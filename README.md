# azdo

# Option #1: Run these in the host

cd ~/github/repos/azdo
docker system prune -a
docker-compose up --build
docker-compose down

# Option #2: Run these in the terminal in Visual Studio Code attached to the Dev Container
Frontend:
cd /workspaces/azdo/dashboard/
npm ci --omit=dev
npm run build
npm install -g serve
serve -s build -l 3000 -n

npm start

Backend:
cd /workspaces/azdo/api
python3 -m unittest tests/test_projects.py
python3 run.py