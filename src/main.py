from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/javascript/tasks/one')
def javascript_tasks_one(request: Request):
    return templates.TemplateResponse(name="second.html", request=request)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8000)