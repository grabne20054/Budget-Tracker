import request from './req';


export const apiGetAccount = () => request('GET', '/accounts');
export const apiPostAccount = () => request('POST', '/accounts');
