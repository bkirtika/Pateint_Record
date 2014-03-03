from bottle import route, run, template, get, post, request,delete,put
p_record={}


@get('/patient/display/<p_id>')
def show_patient(p_id):
    if p_id not in p_record.keys():
        return 'This is not a correct patient id'
    else:
        return p_record[p_id]

  
@post('/patient/create')
def add_patient():
    p_id = request.POST['id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    p_book={}
    p_book["Name"] = p_name
    p_book["Gender"] = p_gender
    p_book["Age"] = p_age
    p_book["Address"] = p_address
    p_book["Phone"] = p_phone
    p_record.update({p_id:p_book})
    return p_record



@put('/patient/update/<p_id>')
def patient_update(p_id):
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    p_book={}
    p_book["Name"] = p_name
    p_book["Gender"] = p_gender
    p_book["Age"] = p_age
    p_book["Address"] = p_address
    p_book["Phone"] = p_phone
    p_record.update({p_id:p_book})
    return p_record
   


@delete('/patient/delete/<p_id>')
def delete_patient(p_id):
    p_record.pop(p_id)
    return p_record


run(host='localhost',port=8086)
