const later = (response) => {
  return new Promise(function(resolve) {
    setTimeout(() => {
      resolve(response)
    }, 1000)
  })
}

export const api = {
  async request (params) {
    const response = {
      "mock": true,
      "id": 1,
      "title": "mock",
      "status": 200
    }
    return later(response)
  },
  async getBees() {
    const bees = 10
    return bees
  }
}