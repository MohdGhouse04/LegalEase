from src.retrieval.retrieve import retrieve_query

query=input("Ask legal question: ")

results=retrieve_query(query)

print("\nLegalEase Response:\n")

for r in results:
    print(r)