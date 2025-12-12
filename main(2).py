from pyscript import document

# Club data
clubs = {
    "N1": {
        "Description": "DESC.",
        "Meeting Time": "Mondays & Tuesdays & Wednesdays 3:45–5:30 PM",
        "Location": "PLACE",
        "Advisor": "Ms. Carabot, Ms. Caballero",
        "Number of Members": "5",
        "Category": "Academic – Technology"
    },
    "N2": {
        "Description": "DESC.",
        "Meeting Time": "Thursdays & Fridays 4:00–5:15 PM",
        "Location": "PLACE",
        "Advisor": "Ms. Caballero, Ms. Carabot",
        "Number of Members": "14",
        "Category": "Academic – Technology"
    },
    "N3": {
        "Description": "DESC.",
        "Meeting Time": "Mondays & Fridays 3:30–4:30 PM",
        "Location": "PLACE",
        "Advisor": "Ms. Solidum, Mr. Calixihan",
        "Number of Members": "22",
        "Category": "Student Development"
    },
    "N4": {
        "Description": "DESC.",
        "Meeting Time": "Tuesdays & Thursdays 3:00–4:15 PM",
        "Location": "PLACE",
        "Advisor": "Mr. De Leon, Mr. Reyes, Mr. Calixihan",
        "Number of Members": "25",
        "Category": "Service & Operations"
    },
}

def show(club_name):
    info_box = document.getElementById("club_info_box")

    if club_name in clubs:
        details = clubs[club_name]
        text = f"Club Name: {club_name}\n"
        for k, v in details.items():
            text += f"{k}: {v}\n"
        info_box.innerText = text
    else:
        info_box.innerText = "No information available."

def RED_Club(e):
    show("N1")

def CT_Club(e):
    show("N2")

def WND_Club(e):
    show("N3")

def CL_Team(e):
    show("N4")