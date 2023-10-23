python
from flask import Flask, request

app = Flask(name)

@app.route('/', methods=['GET', 'POST'])
def index():
if request.method == 'POST':
name = request.form.get('name')
last_name = request.form.get('last_name')
student_id = request.form.get('student_id')

return f"نام: {name}<br>نام خانوادگی: {last_name}<br>شماره دانشجویی: {student_id}"

return '''
<form method="post">
<label for="name">نام:</label>
<input type="text" id="name" name="name"><br><br>

<label for="last_name">نام خانوادگی:</label>
<input type="text" id="last_name" name="last_name"><br><br>

<label for="student_id">شماره دانشجویی:</label>
<input type="text" id="student_id" name="student_id"><br><br>

<input type="submit" value="ارسال">
</form>
'''

if name == 'main':
app.run()