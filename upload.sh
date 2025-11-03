set -peu  # fail on first error

pandoc --from=markdown --to=rst --output=README.txt README.md
rm -rf dist
# requires hatch
uvx hatch build
uvx hatch publish
