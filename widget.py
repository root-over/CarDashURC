import sys
import can


from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QWidget


from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        #TODO leggere dati via bluetooth

        #TODO Programmare pagine secondarie

        #Come trasmette i dati il volante?


        # Crea un'istanza del controller CAN per il bus SPI (can0)
#        bus = can.interface.Bus(channel='can0', bustype='socketcan', bitrate=500000) #NON PUO FUNZIONARE PERCHE NON CE IL MODULO INSTALLATO


        #inizializzazione delle variabili
        #Devo prendere i dati dal CAN e updateare queste variabili
        self.Velocita=0
        self.Perc_batteria=0
        self.Temp_batteria=0
        self.Temp_max_cella=0
        self.Tempo=0
        self.Temp_powertrain_ant=0
        self.Temp_powertrain_post=0
        self.Tens_max_cella=0
        self.Tens_min_cella=0
        self.Temp_max_cella=0
        self.Tens_lowV=0
        self.Tens_media_batteria=0




        self.value=0 #Valore iniziale
        self.ui.velocita.setText(str(self.value))  #inizializza la label Velocita
        self.ui.tempo.setText(str(self.value))


        # Loop infinito per leggere i messaggi CAN dal bus
#        while True:
#            message = bus.recv()
#            print(message)

#TODO if per vedere quale dato è stato ricevuto e aggiornare le variabili apposite
# All'interno del while ci deve essere anche il richiamo del metodo update_label

        # Timer per aggiornare la label ogni 50 ms
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(50)

    def update_label(self):
        # Incrementa il valore della label di 1
        self.value += 1
        self.Velocita+=3

        #aggiorno le label
        self.ui.velocita.setText(str(self.Velocita))
        self.ui.tempo.setText(str(self.Tempo)) #DA SISTEMARE E DIVIDERE IN MIN E SEC
        self.ui.perc_batteria.setText(str(self.Perc_batteria)+'%')
        self.ui.temp_batteria.setText(str(self.Temp_batteria)+'°')
        self.ui.temp_max_cella.setText(str(self.Temp_max_cella)+'°')
        self.ui.temp_powertrain_ant.setText(str(self.Temp_powertrain_ant)+'°')
        self.ui.temp_powertrain_post.setText(str(self.Temp_powertrain_post)+'°')
        self.ui.temp_max_cella.setText(str(self.Temp_max_cella)+'°')
        self.ui.tens_max_cella.setText(str(self.Tens_max_cella)+'V')
        self.ui.tens_min_cella.setText(str(self.Tens_min_cella)+'V')
        self.ui.tens_lowV.setText(str(self.Tens_lowV)+'V')
        self.ui.tens_media_batteria.setText(str(self.Tens_media_batteria)+'V')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
