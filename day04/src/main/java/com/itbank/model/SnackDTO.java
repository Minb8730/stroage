package com.itbank.model;

public class SnackDTO {
	
//		IDX   NOT NULL NUMBER       
//		NAME           VARCHAR2(20) 
//		PRICE          NUMBER       
//		CNT            NUMBER       

		private int idx, price, cnt;
		private String name;
		
		public int getIdx() {
			return idx;
		}
		public void setIdx(int idx) {
			this.idx = idx;
		}
		public int getPrice() {
			return price;
		}
		public void setPrice(int price) {
			this.price = price;
		}
		public int getCnt() {
			return cnt;
		}
		public void setCnt(int cnt) {
			this.cnt = cnt;
		}
		public String getName() {
			return name;
		}
		public void setName(String name) {
			this.name = name;
		}
	}


