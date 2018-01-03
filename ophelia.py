from dao.persons_repository import PersonsRespository


person_repo = PersonsRespository()

result = person_repo.get(1)

print(result[0])