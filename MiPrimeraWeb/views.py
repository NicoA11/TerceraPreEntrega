from django.shortcuts import render
from .forms import BusquedaForm
from .models import TuModelo  # Asegúrate de importar tu modelo adecuado

def formulario_buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            
            # Lógica para realizar la búsqueda en la base de datos.
            resultados = TuModelo.objects.filter(campo1__icontains=termino_busqueda)
            
            return render(request, 'resultados_busqueda.html', {'resultados': resultados})

    else:
        form = BusquedaForm()

    return render(request, 'formulario_buscar.html', {'form': form})


