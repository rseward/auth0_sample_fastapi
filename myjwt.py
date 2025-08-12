import jwt
import base64

def decode_unverified_jwt(token: str, algorithm='RS256'):
    # Decode the header without verification
    unverified_header = jwt.get_unverified_header(token)
    print("Unverified Header:", unverified_header)

    # Decode the payload without verification
    # Setting options={"verify_signature": False} allows decoding without a key
    unverified_payload = jwt.decode(token, options={"verify_signature": False})
    print("Unverified Payload:", unverified_payload)

    return unverified_payload

def decode_jwt(token, secret_key=None, algorithm='RS256'):
    """
    Decodes a JWT (JSON Web Token) using Python's jwt library.

    Args:
        token (str): The JWT token to decode.
        secret_key (str): The secret key used to sign the JWT.  This *must* match the key used during signing.
        algorithm (str, optional): The algorithm used to sign the JWT. Defaults to 'HS256'.

    Returns:
        dict: A dictionary containing the decoded claims, or None if decoding fails.
    """
    try:
        decoded_payload = None
        if secret_key is None:
            decoded_payload = decode_unverified_jwt(token, algorithm=algorithm)
        else:
            decoded_payload = jwt.decode(token, key=secret_key, algorithms=algorithm)
        return decoded_payload
    except jwt.exceptions.InvalidSignatureError:
        print(f"Invalid signature for JWT: {token}")
        return None
    except jwt.exceptions.InvalidTokenError:
        print(f"Invalid JWT token: {token}")
        return None
    except Exception as e:
        print(f"An error occurred during decoding: {e}")
        return None

