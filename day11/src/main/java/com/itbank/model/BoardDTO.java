package com.itbank.model;

import org.springframework.web.multipart.MultipartFile;

//  TABLE : BOARD
//	IDX        NOT NULL NUMBER         
//	TITLE      NOT NULL VARCHAR2(100)  
//	WRITER     NOT NULL VARCHAR2(50)   
//	CONTENT    NOT NULL VARCHAR2(2000) 
//	PASSWORD   NOT NULL VARCHAR2(500)  
//	UPLOADFILE          VARCHAR2(255)  
//	WDATE               VARCHAR2(20)   
//	IPADDR     NOT NULL VARCHAR2(50)   
//	VIEWCOUNT           NUMBER         
//	DELETED             CHAR(1)  

public class BoardDTO {
	private int idx;
	private String title, writer, content, password, uploadFile, wdate, ipaddr;
	private int viewCount;
	private String deleted;
	private MultipartFile file;
	
	@Override
	public String toString() {
		return String.format("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s", 
				  idx, title, writer, content, password, uploadFile, wdate, ipaddr,
		  viewCount, deleted);
	}
	
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
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
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
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
	public String getIpaddr() {
		return ipaddr;
	}
	public void setIpaddr(String ipaddr) {
		this.ipaddr = ipaddr;
	}
	public int getViewCount() {
		return viewCount;
	}
	public void setViewCount(int viewCount) {
		this.viewCount = viewCount;
	}
	public String getDeleted() {
		return deleted;
	}
	public void setDeleted(String deleted) {
		this.deleted = deleted;
	}
	public MultipartFile getFile() {
		return file;
	}
	public void setFile(MultipartFile file) {
		this.file = file;
	}
	
}
