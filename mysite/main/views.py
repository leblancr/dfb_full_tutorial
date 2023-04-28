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
    print('response.user', response.user)
    print('response.user.is_authenticated', response.user.is_authenticated)
    print('response.method', response.method)
    print('ToDoList.objects', dir(ToDoList.objects))
    print('ToDoList.objects.get(id=id)', ToDoList.objects.get(id=id))

    user_list = ToDoList.objects.get(id=id)  # get user's list

    print('user_list', user_list)
    print('type user_list', type(user_list))
    print('dir user_list', dir(user_list))
    print('user_list.item_set', user_list.item_set)
    print('user_list.item_set.all()', user_list.item_set.all())

    print('response', response)
    print('response.user', response.user)
    print('response.user.todolist', response.user.todolist)
    print('response.user.todolist.all()', response.user.todolist.all())

    # If adding a new item it's a POST, also POST if clicking the Delete checked button
    if response.user.todolist.all():
        if response.method == "POST":
            print('response.POST', response.POST)
            print('response.POST.get("save_check_button")', response.POST.get("save_check_button"))
            if response.POST.get("save_check_button"):
                print('user_list.item_set.all()', user_list.item_set.all())
                # Display all items in the list
                for item in user_list.item_set.all():
                    print('item', item)
                    print('item.complete', item.complete)
                    if response.POST.get("check_button_" + str(item.id)) == "clicked":
                        # delete here
                        # item.complete = True
                        print('dir(item)', dir(item))
                        item.delete()
                    else:
                        item.complete = False

                        item.save()
            elif response.POST.get("new_item_input"):
                txt = response.POST.get("new_item_input")  # input box

                if len(txt) > 2:
                    user_list.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        return render(response, "main/items.html", {"user_list": user_list})  # dict key shows on html
    return render(response, "main/items.html", {})


def home(response):
    print('response.user', response.user)
    print('response.user.is_authenticated', response.user.is_authenticated)
    print('response.method', response.method)

    return render(response, "main/home.html", {})


def create(response):
    print('response.user', response.user)
    print('response.user.is_authenticated', response.user.is_authenticated)
    print('response.method', response.method)
    if response.method == "POST":
        form = CreateNewList(response.POST)
        print('response.POST', dir(response.POST))

        if form.is_valid():
            form_name = form.cleaned_data["name"]
            print("form_name", form_name)
            todolist = ToDoList(name=form_name)
            todolist.save()
            print("todo_list.name", todolist.name)
            print(ToDoList.objects.all())
            print(f"/{todolist.id}" )
            response.user.todolist.add(todolist)

        return HttpResponseRedirect('/' + str(todolist.id))
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})


def lists(response):
    return render(response, "main/lists.html", {})
