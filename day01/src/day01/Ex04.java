package day01;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Ex04 {
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		System.out.println("문자열 입력 : ");
		String text = br.readLine(); // 개행 문자 기준으로 출력
		
		System.out.println("text : " + text);
	}
}
