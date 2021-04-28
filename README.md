# project_music
This repo project_music is the collection of REST API's build using Flask.
It basically performes CRUD operations on Audio files of three categories namely song,podcast and audiobook
To run this project clone this repo.
open CMD, go project directory and run "pipenv install"
after installing the dependensies run "pipenv run python app.py"
This will start the server at http://127.0.0.1:5000/


End points

GET: http://127.0.0.1:5000/<audioFIleType>/<audioFIleID>
    
    ex: http://127.0.0.1:5000/song/1

POST: http://127.0.0.1:5000/  
    ex: http://127.0.0.1:5000/
    
        body(JSON) = {
                      "audioFIleType" : "podcast",
                      "audioFileMetaData" : {
                                              "name" : "FLASK",
                                              "duration" : "200",
                                              "host" : "will"
                                                   }
                      }

PUT: http://127.0.0.1:5000/<audioFIleType>/<audioFIleID>
    
     ex: http://127.0.0.1:5000/audiobook/3

DELETE: http://127.0.0.1:5000/<audioFIleType>/<audioFIleID>
    
         ex: http://127.0.0.1:5000/podcast/4
