package com.itbank.model;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.web.multipart.MultipartFile;

public class GalleryDTO {
//	IDX              NOT NULL NUMBER        
//	ORIGINALFILENAME NOT NULL VARCHAR2(500) 
//	STOREDFILENAME   NOT NULL VARCHAR2(500) 
//	UPLOADDATE                VARCHAR2(500) 

	private int idx;
	private String originalFileName, storedFileName, uploadDate;
	private MultipartFile uploadFile;
	
	public boolean ready() {
		// uploadFile을 이용하여, originalFileName 과 storedFileName 값을 만든다.
		if(uploadFile != null) {
			originalFileName = uploadFile.getOriginalFilename();
			SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd-hh-mm-ss");
			String now = sdf.format(new Date());
			storedFileName = now + "-" + originalFileName;
			return true;
		}
		return false;
	}
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
	}
	public String getOriginalFileName() {
		return originalFileName;
	}
	public void setOriginalFileName(String originalFileName) {
		this.originalFileName = originalFileName;
	}
	public String getStoredFileName() {
		return storedFileName;
	}
	public void setStoredFileName(String storedFileName) {
		this.storedFileName = storedFileName;
	}
	public String getUploadDate() {
		return uploadDate;
	}
	public void setUploadDate(String uploadDate) {
		this.uploadDate = uploadDate;
	}
	public MultipartFile getUploadFile() {
		return uploadFile;
	}
	public void setUploadFile(MultipartFile uploadFile) {
		this.uploadFile = uploadFile;
	}
	
	
	
	
	
	
}
