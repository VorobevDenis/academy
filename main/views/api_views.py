from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from main.models import Department, Employee
from main.pagination import LargeResultsSetPagination
from main.serialize import DepartmentSerializer, EmployeeSerializer


class DepartmentViewSet(ModelViewSet):
    """
    Список департаментов
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeAPIView(ModelViewSet):
    """
    Список сотрудников
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete(self, request, id_employee=None):
        employee = self.queryset.filter(id_employee=id_employee)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class EmployeeUrlList(generics.ListAPIView):
    """
    Список сотрудников отдельно по каждому департаменту, параметр department передается в URL
    """
    serializer_class = EmployeeSerializer
    model = Employee
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        name_department = self.kwargs['department']
        if name_department is not None:
            queryset = self.model.objects.filter(id_department__name_department=name_department)
            return queryset


class EmployeeGetList(generics.ListAPIView):
    """
    Список всех сотрудников, а также отдельно по каждому департаменту, параметр department передается через get запрос
    """
    serializer_class = EmployeeSerializer
    model = Employee
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.model.objects.all()
        name_department = self.request.query_params.get('name_department')
        if name_department is not None:
            queryset = queryset.filter(id_department__name_department=name_department)
        return queryset


class EmployeeFioList(generics.ListAPIView):
    """
    API для получения списка сотрудников + фильтр для поиска по фамилии и по id департамента
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'id_department']
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAuthenticated]

