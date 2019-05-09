<template>
  <builder-account-list v-if="!$route.params.builderAccountId" />
  <builder-account-detail v-else />
</template>
<script>
import BuilderAccountDetail from "../sections/BuilderAccountDetail";
import BuilderAccountList from "../sections/BuilderAccountList";

export default {
  name: "Builders",
  components: {
    BuilderAccountDetail,
    BuilderAccountList
  }
};
</script>
