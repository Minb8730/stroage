package test1;

public class Account {
	private String id, pw, name;


	
	public Account() {}

	public Account(String id, String pw, String name) {
		this.id = id;
		this.pw = pw;
		this.name = name;
	}
	
	@Override
	public boolean equals(Object obj) {
		Account other = (Account) obj;
		boolean idFlag = this.id.equals(other.id);
		boolean pwFlag = this.pw.equals(other.pw);
		
		return idFlag && pwFlag;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPw() {
		return pw;
	}

	public void setPw(String pw) {
		this.pw = pw;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}


}