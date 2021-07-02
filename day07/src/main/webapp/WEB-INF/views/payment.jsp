<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<h2>결제 페이지</h2>
<div>
	<p>
<!-- 	DB 에서 이렇게 출력 되기 때문에 대문자로 변수를 적어주어야 한다. {PAYMENT=0, SFUND=1200000, STATUS=미납, DUE=1500000} -->
		<span class="input-name">수강료</span>
		<b>${payinfo.DUE }</b>
	</p>
	<p>
		<span class="input-name">국가지원금</span>
		<b>${payinfo.SFUND }</b>
	</p>
	<p>
		<span class="input-name">결제 예정 금액</span>
		<b>${payinfo.NEED }</b>
	</p>
	<p>
		<span class="input-name">결제 하신 금액</span>
		<b>${payinfo.PAYMENT }</b>
	</p>
	<p>
		<span class="input-name">최종 상태</span>
		<strong style="color: ${payinfo.STATUS == '완료'? 'blue' : 'red'}">
		${payinfo.STATUS }
		</strong>
	</p>
	<c:if test="${payinfo.STATUS == '미납' }">
	<form method ="post">
		<input type="hidden" name="need" value="${payinfo.NEED }">
		<input type="hidden" name="idx" value="${login.idx }">
		
		<span class="input-name">결제 금액</span>
		<input type="number" name="payment" min="0" max="${payinfo.NEED - payinfo.PAYMENT}">
		<p><input type="submit" value="결제 진행"></p>
	</form>
	</c:if>
</div>





</body>
</html>