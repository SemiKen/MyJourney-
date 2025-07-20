from .page_template import *

api_page = Blueprint('api_page', __name__,
                        template_folder='templates')

# json_page = Blueprint('json_page', __name__,
#                         template_folder='templates')

file_page = Blueprint('file_page', __name__,
                        template_folder='templates')

@simple_page.route("/api")
@api_page.route("/")
def api():
    folder_list = path.get_children(full_path=False)
    return render_template("pages/api.html", 
                              nav_links=links(), nav_siblings=siblings(),
                              folders = folder_list)
    # return "<p>Hello, API!</p>"

@api_page.route("/<file_extension>")
@file_page.route("/")
def file_list(file_extension):
    if file_extension == None:
        return
    nav.set_siblings(path.get_children(full_path=False))
    current_folder = path.search_folders(file_extension)[0]
    files = path.get_children(full_path=False, path=current_folder)
    return render_template("pages/file_list.html",
                           nav_links=links(), nav_siblings=siblings(),
                           files=files)


@file_page.route("/<file_name>.<ext>")
def file_view(file_extension, file_name, ext):
    if ext == "json":
        return json.to_dict(file_name)
    elif ext == "txt":
        return send_file(f"data/{file_name}.txt")
    elif ext == None:
        return f"<p>Hello, {file_name}!</p>"
        pass
