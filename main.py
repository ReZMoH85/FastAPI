import math
import statistics
from fastapi import FastAPI, Path, Query
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Question number 1
# Path Parameter
@app.get("/even-digits/{number}")
def even_digits_path(number: int = Path(...)):
    evens = [digit for digit in str(number) if int(digit) % 2 == 0]
    evens.reverse()
    return {"result": "*".join(evens)}

# Query Parameter
@app.get("/even-digits")
def even_digits_query(number: int = Query(...)):
    evens = [digit for digit in str(number) if int(digit) % 2 == 0]
    evens.reverse()
    return {"result": "*".join(evens)}

# Body Parameter
class NumberInput(BaseModel):
    number: int

@app.post("/even-digits")
def even_digits_body(data: NumberInput):
    evens = [digit for digit in str(data.number) if int(digit) % 2 == 0]
    evens.reverse()
    return {"result": "*".join(evens)}

# Question number 2
# Path Parameter
@app.get("/compute-expression/{terms}")
def compute_expression_path(terms: int = Path(...)):
    total = 0.0
    for i in range(terms):
        numerator = math.factorial((2 * i) + 1)
        denominator = (i + 2)
        term = (numerator / denominator) * (-1) ** i
        if abs(term) > 1e308:
            return {"error": "Computation too large, reduce terms"}
        total += term
    return {"result": "{:.5e}".format(total)}

# Query Parameter
@app.get("/compute-expression")
def compute_expression_query(terms: int = Query(500)):
    total = 0.0
    for i in range(terms):
        numerator = math.factorial((2 * i) + 1)
        denominator = (i + 2)
        term = (numerator / denominator) * (-1) ** i
        if abs(term) > 1e308:
            return {"error": "Computation too large, reduce terms"}
        total += term
    return {"result": "{:.5e}".format(total)}

# Body Parameter
class TermsInput(BaseModel):
    terms: int

@app.post("/compute-expression")
def compute_expression_body(data: TermsInput):
    total = 0.0
    for i in range(data.terms):
        numerator = math.factorial((2 * i) + 1)
        denominator = (i + 2)
        term = (numerator / denominator) * (-1) ** i
        if abs(term) > 1e308:
            return {"error": "Computation too large, reduce terms"}
        total += term
    return {"result": "{:.5e}".format(total)}

# Question number 3
# Path Parameter
@app.get("/four-digit-numbers/{limit}")
def four_digit_numbers_path(limit: int = Path(...)):
    results = [num for num in range(1000, 1000 + limit)
               if (num // 1000) * ((num // 100) % 10) == ((num // 10) % 10) + (num % 10)]
    return {"numbers": results}

# Query Parameter
@app.get("/four-digit-numbers")
def four_digit_numbers_query(limit: int = Query(...)):
    results = [num for num in range(1000, 1000 + limit)
               if (num // 1000) * ((num // 100) % 10) == ((num // 10) % 10) + (num % 10)]
    return {"numbers": results}

# Body Parameter
class LimitInput(BaseModel):
    limit: int

@app.post("/four-digit-numbers")
def four_digit_numbers_body(data: LimitInput):
    results = [num for num in range(1000, 1000 + data.limit)
               if (num // 1000) * ((num // 100) % 10) == ((num // 10) % 10) + (num % 10)]
    return {"numbers": results}

# Question number 4
# Path Parameter
@app.get("/three-digit-even/{limit}")
def three_digit_even_path(limit: int = Path(...)):
    results = [num for num in range(100, 100 + limit) if all(int(d) % 2 == 0 for d in str(num))]
    return {"numbers": results}

# Query Parameter
@app.get("/three-digit-even")
def three_digit_even_query(limit: int = Query(...)):
    results = [num for num in range(100, 100 + limit) if all(int(d) % 2 == 0 for d in str(num))]
    return {"numbers": results}

# Body Parameter
@app.post("/three-digit-even")
def three_digit_even_body(data: LimitInput):
    results = [num for num in range(100, 100 + data.limit) if all(int(d) % 2 == 0 for d in str(num))]
    return {"numbers": results}

# Question Nummber 5
# Path Parameter
@app.get("/triangle_pattern/{number}")
def triangle(number: int):
    result = []  
    for i in range(1, number + 1):
        row = " ".join(str(i * j) for j in range(1, i + 1)) 
        result.append(row)  
    return {"pattern": result}

# Query Paramater
@app.get("/triangle_pattern")
def triangle(number: int = Query(...)):
    result = []  
    for i in range(1, number + 1):
        row = " ".join(str(i * j) for j in range(1, i + 1)) 
        result.append(row)  
    return {"pattern": result}

# Body Parameter
class NumberInput(BaseModel):
    number: int

@app.post("/triangle_pattern")
def triangle(data: NumberInput):
    result = []  
    for i in range(1, data.number + 1):
        row = " ".join(str(i * j) for j in range(1, i + 1)) 
        result.append(row)  
    return {"pattern": result}


# Question number 6
# Path Parameter
@app.get("/compute-statistics/{values}")
def compute_statistics_path(values: str = Path(...)):
    numbers = list(map(float, values.split(",")))
    if not numbers:
        return {"error": "List of numbers cannot be empty"}
    return {
        "max": max(numbers),
        "min": min(numbers),
        "average": sum(numbers) / len(numbers),
        "std_dev": statistics.stdev(numbers) if len(numbers) > 1 else 0
    }

# Query Parameter
@app.get("/compute-statistics")
def compute_statistics_query(numbers: List[float] = Query(...)):
    if not numbers:
        return {"error": "List of numbers cannot be empty"}
    return {
        "max": max(numbers),
        "min": min(numbers),
        "average": sum(numbers) / len(numbers),
        "std_dev": statistics.stdev(numbers) if len(numbers) > 1 else 0
    }

# Body Parameter
class NumberList(BaseModel):
    numbers: List[float]

@app.post("/compute-statistics")
def compute_statistics_body(data: NumberList):
    numbers = data.numbers
    if not numbers:
        return {"error": "List of numbers cannot be empty"}
    return {
        "max": max(numbers),
        "min": min(numbers),
        "average": sum(numbers) / len(numbers),
        "std_dev": statistics.stdev(numbers) if len(numbers) > 1 else 0
    }

# Question number 8
# Path Parameter
@app.get("/process-number/{number}")
def process_number_path(number: int = Path(...)):
    if number < 10000 or number > 99999:
        return {"error": "Please provide a valid 5-digit number", "original_number": number}
    max_digit = max(int(digit) for digit in str(number))
    modified_number = int(str(number).replace(str(max_digit), "", 1)) if str(number).replace(str(max_digit), "", 1) else 0
    return {"original_number": number, "max_digit": max_digit, "modified_number": modified_number}

# Query Parameter
@app.get("/process-number")
def process_number_query(number: int = Query(...)):
    if number < 10000 or number > 99999:
        return {"error": "Please provide a valid 5-digit number", "original_number": number}
    max_digit = max(int(digit) for digit in str(number))
    modified_number = int(str(number).replace(str(max_digit), "", 1)) if str(number).replace(str(max_digit), "", 1) else 0
    return {"original_number": number, "max_digit": max_digit, "modified_number": modified_number}

# Body Parameter
class NumberInput(BaseModel):
    number: int

@app.post("/process-number")
def process_number_body(data: NumberInput):
    number = data.number
    if number < 10000 or number > 99999:
        return {"error": "Please provide a valid 5-digit number", "original_number": number}
    max_digit = max(int(digit) for digit in str(number))
    modified_number = int(str(number).replace(str(max_digit), "", 1)) if str(number).replace(str(max_digit), "", 1) else 0
    return {"original_number": number, "max_digit": max_digit, "modified_number": modified_number}
