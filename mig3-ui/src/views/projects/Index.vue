<template>
  <v-container>
    <breadcrumb-title />
    <router-view />
  </v-container>
</template>
<script>
import BreadcrumbTitle from "@/components/BreadcrumbTitle";
export default {
  components: { BreadcrumbTitle }
};
</script>
