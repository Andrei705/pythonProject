from tinydb import TinyDB, Query

f_template = {"name":"Form template name",
              "user_email":"email",
              "user_phone":"number",
              "user_date":"date",
              "user_text":"text",
              }


db = TinyDB(r'C:\Users\user\PycharmProjects\pythonProject\venv\Web application\db.json')
db.insert(f_template)