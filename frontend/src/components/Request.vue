<template>
  <v-container>
    <v-row class="pl-5">
      <v-col cols="12" md="3">
        <v-select
          color="purple"
          v-model="selectedMethod"
          :items="methods"
          label="Request Method"
        />
      </v-col>
      <v-col cols="12" md="3">
        <v-select
          color="purple"
          v-model="selectedAccept"
          :items="['text/html', 'application/json']"
          label="Accept"
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
    <v-row v-if="isBodySupported">
      <v-col cols="10" class="ml-5 pr-0">
        <v-textarea
          v-model="requestBody"
          label="Request Body"
          color="purple"
        />
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      selectedMethod: "GET",
      methods: ["GET", "POST", "PUT", "PATCH", "DELETE"],
      url: "",
      requestBody: "",
      selectedAccept: 'text/html'
    };
  },
  computed: {
    isBodySupported() {
      return this.selectedMethod != "GET"
    }
  },
  methods: {
    sendParams() {
      const params = {
        url: this.url,
        method: this.selectedMethod,
        body: this.requestBody,
        accept: this.selectedAccept,
      }
      this.$emit("params", params)
    },
  },
};
</script>
