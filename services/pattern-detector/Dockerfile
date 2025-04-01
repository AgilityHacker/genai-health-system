FROM python:3.10-slim
WORKDIR /app
COPY . /app
COPY ../../requirements.common.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
CMD ["python", "pattern_detector_service.py"]
