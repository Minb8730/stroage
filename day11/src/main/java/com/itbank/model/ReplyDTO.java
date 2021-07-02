package com.itbank.model;

//idx		number		primary key (sequence)
//bnum		number		foreign key reference board.idx
//writer		varchar2(50)	not null
//content		varchar2(200)	not null
//password		varchar2(255)	not null

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
