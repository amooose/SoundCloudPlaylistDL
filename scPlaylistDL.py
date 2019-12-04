import os
import mechanize,re
import wget
from bs4 import BeautifulSoup
count = 0
unable = []

def main():
	retry = 0
	count = 0
	status = 0
	try:
		import requests
	except ImportError:
		print ("Missing requests/mechanize/beautifulsoup4")
		exit()

	CLIENT_ID = ""
    if(len(CLIENT_ID)<1):
        print("No client_id!")
        exit()
	URL = input("Copy and paste playlist link here: ")
	API_LINK = 'http://api.soundcloud.com/resolve.json?url=' + URL + '&client_id=' + CLIENT_ID

	r = requests.get(API_LINK)
	data = r.json()
	playlistName = data["title"] + ""

	for tracks in data["tracks"]:
		name = tracks["title"]
		link = tracks["permalink_url"]
		print("\n"+name + " ("+str(count+1)+"/"+str(len(data["tracks"]))+")")
		count+=1

		try:
			downloadSong(link,name,retry)
		except:
			if(retry == 5):
				print("Cant connect! Bad song url/host down?")
				return 0
			while retry <= 5 and status != 1:
				print("retrying.. ("+str(retry+1)+"/5)")
				status = downloadSong(link,name,retry)
				retry+=1
				
		retry = 0
		status = 0

	print("\n"+playlistName + " Done!")
	if(len(unable)>0):
		printErrors()

def printErrors():
	print("\n"+str(len(unable))+" songs API can't download:")
	for a in unable:
		print(a)

def downloadSong(url,name,retry):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(False)
	br.addheaders = [('User-agent', 'Firefox')]             
	br.open( "https://sclouddownloader.net/" )

	br.select_form(nr=0)
	br["sound-url"] = url

	res = br.submit()
	content = res.read()
	soup = BeautifulSoup(content, 'html.parser')
	songUrl = soup.find_all("a", href=re.compile("sndcdn.com"))

	try:
		url = songUrl[0]['href']
	except:
		unable.append(name)
		print("Song can't be downloaded. (Some songs just refuse, download via other methods.)")
		return 0

	wget.download(url, get_valid_filename(name)+'.mp3')
	return 1

def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

if __name__ == '__main__':
    main()
