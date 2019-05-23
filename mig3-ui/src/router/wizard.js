export default {
  path: "/installation-setup/",
  name: "InstallationSetupWizard",
  component: () => import(/* webpackChunkName: "installationsetup" */ "@/views/InstallationSetupWizard.vue")
};
