_G='sec'
_F='bar x10'
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
fcpMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
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
class _Scheda_modem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Scheda_modem_Type.__name__=_B
_Scheda_modem_Object=MibScalar
scheda_modem=_Scheda_modem_Object((1,3,6,1,4,1,9839,2,1,1,1),_Scheda_modem_Type())
scheda_modem.setMaxAccess(_D)
if mibBuilder.loadTexts:scheda_modem.setStatus(_A)
if mibBuilder.loadTexts:scheda_modem.setUnits(_C)
class _Present_expansion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Present_expansion_Type.__name__=_B
_Present_expansion_Object=MibScalar
present_expansion=_Present_expansion_Object((1,3,6,1,4,1,9839,2,1,1,2),_Present_expansion_Type())
present_expansion.setMaxAccess(_D)
if mibBuilder.loadTexts:present_expansion.setStatus(_A)
if mibBuilder.loadTexts:present_expansion.setUnits(_C)
class _Fan1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan1_Type.__name__=_B
_Fan1_Object=MibScalar
fan1=_Fan1_Object((1,3,6,1,4,1,9839,2,1,1,3),_Fan1_Type())
fan1.setMaxAccess(_D)
if mibBuilder.loadTexts:fan1.setStatus(_A)
if mibBuilder.loadTexts:fan1.setUnits(_C)
class _Fan2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan2_Type.__name__=_B
_Fan2_Object=MibScalar
fan2=_Fan2_Object((1,3,6,1,4,1,9839,2,1,1,4),_Fan2_Type())
fan2.setMaxAccess(_D)
if mibBuilder.loadTexts:fan2.setStatus(_A)
if mibBuilder.loadTexts:fan2.setUnits(_C)
class _Fan3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan3_Type.__name__=_B
_Fan3_Object=MibScalar
fan3=_Fan3_Object((1,3,6,1,4,1,9839,2,1,1,5),_Fan3_Type())
fan3.setMaxAccess(_D)
if mibBuilder.loadTexts:fan3.setStatus(_A)
if mibBuilder.loadTexts:fan3.setUnits(_C)
class _Fan4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan4_Type.__name__=_B
_Fan4_Object=MibScalar
fan4=_Fan4_Object((1,3,6,1,4,1,9839,2,1,1,6),_Fan4_Type())
fan4.setMaxAccess(_D)
if mibBuilder.loadTexts:fan4.setStatus(_A)
if mibBuilder.loadTexts:fan4.setUnits(_C)
class _Comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Comp1_Type.__name__=_B
_Comp1_Object=MibScalar
comp1=_Comp1_Object((1,3,6,1,4,1,9839,2,1,1,7),_Comp1_Type())
comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:comp1.setStatus(_A)
if mibBuilder.loadTexts:comp1.setUnits(_C)
class _Rich_parz11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz11_Type.__name__=_B
_Rich_parz11_Object=MibScalar
rich_parz11=_Rich_parz11_Object((1,3,6,1,4,1,9839,2,1,1,8),_Rich_parz11_Type())
rich_parz11.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz11.setStatus(_A)
if mibBuilder.loadTexts:rich_parz11.setUnits(_C)
class _Rich_parz21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz21_Type.__name__=_B
_Rich_parz21_Object=MibScalar
rich_parz21=_Rich_parz21_Object((1,3,6,1,4,1,9839,2,1,1,9),_Rich_parz21_Type())
rich_parz21.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz21.setStatus(_A)
if mibBuilder.loadTexts:rich_parz21.setUnits(_C)
class _Comp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Comp2_Type.__name__=_B
_Comp2_Object=MibScalar
comp2=_Comp2_Object((1,3,6,1,4,1,9839,2,1,1,10),_Comp2_Type())
comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:comp2.setStatus(_A)
if mibBuilder.loadTexts:comp2.setUnits(_C)
class _Rich_parz12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz12_Type.__name__=_B
_Rich_parz12_Object=MibScalar
rich_parz12=_Rich_parz12_Object((1,3,6,1,4,1,9839,2,1,1,11),_Rich_parz12_Type())
rich_parz12.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz12.setStatus(_A)
if mibBuilder.loadTexts:rich_parz12.setUnits(_C)
class _Rich_parz22_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz22_Type.__name__=_B
_Rich_parz22_Object=MibScalar
rich_parz22=_Rich_parz22_Object((1,3,6,1,4,1,9839,2,1,1,12),_Rich_parz22_Type())
rich_parz22.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz22.setStatus(_A)
if mibBuilder.loadTexts:rich_parz22.setUnits(_C)
class _Comp3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Comp3_Type.__name__=_B
_Comp3_Object=MibScalar
comp3=_Comp3_Object((1,3,6,1,4,1,9839,2,1,1,13),_Comp3_Type())
comp3.setMaxAccess(_D)
if mibBuilder.loadTexts:comp3.setStatus(_A)
if mibBuilder.loadTexts:comp3.setUnits(_C)
class _Rich_parz13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz13_Type.__name__=_B
_Rich_parz13_Object=MibScalar
rich_parz13=_Rich_parz13_Object((1,3,6,1,4,1,9839,2,1,1,14),_Rich_parz13_Type())
rich_parz13.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz13.setStatus(_A)
if mibBuilder.loadTexts:rich_parz13.setUnits(_C)
class _Rich_parz23_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz23_Type.__name__=_B
_Rich_parz23_Object=MibScalar
rich_parz23=_Rich_parz23_Object((1,3,6,1,4,1,9839,2,1,1,15),_Rich_parz23_Type())
rich_parz23.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz23.setStatus(_A)
if mibBuilder.loadTexts:rich_parz23.setUnits(_C)
class _Comp4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Comp4_Type.__name__=_B
_Comp4_Object=MibScalar
comp4=_Comp4_Object((1,3,6,1,4,1,9839,2,1,1,16),_Comp4_Type())
comp4.setMaxAccess(_D)
if mibBuilder.loadTexts:comp4.setStatus(_A)
if mibBuilder.loadTexts:comp4.setUnits(_C)
class _Rich_parz14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz14_Type.__name__=_B
_Rich_parz14_Object=MibScalar
rich_parz14=_Rich_parz14_Object((1,3,6,1,4,1,9839,2,1,1,17),_Rich_parz14_Type())
rich_parz14.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz14.setStatus(_A)
if mibBuilder.loadTexts:rich_parz14.setUnits(_C)
class _Rich_parz24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz24_Type.__name__=_B
_Rich_parz24_Object=MibScalar
rich_parz24=_Rich_parz24_Object((1,3,6,1,4,1,9839,2,1,1,18),_Rich_parz24_Type())
rich_parz24.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz24.setStatus(_A)
if mibBuilder.loadTexts:rich_parz24.setUnits(_C)
class _Comp5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Comp5_Type.__name__=_B
_Comp5_Object=MibScalar
comp5=_Comp5_Object((1,3,6,1,4,1,9839,2,1,1,19),_Comp5_Type())
comp5.setMaxAccess(_D)
if mibBuilder.loadTexts:comp5.setStatus(_A)
if mibBuilder.loadTexts:comp5.setUnits(_C)
class _Rich_parz15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz15_Type.__name__=_B
_Rich_parz15_Object=MibScalar
rich_parz15=_Rich_parz15_Object((1,3,6,1,4,1,9839,2,1,1,20),_Rich_parz15_Type())
rich_parz15.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz15.setStatus(_A)
if mibBuilder.loadTexts:rich_parz15.setUnits(_C)
class _Rich_parz25_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz25_Type.__name__=_B
_Rich_parz25_Object=MibScalar
rich_parz25=_Rich_parz25_Object((1,3,6,1,4,1,9839,2,1,1,21),_Rich_parz25_Type())
rich_parz25.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz25.setStatus(_A)
if mibBuilder.loadTexts:rich_parz25.setUnits(_C)
class _Comp6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Comp6_Type.__name__=_B
_Comp6_Object=MibScalar
comp6=_Comp6_Object((1,3,6,1,4,1,9839,2,1,1,22),_Comp6_Type())
comp6.setMaxAccess(_D)
if mibBuilder.loadTexts:comp6.setStatus(_A)
if mibBuilder.loadTexts:comp6.setUnits(_C)
class _Rich_parz16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz16_Type.__name__=_B
_Rich_parz16_Object=MibScalar
rich_parz16=_Rich_parz16_Object((1,3,6,1,4,1,9839,2,1,1,23),_Rich_parz16_Type())
rich_parz16.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz16.setStatus(_A)
if mibBuilder.loadTexts:rich_parz16.setUnits(_C)
class _Rich_parz26_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Rich_parz26_Type.__name__=_B
_Rich_parz26_Object=MibScalar
rich_parz26=_Rich_parz26_Object((1,3,6,1,4,1,9839,2,1,1,24),_Rich_parz26_Type())
rich_parz26.setMaxAccess(_D)
if mibBuilder.loadTexts:rich_parz26.setStatus(_A)
if mibBuilder.loadTexts:rich_parz26.setUnits(_C)
class _Din1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din1_Type.__name__=_B
_Din1_Object=MibScalar
din1=_Din1_Object((1,3,6,1,4,1,9839,2,1,1,25),_Din1_Type())
din1.setMaxAccess(_D)
if mibBuilder.loadTexts:din1.setStatus(_A)
if mibBuilder.loadTexts:din1.setUnits(_C)
class _Din2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din2_Type.__name__=_B
_Din2_Object=MibScalar
din2=_Din2_Object((1,3,6,1,4,1,9839,2,1,1,26),_Din2_Type())
din2.setMaxAccess(_D)
if mibBuilder.loadTexts:din2.setStatus(_A)
if mibBuilder.loadTexts:din2.setUnits(_C)
class _Din3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din3_Type.__name__=_B
_Din3_Object=MibScalar
din3=_Din3_Object((1,3,6,1,4,1,9839,2,1,1,27),_Din3_Type())
din3.setMaxAccess(_D)
if mibBuilder.loadTexts:din3.setStatus(_A)
if mibBuilder.loadTexts:din3.setUnits(_C)
class _Din4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din4_Type.__name__=_B
_Din4_Object=MibScalar
din4=_Din4_Object((1,3,6,1,4,1,9839,2,1,1,28),_Din4_Type())
din4.setMaxAccess(_D)
if mibBuilder.loadTexts:din4.setStatus(_A)
if mibBuilder.loadTexts:din4.setUnits(_C)
class _Din5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din5_Type.__name__=_B
_Din5_Object=MibScalar
din5=_Din5_Object((1,3,6,1,4,1,9839,2,1,1,29),_Din5_Type())
din5.setMaxAccess(_D)
if mibBuilder.loadTexts:din5.setStatus(_A)
if mibBuilder.loadTexts:din5.setUnits(_C)
class _Din6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din6_Type.__name__=_B
_Din6_Object=MibScalar
din6=_Din6_Object((1,3,6,1,4,1,9839,2,1,1,30),_Din6_Type())
din6.setMaxAccess(_D)
if mibBuilder.loadTexts:din6.setStatus(_A)
if mibBuilder.loadTexts:din6.setUnits(_C)
class _Din7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din7_Type.__name__=_B
_Din7_Object=MibScalar
din7=_Din7_Object((1,3,6,1,4,1,9839,2,1,1,31),_Din7_Type())
din7.setMaxAccess(_D)
if mibBuilder.loadTexts:din7.setStatus(_A)
if mibBuilder.loadTexts:din7.setUnits(_C)
class _Din8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din8_Type.__name__=_B
_Din8_Object=MibScalar
din8=_Din8_Object((1,3,6,1,4,1,9839,2,1,1,32),_Din8_Type())
din8.setMaxAccess(_D)
if mibBuilder.loadTexts:din8.setStatus(_A)
if mibBuilder.loadTexts:din8.setUnits(_C)
class _Din9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din9_Type.__name__=_B
_Din9_Object=MibScalar
din9=_Din9_Object((1,3,6,1,4,1,9839,2,1,1,33),_Din9_Type())
din9.setMaxAccess(_D)
if mibBuilder.loadTexts:din9.setStatus(_A)
if mibBuilder.loadTexts:din9.setUnits(_C)
class _Din10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din10_Type.__name__=_B
_Din10_Object=MibScalar
din10=_Din10_Object((1,3,6,1,4,1,9839,2,1,1,34),_Din10_Type())
din10.setMaxAccess(_D)
if mibBuilder.loadTexts:din10.setStatus(_A)
if mibBuilder.loadTexts:din10.setUnits(_C)
class _Din11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din11_Type.__name__=_B
_Din11_Object=MibScalar
din11=_Din11_Object((1,3,6,1,4,1,9839,2,1,1,35),_Din11_Type())
din11.setMaxAccess(_D)
if mibBuilder.loadTexts:din11.setStatus(_A)
if mibBuilder.loadTexts:din11.setUnits(_C)
class _Din12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din12_Type.__name__=_B
_Din12_Object=MibScalar
din12=_Din12_Object((1,3,6,1,4,1,9839,2,1,1,36),_Din12_Type())
din12.setMaxAccess(_D)
if mibBuilder.loadTexts:din12.setStatus(_A)
if mibBuilder.loadTexts:din12.setUnits(_C)
class _Din13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din13_Type.__name__=_B
_Din13_Object=MibScalar
din13=_Din13_Object((1,3,6,1,4,1,9839,2,1,1,37),_Din13_Type())
din13.setMaxAccess(_D)
if mibBuilder.loadTexts:din13.setStatus(_A)
if mibBuilder.loadTexts:din13.setUnits(_C)
class _Din14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din14_Type.__name__=_B
_Din14_Object=MibScalar
din14=_Din14_Object((1,3,6,1,4,1,9839,2,1,1,38),_Din14_Type())
din14.setMaxAccess(_D)
if mibBuilder.loadTexts:din14.setStatus(_A)
if mibBuilder.loadTexts:din14.setUnits(_C)
class _Din15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din15_Type.__name__=_B
_Din15_Object=MibScalar
din15=_Din15_Object((1,3,6,1,4,1,9839,2,1,1,39),_Din15_Type())
din15.setMaxAccess(_D)
if mibBuilder.loadTexts:din15.setStatus(_A)
if mibBuilder.loadTexts:din15.setUnits(_C)
class _Din16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din16_Type.__name__=_B
_Din16_Object=MibScalar
din16=_Din16_Object((1,3,6,1,4,1,9839,2,1,1,40),_Din16_Type())
din16.setMaxAccess(_D)
if mibBuilder.loadTexts:din16.setStatus(_A)
if mibBuilder.loadTexts:din16.setUnits(_C)
class _Din17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din17_Type.__name__=_B
_Din17_Object=MibScalar
din17=_Din17_Object((1,3,6,1,4,1,9839,2,1,1,41),_Din17_Type())
din17.setMaxAccess(_D)
if mibBuilder.loadTexts:din17.setStatus(_A)
if mibBuilder.loadTexts:din17.setUnits(_C)
class _Din18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din18_Type.__name__=_B
_Din18_Object=MibScalar
din18=_Din18_Object((1,3,6,1,4,1,9839,2,1,1,42),_Din18_Type())
din18.setMaxAccess(_D)
if mibBuilder.loadTexts:din18.setStatus(_A)
if mibBuilder.loadTexts:din18.setUnits(_C)
class _All_pres_lpres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_pres_lpres_Type.__name__=_B
_All_pres_lpres_Object=MibScalar
all_pres_lpres=_All_pres_lpres_Object((1,3,6,1,4,1,9839,2,1,1,43),_All_pres_lpres_Type())
all_pres_lpres.setMaxAccess(_D)
if mibBuilder.loadTexts:all_pres_lpres.setStatus(_A)
if mibBuilder.loadTexts:all_pres_lpres.setUnits(_C)
class _All_pres_hpres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_All_pres_hpres_Type.__name__=_B
_All_pres_hpres_Object=MibScalar
all_pres_hpres=_All_pres_hpres_Object((1,3,6,1,4,1,9839,2,1,1,44),_All_pres_hpres_Type())
all_pres_hpres.setMaxAccess(_D)
if mibBuilder.loadTexts:all_pres_hpres.setStatus(_A)
if mibBuilder.loadTexts:all_pres_hpres.setUnits(_C)
class _Din101_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din101_Type.__name__=_B
_Din101_Object=MibScalar
din101=_Din101_Object((1,3,6,1,4,1,9839,2,1,1,45),_Din101_Type())
din101.setMaxAccess(_D)
if mibBuilder.loadTexts:din101.setStatus(_A)
if mibBuilder.loadTexts:din101.setUnits(_C)
class _Din102_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din102_Type.__name__=_B
_Din102_Object=MibScalar
din102=_Din102_Object((1,3,6,1,4,1,9839,2,1,1,46),_Din102_Type())
din102.setMaxAccess(_D)
if mibBuilder.loadTexts:din102.setStatus(_A)
if mibBuilder.loadTexts:din102.setUnits(_C)
class _Din103_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din103_Type.__name__=_B
_Din103_Object=MibScalar
din103=_Din103_Object((1,3,6,1,4,1,9839,2,1,1,47),_Din103_Type())
din103.setMaxAccess(_D)
if mibBuilder.loadTexts:din103.setStatus(_A)
if mibBuilder.loadTexts:din103.setUnits(_C)
class _Din104_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din104_Type.__name__=_B
_Din104_Object=MibScalar
din104=_Din104_Object((1,3,6,1,4,1,9839,2,1,1,48),_Din104_Type())
din104.setMaxAccess(_D)
if mibBuilder.loadTexts:din104.setStatus(_A)
if mibBuilder.loadTexts:din104.setUnits(_C)
class _Din105_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din105_Type.__name__=_B
_Din105_Object=MibScalar
din105=_Din105_Object((1,3,6,1,4,1,9839,2,1,1,49),_Din105_Type())
din105.setMaxAccess(_D)
if mibBuilder.loadTexts:din105.setStatus(_A)
if mibBuilder.loadTexts:din105.setUnits(_C)
class _Din106_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din106_Type.__name__=_B
_Din106_Object=MibScalar
din106=_Din106_Object((1,3,6,1,4,1,9839,2,1,1,50),_Din106_Type())
din106.setMaxAccess(_D)
if mibBuilder.loadTexts:din106.setStatus(_A)
if mibBuilder.loadTexts:din106.setUnits(_C)
class _Din107_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din107_Type.__name__=_B
_Din107_Object=MibScalar
din107=_Din107_Object((1,3,6,1,4,1,9839,2,1,1,51),_Din107_Type())
din107.setMaxAccess(_D)
if mibBuilder.loadTexts:din107.setStatus(_A)
if mibBuilder.loadTexts:din107.setUnits(_C)
class _Din108_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Din108_Type.__name__=_B
_Din108_Object=MibScalar
din108=_Din108_Object((1,3,6,1,4,1,9839,2,1,1,52),_Din108_Type())
din108.setMaxAccess(_D)
if mibBuilder.loadTexts:din108.setStatus(_A)
if mibBuilder.loadTexts:din108.setUnits(_C)
class _Mall_term_klix1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_klix1_Type.__name__=_B
_Mall_term_klix1_Object=MibScalar
mall_term_klix1=_Mall_term_klix1_Object((1,3,6,1,4,1,9839,2,1,1,53),_Mall_term_klix1_Type())
mall_term_klix1.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_klix1.setStatus(_A)
if mibBuilder.loadTexts:mall_term_klix1.setUnits(_C)
class _Mall_term_klix2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_klix2_Type.__name__=_B
_Mall_term_klix2_Object=MibScalar
mall_term_klix2=_Mall_term_klix2_Object((1,3,6,1,4,1,9839,2,1,1,54),_Mall_term_klix2_Type())
mall_term_klix2.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_klix2.setStatus(_A)
if mibBuilder.loadTexts:mall_term_klix2.setUnits(_C)
class _Mall_term_klix3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_klix3_Type.__name__=_B
_Mall_term_klix3_Object=MibScalar
mall_term_klix3=_Mall_term_klix3_Object((1,3,6,1,4,1,9839,2,1,1,55),_Mall_term_klix3_Type())
mall_term_klix3.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_klix3.setStatus(_A)
if mibBuilder.loadTexts:mall_term_klix3.setUnits(_C)
class _Mall_term_klix4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_klix4_Type.__name__=_B
_Mall_term_klix4_Object=MibScalar
mall_term_klix4=_Mall_term_klix4_Object((1,3,6,1,4,1,9839,2,1,1,56),_Mall_term_klix4_Type())
mall_term_klix4.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_klix4.setStatus(_A)
if mibBuilder.loadTexts:mall_term_klix4.setUnits(_C)
class _Mall_term_klix5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_klix5_Type.__name__=_B
_Mall_term_klix5_Object=MibScalar
mall_term_klix5=_Mall_term_klix5_Object((1,3,6,1,4,1,9839,2,1,1,57),_Mall_term_klix5_Type())
mall_term_klix5.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_klix5.setStatus(_A)
if mibBuilder.loadTexts:mall_term_klix5.setUnits(_C)
class _Mall_term_klix6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_klix6_Type.__name__=_B
_Mall_term_klix6_Object=MibScalar
mall_term_klix6=_Mall_term_klix6_Object((1,3,6,1,4,1,9839,2,1,1,58),_Mall_term_klix6_Type())
mall_term_klix6.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_klix6.setStatus(_A)
if mibBuilder.loadTexts:mall_term_klix6.setUnits(_C)
class _Mall_pres_h1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_pres_h1_Type.__name__=_B
_Mall_pres_h1_Object=MibScalar
mall_pres_h1=_Mall_pres_h1_Object((1,3,6,1,4,1,9839,2,1,1,59),_Mall_pres_h1_Type())
mall_pres_h1.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_pres_h1.setStatus(_A)
if mibBuilder.loadTexts:mall_pres_h1.setUnits(_C)
class _Mall_pres_h2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_pres_h2_Type.__name__=_B
_Mall_pres_h2_Object=MibScalar
mall_pres_h2=_Mall_pres_h2_Object((1,3,6,1,4,1,9839,2,1,1,60),_Mall_pres_h2_Type())
mall_pres_h2.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_pres_h2.setStatus(_A)
if mibBuilder.loadTexts:mall_pres_h2.setUnits(_C)
class _Mall_pres_h3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_pres_h3_Type.__name__=_B
_Mall_pres_h3_Object=MibScalar
mall_pres_h3=_Mall_pres_h3_Object((1,3,6,1,4,1,9839,2,1,1,61),_Mall_pres_h3_Type())
mall_pres_h3.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_pres_h3.setStatus(_A)
if mibBuilder.loadTexts:mall_pres_h3.setUnits(_C)
class _Mall_pres_h4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_pres_h4_Type.__name__=_B
_Mall_pres_h4_Object=MibScalar
mall_pres_h4=_Mall_pres_h4_Object((1,3,6,1,4,1,9839,2,1,1,62),_Mall_pres_h4_Type())
mall_pres_h4.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_pres_h4.setStatus(_A)
if mibBuilder.loadTexts:mall_pres_h4.setUnits(_C)
class _Mall_pres_h5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_pres_h5_Type.__name__=_B
_Mall_pres_h5_Object=MibScalar
mall_pres_h5=_Mall_pres_h5_Object((1,3,6,1,4,1,9839,2,1,1,63),_Mall_pres_h5_Type())
mall_pres_h5.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_pres_h5.setStatus(_A)
if mibBuilder.loadTexts:mall_pres_h5.setUnits(_C)
class _Mall_pres_h6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_pres_h6_Type.__name__=_B
_Mall_pres_h6_Object=MibScalar
mall_pres_h6=_Mall_pres_h6_Object((1,3,6,1,4,1,9839,2,1,1,64),_Mall_pres_h6_Type())
mall_pres_h6.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_pres_h6.setStatus(_A)
if mibBuilder.loadTexts:mall_pres_h6.setUnits(_C)
class _Mall_dif_olio1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_dif_olio1_Type.__name__=_B
_Mall_dif_olio1_Object=MibScalar
mall_dif_olio1=_Mall_dif_olio1_Object((1,3,6,1,4,1,9839,2,1,1,65),_Mall_dif_olio1_Type())
mall_dif_olio1.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_dif_olio1.setStatus(_A)
if mibBuilder.loadTexts:mall_dif_olio1.setUnits(_C)
class _Mall_dif_olio2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_dif_olio2_Type.__name__=_B
_Mall_dif_olio2_Object=MibScalar
mall_dif_olio2=_Mall_dif_olio2_Object((1,3,6,1,4,1,9839,2,1,1,66),_Mall_dif_olio2_Type())
mall_dif_olio2.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_dif_olio2.setStatus(_A)
if mibBuilder.loadTexts:mall_dif_olio2.setUnits(_C)
class _Mall_dif_olio3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_dif_olio3_Type.__name__=_B
_Mall_dif_olio3_Object=MibScalar
mall_dif_olio3=_Mall_dif_olio3_Object((1,3,6,1,4,1,9839,2,1,1,67),_Mall_dif_olio3_Type())
mall_dif_olio3.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_dif_olio3.setStatus(_A)
if mibBuilder.loadTexts:mall_dif_olio3.setUnits(_C)
class _Mall_dif_olio4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_dif_olio4_Type.__name__=_B
_Mall_dif_olio4_Object=MibScalar
mall_dif_olio4=_Mall_dif_olio4_Object((1,3,6,1,4,1,9839,2,1,1,68),_Mall_dif_olio4_Type())
mall_dif_olio4.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_dif_olio4.setStatus(_A)
if mibBuilder.loadTexts:mall_dif_olio4.setUnits(_C)
class _Mall_dif_olio5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_dif_olio5_Type.__name__=_B
_Mall_dif_olio5_Object=MibScalar
mall_dif_olio5=_Mall_dif_olio5_Object((1,3,6,1,4,1,9839,2,1,1,69),_Mall_dif_olio5_Type())
mall_dif_olio5.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_dif_olio5.setStatus(_A)
if mibBuilder.loadTexts:mall_dif_olio5.setUnits(_C)
class _Mall_dif_olio6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_dif_olio6_Type.__name__=_B
_Mall_dif_olio6_Object=MibScalar
mall_dif_olio6=_Mall_dif_olio6_Object((1,3,6,1,4,1,9839,2,1,1,70),_Mall_dif_olio6_Type())
mall_dif_olio6.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_dif_olio6.setStatus(_A)
if mibBuilder.loadTexts:mall_dif_olio6.setUnits(_C)
class _Mall_ore_comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_ore_comp1_Type.__name__=_B
_Mall_ore_comp1_Object=MibScalar
mall_ore_comp1=_Mall_ore_comp1_Object((1,3,6,1,4,1,9839,2,1,1,71),_Mall_ore_comp1_Type())
mall_ore_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_ore_comp1.setStatus(_A)
if mibBuilder.loadTexts:mall_ore_comp1.setUnits(_C)
class _Mall_ore_comp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_ore_comp2_Type.__name__=_B
_Mall_ore_comp2_Object=MibScalar
mall_ore_comp2=_Mall_ore_comp2_Object((1,3,6,1,4,1,9839,2,1,1,72),_Mall_ore_comp2_Type())
mall_ore_comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_ore_comp2.setStatus(_A)
if mibBuilder.loadTexts:mall_ore_comp2.setUnits(_C)
class _Mall_ore_comp3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_ore_comp3_Type.__name__=_B
_Mall_ore_comp3_Object=MibScalar
mall_ore_comp3=_Mall_ore_comp3_Object((1,3,6,1,4,1,9839,2,1,1,73),_Mall_ore_comp3_Type())
mall_ore_comp3.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_ore_comp3.setStatus(_A)
if mibBuilder.loadTexts:mall_ore_comp3.setUnits(_C)
class _Mall_ore_comp4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_ore_comp4_Type.__name__=_B
_Mall_ore_comp4_Object=MibScalar
mall_ore_comp4=_Mall_ore_comp4_Object((1,3,6,1,4,1,9839,2,1,1,74),_Mall_ore_comp4_Type())
mall_ore_comp4.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_ore_comp4.setStatus(_A)
if mibBuilder.loadTexts:mall_ore_comp4.setUnits(_C)
class _Mall_ore_comp5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_ore_comp5_Type.__name__=_B
_Mall_ore_comp5_Object=MibScalar
mall_ore_comp5=_Mall_ore_comp5_Object((1,3,6,1,4,1,9839,2,1,1,75),_Mall_ore_comp5_Type())
mall_ore_comp5.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_ore_comp5.setStatus(_A)
if mibBuilder.loadTexts:mall_ore_comp5.setUnits(_C)
class _Mall_ore_comp6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_ore_comp6_Type.__name__=_B
_Mall_ore_comp6_Object=MibScalar
mall_ore_comp6=_Mall_ore_comp6_Object((1,3,6,1,4,1,9839,2,1,1,76),_Mall_ore_comp6_Type())
mall_ore_comp6.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_ore_comp6.setStatus(_A)
if mibBuilder.loadTexts:mall_ore_comp6.setUnits(_C)
class _Mall_term_vent1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_vent1_Type.__name__=_B
_Mall_term_vent1_Object=MibScalar
mall_term_vent1=_Mall_term_vent1_Object((1,3,6,1,4,1,9839,2,1,1,77),_Mall_term_vent1_Type())
mall_term_vent1.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_vent1.setStatus(_A)
if mibBuilder.loadTexts:mall_term_vent1.setUnits(_C)
class _Mall_term_vent2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_vent2_Type.__name__=_B
_Mall_term_vent2_Object=MibScalar
mall_term_vent2=_Mall_term_vent2_Object((1,3,6,1,4,1,9839,2,1,1,78),_Mall_term_vent2_Type())
mall_term_vent2.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_vent2.setStatus(_A)
if mibBuilder.loadTexts:mall_term_vent2.setUnits(_C)
class _Mall_term_vent3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_vent3_Type.__name__=_B
_Mall_term_vent3_Object=MibScalar
mall_term_vent3=_Mall_term_vent3_Object((1,3,6,1,4,1,9839,2,1,1,79),_Mall_term_vent3_Type())
mall_term_vent3.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_vent3.setStatus(_A)
if mibBuilder.loadTexts:mall_term_vent3.setUnits(_C)
class _Mall_term_vent4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_vent4_Type.__name__=_B
_Mall_term_vent4_Object=MibScalar
mall_term_vent4=_Mall_term_vent4_Object((1,3,6,1,4,1,9839,2,1,1,80),_Mall_term_vent4_Type())
mall_term_vent4.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_vent4.setStatus(_A)
if mibBuilder.loadTexts:mall_term_vent4.setUnits(_C)
class _Mal_liquid_level_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_liquid_level_Type.__name__=_B
_Mal_liquid_level_Object=MibScalar
mal_liquid_level=_Mal_liquid_level_Object((1,3,6,1,4,1,9839,2,1,1,81),_Mal_liquid_level_Type())
mal_liquid_level.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_liquid_level.setStatus(_A)
if mibBuilder.loadTexts:mal_liquid_level.setUnits(_C)
class _Mall_pres_lpres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_pres_lpres_Type.__name__=_B
_Mall_pres_lpres_Object=MibScalar
mall_pres_lpres=_Mall_pres_lpres_Object((1,3,6,1,4,1,9839,2,1,1,82),_Mall_pres_lpres_Type())
mall_pres_lpres.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_pres_lpres.setStatus(_A)
if mibBuilder.loadTexts:mall_pres_lpres.setUnits(_C)
class _Mall_pres_hpres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_pres_hpres_Type.__name__=_B
_Mall_pres_hpres_Object=MibScalar
mall_pres_hpres=_Mall_pres_hpres_Object((1,3,6,1,4,1,9839,2,1,1,83),_Mall_pres_hpres_Type())
mall_pres_hpres.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_pres_hpres.setStatus(_A)
if mibBuilder.loadTexts:mall_pres_hpres.setUnits(_C)
class _Mal_low2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_low2_Type.__name__=_B
_Mal_low2_Object=MibScalar
mal_low2=_Mal_low2_Object((1,3,6,1,4,1,9839,2,1,1,84),_Mal_low2_Type())
mal_low2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_low2.setStatus(_A)
if mibBuilder.loadTexts:mal_low2.setUnits(_C)
class _Mall_alta_mand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_alta_mand_Type.__name__=_B
_Mall_alta_mand_Object=MibScalar
mall_alta_mand=_Mall_alta_mand_Object((1,3,6,1,4,1,9839,2,1,1,85),_Mall_alta_mand_Type())
mall_alta_mand.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_alta_mand.setStatus(_A)
if mibBuilder.loadTexts:mall_alta_mand.setUnits(_C)
class _Mal_low_press_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_low_press_Type.__name__=_B
_Mal_low_press_Object=MibScalar
mal_low_press=_Mal_low_press_Object((1,3,6,1,4,1,9839,2,1,1,86),_Mal_low_press_Type())
mal_low_press.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_low_press.setStatus(_A)
if mibBuilder.loadTexts:mal_low_press.setUnits(_C)
class _Mal_high_press_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_high_press_Type.__name__=_B
_Mal_high_press_Object=MibScalar
mal_high_press=_Mal_high_press_Object((1,3,6,1,4,1,9839,2,1,1,87),_Mal_high_press_Type())
mal_high_press.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_high_press.setStatus(_A)
if mibBuilder.loadTexts:mal_high_press.setUnits(_C)
class _Mal_n_input_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_n_input_Type.__name__=_B
_Mal_n_input_Object=MibScalar
mal_n_input=_Mal_n_input_Object((1,3,6,1,4,1,9839,2,1,1,88),_Mal_n_input_Type())
mal_n_input.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_n_input.setStatus(_A)
if mibBuilder.loadTexts:mal_n_input.setUnits(_C)
class _Mal_n_devices_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_n_devices_Type.__name__=_B
_Mal_n_devices_Object=MibScalar
mal_n_devices=_Mal_n_devices_Object((1,3,6,1,4,1,9839,2,1,1,89),_Mal_n_devices_Type())
mal_n_devices.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_n_devices.setStatus(_A)
if mibBuilder.loadTexts:mal_n_devices.setUnits(_C)
class _Mall_ora_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_ora_Type.__name__=_B
_Mall_ora_Object=MibScalar
mall_ora=_Mall_ora_Object((1,3,6,1,4,1,9839,2,1,1,90),_Mall_ora_Type())
mall_ora.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_ora.setStatus(_A)
if mibBuilder.loadTexts:mall_ora.setUnits(_C)
class _Mal_broke_pr1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_broke_pr1_Type.__name__=_B
_Mal_broke_pr1_Object=MibScalar
mal_broke_pr1=_Mal_broke_pr1_Object((1,3,6,1,4,1,9839,2,1,1,91),_Mal_broke_pr1_Type())
mal_broke_pr1.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_broke_pr1.setStatus(_A)
if mibBuilder.loadTexts:mal_broke_pr1.setUnits(_C)
class _Mal_broke_pr2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mal_broke_pr2_Type.__name__=_B
_Mal_broke_pr2_Object=MibScalar
mal_broke_pr2=_Mal_broke_pr2_Object((1,3,6,1,4,1,9839,2,1,1,92),_Mal_broke_pr2_Type())
mal_broke_pr2.setMaxAccess(_D)
if mibBuilder.loadTexts:mal_broke_pr2.setStatus(_A)
if mibBuilder.loadTexts:mal_broke_pr2.setUnits(_C)
class _Glb_al_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Glb_al_Type.__name__=_B
_Glb_al_Object=MibScalar
glb_al=_Glb_al_Object((1,3,6,1,4,1,9839,2,1,1,93),_Glb_al_Type())
glb_al.setMaxAccess(_D)
if mibBuilder.loadTexts:glb_al.setStatus(_A)
if mibBuilder.loadTexts:glb_al.setUnits(_C)
class _Syson_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Syson_Type.__name__=_B
_Syson_Object=MibScalar
syson=_Syson_Object((1,3,6,1,4,1,9839,2,1,1,101),_Syson_Type())
syson.setMaxAccess(_D)
if mibBuilder.loadTexts:syson.setStatus(_A)
if mibBuilder.loadTexts:syson.setUnits(_C)
class _En_off_supervisor_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_off_supervisor_Type.__name__=_B
_En_off_supervisor_Object=MibScalar
en_off_supervisor=_En_off_supervisor_Object((1,3,6,1,4,1,9839,2,1,1,112),_En_off_supervisor_Type())
en_off_supervisor.setMaxAccess(_E)
if mibBuilder.loadTexts:en_off_supervisor.setStatus(_A)
if mibBuilder.loadTexts:en_off_supervisor.setUnits(_C)
class _Fan5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Fan5_Type.__name__=_B
_Fan5_Object=MibScalar
fan5=_Fan5_Object((1,3,6,1,4,1,9839,2,1,1,114),_Fan5_Type())
fan5.setMaxAccess(_D)
if mibBuilder.loadTexts:fan5.setStatus(_A)
if mibBuilder.loadTexts:fan5.setUnits(_C)
class _Mall_term_vent5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Mall_term_vent5_Type.__name__=_B
_Mall_term_vent5_Object=MibScalar
mall_term_vent5=_Mall_term_vent5_Object((1,3,6,1,4,1,9839,2,1,1,115),_Mall_term_vent5_Type())
mall_term_vent5.setMaxAccess(_D)
if mibBuilder.loadTexts:mall_term_vent5.setStatus(_A)
if mibBuilder.loadTexts:mall_term_vent5.setUnits(_C)
class _En_on_balck_out_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_En_on_balck_out_Type.__name__=_B
_En_on_balck_out_Object=MibScalar
en_on_balck_out=_En_on_balck_out_Object((1,3,6,1,4,1,9839,2,1,1,118),_En_on_balck_out_Type())
en_on_balck_out.setMaxAccess(_E)
if mibBuilder.loadTexts:en_on_balck_out.setStatus(_A)
if mibBuilder.loadTexts:en_on_balck_out.setUnits(_C)
class _Dout1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout1_Type.__name__=_B
_Dout1_Object=MibScalar
dout1=_Dout1_Object((1,3,6,1,4,1,9839,2,1,1,119),_Dout1_Type())
dout1.setMaxAccess(_D)
if mibBuilder.loadTexts:dout1.setStatus(_A)
if mibBuilder.loadTexts:dout1.setUnits(_C)
class _Dout2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout2_Type.__name__=_B
_Dout2_Object=MibScalar
dout2=_Dout2_Object((1,3,6,1,4,1,9839,2,1,1,120),_Dout2_Type())
dout2.setMaxAccess(_D)
if mibBuilder.loadTexts:dout2.setStatus(_A)
if mibBuilder.loadTexts:dout2.setUnits(_C)
class _Dout3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout3_Type.__name__=_B
_Dout3_Object=MibScalar
dout3=_Dout3_Object((1,3,6,1,4,1,9839,2,1,1,121),_Dout3_Type())
dout3.setMaxAccess(_D)
if mibBuilder.loadTexts:dout3.setStatus(_A)
if mibBuilder.loadTexts:dout3.setUnits(_C)
class _Dout4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout4_Type.__name__=_B
_Dout4_Object=MibScalar
dout4=_Dout4_Object((1,3,6,1,4,1,9839,2,1,1,122),_Dout4_Type())
dout4.setMaxAccess(_D)
if mibBuilder.loadTexts:dout4.setStatus(_A)
if mibBuilder.loadTexts:dout4.setUnits(_C)
class _Dout5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout5_Type.__name__=_B
_Dout5_Object=MibScalar
dout5=_Dout5_Object((1,3,6,1,4,1,9839,2,1,1,123),_Dout5_Type())
dout5.setMaxAccess(_D)
if mibBuilder.loadTexts:dout5.setStatus(_A)
if mibBuilder.loadTexts:dout5.setUnits(_C)
class _Dout6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout6_Type.__name__=_B
_Dout6_Object=MibScalar
dout6=_Dout6_Object((1,3,6,1,4,1,9839,2,1,1,124),_Dout6_Type())
dout6.setMaxAccess(_D)
if mibBuilder.loadTexts:dout6.setStatus(_A)
if mibBuilder.loadTexts:dout6.setUnits(_C)
class _Dout7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout7_Type.__name__=_B
_Dout7_Object=MibScalar
dout7=_Dout7_Object((1,3,6,1,4,1,9839,2,1,1,125),_Dout7_Type())
dout7.setMaxAccess(_D)
if mibBuilder.loadTexts:dout7.setStatus(_A)
if mibBuilder.loadTexts:dout7.setUnits(_C)
class _Dout8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout8_Type.__name__=_B
_Dout8_Object=MibScalar
dout8=_Dout8_Object((1,3,6,1,4,1,9839,2,1,1,126),_Dout8_Type())
dout8.setMaxAccess(_D)
if mibBuilder.loadTexts:dout8.setStatus(_A)
if mibBuilder.loadTexts:dout8.setUnits(_C)
class _Dout9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout9_Type.__name__=_B
_Dout9_Object=MibScalar
dout9=_Dout9_Object((1,3,6,1,4,1,9839,2,1,1,127),_Dout9_Type())
dout9.setMaxAccess(_D)
if mibBuilder.loadTexts:dout9.setStatus(_A)
if mibBuilder.loadTexts:dout9.setUnits(_C)
class _Dout10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout10_Type.__name__=_B
_Dout10_Object=MibScalar
dout10=_Dout10_Object((1,3,6,1,4,1,9839,2,1,1,128),_Dout10_Type())
dout10.setMaxAccess(_D)
if mibBuilder.loadTexts:dout10.setStatus(_A)
if mibBuilder.loadTexts:dout10.setUnits(_C)
class _Dout11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout11_Type.__name__=_B
_Dout11_Object=MibScalar
dout11=_Dout11_Object((1,3,6,1,4,1,9839,2,1,1,129),_Dout11_Type())
dout11.setMaxAccess(_D)
if mibBuilder.loadTexts:dout11.setStatus(_A)
if mibBuilder.loadTexts:dout11.setUnits(_C)
class _Dout12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout12_Type.__name__=_B
_Dout12_Object=MibScalar
dout12=_Dout12_Object((1,3,6,1,4,1,9839,2,1,1,130),_Dout12_Type())
dout12.setMaxAccess(_D)
if mibBuilder.loadTexts:dout12.setStatus(_A)
if mibBuilder.loadTexts:dout12.setUnits(_C)
class _Dout13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout13_Type.__name__=_B
_Dout13_Object=MibScalar
dout13=_Dout13_Object((1,3,6,1,4,1,9839,2,1,1,131),_Dout13_Type())
dout13.setMaxAccess(_D)
if mibBuilder.loadTexts:dout13.setStatus(_A)
if mibBuilder.loadTexts:dout13.setUnits(_C)
class _Dout14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout14_Type.__name__=_B
_Dout14_Object=MibScalar
dout14=_Dout14_Object((1,3,6,1,4,1,9839,2,1,1,132),_Dout14_Type())
dout14.setMaxAccess(_D)
if mibBuilder.loadTexts:dout14.setStatus(_A)
if mibBuilder.loadTexts:dout14.setUnits(_C)
class _Dout15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout15_Type.__name__=_B
_Dout15_Object=MibScalar
dout15=_Dout15_Object((1,3,6,1,4,1,9839,2,1,1,133),_Dout15_Type())
dout15.setMaxAccess(_D)
if mibBuilder.loadTexts:dout15.setStatus(_A)
if mibBuilder.loadTexts:dout15.setUnits(_C)
class _Dout16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout16_Type.__name__=_B
_Dout16_Object=MibScalar
dout16=_Dout16_Object((1,3,6,1,4,1,9839,2,1,1,134),_Dout16_Type())
dout16.setMaxAccess(_D)
if mibBuilder.loadTexts:dout16.setStatus(_A)
if mibBuilder.loadTexts:dout16.setUnits(_C)
class _Dout17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout17_Type.__name__=_B
_Dout17_Object=MibScalar
dout17=_Dout17_Object((1,3,6,1,4,1,9839,2,1,1,135),_Dout17_Type())
dout17.setMaxAccess(_D)
if mibBuilder.loadTexts:dout17.setStatus(_A)
if mibBuilder.loadTexts:dout17.setUnits(_C)
class _Dout18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dout18_Type.__name__=_B
_Dout18_Object=MibScalar
dout18=_Dout18_Object((1,3,6,1,4,1,9839,2,1,1,136),_Dout18_Type())
dout18.setMaxAccess(_D)
if mibBuilder.loadTexts:dout18.setStatus(_A)
if mibBuilder.loadTexts:dout18.setUnits(_C)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _Asp_conv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Asp_conv_Type.__name__=_B
_Asp_conv_Object=MibScalar
asp_conv=_Asp_conv_Object((1,3,6,1,4,1,9839,2,1,2,1),_Asp_conv_Type())
asp_conv.setMaxAccess(_D)
if mibBuilder.loadTexts:asp_conv.setStatus(_A)
if mibBuilder.loadTexts:asp_conv.setUnits(_F)
class _Press_mand_conv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Press_mand_conv_Type.__name__=_B
_Press_mand_conv_Object=MibScalar
press_mand_conv=_Press_mand_conv_Object((1,3,6,1,4,1,9839,2,1,2,2),_Press_mand_conv_Type())
press_mand_conv.setMaxAccess(_D)
if mibBuilder.loadTexts:press_mand_conv.setStatus(_A)
if mibBuilder.loadTexts:press_mand_conv.setUnits(_F)
class _Out_inv_fan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Out_inv_fan_Type.__name__=_B
_Out_inv_fan_Object=MibScalar
out_inv_fan=_Out_inv_fan_Object((1,3,6,1,4,1,9839,2,1,2,3),_Out_inv_fan_Type())
out_inv_fan.setMaxAccess(_D)
if mibBuilder.loadTexts:out_inv_fan.setStatus(_A)
if mibBuilder.loadTexts:out_inv_fan.setUnits(_C)
class _Inverter_comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Inverter_comp1_Type.__name__=_B
_Inverter_comp1_Object=MibScalar
inverter_comp1=_Inverter_comp1_Object((1,3,6,1,4,1,9839,2,1,2,4),_Inverter_comp1_Type())
inverter_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:inverter_comp1.setStatus(_A)
if mibBuilder.loadTexts:inverter_comp1.setUnits(_C)
class _Set_comp_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_comp_Type.__name__=_B
_Set_comp_Object=MibScalar
set_comp=_Set_comp_Object((1,3,6,1,4,1,9839,2,1,2,5),_Set_comp_Type())
set_comp.setMaxAccess(_E)
if mibBuilder.loadTexts:set_comp.setStatus(_A)
if mibBuilder.loadTexts:set_comp.setUnits(_F)
class _Diff_comp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_Diff_comp_Type.__name__=_B
_Diff_comp_Object=MibScalar
diff_comp=_Diff_comp_Object((1,3,6,1,4,1,9839,2,1,2,6),_Diff_comp_Type())
diff_comp.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_comp.setStatus(_A)
if mibBuilder.loadTexts:diff_comp.setUnits(_F)
class _Set_fan_Type(Integer32):defaultValue=155;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_fan_Type.__name__=_B
_Set_fan_Object=MibScalar
set_fan=_Set_fan_Object((1,3,6,1,4,1,9839,2,1,2,7),_Set_fan_Type())
set_fan.setMaxAccess(_E)
if mibBuilder.loadTexts:set_fan.setStatus(_A)
if mibBuilder.loadTexts:set_fan.setUnits(_F)
class _Diff_fan_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Diff_fan_Type.__name__=_B
_Diff_fan_Object=MibScalar
diff_fan=_Diff_fan_Object((1,3,6,1,4,1,9839,2,1,2,8),_Diff_fan_Type())
diff_fan.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_fan.setStatus(_A)
if mibBuilder.loadTexts:diff_fan.setUnits(_F)
class _Voltage_in_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Voltage_in_Type.__name__=_B
_Voltage_in_Object=MibScalar
voltage_in=_Voltage_in_Object((1,3,6,1,4,1,9839,2,1,2,9),_Voltage_in_Type())
voltage_in.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage_in.setStatus(_A)
if mibBuilder.loadTexts:voltage_in.setUnits(_C)
class _Max_set_co_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,999))
_Max_set_co_Type.__name__=_B
_Max_set_co_Object=MibScalar
max_set_co=_Max_set_co_Object((1,3,6,1,4,1,9839,2,1,2,10),_Max_set_co_Type())
max_set_co.setMaxAccess(_E)
if mibBuilder.loadTexts:max_set_co.setStatus(_A)
if mibBuilder.loadTexts:max_set_co.setUnits(_F)
class _Min_set_co_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,999))
_Min_set_co_Type.__name__=_B
_Min_set_co_Object=MibScalar
min_set_co=_Min_set_co_Object((1,3,6,1,4,1,9839,2,1,2,11),_Min_set_co_Type())
min_set_co.setMaxAccess(_E)
if mibBuilder.loadTexts:min_set_co.setStatus(_A)
if mibBuilder.loadTexts:min_set_co.setUnits(_F)
class _Max_set_fa_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,999))
_Max_set_fa_Type.__name__=_B
_Max_set_fa_Object=MibScalar
max_set_fa=_Max_set_fa_Object((1,3,6,1,4,1,9839,2,1,2,12),_Max_set_fa_Type())
max_set_fa.setMaxAccess(_E)
if mibBuilder.loadTexts:max_set_fa.setStatus(_A)
if mibBuilder.loadTexts:max_set_fa.setUnits(_F)
class _Min_set_fa_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,999))
_Min_set_fa_Type.__name__=_B
_Min_set_fa_Object=MibScalar
min_set_fa=_Min_set_fa_Object((1,3,6,1,4,1,9839,2,1,2,13),_Min_set_fa_Type())
min_set_fa.setMaxAccess(_E)
if mibBuilder.loadTexts:min_set_fa.setStatus(_A)
if mibBuilder.loadTexts:min_set_fa.setUnits(_F)
class _Thresh_high1_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Thresh_high1_Type.__name__=_B
_Thresh_high1_Object=MibScalar
thresh_high1=_Thresh_high1_Object((1,3,6,1,4,1,9839,2,1,2,14),_Thresh_high1_Type())
thresh_high1.setMaxAccess(_E)
if mibBuilder.loadTexts:thresh_high1.setStatus(_A)
if mibBuilder.loadTexts:thresh_high1.setUnits(_F)
class _Diff_high1_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Diff_high1_Type.__name__=_B
_Diff_high1_Object=MibScalar
diff_high1=_Diff_high1_Object((1,3,6,1,4,1,9839,2,1,2,15),_Diff_high1_Type())
diff_high1.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_high1.setStatus(_A)
if mibBuilder.loadTexts:diff_high1.setUnits(_F)
class _Thresh_low1_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,50))
_Thresh_low1_Type.__name__=_B
_Thresh_low1_Object=MibScalar
thresh_low1=_Thresh_low1_Object((1,3,6,1,4,1,9839,2,1,2,16),_Thresh_low1_Type())
thresh_low1.setMaxAccess(_E)
if mibBuilder.loadTexts:thresh_low1.setStatus(_A)
if mibBuilder.loadTexts:thresh_low1.setUnits(_F)
class _Diff_low1_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Diff_low1_Type.__name__=_B
_Diff_low1_Object=MibScalar
diff_low1=_Diff_low1_Object((1,3,6,1,4,1,9839,2,1,2,17),_Diff_low1_Type())
diff_low1.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_low1.setStatus(_A)
if mibBuilder.loadTexts:diff_low1.setUnits(_F)
class _Thresh_high2_Type(Integer32):defaultValue=185;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,300))
_Thresh_high2_Type.__name__=_B
_Thresh_high2_Object=MibScalar
thresh_high2=_Thresh_high2_Object((1,3,6,1,4,1,9839,2,1,2,18),_Thresh_high2_Type())
thresh_high2.setMaxAccess(_E)
if mibBuilder.loadTexts:thresh_high2.setStatus(_A)
if mibBuilder.loadTexts:thresh_high2.setUnits(_F)
class _Diff_high2_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,40))
_Diff_high2_Type.__name__=_B
_Diff_high2_Object=MibScalar
diff_high2=_Diff_high2_Object((1,3,6,1,4,1,9839,2,1,2,19),_Diff_high2_Type())
diff_high2.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_high2.setStatus(_A)
if mibBuilder.loadTexts:diff_high2.setUnits(_F)
class _Thresh_low2_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,300))
_Thresh_low2_Type.__name__=_B
_Thresh_low2_Object=MibScalar
thresh_low2=_Thresh_low2_Object((1,3,6,1,4,1,9839,2,1,2,20),_Thresh_low2_Type())
thresh_low2.setMaxAccess(_E)
if mibBuilder.loadTexts:thresh_low2.setStatus(_A)
if mibBuilder.loadTexts:thresh_low2.setUnits(_F)
class _Diff_low2_Type(Integer32):defaultValue=1200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_Diff_low2_Type.__name__=_B
_Diff_low2_Object=MibScalar
diff_low2=_Diff_low2_Object((1,3,6,1,4,1,9839,2,1,2,21),_Diff_low2_Type())
diff_low2.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_low2.setStatus(_A)
if mibBuilder.loadTexts:diff_low2.setUnits('sec x10')
class _Set_vent_inv_Type(Integer32):defaultValue=155;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Set_vent_inv_Type.__name__=_B
_Set_vent_inv_Object=MibScalar
set_vent_inv=_Set_vent_inv_Object((1,3,6,1,4,1,9839,2,1,2,27),_Set_vent_inv_Type())
set_vent_inv.setMaxAccess(_E)
if mibBuilder.loadTexts:set_vent_inv.setStatus(_A)
if mibBuilder.loadTexts:set_vent_inv.setUnits(_F)
class _Diff_vent_inv_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_Diff_vent_inv_Type.__name__=_B
_Diff_vent_inv_Object=MibScalar
diff_vent_inv=_Diff_vent_inv_Object((1,3,6,1,4,1,9839,2,1,2,28),_Diff_vent_inv_Type())
diff_vent_inv.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_vent_inv.setStatus(_A)
if mibBuilder.loadTexts:diff_vent_inv.setUnits(_F)
class _Seinverter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Seinverter_Type.__name__=_B
_Seinverter_Object=MibScalar
seinverter=_Seinverter_Object((1,3,6,1,4,1,9839,2,1,2,32),_Seinverter_Type())
seinverter.setMaxAccess(_E)
if mibBuilder.loadTexts:seinverter.setStatus(_A)
if mibBuilder.loadTexts:seinverter.setUnits(_C)
class _Diff_inv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Diff_inv_Type.__name__=_B
_Diff_inv_Object=MibScalar
diff_inv=_Diff_inv_Object((1,3,6,1,4,1,9839,2,1,2,33),_Diff_inv_Type())
diff_inv.setMaxAccess(_E)
if mibBuilder.loadTexts:diff_inv.setStatus(_A)
if mibBuilder.loadTexts:diff_inv.setUnits(_C)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _Lhour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Lhour_Type.__name__=_B
_Lhour_Object=MibScalar
lhour=_Lhour_Object((1,3,6,1,4,1,9839,2,1,3,11),_Lhour_Type())
lhour.setMaxAccess(_E)
if mibBuilder.loadTexts:lhour.setStatus(_A)
if mibBuilder.loadTexts:lhour.setUnits(_C)
class _Lminute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Lminute_Type.__name__=_B
_Lminute_Object=MibScalar
lminute=_Lminute_Object((1,3,6,1,4,1,9839,2,1,3,12),_Lminute_Type())
lminute.setMaxAccess(_E)
if mibBuilder.loadTexts:lminute.setStatus(_A)
if mibBuilder.loadTexts:lminute.setUnits(_C)
class _Lday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Lday_Type.__name__=_B
_Lday_Object=MibScalar
lday=_Lday_Object((1,3,6,1,4,1,9839,2,1,3,13),_Lday_Type())
lday.setMaxAccess(_E)
if mibBuilder.loadTexts:lday.setStatus(_A)
if mibBuilder.loadTexts:lday.setUnits(_C)
class _Lmonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Lmonth_Type.__name__=_B
_Lmonth_Object=MibScalar
lmonth=_Lmonth_Object((1,3,6,1,4,1,9839,2,1,3,14),_Lmonth_Type())
lmonth.setMaxAccess(_E)
if mibBuilder.loadTexts:lmonth.setStatus(_A)
if mibBuilder.loadTexts:lmonth.setUnits(_C)
class _Lyear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Lyear_Type.__name__=_B
_Lyear_Object=MibScalar
lyear=_Lyear_Object((1,3,6,1,4,1,9839,2,1,3,15),_Lyear_Type())
lyear.setMaxAccess(_E)
if mibBuilder.loadTexts:lyear.setStatus(_A)
if mibBuilder.loadTexts:lyear.setUnits(_C)
class _Hour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_Type.__name__=_B
_Hour_Object=MibScalar
hour=_Hour_Object((1,3,6,1,4,1,9839,2,1,3,16),_Hour_Type())
hour.setMaxAccess(_D)
if mibBuilder.loadTexts:hour.setStatus(_A)
if mibBuilder.loadTexts:hour.setUnits(_C)
class _Minute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Minute_Type.__name__=_B
_Minute_Object=MibScalar
minute=_Minute_Object((1,3,6,1,4,1,9839,2,1,3,17),_Minute_Type())
minute.setMaxAccess(_D)
if mibBuilder.loadTexts:minute.setStatus(_A)
if mibBuilder.loadTexts:minute.setUnits(_C)
class _Month_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Month_Type.__name__=_B
_Month_Object=MibScalar
month=_Month_Object((1,3,6,1,4,1,9839,2,1,3,18),_Month_Type())
month.setMaxAccess(_D)
if mibBuilder.loadTexts:month.setStatus(_A)
if mibBuilder.loadTexts:month.setUnits(_C)
class _Pyear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Pyear_Type.__name__=_B
_Pyear_Object=MibScalar
pyear=_Pyear_Object((1,3,6,1,4,1,9839,2,1,3,19),_Pyear_Type())
pyear.setMaxAccess(_D)
if mibBuilder.loadTexts:pyear.setStatus(_A)
if mibBuilder.loadTexts:pyear.setUnits(_C)
class _Oil_diff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Oil_diff_Type.__name__=_B
_Oil_diff_Object=MibScalar
oil_diff=_Oil_diff_Object((1,3,6,1,4,1,9839,2,1,3,21),_Oil_diff_Type())
oil_diff.setMaxAccess(_E)
if mibBuilder.loadTexts:oil_diff.setStatus(_A)
if mibBuilder.loadTexts:oil_diff.setUnits(_C)
class _Out_inv_fani_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Out_inv_fani_Type.__name__=_B
_Out_inv_fani_Object=MibScalar
out_inv_fani=_Out_inv_fani_Object((1,3,6,1,4,1,9839,2,1,3,26),_Out_inv_fani_Type())
out_inv_fani.setMaxAccess(_D)
if mibBuilder.loadTexts:out_inv_fani.setStatus(_A)
if mibBuilder.loadTexts:out_inv_fani.setUnits(_C)
class _Inverter_compi1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Inverter_compi1_Type.__name__=_B
_Inverter_compi1_Object=MibScalar
inverter_compi1=_Inverter_compi1_Object((1,3,6,1,4,1,9839,2,1,3,27),_Inverter_compi1_Type())
inverter_compi1.setMaxAccess(_D)
if mibBuilder.loadTexts:inverter_compi1.setStatus(_A)
if mibBuilder.loadTexts:inverter_compi1.setUnits(_C)
class _Board_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Board_type_Type.__name__=_B
_Board_type_Object=MibScalar
board_type=_Board_type_Object((1,3,6,1,4,1,9839,2,1,3,28),_Board_type_Type())
board_type.setMaxAccess(_D)
if mibBuilder.loadTexts:board_type.setStatus(_A)
if mibBuilder.loadTexts:board_type.setUnits(_C)
class _Unit_status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Unit_status_Type.__name__=_B
_Unit_status_Object=MibScalar
unit_status=_Unit_status_Object((1,3,6,1,4,1,9839,2,1,3,29),_Unit_status_Type())
unit_status.setMaxAccess(_D)
if mibBuilder.loadTexts:unit_status.setStatus(_A)
if mibBuilder.loadTexts:unit_status.setUnits(_C)
class _Type_b1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Type_b1_Type.__name__=_B
_Type_b1_Object=MibScalar
type_b1=_Type_b1_Object((1,3,6,1,4,1,9839,2,1,3,30),_Type_b1_Type())
type_b1.setMaxAccess(_D)
if mibBuilder.loadTexts:type_b1.setStatus(_A)
if mibBuilder.loadTexts:type_b1.setUnits(_C)
class _Type_b2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Type_b2_Type.__name__=_B
_Type_b2_Object=MibScalar
type_b2=_Type_b2_Object((1,3,6,1,4,1,9839,2,1,3,31),_Type_b2_Type())
type_b2.setMaxAccess(_D)
if mibBuilder.loadTexts:type_b2.setStatus(_A)
if mibBuilder.loadTexts:type_b2.setUnits(_C)
class _Bios_release_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Bios_release_Type.__name__=_B
_Bios_release_Object=MibScalar
bios_release=_Bios_release_Object((1,3,6,1,4,1,9839,2,1,3,32),_Bios_release_Type())
bios_release.setMaxAccess(_D)
if mibBuilder.loadTexts:bios_release.setStatus(_A)
if mibBuilder.loadTexts:bios_release.setUnits(_C)
class _Bios_date_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Bios_date_Type.__name__=_B
_Bios_date_Object=MibScalar
bios_date=_Bios_date_Object((1,3,6,1,4,1,9839,2,1,3,33),_Bios_date_Type())
bios_date.setMaxAccess(_D)
if mibBuilder.loadTexts:bios_date.setStatus(_A)
if mibBuilder.loadTexts:bios_date.setUnits(_C)
class _Boot_release_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Boot_release_Type.__name__=_B
_Boot_release_Object=MibScalar
boot_release=_Boot_release_Object((1,3,6,1,4,1,9839,2,1,3,34),_Boot_release_Type())
boot_release.setMaxAccess(_D)
if mibBuilder.loadTexts:boot_release.setStatus(_A)
if mibBuilder.loadTexts:boot_release.setUnits(_C)
class _Boot_date_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Boot_date_Type.__name__=_B
_Boot_date_Object=MibScalar
boot_date=_Boot_date_Object((1,3,6,1,4,1,9839,2,1,3,35),_Boot_date_Type())
boot_date.setMaxAccess(_D)
if mibBuilder.loadTexts:boot_date.setStatus(_A)
if mibBuilder.loadTexts:boot_date.setUnits(_C)
class _Time_switch_on1_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,360))
_Time_switch_on1_Type.__name__=_B
_Time_switch_on1_Object=MibScalar
time_switch_on1=_Time_switch_on1_Object((1,3,6,1,4,1,9839,2,1,3,37),_Time_switch_on1_Type())
time_switch_on1.setMaxAccess(_E)
if mibBuilder.loadTexts:time_switch_on1.setStatus(_A)
if mibBuilder.loadTexts:time_switch_on1.setUnits(_G)
class _Time_switchoff1_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,360))
_Time_switchoff1_Type.__name__=_B
_Time_switchoff1_Object=MibScalar
time_switchoff1=_Time_switchoff1_Object((1,3,6,1,4,1,9839,2,1,3,38),_Time_switchoff1_Type())
time_switchoff1.setMaxAccess(_E)
if mibBuilder.loadTexts:time_switchoff1.setStatus(_A)
if mibBuilder.loadTexts:time_switchoff1.setUnits(_G)
class _Time_min_on_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,360))
_Time_min_on_Type.__name__=_B
_Time_min_on_Object=MibScalar
time_min_on=_Time_min_on_Object((1,3,6,1,4,1,9839,2,1,3,39),_Time_min_on_Type())
time_min_on.setMaxAccess(_E)
if mibBuilder.loadTexts:time_min_on.setStatus(_A)
if mibBuilder.loadTexts:time_min_on.setUnits(_G)
class _Time_min_off_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,360))
_Time_min_off_Type.__name__=_B
_Time_min_off_Object=MibScalar
time_min_off=_Time_min_off_Object((1,3,6,1,4,1,9839,2,1,3,40),_Time_min_off_Type())
time_min_off.setMaxAccess(_E)
if mibBuilder.loadTexts:time_min_off.setStatus(_A)
if mibBuilder.loadTexts:time_min_off.setUnits(_G)
class _Time_betw_comp_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_Time_betw_comp_Type.__name__=_B
_Time_betw_comp_Object=MibScalar
time_betw_comp=_Time_betw_comp_Object((1,3,6,1,4,1,9839,2,1,3,41),_Time_betw_comp_Type())
time_betw_comp.setMaxAccess(_E)
if mibBuilder.loadTexts:time_betw_comp.setStatus(_A)
if mibBuilder.loadTexts:time_betw_comp.setUnits(_G)
class _Time_same_comp_Type(Integer32):defaultValue=360;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(240,600))
_Time_same_comp_Type.__name__=_B
_Time_same_comp_Object=MibScalar
time_same_comp=_Time_same_comp_Object((1,3,6,1,4,1,9839,2,1,3,42),_Time_same_comp_Type())
time_same_comp.setMaxAccess(_E)
if mibBuilder.loadTexts:time_same_comp.setStatus(_A)
if mibBuilder.loadTexts:time_same_comp.setUnits(_G)
class _Unload_delay_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Unload_delay_Type.__name__=_B
_Unload_delay_Object=MibScalar
unload_delay=_Unload_delay_Object((1,3,6,1,4,1,9839,2,1,3,43),_Unload_delay_Type())
unload_delay.setMaxAccess(_E)
if mibBuilder.loadTexts:unload_delay.setStatus(_A)
if mibBuilder.loadTexts:unload_delay.setUnits(_G)
class _Time_switch_on2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Time_switch_on2_Type.__name__=_B
_Time_switch_on2_Object=MibScalar
time_switch_on2=_Time_switch_on2_Object((1,3,6,1,4,1,9839,2,1,3,44),_Time_switch_on2_Type())
time_switch_on2.setMaxAccess(_E)
if mibBuilder.loadTexts:time_switch_on2.setStatus(_A)
if mibBuilder.loadTexts:time_switch_on2.setUnits(_G)
class _Time_switchoff2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Time_switchoff2_Type.__name__=_B
_Time_switchoff2_Object=MibScalar
time_switchoff2=_Time_switchoff2_Object((1,3,6,1,4,1,9839,2,1,3,45),_Time_switchoff2_Type())
time_switchoff2.setMaxAccess(_E)
if mibBuilder.loadTexts:time_switchoff2.setStatus(_A)
if mibBuilder.loadTexts:time_switchoff2.setUnits(_G)
class _Time_betw_fan_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_Time_betw_fan_Type.__name__=_B
_Time_betw_fan_Object=MibScalar
time_betw_fan=_Time_betw_fan_Object((1,3,6,1,4,1,9839,2,1,3,46),_Time_betw_fan_Type())
time_betw_fan.setMaxAccess(_E)
if mibBuilder.loadTexts:time_betw_fan.setStatus(_A)
if mibBuilder.loadTexts:time_betw_fan.setUnits(_G)
class _Rit_dif_olio_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,360))
_Rit_dif_olio_Type.__name__=_B
_Rit_dif_olio_Object=MibScalar
rit_dif_olio=_Rit_dif_olio_Object((1,3,6,1,4,1,9839,2,1,3,47),_Rit_dif_olio_Type())
rit_dif_olio.setMaxAccess(_E)
if mibBuilder.loadTexts:rit_dif_olio.setStatus(_A)
if mibBuilder.loadTexts:rit_dif_olio.setUnits(_G)
class _Rit_all_liq_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,360))
_Rit_all_liq_Type.__name__=_B
_Rit_all_liq_Object=MibScalar
rit_all_liq=_Rit_all_liq_Object((1,3,6,1,4,1,9839,2,1,3,48),_Rit_all_liq_Type())
rit_all_liq.setMaxAccess(_E)
if mibBuilder.loadTexts:rit_all_liq.setStatus(_A)
if mibBuilder.loadTexts:rit_all_liq.setUnits(_G)
class _Sg_ore_comp_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_Sg_ore_comp_Type.__name__=_B
_Sg_ore_comp_Object=MibScalar
sg_ore_comp=_Sg_ore_comp_Object((1,3,6,1,4,1,9839,2,1,3,53),_Sg_ore_comp_Type())
sg_ore_comp.setMaxAccess(_E)
if mibBuilder.loadTexts:sg_ore_comp.setStatus(_A)
if mibBuilder.loadTexts:sg_ore_comp.setUnits('Hours')
class _Hour_comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_comp1_Type.__name__=_B
_Hour_comp1_Object=MibScalar
hour_comp1=_Hour_comp1_Object((1,3,6,1,4,1,9839,2,1,3,54),_Hour_comp1_Type())
hour_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_comp1.setStatus(_A)
if mibBuilder.loadTexts:hour_comp1.setUnits(_C)
class _Hour_l_comp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_l_comp1_Type.__name__=_B
_Hour_l_comp1_Object=MibScalar
hour_l_comp1=_Hour_l_comp1_Object((1,3,6,1,4,1,9839,2,1,3,55),_Hour_l_comp1_Type())
hour_l_comp1.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_l_comp1.setStatus(_A)
if mibBuilder.loadTexts:hour_l_comp1.setUnits(_C)
class _Hour_comp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_comp2_Type.__name__=_B
_Hour_comp2_Object=MibScalar
hour_comp2=_Hour_comp2_Object((1,3,6,1,4,1,9839,2,1,3,56),_Hour_comp2_Type())
hour_comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_comp2.setStatus(_A)
if mibBuilder.loadTexts:hour_comp2.setUnits(_C)
class _Hour_l_comp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_l_comp2_Type.__name__=_B
_Hour_l_comp2_Object=MibScalar
hour_l_comp2=_Hour_l_comp2_Object((1,3,6,1,4,1,9839,2,1,3,57),_Hour_l_comp2_Type())
hour_l_comp2.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_l_comp2.setStatus(_A)
if mibBuilder.loadTexts:hour_l_comp2.setUnits(_C)
class _Hour_comp3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_comp3_Type.__name__=_B
_Hour_comp3_Object=MibScalar
hour_comp3=_Hour_comp3_Object((1,3,6,1,4,1,9839,2,1,3,58),_Hour_comp3_Type())
hour_comp3.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_comp3.setStatus(_A)
if mibBuilder.loadTexts:hour_comp3.setUnits(_C)
class _Hour_l_comp3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_l_comp3_Type.__name__=_B
_Hour_l_comp3_Object=MibScalar
hour_l_comp3=_Hour_l_comp3_Object((1,3,6,1,4,1,9839,2,1,3,59),_Hour_l_comp3_Type())
hour_l_comp3.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_l_comp3.setStatus(_A)
if mibBuilder.loadTexts:hour_l_comp3.setUnits(_C)
class _Hour_comp4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_comp4_Type.__name__=_B
_Hour_comp4_Object=MibScalar
hour_comp4=_Hour_comp4_Object((1,3,6,1,4,1,9839,2,1,3,60),_Hour_comp4_Type())
hour_comp4.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_comp4.setStatus(_A)
if mibBuilder.loadTexts:hour_comp4.setUnits(_C)
class _Hour_l_comp4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_l_comp4_Type.__name__=_B
_Hour_l_comp4_Object=MibScalar
hour_l_comp4=_Hour_l_comp4_Object((1,3,6,1,4,1,9839,2,1,3,61),_Hour_l_comp4_Type())
hour_l_comp4.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_l_comp4.setStatus(_A)
if mibBuilder.loadTexts:hour_l_comp4.setUnits(_C)
class _Hour_comp5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_comp5_Type.__name__=_B
_Hour_comp5_Object=MibScalar
hour_comp5=_Hour_comp5_Object((1,3,6,1,4,1,9839,2,1,3,62),_Hour_comp5_Type())
hour_comp5.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_comp5.setStatus(_A)
if mibBuilder.loadTexts:hour_comp5.setUnits(_C)
class _Hour_l_comp5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_l_comp5_Type.__name__=_B
_Hour_l_comp5_Object=MibScalar
hour_l_comp5=_Hour_l_comp5_Object((1,3,6,1,4,1,9839,2,1,3,63),_Hour_l_comp5_Type())
hour_l_comp5.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_l_comp5.setStatus(_A)
if mibBuilder.loadTexts:hour_l_comp5.setUnits(_C)
class _Hour_comp6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_comp6_Type.__name__=_B
_Hour_comp6_Object=MibScalar
hour_comp6=_Hour_comp6_Object((1,3,6,1,4,1,9839,2,1,3,64),_Hour_comp6_Type())
hour_comp6.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_comp6.setStatus(_A)
if mibBuilder.loadTexts:hour_comp6.setUnits(_C)
class _Hour_l_comp6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Hour_l_comp6_Type.__name__=_B
_Hour_l_comp6_Object=MibScalar
hour_l_comp6=_Hour_l_comp6_Object((1,3,6,1,4,1,9839,2,1,3,65),_Hour_l_comp6_Type())
hour_l_comp6.setMaxAccess(_D)
if mibBuilder.loadTexts:hour_l_comp6.setStatus(_A)
if mibBuilder.loadTexts:hour_l_comp6.setUnits(_C)
class _H_hour_fan1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_H_hour_fan1_Type.__name__=_B
_H_hour_fan1_Object=MibScalar
h_hour_fan1=_H_hour_fan1_Object((1,3,6,1,4,1,9839,2,1,3,66),_H_hour_fan1_Type())
h_hour_fan1.setMaxAccess(_D)
if mibBuilder.loadTexts:h_hour_fan1.setStatus(_A)
if mibBuilder.loadTexts:h_hour_fan1.setUnits(_C)
class _L_hour_fan1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_L_hour_fan1_Type.__name__=_B
_L_hour_fan1_Object=MibScalar
l_hour_fan1=_L_hour_fan1_Object((1,3,6,1,4,1,9839,2,1,3,67),_L_hour_fan1_Type())
l_hour_fan1.setMaxAccess(_D)
if mibBuilder.loadTexts:l_hour_fan1.setStatus(_A)
if mibBuilder.loadTexts:l_hour_fan1.setUnits(_C)
class _H_hour_fan2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_H_hour_fan2_Type.__name__=_B
_H_hour_fan2_Object=MibScalar
h_hour_fan2=_H_hour_fan2_Object((1,3,6,1,4,1,9839,2,1,3,68),_H_hour_fan2_Type())
h_hour_fan2.setMaxAccess(_D)
if mibBuilder.loadTexts:h_hour_fan2.setStatus(_A)
if mibBuilder.loadTexts:h_hour_fan2.setUnits(_C)
class _L_hour_fan2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_L_hour_fan2_Type.__name__=_B
_L_hour_fan2_Object=MibScalar
l_hour_fan2=_L_hour_fan2_Object((1,3,6,1,4,1,9839,2,1,3,69),_L_hour_fan2_Type())
l_hour_fan2.setMaxAccess(_D)
if mibBuilder.loadTexts:l_hour_fan2.setStatus(_A)
if mibBuilder.loadTexts:l_hour_fan2.setUnits(_C)
class _H_hour_fan3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_H_hour_fan3_Type.__name__=_B
_H_hour_fan3_Object=MibScalar
h_hour_fan3=_H_hour_fan3_Object((1,3,6,1,4,1,9839,2,1,3,70),_H_hour_fan3_Type())
h_hour_fan3.setMaxAccess(_D)
if mibBuilder.loadTexts:h_hour_fan3.setStatus(_A)
if mibBuilder.loadTexts:h_hour_fan3.setUnits(_C)
class _L_hour_fan3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_L_hour_fan3_Type.__name__=_B
_L_hour_fan3_Object=MibScalar
l_hour_fan3=_L_hour_fan3_Object((1,3,6,1,4,1,9839,2,1,3,71),_L_hour_fan3_Type())
l_hour_fan3.setMaxAccess(_D)
if mibBuilder.loadTexts:l_hour_fan3.setStatus(_A)
if mibBuilder.loadTexts:l_hour_fan3.setUnits(_C)
class _H_hour_fan4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_H_hour_fan4_Type.__name__=_B
_H_hour_fan4_Object=MibScalar
h_hour_fan4=_H_hour_fan4_Object((1,3,6,1,4,1,9839,2,1,3,72),_H_hour_fan4_Type())
h_hour_fan4.setMaxAccess(_D)
if mibBuilder.loadTexts:h_hour_fan4.setStatus(_A)
if mibBuilder.loadTexts:h_hour_fan4.setUnits(_C)
class _L_hour_fan4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_L_hour_fan4_Type.__name__=_B
_L_hour_fan4_Object=MibScalar
l_hour_fan4=_L_hour_fan4_Object((1,3,6,1,4,1,9839,2,1,3,73),_L_hour_fan4_Type())
l_hour_fan4.setMaxAccess(_D)
if mibBuilder.loadTexts:l_hour_fan4.setStatus(_A)
if mibBuilder.loadTexts:l_hour_fan4.setUnits(_C)
class _Sg_ore_fan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Sg_ore_fan_Type.__name__=_B
_Sg_ore_fan_Object=MibScalar
sg_ore_fan=_Sg_ore_fan_Object((1,3,6,1,4,1,9839,2,1,3,74),_Sg_ore_fan_Type())
sg_ore_fan.setMaxAccess(_E)
if mibBuilder.loadTexts:sg_ore_fan.setStatus(_A)
if mibBuilder.loadTexts:sg_ore_fan.setUnits(_C)
class _Version_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Version_Type.__name__=_B
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,9839,2,1,3,75),_Version_Type())
version.setMaxAccess(_D)
if mibBuilder.loadTexts:version.setStatus(_A)
if mibBuilder.loadTexts:version.setUnits(_C)
class _H_hour_fan5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_H_hour_fan5_Type.__name__=_B
_H_hour_fan5_Object=MibScalar
h_hour_fan5=_H_hour_fan5_Object((1,3,6,1,4,1,9839,2,1,3,76),_H_hour_fan5_Type())
h_hour_fan5.setMaxAccess(_D)
if mibBuilder.loadTexts:h_hour_fan5.setStatus(_A)
if mibBuilder.loadTexts:h_hour_fan5.setUnits(_C)
class _L_hour_fan5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_L_hour_fan5_Type.__name__=_B
_L_hour_fan5_Object=MibScalar
l_hour_fan5=_L_hour_fan5_Object((1,3,6,1,4,1,9839,2,1,3,77),_L_hour_fan5_Type())
l_hour_fan5.setMaxAccess(_D)
if mibBuilder.loadTexts:l_hour_fan5.setStatus(_A)
if mibBuilder.loadTexts:l_hour_fan5.setUnits(_C)
class _Time_on_black_out_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Time_on_black_out_Type.__name__=_B
_Time_on_black_out_Object=MibScalar
time_on_black_out=_Time_on_black_out_Object((1,3,6,1,4,1,9839,2,1,3,78),_Time_on_black_out_Type())
time_on_black_out.setMaxAccess(_D)
if mibBuilder.loadTexts:time_on_black_out.setStatus(_A)
if mibBuilder.loadTexts:time_on_black_out.setUnits(_C)
class _Config_in1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in1_Type.__name__=_B
_Config_in1_Object=MibScalar
config_in1=_Config_in1_Object((1,3,6,1,4,1,9839,2,1,3,79),_Config_in1_Type())
config_in1.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in1.setStatus(_A)
if mibBuilder.loadTexts:config_in1.setUnits(_C)
class _Config_in2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in2_Type.__name__=_B
_Config_in2_Object=MibScalar
config_in2=_Config_in2_Object((1,3,6,1,4,1,9839,2,1,3,80),_Config_in2_Type())
config_in2.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in2.setStatus(_A)
if mibBuilder.loadTexts:config_in2.setUnits(_C)
class _Config_in3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in3_Type.__name__=_B
_Config_in3_Object=MibScalar
config_in3=_Config_in3_Object((1,3,6,1,4,1,9839,2,1,3,81),_Config_in3_Type())
config_in3.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in3.setStatus(_A)
if mibBuilder.loadTexts:config_in3.setUnits(_C)
class _Config_in4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in4_Type.__name__=_B
_Config_in4_Object=MibScalar
config_in4=_Config_in4_Object((1,3,6,1,4,1,9839,2,1,3,82),_Config_in4_Type())
config_in4.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in4.setStatus(_A)
if mibBuilder.loadTexts:config_in4.setUnits(_C)
class _Config_in5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in5_Type.__name__=_B
_Config_in5_Object=MibScalar
config_in5=_Config_in5_Object((1,3,6,1,4,1,9839,2,1,3,83),_Config_in5_Type())
config_in5.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in5.setStatus(_A)
if mibBuilder.loadTexts:config_in5.setUnits(_C)
class _Config_in6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in6_Type.__name__=_B
_Config_in6_Object=MibScalar
config_in6=_Config_in6_Object((1,3,6,1,4,1,9839,2,1,3,84),_Config_in6_Type())
config_in6.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in6.setStatus(_A)
if mibBuilder.loadTexts:config_in6.setUnits(_C)
class _Config_in7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in7_Type.__name__=_B
_Config_in7_Object=MibScalar
config_in7=_Config_in7_Object((1,3,6,1,4,1,9839,2,1,3,85),_Config_in7_Type())
config_in7.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in7.setStatus(_A)
if mibBuilder.loadTexts:config_in7.setUnits(_C)
class _Config_in8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in8_Type.__name__=_B
_Config_in8_Object=MibScalar
config_in8=_Config_in8_Object((1,3,6,1,4,1,9839,2,1,3,86),_Config_in8_Type())
config_in8.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in8.setStatus(_A)
if mibBuilder.loadTexts:config_in8.setUnits(_C)
class _Config_in9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in9_Type.__name__=_B
_Config_in9_Object=MibScalar
config_in9=_Config_in9_Object((1,3,6,1,4,1,9839,2,1,3,87),_Config_in9_Type())
config_in9.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in9.setStatus(_A)
if mibBuilder.loadTexts:config_in9.setUnits(_C)
class _Config_in10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in10_Type.__name__=_B
_Config_in10_Object=MibScalar
config_in10=_Config_in10_Object((1,3,6,1,4,1,9839,2,1,3,88),_Config_in10_Type())
config_in10.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in10.setStatus(_A)
if mibBuilder.loadTexts:config_in10.setUnits(_C)
class _Config_in11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in11_Type.__name__=_B
_Config_in11_Object=MibScalar
config_in11=_Config_in11_Object((1,3,6,1,4,1,9839,2,1,3,89),_Config_in11_Type())
config_in11.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in11.setStatus(_A)
if mibBuilder.loadTexts:config_in11.setUnits(_C)
class _Config_in12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in12_Type.__name__=_B
_Config_in12_Object=MibScalar
config_in12=_Config_in12_Object((1,3,6,1,4,1,9839,2,1,3,90),_Config_in12_Type())
config_in12.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in12.setStatus(_A)
if mibBuilder.loadTexts:config_in12.setUnits(_C)
class _Config_in13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in13_Type.__name__=_B
_Config_in13_Object=MibScalar
config_in13=_Config_in13_Object((1,3,6,1,4,1,9839,2,1,3,91),_Config_in13_Type())
config_in13.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in13.setStatus(_A)
if mibBuilder.loadTexts:config_in13.setUnits(_C)
class _Config_in14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in14_Type.__name__=_B
_Config_in14_Object=MibScalar
config_in14=_Config_in14_Object((1,3,6,1,4,1,9839,2,1,3,92),_Config_in14_Type())
config_in14.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in14.setStatus(_A)
if mibBuilder.loadTexts:config_in14.setUnits(_C)
class _Config_in15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in15_Type.__name__=_B
_Config_in15_Object=MibScalar
config_in15=_Config_in15_Object((1,3,6,1,4,1,9839,2,1,3,93),_Config_in15_Type())
config_in15.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in15.setStatus(_A)
if mibBuilder.loadTexts:config_in15.setUnits(_C)
class _Config_in16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in16_Type.__name__=_B
_Config_in16_Object=MibScalar
config_in16=_Config_in16_Object((1,3,6,1,4,1,9839,2,1,3,94),_Config_in16_Type())
config_in16.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in16.setStatus(_A)
if mibBuilder.loadTexts:config_in16.setUnits(_C)
class _Config_in17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in17_Type.__name__=_B
_Config_in17_Object=MibScalar
config_in17=_Config_in17_Object((1,3,6,1,4,1,9839,2,1,3,95),_Config_in17_Type())
config_in17.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in17.setStatus(_A)
if mibBuilder.loadTexts:config_in17.setUnits(_C)
class _Config_in18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_in18_Type.__name__=_B
_Config_in18_Object=MibScalar
config_in18=_Config_in18_Object((1,3,6,1,4,1,9839,2,1,3,96),_Config_in18_Type())
config_in18.setMaxAccess(_D)
if mibBuilder.loadTexts:config_in18.setStatus(_A)
if mibBuilder.loadTexts:config_in18.setUnits(_C)
class _Config_out1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out1_Type.__name__=_B
_Config_out1_Object=MibScalar
config_out1=_Config_out1_Object((1,3,6,1,4,1,9839,2,1,3,97),_Config_out1_Type())
config_out1.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out1.setStatus(_A)
if mibBuilder.loadTexts:config_out1.setUnits(_C)
class _Config_out2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out2_Type.__name__=_B
_Config_out2_Object=MibScalar
config_out2=_Config_out2_Object((1,3,6,1,4,1,9839,2,1,3,98),_Config_out2_Type())
config_out2.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out2.setStatus(_A)
if mibBuilder.loadTexts:config_out2.setUnits(_C)
class _Config_out3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out3_Type.__name__=_B
_Config_out3_Object=MibScalar
config_out3=_Config_out3_Object((1,3,6,1,4,1,9839,2,1,3,99),_Config_out3_Type())
config_out3.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out3.setStatus(_A)
if mibBuilder.loadTexts:config_out3.setUnits(_C)
class _Config_out4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out4_Type.__name__=_B
_Config_out4_Object=MibScalar
config_out4=_Config_out4_Object((1,3,6,1,4,1,9839,2,1,3,100),_Config_out4_Type())
config_out4.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out4.setStatus(_A)
if mibBuilder.loadTexts:config_out4.setUnits(_C)
class _Config_out5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out5_Type.__name__=_B
_Config_out5_Object=MibScalar
config_out5=_Config_out5_Object((1,3,6,1,4,1,9839,2,1,3,101),_Config_out5_Type())
config_out5.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out5.setStatus(_A)
if mibBuilder.loadTexts:config_out5.setUnits(_C)
class _Config_out6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out6_Type.__name__=_B
_Config_out6_Object=MibScalar
config_out6=_Config_out6_Object((1,3,6,1,4,1,9839,2,1,3,102),_Config_out6_Type())
config_out6.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out6.setStatus(_A)
if mibBuilder.loadTexts:config_out6.setUnits(_C)
class _Config_out7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out7_Type.__name__=_B
_Config_out7_Object=MibScalar
config_out7=_Config_out7_Object((1,3,6,1,4,1,9839,2,1,3,103),_Config_out7_Type())
config_out7.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out7.setStatus(_A)
if mibBuilder.loadTexts:config_out7.setUnits(_C)
class _Config_out8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out8_Type.__name__=_B
_Config_out8_Object=MibScalar
config_out8=_Config_out8_Object((1,3,6,1,4,1,9839,2,1,3,104),_Config_out8_Type())
config_out8.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out8.setStatus(_A)
if mibBuilder.loadTexts:config_out8.setUnits(_C)
class _Config_out9_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out9_Type.__name__=_B
_Config_out9_Object=MibScalar
config_out9=_Config_out9_Object((1,3,6,1,4,1,9839,2,1,3,105),_Config_out9_Type())
config_out9.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out9.setStatus(_A)
if mibBuilder.loadTexts:config_out9.setUnits(_C)
class _Config_out10_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out10_Type.__name__=_B
_Config_out10_Object=MibScalar
config_out10=_Config_out10_Object((1,3,6,1,4,1,9839,2,1,3,106),_Config_out10_Type())
config_out10.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out10.setStatus(_A)
if mibBuilder.loadTexts:config_out10.setUnits(_C)
class _Config_out11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out11_Type.__name__=_B
_Config_out11_Object=MibScalar
config_out11=_Config_out11_Object((1,3,6,1,4,1,9839,2,1,3,107),_Config_out11_Type())
config_out11.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out11.setStatus(_A)
if mibBuilder.loadTexts:config_out11.setUnits(_C)
class _Config_out12_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out12_Type.__name__=_B
_Config_out12_Object=MibScalar
config_out12=_Config_out12_Object((1,3,6,1,4,1,9839,2,1,3,108),_Config_out12_Type())
config_out12.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out12.setStatus(_A)
if mibBuilder.loadTexts:config_out12.setUnits(_C)
class _Config_out13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out13_Type.__name__=_B
_Config_out13_Object=MibScalar
config_out13=_Config_out13_Object((1,3,6,1,4,1,9839,2,1,3,109),_Config_out13_Type())
config_out13.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out13.setStatus(_A)
if mibBuilder.loadTexts:config_out13.setUnits(_C)
class _Config_out14_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out14_Type.__name__=_B
_Config_out14_Object=MibScalar
config_out14=_Config_out14_Object((1,3,6,1,4,1,9839,2,1,3,110),_Config_out14_Type())
config_out14.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out14.setStatus(_A)
if mibBuilder.loadTexts:config_out14.setUnits(_C)
class _Config_out15_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out15_Type.__name__=_B
_Config_out15_Object=MibScalar
config_out15=_Config_out15_Object((1,3,6,1,4,1,9839,2,1,3,111),_Config_out15_Type())
config_out15.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out15.setStatus(_A)
if mibBuilder.loadTexts:config_out15.setUnits(_C)
class _Config_out16_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out16_Type.__name__=_B
_Config_out16_Object=MibScalar
config_out16=_Config_out16_Object((1,3,6,1,4,1,9839,2,1,3,112),_Config_out16_Type())
config_out16.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out16.setStatus(_A)
if mibBuilder.loadTexts:config_out16.setUnits(_C)
class _Config_out17_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out17_Type.__name__=_B
_Config_out17_Object=MibScalar
config_out17=_Config_out17_Object((1,3,6,1,4,1,9839,2,1,3,113),_Config_out17_Type())
config_out17.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out17.setStatus(_A)
if mibBuilder.loadTexts:config_out17.setUnits(_C)
class _Config_out18_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Config_out18_Type.__name__=_B
_Config_out18_Object=MibScalar
config_out18=_Config_out18_Object((1,3,6,1,4,1,9839,2,1,3,114),_Config_out18_Type())
config_out18.setMaxAccess(_D)
if mibBuilder.loadTexts:config_out18.setStatus(_A)
if mibBuilder.loadTexts:config_out18.setUnits(_C)
mibBuilder.exportSymbols('CAREL-fcp-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'unitOnLineStatusGroup':unitOnLineStatusGroup,'unit1-OnLineStatus':unit1_OnLineStatus,'fcpMIB':fcpMIB,'digitalObjects':digitalObjects,'scheda_modem':scheda_modem,'present_expansion':present_expansion,'fan1':fan1,'fan2':fan2,'fan3':fan3,'fan4':fan4,'comp1':comp1,'rich_parz11':rich_parz11,'rich_parz21':rich_parz21,'comp2':comp2,'rich_parz12':rich_parz12,'rich_parz22':rich_parz22,'comp3':comp3,'rich_parz13':rich_parz13,'rich_parz23':rich_parz23,'comp4':comp4,'rich_parz14':rich_parz14,'rich_parz24':rich_parz24,'comp5':comp5,'rich_parz15':rich_parz15,'rich_parz25':rich_parz25,'comp6':comp6,'rich_parz16':rich_parz16,'rich_parz26':rich_parz26,'din1':din1,'din2':din2,'din3':din3,'din4':din4,'din5':din5,'din6':din6,'din7':din7,'din8':din8,'din9':din9,'din10':din10,'din11':din11,'din12':din12,'din13':din13,'din14':din14,'din15':din15,'din16':din16,'din17':din17,'din18':din18,'all_pres_lpres':all_pres_lpres,'all_pres_hpres':all_pres_hpres,'din101':din101,'din102':din102,'din103':din103,'din104':din104,'din105':din105,'din106':din106,'din107':din107,'din108':din108,'mall_term_klix1':mall_term_klix1,'mall_term_klix2':mall_term_klix2,'mall_term_klix3':mall_term_klix3,'mall_term_klix4':mall_term_klix4,'mall_term_klix5':mall_term_klix5,'mall_term_klix6':mall_term_klix6,'mall_pres_h1':mall_pres_h1,'mall_pres_h2':mall_pres_h2,'mall_pres_h3':mall_pres_h3,'mall_pres_h4':mall_pres_h4,'mall_pres_h5':mall_pres_h5,'mall_pres_h6':mall_pres_h6,'mall_dif_olio1':mall_dif_olio1,'mall_dif_olio2':mall_dif_olio2,'mall_dif_olio3':mall_dif_olio3,'mall_dif_olio4':mall_dif_olio4,'mall_dif_olio5':mall_dif_olio5,'mall_dif_olio6':mall_dif_olio6,'mall_ore_comp1':mall_ore_comp1,'mall_ore_comp2':mall_ore_comp2,'mall_ore_comp3':mall_ore_comp3,'mall_ore_comp4':mall_ore_comp4,'mall_ore_comp5':mall_ore_comp5,'mall_ore_comp6':mall_ore_comp6,'mall_term_vent1':mall_term_vent1,'mall_term_vent2':mall_term_vent2,'mall_term_vent3':mall_term_vent3,'mall_term_vent4':mall_term_vent4,'mal_liquid_level':mal_liquid_level,'mall_pres_lpres':mall_pres_lpres,'mall_pres_hpres':mall_pres_hpres,'mal_low2':mal_low2,'mall_alta_mand':mall_alta_mand,'mal_low_press':mal_low_press,'mal_high_press':mal_high_press,'mal_n_input':mal_n_input,'mal_n_devices':mal_n_devices,'mall_ora':mall_ora,'mal_broke_pr1':mal_broke_pr1,'mal_broke_pr2':mal_broke_pr2,'glb_al':glb_al,'syson':syson,'en_off_supervisor':en_off_supervisor,'fan5':fan5,'mall_term_vent5':mall_term_vent5,'en_on_balck_out':en_on_balck_out,'dout1':dout1,'dout2':dout2,'dout3':dout3,'dout4':dout4,'dout5':dout5,'dout6':dout6,'dout7':dout7,'dout8':dout8,'dout9':dout9,'dout10':dout10,'dout11':dout11,'dout12':dout12,'dout13':dout13,'dout14':dout14,'dout15':dout15,'dout16':dout16,'dout17':dout17,'dout18':dout18,'analogObjects':analogObjects,'asp_conv':asp_conv,'press_mand_conv':press_mand_conv,'out_inv_fan':out_inv_fan,'inverter_comp1':inverter_comp1,'set_comp':set_comp,'diff_comp':diff_comp,'set_fan':set_fan,'diff_fan':diff_fan,'voltage_in':voltage_in,'max_set_co':max_set_co,'min_set_co':min_set_co,'max_set_fa':max_set_fa,'min_set_fa':min_set_fa,'thresh_high1':thresh_high1,'diff_high1':diff_high1,'thresh_low1':thresh_low1,'diff_low1':diff_low1,'thresh_high2':thresh_high2,'diff_high2':diff_high2,'thresh_low2':thresh_low2,'diff_low2':diff_low2,'set_vent_inv':set_vent_inv,'diff_vent_inv':diff_vent_inv,'seinverter':seinverter,'diff_inv':diff_inv,'integerObjects':integerObjects,'lhour':lhour,'lminute':lminute,'lday':lday,'lmonth':lmonth,'lyear':lyear,'hour':hour,'minute':minute,'month':month,'pyear':pyear,'oil_diff':oil_diff,'out_inv_fani':out_inv_fani,'inverter_compi1':inverter_compi1,'board_type':board_type,'unit_status':unit_status,'type_b1':type_b1,'type_b2':type_b2,'bios_release':bios_release,'bios_date':bios_date,'boot_release':boot_release,'boot_date':boot_date,'time_switch_on1':time_switch_on1,'time_switchoff1':time_switchoff1,'time_min_on':time_min_on,'time_min_off':time_min_off,'time_betw_comp':time_betw_comp,'time_same_comp':time_same_comp,'unload_delay':unload_delay,'time_switch_on2':time_switch_on2,'time_switchoff2':time_switchoff2,'time_betw_fan':time_betw_fan,'rit_dif_olio':rit_dif_olio,'rit_all_liq':rit_all_liq,'sg_ore_comp':sg_ore_comp,'hour_comp1':hour_comp1,'hour_l_comp1':hour_l_comp1,'hour_comp2':hour_comp2,'hour_l_comp2':hour_l_comp2,'hour_comp3':hour_comp3,'hour_l_comp3':hour_l_comp3,'hour_comp4':hour_comp4,'hour_l_comp4':hour_l_comp4,'hour_comp5':hour_comp5,'hour_l_comp5':hour_l_comp5,'hour_comp6':hour_comp6,'hour_l_comp6':hour_l_comp6,'h_hour_fan1':h_hour_fan1,'l_hour_fan1':l_hour_fan1,'h_hour_fan2':h_hour_fan2,'l_hour_fan2':l_hour_fan2,'h_hour_fan3':h_hour_fan3,'l_hour_fan3':l_hour_fan3,'h_hour_fan4':h_hour_fan4,'l_hour_fan4':l_hour_fan4,'sg_ore_fan':sg_ore_fan,'version':version,'h_hour_fan5':h_hour_fan5,'l_hour_fan5':l_hour_fan5,'time_on_black_out':time_on_black_out,'config_in1':config_in1,'config_in2':config_in2,'config_in3':config_in3,'config_in4':config_in4,'config_in5':config_in5,'config_in6':config_in6,'config_in7':config_in7,'config_in8':config_in8,'config_in9':config_in9,'config_in10':config_in10,'config_in11':config_in11,'config_in12':config_in12,'config_in13':config_in13,'config_in14':config_in14,'config_in15':config_in15,'config_in16':config_in16,'config_in17':config_in17,'config_in18':config_in18,'config_out1':config_out1,'config_out2':config_out2,'config_out3':config_out3,'config_out4':config_out4,'config_out5':config_out5,'config_out6':config_out6,'config_out7':config_out7,'config_out8':config_out8,'config_out9':config_out9,'config_out10':config_out10,'config_out11':config_out11,'config_out12':config_out12,'config_out13':config_out13,'config_out14':config_out14,'config_out15':config_out15,'config_out16':config_out16,'config_out17':config_out17,'config_out18':config_out18})