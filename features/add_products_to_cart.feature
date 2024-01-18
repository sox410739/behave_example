Feature: 商品加到購物車
	
	Scenario: 把兩個商品加進購物車
		Given 一個 10 元的餅乾
		And 一個 2 元的糖果
		When 餅乾和糖果被加進購物車
		Then 購物車內的總金額是 12 元
        But 購物車內有 2 樣商品


    Scenario Outline: 把兩個商品加進購物車-多組資料
		Given 一個 <product1_price> 元的 <product1_name>
        And 一個 <product2_price> 元的 <product2_name>
		When 兩樣商品被加進購物車
		Then 購物車內的總金額是 <total_price> 元
        But 購物車內有 2 樣商品
    
        Examples:
            | product1_name | product1_price | product2_name | product2_price | total_price |
            | 餅乾          | 10             | 糖果          | 2              | 12          |
            | 巧克力        | 20             | 糖果          | 2              | 22          |
            | 果汁          | 15             | 紅茶          | 10             | 25          |



