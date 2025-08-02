_I='min.'
_H='bar/ x10'
_G='sec.'
_F='C/F x10'
_E='read-only'
_D='read-write'
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
mioMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_C)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_E)
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
netSize.setMaxAccess(_D)
if mibBuilder.loadTexts:netSize.setStatus(_A)
if mibBuilder.loadTexts:netSize.setUnits(_C)
class _BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200))
_BaudRate_Type.__name__=_B
_BaudRate_Object=MibScalar
baudRate=_BaudRate_Object((1,3,6,1,4,1,9839,2,0,1,2),_BaudRate_Type())
baudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:baudRate.setStatus(_A)
if mibBuilder.loadTexts:baudRate.setUnits(_C)
_UnitTypeGroup_ObjectIdentity=ObjectIdentity
unitTypeGroup=_UnitTypeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,2))
_Unit1_Type_Type=DisplayString
_Unit1_Type_Object=MibScalar
unit1_Type=_Unit1_Type_Object((1,3,6,1,4,1,9839,2,0,2,1),_Unit1_Type_Type())
unit1_Type.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_C)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_C)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_C)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_C)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_C)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_C)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_C)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_C)
_UnitOnLineStatusGroup_ObjectIdentity=ObjectIdentity
unitOnLineStatusGroup=_UnitOnLineStatusGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,10))
_Unit1_OnLineStatus_Type=Integer32
_Unit1_OnLineStatus_Object=MibScalar
unit1_OnLineStatus=_Unit1_OnLineStatus_Object((1,3,6,1,4,1,9839,2,0,10,1),_Unit1_OnLineStatus_Type())
unit1_OnLineStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:unit1_OnLineStatus.setStatus(_A)
if mibBuilder.loadTexts:unit1_OnLineStatus.setUnits(_C)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _Buz_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Buz_Type.__name__=_B
_Buz_Object=MibScalar
buz=_Buz_Object((1,3,6,1,4,1,9839,2,1,1,1),_Buz_Type())
buz.setMaxAccess(_D)
if mibBuilder.loadTexts:buz.setStatus(_A)
if mibBuilder.loadTexts:buz.setUnits(_C)
class _Cf_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Cf_Type.__name__=_B
_Cf_Object=MibScalar
cf=_Cf_Object((1,3,6,1,4,1,9839,2,1,1,2),_Cf_Type())
cf.setMaxAccess(_D)
if mibBuilder.loadTexts:cf.setStatus(_A)
if mibBuilder.loadTexts:cf.setUnits(_C)
class _Mtd1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mtd1_Type.__name__=_B
_Mtd1_Object=MibScalar
mtd1=_Mtd1_Object((1,3,6,1,4,1,9839,2,1,1,3),_Mtd1_Type())
mtd1.setMaxAccess(_D)
if mibBuilder.loadTexts:mtd1.setStatus(_A)
if mibBuilder.loadTexts:mtd1.setUnits(_C)
class _Mtd2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mtd2_Type.__name__=_B
_Mtd2_Object=MibScalar
mtd2=_Mtd2_Object((1,3,6,1,4,1,9839,2,1,1,4),_Mtd2_Type())
mtd2.setMaxAccess(_D)
if mibBuilder.loadTexts:mtd2.setStatus(_A)
if mibBuilder.loadTexts:mtd2.setUnits(_C)
class _Mtd5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mtd5_Type.__name__=_B
_Mtd5_Object=MibScalar
mtd5=_Mtd5_Object((1,3,6,1,4,1,9839,2,1,1,7),_Mtd5_Type())
mtd5.setMaxAccess(_D)
if mibBuilder.loadTexts:mtd5.setStatus(_A)
if mibBuilder.loadTexts:mtd5.setUnits(_C)
class _Mtd6_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mtd6_Type.__name__=_B
_Mtd6_Object=MibScalar
mtd6=_Mtd6_Object((1,3,6,1,4,1,9839,2,1,1,8),_Mtd6_Type())
mtd6.setMaxAccess(_D)
if mibBuilder.loadTexts:mtd6.setStatus(_A)
if mibBuilder.loadTexts:mtd6.setUnits(_C)
class _Rele1_pwup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rele1_pwup_Type.__name__=_B
_Rele1_pwup_Object=MibScalar
rele1_pwup=_Rele1_pwup_Object((1,3,6,1,4,1,9839,2,1,1,9),_Rele1_pwup_Type())
rele1_pwup.setMaxAccess(_D)
if mibBuilder.loadTexts:rele1_pwup.setStatus(_A)
if mibBuilder.loadTexts:rele1_pwup.setUnits(_C)
class _Buzz_pwup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Buzz_pwup_Type.__name__=_B
_Buzz_pwup_Object=MibScalar
buzz_pwup=_Buzz_pwup_Object((1,3,6,1,4,1,9839,2,1,1,13),_Buzz_pwup_Type())
buzz_pwup.setMaxAccess(_D)
if mibBuilder.loadTexts:buzz_pwup.setStatus(_A)
if mibBuilder.loadTexts:buzz_pwup.setUnits(_C)
class _Di1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Di1_Type.__name__=_B
_Di1_Object=MibScalar
di1=_Di1_Object((1,3,6,1,4,1,9839,2,1,1,14),_Di1_Type())
di1.setMaxAccess(_E)
if mibBuilder.loadTexts:di1.setStatus(_A)
if mibBuilder.loadTexts:di1.setUnits(_C)
class _Di2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Di2_Type.__name__=_B
_Di2_Object=MibScalar
di2=_Di2_Object((1,3,6,1,4,1,9839,2,1,1,15),_Di2_Type())
di2.setMaxAccess(_E)
if mibBuilder.loadTexts:di2.setStatus(_A)
if mibBuilder.loadTexts:di2.setUnits(_C)
class _Di5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Di5_Type.__name__=_B
_Di5_Object=MibScalar
di5=_Di5_Object((1,3,6,1,4,1,9839,2,1,1,18),_Di5_Type())
di5.setMaxAccess(_E)
if mibBuilder.loadTexts:di5.setStatus(_A)
if mibBuilder.loadTexts:di5.setUnits(_C)
class _Di6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Di6_Type.__name__=_B
_Di6_Object=MibScalar
di6=_Di6_Object((1,3,6,1,4,1,9839,2,1,1,19),_Di6_Type())
di6.setMaxAccess(_E)
if mibBuilder.loadTexts:di6.setStatus(_A)
if mibBuilder.loadTexts:di6.setUnits(_C)
class _Ag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ag_Type.__name__=_B
_Ag_Object=MibScalar
ag=_Ag_Object((1,3,6,1,4,1,9839,2,1,1,20),_Ag_Type())
ag.setMaxAccess(_E)
if mibBuilder.loadTexts:ag.setStatus(_A)
if mibBuilder.loadTexts:ag.setUnits(_C)
class _At1h_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_At1h_Type.__name__=_B
_At1h_Object=MibScalar
at1h=_At1h_Object((1,3,6,1,4,1,9839,2,1,1,21),_At1h_Type())
at1h.setMaxAccess(_E)
if mibBuilder.loadTexts:at1h.setStatus(_A)
if mibBuilder.loadTexts:at1h.setUnits(_C)
class _At1l_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_At1l_Type.__name__=_B
_At1l_Object=MibScalar
at1l=_At1l_Object((1,3,6,1,4,1,9839,2,1,1,22),_At1l_Type())
at1l.setMaxAccess(_E)
if mibBuilder.loadTexts:at1l.setStatus(_A)
if mibBuilder.loadTexts:at1l.setUnits(_C)
class _At2h_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_At2h_Type.__name__=_B
_At2h_Object=MibScalar
at2h=_At2h_Object((1,3,6,1,4,1,9839,2,1,1,23),_At2h_Type())
at2h.setMaxAccess(_E)
if mibBuilder.loadTexts:at2h.setStatus(_A)
if mibBuilder.loadTexts:at2h.setUnits(_C)
class _At2l_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_At2l_Type.__name__=_B
_At2l_Object=MibScalar
at2l=_At2l_Object((1,3,6,1,4,1,9839,2,1,1,24),_At2l_Type())
at2l.setMaxAccess(_E)
if mibBuilder.loadTexts:at2l.setStatus(_A)
if mibBuilder.loadTexts:at2l.setUnits(_C)
class _At3h_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_At3h_Type.__name__=_B
_At3h_Object=MibScalar
at3h=_At3h_Object((1,3,6,1,4,1,9839,2,1,1,25),_At3h_Type())
at3h.setMaxAccess(_E)
if mibBuilder.loadTexts:at3h.setStatus(_A)
if mibBuilder.loadTexts:at3h.setUnits(_C)
class _At3l_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_At3l_Type.__name__=_B
_At3l_Object=MibScalar
at3l=_At3l_Object((1,3,6,1,4,1,9839,2,1,1,26),_At3l_Type())
at3l.setMaxAccess(_E)
if mibBuilder.loadTexts:at3l.setStatus(_A)
if mibBuilder.loadTexts:at3l.setUnits(_C)
class _At4h_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_At4h_Type.__name__=_B
_At4h_Object=MibScalar
at4h=_At4h_Object((1,3,6,1,4,1,9839,2,1,1,27),_At4h_Type())
at4h.setMaxAccess(_E)
if mibBuilder.loadTexts:at4h.setStatus(_A)
if mibBuilder.loadTexts:at4h.setUnits(_C)
class _At4l_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_At4l_Type.__name__=_B
_At4l_Object=MibScalar
at4l=_At4l_Object((1,3,6,1,4,1,9839,2,1,1,28),_At4l_Type())
at4l.setMaxAccess(_E)
if mibBuilder.loadTexts:at4l.setStatus(_A)
if mibBuilder.loadTexts:at4l.setUnits(_C)
class _Af1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Af1_Type.__name__=_B
_Af1_Object=MibScalar
af1=_Af1_Object((1,3,6,1,4,1,9839,2,1,1,29),_Af1_Type())
af1.setMaxAccess(_E)
if mibBuilder.loadTexts:af1.setStatus(_A)
if mibBuilder.loadTexts:af1.setUnits(_C)
class _Af2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Af2_Type.__name__=_B
_Af2_Object=MibScalar
af2=_Af2_Object((1,3,6,1,4,1,9839,2,1,1,30),_Af2_Type())
af2.setMaxAccess(_E)
if mibBuilder.loadTexts:af2.setStatus(_A)
if mibBuilder.loadTexts:af2.setUnits(_C)
class _Af5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Af5_Type.__name__=_B
_Af5_Object=MibScalar
af5=_Af5_Object((1,3,6,1,4,1,9839,2,1,1,33),_Af5_Type())
af5.setMaxAccess(_E)
if mibBuilder.loadTexts:af5.setStatus(_A)
if mibBuilder.loadTexts:af5.setUnits(_C)
class _Af6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Af6_Type.__name__=_B
_Af6_Object=MibScalar
af6=_Af6_Object((1,3,6,1,4,1,9839,2,1,1,34),_Af6_Type())
af6.setMaxAccess(_E)
if mibBuilder.loadTexts:af6.setStatus(_A)
if mibBuilder.loadTexts:af6.setUnits(_C)
class _As1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_As1_Type.__name__=_B
_As1_Object=MibScalar
as1=_As1_Object((1,3,6,1,4,1,9839,2,1,1,35),_As1_Type())
as1.setMaxAccess(_E)
if mibBuilder.loadTexts:as1.setStatus(_A)
if mibBuilder.loadTexts:as1.setUnits(_C)
class _As2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_As2_Type.__name__=_B
_As2_Object=MibScalar
as2=_As2_Object((1,3,6,1,4,1,9839,2,1,1,36),_As2_Type())
as2.setMaxAccess(_E)
if mibBuilder.loadTexts:as2.setStatus(_A)
if mibBuilder.loadTexts:as2.setUnits(_C)
class _As3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_As3_Type.__name__=_B
_As3_Object=MibScalar
as3=_As3_Object((1,3,6,1,4,1,9839,2,1,1,37),_As3_Type())
as3.setMaxAccess(_E)
if mibBuilder.loadTexts:as3.setStatus(_A)
if mibBuilder.loadTexts:as3.setUnits(_C)
class _As4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_As4_Type.__name__=_B
_As4_Object=MibScalar
as4=_As4_Object((1,3,6,1,4,1,9839,2,1,1,38),_As4_Type())
as4.setMaxAccess(_E)
if mibBuilder.loadTexts:as4.setStatus(_A)
if mibBuilder.loadTexts:as4.setUnits(_C)
class _Ahw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ahw_Type.__name__=_B
_Ahw_Object=MibScalar
ahw=_Ahw_Object((1,3,6,1,4,1,9839,2,1,1,39),_Ahw_Type())
ahw.setMaxAccess(_E)
if mibBuilder.loadTexts:ahw.setStatus(_A)
if mibBuilder.loadTexts:ahw.setUnits(_C)
class _Td1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Td1_Type.__name__=_B
_Td1_Object=MibScalar
td1=_Td1_Object((1,3,6,1,4,1,9839,2,1,1,40),_Td1_Type())
td1.setMaxAccess(_D)
if mibBuilder.loadTexts:td1.setStatus(_A)
if mibBuilder.loadTexts:td1.setUnits(_C)
class _Td2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Td2_Type.__name__=_B
_Td2_Object=MibScalar
td2=_Td2_Object((1,3,6,1,4,1,9839,2,1,1,41),_Td2_Type())
td2.setMaxAccess(_D)
if mibBuilder.loadTexts:td2.setStatus(_A)
if mibBuilder.loadTexts:td2.setUnits(_C)
class _Td5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Td5_Type.__name__=_B
_Td5_Object=MibScalar
td5=_Td5_Object((1,3,6,1,4,1,9839,2,1,1,44),_Td5_Type())
td5.setMaxAccess(_D)
if mibBuilder.loadTexts:td5.setStatus(_A)
if mibBuilder.loadTexts:td5.setUnits(_C)
class _Td6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Td6_Type.__name__=_B
_Td6_Object=MibScalar
td6=_Td6_Object((1,3,6,1,4,1,9839,2,1,1,45),_Td6_Type())
td6.setMaxAccess(_D)
if mibBuilder.loadTexts:td6.setStatus(_A)
if mibBuilder.loadTexts:td6.setUnits(_C)
class _Ct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Ct_Type.__name__=_B
_Ct_Object=MibScalar
ct=_Ct_Object((1,3,6,1,4,1,9839,2,1,1,46),_Ct_Type())
ct.setMaxAccess(_E)
if mibBuilder.loadTexts:ct.setStatus(_A)
if mibBuilder.loadTexts:ct.setUnits(_C)
class _Buzz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Buzz_Type.__name__=_B
_Buzz_Object=MibScalar
buzz=_Buzz_Object((1,3,6,1,4,1,9839,2,1,1,47),_Buzz_Type())
buzz.setMaxAccess(_E)
if mibBuilder.loadTexts:buzz.setStatus(_A)
if mibBuilder.loadTexts:buzz.setUnits(_C)
class _Rele1_stato_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rele1_stato_Type.__name__=_B
_Rele1_stato_Object=MibScalar
rele1_stato=_Rele1_stato_Object((1,3,6,1,4,1,9839,2,1,1,48),_Rele1_stato_Type())
rele1_stato.setMaxAccess(_E)
if mibBuilder.loadTexts:rele1_stato.setStatus(_A)
if mibBuilder.loadTexts:rele1_stato.setUnits(_C)
class _Buzz_output_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Buzz_output_Type.__name__=_B
_Buzz_output_Object=MibScalar
buzz_output=_Buzz_output_Object((1,3,6,1,4,1,9839,2,1,1,52),_Buzz_output_Type())
buzz_output.setMaxAccess(_D)
if mibBuilder.loadTexts:buzz_output.setStatus(_A)
if mibBuilder.loadTexts:buzz_output.setUnits(_C)
class _Rele1_output_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rele1_output_Type.__name__=_B
_Rele1_output_Object=MibScalar
rele1_output=_Rele1_output_Object((1,3,6,1,4,1,9839,2,1,1,53),_Rele1_output_Type())
rele1_output.setMaxAccess(_D)
if mibBuilder.loadTexts:rele1_output.setStatus(_A)
if mibBuilder.loadTexts:rele1_output.setUnits(_C)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _H1_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,10000))
_H1_Type.__name__=_B
_H1_Object=MibScalar
h1=_H1_Object((1,3,6,1,4,1,9839,2,1,2,1),_H1_Type())
h1.setMaxAccess(_D)
if mibBuilder.loadTexts:h1.setStatus(_A)
if mibBuilder.loadTexts:h1.setUnits(_F)
class _L1_Type(Integer32):defaultValue=-1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2000,32767))
_L1_Type.__name__=_B
_L1_Object=MibScalar
l1=_L1_Object((1,3,6,1,4,1,9839,2,1,2,2),_L1_Type())
l1.setMaxAccess(_D)
if mibBuilder.loadTexts:l1.setStatus(_A)
if mibBuilder.loadTexts:l1.setUnits(_F)
class _H2_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,10000))
_H2_Type.__name__=_B
_H2_Object=MibScalar
h2=_H2_Object((1,3,6,1,4,1,9839,2,1,2,3),_H2_Type())
h2.setMaxAccess(_D)
if mibBuilder.loadTexts:h2.setStatus(_A)
if mibBuilder.loadTexts:h2.setUnits(_F)
class _L2_Type(Integer32):defaultValue=-1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2000,32767))
_L2_Type.__name__=_B
_L2_Object=MibScalar
l2=_L2_Object((1,3,6,1,4,1,9839,2,1,2,4),_L2_Type())
l2.setMaxAccess(_D)
if mibBuilder.loadTexts:l2.setStatus(_A)
if mibBuilder.loadTexts:l2.setUnits(_F)
class _H3_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,10000))
_H3_Type.__name__=_B
_H3_Object=MibScalar
h3=_H3_Object((1,3,6,1,4,1,9839,2,1,2,5),_H3_Type())
h3.setMaxAccess(_D)
if mibBuilder.loadTexts:h3.setStatus(_A)
if mibBuilder.loadTexts:h3.setUnits(_F)
class _L3_Type(Integer32):defaultValue=-1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2000,32767))
_L3_Type.__name__=_B
_L3_Object=MibScalar
l3=_L3_Object((1,3,6,1,4,1,9839,2,1,2,6),_L3_Type())
l3.setMaxAccess(_D)
if mibBuilder.loadTexts:l3.setStatus(_A)
if mibBuilder.loadTexts:l3.setUnits(_F)
class _H4_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,10000))
_H4_Type.__name__=_B
_H4_Object=MibScalar
h4=_H4_Object((1,3,6,1,4,1,9839,2,1,2,7),_H4_Type())
h4.setMaxAccess(_D)
if mibBuilder.loadTexts:h4.setStatus(_A)
if mibBuilder.loadTexts:h4.setUnits(_F)
class _L4_Type(Integer32):defaultValue=-1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2000,32767))
_L4_Type.__name__=_B
_L4_Object=MibScalar
l4=_L4_Object((1,3,6,1,4,1,9839,2,1,2,8),_L4_Type())
l4.setMaxAccess(_D)
if mibBuilder.loadTexts:l4.setStatus(_A)
if mibBuilder.loadTexts:l4.setUnits(_F)
class _V3l_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2000,32767))
_V3l_Type.__name__=_B
_V3l_Object=MibScalar
v3l=_V3l_Object((1,3,6,1,4,1,9839,2,1,2,9),_V3l_Type())
v3l.setMaxAccess(_D)
if mibBuilder.loadTexts:v3l.setStatus(_A)
if mibBuilder.loadTexts:v3l.setUnits(_H)
class _V3h_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,10000))
_V3h_Type.__name__=_B
_V3h_Object=MibScalar
v3h=_V3h_Object((1,3,6,1,4,1,9839,2,1,2,10),_V3h_Type())
v3h.setMaxAccess(_D)
if mibBuilder.loadTexts:v3h.setStatus(_A)
if mibBuilder.loadTexts:v3h.setUnits(_H)
class _V4l_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2000,32767))
_V4l_Type.__name__=_B
_V4l_Object=MibScalar
v4l=_V4l_Object((1,3,6,1,4,1,9839,2,1,2,11),_V4l_Type())
v4l.setMaxAccess(_D)
if mibBuilder.loadTexts:v4l.setStatus(_A)
if mibBuilder.loadTexts:v4l.setUnits(_H)
class _V4h_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,10000))
_V4h_Type.__name__=_B
_V4h_Object=MibScalar
v4h=_V4h_Object((1,3,6,1,4,1,9839,2,1,2,12),_V4h_Type())
v4h.setMaxAccess(_D)
if mibBuilder.loadTexts:v4h.setStatus(_A)
if mibBuilder.loadTexts:v4h.setUnits(_H)
class _O1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_O1_Type.__name__=_B
_O1_Object=MibScalar
o1=_O1_Object((1,3,6,1,4,1,9839,2,1,2,13),_O1_Type())
o1.setMaxAccess(_D)
if mibBuilder.loadTexts:o1.setStatus(_A)
if mibBuilder.loadTexts:o1.setUnits(_F)
class _O2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_O2_Type.__name__=_B
_O2_Object=MibScalar
o2=_O2_Object((1,3,6,1,4,1,9839,2,1,2,14),_O2_Type())
o2.setMaxAccess(_D)
if mibBuilder.loadTexts:o2.setStatus(_A)
if mibBuilder.loadTexts:o2.setUnits(_F)
class _O3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_O3_Type.__name__=_B
_O3_Object=MibScalar
o3=_O3_Object((1,3,6,1,4,1,9839,2,1,2,15),_O3_Type())
o3.setMaxAccess(_D)
if mibBuilder.loadTexts:o3.setStatus(_A)
if mibBuilder.loadTexts:o3.setUnits(_F)
class _O4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_O4_Type.__name__=_B
_O4_Object=MibScalar
o4=_O4_Object((1,3,6,1,4,1,9839,2,1,2,16),_O4_Type())
o4.setMaxAccess(_D)
if mibBuilder.loadTexts:o4.setStatus(_A)
if mibBuilder.loadTexts:o4.setUnits(_F)
class _Ds1_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_Ds1_Type.__name__=_B
_Ds1_Object=MibScalar
ds1=_Ds1_Object((1,3,6,1,4,1,9839,2,1,2,17),_Ds1_Type())
ds1.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1.setStatus(_A)
if mibBuilder.loadTexts:ds1.setUnits(_F)
class _Ds2_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_Ds2_Type.__name__=_B
_Ds2_Object=MibScalar
ds2=_Ds2_Object((1,3,6,1,4,1,9839,2,1,2,18),_Ds2_Type())
ds2.setMaxAccess(_D)
if mibBuilder.loadTexts:ds2.setStatus(_A)
if mibBuilder.loadTexts:ds2.setUnits(_F)
class _Ds3_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_Ds3_Type.__name__=_B
_Ds3_Object=MibScalar
ds3=_Ds3_Object((1,3,6,1,4,1,9839,2,1,2,19),_Ds3_Type())
ds3.setMaxAccess(_D)
if mibBuilder.loadTexts:ds3.setStatus(_A)
if mibBuilder.loadTexts:ds3.setUnits(_F)
class _Ds4_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_Ds4_Type.__name__=_B
_Ds4_Object=MibScalar
ds4=_Ds4_Object((1,3,6,1,4,1,9839,2,1,2,20),_Ds4_Type())
ds4.setMaxAccess(_D)
if mibBuilder.loadTexts:ds4.setStatus(_A)
if mibBuilder.loadTexts:ds4.setUnits(_F)
class _S1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_S1_Type.__name__=_B
_S1_Object=MibScalar
s1=_S1_Object((1,3,6,1,4,1,9839,2,1,2,21),_S1_Type())
s1.setMaxAccess(_E)
if mibBuilder.loadTexts:s1.setStatus(_A)
if mibBuilder.loadTexts:s1.setUnits(_F)
class _S2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_S2_Type.__name__=_B
_S2_Object=MibScalar
s2=_S2_Object((1,3,6,1,4,1,9839,2,1,2,22),_S2_Type())
s2.setMaxAccess(_E)
if mibBuilder.loadTexts:s2.setStatus(_A)
if mibBuilder.loadTexts:s2.setUnits(_F)
class _S3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_S3_Type.__name__=_B
_S3_Object=MibScalar
s3=_S3_Object((1,3,6,1,4,1,9839,2,1,2,23),_S3_Type())
s3.setMaxAccess(_E)
if mibBuilder.loadTexts:s3.setStatus(_A)
if mibBuilder.loadTexts:s3.setUnits(_F)
class _S4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_S4_Type.__name__=_B
_S4_Object=MibScalar
s4=_S4_Object((1,3,6,1,4,1,9839,2,1,2,24),_S4_Type())
s4.setMaxAccess(_E)
if mibBuilder.loadTexts:s4.setStatus(_A)
if mibBuilder.loadTexts:s4.setUnits(_F)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Mod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Mod_Type.__name__=_B
_Mod_Object=MibScalar
mod=_Mod_Object((1,3,6,1,4,1,9839,2,1,3,1),_Mod_Type())
mod.setMaxAccess(_D)
if mibBuilder.loadTexts:mod.setStatus(_A)
if mibBuilder.loadTexts:mod.setUnits(_C)
class _Sonde_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Sonde_Type.__name__=_B
_Sonde_Object=MibScalar
sonde=_Sonde_Object((1,3,6,1,4,1,9839,2,1,3,2),_Sonde_Type())
sonde.setMaxAccess(_D)
if mibBuilder.loadTexts:sonde.setStatus(_A)
if mibBuilder.loadTexts:sonde.setUnits(_C)
class _A1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_A1_Type.__name__=_B
_A1_Object=MibScalar
a1=_A1_Object((1,3,6,1,4,1,9839,2,1,3,3),_A1_Type())
a1.setMaxAccess(_D)
if mibBuilder.loadTexts:a1.setStatus(_A)
if mibBuilder.loadTexts:a1.setUnits(_C)
class _A2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_A2_Type.__name__=_B
_A2_Object=MibScalar
a2=_A2_Object((1,3,6,1,4,1,9839,2,1,3,4),_A2_Type())
a2.setMaxAccess(_D)
if mibBuilder.loadTexts:a2.setStatus(_A)
if mibBuilder.loadTexts:a2.setUnits(_C)
class _A5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_A5_Type.__name__=_B
_A5_Object=MibScalar
a5=_A5_Object((1,3,6,1,4,1,9839,2,1,3,7),_A5_Type())
a5.setMaxAccess(_D)
if mibBuilder.loadTexts:a5.setStatus(_A)
if mibBuilder.loadTexts:a5.setUnits(_C)
class _A6_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_A6_Type.__name__=_B
_A6_Object=MibScalar
a6=_A6_Object((1,3,6,1,4,1,9839,2,1,3,8),_A6_Type())
a6.setMaxAccess(_D)
if mibBuilder.loadTexts:a6.setStatus(_A)
if mibBuilder.loadTexts:a6.setUnits(_C)
class _D1_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_D1_Type.__name__=_B
_D1_Object=MibScalar
d1=_D1_Object((1,3,6,1,4,1,9839,2,1,3,9),_D1_Type())
d1.setMaxAccess(_D)
if mibBuilder.loadTexts:d1.setStatus(_A)
if mibBuilder.loadTexts:d1.setUnits(_G)
class _D2_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_D2_Type.__name__=_B
_D2_Object=MibScalar
d2=_D2_Object((1,3,6,1,4,1,9839,2,1,3,10),_D2_Type())
d2.setMaxAccess(_D)
if mibBuilder.loadTexts:d2.setStatus(_A)
if mibBuilder.loadTexts:d2.setUnits(_G)
class _D5_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_D5_Type.__name__=_B
_D5_Object=MibScalar
d5=_D5_Object((1,3,6,1,4,1,9839,2,1,3,13),_D5_Type())
d5.setMaxAccess(_D)
if mibBuilder.loadTexts:d5.setStatus(_A)
if mibBuilder.loadTexts:d5.setUnits(_G)
class _D6_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_D6_Type.__name__=_B
_D6_Object=MibScalar
d6=_D6_Object((1,3,6,1,4,1,9839,2,1,3,14),_D6_Type())
d6.setMaxAccess(_D)
if mibBuilder.loadTexts:d6.setStatus(_A)
if mibBuilder.loadTexts:d6.setUnits(_G)
class _N1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_N1_Type.__name__=_B
_N1_Object=MibScalar
n1=_N1_Object((1,3,6,1,4,1,9839,2,1,3,15),_N1_Type())
n1.setMaxAccess(_D)
if mibBuilder.loadTexts:n1.setStatus(_A)
if mibBuilder.loadTexts:n1.setUnits(_C)
class _R1_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_R1_Type.__name__=_B
_R1_Object=MibScalar
r1=_R1_Object((1,3,6,1,4,1,9839,2,1,3,16),_R1_Type())
r1.setMaxAccess(_D)
if mibBuilder.loadTexts:r1.setStatus(_A)
if mibBuilder.loadTexts:r1.setUnits(_I)
class _F1_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_F1_Type.__name__=_B
_F1_Object=MibScalar
f1=_F1_Object((1,3,6,1,4,1,9839,2,1,3,17),_F1_Type())
f1.setMaxAccess(_D)
if mibBuilder.loadTexts:f1.setStatus(_A)
if mibBuilder.loadTexts:f1.setUnits(_C)
class _N2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_N2_Type.__name__=_B
_N2_Object=MibScalar
n2=_N2_Object((1,3,6,1,4,1,9839,2,1,3,18),_N2_Type())
n2.setMaxAccess(_D)
if mibBuilder.loadTexts:n2.setStatus(_A)
if mibBuilder.loadTexts:n2.setUnits(_C)
class _R2_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_R2_Type.__name__=_B
_R2_Object=MibScalar
r2=_R2_Object((1,3,6,1,4,1,9839,2,1,3,19),_R2_Type())
r2.setMaxAccess(_D)
if mibBuilder.loadTexts:r2.setStatus(_A)
if mibBuilder.loadTexts:r2.setUnits(_I)
class _F2_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_F2_Type.__name__=_B
_F2_Object=MibScalar
f2=_F2_Object((1,3,6,1,4,1,9839,2,1,3,20),_F2_Type())
f2.setMaxAccess(_D)
if mibBuilder.loadTexts:f2.setStatus(_A)
if mibBuilder.loadTexts:f2.setUnits(_C)
class _N3_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_N3_Type.__name__=_B
_N3_Object=MibScalar
n3=_N3_Object((1,3,6,1,4,1,9839,2,1,3,21),_N3_Type())
n3.setMaxAccess(_D)
if mibBuilder.loadTexts:n3.setStatus(_A)
if mibBuilder.loadTexts:n3.setUnits(_C)
class _R3_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_R3_Type.__name__=_B
_R3_Object=MibScalar
r3=_R3_Object((1,3,6,1,4,1,9839,2,1,3,22),_R3_Type())
r3.setMaxAccess(_D)
if mibBuilder.loadTexts:r3.setStatus(_A)
if mibBuilder.loadTexts:r3.setUnits(_I)
class _F3_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_F3_Type.__name__=_B
_F3_Object=MibScalar
f3=_F3_Object((1,3,6,1,4,1,9839,2,1,3,23),_F3_Type())
f3.setMaxAccess(_D)
if mibBuilder.loadTexts:f3.setStatus(_A)
if mibBuilder.loadTexts:f3.setUnits(_C)
class _N4_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_N4_Type.__name__=_B
_N4_Object=MibScalar
n4=_N4_Object((1,3,6,1,4,1,9839,2,1,3,24),_N4_Type())
n4.setMaxAccess(_D)
if mibBuilder.loadTexts:n4.setStatus(_A)
if mibBuilder.loadTexts:n4.setUnits(_C)
class _R4_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_R4_Type.__name__=_B
_R4_Object=MibScalar
r4=_R4_Object((1,3,6,1,4,1,9839,2,1,3,25),_R4_Type())
r4.setMaxAccess(_D)
if mibBuilder.loadTexts:r4.setStatus(_A)
if mibBuilder.loadTexts:r4.setUnits(_I)
class _F4_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_F4_Type.__name__=_B
_F4_Object=MibScalar
f4=_F4_Object((1,3,6,1,4,1,9839,2,1,3,26),_F4_Type())
f4.setMaxAccess(_D)
if mibBuilder.loadTexts:f4.setStatus(_A)
if mibBuilder.loadTexts:f4.setUnits(_C)
class _Out_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Out_Type.__name__=_B
_Out_Object=MibScalar
out=_Out_Object((1,3,6,1,4,1,9839,2,1,3,27),_Out_Type())
out.setMaxAccess(_D)
if mibBuilder.loadTexts:out.setStatus(_A)
if mibBuilder.loadTexts:out.setUnits(_C)
class _Mode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Mode_Type.__name__=_B
_Mode_Object=MibScalar
mode=_Mode_Object((1,3,6,1,4,1,9839,2,1,3,28),_Mode_Type())
mode.setMaxAccess(_D)
if mibBuilder.loadTexts:mode.setStatus(_A)
if mibBuilder.loadTexts:mode.setUnits(_C)
class _Link1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Link1_Type.__name__=_B
_Link1_Object=MibScalar
link1=_Link1_Object((1,3,6,1,4,1,9839,2,1,3,29),_Link1_Type())
link1.setMaxAccess(_D)
if mibBuilder.loadTexts:link1.setStatus(_A)
if mibBuilder.loadTexts:link1.setUnits(_C)
class _Link2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Link2_Type.__name__=_B
_Link2_Object=MibScalar
link2=_Link2_Object((1,3,6,1,4,1,9839,2,1,3,30),_Link2_Type())
link2.setMaxAccess(_D)
if mibBuilder.loadTexts:link2.setStatus(_A)
if mibBuilder.loadTexts:link2.setUnits(_C)
class _Outl1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Outl1_Type.__name__=_B
_Outl1_Object=MibScalar
outl1=_Outl1_Object((1,3,6,1,4,1,9839,2,1,3,31),_Outl1_Type())
outl1.setMaxAccess(_D)
if mibBuilder.loadTexts:outl1.setStatus(_A)
if mibBuilder.loadTexts:outl1.setUnits(_C)
class _Outl2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Outl2_Type.__name__=_B
_Outl2_Object=MibScalar
outl2=_Outl2_Object((1,3,6,1,4,1,9839,2,1,3,32),_Outl2_Type())
outl2.setMaxAccess(_D)
if mibBuilder.loadTexts:outl2.setStatus(_A)
if mibBuilder.loadTexts:outl2.setUnits(_C)
class _Priority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Priority_Type.__name__=_B
_Priority_Object=MibScalar
priority=_Priority_Object((1,3,6,1,4,1,9839,2,1,3,33),_Priority_Type())
priority.setMaxAccess(_D)
if mibBuilder.loadTexts:priority.setStatus(_A)
if mibBuilder.loadTexts:priority.setUnits(_C)
class _Alcomm_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_Alcomm_Type.__name__=_B
_Alcomm_Object=MibScalar
alcomm=_Alcomm_Object((1,3,6,1,4,1,9839,2,1,3,34),_Alcomm_Type())
alcomm.setMaxAccess(_D)
if mibBuilder.loadTexts:alcomm.setStatus(_A)
if mibBuilder.loadTexts:alcomm.setUnits(_C)
class _Dk1_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Dk1_Type.__name__=_B
_Dk1_Object=MibScalar
dk1=_Dk1_Object((1,3,6,1,4,1,9839,2,1,3,35),_Dk1_Type())
dk1.setMaxAccess(_D)
if mibBuilder.loadTexts:dk1.setStatus(_A)
if mibBuilder.loadTexts:dk1.setUnits(_G)
class _Dk2_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Dk2_Type.__name__=_B
_Dk2_Object=MibScalar
dk2=_Dk2_Object((1,3,6,1,4,1,9839,2,1,3,36),_Dk2_Type())
dk2.setMaxAccess(_D)
if mibBuilder.loadTexts:dk2.setStatus(_A)
if mibBuilder.loadTexts:dk2.setUnits(_G)
class _Dk5_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Dk5_Type.__name__=_B
_Dk5_Object=MibScalar
dk5=_Dk5_Object((1,3,6,1,4,1,9839,2,1,3,39),_Dk5_Type())
dk5.setMaxAccess(_D)
if mibBuilder.loadTexts:dk5.setStatus(_A)
if mibBuilder.loadTexts:dk5.setUnits(_G)
class _Dk6_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Dk6_Type.__name__=_B
_Dk6_Object=MibScalar
dk6=_Dk6_Object((1,3,6,1,4,1,9839,2,1,3,40),_Dk6_Type())
dk6.setMaxAccess(_D)
if mibBuilder.loadTexts:dk6.setStatus(_A)
if mibBuilder.loadTexts:dk6.setUnits(_G)
mibBuilder.exportSymbols('CAREL-mio-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'mioMIB':mioMIB,'digitalObjects':digitalObjects,'buz':buz,'cf':cf,'mtd1':mtd1,'mtd2':mtd2,'mtd5':mtd5,'mtd6':mtd6,'rele1_pwup':rele1_pwup,'buzz_pwup':buzz_pwup,'di1':di1,'di2':di2,'di5':di5,'di6':di6,'ag':ag,'at1h':at1h,'at1l':at1l,'at2h':at2h,'at2l':at2l,'at3h':at3h,'at3l':at3l,'at4h':at4h,'at4l':at4l,'af1':af1,'af2':af2,'af5':af5,'af6':af6,'as1':as1,'as2':as2,'as3':as3,'as4':as4,'ahw':ahw,'td1':td1,'td2':td2,'td5':td5,'td6':td6,'ct':ct,'buzz':buzz,'rele1_stato':rele1_stato,'buzz_output':buzz_output,'rele1_output':rele1_output,'analogObjects':analogObjects,'h1':h1,'l1':l1,'h2':h2,'l2':l2,'h3':h3,'l3':l3,'h4':h4,'l4':l4,'v3l':v3l,'v3h':v3h,'v4l':v4l,'v4h':v4h,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'ds1':ds1,'ds2':ds2,'ds3':ds3,'ds4':ds4,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'integerObjects':integerObjects,'mod':mod,'sonde':sonde,'a1':a1,'a2':a2,'a5':a5,'a6':a6,'d1':d1,'d2':d2,'d5':d5,'d6':d6,'n1':n1,'r1':r1,'f1':f1,'n2':n2,'r2':r2,'f2':f2,'n3':n3,'r3':r3,'f3':f3,'n4':n4,'r4':r4,'f4':f4,'out':out,'mode':mode,'link1':link1,'link2':link2,'outl1':outl1,'outl2':outl2,'priority':priority,'alcomm':alcomm,'dk1':dk1,'dk2':dk2,'dk5':dk5,'dk6':dk6})