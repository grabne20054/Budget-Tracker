<template>
  <div class="chart-wrapper">
    <select v-if="type === 'line'" v-model="selectedType" class="type-select">
      <option value="income">Income</option>
      <option value="expense">Expense</option>
    </select>
    <select v-if="type === 'bar'" v-model="selectedCategoryType" class="type-select">
      <option value="income">Income by Category</option>
      <option value="expense">Expense by Category</option>
    </select>
    <component
      :is="chartComponent"
      :data="chartData"
      :options="chartOptions"
    />
  </div>
</template>

<script>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Line, Bar } from 'vue-chartjs';


ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default {
  name: 'ChartComponent',
  props: {
    type: {
      type: String,
      default: 'line'
    },
    data: {
      type: Array,
      required: true
    },
    categories: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      selectedType: 'income',
      selectedCategoryType: 'expense'
    };
  },
  computed: {
    chartComponent() {
      const types = {
        line: Line,
        bar: Bar
      };
      return types[this.type] || Line;
    },
    chartData() {
      if (!this.data || this.data.length === 0) {
        return {
          labels: [],
          datasets: []
        };
      }

      if (this.type === 'bar') {
        const categories = [...new Set(this.data.map(item => this.getCategoryNameById(item.category_id)))];
        const categoryData = categories.map(category => {
          return this.data
            .filter(item => this.getCategoryNameById(item.category_id) === category && item.type === this.selectedCategoryType)
            .reduce((sum, item) => sum + item.amount, 0);
        });

        return {
          labels: categories,
          datasets: [
            {
              label: `${this.selectedCategoryType} by Category`,
              data: categoryData,
              backgroundColor: this.selectedCategoryType === 'income' ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)',
              borderColor: this.selectedCategoryType === 'income' ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)',
              borderWidth: 1
            }
          ]
        };
      }

      const filteredData = this.data.filter(item => item.type === this.selectedType);

      return {
        labels: filteredData.map(item => item.created),
        datasets: [
          {
            label: this.selectedType,
            data: filteredData.map(item => item.amount),
            borderColor: this.selectedType === 'income' ? 'rgba(75, 192, 192, 1)' : 'rgba(255, 99, 132, 1)',
            backgroundColor: this.selectedType === 'income' ? 'rgba(75, 192, 192, 0.2)' : 'rgba(255, 99, 132, 0.2)',
            fill: true,
            tension: 0.4
          }
        ]
      };
    },
    chartOptions() {
      return {
        responsive: true,
        plugins: {
          legend: {
            position: 'top'
          },
          title: {
            display: true,
            text: this.type === 'bar' 
              ? `${this.selectedCategoryType} by Category` 
              : 'Income vs Expense Chart'
          }
        },
        scales: {
          y: {
            beginAtZero: true
          }
        }
      };
    },
  },
  methods: {
    getCategoryNameById(id) {
      const category = this.categories.find(cat => cat.id === id);
      return category ? category.name : 'Unknown';
    }
  }
};
</script>

<style scoped>
.chart-wrapper {
  width: 100%;
  margin: auto;
}

.type-select {
  display: block;
  margin: 1rem auto;
  padding: 0.5rem;
  font-size: 1rem;
}
</style>
