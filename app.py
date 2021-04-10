from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.config.secret_key = "xxxxxxxxxx"


Office = [
    {
        'name': "Hospital Amerimed",
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
        'telephone': ['(044) 9988813408']
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
        'telephone': ['(044) 998 4891646', '(044) 998 3214400' ] 
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
    'specialities': ['Orthopedics','Trauma']
}

Main_info = {
    'Overview': ['I am a doctor who has practical skills in the treatment of injuries and diseases that are associated with the musculoskeletal system.'],
    'Orthopedist': ['Bone fracture','soft tissue (muscle, tendon, and ligament) injuries','back pain','neck pain','Surgery'],
    'Traumatologist': ['Muscle Seizure','Contusions and ruptures of tendons, ligament damage.']
}

Gallery = []


@app.route('/')
def index():
    return render_template('index.html', Office = Office, Section_titles = Section_titles, Doctor_information = Doctor_information, Main_info = Main_info, Gallery = Gallery)






if __name__ == '__main__':
    app.run(debug=True)