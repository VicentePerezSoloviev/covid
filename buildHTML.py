#!/usr/bin/python
#!python

def generateHTML (countries, percentage):
    htmFile = open("report.html", "w")
    htmFile.write(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>Covid evolution up to date</title>
    </head>
    <body>
        <center>
            <h1><p>Report of covid-19 evolution: <span id="datetime"></span></p></h1>
            <script>
                var dt = new Date();
                document.getElementById("datetime").innerHTML = dt.toLocaleString();
            </script>
            <div class="row">
                  <div class="column">
                      <h2>Covid-19 cases</h2>
                      <p>Number of cases evolution in the top countries, considering the total of the population of the country</p>
                      <img src="images/cases.png" alt="cases evolution">
                  </div>
                  <div class="column">
                      <h2>Covid-19 deaths</h2>
                      <p>Number of deaths evolution in the top countries, considering the total of the population of the country</p>
                      <img src="images/deaths.png" alt="deaths evolution">
                  </div>
            </div>
            
            <div class="row">
                  <div class="column">
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
                      
                  </div>
                  <div class="column">
                    <h2>Spanish evolution</h2>
                    <img src="images/spain.png" alt="spanish evolution">
                  </div>
            </div>
            
        
        </center>
    
    </body>
</html>
    
    """

    )

    htmFile.close

