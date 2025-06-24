from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from mytodo.forms import TaskForm # クラスベースビューを継承するのに必要
from .models import Task

# Create your views here.
class IndexView(View):
    def get(self, request): # GETリクエストが送信された時に呼び出される
        # todoリストを取得
        todo_list = Task.objects.all()
        context = {"todo_list": todo_list}

        # テンプレートをレンダリング
        return render(request, "mytodo/index.html", context)

# ビュークラスをインスタンス化
index = IndexView.as_view()

class AddView(View):
    def get(self, request):
        # 空のフォームを作ってテンプレートに渡す
        form = TaskForm()
        # テンプレートのレンダリング処理
        return render(request, "mytodo/add.html", {'form': form})

    def post(self, request, *args, **kwargs):
        # 登録処理
        # 入力データをフォームに渡す
        form = TaskForm(request.POST)
        # 入力データに誤りがないかチェック
        is_valid = form.is_valid()

        # データが正常であれば
        if is_valid:
            # モデルに登録
            form.save()
            return redirect('/')

        # データが正常じゃない
        return render(request, 'mytodo/add.html', {'form': form})

add = AddView.as_view()

class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')

        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()

        return redirect('/')

update_task_complete = Update_task_complete.as_view()

class delete_task(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')

        task = Task.objects.get(id=task_id)
        task.delete()

        return redirect('/')

delete_task = delete_task.as_view()

class EditTaskView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        return render(request, "mytodo/edit_task.html", {"task": task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.start_date = request.POST.get("start_date")
        task.end_date = request.POST.get("end_date")
        task.save()
        return redirect("/")

edit_task = EditTaskView.as_view()