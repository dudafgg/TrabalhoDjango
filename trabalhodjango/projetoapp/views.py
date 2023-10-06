from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemEstoque
from .forms import ItemEstoqueForm

def lista_estoque(request):
    itens = ItemEstoque.objects.all()
    
    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estoque')

    else:
        form = ItemEstoqueForm()

    return render(request, 'projetoapp/lista_estoque.html', {'itens': itens, 'form': form})

def adicionar_item_estoque(request):
    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estoque')

    else:
        form = ItemEstoqueForm()

    return render(request, 'projetoapp/adicionar_item_estoque.html', {'form': form})

def detalhes_item_estoque(request, item_id):
    item = get_object_or_404(ItemEstoque, pk=item_id)

    return render(request, 'projetoapp/detalhes_item_estoque.html', {'item': item})

def editar_item_estoque(request, item_id):
    item = get_object_or_404(ItemEstoque, pk=item_id)

    if request.method == 'POST':
        form = ItemEstoqueForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('lista_estoque')
    else:
        form = ItemEstoqueForm(instance=item)

    return render(request, 'projetoapp/editar_item_estoque.html', {'form': form})

def confirmar_exclusao_item_estoque(request, item_id):
    item = get_object_or_404(ItemEstoque, pk=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('lista_estoque')

    return render(request, 'projetoapp/confirmar_exclusao_item_estoque.html', {'item': item})
