const expenseChartElemYear = document.getElementById("expenseChartYearly");
const incomeExpenseChartElemYear = document.getElementById("incomeExpenseChartYearly"); //

// Safely parse data passed from Django template
const categories_year = expenseChartElemYear.getAttribute("data-categories").split(",");
const amounts_year = expenseChartElemYear.getAttribute("data-amounts").split(",");
const totalExpenses_year = parseFloat(
  expenseChartElemYear.getAttribute("data-expenses")
);
const totalIncome_year = parseFloat(expenseChartElemYear.getAttribute("data-income"));
const totalSavings_year = parseFloat(expenseChartElemYear.getAttribute("data-savings"));



// Create Pie chart for expense distribution
const expenseChartCtxYear = expenseChartElemYear.getContext("2d");
new Chart(expenseChartCtxYear, {
  type: "pie",
  data: {
    labels: categories_year,
    datasets: [
      {
        data: amounts_year.map((amount) => parseFloat(amount)), // Convert string amounts to numbers
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

// Create Bar chart for income, expenses, and savings
const incomeExpenseChartCtxYear = incomeExpenseChartElemYear.getContext("2d");
new Chart(incomeExpenseChartCtxYear, {
  type: "bar",
  data: {
    labels: ["Income", "Expenses", "Savings"],
    datasets: [
      {
        label: "Amount (₹)",
        data: [totalIncome_year, totalExpenses_year, totalSavings_year],
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
