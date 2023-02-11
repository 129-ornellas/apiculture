const later = (response) => {
    return new Promise(function(resolve) {
      setTimeout(() => {
        resolve(response)
      }, 1000)
    })
  }
  
  export const api = {
    async sendRequest (url, requestMethod) {
      const response = {
        "mock": false,
        "id": 1,
        "title": "mock",
        "status": 200
      }
      return later(response)
    }
  }