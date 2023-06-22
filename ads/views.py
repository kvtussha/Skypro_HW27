from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.core.exceptions import ValidationError

from ads.models import Category, Ads

import json
from config import Config


def status_view(request):
    response = {"status": "ok"}
    return JsonResponse(response)



class AdsDataView(View):
    def get(self, request):
        with open(Config.data_path_ads, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                is_published = item.get("is_published").title()

                ads = Ads(
                    name=item.get("name"),
                    author=item.get("author"),
                    price=item.get("price"),
                    description=item.get("description"),
                    address=item.get("address"),
                    is_published=is_published,
                )

                ads.save()

        return JsonResponse({"message": "Success"}, status=200)



@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        all_ads = Ads.objects.all()
        return JsonResponse([{"id": ads.id,
                              "name": ads.name,
                              "author": ads.author,
                              "price": ads.price,
                              "description": ads.description,
                              "address": ads.address,
                              "is_published": ads.is_published
                              } for ads in all_ads], safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)
        ads = Ads()

        ads.id = ads_data.get("id")
        ads.name = ads_data.get("name")
        ads.author = ads_data.get("author")
        ads.price = ads_data.get("price")
        ads.description = ads_data.get("description")
        ads.address = ads_data.get("address")
        ads.is_published = ads_data.get("is_published")

        try:
            ads.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
         })



class AdsDetailView(DetailView):
    model = Ads
    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
         })



class CategoryDataView(View):
    def get(self, request):
        with open(Config.data_path_cat, "r", encoding="utf-8") as file:
            data = json.load(file)

            for item in data:
                categories = Category(name=item.get("name"))
                categories.save()

        return JsonResponse({"message": "Success"}, status=200)



@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):

    def get(self, request):
        categories = Category.objects.all()
        return JsonResponse([{"id": cat.id, "name": cat.name} for cat in categories],
                            safe=False)


    def post(self, request):
        categories_data = json.loads(request.body)
        categories = Category()

        categories.id = categories_data.get("id")
        categories.name = categories_data.get("name")

        try:
           categories.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        categories.save()

        return JsonResponse({
            "id": categories.id,
            "name": categories.name
        })



class CategoryDetailView(DetailView):
    model = Category
    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({
            "id": cat.id,
            "name": cat.name
        })
