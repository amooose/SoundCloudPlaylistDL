# SoundCloudPlaylistDL
Downloads your entire desired playlist automatically

A small script to automatically download all tracks from a soundcloud.com playlist.  
A Client_id key is required to use this (more info below).

## Installation

#### Requirements
* `pip install mechanize`
* `pip install wget`
* `pip install beautifulsoup4`

### Getting a Client_id key
* Navigate to soundcloud, and hit f12 to enable developer tools in Chrome, and go into the Network tab.
* Type in the network filter client_id, and hit play on any song
* Multiple entries will apear, containing client_id=__________
* An example would look like this (Select only the bold, dont literally use the key shown below, it wont work.)
* api-v2.soundcloud.com/me/play-history?client_id=**pToSDVYjhMm3OkPBnOlGGGfEBFrYx4fz**&app_version=1575380558&app_locale=en

### Usage
* Paste your key into the scPlaylistDL.py at CLIENT_ID = ""
* Run the script and input your playlist URL

### Bugs
* This downloader uses a separate site to generate a download link, occasionally the download will hang for 5-10 seconds, it will automatically retry.
* Some songs will refuse to be downloaded, this cannot be fixed at the moment  
(Every website is unable to download these specific problem songs).  
A list of these songs will be generated and shown at the end.
