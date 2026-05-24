# Amazon Dataset Data Dictionary

| Column Name         | Data Type | Description                                    | Business Relevance             |
| ------------------- | --------- | ---------------------------------------------- | ------------------------------ |
| product_id          | Object    | Unique product identifier                      | Helps track products uniquely  |
| product_name        | Object    | Name of the product                            | Product identification         |
| category            | Object    | Full product category hierarchy                | Product classification         |
| discounted_price    | Float     | Final selling price after discount             | Revenue analysis               |
| actual_price        | Float     | Original product price                         | Price comparison               |
| discount_percentage | Float     | Discount offered on product                    | Marketing & sales analysis     |
| rating              | Float     | Average customer rating                        | Customer satisfaction analysis |
| rating_count        | Integer   | Number of users who rated the product          | Product popularity             |
| about_product       | Object    | Product description/details                    | Product understanding          |
| user_id             | Object    | Unique customer ID                             | Customer tracking              |
| user_name           | Object    | Customer name                                  | User identification            |
| review_id           | Object    | Unique review ID                               | Review tracking                |
| review_title        | Object    | Review heading/title                           | Sentiment analysis             |
| review_content      | Object    | Full customer review text                      | NLP/Text analytics             |
| img_link            | Object    | Product image URL                              | Product visualization          |
| product_link        | Object    | Amazon product URL                             | Product navigation             |
| main_category       | Object    | Simplified top-level category                  | Easier category analysis       |
| savings_amount      | Float     | Difference between actual and discounted price | Savings analysis               |
