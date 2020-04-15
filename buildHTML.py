#!/usr/bin/python
#!python

import sys

def generateHTML (countries, percentage):
    htmFile = open("report.html", "w")
    htmFile.write(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <style>
    * {
      box-sizing: border-box;
    }

    .column {
      float: left;
      width: 50%;
      padding: 5px;
    }

    /* Clearfix (clear floats) */
    .row::after {
      content: "";
      clear: both;
      display: table;
    }
    
    table {
      font-family: arial, sans-serif;
      border-collapse: collapse;
      width: 50%;
      text-align:center;
    }
    
    td, th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }
    
    tr:nth-child(even) {
      background-color: #dddddd;
    }
    </style>
    <title>Covid evolution up to date</title>
    </head>
    <body>
        <center>
            <h1><p>Report of: <span id="datetime"></span></p></h1>
            <script>
                var dt = new Date();
                document.getElementById("datetime").innerHTML = dt.toLocaleString();
            </script>
            <div class="row">
                  <div class="column">
                      <h2>Cases</h2>
                      <p>Number of cases evolution in the top countries</p>
                      <img src="cases.png" alt="cases evolution">
                  </div>
                  <div class="column">
                      <h2>Deaths</h2>
                      <p>Number of deaths evolution in the top countries</p>
                      <img src="deaths.png" alt="deaths evolution">
                  </div>
            </div>
            
        <h2>Percentage of deaths by cases</h2>
        
        <table>
          <tr>
            <th>Country</th>
            <th>Percentage</th>
          </tr>
          <tr>
          """)

    for i in range(len(countries)):
        htmFile.write("<tr><td>" + str(countries[i]) +"</td>" + "<td>" + "{:.2f}".format(percentage[i]) + " %" +"</td></tr>")

    htmFile.write(
          """

        
        </table>
        </center>
    
    </body>
</html>
    
    """

    )

    htmFile.close

