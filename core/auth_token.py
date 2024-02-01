from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

users = User.objects.all()
create_token = Token.objects.create(users)

print(create_token.key)