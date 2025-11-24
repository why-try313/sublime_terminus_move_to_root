# SublimeText:Terminus extension

This simple script allows to start Terminus on a project root via `.env` file setting a `Terminus_ROOT` key

### Installation
1. Grab the python script and save it in your Sublime User folder (Preferences > Browse Packages... > "User" folder)
2. In your project, set an `.env` file in the root of your projects directories with your `Terminus_ROOT` path
   ```.env
   # .env
   Terminus_ROOT = "/my/root/dir/for/this/project"
   ```
3. Open Terminus in Sublime Text, if the current file you're working on has an `.env` file with the `Terminus_ROOT` key, Terminus will move to that root location
