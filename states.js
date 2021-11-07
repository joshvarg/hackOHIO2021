// $(document).ready(function(){
  $.getJSON("https://joshvarg.github.io/stateAnalysis.json", function(data){
    var ctx = document.getElementById("myChart").getContext("2d");
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
          data: [data.targets[0].nRx, data.targets[1].nRx, data.targets[2].nRx, data.targets[3].nRx, data.targets[4].nRx, data.targets[5].nRx, data.targets[6].nRx, data.targets[7].nRx, data.targets[8].nRx, data.targets[9].nRx]
        },
        {
          label: "Projected",
          backgroundColor: "lightblue",
          data: [data.targets[0].proj, data.targets[1].proj, data.targets[2].proj, data.targets[3].proj, data.targets[4].proj, data.targets[5].proj, data.targets[6].proj, data.targets[7].proj, data.targets[8].proj, data.targets[9].proj]
        }

      ]
    };

    var myBarChart = new Chart(ctx, {
      type: 'bar',
      data: barChartData,
      options: {
        barValueSpacing: 10,
        scales: {
          yAxes: [{
            ticks: {
              min: 0,
            }
          }]
        }
      }
    })
    
//   }); 
// });
});
