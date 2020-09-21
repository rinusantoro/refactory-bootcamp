from app import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        model.save()
        # Failure to return a redirect or render_template
    else:
        message_value = "Form Pendaftaran Proposal Skripsi"
        return render_template('index.html',message_key=message_value)