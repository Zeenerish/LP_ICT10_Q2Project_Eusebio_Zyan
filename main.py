from js import document
from pyscript import display

def Calculate(e=None):
    fname = (document.getElementById("Fname").value or "").strip()
    lname = (document.getElementById("Lname").value or "").strip()

    def parse_score(id_):
        raw = (document.getElementById(id_).value or "").strip()
        if raw == "":
            return None, f"Please enter a value for {id_}"
        try:
            return int(raw), None
        except Exception:
            return None, f"Value for {id_} must be a whole number"

    ids = ["Science", "Math", "English", "Filipino", "ICT", "PE"]
    scores = {}
    for i in ids:
        val, err = parse_score(i)
        if err:
            display(err, target="average", append=False)
            return
        scores[i] = val

    total = sum(scores[i] for i in ids)
    averagegrade = round(total / len(ids), 2)

    display(f"Name: {fname} {lname}".strip(), target="name", append=False)
    display(f"Science: {scores['Science']}", target="grades", append=False)
    display(f"Math: {scores['Math']}", target="grades")
    display(f"English: {scores['English']}", target="grades")
    display(f"ICT: {scores['ICT']}", target="grades")
    display(f"Filipino: {scores['Filipino']}", target="grades")
    display(f"PE: {scores['PE']}", target="grades")
    display(f"Your general weighted average is {averagegrade}", target="average", append=False)