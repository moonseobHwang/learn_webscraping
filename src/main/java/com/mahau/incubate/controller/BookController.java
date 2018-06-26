/**
 * It's Designed For incubated Center
 * @author      Oh Sanghun
 * @version     %I%, %G%
 * @since       1.0
 */
package com.mahau.incubate.controller;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.mahau.incubate.model.ParamCollector;
import com.mahau.incubate.service.ShareService;

@Controller
public class BookController {

	@Resource(name = "bookService")
	private ShareService service;

	private String ROOT_VIEW = "/book/";

	// Receive Parameters from Html Using @RequestParam Map with @PathVariable
	@SuppressWarnings("unchecked")
	@RequestMapping(value = "/book/{action}", method = { RequestMethod.GET,
			RequestMethod.POST })
	public ModelAndView doRequest(ParamCollector requestMap,
			@PathVariable String action, ModelAndView modelandView) {

		List<Object> resultList = null;
		Map<Object, Object> resultMap = new HashMap<Object, Object>();
		String viewName = ROOT_VIEW + action;

		// delete
		if ("insert".equals(action)) {
			resultMap = (Map<Object, Object>) service.saveObject(viewName,
					requestMap.getMap());
			viewName = ROOT_VIEW + "read";

			// edit by pass
		} else if ("edit".equals(action)) {
			String userid = (String) requestMap.get("MEMBERID");
			if (userid == null) {
				resultMap.put("forword", "insert");
			}

			// list
		}
		modelandView.addObject("resultList", resultList);
		modelandView.addObject("resultMap", resultMap);
		modelandView.addObject("paramMap", requestMap);
		modelandView.setViewName(viewName);
		return modelandView;

	}
}