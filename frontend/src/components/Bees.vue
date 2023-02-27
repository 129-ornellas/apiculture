<template>
  <v-container>
    <v-responsive class="text-center">
      <v-chip prepend-icon="mdi-bee" text-color="white" color="purple">
       <p v-if="updatedBees">Bees: {{ updatedBees }}</p>
       <p v-else>Bees: {{ bees }}</p>
      </v-chip>
    </v-responsive>
  </v-container>
</template>

<script>
import { api } from "~api"

export default {
  name: "Bees",
  props: {
    updatedBees: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      bees: 0
    }
  },
  async mounted() {
    this.bees = await api.getBees()
  }
}
</script>
