_j='ciscoCallHistoryMibGroupRev2'
_i='ciscoCallHistoryMibGroup'
_h='ciscoCallHistoryRetainTimer'
_g='ciscoCallHistoryTableMaxLength'
_f='ciscoCallHistoryMultiplier'
_e='ciscoCallHistoryCurrencyAmount'
_d='ciscoCallHistoryCurrency'
_c='ciscoCallHistoryRecordedUnits'
_b='not-accessible'
_a='ciscoCallHistoryIndex'
_Z='ciscoCallHistoryStartTime'
_Y='read-write'
_X='1995-08-15 00:00'
_W='ciscoCallHistoryMibGlobalsGroup'
_V='ciscoCallHistoryMibGroupRev1'
_U='ciscoCallHistoryReceiveBytes'
_T='ciscoCallHistoryReceivePackets'
_S='ciscoCallHistoryTransmitBytes'
_R='ciscoCallHistoryTransmitPackets'
_Q='ciscoCallHistoryDisconnectTimeOfDay'
_P='ciscoCallHistoryConnectTimeOfDay'
_O='ciscoCallHistoryDialReason'
_N='ciscoCallHistoryCallDisconnectTime'
_M='ciscoCallHistoryCallConnectionTime'
_L='ciscoCallHistoryCallDisconnectCause'
_K='ciscoCallHistoryDestinationHostName'
_J='ciscoCallHistoryDestinationAddress'
_I='ciscoCallHistoryInterfaceNumber'
_H='ciscoCallHistoryCalledNumber'
_G='ciscoCallHistoryCallingNumber'
_F='OctetString'
_E='obsolete'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-CALL-HISTORY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoCallHistoryMib=ModuleIdentity((1,3,6,1,4,1,9,9,27))
if mibBuilder.loadTexts:ciscoCallHistoryMib.setRevisions((_X,'1995-07-20 00:00',_X,'1996-11-19 00:00'))
_CiscoCallHistoryMibObjects_ObjectIdentity=ObjectIdentity
ciscoCallHistoryMibObjects=_CiscoCallHistoryMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,27,1))
_CiscoCallHistory_ObjectIdentity=ObjectIdentity
ciscoCallHistory=_CiscoCallHistory_ObjectIdentity((1,3,6,1,4,1,9,9,27,1,1))
class _CiscoCallHistoryTableMaxLength_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CiscoCallHistoryTableMaxLength_Type.__name__=_D
_CiscoCallHistoryTableMaxLength_Object=MibScalar
ciscoCallHistoryTableMaxLength=_CiscoCallHistoryTableMaxLength_Object((1,3,6,1,4,1,9,9,27,1,1,1),_CiscoCallHistoryTableMaxLength_Type())
ciscoCallHistoryTableMaxLength.setMaxAccess(_Y)
if mibBuilder.loadTexts:ciscoCallHistoryTableMaxLength.setStatus(_B)
class _CiscoCallHistoryRetainTimer_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CiscoCallHistoryRetainTimer_Type.__name__=_D
_CiscoCallHistoryRetainTimer_Object=MibScalar
ciscoCallHistoryRetainTimer=_CiscoCallHistoryRetainTimer_Object((1,3,6,1,4,1,9,9,27,1,1,2),_CiscoCallHistoryRetainTimer_Type())
ciscoCallHistoryRetainTimer.setMaxAccess(_Y)
if mibBuilder.loadTexts:ciscoCallHistoryRetainTimer.setStatus(_B)
if mibBuilder.loadTexts:ciscoCallHistoryRetainTimer.setUnits('minutes')
_CiscoCallHistoryTable_Object=MibTable
ciscoCallHistoryTable=_CiscoCallHistoryTable_Object((1,3,6,1,4,1,9,9,27,1,1,3))
if mibBuilder.loadTexts:ciscoCallHistoryTable.setStatus(_B)
_CiscoCallHistoryEntry_Object=MibTableRow
ciscoCallHistoryEntry=_CiscoCallHistoryEntry_Object((1,3,6,1,4,1,9,9,27,1,1,3,1))
ciscoCallHistoryEntry.setIndexNames((0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:ciscoCallHistoryEntry.setStatus(_B)
_CiscoCallHistoryStartTime_Type=TimeStamp
_CiscoCallHistoryStartTime_Object=MibTableColumn
ciscoCallHistoryStartTime=_CiscoCallHistoryStartTime_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,1),_CiscoCallHistoryStartTime_Type())
ciscoCallHistoryStartTime.setMaxAccess(_b)
if mibBuilder.loadTexts:ciscoCallHistoryStartTime.setStatus(_B)
class _CiscoCallHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoCallHistoryIndex_Type.__name__=_D
_CiscoCallHistoryIndex_Object=MibTableColumn
ciscoCallHistoryIndex=_CiscoCallHistoryIndex_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,2),_CiscoCallHistoryIndex_Type())
ciscoCallHistoryIndex.setMaxAccess(_b)
if mibBuilder.loadTexts:ciscoCallHistoryIndex.setStatus(_B)
class _CiscoCallHistoryCallingNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CiscoCallHistoryCallingNumber_Type.__name__=_F
_CiscoCallHistoryCallingNumber_Object=MibTableColumn
ciscoCallHistoryCallingNumber=_CiscoCallHistoryCallingNumber_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,3),_CiscoCallHistoryCallingNumber_Type())
ciscoCallHistoryCallingNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryCallingNumber.setStatus(_B)
class _CiscoCallHistoryCalledNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CiscoCallHistoryCalledNumber_Type.__name__=_F
_CiscoCallHistoryCalledNumber_Object=MibTableColumn
ciscoCallHistoryCalledNumber=_CiscoCallHistoryCalledNumber_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,4),_CiscoCallHistoryCalledNumber_Type())
ciscoCallHistoryCalledNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryCalledNumber.setStatus(_B)
_CiscoCallHistoryInterfaceNumber_Type=InterfaceIndex
_CiscoCallHistoryInterfaceNumber_Object=MibTableColumn
ciscoCallHistoryInterfaceNumber=_CiscoCallHistoryInterfaceNumber_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,5),_CiscoCallHistoryInterfaceNumber_Type())
ciscoCallHistoryInterfaceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryInterfaceNumber.setStatus(_B)
class _CiscoCallHistoryDestinationAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,60))
_CiscoCallHistoryDestinationAddress_Type.__name__=_F
_CiscoCallHistoryDestinationAddress_Object=MibTableColumn
ciscoCallHistoryDestinationAddress=_CiscoCallHistoryDestinationAddress_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,6),_CiscoCallHistoryDestinationAddress_Type())
ciscoCallHistoryDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryDestinationAddress.setStatus(_B)
_CiscoCallHistoryDestinationHostName_Type=DisplayString
_CiscoCallHistoryDestinationHostName_Object=MibTableColumn
ciscoCallHistoryDestinationHostName=_CiscoCallHistoryDestinationHostName_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,7),_CiscoCallHistoryDestinationHostName_Type())
ciscoCallHistoryDestinationHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryDestinationHostName.setStatus(_B)
class _CiscoCallHistoryCallDisconnectCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('normalDisconnectSent',2),('normalDisconnectReceived',3),('networkOutOfOrder',4),('callRejected',5),('userBusy',6),('noCircuitChannelAvailable',7),('interworkingError',8)))
_CiscoCallHistoryCallDisconnectCause_Type.__name__=_D
_CiscoCallHistoryCallDisconnectCause_Object=MibTableColumn
ciscoCallHistoryCallDisconnectCause=_CiscoCallHistoryCallDisconnectCause_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,8),_CiscoCallHistoryCallDisconnectCause_Type())
ciscoCallHistoryCallDisconnectCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryCallDisconnectCause.setStatus(_B)
_CiscoCallHistoryCallConnectionTime_Type=TimeStamp
_CiscoCallHistoryCallConnectionTime_Object=MibTableColumn
ciscoCallHistoryCallConnectionTime=_CiscoCallHistoryCallConnectionTime_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,9),_CiscoCallHistoryCallConnectionTime_Type())
ciscoCallHistoryCallConnectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryCallConnectionTime.setStatus(_B)
_CiscoCallHistoryCallDisconnectTime_Type=TimeStamp
_CiscoCallHistoryCallDisconnectTime_Object=MibTableColumn
ciscoCallHistoryCallDisconnectTime=_CiscoCallHistoryCallDisconnectTime_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,10),_CiscoCallHistoryCallDisconnectTime_Type())
ciscoCallHistoryCallDisconnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryCallDisconnectTime.setStatus(_B)
_CiscoCallHistoryDialReason_Type=DisplayString
_CiscoCallHistoryDialReason_Object=MibTableColumn
ciscoCallHistoryDialReason=_CiscoCallHistoryDialReason_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,11),_CiscoCallHistoryDialReason_Type())
ciscoCallHistoryDialReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryDialReason.setStatus(_B)
_CiscoCallHistoryConnectTimeOfDay_Type=DisplayString
_CiscoCallHistoryConnectTimeOfDay_Object=MibTableColumn
ciscoCallHistoryConnectTimeOfDay=_CiscoCallHistoryConnectTimeOfDay_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,12),_CiscoCallHistoryConnectTimeOfDay_Type())
ciscoCallHistoryConnectTimeOfDay.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryConnectTimeOfDay.setStatus(_B)
_CiscoCallHistoryDisconnectTimeOfDay_Type=DisplayString
_CiscoCallHistoryDisconnectTimeOfDay_Object=MibTableColumn
ciscoCallHistoryDisconnectTimeOfDay=_CiscoCallHistoryDisconnectTimeOfDay_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,13),_CiscoCallHistoryDisconnectTimeOfDay_Type())
ciscoCallHistoryDisconnectTimeOfDay.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryDisconnectTimeOfDay.setStatus(_B)
_CiscoCallHistoryTransmitPackets_Type=Integer32
_CiscoCallHistoryTransmitPackets_Object=MibTableColumn
ciscoCallHistoryTransmitPackets=_CiscoCallHistoryTransmitPackets_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,14),_CiscoCallHistoryTransmitPackets_Type())
ciscoCallHistoryTransmitPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryTransmitPackets.setStatus(_B)
_CiscoCallHistoryTransmitBytes_Type=Integer32
_CiscoCallHistoryTransmitBytes_Object=MibTableColumn
ciscoCallHistoryTransmitBytes=_CiscoCallHistoryTransmitBytes_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,15),_CiscoCallHistoryTransmitBytes_Type())
ciscoCallHistoryTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryTransmitBytes.setStatus(_B)
_CiscoCallHistoryReceivePackets_Type=Integer32
_CiscoCallHistoryReceivePackets_Object=MibTableColumn
ciscoCallHistoryReceivePackets=_CiscoCallHistoryReceivePackets_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,16),_CiscoCallHistoryReceivePackets_Type())
ciscoCallHistoryReceivePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryReceivePackets.setStatus(_B)
_CiscoCallHistoryReceiveBytes_Type=Integer32
_CiscoCallHistoryReceiveBytes_Object=MibTableColumn
ciscoCallHistoryReceiveBytes=_CiscoCallHistoryReceiveBytes_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,17),_CiscoCallHistoryReceiveBytes_Type())
ciscoCallHistoryReceiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryReceiveBytes.setStatus(_B)
class _CiscoCallHistoryRecordedUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CiscoCallHistoryRecordedUnits_Type.__name__=_D
_CiscoCallHistoryRecordedUnits_Object=MibTableColumn
ciscoCallHistoryRecordedUnits=_CiscoCallHistoryRecordedUnits_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,18),_CiscoCallHistoryRecordedUnits_Type())
ciscoCallHistoryRecordedUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryRecordedUnits.setStatus(_B)
_CiscoCallHistoryCurrency_Type=DisplayString
_CiscoCallHistoryCurrency_Object=MibTableColumn
ciscoCallHistoryCurrency=_CiscoCallHistoryCurrency_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,19),_CiscoCallHistoryCurrency_Type())
ciscoCallHistoryCurrency.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryCurrency.setStatus(_B)
class _CiscoCallHistoryCurrencyAmount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CiscoCallHistoryCurrencyAmount_Type.__name__=_D
_CiscoCallHistoryCurrencyAmount_Object=MibTableColumn
ciscoCallHistoryCurrencyAmount=_CiscoCallHistoryCurrencyAmount_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,20),_CiscoCallHistoryCurrencyAmount_Type())
ciscoCallHistoryCurrencyAmount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryCurrencyAmount.setStatus(_B)
class _CiscoCallHistoryMultiplier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('oneThousandth',0),('oneHundreth',1),('oneTenth',2),('one',3),('ten',4),('hundred',5),('thousand',6)))
_CiscoCallHistoryMultiplier_Type.__name__=_D
_CiscoCallHistoryMultiplier_Object=MibTableColumn
ciscoCallHistoryMultiplier=_CiscoCallHistoryMultiplier_Object((1,3,6,1,4,1,9,9,27,1,1,3,1,21),_CiscoCallHistoryMultiplier_Type())
ciscoCallHistoryMultiplier.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoCallHistoryMultiplier.setStatus(_B)
_CiscoCallHistoryMibConformance_ObjectIdentity=ObjectIdentity
ciscoCallHistoryMibConformance=_CiscoCallHistoryMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,27,2))
_CiscoCallHistoryMibCompliances_ObjectIdentity=ObjectIdentity
ciscoCallHistoryMibCompliances=_CiscoCallHistoryMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,27,2,1))
_CiscoCallHistoryMibGroups_ObjectIdentity=ObjectIdentity
ciscoCallHistoryMibGroups=_CiscoCallHistoryMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,27,2,2))
ciscoCallHistoryMibGroup=ObjectGroup((1,3,6,1,4,1,9,9,27,2,2,1))
ciscoCallHistoryMibGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoCallHistoryMibGroup.setStatus(_E)
ciscoCallHistoryMibGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,27,2,2,2))
ciscoCallHistoryMibGroupRev1.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ciscoCallHistoryMibGroupRev1.setStatus(_E)
ciscoCallHistoryMibGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,27,2,2,3))
ciscoCallHistoryMibGroupRev2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ciscoCallHistoryMibGroupRev2.setStatus(_B)
ciscoCallHistoryMibGlobalsGroup=ObjectGroup((1,3,6,1,4,1,9,9,27,2,2,4))
ciscoCallHistoryMibGlobalsGroup.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:ciscoCallHistoryMibGlobalsGroup.setStatus(_B)
ciscoCallHistoryMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,27,2,1,1))
ciscoCallHistoryMibCompliance.setObjects((_A,_i))
if mibBuilder.loadTexts:ciscoCallHistoryMibCompliance.setStatus(_E)
ciscoCallHistoryMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,27,2,1,2))
ciscoCallHistoryMibComplianceRev1.setObjects((_A,_V))
if mibBuilder.loadTexts:ciscoCallHistoryMibComplianceRev1.setStatus(_E)
ciscoCallHistoryMibComplianceV11R01=ModuleCompliance((1,3,6,1,4,1,9,9,27,2,1,3))
ciscoCallHistoryMibComplianceV11R01.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoCallHistoryMibComplianceV11R01.setStatus(_E)
ciscoCallHistoryMibComplianceV11R02=ModuleCompliance((1,3,6,1,4,1,9,9,27,2,1,4))
ciscoCallHistoryMibComplianceV11R02.setObjects(*((_A,_j),(_A,_W)))
if mibBuilder.loadTexts:ciscoCallHistoryMibComplianceV11R02.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoCallHistoryMib':ciscoCallHistoryMib,'ciscoCallHistoryMibObjects':ciscoCallHistoryMibObjects,'ciscoCallHistory':ciscoCallHistory,_g:ciscoCallHistoryTableMaxLength,_h:ciscoCallHistoryRetainTimer,'ciscoCallHistoryTable':ciscoCallHistoryTable,'ciscoCallHistoryEntry':ciscoCallHistoryEntry,_Z:ciscoCallHistoryStartTime,_a:ciscoCallHistoryIndex,_G:ciscoCallHistoryCallingNumber,_H:ciscoCallHistoryCalledNumber,_I:ciscoCallHistoryInterfaceNumber,_J:ciscoCallHistoryDestinationAddress,_K:ciscoCallHistoryDestinationHostName,_L:ciscoCallHistoryCallDisconnectCause,_M:ciscoCallHistoryCallConnectionTime,_N:ciscoCallHistoryCallDisconnectTime,_O:ciscoCallHistoryDialReason,_P:ciscoCallHistoryConnectTimeOfDay,_Q:ciscoCallHistoryDisconnectTimeOfDay,_R:ciscoCallHistoryTransmitPackets,_S:ciscoCallHistoryTransmitBytes,_T:ciscoCallHistoryReceivePackets,_U:ciscoCallHistoryReceiveBytes,_c:ciscoCallHistoryRecordedUnits,_d:ciscoCallHistoryCurrency,_e:ciscoCallHistoryCurrencyAmount,_f:ciscoCallHistoryMultiplier,'ciscoCallHistoryMibConformance':ciscoCallHistoryMibConformance,'ciscoCallHistoryMibCompliances':ciscoCallHistoryMibCompliances,'ciscoCallHistoryMibCompliance':ciscoCallHistoryMibCompliance,'ciscoCallHistoryMibComplianceRev1':ciscoCallHistoryMibComplianceRev1,'ciscoCallHistoryMibComplianceV11R01':ciscoCallHistoryMibComplianceV11R01,'ciscoCallHistoryMibComplianceV11R02':ciscoCallHistoryMibComplianceV11R02,'ciscoCallHistoryMibGroups':ciscoCallHistoryMibGroups,_i:ciscoCallHistoryMibGroup,_V:ciscoCallHistoryMibGroupRev1,_j:ciscoCallHistoryMibGroupRev2,_W:ciscoCallHistoryMibGlobalsGroup})