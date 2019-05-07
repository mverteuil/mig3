<template>
  <builder-account-detail v-if="$route.params.id" />
  <builder-account-list v-else />
</template>

<script>
import BuilderAccountDetail from "../components/BuilderAccountDetail";
import BuilderAccountList from "../components/BuilderAccountList";

export default {
  name: "Builders",
  components: { BuilderAccountDetail, BuilderAccountList }
};
</script>

<style scoped></style>
