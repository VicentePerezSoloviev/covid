#!/usr/bin/python
#!python

def generateHTML (countries, percentage):
    htmFile = open("docs/index.html", "w")
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
            <h1><p>Report of COVID-19 daily evolution: <span id="datetime"></span></p></h1>
            <script>
                var dt = new Date();
                document.getElementById("datetime").innerHTML = dt.toLocaleString();
            </script>
            <div class="row">
                  <div class="column">
                      <h2>COVID-19 daily cases</h2>
                      <p>Time evolution of COVID cases per population (%) for the top countries</p>
                      <img src="images/cases.png" alt="cases evolution">
                  </div>
                  <div class="column">
                      <h2>COVID-19 daily deaths</h2>
                      <p>Time evolution of deaths per population (%) for the top countries</p>
                      <img src="images/deaths.png" alt="deaths evolution">
                  </div>
            </div>
            
            <div class="row">
            
                <div class="column">
                  <h2>COVID-19 daily evolution per CCAA Spain</h2>
                  <p>Time evolution of COVID cases per CCAA population (%) for the top CCAA in Spain. Galicia is added to show for comparison, despite the fact that is not one of the most affected CCAA</p>
                  <img src="images/ccaa.png" alt="cases evolution ccaa">
                  </div>
                  
                  <div class="column">
                    <h2>Spanish daily evolution and prediction for next 10 days</h2>
                    <p>Number of cases and deaths evolution in Spain</p>
                    <img src="images/spain.png" alt="spanish evolution">
                  </div>
            </div>
            
            <div class="row">
                  <div class="column">
                  <h2>Percentage of deaths per cases</h2>
        
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
                  </div>
            </div>
            
        
        </center>
    
    </body>
</html>
    
    """

    )

    htmFile.close

