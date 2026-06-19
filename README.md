# Warsztaty DevOps – CI/CD dla AWS Lambda z wykorzystaniem AWS CLI

## Opis

To repozytorium zawiera szablon projektu wykorzystywany podczas warsztatów DevOps.

Celem zajęć jest zbudowanie kompletnego pipeline'u CI/CD dla prostej aplikacji **Calculator API** oraz automatyczne wdrożenie jej do **AWS Lambda** przy użyciu **AWS CLI** i federacji tożsamości **OIDC (OpenID Connect)**, bez przechowywania długoterminowych kluczy dostępowych.

Podczas warsztatów będziemy krok po kroku budować pipeline, uruchamiać testy oraz wdrażać aplikację do AWS w sposób zgodny z dobrymi praktykami bezpieczeństwa.

---

# Cele warsztatów

Po zakończeniu zajęć będziesz potrafił:

- zrozumieć podstawy działania CI/CD,
- uruchamiać automatyczne testy w pipeline,
- przygotować aplikację Python do wdrożenia na AWS Lambda,
- skonfigurować uwierzytelnianie do AWS z wykorzystaniem OIDC,
- wdrażać i aktualizować funkcje AWS Lambda przy użyciu AWS CLI,
- weryfikować poprawność wdrożenia,
- zrozumieć podstawy automatyzacji wdrożeń oraz Infrastructure as Code (IaC).

---

# Architektura rozwiązania

```text
Programista
      │
      ▼
Repozytorium Git
      │
      ▼
Pipeline CI/CD
 ├── Instalacja zależności
 ├── Uruchomienie testów
 ├── Budowanie obrazu Docker
 ├── Budowanie artefaktu Lambda
 ├── Uwierzytelnienie przez OIDC
 └── Deployment przez AWS CLI
      │
      │
      ▼
AWS Lambda
      │
      ▼
Testowanie aplikacji
```

---

# Struktura projektu

```text
.
── app/
├── tests/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── requirements.txt
├── lambda_handler.py
├── Dockerfile
└── README.md
```

---

# Zadanie 1 – Poznanie aplikacji

## Cel

Zrozumienie działania aplikacji Calculator API.

## Do wykonania

- [ ] Uruchom aplikację lokalnie
- [ ] Przeanalizuj strukturę projektu
- [ ] Zidentyfikuj punkt wejścia dla AWS Lambda

---

# Zadanie 2 – Uruchomienie testów

## Cel

Zweryfikowanie poprawności działania aplikacji.

## Do wykonania

- [ ] Zainstaluj zależności
- [ ] Uruchom testy lokalnie
- [ ] Napraw ewentualne błędy

## Komendy

```bash
# Uzupełnij podczas warsztatów
```

---

# Zadanie 3 – Budowa pipeline'u CI

## Cel

Automatyzacja procesu testowania.

## Do wykonania

- [ ] Utwórz plik workflow
- [ ] Dodaj instalację zależności
- [ ] Dodaj automatyczne uruchamianie testów
- [ ] Zdefiniuj etapy pipeline'u

---

# Zadanie 4 – Konfiguracja uwierzytelniania OIDC

## Cel

Skonfigurowanie bezpiecznego dostępu pipeline'u do AWS bez użycia kluczy dostępowych.

## Do wykonania

- [ ] Utwórz dostawcę tożsamości OIDC w AWS
- [ ] Utwórz rolę IAM dla pipeline'u
- [ ] Skonfiguruj relację zaufania (Trust Relationship)
- [ ] Zweryfikuj możliwość przejęcia roli z poziomu pipeline'u

---

# Zadanie 5 – Przygotowanie paczki wdrożeniowej

## Cel

Przygotowanie artefaktu do wdrożenia na AWS Lambda.

## Do wykonania

- [ ] Utwórz paczkę ZIP
- [ ] Zweryfikuj jej zawartość
- [ ] Dodaj generowanie artefaktu do pipeline'u

## Komendy

```bash
# Uzupełnij podczas warsztatów
```

---

# Zadanie 6 – Wdrożenie do AWS Lambda

## Cel

Automatyczne wdrożenie aplikacji.

## Do wykonania

- [ ] Utwórz funkcję Lambda
- [ ] Wdróż aplikację przy użyciu AWS CLI
- [ ] Dodaj automatyczną aktualizację kodu w pipeline

## Komendy

```bash
# Uzupełnij podczas warsztatów
```

---

# Zadanie 7 – Weryfikacja wdrożenia

## Cel

Potwierdzenie poprawności działania wdrożonej aplikacji.

## Do wykonania

- [ ] Wywołaj funkcję Lambda
- [ ] Przeanalizuj logi
- [ ] Zweryfikuj odpowiedzi Calculator API

---

# Zadanie 8 – Konteneryzacja aplikacji

## Cel

Przygotowanie aplikacji do uruchomienia w środowisku kontenerowym.

## Do wykonania

- [ ] Przeanalizuj plik Dockerfile
- [ ] Zbuduj obraz Docker
- [ ] Uruchom aplikację lokalnie w kontenerze
- [ ] Zweryfikuj działanie aplikacji

## Komendy

```bash
# Uzupełnij podczas warsztatów
```

---

# Zadania dodatkowe (Bonus)

- [ ] Dodaj środowiska `dev` i `prod`
- [ ] Dodaj wdrożenie wyłącznie z gałęzi `main`
- [ ] Dodaj wersjonowanie na podstawie SHA commita
- [ ] Dodaj oddzielne joby `test` i `deploy`
- [ ] Dodaj automatyczne tagowanie wersji
- [ ] Dodaj rollback do poprzedniej wersji Lambda

---

# Lista kontrolna

- [ ] Aplikacja działa lokalnie
- [ ] Testy przechodzą poprawnie
- [ ] Pipeline CI/CD działa
- [ ] OIDC zostało poprawnie skonfigurowane
- [ ] Obraz Docker został zbudowany
- [ ] Artefakt Lambda został przygotowany
- [ ] Aplikacja została wdrożona
- [ ] Wdrożenie zostało zweryfikowane
