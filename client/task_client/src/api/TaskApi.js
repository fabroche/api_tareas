import axios from "axios";

const taskApi = axios.create({
  baseURL: "http://192.168.1.101:8000/task/api/v1/tasks/",
});

export const getAllTask = () => taskApi.get("/");

export const getTask = (id) => taskApi.get(`/${id}/`);

export const createTask = (task) => taskApi.post("/", task);

export const deleteTask = (id) => taskApi.delete(`/${id}`);

export const updateTask = (id, task) => taskApi.put(`/${id}/`, task);
