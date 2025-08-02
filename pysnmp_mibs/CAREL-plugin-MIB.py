_J='C x10'
_I='flags'
_H='C/F'
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
pluginMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
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
class _Unit_meas__5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Unit_meas__5_Type.__name__=_B
_Unit_meas__5_Object=MibScalar
unit_meas__5=_Unit_meas__5_Object((1,3,6,1,4,1,9839,2,1,1,1),_Unit_meas__5_Type())
unit_meas__5.setMaxAccess(_C)
if mibBuilder.loadTexts:unit_meas__5.setStatus(_A)
if mibBuilder.loadTexts:unit_meas__5.setUnits(_F)
class _En_alm_ed_r3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_alm_ed_r3_Type.__name__=_B
_En_alm_ed_r3_Object=MibScalar
en_alm_ed_r3=_En_alm_ed_r3_Object((1,3,6,1,4,1,9839,2,1,1,2),_En_alm_ed_r3_Type())
en_alm_ed_r3.setMaxAccess(_C)
if mibBuilder.loadTexts:en_alm_ed_r3.setStatus(_A)
if mibBuilder.loadTexts:en_alm_ed_r3.setUnits(_F)
class _Fan_mode_f0_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan_mode_f0_Type.__name__=_B
_Fan_mode_f0_Object=MibScalar
fan_mode_f0=_Fan_mode_f0_Object((1,3,6,1,4,1,9839,2,1,1,3),_Fan_mode_f0_Type())
fan_mode_f0.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_mode_f0.setStatus(_A)
if mibBuilder.loadTexts:fan_mode_f0.setUnits(_I)
class _Start_def_on_d4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Start_def_on_d4_Type.__name__=_B
_Start_def_on_d4_Object=MibScalar
start_def_on_d4=_Start_def_on_d4_Object((1,3,6,1,4,1,9839,2,1,1,4),_Start_def_on_d4_Type())
start_def_on_d4.setMaxAccess(_C)
if mibBuilder.loadTexts:start_def_on_d4.setStatus(_A)
if mibBuilder.loadTexts:start_def_on_d4.setUnits(_F)
class _Stop_vis_def_d6_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Stop_vis_def_d6_Type.__name__=_B
_Stop_vis_def_d6_Object=MibScalar
stop_vis_def_d6=_Stop_vis_def_d6_Object((1,3,6,1,4,1,9839,2,1,1,5),_Stop_vis_def_d6_Type())
stop_vis_def_d6.setMaxAccess(_C)
if mibBuilder.loadTexts:stop_vis_def_d6.setStatus(_A)
if mibBuilder.loadTexts:stop_vis_def_d6.setUnits(_F)
class _Def_priority_d9_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Def_priority_d9_Type.__name__=_B
_Def_priority_d9_Object=MibScalar
def_priority_d9=_Def_priority_d9_Object((1,3,6,1,4,1,9839,2,1,1,6),_Def_priority_d9_Type())
def_priority_d9.setMaxAccess(_C)
if mibBuilder.loadTexts:def_priority_d9.setStatus(_A)
if mibBuilder.loadTexts:def_priority_d9.setUnits(_F)
class _Time_base_dc_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Time_base_dc_Type.__name__=_B
_Time_base_dc_Object=MibScalar
time_base_dc=_Time_base_dc_Object((1,3,6,1,4,1,9839,2,1,1,7),_Time_base_dc_Type())
time_base_dc.setMaxAccess(_C)
if mibBuilder.loadTexts:time_base_dc.setStatus(_A)
if mibBuilder.loadTexts:time_base_dc.setUnits(_F)
class _Fan_cmp_off_f2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan_cmp_off_f2_Type.__name__=_B
_Fan_cmp_off_f2_Object=MibScalar
fan_cmp_off_f2=_Fan_cmp_off_f2_Object((1,3,6,1,4,1,9839,2,1,1,8),_Fan_cmp_off_f2_Type())
fan_cmp_off_f2.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_cmp_off_f2.setStatus(_A)
if mibBuilder.loadTexts:fan_cmp_off_f2.setUnits(_I)
class _Fan_off_def_f3_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan_off_def_f3_Type.__name__=_B
_Fan_off_def_f3_Object=MibScalar
fan_off_def_f3=_Fan_off_def_f3_Object((1,3,6,1,4,1,9839,2,1,1,9),_Fan_off_def_f3_Type())
fan_off_def_f3.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_off_def_f3.setStatus(_A)
if mibBuilder.loadTexts:fan_off_def_f3.setUnits(_I)
class _Dis_buzzer_h4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dis_buzzer_h4_Type.__name__=_B
_Dis_buzzer_h4_Object=MibScalar
dis_buzzer_h4=_Dis_buzzer_h4_Object((1,3,6,1,4,1,9839,2,1,1,10),_Dis_buzzer_h4_Type())
dis_buzzer_h4.setMaxAccess(_C)
if mibBuilder.loadTexts:dis_buzzer_h4.setStatus(_A)
if mibBuilder.loadTexts:dis_buzzer_h4.setUnits(_F)
class _Dis_keyb_h2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dis_keyb_h2_Type.__name__=_B
_Dis_keyb_h2_Object=MibScalar
dis_keyb_h2=_Dis_keyb_h2_Object((1,3,6,1,4,1,9839,2,1,1,11),_Dis_keyb_h2_Type())
dis_keyb_h2.setMaxAccess(_C)
if mibBuilder.loadTexts:dis_keyb_h2.setStatus(_A)
if mibBuilder.loadTexts:dis_keyb_h2.setUnits(_F)
class _Vis_probe__4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Vis_probe__4_Type.__name__=_B
_Vis_probe__4_Object=MibScalar
vis_probe__4=_Vis_probe__4_Object((1,3,6,1,4,1,9839,2,1,1,12),_Vis_probe__4_Type())
vis_probe__4.setMaxAccess(_C)
if mibBuilder.loadTexts:vis_probe__4.setStatus(_A)
if mibBuilder.loadTexts:vis_probe__4.setUnits(_F)
class _Al_probe1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Al_probe1_Type.__name__=_B
_Al_probe1_Object=MibScalar
al_probe1=_Al_probe1_Object((1,3,6,1,4,1,9839,2,1,1,18),_Al_probe1_Type())
al_probe1.setMaxAccess(_E)
if mibBuilder.loadTexts:al_probe1.setStatus(_A)
if mibBuilder.loadTexts:al_probe1.setUnits(_D)
class _Al_probe2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Al_probe2_Type.__name__=_B
_Al_probe2_Object=MibScalar
al_probe2=_Al_probe2_Object((1,3,6,1,4,1,9839,2,1,1,19),_Al_probe2_Type())
al_probe2.setMaxAccess(_E)
if mibBuilder.loadTexts:al_probe2.setStatus(_A)
if mibBuilder.loadTexts:al_probe2.setUnits(_D)
class _Al_ext_id_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Al_ext_id_Type.__name__=_B
_Al_ext_id_Object=MibScalar
al_ext_id=_Al_ext_id_Object((1,3,6,1,4,1,9839,2,1,1,20),_Al_ext_id_Type())
al_ext_id.setMaxAccess(_E)
if mibBuilder.loadTexts:al_ext_id.setStatus(_A)
if mibBuilder.loadTexts:al_ext_id.setUnits(_D)
class _Al_low_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Al_low_temp_Type.__name__=_B
_Al_low_temp_Object=MibScalar
al_low_temp=_Al_low_temp_Object((1,3,6,1,4,1,9839,2,1,1,21),_Al_low_temp_Type())
al_low_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:al_low_temp.setStatus(_A)
if mibBuilder.loadTexts:al_low_temp.setUnits(_D)
class _Al_hi_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Al_hi_temp_Type.__name__=_B
_Al_hi_temp_Object=MibScalar
al_hi_temp=_Al_hi_temp_Object((1,3,6,1,4,1,9839,2,1,1,22),_Al_hi_temp_Type())
al_hi_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:al_hi_temp.setStatus(_A)
if mibBuilder.loadTexts:al_hi_temp.setUnits(_D)
class _Al_ee_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Al_ee_Type.__name__=_B
_Al_ee_Object=MibScalar
al_ee=_Al_ee_Object((1,3,6,1,4,1,9839,2,1,1,23),_Al_ee_Type())
al_ee.setMaxAccess(_E)
if mibBuilder.loadTexts:al_ee.setStatus(_A)
if mibBuilder.loadTexts:al_ee.setUnits(_D)
class _Comp_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Comp_status_Type.__name__=_B
_Comp_status_Object=MibScalar
comp_status=_Comp_status_Object((1,3,6,1,4,1,9839,2,1,1,26),_Comp_status_Type())
comp_status.setMaxAccess(_E)
if mibBuilder.loadTexts:comp_status.setStatus(_A)
if mibBuilder.loadTexts:comp_status.setUnits(_D)
class _Fan_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan_status_Type.__name__=_B
_Fan_status_Object=MibScalar
fan_status=_Fan_status_Object((1,3,6,1,4,1,9839,2,1,1,27),_Fan_status_Type())
fan_status.setMaxAccess(_E)
if mibBuilder.loadTexts:fan_status.setStatus(_A)
if mibBuilder.loadTexts:fan_status.setUnits(_D)
class _Defrost_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Defrost_status_Type.__name__=_B
_Defrost_status_Object=MibScalar
defrost_status=_Defrost_status_Object((1,3,6,1,4,1,9839,2,1,1,28),_Defrost_status_Type())
defrost_status.setMaxAccess(_E)
if mibBuilder.loadTexts:defrost_status.setStatus(_A)
if mibBuilder.loadTexts:defrost_status.setUnits(_D)
class _Aux_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Aux_status_Type.__name__=_B
_Aux_status_Object=MibScalar
aux_status=_Aux_status_Object((1,3,6,1,4,1,9839,2,1,1,29),_Aux_status_Type())
aux_status.setMaxAccess(_E)
if mibBuilder.loadTexts:aux_status.setStatus(_A)
if mibBuilder.loadTexts:aux_status.setUnits(_D)
class _Di_glb_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Di_glb_status_Type.__name__=_B
_Di_glb_status_Object=MibScalar
di_glb_status=_Di_glb_status_Object((1,3,6,1,4,1,9839,2,1,1,35),_Di_glb_status_Type())
di_glb_status.setMaxAccess(_E)
if mibBuilder.loadTexts:di_glb_status.setStatus(_A)
if mibBuilder.loadTexts:di_glb_status.setUnits(_D)
class _Instr_connect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Instr_connect_Type.__name__=_B
_Instr_connect_Object=MibScalar
instr_connect=_Instr_connect_Object((1,3,6,1,4,1,9839,2,1,1,36),_Instr_connect_Type())
instr_connect.setMaxAccess(_E)
if mibBuilder.loadTexts:instr_connect.setStatus(_A)
if mibBuilder.loadTexts:instr_connect.setUnits(_D)
class _Al_low_voltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Al_low_voltage_Type.__name__=_B
_Al_low_voltage_Object=MibScalar
al_low_voltage=_Al_low_voltage_Object((1,3,6,1,4,1,9839,2,1,1,37),_Al_low_voltage_Type())
al_low_voltage.setMaxAccess(_E)
if mibBuilder.loadTexts:al_low_voltage.setStatus(_A)
if mibBuilder.loadTexts:al_low_voltage.setUnits(_D)
class _I2c_int_fail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_I2c_int_fail_Type.__name__=_B
_I2c_int_fail_Object=MibScalar
i2c_int_fail=_I2c_int_fail_Object((1,3,6,1,4,1,9839,2,1,1,38),_I2c_int_fail_Type())
i2c_int_fail.setMaxAccess(_E)
if mibBuilder.loadTexts:i2c_int_fail.setStatus(_A)
if mibBuilder.loadTexts:i2c_int_fail.setUnits(_D)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Probe_0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Probe_0_Type.__name__=_B
_Probe_0_Object=MibScalar
probe_0=_Probe_0_Object((1,3,6,1,4,1,9839,2,1,2,1),_Probe_0_Type())
probe_0.setMaxAccess(_E)
if mibBuilder.loadTexts:probe_0.setStatus(_A)
if mibBuilder.loadTexts:probe_0.setUnits(_J)
class _Probe_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Probe_1_Type.__name__=_B
_Probe_1_Object=MibScalar
probe_1=_Probe_1_Object((1,3,6,1,4,1,9839,2,1,2,2),_Probe_1_Type())
probe_1.setMaxAccess(_E)
if mibBuilder.loadTexts:probe_1.setStatus(_A)
if mibBuilder.loadTexts:probe_1.setUnits(_J)
class _Probe_cal__c_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_Probe_cal__c_Type.__name__=_B
_Probe_cal__c_Object=MibScalar
probe_cal__c=_Probe_cal__c_Object((1,3,6,1,4,1,9839,2,1,2,3),_Probe_cal__c_Type())
probe_cal__c.setMaxAccess(_C)
if mibBuilder.loadTexts:probe_cal__c.setStatus(_A)
if mibBuilder.loadTexts:probe_cal__c.setUnits(_J)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _T_on_fan_f1_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,127))
_T_on_fan_f1_Type.__name__=_B
_T_on_fan_f1_Object=MibScalar
t_on_fan_f1=_T_on_fan_f1_Object((1,3,6,1,4,1,9839,2,1,3,18),_T_on_fan_f1_Type())
t_on_fan_f1.setMaxAccess(_C)
if mibBuilder.loadTexts:t_on_fan_f1.setStatus(_A)
if mibBuilder.loadTexts:t_on_fan_f1.setUnits(_H)
class _Tm_postdripp_fd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Tm_postdripp_fd_Type.__name__=_B
_Tm_postdripp_fd_Object=MibScalar
tm_postdripp_fd=_Tm_postdripp_fd_Object((1,3,6,1,4,1,9839,2,1,3,19),_Tm_postdripp_fd_Type())
tm_postdripp_fd.setMaxAccess(_C)
if mibBuilder.loadTexts:tm_postdripp_fd.setStatus(_A)
if mibBuilder.loadTexts:tm_postdripp_fd.setUnits(_G)
class _Setpoint_l1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,127))
_Setpoint_l1_Type.__name__=_B
_Setpoint_l1_Object=MibScalar
setpoint_l1=_Setpoint_l1_Object((1,3,6,1,4,1,9839,2,1,3,21),_Setpoint_l1_Type())
setpoint_l1.setMaxAccess(_C)
if mibBuilder.loadTexts:setpoint_l1.setStatus(_A)
if mibBuilder.loadTexts:setpoint_l1.setUnits('C')
class _Stability__2_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Stability__2_Type.__name__=_B
_Stability__2_Object=MibScalar
stability__2=_Stability__2_Object((1,3,6,1,4,1,9839,2,1,3,23),_Stability__2_Type())
stability__2.setMaxAccess(_C)
if mibBuilder.loadTexts:stability__2.setStatus(_A)
if mibBuilder.loadTexts:stability__2.setUnits(_D)
class _Min_setp_r1_Type(Integer32):defaultValue=-50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,32767))
_Min_setp_r1_Type.__name__=_B
_Min_setp_r1_Object=MibScalar
min_setp_r1=_Min_setp_r1_Object((1,3,6,1,4,1,9839,2,1,3,24),_Min_setp_r1_Type())
min_setp_r1.setMaxAccess(_C)
if mibBuilder.loadTexts:min_setp_r1.setStatus(_A)
if mibBuilder.loadTexts:min_setp_r1.setUnits(_H)
class _Max_setp_r2_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,127))
_Max_setp_r2_Type.__name__=_B
_Max_setp_r2_Object=MibScalar
max_setp_r2=_Max_setp_r2_Object((1,3,6,1,4,1,9839,2,1,3,25),_Max_setp_r2_Type())
max_setp_r2.setMaxAccess(_C)
if mibBuilder.loadTexts:max_setp_r2.setStatus(_A)
if mibBuilder.loadTexts:max_setp_r2.setUnits(_H)
class _Differ_rd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_Differ_rd_Type.__name__=_B
_Differ_rd_Object=MibScalar
differ_rd=_Differ_rd_Object((1,3,6,1,4,1,9839,2,1,3,26),_Differ_rd_Type())
differ_rd.setMaxAccess(_C)
if mibBuilder.loadTexts:differ_rd.setStatus(_A)
if mibBuilder.loadTexts:differ_rd.setUnits(_H)
class _Ngt_setp_var_r4_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_Ngt_setp_var_r4_Type.__name__=_B
_Ngt_setp_var_r4_Object=MibScalar
ngt_setp_var_r4=_Ngt_setp_var_r4_Object((1,3,6,1,4,1,9839,2,1,3,27),_Ngt_setp_var_r4_Type())
ngt_setp_var_r4.setMaxAccess(_C)
if mibBuilder.loadTexts:ngt_setp_var_r4.setStatus(_A)
if mibBuilder.loadTexts:ngt_setp_var_r4.setUnits(_H)
class _Thr_lt_al_al_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_Thr_lt_al_al_Type.__name__=_B
_Thr_lt_al_al_Object=MibScalar
thr_lt_al_al=_Thr_lt_al_al_Object((1,3,6,1,4,1,9839,2,1,3,28),_Thr_lt_al_al_Type())
thr_lt_al_al.setMaxAccess(_C)
if mibBuilder.loadTexts:thr_lt_al_al.setStatus(_A)
if mibBuilder.loadTexts:thr_lt_al_al.setUnits(_H)
class _Thr_ht_al_ah_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_Thr_ht_al_ah_Type.__name__=_B
_Thr_ht_al_ah_Object=MibScalar
thr_ht_al_ah=_Thr_ht_al_ah_Object((1,3,6,1,4,1,9839,2,1,3,29),_Thr_ht_al_ah_Type())
thr_ht_al_ah.setMaxAccess(_C)
if mibBuilder.loadTexts:thr_ht_al_ah.setStatus(_A)
if mibBuilder.loadTexts:thr_ht_al_ah.setUnits(_H)
class _Id_al_delay_a7_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Id_al_delay_a7_Type.__name__=_B
_Id_al_delay_a7_Object=MibScalar
id_al_delay_a7=_Id_al_delay_a7_Object((1,3,6,1,4,1,9839,2,1,3,30),_Id_al_delay_a7_Type())
id_al_delay_a7.setMaxAccess(_C)
if mibBuilder.loadTexts:id_al_delay_a7.setStatus(_A)
if mibBuilder.loadTexts:id_al_delay_a7.setUnits(_G)
class _Conf_id_a4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Conf_id_a4_Type.__name__=_B
_Conf_id_a4_Object=MibScalar
conf_id_a4=_Conf_id_a4_Object((1,3,6,1,4,1,9839,2,1,3,31),_Conf_id_a4_Type())
conf_id_a4.setMaxAccess(_C)
if mibBuilder.loadTexts:conf_id_a4.setStatus(_A)
if mibBuilder.loadTexts:conf_id_a4.setUnits(_D)
class _Comp_delay_c0_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Comp_delay_c0_Type.__name__=_B
_Comp_delay_c0_Object=MibScalar
comp_delay_c0=_Comp_delay_c0_Object((1,3,6,1,4,1,9839,2,1,3,32),_Comp_delay_c0_Type())
comp_delay_c0.setMaxAccess(_C)
if mibBuilder.loadTexts:comp_delay_c0.setStatus(_A)
if mibBuilder.loadTexts:comp_delay_c0.setUnits(_G)
class _T_al_delay_ad_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_T_al_delay_ad_Type.__name__=_B
_T_al_delay_ad_Object=MibScalar
t_al_delay_ad=_T_al_delay_ad_Object((1,3,6,1,4,1,9839,2,1,3,33),_T_al_delay_ad_Type())
t_al_delay_ad.setMaxAccess(_C)
if mibBuilder.loadTexts:t_al_delay_ad.setStatus(_A)
if mibBuilder.loadTexts:t_al_delay_ad.setUnits(_G)
class _Keycode_sv_h5_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,99))
_Keycode_sv_h5_Type.__name__=_B
_Keycode_sv_h5_Object=MibScalar
keycode_sv_h5=_Keycode_sv_h5_Object((1,3,6,1,4,1,9839,2,1,3,34),_Keycode_sv_h5_Type())
keycode_sv_h5.setMaxAccess(_C)
if mibBuilder.loadTexts:keycode_sv_h5.setStatus(_A)
if mibBuilder.loadTexts:keycode_sv_h5.setUnits(_D)
class _En_def_mf_h1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_def_mf_h1_Type.__name__=_B
_En_def_mf_h1_Object=MibScalar
en_def_mf_h1=_En_def_mf_h1_Object((1,3,6,1,4,1,9839,2,1,3,35),_En_def_mf_h1_Type())
en_def_mf_h1.setMaxAccess(_C)
if mibBuilder.loadTexts:en_def_mf_h1.setStatus(_A)
if mibBuilder.loadTexts:en_def_mf_h1.setUnits(_F)
class _T_betw_2_on_c1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_T_betw_2_on_c1_Type.__name__=_B
_T_betw_2_on_c1_Object=MibScalar
t_betw_2_on_c1=_T_betw_2_on_c1_Object((1,3,6,1,4,1,9839,2,1,3,36),_T_betw_2_on_c1_Type())
t_betw_2_on_c1.setMaxAccess(_C)
if mibBuilder.loadTexts:t_betw_2_on_c1.setStatus(_A)
if mibBuilder.loadTexts:t_betw_2_on_c1.setUnits(_G)
class _Min_off_time_c2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Min_off_time_c2_Type.__name__=_B
_Min_off_time_c2_Object=MibScalar
min_off_time_c2=_Min_off_time_c2_Object((1,3,6,1,4,1,9839,2,1,3,37),_Min_off_time_c2_Type())
min_off_time_c2.setMaxAccess(_C)
if mibBuilder.loadTexts:min_off_time_c2.setStatus(_A)
if mibBuilder.loadTexts:min_off_time_c2.setUnits(_G)
class _Min_on_time_c3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Min_on_time_c3_Type.__name__=_B
_Min_on_time_c3_Object=MibScalar
min_on_time_c3=_Min_on_time_c3_Object((1,3,6,1,4,1,9839,2,1,3,38),_Min_on_time_c3_Type())
min_on_time_c3.setMaxAccess(_C)
if mibBuilder.loadTexts:min_on_time_c3.setStatus(_A)
if mibBuilder.loadTexts:min_on_time_c3.setUnits(_G)
class _T_safe_relay_c4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_T_safe_relay_c4_Type.__name__=_B
_T_safe_relay_c4_Object=MibScalar
t_safe_relay_c4=_T_safe_relay_c4_Object((1,3,6,1,4,1,9839,2,1,3,39),_T_safe_relay_c4_Type())
t_safe_relay_c4.setMaxAccess(_C)
if mibBuilder.loadTexts:t_safe_relay_c4.setStatus(_A)
if mibBuilder.loadTexts:t_safe_relay_c4.setUnits(_G)
class _Cont_cycle_cc_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Cont_cycle_cc_Type.__name__=_B
_Cont_cycle_cc_Object=MibScalar
cont_cycle_cc=_Cont_cycle_cc_Object((1,3,6,1,4,1,9839,2,1,3,40),_Cont_cycle_cc_Type())
cont_cycle_cc.setMaxAccess(_C)
if mibBuilder.loadTexts:cont_cycle_cc.setStatus(_A)
if mibBuilder.loadTexts:cont_cycle_cc.setUnits('hours')
class _Offal_postcc_c6_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Offal_postcc_c6_Type.__name__=_B
_Offal_postcc_c6_Object=MibScalar
offal_postcc_c6=_Offal_postcc_c6_Object((1,3,6,1,4,1,9839,2,1,3,41),_Offal_postcc_c6_Type())
offal_postcc_c6.setMaxAccess(_C)
if mibBuilder.loadTexts:offal_postcc_c6.setStatus(_A)
if mibBuilder.loadTexts:offal_postcc_c6.setUnits('hours')
class _Def_type_d0_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Def_type_d0_Type.__name__=_B
_Def_type_d0_Object=MibScalar
def_type_d0=_Def_type_d0_Object((1,3,6,1,4,1,9839,2,1,3,42),_Def_type_d0_Type())
def_type_d0.setMaxAccess(_C)
if mibBuilder.loadTexts:def_type_d0.setStatus(_A)
if mibBuilder.loadTexts:def_type_d0.setUnits(_F)
class _T_betw_def_dl_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_T_betw_def_dl_Type.__name__=_B
_T_betw_def_dl_Object=MibScalar
t_betw_def_dl=_T_betw_def_dl_Object((1,3,6,1,4,1,9839,2,1,3,43),_T_betw_def_dl_Type())
t_betw_def_dl.setMaxAccess(_C)
if mibBuilder.loadTexts:t_betw_def_dl.setStatus(_A)
if mibBuilder.loadTexts:t_betw_def_dl.setUnits('hour/min')
class _Def_end_t_dt_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,127))
_Def_end_t_dt_Type.__name__=_B
_Def_end_t_dt_Object=MibScalar
def_end_t_dt=_Def_end_t_dt_Object((1,3,6,1,4,1,9839,2,1,3,44),_Def_end_t_dt_Type())
def_end_t_dt.setMaxAccess(_C)
if mibBuilder.loadTexts:def_end_t_dt.setStatus(_A)
if mibBuilder.loadTexts:def_end_t_dt.setUnits(_H)
class _Def_durat_dp_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_Def_durat_dp_Type.__name__=_B
_Def_durat_dp_Object=MibScalar
def_durat_dp=_Def_durat_dp_Object((1,3,6,1,4,1,9839,2,1,3,45),_Def_durat_dp_Type())
def_durat_dp.setMaxAccess(_C)
if mibBuilder.loadTexts:def_durat_dp.setStatus(_A)
if mibBuilder.loadTexts:def_durat_dp.setUnits(_G)
class _Def_delay_d5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,199))
_Def_delay_d5_Type.__name__=_B
_Def_delay_d5_Object=MibScalar
def_delay_d5=_Def_delay_d5_Object((1,3,6,1,4,1,9839,2,1,3,46),_Def_delay_d5_Type())
def_delay_d5.setMaxAccess(_C)
if mibBuilder.loadTexts:def_delay_d5.setStatus(_A)
if mibBuilder.loadTexts:def_delay_d5.setUnits(_G)
class _Postdef_dr_t_dd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Postdef_dr_t_dd_Type.__name__=_B
_Postdef_dr_t_dd_Object=MibScalar
postdef_dr_t_dd=_Postdef_dr_t_dd_Object((1,3,6,1,4,1,9839,2,1,3,47),_Postdef_dr_t_dd_Type())
postdef_dr_t_dd.setMaxAccess(_C)
if mibBuilder.loadTexts:postdef_dr_t_dd.setStatus(_A)
if mibBuilder.loadTexts:postdef_dr_t_dd.setUnits(_G)
class _T_al_exc_def_d8_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_T_al_exc_def_d8_Type.__name__=_B
_T_al_exc_def_d8_Object=MibScalar
t_al_exc_def_d8=_T_al_exc_def_d8_Object((1,3,6,1,4,1,9839,2,1,3,48),_T_al_exc_def_d8_Type())
t_al_exc_def_d8.setMaxAccess(_C)
if mibBuilder.loadTexts:t_al_exc_def_d8.setStatus(_A)
if mibBuilder.loadTexts:t_al_exc_def_d8.setUnits('Hours')
class _Diff_al_fan_a0_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_Diff_al_fan_a0_Type.__name__=_B
_Diff_al_fan_a0_Object=MibScalar
diff_al_fan_a0=_Diff_al_fan_a0_Object((1,3,6,1,4,1,9839,2,1,3,49),_Diff_al_fan_a0_Type())
diff_al_fan_a0.setMaxAccess(_C)
if mibBuilder.loadTexts:diff_al_fan_a0.setStatus(_A)
if mibBuilder.loadTexts:diff_al_fan_a0.setUnits(_H)
mibBuilder.exportSymbols('CAREL-plugin-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'pluginMIB':pluginMIB,'digitalObjects':digitalObjects,'unit_meas__5':unit_meas__5,'en_alm_ed_r3':en_alm_ed_r3,'fan_mode_f0':fan_mode_f0,'start_def_on_d4':start_def_on_d4,'stop_vis_def_d6':stop_vis_def_d6,'def_priority_d9':def_priority_d9,'time_base_dc':time_base_dc,'fan_cmp_off_f2':fan_cmp_off_f2,'fan_off_def_f3':fan_off_def_f3,'dis_buzzer_h4':dis_buzzer_h4,'dis_keyb_h2':dis_keyb_h2,'vis_probe__4':vis_probe__4,'al_probe1':al_probe1,'al_probe2':al_probe2,'al_ext_id':al_ext_id,'al_low_temp':al_low_temp,'al_hi_temp':al_hi_temp,'al_ee':al_ee,'comp_status':comp_status,'fan_status':fan_status,'defrost_status':defrost_status,'aux_status':aux_status,'di_glb_status':di_glb_status,'instr_connect':instr_connect,'al_low_voltage':al_low_voltage,'i2c_int_fail':i2c_int_fail,'analogObjects':analogObjects,'probe_0':probe_0,'probe_1':probe_1,'probe_cal__c':probe_cal__c,'integerObjects':integerObjects,'t_on_fan_f1':t_on_fan_f1,'tm_postdripp_fd':tm_postdripp_fd,'setpoint_l1':setpoint_l1,'stability__2':stability__2,'min_setp_r1':min_setp_r1,'max_setp_r2':max_setp_r2,'differ_rd':differ_rd,'ngt_setp_var_r4':ngt_setp_var_r4,'thr_lt_al_al':thr_lt_al_al,'thr_ht_al_ah':thr_ht_al_ah,'id_al_delay_a7':id_al_delay_a7,'conf_id_a4':conf_id_a4,'comp_delay_c0':comp_delay_c0,'t_al_delay_ad':t_al_delay_ad,'keycode_sv_h5':keycode_sv_h5,'en_def_mf_h1':en_def_mf_h1,'t_betw_2_on_c1':t_betw_2_on_c1,'min_off_time_c2':min_off_time_c2,'min_on_time_c3':min_on_time_c3,'t_safe_relay_c4':t_safe_relay_c4,'cont_cycle_cc':cont_cycle_cc,'offal_postcc_c6':offal_postcc_c6,'def_type_d0':def_type_d0,'t_betw_def_dl':t_betw_def_dl,'def_end_t_dt':def_end_t_dt,'def_durat_dp':def_durat_dp,'def_delay_d5':def_delay_d5,'postdef_dr_t_dd':postdef_dr_t_dd,'t_al_exc_def_d8':t_al_exc_def_d8,'diff_al_fan_a0':diff_al_fan_a0})