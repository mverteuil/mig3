<template>
  <user-account-list v-if="!$route.params.userAccountId" />
  <user-account-detail v-else />
</template>
<script>
import UserAccountDetail from "@/components/UserAccountDetail";
import UserAccountList from "@/components/UserAccountList";

export default {
  components: {
    UserAccountDetail,
    UserAccountList
  }
};
</script>
