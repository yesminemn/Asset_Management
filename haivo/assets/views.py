from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Asset, Employee

# Create your views here.

# List of all assets
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'list.html', {'assets': assets})

# Lending an asset
def lend_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    
    # If the asset is unavailable, show a warning
    if not asset.available:
        messages.warning(request, 'This asset is currently unavailable for lending.')
        return redirect('asset_list')

    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = get_object_or_404(Employee, id=employee_id)

        # Create a lending record and mark the asset as unavailable
        # Lending.objects.create(asset=asset, employee=employee)
        # asset.available = False
        # asset.save()

        asset.available = False
        asset.save()
        messages.success(request, f"Asset {asset.name} successfully lent to {employee.name}.")
        return redirect('asset_list')

    employees = Employee.objects.all()
    return render(request, 'lend.html', {'asset': asset, 'employees': employees})

# Returning an asset
def return_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        # Mark the asset as available again
        asset.available = True
        asset.save()

        messages.success(request, f"Asset {asset.name} has been returned.")
        return redirect('asset_list')

    return render(request, 'return_asset.html', {'asset': asset})
