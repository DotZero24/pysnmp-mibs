_M='rlIpPrefListInfoName'
_L='rlIpPrefListInfoType'
_K='rlIpPrefListEntryIndex'
_J='rlIpPrefListName'
_I='rlIpPrefListType'
_H='Unsigned32'
_G='read-only'
_F='DisplayString'
_E='Integer32'
_D='not-accessible'
_C='RADLAN-ippreflist-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType,InetVersion,InetZoneIndex=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType','InetVersion','InetZoneIndex')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
class RlIpPrefListEntryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rule',1),('description',2)))
class RlIpPrefListActionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),('permit',2)))
class RlIpPrefListType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_RlIpPrefList_ObjectIdentity=ObjectIdentity
rlIpPrefList=_RlIpPrefList_ObjectIdentity((1,3,6,1,4,1,89,212))
_RlIpPrefListTable_Object=MibTable
rlIpPrefListTable=_RlIpPrefListTable_Object((1,3,6,1,4,1,89,212,1))
if mibBuilder.loadTexts:rlIpPrefListTable.setStatus(_A)
_RlIpPrefListEntry_Object=MibTableRow
rlIpPrefListEntry=_RlIpPrefListEntry_Object((1,3,6,1,4,1,89,212,1,1))
rlIpPrefListEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:rlIpPrefListEntry.setStatus(_A)
_RlIpPrefListType_Type=RlIpPrefListType
_RlIpPrefListType_Object=MibTableColumn
rlIpPrefListType=_RlIpPrefListType_Object((1,3,6,1,4,1,89,212,1,1,1),_RlIpPrefListType_Type())
rlIpPrefListType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIpPrefListType.setStatus(_A)
class _RlIpPrefListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlIpPrefListName_Type.__name__=_F
_RlIpPrefListName_Object=MibTableColumn
rlIpPrefListName=_RlIpPrefListName_Object((1,3,6,1,4,1,89,212,1,1,2),_RlIpPrefListName_Type())
rlIpPrefListName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIpPrefListName.setStatus(_A)
class _RlIpPrefListEntryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967294))
_RlIpPrefListEntryIndex_Type.__name__=_H
_RlIpPrefListEntryIndex_Object=MibTableColumn
rlIpPrefListEntryIndex=_RlIpPrefListEntryIndex_Object((1,3,6,1,4,1,89,212,1,1,3),_RlIpPrefListEntryIndex_Type())
rlIpPrefListEntryIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIpPrefListEntryIndex.setStatus(_A)
_RlIpPrefListEntryType_Type=RlIpPrefListEntryType
_RlIpPrefListEntryType_Object=MibTableColumn
rlIpPrefListEntryType=_RlIpPrefListEntryType_Object((1,3,6,1,4,1,89,212,1,1,4),_RlIpPrefListEntryType_Type())
rlIpPrefListEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIpPrefListEntryType.setStatus(_A)
_RlIpPrefListInetAddrType_Type=InetAddressType
_RlIpPrefListInetAddrType_Object=MibTableColumn
rlIpPrefListInetAddrType=_RlIpPrefListInetAddrType_Object((1,3,6,1,4,1,89,212,1,1,5),_RlIpPrefListInetAddrType_Type())
rlIpPrefListInetAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIpPrefListInetAddrType.setStatus(_A)
_RlIpPrefListInetAddr_Type=InetAddress
_RlIpPrefListInetAddr_Object=MibTableColumn
rlIpPrefListInetAddr=_RlIpPrefListInetAddr_Object((1,3,6,1,4,1,89,212,1,1,6),_RlIpPrefListInetAddr_Type())
rlIpPrefListInetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIpPrefListInetAddr.setStatus(_A)
class _RlIpPrefListPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_RlIpPrefListPrefixLength_Type.__name__=_E
_RlIpPrefListPrefixLength_Object=MibTableColumn
rlIpPrefListPrefixLength=_RlIpPrefListPrefixLength_Object((1,3,6,1,4,1,89,212,1,1,7),_RlIpPrefListPrefixLength_Type())
rlIpPrefListPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIpPrefListPrefixLength.setStatus(_A)
_RlIpPrefListAction_Type=RlIpPrefListActionType
_RlIpPrefListAction_Object=MibTableColumn
rlIpPrefListAction=_RlIpPrefListAction_Object((1,3,6,1,4,1,89,212,1,1,8),_RlIpPrefListAction_Type())
rlIpPrefListAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIpPrefListAction.setStatus(_A)
class _RlIpPrefListGeLength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_RlIpPrefListGeLength_Type.__name__=_E
_RlIpPrefListGeLength_Object=MibTableColumn
rlIpPrefListGeLength=_RlIpPrefListGeLength_Object((1,3,6,1,4,1,89,212,1,1,9),_RlIpPrefListGeLength_Type())
rlIpPrefListGeLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIpPrefListGeLength.setStatus(_A)
class _RlIpPrefListLeLength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_RlIpPrefListLeLength_Type.__name__=_E
_RlIpPrefListLeLength_Object=MibTableColumn
rlIpPrefListLeLength=_RlIpPrefListLeLength_Object((1,3,6,1,4,1,89,212,1,1,10),_RlIpPrefListLeLength_Type())
rlIpPrefListLeLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIpPrefListLeLength.setStatus(_A)
class _RlIpPrefListDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_RlIpPrefListDescription_Type.__name__=_F
_RlIpPrefListDescription_Object=MibTableColumn
rlIpPrefListDescription=_RlIpPrefListDescription_Object((1,3,6,1,4,1,89,212,1,1,11),_RlIpPrefListDescription_Type())
rlIpPrefListDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIpPrefListDescription.setStatus(_A)
_RlIpPrefListHitCount_Type=Integer32
_RlIpPrefListHitCount_Object=MibTableColumn
rlIpPrefListHitCount=_RlIpPrefListHitCount_Object((1,3,6,1,4,1,89,212,1,1,12),_RlIpPrefListHitCount_Type())
rlIpPrefListHitCount.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIpPrefListHitCount.setStatus(_A)
_RlIpPrefListRowStatus_Type=RowStatus
_RlIpPrefListRowStatus_Object=MibTableColumn
rlIpPrefListRowStatus=_RlIpPrefListRowStatus_Object((1,3,6,1,4,1,89,212,1,1,13),_RlIpPrefListRowStatus_Type())
rlIpPrefListRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlIpPrefListRowStatus.setStatus(_A)
_RlIpPrefListInfoTable_Object=MibTable
rlIpPrefListInfoTable=_RlIpPrefListInfoTable_Object((1,3,6,1,4,1,89,212,2))
if mibBuilder.loadTexts:rlIpPrefListInfoTable.setStatus(_A)
_RlIpPrefListInfoEntry_Object=MibTableRow
rlIpPrefListInfoEntry=_RlIpPrefListInfoEntry_Object((1,3,6,1,4,1,89,212,2,1))
rlIpPrefListInfoEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:rlIpPrefListInfoEntry.setStatus(_A)
_RlIpPrefListInfoType_Type=RlIpPrefListType
_RlIpPrefListInfoType_Object=MibTableColumn
rlIpPrefListInfoType=_RlIpPrefListInfoType_Object((1,3,6,1,4,1,89,212,2,1,1),_RlIpPrefListInfoType_Type())
rlIpPrefListInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIpPrefListInfoType.setStatus(_A)
class _RlIpPrefListInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlIpPrefListInfoName_Type.__name__=_F
_RlIpPrefListInfoName_Object=MibTableColumn
rlIpPrefListInfoName=_RlIpPrefListInfoName_Object((1,3,6,1,4,1,89,212,2,1,2),_RlIpPrefListInfoName_Type())
rlIpPrefListInfoName.setMaxAccess(_D)
if mibBuilder.loadTexts:rlIpPrefListInfoName.setStatus(_A)
_RlIpPrefListInfoEntriesNumber_Type=Integer32
_RlIpPrefListInfoEntriesNumber_Object=MibTableColumn
rlIpPrefListInfoEntriesNumber=_RlIpPrefListInfoEntriesNumber_Object((1,3,6,1,4,1,89,212,2,1,3),_RlIpPrefListInfoEntriesNumber_Type())
rlIpPrefListInfoEntriesNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:rlIpPrefListInfoEntriesNumber.setStatus(_A)
_RlIpPrefListInfoRangeEntries_Type=Integer32
_RlIpPrefListInfoRangeEntries_Object=MibTableColumn
rlIpPrefListInfoRangeEntries=_RlIpPrefListInfoRangeEntries_Object((1,3,6,1,4,1,89,212,2,1,4),_RlIpPrefListInfoRangeEntries_Type())
rlIpPrefListInfoRangeEntries.setMaxAccess(_G)
if mibBuilder.loadTexts:rlIpPrefListInfoRangeEntries.setStatus(_A)
_RlIpPrefListInfoNextFreeIndex_Type=Integer32
_RlIpPrefListInfoNextFreeIndex_Object=MibTableColumn
rlIpPrefListInfoNextFreeIndex=_RlIpPrefListInfoNextFreeIndex_Object((1,3,6,1,4,1,89,212,2,1,5),_RlIpPrefListInfoNextFreeIndex_Type())
rlIpPrefListInfoNextFreeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlIpPrefListInfoNextFreeIndex.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RlIpPrefListEntryType':RlIpPrefListEntryType,'RlIpPrefListActionType':RlIpPrefListActionType,'RlIpPrefListType':RlIpPrefListType,'rlIpPrefList':rlIpPrefList,'rlIpPrefListTable':rlIpPrefListTable,'rlIpPrefListEntry':rlIpPrefListEntry,_I:rlIpPrefListType,_J:rlIpPrefListName,_K:rlIpPrefListEntryIndex,'rlIpPrefListEntryType':rlIpPrefListEntryType,'rlIpPrefListInetAddrType':rlIpPrefListInetAddrType,'rlIpPrefListInetAddr':rlIpPrefListInetAddr,'rlIpPrefListPrefixLength':rlIpPrefListPrefixLength,'rlIpPrefListAction':rlIpPrefListAction,'rlIpPrefListGeLength':rlIpPrefListGeLength,'rlIpPrefListLeLength':rlIpPrefListLeLength,'rlIpPrefListDescription':rlIpPrefListDescription,'rlIpPrefListHitCount':rlIpPrefListHitCount,'rlIpPrefListRowStatus':rlIpPrefListRowStatus,'rlIpPrefListInfoTable':rlIpPrefListInfoTable,'rlIpPrefListInfoEntry':rlIpPrefListInfoEntry,_L:rlIpPrefListInfoType,_M:rlIpPrefListInfoName,'rlIpPrefListInfoEntriesNumber':rlIpPrefListInfoEntriesNumber,'rlIpPrefListInfoRangeEntries':rlIpPrefListInfoRangeEntries,'rlIpPrefListInfoNextFreeIndex':rlIpPrefListInfoNextFreeIndex})