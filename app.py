from flask import Flask, request,jsonify
import logging
from schemas import ZeroShotRequestSchema
from transformers import pipeline
from marshmallow.exceptions import ValidationError
from flasgger import Swagger
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize Flask app
app = Flask(__name__)
Swagger(app)

# Set the logger level for Flask's logger
app.logger.setLevel(logging.INFO)

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

limiter = Limiter(get_remote_address, app=app)

@app.route('/', methods=['GET'])
def health_check():
    """
    Simple health check endpoint
    ---
    responses:
      200:
        description: A successful response
        schema:
          type: object
          properties:
            success:
              type: boolean
            message:
              type: string
    """
    app.logger.info('Main endpoint processing HTTP request')
    return jsonify({"success":True, "message": "Service is healthy"}), 200


@app.route('/classify', methods=['POST'])
@limiter.limit("5 per minute")
def classify():
    """
        Zero-Shot Text Classification Endpoint
        ---
        parameters:
        - name: body
          in: body
          required: true
          schema:
            id: ZeroShotRequest
            required:
              - text
              - labels
            properties:
              text:
                type: string
                description: Text to classify
              labels:
                type: array
                items:
                  type: string
                description: List of possible labels
        responses:
          200:
            description: Classification results
            schema:
              type: object
              properties:
                success:
                  type: boolean
                message:
                  type: string
                data:
                  type: object
                  properties:
                    text:
                      type: string
                    labels:
                      type: array
                      items:
                        type: string
                    classification:
                      type: object
                      properties:
                        label:
                          type: string
                        confidence:
                          type: number
          400:
            description: Invalid input
          429:
            description: Too many requests
          500:
            description: Internal server error
    """
    try:
        data = request.get_json()
        app.logger.info(f"Received data: {data}")
        try:
            validated_data = ZeroShotRequestSchema().load(data)
        except ValidationError as ve:
            app.logger.error(f"Validation error: {ve.messages}")
            return jsonify({"success": False, "message": "Invalid input", "errors": ve.messages}), 400

        result = classifier(
            validated_data['text'],
            validated_data['labels'],
            multi_label=True
        )

        response = {
            "text": validated_data['text'],
            "labels": validated_data['labels'],
            "classification": {
                "label": result['labels'],
                "confidence": result['scores']
            }
        }
        return jsonify({"success":True, "message": "Classification successful", "data": response}), 200
    except Exception as e:
        app.logger.error(f"Error in classification: {e}")
        return jsonify({"success":False, "message": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=50505)