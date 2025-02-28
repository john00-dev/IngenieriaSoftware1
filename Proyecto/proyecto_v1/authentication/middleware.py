import jwt
import requests
from django.http import JsonResponse
from django.conf import settings

class Auth0Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/public/"):  
            return self.get_response(request)

        auth = request.headers.get("Authorization", None)
        if not auth:
            return JsonResponse({"error": "Token requerido"}, status=401)

        token = auth.split(" ")[1]

        try:
            jwks = requests.get(f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json").json()
            signing_key = jwt.algorithms.RSAAlgorithm.from_jwk(jwks["keys"][0])

            payload = jwt.decode(
                token,
                signing_key,
                algorithms=["RS256"],
                audience=settings.API_IDENTIFIER,
                issuer=settings.JWT_ISSUER,
            )

            request.user = payload

        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token expirado"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Token inválido"}, status=401)

        return self.get_response(request)
