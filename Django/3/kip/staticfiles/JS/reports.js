google.charts.load('current', {'packages':['corechart']});

function areaChart(name_id, dataArray, optionsObj){
       google.charts.setOnLoadCallback(drawVisualization_area);

      function drawVisualization_area() {
        // Some raw data (not necessarily accurate)
        var data = google.visualization.arrayToDataTable(dataArray);


   var options = optionsObj['options'];

    var chart = new google.visualization.AreaChart(document.getElementById(name_id));
    chart.draw(data, options);
  }
}

function pieChart(name_id, dataArray, optionsObj){

          google.charts.setOnLoadCallback(drawVisualization_pie);

          function drawVisualization_pie() {

        var data = google.visualization.arrayToDataTable(dataArray)

    var options = optionsObj['options'];
        var chart = new google.visualization.PieChart(document.getElementById(name_id));
        chart.draw(data, options);
      }
 }


