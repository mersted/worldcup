require(['Downloads/Chart.js/Chart.js'], function(Chart){
	var Chartjs = Chart.noConflict();
});

var ctx = document.getElementById("myChart").getContext("2d");
var myLineChart = new Chart(ctx).Line(data, options);

var data = {
	labels: ["22:52", "22:57", "23:02", "23:07", "23:12", "23:17", "23:22", "23:27", "23:32", "23:37", "23:42", "23:47", "23:52"],
	datasets: [
		{
			label: "Dempsey",
			fillColor: "rgba(100, 100, 0, 1)",
			strokeColor: "rgba(100, 100, 0, 1)",
			pointColor: "rgba(100, 100, 0, 1)",
			data: [11047, 9148, 8611, 5358, 3728, 2171, 2317, 2552, 2366, 3524, 1568, 594, 3008]
		},
		{
			label: "Ghana",
			fillColor: "rgba(100, 100, 0, 1)",
			strokeColor: "rgba(100, 100, 0, 1)",
			pointColor: "rgba(100, 100, 0, 1)",
			data: [22239, 19059, 17278, 14036, 13441, 23875, 24691, 21314, 19892, 18304, 32546, 12952, 17522]
		},
		{
			label: "Goal",
			fillColor: "rgba(100, 100, 0, 1)",
			strokeColor: "rgba(100, 100, 0, 1)",
			pointColor: "rgba(100, 100, 0, 1)",
			data: [6870, 5265, 5292, 3516, 2726, 3194, 3730, 3267, 3180, 2978, 5345, 6554, 3944]
		},
		{
			label: "USA",
			fillColor: "rgba(100, 100, 0, 1)",
			strokeColor: "rgba(100, 100, 0, 1)",
			pointColor: "rgba(100, 100, 0, 1)",
			data: [28052, 24070, 24180, 21116, 18104, 20159, 21874, 20806, 20419, 20868, 19727, 42011, 35833]
		}
	]
};
