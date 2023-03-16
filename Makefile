app:
	docker-compose -f docker-compose.yml down; docker-compose run --service-ports app;
migrations:
	docker-compose run app python manage.py makemigrations
migrate:
	docker-compose run app python manage.py migrate
supperuser:
	docker-compose run app python manage.py createsuperuser
info:
	docker-compose run app python manage.py
build:
	docker-compose build app
bash:
	docker-compose run app bash
requirements:
	docker-compose run app pip freeze > requirements.txt