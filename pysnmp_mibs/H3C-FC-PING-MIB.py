_Q='h3cFcPingResPackets'
_P='h3cFcPingReqPackets'
_O='h3cFcPingAddress'
_N='h3cFcPingAddressType'
_M='h3cFcPingVsan'
_L='TruthValue'
_K='Integer32'
_J='H3cFcStartOper'
_I='H3cFcAddressType'
_H='microseconds'
_G='seconds'
_F='h3cFcPingIndex'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='H3C-FC-PING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cFcAddress,H3cFcAddressType,H3cFcStartOper,H3cFcVsanIndex=mibBuilder.importSymbols('H3C-FC-TC-MIB','H3cFcAddress',_I,_J,'H3cFcVsanIndex')
h3cSan,=mibBuilder.importSymbols('H3C-VSAN-MIB','h3cSan')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
h3cFcPing=ModuleIdentity((1,3,6,1,4,1,2011,10,2,127,5))
if mibBuilder.loadTexts:h3cFcPing.setRevisions(('2013-03-15 00:00',))
_H3cFcPingObjects_ObjectIdentity=ObjectIdentity
h3cFcPingObjects=_H3cFcPingObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,5,1))
_H3cFcPingConfigurations_ObjectIdentity=ObjectIdentity
h3cFcPingConfigurations=_H3cFcPingConfigurations_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,5,1,1))
_H3cFcPingTable_Object=MibTable
h3cFcPingTable=_H3cFcPingTable_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1))
if mibBuilder.loadTexts:h3cFcPingTable.setStatus(_A)
_H3cFcPingEntry_Object=MibTableRow
h3cFcPingEntry=_H3cFcPingEntry_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1))
h3cFcPingEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:h3cFcPingEntry.setStatus(_A)
class _H3cFcPingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cFcPingIndex_Type.__name__=_E
_H3cFcPingIndex_Object=MibTableColumn
h3cFcPingIndex=_H3cFcPingIndex_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,1),_H3cFcPingIndex_Type())
h3cFcPingIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cFcPingIndex.setStatus(_A)
_H3cFcPingVsan_Type=H3cFcVsanIndex
_H3cFcPingVsan_Object=MibTableColumn
h3cFcPingVsan=_H3cFcPingVsan_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,2),_H3cFcPingVsan_Type())
h3cFcPingVsan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcPingVsan.setStatus(_A)
class _H3cFcPingAddressType_Type(H3cFcAddressType):defaultValue=2
_H3cFcPingAddressType_Type.__name__=_I
_H3cFcPingAddressType_Object=MibTableColumn
h3cFcPingAddressType=_H3cFcPingAddressType_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,3),_H3cFcPingAddressType_Type())
h3cFcPingAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcPingAddressType.setStatus(_A)
_H3cFcPingAddress_Type=H3cFcAddress
_H3cFcPingAddress_Object=MibTableColumn
h3cFcPingAddress=_H3cFcPingAddress_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,4),_H3cFcPingAddress_Type())
h3cFcPingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcPingAddress.setStatus(_A)
class _H3cFcPingPacketCount_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cFcPingPacketCount_Type.__name__=_E
_H3cFcPingPacketCount_Object=MibTableColumn
h3cFcPingPacketCount=_H3cFcPingPacketCount_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,5),_H3cFcPingPacketCount_Type())
h3cFcPingPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcPingPacketCount.setStatus(_A)
_H3cFcPingPayloadSize_Type=Unsigned32
_H3cFcPingPayloadSize_Object=MibTableColumn
h3cFcPingPayloadSize=_H3cFcPingPayloadSize_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,6),_H3cFcPingPayloadSize_Type())
h3cFcPingPayloadSize.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcPingPayloadSize.setStatus(_A)
class _H3cFcPingTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_H3cFcPingTimeout_Type.__name__=_E
_H3cFcPingTimeout_Object=MibTableColumn
h3cFcPingTimeout=_H3cFcPingTimeout_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,7),_H3cFcPingTimeout_Type())
h3cFcPingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcPingTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cFcPingTimeout.setUnits(_G)
_H3cFcPingDelay_Type=Unsigned32
_H3cFcPingDelay_Object=MibTableColumn
h3cFcPingDelay=_H3cFcPingDelay_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,8),_H3cFcPingDelay_Type())
h3cFcPingDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcPingDelay.setStatus(_A)
if mibBuilder.loadTexts:h3cFcPingDelay.setUnits(_G)
class _H3cFcPingAgeInterval_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,900))
_H3cFcPingAgeInterval_Type.__name__=_E
_H3cFcPingAgeInterval_Object=MibTableColumn
h3cFcPingAgeInterval=_H3cFcPingAgeInterval_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,9),_H3cFcPingAgeInterval_Type())
h3cFcPingAgeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcPingAgeInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cFcPingAgeInterval.setUnits(_G)
class _H3cFcPingAdminStatus_Type(H3cFcStartOper):defaultValue=2
_H3cFcPingAdminStatus_Type.__name__=_J
_H3cFcPingAdminStatus_Object=MibTableColumn
h3cFcPingAdminStatus=_H3cFcPingAdminStatus_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,10),_H3cFcPingAdminStatus_Type())
h3cFcPingAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcPingAdminStatus.setStatus(_A)
class _H3cFcPingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inProgress',1),('complete',2),('disabled',3),('failed',4)))
_H3cFcPingOperStatus_Type.__name__=_K
_H3cFcPingOperStatus_Object=MibTableColumn
h3cFcPingOperStatus=_H3cFcPingOperStatus_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,11),_H3cFcPingOperStatus_Type())
h3cFcPingOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcPingOperStatus.setStatus(_A)
class _H3cFcPingTrapOnCompletion_Type(TruthValue):defaultValue=2
_H3cFcPingTrapOnCompletion_Type.__name__=_L
_H3cFcPingTrapOnCompletion_Object=MibTableColumn
h3cFcPingTrapOnCompletion=_H3cFcPingTrapOnCompletion_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,12),_H3cFcPingTrapOnCompletion_Type())
h3cFcPingTrapOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcPingTrapOnCompletion.setStatus(_A)
_H3cFcPingRowStatus_Type=RowStatus
_H3cFcPingRowStatus_Object=MibTableColumn
h3cFcPingRowStatus=_H3cFcPingRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,5,1,1,1,1,13),_H3cFcPingRowStatus_Type())
h3cFcPingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcPingRowStatus.setStatus(_A)
_H3cFcPingStatistics_ObjectIdentity=ObjectIdentity
h3cFcPingStatistics=_H3cFcPingStatistics_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,5,1,2))
_H3cFcPingStatTable_Object=MibTable
h3cFcPingStatTable=_H3cFcPingStatTable_Object((1,3,6,1,4,1,2011,10,2,127,5,1,2,1))
if mibBuilder.loadTexts:h3cFcPingStatTable.setStatus(_A)
_H3cFcPingStatEntry_Object=MibTableRow
h3cFcPingStatEntry=_H3cFcPingStatEntry_Object((1,3,6,1,4,1,2011,10,2,127,5,1,2,1,1))
h3cFcPingStatEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:h3cFcPingStatEntry.setStatus(_A)
_H3cFcPingReqPackets_Type=Unsigned32
_H3cFcPingReqPackets_Object=MibTableColumn
h3cFcPingReqPackets=_H3cFcPingReqPackets_Object((1,3,6,1,4,1,2011,10,2,127,5,1,2,1,1,1),_H3cFcPingReqPackets_Type())
h3cFcPingReqPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcPingReqPackets.setStatus(_A)
_H3cFcPingResPackets_Type=Unsigned32
_H3cFcPingResPackets_Object=MibTableColumn
h3cFcPingResPackets=_H3cFcPingResPackets_Object((1,3,6,1,4,1,2011,10,2,127,5,1,2,1,1,2),_H3cFcPingResPackets_Type())
h3cFcPingResPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcPingResPackets.setStatus(_A)
_H3cFcPingMinTime_Type=Integer32
_H3cFcPingMinTime_Object=MibTableColumn
h3cFcPingMinTime=_H3cFcPingMinTime_Object((1,3,6,1,4,1,2011,10,2,127,5,1,2,1,1,3),_H3cFcPingMinTime_Type())
h3cFcPingMinTime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcPingMinTime.setStatus(_A)
if mibBuilder.loadTexts:h3cFcPingMinTime.setUnits(_H)
_H3cFcPingAverageTime_Type=Integer32
_H3cFcPingAverageTime_Object=MibTableColumn
h3cFcPingAverageTime=_H3cFcPingAverageTime_Object((1,3,6,1,4,1,2011,10,2,127,5,1,2,1,1,4),_H3cFcPingAverageTime_Type())
h3cFcPingAverageTime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcPingAverageTime.setStatus(_A)
if mibBuilder.loadTexts:h3cFcPingAverageTime.setUnits(_H)
_H3cFcPingMaxTime_Type=Integer32
_H3cFcPingMaxTime_Object=MibTableColumn
h3cFcPingMaxTime=_H3cFcPingMaxTime_Object((1,3,6,1,4,1,2011,10,2,127,5,1,2,1,1,5),_H3cFcPingMaxTime_Type())
h3cFcPingMaxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcPingMaxTime.setStatus(_A)
if mibBuilder.loadTexts:h3cFcPingMaxTime.setUnits(_H)
_H3cFcPingTimeoutNum_Type=Unsigned32
_H3cFcPingTimeoutNum_Object=MibTableColumn
h3cFcPingTimeoutNum=_H3cFcPingTimeoutNum_Object((1,3,6,1,4,1,2011,10,2,127,5,1,2,1,1,6),_H3cFcPingTimeoutNum_Type())
h3cFcPingTimeoutNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcPingTimeoutNum.setStatus(_A)
_H3cFcPingNotifications_ObjectIdentity=ObjectIdentity
h3cFcPingNotifications=_H3cFcPingNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,5,1,3))
_H3cFcPingNotifyPrefix_ObjectIdentity=ObjectIdentity
h3cFcPingNotifyPrefix=_H3cFcPingNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,5,1,3,0))
h3cFcPingCompletionNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,5,1,3,0,1))
h3cFcPingCompletionNotify.setObjects(*((_B,_F),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3cFcPingCompletionNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cFcPing':h3cFcPing,'h3cFcPingObjects':h3cFcPingObjects,'h3cFcPingConfigurations':h3cFcPingConfigurations,'h3cFcPingTable':h3cFcPingTable,'h3cFcPingEntry':h3cFcPingEntry,_F:h3cFcPingIndex,_M:h3cFcPingVsan,_N:h3cFcPingAddressType,_O:h3cFcPingAddress,'h3cFcPingPacketCount':h3cFcPingPacketCount,'h3cFcPingPayloadSize':h3cFcPingPayloadSize,'h3cFcPingTimeout':h3cFcPingTimeout,'h3cFcPingDelay':h3cFcPingDelay,'h3cFcPingAgeInterval':h3cFcPingAgeInterval,'h3cFcPingAdminStatus':h3cFcPingAdminStatus,'h3cFcPingOperStatus':h3cFcPingOperStatus,'h3cFcPingTrapOnCompletion':h3cFcPingTrapOnCompletion,'h3cFcPingRowStatus':h3cFcPingRowStatus,'h3cFcPingStatistics':h3cFcPingStatistics,'h3cFcPingStatTable':h3cFcPingStatTable,'h3cFcPingStatEntry':h3cFcPingStatEntry,_P:h3cFcPingReqPackets,_Q:h3cFcPingResPackets,'h3cFcPingMinTime':h3cFcPingMinTime,'h3cFcPingAverageTime':h3cFcPingAverageTime,'h3cFcPingMaxTime':h3cFcPingMaxTime,'h3cFcPingTimeoutNum':h3cFcPingTimeoutNum,'h3cFcPingNotifications':h3cFcPingNotifications,'h3cFcPingNotifyPrefix':h3cFcPingNotifyPrefix,'h3cFcPingCompletionNotify':h3cFcPingCompletionNotify})