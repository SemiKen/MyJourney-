from .page_template import *

diary_page = Blueprint('diary_page', __name__,
                        template_folder='templates')


topic_page = Blueprint('topic_page', __name__,
                        template_folder='templates')

PAGE_URL = "diary"

@simple_page.route("/diary")
@diary_page.route("/")
def mydiary():
    diarys = ["Diary1", "Diary2", "Diary3"]
    return render_template(f'pages/diary_list.html'
                           ,page_url=PAGE_URL, diarys=diarys)

@simple_page.route("/diary/<diary_name>")
@diary_page.route("/<diary_name>")
def diary(diary_name):
    test_topic = [
        {"name": "Topic1"},
        {"name": "Topic2"},
        {"name": "Topic3"},
    ]
    return render_template(f'pages/diary_detail.html'
                        ,page_url=PAGE_URL
                        ,diary=diary_name
                        ,topics=test_topic)


@diary_page.route("/<diary_name>/<topic_name>")
@topic_page.route("/")
def topic_blog(diary_name, topic_name):
    return render_template(f'pages/topic_detail.html',
                           page_url=PAGE_URL,
                           diary=diary_name,
                           topic=topic_name)
    # return f"<p>Topic '{topic_name}' in Diary '{diary_name}'</p>"