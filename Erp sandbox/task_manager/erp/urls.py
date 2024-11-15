from django.urls import path
from erp import views

app_name = 'erp'

urlpatterns = [
    # GET /
    path('', views.HomeView.as_view(), name="index"),

    # GET /funcionarios
    path('funcionarios/', views.HomeFuncionarioView.as_view(), name="index_funcionarios"),

    # GET /funcionarios/cadastrar
    path('funcionarios/cadastrar', views.CriaFuncionarioView.as_view(), name="cadastra_funcionario"),

    # GET /funcionarios/lista
    path('funcionarios/lista', views.ListaFuncionariosView.as_view(), name="lista_funcionarios"),

    # GET/POST /funcionarios/{pk}
    path('funcionarios/<pk>', views.AtualizaFuncionarioView.as_view(), name="atualiza_funcionario"),

    # GET/POST /funcionarios/excluir/{pk}
    path('funcionarios/excluir/<pk>', views.DeletaFuncionarioView.as_view(), name="deleta_funcionario"),

    # GET /produtos
    path('produtos/', views.HomeProdutoView.as_view(), name="index_produtos"),

    # GET /produtos/cadastrar
    path('produtos/cadastrar', views.CriaProdutoView.as_view(), name="cadastra_produto"),

    # GET /produtos/lista
    path('produtos/lista', views.ListaProdutosView.as_view(), name="lista_produtos"),

    # GET/POST /produtos/{pk}
    path('produtos/<pk>', views.AtualizaProdutoView.as_view(), name="atualiza_produto"),

    # GET/POST /produtos/excluir/{pk}
    path('produtos/excluir/<pk>', views.DeletaProdutoView.as_view(), name="deleta_produto"),

    # GET /vendas
    path('vendas/', views.HomeVendaView.as_view(), name="index_vendas"),

    # GET /vendas/cadastrar
    path('vendas/cadastrar', views.CriaVendaView.as_view(), name="cadastra_venda"),

    # GET /vendas/lista
    path('vendas/lista', views.ListaVendasView.as_view(), name="lista_vendas"),

    # GET/POST /vendas/{pk}
    path('vendas/<pk>', views.AtualizaVendaView.as_view(), name="atualiza_venda"),

    # GET/POST /vendas/excluir/{pk}
    path('vendas/excluir/<pk>', views.DeletaVendaView.as_view(), name="deleta_venda"),

    # Atividades Routes
    # GET /atividades
    path('atividades/', views.ListaAtividadesView.as_view(), name="index_atividades"),

    # GET /atividades/cadastrar
    path('atividades/cadastrar', views.CriaAtividadeView.as_view(), name="cadastra_atividade"),

    # GET /atividades/lista
    path('atividades/lista', views.ListaAtividadesView.as_view(), name="lista_atividades"),

    # GET/POST /atividades/{pk}
    path('atividades/<pk>', views.AtualizaAtividadeView.as_view(), name="atualiza_atividade"),

    # GET/POST /atividades/excluir/{pk}
    path('atividades/excluir/<pk>', views.DeletaAtividadeView.as_view(), name="deleta_atividade"),
]
