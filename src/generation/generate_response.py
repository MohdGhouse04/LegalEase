from src.retrieval.retrieve import retrieve_query

query=input("Ask legal question: ")

results=retrieve_query(query)

print("\nLegalEase Answer:\n")

# Simple generated response (rule-based version)
for chunk in results[:1]:
    print("Based on retrieved legal provisions:")
    print(chunk)