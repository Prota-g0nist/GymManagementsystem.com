from flask import Flask
def create_app():
    App=Flask(__name__)
    App.config['SECRET_KEY'] = 'absiad' 
    from routes import dp as main_bp
    App.register_blueprint(main_bp)
    return App
app= create_app()
if __name__== "__main__":
    app.run(host='0.0.0.0',port=5000)
