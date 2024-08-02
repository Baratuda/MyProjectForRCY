import os
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'myDB.db'))

# from flask import Flask, request, render_template
# from sqlalchemy.orm import scoped_session, sessionmaker
# from config import engine
# from models import FireTruks, FireDepartment, FireFighters




# app = Flask(__name__) 
# @app.route("/", methods=['GET','POST'])
# def all():
    
#     query2 = request.args.get('licensePlate')
#     ric = request.args.get('rictangle')
    
#     if request.method == 'POST':   
#         query = request.form['query']
#         if query.lower() == 'ремонт':
#             results = { i.fireDepartmentNumber:[] for i in db_session.query(FireDepartment).order_by(FireDepartment.districtDepartment_id).all()}
#             for i in db_session.query(FireTruks).filter(FireTruks.status == "REP"):
#                 results[i.fireDepartment_id].append(i)
#             return render_template('repair.html', results=results, status = "rep")
#         if query.lower() == 'резерв':
#             results = { i.fireDepartmentNumber:[] for i in db_session.query(FireDepartment).order_by(FireDepartment.districtDepartment_id).all()}
#             for i in db_session.query(FireTruks).filter(FireTruks.status == "RES"):
#                 results[i.fireDepartment_id].append(i)
#             return render_template('reserve.html', results=results, status = "res") 
#         if str(query) in rictangles:
#             rictangle = rictangles[query]
#             result = { i:[] for i in rictangle}
#             for i in db_session.query(FireTruks).filter(FireTruks.fireDepartment_id.in_(rictangle)).all():
#                 result[i.fireDepartment_id].append(i)
#             return render_template('rictangle.html', results=result, status = 'ric', rictangle = query, notСombatVehicles=getNotСombatVehicles() ) 
#     if query2:
#           firefighters = db_session.query(FireFighters).filter(FireFighters.fireTruk_id==query2)
#           result = None
#           if ric:
#             rictangle = rictangles[ric]
#             result = { i:[] for i in rictangle}
#     if request.method == 'GET' or query=='':
#           all_fire_department = db_session.query(FireDepartment).order_by(FireDepartment.districtDepartment_id).all()
#           all_firetruks = db_session.query(FireTruks).all()
#           return render_template('all.html', results = get_firetruks(all_fire_department, all_firetruks, True))    
    

# if __name__ == '__main__':
#     app.run()