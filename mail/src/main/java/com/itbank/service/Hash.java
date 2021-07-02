package com.itbank.service;

import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Hash {

	public static String getHash(String authNumber) {
		try {
			MessageDigest md = MessageDigest.getInstance("SHA-512");
			md.reset();
			md.update(authNumber.getBytes("utf-8"));
			String ret = String.format("%0128x", new BigInteger(1, md.digest()));	// 빈자리 0 으로 채워진 128 자리 16 진수형태로 포멧
			return ret;
		}catch(NoSuchAlgorithmException | UnsupportedEncodingException e) {
			System.out.println("해쉬 알고리즘이 틀렸거나 인코딩에 문제가 있습니다.");
			e.printStackTrace();
		}
		return null;
	}
	
	

}
