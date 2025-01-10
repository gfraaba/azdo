# *** On Windows machine first set a system environment variable called PLATFORM and set it to "linux/amd64"

# *** In macOS, add a new environment variable (~/.zshrc) called PLATFORM and set it to "linux/arm64":
## Steps 

1. **Open Zsh Terminal**:
    - Run `code ~/.zshrc`
2. **Use VS Code to update ~/.zshrc by adding the following line**: 
    - Add new line: `export PLATFORM="linux/arm64"`
3.  **Back to Zsh Terminal to Source the Just Updated ~/.zshrc**: 
    - Run `source ~/.zshrc`
    - Run `echo $PLATFORM`
4. **Open Pwsh Terminal**:
   - Run `echo $env:PLATFORM`

***NOTE: Adding a new environment variable in ~/.zshrc will make it available to all other shells as well!***

***Or, you can just skip these steps on macOS by using the default 'linux/arm64' if the 'localEnv:PLATFORM' results in null ***
*** Here's the syntax: `"${localEnv:PLATFORM:linux/arm64}"` ***

# azdo

# Option #1: Run these in the host without needing to open VS Code and attach it to the Dev Container

cd ~/github/repos/azdo
#docker system prune -a
docker-compose up --build
docker-compose down

# Option #2: Run these in the terminal in Visual Studio Code attached to the Dev Container

# First, Run the Backend:
cd /workspaces/azdo/api
python3 -m unittest tests/test_projects.py
python3 run.py
#Browse to: http://localhost:5500/api/projects

# Next, Run the Frontend (in a new terminal)
### Development
cd /workspaces/azdo/dashboard/
npm install --save-dev @babel/plugin-proposal-private-property-in-object
npm start

### Production **DIDN'T WORK!!!!!!!
<!-- cd /workspaces/azdo/dashboard/
npm ci --omit=dev
npm run build
npm install --save-dev @babel/plugin-proposal-private-property-in-object
npm install -g serve
serve -s build -l 3000 -n -->