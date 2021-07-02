package com.itbank.member2;

//	TABLE : MEMBER2
//	userid      varchar2(20)    primary key,
//	userpw      varchar2(130)   not null,
//	username    varchar2(20)    not null,
//	birth       varchar2(10)    not null,
//	email       varchar2(50)    not null,
//	gender      varchar2(50)    check(gender in ('남', '여')),
//	address     varchar2(200)   not null

public class MemberDTO {
	private String userid, userpw, username, birth, email, gender, address;
	

	public String getUserid() {
		return userid;
	}

	public void setUserid(String userid) {
		this.userid = userid;
	}

	public String getUserpw() {
		return userpw;
	}

	public void setUserpw(String userpw) {
		this.userpw = userpw;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getBirth() {
		return birth;
	}

	public void setBirth(String birth) {
		this.birth = birth;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}
}
