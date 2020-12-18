import os
from server import create_app


app = create_app(os.environ.get('CONFIG_MODE'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
