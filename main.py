import math
import statistics
from fastapi import FastAPI , Path , Query 
from typing import List
from pydantic import BaseModel , Field


app = FastAPI()

# Question number 1

@app.get("/even-digits/{number}")
def even_digits(number: int):
    evens = [digit for digit in str(number) if int(digit) % 2 == 0]
    evens.reverse() 
    return {"result": "*".join(evens)}

# Question Number 2 ( Error Due to Overflow Digits even with Science Notation )

@app.get("/compute-expression")
def compute_expression():
    total = 0.0
    for i in range(500):
        numerator = math.factorial((2 * i) + 1)
        denominator = (i + 2)
        term = (numerator / denominator) * (-1)**i

        if abs(term) > 1e308: 
            return {"error": "Computation too large, reduce terms"}

        total += term

    scientific_result = "{:.5e}".format(total)

    return {"result": scientific_result}

# Question Number 3 

@app.get("/four-digit-numbers")
def four_digit_numbers():
    results = []
    for num in range(1000, 10000):
        d1 = (num // 1000)  
        d2 = (num // 100) % 10 
        d3 = (num // 10) % 10  
        d4 = num % 10 

        if (d1 * d2) == (d3 + d4): 
            results.append(num)

    return {"numbers": results}

# Question Number 4

@app.get("/three-digit-even")
def three_digit_even():
    results = [num for num in range(100, 1000) if all(int(d) % 2 == 0 for d in str(num))]
    return {"numbers": results}

# Question Number 5

@app.get("/triangle_pattern/{number}")
def triangle(number: int):
    result = []  

    for i in range(1, number + 1):
        row = " ".join(str(i * j) for j in range(1, i + 1)) 
        result.append(row)  
    
    return {"pattern": result} 

# Question Number 6

class NumberList(BaseModel):
    numbers: List[float]  

@app.post("/compute-statistics")
def compute_statistics(data: NumberList):
    numbers = data.numbers
    
    if len(numbers) == 0:
        return {"error": "List of numbers cannot be empty"}

    max_value = max(numbers)
    min_value = min(numbers)
    avg_value = sum(numbers) / len(numbers)
    std_dev = statistics.stdev(numbers) if len(numbers) > 1 else 0 

    return {
        "max": max_value,
        "min": min_value,
        "average": avg_value,
        "std_dev": std_dev
    }
 
# Question Number 7


class NumberList(BaseModel):
    numbers: List[float]  


def Max1(numbers: List[float]) -> float:
    return max(numbers)

def Min1(numbers: List[float]) -> float:
    return min(numbers)

def Ave1(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

def STD1(numbers: List[float]) -> float:
    return statistics.stdev(numbers) if len(numbers) > 1 else 0 

@app.post("/compute-stats")
def compute_stats(data: NumberList):
    numbers = data.numbers

    if len(numbers) < 2:
        return {"error": "Please provide at least 2 numbers"}

    return {
        "max": Max1(numbers),
        "min": Min1(numbers),
        "average": Ave1(numbers),
        "std_dev": STD1(numbers)
    }

# Question Number 8


class NumberInput(BaseModel):
    number: int 


def F1(number: int) -> int:
    return max(int(digit) for digit in str(number))


def F2(number: int, max_digit: int) -> int:
    number_str = str(number)
    new_number = number_str.replace(str(max_digit), "", 1) 
    return int(new_number) if new_number else 0 
@app.post("/process-number")
def process_number(data: NumberInput):
    number = data.number


    if number < 10000 or number > 99999:
        return {
            "error": "Please provide a valid 5-digit number",
            "original_number": number
        }

    max_digit = F1(number) 
    modified_number = F2(number, max_digit)  

    return {
        "original_number": number,
        "max_digit": max_digit,
        "modified_number": modified_number
    }

