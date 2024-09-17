from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///multi_formdata.db'  # Use SQLite for simplicity; change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Base(DeclarativeBase):
  pass


class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    performer = db.Column(db.String(100), nullable=False)
    composer = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.String(20), nullable=False)
    rights_owner = db.Column(db.String(100), nullable=False)
    collection_society = db.Column(db.String(100), nullable=False)
    royalty_splits = db.Column(db.String(100), nullable=False)
    license_type = db.Column(db.String(100), nullable=False)
    license_terms = db.Column(db.String(100), nullable=False)
    territory_rights = db.Column(db.String(100), nullable=False)
    iswc = db.Column(db.String(100), nullable=False)
    release_type = db.Column(db.String(100), nullable=False)
    version_info = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<FormData {self.title}>'


def create_tables():
    db.create_all()

@app.route('/',methods=['GET','POST'])
def home():
    db.create_all()
    print("Entered")
    if request.method == 'POST':
        print("Postyy")
        form_data = FormData(
            title=request.form.get('title'),
            performer=request.form.get('performer'),
            composer=request.form.get('composer'),
            publisher=request.form.get('publisher'),
            release_date=request.form.get('releaseDate'),
            rights_owner=request.form.get('rightsOwner'),
            collection_society=request.form.get('collectionSociety'),
            royalty_splits=request.form.get('royaltySplits'),
            license_type=request.form.get('licenseType'),
            license_terms=request.form.get('licenseTerms'),
            territory_rights=request.form.get('territoryRights'),
            iswc=request.form.get('iswc'),
            release_type=request.form.get('releaseType'),
            version_info=request.form.get('versionInfo')
        )
        
        db.session.add(form_data)
        db.session.commit()
        
        return redirect(url_for('success'))

    
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/formdata', methods=['POST'])
def form_data():
    # print("Entered")
    # if request.method == 'POST':
    #     form_data = FormData(
    #         title=request.form.get('title'),
    #         performer=request.form.get('performer'),
    #         composer=request.form.get('composer'),
    #         publisher=request.form.get('publisher'),
    #         release_date=request.form.get('releaseDate'),
    #         rights_owner=request.form.get('rightsOwner'),
    #         collection_society=request.form.get('collectionSociety'),
    #         royalty_splits=request.form.get('royaltySplits'),
    #         license_type=request.form.get('licenseType'),
    #         license_terms=request.form.get('licenseTerms'),
    #         territory_rights=request.form.get('territoryRights'),
    #         iswc=request.form.get('iswc'),
    #         release_type=request.form.get('releaseType'),
    #         version_info=request.form.get('versionInfo')
    #     )
        
    #     db.session.add(form_data)
    #     db.session.commit()
        
    #     return redirect(url_for('success'))
    pass

if __name__ == "__main__":
    app.run(debug=True)
