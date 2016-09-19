# from app import app, socket_io
from app import app

if __name__ == '__main__':
    # socket_io.run(app, debug=True, port=9999, host='0.0.0.0')
    app.run(debug=True, port=9999)
