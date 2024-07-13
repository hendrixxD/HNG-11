from app import create_app
import os
import sys

"""
this function calls our application
"""
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
