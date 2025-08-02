_F='C/F/bar x10'
_E='read-write'
_D='read-only'
_C='N/A'
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
insgrdMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_C)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentCode.setStatus(_A)
if mibBuilder.loadTexts:agentCode.setUnits(_C)
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
netSize.setMaxAccess(_E)
if mibBuilder.loadTexts:netSize.setStatus(_A)
if mibBuilder.loadTexts:netSize.setUnits(_C)
class _BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200))
_BaudRate_Type.__name__=_B
_BaudRate_Object=MibScalar
baudRate=_BaudRate_Object((1,3,6,1,4,1,9839,2,0,1,2),_BaudRate_Type())
baudRate.setMaxAccess(_E)
if mibBuilder.loadTexts:baudRate.setStatus(_A)
if mibBuilder.loadTexts:baudRate.setUnits(_C)
_UnitTypeGroup_ObjectIdentity=ObjectIdentity
unitTypeGroup=_UnitTypeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,2))
_Unit1_Type_Type=DisplayString
_Unit1_Type_Object=MibScalar
unit1_Type=_Unit1_Type_Object((1,3,6,1,4,1,9839,2,0,2,1),_Unit1_Type_Type())
unit1_Type.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_C)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_C)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_C)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_C)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_C)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_C)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_C)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_C)
_UnitOnLineStatusGroup_ObjectIdentity=ObjectIdentity
unitOnLineStatusGroup=_UnitOnLineStatusGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_Unit1_OnLineStatus_Type=Integer32
_Unit1_OnLineStatus_Object=MibScalar
unit1_OnLineStatus=_Unit1_OnLineStatus_Object((1,3,6,1,4,1,9839,2,0,10,1),_Unit1_OnLineStatus_Type())
unit1_OnLineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:unit1_OnLineStatus.setStatus(_A)
if mibBuilder.loadTexts:unit1_OnLineStatus.setUnits(_C)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _Device1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device1_Type.__name__=_B
_Device1_Object=MibScalar
device1=_Device1_Object((1,3,6,1,4,1,9839,2,1,1,1),_Device1_Type())
device1.setMaxAccess(_D)
if mibBuilder.loadTexts:device1.setStatus(_A)
if mibBuilder.loadTexts:device1.setUnits(_C)
class _Device2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device2_Type.__name__=_B
_Device2_Object=MibScalar
device2=_Device2_Object((1,3,6,1,4,1,9839,2,1,1,2),_Device2_Type())
device2.setMaxAccess(_D)
if mibBuilder.loadTexts:device2.setStatus(_A)
if mibBuilder.loadTexts:device2.setUnits(_C)
class _Device3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device3_Type.__name__=_B
_Device3_Object=MibScalar
device3=_Device3_Object((1,3,6,1,4,1,9839,2,1,1,3),_Device3_Type())
device3.setMaxAccess(_D)
if mibBuilder.loadTexts:device3.setStatus(_A)
if mibBuilder.loadTexts:device3.setUnits(_C)
class _Device4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device4_Type.__name__=_B
_Device4_Object=MibScalar
device4=_Device4_Object((1,3,6,1,4,1,9839,2,1,1,4),_Device4_Type())
device4.setMaxAccess(_D)
if mibBuilder.loadTexts:device4.setStatus(_A)
if mibBuilder.loadTexts:device4.setUnits(_C)
class _Device5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device5_Type.__name__=_B
_Device5_Object=MibScalar
device5=_Device5_Object((1,3,6,1,4,1,9839,2,1,1,5),_Device5_Type())
device5.setMaxAccess(_D)
if mibBuilder.loadTexts:device5.setStatus(_A)
if mibBuilder.loadTexts:device5.setUnits(_C)
class _Device6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device6_Type.__name__=_B
_Device6_Object=MibScalar
device6=_Device6_Object((1,3,6,1,4,1,9839,2,1,1,6),_Device6_Type())
device6.setMaxAccess(_D)
if mibBuilder.loadTexts:device6.setStatus(_A)
if mibBuilder.loadTexts:device6.setUnits(_C)
class _Device7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device7_Type.__name__=_B
_Device7_Object=MibScalar
device7=_Device7_Object((1,3,6,1,4,1,9839,2,1,1,7),_Device7_Type())
device7.setMaxAccess(_D)
if mibBuilder.loadTexts:device7.setStatus(_A)
if mibBuilder.loadTexts:device7.setUnits(_C)
class _Device8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device8_Type.__name__=_B
_Device8_Object=MibScalar
device8=_Device8_Object((1,3,6,1,4,1,9839,2,1,1,8),_Device8_Type())
device8.setMaxAccess(_D)
if mibBuilder.loadTexts:device8.setStatus(_A)
if mibBuilder.loadTexts:device8.setUnits(_C)
class _Device9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device9_Type.__name__=_B
_Device9_Object=MibScalar
device9=_Device9_Object((1,3,6,1,4,1,9839,2,1,1,9),_Device9_Type())
device9.setMaxAccess(_D)
if mibBuilder.loadTexts:device9.setStatus(_A)
if mibBuilder.loadTexts:device9.setUnits(_C)
class _Device10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Device10_Type.__name__=_B
_Device10_Object=MibScalar
device10=_Device10_Object((1,3,6,1,4,1,9839,2,1,1,10),_Device10_Type())
device10.setMaxAccess(_D)
if mibBuilder.loadTexts:device10.setStatus(_A)
if mibBuilder.loadTexts:device10.setUnits(_C)
class _Compressor1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor1_Type.__name__=_B
_Compressor1_Object=MibScalar
compressor1=_Compressor1_Object((1,3,6,1,4,1,9839,2,1,1,12),_Compressor1_Type())
compressor1.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor1.setStatus(_A)
if mibBuilder.loadTexts:compressor1.setUnits(_C)
class _Compressor2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor2_Type.__name__=_B
_Compressor2_Object=MibScalar
compressor2=_Compressor2_Object((1,3,6,1,4,1,9839,2,1,1,13),_Compressor2_Type())
compressor2.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor2.setStatus(_A)
if mibBuilder.loadTexts:compressor2.setUnits(_C)
class _Compressor3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor3_Type.__name__=_B
_Compressor3_Object=MibScalar
compressor3=_Compressor3_Object((1,3,6,1,4,1,9839,2,1,1,14),_Compressor3_Type())
compressor3.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor3.setStatus(_A)
if mibBuilder.loadTexts:compressor3.setUnits(_C)
class _Compressor4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor4_Type.__name__=_B
_Compressor4_Object=MibScalar
compressor4=_Compressor4_Object((1,3,6,1,4,1,9839,2,1,1,15),_Compressor4_Type())
compressor4.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor4.setStatus(_A)
if mibBuilder.loadTexts:compressor4.setUnits(_C)
class _Compressor5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor5_Type.__name__=_B
_Compressor5_Object=MibScalar
compressor5=_Compressor5_Object((1,3,6,1,4,1,9839,2,1,1,16),_Compressor5_Type())
compressor5.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor5.setStatus(_A)
if mibBuilder.loadTexts:compressor5.setUnits(_C)
class _Compressor6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor6_Type.__name__=_B
_Compressor6_Object=MibScalar
compressor6=_Compressor6_Object((1,3,6,1,4,1,9839,2,1,1,17),_Compressor6_Type())
compressor6.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor6.setStatus(_A)
if mibBuilder.loadTexts:compressor6.setUnits(_C)
class _Compressor7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor7_Type.__name__=_B
_Compressor7_Object=MibScalar
compressor7=_Compressor7_Object((1,3,6,1,4,1,9839,2,1,1,18),_Compressor7_Type())
compressor7.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor7.setStatus(_A)
if mibBuilder.loadTexts:compressor7.setUnits(_C)
class _Compressor8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor8_Type.__name__=_B
_Compressor8_Object=MibScalar
compressor8=_Compressor8_Object((1,3,6,1,4,1,9839,2,1,1,19),_Compressor8_Type())
compressor8.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor8.setStatus(_A)
if mibBuilder.loadTexts:compressor8.setUnits(_C)
class _Compressor9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor9_Type.__name__=_B
_Compressor9_Object=MibScalar
compressor9=_Compressor9_Object((1,3,6,1,4,1,9839,2,1,1,20),_Compressor9_Type())
compressor9.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor9.setStatus(_A)
if mibBuilder.loadTexts:compressor9.setUnits(_C)
class _Compressor10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor10_Type.__name__=_B
_Compressor10_Object=MibScalar
compressor10=_Compressor10_Object((1,3,6,1,4,1,9839,2,1,1,21),_Compressor10_Type())
compressor10.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor10.setStatus(_A)
if mibBuilder.loadTexts:compressor10.setUnits(_C)
class _Compressor11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressor11_Type.__name__=_B
_Compressor11_Object=MibScalar
compressor11=_Compressor11_Object((1,3,6,1,4,1,9839,2,1,1,22),_Compressor11_Type())
compressor11.setMaxAccess(_D)
if mibBuilder.loadTexts:compressor11.setStatus(_A)
if mibBuilder.loadTexts:compressor11.setUnits(_C)
class _Fan1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan1_Type.__name__=_B
_Fan1_Object=MibScalar
fan1=_Fan1_Object((1,3,6,1,4,1,9839,2,1,1,23),_Fan1_Type())
fan1.setMaxAccess(_D)
if mibBuilder.loadTexts:fan1.setStatus(_A)
if mibBuilder.loadTexts:fan1.setUnits(_C)
class _Fan2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan2_Type.__name__=_B
_Fan2_Object=MibScalar
fan2=_Fan2_Object((1,3,6,1,4,1,9839,2,1,1,24),_Fan2_Type())
fan2.setMaxAccess(_D)
if mibBuilder.loadTexts:fan2.setStatus(_A)
if mibBuilder.loadTexts:fan2.setUnits(_C)
class _Fan3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan3_Type.__name__=_B
_Fan3_Object=MibScalar
fan3=_Fan3_Object((1,3,6,1,4,1,9839,2,1,1,25),_Fan3_Type())
fan3.setMaxAccess(_D)
if mibBuilder.loadTexts:fan3.setStatus(_A)
if mibBuilder.loadTexts:fan3.setUnits(_C)
class _Fan4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan4_Type.__name__=_B
_Fan4_Object=MibScalar
fan4=_Fan4_Object((1,3,6,1,4,1,9839,2,1,1,26),_Fan4_Type())
fan4.setMaxAccess(_D)
if mibBuilder.loadTexts:fan4.setStatus(_A)
if mibBuilder.loadTexts:fan4.setUnits(_C)
class _Fan5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan5_Type.__name__=_B
_Fan5_Object=MibScalar
fan5=_Fan5_Object((1,3,6,1,4,1,9839,2,1,1,27),_Fan5_Type())
fan5.setMaxAccess(_D)
if mibBuilder.loadTexts:fan5.setStatus(_A)
if mibBuilder.loadTexts:fan5.setUnits(_C)
class _Fan6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan6_Type.__name__=_B
_Fan6_Object=MibScalar
fan6=_Fan6_Object((1,3,6,1,4,1,9839,2,1,1,28),_Fan6_Type())
fan6.setMaxAccess(_D)
if mibBuilder.loadTexts:fan6.setStatus(_A)
if mibBuilder.loadTexts:fan6.setUnits(_C)
class _Fan7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan7_Type.__name__=_B
_Fan7_Object=MibScalar
fan7=_Fan7_Object((1,3,6,1,4,1,9839,2,1,1,29),_Fan7_Type())
fan7.setMaxAccess(_D)
if mibBuilder.loadTexts:fan7.setStatus(_A)
if mibBuilder.loadTexts:fan7.setUnits(_C)
class _Fan8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan8_Type.__name__=_B
_Fan8_Object=MibScalar
fan8=_Fan8_Object((1,3,6,1,4,1,9839,2,1,1,30),_Fan8_Type())
fan8.setMaxAccess(_D)
if mibBuilder.loadTexts:fan8.setStatus(_A)
if mibBuilder.loadTexts:fan8.setUnits(_C)
class _Fan9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan9_Type.__name__=_B
_Fan9_Object=MibScalar
fan9=_Fan9_Object((1,3,6,1,4,1,9839,2,1,1,31),_Fan9_Type())
fan9.setMaxAccess(_D)
if mibBuilder.loadTexts:fan9.setStatus(_A)
if mibBuilder.loadTexts:fan9.setUnits(_C)
class _Fan10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan10_Type.__name__=_B
_Fan10_Object=MibScalar
fan10=_Fan10_Object((1,3,6,1,4,1,9839,2,1,1,32),_Fan10_Type())
fan10.setMaxAccess(_D)
if mibBuilder.loadTexts:fan10.setStatus(_A)
if mibBuilder.loadTexts:fan10.setUnits(_C)
class _Fan11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan11_Type.__name__=_B
_Fan11_Object=MibScalar
fan11=_Fan11_Object((1,3,6,1,4,1,9839,2,1,1,33),_Fan11_Type())
fan11.setMaxAccess(_D)
if mibBuilder.loadTexts:fan11.setStatus(_A)
if mibBuilder.loadTexts:fan11.setUnits(_C)
class _Mal_maint_dev1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev1_Type.__name__=_B
_Mal_maint_dev1_Object=MibScalar
mal_maint_dev1=_Mal_maint_dev1_Object((1,3,6,1,4,1,9839,2,1,1,42),_Mal_maint_dev1_Type())
mal_maint_dev1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev1.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev1.setUnits(_C)
class _Mal_maint_dev2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev2_Type.__name__=_B
_Mal_maint_dev2_Object=MibScalar
mal_maint_dev2=_Mal_maint_dev2_Object((1,3,6,1,4,1,9839,2,1,1,43),_Mal_maint_dev2_Type())
mal_maint_dev2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev2.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev2.setUnits(_C)
class _Mal_maint_dev3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev3_Type.__name__=_B
_Mal_maint_dev3_Object=MibScalar
mal_maint_dev3=_Mal_maint_dev3_Object((1,3,6,1,4,1,9839,2,1,1,44),_Mal_maint_dev3_Type())
mal_maint_dev3.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev3.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev3.setUnits(_C)
class _Mal_maint_dev4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev4_Type.__name__=_B
_Mal_maint_dev4_Object=MibScalar
mal_maint_dev4=_Mal_maint_dev4_Object((1,3,6,1,4,1,9839,2,1,1,45),_Mal_maint_dev4_Type())
mal_maint_dev4.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev4.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev4.setUnits(_C)
class _Mal_maint_dev5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev5_Type.__name__=_B
_Mal_maint_dev5_Object=MibScalar
mal_maint_dev5=_Mal_maint_dev5_Object((1,3,6,1,4,1,9839,2,1,1,46),_Mal_maint_dev5_Type())
mal_maint_dev5.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev5.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev5.setUnits(_C)
class _Mal_maint_dev6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev6_Type.__name__=_B
_Mal_maint_dev6_Object=MibScalar
mal_maint_dev6=_Mal_maint_dev6_Object((1,3,6,1,4,1,9839,2,1,1,47),_Mal_maint_dev6_Type())
mal_maint_dev6.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev6.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev6.setUnits(_C)
class _Mal_maint_dev7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev7_Type.__name__=_B
_Mal_maint_dev7_Object=MibScalar
mal_maint_dev7=_Mal_maint_dev7_Object((1,3,6,1,4,1,9839,2,1,1,48),_Mal_maint_dev7_Type())
mal_maint_dev7.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev7.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev7.setUnits(_C)
class _Mal_maint_dev8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev8_Type.__name__=_B
_Mal_maint_dev8_Object=MibScalar
mal_maint_dev8=_Mal_maint_dev8_Object((1,3,6,1,4,1,9839,2,1,1,49),_Mal_maint_dev8_Type())
mal_maint_dev8.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev8.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev8.setUnits(_C)
class _Mal_maint_dev9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev9_Type.__name__=_B
_Mal_maint_dev9_Object=MibScalar
mal_maint_dev9=_Mal_maint_dev9_Object((1,3,6,1,4,1,9839,2,1,1,50),_Mal_maint_dev9_Type())
mal_maint_dev9.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev9.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev9.setUnits(_C)
class _Mal_maint_dev10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev10_Type.__name__=_B
_Mal_maint_dev10_Object=MibScalar
mal_maint_dev10=_Mal_maint_dev10_Object((1,3,6,1,4,1,9839,2,1,1,51),_Mal_maint_dev10_Type())
mal_maint_dev10.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev10.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev10.setUnits(_C)
class _Mal_maint_dev11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_maint_dev11_Type.__name__=_B
_Mal_maint_dev11_Object=MibScalar
mal_maint_dev11=_Mal_maint_dev11_Object((1,3,6,1,4,1,9839,2,1,1,52),_Mal_maint_dev11_Type())
mal_maint_dev11.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_maint_dev11.setStatus(_A)
if mibBuilder.loadTexts:mal_maint_dev11.setUnits(_C)
class _Mal_m_invdev1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_m_invdev1_Type.__name__=_B
_Mal_m_invdev1_Object=MibScalar
mal_m_invdev1=_Mal_m_invdev1_Object((1,3,6,1,4,1,9839,2,1,1,53),_Mal_m_invdev1_Type())
mal_m_invdev1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_m_invdev1.setStatus(_A)
if mibBuilder.loadTexts:mal_m_invdev1.setUnits(_C)
class _Mal_broke_pr1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_broke_pr1_Type.__name__=_B
_Mal_broke_pr1_Object=MibScalar
mal_broke_pr1=_Mal_broke_pr1_Object((1,3,6,1,4,1,9839,2,1,1,54),_Mal_broke_pr1_Type())
mal_broke_pr1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_broke_pr1.setStatus(_A)
if mibBuilder.loadTexts:mal_broke_pr1.setUnits(_C)
class _Mal_broke_pr2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_broke_pr2_Type.__name__=_B
_Mal_broke_pr2_Object=MibScalar
mal_broke_pr2=_Mal_broke_pr2_Object((1,3,6,1,4,1,9839,2,1,1,55),_Mal_broke_pr2_Type())
mal_broke_pr2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_broke_pr2.setStatus(_A)
if mibBuilder.loadTexts:mal_broke_pr2.setUnits(_C)
class _Mal_broke_pr3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_broke_pr3_Type.__name__=_B
_Mal_broke_pr3_Object=MibScalar
mal_broke_pr3=_Mal_broke_pr3_Object((1,3,6,1,4,1,9839,2,1,1,56),_Mal_broke_pr3_Type())
mal_broke_pr3.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_broke_pr3.setStatus(_A)
if mibBuilder.loadTexts:mal_broke_pr3.setUnits(_C)
class _Mal_pres_hpres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_pres_hpres_Type.__name__=_B
_Mal_pres_hpres_Object=MibScalar
mal_pres_hpres=_Mal_pres_hpres_Object((1,3,6,1,4,1,9839,2,1,1,57),_Mal_pres_hpres_Type())
mal_pres_hpres.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_pres_hpres.setStatus(_A)
if mibBuilder.loadTexts:mal_pres_hpres.setUnits(_C)
class _Mal_pres_lpres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_pres_lpres_Type.__name__=_B
_Mal_pres_lpres_Object=MibScalar
mal_pres_lpres=_Mal_pres_lpres_Object((1,3,6,1,4,1,9839,2,1,1,58),_Mal_pres_lpres_Type())
mal_pres_lpres.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_pres_lpres.setStatus(_A)
if mibBuilder.loadTexts:mal_pres_lpres.setUnits(_C)
class _Mal_block_dev1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev1_Type.__name__=_B
_Mal_block_dev1_Object=MibScalar
mal_block_dev1=_Mal_block_dev1_Object((1,3,6,1,4,1,9839,2,1,1,59),_Mal_block_dev1_Type())
mal_block_dev1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev1.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev1.setUnits(_C)
class _Mal_block_dev2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev2_Type.__name__=_B
_Mal_block_dev2_Object=MibScalar
mal_block_dev2=_Mal_block_dev2_Object((1,3,6,1,4,1,9839,2,1,1,60),_Mal_block_dev2_Type())
mal_block_dev2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev2.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev2.setUnits(_C)
class _Mal_block_dev3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev3_Type.__name__=_B
_Mal_block_dev3_Object=MibScalar
mal_block_dev3=_Mal_block_dev3_Object((1,3,6,1,4,1,9839,2,1,1,61),_Mal_block_dev3_Type())
mal_block_dev3.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev3.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev3.setUnits(_C)
class _Mal_block_dev4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev4_Type.__name__=_B
_Mal_block_dev4_Object=MibScalar
mal_block_dev4=_Mal_block_dev4_Object((1,3,6,1,4,1,9839,2,1,1,62),_Mal_block_dev4_Type())
mal_block_dev4.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev4.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev4.setUnits(_C)
class _Mal_block_dev5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev5_Type.__name__=_B
_Mal_block_dev5_Object=MibScalar
mal_block_dev5=_Mal_block_dev5_Object((1,3,6,1,4,1,9839,2,1,1,63),_Mal_block_dev5_Type())
mal_block_dev5.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev5.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev5.setUnits(_C)
class _Mal_block_dev6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev6_Type.__name__=_B
_Mal_block_dev6_Object=MibScalar
mal_block_dev6=_Mal_block_dev6_Object((1,3,6,1,4,1,9839,2,1,1,64),_Mal_block_dev6_Type())
mal_block_dev6.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev6.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev6.setUnits(_C)
class _Mal_block_dev7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev7_Type.__name__=_B
_Mal_block_dev7_Object=MibScalar
mal_block_dev7=_Mal_block_dev7_Object((1,3,6,1,4,1,9839,2,1,1,65),_Mal_block_dev7_Type())
mal_block_dev7.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev7.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev7.setUnits(_C)
class _Mal_block_dev8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev8_Type.__name__=_B
_Mal_block_dev8_Object=MibScalar
mal_block_dev8=_Mal_block_dev8_Object((1,3,6,1,4,1,9839,2,1,1,66),_Mal_block_dev8_Type())
mal_block_dev8.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev8.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev8.setUnits(_C)
class _Mal_block_dev9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev9_Type.__name__=_B
_Mal_block_dev9_Object=MibScalar
mal_block_dev9=_Mal_block_dev9_Object((1,3,6,1,4,1,9839,2,1,1,67),_Mal_block_dev9_Type())
mal_block_dev9.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev9.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev9.setUnits(_C)
class _Mal_block_dev10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev10_Type.__name__=_B
_Mal_block_dev10_Object=MibScalar
mal_block_dev10=_Mal_block_dev10_Object((1,3,6,1,4,1,9839,2,1,1,68),_Mal_block_dev10_Type())
mal_block_dev10.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev10.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev10.setUnits(_C)
class _Mal_block_dev11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_block_dev11_Type.__name__=_B
_Mal_block_dev11_Object=MibScalar
mal_block_dev11=_Mal_block_dev11_Object((1,3,6,1,4,1,9839,2,1,1,69),_Mal_block_dev11_Type())
mal_block_dev11.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_block_dev11.setStatus(_A)
if mibBuilder.loadTexts:mal_block_dev11.setUnits(_C)
class _Mal_high1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_high1_Type.__name__=_B
_Mal_high1_Object=MibScalar
mal_high1=_Mal_high1_Object((1,3,6,1,4,1,9839,2,1,1,70),_Mal_high1_Type())
mal_high1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_high1.setStatus(_A)
if mibBuilder.loadTexts:mal_high1.setUnits(_C)
class _Mal_low1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_low1_Type.__name__=_B
_Mal_low1_Object=MibScalar
mal_low1=_Mal_low1_Object((1,3,6,1,4,1,9839,2,1,1,71),_Mal_low1_Type())
mal_low1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_low1.setStatus(_A)
if mibBuilder.loadTexts:mal_low1.setUnits(_C)
class _Mal_high2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_high2_Type.__name__=_B
_Mal_high2_Object=MibScalar
mal_high2=_Mal_high2_Object((1,3,6,1,4,1,9839,2,1,1,72),_Mal_high2_Type())
mal_high2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_high2.setStatus(_A)
if mibBuilder.loadTexts:mal_high2.setUnits(_C)
class _Mal_low2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_low2_Type.__name__=_B
_Mal_low2_Object=MibScalar
mal_low2=_Mal_low2_Object((1,3,6,1,4,1,9839,2,1,1,73),_Mal_low2_Type())
mal_low2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_low2.setStatus(_A)
if mibBuilder.loadTexts:mal_low2.setUnits(_C)
class _Mal_n_devices_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_n_devices_Type.__name__=_B
_Mal_n_devices_Object=MibScalar
mal_n_devices=_Mal_n_devices_Object((1,3,6,1,4,1,9839,2,1,1,74),_Mal_n_devices_Type())
mal_n_devices.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_n_devices.setStatus(_A)
if mibBuilder.loadTexts:mal_n_devices.setUnits(_C)
class _Mepromnook_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mepromnook_Type.__name__=_B
_Mepromnook_Object=MibScalar
mepromnook=_Mepromnook_Object((1,3,6,1,4,1,9839,2,1,1,75),_Mepromnook_Type())
mepromnook.setMaxAccess(_D)
if mibBuilder.loadTexts:mepromnook.setStatus(_A)
if mibBuilder.loadTexts:mepromnook.setUnits(_C)
class _Mal_clock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_clock_Type.__name__=_B
_Mal_clock_Object=MibScalar
mal_clock=_Mal_clock_Object((1,3,6,1,4,1,9839,2,1,1,76),_Mal_clock_Type())
mal_clock.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_clock.setStatus(_A)
if mibBuilder.loadTexts:mal_clock.setUnits(_C)
class _Syson_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Syson_Type.__name__=_B
_Syson_Object=MibScalar
syson=_Syson_Object((1,3,6,1,4,1,9839,2,1,1,77),_Syson_Type())
syson.setMaxAccess(_E)
if mibBuilder.loadTexts:syson.setStatus(_A)
if mibBuilder.loadTexts:syson.setUnits(_C)
class _Control_type1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Control_type1_Type.__name__=_B
_Control_type1_Object=MibScalar
control_type1=_Control_type1_Object((1,3,6,1,4,1,9839,2,1,1,114),_Control_type1_Type())
control_type1.setMaxAccess(_E)
if mibBuilder.loadTexts:control_type1.setStatus(_A)
if mibBuilder.loadTexts:control_type1.setUnits(_C)
class _Control_type2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Control_type2_Type.__name__=_B
_Control_type2_Object=MibScalar
control_type2=_Control_type2_Object((1,3,6,1,4,1,9839,2,1,1,115),_Control_type2_Type())
control_type2.setMaxAccess(_E)
if mibBuilder.loadTexts:control_type2.setStatus(_A)
if mibBuilder.loadTexts:control_type2.setUnits('sec')
class _En_inv_dev1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_inv_dev1_Type.__name__=_B
_En_inv_dev1_Object=MibScalar
en_inv_dev1=_En_inv_dev1_Object((1,3,6,1,4,1,9839,2,1,1,116),_En_inv_dev1_Type())
en_inv_dev1.setMaxAccess(_E)
if mibBuilder.loadTexts:en_inv_dev1.setStatus(_A)
if mibBuilder.loadTexts:en_inv_dev1.setUnits(_C)
class _En_rotation1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_rotation1_Type.__name__=_B
_En_rotation1_Object=MibScalar
en_rotation1=_En_rotation1_Object((1,3,6,1,4,1,9839,2,1,1,117),_En_rotation1_Type())
en_rotation1.setMaxAccess(_E)
if mibBuilder.loadTexts:en_rotation1.setStatus(_A)
if mibBuilder.loadTexts:en_rotation1.setUnits(_C)
class _En_rotation2_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_rotation2_Type.__name__=_B
_En_rotation2_Object=MibScalar
en_rotation2=_En_rotation2_Object((1,3,6,1,4,1,9839,2,1,1,118),_En_rotation2_Type())
en_rotation2.setMaxAccess(_E)
if mibBuilder.loadTexts:en_rotation2.setStatus(_A)
if mibBuilder.loadTexts:en_rotation2.setUnits(_C)
class _On_off_boss_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_On_off_boss_Type.__name__=_B
_On_off_boss_Object=MibScalar
on_off_boss=_On_off_boss_Object((1,3,6,1,4,1,9839,2,1,1,119),_On_off_boss_Type())
on_off_boss.setMaxAccess(_E)
if mibBuilder.loadTexts:on_off_boss.setStatus(_A)
if mibBuilder.loadTexts:on_off_boss.setUnits(_C)
class _Cel_fahr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cel_fahr_Type.__name__=_B
_Cel_fahr_Object=MibScalar
cel_fahr=_Cel_fahr_Object((1,3,6,1,4,1,9839,2,1,1,120),_Cel_fahr_Type())
cel_fahr.setMaxAccess(_E)
if mibBuilder.loadTexts:cel_fahr.setStatus(_A)
if mibBuilder.loadTexts:cel_fahr.setUnits('sec')
class _En_air_temp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_air_temp_Type.__name__=_B
_En_air_temp_Object=MibScalar
en_air_temp=_En_air_temp_Object((1,3,6,1,4,1,9839,2,1,1,121),_En_air_temp_Type())
en_air_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:en_air_temp.setStatus(_A)
if mibBuilder.loadTexts:en_air_temp.setUnits(_C)
class _Bool_device11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Bool_device11_Type.__name__=_B
_Bool_device11_Object=MibScalar
bool_device11=_Bool_device11_Object((1,3,6,1,4,1,9839,2,1,1,124),_Bool_device11_Type())
bool_device11.setMaxAccess(_D)
if mibBuilder.loadTexts:bool_device11.setStatus(_A)
if mibBuilder.loadTexts:bool_device11.setUnits(_C)
class _Off_mode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Off_mode_Type.__name__=_B
_Off_mode_Object=MibScalar
off_mode=_Off_mode_Object((1,3,6,1,4,1,9839,2,1,1,125),_Off_mode_Type())
off_mode.setMaxAccess(_E)
if mibBuilder.loadTexts:off_mode.setStatus(_A)
if mibBuilder.loadTexts:off_mode.setUnits(_C)
class _Cool_heat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cool_heat_Type.__name__=_B
_Cool_heat_Object=MibScalar
cool_heat=_Cool_heat_Object((1,3,6,1,4,1,9839,2,1,1,126),_Cool_heat_Type())
cool_heat.setMaxAccess(_E)
if mibBuilder.loadTexts:cool_heat.setStatus(_A)
if mibBuilder.loadTexts:cool_heat.setUnits(_C)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Probe_circ1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Probe_circ1_Type.__name__=_B
_Probe_circ1_Object=MibScalar
probe_circ1=_Probe_circ1_Object((1,3,6,1,4,1,9839,2,1,2,1),_Probe_circ1_Type())
probe_circ1.setMaxAccess(_D)
if mibBuilder.loadTexts:probe_circ1.setStatus(_A)
if mibBuilder.loadTexts:probe_circ1.setUnits('C x10')
class _Probe_circ2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Probe_circ2_Type.__name__=_B
_Probe_circ2_Object=MibScalar
probe_circ2=_Probe_circ2_Object((1,3,6,1,4,1,9839,2,1,2,2),_Probe_circ2_Type())
probe_circ2.setMaxAccess(_D)
if mibBuilder.loadTexts:probe_circ2.setStatus(_A)
if mibBuilder.loadTexts:probe_circ2.setUnits('C x10')
class _Setp_air_temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Setp_air_temp_Type.__name__=_B
_Setp_air_temp_Object=MibScalar
setp_air_temp=_Setp_air_temp_Object((1,3,6,1,4,1,9839,2,1,2,3),_Setp_air_temp_Type())
setp_air_temp.setMaxAccess(_E)
if mibBuilder.loadTexts:setp_air_temp.setStatus(_A)
if mibBuilder.loadTexts:setp_air_temp.setUnits(_C)
class _Inverter_fan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Inverter_fan_Type.__name__=_B
_Inverter_fan_Object=MibScalar
inverter_fan=_Inverter_fan_Object((1,3,6,1,4,1,9839,2,1,2,4),_Inverter_fan_Type())
inverter_fan.setMaxAccess(_D)
if mibBuilder.loadTexts:inverter_fan.setStatus(_A)
if mibBuilder.loadTexts:inverter_fan.setUnits('V x10')
class _Inverter_dev1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Inverter_dev1_Type.__name__=_B
_Inverter_dev1_Object=MibScalar
inverter_dev1=_Inverter_dev1_Object((1,3,6,1,4,1,9839,2,1,2,5),_Inverter_dev1_Type())
inverter_dev1.setMaxAccess(_D)
if mibBuilder.loadTexts:inverter_dev1.setStatus(_A)
if mibBuilder.loadTexts:inverter_dev1.setUnits('V x10')
class _Set_circuit1_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_circuit1_Type.__name__=_B
_Set_circuit1_Object=MibScalar
set_circuit1=_Set_circuit1_Object((1,3,6,1,4,1,9839,2,1,2,6),_Set_circuit1_Type())
set_circuit1.setMaxAccess(_E)
if mibBuilder.loadTexts:set_circuit1.setStatus(_A)
if mibBuilder.loadTexts:set_circuit1.setUnits(_F)
class _Set_c1_mask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_c1_mask_Type.__name__=_B
_Set_c1_mask_Object=MibScalar
set_c1_mask=_Set_c1_mask_Object((1,3,6,1,4,1,9839,2,1,2,7),_Set_c1_mask_Type())
set_c1_mask.setMaxAccess(_D)
if mibBuilder.loadTexts:set_c1_mask.setStatus(_A)
if mibBuilder.loadTexts:set_c1_mask.setUnits(_F)
class _Reduced_set_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Reduced_set_Type.__name__=_B
_Reduced_set_Object=MibScalar
reduced_set=_Reduced_set_Object((1,3,6,1,4,1,9839,2,1,2,8),_Reduced_set_Type())
reduced_set.setMaxAccess(_E)
if mibBuilder.loadTexts:reduced_set.setStatus(_A)
if mibBuilder.loadTexts:reduced_set.setUnits(_F)
class _Set_inv_dev1_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_inv_dev1_Type.__name__=_B
_Set_inv_dev1_Object=MibScalar
set_inv_dev1=_Set_inv_dev1_Object((1,3,6,1,4,1,9839,2,1,2,9),_Set_inv_dev1_Type())
set_inv_dev1.setMaxAccess(_E)
if mibBuilder.loadTexts:set_inv_dev1.setStatus(_A)
if mibBuilder.loadTexts:set_inv_dev1.setUnits(_F)
class _Set_inv_fan_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_inv_fan_Type.__name__=_B
_Set_inv_fan_Object=MibScalar
set_inv_fan=_Set_inv_fan_Object((1,3,6,1,4,1,9839,2,1,2,10),_Set_inv_fan_Type())
set_inv_fan.setMaxAccess(_E)
if mibBuilder.loadTexts:set_inv_fan.setStatus(_A)
if mibBuilder.loadTexts:set_inv_fan.setUnits(_F)
class _Comp_setp_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Comp_setp_Type.__name__=_B
_Comp_setp_Object=MibScalar
comp_setp=_Comp_setp_Object((1,3,6,1,4,1,9839,2,1,2,11),_Comp_setp_Type())
comp_setp.setMaxAccess(_E)
if mibBuilder.loadTexts:comp_setp.setStatus(_A)
if mibBuilder.loadTexts:comp_setp.setUnits('min x10')
class _Set_circuit2_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_circuit2_Type.__name__=_B
_Set_circuit2_Object=MibScalar
set_circuit2=_Set_circuit2_Object((1,3,6,1,4,1,9839,2,1,2,12),_Set_circuit2_Type())
set_circuit2.setMaxAccess(_E)
if mibBuilder.loadTexts:set_circuit2.setStatus(_A)
if mibBuilder.loadTexts:set_circuit2.setUnits(_F)
class _Diff_circuit1_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Diff_circuit1_Type.__name__=_B
_Diff_circuit1_Object=MibScalar
diff_circuit1=_Diff_circuit1_Object((1,3,6,1,4,1,9839,2,1,2,13),_Diff_circuit1_Type())
diff_circuit1.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_circuit1.setStatus(_A)
if mibBuilder.loadTexts:diff_circuit1.setUnits(_F)
class _Diff_circuit2_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Diff_circuit2_Type.__name__=_B
_Diff_circuit2_Object=MibScalar
diff_circuit2=_Diff_circuit2_Object((1,3,6,1,4,1,9839,2,1,2,14),_Diff_circuit2_Type())
diff_circuit2.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_circuit2.setStatus(_A)
if mibBuilder.loadTexts:diff_circuit2.setUnits(_F)
class _Thresh_low1_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Thresh_low1_Type.__name__=_B
_Thresh_low1_Object=MibScalar
thresh_low1=_Thresh_low1_Object((1,3,6,1,4,1,9839,2,1,2,15),_Thresh_low1_Type())
thresh_low1.setMaxAccess(_E)
if mibBuilder.loadTexts:thresh_low1.setStatus(_A)
if mibBuilder.loadTexts:thresh_low1.setUnits(_F)
class _Thresh_low2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Thresh_low2_Type.__name__=_B
_Thresh_low2_Object=MibScalar
thresh_low2=_Thresh_low2_Object((1,3,6,1,4,1,9839,2,1,2,16),_Thresh_low2_Type())
thresh_low2.setMaxAccess(_E)
if mibBuilder.loadTexts:thresh_low2.setStatus(_A)
if mibBuilder.loadTexts:thresh_low2.setUnits(_F)
class _Thresh_high1_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Thresh_high1_Type.__name__=_B
_Thresh_high1_Object=MibScalar
thresh_high1=_Thresh_high1_Object((1,3,6,1,4,1,9839,2,1,2,17),_Thresh_high1_Type())
thresh_high1.setMaxAccess(_E)
if mibBuilder.loadTexts:thresh_high1.setStatus(_A)
if mibBuilder.loadTexts:thresh_high1.setUnits(_F)
class _Thresh_high2_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Thresh_high2_Type.__name__=_B
_Thresh_high2_Object=MibScalar
thresh_high2=_Thresh_high2_Object((1,3,6,1,4,1,9839,2,1,2,18),_Thresh_high2_Type())
thresh_high2.setMaxAccess(_E)
if mibBuilder.loadTexts:thresh_high2.setStatus(_A)
if mibBuilder.loadTexts:thresh_high2.setUnits(_F)
class _Min_setp1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Min_setp1_Type.__name__=_B
_Min_setp1_Object=MibScalar
min_setp1=_Min_setp1_Object((1,3,6,1,4,1,9839,2,1,2,19),_Min_setp1_Type())
min_setp1.setMaxAccess(_E)
if mibBuilder.loadTexts:min_setp1.setStatus(_A)
if mibBuilder.loadTexts:min_setp1.setUnits(_F)
class _Min_setp2_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Min_setp2_Type.__name__=_B
_Min_setp2_Object=MibScalar
min_setp2=_Min_setp2_Object((1,3,6,1,4,1,9839,2,1,2,20),_Min_setp2_Type())
min_setp2.setMaxAccess(_E)
if mibBuilder.loadTexts:min_setp2.setStatus(_A)
if mibBuilder.loadTexts:min_setp2.setUnits(_F)
class _Max_setp1_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Max_setp1_Type.__name__=_B
_Max_setp1_Object=MibScalar
max_setp1=_Max_setp1_Object((1,3,6,1,4,1,9839,2,1,2,21),_Max_setp1_Type())
max_setp1.setMaxAccess(_E)
if mibBuilder.loadTexts:max_setp1.setStatus(_A)
if mibBuilder.loadTexts:max_setp1.setUnits(_F)
class _Max_setp2_Type(Integer32):defaultValue=240;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-990,999))
_Max_setp2_Type.__name__=_B
_Max_setp2_Object=MibScalar
max_setp2=_Max_setp2_Object((1,3,6,1,4,1,9839,2,1,2,22),_Max_setp2_Type())
max_setp2.setMaxAccess(_E)
if mibBuilder.loadTexts:max_setp2.setStatus(_A)
if mibBuilder.loadTexts:max_setp2.setUnits(_F)
class _Diff_inv_dev1_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Diff_inv_dev1_Type.__name__=_B
_Diff_inv_dev1_Object=MibScalar
diff_inv_dev1=_Diff_inv_dev1_Object((1,3,6,1,4,1,9839,2,1,2,23),_Diff_inv_dev1_Type())
diff_inv_dev1.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_inv_dev1.setStatus(_A)
if mibBuilder.loadTexts:diff_inv_dev1.setUnits(_F)
class _Diff_inv_fan_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Diff_inv_fan_Type.__name__=_B
_Diff_inv_fan_Object=MibScalar
diff_inv_fan=_Diff_inv_fan_Object((1,3,6,1,4,1,9839,2,1,2,24),_Diff_inv_fan_Type())
diff_inv_fan.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_inv_fan.setStatus(_A)
if mibBuilder.loadTexts:diff_inv_fan.setUnits(_F)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Day_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_Day_Type.__name__=_B
_Day_Object=MibScalar
day=_Day_Object((1,3,6,1,4,1,9839,2,1,3,34),_Day_Type())
day.setMaxAccess(_D)
if mibBuilder.loadTexts:day.setStatus(_A)
if mibBuilder.loadTexts:day.setUnits(_C)
class _Month_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_Month_Type.__name__=_B
_Month_Object=MibScalar
month=_Month_Object((1,3,6,1,4,1,9839,2,1,3,35),_Month_Type())
month.setMaxAccess(_D)
if mibBuilder.loadTexts:month.setStatus(_A)
if mibBuilder.loadTexts:month.setUnits(_C)
class _Pyear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_Pyear_Type.__name__=_B
_Pyear_Object=MibScalar
pyear=_Pyear_Object((1,3,6,1,4,1,9839,2,1,3,36),_Pyear_Type())
pyear.setMaxAccess(_D)
if mibBuilder.loadTexts:pyear.setStatus(_A)
if mibBuilder.loadTexts:pyear.setUnits(_C)
class _Lday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_Lday_Type.__name__=_B
_Lday_Object=MibScalar
lday=_Lday_Object((1,3,6,1,4,1,9839,2,1,3,37),_Lday_Type())
lday.setMaxAccess(_E)
if mibBuilder.loadTexts:lday.setStatus(_A)
if mibBuilder.loadTexts:lday.setUnits(_C)
class _Lmonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Lmonth_Type.__name__=_B
_Lmonth_Object=MibScalar
lmonth=_Lmonth_Object((1,3,6,1,4,1,9839,2,1,3,38),_Lmonth_Type())
lmonth.setMaxAccess(_E)
if mibBuilder.loadTexts:lmonth.setStatus(_A)
if mibBuilder.loadTexts:lmonth.setUnits(_C)
class _Lyear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_Lyear_Type.__name__=_B
_Lyear_Object=MibScalar
lyear=_Lyear_Object((1,3,6,1,4,1,9839,2,1,3,39),_Lyear_Type())
lyear.setMaxAccess(_E)
if mibBuilder.loadTexts:lyear.setStatus(_A)
if mibBuilder.loadTexts:lyear.setUnits(_C)
class _Hour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Hour_Type.__name__=_B
_Hour_Object=MibScalar
hour=_Hour_Object((1,3,6,1,4,1,9839,2,1,3,40),_Hour_Type())
hour.setMaxAccess(_D)
if mibBuilder.loadTexts:hour.setStatus(_A)
if mibBuilder.loadTexts:hour.setUnits('hour')
class _Minute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Minute_Type.__name__=_B
_Minute_Object=MibScalar
minute=_Minute_Object((1,3,6,1,4,1,9839,2,1,3,41),_Minute_Type())
minute.setMaxAccess(_D)
if mibBuilder.loadTexts:minute.setStatus(_A)
if mibBuilder.loadTexts:minute.setUnits('min')
class _Lhour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_Lhour_Type.__name__=_B
_Lhour_Object=MibScalar
lhour=_Lhour_Object((1,3,6,1,4,1,9839,2,1,3,42),_Lhour_Type())
lhour.setMaxAccess(_E)
if mibBuilder.loadTexts:lhour.setStatus(_A)
if mibBuilder.loadTexts:lhour.setUnits(_C)
class _Lminute_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_Lminute_Type.__name__=_B
_Lminute_Object=MibScalar
lminute=_Lminute_Object((1,3,6,1,4,1,9839,2,1,3,43),_Lminute_Type())
lminute.setMaxAccess(_E)
if mibBuilder.loadTexts:lminute.setStatus(_A)
if mibBuilder.loadTexts:lminute.setUnits(_C)
class _Delay_low_press_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Delay_low_press_Type.__name__=_B
_Delay_low_press_Object=MibScalar
delay_low_press=_Delay_low_press_Object((1,3,6,1,4,1,9839,2,1,3,44),_Delay_low_press_Type())
delay_low_press.setMaxAccess(_E)
if mibBuilder.loadTexts:delay_low_press.setStatus(_A)
if mibBuilder.loadTexts:delay_low_press.setUnits(_C)
class _N_devices1_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_N_devices1_Type.__name__=_B
_N_devices1_Object=MibScalar
n_devices1=_N_devices1_Object((1,3,6,1,4,1,9839,2,1,3,45),_N_devices1_Type())
n_devices1.setMaxAccess(_E)
if mibBuilder.loadTexts:n_devices1.setStatus(_A)
if mibBuilder.loadTexts:n_devices1.setUnits(_C)
class _N_devices2_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_N_devices2_Type.__name__=_B
_N_devices2_Object=MibScalar
n_devices2=_N_devices2_Object((1,3,6,1,4,1,9839,2,1,3,46),_N_devices2_Type())
n_devices2.setMaxAccess(_E)
if mibBuilder.loadTexts:n_devices2.setStatus(_A)
if mibBuilder.loadTexts:n_devices2.setUnits(_C)
class _N_partial_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_N_partial_Type.__name__=_B
_N_partial_Object=MibScalar
n_partial=_N_partial_Object((1,3,6,1,4,1,9839,2,1,3,47),_N_partial_Type())
n_partial.setMaxAccess(_E)
if mibBuilder.loadTexts:n_partial.setStatus(_A)
if mibBuilder.loadTexts:n_partial.setUnits(_C)
mibBuilder.exportSymbols('CAREL-insgrd-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'insgrdMIB':insgrdMIB,'digitalObjects':digitalObjects,'device1':device1,'device2':device2,'device3':device3,'device4':device4,'device5':device5,'device6':device6,'device7':device7,'device8':device8,'device9':device9,'device10':device10,'compressor1':compressor1,'compressor2':compressor2,'compressor3':compressor3,'compressor4':compressor4,'compressor5':compressor5,'compressor6':compressor6,'compressor7':compressor7,'compressor8':compressor8,'compressor9':compressor9,'compressor10':compressor10,'compressor11':compressor11,'fan1':fan1,'fan2':fan2,'fan3':fan3,'fan4':fan4,'fan5':fan5,'fan6':fan6,'fan7':fan7,'fan8':fan8,'fan9':fan9,'fan10':fan10,'fan11':fan11,'mal_maint_dev1':mal_maint_dev1,'mal_maint_dev2':mal_maint_dev2,'mal_maint_dev3':mal_maint_dev3,'mal_maint_dev4':mal_maint_dev4,'mal_maint_dev5':mal_maint_dev5,'mal_maint_dev6':mal_maint_dev6,'mal_maint_dev7':mal_maint_dev7,'mal_maint_dev8':mal_maint_dev8,'mal_maint_dev9':mal_maint_dev9,'mal_maint_dev10':mal_maint_dev10,'mal_maint_dev11':mal_maint_dev11,'mal_m_invdev1':mal_m_invdev1,'mal_broke_pr1':mal_broke_pr1,'mal_broke_pr2':mal_broke_pr2,'mal_broke_pr3':mal_broke_pr3,'mal_pres_hpres':mal_pres_hpres,'mal_pres_lpres':mal_pres_lpres,'mal_block_dev1':mal_block_dev1,'mal_block_dev2':mal_block_dev2,'mal_block_dev3':mal_block_dev3,'mal_block_dev4':mal_block_dev4,'mal_block_dev5':mal_block_dev5,'mal_block_dev6':mal_block_dev6,'mal_block_dev7':mal_block_dev7,'mal_block_dev8':mal_block_dev8,'mal_block_dev9':mal_block_dev9,'mal_block_dev10':mal_block_dev10,'mal_block_dev11':mal_block_dev11,'mal_high1':mal_high1,'mal_low1':mal_low1,'mal_high2':mal_high2,'mal_low2':mal_low2,'mal_n_devices':mal_n_devices,'mepromnook':mepromnook,'mal_clock':mal_clock,'syson':syson,'control_type1':control_type1,'control_type2':control_type2,'en_inv_dev1':en_inv_dev1,'en_rotation1':en_rotation1,'en_rotation2':en_rotation2,'on_off_boss':on_off_boss,'cel_fahr':cel_fahr,'en_air_temp':en_air_temp,'bool_device11':bool_device11,'off_mode':off_mode,'cool_heat':cool_heat,'analogObjects':analogObjects,'probe_circ1':probe_circ1,'probe_circ2':probe_circ2,'setp_air_temp':setp_air_temp,'inverter_fan':inverter_fan,'inverter_dev1':inverter_dev1,'set_circuit1':set_circuit1,'set_c1_mask':set_c1_mask,'reduced_set':reduced_set,'set_inv_dev1':set_inv_dev1,'set_inv_fan':set_inv_fan,'comp_setp':comp_setp,'set_circuit2':set_circuit2,'diff_circuit1':diff_circuit1,'diff_circuit2':diff_circuit2,'thresh_low1':thresh_low1,'thresh_low2':thresh_low2,'thresh_high1':thresh_high1,'thresh_high2':thresh_high2,'min_setp1':min_setp1,'min_setp2':min_setp2,'max_setp1':max_setp1,'max_setp2':max_setp2,'diff_inv_dev1':diff_inv_dev1,'diff_inv_fan':diff_inv_fan,'integerObjects':integerObjects,'day':day,'month':month,'pyear':pyear,'lday':lday,'lmonth':lmonth,'lyear':lyear,'hour':hour,'minute':minute,'lhour':lhour,'lminute':lminute,'delay_low_press':delay_low_press,'n_devices1':n_devices1,'n_devices2':n_devices2,'n_partial':n_partial})