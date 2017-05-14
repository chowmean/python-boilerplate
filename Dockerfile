FROM python:2.7
RUN pip install -r requirements.txt
CMD ["python","./run.py"]