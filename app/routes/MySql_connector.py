"""pymysql을 이용해 쿼리를 처리하는 프로그램입니다. 쿼리를 처리하려면? 적절한 변수가 입력되어야지요!"""

import pymysql,datetime,time

DBHOST = 'localhost'
DBPort = 8080
DBUser = 'root'
DBPassword = 'rhkdtks!0315'
DBDb = 'example'

class mysql_connector:
    """DB와 연결될 커넥터 클래스입니다. 이 클래스가 mysql DB와 연결되는 작업을 합니다."""

    def __init__(self,DB_host,DB_port,DB_user,DB_password,DB_db):
        self.DB_host = DB_host
        self.DB_port = DB_port
        self.DB_user = DB_user
        self.DB_password = DB_password
        self.DB_db = DB_db

    def connect_DB(self):
        try:
            self.connect = pymysql.connect(host=self.DB_host, port=self.DB_port, user=self.DB_user, password=self.DB_password, database=self.DB_db)
        except:
            self.connect.close()

    ##
    # Cart 테이블 DML
    ##

    def insert_cart(self, start_time, cart_num, cart_mac):
        try:
            with self.connect.cursor() as cursor:
                sql = "insert into Cart(Start_time,Cart_num,Cart_mac) values(%s,%s,%s)"
                cursor.execute(sql, (start_time.strftime("%Y-%m-%d %H:%M:%S"), cart_num, cart_mac))
                print(self.connect.commit())

        except:
            self.connect.close()

    def update_cart_end(self, cart_id, end_time):
        try:
            with self.connect.cursor() as cursor:
                sql = "update Cart set End_time = %s where Cart_id = %s"
                cursor.execute(sql, (end_time.strftime("%Y-%m-%d %H:%M:%S"), cart_id))
                print(self.connect.commit())

        except:
            self.connect.close()

    def delete_cart(self, cart_id):
        try:
            with self.connect.cursor() as cursor:
                sql = "delete from Cart where Cart_id = %s"
                cursor.execute(sql,cart_id )
                print(self.connect.commit())

        except:
            self.connect.close()

    ##
    # location 테이블 DML
    ##

    def insert_location(self,description,location_type):
        try:
            with self.connect.cursor() as cursor:
                sql = "insert into location(Description, location_type) values(%s, %s)"
                cursor.execute(sql, (description,location_type))
                print(self.connect.commit())

        except:
            self.connect.close()

    def update_location(self, location_id, description, location_type):
        try:
            with self.connect.cursor() as cursor:
                sql = "update location set description = %s, location_type = %s where location_id = %s"
                cursor.execute(sql, (description,location_type, location_id))
                print(self.connect.commit())

        except:
            self.connect.close()

    def delete_location(self,location_id):
        try:
            with self.connect.cursor() as cursor:
                sql = "delete from location where location_id = %s"
                cursor.execute(sql, location_id)
                print(self.connect.commit())

        except:
            self.connect.close()

    ##
    # Node 테이블 DML
    ##

    def insert_node(self,card_id,location_id,category):
        try:
            with self.connect.cursor() as cursor:
                sql = "insert into Node(card_id,location_id,category) values(%s,%s,%s)"
                cursor.execute(sql, (card_id,location_id,category))
                print(self.connect.commit())

        except:
            self.connect.close()

    def update_node(self,card_id,location_id,category):
        try:
            with self.connect.cursor() as cursor:
                sql = "update node set location_id = %s, category = %s where card_id = %s"
                cursor.execute(sql, (location_id,category, card_id))
                print(self.connect.commit())

        except:
            self.connect.close()

    def delete_node(self,card_id):
        try:
            with self.connect.cursor() as cursor:
                sql = "delete from Node where card_id = %s"
                cursor.execute(sql, card_id)
                print(self.connect.commit())

        except:
            self.connect.close()

    ##
    # Edge 테이블 DML
    ##

    def insert_edge(self,node_id1,node_id2):
        try:
            with self.connect.cursor() as cursor:
                sql = "insert into Edge(node_id1,node_id2) values(%s,%s)"
                cursor.execute(sql, (node_id1,node_id2))
                print(self.connect.commit())

        except:
            self.connect.close()

    def update_edge(self,edge_id,node_id1,node_id2):
        try:
            with self.connect.cursor() as cursor:
                sql = "update Edge set node_id1 = %s, node_id2=%s where edge_id = %s"
                cursor.execute(sql, (node_id1,node_id2,edge_id))
                print(self.connect.commit())

        except:
            self.connect.close()

    def delete_edge(self,edge_id):
        try:
            with self.connect.cursor() as cursor:
                sql = "delete from Edge where card_id = %s"
                cursor.execute(sql, edge_id)
                print(self.connect.commit())

        except:
            self.connect.close()

    ##
    #Sign 테이블 DML
    ##

    def insert_sign(self,cart_id,node_id,sign_time):
        try:
            with self.connect.cursor() as cursor:
                sql = "insert into Sign(Cart_id,Node_id,Sign_time) values(%s,%s,%s)"
                cursor.execute(sql, (cart_id,node_id,sign_time))
                print(self.connect.commit())

        except:
            self.connect.close()

    def update_sign(self,sign_id,cart_id,node_id,sign_time):
        try:
            with self.connect.cursor() as cursor:
                sql = "update Edge set Cart_id = %s, Node_id=%s, Sign_time=%s where Sign_id = %s"
                cursor.execute(sql, (cart_id, node_id, sign_time,sign_id))
                print(self.connect.commit())

        except:
            self.connect.close()

    def delete_sign(self,sign_id):
        try:
            with self.connect.cursor() as cursor:
                sql = "delete from Sign where Sign_id = %s"
                cursor.execute(sql, sign_id)
                print(self.connect.commit())

        except:
            self.connect.close()

    ##
    # 해당 노드에 몇번의 신호가 왔는지(=카트들이 몇번 지나갔는지)를 파악하는 SQL입니다.
    ##

    def node_statistic(self,card_id):
        try:
            with self.connect.cursor() as cursor:
                sql = "select card_id,count(Sign_id) from Node NATURAL JOIN Sign group by card_id having card_id = %s"
                cursor.execute(sql, card_id)
                result = cursor.fetch
                print(self.connect.commit())
                return result

        except:
            self.connect.close()
            return null

    ##
    # 노드와 엣지를 읽고 그래프 인접행렬을 그리는 함수입니다.
    ##

    def graph_create(self):
        try:
            node_index = 0
            node_dict = []
            with self.connect.cursor() as cursor:
                sql = "select node_id from Node"
                cursor.execute(sql)
                result = cursor.fetchall()
                for node in result:
                    node_dict.insert(node,node_index++ )
            with self.connect.cursor() as cursor:
                sql = "select node_id,node_id2 from Node NATURAL JOIN Edge"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(self.connect.commit())
                return result

        except:
            self.connect.close()
            return null


connector = mysql_connector(DBHOST,DBPort,DBUser,DBPassword,DBDb)
connector.connect_DB()

