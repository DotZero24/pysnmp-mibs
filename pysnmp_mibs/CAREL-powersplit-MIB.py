_K='flag'
_J='gg'
_I='min.'
_H='ore'
_G='min'
_F='C/F x10'
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
powersplitMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
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
class _Cent_fhren_flag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cent_fhren_flag_Type.__name__=_B
_Cent_fhren_flag_Object=MibScalar
cent_fhren_flag=_Cent_fhren_flag_Object((1,3,6,1,4,1,9839,2,1,1,1),_Cent_fhren_flag_Type())
cent_fhren_flag.setMaxAccess(_C)
if mibBuilder.loadTexts:cent_fhren_flag.setStatus(_A)
if mibBuilder.loadTexts:cent_fhren_flag.setUnits(_D)
class _Autoscale_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Autoscale_Type.__name__=_B
_Autoscale_Object=MibScalar
autoscale=_Autoscale_Object((1,3,6,1,4,1,9839,2,1,1,2),_Autoscale_Type())
autoscale.setMaxAccess(_C)
if mibBuilder.loadTexts:autoscale.setStatus(_A)
if mibBuilder.loadTexts:autoscale.setUnits(_D)
class _Defrostprobeselect_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Defrostprobeselect_Type.__name__=_B
_Defrostprobeselect_Object=MibScalar
defrostprobeselect=_Defrostprobeselect_Object((1,3,6,1,4,1,9839,2,1,1,3),_Defrostprobeselect_Type())
defrostprobeselect.setMaxAccess(_C)
if mibBuilder.loadTexts:defrostprobeselect.setStatus(_A)
if mibBuilder.loadTexts:defrostprobeselect.setUnits(_D)
class _Defrost_cmd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Defrost_cmd_Type.__name__=_B
_Defrost_cmd_Object=MibScalar
defrost_cmd=_Defrost_cmd_Object((1,3,6,1,4,1,9839,2,1,1,4),_Defrost_cmd_Type())
defrost_cmd.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_cmd.setStatus(_A)
if mibBuilder.loadTexts:defrost_cmd.setUnits(_K)
class _Defrost_at_startup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Defrost_at_startup_Type.__name__=_B
_Defrost_at_startup_Object=MibScalar
defrost_at_startup=_Defrost_at_startup_Object((1,3,6,1,4,1,9839,2,1,1,5),_Defrost_at_startup_Type())
defrost_at_startup.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_at_startup.setStatus(_A)
if mibBuilder.loadTexts:defrost_at_startup.setUnits(_K)
class _Defrost_show_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Defrost_show_Type.__name__=_B
_Defrost_show_Object=MibScalar
defrost_show=_Defrost_show_Object((1,3,6,1,4,1,9839,2,1,1,6),_Defrost_show_Type())
defrost_show.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_show.setStatus(_A)
if mibBuilder.loadTexts:defrost_show.setUnits(_K)
class _Defrost_priority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Defrost_priority_Type.__name__=_B
_Defrost_priority_Object=MibScalar
defrost_priority=_Defrost_priority_Object((1,3,6,1,4,1,9839,2,1,1,7),_Defrost_priority_Type())
defrost_priority.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_priority.setStatus(_A)
if mibBuilder.loadTexts:defrost_priority.setUnits(_K)
class _Fan_cfg_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan_cfg_Type.__name__=_B
_Fan_cfg_Object=MibScalar
fan_cfg=_Fan_cfg_Object((1,3,6,1,4,1,9839,2,1,1,8),_Fan_cfg_Type())
fan_cfg.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_cfg.setStatus(_A)
if mibBuilder.loadTexts:fan_cfg.setUnits(_D)
class _Fan_off_ctrl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan_off_ctrl_Type.__name__=_B
_Fan_off_ctrl_Object=MibScalar
fan_off_ctrl=_Fan_off_ctrl_Object((1,3,6,1,4,1,9839,2,1,1,9),_Fan_off_ctrl_Type())
fan_off_ctrl.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_off_ctrl.setStatus(_A)
if mibBuilder.loadTexts:fan_off_ctrl.setUnits(_D)
class _Fan_defrost_ctrl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan_defrost_ctrl_Type.__name__=_B
_Fan_defrost_ctrl_Object=MibScalar
fan_defrost_ctrl=_Fan_defrost_ctrl_Object((1,3,6,1,4,1,9839,2,1,1,10),_Fan_defrost_ctrl_Type())
fan_defrost_ctrl.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_defrost_ctrl.setStatus(_A)
if mibBuilder.loadTexts:fan_defrost_ctrl.setUnits(_D)
class _Keyb_disabled_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Keyb_disabled_Type.__name__=_B
_Keyb_disabled_Object=MibScalar
keyb_disabled=_Keyb_disabled_Object((1,3,6,1,4,1,9839,2,1,1,11),_Keyb_disabled_Type())
keyb_disabled.setMaxAccess(_C)
if mibBuilder.loadTexts:keyb_disabled.setStatus(_A)
if mibBuilder.loadTexts:keyb_disabled.setUnits(_D)
class _Loc_on_off_ena_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Loc_on_off_ena_Type.__name__=_B
_Loc_on_off_ena_Object=MibScalar
loc_on_off_ena=_Loc_on_off_ena_Object((1,3,6,1,4,1,9839,2,1,1,12),_Loc_on_off_ena_Type())
loc_on_off_ena.setMaxAccess(_C)
if mibBuilder.loadTexts:loc_on_off_ena.setStatus(_A)
if mibBuilder.loadTexts:loc_on_off_ena.setUnits(_D)
class _Lan_on_off_ena_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Lan_on_off_ena_Type.__name__=_B
_Lan_on_off_ena_Object=MibScalar
lan_on_off_ena=_Lan_on_off_ena_Object((1,3,6,1,4,1,9839,2,1,1,13),_Lan_on_off_ena_Type())
lan_on_off_ena.setMaxAccess(_C)
if mibBuilder.loadTexts:lan_on_off_ena.setStatus(_A)
if mibBuilder.loadTexts:lan_on_off_ena.setUnits(_D)
class _Lan_din_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Lan_din_Type.__name__=_B
_Lan_din_Object=MibScalar
lan_din=_Lan_din_Object((1,3,6,1,4,1,9839,2,1,1,14),_Lan_din_Type())
lan_din.setMaxAccess(_C)
if mibBuilder.loadTexts:lan_din.setStatus(_A)
if mibBuilder.loadTexts:lan_din.setUnits(_D)
class _Defrost_tout_alarm_ena_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Defrost_tout_alarm_ena_Type.__name__=_B
_Defrost_tout_alarm_ena_Object=MibScalar
defrost_tout_alarm_ena=_Defrost_tout_alarm_ena_Object((1,3,6,1,4,1,9839,2,1,1,15),_Defrost_tout_alarm_ena_Type())
defrost_tout_alarm_ena.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_tout_alarm_ena.setStatus(_A)
if mibBuilder.loadTexts:defrost_tout_alarm_ena.setUnits(_D)
class _Minmax_store_enable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Minmax_store_enable_Type.__name__=_B
_Minmax_store_enable_Object=MibScalar
minmax_store_enable=_Minmax_store_enable_Object((1,3,6,1,4,1,9839,2,1,1,16),_Minmax_store_enable_Type())
minmax_store_enable.setMaxAccess(_C)
if mibBuilder.loadTexts:minmax_store_enable.setStatus(_A)
if mibBuilder.loadTexts:minmax_store_enable.setUnits(_D)
class _Night_reg_probe_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Night_reg_probe_Type.__name__=_B
_Night_reg_probe_Object=MibScalar
night_reg_probe=_Night_reg_probe_Object((1,3,6,1,4,1,9839,2,1,1,17),_Night_reg_probe_Type())
night_reg_probe.setMaxAccess(_C)
if mibBuilder.loadTexts:night_reg_probe.setStatus(_A)
if mibBuilder.loadTexts:night_reg_probe.setUnits(_D)
class _Haccp_reset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Haccp_reset_Type.__name__=_B
_Haccp_reset_Object=MibScalar
haccp_reset=_Haccp_reset_Object((1,3,6,1,4,1,9839,2,1,1,18),_Haccp_reset_Type())
haccp_reset.setMaxAccess(_C)
if mibBuilder.loadTexts:haccp_reset.setStatus(_A)
if mibBuilder.loadTexts:haccp_reset.setUnits(_D)
class _Dig_in_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dig_in_1_Type.__name__=_B
_Dig_in_1_Object=MibScalar
dig_in_1=_Dig_in_1_Object((1,3,6,1,4,1,9839,2,1,1,29),_Dig_in_1_Type())
dig_in_1.setMaxAccess(_E)
if mibBuilder.loadTexts:dig_in_1.setStatus(_A)
if mibBuilder.loadTexts:dig_in_1.setUnits(_D)
class _Dig_in_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dig_in_2_Type.__name__=_B
_Dig_in_2_Object=MibScalar
dig_in_2=_Dig_in_2_Object((1,3,6,1,4,1,9839,2,1,1,30),_Dig_in_2_Type())
dig_in_2.setMaxAccess(_E)
if mibBuilder.loadTexts:dig_in_2.setStatus(_A)
if mibBuilder.loadTexts:dig_in_2.setUnits(_D)
class _S_comp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_comp_Type.__name__=_B
_S_comp_Object=MibScalar
s_comp=_S_comp_Object((1,3,6,1,4,1,9839,2,1,1,33),_S_comp_Type())
s_comp.setMaxAccess(_E)
if mibBuilder.loadTexts:s_comp.setStatus(_A)
if mibBuilder.loadTexts:s_comp.setUnits(_D)
class _S_fan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_fan_Type.__name__=_B
_S_fan_Object=MibScalar
s_fan=_S_fan_Object((1,3,6,1,4,1,9839,2,1,1,34),_S_fan_Type())
s_fan.setMaxAccess(_E)
if mibBuilder.loadTexts:s_fan.setStatus(_A)
if mibBuilder.loadTexts:s_fan.setUnits(_D)
class _S_defrost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_defrost_Type.__name__=_B
_S_defrost_Object=MibScalar
s_defrost=_S_defrost_Object((1,3,6,1,4,1,9839,2,1,1,35),_S_defrost_Type())
s_defrost.setMaxAccess(_E)
if mibBuilder.loadTexts:s_defrost.setStatus(_A)
if mibBuilder.loadTexts:s_defrost.setUnits(_D)
class _S_aux_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_aux_2_Type.__name__=_B
_S_aux_2_Object=MibScalar
s_aux_2=_S_aux_2_Object((1,3,6,1,4,1,9839,2,1,1,36),_S_aux_2_Type())
s_aux_2.setMaxAccess(_E)
if mibBuilder.loadTexts:s_aux_2.setStatus(_A)
if mibBuilder.loadTexts:s_aux_2.setUnits(_D)
class _S_alarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_alarm_Type.__name__=_B
_S_alarm_Object=MibScalar
s_alarm=_S_alarm_Object((1,3,6,1,4,1,9839,2,1,1,37),_S_alarm_Type())
s_alarm.setMaxAccess(_E)
if mibBuilder.loadTexts:s_alarm.setStatus(_A)
if mibBuilder.loadTexts:s_alarm.setUnits(_D)
class _S_light_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_S_light_Type.__name__=_B
_S_light_Object=MibScalar
s_light=_S_light_Object((1,3,6,1,4,1,9839,2,1,1,39),_S_light_Type())
s_light.setMaxAccess(_E)
if mibBuilder.loadTexts:s_light.setStatus(_A)
if mibBuilder.loadTexts:s_light.setUnits(_D)
class _Dr_supervisor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dr_supervisor_Type.__name__=_B
_Dr_supervisor_Object=MibScalar
dr_supervisor=_Dr_supervisor_Object((1,3,6,1,4,1,9839,2,1,1,40),_Dr_supervisor_Type())
dr_supervisor.setMaxAccess(_C)
if mibBuilder.loadTexts:dr_supervisor.setStatus(_A)
if mibBuilder.loadTexts:dr_supervisor.setUnits(_D)
class _Dr_svendreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dr_svendreq_Type.__name__=_B
_Dr_svendreq_Object=MibScalar
dr_svendreq=_Dr_svendreq_Object((1,3,6,1,4,1,9839,2,1,1,41),_Dr_svendreq_Type())
dr_svendreq.setMaxAccess(_C)
if mibBuilder.loadTexts:dr_svendreq.setStatus(_A)
if mibBuilder.loadTexts:dr_svendreq.setUnits(_D)
class _A1_e1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A1_e1_Type.__name__=_B
_A1_e1_Object=MibScalar
a1_e1=_A1_e1_Object((1,3,6,1,4,1,9839,2,1,1,44),_A1_e1_Type())
a1_e1.setMaxAccess(_E)
if mibBuilder.loadTexts:a1_e1.setStatus(_A)
if mibBuilder.loadTexts:a1_e1.setUnits(_D)
class _A1_e2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A1_e2_Type.__name__=_B
_A1_e2_Object=MibScalar
a1_e2=_A1_e2_Object((1,3,6,1,4,1,9839,2,1,1,45),_A1_e2_Type())
a1_e2.setMaxAccess(_E)
if mibBuilder.loadTexts:a1_e2.setStatus(_A)
if mibBuilder.loadTexts:a1_e2.setUnits(_D)
class _A1_e3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A1_e3_Type.__name__=_B
_A1_e3_Object=MibScalar
a1_e3=_A1_e3_Object((1,3,6,1,4,1,9839,2,1,1,46),_A1_e3_Type())
a1_e3.setMaxAccess(_E)
if mibBuilder.loadTexts:a1_e3.setStatus(_A)
if mibBuilder.loadTexts:a1_e3.setUnits(_D)
class _A1_ia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A1_ia_Type.__name__=_B
_A1_ia_Object=MibScalar
a1_ia=_A1_ia_Object((1,3,6,1,4,1,9839,2,1,1,47),_A1_ia_Type())
a1_ia.setMaxAccess(_E)
if mibBuilder.loadTexts:a1_ia.setStatus(_A)
if mibBuilder.loadTexts:a1_ia.setUnits(_D)
class _A1_da_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A1_da_Type.__name__=_B
_A1_da_Object=MibScalar
a1_da=_A1_da_Object((1,3,6,1,4,1,9839,2,1,1,48),_A1_da_Type())
a1_da.setMaxAccess(_E)
if mibBuilder.loadTexts:a1_da.setStatus(_A)
if mibBuilder.loadTexts:a1_da.setUnits(_D)
class _A1_ea_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A1_ea_Type.__name__=_B
_A1_ea_Object=MibScalar
a1_ea=_A1_ea_Object((1,3,6,1,4,1,9839,2,1,1,49),_A1_ea_Type())
a1_ea.setMaxAccess(_E)
if mibBuilder.loadTexts:a1_ea.setStatus(_A)
if mibBuilder.loadTexts:a1_ea.setUnits(_D)
class _A1_re_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A1_re_Type.__name__=_B
_A1_re_Object=MibScalar
a1_re=_A1_re_Object((1,3,6,1,4,1,9839,2,1,1,50),_A1_re_Type())
a1_re.setMaxAccess(_E)
if mibBuilder.loadTexts:a1_re.setStatus(_A)
if mibBuilder.loadTexts:a1_re.setUnits(_D)
class _A1_id_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A1_id_Type.__name__=_B
_A1_id_Object=MibScalar
a1_id=_A1_id_Object((1,3,6,1,4,1,9839,2,1,1,51),_A1_id_Type())
a1_id.setMaxAccess(_E)
if mibBuilder.loadTexts:a1_id.setStatus(_A)
if mibBuilder.loadTexts:a1_id.setUnits(_D)
class _A2_hi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A2_hi_Type.__name__=_B
_A2_hi_Object=MibScalar
a2_hi=_A2_hi_Object((1,3,6,1,4,1,9839,2,1,1,52),_A2_hi_Type())
a2_hi.setMaxAccess(_E)
if mibBuilder.loadTexts:a2_hi.setStatus(_A)
if mibBuilder.loadTexts:a2_hi.setUnits(_D)
class _A2_lo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A2_lo_Type.__name__=_B
_A2_lo_Object=MibScalar
a2_lo=_A2_lo_Object((1,3,6,1,4,1,9839,2,1,1,53),_A2_lo_Type())
a2_lo.setMaxAccess(_E)
if mibBuilder.loadTexts:a2_lo.setStatus(_A)
if mibBuilder.loadTexts:a2_lo.setUnits(_D)
class _A2_ha_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A2_ha_Type.__name__=_B
_A2_ha_Object=MibScalar
a2_ha=_A2_ha_Object((1,3,6,1,4,1,9839,2,1,1,54),_A2_ha_Type())
a2_ha.setMaxAccess(_E)
if mibBuilder.loadTexts:a2_ha.setStatus(_A)
if mibBuilder.loadTexts:a2_ha.setUnits(_D)
class _A2_hf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A2_hf_Type.__name__=_B
_A2_hf_Object=MibScalar
a2_hf=_A2_hf_Object((1,3,6,1,4,1,9839,2,1,1,55),_A2_hf_Type())
a2_hf.setMaxAccess(_E)
if mibBuilder.loadTexts:a2_hf.setStatus(_A)
if mibBuilder.loadTexts:a2_hf.setUnits(_D)
class _A2_ed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_A2_ed_Type.__name__=_B
_A2_ed_Object=MibScalar
a2_ed=_A2_ed_Object((1,3,6,1,4,1,9839,2,1,1,56),_A2_ed_Type())
a2_ed.setMaxAccess(_E)
if mibBuilder.loadTexts:a2_ed.setStatus(_A)
if mibBuilder.loadTexts:a2_ed.setUnits(_D)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Probeoffset_3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-199,199))
_Probeoffset_3_Type.__name__=_B
_Probeoffset_3_Object=MibScalar
probeoffset_3=_Probeoffset_3_Object((1,3,6,1,4,1,9839,2,1,2,1),_Probeoffset_3_Type())
probeoffset_3.setMaxAccess(_C)
if mibBuilder.loadTexts:probeoffset_3.setStatus(_A)
if mibBuilder.loadTexts:probeoffset_3.setUnits(_F)
class _Probeoffset_1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-199,199))
_Probeoffset_1_Type.__name__=_B
_Probeoffset_1_Object=MibScalar
probeoffset_1=_Probeoffset_1_Object((1,3,6,1,4,1,9839,2,1,2,2),_Probeoffset_1_Type())
probeoffset_1.setMaxAccess(_C)
if mibBuilder.loadTexts:probeoffset_1.setStatus(_A)
if mibBuilder.loadTexts:probeoffset_1.setUnits(_F)
class _Probeoffset_2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-199,199))
_Probeoffset_2_Type.__name__=_B
_Probeoffset_2_Object=MibScalar
probeoffset_2=_Probeoffset_2_Object((1,3,6,1,4,1,9839,2,1,2,3),_Probeoffset_2_Type())
probeoffset_2.setMaxAccess(_C)
if mibBuilder.loadTexts:probeoffset_2.setStatus(_A)
if mibBuilder.loadTexts:probeoffset_2.setUnits(_F)
class _Fan_alarm_hyst_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_Fan_alarm_hyst_Type.__name__=_B
_Fan_alarm_hyst_Object=MibScalar
fan_alarm_hyst=_Fan_alarm_hyst_Object((1,3,6,1,4,1,9839,2,1,2,4),_Fan_alarm_hyst_Type())
fan_alarm_hyst.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_alarm_hyst.setStatus(_A)
if mibBuilder.loadTexts:fan_alarm_hyst.setUnits(_F)
class _Alarm_max_delta_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1990))
_Alarm_max_delta_Type.__name__=_B
_Alarm_max_delta_Object=MibScalar
alarm_max_delta=_Alarm_max_delta_Object((1,3,6,1,4,1,9839,2,1,2,5),_Alarm_max_delta_Type())
alarm_max_delta.setMaxAccess(_C)
if mibBuilder.loadTexts:alarm_max_delta.setStatus(_A)
if mibBuilder.loadTexts:alarm_max_delta.setUnits(_F)
class _Alarm_min_delta_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1990))
_Alarm_min_delta_Type.__name__=_B
_Alarm_min_delta_Object=MibScalar
alarm_min_delta=_Alarm_min_delta_Object((1,3,6,1,4,1,9839,2,1,2,6),_Alarm_min_delta_Type())
alarm_min_delta.setMaxAccess(_C)
if mibBuilder.loadTexts:alarm_min_delta.setStatus(_A)
if mibBuilder.loadTexts:alarm_min_delta.setUnits(_F)
class _Defrost_end_temp_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,199))
_Defrost_end_temp_Type.__name__=_B
_Defrost_end_temp_Object=MibScalar
defrost_end_temp=_Defrost_end_temp_Object((1,3,6,1,4,1,9839,2,1,2,7),_Defrost_end_temp_Type())
defrost_end_temp.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_end_temp.setStatus(_A)
if mibBuilder.loadTexts:defrost_end_temp.setUnits(_F)
class _Fan_on_temp_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,500))
_Fan_on_temp_Type.__name__=_B
_Fan_on_temp_Object=MibScalar
fan_on_temp=_Fan_on_temp_Object((1,3,6,1,4,1,9839,2,1,2,8),_Fan_on_temp_Type())
fan_on_temp.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_on_temp.setStatus(_A)
if mibBuilder.loadTexts:fan_on_temp.setUnits(_F)
class _Setpoint_min_Type(Integer32):defaultValue=-500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,32767))
_Setpoint_min_Type.__name__=_B
_Setpoint_min_Object=MibScalar
setpoint_min=_Setpoint_min_Object((1,3,6,1,4,1,9839,2,1,2,9),_Setpoint_min_Type())
setpoint_min.setMaxAccess(_C)
if mibBuilder.loadTexts:setpoint_min.setStatus(_A)
if mibBuilder.loadTexts:setpoint_min.setUnits(_F)
class _Setpoint_max_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,1990))
_Setpoint_max_Type.__name__=_B
_Setpoint_max_Object=MibScalar
setpoint_max=_Setpoint_max_Object((1,3,6,1,4,1,9839,2,1,2,10),_Setpoint_max_Type())
setpoint_max.setMaxAccess(_C)
if mibBuilder.loadTexts:setpoint_max.setStatus(_A)
if mibBuilder.loadTexts:setpoint_max.setUnits(_F)
class _Setpoint_night_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-200,200))
_Setpoint_night_Type.__name__=_B
_Setpoint_night_Object=MibScalar
setpoint_night=_Setpoint_night_Object((1,3,6,1,4,1,9839,2,1,2,11),_Setpoint_night_Type())
setpoint_night.setMaxAccess(_C)
if mibBuilder.loadTexts:setpoint_night.setStatus(_A)
if mibBuilder.loadTexts:setpoint_night.setUnits(_F)
class _Reghyst_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Reghyst_Type.__name__=_B
_Reghyst_Object=MibScalar
reghyst=_Reghyst_Object((1,3,6,1,4,1,9839,2,1,2,12),_Reghyst_Type())
reghyst.setMaxAccess(_C)
if mibBuilder.loadTexts:reghyst.setStatus(_A)
if mibBuilder.loadTexts:reghyst.setUnits(_F)
class _Max_store_value_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Max_store_value_Type.__name__=_B
_Max_store_value_Object=MibScalar
max_store_value=_Max_store_value_Object((1,3,6,1,4,1,9839,2,1,2,13),_Max_store_value_Type())
max_store_value.setMaxAccess(_E)
if mibBuilder.loadTexts:max_store_value.setStatus(_A)
if mibBuilder.loadTexts:max_store_value.setUnits(_F)
class _Min_store_value_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Min_store_value_Type.__name__=_B
_Min_store_value_Object=MibScalar
min_store_value=_Min_store_value_Object((1,3,6,1,4,1,9839,2,1,2,14),_Min_store_value_Type())
min_store_value.setMaxAccess(_E)
if mibBuilder.loadTexts:min_store_value.setStatus(_A)
if mibBuilder.loadTexts:min_store_value.setUnits(_F)
class _Setpoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Setpoint_Type.__name__=_B
_Setpoint_Object=MibScalar
setpoint=_Setpoint_Object((1,3,6,1,4,1,9839,2,1,2,15),_Setpoint_Type())
setpoint.setMaxAccess(_C)
if mibBuilder.loadTexts:setpoint.setStatus(_A)
if mibBuilder.loadTexts:setpoint.setUnits(_F)
class _Probe_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Probe_1_Type.__name__=_B
_Probe_1_Object=MibScalar
probe_1=_Probe_1_Object((1,3,6,1,4,1,9839,2,1,2,26),_Probe_1_Type())
probe_1.setMaxAccess(_E)
if mibBuilder.loadTexts:probe_1.setStatus(_A)
if mibBuilder.loadTexts:probe_1.setUnits(_F)
class _Probe_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Probe_2_Type.__name__=_B
_Probe_2_Object=MibScalar
probe_2=_Probe_2_Object((1,3,6,1,4,1,9839,2,1,2,27),_Probe_2_Type())
probe_2.setMaxAccess(_E)
if mibBuilder.loadTexts:probe_2.setStatus(_A)
if mibBuilder.loadTexts:probe_2.setUnits(_F)
class _Probe_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Probe_3_Type.__name__=_B
_Probe_3_Object=MibScalar
probe_3=_Probe_3_Object((1,3,6,1,4,1,9839,2,1,2,28),_Probe_3_Type())
probe_3.setMaxAccess(_E)
if mibBuilder.loadTexts:probe_3.setStatus(_A)
if mibBuilder.loadTexts:probe_3.setUnits(_F)
class _Probe_virtual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Probe_virtual_Type.__name__=_B
_Probe_virtual_Object=MibScalar
probe_virtual=_Probe_virtual_Object((1,3,6,1,4,1,9839,2,1,2,29),_Probe_virtual_Type())
probe_virtual.setMaxAccess(_E)
if mibBuilder.loadTexts:probe_virtual.setStatus(_A)
if mibBuilder.loadTexts:probe_virtual.setUnits(_F)
class _Power_supply_voltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Power_supply_voltage_Type.__name__=_B
_Power_supply_voltage_Object=MibScalar
power_supply_voltage=_Power_supply_voltage_Object((1,3,6,1,4,1,9839,2,1,2,30),_Power_supply_voltage_Type())
power_supply_voltage.setMaxAccess(_E)
if mibBuilder.loadTexts:power_supply_voltage.setStatus(_A)
if mibBuilder.loadTexts:power_supply_voltage.setUnits('V x10')
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Probe_stability_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Probe_stability_Type.__name__=_B
_Probe_stability_Object=MibScalar
probe_stability=_Probe_stability_Object((1,3,6,1,4,1,9839,2,1,3,1),_Probe_stability_Type())
probe_stability.setMaxAccess(_C)
if mibBuilder.loadTexts:probe_stability.setStatus(_A)
if mibBuilder.loadTexts:probe_stability.setUnits(_D)
class _Virt_probe_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Virt_probe_Type.__name__=_B
_Virt_probe_Object=MibScalar
virt_probe=_Virt_probe_Object((1,3,6,1,4,1,9839,2,1,3,2),_Virt_probe_Type())
virt_probe.setMaxAccess(_C)
if mibBuilder.loadTexts:virt_probe.setStatus(_A)
if mibBuilder.loadTexts:virt_probe.setUnits(_D)
class _Showprobe_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Showprobe_Type.__name__=_B
_Showprobe_Object=MibScalar
showprobe=_Showprobe_Object((1,3,6,1,4,1,9839,2,1,3,3),_Showprobe_Type())
showprobe.setMaxAccess(_C)
if mibBuilder.loadTexts:showprobe.setStatus(_A)
if mibBuilder.loadTexts:showprobe.setUnits(_D)
class _Showprobe_t_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Showprobe_t_Type.__name__=_B
_Showprobe_t_Object=MibScalar
showprobe_t=_Showprobe_t_Object((1,3,6,1,4,1,9839,2,1,3,4),_Showprobe_t_Type())
showprobe_t.setMaxAccess(_C)
if mibBuilder.loadTexts:showprobe_t.setStatus(_A)
if mibBuilder.loadTexts:showprobe_t.setUnits(_D)
class _Defrostprobepresence_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Defrostprobepresence_Type.__name__=_B
_Defrostprobepresence_Object=MibScalar
defrostprobepresence=_Defrostprobepresence_Object((1,3,6,1,4,1,9839,2,1,3,5),_Defrostprobepresence_Type())
defrostprobepresence.setMaxAccess(_C)
if mibBuilder.loadTexts:defrostprobepresence.setStatus(_A)
if mibBuilder.loadTexts:defrostprobepresence.setUnits(_D)
class _Dig_in_cfg_1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dig_in_cfg_1_Type.__name__=_B
_Dig_in_cfg_1_Object=MibScalar
dig_in_cfg_1=_Dig_in_cfg_1_Object((1,3,6,1,4,1,9839,2,1,3,6),_Dig_in_cfg_1_Type())
dig_in_cfg_1.setMaxAccess(_C)
if mibBuilder.loadTexts:dig_in_cfg_1.setStatus(_A)
if mibBuilder.loadTexts:dig_in_cfg_1.setUnits(_D)
class _Dig_in_cfg_2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dig_in_cfg_2_Type.__name__=_B
_Dig_in_cfg_2_Object=MibScalar
dig_in_cfg_2=_Dig_in_cfg_2_Object((1,3,6,1,4,1,9839,2,1,3,7),_Dig_in_cfg_2_Type())
dig_in_cfg_2.setMaxAccess(_C)
if mibBuilder.loadTexts:dig_in_cfg_2.setStatus(_A)
if mibBuilder.loadTexts:dig_in_cfg_2.setUnits(_D)
class _Alarm_input_delay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Alarm_input_delay_Type.__name__=_B
_Alarm_input_delay_Object=MibScalar
alarm_input_delay=_Alarm_input_delay_Object((1,3,6,1,4,1,9839,2,1,3,8),_Alarm_input_delay_Type())
alarm_input_delay.setMaxAccess(_C)
if mibBuilder.loadTexts:alarm_input_delay.setStatus(_A)
if mibBuilder.loadTexts:alarm_input_delay.setUnits(_G)
class _Alarm_delay_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Alarm_delay_Type.__name__=_B
_Alarm_delay_Object=MibScalar
alarm_delay=_Alarm_delay_Object((1,3,6,1,4,1,9839,2,1,3,9),_Alarm_delay_Type())
alarm_delay.setMaxAccess(_C)
if mibBuilder.loadTexts:alarm_delay.setStatus(_A)
if mibBuilder.loadTexts:alarm_delay.setUnits(_G)
class _Comp_startup_delay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Comp_startup_delay_Type.__name__=_B
_Comp_startup_delay_Object=MibScalar
comp_startup_delay=_Comp_startup_delay_Object((1,3,6,1,4,1,9839,2,1,3,10),_Comp_startup_delay_Type())
comp_startup_delay.setMaxAccess(_C)
if mibBuilder.loadTexts:comp_startup_delay.setStatus(_A)
if mibBuilder.loadTexts:comp_startup_delay.setUnits(_I)
class _Comp_s2s_delay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Comp_s2s_delay_Type.__name__=_B
_Comp_s2s_delay_Object=MibScalar
comp_s2s_delay=_Comp_s2s_delay_Object((1,3,6,1,4,1,9839,2,1,3,11),_Comp_s2s_delay_Type())
comp_s2s_delay.setMaxAccess(_C)
if mibBuilder.loadTexts:comp_s2s_delay.setStatus(_A)
if mibBuilder.loadTexts:comp_s2s_delay.setUnits(_I)
class _Comp_min_off_time_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Comp_min_off_time_Type.__name__=_B
_Comp_min_off_time_Object=MibScalar
comp_min_off_time=_Comp_min_off_time_Object((1,3,6,1,4,1,9839,2,1,3,12),_Comp_min_off_time_Type())
comp_min_off_time.setMaxAccess(_C)
if mibBuilder.loadTexts:comp_min_off_time.setStatus(_A)
if mibBuilder.loadTexts:comp_min_off_time.setUnits(_I)
class _Comp_min_on_time_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Comp_min_on_time_Type.__name__=_B
_Comp_min_on_time_Object=MibScalar
comp_min_on_time=_Comp_min_on_time_Object((1,3,6,1,4,1,9839,2,1,3,13),_Comp_min_on_time_Type())
comp_min_on_time.setMaxAccess(_C)
if mibBuilder.loadTexts:comp_min_on_time.setStatus(_A)
if mibBuilder.loadTexts:comp_min_on_time.setUnits(_I)
class _Rele_safety_cycle_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Rele_safety_cycle_Type.__name__=_B
_Rele_safety_cycle_Object=MibScalar
rele_safety_cycle=_Rele_safety_cycle_Object((1,3,6,1,4,1,9839,2,1,3,14),_Rele_safety_cycle_Type())
rele_safety_cycle.setMaxAccess(_C)
if mibBuilder.loadTexts:rele_safety_cycle.setStatus(_A)
if mibBuilder.loadTexts:rele_safety_cycle.setUnits(_I)
class _Cc_alarm_delay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Cc_alarm_delay_Type.__name__=_B
_Cc_alarm_delay_Object=MibScalar
cc_alarm_delay=_Cc_alarm_delay_Object((1,3,6,1,4,1,9839,2,1,3,15),_Cc_alarm_delay_Type())
cc_alarm_delay.setMaxAccess(_C)
if mibBuilder.loadTexts:cc_alarm_delay.setStatus(_A)
if mibBuilder.loadTexts:cc_alarm_delay.setUnits('Hours')
class _Comp_cc_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Comp_cc_Type.__name__=_B
_Comp_cc_Object=MibScalar
comp_cc=_Comp_cc_Object((1,3,6,1,4,1,9839,2,1,3,16),_Comp_cc_Type())
comp_cc.setMaxAccess(_C)
if mibBuilder.loadTexts:comp_cc.setStatus(_A)
if mibBuilder.loadTexts:comp_cc.setUnits('Hours')
class _Defrost_type_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Defrost_type_Type.__name__=_B
_Defrost_type_Object=MibScalar
defrost_type=_Defrost_type_Object((1,3,6,1,4,1,9839,2,1,3,17),_Defrost_type_Type())
defrost_type.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_type.setStatus(_A)
if mibBuilder.loadTexts:defrost_type.setUnits(_D)
class _Defrost_delay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Defrost_delay_Type.__name__=_B
_Defrost_delay_Object=MibScalar
defrost_delay=_Defrost_delay_Object((1,3,6,1,4,1,9839,2,1,3,18),_Defrost_delay_Type())
defrost_delay.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_delay.setStatus(_A)
if mibBuilder.loadTexts:defrost_delay.setUnits(_G)
class _Alarm_delay_df_door_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Alarm_delay_df_door_Type.__name__=_B
_Alarm_delay_df_door_Object=MibScalar
alarm_delay_df_door=_Alarm_delay_df_door_Object((1,3,6,1,4,1,9839,2,1,3,19),_Alarm_delay_df_door_Type())
alarm_delay_df_door.setMaxAccess(_C)
if mibBuilder.loadTexts:alarm_delay_df_door.setStatus(_A)
if mibBuilder.loadTexts:alarm_delay_df_door.setUnits(_H)
class _Dripping_interval_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Dripping_interval_Type.__name__=_B
_Dripping_interval_Object=MibScalar
dripping_interval=_Dripping_interval_Object((1,3,6,1,4,1,9839,2,1,3,20),_Dripping_interval_Type())
dripping_interval.setMaxAccess(_C)
if mibBuilder.loadTexts:dripping_interval.setStatus(_A)
if mibBuilder.loadTexts:dripping_interval.setUnits(_G)
class _Defrost_interval_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Defrost_interval_Type.__name__=_B
_Defrost_interval_Object=MibScalar
defrost_interval=_Defrost_interval_Object((1,3,6,1,4,1,9839,2,1,3,21),_Defrost_interval_Type())
defrost_interval.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_interval.setStatus(_A)
if mibBuilder.loadTexts:defrost_interval.setUnits(_H)
class _Defrost_max_time_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_Defrost_max_time_Type.__name__=_B
_Defrost_max_time_Object=MibScalar
defrost_max_time=_Defrost_max_time_Object((1,3,6,1,4,1,9839,2,1,3,22),_Defrost_max_time_Type())
defrost_max_time.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_max_time.setStatus(_A)
if mibBuilder.loadTexts:defrost_max_time.setUnits(_G)
class _Fan_drip_interval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Fan_drip_interval_Type.__name__=_B
_Fan_drip_interval_Object=MibScalar
fan_drip_interval=_Fan_drip_interval_Object((1,3,6,1,4,1,9839,2,1,3,23),_Fan_drip_interval_Type())
fan_drip_interval.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_drip_interval.setStatus(_A)
if mibBuilder.loadTexts:fan_drip_interval.setUnits(_G)
class _Aux1_cfg_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Aux1_cfg_Type.__name__=_B
_Aux1_cfg_Object=MibScalar
aux1_cfg=_Aux1_cfg_Object((1,3,6,1,4,1,9839,2,1,3,24),_Aux1_cfg_Type())
aux1_cfg.setMaxAccess(_C)
if mibBuilder.loadTexts:aux1_cfg.setStatus(_A)
if mibBuilder.loadTexts:aux1_cfg.setUnits(_D)
class _Aux2_cfg_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Aux2_cfg_Type.__name__=_B
_Aux2_cfg_Object=MibScalar
aux2_cfg=_Aux2_cfg_Object((1,3,6,1,4,1,9839,2,1,3,25),_Aux2_cfg_Type())
aux2_cfg.setMaxAccess(_C)
if mibBuilder.loadTexts:aux2_cfg.setStatus(_A)
if mibBuilder.loadTexts:aux2_cfg.setUnits(_D)
class _Light_sens_1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Light_sens_1_Type.__name__=_B
_Light_sens_1_Object=MibScalar
light_sens_1=_Light_sens_1_Object((1,3,6,1,4,1,9839,2,1,3,26),_Light_sens_1_Type())
light_sens_1.setMaxAccess(_C)
if mibBuilder.loadTexts:light_sens_1.setStatus(_A)
if mibBuilder.loadTexts:light_sens_1.setUnits(_D)
class _Light_timer_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Light_timer_Type.__name__=_B
_Light_timer_Object=MibScalar
light_timer=_Light_timer_Object((1,3,6,1,4,1,9839,2,1,3,27),_Light_timer_Type())
light_timer.setMaxAccess(_C)
if mibBuilder.loadTexts:light_timer.setStatus(_A)
if mibBuilder.loadTexts:light_timer.setUnits(_G)
class _Minmax_acq_time_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Minmax_acq_time_Type.__name__=_B
_Minmax_acq_time_Object=MibScalar
minmax_acq_time=_Minmax_acq_time_Object((1,3,6,1,4,1,9839,2,1,3,28),_Minmax_acq_time_Type())
minmax_acq_time.setMaxAccess(_E)
if mibBuilder.loadTexts:minmax_acq_time.setStatus(_A)
if mibBuilder.loadTexts:minmax_acq_time.setUnits(_H)
class _Haccp_ha_day_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Haccp_ha_day_Type.__name__=_B
_Haccp_ha_day_Object=MibScalar
haccp_ha_day=_Haccp_ha_day_Object((1,3,6,1,4,1,9839,2,1,3,29),_Haccp_ha_day_Type())
haccp_ha_day.setMaxAccess(_E)
if mibBuilder.loadTexts:haccp_ha_day.setStatus(_A)
if mibBuilder.loadTexts:haccp_ha_day.setUnits(_D)
class _Haccp_ha_hour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Haccp_ha_hour_Type.__name__=_B
_Haccp_ha_hour_Object=MibScalar
haccp_ha_hour=_Haccp_ha_hour_Object((1,3,6,1,4,1,9839,2,1,3,30),_Haccp_ha_hour_Type())
haccp_ha_hour.setMaxAccess(_E)
if mibBuilder.loadTexts:haccp_ha_hour.setStatus(_A)
if mibBuilder.loadTexts:haccp_ha_hour.setUnits(_H)
class _Haccp_ha_min_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Haccp_ha_min_Type.__name__=_B
_Haccp_ha_min_Object=MibScalar
haccp_ha_min=_Haccp_ha_min_Object((1,3,6,1,4,1,9839,2,1,3,31),_Haccp_ha_min_Type())
haccp_ha_min.setMaxAccess(_E)
if mibBuilder.loadTexts:haccp_ha_min.setStatus(_A)
if mibBuilder.loadTexts:haccp_ha_min.setUnits(_I)
class _Haccp_hf_day_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Haccp_hf_day_Type.__name__=_B
_Haccp_hf_day_Object=MibScalar
haccp_hf_day=_Haccp_hf_day_Object((1,3,6,1,4,1,9839,2,1,3,32),_Haccp_hf_day_Type())
haccp_hf_day.setMaxAccess(_E)
if mibBuilder.loadTexts:haccp_hf_day.setStatus(_A)
if mibBuilder.loadTexts:haccp_hf_day.setUnits(_D)
class _Haccp_hf_hour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Haccp_hf_hour_Type.__name__=_B
_Haccp_hf_hour_Object=MibScalar
haccp_hf_hour=_Haccp_hf_hour_Object((1,3,6,1,4,1,9839,2,1,3,33),_Haccp_hf_hour_Type())
haccp_hf_hour.setMaxAccess(_E)
if mibBuilder.loadTexts:haccp_hf_hour.setStatus(_A)
if mibBuilder.loadTexts:haccp_hf_hour.setUnits(_H)
class _Haccp_hf_min_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Haccp_hf_min_Type.__name__=_B
_Haccp_hf_min_Object=MibScalar
haccp_hf_min=_Haccp_hf_min_Object((1,3,6,1,4,1,9839,2,1,3,34),_Haccp_hf_min_Type())
haccp_hf_min.setMaxAccess(_E)
if mibBuilder.loadTexts:haccp_hf_min.setStatus(_A)
if mibBuilder.loadTexts:haccp_hf_min.setUnits(_I)
class _Haccp_alarm_delay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Haccp_alarm_delay_Type.__name__=_B
_Haccp_alarm_delay_Object=MibScalar
haccp_alarm_delay=_Haccp_alarm_delay_Object((1,3,6,1,4,1,9839,2,1,3,35),_Haccp_alarm_delay_Type())
haccp_alarm_delay.setMaxAccess(_C)
if mibBuilder.loadTexts:haccp_alarm_delay.setStatus(_A)
if mibBuilder.loadTexts:haccp_alarm_delay.setUnits(_I)
class _Defrost_t1_dd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Defrost_t1_dd_Type.__name__=_B
_Defrost_t1_dd_Object=MibScalar
defrost_t1_dd=_Defrost_t1_dd_Object((1,3,6,1,4,1,9839,2,1,3,36),_Defrost_t1_dd_Type())
defrost_t1_dd.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t1_dd.setStatus(_A)
if mibBuilder.loadTexts:defrost_t1_dd.setUnits(_H)
class _Defrost_t1_hh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Defrost_t1_hh_Type.__name__=_B
_Defrost_t1_hh_Object=MibScalar
defrost_t1_hh=_Defrost_t1_hh_Object((1,3,6,1,4,1,9839,2,1,3,37),_Defrost_t1_hh_Type())
defrost_t1_hh.setMaxAccess(_E)
if mibBuilder.loadTexts:defrost_t1_hh.setStatus(_A)
if mibBuilder.loadTexts:defrost_t1_hh.setUnits(_D)
class _Defrost_t1_mm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Defrost_t1_mm_Type.__name__=_B
_Defrost_t1_mm_Object=MibScalar
defrost_t1_mm=_Defrost_t1_mm_Object((1,3,6,1,4,1,9839,2,1,3,38),_Defrost_t1_mm_Type())
defrost_t1_mm.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t1_mm.setStatus(_A)
if mibBuilder.loadTexts:defrost_t1_mm.setUnits(_I)
class _Defrost_t2_dd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Defrost_t2_dd_Type.__name__=_B
_Defrost_t2_dd_Object=MibScalar
defrost_t2_dd=_Defrost_t2_dd_Object((1,3,6,1,4,1,9839,2,1,3,39),_Defrost_t2_dd_Type())
defrost_t2_dd.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t2_dd.setStatus(_A)
if mibBuilder.loadTexts:defrost_t2_dd.setUnits(_J)
class _Defrost_t2_hh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Defrost_t2_hh_Type.__name__=_B
_Defrost_t2_hh_Object=MibScalar
defrost_t2_hh=_Defrost_t2_hh_Object((1,3,6,1,4,1,9839,2,1,3,40),_Defrost_t2_hh_Type())
defrost_t2_hh.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t2_hh.setStatus(_A)
if mibBuilder.loadTexts:defrost_t2_hh.setUnits(_H)
class _Defrost_t2_mm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Defrost_t2_mm_Type.__name__=_B
_Defrost_t2_mm_Object=MibScalar
defrost_t2_mm=_Defrost_t2_mm_Object((1,3,6,1,4,1,9839,2,1,3,41),_Defrost_t2_mm_Type())
defrost_t2_mm.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t2_mm.setStatus(_A)
if mibBuilder.loadTexts:defrost_t2_mm.setUnits(_G)
class _Defrost_t3_dd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Defrost_t3_dd_Type.__name__=_B
_Defrost_t3_dd_Object=MibScalar
defrost_t3_dd=_Defrost_t3_dd_Object((1,3,6,1,4,1,9839,2,1,3,42),_Defrost_t3_dd_Type())
defrost_t3_dd.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t3_dd.setStatus(_A)
if mibBuilder.loadTexts:defrost_t3_dd.setUnits(_J)
class _Defrost_t3_hh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Defrost_t3_hh_Type.__name__=_B
_Defrost_t3_hh_Object=MibScalar
defrost_t3_hh=_Defrost_t3_hh_Object((1,3,6,1,4,1,9839,2,1,3,43),_Defrost_t3_hh_Type())
defrost_t3_hh.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t3_hh.setStatus(_A)
if mibBuilder.loadTexts:defrost_t3_hh.setUnits(_H)
class _Defrost_t3_mm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Defrost_t3_mm_Type.__name__=_B
_Defrost_t3_mm_Object=MibScalar
defrost_t3_mm=_Defrost_t3_mm_Object((1,3,6,1,4,1,9839,2,1,3,44),_Defrost_t3_mm_Type())
defrost_t3_mm.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t3_mm.setStatus(_A)
if mibBuilder.loadTexts:defrost_t3_mm.setUnits(_G)
class _Defrost_t4_dd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Defrost_t4_dd_Type.__name__=_B
_Defrost_t4_dd_Object=MibScalar
defrost_t4_dd=_Defrost_t4_dd_Object((1,3,6,1,4,1,9839,2,1,3,45),_Defrost_t4_dd_Type())
defrost_t4_dd.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t4_dd.setStatus(_A)
if mibBuilder.loadTexts:defrost_t4_dd.setUnits(_J)
class _Defrost_t4_hh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Defrost_t4_hh_Type.__name__=_B
_Defrost_t4_hh_Object=MibScalar
defrost_t4_hh=_Defrost_t4_hh_Object((1,3,6,1,4,1,9839,2,1,3,46),_Defrost_t4_hh_Type())
defrost_t4_hh.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t4_hh.setStatus(_A)
if mibBuilder.loadTexts:defrost_t4_hh.setUnits(_H)
class _Defrost_t4_mm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Defrost_t4_mm_Type.__name__=_B
_Defrost_t4_mm_Object=MibScalar
defrost_t4_mm=_Defrost_t4_mm_Object((1,3,6,1,4,1,9839,2,1,3,47),_Defrost_t4_mm_Type())
defrost_t4_mm.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t4_mm.setStatus(_A)
if mibBuilder.loadTexts:defrost_t4_mm.setUnits(_G)
class _Defrost_t5_dd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Defrost_t5_dd_Type.__name__=_B
_Defrost_t5_dd_Object=MibScalar
defrost_t5_dd=_Defrost_t5_dd_Object((1,3,6,1,4,1,9839,2,1,3,48),_Defrost_t5_dd_Type())
defrost_t5_dd.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t5_dd.setStatus(_A)
if mibBuilder.loadTexts:defrost_t5_dd.setUnits(_J)
class _Defrost_t5_hh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Defrost_t5_hh_Type.__name__=_B
_Defrost_t5_hh_Object=MibScalar
defrost_t5_hh=_Defrost_t5_hh_Object((1,3,6,1,4,1,9839,2,1,3,49),_Defrost_t5_hh_Type())
defrost_t5_hh.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t5_hh.setStatus(_A)
if mibBuilder.loadTexts:defrost_t5_hh.setUnits(_H)
class _Defrost_t5_mm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Defrost_t5_mm_Type.__name__=_B
_Defrost_t5_mm_Object=MibScalar
defrost_t5_mm=_Defrost_t5_mm_Object((1,3,6,1,4,1,9839,2,1,3,50),_Defrost_t5_mm_Type())
defrost_t5_mm.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t5_mm.setStatus(_A)
if mibBuilder.loadTexts:defrost_t5_mm.setUnits(_G)
class _Defrost_t6_dd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Defrost_t6_dd_Type.__name__=_B
_Defrost_t6_dd_Object=MibScalar
defrost_t6_dd=_Defrost_t6_dd_Object((1,3,6,1,4,1,9839,2,1,3,51),_Defrost_t6_dd_Type())
defrost_t6_dd.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t6_dd.setStatus(_A)
if mibBuilder.loadTexts:defrost_t6_dd.setUnits(_J)
class _Defrost_t6_hh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Defrost_t6_hh_Type.__name__=_B
_Defrost_t6_hh_Object=MibScalar
defrost_t6_hh=_Defrost_t6_hh_Object((1,3,6,1,4,1,9839,2,1,3,52),_Defrost_t6_hh_Type())
defrost_t6_hh.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t6_hh.setStatus(_A)
if mibBuilder.loadTexts:defrost_t6_hh.setUnits(_H)
class _Defrost_t6_mm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Defrost_t6_mm_Type.__name__=_B
_Defrost_t6_mm_Object=MibScalar
defrost_t6_mm=_Defrost_t6_mm_Object((1,3,6,1,4,1,9839,2,1,3,53),_Defrost_t6_mm_Type())
defrost_t6_mm.setMaxAccess(_C)
if mibBuilder.loadTexts:defrost_t6_mm.setStatus(_A)
if mibBuilder.loadTexts:defrost_t6_mm.setUnits(_G)
class _Tm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Tm_Type.__name__=_B
_Tm_Object=MibScalar
tm=_Tm_Object((1,3,6,1,4,1,9839,2,1,3,54),_Tm_Type())
tm.setMaxAccess(_E)
if mibBuilder.loadTexts:tm.setStatus(_A)
if mibBuilder.loadTexts:tm.setUnits(_G)
class _Th_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Th_Type.__name__=_B
_Th_Object=MibScalar
th=_Th_Object((1,3,6,1,4,1,9839,2,1,3,55),_Th_Type())
th.setMaxAccess(_E)
if mibBuilder.loadTexts:th.setStatus(_A)
if mibBuilder.loadTexts:th.setUnits(_H)
class _Td_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Td_Type.__name__=_B
_Td_Object=MibScalar
td=_Td_Object((1,3,6,1,4,1,9839,2,1,3,56),_Td_Type())
td.setMaxAccess(_E)
if mibBuilder.loadTexts:td.setStatus(_A)
if mibBuilder.loadTexts:td.setUnits(_D)
mibBuilder.exportSymbols('CAREL-powersplit-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'powersplitMIB':powersplitMIB,'digitalObjects':digitalObjects,'cent_fhren_flag':cent_fhren_flag,'autoscale':autoscale,'defrostprobeselect':defrostprobeselect,'defrost_cmd':defrost_cmd,'defrost_at_startup':defrost_at_startup,'defrost_show':defrost_show,'defrost_priority':defrost_priority,'fan_cfg':fan_cfg,'fan_off_ctrl':fan_off_ctrl,'fan_defrost_ctrl':fan_defrost_ctrl,'keyb_disabled':keyb_disabled,'loc_on_off_ena':loc_on_off_ena,'lan_on_off_ena':lan_on_off_ena,'lan_din':lan_din,'defrost_tout_alarm_ena':defrost_tout_alarm_ena,'minmax_store_enable':minmax_store_enable,'night_reg_probe':night_reg_probe,'haccp_reset':haccp_reset,'dig_in_1':dig_in_1,'dig_in_2':dig_in_2,'s_comp':s_comp,'s_fan':s_fan,'s_defrost':s_defrost,'s_aux_2':s_aux_2,'s_alarm':s_alarm,'s_light':s_light,'dr_supervisor':dr_supervisor,'dr_svendreq':dr_svendreq,'a1_e1':a1_e1,'a1_e2':a1_e2,'a1_e3':a1_e3,'a1_ia':a1_ia,'a1_da':a1_da,'a1_ea':a1_ea,'a1_re':a1_re,'a1_id':a1_id,'a2_hi':a2_hi,'a2_lo':a2_lo,'a2_ha':a2_ha,'a2_hf':a2_hf,'a2_ed':a2_ed,'analogObjects':analogObjects,'probeoffset_3':probeoffset_3,'probeoffset_1':probeoffset_1,'probeoffset_2':probeoffset_2,'fan_alarm_hyst':fan_alarm_hyst,'alarm_max_delta':alarm_max_delta,'alarm_min_delta':alarm_min_delta,'defrost_end_temp':defrost_end_temp,'fan_on_temp':fan_on_temp,'setpoint_min':setpoint_min,'setpoint_max':setpoint_max,'setpoint_night':setpoint_night,'reghyst':reghyst,'max_store_value':max_store_value,'min_store_value':min_store_value,'setpoint':setpoint,'probe_1':probe_1,'probe_2':probe_2,'probe_3':probe_3,'probe_virtual':probe_virtual,'power_supply_voltage':power_supply_voltage,'integerObjects':integerObjects,'probe_stability':probe_stability,'virt_probe':virt_probe,'showprobe':showprobe,'showprobe_t':showprobe_t,'defrostprobepresence':defrostprobepresence,'dig_in_cfg_1':dig_in_cfg_1,'dig_in_cfg_2':dig_in_cfg_2,'alarm_input_delay':alarm_input_delay,'alarm_delay':alarm_delay,'comp_startup_delay':comp_startup_delay,'comp_s2s_delay':comp_s2s_delay,'comp_min_off_time':comp_min_off_time,'comp_min_on_time':comp_min_on_time,'rele_safety_cycle':rele_safety_cycle,'cc_alarm_delay':cc_alarm_delay,'comp_cc':comp_cc,'defrost_type':defrost_type,'defrost_delay':defrost_delay,'alarm_delay_df_door':alarm_delay_df_door,'dripping_interval':dripping_interval,'defrost_interval':defrost_interval,'defrost_max_time':defrost_max_time,'fan_drip_interval':fan_drip_interval,'aux1_cfg':aux1_cfg,'aux2_cfg':aux2_cfg,'light_sens_1':light_sens_1,'light_timer':light_timer,'minmax_acq_time':minmax_acq_time,'haccp_ha_day':haccp_ha_day,'haccp_ha_hour':haccp_ha_hour,'haccp_ha_min':haccp_ha_min,'haccp_hf_day':haccp_hf_day,'haccp_hf_hour':haccp_hf_hour,'haccp_hf_min':haccp_hf_min,'haccp_alarm_delay':haccp_alarm_delay,'defrost_t1_dd':defrost_t1_dd,'defrost_t1_hh':defrost_t1_hh,'defrost_t1_mm':defrost_t1_mm,'defrost_t2_dd':defrost_t2_dd,'defrost_t2_hh':defrost_t2_hh,'defrost_t2_mm':defrost_t2_mm,'defrost_t3_dd':defrost_t3_dd,'defrost_t3_hh':defrost_t3_hh,'defrost_t3_mm':defrost_t3_mm,'defrost_t4_dd':defrost_t4_dd,'defrost_t4_hh':defrost_t4_hh,'defrost_t4_mm':defrost_t4_mm,'defrost_t5_dd':defrost_t5_dd,'defrost_t5_hh':defrost_t5_hh,'defrost_t5_mm':defrost_t5_mm,'defrost_t6_dd':defrost_t6_dd,'defrost_t6_hh':defrost_t6_hh,'defrost_t6_mm':defrost_t6_mm,'tm':tm,'th':th,'td':td})