_u='trap_u_batterie_higher_warning_removed'
_t='trap_u_batterie_lower_warning_removed'
_s='trap_uout_low_removed'
_r='trap_fan_error_removed'
_q='trap_dc_voltage_high_added_removed'
_p='trap_dc_voltage_low_removed'
_o='trap_sts_current_need_redandancy_removed'
_n='trap_inverter_overload_removed'
_m='trap_sts_overload_removed'
_l='trap_sts_overtemperature_removed'
_k='trap_critical_inverter_quantity_removed'
_j='trap_no_redundant_inverter_removed'
_i='trap_inverter_failure_removed'
_h='trap_syncronisation_error_removed'
_g='trap_source_inverter_failure_removed'
_f='trap_source_mains_failure_removed'
_e='trap_u_batterie_higher_warning_present'
_d='trap_u_batterie_lower_warning_present'
_c='trap_uout_low_present'
_b='trap_fan_error_present'
_a='trap_dc_voltage_high_present'
_Z='trap_dc_voltage_low_present'
_Y='trap_sts_current_need_redandancy_present'
_X='trap_inverter_overload_present'
_W='trap_sts_overload_present'
_V='trap_sts_overtemperature_present'
_U='trap_critical_inverter_quantity_present'
_T='trap_no_redundant_inverter_present'
_S='trap_inverter_failure_present'
_R='trap_syncronisation_error_present'
_Q='trap_source_inverter_failure_present'
_P='trap_source_mains_failue_present'
_O='histIndex'
_N='current'
_M='optional'
_L='inv_Index'
_K='NotificationType'
_J='DisplayString'
_I='trapSourceIPTest'
_H='trapLastMessageNbrTest'
_G='trapLastMessageStringTest'
_F='not-accessible'
_E='read-only'
_D='read-write'
_C='STS_SEQUENZ-MIB'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
sts_system=ModuleIdentity((1,3,6,1,4,1,16460,4))
_Convertronic_ObjectIdentity=ObjectIdentity
convertronic=_Convertronic_ObjectIdentity((1,3,6,1,4,1,16460))
_MeasureValues_ObjectIdentity=ObjectIdentity
measureValues=_MeasureValues_ObjectIdentity((1,3,6,1,4,1,16460,4,1))
_Sts_measureValues_ObjectIdentity=ObjectIdentity
sts_measureValues=_Sts_measureValues_ObjectIdentity((1,3,6,1,4,1,16460,4,1,1))
class _SVal_UN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_UN_Type.__name__=_B
_SVal_UN_Object=MibScalar
sVal_UN=_SVal_UN_Object((1,3,6,1,4,1,16460,4,1,1,1),_SVal_UN_Type())
sVal_UN.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_UN.setStatus(_A)
class _SVal_FreqNetz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_FreqNetz_Type.__name__=_B
_SVal_FreqNetz_Object=MibScalar
sVal_FreqNetz=_SVal_FreqNetz_Object((1,3,6,1,4,1,16460,4,1,1,2),_SVal_FreqNetz_Type())
sVal_FreqNetz.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_FreqNetz.setStatus(_A)
class _SVal_UWR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_UWR_Type.__name__=_B
_SVal_UWR_Object=MibScalar
sVal_UWR=_SVal_UWR_Object((1,3,6,1,4,1,16460,4,1,1,3),_SVal_UWR_Type())
sVal_UWR.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_UWR.setStatus(_A)
class _SVal_FreqWR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_FreqWR_Type.__name__=_B
_SVal_FreqWR_Object=MibScalar
sVal_FreqWR=_SVal_FreqWR_Object((1,3,6,1,4,1,16460,4,1,1,4),_SVal_FreqWR_Type())
sVal_FreqWR.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_FreqWR.setStatus(_A)
class _SVal_UDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_UDC_Type.__name__=_B
_SVal_UDC_Object=MibScalar
sVal_UDC=_SVal_UDC_Object((1,3,6,1,4,1,16460,4,1,1,5),_SVal_UDC_Type())
sVal_UDC.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_UDC.setStatus(_A)
class _SVal_U10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_U10_Type.__name__=_B
_SVal_U10_Object=MibScalar
sVal_U10=_SVal_U10_Object((1,3,6,1,4,1,16460,4,1,1,6),_SVal_U10_Type())
sVal_U10.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_U10.setStatus(_A)
class _SVal_IO1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_IO1_Type.__name__=_B
_SVal_IO1_Object=MibScalar
sVal_IO1=_SVal_IO1_Object((1,3,6,1,4,1,16460,4,1,1,7),_SVal_IO1_Type())
sVal_IO1.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_IO1.setStatus(_A)
class _SVal_P_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_P_Type.__name__=_B
_SVal_P_Object=MibScalar
sVal_P=_SVal_P_Object((1,3,6,1,4,1,16460,4,1,1,8),_SVal_P_Type())
sVal_P.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_P.setStatus(_A)
class _SVal_S_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_S_Type.__name__=_B
_SVal_S_Object=MibScalar
sVal_S=_SVal_S_Object((1,3,6,1,4,1,16460,4,1,1,9),_SVal_S_Type())
sVal_S.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_S.setStatus(_A)
class _SVal_FAN1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_FAN1_Type.__name__=_B
_SVal_FAN1_Object=MibScalar
sVal_FAN1=_SVal_FAN1_Object((1,3,6,1,4,1,16460,4,1,1,10),_SVal_FAN1_Type())
sVal_FAN1.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_FAN1.setStatus(_A)
class _SVal_FAN2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_FAN2_Type.__name__=_B
_SVal_FAN2_Object=MibScalar
sVal_FAN2=_SVal_FAN2_Object((1,3,6,1,4,1,16460,4,1,1,11),_SVal_FAN2_Type())
sVal_FAN2.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_FAN2.setStatus(_A)
class _SVal_TK_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_TK_Type.__name__=_B
_SVal_TK_Object=MibScalar
sVal_TK=_SVal_TK_Object((1,3,6,1,4,1,16460,4,1,1,12),_SVal_TK_Type())
sVal_TK.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_TK.setStatus(_A)
class _SVal_IO2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_IO2_Type.__name__=_B
_SVal_IO2_Object=MibScalar
sVal_IO2=_SVal_IO2_Object((1,3,6,1,4,1,16460,4,1,1,13),_SVal_IO2_Type())
sVal_IO2.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_IO2.setStatus(_A)
class _SVal_IDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SVal_IDC_Type.__name__=_B
_SVal_IDC_Object=MibScalar
sVal_IDC=_SVal_IDC_Object((1,3,6,1,4,1,16460,4,1,1,14),_SVal_IDC_Type())
sVal_IDC.setMaxAccess(_E)
if mibBuilder.loadTexts:sVal_IDC.setStatus(_A)
_Inverter_measureValues_ObjectIdentity=ObjectIdentity
inverter_measureValues=_Inverter_measureValues_ObjectIdentity((1,3,6,1,4,1,16460,4,1,2))
_Inverter_Table_Object=MibTable
inverter_Table=_Inverter_Table_Object((1,3,6,1,4,1,16460,4,1,2,1))
if mibBuilder.loadTexts:inverter_Table.setStatus(_A)
_Inverter_Entry_Object=MibTableRow
inverter_Entry=_Inverter_Entry_Object((1,3,6,1,4,1,16460,4,1,2,1,1))
inverter_Entry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:inverter_Entry.setStatus(_M)
class _Inv_Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Inv_Index_Type.__name__=_B
_Inv_Index_Object=MibTableColumn
inv_Index=_Inv_Index_Object((1,3,6,1,4,1,16460,4,1,2,1,1,0),_Inv_Index_Type())
inv_Index.setMaxAccess(_F)
if mibBuilder.loadTexts:inv_Index.setStatus(_N)
if mibBuilder.loadTexts:inv_Index.setUnits('NA')
class _Inv_Nbr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Inv_Nbr_Type.__name__=_B
_Inv_Nbr_Object=MibTableColumn
inv_Nbr=_Inv_Nbr_Object((1,3,6,1,4,1,16460,4,1,2,1,1,1),_Inv_Nbr_Type())
inv_Nbr.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Nbr.setStatus(_A)
class _Inv_InCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Inv_InCurrent_Type.__name__=_B
_Inv_InCurrent_Object=MibTableColumn
inv_InCurrent=_Inv_InCurrent_Object((1,3,6,1,4,1,16460,4,1,2,1,1,2),_Inv_InCurrent_Type())
inv_InCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_InCurrent.setStatus(_A)
class _Inv_OutCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Inv_OutCurrent_Type.__name__=_B
_Inv_OutCurrent_Object=MibTableColumn
inv_OutCurrent=_Inv_OutCurrent_Object((1,3,6,1,4,1,16460,4,1,2,1,1,3),_Inv_OutCurrent_Type())
inv_OutCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_OutCurrent.setStatus(_A)
class _Inv_Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Inv_Temperature_Type.__name__=_B
_Inv_Temperature_Object=MibTableColumn
inv_Temperature=_Inv_Temperature_Object((1,3,6,1,4,1,16460,4,1,2,1,1,4),_Inv_Temperature_Type())
inv_Temperature.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Temperature.setStatus(_A)
class _Inv_InputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Inv_InputVoltage_Type.__name__=_B
_Inv_InputVoltage_Object=MibTableColumn
inv_InputVoltage=_Inv_InputVoltage_Object((1,3,6,1,4,1,16460,4,1,2,1,1,5),_Inv_InputVoltage_Type())
inv_InputVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_InputVoltage.setStatus(_A)
class _Inv_STi_great_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_STi_great_Type.__name__=_B
_Inv_STi_great_Object=MibTableColumn
inv_STi_great=_Inv_STi_great_Object((1,3,6,1,4,1,16460,4,1,2,1,1,6),_Inv_STi_great_Type())
inv_STi_great.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_STi_great.setStatus(_A)
class _Inv_Fan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Fan_Type.__name__=_B
_Inv_Fan_Object=MibTableColumn
inv_Fan=_Inv_Fan_Object((1,3,6,1,4,1,16460,4,1,2,1,1,7),_Inv_Fan_Type())
inv_Fan.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Fan.setStatus(_A)
class _Inv_RemoteOffCan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_RemoteOffCan_Type.__name__=_B
_Inv_RemoteOffCan_Object=MibTableColumn
inv_RemoteOffCan=_Inv_RemoteOffCan_Object((1,3,6,1,4,1,16460,4,1,2,1,1,8),_Inv_RemoteOffCan_Type())
inv_RemoteOffCan.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_RemoteOffCan.setStatus(_A)
class _Inv_UoutOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_UoutOff_Type.__name__=_B
_Inv_UoutOff_Object=MibTableColumn
inv_UoutOff=_Inv_UoutOff_Object((1,3,6,1,4,1,16460,4,1,2,1,1,9),_Inv_UoutOff_Type())
inv_UoutOff.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_UoutOff.setStatus(_A)
class _Inv_Bit_ShortCircuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Bit_ShortCircuit_Type.__name__=_B
_Inv_Bit_ShortCircuit_Object=MibTableColumn
inv_Bit_ShortCircuit=_Inv_Bit_ShortCircuit_Object((1,3,6,1,4,1,16460,4,1,2,1,1,10),_Inv_Bit_ShortCircuit_Type())
inv_Bit_ShortCircuit.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Bit_ShortCircuit.setStatus(_A)
class _Inv_Bit_OutputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Bit_OutputVoltage_Type.__name__=_B
_Inv_Bit_OutputVoltage_Object=MibTableColumn
inv_Bit_OutputVoltage=_Inv_Bit_OutputVoltage_Object((1,3,6,1,4,1,16460,4,1,2,1,1,11),_Inv_Bit_OutputVoltage_Type())
inv_Bit_OutputVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Bit_OutputVoltage.setStatus(_A)
class _Inv_Bit_InputVoltLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Bit_InputVoltLow_Type.__name__=_B
_Inv_Bit_InputVoltLow_Object=MibTableColumn
inv_Bit_InputVoltLow=_Inv_Bit_InputVoltLow_Object((1,3,6,1,4,1,16460,4,1,2,1,1,12),_Inv_Bit_InputVoltLow_Type())
inv_Bit_InputVoltLow.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Bit_InputVoltLow.setStatus(_A)
class _Inv_Bit_InputVoltHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Bit_InputVoltHigh_Type.__name__=_B
_Inv_Bit_InputVoltHigh_Object=MibTableColumn
inv_Bit_InputVoltHigh=_Inv_Bit_InputVoltHigh_Object((1,3,6,1,4,1,16460,4,1,2,1,1,13),_Inv_Bit_InputVoltHigh_Type())
inv_Bit_InputVoltHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Bit_InputVoltHigh.setStatus(_A)
class _Inv_Bit_OutputVoltLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Bit_OutputVoltLow_Type.__name__=_B
_Inv_Bit_OutputVoltLow_Object=MibTableColumn
inv_Bit_OutputVoltLow=_Inv_Bit_OutputVoltLow_Object((1,3,6,1,4,1,16460,4,1,2,1,1,14),_Inv_Bit_OutputVoltLow_Type())
inv_Bit_OutputVoltLow.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Bit_OutputVoltLow.setStatus(_A)
class _Inv_Bit_OutputVoltHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Bit_OutputVoltHigh_Type.__name__=_B
_Inv_Bit_OutputVoltHigh_Object=MibTableColumn
inv_Bit_OutputVoltHigh=_Inv_Bit_OutputVoltHigh_Object((1,3,6,1,4,1,16460,4,1,2,1,1,15),_Inv_Bit_OutputVoltHigh_Type())
inv_Bit_OutputVoltHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Bit_OutputVoltHigh.setStatus(_A)
class _Inv_Bit_OutputCurrHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Bit_OutputCurrHigh_Type.__name__=_B
_Inv_Bit_OutputCurrHigh_Object=MibTableColumn
inv_Bit_OutputCurrHigh=_Inv_Bit_OutputCurrHigh_Object((1,3,6,1,4,1,16460,4,1,2,1,1,16),_Inv_Bit_OutputCurrHigh_Type())
inv_Bit_OutputCurrHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Bit_OutputCurrHigh.setStatus(_A)
class _Inv_Bit_RemoteOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Bit_RemoteOff_Type.__name__=_B
_Inv_Bit_RemoteOff_Object=MibTableColumn
inv_Bit_RemoteOff=_Inv_Bit_RemoteOff_Object((1,3,6,1,4,1,16460,4,1,2,1,1,17),_Inv_Bit_RemoteOff_Type())
inv_Bit_RemoteOff.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Bit_RemoteOff.setStatus(_A)
class _Inv_Bit_CentralAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inv_Bit_CentralAlarm_Type.__name__=_B
_Inv_Bit_CentralAlarm_Object=MibTableColumn
inv_Bit_CentralAlarm=_Inv_Bit_CentralAlarm_Object((1,3,6,1,4,1,16460,4,1,2,1,1,18),_Inv_Bit_CentralAlarm_Type())
inv_Bit_CentralAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Bit_CentralAlarm.setStatus(_A)
class _Inv_Type_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Inv_Type_Type.__name__=_J
_Inv_Type_Object=MibTableColumn
inv_Type=_Inv_Type_Object((1,3,6,1,4,1,16460,4,1,2,1,1,19),_Inv_Type_Type())
inv_Type.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Type.setStatus(_A)
class _Inv_Mat_CD_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Inv_Mat_CD_Type.__name__=_J
_Inv_Mat_CD_Object=MibTableColumn
inv_Mat_CD=_Inv_Mat_CD_Object((1,3,6,1,4,1,16460,4,1,2,1,1,20),_Inv_Mat_CD_Type())
inv_Mat_CD.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_Mat_CD.setStatus(_A)
class _Inv_SerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Inv_SerialNo_Type.__name__=_J
_Inv_SerialNo_Object=MibTableColumn
inv_SerialNo=_Inv_SerialNo_Object((1,3,6,1,4,1,16460,4,1,2,1,1,21),_Inv_SerialNo_Type())
inv_SerialNo.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_SerialNo.setStatus(_A)
class _Inv_HardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Inv_HardwareVersion_Type.__name__=_J
_Inv_HardwareVersion_Object=MibTableColumn
inv_HardwareVersion=_Inv_HardwareVersion_Object((1,3,6,1,4,1,16460,4,1,2,1,1,22),_Inv_HardwareVersion_Type())
inv_HardwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_HardwareVersion.setStatus(_A)
class _Inv_SoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_Inv_SoftwareVersion_Type.__name__=_J
_Inv_SoftwareVersion_Object=MibTableColumn
inv_SoftwareVersion=_Inv_SoftwareVersion_Object((1,3,6,1,4,1,16460,4,1,2,1,1,23),_Inv_SoftwareVersion_Type())
inv_SoftwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:inv_SoftwareVersion.setStatus(_A)
_Settings_ObjectIdentity=ObjectIdentity
settings=_Settings_ObjectIdentity((1,3,6,1,4,1,16460,4,2))
_NetworkSettings_ObjectIdentity=ObjectIdentity
networkSettings=_NetworkSettings_ObjectIdentity((1,3,6,1,4,1,16460,4,2,1))
_BaseSettings_ObjectIdentity=ObjectIdentity
baseSettings=_BaseSettings_ObjectIdentity((1,3,6,1,4,1,16460,4,2,1,1))
class _BETHSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BETHSpeed_Type.__name__=_B
_BETHSpeed_Object=MibScalar
bETHSpeed=_BETHSpeed_Object((1,3,6,1,4,1,16460,4,2,1,1,1),_BETHSpeed_Type())
bETHSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:bETHSpeed.setStatus(_A)
_BLocalIP_Type=IpAddress
_BLocalIP_Object=MibScalar
bLocalIP=_BLocalIP_Object((1,3,6,1,4,1,16460,4,2,1,1,2),_BLocalIP_Type())
bLocalIP.setMaxAccess(_D)
if mibBuilder.loadTexts:bLocalIP.setStatus(_A)
_BSubnetMask_Type=IpAddress
_BSubnetMask_Object=MibScalar
bSubnetMask=_BSubnetMask_Object((1,3,6,1,4,1,16460,4,2,1,1,3),_BSubnetMask_Type())
bSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:bSubnetMask.setStatus(_A)
_BGateway_Type=IpAddress
_BGateway_Object=MibScalar
bGateway=_BGateway_Object((1,3,6,1,4,1,16460,4,2,1,1,4),_BGateway_Type())
bGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:bGateway.setStatus(_A)
_BDNSServer_Type=IpAddress
_BDNSServer_Object=MibScalar
bDNSServer=_BDNSServer_Object((1,3,6,1,4,1,16460,4,2,1,1,5),_BDNSServer_Type())
bDNSServer.setMaxAccess(_D)
if mibBuilder.loadTexts:bDNSServer.setStatus(_A)
class _BDHCPServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BDHCPServer_Type.__name__=_J
_BDHCPServer_Object=MibScalar
bDHCPServer=_BDHCPServer_Object((1,3,6,1,4,1,16460,4,2,1,1,6),_BDHCPServer_Type())
bDHCPServer.setMaxAccess(_D)
if mibBuilder.loadTexts:bDHCPServer.setStatus(_A)
class _BFixedIP_OnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BFixedIP_OnOff_Type.__name__=_B
_BFixedIP_OnOff_Object=MibScalar
bFixedIP_OnOff=_BFixedIP_OnOff_Object((1,3,6,1,4,1,16460,4,2,1,1,7),_BFixedIP_OnOff_Type())
bFixedIP_OnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:bFixedIP_OnOff.setStatus(_A)
class _BDefaultIP_OnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BDefaultIP_OnOff_Type.__name__=_B
_BDefaultIP_OnOff_Object=MibScalar
bDefaultIP_OnOff=_BDefaultIP_OnOff_Object((1,3,6,1,4,1,16460,4,2,1,1,8),_BDefaultIP_OnOff_Type())
bDefaultIP_OnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:bDefaultIP_OnOff.setStatus(_A)
class _BDHCP_OnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BDHCP_OnOff_Type.__name__=_B
_BDHCP_OnOff_Object=MibScalar
bDHCP_OnOff=_BDHCP_OnOff_Object((1,3,6,1,4,1,16460,4,2,1,1,9),_BDHCP_OnOff_Type())
bDHCP_OnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:bDHCP_OnOff.setStatus(_A)
class _BBOOTP_OnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_BBOOTP_OnOff_Type.__name__=_B
_BBOOTP_OnOff_Object=MibScalar
bBOOTP_OnOff=_BBOOTP_OnOff_Object((1,3,6,1,4,1,16460,4,2,1,1,10),_BBOOTP_OnOff_Type())
bBOOTP_OnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:bBOOTP_OnOff.setStatus(_A)
class _BLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BLocation_Type.__name__=_J
_BLocation_Object=MibScalar
bLocation=_BLocation_Object((1,3,6,1,4,1,16460,4,2,1,1,11),_BLocation_Type())
bLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:bLocation.setStatus(_A)
_ServiceSettings_ObjectIdentity=ObjectIdentity
serviceSettings=_ServiceSettings_ObjectIdentity((1,3,6,1,4,1,16460,4,2,1,2))
class _ServSNMP_OnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ServSNMP_OnOff_Type.__name__=_B
_ServSNMP_OnOff_Object=MibScalar
servSNMP_OnOff=_ServSNMP_OnOff_Object((1,3,6,1,4,1,16460,4,2,1,2,1),_ServSNMP_OnOff_Type())
servSNMP_OnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:servSNMP_OnOff.setStatus(_A)
_ServTrapReceiver1_Type=IpAddress
_ServTrapReceiver1_Object=MibScalar
servTrapReceiver1=_ServTrapReceiver1_Object((1,3,6,1,4,1,16460,4,2,1,2,2),_ServTrapReceiver1_Type())
servTrapReceiver1.setMaxAccess(_D)
if mibBuilder.loadTexts:servTrapReceiver1.setStatus(_A)
_ServTrapReceiver2_Type=IpAddress
_ServTrapReceiver2_Object=MibScalar
servTrapReceiver2=_ServTrapReceiver2_Object((1,3,6,1,4,1,16460,4,2,1,2,3),_ServTrapReceiver2_Type())
servTrapReceiver2.setMaxAccess(_D)
if mibBuilder.loadTexts:servTrapReceiver2.setStatus(_A)
_ServTrapReceiver3_Type=IpAddress
_ServTrapReceiver3_Object=MibScalar
servTrapReceiver3=_ServTrapReceiver3_Object((1,3,6,1,4,1,16460,4,2,1,2,4),_ServTrapReceiver3_Type())
servTrapReceiver3.setMaxAccess(_D)
if mibBuilder.loadTexts:servTrapReceiver3.setStatus(_A)
_ServTrapReceiver4_Type=IpAddress
_ServTrapReceiver4_Object=MibScalar
servTrapReceiver4=_ServTrapReceiver4_Object((1,3,6,1,4,1,16460,4,2,1,2,5),_ServTrapReceiver4_Type())
servTrapReceiver4.setMaxAccess(_D)
if mibBuilder.loadTexts:servTrapReceiver4.setStatus(_A)
class _ServReadCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_ServReadCommunity_Type.__name__=_J
_ServReadCommunity_Object=MibScalar
servReadCommunity=_ServReadCommunity_Object((1,3,6,1,4,1,16460,4,2,1,2,6),_ServReadCommunity_Type())
servReadCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:servReadCommunity.setStatus(_A)
class _ServWriteCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_ServWriteCommunity_Type.__name__=_J
_ServWriteCommunity_Object=MibScalar
servWriteCommunity=_ServWriteCommunity_Object((1,3,6,1,4,1,16460,4,2,1,2,7),_ServWriteCommunity_Type())
servWriteCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:servWriteCommunity.setStatus(_A)
class _ServSMTP_OnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ServSMTP_OnOff_Type.__name__=_B
_ServSMTP_OnOff_Object=MibScalar
servSMTP_OnOff=_ServSMTP_OnOff_Object((1,3,6,1,4,1,16460,4,2,1,2,8),_ServSMTP_OnOff_Type())
servSMTP_OnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:servSMTP_OnOff.setStatus(_A)
class _ServMailServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_ServMailServer_Type.__name__=_J
_ServMailServer_Object=MibScalar
servMailServer=_ServMailServer_Object((1,3,6,1,4,1,16460,4,2,1,2,9),_ServMailServer_Type())
servMailServer.setMaxAccess(_D)
if mibBuilder.loadTexts:servMailServer.setStatus(_A)
class _ServMailUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_ServMailUsername_Type.__name__=_J
_ServMailUsername_Object=MibScalar
servMailUsername=_ServMailUsername_Object((1,3,6,1,4,1,16460,4,2,1,2,10),_ServMailUsername_Type())
servMailUsername.setMaxAccess(_D)
if mibBuilder.loadTexts:servMailUsername.setStatus(_A)
class _ServMailPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_ServMailPassword_Type.__name__=_J
_ServMailPassword_Object=MibScalar
servMailPassword=_ServMailPassword_Object((1,3,6,1,4,1,16460,4,2,1,2,11),_ServMailPassword_Type())
servMailPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:servMailPassword.setStatus(_A)
class _ServMailReceiver1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_ServMailReceiver1_Type.__name__=_J
_ServMailReceiver1_Object=MibScalar
servMailReceiver1=_ServMailReceiver1_Object((1,3,6,1,4,1,16460,4,2,1,2,12),_ServMailReceiver1_Type())
servMailReceiver1.setMaxAccess(_D)
if mibBuilder.loadTexts:servMailReceiver1.setStatus(_A)
class _ServMailTrapLevel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ServMailTrapLevel1_Type.__name__=_B
_ServMailTrapLevel1_Object=MibScalar
servMailTrapLevel1=_ServMailTrapLevel1_Object((1,3,6,1,4,1,16460,4,2,1,2,13),_ServMailTrapLevel1_Type())
servMailTrapLevel1.setMaxAccess(_D)
if mibBuilder.loadTexts:servMailTrapLevel1.setStatus(_A)
class _ServMailReceiver2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_ServMailReceiver2_Type.__name__=_J
_ServMailReceiver2_Object=MibScalar
servMailReceiver2=_ServMailReceiver2_Object((1,3,6,1,4,1,16460,4,2,1,2,14),_ServMailReceiver2_Type())
servMailReceiver2.setMaxAccess(_D)
if mibBuilder.loadTexts:servMailReceiver2.setStatus(_A)
class _ServMailTrapLevel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ServMailTrapLevel2_Type.__name__=_B
_ServMailTrapLevel2_Object=MibScalar
servMailTrapLevel2=_ServMailTrapLevel2_Object((1,3,6,1,4,1,16460,4,2,1,2,15),_ServMailTrapLevel2_Type())
servMailTrapLevel2.setMaxAccess(_D)
if mibBuilder.loadTexts:servMailTrapLevel2.setStatus(_A)
class _ServSNTP_OnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ServSNTP_OnOff_Type.__name__=_B
_ServSNTP_OnOff_Object=MibScalar
servSNTP_OnOff=_ServSNTP_OnOff_Object((1,3,6,1,4,1,16460,4,2,1,2,16),_ServSNTP_OnOff_Type())
servSNTP_OnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:servSNTP_OnOff.setStatus(_A)
class _ServSNTPServer1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_ServSNTPServer1_Type.__name__=_J
_ServSNTPServer1_Object=MibScalar
servSNTPServer1=_ServSNTPServer1_Object((1,3,6,1,4,1,16460,4,2,1,2,17),_ServSNTPServer1_Type())
servSNTPServer1.setMaxAccess(_D)
if mibBuilder.loadTexts:servSNTPServer1.setStatus(_A)
class _ServSNTPServer2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_ServSNTPServer2_Type.__name__=_J
_ServSNTPServer2_Object=MibScalar
servSNTPServer2=_ServSNTPServer2_Object((1,3,6,1,4,1,16460,4,2,1,2,18),_ServSNTPServer2_Type())
servSNTPServer2.setMaxAccess(_D)
if mibBuilder.loadTexts:servSNTPServer2.setStatus(_A)
class _ServTelnet_OnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ServTelnet_OnOff_Type.__name__=_B
_ServTelnet_OnOff_Object=MibScalar
servTelnet_OnOff=_ServTelnet_OnOff_Object((1,3,6,1,4,1,16460,4,2,1,2,19),_ServTelnet_OnOff_Type())
servTelnet_OnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:servTelnet_OnOff.setStatus(_A)
class _ServSyslog_OnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ServSyslog_OnOff_Type.__name__=_B
_ServSyslog_OnOff_Object=MibScalar
servSyslog_OnOff=_ServSyslog_OnOff_Object((1,3,6,1,4,1,16460,4,2,1,2,20),_ServSyslog_OnOff_Type())
servSyslog_OnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:servSyslog_OnOff.setStatus(_A)
_UnitSettings_ObjectIdentity=ObjectIdentity
unitSettings=_UnitSettings_ObjectIdentity((1,3,6,1,4,1,16460,4,2,2))
_BasicSettings_ObjectIdentity=ObjectIdentity
basicSettings=_BasicSettings_ObjectIdentity((1,3,6,1,4,1,16460,4,2,2,1))
class _Sts_Version_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Sts_Version_Type.__name__=_B
_Sts_Version_Object=MibScalar
sts_Version=_Sts_Version_Object((1,3,6,1,4,1,16460,4,2,2,1,1),_Sts_Version_Type())
sts_Version.setMaxAccess(_E)
if mibBuilder.loadTexts:sts_Version.setStatus(_A)
class _Sts_Inverter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Sts_Inverter_Type.__name__=_B
_Sts_Inverter_Object=MibScalar
sts_Inverter=_Sts_Inverter_Object((1,3,6,1,4,1,16460,4,2,2,1,2),_Sts_Inverter_Type())
sts_Inverter.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_Inverter.setStatus(_A)
class _Sts_SigCF_b0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b0_Type.__name__=_B
_Sts_SigCF_b0_Object=MibScalar
sts_SigCF_b0=_Sts_SigCF_b0_Object((1,3,6,1,4,1,16460,4,2,2,1,3),_Sts_SigCF_b0_Type())
sts_SigCF_b0.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b0.setStatus(_A)
class _Sts_SigCF_b1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b1_Type.__name__=_B
_Sts_SigCF_b1_Object=MibScalar
sts_SigCF_b1=_Sts_SigCF_b1_Object((1,3,6,1,4,1,16460,4,2,2,1,4),_Sts_SigCF_b1_Type())
sts_SigCF_b1.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b1.setStatus(_A)
class _Sts_SigCF_b2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b2_Type.__name__=_B
_Sts_SigCF_b2_Object=MibScalar
sts_SigCF_b2=_Sts_SigCF_b2_Object((1,3,6,1,4,1,16460,4,2,2,1,5),_Sts_SigCF_b2_Type())
sts_SigCF_b2.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b2.setStatus(_A)
class _Sts_SigCF_b3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b3_Type.__name__=_B
_Sts_SigCF_b3_Object=MibScalar
sts_SigCF_b3=_Sts_SigCF_b3_Object((1,3,6,1,4,1,16460,4,2,2,1,6),_Sts_SigCF_b3_Type())
sts_SigCF_b3.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b3.setStatus(_A)
class _Sts_SigCF_b4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b4_Type.__name__=_B
_Sts_SigCF_b4_Object=MibScalar
sts_SigCF_b4=_Sts_SigCF_b4_Object((1,3,6,1,4,1,16460,4,2,2,1,7),_Sts_SigCF_b4_Type())
sts_SigCF_b4.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b4.setStatus(_A)
class _Sts_SigCF_b5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b5_Type.__name__=_B
_Sts_SigCF_b5_Object=MibScalar
sts_SigCF_b5=_Sts_SigCF_b5_Object((1,3,6,1,4,1,16460,4,2,2,1,8),_Sts_SigCF_b5_Type())
sts_SigCF_b5.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b5.setStatus(_A)
class _Sts_SigCF_b6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b6_Type.__name__=_B
_Sts_SigCF_b6_Object=MibScalar
sts_SigCF_b6=_Sts_SigCF_b6_Object((1,3,6,1,4,1,16460,4,2,2,1,9),_Sts_SigCF_b6_Type())
sts_SigCF_b6.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b6.setStatus(_A)
class _Sts_SigCF_b7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b7_Type.__name__=_B
_Sts_SigCF_b7_Object=MibScalar
sts_SigCF_b7=_Sts_SigCF_b7_Object((1,3,6,1,4,1,16460,4,2,2,1,10),_Sts_SigCF_b7_Type())
sts_SigCF_b7.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b7.setStatus(_A)
class _Sts_SigCF_b8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b8_Type.__name__=_B
_Sts_SigCF_b8_Object=MibScalar
sts_SigCF_b8=_Sts_SigCF_b8_Object((1,3,6,1,4,1,16460,4,2,2,1,11),_Sts_SigCF_b8_Type())
sts_SigCF_b8.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b8.setStatus(_A)
class _Sts_SigCF_b9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b9_Type.__name__=_B
_Sts_SigCF_b9_Object=MibScalar
sts_SigCF_b9=_Sts_SigCF_b9_Object((1,3,6,1,4,1,16460,4,2,2,1,12),_Sts_SigCF_b9_Type())
sts_SigCF_b9.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b9.setStatus(_A)
class _Sts_SigCF_b10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b10_Type.__name__=_B
_Sts_SigCF_b10_Object=MibScalar
sts_SigCF_b10=_Sts_SigCF_b10_Object((1,3,6,1,4,1,16460,4,2,2,1,13),_Sts_SigCF_b10_Type())
sts_SigCF_b10.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b10.setStatus(_A)
class _Sts_SigCF_b11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b11_Type.__name__=_B
_Sts_SigCF_b11_Object=MibScalar
sts_SigCF_b11=_Sts_SigCF_b11_Object((1,3,6,1,4,1,16460,4,2,2,1,14),_Sts_SigCF_b11_Type())
sts_SigCF_b11.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b11.setStatus(_A)
class _Sts_SigCF_b12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b12_Type.__name__=_B
_Sts_SigCF_b12_Object=MibScalar
sts_SigCF_b12=_Sts_SigCF_b12_Object((1,3,6,1,4,1,16460,4,2,2,1,15),_Sts_SigCF_b12_Type())
sts_SigCF_b12.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b12.setStatus(_A)
class _Sts_SigCF_b13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b13_Type.__name__=_B
_Sts_SigCF_b13_Object=MibScalar
sts_SigCF_b13=_Sts_SigCF_b13_Object((1,3,6,1,4,1,16460,4,2,2,1,16),_Sts_SigCF_b13_Type())
sts_SigCF_b13.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b13.setStatus(_A)
class _Sts_SigCF_b14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b14_Type.__name__=_B
_Sts_SigCF_b14_Object=MibScalar
sts_SigCF_b14=_Sts_SigCF_b14_Object((1,3,6,1,4,1,16460,4,2,2,1,17),_Sts_SigCF_b14_Type())
sts_SigCF_b14.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b14.setStatus(_A)
class _Sts_SigCF_b15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigCF_b15_Type.__name__=_B
_Sts_SigCF_b15_Object=MibScalar
sts_SigCF_b15=_Sts_SigCF_b15_Object((1,3,6,1,4,1,16460,4,2,2,1,18),_Sts_SigCF_b15_Type())
sts_SigCF_b15.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigCF_b15.setStatus(_A)
class _Sts_DelayRelCA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Sts_DelayRelCA_Type.__name__=_B
_Sts_DelayRelCA_Object=MibScalar
sts_DelayRelCA=_Sts_DelayRelCA_Object((1,3,6,1,4,1,16460,4,2,2,1,19),_Sts_DelayRelCA_Type())
sts_DelayRelCA.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_DelayRelCA.setStatus(_A)
class _Sts_DelayLEDCA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Sts_DelayLEDCA_Type.__name__=_B
_Sts_DelayLEDCA_Object=MibScalar
sts_DelayLEDCA=_Sts_DelayLEDCA_Object((1,3,6,1,4,1,16460,4,2,2,1,20),_Sts_DelayLEDCA_Type())
sts_DelayLEDCA.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_DelayLEDCA.setStatus(_A)
class _Sts_LCDContrast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Sts_LCDContrast_Type.__name__=_B
_Sts_LCDContrast_Object=MibScalar
sts_LCDContrast=_Sts_LCDContrast_Object((1,3,6,1,4,1,16460,4,2,2,1,21),_Sts_LCDContrast_Type())
sts_LCDContrast.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_LCDContrast.setStatus(_A)
class _Sts_Language_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Sts_Language_Type.__name__=_B
_Sts_Language_Object=MibScalar
sts_Language=_Sts_Language_Object((1,3,6,1,4,1,16460,4,2,2,1,22),_Sts_Language_Type())
sts_Language.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_Language.setStatus(_A)
_AdvancedSettings_ObjectIdentity=ObjectIdentity
advancedSettings=_AdvancedSettings_ObjectIdentity((1,3,6,1,4,1,16460,4,2,2,2))
class _Sts_OpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_OpMode_Type.__name__=_B
_Sts_OpMode_Object=MibScalar
sts_OpMode=_Sts_OpMode_Object((1,3,6,1,4,1,16460,4,2,2,2,1),_Sts_OpMode_Type())
sts_OpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_OpMode.setStatus(_A)
class _Sts_UpperSwitchLimS1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,20))
_Sts_UpperSwitchLimS1_Type.__name__=_B
_Sts_UpperSwitchLimS1_Object=MibScalar
sts_UpperSwitchLimS1=_Sts_UpperSwitchLimS1_Object((1,3,6,1,4,1,16460,4,2,2,2,2),_Sts_UpperSwitchLimS1_Type())
sts_UpperSwitchLimS1.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_UpperSwitchLimS1.setStatus(_A)
class _Sts_LowerSwitchLimS1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,20))
_Sts_LowerSwitchLimS1_Type.__name__=_B
_Sts_LowerSwitchLimS1_Object=MibScalar
sts_LowerSwitchLimS1=_Sts_LowerSwitchLimS1_Object((1,3,6,1,4,1,16460,4,2,2,2,3),_Sts_LowerSwitchLimS1_Type())
sts_LowerSwitchLimS1.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_LowerSwitchLimS1.setStatus(_A)
class _Sts_SwitchDelayS1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Sts_SwitchDelayS1_Type.__name__=_B
_Sts_SwitchDelayS1_Object=MibScalar
sts_SwitchDelayS1=_Sts_SwitchDelayS1_Object((1,3,6,1,4,1,16460,4,2,2,2,4),_Sts_SwitchDelayS1_Type())
sts_SwitchDelayS1.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SwitchDelayS1.setStatus(_A)
class _Sts_UpperSwitchLimS2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,20))
_Sts_UpperSwitchLimS2_Type.__name__=_B
_Sts_UpperSwitchLimS2_Object=MibScalar
sts_UpperSwitchLimS2=_Sts_UpperSwitchLimS2_Object((1,3,6,1,4,1,16460,4,2,2,2,5),_Sts_UpperSwitchLimS2_Type())
sts_UpperSwitchLimS2.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_UpperSwitchLimS2.setStatus(_A)
class _Sts_LowerSwitchLimS2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,20))
_Sts_LowerSwitchLimS2_Type.__name__=_B
_Sts_LowerSwitchLimS2_Object=MibScalar
sts_LowerSwitchLimS2=_Sts_LowerSwitchLimS2_Object((1,3,6,1,4,1,16460,4,2,2,2,6),_Sts_LowerSwitchLimS2_Type())
sts_LowerSwitchLimS2.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_LowerSwitchLimS2.setStatus(_A)
class _Sts_SwitchDelayS2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Sts_SwitchDelayS2_Type.__name__=_B
_Sts_SwitchDelayS2_Object=MibScalar
sts_SwitchDelayS2=_Sts_SwitchDelayS2_Object((1,3,6,1,4,1,16460,4,2,2,2,7),_Sts_SwitchDelayS2_Type())
sts_SwitchDelayS2.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SwitchDelayS2.setStatus(_A)
class _Sts_MaxCellVolt1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,300))
_Sts_MaxCellVolt1_Type.__name__=_B
_Sts_MaxCellVolt1_Object=MibScalar
sts_MaxCellVolt1=_Sts_MaxCellVolt1_Object((1,3,6,1,4,1,16460,4,2,2,2,8),_Sts_MaxCellVolt1_Type())
sts_MaxCellVolt1.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_MaxCellVolt1.setStatus(_A)
class _Sts_MinCellVolt1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(70,250))
_Sts_MinCellVolt1_Type.__name__=_B
_Sts_MinCellVolt1_Object=MibScalar
sts_MinCellVolt1=_Sts_MinCellVolt1_Object((1,3,6,1,4,1,16460,4,2,2,2,9),_Sts_MinCellVolt1_Type())
sts_MinCellVolt1.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_MinCellVolt1.setStatus(_A)
class _Sts_MinCellVolt2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,250))
_Sts_MinCellVolt2_Type.__name__=_B
_Sts_MinCellVolt2_Object=MibScalar
sts_MinCellVolt2=_Sts_MinCellVolt2_Object((1,3,6,1,4,1,16460,4,2,2,2,10),_Sts_MinCellVolt2_Type())
sts_MinCellVolt2.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_MinCellVolt2.setStatus(_A)
class _Sts_MinULimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(170,210))
_Sts_MinULimit_Type.__name__=_B
_Sts_MinULimit_Object=MibScalar
sts_MinULimit=_Sts_MinULimit_Object((1,3,6,1,4,1,16460,4,2,2,2,11),_Sts_MinULimit_Type())
sts_MinULimit.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_MinULimit.setStatus(_A)
class _Sts_MaxULimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(220,250))
_Sts_MaxULimit_Type.__name__=_B
_Sts_MaxULimit_Object=MibScalar
sts_MaxULimit=_Sts_MaxULimit_Object((1,3,6,1,4,1,16460,4,2,2,2,12),_Sts_MaxULimit_Type())
sts_MaxULimit.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_MaxULimit.setStatus(_A)
_AdvancedSettings2_ObjectIdentity=ObjectIdentity
advancedSettings2=_AdvancedSettings2_ObjectIdentity((1,3,6,1,4,1,16460,4,2,2,3))
class _Sts_NomPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,500))
_Sts_NomPower_Type.__name__=_B
_Sts_NomPower_Object=MibScalar
sts_NomPower=_Sts_NomPower_Object((1,3,6,1,4,1,16460,4,2,2,3,1),_Sts_NomPower_Type())
sts_NomPower.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_NomPower.setStatus(_A)
class _Sts_NomVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,250))
_Sts_NomVolt_Type.__name__=_B
_Sts_NomVolt_Object=MibScalar
sts_NomVolt=_Sts_NomVolt_Object((1,3,6,1,4,1,16460,4,2,2,3,2),_Sts_NomVolt_Type())
sts_NomVolt.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_NomVolt.setStatus(_A)
class _Sts_NomFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_NomFreq_Type.__name__=_B
_Sts_NomFreq_Object=MibScalar
sts_NomFreq=_Sts_NomFreq_Object((1,3,6,1,4,1,16460,4,2,2,3,3),_Sts_NomFreq_Type())
sts_NomFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_NomFreq.setStatus(_A)
class _Sts_FreqRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Sts_FreqRange_Type.__name__=_B
_Sts_FreqRange_Object=MibScalar
sts_FreqRange=_Sts_FreqRange_Object((1,3,6,1,4,1,16460,4,2,2,3,4),_Sts_FreqRange_Type())
sts_FreqRange.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_FreqRange.setStatus(_A)
class _Sts_MaxCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2500))
_Sts_MaxCurrent_Type.__name__=_B
_Sts_MaxCurrent_Object=MibScalar
sts_MaxCurrent=_Sts_MaxCurrent_Object((1,3,6,1,4,1,16460,4,2,2,3,5),_Sts_MaxCurrent_Type())
sts_MaxCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_MaxCurrent.setStatus(_A)
class _Sts_PresentCell_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(12,200))
_Sts_PresentCell_Type.__name__=_B
_Sts_PresentCell_Object=MibScalar
sts_PresentCell=_Sts_PresentCell_Object((1,3,6,1,4,1,16460,4,2,2,3,6),_Sts_PresentCell_Type())
sts_PresentCell.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_PresentCell.setStatus(_A)
class _Sts_CellVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_CellVoltage_Type.__name__=_B
_Sts_CellVoltage_Object=MibScalar
sts_CellVoltage=_Sts_CellVoltage_Object((1,3,6,1,4,1,16460,4,2,2,3,7),_Sts_CellVoltage_Type())
sts_CellVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_CellVoltage.setStatus(_A)
class _Sts_Adress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_Sts_Adress_Type.__name__=_B
_Sts_Adress_Object=MibScalar
sts_Adress=_Sts_Adress_Object((1,3,6,1,4,1,16460,4,2,2,3,8),_Sts_Adress_Type())
sts_Adress.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_Adress.setStatus(_A)
class _Sts_SigRel2_b0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b0_Type.__name__=_B
_Sts_SigRel2_b0_Object=MibScalar
sts_SigRel2_b0=_Sts_SigRel2_b0_Object((1,3,6,1,4,1,16460,4,2,2,3,9),_Sts_SigRel2_b0_Type())
sts_SigRel2_b0.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b0.setStatus(_A)
class _Sts_SigRel2_b1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b1_Type.__name__=_B
_Sts_SigRel2_b1_Object=MibScalar
sts_SigRel2_b1=_Sts_SigRel2_b1_Object((1,3,6,1,4,1,16460,4,2,2,3,10),_Sts_SigRel2_b1_Type())
sts_SigRel2_b1.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b1.setStatus(_A)
class _Sts_SigRel2_b2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b2_Type.__name__=_B
_Sts_SigRel2_b2_Object=MibScalar
sts_SigRel2_b2=_Sts_SigRel2_b2_Object((1,3,6,1,4,1,16460,4,2,2,3,11),_Sts_SigRel2_b2_Type())
sts_SigRel2_b2.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b2.setStatus(_A)
class _Sts_SigRel2_b3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b3_Type.__name__=_B
_Sts_SigRel2_b3_Object=MibScalar
sts_SigRel2_b3=_Sts_SigRel2_b3_Object((1,3,6,1,4,1,16460,4,2,2,3,12),_Sts_SigRel2_b3_Type())
sts_SigRel2_b3.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b3.setStatus(_A)
class _Sts_SigRel2_b4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b4_Type.__name__=_B
_Sts_SigRel2_b4_Object=MibScalar
sts_SigRel2_b4=_Sts_SigRel2_b4_Object((1,3,6,1,4,1,16460,4,2,2,3,13),_Sts_SigRel2_b4_Type())
sts_SigRel2_b4.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b4.setStatus(_A)
class _Sts_SigRel2_b5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b5_Type.__name__=_B
_Sts_SigRel2_b5_Object=MibScalar
sts_SigRel2_b5=_Sts_SigRel2_b5_Object((1,3,6,1,4,1,16460,4,2,2,3,14),_Sts_SigRel2_b5_Type())
sts_SigRel2_b5.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b5.setStatus(_A)
class _Sts_SigRel2_b6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b6_Type.__name__=_B
_Sts_SigRel2_b6_Object=MibScalar
sts_SigRel2_b6=_Sts_SigRel2_b6_Object((1,3,6,1,4,1,16460,4,2,2,3,15),_Sts_SigRel2_b6_Type())
sts_SigRel2_b6.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b6.setStatus(_A)
class _Sts_SigRel2_b7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b7_Type.__name__=_B
_Sts_SigRel2_b7_Object=MibScalar
sts_SigRel2_b7=_Sts_SigRel2_b7_Object((1,3,6,1,4,1,16460,4,2,2,3,16),_Sts_SigRel2_b7_Type())
sts_SigRel2_b7.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b7.setStatus(_A)
class _Sts_SigRel2_b8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b8_Type.__name__=_B
_Sts_SigRel2_b8_Object=MibScalar
sts_SigRel2_b8=_Sts_SigRel2_b8_Object((1,3,6,1,4,1,16460,4,2,2,3,17),_Sts_SigRel2_b8_Type())
sts_SigRel2_b8.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b8.setStatus(_A)
class _Sts_SigRel2_b9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b9_Type.__name__=_B
_Sts_SigRel2_b9_Object=MibScalar
sts_SigRel2_b9=_Sts_SigRel2_b9_Object((1,3,6,1,4,1,16460,4,2,2,3,18),_Sts_SigRel2_b9_Type())
sts_SigRel2_b9.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b9.setStatus(_A)
class _Sts_SigRel2_b10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b10_Type.__name__=_B
_Sts_SigRel2_b10_Object=MibScalar
sts_SigRel2_b10=_Sts_SigRel2_b10_Object((1,3,6,1,4,1,16460,4,2,2,3,19),_Sts_SigRel2_b10_Type())
sts_SigRel2_b10.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b10.setStatus(_A)
class _Sts_SigRel2_b11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b11_Type.__name__=_B
_Sts_SigRel2_b11_Object=MibScalar
sts_SigRel2_b11=_Sts_SigRel2_b11_Object((1,3,6,1,4,1,16460,4,2,2,3,20),_Sts_SigRel2_b11_Type())
sts_SigRel2_b11.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b11.setStatus(_A)
class _Sts_SigRel2_b12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b12_Type.__name__=_B
_Sts_SigRel2_b12_Object=MibScalar
sts_SigRel2_b12=_Sts_SigRel2_b12_Object((1,3,6,1,4,1,16460,4,2,2,3,21),_Sts_SigRel2_b12_Type())
sts_SigRel2_b12.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b12.setStatus(_A)
class _Sts_SigRel2_b13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b13_Type.__name__=_B
_Sts_SigRel2_b13_Object=MibScalar
sts_SigRel2_b13=_Sts_SigRel2_b13_Object((1,3,6,1,4,1,16460,4,2,2,3,22),_Sts_SigRel2_b13_Type())
sts_SigRel2_b13.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b13.setStatus(_A)
class _Sts_SigRel2_b14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b14_Type.__name__=_B
_Sts_SigRel2_b14_Object=MibScalar
sts_SigRel2_b14=_Sts_SigRel2_b14_Object((1,3,6,1,4,1,16460,4,2,2,3,23),_Sts_SigRel2_b14_Type())
sts_SigRel2_b14.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b14.setStatus(_A)
class _Sts_SigRel2_b15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_SigRel2_b15_Type.__name__=_B
_Sts_SigRel2_b15_Object=MibScalar
sts_SigRel2_b15=_Sts_SigRel2_b15_Object((1,3,6,1,4,1,16460,4,2,2,3,24),_Sts_SigRel2_b15_Type())
sts_SigRel2_b15.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_SigRel2_b15.setStatus(_A)
class _Sts_ModeRel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sts_ModeRel2_Type.__name__=_B
_Sts_ModeRel2_Object=MibScalar
sts_ModeRel2=_Sts_ModeRel2_Object((1,3,6,1,4,1,16460,4,2,2,3,25),_Sts_ModeRel2_Type())
sts_ModeRel2.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_ModeRel2.setStatus(_A)
class _Sts_DelayRel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Sts_DelayRel2_Type.__name__=_B
_Sts_DelayRel2_Object=MibScalar
sts_DelayRel2=_Sts_DelayRel2_Object((1,3,6,1,4,1,16460,4,2,2,3,26),_Sts_DelayRel2_Type())
sts_DelayRel2.setMaxAccess(_D)
if mibBuilder.loadTexts:sts_DelayRel2.setStatus(_A)
class _Sts_OverTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(358,358))
_Sts_OverTemp_Type.__name__=_B
_Sts_OverTemp_Object=MibScalar
sts_OverTemp=_Sts_OverTemp_Object((1,3,6,1,4,1,16460,4,2,2,3,27),_Sts_OverTemp_Type())
sts_OverTemp.setMaxAccess(_E)
if mibBuilder.loadTexts:sts_OverTemp.setStatus(_A)
_ExtendedSettings_ObjectIdentity=ObjectIdentity
extendedSettings=_ExtendedSettings_ObjectIdentity((1,3,6,1,4,1,16460,4,3))
_NetSyncronisationSet_ObjectIdentity=ObjectIdentity
netSyncronisationSet=_NetSyncronisationSet_ObjectIdentity((1,3,6,1,4,1,16460,4,3,1))
class _Net_EdgeDetectionDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_Net_EdgeDetectionDelay_Type.__name__=_B
_Net_EdgeDetectionDelay_Object=MibScalar
net_EdgeDetectionDelay=_Net_EdgeDetectionDelay_Object((1,3,6,1,4,1,16460,4,3,1,1),_Net_EdgeDetectionDelay_Type())
net_EdgeDetectionDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:net_EdgeDetectionDelay.setStatus(_A)
class _Net_TimeOutDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_Net_TimeOutDelay_Type.__name__=_B
_Net_TimeOutDelay_Object=MibScalar
net_TimeOutDelay=_Net_TimeOutDelay_Object((1,3,6,1,4,1,16460,4,3,1,2),_Net_TimeOutDelay_Type())
net_TimeOutDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:net_TimeOutDelay.setStatus(_A)
class _Net_MaxCorrPhi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Net_MaxCorrPhi_Type.__name__=_B
_Net_MaxCorrPhi_Object=MibScalar
net_MaxCorrPhi=_Net_MaxCorrPhi_Object((1,3,6,1,4,1,16460,4,3,1,3),_Net_MaxCorrPhi_Type())
net_MaxCorrPhi.setMaxAccess(_D)
if mibBuilder.loadTexts:net_MaxCorrPhi.setStatus(_A)
class _Net_DivDeltaPhi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Net_DivDeltaPhi_Type.__name__=_B
_Net_DivDeltaPhi_Object=MibScalar
net_DivDeltaPhi=_Net_DivDeltaPhi_Object((1,3,6,1,4,1,16460,4,3,1,4),_Net_DivDeltaPhi_Type())
net_DivDeltaPhi.setMaxAccess(_D)
if mibBuilder.loadTexts:net_DivDeltaPhi.setStatus(_A)
class _Net_DivCorrPhi_I_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Net_DivCorrPhi_I_Type.__name__=_B
_Net_DivCorrPhi_I_Object=MibScalar
net_DivCorrPhi_I=_Net_DivCorrPhi_I_Object((1,3,6,1,4,1,16460,4,3,1,5),_Net_DivCorrPhi_I_Type())
net_DivCorrPhi_I.setMaxAccess(_D)
if mibBuilder.loadTexts:net_DivCorrPhi_I.setStatus(_A)
class _Net_MaxCorrT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Net_MaxCorrT_Type.__name__=_B
_Net_MaxCorrT_Object=MibScalar
net_MaxCorrT=_Net_MaxCorrT_Object((1,3,6,1,4,1,16460,4,3,1,6),_Net_MaxCorrT_Type())
net_MaxCorrT.setMaxAccess(_D)
if mibBuilder.loadTexts:net_MaxCorrT.setStatus(_A)
class _Net_DivDeltaT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Net_DivDeltaT_Type.__name__=_B
_Net_DivDeltaT_Object=MibScalar
net_DivDeltaT=_Net_DivDeltaT_Object((1,3,6,1,4,1,16460,4,3,1,7),_Net_DivDeltaT_Type())
net_DivDeltaT.setMaxAccess(_D)
if mibBuilder.loadTexts:net_DivDeltaT.setStatus(_A)
class _Net_SyncOKNr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Net_SyncOKNr_Type.__name__=_B
_Net_SyncOKNr_Object=MibScalar
net_SyncOKNr=_Net_SyncOKNr_Object((1,3,6,1,4,1,16460,4,3,1,8),_Net_SyncOKNr_Type())
net_SyncOKNr.setMaxAccess(_D)
if mibBuilder.loadTexts:net_SyncOKNr.setStatus(_A)
class _Net_SyncErrorNr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Net_SyncErrorNr_Type.__name__=_B
_Net_SyncErrorNr_Object=MibScalar
net_SyncErrorNr=_Net_SyncErrorNr_Object((1,3,6,1,4,1,16460,4,3,1,9),_Net_SyncErrorNr_Type())
net_SyncErrorNr.setMaxAccess(_D)
if mibBuilder.loadTexts:net_SyncErrorNr.setStatus(_A)
class _Net_P_Diff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,15000))
_Net_P_Diff_Type.__name__=_B
_Net_P_Diff_Object=MibScalar
net_P_Diff=_Net_P_Diff_Object((1,3,6,1,4,1,16460,4,3,1,10),_Net_P_Diff_Type())
net_P_Diff.setMaxAccess(_D)
if mibBuilder.loadTexts:net_P_Diff.setStatus(_A)
_AdjustValues_ObjectIdentity=ObjectIdentity
adjustValues=_AdjustValues_ObjectIdentity((1,3,6,1,4,1,16460,4,3,2))
class _Adj_UMains_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(368,432))
_Adj_UMains_Type.__name__=_B
_Adj_UMains_Object=MibScalar
adj_UMains=_Adj_UMains_Object((1,3,6,1,4,1,16460,4,3,2,1),_Adj_UMains_Type())
adj_UMains.setMaxAccess(_D)
if mibBuilder.loadTexts:adj_UMains.setStatus(_A)
class _Adj_UInv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(368,432))
_Adj_UInv_Type.__name__=_B
_Adj_UInv_Object=MibScalar
adj_UInv=_Adj_UInv_Object((1,3,6,1,4,1,16460,4,3,2,2),_Adj_UInv_Type())
adj_UInv.setMaxAccess(_D)
if mibBuilder.loadTexts:adj_UInv.setStatus(_A)
class _Adj_UDC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1372,1628))
_Adj_UDC_Type.__name__=_B
_Adj_UDC_Object=MibScalar
adj_UDC=_Adj_UDC_Object((1,3,6,1,4,1,16460,4,3,2,3),_Adj_UDC_Type())
adj_UDC.setMaxAccess(_D)
if mibBuilder.loadTexts:adj_UDC.setStatus(_A)
class _Adj_Uout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(368,432))
_Adj_Uout_Type.__name__=_B
_Adj_Uout_Object=MibScalar
adj_Uout=_Adj_Uout_Object((1,3,6,1,4,1,16460,4,3,2,4),_Adj_Uout_Type())
adj_Uout.setMaxAccess(_D)
if mibBuilder.loadTexts:adj_Uout.setStatus(_A)
class _Adj_Iout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1988,3012))
_Adj_Iout_Type.__name__=_B
_Adj_Iout_Object=MibScalar
adj_Iout=_Adj_Iout_Object((1,3,6,1,4,1,16460,4,3,2,5),_Adj_Iout_Type())
adj_Iout.setMaxAccess(_D)
if mibBuilder.loadTexts:adj_Iout.setStatus(_A)
_Tables_ObjectIdentity=ObjectIdentity
tables=_Tables_ObjectIdentity((1,3,6,1,4,1,16460,4,4))
_HistoryTable_Object=MibTable
historyTable=_HistoryTable_Object((1,3,6,1,4,1,16460,4,4,1))
if mibBuilder.loadTexts:historyTable.setStatus(_A)
_HistoryEntry_Object=MibTableRow
historyEntry=_HistoryEntry_Object((1,3,6,1,4,1,16460,4,4,1,1))
historyEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:historyEntry.setStatus(_M)
class _HistIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_HistIndex_Type.__name__=_B
_HistIndex_Object=MibTableColumn
histIndex=_HistIndex_Object((1,3,6,1,4,1,16460,4,4,1,1,0),_HistIndex_Type())
histIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:histIndex.setStatus(_N)
if mibBuilder.loadTexts:histIndex.setUnits('NA')
class _HistInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HistInd_Type.__name__=_B
_HistInd_Object=MibTableColumn
histInd=_HistInd_Object((1,3,6,1,4,1,16460,4,4,1,1,1),_HistInd_Type())
histInd.setMaxAccess(_E)
if mibBuilder.loadTexts:histInd.setStatus(_A)
class _HistDateTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400000000))
_HistDateTime_Type.__name__=_B
_HistDateTime_Object=MibTableColumn
histDateTime=_HistDateTime_Object((1,3,6,1,4,1,16460,4,4,1,1,2),_HistDateTime_Type())
histDateTime.setMaxAccess(_E)
if mibBuilder.loadTexts:histDateTime.setStatus(_A)
class _HistEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HistEvent_Type.__name__=_B
_HistEvent_Object=MibTableColumn
histEvent=_HistEvent_Object((1,3,6,1,4,1,16460,4,4,1,1,3),_HistEvent_Type())
histEvent.setMaxAccess(_E)
if mibBuilder.loadTexts:histEvent.setStatus(_A)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,16460,4,5))
_TrapLastMessageStringTest_Type=OctetString
_TrapLastMessageStringTest_Object=MibScalar
trapLastMessageStringTest=_TrapLastMessageStringTest_Object((1,3,6,1,4,1,16460,4,5,1),_TrapLastMessageStringTest_Type())
trapLastMessageStringTest.setMaxAccess(_F)
if mibBuilder.loadTexts:trapLastMessageStringTest.setStatus(_A)
class _TrapLastMessageNbrTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,46))
_TrapLastMessageNbrTest_Type.__name__=_B
_TrapLastMessageNbrTest_Object=MibScalar
trapLastMessageNbrTest=_TrapLastMessageNbrTest_Object((1,3,6,1,4,1,16460,4,5,2),_TrapLastMessageNbrTest_Type())
trapLastMessageNbrTest.setMaxAccess(_F)
if mibBuilder.loadTexts:trapLastMessageNbrTest.setStatus(_A)
_TrapSourceIPTest_Type=IpAddress
_TrapSourceIPTest_Object=MibScalar
trapSourceIPTest=_TrapSourceIPTest_Object((1,3,6,1,4,1,16460,4,5,3),_TrapSourceIPTest_Type())
trapSourceIPTest.setMaxAccess(_F)
if mibBuilder.loadTexts:trapSourceIPTest.setStatus(_A)
class _Trap_source_mains_failue_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_source_mains_failue_present_Type.__name__=_B
_Trap_source_mains_failue_present_Object=MibScalar
trap_source_mains_failue_present=_Trap_source_mains_failue_present_Object((1,3,6,1,4,1,16460,4,5,17),_Trap_source_mains_failue_present_Type())
trap_source_mains_failue_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_source_mains_failue_present.setStatus(_A)
class _Trap_source_inverter_failure_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_source_inverter_failure_present_Type.__name__=_B
_Trap_source_inverter_failure_present_Object=MibScalar
trap_source_inverter_failure_present=_Trap_source_inverter_failure_present_Object((1,3,6,1,4,1,16460,4,5,18),_Trap_source_inverter_failure_present_Type())
trap_source_inverter_failure_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_source_inverter_failure_present.setStatus(_A)
class _Trap_syncronisation_error_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_syncronisation_error_present_Type.__name__=_B
_Trap_syncronisation_error_present_Object=MibScalar
trap_syncronisation_error_present=_Trap_syncronisation_error_present_Object((1,3,6,1,4,1,16460,4,5,19),_Trap_syncronisation_error_present_Type())
trap_syncronisation_error_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_syncronisation_error_present.setStatus(_A)
class _Trap_inverter_failure_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_inverter_failure_present_Type.__name__=_B
_Trap_inverter_failure_present_Object=MibScalar
trap_inverter_failure_present=_Trap_inverter_failure_present_Object((1,3,6,1,4,1,16460,4,5,20),_Trap_inverter_failure_present_Type())
trap_inverter_failure_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_inverter_failure_present.setStatus(_A)
class _Trap_no_redundant_inverter_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_no_redundant_inverter_present_Type.__name__=_B
_Trap_no_redundant_inverter_present_Object=MibScalar
trap_no_redundant_inverter_present=_Trap_no_redundant_inverter_present_Object((1,3,6,1,4,1,16460,4,5,21),_Trap_no_redundant_inverter_present_Type())
trap_no_redundant_inverter_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_no_redundant_inverter_present.setStatus(_A)
class _Trap_critical_inverter_quantity_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_critical_inverter_quantity_present_Type.__name__=_B
_Trap_critical_inverter_quantity_present_Object=MibScalar
trap_critical_inverter_quantity_present=_Trap_critical_inverter_quantity_present_Object((1,3,6,1,4,1,16460,4,5,22),_Trap_critical_inverter_quantity_present_Type())
trap_critical_inverter_quantity_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_critical_inverter_quantity_present.setStatus(_A)
class _Trap_sts_overtemperature_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_sts_overtemperature_present_Type.__name__=_B
_Trap_sts_overtemperature_present_Object=MibScalar
trap_sts_overtemperature_present=_Trap_sts_overtemperature_present_Object((1,3,6,1,4,1,16460,4,5,23),_Trap_sts_overtemperature_present_Type())
trap_sts_overtemperature_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_sts_overtemperature_present.setStatus(_A)
class _Trap_sts_overload_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_sts_overload_present_Type.__name__=_B
_Trap_sts_overload_present_Object=MibScalar
trap_sts_overload_present=_Trap_sts_overload_present_Object((1,3,6,1,4,1,16460,4,5,24),_Trap_sts_overload_present_Type())
trap_sts_overload_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_sts_overload_present.setStatus(_A)
class _Trap_inverter_overload_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_inverter_overload_present_Type.__name__=_B
_Trap_inverter_overload_present_Object=MibScalar
trap_inverter_overload_present=_Trap_inverter_overload_present_Object((1,3,6,1,4,1,16460,4,5,25),_Trap_inverter_overload_present_Type())
trap_inverter_overload_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_inverter_overload_present.setStatus(_A)
class _Trap_sts_current_need_redandancy_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_sts_current_need_redandancy_present_Type.__name__=_B
_Trap_sts_current_need_redandancy_present_Object=MibScalar
trap_sts_current_need_redandancy_present=_Trap_sts_current_need_redandancy_present_Object((1,3,6,1,4,1,16460,4,5,26),_Trap_sts_current_need_redandancy_present_Type())
trap_sts_current_need_redandancy_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_sts_current_need_redandancy_present.setStatus(_A)
class _Trap_dc_voltage_low_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_dc_voltage_low_present_Type.__name__=_B
_Trap_dc_voltage_low_present_Object=MibScalar
trap_dc_voltage_low_present=_Trap_dc_voltage_low_present_Object((1,3,6,1,4,1,16460,4,5,27),_Trap_dc_voltage_low_present_Type())
trap_dc_voltage_low_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_dc_voltage_low_present.setStatus(_A)
class _Trap_dc_voltage_high_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_dc_voltage_high_present_Type.__name__=_B
_Trap_dc_voltage_high_present_Object=MibScalar
trap_dc_voltage_high_present=_Trap_dc_voltage_high_present_Object((1,3,6,1,4,1,16460,4,5,28),_Trap_dc_voltage_high_present_Type())
trap_dc_voltage_high_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_dc_voltage_high_present.setStatus(_A)
class _Trap_fan_error_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_fan_error_present_Type.__name__=_B
_Trap_fan_error_present_Object=MibScalar
trap_fan_error_present=_Trap_fan_error_present_Object((1,3,6,1,4,1,16460,4,5,29),_Trap_fan_error_present_Type())
trap_fan_error_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_fan_error_present.setStatus(_A)
class _Trap_uout_low_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_uout_low_present_Type.__name__=_B
_Trap_uout_low_present_Object=MibScalar
trap_uout_low_present=_Trap_uout_low_present_Object((1,3,6,1,4,1,16460,4,5,30),_Trap_uout_low_present_Type())
trap_uout_low_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_uout_low_present.setStatus(_A)
class _Trap_u_batterie_lower_warning_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_u_batterie_lower_warning_present_Type.__name__=_B
_Trap_u_batterie_lower_warning_present_Object=MibScalar
trap_u_batterie_lower_warning_present=_Trap_u_batterie_lower_warning_present_Object((1,3,6,1,4,1,16460,4,5,31),_Trap_u_batterie_lower_warning_present_Type())
trap_u_batterie_lower_warning_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_u_batterie_lower_warning_present.setStatus(_A)
class _Trap_u_batterie_higher_warning_present_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_u_batterie_higher_warning_present_Type.__name__=_B
_Trap_u_batterie_higher_warning_present_Object=MibScalar
trap_u_batterie_higher_warning_present=_Trap_u_batterie_higher_warning_present_Object((1,3,6,1,4,1,16460,4,5,32),_Trap_u_batterie_higher_warning_present_Type())
trap_u_batterie_higher_warning_present.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_u_batterie_higher_warning_present.setStatus(_A)
class _Trap_source_mains_failure_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_source_mains_failure_removed_Type.__name__=_B
_Trap_source_mains_failure_removed_Object=MibScalar
trap_source_mains_failure_removed=_Trap_source_mains_failure_removed_Object((1,3,6,1,4,1,16460,4,5,33),_Trap_source_mains_failure_removed_Type())
trap_source_mains_failure_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_source_mains_failure_removed.setStatus(_A)
class _Trap_source_inverter_failure_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_source_inverter_failure_removed_Type.__name__=_B
_Trap_source_inverter_failure_removed_Object=MibScalar
trap_source_inverter_failure_removed=_Trap_source_inverter_failure_removed_Object((1,3,6,1,4,1,16460,4,5,34),_Trap_source_inverter_failure_removed_Type())
trap_source_inverter_failure_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_source_inverter_failure_removed.setStatus(_A)
class _Trap_syncronisation_error_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_syncronisation_error_removed_Type.__name__=_B
_Trap_syncronisation_error_removed_Object=MibScalar
trap_syncronisation_error_removed=_Trap_syncronisation_error_removed_Object((1,3,6,1,4,1,16460,4,5,35),_Trap_syncronisation_error_removed_Type())
trap_syncronisation_error_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_syncronisation_error_removed.setStatus(_A)
class _Trap_inverter_failure_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_inverter_failure_removed_Type.__name__=_B
_Trap_inverter_failure_removed_Object=MibScalar
trap_inverter_failure_removed=_Trap_inverter_failure_removed_Object((1,3,6,1,4,1,16460,4,5,36),_Trap_inverter_failure_removed_Type())
trap_inverter_failure_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_inverter_failure_removed.setStatus(_A)
class _Trap_no_redundant_inverter_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_no_redundant_inverter_removed_Type.__name__=_B
_Trap_no_redundant_inverter_removed_Object=MibScalar
trap_no_redundant_inverter_removed=_Trap_no_redundant_inverter_removed_Object((1,3,6,1,4,1,16460,4,5,37),_Trap_no_redundant_inverter_removed_Type())
trap_no_redundant_inverter_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_no_redundant_inverter_removed.setStatus(_A)
class _Trap_critical_inverter_quantity_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_critical_inverter_quantity_removed_Type.__name__=_B
_Trap_critical_inverter_quantity_removed_Object=MibScalar
trap_critical_inverter_quantity_removed=_Trap_critical_inverter_quantity_removed_Object((1,3,6,1,4,1,16460,4,5,38),_Trap_critical_inverter_quantity_removed_Type())
trap_critical_inverter_quantity_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_critical_inverter_quantity_removed.setStatus(_A)
class _Trap_sts_overtemperature_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_sts_overtemperature_removed_Type.__name__=_B
_Trap_sts_overtemperature_removed_Object=MibScalar
trap_sts_overtemperature_removed=_Trap_sts_overtemperature_removed_Object((1,3,6,1,4,1,16460,4,5,39),_Trap_sts_overtemperature_removed_Type())
trap_sts_overtemperature_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_sts_overtemperature_removed.setStatus(_A)
class _Trap_sts_overload_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_sts_overload_removed_Type.__name__=_B
_Trap_sts_overload_removed_Object=MibScalar
trap_sts_overload_removed=_Trap_sts_overload_removed_Object((1,3,6,1,4,1,16460,4,5,40),_Trap_sts_overload_removed_Type())
trap_sts_overload_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_sts_overload_removed.setStatus(_A)
class _Trap_inverter_overload_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_inverter_overload_removed_Type.__name__=_B
_Trap_inverter_overload_removed_Object=MibScalar
trap_inverter_overload_removed=_Trap_inverter_overload_removed_Object((1,3,6,1,4,1,16460,4,5,41),_Trap_inverter_overload_removed_Type())
trap_inverter_overload_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_inverter_overload_removed.setStatus(_A)
class _Trap_sts_current_need_redandancy_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_sts_current_need_redandancy_removed_Type.__name__=_B
_Trap_sts_current_need_redandancy_removed_Object=MibScalar
trap_sts_current_need_redandancy_removed=_Trap_sts_current_need_redandancy_removed_Object((1,3,6,1,4,1,16460,4,5,42),_Trap_sts_current_need_redandancy_removed_Type())
trap_sts_current_need_redandancy_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_sts_current_need_redandancy_removed.setStatus(_A)
class _Trap_dc_voltage_low_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_dc_voltage_low_removed_Type.__name__=_B
_Trap_dc_voltage_low_removed_Object=MibScalar
trap_dc_voltage_low_removed=_Trap_dc_voltage_low_removed_Object((1,3,6,1,4,1,16460,4,5,43),_Trap_dc_voltage_low_removed_Type())
trap_dc_voltage_low_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_dc_voltage_low_removed.setStatus(_A)
class _Trap_dc_voltage_high_added_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_dc_voltage_high_added_removed_Type.__name__=_B
_Trap_dc_voltage_high_added_removed_Object=MibScalar
trap_dc_voltage_high_added_removed=_Trap_dc_voltage_high_added_removed_Object((1,3,6,1,4,1,16460,4,5,44),_Trap_dc_voltage_high_added_removed_Type())
trap_dc_voltage_high_added_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_dc_voltage_high_added_removed.setStatus(_A)
class _Trap_fan_error_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_fan_error_removed_Type.__name__=_B
_Trap_fan_error_removed_Object=MibScalar
trap_fan_error_removed=_Trap_fan_error_removed_Object((1,3,6,1,4,1,16460,4,5,45),_Trap_fan_error_removed_Type())
trap_fan_error_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_fan_error_removed.setStatus(_A)
class _Trap_uout_low_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_uout_low_removed_Type.__name__=_B
_Trap_uout_low_removed_Object=MibScalar
trap_uout_low_removed=_Trap_uout_low_removed_Object((1,3,6,1,4,1,16460,4,5,46),_Trap_uout_low_removed_Type())
trap_uout_low_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_uout_low_removed.setStatus(_A)
class _Trap_u_batterie_lower_warning_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_u_batterie_lower_warning_removed_Type.__name__=_B
_Trap_u_batterie_lower_warning_removed_Object=MibScalar
trap_u_batterie_lower_warning_removed=_Trap_u_batterie_lower_warning_removed_Object((1,3,6,1,4,1,16460,4,5,47),_Trap_u_batterie_lower_warning_removed_Type())
trap_u_batterie_lower_warning_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_u_batterie_lower_warning_removed.setStatus(_A)
class _Trap_u_batterie_higher_warning_removed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Trap_u_batterie_higher_warning_removed_Type.__name__=_B
_Trap_u_batterie_higher_warning_removed_Object=MibScalar
trap_u_batterie_higher_warning_removed=_Trap_u_batterie_higher_warning_removed_Object((1,3,6,1,4,1,16460,4,5,48),_Trap_u_batterie_higher_warning_removed_Type())
trap_u_batterie_higher_warning_removed.setMaxAccess(_F)
if mibBuilder.loadTexts:trap_u_batterie_higher_warning_removed.setStatus(_A)
source_mains_failue_present_trap=NotificationType((1,3,6,1,4,1,16460,0,16))
source_mains_failue_present_trap.setObjects(*((_C,_P),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:source_mains_failue_present_trap.setStatus('')
source_inverter_failure_present=NotificationType((1,3,6,1,4,1,16460,0,17))
source_inverter_failure_present.setObjects(*((_C,_Q),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:source_inverter_failure_present.setStatus('')
syncronisation_error_present=NotificationType((1,3,6,1,4,1,16460,0,18))
syncronisation_error_present.setObjects(*((_C,_R),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:syncronisation_error_present.setStatus('')
inverter_failure_present=NotificationType((1,3,6,1,4,1,16460,0,19))
inverter_failure_present.setObjects(*((_C,_S),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:inverter_failure_present.setStatus('')
no_redundant_inverter_present=NotificationType((1,3,6,1,4,1,16460,0,20))
no_redundant_inverter_present.setObjects(*((_C,_T),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:no_redundant_inverter_present.setStatus('')
critical_inverter_quantity_present=NotificationType((1,3,6,1,4,1,16460,0,21))
critical_inverter_quantity_present.setObjects(*((_C,_U),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:critical_inverter_quantity_present.setStatus('')
sts_overtemperature_present=NotificationType((1,3,6,1,4,1,16460,0,22))
sts_overtemperature_present.setObjects(*((_C,_V),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:sts_overtemperature_present.setStatus('')
sts_overload_present=NotificationType((1,3,6,1,4,1,16460,0,23))
sts_overload_present.setObjects(*((_C,_W),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:sts_overload_present.setStatus('')
inverter_overload_present=NotificationType((1,3,6,1,4,1,16460,0,24))
inverter_overload_present.setObjects(*((_C,_X),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:inverter_overload_present.setStatus('')
sts_current_need_redandancy_present=NotificationType((1,3,6,1,4,1,16460,0,25))
sts_current_need_redandancy_present.setObjects(*((_C,_Y),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:sts_current_need_redandancy_present.setStatus('')
dc_voltage_low_present=NotificationType((1,3,6,1,4,1,16460,0,26))
dc_voltage_low_present.setObjects(*((_C,_Z),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:dc_voltage_low_present.setStatus('')
dc_voltage_high_present=NotificationType((1,3,6,1,4,1,16460,0,27))
dc_voltage_high_present.setObjects(*((_C,_a),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:dc_voltage_high_present.setStatus('')
fan_error_present=NotificationType((1,3,6,1,4,1,16460,0,28))
fan_error_present.setObjects(*((_C,_b),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:fan_error_present.setStatus('')
uout_low_present=NotificationType((1,3,6,1,4,1,16460,0,29))
uout_low_present.setObjects(*((_C,_c),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:uout_low_present.setStatus('')
u_batterie_lower_warning_present=NotificationType((1,3,6,1,4,1,16460,0,30))
u_batterie_lower_warning_present.setObjects(*((_C,_d),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:u_batterie_lower_warning_present.setStatus('')
u_batterie_higher_warning_present=NotificationType((1,3,6,1,4,1,16460,0,31))
u_batterie_higher_warning_present.setObjects(*((_C,_e),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:u_batterie_higher_warning_present.setStatus('')
source_mains_failure_removed=NotificationType((1,3,6,1,4,1,16460,0,32))
source_mains_failure_removed.setObjects(*((_C,_f),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:source_mains_failure_removed.setStatus('')
source_inverter_failure_removed=NotificationType((1,3,6,1,4,1,16460,0,33))
source_inverter_failure_removed.setObjects(*((_C,_g),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:source_inverter_failure_removed.setStatus('')
syncronisation_error_removed=NotificationType((1,3,6,1,4,1,16460,0,34))
syncronisation_error_removed.setObjects(*((_C,_h),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:syncronisation_error_removed.setStatus('')
inverter_failure_removed=NotificationType((1,3,6,1,4,1,16460,0,35))
inverter_failure_removed.setObjects(*((_C,_i),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:inverter_failure_removed.setStatus('')
no_redundant_inverter_removed=NotificationType((1,3,6,1,4,1,16460,0,36))
no_redundant_inverter_removed.setObjects(*((_C,_j),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:no_redundant_inverter_removed.setStatus('')
critical_inverter_quantity_removed=NotificationType((1,3,6,1,4,1,16460,0,37))
critical_inverter_quantity_removed.setObjects(*((_C,_k),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:critical_inverter_quantity_removed.setStatus('')
sts_overtemperature_removed=NotificationType((1,3,6,1,4,1,16460,0,38))
sts_overtemperature_removed.setObjects(*((_C,_l),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:sts_overtemperature_removed.setStatus('')
sts_overload_removed=NotificationType((1,3,6,1,4,1,16460,0,39))
sts_overload_removed.setObjects(*((_C,_m),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:sts_overload_removed.setStatus('')
inverter_overload_removed=NotificationType((1,3,6,1,4,1,16460,0,40))
inverter_overload_removed.setObjects(*((_C,_n),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:inverter_overload_removed.setStatus('')
sts_current_need_redandancy_removed=NotificationType((1,3,6,1,4,1,16460,0,41))
sts_current_need_redandancy_removed.setObjects(*((_C,_o),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:sts_current_need_redandancy_removed.setStatus('')
dc_voltage_low_removed=NotificationType((1,3,6,1,4,1,16460,0,42))
dc_voltage_low_removed.setObjects(*((_C,_p),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:dc_voltage_low_removed.setStatus('')
dc_voltage_high_added_removed=NotificationType((1,3,6,1,4,1,16460,0,43))
dc_voltage_high_added_removed.setObjects(*((_C,_q),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:dc_voltage_high_added_removed.setStatus('')
fan_error_removed=NotificationType((1,3,6,1,4,1,16460,0,44))
fan_error_removed.setObjects(*((_C,_r),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:fan_error_removed.setStatus('')
uout_low_removed=NotificationType((1,3,6,1,4,1,16460,0,45))
uout_low_removed.setObjects(*((_C,_s),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:uout_low_removed.setStatus('')
u_batterie_lower_warning_removed=NotificationType((1,3,6,1,4,1,16460,0,46))
u_batterie_lower_warning_removed.setObjects(*((_C,_t),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:u_batterie_lower_warning_removed.setStatus('')
u_batterie_higher_warning_removed=NotificationType((1,3,6,1,4,1,16460,0,47))
u_batterie_higher_warning_removed.setObjects(*((_C,_u),(_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:u_batterie_higher_warning_removed.setStatus('')
mibBuilder.exportSymbols(_C,**{'convertronic':convertronic,'source_mains_failue_present_trap':source_mains_failue_present_trap,'source_inverter_failure_present':source_inverter_failure_present,'syncronisation_error_present':syncronisation_error_present,'inverter_failure_present':inverter_failure_present,'no_redundant_inverter_present':no_redundant_inverter_present,'critical_inverter_quantity_present':critical_inverter_quantity_present,'sts_overtemperature_present':sts_overtemperature_present,'sts_overload_present':sts_overload_present,'inverter_overload_present':inverter_overload_present,'sts_current_need_redandancy_present':sts_current_need_redandancy_present,'dc_voltage_low_present':dc_voltage_low_present,'dc_voltage_high_present':dc_voltage_high_present,'fan_error_present':fan_error_present,'uout_low_present':uout_low_present,'u_batterie_lower_warning_present':u_batterie_lower_warning_present,'u_batterie_higher_warning_present':u_batterie_higher_warning_present,'source_mains_failure_removed':source_mains_failure_removed,'source_inverter_failure_removed':source_inverter_failure_removed,'syncronisation_error_removed':syncronisation_error_removed,'inverter_failure_removed':inverter_failure_removed,'no_redundant_inverter_removed':no_redundant_inverter_removed,'critical_inverter_quantity_removed':critical_inverter_quantity_removed,'sts_overtemperature_removed':sts_overtemperature_removed,'sts_overload_removed':sts_overload_removed,'inverter_overload_removed':inverter_overload_removed,'sts_current_need_redandancy_removed':sts_current_need_redandancy_removed,'dc_voltage_low_removed':dc_voltage_low_removed,'dc_voltage_high_added_removed':dc_voltage_high_added_removed,'fan_error_removed':fan_error_removed,'uout_low_removed':uout_low_removed,'u_batterie_lower_warning_removed':u_batterie_lower_warning_removed,'u_batterie_higher_warning_removed':u_batterie_higher_warning_removed,'sts_system':sts_system,'measureValues':measureValues,'sts_measureValues':sts_measureValues,'sVal_UN':sVal_UN,'sVal_FreqNetz':sVal_FreqNetz,'sVal_UWR':sVal_UWR,'sVal_FreqWR':sVal_FreqWR,'sVal_UDC':sVal_UDC,'sVal_U10':sVal_U10,'sVal_IO1':sVal_IO1,'sVal_P':sVal_P,'sVal_S':sVal_S,'sVal_FAN1':sVal_FAN1,'sVal_FAN2':sVal_FAN2,'sVal_TK':sVal_TK,'sVal_IO2':sVal_IO2,'sVal_IDC':sVal_IDC,'inverter_measureValues':inverter_measureValues,'inverter_Table':inverter_Table,'inverter_Entry':inverter_Entry,_L:inv_Index,'inv_Nbr':inv_Nbr,'inv_InCurrent':inv_InCurrent,'inv_OutCurrent':inv_OutCurrent,'inv_Temperature':inv_Temperature,'inv_InputVoltage':inv_InputVoltage,'inv_STi_great':inv_STi_great,'inv_Fan':inv_Fan,'inv_RemoteOffCan':inv_RemoteOffCan,'inv_UoutOff':inv_UoutOff,'inv_Bit_ShortCircuit':inv_Bit_ShortCircuit,'inv_Bit_OutputVoltage':inv_Bit_OutputVoltage,'inv_Bit_InputVoltLow':inv_Bit_InputVoltLow,'inv_Bit_InputVoltHigh':inv_Bit_InputVoltHigh,'inv_Bit_OutputVoltLow':inv_Bit_OutputVoltLow,'inv_Bit_OutputVoltHigh':inv_Bit_OutputVoltHigh,'inv_Bit_OutputCurrHigh':inv_Bit_OutputCurrHigh,'inv_Bit_RemoteOff':inv_Bit_RemoteOff,'inv_Bit_CentralAlarm':inv_Bit_CentralAlarm,'inv_Type':inv_Type,'inv_Mat_CD':inv_Mat_CD,'inv_SerialNo':inv_SerialNo,'inv_HardwareVersion':inv_HardwareVersion,'inv_SoftwareVersion':inv_SoftwareVersion,'settings':settings,'networkSettings':networkSettings,'baseSettings':baseSettings,'bETHSpeed':bETHSpeed,'bLocalIP':bLocalIP,'bSubnetMask':bSubnetMask,'bGateway':bGateway,'bDNSServer':bDNSServer,'bDHCPServer':bDHCPServer,'bFixedIP_OnOff':bFixedIP_OnOff,'bDefaultIP_OnOff':bDefaultIP_OnOff,'bDHCP_OnOff':bDHCP_OnOff,'bBOOTP_OnOff':bBOOTP_OnOff,'bLocation':bLocation,'serviceSettings':serviceSettings,'servSNMP_OnOff':servSNMP_OnOff,'servTrapReceiver1':servTrapReceiver1,'servTrapReceiver2':servTrapReceiver2,'servTrapReceiver3':servTrapReceiver3,'servTrapReceiver4':servTrapReceiver4,'servReadCommunity':servReadCommunity,'servWriteCommunity':servWriteCommunity,'servSMTP_OnOff':servSMTP_OnOff,'servMailServer':servMailServer,'servMailUsername':servMailUsername,'servMailPassword':servMailPassword,'servMailReceiver1':servMailReceiver1,'servMailTrapLevel1':servMailTrapLevel1,'servMailReceiver2':servMailReceiver2,'servMailTrapLevel2':servMailTrapLevel2,'servSNTP_OnOff':servSNTP_OnOff,'servSNTPServer1':servSNTPServer1,'servSNTPServer2':servSNTPServer2,'servTelnet_OnOff':servTelnet_OnOff,'servSyslog_OnOff':servSyslog_OnOff,'unitSettings':unitSettings,'basicSettings':basicSettings,'sts_Version':sts_Version,'sts_Inverter':sts_Inverter,'sts_SigCF_b0':sts_SigCF_b0,'sts_SigCF_b1':sts_SigCF_b1,'sts_SigCF_b2':sts_SigCF_b2,'sts_SigCF_b3':sts_SigCF_b3,'sts_SigCF_b4':sts_SigCF_b4,'sts_SigCF_b5':sts_SigCF_b5,'sts_SigCF_b6':sts_SigCF_b6,'sts_SigCF_b7':sts_SigCF_b7,'sts_SigCF_b8':sts_SigCF_b8,'sts_SigCF_b9':sts_SigCF_b9,'sts_SigCF_b10':sts_SigCF_b10,'sts_SigCF_b11':sts_SigCF_b11,'sts_SigCF_b12':sts_SigCF_b12,'sts_SigCF_b13':sts_SigCF_b13,'sts_SigCF_b14':sts_SigCF_b14,'sts_SigCF_b15':sts_SigCF_b15,'sts_DelayRelCA':sts_DelayRelCA,'sts_DelayLEDCA':sts_DelayLEDCA,'sts_LCDContrast':sts_LCDContrast,'sts_Language':sts_Language,'advancedSettings':advancedSettings,'sts_OpMode':sts_OpMode,'sts_UpperSwitchLimS1':sts_UpperSwitchLimS1,'sts_LowerSwitchLimS1':sts_LowerSwitchLimS1,'sts_SwitchDelayS1':sts_SwitchDelayS1,'sts_UpperSwitchLimS2':sts_UpperSwitchLimS2,'sts_LowerSwitchLimS2':sts_LowerSwitchLimS2,'sts_SwitchDelayS2':sts_SwitchDelayS2,'sts_MaxCellVolt1':sts_MaxCellVolt1,'sts_MinCellVolt1':sts_MinCellVolt1,'sts_MinCellVolt2':sts_MinCellVolt2,'sts_MinULimit':sts_MinULimit,'sts_MaxULimit':sts_MaxULimit,'advancedSettings2':advancedSettings2,'sts_NomPower':sts_NomPower,'sts_NomVolt':sts_NomVolt,'sts_NomFreq':sts_NomFreq,'sts_FreqRange':sts_FreqRange,'sts_MaxCurrent':sts_MaxCurrent,'sts_PresentCell':sts_PresentCell,'sts_CellVoltage':sts_CellVoltage,'sts_Adress':sts_Adress,'sts_SigRel2_b0':sts_SigRel2_b0,'sts_SigRel2_b1':sts_SigRel2_b1,'sts_SigRel2_b2':sts_SigRel2_b2,'sts_SigRel2_b3':sts_SigRel2_b3,'sts_SigRel2_b4':sts_SigRel2_b4,'sts_SigRel2_b5':sts_SigRel2_b5,'sts_SigRel2_b6':sts_SigRel2_b6,'sts_SigRel2_b7':sts_SigRel2_b7,'sts_SigRel2_b8':sts_SigRel2_b8,'sts_SigRel2_b9':sts_SigRel2_b9,'sts_SigRel2_b10':sts_SigRel2_b10,'sts_SigRel2_b11':sts_SigRel2_b11,'sts_SigRel2_b12':sts_SigRel2_b12,'sts_SigRel2_b13':sts_SigRel2_b13,'sts_SigRel2_b14':sts_SigRel2_b14,'sts_SigRel2_b15':sts_SigRel2_b15,'sts_ModeRel2':sts_ModeRel2,'sts_DelayRel2':sts_DelayRel2,'sts_OverTemp':sts_OverTemp,'extendedSettings':extendedSettings,'netSyncronisationSet':netSyncronisationSet,'net_EdgeDetectionDelay':net_EdgeDetectionDelay,'net_TimeOutDelay':net_TimeOutDelay,'net_MaxCorrPhi':net_MaxCorrPhi,'net_DivDeltaPhi':net_DivDeltaPhi,'net_DivCorrPhi_I':net_DivCorrPhi_I,'net_MaxCorrT':net_MaxCorrT,'net_DivDeltaT':net_DivDeltaT,'net_SyncOKNr':net_SyncOKNr,'net_SyncErrorNr':net_SyncErrorNr,'net_P_Diff':net_P_Diff,'adjustValues':adjustValues,'adj_UMains':adj_UMains,'adj_UInv':adj_UInv,'adj_UDC':adj_UDC,'adj_Uout':adj_Uout,'adj_Iout':adj_Iout,'tables':tables,'historyTable':historyTable,'historyEntry':historyEntry,_O:histIndex,'histInd':histInd,'histDateTime':histDateTime,'histEvent':histEvent,'traps':traps,_G:trapLastMessageStringTest,_H:trapLastMessageNbrTest,_I:trapSourceIPTest,_P:trap_source_mains_failue_present,_Q:trap_source_inverter_failure_present,_R:trap_syncronisation_error_present,_S:trap_inverter_failure_present,_T:trap_no_redundant_inverter_present,_U:trap_critical_inverter_quantity_present,_V:trap_sts_overtemperature_present,_W:trap_sts_overload_present,_X:trap_inverter_overload_present,_Y:trap_sts_current_need_redandancy_present,_Z:trap_dc_voltage_low_present,_a:trap_dc_voltage_high_present,_b:trap_fan_error_present,_c:trap_uout_low_present,_d:trap_u_batterie_lower_warning_present,_e:trap_u_batterie_higher_warning_present,_f:trap_source_mains_failure_removed,_g:trap_source_inverter_failure_removed,_h:trap_syncronisation_error_removed,_i:trap_inverter_failure_removed,_j:trap_no_redundant_inverter_removed,_k:trap_critical_inverter_quantity_removed,_l:trap_sts_overtemperature_removed,_m:trap_sts_overload_removed,_n:trap_inverter_overload_removed,_o:trap_sts_current_need_redandancy_removed,_p:trap_dc_voltage_low_removed,_q:trap_dc_voltage_high_added_removed,_r:trap_fan_error_removed,_s:trap_uout_low_removed,_t:trap_u_batterie_lower_warning_removed,_u:trap_u_batterie_higher_warning_removed})