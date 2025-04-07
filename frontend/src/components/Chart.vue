<template>
  <div class="chart-wrapper">
    <select v-model="selectedType" class="type-select">
      <option value="income">Income</option>
      <option value="expense">Expense</option>
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
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Line } from 'vue-chartjs';

ChartJS.register(
  CategoryScale,
  LinearScale,
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
    }
  },
  data() {
    return {
      selectedType: 'income' // default selection
    };
  },
  computed: {
    chartComponent() {
      const types = {
        line: Line,
      };
      return types[this.type] || Line;
    },
    chartData() {
      const filteredData = this.data.filter(item => item.type === this.selectedType);

      return {
        labels: filteredData.map(item => item.created),
        datasets: [
          {
            label: this.selectedType.charAt(0).toUpperCase() + this.selectedType.slice(1),
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
            text: 'Income vs Expense Chart'
          }
        },
        scales: {
          y: {
            beginAtZero: true
          }
        }
      };
    }
  }
};
</script>
<style scoped>
.chart-wrapper {
  width: 100%;
  max-width: 1000px;
  margin: auto;
}

.type-select {
  display: block;
  margin: 1rem auto;
  padding: 0.5rem;
  font-size: 1rem;
}
</style>
