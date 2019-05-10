<template>
  <v-layout column grid-list-lg tag="v-container">
    <v-flex>
      <span class="display-4 font-weight-black text-capitalize">Users</span>
      <v-layout>
        <v-flex :key="user.email" v-for="user in users" xs4>
          <v-card :to="{ name: 'users', params: { userAccountId: user.id } }" dark>
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
                <span class="icon-text">{{ user.build_count }}</span>
              </div>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>
<script>
export default {
  name: "UserAccountList",
  data: () => ({
    users: [
      {
        id: "E0lrPbR",
        email: "jwood@hotmail.com",
        name: "Joshua Wood",
        build_count: 1
      },
      {
        id: "qL70nKe",
        email: "mverteuil@github.com",
        name: "",
        build_count: 0
      }
    ]
  }),
  methods: {
    getUserAvatar(user) {
      return this.getNameOrEmailUsername(user).substr(0, 1);
    },
    getNameOrEmailUsername(user) {
      return user.name ? user.name : user.email.split("@")[0];
    }
  }
};
</script>
