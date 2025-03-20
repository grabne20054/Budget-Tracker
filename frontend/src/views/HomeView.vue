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
                        <th scope="col">Category</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(category, idx) in categoriesList.value" :key="idx">
                        <th scope="row">{{ category.name }}</th>
                    </tr>
                </tbody>
            </table>

            <div class="mt-3">
                <input type="text" v-model="categoryForm.name" placeholder="Category Name" class="form-control mb-2">
                <textarea v-model="categoryForm.description" placeholder="Description" class="form-control mb-2"></textarea>
                <div class="d-flex justify-content-center">
                    <button type="submit" class="btn btn-primary" @click="addCategory">Add Category</button>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script setup>
import { onMounted, ref } from 'vue';
import { useFetchAccounts, registerAccount } from '../store/accounts';
import { useFetchCategories, registerCategory } from '../store/categories';

let { accountList } = useFetchAccounts();
let { categoriesList } = useFetchCategories();

const categoryForm = ref({
    name: '',
    description: ''
});

const addCategory = async () => {
    if (!categoryForm.value.name.trim()) {
        alert('Please enter a category name.');
        return;
    }
    await registerCategory(categoryForm.value);
    categoryForm.value.name = '';
    categoryForm.value.description = '';
};

const submit = async () => {
    await registerAccount();
};

onMounted(() => {
    submit();
});
</script>
