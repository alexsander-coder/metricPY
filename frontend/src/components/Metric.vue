<template>
  <div class="card">
    <h3>Upload de Arquivo</h3>
    <input type="file" @change="handleFileUpload" />
    <button @click="submitFile">Enviar Arquivo</button>
  </div>
  <div class="chart-container">
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';
import Chart from 'chart.js/auto';


let selectedFile: any = null;
const chartCanvas = ref(null);
let myChart: Chart | null = null;

function handleFileUpload(event: any) {
  selectedFile = event.target.files[0];
}

async function submitFile() {
  if (!selectedFile) {
    alert('Por favor, selecione um arquivo primeiro.');
    return;
  }

  const formData = new FormData();
  formData.append('file', selectedFile);

  try {
    const response = await axios.post('http://localhost:8000/upload/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    if (response.data.metrics && Array.isArray(response.data.metrics)) {
      renderChartWithData(response.data.metrics);
    } else {
      console.error('Os dados recebidos não são um array válido.');
    }
  } catch (error) {
    console.error('Houve um erro ao enviar o arquivo:', error);
  }
}

function renderChartWithData(data: any) {
  if (!Array.isArray(data)) {
    console.error('Os dados recebidos não são um array válido.');
    return;
  }


  const labels = data.map((item) => item.mes_ano);
  const mrrValues = data.map((item) => item.MRR);
  const churnRateValues = data.map((item) => item["Churn Rate"]);
  const ltvValues = data.map((item) => item.LTV);
  const arpaValues = data.map((item) => item.ARPA);

  console.log(arpaValues, 'eae feu')


  if (chartCanvas.value) {
    if (myChart) myChart.destroy();

    const ctx = (chartCanvas.value as HTMLCanvasElement).getContext('2d');
    if (ctx) {
      myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: 'MRR',
              data: mrrValues,
              borderColor: 'blue',
              backgroundColor: 'rgba(0, 123, 255, 0.2)',
              fill: false,
            },
            {
              label: 'Churn Rate',
              data: churnRateValues,
              borderColor: 'red',
              backgroundColor: 'rgba(255, 99, 132, 0.2)',
              fill: false,
            },
            {
              label: 'LTV',
              data: ltvValues,
              borderColor: 'green',
              backgroundColor: 'rgba(0, 255, 0, 0.2)',
              fill: false,
            },
            {
              label: 'ARPA',
              data: arpaValues,
              borderColor: 'black',
              backgroundColor: 'green',
              fill: false,
            }
          ],
        },
        options: {
          responsive: true,
          plugins: {
            tooltip: {
              mode: 'index',
              intersect: false,
              callbacks: {
                label: function (context) {
                  let label = context.dataset.label || '';
                  if (label) {
                    label += ': ';
                  }
                  label += Math.round(context.parsed.y * 100) / 100;
                  return label;
                }
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        }
      });
    }
  }
}
</script>

<style scoped>
.card {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  margin-top: 20px;
  text-align: center;
}

input[type="file"] {
  margin-top: 10px;
  padding: 5px;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.chart-container {
  margin-top: 20px;
  width: 100%;
  max-width: 600px;
  /* Ajuste conforme necessário */
  margin-left: auto;
  margin-right: auto;
}
</style>
