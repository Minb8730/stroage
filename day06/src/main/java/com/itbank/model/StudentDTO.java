package com.itbank.model;

public class StudentDTO {


//idx	number		pk
//stype	varchar2(20)	check(stype in ('it','ib')
//id	varchar2(20)	unique
//pw	varchar2(500)	not null
//name	varchar2(20)	not null
//phone	varchar2(20)	not null
//birth	varchar2(20)	not null
//rdate	varchar2(20)	default to_char(sysdate, 'yyyy-mm-dd')
//due	number		not null		결제해야될 금액
//sfund	number		default 0	지원금(it면 없고, ib일 때 발생)
//payment	number		default 0	
//status 	varchar2(20)	default '미납'	due - sfund == payment = >'완납'

	private int idx, due, sfund, payment;
	private String stype, id, pw, name, phone, birth, rdate, status;
	
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
	}
	public int getDue() {
		return due;
	}
	public void setDue(int due) {
		this.due = due;
	}
	public int getSfund() {
		return sfund;
	}
	public void setSfund(int sfund) {
		this.sfund = sfund;
	}
	public int getPayment() {
		return payment;
	}
	public void setPayment(int payment) {
		this.payment = payment;
	}
	public String getStype() {
		return stype;
	}
	public void setStype(String stype) {
		this.stype = stype;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPw() {
		return pw;
	}
	public void setPw(String pw) {
		this.pw = pw;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getBirth() {
		return birth;
	}
	public void setBirth(String birth) {
		this.birth = birth;
	}
	public String getRdate() {
		return rdate;
	}
	public void setRdate(String rdate) {
		this.rdate = rdate;
	}
	public String getStatus() {
		return status;
	}
	public void setStatus(String status) {
		this.status = status;
	}
	
	
}
