from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__, template_folder='templates', static_folder='static')
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ''
    src_lang = 'auto'
    dest_lang = 'fr'
    original_text = ''
    
    if request.method == 'POST':
        original_text = request.form['text']
        src_lang = request.form.get('src_lang', 'auto')
        dest_lang = request.form['dest_lang']
        translation = translator.translate(original_text, src=src_lang, dest=dest_lang).text
    
    return render_template('teamplate.html', translation=translation, languages=LANGUAGES, src_lang=src_lang, dest_lang=dest_lang, original_text=original_text)

if __name__ == '__main__':
    app.run(debug=True)