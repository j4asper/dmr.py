from .user_agent import get_user_agent


def get_headers(data: dict = None):
    headers = {
        'User-Agent': get_user_agent(),
    }

    if data:
        headers = headers.update(data)

    return headers
