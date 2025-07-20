from .page_template import *

@simple_page.route("/")
@simple_page.route("/overview")
def overview():
    return render_template('pages/overview.html')


@simple_page.route("/<user>")
def user(user):
    try:
        return render_template(f'pages/{user}.html')
    except TemplateNotFound:
        abort(404)

@simple_page.route("/recently")
def recently():
    return "<p>Hello, Recently!</p>"

@simple_page.route("/calender")
def calender():
    return "<p>Hello, Calender!</p>"

@simple_page.route("/setting")
def setting():
    return "<p>Hello, Setting!</p>"


@simple_page.route("/favorite")
def favorite():
    return "<p>Hello, My Saving!</p>"

@simple_page.route("/notification")
def notification():
    return "<p>Hello, Notification!</p>"

@simple_page.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404