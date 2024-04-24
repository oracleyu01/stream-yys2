import cx_Oracle
import pandas as pd
import streamlit as st

def table_def(table_name):
    import cx_Oracle
    import pandas as pd
    import streamlit as st

    # Connection details
    dsn = cx_Oracle.makedsn('192.168.19.14', 8081, 'orcl')
    db = cx_Oracle.connect('system', 'oracle_4U', dsn)
    
    cursor = db.cursor()
    # Execute SQL query
    query = f"""
    SELECT A.COLUMN_ID AS NO
         , B.COMMENTS AS "논리명"
         , A.COLUMN_NAME AS "물리명"
         , A.DATA_TYPE AS "자료형태"
         , A.DATA_LENGTH AS "길이"
         , DECODE(A.NULLABLE, 'N', 'No', 'Y', 'Yes') AS "Null허용"
         , A.DATA_DEFAULT AS "기본값"
    FROM ALL_TAB_COLUMNS A
    LEFT JOIN ALL_COL_COMMENTS B
      ON A.OWNER = B.OWNER
     AND A.TABLE_NAME = B.TABLE_NAME
     AND A.COLUMN_NAME = B.COLUMN_NAME
    WHERE A.TABLE_NAME = :tbl_name 
    ORDER BY A.COLUMN_ID
    """
    cursor.execute(query, tbl_name=table_name.upper())
    
    # Fetch data and metadata for column names
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]  # Get column names from description

    # Create DataFrame with correct column names
    df = pd.DataFrame(rows, columns=columns)

    cursor.close()  # It's good practice to close cursor and connection
    db.close()

    return df


a =table_def('EMP')
st.dataframe(a)  # Same as st.write(df)
