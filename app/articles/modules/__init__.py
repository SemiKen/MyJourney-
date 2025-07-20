__all__ = ["simple_page", 
           "project_page", "task_page",
           "diary_page", "topic_page",
           "api_page", "file_page"]


from .default import simple_page
from .project import project_page, task_page
from .diary import diary_page, topic_page
from .api import api_page, file_page