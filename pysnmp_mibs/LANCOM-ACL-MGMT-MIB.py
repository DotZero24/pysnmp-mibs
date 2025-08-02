_I='aclMgmtTrapReason'
_H='aclMgmtListPriority'
_G='aclMgmtListName'
_F='Unsigned32'
_E='DisplayString'
_D='LANCOM-ACL-MGMT-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
aclMgmtGroup=ModuleIdentity((1,3,6,1,4,1,2356,16,1,62))
if mibBuilder.loadTexts:aclMgmtGroup.setRevisions(('2015-12-11 00:00',))
class AclMgmtServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('allType',0),('telnet',1),('http',2),('https',3),('snmp',4),('ssh',5),('tftp',6),('sntp',7)))
class AclMgmtActionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('permit',0),('deny',1)))
_AclMgmtEnable_Type=TruthValue
_AclMgmtEnable_Object=MibScalar
aclMgmtEnable=_AclMgmtEnable_Object((1,3,6,1,4,1,2356,16,1,62,1),_AclMgmtEnable_Type())
aclMgmtEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:aclMgmtEnable.setStatus(_A)
class _AclMgmtActiveListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AclMgmtActiveListName_Type.__name__=_E
_AclMgmtActiveListName_Object=MibScalar
aclMgmtActiveListName=_AclMgmtActiveListName_Object((1,3,6,1,4,1,2356,16,1,62,2),_AclMgmtActiveListName_Type())
aclMgmtActiveListName.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMgmtActiveListName.setStatus(_A)
_AclMgmtListTable_Object=MibTable
aclMgmtListTable=_AclMgmtListTable_Object((1,3,6,1,4,1,2356,16,1,62,3))
if mibBuilder.loadTexts:aclMgmtListTable.setStatus(_A)
_AclMgmtListEntry_Object=MibTableRow
aclMgmtListEntry=_AclMgmtListEntry_Object((1,3,6,1,4,1,2356,16,1,62,3,1))
aclMgmtListEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:aclMgmtListEntry.setStatus(_A)
class _AclMgmtListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AclMgmtListName_Type.__name__=_E
_AclMgmtListName_Object=MibTableColumn
aclMgmtListName=_AclMgmtListName_Object((1,3,6,1,4,1,2356,16,1,62,3,1,1),_AclMgmtListName_Type())
aclMgmtListName.setMaxAccess(_C)
if mibBuilder.loadTexts:aclMgmtListName.setStatus(_A)
class _AclMgmtListPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_AclMgmtListPriority_Type.__name__=_F
_AclMgmtListPriority_Object=MibTableColumn
aclMgmtListPriority=_AclMgmtListPriority_Object((1,3,6,1,4,1,2356,16,1,62,3,1,2),_AclMgmtListPriority_Type())
aclMgmtListPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:aclMgmtListPriority.setStatus(_A)
_AclMgmtListIfIndex_Type=Unsigned32
_AclMgmtListIfIndex_Object=MibTableColumn
aclMgmtListIfIndex=_AclMgmtListIfIndex_Object((1,3,6,1,4,1,2356,16,1,62,3,1,3),_AclMgmtListIfIndex_Type())
aclMgmtListIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMgmtListIfIndex.setStatus(_A)
_AclMgmtListIpAddr_Type=IpAddress
_AclMgmtListIpAddr_Object=MibTableColumn
aclMgmtListIpAddr=_AclMgmtListIpAddr_Object((1,3,6,1,4,1,2356,16,1,62,3,1,4),_AclMgmtListIpAddr_Type())
aclMgmtListIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMgmtListIpAddr.setStatus(_A)
_AclMgmtListIpNetMask_Type=IpAddress
_AclMgmtListIpNetMask_Object=MibTableColumn
aclMgmtListIpNetMask=_AclMgmtListIpNetMask_Object((1,3,6,1,4,1,2356,16,1,62,3,1,5),_AclMgmtListIpNetMask_Type())
aclMgmtListIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMgmtListIpNetMask.setStatus(_A)
_AclMgmtListService_Type=AclMgmtServiceType
_AclMgmtListService_Object=MibTableColumn
aclMgmtListService=_AclMgmtListService_Object((1,3,6,1,4,1,2356,16,1,62,3,1,6),_AclMgmtListService_Type())
aclMgmtListService.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMgmtListService.setStatus(_A)
_AclMgmtListAction_Type=AclMgmtActionType
_AclMgmtListAction_Object=MibTableColumn
aclMgmtListAction=_AclMgmtListAction_Object((1,3,6,1,4,1,2356,16,1,62,3,1,7),_AclMgmtListAction_Type())
aclMgmtListAction.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMgmtListAction.setStatus(_A)
_AclMgmtListRowStatus_Type=RowStatus
_AclMgmtListRowStatus_Object=MibTableColumn
aclMgmtListRowStatus=_AclMgmtListRowStatus_Object((1,3,6,1,4,1,2356,16,1,62,3,1,8),_AclMgmtListRowStatus_Type())
aclMgmtListRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:aclMgmtListRowStatus.setStatus(_A)
_AclMgmtListVlanId_Type=Unsigned32
_AclMgmtListVlanId_Object=MibTableColumn
aclMgmtListVlanId=_AclMgmtListVlanId_Object((1,3,6,1,4,1,2356,16,1,62,3,1,9),_AclMgmtListVlanId_Type())
aclMgmtListVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMgmtListVlanId.setStatus(_A)
_AclRuleIsConflict_Type=TruthValue
_AclRuleIsConflict_Object=MibTableColumn
aclRuleIsConflict=_AclRuleIsConflict_Object((1,3,6,1,4,1,2356,16,1,62,3,1,10),_AclRuleIsConflict_Type())
aclRuleIsConflict.setMaxAccess(_C)
if mibBuilder.loadTexts:aclRuleIsConflict.setStatus(_A)
_AclMgmtTrapReason_Type=DisplayString
_AclMgmtTrapReason_Object=MibScalar
aclMgmtTrapReason=_AclMgmtTrapReason_Object((1,3,6,1,4,1,2356,16,1,62,5),_AclMgmtTrapReason_Type())
aclMgmtTrapReason.setMaxAccess(_C)
if mibBuilder.loadTexts:aclMgmtTrapReason.setStatus(_A)
aclMgmtTrapInfo=NotificationType((1,3,6,1,4,1,2356,16,1,62,4))
aclMgmtTrapInfo.setObjects((_D,_I))
if mibBuilder.loadTexts:aclMgmtTrapInfo.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'AclMgmtServiceType':AclMgmtServiceType,'AclMgmtActionType':AclMgmtActionType,'aclMgmtGroup':aclMgmtGroup,'aclMgmtEnable':aclMgmtEnable,'aclMgmtActiveListName':aclMgmtActiveListName,'aclMgmtListTable':aclMgmtListTable,'aclMgmtListEntry':aclMgmtListEntry,_G:aclMgmtListName,_H:aclMgmtListPriority,'aclMgmtListIfIndex':aclMgmtListIfIndex,'aclMgmtListIpAddr':aclMgmtListIpAddr,'aclMgmtListIpNetMask':aclMgmtListIpNetMask,'aclMgmtListService':aclMgmtListService,'aclMgmtListAction':aclMgmtListAction,'aclMgmtListRowStatus':aclMgmtListRowStatus,'aclMgmtListVlanId':aclMgmtListVlanId,'aclRuleIsConflict':aclRuleIsConflict,'aclMgmtTrapInfo':aclMgmtTrapInfo,_I:aclMgmtTrapReason})