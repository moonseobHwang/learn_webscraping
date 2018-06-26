package com.mahau.incubate.service;

import java.util.Map;

import javax.mail.internet.MimeMessage;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.stereotype.Component;

@Component
public class MailService {
	
	@Autowired
	private JavaMailSender mailSender;

	public String sendMail(Map<?, ?> paramObject) {

		MimeMessage message = mailSender.createMimeMessage();
		
		try{
			MimeMessageHelper helper = new MimeMessageHelper(message, true);

			// set plain text message
	        helper.setFrom((String) paramObject.get("FROMEMAIL"));
	        helper.setTo((String) paramObject.get("EMAIL"));
	        helper.setSubject((String) paramObject.get("SUBJECT"));
	        helper.setText((String) paramObject.get("MESSAGE"), true);

	        mailSender.send(message);
		} catch (Exception e)  {
			return "Failure" ; 	// error send mail
		}
		
		return "Success" ;
	}

}
