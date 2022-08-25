from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    req = request.GET.get('from-landing')
    counter_click[req] += 1
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    param = request.GET.get('ab-test-arg')
    counter_show[param] += 1
    if param == 'original':
        return render(request, 'landing.html')
    elif param == 'test':
        return render(request, 'landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    test_conv = 0
    if counter_show['test']:
        test_conv = round(counter_click['test']/ counter_show['test'], 2)

    origin_conv = 0
    if counter_show['original']:
        origin_conv = round(counter_click['original']/ counter_show['original'], 2)
    return render(request, 'stats.html', context={
        'test_conversion': test_conv,
        'original_conversion': origin_conv,
    })
