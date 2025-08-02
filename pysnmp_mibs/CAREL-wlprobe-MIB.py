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
wlprobeMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
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
class _Diginput1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Diginput1_Type.__name__=_C
_Diginput1_Object=MibScalar
diginput1=_Diginput1_Object((1,3,6,1,4,1,9839,2,1,1,1),_Diginput1_Type())
diginput1.setMaxAccess(_D)
if mibBuilder.loadTexts:diginput1.setStatus(_A)
if mibBuilder.loadTexts:diginput1.setUnits(_B)
class _Diginput2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Diginput2_Type.__name__=_C
_Diginput2_Object=MibScalar
diginput2=_Diginput2_Object((1,3,6,1,4,1,9839,2,1,1,2),_Diginput2_Type())
diginput2.setMaxAccess(_D)
if mibBuilder.loadTexts:diginput2.setStatus(_A)
if mibBuilder.loadTexts:diginput2.setUnits(_B)
class _Alrlowbatt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alrlowbatt_Type.__name__=_C
_Alrlowbatt_Object=MibScalar
alrlowbatt=_Alrlowbatt_Object((1,3,6,1,4,1,9839,2,1,1,3),_Alrlowbatt_Type())
alrlowbatt.setMaxAccess(_D)
if mibBuilder.loadTexts:alrlowbatt.setStatus(_A)
if mibBuilder.loadTexts:alrlowbatt.setUnits(_B)
class _Alrprobefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alrprobefault_Type.__name__=_C
_Alrprobefault_Object=MibScalar
alrprobefault=_Alrprobefault_Object((1,3,6,1,4,1,9839,2,1,1,4),_Alrprobefault_Type())
alrprobefault.setMaxAccess(_D)
if mibBuilder.loadTexts:alrprobefault.setStatus(_A)
if mibBuilder.loadTexts:alrprobefault.setUnits(_B)
class _Alrhightempprobe1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alrhightempprobe1_Type.__name__=_C
_Alrhightempprobe1_Object=MibScalar
alrhightempprobe1=_Alrhightempprobe1_Object((1,3,6,1,4,1,9839,2,1,1,6),_Alrhightempprobe1_Type())
alrhightempprobe1.setMaxAccess(_D)
if mibBuilder.loadTexts:alrhightempprobe1.setStatus(_A)
if mibBuilder.loadTexts:alrhightempprobe1.setUnits(_B)
class _Alrhightempprobe2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alrhightempprobe2_Type.__name__=_C
_Alrhightempprobe2_Object=MibScalar
alrhightempprobe2=_Alrhightempprobe2_Object((1,3,6,1,4,1,9839,2,1,1,7),_Alrhightempprobe2_Type())
alrhightempprobe2.setMaxAccess(_D)
if mibBuilder.loadTexts:alrhightempprobe2.setStatus(_A)
if mibBuilder.loadTexts:alrhightempprobe2.setUnits(_B)
class _Alrlowtempprobe1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alrlowtempprobe1_Type.__name__=_C
_Alrlowtempprobe1_Object=MibScalar
alrlowtempprobe1=_Alrlowtempprobe1_Object((1,3,6,1,4,1,9839,2,1,1,8),_Alrlowtempprobe1_Type())
alrlowtempprobe1.setMaxAccess(_D)
if mibBuilder.loadTexts:alrlowtempprobe1.setStatus(_A)
if mibBuilder.loadTexts:alrlowtempprobe1.setUnits(_B)
class _Alrlowtempprobe2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alrlowtempprobe2_Type.__name__=_C
_Alrlowtempprobe2_Object=MibScalar
alrlowtempprobe2=_Alrlowtempprobe2_Object((1,3,6,1,4,1,9839,2,1,1,9),_Alrlowtempprobe2_Type())
alrlowtempprobe2.setMaxAccess(_D)
if mibBuilder.loadTexts:alrlowtempprobe2.setStatus(_A)
if mibBuilder.loadTexts:alrlowtempprobe2.setUnits(_B)
class _Hightempalrenabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Hightempalrenabled_Type.__name__=_C
_Hightempalrenabled_Object=MibScalar
hightempalrenabled=_Hightempalrenabled_Object((1,3,6,1,4,1,9839,2,1,1,10),_Hightempalrenabled_Type())
hightempalrenabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hightempalrenabled.setStatus(_A)
if mibBuilder.loadTexts:hightempalrenabled.setUnits(_B)
class _Diginputpol1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Diginputpol1_Type.__name__=_C
_Diginputpol1_Object=MibScalar
diginputpol1=_Diginputpol1_Object((1,3,6,1,4,1,9839,2,1,1,11),_Diginputpol1_Type())
diginputpol1.setMaxAccess(_E)
if mibBuilder.loadTexts:diginputpol1.setStatus(_A)
if mibBuilder.loadTexts:diginputpol1.setUnits(_B)
class _Diginputpol2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Diginputpol2_Type.__name__=_C
_Diginputpol2_Object=MibScalar
diginputpol2=_Diginputpol2_Object((1,3,6,1,4,1,9839,2,1,1,12),_Diginputpol2_Type())
diginputpol2.setMaxAccess(_E)
if mibBuilder.loadTexts:diginputpol2.setStatus(_A)
if mibBuilder.loadTexts:diginputpol2.setUnits(_B)
class _Alrdefrost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alrdefrost_Type.__name__=_C
_Alrdefrost_Object=MibScalar
alrdefrost=_Alrdefrost_Object((1,3,6,1,4,1,9839,2,1,1,13),_Alrdefrost_Type())
alrdefrost.setMaxAccess(_D)
if mibBuilder.loadTexts:alrdefrost.setStatus(_A)
if mibBuilder.loadTexts:alrdefrost.setUnits(_B)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Probe1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Probe1_Type.__name__=_C
_Probe1_Object=MibScalar
probe1=_Probe1_Object((1,3,6,1,4,1,9839,2,1,2,1),_Probe1_Type())
probe1.setMaxAccess(_D)
if mibBuilder.loadTexts:probe1.setStatus(_A)
if mibBuilder.loadTexts:probe1.setUnits(_B)
class _Probe2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Probe2_Type.__name__=_C
_Probe2_Object=MibScalar
probe2=_Probe2_Object((1,3,6,1,4,1,9839,2,1,2,2),_Probe2_Type())
probe2.setMaxAccess(_D)
if mibBuilder.loadTexts:probe2.setStatus(_A)
if mibBuilder.loadTexts:probe2.setUnits(_B)
class _Thrshitempprobe1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1250))
_Thrshitempprobe1_Type.__name__=_C
_Thrshitempprobe1_Object=MibScalar
thrshitempprobe1=_Thrshitempprobe1_Object((1,3,6,1,4,1,9839,2,1,2,3),_Thrshitempprobe1_Type())
thrshitempprobe1.setMaxAccess(_E)
if mibBuilder.loadTexts:thrshitempprobe1.setStatus(_A)
if mibBuilder.loadTexts:thrshitempprobe1.setUnits(_B)
class _Thrshitempprobe2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1250))
_Thrshitempprobe2_Type.__name__=_C
_Thrshitempprobe2_Object=MibScalar
thrshitempprobe2=_Thrshitempprobe2_Object((1,3,6,1,4,1,9839,2,1,2,4),_Thrshitempprobe2_Type())
thrshitempprobe2.setMaxAccess(_E)
if mibBuilder.loadTexts:thrshitempprobe2.setStatus(_A)
if mibBuilder.loadTexts:thrshitempprobe2.setUnits(_B)
class _Thrslotempprobe1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,100))
_Thrslotempprobe1_Type.__name__=_C
_Thrslotempprobe1_Object=MibScalar
thrslotempprobe1=_Thrslotempprobe1_Object((1,3,6,1,4,1,9839,2,1,2,5),_Thrslotempprobe1_Type())
thrslotempprobe1.setMaxAccess(_E)
if mibBuilder.loadTexts:thrslotempprobe1.setStatus(_A)
if mibBuilder.loadTexts:thrslotempprobe1.setUnits(_B)
class _Thrslotempprobe2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,100))
_Thrslotempprobe2_Type.__name__=_C
_Thrslotempprobe2_Object=MibScalar
thrslotempprobe2=_Thrslotempprobe2_Object((1,3,6,1,4,1,9839,2,1,2,6),_Thrslotempprobe2_Type())
thrslotempprobe2.setMaxAccess(_E)
if mibBuilder.loadTexts:thrslotempprobe2.setStatus(_A)
if mibBuilder.loadTexts:thrslotempprobe2.setUnits(_B)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Hightempdelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_Hightempdelay_Type.__name__=_C
_Hightempdelay_Object=MibScalar
hightempdelay=_Hightempdelay_Object((1,3,6,1,4,1,9839,2,1,3,1),_Hightempdelay_Type())
hightempdelay.setMaxAccess(_E)
if mibBuilder.loadTexts:hightempdelay.setStatus(_A)
if mibBuilder.loadTexts:hightempdelay.setUnits('min')
class _Defrostdelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_Defrostdelay_Type.__name__=_C
_Defrostdelay_Object=MibScalar
defrostdelay=_Defrostdelay_Object((1,3,6,1,4,1,9839,2,1,3,2),_Defrostdelay_Type())
defrostdelay.setMaxAccess(_E)
if mibBuilder.loadTexts:defrostdelay.setStatus(_A)
if mibBuilder.loadTexts:defrostdelay.setUnits('min')
class _Ampsignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Ampsignal_Type.__name__=_C
_Ampsignal_Object=MibScalar
ampsignal=_Ampsignal_Object((1,3,6,1,4,1,9839,2,1,3,3),_Ampsignal_Type())
ampsignal.setMaxAccess(_D)
if mibBuilder.loadTexts:ampsignal.setStatus(_A)
if mibBuilder.loadTexts:ampsignal.setUnits(_B)
mibBuilder.exportSymbols('CAREL-wlprobe-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'wlprobeMIB':wlprobeMIB,'digitalObjects':digitalObjects,'diginput1':diginput1,'diginput2':diginput2,'alrlowbatt':alrlowbatt,'alrprobefault':alrprobefault,'alrhightempprobe1':alrhightempprobe1,'alrhightempprobe2':alrhightempprobe2,'alrlowtempprobe1':alrlowtempprobe1,'alrlowtempprobe2':alrlowtempprobe2,'hightempalrenabled':hightempalrenabled,'diginputpol1':diginputpol1,'diginputpol2':diginputpol2,'alrdefrost':alrdefrost,'analogObjects':analogObjects,'probe1':probe1,'probe2':probe2,'thrshitempprobe1':thrshitempprobe1,'thrshitempprobe2':thrshitempprobe2,'thrslotempprobe1':thrslotempprobe1,'thrslotempprobe2':thrslotempprobe2,'integerObjects':integerObjects,'hightempdelay':hightempdelay,'defrostdelay':defrostdelay,'ampsignal':ampsignal})