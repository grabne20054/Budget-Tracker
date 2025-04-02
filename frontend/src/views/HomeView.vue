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
            <div class="mt-3">
                <input type="text" v-model="transactionForm.paymentreason" placeholder="Payment Reason" class="form-control mb-2">
                <input type="number" v-model="transactionForm.amount" placeholder="Amount" class="form-control mb-2">
                
                <div>
                <label>Transaction Type:</label><br>  
                <input v-model="transactionForm.type" type="radio" id="expense" name="type" value="expense">
                <label for="expense">Expense</label><br>
                <input v-model="transactionForm.type" type="radio" id="income" name="type" value="income">
                <label for="income">Income</label><br>
                </div>
                <label>Category:</label><br> 
                <select v-model="transactionForm.category_id" class="form-control">
                    <option disabled value="">Select a category</option>
                    <option v-for="(category, idx) in categoriesList?.value || []" :key="category.id || idx" :value="category.id">
                        {{ category.name }}
                    </option>
                </select>

                <div class="d-flex justify-content-center">
                    <button type="submit" class="btn btn-primary" @click="addTransaction">Add Transaction</button>
                </div>
            </div>
        </div>
    </div>

        
</template>
  
<script setup>
import { onMounted, ref } from 'vue';
import { useFetchAccounts, registerAccount } from '../store/accounts';
import { useFetchTransactions, registerTransaction } from '../store/transactions';
import { useFetchCategories } from '../store/categories';
import router from '../router';

let { accountList } = useFetchAccounts();
let { transactionsList } = useFetchTransactions();
let { categoriesList } = useFetchCategories();

const transactionForm = ref({
    paymentreason: '',
    amount: 0,
    type: "", 
    category_id: 0
})


const submit = async () => {
    await registerAccount();
};

const addTransaction = async () => {
    if (!transactionForm.value.paymentreason.trim()) {
        alert('Please enter a Payment reason.');
        return;
    }
    if (!transactionForm.value.type.trim()) {
        alert('Please enter a Payment type.');
        return;
    }
    await registerTransaction(transactionForm.value);
    transactionForm.value.amount = 0;
    transactionForm.value.paymentreason = '';
    transactionForm.value.type = '';
    transactionForm.value.category_id = '';
    router.push('/refresh');
};

onMounted(() => {
    submit();
});
</script>
