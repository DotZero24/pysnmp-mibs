_O='critical'
_N='caution'
_M='repaired'
_L='infoWithAlert'
_K='informational'
_J='hpnsaEventLogRecType'
_I='hpnsaEventLogAgentIndex'
_H='hpnsaEventLogTableIndex'
_G='read-write'
_F='HPNSAEVENT-MIB'
_E='OctetString'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaEventLog_ObjectIdentity=ObjectIdentity
hpnsaEventLog=_HpnsaEventLog_ObjectIdentity((1,3,6,1,4,1,11,2,23,19))
_HpnsaEventLogRev_ObjectIdentity=ObjectIdentity
hpnsaEventLogRev=_HpnsaEventLogRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,19,1))
class _HpnsaEventLogMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEventLogMibRevMajor_Type.__name__=_D
_HpnsaEventLogMibRevMajor_Object=MibScalar
hpnsaEventLogMibRevMajor=_HpnsaEventLogMibRevMajor_Object((1,3,6,1,4,1,11,2,23,19,1,1),_HpnsaEventLogMibRevMajor_Type())
hpnsaEventLogMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogMibRevMajor.setStatus(_A)
class _HpnsaEventLogMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEventLogMibRevMinor_Type.__name__=_D
_HpnsaEventLogMibRevMinor_Object=MibScalar
hpnsaEventLogMibRevMinor=_HpnsaEventLogMibRevMinor_Object((1,3,6,1,4,1,11,2,23,19,1,2),_HpnsaEventLogMibRevMinor_Type())
hpnsaEventLogMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogMibRevMinor.setStatus(_A)
_HpnsaEventLogAgentInfo_ObjectIdentity=ObjectIdentity
hpnsaEventLogAgentInfo=_HpnsaEventLogAgentInfo_ObjectIdentity((1,3,6,1,4,1,11,2,23,19,2))
_HpnsaEventLogAgentTable_Object=MibTable
hpnsaEventLogAgentTable=_HpnsaEventLogAgentTable_Object((1,3,6,1,4,1,11,2,23,19,2,1))
if mibBuilder.loadTexts:hpnsaEventLogAgentTable.setStatus(_A)
_HpnsaEventLogAgentEntry_Object=MibTableRow
hpnsaEventLogAgentEntry=_HpnsaEventLogAgentEntry_Object((1,3,6,1,4,1,11,2,23,19,2,1,1))
hpnsaEventLogAgentEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:hpnsaEventLogAgentEntry.setStatus(_A)
class _HpnsaEventLogAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEventLogAgentIndex_Type.__name__=_D
_HpnsaEventLogAgentIndex_Object=MibTableColumn
hpnsaEventLogAgentIndex=_HpnsaEventLogAgentIndex_Object((1,3,6,1,4,1,11,2,23,19,2,1,1,1),_HpnsaEventLogAgentIndex_Type())
hpnsaEventLogAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogAgentIndex.setStatus(_A)
class _HpnsaEventLogAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogAgentName_Type.__name__=_C
_HpnsaEventLogAgentName_Object=MibTableColumn
hpnsaEventLogAgentName=_HpnsaEventLogAgentName_Object((1,3,6,1,4,1,11,2,23,19,2,1,1,2),_HpnsaEventLogAgentName_Type())
hpnsaEventLogAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogAgentName.setStatus(_A)
class _HpnsaEventLogAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_HpnsaEventLogAgentVersion_Type.__name__=_C
_HpnsaEventLogAgentVersion_Object=MibTableColumn
hpnsaEventLogAgentVersion=_HpnsaEventLogAgentVersion_Object((1,3,6,1,4,1,11,2,23,19,2,1,1,3),_HpnsaEventLogAgentVersion_Type())
hpnsaEventLogAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogAgentVersion.setStatus(_A)
class _HpnsaEventLogAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaEventLogAgentDate_Type.__name__=_E
_HpnsaEventLogAgentDate_Object=MibTableColumn
hpnsaEventLogAgentDate=_HpnsaEventLogAgentDate_Object((1,3,6,1,4,1,11,2,23,19,2,1,1,4),_HpnsaEventLogAgentDate_Type())
hpnsaEventLogAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogAgentDate.setStatus(_A)
_HpnsaEventAgentCfgInfo_ObjectIdentity=ObjectIdentity
hpnsaEventAgentCfgInfo=_HpnsaEventAgentCfgInfo_ObjectIdentity((1,3,6,1,4,1,11,2,23,19,3))
_HpnsaEventCfgTable_Object=MibTable
hpnsaEventCfgTable=_HpnsaEventCfgTable_Object((1,3,6,1,4,1,11,2,23,19,3,1))
if mibBuilder.loadTexts:hpnsaEventCfgTable.setStatus(_A)
_HpnsaEventCfgTableEntry_Object=MibTableRow
hpnsaEventCfgTableEntry=_HpnsaEventCfgTableEntry_Object((1,3,6,1,4,1,11,2,23,19,3,1,1))
hpnsaEventCfgTableEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:hpnsaEventCfgTableEntry.setStatus(_A)
class _HpnsaEventLogRecType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,20,21,22,23,33,34,35,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,247,248)));namedValues=NamedValues(*(('errorEccSingleBit',1),('errorEccMultipleBit',2),('errorParityMemory',3),('errorBusTimeout',4),('errorIOChannelCheck',5),('errorSoftwareNMI',6),('errorPostMemoryResize',7),('errorPost',8),('errorPciParity',9),('errorPciSystem',10),('errorCpuFailure',11),('errorFailsafeTimeout',12),('infoSingleBitErrorDisabled',13),('infoErrorLoggingDisabled',14),('errorSystemLimitExceeded',16),('infoAsynchronousSystemReset',17),('infoSystemReconfig',20),('errorPCISystem',21),('logAreaReset',22),('systemRebooted',23),('errorECCSingleBit',33),('errorECCMultipleBit',34),('errorPOSTMemoryResize',35),('cpuDeconfigured',128),('p6ECCError',129),('frontPanelNMI',130),('cpuPciSingleFanError',131),('cpuPciMultipleFanError',132),('cpuPciFanRestored',133),('watchdogTimerReset',134),('memorySingleFanError',135),('memoryMultipleFanError',136),('memoryFanRestored',137),('cpuReconfigured',138),('powerSupplyEvent',139),('powerSupplyRemoved',140),('powerSupplyInserted',141),('controlBoardReset',142),('controlBoardPowerCycle',143),('cpuCardMissing',144),('voltageRegulatingMonitorFailure',145),('infoRedundantPowerSupply',247),('infoHotSwapModule',248)))
_HpnsaEventLogRecType_Type.__name__=_D
_HpnsaEventLogRecType_Object=MibTableColumn
hpnsaEventLogRecType=_HpnsaEventLogRecType_Object((1,3,6,1,4,1,11,2,23,19,3,1,1,1),_HpnsaEventLogRecType_Type())
hpnsaEventLogRecType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogRecType.setStatus(_A)
class _HpnsaEventLogRecTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trapDisabled',1),('trapEnabled',2)))
_HpnsaEventLogRecTrapEnable_Type.__name__=_D
_HpnsaEventLogRecTrapEnable_Object=MibTableColumn
hpnsaEventLogRecTrapEnable=_HpnsaEventLogRecTrapEnable_Object((1,3,6,1,4,1,11,2,23,19,3,1,1,2),_HpnsaEventLogRecTrapEnable_Type())
hpnsaEventLogRecTrapEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnsaEventLogRecTrapEnable.setStatus(_A)
_HpnsaEventLogPresenceId_ObjectIdentity=ObjectIdentity
hpnsaEventLogPresenceId=_HpnsaEventLogPresenceId_ObjectIdentity((1,3,6,1,4,1,11,2,23,19,4))
class _HpnsaEccPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HpnsaEccPresent_Type.__name__=_D
_HpnsaEccPresent_Object=MibScalar
hpnsaEccPresent=_HpnsaEccPresent_Object((1,3,6,1,4,1,11,2,23,19,4,1),_HpnsaEccPresent_Type())
hpnsaEccPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccPresent.setStatus(_A)
class _HpnsaPostPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HpnsaPostPresent_Type.__name__=_D
_HpnsaPostPresent_Object=MibScalar
hpnsaPostPresent=_HpnsaPostPresent_Object((1,3,6,1,4,1,11,2,23,19,4,2),_HpnsaPostPresent_Type())
hpnsaPostPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaPostPresent.setStatus(_A)
class _HpnsaTempVoltagePresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HpnsaTempVoltagePresent_Type.__name__=_D
_HpnsaTempVoltagePresent_Object=MibScalar
hpnsaTempVoltagePresent=_HpnsaTempVoltagePresent_Object((1,3,6,1,4,1,11,2,23,19,4,3),_HpnsaTempVoltagePresent_Type())
hpnsaTempVoltagePresent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaTempVoltagePresent.setStatus(_A)
class _HpnsaASRPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HpnsaASRPresent_Type.__name__=_D
_HpnsaASRPresent_Object=MibScalar
hpnsaASRPresent=_HpnsaASRPresent_Object((1,3,6,1,4,1,11,2,23,19,4,4),_HpnsaASRPresent_Type())
hpnsaASRPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaASRPresent.setStatus(_A)
class _HpnsaNMIPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HpnsaNMIPresent_Type.__name__=_D
_HpnsaNMIPresent_Object=MibScalar
hpnsaNMIPresent=_HpnsaNMIPresent_Object((1,3,6,1,4,1,11,2,23,19,4,5),_HpnsaNMIPresent_Type())
hpnsaNMIPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaNMIPresent.setStatus(_A)
_HpnsaEventLogStatistics_ObjectIdentity=ObjectIdentity
hpnsaEventLogStatistics=_HpnsaEventLogStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,23,19,5))
class _HpnsaEventLogPercentFull_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnsaEventLogPercentFull_Type.__name__=_D
_HpnsaEventLogPercentFull_Object=MibScalar
hpnsaEventLogPercentFull=_HpnsaEventLogPercentFull_Object((1,3,6,1,4,1,11,2,23,19,5,1),_HpnsaEventLogPercentFull_Type())
hpnsaEventLogPercentFull.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogPercentFull.setStatus(_A)
class _HpnsaEventLogLastErasedDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaEventLogLastErasedDate_Type.__name__=_E
_HpnsaEventLogLastErasedDate_Object=MibScalar
hpnsaEventLogLastErasedDate=_HpnsaEventLogLastErasedDate_Object((1,3,6,1,4,1,11,2,23,19,5,2),_HpnsaEventLogLastErasedDate_Type())
hpnsaEventLogLastErasedDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLastErasedDate.setStatus(_A)
_HpnsaEventLogErasures_Type=Counter32
_HpnsaEventLogErasures_Object=MibScalar
hpnsaEventLogErasures=_HpnsaEventLogErasures_Object((1,3,6,1,4,1,11,2,23,19,5,3),_HpnsaEventLogErasures_Type())
hpnsaEventLogErasures.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogErasures.setStatus(_A)
class _HpnsaEventLogEraseLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1234));namedValues=NamedValues(('eraseLogNow',1234))
_HpnsaEventLogEraseLog_Type.__name__=_D
_HpnsaEventLogEraseLog_Object=MibScalar
hpnsaEventLogEraseLog=_HpnsaEventLogEraseLog_Object((1,3,6,1,4,1,11,2,23,19,5,4),_HpnsaEventLogEraseLog_Type())
hpnsaEventLogEraseLog.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnsaEventLogEraseLog.setStatus(_A)
_HpnsaEventLogTable_Object=MibTable
hpnsaEventLogTable=_HpnsaEventLogTable_Object((1,3,6,1,4,1,11,2,23,19,5,5))
if mibBuilder.loadTexts:hpnsaEventLogTable.setStatus(_A)
_HpnsaEventLogTableEntry_Object=MibTableRow
hpnsaEventLogTableEntry=_HpnsaEventLogTableEntry_Object((1,3,6,1,4,1,11,2,23,19,5,5,1))
hpnsaEventLogTableEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:hpnsaEventLogTableEntry.setStatus(_A)
_HpnsaEventLogTableIndex_Type=Integer32
_HpnsaEventLogTableIndex_Object=MibTableColumn
hpnsaEventLogTableIndex=_HpnsaEventLogTableIndex_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,1),_HpnsaEventLogTableIndex_Type())
hpnsaEventLogTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogTableIndex.setStatus(_A)
class _HpnsaEventLogEntryDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaEventLogEntryDate_Type.__name__=_E
_HpnsaEventLogEntryDate_Object=MibTableColumn
hpnsaEventLogEntryDate=_HpnsaEventLogEntryDate_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,2),_HpnsaEventLogEntryDate_Type())
hpnsaEventLogEntryDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryDate.setStatus(_A)
class _HpnsaEventLogEntryDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryDescr_Type.__name__=_C
_HpnsaEventLogEntryDescr_Object=MibTableColumn
hpnsaEventLogEntryDescr=_HpnsaEventLogEntryDescr_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,3),_HpnsaEventLogEntryDescr_Type())
hpnsaEventLogEntryDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryDescr.setStatus(_A)
class _HpnsaEventLogEntryTrapID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryTrapID_Type.__name__=_C
_HpnsaEventLogEntryTrapID_Object=MibTableColumn
hpnsaEventLogEntryTrapID=_HpnsaEventLogEntryTrapID_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,4),_HpnsaEventLogEntryTrapID_Type())
hpnsaEventLogEntryTrapID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryTrapID.setStatus(_A)
class _HpnsaEventLogEntryVB1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryVB1_Type.__name__=_C
_HpnsaEventLogEntryVB1_Object=MibTableColumn
hpnsaEventLogEntryVB1=_HpnsaEventLogEntryVB1_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,5),_HpnsaEventLogEntryVB1_Type())
hpnsaEventLogEntryVB1.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryVB1.setStatus(_A)
class _HpnsaEventLogEntryVB2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryVB2_Type.__name__=_C
_HpnsaEventLogEntryVB2_Object=MibTableColumn
hpnsaEventLogEntryVB2=_HpnsaEventLogEntryVB2_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,6),_HpnsaEventLogEntryVB2_Type())
hpnsaEventLogEntryVB2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryVB2.setStatus(_A)
class _HpnsaEventLogEntryVB3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryVB3_Type.__name__=_C
_HpnsaEventLogEntryVB3_Object=MibTableColumn
hpnsaEventLogEntryVB3=_HpnsaEventLogEntryVB3_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,7),_HpnsaEventLogEntryVB3_Type())
hpnsaEventLogEntryVB3.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryVB3.setStatus(_A)
class _HpnsaEventLogEntryVB4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryVB4_Type.__name__=_C
_HpnsaEventLogEntryVB4_Object=MibTableColumn
hpnsaEventLogEntryVB4=_HpnsaEventLogEntryVB4_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,8),_HpnsaEventLogEntryVB4_Type())
hpnsaEventLogEntryVB4.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryVB4.setStatus(_A)
class _HpnsaEventLogEntryVB5_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryVB5_Type.__name__=_C
_HpnsaEventLogEntryVB5_Object=MibTableColumn
hpnsaEventLogEntryVB5=_HpnsaEventLogEntryVB5_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,9),_HpnsaEventLogEntryVB5_Type())
hpnsaEventLogEntryVB5.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryVB5.setStatus(_A)
class _HpnsaEventLogEntryVB6_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryVB6_Type.__name__=_C
_HpnsaEventLogEntryVB6_Object=MibTableColumn
hpnsaEventLogEntryVB6=_HpnsaEventLogEntryVB6_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,10),_HpnsaEventLogEntryVB6_Type())
hpnsaEventLogEntryVB6.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryVB6.setStatus(_A)
class _HpnsaEventLogEntryVB7_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryVB7_Type.__name__=_C
_HpnsaEventLogEntryVB7_Object=MibTableColumn
hpnsaEventLogEntryVB7=_HpnsaEventLogEntryVB7_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,11),_HpnsaEventLogEntryVB7_Type())
hpnsaEventLogEntryVB7.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryVB7.setStatus(_A)
class _HpnsaEventLogEntryVB8_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryVB8_Type.__name__=_C
_HpnsaEventLogEntryVB8_Object=MibTableColumn
hpnsaEventLogEntryVB8=_HpnsaEventLogEntryVB8_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,12),_HpnsaEventLogEntryVB8_Type())
hpnsaEventLogEntryVB8.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryVB8.setStatus(_A)
class _HpnsaEventLogEntryAdvisory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_HpnsaEventLogEntryAdvisory_Type.__name__=_C
_HpnsaEventLogEntryAdvisory_Object=MibTableColumn
hpnsaEventLogEntryAdvisory=_HpnsaEventLogEntryAdvisory_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,13),_HpnsaEventLogEntryAdvisory_Type())
hpnsaEventLogEntryAdvisory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryAdvisory.setStatus(_A)
class _HpnsaEventLogEntryReportEntity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntryReportEntity_Type.__name__=_C
_HpnsaEventLogEntryReportEntity_Object=MibTableColumn
hpnsaEventLogEntryReportEntity=_HpnsaEventLogEntryReportEntity_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,14),_HpnsaEventLogEntryReportEntity_Type())
hpnsaEventLogEntryReportEntity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryReportEntity.setStatus(_A)
class _HpnsaEventLogEntrySeverity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogEntrySeverity_Type.__name__=_C
_HpnsaEventLogEntrySeverity_Object=MibTableColumn
hpnsaEventLogEntrySeverity=_HpnsaEventLogEntrySeverity_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,15),_HpnsaEventLogEntrySeverity_Type())
hpnsaEventLogEntrySeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntrySeverity.setStatus(_A)
class _HpnsaEventLogEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,6,9,15)));namedValues=NamedValues(*((_K,2),(_L,3),(_M,6),(_N,9),(_O,15)))
_HpnsaEventLogEntryStatus_Type.__name__=_D
_HpnsaEventLogEntryStatus_Object=MibTableColumn
hpnsaEventLogEntryStatus=_HpnsaEventLogEntryStatus_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,16),_HpnsaEventLogEntryStatus_Type())
hpnsaEventLogEntryStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnsaEventLogEntryStatus.setStatus(_A)
_HpnsaEventLogEntryInfo_Type=Integer32
_HpnsaEventLogEntryInfo_Object=MibTableColumn
hpnsaEventLogEntryInfo=_HpnsaEventLogEntryInfo_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,17),_HpnsaEventLogEntryInfo_Type())
hpnsaEventLogEntryInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryInfo.setStatus(_A)
class _HpnsaEventLogEntryUpdateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaEventLogEntryUpdateTime_Type.__name__=_E
_HpnsaEventLogEntryUpdateTime_Object=MibTableColumn
hpnsaEventLogEntryUpdateTime=_HpnsaEventLogEntryUpdateTime_Object((1,3,6,1,4,1,11,2,23,19,5,5,1,18),_HpnsaEventLogEntryUpdateTime_Type())
hpnsaEventLogEntryUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogEntryUpdateTime.setStatus(_A)
_HpnsaEventLogNumberOfEvents_Type=Integer32
_HpnsaEventLogNumberOfEvents_Object=MibScalar
hpnsaEventLogNumberOfEvents=_HpnsaEventLogNumberOfEvents_Object((1,3,6,1,4,1,11,2,23,19,5,6),_HpnsaEventLogNumberOfEvents_Type())
hpnsaEventLogNumberOfEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogNumberOfEvents.setStatus(_A)
class _HpnsaEventLogAggregationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),('degraded',3),('failed',4)))
_HpnsaEventLogAggregationStatus_Type.__name__=_D
_HpnsaEventLogAggregationStatus_Object=MibScalar
hpnsaEventLogAggregationStatus=_HpnsaEventLogAggregationStatus_Object((1,3,6,1,4,1,11,2,23,19,5,7),_HpnsaEventLogAggregationStatus_Type())
hpnsaEventLogAggregationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogAggregationStatus.setStatus(_A)
_HpnsaEventLogLocalTable_Object=MibTable
hpnsaEventLogLocalTable=_HpnsaEventLogLocalTable_Object((1,3,6,1,4,1,11,2,23,19,5,8))
if mibBuilder.loadTexts:hpnsaEventLogLocalTable.setStatus(_A)
_HpnsaEventLogLocalTableEntry_Object=MibTableRow
hpnsaEventLogLocalTableEntry=_HpnsaEventLogLocalTableEntry_Object((1,3,6,1,4,1,11,2,23,19,5,8,1))
hpnsaEventLogLocalTableEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:hpnsaEventLogLocalTableEntry.setStatus(_A)
_HpnsaEventLogLocalTableIndex_Type=Integer32
_HpnsaEventLogLocalTableIndex_Object=MibTableColumn
hpnsaEventLogLocalTableIndex=_HpnsaEventLogLocalTableIndex_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,1),_HpnsaEventLogLocalTableIndex_Type())
hpnsaEventLogLocalTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalTableIndex.setStatus(_A)
class _HpnsaEventLogLocalEntryDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaEventLogLocalEntryDate_Type.__name__=_E
_HpnsaEventLogLocalEntryDate_Object=MibTableColumn
hpnsaEventLogLocalEntryDate=_HpnsaEventLogLocalEntryDate_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,2),_HpnsaEventLogLocalEntryDate_Type())
hpnsaEventLogLocalEntryDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryDate.setStatus(_A)
class _HpnsaEventLogLocalEntryDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryDescr_Type.__name__=_C
_HpnsaEventLogLocalEntryDescr_Object=MibTableColumn
hpnsaEventLogLocalEntryDescr=_HpnsaEventLogLocalEntryDescr_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,3),_HpnsaEventLogLocalEntryDescr_Type())
hpnsaEventLogLocalEntryDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryDescr.setStatus(_A)
class _HpnsaEventLogLocalEntryTrapID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryTrapID_Type.__name__=_C
_HpnsaEventLogLocalEntryTrapID_Object=MibTableColumn
hpnsaEventLogLocalEntryTrapID=_HpnsaEventLogLocalEntryTrapID_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,4),_HpnsaEventLogLocalEntryTrapID_Type())
hpnsaEventLogLocalEntryTrapID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryTrapID.setStatus(_A)
class _HpnsaEventLogLocalEntryVB1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryVB1_Type.__name__=_C
_HpnsaEventLogLocalEntryVB1_Object=MibTableColumn
hpnsaEventLogLocalEntryVB1=_HpnsaEventLogLocalEntryVB1_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,5),_HpnsaEventLogLocalEntryVB1_Type())
hpnsaEventLogLocalEntryVB1.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryVB1.setStatus(_A)
class _HpnsaEventLogLocalEntryVB2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryVB2_Type.__name__=_C
_HpnsaEventLogLocalEntryVB2_Object=MibTableColumn
hpnsaEventLogLocalEntryVB2=_HpnsaEventLogLocalEntryVB2_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,6),_HpnsaEventLogLocalEntryVB2_Type())
hpnsaEventLogLocalEntryVB2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryVB2.setStatus(_A)
class _HpnsaEventLogLocalEntryVB3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryVB3_Type.__name__=_C
_HpnsaEventLogLocalEntryVB3_Object=MibTableColumn
hpnsaEventLogLocalEntryVB3=_HpnsaEventLogLocalEntryVB3_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,7),_HpnsaEventLogLocalEntryVB3_Type())
hpnsaEventLogLocalEntryVB3.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryVB3.setStatus(_A)
class _HpnsaEventLogLocalEntryVB4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryVB4_Type.__name__=_C
_HpnsaEventLogLocalEntryVB4_Object=MibTableColumn
hpnsaEventLogLocalEntryVB4=_HpnsaEventLogLocalEntryVB4_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,8),_HpnsaEventLogLocalEntryVB4_Type())
hpnsaEventLogLocalEntryVB4.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryVB4.setStatus(_A)
class _HpnsaEventLogLocalEntryVB5_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryVB5_Type.__name__=_C
_HpnsaEventLogLocalEntryVB5_Object=MibTableColumn
hpnsaEventLogLocalEntryVB5=_HpnsaEventLogLocalEntryVB5_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,9),_HpnsaEventLogLocalEntryVB5_Type())
hpnsaEventLogLocalEntryVB5.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryVB5.setStatus(_A)
class _HpnsaEventLogLocalEntryVB6_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryVB6_Type.__name__=_C
_HpnsaEventLogLocalEntryVB6_Object=MibTableColumn
hpnsaEventLogLocalEntryVB6=_HpnsaEventLogLocalEntryVB6_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,10),_HpnsaEventLogLocalEntryVB6_Type())
hpnsaEventLogLocalEntryVB6.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryVB6.setStatus(_A)
class _HpnsaEventLogLocalEntryVB7_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryVB7_Type.__name__=_C
_HpnsaEventLogLocalEntryVB7_Object=MibTableColumn
hpnsaEventLogLocalEntryVB7=_HpnsaEventLogLocalEntryVB7_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,11),_HpnsaEventLogLocalEntryVB7_Type())
hpnsaEventLogLocalEntryVB7.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryVB7.setStatus(_A)
class _HpnsaEventLogLocalEntryVB8_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryVB8_Type.__name__=_C
_HpnsaEventLogLocalEntryVB8_Object=MibTableColumn
hpnsaEventLogLocalEntryVB8=_HpnsaEventLogLocalEntryVB8_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,12),_HpnsaEventLogLocalEntryVB8_Type())
hpnsaEventLogLocalEntryVB8.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryVB8.setStatus(_A)
class _HpnsaEventLogLocalEntryAdvisory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_HpnsaEventLogLocalEntryAdvisory_Type.__name__=_C
_HpnsaEventLogLocalEntryAdvisory_Object=MibTableColumn
hpnsaEventLogLocalEntryAdvisory=_HpnsaEventLogLocalEntryAdvisory_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,13),_HpnsaEventLogLocalEntryAdvisory_Type())
hpnsaEventLogLocalEntryAdvisory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryAdvisory.setStatus(_A)
class _HpnsaEventLogLocalEntryReportEntity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntryReportEntity_Type.__name__=_C
_HpnsaEventLogLocalEntryReportEntity_Object=MibTableColumn
hpnsaEventLogLocalEntryReportEntity=_HpnsaEventLogLocalEntryReportEntity_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,14),_HpnsaEventLogLocalEntryReportEntity_Type())
hpnsaEventLogLocalEntryReportEntity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryReportEntity.setStatus(_A)
class _HpnsaEventLogLocalEntrySeverity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEventLogLocalEntrySeverity_Type.__name__=_C
_HpnsaEventLogLocalEntrySeverity_Object=MibTableColumn
hpnsaEventLogLocalEntrySeverity=_HpnsaEventLogLocalEntrySeverity_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,15),_HpnsaEventLogLocalEntrySeverity_Type())
hpnsaEventLogLocalEntrySeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntrySeverity.setStatus(_A)
class _HpnsaEventLogLocalEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,6,9,15)));namedValues=NamedValues(*((_K,2),(_L,3),(_M,6),(_N,9),(_O,15)))
_HpnsaEventLogLocalEntryStatus_Type.__name__=_D
_HpnsaEventLogLocalEntryStatus_Object=MibTableColumn
hpnsaEventLogLocalEntryStatus=_HpnsaEventLogLocalEntryStatus_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,16),_HpnsaEventLogLocalEntryStatus_Type())
hpnsaEventLogLocalEntryStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryStatus.setStatus(_A)
_HpnsaEventLogLocalEntryInfo_Type=Integer32
_HpnsaEventLogLocalEntryInfo_Object=MibTableColumn
hpnsaEventLogLocalEntryInfo=_HpnsaEventLogLocalEntryInfo_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,17),_HpnsaEventLogLocalEntryInfo_Type())
hpnsaEventLogLocalEntryInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryInfo.setStatus(_A)
class _HpnsaEventLogLocalEntryUpdateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaEventLogLocalEntryUpdateTime_Type.__name__=_E
_HpnsaEventLogLocalEntryUpdateTime_Object=MibTableColumn
hpnsaEventLogLocalEntryUpdateTime=_HpnsaEventLogLocalEntryUpdateTime_Object((1,3,6,1,4,1,11,2,23,19,5,8,1,18),_HpnsaEventLogLocalEntryUpdateTime_Type())
hpnsaEventLogLocalEntryUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogLocalEntryUpdateTime.setStatus(_A)
_HpnsaEventLogNumOfLocalEvents_Type=Integer32
_HpnsaEventLogNumOfLocalEvents_Object=MibScalar
hpnsaEventLogNumOfLocalEvents=_HpnsaEventLogNumOfLocalEvents_Object((1,3,6,1,4,1,11,2,23,19,5,9),_HpnsaEventLogNumOfLocalEvents_Type())
hpnsaEventLogNumOfLocalEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEventLogNumOfLocalEvents.setStatus(_A)
_HpnsaEventCustomerAcknowledgeActions_ObjectIdentity=ObjectIdentity
hpnsaEventCustomerAcknowledgeActions=_HpnsaEventCustomerAcknowledgeActions_ObjectIdentity((1,3,6,1,4,1,11,2,23,19,6))
class _HpnsaEventClearLEDs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clearAttentionLED',1))
_HpnsaEventClearLEDs_Type.__name__=_D
_HpnsaEventClearLEDs_Object=MibScalar
hpnsaEventClearLEDs=_HpnsaEventClearLEDs_Object((1,3,6,1,4,1,11,2,23,19,6,1),_HpnsaEventClearLEDs_Type())
hpnsaEventClearLEDs.setMaxAccess('write-only')
if mibBuilder.loadTexts:hpnsaEventClearLEDs.setStatus('optional')
mibBuilder.exportSymbols(_F,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaEventLog':hpnsaEventLog,'hpnsaEventLogRev':hpnsaEventLogRev,'hpnsaEventLogMibRevMajor':hpnsaEventLogMibRevMajor,'hpnsaEventLogMibRevMinor':hpnsaEventLogMibRevMinor,'hpnsaEventLogAgentInfo':hpnsaEventLogAgentInfo,'hpnsaEventLogAgentTable':hpnsaEventLogAgentTable,'hpnsaEventLogAgentEntry':hpnsaEventLogAgentEntry,_I:hpnsaEventLogAgentIndex,'hpnsaEventLogAgentName':hpnsaEventLogAgentName,'hpnsaEventLogAgentVersion':hpnsaEventLogAgentVersion,'hpnsaEventLogAgentDate':hpnsaEventLogAgentDate,'hpnsaEventAgentCfgInfo':hpnsaEventAgentCfgInfo,'hpnsaEventCfgTable':hpnsaEventCfgTable,'hpnsaEventCfgTableEntry':hpnsaEventCfgTableEntry,_J:hpnsaEventLogRecType,'hpnsaEventLogRecTrapEnable':hpnsaEventLogRecTrapEnable,'hpnsaEventLogPresenceId':hpnsaEventLogPresenceId,'hpnsaEccPresent':hpnsaEccPresent,'hpnsaPostPresent':hpnsaPostPresent,'hpnsaTempVoltagePresent':hpnsaTempVoltagePresent,'hpnsaASRPresent':hpnsaASRPresent,'hpnsaNMIPresent':hpnsaNMIPresent,'hpnsaEventLogStatistics':hpnsaEventLogStatistics,'hpnsaEventLogPercentFull':hpnsaEventLogPercentFull,'hpnsaEventLogLastErasedDate':hpnsaEventLogLastErasedDate,'hpnsaEventLogErasures':hpnsaEventLogErasures,'hpnsaEventLogEraseLog':hpnsaEventLogEraseLog,'hpnsaEventLogTable':hpnsaEventLogTable,'hpnsaEventLogTableEntry':hpnsaEventLogTableEntry,_H:hpnsaEventLogTableIndex,'hpnsaEventLogEntryDate':hpnsaEventLogEntryDate,'hpnsaEventLogEntryDescr':hpnsaEventLogEntryDescr,'hpnsaEventLogEntryTrapID':hpnsaEventLogEntryTrapID,'hpnsaEventLogEntryVB1':hpnsaEventLogEntryVB1,'hpnsaEventLogEntryVB2':hpnsaEventLogEntryVB2,'hpnsaEventLogEntryVB3':hpnsaEventLogEntryVB3,'hpnsaEventLogEntryVB4':hpnsaEventLogEntryVB4,'hpnsaEventLogEntryVB5':hpnsaEventLogEntryVB5,'hpnsaEventLogEntryVB6':hpnsaEventLogEntryVB6,'hpnsaEventLogEntryVB7':hpnsaEventLogEntryVB7,'hpnsaEventLogEntryVB8':hpnsaEventLogEntryVB8,'hpnsaEventLogEntryAdvisory':hpnsaEventLogEntryAdvisory,'hpnsaEventLogEntryReportEntity':hpnsaEventLogEntryReportEntity,'hpnsaEventLogEntrySeverity':hpnsaEventLogEntrySeverity,'hpnsaEventLogEntryStatus':hpnsaEventLogEntryStatus,'hpnsaEventLogEntryInfo':hpnsaEventLogEntryInfo,'hpnsaEventLogEntryUpdateTime':hpnsaEventLogEntryUpdateTime,'hpnsaEventLogNumberOfEvents':hpnsaEventLogNumberOfEvents,'hpnsaEventLogAggregationStatus':hpnsaEventLogAggregationStatus,'hpnsaEventLogLocalTable':hpnsaEventLogLocalTable,'hpnsaEventLogLocalTableEntry':hpnsaEventLogLocalTableEntry,'hpnsaEventLogLocalTableIndex':hpnsaEventLogLocalTableIndex,'hpnsaEventLogLocalEntryDate':hpnsaEventLogLocalEntryDate,'hpnsaEventLogLocalEntryDescr':hpnsaEventLogLocalEntryDescr,'hpnsaEventLogLocalEntryTrapID':hpnsaEventLogLocalEntryTrapID,'hpnsaEventLogLocalEntryVB1':hpnsaEventLogLocalEntryVB1,'hpnsaEventLogLocalEntryVB2':hpnsaEventLogLocalEntryVB2,'hpnsaEventLogLocalEntryVB3':hpnsaEventLogLocalEntryVB3,'hpnsaEventLogLocalEntryVB4':hpnsaEventLogLocalEntryVB4,'hpnsaEventLogLocalEntryVB5':hpnsaEventLogLocalEntryVB5,'hpnsaEventLogLocalEntryVB6':hpnsaEventLogLocalEntryVB6,'hpnsaEventLogLocalEntryVB7':hpnsaEventLogLocalEntryVB7,'hpnsaEventLogLocalEntryVB8':hpnsaEventLogLocalEntryVB8,'hpnsaEventLogLocalEntryAdvisory':hpnsaEventLogLocalEntryAdvisory,'hpnsaEventLogLocalEntryReportEntity':hpnsaEventLogLocalEntryReportEntity,'hpnsaEventLogLocalEntrySeverity':hpnsaEventLogLocalEntrySeverity,'hpnsaEventLogLocalEntryStatus':hpnsaEventLogLocalEntryStatus,'hpnsaEventLogLocalEntryInfo':hpnsaEventLogLocalEntryInfo,'hpnsaEventLogLocalEntryUpdateTime':hpnsaEventLogLocalEntryUpdateTime,'hpnsaEventLogNumOfLocalEvents':hpnsaEventLogNumOfLocalEvents,'hpnsaEventCustomerAcknowledgeActions':hpnsaEventCustomerAcknowledgeActions,'hpnsaEventClearLEDs':hpnsaEventClearLEDs})