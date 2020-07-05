from django.shortcuts import render
from django.views import generic
from .models import Employee
from .forms import SearchForm


class IndexView(generic.ListView):
    model = Employee
    paginate_by = 3

    def get_context_data(self):
        """テンプレートへ渡す辞書を作成する"""
        context = super().get_context_data()  # 汎用ビューの既存処理を実行
        context['form'] = SearchForm(self.request.GET)  # 基の辞書にformを追加（入力された検索条件を返却し再度画面表示させる）
        return context

    def get_queryset(self):
        """テンプレートへ渡すemployee_listを作成する"""
        form = SearchForm(self.request.GET)
        form.is_valid()  # required=Falseのため無効になることはないが、これを呼ばないとcleaned_dataができない！
        queryset = super().get_queryset()  # 全社員を取得
        
        department = form.cleaned_data['department']
        if department:
            # 部署名の選択があった場合
            queryset = queryset.filter(department=department)
        club = form.cleaned_data['club']
        if club:
            # サークル名の選択があった場合
            queryset = queryset.filter(club=club)
        return queryset.order_by('-created_at')
