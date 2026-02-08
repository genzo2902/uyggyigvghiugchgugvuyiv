from pyscript import document

def next_page(e):
    document.getElementById("page1").classList.add("hidden")
    document.getElementById("page2").classList.remove("hidden")

def say_yes(e):
    document.getElementById("page2").classList.add("hidden")
    document.getElementById("page3").classList.remove("hidden")
