import Cookie
import cookielib

from lixian_config import LIXIAN_DEFAULT_COOKIES


s = raw_input('Paste cookie here:\n')
cookie = Cookie.SimpleCookie()
cookie.load(s)

domain = '.xunlei.com'

cookiejar = cookielib.LWPCookieJar()
for k, v in cookie.items():
    c = cookielib.Cookie(version=0, name=k, value=v.value, port=None, port_specified=False, domain=domain, domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={}, rfc2109=False)
    cookiejar.set_cookie(c)

cookiejar.save(LIXIAN_DEFAULT_COOKIES, ignore_discard=True)
