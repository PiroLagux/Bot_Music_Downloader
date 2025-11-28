from parse_hitmos.entered_tracks import EnteredTrack
import requests

def download_music(name, chat_id):
	result = EnteredTrack(name, 1).get_url_down
	r = requests.get(result[0])
	with open(f'{chat_id}.mp3', 'wb') as f:
		f.write(r.content)