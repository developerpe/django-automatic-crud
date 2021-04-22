Reporte en Excel
================

Django Automatic CRUD incluye una ruta extra que genera un Reporte en
formato de Excel, este reporte es automatizado, toma el modelo en
cuestión y genera toda la estructura definida, es decir,
``título, cabecera y cuerpo``.

El constructor de esta clase llamada ``ExcelReportFormat``, define las
siguientes variables y parámetros:

::

    Parámetros:
        _app_name                   nombre de la aplicación donde está el modelo en cuestión.
        _model_name                 nombre del modelo a utilizar.

    Variables:
        _app_name                   nombre de la aplicación donde está el modelo en cuestión.
        _model_name                 nombre del modelo a utilizar.
        __model                     modelo a usarse.
        __model_fields_names        lista de campos del modelo.
        __queryset                  queryset del modelo, contiene todos los registros de este.
        __report_title              título del reporte.
        __workbook                  instancia de Workbook.
        __sheetwork                 hoja de Excel a utilizarse, por defecto es la primera.

La construcción del Reporte se realiza por etapas:

-  **Etapa 1** - lo primero que se realiza es la asignación de las
   variables iniciales.

.. code:: python

    def __init__(self,__app_name:str,__model_name:str, *args, **kwargs):
        self.__app_name = __app_name
        self.__model_name = __model_name
        self.__model = get_model(self.__app_name,self.__model_name)
        self.__model_fields_names = get_model_fields_names(self.__model)
        self.__queryset = get_queryset(self.__model)
        self.__report_title = _excel_report_title(self.__model_name)
        self.__workbook = Workbook()
        self.__sheetwork = self.__workbook.active

-  **Etapa 2** - se genera la cabecera del reporte, es decir, los
   nombres de cada campo como cabecera de las celdas donde se pintarán
   cada valor de cada campo, estos campos se obtienen de la variable
   ``__model_fields_names``, en estos no se incluyen los campos que se
   encuentran en el atributo del modelo ``exclude_fields``.

.. code:: python

    def __excel_report_header(self,row_dimension = 15, col_dimension = 25):
        pass

-  **Etapa 3** - se pintan los valores para cada campos que se colocó en
   la cabecera de la tabla, dichos valores se obtienen de la variable
   ``__queryset``.

.. code:: python

        def __print_values(self):

-  **Etapa 4** - se construye la respuesta de tipo ``ms-excel``, se toma
   el título que se genera con la función:

.. code:: python

    def _excel_report_title(__model_name: str):
        """
        Build report title with today date
        """


        date = datetime.now()
        title = "REPORTE DE {0} EN FORMATO EXCEL REALIZADO EN LA FECHA: {1}".format(
                                                                                __model_name.upper(),
                                                                                "%s/%s/%s" % (
                                                                                    date.day,date.month,
                                                                                    date.year
                                                                                )
                                                                            )
        return title

Y se procede a construir una respuesta de tipo HttpResponse a la cual se
le agrega el reporte.

.. code:: python

    def get_excel_report(self):
        pass

-  Etapa 5 - finalmente hay una función que agrupa todos estos pasos, la
   cual construye como tal el reporte.

.. code:: python

    def build_report(self):
        """
        Build report call 2 functions: __excel_report_header and __print_values
        """

        self.__excel_report_header()
        self.__print_values()

--------------

Sin embargo, la clase ``ExcelReportFormat`` NO genera el retorno del
Reporte en Excel que la URL dedicada llama, sino lo retorna la vista
``GetExcelReport``, la cual recibe herencia de ``BaseCrudMixin`` y de
``TemplateView``.

.. code:: python

    class GetExcelReport(BaseCrudMixin,TemplateView):
        pass

