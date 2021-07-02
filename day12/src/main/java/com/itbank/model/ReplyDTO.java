package com.itbank.model;

//	TABLE : REPLY
//	IDX      NOT NULL NUMBER        
//	BNUM              NUMBER        
//	WRITER   NOT NULL VARCHAR2(50)  
//	CONTENT  NOT NULL VARCHAR2(200) 
//	PASSWORD NOT NULL VARCHAR2(255)

public class ReplyDTO {

	private int idx, bnum;
	private String writer, content, password;
	
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
	}
	public int getBnum() {
		return bnum;
	}
	public void setBnum(int bnum) {
		this.bnum = bnum;
	}
	public String getWriter() {
		return writer;
	}
	public void setWriter(String writer) {
		this.writer = writer;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	
	
}
