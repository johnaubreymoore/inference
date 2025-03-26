FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install PyTorch (compatible with your Python version and OS)
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Preload the model during the build process
RUN python -c "\
from transformers import pipeline;\
classifier = pipeline(\
    'zero-shot-classification',\
    model='facebook/bart-large-mnli'\
)\
"

COPY . /app

EXPOSE 50505

CMD ["gunicorn", "--chdir", "/app", "--bind", "0.0.0.0:50505", "--access-logfile", "-", "--error-logfile", "-", "app:app"]