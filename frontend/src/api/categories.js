import request from './req';


export const apiGetCategories = () => request('GET', '/categories');
export const apiPostCategory = data => request('POST', '/categories', data);
export const apiDeleteCategory = data => request('DELETE', '/categories/?categoryId=' + data);