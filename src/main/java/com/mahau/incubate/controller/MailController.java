/**
 * It's Designed For incubated Center
 * @author      Oh Sanghun
 * @version     %I%, %G%
 * @since       1.0
 */
package com.mahau.incubate.controller;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import javax.annotation.Resource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import com.mahau.incubate.service.MailService;
import com.mahau.incubate.service.ShareService;

@Controller
public class MailController {

	@Resource(name = "shareService")
	private ShareService service;

	@Autowired
	private MailService mailService;

	private String ROOT_VIEW = "/mail/";

	// Receive Parameters from Html Using @RequestParam Map with @PathVariable
	@SuppressWarnings("unchecked")
	@RequestMapping(value = "/mail/{action}", method = { RequestMethod.GET,
			RequestMethod.POST })
	public ModelAndView doRequest(@RequestParam Map<Object, Object> paramMap,
			@PathVariable String action, ModelAndView modelandView) {

		List<Object> resultList = null;
		Map<Object, Object> resultMap = new HashMap<Object, Object>();
		String viewName = ROOT_VIEW + action;
		
		String resultCode = "";
		// check to send email or not
		if ("sendSingle".equals(action)) { // try to send
			resultCode = mailService.sendMail(paramMap);

		} else if ("sendMulti".equals(action)) { // try to send
			
			resultList = service.getList("/member/list", paramMap);

			// check to exist email
			// if (resultList != null && resultList.size() > 0) {

			Iterator<?> itr = resultList.iterator();

			Map<Object, Object> dataMap = null;

//			dataMap = paramMap;
			// as if up to two email
			while (itr.hasNext()) {
				dataMap = (Map<Object, Object>) itr.next();
				dataMap.put("FROMEMAIL", paramMap.get("FROMEMAIL"));
				dataMap.put("SUBJECT", paramMap.get("SUBJECT"));
				dataMap.put("MESSAGE", getMessageFromFile());

				resultCode = mailService.sendMail(dataMap);
			}

		}

		resultMap.put("resultCode", resultCode);
		
		viewName = ROOT_VIEW + "send"; 
				
		modelandView.addObject("resultList", resultList);
		modelandView.addObject("resultMap", resultMap);
		modelandView.addObject("paramMap", paramMap);
		modelandView.setViewName(viewName);
		return modelandView;
	}
	
	private String getMessageFromFile(){
		BufferedReader br = null;

		String sCurrentLine;
		StringBuffer message = new StringBuffer();

		try {

			br = new BufferedReader(new FileReader("C:\\uploads\\mail_send.html"));

			while ((sCurrentLine = br.readLine()) != null) {
				message.append(sCurrentLine);
			}

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)br.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
		
		return message.toString();
		
	}

}