FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1 \ 
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY . . 


## Installing required dependency and remove cache dir 
RUN pip install --no-cache-dir -e . 

### Running the training pipeline file -- Data Ingestion,Data Preprocessing,Model Training
RUN python pipeline/training_pipeline.py

### Front end route like Flask default route 
EXPOSE 5000

CMD ["python","application.py"]

