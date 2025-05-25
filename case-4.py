import random

def guessthenumber():
    # ���������� ��������� ����� �� 1 �� 100
    secret_number = random.randint(1, 100)
    attempts = 10  # ������������ ���������� �������

    print("����� ���������� � ���� '������ �����'!")
    print("� ������� ����� �� 1 �� 100. � ���� ���� 10 �������, ����� ��� �������!")

    for attempt in range(attempts):
        try:
            guess = int(input(f"������� {attempt + 1}: ����� ���� �������������: "))

            if guess < 1 or guess > 100:
                print("����������, ����� ����� �� 1 �� 100.")
                continue

            if guess < secret_number:
                print("������� ��������� �����!")
            elif guess > secret_number:
                print("������� ������� �����!")
            else:
                print(f"����������! �� ������ ����� {secret_number} �� {attempt + 1} �������!")
                break
        except ValueError:
            print("������: ����������, ����� ���������� ����� �����.")

    else:
        print(f"���, �� �� ������ �����. ��� ���� {secret_number}.")

if name == "main":
    guessthenumber()