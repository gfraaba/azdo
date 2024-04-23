import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { Breadcrumb, BreadcrumbItem } from 'reactstrap';
import apiService from '../services/apiService';

function ProjectDetails() {
  const { id } = useParams();
  const [project, setProject] = useState(null);

  useEffect(() => {
    apiService.getProject(id).then(project => setProject(project));
  }, [id]);

  if (!project) {
    return <div className="d-flex justify-content-center mt-5"><div className="spinner-border" role="status"></div></div>;
  }

  return (
    <div className="container mt-5">
      <Breadcrumb>
        <BreadcrumbItem><Link to="/">Home</Link></BreadcrumbItem>
        <BreadcrumbItem active>{project.projectName}</BreadcrumbItem>
      </Breadcrumb>
      <h1 className="mb-4">{project.projectName}</h1>
      <h2 className="mb-3">Repos</h2>
      {project.repos.map(repo => (
        <div key={repo.repoID} className="card mb-3">
          <div className="card-body">
            <Link to={`/project/${id}/repo/${repo.repoID}`} className="card-link">{repo.repoName}</Link>
          </div>
        </div>
      ))}
    </div>
  );
}

export default ProjectDetails;