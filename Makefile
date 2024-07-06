.PHONY: fmt style db-start db-stop db-shell

fmt:
	ruff format

style:
	mypy htmx_table
	ruff check

db-start:
	docker-compose up db -d

db-stop:
	docker-compose down

db-shell:
	PGPASSWORD=test psql -U cruds -h localhost -p 5432 -d cruds
