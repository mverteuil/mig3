const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/static/" : "http://localhost:8080/",
  outputDir: "./dist/",

  chainWebpack: config => {
    config.optimization.splitChunks(false);

    config.plugin("BundleTracker").use(BundleTracker, [
      {
        filename: "./dist/webpack-stats.json"
      }
    ]);

    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      .public("http://0.0.0.0:8080")
      .host("0.0.0.0")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .proxy({
        "^/api": {
          target: "<url>",
          ws: true,
          changeOrigin: true
        }
      })
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  }
};
