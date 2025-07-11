# squid-game-api
an API containing JSON content about Squid Game.

![sg](sg-api.png)
## Seasons 
   - [Season 1](https://github.com/stainlesteel/squid-game-api/tree/main/s1)
   - [Season 2](https://github.com/stainlesteel/squid-game-api/tree/main/s2)
### Why no season 3?
Season 3 is just the second half of Season 2. As such, all contents of season 3 are added into season 2, including the episodes. 
When running the server, season 3 is added and you can access it's characters and episodes, but they will come from Season 2's folder.
# Run
## GNU/Linux/BSD && MacOS && Windows
Here are the instructions to run on any GNU-based Linux or BSD system, as well as MacOS and Windows, albeit maybe with some different terminal commands.
1. Download the files (either via, git clone "{github .git url}" or  downloading the zip)
2. Go to the root of the folder
3. Open a terminal (zsh, bash, fish, .etc)
4. Have these python dependenices installed: fastapi, uvicorn (via pip3)
5. `uvicorn main:app --reload --port 2456 # or whatever other port`
## Docker
Coming soon..

# Contribute
There are some issues that should be fixed below:
1. Some JSON files have /n or other typos made by AI. I won't go through all of these (912) files but if you found an error, you can open an issue so I can fix it or open a PR so I can approve it.
2. You could also provide a Dockerfile for docker
