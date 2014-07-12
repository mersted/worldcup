require(['Downloads/Chart.js'], function(Chart){
	var Chartjs = Chart.noConflict();
});

// var ctx = document.getElementById("myChart").getContext("2d");
// var myNewChart = new Chart(ctx).PolarArea(data);

var myLineChart = new Chart(ctx).Line(data, options);

var data = {
	labels: []
	datasets: []
}