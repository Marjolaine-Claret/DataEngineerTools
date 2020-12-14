#!/usr/bin/env python


##
def connect(accountName,password):
    server = Server('dc1.lan.esiee.fr', use_ssl=True, get_info=ALL)
    conn = Connection(server, user="cn=LDAP,ou=comptes_services,ou=utilisateurs,DC=lan,DC=esiee,DC=fr",password="UE=cv,VR1^%Mbj43")
    conn.bind()
    conn.search('DC=lan, DC=esiee, DC=fr', "(&(objectclass=person)(sAMAccountName="+accountName+"))",attributes=['distinguishedName', 'sn', 'telephoneNumber', 'displayName', 'roomNumber', 'givenName','Name'])
    if len(conn.entries)>0:
        DN = conn.entries[0].distinguishedName.value
        conn = Connection(server, user=DN, password=password) 
        if(conn.bind()) :
            return True
    return False
##

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def rien():
    return "Rien ici... <a href='/login'> voir là </a> "

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if connect(form.login.data, form.password.data):
            u = User(42, form.login.data)
            login_user(u, remember=form.remember_me.data)
            return redirect('/success/'+form.login.data)
    return render_template('login.html', form=form)

@login_required
@app.route('/success/<username>')
def sucess(username):
    return "Salut " + username + ".\nTu es arrivé jusque là. "


@app.route('/upload', methods = ['GET', 'POST'])
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    import pandas as pd
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename): 
            filename = secure_filename(file.filename)
            uploaded_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(uploaded_file, filename))
            flash('file uploaded successfully')        
            """
            Ici ajouter le traitement du fichier
            year = filename.split('_')[-1]
            df = pd.read_csv(uploaded_file)
            for worker in df.index:
                u = User(worker, year, *df.loc[worker,:]) 
                db.session.add(u)
                db.session.commit()
            """
            return redirect(url_for('index'))
        else:
            if file and not allowed_file(file.filename): 
                flash("Un fichier de type autorisé svp")
    return render_template('upload.html', allowed=ALLOWED_EXTENSIONS)  

@app.route('/download/<file>')
def download(file):
    ext = file.split('.')[-1]
    return send_file(file,
                     attachment_filename="result."+ext,
                     as_attachment=True)

@app.route('/plot')


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return "you are logged out"
