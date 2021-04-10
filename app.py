from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.config.secret_key = "xxxxxxxxxx"


Office = [
    {
        'name': "Torre Médica Hospital Amerimed",
        'country': 'México',
        'city': 'Cancún',
        'adress': 'AV. BONAMPAK MZA 01 LOTE 1 CONSULTORIO 104 PRIMER PISO  SM6A BENITO JUAREZ  CANCUN QROO',
        'reference': 'Entre el centro comercial plaza las americas y el conjunto habitacional Malecon',
        'available': {
            'Monday': '16:00-18:00',
            'Tuesday': 'NA',
            'Wednesday': '16:00-18:00',
            'Thursday': '16:00-18:00',
            'Friday': '16:00-18:00',
            'Saturday': '08:00-15:00',
            'Sunday': 'NA'
        },
        'telephone': ['(998) 8454383','(998) 8813408']
    },
    {
        'name': "CENTRO QUIROPRACTICO CASSAN",
        'country': 'México',
        'city': 'Cancún',
        'adress': 'CALLE VENADO no. 31 SM 20',
        'reference': 'Not available',
        'available': {
            'Monday': 'NA',
            'Tuesday': '16:00-18:00',
            'Wednesday': 'NA',
            'Thursday': 'NA',
            'Friday': 'NA',
            'Saturday': 'NA',
            'Sunday': 'NA'
        },
        'telephone': ['(998) 8454383','(998) 4891646', '(998) 3214400' ] 
    }
]

Section_titles = {
    'main_info': "What do I specialize in as a doctor?",
    'contact_info': 'Where and when can I attend you?',
    'gallery': 'Photo Gallery',
    'doctor_info': 'Who am I?'
}

Doctor_information = {
    'name': "Berl",
    'lastname': "Blank",
    'telephone': '(044) 998 8454383',
    'university': 'Universidad Nacional Autónoma de México',
    'specialities': ['Orthopedics','Trauma'],
    'curriculum': 'Soy un  médico cirujano graduado de la facultad de medicina de la UNAM, con   especialidad en ortopedia y traumatología  en el Hospital General de México,  con 25 años  de  experiencia laborando en Servicio de Ortopedia y traumatología del Hospital General de Cancún QROO y en mi practica privada, certificado por el consejo mexicano de Ortopedia y Traumatología.',
    'extra': ['Cedula Profesional 1706877','Cedula de especialista  327158','Consejo Mexicano de Ortopedia y traumatología 23289615','RFCBAGB650322186'],
}

Main_info = {
    'Overview': ['I am a doctor who has practical skills in the treatment of injuries and diseases that are associated with the musculoskeletal system.'],
    'Orthopedist': ['Bone fracture','soft tissue (muscle, tendon, and ligament) injuries','back pain','neck pain','Surgery'],
    'Traumatologist': ['Muscle Seizure','Contusions and ruptures of tendons, ligament damage.']
}

Gallery = ['slide1.jpg','slide2.jpg','slide3.jpeg','slide4.jpeg','slide5.jpg','slide6.jpg','slide7.jpg']


@app.route('/')
def index():
    return render_template('index.html', Office = Office, Section_titles = Section_titles, Doctor_information = Doctor_information, Main_info = Main_info, Gallery = Gallery)






if __name__ == '__main__':
    app.run(debug=True)