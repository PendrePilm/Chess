from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            email = data.get("email")
            pseudo = data.get("pseudo")
            nom = data.get("nom")
            prenom = data.get("prenom")
            password = data.get("password")

            print(f"Received data - Email: {email}, Pseudo: {pseudo}")

            if not email or not pseudo or not nom or not prenom or not password:
                return JsonResponse({"error": "Tous les champs sont obligatoires."}, status=400)

            user = User.objects.create_user(email=email, pseudo=pseudo, nom=nom, prenom=prenom, password=password)
            return JsonResponse({"message": "Inscription réussie !"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Connexion réussie !"}, status=200)
            else:
                return JsonResponse({"error": "Email ou mot de passe incorrect"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)
