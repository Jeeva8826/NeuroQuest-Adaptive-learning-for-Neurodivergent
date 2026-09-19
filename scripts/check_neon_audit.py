import psycopg2

CONN_STR = 'postgresql://neondb_owner:npg_rzHeNO6QRlX4@ep-aged-heart-b52ll5dt-pooler.c-7.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
try:
    conn = psycopg2.connect(CONN_STR, connect_timeout=15)
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY table_name;")
    tables = [row[0] for row in cur.fetchall()]
    print(f'[NEON POSTGRES]: Connected successfully! Total public tables: {len(tables)}')
    for t in tables:
        print(f'  - {t}')
    cur.close()
    conn.close()
except Exception as e:
    print('[NEON POSTGRES ERROR]:', e)
