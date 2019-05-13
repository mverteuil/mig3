<template>
  <v-container fluid>
    <v-layout column>
      <v-flex wrap justify-left align-center>
        <span class="display-4 font-weight-black text-capitalize">Users</span>
      </v-flex>
      <v-layout row wrap>
        <v-container fluid grid-list-lg align-content-start pl-1>
          <v-layout>
            <v-flex :key="user.email" v-for="user in users" xs4>
              <v-card dark>
                <v-sheet color="red darken-4">
                  <v-card-title>
                    <v-flex>
                      <v-avatar color="red" left small>
                        <span class="white--text headline text-uppercase">{{ getUserAvatar(user) }}</span>
                      </v-avatar>
                      <span class="headline icon-text">{{ getNameOrEmailUsername(user) }}</span>
                    </v-flex>
                  </v-card-title>
                </v-sheet>
                <v-card-actions class="space-evenly">
                  <div>
                    <v-icon class="mdi-at vertical-middle">mdi-at</v-icon>
                    <span class="icon-text">{{ user.email }}</span>
                  </div>
                  <div>
                    <v-icon class="mdi-at vertical-middle">mdi-upload-network</v-icon>
                    <span class="icon-text">{{ user.us_count }}</span>
                  </div>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-layout>
    </v-layout>
  </v-container>
</template>
<script>
import { mapState } from "vuex";

export default {
  name: "Users",
  computed: {
    ...mapState({
      users: "users"
    })
  },
  methods: {
    fetchUsers() {
      return this.$store.dispatch("FETCH_USERS");
    },
    getUserAvatar(user) {
      return this.getNameOrEmailUsername(user).substr(0, 1);
    },
    getNameOrEmailUsername(user) {
      return user.name ? user.name : user.email.split("@")[0];
    }
  },
  mounted() {
    this.fetchUsers();
  }
};
</script>
