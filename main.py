from pyscript import display, document
def compute_average(event):
    #we use this inorder to compute for average
    try:
        s1 = float(document.getElementById("score1").value)
        s2 = float(document.getElementById("score2").value)
        avg = (s1 + s2) / 2
#a block of is executed if a specified condition is true
        if avg >= 75:
            result = f"Average: {avg:.2f} ✔ Passed"
#a block of is executed if a specified condition is false
        else:
            result = f"Average: {avg:.2f} ❌ Failed"

        document.getElementById("output").innerHTML = result  
#we use except Exception in order for python to recognize user's errors like leaving a box blank
    except Exception:
        document.getElementById("output").innerHTML = "Enter Valid Score"


