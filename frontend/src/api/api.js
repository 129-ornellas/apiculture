import $axios from "./config.js"

export const api = {
  async request (params) {
    const response = await $axios.get("/get", {params: params})
    return response.data
  }
}