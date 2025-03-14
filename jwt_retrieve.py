import jwt, datetime, uuid

# Enter Credentials from the Connnected App
connectedAppClientId = "CLIENT_ID"
connectedAppSecretId = "SECRET_ID"
connectedAppSecretKey = "SECRET_KEY"

# # Enter the username of the user logging in
user = "USERNAME_LOGGING_IN"

token = jwt.encode(
    {
        "iss": connectedAppClientId,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
        "jti": str(uuid.uuid4()),
        "aud": "tableau",
        "sub": user,
        "scp": ["tableau:views:embed"]
    },
        connectedAppSecretKey,
        algorithm = "HS256",
        headers = {
        'kid': connectedAppSecretId,
        'iss': connectedAppClientId
        }
)

print("JWT for logging in, this can be checked using a JWT debugger like at https://jwt.io:\n", token)