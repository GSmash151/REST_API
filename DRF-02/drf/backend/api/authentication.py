# drf/backend/api/authentication.py
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

class TokenAuthentication(BaseTokenAuth):
  keyword = 'Bearer'