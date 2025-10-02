from django.shortcuts import render
def calculateBMI(request):
    context={}
    context['bmi']="0"
    context['h']="0"
    context['w']="0"
    if(request.method == "POST"):
        h=request.POST.get("height")
        w=request.POST.get("weight")
        h=float(h)
        w=float(w)
        bmi=round(w/(h**2),2)
        context['bmi']=bmi
        context['h']=h
        context['w']=w
        print("Request=",request)
        print("Height=",h)
        print("Weight=",w)
        print("BMI=",bmi)
    return render(request,'mathapp/samp.html',context)