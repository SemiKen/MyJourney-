import os

from flask import Flask
from app.articles import modules as routes


from pathlib import Path

# Define the __all__ variable
__all__ = ['create_app']

def create_app(test_config=None):
    # สร้างและแก้ไขได้ของ app
    app = Flask(__name__, instance_relative_config=True) # สร้าง app
    app.register_blueprint(routes.simple_page)
    routes.project_page.register_blueprint(routes.task_page, url_prefix='/<project_name>/<task_name>')
    app.register_blueprint(routes.project_page, url_prefix='/project')
    routes.diary_page.register_blueprint(routes.topic_page, url_prefix='/<diary_name>/<topic_name>')
    app.register_blueprint(routes.diary_page, url_prefix='/diary')

    routes.api_page.register_blueprint(routes.file_page, url_prefix='/<file_extension>')
    app.register_blueprint(routes.api_page, url_prefix='/api')

    # Config หรือปรับแต่ง app ได้ตามใจอยาก เหมือนกำหนดค่าเริ่มต้น
    # Secret key เหมือนกับคีย์เข้ารหัส และ 
    # app.config.from_mapping(
    #     SECRET_KEY='devILovingIceCream',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # โหลดค่าตั้งค่าเริ่มต้นจาก ไฟล์ config.py
        # app.config.from_pyfile('config.py', silent=True)
        print("Default Config Loaded!")
    else:
        # load the test config if passed in
        if Path(test_config).is_file():
            app.config.from_pyfile(test_config, silent=True)
        else:
            app.config.from_mapping(test_config)
        print("Config Loaded!")


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app