from flask import Flask, render_template, request, session
from googletrans import Translator, LANGUAGES

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'your_secret_key'
translator = Translator()

FAVORITE_LANGUAGES = ['en', 'fr', 'es', 'de', 'it']

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ''
    src_lang = 'auto'
    dest_lang = 'fr'
    original_text = ''

    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        original_text = request.form['text']
        src_lang = request.form.get('src_lang', 'auto')
        dest_lang = request.form['dest_lang']

        if original_text.strip():
            try:
                result = translator.translate(original_text, src=src_lang, dest=dest_lang)
                translation = result.text
                # Ajouter la traduction à l'historique
                session['history'].append({
                    'original_text': original_text,
                    'translation': translation,
                    'src_lang': src_lang,
                    'dest_lang': dest_lang
                })
            except Exception as e:
                translation = f'Error: {str(e)}'

    return render_template('teamplate.html', translation=translation, languages=LANGUAGES, favorite_languages=FAVORITE_LANGUAGES, src_lang=src_lang, dest_lang=dest_lang, original_text=original_text, history=session['history'])

if __name__ == '__main__':
    app.run()