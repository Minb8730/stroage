package com.itbank.board2;

import org.springframework.web.multipart.MultipartFile;

//  TABLE : BOARD2
//	IDX        NOT NULL NUMBER         
//	TITLE      NOT NULL VARCHAR2(50)   
//	WRITER     NOT NULL VARCHAR2(20)   
//	CONTENT    NOT NULL VARCHAR2(2000) 
//	UPLOADFILE NOT NULL VARCHAR2(255)  
//	VIEWCOUNT           NUMBER         
//	WDATE               VARCHAR2(20)   

public class BoardDTO {
	private int idx, viewCount;
	private String title, writer, content; 
	private String uploadFile, wdate;
	private MultipartFile file;
	
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
	public MultipartFile getFile() {
		return file;
	}
	public void setFile(MultipartFile file) {
		this.file = file;
	}
}
