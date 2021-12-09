# azureml-sample-iris

This repo is a work in progress, not ready for use.

## Setting up a local environment

- Install conda
- Install Azure CLI
- Conda create environment

## Using the CLI

Train model:
```
az ml job submit --file azureml/train.yml --iterations=10000
```

Register model from the last local run:
```
az ml model create --file azureml/registermodel.yml
```

Deploy model:
```
az ml online-endpoint create --file azureml/deploy.yml
```



