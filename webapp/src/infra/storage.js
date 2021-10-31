// TODO add functions to get and set items in localStorage

export const saveCredentials = (credentials) => {
  localStorage.setItem('credentials', JSON.stringify(credentials));
};

export const getCredentials = localStorage.getItem('credentials');
