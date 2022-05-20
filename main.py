from website import create_app #website is a python package it will by default run all of the stuff in init.py

app=create_app()

if __name__=='__main__': #only if we run this file, the line will be executed
    app.run(debug=False, host='0.0.0.0') #everytime we change the code the webserver will rerun
    