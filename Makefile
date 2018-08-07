init:
    pip install pipenv
    pipenv install --dev

test:
    pipenv run py.test tests
    pipenv run migrate.py test
