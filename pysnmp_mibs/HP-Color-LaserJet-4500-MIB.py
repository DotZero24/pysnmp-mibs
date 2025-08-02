_A2='ePcsAdobeStandardEncoding'
_A1='ePcsASCII'
_A0='ePimpressions'
_z='ePcsISOLatinCyrillic'
_y='ePcsISOLatin2'
_x='eInternationalB5'
_w='eInternationalC5'
_v='eInternationalDL'
_u='eCommercial10'
_t='eMonarch'
_s='eEDORandomAccessMemory'
_r='eFPMRandomAccessMemory'
_q='eSRandomAccessMemory'
_p='eSDRandomAccessMemory'
_o='eBindingPHD'
_n='eIOCard'
_m='eOutputPHD'
_l='eInputPHD'
_k='eDiskDrive'
_j='eNonVolatileRandomAccessMemory'
_i='eUnSupported'
_h='eInitiateAction'
_g='eFalse'
_f='ePcsHPRoman8'
_e='ePnotPresent'
_d='eISOandJISA5'
_c='ePunknown'
_b='ePmeters'
_a='ePfeet'
_Z='ePsheets'
_Y='eCustom'
_X='eJISB5'
_W='eUSLegal'
_V='eUSExecutive'
_U='eRamRom'
_T='eFlashMemory'
_S='eISOandJISA4'
_R='eUSLetter'
_Q='eVolatileRandomAccessMemory'
_P='eReadOnlyMemory'
_O='eUnknown'
_N='eEmpty'
_M='DisplayString'
_L='eOn'
_K='write-only'
_J='ePmicrometers'
_I='ePtenThousandthsOfInches'
_H='eOff'
_G='ePother'
_F='mandatory'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='optional'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpsystem_ObjectIdentity=ObjectIdentity
hpsystem=_Hpsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3))
_Net_peripheral_ObjectIdentity=ObjectIdentity
net_peripheral=_Net_peripheral_ObjectIdentity((1,3,6,1,4,1,11,2,3,9))
_Netdm_ObjectIdentity=ObjectIdentity
netdm=_Netdm_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4))
_Dm_ObjectIdentity=ObjectIdentity
dm=_Dm_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1))
_Settings_system_ObjectIdentity=ObjectIdentity
settings_system=_Settings_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1))
class _Energy_star_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28800))
_Energy_star_Type.__name__=_C
_Energy_star_Object=MibScalar
energy_star=_Energy_star_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,1),_Energy_star_Type())
energy_star.setMaxAccess(_D)
if mibBuilder.loadTexts:energy_star.setStatus(_A)
class _Sleep_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('eTrue',2)))
_Sleep_mode_Type.__name__=_C
_Sleep_mode_Object=MibScalar
sleep_mode=_Sleep_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,2),_Sleep_mode_Type())
sleep_mode.setMaxAccess(_D)
if mibBuilder.loadTexts:sleep_mode.setStatus(_A)
_Status_system_ObjectIdentity=ObjectIdentity
status_system=_Status_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2))
class _On_off_line_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eOnline',1),('eOffline',2),('eOfflineAtEndOfJob',3)))
_On_off_line_Type.__name__=_C
_On_off_line_Object=MibScalar
on_off_line=_On_off_line_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,5),_On_off_line_Type())
on_off_line.setMaxAccess(_D)
if mibBuilder.loadTexts:on_off_line.setStatus(_A)
class __pysmi_continue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_h,1))
__pysmi_continue_Type.__name__=_C
__pysmi_continue_Object=MibScalar
_pysmi_continue=__pysmi_continue_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,6),__pysmi_continue_Type())
_pysmi_continue.setMaxAccess(_K)
if mibBuilder.loadTexts:_pysmi_continue.setStatus(_A)
class _Auto_continue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_L,2)))
_Auto_continue_Type.__name__=_C
_Auto_continue_Object=MibScalar
auto_continue=_Auto_continue_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,7),_Auto_continue_Type())
auto_continue.setMaxAccess(_D)
if mibBuilder.loadTexts:auto_continue.setStatus(_A)
class _Job_input_auto_continue_timeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,3600))
_Job_input_auto_continue_timeout_Type.__name__=_C
_Job_input_auto_continue_timeout_Object=MibScalar
job_input_auto_continue_timeout=_Job_input_auto_continue_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,35),_Job_input_auto_continue_timeout_Type())
job_input_auto_continue_timeout.setMaxAccess(_D)
if mibBuilder.loadTexts:job_input_auto_continue_timeout.setStatus(_A)
_Job_input_auto_continue_mode_Type=OctetString
_Job_input_auto_continue_mode_Object=MibScalar
job_input_auto_continue_mode=_Job_input_auto_continue_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,36),_Job_input_auto_continue_mode_Type())
job_input_auto_continue_mode.setMaxAccess(_B)
if mibBuilder.loadTexts:job_input_auto_continue_mode.setStatus(_A)
_Background_message_ObjectIdentity=ObjectIdentity
background_message=_Background_message_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37))
_Background_message1_ObjectIdentity=ObjectIdentity
background_message1=_Background_message1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,1))
class _Background_status_msg_line1_part1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Background_status_msg_line1_part1_Type.__name__=_M
_Background_status_msg_line1_part1_Object=MibScalar
background_status_msg_line1_part1=_Background_status_msg_line1_part1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,1,1),_Background_status_msg_line1_part1_Type())
background_status_msg_line1_part1.setMaxAccess(_D)
if mibBuilder.loadTexts:background_status_msg_line1_part1.setStatus(_A)
_Background_message2_ObjectIdentity=ObjectIdentity
background_message2=_Background_message2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,2))
class _Background_status_msg_line2_part1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Background_status_msg_line2_part1_Type.__name__=_M
_Background_status_msg_line2_part1_Object=MibScalar
background_status_msg_line2_part1=_Background_status_msg_line2_part1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,2,1),_Background_status_msg_line2_part1_Type())
background_status_msg_line2_part1.setMaxAccess(_D)
if mibBuilder.loadTexts:background_status_msg_line2_part1.setStatus(_A)
class _Error_log_clear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eClearErrorLog',1))
_Error_log_clear_Type.__name__=_C
_Error_log_clear_Object=MibScalar
error_log_clear=_Error_log_clear_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,38),_Error_log_clear_Type())
error_log_clear.setMaxAccess(_K)
if mibBuilder.loadTexts:error_log_clear.setStatus(_A)
class _Job_output_auto_continue_timeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,3600))
_Job_output_auto_continue_timeout_Type.__name__=_C
_Job_output_auto_continue_timeout_Object=MibScalar
job_output_auto_continue_timeout=_Job_output_auto_continue_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,40),_Job_output_auto_continue_timeout_Type())
job_output_auto_continue_timeout.setMaxAccess(_B)
if mibBuilder.loadTexts:job_output_auto_continue_timeout.setStatus(_A)
_Localization_languages_supported_Type=DisplayString
_Localization_languages_supported_Object=MibScalar
localization_languages_supported=_Localization_languages_supported_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,52),_Localization_languages_supported_Type())
localization_languages_supported.setMaxAccess(_B)
if mibBuilder.loadTexts:localization_languages_supported.setStatus(_A)
_Localization_countries_supported_Type=DisplayString
_Localization_countries_supported_Object=MibScalar
localization_countries_supported=_Localization_countries_supported_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,53),_Localization_countries_supported_Type())
localization_countries_supported.setMaxAccess(_B)
if mibBuilder.loadTexts:localization_countries_supported.setStatus(_A)
_Id_ObjectIdentity=ObjectIdentity
id=_Id_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3))
_Model_number_Type=DisplayString
_Model_number_Object=MibScalar
model_number=_Model_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,1),_Model_number_Type())
model_number.setMaxAccess(_B)
if mibBuilder.loadTexts:model_number.setStatus(_A)
_Model_name_Type=DisplayString
_Model_name_Object=MibScalar
model_name=_Model_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,2),_Model_name_Type())
model_name.setMaxAccess(_B)
if mibBuilder.loadTexts:model_name.setStatus(_A)
class _Serial_number_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Serial_number_Type.__name__=_M
_Serial_number_Object=MibScalar
serial_number=_Serial_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,3),_Serial_number_Type())
serial_number.setMaxAccess(_B)
if mibBuilder.loadTexts:serial_number.setStatus(_A)
_Device_name_Type=DisplayString
_Device_name_Object=MibScalar
device_name=_Device_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,10),_Device_name_Type())
device_name.setMaxAccess(_D)
if mibBuilder.loadTexts:device_name.setStatus(_A)
_Device_location_Type=DisplayString
_Device_location_Object=MibScalar
device_location=_Device_location_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,11),_Device_location_Type())
device_location.setMaxAccess(_D)
if mibBuilder.loadTexts:device_location.setStatus(_A)
_Asset_number_Type=DisplayString
_Asset_number_Object=MibScalar
asset_number=_Asset_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,12),_Asset_number_Type())
asset_number.setMaxAccess(_D)
if mibBuilder.loadTexts:asset_number.setStatus(_A)
_Interface_ObjectIdentity=ObjectIdentity
interface=_Interface_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4))
_Simm_ObjectIdentity=ObjectIdentity
simm=_Simm_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1))
_Simm1_ObjectIdentity=ObjectIdentity
simm1=_Simm1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1))
class _Simm1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,4),(_Q,5)))
_Simm1_type_Type.__name__=_C
_Simm1_type_Object=MibScalar
simm1_type=_Simm1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,4),_Simm1_type_Type())
simm1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm1_type.setStatus(_A)
_Simm1_capacity_Type=Integer32
_Simm1_capacity_Object=MibScalar
simm1_capacity=_Simm1_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1,5),_Simm1_capacity_Type())
simm1_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm1_capacity.setStatus(_A)
_Simm2_ObjectIdentity=ObjectIdentity
simm2=_Simm2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2))
class _Simm2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,7,9)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,4),(_Q,5),(_T,7),(_U,9)))
_Simm2_type_Type.__name__=_C
_Simm2_type_Object=MibScalar
simm2_type=_Simm2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,4),_Simm2_type_Type())
simm2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm2_type.setStatus(_A)
_Simm2_capacity_Type=Integer32
_Simm2_capacity_Object=MibScalar
simm2_capacity=_Simm2_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,2,5),_Simm2_capacity_Type())
simm2_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm2_capacity.setStatus(_A)
_Simm3_ObjectIdentity=ObjectIdentity
simm3=_Simm3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3))
class _Simm3_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,7,9)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,4),(_Q,5),(_T,7),(_U,9)))
_Simm3_type_Type.__name__=_C
_Simm3_type_Object=MibScalar
simm3_type=_Simm3_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,4),_Simm3_type_Type())
simm3_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm3_type.setStatus(_A)
_Simm3_capacity_Type=Integer32
_Simm3_capacity_Object=MibScalar
simm3_capacity=_Simm3_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,3,5),_Simm3_capacity_Type())
simm3_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm3_capacity.setStatus(_A)
_Mio_ObjectIdentity=ObjectIdentity
mio=_Mio_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3))
_Mio1_ObjectIdentity=ObjectIdentity
mio1=_Mio1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,1))
_Mio1_model_name_Type=DisplayString
_Mio1_model_name_Object=MibScalar
mio1_model_name=_Mio1_model_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,1,2),_Mio1_model_name_Type())
mio1_model_name.setMaxAccess(_B)
if mibBuilder.loadTexts:mio1_model_name.setStatus(_A)
_Mio1_manufacturing_info_Type=DisplayString
_Mio1_manufacturing_info_Object=MibScalar
mio1_manufacturing_info=_Mio1_manufacturing_info_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,1,3),_Mio1_manufacturing_info_Type())
mio1_manufacturing_info.setMaxAccess(_B)
if mibBuilder.loadTexts:mio1_manufacturing_info.setStatus(_A)
class _Mio1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_N,1),(_O,2),(_i,3),(_P,4),(_Q,5),(_j,6),(_T,7),(_k,8),(_U,9),(_l,10),(_m,11),(_n,12),(_o,13),(_p,14),(_q,15),(_r,16),(_s,17)))
_Mio1_type_Type.__name__=_C
_Mio1_type_Object=MibScalar
mio1_type=_Mio1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,1,4),_Mio1_type_Type())
mio1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:mio1_type.setStatus(_A)
_Mio2_ObjectIdentity=ObjectIdentity
mio2=_Mio2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,2))
_Mio2_model_name_Type=DisplayString
_Mio2_model_name_Object=MibScalar
mio2_model_name=_Mio2_model_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,2,2),_Mio2_model_name_Type())
mio2_model_name.setMaxAccess(_B)
if mibBuilder.loadTexts:mio2_model_name.setStatus(_A)
_Mio2_manufacturing_info_Type=DisplayString
_Mio2_manufacturing_info_Object=MibScalar
mio2_manufacturing_info=_Mio2_manufacturing_info_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,2,3),_Mio2_manufacturing_info_Type())
mio2_manufacturing_info.setMaxAccess(_B)
if mibBuilder.loadTexts:mio2_manufacturing_info.setStatus(_A)
class _Mio2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_N,1),(_O,2),(_i,3),(_P,4),(_Q,5),(_j,6),(_T,7),(_k,8),(_U,9),(_l,10),(_m,11),(_n,12),(_o,13),(_p,14),(_q,15),(_r,16),(_s,17)))
_Mio2_type_Type.__name__=_C
_Mio2_type_Object=MibScalar
mio2_type=_Mio2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,2,4),_Mio2_type_Type())
mio2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:mio2_type.setStatus(_A)
_Test_ObjectIdentity=ObjectIdentity
test=_Test_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5))
class _Self_test_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*(('eNotInASelfTest',1),('eNonDestructiveSelfTest',4)))
_Self_test_Type.__name__=_C
_Self_test_Object=MibScalar
self_test=_Self_test_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,1),_Self_test_Type())
self_test.setMaxAccess(_D)
if mibBuilder.loadTexts:self_test.setStatus(_A)
class _Print_internal_page_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,9,350,450,1000)));namedValues=NamedValues(*(('eNotPrintingAnInternalPage',1),('ePrintingAnUnknownInternalPage',2),('eDeviceDemoPage1ConfigurationPage',3),('eDeviceDemoPage7MenuMap',9),('ePCLFontList1',350),('ePostScriptFontList1',450),('eMarkingAgentTestPattern',1000)))
_Print_internal_page_Type.__name__=_C
_Print_internal_page_Object=MibScalar
print_internal_page=_Print_internal_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,2),_Print_internal_page_Type())
print_internal_page.setMaxAccess(_D)
if mibBuilder.loadTexts:print_internal_page.setStatus(_A)
_Job_ObjectIdentity=ObjectIdentity
job=_Job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6))
_Settings_job_ObjectIdentity=ObjectIdentity
settings_job=_Settings_job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1))
class _Clearable_warning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_L,2),('eJob',3)))
_Clearable_warning_Type.__name__=_C
_Clearable_warning_Object=MibScalar
clearable_warning=_Clearable_warning_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,1),_Clearable_warning_Type())
clearable_warning.setMaxAccess(_D)
if mibBuilder.loadTexts:clearable_warning.setStatus(_A)
class _Cancel_job_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_Cancel_job_Type.__name__=_C
_Cancel_job_Object=MibScalar
cancel_job=_Cancel_job_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,2),_Cancel_job_Type())
cancel_job.setMaxAccess(_K)
if mibBuilder.loadTexts:cancel_job.setStatus(_A)
class _Job_info_change_id_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Job_info_change_id_Type.__name__=_E
_Job_info_change_id_Object=MibScalar
job_info_change_id=_Job_info_change_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,3),_Job_info_change_id_Type())
job_info_change_id.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_change_id.setStatus(_A)
_Active_print_jobs_ObjectIdentity=ObjectIdentity
active_print_jobs=_Active_print_jobs_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,2))
_Job_being_parsed_ObjectIdentity=ObjectIdentity
job_being_parsed=_Job_being_parsed_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,2,1))
class _Current_job_parsing_id_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,32767))
_Current_job_parsing_id_Type.__name__=_C
_Current_job_parsing_id_Object=MibScalar
current_job_parsing_id=_Current_job_parsing_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,2,1,1),_Current_job_parsing_id_Type())
current_job_parsing_id.setMaxAccess(_B)
if mibBuilder.loadTexts:current_job_parsing_id.setStatus(_A)
_Job_info_ObjectIdentity=ObjectIdentity
job_info=_Job_info_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5))
_Job_info_name1_Type=DisplayString
_Job_info_name1_Object=MibScalar
job_info_name1=_Job_info_name1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,1),_Job_info_name1_Type())
job_info_name1.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_name1.setStatus(_A)
_Job_info_name2_Type=DisplayString
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
class _Job_info_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,7,10,11)));namedValues=NamedValues(*(('eAborted',3),('eWaitingForResources',4),('ePrinted',5),('eTerminating',7),('eCancelled',10),('eProcessing',11)))
_Job_info_state_Type.__name__=_C
_Job_info_state_Object=MibScalar
job_info_state=_Job_info_state_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,15),_Job_info_state_Type())
job_info_state.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_state.setStatus(_A)
class _Job_info_outcome_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues(('eOk',3))
_Job_info_outcome_Type.__name__=_C
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
_Source_subsystem_ObjectIdentity=ObjectIdentity
source_subsystem=_Source_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2))
_Io_ObjectIdentity=ObjectIdentity
io=_Io_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1))
_Settings_io_ObjectIdentity=ObjectIdentity
settings_io=_Settings_io_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1))
class _Io_timeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_Io_timeout_Type.__name__=_C
_Io_timeout_Object=MibScalar
io_timeout=_Io_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,1),_Io_timeout_Type())
io_timeout.setMaxAccess(_D)
if mibBuilder.loadTexts:io_timeout.setStatus(_A)
class _Io_switch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eYes',1))
_Io_switch_Type.__name__=_C
_Io_switch_Object=MibScalar
io_switch=_Io_switch_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,2),_Io_switch_Type())
io_switch.setMaxAccess(_B)
if mibBuilder.loadTexts:io_switch.setStatus(_A)
class _Io_buffering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_L,2),('eAuto',3)))
_Io_buffering_Type.__name__=_C
_Io_buffering_Object=MibScalar
io_buffering=_Io_buffering_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,5),_Io_buffering_Type())
io_buffering.setMaxAccess(_D)
if mibBuilder.loadTexts:io_buffering.setStatus(_A)
_Io_buffer_size_Type=Integer32
_Io_buffer_size_Object=MibScalar
io_buffer_size=_Io_buffer_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,6),_Io_buffer_size_Type())
io_buffer_size.setMaxAccess(_D)
if mibBuilder.loadTexts:io_buffer_size.setStatus(_A)
_Maximum_io_buffering_memory_Type=Integer32
_Maximum_io_buffering_memory_Object=MibScalar
maximum_io_buffering_memory=_Maximum_io_buffering_memory_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,7),_Maximum_io_buffering_memory_Type())
maximum_io_buffering_memory.setMaxAccess(_B)
if mibBuilder.loadTexts:maximum_io_buffering_memory.setStatus(_A)
_Ports_ObjectIdentity=ObjectIdentity
ports=_Ports_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3))
_Port1_ObjectIdentity=ObjectIdentity
port1=_Port1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3,1))
class _Port1_parallel_speed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eSlow',1),('eFast',2)))
_Port1_parallel_speed_Type.__name__=_C
_Port1_parallel_speed_Object=MibScalar
port1_parallel_speed=_Port1_parallel_speed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3,1,4),_Port1_parallel_speed_Type())
port1_parallel_speed.setMaxAccess(_D)
if mibBuilder.loadTexts:port1_parallel_speed.setStatus(_A)
class _Port1_parallel_bidirectionality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eUnidirectional',1),('eBidirectional',2)))
_Port1_parallel_bidirectionality_Type.__name__=_C
_Port1_parallel_bidirectionality_Object=MibScalar
port1_parallel_bidirectionality=_Port1_parallel_bidirectionality_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3,1,5),_Port1_parallel_bidirectionality_Type())
port1_parallel_bidirectionality.setMaxAccess(_D)
if mibBuilder.loadTexts:port1_parallel_bidirectionality.setStatus(_A)
_Processing_subsystem_ObjectIdentity=ObjectIdentity
processing_subsystem=_Processing_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3))
_Pdl_ObjectIdentity=ObjectIdentity
pdl=_Pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3))
_Settings_pdl_ObjectIdentity=ObjectIdentity
settings_pdl=_Settings_pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1))
class _Default_copies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_Default_copies_Type.__name__=_C
_Default_copies_Object=MibScalar
default_copies=_Default_copies_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,4),_Default_copies_Type())
default_copies.setMaxAccess(_D)
if mibBuilder.loadTexts:default_copies.setStatus(_A)
class _Form_feed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_h,1))
_Form_feed_Type.__name__=_C
_Form_feed_Object=MibScalar
form_feed=_Form_feed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,5),_Form_feed_Type())
form_feed.setMaxAccess(_K)
if mibBuilder.loadTexts:form_feed.setStatus(_A)
class _Resource_saving_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_H,1))
_Resource_saving_Type.__name__=_C
_Resource_saving_Object=MibScalar
resource_saving=_Resource_saving_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,6),_Resource_saving_Type())
resource_saving.setMaxAccess(_B)
if mibBuilder.loadTexts:resource_saving.setStatus(_A)
_Default_vertical_black_resolution_Type=Integer32
_Default_vertical_black_resolution_Object=MibScalar
default_vertical_black_resolution=_Default_vertical_black_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,8),_Default_vertical_black_resolution_Type())
default_vertical_black_resolution.setMaxAccess(_B)
if mibBuilder.loadTexts:default_vertical_black_resolution.setStatus(_A)
_Default_horizontal_black_resolution_Type=Integer32
_Default_horizontal_black_resolution_Object=MibScalar
default_horizontal_black_resolution=_Default_horizontal_black_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,9),_Default_horizontal_black_resolution_Type())
default_horizontal_black_resolution.setMaxAccess(_B)
if mibBuilder.loadTexts:default_horizontal_black_resolution.setStatus(_A)
class _Default_page_protect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues(('eAuto',3))
_Default_page_protect_Type.__name__=_C
_Default_page_protect_Object=MibScalar
default_page_protect=_Default_page_protect_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,10),_Default_page_protect_Type())
default_page_protect.setMaxAccess(_B)
if mibBuilder.loadTexts:default_page_protect.setStatus(_A)
_Default_lines_per_page_Type=Integer32
_Default_lines_per_page_Object=MibScalar
default_lines_per_page=_Default_lines_per_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,11),_Default_lines_per_page_Type())
default_lines_per_page.setMaxAccess(_D)
if mibBuilder.loadTexts:default_lines_per_page.setStatus(_A)
_Default_vmi_Type=Integer32
_Default_vmi_Object=MibScalar
default_vmi=_Default_vmi_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,12),_Default_vmi_Type())
default_vmi.setMaxAccess(_D)
if mibBuilder.loadTexts:default_vmi.setStatus(_A)
class _Default_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,25,26,45,80,81,90,91,100,101)));namedValues=NamedValues(*((_V,1),(_R,2),(_W,3),(_d,25),(_S,26),(_X,45),(_t,80),(_u,81),(_v,90),(_w,91),(_x,100),(_Y,101)))
_Default_media_size_Type.__name__=_C
_Default_media_size_Object=MibScalar
default_media_size=_Default_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,13),_Default_media_size_Type())
default_media_size.setMaxAccess(_D)
if mibBuilder.loadTexts:default_media_size.setStatus(_A)
class _Cold_reset_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,26)));namedValues=NamedValues(*((_R,2),(_S,26)))
_Cold_reset_media_size_Type.__name__=_C
_Cold_reset_media_size_Object=MibScalar
cold_reset_media_size=_Cold_reset_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,19),_Cold_reset_media_size_Type())
cold_reset_media_size.setMaxAccess(_D)
if mibBuilder.loadTexts:cold_reset_media_size.setStatus(_A)
_Default_media_name_Type=DisplayString
_Default_media_name_Object=MibScalar
default_media_name=_Default_media_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,22),_Default_media_name_Type())
default_media_name.setMaxAccess(_D)
if mibBuilder.loadTexts:default_media_name.setStatus(_A)
class _Reprint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_L,2)))
_Reprint_Type.__name__=_C
_Reprint_Object=MibScalar
reprint=_Reprint_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,36),_Reprint_Type())
reprint.setMaxAccess(_D)
if mibBuilder.loadTexts:reprint.setStatus(_A)
_Default_bits_per_pixel_Type=Integer32
_Default_bits_per_pixel_Object=MibScalar
default_bits_per_pixel=_Default_bits_per_pixel_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,39),_Default_bits_per_pixel_Type())
default_bits_per_pixel.setMaxAccess(_B)
if mibBuilder.loadTexts:default_bits_per_pixel.setStatus(_A)
_Status_pdl_ObjectIdentity=ObjectIdentity
status_pdl=_Status_pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,2))
class _Form_feed_needed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('eTrue',2)))
_Form_feed_needed_Type.__name__=_C
_Form_feed_needed_Object=MibScalar
form_feed_needed=_Form_feed_needed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,2,2),_Form_feed_needed_Type())
form_feed_needed.setMaxAccess(_B)
if mibBuilder.loadTexts:form_feed_needed.setStatus(_A)
_Pdl_pcl_ObjectIdentity=ObjectIdentity
pdl_pcl=_Pdl_pcl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3))
_Pcl_default_font_height_Type=Integer32
_Pcl_default_font_height_Object=MibScalar
pcl_default_font_height=_Pcl_default_font_height_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,13),_Pcl_default_font_height_Type())
pcl_default_font_height.setMaxAccess(_D)
if mibBuilder.loadTexts:pcl_default_font_height.setStatus(_A)
class _Pcl_default_font_source_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10,11,12)));namedValues=NamedValues(*(('eInternal',1),('ePermanentSoft',2),('eRomSimm1',10),('eRomSimm2',11),('eRomSimm3',12)))
_Pcl_default_font_source_Type.__name__=_C
_Pcl_default_font_source_Object=MibScalar
pcl_default_font_source=_Pcl_default_font_source_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,14),_Pcl_default_font_source_Type())
pcl_default_font_source.setMaxAccess(_D)
if mibBuilder.loadTexts:pcl_default_font_source.setStatus(_A)
class _Pcl_default_font_number_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Pcl_default_font_number_Type.__name__=_C
_Pcl_default_font_number_Object=MibScalar
pcl_default_font_number=_Pcl_default_font_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,15),_Pcl_default_font_number_Type())
pcl_default_font_number.setMaxAccess(_D)
if mibBuilder.loadTexts:pcl_default_font_number.setStatus(_A)
class _Pcl_default_font_width_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(44,9999))
_Pcl_default_font_width_Type.__name__=_C
_Pcl_default_font_width_Object=MibScalar
pcl_default_font_width=_Pcl_default_font_width_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,16),_Pcl_default_font_width_Type())
pcl_default_font_width.setMaxAccess(_D)
if mibBuilder.loadTexts:pcl_default_font_width.setStatus(_A)
_Pdl_postscript_ObjectIdentity=ObjectIdentity
pdl_postscript=_Pdl_postscript_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4))
class _Postscript_print_errors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_L,2)))
_Postscript_print_errors_Type.__name__=_C
_Postscript_print_errors_Object=MibScalar
postscript_print_errors=_Postscript_print_errors_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4,11),_Postscript_print_errors_Type())
postscript_print_errors.setMaxAccess(_D)
if mibBuilder.loadTexts:postscript_print_errors.setStatus(_A)
_Pjl_ObjectIdentity=ObjectIdentity
pjl=_Pjl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,5))
_Pjl_password_Type=Integer32
_Pjl_password_Object=MibScalar
pjl_password=_Pjl_password_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,5,1),_Pjl_password_Type())
pjl_password.setMaxAccess(_B)
if mibBuilder.loadTexts:pjl_password.setStatus(_A)
_Jetsend_proc_sub_ObjectIdentity=ObjectIdentity
jetsend_proc_sub=_Jetsend_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8))
_Settings_jetsend_ObjectIdentity=ObjectIdentity
settings_jetsend=_Settings_jetsend_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,1))
class _Jetsend_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_L,2)))
_Jetsend_mode_Type.__name__=_C
_Jetsend_mode_Object=MibScalar
jetsend_mode=_Jetsend_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,1,1),_Jetsend_mode_Type())
jetsend_mode.setMaxAccess(_D)
if mibBuilder.loadTexts:jetsend_mode.setStatus(_A)
_Jetsend_contact_ObjectIdentity=ObjectIdentity
jetsend_contact=_Jetsend_contact_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,3))
_Settings_jetsend_contact_ObjectIdentity=ObjectIdentity
settings_jetsend_contact=_Settings_jetsend_contact_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,3,1))
class _Jetsend_contact_password_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Jetsend_contact_password_Type.__name__=_E
_Jetsend_contact_password_Object=MibScalar
jetsend_contact_password=_Jetsend_contact_password_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,3,1,1),_Jetsend_contact_password_Type())
jetsend_contact_password.setMaxAccess(_K)
if mibBuilder.loadTexts:jetsend_contact_password.setStatus(_A)
class _Jetsend_contact_ip_address_security_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Jetsend_contact_ip_address_security_Type.__name__=_E
_Jetsend_contact_ip_address_security_Object=MibScalar
jetsend_contact_ip_address_security=_Jetsend_contact_ip_address_security_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,3,1,2),_Jetsend_contact_ip_address_security_Type())
jetsend_contact_ip_address_security.setMaxAccess(_K)
if mibBuilder.loadTexts:jetsend_contact_ip_address_security.setStatus(_A)
_Destination_subsystem_ObjectIdentity=ObjectIdentity
destination_subsystem=_Destination_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4))
_Print_engine_ObjectIdentity=ObjectIdentity
print_engine=_Print_engine_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1))
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
_Intray_ObjectIdentity=ObjectIdentity
intray=_Intray_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3))
_Settings_intray_ObjectIdentity=ObjectIdentity
settings_intray=_Settings_intray_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1))
class _Mp_tray_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('eCassette',2),('eFirst',3)))
_Mp_tray_Type.__name__=_C
_Mp_tray_Object=MibScalar
mp_tray=_Mp_tray_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,5),_Mp_tray_Type())
mp_tray.setMaxAccess(_D)
if mibBuilder.loadTexts:mp_tray.setStatus(_A)
_Intrays_ObjectIdentity=ObjectIdentity
intrays=_Intrays_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3))
_Intray1_ObjectIdentity=ObjectIdentity
intray1=_Intray1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1))
class _Tray1_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,25,26,45,80,81,90,91,100,101)));namedValues=NamedValues(*((_V,1),(_R,2),(_W,3),(_d,25),(_S,26),(_X,45),(_t,80),(_u,81),(_v,90),(_w,91),(_x,100),(_Y,101)))
_Tray1_media_size_loaded_Type.__name__=_C
_Tray1_media_size_loaded_Object=MibScalar
tray1_media_size_loaded=_Tray1_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,1),_Tray1_media_size_loaded_Type())
tray1_media_size_loaded.setMaxAccess(_D)
if mibBuilder.loadTexts:tray1_media_size_loaded.setStatus(_A)
_Intray2_ObjectIdentity=ObjectIdentity
intray2=_Intray2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2))
class _Tray2_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,25,26,45,101)));namedValues=NamedValues(*((_V,1),(_R,2),(_W,3),(_d,25),(_S,26),(_X,45),(_Y,101)))
_Tray2_media_size_loaded_Type.__name__=_C
_Tray2_media_size_loaded_Object=MibScalar
tray2_media_size_loaded=_Tray2_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,1),_Tray2_media_size_loaded_Type())
tray2_media_size_loaded.setMaxAccess(_B)
if mibBuilder.loadTexts:tray2_media_size_loaded.setStatus(_A)
_Intray3_ObjectIdentity=ObjectIdentity
intray3=_Intray3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3))
class _Tray3_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,26,45,101)));namedValues=NamedValues(*((_V,1),(_R,2),(_W,3),(_S,26),(_X,45),(_Y,101)))
_Tray3_media_size_loaded_Type.__name__=_C
_Tray3_media_size_loaded_Object=MibScalar
tray3_media_size_loaded=_Tray3_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,1),_Tray3_media_size_loaded_Type())
tray3_media_size_loaded.setMaxAccess(_B)
if mibBuilder.loadTexts:tray3_media_size_loaded.setStatus(_A)
_Outbin_ObjectIdentity=ObjectIdentity
outbin=_Outbin_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4))
_Settings_outbin_ObjectIdentity=ObjectIdentity
settings_outbin=_Settings_outbin_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,1))
_Overflow_bin_Type=Integer32
_Overflow_bin_Object=MibScalar
overflow_bin=_Overflow_bin_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,1,4),_Overflow_bin_Type())
overflow_bin.setMaxAccess(_B)
if mibBuilder.loadTexts:overflow_bin.setStatus(_A)
_Marking_agent_ObjectIdentity=ObjectIdentity
marking_agent=_Marking_agent_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,5))
_Settings_marking_agent_ObjectIdentity=ObjectIdentity
settings_marking_agent=_Settings_marking_agent_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,5,1))
class _Low_marking_agent_processing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eStop',1),('eCont',2)))
_Low_marking_agent_processing_Type.__name__=_C
_Low_marking_agent_processing_Object=MibScalar
low_marking_agent_processing=_Low_marking_agent_processing_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,5,1,3),_Low_marking_agent_processing_Type())
low_marking_agent_processing.setMaxAccess(_D)
if mibBuilder.loadTexts:low_marking_agent_processing.setStatus(_A)
_Imaging_ObjectIdentity=ObjectIdentity
imaging=_Imaging_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,6))
class _Default_ret_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_H,1))
_Default_ret_Type.__name__=_C
_Default_ret_Object=MibScalar
default_ret=_Default_ret_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,6,5),_Default_ret_Type())
default_ret.setMaxAccess(_B)
if mibBuilder.loadTexts:default_ret.setStatus(_A)
class _Default_print_quality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Default_print_quality_Type.__name__=_C
_Default_print_quality_Object=MibScalar
default_print_quality=_Default_print_quality_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,6,7),_Default_print_quality_Type())
default_print_quality.setMaxAccess(_B)
if mibBuilder.loadTexts:default_print_quality.setStatus(_A)
_Print_media_ObjectIdentity=ObjectIdentity
print_media=_Print_media_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8))
_Settings_print_media_ObjectIdentity=ObjectIdentity
settings_print_media=_Settings_print_media_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1))
_Media_names_available_Type=OctetString
_Media_names_available_Object=MibScalar
media_names_available=_Media_names_available_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1,1),_Media_names_available_Type())
media_names_available.setMaxAccess(_B)
if mibBuilder.loadTexts:media_names_available.setStatus(_A)
_Media_info_ObjectIdentity=ObjectIdentity
media_info=_Media_info_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3))
_Media1_ObjectIdentity=ObjectIdentity
media1=_Media1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1))
_Media1_name_Type=DisplayString
_Media1_name_Object=MibScalar
media1_name=_Media1_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1,1),_Media1_name_Type())
media1_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media1_name.setStatus(_A)
_Media1_short_name_Type=DisplayString
_Media1_short_name_Object=MibScalar
media1_short_name=_Media1_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1,2),_Media1_short_name_Type())
media1_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media1_short_name.setStatus(_A)
_Media1_page_count_Type=Integer32
_Media1_page_count_Object=MibScalar
media1_page_count=_Media1_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1,3),_Media1_page_count_Type())
media1_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media1_page_count.setStatus(_A)
_Media2_ObjectIdentity=ObjectIdentity
media2=_Media2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2))
_Media2_name_Type=DisplayString
_Media2_name_Object=MibScalar
media2_name=_Media2_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2,1),_Media2_name_Type())
media2_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media2_name.setStatus(_A)
_Media2_short_name_Type=DisplayString
_Media2_short_name_Object=MibScalar
media2_short_name=_Media2_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2,2),_Media2_short_name_Type())
media2_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media2_short_name.setStatus(_A)
_Media2_page_count_Type=Integer32
_Media2_page_count_Object=MibScalar
media2_page_count=_Media2_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2,3),_Media2_page_count_Type())
media2_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media2_page_count.setStatus(_A)
_Media3_ObjectIdentity=ObjectIdentity
media3=_Media3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3))
_Media3_name_Type=DisplayString
_Media3_name_Object=MibScalar
media3_name=_Media3_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3,1),_Media3_name_Type())
media3_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media3_name.setStatus(_A)
_Media3_short_name_Type=DisplayString
_Media3_short_name_Object=MibScalar
media3_short_name=_Media3_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3,2),_Media3_short_name_Type())
media3_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media3_short_name.setStatus(_A)
_Media3_page_count_Type=Integer32
_Media3_page_count_Object=MibScalar
media3_page_count=_Media3_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3,3),_Media3_page_count_Type())
media3_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media3_page_count.setStatus(_A)
_Media4_ObjectIdentity=ObjectIdentity
media4=_Media4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4))
_Media4_name_Type=DisplayString
_Media4_name_Object=MibScalar
media4_name=_Media4_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4,1),_Media4_name_Type())
media4_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media4_name.setStatus(_A)
_Media4_short_name_Type=DisplayString
_Media4_short_name_Object=MibScalar
media4_short_name=_Media4_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4,2),_Media4_short_name_Type())
media4_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media4_short_name.setStatus(_A)
_Media4_page_count_Type=Integer32
_Media4_page_count_Object=MibScalar
media4_page_count=_Media4_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4,3),_Media4_page_count_Type())
media4_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media4_page_count.setStatus(_A)
_Media5_ObjectIdentity=ObjectIdentity
media5=_Media5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5))
_Media5_name_Type=DisplayString
_Media5_name_Object=MibScalar
media5_name=_Media5_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5,1),_Media5_name_Type())
media5_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media5_name.setStatus(_A)
_Media5_short_name_Type=DisplayString
_Media5_short_name_Object=MibScalar
media5_short_name=_Media5_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5,2),_Media5_short_name_Type())
media5_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media5_short_name.setStatus(_A)
_Media5_page_count_Type=Integer32
_Media5_page_count_Object=MibScalar
media5_page_count=_Media5_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5,3),_Media5_page_count_Type())
media5_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media5_page_count.setStatus(_A)
_Media6_ObjectIdentity=ObjectIdentity
media6=_Media6_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6))
_Media6_name_Type=DisplayString
_Media6_name_Object=MibScalar
media6_name=_Media6_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6,1),_Media6_name_Type())
media6_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media6_name.setStatus(_A)
_Media6_short_name_Type=DisplayString
_Media6_short_name_Object=MibScalar
media6_short_name=_Media6_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6,2),_Media6_short_name_Type())
media6_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media6_short_name.setStatus(_A)
_Media6_page_count_Type=Integer32
_Media6_page_count_Object=MibScalar
media6_page_count=_Media6_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6,3),_Media6_page_count_Type())
media6_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media6_page_count.setStatus(_A)
_Media7_ObjectIdentity=ObjectIdentity
media7=_Media7_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7))
_Media7_name_Type=DisplayString
_Media7_name_Object=MibScalar
media7_name=_Media7_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7,1),_Media7_name_Type())
media7_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media7_name.setStatus(_A)
_Media7_short_name_Type=DisplayString
_Media7_short_name_Object=MibScalar
media7_short_name=_Media7_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7,2),_Media7_short_name_Type())
media7_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media7_short_name.setStatus(_A)
_Media7_page_count_Type=Integer32
_Media7_page_count_Object=MibScalar
media7_page_count=_Media7_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7,3),_Media7_page_count_Type())
media7_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media7_page_count.setStatus(_A)
_Media8_ObjectIdentity=ObjectIdentity
media8=_Media8_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8))
_Media8_name_Type=DisplayString
_Media8_name_Object=MibScalar
media8_name=_Media8_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8,1),_Media8_name_Type())
media8_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media8_name.setStatus(_A)
_Media8_short_name_Type=DisplayString
_Media8_short_name_Object=MibScalar
media8_short_name=_Media8_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8,2),_Media8_short_name_Type())
media8_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media8_short_name.setStatus(_A)
_Media8_page_count_Type=Integer32
_Media8_page_count_Object=MibScalar
media8_page_count=_Media8_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8,3),_Media8_page_count_Type())
media8_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media8_page_count.setStatus(_A)
_Media9_ObjectIdentity=ObjectIdentity
media9=_Media9_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9))
_Media9_name_Type=DisplayString
_Media9_name_Object=MibScalar
media9_name=_Media9_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9,1),_Media9_name_Type())
media9_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media9_name.setStatus(_A)
_Media9_short_name_Type=DisplayString
_Media9_short_name_Object=MibScalar
media9_short_name=_Media9_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9,2),_Media9_short_name_Type())
media9_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media9_short_name.setStatus(_A)
_Media9_page_count_Type=Integer32
_Media9_page_count_Object=MibScalar
media9_page_count=_Media9_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9,3),_Media9_page_count_Type())
media9_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media9_page_count.setStatus(_A)
_Media10_ObjectIdentity=ObjectIdentity
media10=_Media10_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10))
_Media10_name_Type=DisplayString
_Media10_name_Object=MibScalar
media10_name=_Media10_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10,1),_Media10_name_Type())
media10_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media10_name.setStatus(_A)
_Media10_short_name_Type=DisplayString
_Media10_short_name_Object=MibScalar
media10_short_name=_Media10_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10,2),_Media10_short_name_Type())
media10_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media10_short_name.setStatus(_A)
_Media10_page_count_Type=Integer32
_Media10_page_count_Object=MibScalar
media10_page_count=_Media10_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10,3),_Media10_page_count_Type())
media10_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media10_page_count.setStatus(_A)
_Media11_ObjectIdentity=ObjectIdentity
media11=_Media11_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11))
_Media11_name_Type=DisplayString
_Media11_name_Object=MibScalar
media11_name=_Media11_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11,1),_Media11_name_Type())
media11_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media11_name.setStatus(_A)
_Media11_short_name_Type=DisplayString
_Media11_short_name_Object=MibScalar
media11_short_name=_Media11_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11,2),_Media11_short_name_Type())
media11_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media11_short_name.setStatus(_A)
_Media11_page_count_Type=Integer32
_Media11_page_count_Object=MibScalar
media11_page_count=_Media11_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11,3),_Media11_page_count_Type())
media11_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media11_page_count.setStatus(_A)
_Media12_ObjectIdentity=ObjectIdentity
media12=_Media12_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12))
_Media12_name_Type=DisplayString
_Media12_name_Object=MibScalar
media12_name=_Media12_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12,1),_Media12_name_Type())
media12_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media12_name.setStatus(_A)
_Media12_short_name_Type=DisplayString
_Media12_short_name_Object=MibScalar
media12_short_name=_Media12_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12,2),_Media12_short_name_Type())
media12_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media12_short_name.setStatus(_A)
_Media12_page_count_Type=Integer32
_Media12_page_count_Object=MibScalar
media12_page_count=_Media12_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12,3),_Media12_page_count_Type())
media12_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media12_page_count.setStatus(_A)
_Media_size_ObjectIdentity=ObjectIdentity
media_size=_Media_size_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,5))
_Media_size_count_Type=Integer32
_Media_size_count_Object=MibScalar
media_size_count=_Media_size_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,5,1),_Media_size_count_Type())
media_size_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media_size_count.setStatus(_A)
_Media_mode_details_ObjectIdentity=ObjectIdentity
media_mode_details=_Media_mode_details_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6))
_Media_mode1_ObjectIdentity=ObjectIdentity
media_mode1=_Media_mode1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,1))
_Engine_media_mode1_page_count_Type=Integer32
_Engine_media_mode1_page_count_Object=MibScalar
engine_media_mode1_page_count=_Engine_media_mode1_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,1,2),_Engine_media_mode1_page_count_Type())
engine_media_mode1_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:engine_media_mode1_page_count.setStatus(_A)
_Media_mode2_ObjectIdentity=ObjectIdentity
media_mode2=_Media_mode2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,2))
_Engine_media_mode2_page_count_Type=Integer32
_Engine_media_mode2_page_count_Object=MibScalar
engine_media_mode2_page_count=_Engine_media_mode2_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,2,2),_Engine_media_mode2_page_count_Type())
engine_media_mode2_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:engine_media_mode2_page_count.setStatus(_A)
_Media_mode3_ObjectIdentity=ObjectIdentity
media_mode3=_Media_mode3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,3))
_Engine_media_mode3_page_count_Type=Integer32
_Engine_media_mode3_page_count_Object=MibScalar
engine_media_mode3_page_count=_Engine_media_mode3_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,3,2),_Engine_media_mode3_page_count_Type())
engine_media_mode3_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:engine_media_mode3_page_count.setStatus(_A)
_Media_mode4_ObjectIdentity=ObjectIdentity
media_mode4=_Media_mode4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,4))
_Engine_media_mode4_page_count_Type=Integer32
_Engine_media_mode4_page_count_Object=MibScalar
engine_media_mode4_page_count=_Engine_media_mode4_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,4,2),_Engine_media_mode4_page_count_Type())
engine_media_mode4_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:engine_media_mode4_page_count.setStatus(_A)
_Media_mode5_ObjectIdentity=ObjectIdentity
media_mode5=_Media_mode5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,5))
_Engine_media_mode5_page_count_Type=Integer32
_Engine_media_mode5_page_count_Object=MibScalar
engine_media_mode5_page_count=_Engine_media_mode5_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,6,5,2),_Engine_media_mode5_page_count_Type())
engine_media_mode5_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:engine_media_mode5_page_count.setStatus(_A)
_Channel_ObjectIdentity=ObjectIdentity
channel=_Channel_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,6))
_ChannelTable_ObjectIdentity=ObjectIdentity
channelTable=_ChannelTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,6,3))
_ChannelEntry_ObjectIdentity=ObjectIdentity
channelEntry=_ChannelEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,6,3,1))
_Tables_ObjectIdentity=ObjectIdentity
tables=_Tables_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,7))
_Channel_table_ObjectIdentity=ObjectIdentity
channel_table=_Channel_table_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,7,2))
_Channel_entry_ObjectIdentity=ObjectIdentity
channel_entry=_Channel_entry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,7,2,1))
_Channel_bytes_sent_Type=Integer32
_Channel_bytes_sent_Object=MibScalar
channel_bytes_sent=_Channel_bytes_sent_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,7,2,1,2),_Channel_bytes_sent_Type())
channel_bytes_sent.setMaxAccess(_B)
if mibBuilder.loadTexts:channel_bytes_sent.setStatus(_A)
_Channel_bytes_received_Type=Integer32
_Channel_bytes_received_Object=MibScalar
channel_bytes_received=_Channel_bytes_received_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,7,2,1,3),_Channel_bytes_received_Type())
channel_bytes_received.setMaxAccess(_B)
if mibBuilder.loadTexts:channel_bytes_received.setStatus(_A)
_Channel_io_errors_Type=Integer32
_Channel_io_errors_Object=MibScalar
channel_io_errors=_Channel_io_errors_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,7,2,1,4),_Channel_io_errors_Type())
channel_io_errors.setMaxAccess(_B)
if mibBuilder.loadTexts:channel_io_errors.setStatus(_A)
_Channel_jobs_received_Type=Integer32
_Channel_jobs_received_Object=MibScalar
channel_jobs_received=_Channel_jobs_received_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,7,2,1,5),_Channel_jobs_received_Type())
channel_jobs_received.setMaxAccess(_B)
if mibBuilder.loadTexts:channel_jobs_received.setStatus(_A)
_Channel_mio_Type=Integer32
_Channel_mio_Object=MibScalar
channel_mio=_Channel_mio_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,7,2,1,6),_Channel_mio_Type())
channel_mio.setMaxAccess(_B)
if mibBuilder.loadTexts:channel_mio.setStatus(_A)
_Printmib_ObjectIdentity=ObjectIdentity
printmib=_Printmib_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2))
_PrtGeneral_ObjectIdentity=ObjectIdentity
prtGeneral=_PrtGeneral_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5))
_PrtGeneralTable_ObjectIdentity=ObjectIdentity
prtGeneralTable=_PrtGeneralTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1))
_PrtGeneralEntry_ObjectIdentity=ObjectIdentity
prtGeneralEntry=_PrtGeneralEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1))
class _Prtgeneralconfigchanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967296))
_Prtgeneralconfigchanges_Type.__name__=_C
_Prtgeneralconfigchanges_Object=MibScalar
prtgeneralconfigchanges=_Prtgeneralconfigchanges_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,1),_Prtgeneralconfigchanges_Type())
prtgeneralconfigchanges.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgeneralconfigchanges.setStatus(_A)
class _Prtgeneralcurrentlocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Prtgeneralcurrentlocalization_Type.__name__=_C
_Prtgeneralcurrentlocalization_Object=MibScalar
prtgeneralcurrentlocalization=_Prtgeneralcurrentlocalization_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,2),_Prtgeneralcurrentlocalization_Type())
prtgeneralcurrentlocalization.setMaxAccess(_D)
if mibBuilder.loadTexts:prtgeneralcurrentlocalization.setStatus(_A)
class _Prtgeneralreset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6)));namedValues=NamedValues(*(('ePnotResetting',3),('ePpowerCycleReset',4),('ePresetToNVRAM',5),('ePresetToFactoryDefaults',6)))
_Prtgeneralreset_Type.__name__=_C
_Prtgeneralreset_Object=MibScalar
prtgeneralreset=_Prtgeneralreset_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,3),_Prtgeneralreset_Type())
prtgeneralreset.setMaxAccess(_D)
if mibBuilder.loadTexts:prtgeneralreset.setStatus(_A)
class _Prtgeneralcurrentoperator_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Prtgeneralcurrentoperator_Type.__name__=_E
_Prtgeneralcurrentoperator_Object=MibScalar
prtgeneralcurrentoperator=_Prtgeneralcurrentoperator_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,4),_Prtgeneralcurrentoperator_Type())
prtgeneralcurrentoperator.setMaxAccess(_D)
if mibBuilder.loadTexts:prtgeneralcurrentoperator.setStatus(_A)
class _Prtgeneralserviceperson_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Prtgeneralserviceperson_Type.__name__=_E
_Prtgeneralserviceperson_Object=MibScalar
prtgeneralserviceperson=_Prtgeneralserviceperson_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,5),_Prtgeneralserviceperson_Type())
prtgeneralserviceperson.setMaxAccess(_D)
if mibBuilder.loadTexts:prtgeneralserviceperson.setStatus(_A)
_Prtinputdefaultindex_Type=Integer32
_Prtinputdefaultindex_Object=MibScalar
prtinputdefaultindex=_Prtinputdefaultindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,6),_Prtinputdefaultindex_Type())
prtinputdefaultindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputdefaultindex.setStatus(_A)
_Prtoutputdefaultindex_Type=Integer32
_Prtoutputdefaultindex_Object=MibScalar
prtoutputdefaultindex=_Prtoutputdefaultindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,7),_Prtoutputdefaultindex_Type())
prtoutputdefaultindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputdefaultindex.setStatus(_A)
class _Prtmarkerdefaultindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Prtmarkerdefaultindex_Type.__name__=_C
_Prtmarkerdefaultindex_Object=MibScalar
prtmarkerdefaultindex=_Prtmarkerdefaultindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,8),_Prtmarkerdefaultindex_Type())
prtmarkerdefaultindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkerdefaultindex.setStatus(_A)
class _Prtmediapathdefaultindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Prtmediapathdefaultindex_Type.__name__=_C
_Prtmediapathdefaultindex_Object=MibScalar
prtmediapathdefaultindex=_Prtmediapathdefaultindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,9),_Prtmediapathdefaultindex_Type())
prtmediapathdefaultindex.setMaxAccess(_D)
if mibBuilder.loadTexts:prtmediapathdefaultindex.setStatus(_A)
class _Prtconsolelocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Prtconsolelocalization_Type.__name__=_C
_Prtconsolelocalization_Object=MibScalar
prtconsolelocalization=_Prtconsolelocalization_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,10),_Prtconsolelocalization_Type())
prtconsolelocalization.setMaxAccess(_D)
if mibBuilder.loadTexts:prtconsolelocalization.setStatus(_A)
class _Prtconsolenumberofdisplaylines_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Prtconsolenumberofdisplaylines_Type.__name__=_C
_Prtconsolenumberofdisplaylines_Object=MibScalar
prtconsolenumberofdisplaylines=_Prtconsolenumberofdisplaylines_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,11),_Prtconsolenumberofdisplaylines_Type())
prtconsolenumberofdisplaylines.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsolenumberofdisplaylines.setStatus(_A)
_Prtconsolenumberofdisplaychars_Type=Integer32
_Prtconsolenumberofdisplaychars_Object=MibScalar
prtconsolenumberofdisplaychars=_Prtconsolenumberofdisplaychars_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,12),_Prtconsolenumberofdisplaychars_Type())
prtconsolenumberofdisplaychars.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsolenumberofdisplaychars.setStatus(_A)
class _Prtconsoledisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6)));namedValues=NamedValues(*(('ePoperatorConsoleEnabled',3),('ePoperatorConsoleDisabled',4),('ePoperatorConsoleEnabledLevel1',5),('ePoperatorConsoleEnabledLevel2',6)))
_Prtconsoledisable_Type.__name__=_C
_Prtconsoledisable_Object=MibScalar
prtconsoledisable=_Prtconsoledisable_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,13),_Prtconsoledisable_Type())
prtconsoledisable.setMaxAccess(_D)
if mibBuilder.loadTexts:prtconsoledisable.setStatus(_A)
class _Prtgeneralstartuppage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_e,5))
_Prtgeneralstartuppage_Type.__name__=_C
_Prtgeneralstartuppage_Object=MibScalar
prtgeneralstartuppage=_Prtgeneralstartuppage_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,14),_Prtgeneralstartuppage_Type())
prtgeneralstartuppage.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgeneralstartuppage.setStatus(_A)
class _Prtgeneralbannerpage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_e,5))
_Prtgeneralbannerpage_Type.__name__=_C
_Prtgeneralbannerpage_Object=MibScalar
prtgeneralbannerpage=_Prtgeneralbannerpage_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,15),_Prtgeneralbannerpage_Type())
prtgeneralbannerpage.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgeneralbannerpage.setStatus(_A)
class _Prtgeneralprintername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Prtgeneralprintername_Type.__name__=_E
_Prtgeneralprintername_Object=MibScalar
prtgeneralprintername=_Prtgeneralprintername_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,16),_Prtgeneralprintername_Type())
prtgeneralprintername.setMaxAccess(_D)
if mibBuilder.loadTexts:prtgeneralprintername.setStatus(_A)
class _Prtgeneralserialnumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Prtgeneralserialnumber_Type.__name__=_E
_Prtgeneralserialnumber_Object=MibScalar
prtgeneralserialnumber=_Prtgeneralserialnumber_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,17),_Prtgeneralserialnumber_Type())
prtgeneralserialnumber.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgeneralserialnumber.setStatus(_A)
_Prtalertcriticalevents_Type=Integer32
_Prtalertcriticalevents_Object=MibScalar
prtalertcriticalevents=_Prtalertcriticalevents_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,18),_Prtalertcriticalevents_Type())
prtalertcriticalevents.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertcriticalevents.setStatus(_A)
_Prtalertallevents_Type=Integer32
_Prtalertallevents_Object=MibScalar
prtalertallevents=_Prtalertallevents_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,19),_Prtalertallevents_Type())
prtalertallevents.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertallevents.setStatus(_A)
_PrtStorageRefTable_ObjectIdentity=ObjectIdentity
prtStorageRefTable=_PrtStorageRefTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5,2))
_PrtStorageRefEntry_ObjectIdentity=ObjectIdentity
prtStorageRefEntry=_PrtStorageRefEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5,2,1))
class _Prtstoragerefindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Prtstoragerefindex_Type.__name__=_C
_Prtstoragerefindex_Object=MibScalar
prtstoragerefindex=_Prtstoragerefindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,2,1,2),_Prtstoragerefindex_Type())
prtstoragerefindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtstoragerefindex.setStatus(_A)
_PrtDeviceRefTable_ObjectIdentity=ObjectIdentity
prtDeviceRefTable=_PrtDeviceRefTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5,3))
_PrtDeviceRefEntry_ObjectIdentity=ObjectIdentity
prtDeviceRefEntry=_PrtDeviceRefEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5,3,1))
class _Prtdevicerefindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Prtdevicerefindex_Type.__name__=_C
_Prtdevicerefindex_Object=MibScalar
prtdevicerefindex=_Prtdevicerefindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,3,1,2),_Prtdevicerefindex_Type())
prtdevicerefindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtdevicerefindex.setStatus(_A)
_PrtCover_ObjectIdentity=ObjectIdentity
prtCover=_PrtCover_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,6))
_PrtCoverTable_ObjectIdentity=ObjectIdentity
prtCoverTable=_PrtCoverTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,6,1))
_PrtCoverEntry_ObjectIdentity=ObjectIdentity
prtCoverEntry=_PrtCoverEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,6,1,1))
class _Prtcoverdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtcoverdescription_Type.__name__=_E
_Prtcoverdescription_Object=MibScalar
prtcoverdescription=_Prtcoverdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,6,1,1,2),_Prtcoverdescription_Type())
prtcoverdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtcoverdescription.setStatus(_A)
class _Prtcoverstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('ePcoverOpen',3),('ePcoverClosed',4)))
_Prtcoverstatus_Type.__name__=_C
_Prtcoverstatus_Object=MibScalar
prtcoverstatus=_Prtcoverstatus_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,6,1,1,3),_Prtcoverstatus_Type())
prtcoverstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtcoverstatus.setStatus(_A)
_PrtLocalization_ObjectIdentity=ObjectIdentity
prtLocalization=_PrtLocalization_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,7))
_PrtLocalizationTable_ObjectIdentity=ObjectIdentity
prtLocalizationTable=_PrtLocalizationTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,7,1))
_PrtLocalizationEntry_ObjectIdentity=ObjectIdentity
prtLocalizationEntry=_PrtLocalizationEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,7,1,1))
class _Prtlocalizationlanguage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_Prtlocalizationlanguage_Type.__name__=_E
_Prtlocalizationlanguage_Object=MibScalar
prtlocalizationlanguage=_Prtlocalizationlanguage_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,7,1,1,2),_Prtlocalizationlanguage_Type())
prtlocalizationlanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:prtlocalizationlanguage.setStatus(_A)
class _Prtlocalizationcountry_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_Prtlocalizationcountry_Type.__name__=_E
_Prtlocalizationcountry_Object=MibScalar
prtlocalizationcountry=_Prtlocalizationcountry_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,7,1,1,3),_Prtlocalizationcountry_Type())
prtlocalizationcountry.setMaxAccess(_B)
if mibBuilder.loadTexts:prtlocalizationcountry.setStatus(_A)
class _Prtlocalizationcharacterset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,8,2004,2024)));namedValues=NamedValues(*((_y,5),(_z,8),(_f,2004),('ePcsWindows31J',2024)))
_Prtlocalizationcharacterset_Type.__name__=_C
_Prtlocalizationcharacterset_Object=MibScalar
prtlocalizationcharacterset=_Prtlocalizationcharacterset_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,7,1,1,4),_Prtlocalizationcharacterset_Type())
prtlocalizationcharacterset.setMaxAccess(_B)
if mibBuilder.loadTexts:prtlocalizationcharacterset.setStatus(_A)
_PrtInput_ObjectIdentity=ObjectIdentity
prtInput=_PrtInput_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,8))
_PrtInputTable_ObjectIdentity=ObjectIdentity
prtInputTable=_PrtInputTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2))
_PrtInputEntry_ObjectIdentity=ObjectIdentity
prtInputEntry=_PrtInputEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1))
class _Prtinputtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('ePsheetFeedAutoRemovableTray',3),('ePsheetFeedAutoNonRemovableTray',4)))
_Prtinputtype_Type.__name__=_C
_Prtinputtype_Object=MibScalar
prtinputtype=_Prtinputtype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,2),_Prtinputtype_Type())
prtinputtype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputtype.setStatus(_A)
class _Prtinputdimunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_I,3),(_J,4)))
_Prtinputdimunit_Type.__name__=_C
_Prtinputdimunit_Object=MibScalar
prtinputdimunit=_Prtinputdimunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,3),_Prtinputdimunit_Type())
prtinputdimunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputdimunit.setStatus(_A)
_Prtinputmediadimfeeddirdeclared_Type=Integer32
_Prtinputmediadimfeeddirdeclared_Object=MibScalar
prtinputmediadimfeeddirdeclared=_Prtinputmediadimfeeddirdeclared_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,4),_Prtinputmediadimfeeddirdeclared_Type())
prtinputmediadimfeeddirdeclared.setMaxAccess(_D)
if mibBuilder.loadTexts:prtinputmediadimfeeddirdeclared.setStatus(_A)
_Prtinputmediadimxfeeddirdeclared_Type=Integer32
_Prtinputmediadimxfeeddirdeclared_Object=MibScalar
prtinputmediadimxfeeddirdeclared=_Prtinputmediadimxfeeddirdeclared_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,5),_Prtinputmediadimxfeeddirdeclared_Type())
prtinputmediadimxfeeddirdeclared.setMaxAccess(_D)
if mibBuilder.loadTexts:prtinputmediadimxfeeddirdeclared.setStatus(_A)
_Prtinputmediadimfeeddirchosen_Type=Integer32
_Prtinputmediadimfeeddirchosen_Object=MibScalar
prtinputmediadimfeeddirchosen=_Prtinputmediadimfeeddirchosen_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,6),_Prtinputmediadimfeeddirchosen_Type())
prtinputmediadimfeeddirchosen.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputmediadimfeeddirchosen.setStatus(_A)
_Prtinputmediadimxfeeddirchosen_Type=Integer32
_Prtinputmediadimxfeeddirchosen_Object=MibScalar
prtinputmediadimxfeeddirchosen=_Prtinputmediadimxfeeddirchosen_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,7),_Prtinputmediadimxfeeddirchosen_Type())
prtinputmediadimxfeeddirchosen.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputmediadimxfeeddirchosen.setStatus(_A)
class _Prtinputcapacityunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,8,16,17)));namedValues=NamedValues(*((_I,3),(_J,4),(_Z,8),(_a,16),(_b,17)))
_Prtinputcapacityunit_Type.__name__=_C
_Prtinputcapacityunit_Object=MibScalar
prtinputcapacityunit=_Prtinputcapacityunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,8),_Prtinputcapacityunit_Type())
prtinputcapacityunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputcapacityunit.setStatus(_A)
_Prtinputmaxcapacity_Type=Integer32
_Prtinputmaxcapacity_Object=MibScalar
prtinputmaxcapacity=_Prtinputmaxcapacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,9),_Prtinputmaxcapacity_Type())
prtinputmaxcapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputmaxcapacity.setStatus(_A)
_Prtinputcurrentlevel_Type=Integer32
_Prtinputcurrentlevel_Object=MibScalar
prtinputcurrentlevel=_Prtinputcurrentlevel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,10),_Prtinputcurrentlevel_Type())
prtinputcurrentlevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputcurrentlevel.setStatus(_A)
_Prtinputstatus_Type=Integer32
_Prtinputstatus_Object=MibScalar
prtinputstatus=_Prtinputstatus_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,11),_Prtinputstatus_Type())
prtinputstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputstatus.setStatus(_A)
class _Prtinputmedianame_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputmedianame_Type.__name__=_E
_Prtinputmedianame_Object=MibScalar
prtinputmedianame=_Prtinputmedianame_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,12),_Prtinputmedianame_Type())
prtinputmedianame.setMaxAccess(_D)
if mibBuilder.loadTexts:prtinputmedianame.setStatus(_A)
class _Prtinputname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputname_Type.__name__=_E
_Prtinputname_Object=MibScalar
prtinputname=_Prtinputname_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,13),_Prtinputname_Type())
prtinputname.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputname.setStatus(_A)
class _Prtinputvendorname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputvendorname_Type.__name__=_E
_Prtinputvendorname_Object=MibScalar
prtinputvendorname=_Prtinputvendorname_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,14),_Prtinputvendorname_Type())
prtinputvendorname.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputvendorname.setStatus(_A)
class _Prtinputmodel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputmodel_Type.__name__=_E
_Prtinputmodel_Object=MibScalar
prtinputmodel=_Prtinputmodel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,15),_Prtinputmodel_Type())
prtinputmodel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputmodel.setStatus(_A)
class _Prtinputversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputversion_Type.__name__=_E
_Prtinputversion_Object=MibScalar
prtinputversion=_Prtinputversion_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,16),_Prtinputversion_Type())
prtinputversion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputversion.setStatus(_A)
class _Prtinputserialnumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Prtinputserialnumber_Type.__name__=_E
_Prtinputserialnumber_Object=MibScalar
prtinputserialnumber=_Prtinputserialnumber_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,17),_Prtinputserialnumber_Type())
prtinputserialnumber.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputserialnumber.setStatus(_A)
class _Prtinputdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtinputdescription_Type.__name__=_E
_Prtinputdescription_Object=MibScalar
prtinputdescription=_Prtinputdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,18),_Prtinputdescription_Type())
prtinputdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputdescription.setStatus(_A)
class _Prtinputsecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_G,1),('ePon',3),('ePoff',4),(_e,5)))
_Prtinputsecurity_Type.__name__=_C
_Prtinputsecurity_Object=MibScalar
prtinputsecurity=_Prtinputsecurity_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,19),_Prtinputsecurity_Type())
prtinputsecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputsecurity.setStatus(_A)
_Prtinputmedialoadtimeout_Type=Integer32
_Prtinputmedialoadtimeout_Object=MibScalar
prtinputmedialoadtimeout=_Prtinputmedialoadtimeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,24),_Prtinputmedialoadtimeout_Type())
prtinputmedialoadtimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputmedialoadtimeout.setStatus(_A)
_Prtinputnextindex_Type=Integer32
_Prtinputnextindex_Object=MibScalar
prtinputnextindex=_Prtinputnextindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,26),_Prtinputnextindex_Type())
prtinputnextindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputnextindex.setStatus(_A)
_PrtOutput_ObjectIdentity=ObjectIdentity
prtOutput=_PrtOutput_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,9))
_PrtOutputTable_ObjectIdentity=ObjectIdentity
prtOutputTable=_PrtOutputTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2))
_PrtOutputEntry_ObjectIdentity=ObjectIdentity
prtOutputEntry=_PrtOutputEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1))
class _Prtoutputtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_c,2),('ePremovableBin',3),('ePunRemovableBin',4),('ePcontinuousRollDevice',5),('ePmailBox',6),('ePcontinousFanFold',7)))
_Prtoutputtype_Type.__name__=_C
_Prtoutputtype_Object=MibScalar
prtoutputtype=_Prtoutputtype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,2),_Prtoutputtype_Type())
prtoutputtype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputtype.setStatus(_A)
class _Prtoutputcapacityunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,8,16,17)));namedValues=NamedValues(*((_I,3),(_J,4),(_Z,8),(_a,16),(_b,17)))
_Prtoutputcapacityunit_Type.__name__=_C
_Prtoutputcapacityunit_Object=MibScalar
prtoutputcapacityunit=_Prtoutputcapacityunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,3),_Prtoutputcapacityunit_Type())
prtoutputcapacityunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputcapacityunit.setStatus(_A)
_Prtoutputmaxcapacity_Type=Integer32
_Prtoutputmaxcapacity_Object=MibScalar
prtoutputmaxcapacity=_Prtoutputmaxcapacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,4),_Prtoutputmaxcapacity_Type())
prtoutputmaxcapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputmaxcapacity.setStatus(_A)
_Prtoutputremainingcapacity_Type=Integer32
_Prtoutputremainingcapacity_Object=MibScalar
prtoutputremainingcapacity=_Prtoutputremainingcapacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,5),_Prtoutputremainingcapacity_Type())
prtoutputremainingcapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputremainingcapacity.setStatus(_A)
_Prtoutputstatus_Type=Integer32
_Prtoutputstatus_Object=MibScalar
prtoutputstatus=_Prtoutputstatus_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,6),_Prtoutputstatus_Type())
prtoutputstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputstatus.setStatus(_A)
_PrtMarker_ObjectIdentity=ObjectIdentity
prtMarker=_PrtMarker_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,10))
_PrtMarkerTable_ObjectIdentity=ObjectIdentity
prtMarkerTable=_PrtMarkerTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2))
_PrtMarkerEntry_ObjectIdentity=ObjectIdentity
prtMarkerEntry=_PrtMarkerEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1))
class _Prtmarkermarktech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_G,1),(_c,2),('ePelectrophotographicLED',3),('ePelectrophotographicLaser',4),('ePelectrophotographicOther',5),('ePimpactMovingHeadDotMatrix9pin',6),('ePimpactMovingHeadDotMatrix24pin',7),('ePimpactMovingHeadDotMatrixOther',8),('ePimpactMovingHeadFullyFormed',9),('ePimpactBand',10),('ePimpactOther',11),('ePinkjetAqueous',12),('ePinkjetSolid',13),('ePinkjetOther',14),('ePpen',15),('ePthermalTransfer',16),('ePthermalSensitive',17),('ePthermalDiffusion',18),('ePthermalOther',19),('ePelectroerosion',20),('ePelectrostatic',21),('ePphotographicMicrofiche',22),('ePphotographicImagesetter',23),('ePphotographicOther',24),('ePionDeposition',25),('ePeBeam',26),('ePtypesetter',27)))
_Prtmarkermarktech_Type.__name__=_C
_Prtmarkermarktech_Object=MibScalar
prtmarkermarktech=_Prtmarkermarktech_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,2),_Prtmarkermarktech_Type())
prtmarkermarktech.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkermarktech.setStatus(_A)
class _Prtmarkercounterunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,11,16,17)));namedValues=NamedValues(*((_I,3),(_J,4),('ePcharacters',5),('ePlines',6),(_A0,7),(_Z,8),('ePdotRow',9),('ePhours',11),(_a,16),(_b,17)))
_Prtmarkercounterunit_Type.__name__=_C
_Prtmarkercounterunit_Object=MibScalar
prtmarkercounterunit=_Prtmarkercounterunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,3),_Prtmarkercounterunit_Type())
prtmarkercounterunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkercounterunit.setStatus(_A)
_Prtmarkerlifecount_Type=Integer32
_Prtmarkerlifecount_Object=MibScalar
prtmarkerlifecount=_Prtmarkerlifecount_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,4),_Prtmarkerlifecount_Type())
prtmarkerlifecount.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkerlifecount.setStatus(_A)
_Prtmarkerpoweroncount_Type=Integer32
_Prtmarkerpoweroncount_Object=MibScalar
prtmarkerpoweroncount=_Prtmarkerpoweroncount_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,5),_Prtmarkerpoweroncount_Type())
prtmarkerpoweroncount.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkerpoweroncount.setStatus(_A)
class _Prtmarkerprocesscolorants_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Prtmarkerprocesscolorants_Type.__name__=_C
_Prtmarkerprocesscolorants_Object=MibScalar
prtmarkerprocesscolorants=_Prtmarkerprocesscolorants_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,6),_Prtmarkerprocesscolorants_Type())
prtmarkerprocesscolorants.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkerprocesscolorants.setStatus(_A)
class _Prtmarkerspotcolorants_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Prtmarkerspotcolorants_Type.__name__=_C
_Prtmarkerspotcolorants_Object=MibScalar
prtmarkerspotcolorants=_Prtmarkerspotcolorants_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,7),_Prtmarkerspotcolorants_Type())
prtmarkerspotcolorants.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkerspotcolorants.setStatus(_A)
class _Prtmarkeraddressabilityunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_I,3),(_J,4)))
_Prtmarkeraddressabilityunit_Type.__name__=_C
_Prtmarkeraddressabilityunit_Object=MibScalar
prtmarkeraddressabilityunit=_Prtmarkeraddressabilityunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,8),_Prtmarkeraddressabilityunit_Type())
prtmarkeraddressabilityunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkeraddressabilityunit.setStatus(_A)
_Prtmarkeraddressabilityfeeddir_Type=Integer32
_Prtmarkeraddressabilityfeeddir_Object=MibScalar
prtmarkeraddressabilityfeeddir=_Prtmarkeraddressabilityfeeddir_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,9),_Prtmarkeraddressabilityfeeddir_Type())
prtmarkeraddressabilityfeeddir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkeraddressabilityfeeddir.setStatus(_A)
_Prtmarkeraddressabilityxfeeddir_Type=Integer32
_Prtmarkeraddressabilityxfeeddir_Object=MibScalar
prtmarkeraddressabilityxfeeddir=_Prtmarkeraddressabilityxfeeddir_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,10),_Prtmarkeraddressabilityxfeeddir_Type())
prtmarkeraddressabilityxfeeddir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkeraddressabilityxfeeddir.setStatus(_A)
_Prtmarkernorthmargin_Type=Integer32
_Prtmarkernorthmargin_Object=MibScalar
prtmarkernorthmargin=_Prtmarkernorthmargin_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,11),_Prtmarkernorthmargin_Type())
prtmarkernorthmargin.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkernorthmargin.setStatus(_A)
_Prtmarkersouthmargin_Type=Integer32
_Prtmarkersouthmargin_Object=MibScalar
prtmarkersouthmargin=_Prtmarkersouthmargin_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,12),_Prtmarkersouthmargin_Type())
prtmarkersouthmargin.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersouthmargin.setStatus(_A)
_Prtmarkerwestmargin_Type=Integer32
_Prtmarkerwestmargin_Object=MibScalar
prtmarkerwestmargin=_Prtmarkerwestmargin_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,13),_Prtmarkerwestmargin_Type())
prtmarkerwestmargin.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkerwestmargin.setStatus(_A)
_Prtmarkereastmargin_Type=Integer32
_Prtmarkereastmargin_Object=MibScalar
prtmarkereastmargin=_Prtmarkereastmargin_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,14),_Prtmarkereastmargin_Type())
prtmarkereastmargin.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkereastmargin.setStatus(_A)
_Prtmarkerstatus_Type=Integer32
_Prtmarkerstatus_Object=MibScalar
prtmarkerstatus=_Prtmarkerstatus_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,15),_Prtmarkerstatus_Type())
prtmarkerstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkerstatus.setStatus(_A)
_PrtMarkerSupplies_ObjectIdentity=ObjectIdentity
prtMarkerSupplies=_PrtMarkerSupplies_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,11))
_PrtMarkerSuppliesTable_ObjectIdentity=ObjectIdentity
prtMarkerSuppliesTable=_PrtMarkerSuppliesTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1))
_PrtMarkerSuppliesEntry_ObjectIdentity=ObjectIdentity
prtMarkerSuppliesEntry=_PrtMarkerSuppliesEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1))
class _Prtmarkersuppliesmarkerindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Prtmarkersuppliesmarkerindex_Type.__name__=_C
_Prtmarkersuppliesmarkerindex_Object=MibScalar
prtmarkersuppliesmarkerindex=_Prtmarkersuppliesmarkerindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,2),_Prtmarkersuppliesmarkerindex_Type())
prtmarkersuppliesmarkerindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliesmarkerindex.setStatus(_A)
class _Prtmarkersuppliescolorantindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Prtmarkersuppliescolorantindex_Type.__name__=_C
_Prtmarkersuppliescolorantindex_Object=MibScalar
prtmarkersuppliescolorantindex=_Prtmarkersuppliescolorantindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,3),_Prtmarkersuppliescolorantindex_Type())
prtmarkersuppliescolorantindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliescolorantindex.setStatus(_A)
class _Prtmarkersuppliesclass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_G,1),('ePsupplyThatIsConsumed',3),('ePreceptacleThatIsFilled',4)))
_Prtmarkersuppliesclass_Type.__name__=_C
_Prtmarkersuppliesclass_Object=MibScalar
prtmarkersuppliesclass=_Prtmarkersuppliesclass_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,4),_Prtmarkersuppliesclass_Type())
prtmarkersuppliesclass.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliesclass.setStatus(_A)
class _Prtmarkersuppliestype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_G,1),(_c,2),('ePtoner',3),('ePwasteToner',4),('ePink',5),('ePinkCartridge',6),('ePinkRibbon',7),('ePwasteInk',8),('ePopc',9),('ePdeveloper',10),('ePfuserOil',11),('ePsolidWax',12),('ePribbonWax',13),('ePwasteWax',14),('ePfuser',15),('ePcoronaWire',16),('ePfuserOilWick',17),('ePcleanerUnit',18),('ePfuserCleaningPad',19),('ePtransferUnit',20),('ePtonerCartridge',21),('ePfuserOiler',22)))
_Prtmarkersuppliestype_Type.__name__=_C
_Prtmarkersuppliestype_Object=MibScalar
prtmarkersuppliestype=_Prtmarkersuppliestype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,5),_Prtmarkersuppliestype_Type())
prtmarkersuppliestype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliestype.setStatus(_A)
class _Prtmarkersuppliesdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtmarkersuppliesdescription_Type.__name__=_E
_Prtmarkersuppliesdescription_Object=MibScalar
prtmarkersuppliesdescription=_Prtmarkersuppliesdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,6),_Prtmarkersuppliesdescription_Type())
prtmarkersuppliesdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliesdescription.setStatus(_A)
class _Prtmarkersuppliessupplyunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,7,8,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_I,3),(_J,4),(_A0,7),(_Z,8),('ePhours',11),('ePthousandthsOfOunces',12),('ePtenthsOfGrams',13),('ePhundrethsOfFluidOunces',14),('ePtenthsOfMilliliters',15),(_a,16),(_b,17)))
_Prtmarkersuppliessupplyunit_Type.__name__=_C
_Prtmarkersuppliessupplyunit_Object=MibScalar
prtmarkersuppliessupplyunit=_Prtmarkersuppliessupplyunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,7),_Prtmarkersuppliessupplyunit_Type())
prtmarkersuppliessupplyunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliessupplyunit.setStatus(_A)
_Prtmarkersuppliesmaxcapacity_Type=Integer32
_Prtmarkersuppliesmaxcapacity_Object=MibScalar
prtmarkersuppliesmaxcapacity=_Prtmarkersuppliesmaxcapacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,8),_Prtmarkersuppliesmaxcapacity_Type())
prtmarkersuppliesmaxcapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliesmaxcapacity.setStatus(_A)
_Prtmarkersupplieslevel_Type=Integer32
_Prtmarkersupplieslevel_Object=MibScalar
prtmarkersupplieslevel=_Prtmarkersupplieslevel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,9),_Prtmarkersupplieslevel_Type())
prtmarkersupplieslevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersupplieslevel.setStatus(_A)
_PrtMarkerColorant_ObjectIdentity=ObjectIdentity
prtMarkerColorant=_PrtMarkerColorant_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,12))
_PrtMarkerColorantTable_ObjectIdentity=ObjectIdentity
prtMarkerColorantTable=_PrtMarkerColorantTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,12,1))
_PrtMarkerColorantEntry_ObjectIdentity=ObjectIdentity
prtMarkerColorantEntry=_PrtMarkerColorantEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,12,1,1))
class _Prtmarkercolorantmarkerindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Prtmarkercolorantmarkerindex_Type.__name__=_C
_Prtmarkercolorantmarkerindex_Object=MibScalar
prtmarkercolorantmarkerindex=_Prtmarkercolorantmarkerindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,12,1,1,2),_Prtmarkercolorantmarkerindex_Type())
prtmarkercolorantmarkerindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkercolorantmarkerindex.setStatus(_A)
class _Prtmarkercolorantrole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_G,1),('ePprocess',3),('ePspot',4)))
_Prtmarkercolorantrole_Type.__name__=_C
_Prtmarkercolorantrole_Object=MibScalar
prtmarkercolorantrole=_Prtmarkercolorantrole_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,12,1,1,3),_Prtmarkercolorantrole_Type())
prtmarkercolorantrole.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkercolorantrole.setStatus(_A)
class _Prtmarkercolorantvalue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtmarkercolorantvalue_Type.__name__=_E
_Prtmarkercolorantvalue_Object=MibScalar
prtmarkercolorantvalue=_Prtmarkercolorantvalue_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,12,1,1,4),_Prtmarkercolorantvalue_Type())
prtmarkercolorantvalue.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkercolorantvalue.setStatus(_A)
_Prtmarkercoloranttonality_Type=Integer32
_Prtmarkercoloranttonality_Object=MibScalar
prtmarkercoloranttonality=_Prtmarkercoloranttonality_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,12,1,1,5),_Prtmarkercoloranttonality_Type())
prtmarkercoloranttonality.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkercoloranttonality.setStatus(_A)
_PrtMediaPath_ObjectIdentity=ObjectIdentity
prtMediaPath=_PrtMediaPath_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,13))
_PrtMediaPathTable_ObjectIdentity=ObjectIdentity
prtMediaPathTable=_PrtMediaPathTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4))
_PrtMediaPathEntry_ObjectIdentity=ObjectIdentity
prtMediaPathEntry=_PrtMediaPathEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1))
class _Prtmediapathmaxspeedprintunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,16,17)));namedValues=NamedValues(*(('ePtenThousandthsOfInchesPerHour',3),('ePmicrometersPerHour',4),('ePcharactersPerHour',5),('ePlinesPerHour',6),('ePimpressionsPerHour',7),('ePsheetsPerHour',8),('ePdotRowPerHour',9),('ePfeetPerHour',16),('ePmetersPerHour',17)))
_Prtmediapathmaxspeedprintunit_Type.__name__=_C
_Prtmediapathmaxspeedprintunit_Object=MibScalar
prtmediapathmaxspeedprintunit=_Prtmediapathmaxspeedprintunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,2),_Prtmediapathmaxspeedprintunit_Type())
prtmediapathmaxspeedprintunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathmaxspeedprintunit.setStatus(_A)
class _Prtmediapathmediasizeunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_I,3),(_J,4)))
_Prtmediapathmediasizeunit_Type.__name__=_C
_Prtmediapathmediasizeunit_Object=MibScalar
prtmediapathmediasizeunit=_Prtmediapathmediasizeunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,3),_Prtmediapathmediasizeunit_Type())
prtmediapathmediasizeunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathmediasizeunit.setStatus(_A)
_Prtmediapathmaxspeed_Type=Integer32
_Prtmediapathmaxspeed_Object=MibScalar
prtmediapathmaxspeed=_Prtmediapathmaxspeed_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,4),_Prtmediapathmaxspeed_Type())
prtmediapathmaxspeed.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathmaxspeed.setStatus(_A)
_Prtmediapathmaxmediafeeddir_Type=Integer32
_Prtmediapathmaxmediafeeddir_Object=MibScalar
prtmediapathmaxmediafeeddir=_Prtmediapathmaxmediafeeddir_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,5),_Prtmediapathmaxmediafeeddir_Type())
prtmediapathmaxmediafeeddir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathmaxmediafeeddir.setStatus(_A)
_Prtmediapathmaxmediaxfeeddir_Type=Integer32
_Prtmediapathmaxmediaxfeeddir_Object=MibScalar
prtmediapathmaxmediaxfeeddir=_Prtmediapathmaxmediaxfeeddir_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,6),_Prtmediapathmaxmediaxfeeddir_Type())
prtmediapathmaxmediaxfeeddir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathmaxmediaxfeeddir.setStatus(_A)
_Prtmediapathminmediafeeddir_Type=Integer32
_Prtmediapathminmediafeeddir_Object=MibScalar
prtmediapathminmediafeeddir=_Prtmediapathminmediafeeddir_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,7),_Prtmediapathminmediafeeddir_Type())
prtmediapathminmediafeeddir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathminmediafeeddir.setStatus(_A)
_Prtmediapathminmediaxfeeddir_Type=Integer32
_Prtmediapathminmediaxfeeddir_Object=MibScalar
prtmediapathminmediaxfeeddir=_Prtmediapathminmediaxfeeddir_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,8),_Prtmediapathminmediaxfeeddir_Type())
prtmediapathminmediaxfeeddir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathminmediaxfeeddir.setStatus(_A)
class _Prtmediapathtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5)));namedValues=NamedValues(*(('ePlongEdgeBindingDuplex',3),('ePshortEdgeBindingDuplex',4),('ePsimplex',5)))
_Prtmediapathtype_Type.__name__=_C
_Prtmediapathtype_Object=MibScalar
prtmediapathtype=_Prtmediapathtype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,9),_Prtmediapathtype_Type())
prtmediapathtype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathtype.setStatus(_A)
class _Prtmediapathdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtmediapathdescription_Type.__name__=_E
_Prtmediapathdescription_Object=MibScalar
prtmediapathdescription=_Prtmediapathdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,10),_Prtmediapathdescription_Type())
prtmediapathdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathdescription.setStatus(_A)
_Prtmediapathstatus_Type=Integer32
_Prtmediapathstatus_Object=MibScalar
prtmediapathstatus=_Prtmediapathstatus_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,11),_Prtmediapathstatus_Type())
prtmediapathstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathstatus.setStatus(_A)
_PrtChannel_ObjectIdentity=ObjectIdentity
prtChannel=_PrtChannel_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,14))
_PrtChannelTable_ObjectIdentity=ObjectIdentity
prtChannelTable=_PrtChannelTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1))
_PrtChannelEntry_ObjectIdentity=ObjectIdentity
prtChannelEntry=_PrtChannelEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1))
class _Prtchanneltype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,7,10,15,38)));namedValues=NamedValues(*((_G,1),('ePchIEEE1284Port',5),('ePchAppleTalkPAP',7),('ePchNetwarePServer',10),('ePchDLCLLCPort',15),('ePchBidirPortTCP',38)))
_Prtchanneltype_Type.__name__=_C
_Prtchanneltype_Object=MibScalar
prtchanneltype=_Prtchanneltype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1,2),_Prtchanneltype_Type())
prtchanneltype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtchanneltype.setStatus(_A)
class _Prtchannelprotocolversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtchannelprotocolversion_Type.__name__=_E
_Prtchannelprotocolversion_Object=MibScalar
prtchannelprotocolversion=_Prtchannelprotocolversion_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1,3),_Prtchannelprotocolversion_Type())
prtchannelprotocolversion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtchannelprotocolversion.setStatus(_A)
_Prtchannelcurrentjobcntllangindex_Type=Integer32
_Prtchannelcurrentjobcntllangindex_Object=MibScalar
prtchannelcurrentjobcntllangindex=_Prtchannelcurrentjobcntllangindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1,4),_Prtchannelcurrentjobcntllangindex_Type())
prtchannelcurrentjobcntllangindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtchannelcurrentjobcntllangindex.setStatus(_A)
_Prtchanneldefaultpagedesclangindex_Type=Integer32
_Prtchanneldefaultpagedesclangindex_Object=MibScalar
prtchanneldefaultpagedesclangindex=_Prtchanneldefaultpagedesclangindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1,5),_Prtchanneldefaultpagedesclangindex_Type())
prtchanneldefaultpagedesclangindex.setMaxAccess(_D)
if mibBuilder.loadTexts:prtchanneldefaultpagedesclangindex.setStatus(_A)
class _Prtchannelstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_G,1),('ePprintDataAccepted',3),('ePnoDataAccepted',4)))
_Prtchannelstate_Type.__name__=_C
_Prtchannelstate_Object=MibScalar
prtchannelstate=_Prtchannelstate_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1,6),_Prtchannelstate_Type())
prtchannelstate.setMaxAccess(_B)
if mibBuilder.loadTexts:prtchannelstate.setStatus(_A)
_Prtchannelifindex_Type=Integer32
_Prtchannelifindex_Object=MibScalar
prtchannelifindex=_Prtchannelifindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1,7),_Prtchannelifindex_Type())
prtchannelifindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtchannelifindex.setStatus(_A)
_Prtchannelstatus_Type=Integer32
_Prtchannelstatus_Object=MibScalar
prtchannelstatus=_Prtchannelstatus_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1,8),_Prtchannelstatus_Type())
prtchannelstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtchannelstatus.setStatus(_A)
class _Prtchannelinformation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtchannelinformation_Type.__name__=_E
_Prtchannelinformation_Object=MibScalar
prtchannelinformation=_Prtchannelinformation_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1,9),_Prtchannelinformation_Type())
prtchannelinformation.setMaxAccess(_B)
if mibBuilder.loadTexts:prtchannelinformation.setStatus(_A)
_PrtInterpreter_ObjectIdentity=ObjectIdentity
prtInterpreter=_PrtInterpreter_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,15))
_PrtInterpreterTable_ObjectIdentity=ObjectIdentity
prtInterpreterTable=_PrtInterpreterTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1))
_PrtInterpreterEntry_ObjectIdentity=ObjectIdentity
prtInterpreterEntry=_PrtInterpreterEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1))
class _Prtinterpreterlangfamily_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,5,6,37,47)));namedValues=NamedValues(*((_G,1),('ePlangPCL',3),('ePlangPJL',5),('ePlangPS',6),('ePlangAutomatic',37),('ePlangPCLXL',47)))
_Prtinterpreterlangfamily_Type.__name__=_C
_Prtinterpreterlangfamily_Object=MibScalar
prtinterpreterlangfamily=_Prtinterpreterlangfamily_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,2),_Prtinterpreterlangfamily_Type())
prtinterpreterlangfamily.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterlangfamily.setStatus(_A)
class _Prtinterpreterlanglevel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Prtinterpreterlanglevel_Type.__name__=_E
_Prtinterpreterlanglevel_Object=MibScalar
prtinterpreterlanglevel=_Prtinterpreterlanglevel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,3),_Prtinterpreterlanglevel_Type())
prtinterpreterlanglevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterlanglevel.setStatus(_A)
class _Prtinterpreterlangversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Prtinterpreterlangversion_Type.__name__=_E
_Prtinterpreterlangversion_Object=MibScalar
prtinterpreterlangversion=_Prtinterpreterlangversion_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,4),_Prtinterpreterlangversion_Type())
prtinterpreterlangversion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterlangversion.setStatus(_A)
class _Prtinterpreterdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtinterpreterdescription_Type.__name__=_E
_Prtinterpreterdescription_Object=MibScalar
prtinterpreterdescription=_Prtinterpreterdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,5),_Prtinterpreterdescription_Type())
prtinterpreterdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterdescription.setStatus(_A)
class _Prtinterpreterversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Prtinterpreterversion_Type.__name__=_E
_Prtinterpreterversion_Object=MibScalar
prtinterpreterversion=_Prtinterpreterversion_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,6),_Prtinterpreterversion_Type())
prtinterpreterversion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterversion.setStatus(_A)
class _Prtinterpreterdefaultorientation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('ePportrait',3),('ePlandscape',4)))
_Prtinterpreterdefaultorientation_Type.__name__=_C
_Prtinterpreterdefaultorientation_Object=MibScalar
prtinterpreterdefaultorientation=_Prtinterpreterdefaultorientation_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,7),_Prtinterpreterdefaultorientation_Type())
prtinterpreterdefaultorientation.setMaxAccess(_D)
if mibBuilder.loadTexts:prtinterpreterdefaultorientation.setStatus(_A)
_Prtinterpreterfeedaddressability_Type=Integer32
_Prtinterpreterfeedaddressability_Object=MibScalar
prtinterpreterfeedaddressability=_Prtinterpreterfeedaddressability_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,8),_Prtinterpreterfeedaddressability_Type())
prtinterpreterfeedaddressability.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterfeedaddressability.setStatus(_A)
_Prtinterpreterxfeedaddressability_Type=Integer32
_Prtinterpreterxfeedaddressability_Object=MibScalar
prtinterpreterxfeedaddressability=_Prtinterpreterxfeedaddressability_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,9),_Prtinterpreterxfeedaddressability_Type())
prtinterpreterxfeedaddressability.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterxfeedaddressability.setStatus(_A)
class _Prtinterpreterdefaultcharsetin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,8,9,12,13,20,21,22,23,24,25,26,1004,2000,2001,2002,2003,2004,2005,2009,2010,2011,2012,2014,2017,2021,2027,2087,2257)));namedValues=NamedValues(*((_G,1),(_A1,3),('ePcsISOLatin1',4),(_y,5),(_z,8),('ePcsISOLatinArabic',9),('ePcsISOLatin5',12),('ePcsISOLatin6',13),('ePcsISO4UnitedKingdom',20),('ePcsISO11SwedishforNames',21),('ePcsISO15Italian',22),('ePcsISO17Spanish',23),('ePcsISO21German',24),('ePcsISO60DanishNorwegian',25),('ePcsISO69French',26),('ePcsUnicodeIBM2039',1004),('ePcsWindows30Latin1',2000),('ePcsWindows31Latin1',2001),('ePcsWindows31Latin2',2002),('ePcsWindows31Latin5',2003),(_f,2004),(_A2,2005),('ePcsPC850Multilingual',2009),('ePcsPCp852',2010),('ePcsPC8CodePage437',2011),('ePcsPC8DNDanishNorwegian',2012),('ePcsHPPC8Turkish',2014),('ePcsHPLegal',2017),('ePcsHPDeskTop',2021),('ePcsMacintosh',2027),('ePcsPC775Baltic',2087),('ePcsWindows1257Baltic',2257)))
_Prtinterpreterdefaultcharsetin_Type.__name__=_C
_Prtinterpreterdefaultcharsetin_Object=MibScalar
prtinterpreterdefaultcharsetin=_Prtinterpreterdefaultcharsetin_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,10),_Prtinterpreterdefaultcharsetin_Type())
prtinterpreterdefaultcharsetin.setMaxAccess(_D)
if mibBuilder.loadTexts:prtinterpreterdefaultcharsetin.setStatus(_A)
class _Prtinterpreterdefaultcharsetout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,2004,2005)));namedValues=NamedValues(*(('ePcsNoDefault',2),(_A1,3),(_f,2004),(_A2,2005)))
_Prtinterpreterdefaultcharsetout_Type.__name__=_C
_Prtinterpreterdefaultcharsetout_Object=MibScalar
prtinterpreterdefaultcharsetout=_Prtinterpreterdefaultcharsetout_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,11),_Prtinterpreterdefaultcharsetout_Type())
prtinterpreterdefaultcharsetout.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterdefaultcharsetout.setStatus(_A)
class _Prtinterpretertwoway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('ePyes',3),('ePno',4)))
_Prtinterpretertwoway_Type.__name__=_C
_Prtinterpretertwoway_Object=MibScalar
prtinterpretertwoway=_Prtinterpretertwoway_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,12),_Prtinterpretertwoway_Type())
prtinterpretertwoway.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpretertwoway.setStatus(_A)
_PrtConsoleDisplayBuffer_ObjectIdentity=ObjectIdentity
prtConsoleDisplayBuffer=_PrtConsoleDisplayBuffer_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,16))
_PrtConsoleDisplayBufferTable_ObjectIdentity=ObjectIdentity
prtConsoleDisplayBufferTable=_PrtConsoleDisplayBufferTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,16,5))
_PrtConsoleDisplayBufferEntry_ObjectIdentity=ObjectIdentity
prtConsoleDisplayBufferEntry=_PrtConsoleDisplayBufferEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,16,5,1))
class _Prtconsoledisplaybuffertext_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtconsoledisplaybuffertext_Type.__name__=_E
_Prtconsoledisplaybuffertext_Object=MibScalar
prtconsoledisplaybuffertext=_Prtconsoledisplaybuffertext_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,16,5,1,2),_Prtconsoledisplaybuffertext_Type())
prtconsoledisplaybuffertext.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsoledisplaybuffertext.setStatus(_A)
_PrtConsoleLights_ObjectIdentity=ObjectIdentity
prtConsoleLights=_PrtConsoleLights_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,17))
_PrtConsoleLightTable_ObjectIdentity=ObjectIdentity
prtConsoleLightTable=_PrtConsoleLightTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,17,6))
_PrtConsoleLightEntry_ObjectIdentity=ObjectIdentity
prtConsoleLightEntry=_PrtConsoleLightEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,17,6,1))
_Prtconsoleontime_Type=Integer32
_Prtconsoleontime_Object=MibScalar
prtconsoleontime=_Prtconsoleontime_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,17,6,1,2),_Prtconsoleontime_Type())
prtconsoleontime.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsoleontime.setStatus(_A)
_Prtconsoleofftime_Type=Integer32
_Prtconsoleofftime_Object=MibScalar
prtconsoleofftime=_Prtconsoleofftime_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,17,6,1,3),_Prtconsoleofftime_Type())
prtconsoleofftime.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsoleofftime.setStatus(_A)
class _Prtconsolecolor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),(_c,2),('ePwhite',3),('ePred',4),('ePgreen',5),('ePblue',6),('ePcyan',7),('ePmagenta',8),('ePyellow',9)))
_Prtconsolecolor_Type.__name__=_C
_Prtconsolecolor_Object=MibScalar
prtconsolecolor=_Prtconsolecolor_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,17,6,1,4),_Prtconsolecolor_Type())
prtconsolecolor.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsolecolor.setStatus(_A)
class _Prtconsoledescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtconsoledescription_Type.__name__=_E
_Prtconsoledescription_Object=MibScalar
prtconsoledescription=_Prtconsoledescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,17,6,1,5),_Prtconsoledescription_Type())
prtconsoledescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsoledescription.setStatus(_A)
_PrtAlert_ObjectIdentity=ObjectIdentity
prtAlert=_PrtAlert_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,18))
_PrtAlertTable_ObjectIdentity=ObjectIdentity
prtAlertTable=_PrtAlertTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1))
_PrtAlertEntry_ObjectIdentity=ObjectIdentity
prtAlertEntry=_PrtAlertEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1))
class _Prtalertseveritylevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_G,1),('ePcriticalBinaryChangeEvent',3),('ePwarningUnaryChangeEvent',4),('ePwarningBinaryChangeEvent',5)))
_Prtalertseveritylevel_Type.__name__=_C
_Prtalertseveritylevel_Object=MibScalar
prtalertseveritylevel=_Prtalertseveritylevel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,2),_Prtalertseveritylevel_Type())
prtalertseveritylevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertseveritylevel.setStatus(_A)
class _Prtalerttraininglevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_G,1),('ePuntrained',3),('ePtrained',4),('ePfieldService',5)))
_Prtalerttraininglevel_Type.__name__=_C
_Prtalerttraininglevel_Object=MibScalar
prtalerttraininglevel=_Prtalerttraininglevel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,3),_Prtalerttraininglevel_Type())
prtalerttraininglevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalerttraininglevel.setStatus(_A)
class _Prtalertgroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,8,9,10,11,13,14,15)));namedValues=NamedValues(*(('ePgeneralPrinter',5),('ePcover',6),('ePinput',8),('ePoutput',9),('ePmarker',10),('ePmarkerSupplies',11),('ePmediaPath',13),('ePchannel',14),('ePinterpreter',15)))
_Prtalertgroup_Type.__name__=_C
_Prtalertgroup_Object=MibScalar
prtalertgroup=_Prtalertgroup_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,4),_Prtalertgroup_Type())
prtalertgroup.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertgroup.setStatus(_A)
_Prtalertgroupindex_Type=Integer32
_Prtalertgroupindex_Object=MibScalar
prtalertgroupindex=_Prtalertgroupindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,5),_Prtalertgroupindex_Type())
prtalertgroupindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertgroupindex.setStatus(_A)
_Prtalertlocation_Type=Integer32
_Prtalertlocation_Object=MibScalar
prtalertlocation=_Prtalertlocation_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,6),_Prtalertlocation_Type())
prtalertlocation.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertlocation.setStatus(_A)
class _Prtalertcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,8,9,10,11,12,13,15,18,22,23,29,30,33,809,1001,1002)));namedValues=NamedValues(*((_G,1),('ePcoverOpened',3),('ePjam',8),('ePsubunitMissing',9),('ePsubunitLifeAlmostOver',10),('ePsubunitLifeOver',11),('ePsubunitAlmostEmpty',12),('ePsubunitEmpty',13),('ePsubunitFull',15),('ePsubunitOpened',18),('ePsubunitOffline',22),('ePsubunitPowerSaver',23),('ePsubunitRecoverableFailure',29),('ePsubunitUnrecoverableFailure',30),('ePsubunitMotorFailure',33),('ePInputMediaChangeRequest',809),('ePmarkerFuserUnderTemperature',1001),('ePmarkerFuserOverTemperature',1002)))
_Prtalertcode_Type.__name__=_C
_Prtalertcode_Object=MibScalar
prtalertcode=_Prtalertcode_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,7),_Prtalertcode_Type())
prtalertcode.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertcode.setStatus(_A)
class _Prtalertdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtalertdescription_Type.__name__=_E
_Prtalertdescription_Object=MibScalar
prtalertdescription=_Prtalertdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,8),_Prtalertdescription_Type())
prtalertdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertdescription.setStatus(_A)
_Prtalerttime_Type=Integer32
_Prtalerttime_Object=MibScalar
prtalerttime=_Prtalerttime_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,9),_Prtalerttime_Type())
prtalerttime.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalerttime.setStatus(_A)
_Hrm_ObjectIdentity=ObjectIdentity
hrm=_Hrm_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3))
_HrStorage_ObjectIdentity=ObjectIdentity
hrStorage=_HrStorage_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,2))
_Hrmemorysize_Type=Integer32
_Hrmemorysize_Object=MibScalar
hrmemorysize=_Hrmemorysize_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,2,2),_Hrmemorysize_Type())
hrmemorysize.setMaxAccess(_B)
if mibBuilder.loadTexts:hrmemorysize.setStatus(_F)
_HrStorageTable_ObjectIdentity=ObjectIdentity
hrStorageTable=_HrStorageTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,2,3))
_HrStorageEntry_ObjectIdentity=ObjectIdentity
hrStorageEntry=_HrStorageEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,2,3,1))
class _Hrstorageindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hrstorageindex_Type.__name__=_C
_Hrstorageindex_Object=MibScalar
hrstorageindex=_Hrstorageindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,2,3,1,1),_Hrstorageindex_Type())
hrstorageindex.setMaxAccess(_B)
if mibBuilder.loadTexts:hrstorageindex.setStatus(_F)
_Hrstoragetype_Type=ObjectIdentifier
_Hrstoragetype_Object=MibScalar
hrstoragetype=_Hrstoragetype_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,2,3,1,2),_Hrstoragetype_Type())
hrstoragetype.setMaxAccess(_B)
if mibBuilder.loadTexts:hrstoragetype.setStatus(_F)
_Hrstoragedescr_Type=OctetString
_Hrstoragedescr_Object=MibScalar
hrstoragedescr=_Hrstoragedescr_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,2,3,1,3),_Hrstoragedescr_Type())
hrstoragedescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hrstoragedescr.setStatus(_F)
class _Hrstorageallocationunits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hrstorageallocationunits_Type.__name__=_C
_Hrstorageallocationunits_Object=MibScalar
hrstorageallocationunits=_Hrstorageallocationunits_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,2,3,1,4),_Hrstorageallocationunits_Type())
hrstorageallocationunits.setMaxAccess(_B)
if mibBuilder.loadTexts:hrstorageallocationunits.setStatus(_F)
class _Hrstoragesize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hrstoragesize_Type.__name__=_C
_Hrstoragesize_Object=MibScalar
hrstoragesize=_Hrstoragesize_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,2,3,1,5),_Hrstoragesize_Type())
hrstoragesize.setMaxAccess(_B)
if mibBuilder.loadTexts:hrstoragesize.setStatus(_F)
class _Hrstorageused_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hrstorageused_Type.__name__=_C
_Hrstorageused_Object=MibScalar
hrstorageused=_Hrstorageused_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,2,3,1,6),_Hrstorageused_Type())
hrstorageused.setMaxAccess(_B)
if mibBuilder.loadTexts:hrstorageused.setStatus(_F)
_Hrstorageallocationfailures_Type=Integer32
_Hrstorageallocationfailures_Object=MibScalar
hrstorageallocationfailures=_Hrstorageallocationfailures_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,2,3,1,7),_Hrstorageallocationfailures_Type())
hrstorageallocationfailures.setMaxAccess(_B)
if mibBuilder.loadTexts:hrstorageallocationfailures.setStatus(_F)
_HrDevice_ObjectIdentity=ObjectIdentity
hrDevice=_HrDevice_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3))
_HrDeviceTable_ObjectIdentity=ObjectIdentity
hrDeviceTable=_HrDeviceTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,2))
_HrDeviceEntry_ObjectIdentity=ObjectIdentity
hrDeviceEntry=_HrDeviceEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,2,1))
class _Hrdeviceindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hrdeviceindex_Type.__name__=_C
_Hrdeviceindex_Object=MibScalar
hrdeviceindex=_Hrdeviceindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,2,1,1),_Hrdeviceindex_Type())
hrdeviceindex.setMaxAccess(_B)
if mibBuilder.loadTexts:hrdeviceindex.setStatus(_F)
_Hrdevicetype_Type=ObjectIdentifier
_Hrdevicetype_Object=MibScalar
hrdevicetype=_Hrdevicetype_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,2,1,2),_Hrdevicetype_Type())
hrdevicetype.setMaxAccess(_B)
if mibBuilder.loadTexts:hrdevicetype.setStatus(_F)
class _Hrdevicedescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Hrdevicedescr_Type.__name__=_E
_Hrdevicedescr_Object=MibScalar
hrdevicedescr=_Hrdevicedescr_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,2,1,3),_Hrdevicedescr_Type())
hrdevicedescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hrdevicedescr.setStatus(_F)
_Hrdeviceid_Type=ObjectIdentifier
_Hrdeviceid_Object=MibScalar
hrdeviceid=_Hrdeviceid_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,2,1,4),_Hrdeviceid_Type())
hrdeviceid.setMaxAccess(_B)
if mibBuilder.loadTexts:hrdeviceid.setStatus(_F)
class _Hrdevicestatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*(('eHrunning',2),('eHwarning',3),('eHtesting',4),('eHdown',5)))
_Hrdevicestatus_Type.__name__=_C
_Hrdevicestatus_Object=MibScalar
hrdevicestatus=_Hrdevicestatus_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,2,1,5),_Hrdevicestatus_Type())
hrdevicestatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hrdevicestatus.setStatus(_F)
_Hrdeviceerrors_Type=Integer32
_Hrdeviceerrors_Object=MibScalar
hrdeviceerrors=_Hrdeviceerrors_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,2,1,6),_Hrdeviceerrors_Type())
hrdeviceerrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hrdeviceerrors.setStatus(_F)
_HrPrinterTable_ObjectIdentity=ObjectIdentity
hrPrinterTable=_HrPrinterTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,5))
_HrPrinterEntry_ObjectIdentity=ObjectIdentity
hrPrinterEntry=_HrPrinterEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,5,1))
class _Hrprinterstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*(('eHother',1),('eHidle',3),('eHprinting',4),('eHwarmup',5)))
_Hrprinterstatus_Type.__name__=_C
_Hrprinterstatus_Object=MibScalar
hrprinterstatus=_Hrprinterstatus_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,5,1,1),_Hrprinterstatus_Type())
hrprinterstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hrprinterstatus.setStatus(_F)
_Hrprinterdetectederrorstate_Type=OctetString
_Hrprinterdetectederrorstate_Object=MibScalar
hrprinterdetectederrorstate=_Hrprinterdetectederrorstate_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,5,1,2),_Hrprinterdetectederrorstate_Type())
hrprinterdetectederrorstate.setMaxAccess(_B)
if mibBuilder.loadTexts:hrprinterdetectederrorstate.setStatus(_F)
mibBuilder.exportSymbols('HP-Color-LaserJet-4500-MIB',**{_M:DisplayString,'hp':hp,'nm':nm,'hpsystem':hpsystem,'net-peripheral':net_peripheral,'netdm':netdm,'dm':dm,'device':device,'system':system,'settings-system':settings_system,'energy-star':energy_star,'sleep-mode':sleep_mode,'status-system':status_system,'on-off-line':on_off_line,'continue':_pysmi_continue,'auto-continue':auto_continue,'job-input-auto-continue-timeout':job_input_auto_continue_timeout,'job-input-auto-continue-mode':job_input_auto_continue_mode,'background-message':background_message,'background-message1':background_message1,'background-status-msg-line1-part1':background_status_msg_line1_part1,'background-message2':background_message2,'background-status-msg-line2-part1':background_status_msg_line2_part1,'error-log-clear':error_log_clear,'job-output-auto-continue-timeout':job_output_auto_continue_timeout,'localization-languages-supported':localization_languages_supported,'localization-countries-supported':localization_countries_supported,'id':id,'model-number':model_number,'model-name':model_name,'serial-number':serial_number,'device-name':device_name,'device-location':device_location,'asset-number':asset_number,'interface':interface,'simm':simm,'simm1':simm1,'simm1-type':simm1_type,'simm1-capacity':simm1_capacity,'simm2':simm2,'simm2-type':simm2_type,'simm2-capacity':simm2_capacity,'simm3':simm3,'simm3-type':simm3_type,'simm3-capacity':simm3_capacity,'mio':mio,'mio1':mio1,'mio1-model-name':mio1_model_name,'mio1-manufacturing-info':mio1_manufacturing_info,'mio1-type':mio1_type,'mio2':mio2,'mio2-model-name':mio2_model_name,'mio2-manufacturing-info':mio2_manufacturing_info,'mio2-type':mio2_type,'test':test,'self-test':self_test,'print-internal-page':print_internal_page,'job':job,'settings-job':settings_job,'clearable-warning':clearable_warning,'cancel-job':cancel_job,'job-info-change-id':job_info_change_id,'active-print-jobs':active_print_jobs,'job-being-parsed':job_being_parsed,'current-job-parsing-id':current_job_parsing_id,'job-info':job_info,'job-info-name1':job_info_name1,'job-info-name2':job_info_name2,'job-info-stage':job_info_stage,'job-info-io-source':job_info_io_source,'job-info-pages-processed':job_info_pages_processed,'job-info-pages-printed':job_info_pages_printed,'job-info-size':job_info_size,'job-info-state':job_info_state,'job-info-outcome':job_info_outcome,'job-info-outbins-used':job_info_outbins_used,'job-info-physical-outbins-used':job_info_physical_outbins_used,'job-info-attribute':job_info_attribute,'job-info-attr-1':job_info_attr_1,'job-info-attr-2':job_info_attr_2,'job-info-attr-3':job_info_attr_3,'job-info-attr-4':job_info_attr_4,'job-info-attr-5':job_info_attr_5,'job-info-attr-6':job_info_attr_6,'job-info-attr-7':job_info_attr_7,'job-info-attr-8':job_info_attr_8,'job-info-attr-9':job_info_attr_9,'job-info-attr-10':job_info_attr_10,'job-info-attr-11':job_info_attr_11,'job-info-attr-12':job_info_attr_12,'job-info-attr-13':job_info_attr_13,'job-info-attr-14':job_info_attr_14,'job-info-attr-15':job_info_attr_15,'job-info-attr-16':job_info_attr_16,'errorlog':errorlog,'error1':error1,'error1-time-stamp':error1_time_stamp,'error1-code':error1_code,'error2':error2,'error2-time-stamp':error2_time_stamp,'error2-code':error2_code,'error3':error3,'error3-time-stamp':error3_time_stamp,'error3-code':error3_code,'error4':error4,'error4-time-stamp':error4_time_stamp,'error4-code':error4_code,'error5':error5,'error5-time-stamp':error5_time_stamp,'error5-code':error5_code,'error6':error6,'error6-time-stamp':error6_time_stamp,'error6-code':error6_code,'error7':error7,'error7-time-stamp':error7_time_stamp,'error7-code':error7_code,'error8':error8,'error8-time-stamp':error8_time_stamp,'error8-code':error8_code,'error9':error9,'error9-time-stamp':error9_time_stamp,'error9-code':error9_code,'error10':error10,'error10-time-stamp':error10_time_stamp,'error10-code':error10_code,'error11':error11,'error11-time-stamp':error11_time_stamp,'error11-code':error11_code,'error12':error12,'error12-time-stamp':error12_time_stamp,'error12-code':error12_code,'error13':error13,'error13-time-stamp':error13_time_stamp,'error13-code':error13_code,'error14':error14,'error14-time-stamp':error14_time_stamp,'error14-code':error14_code,'error15':error15,'error15-time-stamp':error15_time_stamp,'error15-code':error15_code,'error16':error16,'error16-time-stamp':error16_time_stamp,'error16-code':error16_code,'error17':error17,'error17-time-stamp':error17_time_stamp,'error17-code':error17_code,'error18':error18,'error18-time-stamp':error18_time_stamp,'error18-code':error18_code,'error19':error19,'error19-time-stamp':error19_time_stamp,'error19-code':error19_code,'error20':error20,'error20-time-stamp':error20_time_stamp,'error20-code':error20_code,'error21':error21,'error21-time-stamp':error21_time_stamp,'error21-code':error21_code,'error22':error22,'error22-time-stamp':error22_time_stamp,'error22-code':error22_code,'error23':error23,'error23-time-stamp':error23_time_stamp,'error23-code':error23_code,'error24':error24,'error24-time-stamp':error24_time_stamp,'error24-code':error24_code,'error25':error25,'error25-time-stamp':error25_time_stamp,'error25-code':error25_code,'error26':error26,'error26-time-stamp':error26_time_stamp,'error26-code':error26_code,'error27':error27,'error27-time-stamp':error27_time_stamp,'error27-code':error27_code,'error28':error28,'error28-time-stamp':error28_time_stamp,'error28-code':error28_code,'error29':error29,'error29-time-stamp':error29_time_stamp,'error29-code':error29_code,'error30':error30,'error30-time-stamp':error30_time_stamp,'error30-code':error30_code,'error31':error31,'error31-time-stamp':error31_time_stamp,'error31-code':error31_code,'error32':error32,'error32-time-stamp':error32_time_stamp,'error32-code':error32_code,'error33':error33,'error33-time-stamp':error33_time_stamp,'error33-code':error33_code,'error34':error34,'error34-time-stamp':error34_time_stamp,'error34-code':error34_code,'error35':error35,'error35-time-stamp':error35_time_stamp,'error35-code':error35_code,'error36':error36,'error36-time-stamp':error36_time_stamp,'error36-code':error36_code,'error37':error37,'error37-time-stamp':error37_time_stamp,'error37-code':error37_code,'error38':error38,'error38-time-stamp':error38_time_stamp,'error38-code':error38_code,'error39':error39,'error39-time-stamp':error39_time_stamp,'error39-code':error39_code,'error40':error40,'error40-time-stamp':error40_time_stamp,'error40-code':error40_code,'error41':error41,'error41-time-stamp':error41_time_stamp,'error41-code':error41_code,'error42':error42,'error42-time-stamp':error42_time_stamp,'error42-code':error42_code,'error43':error43,'error43-time-stamp':error43_time_stamp,'error43-code':error43_code,'error44':error44,'error44-time-stamp':error44_time_stamp,'error44-code':error44_code,'error45':error45,'error45-time-stamp':error45_time_stamp,'error45-code':error45_code,'error46':error46,'error46-time-stamp':error46_time_stamp,'error46-code':error46_code,'error47':error47,'error47-time-stamp':error47_time_stamp,'error47-code':error47_code,'error48':error48,'error48-time-stamp':error48_time_stamp,'error48-code':error48_code,'error49':error49,'error49-time-stamp':error49_time_stamp,'error49-code':error49_code,'error50':error50,'error50-time-stamp':error50_time_stamp,'error50-code':error50_code,'source-subsystem':source_subsystem,'io':io,'settings-io':settings_io,'io-timeout':io_timeout,'io-switch':io_switch,'io-buffering':io_buffering,'io-buffer-size':io_buffer_size,'maximum-io-buffering-memory':maximum_io_buffering_memory,'ports':ports,'port1':port1,'port1-parallel-speed':port1_parallel_speed,'port1-parallel-bidirectionality':port1_parallel_bidirectionality,'processing-subsystem':processing_subsystem,'pdl':pdl,'settings-pdl':settings_pdl,'default-copies':default_copies,'form-feed':form_feed,'resource-saving':resource_saving,'default-vertical-black-resolution':default_vertical_black_resolution,'default-horizontal-black-resolution':default_horizontal_black_resolution,'default-page-protect':default_page_protect,'default-lines-per-page':default_lines_per_page,'default-vmi':default_vmi,'default-media-size':default_media_size,'cold-reset-media-size':cold_reset_media_size,'default-media-name':default_media_name,'reprint':reprint,'default-bits-per-pixel':default_bits_per_pixel,'status-pdl':status_pdl,'form-feed-needed':form_feed_needed,'pdl-pcl':pdl_pcl,'pcl-default-font-height':pcl_default_font_height,'pcl-default-font-source':pcl_default_font_source,'pcl-default-font-number':pcl_default_font_number,'pcl-default-font-width':pcl_default_font_width,'pdl-postscript':pdl_postscript,'postscript-print-errors':postscript_print_errors,'pjl':pjl,'pjl-password':pjl_password,'jetsend-proc-sub':jetsend_proc_sub,'settings-jetsend':settings_jetsend,'jetsend-mode':jetsend_mode,'jetsend-contact':jetsend_contact,'settings-jetsend-contact':settings_jetsend_contact,'jetsend-contact-password':jetsend_contact_password,'jetsend-contact-ip-address-security':jetsend_contact_ip_address_security,'destination-subsystem':destination_subsystem,'print-engine':print_engine,'status-prt-eng':status_prt_eng,'total-color-page-count':total_color_page_count,'duplex-page-count':duplex_page_count,'intray':intray,'settings-intray':settings_intray,'mp-tray':mp_tray,'intrays':intrays,'intray1':intray1,'tray1-media-size-loaded':tray1_media_size_loaded,'intray2':intray2,'tray2-media-size-loaded':tray2_media_size_loaded,'intray3':intray3,'tray3-media-size-loaded':tray3_media_size_loaded,'outbin':outbin,'settings-outbin':settings_outbin,'overflow-bin':overflow_bin,'marking-agent':marking_agent,'settings-marking-agent':settings_marking_agent,'low-marking-agent-processing':low_marking_agent_processing,'imaging':imaging,'default-ret':default_ret,'default-print-quality':default_print_quality,'print-media':print_media,'settings-print-media':settings_print_media,'media-names-available':media_names_available,'media-info':media_info,'media1':media1,'media1-name':media1_name,'media1-short-name':media1_short_name,'media1-page-count':media1_page_count,'media2':media2,'media2-name':media2_name,'media2-short-name':media2_short_name,'media2-page-count':media2_page_count,'media3':media3,'media3-name':media3_name,'media3-short-name':media3_short_name,'media3-page-count':media3_page_count,'media4':media4,'media4-name':media4_name,'media4-short-name':media4_short_name,'media4-page-count':media4_page_count,'media5':media5,'media5-name':media5_name,'media5-short-name':media5_short_name,'media5-page-count':media5_page_count,'media6':media6,'media6-name':media6_name,'media6-short-name':media6_short_name,'media6-page-count':media6_page_count,'media7':media7,'media7-name':media7_name,'media7-short-name':media7_short_name,'media7-page-count':media7_page_count,'media8':media8,'media8-name':media8_name,'media8-short-name':media8_short_name,'media8-page-count':media8_page_count,'media9':media9,'media9-name':media9_name,'media9-short-name':media9_short_name,'media9-page-count':media9_page_count,'media10':media10,'media10-name':media10_name,'media10-short-name':media10_short_name,'media10-page-count':media10_page_count,'media11':media11,'media11-name':media11_name,'media11-short-name':media11_short_name,'media11-page-count':media11_page_count,'media12':media12,'media12-name':media12_name,'media12-short-name':media12_short_name,'media12-page-count':media12_page_count,'media-size':media_size,'media-size-count':media_size_count,'media-mode-details':media_mode_details,'media-mode1':media_mode1,'engine-media-mode1-page-count':engine_media_mode1_page_count,'media-mode2':media_mode2,'engine-media-mode2-page-count':engine_media_mode2_page_count,'media-mode3':media_mode3,'engine-media-mode3-page-count':engine_media_mode3_page_count,'media-mode4':media_mode4,'engine-media-mode4-page-count':engine_media_mode4_page_count,'media-mode5':media_mode5,'engine-media-mode5-page-count':engine_media_mode5_page_count,'channel':channel,'channelTable':channelTable,'channelEntry':channelEntry,'tables':tables,'channel-table':channel_table,'channel-entry':channel_entry,'channel-bytes-sent':channel_bytes_sent,'channel-bytes-received':channel_bytes_received,'channel-io-errors':channel_io_errors,'channel-jobs-received':channel_jobs_received,'channel-mio':channel_mio,'printmib':printmib,'prtGeneral':prtGeneral,'prtGeneralTable':prtGeneralTable,'prtGeneralEntry':prtGeneralEntry,'prtgeneralconfigchanges':prtgeneralconfigchanges,'prtgeneralcurrentlocalization':prtgeneralcurrentlocalization,'prtgeneralreset':prtgeneralreset,'prtgeneralcurrentoperator':prtgeneralcurrentoperator,'prtgeneralserviceperson':prtgeneralserviceperson,'prtinputdefaultindex':prtinputdefaultindex,'prtoutputdefaultindex':prtoutputdefaultindex,'prtmarkerdefaultindex':prtmarkerdefaultindex,'prtmediapathdefaultindex':prtmediapathdefaultindex,'prtconsolelocalization':prtconsolelocalization,'prtconsolenumberofdisplaylines':prtconsolenumberofdisplaylines,'prtconsolenumberofdisplaychars':prtconsolenumberofdisplaychars,'prtconsoledisable':prtconsoledisable,'prtgeneralstartuppage':prtgeneralstartuppage,'prtgeneralbannerpage':prtgeneralbannerpage,'prtgeneralprintername':prtgeneralprintername,'prtgeneralserialnumber':prtgeneralserialnumber,'prtalertcriticalevents':prtalertcriticalevents,'prtalertallevents':prtalertallevents,'prtStorageRefTable':prtStorageRefTable,'prtStorageRefEntry':prtStorageRefEntry,'prtstoragerefindex':prtstoragerefindex,'prtDeviceRefTable':prtDeviceRefTable,'prtDeviceRefEntry':prtDeviceRefEntry,'prtdevicerefindex':prtdevicerefindex,'prtCover':prtCover,'prtCoverTable':prtCoverTable,'prtCoverEntry':prtCoverEntry,'prtcoverdescription':prtcoverdescription,'prtcoverstatus':prtcoverstatus,'prtLocalization':prtLocalization,'prtLocalizationTable':prtLocalizationTable,'prtLocalizationEntry':prtLocalizationEntry,'prtlocalizationlanguage':prtlocalizationlanguage,'prtlocalizationcountry':prtlocalizationcountry,'prtlocalizationcharacterset':prtlocalizationcharacterset,'prtInput':prtInput,'prtInputTable':prtInputTable,'prtInputEntry':prtInputEntry,'prtinputtype':prtinputtype,'prtinputdimunit':prtinputdimunit,'prtinputmediadimfeeddirdeclared':prtinputmediadimfeeddirdeclared,'prtinputmediadimxfeeddirdeclared':prtinputmediadimxfeeddirdeclared,'prtinputmediadimfeeddirchosen':prtinputmediadimfeeddirchosen,'prtinputmediadimxfeeddirchosen':prtinputmediadimxfeeddirchosen,'prtinputcapacityunit':prtinputcapacityunit,'prtinputmaxcapacity':prtinputmaxcapacity,'prtinputcurrentlevel':prtinputcurrentlevel,'prtinputstatus':prtinputstatus,'prtinputmedianame':prtinputmedianame,'prtinputname':prtinputname,'prtinputvendorname':prtinputvendorname,'prtinputmodel':prtinputmodel,'prtinputversion':prtinputversion,'prtinputserialnumber':prtinputserialnumber,'prtinputdescription':prtinputdescription,'prtinputsecurity':prtinputsecurity,'prtinputmedialoadtimeout':prtinputmedialoadtimeout,'prtinputnextindex':prtinputnextindex,'prtOutput':prtOutput,'prtOutputTable':prtOutputTable,'prtOutputEntry':prtOutputEntry,'prtoutputtype':prtoutputtype,'prtoutputcapacityunit':prtoutputcapacityunit,'prtoutputmaxcapacity':prtoutputmaxcapacity,'prtoutputremainingcapacity':prtoutputremainingcapacity,'prtoutputstatus':prtoutputstatus,'prtMarker':prtMarker,'prtMarkerTable':prtMarkerTable,'prtMarkerEntry':prtMarkerEntry,'prtmarkermarktech':prtmarkermarktech,'prtmarkercounterunit':prtmarkercounterunit,'prtmarkerlifecount':prtmarkerlifecount,'prtmarkerpoweroncount':prtmarkerpoweroncount,'prtmarkerprocesscolorants':prtmarkerprocesscolorants,'prtmarkerspotcolorants':prtmarkerspotcolorants,'prtmarkeraddressabilityunit':prtmarkeraddressabilityunit,'prtmarkeraddressabilityfeeddir':prtmarkeraddressabilityfeeddir,'prtmarkeraddressabilityxfeeddir':prtmarkeraddressabilityxfeeddir,'prtmarkernorthmargin':prtmarkernorthmargin,'prtmarkersouthmargin':prtmarkersouthmargin,'prtmarkerwestmargin':prtmarkerwestmargin,'prtmarkereastmargin':prtmarkereastmargin,'prtmarkerstatus':prtmarkerstatus,'prtMarkerSupplies':prtMarkerSupplies,'prtMarkerSuppliesTable':prtMarkerSuppliesTable,'prtMarkerSuppliesEntry':prtMarkerSuppliesEntry,'prtmarkersuppliesmarkerindex':prtmarkersuppliesmarkerindex,'prtmarkersuppliescolorantindex':prtmarkersuppliescolorantindex,'prtmarkersuppliesclass':prtmarkersuppliesclass,'prtmarkersuppliestype':prtmarkersuppliestype,'prtmarkersuppliesdescription':prtmarkersuppliesdescription,'prtmarkersuppliessupplyunit':prtmarkersuppliessupplyunit,'prtmarkersuppliesmaxcapacity':prtmarkersuppliesmaxcapacity,'prtmarkersupplieslevel':prtmarkersupplieslevel,'prtMarkerColorant':prtMarkerColorant,'prtMarkerColorantTable':prtMarkerColorantTable,'prtMarkerColorantEntry':prtMarkerColorantEntry,'prtmarkercolorantmarkerindex':prtmarkercolorantmarkerindex,'prtmarkercolorantrole':prtmarkercolorantrole,'prtmarkercolorantvalue':prtmarkercolorantvalue,'prtmarkercoloranttonality':prtmarkercoloranttonality,'prtMediaPath':prtMediaPath,'prtMediaPathTable':prtMediaPathTable,'prtMediaPathEntry':prtMediaPathEntry,'prtmediapathmaxspeedprintunit':prtmediapathmaxspeedprintunit,'prtmediapathmediasizeunit':prtmediapathmediasizeunit,'prtmediapathmaxspeed':prtmediapathmaxspeed,'prtmediapathmaxmediafeeddir':prtmediapathmaxmediafeeddir,'prtmediapathmaxmediaxfeeddir':prtmediapathmaxmediaxfeeddir,'prtmediapathminmediafeeddir':prtmediapathminmediafeeddir,'prtmediapathminmediaxfeeddir':prtmediapathminmediaxfeeddir,'prtmediapathtype':prtmediapathtype,'prtmediapathdescription':prtmediapathdescription,'prtmediapathstatus':prtmediapathstatus,'prtChannel':prtChannel,'prtChannelTable':prtChannelTable,'prtChannelEntry':prtChannelEntry,'prtchanneltype':prtchanneltype,'prtchannelprotocolversion':prtchannelprotocolversion,'prtchannelcurrentjobcntllangindex':prtchannelcurrentjobcntllangindex,'prtchanneldefaultpagedesclangindex':prtchanneldefaultpagedesclangindex,'prtchannelstate':prtchannelstate,'prtchannelifindex':prtchannelifindex,'prtchannelstatus':prtchannelstatus,'prtchannelinformation':prtchannelinformation,'prtInterpreter':prtInterpreter,'prtInterpreterTable':prtInterpreterTable,'prtInterpreterEntry':prtInterpreterEntry,'prtinterpreterlangfamily':prtinterpreterlangfamily,'prtinterpreterlanglevel':prtinterpreterlanglevel,'prtinterpreterlangversion':prtinterpreterlangversion,'prtinterpreterdescription':prtinterpreterdescription,'prtinterpreterversion':prtinterpreterversion,'prtinterpreterdefaultorientation':prtinterpreterdefaultorientation,'prtinterpreterfeedaddressability':prtinterpreterfeedaddressability,'prtinterpreterxfeedaddressability':prtinterpreterxfeedaddressability,'prtinterpreterdefaultcharsetin':prtinterpreterdefaultcharsetin,'prtinterpreterdefaultcharsetout':prtinterpreterdefaultcharsetout,'prtinterpretertwoway':prtinterpretertwoway,'prtConsoleDisplayBuffer':prtConsoleDisplayBuffer,'prtConsoleDisplayBufferTable':prtConsoleDisplayBufferTable,'prtConsoleDisplayBufferEntry':prtConsoleDisplayBufferEntry,'prtconsoledisplaybuffertext':prtconsoledisplaybuffertext,'prtConsoleLights':prtConsoleLights,'prtConsoleLightTable':prtConsoleLightTable,'prtConsoleLightEntry':prtConsoleLightEntry,'prtconsoleontime':prtconsoleontime,'prtconsoleofftime':prtconsoleofftime,'prtconsolecolor':prtconsolecolor,'prtconsoledescription':prtconsoledescription,'prtAlert':prtAlert,'prtAlertTable':prtAlertTable,'prtAlertEntry':prtAlertEntry,'prtalertseveritylevel':prtalertseveritylevel,'prtalerttraininglevel':prtalerttraininglevel,'prtalertgroup':prtalertgroup,'prtalertgroupindex':prtalertgroupindex,'prtalertlocation':prtalertlocation,'prtalertcode':prtalertcode,'prtalertdescription':prtalertdescription,'prtalerttime':prtalerttime,'hrm':hrm,'hrStorage':hrStorage,'hrmemorysize':hrmemorysize,'hrStorageTable':hrStorageTable,'hrStorageEntry':hrStorageEntry,'hrstorageindex':hrstorageindex,'hrstoragetype':hrstoragetype,'hrstoragedescr':hrstoragedescr,'hrstorageallocationunits':hrstorageallocationunits,'hrstoragesize':hrstoragesize,'hrstorageused':hrstorageused,'hrstorageallocationfailures':hrstorageallocationfailures,'hrDevice':hrDevice,'hrDeviceTable':hrDeviceTable,'hrDeviceEntry':hrDeviceEntry,'hrdeviceindex':hrdeviceindex,'hrdevicetype':hrdevicetype,'hrdevicedescr':hrdevicedescr,'hrdeviceid':hrdeviceid,'hrdevicestatus':hrdevicestatus,'hrdeviceerrors':hrdeviceerrors,'hrPrinterTable':hrPrinterTable,'hrPrinterEntry':hrPrinterEntry,'hrprinterstatus':hrprinterstatus,'hrprinterdetectederrorstate':hrprinterdetectederrorstate})