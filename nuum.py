import requests
#This is my latest project. I'm tired of looking for ideas for libraries. In the future I will be involved in investments and my telegram channel.
class Client():
	def __init__(self):
		self.api="https://nuum.ru/api"
		self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.user_id=None
	def login(self,email,password):
		data={"user_email":email,"user_password":password,"enable_wasd_news":False}
		req=requests.post(f"{self.api}/v2/auth/tokens",json=data,headers=self.headers)
		self.headers['Cookie']=req.headers['Set-Cookie']
		self.user_id=self.account_info()['result']['user_id']
		return req.json()
	def follow(self,id):
		return requests.put(f"{self.api}/channels/{id}/followers",headers=self.headers).json()
	def unfollow(self,id):
		return requests.delete(f"{self.api}/channels/{id}/followers",headers=self.headers).json()
	def categories_list(self):
		return requests.get(f"{self.api}/v2/categories",headers=self.headers).json()
	def feed_clips(self,limit,offset,category:str="all"):
		return requests.get(f"{self.api}/v2/main/clips/feed?category={category}&limit={limit}&offset={offset}",headers=self.headers).json()
	def get_notifications(self):
		return requests.get(f"{self.api}/v3/notifications/bell/status",headers=self.headers).json()
	def featured_members(self):
		return requests.get(f"{self.api}/v2/recommendations/channels-lists/FEATURED/members",headers=self.headers).json()
	def my_followed_channels(self,limit,offset):
		return requests.get(f"{self.api}/profiles/current/followed-channels?limit={limit}&offset={offset}&order_type=ACTIVITY",headers=self.headers).json()
	def submit_comment(self,text,videoId,parentId:int=None):
		data={"text":text}
		if parentId:data["parentId"]=parentId
		return requests.post(f"{self.api}/v3/comments/{videoId}",json=data,headers=self.headers).json()
	def account_info(self):
		return requests.get(f"{self.api}/v2/profiles/current",headers=self.headers).json()
	def comment_info(self,parentId,videoId,limit):
		return requests.get(f"{self.api}/v3/comments/{videoId}?limit={limit}&parent_id={parentId}",headers=self.headers).json()
	def edit_profile(self,description:str=None,name:str=None):
		data={}
		if name:data["channel_name"]=name
		if description:data["channel_description"]=description
		return requests.put(f"{self.api}/channels/{self.user_id}",json=data,headers=self.headers).json()
	def search_channels(self,limit,offset,q):
		return requests.get(f"{self.api}/search/channels?limit={limit}&offset={offset}&search_phrase={q}",headers=self.headers).json()