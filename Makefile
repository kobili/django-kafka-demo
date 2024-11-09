build:
	docker compose build

run:
	docker compose up

destroy:
	docker compose stop
	docker compose down -v --rmi local

createsuperuser:
	docker compose -f compose.yaml run --rm django python /app/django-app/manage.py createsuperuser

app ?=
makemigrations:
	docker compose run --rm django python /app/django-app/manage.py makemigrations ${app}
mm: makemigrations

migrate:
	docker compose run --rm django python /app/django-app/manage.py migrate
m: migrate

createsuperuser-other:
	docker compose -f compose.yaml run --rm django-other python /app/django-app/manage.py createsuperuser

makemigrations-other:
	docker compose run --rm django-other python /app/django-app/manage.py makemigrations ${app}
mm-other: makemigrations-other

migrate-other:
	docker compose run --rm django-other python /app/django-app/manage.py migrate
m-other: migrate-other

kafka-consumer:
	docker compose exec kafka ./opt/kafka/bin/kafka-console-consumer.sh --topic ${topic} --from-beginning --bootstrap-server kafka:9092
