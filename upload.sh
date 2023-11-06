set -peu  # fail on first error

pandoc --from=markdown --to=rst --output=README.txt README.md
rm -rf dist
python setup.py sdist bdist_wheel
twine upload -r testpypi dist/*
twine upload -r pypi dist/*
