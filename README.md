## UPDATE :- NO need to go through the later processes, just follow this 3 steps
* download `youtube-dl`
* download `ffmpeg` and add this to system `path`
* run `youtube-dl <url://link.m3u8>`

______________________________________________________________________________________________

To download and merge ts files, enter the file name, master m3u8 link and domain name.

For example,

- file name => "dynamic_programming"
- master m3u8 link => "https://media.prog.io/file/DPSERIES/dynamic_programming.m3u8"
- domain name => "https://media.prog.io/file/DPSERIES/"

Add them as python lists as shown in the config file.

Then in your terminal run ~ `python downloader.py`

Terminal will pop up for resolution value of each video. You can edit the script as per your convenience.

**For decryption see SHELL_COMMANDS.md file**

TODOS

- [ ] chrome extension for a simple bucket list to collect names and links
- [ ] auto domain name extraction
- [ ] Automate sh commands
- [ ] Migrate it to JS for an browser extension

**_Feel free to reach out. Suggestions and collaborations will be highly appreciated._**
