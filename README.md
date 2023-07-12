# yt-dl-mp3-extension

Simple extension for firefox and other browsers to make your playlist building experience smoother. 

## INSTALLATION:

### Serverside

- run:
> docker build --tag dl-mp3 .
> docker run -p 8000:5000 -v {YOUR_DOWNLOAD_DIR_HERE}:/app/downloads -d --restart unless-stopped --name mp3-dl mp3-dl

- This will build and install the dockerized server. Remember to specify your output directory!


### Browser

- In firefox, write "about:debugging" in the search bar
- Click "this firefox"
- Click "Add temporary extension" and point to the manifest.json file. You are now done. 

## USAGE:

- Simply click on the extension window while in a youtube video tab and enjoy!

## TODO:

- [x] dockerize

- [ ] make extension easier to add permanently to browser

- [ ] make extension cross-browser

- [ ] add options to server like download folder, file mirroring, mass renaming
