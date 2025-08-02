_H='C/F x10'
_G='min'
_F='flag'
_E='read-only'
_D='N/A'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysContact,sysLocation,sysName=mibBuilder.importSymbols('SNMPv2-MIB','sysContact','sysLocation','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mcellaMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_D)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentCode.setStatus(_A)
if mibBuilder.loadTexts:agentCode.setUnits(_D)
_Instruments_ObjectIdentity=ObjectIdentity
instruments=_Instruments_ObjectIdentity((1,3,6,1,4,1,9839,2))
_WebGateInfo_ObjectIdentity=ObjectIdentity
webGateInfo=_WebGateInfo_ObjectIdentity((1,3,6,1,4,1,9839,2,0))
_AgentParameters_ObjectIdentity=ObjectIdentity
agentParameters=_AgentParameters_ObjectIdentity((1,3,6,1,4,1,9839,2,0,1))
class _NetSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NetSize_Type.__name__=_B
_NetSize_Object=MibScalar
netSize=_NetSize_Object((1,3,6,1,4,1,9839,2,0,1,1),_NetSize_Type())
netSize.setMaxAccess(_C)
if mibBuilder.loadTexts:netSize.setStatus(_A)
if mibBuilder.loadTexts:netSize.setUnits(_D)
class _BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200))
_BaudRate_Type.__name__=_B
_BaudRate_Object=MibScalar
baudRate=_BaudRate_Object((1,3,6,1,4,1,9839,2,0,1,2),_BaudRate_Type())
baudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:baudRate.setStatus(_A)
if mibBuilder.loadTexts:baudRate.setUnits(_D)
_UnitTypeGroup_ObjectIdentity=ObjectIdentity
unitTypeGroup=_UnitTypeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,2))
_Unit1_Type_Type=DisplayString
_Unit1_Type_Object=MibScalar
unit1_Type=_Unit1_Type_Object((1,3,6,1,4,1,9839,2,0,2,1),_Unit1_Type_Type())
unit1_Type.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_D)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_D)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_D)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_D)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_D)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_D)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_D)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_D)
_UnitOnLineStatusGroup_ObjectIdentity=ObjectIdentity
unitOnLineStatusGroup=_UnitOnLineStatusGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_Unit1_OnLineStatus_Type=Integer32
_Unit1_OnLineStatus_Object=MibScalar
unit1_OnLineStatus=_Unit1_OnLineStatus_Object((1,3,6,1,4,1,9839,2,0,10,1),_Unit1_OnLineStatus_Type())
unit1_OnLineStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_OnLineStatus.setStatus(_A)
if mibBuilder.loadTexts:unit1_OnLineStatus.setUnits(_D)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _Ciclo_continuo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ciclo_continuo_Type.__name__=_B
_Ciclo_continuo_Object=MibScalar
ciclo_continuo=_Ciclo_continuo_Object((1,3,6,1,4,1,9839,2,1,1,1),_Ciclo_continuo_Type())
ciclo_continuo.setMaxAccess(_E)
if mibBuilder.loadTexts:ciclo_continuo.setStatus(_A)
if mibBuilder.loadTexts:ciclo_continuo.setUnits(_D)
class _Ventilatori_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ventilatori_Type.__name__=_B
_Ventilatori_Object=MibScalar
ventilatori=_Ventilatori_Object((1,3,6,1,4,1,9839,2,1,1,2),_Ventilatori_Type())
ventilatori.setMaxAccess(_E)
if mibBuilder.loadTexts:ventilatori.setStatus(_A)
if mibBuilder.loadTexts:ventilatori.setUnits(_D)
class _Compressor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor_Type.__name__=_B
_Compressor_Object=MibScalar
compressor=_Compressor_Object((1,3,6,1,4,1,9839,2,1,1,4),_Compressor_Type())
compressor.setMaxAccess(_E)
if mibBuilder.loadTexts:compressor.setStatus(_A)
if mibBuilder.loadTexts:compressor.setUnits(_D)
class _Aux_out_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Aux_out_Type.__name__=_B
_Aux_out_Object=MibScalar
aux_out=_Aux_out_Object((1,3,6,1,4,1,9839,2,1,1,5),_Aux_out_Type())
aux_out.setMaxAccess(_C)
if mibBuilder.loadTexts:aux_out.setStatus(_A)
if mibBuilder.loadTexts:aux_out.setUnits(_D)
class _Valv_inv_ciclo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Valv_inv_ciclo_Type.__name__=_B
_Valv_inv_ciclo_Object=MibScalar
valv_inv_ciclo=_Valv_inv_ciclo_Object((1,3,6,1,4,1,9839,2,1,1,6),_Valv_inv_ciclo_Type())
valv_inv_ciclo.setMaxAccess(_E)
if mibBuilder.loadTexts:valv_inv_ciclo.setStatus(_A)
if mibBuilder.loadTexts:valv_inv_ciclo.setUnits(_D)
class _All_eeprom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_eeprom_Type.__name__=_B
_All_eeprom_Object=MibScalar
all_eeprom=_All_eeprom_Object((1,3,6,1,4,1,9839,2,1,1,8),_All_eeprom_Type())
all_eeprom.setMaxAccess(_E)
if mibBuilder.loadTexts:all_eeprom.setStatus(_A)
if mibBuilder.loadTexts:all_eeprom.setUnits(_D)
class _All_timeout_def_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_timeout_def_Type.__name__=_B
_All_timeout_def_Object=MibScalar
all_timeout_def=_All_timeout_def_Object((1,3,6,1,4,1,9839,2,1,1,9),_All_timeout_def_Type())
all_timeout_def.setMaxAccess(_E)
if mibBuilder.loadTexts:all_timeout_def.setStatus(_A)
if mibBuilder.loadTexts:all_timeout_def.setUnits(_D)
class _All_bassa_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_bassa_temp_Type.__name__=_B
_All_bassa_temp_Object=MibScalar
all_bassa_temp=_All_bassa_temp_Object((1,3,6,1,4,1,9839,2,1,1,10),_All_bassa_temp_Type())
all_bassa_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:all_bassa_temp.setStatus(_A)
if mibBuilder.loadTexts:all_bassa_temp.setUnits(_D)
class _All_alta_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_alta_temp_Type.__name__=_B
_All_alta_temp_Object=MibScalar
all_alta_temp=_All_alta_temp_Object((1,3,6,1,4,1,9839,2,1,1,11),_All_alta_temp_Type())
all_alta_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:all_alta_temp.setStatus(_A)
if mibBuilder.loadTexts:all_alta_temp.setUnits(_D)
class _All_sonda_amb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_sonda_amb_Type.__name__=_B
_All_sonda_amb_Object=MibScalar
all_sonda_amb=_All_sonda_amb_Object((1,3,6,1,4,1,9839,2,1,1,12),_All_sonda_amb_Type())
all_sonda_amb.setMaxAccess(_E)
if mibBuilder.loadTexts:all_sonda_amb.setStatus(_A)
if mibBuilder.loadTexts:all_sonda_amb.setUnits(_D)
class _All_sonda_def_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_sonda_def_Type.__name__=_B
_All_sonda_def_Object=MibScalar
all_sonda_def=_All_sonda_def_Object((1,3,6,1,4,1,9839,2,1,1,13),_All_sonda_def_Type())
all_sonda_def.setMaxAccess(_E)
if mibBuilder.loadTexts:all_sonda_def.setStatus(_A)
if mibBuilder.loadTexts:all_sonda_def.setUnits(_D)
class _All_imm_ai_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_imm_ai_Type.__name__=_B
_All_imm_ai_Object=MibScalar
all_imm_ai=_All_imm_ai_Object((1,3,6,1,4,1,9839,2,1,1,14),_All_imm_ai_Type())
all_imm_ai.setMaxAccess(_E)
if mibBuilder.loadTexts:all_imm_ai.setStatus(_A)
if mibBuilder.loadTexts:all_imm_ai.setUnits(_D)
class _All_rit_ad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_rit_ad_Type.__name__=_B
_All_rit_ad_Object=MibScalar
all_rit_ad=_All_rit_ad_Object((1,3,6,1,4,1,9839,2,1,1,15),_All_rit_ad_Type())
all_rit_ad.setMaxAccess(_E)
if mibBuilder.loadTexts:all_rit_ad.setStatus(_A)
if mibBuilder.loadTexts:all_rit_ad.setUnits(_D)
class _Sbrinam_on_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sbrinam_on_Type.__name__=_B
_Sbrinam_on_Object=MibScalar
sbrinam_on=_Sbrinam_on_Object((1,3,6,1,4,1,9839,2,1,1,17),_Sbrinam_on_Type())
sbrinam_on.setMaxAccess(_E)
if mibBuilder.loadTexts:sbrinam_on.setStatus(_A)
if mibBuilder.loadTexts:sbrinam_on.setUnits(_D)
class _C_f__5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_C_f__5_Type.__name__=_B
_C_f__5_Object=MibScalar
c_f__5=_C_f__5_Object((1,3,6,1,4,1,9839,2,1,1,26),_C_f__5_Type())
c_f__5.setMaxAccess(_C)
if mibBuilder.loadTexts:c_f__5.setStatus(_A)
if mibBuilder.loadTexts:c_f__5.setUnits(_F)
class _En_ed_alarm_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_ed_alarm_Type.__name__=_B
_En_ed_alarm_Object=MibScalar
en_ed_alarm=_En_ed_alarm_Object((1,3,6,1,4,1,9839,2,1,1,27),_En_ed_alarm_Type())
en_ed_alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:en_ed_alarm.setStatus(_A)
if mibBuilder.loadTexts:en_ed_alarm.setUnits(_F)
class _Def_uni_up_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Def_uni_up_Type.__name__=_B
_Def_uni_up_Object=MibScalar
def_uni_up=_Def_uni_up_Object((1,3,6,1,4,1,9839,2,1,1,29),_Def_uni_up_Type())
def_uni_up.setMaxAccess(_C)
if mibBuilder.loadTexts:def_uni_up.setStatus(_A)
if mibBuilder.loadTexts:def_uni_up.setUnits(_F)
class _Def_pri_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Def_pri_Type.__name__=_B
_Def_pri_Object=MibScalar
def_pri=_Def_pri_Object((1,3,6,1,4,1,9839,2,1,1,30),_Def_pri_Type())
def_pri.setMaxAccess(_C)
if mibBuilder.loadTexts:def_pri.setStatus(_A)
if mibBuilder.loadTexts:def_pri.setUnits(_F)
class _Time_base_dc_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Time_base_dc_Type.__name__=_B
_Time_base_dc_Object=MibScalar
time_base_dc=_Time_base_dc_Object((1,3,6,1,4,1,9839,2,1,1,31),_Time_base_dc_Type())
time_base_dc.setMaxAccess(_C)
if mibBuilder.loadTexts:time_base_dc.setStatus(_A)
if mibBuilder.loadTexts:time_base_dc.setUnits(_F)
class _Stop_fan_f2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stop_fan_f2_Type.__name__=_B
_Stop_fan_f2_Object=MibScalar
stop_fan_f2=_Stop_fan_f2_Object((1,3,6,1,4,1,9839,2,1,1,33),_Stop_fan_f2_Type())
stop_fan_f2.setMaxAccess(_C)
if mibBuilder.loadTexts:stop_fan_f2.setStatus(_A)
if mibBuilder.loadTexts:stop_fan_f2.setUnits(_F)
class _Stop_fan_f3_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stop_fan_f3_Type.__name__=_B
_Stop_fan_f3_Object=MibScalar
stop_fan_f3=_Stop_fan_f3_Object((1,3,6,1,4,1,9839,2,1,1,34),_Stop_fan_f3_Type())
stop_fan_f3.setMaxAccess(_C)
if mibBuilder.loadTexts:stop_fan_f3.setStatus(_A)
if mibBuilder.loadTexts:stop_fan_f3.setUnits(_F)
class _M_def_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_M_def_Type.__name__=_B
_M_def_Object=MibScalar
m_def=_M_def_Object((1,3,6,1,4,1,9839,2,1,1,39),_M_def_Type())
m_def.setMaxAccess(_C)
if mibBuilder.loadTexts:m_def.setStatus(_A)
if mibBuilder.loadTexts:m_def.setUnits(_D)
class _Int_display_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Int_display_Type.__name__=_B
_Int_display_Object=MibScalar
int_display=_Int_display_Object((1,3,6,1,4,1,9839,2,1,1,42),_Int_display_Type())
int_display.setMaxAccess(_C)
if mibBuilder.loadTexts:int_display.setStatus(_A)
if mibBuilder.loadTexts:int_display.setUnits(_F)
class _En_max_min_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_max_min_Type.__name__=_B
_En_max_min_Object=MibScalar
en_max_min=_En_max_min_Object((1,3,6,1,4,1,9839,2,1,1,43),_En_max_min_Type())
en_max_min.setMaxAccess(_C)
if mibBuilder.loadTexts:en_max_min.setStatus(_A)
if mibBuilder.loadTexts:en_max_min.setUnits(_F)
class _Blocco_vis_sbrin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Blocco_vis_sbrin_Type.__name__=_B
_Blocco_vis_sbrin_Object=MibScalar
blocco_vis_sbrin=_Blocco_vis_sbrin_Object((1,3,6,1,4,1,9839,2,1,1,44),_Blocco_vis_sbrin_Type())
blocco_vis_sbrin.setMaxAccess(_C)
if mibBuilder.loadTexts:blocco_vis_sbrin.setStatus(_A)
if mibBuilder.loadTexts:blocco_vis_sbrin.setUnits(_F)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Temp_ambiente_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Temp_ambiente_Type.__name__=_B
_Temp_ambiente_Object=MibScalar
temp_ambiente=_Temp_ambiente_Object((1,3,6,1,4,1,9839,2,1,2,1),_Temp_ambiente_Type())
temp_ambiente.setMaxAccess(_E)
if mibBuilder.loadTexts:temp_ambiente.setStatus(_A)
if mibBuilder.loadTexts:temp_ambiente.setUnits('C x10')
class _Temp_evap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Temp_evap_Type.__name__=_B
_Temp_evap_Object=MibScalar
temp_evap=_Temp_evap_Object((1,3,6,1,4,1,9839,2,1,2,2),_Temp_evap_Type())
temp_evap.setMaxAccess(_E)
if mibBuilder.loadTexts:temp_evap.setStatus(_A)
if mibBuilder.loadTexts:temp_evap.setUnits('C x10')
class _Set_point_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_point_Type.__name__=_B
_Set_point_Object=MibScalar
set_point=_Set_point_Object((1,3,6,1,4,1,9839,2,1,2,3),_Set_point_Type())
set_point.setMaxAccess(_C)
if mibBuilder.loadTexts:set_point.setStatus(_A)
if mibBuilder.loadTexts:set_point.setUnits(_H)
class _Offset_probe_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-200,200))
_Offset_probe_Type.__name__=_B
_Offset_probe_Object=MibScalar
offset_probe=_Offset_probe_Object((1,3,6,1,4,1,9839,2,1,2,4),_Offset_probe_Type())
offset_probe.setMaxAccess(_C)
if mibBuilder.loadTexts:offset_probe.setStatus(_A)
if mibBuilder.loadTexts:offset_probe.setUnits(_H)
class _Control_delta_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_Control_delta_Type.__name__=_B
_Control_delta_Object=MibScalar
control_delta=_Control_delta_Object((1,3,6,1,4,1,9839,2,1,2,5),_Control_delta_Type())
control_delta.setMaxAccess(_C)
if mibBuilder.loadTexts:control_delta.setStatus(_A)
if mibBuilder.loadTexts:control_delta.setUnits(_H)
class _Set_point_min_Type(Integer32):defaultValue=-500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,32767))
_Set_point_min_Type.__name__=_B
_Set_point_min_Object=MibScalar
set_point_min=_Set_point_min_Object((1,3,6,1,4,1,9839,2,1,2,6),_Set_point_min_Type())
set_point_min.setMaxAccess(_C)
if mibBuilder.loadTexts:set_point_min.setStatus(_A)
if mibBuilder.loadTexts:set_point_min.setUnits(_H)
class _Set_point_max_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,1990))
_Set_point_max_Type.__name__=_B
_Set_point_max_Object=MibScalar
set_point_max=_Set_point_max_Object((1,3,6,1,4,1,9839,2,1,2,7),_Set_point_max_Type())
set_point_max.setMaxAccess(_C)
if mibBuilder.loadTexts:set_point_max.setStatus(_A)
if mibBuilder.loadTexts:set_point_max.setUnits(_H)
class _Defrost_end_temperature_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,1990))
_Defrost_end_temperature_Type.__name__=_B
_Defrost_end_temperature_Object=MibScalar
defrost_end_temperature=_Defrost_end_temperature_Object((1,3,6,1,4,1,9839,2,1,2,8),_Defrost_end_temperature_Type())
defrost_end_temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_end_temperature.setStatus(_A)
if mibBuilder.loadTexts:defrost_end_temperature.setUnits(_H)
class _Diff_alarm_fan_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_Diff_alarm_fan_Type.__name__=_B
_Diff_alarm_fan_Object=MibScalar
diff_alarm_fan=_Diff_alarm_fan_Object((1,3,6,1,4,1,9839,2,1,2,9),_Diff_alarm_fan_Type())
diff_alarm_fan.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_alarm_fan.setStatus(_A)
if mibBuilder.loadTexts:diff_alarm_fan.setUnits(_H)
class _Sgl_alarm_min_rel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1990))
_Sgl_alarm_min_rel_Type.__name__=_B
_Sgl_alarm_min_rel_Object=MibScalar
sgl_alarm_min_rel=_Sgl_alarm_min_rel_Object((1,3,6,1,4,1,9839,2,1,2,10),_Sgl_alarm_min_rel_Type())
sgl_alarm_min_rel.setMaxAccess(_C)
if mibBuilder.loadTexts:sgl_alarm_min_rel.setStatus(_A)
if mibBuilder.loadTexts:sgl_alarm_min_rel.setUnits(_H)
class _Sgl_alarl_max_rel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1990))
_Sgl_alarl_max_rel_Type.__name__=_B
_Sgl_alarl_max_rel_Object=MibScalar
sgl_alarl_max_rel=_Sgl_alarl_max_rel_Object((1,3,6,1,4,1,9839,2,1,2,11),_Sgl_alarl_max_rel_Type())
sgl_alarl_max_rel.setMaxAccess(_C)
if mibBuilder.loadTexts:sgl_alarl_max_rel.setStatus(_A)
if mibBuilder.loadTexts:sgl_alarl_max_rel.setUnits(_H)
class _Set_fan_off_rel_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,200))
_Set_fan_off_rel_Type.__name__=_B
_Set_fan_off_rel_Object=MibScalar
set_fan_off_rel=_Set_fan_off_rel_Object((1,3,6,1,4,1,9839,2,1,2,12),_Set_fan_off_rel_Type())
set_fan_off_rel.setMaxAccess(_C)
if mibBuilder.loadTexts:set_fan_off_rel.setStatus(_A)
if mibBuilder.loadTexts:set_fan_off_rel.setUnits(_H)
class _Delta_set_point_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Delta_set_point_Type.__name__=_B
_Delta_set_point_Object=MibScalar
delta_set_point=_Delta_set_point_Object((1,3,6,1,4,1,9839,2,1,2,13),_Delta_set_point_Type())
delta_set_point.setMaxAccess(_C)
if mibBuilder.loadTexts:delta_set_point.setStatus(_A)
if mibBuilder.loadTexts:delta_set_point.setUnits(_H)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Modello_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Modello_Type.__name__=_B
_Modello_Object=MibScalar
modello=_Modello_Object((1,3,6,1,4,1,9839,2,1,3,1),_Modello_Type())
modello.setMaxAccess(_E)
if mibBuilder.loadTexts:modello.setStatus(_A)
if mibBuilder.loadTexts:modello.setUnits(_D)
class _Type_defrost_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Type_defrost_Type.__name__=_B
_Type_defrost_Object=MibScalar
type_defrost=_Type_defrost_Object((1,3,6,1,4,1,9839,2,1,3,2),_Type_defrost_Type())
type_defrost.setMaxAccess(_C)
if mibBuilder.loadTexts:type_defrost.setStatus(_A)
if mibBuilder.loadTexts:type_defrost.setUnits(_F)
class _Filter_digital_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Filter_digital_Type.__name__=_B
_Filter_digital_Object=MibScalar
filter_digital=_Filter_digital_Object((1,3,6,1,4,1,9839,2,1,3,3),_Filter_digital_Type())
filter_digital.setMaxAccess(_C)
if mibBuilder.loadTexts:filter_digital.setStatus(_A)
if mibBuilder.loadTexts:filter_digital.setUnits(_D)
class _Derivata_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Derivata_Type.__name__=_B
_Derivata_Object=MibScalar
derivata=_Derivata_Object((1,3,6,1,4,1,9839,2,1,3,4),_Derivata_Type())
derivata.setMaxAccess(_C)
if mibBuilder.loadTexts:derivata.setStatus(_A)
if mibBuilder.loadTexts:derivata.setUnits(_D)
class _Virtual_probe_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Virtual_probe_Type.__name__=_B
_Virtual_probe_Object=MibScalar
virtual_probe=_Virtual_probe_Object((1,3,6,1,4,1,9839,2,1,3,5),_Virtual_probe_Type())
virtual_probe.setMaxAccess(_C)
if mibBuilder.loadTexts:virtual_probe.setStatus(_A)
if mibBuilder.loadTexts:virtual_probe.setUnits(_D)
class _Delay_from_startup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Delay_from_startup_Type.__name__=_B
_Delay_from_startup_Object=MibScalar
delay_from_startup=_Delay_from_startup_Object((1,3,6,1,4,1,9839,2,1,3,6),_Delay_from_startup_Type())
delay_from_startup.setMaxAccess(_C)
if mibBuilder.loadTexts:delay_from_startup.setStatus(_A)
if mibBuilder.loadTexts:delay_from_startup.setUnits(_G)
class _Interval_between_2_start_up_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Interval_between_2_start_up_Type.__name__=_B
_Interval_between_2_start_up_Object=MibScalar
interval_between_2_start_up=_Interval_between_2_start_up_Object((1,3,6,1,4,1,9839,2,1,3,7),_Interval_between_2_start_up_Type())
interval_between_2_start_up.setMaxAccess(_C)
if mibBuilder.loadTexts:interval_between_2_start_up.setStatus(_A)
if mibBuilder.loadTexts:interval_between_2_start_up.setUnits(_G)
class _Time_min_off_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Time_min_off_Type.__name__=_B
_Time_min_off_Object=MibScalar
time_min_off=_Time_min_off_Object((1,3,6,1,4,1,9839,2,1,3,8),_Time_min_off_Type())
time_min_off.setMaxAccess(_C)
if mibBuilder.loadTexts:time_min_off.setStatus(_A)
if mibBuilder.loadTexts:time_min_off.setUnits(_G)
class _Time_min_on_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Time_min_on_Type.__name__=_B
_Time_min_on_Object=MibScalar
time_min_on=_Time_min_on_Object((1,3,6,1,4,1,9839,2,1,3,9),_Time_min_on_Type())
time_min_on.setMaxAccess(_C)
if mibBuilder.loadTexts:time_min_on.setStatus(_A)
if mibBuilder.loadTexts:time_min_on.setUnits(_G)
class _Safety_relay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Safety_relay_Type.__name__=_B
_Safety_relay_Object=MibScalar
safety_relay=_Safety_relay_Object((1,3,6,1,4,1,9839,2,1,3,10),_Safety_relay_Type())
safety_relay.setMaxAccess(_C)
if mibBuilder.loadTexts:safety_relay.setStatus(_A)
if mibBuilder.loadTexts:safety_relay.setUnits(_G)
class _Duration_cc_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Duration_cc_Type.__name__=_B
_Duration_cc_Object=MibScalar
duration_cc=_Duration_cc_Object((1,3,6,1,4,1,9839,2,1,3,11),_Duration_cc_Type())
duration_cc.setMaxAccess(_C)
if mibBuilder.loadTexts:duration_cc.setStatus(_A)
if mibBuilder.loadTexts:duration_cc.setUnits('hour')
class _No_alarm_after_cc_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_No_alarm_after_cc_Type.__name__=_B
_No_alarm_after_cc_Object=MibScalar
no_alarm_after_cc=_No_alarm_after_cc_Object((1,3,6,1,4,1,9839,2,1,3,12),_No_alarm_after_cc_Type())
no_alarm_after_cc.setMaxAccess(_C)
if mibBuilder.loadTexts:no_alarm_after_cc.setStatus(_A)
if mibBuilder.loadTexts:no_alarm_after_cc.setUnits('hour')
class _Interval_between_defrost_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Interval_between_defrost_Type.__name__=_B
_Interval_between_defrost_Object=MibScalar
interval_between_defrost=_Interval_between_defrost_Object((1,3,6,1,4,1,9839,2,1,3,13),_Interval_between_defrost_Type())
interval_between_defrost.setMaxAccess(_C)
if mibBuilder.loadTexts:interval_between_defrost.setStatus(_A)
if mibBuilder.loadTexts:interval_between_defrost.setUnits('hours')
class _Duration_def_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_Duration_def_Type.__name__=_B
_Duration_def_Object=MibScalar
duration_def=_Duration_def_Object((1,3,6,1,4,1,9839,2,1,3,14),_Duration_def_Type())
duration_def.setMaxAccess(_C)
if mibBuilder.loadTexts:duration_def.setStatus(_A)
if mibBuilder.loadTexts:duration_def.setUnits(_G)
class _Delay_def_after_sturt_up_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Delay_def_after_sturt_up_Type.__name__=_B
_Delay_def_after_sturt_up_Object=MibScalar
delay_def_after_sturt_up=_Delay_def_after_sturt_up_Object((1,3,6,1,4,1,9839,2,1,3,15),_Delay_def_after_sturt_up_Type())
delay_def_after_sturt_up.setMaxAccess(_C)
if mibBuilder.loadTexts:delay_def_after_sturt_up.setStatus(_A)
if mibBuilder.loadTexts:delay_def_after_sturt_up.setUnits(_G)
class _Dripping_iyme_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Dripping_iyme_Type.__name__=_B
_Dripping_iyme_Object=MibScalar
dripping_iyme=_Dripping_iyme_Object((1,3,6,1,4,1,9839,2,1,3,16),_Dripping_iyme_Type())
dripping_iyme.setMaxAccess(_C)
if mibBuilder.loadTexts:dripping_iyme.setStatus(_A)
if mibBuilder.loadTexts:dripping_iyme.setUnits(_G)
class _Duration_of_alarm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Duration_of_alarm_Type.__name__=_B
_Duration_of_alarm_Object=MibScalar
duration_of_alarm=_Duration_of_alarm_Object((1,3,6,1,4,1,9839,2,1,3,17),_Duration_of_alarm_Type())
duration_of_alarm.setMaxAccess(_C)
if mibBuilder.loadTexts:duration_of_alarm.setStatus(_A)
if mibBuilder.loadTexts:duration_of_alarm.setUnits('hours')
class _Rit_all_temp_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Rit_all_temp_Type.__name__=_B
_Rit_all_temp_Object=MibScalar
rit_all_temp=_Rit_all_temp_Object((1,3,6,1,4,1,9839,2,1,3,18),_Rit_all_temp_Type())
rit_all_temp.setMaxAccess(_C)
if mibBuilder.loadTexts:rit_all_temp.setStatus(_A)
if mibBuilder.loadTexts:rit_all_temp.setUnits(_G)
class _Config_dig_in1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Config_dig_in1_Type.__name__=_B
_Config_dig_in1_Object=MibScalar
config_dig_in1=_Config_dig_in1_Object((1,3,6,1,4,1,9839,2,1,3,19),_Config_dig_in1_Type())
config_dig_in1.setMaxAccess(_C)
if mibBuilder.loadTexts:config_dig_in1.setStatus(_A)
if mibBuilder.loadTexts:config_dig_in1.setUnits(_D)
class _Config_dig_in2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Config_dig_in2_Type.__name__=_B
_Config_dig_in2_Object=MibScalar
config_dig_in2=_Config_dig_in2_Object((1,3,6,1,4,1,9839,2,1,3,20),_Config_dig_in2_Type())
config_dig_in2.setMaxAccess(_C)
if mibBuilder.loadTexts:config_dig_in2.setStatus(_A)
if mibBuilder.loadTexts:config_dig_in2.setUnits(_D)
class _Look_comp_ext_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Look_comp_ext_Type.__name__=_B
_Look_comp_ext_Object=MibScalar
look_comp_ext=_Look_comp_ext_Object((1,3,6,1,4,1,9839,2,1,3,21),_Look_comp_ext_Type())
look_comp_ext.setMaxAccess(_C)
if mibBuilder.loadTexts:look_comp_ext.setStatus(_A)
if mibBuilder.loadTexts:look_comp_ext.setUnits(_G)
class _Delay_activ_alr_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Delay_activ_alr_Type.__name__=_B
_Delay_activ_alr_Object=MibScalar
delay_activ_alr=_Delay_activ_alr_Object((1,3,6,1,4,1,9839,2,1,3,22),_Delay_activ_alr_Type())
delay_activ_alr.setMaxAccess(_C)
if mibBuilder.loadTexts:delay_activ_alr.setStatus(_A)
if mibBuilder.loadTexts:delay_activ_alr.setUnits(_G)
class _Enabling_telecom_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Enabling_telecom_Type.__name__=_B
_Enabling_telecom_Object=MibScalar
enabling_telecom=_Enabling_telecom_Object((1,3,6,1,4,1,9839,2,1,3,23),_Enabling_telecom_Type())
enabling_telecom.setMaxAccess(_C)
if mibBuilder.loadTexts:enabling_telecom.setStatus(_A)
if mibBuilder.loadTexts:enabling_telecom.setUnits(_D)
class _Sto_after_drip_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Sto_after_drip_Type.__name__=_B
_Sto_after_drip_Object=MibScalar
sto_after_drip=_Sto_after_drip_Object((1,3,6,1,4,1,9839,2,1,3,24),_Sto_after_drip_Type())
sto_after_drip.setMaxAccess(_C)
if mibBuilder.loadTexts:sto_after_drip.setStatus(_A)
if mibBuilder.loadTexts:sto_after_drip.setUnits(_G)
class _Key_lock_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Key_lock_Type.__name__=_B
_Key_lock_Object=MibScalar
key_lock=_Key_lock_Object((1,3,6,1,4,1,9839,2,1,3,25),_Key_lock_Type())
key_lock.setMaxAccess(_C)
if mibBuilder.loadTexts:key_lock.setStatus(_A)
if mibBuilder.loadTexts:key_lock.setUnits(_F)
class _Fan_man_f0_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Fan_man_f0_Type.__name__=_B
_Fan_man_f0_Object=MibScalar
fan_man_f0=_Fan_man_f0_Object((1,3,6,1,4,1,9839,2,1,3,26),_Fan_man_f0_Type())
fan_man_f0.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_man_f0.setStatus(_A)
if mibBuilder.loadTexts:fan_man_f0.setUnits(_F)
class _Oper_mode_h1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Oper_mode_h1_Type.__name__=_B
_Oper_mode_h1_Object=MibScalar
oper_mode_h1=_Oper_mode_h1_Object((1,3,6,1,4,1,9839,2,1,3,27),_Oper_mode_h1_Type())
oper_mode_h1.setMaxAccess(_C)
if mibBuilder.loadTexts:oper_mode_h1.setStatus(_A)
if mibBuilder.loadTexts:oper_mode_h1.setUnits(_D)
mibBuilder.exportSymbols('CAREL-mcella-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'mcellaMIB':mcellaMIB,'digitalObjects':digitalObjects,'ciclo_continuo':ciclo_continuo,'ventilatori':ventilatori,'compressor':compressor,'aux_out':aux_out,'valv_inv_ciclo':valv_inv_ciclo,'all_eeprom':all_eeprom,'all_timeout_def':all_timeout_def,'all_bassa_temp':all_bassa_temp,'all_alta_temp':all_alta_temp,'all_sonda_amb':all_sonda_amb,'all_sonda_def':all_sonda_def,'all_imm_ai':all_imm_ai,'all_rit_ad':all_rit_ad,'sbrinam_on':sbrinam_on,'c_f__5':c_f__5,'en_ed_alarm':en_ed_alarm,'def_uni_up':def_uni_up,'def_pri':def_pri,'time_base_dc':time_base_dc,'stop_fan_f2':stop_fan_f2,'stop_fan_f3':stop_fan_f3,'m_def':m_def,'int_display':int_display,'en_max_min':en_max_min,'blocco_vis_sbrin':blocco_vis_sbrin,'analogObjects':analogObjects,'temp_ambiente':temp_ambiente,'temp_evap':temp_evap,'set_point':set_point,'offset_probe':offset_probe,'control_delta':control_delta,'set_point_min':set_point_min,'set_point_max':set_point_max,'defrost_end_temperature':defrost_end_temperature,'diff_alarm_fan':diff_alarm_fan,'sgl_alarm_min_rel':sgl_alarm_min_rel,'sgl_alarl_max_rel':sgl_alarl_max_rel,'set_fan_off_rel':set_fan_off_rel,'delta_set_point':delta_set_point,'integerObjects':integerObjects,'modello':modello,'type_defrost':type_defrost,'filter_digital':filter_digital,'derivata':derivata,'virtual_probe':virtual_probe,'delay_from_startup':delay_from_startup,'interval_between_2_start-up':interval_between_2_start_up,'time_min_off':time_min_off,'time_min_on':time_min_on,'safety_relay':safety_relay,'duration_cc':duration_cc,'no_alarm_after_cc':no_alarm_after_cc,'interval_between_defrost':interval_between_defrost,'duration_def':duration_def,'delay_def_after_sturt_up':delay_def_after_sturt_up,'dripping_iyme':dripping_iyme,'duration_of_alarm':duration_of_alarm,'rit_all_temp':rit_all_temp,'config_dig_in1':config_dig_in1,'config_dig_in2':config_dig_in2,'look_comp_ext':look_comp_ext,'delay_activ_alr':delay_activ_alr,'enabling_telecom':enabling_telecom,'sto_after_drip':sto_after_drip,'key_lock':key_lock,'fan_man_f0':fan_man_f0,'oper_mode_h1':oper_mode_h1})