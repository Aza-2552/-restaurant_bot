import sqlite3

def create_users_tabale():
    database = sqlite3.connect('shorva.db')
    cursor =database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT
        );
        ''')
    database.commit()
    database.close()

# create_users_tabale()

def create_carts_tabale():
    database = sqlite3.connect('shorva.db')
    cursor =database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
        cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id REFERENCES users(user_id),
        total_price DECIMAL(12, 2) DEFAULT 0,
        total_products INTEGER DEFAULT 0
    );
    ''')
    database.commit()
    database.close()

# create_carts_tabale()

def create_cart_products_table():
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart_products(
            cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            products_name TEXT,
            quantity INTEGER NOT NULL,
            final_price DECIMAL(12, 2) NOT NULL,
            cart_id INTEGER REFERENCES carts(cart_id),
            
            UNIQUE(products_name, cart_id)
        );
    ''')

    database.commit()
    database.close()

# create_cart_products_table()

def create_categories_table():
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories(
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL UNIQUE
        );
    ''')

    database.commit()
    database.close()

# create_categories_table()

def insert_categories():
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO categories(category_name) VALUES
    ('Beshbarmok 🫕'),
    ('Chuchvara 🥟'),
    ('Do`lma 🧆'),
    ('Kabob 🥘'),
    ('Lag`mon 🍜'),
    ('Norin 🍝'),
    ('Osh 🥗'),
    ('Shorva 🍲'),
    ('Xalim 🍮'),
    ('Xasip 🍛'),
    ('Ichimliklar 🍾')
    ''')
    database.commit()
    database.close()

# insert_categories()

def create_products_table():
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        product_name TEXT NOT NULL,
        price DECIMAL (12, 2) NOT NULL,
        description VARCHAR(100),
        image TEXT,
        
        FOREIGN KEY(category_id) REFERENCES categories(category_id) 
    );
    ''')
    database.commit()
    database.close()

# create_products_table()

def insert_products_table():
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO products(category_id, product_name, price, description, image) VALUES
    (1, 'mol goshtlik beshbarmoq', '65000', '1.5kg mol goshtlik beshbarmoq', 'oshhona_foto/beshbarmok/mol_goshtlik_beshbarmoq.jpg'),
    (1, 'qoy goshtlik beshbarmoq', '65000', '1.5kg qoy goshtlik beshbarmoq', 'oshhona_foto/beshbarmok/qoy_goshtlik_beshbarmoq.jpg'),
    
    (2, 'qaynatma chuchvara', '35000', 'bir kosa qaynatma shirin chuchvara', 'oshhona_foto/chichvara/qaynatma_chuchvara.jpg'),
    (2, 'qovurilgan chuchvara', '35000', 'bir tarelka qovurilgan shirin chuchvara', 'oshhona_foto/chichvara/qovurilgan_chuchvara.webp'),
    
    (3, 'asorti dolma', '45000', 'bir tarelka asorti shirin dolmalar', 'oshhona_foto/dolma/asorti_dolma.jpg'),
    (3, 'toklik dolma', '45000', 'bir tarelka toklik shirin dolmalar', 'oshhona_foto/dolma/toklik_dolma.jpg'),
    
    (4, 'mol goshtlik jaz kabob', '22000', 'shirin mol goshtlik jaz', 'oshhona_foto/kaboblar/mol_goshtlik_jaz_kabob.webp'),
    (4, 'mol goshtlik non kabob', '25000', 'shirin mol goshtlik non kabob', 'oshhona_foto/kaboblar/mol_goshtlik_non_kabob.jpg'),
    (4, 'mol goshtlik qiyma kabob', '20000', ' shirin mol goshtlik qiyma kabob', 'oshhona_foto/kaboblar/mol_goshtlik_qiyma_kabob.webp'),
    (4, 'mol goshtlik qozon kabob', '70000', 'bir lagan shirin mol goshtlik qozon kabob', 'oshhona_foto/kaboblar/mol_goshtlik_qozon_kabob.webp'),
    (4, 'qoy goshtlik jaz kabob', '25000', 'shirin qoy goshtlik jaz kabob', 'oshhona_foto/kaboblar/qoy_goshtlik_jaz_kabob.webp'),
    (4, 'qoy goshtlik non kabob', '23000', 'shirin qoy goshtlik non kabob', 'oshhona_foto/kaboblar/qoy_goshtlik_non_kabob.jpg'),
    (4, 'qoy goshtlik qiyma kabob', '23000', 'shirin qoy goshtlik qiyma kabob', 'oshhona_foto/kaboblar/qoy_goshtlik_qiyma_kabob.webp'),
    (4, 'qoy goshtlik qozon kabob', '75000', 'bir lagan shirin qoy goshtlik qozon kabob', 'oshhona_foto/kaboblar/qoy_goshtlik_qozon_kabob.jpg'),
    (4, 'tovuqlik jaz kabob', '15000', 'shirin tovuqlik jaz kabob', 'oshhona_foto/kaboblar/tovuqlik_jaz_kabob.webp'),
    (4, 'tovuqlik qozon kabob', '60000', 'bir lagan shirin tovuqlik qozon kabob', 'oshhona_foto/kaboblar/tovuqlik_qozon_kabob.webp'),
    
    (5, 'padliv lagmon', '35000', 'shirin padlivliy lagmon', 'oshhona_foto/lagmon/padlivliy_lagmon.webp'),
    (5, 'qovurulgan lagmon', '28000', 'shirin qovurulgan lagmon', 'oshhona_foto/lagmon/qovurulgan_lagmon.webp'),
    (5, 'shorva lagmon', '25000', 'shirin shorva lagmon', 'oshhona_foto/lagmon/shorva_lagmon.webp'),
    
    (6, 'mol goshtlik norin', '35000', 'shirin mol goshtlik norin', 'oshhona_foto/norin/mol_goshtlik_norin.webp'),
    (6, 'ordak goshtlik norin', '45000', 'shirin ordak goshtlik norin', 'oshhona_foto/norin/ordak_goshtlik_norin.jpg'),
    (6, 'ot goshtlik norin', '40000', 'shirin ot goshtlik norin', 'oshhona_foto/norin/ot_goshtlik_norin.jpg'),
    (6, 'qoy goshtlik norin', '45000', 'shirin qoy goshtlik norin', 'oshhona_foto/norin/qoy_goshtlik_norin.jpg'),
    
    (7, 'choy xona oshi', '35000', 'bir tarelka shirin choy xona oshi', 'oshhona_foto/osh/choy_xona_oshi.jpg'),
    (7, 'samarqand mol goshtlik osh', '25000', 'bir tarelka shirin samarqand mol goshtlik osh', 'oshhona_foto/osh/samarqand_mol_goshtlik_osh.webp'),
    (7, 'samarqand qoy goshtlik osh', '28000', 'bir tarelka shirin samarqand qoy goshtlik osh', 'oshhona_foto/osh/samarqand_qoy_goshtlik_osh.webp'),
    (7, 'toshkent mol goshtlik osh', '25000', 'bir tarelka shirin toshkent mol goshtlik osh', 'oshhona_foto/osh/toshkent_mol_goshtlik_osh.jpg'),
    (7, 'toshkent qoy goshtlik osh', '30000', 'bir tarelka shirin toshkent qoy goshtlik osh', 'oshhona_foto/osh/toshkent_qoy_goshtlik_osh.jpg'),
    (7, 'toy oshi', '35000', 'bir tarelka shirin toy oshi', 'oshhona_foto/osh/toy_oshi.webp'),
    
    (8, 'chuchvara shorva', '35000', 'bir kosa shirin chuchvara shorva', 'oshhona_foto/soups/chuchvara_shorva.jpg'),
    (8, 'dolmalik shorva', '35000', 'bir kosa shirin dolmalik shorva', 'oshhona_foto/soups/dolmalik_shorva.webp'),
    (8, 'garox shorva', '35000', 'bir kosa shirin garox shorva', 'oshhona_foto/soups/garox_shorva.webp'),
    (8, 'mastava shorva', '35000', 'bir kosa shirin mastava shorva', 'oshhona_foto/soups/mastava_shorva.jpg'),
    (8, 'mol goshtli shorva', '35000', 'bir kosa shirin mol goshtli shorva', 'oshhona_foto/soups/mol_goshtli_shorva.webp'),
    (8, 'mosh hordalik shorva', '35000', 'bir kosa shirin mosh hordalik shorva', 'oshhona_foto/soups/mosh_hordalik_shorva.webp'),
    (8, 'naxot shorva', '35000', 'bir kosa shirin naxot shorva', 'oshhona_foto/soups/naxot_shorva.jpg'),
    (8, 'qoy goshtlik shorva', '35000', 'bir kosa shirin qoy goshtlik shorva', 'oshhona_foto/soups/qoy_goshtlik_shorva.jpg'),
    (8, 'tovuqliy shorva', '35000', 'bir kosa shirin tovuqliy shorva', 'oshhona_foto/soups/tovuqliy_shorva.webp'),
    (8, 'ugra shorva', '35000', 'bir kosa shirin ugra shorva', 'oshhona_foto/soups/ugrak_shorva.jpg'),
    
    (9, 'mol goshtlik xalim', '45000', 'shirin mol goshtlik xalim', 'oshhona_foto/xalim/mol_goshtlik_xalim.webp'),
    (9, 'ot goshtlik xalim', '45000', 'shirin ot goshtlik xalim', 'oshhona_foto/xalim/ot_goshtlik_xalim.webp'),
    (9, 'qoy goshtlik xalim', '45000', 'shirin qoy goshtlik xalim', 'oshhona_foto/xalim/qoy_goshtlik_xalim.webp'),
    
    (10, 'mol goshtlik xasip', '45000', 'shirin qoy goshtlik xasip', 'oshhona_foto/xasip/mol_goshtlik_xasip.jpg'),
    (10, 'qoy goshtlik xasip', '45000', 'shirin qoy goshtlik xasip', 'oshhona_foto/xasip/qoy_goshtlik_xasip.jpg')
    ''')
    database.commit()
    database.close()

# insert_products_table()

def first_select_user(chat_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE telegram_id = ?
    ''', (chat_id,))
    user = cursor.fetchone()
    database.close()
    return user

def first_register_user(chat_id, full_name):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO users(telegram_id, full_name) VALUES (?, ?)
    ''', (chat_id, full_name))
    database.commit()
    database.close()

def update_user_to_finish_register(chat_id, phone):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
        UPDATE users
        SET phone = ?
        WHERE telegram_id = ?
    ''', (phone, chat_id))
    database.commit()
    database.close()

def insert_to_cart(chat_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO carts(user_id) VALUES
    (
    (SELECT user_id FROM users WHERE telegram_id = ?)
    )
    ''', (chat_id,))
    database.commit()
    database.close()

def get_all_categories():
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM categories;
    ''')
    categories = cursor.fetchall()
    database.close()
    return categories

def get_products_by_category(category_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_id, product_name
    FROM products WHERE category_id = ?
    ''', (category_id,))
    products = cursor.fetchall()
    database.close()
    return products

def get_product_detail(product_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM products
    WHERE product_id = ?
    ''', (product_id,))
    product = cursor.fetchone()
    database.close()
    return product

def get_user_cart_id(chat_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT cart_id FROM carts
    WHERE user_id = (SELECT user_id FROM users WHERE telegram_id = ?)
    ''', (chat_id,))
    cart_id = cursor.fetchone()[0]
    database.close()
    return cart_id

def insert_or_update_cart_product(cart_id, product, quantity, final_price):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()

    try:
        cursor.execute('''
        INSERT INTO cart_products(cart_id, products_name, quantity, final_price)
        VALUES(?, ?, ?, ?)
        ''', (cart_id, product, quantity, final_price))
        database.commit()
        return True
    except:
        cursor.execute('''
        UPDATE cart_products
        SET quantity = ?,
        final_price = ?
        WHERE products_name = ? AND cart_id = ?
        ''', (quantity, final_price, product, cart_id))
        database.commit()
        return False
    finally:
        database.close()

def  update_total_product_total_price(cart_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    UPDATE carts
    SET total_products = (
    SELECT SUM(quantity) FROM cart_products
    WHERE cart_id = :cart_id
    ),
    total_price = (
    SELECT SUM(final_price) FROM cart_products
    WHERE cart_id = :cart_id
    )
    WHERE cart_id = :cart_id
    ''', {'cart_id': cart_id})
    database.commit()
    database.commit()

def get_cart_products(cart_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT products_name, quantity, final_price 
    FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products

def get_total_products_price(cart_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT total_products, total_price FROM carts WHERE cart_id = ?
    ''', (cart_id,))
    total_products, total_price = cursor.fetchone()
    database.close()
    return total_products, total_price

def get_cart_product_for_delete(cart_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT cart_product_id , products_name
    FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products

def delete_cart_product_from_database(cart_product_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products WHERE cart_product_id = ?
    ''', (cart_product_id,))
    database.commit()
    database.close()

def drop_cart_products_default(cart_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    database.commit()
    database.close()

def orders_check():
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders_check(
    order_check_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER REFERENCES carts(cart_id),
    total_price DECIMAL(12, 2) DEFAULT 0,
    total_products INTEGER DEFAULT 0,
    time_order TEXT,
    data_order TEXT
    );
    ''')

# orders_check()

def order():
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_check_id INTEGER REFERENCES orders_check(order_check_id),
        products_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        final_price DECIMAL(12, 2) NOT NULL
    );
    ''')
    database.commit()
    database.close()
# order()

def save_order_check(cart_id, total_products, total_price, time_order, data_order):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders_check(cart_id, total_products, total_price, time_order, data_order)
    VALUES(?, ?, ?, ?, ?)
    ''', (cart_id, total_products, total_price, time_order, data_order))
    database.commit()
    database.close()

def get_order_check_id(cart_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT order_check_id FROM orders_check
    WHERE cart_id = ?
    ''', (cart_id,))
    order_check_id = cursor.fetchall()[-1][0]
    database.close()
    return order_check_id

def save_order(order_check_id, products_name, quantity, final_price):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders(order_check_id, products_name, quantity, final_price)
    VALUES(?, ?, ?, ?) 
    ''', (order_check_id, products_name, quantity, final_price))
    database.commit()
    database.close()

def get_order_check(cart_id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM orders_check
    WHERE cart_id = ?
    ''', (cart_id,))
    orders_check_info = cursor.fetchall()
    database.close()
    return orders_check_info

def get_detail_order(id):
    database = sqlite3.connect('shorva.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT products_name, quantity, final_price FROM orders
    WHERE order_check_id = ?
    ''', (id,))
    detail_order = cursor.fetchall()
    database.close()
    return detail_order









