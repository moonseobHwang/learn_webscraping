<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring"%>
<!-- %@ taglib prefix="nav" uri="/pNavi-tags"% -->

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<script type="text/javascript"
	src="<c:url value='/resources/js/jquery-1.11.3.min.js' />"></script>
<script src="<c:url value="/resources/js/jscommon.js" />"
	type="text/javascript"></script>

</head>
<script>
	$.post("<c:url value='/restfulMap' />", {
		viewName : "/common/list",
		PARENTCODE : "10001"
	}, function(data, status) {
		var str = "<select name='searchCode' id='searchCode'>";
		$.each(data, function(index, value) {
			str += '<option value="'+value.CHILDCODE+'">' + value.CODENAME
					+ '</option>';
		});
		str += '</select>';
		$("#commonCodes").html(str);
		var searchCode = "${paramMap.searchCode}";
		$("#searchCode").val(searchCode != "" ? searchCode : "EMAIL").attr(
				'selected', true);
	});
</script>

</head>
<body>
	<form action="<c:url value='/member/list' />" method="post">
		<table>
			<tr>
				<td><span id="commonCodes"></span> <input type="text"
					value="${paramMap.searchWord}" name="searchWord"> <input
					type="submit" title="search" onclick="doSubmit(this.form);">
				</td>
			</tr>
			<tr>
				<td>
					<table border=1>
						<thead>
							<tr>
								<th><spring:message code="label.member.email" /></th>
								<th><spring:message code="label.member.membername" /></th>
								<th><spring:message code="label.member.password" /></th>
								<th colspan=2>Function</th>
							</tr>
						</thead>
						<tbody>
							<c:forEach items="${resultList}" var="resultData">
								<tr>
									<td><a
										href="<c:url value='/member/read?MEMBERID=${resultData.MEMBERID}' />">${resultData.EMAIL}</a></td>
									<td>${resultData.MEMBERNAME}</td>
									<td>${resultData.PASSWORD}</td>
									<td><a
										href="<c:url value='/member/edit?MEMBERID=${resultData.MEMBERID}' />">Update</a></td>
									<td><a
										href="<c:url value='/member/delete?MEMBERID=${resultData.MEMBERID}' />">Delete</a></td>
								</tr>
							</c:forEach>
						</tbody>
					</table>
				</td>
			</tr>
			<tr>
				<td>
					<!-- paging : start >
					<div class="pageNum">
						<nav:pageNavi
							doSubmit="doSubmit(<c:url value='/member/list' />, this.from, 'get');"
							pageList="${resultList}" />
					</div> <!-- paging : end -->
				</td>
			</tr>
			<tr>
				<td>
					<p>
						<a href="<c:url value='/member/edit' />">Add Member</a>
					</p>
				</td>
			</tr>


		</table>
	</form>
</body>
</html>