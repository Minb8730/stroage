package com.itbank.model;

//idx		number		primary key
//title		varchar2(50)	not null	
//writer		varchar2(20)	references member2.userid	(FK)
//content		varchar2(2000)	not null
//uploadFile	varchar2(255)	
//viewCount	number		default 0
//wdate		varchar2(20)	default to_char(sysdate, 'yyyy-MM-dd')
//rCount(dto에 추가하기)

public class Board2DTO {

	private int idx, viewCount;
	private String title, writer, content, uploadFile, wdate, rCount;
	private String deleted;
	
	
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
	}
	public int getViewCount() {
		return viewCount;
	}
	public void setViewCount(int viewCount) {
		this.viewCount = viewCount;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
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
	public String getUploadFile() {
		return uploadFile;
	}
	public void setUploadFile(String uploadFile) {
		this.uploadFile = uploadFile;
	}
	public String getWdate() {
		return wdate;
	}
	public void setWdate(String wdate) {
		this.wdate = wdate;
	}
	public String getrCount() {
		return rCount;
	}
	public void setrCount(String rCount) {
		this.rCount = rCount;
	}
	public String getDeleted() {
		return deleted;
	}
	public void setDeleted(String deleted) {
		this.deleted = deleted;
	}
	
	
	
	
}
