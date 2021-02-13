from ArduinoC import Ardu_On
from lcd import print_on_lcd
from mdc import dc_motor_on

def main():
	print("Program Main")
	kelembaban = Ardu_On()
	if kelembaban <=  30:
		print_on_lcd(txt="Sedang Menyiram", waiting=True)
		dc_motor_on(15)
		print_on_lcd("Selesai Menyiram")
	else:
		print("Tidak Menyiram")
	print_on_lcd(txt="Kelembaban: {}%".format(Ardu_On()), waiting=True)
	print("Kelembaban: {}%".format(Ardu_On()))
if __name__ == "__main__":
	main() 
