all:
	@echo "make lint	- Check code with flake8"
#	@echo "make test	- Run tests"
	@echo "make db		- Run only db container"
	@echo "make local	- Run app locally"
	@echo "make alembic	- Run alembic migrations"
	@exit 0

lint:
	flake8 app --count --exit-zero --exclude=app/db/migrations/ --max-complexity=10 --max-line-length=127 --statistics
	#flake8 tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

#test:
#	pytest --disable-warnings

db:
	docker-compose up -d

local:
	uvicorn app.main:app --reload --host 0.0.0.0

dbconn:
	psql -h 127.0.0.1 -U postgres -p 5432 common
