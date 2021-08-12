FROM python:2.7
LABLE "maqintainer=Qxx<qxx@qq.com>"
RUN pip install flask
COPY  flask.py /app/
WORKDIR /app
EXPOSE 5000
CMD ["python","flask.py"]