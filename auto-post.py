import urllib, json,sys, facebook, time

page_user_name = str(sys.argv[1])
target_likes = int(sys.argv[2])
post = str(sys.argv[3])

ACCESS_TOKEN = "YOUR ACCESS TOKEN HERE"

url = "https://graph.facebook.com/%s" %page_user_name
response = urllib.urlopen(url);
data = json.loads(response.read())

likes = int(data["likes"])
page_id = data["id"]

access_token_url ="https://graph.facebook.com/me/accounts?access_token=%s" %ACCESS_TOKEN
access_token_response = urllib.urlopen(access_token_url);
access_token_data = json.loads(access_token_response.read())
page_access_token = ""
for page in range(len(access_token_data["data"])):
	if page_id == access_token_data["data"][page]["id"]:
		page_access_token = access_token_data["data"][page]["access_token"]

while True:
    if likes >= target_likes:
		graph = facebook.GraphAPI(page_access_token)
		graph.put_object(page_id, "feed", message=post)
		exit()
    time.sleep(60)
