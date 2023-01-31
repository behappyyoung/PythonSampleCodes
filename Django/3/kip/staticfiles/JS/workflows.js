

    var print_div = function(landscape=false, css=''){
         var divElements = $('.for-print').html();
         var date = new Date;
         if($('.print-title').text() == ''){
            var title = $('.sub-title').text().trim() + date.toLocaleDateString();   
         }else{
            var title = $('.print-title').text().trim();
         }
         if(landscape){
            var printWindow = window.open("", "_blank", 'height=800,width=1150');
         }else{
            var printWindow = window.open("", "_blank", 'height=1100,width=800');
         }
        
        printWindow.document.open();
        if(css !=''){
                printWindow.document.write('<html><head><title> '+ title +' </title><link rel="stylesheet" type="text/css" href="/static/CSS/'+css+'.css?v=1101"></head> \
                                    <body><div id="printingDiv" class="printingDiv">');
        }else{
              printWindow.document.write('<html><head><title> '+ title +' </title><link rel="stylesheet" type="text/css" href="/static/CSS/print-lab.css?v=1116"></head> \
                                    <body><div id="printingDiv" class="printingDiv">');
             if(landscape){
                    printWindow.document.write('<html><head><title> '+ title +' </title><link rel="stylesheet" type="text/css" href="/static/CSS/print-lab-landscape.css?v=0622"></head> \
                                    <body><div id="printingDiv" class="printingDiv">');
             }else{
                 printWindow.document.write('<html><head><title> '+ title +' </title><link rel="stylesheet" type="text/css" href="/static/CSS/print-lab-portrait.css?v=0403"></head> \
                                    <body><div id="printingDiv" class="printingDiv">');
             }             
        }
                
        

                            printWindow.document.write(divElements);
                            printWindow.document.write('</div></body></html>');

                if(location.hostname.search('gims.org') < 0){
                             setTimeout(function() {
                                 printWindow.print();
                                 printWindow.close();

                             }, 2000);
                }
                    

    }

  var exportTableToCSV = function($table) {
                    //------------------------------------------------------------
                // Helper Functions 
                //------------------------------------------------------------
                // Format the output so it has the appropriate delimiters
                function formatRows(rows){
                    return rows.get().join(tmpRowDelim)
                        .split(tmpRowDelim).join(rowDelim)
                        .split(tmpColDelim).join(colDelim);
                }
                // Grab and format a row from the table
                function grabRow(i,row){
                     
                    var $row = $(row);
                    //for some reason $cols = $row.find('td') || $row.find('th') won't work...
                    var $cols = $row.find('td'); 
                    if(!$cols.length) $cols = $row.find('th');  

                    return $cols.map(grabCol)
                                .get().join(tmpColDelim);
                }
                // Grab and format a column from the table 
                function grabCol(j,col){
                    var $col = $(col),
                        $text = $col.text();

                    return $text.replace('"', '""'); // escape double quotes

                }

                var $headers = $table.find('tr:has(th)')
                    ,$rows = $table.find('tr:has(td)')

                    // Temporary delimiter characters unlikely to be typed by keyboard
                    // This is to avoid accidentally splitting the actual contents
                    ,tmpColDelim = String.fromCharCode(11) // vertical tab character
                    ,tmpRowDelim = String.fromCharCode(0) // null character

                    // actual delimiter characters for CSV format
                    ,colDelim = '","'
                    ,rowDelim = '"\r\n"';

                    // Grab text from table into CSV formatted string
                    var csv = '"';
                    csv += formatRows($headers.map(grabRow));
                    csv += rowDelim;
                    csv += formatRows($rows.map(grabRow)) + '"';
                return csv;
                //     // Data URI
                //     var csvData = 'data:application/csv;charset=utf-8,' + encodeURIComponent(csv);

                // // For IE (tested 10+)
                // if (window.navigator.msSaveOrOpenBlob) {
                //     var blob = new Blob([decodeURIComponent(encodeURI(csv))], {
                //         type: "text/csv;charset=utf-8;"
                //     });
                //     navigator.msSaveBlob(blob, filename);
                // } else {
                //     $(this)
                //         .attr({
                //             'download': filename
                //             ,'href': csvData
                //             //,'target' : '_blank' //if you want it to open in a new window
                //     });
                // }


            }



     var save_div = function(needClass=false){
        var divElements = $('.for-print').html();
         var date = new Date;
         if($('.print-title').text() == ''){
            var title = $('.sub-title').text().trim() + date.toLocaleDateString();   
         }else{
            var title = $('.print-title').text().trim();
         }
         
        dom_parser = new DOMParser().parseFromString(divElements, 'text/html');

        // documentElement always represents the root node
        window.dom_parser = dom_parser;        
        table = dom_parser.documentElement.childNodes[1].childNodes[0];
         
        var csvContent = "data:text/csv;charset=utf-8,";
        items = $('.print-items');
        for(var i=0;i<items.length;i++){
            // console.log($(items[i]).text());
            csvContent += $(items[i]).text() + "\r\n"
        }
        csvContent += "\r\n"
        if(needClass){
             csvContent += exportTableToCSV( $('.for-print table.for-print'));     
        }else{
             csvContent += exportTableToCSV( $('.for-print table'));
        }
       
        var encodedUri = encodeURI(csvContent);
        var link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", title + ".csv");
        document.body.appendChild(link); // Required for FF

       link.click();
    }

var exportTableToCSV_withdiv = function($table) {
                    //------------------------------------------------------------
                // Helper Functions 
                //------------------------------------------------------------
                // Format the output so it has the appropriate delimiters
                function formatRows(rows){
                    console.log('rows.get()', rows.get());
                    return rows.get().join(tmpRowDelim)
                        .split(tmpRowDelim).join(rowDelim)
                        .split(tmpColDelim).join(colDelim);
                }
                // Grab and format a row from the table
                function grabRow(i,row){
                     
                    var $row = $(row);
                    //for some reason $cols = $row.find('td') || $row.find('th') won't work...
                    if($row.hasClass("ng-hide") || $row.hasClass("print-exclude")){
                        return null;
                    }
                    var $cols = $row.find('td'); 
                    if(!$cols.length) $cols = $row.find('th');  

                    // console.log('td row', $cols.map(grabCol).get().join(tmpColDelim));
                    return $cols.map(grabCol)
                                .get().join(tmpColDelim);
                }
                // Grab and format a column from the table 
                function grabCol(j,col){
                    var $col = $(col),
                        $text = $col.text();
                    // console.log('in td text',$col,  $text, $col.html(),  $text.replace(/\s+/g, '\n') );
                    if($col.hasClass("multi-line")){
                        $text = $text.replace(/\s+/g, '\n');
                    }
                    // $text = $text.replace(' ', '');
                    return $text.replace('"', '""'); // escape double quotes

                }

                var $headers = $table.find('tr:has(th)')
                    ,$rows = $table.find('tr:has(td)')

                    // Temporary delimiter characters unlikely to be typed by keyboard
                    // This is to avoid accidentally splitting the actual contents
                    ,tmpColDelim = String.fromCharCode(11) // vertical tab character
                    ,tmpRowDelim = String.fromCharCode(0) // null character

                    // actual delimiter characters for CSV format
                    ,colDelim = '","'
                    ,rowDelim = '"\r\n"';

                    // Grab text from table into CSV formatted string
                    var csv = '"';
                    csv += formatRows($headers.map(grabRow));
                    csv += rowDelim;
                    csv += formatRows($rows.map(grabRow)) + '"';
                // return 'test';
                return csv;


            }


     var save_div_new = function(needClass=false, addclass=" "){
        var divElements = $('.for-print').html();
         var date = new Date;
         if($('.print-title'+addclass).text() == ''){
            var title = $('.sub-title'+addclass).text().trim() + date.toLocaleDateString();   
         }else{
            var title = $('.print-title'+addclass).text().trim();
         }
         
        dom_parser = new DOMParser().parseFromString(divElements, 'text/html');

        // documentElement always represents the root node
        window.dom_parser = dom_parser;        
        table = dom_parser.documentElement.childNodes[1].childNodes[0];
         
        var csvContent = "data:text/csv;charset=utf-8,";
        items = $('.print-items'+addclass);
        for(var i=0;i<items.length;i++){
            console.log($(items[i]).text(), $(items[i]).hasClass("print-exclude"));
            if($(items[i]).hasClass("ng-hide") || $(items[i]).hasClass("print-exclude")){
                    continue;
            }else{
                csvContent += $(items[i]).text() + "\r\n"    
            }
            
        }
        csvContent += "\r\n"
        // console.log('before', csvContent);
        if(needClass){
             csvContent += exportTableToCSV_withdiv( $('.for-print table'+addclass));     
        }else{
             csvContent += exportTableToCSV_withdiv( $('.for-print table'));
        }
       // console.log('after', csvContent);
        var encodedUri = encodeURI(csvContent);
        var link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", title + ".csv");
        document.body.appendChild(link); // Required for FF

       link.click();
    }