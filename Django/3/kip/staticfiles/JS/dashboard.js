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
  // console.log(sessionStorage.dash);
  $.when( $.ajax({
    url: "/user/widgets/get/",
   
  })
  ).done(function(data){
    sessionStorage.clear();
    sessionStorage.dash = data.replace(', ', ',');
    // console.log(data, sessionStorage.dash);
  });
 }

 function putWidget(widget){
  $.ajax({
    url: "/user/widgets/"+widget+'/',
  });
 }


 $(document).ready(function(){
    // menu item initialize with sessionStorage

    var today = new Date();
    var sdate, edate;
    if(window.location.search.substr(1)){
                    var inputdate = window.location.search.substr(1).split('~');
                    sdate = inputdate[0];
                    edate = inputdate[1];

        }else{

            if( today.getMonth()<1){
                sdate = (today.getFullYear()-1)+'-'+'12'+'-'+('0' + today.getDate()).substr(-2);
            }else{
                sdate = today.getFullYear()+'-'+('0'+( parseInt(today.getMonth()) )).substr(-2)+'-'+('0' + today.getDate()).substr(-2);
            }

             edate = today.getFullYear()+'-'+('0'+( parseInt(today.getMonth())+1 )).substr(-2)+'-'+('0' + today.getDate() ).substr(-2);      
        }
        // console.log('sdate', sdate, 'edate', edate);
      $( "#datepicker_start" ).val(sdate).datepicker({
                    dateFormat: 'yy-mm-dd',
                    defaultDate: sdate,
                    setDate: sdate,
                });
      $( "#datepicker_end" ).val(edate).datepicker({
                    dateFormat: 'yy-mm-dd',
                    defaultDate: edate,
                    setDate: edate,
                    onSelect: function(dateText) {
                        window.location = '?'+$('#datepicker_start').val()+"~"+dateText+"";
                    }
      });

      $('#select-period').change(function(){     // when period updated
         // console.log(this.value);


             edate = today.getFullYear()+'-'+('0'+( parseInt(today.getMonth())+1 )).substr(-2)+'-'+('0' + today.getDate() ).substr(-2);    

            if(this.value =='Month'){
                if( today.getMonth()<1){
                    sdate = (today.getFullYear()-1)+'-'+'12'+'-'+('0' + today.getDate()).substr(-2);
                }else{
                    sdate = today.getFullYear()+'-'+('0'+( parseInt(today.getMonth()) )).substr(-2)+'-'+('0' + today.getDate()).substr(-2);
                }
            }else if(this.value =='Year'){
                  sdate = (today.getFullYear()-1)+'-'+('0'+( parseInt(today.getMonth())+1 )).substr(-2)+'-'+('0' + today.getDate() ).substr(-2);    
            }else if(this.value =='Total'){
                  sdate = '2016-01-01';
            }
            
            window.location = '?'+sdate+"~"+edate+"";
        });

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

