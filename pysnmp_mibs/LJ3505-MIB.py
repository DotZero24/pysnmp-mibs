_A5='eJapanesePostcardDouble'
_A4='eStatement'
_A3='eWritingImageError'
_A2='eWritingImage'
_A1='eVerifiedImageError'
_A0='eReceivedImageError'
_z='eEnabled'
_y='eDisabled'
_x='eISOandJISA4R'
_w='eUSLetterR'
_v='eJapansePostcardDouble'
_u='eISOB5'
_t='eJISB4'
_s='eISOandJISA3'
_r='eROC8K'
_q='eLedger'
_p='eIOCard'
_o='eInitiateAction'
_n='eOffline'
_m='DisplayString'
_l='eAnySize'
_k='eAnyCustomSize'
_j='eInitializing'
_i='eUnknownMediaSize'
_h='eAuto'
_g='eFoolscap'
_f='eInternationalB5'
_e='eInternationalC5'
_d='eInternationalDL'
_c='eCommercial10'
_b='eMonarch'
_a='eCustom'
_Z='eJISB5'
_Y='eISOandJISA5'
_X='eJISExecutive'
_W='eROC16K'
_V='eUSLegal'
_U='eUSExecutive'
_T='mandatory'
_S='eFalse'
_R='eISOandJISA4'
_Q='eUSLetter'
_P='eOn'
_O='eTrue'
_N='eOff'
_M='eRamRom'
_L='eFlashMemory'
_K='eVolatileRandomAccessMemory'
_J='eReadOnlyMemory'
_I='eUnknown'
_H='eUnSupported'
_G='eEmpty'
_F='write-only'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='optional'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_m,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Dm_ObjectIdentity=ObjectIdentity
dm=_Dm_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1))
_Device_system_ObjectIdentity=ObjectIdentity
device_system=_Device_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1))
_Settings_system_ObjectIdentity=ObjectIdentity
settings_system=_Settings_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1))
_Energy_star_Type=Integer32
_Energy_star_Object=MibScalar
energy_star=_Energy_star_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,1),_Energy_star_Type())
energy_star.setMaxAccess(_C)
if mibBuilder.loadTexts:energy_star.setStatus(_A)
class _Sleep_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_O,2)))
_Sleep_mode_Type.__name__=_D
_Sleep_mode_Object=MibScalar
sleep_mode=_Sleep_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,2),_Sleep_mode_Type())
sleep_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleep_mode.setStatus(_A)
class _Date_display_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,6)));namedValues=NamedValues(*(('eDateDisplayMMM-DD-YYYY',4),('eDateDisplayDD-MMM-YYYY',5),('eDateDisplayYYYY-MMM-DD',6)))
_Date_display_Type.__name__=_D
_Date_display_Object=MibScalar
date_display=_Date_display_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,22),_Date_display_Type())
date_display.setMaxAccess(_C)
if mibBuilder.loadTexts:date_display.setStatus(_A)
class _Mono_color_switching_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eAutoSwitch',1),('eMostlyColor',2),('eMostlyMono',3)))
_Mono_color_switching_mode_Type.__name__=_D
_Mono_color_switching_mode_Object=MibScalar
mono_color_switching_mode=_Mono_color_switching_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,31),_Mono_color_switching_mode_Type())
mono_color_switching_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:mono_color_switching_mode.setStatus(_A)
_Device_configure_ObjectIdentity=ObjectIdentity
device_configure=_Device_configure_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,32))
class _Device_configure_printer_parameters_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_Device_configure_printer_parameters_Type.__name__=_E
_Device_configure_printer_parameters_Object=MibScalar
device_configure_printer_parameters=_Device_configure_printer_parameters_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,32,12),_Device_configure_printer_parameters_Type())
device_configure_printer_parameters.setMaxAccess(_C)
if mibBuilder.loadTexts:device_configure_printer_parameters.setStatus(_A)
class _Color_supply_out_action_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eStop',1),('eAutoContinueBlack',2)))
_Color_supply_out_action_Type.__name__=_D
_Color_supply_out_action_Object=MibScalar
color_supply_out_action=_Color_supply_out_action_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,34),_Color_supply_out_action_Type())
color_supply_out_action.setMaxAccess(_C)
if mibBuilder.loadTexts:color_supply_out_action.setStatus(_A)
class _Direct_connect_ports_enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_O,2),(_H,3)))
_Direct_connect_ports_enable_Type.__name__=_D
_Direct_connect_ports_enable_Object=MibScalar
direct_connect_ports_enable=_Direct_connect_ports_enable_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,43),_Direct_connect_ports_enable_Type())
direct_connect_ports_enable.setMaxAccess(_C)
if mibBuilder.loadTexts:direct_connect_ports_enable.setStatus(_A)
class _Control_panel_supplies_status_message_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eShow',1),('eDontShow',2)))
_Control_panel_supplies_status_message_Type.__name__=_D
_Control_panel_supplies_status_message_Object=MibScalar
control_panel_supplies_status_message=_Control_panel_supplies_status_message_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,44),_Control_panel_supplies_status_message_Type())
control_panel_supplies_status_message.setMaxAccess(_C)
if mibBuilder.loadTexts:control_panel_supplies_status_message.setStatus(_A)
class _Speed_energy_usage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eFasterFirstPage',1),('eSaveEnergy',2)))
_Speed_energy_usage_Type.__name__=_D
_Speed_energy_usage_Object=MibScalar
speed_energy_usage=_Speed_energy_usage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,50),_Speed_energy_usage_Type())
speed_energy_usage.setMaxAccess(_C)
if mibBuilder.loadTexts:speed_energy_usage.setStatus(_A)
class _Calibration_data_reset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eFALSE',1),('eTRUE',2)))
_Calibration_data_reset_Type.__name__=_D
_Calibration_data_reset_Object=MibScalar
calibration_data_reset=_Calibration_data_reset_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,86),_Calibration_data_reset_Type())
calibration_data_reset.setMaxAccess(_F)
if mibBuilder.loadTexts:calibration_data_reset.setStatus(_T)
_Status_system_ObjectIdentity=ObjectIdentity
status_system=_Status_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2))
class _On_off_line_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eOnline',1),(_n,2),('eOfflineAtEndOfJob',3)))
_On_off_line_Type.__name__=_D
_On_off_line_Object=MibScalar
on_off_line=_On_off_line_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,5),_On_off_line_Type())
on_off_line.setMaxAccess(_C)
if mibBuilder.loadTexts:on_off_line.setStatus(_A)
class __pysmi_continue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_o,1),('eRetry',2),('eRetryAndCheck',3),('eUseLoadedMedia',4),('eEjectAndWait',5),('eSelectMediaSize',6)))
__pysmi_continue_Type.__name__=_D
__pysmi_continue_Object=MibScalar
_pysmi_continue=__pysmi_continue_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,6),__pysmi_continue_Type())
_pysmi_continue.setMaxAccess(_F)
if mibBuilder.loadTexts:_pysmi_continue.setStatus(_A)
class _Auto_continue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_P,2)))
_Auto_continue_Type.__name__=_D
_Auto_continue_Object=MibScalar
auto_continue=_Auto_continue_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,7),_Auto_continue_Type())
auto_continue.setMaxAccess(_C)
if mibBuilder.loadTexts:auto_continue.setStatus(_A)
class _Install_date_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_Install_date_Type.__name__=_E
_Install_date_Object=MibScalar
install_date=_Install_date_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,8),_Install_date_Type())
install_date.setMaxAccess(_C)
if mibBuilder.loadTexts:install_date.setStatus(_A)
_Perm_store_init_occurred_Type=OctetString
_Perm_store_init_occurred_Object=MibScalar
perm_store_init_occurred=_Perm_store_init_occurred_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,10),_Perm_store_init_occurred_Type())
perm_store_init_occurred.setMaxAccess(_B)
if mibBuilder.loadTexts:perm_store_init_occurred.setStatus(_A)
_Date_and_time_Type=OctetString
_Date_and_time_Object=MibScalar
date_and_time=_Date_and_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,17),_Date_and_time_Type())
date_and_time.setMaxAccess(_C)
if mibBuilder.loadTexts:date_and_time.setStatus(_A)
class _Service_id_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_Service_id_Type.__name__=_E
_Service_id_Object=MibScalar
service_id=_Service_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,19),_Service_id_Type())
service_id.setMaxAccess(_C)
if mibBuilder.loadTexts:service_id.setStatus(_A)
_Display_ObjectIdentity=ObjectIdentity
display=_Display_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,20))
_Display_status_ObjectIdentity=ObjectIdentity
display_status=_Display_status_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,20,1))
class _Show_address_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_N,1),(_h,3)))
_Show_address_Type.__name__=_D
_Show_address_Object=MibScalar
show_address=_Show_address_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,20,1,3),_Show_address_Type())
show_address.setMaxAccess(_C)
if mibBuilder.loadTexts:show_address.setStatus(_A)
class _Time_display_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eTimeDisplayTwelveHour',1),('eTimeDisplayTwentyFourHour',2)))
_Time_display_Type.__name__=_D
_Time_display_Object=MibScalar
time_display=_Time_display_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,28),_Time_display_Type())
time_display.setMaxAccess(_C)
if mibBuilder.loadTexts:time_display.setStatus(_A)
class _Job_input_auto_continue_timeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,3600))
_Job_input_auto_continue_timeout_Type.__name__=_D
_Job_input_auto_continue_timeout_Object=MibScalar
job_input_auto_continue_timeout=_Job_input_auto_continue_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,35),_Job_input_auto_continue_timeout_Type())
job_input_auto_continue_timeout.setMaxAccess(_C)
if mibBuilder.loadTexts:job_input_auto_continue_timeout.setStatus(_A)
_Job_input_auto_continue_mode_Type=OctetString
_Job_input_auto_continue_mode_Object=MibScalar
job_input_auto_continue_mode=_Job_input_auto_continue_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,36),_Job_input_auto_continue_mode_Type())
job_input_auto_continue_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:job_input_auto_continue_mode.setStatus(_A)
_Background_message_ObjectIdentity=ObjectIdentity
background_message=_Background_message_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37))
_Background_message1_ObjectIdentity=ObjectIdentity
background_message1=_Background_message1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,1))
class _Background_status_msg_line1_part1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Background_status_msg_line1_part1_Type.__name__=_E
_Background_status_msg_line1_part1_Object=MibScalar
background_status_msg_line1_part1=_Background_status_msg_line1_part1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,1,1),_Background_status_msg_line1_part1_Type())
background_status_msg_line1_part1.setMaxAccess(_C)
if mibBuilder.loadTexts:background_status_msg_line1_part1.setStatus(_A)
_Background_message2_ObjectIdentity=ObjectIdentity
background_message2=_Background_message2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,2))
class _Background_status_msg_line2_part1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Background_status_msg_line2_part1_Type.__name__=_E
_Background_status_msg_line2_part1_Object=MibScalar
background_status_msg_line2_part1=_Background_status_msg_line2_part1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,2,1),_Background_status_msg_line2_part1_Type())
background_status_msg_line2_part1.setMaxAccess(_C)
if mibBuilder.loadTexts:background_status_msg_line2_part1.setStatus(_A)
class _Error_log_clear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eClearErrorLog',1))
_Error_log_clear_Type.__name__=_D
_Error_log_clear_Object=MibScalar
error_log_clear=_Error_log_clear_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,38),_Error_log_clear_Type())
error_log_clear.setMaxAccess(_F)
if mibBuilder.loadTexts:error_log_clear.setStatus(_A)
class _Job_output_auto_continue_timeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,3600))
_Job_output_auto_continue_timeout_Type.__name__=_D
_Job_output_auto_continue_timeout_Object=MibScalar
job_output_auto_continue_timeout=_Job_output_auto_continue_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,40),_Job_output_auto_continue_timeout_Type())
job_output_auto_continue_timeout.setMaxAccess(_C)
if mibBuilder.loadTexts:job_output_auto_continue_timeout.setStatus(_A)
_Collated_originals_support_Type=OctetString
_Collated_originals_support_Object=MibScalar
collated_originals_support=_Collated_originals_support_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,42),_Collated_originals_support_Type())
collated_originals_support.setMaxAccess(_B)
if mibBuilder.loadTexts:collated_originals_support.setStatus(_A)
_Localization_languages_supported_Type=OctetString
_Localization_languages_supported_Object=MibScalar
localization_languages_supported=_Localization_languages_supported_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,52),_Localization_languages_supported_Type())
localization_languages_supported.setMaxAccess(_B)
if mibBuilder.loadTexts:localization_languages_supported.setStatus(_A)
_Localization_countries_supported_Type=OctetString
_Localization_countries_supported_Object=MibScalar
localization_countries_supported=_Localization_countries_supported_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,53),_Localization_countries_supported_Type())
localization_countries_supported.setMaxAccess(_B)
if mibBuilder.loadTexts:localization_countries_supported.setStatus(_A)
_Host_application_available_memory_Type=Integer32
_Host_application_available_memory_Object=MibScalar
host_application_available_memory=_Host_application_available_memory_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,59),_Host_application_available_memory_Type())
host_application_available_memory.setMaxAccess(_B)
if mibBuilder.loadTexts:host_application_available_memory.setStatus(_A)
class _Control_panel_button_press_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)));namedValues=NamedValues(*(('eMenuPlusButton',2),('eMenuMinusButton',3),('eItemPlusButton',4),('eItemMinusButton',5),('eValuePlusButton',6),('eValueMinusButton',7),('eSelectButton',8),('eCancelJobButton',9),('ePauseResumeButton',10),('eUpArrowButton',11),('eDownArrowButton',12),('eBackButton',13),('eQuestionMarkButton',14),('eClearButton',15),('eNumericButton0',16),('eNumericButton1',17),('eNumericButton2',18),('eNumericButton3',19),('eNumericButton4',20),('eNumericButton5',21),('eNumericButton6',22),('eNumericButton7',23),('eNumericButton8',24),('eNumericButton9',25),('eRotateButton',26),('eInfoButton',27),('eMenuButton',28),('eStopButton',29)))
_Control_panel_button_press_Type.__name__=_D
_Control_panel_button_press_Object=MibScalar
control_panel_button_press=_Control_panel_button_press_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,60),_Control_panel_button_press_Type())
control_panel_button_press.setMaxAccess(_C)
if mibBuilder.loadTexts:control_panel_button_press.setStatus(_A)
_Control_panel_display_contents_change_counter_Type=Integer32
_Control_panel_display_contents_change_counter_Object=MibScalar
control_panel_display_contents_change_counter=_Control_panel_display_contents_change_counter_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,63),_Control_panel_display_contents_change_counter_Type())
control_panel_display_contents_change_counter.setMaxAccess(_B)
if mibBuilder.loadTexts:control_panel_display_contents_change_counter.setStatus(_A)
_Control_panel_display_contents_crc_Type=Integer32
_Control_panel_display_contents_crc_Object=MibScalar
control_panel_display_contents_crc=_Control_panel_display_contents_crc_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,64),_Control_panel_display_contents_crc_Type())
control_panel_display_contents_crc.setMaxAccess(_B)
if mibBuilder.loadTexts:control_panel_display_contents_crc.setStatus(_A)
_Control_panel_display_ObjectIdentity=ObjectIdentity
control_panel_display=_Control_panel_display_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,65))
_Control_panel_display_graphical_contents_Type=OctetString
_Control_panel_display_graphical_contents_Object=MibScalar
control_panel_display_graphical_contents=_Control_panel_display_graphical_contents_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,65,1),_Control_panel_display_graphical_contents_Type())
control_panel_display_graphical_contents.setMaxAccess(_B)
if mibBuilder.loadTexts:control_panel_display_graphical_contents.setStatus(_A)
_Page_frame_memory_available_Type=Integer32
_Page_frame_memory_available_Object=MibScalar
page_frame_memory_available=_Page_frame_memory_available_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,72),_Page_frame_memory_available_Type())
page_frame_memory_available.setMaxAccess(_B)
if mibBuilder.loadTexts:page_frame_memory_available.setStatus(_A)
_Id_ObjectIdentity=ObjectIdentity
id=_Id_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3))
_Model_number_Type=OctetString
_Model_number_Object=MibScalar
model_number=_Model_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,1),_Model_number_Type())
model_number.setMaxAccess(_B)
if mibBuilder.loadTexts:model_number.setStatus(_A)
class _Model_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Model_name_Type.__name__=_E
_Model_name_Object=MibScalar
model_name=_Model_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,2),_Model_name_Type())
model_name.setMaxAccess(_B)
if mibBuilder.loadTexts:model_name.setStatus(_A)
class _Serial_number_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Serial_number_Type.__name__=_E
_Serial_number_Object=MibScalar
serial_number=_Serial_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,3),_Serial_number_Type())
serial_number.setMaxAccess(_B)
if mibBuilder.loadTexts:serial_number.setStatus(_A)
_Fw_rom_datecode_Type=OctetString
_Fw_rom_datecode_Object=MibScalar
fw_rom_datecode=_Fw_rom_datecode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,5),_Fw_rom_datecode_Type())
fw_rom_datecode.setMaxAccess(_B)
if mibBuilder.loadTexts:fw_rom_datecode.setStatus(_A)
_Fw_rom_revision_Type=OctetString
_Fw_rom_revision_Object=MibScalar
fw_rom_revision=_Fw_rom_revision_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,6),_Fw_rom_revision_Type())
fw_rom_revision.setMaxAccess(_B)
if mibBuilder.loadTexts:fw_rom_revision.setStatus(_A)
class _Device_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Device_name_Type.__name__=_E
_Device_name_Object=MibScalar
device_name=_Device_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,10),_Device_name_Type())
device_name.setMaxAccess(_C)
if mibBuilder.loadTexts:device_name.setStatus(_A)
_Device_location_Type=OctetString
_Device_location_Object=MibScalar
device_location=_Device_location_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,11),_Device_location_Type())
device_location.setMaxAccess(_C)
if mibBuilder.loadTexts:device_location.setStatus(_A)
_Asset_number_Type=OctetString
_Asset_number_Object=MibScalar
asset_number=_Asset_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,12),_Asset_number_Type())
asset_number.setMaxAccess(_C)
if mibBuilder.loadTexts:asset_number.setStatus(_A)
_Formatter_serial_number_Type=OctetString
_Formatter_serial_number_Object=MibScalar
formatter_serial_number=_Formatter_serial_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,20),_Formatter_serial_number_Type())
formatter_serial_number.setMaxAccess(_B)
if mibBuilder.loadTexts:formatter_serial_number.setStatus(_A)
_Interface_ObjectIdentity=ObjectIdentity
interface=_Interface_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4))
_Simm_ObjectIdentity=ObjectIdentity
simm=_Simm_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1))
_Simm1_ObjectIdentity=ObjectIdentity
simm1=_Simm1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1))
class _Simm1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm1_type_Type.__name__=_D
_Simm1_type_Object=MibScalar
simm1_type=_Simm1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,4),_Simm1_type_Type())
simm1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm1_type.setStatus(_A)
_Simm1_capacity_Type=Integer32
_Simm1_capacity_Object=MibScalar
simm1_capacity=_Simm1_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,5),_Simm1_capacity_Type())
simm1_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm1_capacity.setStatus(_A)
_Simm1_bank_ObjectIdentity=ObjectIdentity
simm1_bank=_Simm1_bank_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,6))
_Simm1_bank1_ObjectIdentity=ObjectIdentity
simm1_bank1=_Simm1_bank1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,6,1))
class _Simm1_bank1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm1_bank1_type_Type.__name__=_D
_Simm1_bank1_type_Object=MibScalar
simm1_bank1_type=_Simm1_bank1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,6,1,1),_Simm1_bank1_type_Type())
simm1_bank1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm1_bank1_type.setStatus(_A)
_Simm1_bank1_capacity_Type=Integer32
_Simm1_bank1_capacity_Object=MibScalar
simm1_bank1_capacity=_Simm1_bank1_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,6,1,2),_Simm1_bank1_capacity_Type())
simm1_bank1_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm1_bank1_capacity.setStatus(_A)
_Simm1_bank2_ObjectIdentity=ObjectIdentity
simm1_bank2=_Simm1_bank2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,6,2))
class _Simm1_bank2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm1_bank2_type_Type.__name__=_D
_Simm1_bank2_type_Object=MibScalar
simm1_bank2_type=_Simm1_bank2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,6,2,1),_Simm1_bank2_type_Type())
simm1_bank2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm1_bank2_type.setStatus(_A)
_Simm1_bank2_capacity_Type=Integer32
_Simm1_bank2_capacity_Object=MibScalar
simm1_bank2_capacity=_Simm1_bank2_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,6,2,2),_Simm1_bank2_capacity_Type())
simm1_bank2_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm1_bank2_capacity.setStatus(_A)
_Simm2_ObjectIdentity=ObjectIdentity
simm2=_Simm2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2))
class _Simm2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm2_type_Type.__name__=_D
_Simm2_type_Object=MibScalar
simm2_type=_Simm2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,4),_Simm2_type_Type())
simm2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm2_type.setStatus(_A)
_Simm2_capacity_Type=Integer32
_Simm2_capacity_Object=MibScalar
simm2_capacity=_Simm2_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,5),_Simm2_capacity_Type())
simm2_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm2_capacity.setStatus(_A)
_Simm2_bank_ObjectIdentity=ObjectIdentity
simm2_bank=_Simm2_bank_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,6))
_Simm2_bank1_ObjectIdentity=ObjectIdentity
simm2_bank1=_Simm2_bank1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,6,1))
class _Simm2_bank1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm2_bank1_type_Type.__name__=_D
_Simm2_bank1_type_Object=MibScalar
simm2_bank1_type=_Simm2_bank1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,6,1,1),_Simm2_bank1_type_Type())
simm2_bank1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm2_bank1_type.setStatus(_A)
_Simm2_bank1_capacity_Type=Integer32
_Simm2_bank1_capacity_Object=MibScalar
simm2_bank1_capacity=_Simm2_bank1_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,6,1,2),_Simm2_bank1_capacity_Type())
simm2_bank1_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm2_bank1_capacity.setStatus(_A)
_Simm2_bank2_ObjectIdentity=ObjectIdentity
simm2_bank2=_Simm2_bank2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,6,2))
class _Simm2_bank2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm2_bank2_type_Type.__name__=_D
_Simm2_bank2_type_Object=MibScalar
simm2_bank2_type=_Simm2_bank2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,6,2,1),_Simm2_bank2_type_Type())
simm2_bank2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm2_bank2_type.setStatus(_A)
_Simm2_bank2_capacity_Type=Integer32
_Simm2_bank2_capacity_Object=MibScalar
simm2_bank2_capacity=_Simm2_bank2_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,6,2,2),_Simm2_bank2_capacity_Type())
simm2_bank2_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm2_bank2_capacity.setStatus(_A)
_Simm3_ObjectIdentity=ObjectIdentity
simm3=_Simm3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3))
class _Simm3_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm3_type_Type.__name__=_D
_Simm3_type_Object=MibScalar
simm3_type=_Simm3_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,4),_Simm3_type_Type())
simm3_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm3_type.setStatus(_A)
_Simm3_capacity_Type=Integer32
_Simm3_capacity_Object=MibScalar
simm3_capacity=_Simm3_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,5),_Simm3_capacity_Type())
simm3_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm3_capacity.setStatus(_A)
_Simm3_bank_ObjectIdentity=ObjectIdentity
simm3_bank=_Simm3_bank_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,6))
_Simm3_bank1_ObjectIdentity=ObjectIdentity
simm3_bank1=_Simm3_bank1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,6,1))
class _Simm3_bank1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm3_bank1_type_Type.__name__=_D
_Simm3_bank1_type_Object=MibScalar
simm3_bank1_type=_Simm3_bank1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,6,1,1),_Simm3_bank1_type_Type())
simm3_bank1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm3_bank1_type.setStatus(_A)
_Simm3_bank1_capacity_Type=Integer32
_Simm3_bank1_capacity_Object=MibScalar
simm3_bank1_capacity=_Simm3_bank1_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,6,1,2),_Simm3_bank1_capacity_Type())
simm3_bank1_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm3_bank1_capacity.setStatus(_A)
_Simm3_bank2_ObjectIdentity=ObjectIdentity
simm3_bank2=_Simm3_bank2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,6,2))
class _Simm3_bank2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm3_bank2_type_Type.__name__=_D
_Simm3_bank2_type_Object=MibScalar
simm3_bank2_type=_Simm3_bank2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,6,2,1),_Simm3_bank2_type_Type())
simm3_bank2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm3_bank2_type.setStatus(_A)
_Simm3_bank2_capacity_Type=Integer32
_Simm3_bank2_capacity_Object=MibScalar
simm3_bank2_capacity=_Simm3_bank2_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,6,2,2),_Simm3_bank2_capacity_Type())
simm3_bank2_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm3_bank2_capacity.setStatus(_A)
_Simm4_ObjectIdentity=ObjectIdentity
simm4=_Simm4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4))
class _Simm4_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm4_type_Type.__name__=_D
_Simm4_type_Object=MibScalar
simm4_type=_Simm4_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,4),_Simm4_type_Type())
simm4_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm4_type.setStatus(_A)
_Simm4_capacity_Type=Integer32
_Simm4_capacity_Object=MibScalar
simm4_capacity=_Simm4_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,5),_Simm4_capacity_Type())
simm4_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm4_capacity.setStatus(_A)
_Simm4_bank_ObjectIdentity=ObjectIdentity
simm4_bank=_Simm4_bank_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,6))
_Simm4_bank1_ObjectIdentity=ObjectIdentity
simm4_bank1=_Simm4_bank1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,6,1))
class _Simm4_bank1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm4_bank1_type_Type.__name__=_D
_Simm4_bank1_type_Object=MibScalar
simm4_bank1_type=_Simm4_bank1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,6,1,1),_Simm4_bank1_type_Type())
simm4_bank1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm4_bank1_type.setStatus(_A)
_Simm4_bank1_capacity_Type=Integer32
_Simm4_bank1_capacity_Object=MibScalar
simm4_bank1_capacity=_Simm4_bank1_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,6,1,2),_Simm4_bank1_capacity_Type())
simm4_bank1_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm4_bank1_capacity.setStatus(_A)
_Simm4_bank2_ObjectIdentity=ObjectIdentity
simm4_bank2=_Simm4_bank2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,6,2))
class _Simm4_bank2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm4_bank2_type_Type.__name__=_D
_Simm4_bank2_type_Object=MibScalar
simm4_bank2_type=_Simm4_bank2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,6,2,1),_Simm4_bank2_type_Type())
simm4_bank2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm4_bank2_type.setStatus(_A)
_Simm4_bank2_capacity_Type=Integer32
_Simm4_bank2_capacity_Object=MibScalar
simm4_bank2_capacity=_Simm4_bank2_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,6,2,2),_Simm4_bank2_capacity_Type())
simm4_bank2_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm4_bank2_capacity.setStatus(_A)
_Simm5_ObjectIdentity=ObjectIdentity
simm5=_Simm5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5))
class _Simm5_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm5_type_Type.__name__=_D
_Simm5_type_Object=MibScalar
simm5_type=_Simm5_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,4),_Simm5_type_Type())
simm5_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm5_type.setStatus(_A)
_Simm5_capacity_Type=Integer32
_Simm5_capacity_Object=MibScalar
simm5_capacity=_Simm5_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,5),_Simm5_capacity_Type())
simm5_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm5_capacity.setStatus(_A)
_Simm5_bank_ObjectIdentity=ObjectIdentity
simm5_bank=_Simm5_bank_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,6))
_Simm5_bank1_ObjectIdentity=ObjectIdentity
simm5_bank1=_Simm5_bank1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,6,1))
class _Simm5_bank1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm5_bank1_type_Type.__name__=_D
_Simm5_bank1_type_Object=MibScalar
simm5_bank1_type=_Simm5_bank1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,6,1,1),_Simm5_bank1_type_Type())
simm5_bank1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm5_bank1_type.setStatus(_A)
_Simm5_bank1_capacity_Type=Integer32
_Simm5_bank1_capacity_Object=MibScalar
simm5_bank1_capacity=_Simm5_bank1_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,6,1,2),_Simm5_bank1_capacity_Type())
simm5_bank1_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm5_bank1_capacity.setStatus(_A)
_Simm5_bank2_ObjectIdentity=ObjectIdentity
simm5_bank2=_Simm5_bank2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,6,2))
class _Simm5_bank2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,9)));namedValues=NamedValues(*((_G,1),(_I,2),(_H,3),(_J,4),(_K,5),(_L,7),(_M,9)))
_Simm5_bank2_type_Type.__name__=_D
_Simm5_bank2_type_Object=MibScalar
simm5_bank2_type=_Simm5_bank2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,6,2,1),_Simm5_bank2_type_Type())
simm5_bank2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm5_bank2_type.setStatus(_A)
_Simm5_bank2_capacity_Type=Integer32
_Simm5_bank2_capacity_Object=MibScalar
simm5_bank2_capacity=_Simm5_bank2_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,6,2,2),_Simm5_bank2_capacity_Type())
simm5_bank2_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm5_bank2_capacity.setStatus(_A)
_Mio_ObjectIdentity=ObjectIdentity
mio=_Mio_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3))
_Mio1_ObjectIdentity=ObjectIdentity
mio1=_Mio1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,1))
_Mio1_model_name_Type=OctetString
_Mio1_model_name_Object=MibScalar
mio1_model_name=_Mio1_model_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,1,2),_Mio1_model_name_Type())
mio1_model_name.setMaxAccess(_B)
if mibBuilder.loadTexts:mio1_model_name.setStatus(_A)
_Mio1_manufacturing_info_Type=OctetString
_Mio1_manufacturing_info_Object=MibScalar
mio1_manufacturing_info=_Mio1_manufacturing_info_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,1,3),_Mio1_manufacturing_info_Type())
mio1_manufacturing_info.setMaxAccess(_B)
if mibBuilder.loadTexts:mio1_manufacturing_info.setStatus(_A)
class _Mio1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,8,12)));namedValues=NamedValues(*((_G,1),(_I,2),('eDiskDrive',8),(_p,12)))
_Mio1_type_Type.__name__=_D
_Mio1_type_Object=MibScalar
mio1_type=_Mio1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,1,4),_Mio1_type_Type())
mio1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:mio1_type.setStatus(_A)
_Mio1_ip_address_Type=OctetString
_Mio1_ip_address_Object=MibScalar
mio1_ip_address=_Mio1_ip_address_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,1,6),_Mio1_ip_address_Type())
mio1_ip_address.setMaxAccess(_B)
if mibBuilder.loadTexts:mio1_ip_address.setStatus(_A)
_Mio4_ObjectIdentity=ObjectIdentity
mio4=_Mio4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,4))
_Mio4_model_name_Type=OctetString
_Mio4_model_name_Object=MibScalar
mio4_model_name=_Mio4_model_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,4,2),_Mio4_model_name_Type())
mio4_model_name.setMaxAccess(_B)
if mibBuilder.loadTexts:mio4_model_name.setStatus(_A)
_Mio4_manufacturing_info_Type=OctetString
_Mio4_manufacturing_info_Object=MibScalar
mio4_manufacturing_info=_Mio4_manufacturing_info_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,4,3),_Mio4_manufacturing_info_Type())
mio4_manufacturing_info.setMaxAccess(_B)
if mibBuilder.loadTexts:mio4_manufacturing_info.setStatus(_A)
class _Mio4_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,12)));namedValues=NamedValues(*((_G,1),(_p,12)))
_Mio4_type_Type.__name__=_D
_Mio4_type_Object=MibScalar
mio4_type=_Mio4_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,4,4),_Mio4_type_Type())
mio4_type.setMaxAccess(_B)
if mibBuilder.loadTexts:mio4_type.setStatus(_A)
_Mio4_ip_address_Type=OctetString
_Mio4_ip_address_Object=MibScalar
mio4_ip_address=_Mio4_ip_address_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,4,6),_Mio4_ip_address_Type())
mio4_ip_address.setMaxAccess(_B)
if mibBuilder.loadTexts:mio4_ip_address.setStatus(_A)
_Web_server_ObjectIdentity=ObjectIdentity
web_server=_Web_server_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,6))
_Settings_web_server_ObjectIdentity=ObjectIdentity
settings_web_server=_Settings_web_server_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,6,1))
class _Ews_request_control_panel_supplies_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_O,2)))
_Ews_request_control_panel_supplies_status_Type.__name__=_D
_Ews_request_control_panel_supplies_status_Object=MibScalar
ews_request_control_panel_supplies_status=_Ews_request_control_panel_supplies_status_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,6,1,5),_Ews_request_control_panel_supplies_status_Type())
ews_request_control_panel_supplies_status.setMaxAccess(_C)
if mibBuilder.loadTexts:ews_request_control_panel_supplies_status.setStatus(_A)
_Usb_interface_ObjectIdentity=ObjectIdentity
usb_interface=_Usb_interface_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9))
class _Usb_host_supported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_O,2)))
_Usb_host_supported_Type.__name__=_D
_Usb_host_supported_Object=MibScalar
usb_host_supported=_Usb_host_supported_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9,1),_Usb_host_supported_Type())
usb_host_supported.setMaxAccess(_B)
if mibBuilder.loadTexts:usb_host_supported.setStatus(_A)
_Usb_ObjectIdentity=ObjectIdentity
usb=_Usb_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9,2))
_Usb_serial_number_Type=OctetString
_Usb_serial_number_Object=MibScalar
usb_serial_number=_Usb_serial_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9,2,1),_Usb_serial_number_Type())
usb_serial_number.setMaxAccess(_B)
if mibBuilder.loadTexts:usb_serial_number.setStatus(_A)
_Usb_manufacturer_name_Type=OctetString
_Usb_manufacturer_name_Object=MibScalar
usb_manufacturer_name=_Usb_manufacturer_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9,2,2),_Usb_manufacturer_name_Type())
usb_manufacturer_name.setMaxAccess(_B)
if mibBuilder.loadTexts:usb_manufacturer_name.setStatus(_A)
_Usb_product_description_Type=OctetString
_Usb_product_description_Object=MibScalar
usb_product_description=_Usb_product_description_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9,2,3),_Usb_product_description_Type())
usb_product_description.setMaxAccess(_B)
if mibBuilder.loadTexts:usb_product_description.setStatus(_A)
_Usb_vendor_id_Type=Integer32
_Usb_vendor_id_Object=MibScalar
usb_vendor_id=_Usb_vendor_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9,2,4),_Usb_vendor_id_Type())
usb_vendor_id.setMaxAccess(_B)
if mibBuilder.loadTexts:usb_vendor_id.setStatus(_A)
_Usb_product_id_Type=Integer32
_Usb_product_id_Object=MibScalar
usb_product_id=_Usb_product_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9,2,5),_Usb_product_id_Type())
usb_product_id.setMaxAccess(_B)
if mibBuilder.loadTexts:usb_product_id.setStatus(_A)
class _Usb_device_kind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eUSBStorageDevice',1),('eUSBNonStorageDevice',2),('eUSBCompositeDevice',3),('eUSBUnsupportedDevice',4)))
_Usb_device_kind_Type.__name__=_D
_Usb_device_kind_Object=MibScalar
usb_device_kind=_Usb_device_kind_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9,2,6),_Usb_device_kind_Type())
usb_device_kind.setMaxAccess(_B)
if mibBuilder.loadTexts:usb_device_kind.setStatus(_A)
_Usb_driver_name_Type=OctetString
_Usb_driver_name_Object=MibScalar
usb_driver_name=_Usb_driver_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,9,2,7),_Usb_driver_name_Type())
usb_driver_name.setMaxAccess(_B)
if mibBuilder.loadTexts:usb_driver_name.setStatus(_A)
_Test_ObjectIdentity=ObjectIdentity
test=_Test_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5))
class _Print_internal_page_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,7,8,9,100,101,252,253,254,255,256,257,258,259,260,350,450,1406)));namedValues=NamedValues(*(('eNotPrintingAnInternalPage',1),('ePrintingAnUnknownInternalPage',2),('eDeviceDemoPage1ConfigurationPage',3),('eDeviceDemoPage2',4),('eDeviceDemoPage5ErrorLog',7),('eDeviceDemoPage6FileSystemDirectoryListing',8),('eDeviceDemoPage7MenuMap',9),('ePrintUsagePage',100),('eSuppliesPage',101),('eDeviceAutoCleaningPage',252),('eDeviceCleaningPage',253),('eDevicePaperPathTest',254),('eDevicePageRegistrationPage',255),('ePrintQualityPages',256),('eHighVoltageTestPage',257),('eColorPaletteRGBPage',258),('eColorPaletteCMYKPage',259),('eDevicePageDiagnosticsPage',260),('ePCLFontList1',350),('ePSFontList',450),('eDeviceShowMeHowPageHelpGuide',1406)))
_Print_internal_page_Type.__name__=_D
_Print_internal_page_Object=MibScalar
print_internal_page=_Print_internal_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,2),_Print_internal_page_Type())
print_internal_page.setMaxAccess(_C)
if mibBuilder.loadTexts:print_internal_page.setStatus(_A)
_Engine_self_diagnostic_Type=OctetString
_Engine_self_diagnostic_Object=MibScalar
engine_self_diagnostic=_Engine_self_diagnostic_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,7),_Engine_self_diagnostic_Type())
engine_self_diagnostic.setMaxAccess(_B)
if mibBuilder.loadTexts:engine_self_diagnostic.setStatus(_A)
_Engine_parameter_Type=OctetString
_Engine_parameter_Object=MibScalar
engine_parameter=_Engine_parameter_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,8),_Engine_parameter_Type())
engine_parameter.setMaxAccess(_B)
if mibBuilder.loadTexts:engine_parameter.setStatus(_A)
_Job_ObjectIdentity=ObjectIdentity
job=_Job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6))
_Settings_job_ObjectIdentity=ObjectIdentity
settings_job=_Settings_job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1))
class _Clearable_warning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_P,2),('eJob',3)))
_Clearable_warning_Type.__name__=_D
_Clearable_warning_Object=MibScalar
clearable_warning=_Clearable_warning_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,1),_Clearable_warning_Type())
clearable_warning.setMaxAccess(_C)
if mibBuilder.loadTexts:clearable_warning.setStatus(_A)
class _Cancel_job_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,32767))
_Cancel_job_Type.__name__=_D
_Cancel_job_Object=MibScalar
cancel_job=_Cancel_job_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,2),_Cancel_job_Type())
cancel_job.setMaxAccess(_F)
if mibBuilder.loadTexts:cancel_job.setStatus(_A)
class _Job_info_change_id_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Job_info_change_id_Type.__name__=_E
_Job_info_change_id_Object=MibScalar
job_info_change_id=_Job_info_change_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,3),_Job_info_change_id_Type())
job_info_change_id.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_change_id.setStatus(_A)
_Hold_job_timeout_Type=Integer32
_Hold_job_timeout_Object=MibScalar
hold_job_timeout=_Hold_job_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,10),_Hold_job_timeout_Type())
hold_job_timeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hold_job_timeout.setStatus(_A)
_Active_print_jobs_ObjectIdentity=ObjectIdentity
active_print_jobs=_Active_print_jobs_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,2))
_Job_being_parsed_ObjectIdentity=ObjectIdentity
job_being_parsed=_Job_being_parsed_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,2,1))
class _Current_job_parsing_id_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_Current_job_parsing_id_Type.__name__=_D
_Current_job_parsing_id_Object=MibScalar
current_job_parsing_id=_Current_job_parsing_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,2,1,1),_Current_job_parsing_id_Type())
current_job_parsing_id.setMaxAccess(_B)
if mibBuilder.loadTexts:current_job_parsing_id.setStatus(_A)
_Job_info_ObjectIdentity=ObjectIdentity
job_info=_Job_info_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5))
_Job_info_name1_Type=OctetString
_Job_info_name1_Object=MibScalar
job_info_name1=_Job_info_name1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,1),_Job_info_name1_Type())
job_info_name1.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_name1.setStatus(_A)
_Job_info_name2_Type=OctetString
_Job_info_name2_Object=MibScalar
job_info_name2=_Job_info_name2_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,2),_Job_info_name2_Type())
job_info_name2.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_name2.setStatus(_A)
_Job_info_stage_Type=OctetString
_Job_info_stage_Object=MibScalar
job_info_stage=_Job_info_stage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,10),_Job_info_stage_Type())
job_info_stage.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_stage.setStatus(_A)
_Job_info_io_source_Type=Integer32
_Job_info_io_source_Object=MibScalar
job_info_io_source=_Job_info_io_source_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,11),_Job_info_io_source_Type())
job_info_io_source.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_io_source.setStatus(_A)
_Job_info_pages_processed_Type=Integer32
_Job_info_pages_processed_Object=MibScalar
job_info_pages_processed=_Job_info_pages_processed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,12),_Job_info_pages_processed_Type())
job_info_pages_processed.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_pages_processed.setStatus(_A)
_Job_info_pages_printed_Type=Integer32
_Job_info_pages_printed_Object=MibScalar
job_info_pages_printed=_Job_info_pages_printed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,13),_Job_info_pages_printed_Type())
job_info_pages_printed.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_pages_printed.setStatus(_A)
_Job_info_size_Type=Integer32
_Job_info_size_Object=MibScalar
job_info_size=_Job_info_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,14),_Job_info_size_Type())
job_info_size.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_size.setStatus(_A)
class _Job_info_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,7,10,11,12,13)));namedValues=NamedValues(*(('eAborted',3),('eWaitingForResources',4),('ePrinted',5),('eTerminating',7),('eCancelled',10),('eProcessing',11),('eScanning',12),('eSending',13)))
_Job_info_state_Type.__name__=_D
_Job_info_state_Object=MibScalar
job_info_state=_Job_info_state_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,15),_Job_info_state_Type())
job_info_state.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_state.setStatus(_A)
class _Job_info_outcome_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues(('eOk',3))
_Job_info_outcome_Type.__name__=_D
_Job_info_outcome_Object=MibScalar
job_info_outcome=_Job_info_outcome_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,19),_Job_info_outcome_Type())
job_info_outcome.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_outcome.setStatus(_A)
_Job_info_outbins_used_Type=OctetString
_Job_info_outbins_used_Object=MibScalar
job_info_outbins_used=_Job_info_outbins_used_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,20),_Job_info_outbins_used_Type())
job_info_outbins_used.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_outbins_used.setStatus(_A)
_Job_info_physical_outbins_used_Type=OctetString
_Job_info_physical_outbins_used_Object=MibScalar
job_info_physical_outbins_used=_Job_info_physical_outbins_used_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,22),_Job_info_physical_outbins_used_Type())
job_info_physical_outbins_used.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_physical_outbins_used.setStatus(_A)
_Job_info_attribute_ObjectIdentity=ObjectIdentity
job_info_attribute=_Job_info_attribute_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23))
class _Job_info_attr_1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_1_Type.__name__=_E
_Job_info_attr_1_Object=MibScalar
job_info_attr_1=_Job_info_attr_1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,1),_Job_info_attr_1_Type())
job_info_attr_1.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_1.setStatus(_A)
class _Job_info_attr_2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_2_Type.__name__=_E
_Job_info_attr_2_Object=MibScalar
job_info_attr_2=_Job_info_attr_2_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,2),_Job_info_attr_2_Type())
job_info_attr_2.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_2.setStatus(_A)
class _Job_info_attr_3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_3_Type.__name__=_E
_Job_info_attr_3_Object=MibScalar
job_info_attr_3=_Job_info_attr_3_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,3),_Job_info_attr_3_Type())
job_info_attr_3.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_3.setStatus(_A)
class _Job_info_attr_4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_4_Type.__name__=_E
_Job_info_attr_4_Object=MibScalar
job_info_attr_4=_Job_info_attr_4_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,4),_Job_info_attr_4_Type())
job_info_attr_4.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_4.setStatus(_A)
class _Job_info_attr_5_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_5_Type.__name__=_E
_Job_info_attr_5_Object=MibScalar
job_info_attr_5=_Job_info_attr_5_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,5),_Job_info_attr_5_Type())
job_info_attr_5.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_5.setStatus(_A)
class _Job_info_attr_6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_6_Type.__name__=_E
_Job_info_attr_6_Object=MibScalar
job_info_attr_6=_Job_info_attr_6_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,6),_Job_info_attr_6_Type())
job_info_attr_6.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_6.setStatus(_A)
class _Job_info_attr_7_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_7_Type.__name__=_E
_Job_info_attr_7_Object=MibScalar
job_info_attr_7=_Job_info_attr_7_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,7),_Job_info_attr_7_Type())
job_info_attr_7.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_7.setStatus(_A)
class _Job_info_attr_8_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_8_Type.__name__=_E
_Job_info_attr_8_Object=MibScalar
job_info_attr_8=_Job_info_attr_8_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,8),_Job_info_attr_8_Type())
job_info_attr_8.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_8.setStatus(_A)
class _Job_info_attr_9_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_9_Type.__name__=_E
_Job_info_attr_9_Object=MibScalar
job_info_attr_9=_Job_info_attr_9_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,9),_Job_info_attr_9_Type())
job_info_attr_9.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_9.setStatus(_A)
class _Job_info_attr_10_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_10_Type.__name__=_E
_Job_info_attr_10_Object=MibScalar
job_info_attr_10=_Job_info_attr_10_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,10),_Job_info_attr_10_Type())
job_info_attr_10.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_10.setStatus(_A)
class _Job_info_attr_11_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_11_Type.__name__=_E
_Job_info_attr_11_Object=MibScalar
job_info_attr_11=_Job_info_attr_11_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,11),_Job_info_attr_11_Type())
job_info_attr_11.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_11.setStatus(_A)
class _Job_info_attr_12_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_12_Type.__name__=_E
_Job_info_attr_12_Object=MibScalar
job_info_attr_12=_Job_info_attr_12_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,12),_Job_info_attr_12_Type())
job_info_attr_12.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_12.setStatus(_A)
class _Job_info_attr_13_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_13_Type.__name__=_E
_Job_info_attr_13_Object=MibScalar
job_info_attr_13=_Job_info_attr_13_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,13),_Job_info_attr_13_Type())
job_info_attr_13.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_13.setStatus(_A)
class _Job_info_attr_14_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_14_Type.__name__=_E
_Job_info_attr_14_Object=MibScalar
job_info_attr_14=_Job_info_attr_14_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,14),_Job_info_attr_14_Type())
job_info_attr_14.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_14.setStatus(_A)
class _Job_info_attr_15_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_15_Type.__name__=_E
_Job_info_attr_15_Object=MibScalar
job_info_attr_15=_Job_info_attr_15_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,15),_Job_info_attr_15_Type())
job_info_attr_15.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_15.setStatus(_A)
class _Job_info_attr_16_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_16_Type.__name__=_E
_Job_info_attr_16_Object=MibScalar
job_info_attr_16=_Job_info_attr_16_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,16),_Job_info_attr_16_Type())
job_info_attr_16.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_16.setStatus(_A)
_Job_info_requested_originals_Type=Integer32
_Job_info_requested_originals_Object=MibScalar
job_info_requested_originals=_Job_info_requested_originals_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,24),_Job_info_requested_originals_Type())
job_info_requested_originals.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_requested_originals.setStatus(_A)
_Job_info_page_count_current_original_Type=Integer32
_Job_info_page_count_current_original_Object=MibScalar
job_info_page_count_current_original=_Job_info_page_count_current_original_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,25),_Job_info_page_count_current_original_Type())
job_info_page_count_current_original.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_page_count_current_original.setStatus(_A)
_Job_info_pages_in_original_Type=Integer32
_Job_info_pages_in_original_Object=MibScalar
job_info_pages_in_original=_Job_info_pages_in_original_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,26),_Job_info_pages_in_original_Type())
job_info_pages_in_original.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_pages_in_original.setStatus(_A)
_Job_info_printed_originals_Type=Integer32
_Job_info_printed_originals_Object=MibScalar
job_info_printed_originals=_Job_info_printed_originals_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,27),_Job_info_printed_originals_Type())
job_info_printed_originals.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_printed_originals.setStatus(_A)
_Job_info_accounting_ObjectIdentity=ObjectIdentity
job_info_accounting=_Job_info_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28))
class _Job_info_accounting_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,11,17,18,19,25,26,27,45,46,65,72,80,81,90,91,100,101,258,282,32767)));namedValues=NamedValues(*((_U,1),(_Q,2),(_V,3),(_q,11),(_W,17),(_X,18),(_r,19),(_Y,25),(_R,26),(_s,27),(_Z,45),(_t,46),(_u,65),(_v,72),(_b,80),(_c,81),(_d,90),(_e,91),(_f,100),(_a,101),(_w,258),(_x,282),(_i,32767)))
_Job_info_accounting_media_size_Type.__name__=_D
_Job_info_accounting_media_size_Object=MibScalar
job_info_accounting_media_size=_Job_info_accounting_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,1),_Job_info_accounting_media_size_Type())
job_info_accounting_media_size.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_media_size.setStatus(_A)
class _Job_info_accounting_media_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39)));namedValues=NamedValues(*(('eUnknownMedia',1),('eStandardType',2),('ePreprinted',3),('eLetterhead',4),('eTransparency',5),('ePrepunched',6),('eLabels',7),('eBond',8),('eRecycled',9),('eColored',10),('eCardStock',11),('eLight',12),('eIntermediate',13),('eHeavy',14),('eExtraHeavy',15),('eRough',16),('eGloss',17),('eHeavyGloss',18),('eEnvelope',19),('eGlossFilm',20),('eExtraHeavyGloss',21),('eCardGlossy',22),('eMidWeight',23),('eHpMatte90',24),('eHpMatte105',25),('eHpMatte120',26),('eHpSoftGloss120',27),('eHpGlossy120',28),('eHpMatte160',29),('eHpGlossy160',30),('eHpMatte200',31),('eHpMatte220',32),('eHpGlossy220',33),('eHpTough',34),('eUserType1',35),('eUserType2',36),('eUserType3',37),('eUserType4',38),('eUserType5',39)))
_Job_info_accounting_media_type_Type.__name__=_D
_Job_info_accounting_media_type_Object=MibScalar
job_info_accounting_media_type=_Job_info_accounting_media_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,2),_Job_info_accounting_media_type_Type())
job_info_accounting_media_type.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_media_type.setStatus(_A)
class _Job_info_accounting_finishing_options_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('eNoFinish',1),('eOffset',2),('ePunch',3),('eStapler',4),('eFinisher',5)))
_Job_info_accounting_finishing_options_Type.__name__=_D
_Job_info_accounting_finishing_options_Object=MibScalar
job_info_accounting_finishing_options=_Job_info_accounting_finishing_options_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,3),_Job_info_accounting_finishing_options_Type())
job_info_accounting_finishing_options.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_finishing_options.setStatus(_A)
_Job_info_accounting_media_simplex_count_Type=Integer32
_Job_info_accounting_media_simplex_count_Object=MibScalar
job_info_accounting_media_simplex_count=_Job_info_accounting_media_simplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,4),_Job_info_accounting_media_simplex_count_Type())
job_info_accounting_media_simplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_media_simplex_count.setStatus(_A)
_Job_info_accounting_media_duplex_count_Type=Integer32
_Job_info_accounting_media_duplex_count_Object=MibScalar
job_info_accounting_media_duplex_count=_Job_info_accounting_media_duplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,5),_Job_info_accounting_media_duplex_count_Type())
job_info_accounting_media_duplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_media_duplex_count.setStatus(_A)
_Job_info_accounting_grayscale_impression_count_Type=Integer32
_Job_info_accounting_grayscale_impression_count_Object=MibScalar
job_info_accounting_grayscale_impression_count=_Job_info_accounting_grayscale_impression_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,6),_Job_info_accounting_grayscale_impression_count_Type())
job_info_accounting_grayscale_impression_count.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_grayscale_impression_count.setStatus(_A)
_Job_info_accounting_color_impression_count_Type=Integer32
_Job_info_accounting_color_impression_count_Object=MibScalar
job_info_accounting_color_impression_count=_Job_info_accounting_color_impression_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,7),_Job_info_accounting_color_impression_count_Type())
job_info_accounting_color_impression_count.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_color_impression_count.setStatus(_A)
_Job_info_accounting_black_dots_Type=Integer32
_Job_info_accounting_black_dots_Object=MibScalar
job_info_accounting_black_dots=_Job_info_accounting_black_dots_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,8),_Job_info_accounting_black_dots_Type())
job_info_accounting_black_dots.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_black_dots.setStatus(_A)
_Job_info_accounting_yellow_dots_Type=Integer32
_Job_info_accounting_yellow_dots_Object=MibScalar
job_info_accounting_yellow_dots=_Job_info_accounting_yellow_dots_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,9),_Job_info_accounting_yellow_dots_Type())
job_info_accounting_yellow_dots.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_yellow_dots.setStatus(_A)
_Job_info_accounting_cyan_dots_Type=Integer32
_Job_info_accounting_cyan_dots_Object=MibScalar
job_info_accounting_cyan_dots=_Job_info_accounting_cyan_dots_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,10),_Job_info_accounting_cyan_dots_Type())
job_info_accounting_cyan_dots.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_cyan_dots.setStatus(_A)
_Job_info_accounting_magenta_dots_Type=Integer32
_Job_info_accounting_magenta_dots_Object=MibScalar
job_info_accounting_magenta_dots=_Job_info_accounting_magenta_dots_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,11),_Job_info_accounting_magenta_dots_Type())
job_info_accounting_magenta_dots.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_magenta_dots.setStatus(_A)
class _Job_info_accounting_job_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,1000)));namedValues=NamedValues(*(('ePrintJob',1),('eIPPJob',2),('eCopyJob',3),('eCopyInterruptJob',4),('eJetSendJob',5),('eInternalPage',6),('eCleaningPage',7),('eAutoCleaningPage',8),('eDigitalSendJob',9),('eWebPrintJob',10),('eFaxPrintJob',11),('eRetrievedJob',12),('ePhotoCardPrintJob',13),('eUnknownJob',1000)))
_Job_info_accounting_job_type_Type.__name__=_D
_Job_info_accounting_job_type_Object=MibScalar
job_info_accounting_job_type=_Job_info_accounting_job_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,14),_Job_info_accounting_job_type_Type())
job_info_accounting_job_type.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_accounting_job_type.setStatus(_A)
class _Job_info_accounting_color_usage_log_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eClear',1),('ePrint',2)))
_Job_info_accounting_color_usage_log_Type.__name__=_D
_Job_info_accounting_color_usage_log_Object=MibScalar
job_info_accounting_color_usage_log=_Job_info_accounting_color_usage_log_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,28,32),_Job_info_accounting_color_usage_log_Type())
job_info_accounting_color_usage_log.setMaxAccess(_F)
if mibBuilder.loadTexts:job_info_accounting_color_usage_log.setStatus(_A)
_Held_job_ObjectIdentity=ObjectIdentity
held_job=_Held_job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7))
_Held_job_info_ObjectIdentity=ObjectIdentity
held_job_info=_Held_job_info_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1))
class _Held_job_user_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Held_job_user_name_Type.__name__=_E
_Held_job_user_name_Object=MibScalar
held_job_user_name=_Held_job_user_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,1),_Held_job_user_name_Type())
held_job_user_name.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_user_name.setStatus(_A)
class _Held_job_job_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Held_job_job_name_Type.__name__=_E
_Held_job_job_name_Object=MibScalar
held_job_job_name=_Held_job_job_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,2),_Held_job_job_name_Type())
held_job_job_name.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_job_name.setStatus(_A)
class _Held_job_retention_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eHoldOff',1),('eHoldOn',2),('eHoldStore',3),('eHoldProof',4)))
_Held_job_retention_Type.__name__=_D
_Held_job_retention_Object=MibScalar
held_job_retention=_Held_job_retention_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,3),_Held_job_retention_Type())
held_job_retention.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_retention.setStatus(_A)
class _Held_job_security_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eHoldTypePublic',1),('eHoldTypePrivate',2)))
_Held_job_security_Type.__name__=_D
_Held_job_security_Object=MibScalar
held_job_security=_Held_job_security_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,4),_Held_job_security_Type())
held_job_security.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_security.setStatus(_A)
class _Held_job_quantity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_Held_job_quantity_Type.__name__=_D
_Held_job_quantity_Object=MibScalar
held_job_quantity=_Held_job_quantity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,5),_Held_job_quantity_Type())
held_job_quantity.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_quantity.setStatus(_A)
class _Held_job_pin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_Held_job_pin_Type.__name__=_E
_Held_job_pin_Object=MibScalar
held_job_pin=_Held_job_pin_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,6),_Held_job_pin_Type())
held_job_pin.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_pin.setStatus(_A)
_Held_job_control_ObjectIdentity=ObjectIdentity
held_job_control=_Held_job_control_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2))
class _Held_job_print_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_Held_job_print_Type.__name__=_E
_Held_job_print_Object=MibScalar
held_job_print=_Held_job_print_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2,1),_Held_job_print_Type())
held_job_print.setMaxAccess(_F)
if mibBuilder.loadTexts:held_job_print.setStatus(_A)
_Held_job_delete_Type=Integer32
_Held_job_delete_Object=MibScalar
held_job_delete=_Held_job_delete_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2,2),_Held_job_delete_Type())
held_job_delete.setMaxAccess(_F)
if mibBuilder.loadTexts:held_job_delete.setStatus(_A)
class _Held_job_set_queue_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Held_job_set_queue_size_Type.__name__=_D
_Held_job_set_queue_size_Object=MibScalar
held_job_set_queue_size=_Held_job_set_queue_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2,3),_Held_job_set_queue_size_Type())
held_job_set_queue_size.setMaxAccess(_C)
if mibBuilder.loadTexts:held_job_set_queue_size.setStatus(_A)
class _Held_job_enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_y,1),(_z,2)))
_Held_job_enable_Type.__name__=_D
_Held_job_enable_Object=MibScalar
held_job_enable=_Held_job_enable_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2,4),_Held_job_enable_Type())
held_job_enable.setMaxAccess(_C)
if mibBuilder.loadTexts:held_job_enable.setStatus(_A)
_File_system_ObjectIdentity=ObjectIdentity
file_system=_File_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10))
_Settings_file_system_ObjectIdentity=ObjectIdentity
settings_file_system=_Settings_file_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1))
_File_system_max_open_files_Type=Integer32
_File_system_max_open_files_Object=MibScalar
file_system_max_open_files=_File_system_max_open_files_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,2),_File_system_max_open_files_Type())
file_system_max_open_files.setMaxAccess(_B)
if mibBuilder.loadTexts:file_system_max_open_files.setStatus(_A)
_File_system_set_system_partition_writeable_Type=OctetString
_File_system_set_system_partition_writeable_Object=MibScalar
file_system_set_system_partition_writeable=_File_system_set_system_partition_writeable_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,6),_File_system_set_system_partition_writeable_Type())
file_system_set_system_partition_writeable.setMaxAccess(_F)
if mibBuilder.loadTexts:file_system_set_system_partition_writeable.setStatus(_A)
_File_system_set_system_partition_readonly_Type=Integer32
_File_system_set_system_partition_readonly_Object=MibScalar
file_system_set_system_partition_readonly=_File_system_set_system_partition_readonly_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,7),_File_system_set_system_partition_readonly_Type())
file_system_set_system_partition_readonly.setMaxAccess(_F)
if mibBuilder.loadTexts:file_system_set_system_partition_readonly.setStatus(_A)
_File_system_delete_files_Type=OctetString
_File_system_delete_files_Object=MibScalar
file_system_delete_files=_File_system_delete_files_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,8),_File_system_delete_files_Type())
file_system_delete_files.setMaxAccess(_F)
if mibBuilder.loadTexts:file_system_delete_files.setStatus(_A)
_File_system_external_access_capabilities_Type=OctetString
_File_system_external_access_capabilities_Object=MibScalar
file_system_external_access_capabilities=_File_system_external_access_capabilities_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,10),_File_system_external_access_capabilities_Type())
file_system_external_access_capabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:file_system_external_access_capabilities.setStatus(_A)
_File_system_erase_mode_Type=OctetString
_File_system_erase_mode_Object=MibScalar
file_system_erase_mode=_File_system_erase_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,11),_File_system_erase_mode_Type())
file_system_erase_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:file_system_erase_mode.setStatus(_A)
_File_system_wipe_disk_Type=Integer32
_File_system_wipe_disk_Object=MibScalar
file_system_wipe_disk=_File_system_wipe_disk_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,12),_File_system_wipe_disk_Type())
file_system_wipe_disk.setMaxAccess(_C)
if mibBuilder.loadTexts:file_system_wipe_disk.setStatus(_A)
_File_system_wipe_disk_status_Type=Integer32
_File_system_wipe_disk_status_Object=MibScalar
file_system_wipe_disk_status=_File_system_wipe_disk_status_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,13),_File_system_wipe_disk_status_Type())
file_system_wipe_disk_status.setMaxAccess(_B)
if mibBuilder.loadTexts:file_system_wipe_disk_status.setStatus(_A)
_File_systems_ObjectIdentity=ObjectIdentity
file_systems=_File_systems_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3))
_File_system2_ObjectIdentity=ObjectIdentity
file_system2=_File_system2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3,2))
class _File_system2_initialize_volume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_j,2))
_File_system2_initialize_volume_Type.__name__=_D
_File_system2_initialize_volume_Object=MibScalar
file_system2_initialize_volume=_File_system2_initialize_volume_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3,2,6),_File_system2_initialize_volume_Type())
file_system2_initialize_volume.setMaxAccess(_F)
if mibBuilder.loadTexts:file_system2_initialize_volume.setStatus(_A)
_File_system3_ObjectIdentity=ObjectIdentity
file_system3=_File_system3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3,3))
class _File_system3_initialize_volume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_j,2))
_File_system3_initialize_volume_Type.__name__=_D
_File_system3_initialize_volume_Object=MibScalar
file_system3_initialize_volume=_File_system3_initialize_volume_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3,3,6),_File_system3_initialize_volume_Type())
file_system3_initialize_volume.setMaxAccess(_F)
if mibBuilder.loadTexts:file_system3_initialize_volume.setStatus(_A)
_File_system4_ObjectIdentity=ObjectIdentity
file_system4=_File_system4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3,4))
class _File_system4_initialize_volume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_j,2))
_File_system4_initialize_volume_Type.__name__=_D
_File_system4_initialize_volume_Object=MibScalar
file_system4_initialize_volume=_File_system4_initialize_volume_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3,4,6),_File_system4_initialize_volume_Type())
file_system4_initialize_volume.setMaxAccess(_F)
if mibBuilder.loadTexts:file_system4_initialize_volume.setStatus(_A)
_Errorlog_ObjectIdentity=ObjectIdentity
errorlog=_Errorlog_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11))
_Error1_ObjectIdentity=ObjectIdentity
error1=_Error1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1))
_Error1_time_stamp_Type=Integer32
_Error1_time_stamp_Object=MibScalar
error1_time_stamp=_Error1_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1,1),_Error1_time_stamp_Type())
error1_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error1_time_stamp.setStatus(_A)
_Error1_code_Type=Integer32
_Error1_code_Object=MibScalar
error1_code=_Error1_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1,2),_Error1_code_Type())
error1_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error1_code.setStatus(_A)
_Error1_date_time_Type=OctetString
_Error1_date_time_Object=MibScalar
error1_date_time=_Error1_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1,3),_Error1_date_time_Type())
error1_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error1_date_time.setStatus(_A)
_Error2_ObjectIdentity=ObjectIdentity
error2=_Error2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2))
_Error2_time_stamp_Type=Integer32
_Error2_time_stamp_Object=MibScalar
error2_time_stamp=_Error2_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2,1),_Error2_time_stamp_Type())
error2_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error2_time_stamp.setStatus(_A)
_Error2_code_Type=Integer32
_Error2_code_Object=MibScalar
error2_code=_Error2_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2,2),_Error2_code_Type())
error2_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error2_code.setStatus(_A)
_Error2_date_time_Type=OctetString
_Error2_date_time_Object=MibScalar
error2_date_time=_Error2_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2,3),_Error2_date_time_Type())
error2_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error2_date_time.setStatus(_A)
_Error3_ObjectIdentity=ObjectIdentity
error3=_Error3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3))
_Error3_time_stamp_Type=Integer32
_Error3_time_stamp_Object=MibScalar
error3_time_stamp=_Error3_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3,1),_Error3_time_stamp_Type())
error3_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error3_time_stamp.setStatus(_A)
_Error3_code_Type=Integer32
_Error3_code_Object=MibScalar
error3_code=_Error3_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3,2),_Error3_code_Type())
error3_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error3_code.setStatus(_A)
_Error3_date_time_Type=OctetString
_Error3_date_time_Object=MibScalar
error3_date_time=_Error3_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3,3),_Error3_date_time_Type())
error3_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error3_date_time.setStatus(_A)
_Error4_ObjectIdentity=ObjectIdentity
error4=_Error4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4))
_Error4_time_stamp_Type=Integer32
_Error4_time_stamp_Object=MibScalar
error4_time_stamp=_Error4_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4,1),_Error4_time_stamp_Type())
error4_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error4_time_stamp.setStatus(_A)
_Error4_code_Type=Integer32
_Error4_code_Object=MibScalar
error4_code=_Error4_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4,2),_Error4_code_Type())
error4_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error4_code.setStatus(_A)
_Error4_date_time_Type=OctetString
_Error4_date_time_Object=MibScalar
error4_date_time=_Error4_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4,3),_Error4_date_time_Type())
error4_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error4_date_time.setStatus(_A)
_Error5_ObjectIdentity=ObjectIdentity
error5=_Error5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5))
_Error5_time_stamp_Type=Integer32
_Error5_time_stamp_Object=MibScalar
error5_time_stamp=_Error5_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5,1),_Error5_time_stamp_Type())
error5_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error5_time_stamp.setStatus(_A)
_Error5_code_Type=Integer32
_Error5_code_Object=MibScalar
error5_code=_Error5_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5,2),_Error5_code_Type())
error5_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error5_code.setStatus(_A)
_Error5_date_time_Type=OctetString
_Error5_date_time_Object=MibScalar
error5_date_time=_Error5_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5,3),_Error5_date_time_Type())
error5_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error5_date_time.setStatus(_A)
_Error6_ObjectIdentity=ObjectIdentity
error6=_Error6_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6))
_Error6_time_stamp_Type=Integer32
_Error6_time_stamp_Object=MibScalar
error6_time_stamp=_Error6_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6,1),_Error6_time_stamp_Type())
error6_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error6_time_stamp.setStatus(_A)
_Error6_code_Type=Integer32
_Error6_code_Object=MibScalar
error6_code=_Error6_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6,2),_Error6_code_Type())
error6_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error6_code.setStatus(_A)
_Error6_date_time_Type=OctetString
_Error6_date_time_Object=MibScalar
error6_date_time=_Error6_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6,3),_Error6_date_time_Type())
error6_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error6_date_time.setStatus(_A)
_Error7_ObjectIdentity=ObjectIdentity
error7=_Error7_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7))
_Error7_time_stamp_Type=Integer32
_Error7_time_stamp_Object=MibScalar
error7_time_stamp=_Error7_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7,1),_Error7_time_stamp_Type())
error7_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error7_time_stamp.setStatus(_A)
_Error7_code_Type=Integer32
_Error7_code_Object=MibScalar
error7_code=_Error7_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7,2),_Error7_code_Type())
error7_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error7_code.setStatus(_A)
_Error7_date_time_Type=OctetString
_Error7_date_time_Object=MibScalar
error7_date_time=_Error7_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7,3),_Error7_date_time_Type())
error7_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error7_date_time.setStatus(_A)
_Error8_ObjectIdentity=ObjectIdentity
error8=_Error8_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8))
_Error8_time_stamp_Type=Integer32
_Error8_time_stamp_Object=MibScalar
error8_time_stamp=_Error8_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8,1),_Error8_time_stamp_Type())
error8_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error8_time_stamp.setStatus(_A)
_Error8_code_Type=Integer32
_Error8_code_Object=MibScalar
error8_code=_Error8_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8,2),_Error8_code_Type())
error8_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error8_code.setStatus(_A)
_Error8_date_time_Type=OctetString
_Error8_date_time_Object=MibScalar
error8_date_time=_Error8_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8,3),_Error8_date_time_Type())
error8_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error8_date_time.setStatus(_A)
_Error9_ObjectIdentity=ObjectIdentity
error9=_Error9_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9))
_Error9_time_stamp_Type=Integer32
_Error9_time_stamp_Object=MibScalar
error9_time_stamp=_Error9_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9,1),_Error9_time_stamp_Type())
error9_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error9_time_stamp.setStatus(_A)
_Error9_code_Type=Integer32
_Error9_code_Object=MibScalar
error9_code=_Error9_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9,2),_Error9_code_Type())
error9_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error9_code.setStatus(_A)
_Error9_date_time_Type=OctetString
_Error9_date_time_Object=MibScalar
error9_date_time=_Error9_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9,3),_Error9_date_time_Type())
error9_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error9_date_time.setStatus(_A)
_Error10_ObjectIdentity=ObjectIdentity
error10=_Error10_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10))
_Error10_time_stamp_Type=Integer32
_Error10_time_stamp_Object=MibScalar
error10_time_stamp=_Error10_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10,1),_Error10_time_stamp_Type())
error10_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error10_time_stamp.setStatus(_A)
_Error10_code_Type=Integer32
_Error10_code_Object=MibScalar
error10_code=_Error10_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10,2),_Error10_code_Type())
error10_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error10_code.setStatus(_A)
_Error10_date_time_Type=OctetString
_Error10_date_time_Object=MibScalar
error10_date_time=_Error10_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10,3),_Error10_date_time_Type())
error10_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error10_date_time.setStatus(_A)
_Error11_ObjectIdentity=ObjectIdentity
error11=_Error11_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11))
_Error11_time_stamp_Type=Integer32
_Error11_time_stamp_Object=MibScalar
error11_time_stamp=_Error11_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11,1),_Error11_time_stamp_Type())
error11_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error11_time_stamp.setStatus(_A)
_Error11_code_Type=Integer32
_Error11_code_Object=MibScalar
error11_code=_Error11_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11,2),_Error11_code_Type())
error11_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error11_code.setStatus(_A)
_Error11_date_time_Type=OctetString
_Error11_date_time_Object=MibScalar
error11_date_time=_Error11_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11,3),_Error11_date_time_Type())
error11_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error11_date_time.setStatus(_A)
_Error12_ObjectIdentity=ObjectIdentity
error12=_Error12_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12))
_Error12_time_stamp_Type=Integer32
_Error12_time_stamp_Object=MibScalar
error12_time_stamp=_Error12_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12,1),_Error12_time_stamp_Type())
error12_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error12_time_stamp.setStatus(_A)
_Error12_code_Type=Integer32
_Error12_code_Object=MibScalar
error12_code=_Error12_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12,2),_Error12_code_Type())
error12_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error12_code.setStatus(_A)
_Error12_date_time_Type=OctetString
_Error12_date_time_Object=MibScalar
error12_date_time=_Error12_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12,3),_Error12_date_time_Type())
error12_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error12_date_time.setStatus(_A)
_Error13_ObjectIdentity=ObjectIdentity
error13=_Error13_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13))
_Error13_time_stamp_Type=Integer32
_Error13_time_stamp_Object=MibScalar
error13_time_stamp=_Error13_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13,1),_Error13_time_stamp_Type())
error13_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error13_time_stamp.setStatus(_A)
_Error13_code_Type=Integer32
_Error13_code_Object=MibScalar
error13_code=_Error13_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13,2),_Error13_code_Type())
error13_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error13_code.setStatus(_A)
_Error13_date_time_Type=OctetString
_Error13_date_time_Object=MibScalar
error13_date_time=_Error13_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13,3),_Error13_date_time_Type())
error13_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error13_date_time.setStatus(_A)
_Error14_ObjectIdentity=ObjectIdentity
error14=_Error14_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14))
_Error14_time_stamp_Type=Integer32
_Error14_time_stamp_Object=MibScalar
error14_time_stamp=_Error14_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14,1),_Error14_time_stamp_Type())
error14_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error14_time_stamp.setStatus(_A)
_Error14_code_Type=Integer32
_Error14_code_Object=MibScalar
error14_code=_Error14_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14,2),_Error14_code_Type())
error14_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error14_code.setStatus(_A)
_Error14_date_time_Type=OctetString
_Error14_date_time_Object=MibScalar
error14_date_time=_Error14_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14,3),_Error14_date_time_Type())
error14_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error14_date_time.setStatus(_A)
_Error15_ObjectIdentity=ObjectIdentity
error15=_Error15_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15))
_Error15_time_stamp_Type=Integer32
_Error15_time_stamp_Object=MibScalar
error15_time_stamp=_Error15_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15,1),_Error15_time_stamp_Type())
error15_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error15_time_stamp.setStatus(_A)
_Error15_code_Type=Integer32
_Error15_code_Object=MibScalar
error15_code=_Error15_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15,2),_Error15_code_Type())
error15_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error15_code.setStatus(_A)
_Error15_date_time_Type=OctetString
_Error15_date_time_Object=MibScalar
error15_date_time=_Error15_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15,3),_Error15_date_time_Type())
error15_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error15_date_time.setStatus(_A)
_Error16_ObjectIdentity=ObjectIdentity
error16=_Error16_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,16))
_Error16_time_stamp_Type=Integer32
_Error16_time_stamp_Object=MibScalar
error16_time_stamp=_Error16_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,16,1),_Error16_time_stamp_Type())
error16_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error16_time_stamp.setStatus(_A)
_Error16_code_Type=Integer32
_Error16_code_Object=MibScalar
error16_code=_Error16_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,16,2),_Error16_code_Type())
error16_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error16_code.setStatus(_A)
_Error16_date_time_Type=OctetString
_Error16_date_time_Object=MibScalar
error16_date_time=_Error16_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,16,3),_Error16_date_time_Type())
error16_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error16_date_time.setStatus(_A)
_Error17_ObjectIdentity=ObjectIdentity
error17=_Error17_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,17))
_Error17_time_stamp_Type=Integer32
_Error17_time_stamp_Object=MibScalar
error17_time_stamp=_Error17_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,17,1),_Error17_time_stamp_Type())
error17_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error17_time_stamp.setStatus(_A)
_Error17_code_Type=Integer32
_Error17_code_Object=MibScalar
error17_code=_Error17_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,17,2),_Error17_code_Type())
error17_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error17_code.setStatus(_A)
_Error17_date_time_Type=OctetString
_Error17_date_time_Object=MibScalar
error17_date_time=_Error17_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,17,3),_Error17_date_time_Type())
error17_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error17_date_time.setStatus(_A)
_Error18_ObjectIdentity=ObjectIdentity
error18=_Error18_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,18))
_Error18_time_stamp_Type=Integer32
_Error18_time_stamp_Object=MibScalar
error18_time_stamp=_Error18_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,18,1),_Error18_time_stamp_Type())
error18_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error18_time_stamp.setStatus(_A)
_Error18_code_Type=Integer32
_Error18_code_Object=MibScalar
error18_code=_Error18_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,18,2),_Error18_code_Type())
error18_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error18_code.setStatus(_A)
_Error18_date_time_Type=OctetString
_Error18_date_time_Object=MibScalar
error18_date_time=_Error18_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,18,3),_Error18_date_time_Type())
error18_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error18_date_time.setStatus(_A)
_Error19_ObjectIdentity=ObjectIdentity
error19=_Error19_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,19))
_Error19_time_stamp_Type=Integer32
_Error19_time_stamp_Object=MibScalar
error19_time_stamp=_Error19_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,19,1),_Error19_time_stamp_Type())
error19_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error19_time_stamp.setStatus(_A)
_Error19_code_Type=Integer32
_Error19_code_Object=MibScalar
error19_code=_Error19_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,19,2),_Error19_code_Type())
error19_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error19_code.setStatus(_A)
_Error19_date_time_Type=OctetString
_Error19_date_time_Object=MibScalar
error19_date_time=_Error19_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,19,3),_Error19_date_time_Type())
error19_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error19_date_time.setStatus(_A)
_Error20_ObjectIdentity=ObjectIdentity
error20=_Error20_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,20))
_Error20_time_stamp_Type=Integer32
_Error20_time_stamp_Object=MibScalar
error20_time_stamp=_Error20_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,20,1),_Error20_time_stamp_Type())
error20_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error20_time_stamp.setStatus(_A)
_Error20_code_Type=Integer32
_Error20_code_Object=MibScalar
error20_code=_Error20_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,20,2),_Error20_code_Type())
error20_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error20_code.setStatus(_A)
_Error20_date_time_Type=OctetString
_Error20_date_time_Object=MibScalar
error20_date_time=_Error20_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,20,3),_Error20_date_time_Type())
error20_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error20_date_time.setStatus(_A)
_Error21_ObjectIdentity=ObjectIdentity
error21=_Error21_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,21))
_Error21_time_stamp_Type=Integer32
_Error21_time_stamp_Object=MibScalar
error21_time_stamp=_Error21_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,21,1),_Error21_time_stamp_Type())
error21_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error21_time_stamp.setStatus(_A)
_Error21_code_Type=Integer32
_Error21_code_Object=MibScalar
error21_code=_Error21_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,21,2),_Error21_code_Type())
error21_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error21_code.setStatus(_A)
_Error21_date_time_Type=OctetString
_Error21_date_time_Object=MibScalar
error21_date_time=_Error21_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,21,3),_Error21_date_time_Type())
error21_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error21_date_time.setStatus(_A)
_Error22_ObjectIdentity=ObjectIdentity
error22=_Error22_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,22))
_Error22_time_stamp_Type=Integer32
_Error22_time_stamp_Object=MibScalar
error22_time_stamp=_Error22_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,22,1),_Error22_time_stamp_Type())
error22_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error22_time_stamp.setStatus(_A)
_Error22_code_Type=Integer32
_Error22_code_Object=MibScalar
error22_code=_Error22_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,22,2),_Error22_code_Type())
error22_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error22_code.setStatus(_A)
_Error22_date_time_Type=OctetString
_Error22_date_time_Object=MibScalar
error22_date_time=_Error22_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,22,3),_Error22_date_time_Type())
error22_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error22_date_time.setStatus(_A)
_Error23_ObjectIdentity=ObjectIdentity
error23=_Error23_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,23))
_Error23_time_stamp_Type=Integer32
_Error23_time_stamp_Object=MibScalar
error23_time_stamp=_Error23_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,23,1),_Error23_time_stamp_Type())
error23_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error23_time_stamp.setStatus(_A)
_Error23_code_Type=Integer32
_Error23_code_Object=MibScalar
error23_code=_Error23_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,23,2),_Error23_code_Type())
error23_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error23_code.setStatus(_A)
_Error23_date_time_Type=OctetString
_Error23_date_time_Object=MibScalar
error23_date_time=_Error23_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,23,3),_Error23_date_time_Type())
error23_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error23_date_time.setStatus(_A)
_Error24_ObjectIdentity=ObjectIdentity
error24=_Error24_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,24))
_Error24_time_stamp_Type=Integer32
_Error24_time_stamp_Object=MibScalar
error24_time_stamp=_Error24_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,24,1),_Error24_time_stamp_Type())
error24_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error24_time_stamp.setStatus(_A)
_Error24_code_Type=Integer32
_Error24_code_Object=MibScalar
error24_code=_Error24_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,24,2),_Error24_code_Type())
error24_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error24_code.setStatus(_A)
_Error24_date_time_Type=OctetString
_Error24_date_time_Object=MibScalar
error24_date_time=_Error24_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,24,3),_Error24_date_time_Type())
error24_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error24_date_time.setStatus(_A)
_Error25_ObjectIdentity=ObjectIdentity
error25=_Error25_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,25))
_Error25_time_stamp_Type=Integer32
_Error25_time_stamp_Object=MibScalar
error25_time_stamp=_Error25_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,25,1),_Error25_time_stamp_Type())
error25_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error25_time_stamp.setStatus(_A)
_Error25_code_Type=Integer32
_Error25_code_Object=MibScalar
error25_code=_Error25_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,25,2),_Error25_code_Type())
error25_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error25_code.setStatus(_A)
_Error25_date_time_Type=OctetString
_Error25_date_time_Object=MibScalar
error25_date_time=_Error25_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,25,3),_Error25_date_time_Type())
error25_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error25_date_time.setStatus(_A)
_Error26_ObjectIdentity=ObjectIdentity
error26=_Error26_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,26))
_Error26_time_stamp_Type=Integer32
_Error26_time_stamp_Object=MibScalar
error26_time_stamp=_Error26_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,26,1),_Error26_time_stamp_Type())
error26_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error26_time_stamp.setStatus(_A)
_Error26_code_Type=Integer32
_Error26_code_Object=MibScalar
error26_code=_Error26_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,26,2),_Error26_code_Type())
error26_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error26_code.setStatus(_A)
_Error26_date_time_Type=OctetString
_Error26_date_time_Object=MibScalar
error26_date_time=_Error26_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,26,3),_Error26_date_time_Type())
error26_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error26_date_time.setStatus(_A)
_Error27_ObjectIdentity=ObjectIdentity
error27=_Error27_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,27))
_Error27_time_stamp_Type=Integer32
_Error27_time_stamp_Object=MibScalar
error27_time_stamp=_Error27_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,27,1),_Error27_time_stamp_Type())
error27_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error27_time_stamp.setStatus(_A)
_Error27_code_Type=Integer32
_Error27_code_Object=MibScalar
error27_code=_Error27_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,27,2),_Error27_code_Type())
error27_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error27_code.setStatus(_A)
_Error27_date_time_Type=OctetString
_Error27_date_time_Object=MibScalar
error27_date_time=_Error27_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,27,3),_Error27_date_time_Type())
error27_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error27_date_time.setStatus(_A)
_Error28_ObjectIdentity=ObjectIdentity
error28=_Error28_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,28))
_Error28_time_stamp_Type=Integer32
_Error28_time_stamp_Object=MibScalar
error28_time_stamp=_Error28_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,28,1),_Error28_time_stamp_Type())
error28_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error28_time_stamp.setStatus(_A)
_Error28_code_Type=Integer32
_Error28_code_Object=MibScalar
error28_code=_Error28_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,28,2),_Error28_code_Type())
error28_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error28_code.setStatus(_A)
_Error28_date_time_Type=OctetString
_Error28_date_time_Object=MibScalar
error28_date_time=_Error28_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,28,3),_Error28_date_time_Type())
error28_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error28_date_time.setStatus(_A)
_Error29_ObjectIdentity=ObjectIdentity
error29=_Error29_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,29))
_Error29_time_stamp_Type=Integer32
_Error29_time_stamp_Object=MibScalar
error29_time_stamp=_Error29_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,29,1),_Error29_time_stamp_Type())
error29_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error29_time_stamp.setStatus(_A)
_Error29_code_Type=Integer32
_Error29_code_Object=MibScalar
error29_code=_Error29_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,29,2),_Error29_code_Type())
error29_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error29_code.setStatus(_A)
_Error29_date_time_Type=OctetString
_Error29_date_time_Object=MibScalar
error29_date_time=_Error29_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,29,3),_Error29_date_time_Type())
error29_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error29_date_time.setStatus(_A)
_Error30_ObjectIdentity=ObjectIdentity
error30=_Error30_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,30))
_Error30_time_stamp_Type=Integer32
_Error30_time_stamp_Object=MibScalar
error30_time_stamp=_Error30_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,30,1),_Error30_time_stamp_Type())
error30_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error30_time_stamp.setStatus(_A)
_Error30_code_Type=Integer32
_Error30_code_Object=MibScalar
error30_code=_Error30_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,30,2),_Error30_code_Type())
error30_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error30_code.setStatus(_A)
_Error30_date_time_Type=OctetString
_Error30_date_time_Object=MibScalar
error30_date_time=_Error30_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,30,3),_Error30_date_time_Type())
error30_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error30_date_time.setStatus(_A)
_Error31_ObjectIdentity=ObjectIdentity
error31=_Error31_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,31))
_Error31_time_stamp_Type=Integer32
_Error31_time_stamp_Object=MibScalar
error31_time_stamp=_Error31_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,31,1),_Error31_time_stamp_Type())
error31_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error31_time_stamp.setStatus(_A)
_Error31_code_Type=Integer32
_Error31_code_Object=MibScalar
error31_code=_Error31_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,31,2),_Error31_code_Type())
error31_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error31_code.setStatus(_A)
_Error31_date_time_Type=OctetString
_Error31_date_time_Object=MibScalar
error31_date_time=_Error31_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,31,3),_Error31_date_time_Type())
error31_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error31_date_time.setStatus(_A)
_Error32_ObjectIdentity=ObjectIdentity
error32=_Error32_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,32))
_Error32_time_stamp_Type=Integer32
_Error32_time_stamp_Object=MibScalar
error32_time_stamp=_Error32_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,32,1),_Error32_time_stamp_Type())
error32_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error32_time_stamp.setStatus(_A)
_Error32_code_Type=Integer32
_Error32_code_Object=MibScalar
error32_code=_Error32_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,32,2),_Error32_code_Type())
error32_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error32_code.setStatus(_A)
_Error32_date_time_Type=OctetString
_Error32_date_time_Object=MibScalar
error32_date_time=_Error32_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,32,3),_Error32_date_time_Type())
error32_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error32_date_time.setStatus(_A)
_Error33_ObjectIdentity=ObjectIdentity
error33=_Error33_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,33))
_Error33_time_stamp_Type=Integer32
_Error33_time_stamp_Object=MibScalar
error33_time_stamp=_Error33_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,33,1),_Error33_time_stamp_Type())
error33_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error33_time_stamp.setStatus(_A)
_Error33_code_Type=Integer32
_Error33_code_Object=MibScalar
error33_code=_Error33_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,33,2),_Error33_code_Type())
error33_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error33_code.setStatus(_A)
_Error33_date_time_Type=OctetString
_Error33_date_time_Object=MibScalar
error33_date_time=_Error33_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,33,3),_Error33_date_time_Type())
error33_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error33_date_time.setStatus(_A)
_Error34_ObjectIdentity=ObjectIdentity
error34=_Error34_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,34))
_Error34_time_stamp_Type=Integer32
_Error34_time_stamp_Object=MibScalar
error34_time_stamp=_Error34_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,34,1),_Error34_time_stamp_Type())
error34_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error34_time_stamp.setStatus(_A)
_Error34_code_Type=Integer32
_Error34_code_Object=MibScalar
error34_code=_Error34_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,34,2),_Error34_code_Type())
error34_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error34_code.setStatus(_A)
_Error34_date_time_Type=OctetString
_Error34_date_time_Object=MibScalar
error34_date_time=_Error34_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,34,3),_Error34_date_time_Type())
error34_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error34_date_time.setStatus(_A)
_Error35_ObjectIdentity=ObjectIdentity
error35=_Error35_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,35))
_Error35_time_stamp_Type=Integer32
_Error35_time_stamp_Object=MibScalar
error35_time_stamp=_Error35_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,35,1),_Error35_time_stamp_Type())
error35_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error35_time_stamp.setStatus(_A)
_Error35_code_Type=Integer32
_Error35_code_Object=MibScalar
error35_code=_Error35_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,35,2),_Error35_code_Type())
error35_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error35_code.setStatus(_A)
_Error35_date_time_Type=OctetString
_Error35_date_time_Object=MibScalar
error35_date_time=_Error35_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,35,3),_Error35_date_time_Type())
error35_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error35_date_time.setStatus(_A)
_Error36_ObjectIdentity=ObjectIdentity
error36=_Error36_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,36))
_Error36_time_stamp_Type=Integer32
_Error36_time_stamp_Object=MibScalar
error36_time_stamp=_Error36_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,36,1),_Error36_time_stamp_Type())
error36_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error36_time_stamp.setStatus(_A)
_Error36_code_Type=Integer32
_Error36_code_Object=MibScalar
error36_code=_Error36_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,36,2),_Error36_code_Type())
error36_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error36_code.setStatus(_A)
_Error36_date_time_Type=OctetString
_Error36_date_time_Object=MibScalar
error36_date_time=_Error36_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,36,3),_Error36_date_time_Type())
error36_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error36_date_time.setStatus(_A)
_Error37_ObjectIdentity=ObjectIdentity
error37=_Error37_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,37))
_Error37_time_stamp_Type=Integer32
_Error37_time_stamp_Object=MibScalar
error37_time_stamp=_Error37_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,37,1),_Error37_time_stamp_Type())
error37_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error37_time_stamp.setStatus(_A)
_Error37_code_Type=Integer32
_Error37_code_Object=MibScalar
error37_code=_Error37_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,37,2),_Error37_code_Type())
error37_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error37_code.setStatus(_A)
_Error37_date_time_Type=OctetString
_Error37_date_time_Object=MibScalar
error37_date_time=_Error37_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,37,3),_Error37_date_time_Type())
error37_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error37_date_time.setStatus(_A)
_Error38_ObjectIdentity=ObjectIdentity
error38=_Error38_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,38))
_Error38_time_stamp_Type=Integer32
_Error38_time_stamp_Object=MibScalar
error38_time_stamp=_Error38_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,38,1),_Error38_time_stamp_Type())
error38_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error38_time_stamp.setStatus(_A)
_Error38_code_Type=Integer32
_Error38_code_Object=MibScalar
error38_code=_Error38_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,38,2),_Error38_code_Type())
error38_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error38_code.setStatus(_A)
_Error38_date_time_Type=OctetString
_Error38_date_time_Object=MibScalar
error38_date_time=_Error38_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,38,3),_Error38_date_time_Type())
error38_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error38_date_time.setStatus(_A)
_Error39_ObjectIdentity=ObjectIdentity
error39=_Error39_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,39))
_Error39_time_stamp_Type=Integer32
_Error39_time_stamp_Object=MibScalar
error39_time_stamp=_Error39_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,39,1),_Error39_time_stamp_Type())
error39_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error39_time_stamp.setStatus(_A)
_Error39_code_Type=Integer32
_Error39_code_Object=MibScalar
error39_code=_Error39_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,39,2),_Error39_code_Type())
error39_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error39_code.setStatus(_A)
_Error39_date_time_Type=OctetString
_Error39_date_time_Object=MibScalar
error39_date_time=_Error39_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,39,3),_Error39_date_time_Type())
error39_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error39_date_time.setStatus(_A)
_Error40_ObjectIdentity=ObjectIdentity
error40=_Error40_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,40))
_Error40_time_stamp_Type=Integer32
_Error40_time_stamp_Object=MibScalar
error40_time_stamp=_Error40_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,40,1),_Error40_time_stamp_Type())
error40_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error40_time_stamp.setStatus(_A)
_Error40_code_Type=Integer32
_Error40_code_Object=MibScalar
error40_code=_Error40_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,40,2),_Error40_code_Type())
error40_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error40_code.setStatus(_A)
_Error40_date_time_Type=OctetString
_Error40_date_time_Object=MibScalar
error40_date_time=_Error40_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,40,3),_Error40_date_time_Type())
error40_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error40_date_time.setStatus(_A)
_Error41_ObjectIdentity=ObjectIdentity
error41=_Error41_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,41))
_Error41_time_stamp_Type=Integer32
_Error41_time_stamp_Object=MibScalar
error41_time_stamp=_Error41_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,41,1),_Error41_time_stamp_Type())
error41_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error41_time_stamp.setStatus(_A)
_Error41_code_Type=Integer32
_Error41_code_Object=MibScalar
error41_code=_Error41_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,41,2),_Error41_code_Type())
error41_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error41_code.setStatus(_A)
_Error41_date_time_Type=OctetString
_Error41_date_time_Object=MibScalar
error41_date_time=_Error41_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,41,3),_Error41_date_time_Type())
error41_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error41_date_time.setStatus(_A)
_Error42_ObjectIdentity=ObjectIdentity
error42=_Error42_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,42))
_Error42_time_stamp_Type=Integer32
_Error42_time_stamp_Object=MibScalar
error42_time_stamp=_Error42_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,42,1),_Error42_time_stamp_Type())
error42_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error42_time_stamp.setStatus(_A)
_Error42_code_Type=Integer32
_Error42_code_Object=MibScalar
error42_code=_Error42_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,42,2),_Error42_code_Type())
error42_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error42_code.setStatus(_A)
_Error42_date_time_Type=OctetString
_Error42_date_time_Object=MibScalar
error42_date_time=_Error42_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,42,3),_Error42_date_time_Type())
error42_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error42_date_time.setStatus(_A)
_Error43_ObjectIdentity=ObjectIdentity
error43=_Error43_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,43))
_Error43_time_stamp_Type=Integer32
_Error43_time_stamp_Object=MibScalar
error43_time_stamp=_Error43_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,43,1),_Error43_time_stamp_Type())
error43_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error43_time_stamp.setStatus(_A)
_Error43_code_Type=Integer32
_Error43_code_Object=MibScalar
error43_code=_Error43_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,43,2),_Error43_code_Type())
error43_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error43_code.setStatus(_A)
_Error43_date_time_Type=OctetString
_Error43_date_time_Object=MibScalar
error43_date_time=_Error43_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,43,3),_Error43_date_time_Type())
error43_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error43_date_time.setStatus(_A)
_Error44_ObjectIdentity=ObjectIdentity
error44=_Error44_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,44))
_Error44_time_stamp_Type=Integer32
_Error44_time_stamp_Object=MibScalar
error44_time_stamp=_Error44_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,44,1),_Error44_time_stamp_Type())
error44_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error44_time_stamp.setStatus(_A)
_Error44_code_Type=Integer32
_Error44_code_Object=MibScalar
error44_code=_Error44_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,44,2),_Error44_code_Type())
error44_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error44_code.setStatus(_A)
_Error44_date_time_Type=OctetString
_Error44_date_time_Object=MibScalar
error44_date_time=_Error44_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,44,3),_Error44_date_time_Type())
error44_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error44_date_time.setStatus(_A)
_Error45_ObjectIdentity=ObjectIdentity
error45=_Error45_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,45))
_Error45_time_stamp_Type=Integer32
_Error45_time_stamp_Object=MibScalar
error45_time_stamp=_Error45_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,45,1),_Error45_time_stamp_Type())
error45_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error45_time_stamp.setStatus(_A)
_Error45_code_Type=Integer32
_Error45_code_Object=MibScalar
error45_code=_Error45_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,45,2),_Error45_code_Type())
error45_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error45_code.setStatus(_A)
_Error45_date_time_Type=OctetString
_Error45_date_time_Object=MibScalar
error45_date_time=_Error45_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,45,3),_Error45_date_time_Type())
error45_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error45_date_time.setStatus(_A)
_Error46_ObjectIdentity=ObjectIdentity
error46=_Error46_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,46))
_Error46_time_stamp_Type=Integer32
_Error46_time_stamp_Object=MibScalar
error46_time_stamp=_Error46_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,46,1),_Error46_time_stamp_Type())
error46_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error46_time_stamp.setStatus(_A)
_Error46_code_Type=Integer32
_Error46_code_Object=MibScalar
error46_code=_Error46_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,46,2),_Error46_code_Type())
error46_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error46_code.setStatus(_A)
_Error46_date_time_Type=OctetString
_Error46_date_time_Object=MibScalar
error46_date_time=_Error46_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,46,3),_Error46_date_time_Type())
error46_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error46_date_time.setStatus(_A)
_Error47_ObjectIdentity=ObjectIdentity
error47=_Error47_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,47))
_Error47_time_stamp_Type=Integer32
_Error47_time_stamp_Object=MibScalar
error47_time_stamp=_Error47_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,47,1),_Error47_time_stamp_Type())
error47_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error47_time_stamp.setStatus(_A)
_Error47_code_Type=Integer32
_Error47_code_Object=MibScalar
error47_code=_Error47_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,47,2),_Error47_code_Type())
error47_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error47_code.setStatus(_A)
_Error47_date_time_Type=OctetString
_Error47_date_time_Object=MibScalar
error47_date_time=_Error47_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,47,3),_Error47_date_time_Type())
error47_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error47_date_time.setStatus(_A)
_Error48_ObjectIdentity=ObjectIdentity
error48=_Error48_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,48))
_Error48_time_stamp_Type=Integer32
_Error48_time_stamp_Object=MibScalar
error48_time_stamp=_Error48_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,48,1),_Error48_time_stamp_Type())
error48_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error48_time_stamp.setStatus(_A)
_Error48_code_Type=Integer32
_Error48_code_Object=MibScalar
error48_code=_Error48_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,48,2),_Error48_code_Type())
error48_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error48_code.setStatus(_A)
_Error48_date_time_Type=OctetString
_Error48_date_time_Object=MibScalar
error48_date_time=_Error48_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,48,3),_Error48_date_time_Type())
error48_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error48_date_time.setStatus(_A)
_Error49_ObjectIdentity=ObjectIdentity
error49=_Error49_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,49))
_Error49_time_stamp_Type=Integer32
_Error49_time_stamp_Object=MibScalar
error49_time_stamp=_Error49_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,49,1),_Error49_time_stamp_Type())
error49_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error49_time_stamp.setStatus(_A)
_Error49_code_Type=Integer32
_Error49_code_Object=MibScalar
error49_code=_Error49_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,49,2),_Error49_code_Type())
error49_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error49_code.setStatus(_A)
_Error49_date_time_Type=OctetString
_Error49_date_time_Object=MibScalar
error49_date_time=_Error49_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,49,3),_Error49_date_time_Type())
error49_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error49_date_time.setStatus(_A)
_Error50_ObjectIdentity=ObjectIdentity
error50=_Error50_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,50))
_Error50_time_stamp_Type=Integer32
_Error50_time_stamp_Object=MibScalar
error50_time_stamp=_Error50_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,50,1),_Error50_time_stamp_Type())
error50_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error50_time_stamp.setStatus(_A)
_Error50_code_Type=Integer32
_Error50_code_Object=MibScalar
error50_code=_Error50_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,50,2),_Error50_code_Type())
error50_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error50_code.setStatus(_A)
_Error50_date_time_Type=OctetString
_Error50_date_time_Object=MibScalar
error50_date_time=_Error50_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,50,3),_Error50_date_time_Type())
error50_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error50_date_time.setStatus(_A)
_Resource_manager_ObjectIdentity=ObjectIdentity
resource_manager=_Resource_manager_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,12))
_Mass_storage_resources_ObjectIdentity=ObjectIdentity
mass_storage_resources=_Mass_storage_resources_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,12,3))
_Mass_storage_resource_change_counter_Type=Integer32
_Mass_storage_resource_change_counter_Object=MibScalar
mass_storage_resource_change_counter=_Mass_storage_resource_change_counter_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,12,3,1),_Mass_storage_resource_change_counter_Type())
mass_storage_resource_change_counter.setMaxAccess(_B)
if mibBuilder.loadTexts:mass_storage_resource_change_counter.setStatus(_A)
class _Mass_storage_resource_changed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_O,2))
_Mass_storage_resource_changed_Type.__name__=_D
_Mass_storage_resource_changed_Object=MibScalar
mass_storage_resource_changed=_Mass_storage_resource_changed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,12,3,2),_Mass_storage_resource_changed_Type())
mass_storage_resource_changed.setMaxAccess(_F)
if mibBuilder.loadTexts:mass_storage_resource_changed.setStatus(_A)
_Remote_procedure_call_ObjectIdentity=ObjectIdentity
remote_procedure_call=_Remote_procedure_call_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13))
_Settings_rpc_ObjectIdentity=ObjectIdentity
settings_rpc=_Settings_rpc_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,1))
_Rpc_bind_protocol_address_Type=OctetString
_Rpc_bind_protocol_address_Object=MibScalar
rpc_bind_protocol_address=_Rpc_bind_protocol_address_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,1,2),_Rpc_bind_protocol_address_Type())
rpc_bind_protocol_address.setMaxAccess(_B)
if mibBuilder.loadTexts:rpc_bind_protocol_address.setStatus(_A)
_Status_rpc_ObjectIdentity=ObjectIdentity
status_rpc=_Status_rpc_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,2))
_Rpc_bound_protocol_address_Type=OctetString
_Rpc_bound_protocol_address_Object=MibScalar
rpc_bound_protocol_address=_Rpc_bound_protocol_address_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,2,3),_Rpc_bound_protocol_address_Type())
rpc_bound_protocol_address.setMaxAccess(_B)
if mibBuilder.loadTexts:rpc_bound_protocol_address.setStatus(_A)
_Mass_storage_block_driver_ObjectIdentity=ObjectIdentity
mass_storage_block_driver=_Mass_storage_block_driver_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,15))
_Settings_mass_storage_bd_ObjectIdentity=ObjectIdentity
settings_mass_storage_bd=_Settings_mass_storage_bd_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,15,1))
class _Ram_disk_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_N,1),(_h,3)))
_Ram_disk_mode_Type.__name__=_D
_Ram_disk_mode_Object=MibScalar
ram_disk_mode=_Ram_disk_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,15,1,1),_Ram_disk_mode_Type())
ram_disk_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:ram_disk_mode.setStatus(_A)
_Ram_disk_size_Type=Integer32
_Ram_disk_size_Object=MibScalar
ram_disk_size=_Ram_disk_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,15,1,2),_Ram_disk_size_Type())
ram_disk_size.setMaxAccess(_B)
if mibBuilder.loadTexts:ram_disk_size.setStatus(_A)
_Status_mass_storage_bd_ObjectIdentity=ObjectIdentity
status_mass_storage_bd=_Status_mass_storage_bd_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,15,2))
_Maximum_ram_disk_memory_Type=Integer32
_Maximum_ram_disk_memory_Object=MibScalar
maximum_ram_disk_memory=_Maximum_ram_disk_memory_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,15,2,1),_Maximum_ram_disk_memory_Type())
maximum_ram_disk_memory.setMaxAccess(_B)
if mibBuilder.loadTexts:maximum_ram_disk_memory.setStatus(_A)
_Accounting_ObjectIdentity=ObjectIdentity
accounting=_Accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16))
_Printer_accounting_ObjectIdentity=ObjectIdentity
printer_accounting=_Printer_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1))
_Printed_media_usage_ObjectIdentity=ObjectIdentity
printed_media_usage=_Printed_media_usage_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1))
class _Printed_media_simplex_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,930576247))
_Printed_media_simplex_count_Type.__name__=_D
_Printed_media_simplex_count_Object=MibScalar
printed_media_simplex_count=_Printed_media_simplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,1),_Printed_media_simplex_count_Type())
printed_media_simplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_simplex_count.setStatus(_A)
_Printed_media_simplex_charge_Type=OctetString
_Printed_media_simplex_charge_Object=MibScalar
printed_media_simplex_charge=_Printed_media_simplex_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,2),_Printed_media_simplex_charge_Type())
printed_media_simplex_charge.setMaxAccess(_C)
if mibBuilder.loadTexts:printed_media_simplex_charge.setStatus(_A)
class _Printed_media_duplex_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,930576247))
_Printed_media_duplex_count_Type.__name__=_D
_Printed_media_duplex_count_Object=MibScalar
printed_media_duplex_count=_Printed_media_duplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,3),_Printed_media_duplex_count_Type())
printed_media_duplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_duplex_count.setStatus(_A)
_Printed_media_duplex_charge_Type=OctetString
_Printed_media_duplex_charge_Object=MibScalar
printed_media_duplex_charge=_Printed_media_duplex_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,4),_Printed_media_duplex_charge_Type())
printed_media_duplex_charge.setMaxAccess(_C)
if mibBuilder.loadTexts:printed_media_duplex_charge.setStatus(_A)
_Printed_media_total_charge_Type=OctetString
_Printed_media_total_charge_Object=MibScalar
printed_media_total_charge=_Printed_media_total_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,5),_Printed_media_total_charge_Type())
printed_media_total_charge.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_total_charge.setStatus(_A)
_Printed_media_maximum_pixels_per_page_Type=Integer32
_Printed_media_maximum_pixels_per_page_Object=MibScalar
printed_media_maximum_pixels_per_page=_Printed_media_maximum_pixels_per_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,6),_Printed_media_maximum_pixels_per_page_Type())
printed_media_maximum_pixels_per_page.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_maximum_pixels_per_page.setStatus(_A)
_Printed_media_combined_total_Type=OctetString
_Printed_media_combined_total_Object=MibScalar
printed_media_combined_total=_Printed_media_combined_total_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,7),_Printed_media_combined_total_Type())
printed_media_combined_total.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_combined_total.setStatus(_A)
class _Printed_media_dimplex_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,930576247))
_Printed_media_dimplex_count_Type.__name__=_D
_Printed_media_dimplex_count_Object=MibScalar
printed_media_dimplex_count=_Printed_media_dimplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,10),_Printed_media_dimplex_count_Type())
printed_media_dimplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_dimplex_count.setStatus(_A)
_Usage_printer_total_charge_Type=OctetString
_Usage_printer_total_charge_Object=MibScalar
usage_printer_total_charge=_Usage_printer_total_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,2),_Usage_printer_total_charge_Type())
usage_printer_total_charge.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_printer_total_charge.setStatus(_A)
_Usage_average_toner_coverage_Type=OctetString
_Usage_average_toner_coverage_Object=MibScalar
usage_average_toner_coverage=_Usage_average_toner_coverage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,3),_Usage_average_toner_coverage_Type())
usage_average_toner_coverage.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_average_toner_coverage.setStatus(_A)
class _Usage_staple_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,930576247))
_Usage_staple_count_Type.__name__=_D
_Usage_staple_count_Object=MibScalar
usage_staple_count=_Usage_staple_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,4),_Usage_staple_count_Type())
usage_staple_count.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_staple_count.setStatus(_A)
class _Usage_instructions_line1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Usage_instructions_line1_Type.__name__=_E
_Usage_instructions_line1_Object=MibScalar
usage_instructions_line1=_Usage_instructions_line1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,5),_Usage_instructions_line1_Type())
usage_instructions_line1.setMaxAccess(_C)
if mibBuilder.loadTexts:usage_instructions_line1.setStatus(_A)
class _Usage_instructions_line2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Usage_instructions_line2_Type.__name__=_E
_Usage_instructions_line2_Object=MibScalar
usage_instructions_line2=_Usage_instructions_line2_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,6),_Usage_instructions_line2_Type())
usage_instructions_line2.setMaxAccess(_C)
if mibBuilder.loadTexts:usage_instructions_line2.setStatus(_A)
class _Usage_instructions_line3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Usage_instructions_line3_Type.__name__=_E
_Usage_instructions_line3_Object=MibScalar
usage_instructions_line3=_Usage_instructions_line3_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,7),_Usage_instructions_line3_Type())
usage_instructions_line3.setMaxAccess(_C)
if mibBuilder.loadTexts:usage_instructions_line3.setStatus(_A)
class _Usage_instructions_line4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Usage_instructions_line4_Type.__name__=_E
_Usage_instructions_line4_Object=MibScalar
usage_instructions_line4=_Usage_instructions_line4_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,8),_Usage_instructions_line4_Type())
usage_instructions_line4.setMaxAccess(_C)
if mibBuilder.loadTexts:usage_instructions_line4.setStatus(_A)
_Printed_modes_usage_total_Type=Integer32
_Printed_modes_usage_total_Object=MibScalar
printed_modes_usage_total=_Printed_modes_usage_total_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,9),_Printed_modes_usage_total_Type())
printed_modes_usage_total.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_modes_usage_total.setStatus(_A)
_Source_tray_usage_total_Type=Integer32
_Source_tray_usage_total_Object=MibScalar
source_tray_usage_total=_Source_tray_usage_total_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,10),_Source_tray_usage_total_Type())
source_tray_usage_total.setMaxAccess(_B)
if mibBuilder.loadTexts:source_tray_usage_total.setStatus(_A)
_Destination_bin_usage_total_Type=Integer32
_Destination_bin_usage_total_Object=MibScalar
destination_bin_usage_total=_Destination_bin_usage_total_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,11),_Destination_bin_usage_total_Type())
destination_bin_usage_total.setMaxAccess(_B)
if mibBuilder.loadTexts:destination_bin_usage_total.setStatus(_A)
_Usage_printer_mono_total_charge_Type=OctetString
_Usage_printer_mono_total_charge_Object=MibScalar
usage_printer_mono_total_charge=_Usage_printer_mono_total_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,12),_Usage_printer_mono_total_charge_Type())
usage_printer_mono_total_charge.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_printer_mono_total_charge.setStatus(_A)
_Usage_printer_color_total_charge_Type=OctetString
_Usage_printer_color_total_charge_Object=MibScalar
usage_printer_color_total_charge=_Usage_printer_color_total_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,13),_Usage_printer_color_total_charge_Type())
usage_printer_color_total_charge.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_printer_color_total_charge.setStatus(_A)
_Printer_color_accounting_ObjectIdentity=ObjectIdentity
printer_color_accounting=_Printer_color_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3))
_Printed_media_color_usage_ObjectIdentity=ObjectIdentity
printed_media_color_usage=_Printed_media_color_usage_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1))
_Printed_media_color_simplex_count_Type=Integer32
_Printed_media_color_simplex_count_Object=MibScalar
printed_media_color_simplex_count=_Printed_media_color_simplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1,1),_Printed_media_color_simplex_count_Type())
printed_media_color_simplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_color_simplex_count.setStatus(_A)
_Printed_media_color_duplex_count_Type=Integer32
_Printed_media_color_duplex_count_Object=MibScalar
printed_media_color_duplex_count=_Printed_media_color_duplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1,3),_Printed_media_color_duplex_count_Type())
printed_media_color_duplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_color_duplex_count.setStatus(_A)
_Printed_media_color_total_count_Type=OctetString
_Printed_media_color_total_count_Object=MibScalar
printed_media_color_total_count=_Printed_media_color_total_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1,5),_Printed_media_color_total_count_Type())
printed_media_color_total_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_color_total_count.setStatus(_A)
_Printed_media_color_dimplex_count_Type=Integer32
_Printed_media_color_dimplex_count_Object=MibScalar
printed_media_color_dimplex_count=_Printed_media_color_dimplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1,6),_Printed_media_color_dimplex_count_Type())
printed_media_color_dimplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_color_dimplex_count.setStatus(_A)
_Printed_modes_accounting_ObjectIdentity=ObjectIdentity
printed_modes_accounting=_Printed_modes_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,4))
_Printed_modes_usage_ObjectIdentity=ObjectIdentity
printed_modes_usage=_Printed_modes_usage_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,4,1))
_Printed_modes_mono_count_Type=Integer32
_Printed_modes_mono_count_Object=MibScalar
printed_modes_mono_count=_Printed_modes_mono_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,4,1,1),_Printed_modes_mono_count_Type())
printed_modes_mono_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_modes_mono_count.setStatus(_A)
_Printed_modes_color_count_Type=Integer32
_Printed_modes_color_count_Object=MibScalar
printed_modes_color_count=_Printed_modes_color_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,4,1,3),_Printed_modes_color_count_Type())
printed_modes_color_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_modes_color_count.setStatus(_A)
_Printed_modes_total_count_Type=Integer32
_Printed_modes_total_count_Object=MibScalar
printed_modes_total_count=_Printed_modes_total_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,4,1,5),_Printed_modes_total_count_Type())
printed_modes_total_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_modes_total_count.setStatus(_A)
_Source_tray_accounting_ObjectIdentity=ObjectIdentity
source_tray_accounting=_Source_tray_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,5))
_Source_tray_usage_ObjectIdentity=ObjectIdentity
source_tray_usage=_Source_tray_usage_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,5,1))
_Source_tray_usage_count_Type=Integer32
_Source_tray_usage_count_Object=MibScalar
source_tray_usage_count=_Source_tray_usage_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,5,1,1),_Source_tray_usage_count_Type())
source_tray_usage_count.setMaxAccess(_B)
if mibBuilder.loadTexts:source_tray_usage_count.setStatus(_A)
_Destination_bin_accounting_ObjectIdentity=ObjectIdentity
destination_bin_accounting=_Destination_bin_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,6))
_Destination_bin_usage_ObjectIdentity=ObjectIdentity
destination_bin_usage=_Destination_bin_usage_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,6,1))
_Destination_bin_usage_count_Type=Integer32
_Destination_bin_usage_count_Object=MibScalar
destination_bin_usage_count=_Destination_bin_usage_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,6,1,1),_Destination_bin_usage_count_Type())
destination_bin_usage_count.setMaxAccess(_B)
if mibBuilder.loadTexts:destination_bin_usage_count.setStatus(_A)
_Firmware_download_ObjectIdentity=ObjectIdentity
firmware_download=_Firmware_download_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,18))
class _Firmware_download_write_status_supported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_O,2)))
_Firmware_download_write_status_supported_Type.__name__=_D
_Firmware_download_write_status_supported_Object=MibScalar
firmware_download_write_status_supported=_Firmware_download_write_status_supported_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,18,1),_Firmware_download_write_status_supported_Type())
firmware_download_write_status_supported.setMaxAccess(_B)
if mibBuilder.loadTexts:firmware_download_write_status_supported.setStatus(_A)
_Firmware_download_write_time_Type=Integer32
_Firmware_download_write_time_Object=MibScalar
firmware_download_write_time=_Firmware_download_write_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,18,2),_Firmware_download_write_time_Type())
firmware_download_write_time.setMaxAccess(_B)
if mibBuilder.loadTexts:firmware_download_write_time.setStatus(_A)
class _Firmware_download_current_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('eIdle',1),('eReceivingImage',2),(_A0,3),('eVerifyingImage',4),(_A1,5),(_A2,6),(_A3,7),('eDownloadComplete',8),('eOKtoShutDown',9),('eCancelDownload',10),('eShuttingDown',11)))
_Firmware_download_current_state_Type.__name__=_D
_Firmware_download_current_state_Object=MibScalar
firmware_download_current_state=_Firmware_download_current_state_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,18,4),_Firmware_download_current_state_Type())
firmware_download_current_state.setMaxAccess(_B)
if mibBuilder.loadTexts:firmware_download_current_state.setStatus(_A)
_Firmware_download_name_Type=OctetString
_Firmware_download_name_Object=MibScalar
firmware_download_name=_Firmware_download_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,18,6),_Firmware_download_name_Type())
firmware_download_name.setMaxAccess(_B)
if mibBuilder.loadTexts:firmware_download_name.setStatus(_T)
_Firmware_download_version_Type=OctetString
_Firmware_download_version_Object=MibScalar
firmware_download_version=_Firmware_download_version_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,18,7),_Firmware_download_version_Type())
firmware_download_version.setMaxAccess(_B)
if mibBuilder.loadTexts:firmware_download_version.setStatus(_T)
_Operating_system_ObjectIdentity=ObjectIdentity
operating_system=_Operating_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,19))
_Os_execute_file_Type=OctetString
_Os_execute_file_Object=MibScalar
os_execute_file=_Os_execute_file_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,19,1),_Os_execute_file_Type())
os_execute_file.setMaxAccess(_F)
if mibBuilder.loadTexts:os_execute_file.setStatus(_A)
_Upgradable_devices_ObjectIdentity=ObjectIdentity
upgradable_devices=_Upgradable_devices_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,20))
class _Upgradable_devices_write_status_supported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_O,2)))
_Upgradable_devices_write_status_supported_Type.__name__=_D
_Upgradable_devices_write_status_supported_Object=MibScalar
upgradable_devices_write_status_supported=_Upgradable_devices_write_status_supported_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,20,1),_Upgradable_devices_write_status_supported_Type())
upgradable_devices_write_status_supported.setMaxAccess(_B)
if mibBuilder.loadTexts:upgradable_devices_write_status_supported.setStatus(_A)
_Upgradable_devices_write_time_Type=Integer32
_Upgradable_devices_write_time_Object=MibScalar
upgradable_devices_write_time=_Upgradable_devices_write_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,20,2),_Upgradable_devices_write_time_Type())
upgradable_devices_write_time.setMaxAccess(_B)
if mibBuilder.loadTexts:upgradable_devices_write_time.setStatus(_A)
class _Upgradable_devices_current_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('eIdle',1),('eReceivedImage',2),(_A0,3),('eVerifiedImage',4),(_A1,5),(_A2,6),(_A3,7),('eUpgradeComplete',8),('eUpgradeSkipped',9)))
_Upgradable_devices_current_state_Type.__name__=_D
_Upgradable_devices_current_state_Object=MibScalar
upgradable_devices_current_state=_Upgradable_devices_current_state_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,20,4),_Upgradable_devices_current_state_Type())
upgradable_devices_current_state.setMaxAccess(_B)
if mibBuilder.loadTexts:upgradable_devices_current_state.setStatus(_A)
_Upgradable_devices_name_Type=OctetString
_Upgradable_devices_name_Object=MibScalar
upgradable_devices_name=_Upgradable_devices_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,20,6),_Upgradable_devices_name_Type())
upgradable_devices_name.setMaxAccess(_B)
if mibBuilder.loadTexts:upgradable_devices_name.setStatus(_T)
_Upgradable_devices_version_Type=OctetString
_Upgradable_devices_version_Object=MibScalar
upgradable_devices_version=_Upgradable_devices_version_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,20,7),_Upgradable_devices_version_Type())
upgradable_devices_version.setMaxAccess(_B)
if mibBuilder.loadTexts:upgradable_devices_version.setStatus(_T)
class _Remote_upgrade_enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_P,2)))
_Remote_upgrade_enable_Type.__name__=_D
_Remote_upgrade_enable_Object=MibScalar
remote_upgrade_enable=_Remote_upgrade_enable_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,20,8),_Remote_upgrade_enable_Type())
remote_upgrade_enable.setMaxAccess(_C)
if mibBuilder.loadTexts:remote_upgrade_enable.setStatus(_T)
_Source_subsystem_ObjectIdentity=ObjectIdentity
source_subsystem=_Source_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2))
_Io_ObjectIdentity=ObjectIdentity
io=_Io_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1))
_Settings_io_ObjectIdentity=ObjectIdentity
settings_io=_Settings_io_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1))
class _Io_timeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_Io_timeout_Type.__name__=_D
_Io_timeout_Object=MibScalar
io_timeout=_Io_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,1),_Io_timeout_Type())
io_timeout.setMaxAccess(_C)
if mibBuilder.loadTexts:io_timeout.setStatus(_A)
class _Io_switch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eYes',1))
_Io_switch_Type.__name__=_D
_Io_switch_Object=MibScalar
io_switch=_Io_switch_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,2),_Io_switch_Type())
io_switch.setMaxAccess(_B)
if mibBuilder.loadTexts:io_switch.setStatus(_A)
_Ports_ObjectIdentity=ObjectIdentity
ports=_Ports_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3))
_Port1_ObjectIdentity=ObjectIdentity
port1=_Port1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3,1))
class _Port1_parallel_speed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eSlow',1),('eFast',2)))
_Port1_parallel_speed_Type.__name__=_D
_Port1_parallel_speed_Object=MibScalar
port1_parallel_speed=_Port1_parallel_speed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3,1,4),_Port1_parallel_speed_Type())
port1_parallel_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:port1_parallel_speed.setStatus(_A)
class _Port1_parallel_bidirectionality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eUnidirectional',1),('eBidirectional',2)))
_Port1_parallel_bidirectionality_Type.__name__=_D
_Port1_parallel_bidirectionality_Object=MibScalar
port1_parallel_bidirectionality=_Port1_parallel_bidirectionality_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3,1,5),_Port1_parallel_bidirectionality_Type())
port1_parallel_bidirectionality.setMaxAccess(_C)
if mibBuilder.loadTexts:port1_parallel_bidirectionality.setStatus(_A)
_Spooler_ObjectIdentity=ObjectIdentity
spooler=_Spooler_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,4))
_Settings_spooler_ObjectIdentity=ObjectIdentity
settings_spooler=_Settings_spooler_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,4,1))
class _Mopy_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5)));namedValues=NamedValues(*((_N,1),('eStandard',4),('eEnhanced',5)))
_Mopy_mode_Type.__name__=_D
_Mopy_mode_Object=MibScalar
mopy_mode=_Mopy_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,4,1,1),_Mopy_mode_Type())
mopy_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:mopy_mode.setStatus(_A)
_Processing_subsystem_ObjectIdentity=ObjectIdentity
processing_subsystem=_Processing_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3))
_Pdl_ObjectIdentity=ObjectIdentity
pdl=_Pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3))
_Settings_pdl_ObjectIdentity=ObjectIdentity
settings_pdl=_Settings_pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1))
_Default_copies_Type=Integer32
_Default_copies_Object=MibScalar
default_copies=_Default_copies_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,4),_Default_copies_Type())
default_copies.setMaxAccess(_C)
if mibBuilder.loadTexts:default_copies.setStatus(_A)
class _Form_feed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_o,1))
_Form_feed_Type.__name__=_D
_Form_feed_Object=MibScalar
form_feed=_Form_feed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,5),_Form_feed_Type())
form_feed.setMaxAccess(_F)
if mibBuilder.loadTexts:form_feed.setStatus(_A)
_Default_vertical_black_resolution_Type=Integer32
_Default_vertical_black_resolution_Object=MibScalar
default_vertical_black_resolution=_Default_vertical_black_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,8),_Default_vertical_black_resolution_Type())
default_vertical_black_resolution.setMaxAccess(_C)
if mibBuilder.loadTexts:default_vertical_black_resolution.setStatus(_A)
_Default_horizontal_black_resolution_Type=Integer32
_Default_horizontal_black_resolution_Object=MibScalar
default_horizontal_black_resolution=_Default_horizontal_black_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,9),_Default_horizontal_black_resolution_Type())
default_horizontal_black_resolution.setMaxAccess(_C)
if mibBuilder.loadTexts:default_horizontal_black_resolution.setStatus(_A)
class _Default_page_protect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_P,2))
_Default_page_protect_Type.__name__=_D
_Default_page_protect_Object=MibScalar
default_page_protect=_Default_page_protect_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,10),_Default_page_protect_Type())
default_page_protect.setMaxAccess(_C)
if mibBuilder.loadTexts:default_page_protect.setStatus(_A)
_Default_lines_per_page_Type=Integer32
_Default_lines_per_page_Object=MibScalar
default_lines_per_page=_Default_lines_per_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,11),_Default_lines_per_page_Type())
default_lines_per_page.setMaxAccess(_C)
if mibBuilder.loadTexts:default_lines_per_page.setStatus(_A)
_Default_vmi_Type=Integer32
_Default_vmi_Object=MibScalar
default_vmi=_Default_vmi_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,12),_Default_vmi_Type())
default_vmi.setMaxAccess(_C)
if mibBuilder.loadTexts:default_vmi.setStatus(_A)
class _Default_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,15,17,18,25,26,45,72,80,81,90,91,100,101,32767)));namedValues=NamedValues(*((_U,1),(_Q,2),(_V,3),(_g,10),(_A4,15),(_W,17),(_X,18),(_Y,25),(_R,26),(_Z,45),(_A5,72),(_b,80),(_c,81),(_d,90),(_e,91),(_f,100),(_a,101),(_i,32767)))
_Default_media_size_Type.__name__=_D
_Default_media_size_Object=MibScalar
default_media_size=_Default_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,13),_Default_media_size_Type())
default_media_size.setMaxAccess(_C)
if mibBuilder.loadTexts:default_media_size.setStatus(_A)
class _Cold_reset_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,26)));namedValues=NamedValues(*((_Q,2),(_R,26)))
_Cold_reset_media_size_Type.__name__=_D
_Cold_reset_media_size_Object=MibScalar
cold_reset_media_size=_Cold_reset_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,19),_Cold_reset_media_size_Type())
cold_reset_media_size.setMaxAccess(_C)
if mibBuilder.loadTexts:cold_reset_media_size.setStatus(_A)
_Default_media_name_Type=OctetString
_Default_media_name_Object=MibScalar
default_media_name=_Default_media_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,22),_Default_media_name_Type())
default_media_name.setMaxAccess(_C)
if mibBuilder.loadTexts:default_media_name.setStatus(_A)
class _Reprint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_P,2),(_h,3)))
_Reprint_Type.__name__=_D
_Reprint_Object=MibScalar
reprint=_Reprint_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,36),_Reprint_Type())
reprint.setMaxAccess(_C)
if mibBuilder.loadTexts:reprint.setStatus(_A)
_Default_bits_per_pixel_Type=Integer32
_Default_bits_per_pixel_Object=MibScalar
default_bits_per_pixel=_Default_bits_per_pixel_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,39),_Default_bits_per_pixel_Type())
default_bits_per_pixel.setMaxAccess(_C)
if mibBuilder.loadTexts:default_bits_per_pixel.setStatus(_A)
_Status_pdl_ObjectIdentity=ObjectIdentity
status_pdl=_Status_pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,2))
class _Form_feed_needed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_O,2)))
_Form_feed_needed_Type.__name__=_D
_Form_feed_needed_Object=MibScalar
form_feed_needed=_Form_feed_needed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,2,2),_Form_feed_needed_Type())
form_feed_needed.setMaxAccess(_B)
if mibBuilder.loadTexts:form_feed_needed.setStatus(_A)
_Pdl_pcl_ObjectIdentity=ObjectIdentity
pdl_pcl=_Pdl_pcl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3))
_Pcl_total_page_count_Type=Integer32
_Pcl_total_page_count_Object=MibScalar
pcl_total_page_count=_Pcl_total_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,5),_Pcl_total_page_count_Type())
pcl_total_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:pcl_total_page_count.setStatus(_A)
_Pcl_default_font_height_Type=Integer32
_Pcl_default_font_height_Object=MibScalar
pcl_default_font_height=_Pcl_default_font_height_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,13),_Pcl_default_font_height_Type())
pcl_default_font_height.setMaxAccess(_C)
if mibBuilder.loadTexts:pcl_default_font_height.setStatus(_A)
class _Pcl_default_font_source_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,11,12,13,14)));namedValues=NamedValues(*(('eInternal',1),('ePermanentSoft',2),('eRomSimm2',11),('eRomSimm3',12),('eRomSimm4',13),('eRomSimm5',14)))
_Pcl_default_font_source_Type.__name__=_D
_Pcl_default_font_source_Object=MibScalar
pcl_default_font_source=_Pcl_default_font_source_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,14),_Pcl_default_font_source_Type())
pcl_default_font_source.setMaxAccess(_C)
if mibBuilder.loadTexts:pcl_default_font_source.setStatus(_A)
class _Pcl_default_font_number_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Pcl_default_font_number_Type.__name__=_D
_Pcl_default_font_number_Object=MibScalar
pcl_default_font_number=_Pcl_default_font_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,15),_Pcl_default_font_number_Type())
pcl_default_font_number.setMaxAccess(_C)
if mibBuilder.loadTexts:pcl_default_font_number.setStatus(_A)
_Pcl_default_font_width_Type=Integer32
_Pcl_default_font_width_Object=MibScalar
pcl_default_font_width=_Pcl_default_font_width_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,16),_Pcl_default_font_width_Type())
pcl_default_font_width.setMaxAccess(_C)
if mibBuilder.loadTexts:pcl_default_font_width.setStatus(_A)
_Pdl_postscript_ObjectIdentity=ObjectIdentity
pdl_postscript=_Pdl_postscript_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4))
_Postscript_total_page_count_Type=Integer32
_Postscript_total_page_count_Object=MibScalar
postscript_total_page_count=_Postscript_total_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4,5),_Postscript_total_page_count_Type())
postscript_total_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:postscript_total_page_count.setStatus(_A)
class _Postscript_print_errors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_P,2)))
_Postscript_print_errors_Type.__name__=_D
_Postscript_print_errors_Object=MibScalar
postscript_print_errors=_Postscript_print_errors_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4,11),_Postscript_print_errors_Type())
postscript_print_errors.setMaxAccess(_C)
if mibBuilder.loadTexts:postscript_print_errors.setStatus(_A)
_Pdl_pdf_ObjectIdentity=ObjectIdentity
pdl_pdf=_Pdl_pdf_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,15))
class _Pdf_print_errors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_P,2)))
_Pdf_print_errors_Type.__name__=_D
_Pdf_print_errors_Object=MibScalar
pdf_print_errors=_Pdf_print_errors_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,15,4),_Pdf_print_errors_Type())
pdf_print_errors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdf_print_errors.setStatus(_A)
_Pml_ObjectIdentity=ObjectIdentity
pml=_Pml_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,4))
_Pjl_ObjectIdentity=ObjectIdentity
pjl=_Pjl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,5))
_Webserver_proc_sub_ObjectIdentity=ObjectIdentity
webserver_proc_sub=_Webserver_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,9))
_Settings_webserver_ObjectIdentity=ObjectIdentity
settings_webserver=_Settings_webserver_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,9,1))
class _Web_server_url_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Web_server_url_Type.__name__=_E
_Web_server_url_Object=MibScalar
web_server_url=_Web_server_url_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,9,1,2),_Web_server_url_Type())
web_server_url.setMaxAccess(_C)
if mibBuilder.loadTexts:web_server_url.setStatus(_A)
_Web_server_security_Type=OctetString
_Web_server_security_Object=MibScalar
web_server_security=_Web_server_security_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,9,1,3),_Web_server_security_Type())
web_server_security.setMaxAccess(_C)
if mibBuilder.loadTexts:web_server_security.setStatus(_A)
_Destination_subsystem_ObjectIdentity=ObjectIdentity
destination_subsystem=_Destination_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4))
_Print_engine_ObjectIdentity=ObjectIdentity
print_engine=_Print_engine_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1))
_Settings_prt_eng_ObjectIdentity=ObjectIdentity
settings_prt_eng=_Settings_prt_eng_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1))
_Override_media_name_Type=OctetString
_Override_media_name_Object=MibScalar
override_media_name=_Override_media_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,2),_Override_media_name_Type())
override_media_name.setMaxAccess(_C)
if mibBuilder.loadTexts:override_media_name.setStatus(_A)
class _Override_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,11,17,18,19,25,26,27,45,46,65,72,80,81,90,91,100,101,258,282,32767)));namedValues=NamedValues(*((_U,1),(_Q,2),(_V,3),(_q,11),(_W,17),(_X,18),(_r,19),(_Y,25),(_R,26),(_s,27),(_Z,45),(_t,46),(_u,65),(_A5,72),(_b,80),(_c,81),(_d,90),(_e,91),(_f,100),(_a,101),(_w,258),(_x,282),(_i,32767)))
_Override_media_size_Type.__name__=_D
_Override_media_size_Object=MibScalar
override_media_size=_Override_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,3),_Override_media_size_Type())
override_media_size.setMaxAccess(_C)
if mibBuilder.loadTexts:override_media_size.setStatus(_A)
_Marking_agent_density_ObjectIdentity=ObjectIdentity
marking_agent_density=_Marking_agent_density_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,9))
_Marking_agent_highlights_density_setting_Type=Integer32
_Marking_agent_highlights_density_setting_Object=MibScalar
marking_agent_highlights_density_setting=_Marking_agent_highlights_density_setting_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,9,2),_Marking_agent_highlights_density_setting_Type())
marking_agent_highlights_density_setting.setMaxAccess(_C)
if mibBuilder.loadTexts:marking_agent_highlights_density_setting.setStatus(_A)
_Marking_agent_midtones_density_setting_Type=Integer32
_Marking_agent_midtones_density_setting_Object=MibScalar
marking_agent_midtones_density_setting=_Marking_agent_midtones_density_setting_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,9,3),_Marking_agent_midtones_density_setting_Type())
marking_agent_midtones_density_setting.setMaxAccess(_C)
if mibBuilder.loadTexts:marking_agent_midtones_density_setting.setStatus(_A)
_Marking_agent_shadows_density_setting_Type=Integer32
_Marking_agent_shadows_density_setting_Object=MibScalar
marking_agent_shadows_density_setting=_Marking_agent_shadows_density_setting_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,9,4),_Marking_agent_shadows_density_setting_Type())
marking_agent_shadows_density_setting.setMaxAccess(_C)
if mibBuilder.loadTexts:marking_agent_shadows_density_setting.setStatus(_A)
_Autocleaning_page_frequency_Type=Integer32
_Autocleaning_page_frequency_Object=MibScalar
autocleaning_page_frequency=_Autocleaning_page_frequency_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,11),_Autocleaning_page_frequency_Type())
autocleaning_page_frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:autocleaning_page_frequency.setStatus(_A)
class _Autocleaning_page_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,26)));namedValues=NamedValues(*((_Q,2),(_R,26)))
_Autocleaning_page_size_Type.__name__=_D
_Autocleaning_page_size_Object=MibScalar
autocleaning_page_size=_Autocleaning_page_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,12),_Autocleaning_page_size_Type())
autocleaning_page_size.setMaxAccess(_C)
if mibBuilder.loadTexts:autocleaning_page_size.setStatus(_A)
_Calibration_power_on_delay_Type=Integer32
_Calibration_power_on_delay_Object=MibScalar
calibration_power_on_delay=_Calibration_power_on_delay_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,21),_Calibration_power_on_delay_Type())
calibration_power_on_delay.setMaxAccess(_C)
if mibBuilder.loadTexts:calibration_power_on_delay.setStatus(_A)
class _Configurable_low_threshold_setting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Configurable_low_threshold_setting_Type.__name__=_D
_Configurable_low_threshold_setting_Object=MibScalar
configurable_low_threshold_setting=_Configurable_low_threshold_setting_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,24),_Configurable_low_threshold_setting_Type())
configurable_low_threshold_setting.setMaxAccess(_C)
if mibBuilder.loadTexts:configurable_low_threshold_setting.setStatus(_A)
class _Supplies_replace_action_at_setting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('eStopAtLow',1),('eStopAtOut',2),('eOverrideAtOut',4)))
_Supplies_replace_action_at_setting_Type.__name__=_D
_Supplies_replace_action_at_setting_Object=MibScalar
supplies_replace_action_at_setting=_Supplies_replace_action_at_setting_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,25),_Supplies_replace_action_at_setting_Type())
supplies_replace_action_at_setting.setMaxAccess(_C)
if mibBuilder.loadTexts:supplies_replace_action_at_setting.setStatus(_A)
class _Supply_out_user_configured_override_limit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_Supply_out_user_configured_override_limit_Type.__name__=_D
_Supply_out_user_configured_override_limit_Object=MibScalar
supply_out_user_configured_override_limit=_Supply_out_user_configured_override_limit_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,26),_Supply_out_user_configured_override_limit_Type())
supply_out_user_configured_override_limit.setMaxAccess(_B)
if mibBuilder.loadTexts:supply_out_user_configured_override_limit.setStatus(_A)
_Cartridge_out_override_control_Type=Integer32
_Cartridge_out_override_control_Object=MibScalar
cartridge_out_override_control=_Cartridge_out_override_control_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,27),_Cartridge_out_override_control_Type())
cartridge_out_override_control.setMaxAccess(_F)
if mibBuilder.loadTexts:cartridge_out_override_control.setStatus(_A)
class _Duplex_blank_pages_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eDuplexBlankPagesAuto',1),('eDuplexBlankPagesYes',2)))
_Duplex_blank_pages_Type.__name__=_D
_Duplex_blank_pages_Object=MibScalar
duplex_blank_pages=_Duplex_blank_pages_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,28),_Duplex_blank_pages_Type())
duplex_blank_pages.setMaxAccess(_C)
if mibBuilder.loadTexts:duplex_blank_pages.setStatus(_A)
_Supply_out_user_configured_override2_limit_Type=Integer32
_Supply_out_user_configured_override2_limit_Object=MibScalar
supply_out_user_configured_override2_limit=_Supply_out_user_configured_override2_limit_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,33),_Supply_out_user_configured_override2_limit_Type())
supply_out_user_configured_override2_limit.setMaxAccess(_B)
if mibBuilder.loadTexts:supply_out_user_configured_override2_limit.setStatus(_A)
_Status_prt_eng_ObjectIdentity=ObjectIdentity
status_prt_eng=_Status_prt_eng_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2))
_Total_color_page_count_Type=Integer32
_Total_color_page_count_Object=MibScalar
total_color_page_count=_Total_color_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,7),_Total_color_page_count_Type())
total_color_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:total_color_page_count.setStatus(_A)
_Duplex_page_count_Type=Integer32
_Duplex_page_count_Object=MibScalar
duplex_page_count=_Duplex_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,22),_Duplex_page_count_Type())
duplex_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:duplex_page_count.setStatus(_A)
class _Print_engine_revision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Print_engine_revision_Type.__name__=_E
_Print_engine_revision_Object=MibScalar
print_engine_revision=_Print_engine_revision_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,26),_Print_engine_revision_Type())
print_engine_revision.setMaxAccess(_B)
if mibBuilder.loadTexts:print_engine_revision.setStatus(_A)
_Printer_calibration_dhalf_ObjectIdentity=ObjectIdentity
printer_calibration_dhalf=_Printer_calibration_dhalf_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37))
_Printer_cal_dhalf_page_count_Type=Integer32
_Printer_cal_dhalf_page_count_Object=MibScalar
printer_cal_dhalf_page_count=_Printer_cal_dhalf_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,1),_Printer_cal_dhalf_page_count_Type())
printer_cal_dhalf_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_dhalf_page_count.setStatus(_A)
_Printer_cal_dhalf_utc_Type=Integer32
_Printer_cal_dhalf_utc_Object=MibScalar
printer_cal_dhalf_utc=_Printer_cal_dhalf_utc_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,2),_Printer_cal_dhalf_utc_Type())
printer_cal_dhalf_utc.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_dhalf_utc.setStatus(_A)
_Printer_cal_dhalf_data_ObjectIdentity=ObjectIdentity
printer_cal_dhalf_data=_Printer_cal_dhalf_data_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,3))
_Printer_cal_dhalf_data1_Type=OctetString
_Printer_cal_dhalf_data1_Object=MibScalar
printer_cal_dhalf_data1=_Printer_cal_dhalf_data1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,3,1),_Printer_cal_dhalf_data1_Type())
printer_cal_dhalf_data1.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_dhalf_data1.setStatus(_A)
_Printer_cal_dhalf_data2_Type=OctetString
_Printer_cal_dhalf_data2_Object=MibScalar
printer_cal_dhalf_data2=_Printer_cal_dhalf_data2_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,3,2),_Printer_cal_dhalf_data2_Type())
printer_cal_dhalf_data2.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_dhalf_data2.setStatus(_A)
_Printer_cal_grayaxis_count_Type=Integer32
_Printer_cal_grayaxis_count_Object=MibScalar
printer_cal_grayaxis_count=_Printer_cal_grayaxis_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,4),_Printer_cal_grayaxis_count_Type())
printer_cal_grayaxis_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_grayaxis_count.setStatus(_A)
_Printer_cal_grayaxis_utc_Type=Integer32
_Printer_cal_grayaxis_utc_Object=MibScalar
printer_cal_grayaxis_utc=_Printer_cal_grayaxis_utc_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,5),_Printer_cal_grayaxis_utc_Type())
printer_cal_grayaxis_utc.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_grayaxis_utc.setStatus(_A)
_Printer_cal_grayaxis_ObjectIdentity=ObjectIdentity
printer_cal_grayaxis=_Printer_cal_grayaxis_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,6))
_Printer_cal_grayaxis_tray_Type=Integer32
_Printer_cal_grayaxis_tray_Object=MibScalar
printer_cal_grayaxis_tray=_Printer_cal_grayaxis_tray_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,6,1),_Printer_cal_grayaxis_tray_Type())
printer_cal_grayaxis_tray.setMaxAccess(_C)
if mibBuilder.loadTexts:printer_cal_grayaxis_tray.setStatus(_A)
class _Printer_cal_grayaxis_media_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Printer_cal_grayaxis_media_Type.__name__=_E
_Printer_cal_grayaxis_media_Object=MibScalar
printer_cal_grayaxis_media=_Printer_cal_grayaxis_media_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,6,2),_Printer_cal_grayaxis_media_Type())
printer_cal_grayaxis_media.setMaxAccess(_C)
if mibBuilder.loadTexts:printer_cal_grayaxis_media.setStatus(_A)
_Printer_cal_grayaxis_xsize_Type=Integer32
_Printer_cal_grayaxis_xsize_Object=MibScalar
printer_cal_grayaxis_xsize=_Printer_cal_grayaxis_xsize_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,6,3),_Printer_cal_grayaxis_xsize_Type())
printer_cal_grayaxis_xsize.setMaxAccess(_C)
if mibBuilder.loadTexts:printer_cal_grayaxis_xsize.setStatus(_A)
_Printer_cal_grayaxis_ysize_Type=Integer32
_Printer_cal_grayaxis_ysize_Object=MibScalar
printer_cal_grayaxis_ysize=_Printer_cal_grayaxis_ysize_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,6,4),_Printer_cal_grayaxis_ysize_Type())
printer_cal_grayaxis_ysize.setMaxAccess(_C)
if mibBuilder.loadTexts:printer_cal_grayaxis_ysize.setStatus(_A)
_Printer_cal_grayaxis_data_ObjectIdentity=ObjectIdentity
printer_cal_grayaxis_data=_Printer_cal_grayaxis_data_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,7))
_Printer_cal_grayaxis_data1_Type=OctetString
_Printer_cal_grayaxis_data1_Object=MibScalar
printer_cal_grayaxis_data1=_Printer_cal_grayaxis_data1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,7,1),_Printer_cal_grayaxis_data1_Type())
printer_cal_grayaxis_data1.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_grayaxis_data1.setStatus(_A)
_Printer_cal_grayaxis_data2_Type=OctetString
_Printer_cal_grayaxis_data2_Object=MibScalar
printer_cal_grayaxis_data2=_Printer_cal_grayaxis_data2_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,37,7,2),_Printer_cal_grayaxis_data2_Type())
printer_cal_grayaxis_data2.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_grayaxis_data2.setStatus(_A)
_Printer_calibration_cpr_ObjectIdentity=ObjectIdentity
printer_calibration_cpr=_Printer_calibration_cpr_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,38))
_Printer_cal_cpr_page_count_Type=Integer32
_Printer_cal_cpr_page_count_Object=MibScalar
printer_cal_cpr_page_count=_Printer_cal_cpr_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,38,1),_Printer_cal_cpr_page_count_Type())
printer_cal_cpr_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_cpr_page_count.setStatus(_A)
_Printer_cal_cpr_utc_Type=Integer32
_Printer_cal_cpr_utc_Object=MibScalar
printer_cal_cpr_utc=_Printer_cal_cpr_utc_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,38,2),_Printer_cal_cpr_utc_Type())
printer_cal_cpr_utc.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_cpr_utc.setStatus(_A)
_Printer_cal_cpr_data_Type=OctetString
_Printer_cal_cpr_data_Object=MibScalar
printer_cal_cpr_data=_Printer_cal_cpr_data_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,38,3),_Printer_cal_cpr_data_Type())
printer_cal_cpr_data.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_cal_cpr_data.setStatus(_A)
_Supply_out_action_support_Type=OctetString
_Supply_out_action_support_Object=MibScalar
supply_out_action_support=_Supply_out_action_support_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,48),_Supply_out_action_support_Type())
supply_out_action_support.setMaxAccess(_B)
if mibBuilder.loadTexts:supply_out_action_support.setStatus(_A)
class _Supply_out_device_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eNoSupplyOut',1),(_n,2),('eSupplyOutOverride',3),('eMonochromePrintingAfterColorCartridgeOut',4)))
_Supply_out_device_state_Type.__name__=_D
_Supply_out_device_state_Object=MibScalar
supply_out_device_state=_Supply_out_device_state_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,49),_Supply_out_device_state_Type())
supply_out_device_state.setMaxAccess(_B)
if mibBuilder.loadTexts:supply_out_device_state.setStatus(_A)
_Supply_after_out_state_Type=OctetString
_Supply_after_out_state_Object=MibScalar
supply_after_out_state=_Supply_after_out_state_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,50),_Supply_after_out_state_Type())
supply_after_out_state.setMaxAccess(_B)
if mibBuilder.loadTexts:supply_after_out_state.setStatus(_A)
_Intray_ObjectIdentity=ObjectIdentity
intray=_Intray_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3))
_Settings_intray_ObjectIdentity=ObjectIdentity
settings_intray=_Settings_intray_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1))
class _Input_tray_auto_select_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_P,2)))
_Input_tray_auto_select_Type.__name__=_D
_Input_tray_auto_select_Object=MibScalar
input_tray_auto_select=_Input_tray_auto_select_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,2),_Input_tray_auto_select_Type())
input_tray_auto_select.setMaxAccess(_C)
if mibBuilder.loadTexts:input_tray_auto_select.setStatus(_A)
_Custom_paper_feed_dim_Type=Integer32
_Custom_paper_feed_dim_Object=MibScalar
custom_paper_feed_dim=_Custom_paper_feed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,8),_Custom_paper_feed_dim_Type())
custom_paper_feed_dim.setMaxAccess(_C)
if mibBuilder.loadTexts:custom_paper_feed_dim.setStatus(_A)
_Custom_paper_xfeed_dim_Type=Integer32
_Custom_paper_xfeed_dim_Object=MibScalar
custom_paper_xfeed_dim=_Custom_paper_xfeed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,9),_Custom_paper_xfeed_dim_Type())
custom_paper_xfeed_dim.setMaxAccess(_C)
if mibBuilder.loadTexts:custom_paper_xfeed_dim.setStatus(_A)
class _Default_custom_paper_dim_unit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('eTenThousandthsOfInches',3),('eMicrometers',4)))
_Default_custom_paper_dim_unit_Type.__name__=_D
_Default_custom_paper_dim_unit_Object=MibScalar
default_custom_paper_dim_unit=_Default_custom_paper_dim_unit_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,10),_Default_custom_paper_dim_unit_Type())
default_custom_paper_dim_unit.setMaxAccess(_C)
if mibBuilder.loadTexts:default_custom_paper_dim_unit.setStatus(_A)
_Default_custom_paper_feed_dim_Type=Integer32
_Default_custom_paper_feed_dim_Object=MibScalar
default_custom_paper_feed_dim=_Default_custom_paper_feed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,11),_Default_custom_paper_feed_dim_Type())
default_custom_paper_feed_dim.setMaxAccess(_C)
if mibBuilder.loadTexts:default_custom_paper_feed_dim.setStatus(_A)
_Default_custom_paper_xfeed_dim_Type=Integer32
_Default_custom_paper_xfeed_dim_Object=MibScalar
default_custom_paper_xfeed_dim=_Default_custom_paper_xfeed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,12),_Default_custom_paper_xfeed_dim_Type())
default_custom_paper_xfeed_dim.setMaxAccess(_C)
if mibBuilder.loadTexts:default_custom_paper_xfeed_dim.setStatus(_A)
_Input_tray_max_media_feed_dim_Type=Integer32
_Input_tray_max_media_feed_dim_Object=MibScalar
input_tray_max_media_feed_dim=_Input_tray_max_media_feed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,14),_Input_tray_max_media_feed_dim_Type())
input_tray_max_media_feed_dim.setMaxAccess(_B)
if mibBuilder.loadTexts:input_tray_max_media_feed_dim.setStatus(_A)
_Input_tray_max_media_xfeed_dim_Type=Integer32
_Input_tray_max_media_xfeed_dim_Object=MibScalar
input_tray_max_media_xfeed_dim=_Input_tray_max_media_xfeed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,15),_Input_tray_max_media_xfeed_dim_Type())
input_tray_max_media_xfeed_dim.setMaxAccess(_B)
if mibBuilder.loadTexts:input_tray_max_media_xfeed_dim.setStatus(_A)
_Input_tray_min_media_feed_dim_Type=Integer32
_Input_tray_min_media_feed_dim_Object=MibScalar
input_tray_min_media_feed_dim=_Input_tray_min_media_feed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,16),_Input_tray_min_media_feed_dim_Type())
input_tray_min_media_feed_dim.setMaxAccess(_B)
if mibBuilder.loadTexts:input_tray_min_media_feed_dim.setStatus(_A)
_Input_tray_min_media_xfeed_dim_Type=Integer32
_Input_tray_min_media_xfeed_dim_Object=MibScalar
input_tray_min_media_xfeed_dim=_Input_tray_min_media_xfeed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,17),_Input_tray_min_media_xfeed_dim_Type())
input_tray_min_media_xfeed_dim.setMaxAccess(_B)
if mibBuilder.loadTexts:input_tray_min_media_xfeed_dim.setStatus(_A)
class _Tray_prompt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eDoNotDisplay',1),('eDisplay',2)))
_Tray_prompt_Type.__name__=_D
_Tray_prompt_Object=MibScalar
tray_prompt=_Tray_prompt_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,19),_Tray_prompt_Type())
tray_prompt.setMaxAccess(_C)
if mibBuilder.loadTexts:tray_prompt.setStatus(_A)
_Intrays_ObjectIdentity=ObjectIdentity
intrays=_Intrays_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3))
_Intray1_ObjectIdentity=ObjectIdentity
intray1=_Intray1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1))
class _Tray1_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,15,17,18,25,26,45,72,80,81,90,91,100,101,32764,32765)));namedValues=NamedValues(*((_U,1),(_Q,2),(_V,3),(_g,10),(_A4,15),(_W,17),(_X,18),(_Y,25),(_R,26),(_Z,45),(_v,72),(_b,80),(_c,81),(_d,90),(_e,91),(_f,100),(_a,101),(_k,32764),(_l,32765)))
_Tray1_media_size_loaded_Type.__name__=_D
_Tray1_media_size_loaded_Object=MibScalar
tray1_media_size_loaded=_Tray1_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,1),_Tray1_media_size_loaded_Type())
tray1_media_size_loaded.setMaxAccess(_C)
if mibBuilder.loadTexts:tray1_media_size_loaded.setStatus(_A)
_Tray1_phd_Type=Integer32
_Tray1_phd_Object=MibScalar
tray1_phd=_Tray1_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,12),_Tray1_phd_Type())
tray1_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:tray1_phd.setStatus(_A)
_Intray2_ObjectIdentity=ObjectIdentity
intray2=_Intray2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2))
class _Tray2_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,17,18,25,26,45,101,32764,32765)));namedValues=NamedValues(*((_U,1),(_Q,2),(_V,3),(_g,10),(_W,17),(_X,18),(_Y,25),(_R,26),(_Z,45),(_a,101),(_k,32764),(_l,32765)))
_Tray2_media_size_loaded_Type.__name__=_D
_Tray2_media_size_loaded_Object=MibScalar
tray2_media_size_loaded=_Tray2_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,1),_Tray2_media_size_loaded_Type())
tray2_media_size_loaded.setMaxAccess(_C)
if mibBuilder.loadTexts:tray2_media_size_loaded.setStatus(_A)
_Tray2_phd_Type=Integer32
_Tray2_phd_Object=MibScalar
tray2_phd=_Tray2_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,12),_Tray2_phd_Type())
tray2_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:tray2_phd.setStatus(_A)
_Intray3_ObjectIdentity=ObjectIdentity
intray3=_Intray3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3))
class _Tray3_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,17,18,25,26,45,101,32764,32765)));namedValues=NamedValues(*((_U,1),(_Q,2),(_V,3),(_g,10),(_W,17),(_X,18),(_Y,25),(_R,26),(_Z,45),(_a,101),(_k,32764),(_l,32765)))
_Tray3_media_size_loaded_Type.__name__=_D
_Tray3_media_size_loaded_Object=MibScalar
tray3_media_size_loaded=_Tray3_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,1),_Tray3_media_size_loaded_Type())
tray3_media_size_loaded.setMaxAccess(_C)
if mibBuilder.loadTexts:tray3_media_size_loaded.setStatus(_A)
_Tray3_phd_Type=Integer32
_Tray3_phd_Object=MibScalar
tray3_phd=_Tray3_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,12),_Tray3_phd_Type())
tray3_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:tray3_phd.setStatus(_A)
_Outbin_ObjectIdentity=ObjectIdentity
outbin=_Outbin_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4))
_Settings_outbin_ObjectIdentity=ObjectIdentity
settings_outbin=_Settings_outbin_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,1))
_Overflow_bin_Type=Integer32
_Overflow_bin_Object=MibScalar
overflow_bin=_Overflow_bin_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,1,4),_Overflow_bin_Type())
overflow_bin.setMaxAccess(_C)
if mibBuilder.loadTexts:overflow_bin.setStatus(_A)
_Outbins_ObjectIdentity=ObjectIdentity
outbins=_Outbins_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3))
_Outbin1_ObjectIdentity=ObjectIdentity
outbin1=_Outbin1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,1))
_Outbin1_override_mode_Type=OctetString
_Outbin1_override_mode_Object=MibScalar
outbin1_override_mode=_Outbin1_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,1,9),_Outbin1_override_mode_Type())
outbin1_override_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:outbin1_override_mode.setStatus(_A)
_Marking_agent_ObjectIdentity=ObjectIdentity
marking_agent=_Marking_agent_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,5))
_Settings_marking_agent_ObjectIdentity=ObjectIdentity
settings_marking_agent=_Settings_marking_agent_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,5,1))
class _Marker_density_calibration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('eNotCalibrating',1),('eCalibrateALL',2),('eCalibrateColor',3),('eCalibrateHalftone',4),('eCalibrateColorPlaneRegistration',5)))
_Marker_density_calibration_Type.__name__=_D
_Marker_density_calibration_Object=MibScalar
marker_density_calibration=_Marker_density_calibration_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,5,1,11),_Marker_density_calibration_Type())
marker_density_calibration.setMaxAccess(_C)
if mibBuilder.loadTexts:marker_density_calibration.setStatus(_A)
_Ph_ObjectIdentity=ObjectIdentity
ph=_Ph_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7))
_Settings_ph_ObjectIdentity=ObjectIdentity
settings_ph=_Settings_ph_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7,1))
class _Tray_disable_use_instead_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_y,1),(_z,2)))
_Tray_disable_use_instead_Type.__name__=_D
_Tray_disable_use_instead_Object=MibScalar
tray_disable_use_instead=_Tray_disable_use_instead_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7,1,1),_Tray_disable_use_instead_Type())
tray_disable_use_instead.setMaxAccess(_C)
if mibBuilder.loadTexts:tray_disable_use_instead.setStatus(_A)
_Print_media_ObjectIdentity=ObjectIdentity
print_media=_Print_media_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8))
_Settings_print_media_ObjectIdentity=ObjectIdentity
settings_print_media=_Settings_print_media_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1))
_Media_names_available_Type=OctetString
_Media_names_available_Object=MibScalar
media_names_available=_Media_names_available_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1,1),_Media_names_available_Type())
media_names_available.setMaxAccess(_C)
if mibBuilder.loadTexts:media_names_available.setStatus(_A)
_North_edge_offset_Type=Integer32
_North_edge_offset_Object=MibScalar
north_edge_offset=_North_edge_offset_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1,2),_North_edge_offset_Type())
north_edge_offset.setMaxAccess(_C)
if mibBuilder.loadTexts:north_edge_offset.setStatus(_A)
class _Media_names_enabled_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Media_names_enabled_Type.__name__=_E
_Media_names_enabled_Object=MibScalar
media_names_enabled=_Media_names_enabled_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1,3),_Media_names_enabled_Type())
media_names_enabled.setMaxAccess(_C)
if mibBuilder.loadTexts:media_names_enabled.setStatus(_A)
_Media_info_ObjectIdentity=ObjectIdentity
media_info=_Media_info_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3))
_Media1_ObjectIdentity=ObjectIdentity
media1=_Media1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1))
class _Media1_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media1_name_Type.__name__=_E
_Media1_name_Object=MibScalar
media1_name=_Media1_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1,1),_Media1_name_Type())
media1_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media1_name.setStatus(_A)
class _Media1_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media1_short_name_Type.__name__=_E
_Media1_short_name_Object=MibScalar
media1_short_name=_Media1_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1,2),_Media1_short_name_Type())
media1_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media1_short_name.setStatus(_A)
_Media1_page_count_Type=Integer32
_Media1_page_count_Object=MibScalar
media1_page_count=_Media1_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1,3),_Media1_page_count_Type())
media1_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media1_page_count.setStatus(_A)
_Media1_engine_media_mode_Type=Integer32
_Media1_engine_media_mode_Object=MibScalar
media1_engine_media_mode=_Media1_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1,4),_Media1_engine_media_mode_Type())
media1_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media1_engine_media_mode.setStatus(_A)
_Media2_ObjectIdentity=ObjectIdentity
media2=_Media2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2))
class _Media2_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media2_name_Type.__name__=_E
_Media2_name_Object=MibScalar
media2_name=_Media2_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2,1),_Media2_name_Type())
media2_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media2_name.setStatus(_A)
class _Media2_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media2_short_name_Type.__name__=_E
_Media2_short_name_Object=MibScalar
media2_short_name=_Media2_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2,2),_Media2_short_name_Type())
media2_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media2_short_name.setStatus(_A)
_Media2_page_count_Type=Integer32
_Media2_page_count_Object=MibScalar
media2_page_count=_Media2_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2,3),_Media2_page_count_Type())
media2_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media2_page_count.setStatus(_A)
_Media2_engine_media_mode_Type=Integer32
_Media2_engine_media_mode_Object=MibScalar
media2_engine_media_mode=_Media2_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2,4),_Media2_engine_media_mode_Type())
media2_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media2_engine_media_mode.setStatus(_A)
_Media3_ObjectIdentity=ObjectIdentity
media3=_Media3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3))
class _Media3_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media3_name_Type.__name__=_E
_Media3_name_Object=MibScalar
media3_name=_Media3_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3,1),_Media3_name_Type())
media3_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media3_name.setStatus(_A)
class _Media3_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media3_short_name_Type.__name__=_E
_Media3_short_name_Object=MibScalar
media3_short_name=_Media3_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3,2),_Media3_short_name_Type())
media3_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media3_short_name.setStatus(_A)
_Media3_page_count_Type=Integer32
_Media3_page_count_Object=MibScalar
media3_page_count=_Media3_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3,3),_Media3_page_count_Type())
media3_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media3_page_count.setStatus(_A)
_Media3_engine_media_mode_Type=Integer32
_Media3_engine_media_mode_Object=MibScalar
media3_engine_media_mode=_Media3_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3,4),_Media3_engine_media_mode_Type())
media3_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media3_engine_media_mode.setStatus(_A)
_Media4_ObjectIdentity=ObjectIdentity
media4=_Media4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4))
class _Media4_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media4_name_Type.__name__=_E
_Media4_name_Object=MibScalar
media4_name=_Media4_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4,1),_Media4_name_Type())
media4_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media4_name.setStatus(_A)
class _Media4_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media4_short_name_Type.__name__=_E
_Media4_short_name_Object=MibScalar
media4_short_name=_Media4_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4,2),_Media4_short_name_Type())
media4_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media4_short_name.setStatus(_A)
_Media4_page_count_Type=Integer32
_Media4_page_count_Object=MibScalar
media4_page_count=_Media4_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4,3),_Media4_page_count_Type())
media4_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media4_page_count.setStatus(_A)
_Media4_engine_media_mode_Type=Integer32
_Media4_engine_media_mode_Object=MibScalar
media4_engine_media_mode=_Media4_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4,4),_Media4_engine_media_mode_Type())
media4_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media4_engine_media_mode.setStatus(_A)
_Media5_ObjectIdentity=ObjectIdentity
media5=_Media5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5))
class _Media5_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media5_name_Type.__name__=_E
_Media5_name_Object=MibScalar
media5_name=_Media5_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5,1),_Media5_name_Type())
media5_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media5_name.setStatus(_A)
class _Media5_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media5_short_name_Type.__name__=_E
_Media5_short_name_Object=MibScalar
media5_short_name=_Media5_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5,2),_Media5_short_name_Type())
media5_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media5_short_name.setStatus(_A)
_Media5_page_count_Type=Integer32
_Media5_page_count_Object=MibScalar
media5_page_count=_Media5_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5,3),_Media5_page_count_Type())
media5_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media5_page_count.setStatus(_A)
_Media5_engine_media_mode_Type=Integer32
_Media5_engine_media_mode_Object=MibScalar
media5_engine_media_mode=_Media5_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5,4),_Media5_engine_media_mode_Type())
media5_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media5_engine_media_mode.setStatus(_A)
_Media6_ObjectIdentity=ObjectIdentity
media6=_Media6_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6))
class _Media6_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media6_name_Type.__name__=_E
_Media6_name_Object=MibScalar
media6_name=_Media6_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6,1),_Media6_name_Type())
media6_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media6_name.setStatus(_A)
class _Media6_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media6_short_name_Type.__name__=_E
_Media6_short_name_Object=MibScalar
media6_short_name=_Media6_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6,2),_Media6_short_name_Type())
media6_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media6_short_name.setStatus(_A)
_Media6_page_count_Type=Integer32
_Media6_page_count_Object=MibScalar
media6_page_count=_Media6_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6,3),_Media6_page_count_Type())
media6_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media6_page_count.setStatus(_A)
_Media6_engine_media_mode_Type=Integer32
_Media6_engine_media_mode_Object=MibScalar
media6_engine_media_mode=_Media6_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6,4),_Media6_engine_media_mode_Type())
media6_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media6_engine_media_mode.setStatus(_A)
_Media7_ObjectIdentity=ObjectIdentity
media7=_Media7_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7))
class _Media7_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media7_name_Type.__name__=_E
_Media7_name_Object=MibScalar
media7_name=_Media7_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7,1),_Media7_name_Type())
media7_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media7_name.setStatus(_A)
class _Media7_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media7_short_name_Type.__name__=_E
_Media7_short_name_Object=MibScalar
media7_short_name=_Media7_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7,2),_Media7_short_name_Type())
media7_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media7_short_name.setStatus(_A)
_Media7_page_count_Type=Integer32
_Media7_page_count_Object=MibScalar
media7_page_count=_Media7_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7,3),_Media7_page_count_Type())
media7_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media7_page_count.setStatus(_A)
_Media7_engine_media_mode_Type=Integer32
_Media7_engine_media_mode_Object=MibScalar
media7_engine_media_mode=_Media7_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7,4),_Media7_engine_media_mode_Type())
media7_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media7_engine_media_mode.setStatus(_A)
_Media8_ObjectIdentity=ObjectIdentity
media8=_Media8_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8))
class _Media8_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media8_name_Type.__name__=_E
_Media8_name_Object=MibScalar
media8_name=_Media8_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8,1),_Media8_name_Type())
media8_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media8_name.setStatus(_A)
class _Media8_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media8_short_name_Type.__name__=_E
_Media8_short_name_Object=MibScalar
media8_short_name=_Media8_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8,2),_Media8_short_name_Type())
media8_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media8_short_name.setStatus(_A)
_Media8_page_count_Type=Integer32
_Media8_page_count_Object=MibScalar
media8_page_count=_Media8_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8,3),_Media8_page_count_Type())
media8_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media8_page_count.setStatus(_A)
_Media8_engine_media_mode_Type=Integer32
_Media8_engine_media_mode_Object=MibScalar
media8_engine_media_mode=_Media8_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8,4),_Media8_engine_media_mode_Type())
media8_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media8_engine_media_mode.setStatus(_A)
_Media9_ObjectIdentity=ObjectIdentity
media9=_Media9_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9))
class _Media9_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media9_name_Type.__name__=_E
_Media9_name_Object=MibScalar
media9_name=_Media9_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9,1),_Media9_name_Type())
media9_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media9_name.setStatus(_A)
class _Media9_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media9_short_name_Type.__name__=_E
_Media9_short_name_Object=MibScalar
media9_short_name=_Media9_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9,2),_Media9_short_name_Type())
media9_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media9_short_name.setStatus(_A)
_Media9_page_count_Type=Integer32
_Media9_page_count_Object=MibScalar
media9_page_count=_Media9_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9,3),_Media9_page_count_Type())
media9_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media9_page_count.setStatus(_A)
_Media9_engine_media_mode_Type=Integer32
_Media9_engine_media_mode_Object=MibScalar
media9_engine_media_mode=_Media9_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9,4),_Media9_engine_media_mode_Type())
media9_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media9_engine_media_mode.setStatus(_A)
_Media10_ObjectIdentity=ObjectIdentity
media10=_Media10_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10))
class _Media10_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media10_name_Type.__name__=_E
_Media10_name_Object=MibScalar
media10_name=_Media10_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10,1),_Media10_name_Type())
media10_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media10_name.setStatus(_A)
class _Media10_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media10_short_name_Type.__name__=_E
_Media10_short_name_Object=MibScalar
media10_short_name=_Media10_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10,2),_Media10_short_name_Type())
media10_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media10_short_name.setStatus(_A)
_Media10_page_count_Type=Integer32
_Media10_page_count_Object=MibScalar
media10_page_count=_Media10_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10,3),_Media10_page_count_Type())
media10_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media10_page_count.setStatus(_A)
_Media10_engine_media_mode_Type=Integer32
_Media10_engine_media_mode_Object=MibScalar
media10_engine_media_mode=_Media10_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10,4),_Media10_engine_media_mode_Type())
media10_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media10_engine_media_mode.setStatus(_A)
_Media11_ObjectIdentity=ObjectIdentity
media11=_Media11_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11))
class _Media11_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media11_name_Type.__name__=_E
_Media11_name_Object=MibScalar
media11_name=_Media11_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11,1),_Media11_name_Type())
media11_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media11_name.setStatus(_A)
class _Media11_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media11_short_name_Type.__name__=_E
_Media11_short_name_Object=MibScalar
media11_short_name=_Media11_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11,2),_Media11_short_name_Type())
media11_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media11_short_name.setStatus(_A)
_Media11_page_count_Type=Integer32
_Media11_page_count_Object=MibScalar
media11_page_count=_Media11_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11,3),_Media11_page_count_Type())
media11_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media11_page_count.setStatus(_A)
_Media11_engine_media_mode_Type=Integer32
_Media11_engine_media_mode_Object=MibScalar
media11_engine_media_mode=_Media11_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11,4),_Media11_engine_media_mode_Type())
media11_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media11_engine_media_mode.setStatus(_A)
_Media12_ObjectIdentity=ObjectIdentity
media12=_Media12_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12))
class _Media12_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media12_name_Type.__name__=_E
_Media12_name_Object=MibScalar
media12_name=_Media12_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12,1),_Media12_name_Type())
media12_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media12_name.setStatus(_A)
class _Media12_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media12_short_name_Type.__name__=_E
_Media12_short_name_Object=MibScalar
media12_short_name=_Media12_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12,2),_Media12_short_name_Type())
media12_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media12_short_name.setStatus(_A)
_Media12_page_count_Type=Integer32
_Media12_page_count_Object=MibScalar
media12_page_count=_Media12_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12,3),_Media12_page_count_Type())
media12_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media12_page_count.setStatus(_A)
_Media12_engine_media_mode_Type=Integer32
_Media12_engine_media_mode_Object=MibScalar
media12_engine_media_mode=_Media12_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12,4),_Media12_engine_media_mode_Type())
media12_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media12_engine_media_mode.setStatus(_A)
_Media13_ObjectIdentity=ObjectIdentity
media13=_Media13_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13))
class _Media13_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media13_name_Type.__name__=_E
_Media13_name_Object=MibScalar
media13_name=_Media13_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13,1),_Media13_name_Type())
media13_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media13_name.setStatus(_A)
class _Media13_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media13_short_name_Type.__name__=_E
_Media13_short_name_Object=MibScalar
media13_short_name=_Media13_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13,2),_Media13_short_name_Type())
media13_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media13_short_name.setStatus(_A)
_Media13_page_count_Type=Integer32
_Media13_page_count_Object=MibScalar
media13_page_count=_Media13_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13,3),_Media13_page_count_Type())
media13_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media13_page_count.setStatus(_A)
_Media13_engine_media_mode_Type=Integer32
_Media13_engine_media_mode_Object=MibScalar
media13_engine_media_mode=_Media13_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13,4),_Media13_engine_media_mode_Type())
media13_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media13_engine_media_mode.setStatus(_A)
_Media14_ObjectIdentity=ObjectIdentity
media14=_Media14_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14))
class _Media14_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media14_name_Type.__name__=_E
_Media14_name_Object=MibScalar
media14_name=_Media14_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14,1),_Media14_name_Type())
media14_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media14_name.setStatus(_A)
class _Media14_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media14_short_name_Type.__name__=_E
_Media14_short_name_Object=MibScalar
media14_short_name=_Media14_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14,2),_Media14_short_name_Type())
media14_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media14_short_name.setStatus(_A)
_Media14_page_count_Type=Integer32
_Media14_page_count_Object=MibScalar
media14_page_count=_Media14_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14,3),_Media14_page_count_Type())
media14_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media14_page_count.setStatus(_A)
_Media14_engine_media_mode_Type=Integer32
_Media14_engine_media_mode_Object=MibScalar
media14_engine_media_mode=_Media14_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14,4),_Media14_engine_media_mode_Type())
media14_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media14_engine_media_mode.setStatus(_A)
_Media15_ObjectIdentity=ObjectIdentity
media15=_Media15_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15))
class _Media15_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media15_name_Type.__name__=_E
_Media15_name_Object=MibScalar
media15_name=_Media15_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15,1),_Media15_name_Type())
media15_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media15_name.setStatus(_A)
class _Media15_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media15_short_name_Type.__name__=_E
_Media15_short_name_Object=MibScalar
media15_short_name=_Media15_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15,2),_Media15_short_name_Type())
media15_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media15_short_name.setStatus(_A)
_Media15_page_count_Type=Integer32
_Media15_page_count_Object=MibScalar
media15_page_count=_Media15_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15,3),_Media15_page_count_Type())
media15_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media15_page_count.setStatus(_A)
_Media15_engine_media_mode_Type=Integer32
_Media15_engine_media_mode_Object=MibScalar
media15_engine_media_mode=_Media15_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15,4),_Media15_engine_media_mode_Type())
media15_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media15_engine_media_mode.setStatus(_A)
_Media16_ObjectIdentity=ObjectIdentity
media16=_Media16_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,16))
class _Media16_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media16_name_Type.__name__=_E
_Media16_name_Object=MibScalar
media16_name=_Media16_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,16,1),_Media16_name_Type())
media16_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media16_name.setStatus(_A)
class _Media16_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media16_short_name_Type.__name__=_E
_Media16_short_name_Object=MibScalar
media16_short_name=_Media16_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,16,2),_Media16_short_name_Type())
media16_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media16_short_name.setStatus(_A)
_Media16_page_count_Type=Integer32
_Media16_page_count_Object=MibScalar
media16_page_count=_Media16_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,16,3),_Media16_page_count_Type())
media16_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media16_page_count.setStatus(_A)
_Media16_engine_media_mode_Type=Integer32
_Media16_engine_media_mode_Object=MibScalar
media16_engine_media_mode=_Media16_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,16,4),_Media16_engine_media_mode_Type())
media16_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media16_engine_media_mode.setStatus(_A)
_Media17_ObjectIdentity=ObjectIdentity
media17=_Media17_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,17))
class _Media17_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media17_name_Type.__name__=_E
_Media17_name_Object=MibScalar
media17_name=_Media17_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,17,1),_Media17_name_Type())
media17_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media17_name.setStatus(_A)
class _Media17_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media17_short_name_Type.__name__=_E
_Media17_short_name_Object=MibScalar
media17_short_name=_Media17_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,17,2),_Media17_short_name_Type())
media17_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media17_short_name.setStatus(_A)
_Media17_page_count_Type=Integer32
_Media17_page_count_Object=MibScalar
media17_page_count=_Media17_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,17,3),_Media17_page_count_Type())
media17_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media17_page_count.setStatus(_A)
_Media17_engine_media_mode_Type=Integer32
_Media17_engine_media_mode_Object=MibScalar
media17_engine_media_mode=_Media17_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,17,4),_Media17_engine_media_mode_Type())
media17_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media17_engine_media_mode.setStatus(_A)
_Media18_ObjectIdentity=ObjectIdentity
media18=_Media18_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,18))
class _Media18_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media18_name_Type.__name__=_E
_Media18_name_Object=MibScalar
media18_name=_Media18_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,18,1),_Media18_name_Type())
media18_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media18_name.setStatus(_A)
class _Media18_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media18_short_name_Type.__name__=_E
_Media18_short_name_Object=MibScalar
media18_short_name=_Media18_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,18,2),_Media18_short_name_Type())
media18_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media18_short_name.setStatus(_A)
_Media18_page_count_Type=Integer32
_Media18_page_count_Object=MibScalar
media18_page_count=_Media18_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,18,3),_Media18_page_count_Type())
media18_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media18_page_count.setStatus(_A)
_Media18_engine_media_mode_Type=Integer32
_Media18_engine_media_mode_Object=MibScalar
media18_engine_media_mode=_Media18_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,18,4),_Media18_engine_media_mode_Type())
media18_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media18_engine_media_mode.setStatus(_A)
_Media19_ObjectIdentity=ObjectIdentity
media19=_Media19_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,19))
class _Media19_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media19_name_Type.__name__=_E
_Media19_name_Object=MibScalar
media19_name=_Media19_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,19,1),_Media19_name_Type())
media19_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media19_name.setStatus(_A)
class _Media19_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media19_short_name_Type.__name__=_E
_Media19_short_name_Object=MibScalar
media19_short_name=_Media19_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,19,2),_Media19_short_name_Type())
media19_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media19_short_name.setStatus(_A)
_Media19_page_count_Type=Integer32
_Media19_page_count_Object=MibScalar
media19_page_count=_Media19_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,19,3),_Media19_page_count_Type())
media19_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media19_page_count.setStatus(_A)
_Media19_engine_media_mode_Type=Integer32
_Media19_engine_media_mode_Object=MibScalar
media19_engine_media_mode=_Media19_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,19,4),_Media19_engine_media_mode_Type())
media19_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media19_engine_media_mode.setStatus(_A)
_Media20_ObjectIdentity=ObjectIdentity
media20=_Media20_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,20))
class _Media20_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media20_name_Type.__name__=_E
_Media20_name_Object=MibScalar
media20_name=_Media20_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,20,1),_Media20_name_Type())
media20_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media20_name.setStatus(_A)
class _Media20_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media20_short_name_Type.__name__=_E
_Media20_short_name_Object=MibScalar
media20_short_name=_Media20_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,20,2),_Media20_short_name_Type())
media20_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media20_short_name.setStatus(_A)
_Media20_page_count_Type=Integer32
_Media20_page_count_Object=MibScalar
media20_page_count=_Media20_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,20,3),_Media20_page_count_Type())
media20_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media20_page_count.setStatus(_A)
_Media20_engine_media_mode_Type=Integer32
_Media20_engine_media_mode_Object=MibScalar
media20_engine_media_mode=_Media20_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,20,4),_Media20_engine_media_mode_Type())
media20_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media20_engine_media_mode.setStatus(_A)
_Media21_ObjectIdentity=ObjectIdentity
media21=_Media21_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,21))
class _Media21_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media21_name_Type.__name__=_E
_Media21_name_Object=MibScalar
media21_name=_Media21_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,21,1),_Media21_name_Type())
media21_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media21_name.setStatus(_A)
class _Media21_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media21_short_name_Type.__name__=_E
_Media21_short_name_Object=MibScalar
media21_short_name=_Media21_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,21,2),_Media21_short_name_Type())
media21_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media21_short_name.setStatus(_A)
_Media21_page_count_Type=Integer32
_Media21_page_count_Object=MibScalar
media21_page_count=_Media21_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,21,3),_Media21_page_count_Type())
media21_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media21_page_count.setStatus(_A)
_Media21_engine_media_mode_Type=Integer32
_Media21_engine_media_mode_Object=MibScalar
media21_engine_media_mode=_Media21_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,21,4),_Media21_engine_media_mode_Type())
media21_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media21_engine_media_mode.setStatus(_A)
_Media22_ObjectIdentity=ObjectIdentity
media22=_Media22_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,22))
class _Media22_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media22_name_Type.__name__=_E
_Media22_name_Object=MibScalar
media22_name=_Media22_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,22,1),_Media22_name_Type())
media22_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media22_name.setStatus(_A)
class _Media22_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media22_short_name_Type.__name__=_E
_Media22_short_name_Object=MibScalar
media22_short_name=_Media22_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,22,2),_Media22_short_name_Type())
media22_short_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media22_short_name.setStatus(_A)
_Media22_page_count_Type=Integer32
_Media22_page_count_Object=MibScalar
media22_page_count=_Media22_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,22,3),_Media22_page_count_Type())
media22_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media22_page_count.setStatus(_A)
_Media22_engine_media_mode_Type=Integer32
_Media22_engine_media_mode_Object=MibScalar
media22_engine_media_mode=_Media22_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,22,4),_Media22_engine_media_mode_Type())
media22_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media22_engine_media_mode.setStatus(_A)
_Media23_ObjectIdentity=ObjectIdentity
media23=_Media23_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,23))
class _Media23_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media23_name_Type.__name__=_E
_Media23_name_Object=MibScalar
media23_name=_Media23_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,23,1),_Media23_name_Type())
media23_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media23_name.setStatus(_A)
class _Media23_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media23_short_name_Type.__name__=_E
_Media23_short_name_Object=MibScalar
media23_short_name=_Media23_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,23,2),_Media23_short_name_Type())
media23_short_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media23_short_name.setStatus(_A)
_Media23_page_count_Type=Integer32
_Media23_page_count_Object=MibScalar
media23_page_count=_Media23_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,23,3),_Media23_page_count_Type())
media23_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media23_page_count.setStatus(_A)
_Media23_engine_media_mode_Type=Integer32
_Media23_engine_media_mode_Object=MibScalar
media23_engine_media_mode=_Media23_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,23,4),_Media23_engine_media_mode_Type())
media23_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media23_engine_media_mode.setStatus(_A)
_Media24_ObjectIdentity=ObjectIdentity
media24=_Media24_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,24))
class _Media24_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media24_name_Type.__name__=_E
_Media24_name_Object=MibScalar
media24_name=_Media24_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,24,1),_Media24_name_Type())
media24_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media24_name.setStatus(_A)
class _Media24_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media24_short_name_Type.__name__=_E
_Media24_short_name_Object=MibScalar
media24_short_name=_Media24_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,24,2),_Media24_short_name_Type())
media24_short_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media24_short_name.setStatus(_A)
_Media24_page_count_Type=Integer32
_Media24_page_count_Object=MibScalar
media24_page_count=_Media24_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,24,3),_Media24_page_count_Type())
media24_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media24_page_count.setStatus(_A)
_Media24_engine_media_mode_Type=Integer32
_Media24_engine_media_mode_Object=MibScalar
media24_engine_media_mode=_Media24_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,24,4),_Media24_engine_media_mode_Type())
media24_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media24_engine_media_mode.setStatus(_A)
_Media25_ObjectIdentity=ObjectIdentity
media25=_Media25_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,25))
class _Media25_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media25_name_Type.__name__=_E
_Media25_name_Object=MibScalar
media25_name=_Media25_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,25,1),_Media25_name_Type())
media25_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media25_name.setStatus(_A)
class _Media25_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media25_short_name_Type.__name__=_E
_Media25_short_name_Object=MibScalar
media25_short_name=_Media25_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,25,2),_Media25_short_name_Type())
media25_short_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media25_short_name.setStatus(_A)
_Media25_page_count_Type=Integer32
_Media25_page_count_Object=MibScalar
media25_page_count=_Media25_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,25,3),_Media25_page_count_Type())
media25_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media25_page_count.setStatus(_A)
_Media25_engine_media_mode_Type=Integer32
_Media25_engine_media_mode_Object=MibScalar
media25_engine_media_mode=_Media25_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,25,4),_Media25_engine_media_mode_Type())
media25_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media25_engine_media_mode.setStatus(_A)
_Media26_ObjectIdentity=ObjectIdentity
media26=_Media26_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,26))
class _Media26_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media26_name_Type.__name__=_E
_Media26_name_Object=MibScalar
media26_name=_Media26_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,26,1),_Media26_name_Type())
media26_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media26_name.setStatus(_A)
class _Media26_short_name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,9))
_Media26_short_name_Type.__name__=_E
_Media26_short_name_Object=MibScalar
media26_short_name=_Media26_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,26,2),_Media26_short_name_Type())
media26_short_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media26_short_name.setStatus(_A)
_Media26_page_count_Type=Integer32
_Media26_page_count_Object=MibScalar
media26_page_count=_Media26_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,26,3),_Media26_page_count_Type())
media26_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media26_page_count.setStatus(_A)
_Media26_engine_media_mode_Type=Integer32
_Media26_engine_media_mode_Object=MibScalar
media26_engine_media_mode=_Media26_engine_media_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,26,4),_Media26_engine_media_mode_Type())
media26_engine_media_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:media26_engine_media_mode.setStatus(_A)
_Media_modes_ObjectIdentity=ObjectIdentity
media_modes=_Media_modes_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,4))
_Engine_media_modes_supported1_Type=OctetString
_Engine_media_modes_supported1_Object=MibScalar
engine_media_modes_supported1=_Engine_media_modes_supported1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,4,1),_Engine_media_modes_supported1_Type())
engine_media_modes_supported1.setMaxAccess(_B)
if mibBuilder.loadTexts:engine_media_modes_supported1.setStatus(_A)
_Media_size_ObjectIdentity=ObjectIdentity
media_size=_Media_size_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,5))
_Media_size_count_Type=Integer32
_Media_size_count_Object=MibScalar
media_size_count=_Media_size_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,5,1),_Media_size_count_Type())
media_size_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media_size_count.setStatus(_A)
_Media_size_west_edge_first_side_offset_Type=Integer32
_Media_size_west_edge_first_side_offset_Object=MibScalar
media_size_west_edge_first_side_offset=_Media_size_west_edge_first_side_offset_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,5,2),_Media_size_west_edge_first_side_offset_Type())
media_size_west_edge_first_side_offset.setMaxAccess(_C)
if mibBuilder.loadTexts:media_size_west_edge_first_side_offset.setStatus(_A)
_Media_size_west_edge_second_side_offset_Type=Integer32
_Media_size_west_edge_second_side_offset_Object=MibScalar
media_size_west_edge_second_side_offset=_Media_size_west_edge_second_side_offset_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,5,3),_Media_size_west_edge_second_side_offset_Type())
media_size_west_edge_second_side_offset.setMaxAccess(_C)
if mibBuilder.loadTexts:media_size_west_edge_second_side_offset.setStatus(_A)
_Media_size_west_edge_side_offset_by_tray_Type=Integer32
_Media_size_west_edge_side_offset_by_tray_Object=MibScalar
media_size_west_edge_side_offset_by_tray=_Media_size_west_edge_side_offset_by_tray_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,5,4),_Media_size_west_edge_side_offset_by_tray_Type())
media_size_west_edge_side_offset_by_tray.setMaxAccess(_C)
if mibBuilder.loadTexts:media_size_west_edge_side_offset_by_tray.setStatus(_A)
_Media_counts_ObjectIdentity=ObjectIdentity
media_counts=_Media_counts_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,7))
_Non_assured_oht_page_count_Type=Integer32
_Non_assured_oht_page_count_Object=MibScalar
non_assured_oht_page_count=_Non_assured_oht_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,7,1),_Non_assured_oht_page_count_Type())
non_assured_oht_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:non_assured_oht_page_count.setStatus(_A)
_Media_types_ObjectIdentity=ObjectIdentity
media_types=_Media_types_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,8))
_Media_number_of_type_supported_Type=Integer32
_Media_number_of_type_supported_Object=MibScalar
media_number_of_type_supported=_Media_number_of_type_supported_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,8,1),_Media_number_of_type_supported_Type())
media_number_of_type_supported.setMaxAccess(_B)
if mibBuilder.loadTexts:media_number_of_type_supported.setStatus(_A)
_Consumables_ObjectIdentity=ObjectIdentity
consumables=_Consumables_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10))
_Consumables_1_ObjectIdentity=ObjectIdentity
consumables_1=_Consumables_1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1))
_Consumable_status_ObjectIdentity=ObjectIdentity
consumable_status=_Consumable_status_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1))
_Consumable_status_web_service_access_data_Type=Integer32
_Consumable_status_web_service_access_data_Object=MibScalar
consumable_status_web_service_access_data=_Consumable_status_web_service_access_data_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1,75),_Consumable_status_web_service_access_data_Type())
consumable_status_web_service_access_data.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_status_web_service_access_data.setStatus(_A)
_Consumable_status_web_service_access_control_Type=OctetString
_Consumable_status_web_service_access_control_Object=MibScalar
consumable_status_web_service_access_control=_Consumable_status_web_service_access_control_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1,76),_Consumable_status_web_service_access_control_Type())
consumable_status_web_service_access_control.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_status_web_service_access_control.setStatus(_A)
class _Consumable_reorder_url_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Consumable_reorder_url_Type.__name__=_E
_Consumable_reorder_url_Object=MibScalar
consumable_reorder_url=_Consumable_reorder_url_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,2),_Consumable_reorder_url_Type())
consumable_reorder_url.setMaxAccess(_C)
if mibBuilder.loadTexts:consumable_reorder_url.setStatus(_A)
_Consumables_status_ObjectIdentity=ObjectIdentity
consumables_status=_Consumables_status_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,5))
_Consumables_life_ObjectIdentity=ObjectIdentity
consumables_life=_Consumables_life_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,5,1))
_Consumable_life_usage_units_remaining_Type=Integer32
_Consumable_life_usage_units_remaining_Object=MibScalar
consumable_life_usage_units_remaining=_Consumable_life_usage_units_remaining_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,5,1,1),_Consumable_life_usage_units_remaining_Type())
consumable_life_usage_units_remaining.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_life_usage_units_remaining.setStatus(_A)
class _Consumable_life_usage_units_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ePagesRemaining',1),('eEstimatedPagesRemaining',2)))
_Consumable_life_usage_units_Type.__name__=_D
_Consumable_life_usage_units_Object=MibScalar
consumable_life_usage_units=_Consumable_life_usage_units_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,5,1,2),_Consumable_life_usage_units_Type())
consumable_life_usage_units.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_life_usage_units.setStatus(_A)
_Consumable_life_low_threshold_Type=Integer32
_Consumable_life_low_threshold_Object=MibScalar
consumable_life_low_threshold=_Consumable_life_low_threshold_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,5,1,3),_Consumable_life_low_threshold_Type())
consumable_life_low_threshold.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_life_low_threshold.setStatus(_A)
_Consumable_current_state_Type=OctetString
_Consumable_current_state_Object=MibScalar
consumable_current_state=_Consumable_current_state_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,7),_Consumable_current_state_Type())
consumable_current_state.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_current_state.setStatus(_A)
_Consumable_string_ObjectIdentity=ObjectIdentity
consumable_string=_Consumable_string_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,8))
class _Consumable_string_information_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,287))
_Consumable_string_information_Type.__name__=_E
_Consumable_string_information_Object=MibScalar
consumable_string_information=_Consumable_string_information_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,8,1),_Consumable_string_information_Type())
consumable_string_information.setMaxAccess(_C)
if mibBuilder.loadTexts:consumable_string_information.setStatus(_A)
class _Consumable_string_information_reset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ePresetToNVRAM',1))
_Consumable_string_information_reset_Type.__name__=_D
_Consumable_string_information_reset_Object=MibScalar
consumable_string_information_reset=_Consumable_string_information_reset_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,8,2),_Consumable_string_information_reset_Type())
consumable_string_information_reset.setMaxAccess(_C)
if mibBuilder.loadTexts:consumable_string_information_reset.setStatus(_A)
_Consumable_notification_status_Type=OctetString
_Consumable_notification_status_Object=MibScalar
consumable_notification_status=_Consumable_notification_status_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,10),_Consumable_notification_status_Type())
consumable_notification_status.setMaxAccess(_C)
if mibBuilder.loadTexts:consumable_notification_status.setStatus(_A)
_Consumable_pages_printed_with_supply_Type=Integer32
_Consumable_pages_printed_with_supply_Object=MibScalar
consumable_pages_printed_with_supply=_Consumable_pages_printed_with_supply_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,11),_Consumable_pages_printed_with_supply_Type())
consumable_pages_printed_with_supply.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_pages_printed_with_supply.setStatus(_A)
class _Supply_override_activated_level_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eHasNotBeenActivated',1),('eLevel01',2)))
_Supply_override_activated_level_Type.__name__=_D
_Supply_override_activated_level_Object=MibScalar
supply_override_activated_level=_Supply_override_activated_level_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,12),_Supply_override_activated_level_Type())
supply_override_activated_level.setMaxAccess(_B)
if mibBuilder.loadTexts:supply_override_activated_level.setStatus(_A)
_Supply_override_activated_pagecount_Type=Integer32
_Supply_override_activated_pagecount_Object=MibScalar
supply_override_activated_pagecount=_Supply_override_activated_pagecount_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,13),_Supply_override_activated_pagecount_Type())
supply_override_activated_pagecount.setMaxAccess(_B)
if mibBuilder.loadTexts:supply_override_activated_pagecount.setStatus(_A)
_Supply_override_activated_date_Type=OctetString
_Supply_override_activated_date_Object=MibScalar
supply_override_activated_date=_Supply_override_activated_date_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,14),_Supply_override_activated_date_Type())
supply_override_activated_date.setMaxAccess(_B)
if mibBuilder.loadTexts:supply_override_activated_date.setStatus(_A)
_Print_meter_ObjectIdentity=ObjectIdentity
print_meter=_Print_meter_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,11))
_Printer_average_ObjectIdentity=ObjectIdentity
printer_average=_Printer_average_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,11,1))
_Printer_average_marking_agent_coverage_Type=OctetString
_Printer_average_marking_agent_coverage_Object=MibScalar
printer_average_marking_agent_coverage=_Printer_average_marking_agent_coverage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,11,1,1),_Printer_average_marking_agent_coverage_Type())
printer_average_marking_agent_coverage.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_average_marking_agent_coverage.setStatus(_A)
_Printer_average_marking_agent_coverage_sum_Type=OctetString
_Printer_average_marking_agent_coverage_sum_Object=MibScalar
printer_average_marking_agent_coverage_sum=_Printer_average_marking_agent_coverage_sum_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,11,1,2),_Printer_average_marking_agent_coverage_sum_Type())
printer_average_marking_agent_coverage_sum.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_average_marking_agent_coverage_sum.setStatus(_A)
_Printer_average_marking_agent_coverage_sum_squared_Type=OctetString
_Printer_average_marking_agent_coverage_sum_squared_Object=MibScalar
printer_average_marking_agent_coverage_sum_squared=_Printer_average_marking_agent_coverage_sum_squared_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,11,1,3),_Printer_average_marking_agent_coverage_sum_squared_Type())
printer_average_marking_agent_coverage_sum_squared.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_average_marking_agent_coverage_sum_squared.setStatus(_A)
_Printer_average_marking_agent_units_per_gram_Type=OctetString
_Printer_average_marking_agent_units_per_gram_Object=MibScalar
printer_average_marking_agent_units_per_gram=_Printer_average_marking_agent_units_per_gram_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,11,1,4),_Printer_average_marking_agent_units_per_gram_Type())
printer_average_marking_agent_units_per_gram.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_average_marking_agent_units_per_gram.setStatus(_A)
_Printer_average_marking_agent_coverage_actual_Type=OctetString
_Printer_average_marking_agent_coverage_actual_Object=MibScalar
printer_average_marking_agent_coverage_actual=_Printer_average_marking_agent_coverage_actual_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,11,1,5),_Printer_average_marking_agent_coverage_actual_Type())
printer_average_marking_agent_coverage_actual.setMaxAccess(_B)
if mibBuilder.loadTexts:printer_average_marking_agent_coverage_actual.setStatus(_A)
_Menus_ObjectIdentity=ObjectIdentity
menus=_Menus_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,13))
_Tables_ObjectIdentity=ObjectIdentity
tables=_Tables_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,7))
mibBuilder.exportSymbols('LJ3505-MIB',**{_m:DisplayString,'hp':hp,'dm':dm,'device':device,'device-system':device_system,'settings-system':settings_system,'energy-star':energy_star,'sleep-mode':sleep_mode,'date-display':date_display,'mono-color-switching-mode':mono_color_switching_mode,'device-configure':device_configure,'device-configure-printer-parameters':device_configure_printer_parameters,'color-supply-out-action':color_supply_out_action,'direct-connect-ports-enable':direct_connect_ports_enable,'control-panel-supplies-status-message':control_panel_supplies_status_message,'speed-energy-usage':speed_energy_usage,'calibration-data-reset':calibration_data_reset,'status-system':status_system,'on-off-line':on_off_line,'continue':_pysmi_continue,'auto-continue':auto_continue,'install-date':install_date,'perm-store-init-occurred':perm_store_init_occurred,'date-and-time':date_and_time,'service-id':service_id,'display':display,'display-status':display_status,'show-address':show_address,'time-display':time_display,'job-input-auto-continue-timeout':job_input_auto_continue_timeout,'job-input-auto-continue-mode':job_input_auto_continue_mode,'background-message':background_message,'background-message1':background_message1,'background-status-msg-line1-part1':background_status_msg_line1_part1,'background-message2':background_message2,'background-status-msg-line2-part1':background_status_msg_line2_part1,'error-log-clear':error_log_clear,'job-output-auto-continue-timeout':job_output_auto_continue_timeout,'collated-originals-support':collated_originals_support,'localization-languages-supported':localization_languages_supported,'localization-countries-supported':localization_countries_supported,'host-application-available-memory':host_application_available_memory,'control-panel-button-press':control_panel_button_press,'control-panel-display-contents-change-counter':control_panel_display_contents_change_counter,'control-panel-display-contents-crc':control_panel_display_contents_crc,'control-panel-display':control_panel_display,'control-panel-display-graphical-contents':control_panel_display_graphical_contents,'page-frame-memory-available':page_frame_memory_available,'id':id,'model-number':model_number,'model-name':model_name,'serial-number':serial_number,'fw-rom-datecode':fw_rom_datecode,'fw-rom-revision':fw_rom_revision,'device-name':device_name,'device-location':device_location,'asset-number':asset_number,'formatter-serial-number':formatter_serial_number,'interface':interface,'simm':simm,'simm1':simm1,'simm1-type':simm1_type,'simm1-capacity':simm1_capacity,'simm1-bank':simm1_bank,'simm1-bank1':simm1_bank1,'simm1-bank1-type':simm1_bank1_type,'simm1-bank1-capacity':simm1_bank1_capacity,'simm1-bank2':simm1_bank2,'simm1-bank2-type':simm1_bank2_type,'simm1-bank2-capacity':simm1_bank2_capacity,'simm2':simm2,'simm2-type':simm2_type,'simm2-capacity':simm2_capacity,'simm2-bank':simm2_bank,'simm2-bank1':simm2_bank1,'simm2-bank1-type':simm2_bank1_type,'simm2-bank1-capacity':simm2_bank1_capacity,'simm2-bank2':simm2_bank2,'simm2-bank2-type':simm2_bank2_type,'simm2-bank2-capacity':simm2_bank2_capacity,'simm3':simm3,'simm3-type':simm3_type,'simm3-capacity':simm3_capacity,'simm3-bank':simm3_bank,'simm3-bank1':simm3_bank1,'simm3-bank1-type':simm3_bank1_type,'simm3-bank1-capacity':simm3_bank1_capacity,'simm3-bank2':simm3_bank2,'simm3-bank2-type':simm3_bank2_type,'simm3-bank2-capacity':simm3_bank2_capacity,'simm4':simm4,'simm4-type':simm4_type,'simm4-capacity':simm4_capacity,'simm4-bank':simm4_bank,'simm4-bank1':simm4_bank1,'simm4-bank1-type':simm4_bank1_type,'simm4-bank1-capacity':simm4_bank1_capacity,'simm4-bank2':simm4_bank2,'simm4-bank2-type':simm4_bank2_type,'simm4-bank2-capacity':simm4_bank2_capacity,'simm5':simm5,'simm5-type':simm5_type,'simm5-capacity':simm5_capacity,'simm5-bank':simm5_bank,'simm5-bank1':simm5_bank1,'simm5-bank1-type':simm5_bank1_type,'simm5-bank1-capacity':simm5_bank1_capacity,'simm5-bank2':simm5_bank2,'simm5-bank2-type':simm5_bank2_type,'simm5-bank2-capacity':simm5_bank2_capacity,'mio':mio,'mio1':mio1,'mio1-model-name':mio1_model_name,'mio1-manufacturing-info':mio1_manufacturing_info,'mio1-type':mio1_type,'mio1-ip-address':mio1_ip_address,'mio4':mio4,'mio4-model-name':mio4_model_name,'mio4-manufacturing-info':mio4_manufacturing_info,'mio4-type':mio4_type,'mio4-ip-address':mio4_ip_address,'web-server':web_server,'settings-web-server':settings_web_server,'ews-request-control-panel-supplies-status':ews_request_control_panel_supplies_status,'usb-interface':usb_interface,'usb-host-supported':usb_host_supported,'usb':usb,'usb-serial-number':usb_serial_number,'usb-manufacturer-name':usb_manufacturer_name,'usb-product-description':usb_product_description,'usb-vendor-id':usb_vendor_id,'usb-product-id':usb_product_id,'usb-device-kind':usb_device_kind,'usb-driver-name':usb_driver_name,'test':test,'print-internal-page':print_internal_page,'engine-self-diagnostic':engine_self_diagnostic,'engine-parameter':engine_parameter,'job':job,'settings-job':settings_job,'clearable-warning':clearable_warning,'cancel-job':cancel_job,'job-info-change-id':job_info_change_id,'hold-job-timeout':hold_job_timeout,'active-print-jobs':active_print_jobs,'job-being-parsed':job_being_parsed,'current-job-parsing-id':current_job_parsing_id,'job-info':job_info,'job-info-name1':job_info_name1,'job-info-name2':job_info_name2,'job-info-stage':job_info_stage,'job-info-io-source':job_info_io_source,'job-info-pages-processed':job_info_pages_processed,'job-info-pages-printed':job_info_pages_printed,'job-info-size':job_info_size,'job-info-state':job_info_state,'job-info-outcome':job_info_outcome,'job-info-outbins-used':job_info_outbins_used,'job-info-physical-outbins-used':job_info_physical_outbins_used,'job-info-attribute':job_info_attribute,'job-info-attr-1':job_info_attr_1,'job-info-attr-2':job_info_attr_2,'job-info-attr-3':job_info_attr_3,'job-info-attr-4':job_info_attr_4,'job-info-attr-5':job_info_attr_5,'job-info-attr-6':job_info_attr_6,'job-info-attr-7':job_info_attr_7,'job-info-attr-8':job_info_attr_8,'job-info-attr-9':job_info_attr_9,'job-info-attr-10':job_info_attr_10,'job-info-attr-11':job_info_attr_11,'job-info-attr-12':job_info_attr_12,'job-info-attr-13':job_info_attr_13,'job-info-attr-14':job_info_attr_14,'job-info-attr-15':job_info_attr_15,'job-info-attr-16':job_info_attr_16,'job-info-requested-originals':job_info_requested_originals,'job-info-page-count-current-original':job_info_page_count_current_original,'job-info-pages-in-original':job_info_pages_in_original,'job-info-printed-originals':job_info_printed_originals,'job-info-accounting':job_info_accounting,'job-info-accounting-media-size':job_info_accounting_media_size,'job-info-accounting-media-type':job_info_accounting_media_type,'job-info-accounting-finishing-options':job_info_accounting_finishing_options,'job-info-accounting-media-simplex-count':job_info_accounting_media_simplex_count,'job-info-accounting-media-duplex-count':job_info_accounting_media_duplex_count,'job-info-accounting-grayscale-impression-count':job_info_accounting_grayscale_impression_count,'job-info-accounting-color-impression-count':job_info_accounting_color_impression_count,'job-info-accounting-black-dots':job_info_accounting_black_dots,'job-info-accounting-yellow-dots':job_info_accounting_yellow_dots,'job-info-accounting-cyan-dots':job_info_accounting_cyan_dots,'job-info-accounting-magenta-dots':job_info_accounting_magenta_dots,'job-info-accounting-job-type':job_info_accounting_job_type,'job-info-accounting-color-usage-log':job_info_accounting_color_usage_log,'held-job':held_job,'held-job-info':held_job_info,'held-job-user-name':held_job_user_name,'held-job-job-name':held_job_job_name,'held-job-retention':held_job_retention,'held-job-security':held_job_security,'held-job-quantity':held_job_quantity,'held-job-pin':held_job_pin,'held-job-control':held_job_control,'held-job-print':held_job_print,'held-job-delete':held_job_delete,'held-job-set-queue-size':held_job_set_queue_size,'held-job-enable':held_job_enable,'file-system':file_system,'settings-file-system':settings_file_system,'file-system-max-open-files':file_system_max_open_files,'file-system-set-system-partition-writeable':file_system_set_system_partition_writeable,'file-system-set-system-partition-readonly':file_system_set_system_partition_readonly,'file-system-delete-files':file_system_delete_files,'file-system-external-access-capabilities':file_system_external_access_capabilities,'file-system-erase-mode':file_system_erase_mode,'file-system-wipe-disk':file_system_wipe_disk,'file-system-wipe-disk-status':file_system_wipe_disk_status,'file-systems':file_systems,'file-system2':file_system2,'file-system2-initialize-volume':file_system2_initialize_volume,'file-system3':file_system3,'file-system3-initialize-volume':file_system3_initialize_volume,'file-system4':file_system4,'file-system4-initialize-volume':file_system4_initialize_volume,'errorlog':errorlog,'error1':error1,'error1-time-stamp':error1_time_stamp,'error1-code':error1_code,'error1-date-time':error1_date_time,'error2':error2,'error2-time-stamp':error2_time_stamp,'error2-code':error2_code,'error2-date-time':error2_date_time,'error3':error3,'error3-time-stamp':error3_time_stamp,'error3-code':error3_code,'error3-date-time':error3_date_time,'error4':error4,'error4-time-stamp':error4_time_stamp,'error4-code':error4_code,'error4-date-time':error4_date_time,'error5':error5,'error5-time-stamp':error5_time_stamp,'error5-code':error5_code,'error5-date-time':error5_date_time,'error6':error6,'error6-time-stamp':error6_time_stamp,'error6-code':error6_code,'error6-date-time':error6_date_time,'error7':error7,'error7-time-stamp':error7_time_stamp,'error7-code':error7_code,'error7-date-time':error7_date_time,'error8':error8,'error8-time-stamp':error8_time_stamp,'error8-code':error8_code,'error8-date-time':error8_date_time,'error9':error9,'error9-time-stamp':error9_time_stamp,'error9-code':error9_code,'error9-date-time':error9_date_time,'error10':error10,'error10-time-stamp':error10_time_stamp,'error10-code':error10_code,'error10-date-time':error10_date_time,'error11':error11,'error11-time-stamp':error11_time_stamp,'error11-code':error11_code,'error11-date-time':error11_date_time,'error12':error12,'error12-time-stamp':error12_time_stamp,'error12-code':error12_code,'error12-date-time':error12_date_time,'error13':error13,'error13-time-stamp':error13_time_stamp,'error13-code':error13_code,'error13-date-time':error13_date_time,'error14':error14,'error14-time-stamp':error14_time_stamp,'error14-code':error14_code,'error14-date-time':error14_date_time,'error15':error15,'error15-time-stamp':error15_time_stamp,'error15-code':error15_code,'error15-date-time':error15_date_time,'error16':error16,'error16-time-stamp':error16_time_stamp,'error16-code':error16_code,'error16-date-time':error16_date_time,'error17':error17,'error17-time-stamp':error17_time_stamp,'error17-code':error17_code,'error17-date-time':error17_date_time,'error18':error18,'error18-time-stamp':error18_time_stamp,'error18-code':error18_code,'error18-date-time':error18_date_time,'error19':error19,'error19-time-stamp':error19_time_stamp,'error19-code':error19_code,'error19-date-time':error19_date_time,'error20':error20,'error20-time-stamp':error20_time_stamp,'error20-code':error20_code,'error20-date-time':error20_date_time,'error21':error21,'error21-time-stamp':error21_time_stamp,'error21-code':error21_code,'error21-date-time':error21_date_time,'error22':error22,'error22-time-stamp':error22_time_stamp,'error22-code':error22_code,'error22-date-time':error22_date_time,'error23':error23,'error23-time-stamp':error23_time_stamp,'error23-code':error23_code,'error23-date-time':error23_date_time,'error24':error24,'error24-time-stamp':error24_time_stamp,'error24-code':error24_code,'error24-date-time':error24_date_time,'error25':error25,'error25-time-stamp':error25_time_stamp,'error25-code':error25_code,'error25-date-time':error25_date_time,'error26':error26,'error26-time-stamp':error26_time_stamp,'error26-code':error26_code,'error26-date-time':error26_date_time,'error27':error27,'error27-time-stamp':error27_time_stamp,'error27-code':error27_code,'error27-date-time':error27_date_time,'error28':error28,'error28-time-stamp':error28_time_stamp,'error28-code':error28_code,'error28-date-time':error28_date_time,'error29':error29,'error29-time-stamp':error29_time_stamp,'error29-code':error29_code,'error29-date-time':error29_date_time,'error30':error30,'error30-time-stamp':error30_time_stamp,'error30-code':error30_code,'error30-date-time':error30_date_time,'error31':error31,'error31-time-stamp':error31_time_stamp,'error31-code':error31_code,'error31-date-time':error31_date_time,'error32':error32,'error32-time-stamp':error32_time_stamp,'error32-code':error32_code,'error32-date-time':error32_date_time,'error33':error33,'error33-time-stamp':error33_time_stamp,'error33-code':error33_code,'error33-date-time':error33_date_time,'error34':error34,'error34-time-stamp':error34_time_stamp,'error34-code':error34_code,'error34-date-time':error34_date_time,'error35':error35,'error35-time-stamp':error35_time_stamp,'error35-code':error35_code,'error35-date-time':error35_date_time,'error36':error36,'error36-time-stamp':error36_time_stamp,'error36-code':error36_code,'error36-date-time':error36_date_time,'error37':error37,'error37-time-stamp':error37_time_stamp,'error37-code':error37_code,'error37-date-time':error37_date_time,'error38':error38,'error38-time-stamp':error38_time_stamp,'error38-code':error38_code,'error38-date-time':error38_date_time,'error39':error39,'error39-time-stamp':error39_time_stamp,'error39-code':error39_code,'error39-date-time':error39_date_time,'error40':error40,'error40-time-stamp':error40_time_stamp,'error40-code':error40_code,'error40-date-time':error40_date_time,'error41':error41,'error41-time-stamp':error41_time_stamp,'error41-code':error41_code,'error41-date-time':error41_date_time,'error42':error42,'error42-time-stamp':error42_time_stamp,'error42-code':error42_code,'error42-date-time':error42_date_time,'error43':error43,'error43-time-stamp':error43_time_stamp,'error43-code':error43_code,'error43-date-time':error43_date_time,'error44':error44,'error44-time-stamp':error44_time_stamp,'error44-code':error44_code,'error44-date-time':error44_date_time,'error45':error45,'error45-time-stamp':error45_time_stamp,'error45-code':error45_code,'error45-date-time':error45_date_time,'error46':error46,'error46-time-stamp':error46_time_stamp,'error46-code':error46_code,'error46-date-time':error46_date_time,'error47':error47,'error47-time-stamp':error47_time_stamp,'error47-code':error47_code,'error47-date-time':error47_date_time,'error48':error48,'error48-time-stamp':error48_time_stamp,'error48-code':error48_code,'error48-date-time':error48_date_time,'error49':error49,'error49-time-stamp':error49_time_stamp,'error49-code':error49_code,'error49-date-time':error49_date_time,'error50':error50,'error50-time-stamp':error50_time_stamp,'error50-code':error50_code,'error50-date-time':error50_date_time,'resource-manager':resource_manager,'mass-storage-resources':mass_storage_resources,'mass-storage-resource-change-counter':mass_storage_resource_change_counter,'mass-storage-resource-changed':mass_storage_resource_changed,'remote-procedure-call':remote_procedure_call,'settings-rpc':settings_rpc,'rpc-bind-protocol-address':rpc_bind_protocol_address,'status-rpc':status_rpc,'rpc-bound-protocol-address':rpc_bound_protocol_address,'mass-storage-block-driver':mass_storage_block_driver,'settings-mass-storage-bd':settings_mass_storage_bd,'ram-disk-mode':ram_disk_mode,'ram-disk-size':ram_disk_size,'status-mass-storage-bd':status_mass_storage_bd,'maximum-ram-disk-memory':maximum_ram_disk_memory,'accounting':accounting,'printer-accounting':printer_accounting,'printed-media-usage':printed_media_usage,'printed-media-simplex-count':printed_media_simplex_count,'printed-media-simplex-charge':printed_media_simplex_charge,'printed-media-duplex-count':printed_media_duplex_count,'printed-media-duplex-charge':printed_media_duplex_charge,'printed-media-total-charge':printed_media_total_charge,'printed-media-maximum-pixels-per-page':printed_media_maximum_pixels_per_page,'printed-media-combined-total':printed_media_combined_total,'printed-media-dimplex-count':printed_media_dimplex_count,'usage-printer-total-charge':usage_printer_total_charge,'usage-average-toner-coverage':usage_average_toner_coverage,'usage-staple-count':usage_staple_count,'usage-instructions-line1':usage_instructions_line1,'usage-instructions-line2':usage_instructions_line2,'usage-instructions-line3':usage_instructions_line3,'usage-instructions-line4':usage_instructions_line4,'printed-modes-usage-total':printed_modes_usage_total,'source-tray-usage-total':source_tray_usage_total,'destination-bin-usage-total':destination_bin_usage_total,'usage-printer-mono-total-charge':usage_printer_mono_total_charge,'usage-printer-color-total-charge':usage_printer_color_total_charge,'printer-color-accounting':printer_color_accounting,'printed-media-color-usage':printed_media_color_usage,'printed-media-color-simplex-count':printed_media_color_simplex_count,'printed-media-color-duplex-count':printed_media_color_duplex_count,'printed-media-color-total-count':printed_media_color_total_count,'printed-media-color-dimplex-count':printed_media_color_dimplex_count,'printed-modes-accounting':printed_modes_accounting,'printed-modes-usage':printed_modes_usage,'printed-modes-mono-count':printed_modes_mono_count,'printed-modes-color-count':printed_modes_color_count,'printed-modes-total-count':printed_modes_total_count,'source-tray-accounting':source_tray_accounting,'source-tray-usage':source_tray_usage,'source-tray-usage-count':source_tray_usage_count,'destination-bin-accounting':destination_bin_accounting,'destination-bin-usage':destination_bin_usage,'destination-bin-usage-count':destination_bin_usage_count,'firmware-download':firmware_download,'firmware-download-write-status-supported':firmware_download_write_status_supported,'firmware-download-write-time':firmware_download_write_time,'firmware-download-current-state':firmware_download_current_state,'firmware-download-name':firmware_download_name,'firmware-download-version':firmware_download_version,'operating-system':operating_system,'os-execute-file':os_execute_file,'upgradable-devices':upgradable_devices,'upgradable-devices-write-status-supported':upgradable_devices_write_status_supported,'upgradable-devices-write-time':upgradable_devices_write_time,'upgradable-devices-current-state':upgradable_devices_current_state,'upgradable-devices-name':upgradable_devices_name,'upgradable-devices-version':upgradable_devices_version,'remote-upgrade-enable':remote_upgrade_enable,'source-subsystem':source_subsystem,'io':io,'settings-io':settings_io,'io-timeout':io_timeout,'io-switch':io_switch,'ports':ports,'port1':port1,'port1-parallel-speed':port1_parallel_speed,'port1-parallel-bidirectionality':port1_parallel_bidirectionality,'spooler':spooler,'settings-spooler':settings_spooler,'mopy-mode':mopy_mode,'processing-subsystem':processing_subsystem,'pdl':pdl,'settings-pdl':settings_pdl,'default-copies':default_copies,'form-feed':form_feed,'default-vertical-black-resolution':default_vertical_black_resolution,'default-horizontal-black-resolution':default_horizontal_black_resolution,'default-page-protect':default_page_protect,'default-lines-per-page':default_lines_per_page,'default-vmi':default_vmi,'default-media-size':default_media_size,'cold-reset-media-size':cold_reset_media_size,'default-media-name':default_media_name,'reprint':reprint,'default-bits-per-pixel':default_bits_per_pixel,'status-pdl':status_pdl,'form-feed-needed':form_feed_needed,'pdl-pcl':pdl_pcl,'pcl-total-page-count':pcl_total_page_count,'pcl-default-font-height':pcl_default_font_height,'pcl-default-font-source':pcl_default_font_source,'pcl-default-font-number':pcl_default_font_number,'pcl-default-font-width':pcl_default_font_width,'pdl-postscript':pdl_postscript,'postscript-total-page-count':postscript_total_page_count,'postscript-print-errors':postscript_print_errors,'pdl-pdf':pdl_pdf,'pdf-print-errors':pdf_print_errors,'pml':pml,'pjl':pjl,'webserver-proc-sub':webserver_proc_sub,'settings-webserver':settings_webserver,'web-server-url':web_server_url,'web-server-security':web_server_security,'destination-subsystem':destination_subsystem,'print-engine':print_engine,'settings-prt-eng':settings_prt_eng,'override-media-name':override_media_name,'override-media-size':override_media_size,'marking-agent-density':marking_agent_density,'marking-agent-highlights-density-setting':marking_agent_highlights_density_setting,'marking-agent-midtones-density-setting':marking_agent_midtones_density_setting,'marking-agent-shadows-density-setting':marking_agent_shadows_density_setting,'autocleaning-page-frequency':autocleaning_page_frequency,'autocleaning-page-size':autocleaning_page_size,'calibration-power-on-delay':calibration_power_on_delay,'configurable-low-threshold-setting':configurable_low_threshold_setting,'supplies-replace-action-at-setting':supplies_replace_action_at_setting,'supply-out-user-configured-override-limit':supply_out_user_configured_override_limit,'cartridge-out-override-control':cartridge_out_override_control,'duplex-blank-pages':duplex_blank_pages,'supply-out-user-configured-override2-limit':supply_out_user_configured_override2_limit,'status-prt-eng':status_prt_eng,'total-color-page-count':total_color_page_count,'duplex-page-count':duplex_page_count,'print-engine-revision':print_engine_revision,'printer-calibration-dhalf':printer_calibration_dhalf,'printer-cal-dhalf-page-count':printer_cal_dhalf_page_count,'printer-cal-dhalf-utc':printer_cal_dhalf_utc,'printer-cal-dhalf-data':printer_cal_dhalf_data,'printer-cal-dhalf-data1':printer_cal_dhalf_data1,'printer-cal-dhalf-data2':printer_cal_dhalf_data2,'printer-cal-grayaxis-count':printer_cal_grayaxis_count,'printer-cal-grayaxis-utc':printer_cal_grayaxis_utc,'printer-cal-grayaxis':printer_cal_grayaxis,'printer-cal-grayaxis-tray':printer_cal_grayaxis_tray,'printer-cal-grayaxis-media':printer_cal_grayaxis_media,'printer-cal-grayaxis-xsize':printer_cal_grayaxis_xsize,'printer-cal-grayaxis-ysize':printer_cal_grayaxis_ysize,'printer-cal-grayaxis-data':printer_cal_grayaxis_data,'printer-cal-grayaxis-data1':printer_cal_grayaxis_data1,'printer-cal-grayaxis-data2':printer_cal_grayaxis_data2,'printer-calibration-cpr':printer_calibration_cpr,'printer-cal-cpr-page-count':printer_cal_cpr_page_count,'printer-cal-cpr-utc':printer_cal_cpr_utc,'printer-cal-cpr-data':printer_cal_cpr_data,'supply-out-action-support':supply_out_action_support,'supply-out-device-state':supply_out_device_state,'supply-after-out-state':supply_after_out_state,'intray':intray,'settings-intray':settings_intray,'input-tray-auto-select':input_tray_auto_select,'custom-paper-feed-dim':custom_paper_feed_dim,'custom-paper-xfeed-dim':custom_paper_xfeed_dim,'default-custom-paper-dim-unit':default_custom_paper_dim_unit,'default-custom-paper-feed-dim':default_custom_paper_feed_dim,'default-custom-paper-xfeed-dim':default_custom_paper_xfeed_dim,'input-tray-max-media-feed-dim':input_tray_max_media_feed_dim,'input-tray-max-media-xfeed-dim':input_tray_max_media_xfeed_dim,'input-tray-min-media-feed-dim':input_tray_min_media_feed_dim,'input-tray-min-media-xfeed-dim':input_tray_min_media_xfeed_dim,'tray-prompt':tray_prompt,'intrays':intrays,'intray1':intray1,'tray1-media-size-loaded':tray1_media_size_loaded,'tray1-phd':tray1_phd,'intray2':intray2,'tray2-media-size-loaded':tray2_media_size_loaded,'tray2-phd':tray2_phd,'intray3':intray3,'tray3-media-size-loaded':tray3_media_size_loaded,'tray3-phd':tray3_phd,'outbin':outbin,'settings-outbin':settings_outbin,'overflow-bin':overflow_bin,'outbins':outbins,'outbin1':outbin1,'outbin1-override-mode':outbin1_override_mode,'marking-agent':marking_agent,'settings-marking-agent':settings_marking_agent,'marker-density-calibration':marker_density_calibration,'ph':ph,'settings-ph':settings_ph,'tray-disable-use-instead':tray_disable_use_instead,'print-media':print_media,'settings-print-media':settings_print_media,'media-names-available':media_names_available,'north-edge-offset':north_edge_offset,'media-names-enabled':media_names_enabled,'media-info':media_info,'media1':media1,'media1-name':media1_name,'media1-short-name':media1_short_name,'media1-page-count':media1_page_count,'media1-engine-media-mode':media1_engine_media_mode,'media2':media2,'media2-name':media2_name,'media2-short-name':media2_short_name,'media2-page-count':media2_page_count,'media2-engine-media-mode':media2_engine_media_mode,'media3':media3,'media3-name':media3_name,'media3-short-name':media3_short_name,'media3-page-count':media3_page_count,'media3-engine-media-mode':media3_engine_media_mode,'media4':media4,'media4-name':media4_name,'media4-short-name':media4_short_name,'media4-page-count':media4_page_count,'media4-engine-media-mode':media4_engine_media_mode,'media5':media5,'media5-name':media5_name,'media5-short-name':media5_short_name,'media5-page-count':media5_page_count,'media5-engine-media-mode':media5_engine_media_mode,'media6':media6,'media6-name':media6_name,'media6-short-name':media6_short_name,'media6-page-count':media6_page_count,'media6-engine-media-mode':media6_engine_media_mode,'media7':media7,'media7-name':media7_name,'media7-short-name':media7_short_name,'media7-page-count':media7_page_count,'media7-engine-media-mode':media7_engine_media_mode,'media8':media8,'media8-name':media8_name,'media8-short-name':media8_short_name,'media8-page-count':media8_page_count,'media8-engine-media-mode':media8_engine_media_mode,'media9':media9,'media9-name':media9_name,'media9-short-name':media9_short_name,'media9-page-count':media9_page_count,'media9-engine-media-mode':media9_engine_media_mode,'media10':media10,'media10-name':media10_name,'media10-short-name':media10_short_name,'media10-page-count':media10_page_count,'media10-engine-media-mode':media10_engine_media_mode,'media11':media11,'media11-name':media11_name,'media11-short-name':media11_short_name,'media11-page-count':media11_page_count,'media11-engine-media-mode':media11_engine_media_mode,'media12':media12,'media12-name':media12_name,'media12-short-name':media12_short_name,'media12-page-count':media12_page_count,'media12-engine-media-mode':media12_engine_media_mode,'media13':media13,'media13-name':media13_name,'media13-short-name':media13_short_name,'media13-page-count':media13_page_count,'media13-engine-media-mode':media13_engine_media_mode,'media14':media14,'media14-name':media14_name,'media14-short-name':media14_short_name,'media14-page-count':media14_page_count,'media14-engine-media-mode':media14_engine_media_mode,'media15':media15,'media15-name':media15_name,'media15-short-name':media15_short_name,'media15-page-count':media15_page_count,'media15-engine-media-mode':media15_engine_media_mode,'media16':media16,'media16-name':media16_name,'media16-short-name':media16_short_name,'media16-page-count':media16_page_count,'media16-engine-media-mode':media16_engine_media_mode,'media17':media17,'media17-name':media17_name,'media17-short-name':media17_short_name,'media17-page-count':media17_page_count,'media17-engine-media-mode':media17_engine_media_mode,'media18':media18,'media18-name':media18_name,'media18-short-name':media18_short_name,'media18-page-count':media18_page_count,'media18-engine-media-mode':media18_engine_media_mode,'media19':media19,'media19-name':media19_name,'media19-short-name':media19_short_name,'media19-page-count':media19_page_count,'media19-engine-media-mode':media19_engine_media_mode,'media20':media20,'media20-name':media20_name,'media20-short-name':media20_short_name,'media20-page-count':media20_page_count,'media20-engine-media-mode':media20_engine_media_mode,'media21':media21,'media21-name':media21_name,'media21-short-name':media21_short_name,'media21-page-count':media21_page_count,'media21-engine-media-mode':media21_engine_media_mode,'media22':media22,'media22-name':media22_name,'media22-short-name':media22_short_name,'media22-page-count':media22_page_count,'media22-engine-media-mode':media22_engine_media_mode,'media23':media23,'media23-name':media23_name,'media23-short-name':media23_short_name,'media23-page-count':media23_page_count,'media23-engine-media-mode':media23_engine_media_mode,'media24':media24,'media24-name':media24_name,'media24-short-name':media24_short_name,'media24-page-count':media24_page_count,'media24-engine-media-mode':media24_engine_media_mode,'media25':media25,'media25-name':media25_name,'media25-short-name':media25_short_name,'media25-page-count':media25_page_count,'media25-engine-media-mode':media25_engine_media_mode,'media26':media26,'media26-name':media26_name,'media26-short-name':media26_short_name,'media26-page-count':media26_page_count,'media26-engine-media-mode':media26_engine_media_mode,'media-modes':media_modes,'engine-media-modes-supported1':engine_media_modes_supported1,'media-size':media_size,'media-size-count':media_size_count,'media-size-west-edge-first-side-offset':media_size_west_edge_first_side_offset,'media-size-west-edge-second-side-offset':media_size_west_edge_second_side_offset,'media-size-west-edge-side-offset-by-tray':media_size_west_edge_side_offset_by_tray,'media-counts':media_counts,'non-assured-oht-page-count':non_assured_oht_page_count,'media-types':media_types,'media-number-of-type-supported':media_number_of_type_supported,'consumables':consumables,'consumables-1':consumables_1,'consumable-status':consumable_status,'consumable-status-web-service-access-data':consumable_status_web_service_access_data,'consumable-status-web-service-access-control':consumable_status_web_service_access_control,'consumable-reorder-url':consumable_reorder_url,'consumables-status':consumables_status,'consumables-life':consumables_life,'consumable-life-usage-units-remaining':consumable_life_usage_units_remaining,'consumable-life-usage-units':consumable_life_usage_units,'consumable-life-low-threshold':consumable_life_low_threshold,'consumable-current-state':consumable_current_state,'consumable-string':consumable_string,'consumable-string-information':consumable_string_information,'consumable-string-information-reset':consumable_string_information_reset,'consumable-notification-status':consumable_notification_status,'consumable-pages-printed-with-supply':consumable_pages_printed_with_supply,'supply-override-activated-level':supply_override_activated_level,'supply-override-activated-pagecount':supply_override_activated_pagecount,'supply-override-activated-date':supply_override_activated_date,'print-meter':print_meter,'printer-average':printer_average,'printer-average-marking-agent-coverage':printer_average_marking_agent_coverage,'printer-average-marking-agent-coverage-sum':printer_average_marking_agent_coverage_sum,'printer-average-marking-agent-coverage-sum-squared':printer_average_marking_agent_coverage_sum_squared,'printer-average-marking-agent-units-per-gram':printer_average_marking_agent_units_per_gram,'printer-average-marking-agent-coverage-actual':printer_average_marking_agent_coverage_actual,'menus':menus,'tables':tables})