<template>
  <v-layout column grid-list-lg tag="v-container">
    <v-flex>
      <span class="display-4 font-weight-black text-capitalize">Users</span>
      <v-layout>
        <v-flex :key="user.email" v-for="user in users" xs4>
          <v-card
            :to="{ name: 'users', params: { userAccountId: user.id } }"
            dark
          >
            <v-sheet color="red darken-4">
              <v-card-title>
                <v-flex>
                  <v-avatar color="red" left small>
                    <span class="white--text headline text-uppercase">{{
                      user.name.substr(0, 1)
                    }}</span>
                  </v-avatar>
                  <span class="headline icon-text">{{ user.name }}</span>
                </v-flex>
              </v-card-title>
            </v-sheet>
            <v-card-actions class="space-evenly">
              <div>
                <v-icon class="mdi-at vertical-middle">mdi-at</v-icon>
                <span class="icon-text">{{ user.email }}</span>
              </div>
              <div>
                <v-icon class="mdi-at vertical-middle"
                  >mdi-upload-network
                </v-icon>
                <span class="icon-text">{{ user.builds }}</span>
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
        id: "",
        email: "mverteuil@gmail.com",
        name: "Matthew de Verteuil",
        builds: 10
      },
      {
        id: "E0lrPbR",
        email: "nfisher@yahoo.com",
        name: "Theresa Brown",
        builds: 143
      },
      {
        id: "vJ7v5lA",
        email: "kmartinez@wright.com",
        name: "Ryan Gallagher",
        builds: 16
      }
    ]
  })
};
</script>
