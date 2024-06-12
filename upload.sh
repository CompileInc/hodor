set -peu  # fail on first error

pandoc --from=markdown --to=rst --output=README.txt README.md
rm -rf dist
# requires pypa/build
python -m build
twine upload -r testpypi dist/*
twine upload -r pypi dist/*
