# *** On Windows machine first set a system environment variable called PLATFORM and set it to "linux/amd64"

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

# Next, Run the Frontend
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