import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import apiService from '../services/apiService';

function Projects() {
  const [projects, setProjects] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // console.log('Fetching projects'); // Log a message at the start of the useEffect hook
    apiService.getProjects()
      .then(projects => {
        // console.log(projects); // Log the projects data
        setProjects(projects);
        setIsLoading(false);
      })
      .catch(error => {
        console.error(error);
        setError(error);
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return <div className="d-flex justify-content-center mt-5"><div className="spinner-border" role="status"></div></div>;
  }

  if (error) {
    return <div className="alert alert-danger" role="alert">Error: {error.message}</div>;
  }

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Projects</h1>
      {projects.map(project => (
        <div key={project.projectID} className="card mb-3">
          <div className="card-body">
            <Link to={`/project/${project.projectID}`} className="card-link">{project.projectName}</Link>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Projects;