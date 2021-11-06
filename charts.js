
let doctors1 = ['Placeholder1', 'Placeholder2'];
let prescriptions1 = [50, 3, 4, 5];
let colors1 = ['#49A9EA', '#36CAAB', '#34495E', '#B370CF'];

let barChart1 = document.getElementById("myChart").getContext('2d');

let chart1 = new Chart(barChart1, {
    type: 'bar',
    data: {
        labels: doctors1,
        datasets: [ {
            data: prescriptions1,
            backgroundColor: colors1
        }]
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
                    labelString: 'Doctor'
                },
                ticks: {
                    display: false
                }

            }],
       
        },

        title: {
            text: "Top 10% of Doctors Prescribing Cholecap",
            display: true
        },
        legend: {
          display: false
        }, 
        labels: {
            display: false
        },
    }
});


let doctors2 = ['Placeholder1', 'Placeholder2'];
let prescriptions2 = [50, 3, 4, 5];
let colors2 = ['#49A9EA', '#36CAAB', '#34495E', '#B370CF'];

let barChart2 = document.getElementById("myChart2").getContext('2d');

let chart2 = new Chart(barChart2, {
    type: 'bar',
    data: {
        labels: doctors1,
        datasets: [ {
            data: prescriptions1,
            backgroundColor: colors2
        }]
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
                    labelString: 'Doctor'
                },
                ticks: {
                    display: false
                }

            }],
       
        },

        title: {
            text: "Top 10% of Doctors Prescribing Zap-a-Pain",
            display: true
        },
        legend: {
          display: false
        }, 
        labels: {
            display: false
        },
    }
});



let doctors3 = ['Placeholder1', 'Placeholder2'];
let prescriptions3 = [50, 3, 4, 5];
let colors3 = ['#49A9EA', '#36CAAB', '#34495E', '#B370CF'];

let barChart3 = document.getElementById("myChart3").getContext('2d');

let chart3 = new Chart(barChart3, {
    type: 'bar',
    data: {
        labels: doctors1,
        datasets: [ {
            data: prescriptions1,
            backgroundColor: colors3
        }]
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
                    labelString: 'Doctor'
                },
                ticks: {
                    display: false
                }

            }],
       
        },

        title: {
            text: "Top 10% of Doctors Prescribing Nasalclear",
            display: true
        },
        legend: {
          display: false
        }, 
        labels: {
            display: false
        },
    }
});



let doctors4 = ['Placeholder1', 'Placeholder2'];
let prescriptions4 = [50, 3, 4, 5];
let colors4 = ['#49A9EA', '#36CAAB', '#34495E', '#B370CF'];

let barChart4 = document.getElementById("myChart4").getContext('2d');

let chart4 = new Chart(barChart4, {
    type: 'bar',
    data: {
        labels: doctors1,
        datasets: [ {
            data: prescriptions1,
            backgroundColor: colors4
        }]
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
                    labelString: 'Doctor'
                },
                ticks: {
                    display: false
                }

            }],
       
        },

        title: {
            text: "Top 10% of Doctors Prescribing Nova-itch",
            display: true
        },
        legend: {
          display: false
        }, 
        labels: {
            display: false
        },
    }
});



