import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="validate_cpf")
def validate_cpf(req: func.HttpRequest) -> func.HttpResponse:

    cpf = req.params.get("cpf")

    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            return func.HttpResponse("Por favor, digite o cpf no formato json, como {\"cpf\": \"xxxxxxxxxxx\"}")
        else:
            cpf = req_body.get("cpf")

            if isinstance(cpf, int):
                cpf = str(cpf)

    if cpf:
        is_valid = is_cpf_valid(cpf)
        return func.HttpResponse("CPF válido" if is_valid else "CPF inválido", status_code=200)
    else:
        return func.HttpResponse(f"Por favor, digite o cpf")

def is_cpf_valid(cpf: str) -> bool:
    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    nums = [int(d) for d in cpf]

    def calc_check_digit(base_digits: list[int]) -> int:
        peso = len(base_digits) + 1
        s = sum(d * peso for d, peso in zip(base_digits, range(peso, 1, -1)))
        r = s % 11
        return 0 if r < 2 else 11 - r

    d1 = calc_check_digit(nums[:9])
    if d1 != nums[9]:
        return False

    d2 = calc_check_digit(nums[:9] + [d1])
    if d2 != nums[10]:
        return False

    return True