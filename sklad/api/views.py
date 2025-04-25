import io
import pandas as pd
from django.http import HttpResponse
from rest_framework.decorators import api_view

from .models import Inventory


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
        'Категория объектов': inventory.category.name,
        'Дата': inventory.date.strftime('%Y-%m-%d'),
        'Учетное количество': inventory.count,
        'Фактическое количество': inventory.count_fact,
        'Состояние': inventory.status.name,
        'Примечание': inventory.description
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