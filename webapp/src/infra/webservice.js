const BASE_URL = 'http://localhost:5000';

export const toBase64 = (email, password) => btoa(`${email}:${password}`);

export const createAuthHeader = (credentials) => ({
  Authorization: `Bearer ${credentials}`,
});

export const request = ({ path, method, body = null, headers = {} }) =>
  fetch(`${BASE_URL}${path}`, {
    method,
    body,
    headers: Object.assign(
      {},
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
