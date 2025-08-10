# import jwt
# from datetime import datetime, timedelta

# SECRET_KEY = 'your-secret-key'

# def create_jwt(user):
#     payload = {
#         'id': user.id,
#         'username': user.username,
#         'exp': datetime.utcnow() + timedelta(hours=1),
#         'iat': datetime.utcnow(),
#     }
#     token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
#     return token

# def decode_jwt(token):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         return payload
#     except jwt.ExpiredSignatureError:
#         return None
#     except jwt.InvalidTokenError:
#         return None