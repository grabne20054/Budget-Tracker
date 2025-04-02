import request from './req';


export const apiGetTransactions = () => request('GET', '/transactions');
export const apiPostTransaction = data => request('POST', '/transactions', data);
export const apiDeleteTransaction = data => request('DELETE', '/transactions/?transactionId=' + data);