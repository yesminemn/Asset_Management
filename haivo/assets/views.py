from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Asset, Employee, Lending

# Create your views here.
def select_employee(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        return redirect('choose_asset', employee_id=employee_id)

    return render(request, 'select_employee.html', {'employees': employees})

def choose_asset(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    assets = Asset.objects.all()

    if request.method == 'POST':
        asset_id = request.POST.get('asset')
        asset = get_object_or_404(Asset, id=asset_id)

        # Check if asset is available
        if asset.available:
            # Mark the asset as lent
            asset.available = False
            asset.save()

            # Create lending record
            Lending.objects.create(asset=asset, employee=employee)

            messages.success(request, f"Asset {asset.name} successfully lent to {employee.name}.")
            return redirect('select_employee')
        else:
            # Check if the asset is already borrowed by the same employee
            lending = Lending.objects.filter(asset=asset).first()
            if lending and lending.employee == employee:
                # Asset already with the employee
                return redirect('return_asset', asset_id=asset.id)
            elif lending:
                # Asset is borrowed by another employee
                messages.error(request, f"Asset {asset.name} is currently unavailable and borrowed by another employee.")
                return redirect('choose_asset', employee_id=employee.id)
            else:
                # No lending record found so asset is unavailable for some other reason
                messages.error(request, "Something went wrong. Asset is not available for use.")
                return redirect('choose_asset', employee_id=employee.id)
    return render(request, 'choose_asset.html', {'assets': assets, 'employee': employee})


# Returning an asset
def return_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    # Fetch the active lending associated with the asset
    lending = Lending.objects.filter(asset=asset).first()  
    employee = lending.employee
    
    if request.method == 'POST':
        # Mark the asset as available again
        asset.available = True
        asset.save()

        # Delete the lending record as the asset is being returned
        if lending:
            lending.delete()

        messages.success(request, f"Asset {asset.name} has been returned by {employee}.")
        return redirect('select_employee')  # Redirect to employee selection

    return render(request, 'return_asset.html', {'asset': asset, 'employee': employee})
