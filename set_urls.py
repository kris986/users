from urllib.parse import urljoin
UI_URL = 'http://users.bugred.ru/tasks/'
URL_LIST = 'http://users.bugred.ru/tasks/rest/list'
API_URL = 'http://users.bugred.ru/tasks/rest/'
REGISTER_PATH = 'doregister'
CREATE_COMPANY = 'createcompany'
CREATE_USER = 'createuser'


def go_to_url(method):
    method_url = urljoin(API_URL, method)
    return method_url

# deletetask,addtaskincron,updatetask,createtask,deleteuser,updateUseronefield,fullupdateuser,dologin,getuser,doregister

