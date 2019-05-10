<template>
  <v-card class="detail-card" dark>
    <v-sheet color="detail-heading">
      <v-card-text class="detail-value">{{ this.value }}</v-card-text>
    </v-sheet>
    <v-card-title>
      <span class="detail-field">{{ this.field }}</span>
    </v-card-title>
  </v-card>
</template>
<script>
export default {
  name: "BuildDetailCard",
  data: () => ({
    field: this.field,
    value: this.value
  }),
  props: {
    field: {
      type: String,
      required: true
    },
    value: {
      type: String,
      required: true
    }
  }
};
</script>
<style lang="stylus" scoped>
@import '~vuetify/src/stylus/main'

.detail-card
  @extend .mb-1
  width: 300px

.detail-heading
  @extend .elevation-5, .red.darken-3

.detail-value
  @extend .body-2, .white--text

.detail-field
  @extend .caption, .text-uppercase
</style>
