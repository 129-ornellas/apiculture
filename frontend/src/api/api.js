import $axios from "./config.js"

export const api = {
  async request(params) {
    try {
      console.log(params)
      const response = await $axios.get("/request_manager", {params: params})
      return response.data
    } catch(error) {
      return error.response.data
    }
  },
  async getBees() {
    const response = await $axios.get("/bees_manager")
    return response.data.bees
  }
}
