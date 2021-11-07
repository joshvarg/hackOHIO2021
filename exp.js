$(document).ready(function(){
    $("button").click(function(){
        let ids = [1, 2, 3, 4];
        var eID = this.id;
        for(var i = 0; i<4; i++){
            $("#chart"+ids[i]).hide();
        }
        $("#chart"+eID).toggle();
        
    })
    $.getJSON("https://joshvarg.github.io/topDoctors.json", function(data){
        let med = "";
        let doctors0 = [];
        let prescriptions0 = [];
        for(var i = 0; i < data.contents[0].percentile.length; i++){
            med = data.contents[0].medicine;
            doc = data.contents[0].percentile[i].name;
            doctors0.unshift(doc);
            pre = data.contents[0].percentile[i].tRx
            prescriptions0.unshift(pre);
        }
        let colors1 = '#36CAAB';

        let barChart1 = document.getElementById("chart1").getContext('2d');

        let chart1 = new Chart(barChart1, {
            type: 'bar',
            data: {
                labels: doctors0,
                datasets: [ {
                    data: prescriptions0,
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
                    text: "Top 10% of Doctors Prescribing " + med,
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

        let doctors1 = [];
        let prescriptions1 = [];
        for(var i = 0; i < data.contents[1].percentile.length; i++){
            med = data.contents[1].medicine;
            doc = data.contents[1].percentile[i].name;
            doctors1.unshift(doc);
            pre = data.contents[1].percentile[i].tRx
            prescriptions1.unshift(pre);
        }
        let colors2 = '#36CAAB';

        let barChart2 = document.getElementById("chart2").getContext('2d');

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
                    text: "Top 10% of Doctors Prescribing "+med,
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


        let doctors2 = [];
        let prescriptions2 = [];
        for(var i = 0; i < data.contents[2].percentile.length; i++){
            med = data.contents[2].medicine;
            doc = data.contents[2].percentile[i].name;
            doctors2.unshift(doc);
            pre = data.contents[2].percentile[i].tRx
            prescriptions2.unshift(pre);
        }
        let colors3 = '#36CAAB';

        let barChart3 = document.getElementById("chart3").getContext('2d');

        let chart3 = new Chart(barChart3, {
            type: 'bar',
            data: {
                labels: doctors2,
                datasets: [ {
                    data: prescriptions2,
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
                    text: "Top 10% of Doctors Prescribing "+med,
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



        let doctors3 = [];
        let prescriptions3 = [];
        for(var i = 0; i < data.contents[3].percentile.length; i++){
            med = data.contents[3].medicine;
            doc = data.contents[3].percentile[i].name;
            doctors3.unshift(doc);
            pre = data.contents[3].percentile[i].tRx
            prescriptions3.unshift(pre);
        }
        let colors4 = '#36CAAB';

        let barChart4 = document.getElementById("chart4").getContext('2d');

        let chart4 = new Chart(barChart4, {
            type: 'bar',
            data: {
                labels: doctors3,
                datasets: [ {
                    data: prescriptions3,
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
                    text: "Top 10% of Doctors Prescribing "+med,
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
    });
});