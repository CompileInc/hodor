pandoc --from=markdown --to=rst --output=README.txt README.md
python setup.py sdist upload -r pypi
