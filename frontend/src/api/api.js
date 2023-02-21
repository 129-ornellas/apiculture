import $axios from "./config.js"

export const api = {
  async request (params) {
    try {
      const response = await $axios.get("/get", {params: params})
      return response.data
    } catch(error) {
      return error.response.data
    }
  }
}