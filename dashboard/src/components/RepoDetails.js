import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { Breadcrumb, BreadcrumbItem } from 'reactstrap';
import apiService from '../services/apiService';

function RepoDetails() {
  const { projectId, repoId } = useParams();
  const [project, setProject] = useState(null);
  const [repo, setRepo] = useState(null);

  useEffect(() => {
    apiService.getProject(projectId).then(project => {
      setProject(project);
      const repo = project.repos.find(r => r.repoID === repoId);
      setRepo(repo);
    });
  }, [projectId, repoId]);

  if (!project || !repo) {
    return <div className="d-flex justify-content-center mt-5"><div className="spinner-border" role="status"></div></div>;
  }

  return (
    <div className="container mt-5">
      <Breadcrumb>
        <BreadcrumbItem><Link to="/">Home</Link></BreadcrumbItem>
        <BreadcrumbItem><Link to={`/project/${project.projectID}`}>{project.projectName}</Link></BreadcrumbItem>
        <BreadcrumbItem active>{repo.repoName}</BreadcrumbItem>
      </Breadcrumb>
      <h1 className="mb-4">{repo.repoName}</h1>
      <h2 className="mb-3">Branches</h2>
      {repo.branches.map(branch => (
        <div key={branch.branchID} className="card mb-3">
          <div className="card-body">
            <h5 className="card-title">{branch.branchName}</h5>
            <h6 className="card-subtitle mb-2 text-muted">Commits</h6>
            <ul>
              {branch.commits.map((commit, index) => (
                <li key={index}>{commit}</li>
              ))}
            </ul>
          </div>
        </div>
      ))}
    </div>
  );
}

export default RepoDetails;