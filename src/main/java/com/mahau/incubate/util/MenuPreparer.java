package com.mahau.incubate.util;

import org.apache.tiles.AttributeContext;
import org.apache.tiles.preparer.ViewPreparer;
import org.apache.tiles.request.Request;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Component;

import com.mahau.incubate.model.MemberInfo;

@Component("menuPreparer")
public class MenuPreparer implements ViewPreparer {

	@Override
	public void execute(Request tilesContext, AttributeContext attributeContext) {
		Authentication auth = SecurityContextHolder.getContext()
				.getAuthentication();

		Object principal = auth.getPrincipal();
//		String memberName = "";
		if (principal != null && principal instanceof MemberInfo) {
//			memberName = ((MemberInfo) principal).getMemberName();
		}
//		tilesContext.getParam().put("memberName", memberName);
	}

}
