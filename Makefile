up_test_compose:
	docker compose -f docker-compose-local.yaml up -d && sleep 5
migration: up_test_compose
	poetry run alembic upgrade head
test_run: up_test_compose
	#cd dodo && scrapy crawl -O dodospiderTest.json Dodo
	poetry run python3 main.py
lint:
	poetry run pylint --rcfile=.pylintrc $(git ls-files '*.py')
run_fstream:
	poetry run python3 consumer.py
down:
	docker compose -f docker-compose-local.yaml down --remove-orphans