from fastapi import Request
from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, ValidationError
from sqlalchemy import desc
from urllib.parse import urlparse

async def the_query(request: Request, name = None) -> Dict[str, str]:
    data = {}
    
    if request.query_params:
        data =  request.query_params
    elif request.headers.get("Content-Type") == "application/json":
        data = await request.json()
    else:
        data = await request.form()
    
    if name:
      return data.get(name)
    else:
      return data


async def validate_data(data: Dict[str, Any], model: BaseModel) -> Dict[str, Union[str, Dict[str, Any]]]:
    output = {'status': 'valid'}
    
    try:
        instance = model(**data)
        output['data'] = instance.dict()
    except ValidationError as e:
        # If validation fails, return status as invalid and the validation errors
        output['status'] = 'invalid'
        output['errors'] = e.errors()
        
    return output


def the_sorting(request, query):
        sort_params = request.query_params.get("sort")
        
        if sort_params:
            sort_fields = sort_params.split(",")
            ordering = []
            for field in sort_fields:
                if field.startswith("-"):
                    ordering.append(desc(field[1:]))
                else:
                    ordering.append(field)
            query = query.order_by(*ordering)
            
        return query
    
def app_path(path_name = None):
    from pathlib import Path
    the_path = str(Path(__file__).parent.parent)
    
    if path_name:
        the_path = f'{the_path}/{path_name}'
        
    return the_path
  

def paginate(request: Request, query, serilizer, the_page: int = 1, the_per_page: int = 10, wrap='data'):
    """Paginate the query."""
    
    page = int(request.query_params.get('page', the_page))
    per_page = int(request.query_params.get('per_page', the_per_page))
    
    total = query.count()
    last_page = (total + per_page - 1) // per_page
    offset = (page - 1) * per_page
    paginated_query = query.offset(offset).limit(per_page).all()

    data = [serilizer.from_orm(item) for item in paginated_query]

    base_url = str(request.base_url)
    
    full_path = str(request.url)
    parsed_url = urlparse(full_path)
    path_without_query = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
    
    first_page_url = f"{path_without_query}?page=1&per_page={per_page}"
    last_page_url = f"{path_without_query}?page={last_page}&per_page={per_page}"
    next_page_url = f"{path_without_query}?page={page + 1}&per_page={per_page}" if page < last_page else None
    prev_page_url = f"{path_without_query}?page={page - 1}&per_page={per_page}" if page > 1 else None

    return {
        'total': total,
        'per_page': per_page,
        'current_page': page,
        'last_page': last_page,
        'first_page_url': first_page_url,
        'last_page_url': last_page_url,
        'next_page_url': next_page_url,
        'prev_page_url': prev_page_url,
        'path': base_url,
        'from': offset + 1 if data else None,
        'to': offset + len(data) if data else None,
        wrap: data
    }