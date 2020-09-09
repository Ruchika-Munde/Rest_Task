from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username=request.GET.get('username')
        if username is None:
            return None
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("No such type of user, your credential are invalids")
        return (user,None)



class CustomAuthentication2(BaseAuthentication):
    def authenticate(self, request):
        username=request.GET.get('username')
        key=request.GET.get('key')
        if username is None or key is None:
            return None

        c1=len(key)==7
        c2=key[0]==username[-1].lower()
        c3=key[2]=='z'
        c4=key[4]==username[0]
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("you provided username is invalid, plz provide valid username to access endpoint")
        if c1 and c2 and c3 and c4:
            return (user,None)
        raise AuthenticationFailed("you provided username is invalid, plz provide valid username to access endpoint")

# Requirements: for CustomAuthentication2
#
# 1) Client required to send secret key and username as query parameters.
# 2) Length of key should be 7 characters
# 3) The first character should be lower case alphabet symbol which should be last character of username
# 4) The third character should be 'Z'
# 5) The 5 th character should be first character of username
#
# Eg: username: durga secrete key: a7ZXd98
#
# http://127.0.0.1:8000/api/?username=durga&key=a7ZXd98