<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-6 pt-6">
            <table class="table">
                <thead>
                    <tr v-for="(account, idx) in accountList.value" :key="idx">
                        <th>Account Balance</th>
                        <th scope="row">{{ account }}</th>
                    </tr>
                </thead>    
            </table>
    </div>
    <div class="col-6 pt-6">
        <table class="table">
            <thead>
                <tr>
                    <th>Last 5 Transactions</th>
                </tr>
            </thead>
            <thead>
                <tr>
                    <th>Payment Reason</th>
                    <th>Amount</th>
                    <th>Type</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(transaction, idx) in transactionsList.value" :key="idx">
                    <td>{{ transaction.paymentreason }}</td>
                    <td>{{ transaction.amount }}</td>
                    <td>{{ transaction.type }}</td>
                </tr>
            </tbody>
        </table>
    </div>
    </div>

        
</template>
  
<script setup>
import { onMounted, ref } from 'vue';
import { useFetchAccounts, registerAccount } from '../store/accounts';
import { useFetchTransactions, registerTransaction } from '../store/transactions';
import { useFetchCategories } from '../store/categories';
import router from '../router';

const limit = 5;

let { accountList } = useFetchAccounts();
let { transactionsList } = useFetchTransactions(limit);
let { categoriesList } = useFetchCategories();

const submit = async () => {
    await registerAccount();
};


onMounted(() => {
    submit();
});
</script>
