_Q='hpnicfFcPingResPackets'
_P='hpnicfFcPingReqPackets'
_O='hpnicfFcPingAddress'
_N='hpnicfFcPingAddressType'
_M='hpnicfFcPingVsan'
_L='TruthValue'
_K='Integer32'
_J='HpnicfFcStartOper'
_I='HpnicfFcAddressType'
_H='microseconds'
_G='seconds'
_F='hpnicfFcPingIndex'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='HPN-ICF-FC-PING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfFcAddress,HpnicfFcAddressType,HpnicfFcStartOper,HpnicfFcVsanIndex=mibBuilder.importSymbols('HPN-ICF-FC-TC-MIB','HpnicfFcAddress',_I,_J,'HpnicfFcVsanIndex')
hpnicfSan,=mibBuilder.importSymbols('HPN-ICF-VSAN-MIB','hpnicfSan')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
hpnicfFcPing=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,5))
if mibBuilder.loadTexts:hpnicfFcPing.setRevisions(('2013-03-15 00:00',))
_HpnicfFcPingObjects_ObjectIdentity=ObjectIdentity
hpnicfFcPingObjects=_HpnicfFcPingObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1))
_HpnicfFcPingConfigurations_ObjectIdentity=ObjectIdentity
hpnicfFcPingConfigurations=_HpnicfFcPingConfigurations_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1))
_HpnicfFcPingTable_Object=MibTable
hpnicfFcPingTable=_HpnicfFcPingTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1))
if mibBuilder.loadTexts:hpnicfFcPingTable.setStatus(_A)
_HpnicfFcPingEntry_Object=MibTableRow
hpnicfFcPingEntry=_HpnicfFcPingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1))
hpnicfFcPingEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hpnicfFcPingEntry.setStatus(_A)
class _HpnicfFcPingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfFcPingIndex_Type.__name__=_E
_HpnicfFcPingIndex_Object=MibTableColumn
hpnicfFcPingIndex=_HpnicfFcPingIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,1),_HpnicfFcPingIndex_Type())
hpnicfFcPingIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfFcPingIndex.setStatus(_A)
_HpnicfFcPingVsan_Type=HpnicfFcVsanIndex
_HpnicfFcPingVsan_Object=MibTableColumn
hpnicfFcPingVsan=_HpnicfFcPingVsan_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,2),_HpnicfFcPingVsan_Type())
hpnicfFcPingVsan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPingVsan.setStatus(_A)
class _HpnicfFcPingAddressType_Type(HpnicfFcAddressType):defaultValue=2
_HpnicfFcPingAddressType_Type.__name__=_I
_HpnicfFcPingAddressType_Object=MibTableColumn
hpnicfFcPingAddressType=_HpnicfFcPingAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,3),_HpnicfFcPingAddressType_Type())
hpnicfFcPingAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPingAddressType.setStatus(_A)
_HpnicfFcPingAddress_Type=HpnicfFcAddress
_HpnicfFcPingAddress_Object=MibTableColumn
hpnicfFcPingAddress=_HpnicfFcPingAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,4),_HpnicfFcPingAddress_Type())
hpnicfFcPingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPingAddress.setStatus(_A)
class _HpnicfFcPingPacketCount_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfFcPingPacketCount_Type.__name__=_E
_HpnicfFcPingPacketCount_Object=MibTableColumn
hpnicfFcPingPacketCount=_HpnicfFcPingPacketCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,5),_HpnicfFcPingPacketCount_Type())
hpnicfFcPingPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPingPacketCount.setStatus(_A)
_HpnicfFcPingPayloadSize_Type=Unsigned32
_HpnicfFcPingPayloadSize_Object=MibTableColumn
hpnicfFcPingPayloadSize=_HpnicfFcPingPayloadSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,6),_HpnicfFcPingPayloadSize_Type())
hpnicfFcPingPayloadSize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFcPingPayloadSize.setStatus(_A)
class _HpnicfFcPingTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HpnicfFcPingTimeout_Type.__name__=_E
_HpnicfFcPingTimeout_Object=MibTableColumn
hpnicfFcPingTimeout=_HpnicfFcPingTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,7),_HpnicfFcPingTimeout_Type())
hpnicfFcPingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPingTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFcPingTimeout.setUnits(_G)
_HpnicfFcPingDelay_Type=Unsigned32
_HpnicfFcPingDelay_Object=MibTableColumn
hpnicfFcPingDelay=_HpnicfFcPingDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,8),_HpnicfFcPingDelay_Type())
hpnicfFcPingDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFcPingDelay.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFcPingDelay.setUnits(_G)
class _HpnicfFcPingAgeInterval_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,900))
_HpnicfFcPingAgeInterval_Type.__name__=_E
_HpnicfFcPingAgeInterval_Object=MibTableColumn
hpnicfFcPingAgeInterval=_HpnicfFcPingAgeInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,9),_HpnicfFcPingAgeInterval_Type())
hpnicfFcPingAgeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPingAgeInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFcPingAgeInterval.setUnits(_G)
class _HpnicfFcPingAdminStatus_Type(HpnicfFcStartOper):defaultValue=2
_HpnicfFcPingAdminStatus_Type.__name__=_J
_HpnicfFcPingAdminStatus_Object=MibTableColumn
hpnicfFcPingAdminStatus=_HpnicfFcPingAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,10),_HpnicfFcPingAdminStatus_Type())
hpnicfFcPingAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPingAdminStatus.setStatus(_A)
class _HpnicfFcPingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inProgress',1),('complete',2),('disabled',3),('failed',4)))
_HpnicfFcPingOperStatus_Type.__name__=_K
_HpnicfFcPingOperStatus_Object=MibTableColumn
hpnicfFcPingOperStatus=_HpnicfFcPingOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,11),_HpnicfFcPingOperStatus_Type())
hpnicfFcPingOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFcPingOperStatus.setStatus(_A)
class _HpnicfFcPingTrapOnCompletion_Type(TruthValue):defaultValue=2
_HpnicfFcPingTrapOnCompletion_Type.__name__=_L
_HpnicfFcPingTrapOnCompletion_Object=MibTableColumn
hpnicfFcPingTrapOnCompletion=_HpnicfFcPingTrapOnCompletion_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,12),_HpnicfFcPingTrapOnCompletion_Type())
hpnicfFcPingTrapOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPingTrapOnCompletion.setStatus(_A)
_HpnicfFcPingRowStatus_Type=RowStatus
_HpnicfFcPingRowStatus_Object=MibTableColumn
hpnicfFcPingRowStatus=_HpnicfFcPingRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,1,1,1,13),_HpnicfFcPingRowStatus_Type())
hpnicfFcPingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPingRowStatus.setStatus(_A)
_HpnicfFcPingStatistics_ObjectIdentity=ObjectIdentity
hpnicfFcPingStatistics=_HpnicfFcPingStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,2))
_HpnicfFcPingStatTable_Object=MibTable
hpnicfFcPingStatTable=_HpnicfFcPingStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,2,1))
if mibBuilder.loadTexts:hpnicfFcPingStatTable.setStatus(_A)
_HpnicfFcPingStatEntry_Object=MibTableRow
hpnicfFcPingStatEntry=_HpnicfFcPingStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,2,1,1))
hpnicfFcPingStatEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hpnicfFcPingStatEntry.setStatus(_A)
_HpnicfFcPingReqPackets_Type=Unsigned32
_HpnicfFcPingReqPackets_Object=MibTableColumn
hpnicfFcPingReqPackets=_HpnicfFcPingReqPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,2,1,1,1),_HpnicfFcPingReqPackets_Type())
hpnicfFcPingReqPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFcPingReqPackets.setStatus(_A)
_HpnicfFcPingResPackets_Type=Unsigned32
_HpnicfFcPingResPackets_Object=MibTableColumn
hpnicfFcPingResPackets=_HpnicfFcPingResPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,2,1,1,2),_HpnicfFcPingResPackets_Type())
hpnicfFcPingResPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFcPingResPackets.setStatus(_A)
_HpnicfFcPingMinTime_Type=Integer32
_HpnicfFcPingMinTime_Object=MibTableColumn
hpnicfFcPingMinTime=_HpnicfFcPingMinTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,2,1,1,3),_HpnicfFcPingMinTime_Type())
hpnicfFcPingMinTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFcPingMinTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFcPingMinTime.setUnits(_H)
_HpnicfFcPingAverageTime_Type=Integer32
_HpnicfFcPingAverageTime_Object=MibTableColumn
hpnicfFcPingAverageTime=_HpnicfFcPingAverageTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,2,1,1,4),_HpnicfFcPingAverageTime_Type())
hpnicfFcPingAverageTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFcPingAverageTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFcPingAverageTime.setUnits(_H)
_HpnicfFcPingMaxTime_Type=Integer32
_HpnicfFcPingMaxTime_Object=MibTableColumn
hpnicfFcPingMaxTime=_HpnicfFcPingMaxTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,2,1,1,5),_HpnicfFcPingMaxTime_Type())
hpnicfFcPingMaxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFcPingMaxTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFcPingMaxTime.setUnits(_H)
_HpnicfFcPingTimeoutNum_Type=Unsigned32
_HpnicfFcPingTimeoutNum_Object=MibTableColumn
hpnicfFcPingTimeoutNum=_HpnicfFcPingTimeoutNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,2,1,1,6),_HpnicfFcPingTimeoutNum_Type())
hpnicfFcPingTimeoutNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFcPingTimeoutNum.setStatus(_A)
_HpnicfFcPingNotifications_ObjectIdentity=ObjectIdentity
hpnicfFcPingNotifications=_HpnicfFcPingNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,3))
_HpnicfFcPingNotifyPrefix_ObjectIdentity=ObjectIdentity
hpnicfFcPingNotifyPrefix=_HpnicfFcPingNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,3,0))
hpnicfFcPingCompletionNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,5,1,3,0,1))
hpnicfFcPingCompletionNotify.setObjects(*((_B,_F),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpnicfFcPingCompletionNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfFcPing':hpnicfFcPing,'hpnicfFcPingObjects':hpnicfFcPingObjects,'hpnicfFcPingConfigurations':hpnicfFcPingConfigurations,'hpnicfFcPingTable':hpnicfFcPingTable,'hpnicfFcPingEntry':hpnicfFcPingEntry,_F:hpnicfFcPingIndex,_M:hpnicfFcPingVsan,_N:hpnicfFcPingAddressType,_O:hpnicfFcPingAddress,'hpnicfFcPingPacketCount':hpnicfFcPingPacketCount,'hpnicfFcPingPayloadSize':hpnicfFcPingPayloadSize,'hpnicfFcPingTimeout':hpnicfFcPingTimeout,'hpnicfFcPingDelay':hpnicfFcPingDelay,'hpnicfFcPingAgeInterval':hpnicfFcPingAgeInterval,'hpnicfFcPingAdminStatus':hpnicfFcPingAdminStatus,'hpnicfFcPingOperStatus':hpnicfFcPingOperStatus,'hpnicfFcPingTrapOnCompletion':hpnicfFcPingTrapOnCompletion,'hpnicfFcPingRowStatus':hpnicfFcPingRowStatus,'hpnicfFcPingStatistics':hpnicfFcPingStatistics,'hpnicfFcPingStatTable':hpnicfFcPingStatTable,'hpnicfFcPingStatEntry':hpnicfFcPingStatEntry,_P:hpnicfFcPingReqPackets,_Q:hpnicfFcPingResPackets,'hpnicfFcPingMinTime':hpnicfFcPingMinTime,'hpnicfFcPingAverageTime':hpnicfFcPingAverageTime,'hpnicfFcPingMaxTime':hpnicfFcPingMaxTime,'hpnicfFcPingTimeoutNum':hpnicfFcPingTimeoutNum,'hpnicfFcPingNotifications':hpnicfFcPingNotifications,'hpnicfFcPingNotifyPrefix':hpnicfFcPingNotifyPrefix,'hpnicfFcPingCompletionNotify':hpnicfFcPingCompletionNotify})