import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the API!")



# CRUD for Company
@csrf_exempt
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Save the new company
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def company_detail(request, company_id=None):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        new_data = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=new_data)
        if serializer.is_valid():
            serializer.save()  # Update the company
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'Company deleted'})

# CRUD for Vacancy
@csrf_exempt
def vacancies_list(request):
    if request.method == 'GET':
        # Получение всех вакансий
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = VacancySerializer(data=data)
            if serializer.is_valid():
                serializer.save()  # Сохранение новой вакансии
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse({"error": "Validation failed", "details": serializer.errors}, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON format", "details": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    # Добавьте сюда обработку других методов, если нужно.
    return JsonResponse({"error": "Invalid method"}, status=405)  # Для обработки не поддерживаемых методов


@csrf_exempt
def vacancy_detail(request, vacancy_id=None):
    try:
        vacancy = Vacancy.objects.get(pk=vacancy_id)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy not found'}, status=404)

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        new_data = json.loads(request.body)
        serializer = VacancySerializer(instance=vacancy, data=new_data)
        if serializer.is_valid():
            serializer.save()  # Update the vacancy
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'Vacancy deleted'})


@csrf_exempt
def company_vacancies(request, company_id=None):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)

    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company=company)
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def top_ten_vacancies(request):
    if request.method == 'GET':
        top_vacancies = Vacancy.objects.all().order_by('-salary')[:10]
        serializer = VacancySerializer(top_vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)