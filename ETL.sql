-- Active: 1755000866348@@127.0.0.1@3306@olist
CREATE TABLE IF NOT EXISTS customers(
    customerId VARCHAR(255) PRIMARY KEY,
    customerUniqueId VARCHAR(255),
    customerZipCodePrefix INT,
    customerCity TEXT,
    customerState TEXT
);
CREATE TABLE IF NOT EXISTS sellers(
    sellerID VARCHAR(255) PRIMARY KEY,
    sellerZipCodePrefix INT,
    sellerCity TEXT,
    sellerState TEXT
);

CREATE TABLE IF NOT EXISTS geolocation(
    geoID INT PRIMARY KEY,
    geoLat FLOAT,
    geoLng FLOAT,
    geoCit TEXT,
    geoSta TEXT
);

CREATE TABLE IF NOT EXISTS products(
    prodID VARCHAR(255) PRIMARY KEY,
    prodCategory TEXT,
    prodNameLen INT,
    prodDescLen INT,
    prodPhotQtd INT,
    prodWeightG INT,
    prodLenCm INT,
    prodHeightCm INT,
    prodWidthCm INT
);

CREATE TABLE IF NOT EXISTS orderitems(
    orderID VARCHAR(255) PRIMARY KEY,
    orderItemID VARCHAR(255),
    productID VARCHAR(255),
    sellerID VARCHAR(255),
    shippingLimit DATETIME,
    price FLOAT,
    freight FLOAT,
    FOREIGN KEY (productID) REFERENCES products(prodID),
    FOREIGN KEY (sellerID) REFERENCES sellers(sellerID)
);

CREATE TABLE IF NOT EXISTS orderpayments(
    orderID VARCHAR(255) PRIMARY KEY,
    paymentSeq INT,
    paymentType TEXT,
    paymentInstallments INT,
    paymentValue FLOAT
);

CREATE TABLE IF NOT EXISTS orderreviews(
    reviewID VARCHAR(255) PRIMARY KEY,
    orderID VARCHAR(255),
    reviewScore INT,
    reviewCommentTitle TEXT,
    reviewCommentMessage TEXT,
    reviewCreationDate DATETIME,
    reviewAnswerTimeStamp DATETIME
);
CREATE TABLE IF NOT EXISTS orders(
    orderID VARCHAR(255),
    customerID VARCHAR(255),
    orderStatus VARCHAR(255),
    orderPurchase DATETIME,
    orderApproved DATETIME,
    orderMidvered DATETIME,
    orderDelivered DATETIME,
    orderEstimated DATETIME
)