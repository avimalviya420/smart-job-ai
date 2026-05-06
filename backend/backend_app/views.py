# from django.shortcuts import render

# Create your views here.


from django.contrib.auth import authenticate
from django.http import JsonResponse
import json

# def login_view(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         username = data.get("username")
#         password = data.get("password")

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             return JsonResponse({"message": "Login successful"})
#         else:
#             return JsonResponse({"error": "Invalid credentials"}, status=401)



from django.http import JsonResponse
import json

def login_view(request):

    # 👇 CORS preflight request handle करो
    if request.method == "OPTIONS":
        return JsonResponse({"message": "ok"})

    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        if username == "admin" and password == "1234":
            return JsonResponse({
                "status": "success",
                "message": "Login successful"
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "Invalid credentials"
            })

    # 👇 IMPORTANT fallback (warna None return hoga)
    return JsonResponse({"error": "Invalid request method"})