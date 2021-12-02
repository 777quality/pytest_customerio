from pytest import fixture
from requests import Session
import pytest
import json
import requests
from requests.sessions import session

@pytest.fixture
def logged_in_session(scope="session"):
# Mimic navigating to the landing page (actions such as this help avoid server ban)   
    login_sso_headers = {
    'authority': 'fly.customer.io', 
    'method': 'GET',
    'path': '/v1/login_sso_info?email=dalejohnfixter%40gmail.com',
    'scheme': 'https',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://fly.customer.io/login',
    'accept-language': 'en-US,en;q=0.9,en-GB;q=0.8',
    'cookie': '_gcl_au=1.1.394485335.1635952830; ajs_anonymous_id=0049a253-258f-4a16-b10e-b7c2ba8c4673; ember_simple_auth-session-expiration_time=604800; _fbp=fb.1.1636567352500.340112651; __stripe_mid=c20f39ec-981c-424e-baeb-3ea24d53c917df4cea; fs_uid=rs.fullstory.com#MVQPJ#6564938040975360:5360799675031552#d05ae9ae#/1668103663; tk_ai=DMQzo003fQlMJ4MpF2c3F%2Bz%2F; _ga=GA1.2.792098883.1635952830; _gid=GA1.2.578777594.1638295596; __stripe_sid=b0e89aa3-49a8-4470-8f96-5e8676f6309378f325; _ga_L97TR1N1TG=GS1.1.1638359865.15.0.1638359865.60; ember_simple_auth-session=%7B%22authenticated%22%3A%7B%7D%7D; _gat_UA-28175335-1=1',
}

    login_sso_params = (
    ('email', 'dalejohnfixter@gmail.com'),
)

    with requests.Session() as s:
        login_sso_url = 'https://fly.customer.io/v1/login_email'
        r = s.get(login_sso_url, headers=login_sso_headers, params=login_sso_params)
        print(r)
        assert r.status_code == 200
        
    login_email_headers = {
    'authority': 'fly.customer.io',
    'method': 'POST',
    'path': '/v1/login_email',
    'scheme': 'https',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': '*/*',
    'content-type': 'application/json',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://fly.customer.io',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://fly.customer.io/login/password',
    'accept-language': 'en-US,en;q=0.9,en-GB;q=0.8',
    'cookie': '_gcl_au=1.1.394485335.1635952830; ajs_anonymous_id=0049a253-258f-4a16-b10e-b7c2ba8c4673; ember_simple_auth-session-expiration_time=604800; _fbp=fb.1.1636567352500.340112651; __stripe_mid=c20f39ec-981c-424e-baeb-3ea24d53c917df4cea; fs_uid=rs.fullstory.com#MVQPJ#6564938040975360:5360799675031552#d05ae9ae#/1668103663; tk_ai=DMQzo003fQlMJ4MpF2c3F%2Bz%2F; _ga=GA1.2.792098883.1635952830; _gid=GA1.2.578777594.1638295596; __stripe_sid=b0e89aa3-49a8-4470-8f96-5e8676f6309378f325; _ga_L97TR1N1TG=GS1.1.1638359865.15.0.1638359865.60; _gat_UA-28175335-1=1; ember_simple_auth-session={%22authenticated%22:{}}',
}

    login_email_data = '{"email":"dalejohnfixter@gmail.com","password":"Nt3FQb3Uuqd#Rn3","ga_client_id":"792098883.1635952830"}'

# POST login
    r = s.post('https://fly.customer.io/v1/login_email', data= login_email_data, headers= login_email_headers)
    print(r.text)

# Extract auth token from response and set in auth headers    
    AUTH_TOKEN = json.loads(r.text)['access_token']
    print(AUTH_TOKEN)
    AUTH_HEADERS = {'authorization': 'Bearer {}'.format(AUTH_TOKEN)}
    print(AUTH_HEADERS)

    return AUTH_HEADERS