init:
	pip install pipenv
	pipenv install --dev

test:
	# pipenv run py.test
	pipenv run manage.py test
