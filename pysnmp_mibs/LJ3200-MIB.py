_A3='ePcsAdobeStandardEncoding'
_A2='ePcsASCII'
_A1='eCopierQualityDraft'
_A0='eCopierQualityPresentation'
_z='eCopierQualityNormal'
_y='eCopierQualityFast'
_x='eCollateForward'
_w='eCollateDisabled'
_v='eCustom'
_u='eInternationalB5'
_t='eInternationalC5'
_s='eInternationalDL'
_r='eCommercial10'
_q='eMonarch'
_p='eJapanesePostcardDouble'
_o='eJapanesePostcardSingle'
_n='eJISB5'
_m='eISOandJISA5'
_l='eROC16K'
_k='eFoolscap'
_j='eUSExecutive'
_i='eBiLevelThesholded'
_h='eNever'
_g='eInitiateAction'
_f='eJunkFaxDialStrings'
_e='eConfigPrams'
_d='eFaxLogs'
_c='eSpeedDials'
_b='ePunknown'
_a='ePmicrometers'
_Z='ePcsHPRoman8'
_Y='eUSLegal'
_X='eRamRom'
_W='eVolatileRandomAccessMemory'
_V='eReadOnlyMemory'
_U='eUnSupported'
_T='eUnknown'
_S='eEmpty'
_R='eTrue'
_Q='eFalse'
_P='ePtenThousandthsOfInches'
_O='eISOandJISA4'
_N='eUSLetter'
_M='DisplayString'
_L='eEnabled'
_K='eDisabled'
_J='eOn'
_I='eOff'
_H='write-only'
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
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Dm_ObjectIdentity=ObjectIdentity
dm=_Dm_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1))
_Settings_system_ObjectIdentity=ObjectIdentity
settings_system=_Settings_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1))
_Energy_star_Type=Integer32
_Energy_star_Object=MibScalar
energy_star=_Energy_star_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,1),_Energy_star_Type())
energy_star.setMaxAccess(_B)
if mibBuilder.loadTexts:energy_star.setStatus(_A)
class _Sleep_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_Sleep_mode_Type.__name__=_C
_Sleep_mode_Object=MibScalar
sleep_mode=_Sleep_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,2),_Sleep_mode_Type())
sleep_mode.setMaxAccess(_B)
if mibBuilder.loadTexts:sleep_mode.setStatus(_A)
_Service_password_Type=Integer32
_Service_password_Object=MibScalar
service_password=_Service_password_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,9),_Service_password_Type())
service_password.setMaxAccess(_H)
if mibBuilder.loadTexts:service_password.setStatus(_A)
class _Device_cfg_download_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('eCfgDownloadIdle',1),('eCfgDownloadStart',2),('eCfgDownloadActive',3),('eCfgDownloadAborted',4),('eCfgDownloadDone',5)))
_Device_cfg_download_Type.__name__=_C
_Device_cfg_download_Object=MibScalar
device_cfg_download=_Device_cfg_download_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,11),_Device_cfg_download_Type())
device_cfg_download.setMaxAccess(_D)
if mibBuilder.loadTexts:device_cfg_download.setStatus(_A)
class _Device_cfg_download_data_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,9)));namedValues=NamedValues(*((_c,5),(_d,6),(_e,7),(_f,9)))
_Device_cfg_download_data_type_Type.__name__=_C
_Device_cfg_download_data_type_Object=MibScalar
device_cfg_download_data_type=_Device_cfg_download_data_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,12),_Device_cfg_download_data_type_Type())
device_cfg_download_data_type.setMaxAccess(_D)
if mibBuilder.loadTexts:device_cfg_download_data_type.setStatus(_A)
class _Device_cfg_upload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('eCfgUploadIdle',1),('eCfgUploadStart',2),('eCfgUploadActive',3),('eCfgUploadAborted',4),('eCfgUploadDone',5)))
_Device_cfg_upload_Type.__name__=_C
_Device_cfg_upload_Object=MibScalar
device_cfg_upload=_Device_cfg_upload_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,13),_Device_cfg_upload_Type())
device_cfg_upload.setMaxAccess(_D)
if mibBuilder.loadTexts:device_cfg_upload.setStatus(_A)
class _Device_cfg_upload_data_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,9)));namedValues=NamedValues(*((_c,5),(_d,6),(_e,7),(_f,9)))
_Device_cfg_upload_data_type_Type.__name__=_C
_Device_cfg_upload_data_type_Object=MibScalar
device_cfg_upload_data_type=_Device_cfg_upload_data_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,14),_Device_cfg_upload_data_type_Type())
device_cfg_upload_data_type.setMaxAccess(_D)
if mibBuilder.loadTexts:device_cfg_upload_data_type.setStatus(_A)
_Download_timeout_Type=Integer32
_Download_timeout_Object=MibScalar
download_timeout=_Download_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,17),_Download_timeout_Type())
download_timeout.setMaxAccess(_D)
if mibBuilder.loadTexts:download_timeout.setStatus(_A)
_Upload_timeout_Type=Integer32
_Upload_timeout_Object=MibScalar
upload_timeout=_Upload_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,18),_Upload_timeout_Type())
upload_timeout.setMaxAccess(_D)
if mibBuilder.loadTexts:upload_timeout.setStatus(_A)
class _Date_display_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eDateDisplayMMDDYY',1),('eDateDisplayDDMMYY',2),('eDateDisplayYYMMDD',3)))
_Date_display_Type.__name__=_C
_Date_display_Object=MibScalar
date_display=_Date_display_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,22),_Date_display_Type())
date_display.setMaxAccess(_D)
if mibBuilder.loadTexts:date_display.setStatus(_A)
_Device_cfg_param_command_Type=OctetString
_Device_cfg_param_command_Object=MibScalar
device_cfg_param_command=_Device_cfg_param_command_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,23),_Device_cfg_param_command_Type())
device_cfg_param_command.setMaxAccess(_D)
if mibBuilder.loadTexts:device_cfg_param_command.setStatus(_A)
class _Copier_token_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_Copier_token_Type.__name__=_E
_Copier_token_Object=MibScalar
copier_token=_Copier_token_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,24),_Copier_token_Type())
copier_token.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_token.setStatus(_A)
class _Scan_token_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_Scan_token_Type.__name__=_E
_Scan_token_Object=MibScalar
scan_token=_Scan_token_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,25),_Scan_token_Type())
scan_token.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_token.setStatus(_A)
class _Fax_upload_token_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_Fax_upload_token_Type.__name__=_E
_Fax_upload_token_Object=MibScalar
fax_upload_token=_Fax_upload_token_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,26),_Fax_upload_token_Type())
fax_upload_token.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_upload_token.setStatus(_A)
class _Fax_download_token_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_Fax_download_token_Type.__name__=_E
_Fax_download_token_Object=MibScalar
fax_download_token=_Fax_download_token_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,27),_Fax_download_token_Type())
fax_download_token.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_download_token.setStatus(_A)
class _Device_config_token_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_Device_config_token_Type.__name__=_E
_Device_config_token_Object=MibScalar
device_config_token=_Device_config_token_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,28),_Device_config_token_Type())
device_config_token.setMaxAccess(_D)
if mibBuilder.loadTexts:device_config_token.setStatus(_A)
_Status_system_ObjectIdentity=ObjectIdentity
status_system=_Status_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2))
class _On_off_line_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eOnline',1),('eOffline',2)))
_On_off_line_Type.__name__=_C
_On_off_line_Object=MibScalar
on_off_line=_On_off_line_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,5),_On_off_line_Type())
on_off_line.setMaxAccess(_B)
if mibBuilder.loadTexts:on_off_line.setStatus(_A)
class __pysmi_continue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_g,1))
__pysmi_continue_Type.__name__=_C
__pysmi_continue_Object=MibScalar
_pysmi_continue=__pysmi_continue_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,6),__pysmi_continue_Type())
_pysmi_continue.setMaxAccess(_H)
if mibBuilder.loadTexts:_pysmi_continue.setStatus(_A)
class _Auto_continue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Auto_continue_Type.__name__=_C
_Auto_continue_Object=MibScalar
auto_continue=_Auto_continue_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,7),_Auto_continue_Type())
auto_continue.setMaxAccess(_D)
if mibBuilder.loadTexts:auto_continue.setStatus(_A)
class _Install_date_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_Install_date_Type.__name__=_M
_Install_date_Object=MibScalar
install_date=_Install_date_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,8),_Install_date_Type())
install_date.setMaxAccess(_B)
if mibBuilder.loadTexts:install_date.setStatus(_A)
_Date_and_time_Type=OctetString
_Date_and_time_Object=MibScalar
date_and_time=_Date_and_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,17),_Date_and_time_Type())
date_and_time.setMaxAccess(_D)
if mibBuilder.loadTexts:date_and_time.setStatus(_A)
class _Time_display_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eTimeDisplayTwelveHour',1),('eTimeDisplayTwentyFourHour',2)))
_Time_display_Type.__name__=_C
_Time_display_Object=MibScalar
time_display=_Time_display_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,28),_Time_display_Type())
time_display.setMaxAccess(_D)
if mibBuilder.loadTexts:time_display.setStatus(_A)
class _Error_log_clear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eClearErrorLog',1))
_Error_log_clear_Type.__name__=_C
_Error_log_clear_Object=MibScalar
error_log_clear=_Error_log_clear_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,38),_Error_log_clear_Type())
error_log_clear.setMaxAccess(_H)
if mibBuilder.loadTexts:error_log_clear.setStatus(_A)
_Collated_originals_support_Type=OctetString
_Collated_originals_support_Object=MibScalar
collated_originals_support=_Collated_originals_support_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,42),_Collated_originals_support_Type())
collated_originals_support.setMaxAccess(_B)
if mibBuilder.loadTexts:collated_originals_support.setStatus(_A)
_Device_cfg_download_error_Type=Integer32
_Device_cfg_download_error_Object=MibScalar
device_cfg_download_error=_Device_cfg_download_error_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,43),_Device_cfg_download_error_Type())
device_cfg_download_error.setMaxAccess(_B)
if mibBuilder.loadTexts:device_cfg_download_error.setStatus(_A)
_Device_cfg_upload_error_Type=Integer32
_Device_cfg_upload_error_Object=MibScalar
device_cfg_upload_error=_Device_cfg_upload_error_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,45),_Device_cfg_upload_error_Type())
device_cfg_upload_error.setMaxAccess(_B)
if mibBuilder.loadTexts:device_cfg_upload_error.setStatus(_A)
_Id_ObjectIdentity=ObjectIdentity
id=_Id_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3))
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
_Fw_rom_datecode_Type=DisplayString
_Fw_rom_datecode_Object=MibScalar
fw_rom_datecode=_Fw_rom_datecode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,5),_Fw_rom_datecode_Type())
fw_rom_datecode.setMaxAccess(_B)
if mibBuilder.loadTexts:fw_rom_datecode.setStatus(_A)
_Fax_local_phone_num_Type=DisplayString
_Fax_local_phone_num_Object=MibScalar
fax_local_phone_num=_Fax_local_phone_num_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,8),_Fax_local_phone_num_Type())
fax_local_phone_num.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_local_phone_num.setStatus(_A)
_Fax_station_name_Type=DisplayString
_Fax_station_name_Object=MibScalar
fax_station_name=_Fax_station_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,9),_Fax_station_name_Type())
fax_station_name.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_station_name.setStatus(_A)
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
class _Fax_line_interface_unit_id_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Fax_line_interface_unit_id_Type.__name__=_C
_Fax_line_interface_unit_id_Object=MibScalar
fax_line_interface_unit_id=_Fax_line_interface_unit_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,18),_Fax_line_interface_unit_id_Type())
fax_line_interface_unit_id.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_line_interface_unit_id.setStatus(_A)
_Interface_ObjectIdentity=ObjectIdentity
interface=_Interface_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4))
_Simm_ObjectIdentity=ObjectIdentity
simm=_Simm_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1))
_Simm1_ObjectIdentity=ObjectIdentity
simm1=_Simm1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1))
class _Simm1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,9)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_V,4),(_W,5),(_X,9)))
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
class _Simm2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,9)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_V,4),(_W,5),(_X,9)))
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
class _Simm3_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,9)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_V,4),(_W,5),(_X,9)))
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
_Test_ObjectIdentity=ObjectIdentity
test=_Test_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5))
class _Self_test_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*(('eNotInASelfTest',1),('eNonDestructiveSelfTest',4)))
_Self_test_Type.__name__=_C
_Self_test_Object=MibScalar
self_test=_Self_test_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,1),_Self_test_Type())
self_test.setMaxAccess(_D)
if mibBuilder.loadTexts:self_test.setStatus(_A)
class _Print_internal_page_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,11,12,350,450)));namedValues=NamedValues(*(('eNotPrintingAnInternalPage',1),('ePrintingAnUnknownInternalPage',2),('eDeviceDemoPage1ConfigurationPage',3),('eDeviceDemoPage2',4),('eDeviceDemoPage8BlockFaxList',11),('eDeviceDemoPage9BlockFaxLogReport',12),('ePCLFontList1',350),('ePostScriptFontList1',450)))
_Print_internal_page_Type.__name__=_C
_Print_internal_page_Object=MibScalar
print_internal_page=_Print_internal_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,2),_Print_internal_page_Type())
print_internal_page.setMaxAccess(_D)
if mibBuilder.loadTexts:print_internal_page.setStatus(_A)
_Job_ObjectIdentity=ObjectIdentity
job=_Job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6))
_Settings_job_ObjectIdentity=ObjectIdentity
settings_job=_Settings_job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1))
_Cancel_job_Type=Integer32
_Cancel_job_Object=MibScalar
cancel_job=_Cancel_job_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,2),_Cancel_job_Type())
cancel_job.setMaxAccess(_D)
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
_Fax_job_control_ObjectIdentity=ObjectIdentity
fax_job_control=_Fax_job_control_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3))
_Settings_fax_job_ObjectIdentity=ObjectIdentity
settings_fax_job=_Settings_fax_job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,1))
class _Faxjob_action_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('ePrintFaxToPrinter',1),('eDeleteFaxFromMemory',3)))
_Faxjob_action_Type.__name__=_C
_Faxjob_action_Object=MibScalar
faxjob_action=_Faxjob_action_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,1,1),_Faxjob_action_Type())
faxjob_action.setMaxAccess(_D)
if mibBuilder.loadTexts:faxjob_action.setStatus(_A)
_Faxjob_action_id_Type=Integer32
_Faxjob_action_id_Object=MibScalar
faxjob_action_id=_Faxjob_action_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,1,2),_Faxjob_action_id_Type())
faxjob_action_id.setMaxAccess(_D)
if mibBuilder.loadTexts:faxjob_action_id.setStatus(_A)
class _Faxjob_tx_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,5,9)));namedValues=NamedValues(*(('eSrcHostOnly',2),('eSrcScannerOnly',5),('eSrcHostToMemoryOnly',9)))
_Faxjob_tx_type_Type.__name__=_C
_Faxjob_tx_type_Object=MibScalar
faxjob_tx_type=_Faxjob_tx_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,1,3),_Faxjob_tx_type_Type())
faxjob_tx_type.setMaxAccess(_D)
if mibBuilder.loadTexts:faxjob_tx_type.setStatus(_A)
_Status_fax_job_ObjectIdentity=ObjectIdentity
status_fax_job=_Status_fax_job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,2))
_Faxjob_download_id_Type=Integer32
_Faxjob_download_id_Object=MibScalar
faxjob_download_id=_Faxjob_download_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,2,1),_Faxjob_download_id_Type())
faxjob_download_id.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_download_id.setStatus(_A)
_Faxjob_rx_id_Type=Integer32
_Faxjob_rx_id_Object=MibScalar
faxjob_rx_id=_Faxjob_rx_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,2,2),_Faxjob_rx_id_Type())
faxjob_rx_id.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_rx_id.setStatus(_A)
_Faxjob_tx_id_Type=Integer32
_Faxjob_tx_id_Object=MibScalar
faxjob_tx_id=_Faxjob_tx_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,2,3),_Faxjob_tx_id_Type())
faxjob_tx_id.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_tx_id.setStatus(_A)
_Faxjob_upload_id_Type=Integer32
_Faxjob_upload_id_Object=MibScalar
faxjob_upload_id=_Faxjob_upload_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,2,4),_Faxjob_upload_id_Type())
faxjob_upload_id.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_upload_id.setStatus(_A)
_Faxjob_ObjectIdentity=ObjectIdentity
faxjob=_Faxjob_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3))
_Faxjob_rx_status_ObjectIdentity=ObjectIdentity
faxjob_rx_status=_Faxjob_rx_status_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,1))
class _Faxjob_rx_status_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eFaxRxIdle',1),('eFaxRxRinging',2),('eFaxRxAnswering',3),('eFaxRxReceiving',4)))
_Faxjob_rx_status_1_Type.__name__=_C
_Faxjob_rx_status_1_Object=MibScalar
faxjob_rx_status_1=_Faxjob_rx_status_1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,1,1),_Faxjob_rx_status_1_Type())
faxjob_rx_status_1.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_rx_status_1.setStatus(_A)
_Faxjob_tx_status_ObjectIdentity=ObjectIdentity
faxjob_tx_status=_Faxjob_tx_status_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,3))
class _Faxjob_tx_status_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eFaxTxIdle',1),('eFaxTxDialing',2),('eFaxTxConnecting',3),('eFaxTxTransmitting',4)))
_Faxjob_tx_status_1_Type.__name__=_C
_Faxjob_tx_status_1_Object=MibScalar
faxjob_tx_status_1=_Faxjob_tx_status_1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,3,1),_Faxjob_tx_status_1_Type())
faxjob_tx_status_1.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_tx_status_1.setStatus(_A)
_Faxjob_tx_error_ObjectIdentity=ObjectIdentity
faxjob_tx_error=_Faxjob_tx_error_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,4))
_Faxjob_tx_error_1_Type=Integer32
_Faxjob_tx_error_1_Object=MibScalar
faxjob_tx_error_1=_Faxjob_tx_error_1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,4,1),_Faxjob_tx_error_1_Type())
faxjob_tx_error_1.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_tx_error_1.setStatus(_A)
_Faxjob_tx_current_page_ObjectIdentity=ObjectIdentity
faxjob_tx_current_page=_Faxjob_tx_current_page_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,5))
_Faxjob_tx_current_page_1_Type=Integer32
_Faxjob_tx_current_page_1_Object=MibScalar
faxjob_tx_current_page_1=_Faxjob_tx_current_page_1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,5,1),_Faxjob_tx_current_page_1_Type())
faxjob_tx_current_page_1.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_tx_current_page_1.setStatus(_A)
_Faxjob_rx_current_page_ObjectIdentity=ObjectIdentity
faxjob_rx_current_page=_Faxjob_rx_current_page_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,6))
_Faxjob_rx_current_page_1_Type=Integer32
_Faxjob_rx_current_page_1_Object=MibScalar
faxjob_rx_current_page_1=_Faxjob_rx_current_page_1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,6,1),_Faxjob_rx_current_page_1_Type())
faxjob_rx_current_page_1.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_rx_current_page_1.setStatus(_A)
_Faxjob_rx_duration_ObjectIdentity=ObjectIdentity
faxjob_rx_duration=_Faxjob_rx_duration_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,7))
_Faxjob_rx_duration_1_Type=Integer32
_Faxjob_rx_duration_1_Object=MibScalar
faxjob_rx_duration_1=_Faxjob_rx_duration_1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,7,1),_Faxjob_rx_duration_1_Type())
faxjob_rx_duration_1.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_rx_duration_1.setStatus(_A)
_Faxjob_tx_duration_ObjectIdentity=ObjectIdentity
faxjob_tx_duration=_Faxjob_tx_duration_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,8))
_Faxjob_tx_duration_1_Type=Integer32
_Faxjob_tx_duration_1_Object=MibScalar
faxjob_tx_duration_1=_Faxjob_tx_duration_1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,3,3,8,1),_Faxjob_tx_duration_1_Type())
faxjob_tx_duration_1.setMaxAccess(_B)
if mibBuilder.loadTexts:faxjob_tx_duration_1.setStatus(_A)
_Fax_activity_log_ObjectIdentity=ObjectIdentity
fax_activity_log=_Fax_activity_log_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,4))
_Settings_faxlog_ObjectIdentity=ObjectIdentity
settings_faxlog=_Settings_faxlog_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,4,1))
class _Fax_log_action_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eIdle',1),('eClear',2),('ePrintLatest',3),('ePrintAll',4)))
_Fax_log_action_Type.__name__=_C
_Fax_log_action_Object=MibScalar
fax_log_action=_Fax_log_action_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,4,1,1),_Fax_log_action_Type())
fax_log_action.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_log_action.setStatus(_A)
class _Fax_log_reporting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),('eErrorOnly',2),('eSendOnly',3)))
_Fax_log_reporting_Type.__name__=_C
_Fax_log_reporting_Object=MibScalar
fax_log_reporting=_Fax_log_reporting_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,4,1,2),_Fax_log_reporting_Type())
fax_log_reporting.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_log_reporting.setStatus(_A)
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
_Phone_ObjectIdentity=ObjectIdentity
phone=_Phone_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9))
_Dial_ObjectIdentity=ObjectIdentity
dial=_Dial_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9,1))
_Dial_all_lines_ObjectIdentity=ObjectIdentity
dial_all_lines=_Dial_all_lines_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9,1,1))
class _Fax_dial_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eToneDial',1),('ePulseDial',2)))
_Fax_dial_mode_Type.__name__=_C
_Fax_dial_mode_Object=MibScalar
fax_dial_mode=_Fax_dial_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9,1,1,1),_Fax_dial_mode_Type())
fax_dial_mode.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_dial_mode.setStatus(_A)
_Device_redial_Type=OctetString
_Device_redial_Object=MibScalar
device_redial=_Device_redial_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9,1,1,2),_Device_redial_Type())
device_redial.setMaxAccess(_D)
if mibBuilder.loadTexts:device_redial.setStatus(_A)
_Answer_ObjectIdentity=ObjectIdentity
answer=_Answer_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9,2))
_Answer_all_lines_ObjectIdentity=ObjectIdentity
answer_all_lines=_Answer_all_lines_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9,2,1))
class _Fax_answer_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eManualAnswer',1),('eFaxAnswer',2)))
_Fax_answer_mode_Type.__name__=_C
_Fax_answer_mode_Object=MibScalar
fax_answer_mode=_Fax_answer_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9,2,1,1),_Fax_answer_mode_Type())
fax_answer_mode.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_answer_mode.setStatus(_A)
class _Fax_num_rings_pickup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Fax_num_rings_pickup_Type.__name__=_C
_Fax_num_rings_pickup_Object=MibScalar
fax_num_rings_pickup=_Fax_num_rings_pickup_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9,2,1,2),_Fax_num_rings_pickup_Type())
fax_num_rings_pickup.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_num_rings_pickup.setStatus(_A)
_Device_ring_type_pickup_Type=OctetString
_Device_ring_type_pickup_Object=MibScalar
device_ring_type_pickup=_Device_ring_type_pickup_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,9,2,1,3),_Device_ring_type_pickup_Type())
device_ring_type_pickup.setMaxAccess(_D)
if mibBuilder.loadTexts:device_ring_type_pickup.setStatus(_A)
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
_Scanner_ObjectIdentity=ObjectIdentity
scanner=_Scanner_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2))
_Settings_scanner_ObjectIdentity=ObjectIdentity
settings_scanner=_Settings_scanner_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1))
class _Scan_contrast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_Scan_contrast_Type.__name__=_C
_Scan_contrast_Object=MibScalar
scan_contrast=_Scan_contrast_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,1),_Scan_contrast_Type())
scan_contrast.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_contrast.setStatus(_A)
class _Scan_resolution_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_Scan_resolution_Type.__name__=_E
_Scan_resolution_Object=MibScalar
scan_resolution=_Scan_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,2),_Scan_resolution_Type())
scan_resolution.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_resolution.setStatus(_A)
class _Scan_pixel_data_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,8,24)));namedValues=NamedValues(*((_i,1),('eGrey256',8),('e24BitColor',24)))
_Scan_pixel_data_type_Type.__name__=_C
_Scan_pixel_data_type_Object=MibScalar
scan_pixel_data_type=_Scan_pixel_data_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,3),_Scan_pixel_data_type_Type())
scan_pixel_data_type.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_pixel_data_type.setStatus(_A)
class _Scan_compression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6)));namedValues=NamedValues(*(('eCompressNone',1),('eCompressDefault',2),('eCompressionMMR',5),('eCompressionJPEG',6)))
_Scan_compression_Type.__name__=_C
_Scan_compression_Object=MibScalar
scan_compression=_Scan_compression_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,4),_Scan_compression_Type())
scan_compression.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_compression.setStatus(_A)
class _Scan_compression_factor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Scan_compression_factor_Type.__name__=_C
_Scan_compression_factor_Object=MibScalar
scan_compression_factor=_Scan_compression_factor_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,5),_Scan_compression_factor_Type())
scan_compression_factor.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_compression_factor.setStatus(_A)
_Scan_upload_error_Type=Integer32
_Scan_upload_error_Object=MibScalar
scan_upload_error=_Scan_upload_error_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,6),_Scan_upload_error_Type())
scan_upload_error.setMaxAccess(_B)
if mibBuilder.loadTexts:scan_upload_error.setStatus(_A)
class _Scan_upload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('eScanUploadIdle',1),('eScanUploadStart',2),('eScanUploadActive',3),('eScanUploadAborted',4),('eScanUploadDone',5),('eScanUploadNewPage',6)))
_Scan_upload_Type.__name__=_C
_Scan_upload_Object=MibScalar
scan_upload=_Scan_upload_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,12),_Scan_upload_Type())
scan_upload.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_upload.setStatus(_A)
class _Default_scanner_margin_left_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5088))
_Default_scanner_margin_left_Type.__name__=_C
_Default_scanner_margin_left_Object=MibScalar
default_scanner_margin_left=_Default_scanner_margin_left_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,16),_Default_scanner_margin_left_Type())
default_scanner_margin_left.setMaxAccess(_D)
if mibBuilder.loadTexts:default_scanner_margin_left.setStatus(_A)
class _Default_scanner_margin_right_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,5120))
_Default_scanner_margin_right_Type.__name__=_C
_Default_scanner_margin_right_Object=MibScalar
default_scanner_margin_right=_Default_scanner_margin_right_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,17),_Default_scanner_margin_right_Type())
default_scanner_margin_right.setMaxAccess(_D)
if mibBuilder.loadTexts:default_scanner_margin_right.setStatus(_A)
_Scan_calibration_ObjectIdentity=ObjectIdentity
scan_calibration=_Scan_calibration_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,32))
class _Scan_calibration_target_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eWhiteSheet',1),('ePlaten',2)))
_Scan_calibration_target_Type.__name__=_C
_Scan_calibration_target_Object=MibScalar
scan_calibration_target=_Scan_calibration_target_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,32,18),_Scan_calibration_target_Type())
scan_calibration_target.setMaxAccess(_B)
if mibBuilder.loadTexts:scan_calibration_target.setStatus(_A)
_Ui_add_option_Type=DisplayString
_Ui_add_option_Object=MibScalar
ui_add_option=_Ui_add_option_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,37),_Ui_add_option_Type())
ui_add_option.setMaxAccess(_H)
if mibBuilder.loadTexts:ui_add_option.setStatus(_A)
_Ui_select_option_Type=DisplayString
_Ui_select_option_Object=MibScalar
ui_select_option=_Ui_select_option_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,38),_Ui_select_option_Type())
ui_select_option.setMaxAccess(_B)
if mibBuilder.loadTexts:ui_select_option.setStatus(_A)
_Ui_delete_option_Type=DisplayString
_Ui_delete_option_Object=MibScalar
ui_delete_option=_Ui_delete_option_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,42),_Ui_delete_option_Type())
ui_delete_option.setMaxAccess(_H)
if mibBuilder.loadTexts:ui_delete_option.setStatus(_A)
_Scanner_jam_page_count_Type=Integer32
_Scanner_jam_page_count_Object=MibScalar
scanner_jam_page_count=_Scanner_jam_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,43),_Scanner_jam_page_count_Type())
scanner_jam_page_count.setMaxAccess(_D)
if mibBuilder.loadTexts:scanner_jam_page_count.setStatus(_A)
_Scanner_adf_page_count_Type=Integer32
_Scanner_adf_page_count_Object=MibScalar
scanner_adf_page_count=_Scanner_adf_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,44),_Scanner_adf_page_count_Type())
scanner_adf_page_count.setMaxAccess(_D)
if mibBuilder.loadTexts:scanner_adf_page_count.setStatus(_A)
_Scan_adf_page_count_Type=Integer32
_Scan_adf_page_count_Object=MibScalar
scan_adf_page_count=_Scan_adf_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,45),_Scan_adf_page_count_Type())
scan_adf_page_count.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_adf_page_count.setStatus(_A)
class _Scan_image_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eText',1),('ePhoto',2),('eMixed',3)))
_Scan_image_type_Type.__name__=_C
_Scan_image_type_Object=MibScalar
scan_image_type=_Scan_image_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,46),_Scan_image_type_Type())
scan_image_type.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_image_type.setStatus(_A)
class _Scan_subsample_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eFourToOneToOne',1),('eFourToTwoToTwo',2),('eFourToThreeToThree',3),('eFourToFourToFour',4)))
_Scan_subsample_Type.__name__=_C
_Scan_subsample_Object=MibScalar
scan_subsample=_Scan_subsample_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,47),_Scan_subsample_Type())
scan_subsample.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_subsample.setStatus(_A)
_Scanner_retrieve_scanline_Type=OctetString
_Scanner_retrieve_scanline_Object=MibScalar
scanner_retrieve_scanline=_Scanner_retrieve_scanline_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,48),_Scanner_retrieve_scanline_Type())
scanner_retrieve_scanline.setMaxAccess(_D)
if mibBuilder.loadTexts:scanner_retrieve_scanline.setStatus(_A)
_Scanner_motor_control_Type=Integer32
_Scanner_motor_control_Object=MibScalar
scanner_motor_control=_Scanner_motor_control_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,49),_Scanner_motor_control_Type())
scanner_motor_control.setMaxAccess(_D)
if mibBuilder.loadTexts:scanner_motor_control.setStatus(_A)
class _Scan_height_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25200))
_Scan_height_Type.__name__=_C
_Scan_height_Object=MibScalar
scan_height=_Scan_height_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,50),_Scan_height_Type())
scan_height.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_height.setStatus(_A)
_Scanner_scanline_statistics_Type=DisplayString
_Scanner_scanline_statistics_Object=MibScalar
scanner_scanline_statistics=_Scanner_scanline_statistics_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,51),_Scanner_scanline_statistics_Type())
scanner_scanline_statistics.setMaxAccess(_B)
if mibBuilder.loadTexts:scanner_scanline_statistics.setStatus(_A)
_Scan_control_descriptor_Type=DisplayString
_Scan_control_descriptor_Object=MibScalar
scan_control_descriptor=_Scan_control_descriptor_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,52),_Scan_control_descriptor_Type())
scan_control_descriptor.setMaxAccess(_B)
if mibBuilder.loadTexts:scan_control_descriptor.setStatus(_A)
class _Scan_gamma_correction_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Scan_gamma_correction_Type.__name__=_E
_Scan_gamma_correction_Object=MibScalar
scan_gamma_correction=_Scan_gamma_correction_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,53),_Scan_gamma_correction_Type())
scan_gamma_correction.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_gamma_correction.setStatus(_A)
class _Scan_pad_image_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Scan_pad_image_Type.__name__=_C
_Scan_pad_image_Object=MibScalar
scan_pad_image=_Scan_pad_image_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,54),_Scan_pad_image_Type())
scan_pad_image.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_pad_image.setStatus(_A)
_Status_scanner_ObjectIdentity=ObjectIdentity
status_scanner=_Status_scanner_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,2))
_Not_ready_source_scanner_Type=OctetString
_Not_ready_source_scanner_Object=MibScalar
not_ready_source_scanner=_Not_ready_source_scanner_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,2,1),_Not_ready_source_scanner_Type())
not_ready_source_scanner.setMaxAccess(_B)
if mibBuilder.loadTexts:not_ready_source_scanner.setStatus(_A)
_Scan_resolution_range_Type=DisplayString
_Scan_resolution_range_Object=MibScalar
scan_resolution_range=_Scan_resolution_range_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,2,3),_Scan_resolution_range_Type())
scan_resolution_range.setMaxAccess(_B)
if mibBuilder.loadTexts:scan_resolution_range.setStatus(_A)
_Scan_calibration_download_Type=OctetString
_Scan_calibration_download_Object=MibScalar
scan_calibration_download=_Scan_calibration_download_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,2,5),_Scan_calibration_download_Type())
scan_calibration_download.setMaxAccess(_D)
if mibBuilder.loadTexts:scan_calibration_download.setStatus(_A)
class _Scan_calibration_error_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('eNoError',1),('eUnknownCalibrationError',2),('eScannerFeederEmpty',3),('eLowMemory',4),('eWriteFailed',5),('eScannerBusy',6),('eADFMispick',7),('eADFJam',8),('eUncorrectablePixels',9)))
_Scan_calibration_error_Type.__name__=_C
_Scan_calibration_error_Object=MibScalar
scan_calibration_error=_Scan_calibration_error_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,2,6),_Scan_calibration_error_Type())
scan_calibration_error.setMaxAccess(_B)
if mibBuilder.loadTexts:scan_calibration_error.setStatus(_A)
class _Scanner_button_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Scanner_button_status_Type.__name__=_C
_Scanner_button_status_Object=MibScalar
scanner_button_status=_Scanner_button_status_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,2,7),_Scanner_button_status_Type())
scanner_button_status.setMaxAccess(_D)
if mibBuilder.loadTexts:scanner_button_status.setStatus(_A)
_Fax_receive_ObjectIdentity=ObjectIdentity
fax_receive=_Fax_receive_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,3))
_Settings_fax_receive_ObjectIdentity=ObjectIdentity
settings_fax_receive=_Settings_fax_receive_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,3,1))
class _Fax_receive_stamping_enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Fax_receive_stamping_enable_Type.__name__=_C
_Fax_receive_stamping_enable_Object=MibScalar
fax_receive_stamping_enable=_Fax_receive_stamping_enable_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,3,1,1),_Fax_receive_stamping_enable_Type())
fax_receive_stamping_enable.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_receive_stamping_enable.setStatus(_A)
_Status_fax_receive_ObjectIdentity=ObjectIdentity
status_fax_receive=_Status_fax_receive_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,3,2))
_Not_ready_fax_receive_Type=OctetString
_Not_ready_fax_receive_Object=MibScalar
not_ready_fax_receive=_Not_ready_fax_receive_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,3,2,1),_Not_ready_fax_receive_Type())
not_ready_fax_receive.setMaxAccess(_B)
if mibBuilder.loadTexts:not_ready_fax_receive.setStatus(_A)
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
class _Form_feed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_g,1))
_Form_feed_Type.__name__=_C
_Form_feed_Object=MibScalar
form_feed=_Form_feed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,5),_Form_feed_Type())
form_feed.setMaxAccess(_H)
if mibBuilder.loadTexts:form_feed.setStatus(_A)
_Maximum_resource_saving_memory_Type=Integer32
_Maximum_resource_saving_memory_Object=MibScalar
maximum_resource_saving_memory=_Maximum_resource_saving_memory_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,7),_Maximum_resource_saving_memory_Type())
maximum_resource_saving_memory.setMaxAccess(_B)
if mibBuilder.loadTexts:maximum_resource_saving_memory.setStatus(_A)
_Default_vertical_black_resolution_Type=Integer32
_Default_vertical_black_resolution_Object=MibScalar
default_vertical_black_resolution=_Default_vertical_black_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,8),_Default_vertical_black_resolution_Type())
default_vertical_black_resolution.setMaxAccess(_D)
if mibBuilder.loadTexts:default_vertical_black_resolution.setStatus(_A)
_Default_horizontal_black_resolution_Type=Integer32
_Default_horizontal_black_resolution_Object=MibScalar
default_horizontal_black_resolution=_Default_horizontal_black_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,9),_Default_horizontal_black_resolution_Type())
default_horizontal_black_resolution.setMaxAccess(_D)
if mibBuilder.loadTexts:default_horizontal_black_resolution.setStatus(_A)
class _Default_page_protect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_J,2),('eAuto',3)))
_Default_page_protect_Type.__name__=_C
_Default_page_protect_Object=MibScalar
default_page_protect=_Default_page_protect_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,10),_Default_page_protect_Type())
default_page_protect.setMaxAccess(_D)
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
class _Default_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,17,25,26,45,71,72,80,81,90,91,100,101)));namedValues=NamedValues(*((_j,1),(_N,2),(_Y,3),(_k,10),(_l,17),(_m,25),(_O,26),(_n,45),(_o,71),(_p,72),(_q,80),(_r,81),(_s,90),(_t,91),(_u,100),(_v,101)))
_Default_media_size_Type.__name__=_C
_Default_media_size_Object=MibScalar
default_media_size=_Default_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,13),_Default_media_size_Type())
default_media_size.setMaxAccess(_D)
if mibBuilder.loadTexts:default_media_size.setStatus(_A)
class _Cold_reset_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,26)));namedValues=NamedValues(*((_N,2),(_O,26)))
_Cold_reset_media_size_Type.__name__=_C
_Cold_reset_media_size_Object=MibScalar
cold_reset_media_size=_Cold_reset_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,19),_Cold_reset_media_size_Type())
cold_reset_media_size.setMaxAccess(_D)
if mibBuilder.loadTexts:cold_reset_media_size.setStatus(_A)
class _Reprint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('eAuto',3)))
_Reprint_Type.__name__=_C
_Reprint_Object=MibScalar
reprint=_Reprint_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,36),_Reprint_Type())
reprint.setMaxAccess(_D)
if mibBuilder.loadTexts:reprint.setStatus(_A)
class _Wide_a4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Wide_a4_Type.__name__=_C
_Wide_a4_Object=MibScalar
wide_a4=_Wide_a4_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,37),_Wide_a4_Type())
wide_a4.setMaxAccess(_D)
if mibBuilder.loadTexts:wide_a4.setStatus(_A)
class _Dark_courier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Dark_courier_Type.__name__=_C
_Dark_courier_Object=MibScalar
dark_courier=_Dark_courier_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,38),_Dark_courier_Type())
dark_courier.setMaxAccess(_D)
if mibBuilder.loadTexts:dark_courier.setStatus(_A)
_Default_bits_per_pixel_Type=Integer32
_Default_bits_per_pixel_Object=MibScalar
default_bits_per_pixel=_Default_bits_per_pixel_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,39),_Default_bits_per_pixel_Type())
default_bits_per_pixel.setMaxAccess(_D)
if mibBuilder.loadTexts:default_bits_per_pixel.setStatus(_A)
_Status_pdl_ObjectIdentity=ObjectIdentity
status_pdl=_Status_pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,2))
class _Form_feed_needed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_Form_feed_needed_Type.__name__=_C
_Form_feed_needed_Object=MibScalar
form_feed_needed=_Form_feed_needed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,2,2),_Form_feed_needed_Type())
form_feed_needed.setMaxAccess(_B)
if mibBuilder.loadTexts:form_feed_needed.setStatus(_A)
_Pdl_pcl_ObjectIdentity=ObjectIdentity
pdl_pcl=_Pdl_pcl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3))
_Pcl_resource_saving_memory_size_Type=Integer32
_Pcl_resource_saving_memory_size_Object=MibScalar
pcl_resource_saving_memory_size=_Pcl_resource_saving_memory_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,2),_Pcl_resource_saving_memory_size_Type())
pcl_resource_saving_memory_size.setMaxAccess(_D)
if mibBuilder.loadTexts:pcl_resource_saving_memory_size.setStatus(_A)
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
_Pcl_default_font_width_Type=Integer32
_Pcl_default_font_width_Object=MibScalar
pcl_default_font_width=_Pcl_default_font_width_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,16),_Pcl_default_font_width_Type())
pcl_default_font_width.setMaxAccess(_D)
if mibBuilder.loadTexts:pcl_default_font_width.setStatus(_A)
_Pjl_ObjectIdentity=ObjectIdentity
pjl=_Pjl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,5))
_Pjl_password_Type=Integer32
_Pjl_password_Object=MibScalar
pjl_password=_Pjl_password_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,5,1),_Pjl_password_Type())
pjl_password.setMaxAccess(_B)
if mibBuilder.loadTexts:pjl_password.setStatus(_A)
_Fax_proc_sub_ObjectIdentity=ObjectIdentity
fax_proc_sub=_Fax_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7))
_Settings_fax_proc_sub_ObjectIdentity=ObjectIdentity
settings_fax_proc_sub=_Settings_fax_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1))
_Fax_rxscale_Type=Integer32
_Fax_rxscale_Object=MibScalar
fax_rxscale=_Fax_rxscale_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,1),_Fax_rxscale_Type())
fax_rxscale.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_rxscale.setStatus(_A)
class _Fax_noise_volume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Fax_noise_volume_Type.__name__=_C
_Fax_noise_volume_Object=MibScalar
fax_noise_volume=_Fax_noise_volume_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,3),_Fax_noise_volume_Type())
fax_noise_volume.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_noise_volume.setStatus(_A)
class _Fax_download_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('eFaxDownloadIdle',1),('eFaxDownloadStart',2),('eFaxDownloadActive',3),('eFaxDownloadAborted',4),('eFaxDownloadDone',5)))
_Fax_download_Type.__name__=_C
_Fax_download_Object=MibScalar
fax_download=_Fax_download_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,6),_Fax_download_Type())
fax_download.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_download.setStatus(_A)
class _Fax_silent_detection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Fax_silent_detection_Type.__name__=_C
_Fax_silent_detection_Object=MibScalar
fax_silent_detection=_Fax_silent_detection_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,7),_Fax_silent_detection_Type())
fax_silent_detection.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_silent_detection.setStatus(_A)
class _Fax_ring_enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Fax_ring_enable_Type.__name__=_C
_Fax_ring_enable_Object=MibScalar
fax_ring_enable=_Fax_ring_enable_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,8),_Fax_ring_enable_Type())
fax_ring_enable.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_ring_enable.setStatus(_A)
class _Fax_country_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,13,14,15,19,21,23,27,29,30,31,34,35,37,39,40,41,43,44,45,46,47,51,55,56,62,63,64)));namedValues=NamedValues(*(('eChina',6),('eMexicoAndLatinAmerica',13),('eCanadaFrench',14),('eUnitedStatesAndCanadaEnglish',15),('eNewZealand',19),('eIsrael',21),('eAustralia',23),('eMalaysia',27),('eHongKong',29),('eSingapore',30),('eUnitedKingdom',31),('eAustria',34),('eNetherlands',35),('eSwitzerlandFrench',37),('eGermany',39),('eDenmark',40),('eSweden',41),('eNorway',43),('eIreland',44),('eBelgium',45),('eFinland',46),('eFrance',47),('eItaly',51),('eSpain',55),('ePoland',56),('eHungary',62),('eUkraine',63),('eRussia',64)))
_Fax_country_Type.__name__=_C
_Fax_country_Object=MibScalar
fax_country=_Fax_country_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,9),_Fax_country_Type())
fax_country.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_country.setStatus(_A)
_Fax_tx_phone_number_Type=DisplayString
_Fax_tx_phone_number_Object=MibScalar
fax_tx_phone_number=_Fax_tx_phone_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,10),_Fax_tx_phone_number_Type())
fax_tx_phone_number.setMaxAccess(_H)
if mibBuilder.loadTexts:fax_tx_phone_number.setStatus(_A)
_Fax_redial_time_Type=Integer32
_Fax_redial_time_Object=MibScalar
fax_redial_time=_Fax_redial_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,14),_Fax_redial_time_Type())
fax_redial_time.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_redial_time.setStatus(_A)
_Fax_pstn_access_code_Type=DisplayString
_Fax_pstn_access_code_Object=MibScalar
fax_pstn_access_code=_Fax_pstn_access_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,18),_Fax_pstn_access_code_Type())
fax_pstn_access_code.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_pstn_access_code.setStatus(_A)
class _Fax_rx_disposition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,6)));namedValues=NamedValues(*(('ePrintOnly',1),('eUploadOnly',2),('eUploadElsePrint',4),('eForwardElsePrint',6)))
_Fax_rx_disposition_Type.__name__=_C
_Fax_rx_disposition_Object=MibScalar
fax_rx_disposition=_Fax_rx_disposition_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,19),_Fax_rx_disposition_Type())
fax_rx_disposition.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_rx_disposition.setStatus(_A)
class _Fax_error_correction_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Fax_error_correction_mode_Type.__name__=_C
_Fax_error_correction_mode_Object=MibScalar
fax_error_correction_mode=_Fax_error_correction_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,21),_Fax_error_correction_mode_Type())
fax_error_correction_mode.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_error_correction_mode.setStatus(_A)
class _Fax_report_transmission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('eNone',1),('ePrintReport',2),('ePrintReportOnSend',3),('ePrintReportOnError',4),('ePrintReportOnSendError',5),('ePrintReportOnReceiveError',6)))
_Fax_report_transmission_Type.__name__=_C
_Fax_report_transmission_Object=MibScalar
fax_report_transmission=_Fax_report_transmission_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,22),_Fax_report_transmission_Type())
fax_report_transmission.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_report_transmission.setStatus(_A)
class _Fax_report_activity_log_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),('eThreshold',2)))
_Fax_report_activity_log_Type.__name__=_C
_Fax_report_activity_log_Object=MibScalar
fax_report_activity_log=_Fax_report_activity_log_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,23),_Fax_report_activity_log_Type())
fax_report_activity_log.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_report_activity_log.setStatus(_A)
class _Fax_dial_tone_detection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Fax_dial_tone_detection_Type.__name__=_C
_Fax_dial_tone_detection_Object=MibScalar
fax_dial_tone_detection=_Fax_dial_tone_detection_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,24),_Fax_dial_tone_detection_Type())
fax_dial_tone_detection.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_dial_tone_detection.setStatus(_A)
class _Fax_alarm_volume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Fax_alarm_volume_Type.__name__=_C
_Fax_alarm_volume_Object=MibScalar
fax_alarm_volume=_Fax_alarm_volume_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,25),_Fax_alarm_volume_Type())
fax_alarm_volume.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_alarm_volume.setStatus(_A)
class _Fax_beep_volume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Fax_beep_volume_Type.__name__=_C
_Fax_beep_volume_Object=MibScalar
fax_beep_volume=_Fax_beep_volume_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,26),_Fax_beep_volume_Type())
fax_beep_volume.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_beep_volume.setStatus(_A)
class _Fax_ring_volume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Fax_ring_volume_Type.__name__=_C
_Fax_ring_volume_Object=MibScalar
fax_ring_volume=_Fax_ring_volume_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,27),_Fax_ring_volume_Type())
fax_ring_volume.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_ring_volume.setStatus(_A)
_Fax_master_host_Type=DisplayString
_Fax_master_host_Object=MibScalar
fax_master_host=_Fax_master_host_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,28),_Fax_master_host_Type())
fax_master_host.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_master_host.setStatus(_A)
class _Fax_thumbnail_enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Fax_thumbnail_enable_Type.__name__=_C
_Fax_thumbnail_enable_Object=MibScalar
fax_thumbnail_enable=_Fax_thumbnail_enable_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,29),_Fax_thumbnail_enable_Type())
fax_thumbnail_enable.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_thumbnail_enable.setStatus(_A)
class _Fax_phone_pickup_enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_Fax_phone_pickup_enable_Type.__name__=_C
_Fax_phone_pickup_enable_Object=MibScalar
fax_phone_pickup_enable=_Fax_phone_pickup_enable_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,30),_Fax_phone_pickup_enable_Type())
fax_phone_pickup_enable.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_phone_pickup_enable.setStatus(_A)
_Status_fax_proc_sub_ObjectIdentity=ObjectIdentity
status_fax_proc_sub=_Status_fax_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2))
class _Fax_upload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('eFaxUploadIdle',1),('eFaxUploadStart',2),('eFaxUploadActive',3),('eFaxUploadAborted',4),('eFaxUploadDone',5),('eFaxUploadNeeded',6)))
_Fax_upload_Type.__name__=_C
_Fax_upload_Object=MibScalar
fax_upload=_Fax_upload_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,1),_Fax_upload_Type())
fax_upload.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_upload.setStatus(_A)
class _Fax_min_rings_pickup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Fax_min_rings_pickup_Type.__name__=_C
_Fax_min_rings_pickup_Object=MibScalar
fax_min_rings_pickup=_Fax_min_rings_pickup_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,2),_Fax_min_rings_pickup_Type())
fax_min_rings_pickup.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_min_rings_pickup.setStatus(_A)
class _Fax_max_rings_pickup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Fax_max_rings_pickup_Type.__name__=_C
_Fax_max_rings_pickup_Object=MibScalar
fax_max_rings_pickup=_Fax_max_rings_pickup_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,3),_Fax_max_rings_pickup_Type())
fax_max_rings_pickup.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_max_rings_pickup.setStatus(_A)
_Fax_max_redials_Type=Integer32
_Fax_max_redials_Object=MibScalar
fax_max_redials=_Fax_max_redials_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,4),_Fax_max_redials_Type())
fax_max_redials.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_max_redials.setStatus(_A)
_Fax_additional_wait_Type=Integer32
_Fax_additional_wait_Object=MibScalar
fax_additional_wait=_Fax_additional_wait_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,5),_Fax_additional_wait_Type())
fax_additional_wait.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_additional_wait.setStatus(_A)
_Fax_download_error_Type=Integer32
_Fax_download_error_Object=MibScalar
fax_download_error=_Fax_download_error_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,6),_Fax_download_error_Type())
fax_download_error.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_download_error.setStatus(_A)
_Fax_upload_error_Type=Integer32
_Fax_upload_error_Object=MibScalar
fax_upload_error=_Fax_upload_error_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,7),_Fax_upload_error_Type())
fax_upload_error.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_upload_error.setStatus(_A)
class _Fax_firmware_revision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Fax_firmware_revision_Type.__name__=_M
_Fax_firmware_revision_Object=MibScalar
fax_firmware_revision=_Fax_firmware_revision_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,8),_Fax_firmware_revision_Type())
fax_firmware_revision.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_firmware_revision.setStatus(_A)
_Fax_forwarding_ObjectIdentity=ObjectIdentity
fax_forwarding=_Fax_forwarding_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,3))
_Fax_forwarding_phone_num_Type=DisplayString
_Fax_forwarding_phone_num_Object=MibScalar
fax_forwarding_phone_num=_Fax_forwarding_phone_num_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,3,3),_Fax_forwarding_phone_num_Type())
fax_forwarding_phone_num.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_forwarding_phone_num.setStatus(_A)
_Destination_subsystem_ObjectIdentity=ObjectIdentity
destination_subsystem=_Destination_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4))
_Print_engine_ObjectIdentity=ObjectIdentity
print_engine=_Print_engine_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1))
_Settings_prt_eng_ObjectIdentity=ObjectIdentity
settings_prt_eng=_Settings_prt_eng_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1))
class _Override_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,17,25,26,45,71,72,80,81,90,91,100,101)));namedValues=NamedValues(*((_j,1),(_N,2),(_Y,3),(_k,10),(_l,17),(_m,25),(_O,26),(_n,45),(_o,71),(_p,72),(_q,80),(_r,81),(_s,90),(_t,91),(_u,100),(_v,101)))
_Override_media_size_Type.__name__=_C
_Override_media_size_Object=MibScalar
override_media_size=_Override_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,3),_Override_media_size_Type())
override_media_size.setMaxAccess(_D)
if mibBuilder.loadTexts:override_media_size.setStatus(_A)
class _Print_density_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Print_density_Type.__name__=_C
_Print_density_Object=MibScalar
print_density=_Print_density_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,1,5),_Print_density_Type())
print_density.setMaxAccess(_D)
if mibBuilder.loadTexts:print_density.setStatus(_A)
_Status_prt_eng_ObjectIdentity=ObjectIdentity
status_prt_eng=_Status_prt_eng_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2))
_Total_engine_page_count_Type=Integer32
_Total_engine_page_count_Object=MibScalar
total_engine_page_count=_Total_engine_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,5),_Total_engine_page_count_Type())
total_engine_page_count.setMaxAccess(_D)
if mibBuilder.loadTexts:total_engine_page_count.setStatus(_A)
_Print_engine_jam_count_Type=Integer32
_Print_engine_jam_count_Object=MibScalar
print_engine_jam_count=_Print_engine_jam_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,34),_Print_engine_jam_count_Type())
print_engine_jam_count.setMaxAccess(_D)
if mibBuilder.loadTexts:print_engine_jam_count.setStatus(_A)
_Print_engine_mispick_count_Type=Integer32
_Print_engine_mispick_count_Object=MibScalar
print_engine_mispick_count=_Print_engine_mispick_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,35),_Print_engine_mispick_count_Type())
print_engine_mispick_count.setMaxAccess(_D)
if mibBuilder.loadTexts:print_engine_mispick_count.setStatus(_A)
_Intray_ObjectIdentity=ObjectIdentity
intray=_Intray_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3))
_Settings_intray_ObjectIdentity=ObjectIdentity
settings_intray=_Settings_intray_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1))
class _Custom_paper_dim_unit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('eTenThousandthsOfInches',3),('eMicrometers',4)))
_Custom_paper_dim_unit_Type.__name__=_C
_Custom_paper_dim_unit_Object=MibScalar
custom_paper_dim_unit=_Custom_paper_dim_unit_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,7),_Custom_paper_dim_unit_Type())
custom_paper_dim_unit.setMaxAccess(_D)
if mibBuilder.loadTexts:custom_paper_dim_unit.setStatus(_A)
_Custom_paper_feed_dim_Type=Integer32
_Custom_paper_feed_dim_Object=MibScalar
custom_paper_feed_dim=_Custom_paper_feed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,8),_Custom_paper_feed_dim_Type())
custom_paper_feed_dim.setMaxAccess(_D)
if mibBuilder.loadTexts:custom_paper_feed_dim.setStatus(_A)
_Custom_paper_xfeed_dim_Type=Integer32
_Custom_paper_xfeed_dim_Object=MibScalar
custom_paper_xfeed_dim=_Custom_paper_xfeed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,9),_Custom_paper_xfeed_dim_Type())
custom_paper_xfeed_dim.setMaxAccess(_D)
if mibBuilder.loadTexts:custom_paper_xfeed_dim.setStatus(_A)
_Intrays_ObjectIdentity=ObjectIdentity
intrays=_Intrays_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3))
_Intray1_ObjectIdentity=ObjectIdentity
intray1=_Intray1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1))
class _Tray1_fuser_temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Tray1_fuser_temperature_Type.__name__=_C
_Tray1_fuser_temperature_Object=MibScalar
tray1_fuser_temperature=_Tray1_fuser_temperature_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,13),_Tray1_fuser_temperature_Type())
tray1_fuser_temperature.setMaxAccess(_D)
if mibBuilder.loadTexts:tray1_fuser_temperature.setStatus(_A)
_Imaging_ObjectIdentity=ObjectIdentity
imaging=_Imaging_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,6))
class _Default_ret_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('eLight',2),('eMedium',3),('eDark',4)))
_Default_ret_Type.__name__=_C
_Default_ret_Object=MibScalar
default_ret=_Default_ret_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,6,5),_Default_ret_Type())
default_ret.setMaxAccess(_D)
if mibBuilder.loadTexts:default_ret.setStatus(_A)
class _Default_print_quality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Default_print_quality_Type.__name__=_C
_Default_print_quality_Object=MibScalar
default_print_quality=_Default_print_quality_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,6,7),_Default_print_quality_Type())
default_print_quality.setMaxAccess(_D)
if mibBuilder.loadTexts:default_print_quality.setStatus(_A)
_Fax_send_ObjectIdentity=ObjectIdentity
fax_send=_Fax_send_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,2))
_Settings_fax_send_ObjectIdentity=ObjectIdentity
settings_fax_send=_Settings_fax_send_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,2,1))
class _Fax_resolution_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_Fax_resolution_Type.__name__=_E
_Fax_resolution_Object=MibScalar
fax_resolution=_Fax_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,2,1,1),_Fax_resolution_Type())
fax_resolution.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_resolution.setStatus(_A)
class _Fax_contrast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_Fax_contrast_Type.__name__=_C
_Fax_contrast_Object=MibScalar
fax_contrast=_Fax_contrast_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,2,1,2),_Fax_contrast_Type())
fax_contrast.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_contrast.setStatus(_A)
class _Fax_pixel_data_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),('eBiLevelHalfToned',2)))
_Fax_pixel_data_type_Type.__name__=_C
_Fax_pixel_data_type_Object=MibScalar
fax_pixel_data_type=_Fax_pixel_data_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,2,1,3),_Fax_pixel_data_type_Type())
fax_pixel_data_type.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_pixel_data_type.setStatus(_A)
_Status_fax_send_ObjectIdentity=ObjectIdentity
status_fax_send=_Status_fax_send_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,2,2))
_Not_ready_fax_send_Type=OctetString
_Not_ready_fax_send_Object=MibScalar
not_ready_fax_send=_Not_ready_fax_send_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,2,2,1),_Not_ready_fax_send_Type())
not_ready_fax_send.setMaxAccess(_B)
if mibBuilder.loadTexts:not_ready_fax_send.setStatus(_A)
_Transmit_fax_ObjectIdentity=ObjectIdentity
transmit_fax=_Transmit_fax_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,2,5))
class _Fax_allow_redials_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_Fax_allow_redials_Type.__name__=_C
_Fax_allow_redials_Object=MibScalar
fax_allow_redials=_Fax_allow_redials_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,2,5,3),_Fax_allow_redials_Type())
fax_allow_redials.setMaxAccess(_D)
if mibBuilder.loadTexts:fax_allow_redials.setStatus(_A)
_Copier_ObjectIdentity=ObjectIdentity
copier=_Copier_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,5))
_Settings_copier_ObjectIdentity=ObjectIdentity
settings_copier=_Settings_copier_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1))
class _Copier_contrast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_Copier_contrast_Type.__name__=_C
_Copier_contrast_Object=MibScalar
copier_contrast=_Copier_contrast_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,2),_Copier_contrast_Type())
copier_contrast.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_contrast.setStatus(_A)
class _Copier_reduction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,200))
_Copier_reduction_Type.__name__=_C
_Copier_reduction_Object=MibScalar
copier_reduction=_Copier_reduction_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,4),_Copier_reduction_Type())
copier_reduction.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_reduction.setStatus(_A)
class _Copier_num_copies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_Copier_num_copies_Type.__name__=_C
_Copier_num_copies_Object=MibScalar
copier_num_copies=_Copier_num_copies_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,6),_Copier_num_copies_Type())
copier_num_copies.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_num_copies.setStatus(_A)
class _Copier_collation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_w,1),(_x,2)))
_Copier_collation_Type.__name__=_C
_Copier_collation_Object=MibScalar
copier_collation=_Copier_collation_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,7),_Copier_collation_Type())
copier_collation.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_collation.setStatus(_A)
class _Copier_quality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_y,1),(_z,2),(_A0,3),(_A1,4)))
_Copier_quality_Type.__name__=_C
_Copier_quality_Object=MibScalar
copier_quality=_Copier_quality_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,13),_Copier_quality_Type())
copier_quality.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_quality.setStatus(_A)
_Copier_adf_page_count_Type=Integer32
_Copier_adf_page_count_Object=MibScalar
copier_adf_page_count=_Copier_adf_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,19),_Copier_adf_page_count_Type())
copier_adf_page_count.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_adf_page_count.setStatus(_A)
_Copier_print_page_count_Type=Integer32
_Copier_print_page_count_Object=MibScalar
copier_print_page_count=_Copier_print_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,20),_Copier_print_page_count_Type())
copier_print_page_count.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_print_page_count.setStatus(_A)
class _Copier_job_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,26)));namedValues=NamedValues(*((_N,2),(_Y,3),(_O,26)))
_Copier_job_media_size_Type.__name__=_C
_Copier_job_media_size_Object=MibScalar
copier_job_media_size=_Copier_job_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,21),_Copier_job_media_size_Type())
copier_job_media_size.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_job_media_size.setStatus(_A)
class _Copier_job_quality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_y,1),(_z,2),(_A0,3),(_A1,4)))
_Copier_job_quality_Type.__name__=_C
_Copier_job_quality_Object=MibScalar
copier_job_quality=_Copier_job_quality_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,22),_Copier_job_quality_Type())
copier_job_quality.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_job_quality.setStatus(_A)
class _Copier_job_collation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_w,1),(_x,2)))
_Copier_job_collation_Type.__name__=_C
_Copier_job_collation_Object=MibScalar
copier_job_collation=_Copier_job_collation_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,23),_Copier_job_collation_Type())
copier_job_collation.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_job_collation.setStatus(_A)
class _Copier_job_num_copies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_Copier_job_num_copies_Type.__name__=_C
_Copier_job_num_copies_Object=MibScalar
copier_job_num_copies=_Copier_job_num_copies_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,24),_Copier_job_num_copies_Type())
copier_job_num_copies.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_job_num_copies.setStatus(_A)
class _Copier_job_reduction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,200))
_Copier_job_reduction_Type.__name__=_C
_Copier_job_reduction_Object=MibScalar
copier_job_reduction=_Copier_job_reduction_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,25),_Copier_job_reduction_Type())
copier_job_reduction.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_job_reduction.setStatus(_A)
class _Copier_job_contrast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_Copier_job_contrast_Type.__name__=_C
_Copier_job_contrast_Object=MibScalar
copier_job_contrast=_Copier_job_contrast_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,26),_Copier_job_contrast_Type())
copier_job_contrast.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_job_contrast.setStatus(_A)
class _Copier_job_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('eCopierIdle',1),('eCopierStart',2),('eCopierActive',3),('eCopierAborting',4),('eCopierSetup',5)))
_Copier_job_Type.__name__=_C
_Copier_job_Object=MibScalar
copier_job=_Copier_job_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,5,1,27),_Copier_job_Type())
copier_job.setMaxAccess(_D)
if mibBuilder.loadTexts:copier_job.setStatus(_A)
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
_Printmib_ObjectIdentity=ObjectIdentity
printmib=_Printmib_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2))
_PrtGeneral_ObjectIdentity=ObjectIdentity
prtGeneral=_PrtGeneral_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5))
_PrtGeneralTable_ObjectIdentity=ObjectIdentity
prtGeneralTable=_PrtGeneralTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1))
_PrtGeneralEntry_ObjectIdentity=ObjectIdentity
prtGeneralEntry=_PrtGeneralEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1))
_Prtgeneralconfigchanges_Type=Integer32
_Prtgeneralconfigchanges_Object=MibScalar
prtgeneralconfigchanges=_Prtgeneralconfigchanges_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,1),_Prtgeneralconfigchanges_Type())
prtgeneralconfigchanges.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgeneralconfigchanges.setStatus(_A)
class _Prtgeneralcurrentlocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_Prtgeneralcurrentlocalization_Type.__name__=_C
_Prtgeneralcurrentlocalization_Object=MibScalar
prtgeneralcurrentlocalization=_Prtgeneralcurrentlocalization_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,2),_Prtgeneralcurrentlocalization_Type())
prtgeneralcurrentlocalization.setMaxAccess(_D)
if mibBuilder.loadTexts:prtgeneralcurrentlocalization.setStatus(_A)
class _Prtgeneralreset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5)));namedValues=NamedValues(*(('ePnotResetting',3),('ePresetToNVRAM',5)))
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
prtmediapathdefaultindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathdefaultindex.setStatus(_A)
class _Prtconsolelocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
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
class _Prtconsolenumberofdisplaychars_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Prtconsolenumberofdisplaychars_Type.__name__=_C
_Prtconsolenumberofdisplaychars_Object=MibScalar
prtconsolenumberofdisplaychars=_Prtconsolenumberofdisplaychars_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,12),_Prtconsolenumberofdisplaychars_Type())
prtconsolenumberofdisplaychars.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsolenumberofdisplaychars.setStatus(_A)
class _Prtconsoledisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues(('ePoperatorConsoleEnabled',3))
_Prtconsoledisable_Type.__name__=_C
_Prtconsoledisable_Object=MibScalar
prtconsoledisable=_Prtconsoledisable_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,13),_Prtconsoledisable_Type())
prtconsoledisable.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsoledisable.setStatus(_A)
class _Prtgeneralprintername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Prtgeneralprintername_Type.__name__=_E
_Prtgeneralprintername_Object=MibScalar
prtgeneralprintername=_Prtgeneralprintername_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,16),_Prtgeneralprintername_Type())
prtgeneralprintername.setMaxAccess(_D)
if mibBuilder.loadTexts:prtgeneralprintername.setStatus(_A)
class _Prtgeneralserialnumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
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
class _Prtcoverstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('ePdoorOpen',3),('ePdoorClosed',4)))
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
class _Prtlocalizationcharacterset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,2004)));namedValues=NamedValues(*(('ePcsISOLatinCyrillic',8),(_Z,2004)))
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
class _Prtinputdimunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_P,3),(_a,4)))
_Prtinputdimunit_Type.__name__=_C
_Prtinputdimunit_Object=MibScalar
prtinputdimunit=_Prtinputdimunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,3),_Prtinputdimunit_Type())
prtinputdimunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputdimunit.setStatus(_A)
_Prtinputmediadimfeeddirdeclared_Type=Integer32
_Prtinputmediadimfeeddirdeclared_Object=MibScalar
prtinputmediadimfeeddirdeclared=_Prtinputmediadimfeeddirdeclared_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,4),_Prtinputmediadimfeeddirdeclared_Type())
prtinputmediadimfeeddirdeclared.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputmediadimfeeddirdeclared.setStatus(_A)
_Prtinputmediadimxfeeddirdeclared_Type=Integer32
_Prtinputmediadimxfeeddirdeclared_Object=MibScalar
prtinputmediadimxfeeddirdeclared=_Prtinputmediadimxfeeddirdeclared_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,5),_Prtinputmediadimxfeeddirdeclared_Type())
prtinputmediadimxfeeddirdeclared.setMaxAccess(_B)
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
class _Prtinputcapacityunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(8));namedValues=NamedValues(('ePsheets',8))
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
prtinputmedianame.setMaxAccess(_B)
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
class _Prtinputsecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_G,1),('ePon',3),('ePoff',4),('ePnotPresent',5)))
_Prtinputsecurity_Type.__name__=_C
_Prtinputsecurity_Object=MibScalar
prtinputsecurity=_Prtinputsecurity_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,19),_Prtinputsecurity_Type())
prtinputsecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputsecurity.setStatus(_A)
_PrtOutput_ObjectIdentity=ObjectIdentity
prtOutput=_PrtOutput_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,9))
_PrtOutputTable_ObjectIdentity=ObjectIdentity
prtOutputTable=_PrtOutputTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2))
_PrtOutputEntry_ObjectIdentity=ObjectIdentity
prtOutputEntry=_PrtOutputEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1))
class _Prtoutputtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_b,2),('ePremovableBin',3),('ePunRemovableBin',4),('ePcontinuousRollDevice',5),('ePmailBox',6),('ePcontinousFanFold',7)))
_Prtoutputtype_Type.__name__=_C
_Prtoutputtype_Object=MibScalar
prtoutputtype=_Prtoutputtype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,2),_Prtoutputtype_Type())
prtoutputtype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputtype.setStatus(_A)
class _Prtoutputcapacityunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,8,16,17)));namedValues=NamedValues(*((_P,3),(_a,4),('ePsheets',8),('ePfeet',16),('ePmeters',17)))
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
class _Prtmarkermarktech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(4));namedValues=NamedValues(('ePelectrophotographicLaser',4))
_Prtmarkermarktech_Type.__name__=_C
_Prtmarkermarktech_Object=MibScalar
prtmarkermarktech=_Prtmarkermarktech_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,2),_Prtmarkermarktech_Type())
prtmarkermarktech.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkermarktech.setStatus(_A)
class _Prtmarkercounterunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(7));namedValues=NamedValues(('ePimpressions',7))
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
class _Prtmarkeraddressabilityunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues((_P,3))
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
class _Prtmarkersuppliestype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues(('ePtoner',3))
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
class _Prtmarkersuppliessupplyunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(13));namedValues=NamedValues(('ePtenthsOfGrams',13))
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
_PrtMediaPath_ObjectIdentity=ObjectIdentity
prtMediaPath=_PrtMediaPath_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,13))
_PrtMediaPathTable_ObjectIdentity=ObjectIdentity
prtMediaPathTable=_PrtMediaPathTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4))
_PrtMediaPathEntry_ObjectIdentity=ObjectIdentity
prtMediaPathEntry=_PrtMediaPathEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1))
class _Prtmediapathmaxspeedprintunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(7));namedValues=NamedValues(('ePimpressionsPerHour',7))
_Prtmediapathmaxspeedprintunit_Type.__name__=_C
_Prtmediapathmaxspeedprintunit_Object=MibScalar
prtmediapathmaxspeedprintunit=_Prtmediapathmaxspeedprintunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,2),_Prtmediapathmaxspeedprintunit_Type())
prtmediapathmaxspeedprintunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathmaxspeedprintunit.setStatus(_A)
class _Prtmediapathmediasizeunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_P,3),(_a,4)))
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
class _Prtmediapathtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues(('ePsimplex',5))
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
class _Prtchanneltype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,7,10,11,15,34,35,38)));namedValues=NamedValues(*((_G,1),('ePchIEEE1284Port',5),('ePchAppleTalkPAP',7),('ePchNetwarePServer',10),('ePchPort9100',11),('ePchDLCLLCPort',15),('ePchUSB',34),('ePchIrDA',35),('ePchBidirPortTCP',38)))
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
class _Prtinterpreterdefaultcharsetin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,12,13,20,21,22,23,24,25,26,1004,2000,2001,2002,2003,2004,2005,2009,2010,2011,2012,2014,2017,2021,2027)));namedValues=NamedValues(*((_G,1),(_A2,3),('ePcsISOLatin1',4),('ePcsISOLatin2',5),('ePcsISOLatin5',12),('ePcsISOLatin6',13),('ePcsISO4UnitedKingdom',20),('ePcsISO11SwedishforNames',21),('ePcsISO15Italian',22),('ePcsISO17Spanish',23),('ePcsISO21German',24),('ePcsISO60DanishNorwegian',25),('ePcsISO69French',26),('ePcsUnicodeIBM2039',1004),('ePcsWindows30Latin1',2000),('ePcsWindows31Latin1',2001),('ePcsWindows31Latin2',2002),('ePcsWindows31Latin5',2003),(_Z,2004),(_A3,2005),('ePcsPC850Multilingual',2009),('ePcsPCp852',2010),('ePcsPC8CodePage437',2011),('ePcsPC8DNDanishNorwegian',2012),('ePcsHPPC8Turkish',2014),('ePcsHPLegal',2017),('ePcsHPDeskTop',2021),('ePcsMacintosh',2027)))
_Prtinterpreterdefaultcharsetin_Type.__name__=_C
_Prtinterpreterdefaultcharsetin_Object=MibScalar
prtinterpreterdefaultcharsetin=_Prtinterpreterdefaultcharsetin_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,10),_Prtinterpreterdefaultcharsetin_Type())
prtinterpreterdefaultcharsetin.setMaxAccess(_D)
if mibBuilder.loadTexts:prtinterpreterdefaultcharsetin.setStatus(_A)
class _Prtinterpreterdefaultcharsetout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,2004,2005)));namedValues=NamedValues(*(('ePcsNoDefault',2),(_A2,3),(_Z,2004),(_A3,2005)))
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
class _Prtconsolecolor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),(_b,2),('ePwhite',3),('ePred',4),('ePgreen',5),('ePblue',6),('ePcyan',7),('ePmagenta',8),('ePyellow',9)))
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
class _Prtalerttraininglevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_b,2),('ePuntrained',3),('ePtrained',4),('ePfieldService',5),('ePmanagement',6),('ePnoInterventionRequired',7)))
_Prtalerttraininglevel_Type.__name__=_C
_Prtalerttraininglevel_Object=MibScalar
prtalerttraininglevel=_Prtalerttraininglevel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,3),_Prtalerttraininglevel_Type())
prtalerttraininglevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalerttraininglevel.setStatus(_A)
class _Prtalertgroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,8,9,10,14)));namedValues=NamedValues(*(('ePgeneralPrinter',5),('ePcover',6),('ePinput',8),('ePoutput',9),('ePmarker',10),('ePchannel',14)))
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
class _Prtalertcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,8,801,808)));namedValues=NamedValues(*((_G,1),('ePcoverOpened',3),('ePjam',8),('ePinputMediaTrayMissing',801),('ePinputMediaSupplyEmpty',808)))
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
class _Hrdevicestatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,5)));namedValues=NamedValues(*(('eHrunning',2),('eHwarning',3),('eHdown',5)))
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
mibBuilder.exportSymbols('LJ3200-MIB',**{_M:DisplayString,'hp':hp,'dm':dm,'device':device,'system':system,'settings-system':settings_system,'energy-star':energy_star,'sleep-mode':sleep_mode,'service-password':service_password,'device-cfg-download':device_cfg_download,'device-cfg-download-data-type':device_cfg_download_data_type,'device-cfg-upload':device_cfg_upload,'device-cfg-upload-data-type':device_cfg_upload_data_type,'download-timeout':download_timeout,'upload-timeout':upload_timeout,'date-display':date_display,'device-cfg-param-command':device_cfg_param_command,'copier-token':copier_token,'scan-token':scan_token,'fax-upload-token':fax_upload_token,'fax-download-token':fax_download_token,'device-config-token':device_config_token,'status-system':status_system,'on-off-line':on_off_line,'continue':_pysmi_continue,'auto-continue':auto_continue,'install-date':install_date,'date-and-time':date_and_time,'time-display':time_display,'error-log-clear':error_log_clear,'collated-originals-support':collated_originals_support,'device-cfg-download-error':device_cfg_download_error,'device-cfg-upload-error':device_cfg_upload_error,'id':id,'model-name':model_name,'serial-number':serial_number,'fw-rom-datecode':fw_rom_datecode,'fax-local-phone-num':fax_local_phone_num,'fax-station-name':fax_station_name,'device-name':device_name,'device-location':device_location,'asset-number':asset_number,'fax-line-interface-unit-id':fax_line_interface_unit_id,'interface':interface,'simm':simm,'simm1':simm1,'simm1-type':simm1_type,'simm1-capacity':simm1_capacity,'simm2':simm2,'simm2-type':simm2_type,'simm2-capacity':simm2_capacity,'simm3':simm3,'simm3-type':simm3_type,'simm3-capacity':simm3_capacity,'test':test,'self-test':self_test,'print-internal-page':print_internal_page,'job':job,'settings-job':settings_job,'cancel-job':cancel_job,'job-info-change-id':job_info_change_id,'active-print-jobs':active_print_jobs,'job-being-parsed':job_being_parsed,'current-job-parsing-id':current_job_parsing_id,'fax-job-control':fax_job_control,'settings-fax-job':settings_fax_job,'faxjob-action':faxjob_action,'faxjob-action-id':faxjob_action_id,'faxjob-tx-type':faxjob_tx_type,'status-fax-job':status_fax_job,'faxjob-download-id':faxjob_download_id,'faxjob-rx-id':faxjob_rx_id,'faxjob-tx-id':faxjob_tx_id,'faxjob-upload-id':faxjob_upload_id,'faxjob':faxjob,'faxjob-rx-status':faxjob_rx_status,'faxjob-rx-status-1':faxjob_rx_status_1,'faxjob-tx-status':faxjob_tx_status,'faxjob-tx-status-1':faxjob_tx_status_1,'faxjob-tx-error':faxjob_tx_error,'faxjob-tx-error-1':faxjob_tx_error_1,'faxjob-tx-current-page':faxjob_tx_current_page,'faxjob-tx-current-page-1':faxjob_tx_current_page_1,'faxjob-rx-current-page':faxjob_rx_current_page,'faxjob-rx-current-page-1':faxjob_rx_current_page_1,'faxjob-rx-duration':faxjob_rx_duration,'faxjob-rx-duration-1':faxjob_rx_duration_1,'faxjob-tx-duration':faxjob_tx_duration,'faxjob-tx-duration-1':faxjob_tx_duration_1,'fax-activity-log':fax_activity_log,'settings-faxlog':settings_faxlog,'fax-log-action':fax_log_action,'fax-log-reporting':fax_log_reporting,'job-info':job_info,'job-info-name1':job_info_name1,'job-info-name2':job_info_name2,'job-info-stage':job_info_stage,'job-info-io-source':job_info_io_source,'job-info-pages-processed':job_info_pages_processed,'job-info-pages-printed':job_info_pages_printed,'job-info-size':job_info_size,'job-info-state':job_info_state,'job-info-outcome':job_info_outcome,'job-info-outbins-used':job_info_outbins_used,'job-info-physical-outbins-used':job_info_physical_outbins_used,'job-info-attribute':job_info_attribute,'job-info-attr-1':job_info_attr_1,'job-info-attr-2':job_info_attr_2,'job-info-attr-3':job_info_attr_3,'job-info-attr-4':job_info_attr_4,'job-info-attr-5':job_info_attr_5,'job-info-attr-6':job_info_attr_6,'job-info-attr-7':job_info_attr_7,'job-info-attr-8':job_info_attr_8,'job-info-attr-9':job_info_attr_9,'job-info-attr-10':job_info_attr_10,'job-info-attr-11':job_info_attr_11,'job-info-attr-12':job_info_attr_12,'job-info-attr-13':job_info_attr_13,'job-info-attr-14':job_info_attr_14,'job-info-attr-15':job_info_attr_15,'job-info-attr-16':job_info_attr_16,'phone':phone,'dial':dial,'dial-all-lines':dial_all_lines,'fax-dial-mode':fax_dial_mode,'device-redial':device_redial,'answer':answer,'answer-all-lines':answer_all_lines,'fax-answer-mode':fax_answer_mode,'fax-num-rings-pickup':fax_num_rings_pickup,'device-ring-type-pickup':device_ring_type_pickup,'errorlog':errorlog,'error1':error1,'error1-time-stamp':error1_time_stamp,'error1-code':error1_code,'error2':error2,'error2-time-stamp':error2_time_stamp,'error2-code':error2_code,'error3':error3,'error3-time-stamp':error3_time_stamp,'error3-code':error3_code,'error4':error4,'error4-time-stamp':error4_time_stamp,'error4-code':error4_code,'error5':error5,'error5-time-stamp':error5_time_stamp,'error5-code':error5_code,'error6':error6,'error6-time-stamp':error6_time_stamp,'error6-code':error6_code,'error7':error7,'error7-time-stamp':error7_time_stamp,'error7-code':error7_code,'error8':error8,'error8-time-stamp':error8_time_stamp,'error8-code':error8_code,'error9':error9,'error9-time-stamp':error9_time_stamp,'error9-code':error9_code,'error10':error10,'error10-time-stamp':error10_time_stamp,'error10-code':error10_code,'source-subsystem':source_subsystem,'io':io,'settings-io':settings_io,'io-timeout':io_timeout,'io-switch':io_switch,'scanner':scanner,'settings-scanner':settings_scanner,'scan-contrast':scan_contrast,'scan-resolution':scan_resolution,'scan-pixel-data-type':scan_pixel_data_type,'scan-compression':scan_compression,'scan-compression-factor':scan_compression_factor,'scan-upload-error':scan_upload_error,'scan-upload':scan_upload,'default-scanner-margin-left':default_scanner_margin_left,'default-scanner-margin-right':default_scanner_margin_right,'scan-calibration':scan_calibration,'scan-calibration-target':scan_calibration_target,'ui-add-option':ui_add_option,'ui-select-option':ui_select_option,'ui-delete-option':ui_delete_option,'scanner-jam-page-count':scanner_jam_page_count,'scanner-adf-page-count':scanner_adf_page_count,'scan-adf-page-count':scan_adf_page_count,'scan-image-type':scan_image_type,'scan-subsample':scan_subsample,'scanner-retrieve-scanline':scanner_retrieve_scanline,'scanner-motor-control':scanner_motor_control,'scan-height':scan_height,'scanner-scanline-statistics':scanner_scanline_statistics,'scan-control-descriptor':scan_control_descriptor,'scan-gamma-correction':scan_gamma_correction,'scan-pad-image':scan_pad_image,'status-scanner':status_scanner,'not-ready-source-scanner':not_ready_source_scanner,'scan-resolution-range':scan_resolution_range,'scan-calibration-download':scan_calibration_download,'scan-calibration-error':scan_calibration_error,'scanner-button-status':scanner_button_status,'fax-receive':fax_receive,'settings-fax-receive':settings_fax_receive,'fax-receive-stamping-enable':fax_receive_stamping_enable,'status-fax-receive':status_fax_receive,'not-ready-fax-receive':not_ready_fax_receive,'processing-subsystem':processing_subsystem,'pdl':pdl,'settings-pdl':settings_pdl,'default-copies':default_copies,'form-feed':form_feed,'maximum-resource-saving-memory':maximum_resource_saving_memory,'default-vertical-black-resolution':default_vertical_black_resolution,'default-horizontal-black-resolution':default_horizontal_black_resolution,'default-page-protect':default_page_protect,'default-lines-per-page':default_lines_per_page,'default-vmi':default_vmi,'default-media-size':default_media_size,'cold-reset-media-size':cold_reset_media_size,'reprint':reprint,'wide-a4':wide_a4,'dark-courier':dark_courier,'default-bits-per-pixel':default_bits_per_pixel,'status-pdl':status_pdl,'form-feed-needed':form_feed_needed,'pdl-pcl':pdl_pcl,'pcl-resource-saving-memory-size':pcl_resource_saving_memory_size,'pcl-default-font-height':pcl_default_font_height,'pcl-default-font-source':pcl_default_font_source,'pcl-default-font-number':pcl_default_font_number,'pcl-default-font-width':pcl_default_font_width,'pjl':pjl,'pjl-password':pjl_password,'fax-proc-sub':fax_proc_sub,'settings-fax-proc-sub':settings_fax_proc_sub,'fax-rxscale':fax_rxscale,'fax-noise-volume':fax_noise_volume,'fax-download':fax_download,'fax-silent-detection':fax_silent_detection,'fax-ring-enable':fax_ring_enable,'fax-country':fax_country,'fax-tx-phone-number':fax_tx_phone_number,'fax-redial-time':fax_redial_time,'fax-pstn-access-code':fax_pstn_access_code,'fax-rx-disposition':fax_rx_disposition,'fax-error-correction-mode':fax_error_correction_mode,'fax-report-transmission':fax_report_transmission,'fax-report-activity-log':fax_report_activity_log,'fax-dial-tone-detection':fax_dial_tone_detection,'fax-alarm-volume':fax_alarm_volume,'fax-beep-volume':fax_beep_volume,'fax-ring-volume':fax_ring_volume,'fax-master-host':fax_master_host,'fax-thumbnail-enable':fax_thumbnail_enable,'fax-phone-pickup-enable':fax_phone_pickup_enable,'status-fax-proc-sub':status_fax_proc_sub,'fax-upload':fax_upload,'fax-min-rings-pickup':fax_min_rings_pickup,'fax-max-rings-pickup':fax_max_rings_pickup,'fax-max-redials':fax_max_redials,'fax-additional-wait':fax_additional_wait,'fax-download-error':fax_download_error,'fax-upload-error':fax_upload_error,'fax-firmware-revision':fax_firmware_revision,'fax-forwarding':fax_forwarding,'fax-forwarding-phone-num':fax_forwarding_phone_num,'destination-subsystem':destination_subsystem,'print-engine':print_engine,'settings-prt-eng':settings_prt_eng,'override-media-size':override_media_size,'print-density':print_density,'status-prt-eng':status_prt_eng,'total-engine-page-count':total_engine_page_count,'print-engine-jam-count':print_engine_jam_count,'print-engine-mispick-count':print_engine_mispick_count,'intray':intray,'settings-intray':settings_intray,'custom-paper-dim-unit':custom_paper_dim_unit,'custom-paper-feed-dim':custom_paper_feed_dim,'custom-paper-xfeed-dim':custom_paper_xfeed_dim,'intrays':intrays,'intray1':intray1,'tray1-fuser-temperature':tray1_fuser_temperature,'imaging':imaging,'default-ret':default_ret,'default-print-quality':default_print_quality,'fax-send':fax_send,'settings-fax-send':settings_fax_send,'fax-resolution':fax_resolution,'fax-contrast':fax_contrast,'fax-pixel-data-type':fax_pixel_data_type,'status-fax-send':status_fax_send,'not-ready-fax-send':not_ready_fax_send,'transmit-fax':transmit_fax,'fax-allow-redials':fax_allow_redials,'copier':copier,'settings-copier':settings_copier,'copier-contrast':copier_contrast,'copier-reduction':copier_reduction,'copier-num-copies':copier_num_copies,'copier-collation':copier_collation,'copier-quality':copier_quality,'copier-adf-page-count':copier_adf_page_count,'copier-print-page-count':copier_print_page_count,'copier-job-media-size':copier_job_media_size,'copier-job-quality':copier_job_quality,'copier-job-collation':copier_job_collation,'copier-job-num-copies':copier_job_num_copies,'copier-job-reduction':copier_job_reduction,'copier-job-contrast':copier_job_contrast,'copier-job':copier_job,'tables':tables,'channel-table':channel_table,'channel-entry':channel_entry,'channel-bytes-sent':channel_bytes_sent,'channel-bytes-received':channel_bytes_received,'channel-io-errors':channel_io_errors,'channel-jobs-received':channel_jobs_received,'printmib':printmib,'prtGeneral':prtGeneral,'prtGeneralTable':prtGeneralTable,'prtGeneralEntry':prtGeneralEntry,'prtgeneralconfigchanges':prtgeneralconfigchanges,'prtgeneralcurrentlocalization':prtgeneralcurrentlocalization,'prtgeneralreset':prtgeneralreset,'prtgeneralcurrentoperator':prtgeneralcurrentoperator,'prtgeneralserviceperson':prtgeneralserviceperson,'prtinputdefaultindex':prtinputdefaultindex,'prtoutputdefaultindex':prtoutputdefaultindex,'prtmarkerdefaultindex':prtmarkerdefaultindex,'prtmediapathdefaultindex':prtmediapathdefaultindex,'prtconsolelocalization':prtconsolelocalization,'prtconsolenumberofdisplaylines':prtconsolenumberofdisplaylines,'prtconsolenumberofdisplaychars':prtconsolenumberofdisplaychars,'prtconsoledisable':prtconsoledisable,'prtgeneralprintername':prtgeneralprintername,'prtgeneralserialnumber':prtgeneralserialnumber,'prtalertcriticalevents':prtalertcriticalevents,'prtalertallevents':prtalertallevents,'prtStorageRefTable':prtStorageRefTable,'prtStorageRefEntry':prtStorageRefEntry,'prtstoragerefindex':prtstoragerefindex,'prtDeviceRefTable':prtDeviceRefTable,'prtDeviceRefEntry':prtDeviceRefEntry,'prtdevicerefindex':prtdevicerefindex,'prtCover':prtCover,'prtCoverTable':prtCoverTable,'prtCoverEntry':prtCoverEntry,'prtcoverdescription':prtcoverdescription,'prtcoverstatus':prtcoverstatus,'prtLocalization':prtLocalization,'prtLocalizationTable':prtLocalizationTable,'prtLocalizationEntry':prtLocalizationEntry,'prtlocalizationlanguage':prtlocalizationlanguage,'prtlocalizationcountry':prtlocalizationcountry,'prtlocalizationcharacterset':prtlocalizationcharacterset,'prtInput':prtInput,'prtInputTable':prtInputTable,'prtInputEntry':prtInputEntry,'prtinputtype':prtinputtype,'prtinputdimunit':prtinputdimunit,'prtinputmediadimfeeddirdeclared':prtinputmediadimfeeddirdeclared,'prtinputmediadimxfeeddirdeclared':prtinputmediadimxfeeddirdeclared,'prtinputmediadimfeeddirchosen':prtinputmediadimfeeddirchosen,'prtinputmediadimxfeeddirchosen':prtinputmediadimxfeeddirchosen,'prtinputcapacityunit':prtinputcapacityunit,'prtinputmaxcapacity':prtinputmaxcapacity,'prtinputcurrentlevel':prtinputcurrentlevel,'prtinputstatus':prtinputstatus,'prtinputmedianame':prtinputmedianame,'prtinputname':prtinputname,'prtinputvendorname':prtinputvendorname,'prtinputmodel':prtinputmodel,'prtinputversion':prtinputversion,'prtinputserialnumber':prtinputserialnumber,'prtinputdescription':prtinputdescription,'prtinputsecurity':prtinputsecurity,'prtOutput':prtOutput,'prtOutputTable':prtOutputTable,'prtOutputEntry':prtOutputEntry,'prtoutputtype':prtoutputtype,'prtoutputcapacityunit':prtoutputcapacityunit,'prtoutputmaxcapacity':prtoutputmaxcapacity,'prtoutputremainingcapacity':prtoutputremainingcapacity,'prtoutputstatus':prtoutputstatus,'prtMarker':prtMarker,'prtMarkerTable':prtMarkerTable,'prtMarkerEntry':prtMarkerEntry,'prtmarkermarktech':prtmarkermarktech,'prtmarkercounterunit':prtmarkercounterunit,'prtmarkerlifecount':prtmarkerlifecount,'prtmarkerpoweroncount':prtmarkerpoweroncount,'prtmarkerprocesscolorants':prtmarkerprocesscolorants,'prtmarkerspotcolorants':prtmarkerspotcolorants,'prtmarkeraddressabilityunit':prtmarkeraddressabilityunit,'prtmarkeraddressabilityfeeddir':prtmarkeraddressabilityfeeddir,'prtmarkeraddressabilityxfeeddir':prtmarkeraddressabilityxfeeddir,'prtmarkernorthmargin':prtmarkernorthmargin,'prtmarkersouthmargin':prtmarkersouthmargin,'prtmarkerwestmargin':prtmarkerwestmargin,'prtmarkereastmargin':prtmarkereastmargin,'prtmarkerstatus':prtmarkerstatus,'prtMarkerSupplies':prtMarkerSupplies,'prtMarkerSuppliesTable':prtMarkerSuppliesTable,'prtMarkerSuppliesEntry':prtMarkerSuppliesEntry,'prtmarkersuppliesmarkerindex':prtmarkersuppliesmarkerindex,'prtmarkersuppliescolorantindex':prtmarkersuppliescolorantindex,'prtmarkersuppliesclass':prtmarkersuppliesclass,'prtmarkersuppliestype':prtmarkersuppliestype,'prtmarkersuppliesdescription':prtmarkersuppliesdescription,'prtmarkersuppliessupplyunit':prtmarkersuppliessupplyunit,'prtmarkersuppliesmaxcapacity':prtmarkersuppliesmaxcapacity,'prtmarkersupplieslevel':prtmarkersupplieslevel,'prtMediaPath':prtMediaPath,'prtMediaPathTable':prtMediaPathTable,'prtMediaPathEntry':prtMediaPathEntry,'prtmediapathmaxspeedprintunit':prtmediapathmaxspeedprintunit,'prtmediapathmediasizeunit':prtmediapathmediasizeunit,'prtmediapathmaxspeed':prtmediapathmaxspeed,'prtmediapathmaxmediafeeddir':prtmediapathmaxmediafeeddir,'prtmediapathmaxmediaxfeeddir':prtmediapathmaxmediaxfeeddir,'prtmediapathminmediafeeddir':prtmediapathminmediafeeddir,'prtmediapathminmediaxfeeddir':prtmediapathminmediaxfeeddir,'prtmediapathtype':prtmediapathtype,'prtmediapathdescription':prtmediapathdescription,'prtmediapathstatus':prtmediapathstatus,'prtChannel':prtChannel,'prtChannelTable':prtChannelTable,'prtChannelEntry':prtChannelEntry,'prtchanneltype':prtchanneltype,'prtchannelprotocolversion':prtchannelprotocolversion,'prtchannelcurrentjobcntllangindex':prtchannelcurrentjobcntllangindex,'prtchanneldefaultpagedesclangindex':prtchanneldefaultpagedesclangindex,'prtchannelstate':prtchannelstate,'prtchannelifindex':prtchannelifindex,'prtchannelstatus':prtchannelstatus,'prtchannelinformation':prtchannelinformation,'prtInterpreter':prtInterpreter,'prtInterpreterTable':prtInterpreterTable,'prtInterpreterEntry':prtInterpreterEntry,'prtinterpreterlangfamily':prtinterpreterlangfamily,'prtinterpreterlanglevel':prtinterpreterlanglevel,'prtinterpreterlangversion':prtinterpreterlangversion,'prtinterpreterdescription':prtinterpreterdescription,'prtinterpreterversion':prtinterpreterversion,'prtinterpreterdefaultorientation':prtinterpreterdefaultorientation,'prtinterpreterfeedaddressability':prtinterpreterfeedaddressability,'prtinterpreterxfeedaddressability':prtinterpreterxfeedaddressability,'prtinterpreterdefaultcharsetin':prtinterpreterdefaultcharsetin,'prtinterpreterdefaultcharsetout':prtinterpreterdefaultcharsetout,'prtinterpretertwoway':prtinterpretertwoway,'prtConsoleDisplayBuffer':prtConsoleDisplayBuffer,'prtConsoleDisplayBufferTable':prtConsoleDisplayBufferTable,'prtConsoleDisplayBufferEntry':prtConsoleDisplayBufferEntry,'prtconsoledisplaybuffertext':prtconsoledisplaybuffertext,'prtConsoleLights':prtConsoleLights,'prtConsoleLightTable':prtConsoleLightTable,'prtConsoleLightEntry':prtConsoleLightEntry,'prtconsoleontime':prtconsoleontime,'prtconsoleofftime':prtconsoleofftime,'prtconsolecolor':prtconsolecolor,'prtconsoledescription':prtconsoledescription,'prtAlert':prtAlert,'prtAlertTable':prtAlertTable,'prtAlertEntry':prtAlertEntry,'prtalertseveritylevel':prtalertseveritylevel,'prtalerttraininglevel':prtalerttraininglevel,'prtalertgroup':prtalertgroup,'prtalertgroupindex':prtalertgroupindex,'prtalertlocation':prtalertlocation,'prtalertcode':prtalertcode,'prtalertdescription':prtalertdescription,'prtalerttime':prtalerttime,'hrm':hrm,'hrStorage':hrStorage,'hrmemorysize':hrmemorysize,'hrStorageTable':hrStorageTable,'hrStorageEntry':hrStorageEntry,'hrstorageindex':hrstorageindex,'hrstoragetype':hrstoragetype,'hrstoragedescr':hrstoragedescr,'hrstorageallocationunits':hrstorageallocationunits,'hrstoragesize':hrstoragesize,'hrstorageused':hrstorageused,'hrstorageallocationfailures':hrstorageallocationfailures,'hrDevice':hrDevice,'hrDeviceTable':hrDeviceTable,'hrDeviceEntry':hrDeviceEntry,'hrdeviceindex':hrdeviceindex,'hrdevicetype':hrdevicetype,'hrdevicedescr':hrdevicedescr,'hrdeviceid':hrdeviceid,'hrdevicestatus':hrdevicestatus,'hrdeviceerrors':hrdeviceerrors,'hrPrinterTable':hrPrinterTable,'hrPrinterEntry':hrPrinterEntry,'hrprinterstatus':hrprinterstatus,'hrprinterdetectederrorstate':hrprinterdetectederrorstate})