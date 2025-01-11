const expenseChartElem = document.getElementById("expenseChartMonth");
const incomeExpenseChartElem = document.getElementById("incomeExpenseChartMonth");
const categories = expenseChartElem.getAttribute("data-categories").split(",");
const amounts = expenseChartElem.getAttribute("data-amounts").split(",");

const totalExpenses = parseFloat(
  expenseChartElem.getAttribute("data-expenses")
);
const totalIncome = parseFloat(expenseChartElem.getAttribute("data-income"));
const totalSavings = parseFloat(expenseChartElem.getAttribute("data-savings"));

const expenseChartCtx = expenseChartElem.getContext("2d");
new Chart(expenseChartCtx, {
  type: "pie",
  data: {
    labels: categories,
    datasets: [
      {
        data: amounts.map((amount) => parseFloat(amount)), // Convert string amounts to numbers
        backgroundColor: [
          "#ff6384",
          "#36a2eb",
          "#ffcd56",
          "#4bc0c0",
          "#9966ff",
        ],
      },
    ],
  },
  options: {
    responsive: true,
    plugins: {
      tooltip: {
        callbacks: {
          label: function (tooltipItem) {
            let total = tooltipItem.dataset.data.reduce((a, b) => a + b, 0);
            let percentage = Math.round((tooltipItem.raw / total) * 100);
            return tooltipItem.label + ": " + percentage + "%";
          },
        },
      },
      // Display the percentage directly on the pie chart
      datalabels: {
        formatter: (value, ctx) => {
          let total = ctx.dataset.data.reduce((a, b) => a + b, 0);
          let percentage = Math.round((value / total) * 100);
          return percentage + "%";
        },
        color: "#fff",
        font: {
          weight: "bold",
          size: 16,
        },
      },
    },
  },
});

const incomeExpenseChartCtx = incomeExpenseChartElem.getContext("2d");
new Chart(incomeExpenseChartCtx, {
  type: "bar",
  data: {
    labels: ["Income", "Expenses", "Savings"],
    datasets: [
      {
        label: "Amount (₹)",
        data: [totalIncome, totalExpenses, totalSavings],
        backgroundColor: ["#36a2eb", "#ff6384", "#4bc0c0"], // Blue for Income, Red for Expenses, Green for Savings
        borderColor: ["#36a2eb", "#ff6384", "#4bc0c0"],
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          stepSize: 20000, // Adjust this step size as per your data
        },
      },
    },
  },
});
