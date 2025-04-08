<template>
    <div class="col-6 pt-6">
        <table class="table">
            <thead>
            <tr>
                <th colspan="3">Transactions</th>
            </tr>
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

                    <td>
                        <button class="btn btn-primary" @click="removeTransaction(transaction.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
            
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
import { ref } from 'vue';
import { useFetchCategories} from '../store/categories';
import { useFetchTransactions, registerTransaction, deleteTransaction } from '../store/transactions';
import router from '../router';

let { categoriesList } = useFetchCategories();
let { transactionsList } = useFetchTransactions();

const transactionForm = ref({
    paymentreason: '',
    amount: 0.0,
    type: "", 
    category_id: 0
})


const addTransaction = async () => {
    if (!transactionForm.value.paymentreason.trim()) {
        alert('Please enter a Payment reason.');
        return;
    }
    if (!transactionForm.value.type.trim()) {
        alert('Please enter a Payment type.');
        return;
    }
    console.log('Transaction Form:', transactionForm.value);
    await registerTransaction(transactionForm.value);
    transactionForm.value.amount = 0;
    transactionForm.value.paymentreason = '';
    transactionForm.value.type = '';
    transactionForm.value.category_id = '';
    router.push('/refresh');
};

const removeTransaction = async id => {
    await deleteTransaction(id);
    router.push('/refresh');
}
</script>