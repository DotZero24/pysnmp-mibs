_F='flag'
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
mod_chMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
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
dout_1=_Dout_1_Object((1,3,6,1,4,1,9839,2,1,1,10),_Dout_1_Type())
dout_1.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_1.setStatus(_A)
if mibBuilder.loadTexts:dout_1.setUnits(_B)
class _Dout_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_2_Type.__name__=_C
_Dout_2_Object=MibScalar
dout_2=_Dout_2_Object((1,3,6,1,4,1,9839,2,1,1,11),_Dout_2_Type())
dout_2.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_2.setStatus(_A)
if mibBuilder.loadTexts:dout_2.setUnits(_B)
class _Dout_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_3_Type.__name__=_C
_Dout_3_Object=MibScalar
dout_3=_Dout_3_Object((1,3,6,1,4,1,9839,2,1,1,12),_Dout_3_Type())
dout_3.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_3.setStatus(_A)
if mibBuilder.loadTexts:dout_3.setUnits(_B)
class _Dout_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_4_Type.__name__=_C
_Dout_4_Object=MibScalar
dout_4=_Dout_4_Object((1,3,6,1,4,1,9839,2,1,1,13),_Dout_4_Type())
dout_4.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_4.setStatus(_A)
if mibBuilder.loadTexts:dout_4.setUnits(_B)
class _Dout_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_5_Type.__name__=_C
_Dout_5_Object=MibScalar
dout_5=_Dout_5_Object((1,3,6,1,4,1,9839,2,1,1,14),_Dout_5_Type())
dout_5.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_5.setStatus(_A)
if mibBuilder.loadTexts:dout_5.setUnits(_B)
class _Dout_6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_6_Type.__name__=_C
_Dout_6_Object=MibScalar
dout_6=_Dout_6_Object((1,3,6,1,4,1,9839,2,1,1,15),_Dout_6_Type())
dout_6.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_6.setStatus(_A)
if mibBuilder.loadTexts:dout_6.setUnits(_B)
class _Dout_7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_7_Type.__name__=_C
_Dout_7_Object=MibScalar
dout_7=_Dout_7_Object((1,3,6,1,4,1,9839,2,1,1,16),_Dout_7_Type())
dout_7.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_7.setStatus(_A)
if mibBuilder.loadTexts:dout_7.setUnits(_B)
class _Dout_8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_8_Type.__name__=_C
_Dout_8_Object=MibScalar
dout_8=_Dout_8_Object((1,3,6,1,4,1,9839,2,1,1,17),_Dout_8_Type())
dout_8.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_8.setStatus(_A)
if mibBuilder.loadTexts:dout_8.setUnits(_B)
class _Dout_9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_9_Type.__name__=_C
_Dout_9_Object=MibScalar
dout_9=_Dout_9_Object((1,3,6,1,4,1,9839,2,1,1,18),_Dout_9_Type())
dout_9.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_9.setStatus(_A)
if mibBuilder.loadTexts:dout_9.setUnits(_B)
class _Dout_10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_10_Type.__name__=_C
_Dout_10_Object=MibScalar
dout_10=_Dout_10_Object((1,3,6,1,4,1,9839,2,1,1,19),_Dout_10_Type())
dout_10.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_10.setStatus(_A)
if mibBuilder.loadTexts:dout_10.setUnits(_B)
class _Dout_11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_11_Type.__name__=_C
_Dout_11_Object=MibScalar
dout_11=_Dout_11_Object((1,3,6,1,4,1,9839,2,1,1,20),_Dout_11_Type())
dout_11.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_11.setStatus(_A)
if mibBuilder.loadTexts:dout_11.setUnits(_B)
class _Dout_12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_12_Type.__name__=_C
_Dout_12_Object=MibScalar
dout_12=_Dout_12_Object((1,3,6,1,4,1,9839,2,1,1,21),_Dout_12_Type())
dout_12.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_12.setStatus(_A)
if mibBuilder.loadTexts:dout_12.setUnits(_B)
class _Dout_13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout_13_Type.__name__=_C
_Dout_13_Object=MibScalar
dout_13=_Dout_13_Object((1,3,6,1,4,1,9839,2,1,1,22),_Dout_13_Type())
dout_13.setMaxAccess(_D)
if mibBuilder.loadTexts:dout_13.setStatus(_A)
if mibBuilder.loadTexts:dout_13.setUnits(_B)
class _Master_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Master_Type.__name__=_C
_Master_Object=MibScalar
master=_Master_Object((1,3,6,1,4,1,9839,2,1,1,28),_Master_Type())
master.setMaxAccess(_D)
if mibBuilder.loadTexts:master.setStatus(_A)
if mibBuilder.loadTexts:master.setUnits(_B)
class _Slave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Slave_Type.__name__=_C
_Slave_Object=MibScalar
slave=_Slave_Object((1,3,6,1,4,1,9839,2,1,1,29),_Slave_Type())
slave.setMaxAccess(_D)
if mibBuilder.loadTexts:slave.setStatus(_A)
if mibBuilder.loadTexts:slave.setUnits(_B)
class _En_b1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b1_Type.__name__=_C
_En_b1_Object=MibScalar
en_b1=_En_b1_Object((1,3,6,1,4,1,9839,2,1,1,30),_En_b1_Type())
en_b1.setMaxAccess(_E)
if mibBuilder.loadTexts:en_b1.setStatus(_A)
if mibBuilder.loadTexts:en_b1.setUnits(_F)
class _En_b2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b2_Type.__name__=_C
_En_b2_Object=MibScalar
en_b2=_En_b2_Object((1,3,6,1,4,1,9839,2,1,1,31),_En_b2_Type())
en_b2.setMaxAccess(_E)
if mibBuilder.loadTexts:en_b2.setStatus(_A)
if mibBuilder.loadTexts:en_b2.setUnits(_F)
class _En_b3_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b3_Type.__name__=_C
_En_b3_Object=MibScalar
en_b3=_En_b3_Object((1,3,6,1,4,1,9839,2,1,1,32),_En_b3_Type())
en_b3.setMaxAccess(_E)
if mibBuilder.loadTexts:en_b3.setStatus(_A)
if mibBuilder.loadTexts:en_b3.setUnits(_F)
class _En_b4_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b4_Type.__name__=_C
_En_b4_Object=MibScalar
en_b4=_En_b4_Object((1,3,6,1,4,1,9839,2,1,1,33),_En_b4_Type())
en_b4.setMaxAccess(_E)
if mibBuilder.loadTexts:en_b4.setStatus(_A)
if mibBuilder.loadTexts:en_b4.setUnits(_F)
class _En_b5_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b5_Type.__name__=_C
_En_b5_Object=MibScalar
en_b5=_En_b5_Object((1,3,6,1,4,1,9839,2,1,1,34),_En_b5_Type())
en_b5.setMaxAccess(_E)
if mibBuilder.loadTexts:en_b5.setStatus(_A)
if mibBuilder.loadTexts:en_b5.setUnits(_F)
class _En_b6_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b6_Type.__name__=_C
_En_b6_Object=MibScalar
en_b6=_En_b6_Object((1,3,6,1,4,1,9839,2,1,1,35),_En_b6_Type())
en_b6.setMaxAccess(_E)
if mibBuilder.loadTexts:en_b6.setStatus(_A)
if mibBuilder.loadTexts:en_b6.setUnits(_F)
class _En_b7_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b7_Type.__name__=_C
_En_b7_Object=MibScalar
en_b7=_En_b7_Object((1,3,6,1,4,1,9839,2,1,1,36),_En_b7_Type())
en_b7.setMaxAccess(_E)
if mibBuilder.loadTexts:en_b7.setStatus(_A)
if mibBuilder.loadTexts:en_b7.setUnits(_F)
class _En_b8_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_b8_Type.__name__=_C
_En_b8_Object=MibScalar
en_b8=_En_b8_Object((1,3,6,1,4,1,9839,2,1,1,37),_En_b8_Type())
en_b8.setMaxAccess(_E)
if mibBuilder.loadTexts:en_b8.setStatus(_A)
if mibBuilder.loadTexts:en_b8.setUnits(_F)
class _Main_pump_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Main_pump_Type.__name__=_C
_Main_pump_Object=MibScalar
main_pump=_Main_pump_Object((1,3,6,1,4,1,9839,2,1,1,40),_Main_pump_Type())
main_pump.setMaxAccess(_D)
if mibBuilder.loadTexts:main_pump.setStatus(_A)
if mibBuilder.loadTexts:main_pump.setUnits(_B)
class _Cond_pump_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cond_pump_Type.__name__=_C
_Cond_pump_Object=MibScalar
cond_pump=_Cond_pump_Object((1,3,6,1,4,1,9839,2,1,1,41),_Cond_pump_Type())
cond_pump.setMaxAccess(_D)
if mibBuilder.loadTexts:cond_pump.setStatus(_A)
if mibBuilder.loadTexts:cond_pump.setUnits(_B)
class _Superv_onoff_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Superv_onoff_Type.__name__=_C
_Superv_onoff_Object=MibScalar
superv_onoff=_Superv_onoff_Object((1,3,6,1,4,1,9839,2,1,1,42),_Superv_onoff_Type())
superv_onoff.setMaxAccess(_E)
if mibBuilder.loadTexts:superv_onoff.setStatus(_A)
if mibBuilder.loadTexts:superv_onoff.setUnits(_B)
class _Sum_win_sup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sum_win_sup_Type.__name__=_C
_Sum_win_sup_Object=MibScalar
sum_win_sup=_Sum_win_sup_Object((1,3,6,1,4,1,9839,2,1,1,44),_Sum_win_sup_Type())
sum_win_sup.setMaxAccess(_E)
if mibBuilder.loadTexts:sum_win_sup.setStatus(_A)
if mibBuilder.loadTexts:sum_win_sup.setUnits(_B)
class _En_freecooling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_freecooling_Type.__name__=_C
_En_freecooling_Object=MibScalar
en_freecooling=_En_freecooling_Object((1,3,6,1,4,1,9839,2,1,1,46),_En_freecooling_Type())
en_freecooling.setMaxAccess(_D)
if mibBuilder.loadTexts:en_freecooling.setStatus(_A)
if mibBuilder.loadTexts:en_freecooling.setUnits(_B)
class _En_aa_unit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_aa_unit_Type.__name__=_C
_En_aa_unit_Object=MibScalar
en_aa_unit=_En_aa_unit_Object((1,3,6,1,4,1,9839,2,1,1,47),_En_aa_unit_Type())
en_aa_unit.setMaxAccess(_D)
if mibBuilder.loadTexts:en_aa_unit.setStatus(_A)
if mibBuilder.loadTexts:en_aa_unit.setUnits(_B)
class _En_ww_unit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_ww_unit_Type.__name__=_C
_En_ww_unit_Object=MibScalar
en_ww_unit=_En_ww_unit_Object((1,3,6,1,4,1,9839,2,1,1,48),_En_ww_unit_Type())
en_ww_unit.setMaxAccess(_D)
if mibBuilder.loadTexts:en_ww_unit.setStatus(_A)
if mibBuilder.loadTexts:en_ww_unit.setUnits(_B)
class _Sum_win_sel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sum_win_sel_Type.__name__=_C
_Sum_win_sel_Object=MibScalar
sum_win_sel=_Sum_win_sel_Object((1,3,6,1,4,1,9839,2,1,1,49),_Sum_win_sel_Type())
sum_win_sel.setMaxAccess(_D)
if mibBuilder.loadTexts:sum_win_sel.setStatus(_A)
if mibBuilder.loadTexts:sum_win_sel.setUnits(_B)
class _En_sum_win_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_sum_win_Type.__name__=_C
_En_sum_win_Object=MibScalar
en_sum_win=_En_sum_win_Object((1,3,6,1,4,1,9839,2,1,1,50),_En_sum_win_Type())
en_sum_win.setMaxAccess(_D)
if mibBuilder.loadTexts:en_sum_win.setStatus(_A)
if mibBuilder.loadTexts:en_sum_win.setUnits(_B)
class _Cooling_heating_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cooling_heating_Type.__name__=_C
_Cooling_heating_Object=MibScalar
cooling_heating=_Cooling_heating_Object((1,3,6,1,4,1,9839,2,1,1,51),_Cooling_heating_Type())
cooling_heating.setMaxAccess(_D)
if mibBuilder.loadTexts:cooling_heating.setStatus(_A)
if mibBuilder.loadTexts:cooling_heating.setUnits(_B)
class _Cond_config_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cond_config_Type.__name__=_C
_Cond_config_Object=MibScalar
cond_config=_Cond_config_Object((1,3,6,1,4,1,9839,2,1,1,53),_Cond_config_Type())
cond_config.setMaxAccess(_E)
if mibBuilder.loadTexts:cond_config.setStatus(_A)
if mibBuilder.loadTexts:cond_config.setUnits(_B)
class _Inverter_steps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inverter_steps_Type.__name__=_C
_Inverter_steps_Object=MibScalar
inverter_steps=_Inverter_steps_Object((1,3,6,1,4,1,9839,2,1,1,56),_Inverter_steps_Type())
inverter_steps.setMaxAccess(_E)
if mibBuilder.loadTexts:inverter_steps.setStatus(_A)
if mibBuilder.loadTexts:inverter_steps.setUnits(_B)
class _Inverter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Inverter_Type.__name__=_C
_Inverter_Object=MibScalar
inverter=_Inverter_Object((1,3,6,1,4,1,9839,2,1,1,57),_Inverter_Type())
inverter.setMaxAccess(_D)
if mibBuilder.loadTexts:inverter.setStatus(_A)
if mibBuilder.loadTexts:inverter.setUnits(_B)
class _Fc_valve_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fc_valve_type_Type.__name__=_C
_Fc_valve_type_Object=MibScalar
fc_valve_type=_Fc_valve_type_Object((1,3,6,1,4,1,9839,2,1,1,58),_Fc_valve_type_Type())
fc_valve_type.setMaxAccess(_E)
if mibBuilder.loadTexts:fc_valve_type.setStatus(_A)
if mibBuilder.loadTexts:fc_valve_type.setUnits(_B)
class _Not_fc_vlv_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Not_fc_vlv_type_Type.__name__=_C
_Not_fc_vlv_type_Object=MibScalar
not_fc_vlv_type=_Not_fc_vlv_type_Object((1,3,6,1,4,1,9839,2,1,1,59),_Not_fc_vlv_type_Type())
not_fc_vlv_type.setMaxAccess(_D)
if mibBuilder.loadTexts:not_fc_vlv_type.setStatus(_A)
if mibBuilder.loadTexts:not_fc_vlv_type.setUnits(_B)
class _Unloads_logic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Unloads_logic_Type.__name__=_C
_Unloads_logic_Object=MibScalar
unloads_logic=_Unloads_logic_Object((1,3,6,1,4,1,9839,2,1,1,60),_Unloads_logic_Type())
unloads_logic.setMaxAccess(_E)
if mibBuilder.loadTexts:unloads_logic.setStatus(_A)
if mibBuilder.loadTexts:unloads_logic.setUnits(_B)
class _Valve4way_logic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Valve4way_logic_Type.__name__=_C
_Valve4way_logic_Object=MibScalar
valve4way_logic=_Valve4way_logic_Object((1,3,6,1,4,1,9839,2,1,1,61),_Valve4way_logic_Type())
valve4way_logic.setMaxAccess(_E)
if mibBuilder.loadTexts:valve4way_logic.setStatus(_A)
if mibBuilder.loadTexts:valve4way_logic.setUnits(_B)
class _Glb_al_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Glb_al_Type.__name__=_C
_Glb_al_Object=MibScalar
glb_al=_Glb_al_Object((1,3,6,1,4,1,9839,2,1,1,70),_Glb_al_Type())
glb_al.setMaxAccess(_D)
if mibBuilder.loadTexts:glb_al.setStatus(_A)
if mibBuilder.loadTexts:glb_al.setUnits(_B)
class _Man_freeze_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Man_freeze_Type.__name__=_C
_Man_freeze_Object=MibScalar
man_freeze=_Man_freeze_Object((1,3,6,1,4,1,9839,2,1,1,71),_Man_freeze_Type())
man_freeze.setMaxAccess(_D)
if mibBuilder.loadTexts:man_freeze.setStatus(_A)
if mibBuilder.loadTexts:man_freeze.setUnits(_B)
class _Mal_ov1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_ov1_Type.__name__=_C
_Mal_ov1_Object=MibScalar
mal_ov1=_Mal_ov1_Object((1,3,6,1,4,1,9839,2,1,1,72),_Mal_ov1_Type())
mal_ov1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_ov1.setStatus(_A)
if mibBuilder.loadTexts:mal_ov1.setUnits(_B)
class _Mal_ov2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_ov2_Type.__name__=_C
_Mal_ov2_Object=MibScalar
mal_ov2=_Mal_ov2_Object((1,3,6,1,4,1,9839,2,1,1,73),_Mal_ov2_Type())
mal_ov2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_ov2.setStatus(_A)
if mibBuilder.loadTexts:mal_ov2.setUnits(_B)
class _Mal_ov3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_ov3_Type.__name__=_C
_Mal_ov3_Object=MibScalar
mal_ov3=_Mal_ov3_Object((1,3,6,1,4,1,9839,2,1,1,74),_Mal_ov3_Type())
mal_ov3.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_ov3.setStatus(_A)
if mibBuilder.loadTexts:mal_ov3.setUnits(_B)
class _Mal_ov4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_ov4_Type.__name__=_C
_Mal_ov4_Object=MibScalar
mal_ov4=_Mal_ov4_Object((1,3,6,1,4,1,9839,2,1,1,75),_Mal_ov4_Type())
mal_ov4.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_ov4.setStatus(_A)
if mibBuilder.loadTexts:mal_ov4.setUnits(_B)
class _Mal_cflow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_cflow_Type.__name__=_C
_Mal_cflow_Object=MibScalar
mal_cflow=_Mal_cflow_Object((1,3,6,1,4,1,9839,2,1,1,76),_Mal_cflow_Type())
mal_cflow.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_cflow.setStatus(_A)
if mibBuilder.loadTexts:mal_cflow.setUnits(_B)
class _Mal_eflow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_eflow_Type.__name__=_C
_Mal_eflow_Object=MibScalar
mal_eflow=_Mal_eflow_Object((1,3,6,1,4,1,9839,2,1,1,77),_Mal_eflow_Type())
mal_eflow.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_eflow.setStatus(_A)
if mibBuilder.loadTexts:mal_eflow.setUnits(_B)
class _Mal_hp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_hp1_Type.__name__=_C
_Mal_hp1_Object=MibScalar
mal_hp1=_Mal_hp1_Object((1,3,6,1,4,1,9839,2,1,1,78),_Mal_hp1_Type())
mal_hp1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_hp1.setStatus(_A)
if mibBuilder.loadTexts:mal_hp1.setUnits(_B)
class _Mal_hp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_hp2_Type.__name__=_C
_Mal_hp2_Object=MibScalar
mal_hp2=_Mal_hp2_Object((1,3,6,1,4,1,9839,2,1,1,79),_Mal_hp2_Type())
mal_hp2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_hp2.setStatus(_A)
if mibBuilder.loadTexts:mal_hp2.setUnits(_B)
class _Mal_od1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_od1_Type.__name__=_C
_Mal_od1_Object=MibScalar
mal_od1=_Mal_od1_Object((1,3,6,1,4,1,9839,2,1,1,80),_Mal_od1_Type())
mal_od1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_od1.setStatus(_A)
if mibBuilder.loadTexts:mal_od1.setUnits(_B)
class _Mal_od2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_od2_Type.__name__=_C
_Mal_od2_Object=MibScalar
mal_od2=_Mal_od2_Object((1,3,6,1,4,1,9839,2,1,1,81),_Mal_od2_Type())
mal_od2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_od2.setStatus(_A)
if mibBuilder.loadTexts:mal_od2.setUnits(_B)
class _Mal_lp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_lp1_Type.__name__=_C
_Mal_lp1_Object=MibScalar
mal_lp1=_Mal_lp1_Object((1,3,6,1,4,1,9839,2,1,1,82),_Mal_lp1_Type())
mal_lp1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_lp1.setStatus(_A)
if mibBuilder.loadTexts:mal_lp1.setUnits(_B)
class _Mal_lp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_lp2_Type.__name__=_C
_Mal_lp2_Object=MibScalar
mal_lp2=_Mal_lp2_Object((1,3,6,1,4,1,9839,2,1,1,83),_Mal_lp2_Type())
mal_lp2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_lp2.setStatus(_A)
if mibBuilder.loadTexts:mal_lp2.setUnits(_B)
class _Mal_hpt1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_hpt1_Type.__name__=_C
_Mal_hpt1_Object=MibScalar
mal_hpt1=_Mal_hpt1_Object((1,3,6,1,4,1,9839,2,1,1,84),_Mal_hpt1_Type())
mal_hpt1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_hpt1.setStatus(_A)
if mibBuilder.loadTexts:mal_hpt1.setUnits(_B)
class _Mal_hpt2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_hpt2_Type.__name__=_C
_Mal_hpt2_Object=MibScalar
mal_hpt2=_Mal_hpt2_Object((1,3,6,1,4,1,9839,2,1,1,85),_Mal_hpt2_Type())
mal_hpt2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_hpt2.setStatus(_A)
if mibBuilder.loadTexts:mal_hpt2.setUnits(_B)
class _Mal_serious_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_serious_Type.__name__=_C
_Mal_serious_Object=MibScalar
mal_serious=_Mal_serious_Object((1,3,6,1,4,1,9839,2,1,1,86),_Mal_serious_Type())
mal_serious.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_serious.setStatus(_A)
if mibBuilder.loadTexts:mal_serious.setUnits(_B)
class _Mal_f1_overload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_f1_overload_Type.__name__=_C
_Mal_f1_overload_Object=MibScalar
mal_f1_overload=_Mal_f1_overload_Object((1,3,6,1,4,1,9839,2,1,1,87),_Mal_f1_overload_Type())
mal_f1_overload.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_f1_overload.setStatus(_A)
if mibBuilder.loadTexts:mal_f1_overload.setUnits(_B)
class _Mal_f2_overload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_f2_overload_Type.__name__=_C
_Mal_f2_overload_Object=MibScalar
mal_f2_overload=_Mal_f2_overload_Object((1,3,6,1,4,1,9839,2,1,1,88),_Mal_f2_overload_Type())
mal_f2_overload.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_f2_overload.setStatus(_A)
if mibBuilder.loadTexts:mal_f2_overload.setUnits(_B)
class _Mal_f3_overload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_f3_overload_Type.__name__=_C
_Mal_f3_overload_Object=MibScalar
mal_f3_overload=_Mal_f3_overload_Object((1,3,6,1,4,1,9839,2,1,1,89),_Mal_f3_overload_Type())
mal_f3_overload.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_f3_overload.setStatus(_A)
if mibBuilder.loadTexts:mal_f3_overload.setUnits(_B)
class _Mal_fan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_fan_Type.__name__=_C
_Mal_fan_Object=MibScalar
mal_fan=_Mal_fan_Object((1,3,6,1,4,1,9839,2,1,1,90),_Mal_fan_Type())
mal_fan.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_fan.setStatus(_A)
if mibBuilder.loadTexts:mal_fan.setUnits(_B)
class _Mal_cpump_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_cpump_Type.__name__=_C
_Mal_cpump_Object=MibScalar
mal_cpump=_Mal_cpump_Object((1,3,6,1,4,1,9839,2,1,1,91),_Mal_cpump_Type())
mal_cpump.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_cpump.setStatus(_A)
if mibBuilder.loadTexts:mal_cpump.setUnits(_B)
class _Mal_pump_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_pump_Type.__name__=_C
_Mal_pump_Object=MibScalar
mal_pump=_Mal_pump_Object((1,3,6,1,4,1,9839,2,1,1,92),_Mal_pump_Type())
mal_pump.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_pump.setStatus(_A)
if mibBuilder.loadTexts:mal_pump.setUnits(_B)
class _Mal_unit1_offl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_unit1_offl_Type.__name__=_C
_Mal_unit1_offl_Object=MibScalar
mal_unit1_offl=_Mal_unit1_offl_Object((1,3,6,1,4,1,9839,2,1,1,93),_Mal_unit1_offl_Type())
mal_unit1_offl.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_unit1_offl.setStatus(_A)
if mibBuilder.loadTexts:mal_unit1_offl.setUnits(_B)
class _Mal_unit2_offl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_unit2_offl_Type.__name__=_C
_Mal_unit2_offl_Object=MibScalar
mal_unit2_offl=_Mal_unit2_offl_Object((1,3,6,1,4,1,9839,2,1,1,94),_Mal_unit2_offl_Type())
mal_unit2_offl.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_unit2_offl.setStatus(_A)
if mibBuilder.loadTexts:mal_unit2_offl.setUnits(_B)
class _Mal_unit3_offl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_unit3_offl_Type.__name__=_C
_Mal_unit3_offl_Object=MibScalar
mal_unit3_offl=_Mal_unit3_offl_Object((1,3,6,1,4,1,9839,2,1,1,95),_Mal_unit3_offl_Type())
mal_unit3_offl.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_unit3_offl.setStatus(_A)
if mibBuilder.loadTexts:mal_unit3_offl.setUnits(_B)
class _Mal_unit4_offl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_unit4_offl_Type.__name__=_C
_Mal_unit4_offl_Object=MibScalar
mal_unit4_offl=_Mal_unit4_offl_Object((1,3,6,1,4,1,9839,2,1,1,96),_Mal_unit4_offl_Type())
mal_unit4_offl.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_unit4_offl.setStatus(_A)
if mibBuilder.loadTexts:mal_unit4_offl.setUnits(_B)
class _Mal_b1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b1_Type.__name__=_C
_Mal_b1_Object=MibScalar
mal_b1=_Mal_b1_Object((1,3,6,1,4,1,9839,2,1,1,97),_Mal_b1_Type())
mal_b1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b1.setStatus(_A)
if mibBuilder.loadTexts:mal_b1.setUnits(_B)
class _Mal_b2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b2_Type.__name__=_C
_Mal_b2_Object=MibScalar
mal_b2=_Mal_b2_Object((1,3,6,1,4,1,9839,2,1,1,98),_Mal_b2_Type())
mal_b2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b2.setStatus(_A)
if mibBuilder.loadTexts:mal_b2.setUnits(_B)
class _Mal_b3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b3_Type.__name__=_C
_Mal_b3_Object=MibScalar
mal_b3=_Mal_b3_Object((1,3,6,1,4,1,9839,2,1,1,99),_Mal_b3_Type())
mal_b3.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b3.setStatus(_A)
if mibBuilder.loadTexts:mal_b3.setUnits(_B)
class _Mal_b4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b4_Type.__name__=_C
_Mal_b4_Object=MibScalar
mal_b4=_Mal_b4_Object((1,3,6,1,4,1,9839,2,1,1,100),_Mal_b4_Type())
mal_b4.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b4.setStatus(_A)
if mibBuilder.loadTexts:mal_b4.setUnits(_B)
class _Mal_b5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b5_Type.__name__=_C
_Mal_b5_Object=MibScalar
mal_b5=_Mal_b5_Object((1,3,6,1,4,1,9839,2,1,1,101),_Mal_b5_Type())
mal_b5.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b5.setStatus(_A)
if mibBuilder.loadTexts:mal_b5.setUnits(_B)
class _Mal_b6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b6_Type.__name__=_C
_Mal_b6_Object=MibScalar
mal_b6=_Mal_b6_Object((1,3,6,1,4,1,9839,2,1,1,102),_Mal_b6_Type())
mal_b6.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b6.setStatus(_A)
if mibBuilder.loadTexts:mal_b6.setUnits(_B)
class _Mal_b7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b7_Type.__name__=_C
_Mal_b7_Object=MibScalar
mal_b7=_Mal_b7_Object((1,3,6,1,4,1,9839,2,1,1,103),_Mal_b7_Type())
mal_b7.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b7.setStatus(_A)
if mibBuilder.loadTexts:mal_b7.setUnits(_B)
class _Mal_b8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_b8_Type.__name__=_C
_Mal_b8_Object=MibScalar
mal_b8=_Mal_b8_Object((1,3,6,1,4,1,9839,2,1,1,104),_Mal_b8_Type())
mal_b8.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_b8.setStatus(_A)
if mibBuilder.loadTexts:mal_b8.setUnits(_B)
class _Mal_h_main_pump_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_h_main_pump_Type.__name__=_C
_Mal_h_main_pump_Object=MibScalar
mal_h_main_pump=_Mal_h_main_pump_Object((1,3,6,1,4,1,9839,2,1,1,105),_Mal_h_main_pump_Type())
mal_h_main_pump.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_h_main_pump.setStatus(_A)
if mibBuilder.loadTexts:mal_h_main_pump.setUnits(_B)
class _Mal_h_comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_h_comp1_Type.__name__=_C
_Mal_h_comp1_Object=MibScalar
mal_h_comp1=_Mal_h_comp1_Object((1,3,6,1,4,1,9839,2,1,1,106),_Mal_h_comp1_Type())
mal_h_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_h_comp1.setStatus(_A)
if mibBuilder.loadTexts:mal_h_comp1.setUnits(_B)
class _Mal_h_comp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_h_comp2_Type.__name__=_C
_Mal_h_comp2_Object=MibScalar
mal_h_comp2=_Mal_h_comp2_Object((1,3,6,1,4,1,9839,2,1,1,107),_Mal_h_comp2_Type())
mal_h_comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_h_comp2.setStatus(_A)
if mibBuilder.loadTexts:mal_h_comp2.setUnits(_B)
class _Mal_h_comp3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_h_comp3_Type.__name__=_C
_Mal_h_comp3_Object=MibScalar
mal_h_comp3=_Mal_h_comp3_Object((1,3,6,1,4,1,9839,2,1,1,108),_Mal_h_comp3_Type())
mal_h_comp3.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_h_comp3.setStatus(_A)
if mibBuilder.loadTexts:mal_h_comp3.setUnits(_B)
class _Mal_h_comp4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_h_comp4_Type.__name__=_C
_Mal_h_comp4_Object=MibScalar
mal_h_comp4=_Mal_h_comp4_Object((1,3,6,1,4,1,9839,2,1,1,109),_Mal_h_comp4_Type())
mal_h_comp4.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_h_comp4.setStatus(_A)
if mibBuilder.loadTexts:mal_h_comp4.setUnits(_B)
class _Mal_clock32_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_clock32_Type.__name__=_C
_Mal_clock32_Object=MibScalar
mal_clock32=_Mal_clock32_Object((1,3,6,1,4,1,9839,2,1,1,110),_Mal_clock32_Type())
mal_clock32.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_clock32.setStatus(_A)
if mibBuilder.loadTexts:mal_clock32.setUnits(_B)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Ain_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_1_Type.__name__=_C
_Ain_1_Object=MibScalar
ain_1=_Ain_1_Object((1,3,6,1,4,1,9839,2,1,2,1),_Ain_1_Type())
ain_1.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_1.setStatus(_A)
if mibBuilder.loadTexts:ain_1.setUnits(_B)
class _Ain_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_2_Type.__name__=_C
_Ain_2_Object=MibScalar
ain_2=_Ain_2_Object((1,3,6,1,4,1,9839,2,1,2,2),_Ain_2_Type())
ain_2.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_2.setStatus(_A)
if mibBuilder.loadTexts:ain_2.setUnits(_B)
class _Ain_3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_3_Type.__name__=_C
_Ain_3_Object=MibScalar
ain_3=_Ain_3_Object((1,3,6,1,4,1,9839,2,1,2,3),_Ain_3_Type())
ain_3.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_3.setStatus(_A)
if mibBuilder.loadTexts:ain_3.setUnits(_B)
class _Ain_4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_4_Type.__name__=_C
_Ain_4_Object=MibScalar
ain_4=_Ain_4_Object((1,3,6,1,4,1,9839,2,1,2,4),_Ain_4_Type())
ain_4.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_4.setStatus(_A)
if mibBuilder.loadTexts:ain_4.setUnits(_B)
class _Ain_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_5_Type.__name__=_C
_Ain_5_Object=MibScalar
ain_5=_Ain_5_Object((1,3,6,1,4,1,9839,2,1,2,5),_Ain_5_Type())
ain_5.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_5.setStatus(_A)
if mibBuilder.loadTexts:ain_5.setUnits(_B)
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
if mibBuilder.loadTexts:ain_7.setUnits(_B)
class _Ain_8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ain_8_Type.__name__=_C
_Ain_8_Object=MibScalar
ain_8=_Ain_8_Object((1,3,6,1,4,1,9839,2,1,2,8),_Ain_8_Type())
ain_8.setMaxAccess(_D)
if mibBuilder.loadTexts:ain_8.setStatus(_A)
if mibBuilder.loadTexts:ain_8.setUnits(_B)
class _Analog_out_1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Analog_out_1_Type.__name__=_C
_Analog_out_1_Object=MibScalar
analog_out_1=_Analog_out_1_Object((1,3,6,1,4,1,9839,2,1,2,9),_Analog_out_1_Type())
analog_out_1.setMaxAccess(_D)
if mibBuilder.loadTexts:analog_out_1.setStatus(_A)
if mibBuilder.loadTexts:analog_out_1.setUnits(_B)
class _Analog_out_2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Analog_out_2_Type.__name__=_C
_Analog_out_2_Object=MibScalar
analog_out_2=_Analog_out_2_Object((1,3,6,1,4,1,9839,2,1,2,10),_Analog_out_2_Type())
analog_out_2.setMaxAccess(_D)
if mibBuilder.loadTexts:analog_out_2.setStatus(_A)
if mibBuilder.loadTexts:analog_out_2.setUnits(_B)
class _S_temp_setpoint_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_S_temp_setpoint_Type.__name__=_C
_S_temp_setpoint_Object=MibScalar
s_temp_setpoint=_S_temp_setpoint_Object((1,3,6,1,4,1,9839,2,1,2,11),_S_temp_setpoint_Type())
s_temp_setpoint.setMaxAccess(_E)
if mibBuilder.loadTexts:s_temp_setpoint.setStatus(_A)
if mibBuilder.loadTexts:s_temp_setpoint.setUnits(_B)
class _W_temp_setpoint_Type(Integer32):defaultValue=450;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_W_temp_setpoint_Type.__name__=_C
_W_temp_setpoint_Object=MibScalar
w_temp_setpoint=_W_temp_setpoint_Object((1,3,6,1,4,1,9839,2,1,2,12),_W_temp_setpoint_Type())
w_temp_setpoint.setMaxAccess(_E)
if mibBuilder.loadTexts:w_temp_setpoint.setStatus(_A)
if mibBuilder.loadTexts:w_temp_setpoint.setUnits(_B)
class _Cond_setpoint_Type(Integer32):defaultValue=140;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Cond_setpoint_Type.__name__=_C
_Cond_setpoint_Object=MibScalar
cond_setpoint=_Cond_setpoint_Object((1,3,6,1,4,1,9839,2,1,2,13),_Cond_setpoint_Type())
cond_setpoint.setMaxAccess(_E)
if mibBuilder.loadTexts:cond_setpoint.setStatus(_A)
if mibBuilder.loadTexts:cond_setpoint.setUnits(_B)
class _In_temp_setp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_In_temp_setp_Type.__name__=_C
_In_temp_setp_Object=MibScalar
in_temp_setp=_In_temp_setp_Object((1,3,6,1,4,1,9839,2,1,2,14),_In_temp_setp_Type())
in_temp_setp.setMaxAccess(_D)
if mibBuilder.loadTexts:in_temp_setp.setStatus(_A)
if mibBuilder.loadTexts:in_temp_setp.setUnits(_B)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Cu_remote_ctrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Cu_remote_ctrl_Type.__name__=_C
_Cu_remote_ctrl_Object=MibScalar
cu_remote_ctrl=_Cu_remote_ctrl_Object((1,3,6,1,4,1,9839,2,1,3,10),_Cu_remote_ctrl_Type())
cu_remote_ctrl.setMaxAccess(_D)
if mibBuilder.loadTexts:cu_remote_ctrl.setStatus(_A)
if mibBuilder.loadTexts:cu_remote_ctrl.setUnits(_B)
class _Recover_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Recover_mode_Type.__name__=_C
_Recover_mode_Object=MibScalar
recover_mode=_Recover_mode_Object((1,3,6,1,4,1,9839,2,1,3,11),_Recover_mode_Type())
recover_mode.setMaxAccess(_D)
if mibBuilder.loadTexts:recover_mode.setStatus(_A)
if mibBuilder.loadTexts:recover_mode.setUnits(_B)
class _Unit_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Unit_status_Type.__name__=_C
_Unit_status_Object=MibScalar
unit_status=_Unit_status_Object((1,3,6,1,4,1,9839,2,1,3,12),_Unit_status_Type())
unit_status.setMaxAccess(_D)
if mibBuilder.loadTexts:unit_status.setStatus(_A)
if mibBuilder.loadTexts:unit_status.setUnits(_B)
class _Cond_fans_mng_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Cond_fans_mng_Type.__name__=_C
_Cond_fans_mng_Object=MibScalar
cond_fans_mng=_Cond_fans_mng_Object((1,3,6,1,4,1,9839,2,1,3,13),_Cond_fans_mng_Type())
cond_fans_mng.setMaxAccess(_E)
if mibBuilder.loadTexts:cond_fans_mng.setStatus(_A)
if mibBuilder.loadTexts:cond_fans_mng.setUnits(_B)
class _X_h_main_pump_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_X_h_main_pump_Type.__name__=_C
_X_h_main_pump_Object=MibScalar
x_h_main_pump=_X_h_main_pump_Object((1,3,6,1,4,1,9839,2,1,3,20),_X_h_main_pump_Type())
x_h_main_pump.setMaxAccess(_D)
if mibBuilder.loadTexts:x_h_main_pump.setStatus(_A)
if mibBuilder.loadTexts:x_h_main_pump.setUnits(_B)
class _X_l_main_pump_Type(Integer32):defaultValue=20000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_X_l_main_pump_Type.__name__=_C
_X_l_main_pump_Object=MibScalar
x_l_main_pump=_X_l_main_pump_Object((1,3,6,1,4,1,9839,2,1,3,21),_X_l_main_pump_Type())
x_l_main_pump.setMaxAccess(_D)
if mibBuilder.loadTexts:x_l_main_pump.setStatus(_A)
if mibBuilder.loadTexts:x_l_main_pump.setUnits(_B)
class _X_h_comp1_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_X_h_comp1_Type.__name__=_C
_X_h_comp1_Object=MibScalar
x_h_comp1=_X_h_comp1_Object((1,3,6,1,4,1,9839,2,1,3,22),_X_h_comp1_Type())
x_h_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:x_h_comp1.setStatus(_A)
if mibBuilder.loadTexts:x_h_comp1.setUnits(_B)
class _X_l_comp1_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_X_l_comp1_Type.__name__=_C
_X_l_comp1_Object=MibScalar
x_l_comp1=_X_l_comp1_Object((1,3,6,1,4,1,9839,2,1,3,23),_X_l_comp1_Type())
x_l_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:x_l_comp1.setStatus(_A)
if mibBuilder.loadTexts:x_l_comp1.setUnits(_B)
class _X_h_comp2_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_X_h_comp2_Type.__name__=_C
_X_h_comp2_Object=MibScalar
x_h_comp2=_X_h_comp2_Object((1,3,6,1,4,1,9839,2,1,3,24),_X_h_comp2_Type())
x_h_comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:x_h_comp2.setStatus(_A)
if mibBuilder.loadTexts:x_h_comp2.setUnits(_B)
class _X_l_comp2_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_X_l_comp2_Type.__name__=_C
_X_l_comp2_Object=MibScalar
x_l_comp2=_X_l_comp2_Object((1,3,6,1,4,1,9839,2,1,3,25),_X_l_comp2_Type())
x_l_comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:x_l_comp2.setStatus(_A)
if mibBuilder.loadTexts:x_l_comp2.setUnits(_B)
class _X_h_comp3_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_X_h_comp3_Type.__name__=_C
_X_h_comp3_Object=MibScalar
x_h_comp3=_X_h_comp3_Object((1,3,6,1,4,1,9839,2,1,3,26),_X_h_comp3_Type())
x_h_comp3.setMaxAccess(_D)
if mibBuilder.loadTexts:x_h_comp3.setStatus(_A)
if mibBuilder.loadTexts:x_h_comp3.setUnits(_B)
class _X_l_comp3_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_X_l_comp3_Type.__name__=_C
_X_l_comp3_Object=MibScalar
x_l_comp3=_X_l_comp3_Object((1,3,6,1,4,1,9839,2,1,3,27),_X_l_comp3_Type())
x_l_comp3.setMaxAccess(_D)
if mibBuilder.loadTexts:x_l_comp3.setStatus(_A)
if mibBuilder.loadTexts:x_l_comp3.setUnits(_B)
class _X_h_comp4_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_X_h_comp4_Type.__name__=_C
_X_h_comp4_Object=MibScalar
x_h_comp4=_X_h_comp4_Object((1,3,6,1,4,1,9839,2,1,3,28),_X_h_comp4_Type())
x_h_comp4.setMaxAccess(_D)
if mibBuilder.loadTexts:x_h_comp4.setStatus(_A)
if mibBuilder.loadTexts:x_h_comp4.setUnits(_B)
class _X_l_comp4_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_X_l_comp4_Type.__name__=_C
_X_l_comp4_Object=MibScalar
x_l_comp4=_X_l_comp4_Object((1,3,6,1,4,1,9839,2,1,3,29),_X_l_comp4_Type())
x_l_comp4.setMaxAccess(_D)
if mibBuilder.loadTexts:x_l_comp4.setStatus(_A)
if mibBuilder.loadTexts:x_l_comp4.setUnits(_B)
class _Config_unit_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Config_unit_Type.__name__=_C
_Config_unit_Object=MibScalar
config_unit=_Config_unit_Object((1,3,6,1,4,1,9839,2,1,3,30),_Config_unit_Type())
config_unit.setMaxAccess(_D)
if mibBuilder.loadTexts:config_unit.setStatus(_A)
if mibBuilder.loadTexts:config_unit.setUnits(_B)
class _Config_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_type_Type.__name__=_C
_Config_type_Object=MibScalar
config_type=_Config_type_Object((1,3,6,1,4,1,9839,2,1,3,31),_Config_type_Type())
config_type.setMaxAccess(_E)
if mibBuilder.loadTexts:config_type.setStatus(_A)
if mibBuilder.loadTexts:config_type.setUnits(_B)
class _Ph_circ_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ph_circ_type_Type.__name__=_C
_Ph_circ_type_Object=MibScalar
ph_circ_type=_Ph_circ_type_Object((1,3,6,1,4,1,9839,2,1,3,32),_Ph_circ_type_Type())
ph_circ_type.setMaxAccess(_D)
if mibBuilder.loadTexts:ph_circ_type.setStatus(_A)
if mibBuilder.loadTexts:ph_circ_type.setUnits(_B)
class _N_comps_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_N_comps_Type.__name__=_C
_N_comps_Object=MibScalar
n_comps=_N_comps_Object((1,3,6,1,4,1,9839,2,1,3,33),_N_comps_Type())
n_comps.setMaxAccess(_E)
if mibBuilder.loadTexts:n_comps.setStatus(_A)
if mibBuilder.loadTexts:n_comps.setUnits(_B)
class _Comps_x_unit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Comps_x_unit_Type.__name__=_C
_Comps_x_unit_Object=MibScalar
comps_x_unit=_Comps_x_unit_Object((1,3,6,1,4,1,9839,2,1,3,34),_Comps_x_unit_Type())
comps_x_unit.setMaxAccess(_E)
if mibBuilder.loadTexts:comps_x_unit.setStatus(_A)
if mibBuilder.loadTexts:comps_x_unit.setUnits(_B)
class _N_unloaders_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_N_unloaders_Type.__name__=_C
_N_unloaders_Object=MibScalar
n_unloaders=_N_unloaders_Object((1,3,6,1,4,1,9839,2,1,3,35),_N_unloaders_Type())
n_unloaders.setMaxAccess(_E)
if mibBuilder.loadTexts:n_unloaders.setStatus(_A)
if mibBuilder.loadTexts:n_unloaders.setUnits(_B)
class _Cond_fans_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Cond_fans_Type.__name__=_C
_Cond_fans_Object=MibScalar
cond_fans=_Cond_fans_Object((1,3,6,1,4,1,9839,2,1,3,36),_Cond_fans_Type())
cond_fans.setMaxAccess(_E)
if mibBuilder.loadTexts:cond_fans.setStatus(_A)
if mibBuilder.loadTexts:cond_fans.setUnits(_B)
class _Fan1_speed_reg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Fan1_speed_reg_Type.__name__=_C
_Fan1_speed_reg_Object=MibScalar
fan1_speed_reg=_Fan1_speed_reg_Object((1,3,6,1,4,1,9839,2,1,3,37),_Fan1_speed_reg_Type())
fan1_speed_reg.setMaxAccess(_D)
if mibBuilder.loadTexts:fan1_speed_reg.setStatus(_A)
if mibBuilder.loadTexts:fan1_speed_reg.setUnits(_B)
class _Fan2_speed_reg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Fan2_speed_reg_Type.__name__=_C
_Fan2_speed_reg_Object=MibScalar
fan2_speed_reg=_Fan2_speed_reg_Object((1,3,6,1,4,1,9839,2,1,3,38),_Fan2_speed_reg_Type())
fan2_speed_reg.setMaxAccess(_D)
if mibBuilder.loadTexts:fan2_speed_reg.setStatus(_A)
if mibBuilder.loadTexts:fan2_speed_reg.setUnits(_B)
class _Freecool_valve_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Freecool_valve_Type.__name__=_C
_Freecool_valve_Object=MibScalar
freecool_valve=_Freecool_valve_Object((1,3,6,1,4,1,9839,2,1,3,39),_Freecool_valve_Type())
freecool_valve.setMaxAccess(_D)
if mibBuilder.loadTexts:freecool_valve.setStatus(_A)
if mibBuilder.loadTexts:freecool_valve.setUnits(_B)
mibBuilder.exportSymbols('CAREL-mod_ch-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'mod_chMIB':mod_chMIB,'digitalObjects':digitalObjects,'syson_s':syson_s,'dout_1':dout_1,'dout_2':dout_2,'dout_3':dout_3,'dout_4':dout_4,'dout_5':dout_5,'dout_6':dout_6,'dout_7':dout_7,'dout_8':dout_8,'dout_9':dout_9,'dout_10':dout_10,'dout_11':dout_11,'dout_12':dout_12,'dout_13':dout_13,'master':master,'slave':slave,'en_b1':en_b1,'en_b2':en_b2,'en_b3':en_b3,'en_b4':en_b4,'en_b5':en_b5,'en_b6':en_b6,'en_b7':en_b7,'en_b8':en_b8,'main_pump':main_pump,'cond_pump':cond_pump,'superv_onoff':superv_onoff,'sum_win_sup':sum_win_sup,'en_freecooling':en_freecooling,'en_aa_unit':en_aa_unit,'en_ww_unit':en_ww_unit,'sum_win_sel':sum_win_sel,'en_sum_win':en_sum_win,'cooling_heating':cooling_heating,'cond_config':cond_config,'inverter_steps':inverter_steps,'inverter':inverter,'fc_valve_type':fc_valve_type,'not_fc_vlv_type':not_fc_vlv_type,'unloads_logic':unloads_logic,'valve4way_logic':valve4way_logic,'glb_al':glb_al,'man_freeze':man_freeze,'mal_ov1':mal_ov1,'mal_ov2':mal_ov2,'mal_ov3':mal_ov3,'mal_ov4':mal_ov4,'mal_cflow':mal_cflow,'mal_eflow':mal_eflow,'mal_hp1':mal_hp1,'mal_hp2':mal_hp2,'mal_od1':mal_od1,'mal_od2':mal_od2,'mal_lp1':mal_lp1,'mal_lp2':mal_lp2,'mal_hpt1':mal_hpt1,'mal_hpt2':mal_hpt2,'mal_serious':mal_serious,'mal_f1_overload':mal_f1_overload,'mal_f2_overload':mal_f2_overload,'mal_f3_overload':mal_f3_overload,'mal_fan':mal_fan,'mal_cpump':mal_cpump,'mal_pump':mal_pump,'mal_unit1_offl':mal_unit1_offl,'mal_unit2_offl':mal_unit2_offl,'mal_unit3_offl':mal_unit3_offl,'mal_unit4_offl':mal_unit4_offl,'mal_b1':mal_b1,'mal_b2':mal_b2,'mal_b3':mal_b3,'mal_b4':mal_b4,'mal_b5':mal_b5,'mal_b6':mal_b6,'mal_b7':mal_b7,'mal_b8':mal_b8,'mal_h_main_pump':mal_h_main_pump,'mal_h_comp1':mal_h_comp1,'mal_h_comp2':mal_h_comp2,'mal_h_comp3':mal_h_comp3,'mal_h_comp4':mal_h_comp4,'mal_clock32':mal_clock32,'analogObjects':analogObjects,'ain_1':ain_1,'ain_2':ain_2,'ain_3':ain_3,'ain_4':ain_4,'ain_5':ain_5,'ain_6':ain_6,'ain_7':ain_7,'ain_8':ain_8,'analog_out_1':analog_out_1,'analog_out_2':analog_out_2,'s_temp_setpoint':s_temp_setpoint,'w_temp_setpoint':w_temp_setpoint,'cond_setpoint':cond_setpoint,'in_temp_setp':in_temp_setp,'integerObjects':integerObjects,'cu_remote_ctrl':cu_remote_ctrl,'recover_mode':recover_mode,'unit_status':unit_status,'cond_fans_mng':cond_fans_mng,'x_h_main_pump':x_h_main_pump,'x_l_main_pump':x_l_main_pump,'x_h_comp1':x_h_comp1,'x_l_comp1':x_l_comp1,'x_h_comp2':x_h_comp2,'x_l_comp2':x_l_comp2,'x_h_comp3':x_h_comp3,'x_l_comp3':x_l_comp3,'x_h_comp4':x_h_comp4,'x_l_comp4':x_l_comp4,'config_unit':config_unit,'config_type':config_type,'ph_circ_type':ph_circ_type,'n_comps':n_comps,'comps_x_unit':comps_x_unit,'n_unloaders':n_unloaders,'cond_fans':cond_fans,'fan1_speed_reg':fan1_speed_reg,'fan2_speed_reg':fan2_speed_reg,'freecool_valve':freecool_valve})