from flask import Flask
app=Flask(__name__)
@app.route('/')
def helloworld():
    return 'my name is atharv'

if(__name__=="__main__"):
    app.run()
