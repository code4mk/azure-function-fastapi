# azure-function-fastapi
deploy python fastapi on azure function

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

# sql project enable

set the environment variable 
* `DATABASE_URL`
* `LOAD_SQL_PROJECT` value will be `yes`