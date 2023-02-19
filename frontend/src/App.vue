<script setup>
  import Navbar from '@/components/Navbar.vue'
  import Bees from '@/components/Bees.vue'
  import Request from '@/components/Request.vue'
  import Response from '@/components/Response.vue'
</script>

<template>
  <v-app>
    <v-main>
      <Navbar/>
      <Bees/>
      <Request @requestParams="handleRequestParams"/>
      <v-container v-if="requestParams">
        <Response :requestParams="requestParams"/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      requestParams: null
    }
  },
  methods: {
    handleRequestParams(requestParams) {
      this.requestParams = requestParams
    }
  }
}
</script>
