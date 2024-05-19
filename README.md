# azure-function-fastapi
Deploy Python FastAPI serverless application on Azure Functions.

* Good project structure

# local development (fastapi)

## venv
```bash
# create virtual environment
python3 -m venv .azure_function_fastapi_venv

# activate virtual environment
source .azure_function_fastapi_venv/bin/activate
```

## run fast api project

```bash
# install packages
pip3 install -r requirements.txt

# run project with uvicorn
uvicorn "fastapi_project.main:app" --reload --port=8000
```

# deploy on production

## vscode extension
<img width="986" alt="Screenshot 2024-05-19 at 5 50 24 PM" src="https://github.com/code4mk/azure-function-fastapi/assets/17185462/6ed26cba-70d8-4c76-8518-5c0b20eaf281">

* [Azure Function Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)

## sql project enable

set the environment variable
* `DATABASE_URL`
* `LOAD_SQL_PROJECT` value will be `yes`