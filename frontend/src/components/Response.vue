<template>
  <v-card color="background" max-width="1500" v-if="responseData">
    <v-card-title class="green">Response</v-card-title>
    <v-card-text>
      <v-card>
        <v-card-text>
          <pre><code class="language-json">{{ responseData }}</code></pre>
        </v-card-text>
      </v-card>
    </v-card-text>
  </v-card>
</template>

<script>
import { api } from '~api'

export default {
  name: "Response",
  props: {
    requestParams: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      responseData: null
    }
  },
  methods: {
    async makeRequest() {
      const response = await api.request(this.requestParams)
      this.responseData = response
    }
  },
  mounted() {
    this.makeRequest()
  }
}
</script>

<style>
.green {
  color: #50fa7b;
}
</style>