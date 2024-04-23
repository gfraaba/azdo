def get_mock_data():
    mock_data = []

    project_names = ["Apollo", "Mercury", "Gemini", "Voyager", "Pioneer", "Challenger", "Discovery", "Endeavour", "Atlantis", "Enterprise"]
    repo_names = ["Orion", "Centaurus", "Draco", "Pegasus", "Phoenix", "Lyra", "Hercules", "Cassiopeia", "Perseus", "Andromeda"]
    branch_names = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa"]
    commit_messages = ["Initial commit", "Added feature", "Fixed bug", "Refactored code", "Updated documentation", "Improved performance", "Added tests", "Fixed typo", "Removed unused code", "Updated dependencies"]

    for i in range(10):  # Generate 10 projects
        project = {
            'projectID': str(i+1),
            'projectName': project_names[i],
            'repos': []
        }

        for j in range(2):  # Generate 2 repos for each project
            repo = {
                'repoID': str(j+1),
                'repoName': repo_names[(i*2+j)%10],
                'branches': []
            }

            for k in range(2):  # Generate 2 branches for each repo
                branch = {
                    'branchID': str(k+1),
                    'branchName': branch_names[(i*2+j*2+k)%10],
                    'commits': [commit_messages[(i*2+j*2+k*2+l)%10] for l in range(2)]  # Generate 2 commits for each branch
                }

                repo['branches'].append(branch)

            project['repos'].append(repo)

        mock_data.append(project)
    return mock_data