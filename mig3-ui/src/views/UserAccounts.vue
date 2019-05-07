<template>
  <user-account-detail v-if="$route.params.id" />
  <user-account-list v-else />
</template>

<script>
import UserAccountDetail from "@/components/UserAccountDetail";
import UserAccountList from "@/components/UserAccountList";

export default {
  components: { UserAccountDetail, UserAccountList }
};
</script>
