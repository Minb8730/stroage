package com.itbank.model;


/*member2 - 가입, 로그인, 정보수정, 탈퇴
	userid		varchar2(20)		primary key
	userpw		varchar2(130)		not null
	username		varchar2(20)		not null
	birth		varchar2(10)
	email		varchar2(50)
	gender		varchar2(10)		check
	address		varchar2(200)
*/


public class Member2DTO {

	private String userId, userPw, userName, birth, email, gender, address;
	private String multipart;
	public String getUserId() {
		return userId;
	}

	public void setUserId(String userId) {
		this.userId = userId;
	}

	public String getUserPw() {
		return userPw;
	}

	public void setUserPw(String userPw) {
		this.userPw = userPw;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
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

	public String getMultipart() {
		return multipart;
	}

	public void setMultipart(String multipart) {
		this.multipart = multipart;
	}
	
	
	
}
