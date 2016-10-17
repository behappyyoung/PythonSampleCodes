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

 function getWidget(){
  console.log(sessionStorage.dash);
  $.when( $.ajax({
    url: "/user/widgets/get/",
   
  })
  ).done(function(data){
    sessionStorage.clear();
    sessionStorage.dash = data.replace(', ', ',');
    console.log(data, sessionStorage.dash);
  });
 }

 function putWidget(widget){
  $.ajax({
    url: "/user/widgets/"+widget+'/',
  });
 }


 $(document).ready(function(){
    // menu item initialize with sessionStorage

    getWidget();
    if(sessionStorage.dash){
      dashArray = sessionStorage.dash.split(',')
        for( item in dashArray){
            if(dashArray[item]){
                $('#dash-'+dashArray[item]).show('fold');
                var functionName = 'draw_'+dashArray[item];
                console.log(functionName, window[functionName]);
                if(window[functionName]){
                    console.log(functionName);
                        window[functionName]();
                }
                $('.dash-list .listitem[data-id='+dashArray[item]+']').removeClass('show');
            }
      }     
    }

    $('.dash-list .listitem').on('click', function(){                   // menu item add / remove
             var currentDash = $(this).data('id');
                      $('#dash-'+currentDash).show('fold');
                      var functionName = 'draw_'+currentDash;
                      if(window[functionName]){
                          window[functionName]();
                      }
                      $(this).removeClass('show');
                      sessionStorage.dash += currentDash + ',';
                      putWidget(sessionStorage.dash.replace(',', ', '));
             });
    $('.panel-dash .dashhide').on('click', function(){
             var currentDash = $(this).data('id');
              $('#dash-'+currentDash).hide('fold');
              $('.dash-list .listitem[data-id="'+currentDash+'"]').addClass('show');
              sessionStorage.dash = sessionStorage.dash.replace(currentDash+',', '');
              putWidget(sessionStorage.dash.replace(',', ','));
    });
 });

