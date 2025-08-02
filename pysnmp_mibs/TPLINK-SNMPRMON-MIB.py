_R='tpSnmpRmonAlarmCtrlIndex'
_Q='tpSnmpRmonEventLogIndex'
_P='tpSnmpRmonEventLogEventIndex'
_O='tpSnmpRmonEventCtrlIndex'
_N='tpSnmpRmonHistoryDataIndex'
_M='tpSnmpRmonHistoryCtrlIndex'
_L='EntryStatus'
_K='tpSnmpRmonStatsCtrlIndex'
_J='enable'
_I='disable'
_H='read-create'
_G='Packets'
_F='TPLINK-SNMPRMON-MIB'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkSnmpMIBObjects,=mibBuilder.importSymbols('TPLINK-SNMP-MIB','tplinkSnmpMIBObjects')
class EntryStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
_TpSnmpRmonControl_ObjectIdentity=ObjectIdentity
tpSnmpRmonControl=_TpSnmpRmonControl_ObjectIdentity((1,3,6,1,4,1,11863,6,32,1,2))
_TpSnmpRmonStatisticsCtrl_ObjectIdentity=ObjectIdentity
tpSnmpRmonStatisticsCtrl=_TpSnmpRmonStatisticsCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,32,1,2,1))
_TpSnmpRmonStatsCtrlTable_Object=MibTable
tpSnmpRmonStatsCtrlTable=_TpSnmpRmonStatsCtrlTable_Object((1,3,6,1,4,1,11863,6,32,1,2,1,1))
if mibBuilder.loadTexts:tpSnmpRmonStatsCtrlTable.setStatus(_A)
_TpSnmpRmonStatsCtrlEntry_Object=MibTableRow
tpSnmpRmonStatsCtrlEntry=_TpSnmpRmonStatsCtrlEntry_Object((1,3,6,1,4,1,11863,6,32,1,2,1,1,1))
tpSnmpRmonStatsCtrlEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:tpSnmpRmonStatsCtrlEntry.setStatus(_A)
class _TpSnmpRmonStatsCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpSnmpRmonStatsCtrlIndex_Type.__name__=_C
_TpSnmpRmonStatsCtrlIndex_Object=MibTableColumn
tpSnmpRmonStatsCtrlIndex=_TpSnmpRmonStatsCtrlIndex_Object((1,3,6,1,4,1,11863,6,32,1,2,1,1,1,1),_TpSnmpRmonStatsCtrlIndex_Type())
tpSnmpRmonStatsCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonStatsCtrlIndex.setStatus(_A)
_TpSnmpRmonStatsCtrlDataSource_Type=OctetString
_TpSnmpRmonStatsCtrlDataSource_Object=MibTableColumn
tpSnmpRmonStatsCtrlDataSource=_TpSnmpRmonStatsCtrlDataSource_Object((1,3,6,1,4,1,11863,6,32,1,2,1,1,1,2),_TpSnmpRmonStatsCtrlDataSource_Type())
tpSnmpRmonStatsCtrlDataSource.setMaxAccess(_H)
if mibBuilder.loadTexts:tpSnmpRmonStatsCtrlDataSource.setStatus(_A)
class _TpSnmpRmonStatsCtrlOwner_Type(OctetString):defaultValue=OctetString('MibBrowser');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_TpSnmpRmonStatsCtrlOwner_Type.__name__=_E
_TpSnmpRmonStatsCtrlOwner_Object=MibTableColumn
tpSnmpRmonStatsCtrlOwner=_TpSnmpRmonStatsCtrlOwner_Object((1,3,6,1,4,1,11863,6,32,1,2,1,1,1,3),_TpSnmpRmonStatsCtrlOwner_Type())
tpSnmpRmonStatsCtrlOwner.setMaxAccess(_H)
if mibBuilder.loadTexts:tpSnmpRmonStatsCtrlOwner.setStatus(_A)
class _TpSnmpRmonStatsCtrlRowStatus_Type(EntryStatus):defaultValue=2
_TpSnmpRmonStatsCtrlRowStatus_Type.__name__=_L
_TpSnmpRmonStatsCtrlRowStatus_Object=MibTableColumn
tpSnmpRmonStatsCtrlRowStatus=_TpSnmpRmonStatsCtrlRowStatus_Object((1,3,6,1,4,1,11863,6,32,1,2,1,1,1,4),_TpSnmpRmonStatsCtrlRowStatus_Type())
tpSnmpRmonStatsCtrlRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:tpSnmpRmonStatsCtrlRowStatus.setStatus(_A)
_TpSnmpRmonHistoryCtrl_ObjectIdentity=ObjectIdentity
tpSnmpRmonHistoryCtrl=_TpSnmpRmonHistoryCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,32,1,2,2))
_TpSnmpRmonHistoryCtrlTable_Object=MibTable
tpSnmpRmonHistoryCtrlTable=_TpSnmpRmonHistoryCtrlTable_Object((1,3,6,1,4,1,11863,6,32,1,2,2,1))
if mibBuilder.loadTexts:tpSnmpRmonHistoryCtrlTable.setStatus(_A)
_TpSnmpRmonHistoryCtrlEntry_Object=MibTableRow
tpSnmpRmonHistoryCtrlEntry=_TpSnmpRmonHistoryCtrlEntry_Object((1,3,6,1,4,1,11863,6,32,1,2,2,1,1))
tpSnmpRmonHistoryCtrlEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:tpSnmpRmonHistoryCtrlEntry.setStatus(_A)
_TpSnmpRmonHistoryCtrlIndex_Type=Integer32
_TpSnmpRmonHistoryCtrlIndex_Object=MibTableColumn
tpSnmpRmonHistoryCtrlIndex=_TpSnmpRmonHistoryCtrlIndex_Object((1,3,6,1,4,1,11863,6,32,1,2,2,1,1,1),_TpSnmpRmonHistoryCtrlIndex_Type())
tpSnmpRmonHistoryCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryCtrlIndex.setStatus(_A)
_TpSnmpRmonHistoryCtrlSourcePort_Type=OctetString
_TpSnmpRmonHistoryCtrlSourcePort_Object=MibTableColumn
tpSnmpRmonHistoryCtrlSourcePort=_TpSnmpRmonHistoryCtrlSourcePort_Object((1,3,6,1,4,1,11863,6,32,1,2,2,1,1,2),_TpSnmpRmonHistoryCtrlSourcePort_Type())
tpSnmpRmonHistoryCtrlSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonHistoryCtrlSourcePort.setStatus(_A)
class _TpSnmpRmonHistoryCtrlInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_TpSnmpRmonHistoryCtrlInterval_Type.__name__=_C
_TpSnmpRmonHistoryCtrlInterval_Object=MibTableColumn
tpSnmpRmonHistoryCtrlInterval=_TpSnmpRmonHistoryCtrlInterval_Object((1,3,6,1,4,1,11863,6,32,1,2,2,1,1,3),_TpSnmpRmonHistoryCtrlInterval_Type())
tpSnmpRmonHistoryCtrlInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonHistoryCtrlInterval.setStatus(_A)
class _TpSnmpRmonHistoryCtrlBucketsRequested_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpSnmpRmonHistoryCtrlBucketsRequested_Type.__name__=_C
_TpSnmpRmonHistoryCtrlBucketsRequested_Object=MibTableColumn
tpSnmpRmonHistoryCtrlBucketsRequested=_TpSnmpRmonHistoryCtrlBucketsRequested_Object((1,3,6,1,4,1,11863,6,32,1,2,2,1,1,4),_TpSnmpRmonHistoryCtrlBucketsRequested_Type())
tpSnmpRmonHistoryCtrlBucketsRequested.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonHistoryCtrlBucketsRequested.setStatus(_A)
class _TpSnmpRmonHistoryCtrlOwner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpSnmpRmonHistoryCtrlOwner_Type.__name__=_E
_TpSnmpRmonHistoryCtrlOwner_Object=MibTableColumn
tpSnmpRmonHistoryCtrlOwner=_TpSnmpRmonHistoryCtrlOwner_Object((1,3,6,1,4,1,11863,6,32,1,2,2,1,1,5),_TpSnmpRmonHistoryCtrlOwner_Type())
tpSnmpRmonHistoryCtrlOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonHistoryCtrlOwner.setStatus(_A)
class _TpSnmpRmonHistoryCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_TpSnmpRmonHistoryCtrlStatus_Type.__name__=_C
_TpSnmpRmonHistoryCtrlStatus_Object=MibTableColumn
tpSnmpRmonHistoryCtrlStatus=_TpSnmpRmonHistoryCtrlStatus_Object((1,3,6,1,4,1,11863,6,32,1,2,2,1,1,6),_TpSnmpRmonHistoryCtrlStatus_Type())
tpSnmpRmonHistoryCtrlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonHistoryCtrlStatus.setStatus(_A)
_TpSnmpRmonHistoryDataTable_Object=MibTable
tpSnmpRmonHistoryDataTable=_TpSnmpRmonHistoryDataTable_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2))
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataTable.setStatus(_A)
_TpSnmpRmonHistoryDataEntry_Object=MibTableRow
tpSnmpRmonHistoryDataEntry=_TpSnmpRmonHistoryDataEntry_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1))
tpSnmpRmonHistoryDataEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataEntry.setStatus(_A)
class _TpSnmpRmonHistoryDataIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpSnmpRmonHistoryDataIndex_Type.__name__=_C
_TpSnmpRmonHistoryDataIndex_Object=MibTableColumn
tpSnmpRmonHistoryDataIndex=_TpSnmpRmonHistoryDataIndex_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,1),_TpSnmpRmonHistoryDataIndex_Type())
tpSnmpRmonHistoryDataIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataIndex.setStatus(_A)
class _TpSnmpRmonHistoryDataSampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TpSnmpRmonHistoryDataSampleIndex_Type.__name__=_C
_TpSnmpRmonHistoryDataSampleIndex_Object=MibTableColumn
tpSnmpRmonHistoryDataSampleIndex=_TpSnmpRmonHistoryDataSampleIndex_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,2),_TpSnmpRmonHistoryDataSampleIndex_Type())
tpSnmpRmonHistoryDataSampleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataSampleIndex.setStatus(_A)
_TpSnmpRmonHistoryDataIntervalStart_Type=TimeTicks
_TpSnmpRmonHistoryDataIntervalStart_Object=MibTableColumn
tpSnmpRmonHistoryDataIntervalStart=_TpSnmpRmonHistoryDataIntervalStart_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,3),_TpSnmpRmonHistoryDataIntervalStart_Type())
tpSnmpRmonHistoryDataIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataIntervalStart.setStatus(_A)
_TpSnmpRmonHistoryDataDropEvents_Type=Counter32
_TpSnmpRmonHistoryDataDropEvents_Object=MibTableColumn
tpSnmpRmonHistoryDataDropEvents=_TpSnmpRmonHistoryDataDropEvents_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,4),_TpSnmpRmonHistoryDataDropEvents_Type())
tpSnmpRmonHistoryDataDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataDropEvents.setStatus(_A)
_TpSnmpRmonHistoryDataOctets_Type=Counter32
_TpSnmpRmonHistoryDataOctets_Object=MibTableColumn
tpSnmpRmonHistoryDataOctets=_TpSnmpRmonHistoryDataOctets_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,5),_TpSnmpRmonHistoryDataOctets_Type())
tpSnmpRmonHistoryDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataOctets.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataOctets.setUnits('Octets')
_TpSnmpRmonHistoryDataPkts_Type=Counter32
_TpSnmpRmonHistoryDataPkts_Object=MibTableColumn
tpSnmpRmonHistoryDataPkts=_TpSnmpRmonHistoryDataPkts_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,6),_TpSnmpRmonHistoryDataPkts_Type())
tpSnmpRmonHistoryDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataPkts.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataPkts.setUnits(_G)
_TpSnmpRmonHistoryDataBroadcastPkts_Type=Counter32
_TpSnmpRmonHistoryDataBroadcastPkts_Object=MibTableColumn
tpSnmpRmonHistoryDataBroadcastPkts=_TpSnmpRmonHistoryDataBroadcastPkts_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,7),_TpSnmpRmonHistoryDataBroadcastPkts_Type())
tpSnmpRmonHistoryDataBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataBroadcastPkts.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataBroadcastPkts.setUnits(_G)
_TpSnmpRmonHistoryDataMulticastPkts_Type=Counter32
_TpSnmpRmonHistoryDataMulticastPkts_Object=MibTableColumn
tpSnmpRmonHistoryDataMulticastPkts=_TpSnmpRmonHistoryDataMulticastPkts_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,8),_TpSnmpRmonHistoryDataMulticastPkts_Type())
tpSnmpRmonHistoryDataMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataMulticastPkts.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataMulticastPkts.setUnits(_G)
_TpSnmpRmonHistoryDataCRCAlignErrors_Type=Counter32
_TpSnmpRmonHistoryDataCRCAlignErrors_Object=MibTableColumn
tpSnmpRmonHistoryDataCRCAlignErrors=_TpSnmpRmonHistoryDataCRCAlignErrors_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,9),_TpSnmpRmonHistoryDataCRCAlignErrors_Type())
tpSnmpRmonHistoryDataCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataCRCAlignErrors.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataCRCAlignErrors.setUnits(_G)
_TpSnmpRmonHistoryDataUndersizePkts_Type=Counter32
_TpSnmpRmonHistoryDataUndersizePkts_Object=MibTableColumn
tpSnmpRmonHistoryDataUndersizePkts=_TpSnmpRmonHistoryDataUndersizePkts_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,10),_TpSnmpRmonHistoryDataUndersizePkts_Type())
tpSnmpRmonHistoryDataUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataUndersizePkts.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataUndersizePkts.setUnits(_G)
_TpSnmpRmonHistoryDataOversizePkts_Type=Counter32
_TpSnmpRmonHistoryDataOversizePkts_Object=MibTableColumn
tpSnmpRmonHistoryDataOversizePkts=_TpSnmpRmonHistoryDataOversizePkts_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,11),_TpSnmpRmonHistoryDataOversizePkts_Type())
tpSnmpRmonHistoryDataOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataOversizePkts.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataOversizePkts.setUnits(_G)
_TpSnmpRmonHistoryDataFragments_Type=Counter32
_TpSnmpRmonHistoryDataFragments_Object=MibTableColumn
tpSnmpRmonHistoryDataFragments=_TpSnmpRmonHistoryDataFragments_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,12),_TpSnmpRmonHistoryDataFragments_Type())
tpSnmpRmonHistoryDataFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataFragments.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataFragments.setUnits(_G)
_TpSnmpRmonHistoryDataJabbers_Type=Counter32
_TpSnmpRmonHistoryDataJabbers_Object=MibTableColumn
tpSnmpRmonHistoryDataJabbers=_TpSnmpRmonHistoryDataJabbers_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,13),_TpSnmpRmonHistoryDataJabbers_Type())
tpSnmpRmonHistoryDataJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataJabbers.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataJabbers.setUnits(_G)
_TpSnmpRmonHistoryDataCollisions_Type=Counter32
_TpSnmpRmonHistoryDataCollisions_Object=MibTableColumn
tpSnmpRmonHistoryDataCollisions=_TpSnmpRmonHistoryDataCollisions_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,14),_TpSnmpRmonHistoryDataCollisions_Type())
tpSnmpRmonHistoryDataCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataCollisions.setStatus(_A)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataCollisions.setUnits('Collisions')
class _TpSnmpRmonHistoryDataUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_TpSnmpRmonHistoryDataUtilization_Type.__name__=_C
_TpSnmpRmonHistoryDataUtilization_Object=MibTableColumn
tpSnmpRmonHistoryDataUtilization=_TpSnmpRmonHistoryDataUtilization_Object((1,3,6,1,4,1,11863,6,32,1,2,2,2,1,15),_TpSnmpRmonHistoryDataUtilization_Type())
tpSnmpRmonHistoryDataUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonHistoryDataUtilization.setStatus(_A)
_TpSnmpRmonEventCtrl_ObjectIdentity=ObjectIdentity
tpSnmpRmonEventCtrl=_TpSnmpRmonEventCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,32,1,2,3))
_TpSnmpRmonEventCtrlTable_Object=MibTable
tpSnmpRmonEventCtrlTable=_TpSnmpRmonEventCtrlTable_Object((1,3,6,1,4,1,11863,6,32,1,2,3,1))
if mibBuilder.loadTexts:tpSnmpRmonEventCtrlTable.setStatus(_A)
_TpSnmpRmonEventCtrlEntry_Object=MibTableRow
tpSnmpRmonEventCtrlEntry=_TpSnmpRmonEventCtrlEntry_Object((1,3,6,1,4,1,11863,6,32,1,2,3,1,1))
tpSnmpRmonEventCtrlEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:tpSnmpRmonEventCtrlEntry.setStatus(_A)
_TpSnmpRmonEventCtrlIndex_Type=Integer32
_TpSnmpRmonEventCtrlIndex_Object=MibTableColumn
tpSnmpRmonEventCtrlIndex=_TpSnmpRmonEventCtrlIndex_Object((1,3,6,1,4,1,11863,6,32,1,2,3,1,1,1),_TpSnmpRmonEventCtrlIndex_Type())
tpSnmpRmonEventCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonEventCtrlIndex.setStatus(_A)
class _TpSnmpRmonEventCtrlUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpSnmpRmonEventCtrlUserName_Type.__name__=_E
_TpSnmpRmonEventCtrlUserName_Object=MibTableColumn
tpSnmpRmonEventCtrlUserName=_TpSnmpRmonEventCtrlUserName_Object((1,3,6,1,4,1,11863,6,32,1,2,3,1,1,2),_TpSnmpRmonEventCtrlUserName_Type())
tpSnmpRmonEventCtrlUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonEventCtrlUserName.setStatus(_A)
class _TpSnmpRmonEventCtrlDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpSnmpRmonEventCtrlDesc_Type.__name__=_E
_TpSnmpRmonEventCtrlDesc_Object=MibTableColumn
tpSnmpRmonEventCtrlDesc=_TpSnmpRmonEventCtrlDesc_Object((1,3,6,1,4,1,11863,6,32,1,2,3,1,1,3),_TpSnmpRmonEventCtrlDesc_Type())
tpSnmpRmonEventCtrlDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonEventCtrlDesc.setStatus(_A)
class _TpSnmpRmonEventCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('log',2),('snmptrap',3),('logandtrap',4)))
_TpSnmpRmonEventCtrlType_Type.__name__=_C
_TpSnmpRmonEventCtrlType_Object=MibTableColumn
tpSnmpRmonEventCtrlType=_TpSnmpRmonEventCtrlType_Object((1,3,6,1,4,1,11863,6,32,1,2,3,1,1,4),_TpSnmpRmonEventCtrlType_Type())
tpSnmpRmonEventCtrlType.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonEventCtrlType.setStatus(_A)
class _TpSnmpRmonEventCtrlOwner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpSnmpRmonEventCtrlOwner_Type.__name__=_E
_TpSnmpRmonEventCtrlOwner_Object=MibTableColumn
tpSnmpRmonEventCtrlOwner=_TpSnmpRmonEventCtrlOwner_Object((1,3,6,1,4,1,11863,6,32,1,2,3,1,1,5),_TpSnmpRmonEventCtrlOwner_Type())
tpSnmpRmonEventCtrlOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonEventCtrlOwner.setStatus(_A)
class _TpSnmpRmonEventCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_TpSnmpRmonEventCtrlStatus_Type.__name__=_C
_TpSnmpRmonEventCtrlStatus_Object=MibTableColumn
tpSnmpRmonEventCtrlStatus=_TpSnmpRmonEventCtrlStatus_Object((1,3,6,1,4,1,11863,6,32,1,2,3,1,1,6),_TpSnmpRmonEventCtrlStatus_Type())
tpSnmpRmonEventCtrlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonEventCtrlStatus.setStatus(_A)
_TpSnmpRmonEventLogTable_Object=MibTable
tpSnmpRmonEventLogTable=_TpSnmpRmonEventLogTable_Object((1,3,6,1,4,1,11863,6,32,1,2,3,2))
if mibBuilder.loadTexts:tpSnmpRmonEventLogTable.setStatus(_A)
_TpSnmpRmonEventLogEntry_Object=MibTableRow
tpSnmpRmonEventLogEntry=_TpSnmpRmonEventLogEntry_Object((1,3,6,1,4,1,11863,6,32,1,2,3,2,1))
tpSnmpRmonEventLogEntry.setIndexNames((0,_F,_P),(0,_F,_Q))
if mibBuilder.loadTexts:tpSnmpRmonEventLogEntry.setStatus(_A)
class _TpSnmpRmonEventLogEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpSnmpRmonEventLogEventIndex_Type.__name__=_C
_TpSnmpRmonEventLogEventIndex_Object=MibTableColumn
tpSnmpRmonEventLogEventIndex=_TpSnmpRmonEventLogEventIndex_Object((1,3,6,1,4,1,11863,6,32,1,2,3,2,1,1),_TpSnmpRmonEventLogEventIndex_Type())
tpSnmpRmonEventLogEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonEventLogEventIndex.setStatus(_A)
class _TpSnmpRmonEventLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TpSnmpRmonEventLogIndex_Type.__name__=_C
_TpSnmpRmonEventLogIndex_Object=MibTableColumn
tpSnmpRmonEventLogIndex=_TpSnmpRmonEventLogIndex_Object((1,3,6,1,4,1,11863,6,32,1,2,3,2,1,2),_TpSnmpRmonEventLogIndex_Type())
tpSnmpRmonEventLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonEventLogIndex.setStatus(_A)
_TpSnmpRmonEventLogTime_Type=TimeTicks
_TpSnmpRmonEventLogTime_Object=MibTableColumn
tpSnmpRmonEventLogTime=_TpSnmpRmonEventLogTime_Object((1,3,6,1,4,1,11863,6,32,1,2,3,2,1,3),_TpSnmpRmonEventLogTime_Type())
tpSnmpRmonEventLogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonEventLogTime.setStatus(_A)
class _TpSnmpRmonEventLogDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpSnmpRmonEventLogDescription_Type.__name__=_E
_TpSnmpRmonEventLogDescription_Object=MibTableColumn
tpSnmpRmonEventLogDescription=_TpSnmpRmonEventLogDescription_Object((1,3,6,1,4,1,11863,6,32,1,2,3,2,1,4),_TpSnmpRmonEventLogDescription_Type())
tpSnmpRmonEventLogDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonEventLogDescription.setStatus(_A)
_TpSnmpRmonAlarmCtrl_ObjectIdentity=ObjectIdentity
tpSnmpRmonAlarmCtrl=_TpSnmpRmonAlarmCtrl_ObjectIdentity((1,3,6,1,4,1,11863,6,32,1,2,4))
_TpSnmpRmonAlarmCtrlTable_Object=MibTable
tpSnmpRmonAlarmCtrlTable=_TpSnmpRmonAlarmCtrlTable_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1))
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlTable.setStatus(_A)
_TpSnmpRmonAlarmCtrlEntry_Object=MibTableRow
tpSnmpRmonAlarmCtrlEntry=_TpSnmpRmonAlarmCtrlEntry_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1))
tpSnmpRmonAlarmCtrlEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlEntry.setStatus(_A)
_TpSnmpRmonAlarmCtrlIndex_Type=Integer32
_TpSnmpRmonAlarmCtrlIndex_Object=MibTableColumn
tpSnmpRmonAlarmCtrlIndex=_TpSnmpRmonAlarmCtrlIndex_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,1),_TpSnmpRmonAlarmCtrlIndex_Type())
tpSnmpRmonAlarmCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlIndex.setStatus(_A)
class _TpSnmpRmonAlarmCtrlVariable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,6,7,8,9,10,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('recBytes',4),('recPackets',5),('bPackets',6),('mPackets',7),('crcAlignErr',8),('undersize',9),('oversize',10),('jabbers',12),('collisions',13),('packet64Bytes',14),('packetFrom65to127',15),('packetFrom128to255',16),('packetFrom256to511',17),('packetFrom512to1023',18),('packetFrom1024to1518',19)))
_TpSnmpRmonAlarmCtrlVariable_Type.__name__=_C
_TpSnmpRmonAlarmCtrlVariable_Object=MibTableColumn
tpSnmpRmonAlarmCtrlVariable=_TpSnmpRmonAlarmCtrlVariable_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,2),_TpSnmpRmonAlarmCtrlVariable_Type())
tpSnmpRmonAlarmCtrlVariable.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlVariable.setStatus(_A)
class _TpSnmpRmonAlarmCtrlStatisticsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpSnmpRmonAlarmCtrlStatisticsIndex_Type.__name__=_C
_TpSnmpRmonAlarmCtrlStatisticsIndex_Object=MibTableColumn
tpSnmpRmonAlarmCtrlStatisticsIndex=_TpSnmpRmonAlarmCtrlStatisticsIndex_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,3),_TpSnmpRmonAlarmCtrlStatisticsIndex_Type())
tpSnmpRmonAlarmCtrlStatisticsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlStatisticsIndex.setStatus(_A)
class _TpSnmpRmonAlarmCtrlSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2)))
_TpSnmpRmonAlarmCtrlSampleType_Type.__name__=_C
_TpSnmpRmonAlarmCtrlSampleType_Object=MibTableColumn
tpSnmpRmonAlarmCtrlSampleType=_TpSnmpRmonAlarmCtrlSampleType_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,4),_TpSnmpRmonAlarmCtrlSampleType_Type())
tpSnmpRmonAlarmCtrlSampleType.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlSampleType.setStatus(_A)
class _TpSnmpRmonAlarmCtrlRisingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpSnmpRmonAlarmCtrlRisingThreshold_Type.__name__=_C
_TpSnmpRmonAlarmCtrlRisingThreshold_Object=MibTableColumn
tpSnmpRmonAlarmCtrlRisingThreshold=_TpSnmpRmonAlarmCtrlRisingThreshold_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,5),_TpSnmpRmonAlarmCtrlRisingThreshold_Type())
tpSnmpRmonAlarmCtrlRisingThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlRisingThreshold.setStatus(_A)
class _TpSnmpRmonAlarmCtrlRisingEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_TpSnmpRmonAlarmCtrlRisingEvent_Type.__name__=_C
_TpSnmpRmonAlarmCtrlRisingEvent_Object=MibTableColumn
tpSnmpRmonAlarmCtrlRisingEvent=_TpSnmpRmonAlarmCtrlRisingEvent_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,6),_TpSnmpRmonAlarmCtrlRisingEvent_Type())
tpSnmpRmonAlarmCtrlRisingEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlRisingEvent.setStatus(_A)
class _TpSnmpRmonAlarmCtrlFallingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpSnmpRmonAlarmCtrlFallingThreshold_Type.__name__=_C
_TpSnmpRmonAlarmCtrlFallingThreshold_Object=MibTableColumn
tpSnmpRmonAlarmCtrlFallingThreshold=_TpSnmpRmonAlarmCtrlFallingThreshold_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,7),_TpSnmpRmonAlarmCtrlFallingThreshold_Type())
tpSnmpRmonAlarmCtrlFallingThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlFallingThreshold.setStatus(_A)
class _TpSnmpRmonAlarmCtrlFallingEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_TpSnmpRmonAlarmCtrlFallingEvent_Type.__name__=_C
_TpSnmpRmonAlarmCtrlFallingEvent_Object=MibTableColumn
tpSnmpRmonAlarmCtrlFallingEvent=_TpSnmpRmonAlarmCtrlFallingEvent_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,8),_TpSnmpRmonAlarmCtrlFallingEvent_Type())
tpSnmpRmonAlarmCtrlFallingEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlFallingEvent.setStatus(_A)
class _TpSnmpRmonAlarmCtrlStartUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
_TpSnmpRmonAlarmCtrlStartUp_Type.__name__=_C
_TpSnmpRmonAlarmCtrlStartUp_Object=MibTableColumn
tpSnmpRmonAlarmCtrlStartUp=_TpSnmpRmonAlarmCtrlStartUp_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,9),_TpSnmpRmonAlarmCtrlStartUp_Type())
tpSnmpRmonAlarmCtrlStartUp.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlStartUp.setStatus(_A)
class _TpSnmpRmonAlarmCtrlInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_TpSnmpRmonAlarmCtrlInterval_Type.__name__=_C
_TpSnmpRmonAlarmCtrlInterval_Object=MibTableColumn
tpSnmpRmonAlarmCtrlInterval=_TpSnmpRmonAlarmCtrlInterval_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,10),_TpSnmpRmonAlarmCtrlInterval_Type())
tpSnmpRmonAlarmCtrlInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlInterval.setStatus(_A)
class _TpSnmpRmonAlarmCtrlOwner_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpSnmpRmonAlarmCtrlOwner_Type.__name__=_E
_TpSnmpRmonAlarmCtrlOwner_Object=MibTableColumn
tpSnmpRmonAlarmCtrlOwner=_TpSnmpRmonAlarmCtrlOwner_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,11),_TpSnmpRmonAlarmCtrlOwner_Type())
tpSnmpRmonAlarmCtrlOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlOwner.setStatus(_A)
class _TpSnmpRmonAlarmCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_TpSnmpRmonAlarmCtrlStatus_Type.__name__=_C
_TpSnmpRmonAlarmCtrlStatus_Object=MibTableColumn
tpSnmpRmonAlarmCtrlStatus=_TpSnmpRmonAlarmCtrlStatus_Object((1,3,6,1,4,1,11863,6,32,1,2,4,1,1,12),_TpSnmpRmonAlarmCtrlStatus_Type())
tpSnmpRmonAlarmCtrlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSnmpRmonAlarmCtrlStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_L:EntryStatus,'tpSnmpRmonControl':tpSnmpRmonControl,'tpSnmpRmonStatisticsCtrl':tpSnmpRmonStatisticsCtrl,'tpSnmpRmonStatsCtrlTable':tpSnmpRmonStatsCtrlTable,'tpSnmpRmonStatsCtrlEntry':tpSnmpRmonStatsCtrlEntry,_K:tpSnmpRmonStatsCtrlIndex,'tpSnmpRmonStatsCtrlDataSource':tpSnmpRmonStatsCtrlDataSource,'tpSnmpRmonStatsCtrlOwner':tpSnmpRmonStatsCtrlOwner,'tpSnmpRmonStatsCtrlRowStatus':tpSnmpRmonStatsCtrlRowStatus,'tpSnmpRmonHistoryCtrl':tpSnmpRmonHistoryCtrl,'tpSnmpRmonHistoryCtrlTable':tpSnmpRmonHistoryCtrlTable,'tpSnmpRmonHistoryCtrlEntry':tpSnmpRmonHistoryCtrlEntry,_M:tpSnmpRmonHistoryCtrlIndex,'tpSnmpRmonHistoryCtrlSourcePort':tpSnmpRmonHistoryCtrlSourcePort,'tpSnmpRmonHistoryCtrlInterval':tpSnmpRmonHistoryCtrlInterval,'tpSnmpRmonHistoryCtrlBucketsRequested':tpSnmpRmonHistoryCtrlBucketsRequested,'tpSnmpRmonHistoryCtrlOwner':tpSnmpRmonHistoryCtrlOwner,'tpSnmpRmonHistoryCtrlStatus':tpSnmpRmonHistoryCtrlStatus,'tpSnmpRmonHistoryDataTable':tpSnmpRmonHistoryDataTable,'tpSnmpRmonHistoryDataEntry':tpSnmpRmonHistoryDataEntry,_N:tpSnmpRmonHistoryDataIndex,'tpSnmpRmonHistoryDataSampleIndex':tpSnmpRmonHistoryDataSampleIndex,'tpSnmpRmonHistoryDataIntervalStart':tpSnmpRmonHistoryDataIntervalStart,'tpSnmpRmonHistoryDataDropEvents':tpSnmpRmonHistoryDataDropEvents,'tpSnmpRmonHistoryDataOctets':tpSnmpRmonHistoryDataOctets,'tpSnmpRmonHistoryDataPkts':tpSnmpRmonHistoryDataPkts,'tpSnmpRmonHistoryDataBroadcastPkts':tpSnmpRmonHistoryDataBroadcastPkts,'tpSnmpRmonHistoryDataMulticastPkts':tpSnmpRmonHistoryDataMulticastPkts,'tpSnmpRmonHistoryDataCRCAlignErrors':tpSnmpRmonHistoryDataCRCAlignErrors,'tpSnmpRmonHistoryDataUndersizePkts':tpSnmpRmonHistoryDataUndersizePkts,'tpSnmpRmonHistoryDataOversizePkts':tpSnmpRmonHistoryDataOversizePkts,'tpSnmpRmonHistoryDataFragments':tpSnmpRmonHistoryDataFragments,'tpSnmpRmonHistoryDataJabbers':tpSnmpRmonHistoryDataJabbers,'tpSnmpRmonHistoryDataCollisions':tpSnmpRmonHistoryDataCollisions,'tpSnmpRmonHistoryDataUtilization':tpSnmpRmonHistoryDataUtilization,'tpSnmpRmonEventCtrl':tpSnmpRmonEventCtrl,'tpSnmpRmonEventCtrlTable':tpSnmpRmonEventCtrlTable,'tpSnmpRmonEventCtrlEntry':tpSnmpRmonEventCtrlEntry,_O:tpSnmpRmonEventCtrlIndex,'tpSnmpRmonEventCtrlUserName':tpSnmpRmonEventCtrlUserName,'tpSnmpRmonEventCtrlDesc':tpSnmpRmonEventCtrlDesc,'tpSnmpRmonEventCtrlType':tpSnmpRmonEventCtrlType,'tpSnmpRmonEventCtrlOwner':tpSnmpRmonEventCtrlOwner,'tpSnmpRmonEventCtrlStatus':tpSnmpRmonEventCtrlStatus,'tpSnmpRmonEventLogTable':tpSnmpRmonEventLogTable,'tpSnmpRmonEventLogEntry':tpSnmpRmonEventLogEntry,_P:tpSnmpRmonEventLogEventIndex,_Q:tpSnmpRmonEventLogIndex,'tpSnmpRmonEventLogTime':tpSnmpRmonEventLogTime,'tpSnmpRmonEventLogDescription':tpSnmpRmonEventLogDescription,'tpSnmpRmonAlarmCtrl':tpSnmpRmonAlarmCtrl,'tpSnmpRmonAlarmCtrlTable':tpSnmpRmonAlarmCtrlTable,'tpSnmpRmonAlarmCtrlEntry':tpSnmpRmonAlarmCtrlEntry,_R:tpSnmpRmonAlarmCtrlIndex,'tpSnmpRmonAlarmCtrlVariable':tpSnmpRmonAlarmCtrlVariable,'tpSnmpRmonAlarmCtrlStatisticsIndex':tpSnmpRmonAlarmCtrlStatisticsIndex,'tpSnmpRmonAlarmCtrlSampleType':tpSnmpRmonAlarmCtrlSampleType,'tpSnmpRmonAlarmCtrlRisingThreshold':tpSnmpRmonAlarmCtrlRisingThreshold,'tpSnmpRmonAlarmCtrlRisingEvent':tpSnmpRmonAlarmCtrlRisingEvent,'tpSnmpRmonAlarmCtrlFallingThreshold':tpSnmpRmonAlarmCtrlFallingThreshold,'tpSnmpRmonAlarmCtrlFallingEvent':tpSnmpRmonAlarmCtrlFallingEvent,'tpSnmpRmonAlarmCtrlStartUp':tpSnmpRmonAlarmCtrlStartUp,'tpSnmpRmonAlarmCtrlInterval':tpSnmpRmonAlarmCtrlInterval,'tpSnmpRmonAlarmCtrlOwner':tpSnmpRmonAlarmCtrlOwner,'tpSnmpRmonAlarmCtrlStatus':tpSnmpRmonAlarmCtrlStatus})