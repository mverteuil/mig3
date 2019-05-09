<template>
  <user-account-list v-if="!$route.params.userAccountId" />
  <user-account-detail v-else />
</template>
<script>
import UserAccountDetail from "@/sections/UserAccountDetail";
import UserAccountList from "@/sections/UserAccountList";

export default {
  components: {
    UserAccountDetail,
    UserAccountList
  }
};
</script>
