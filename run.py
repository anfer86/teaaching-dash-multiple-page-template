from app import app

if __name__ == '__main__':
    app.run_server(port=80, debug=True, host='localhost')
