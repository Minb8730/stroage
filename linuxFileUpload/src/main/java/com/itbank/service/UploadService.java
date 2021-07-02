package com.itbank.service;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.jcraft.jsch.Channel;
import com.jcraft.jsch.ChannelSftp;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;
import com.jcraft.jsch.SftpException;

@Service
public class UploadService {

	private final String serverIP = "192.168.0.91"; // 본인의 IP
	private final int serverPort = 22;
	private final String serverUser = "root";
	private final String serverPass = "1";
	private ChannelSftp chSftp = null;
			
			
			
	public String upload(MultipartFile file) throws JSchException, IllegalStateException, IOException, SftpException {
		
		Session sess = null;
		Channel channel = null;
		JSch jsch = new JSch();
		
		sess = jsch.getSession(serverUser, serverIP, serverPort);
		sess.setPassword(serverPass);
		sess.setConfig("StrictHostKeyChecking", "no");
		
		sess.connect();
		System.out.println("sftp> Connected !!");
		
		channel = sess.openChannel("sftp"); 		//sftp(파일전송) 모드로 채널을 연다.
		channel.connect();
		
		chSftp = (ChannelSftp)channel;			// 전송 준비 끝
				
		File tmp = new File(file.getOriginalFilename());
		file.transferTo(tmp);		//웹 서버에 파일이 생성됨(임시파일)
		
		FileInputStream fis = new FileInputStream(tmp);
		chSftp.cd("/var/www/html");			// cd/ var/www/html
		chSftp.put(fis, file.getOriginalFilename());		//put iu.jpg
		
		System.out.println("sftp> transfer complete !!");	// 전송 완료
		
		fis.close();
		chSftp.exit();
		tmp.delete();
		
		System.out.println("sftp > exit");
		
		
		return "http://" + serverIP + ":1234/" + file.getOriginalFilename();
		
		
		
	}

	
}
