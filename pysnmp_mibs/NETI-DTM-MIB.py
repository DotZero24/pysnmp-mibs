_Z='dtmTimeSourceIndex'
_Y='noControl'
_X='limited'
_W='recover'
_V='dtmLinkStateIfIndex'
_U='lowerLayerDown'
_T='absent'
_S='dtmIfIndex'
_R='not-accessible'
_Q='dtmHostsEntryIndex'
_P='loopback'
_O='dtmAddrEntryIndex'
_N='TruthValue'
_M='SnmpAdminString'
_L='dtmLinkStateIndex'
_K='down'
_J='Unsigned32'
_I='up'
_H='Gauge32'
_G='deprecated'
_F='NETI-DTM-MIB'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FaultStatus,netiExperimentalGeneric=mibBuilder.importSymbols('NETI-COMMON-MIB','FaultStatus','netiExperimentalGeneric')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_H,_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention',_N)
netiDTMMIB=ModuleIdentity((1,3,6,1,4,1,2928,6,2,4))
if mibBuilder.loadTexts:netiDTMMIB.setRevisions(('2013-11-12 08:00','2013-09-10 13:00','2010-09-01 14:00','2010-03-03 09:00','2009-06-25 14:00','2008-02-06 17:00','2006-08-22 10:00','2006-05-16 13:00','2004-09-29 00:00','2003-02-28 00:00'))
class DtmAddress(TextualConvention,OctetString):status=_A;displayHint='1x.';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class DtmSourceRoute(TextualConvention,OctetString):status=_A;displayHint='1x.1x.1x.1x.1x.1x.1x.1x 1x:1x'
_NetiDTMMIBObjects_ObjectIdentity=ObjectIdentity
netiDTMMIBObjects=_NetiDTMMIBObjects_ObjectIdentity((1,3,6,1,4,1,2928,6,2,4,1))
_DtmAddrGroup_ObjectIdentity=ObjectIdentity
dtmAddrGroup=_DtmAddrGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,4,1,1))
_DtmAddrTable_Object=MibTable
dtmAddrTable=_DtmAddrTable_Object((1,3,6,1,4,1,2928,6,2,4,1,1,1))
if mibBuilder.loadTexts:dtmAddrTable.setStatus(_A)
_DtmAddrEntry_Object=MibTableRow
dtmAddrEntry=_DtmAddrEntry_Object((1,3,6,1,4,1,2928,6,2,4,1,1,1,1))
dtmAddrEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:dtmAddrEntry.setStatus(_A)
class _DtmAddrEntryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DtmAddrEntryIndex_Type.__name__=_J
_DtmAddrEntryIndex_Object=MibTableColumn
dtmAddrEntryIndex=_DtmAddrEntryIndex_Object((1,3,6,1,4,1,2928,6,2,4,1,1,1,1,1),_DtmAddrEntryIndex_Type())
dtmAddrEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmAddrEntryIndex.setStatus(_A)
_DtmAddrEntryAddr_Type=DtmAddress
_DtmAddrEntryAddr_Object=MibTableColumn
dtmAddrEntryAddr=_DtmAddrEntryAddr_Object((1,3,6,1,4,1,2928,6,2,4,1,1,1,1,2),_DtmAddrEntryAddr_Type())
dtmAddrEntryAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmAddrEntryAddr.setStatus(_A)
class _DtmAddrEntryIsAlias_Type(TruthValue):defaultValue=1
_DtmAddrEntryIsAlias_Type.__name__=_N
_DtmAddrEntryIsAlias_Object=MibTableColumn
dtmAddrEntryIsAlias=_DtmAddrEntryIsAlias_Object((1,3,6,1,4,1,2928,6,2,4,1,1,1,1,3),_DtmAddrEntryIsAlias_Type())
dtmAddrEntryIsAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmAddrEntryIsAlias.setStatus(_A)
class _DtmAddrEntryAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unspecified',1),(_P,2),('local',3),('multicast',4),('global',5)))
_DtmAddrEntryAddrType_Type.__name__=_C
_DtmAddrEntryAddrType_Object=MibTableColumn
dtmAddrEntryAddrType=_DtmAddrEntryAddrType_Object((1,3,6,1,4,1,2928,6,2,4,1,1,1,1,4),_DtmAddrEntryAddrType_Type())
dtmAddrEntryAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmAddrEntryAddrType.setStatus(_A)
_DtmAddrEntryRowStatus_Type=RowStatus
_DtmAddrEntryRowStatus_Object=MibTableColumn
dtmAddrEntryRowStatus=_DtmAddrEntryRowStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,1,1,1,5),_DtmAddrEntryRowStatus_Type())
dtmAddrEntryRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmAddrEntryRowStatus.setStatus(_A)
_DtmHostsTable_Object=MibTable
dtmHostsTable=_DtmHostsTable_Object((1,3,6,1,4,1,2928,6,2,4,1,1,2))
if mibBuilder.loadTexts:dtmHostsTable.setStatus(_A)
_DtmHostsEntry_Object=MibTableRow
dtmHostsEntry=_DtmHostsEntry_Object((1,3,6,1,4,1,2928,6,2,4,1,1,2,1))
dtmHostsEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:dtmHostsEntry.setStatus(_A)
class _DtmHostsEntryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DtmHostsEntryIndex_Type.__name__=_J
_DtmHostsEntryIndex_Object=MibTableColumn
dtmHostsEntryIndex=_DtmHostsEntryIndex_Object((1,3,6,1,4,1,2928,6,2,4,1,1,2,1,1),_DtmHostsEntryIndex_Type())
dtmHostsEntryIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:dtmHostsEntryIndex.setStatus(_A)
_DtmHostsEntryAddr_Type=DtmAddress
_DtmHostsEntryAddr_Object=MibTableColumn
dtmHostsEntryAddr=_DtmHostsEntryAddr_Object((1,3,6,1,4,1,2928,6,2,4,1,1,2,1,2),_DtmHostsEntryAddr_Type())
dtmHostsEntryAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmHostsEntryAddr.setStatus(_A)
_DtmHostsEntryName_Type=DisplayString
_DtmHostsEntryName_Object=MibTableColumn
dtmHostsEntryName=_DtmHostsEntryName_Object((1,3,6,1,4,1,2928,6,2,4,1,1,2,1,3),_DtmHostsEntryName_Type())
dtmHostsEntryName.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmHostsEntryName.setStatus(_A)
_DtmHostsEntryRowStatus_Type=RowStatus
_DtmHostsEntryRowStatus_Object=MibTableColumn
dtmHostsEntryRowStatus=_DtmHostsEntryRowStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,1,2,1,4),_DtmHostsEntryRowStatus_Type())
dtmHostsEntryRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmHostsEntryRowStatus.setStatus(_A)
_DtmIfGroup_ObjectIdentity=ObjectIdentity
dtmIfGroup=_DtmIfGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,4,1,2))
_DtmIfTable_Object=MibTable
dtmIfTable=_DtmIfTable_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1))
if mibBuilder.loadTexts:dtmIfTable.setStatus(_A)
_DtmIfEntry_Object=MibTableRow
dtmIfEntry=_DtmIfEntry_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1))
dtmIfEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:dtmIfEntry.setStatus(_A)
class _DtmIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DtmIfIndex_Type.__name__=_C
_DtmIfIndex_Object=MibTableColumn
dtmIfIndex=_DtmIfIndex_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,1),_DtmIfIndex_Type())
dtmIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfIndex.setStatus(_A)
_DtmIfName_Type=DisplayString
_DtmIfName_Object=MibTableColumn
dtmIfName=_DtmIfName_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,2),_DtmIfName_Type())
dtmIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfName.setStatus(_A)
_DtmIfMacAddress_Type=MacAddress
_DtmIfMacAddress_Object=MibTableColumn
dtmIfMacAddress=_DtmIfMacAddress_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,3),_DtmIfMacAddress_Type())
dtmIfMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfMacAddress.setStatus(_A)
_DtmIfTxCapacity_Type=Gauge32
_DtmIfTxCapacity_Object=MibTableColumn
dtmIfTxCapacity=_DtmIfTxCapacity_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,4),_DtmIfTxCapacity_Type())
dtmIfTxCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfTxCapacity.setStatus(_A)
class _DtmIfTxCapacityCtrl_Type(Gauge32):defaultValue=5
_DtmIfTxCapacityCtrl_Type.__name__=_H
_DtmIfTxCapacityCtrl_Object=MibTableColumn
dtmIfTxCapacityCtrl=_DtmIfTxCapacityCtrl_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,5),_DtmIfTxCapacityCtrl_Type())
dtmIfTxCapacityCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfTxCapacityCtrl.setStatus(_A)
class _DtmIfTxCapacityStart_Type(Gauge32):defaultValue=1
_DtmIfTxCapacityStart_Type.__name__=_H
_DtmIfTxCapacityStart_Object=MibTableColumn
dtmIfTxCapacityStart=_DtmIfTxCapacityStart_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,6),_DtmIfTxCapacityStart_Type())
dtmIfTxCapacityStart.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfTxCapacityStart.setStatus(_G)
class _DtmIfTxCapacityOwned_Type(Gauge32):defaultValue=0
_DtmIfTxCapacityOwned_Type.__name__=_H
_DtmIfTxCapacityOwned_Object=MibTableColumn
dtmIfTxCapacityOwned=_DtmIfTxCapacityOwned_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,7),_DtmIfTxCapacityOwned_Type())
dtmIfTxCapacityOwned.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfTxCapacityOwned.setStatus(_G)
_DtmIfTxCapacityBorrowed_Type=Gauge32
_DtmIfTxCapacityBorrowed_Object=MibTableColumn
dtmIfTxCapacityBorrowed=_DtmIfTxCapacityBorrowed_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,8),_DtmIfTxCapacityBorrowed_Type())
dtmIfTxCapacityBorrowed.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfTxCapacityBorrowed.setStatus(_G)
class _DtmIfTxCapacityMaxLend_Type(Gauge32):defaultValue=0
_DtmIfTxCapacityMaxLend_Type.__name__=_H
_DtmIfTxCapacityMaxLend_Object=MibTableColumn
dtmIfTxCapacityMaxLend=_DtmIfTxCapacityMaxLend_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,9),_DtmIfTxCapacityMaxLend_Type())
dtmIfTxCapacityMaxLend.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfTxCapacityMaxLend.setStatus(_G)
_DtmIfTxCapacityLent_Type=Gauge32
_DtmIfTxCapacityLent_Object=MibTableColumn
dtmIfTxCapacityLent=_DtmIfTxCapacityLent_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,10),_DtmIfTxCapacityLent_Type())
dtmIfTxCapacityLent.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfTxCapacityLent.setStatus(_G)
_DtmIfTxCapacityUsed_Type=Gauge32
_DtmIfTxCapacityUsed_Object=MibTableColumn
dtmIfTxCapacityUsed=_DtmIfTxCapacityUsed_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,11),_DtmIfTxCapacityUsed_Type())
dtmIfTxCapacityUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfTxCapacityUsed.setStatus(_A)
_DtmIfRxCapacity_Type=Gauge32
_DtmIfRxCapacity_Object=MibTableColumn
dtmIfRxCapacity=_DtmIfRxCapacity_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,12),_DtmIfRxCapacity_Type())
dtmIfRxCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfRxCapacity.setStatus(_A)
_DtmIfRxCapacityUsed_Type=Gauge32
_DtmIfRxCapacityUsed_Object=MibTableColumn
dtmIfRxCapacityUsed=_DtmIfRxCapacityUsed_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,13),_DtmIfRxCapacityUsed_Type())
dtmIfRxCapacityUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfRxCapacityUsed.setStatus(_A)
class _DtmIfIfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DtmIfIfIndex_Type.__name__=_C
_DtmIfIfIndex_Object=MibTableColumn
dtmIfIfIndex=_DtmIfIfIndex_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,14),_DtmIfIfIndex_Type())
dtmIfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfIfIndex.setStatus(_G)
class _DtmIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_K,2)))
_DtmIfAdminStatus_Type.__name__=_C
_DtmIfAdminStatus_Object=MibTableColumn
dtmIfAdminStatus=_DtmIfAdminStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,15),_DtmIfAdminStatus_Type())
dtmIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfAdminStatus.setStatus(_A)
class _DtmIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_K,2),(_T,3),(_U,4)))
_DtmIfOperStatus_Type.__name__=_C
_DtmIfOperStatus_Object=MibTableColumn
dtmIfOperStatus=_DtmIfOperStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,16),_DtmIfOperStatus_Type())
dtmIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfOperStatus.setStatus(_A)
_DtmIfRowStatus_Type=RowStatus
_DtmIfRowStatus_Object=MibTableColumn
dtmIfRowStatus=_DtmIfRowStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,17),_DtmIfRowStatus_Type())
dtmIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfRowStatus.setStatus(_A)
_DtmIfAbsent_Type=FaultStatus
_DtmIfAbsent_Object=MibTableColumn
dtmIfAbsent=_DtmIfAbsent_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,18),_DtmIfAbsent_Type())
dtmIfAbsent.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfAbsent.setStatus(_G)
_DtmIfLOS_Type=FaultStatus
_DtmIfLOS_Object=MibTableColumn
dtmIfLOS=_DtmIfLOS_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,19),_DtmIfLOS_Type())
dtmIfLOS.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfLOS.setStatus(_A)
_DtmIfReducedCtrlCapacity_Type=FaultStatus
_DtmIfReducedCtrlCapacity_Object=MibTableColumn
dtmIfReducedCtrlCapacity=_DtmIfReducedCtrlCapacity_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,20),_DtmIfReducedCtrlCapacity_Type())
dtmIfReducedCtrlCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmIfReducedCtrlCapacity.setStatus(_A)
class _DtmIfTxCapacityOwnedFirstSlot_Type(Gauge32):defaultValue=0
_DtmIfTxCapacityOwnedFirstSlot_Type.__name__=_H
_DtmIfTxCapacityOwnedFirstSlot_Object=MibTableColumn
dtmIfTxCapacityOwnedFirstSlot=_DtmIfTxCapacityOwnedFirstSlot_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,21),_DtmIfTxCapacityOwnedFirstSlot_Type())
dtmIfTxCapacityOwnedFirstSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfTxCapacityOwnedFirstSlot.setStatus(_G)
class _DtmIfTxCapacityOwnedLastSlot_Type(Gauge32):defaultValue=0
_DtmIfTxCapacityOwnedLastSlot_Type.__name__=_H
_DtmIfTxCapacityOwnedLastSlot_Object=MibTableColumn
dtmIfTxCapacityOwnedLastSlot=_DtmIfTxCapacityOwnedLastSlot_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,22),_DtmIfTxCapacityOwnedLastSlot_Type())
dtmIfTxCapacityOwnedLastSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfTxCapacityOwnedLastSlot.setStatus(_A)
class _DtmIfRouteMetric_Type(Unsigned32):defaultValue=1
_DtmIfRouteMetric_Type.__name__=_J
_DtmIfRouteMetric_Object=MibTableColumn
dtmIfRouteMetric=_DtmIfRouteMetric_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,23),_DtmIfRouteMetric_Type())
dtmIfRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfRouteMetric.setStatus(_A)
class _DtmIfLinkClass_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('persistent',2),('nailed',3)))
_DtmIfLinkClass_Type.__name__=_C
_DtmIfLinkClass_Object=MibTableColumn
dtmIfLinkClass=_DtmIfLinkClass_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,24),_DtmIfLinkClass_Type())
dtmIfLinkClass.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfLinkClass.setStatus(_A)
class _DtmIfPurpose_Type(SnmpAdminString):defaultHexValue=''
_DtmIfPurpose_Type.__name__=_M
_DtmIfPurpose_Object=MibTableColumn
dtmIfPurpose=_DtmIfPurpose_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,25),_DtmIfPurpose_Type())
dtmIfPurpose.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfPurpose.setStatus(_A)
class _DtmIfSyncEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_DtmIfSyncEnabled_Type.__name__=_C
_DtmIfSyncEnabled_Object=MibTableColumn
dtmIfSyncEnabled=_DtmIfSyncEnabled_Object((1,3,6,1,4,1,2928,6,2,4,1,2,1,1,26),_DtmIfSyncEnabled_Type())
dtmIfSyncEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:dtmIfSyncEnabled.setStatus(_A)
_DtmLinkStateGroup_ObjectIdentity=ObjectIdentity
dtmLinkStateGroup=_DtmLinkStateGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,4,1,3))
_DtmLinkStateTableLastChangedTime_Type=DateAndTime
_DtmLinkStateTableLastChangedTime_Object=MibScalar
dtmLinkStateTableLastChangedTime=_DtmLinkStateTableLastChangedTime_Object((1,3,6,1,4,1,2928,6,2,4,1,3,1),_DtmLinkStateTableLastChangedTime_Type())
dtmLinkStateTableLastChangedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateTableLastChangedTime.setStatus(_A)
_DtmLinkStateNrOfLinks_Type=Unsigned32
_DtmLinkStateNrOfLinks_Object=MibScalar
dtmLinkStateNrOfLinks=_DtmLinkStateNrOfLinks_Object((1,3,6,1,4,1,2928,6,2,4,1,3,2),_DtmLinkStateNrOfLinks_Type())
dtmLinkStateNrOfLinks.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateNrOfLinks.setStatus(_A)
_DtmLinkStateTable_Object=MibTable
dtmLinkStateTable=_DtmLinkStateTable_Object((1,3,6,1,4,1,2928,6,2,4,1,3,3))
if mibBuilder.loadTexts:dtmLinkStateTable.setStatus(_A)
_DtmLinkStateEntry_Object=MibTableRow
dtmLinkStateEntry=_DtmLinkStateEntry_Object((1,3,6,1,4,1,2928,6,2,4,1,3,3,1))
dtmLinkStateEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:dtmLinkStateEntry.setStatus(_A)
_DtmLinkStateIndex_Type=Unsigned32
_DtmLinkStateIndex_Object=MibTableColumn
dtmLinkStateIndex=_DtmLinkStateIndex_Object((1,3,6,1,4,1,2928,6,2,4,1,3,3,1,1),_DtmLinkStateIndex_Type())
dtmLinkStateIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateIndex.setStatus(_A)
class _DtmLinkStateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('looped',2),('open',3)))
_DtmLinkStateType_Type.__name__=_C
_DtmLinkStateType_Object=MibTableColumn
dtmLinkStateType=_DtmLinkStateType_Object((1,3,6,1,4,1,2928,6,2,4,1,3,3,1,2),_DtmLinkStateType_Type())
dtmLinkStateType.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateType.setStatus(_A)
_DtmLinkStateLocalIf_Type=DisplayString
_DtmLinkStateLocalIf_Object=MibTableColumn
dtmLinkStateLocalIf=_DtmLinkStateLocalIf_Object((1,3,6,1,4,1,2928,6,2,4,1,3,3,1,3),_DtmLinkStateLocalIf_Type())
dtmLinkStateLocalIf.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateLocalIf.setStatus(_A)
_DtmLinkStateNrOfIfs_Type=Unsigned32
_DtmLinkStateNrOfIfs_Object=MibScalar
dtmLinkStateNrOfIfs=_DtmLinkStateNrOfIfs_Object((1,3,6,1,4,1,2928,6,2,4,1,3,4),_DtmLinkStateNrOfIfs_Type())
dtmLinkStateNrOfIfs.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateNrOfIfs.setStatus(_A)
_DtmLinkStateIfTable_Object=MibTable
dtmLinkStateIfTable=_DtmLinkStateIfTable_Object((1,3,6,1,4,1,2928,6,2,4,1,3,5))
if mibBuilder.loadTexts:dtmLinkStateIfTable.setStatus(_A)
_DtmLinkStateIfEntry_Object=MibTableRow
dtmLinkStateIfEntry=_DtmLinkStateIfEntry_Object((1,3,6,1,4,1,2928,6,2,4,1,3,5,1))
dtmLinkStateIfEntry.setIndexNames((0,_F,_L),(0,_F,_V))
if mibBuilder.loadTexts:dtmLinkStateIfEntry.setStatus(_A)
_DtmLinkStateIfIndex_Type=Unsigned32
_DtmLinkStateIfIndex_Object=MibTableColumn
dtmLinkStateIfIndex=_DtmLinkStateIfIndex_Object((1,3,6,1,4,1,2928,6,2,4,1,3,5,1,1),_DtmLinkStateIfIndex_Type())
dtmLinkStateIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateIfIndex.setStatus(_A)
_DtmLinkStateIfMacAddress_Type=MacAddress
_DtmLinkStateIfMacAddress_Object=MibTableColumn
dtmLinkStateIfMacAddress=_DtmLinkStateIfMacAddress_Object((1,3,6,1,4,1,2928,6,2,4,1,3,5,1,2),_DtmLinkStateIfMacAddress_Type())
dtmLinkStateIfMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateIfMacAddress.setStatus(_A)
_DtmLinkStateIfNodeMacAddress_Type=MacAddress
_DtmLinkStateIfNodeMacAddress_Object=MibTableColumn
dtmLinkStateIfNodeMacAddress=_DtmLinkStateIfNodeMacAddress_Object((1,3,6,1,4,1,2928,6,2,4,1,3,5,1,3),_DtmLinkStateIfNodeMacAddress_Type())
dtmLinkStateIfNodeMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateIfNodeMacAddress.setStatus(_A)
_DtmLinkStateIfNodeAddress_Type=DtmAddress
_DtmLinkStateIfNodeAddress_Object=MibTableColumn
dtmLinkStateIfNodeAddress=_DtmLinkStateIfNodeAddress_Object((1,3,6,1,4,1,2928,6,2,4,1,3,5,1,4),_DtmLinkStateIfNodeAddress_Type())
dtmLinkStateIfNodeAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateIfNodeAddress.setStatus(_A)
_DtmLinkStateLocalSubIf_Type=DisplayString
_DtmLinkStateLocalSubIf_Object=MibTableColumn
dtmLinkStateLocalSubIf=_DtmLinkStateLocalSubIf_Object((1,3,6,1,4,1,2928,6,2,4,1,3,5,1,5),_DtmLinkStateLocalSubIf_Type())
dtmLinkStateLocalSubIf.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateLocalSubIf.setStatus(_A)
class _DtmLinkStateIfNodeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notApplicable',0),(_I,1),(_W,2),(_X,3),(_Y,4),('downKeep',5),('pending',6),(_P,7)))
_DtmLinkStateIfNodeStatus_Type.__name__=_C
_DtmLinkStateIfNodeStatus_Object=MibTableColumn
dtmLinkStateIfNodeStatus=_DtmLinkStateIfNodeStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,3,5,1,6),_DtmLinkStateIfNodeStatus_Type())
dtmLinkStateIfNodeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmLinkStateIfNodeStatus.setStatus(_A)
_DtmRouteGroup_ObjectIdentity=ObjectIdentity
dtmRouteGroup=_DtmRouteGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,4,1,4))
_DtmDrpNodeRouteMetric_Type=Unsigned32
_DtmDrpNodeRouteMetric_Object=MibScalar
dtmDrpNodeRouteMetric=_DtmDrpNodeRouteMetric_Object((1,3,6,1,4,1,2928,6,2,4,1,4,2),_DtmDrpNodeRouteMetric_Type())
dtmDrpNodeRouteMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmDrpNodeRouteMetric.setStatus(_A)
class _DtmDrpNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switch',1),('endNode',2)))
_DtmDrpNodeType_Type.__name__=_C
_DtmDrpNodeType_Object=MibScalar
dtmDrpNodeType=_DtmDrpNodeType_Object((1,3,6,1,4,1,2928,6,2,4,1,4,3),_DtmDrpNodeType_Type())
dtmDrpNodeType.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmDrpNodeType.setStatus(_A)
_DtmDrpAreaNumber_Type=Unsigned32
_DtmDrpAreaNumber_Object=MibScalar
dtmDrpAreaNumber=_DtmDrpAreaNumber_Object((1,3,6,1,4,1,2928,6,2,4,1,4,4),_DtmDrpAreaNumber_Type())
dtmDrpAreaNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmDrpAreaNumber.setStatus(_A)
_DtmDrpDetectAreaNumber_Type=TruthValue
_DtmDrpDetectAreaNumber_Object=MibScalar
dtmDrpDetectAreaNumber=_DtmDrpDetectAreaNumber_Object((1,3,6,1,4,1,2928,6,2,4,1,4,5),_DtmDrpDetectAreaNumber_Type())
dtmDrpDetectAreaNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmDrpDetectAreaNumber.setStatus(_A)
_DtmDrpDetectDefaultGateway_Type=TruthValue
_DtmDrpDetectDefaultGateway_Object=MibScalar
dtmDrpDetectDefaultGateway=_DtmDrpDetectDefaultGateway_Object((1,3,6,1,4,1,2928,6,2,4,1,4,6),_DtmDrpDetectDefaultGateway_Type())
dtmDrpDetectDefaultGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmDrpDetectDefaultGateway.setStatus(_A)
_DtmHistoryGroup_ObjectIdentity=ObjectIdentity
dtmHistoryGroup=_DtmHistoryGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,4,1,5))
_DtmNodeGroup_ObjectIdentity=ObjectIdentity
dtmNodeGroup=_DtmNodeGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,4,1,6))
class _DtmNodeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_W,2),(_X,3),(_Y,4)))
_DtmNodeStatus_Type.__name__=_C
_DtmNodeStatus_Object=MibScalar
dtmNodeStatus=_DtmNodeStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,6,1),_DtmNodeStatus_Type())
dtmNodeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmNodeStatus.setStatus(_A)
_DtmNodeRestartOnError_Type=TruthValue
_DtmNodeRestartOnError_Object=MibScalar
dtmNodeRestartOnError=_DtmNodeRestartOnError_Object((1,3,6,1,4,1,2928,6,2,4,1,6,2),_DtmNodeRestartOnError_Type())
dtmNodeRestartOnError.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmNodeRestartOnError.setStatus(_A)
_DtmNodeId_Type=MacAddress
_DtmNodeId_Object=MibScalar
dtmNodeId=_DtmNodeId_Object((1,3,6,1,4,1,2928,6,2,4,1,6,3),_DtmNodeId_Type())
dtmNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmNodeId.setStatus(_A)
_DtmSyncGroup_ObjectIdentity=ObjectIdentity
dtmSyncGroup=_DtmSyncGroup_ObjectIdentity((1,3,6,1,4,1,2928,6,2,4,1,7))
_DtmSyncNodeId_Type=MacAddress
_DtmSyncNodeId_Object=MibScalar
dtmSyncNodeId=_DtmSyncNodeId_Object((1,3,6,1,4,1,2928,6,2,4,1,7,1),_DtmSyncNodeId_Type())
dtmSyncNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmSyncNodeId.setStatus(_A)
_DtmCurrentTimingSourceName_Type=DisplayString
_DtmCurrentTimingSourceName_Object=MibScalar
dtmCurrentTimingSourceName=_DtmCurrentTimingSourceName_Object((1,3,6,1,4,1,2928,6,2,4,1,7,2),_DtmCurrentTimingSourceName_Type())
dtmCurrentTimingSourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmCurrentTimingSourceName.setStatus(_A)
_DtmCurrentTimingSourcePeerId_Type=MacAddress
_DtmCurrentTimingSourcePeerId_Object=MibScalar
dtmCurrentTimingSourcePeerId=_DtmCurrentTimingSourcePeerId_Object((1,3,6,1,4,1,2928,6,2,4,1,7,3),_DtmCurrentTimingSourcePeerId_Type())
dtmCurrentTimingSourcePeerId.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmCurrentTimingSourcePeerId.setStatus(_A)
class _DtmTimeScaleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notSupported',1),('uninitiated',2),('reassigned',3),('compensated',4)))
_DtmTimeScaleStatus_Type.__name__=_C
_DtmTimeScaleStatus_Object=MibScalar
dtmTimeScaleStatus=_DtmTimeScaleStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,7,4),_DtmTimeScaleStatus_Type())
dtmTimeScaleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmTimeScaleStatus.setStatus(_A)
_DtmTimeSourceCalibrationReference_Type=Integer32
_DtmTimeSourceCalibrationReference_Object=MibScalar
dtmTimeSourceCalibrationReference=_DtmTimeSourceCalibrationReference_Object((1,3,6,1,4,1,2928,6,2,4,1,7,5),_DtmTimeSourceCalibrationReference_Type())
dtmTimeSourceCalibrationReference.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmTimeSourceCalibrationReference.setStatus(_A)
_DtmTimeSourceTable_Object=MibTable
dtmTimeSourceTable=_DtmTimeSourceTable_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6))
if mibBuilder.loadTexts:dtmTimeSourceTable.setStatus(_A)
_DtmTimeSourceEntry_Object=MibTableRow
dtmTimeSourceEntry=_DtmTimeSourceEntry_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1))
dtmTimeSourceEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:dtmTimeSourceEntry.setStatus(_A)
class _DtmTimeSourceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DtmTimeSourceIndex_Type.__name__=_C
_DtmTimeSourceIndex_Object=MibTableColumn
dtmTimeSourceIndex=_DtmTimeSourceIndex_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,1),_DtmTimeSourceIndex_Type())
dtmTimeSourceIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:dtmTimeSourceIndex.setStatus(_A)
_DtmTimeSourceName_Type=DisplayString
_DtmTimeSourceName_Object=MibTableColumn
dtmTimeSourceName=_DtmTimeSourceName_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,2),_DtmTimeSourceName_Type())
dtmTimeSourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmTimeSourceName.setStatus(_A)
class _DtmTimeSourceAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_K,2)))
_DtmTimeSourceAdminStatus_Type.__name__=_C
_DtmTimeSourceAdminStatus_Object=MibTableColumn
dtmTimeSourceAdminStatus=_DtmTimeSourceAdminStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,3),_DtmTimeSourceAdminStatus_Type())
dtmTimeSourceAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmTimeSourceAdminStatus.setStatus(_A)
class _DtmTimeSourceOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_K,2),(_T,3),(_U,4),('dormant',5)))
_DtmTimeSourceOperStatus_Type.__name__=_C
_DtmTimeSourceOperStatus_Object=MibTableColumn
dtmTimeSourceOperStatus=_DtmTimeSourceOperStatus_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,4),_DtmTimeSourceOperStatus_Type())
dtmTimeSourceOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmTimeSourceOperStatus.setStatus(_A)
class _DtmTimeSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dsyp',1),('sqc',2),('ssm',3),('internal',4)))
_DtmTimeSourceType_Type.__name__=_C
_DtmTimeSourceType_Object=MibTableColumn
dtmTimeSourceType=_DtmTimeSourceType_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,5),_DtmTimeSourceType_Type())
dtmTimeSourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmTimeSourceType.setStatus(_A)
_DtmTimeSourceRef_Type=RowPointer
_DtmTimeSourceRef_Object=MibTableColumn
dtmTimeSourceRef=_DtmTimeSourceRef_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,6),_DtmTimeSourceRef_Type())
dtmTimeSourceRef.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmTimeSourceRef.setStatus(_A)
_DtmTimeSourceRoundTripTime_Type=Unsigned32
_DtmTimeSourceRoundTripTime_Object=MibTableColumn
dtmTimeSourceRoundTripTime=_DtmTimeSourceRoundTripTime_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,7),_DtmTimeSourceRoundTripTime_Type())
dtmTimeSourceRoundTripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmTimeSourceRoundTripTime.setStatus(_A)
_DtmTimeSourceTimeError_Type=Integer32
_DtmTimeSourceTimeError_Object=MibTableColumn
dtmTimeSourceTimeError=_DtmTimeSourceTimeError_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,8),_DtmTimeSourceTimeError_Type())
dtmTimeSourceTimeError.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmTimeSourceTimeError.setStatus(_A)
_DtmTimeSourceCalibrationTimeError_Type=Integer32
_DtmTimeSourceCalibrationTimeError_Object=MibTableColumn
dtmTimeSourceCalibrationTimeError=_DtmTimeSourceCalibrationTimeError_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,9),_DtmTimeSourceCalibrationTimeError_Type())
dtmTimeSourceCalibrationTimeError.setMaxAccess(_B)
if mibBuilder.loadTexts:dtmTimeSourceCalibrationTimeError.setStatus(_A)
class _DtmTimeSourceCalibrationRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-499999,499999))
_DtmTimeSourceCalibrationRatio_Type.__name__=_C
_DtmTimeSourceCalibrationRatio_Object=MibTableColumn
dtmTimeSourceCalibrationRatio=_DtmTimeSourceCalibrationRatio_Object((1,3,6,1,4,1,2928,6,2,4,1,7,6,1,10),_DtmTimeSourceCalibrationRatio_Type())
dtmTimeSourceCalibrationRatio.setMaxAccess(_E)
if mibBuilder.loadTexts:dtmTimeSourceCalibrationRatio.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'DtmAddress':DtmAddress,'DtmSourceRoute':DtmSourceRoute,'netiDTMMIB':netiDTMMIB,'netiDTMMIBObjects':netiDTMMIBObjects,'dtmAddrGroup':dtmAddrGroup,'dtmAddrTable':dtmAddrTable,'dtmAddrEntry':dtmAddrEntry,_O:dtmAddrEntryIndex,'dtmAddrEntryAddr':dtmAddrEntryAddr,'dtmAddrEntryIsAlias':dtmAddrEntryIsAlias,'dtmAddrEntryAddrType':dtmAddrEntryAddrType,'dtmAddrEntryRowStatus':dtmAddrEntryRowStatus,'dtmHostsTable':dtmHostsTable,'dtmHostsEntry':dtmHostsEntry,_Q:dtmHostsEntryIndex,'dtmHostsEntryAddr':dtmHostsEntryAddr,'dtmHostsEntryName':dtmHostsEntryName,'dtmHostsEntryRowStatus':dtmHostsEntryRowStatus,'dtmIfGroup':dtmIfGroup,'dtmIfTable':dtmIfTable,'dtmIfEntry':dtmIfEntry,_S:dtmIfIndex,'dtmIfName':dtmIfName,'dtmIfMacAddress':dtmIfMacAddress,'dtmIfTxCapacity':dtmIfTxCapacity,'dtmIfTxCapacityCtrl':dtmIfTxCapacityCtrl,'dtmIfTxCapacityStart':dtmIfTxCapacityStart,'dtmIfTxCapacityOwned':dtmIfTxCapacityOwned,'dtmIfTxCapacityBorrowed':dtmIfTxCapacityBorrowed,'dtmIfTxCapacityMaxLend':dtmIfTxCapacityMaxLend,'dtmIfTxCapacityLent':dtmIfTxCapacityLent,'dtmIfTxCapacityUsed':dtmIfTxCapacityUsed,'dtmIfRxCapacity':dtmIfRxCapacity,'dtmIfRxCapacityUsed':dtmIfRxCapacityUsed,'dtmIfIfIndex':dtmIfIfIndex,'dtmIfAdminStatus':dtmIfAdminStatus,'dtmIfOperStatus':dtmIfOperStatus,'dtmIfRowStatus':dtmIfRowStatus,'dtmIfAbsent':dtmIfAbsent,'dtmIfLOS':dtmIfLOS,'dtmIfReducedCtrlCapacity':dtmIfReducedCtrlCapacity,'dtmIfTxCapacityOwnedFirstSlot':dtmIfTxCapacityOwnedFirstSlot,'dtmIfTxCapacityOwnedLastSlot':dtmIfTxCapacityOwnedLastSlot,'dtmIfRouteMetric':dtmIfRouteMetric,'dtmIfLinkClass':dtmIfLinkClass,'dtmIfPurpose':dtmIfPurpose,'dtmIfSyncEnabled':dtmIfSyncEnabled,'dtmLinkStateGroup':dtmLinkStateGroup,'dtmLinkStateTableLastChangedTime':dtmLinkStateTableLastChangedTime,'dtmLinkStateNrOfLinks':dtmLinkStateNrOfLinks,'dtmLinkStateTable':dtmLinkStateTable,'dtmLinkStateEntry':dtmLinkStateEntry,_L:dtmLinkStateIndex,'dtmLinkStateType':dtmLinkStateType,'dtmLinkStateLocalIf':dtmLinkStateLocalIf,'dtmLinkStateNrOfIfs':dtmLinkStateNrOfIfs,'dtmLinkStateIfTable':dtmLinkStateIfTable,'dtmLinkStateIfEntry':dtmLinkStateIfEntry,_V:dtmLinkStateIfIndex,'dtmLinkStateIfMacAddress':dtmLinkStateIfMacAddress,'dtmLinkStateIfNodeMacAddress':dtmLinkStateIfNodeMacAddress,'dtmLinkStateIfNodeAddress':dtmLinkStateIfNodeAddress,'dtmLinkStateLocalSubIf':dtmLinkStateLocalSubIf,'dtmLinkStateIfNodeStatus':dtmLinkStateIfNodeStatus,'dtmRouteGroup':dtmRouteGroup,'dtmDrpNodeRouteMetric':dtmDrpNodeRouteMetric,'dtmDrpNodeType':dtmDrpNodeType,'dtmDrpAreaNumber':dtmDrpAreaNumber,'dtmDrpDetectAreaNumber':dtmDrpDetectAreaNumber,'dtmDrpDetectDefaultGateway':dtmDrpDetectDefaultGateway,'dtmHistoryGroup':dtmHistoryGroup,'dtmNodeGroup':dtmNodeGroup,'dtmNodeStatus':dtmNodeStatus,'dtmNodeRestartOnError':dtmNodeRestartOnError,'dtmNodeId':dtmNodeId,'dtmSyncGroup':dtmSyncGroup,'dtmSyncNodeId':dtmSyncNodeId,'dtmCurrentTimingSourceName':dtmCurrentTimingSourceName,'dtmCurrentTimingSourcePeerId':dtmCurrentTimingSourcePeerId,'dtmTimeScaleStatus':dtmTimeScaleStatus,'dtmTimeSourceCalibrationReference':dtmTimeSourceCalibrationReference,'dtmTimeSourceTable':dtmTimeSourceTable,'dtmTimeSourceEntry':dtmTimeSourceEntry,_Z:dtmTimeSourceIndex,'dtmTimeSourceName':dtmTimeSourceName,'dtmTimeSourceAdminStatus':dtmTimeSourceAdminStatus,'dtmTimeSourceOperStatus':dtmTimeSourceOperStatus,'dtmTimeSourceType':dtmTimeSourceType,'dtmTimeSourceRef':dtmTimeSourceRef,'dtmTimeSourceRoundTripTime':dtmTimeSourceRoundTripTime,'dtmTimeSourceTimeError':dtmTimeSourceTimeError,'dtmTimeSourceCalibrationTimeError':dtmTimeSourceCalibrationTimeError,'dtmTimeSourceCalibrationRatio':dtmTimeSourceCalibrationRatio})