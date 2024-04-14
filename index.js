const crimeratechart  = document.getElementById('crime-chart');
const accusedcountchart = document.getElementById('accused-chart');
const victimcountchart = document.getElementById('victim-chart');
const occurenceofcrime = document.getElementById('occurence-crime');


fetch('/api/crime-rate')
.then(res => res.json())
.then(data => 
    new Chart(crimeratechart,{
        type:'line',
        data: {
            labels:data.labels,
            datasets:[{
                label:'No of Crimerates',
                data:data.data,
                borderwidth: 1
            }]
        },
        options:{
            scales: {
                y:{
                    beginAtZero: true
                }
            }
        }
    }))




const estimatedaccusedcount = new Chart(accusedcountchart,{
    type:'line',
    data: {
        labels:['Jan','Feb','Mar','Apr','May'],
        datasets:[{
            label:'No of Accusedrates',
            data:[21,34,23,54,67,35],
            borderwidth: 1
        }]
    },
    options:{
        scales: {
            y:{
                beginAtZero: true
            }
        }
    }
})

const trendofoccurence = new Chart(occurenceofcrime,{
    type:'bar',
    data: {
        labels:['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        datasets:[{
            label:'Crime count',
            data:[45,30,21,34,23,54,37,67,35,67,23,48],
            borderwidth: 1
        }]
    },
    options:{
        scales: {
            y:{
                beginAtZero: true
            }
        }
    }
});