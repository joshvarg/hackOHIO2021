var barChartData = {
    labels: [
      "Washington",
      "Florida",
      "Montana",
      "Indiana",
      "Alaska",
      "Nevada",
      "Oregon",
      "Michigan",
      "Minnesota",
      "Kentucky"

    ],
    datasets: [
      {
        label: "nRx",
        backgroundColor: "pink",
        borderColor: "red",
        borderWidth: 1,
        data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      },
      {
        label: "Projected",
        backgroundColor: "lightblue",
        borderColor: "blue",
        borderWidth: 1,
        data: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
      },

    ]
  };
  
  var chartOptions = {
    responsive: true,
    legend: {
      position: "top"
    },
    title: {
      display: true,
      text: "nRx and Projected Sales per State"
    },
    scales: {
      yAxes: [{
        scaleLabel: {
            display: true,
            labelString: '# Prescribed'
        },
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
  
  window.onload = function() {
    var ctx = document.getElementById("myChart").getContext('2d')
    window.myBar = new Chart(ctx, {
      type: "bar",
      data: barChartData,
      options: chartOptions
    });
  };
  
