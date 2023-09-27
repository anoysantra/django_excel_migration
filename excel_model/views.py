from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import pandas as pd
import os
from .python_excel import file_path,lower_field_names,field_names

def run_migrations(request):
    if request.method == 'POST':
        try:
            subprocess.run(['python', 'manage.py', 'makemigrations'], check=True)
            subprocess.run(['python', 'manage.py', 'migrate'], check=True)
            return HttpResponse('Migrations completed successfully.')
        except subprocess.CalledProcessError as e:
            return HttpResponse(f'Error running migrations: {e}', status=500)

    return render(request, 'run_migrations.html', {})


def view_data(request):
    df=pd.read_excel(file_path)
    data=df.to_dict(orient='records')
    print(data)
    #new concept
    for record in data:
        record['Employee_Id'] = record.pop('Employee Id')

    return render(request,'view_data.html',{'field_names':field_names, 'data':data})






