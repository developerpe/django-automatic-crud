from datetime import datetime

from django.http import HttpResponse
from django.views.generic import TemplateView

from openpyxl import Workbook
from openpyxl.styles import (
    Alignment,Border,Font,Side
)
try:
    from openpyxl.cell import get_column_letter
except ImportError:
    from openpyxl.utils import get_column_letter

from automatic_crud.utils import (
    get_model,get_model_fields_names,get_queryset
)

def excel_report_title(__model_name: str):
    date = datetime.now()
    title = "REPORTE DE {0} EN FORMATO EXCEL REALIZADO EN LA FECHA: {1}".format(
                                                                            __model_name.upper(),
                                                                            "%s/%s/%s" % (
                                                                                date.day,date.month,
                                                                                date.year
                                                                            )
                                                                        )
    return title

def validate_id(__field: str):
    if str(__field).lower() is not 'id':
        return True
    return False

class ExcelReportFormat:
    
    def __init__(self,__app_name:str,__model_name:str, *args, **kwargs):
        self.__app_name = __app_name
        self.__model_name = __model_name
        self.__model = get_model(self.__app_name,self.__model_name)
        self.__model_fields_names = get_model_fields_names(self.__model)
        self.__queryset = get_queryset(self.__model)
        self.__report_title = excel_report_title(self.__model_name)
        self.__workbook = Workbook()
        self.__sheetwork = self.__workbook.active

    def __excel_report_header(self,row_dimension = 15, col_dimension = 25):
        self.__sheetwork['B1'].alignment = Alignment(horizontal = "center", vertical = "center")
        self.__sheetwork['B1'].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
                                                top = Side(border_style = "thin"), bottom = Side(border_style = "thin"))
        self.__sheetwork['B1'].font = Font(name = 'Calibri', size = 12, bold = True)
        self.__sheetwork['B1'] = self.__report_title
        __header_letter = '{0}'.format(get_column_letter(len(self.__model_fields_names)).upper())
        self.__sheetwork.merge_cells('B1:{0}1'.format(__header_letter))
        self.__sheetwork.row_dimensions[3].height = row_dimension

        __count = 1
        for __field in self.__model_fields_names:
            __letter = get_column_letter(__count).upper()
            self.__sheetwork['{0}3'.format(__letter)].alignment = Alignment(horizontal = "center", vertical = "center")
            self.__sheetwork['{0}3'.format(__letter)].border = Border(left = Side(border_style = "thin"), right = Side(border_style = "thin"),
                                                top = Side(border_style = "thin"), bottom = Side(border_style = "thin"))
            self.__sheetwork['{0}3'.format(__letter)].font = Font(name = 'Calibri', size = 9, bold = True)
            self.__sheetwork.column_dimensions['{0}'.format(__letter)].height = col_dimension
            __count += 1
    
    def __print_values(self):
        row_count = 4
        col_count = 1
        general_count = len(self.__model_fields_names)
        data = [value for value in self.__queryset]

        for value in data:
            for key,subvalue in value.items():
                if validate_id(key):
                    if general_count > 0:
                        self.__sheetwork.cell(row = row_count, column = col_count).alignment = Alignment(horizontal = "center")
                        self.__sheetwork.cell(row = row_count, column = col_count).border = Border(left = Side(border_style = "thin"),
                                                                    right = Side(border_style = "thin"),top = Side(border_style = "thin"), 
                                                                    bottom = Side(border_style = "thin"))
                        if type(subvalue) is bool:
                            if subvalue is True:
                                self.__sheetwork.cell(row = row_count, column = col_count).value = 'Si'
                            else:
                                self.__sheetwork.cell(row = row_count, column = col_count).value = 'No'
                        else:
                            self.__sheetwork.cell(row = row_count, column = col_count).value = str(subvalue)
                        col_count += 1
                        general_count -= 1

                    if general_count == 0:
                        general_count = len(self.__model_fields_names)
            
            row_count += 1
            col_count = 1

    def get_excel_report(self):
        report_name = "Reporte {0} en Excel .xlsx".format(self.__model_name)
        response = HttpResponse(content_type = "application/ms-excel")
        content = "attachment; filename = {0}".format(report_name)
        response['Content-Disposition'] = content
        self.__workbook.save(response)
        return response

    def build_report(self):
        self.__excel_report_header()
        self.__print_values()

class GetExcelReport(TemplateView):
    def get(self,request,_app_name:str,_model_name:str,*args,**kwargs):
        __report = ExcelReportFormat(_app_name,_model_name)
        __report.build_report()
        return __report.get_excel_report()