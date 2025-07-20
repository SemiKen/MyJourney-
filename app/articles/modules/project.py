
from .page_template import *
from ..models.Project import ProjectJSON

proj = ProjectJSON(file_path=json.create("project"))

task_page = Blueprint('task_page', __name__,
                        template_folder='templates')

project_page = Blueprint('project_page', __name__,
                        template_folder='templates')

def links(): return nav.generate()['breadcrumb']
def siblings(): return nav.generate()['siblings']

@simple_page.route("/project")
@project_page.route("/")
def myproject():
    projects = proj.to_dict() #["Project1", "Project2", "Project3"]
    nav.set_siblings(None)

    return render_template("pages/project_list.html", 
                           nav_links=links(), nav_siblings=siblings(),
                           projects=projects)

@simple_page.route("/project/<project_name>")
@project_page.route("/<project_name>")
def project(project_name):
    projects = ["Project1", "Project2", "Project3"]
    tasks = [{"name": "Task1"}, {"name": "Task2"}]
    nav.set_siblings(projects)
    return render_template("pages/project_detail.html", nav_links=links(), nav_siblings=siblings(), 
                           project=project_name, tasks=tasks)


@project_page.route("/project/<project_name>/<task_name>")
@task_page.route("/")
def task(project_name, task_name):
    tasks = [{"name": "Task1"}, {"name": "Task2"}]
    nav.set_siblings(tasks)
    return render_template(f'pages/task_detail.html',
                            nav_links=links(), nav_siblings=siblings(),
                            project=project_name,
                            task=task_name)
    # return f"<p>Hello, {task_name}</p>"
