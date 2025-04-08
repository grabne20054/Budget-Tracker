<template>
    <div class="chart">
    <Chart :data="transactionsList.value" ></Chart>
    <Chart :data="transactionsList.value" type="bar" :categories="categoriesList.value"></Chart>
    </div>

</template>


<script setup>
import { useFetchTransactions } from '../store/transactions';

import { useFetchCategories } from '../store/categories';
import Chart from '../components/Chart.vue';


const limit = 5;

let { transactionsList } = useFetchTransactions(limit);
let { categoriesList } = useFetchCategories();
</script>

<style scoped>
.chart {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50%;
    height: 50%;
    margin: auto;
}
.type-select {
    margin: 20px;
}
</style>