import os
import psycopg2
import sys

def run_migration():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))
    sys.path.insert(0, os.path.join(project_root, "backend"))
    from app.config import settings

    print("Connecting to Neon Cloud PostgreSQL...")
    conn = psycopg2.connect(settings.DATABASE_URL)
    cur = conn.cursor()

    sql_file = os.path.join(project_root, "exports", "neon_csv", "neon_schema.sql")
    print(f"Reading schema definition from {sql_file}...")
    with open(sql_file, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    print("Executing schema migrations on Neon...")
    cur.execute(schema_sql)
    conn.commit()
    print("[SUCCESS] Neon schema applied successfully!")

    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY table_name;")
    tables = [r[0] for r in cur.fetchall()]
    print(f"Public tables active on Neon ({len(tables)} total):")
    for t in tables:
        cur.execute(f"SELECT COUNT(*) FROM {t};")
        cnt = cur.fetchone()[0]
        print(f"  - {t}: {cnt} rows")

    cur.close()
    conn.close()

if __name__ == "__main__":
    run_migration()
