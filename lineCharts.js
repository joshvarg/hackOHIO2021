let xlabels = ['1', '2', '3', '4', '5', '6'];

//placeholders, only change code between these comments
let choleSales = [1, 2, 3, 4, 5, 6];
let zapSales = [2, 3, 4, 5, 6, 7];
let nasalSales = [3, 4, 5, 6, 7, 8];
let novaSales = [4, 5, 6, 7, 8, 9];
//end placeholders

let barChart1 = document.getElementById("myChart").getContext('2d');

let chart1 = new Chart(barChart1, {
    type: 'line',
    data: {
        labels: xlabels,
        datasets: [{
            label: 'Cholecap',
            data: choleSales,
            borderWidth: 1,
            fill: false,
            borderColor: 'red'
          },
          {
            label: 'Zap-a-Pain',
            data: zapSales,
            borderWidth: 1,
            fill: false,
            borderColor: 'green'
          },
          {
            label: 'Nasalclear',
            data: nasalSales,
            borderWidth: 1,
            fill: false,
            borderColor: 'blue'
          },
          {
            label: 'Nova-itch',
            data: novaSales,
            borderWidth: 1,
            fill: false,
            borderColor: 'brown'
          }
        ]
      },

    options: {
        scales: {
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: '# Prescribed'
                }
            }],
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Month'
                },
                ticks: {
                    display: true
                }
                

            }],
       
        },

        title: {
            text: "Medicine Sales Per Month",
            display: true
        },
        legend: {
          display: true
        }, 
        labels: {
            display: true
        },
    }
});
