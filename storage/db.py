from supabase import create_client
import os

supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_ANON_KEY"]
)

def get_posts(decision=None, min_relevance=0):
    query = supabase.table("posts").select("*")

    if decision:
        query = query.eq("decision", decision)

    query = query.gte("relevance", min_relevance)

    return query.execute().data
