FROM python:3.10

COPY ./ /source/
RUN pip install --no-cache-dir --upgrade -r /source/requirements.txt

# set environment to production to disable docs
ENV APP_BACKEND_ENV=prod 

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]