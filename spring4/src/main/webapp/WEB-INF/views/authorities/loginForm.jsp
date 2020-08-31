<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@page session="true"%>
<html>
<head>
<title>Login Page</title>
</head>
<body onload='document.loginForm.username.focus();'>

	<h2>Log In</h2>
	<c:if test="${not empty param.fail}">
		<font color="red"> Your login attempt was not successful, try
			again.<br /> Reason:
			${sessionScope["SPRING_SECURITY_LAST_EXCEPTION"].message}<br />
		</font>
		<c:remove scope="session" var="SPRING_SECURITY_LAST_EXCEPTION" />
	</c:if>

	<div id="login-box">
		<form name='loginForm'
			action="<c:url value='/j_spring_security_check' />" method='POST'>

			<table>
				<tr>
					<td>Email:</td>
					<td><input type='text' name='email' value=''></td>
				</tr>
				<tr>
					<td>Password:</td>
					<td><input type='password' name='password' /></td>
				</tr>
				<tr>
					<td colspan='2'><input name="submit" type="submit"
						value="submit" /></td>
				</tr>
			</table>

			<input type="hidden" name="${_csrf.parameterName}"
				value="${_csrf.token}" />

		</form>
	</div>

</body>
</html>