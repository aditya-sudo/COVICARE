import requests
from bs4 import BeautifulSoup

URL = 'https://economictimes.indiatimes.com/topic/Covid-19'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all("div",class_="clr flt topicstry story_list")


                                       
sourceFile = open('scrap.html', 'w')
print('''<!doctype html>
<html lang="en">
  <head>
    <title>Feed</title>
    <link rel="icon" type="image/png" href="logo.png"/>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>


<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js">
    </script>
   

    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
    
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js" integrity="sha384-SR1sx49pcuLnqZUnnPwx6FCym0wLsk5JZuNx2bPPENzswTNFaQU1RDvt3wT4gWFG" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.min.js" integrity="sha384-j0CNLUeiqtyaRmlzUHCPZ+Gy5fQu0dQ6eZ/xAww941Ai1SxSY+0EQqNXNE6DZiVc" crossorigin="anonymous"></script>

    <script src="https://use.fontawesome.com/03c0cabd99.js"></script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    


    <title>COVICARE</title>
    <link href='https://fonts.googleapis.com/css?family=Acme' rel='stylesheet'>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Oswald&display=swap" rel="stylesheet">
   

    <!-- Bootstrap core CSS -->

    <link href="bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="carousel.css" rel="stylesheet">
    <style>
      h2 {
        font-family: 'Oswald', sans-serif;
      }
      </style>
  </head>
  <body>

    <header>
      <nav class="navbar navbar-expand-md navbar-primary fixed-top bg-primary">
        <a class="navbar-brand text-light font-weight-bolder" href="#"><h3><b>
          <img src="logo.png" alt="" width="50" height="50">  COVICARE</b></h3></a>
        <button class="navbar-toggler bg-primary" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <i title="" class="fa fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link text-dark font-weight-bolder" href="index.html"><h4><b>Home</b></h4> <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-dark" href="Breathing Exercise.html"><h4><b>Exercise</b></h4></a>
            </li> 
            <li class="nav-item">
                <a class="nav-link text-dark" href="https://www.cowin.gov.in/home"><h4><b>Vacccination</b></h4></a>
            </li>
            <li class="nav-item">
            <a class="nav-link text-dark" href="Breathing Exercise.html"><h4><b>Feed</b></h4></a>  
            </li> 
            <li class="nav-item">
                  <a class="nav-link text-dark" href="VitalCheck.html"><h4><b>VitalCheck</b></h4></a>
            </li>
            <li class="nav-item">

              <a class="nav-link text-dark" href="http://gujhealth.gujarat.gov.in/corona-virus-guidline.htm"><h4><b>Helpline</b></h4></a>
            </li>
            <li class="nav-item">
              <div class="dropdown">
                <a class="btn btn-dark dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                  About Us
                </a>
              
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                  <li><a class="dropdown-item" href="https://www.privacypolicygenerator.info/live.php?token=tpultFdInq4jIXG3kGgTAXQBCXolMTj6">Privacy Policy</a></li>
                  <li><a id="contact" class="dropdown-item" href="#">Contact Us</a></li>
                  
                 
                </ul>
              </div>
              <div id="myalert" class="alert alert-success collapse " role="alert">
                <a id="mya" href="#" class="close" >&times;</a>                    <h4 class="alert-heading">Contact Info</h4>
                <p>Darshil Shah  Email:shahdarshil338@gmail.com</p>
                <hr>
                <p class="mb-0">Aditya Shah Email:adityashah1510@gmail.com</p>
              </div>
              
              
              <script type="text/javascript">
                $(document).ready(function(){
                  $('#contact').click(function(){
                      $('#myalert').show('fade');
                  });
                  $('#mya').click(function () {
                      $('#myalert').hide('fade');
                  });
                });
              </script>
            </li>
              
          </ul>
         
          
        </div>
      </nav>
    </header>
    <br>
    <br>''',file=sourceFile)


for i in results:
    urls = i.find_all("img")
    for img in urls:
        # print(img['src'])
        # print(img['data-original'])
        img_urls = img['src']
        img_urls = img_urls.replace(img['src'],img['data-original'])
        img['src'] = img_urls
    #print(i.prettify(), file = sourceFile)

for i in results:
    urls = i.find_all("a")
    for url in urls:
        url['href'] = "https://economictimes.indiatimes.com/topic/Covid-19" + url['href']
    print(i.prettify(), file = sourceFile)


sourceFile.close()