package com.itbank.member;

//USERID	VARCHAR2(20 BYTE)
//USERPW	VARCHAR2(130 BYTE)
//USERNAME	VARCHAR2(20 BYTE)
//BIRTH	VARCHAR2(10 BYTE)
//EMAIL	VARCHAR2(50 BYTE)
//GENDER	VARCHAR2(50 BYTE)
//ADDRESS	VARCHAR2(200 BYTE)

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
