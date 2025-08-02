_F='C/F x10'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='N/A'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysContact,sysLocation,sysName=mibBuilder.importSymbols('SNMPv2-MIB','sysContact','sysLocation','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
screw_compressorMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_B)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentCode.setStatus(_A)
if mibBuilder.loadTexts:agentCode.setUnits(_B)
_Instruments_ObjectIdentity=ObjectIdentity
instruments=_Instruments_ObjectIdentity((1,3,6,1,4,1,9839,2))
_WebGateInfo_ObjectIdentity=ObjectIdentity
webGateInfo=_WebGateInfo_ObjectIdentity((1,3,6,1,4,1,9839,2,0))
_AgentParameters_ObjectIdentity=ObjectIdentity
agentParameters=_AgentParameters_ObjectIdentity((1,3,6,1,4,1,9839,2,0,1))
class _NetSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NetSize_Type.__name__=_C
_NetSize_Object=MibScalar
netSize=_NetSize_Object((1,3,6,1,4,1,9839,2,0,1,1),_NetSize_Type())
netSize.setMaxAccess(_E)
if mibBuilder.loadTexts:netSize.setStatus(_A)
if mibBuilder.loadTexts:netSize.setUnits(_B)
class _BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200))
_BaudRate_Type.__name__=_C
_BaudRate_Object=MibScalar
baudRate=_BaudRate_Object((1,3,6,1,4,1,9839,2,0,1,2),_BaudRate_Type())
baudRate.setMaxAccess(_E)
if mibBuilder.loadTexts:baudRate.setStatus(_A)
if mibBuilder.loadTexts:baudRate.setUnits(_B)
_UnitTypeGroup_ObjectIdentity=ObjectIdentity
unitTypeGroup=_UnitTypeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,2))
_Unit1_Type_Type=DisplayString
_Unit1_Type_Object=MibScalar
unit1_Type=_Unit1_Type_Object((1,3,6,1,4,1,9839,2,0,2,1),_Unit1_Type_Type())
unit1_Type.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_B)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_B)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_B)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_B)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_B)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_B)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_B)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_B)
_UnitOnLineStatusGroup_ObjectIdentity=ObjectIdentity
unitOnLineStatusGroup=_UnitOnLineStatusGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_Unit1_OnLineStatus_Type=Integer32
_Unit1_OnLineStatus_Object=MibScalar
unit1_OnLineStatus=_Unit1_OnLineStatus_Object((1,3,6,1,4,1,9839,2,0,10,1),_Unit1_OnLineStatus_Type())
unit1_OnLineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_OnLineStatus.setStatus(_A)
if mibBuilder.loadTexts:unit1_OnLineStatus.setUnits(_B)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _Syson_s_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Syson_s_Type.__name__=_C
_Syson_s_Object=MibScalar
syson_s=_Syson_s_Object((1,3,6,1,4,1,9839,2,1,1,1),_Syson_s_Type())
syson_s.setMaxAccess(_D)
if mibBuilder.loadTexts:syson_s.setStatus(_A)
if mibBuilder.loadTexts:syson_s.setUnits(_B)
class _Dout_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_1_Type.__name__=_C
_Dout_1_Object=MibScalar
dout_1=_Dout_1_Object((1,3,6,1,4,1,9839,2,1,1,2),_Dout_1_Type())
dout_1.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_1.setStatus(_A)
if mibBuilder.loadTexts:dout_1.setUnits(_B)
class _Dout_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_2_Type.__name__=_C
_Dout_2_Object=MibScalar
dout_2=_Dout_2_Object((1,3,6,1,4,1,9839,2,1,1,3),_Dout_2_Type())
dout_2.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_2.setStatus(_A)
if mibBuilder.loadTexts:dout_2.setUnits(_B)
class _Dout_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_3_Type.__name__=_C
_Dout_3_Object=MibScalar
dout_3=_Dout_3_Object((1,3,6,1,4,1,9839,2,1,1,4),_Dout_3_Type())
dout_3.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_3.setStatus(_A)
if mibBuilder.loadTexts:dout_3.setUnits(_B)
class _Dout_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_4_Type.__name__=_C
_Dout_4_Object=MibScalar
dout_4=_Dout_4_Object((1,3,6,1,4,1,9839,2,1,1,5),_Dout_4_Type())
dout_4.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_4.setStatus(_A)
if mibBuilder.loadTexts:dout_4.setUnits(_B)
class _Dout_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_5_Type.__name__=_C
_Dout_5_Object=MibScalar
dout_5=_Dout_5_Object((1,3,6,1,4,1,9839,2,1,1,6),_Dout_5_Type())
dout_5.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_5.setStatus(_A)
if mibBuilder.loadTexts:dout_5.setUnits(_B)
class _Dout_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_6_Type.__name__=_C
_Dout_6_Object=MibScalar
dout_6=_Dout_6_Object((1,3,6,1,4,1,9839,2,1,1,7),_Dout_6_Type())
dout_6.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_6.setStatus(_A)
if mibBuilder.loadTexts:dout_6.setUnits(_B)
class _Dout_7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_7_Type.__name__=_C
_Dout_7_Object=MibScalar
dout_7=_Dout_7_Object((1,3,6,1,4,1,9839,2,1,1,8),_Dout_7_Type())
dout_7.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_7.setStatus(_A)
if mibBuilder.loadTexts:dout_7.setUnits(_B)
class _Dout_8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_8_Type.__name__=_C
_Dout_8_Object=MibScalar
dout_8=_Dout_8_Object((1,3,6,1,4,1,9839,2,1,1,9),_Dout_8_Type())
dout_8.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_8.setStatus(_A)
if mibBuilder.loadTexts:dout_8.setUnits(_B)
class _Dout_9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_9_Type.__name__=_C
_Dout_9_Object=MibScalar
dout_9=_Dout_9_Object((1,3,6,1,4,1,9839,2,1,1,10),_Dout_9_Type())
dout_9.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_9.setStatus(_A)
if mibBuilder.loadTexts:dout_9.setUnits(_B)
class _Dout_10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_10_Type.__name__=_C
_Dout_10_Object=MibScalar
dout_10=_Dout_10_Object((1,3,6,1,4,1,9839,2,1,1,11),_Dout_10_Type())
dout_10.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_10.setStatus(_A)
if mibBuilder.loadTexts:dout_10.setUnits(_B)
class _Dout_11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_11_Type.__name__=_C
_Dout_11_Object=MibScalar
dout_11=_Dout_11_Object((1,3,6,1,4,1,9839,2,1,1,12),_Dout_11_Type())
dout_11.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_11.setStatus(_A)
if mibBuilder.loadTexts:dout_11.setUnits(_B)
class _Dout_12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_12_Type.__name__=_C
_Dout_12_Object=MibScalar
dout_12=_Dout_12_Object((1,3,6,1,4,1,9839,2,1,1,13),_Dout_12_Type())
dout_12.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_12.setStatus(_A)
if mibBuilder.loadTexts:dout_12.setUnits(_B)
class _Dout_13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_13_Type.__name__=_C
_Dout_13_Object=MibScalar
dout_13=_Dout_13_Object((1,3,6,1,4,1,9839,2,1,1,14),_Dout_13_Type())
dout_13.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_13.setStatus(_A)
if mibBuilder.loadTexts:dout_13.setUnits(_B)
class _En_evap_flow_al_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_evap_flow_al_Type.__name__=_C
_En_evap_flow_al_Object=MibScalar
en_evap_flow_al=_En_evap_flow_al_Object((1,3,6,1,4,1,9839,2,1,1,15),_En_evap_flow_al_Type())
en_evap_flow_al.setMaxAccess(_D)
if mibBuilder.loadTexts:en_evap_flow_al.setStatus(_A)
if mibBuilder.loadTexts:en_evap_flow_al.setUnits(_B)
class _En_b1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b1_Type.__name__=_C
_En_b1_Object=MibScalar
en_b1=_En_b1_Object((1,3,6,1,4,1,9839,2,1,1,16),_En_b1_Type())
en_b1.setMaxAccess(_D)
if mibBuilder.loadTexts:en_b1.setStatus(_A)
if mibBuilder.loadTexts:en_b1.setUnits(_B)
class _En_b2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b2_Type.__name__=_C
_En_b2_Object=MibScalar
en_b2=_En_b2_Object((1,3,6,1,4,1,9839,2,1,1,17),_En_b2_Type())
en_b2.setMaxAccess(_D)
if mibBuilder.loadTexts:en_b2.setStatus(_A)
if mibBuilder.loadTexts:en_b2.setUnits(_B)
class _En_b3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b3_Type.__name__=_C
_En_b3_Object=MibScalar
en_b3=_En_b3_Object((1,3,6,1,4,1,9839,2,1,1,18),_En_b3_Type())
en_b3.setMaxAccess(_D)
if mibBuilder.loadTexts:en_b3.setStatus(_A)
if mibBuilder.loadTexts:en_b3.setUnits(_B)
class _En_b4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b4_Type.__name__=_C
_En_b4_Object=MibScalar
en_b4=_En_b4_Object((1,3,6,1,4,1,9839,2,1,1,19),_En_b4_Type())
en_b4.setMaxAccess(_D)
if mibBuilder.loadTexts:en_b4.setStatus(_A)
if mibBuilder.loadTexts:en_b4.setUnits(_B)
class _En_b5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b5_Type.__name__=_C
_En_b5_Object=MibScalar
en_b5=_En_b5_Object((1,3,6,1,4,1,9839,2,1,1,20),_En_b5_Type())
en_b5.setMaxAccess(_D)
if mibBuilder.loadTexts:en_b5.setStatus(_A)
if mibBuilder.loadTexts:en_b5.setUnits(_B)
class _En_b6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b6_Type.__name__=_C
_En_b6_Object=MibScalar
en_b6=_En_b6_Object((1,3,6,1,4,1,9839,2,1,1,21),_En_b6_Type())
en_b6.setMaxAccess(_D)
if mibBuilder.loadTexts:en_b6.setStatus(_A)
if mibBuilder.loadTexts:en_b6.setUnits(_B)
class _En_b7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b7_Type.__name__=_C
_En_b7_Object=MibScalar
en_b7=_En_b7_Object((1,3,6,1,4,1,9839,2,1,1,22),_En_b7_Type())
en_b7.setMaxAccess(_D)
if mibBuilder.loadTexts:en_b7.setStatus(_A)
if mibBuilder.loadTexts:en_b7.setUnits(_B)
class _En_b8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b8_Type.__name__=_C
_En_b8_Object=MibScalar
en_b8=_En_b8_Object((1,3,6,1,4,1,9839,2,1,1,23),_En_b8_Type())
en_b8.setMaxAccess(_D)
if mibBuilder.loadTexts:en_b8.setStatus(_A)
if mibBuilder.loadTexts:en_b8.setUnits(_B)
class _Superv_onoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Superv_onoff_Type.__name__=_C
_Superv_onoff_Object=MibScalar
superv_onoff=_Superv_onoff_Object((1,3,6,1,4,1,9839,2,1,1,24),_Superv_onoff_Type())
superv_onoff.setMaxAccess(_E)
if mibBuilder.loadTexts:superv_onoff.setStatus(_A)
if mibBuilder.loadTexts:superv_onoff.setUnits(_B)
class _En_start_restr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_start_restr_Type.__name__=_C
_En_start_restr_Object=MibScalar
en_start_restr=_En_start_restr_Object((1,3,6,1,4,1,9839,2,1,1,25),_En_start_restr_Type())
en_start_restr.setMaxAccess(_D)
if mibBuilder.loadTexts:en_start_restr.setStatus(_A)
if mibBuilder.loadTexts:en_start_restr.setUnits(_B)
class _En_modulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_modulation_Type.__name__=_C
_En_modulation_Object=MibScalar
en_modulation=_En_modulation_Object((1,3,6,1,4,1,9839,2,1,1,26),_En_modulation_Type())
en_modulation.setMaxAccess(_D)
if mibBuilder.loadTexts:en_modulation.setStatus(_A)
if mibBuilder.loadTexts:en_modulation.setUnits(_B)
class _Sun_win_sel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sun_win_sel_Type.__name__=_C
_Sun_win_sel_Object=MibScalar
sun_win_sel=_Sun_win_sel_Object((1,3,6,1,4,1,9839,2,1,1,27),_Sun_win_sel_Type())
sun_win_sel.setMaxAccess(_D)
if mibBuilder.loadTexts:sun_win_sel.setStatus(_A)
if mibBuilder.loadTexts:sun_win_sel.setUnits(_B)
class _Cooling_heating_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cooling_heating_Type.__name__=_C
_Cooling_heating_Object=MibScalar
cooling_heating=_Cooling_heating_Object((1,3,6,1,4,1,9839,2,1,1,29),_Cooling_heating_Type())
cooling_heating.setMaxAccess(_D)
if mibBuilder.loadTexts:cooling_heating.setStatus(_A)
if mibBuilder.loadTexts:cooling_heating.setUnits(_B)
class _Inverter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inverter_Type.__name__=_C
_Inverter_Object=MibScalar
inverter=_Inverter_Object((1,3,6,1,4,1,9839,2,1,1,30),_Inverter_Type())
inverter.setMaxAccess(_D)
if mibBuilder.loadTexts:inverter.setStatus(_A)
if mibBuilder.loadTexts:inverter.setUnits(_B)
class _Mal_freeze_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_freeze_Type.__name__=_C
_Mal_freeze_Object=MibScalar
mal_freeze=_Mal_freeze_Object((1,3,6,1,4,1,9839,2,1,1,46),_Mal_freeze_Type())
mal_freeze.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_freeze.setStatus(_A)
if mibBuilder.loadTexts:mal_freeze.setUnits(_B)
class _Mal_comp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_comp_Type.__name__=_C
_Mal_comp_Object=MibScalar
mal_comp=_Mal_comp_Object((1,3,6,1,4,1,9839,2,1,1,47),_Mal_comp_Type())
mal_comp.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_comp.setStatus(_A)
if mibBuilder.loadTexts:mal_comp.setUnits(_B)
class _Mal_evap_flow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_evap_flow_Type.__name__=_C
_Mal_evap_flow_Object=MibScalar
mal_evap_flow=_Mal_evap_flow_Object((1,3,6,1,4,1,9839,2,1,1,48),_Mal_evap_flow_Type())
mal_evap_flow.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_evap_flow.setStatus(_A)
if mibBuilder.loadTexts:mal_evap_flow.setUnits(_B)
class _Mal_cond_flow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_cond_flow_Type.__name__=_C
_Mal_cond_flow_Object=MibScalar
mal_cond_flow=_Mal_cond_flow_Object((1,3,6,1,4,1,9839,2,1,1,49),_Mal_cond_flow_Type())
mal_cond_flow.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_cond_flow.setStatus(_A)
if mibBuilder.loadTexts:mal_cond_flow.setUnits(_B)
class _Mal_high_press_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_high_press_Type.__name__=_C
_Mal_high_press_Object=MibScalar
mal_high_press=_Mal_high_press_Object((1,3,6,1,4,1,9839,2,1,1,50),_Mal_high_press_Type())
mal_high_press.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_high_press.setStatus(_A)
if mibBuilder.loadTexts:mal_high_press.setUnits(_B)
class _Mal_oil_level_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_oil_level_Type.__name__=_C
_Mal_oil_level_Object=MibScalar
mal_oil_level=_Mal_oil_level_Object((1,3,6,1,4,1,9839,2,1,1,51),_Mal_oil_level_Type())
mal_oil_level.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_oil_level.setStatus(_A)
if mibBuilder.loadTexts:mal_oil_level.setUnits(_B)
class _Mal_low_pres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_low_pres_Type.__name__=_C
_Mal_low_pres_Object=MibScalar
mal_low_pres=_Mal_low_pres_Object((1,3,6,1,4,1,9839,2,1,1,52),_Mal_low_pres_Type())
mal_low_pres.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_low_pres.setStatus(_A)
if mibBuilder.loadTexts:mal_low_pres.setUnits(_B)
class _Mal_hp_transd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_hp_transd_Type.__name__=_C
_Mal_hp_transd_Object=MibScalar
mal_hp_transd=_Mal_hp_transd_Object((1,3,6,1,4,1,9839,2,1,1,53),_Mal_hp_transd_Type())
mal_hp_transd.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_hp_transd.setStatus(_A)
if mibBuilder.loadTexts:mal_hp_transd.setUnits(_B)
class _Mal_serious_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_serious_Type.__name__=_C
_Mal_serious_Object=MibScalar
mal_serious=_Mal_serious_Object((1,3,6,1,4,1,9839,2,1,1,54),_Mal_serious_Type())
mal_serious.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_serious.setStatus(_A)
if mibBuilder.loadTexts:mal_serious.setUnits(_B)
class _Mal_fan1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_fan1_Type.__name__=_C
_Mal_fan1_Object=MibScalar
mal_fan1=_Mal_fan1_Object((1,3,6,1,4,1,9839,2,1,1,55),_Mal_fan1_Type())
mal_fan1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_fan1.setStatus(_A)
if mibBuilder.loadTexts:mal_fan1.setUnits(_B)
class _Mal_fan2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_fan2_Type.__name__=_C
_Mal_fan2_Object=MibScalar
mal_fan2=_Mal_fan2_Object((1,3,6,1,4,1,9839,2,1,1,56),_Mal_fan2_Type())
mal_fan2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_fan2.setStatus(_A)
if mibBuilder.loadTexts:mal_fan2.setUnits(_B)
class _Mal_pump_evap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_pump_evap_Type.__name__=_C
_Mal_pump_evap_Object=MibScalar
mal_pump_evap=_Mal_pump_evap_Object((1,3,6,1,4,1,9839,2,1,1,57),_Mal_pump_evap_Type())
mal_pump_evap.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_pump_evap.setStatus(_A)
if mibBuilder.loadTexts:mal_pump_evap.setUnits(_B)
class _Mal_master_offl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_master_offl_Type.__name__=_C
_Mal_master_offl_Object=MibScalar
mal_master_offl=_Mal_master_offl_Object((1,3,6,1,4,1,9839,2,1,1,58),_Mal_master_offl_Type())
mal_master_offl.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_master_offl.setStatus(_A)
if mibBuilder.loadTexts:mal_master_offl.setUnits(_B)
class _Mal_unit2_offl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_unit2_offl_Type.__name__=_C
_Mal_unit2_offl_Object=MibScalar
mal_unit2_offl=_Mal_unit2_offl_Object((1,3,6,1,4,1,9839,2,1,1,59),_Mal_unit2_offl_Type())
mal_unit2_offl.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_unit2_offl.setStatus(_A)
if mibBuilder.loadTexts:mal_unit2_offl.setUnits(_B)
class _Mal_unit3_offl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_unit3_offl_Type.__name__=_C
_Mal_unit3_offl_Object=MibScalar
mal_unit3_offl=_Mal_unit3_offl_Object((1,3,6,1,4,1,9839,2,1,1,60),_Mal_unit3_offl_Type())
mal_unit3_offl.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_unit3_offl.setStatus(_A)
if mibBuilder.loadTexts:mal_unit3_offl.setUnits(_B)
class _Mal_unit4_offl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_unit4_offl_Type.__name__=_C
_Mal_unit4_offl_Object=MibScalar
mal_unit4_offl=_Mal_unit4_offl_Object((1,3,6,1,4,1,9839,2,1,1,61),_Mal_unit4_offl_Type())
mal_unit4_offl.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_unit4_offl.setStatus(_A)
if mibBuilder.loadTexts:mal_unit4_offl.setUnits(_B)
class _Mal_b1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b1_Type.__name__=_C
_Mal_b1_Object=MibScalar
mal_b1=_Mal_b1_Object((1,3,6,1,4,1,9839,2,1,1,62),_Mal_b1_Type())
mal_b1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b1.setStatus(_A)
if mibBuilder.loadTexts:mal_b1.setUnits(_B)
class _Mal_b2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b2_Type.__name__=_C
_Mal_b2_Object=MibScalar
mal_b2=_Mal_b2_Object((1,3,6,1,4,1,9839,2,1,1,63),_Mal_b2_Type())
mal_b2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b2.setStatus(_A)
if mibBuilder.loadTexts:mal_b2.setUnits(_B)
class _Mal_b3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b3_Type.__name__=_C
_Mal_b3_Object=MibScalar
mal_b3=_Mal_b3_Object((1,3,6,1,4,1,9839,2,1,1,64),_Mal_b3_Type())
mal_b3.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b3.setStatus(_A)
if mibBuilder.loadTexts:mal_b3.setUnits(_B)
class _Mal_b4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b4_Type.__name__=_C
_Mal_b4_Object=MibScalar
mal_b4=_Mal_b4_Object((1,3,6,1,4,1,9839,2,1,1,65),_Mal_b4_Type())
mal_b4.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b4.setStatus(_A)
if mibBuilder.loadTexts:mal_b4.setUnits(_B)
class _Mal_b5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b5_Type.__name__=_C
_Mal_b5_Object=MibScalar
mal_b5=_Mal_b5_Object((1,3,6,1,4,1,9839,2,1,1,66),_Mal_b5_Type())
mal_b5.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b5.setStatus(_A)
if mibBuilder.loadTexts:mal_b5.setUnits(_B)
class _Mal_b6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b6_Type.__name__=_C
_Mal_b6_Object=MibScalar
mal_b6=_Mal_b6_Object((1,3,6,1,4,1,9839,2,1,1,67),_Mal_b6_Type())
mal_b6.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b6.setStatus(_A)
if mibBuilder.loadTexts:mal_b6.setUnits(_B)
class _Mal_b7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b7_Type.__name__=_C
_Mal_b7_Object=MibScalar
mal_b7=_Mal_b7_Object((1,3,6,1,4,1,9839,2,1,1,68),_Mal_b7_Type())
mal_b7.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b7.setStatus(_A)
if mibBuilder.loadTexts:mal_b7.setUnits(_B)
class _Mal_b8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b8_Type.__name__=_C
_Mal_b8_Object=MibScalar
mal_b8=_Mal_b8_Object((1,3,6,1,4,1,9839,2,1,1,69),_Mal_b8_Type())
mal_b8.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b8.setStatus(_A)
if mibBuilder.loadTexts:mal_b8.setUnits(_B)
class _Mal_pump_cond_h_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_pump_cond_h_Type.__name__=_C
_Mal_pump_cond_h_Object=MibScalar
mal_pump_cond_h=_Mal_pump_cond_h_Object((1,3,6,1,4,1,9839,2,1,1,70),_Mal_pump_cond_h_Type())
mal_pump_cond_h.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_pump_cond_h.setStatus(_A)
if mibBuilder.loadTexts:mal_pump_cond_h.setUnits(_B)
class _Mal_comp_hour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_comp_hour_Type.__name__=_C
_Mal_comp_hour_Object=MibScalar
mal_comp_hour=_Mal_comp_hour_Object((1,3,6,1,4,1,9839,2,1,1,71),_Mal_comp_hour_Type())
mal_comp_hour.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_comp_hour.setStatus(_A)
if mibBuilder.loadTexts:mal_comp_hour.setUnits(_B)
class _Mal_pump_cond_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_pump_cond_Type.__name__=_C
_Mal_pump_cond_Object=MibScalar
mal_pump_cond=_Mal_pump_cond_Object((1,3,6,1,4,1,9839,2,1,1,72),_Mal_pump_cond_Type())
mal_pump_cond.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_pump_cond.setStatus(_A)
if mibBuilder.loadTexts:mal_pump_cond.setUnits(_B)
class _Mal_clock32_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_clock32_Type.__name__=_C
_Mal_clock32_Object=MibScalar
mal_clock32=_Mal_clock32_Object((1,3,6,1,4,1,9839,2,1,1,73),_Mal_clock32_Type())
mal_clock32.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_clock32.setStatus(_A)
if mibBuilder.loadTexts:mal_clock32.setUnits(_B)
class _Mal_phase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_phase_Type.__name__=_C
_Mal_phase_Object=MibScalar
mal_phase=_Mal_phase_Object((1,3,6,1,4,1,9839,2,1,1,74),_Mal_phase_Type())
mal_phase.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_phase.setStatus(_A)
if mibBuilder.loadTexts:mal_phase.setUnits(_B)
class _Mal_ld_transd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_ld_transd_Type.__name__=_C
_Mal_ld_transd_Object=MibScalar
mal_ld_transd=_Mal_ld_transd_Object((1,3,6,1,4,1,9839,2,1,1,75),_Mal_ld_transd_Type())
mal_ld_transd.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_ld_transd.setStatus(_A)
if mibBuilder.loadTexts:mal_ld_transd.setUnits(_B)
class _Mal_voltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_voltage_Type.__name__=_C
_Mal_voltage_Object=MibScalar
mal_voltage=_Mal_voltage_Object((1,3,6,1,4,1,9839,2,1,1,76),_Mal_voltage_Type())
mal_voltage.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_voltage.setStatus(_A)
if mibBuilder.loadTexts:mal_voltage.setUnits(_B)
class _Mal_current_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_current_Type.__name__=_C
_Mal_current_Object=MibScalar
mal_current=_Mal_current_Object((1,3,6,1,4,1,9839,2,1,1,77),_Mal_current_Type())
mal_current.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_current.setStatus(_A)
if mibBuilder.loadTexts:mal_current.setUnits(_B)
class _Mal_pump_ev_h_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_pump_ev_h_Type.__name__=_C
_Mal_pump_ev_h_Object=MibScalar
mal_pump_ev_h=_Mal_pump_ev_h_Object((1,3,6,1,4,1,9839,2,1,1,78),_Mal_pump_ev_h_Type())
mal_pump_ev_h.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_pump_ev_h.setStatus(_A)
if mibBuilder.loadTexts:mal_pump_ev_h.setUnits(_B)
class _Mal_disch_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_disch_temp_Type.__name__=_C
_Mal_disch_temp_Object=MibScalar
mal_disch_temp=_Mal_disch_temp_Object((1,3,6,1,4,1,9839,2,1,1,80),_Mal_disch_temp_Type())
mal_disch_temp.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_disch_temp.setStatus(_A)
if mibBuilder.loadTexts:mal_disch_temp.setUnits(_B)
class _Mal_diff_pres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_diff_pres_Type.__name__=_C
_Mal_diff_pres_Object=MibScalar
mal_diff_pres=_Mal_diff_pres_Object((1,3,6,1,4,1,9839,2,1,1,81),_Mal_diff_pres_Type())
mal_diff_pres.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_diff_pres.setStatus(_A)
if mibBuilder.loadTexts:mal_diff_pres.setUnits(_B)
class _Mal_alco1_67_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_67_r_Type.__name__=_C
_Mal_alco1_67_r_Object=MibScalar
mal_alco1_67_r=_Mal_alco1_67_r_Object((1,3,6,1,4,1,9839,2,1,1,82),_Mal_alco1_67_r_Type())
mal_alco1_67_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_67_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_67_r.setUnits(_B)
class _Mal_alco1_68_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_68_r_Type.__name__=_C
_Mal_alco1_68_r_Object=MibScalar
mal_alco1_68_r=_Mal_alco1_68_r_Object((1,3,6,1,4,1,9839,2,1,1,83),_Mal_alco1_68_r_Type())
mal_alco1_68_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_68_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_68_r.setUnits(_B)
class _Mal_alco1_69_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_69_r_Type.__name__=_C
_Mal_alco1_69_r_Object=MibScalar
mal_alco1_69_r=_Mal_alco1_69_r_Object((1,3,6,1,4,1,9839,2,1,1,84),_Mal_alco1_69_r_Type())
mal_alco1_69_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_69_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_69_r.setUnits(_B)
class _Mal_alco1_70_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_70_r_Type.__name__=_C
_Mal_alco1_70_r_Object=MibScalar
mal_alco1_70_r=_Mal_alco1_70_r_Object((1,3,6,1,4,1,9839,2,1,1,85),_Mal_alco1_70_r_Type())
mal_alco1_70_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_70_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_70_r.setUnits(_B)
class _Mal_alco1_71_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_71_r_Type.__name__=_C
_Mal_alco1_71_r_Object=MibScalar
mal_alco1_71_r=_Mal_alco1_71_r_Object((1,3,6,1,4,1,9839,2,1,1,86),_Mal_alco1_71_r_Type())
mal_alco1_71_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_71_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_71_r.setUnits(_B)
class _Mal_alco1_72_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_72_r_Type.__name__=_C
_Mal_alco1_72_r_Object=MibScalar
mal_alco1_72_r=_Mal_alco1_72_r_Object((1,3,6,1,4,1,9839,2,1,1,87),_Mal_alco1_72_r_Type())
mal_alco1_72_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_72_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_72_r.setUnits(_B)
class _Mal_alco1_73_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_73_r_Type.__name__=_C
_Mal_alco1_73_r_Object=MibScalar
mal_alco1_73_r=_Mal_alco1_73_r_Object((1,3,6,1,4,1,9839,2,1,1,88),_Mal_alco1_73_r_Type())
mal_alco1_73_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_73_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_73_r.setUnits(_B)
class _Mal_alco1_74_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_74_r_Type.__name__=_C
_Mal_alco1_74_r_Object=MibScalar
mal_alco1_74_r=_Mal_alco1_74_r_Object((1,3,6,1,4,1,9839,2,1,1,89),_Mal_alco1_74_r_Type())
mal_alco1_74_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_74_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_74_r.setUnits(_B)
class _Mal_alco1_75_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_75_r_Type.__name__=_C
_Mal_alco1_75_r_Object=MibScalar
mal_alco1_75_r=_Mal_alco1_75_r_Object((1,3,6,1,4,1,9839,2,1,1,90),_Mal_alco1_75_r_Type())
mal_alco1_75_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_75_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_75_r.setUnits(_B)
class _Mal_alco1_760_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_760_r_Type.__name__=_C
_Mal_alco1_760_r_Object=MibScalar
mal_alco1_760_r=_Mal_alco1_760_r_Object((1,3,6,1,4,1,9839,2,1,1,91),_Mal_alco1_760_r_Type())
mal_alco1_760_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_760_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_760_r.setUnits(_B)
class _Mal_alco1_97_r_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_alco1_97_r_Type.__name__=_C
_Mal_alco1_97_r_Object=MibScalar
mal_alco1_97_r=_Mal_alco1_97_r_Object((1,3,6,1,4,1,9839,2,1,1,92),_Mal_alco1_97_r_Type())
mal_alco1_97_r.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_alco1_97_r.setStatus(_A)
if mibBuilder.loadTexts:mal_alco1_97_r.setUnits(_B)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Ain_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_1_Type.__name__=_C
_Ain_1_Object=MibScalar
ain_1=_Ain_1_Object((1,3,6,1,4,1,9839,2,1,2,1),_Ain_1_Type())
ain_1.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_1.setStatus(_A)
if mibBuilder.loadTexts:ain_1.setUnits(_F)
class _Ain_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_2_Type.__name__=_C
_Ain_2_Object=MibScalar
ain_2=_Ain_2_Object((1,3,6,1,4,1,9839,2,1,2,2),_Ain_2_Type())
ain_2.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_2.setStatus(_A)
if mibBuilder.loadTexts:ain_2.setUnits(_F)
class _Ain_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_3_Type.__name__=_C
_Ain_3_Object=MibScalar
ain_3=_Ain_3_Object((1,3,6,1,4,1,9839,2,1,2,3),_Ain_3_Type())
ain_3.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_3.setStatus(_A)
if mibBuilder.loadTexts:ain_3.setUnits(_F)
class _Ain_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_5_Type.__name__=_C
_Ain_5_Object=MibScalar
ain_5=_Ain_5_Object((1,3,6,1,4,1,9839,2,1,2,5),_Ain_5_Type())
ain_5.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_5.setStatus(_A)
if mibBuilder.loadTexts:ain_5.setUnits('V/A/C x10')
class _Ain_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_6_Type.__name__=_C
_Ain_6_Object=MibScalar
ain_6=_Ain_6_Object((1,3,6,1,4,1,9839,2,1,2,6),_Ain_6_Type())
ain_6.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_6.setStatus(_A)
if mibBuilder.loadTexts:ain_6.setUnits(_B)
class _Ain_7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_7_Type.__name__=_C
_Ain_7_Object=MibScalar
ain_7=_Ain_7_Object((1,3,6,1,4,1,9839,2,1,2,7),_Ain_7_Type())
ain_7.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_7.setStatus(_A)
if mibBuilder.loadTexts:ain_7.setUnits('% x10')
class _Ain_8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_8_Type.__name__=_C
_Ain_8_Object=MibScalar
ain_8=_Ain_8_Object((1,3,6,1,4,1,9839,2,1,2,8),_Ain_8_Type())
ain_8.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_8.setStatus(_A)
if mibBuilder.loadTexts:ain_8.setUnits(_B)
class _Aout_1_display_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Aout_1_display_Type.__name__=_C
_Aout_1_display_Object=MibScalar
aout_1_display=_Aout_1_display_Object((1,3,6,1,4,1,9839,2,1,2,9),_Aout_1_display_Type())
aout_1_display.setMaxAccess(_D)
if mibBuilder.loadTexts:aout_1_display.setStatus(_A)
if mibBuilder.loadTexts:aout_1_display.setUnits(_B)
class _S_temp_setpoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_S_temp_setpoint_Type.__name__=_C
_S_temp_setpoint_Object=MibScalar
s_temp_setpoint=_S_temp_setpoint_Object((1,3,6,1,4,1,9839,2,1,2,11),_S_temp_setpoint_Type())
s_temp_setpoint.setMaxAccess(_E)
if mibBuilder.loadTexts:s_temp_setpoint.setStatus(_A)
if mibBuilder.loadTexts:s_temp_setpoint.setUnits(_B)
class _W_temp_setpoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_W_temp_setpoint_Type.__name__=_C
_W_temp_setpoint_Object=MibScalar
w_temp_setpoint=_W_temp_setpoint_Object((1,3,6,1,4,1,9839,2,1,2,12),_W_temp_setpoint_Type())
w_temp_setpoint.setMaxAccess(_E)
if mibBuilder.loadTexts:w_temp_setpoint.setStatus(_A)
if mibBuilder.loadTexts:w_temp_setpoint.setUnits(_B)
class _Cond_setpoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Cond_setpoint_Type.__name__=_C
_Cond_setpoint_Object=MibScalar
cond_setpoint=_Cond_setpoint_Object((1,3,6,1,4,1,9839,2,1,2,13),_Cond_setpoint_Type())
cond_setpoint.setMaxAccess(_E)
if mibBuilder.loadTexts:cond_setpoint.setStatus(_A)
if mibBuilder.loadTexts:cond_setpoint.setUnits(_B)
class _In_temp_band_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_In_temp_band_Type.__name__=_C
_In_temp_band_Object=MibScalar
in_temp_band=_In_temp_band_Object((1,3,6,1,4,1,9839,2,1,2,14),_In_temp_band_Type())
in_temp_band.setMaxAccess(_E)
if mibBuilder.loadTexts:in_temp_band.setStatus(_A)
if mibBuilder.loadTexts:in_temp_band.setUnits(_B)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Unit_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Unit_status_Type.__name__=_C
_Unit_status_Object=MibScalar
unit_status=_Unit_status_Object((1,3,6,1,4,1,9839,2,1,3,1),_Unit_status_Type())
unit_status.setMaxAccess(_D)
if mibBuilder.loadTexts:unit_status.setStatus(_A)
if mibBuilder.loadTexts:unit_status.setUnits(_B)
class _Net_address_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Net_address_Type.__name__=_C
_Net_address_Object=MibScalar
net_address=_Net_address_Object((1,3,6,1,4,1,9839,2,1,3,2),_Net_address_Type())
net_address.setMaxAccess(_D)
if mibBuilder.loadTexts:net_address.setStatus(_A)
if mibBuilder.loadTexts:net_address.setUnits(_B)
class _Cound_fans_mng_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Cound_fans_mng_Type.__name__=_C
_Cound_fans_mng_Object=MibScalar
cound_fans_mng=_Cound_fans_mng_Object((1,3,6,1,4,1,9839,2,1,3,3),_Cound_fans_mng_Type())
cound_fans_mng.setMaxAccess(_E)
if mibBuilder.loadTexts:cound_fans_mng.setStatus(_A)
if mibBuilder.loadTexts:cound_fans_mng.setUnits(_B)
class _Config_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_type_Type.__name__=_C
_Config_type_Object=MibScalar
config_type=_Config_type_Object((1,3,6,1,4,1,9839,2,1,3,4),_Config_type_Type())
config_type.setMaxAccess(_E)
if mibBuilder.loadTexts:config_type.setStatus(_A)
if mibBuilder.loadTexts:config_type.setUnits(_B)
class _Number_comps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Number_comps_Type.__name__=_C
_Number_comps_Object=MibScalar
number_comps=_Number_comps_Object((1,3,6,1,4,1,9839,2,1,3,5),_Number_comps_Type())
number_comps.setMaxAccess(_E)
if mibBuilder.loadTexts:number_comps.setStatus(_A)
if mibBuilder.loadTexts:number_comps.setUnits(_B)
class _Cond_fans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Cond_fans_Type.__name__=_C
_Cond_fans_Object=MibScalar
cond_fans=_Cond_fans_Object((1,3,6,1,4,1,9839,2,1,3,6),_Cond_fans_Type())
cond_fans.setMaxAccess(_E)
if mibBuilder.loadTexts:cond_fans.setStatus(_A)
if mibBuilder.loadTexts:cond_fans.setUnits(_B)
mibBuilder.exportSymbols('CAREL-screw_compressor-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'screw_compressorMIB':screw_compressorMIB,'digitalObjects':digitalObjects,'syson_s':syson_s,'dout_1':dout_1,'dout_2':dout_2,'dout_3':dout_3,'dout_4':dout_4,'dout_5':dout_5,'dout_6':dout_6,'dout_7':dout_7,'dout_8':dout_8,'dout_9':dout_9,'dout_10':dout_10,'dout_11':dout_11,'dout_12':dout_12,'dout_13':dout_13,'en_evap_flow_al':en_evap_flow_al,'en_b1':en_b1,'en_b2':en_b2,'en_b3':en_b3,'en_b4':en_b4,'en_b5':en_b5,'en_b6':en_b6,'en_b7':en_b7,'en_b8':en_b8,'superv_onoff':superv_onoff,'en_start_restr':en_start_restr,'en_modulation':en_modulation,'sun_win_sel':sun_win_sel,'cooling_heating':cooling_heating,'inverter':inverter,'mal_freeze':mal_freeze,'mal_comp':mal_comp,'mal_evap_flow':mal_evap_flow,'mal_cond_flow':mal_cond_flow,'mal_high_press':mal_high_press,'mal_oil_level':mal_oil_level,'mal_low_pres':mal_low_pres,'mal_hp_transd':mal_hp_transd,'mal_serious':mal_serious,'mal_fan1':mal_fan1,'mal_fan2':mal_fan2,'mal_pump_evap':mal_pump_evap,'mal_master_offl':mal_master_offl,'mal_unit2_offl':mal_unit2_offl,'mal_unit3_offl':mal_unit3_offl,'mal_unit4_offl':mal_unit4_offl,'mal_b1':mal_b1,'mal_b2':mal_b2,'mal_b3':mal_b3,'mal_b4':mal_b4,'mal_b5':mal_b5,'mal_b6':mal_b6,'mal_b7':mal_b7,'mal_b8':mal_b8,'mal_pump_cond_h':mal_pump_cond_h,'mal_comp_hour':mal_comp_hour,'mal_pump_cond':mal_pump_cond,'mal_clock32':mal_clock32,'mal_phase':mal_phase,'mal_ld_transd':mal_ld_transd,'mal_voltage':mal_voltage,'mal_current':mal_current,'mal_pump_ev_h':mal_pump_ev_h,'mal_disch_temp':mal_disch_temp,'mal_diff_pres':mal_diff_pres,'mal_alco1_67_r':mal_alco1_67_r,'mal_alco1_68_r':mal_alco1_68_r,'mal_alco1_69_r':mal_alco1_69_r,'mal_alco1_70_r':mal_alco1_70_r,'mal_alco1_71_r':mal_alco1_71_r,'mal_alco1_72_r':mal_alco1_72_r,'mal_alco1_73_r':mal_alco1_73_r,'mal_alco1_74_r':mal_alco1_74_r,'mal_alco1_75_r':mal_alco1_75_r,'mal_alco1_760_r':mal_alco1_760_r,'mal_alco1_97_r':mal_alco1_97_r,'analogObjects':analogObjects,'ain_1':ain_1,'ain_2':ain_2,'ain_3':ain_3,'ain_5':ain_5,'ain_6':ain_6,'ain_7':ain_7,'ain_8':ain_8,'aout_1_display':aout_1_display,'s_temp_setpoint':s_temp_setpoint,'w_temp_setpoint':w_temp_setpoint,'cond_setpoint':cond_setpoint,'in_temp_band':in_temp_band,'integerObjects':integerObjects,'unit_status':unit_status,'net_address':net_address,'cound_fans_mng':cound_fans_mng,'config_type':config_type,'number_comps':number_comps,'cond_fans':cond_fans})