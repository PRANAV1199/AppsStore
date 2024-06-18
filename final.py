from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_PORT']=4306
app.config['MYSQL_DB'] = 'androidios'

mysql = MySQL(app)

@app.route('/')
def redirect():
    cur = mysql.connection.cursor()
    cur.execute("Select id,HeadingName,CurrentVersion from app")
    fetchdata = cur.fetchall()
    user=[]
    if fetchdata :
        for i in fetchdata :
            # print(i)
            user.append({'id': i[0],
                'HeadingName': i[1],
                'CurrentVersion':i[2]})
        print(user)
    return render_template('home.html',data=user)


@app.route('/render/<user_id>', methods=['POST'])
def home(user_id):
    cur = mysql.connection.cursor()
    # cur.execute("Select * from app where id=%s",(str(2)))
    cur.execute("Select * from app where id=%s",(user_id,))
    fetchdata = cur.fetchone()
    if fetchdata :
        user = {
                'id': fetchdata[0],
                'HeadingName': fetchdata[1],
                'Update': fetchdata[2],
                'CurrentVersion': fetchdata[3],
                'Details': fetchdata[4],
                'img1': fetchdata[5],
                'img2': fetchdata[6],
                'img3': fetchdata[7],
                'img4': fetchdata[8],
                'img5': fetchdata[9],
                'RequiresAndroid': fetchdata[10],
                'ReleasedOn': fetchdata[11],
                'DownloadSize': fetchdata[12],
                'feature1': fetchdata[13],
                'feature2': fetchdata[14],
                'feature3': fetchdata[15],
                'NumberOfInstalls': fetchdata[16],
                'linkForDownload': fetchdata[17]
            }
    cur.close()
    print(fetchdata)
    # return render_template('check.html',mydata=fetchdata)
    return render_template('ShaktiQuality.html',data=user)

if __name__ == "__main__":

    app.run(debug=True)