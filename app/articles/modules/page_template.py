from flask import Blueprint, render_template, abort, jsonify, send_file
from flask_json import FlaskJSON, JsonError, json_response, as_json

from jinja2 import TemplateNotFound
from ..utils.Navigator import Navigator
from ..utils.JsonHandler import Json
from ..utils.PathHandler import Path
nav = Navigator()
path = Path('app/static/')
json = Json('app/static/json')

def links(): return nav.generate()['breadcrumb']
def siblings(): return nav.generate()['siblings']

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

