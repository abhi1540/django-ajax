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
        labels = ["Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
