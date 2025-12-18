import requests

def api_request():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"] ["username"]
        contry = user_data["location"] ["country"]
        return username, contry
    else:
        raise Exception("No data to fetch!!")

def main():
    try:
        user_data =  api_request()
        print(user_data)
    except Exception as s:
        print(str(s))

if __name__ == "__main__":
    main()
