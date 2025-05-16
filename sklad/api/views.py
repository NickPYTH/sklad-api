import io
import pandas as pd
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .models import Inventory, Remain, Material


@api_view(['GET'])
def generate_user_report_xlsx(request):
    id = int(request.GET.get('id'))
    inventories = Inventory.objects.all()
    data = []
    #for inventory in inventories:
    inventory = inventories.get(id=id)
    data.append({
        'Номер': inventory.id,
        'Сотрудник проводивший инвентаризацию': inventory.employee.fio,
        'Материал': inventory.materials.all()[0],
        'Учетное количество': inventory.count,
    })
    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Report', index=False)
    output.seek(0)
    response = HttpResponse(
        output.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = 'attachment; filename=report.xlsx'
    response['Content-Transfer-Encoding'] = 'binary'
    return response

@api_view(['GET'])
def generate_second_report_xlsx(request):
    data = []
    for m in Material.objects.all():
        data.append({
            'Материал': m.name,
            'Учетное количество': m.number,
        })

    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Report', index=False)
    output.seek(0)
    response = HttpResponse(
        output.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = 'attachment; filename=report.xlsx'
    response['Content-Transfer-Encoding'] = 'binary'
    return response