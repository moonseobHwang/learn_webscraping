<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
	<form method="POST" action="<c:url value='/member/${resultMap.forword }' />">
		<input type="hidden" name="MEMBERID" value="${resultMap.MEMBERID}" />
		<br />
		<spring:message code="label.member.email" />
		: <input type="text" name="EMAIL" value="${resultMap.EMAIL}" /> <br />
		<spring:message code="label.member.membername" />
		: <input type="text" name="MEMBERNAME" value="${resultMap.MEMBERNAME}" />
		<br />
		<spring:message code="label.member.password" />
		: <input type="password" name="PASSWORD" value="${resultMap.PASSWORD}" />
		<br /> <input type="submit" value="Submit" />
	</form>
</body>
</html>