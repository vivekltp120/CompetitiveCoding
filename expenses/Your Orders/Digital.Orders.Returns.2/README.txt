This is a guide on how to view your returns and refunds data.

Some data fields will have the data value “Not Available”. This means that there was no data present for that field.

It is recommended to view the CSV files in below order.


Digital.Orders.Returns.Transaction.2.csv
- This file has transaction details of your order returns and refunds.
- Use the OrderId field to connect data between the Digital Orders.csv in Digital-Ordering.2.zip and this file.


Digital.Orders.Returns.Monetary.2.csv
- This file has monetary amount details of your order returns and refunds.
- Use the DeliveryPacketId field to connect data between the Digital.Orders.Returns.Transaction.2.csv and this file.
