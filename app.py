from flask import Flask, render_template, request
import time
import random

app = Flask(__name__)

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        pos = low + int(((target - arr[low]) * (high - low))
                        / (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
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

    if request.method == "POST":
        target = int(request.form["target"])

        arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]

        idx_i, comp_i = interpolation_search(arr, target)
        idx_b, comp_b = binary_search(arr, target)

        result = {
            "idx_i": idx_i,
            "comp_i": comp_i,
            "idx_b": idx_b,
            "comp_b": comp_b
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()