import axios from "axios";

export default () =>
  axios.create({
    baseURL: "http://localhost:8000/api/",
    headers: {
      Accepts: "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true",
      "Content-Type": "application/json"
    },
    timeout: 1000,
    withCredentials: true,
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN"
  });
