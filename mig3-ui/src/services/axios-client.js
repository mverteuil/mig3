import axios from "axios";

axios.interceptors.request.use(
  function(config) {
    // eslint-disable-next-line no-console
    console.log("yo");
    // Do something before request is sent
    return config;
  },
  function(error) {
    // eslint-disable-next-line no-console
    console.log("yo");
    // Do something with request error
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  response => {
    // eslint-disable-next-line no-console
    console.log("yo");
    // eslint-disable-next-line no-console
    console.log(response);
    return response;
  },
  error => {
    // eslint-disable-next-line no-console
    console.log(error);
    // eslint-disable-next-line no-console
    console.log("yo");
    if (error.response.status === 401 || error.response.status === 403) {
      window.location.href = "/login/";
    }

    return Promise.reject(error);
  }
);

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
