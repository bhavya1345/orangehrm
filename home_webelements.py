class OrangeHrmElements:
    user_name_text_box_XPATH = "//input[@name='username']"
    password_text_box_XPATH = "//input[@name='password']"
    login_button_XPATH = "//button[@type='submit']"
    invalid_credentials_XPATH = "//p[text() = 'Invalid credentials']"
    PIM_module_link_text = "PIM"
    new_employee_add_button_XPATH = "//button[text()=' Add ']"
    employee_first_name_XPATH = "//*[@name='firstName']"
    employee_middle_name_XPATH = "//*[@name='middleName']"
    employee_last_name_XPATH = "//*[@name='lastName']"
    save_button_XPATH = "//button[@type='submit']"
    employee_list_XPATH = "//a[contains(text(),'Employee List')]"
    employee_id_XPATH = "//label[contains(text(),'Employee Id')]/parent::div/following-sibling::div/input"
    employee_search_button_XPATH = "//button[@type='submit']"
    driver_license_no_XPATH = "//label[contains(text(),'License Number')]/parent::div/following-sibling::div/input"
    license_expiry_XPATH = "//label[contains(text(),'License Expiry " \
                           "Date')]/parent::div/following-sibling::div//div/div/input "
    gender_male_XPATH = "//input[@value='1']/following-sibling::span"
    gender_female_XPATH = "//input[@value='2']/following-sibling::span"
    employee_edit_button = "//i[@class='oxd-icon bi-pencil-fill']"
    employee_delete_button = "//i[@class='oxd-icon bi-trash']"
    yes_delete_button_XPATH = "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger " \
                              "orangehrm-button-margin'] "
    nationality_button_XPATH = "//label[text()='Nationality']/../following-sibling::div/div//following-sibling::div"
    nationality_text_XPATH = "//label[text()='Nationality']/../following-sibling::div/div/div/div[@class " \
                             "='oxd-select-text-input'] "
    nationality_list = "//div[@role='option']"
    employee_image_XPATH = "//img[@class = 'employee-image']"
    employee_image_upload_button_XPATH = "//button[contains(@class,'employee-image-action')]"
    dashboard_text_XPATH = "//h6[text()='Dashboard']"
    home_page_search_text_box_XPATH = "//input[@placeholder='Search']"
    admin_module_XPATH = "//span[text()='Admin']"
    user_management_navigation_XPATH = "//span[contains(text(),'User Management')]"
    users_XPATH = "//a[text()='Users']"
    user_role_dropdown_button_XPATH = "//label[text()='User Role']/../following-sibling::div/div/div/*/*"
    user_role_dropdown_list_XPATH = "//div[@role='option']"
    status_dropdown_button_XPATH = "//label[text()='Status']/../following-sibling::div/div/div/*/*"
    status_dropdown_list_XPATH = "//div[@role='option']"
    SSN_number_XPATH = "//label[text()='SSN Number']/../following-sibling::div/input"
    SIN_number_XPATH = "//label[text()='SIN Number']/../following-sibling::div/input"
    marital_status_button_XPATH = "//label[text()='Marital Status']/../following-sibling::div/div//following-sibling" \
                                  "::div "
    marital_status_text_XPATH = "//label[text()='Marital Status']/../following-sibling::div/div/div/div[@class " \
                                "='oxd-select-text-input'] "
    marital_status_list = "//div[@role='option']"
    date_of_brith = "//label[contains(text(),'Date of Birth')]/parent::div/following-sibling::div//div/div/input "
    employee_full_name_XPATH = "//label[text()='Employee Name']/../following-sibling::div/div/div/input"
    employee_list_present_elements_XPATH = "//div[@role='tab']/a"
    blood_type_button_XPATH = "//label[text()='Blood Type']/../following-sibling::div/div//following-sibling::div"
    blood_type_XPATH = "//label[text()='Blood Type']/../following-sibling::div/div/div/div[@class " \
                       "='oxd-select-text-input'] "
    blood_type_list_XPATH = "//div[@role='option']"
    edit_save_button = "//label[text()='Blood Type']/../../../../../following-sibling::div/button"
    employee_contact_details_tap_XPATH = "//a[text()='Contact Details']"
    street_1_input_box_XPATH = "//label[text()='Street 1']/../following-sibling::div/input"
    city_input_box_XPATH = "//label[text()='City']/../following-sibling::div/input"
    state_province_input_box_XPATH = "//label[text()='State/Province']/../following-sibling::div/input"
    zip_code_input_box_XPATH = "//label[text()='Zip/Postal Code']/../following-sibling::div/input"
    country_button_XPATH = "//label[text()='Country']/../following-sibling::div/div//following-sibling::div"
    country_type_list_XPATH = "//div[@role='option']"
    home_phone_no_XPATH = "//label[text()='Home']/../following-sibling::div/input"
    mobile_no_XPATH = "//label[text()='Mobile']/../following-sibling::div/input"
    work_phone_no_XPATH = "//label[text()='Work']/../following-sibling::div/input"
    work_email_id_XPATH = "//label[text()='Work Email']/../following-sibling::div/input"
    emergency_contacts_add_button_XPATH = "//h6[text()='Assigned Emergency Contacts']/following-sibling::button"
    emergency_contacts_name_input_XPATH = "//label[text()='Name']/../following-sibling::div/input"
    relationship_input_XPATH = "//label[text()='Relationship']/../following-sibling::div/input"
    employee_emergency_contact_details_tap_XPATH = "//a[text()='Emergency Contacts']"
    relationship_dropdown_button_XPATH = "//label[text()='Relationship']/../following-sibling::div/div/" \
                                         "/following-sibling::div"
    relationship_dropdown_list_XPATH = "//div[@role='option']"
    employee_dependent_contact_details_tap_XPATH = "//a[text()='Dependents']"
    employee_dependent_add_button_XPATH = "//h6[text()='Assigned Dependents']/following-sibling::button"
    employee_job_details_tap_XPATH = "//a[text()='Job']"
    employee_join_date_XPATH = "//label[contains(text(),'Joined Date')]/parent::div/following-sibling::div/" \
                               "/div/div/input "
    employee_job_title_dropdown_button_XPATH = "//label[text()='Job Title']/../following-sibling::div/div" \
                                               "//following-sibling::div"
    employee_job_title_dropdown_list_XPATH = "//div[@role='option']"
    employee_job_category_dropdown_button_XPATH = "//label[text()='Job Category']/../following-sibling::div/div" \
                                                  "//following-sibling::div"
    employee_job_category_dropdown_list_XPATH = "//div[@role='option']"
    employee_sub_unit_dropdown_button_XPATH = "//label[text()='Sub Unit']/../following-sibling::div/div/" \
                                              "/following-sibling::div"
    employee_sub_unit_dropdown_list_XPATH = "//div[@role='option']"
    employee_location_dropdown_button_XPATH = "//label[text()='Location']/../following-sibling::div/div/" \
                                              "/following-sibling::div"
    employee_location_dropdown_list_XPATH = "//div[@role='option']"
    employment_status_dropdown_button_XPATH = "//label[text()='Employment Status']/../following-sibling::" \
                                              "div/div//following-sibling::div"
    employment_status_dropdown_list_XPATH = "//div[@role='option']"
    employee_contract_details_toggle_button_XPATH = "//p[text()='Include Employment Contract Details']" \
                                                    "/following-sibling::div/label/span"
    employee_contract_start_date_XPATH = "//label[contains(text(),'Contract Start Date')]/parent::div/" \
                                         "following-sibling::div//div/div/input "
    employee_contract_end_date_XPATH = "//label[contains(text(),'Contract End Date')]/parent::div/" \
                                       "following-sibling::div//div/div/input "
    terminate_employment_and_activation_XPATH = "//h6[text()='Employee Termination / Activiation']" \
                                                "/following-sibling::button"
    termination_date_XPATH = "//label[contains(text(),'Termination " \
                             "Date')]/parent::div/following-sibling::div//div/div/input "
    termination_reason_dropdown_button_XPATH = "//label[text()='Termination " \
                                               "Reason']/../following-sibling::div/div//following-sibling::div "
    termination_reason_dropdown_list_XPATH = "//div[@role='option']"
    required_save_button = "//p[text()=' * Required']/following-sibling::button[@type='submit']"
    employee_salary_tap_XPATH = "//a[text()='Salary']"
    employee_salary_components_add_button_XPATH = "//h6[text()='Assigned Salary Components']/following-sibling::button"
    employee_salary_component_input_box_XPATH = "//label[text()='Salary Component']/../following-sibling::div/input"
    employee_pay_grade_dropdown_button_XPATH = "//label[text()='Pay Grade']/../following-sibling::div/div" \
                                               "//following-sibling::div "
    employee_pay_grade_list_XPATH = "//div[@role='option']"
    employee_pay_frequency_dropdown_button_XPATH = "//label[text()='Pay Frequency']/../following-sibling::div/div" \
                                                   "//following-sibling::div "
    employee_pay_frequency_list_XPATH = "//div[@role='option']"
    currency_dropdown_button_XPATH = "//label[text()='Currency']/../following-sibling::div/div" \
                                     "//following-sibling::div "
    currency_list_XPATH = "//div[@role='option']"
    salary_amount_input_box_XPATH = "//label[text()='Amount']/../following-sibling::div/input"
    bank_account_number_input_box_XPATH = "//label[text()='Account Number']/../following-sibling::div/input"
    bank_account_type_dropdown_button_XPATH = "//label[text()='Account Type']/../following-sibling::div/div" \
                                              "//following-sibling::div "
    bank_account_type_list_XPATH = "//div[@role='option']"
    bank_account_routing_number_input_box_XPATH = "//label[text()='Routing Number']/../following-sibling::div/input"
    deposit_amount_input_box_XPATH = "//label[text()='Routing Number']/../../.././following-sibling::div/div" \
                                     "/*/following-sibling::div/input "
    direct_deposit_details_toggle_button_XPATH = "//p[text()='Include Direct Deposit Details']" \
                                                 "/following-sibling::div/label/span"
    visible_salary_component_XPATH = "//div[text()='Salary Component']"
    federal_income_tax_status_dropdown_button_XPATH = "//h6[text()='State Income " \
                                                      "Tax']/preceding-sibling::div/div/*/*/div/div/*/*/* "
    federal_income_tax_status_list_XPATH = "//div[@role='option']"
    state_income_tax_status_dropdown_button_XPATH = "//label[text()='Unemployment " \
                                                    "State']/../../../preceding-sibling::div[2]/div/div/div/*/*/* "
    state_income_tax_status_list_XPATH = "//div[@role='option']"

    state_income_tax_state_dropdown_button_XPATH = "//label[text()='State']/../following-sibling::div/*/*/*/*"
    state_income_tax_state_list_XPATH = "//div[@role='option']"
    state_income_tax_unemployment_state_dropdown_button_XPATH = "//label[text()='Unemployment " \
                                                                "State']/../following-sibling::div/*/*/*/* "
    state_income_tax_unemployment_state_list_XPATH = "//div[@role='option']"
    state_income_tax_work_state_dropdown_button_XPATH = "//label[text()='Work State']/../following-sibling::div" \
                                                        "/*/*/*/* "
    state_income_tax_work_state_list_XPATH = "//div[@role='option']"
    employee_tax_exemptions_tap_XPATH = "//a[text()='Tax Exemptions']"
