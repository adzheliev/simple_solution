FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ARG STRIPE_PUBLISHABLE_KEY
ARG STRIPE_SECRET_KEY
ARG DJANGO_SECRET_KEY

ENV STRIPE_PUBLISHABLE_KEY=$STRIPE_PUBLISHABLE_KEY
ENV STRIPE_SECRET_KEY=$STRIPE_SECRET_KEY
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY

WORKDIR /app/simple_solution

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]