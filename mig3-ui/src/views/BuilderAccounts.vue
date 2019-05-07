<template>
  <builder-account-list v-if="!$route.params.builderAccountId" />
  <builder-account-detail v-else />
</template>
<script>
import BuilderAccountDetail from "../components/BuilderAccountDetail";
import BuilderAccountList from "../components/BuilderAccountList";

export default {
  name: "Builders",
  components: {
    BuilderAccountDetail,
    BuilderAccountList
  }
};
</script>
