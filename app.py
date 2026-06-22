from flask import Flask, render_template, request

app = Flask(__name__)

# Interpolation Search
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]

    if request.method == "POST":

        try:
            target = int(request.form["target"])

            idx_i, comp_i = interpolation_search(arr, target)
            idx_b, comp_b = binary_search(arr, target)

            result = {
                "idx_i": idx_i,
                "comp_i": comp_i,
                "idx_b": idx_b,
                "comp_b": comp_b,
            }

        except:
            result = {
                "idx_i": "Invalid Input",
                "comp_i": "-",
                "idx_b": "Invalid Input",
                "comp_b": "-"
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)