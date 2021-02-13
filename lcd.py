import lcddriver
import time

def print_on_lcd(txt="Hello World", time_on=5, waiting=False):
	display = lcddriver.lcd()
	display.lcd_display_string(txt, 1)
	try:
		if waiting:
			pass
		else:
			time.sleep(time_on)
			display.lcd_clear()
	except KeyboardInterrupt:
		display.lcd_clear()
		exit()
