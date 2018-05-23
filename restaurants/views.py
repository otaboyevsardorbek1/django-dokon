import json

from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import Restaurant
from .serializers import RestaurantSerializer


@require_GET
def get_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.filter(pk=restaurant_id).first()
    if restaurant:
        serializer = RestaurantSerializer(restaurant)
        return JsonResponse(serializer.data)
    return JsonResponse(
        {
            "ok": False,
            "message": f"restaurant with id={restaurant_id} was not found"
        }
    )


def delete_restaurant(request):
    if request.method != "DELETE":
        return JsonResponse(
                {
                    "ok": False,
                    "message": f"only DELETE requests are accepted"
                }
            )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse(
            {
                "ok": False,
                "message": "data is not a JSON"
            }
        )
    r_id = data.get("id")
    if not r_id:
        return JsonResponse(
            {
                "ok": False,
                "message": "'id' key was not provided."
            }
        )
    try:
        r_id = int(r_id)
    except ValueError:
        return JsonResponse(
            {
                "ok": False,
                "message": "'id' key is not an int."
            }
        )
    r = Restaurant.objects.filter(pk=r_id).first()
    if r:
        r.delete()
        return JsonResponse(
            {
                "ok": True,
                "message": f"restaurant with id={r_id} was successfully deleted"
            }
        )
    return JsonResponse(
            {
                "ok": False,
                "message": f"restaurant with id={r_id} was not found"
            }
        )
