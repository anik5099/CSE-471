from django.shortcuts import render

def home(request):
    return render(request, 'calculator/home.html')

def about(request):
    return render(request, 'calculator/about.html')

def calculator(request):
    result = None
    error = None

    if request.method == 'POST':
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        operation = request.POST.get('operation')

        try:
            number1 = float(number1)
            number2 = float(number2)

            if operation == 'add':
                result = number1 + number2
            elif operation == 'subtract':
                result = number1 - number2
            elif operation == 'multiply':
                result = number1 * number2
            elif operation == 'divide':
                if number2 == 0:
                    error = 'Cannot divide by zero.'
                else:
                    result = number1 / number2
            else:
                error = 'Invalid operation selected.'

        except ValueError:
            error = 'Please enter valid numbers.'

    context = {
        'result': result,
        'error': error,
    }

    return render(request, 'calculator/calculator.html', context)
