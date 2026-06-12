USE store;

INSERT IGNORE INTO products(product_id, product_name, category, price, stock) VALUES
	('PRO001' , 'Mi instan'		, 'Food' 		  , 3500 	, 100),
    ('PRO002' , 'Detergen'		, 'Household' 	  , 30000	, 150),
    ('PRO003' , 'Cat rambut'	, 'Personal care' , 65000   , 60),
    ('PRO004' , 'Coklat'		, 'Snack' 		  , 8000	, 120),
    ('PRO005' , 'Air mineral'	, 'Beverage' 	  , 4000	, 200);
    
INSERT IGNORE INTO customers(customer_id, customer_name, gender, phone_number, address) VALUES
	('CUS001' , 'Enjel' , 'Female' , '0819-1818-2003' , 'Tangerang Selatan'),
    ('CUS002' , 'Nadya' , 'Female' , '0814-8291-7364' , 'Makassar'),
    ('CUS003' , 'Valen' , 'Female' , '0817-3190-5482' , 'Belitung'),
    ('CUS004' , 'Elmar' , 'Male'   , '0815-8420-3917' , 'Jakarta Barat'),
    ('CUS005' , 'Mika'  , 'Male'   , '0819-2647-1538' , 'Kemang'),
    ('CUS006' , 'Rafi'  , 'Male'   , '0813-1784-5206' , 'Bintaro'),
    ('CUS007' , 'Adam'  , 'Male'   , '0816-4091-8275' , 'Aceh');
    
INSERT IGNORE INTO cashiers(cashier_id, cashier_name, username, password, shift) VALUES
	('CAS001' , 'Athiyyah' , 'athiyyah' , 'athiyyah123' , 'Morning'),
    ('CAS002' , 'Donny'	   , 'donny'	, 'donny123'	, 'Evening'),
    ('CAS003' , 'Hane'	   , 'hane'	    , 'hane123'	    , 'Night'),
    ('CAS004' , 'Yoanita'  , 'yoanita'  , 'yoanita123'  , 'Morning'),
    ('CAS005' , 'Yonathan' , 'yonathan'	, 'yonathan123' , 'Evening'),
    ('CAS006' , 'Pirlo'	   , 'pirlo'	, 'pirlo123'	, 'Night'),
    ('CAS007' , 'Zian'	   , 'zian'	    , 'zian123'	    , 'Night');
    
INSERT IGNORE INTO suppliers(supplier_id, supplier_name, contact_number, address, email) VALUES
	('SUP001' , 'PT Indofood CBP Sukses Makmur Tbk.' , '021-5795-8822'  , 'Jakarta Selatan' , 'indofood@gmail.com'),
    ('SUP002' , 'PT Unilever Indonesia Tbk.'		 , '025-1867-2409'  , 'Bogor'			, 'unilever@gmail.com'),
    ('SUP003' , 'PT Eres Revco'						 , '021-525-6976'   , 'Jakarta Selatan' , 'eres.revco@gmail.com'),
    ('SUP004' , 'PT Nestle Indonesia'				 , '021-7883-6000'  , 'Bekasi'			, 'nestle@gmail.com'),
    ('SUP005' , 'PT Tirta Fresindo Jaya'			 , '0838-3924-0777' , 'Jakarta Barat'	, 'tirta.fresindo@gmail.com');

INSERT IGNORE INTO transactions(transaction_id, transaction_date, customer_id, cashier_id, total_price, payment_method) VALUES
	('TRA001' , '2026-04-15' , 'CUS001' , 'CAS001' , 37000 , 'QRIS'),
    ('TRA002' , '2026-04-23' , 'CUS002' , 'CAS002' , 12000 , 'Debit card'),
    ('TRA003' , '2026-04-28' , 'CUS003' , 'CAS003' , 95000 , 'Cash'),
    ('TRA004' , '2026-05-09' , 'CUS004' , 'CAS004' , 37500 , 'Credit card'),
    ('TRA005' , '2026-05-20' , 'CUS005' , 'CAS005' , 30500 , 'QRIS');
    
INSERT IGNORE INTO transaction_details(detail_id, transaction_id, product_id, quantity, sub_total) VALUES
	('DET001' , 'TRA001' , 'PRO001' , 2 , 7000),
    ('DET002' , 'TRA001' , 'PRO002' , 1 , 30000),
    ('DET003' , 'TRA002' , 'PRO004' , 1 , 8000),
    ('DET004' , 'TRA002' , 'PRO005' , 1 , 4000),
    ('DET005' , 'TRA003' , 'PRO002' , 1 , 30000),
    ('DET006' , 'TRA003' , 'PRO003' , 1 , 65000),
    ('DET007' , 'TRA004' , 'PRO001' , 5 , 17500),
    ('DET008' , 'TRA004' , 'PRO005' , 5 , 20000),
    ('DET009' , 'TRA005' , 'PRO001' , 3 , 10500),
    ('DET010' , 'TRA005' , 'PRO005' , 5 , 20000);
    
INSERT IGNORE INTO product_suppliers(product_supplier_id, supplier_id, supplier_price, supply_date, stock_supplied, product_id) VALUES
	('PSU001' , 'SUP001' , 3000  , '2025-07-13' , 50  , 'PRO001'),
    ('PSU002' , 'SUP002' , 28000 , '2025-08-28' , 80  , 'PRO002'),
    ('PSU003' , 'SUP003' , 60000 , '2025-09-01' , 60  , 'PRO003'),
    ('PSU004' , 'SUP004' , 7000  , '2025-11-19' , 70  , 'PRO004'),
    ('PSU005' , 'SUP005' , 3500  , '2025-12-23' , 200 , 'PRO005');