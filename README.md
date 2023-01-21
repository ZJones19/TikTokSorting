# TikTokSorting
App for organizing tiktoks into useful categories  

## For Developers
***Extremely Important***:  
Before pushing any changes, makes sure you have ran the following command:  
`git update-index --skip-worktree config/auth.json`  

This prevents `auth.json` from being tracked. Still, before pushing make it is a best practice to quickly run `git status` to see what files have been staged. If `auth.json` is staged, remove it by running:  
`git reset -- config/auth.json`  
This is *crucial* because pushing credentials to a repository is never a good practice. They are private and should only be added on your local machine.  


### Requirements  
Make sure latest version of Python3 is installed.  
Run `pip install -r requirements.txt` to install all dependencies.  

### How To Run
Insert proper creds in `config/auth.json`  
Run script with `python -m flask --app app run`  
