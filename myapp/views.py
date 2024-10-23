from django.shortcuts import render

from django.views.generic import View
from myapp.forms import StudentForm

# Create your views here.

class StudentView(View):
    templte_name="studemt_add.html"
    form_class=StudentForm

    def get(self,request,*args,**kwargs):
        form_instance=self.form_class

        return render(request,self.templte_name,{"form":form_instance})
