import hashlib
import random

def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()

def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    return render(request, 'login.html', {'hint': hint})



ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def gen_random_code(length=4):
    return ''.join(random.choices(ALL_CHARS, k=length))