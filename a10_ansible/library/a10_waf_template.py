#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = """
module: a10_waf_template
description:
    - Manage WAF template configuration
short_description: Configures A10 waf.template
author: A10 Networks 2018 
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
        - present
        - absent
        required: True
    a10_host:
        description:
        - Host for AXAPI authentication
        required: True
    a10_username:
        description:
        - Username for AXAPI authentication
        required: True
    a10_password:
        description:
        - Password for AXAPI authentication
        required: True
    a10_port:
        description:
        - Port for AXAPI authentication
        required: True
    a10_protocol:
        description:
        - Protocol for AXAPI authentication
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        required: False
    log_succ_reqs:
        description:
        - "Log successful waf requests"
        required: False
    brute_force_resp_headers_file:
        description:
        - "Name of WAF policy list file"
        required: False
    keep_end:
        description:
        - "Number of unmasked characters at the end (default= 0)"
        required: False
    max_cookie_len:
        description:
        - "Max Cookie length allowed in request (default 4096) (Maximum length of cookie allowed (default 4096))"
        required: False
    deploy_mode:
        description:
        - "'active'= Deploy WAF in active (blocking) mode; 'passive'= Deploy WAF in passive (log-only) mode; 'learning'= Deploy WAF in learning mode; "
        required: False
    xml_format_check:
        description:
        - "Check HTTP body for XML format compliance"
        required: False
    brute_force_resp_string:
        description:
        - "Trigger brute-force check on HTTP response line"
        required: False
    max_string:
        description:
        - "Maximum length of a string in a JSON request body (default 64) (Maximum length of a JSON string (default 64))"
        required: False
    ccn_mask:
        description:
        - "Mask credit card numbers in response"
        required: False
    waf_blist_file:
        description:
        - "Name of WAF policy list file"
        required: False
    challenge_action_cookie:
        description:
        - "Use Set-Cookie to determine if client allows cookies"
        required: False
    uuid:
        description:
        - "uuid of the object"
        required: False
    form_set_no_cache:
        description:
        - "Disable caching of form-containing responses"
        required: False
    http_redirect:
        description:
        - "Send HTTP redirect response (302 Found) to specifed URL (URL to redirect to when denying request)"
        required: False
    bot_check:
        description:
        - "Check User-Agent for known bots"
        required: False
    max_cookies_len:
        description:
        - "Max Total Cookies length allowed in request (default 4096) (Maximum total length of cookies allowed (default 4096))"
        required: False
    brute_force_global:
        description:
        - "Brute-force triggers apply globally instead of per-client (Apply brute-force triggers globally)"
        required: False
    url_check:
        description:
        - "Check URL against list of previously learned URLs"
        required: False
    max_parameter_value_len:
        description:
        - "Max HTML parameter value length in an HTTP request (default 4096) (Maximum HTML parameter value in an HTTP request (default 4096))"
        required: False
    max_entities:
        description:
        - "Maximum number of MIME entities allowed in request (default 10)"
        required: False
    hide_resp_codes:
        description:
        - "Hides response codes that are not allowed (default 4xx, 5xx)"
        required: False
    max_depth:
        description:
        - "Maximum recursion depth in a value in a JSON requesnt body (default 16) (Maximum recursion depth in a JSON value (default 16))"
        required: False
    hide_resp_codes_file:
        description:
        - "Name of WAF policy list file"
        required: False
    brute_force_resp_codes_file:
        description:
        - "Name of WAF policy list file"
        required: False
    max_elem_name_len:
        description:
        - "Maximum length for an element name (default 128)"
        required: False
    deny_password_autocomplete:
        description:
        - "Check to protect against server-generated form which contain password fields that allow autocomplete"
        required: False
    name:
        description:
        - "WAF Template Name"
        required: True
    http_resp_200:
        description:
        - "Send HTTP response with status code 200 OK"
        required: False
    user_tag:
        description:
        - "Customized tag"
        required: False
    keep_start:
        description:
        - "Number of unmasked characters at the beginning (default= 0)"
        required: False
    max_hdrs:
        description:
        - "Maximum number of headers allowed in request (default 20)"
        required: False
    max_cookie_value_len:
        description:
        - "Max Cookie Value length allowed in request (default 4096) (Maximum length of cookie value allowed (default 4096))"
        required: False
    max_cdata_len:
        description:
        - "Maximum length of an CDATA section of an element (default 65535)"
        required: False
    max_hdr_value_len:
        description:
        - "Max header value length allowed in request (default 4096) (Maximum length of header value allowed (default 4096))"
        required: False
    secret_encrypted:
        description:
        - "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)"
        required: False
    cookie_name:
        description:
        - "Cookie name (simple string or PCRE pattern)"
        required: False
    max_namespace_uri_len:
        description:
        - "Maximum length of a namespace URI (default 256)"
        required: False
    resp_url_403:
        description:
        - "Response content to send client when denying request"
        required: False
    csrf_check:
        description:
        - "Tag the form to protect against Cross-site Request Forgery"
        required: False
    referer_domain_list:
        description:
        - "List of referer domains allowed"
        required: False
    max_parameters:
        description:
        - "Maximum number of HTML parameters allowed in request (default 64)"
        required: False
    brute_force_lockout_period:
        description:
        - "Number of seconds client should be locked out (default 600)"
        required: False
    stats:
        description:
        - "Field stats"
        required: False
        suboptions:
            redirect_wlist_fail:
                description:
                - "Redirect Whitelist Failure"
            cookie_encrypt_limit_exceeded:
                description:
                - "Cookie Encrypt Limit Exceeded"
            wsdl_succ:
                description:
                - "WSDL Success"
            sqlia_chk_url_succ:
                description:
                - "SQLIA Check URL Success"
            bot_check_succ:
                description:
                - "Botnet Check Success"
            cookie_encrypt_skip_rcache:
                description:
                - "Cookie Encrypt Skip RCache"
            redirect_wlist_learn:
                description:
                - "Redirect Whitelist Learn"
            xml_limit_elem_child:
                description:
                - "XML Limit Element Child"
            buf_ovf_parameter_value_len_fail:
                description:
                - "Buffer Overflow - HTML Parameter Value Length Failure"
            ccn_mask_visa:
                description:
                - "Credit Card Number Mask Visa"
            xss_chk_cookie_succ:
                description:
                - "XSS Check Cookie Success"
            buf_ovf_cookies_len_fail:
                description:
                - "Buffer Overflow - Cookies Length Failure"
            req_denied:
                description:
                - "Requests Denied"
            json_check_failure:
                description:
                - "JSON Check Failure"
            xss_chk_post_reject:
                description:
                - "XSS Check Post Rejected"
            http_check_succ:
                description:
                - "Http Check Success"
            form_consistency_succ:
                description:
                - "Form Consistency Success"
            xml_limit_cdata_len:
                description:
                - "XML Limit CData Length"
            xml_check_failure:
                description:
                - "XML Check Failure"
            buf_ovf_hdrs_len_fail:
                description:
                - "Buffer Overflow - Headers length Failure"
            referer_check_succ:
                description:
                - "Referer Check Success"
            sqlia_chk_post_succ:
                description:
                - "SQLIA Check Post Success"
            xss_chk_url_sanitize:
                description:
                - "XSS Check URL Sanitized"
            cookie_encrypt_succ:
                description:
                - "Cookie Encrypt Success"
            buf_ovf_parameter_total_len_fail:
                description:
                - "Buffer Overflow - HTML Parameter Total Length Failure"
            soap_check_succ:
                description:
                - "Soap Check Success"
            name:
                description:
                - "WAF Template Name"
            max_cookies_fail:
                description:
                - "Max Cookies Failure"
            json_limit_array_value_count:
                description:
                - "JSON Limit Array Value Count"
            uri_wlist_succ:
                description:
                - "URI White List Success"
            brute_force_success:
                description:
                - "Brute-force checks passed"
            resp_code_hidden:
                description:
                - "Response Code Hidden"
            xml_sqlia_chk_fail:
                description:
                - "XML Sqlia Check Failure"
            xss_chk_post_succ:
                description:
                - "XSS Check Post Success"
            pcre_mask:
                description:
                - "PCRE Mask"
            form_consistency_fail:
                description:
                - "Form Consistency Failure"
            http_check_fail:
                description:
                - "Http Check Failure"
            url_check_succ:
                description:
                - "URL Check Success"
            sqlia_chk_url_reject:
                description:
                - "SQLIA Check URL Rejected"
            sqlia_chk_url_sanitize:
                description:
                - "SQLIA Check URL Sanitized"
            xss_chk_cookie_reject:
                description:
                - "XSS Check Cookie Rejected"
            json_check_succ:
                description:
                - "JSON Check Success"
            max_entities_fail:
                description:
                - "Max Entities Failure"
            http_method_check_fail:
                description:
                - "Http Method Check Failure"
            form_non_ssl_reject:
                description:
                - "Form Non SSL Rejected"
            xss_chk_post_sanitize:
                description:
                - "XSS Check Post Sanitized"
            form_set_no_cache:
                description:
                - "Form Set No Cache"
            xml_schema_succ:
                description:
                - "XML Schema Success"
            xml_limit_attr:
                description:
                - "XML Limit Attribue"
            xml_check_succ:
                description:
                - "XML Check Success"
            sess_check_none:
                description:
                - "Session Check None"
            xml_limit_namespace:
                description:
                - "XML Limit Namespace"
            wsdl_fail:
                description:
                - "WSDL Failure"
            post_form_check_succ:
                description:
                - "Post Form Check Success"
            buf_ovf_query_len_fail:
                description:
                - "Buffer Overflow - Query Length Failure"
            sqlia_chk_post_reject:
                description:
                - "SQLIA Check Post Rejected"
            form_password_autocomplete:
                description:
                - "Form Password Autocomplete"
            permitted:
                description:
                - "Honor threshold  count"
            xml_xss_chk_fail:
                description:
                - "XML XSS Check Failure"
            buf_ovf_url_len_fail:
                description:
                - "Buffer Overflow - URL Length Failure"
            buf_ovf_cookie_len_fail:
                description:
                - "Buffer Overflow - Cookie Length Failure"
            form_csrf_tag_succ:
                description:
                - "Form CSRF tag Success"
            xss_chk_cookie_sanitize:
                description:
                - "XSS Check Cookie Sanitized"
            sessions_alloc:
                description:
                - "Sessions allocated"
            xml_limit_entity_exp:
                description:
                - "XML Limit Entity Exp"
            ccn_mask_diners:
                description:
                - "Credit Card Number Mask Diners"
            sess_check_succ:
                description:
                - "Session Check Success"
            json_limit_depth:
                description:
                - "JSON Limit Depth"
            buf_ovf_cookie_name_len_fail:
                description:
                - "Buffer Overflow - Cookie Name Length Failure"
            learn_updates:
                description:
                - "Learning Updates"
            redirect_wlist_succ:
                description:
                - "Redirect Whitelist Success"
            challenge_javascript_sent:
                description:
                - "JavaScript challenge sent"
            req_allowed:
                description:
                - "Requests Allowed"
            json_limit_object_member_count:
                description:
                - "JSON Limit Object Number Count"
            bot_check_fail:
                description:
                - "Botnet Check Failure"
            uri_wlist_fail:
                description:
                - "URI White List Failure"
            uri_blist_fail:
                description:
                - "URI Black List Failure"
            referer_check_redirect:
                description:
                - "Referer Check Redirect"
            challenge_cookie_sent:
                description:
                - "Cookie challenge sent"
            sqlia_chk_post_sanitize:
                description:
                - "SQLIA Check Post Sanitized"
            ccn_mask_amex:
                description:
                - "Credit Card Number Mask Amex"
            num_drops:
                description:
                - "Number Drops"
            referer_check_fail:
                description:
                - "Referer Check Failure"
            post_form_check_sanitize:
                description:
                - "Post Form Check Sanitized"
            cookie_decrypt_succ:
                description:
                - "Cookie Decrypt Success"
            xss_chk_url_reject:
                description:
                - "XSS Check URL Rejected"
            max_parameters_fail:
                description:
                - "Max Parameters Failure"
            url_check_fail:
                description:
                - "URL Check Failure"
            xml_schema_fail:
                description:
                - "XML Schema Failure"
            form_non_post_reject:
                description:
                - "Form Non Post Rejected"
            num_resets:
                description:
                - "Number Resets"
            xml_limit_entity_exp_depth:
                description:
                - "XML Limit Entity Exp Depth"
            form_non_masked_password:
                description:
                - "Form Non Masked Password"
            buf_ovf_line_len_fail:
                description:
                - "Buffer Overflow - Line Length Failure"
            ccn_mask_discover:
                description:
                - "Credit Card Number Mask Discover"
            ssn_mask:
                description:
                - "Social Security Number Mask"
            json_limit_string:
                description:
                - "JSON Limit String"
            resp_hdrs_filtered:
                description:
                - "Response Headers Filtered"
            called:
                description:
                - "Threshold check count"
            ccn_mask_mastercard:
                description:
                - "Credit Card Number Mask Mastercard"
            xml_sqlia_chk_succ:
                description:
                - "XML Sqlia Check Success"
            brute_force_fail:
                description:
                - "Brute-force checks failed"
            max_hdrs_fail:
                description:
                - "Max Headers Failure"
            xml_limit_attr_name_len:
                description:
                - "XML Limit Name Length"
            form_non_ssl_password:
                description:
                - "Form Non SSL Password"
            too_many_sessions:
                description:
                - "Too many sessions consumed"
            buf_ovf_hdr_value_len_fail:
                description:
                - "Buffer Overflow - Header Value Length Failure"
            uri_blist_succ:
                description:
                - "URI Black List Success"
            sess_check_fail:
                description:
                - "Session Check Failure"
            buf_ovf_hdr_name_len_fail:
                description:
                - "Buffer Overflow - Header Name Length Failure"
            resp_denied:
                description:
                - "Responses Denied"
            sessions_freed:
                description:
                - "Sessions freed"
            out_of_sessions:
                description:
                - "Out of sessions"
            xml_limit_elem:
                description:
                - "XML Limit Element"
            buf_ovf_parameter_name_len_fail:
                description:
                - "Buffer Overflow - HTML Parameter Name Length Failure"
            xml_limit_attr_value_len:
                description:
                - "XML Limit Value Length"
            xml_limit_elem_depth:
                description:
                - "XML Limit Element Depth"
            ccn_mask_jcb:
                description:
                - "Credit Card Number Mask Jcb"
            cookie_decrypt_fail:
                description:
                - "Cookie Decrypt Failure"
            buf_ovf_cookie_value_len_fail:
                description:
                - "Buffer Overflow - Cookie Value Length Failure"
            buf_ovf_post_size_fail:
                description:
                - "Buffer Overflow - Post size Failure"
            total_req:
                description:
                - "Total Requests"
            xml_limit_elem_name_len:
                description:
                - "XML Limit Element Name Length"
            url_check_learn:
                description:
                - "URL Check Learn"
            http_method_check_succ:
                description:
                - "Http Method Check Success"
            xss_chk_url_succ:
                description:
                - "XSS Check URL Success"
            xml_limit_namespace_uri_len:
                description:
                - "XML Limit Namespace URI Length"
            post_form_check_reject:
                description:
                - "Post Form Check Rejected"
            cookie_encrypt_fail:
                description:
                - "Cookie Encrypt Failure"
            soap_check_failure:
                description:
                - "Soap Check Failure"
            challenge_captcha_sent:
                description:
                - "Captcha challenge sent"
            form_csrf_tag_fail:
                description:
                - "Form CSRF tag Failure"
            xml_xss_chk_succ:
                description:
                - "XML XSS Check Success"
            buf_ovf_max_data_parse_fail:
                description:
                - "Buffer Overflow - Max Data Parse Failure"
    max_parameter_name_len:
        description:
        - "Max HTML parameter name length in an HTTP request (default 256) (Maximum HTML parameter name length in an HTTP request (default 256))"
        required: False
    deny_non_masked_passwords:
        description:
        - "Denies forms that have a password field with a textual type, resulting in this field not being masked"
        required: False
    challenge_action_javascript:
        description:
        - "Add JavaScript to response to test if client allows JavaScript"
        required: False
    max_hdr_name_len:
        description:
        - "Max header name length allowed in request (default 63) (Maximum length of header name allowed (default 63))"
        required: False
    max_elem_depth:
        description:
        - "Maximum recursion level for element definition (default 256)"
        required: False
    form_consistency_check:
        description:
        - "Form input consistency check"
        required: False
    redirect_wlist:
        description:
        - "Check Redirect URL against list of previously learned redirects"
        required: False
    xml_xss_check:
        description:
        - "Check XML data against XSS policy"
        required: False
    referer_check:
        description:
        - "Check referer to protect against CSRF attacks"
        required: False
    wsdl_resp_val_file:
        description:
        - "Specify name of WSDL file for verifying XML body contents"
        required: False
    brute_force_check:
        description:
        - "Enable brute-force attack mitigation"
        required: False
    brute_force_test_period:
        description:
        - "Number of seconds for brute-force event counting (default 60)"
        required: False
    max_namespace:
        description:
        - "Maximum number of namespace declarations (default 16)"
        required: False
    max_entity_exp:
        description:
        - "Maximum number of entity expansions (default 1024)"
        required: False
    form_deny_non_post:
        description:
        - "Deny request with forms if the method is not POST"
        required: False
    cookie_encryption_secret:
        description:
        - "Cookie encryption secret"
        required: False
    decode_escaped_chars:
        description:
        - "Decode escaped characters such as r n ' xXX u00YY in internal url"
        required: False
    json_format_check:
        description:
        - "Check HTTP body for JSON format compliance"
        required: False
    bot_check_policy_file:
        description:
        - "Name of WAF policy list file"
        required: False
    xml_schema_resp_val_file:
        description:
        - "Specify name of XML-Schema file for verifying XML body contents"
        required: False
    brute_force_challenge_limit:
        description:
        - "Maximum brute-force events before sending challenge (default 2) (Maximum brute-force events before locking out client (default 2))"
        required: False
    allowed_http_methods:
        description:
        - "List of allowed HTTP methods. Default is 'GET POST'. (List of HTTP methods allowed (default 'GET POST'))"
        required: False
    brute_force_resp_codes:
        description:
        - "Trigger brute-force check on HTTP response code"
        required: False
    remove_selfref:
        description:
        - "Remove self-references such as /./ and /path/../ from internal url"
        required: False
    max_elem_child:
        description:
        - "Maximum number of children of an XML element (default 1024)"
        required: False
    max_entity_exp_depth:
        description:
        - "Maximum nested depth of entity expansion (default 32)"
        required: False
    max_array_value_count:
        description:
        - "Maximum number of values in an array in a JSON request body (default 256) (Maximum number of values in a JSON array (default 256))"
        required: False
    max_elem:
        description:
        - "Maximum number of XML elements (default 1024)"
        required: False
    sqlia_check:
        description:
        - "'reject'= Reject requests with SQLIA patterns; 'sanitize'= Remove bad SQL from request; "
        required: False
    max_object_member_count:
        description:
        - "Maximum number of members in an object in a JSON request body (default 256) (Maximum number of members in a JSON object (default 256))"
        required: False
    http_resp_403:
        description:
        - "Send HTTP response with status code 403 Forbidden (default)"
        required: False
    http_check:
        description:
        - "Check request for HTTP protocol compliance"
        required: False
    brute_force_resp_headers:
        description:
        - "Trigger brute-force check on HTTP response header names"
        required: False
    max_cookie_name_len:
        description:
        - "Max Cookie Name length allowed in request (default 64) ( Maximum length of cookie name allowed (default 64))"
        required: False
    remove_comments:
        description:
        - "Remove comments from internal url"
        required: False
    logging:
        description:
        - "Logging template (Logging Config name)"
        required: False
    uri_wlist_check:
        description:
        - "specify name of WAF policy list file to whitelist"
        required: False
    brute_force_resp_string_file:
        description:
        - "Name of WAF policy list file"
        required: False
    form_deny_non_ssl:
        description:
        - "Deny request with forms if the protocol is not SSL"
        required: False
    xss_check:
        description:
        - "'reject'= Reject requests with bad cookies; 'sanitize'= Remove bad cookies from request; "
        required: False
    reset_conn:
        description:
        - "Reset the client connection"
        required: False
    referer_safe_url:
        description:
        - " Safe URL to redirect to if referer is missing"
        required: False
    remove_spaces:
        description:
        - "Remove spaces from internal url"
        required: False
    brute_force_lockout_limit:
        description:
        - "Maximum brute-force events before locking out client (default 5)"
        required: False
    uri_blist_check:
        description:
        - "specify name of WAF policy list file to blacklist"
        required: False
    max_url_len:
        description:
        - "Max URL length allowed in request (default 1024) (Maximum length of URL allowed (default 1024))"
        required: False
    max_hdrs_len:
        description:
        - "Max headers length allowed in request (default 4096) (Maximum length of headers allowed (default 4096))"
        required: False
    waf_wlist_file:
        description:
        - "Name of WAF policy list file"
        required: False
    max_attr_name_len:
        description:
        - "Maximum length of an attribute name (default 128)"
        required: False
    lifetime:
        description:
        - "Session lifetime in minutes (default 10)"
        required: False
    max_attr:
        description:
        - "Maximum number of attributes of an XML element (default 256)"
        required: False
    xss_check_policy_file:
        description:
        - "Name of WAF policy list file"
        required: False
    resp_url_200:
        description:
        - "Response content to send client when denying request"
        required: False
    max_post_size:
        description:
        - "Max content length allowed in POST request (default 20480) (Maximum size allowed content in an HTTP POST request (default 20480))"
        required: False
    decode_hex_chars:
        description:
        - "Decode hex chars such as %xx and %u00yy in internal url"
        required: False
    max_line_len:
        description:
        - "Max Line length allowed in request (default 1024) (Maximum length of Request line allowed (default 1024))"
        required: False
    max_query_len:
        description:
        - "Max Query length allowed in request (default 1024) (Maximum length of Request query allowed (default 1024))"
        required: False
    sqlia_check_policy_file:
        description:
        - "Name of WAF policy list file"
        required: False
    deny_non_ssl_passwords:
        description:
        - "Denies any form that has a password field if the form is not sent over an SSL connection"
        required: False
    max_data_parse:
        description:
        - "Max data parsed for Web Application Firewall (default 65536) (Maximum data parsed for Web Application Firewall (default 65536))"
        required: False
    max_parameter_total_len:
        description:
        - "Max HTML parameter total length in an HTTP request (default 4096) (Maximum HTML parameter total length in an HTTP request (default 4096))"
        required: False
    wsdl_file:
        description:
        - "Specify name of WSDL file for verifying XML body contents"
        required: False
    session_check:
        description:
        - "Enable session checking via session cookie"
        required: False
    disable:
        description:
        - "Disable buffer overflow protection"
        required: False
    filter_resp_hdrs:
        description:
        - "Removes web server's identifying headers"
        required: False
    max_cookies:
        description:
        - "Maximum number of cookies allowed in request (default 20)"
        required: False
    decode_entities:
        description:
        - "Decode entities in internal url"
        required: False
    mask:
        description:
        - "Character to mask the matched pattern (default= X)"
        required: False
    referer_domain_list_only:
        description:
        - "List of referer domains allowed"
        required: False
    max_attr_value_len:
        description:
        - "Maximum length of an attribute text value (default 128)"
        required: False
    pcre_mask:
        description:
        - "Mask matched PCRE pattern in response"
        required: False
    soap_format_check:
        description:
        - "Check XML document for SOAP format compliance"
        required: False
    xml_schema_file:
        description:
        - "Specify name of XML-Schema file for verifying XML body contents"
        required: False
    ssn_mask:
        description:
        - "Mask US Social Security numbers in response"
        required: False
    xml_sqlia_check:
        description:
        - "Check XML data against SQLIA policy"
        required: False


"""

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["allowed_http_methods","bot_check","bot_check_policy_file","brute_force_challenge_limit","brute_force_check","brute_force_global","brute_force_lockout_limit","brute_force_lockout_period","brute_force_resp_codes","brute_force_resp_codes_file","brute_force_resp_headers","brute_force_resp_headers_file","brute_force_resp_string","brute_force_resp_string_file","brute_force_test_period","ccn_mask","challenge_action_cookie","challenge_action_javascript","cookie_encryption_secret","cookie_name","csrf_check","decode_entities","decode_escaped_chars","decode_hex_chars","deny_non_masked_passwords","deny_non_ssl_passwords","deny_password_autocomplete","deploy_mode","disable","filter_resp_hdrs","form_consistency_check","form_deny_non_post","form_deny_non_ssl","form_set_no_cache","hide_resp_codes","hide_resp_codes_file","http_check","http_redirect","http_resp_200","http_resp_403","json_format_check","keep_end","keep_start","lifetime","log_succ_reqs","logging","mask","max_array_value_count","max_attr","max_attr_name_len","max_attr_value_len","max_cdata_len","max_cookie_len","max_cookie_name_len","max_cookie_value_len","max_cookies","max_cookies_len","max_data_parse","max_depth","max_elem","max_elem_child","max_elem_depth","max_elem_name_len","max_entities","max_entity_exp","max_entity_exp_depth","max_hdr_name_len","max_hdr_value_len","max_hdrs","max_hdrs_len","max_line_len","max_namespace","max_namespace_uri_len","max_object_member_count","max_parameter_name_len","max_parameter_total_len","max_parameter_value_len","max_parameters","max_post_size","max_query_len","max_string","max_url_len","name","pcre_mask","redirect_wlist","referer_check","referer_domain_list","referer_domain_list_only","referer_safe_url","remove_comments","remove_selfref","remove_spaces","reset_conn","resp_url_200","resp_url_403","secret_encrypted","session_check","soap_format_check","sqlia_check","sqlia_check_policy_file","ssn_mask","stats","uri_blist_check","uri_wlist_check","url_check","user_tag","uuid","waf_blist_file","waf_wlist_file","wsdl_file","wsdl_resp_val_file","xml_format_check","xml_schema_file","xml_schema_resp_val_file","xml_sqlia_check","xml_xss_check","xss_check","xss_check_policy_file",]

# our imports go at the top so we fail fast.
try:
    from a10_ansible import errors as a10_ex
    from a10_ansible.axapi_http import client_factory, session_factory
    from a10_ansible.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

except (ImportError) as ex:
    module.fail_json(msg="Import Error:{0}".format(ex))
except (Exception) as ex:
    module.fail_json(msg="General Exception in Ansible module import:{0}".format(ex))


def get_default_argspec():
    return dict(
        a10_host=dict(type='str', required=True),
        a10_username=dict(type='str', required=True),
        a10_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=["present", "absent", "noop"]),
        a10_port=dict(type='int', required=True),
        a10_protocol=dict(type='str', choices=["http", "https"]),
        a10_partition=dict(type='dict', name=dict(type='str',), shared=dict(type='str',), required=False, ),
        a10_device_context_id=dict(type='int', choices=[1, 2, 3, 4, 5, 6, 7, 8], required=False, ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )

def get_argspec():
    rv = get_default_argspec()
    rv.update(dict(
        log_succ_reqs=dict(type='bool',),
        brute_force_resp_headers_file=dict(type='str',),
        keep_end=dict(type='int',),
        max_cookie_len=dict(type='int',),
        deploy_mode=dict(type='str',choices=['active','passive','learning']),
        xml_format_check=dict(type='bool',),
        brute_force_resp_string=dict(type='bool',),
        max_string=dict(type='int',),
        ccn_mask=dict(type='bool',),
        waf_blist_file=dict(type='str',),
        challenge_action_cookie=dict(type='bool',),
        uuid=dict(type='str',),
        form_set_no_cache=dict(type='bool',),
        http_redirect=dict(type='str',),
        bot_check=dict(type='bool',),
        max_cookies_len=dict(type='int',),
        brute_force_global=dict(type='bool',),
        url_check=dict(type='bool',),
        max_parameter_value_len=dict(type='int',),
        max_entities=dict(type='int',),
        hide_resp_codes=dict(type='bool',),
        max_depth=dict(type='int',),
        hide_resp_codes_file=dict(type='str',),
        brute_force_resp_codes_file=dict(type='str',),
        max_elem_name_len=dict(type='int',),
        deny_password_autocomplete=dict(type='bool',),
        name=dict(type='str',required=True,),
        http_resp_200=dict(type='bool',),
        user_tag=dict(type='str',),
        keep_start=dict(type='int',),
        max_hdrs=dict(type='int',),
        max_cookie_value_len=dict(type='int',),
        max_cdata_len=dict(type='int',),
        max_hdr_value_len=dict(type='int',),
        secret_encrypted=dict(type='str',),
        cookie_name=dict(type='str',),
        max_namespace_uri_len=dict(type='int',),
        resp_url_403=dict(type='str',),
        csrf_check=dict(type='bool',),
        referer_domain_list=dict(type='str',),
        max_parameters=dict(type='int',),
        brute_force_lockout_period=dict(type='int',),
        stats=dict(type='dict',redirect_wlist_fail=dict(type='str',),cookie_encrypt_limit_exceeded=dict(type='str',),wsdl_succ=dict(type='str',),sqlia_chk_url_succ=dict(type='str',),bot_check_succ=dict(type='str',),cookie_encrypt_skip_rcache=dict(type='str',),redirect_wlist_learn=dict(type='str',),xml_limit_elem_child=dict(type='str',),buf_ovf_parameter_value_len_fail=dict(type='str',),ccn_mask_visa=dict(type='str',),xss_chk_cookie_succ=dict(type='str',),buf_ovf_cookies_len_fail=dict(type='str',),req_denied=dict(type='str',),json_check_failure=dict(type='str',),xss_chk_post_reject=dict(type='str',),http_check_succ=dict(type='str',),form_consistency_succ=dict(type='str',),xml_limit_cdata_len=dict(type='str',),xml_check_failure=dict(type='str',),buf_ovf_hdrs_len_fail=dict(type='str',),referer_check_succ=dict(type='str',),sqlia_chk_post_succ=dict(type='str',),xss_chk_url_sanitize=dict(type='str',),cookie_encrypt_succ=dict(type='str',),buf_ovf_parameter_total_len_fail=dict(type='str',),soap_check_succ=dict(type='str',),name=dict(type='str',required=True,),max_cookies_fail=dict(type='str',),json_limit_array_value_count=dict(type='str',),uri_wlist_succ=dict(type='str',),brute_force_success=dict(type='str',),resp_code_hidden=dict(type='str',),xml_sqlia_chk_fail=dict(type='str',),xss_chk_post_succ=dict(type='str',),pcre_mask=dict(type='str',),form_consistency_fail=dict(type='str',),http_check_fail=dict(type='str',),url_check_succ=dict(type='str',),sqlia_chk_url_reject=dict(type='str',),sqlia_chk_url_sanitize=dict(type='str',),xss_chk_cookie_reject=dict(type='str',),json_check_succ=dict(type='str',),max_entities_fail=dict(type='str',),http_method_check_fail=dict(type='str',),form_non_ssl_reject=dict(type='str',),xss_chk_post_sanitize=dict(type='str',),form_set_no_cache=dict(type='str',),xml_schema_succ=dict(type='str',),xml_limit_attr=dict(type='str',),xml_check_succ=dict(type='str',),sess_check_none=dict(type='str',),xml_limit_namespace=dict(type='str',),wsdl_fail=dict(type='str',),post_form_check_succ=dict(type='str',),buf_ovf_query_len_fail=dict(type='str',),sqlia_chk_post_reject=dict(type='str',),form_password_autocomplete=dict(type='str',),permitted=dict(type='str',),xml_xss_chk_fail=dict(type='str',),buf_ovf_url_len_fail=dict(type='str',),buf_ovf_cookie_len_fail=dict(type='str',),form_csrf_tag_succ=dict(type='str',),xss_chk_cookie_sanitize=dict(type='str',),sessions_alloc=dict(type='str',),xml_limit_entity_exp=dict(type='str',),ccn_mask_diners=dict(type='str',),sess_check_succ=dict(type='str',),json_limit_depth=dict(type='str',),buf_ovf_cookie_name_len_fail=dict(type='str',),learn_updates=dict(type='str',),redirect_wlist_succ=dict(type='str',),challenge_javascript_sent=dict(type='str',),req_allowed=dict(type='str',),json_limit_object_member_count=dict(type='str',),bot_check_fail=dict(type='str',),uri_wlist_fail=dict(type='str',),uri_blist_fail=dict(type='str',),referer_check_redirect=dict(type='str',),challenge_cookie_sent=dict(type='str',),sqlia_chk_post_sanitize=dict(type='str',),ccn_mask_amex=dict(type='str',),num_drops=dict(type='str',),referer_check_fail=dict(type='str',),post_form_check_sanitize=dict(type='str',),cookie_decrypt_succ=dict(type='str',),xss_chk_url_reject=dict(type='str',),max_parameters_fail=dict(type='str',),url_check_fail=dict(type='str',),xml_schema_fail=dict(type='str',),form_non_post_reject=dict(type='str',),num_resets=dict(type='str',),xml_limit_entity_exp_depth=dict(type='str',),form_non_masked_password=dict(type='str',),buf_ovf_line_len_fail=dict(type='str',),ccn_mask_discover=dict(type='str',),ssn_mask=dict(type='str',),json_limit_string=dict(type='str',),resp_hdrs_filtered=dict(type='str',),called=dict(type='str',),ccn_mask_mastercard=dict(type='str',),xml_sqlia_chk_succ=dict(type='str',),brute_force_fail=dict(type='str',),max_hdrs_fail=dict(type='str',),xml_limit_attr_name_len=dict(type='str',),form_non_ssl_password=dict(type='str',),too_many_sessions=dict(type='str',),buf_ovf_hdr_value_len_fail=dict(type='str',),uri_blist_succ=dict(type='str',),sess_check_fail=dict(type='str',),buf_ovf_hdr_name_len_fail=dict(type='str',),resp_denied=dict(type='str',),sessions_freed=dict(type='str',),out_of_sessions=dict(type='str',),xml_limit_elem=dict(type='str',),buf_ovf_parameter_name_len_fail=dict(type='str',),xml_limit_attr_value_len=dict(type='str',),xml_limit_elem_depth=dict(type='str',),ccn_mask_jcb=dict(type='str',),cookie_decrypt_fail=dict(type='str',),buf_ovf_cookie_value_len_fail=dict(type='str',),buf_ovf_post_size_fail=dict(type='str',),total_req=dict(type='str',),xml_limit_elem_name_len=dict(type='str',),url_check_learn=dict(type='str',),http_method_check_succ=dict(type='str',),xss_chk_url_succ=dict(type='str',),xml_limit_namespace_uri_len=dict(type='str',),post_form_check_reject=dict(type='str',),cookie_encrypt_fail=dict(type='str',),soap_check_failure=dict(type='str',),challenge_captcha_sent=dict(type='str',),form_csrf_tag_fail=dict(type='str',),xml_xss_chk_succ=dict(type='str',),buf_ovf_max_data_parse_fail=dict(type='str',)),
        max_parameter_name_len=dict(type='int',),
        deny_non_masked_passwords=dict(type='bool',),
        challenge_action_javascript=dict(type='bool',),
        max_hdr_name_len=dict(type='int',),
        max_elem_depth=dict(type='int',),
        form_consistency_check=dict(type='bool',),
        redirect_wlist=dict(type='bool',),
        xml_xss_check=dict(type='bool',),
        referer_check=dict(type='bool',),
        wsdl_resp_val_file=dict(type='str',),
        brute_force_check=dict(type='bool',),
        brute_force_test_period=dict(type='int',),
        max_namespace=dict(type='int',),
        max_entity_exp=dict(type='int',),
        form_deny_non_post=dict(type='bool',),
        cookie_encryption_secret=dict(type='str',),
        decode_escaped_chars=dict(type='bool',),
        json_format_check=dict(type='bool',),
        bot_check_policy_file=dict(type='str',),
        xml_schema_resp_val_file=dict(type='str',),
        brute_force_challenge_limit=dict(type='int',),
        allowed_http_methods=dict(type='str',),
        brute_force_resp_codes=dict(type='bool',),
        remove_selfref=dict(type='bool',),
        max_elem_child=dict(type='int',),
        max_entity_exp_depth=dict(type='int',),
        max_array_value_count=dict(type='int',),
        max_elem=dict(type='int',),
        sqlia_check=dict(type='str',choices=['reject','sanitize']),
        max_object_member_count=dict(type='int',),
        http_resp_403=dict(type='bool',),
        http_check=dict(type='bool',),
        brute_force_resp_headers=dict(type='bool',),
        max_cookie_name_len=dict(type='int',),
        remove_comments=dict(type='bool',),
        logging=dict(type='str',),
        uri_wlist_check=dict(type='bool',),
        brute_force_resp_string_file=dict(type='str',),
        form_deny_non_ssl=dict(type='bool',),
        xss_check=dict(type='str',choices=['reject','sanitize']),
        reset_conn=dict(type='bool',),
        referer_safe_url=dict(type='str',),
        remove_spaces=dict(type='bool',),
        brute_force_lockout_limit=dict(type='int',),
        uri_blist_check=dict(type='bool',),
        max_url_len=dict(type='int',),
        max_hdrs_len=dict(type='int',),
        waf_wlist_file=dict(type='str',),
        max_attr_name_len=dict(type='int',),
        lifetime=dict(type='int',),
        max_attr=dict(type='int',),
        xss_check_policy_file=dict(type='str',),
        resp_url_200=dict(type='str',),
        max_post_size=dict(type='int',),
        decode_hex_chars=dict(type='bool',),
        max_line_len=dict(type='int',),
        max_query_len=dict(type='int',),
        sqlia_check_policy_file=dict(type='str',),
        deny_non_ssl_passwords=dict(type='bool',),
        max_data_parse=dict(type='int',),
        max_parameter_total_len=dict(type='int',),
        wsdl_file=dict(type='str',),
        session_check=dict(type='bool',),
        disable=dict(type='bool',),
        filter_resp_hdrs=dict(type='bool',),
        max_cookies=dict(type='int',),
        decode_entities=dict(type='bool',),
        mask=dict(type='str',),
        referer_domain_list_only=dict(type='str',),
        max_attr_value_len=dict(type='int',),
        pcre_mask=dict(type='str',),
        soap_format_check=dict(type='bool',),
        xml_schema_file=dict(type='str',),
        ssn_mask=dict(type='bool',),
        xml_sqlia_check=dict(type='bool',)
    ))
   

    return rv

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/waf/template/{name}"

    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/waf/template/{name}"

    f_dict = {}
    f_dict["name"] = module.params["name"]

    return url_base.format(**f_dict)

def stats_url(module):
    """Return the URL for statistical data of and existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/stats"

def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]

def build_envelope(title, data):
    return {
        title: data
    }

def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")

def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        elif isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv

def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v is not None:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            elif isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)

def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if x in params and params.get(x) is not None])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

def get(module):
    return module.client.get(existing_url(module))

def get_list(module):
    return module.client.get(list_url(module))

def get_stats(module):
    if module.params.get("stats"):
        query_params = {}
        for k,v in module.params["stats"].items():
            query_params[k.replace('_', '-')] = v
        return module.client.get(stats_url(module),
                                 params=query_params)
    return module.client.get(stats_url(module))

def exists(module):
    try:
        return get(module)
    except a10_ex.NotFound:
        return None

def report_changes(module, result, existing_config, payload):
    if existing_config:
        for k, v in payload["template"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
               break
            else:
                if existing_config["template"][k] != v:
                    if result["changed"] != True:
                        result["changed"] = True
                    existing_config["template"][k] = v
            result.update(**existing_config)
    else:
        result.update(**payload)
    return result

def create(module, result, payload):
    try:
        post_result = module.client.post(new_url(module), payload)
        if post_result:
            result.update(**post_result)
        result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def delete(module, result):
    try:
        module.client.delete(existing_url(module))
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def update(module, result, existing_config, payload):
    try:
        post_result = module.client.post(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def present(module, result, existing_config):
    payload = build_json("template", module)
    changed_config = report_changes(module, result, existing_config, payload)
    if module.check_mode:
        return changed_config
    elif not existing_config:
        return create(module, result, payload)
    elif existing_config and not changed_config.get('changed'):
        return update(module, result, existing_config, payload)
    else:
        result["changed"] = True
        return result

def absent(module, result, existing_config):
    if module.check_mode:
        if existing_config:
            result["changed"] = True
            return result
        else:
            result["changed"] = False
            return result
    else:
        return delete(module, result)

def replace(module, result, existing_config, payload):
    try:
        post_result = module.client.put(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def run_command(module):
    run_errors = []

    result = dict(
        changed=False,
        original_message="",
        message="",
        result={}
    )

    state = module.params["state"]
    a10_host = module.params["a10_host"]
    a10_username = module.params["a10_username"]
    a10_password = module.params["a10_password"]
    a10_port = module.params["a10_port"] 
    a10_protocol = module.params["a10_protocol"]
    a10_partition = module.params["a10_partition"]
    a10_device_context_id = module.params["a10_device_context_id"]

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        for ve in validation_errors:
            run_errors.append(ve)
    
    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(a10_host, a10_port, a10_protocol, a10_username, a10_password)
    
    if a10_partition:
        module.client.activate_partition(a10_partition)

    if a10_device_context_id:
        module.client.change_context(a10_device_context_id)

    existing_config = exists(module)

    if state == 'present':
        result = present(module, result, existing_config)
    elif state == 'absent':
        result = absent(module, result, existing_config)
    elif state == 'noop':
        if module.params.get("get_type") == "single":
            result["result"] = get(module)
        elif module.params.get("get_type") == "list":
            result["result"] = get_list(module)
        elif module.params.get("get_type") == "stats":
            result["result"] = get_stats(module)
    module.client.session.close()
    return result

def main():
    module = AnsibleModule(argument_spec=get_argspec(), supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)

# standard ansible module imports
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()