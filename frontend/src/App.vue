<template>
  <v-app>
    <v-main>
      <Navbar/>
      <Bees/>
      <Request/>
      <Response/>
    </v-main>
  </v-app>
</template>

<script setup>
  import Navbar from '@/components/Navbar.vue'
  import Bees from '@/components/Bees.vue'
  import Request from '@/components/Request.vue'
  import Response from '@/components/Response.vue'
</script>
