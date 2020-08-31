<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
	<spring:message code="label.member.email" /> :
	${resultMap.EMAIL}
	<br /> <spring:message code="label.member.membername" /> :
	${resultMap.MEMBERNAME}
	<br /> <spring:message code="label.member.password" /> :
	${resultMap.PASSWORD}
	<br /> 
	<a href="<c:url value='/member/list' />">
				Member List</a>
</body>
</html>