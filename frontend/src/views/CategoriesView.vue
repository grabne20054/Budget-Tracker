<template>
    <div class="col-6 pt-6">
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Category</th>
                    </tr>
                </thead>
                <tbody style="max-height: 300px; overflow-y: auto; display: block;">
                    <tr v-for="(category, idx) in categoriesList?.value || []" :key="category.id || idx" style="display: table; width: 100%; table-layout: fixed;">
                        <th scope="row">{{ category.name }}</th>
                        <td>
                            <button class="btn btn-primary" @click="removeCategory(category.id)">Delete</button>
                        </td>
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
</template>

<script setup>
import { ref } from 'vue';
import { useFetchCategories, registerCategory, deleteCategory } from '../store/categories';
import router from '../router';

let { categoriesList } = useFetchCategories();

let categoryForm = ref({
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
    router.push('/refresh');
};

const removeCategory = async id => {
    await deleteCategory(id);
    router.push('/refresh');
}

</script>