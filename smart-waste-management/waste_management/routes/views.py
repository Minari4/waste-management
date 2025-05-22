from django.db import migrations, models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
import json

from .models import CollectionRoute, RouteBin
from .forms import CollectionRouteForm
from bins.models import WasteBin  # <-- Import the correct model


def is_superuser(user):
    return user.is_superuser


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bins", "0001_initial"),  # Ensure the bins app is a dependency
    ]

    operations = [
        migrations.CreateModel(
            name="RouteBin",
            fields=[
                ("id", models.BigAutoField(primary_key=True)),
                ("collection_order", models.PositiveIntegerField(default=1)),
                (
                    "route",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="routes.CollectionRoute",
                        related_name="route_bins",
                    ),
                ),
                (
                    "bin",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        to="routes.Bin",
                        related_name="route_bin_links",
                    ),
                ),
            ],
            options={
                "ordering": ["collection_order"],
                "unique_together": {("route", "bin")},
            },
        ),
    ]

@login_required
def route_list(request):
    """
    View to display a list of all routes.
    """
    routes = CollectionRoute.objects.all().prefetch_related('bins')
    # Prepare data for the map
    routes_json = []
    for route in routes:
        path = []
        for rb in RouteBin.objects.filter(route=route).select_related('bin').order_by('collection_order'):
            if rb.bin.latitude and rb.bin.longitude:
                path.append({
                    "latitude": rb.bin.latitude,
                    "longitude": rb.bin.longitude
                })
        routes_json.append({
            "id": route.id,
            "name": route.name,
            "is_active": route.is_active,
            "point_a": {
                "latitude": route.point_a_latitude,
                "longitude": route.point_a_longitude
            } if route.point_a_latitude and route.point_a_longitude else None,
            "point_b": {
                "latitude": route.point_b_latitude,
                "longitude": route.point_b_longitude
            } if route.point_b_latitude and route.point_b_longitude else None,
            "path": path
        })
    context = {
        "routes": routes,
        "routes_json": json.dumps(routes_json)
    }
    return render(request, "routes/route_list.html", context)

@login_required
def route_detail(request, pk):
    """
    View to display the details of a specific route.
    """
    route = get_object_or_404(CollectionRoute, pk=pk)
    # Get RouteBin objects for this route, ordered
    route_bins = RouteBin.objects.filter(route=route).select_related('bin').order_by('collection_order')

    point_a = {
        "latitude": route.point_a_latitude,
        "longitude": route.point_a_longitude
    } if route.point_a_latitude and route.point_a_longitude else None

    point_b = {
        "latitude": route.point_b_latitude,
        "longitude": route.point_b_longitude
    } if route.point_b_latitude and route.point_b_longitude else None

    # Pass route_bins to the template
    return render(request, 'routes/route_detail.html', {
        'route': route,
        'route_bins': route_bins,
        'point_a': point_a,
        'point_b': point_b,
    })

@user_passes_test(is_superuser)
def route_edit(request, pk):
    """
    View to edit an existing route.
    """
    route = get_object_or_404(CollectionRoute, pk=pk)
    if request.method == 'POST':
        form = CollectionRouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('routes:route_detail', pk=route.pk)
    else:
        form = CollectionRouteForm(instance=route)
    return render(request, 'routes/route_form.html', {'form': form, 'edit_mode': True, 'route': route})

@user_passes_test(is_superuser)
def route_delete(request, pk):
    """
    View to delete an existing route.
    """
    route = get_object_or_404(CollectionRoute, pk=pk)
    if request.method == 'POST':
        route.delete()
        return redirect('routes:route_list')
    return render(request, 'routes/route_confirm_delete.html', {'route': route})

@user_passes_test(is_superuser)
def route_create(request):
    """
    View to create a new route and automatically add all bins to it.
    """
    if request.method == 'POST':
        form = CollectionRouteForm(request.POST)
        if form.is_valid():
            route = form.save()
            # Automatically add all WasteBins to this route
            all_bins = WasteBin.objects.all()
            for idx, bin in enumerate(all_bins, start=1):
                # Create a RouteBin entry for each WasteBin
                RouteBin.objects.create(
                    route=route,
                    bin=bin,
                    collection_order=idx
                )
            return redirect('routes:route_list')
    else:
        form = CollectionRouteForm()
    return render(request, 'routes/route_form.html', {'form': form, 'edit_mode': False})