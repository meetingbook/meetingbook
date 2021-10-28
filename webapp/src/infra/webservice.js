const BASE_URL = 'http://localhost:5000';

export const toBase64 = (email, password) => btoa(`${email}:${password}`);

export const createAuthHeader = (credentials) => ({
  Authorization: `Basic ${credentials}`,
});

/**
 * Makes Fetch request
 * @param {string} path for example '/registration'
 * @param {string} method HTTP method
 * @param {string} body body of POST or PUT request
 * @param {object} headers headers of request
 */
export const request = (path, method, body = '', headers = {}) =>
  fetch(`${BASE_URL}${path}`, {
    method,
    body,
    headers: Object.assign(
      {
        'Content-Type': 'application/json',
      },
      headers
    ),
  }).then((res) => res.json());

export const authRequest = ({
  path,
  method,
  body = '',
  headers = {},
  credentials,
}) =>
  request(
    path,
    method,
    body,
    Object.assign({}, createAuthHeader(credentials), headers)
  );
