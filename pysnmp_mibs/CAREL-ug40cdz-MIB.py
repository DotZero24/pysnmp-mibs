_J='min'
_I='degrees C x10'
_H='rH%'
_G='h'
_F='degrees C'
_E='read-write'
_D='N/A'
_C='read-only'
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
ug40cdzMIB=ModuleIdentity((1,3,6,1,4,1,9839,2,1))
if mibBuilder.loadTexts:ug40cdzMIB.setRevisions(('2006-04-11 16:45',))
_Carel_ObjectIdentity=ObjectIdentity
carel=_Carel_ObjectIdentity((1,3,6,1,4,1,9839))
_Systm_ObjectIdentity=ObjectIdentity
systm=_Systm_ObjectIdentity((1,3,6,1,4,1,9839,1))
_AgentRelease_Type=Integer32
_AgentRelease_Object=MibScalar
agentRelease=_AgentRelease_Object((1,3,6,1,4,1,9839,1,1),_AgentRelease_Type())
agentRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRelease.setStatus(_A)
if mibBuilder.loadTexts:agentRelease.setUnits(_D)
_AgentCode_Type=Integer32
_AgentCode_Object=MibScalar
agentCode=_AgentCode_Object((1,3,6,1,4,1,9839,1,2),_AgentCode_Type())
agentCode.setMaxAccess(_C)
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
netSize.setMaxAccess(_E)
if mibBuilder.loadTexts:netSize.setStatus(_A)
if mibBuilder.loadTexts:netSize.setUnits(_D)
class _BaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200))
_BaudRate_Type.__name__=_B
_BaudRate_Object=MibScalar
baudRate=_BaudRate_Object((1,3,6,1,4,1,9839,2,0,1,2),_BaudRate_Type())
baudRate.setMaxAccess(_E)
if mibBuilder.loadTexts:baudRate.setStatus(_A)
if mibBuilder.loadTexts:baudRate.setUnits(_D)
_UnitTypeGroup_ObjectIdentity=ObjectIdentity
unitTypeGroup=_UnitTypeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,2))
_Unit1_Type_Type=DisplayString
_Unit1_Type_Object=MibScalar
unit1_Type=_Unit1_Type_Object((1,3,6,1,4,1,9839,2,0,2,1),_Unit1_Type_Type())
unit1_Type.setMaxAccess(_C)
if mibBuilder.loadTexts:unit1_Type.setStatus(_A)
if mibBuilder.loadTexts:unit1_Type.setUnits(_D)
_UnitCodeGroup_ObjectIdentity=ObjectIdentity
unitCodeGroup=_UnitCodeGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,3))
_Unit1_Code_Type=Integer32
_Unit1_Code_Object=MibScalar
unit1_Code=_Unit1_Code_Object((1,3,6,1,4,1,9839,2,0,3,1),_Unit1_Code_Type())
unit1_Code.setMaxAccess(_C)
if mibBuilder.loadTexts:unit1_Code.setStatus(_A)
if mibBuilder.loadTexts:unit1_Code.setUnits(_D)
_UnitSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitSoftwareReleaseGroup=_UnitSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,4))
_Unit1_SoftwareRelease_Type=Integer32
_Unit1_SoftwareRelease_Object=MibScalar
unit1_SoftwareRelease=_Unit1_SoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,4,1),_Unit1_SoftwareRelease_Type())
unit1_SoftwareRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_SoftwareRelease.setUnits(_D)
_UnitMinSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMinSoftwareReleaseGroup=_UnitMinSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,5))
_Unit1_MinSoftwareRelease_Type=Integer32
_Unit1_MinSoftwareRelease_Object=MibScalar
unit1_MinSoftwareRelease=_Unit1_MinSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,5,1),_Unit1_MinSoftwareRelease_Type())
unit1_MinSoftwareRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MinSoftwareRelease.setUnits(_D)
_UnitMaxSoftwareReleaseGroup_ObjectIdentity=ObjectIdentity
unitMaxSoftwareReleaseGroup=_UnitMaxSoftwareReleaseGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,6))
_Unit1_MaxSoftwareRelease_Type=Integer32
_Unit1_MaxSoftwareRelease_Object=MibScalar
unit1_MaxSoftwareRelease=_Unit1_MaxSoftwareRelease_Object((1,3,6,1,4,1,9839,2,0,6,1),_Unit1_MaxSoftwareRelease_Type())
unit1_MaxSoftwareRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setStatus(_A)
if mibBuilder.loadTexts:unit1_MaxSoftwareRelease.setUnits(_D)
_UnitNoAnswerCounterGroup_ObjectIdentity=ObjectIdentity
unitNoAnswerCounterGroup=_UnitNoAnswerCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,7))
_Unit1_NoAnswerCounter_Type=Integer32
_Unit1_NoAnswerCounter_Object=MibScalar
unit1_NoAnswerCounter=_Unit1_NoAnswerCounter_Object((1,3,6,1,4,1,9839,2,0,7,1),_Unit1_NoAnswerCounter_Type())
unit1_NoAnswerCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_NoAnswerCounter.setUnits(_D)
_UnitErrorChecksumCounterGroup_ObjectIdentity=ObjectIdentity
unitErrorChecksumCounterGroup=_UnitErrorChecksumCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,8))
_Unit1_ErrorChecksumCounter_Type=Integer32
_Unit1_ErrorChecksumCounter_Object=MibScalar
unit1_ErrorChecksumCounter=_Unit1_ErrorChecksumCounter_Object((1,3,6,1,4,1,9839,2,0,8,1),_Unit1_ErrorChecksumCounter_Type())
unit1_ErrorChecksumCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_ErrorChecksumCounter.setUnits(_D)
_UnitTimeoutCounterGroup_ObjectIdentity=ObjectIdentity
unitTimeoutCounterGroup=_UnitTimeoutCounterGroup_ObjectIdentity((1,3,6,1,4,1,9839,2,0,9))
_Unit1_TimeoutCounter_Type=Integer32
_Unit1_TimeoutCounter_Object=MibScalar
unit1_TimeoutCounter=_Unit1_TimeoutCounter_Object((1,3,6,1,4,1,9839,2,0,9,1),_Unit1_TimeoutCounter_Type())
unit1_TimeoutCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setStatus(_A)
if mibBuilder.loadTexts:unit1_TimeoutCounter.setUnits(_D)
_DigitalObjects_ObjectIdentity=ObjectIdentity
digitalObjects=_DigitalObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,1))
class _SystemOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SystemOn_Type.__name__=_B
_SystemOn_Object=MibScalar
systemOn=_SystemOn_Object((1,3,6,1,4,1,9839,2,1,1,1),_SystemOn_Type())
systemOn.setMaxAccess(_C)
if mibBuilder.loadTexts:systemOn.setStatus(_A)
if mibBuilder.loadTexts:systemOn.setUnits(_D)
class _Compressore1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressore1_Type.__name__=_B
_Compressore1_Object=MibScalar
compressore1=_Compressore1_Object((1,3,6,1,4,1,9839,2,1,1,2),_Compressore1_Type())
compressore1.setMaxAccess(_C)
if mibBuilder.loadTexts:compressore1.setStatus(_A)
if mibBuilder.loadTexts:compressore1.setUnits(_D)
class _Compressore2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressore2_Type.__name__=_B
_Compressore2_Object=MibScalar
compressore2=_Compressore2_Object((1,3,6,1,4,1,9839,2,1,1,3),_Compressore2_Type())
compressore2.setMaxAccess(_C)
if mibBuilder.loadTexts:compressore2.setStatus(_A)
if mibBuilder.loadTexts:compressore2.setUnits(_D)
class _Compressore3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressore3_Type.__name__=_B
_Compressore3_Object=MibScalar
compressore3=_Compressore3_Object((1,3,6,1,4,1,9839,2,1,1,4),_Compressore3_Type())
compressore3.setMaxAccess(_C)
if mibBuilder.loadTexts:compressore3.setStatus(_A)
if mibBuilder.loadTexts:compressore3.setUnits(_D)
class _Compressore4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Compressore4_Type.__name__=_B
_Compressore4_Object=MibScalar
compressore4=_Compressore4_Object((1,3,6,1,4,1,9839,2,1,1,5),_Compressore4_Type())
compressore4.setMaxAccess(_C)
if mibBuilder.loadTexts:compressore4.setStatus(_A)
if mibBuilder.loadTexts:compressore4.setUnits(_D)
class _Heating1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Heating1_Type.__name__=_B
_Heating1_Object=MibScalar
heating1=_Heating1_Object((1,3,6,1,4,1,9839,2,1,1,6),_Heating1_Type())
heating1.setMaxAccess(_C)
if mibBuilder.loadTexts:heating1.setStatus(_A)
if mibBuilder.loadTexts:heating1.setUnits(_D)
class _Heating2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Heating2_Type.__name__=_B
_Heating2_Object=MibScalar
heating2=_Heating2_Object((1,3,6,1,4,1,9839,2,1,1,7),_Heating2_Type())
heating2.setMaxAccess(_C)
if mibBuilder.loadTexts:heating2.setStatus(_A)
if mibBuilder.loadTexts:heating2.setUnits(_D)
class _HotGasCoil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HotGasCoil_Type.__name__=_B
_HotGasCoil_Object=MibScalar
hotGasCoil=_HotGasCoil_Object((1,3,6,1,4,1,9839,2,1,1,9),_HotGasCoil_Type())
hotGasCoil.setMaxAccess(_C)
if mibBuilder.loadTexts:hotGasCoil.setStatus(_A)
if mibBuilder.loadTexts:hotGasCoil.setUnits(_D)
class _Dehumidification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Dehumidification_Type.__name__=_B
_Dehumidification_Object=MibScalar
dehumidification=_Dehumidification_Object((1,3,6,1,4,1,9839,2,1,1,10),_Dehumidification_Type())
dehumidification.setMaxAccess(_C)
if mibBuilder.loadTexts:dehumidification.setStatus(_A)
if mibBuilder.loadTexts:dehumidification.setUnits(_D)
class _Humidification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Humidification_Type.__name__=_B
_Humidification_Object=MibScalar
humidification=_Humidification_Object((1,3,6,1,4,1,9839,2,1,1,11),_Humidification_Type())
humidification.setMaxAccess(_C)
if mibBuilder.loadTexts:humidification.setStatus(_A)
if mibBuilder.loadTexts:humidification.setUnits(_D)
class _Emerg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Emerg_Type.__name__=_B
_Emerg_Object=MibScalar
emerg=_Emerg_Object((1,3,6,1,4,1,9839,2,1,1,12),_Emerg_Type())
emerg.setMaxAccess(_C)
if mibBuilder.loadTexts:emerg.setStatus(_A)
if mibBuilder.loadTexts:emerg.setUnits(_D)
class _AlarmAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmAccess_Type.__name__=_B
_AlarmAccess_Object=MibScalar
alarmAccess=_AlarmAccess_Object((1,3,6,1,4,1,9839,2,1,1,20),_AlarmAccess_Type())
alarmAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmAccess.setStatus(_A)
if mibBuilder.loadTexts:alarmAccess.setUnits(_D)
class _AlarmRoomHT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmRoomHT_Type.__name__=_B
_AlarmRoomHT_Object=MibScalar
alarmRoomHT=_AlarmRoomHT_Object((1,3,6,1,4,1,9839,2,1,1,21),_AlarmRoomHT_Type())
alarmRoomHT.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmRoomHT.setStatus(_A)
if mibBuilder.loadTexts:alarmRoomHT.setUnits(_D)
class _AlarmRoomLT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmRoomLT_Type.__name__=_B
_AlarmRoomLT_Object=MibScalar
alarmRoomLT=_AlarmRoomLT_Object((1,3,6,1,4,1,9839,2,1,1,22),_AlarmRoomLT_Type())
alarmRoomLT.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmRoomLT.setStatus(_A)
if mibBuilder.loadTexts:alarmRoomLT.setUnits(_D)
class _AlarmRoomHH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmRoomHH_Type.__name__=_B
_AlarmRoomHH_Object=MibScalar
alarmRoomHH=_AlarmRoomHH_Object((1,3,6,1,4,1,9839,2,1,1,23),_AlarmRoomHH_Type())
alarmRoomHH.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmRoomHH.setStatus(_A)
if mibBuilder.loadTexts:alarmRoomHH.setUnits(_D)
class _AlarmRoomLH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmRoomLH_Type.__name__=_B
_AlarmRoomLH_Object=MibScalar
alarmRoomLH=_AlarmRoomLH_Object((1,3,6,1,4,1,9839,2,1,1,24),_AlarmRoomLH_Type())
alarmRoomLH.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmRoomLH.setStatus(_A)
if mibBuilder.loadTexts:alarmRoomLH.setUnits(_D)
class _AlarmRoomEAP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmRoomEAP_Type.__name__=_B
_AlarmRoomEAP_Object=MibScalar
alarmRoomEAP=_AlarmRoomEAP_Object((1,3,6,1,4,1,9839,2,1,1,25),_AlarmRoomEAP_Type())
alarmRoomEAP.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmRoomEAP.setStatus(_A)
if mibBuilder.loadTexts:alarmRoomEAP.setUnits(_D)
class _AlarmFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmFilter_Type.__name__=_B
_AlarmFilter_Object=MibScalar
alarmFilter=_AlarmFilter_Object((1,3,6,1,4,1,9839,2,1,1,26),_AlarmFilter_Type())
alarmFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmFilter.setStatus(_A)
if mibBuilder.loadTexts:alarmFilter.setUnits(_D)
class _AlarmFlood_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmFlood_Type.__name__=_B
_AlarmFlood_Object=MibScalar
alarmFlood=_AlarmFlood_Object((1,3,6,1,4,1,9839,2,1,1,27),_AlarmFlood_Type())
alarmFlood.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmFlood.setStatus(_A)
if mibBuilder.loadTexts:alarmFlood.setUnits(_D)
class _AlarmAirFlow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmAirFlow_Type.__name__=_B
_AlarmAirFlow_Object=MibScalar
alarmAirFlow=_AlarmAirFlow_Object((1,3,6,1,4,1,9839,2,1,1,28),_AlarmAirFlow_Type())
alarmAirFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmAirFlow.setStatus(_A)
if mibBuilder.loadTexts:alarmAirFlow.setUnits(_D)
class _AlarmHeater_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHeater_Type.__name__=_B
_AlarmHeater_Object=MibScalar
alarmHeater=_AlarmHeater_Object((1,3,6,1,4,1,9839,2,1,1,29),_AlarmHeater_Type())
alarmHeater.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHeater.setStatus(_A)
if mibBuilder.loadTexts:alarmHeater.setUnits(_D)
class _AlarmHP1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHP1_Type.__name__=_B
_AlarmHP1_Object=MibScalar
alarmHP1=_AlarmHP1_Object((1,3,6,1,4,1,9839,2,1,1,30),_AlarmHP1_Type())
alarmHP1.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHP1.setStatus(_A)
if mibBuilder.loadTexts:alarmHP1.setUnits(_D)
class _AlarmHP2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHP2_Type.__name__=_B
_AlarmHP2_Object=MibScalar
alarmHP2=_AlarmHP2_Object((1,3,6,1,4,1,9839,2,1,1,31),_AlarmHP2_Type())
alarmHP2.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHP2.setStatus(_A)
if mibBuilder.loadTexts:alarmHP2.setUnits(_D)
class _AlarmLP1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmLP1_Type.__name__=_B
_AlarmLP1_Object=MibScalar
alarmLP1=_AlarmLP1_Object((1,3,6,1,4,1,9839,2,1,1,32),_AlarmLP1_Type())
alarmLP1.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLP1.setStatus(_A)
if mibBuilder.loadTexts:alarmLP1.setUnits(_D)
class _AlarmLP2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmLP2_Type.__name__=_B
_AlarmLP2_Object=MibScalar
alarmLP2=_AlarmLP2_Object((1,3,6,1,4,1,9839,2,1,1,33),_AlarmLP2_Type())
alarmLP2.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLP2.setStatus(_A)
if mibBuilder.loadTexts:alarmLP2.setUnits(_D)
class _AlarmEXV1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmEXV1_Type.__name__=_B
_AlarmEXV1_Object=MibScalar
alarmEXV1=_AlarmEXV1_Object((1,3,6,1,4,1,9839,2,1,1,34),_AlarmEXV1_Type())
alarmEXV1.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmEXV1.setStatus(_A)
if mibBuilder.loadTexts:alarmEXV1.setUnits(_D)
class _AlarmEXV2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmEXV2_Type.__name__=_B
_AlarmEXV2_Object=MibScalar
alarmEXV2=_AlarmEXV2_Object((1,3,6,1,4,1,9839,2,1,1,35),_AlarmEXV2_Type())
alarmEXV2.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmEXV2.setStatus(_A)
if mibBuilder.loadTexts:alarmEXV2.setUnits(_D)
class _AlarmPSE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmPSE_Type.__name__=_B
_AlarmPSE_Object=MibScalar
alarmPSE=_AlarmPSE_Object((1,3,6,1,4,1,9839,2,1,1,36),_AlarmPSE_Type())
alarmPSE.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmPSE.setStatus(_A)
if mibBuilder.loadTexts:alarmPSE.setUnits(_D)
class _AlarmSmokeFire_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmSmokeFire_Type.__name__=_B
_AlarmSmokeFire_Object=MibScalar
alarmSmokeFire=_AlarmSmokeFire_Object((1,3,6,1,4,1,9839,2,1,1,37),_AlarmSmokeFire_Type())
alarmSmokeFire.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmSmokeFire.setStatus(_A)
if mibBuilder.loadTexts:alarmSmokeFire.setUnits(_D)
class _AlarmLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmLAN_Type.__name__=_B
_AlarmLAN_Object=MibScalar
alarmLAN=_AlarmLAN_Object((1,3,6,1,4,1,9839,2,1,1,38),_AlarmLAN_Type())
alarmLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLAN.setStatus(_A)
if mibBuilder.loadTexts:alarmLAN.setUnits(_D)
class _AlarmHUHC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHUHC_Type.__name__=_B
_AlarmHUHC_Object=MibScalar
alarmHUHC=_AlarmHUHC_Object((1,3,6,1,4,1,9839,2,1,1,39),_AlarmHUHC_Type())
alarmHUHC.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHUHC.setStatus(_A)
if mibBuilder.loadTexts:alarmHUHC.setUnits(_D)
class _AlarmHUPL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHUPL_Type.__name__=_B
_AlarmHUPL_Object=MibScalar
alarmHUPL=_AlarmHUPL_Object((1,3,6,1,4,1,9839,2,1,1,40),_AlarmHUPL_Type())
alarmHUPL.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHUPL.setStatus(_A)
if mibBuilder.loadTexts:alarmHUPL.setUnits(_D)
class _AlarmHUWL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHUWL_Type.__name__=_B
_AlarmHUWL_Object=MibScalar
alarmHUWL=_AlarmHUWL_Object((1,3,6,1,4,1,9839,2,1,1,41),_AlarmHUWL_Type())
alarmHUWL.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHUWL.setStatus(_A)
if mibBuilder.loadTexts:alarmHUWL.setUnits(_D)
class _AlarmCWDHT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmCWDHT_Type.__name__=_B
_AlarmCWDHT_Object=MibScalar
alarmCWDHT=_AlarmCWDHT_Object((1,3,6,1,4,1,9839,2,1,1,42),_AlarmCWDHT_Type())
alarmCWDHT.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCWDHT.setStatus(_A)
if mibBuilder.loadTexts:alarmCWDHT.setUnits(_D)
class _AlarmCWF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmCWF_Type.__name__=_B
_AlarmCWF_Object=MibScalar
alarmCWF=_AlarmCWF_Object((1,3,6,1,4,1,9839,2,1,1,43),_AlarmCWF_Type())
alarmCWF.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCWF.setStatus(_A)
if mibBuilder.loadTexts:alarmCWF.setUnits(_D)
class _AlarmCWFF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmCWFF_Type.__name__=_B
_AlarmCWFF_Object=MibScalar
alarmCWFF=_AlarmCWFF_Object((1,3,6,1,4,1,9839,2,1,1,44),_AlarmCWFF_Type())
alarmCWFF.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCWFF.setStatus(_A)
if mibBuilder.loadTexts:alarmCWFF.setUnits(_D)
class _AlarmCWHT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmCWHT_Type.__name__=_B
_AlarmCWHT_Object=MibScalar
alarmCWHT=_AlarmCWHT_Object((1,3,6,1,4,1,9839,2,1,1,45),_AlarmCWHT_Type())
alarmCWHT.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCWHT.setStatus(_A)
if mibBuilder.loadTexts:alarmCWHT.setUnits(_D)
class _AlarmRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmRTS_Type.__name__=_B
_AlarmRTS_Object=MibScalar
alarmRTS=_AlarmRTS_Object((1,3,6,1,4,1,9839,2,1,1,46),_AlarmRTS_Type())
alarmRTS.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmRTS.setStatus(_A)
if mibBuilder.loadTexts:alarmRTS.setUnits(_D)
class _AlarmHWS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHWS_Type.__name__=_B
_AlarmHWS_Object=MibScalar
alarmHWS=_AlarmHWS_Object((1,3,6,1,4,1,9839,2,1,1,47),_AlarmHWS_Type())
alarmHWS.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHWS.setStatus(_A)
if mibBuilder.loadTexts:alarmHWS.setUnits(_D)
class _AlarmCWS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmCWS_Type.__name__=_B
_AlarmCWS_Object=MibScalar
alarmCWS=_AlarmCWS_Object((1,3,6,1,4,1,9839,2,1,1,48),_AlarmCWS_Type())
alarmCWS.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCWS.setStatus(_A)
if mibBuilder.loadTexts:alarmCWS.setUnits(_D)
class _AlarmOTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmOTS_Type.__name__=_B
_AlarmOTS_Object=MibScalar
alarmOTS=_AlarmOTS_Object((1,3,6,1,4,1,9839,2,1,1,49),_AlarmOTS_Type())
alarmOTS.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmOTS.setStatus(_A)
if mibBuilder.loadTexts:alarmOTS.setUnits(_D)
class _AlarmDTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmDTS_Type.__name__=_B
_AlarmDTS_Object=MibScalar
alarmDTS=_AlarmDTS_Object((1,3,6,1,4,1,9839,2,1,1,50),_AlarmDTS_Type())
alarmDTS.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmDTS.setStatus(_A)
if mibBuilder.loadTexts:alarmDTS.setUnits(_D)
class _AlarmRHS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmRHS_Type.__name__=_B
_AlarmRHS_Object=MibScalar
alarmRHS=_AlarmRHS_Object((1,3,6,1,4,1,9839,2,1,1,51),_AlarmRHS_Type())
alarmRHS.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmRHS.setStatus(_A)
if mibBuilder.loadTexts:alarmRHS.setUnits(_D)
class _AlarmCWOTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmCWOTS_Type.__name__=_B
_AlarmCWOTS_Object=MibScalar
alarmCWOTS=_AlarmCWOTS_Object((1,3,6,1,4,1,9839,2,1,1,52),_AlarmCWOTS_Type())
alarmCWOTS.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmCWOTS.setStatus(_A)
if mibBuilder.loadTexts:alarmCWOTS.setUnits(_D)
class _AlarmC1Hours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmC1Hours_Type.__name__=_B
_AlarmC1Hours_Object=MibScalar
alarmC1Hours=_AlarmC1Hours_Object((1,3,6,1,4,1,9839,2,1,1,53),_AlarmC1Hours_Type())
alarmC1Hours.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmC1Hours.setStatus(_A)
if mibBuilder.loadTexts:alarmC1Hours.setUnits(_D)
class _AlarmC2Hours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmC2Hours_Type.__name__=_B
_AlarmC2Hours_Object=MibScalar
alarmC2Hours=_AlarmC2Hours_Object((1,3,6,1,4,1,9839,2,1,1,54),_AlarmC2Hours_Type())
alarmC2Hours.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmC2Hours.setStatus(_A)
if mibBuilder.loadTexts:alarmC2Hours.setUnits(_D)
class _AlarmC3Hours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmC3Hours_Type.__name__=_B
_AlarmC3Hours_Object=MibScalar
alarmC3Hours=_AlarmC3Hours_Object((1,3,6,1,4,1,9839,2,1,1,55),_AlarmC3Hours_Type())
alarmC3Hours.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmC3Hours.setStatus(_A)
if mibBuilder.loadTexts:alarmC3Hours.setUnits(_D)
class _AlarmC4Hours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmC4Hours_Type.__name__=_B
_AlarmC4Hours_Object=MibScalar
alarmC4Hours=_AlarmC4Hours_Object((1,3,6,1,4,1,9839,2,1,1,56),_AlarmC4Hours_Type())
alarmC4Hours.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmC4Hours.setStatus(_A)
if mibBuilder.loadTexts:alarmC4Hours.setUnits(_D)
class _AlarmFilterHours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmFilterHours_Type.__name__=_B
_AlarmFilterHours_Object=MibScalar
alarmFilterHours=_AlarmFilterHours_Object((1,3,6,1,4,1,9839,2,1,1,57),_AlarmFilterHours_Type())
alarmFilterHours.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmFilterHours.setStatus(_A)
if mibBuilder.loadTexts:alarmFilterHours.setUnits(_D)
class _AlarmHeat1Hours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHeat1Hours_Type.__name__=_B
_AlarmHeat1Hours_Object=MibScalar
alarmHeat1Hours=_AlarmHeat1Hours_Object((1,3,6,1,4,1,9839,2,1,1,58),_AlarmHeat1Hours_Type())
alarmHeat1Hours.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHeat1Hours.setStatus(_A)
if mibBuilder.loadTexts:alarmHeat1Hours.setUnits(_D)
class _AlarmHeat2Hours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHeat2Hours_Type.__name__=_B
_AlarmHeat2Hours_Object=MibScalar
alarmHeat2Hours=_AlarmHeat2Hours_Object((1,3,6,1,4,1,9839,2,1,1,59),_AlarmHeat2Hours_Type())
alarmHeat2Hours.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHeat2Hours.setStatus(_A)
if mibBuilder.loadTexts:alarmHeat2Hours.setUnits(_D)
class _AlarmHumHours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHumHours_Type.__name__=_B
_AlarmHumHours_Object=MibScalar
alarmHumHours=_AlarmHumHours_Object((1,3,6,1,4,1,9839,2,1,1,60),_AlarmHumHours_Type())
alarmHumHours.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHumHours.setStatus(_A)
if mibBuilder.loadTexts:alarmHumHours.setUnits(_D)
class _AlarmUnitHours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmUnitHours_Type.__name__=_B
_AlarmUnitHours_Object=MibScalar
alarmUnitHours=_AlarmUnitHours_Object((1,3,6,1,4,1,9839,2,1,1,61),_AlarmUnitHours_Type())
alarmUnitHours.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmUnitHours.setStatus(_A)
if mibBuilder.loadTexts:alarmUnitHours.setUnits(_D)
class _AlarmDI2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmDI2_Type.__name__=_B
_AlarmDI2_Object=MibScalar
alarmDI2=_AlarmDI2_Object((1,3,6,1,4,1,9839,2,1,1,62),_AlarmDI2_Type())
alarmDI2.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmDI2.setStatus(_A)
if mibBuilder.loadTexts:alarmDI2.setUnits(_D)
class _AlarmDI4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmDI4_Type.__name__=_B
_AlarmDI4_Object=MibScalar
alarmDI4=_AlarmDI4_Object((1,3,6,1,4,1,9839,2,1,1,63),_AlarmDI4_Type())
alarmDI4.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmDI4.setStatus(_A)
if mibBuilder.loadTexts:alarmDI4.setUnits(_D)
class _AlarmDI6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmDI6_Type.__name__=_B
_AlarmDI6_Object=MibScalar
alarmDI6=_AlarmDI6_Object((1,3,6,1,4,1,9839,2,1,1,64),_AlarmDI6_Type())
alarmDI6.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmDI6.setStatus(_A)
if mibBuilder.loadTexts:alarmDI6.setUnits(_D)
class _AlarmHum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmHum_Type.__name__=_B
_AlarmHum_Object=MibScalar
alarmHum=_AlarmHum_Object((1,3,6,1,4,1,9839,2,1,1,65),_AlarmHum_Type())
alarmHum.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmHum.setStatus(_A)
if mibBuilder.loadTexts:alarmHum.setUnits(_D)
class _AlarmGeneral_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmGeneral_Type.__name__=_B
_AlarmGeneral_Object=MibScalar
alarmGeneral=_AlarmGeneral_Object((1,3,6,1,4,1,9839,2,1,1,66),_AlarmGeneral_Type())
alarmGeneral.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmGeneral.setStatus(_A)
if mibBuilder.loadTexts:alarmGeneral.setUnits(_D)
class _Alarm2ndLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Alarm2ndLevel_Type.__name__=_B
_Alarm2ndLevel_Object=MibScalar
alarm2ndLevel=_Alarm2ndLevel_Object((1,3,6,1,4,1,9839,2,1,1,67),_Alarm2ndLevel_Type())
alarm2ndLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:alarm2ndLevel.setStatus(_A)
if mibBuilder.loadTexts:alarm2ndLevel.setUnits(_D)
class _AlarmA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmA_Type.__name__=_B
_AlarmA_Object=MibScalar
alarmA=_AlarmA_Object((1,3,6,1,4,1,9839,2,1,1,68),_AlarmA_Type())
alarmA.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmA.setStatus(_A)
if mibBuilder.loadTexts:alarmA.setUnits(_D)
class _AlarmB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmB_Type.__name__=_B
_AlarmB_Object=MibScalar
alarmB=_AlarmB_Object((1,3,6,1,4,1,9839,2,1,1,69),_AlarmB_Type())
alarmB.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmB.setStatus(_A)
if mibBuilder.loadTexts:alarmB.setUnits(_D)
class _AlarmC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlarmC_Type.__name__=_B
_AlarmC_Object=MibScalar
alarmC=_AlarmC_Object((1,3,6,1,4,1,9839,2,1,1,70),_AlarmC_Type())
alarmC.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmC.setStatus(_A)
if mibBuilder.loadTexts:alarmC.setUnits(_D)
class _SelDXCW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SelDXCW_Type.__name__=_B
_SelDXCW_Object=MibScalar
selDXCW=_SelDXCW_Object((1,3,6,1,4,1,9839,2,1,1,71),_SelDXCW_Type())
selDXCW.setMaxAccess(_E)
if mibBuilder.loadTexts:selDXCW.setStatus(_A)
if mibBuilder.loadTexts:selDXCW.setUnits(_D)
class _SelSW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SelSW_Type.__name__=_B
_SelSW_Object=MibScalar
selSW=_SelSW_Object((1,3,6,1,4,1,9839,2,1,1,72),_SelSW_Type())
selSW.setMaxAccess(_E)
if mibBuilder.loadTexts:selSW.setStatus(_A)
if mibBuilder.loadTexts:selSW.setUnits(_D)
class _SystemOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SystemOnOff_Type.__name__=_B
_SystemOnOff_Object=MibScalar
systemOnOff=_SystemOnOff_Object((1,3,6,1,4,1,9839,2,1,1,75),_SystemOnOff_Type())
systemOnOff.setMaxAccess(_E)
if mibBuilder.loadTexts:systemOnOff.setStatus(_A)
if mibBuilder.loadTexts:systemOnOff.setUnits(_D)
class _ResetAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetAlarm_Type.__name__=_B
_ResetAlarm_Object=MibScalar
resetAlarm=_ResetAlarm_Object((1,3,6,1,4,1,9839,2,1,1,76),_ResetAlarm_Type())
resetAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:resetAlarm.setStatus(_A)
if mibBuilder.loadTexts:resetAlarm.setUnits(_D)
class _ResetHrsFilt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetHrsFilt_Type.__name__=_B
_ResetHrsFilt_Object=MibScalar
resetHrsFilt=_ResetHrsFilt_Object((1,3,6,1,4,1,9839,2,1,1,77),_ResetHrsFilt_Type())
resetHrsFilt.setMaxAccess(_E)
if mibBuilder.loadTexts:resetHrsFilt.setStatus(_A)
if mibBuilder.loadTexts:resetHrsFilt.setUnits(_D)
class _ResetHrC1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetHrC1_Type.__name__=_B
_ResetHrC1_Object=MibScalar
resetHrC1=_ResetHrC1_Object((1,3,6,1,4,1,9839,2,1,1,78),_ResetHrC1_Type())
resetHrC1.setMaxAccess(_E)
if mibBuilder.loadTexts:resetHrC1.setStatus(_A)
if mibBuilder.loadTexts:resetHrC1.setUnits(_D)
class _ResetHrC2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetHrC2_Type.__name__=_B
_ResetHrC2_Object=MibScalar
resetHrC2=_ResetHrC2_Object((1,3,6,1,4,1,9839,2,1,1,79),_ResetHrC2_Type())
resetHrC2.setMaxAccess(_E)
if mibBuilder.loadTexts:resetHrC2.setStatus(_A)
if mibBuilder.loadTexts:resetHrC2.setUnits(_D)
class _ResetHrC3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetHrC3_Type.__name__=_B
_ResetHrC3_Object=MibScalar
resetHrC3=_ResetHrC3_Object((1,3,6,1,4,1,9839,2,1,1,80),_ResetHrC3_Type())
resetHrC3.setMaxAccess(_E)
if mibBuilder.loadTexts:resetHrC3.setStatus(_A)
if mibBuilder.loadTexts:resetHrC3.setUnits(_D)
class _ResetHrC4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetHrC4_Type.__name__=_B
_ResetHrC4_Object=MibScalar
resetHrC4=_ResetHrC4_Object((1,3,6,1,4,1,9839,2,1,1,81),_ResetHrC4_Type())
resetHrC4.setMaxAccess(_E)
if mibBuilder.loadTexts:resetHrC4.setStatus(_A)
if mibBuilder.loadTexts:resetHrC4.setUnits(_D)
class _ResetStC1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetStC1_Type.__name__=_B
_ResetStC1_Object=MibScalar
resetStC1=_ResetStC1_Object((1,3,6,1,4,1,9839,2,1,1,82),_ResetStC1_Type())
resetStC1.setMaxAccess(_E)
if mibBuilder.loadTexts:resetStC1.setStatus(_A)
if mibBuilder.loadTexts:resetStC1.setUnits(_D)
class _ResetStC2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetStC2_Type.__name__=_B
_ResetStC2_Object=MibScalar
resetStC2=_ResetStC2_Object((1,3,6,1,4,1,9839,2,1,1,83),_ResetStC2_Type())
resetStC2.setMaxAccess(_E)
if mibBuilder.loadTexts:resetStC2.setStatus(_A)
if mibBuilder.loadTexts:resetStC2.setUnits(_D)
class _ResetStC3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetStC3_Type.__name__=_B
_ResetStC3_Object=MibScalar
resetStC3=_ResetStC3_Object((1,3,6,1,4,1,9839,2,1,1,84),_ResetStC3_Type())
resetStC3.setMaxAccess(_E)
if mibBuilder.loadTexts:resetStC3.setStatus(_A)
if mibBuilder.loadTexts:resetStC3.setUnits(_D)
class _ResetStC4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetStC4_Type.__name__=_B
_ResetStC4_Object=MibScalar
resetStC4=_ResetStC4_Object((1,3,6,1,4,1,9839,2,1,1,85),_ResetStC4_Type())
resetStC4.setMaxAccess(_E)
if mibBuilder.loadTexts:resetStC4.setStatus(_A)
if mibBuilder.loadTexts:resetStC4.setUnits(_D)
class _ResetHrH1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetHrH1_Type.__name__=_B
_ResetHrH1_Object=MibScalar
resetHrH1=_ResetHrH1_Object((1,3,6,1,4,1,9839,2,1,1,86),_ResetHrH1_Type())
resetHrH1.setMaxAccess(_E)
if mibBuilder.loadTexts:resetHrH1.setStatus(_A)
if mibBuilder.loadTexts:resetHrH1.setUnits(_D)
class _ResetHrH2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetHrH2_Type.__name__=_B
_ResetHrH2_Object=MibScalar
resetHrH2=_ResetHrH2_Object((1,3,6,1,4,1,9839,2,1,1,87),_ResetHrH2_Type())
resetHrH2.setMaxAccess(_E)
if mibBuilder.loadTexts:resetHrH2.setStatus(_A)
if mibBuilder.loadTexts:resetHrH2.setUnits(_D)
class _ResetStH1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetStH1_Type.__name__=_B
_ResetStH1_Object=MibScalar
resetStH1=_ResetStH1_Object((1,3,6,1,4,1,9839,2,1,1,88),_ResetStH1_Type())
resetStH1.setMaxAccess(_E)
if mibBuilder.loadTexts:resetStH1.setStatus(_A)
if mibBuilder.loadTexts:resetStH1.setUnits(_D)
class _ResetStH2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetStH2_Type.__name__=_B
_ResetStH2_Object=MibScalar
resetStH2=_ResetStH2_Object((1,3,6,1,4,1,9839,2,1,1,89),_ResetStH2_Type())
resetStH2.setMaxAccess(_E)
if mibBuilder.loadTexts:resetStH2.setStatus(_A)
if mibBuilder.loadTexts:resetStH2.setUnits(_D)
class _ResetHrHU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetHrHU_Type.__name__=_B
_ResetHrHU_Object=MibScalar
resetHrHU=_ResetHrHU_Object((1,3,6,1,4,1,9839,2,1,1,90),_ResetHrHU_Type())
resetHrHU.setMaxAccess(_E)
if mibBuilder.loadTexts:resetHrHU.setStatus(_A)
if mibBuilder.loadTexts:resetHrHU.setUnits(_D)
class _ResetStHU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetStHU_Type.__name__=_B
_ResetStHU_Object=MibScalar
resetStHU=_ResetStHU_Object((1,3,6,1,4,1,9839,2,1,1,91),_ResetStHU_Type())
resetStHU.setMaxAccess(_E)
if mibBuilder.loadTexts:resetStHU.setStatus(_A)
if mibBuilder.loadTexts:resetStHU.setUnits(_D)
class _ResetHrACU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ResetHrACU_Type.__name__=_B
_ResetHrACU_Object=MibScalar
resetHrACU=_ResetHrACU_Object((1,3,6,1,4,1,9839,2,1,1,92),_ResetHrACU_Type())
resetHrACU.setMaxAccess(_E)
if mibBuilder.loadTexts:resetHrACU.setStatus(_A)
if mibBuilder.loadTexts:resetHrACU.setUnits(_D)
class _Sleepmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Sleepmode_Type.__name__=_B
_Sleepmode_Object=MibScalar
sleepmode=_Sleepmode_Object((1,3,6,1,4,1,9839,2,1,1,95),_Sleepmode_Type())
sleepmode.setMaxAccess(_E)
if mibBuilder.loadTexts:sleepmode.setStatus(_A)
if mibBuilder.loadTexts:sleepmode.setUnits(_D)
class _Smtest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Smtest_Type.__name__=_B
_Smtest_Object=MibScalar
smtest=_Smtest_Object((1,3,6,1,4,1,9839,2,1,1,96),_Smtest_Type())
smtest.setMaxAccess(_E)
if mibBuilder.loadTexts:smtest.setStatus(_A)
if mibBuilder.loadTexts:smtest.setUnits(_D)
class _EnablemeanT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_EnablemeanT_Type.__name__=_B
_EnablemeanT_Object=MibScalar
enablemeanT=_EnablemeanT_Object((1,3,6,1,4,1,9839,2,1,1,97),_EnablemeanT_Type())
enablemeanT.setMaxAccess(_E)
if mibBuilder.loadTexts:enablemeanT.setStatus(_A)
if mibBuilder.loadTexts:enablemeanT.setUnits(_D)
_AnalogObjects_ObjectIdentity=ObjectIdentity
analogObjects=_AnalogObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,2))
class _RoomTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_RoomTemp_Type.__name__=_B
_RoomTemp_Object=MibScalar
roomTemp=_RoomTemp_Object((1,3,6,1,4,1,9839,2,1,2,1),_RoomTemp_Type())
roomTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:roomTemp.setStatus(_A)
if mibBuilder.loadTexts:roomTemp.setUnits(_F)
class _OutdoorTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_OutdoorTemp_Type.__name__=_B
_OutdoorTemp_Object=MibScalar
outdoorTemp=_OutdoorTemp_Object((1,3,6,1,4,1,9839,2,1,2,2),_OutdoorTemp_Type())
outdoorTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:outdoorTemp.setStatus(_A)
if mibBuilder.loadTexts:outdoorTemp.setUnits(_F)
class _DeliveryTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_DeliveryTemp_Type.__name__=_B
_DeliveryTemp_Object=MibScalar
deliveryTemp=_DeliveryTemp_Object((1,3,6,1,4,1,9839,2,1,2,3),_DeliveryTemp_Type())
deliveryTemp.setMaxAccess(_E)
if mibBuilder.loadTexts:deliveryTemp.setStatus(_A)
if mibBuilder.loadTexts:deliveryTemp.setUnits(_F)
class _CwTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_CwTemp_Type.__name__=_B
_CwTemp_Object=MibScalar
cwTemp=_CwTemp_Object((1,3,6,1,4,1,9839,2,1,2,4),_CwTemp_Type())
cwTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTemp.setStatus(_A)
if mibBuilder.loadTexts:cwTemp.setUnits(_F)
class _HwTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_HwTemp_Type.__name__=_B
_HwTemp_Object=MibScalar
hwTemp=_HwTemp_Object((1,3,6,1,4,1,9839,2,1,2,5),_HwTemp_Type())
hwTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTemp.setStatus(_A)
if mibBuilder.loadTexts:hwTemp.setUnits(_F)
class _RoomRH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_RoomRH_Type.__name__=_B
_RoomRH_Object=MibScalar
roomRH=_RoomRH_Object((1,3,6,1,4,1,9839,2,1,2,6),_RoomRH_Type())
roomRH.setMaxAccess(_C)
if mibBuilder.loadTexts:roomRH.setStatus(_A)
if mibBuilder.loadTexts:roomRH.setUnits(_H)
class _CwoTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_CwoTemp_Type.__name__=_B
_CwoTemp_Object=MibScalar
cwoTemp=_CwoTemp_Object((1,3,6,1,4,1,9839,2,1,2,7),_CwoTemp_Type())
cwoTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:cwoTemp.setStatus(_A)
if mibBuilder.loadTexts:cwoTemp.setUnits(_F)
class _EvapPress1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_EvapPress1_Type.__name__=_B
_EvapPress1_Object=MibScalar
evapPress1=_EvapPress1_Object((1,3,6,1,4,1,9839,2,1,2,8),_EvapPress1_Type())
evapPress1.setMaxAccess(_E)
if mibBuilder.loadTexts:evapPress1.setStatus(_A)
if mibBuilder.loadTexts:evapPress1.setUnits('bar')
class _EvapPress2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_EvapPress2_Type.__name__=_B
_EvapPress2_Object=MibScalar
evapPress2=_EvapPress2_Object((1,3,6,1,4,1,9839,2,1,2,9),_EvapPress2_Type())
evapPress2.setMaxAccess(_E)
if mibBuilder.loadTexts:evapPress2.setStatus(_A)
if mibBuilder.loadTexts:evapPress2.setUnits('bar')
class _SuctTemp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_SuctTemp1_Type.__name__=_B
_SuctTemp1_Object=MibScalar
suctTemp1=_SuctTemp1_Object((1,3,6,1,4,1,9839,2,1,2,10),_SuctTemp1_Type())
suctTemp1.setMaxAccess(_C)
if mibBuilder.loadTexts:suctTemp1.setStatus(_A)
if mibBuilder.loadTexts:suctTemp1.setUnits(_F)
class _SuctTemp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_SuctTemp2_Type.__name__=_B
_SuctTemp2_Object=MibScalar
suctTemp2=_SuctTemp2_Object((1,3,6,1,4,1,9839,2,1,2,11),_SuctTemp2_Type())
suctTemp2.setMaxAccess(_C)
if mibBuilder.loadTexts:suctTemp2.setStatus(_A)
if mibBuilder.loadTexts:suctTemp2.setUnits(_F)
class _EvapTemp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_EvapTemp1_Type.__name__=_B
_EvapTemp1_Object=MibScalar
evapTemp1=_EvapTemp1_Object((1,3,6,1,4,1,9839,2,1,2,12),_EvapTemp1_Type())
evapTemp1.setMaxAccess(_C)
if mibBuilder.loadTexts:evapTemp1.setStatus(_A)
if mibBuilder.loadTexts:evapTemp1.setUnits(_F)
class _EvapTemp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_EvapTemp2_Type.__name__=_B
_EvapTemp2_Object=MibScalar
evapTemp2=_EvapTemp2_Object((1,3,6,1,4,1,9839,2,1,2,13),_EvapTemp2_Type())
evapTemp2.setMaxAccess(_C)
if mibBuilder.loadTexts:evapTemp2.setStatus(_A)
if mibBuilder.loadTexts:evapTemp2.setUnits(_F)
class _Ssh1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ssh1_Type.__name__=_B
_Ssh1_Object=MibScalar
ssh1=_Ssh1_Object((1,3,6,1,4,1,9839,2,1,2,14),_Ssh1_Type())
ssh1.setMaxAccess(_C)
if mibBuilder.loadTexts:ssh1.setStatus(_A)
if mibBuilder.loadTexts:ssh1.setUnits(_F)
class _Ssh2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Ssh2_Type.__name__=_B
_Ssh2_Object=MibScalar
ssh2=_Ssh2_Object((1,3,6,1,4,1,9839,2,1,2,15),_Ssh2_Type())
ssh2.setMaxAccess(_C)
if mibBuilder.loadTexts:ssh2.setStatus(_A)
if mibBuilder.loadTexts:ssh2.setUnits(_F)
class _CoolRamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_CoolRamp_Type.__name__=_B
_CoolRamp_Object=MibScalar
coolRamp=_CoolRamp_Object((1,3,6,1,4,1,9839,2,1,2,16),_CoolRamp_Type())
coolRamp.setMaxAccess(_C)
if mibBuilder.loadTexts:coolRamp.setStatus(_A)
if mibBuilder.loadTexts:coolRamp.setUnits('%')
class _HeatRamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_HeatRamp_Type.__name__=_B
_HeatRamp_Object=MibScalar
heatRamp=_HeatRamp_Object((1,3,6,1,4,1,9839,2,1,2,17),_HeatRamp_Type())
heatRamp.setMaxAccess(_C)
if mibBuilder.loadTexts:heatRamp.setStatus(_A)
if mibBuilder.loadTexts:heatRamp.setUnits('%')
class _FanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_FanSpeed_Type.__name__=_B
_FanSpeed_Object=MibScalar
fanSpeed=_FanSpeed_Object((1,3,6,1,4,1,9839,2,1,2,18),_FanSpeed_Type())
fanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fanSpeed.setStatus(_A)
if mibBuilder.loadTexts:fanSpeed.setUnits('%')
class _CoolSetP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_CoolSetP_Type.__name__=_B
_CoolSetP_Object=MibScalar
coolSetP=_CoolSetP_Object((1,3,6,1,4,1,9839,2,1,2,20),_CoolSetP_Type())
coolSetP.setMaxAccess(_E)
if mibBuilder.loadTexts:coolSetP.setStatus(_A)
if mibBuilder.loadTexts:coolSetP.setUnits(_F)
class _CoolDiff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_CoolDiff_Type.__name__=_B
_CoolDiff_Object=MibScalar
coolDiff=_CoolDiff_Object((1,3,6,1,4,1,9839,2,1,2,21),_CoolDiff_Type())
coolDiff.setMaxAccess(_E)
if mibBuilder.loadTexts:coolDiff.setStatus(_A)
if mibBuilder.loadTexts:coolDiff.setUnits(_F)
class _Cool2SetP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Cool2SetP_Type.__name__=_B
_Cool2SetP_Object=MibScalar
cool2SetP=_Cool2SetP_Object((1,3,6,1,4,1,9839,2,1,2,22),_Cool2SetP_Type())
cool2SetP.setMaxAccess(_E)
if mibBuilder.loadTexts:cool2SetP.setStatus(_A)
if mibBuilder.loadTexts:cool2SetP.setUnits(_F)
class _HeatSetP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_HeatSetP_Type.__name__=_B
_HeatSetP_Object=MibScalar
heatSetP=_HeatSetP_Object((1,3,6,1,4,1,9839,2,1,2,23),_HeatSetP_Type())
heatSetP.setMaxAccess(_E)
if mibBuilder.loadTexts:heatSetP.setStatus(_A)
if mibBuilder.loadTexts:heatSetP.setUnits(_F)
class _Heat2SetP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Heat2SetP_Type.__name__=_B
_Heat2SetP_Object=MibScalar
heat2SetP=_Heat2SetP_Object((1,3,6,1,4,1,9839,2,1,2,24),_Heat2SetP_Type())
heat2SetP.setMaxAccess(_E)
if mibBuilder.loadTexts:heat2SetP.setStatus(_A)
if mibBuilder.loadTexts:heat2SetP.setUnits(_F)
class _HeatDiff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_HeatDiff_Type.__name__=_B
_HeatDiff_Object=MibScalar
heatDiff=_HeatDiff_Object((1,3,6,1,4,1,9839,2,1,2,25),_HeatDiff_Type())
heatDiff.setMaxAccess(_E)
if mibBuilder.loadTexts:heatDiff.setStatus(_A)
if mibBuilder.loadTexts:heatDiff.setUnits(_F)
class _ThrsHT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_ThrsHT_Type.__name__=_B
_ThrsHT_Object=MibScalar
thrsHT=_ThrsHT_Object((1,3,6,1,4,1,9839,2,1,2,26),_ThrsHT_Type())
thrsHT.setMaxAccess(_E)
if mibBuilder.loadTexts:thrsHT.setStatus(_A)
if mibBuilder.loadTexts:thrsHT.setUnits(_I)
class _ThrsLT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_ThrsLT_Type.__name__=_B
_ThrsLT_Object=MibScalar
thrsLT=_ThrsLT_Object((1,3,6,1,4,1,9839,2,1,2,27),_ThrsLT_Type())
thrsLT.setMaxAccess(_E)
if mibBuilder.loadTexts:thrsLT.setStatus(_A)
if mibBuilder.loadTexts:thrsLT.setUnits(_I)
class _SmCoolSetp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_SmCoolSetp_Type.__name__=_B
_SmCoolSetp_Object=MibScalar
smCoolSetp=_SmCoolSetp_Object((1,3,6,1,4,1,9839,2,1,2,28),_SmCoolSetp_Type())
smCoolSetp.setMaxAccess(_E)
if mibBuilder.loadTexts:smCoolSetp.setStatus(_A)
if mibBuilder.loadTexts:smCoolSetp.setUnits(_F)
class _SmHeatSetp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_SmHeatSetp_Type.__name__=_B
_SmHeatSetp_Object=MibScalar
smHeatSetp=_SmHeatSetp_Object((1,3,6,1,4,1,9839,2,1,2,29),_SmHeatSetp_Type())
smHeatSetp.setMaxAccess(_E)
if mibBuilder.loadTexts:smHeatSetp.setStatus(_A)
if mibBuilder.loadTexts:smHeatSetp.setUnits(_F)
class _CwDehumSetp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_CwDehumSetp_Type.__name__=_B
_CwDehumSetp_Object=MibScalar
cwDehumSetp=_CwDehumSetp_Object((1,3,6,1,4,1,9839,2,1,2,30),_CwDehumSetp_Type())
cwDehumSetp.setMaxAccess(_E)
if mibBuilder.loadTexts:cwDehumSetp.setStatus(_A)
if mibBuilder.loadTexts:cwDehumSetp.setUnits(_F)
class _CwHtThrsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_CwHtThrsh_Type.__name__=_B
_CwHtThrsh_Object=MibScalar
cwHtThrsh=_CwHtThrsh_Object((1,3,6,1,4,1,9839,2,1,2,31),_CwHtThrsh_Type())
cwHtThrsh.setMaxAccess(_E)
if mibBuilder.loadTexts:cwHtThrsh.setStatus(_A)
if mibBuilder.loadTexts:cwHtThrsh.setUnits(_F)
class _CwModeSetp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_CwModeSetp_Type.__name__=_B
_CwModeSetp_Object=MibScalar
cwModeSetp=_CwModeSetp_Object((1,3,6,1,4,1,9839,2,1,2,32),_CwModeSetp_Type())
cwModeSetp.setMaxAccess(_E)
if mibBuilder.loadTexts:cwModeSetp.setStatus(_A)
if mibBuilder.loadTexts:cwModeSetp.setUnits(_F)
class _RadcoolSpES_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_RadcoolSpES_Type.__name__=_B
_RadcoolSpES_Object=MibScalar
radcoolSpES=_RadcoolSpES_Object((1,3,6,1,4,1,9839,2,1,2,33),_RadcoolSpES_Type())
radcoolSpES.setMaxAccess(_E)
if mibBuilder.loadTexts:radcoolSpES.setStatus(_A)
if mibBuilder.loadTexts:radcoolSpES.setUnits(_F)
class _RadcoolSpDX_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_RadcoolSpDX_Type.__name__=_B
_RadcoolSpDX_Object=MibScalar
radcoolSpDX=_RadcoolSpDX_Object((1,3,6,1,4,1,9839,2,1,2,34),_RadcoolSpDX_Type())
radcoolSpDX.setMaxAccess(_E)
if mibBuilder.loadTexts:radcoolSpDX.setStatus(_A)
if mibBuilder.loadTexts:radcoolSpDX.setUnits(_F)
class _DelTempLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_DelTempLimit_Type.__name__=_B
_DelTempLimit_Object=MibScalar
delTempLimit=_DelTempLimit_Object((1,3,6,1,4,1,9839,2,1,2,35),_DelTempLimit_Type())
delTempLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:delTempLimit.setStatus(_A)
if mibBuilder.loadTexts:delTempLimit.setUnits(_I)
class _DtAutChgMLT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_DtAutChgMLT_Type.__name__=_B
_DtAutChgMLT_Object=MibScalar
dtAutChgMLT=_DtAutChgMLT_Object((1,3,6,1,4,1,9839,2,1,2,36),_DtAutChgMLT_Type())
dtAutChgMLT.setMaxAccess(_E)
if mibBuilder.loadTexts:dtAutChgMLT.setStatus(_A)
if mibBuilder.loadTexts:dtAutChgMLT.setUnits(_F)
_IntegerObjects_ObjectIdentity=ObjectIdentity
integerObjects=_IntegerObjects_ObjectIdentity((1,3,6,1,4,1,9839,2,1,3))
class _FilterWorkH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_FilterWorkH_Type.__name__=_B
_FilterWorkH_Object=MibScalar
filterWorkH=_FilterWorkH_Object((1,3,6,1,4,1,9839,2,1,3,1),_FilterWorkH_Type())
filterWorkH.setMaxAccess(_C)
if mibBuilder.loadTexts:filterWorkH.setStatus(_A)
if mibBuilder.loadTexts:filterWorkH.setUnits(_G)
class _UnitWorkH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_UnitWorkH_Type.__name__=_B
_UnitWorkH_Object=MibScalar
unitWorkH=_UnitWorkH_Object((1,3,6,1,4,1,9839,2,1,3,2),_UnitWorkH_Type())
unitWorkH.setMaxAccess(_C)
if mibBuilder.loadTexts:unitWorkH.setStatus(_A)
if mibBuilder.loadTexts:unitWorkH.setUnits(_G)
class _Compr1WorkH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Compr1WorkH_Type.__name__=_B
_Compr1WorkH_Object=MibScalar
compr1WorkH=_Compr1WorkH_Object((1,3,6,1,4,1,9839,2,1,3,3),_Compr1WorkH_Type())
compr1WorkH.setMaxAccess(_C)
if mibBuilder.loadTexts:compr1WorkH.setStatus(_A)
if mibBuilder.loadTexts:compr1WorkH.setUnits(_G)
class _Compr2WorkH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Compr2WorkH_Type.__name__=_B
_Compr2WorkH_Object=MibScalar
compr2WorkH=_Compr2WorkH_Object((1,3,6,1,4,1,9839,2,1,3,4),_Compr2WorkH_Type())
compr2WorkH.setMaxAccess(_C)
if mibBuilder.loadTexts:compr2WorkH.setStatus(_A)
if mibBuilder.loadTexts:compr2WorkH.setUnits(_G)
class _Compr3WorkH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Compr3WorkH_Type.__name__=_B
_Compr3WorkH_Object=MibScalar
compr3WorkH=_Compr3WorkH_Object((1,3,6,1,4,1,9839,2,1,3,5),_Compr3WorkH_Type())
compr3WorkH.setMaxAccess(_C)
if mibBuilder.loadTexts:compr3WorkH.setStatus(_A)
if mibBuilder.loadTexts:compr3WorkH.setUnits(_G)
class _Compr4WorkH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Compr4WorkH_Type.__name__=_B
_Compr4WorkH_Object=MibScalar
compr4WorkH=_Compr4WorkH_Object((1,3,6,1,4,1,9839,2,1,3,6),_Compr4WorkH_Type())
compr4WorkH.setMaxAccess(_C)
if mibBuilder.loadTexts:compr4WorkH.setStatus(_A)
if mibBuilder.loadTexts:compr4WorkH.setUnits(_G)
class _Heat1WorkH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Heat1WorkH_Type.__name__=_B
_Heat1WorkH_Object=MibScalar
heat1WorkH=_Heat1WorkH_Object((1,3,6,1,4,1,9839,2,1,3,7),_Heat1WorkH_Type())
heat1WorkH.setMaxAccess(_C)
if mibBuilder.loadTexts:heat1WorkH.setStatus(_A)
if mibBuilder.loadTexts:heat1WorkH.setUnits(_G)
class _Heat2WorkH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Heat2WorkH_Type.__name__=_B
_Heat2WorkH_Object=MibScalar
heat2WorkH=_Heat2WorkH_Object((1,3,6,1,4,1,9839,2,1,3,8),_Heat2WorkH_Type())
heat2WorkH.setMaxAccess(_C)
if mibBuilder.loadTexts:heat2WorkH.setStatus(_A)
if mibBuilder.loadTexts:heat2WorkH.setUnits(_G)
class _HumiWorkH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_HumiWorkH_Type.__name__=_B
_HumiWorkH_Object=MibScalar
humiWorkH=_HumiWorkH_Object((1,3,6,1,4,1,9839,2,1,3,9),_HumiWorkH_Type())
humiWorkH.setMaxAccess(_C)
if mibBuilder.loadTexts:humiWorkH.setStatus(_A)
if mibBuilder.loadTexts:humiWorkH.setUnits(_G)
class _DehumPband_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_DehumPband_Type.__name__=_B
_DehumPband_Object=MibScalar
dehumPband=_DehumPband_Object((1,3,6,1,4,1,9839,2,1,3,12),_DehumPband_Type())
dehumPband.setMaxAccess(_E)
if mibBuilder.loadTexts:dehumPband.setStatus(_A)
if mibBuilder.loadTexts:dehumPband.setUnits(_H)
class _HumidPband_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_HumidPband_Type.__name__=_B
_HumidPband_Object=MibScalar
humidPband=_HumidPband_Object((1,3,6,1,4,1,9839,2,1,3,13),_HumidPband_Type())
humidPband.setMaxAccess(_E)
if mibBuilder.loadTexts:humidPband.setStatus(_A)
if mibBuilder.loadTexts:humidPband.setUnits(_H)
class _HhAlarmThrsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_HhAlarmThrsh_Type.__name__=_B
_HhAlarmThrsh_Object=MibScalar
hhAlarmThrsh=_HhAlarmThrsh_Object((1,3,6,1,4,1,9839,2,1,3,14),_HhAlarmThrsh_Type())
hhAlarmThrsh.setMaxAccess(_E)
if mibBuilder.loadTexts:hhAlarmThrsh.setStatus(_A)
if mibBuilder.loadTexts:hhAlarmThrsh.setUnits(_H)
class _LhAlarmThrsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_LhAlarmThrsh_Type.__name__=_B
_LhAlarmThrsh_Object=MibScalar
lhAlarmThrsh=_LhAlarmThrsh_Object((1,3,6,1,4,1,9839,2,1,3,15),_LhAlarmThrsh_Type())
lhAlarmThrsh.setMaxAccess(_E)
if mibBuilder.loadTexts:lhAlarmThrsh.setStatus(_A)
if mibBuilder.loadTexts:lhAlarmThrsh.setUnits(_H)
class _DehumSetp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_DehumSetp_Type.__name__=_B
_DehumSetp_Object=MibScalar
dehumSetp=_DehumSetp_Object((1,3,6,1,4,1,9839,2,1,3,16),_DehumSetp_Type())
dehumSetp.setMaxAccess(_E)
if mibBuilder.loadTexts:dehumSetp.setStatus(_A)
if mibBuilder.loadTexts:dehumSetp.setUnits(_H)
class _SmDehumSetp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_SmDehumSetp_Type.__name__=_B
_SmDehumSetp_Object=MibScalar
smDehumSetp=_SmDehumSetp_Object((1,3,6,1,4,1,9839,2,1,3,17),_SmDehumSetp_Type())
smDehumSetp.setMaxAccess(_E)
if mibBuilder.loadTexts:smDehumSetp.setStatus(_A)
if mibBuilder.loadTexts:smDehumSetp.setUnits(_H)
class _HumidSetp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_HumidSetp_Type.__name__=_B
_HumidSetp_Object=MibScalar
humidSetp=_HumidSetp_Object((1,3,6,1,4,1,9839,2,1,3,18),_HumidSetp_Type())
humidSetp.setMaxAccess(_E)
if mibBuilder.loadTexts:humidSetp.setStatus(_A)
if mibBuilder.loadTexts:humidSetp.setUnits(_H)
class _SmHumidSetp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_SmHumidSetp_Type.__name__=_B
_SmHumidSetp_Object=MibScalar
smHumidSetp=_SmHumidSetp_Object((1,3,6,1,4,1,9839,2,1,3,19),_SmHumidSetp_Type())
smHumidSetp.setMaxAccess(_E)
if mibBuilder.loadTexts:smHumidSetp.setStatus(_A)
if mibBuilder.loadTexts:smHumidSetp.setUnits(_H)
class _PwOnDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_PwOnDelay_Type.__name__=_B
_PwOnDelay_Object=MibScalar
pwOnDelay=_PwOnDelay_Object((1,3,6,1,4,1,9839,2,1,3,20),_PwOnDelay_Type())
pwOnDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:pwOnDelay.setStatus(_A)
if mibBuilder.loadTexts:pwOnDelay.setUnits('s')
class _RegulDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_RegulDelay_Type.__name__=_B
_RegulDelay_Object=MibScalar
regulDelay=_RegulDelay_Object((1,3,6,1,4,1,9839,2,1,3,21),_RegulDelay_Type())
regulDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:regulDelay.setStatus(_A)
if mibBuilder.loadTexts:regulDelay.setUnits('s')
class _LowPdelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_LowPdelay_Type.__name__=_B
_LowPdelay_Object=MibScalar
lowPdelay=_LowPdelay_Object((1,3,6,1,4,1,9839,2,1,3,22),_LowPdelay_Type())
lowPdelay.setMaxAccess(_E)
if mibBuilder.loadTexts:lowPdelay.setStatus(_A)
if mibBuilder.loadTexts:lowPdelay.setUnits('s')
class _ThAlarmdelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_ThAlarmdelay_Type.__name__=_B
_ThAlarmdelay_Object=MibScalar
thAlarmdelay=_ThAlarmdelay_Object((1,3,6,1,4,1,9839,2,1,3,23),_ThAlarmdelay_Type())
thAlarmdelay.setMaxAccess(_E)
if mibBuilder.loadTexts:thAlarmdelay.setStatus(_A)
if mibBuilder.loadTexts:thAlarmdelay.setUnits(_J)
class _RegExcTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_RegExcTime_Type.__name__=_B
_RegExcTime_Object=MibScalar
regExcTime=_RegExcTime_Object((1,3,6,1,4,1,9839,2,1,3,24),_RegExcTime_Type())
regExcTime.setMaxAccess(_E)
if mibBuilder.loadTexts:regExcTime.setStatus(_A)
if mibBuilder.loadTexts:regExcTime.setUnits(_J)
class _StdbyTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_StdbyTime_Type.__name__=_B
_StdbyTime_Object=MibScalar
stdbyTime=_StdbyTime_Object((1,3,6,1,4,1,9839,2,1,3,25),_StdbyTime_Type())
stdbyTime.setMaxAccess(_E)
if mibBuilder.loadTexts:stdbyTime.setStatus(_A)
if mibBuilder.loadTexts:stdbyTime.setUnits(_G)
class _LanUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_LanUnit_Type.__name__=_B
_LanUnit_Object=MibScalar
lanUnit=_LanUnit_Object((1,3,6,1,4,1,9839,2,1,3,27),_LanUnit_Type())
lanUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:lanUnit.setStatus(_A)
if mibBuilder.loadTexts:lanUnit.setUnits('n')
class _SmCycleTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_SmCycleTime_Type.__name__=_B
_SmCycleTime_Object=MibScalar
smCycleTime=_SmCycleTime_Object((1,3,6,1,4,1,9839,2,1,3,28),_SmCycleTime_Type())
smCycleTime.setMaxAccess(_E)
if mibBuilder.loadTexts:smCycleTime.setStatus(_A)
if mibBuilder.loadTexts:smCycleTime.setUnits(_J)
class _Exv1steps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Exv1steps_Type.__name__=_B
_Exv1steps_Object=MibScalar
exv1steps=_Exv1steps_Object((1,3,6,1,4,1,9839,2,1,3,29),_Exv1steps_Type())
exv1steps.setMaxAccess(_C)
if mibBuilder.loadTexts:exv1steps.setStatus(_A)
if mibBuilder.loadTexts:exv1steps.setUnits('n')
class _Exv2steps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_Exv2steps_Type.__name__=_B
_Exv2steps_Object=MibScalar
exv2steps=_Exv2steps_Object((1,3,6,1,4,1,9839,2,1,3,30),_Exv2steps_Type())
exv2steps.setMaxAccess(_C)
if mibBuilder.loadTexts:exv2steps.setStatus(_A)
if mibBuilder.loadTexts:exv2steps.setUnits('n')
mibBuilder.exportSymbols('CAREL-ug40cdz-MIB',**{'carel':carel,'systm':systm,'agentRelease':agentRelease,'agentCode':agentCode,'instruments':instruments,'webGateInfo':webGateInfo,'agentParameters':agentParameters,'netSize':netSize,'baudRate':baudRate,'unitTypeGroup':unitTypeGroup,'unit1-Type':unit1_Type,'unitCodeGroup':unitCodeGroup,'unit1-Code':unit1_Code,'unitSoftwareReleaseGroup':unitSoftwareReleaseGroup,'unit1-SoftwareRelease':unit1_SoftwareRelease,'unitMinSoftwareReleaseGroup':unitMinSoftwareReleaseGroup,'unit1-MinSoftwareRelease':unit1_MinSoftwareRelease,'unitMaxSoftwareReleaseGroup':unitMaxSoftwareReleaseGroup,'unit1-MaxSoftwareRelease':unit1_MaxSoftwareRelease,'unitNoAnswerCounterGroup':unitNoAnswerCounterGroup,'unit1-NoAnswerCounter':unit1_NoAnswerCounter,'unitErrorChecksumCounterGroup':unitErrorChecksumCounterGroup,'unit1-ErrorChecksumCounter':unit1_ErrorChecksumCounter,'unitTimeoutCounterGroup':unitTimeoutCounterGroup,'unit1-TimeoutCounter':unit1_TimeoutCounter,'ug40cdzMIB':ug40cdzMIB,'digitalObjects':digitalObjects,'systemOn':systemOn,'compressore1':compressore1,'compressore2':compressore2,'compressore3':compressore3,'compressore4':compressore4,'heating1':heating1,'heating2':heating2,'hotGasCoil':hotGasCoil,'dehumidification':dehumidification,'humidification':humidification,'emerg':emerg,'alarmAccess':alarmAccess,'alarmRoomHT':alarmRoomHT,'alarmRoomLT':alarmRoomLT,'alarmRoomHH':alarmRoomHH,'alarmRoomLH':alarmRoomLH,'alarmRoomEAP':alarmRoomEAP,'alarmFilter':alarmFilter,'alarmFlood':alarmFlood,'alarmAirFlow':alarmAirFlow,'alarmHeater':alarmHeater,'alarmHP1':alarmHP1,'alarmHP2':alarmHP2,'alarmLP1':alarmLP1,'alarmLP2':alarmLP2,'alarmEXV1':alarmEXV1,'alarmEXV2':alarmEXV2,'alarmPSE':alarmPSE,'alarmSmokeFire':alarmSmokeFire,'alarmLAN':alarmLAN,'alarmHUHC':alarmHUHC,'alarmHUPL':alarmHUPL,'alarmHUWL':alarmHUWL,'alarmCWDHT':alarmCWDHT,'alarmCWF':alarmCWF,'alarmCWFF':alarmCWFF,'alarmCWHT':alarmCWHT,'alarmRTS':alarmRTS,'alarmHWS':alarmHWS,'alarmCWS':alarmCWS,'alarmOTS':alarmOTS,'alarmDTS':alarmDTS,'alarmRHS':alarmRHS,'alarmCWOTS':alarmCWOTS,'alarmC1Hours':alarmC1Hours,'alarmC2Hours':alarmC2Hours,'alarmC3Hours':alarmC3Hours,'alarmC4Hours':alarmC4Hours,'alarmFilterHours':alarmFilterHours,'alarmHeat1Hours':alarmHeat1Hours,'alarmHeat2Hours':alarmHeat2Hours,'alarmHumHours':alarmHumHours,'alarmUnitHours':alarmUnitHours,'alarmDI2':alarmDI2,'alarmDI4':alarmDI4,'alarmDI6':alarmDI6,'alarmHum':alarmHum,'alarmGeneral':alarmGeneral,'alarm2ndLevel':alarm2ndLevel,'alarmA':alarmA,'alarmB':alarmB,'alarmC':alarmC,'selDXCW':selDXCW,'selSW':selSW,'systemOnOff':systemOnOff,'resetAlarm':resetAlarm,'resetHrsFilt':resetHrsFilt,'resetHrC1':resetHrC1,'resetHrC2':resetHrC2,'resetHrC3':resetHrC3,'resetHrC4':resetHrC4,'resetStC1':resetStC1,'resetStC2':resetStC2,'resetStC3':resetStC3,'resetStC4':resetStC4,'resetHrH1':resetHrH1,'resetHrH2':resetHrH2,'resetStH1':resetStH1,'resetStH2':resetStH2,'resetHrHU':resetHrHU,'resetStHU':resetStHU,'resetHrACU':resetHrACU,'sleepmode':sleepmode,'smtest':smtest,'enablemeanT':enablemeanT,'analogObjects':analogObjects,'roomTemp':roomTemp,'outdoorTemp':outdoorTemp,'deliveryTemp':deliveryTemp,'cwTemp':cwTemp,'hwTemp':hwTemp,'roomRH':roomRH,'cwoTemp':cwoTemp,'evapPress1':evapPress1,'evapPress2':evapPress2,'suctTemp1':suctTemp1,'suctTemp2':suctTemp2,'evapTemp1':evapTemp1,'evapTemp2':evapTemp2,'ssh1':ssh1,'ssh2':ssh2,'coolRamp':coolRamp,'heatRamp':heatRamp,'fanSpeed':fanSpeed,'coolSetP':coolSetP,'coolDiff':coolDiff,'cool2SetP':cool2SetP,'heatSetP':heatSetP,'heat2SetP':heat2SetP,'heatDiff':heatDiff,'thrsHT':thrsHT,'thrsLT':thrsLT,'smCoolSetp':smCoolSetp,'smHeatSetp':smHeatSetp,'cwDehumSetp':cwDehumSetp,'cwHtThrsh':cwHtThrsh,'cwModeSetp':cwModeSetp,'radcoolSpES':radcoolSpES,'radcoolSpDX':radcoolSpDX,'delTempLimit':delTempLimit,'dtAutChgMLT':dtAutChgMLT,'integerObjects':integerObjects,'filterWorkH':filterWorkH,'unitWorkH':unitWorkH,'compr1WorkH':compr1WorkH,'compr2WorkH':compr2WorkH,'compr3WorkH':compr3WorkH,'compr4WorkH':compr4WorkH,'heat1WorkH':heat1WorkH,'heat2WorkH':heat2WorkH,'humiWorkH':humiWorkH,'dehumPband':dehumPband,'humidPband':humidPband,'hhAlarmThrsh':hhAlarmThrsh,'lhAlarmThrsh':lhAlarmThrsh,'dehumSetp':dehumSetp,'smDehumSetp':smDehumSetp,'humidSetp':humidSetp,'smHumidSetp':smHumidSetp,'pwOnDelay':pwOnDelay,'regulDelay':regulDelay,'lowPdelay':lowPdelay,'thAlarmdelay':thAlarmdelay,'regExcTime':regExcTime,'stdbyTime':stdbyTime,'lanUnit':lanUnit,'smCycleTime':smCycleTime,'exv1steps':exv1steps,'exv2steps':exv2steps})