<template>
  <v-container>
    <v-responsive class="text-center">
      <v-chip prepend-icon="mdi-bee" text-color="white" color="purple">Bees: {{ bees }}</v-chip>
    </v-responsive>
  </v-container>
</template>

<script>

export default {
  name: "Bees",
  props: {
    bees: {
      type: Number,
      required: true
    }
  }
}
</script>
