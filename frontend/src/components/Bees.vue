<template>
  <v-container>
    <v-responsive class="text-center">
      <v-chip prepend-icon="mdi-bee" text-color="white" color="purple">Bees: {{ bees }}</v-chip>
    </v-responsive>
  </v-container>
</template>

<script>
import { api } from '@/api/api'

export default {
  name: "Bees",
  props: {
    beesCounter: {
      type: Number,
      default: 0
    },
  },
  data() {
    return {
      bees: 0
    }
  },
  watch: {
    beesCounter: {
      handler: "getBees",
      deep: true
    }
  },
  methods: {
    async getBees() {
      this.bees = await api.getBees()
    }
  },
  mounted() {
    this.getBees()
  }
}
</script>
