<template>
  <v-card color="background" max-width="1500" v-if="data">
    <v-card-title class="green">Response</v-card-title>
    <v-card-text>
      <v-card>
        <v-card-text>
          <pre><code>{{ data }}</code></pre>
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
    params: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      data: null
    }
  },
  watch: {
    params: {
      handler: "makeRequest",
      deep: true,
    },
  },
  methods: {
    async makeRequest() {
      this.data = await api.request(this.params)
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