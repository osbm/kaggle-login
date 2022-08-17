# A github action to login to kaggle


You need to set the username and the key as repository secrets.

### example usage:

```yaml

on: 
  workflow_dispatch: # manually trigger the action
  push: # automatically trigger the action when a new commit is pushed to the repo


jobs:
  testitout:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout the repository
        uses: actions/checkout@v3

      - name: Login to Kaggle
      - uses: osbm/kaggle-login@test-composite
        with:
          KAGGLE_USERNAME: {{ secrets.KAGGLE_USERNAME }}
          KAGGLE_KEY: {{ secrets.KAGGLE_KEY }}

      - name: Use kaggle api to list datasets
        run: |
          kaggle datasets list

```