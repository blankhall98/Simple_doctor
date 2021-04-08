from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.config.secret_key = "xxxxxxxxxx"


Office = [
    {
        'name': "Hospital Amerimed",
        'country': 'Mexico',
        'city': 'Cancún',
        'adress': 'Av. Tulum sur no.260 Manzanas 4, 5 y 9, 7, 77500 Cancún, Q.R.',
        'reference': 'Plaza las Américas',
        'available': {
            'Monday': '16:00-18:00',
            'Tuesday': 'Not available',
            'Wednesday': '16:00-18:00',
            'Thursday': 'Not available',
            'Friday': '16:00-18:00',
            'Saturday': '08:00-15:00',
            'Sunday': 'Not available'
        },
        'telephone': '(044) 998 8454383',
        'average_cost': '$500'
    },
    {
        'name': "Clínica Ortopedista Venado",
        'country': 'Mexico',
        'city': 'Cancún',
        'adress': 'Av. Tulum sur no.260 Manzanas 4, 5 y 9, 7, 77500 Cancún, Q.R.',
        'reference': 'Plaza las Américas',
        'available': {
            'Monday': 'Not available',
            'Tuesday': '16:00-18:00',
            'Wednesday': 'Not available',
            'Thursday': '16:00-18:00',
            'Friday': 'Not available',
            'Saturday': 'Not available',
            'Sunday': 'Not available'
        },
        'telephone': '(044) 998 8454383',
        'average_cost': '$500'
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