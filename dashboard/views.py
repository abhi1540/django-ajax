from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View


# Create your views here.



# class country(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'base.html')

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/india.html')




# class india(APIView):
#     authentication_classes = []
#     permission_classes = []
#
#     def get(self, request, format=None):
#         # qs_count = User.objects.all().count()
#         # labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
#         # default_items = [qs_count, 23, 2, 3, 12, 2]
#         labels = ["Blue", "Yellow", "Green", "Purple", "Orange"]
#         default_items = [23, 2, 3, 12, 2]
#         data = {
#                 "labels": labels,
#                 "default": default_items,
#         }
#         return Response(data)
#
#
# class australia(APIView):
#     authentication_classes = []
#     permission_classes = []
#
#     def get(self, request, format=None):
#         # qs_count = User.objects.all().count()
#         # labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
#         # default_items = [qs_count, 23, 2, 3, 12, 2]
#         labels = ["Blue", "Yellow", "Green", "Purple", "Orange"]
#         default_items = [23, 2, 3, 12, 2]
#         data = {
#                 "labels": labels,
#                 "default": default_items,
#         }
#         return Response(data)
#
# class japan(APIView):
#     authentication_classes = []
#     permission_classes = []
#
#     def get(self, request, format=None):
#         # qs_count = User.objects.all().count()
#         # labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
#         # default_items = [qs_count, 23, 2, 3, 12, 2]
#         labels = ["Blue", "Yellow", "Green", "Purple", "Orange"]
#         default_items = [23, 2, 3, 12, 2]
#         data = {
#                 "labels": labels,
#                 "default": default_items,
#         }
#         return Response(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # qs_count = User.objects.all().count()
        # labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        # default_items = [qs_count, 23, 2, 3, 12, 2]
        labels = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        default_items1 = [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638]
        default_items2 = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0]
        data = {
                "labels": labels,
                "default1": default_items1,
                "default2": default_items2,
        }
        return Response(data)
