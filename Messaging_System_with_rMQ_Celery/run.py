from app import create_app
import os
import sys

"""
this code serves as the entrypoint to our application
"""
if __name__ == '__main__':
    app, _ = create_app()
    app.run(debug=True)
