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
      <Bees @bees="bees"/>
      <Request @params="handleParams"/>
      <v-container v-if="params">
        <Response @bees="handleBees" :params="params"/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      params: null,
      bees: 0
    }
  },
  methods: {
    handleParams(params) {
      this.params = params
    },
    handleBees(bees) {
      this.bees = bees
    }
  }
}
</script>
