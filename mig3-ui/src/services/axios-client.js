import axios from "axios";

export default () =>
  axios.create({
    baseURL: process.env.NODE_ENV === "development" ? "http://localhost:8000/api/" : "/api/",
    headers: {
      Accepts: "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
      "Content-Type": "application/json"
    },
    timeout: 5000,
    withCredentials: true,
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN"
  });
