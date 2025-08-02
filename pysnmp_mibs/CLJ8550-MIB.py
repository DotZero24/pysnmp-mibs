_z='eHreadOnly'
_y='eHreadWrite'
_x='eHother'
_w='ePhours'
_v='ePimpressions'
_u='eChOther'
_t='eInternationalB5'
_s='eInternationalC5'
_r='eInternationalDL'
_q='eCommercial10'
_p='eMonarch'
_o='eJISB5'
_n='eISOandJISA5'
_m='eUSExecutive'
_l='eOutputPHD'
_k='eInputPHD'
_j='eIOCard'
_i='eDiskDrive'
_h='eFalse'
_g='ePcsHPRoman8'
_f='eOff'
_e='eAuto'
_d='ePmeters'
_c='ePfeet'
_b='ePsheets'
_a='eISOandJISA3'
_Z='eLedger'
_Y='eOn'
_X='eJISB4'
_W='eUSLegal'
_V='ePoff'
_U='ePon'
_T='eISOandJISA4'
_S='eUSLetter'
_R='DisplayString'
_Q='ePmicrometers'
_P='ePtenThousandthsOfInches'
_O='ePunknown'
_N='ePnotPresent'
_M='eVolatileRandomAccessMemory'
_L='eReadOnlyMemory'
_K='eUnSupported'
_J='eUnknown'
_I='eEmpty'
_H='ePother'
_G='write-only'
_F='mandatory'
_E='read-write'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='optional'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_R,'PhysAddress','TextualConvention')
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
energy_star.setMaxAccess(_E)
if mibBuilder.loadTexts:energy_star.setStatus(_A)
class _Sleep_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),('eTrue',2)))
_Sleep_mode_Type.__name__=_C
_Sleep_mode_Object=MibScalar
sleep_mode=_Sleep_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,2),_Sleep_mode_Type())
sleep_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:sleep_mode.setStatus(_A)
_Status_system_ObjectIdentity=ObjectIdentity
status_system=_Status_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2))
class _On_off_line_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eOnline',1),('eOffline',2),('eOfflineAtEndOfJob',3)))
_On_off_line_Type.__name__=_C
_On_off_line_Object=MibScalar
on_off_line=_On_off_line_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,5),_On_off_line_Type())
on_off_line.setMaxAccess(_E)
if mibBuilder.loadTexts:on_off_line.setStatus(_A)
class __pysmi_continue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eInitiateAction',1))
__pysmi_continue_Type.__name__=_C
__pysmi_continue_Object=MibScalar
_pysmi_continue=__pysmi_continue_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,6),__pysmi_continue_Type())
_pysmi_continue.setMaxAccess(_G)
if mibBuilder.loadTexts:_pysmi_continue.setStatus(_A)
class _Auto_continue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_Y,2))
_Auto_continue_Type.__name__=_C
_Auto_continue_Object=MibScalar
auto_continue=_Auto_continue_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,7),_Auto_continue_Type())
auto_continue.setMaxAccess(_B)
if mibBuilder.loadTexts:auto_continue.setStatus(_A)
class _Job_input_auto_continue_timeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,3600))
_Job_input_auto_continue_timeout_Type.__name__=_C
_Job_input_auto_continue_timeout_Object=MibScalar
job_input_auto_continue_timeout=_Job_input_auto_continue_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,35),_Job_input_auto_continue_timeout_Type())
job_input_auto_continue_timeout.setMaxAccess(_E)
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
_Background_status_msg_line1_part1_Type.__name__=_R
_Background_status_msg_line1_part1_Object=MibScalar
background_status_msg_line1_part1=_Background_status_msg_line1_part1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,1,1),_Background_status_msg_line1_part1_Type())
background_status_msg_line1_part1.setMaxAccess(_E)
if mibBuilder.loadTexts:background_status_msg_line1_part1.setStatus(_A)
_Background_message2_ObjectIdentity=ObjectIdentity
background_message2=_Background_message2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,2))
_Background_status_msg_line2_part1_Type=DisplayString
_Background_status_msg_line2_part1_Object=MibScalar
background_status_msg_line2_part1=_Background_status_msg_line2_part1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,37,2,1),_Background_status_msg_line2_part1_Type())
background_status_msg_line2_part1.setMaxAccess(_E)
if mibBuilder.loadTexts:background_status_msg_line2_part1.setStatus(_A)
class _Error_log_clear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eClearErrorLog',1))
_Error_log_clear_Type.__name__=_C
_Error_log_clear_Object=MibScalar
error_log_clear=_Error_log_clear_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,38),_Error_log_clear_Type())
error_log_clear.setMaxAccess(_G)
if mibBuilder.loadTexts:error_log_clear.setStatus(_A)
class _Job_output_auto_continue_timeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,3600))
_Job_output_auto_continue_timeout_Type.__name__=_C
_Job_output_auto_continue_timeout_Object=MibScalar
job_output_auto_continue_timeout=_Job_output_auto_continue_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,40),_Job_output_auto_continue_timeout_Type())
job_output_auto_continue_timeout.setMaxAccess(_B)
if mibBuilder.loadTexts:job_output_auto_continue_timeout.setStatus(_A)
_Collated_originals_support_Type=OctetString
_Collated_originals_support_Object=MibScalar
collated_originals_support=_Collated_originals_support_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,42),_Collated_originals_support_Type())
collated_originals_support.setMaxAccess(_B)
if mibBuilder.loadTexts:collated_originals_support.setStatus(_A)
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
_Serial_number_Type=DisplayString
_Serial_number_Object=MibScalar
serial_number=_Serial_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,3),_Serial_number_Type())
serial_number.setMaxAccess(_B)
if mibBuilder.loadTexts:serial_number.setStatus(_A)
_Device_name_Type=DisplayString
_Device_name_Object=MibScalar
device_name=_Device_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,10),_Device_name_Type())
device_name.setMaxAccess(_E)
if mibBuilder.loadTexts:device_name.setStatus(_A)
_Device_location_Type=DisplayString
_Device_location_Object=MibScalar
device_location=_Device_location_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,11),_Device_location_Type())
device_location.setMaxAccess(_E)
if mibBuilder.loadTexts:device_location.setStatus(_A)
_Asset_number_Type=DisplayString
_Asset_number_Object=MibScalar
asset_number=_Asset_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,12),_Asset_number_Type())
asset_number.setMaxAccess(_E)
if mibBuilder.loadTexts:asset_number.setStatus(_A)
_Interface_ObjectIdentity=ObjectIdentity
interface=_Interface_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4))
_Simm_ObjectIdentity=ObjectIdentity
simm=_Simm_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1))
_Simm1_ObjectIdentity=ObjectIdentity
simm1=_Simm1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,1))
class _Simm1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5)))
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
class _Simm2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5)))
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
class _Simm3_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5)))
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
_Simm4_ObjectIdentity=ObjectIdentity
simm4=_Simm4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4))
class _Simm4_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5)))
_Simm4_type_Type.__name__=_C
_Simm4_type_Object=MibScalar
simm4_type=_Simm4_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,4),_Simm4_type_Type())
simm4_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm4_type.setStatus(_A)
_Simm4_capacity_Type=Integer32
_Simm4_capacity_Object=MibScalar
simm4_capacity=_Simm4_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,4,5),_Simm4_capacity_Type())
simm4_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm4_capacity.setStatus(_A)
_Simm5_ObjectIdentity=ObjectIdentity
simm5=_Simm5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5))
class _Simm5_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5)))
_Simm5_type_Type.__name__=_C
_Simm5_type_Object=MibScalar
simm5_type=_Simm5_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,4),_Simm5_type_Type())
simm5_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm5_type.setStatus(_A)
_Simm5_capacity_Type=Integer32
_Simm5_capacity_Object=MibScalar
simm5_capacity=_Simm5_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,5,5),_Simm5_capacity_Type())
simm5_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm5_capacity.setStatus(_A)
_Simm6_ObjectIdentity=ObjectIdentity
simm6=_Simm6_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,6))
class _Simm6_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5)))
_Simm6_type_Type.__name__=_C
_Simm6_type_Object=MibScalar
simm6_type=_Simm6_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,6,4),_Simm6_type_Type())
simm6_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm6_type.setStatus(_A)
_Simm6_capacity_Type=Integer32
_Simm6_capacity_Object=MibScalar
simm6_capacity=_Simm6_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,6,5),_Simm6_capacity_Type())
simm6_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm6_capacity.setStatus(_A)
_Simm7_ObjectIdentity=ObjectIdentity
simm7=_Simm7_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,7))
class _Simm7_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5)))
_Simm7_type_Type.__name__=_C
_Simm7_type_Object=MibScalar
simm7_type=_Simm7_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,7,4),_Simm7_type_Type())
simm7_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm7_type.setStatus(_A)
_Simm7_capacity_Type=Integer32
_Simm7_capacity_Object=MibScalar
simm7_capacity=_Simm7_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,7,5),_Simm7_capacity_Type())
simm7_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm7_capacity.setStatus(_A)
_Simm8_ObjectIdentity=ObjectIdentity
simm8=_Simm8_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,8))
class _Simm8_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5)))
_Simm8_type_Type.__name__=_C
_Simm8_type_Object=MibScalar
simm8_type=_Simm8_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,8,4),_Simm8_type_Type())
simm8_type.setMaxAccess(_B)
if mibBuilder.loadTexts:simm8_type.setStatus(_A)
_Simm8_capacity_Type=Integer32
_Simm8_capacity_Object=MibScalar
simm8_capacity=_Simm8_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,1,8,5),_Simm8_capacity_Type())
simm8_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:simm8_capacity.setStatus(_A)
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
class _Mio1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,8,12)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_i,8),(_j,12)))
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
class _Mio2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,8,12)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_i,8),(_j,12)))
_Mio2_type_Type.__name__=_C
_Mio2_type_Object=MibScalar
mio2_type=_Mio2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,3,2,4),_Mio2_type_Type())
mio2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:mio2_type.setStatus(_A)
_Phd_ObjectIdentity=ObjectIdentity
phd=_Phd_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5))
_Phd1_ObjectIdentity=ObjectIdentity
phd1=_Phd1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,1))
class _Phd1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_Phd1_type_Type.__name__=_C
_Phd1_type_Object=MibScalar
phd1_type=_Phd1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,1,3),_Phd1_type_Type())
phd1_type.setMaxAccess(_B)
if mibBuilder.loadTexts:phd1_type.setStatus(_A)
_Phd2_ObjectIdentity=ObjectIdentity
phd2=_Phd2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,2))
_Phd2_model_Type=DisplayString
_Phd2_model_Object=MibScalar
phd2_model=_Phd2_model_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,2,1),_Phd2_model_Type())
phd2_model.setMaxAccess(_B)
if mibBuilder.loadTexts:phd2_model.setStatus(_A)
_Phd2_manufacturing_info_Type=DisplayString
_Phd2_manufacturing_info_Object=MibScalar
phd2_manufacturing_info=_Phd2_manufacturing_info_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,2,2),_Phd2_manufacturing_info_Type())
phd2_manufacturing_info.setMaxAccess(_B)
if mibBuilder.loadTexts:phd2_manufacturing_info.setStatus(_A)
class _Phd2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,11)));namedValues=NamedValues(*((_I,1),(_k,10),(_l,11)))
_Phd2_type_Type.__name__=_C
_Phd2_type_Object=MibScalar
phd2_type=_Phd2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,2,3),_Phd2_type_Type())
phd2_type.setMaxAccess(_B)
if mibBuilder.loadTexts:phd2_type.setStatus(_A)
_Phd2_capacity_Type=Integer32
_Phd2_capacity_Object=MibScalar
phd2_capacity=_Phd2_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,2,4),_Phd2_capacity_Type())
phd2_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:phd2_capacity.setStatus(_A)
_Phd3_ObjectIdentity=ObjectIdentity
phd3=_Phd3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,3))
_Phd3_model_Type=DisplayString
_Phd3_model_Object=MibScalar
phd3_model=_Phd3_model_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,3,1),_Phd3_model_Type())
phd3_model.setMaxAccess(_B)
if mibBuilder.loadTexts:phd3_model.setStatus(_A)
_Phd3_manufacturing_info_Type=DisplayString
_Phd3_manufacturing_info_Object=MibScalar
phd3_manufacturing_info=_Phd3_manufacturing_info_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,3,2),_Phd3_manufacturing_info_Type())
phd3_manufacturing_info.setMaxAccess(_B)
if mibBuilder.loadTexts:phd3_manufacturing_info.setStatus(_A)
class _Phd3_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,11)));namedValues=NamedValues(*((_I,1),(_k,10),(_l,11)))
_Phd3_type_Type.__name__=_C
_Phd3_type_Object=MibScalar
phd3_type=_Phd3_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,3,3),_Phd3_type_Type())
phd3_type.setMaxAccess(_B)
if mibBuilder.loadTexts:phd3_type.setStatus(_A)
_Phd3_capacity_Type=Integer32
_Phd3_capacity_Object=MibScalar
phd3_capacity=_Phd3_capacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,3,4),_Phd3_capacity_Type())
phd3_capacity.setMaxAccess(_B)
if mibBuilder.loadTexts:phd3_capacity.setStatus(_A)
_Phd4_ObjectIdentity=ObjectIdentity
phd4=_Phd4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,4))
class _Phd4_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_Phd4_type_Type.__name__=_C
_Phd4_type_Object=MibScalar
phd4_type=_Phd4_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,4,3),_Phd4_type_Type())
phd4_type.setMaxAccess(_B)
if mibBuilder.loadTexts:phd4_type.setStatus(_A)
_Phd5_ObjectIdentity=ObjectIdentity
phd5=_Phd5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,5))
class _Phd5_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_Phd5_type_Type.__name__=_C
_Phd5_type_Object=MibScalar
phd5_type=_Phd5_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,5,3),_Phd5_type_Type())
phd5_type.setMaxAccess(_B)
if mibBuilder.loadTexts:phd5_type.setStatus(_A)
_Phd6_ObjectIdentity=ObjectIdentity
phd6=_Phd6_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,6))
class _Phd6_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_Phd6_type_Type.__name__=_C
_Phd6_type_Object=MibScalar
phd6_type=_Phd6_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,4,5,6,3),_Phd6_type_Type())
phd6_type.setMaxAccess(_B)
if mibBuilder.loadTexts:phd6_type.setStatus(_A)
_Test_ObjectIdentity=ObjectIdentity
test=_Test_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5))
class _Self_test_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*(('eNotInASelfTest',1),('eNonDestructiveSelfTest',4)))
_Self_test_Type.__name__=_C
_Self_test_Object=MibScalar
self_test=_Self_test_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,1),_Self_test_Type())
self_test.setMaxAccess(_E)
if mibBuilder.loadTexts:self_test.setStatus(_A)
class _Print_internal_page_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,7,8,9,350,450,1000)));namedValues=NamedValues(*(('eNotPrintingAnInternalPage',1),('ePrintingAnUnknownInternalPage',2),('eDeviceDemoPage1ConfigurationPage',3),('eDeviceDemoPage2',4),('eDeviceDemoPage5ErrorLog',7),('eDeviceDemoPage6FileSystemDirectoryListing',8),('eDeviceDemoPage7MenuMap',9),('ePCLFontList1',350),('ePostScriptFontList1',450),('eMarkingAgentTestPattern',1000)))
_Print_internal_page_Type.__name__=_C
_Print_internal_page_Object=MibScalar
print_internal_page=_Print_internal_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,2),_Print_internal_page_Type())
print_internal_page.setMaxAccess(_E)
if mibBuilder.loadTexts:print_internal_page.setStatus(_A)
_Job_ObjectIdentity=ObjectIdentity
job=_Job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6))
_Settings_job_ObjectIdentity=ObjectIdentity
settings_job=_Settings_job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1))
class _Cancel_job_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_Cancel_job_Type.__name__=_C
_Cancel_job_Object=MibScalar
cancel_job=_Cancel_job_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,2),_Cancel_job_Type())
cancel_job.setMaxAccess(_G)
if mibBuilder.loadTexts:cancel_job.setStatus(_A)
class _Job_info_change_id_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Job_info_change_id_Type.__name__=_D
_Job_info_change_id_Object=MibScalar
job_info_change_id=_Job_info_change_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,3),_Job_info_change_id_Type())
job_info_change_id.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_change_id.setStatus(_A)
_Hold_job_timeout_Type=Integer32
_Hold_job_timeout_Object=MibScalar
hold_job_timeout=_Hold_job_timeout_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,10),_Hold_job_timeout_Type())
hold_job_timeout.setMaxAccess(_E)
if mibBuilder.loadTexts:hold_job_timeout.setStatus(_A)
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
class _Job_info_state_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,9,10,11)));namedValues=NamedValues(*(('eAborted',3),('eWaitingForResources',4),('ePrinted',5),('eRetained',6),('eTerminating',7),('ePaused',9),('eCancelled',10),('eProcessing',11)))
_Job_info_state_Type.__name__=_C
_Job_info_state_Object=MibScalar
job_info_state=_Job_info_state_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,15),_Job_info_state_Type())
job_info_state.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_state.setStatus(_A)
class _Job_info_outcome_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5)));namedValues=NamedValues(*(('eOk',3),('eWarningsEncountered',4),('eErrorsEncountered',5)))
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
_Job_info_attr_1_Type.__name__=_D
_Job_info_attr_1_Object=MibScalar
job_info_attr_1=_Job_info_attr_1_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,1),_Job_info_attr_1_Type())
job_info_attr_1.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_1.setStatus(_A)
class _Job_info_attr_2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_2_Type.__name__=_D
_Job_info_attr_2_Object=MibScalar
job_info_attr_2=_Job_info_attr_2_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,2),_Job_info_attr_2_Type())
job_info_attr_2.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_2.setStatus(_A)
class _Job_info_attr_3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_3_Type.__name__=_D
_Job_info_attr_3_Object=MibScalar
job_info_attr_3=_Job_info_attr_3_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,3),_Job_info_attr_3_Type())
job_info_attr_3.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_3.setStatus(_A)
class _Job_info_attr_4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_4_Type.__name__=_D
_Job_info_attr_4_Object=MibScalar
job_info_attr_4=_Job_info_attr_4_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,4),_Job_info_attr_4_Type())
job_info_attr_4.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_4.setStatus(_A)
class _Job_info_attr_5_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_5_Type.__name__=_D
_Job_info_attr_5_Object=MibScalar
job_info_attr_5=_Job_info_attr_5_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,5),_Job_info_attr_5_Type())
job_info_attr_5.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_5.setStatus(_A)
class _Job_info_attr_6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_6_Type.__name__=_D
_Job_info_attr_6_Object=MibScalar
job_info_attr_6=_Job_info_attr_6_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,6),_Job_info_attr_6_Type())
job_info_attr_6.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_6.setStatus(_A)
class _Job_info_attr_7_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_7_Type.__name__=_D
_Job_info_attr_7_Object=MibScalar
job_info_attr_7=_Job_info_attr_7_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,7),_Job_info_attr_7_Type())
job_info_attr_7.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_7.setStatus(_A)
class _Job_info_attr_8_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_8_Type.__name__=_D
_Job_info_attr_8_Object=MibScalar
job_info_attr_8=_Job_info_attr_8_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,8),_Job_info_attr_8_Type())
job_info_attr_8.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_8.setStatus(_A)
class _Job_info_attr_9_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_9_Type.__name__=_D
_Job_info_attr_9_Object=MibScalar
job_info_attr_9=_Job_info_attr_9_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,9),_Job_info_attr_9_Type())
job_info_attr_9.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_9.setStatus(_A)
class _Job_info_attr_10_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_10_Type.__name__=_D
_Job_info_attr_10_Object=MibScalar
job_info_attr_10=_Job_info_attr_10_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,10),_Job_info_attr_10_Type())
job_info_attr_10.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_10.setStatus(_A)
class _Job_info_attr_11_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_11_Type.__name__=_D
_Job_info_attr_11_Object=MibScalar
job_info_attr_11=_Job_info_attr_11_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,11),_Job_info_attr_11_Type())
job_info_attr_11.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_11.setStatus(_A)
class _Job_info_attr_12_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_12_Type.__name__=_D
_Job_info_attr_12_Object=MibScalar
job_info_attr_12=_Job_info_attr_12_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,12),_Job_info_attr_12_Type())
job_info_attr_12.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_12.setStatus(_A)
class _Job_info_attr_13_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_13_Type.__name__=_D
_Job_info_attr_13_Object=MibScalar
job_info_attr_13=_Job_info_attr_13_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,13),_Job_info_attr_13_Type())
job_info_attr_13.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_13.setStatus(_A)
class _Job_info_attr_14_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_14_Type.__name__=_D
_Job_info_attr_14_Object=MibScalar
job_info_attr_14=_Job_info_attr_14_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,14),_Job_info_attr_14_Type())
job_info_attr_14.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_14.setStatus(_A)
class _Job_info_attr_15_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_15_Type.__name__=_D
_Job_info_attr_15_Object=MibScalar
job_info_attr_15=_Job_info_attr_15_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,15),_Job_info_attr_15_Type())
job_info_attr_15.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_15.setStatus(_A)
class _Job_info_attr_16_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_16_Type.__name__=_D
_Job_info_attr_16_Object=MibScalar
job_info_attr_16=_Job_info_attr_16_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,16),_Job_info_attr_16_Type())
job_info_attr_16.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_16.setStatus(_A)
class _Job_info_attr_17_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_17_Type.__name__=_D
_Job_info_attr_17_Object=MibScalar
job_info_attr_17=_Job_info_attr_17_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,17),_Job_info_attr_17_Type())
job_info_attr_17.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_17.setStatus(_A)
class _Job_info_attr_18_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_18_Type.__name__=_D
_Job_info_attr_18_Object=MibScalar
job_info_attr_18=_Job_info_attr_18_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,18),_Job_info_attr_18_Type())
job_info_attr_18.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_18.setStatus(_A)
class _Job_info_attr_19_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_19_Type.__name__=_D
_Job_info_attr_19_Object=MibScalar
job_info_attr_19=_Job_info_attr_19_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,19),_Job_info_attr_19_Type())
job_info_attr_19.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_19.setStatus(_A)
class _Job_info_attr_20_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_20_Type.__name__=_D
_Job_info_attr_20_Object=MibScalar
job_info_attr_20=_Job_info_attr_20_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,20),_Job_info_attr_20_Type())
job_info_attr_20.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_20.setStatus(_A)
class _Job_info_attr_21_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_21_Type.__name__=_D
_Job_info_attr_21_Object=MibScalar
job_info_attr_21=_Job_info_attr_21_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,21),_Job_info_attr_21_Type())
job_info_attr_21.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_21.setStatus(_A)
class _Job_info_attr_22_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_22_Type.__name__=_D
_Job_info_attr_22_Object=MibScalar
job_info_attr_22=_Job_info_attr_22_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,22),_Job_info_attr_22_Type())
job_info_attr_22.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_22.setStatus(_A)
class _Job_info_attr_23_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_23_Type.__name__=_D
_Job_info_attr_23_Object=MibScalar
job_info_attr_23=_Job_info_attr_23_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,23),_Job_info_attr_23_Type())
job_info_attr_23.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_23.setStatus(_A)
class _Job_info_attr_24_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_24_Type.__name__=_D
_Job_info_attr_24_Object=MibScalar
job_info_attr_24=_Job_info_attr_24_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,24),_Job_info_attr_24_Type())
job_info_attr_24.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_24.setStatus(_A)
class _Job_info_attr_25_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_25_Type.__name__=_D
_Job_info_attr_25_Object=MibScalar
job_info_attr_25=_Job_info_attr_25_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,25),_Job_info_attr_25_Type())
job_info_attr_25.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_25.setStatus(_A)
class _Job_info_attr_26_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_26_Type.__name__=_D
_Job_info_attr_26_Object=MibScalar
job_info_attr_26=_Job_info_attr_26_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,26),_Job_info_attr_26_Type())
job_info_attr_26.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_26.setStatus(_A)
class _Job_info_attr_27_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_27_Type.__name__=_D
_Job_info_attr_27_Object=MibScalar
job_info_attr_27=_Job_info_attr_27_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,27),_Job_info_attr_27_Type())
job_info_attr_27.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_27.setStatus(_A)
class _Job_info_attr_28_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_28_Type.__name__=_D
_Job_info_attr_28_Object=MibScalar
job_info_attr_28=_Job_info_attr_28_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,28),_Job_info_attr_28_Type())
job_info_attr_28.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_28.setStatus(_A)
class _Job_info_attr_29_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_29_Type.__name__=_D
_Job_info_attr_29_Object=MibScalar
job_info_attr_29=_Job_info_attr_29_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,29),_Job_info_attr_29_Type())
job_info_attr_29.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_29.setStatus(_A)
class _Job_info_attr_30_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_30_Type.__name__=_D
_Job_info_attr_30_Object=MibScalar
job_info_attr_30=_Job_info_attr_30_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,30),_Job_info_attr_30_Type())
job_info_attr_30.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_30.setStatus(_A)
class _Job_info_attr_31_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_31_Type.__name__=_D
_Job_info_attr_31_Object=MibScalar
job_info_attr_31=_Job_info_attr_31_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,31),_Job_info_attr_31_Type())
job_info_attr_31.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_31.setStatus(_A)
class _Job_info_attr_32_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_Job_info_attr_32_Type.__name__=_D
_Job_info_attr_32_Object=MibScalar
job_info_attr_32=_Job_info_attr_32_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,5,23,32),_Job_info_attr_32_Type())
job_info_attr_32.setMaxAccess(_B)
if mibBuilder.loadTexts:job_info_attr_32.setStatus(_A)
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
_Held_job_ObjectIdentity=ObjectIdentity
held_job=_Held_job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7))
_Held_job_info_ObjectIdentity=ObjectIdentity
held_job_info=_Held_job_info_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1))
class _Held_job_user_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Held_job_user_name_Type.__name__=_R
_Held_job_user_name_Object=MibScalar
held_job_user_name=_Held_job_user_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,1),_Held_job_user_name_Type())
held_job_user_name.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_user_name.setStatus(_A)
class _Held_job_job_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Held_job_job_name_Type.__name__=_R
_Held_job_job_name_Object=MibScalar
held_job_job_name=_Held_job_job_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,2),_Held_job_job_name_Type())
held_job_job_name.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_job_name.setStatus(_A)
class _Held_job_retention_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eHoldOff',1),('eHoldOn',2),('eHoldStore',3),('eHoldProof',4)))
_Held_job_retention_Type.__name__=_C
_Held_job_retention_Object=MibScalar
held_job_retention=_Held_job_retention_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,3),_Held_job_retention_Type())
held_job_retention.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_retention.setStatus(_A)
class _Held_job_security_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eHoldTypePublic',1),('eHoldTypePrivate',2)))
_Held_job_security_Type.__name__=_C
_Held_job_security_Object=MibScalar
held_job_security=_Held_job_security_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,4),_Held_job_security_Type())
held_job_security.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_security.setStatus(_A)
class _Held_job_quantity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_Held_job_quantity_Type.__name__=_C
_Held_job_quantity_Object=MibScalar
held_job_quantity=_Held_job_quantity_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,5),_Held_job_quantity_Type())
held_job_quantity.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_quantity.setStatus(_A)
class _Held_job_pin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_Held_job_pin_Type.__name__=_R
_Held_job_pin_Object=MibScalar
held_job_pin=_Held_job_pin_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,1,6),_Held_job_pin_Type())
held_job_pin.setMaxAccess(_B)
if mibBuilder.loadTexts:held_job_pin.setStatus(_A)
_Held_job_control_ObjectIdentity=ObjectIdentity
held_job_control=_Held_job_control_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2))
class _Held_job_print_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Held_job_print_Type.__name__=_D
_Held_job_print_Object=MibScalar
held_job_print=_Held_job_print_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2,1),_Held_job_print_Type())
held_job_print.setMaxAccess(_G)
if mibBuilder.loadTexts:held_job_print.setStatus(_A)
class _Held_job_delete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32768))
_Held_job_delete_Type.__name__=_C
_Held_job_delete_Object=MibScalar
held_job_delete=_Held_job_delete_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2,2),_Held_job_delete_Type())
held_job_delete.setMaxAccess(_G)
if mibBuilder.loadTexts:held_job_delete.setStatus(_A)
class _Held_job_set_queue_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_Held_job_set_queue_size_Type.__name__=_C
_Held_job_set_queue_size_Object=MibScalar
held_job_set_queue_size=_Held_job_set_queue_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2,3),_Held_job_set_queue_size_Type())
held_job_set_queue_size.setMaxAccess(_E)
if mibBuilder.loadTexts:held_job_set_queue_size.setStatus(_A)
class _Held_job_enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eDisabled',1),('eEnabled',2)))
_Held_job_enable_Type.__name__=_C
_Held_job_enable_Object=MibScalar
held_job_enable=_Held_job_enable_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,7,2,4),_Held_job_enable_Type())
held_job_enable.setMaxAccess(_E)
if mibBuilder.loadTexts:held_job_enable.setStatus(_A)
_File_system_ObjectIdentity=ObjectIdentity
file_system=_File_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10))
_Settings_file_system_ObjectIdentity=ObjectIdentity
settings_file_system=_Settings_file_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1))
_File_system_memory_Type=Integer32
_File_system_memory_Object=MibScalar
file_system_memory=_File_system_memory_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,1),_File_system_memory_Type())
file_system_memory.setMaxAccess(_E)
if mibBuilder.loadTexts:file_system_memory.setStatus(_A)
class _File_system_max_open_files_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,512))
_File_system_max_open_files_Type.__name__=_C
_File_system_max_open_files_Object=MibScalar
file_system_max_open_files=_File_system_max_open_files_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,1,2),_File_system_max_open_files_Type())
file_system_max_open_files.setMaxAccess(_E)
if mibBuilder.loadTexts:file_system_max_open_files.setStatus(_A)
_Status_file_system_ObjectIdentity=ObjectIdentity
status_file_system=_Status_file_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,2))
_File_system_statistic_read_open_Type=Integer32
_File_system_statistic_read_open_Object=MibScalar
file_system_statistic_read_open=_File_system_statistic_read_open_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,2,1),_File_system_statistic_read_open_Type())
file_system_statistic_read_open.setMaxAccess(_B)
if mibBuilder.loadTexts:file_system_statistic_read_open.setStatus(_A)
_File_system_statistic_write_open_Type=Integer32
_File_system_statistic_write_open_Object=MibScalar
file_system_statistic_write_open=_File_system_statistic_write_open_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,2,2),_File_system_statistic_write_open_Type())
file_system_statistic_write_open.setMaxAccess(_B)
if mibBuilder.loadTexts:file_system_statistic_write_open.setStatus(_A)
_File_system_statistic_successful_Type=Integer32
_File_system_statistic_successful_Object=MibScalar
file_system_statistic_successful=_File_system_statistic_successful_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,2,3),_File_system_statistic_successful_Type())
file_system_statistic_successful.setMaxAccess(_B)
if mibBuilder.loadTexts:file_system_statistic_successful.setStatus(_A)
_File_system_statistic_unsuccessful_Type=Integer32
_File_system_statistic_unsuccessful_Object=MibScalar
file_system_statistic_unsuccessful=_File_system_statistic_unsuccessful_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,2,4),_File_system_statistic_unsuccessful_Type())
file_system_statistic_unsuccessful.setMaxAccess(_B)
if mibBuilder.loadTexts:file_system_statistic_unsuccessful.setStatus(_A)
_File_system_statistic_current_memory_usage_Type=Integer32
_File_system_statistic_current_memory_usage_Object=MibScalar
file_system_statistic_current_memory_usage=_File_system_statistic_current_memory_usage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,2,5),_File_system_statistic_current_memory_usage_Type())
file_system_statistic_current_memory_usage.setMaxAccess(_B)
if mibBuilder.loadTexts:file_system_statistic_current_memory_usage.setStatus(_A)
_File_system_statistic_max_memory_usage_Type=Integer32
_File_system_statistic_max_memory_usage_Object=MibScalar
file_system_statistic_max_memory_usage=_File_system_statistic_max_memory_usage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,2,6),_File_system_statistic_max_memory_usage_Type())
file_system_statistic_max_memory_usage.setMaxAccess(_B)
if mibBuilder.loadTexts:file_system_statistic_max_memory_usage.setStatus(_A)
_File_systems_ObjectIdentity=ObjectIdentity
file_systems=_File_systems_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3))
_File_system2_ObjectIdentity=ObjectIdentity
file_system2=_File_system2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3,2))
class _File_system2_initialize_volume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eNotInitializing',1),('eInitializing',2)))
_File_system2_initialize_volume_Type.__name__=_C
_File_system2_initialize_volume_Object=MibScalar
file_system2_initialize_volume=_File_system2_initialize_volume_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,10,3,2,6),_File_system2_initialize_volume_Type())
file_system2_initialize_volume.setMaxAccess(_G)
if mibBuilder.loadTexts:file_system2_initialize_volume.setStatus(_A)
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
_Resource_manager_ObjectIdentity=ObjectIdentity
resource_manager=_Resource_manager_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,12))
_Mass_storage_resources_ObjectIdentity=ObjectIdentity
mass_storage_resources=_Mass_storage_resources_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,12,3))
_Mass_storage_resource_change_counter_Type=Integer32
_Mass_storage_resource_change_counter_Object=MibScalar
mass_storage_resource_change_counter=_Mass_storage_resource_change_counter_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,12,3,1),_Mass_storage_resource_change_counter_Type())
mass_storage_resource_change_counter.setMaxAccess(_B)
if mibBuilder.loadTexts:mass_storage_resource_change_counter.setStatus(_A)
class _Mass_storage_resource_changed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('eTrue',2))
_Mass_storage_resource_changed_Type.__name__=_C
_Mass_storage_resource_changed_Object=MibScalar
mass_storage_resource_changed=_Mass_storage_resource_changed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,12,3,2),_Mass_storage_resource_changed_Type())
mass_storage_resource_changed.setMaxAccess(_G)
if mibBuilder.loadTexts:mass_storage_resource_changed.setStatus(_A)
_Remote_procedure_call_ObjectIdentity=ObjectIdentity
remote_procedure_call=_Remote_procedure_call_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13))
_Settings_rpc_ObjectIdentity=ObjectIdentity
settings_rpc=_Settings_rpc_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,1))
_Rpc_test_return_code_Type=OctetString
_Rpc_test_return_code_Object=MibScalar
rpc_test_return_code=_Rpc_test_return_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,1,1),_Rpc_test_return_code_Type())
rpc_test_return_code.setMaxAccess(_G)
if mibBuilder.loadTexts:rpc_test_return_code.setStatus(_A)
_Rpc_bind_protocol_address_Type=OctetString
_Rpc_bind_protocol_address_Object=MibScalar
rpc_bind_protocol_address=_Rpc_bind_protocol_address_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,1,2),_Rpc_bind_protocol_address_Type())
rpc_bind_protocol_address.setMaxAccess(_E)
if mibBuilder.loadTexts:rpc_bind_protocol_address.setStatus(_A)
_Status_rpc_ObjectIdentity=ObjectIdentity
status_rpc=_Status_rpc_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,2))
_Rpc_statistic_successful_Type=Integer32
_Rpc_statistic_successful_Object=MibScalar
rpc_statistic_successful=_Rpc_statistic_successful_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,2,1),_Rpc_statistic_successful_Type())
rpc_statistic_successful.setMaxAccess(_B)
if mibBuilder.loadTexts:rpc_statistic_successful.setStatus(_A)
_Rpc_statistic_unsuccessful_Type=Integer32
_Rpc_statistic_unsuccessful_Object=MibScalar
rpc_statistic_unsuccessful=_Rpc_statistic_unsuccessful_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,2,2),_Rpc_statistic_unsuccessful_Type())
rpc_statistic_unsuccessful.setMaxAccess(_B)
if mibBuilder.loadTexts:rpc_statistic_unsuccessful.setStatus(_A)
_Rpc_bound_protocol_address_Type=OctetString
_Rpc_bound_protocol_address_Object=MibScalar
rpc_bound_protocol_address=_Rpc_bound_protocol_address_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,2,3),_Rpc_bound_protocol_address_Type())
rpc_bound_protocol_address.setMaxAccess(_B)
if mibBuilder.loadTexts:rpc_bound_protocol_address.setStatus(_A)
_Rpc_services_ObjectIdentity=ObjectIdentity
rpc_services=_Rpc_services_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3))
_Nfs_server_ObjectIdentity=ObjectIdentity
nfs_server=_Nfs_server_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2))
_Settings_nfs_server_ObjectIdentity=ObjectIdentity
settings_nfs_server=_Settings_nfs_server_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,1))
_Nfs_server_memory_Type=Integer32
_Nfs_server_memory_Object=MibScalar
nfs_server_memory=_Nfs_server_memory_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,1,1),_Nfs_server_memory_Type())
nfs_server_memory.setMaxAccess(_B)
if mibBuilder.loadTexts:nfs_server_memory.setStatus(_A)
class _Nfs_server_read_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1500))
_Nfs_server_read_size_Type.__name__=_C
_Nfs_server_read_size_Object=MibScalar
nfs_server_read_size=_Nfs_server_read_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,1,2),_Nfs_server_read_size_Type())
nfs_server_read_size.setMaxAccess(_E)
if mibBuilder.loadTexts:nfs_server_read_size.setStatus(_A)
class _Nfs_server_write_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1500))
_Nfs_server_write_size_Type.__name__=_C
_Nfs_server_write_size_Object=MibScalar
nfs_server_write_size=_Nfs_server_write_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,1,3),_Nfs_server_write_size_Type())
nfs_server_write_size.setMaxAccess(_E)
if mibBuilder.loadTexts:nfs_server_write_size.setStatus(_A)
_Nfs_server_test_return_code_Type=OctetString
_Nfs_server_test_return_code_Object=MibScalar
nfs_server_test_return_code=_Nfs_server_test_return_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,1,4),_Nfs_server_test_return_code_Type())
nfs_server_test_return_code.setMaxAccess(_G)
if mibBuilder.loadTexts:nfs_server_test_return_code.setStatus(_A)
_Status_nfs_server_ObjectIdentity=ObjectIdentity
status_nfs_server=_Status_nfs_server_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,2))
_Nfs_server_statistic_successful_Type=Integer32
_Nfs_server_statistic_successful_Object=MibScalar
nfs_server_statistic_successful=_Nfs_server_statistic_successful_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,2,1),_Nfs_server_statistic_successful_Type())
nfs_server_statistic_successful.setMaxAccess(_B)
if mibBuilder.loadTexts:nfs_server_statistic_successful.setStatus(_A)
_Nfs_server_statistic_unsuccessful_Type=Integer32
_Nfs_server_statistic_unsuccessful_Object=MibScalar
nfs_server_statistic_unsuccessful=_Nfs_server_statistic_unsuccessful_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,2,2),_Nfs_server_statistic_unsuccessful_Type())
nfs_server_statistic_unsuccessful.setMaxAccess(_B)
if mibBuilder.loadTexts:nfs_server_statistic_unsuccessful.setStatus(_A)
_Nfs_server_statistic_current_memory_usage_Type=Integer32
_Nfs_server_statistic_current_memory_usage_Object=MibScalar
nfs_server_statistic_current_memory_usage=_Nfs_server_statistic_current_memory_usage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,2,4),_Nfs_server_statistic_current_memory_usage_Type())
nfs_server_statistic_current_memory_usage.setMaxAccess(_B)
if mibBuilder.loadTexts:nfs_server_statistic_current_memory_usage.setStatus(_A)
_Nfs_server_statistic_max_memory_usage_Type=Integer32
_Nfs_server_statistic_max_memory_usage_Object=MibScalar
nfs_server_statistic_max_memory_usage=_Nfs_server_statistic_max_memory_usage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,2,2,5),_Nfs_server_statistic_max_memory_usage_Type())
nfs_server_statistic_max_memory_usage.setMaxAccess(_B)
if mibBuilder.loadTexts:nfs_server_statistic_max_memory_usage.setStatus(_A)
_Rpc_bind_ObjectIdentity=ObjectIdentity
rpc_bind=_Rpc_bind_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,3))
_Settings_rpc_bind_ObjectIdentity=ObjectIdentity
settings_rpc_bind=_Settings_rpc_bind_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,3,1))
_Rpc_bind_test_return_code_Type=OctetString
_Rpc_bind_test_return_code_Object=MibScalar
rpc_bind_test_return_code=_Rpc_bind_test_return_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,3,1,1),_Rpc_bind_test_return_code_Type())
rpc_bind_test_return_code.setMaxAccess(_G)
if mibBuilder.loadTexts:rpc_bind_test_return_code.setStatus(_A)
_Status_rpc_bind_ObjectIdentity=ObjectIdentity
status_rpc_bind=_Status_rpc_bind_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,3,2))
_Rpc_bind_statistic_successful_Type=Integer32
_Rpc_bind_statistic_successful_Object=MibScalar
rpc_bind_statistic_successful=_Rpc_bind_statistic_successful_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,3,2,1),_Rpc_bind_statistic_successful_Type())
rpc_bind_statistic_successful.setMaxAccess(_B)
if mibBuilder.loadTexts:rpc_bind_statistic_successful.setStatus(_A)
_Rpc_bind_statistic_unsuccessful_Type=Integer32
_Rpc_bind_statistic_unsuccessful_Object=MibScalar
rpc_bind_statistic_unsuccessful=_Rpc_bind_statistic_unsuccessful_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,13,3,3,2,2),_Rpc_bind_statistic_unsuccessful_Type())
rpc_bind_statistic_unsuccessful.setMaxAccess(_B)
if mibBuilder.loadTexts:rpc_bind_statistic_unsuccessful.setStatus(_A)
_Xport_interface_ObjectIdentity=ObjectIdentity
xport_interface=_Xport_interface_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,14))
_Status_xip_ObjectIdentity=ObjectIdentity
status_xip=_Status_xip_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,14,2))
_Xip_statistic_processed_Type=Integer32
_Xip_statistic_processed_Object=MibScalar
xip_statistic_processed=_Xip_statistic_processed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,14,2,1),_Xip_statistic_processed_Type())
xip_statistic_processed.setMaxAccess(_B)
if mibBuilder.loadTexts:xip_statistic_processed.setStatus(_A)
_Xip_statistic_data_in_dropped_Type=Integer32
_Xip_statistic_data_in_dropped_Object=MibScalar
xip_statistic_data_in_dropped=_Xip_statistic_data_in_dropped_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,14,2,2),_Xip_statistic_data_in_dropped_Type())
xip_statistic_data_in_dropped.setMaxAccess(_B)
if mibBuilder.loadTexts:xip_statistic_data_in_dropped.setStatus(_A)
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
io_timeout.setMaxAccess(_E)
if mibBuilder.loadTexts:io_timeout.setStatus(_A)
class _Io_switch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eYes',1))
_Io_switch_Type.__name__=_C
_Io_switch_Object=MibScalar
io_switch=_Io_switch_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,2),_Io_switch_Type())
io_switch.setMaxAccess(_B)
if mibBuilder.loadTexts:io_switch.setStatus(_A)
class _Io_buffering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues((_e,3))
_Io_buffering_Type.__name__=_C
_Io_buffering_Object=MibScalar
io_buffering=_Io_buffering_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,5),_Io_buffering_Type())
io_buffering.setMaxAccess(_B)
if mibBuilder.loadTexts:io_buffering.setStatus(_A)
_Io_buffer_size_Type=Integer32
_Io_buffer_size_Object=MibScalar
io_buffer_size=_Io_buffer_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,1,6),_Io_buffer_size_Type())
io_buffer_size.setMaxAccess(_B)
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
class _Port1_parallel_speed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('eFast',2))
_Port1_parallel_speed_Type.__name__=_C
_Port1_parallel_speed_Object=MibScalar
port1_parallel_speed=_Port1_parallel_speed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3,1,4),_Port1_parallel_speed_Type())
port1_parallel_speed.setMaxAccess(_B)
if mibBuilder.loadTexts:port1_parallel_speed.setStatus(_A)
class _Port1_parallel_bidirectionality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('eBidirectional',2))
_Port1_parallel_bidirectionality_Type.__name__=_C
_Port1_parallel_bidirectionality_Object=MibScalar
port1_parallel_bidirectionality=_Port1_parallel_bidirectionality_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,1,3,1,5),_Port1_parallel_bidirectionality_Type())
port1_parallel_bidirectionality.setMaxAccess(_B)
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
default_copies.setMaxAccess(_E)
if mibBuilder.loadTexts:default_copies.setStatus(_A)
class _Resource_saving_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues((_e,3))
_Resource_saving_Type.__name__=_C
_Resource_saving_Object=MibScalar
resource_saving=_Resource_saving_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,6),_Resource_saving_Type())
resource_saving.setMaxAccess(_B)
if mibBuilder.loadTexts:resource_saving.setStatus(_A)
_Maximum_resource_saving_memory_Type=Integer32
_Maximum_resource_saving_memory_Object=MibScalar
maximum_resource_saving_memory=_Maximum_resource_saving_memory_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,7),_Maximum_resource_saving_memory_Type())
maximum_resource_saving_memory.setMaxAccess(_B)
if mibBuilder.loadTexts:maximum_resource_saving_memory.setStatus(_A)
_Default_vertical_black_resolution_Type=Integer32
_Default_vertical_black_resolution_Object=MibScalar
default_vertical_black_resolution=_Default_vertical_black_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,8),_Default_vertical_black_resolution_Type())
default_vertical_black_resolution.setMaxAccess(_E)
if mibBuilder.loadTexts:default_vertical_black_resolution.setStatus(_A)
_Default_horizontal_black_resolution_Type=Integer32
_Default_horizontal_black_resolution_Object=MibScalar
default_horizontal_black_resolution=_Default_horizontal_black_resolution_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,9),_Default_horizontal_black_resolution_Type())
default_horizontal_black_resolution.setMaxAccess(_E)
if mibBuilder.loadTexts:default_horizontal_black_resolution.setStatus(_A)
class _Default_page_protect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues((_e,3))
_Default_page_protect_Type.__name__=_C
_Default_page_protect_Object=MibScalar
default_page_protect=_Default_page_protect_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,10),_Default_page_protect_Type())
default_page_protect.setMaxAccess(_B)
if mibBuilder.loadTexts:default_page_protect.setStatus(_A)
_Default_lines_per_page_Type=Integer32
_Default_lines_per_page_Object=MibScalar
default_lines_per_page=_Default_lines_per_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,11),_Default_lines_per_page_Type())
default_lines_per_page.setMaxAccess(_E)
if mibBuilder.loadTexts:default_lines_per_page.setStatus(_A)
_Default_vmi_Type=Integer32
_Default_vmi_Object=MibScalar
default_vmi=_Default_vmi_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,12),_Default_vmi_Type())
default_vmi.setMaxAccess(_E)
if mibBuilder.loadTexts:default_vmi.setStatus(_A)
class _Default_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,11,25,26,27,45,46,72,80,81,90,91,100)));namedValues=NamedValues(*((_m,1),(_S,2),(_W,3),(_Z,11),(_n,25),(_T,26),(_a,27),(_o,45),(_X,46),('eJapanesePostcardDouble',72),(_p,80),(_q,81),(_r,90),(_s,91),(_t,100)))
_Default_media_size_Type.__name__=_C
_Default_media_size_Object=MibScalar
default_media_size=_Default_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,13),_Default_media_size_Type())
default_media_size.setMaxAccess(_E)
if mibBuilder.loadTexts:default_media_size.setStatus(_A)
class _Cold_reset_media_size_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,26)));namedValues=NamedValues(*((_S,2),(_T,26)))
_Cold_reset_media_size_Type.__name__=_C
_Cold_reset_media_size_Object=MibScalar
cold_reset_media_size=_Cold_reset_media_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,19),_Cold_reset_media_size_Type())
cold_reset_media_size.setMaxAccess(_E)
if mibBuilder.loadTexts:cold_reset_media_size.setStatus(_A)
_Default_media_name_Type=DisplayString
_Default_media_name_Object=MibScalar
default_media_name=_Default_media_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,1,22),_Default_media_name_Type())
default_media_name.setMaxAccess(_E)
if mibBuilder.loadTexts:default_media_name.setStatus(_A)
_Status_pdl_ObjectIdentity=ObjectIdentity
status_pdl=_Status_pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,2))
class _Form_feed_needed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_h,1))
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
pcl_resource_saving_memory_size.setMaxAccess(_B)
if mibBuilder.loadTexts:pcl_resource_saving_memory_size.setStatus(_A)
_Pcl_total_page_count_Type=Integer32
_Pcl_total_page_count_Object=MibScalar
pcl_total_page_count=_Pcl_total_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,5),_Pcl_total_page_count_Type())
pcl_total_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:pcl_total_page_count.setStatus(_A)
_Pcl_default_font_height_Type=Integer32
_Pcl_default_font_height_Object=MibScalar
pcl_default_font_height=_Pcl_default_font_height_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,13),_Pcl_default_font_height_Type())
pcl_default_font_height.setMaxAccess(_E)
if mibBuilder.loadTexts:pcl_default_font_height.setStatus(_A)
class _Pcl_default_font_source_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10,11,12,13)));namedValues=NamedValues(*(('eInternal',1),('ePermanentSoft',2),('eRomSimm1',10),('eRomSimm2',11),('eRomSimm3',12),('eRomSimm4',13)))
_Pcl_default_font_source_Type.__name__=_C
_Pcl_default_font_source_Object=MibScalar
pcl_default_font_source=_Pcl_default_font_source_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,14),_Pcl_default_font_source_Type())
pcl_default_font_source.setMaxAccess(_E)
if mibBuilder.loadTexts:pcl_default_font_source.setStatus(_A)
class _Pcl_default_font_number_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Pcl_default_font_number_Type.__name__=_C
_Pcl_default_font_number_Object=MibScalar
pcl_default_font_number=_Pcl_default_font_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,15),_Pcl_default_font_number_Type())
pcl_default_font_number.setMaxAccess(_E)
if mibBuilder.loadTexts:pcl_default_font_number.setStatus(_A)
_Pcl_default_font_width_Type=Integer32
_Pcl_default_font_width_Object=MibScalar
pcl_default_font_width=_Pcl_default_font_width_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,16),_Pcl_default_font_width_Type())
pcl_default_font_width.setMaxAccess(_E)
if mibBuilder.loadTexts:pcl_default_font_width.setStatus(_A)
_Pdl_postscript_ObjectIdentity=ObjectIdentity
pdl_postscript=_Pdl_postscript_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4))
_Postscript_resource_saving_memory_size_Type=Integer32
_Postscript_resource_saving_memory_size_Object=MibScalar
postscript_resource_saving_memory_size=_Postscript_resource_saving_memory_size_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4,2),_Postscript_resource_saving_memory_size_Type())
postscript_resource_saving_memory_size.setMaxAccess(_B)
if mibBuilder.loadTexts:postscript_resource_saving_memory_size.setStatus(_A)
_Postscript_total_page_count_Type=Integer32
_Postscript_total_page_count_Object=MibScalar
postscript_total_page_count=_Postscript_total_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4,5),_Postscript_total_page_count_Type())
postscript_total_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:postscript_total_page_count.setStatus(_A)
class _Postscript_print_errors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_Y,2)))
_Postscript_print_errors_Type.__name__=_C
_Postscript_print_errors_Object=MibScalar
postscript_print_errors=_Postscript_print_errors_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4,11),_Postscript_print_errors_Type())
postscript_print_errors.setMaxAccess(_E)
if mibBuilder.loadTexts:postscript_print_errors.setStatus(_A)
class _Postscript_jam_recovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues((_Y,2))
_Postscript_jam_recovery_Type.__name__=_C
_Postscript_jam_recovery_Object=MibScalar
postscript_jam_recovery=_Postscript_jam_recovery_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4,12),_Postscript_jam_recovery_Type())
postscript_jam_recovery.setMaxAccess(_B)
if mibBuilder.loadTexts:postscript_jam_recovery.setStatus(_A)
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
class _Jetsend_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_Y,2)))
_Jetsend_mode_Type.__name__=_C
_Jetsend_mode_Object=MibScalar
jetsend_mode=_Jetsend_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,1,1),_Jetsend_mode_Type())
jetsend_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:jetsend_mode.setStatus(_A)
_Jetsend_contact_ObjectIdentity=ObjectIdentity
jetsend_contact=_Jetsend_contact_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,3))
_Settings_jetsend_contact_ObjectIdentity=ObjectIdentity
settings_jetsend_contact=_Settings_jetsend_contact_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,3,1))
class _Jetsend_contact_password_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Jetsend_contact_password_Type.__name__=_D
_Jetsend_contact_password_Object=MibScalar
jetsend_contact_password=_Jetsend_contact_password_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,3,1,1),_Jetsend_contact_password_Type())
jetsend_contact_password.setMaxAccess(_G)
if mibBuilder.loadTexts:jetsend_contact_password.setStatus(_A)
class _Jetsend_contact_ip_address_security_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Jetsend_contact_ip_address_security_Type.__name__=_D
_Jetsend_contact_ip_address_security_Object=MibScalar
jetsend_contact_ip_address_security=_Jetsend_contact_ip_address_security_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,8,3,1,2),_Jetsend_contact_ip_address_security_Type())
jetsend_contact_ip_address_security.setMaxAccess(_G)
if mibBuilder.loadTexts:jetsend_contact_ip_address_security.setStatus(_A)
_Destination_subsystem_ObjectIdentity=ObjectIdentity
destination_subsystem=_Destination_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4))
_Print_engine_ObjectIdentity=ObjectIdentity
print_engine=_Print_engine_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1))
_Status_prt_eng_ObjectIdentity=ObjectIdentity
status_prt_eng=_Status_prt_eng_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2))
class _Total_color_page_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967296))
_Total_color_page_count_Type.__name__=_C
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
mp_tray.setMaxAccess(_E)
if mibBuilder.loadTexts:mp_tray.setStatus(_A)
class _Custom_paper_dim_unit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('eTenThousandthsOfInches',3),('eMicrometers',4)))
_Custom_paper_dim_unit_Type.__name__=_C
_Custom_paper_dim_unit_Object=MibScalar
custom_paper_dim_unit=_Custom_paper_dim_unit_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,7),_Custom_paper_dim_unit_Type())
custom_paper_dim_unit.setMaxAccess(_E)
if mibBuilder.loadTexts:custom_paper_dim_unit.setStatus(_A)
_Custom_paper_feed_dim_Type=Integer32
_Custom_paper_feed_dim_Object=MibScalar
custom_paper_feed_dim=_Custom_paper_feed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,8),_Custom_paper_feed_dim_Type())
custom_paper_feed_dim.setMaxAccess(_E)
if mibBuilder.loadTexts:custom_paper_feed_dim.setStatus(_A)
_Custom_paper_xfeed_dim_Type=Integer32
_Custom_paper_xfeed_dim_Object=MibScalar
custom_paper_xfeed_dim=_Custom_paper_xfeed_dim_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,1,9),_Custom_paper_xfeed_dim_Type())
custom_paper_xfeed_dim.setMaxAccess(_E)
if mibBuilder.loadTexts:custom_paper_xfeed_dim.setStatus(_A)
_Intrays_ObjectIdentity=ObjectIdentity
intrays=_Intrays_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3))
_Intray1_ObjectIdentity=ObjectIdentity
intray1=_Intray1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1))
class _Tray1_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,11,25,26,27,45,46,72,80,81,90,91,100,101)));namedValues=NamedValues(*((_m,1),(_S,2),(_W,3),(_Z,11),(_n,25),(_T,26),(_a,27),(_o,45),(_X,46),('eJapansePostcardDouble',72),(_p,80),(_q,81),(_r,90),(_s,91),(_t,100),('eCustom',101)))
_Tray1_media_size_loaded_Type.__name__=_C
_Tray1_media_size_loaded_Object=MibScalar
tray1_media_size_loaded=_Tray1_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,1),_Tray1_media_size_loaded_Type())
tray1_media_size_loaded.setMaxAccess(_E)
if mibBuilder.loadTexts:tray1_media_size_loaded.setStatus(_A)
_Tray1_phd_Type=Integer32
_Tray1_phd_Object=MibScalar
tray1_phd=_Tray1_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,12),_Tray1_phd_Type())
tray1_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:tray1_phd.setStatus(_A)
_Intray2_ObjectIdentity=ObjectIdentity
intray2=_Intray2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2))
class _Tray2_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,26,46)));namedValues=NamedValues(*((_S,2),(_W,3),(_T,26),(_X,46)))
_Tray2_media_size_loaded_Type.__name__=_C
_Tray2_media_size_loaded_Object=MibScalar
tray2_media_size_loaded=_Tray2_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,1),_Tray2_media_size_loaded_Type())
tray2_media_size_loaded.setMaxAccess(_B)
if mibBuilder.loadTexts:tray2_media_size_loaded.setStatus(_A)
_Tray2_phd_Type=Integer32
_Tray2_phd_Object=MibScalar
tray2_phd=_Tray2_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,12),_Tray2_phd_Type())
tray2_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:tray2_phd.setStatus(_A)
_Intray3_ObjectIdentity=ObjectIdentity
intray3=_Intray3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3))
class _Tray3_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,11,26,27,46)));namedValues=NamedValues(*((_S,2),(_W,3),(_Z,11),(_T,26),(_a,27),(_X,46)))
_Tray3_media_size_loaded_Type.__name__=_C
_Tray3_media_size_loaded_Object=MibScalar
tray3_media_size_loaded=_Tray3_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,1),_Tray3_media_size_loaded_Type())
tray3_media_size_loaded.setMaxAccess(_B)
if mibBuilder.loadTexts:tray3_media_size_loaded.setStatus(_A)
_Tray3_phd_Type=Integer32
_Tray3_phd_Object=MibScalar
tray3_phd=_Tray3_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,12),_Tray3_phd_Type())
tray3_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:tray3_phd.setStatus(_A)
_Intray4_ObjectIdentity=ObjectIdentity
intray4=_Intray4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,4))
class _Tray4_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,11,26,27,46)));namedValues=NamedValues(*((_S,2),(_W,3),(_Z,11),(_T,26),(_a,27),(_X,46)))
_Tray4_media_size_loaded_Type.__name__=_C
_Tray4_media_size_loaded_Object=MibScalar
tray4_media_size_loaded=_Tray4_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,4,1),_Tray4_media_size_loaded_Type())
tray4_media_size_loaded.setMaxAccess(_B)
if mibBuilder.loadTexts:tray4_media_size_loaded.setStatus(_A)
_Tray4_phd_Type=Integer32
_Tray4_phd_Object=MibScalar
tray4_phd=_Tray4_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,4,12),_Tray4_phd_Type())
tray4_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:tray4_phd.setStatus(_A)
_Intray5_ObjectIdentity=ObjectIdentity
intray5=_Intray5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,5))
_Tray5_phd_Type=Integer32
_Tray5_phd_Object=MibScalar
tray5_phd=_Tray5_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,5,12),_Tray5_phd_Type())
tray5_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:tray5_phd.setStatus(_A)
_Outbin_ObjectIdentity=ObjectIdentity
outbin=_Outbin_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4))
_Settings_outbin_ObjectIdentity=ObjectIdentity
settings_outbin=_Settings_outbin_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,1))
_Overflow_bin_Type=Integer32
_Overflow_bin_Object=MibScalar
overflow_bin=_Overflow_bin_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,1,4),_Overflow_bin_Type())
overflow_bin.setMaxAccess(_B)
if mibBuilder.loadTexts:overflow_bin.setStatus(_A)
_Outbins_ObjectIdentity=ObjectIdentity
outbins=_Outbins_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3))
_Outbin1_ObjectIdentity=ObjectIdentity
outbin1=_Outbin1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,1))
_Outbin1_override_mode_Type=OctetString
_Outbin1_override_mode_Object=MibScalar
outbin1_override_mode=_Outbin1_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,1,9),_Outbin1_override_mode_Type())
outbin1_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin1_override_mode.setStatus(_A)
_Outbin2_ObjectIdentity=ObjectIdentity
outbin2=_Outbin2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,2))
_Outbin2_override_mode_Type=OctetString
_Outbin2_override_mode_Object=MibScalar
outbin2_override_mode=_Outbin2_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,2,9),_Outbin2_override_mode_Type())
outbin2_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin2_override_mode.setStatus(_A)
_Outbin3_ObjectIdentity=ObjectIdentity
outbin3=_Outbin3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,3))
_Outbin3_override_mode_Type=OctetString
_Outbin3_override_mode_Object=MibScalar
outbin3_override_mode=_Outbin3_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,3,9),_Outbin3_override_mode_Type())
outbin3_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin3_override_mode.setStatus(_A)
_Outbin3_phd_Type=Integer32
_Outbin3_phd_Object=MibScalar
outbin3_phd=_Outbin3_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,3,11),_Outbin3_phd_Type())
outbin3_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:outbin3_phd.setStatus(_A)
_Outbin4_ObjectIdentity=ObjectIdentity
outbin4=_Outbin4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,4))
_Outbin4_override_mode_Type=OctetString
_Outbin4_override_mode_Object=MibScalar
outbin4_override_mode=_Outbin4_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,4,9),_Outbin4_override_mode_Type())
outbin4_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin4_override_mode.setStatus(_A)
_Outbin4_phd_Type=Integer32
_Outbin4_phd_Object=MibScalar
outbin4_phd=_Outbin4_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,4,11),_Outbin4_phd_Type())
outbin4_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:outbin4_phd.setStatus(_A)
_Outbin5_ObjectIdentity=ObjectIdentity
outbin5=_Outbin5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,5))
_Outbin5_override_mode_Type=OctetString
_Outbin5_override_mode_Object=MibScalar
outbin5_override_mode=_Outbin5_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,5,9),_Outbin5_override_mode_Type())
outbin5_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin5_override_mode.setStatus(_A)
_Outbin5_phd_Type=Integer32
_Outbin5_phd_Object=MibScalar
outbin5_phd=_Outbin5_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,5,11),_Outbin5_phd_Type())
outbin5_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:outbin5_phd.setStatus(_A)
_Outbin6_ObjectIdentity=ObjectIdentity
outbin6=_Outbin6_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,6))
_Outbin6_override_mode_Type=OctetString
_Outbin6_override_mode_Object=MibScalar
outbin6_override_mode=_Outbin6_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,6,9),_Outbin6_override_mode_Type())
outbin6_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin6_override_mode.setStatus(_A)
_Outbin6_phd_Type=Integer32
_Outbin6_phd_Object=MibScalar
outbin6_phd=_Outbin6_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,6,11),_Outbin6_phd_Type())
outbin6_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:outbin6_phd.setStatus(_A)
_Outbin7_ObjectIdentity=ObjectIdentity
outbin7=_Outbin7_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,7))
_Outbin7_override_mode_Type=OctetString
_Outbin7_override_mode_Object=MibScalar
outbin7_override_mode=_Outbin7_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,7,9),_Outbin7_override_mode_Type())
outbin7_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin7_override_mode.setStatus(_A)
_Outbin7_phd_Type=Integer32
_Outbin7_phd_Object=MibScalar
outbin7_phd=_Outbin7_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,7,11),_Outbin7_phd_Type())
outbin7_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:outbin7_phd.setStatus(_A)
_Outbin8_ObjectIdentity=ObjectIdentity
outbin8=_Outbin8_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,8))
_Outbin8_override_mode_Type=OctetString
_Outbin8_override_mode_Object=MibScalar
outbin8_override_mode=_Outbin8_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,8,9),_Outbin8_override_mode_Type())
outbin8_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin8_override_mode.setStatus(_A)
_Outbin8_phd_Type=Integer32
_Outbin8_phd_Object=MibScalar
outbin8_phd=_Outbin8_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,8,11),_Outbin8_phd_Type())
outbin8_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:outbin8_phd.setStatus(_A)
_Outbin9_ObjectIdentity=ObjectIdentity
outbin9=_Outbin9_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,9))
_Outbin9_override_mode_Type=OctetString
_Outbin9_override_mode_Object=MibScalar
outbin9_override_mode=_Outbin9_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,9,9),_Outbin9_override_mode_Type())
outbin9_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin9_override_mode.setStatus(_A)
_Outbin9_phd_Type=Integer32
_Outbin9_phd_Object=MibScalar
outbin9_phd=_Outbin9_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,9,11),_Outbin9_phd_Type())
outbin9_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:outbin9_phd.setStatus(_A)
_Outbin10_ObjectIdentity=ObjectIdentity
outbin10=_Outbin10_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,10))
_Outbin10_override_mode_Type=OctetString
_Outbin10_override_mode_Object=MibScalar
outbin10_override_mode=_Outbin10_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,10,9),_Outbin10_override_mode_Type())
outbin10_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin10_override_mode.setStatus(_A)
_Outbin10_phd_Type=Integer32
_Outbin10_phd_Object=MibScalar
outbin10_phd=_Outbin10_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,10,11),_Outbin10_phd_Type())
outbin10_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:outbin10_phd.setStatus(_A)
_Outbin11_ObjectIdentity=ObjectIdentity
outbin11=_Outbin11_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,11))
_Outbin11_override_mode_Type=OctetString
_Outbin11_override_mode_Object=MibScalar
outbin11_override_mode=_Outbin11_override_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,11,9),_Outbin11_override_mode_Type())
outbin11_override_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:outbin11_override_mode.setStatus(_A)
_Outbin11_phd_Type=Integer32
_Outbin11_phd_Object=MibScalar
outbin11_phd=_Outbin11_phd_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,4,3,11,11),_Outbin11_phd_Type())
outbin11_phd.setMaxAccess(_B)
if mibBuilder.loadTexts:outbin11_phd.setStatus(_A)
_Marking_agent_ObjectIdentity=ObjectIdentity
marking_agent=_Marking_agent_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,5))
_Settings_marking_agent_ObjectIdentity=ObjectIdentity
settings_marking_agent=_Settings_marking_agent_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,5,1))
class _Low_marking_agent_processing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eStop',1),('eCont',2)))
_Low_marking_agent_processing_Type.__name__=_C
_Low_marking_agent_processing_Object=MibScalar
low_marking_agent_processing=_Low_marking_agent_processing_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,5,1,3),_Low_marking_agent_processing_Type())
low_marking_agent_processing.setMaxAccess(_E)
if mibBuilder.loadTexts:low_marking_agent_processing.setStatus(_A)
_Imaging_ObjectIdentity=ObjectIdentity
imaging=_Imaging_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,6))
class _Default_ret_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_f,1))
_Default_ret_Type.__name__=_C
_Default_ret_Object=MibScalar
default_ret=_Default_ret_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,6,5),_Default_ret_Type())
default_ret.setMaxAccess(_B)
if mibBuilder.loadTexts:default_ret.setStatus(_A)
class _Default_print_quality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100))
_Default_print_quality_Type.__name__=_C
_Default_print_quality_Object=MibScalar
default_print_quality=_Default_print_quality_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,6,7),_Default_print_quality_Type())
default_print_quality.setMaxAccess(_B)
if mibBuilder.loadTexts:default_print_quality.setStatus(_A)
_Ph_ObjectIdentity=ObjectIdentity
ph=_Ph_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7))
_Ph_devices_ObjectIdentity=ObjectIdentity
ph_devices=_Ph_devices_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7,3))
_Ph2_ObjectIdentity=ObjectIdentity
ph2=_Ph2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7,3,2))
_Phd2_device_specific_command_Type=OctetString
_Phd2_device_specific_command_Object=MibScalar
phd2_device_specific_command=_Phd2_device_specific_command_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7,3,2,2),_Phd2_device_specific_command_Type())
phd2_device_specific_command.setMaxAccess(_G)
if mibBuilder.loadTexts:phd2_device_specific_command.setStatus(_A)
class _Phd2_device_memory_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Phd2_device_memory_Type.__name__=_D
_Phd2_device_memory_Object=MibScalar
phd2_device_memory=_Phd2_device_memory_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7,3,2,4),_Phd2_device_memory_Type())
phd2_device_memory.setMaxAccess(_B)
if mibBuilder.loadTexts:phd2_device_memory.setStatus(_A)
_Ph3_ObjectIdentity=ObjectIdentity
ph3=_Ph3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7,3,3))
_Phd3_device_specific_command_Type=OctetString
_Phd3_device_specific_command_Object=MibScalar
phd3_device_specific_command=_Phd3_device_specific_command_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7,3,3,2),_Phd3_device_specific_command_Type())
phd3_device_specific_command.setMaxAccess(_G)
if mibBuilder.loadTexts:phd3_device_specific_command.setStatus(_A)
class _Phd3_device_memory_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Phd3_device_memory_Type.__name__=_D
_Phd3_device_memory_Object=MibScalar
phd3_device_memory=_Phd3_device_memory_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,7,3,3,4),_Phd3_device_memory_Type())
phd3_device_memory.setMaxAccess(_B)
if mibBuilder.loadTexts:phd3_device_memory.setStatus(_A)
_Print_media_ObjectIdentity=ObjectIdentity
print_media=_Print_media_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8))
_Settings_print_media_ObjectIdentity=ObjectIdentity
settings_print_media=_Settings_print_media_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1))
_Media_names_available_Type=OctetString
_Media_names_available_Object=MibScalar
media_names_available=_Media_names_available_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1,1),_Media_names_available_Type())
media_names_available.setMaxAccess(_E)
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
_Media13_ObjectIdentity=ObjectIdentity
media13=_Media13_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13))
_Media13_name_Type=DisplayString
_Media13_name_Object=MibScalar
media13_name=_Media13_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13,1),_Media13_name_Type())
media13_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media13_name.setStatus(_A)
_Media13_short_name_Type=DisplayString
_Media13_short_name_Object=MibScalar
media13_short_name=_Media13_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13,2),_Media13_short_name_Type())
media13_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media13_short_name.setStatus(_A)
_Media13_page_count_Type=Integer32
_Media13_page_count_Object=MibScalar
media13_page_count=_Media13_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13,3),_Media13_page_count_Type())
media13_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media13_page_count.setStatus(_A)
_Media14_ObjectIdentity=ObjectIdentity
media14=_Media14_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14))
_Media14_name_Type=DisplayString
_Media14_name_Object=MibScalar
media14_name=_Media14_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14,1),_Media14_name_Type())
media14_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media14_name.setStatus(_A)
_Media14_short_name_Type=DisplayString
_Media14_short_name_Object=MibScalar
media14_short_name=_Media14_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14,2),_Media14_short_name_Type())
media14_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media14_short_name.setStatus(_A)
_Media14_page_count_Type=Integer32
_Media14_page_count_Object=MibScalar
media14_page_count=_Media14_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14,3),_Media14_page_count_Type())
media14_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media14_page_count.setStatus(_A)
_Media15_ObjectIdentity=ObjectIdentity
media15=_Media15_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15))
_Media15_name_Type=DisplayString
_Media15_name_Object=MibScalar
media15_name=_Media15_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15,1),_Media15_name_Type())
media15_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media15_name.setStatus(_A)
_Media15_short_name_Type=DisplayString
_Media15_short_name_Object=MibScalar
media15_short_name=_Media15_short_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15,2),_Media15_short_name_Type())
media15_short_name.setMaxAccess(_B)
if mibBuilder.loadTexts:media15_short_name.setStatus(_A)
_Media15_page_count_Type=Integer32
_Media15_page_count_Object=MibScalar
media15_page_count=_Media15_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15,3),_Media15_page_count_Type())
media15_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:media15_page_count.setStatus(_A)
_Print_engine_test_ObjectIdentity=ObjectIdentity
print_engine_test=_Print_engine_test_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,9))
class _Pe_test_button_press_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('eButton1Pressed',1),('eButton2Pressed',2),('eButton3Pressed',3),('eButton4Pressed',4),('eButton5Pressed',5),('eButton6Pressed',6),('eButton7Pressed',7),('eButton8Pressed',8),('eButton9Pressed',9),('eButton10Pressed',10)))
_Pe_test_button_press_Type.__name__=_C
_Pe_test_button_press_Object=MibScalar
pe_test_button_press=_Pe_test_button_press_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,9,6),_Pe_test_button_press_Type())
pe_test_button_press.setMaxAccess(_G)
if mibBuilder.loadTexts:pe_test_button_press.setStatus(_A)
_Channel_ObjectIdentity=ObjectIdentity
channel=_Channel_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,6))
_Channelnumberofchannels_Type=Integer32
_Channelnumberofchannels_Object=MibScalar
channelnumberofchannels=_Channelnumberofchannels_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,6,1),_Channelnumberofchannels_Type())
channelnumberofchannels.setMaxAccess(_G)
if mibBuilder.loadTexts:channelnumberofchannels.setStatus(_A)
_Channelprinteralert_Type=OctetString
_Channelprinteralert_Object=MibScalar
channelprinteralert=_Channelprinteralert_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,6,2),_Channelprinteralert_Type())
channelprinteralert.setMaxAccess(_B)
if mibBuilder.loadTexts:channelprinteralert.setStatus(_A)
_ChannelTable_ObjectIdentity=ObjectIdentity
channelTable=_ChannelTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,6,3))
_ChannelEntry_ObjectIdentity=ObjectIdentity
channelEntry=_ChannelEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,6,3,1))
class _Channeltype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,7,8,9,10,11,15,38)));namedValues=NamedValues(*((_u,1),('eChAppleTalkPAP',7),('eChLPDServer',8),('eChNetwareRPrinter',9),('eChNetwarePServer',10),('eChPort9100',11),('eChDLCLLCPort',15),('eChBidirPortTCP',38)))
_Channeltype_Type.__name__=_C
_Channeltype_Object=MibScalar
channeltype=_Channeltype_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,6,3,1,2),_Channeltype_Type())
channeltype.setMaxAccess(_G)
if mibBuilder.loadTexts:channeltype.setStatus(_A)
_Channelprotocolversion_Type=OctetString
_Channelprotocolversion_Object=MibScalar
channelprotocolversion=_Channelprotocolversion_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,6,3,1,3),_Channelprotocolversion_Type())
channelprotocolversion.setMaxAccess(_G)
if mibBuilder.loadTexts:channelprotocolversion.setStatus(_A)
class _Channelstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_u,1),('eChPrintDataAccecped',3),('eChNoDataAccepted',4)))
_Channelstate_Type.__name__=_C
_Channelstate_Object=MibScalar
channelstate=_Channelstate_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,6,3,1,4),_Channelstate_Type())
channelstate.setMaxAccess(_G)
if mibBuilder.loadTexts:channelstate.setStatus(_A)
_Channelifindex_Type=Integer32
_Channelifindex_Object=MibScalar
channelifindex=_Channelifindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,6,3,1,5),_Channelifindex_Type())
channelifindex.setMaxAccess(_G)
if mibBuilder.loadTexts:channelifindex.setStatus(_A)
_Channelstatus_Type=Integer32
_Channelstatus_Object=MibScalar
channelstatus=_Channelstatus_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,6,3,1,6),_Channelstatus_Type())
channelstatus.setMaxAccess(_G)
if mibBuilder.loadTexts:channelstatus.setStatus(_A)
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
_Prtgeneralconfigchanges_Type=Integer32
_Prtgeneralconfigchanges_Object=MibScalar
prtgeneralconfigchanges=_Prtgeneralconfigchanges_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,1),_Prtgeneralconfigchanges_Type())
prtgeneralconfigchanges.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgeneralconfigchanges.setStatus(_A)
class _Prtgeneralcurrentlocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,11))
_Prtgeneralcurrentlocalization_Type.__name__=_C
_Prtgeneralcurrentlocalization_Object=MibScalar
prtgeneralcurrentlocalization=_Prtgeneralcurrentlocalization_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,2),_Prtgeneralcurrentlocalization_Type())
prtgeneralcurrentlocalization.setMaxAccess(_E)
if mibBuilder.loadTexts:prtgeneralcurrentlocalization.setStatus(_A)
class _Prtgeneralreset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6)));namedValues=NamedValues(*(('ePnotResetting',3),('ePpowerCycleReset',4),('ePresetToNVRAM',5),('ePresetToFactoryDefaults',6)))
_Prtgeneralreset_Type.__name__=_C
_Prtgeneralreset_Object=MibScalar
prtgeneralreset=_Prtgeneralreset_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,3),_Prtgeneralreset_Type())
prtgeneralreset.setMaxAccess(_E)
if mibBuilder.loadTexts:prtgeneralreset.setStatus(_A)
class _Prtgeneralcurrentoperator_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Prtgeneralcurrentoperator_Type.__name__=_D
_Prtgeneralcurrentoperator_Object=MibScalar
prtgeneralcurrentoperator=_Prtgeneralcurrentoperator_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,4),_Prtgeneralcurrentoperator_Type())
prtgeneralcurrentoperator.setMaxAccess(_E)
if mibBuilder.loadTexts:prtgeneralcurrentoperator.setStatus(_A)
class _Prtgeneralserviceperson_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Prtgeneralserviceperson_Type.__name__=_D
_Prtgeneralserviceperson_Object=MibScalar
prtgeneralserviceperson=_Prtgeneralserviceperson_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,5),_Prtgeneralserviceperson_Type())
prtgeneralserviceperson.setMaxAccess(_E)
if mibBuilder.loadTexts:prtgeneralserviceperson.setStatus(_A)
_Prtinputdefaultindex_Type=Integer32
_Prtinputdefaultindex_Object=MibScalar
prtinputdefaultindex=_Prtinputdefaultindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,6),_Prtinputdefaultindex_Type())
prtinputdefaultindex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputdefaultindex.setStatus(_A)
_Prtoutputdefaultindex_Type=Integer32
_Prtoutputdefaultindex_Object=MibScalar
prtoutputdefaultindex=_Prtoutputdefaultindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,7),_Prtoutputdefaultindex_Type())
prtoutputdefaultindex.setMaxAccess(_E)
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
prtmediapathdefaultindex.setMaxAccess(_E)
if mibBuilder.loadTexts:prtmediapathdefaultindex.setStatus(_A)
class _Prtconsolelocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Prtconsolelocalization_Type.__name__=_C
_Prtconsolelocalization_Object=MibScalar
prtconsolelocalization=_Prtconsolelocalization_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,10),_Prtconsolelocalization_Type())
prtconsolelocalization.setMaxAccess(_E)
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
class _Prtconsoledisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6)));namedValues=NamedValues(*(('ePoperatorConsoleEnabled',3),('ePoperatorConsoleDisabled',4),('ePoperatorConsoleEnabledLevel1',5),('ePoperatorConsoleEnabledLevel2',6)))
_Prtconsoledisable_Type.__name__=_C
_Prtconsoledisable_Object=MibScalar
prtconsoledisable=_Prtconsoledisable_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,13),_Prtconsoledisable_Type())
prtconsoledisable.setMaxAccess(_E)
if mibBuilder.loadTexts:prtconsoledisable.setStatus(_A)
class _Prtgeneralbannerpage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(5));namedValues=NamedValues((_N,5))
_Prtgeneralbannerpage_Type.__name__=_C
_Prtgeneralbannerpage_Object=MibScalar
prtgeneralbannerpage=_Prtgeneralbannerpage_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,5,1,1,15),_Prtgeneralbannerpage_Type())
prtgeneralbannerpage.setMaxAccess(_B)
if mibBuilder.loadTexts:prtgeneralbannerpage.setStatus(_A)
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
_Prtcoverdescription_Type.__name__=_D
_Prtcoverdescription_Object=MibScalar
prtcoverdescription=_Prtcoverdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,6,1,1,2),_Prtcoverdescription_Type())
prtcoverdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtcoverdescription.setStatus(_A)
class _Prtcoverstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('ePCoverOpen',3),('ePCoverClosed',4)))
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
_Prtlocalizationlanguage_Type.__name__=_D
_Prtlocalizationlanguage_Object=MibScalar
prtlocalizationlanguage=_Prtlocalizationlanguage_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,7,1,1,2),_Prtlocalizationlanguage_Type())
prtlocalizationlanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:prtlocalizationlanguage.setStatus(_A)
class _Prtlocalizationcountry_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_Prtlocalizationcountry_Type.__name__=_D
_Prtlocalizationcountry_Object=MibScalar
prtlocalizationcountry=_Prtlocalizationcountry_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,7,1,1,3),_Prtlocalizationcountry_Type())
prtlocalizationcountry.setMaxAccess(_B)
if mibBuilder.loadTexts:prtlocalizationcountry.setStatus(_A)
class _Prtlocalizationcharacterset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2004));namedValues=NamedValues((_g,2004))
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
class _Prtinputtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,1),(_O,2),('ePsheetFeedAutoRemovableTray',3),('ePsheetFeedAutoNonRemovableTray',4),('ePsheetFeedManual',5),('ePcontinuousRoll',6),('ePcontinuousFanFold',7)))
_Prtinputtype_Type.__name__=_C
_Prtinputtype_Object=MibScalar
prtinputtype=_Prtinputtype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,2),_Prtinputtype_Type())
prtinputtype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputtype.setStatus(_A)
class _Prtinputdimunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_P,3),(_Q,4)))
_Prtinputdimunit_Type.__name__=_C
_Prtinputdimunit_Object=MibScalar
prtinputdimunit=_Prtinputdimunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,3),_Prtinputdimunit_Type())
prtinputdimunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputdimunit.setStatus(_A)
_Prtinputmediadimfeeddirdeclared_Type=Integer32
_Prtinputmediadimfeeddirdeclared_Object=MibScalar
prtinputmediadimfeeddirdeclared=_Prtinputmediadimfeeddirdeclared_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,4),_Prtinputmediadimfeeddirdeclared_Type())
prtinputmediadimfeeddirdeclared.setMaxAccess(_E)
if mibBuilder.loadTexts:prtinputmediadimfeeddirdeclared.setStatus(_A)
_Prtinputmediadimxfeeddirdeclared_Type=Integer32
_Prtinputmediadimxfeeddirdeclared_Object=MibScalar
prtinputmediadimxfeeddirdeclared=_Prtinputmediadimxfeeddirdeclared_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,5),_Prtinputmediadimxfeeddirdeclared_Type())
prtinputmediadimxfeeddirdeclared.setMaxAccess(_E)
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
class _Prtinputcapacityunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,8,16,17)));namedValues=NamedValues(*((_P,3),(_Q,4),(_b,8),(_c,16),(_d,17)))
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
_Prtinputmedianame_Type.__name__=_D
_Prtinputmedianame_Object=MibScalar
prtinputmedianame=_Prtinputmedianame_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,12),_Prtinputmedianame_Type())
prtinputmedianame.setMaxAccess(_E)
if mibBuilder.loadTexts:prtinputmedianame.setStatus(_A)
class _Prtinputname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputname_Type.__name__=_D
_Prtinputname_Object=MibScalar
prtinputname=_Prtinputname_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,13),_Prtinputname_Type())
prtinputname.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputname.setStatus(_A)
class _Prtinputvendorname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputvendorname_Type.__name__=_D
_Prtinputvendorname_Object=MibScalar
prtinputvendorname=_Prtinputvendorname_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,14),_Prtinputvendorname_Type())
prtinputvendorname.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputvendorname.setStatus(_A)
class _Prtinputmodel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputmodel_Type.__name__=_D
_Prtinputmodel_Object=MibScalar
prtinputmodel=_Prtinputmodel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,15),_Prtinputmodel_Type())
prtinputmodel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputmodel.setStatus(_A)
class _Prtinputversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputversion_Type.__name__=_D
_Prtinputversion_Object=MibScalar
prtinputversion=_Prtinputversion_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,16),_Prtinputversion_Type())
prtinputversion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputversion.setStatus(_A)
class _Prtinputserialnumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtinputserialnumber_Type.__name__=_D
_Prtinputserialnumber_Object=MibScalar
prtinputserialnumber=_Prtinputserialnumber_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,17),_Prtinputserialnumber_Type())
prtinputserialnumber.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputserialnumber.setStatus(_A)
class _Prtinputdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtinputdescription_Type.__name__=_D
_Prtinputdescription_Object=MibScalar
prtinputdescription=_Prtinputdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,8,2,1,18),_Prtinputdescription_Type())
prtinputdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinputdescription.setStatus(_A)
class _Prtinputsecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_H,1),(_U,3),(_V,4),(_N,5)))
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
class _Prtoutputtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,1),(_O,2),('ePremovableBin',3),('ePunRemovableBin',4),('ePcontinuousRollDevice',5),('ePmailBox',6),('ePcontinousFanFold',7)))
_Prtoutputtype_Type.__name__=_C
_Prtoutputtype_Object=MibScalar
prtoutputtype=_Prtoutputtype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,2),_Prtoutputtype_Type())
prtoutputtype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputtype.setStatus(_A)
class _Prtoutputcapacityunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,8,16,17)));namedValues=NamedValues(*((_P,3),(_Q,4),(_b,8),(_c,16),(_d,17)))
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
class _Prtoutputname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_Prtoutputname_Type.__name__=_D
_Prtoutputname_Object=MibScalar
prtoutputname=_Prtoutputname_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,7),_Prtoutputname_Type())
prtoutputname.setMaxAccess(_E)
if mibBuilder.loadTexts:prtoutputname.setStatus(_A)
class _Prtoutputvendorname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtoutputvendorname_Type.__name__=_D
_Prtoutputvendorname_Object=MibScalar
prtoutputvendorname=_Prtoutputvendorname_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,8),_Prtoutputvendorname_Type())
prtoutputvendorname.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputvendorname.setStatus(_A)
class _Prtoutputmodel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtoutputmodel_Type.__name__=_D
_Prtoutputmodel_Object=MibScalar
prtoutputmodel=_Prtoutputmodel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,9),_Prtoutputmodel_Type())
prtoutputmodel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputmodel.setStatus(_A)
class _Prtoutputversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtoutputversion_Type.__name__=_D
_Prtoutputversion_Object=MibScalar
prtoutputversion=_Prtoutputversion_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,10),_Prtoutputversion_Type())
prtoutputversion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputversion.setStatus(_A)
class _Prtoutputserialnumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtoutputserialnumber_Type.__name__=_D
_Prtoutputserialnumber_Object=MibScalar
prtoutputserialnumber=_Prtoutputserialnumber_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,11),_Prtoutputserialnumber_Type())
prtoutputserialnumber.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputserialnumber.setStatus(_A)
class _Prtoutputdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtoutputdescription_Type.__name__=_D
_Prtoutputdescription_Object=MibScalar
prtoutputdescription=_Prtoutputdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,12),_Prtoutputdescription_Type())
prtoutputdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputdescription.setStatus(_A)
class _Prtoutputsecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_H,1),(_U,3),(_V,4),(_N,5)))
_Prtoutputsecurity_Type.__name__=_C
_Prtoutputsecurity_Object=MibScalar
prtoutputsecurity=_Prtoutputsecurity_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,13),_Prtoutputsecurity_Type())
prtoutputsecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputsecurity.setStatus(_A)
class _Prtoutputstackingorder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_O,2),('ePfirstToLast',3),('ePlastToFirst',4)))
_Prtoutputstackingorder_Type.__name__=_C
_Prtoutputstackingorder_Object=MibScalar
prtoutputstackingorder=_Prtoutputstackingorder_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,19),_Prtoutputstackingorder_Type())
prtoutputstackingorder.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputstackingorder.setStatus(_A)
class _Prtoutputpagedeliveryorientation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('ePfaceUp',3),('ePfaceDown',4)))
_Prtoutputpagedeliveryorientation_Type.__name__=_C
_Prtoutputpagedeliveryorientation_Object=MibScalar
prtoutputpagedeliveryorientation=_Prtoutputpagedeliveryorientation_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,20),_Prtoutputpagedeliveryorientation_Type())
prtoutputpagedeliveryorientation.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputpagedeliveryorientation.setStatus(_A)
class _Prtoutputbursting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_H,1),(_U,3),(_V,4),(_N,5)))
_Prtoutputbursting_Type.__name__=_C
_Prtoutputbursting_Object=MibScalar
prtoutputbursting=_Prtoutputbursting_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,21),_Prtoutputbursting_Type())
prtoutputbursting.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputbursting.setStatus(_A)
class _Prtoutputdecollating_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_H,1),(_U,3),(_V,4),(_N,5)))
_Prtoutputdecollating_Type.__name__=_C
_Prtoutputdecollating_Object=MibScalar
prtoutputdecollating=_Prtoutputdecollating_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,22),_Prtoutputdecollating_Type())
prtoutputdecollating.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputdecollating.setStatus(_A)
class _Prtoutputpagecollated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_H,1),(_U,3),(_V,4),(_N,5)))
_Prtoutputpagecollated_Type.__name__=_C
_Prtoutputpagecollated_Object=MibScalar
prtoutputpagecollated=_Prtoutputpagecollated_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,23),_Prtoutputpagecollated_Type())
prtoutputpagecollated.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputpagecollated.setStatus(_A)
class _Prtoutputoffsetstacking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_H,1),(_U,3),(_V,4),(_N,5)))
_Prtoutputoffsetstacking_Type.__name__=_C
_Prtoutputoffsetstacking_Object=MibScalar
prtoutputoffsetstacking=_Prtoutputoffsetstacking_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,9,2,1,24),_Prtoutputoffsetstacking_Type())
prtoutputoffsetstacking.setMaxAccess(_B)
if mibBuilder.loadTexts:prtoutputoffsetstacking.setStatus(_A)
_PrtMarker_ObjectIdentity=ObjectIdentity
prtMarker=_PrtMarker_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,10))
_PrtMarkerTable_ObjectIdentity=ObjectIdentity
prtMarkerTable=_PrtMarkerTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2))
_PrtMarkerEntry_ObjectIdentity=ObjectIdentity
prtMarkerEntry=_PrtMarkerEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1))
class _Prtmarkermarktech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_H,1),(_O,2),('ePelectrophotographicLED',3),('ePelectrophotographicLaser',4),('ePelectrophotographicOther',5),('ePimpactMovingHeadDotMatrix9pin',6),('ePimpactMovingHeadDotMatrix24pin',7),('ePimpactMovingHeadDotMatrixOther',8),('ePimpactMovingHeadFullyFormed',9),('ePimpactBand',10),('ePimpactOther',11),('ePinkjetAqueous',12),('ePinkjetSolid',13),('ePinkjetOther',14),('ePpen',15),('ePthermalTransfer',16),('ePthermalSensitive',17),('ePthermalDiffusion',18),('ePthermalOther',19),('ePelectroerosion',20),('ePelectrostatic',21),('ePphotographicMicrofiche',22),('ePphotographicImagesetter',23),('ePphotographicOther',24),('ePionDeposition',25),('ePeBeam',26),('ePtypesetter',27)))
_Prtmarkermarktech_Type.__name__=_C
_Prtmarkermarktech_Object=MibScalar
prtmarkermarktech=_Prtmarkermarktech_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,10,2,1,2),_Prtmarkermarktech_Type())
prtmarkermarktech.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkermarktech.setStatus(_A)
class _Prtmarkercounterunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,11,16,17)));namedValues=NamedValues(*((_P,3),(_Q,4),('ePcharacters',5),('ePlines',6),(_v,7),(_b,8),('ePdotRow',9),(_w,11),(_c,16),(_d,17)))
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
class _Prtmarkeraddressabilityunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_P,3),(_Q,4)))
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
class _Prtmarkersuppliesclass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_H,1),('ePsupplyThatIsConsumed',3),('ePreceptacleThatIsFilled',4)))
_Prtmarkersuppliesclass_Type.__name__=_C
_Prtmarkersuppliesclass_Object=MibScalar
prtmarkersuppliesclass=_Prtmarkersuppliesclass_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,4),_Prtmarkersuppliesclass_Type())
prtmarkersuppliesclass.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliesclass.setStatus(_A)
class _Prtmarkersuppliestype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_H,1),(_O,2),('ePtoner',3),('ePwasteToner',4),('ePink',5),('ePinkCartridge',6),('ePinkRibbon',7),('ePwasteInk',8),('ePopc',9),('ePdeveloper',10),('ePfuserOil',11),('ePsolidWax',12),('ePribbonWax',13),('ePwasteWax',14),('ePfuser',15),('ePcoronaWire',16),('ePfuserOilWick',17),('ePcleanerUnit',18),('ePfuserCleaningPad',19),('ePtransferUnit',20),('ePtonerCartridge',21),('ePfuserOiler',22)))
_Prtmarkersuppliestype_Type.__name__=_C
_Prtmarkersuppliestype_Object=MibScalar
prtmarkersuppliestype=_Prtmarkersuppliestype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,5),_Prtmarkersuppliestype_Type())
prtmarkersuppliestype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliestype.setStatus(_A)
class _Prtmarkersuppliesdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtmarkersuppliesdescription_Type.__name__=_D
_Prtmarkersuppliesdescription_Object=MibScalar
prtmarkersuppliesdescription=_Prtmarkersuppliesdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,11,1,1,6),_Prtmarkersuppliesdescription_Type())
prtmarkersuppliesdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmarkersuppliesdescription.setStatus(_A)
class _Prtmarkersuppliessupplyunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,7,8,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_P,3),(_Q,4),(_v,7),(_b,8),(_w,11),('ePthousandthsOfOunces',12),('ePtenthsOfGrams',13),('ePhundrethsOfFluidOunces',14),('ePtenthsOfMilliliters',15),(_c,16),(_d,17)))
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
class _Prtmediapathmaxspeedprintunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,16,17)));namedValues=NamedValues(*(('ePtenThousandthsOfInchesPerHour',3),('ePmicrometersPerHour',4),('ePcharactersPerHour',5),('ePlinesPerHour',6),('ePimpressionsPerHour',7),('ePsheetsPerHour',8),('ePdotRowPerHour',9),('ePfeetPerHour',16),('ePmetersPerHour',17)))
_Prtmediapathmaxspeedprintunit_Type.__name__=_C
_Prtmediapathmaxspeedprintunit_Object=MibScalar
prtmediapathmaxspeedprintunit=_Prtmediapathmaxspeedprintunit_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,13,4,1,2),_Prtmediapathmaxspeedprintunit_Type())
prtmediapathmaxspeedprintunit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtmediapathmaxspeedprintunit.setStatus(_A)
class _Prtmediapathmediasizeunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_P,3),(_Q,4)))
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
_Prtmediapathdescription_Type.__name__=_D
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
class _Prtchanneltype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,7,10,15,38)));namedValues=NamedValues(*((_H,1),('ePchIEEE1284Port',5),('ePchAppleTalkPAP',7),('ePchNetwarePServer',10),('ePchDLCLLCPort',15),('ePchBidirPortTCP',38)))
_Prtchanneltype_Type.__name__=_C
_Prtchanneltype_Object=MibScalar
prtchanneltype=_Prtchanneltype_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,14,1,1,2),_Prtchanneltype_Type())
prtchanneltype.setMaxAccess(_B)
if mibBuilder.loadTexts:prtchanneltype.setStatus(_A)
class _Prtchannelprotocolversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_Prtchannelprotocolversion_Type.__name__=_D
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
prtchanneldefaultpagedesclangindex.setMaxAccess(_E)
if mibBuilder.loadTexts:prtchanneldefaultpagedesclangindex.setStatus(_A)
class _Prtchannelstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_H,1),('ePprintDataAccepted',3),('ePnoDataAccepted',4)))
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
_PrtInterpreter_ObjectIdentity=ObjectIdentity
prtInterpreter=_PrtInterpreter_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,15))
_PrtInterpreterTable_ObjectIdentity=ObjectIdentity
prtInterpreterTable=_PrtInterpreterTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1))
_PrtInterpreterEntry_ObjectIdentity=ObjectIdentity
prtInterpreterEntry=_PrtInterpreterEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1))
class _Prtinterpreterlangfamily_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,5,6,37)));namedValues=NamedValues(*(('ePlangPCL',3),('ePlangPJL',5),('ePlangPS',6),('ePlangAutomatic',37)))
_Prtinterpreterlangfamily_Type.__name__=_C
_Prtinterpreterlangfamily_Object=MibScalar
prtinterpreterlangfamily=_Prtinterpreterlangfamily_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,2),_Prtinterpreterlangfamily_Type())
prtinterpreterlangfamily.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterlangfamily.setStatus(_A)
class _Prtinterpreterlanglevel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Prtinterpreterlanglevel_Type.__name__=_D
_Prtinterpreterlanglevel_Object=MibScalar
prtinterpreterlanglevel=_Prtinterpreterlanglevel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,3),_Prtinterpreterlanglevel_Type())
prtinterpreterlanglevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterlanglevel.setStatus(_A)
class _Prtinterpreterlangversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Prtinterpreterlangversion_Type.__name__=_D
_Prtinterpreterlangversion_Object=MibScalar
prtinterpreterlangversion=_Prtinterpreterlangversion_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,4),_Prtinterpreterlangversion_Type())
prtinterpreterlangversion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterlangversion.setStatus(_A)
class _Prtinterpreterdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtinterpreterdescription_Type.__name__=_D
_Prtinterpreterdescription_Object=MibScalar
prtinterpreterdescription=_Prtinterpreterdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,5),_Prtinterpreterdescription_Type())
prtinterpreterdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterdescription.setStatus(_A)
class _Prtinterpreterversion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Prtinterpreterversion_Type.__name__=_D
_Prtinterpreterversion_Object=MibScalar
prtinterpreterversion=_Prtinterpreterversion_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,6),_Prtinterpreterversion_Type())
prtinterpreterversion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtinterpreterversion.setStatus(_A)
class _Prtinterpreterdefaultorientation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('ePportrait',3),('ePlandscape',4)))
_Prtinterpreterdefaultorientation_Type.__name__=_C
_Prtinterpreterdefaultorientation_Object=MibScalar
prtinterpreterdefaultorientation=_Prtinterpreterdefaultorientation_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,7),_Prtinterpreterdefaultorientation_Type())
prtinterpreterdefaultorientation.setMaxAccess(_E)
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
class _Prtinterpreterdefaultcharsetin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,8,12,15,2004)));namedValues=NamedValues(*(('ePcsISOLatin2',5),('ePcsISOLatinCyrillic',8),('ePcsISOLatin5',12),('ePcsHalfWidthKatakana',15),(_g,2004)))
_Prtinterpreterdefaultcharsetin_Type.__name__=_C
_Prtinterpreterdefaultcharsetin_Object=MibScalar
prtinterpreterdefaultcharsetin=_Prtinterpreterdefaultcharsetin_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,15,1,1,10),_Prtinterpreterdefaultcharsetin_Type())
prtinterpreterdefaultcharsetin.setMaxAccess(_E)
if mibBuilder.loadTexts:prtinterpreterdefaultcharsetin.setStatus(_A)
class _Prtinterpreterdefaultcharsetout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,2004,2005)));namedValues=NamedValues(*(('ePcsNoDefault',2),('ePcsASCII',3),(_g,2004),('ePcsAdobeStandardEncoding',2005)))
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
_Prtconsoledisplaybuffertext_Type.__name__=_D
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
class _Prtconsolecolor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,1),(_O,2),('ePwhite',3),('ePred',4),('ePgreen',5),('ePblue',6),('ePcyan',7),('ePmagenta',8),('ePyellow',9),('ePorange',10)))
_Prtconsolecolor_Type.__name__=_C
_Prtconsolecolor_Object=MibScalar
prtconsolecolor=_Prtconsolecolor_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,17,6,1,4),_Prtconsolecolor_Type())
prtconsolecolor.setMaxAccess(_B)
if mibBuilder.loadTexts:prtconsolecolor.setStatus(_A)
class _Prtconsoledescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtconsoledescription_Type.__name__=_D
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
class _Prtalertseveritylevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_H,1),('ePcriticalBinaryChangeEvent',3),('ePwarningUnaryChangeEvent',4),('ePwarningBinaryChangeEvent',5)))
_Prtalertseveritylevel_Type.__name__=_C
_Prtalertseveritylevel_Object=MibScalar
prtalertseveritylevel=_Prtalertseveritylevel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,2),_Prtalertseveritylevel_Type())
prtalertseveritylevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertseveritylevel.setStatus(_A)
class _Prtalerttraininglevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6)));namedValues=NamedValues(*((_H,1),('ePuntrained',3),('ePtrained',4),('ePfieldService',5),('ePmanagement',6)))
_Prtalerttraininglevel_Type.__name__=_C
_Prtalerttraininglevel_Object=MibScalar
prtalerttraininglevel=_Prtalerttraininglevel_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,3),_Prtalerttraininglevel_Type())
prtalerttraininglevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalerttraininglevel.setStatus(_A)
class _Prtalertgroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_H,1),('ePhostResourcesMIBStorageTable',3),('ePhostResourcesMIBDeviceTable',4),('ePgeneralPrinter',5),('ePcover',6),('ePlocalization',7),('ePinput',8),('ePoutput',9),('ePmarker',10),('ePmarkerSupplies',11),('ePmarkerColorant',12),('ePmediaPath',13),('ePchannel',14),('ePinterpreter',15),('ePconsoleDisplayBuffer',16),('ePconsoleLights',17)))
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
class _Prtalertcode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,501,502,503,504,505,506,507,801,802,803,804,805,806,807,808,809,810,811,812,813,901,902,903,904,1001,1002,1003,1004,1005,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1301,1302,1303,1501,1502,1503,1504,1505,1506,1507,1509,1801)));namedValues=NamedValues(*((_H,1),(_O,2),('ePinterlockOpened',5),('ePinterlockClosed',6),('ePconfigurationChanged',7),('ePjammed',8),('ePsubunitMissing',9),('ePsubunitLifeAlmostOver',10),('ePsubunitLifeOver',11),('ePsubunitAlmostEmpty',12),('ePsubunitEmpty',13),('ePsubunitAlmostFull',14),('ePsubunitFull',15),('ePsubunitNearLimit',16),('ePsubunitAtLimit',17),('ePsubunitOpened',18),('ePsubunitClosed',19),('ePsubunitTurnedOn',20),('ePsubunitTurnedOff',21),('ePsubunitOffline',22),('ePsubunitPowerSaver',23),('ePsubunitWarmingUp',24),('ePsubunitAdded',25),('ePsubunitRemoved',26),('ePsubunitRecousrceAdded',27),('ePsubunitResourceRemoved',28),('ePsubunitRecoverableFailure',29),('ePsubunitUnrecoverableFailure',30),('ePsubunitRecoverableStorageError',31),('ePsubunitUnrecoverableStorageError',32),('ePsubunitMotorFailure',33),('ePsubunitMemoryExhausted',34),('ePcoverOpened',501),('ePcoverClosed',502),('ePpoweredUp',503),('ePpoweredDown',504),('ePprinterNMSReset',505),('ePprinterManualReset',506),('ePprinterReadyToPrint',507),('ePinputMediaTrayMissing',801),('ePinputMediaSizeChanged',802),('ePinputMediaWeightChanged',803),('ePinputMediaTypeChanged',804),('ePinputMediaColorChanged',805),('ePinputMediaFormPartsChange',806),('ePinputMediaSupplyLow',807),('ePinputMediaSupplyEmpty',808),('ePinputMediaChangeRequest',809),('ePinputManualInputRequest',810),('ePinputTrayPositionFailure',811),('ePinputTrayElevationFailure',812),('ePinputCannotFeedSizeSelected',813),('ePoutputMediaTrayMissing',901),('ePoutputMediaTrayAlmostFull',902),('ePoutputMediaTrayFull',903),('ePoutputMailboxSelectFailure',904),('ePmarkerFuserUnderTemperature',1001),('ePmarkerFuserOverTemperature',1002),('ePmarkerFuserTimingFailure',1003),('ePmarkerFuserThermistorFailure',1004),('ePmarkerAdjustingPrintQuality',1005),('ePmarkerTonerEmpty',1101),('ePmarkerInkEmpty',1102),('ePmarkerPrintRibbonEmpty',1103),('ePmarkerTonerAlmostEmpty',1104),('ePmarkerInkAlmostEmpty',1105),('ePmarkerPrintRibbonAlmostEmpty',1106),('ePmarkerWasteTonerReceptacleAlmostFull',1107),('ePmarkerWasteInkReceptacleAlmostFull',1108),('ePmarkerWasteTonerReceptacleFull',1109),('ePmarkerWasteInkReceptacleFull',1110),('ePmarkerOpcLifeAlmostOver',1111),('ePmarkerOpcLifeOver',1112),('ePmarkerDeveloperAlmostEmpty',1113),('ePmarkerDeveloperEmpty',1114),('ePmarkerTonerCartridgeMissing',1115),('ePmediaPathMediaTrayMissing',1301),('ePmediaPathMediaTrayAlmostFull',1302),('ePmediaPathMediaTrayFull',1303),('ePinterpreterMemoryIncreased',1501),('ePinterpreterMemoryDecreased',1502),('ePinterpreterCartridgeAdded',1503),('ePinterpreterCartridgeDeleted',1504),('ePinterpreterResourceAdded',1505),('ePinterpreterResourceDeleted',1506),('ePinterpreterResourceUnavailable',1507),('ePinterpreterComplexPageEncountered',1509),('ePalertRemovalOfBinaryChangeEntry',1801)))
_Prtalertcode_Type.__name__=_C
_Prtalertcode_Object=MibScalar
prtalertcode=_Prtalertcode_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,7),_Prtalertcode_Type())
prtalertcode.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertcode.setStatus(_A)
class _Prtalertdescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Prtalertdescription_Type.__name__=_D
_Prtalertdescription_Object=MibScalar
prtalertdescription=_Prtalertdescription_Object((1,3,6,1,4,1,11,2,3,9,4,2,2,18,1,1,8),_Prtalertdescription_Type())
prtalertdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtalertdescription.setStatus(_A)
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
_Hrdevicedescr_Type.__name__=_D
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
class _Hrprinterstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5)));namedValues=NamedValues(*((_x,1),('eHidle',3),('eHprinting',4),('eHwarmup',5)))
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
_HrDiskStorageTable_ObjectIdentity=ObjectIdentity
hrDiskStorageTable=_HrDiskStorageTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,6))
_HrDiskStorageEntry_ObjectIdentity=ObjectIdentity
hrDiskStorageEntry=_HrDiskStorageEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,6,1))
class _Hrdiskstorageaccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_y,1),(_z,2)))
_Hrdiskstorageaccess_Type.__name__=_C
_Hrdiskstorageaccess_Object=MibScalar
hrdiskstorageaccess=_Hrdiskstorageaccess_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,6,1,1),_Hrdiskstorageaccess_Type())
hrdiskstorageaccess.setMaxAccess(_E)
if mibBuilder.loadTexts:hrdiskstorageaccess.setStatus(_F)
class _Hrdiskstoragemedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_x,1),('eHhardDisk',3)))
_Hrdiskstoragemedia_Type.__name__=_C
_Hrdiskstoragemedia_Object=MibScalar
hrdiskstoragemedia=_Hrdiskstoragemedia_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,6,1,2),_Hrdiskstoragemedia_Type())
hrdiskstoragemedia.setMaxAccess(_B)
if mibBuilder.loadTexts:hrdiskstoragemedia.setStatus(_F)
class _Hrdiskstorageremoveble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('eHfalse',2))
_Hrdiskstorageremoveble_Type.__name__=_C
_Hrdiskstorageremoveble_Object=MibScalar
hrdiskstorageremoveble=_Hrdiskstorageremoveble_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,6,1,3),_Hrdiskstorageremoveble_Type())
hrdiskstorageremoveble.setMaxAccess(_B)
if mibBuilder.loadTexts:hrdiskstorageremoveble.setStatus(_F)
_Hrdiskstoragecapacity_Type=Integer32
_Hrdiskstoragecapacity_Object=MibScalar
hrdiskstoragecapacity=_Hrdiskstoragecapacity_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,6,1,4),_Hrdiskstoragecapacity_Type())
hrdiskstoragecapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:hrdiskstoragecapacity.setStatus(_F)
_HrPartitionTable_ObjectIdentity=ObjectIdentity
hrPartitionTable=_HrPartitionTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,7))
_HrPartitionEntry_ObjectIdentity=ObjectIdentity
hrPartitionEntry=_HrPartitionEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,7,1))
class _Hrpartitionindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hrpartitionindex_Type.__name__=_C
_Hrpartitionindex_Object=MibScalar
hrpartitionindex=_Hrpartitionindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,7,1,1),_Hrpartitionindex_Type())
hrpartitionindex.setMaxAccess(_B)
if mibBuilder.loadTexts:hrpartitionindex.setStatus(_F)
class _Hrpartitionlabel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hrpartitionlabel_Type.__name__=_D
_Hrpartitionlabel_Object=MibScalar
hrpartitionlabel=_Hrpartitionlabel_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,7,1,2),_Hrpartitionlabel_Type())
hrpartitionlabel.setMaxAccess(_B)
if mibBuilder.loadTexts:hrpartitionlabel.setStatus(_F)
_Hrpartitionid_Type=OctetString
_Hrpartitionid_Object=MibScalar
hrpartitionid=_Hrpartitionid_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,7,1,3),_Hrpartitionid_Type())
hrpartitionid.setMaxAccess(_B)
if mibBuilder.loadTexts:hrpartitionid.setStatus(_F)
_Hrpartitionsize_Type=Integer32
_Hrpartitionsize_Object=MibScalar
hrpartitionsize=_Hrpartitionsize_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,7,1,4),_Hrpartitionsize_Type())
hrpartitionsize.setMaxAccess(_B)
if mibBuilder.loadTexts:hrpartitionsize.setStatus(_F)
class _Hrpartitionfsindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hrpartitionfsindex_Type.__name__=_C
_Hrpartitionfsindex_Object=MibScalar
hrpartitionfsindex=_Hrpartitionfsindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,7,1,5),_Hrpartitionfsindex_Type())
hrpartitionfsindex.setMaxAccess(_B)
if mibBuilder.loadTexts:hrpartitionfsindex.setStatus(_F)
_HrFSTable_ObjectIdentity=ObjectIdentity
hrFSTable=_HrFSTable_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8))
_HrFSEntry_ObjectIdentity=ObjectIdentity
hrFSEntry=_HrFSEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1))
class _Hrfsindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hrfsindex_Type.__name__=_C
_Hrfsindex_Object=MibScalar
hrfsindex=_Hrfsindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1,1),_Hrfsindex_Type())
hrfsindex.setMaxAccess(_B)
if mibBuilder.loadTexts:hrfsindex.setStatus(_F)
_Hrfsmountpoint_Type=OctetString
_Hrfsmountpoint_Object=MibScalar
hrfsmountpoint=_Hrfsmountpoint_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1,2),_Hrfsmountpoint_Type())
hrfsmountpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:hrfsmountpoint.setStatus(_F)
_Hrfsremotemountpoint_Type=OctetString
_Hrfsremotemountpoint_Object=MibScalar
hrfsremotemountpoint=_Hrfsremotemountpoint_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1,3),_Hrfsremotemountpoint_Type())
hrfsremotemountpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:hrfsremotemountpoint.setStatus(_F)
_Hrfstype_Type=ObjectIdentifier
_Hrfstype_Object=MibScalar
hrfstype=_Hrfstype_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1,4),_Hrfstype_Type())
hrfstype.setMaxAccess(_B)
if mibBuilder.loadTexts:hrfstype.setStatus(_F)
class _Hrfsaccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_y,1),(_z,2)))
_Hrfsaccess_Type.__name__=_C
_Hrfsaccess_Object=MibScalar
hrfsaccess=_Hrfsaccess_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1,5),_Hrfsaccess_Type())
hrfsaccess.setMaxAccess(_E)
if mibBuilder.loadTexts:hrfsaccess.setStatus(_F)
class _Hrfsbootable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('eHfalse',2))
_Hrfsbootable_Type.__name__=_C
_Hrfsbootable_Object=MibScalar
hrfsbootable=_Hrfsbootable_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1,6),_Hrfsbootable_Type())
hrfsbootable.setMaxAccess(_B)
if mibBuilder.loadTexts:hrfsbootable.setStatus(_F)
class _Hrfsstorageindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hrfsstorageindex_Type.__name__=_C
_Hrfsstorageindex_Object=MibScalar
hrfsstorageindex=_Hrfsstorageindex_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1,7),_Hrfsstorageindex_Type())
hrfsstorageindex.setMaxAccess(_B)
if mibBuilder.loadTexts:hrfsstorageindex.setStatus(_F)
_Hrfslastfullbackupdate_Type=OctetString
_Hrfslastfullbackupdate_Object=MibScalar
hrfslastfullbackupdate=_Hrfslastfullbackupdate_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1,8),_Hrfslastfullbackupdate_Type())
hrfslastfullbackupdate.setMaxAccess(_B)
if mibBuilder.loadTexts:hrfslastfullbackupdate.setStatus(_F)
_Hrfslastpartialbackupdate_Type=OctetString
_Hrfslastpartialbackupdate_Object=MibScalar
hrfslastpartialbackupdate=_Hrfslastpartialbackupdate_Object((1,3,6,1,4,1,11,2,3,9,4,2,3,3,8,1,9),_Hrfslastpartialbackupdate_Type())
hrfslastpartialbackupdate.setMaxAccess(_B)
if mibBuilder.loadTexts:hrfslastpartialbackupdate.setStatus(_F)
mibBuilder.exportSymbols('CLJ8550-MIB',**{_R:DisplayString,'hp':hp,'dm':dm,'device':device,'system':system,'settings-system':settings_system,'energy-star':energy_star,'sleep-mode':sleep_mode,'status-system':status_system,'on-off-line':on_off_line,'continue':_pysmi_continue,'auto-continue':auto_continue,'job-input-auto-continue-timeout':job_input_auto_continue_timeout,'job-input-auto-continue-mode':job_input_auto_continue_mode,'background-message':background_message,'background-message1':background_message1,'background-status-msg-line1-part1':background_status_msg_line1_part1,'background-message2':background_message2,'background-status-msg-line2-part1':background_status_msg_line2_part1,'error-log-clear':error_log_clear,'job-output-auto-continue-timeout':job_output_auto_continue_timeout,'collated-originals-support':collated_originals_support,'localization-languages-supported':localization_languages_supported,'localization-countries-supported':localization_countries_supported,'id':id,'model-number':model_number,'model-name':model_name,'serial-number':serial_number,'device-name':device_name,'device-location':device_location,'asset-number':asset_number,'interface':interface,'simm':simm,'simm1':simm1,'simm1-type':simm1_type,'simm1-capacity':simm1_capacity,'simm2':simm2,'simm2-type':simm2_type,'simm2-capacity':simm2_capacity,'simm3':simm3,'simm3-type':simm3_type,'simm3-capacity':simm3_capacity,'simm4':simm4,'simm4-type':simm4_type,'simm4-capacity':simm4_capacity,'simm5':simm5,'simm5-type':simm5_type,'simm5-capacity':simm5_capacity,'simm6':simm6,'simm6-type':simm6_type,'simm6-capacity':simm6_capacity,'simm7':simm7,'simm7-type':simm7_type,'simm7-capacity':simm7_capacity,'simm8':simm8,'simm8-type':simm8_type,'simm8-capacity':simm8_capacity,'mio':mio,'mio1':mio1,'mio1-model-name':mio1_model_name,'mio1-manufacturing-info':mio1_manufacturing_info,'mio1-type':mio1_type,'mio2':mio2,'mio2-model-name':mio2_model_name,'mio2-manufacturing-info':mio2_manufacturing_info,'mio2-type':mio2_type,'phd':phd,'phd1':phd1,'phd1-type':phd1_type,'phd2':phd2,'phd2-model':phd2_model,'phd2-manufacturing-info':phd2_manufacturing_info,'phd2-type':phd2_type,'phd2-capacity':phd2_capacity,'phd3':phd3,'phd3-model':phd3_model,'phd3-manufacturing-info':phd3_manufacturing_info,'phd3-type':phd3_type,'phd3-capacity':phd3_capacity,'phd4':phd4,'phd4-type':phd4_type,'phd5':phd5,'phd5-type':phd5_type,'phd6':phd6,'phd6-type':phd6_type,'test':test,'self-test':self_test,'print-internal-page':print_internal_page,'job':job,'settings-job':settings_job,'cancel-job':cancel_job,'job-info-change-id':job_info_change_id,'hold-job-timeout':hold_job_timeout,'active-print-jobs':active_print_jobs,'job-being-parsed':job_being_parsed,'current-job-parsing-id':current_job_parsing_id,'job-info':job_info,'job-info-name1':job_info_name1,'job-info-name2':job_info_name2,'job-info-stage':job_info_stage,'job-info-io-source':job_info_io_source,'job-info-pages-processed':job_info_pages_processed,'job-info-pages-printed':job_info_pages_printed,'job-info-size':job_info_size,'job-info-state':job_info_state,'job-info-outcome':job_info_outcome,'job-info-outbins-used':job_info_outbins_used,'job-info-physical-outbins-used':job_info_physical_outbins_used,'job-info-attribute':job_info_attribute,'job-info-attr-1':job_info_attr_1,'job-info-attr-2':job_info_attr_2,'job-info-attr-3':job_info_attr_3,'job-info-attr-4':job_info_attr_4,'job-info-attr-5':job_info_attr_5,'job-info-attr-6':job_info_attr_6,'job-info-attr-7':job_info_attr_7,'job-info-attr-8':job_info_attr_8,'job-info-attr-9':job_info_attr_9,'job-info-attr-10':job_info_attr_10,'job-info-attr-11':job_info_attr_11,'job-info-attr-12':job_info_attr_12,'job-info-attr-13':job_info_attr_13,'job-info-attr-14':job_info_attr_14,'job-info-attr-15':job_info_attr_15,'job-info-attr-16':job_info_attr_16,'job-info-attr-17':job_info_attr_17,'job-info-attr-18':job_info_attr_18,'job-info-attr-19':job_info_attr_19,'job-info-attr-20':job_info_attr_20,'job-info-attr-21':job_info_attr_21,'job-info-attr-22':job_info_attr_22,'job-info-attr-23':job_info_attr_23,'job-info-attr-24':job_info_attr_24,'job-info-attr-25':job_info_attr_25,'job-info-attr-26':job_info_attr_26,'job-info-attr-27':job_info_attr_27,'job-info-attr-28':job_info_attr_28,'job-info-attr-29':job_info_attr_29,'job-info-attr-30':job_info_attr_30,'job-info-attr-31':job_info_attr_31,'job-info-attr-32':job_info_attr_32,'job-info-requested-originals':job_info_requested_originals,'job-info-page-count-current-original':job_info_page_count_current_original,'job-info-pages-in-original':job_info_pages_in_original,'job-info-printed-originals':job_info_printed_originals,'held-job':held_job,'held-job-info':held_job_info,'held-job-user-name':held_job_user_name,'held-job-job-name':held_job_job_name,'held-job-retention':held_job_retention,'held-job-security':held_job_security,'held-job-quantity':held_job_quantity,'held-job-pin':held_job_pin,'held-job-control':held_job_control,'held-job-print':held_job_print,'held-job-delete':held_job_delete,'held-job-set-queue-size':held_job_set_queue_size,'held-job-enable':held_job_enable,'file-system':file_system,'settings-file-system':settings_file_system,'file-system-memory':file_system_memory,'file-system-max-open-files':file_system_max_open_files,'status-file-system':status_file_system,'file-system-statistic-read-open':file_system_statistic_read_open,'file-system-statistic-write-open':file_system_statistic_write_open,'file-system-statistic-successful':file_system_statistic_successful,'file-system-statistic-unsuccessful':file_system_statistic_unsuccessful,'file-system-statistic-current-memory-usage':file_system_statistic_current_memory_usage,'file-system-statistic-max-memory-usage':file_system_statistic_max_memory_usage,'file-systems':file_systems,'file-system2':file_system2,'file-system2-initialize-volume':file_system2_initialize_volume,'errorlog':errorlog,'error1':error1,'error1-time-stamp':error1_time_stamp,'error1-code':error1_code,'error2':error2,'error2-time-stamp':error2_time_stamp,'error2-code':error2_code,'error3':error3,'error3-time-stamp':error3_time_stamp,'error3-code':error3_code,'error4':error4,'error4-time-stamp':error4_time_stamp,'error4-code':error4_code,'error5':error5,'error5-time-stamp':error5_time_stamp,'error5-code':error5_code,'error6':error6,'error6-time-stamp':error6_time_stamp,'error6-code':error6_code,'error7':error7,'error7-time-stamp':error7_time_stamp,'error7-code':error7_code,'error8':error8,'error8-time-stamp':error8_time_stamp,'error8-code':error8_code,'error9':error9,'error9-time-stamp':error9_time_stamp,'error9-code':error9_code,'error10':error10,'error10-time-stamp':error10_time_stamp,'error10-code':error10_code,'error11':error11,'error11-time-stamp':error11_time_stamp,'error11-code':error11_code,'error12':error12,'error12-time-stamp':error12_time_stamp,'error12-code':error12_code,'error13':error13,'error13-time-stamp':error13_time_stamp,'error13-code':error13_code,'error14':error14,'error14-time-stamp':error14_time_stamp,'error14-code':error14_code,'error15':error15,'error15-time-stamp':error15_time_stamp,'error15-code':error15_code,'error16':error16,'error16-time-stamp':error16_time_stamp,'error16-code':error16_code,'error17':error17,'error17-time-stamp':error17_time_stamp,'error17-code':error17_code,'error18':error18,'error18-time-stamp':error18_time_stamp,'error18-code':error18_code,'error19':error19,'error19-time-stamp':error19_time_stamp,'error19-code':error19_code,'error20':error20,'error20-time-stamp':error20_time_stamp,'error20-code':error20_code,'error21':error21,'error21-time-stamp':error21_time_stamp,'error21-code':error21_code,'error22':error22,'error22-time-stamp':error22_time_stamp,'error22-code':error22_code,'error23':error23,'error23-time-stamp':error23_time_stamp,'error23-code':error23_code,'error24':error24,'error24-time-stamp':error24_time_stamp,'error24-code':error24_code,'error25':error25,'error25-time-stamp':error25_time_stamp,'error25-code':error25_code,'error26':error26,'error26-time-stamp':error26_time_stamp,'error26-code':error26_code,'error27':error27,'error27-time-stamp':error27_time_stamp,'error27-code':error27_code,'error28':error28,'error28-time-stamp':error28_time_stamp,'error28-code':error28_code,'error29':error29,'error29-time-stamp':error29_time_stamp,'error29-code':error29_code,'error30':error30,'error30-time-stamp':error30_time_stamp,'error30-code':error30_code,'error31':error31,'error31-time-stamp':error31_time_stamp,'error31-code':error31_code,'error32':error32,'error32-time-stamp':error32_time_stamp,'error32-code':error32_code,'error33':error33,'error33-time-stamp':error33_time_stamp,'error33-code':error33_code,'error34':error34,'error34-time-stamp':error34_time_stamp,'error34-code':error34_code,'error35':error35,'error35-time-stamp':error35_time_stamp,'error35-code':error35_code,'error36':error36,'error36-time-stamp':error36_time_stamp,'error36-code':error36_code,'error37':error37,'error37-time-stamp':error37_time_stamp,'error37-code':error37_code,'error38':error38,'error38-time-stamp':error38_time_stamp,'error38-code':error38_code,'error39':error39,'error39-time-stamp':error39_time_stamp,'error39-code':error39_code,'error40':error40,'error40-time-stamp':error40_time_stamp,'error40-code':error40_code,'error41':error41,'error41-time-stamp':error41_time_stamp,'error41-code':error41_code,'error42':error42,'error42-time-stamp':error42_time_stamp,'error42-code':error42_code,'error43':error43,'error43-time-stamp':error43_time_stamp,'error43-code':error43_code,'error44':error44,'error44-time-stamp':error44_time_stamp,'error44-code':error44_code,'error45':error45,'error45-time-stamp':error45_time_stamp,'error45-code':error45_code,'error46':error46,'error46-time-stamp':error46_time_stamp,'error46-code':error46_code,'error47':error47,'error47-time-stamp':error47_time_stamp,'error47-code':error47_code,'error48':error48,'error48-time-stamp':error48_time_stamp,'error48-code':error48_code,'error49':error49,'error49-time-stamp':error49_time_stamp,'error49-code':error49_code,'error50':error50,'error50-time-stamp':error50_time_stamp,'error50-code':error50_code,'resource-manager':resource_manager,'mass-storage-resources':mass_storage_resources,'mass-storage-resource-change-counter':mass_storage_resource_change_counter,'mass-storage-resource-changed':mass_storage_resource_changed,'remote-procedure-call':remote_procedure_call,'settings-rpc':settings_rpc,'rpc-test-return-code':rpc_test_return_code,'rpc-bind-protocol-address':rpc_bind_protocol_address,'status-rpc':status_rpc,'rpc-statistic-successful':rpc_statistic_successful,'rpc-statistic-unsuccessful':rpc_statistic_unsuccessful,'rpc-bound-protocol-address':rpc_bound_protocol_address,'rpc-services':rpc_services,'nfs-server':nfs_server,'settings-nfs-server':settings_nfs_server,'nfs-server-memory':nfs_server_memory,'nfs-server-read-size':nfs_server_read_size,'nfs-server-write-size':nfs_server_write_size,'nfs-server-test-return-code':nfs_server_test_return_code,'status-nfs-server':status_nfs_server,'nfs-server-statistic-successful':nfs_server_statistic_successful,'nfs-server-statistic-unsuccessful':nfs_server_statistic_unsuccessful,'nfs-server-statistic-current-memory-usage':nfs_server_statistic_current_memory_usage,'nfs-server-statistic-max-memory-usage':nfs_server_statistic_max_memory_usage,'rpc-bind':rpc_bind,'settings-rpc-bind':settings_rpc_bind,'rpc-bind-test-return-code':rpc_bind_test_return_code,'status-rpc-bind':status_rpc_bind,'rpc-bind-statistic-successful':rpc_bind_statistic_successful,'rpc-bind-statistic-unsuccessful':rpc_bind_statistic_unsuccessful,'xport-interface':xport_interface,'status-xip':status_xip,'xip-statistic-processed':xip_statistic_processed,'xip-statistic-data-in-dropped':xip_statistic_data_in_dropped,'source-subsystem':source_subsystem,'io':io,'settings-io':settings_io,'io-timeout':io_timeout,'io-switch':io_switch,'io-buffering':io_buffering,'io-buffer-size':io_buffer_size,'maximum-io-buffering-memory':maximum_io_buffering_memory,'ports':ports,'port1':port1,'port1-parallel-speed':port1_parallel_speed,'port1-parallel-bidirectionality':port1_parallel_bidirectionality,'processing-subsystem':processing_subsystem,'pdl':pdl,'settings-pdl':settings_pdl,'default-copies':default_copies,'resource-saving':resource_saving,'maximum-resource-saving-memory':maximum_resource_saving_memory,'default-vertical-black-resolution':default_vertical_black_resolution,'default-horizontal-black-resolution':default_horizontal_black_resolution,'default-page-protect':default_page_protect,'default-lines-per-page':default_lines_per_page,'default-vmi':default_vmi,'default-media-size':default_media_size,'cold-reset-media-size':cold_reset_media_size,'default-media-name':default_media_name,'status-pdl':status_pdl,'form-feed-needed':form_feed_needed,'pdl-pcl':pdl_pcl,'pcl-resource-saving-memory-size':pcl_resource_saving_memory_size,'pcl-total-page-count':pcl_total_page_count,'pcl-default-font-height':pcl_default_font_height,'pcl-default-font-source':pcl_default_font_source,'pcl-default-font-number':pcl_default_font_number,'pcl-default-font-width':pcl_default_font_width,'pdl-postscript':pdl_postscript,'postscript-resource-saving-memory-size':postscript_resource_saving_memory_size,'postscript-total-page-count':postscript_total_page_count,'postscript-print-errors':postscript_print_errors,'postscript-jam-recovery':postscript_jam_recovery,'pjl':pjl,'pjl-password':pjl_password,'jetsend-proc-sub':jetsend_proc_sub,'settings-jetsend':settings_jetsend,'jetsend-mode':jetsend_mode,'jetsend-contact':jetsend_contact,'settings-jetsend-contact':settings_jetsend_contact,'jetsend-contact-password':jetsend_contact_password,'jetsend-contact-ip-address-security':jetsend_contact_ip_address_security,'destination-subsystem':destination_subsystem,'print-engine':print_engine,'status-prt-eng':status_prt_eng,'total-color-page-count':total_color_page_count,'duplex-page-count':duplex_page_count,'intray':intray,'settings-intray':settings_intray,'mp-tray':mp_tray,'custom-paper-dim-unit':custom_paper_dim_unit,'custom-paper-feed-dim':custom_paper_feed_dim,'custom-paper-xfeed-dim':custom_paper_xfeed_dim,'intrays':intrays,'intray1':intray1,'tray1-media-size-loaded':tray1_media_size_loaded,'tray1-phd':tray1_phd,'intray2':intray2,'tray2-media-size-loaded':tray2_media_size_loaded,'tray2-phd':tray2_phd,'intray3':intray3,'tray3-media-size-loaded':tray3_media_size_loaded,'tray3-phd':tray3_phd,'intray4':intray4,'tray4-media-size-loaded':tray4_media_size_loaded,'tray4-phd':tray4_phd,'intray5':intray5,'tray5-phd':tray5_phd,'outbin':outbin,'settings-outbin':settings_outbin,'overflow-bin':overflow_bin,'outbins':outbins,'outbin1':outbin1,'outbin1-override-mode':outbin1_override_mode,'outbin2':outbin2,'outbin2-override-mode':outbin2_override_mode,'outbin3':outbin3,'outbin3-override-mode':outbin3_override_mode,'outbin3-phd':outbin3_phd,'outbin4':outbin4,'outbin4-override-mode':outbin4_override_mode,'outbin4-phd':outbin4_phd,'outbin5':outbin5,'outbin5-override-mode':outbin5_override_mode,'outbin5-phd':outbin5_phd,'outbin6':outbin6,'outbin6-override-mode':outbin6_override_mode,'outbin6-phd':outbin6_phd,'outbin7':outbin7,'outbin7-override-mode':outbin7_override_mode,'outbin7-phd':outbin7_phd,'outbin8':outbin8,'outbin8-override-mode':outbin8_override_mode,'outbin8-phd':outbin8_phd,'outbin9':outbin9,'outbin9-override-mode':outbin9_override_mode,'outbin9-phd':outbin9_phd,'outbin10':outbin10,'outbin10-override-mode':outbin10_override_mode,'outbin10-phd':outbin10_phd,'outbin11':outbin11,'outbin11-override-mode':outbin11_override_mode,'outbin11-phd':outbin11_phd,'marking-agent':marking_agent,'settings-marking-agent':settings_marking_agent,'low-marking-agent-processing':low_marking_agent_processing,'imaging':imaging,'default-ret':default_ret,'default-print-quality':default_print_quality,'ph':ph,'ph-devices':ph_devices,'ph2':ph2,'phd2-device-specific-command':phd2_device_specific_command,'phd2-device-memory':phd2_device_memory,'ph3':ph3,'phd3-device-specific-command':phd3_device_specific_command,'phd3-device-memory':phd3_device_memory,'print-media':print_media,'settings-print-media':settings_print_media,'media-names-available':media_names_available,'media-info':media_info,'media1':media1,'media1-name':media1_name,'media1-short-name':media1_short_name,'media1-page-count':media1_page_count,'media2':media2,'media2-name':media2_name,'media2-short-name':media2_short_name,'media2-page-count':media2_page_count,'media3':media3,'media3-name':media3_name,'media3-short-name':media3_short_name,'media3-page-count':media3_page_count,'media4':media4,'media4-name':media4_name,'media4-short-name':media4_short_name,'media4-page-count':media4_page_count,'media5':media5,'media5-name':media5_name,'media5-short-name':media5_short_name,'media5-page-count':media5_page_count,'media6':media6,'media6-name':media6_name,'media6-short-name':media6_short_name,'media6-page-count':media6_page_count,'media7':media7,'media7-name':media7_name,'media7-short-name':media7_short_name,'media7-page-count':media7_page_count,'media8':media8,'media8-name':media8_name,'media8-short-name':media8_short_name,'media8-page-count':media8_page_count,'media9':media9,'media9-name':media9_name,'media9-short-name':media9_short_name,'media9-page-count':media9_page_count,'media10':media10,'media10-name':media10_name,'media10-short-name':media10_short_name,'media10-page-count':media10_page_count,'media11':media11,'media11-name':media11_name,'media11-short-name':media11_short_name,'media11-page-count':media11_page_count,'media12':media12,'media12-name':media12_name,'media12-short-name':media12_short_name,'media12-page-count':media12_page_count,'media13':media13,'media13-name':media13_name,'media13-short-name':media13_short_name,'media13-page-count':media13_page_count,'media14':media14,'media14-name':media14_name,'media14-short-name':media14_short_name,'media14-page-count':media14_page_count,'media15':media15,'media15-name':media15_name,'media15-short-name':media15_short_name,'media15-page-count':media15_page_count,'print-engine-test':print_engine_test,'pe-test-button-press':pe_test_button_press,'channel':channel,'channelnumberofchannels':channelnumberofchannels,'channelprinteralert':channelprinteralert,'channelTable':channelTable,'channelEntry':channelEntry,'channeltype':channeltype,'channelprotocolversion':channelprotocolversion,'channelstate':channelstate,'channelifindex':channelifindex,'channelstatus':channelstatus,'tables':tables,'channel-table':channel_table,'channel-entry':channel_entry,'channel-bytes-sent':channel_bytes_sent,'channel-bytes-received':channel_bytes_received,'channel-io-errors':channel_io_errors,'channel-jobs-received':channel_jobs_received,'channel-mio':channel_mio,'printmib':printmib,'prtGeneral':prtGeneral,'prtGeneralTable':prtGeneralTable,'prtGeneralEntry':prtGeneralEntry,'prtgeneralconfigchanges':prtgeneralconfigchanges,'prtgeneralcurrentlocalization':prtgeneralcurrentlocalization,'prtgeneralreset':prtgeneralreset,'prtgeneralcurrentoperator':prtgeneralcurrentoperator,'prtgeneralserviceperson':prtgeneralserviceperson,'prtinputdefaultindex':prtinputdefaultindex,'prtoutputdefaultindex':prtoutputdefaultindex,'prtmarkerdefaultindex':prtmarkerdefaultindex,'prtmediapathdefaultindex':prtmediapathdefaultindex,'prtconsolelocalization':prtconsolelocalization,'prtconsolenumberofdisplaylines':prtconsolenumberofdisplaylines,'prtconsolenumberofdisplaychars':prtconsolenumberofdisplaychars,'prtconsoledisable':prtconsoledisable,'prtgeneralbannerpage':prtgeneralbannerpage,'prtStorageRefTable':prtStorageRefTable,'prtStorageRefEntry':prtStorageRefEntry,'prtstoragerefindex':prtstoragerefindex,'prtDeviceRefTable':prtDeviceRefTable,'prtDeviceRefEntry':prtDeviceRefEntry,'prtdevicerefindex':prtdevicerefindex,'prtCover':prtCover,'prtCoverTable':prtCoverTable,'prtCoverEntry':prtCoverEntry,'prtcoverdescription':prtcoverdescription,'prtcoverstatus':prtcoverstatus,'prtLocalization':prtLocalization,'prtLocalizationTable':prtLocalizationTable,'prtLocalizationEntry':prtLocalizationEntry,'prtlocalizationlanguage':prtlocalizationlanguage,'prtlocalizationcountry':prtlocalizationcountry,'prtlocalizationcharacterset':prtlocalizationcharacterset,'prtInput':prtInput,'prtInputTable':prtInputTable,'prtInputEntry':prtInputEntry,'prtinputtype':prtinputtype,'prtinputdimunit':prtinputdimunit,'prtinputmediadimfeeddirdeclared':prtinputmediadimfeeddirdeclared,'prtinputmediadimxfeeddirdeclared':prtinputmediadimxfeeddirdeclared,'prtinputmediadimfeeddirchosen':prtinputmediadimfeeddirchosen,'prtinputmediadimxfeeddirchosen':prtinputmediadimxfeeddirchosen,'prtinputcapacityunit':prtinputcapacityunit,'prtinputmaxcapacity':prtinputmaxcapacity,'prtinputcurrentlevel':prtinputcurrentlevel,'prtinputstatus':prtinputstatus,'prtinputmedianame':prtinputmedianame,'prtinputname':prtinputname,'prtinputvendorname':prtinputvendorname,'prtinputmodel':prtinputmodel,'prtinputversion':prtinputversion,'prtinputserialnumber':prtinputserialnumber,'prtinputdescription':prtinputdescription,'prtinputsecurity':prtinputsecurity,'prtOutput':prtOutput,'prtOutputTable':prtOutputTable,'prtOutputEntry':prtOutputEntry,'prtoutputtype':prtoutputtype,'prtoutputcapacityunit':prtoutputcapacityunit,'prtoutputmaxcapacity':prtoutputmaxcapacity,'prtoutputremainingcapacity':prtoutputremainingcapacity,'prtoutputstatus':prtoutputstatus,'prtoutputname':prtoutputname,'prtoutputvendorname':prtoutputvendorname,'prtoutputmodel':prtoutputmodel,'prtoutputversion':prtoutputversion,'prtoutputserialnumber':prtoutputserialnumber,'prtoutputdescription':prtoutputdescription,'prtoutputsecurity':prtoutputsecurity,'prtoutputstackingorder':prtoutputstackingorder,'prtoutputpagedeliveryorientation':prtoutputpagedeliveryorientation,'prtoutputbursting':prtoutputbursting,'prtoutputdecollating':prtoutputdecollating,'prtoutputpagecollated':prtoutputpagecollated,'prtoutputoffsetstacking':prtoutputoffsetstacking,'prtMarker':prtMarker,'prtMarkerTable':prtMarkerTable,'prtMarkerEntry':prtMarkerEntry,'prtmarkermarktech':prtmarkermarktech,'prtmarkercounterunit':prtmarkercounterunit,'prtmarkerlifecount':prtmarkerlifecount,'prtmarkerpoweroncount':prtmarkerpoweroncount,'prtmarkerprocesscolorants':prtmarkerprocesscolorants,'prtmarkerspotcolorants':prtmarkerspotcolorants,'prtmarkeraddressabilityunit':prtmarkeraddressabilityunit,'prtmarkeraddressabilityfeeddir':prtmarkeraddressabilityfeeddir,'prtmarkeraddressabilityxfeeddir':prtmarkeraddressabilityxfeeddir,'prtmarkernorthmargin':prtmarkernorthmargin,'prtmarkersouthmargin':prtmarkersouthmargin,'prtmarkerwestmargin':prtmarkerwestmargin,'prtmarkereastmargin':prtmarkereastmargin,'prtmarkerstatus':prtmarkerstatus,'prtMarkerSupplies':prtMarkerSupplies,'prtMarkerSuppliesTable':prtMarkerSuppliesTable,'prtMarkerSuppliesEntry':prtMarkerSuppliesEntry,'prtmarkersuppliesmarkerindex':prtmarkersuppliesmarkerindex,'prtmarkersuppliescolorantindex':prtmarkersuppliescolorantindex,'prtmarkersuppliesclass':prtmarkersuppliesclass,'prtmarkersuppliestype':prtmarkersuppliestype,'prtmarkersuppliesdescription':prtmarkersuppliesdescription,'prtmarkersuppliessupplyunit':prtmarkersuppliessupplyunit,'prtmarkersuppliesmaxcapacity':prtmarkersuppliesmaxcapacity,'prtmarkersupplieslevel':prtmarkersupplieslevel,'prtMediaPath':prtMediaPath,'prtMediaPathTable':prtMediaPathTable,'prtMediaPathEntry':prtMediaPathEntry,'prtmediapathmaxspeedprintunit':prtmediapathmaxspeedprintunit,'prtmediapathmediasizeunit':prtmediapathmediasizeunit,'prtmediapathmaxspeed':prtmediapathmaxspeed,'prtmediapathmaxmediafeeddir':prtmediapathmaxmediafeeddir,'prtmediapathmaxmediaxfeeddir':prtmediapathmaxmediaxfeeddir,'prtmediapathminmediafeeddir':prtmediapathminmediafeeddir,'prtmediapathminmediaxfeeddir':prtmediapathminmediaxfeeddir,'prtmediapathtype':prtmediapathtype,'prtmediapathdescription':prtmediapathdescription,'prtmediapathstatus':prtmediapathstatus,'prtChannel':prtChannel,'prtChannelTable':prtChannelTable,'prtChannelEntry':prtChannelEntry,'prtchanneltype':prtchanneltype,'prtchannelprotocolversion':prtchannelprotocolversion,'prtchannelcurrentjobcntllangindex':prtchannelcurrentjobcntllangindex,'prtchanneldefaultpagedesclangindex':prtchanneldefaultpagedesclangindex,'prtchannelstate':prtchannelstate,'prtchannelifindex':prtchannelifindex,'prtchannelstatus':prtchannelstatus,'prtInterpreter':prtInterpreter,'prtInterpreterTable':prtInterpreterTable,'prtInterpreterEntry':prtInterpreterEntry,'prtinterpreterlangfamily':prtinterpreterlangfamily,'prtinterpreterlanglevel':prtinterpreterlanglevel,'prtinterpreterlangversion':prtinterpreterlangversion,'prtinterpreterdescription':prtinterpreterdescription,'prtinterpreterversion':prtinterpreterversion,'prtinterpreterdefaultorientation':prtinterpreterdefaultorientation,'prtinterpreterfeedaddressability':prtinterpreterfeedaddressability,'prtinterpreterxfeedaddressability':prtinterpreterxfeedaddressability,'prtinterpreterdefaultcharsetin':prtinterpreterdefaultcharsetin,'prtinterpreterdefaultcharsetout':prtinterpreterdefaultcharsetout,'prtinterpretertwoway':prtinterpretertwoway,'prtConsoleDisplayBuffer':prtConsoleDisplayBuffer,'prtConsoleDisplayBufferTable':prtConsoleDisplayBufferTable,'prtConsoleDisplayBufferEntry':prtConsoleDisplayBufferEntry,'prtconsoledisplaybuffertext':prtconsoledisplaybuffertext,'prtConsoleLights':prtConsoleLights,'prtConsoleLightTable':prtConsoleLightTable,'prtConsoleLightEntry':prtConsoleLightEntry,'prtconsoleontime':prtconsoleontime,'prtconsoleofftime':prtconsoleofftime,'prtconsolecolor':prtconsolecolor,'prtconsoledescription':prtconsoledescription,'prtAlert':prtAlert,'prtAlertTable':prtAlertTable,'prtAlertEntry':prtAlertEntry,'prtalertseveritylevel':prtalertseveritylevel,'prtalerttraininglevel':prtalerttraininglevel,'prtalertgroup':prtalertgroup,'prtalertgroupindex':prtalertgroupindex,'prtalertlocation':prtalertlocation,'prtalertcode':prtalertcode,'prtalertdescription':prtalertdescription,'hrm':hrm,'hrStorage':hrStorage,'hrmemorysize':hrmemorysize,'hrStorageTable':hrStorageTable,'hrStorageEntry':hrStorageEntry,'hrstorageindex':hrstorageindex,'hrstoragetype':hrstoragetype,'hrstoragedescr':hrstoragedescr,'hrstorageallocationunits':hrstorageallocationunits,'hrstoragesize':hrstoragesize,'hrstorageused':hrstorageused,'hrstorageallocationfailures':hrstorageallocationfailures,'hrDevice':hrDevice,'hrDeviceTable':hrDeviceTable,'hrDeviceEntry':hrDeviceEntry,'hrdeviceindex':hrdeviceindex,'hrdevicetype':hrdevicetype,'hrdevicedescr':hrdevicedescr,'hrdeviceid':hrdeviceid,'hrdevicestatus':hrdevicestatus,'hrdeviceerrors':hrdeviceerrors,'hrPrinterTable':hrPrinterTable,'hrPrinterEntry':hrPrinterEntry,'hrprinterstatus':hrprinterstatus,'hrprinterdetectederrorstate':hrprinterdetectederrorstate,'hrDiskStorageTable':hrDiskStorageTable,'hrDiskStorageEntry':hrDiskStorageEntry,'hrdiskstorageaccess':hrdiskstorageaccess,'hrdiskstoragemedia':hrdiskstoragemedia,'hrdiskstorageremoveble':hrdiskstorageremoveble,'hrdiskstoragecapacity':hrdiskstoragecapacity,'hrPartitionTable':hrPartitionTable,'hrPartitionEntry':hrPartitionEntry,'hrpartitionindex':hrpartitionindex,'hrpartitionlabel':hrpartitionlabel,'hrpartitionid':hrpartitionid,'hrpartitionsize':hrpartitionsize,'hrpartitionfsindex':hrpartitionfsindex,'hrFSTable':hrFSTable,'hrFSEntry':hrFSEntry,'hrfsindex':hrfsindex,'hrfsmountpoint':hrfsmountpoint,'hrfsremotemountpoint':hrfsremotemountpoint,'hrfstype':hrfstype,'hrfsaccess':hrfsaccess,'hrfsbootable':hrfsbootable,'hrfsstorageindex':hrfsstorageindex,'hrfslastfullbackupdate':hrfslastfullbackupdate,'hrfslastpartialbackupdate':hrfslastpartialbackupdate})