var labels = [];
var grade = [];
var bgc =[]

{% for i in stat %}
  labels.push('{{ i.courseId.name }}');
  grade.push({{i.grad}})

  if({{i.grad}} >60)
 bgc.push('rgba(25, 54, 109, 0.9)')
  else
    bgc.push('rgba(255, 0, 43, 0.9)')
{% endfor %}

let sum= 0
grade.forEach((e)=>{
  if(e>=60)
  sum=sum+1
})
suc = [sum,(grade.length-sum)]

  new Chart("myChart2", {
      type: "bar",
      data: {
        labels:labels,
        datasets: [{
          fill: false,
          lineTension: 0,
          backgroundColor: bgc,
          borderColor: "rgba(0,0,255,0.1)",
          data: grade
        }]
      },
      options: {
        maintainAspectRatio: false,
        title: {
          display: true,
          text: '2023_2'
        },
        legend: {display: false},
        scales: {
          yAxes: [{ticks: {min: 0, max:100}}],
        }
      }
    });

    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Pass', 'Fail'],
        datasets: [{
          data: suc,
          backgroundColor: ['rgba(25, 54, 109, 0.9)','rgba(255, 0, 43, 0.9)']
        }]
      },
      options: {
        maintainAspectRatio: false,
        responsive: true,
      legend: {display: true},
      },

    });
  

sussec = []
grade_count =  []
examCourse = []
oneStdAvg = []
{% for i in allstudStat %}
oneStdAvg.push({{i.average_grade}})
sussec.push({{i.success_grades_count}})
grade_count.push({{i.grade_count}})
examCourse.push(`{{i.ec.start_date.year}} - {{i.ec.Semineter}}`)
{% endfor %}
fail=[]


examCourse = examCourse.reverse()
oneStdAvg =oneStdAvg.reverse()
for (var i =0;i<grade_count.length;i++)
    fail.push(grade_count[i]-sussec[i])
console.log(sussec,grade_count,examCourse,fail)

var ctx = document.getElementById('myChart3').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
      labels:examCourse,
      datasets: [{
          label: 'Dataset 1',
          data: sussec,
          borderColor: 'blue',
          fill: true
      }, {
          label: 'Dataset 2',
          data: fail,
          borderColor: 'red',
          fill: true
      },
      {
        label: 'Dataset 3',
        data: grade_count,
        borderColor: 'green',
        fill: false
    }]
  },
  options: {
      maintainAspectRatio: false,
      title: {
          display: true,
          text: 'Sucssec in all ExamCourses'
      },
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
      },
      onClick: function(event, elements) {
        if (elements.length > 0 && elements[0].datasetIndex === 1) {
            myChart.data.datasets[1].data = myChart.data.datasets[1].data.map(function(value) {
                return null;
            });
            myChart.update();
        }
    }
  }
});

avg=[]


{% for i in avgStuInEachEx %}
avg.push({{i.avg}})
{% endfor %}
avg =avg.reverse()
var ctx = document.getElementById('myChart4').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
      labels: examCourse,
      datasets: [{
          label: 'All Student',
          data: avg,
          borderColor: 'red',
          fill: false
      }, {
          label: 'Current Student',
          data: oneStdAvg,
          borderColor: 'blue',
          fill: false
      }]
  },
  options: {
    maintainAspectRatio: false,
      title: {
          display: true,
          text: 'Avg of grade to All student and cuurent std'
      },
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true,
                  max:100,
              }
          }]
      },
      onClick: function(event, elements) {
          if (elements.length > 0 && elements[0].datasetIndex === 1) {
              myChart.data.datasets[1].data = myChart.data.datasets[1].data.map(function(value) {
                  return null;
              });
              myChart.update();
          }
      }
  }
});
