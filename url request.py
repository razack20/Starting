import requests
def fun(url):
    r=requests.get(url)
    if r.status_code == 200:
        print("valid")
    else:
        print("invalid")
url=input("enter the link: ")
fun(url)
