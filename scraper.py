import requests

site = "https://challenge.curbside.com/"

secret = ""
session = ""


def get_session():
    global session
    request = requests.get(site + "get-session")
    session = request.json()['session']


# def start_session(id):
#     payload = {'Session': id}
#     r = requests.get(site + "start", headers=payload)
#     return r.json()["next"]


def next_url(next):
    get_session()
    if isinstance(next, list):
        for url in next:
            # print("Next is list")
            # print(site + url)
            check_for_secret(site + url)
    else:
        # print("Next is string")
        # print(site + next)
        check_for_secret(site + next)


def check_for_secret(page):
    global secret, session
    # print(session)
    # print(page)
    payload = {'Session': session}
    request = requests.get(page, headers=payload)
    # session = get_session()
    # payload = {'Session': session}
    # request = requests.get(page, headers=payload)
    # print(request)
    if 'next' in request.json():
        next_url(request.json()['next'])
    elif 'secret' in request.json():
        # print("Secret found!", request.json())
        secret += request.json()['secret']
        print("Current secret:", secret)


if __name__ == "__main__":
    get_session()
    # print(session_id)
    payload = {'Session': session}
    r = requests.get(site + "start", headers=payload)
    start = r.json()["next"]
    # print(start)
    next_url(start)
    print("Secret is: ", secret)
