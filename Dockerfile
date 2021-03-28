#FROM public.ecr.aws/lambda/python:3.8
FROM python:3.8

WORKDIR /ep

COPY . /ep

RUN pip install pandas
RUN pip install requests
RUN pip install openpyxl
RUN pip install boto3
RUN pip install smart_open
RUN pip install python-string-utils

EXPOSE 8000

CMD ["python", "src/main.py"]

