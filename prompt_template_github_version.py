# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 09:18:35 2025

@author: ggoldenits
"""

def build_html_prompt_v4(html_text, original_character_count):
    prompt = (
        "You are a cybersecurity expert analyzing websites for phishing attempts. Your task is to examine the provided HTML code and determine if the website is likely a phishing site.\n\n"

        "**Important:** The HTML may be truncated to reduce costs, so CSS styles and JavaScript code may be missing. Focus on HTML structure, text content, and URLs.\n\n"
        f"HTML:'{html_text}'\n"
        f"Original HTML character count: {original_character_count}\n"
        "**Look for these phishing indicators (focus on HTML structure and content):**\n\n"

        "1. **Suspicious URLs/domains** - Check href attributes, form actions, image sources for:\n"
           "- Misspelled brand names, unusual domains, suspicious subdomains\n"
           "- IP addresses instead of domains, excessive hyphens, unusual TLDs\n"
        "2. **Form analysis** - Login/input forms with:\n"
           "- Action URLs pointing to wrong domains\n"
           "- Password/sensitive data collection for mismatched brands\n"
           "- Excessive personal information requests (SSN, full address, etc.)\n"
        "3. **Content and language** - Text containing:\n"
           "- Urgent threats: 'Account suspended', 'Verify immediately', 'Limited time'\n"
           "- Fear tactics: 'Security breach', 'Unauthorized access detected'\n"
           "- Reward baits: 'You have won', 'Free gift', 'Exclusive offer'\n"
        "4. **HTML structure issues**:\n"
           "- Spelling/grammar errors in text content\n"
           "- Inconsistent or poor HTML structure\n"
           "- Missing or suspicious meta tags (title, description)\n"
        "5. **Link analysis** - Check all href attributes for:\n"
           "- Links to different domains than expected\n"
           "- Shortened URLs (bit.ly, tinyurl, etc.)\n"
           "- Misleading anchor text vs actual URL\n"
        "6. **Brand impersonation** - Look for:\n"
           "- Company names in text that don't match domain\n"
           "- References to legitimate services (PayPal, Amazon, banks, ...) on wrong domains\n"
           "- Official-sounding but incorrect terminology\n"
        "7. **Missing legitimacy markers**:\n"
           "- No contact information or privacy policy links\n"
           "- Missing proper company details in footer\n"
           "- No legitimate copyright notices\n\n"
        
        "**Note:** Since CSS/JS may be truncated, focus on HTML tags, text content, and URL analysis rather than visual styling or dynamic behavior.\n"
        "**Scoring guide:**\n"
        "- 0-2: Very unlikely phishing (legitimate site)\n"
        "- 3-4: Low risk (minor suspicious elements)\n"
        "- 5-6: Medium risk (several concerning indicators)\n"
        "- 7-8: High risk (multiple clear phishing signs)\n"
        "- 9-10: Very high risk (obvious phishing attempt)\n\n"
        
        "**Required output format (JSON only):**\n"
        "{\n"
          '"phishing_score": int [0-10],\n'
          '"is_phishing": boolean [true/false],\n'
          '"reasoning": string [Brief explanation of your decision based on specific indicators found]\n'
        "}\n\n"
        
        "**Output Constraints:**\n"
        "Do only output the JSON formated output and nothing else.\n"
        
        
    )
    return prompt