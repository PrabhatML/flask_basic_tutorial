# manage.py

from flask_script import Manager
from myapp import app
import unittest

manager = Manager(app)

@manager.command
def test():
	loader = unittest.TestLoader()
	tests = loader.discover(start_dir='.',pattern = 'test*.py')
	testRunner = unittest.runner.TextTestRunner()
	testRunner.run(tests)
	
	
if __name__ == "__main__":
    manager.run()