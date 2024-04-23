import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Projects from './components/Projects';
import ProjectDetails from './components/ProjectDetails';
import RepoDetails from './components/RepoDetails';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/project/:projectId/repo/:repoId" element={<RepoDetails />} />
        <Route path="/project/:id" element={<ProjectDetails />} />
        <Route path="/" element={<Projects />} />
      </Routes>
    </Router>
  );
}

export default App;