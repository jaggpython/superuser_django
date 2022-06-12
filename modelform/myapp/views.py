from django.shortcuts import redirect, render

from myapp.form import EmpForm

# Create your views here.
def emp(request):
    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(emp)
            except:
                pass
    else:
        form=EmpForm()
    return render(request,'index.html',{'form':form})