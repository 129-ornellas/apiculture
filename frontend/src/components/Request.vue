<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="3">
        <v-select
          disabled
          color="purple"
          v-model="selectedMethod"
          :items="methods"
          label="Request Method"
        />
      </v-col>
      <v-col cols="12" md="6">
        <v-text-field
          v-model="url"
          placeholder="https://www.api.culture.com/bees"
          label="URL"
          color="purple"
        />
      </v-col>
      <v-col cols="12" md="3">
        <v-btn @click="sendParams" height="55" color="green">Send Request</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      selectedMethod: 'GET',
      methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
      url: '',
    };
  },
  methods: {
    async sendParams() {
      const params = {
        url: this.url,
        method: this.selectedMethod
      }
      this.$emit("params", params)
    },
  },
};
</script>
