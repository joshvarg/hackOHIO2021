$(document).ready(function(){
  $.getJSON("https://joshvarg.github.io/ppm.json", function(data){
    let xlabels = ['1', '2', '3', '4', '5', '6'];

    //placeholders, only change code between these comments
    let med0 = data.contents[0];
    let med1 = data.contents[1];
    let med2 = data.contents[2];
    let med3 = data.contents[3];
    let choleSales = [med0.Month1, med0.Month2, med0.Month3, med0.Month4, med0.Month5, med0.Month6];
    let zapSales = [med1.Month1, med1.Month2, med1.Month3, med1.Month4, med1.Month5, med1.Month6];
    let nasalSales = [med2.Month1, med2.Month2, med2.Month3, med2.Month4, med2.Month5, med2.Month6];
    let novaSales = [med3.Month1, med3.Month2, med3.Month3, med3.Month4, med3.Month5, med3.Month6];
    //end placeholders

    let barChart1 = document.getElementById("myChart").getContext('2d');

    let chart1 = new Chart(barChart1, {
        type: 'line',
        data: {
            labels: xlabels,
            datasets: [{
                label: med0.medicine,
                data: choleSales,
                borderWidth: 1,
                fill: false,
                borderColor: 'red'
              },
              {
                label: med1.medicine,
                data: zapSales,
                borderWidth: 1,
                fill: false,
                borderColor: 'green'
              },
              {
                label: med2.medicine,
                data: nasalSales,
                borderWidth: 1,
                fill: false,
                borderColor: 'blue'
              },
              {
                label: med3.medicine,
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
  });
});
