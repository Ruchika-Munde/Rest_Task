import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'

# def get_resources(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resources()

# def create_resources():
#     new_emp={
#         'eno':400,
#         'ename':'shiva',
#         'esal':4000,
#         'eaddr':'pune'
#     }
#     r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(r.status_code)
#     print(r.json())
# create_resources()

def update_resource(id):
    new_data={
        'id':id,
        # 'eno':600,
        'ename':'RUCHA ',
        'esal':80000,
        #'eaddr':'Nagpur',
    }
    r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(r.status_code)
    print(r.json())
update_resource(3)

# def delete_resource(id):
#     data={
#         'id':id,
#     }
#     r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(r.status_code)
#     print(r.json())
# delete_resource(4)