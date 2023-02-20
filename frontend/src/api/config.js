import axios from "axios"

const $axios = axios.create({
  baseURL: "http://localhost:8000/api",
  withCredentials: true,
  xsrfHeaderName: "X-CSRFToken",
  xsrfCookieName: "csrftoken",
})

export default $axios