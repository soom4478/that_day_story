from db_connect import get_connection

def user_data():

    con = get_connection()
    cur = con.cursor()

    sql = "SELECT id, userId, userPass, clearCount FROM thatDay.user"
    cur.execute(sql)

    rows = cur.fetchall()

    con.close()

    return rows

def insert_user_data(user_id, user_pass, clear_count):
    # 데이터베이스 연결
    con = get_connection()
    cur = con.cursor()

    # 데이터 삽입 쿼리
    sql = "INSERT INTO thatDay.user (userId, userPass, clearCount) VALUES (%s, %s, %s)"
    try:
        cur.execute(sql, (user_id, user_pass, clear_count))
        con.commit()  # 데이터베이스에 실제로 반영
        print("데이터 삽입 성공")
    except Exception as e:
        print("데이터 삽입 중 오류 발생:", e)
        con.rollback()  # 오류 발생 시 롤백
    finally:
        # 연결 닫기
        con.close()

def user_check(userId, userPass):
    con = get_connection()
    cur = con.cursor()

    sql = "SELECT id, userId, userPass FROM thatDay.user"
    cur.execute(sql)

    rows = cur.fetchall()

    con.close()

    for id, uId, uPass in rows:
        if(uId == userId and uPass == userPass):
            return id

    return 0

# insert_user_data("user123", "user456", 0)
print(user_data())
print(user_check("soo", "soo"))
