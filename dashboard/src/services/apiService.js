import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:5500';

const apiService = {
  getProjects: () => axios.get('/api/projects').then(res => res.data),
  getProject: (id) => axios.get(`/api/project/${id}`).then(res => res.data),
};

export default apiService;