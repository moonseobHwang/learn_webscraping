<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
	<form method="POST" action="<c:url value='/book/insert' />"
		enctype="multipart/form-data">
		<input type="hidden" name="BOOKID" value="${resultMap.BOOKID}" /> <br />
		<spring:message code="label.book.bookname" />
		: <input type="text" name="BOOKNAME" value="${resultMap.BOOKNAME}" />
		<br />
		<spring:message code="label.book.publisher" />
		: <input type="text" name="PUBLISHER" value="${resultMap.PUBLISHER}" />
		<br />
		<spring:message code="label.book.author" />
		: <input type="text" name="AUTHOR" value="${resultMap.AUTHOR}" /> <br />
		<spring:message code="label.book.bookinformation" />
		:
		<textarea name="BOOKINFORMATION" rows="10" cols="30">${resultMap.BOOKINFORMATION}</textarea>
		<br /> <input type="file" name="file" /> <br /> <input
			type="submit" value="Submit" />
	</form>
</body>
</html>