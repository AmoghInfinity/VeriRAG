from app.retriever import retrieve_documents
from app.generator import generate_answer
from app.grader import grade_answer
from app.rewriter import rewrite_query
from app.query_splitter import split_query


# run self-healing RAG pipeline (multi-intent aware)
def run_verirag(query: str, max_retries: int = 2):

    print("\n============================")
    print("Original Query:", query)

    sub_queries = split_query(query)

    print("\nSplit Queries:", sub_queries)

    final_answers = []
    total_retries = 0

    # process each sub-query independently
    for idx, sub_query in enumerate(sub_queries):

        print(f"\n########## SUB-QUERY {idx+1} ##########")

        current_query = sub_query
        attempt = 0
        answer = None

        while attempt <= max_retries:

            print(f"\nAttempt {attempt + 1}")
            print(f"Query: {current_query}")

            # retrieve
            documents, _ = retrieve_documents(current_query)

            print("\nRetrieved Documents:\n")
            for i, doc in enumerate(documents):
                print(f"--- Doc {i+1} ---")
                print(doc)
                print()

            # generate
            answer = generate_answer(current_query, documents)

            print("\nGenerated Answer:\n")
            print(answer)

            # grade
            grade = grade_answer(current_query, documents, answer)

            print("\nGrade:", grade)

            # success → break loop
            if grade == "pass":
                print("\nSub-answer accepted.\n")
                break

            # retry with rewrite
            if attempt < max_retries:
                print("\nRewriting query...")

                rewritten = rewrite_query(current_query)

                # clean chained rewrites
                if "->" in rewritten:
                    rewritten = rewritten.split("->")[-1]

                current_query = rewritten.strip()

                print("New Query:", current_query)

            attempt += 1

        # track retries used for this sub-query
        total_retries += attempt

        # fallback if still bad
        if not answer:
            answer = "I don't know"

        final_answers.append(answer)

    # merge all answers
    final_output = "\n\n".join(final_answers)

    print("\n============================")
    print("FINAL OUTPUT:\n", final_output)

    return {
        "answer": final_output,
        "sub_queries": sub_queries,
        "total_subqueries": len(sub_queries),
        "total_retries": total_retries
    }


# interactive test loop
if __name__ == "__main__":
    while True:
        query = input("\nEnter query (or 'exit'): ")

        if query.lower() == "exit":
            break

        result = run_verirag(query)

        print("\n============================")
        print("FINAL OUTPUT:\n", result["answer"])