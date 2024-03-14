# Last.fm Scrobbler Rewritten
This is essentially the exact same as [my other version](https://github.com/cantwont/scrobbler) except it (currently) excludes the Discord Webhook feature. This version is better because it supports Spotify playlists instead of having a .json file for it. See below on how to use this

# Config.json
Read after this codeblock on how to obtain these values
```txt
{  
  "CLIENT_ID": "",  
  "CLIENT_SECRET": "",  
  "PLAYLIST_ID": "",  
  
  "LASTFM_API_KEY": "",  
  "LASTFM_SHARED_SECRET": "",  
  
  "LASTFM_USERNAME": "",  
  "LASTFM_PASSWORD": ""  
}
```
Client ID and Client Secret are both found at [this website](https://developer.spotify.com/dashboard). When making an app, input any information you want except you need to check the Web API box under "Which API/SDKs are you planning to use?" Playlist ID you get from copying your playlist URL and only inputting this part: 
![enter image description here](https://cdn.discordapp.com/attachments/1118768539520741458/1217679527472271432/image.png?ex=6604e76e&is=65f2726e&hm=1dbf8a8957389058bc4d64d6ddfe1199724ac1d4f7d00b1a6872385b5291cee5&)
Last FM API Key and Shared Secret are both found at [this website here.](https://www.last.fm/api/account/create) The last 2 values are self explanatory.

This scrobbler will wait 30 (with a few extra seconds) to ensure safety. You are easily able to automate/bot 10s of thousands of scrobbles with this, as I have on one of my alternate accounts. Please open an issue if anything happens!
