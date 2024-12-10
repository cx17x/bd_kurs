from jinja2 import Environment, FileSystemLoader
from fastapi.responses import HTMLResponse

env = Environment(loader=FileSystemLoader('templates/user'))
env_adm = Environment(loader=FileSystemLoader('templates/admin'))


def render_template(template_name: str, **context) -> HTMLResponse:
    try:
        template = env.get_template(template_name)
        rendered_html = template.render(**context)
        return HTMLResponse(rendered_html)
    except Exception as e:
        # For production, log the error and return a generic error page
        return HTMLResponse(f'An error occurred: {str(e)}', status_code=500)


def render_template_adm(template_name: str, **context) -> HTMLResponse:
    try:
        template = env_adm.get_template(template_name)
        rendered_html = template.render(**context)
        return HTMLResponse(rendered_html)
    except Exception as e:
        # For production, log the error and return a generic error page
        return HTMLResponse(f'An error occurred: {str(e)}', status_code=500)
