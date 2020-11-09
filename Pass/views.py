from django.shortcuts import render
from Pass.models import PassApplication
from django.core.exceptions import ValidationError
from Checker.models import OnDuty, OnDutyChecked
# Create your views here.
def passConformation(request,number,ondutyid):
    "this will be called when there will an conformation of pass"
    filter_set = dict()
    if len(number) is 10:
        filter_set['phoneNumber'] = number
    elif len(number):
        filter_set['AadharCardNo'] = number
    filter_set['status'] = "Approve"
    filter_set['valid'] = "True"
    try:
        paas = PassApplication.objects.all().filter(**filter_set).order_by("-when_passed")[0]
        print(paas)


        onduty = OnDuty.objects.get(id= ondutyid)
        if onduty.checkedToday:
            today = onduty.OnDutyCheckedPass.all()[0]
            pull_ids = today.passIds
            today.passIds = pull_ids + f",{paas.ApplicationID}"
            today.save()

        else:
            today = OnDutyChecked.objects.create(
                checker = onduty,
                passIds=paas.ApplicationID,
            )

        if paas.recentPicture:
            image = paas.recentPicture.url
        elif paas.recentPictureUrl:
            image = paas.recentPictureUrl
        sdatetime = f"{paas.startTime.day}/{paas.startTime.month}/{paas.startTime.year} {paas.startTime.hour}:{paas.startTime.minute}"
        fdatetime = f"{paas.endtdatetime.day}/{paas.endtdatetime.month}/{paas.endtdatetime.year} {paas.endtdatetime.hour}:{paas.endtdatetime.minute}"
        context = {
            "aadhar":number, 
            "ondutyid":ondutyid,
            "fullName": paas.fullName,
            "cardNo":paas.AadharCardNo,
            "purpose":paas.purpose,
            "from":paas.fromAddr,
            "to":paas.destination,
            "stime":sdatetime,
            "etime":fdatetime,
            "image": image
            }
        return render(request, "test.html", context)
    except:
        return render(request, "notFound.html", {})


def passToSee(request,number):
    "this will be called when there will an conformation of pass"
    filter_set = dict()
    if len(number) is 10:
        filter_set['phoneNumber'] = number
    elif len(number):
        filter_set['AadharCardNo'] = number
    filter_set['status'] = "Approve"
    filter_set['valid'] = "True"
    paas = PassApplication.objects.all().filter(**filter_set).order_by("-when_passed")[0]

    if paas.recentPicture:
        image = paas.recentPicture.url
    elif paas.recentPictureUrl:
        image = paas.recentPictureUrl
    sdatetime = f"{paas.startTime.day}/{paas.startTime.month}/{paas.startTime.year} {paas.startTime.hour}:{paas.startTime.minute}"
    fdatetime = f"{paas.endtdatetime.day}/{paas.endtdatetime.month}/{paas.endtdatetime.year} {paas.endtdatetime.hour}:{paas.endtdatetime.minute}"
    context = {
        "aadhar":number, 
        "ondutyid":"",
        "fullName": paas.fullName,
        "cardNo":paas.AadharCardNo,
        "purpose":paas.purpose,
        "from":paas.fromAddr,
        "to":paas.destination,
        "stime":sdatetime,
        "etime":fdatetime,
        "image": image
        }
    return render(request, "test.html", context)