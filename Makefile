test_run:
	cd dodo && scrapy crawl -O dodospiderTest.json Dodo
lint:
	poetry run pylint --rcfile=.pylintrc $(git ls-files '*.py')
