from glutwindow import GlutWindow as gl

if __name__ == '__main__':
	width = 400
	height = 300
	title = b'Screen.py'

	instance=gl(width,height,title)
	instance.run()