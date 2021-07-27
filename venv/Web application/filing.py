from tinydb import TinyDB, Query

f_template = {"name":"Form template name",
              "Field_name1":"email",
              "Field_name2":"phone",
              "Field_name1":"date",
              "Field_name1":"text",
              }


db = TinyDB(r'C:\Users\user\PycharmProjects\pythonProject\venv\Web application\db.json')
db.insert(f_template)
db.all()