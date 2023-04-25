from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


# Create your views here. Serves web pages. returns html;
# url ends with /<number>. number becomes id for this function
# browser calls this function with id passed in
# function renders html back with object passed into in list.html as variable "ls".
# get a ToDoList object, I guess that's a list
def index(response, id):
    ls = ToDoList.objects.get(id=id)  # get a list

    if response.method == "POST":
        print('response.POST', response.POST)
        if response.POST.get("save_check_button"):
            print('ls.item_set.all()', ls.item_set.all())
            for item in ls.item_set.all():
                print('item', item)
                print('item.complete', item.complete)
                if response.POST.get("check_button_" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()
        elif response.POST.get("new_item_input"):
            txt = response.POST.get("new_item_input")  # input box

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(response, "main/list.html", {"ls": ls})  # dict key shows on html


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    print('response.method', response.method)
    if response.method == "POST":
        form = CreateNewList(response.POST)
        print('response.POST', dir(response.POST))

        if form.is_valid():
            form_name = form.cleaned_data["name"]
            print("form_name", form_name)
            todo_list = ToDoList(name=form_name)
            todo_list.save()
            print("todo_list.name", todo_list.name)
            print(ToDoList.objects.all())
            print(f"/{todo_list.id}" )
            return HttpResponseRedirect('/' + str(todo_list.id))
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
