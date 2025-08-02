_O='accessible-for-notify'
_N='bVlanPerPortIndex'
_M='bWagVlanStatsIndex'
_L='bWagVlanStatsPortIndex'
_K='bWagVlanIndex'
_J='bWagVlanPortIndex'
_I='bVlanIndex'
_H='bVlanPortIndex'
_G='bVlanId'
_F='Integer32'
_E='bVlanPortId'
_D='not-accessible'
_C='read-only'
_B='BENU-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuWAG,=mibBuilder.importSymbols('BENU-WAG-MIB','benuWAG')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bVLANMIB=ModuleIdentity((1,3,6,1,4,1,39406,2,1,8))
if mibBuilder.loadTexts:bVLANMIB.setRevisions(('2015-05-07 00:00','2015-04-14 00:00','2015-01-06 00:00','2014-11-17 00:00','2014-08-04 00:00','2014-06-24 00:00','2014-05-31 00:00'))
_BVLANNotifObjects_ObjectIdentity=ObjectIdentity
bVLANNotifObjects=_BVLANNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,8,0))
if mibBuilder.loadTexts:bVLANNotifObjects.setStatus(_A)
_BVLANMIBObjects_ObjectIdentity=ObjectIdentity
bVLANMIBObjects=_BVLANMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,8,1))
if mibBuilder.loadTexts:bVLANMIBObjects.setStatus(_A)
_BVlanTable_Object=MibTable
bVlanTable=_BVlanTable_Object((1,3,6,1,4,1,39406,2,1,8,1,1))
if mibBuilder.loadTexts:bVlanTable.setStatus(_A)
_BVlanEntry_Object=MibTableRow
bVlanEntry=_BVlanEntry_Object((1,3,6,1,4,1,39406,2,1,8,1,1,1))
bVlanEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:bVlanEntry.setStatus(_A)
_BVlanPortIndex_Type=Integer32
_BVlanPortIndex_Object=MibTableColumn
bVlanPortIndex=_BVlanPortIndex_Object((1,3,6,1,4,1,39406,2,1,8,1,1,1,1),_BVlanPortIndex_Type())
bVlanPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bVlanPortIndex.setStatus(_A)
_BVlanIndex_Type=Integer32
_BVlanIndex_Object=MibTableColumn
bVlanIndex=_BVlanIndex_Object((1,3,6,1,4,1,39406,2,1,8,1,1,1,2),_BVlanIndex_Type())
bVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bVlanIndex.setStatus(_A)
_BVlanName_Type=DisplayString
_BVlanName_Object=MibTableColumn
bVlanName=_BVlanName_Object((1,3,6,1,4,1,39406,2,1,8,1,1,1,3),_BVlanName_Type())
bVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:bVlanName.setStatus(_A)
_BVlanMTU_Type=Unsigned32
_BVlanMTU_Object=MibTableColumn
bVlanMTU=_BVlanMTU_Object((1,3,6,1,4,1,39406,2,1,8,1,1,1,4),_BVlanMTU_Type())
bVlanMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:bVlanMTU.setStatus(_A)
_BVlanEncapName_Type=DisplayString
_BVlanEncapName_Object=MibTableColumn
bVlanEncapName=_BVlanEncapName_Object((1,3,6,1,4,1,39406,2,1,8,1,1,1,5),_BVlanEncapName_Type())
bVlanEncapName.setMaxAccess(_C)
if mibBuilder.loadTexts:bVlanEncapName.setStatus(_A)
class _BVlanAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_BVlanAdminStatus_Type.__name__=_F
_BVlanAdminStatus_Object=MibTableColumn
bVlanAdminStatus=_BVlanAdminStatus_Object((1,3,6,1,4,1,39406,2,1,8,1,1,1,6),_BVlanAdminStatus_Type())
bVlanAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bVlanAdminStatus.setStatus(_A)
class _BVlanOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_BVlanOperStatus_Type.__name__=_F
_BVlanOperStatus_Object=MibTableColumn
bVlanOperStatus=_BVlanOperStatus_Object((1,3,6,1,4,1,39406,2,1,8,1,1,1,7),_BVlanOperStatus_Type())
bVlanOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bVlanOperStatus.setStatus(_A)
_BWagVlanTable_Object=MibTable
bWagVlanTable=_BWagVlanTable_Object((1,3,6,1,4,1,39406,2,1,8,1,2))
if mibBuilder.loadTexts:bWagVlanTable.setStatus(_A)
_BWagVlanEntry_Object=MibTableRow
bWagVlanEntry=_BWagVlanEntry_Object((1,3,6,1,4,1,39406,2,1,8,1,2,1))
bWagVlanEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:bWagVlanEntry.setStatus(_A)
_BWagVlanPortIndex_Type=Integer32
_BWagVlanPortIndex_Object=MibTableColumn
bWagVlanPortIndex=_BWagVlanPortIndex_Object((1,3,6,1,4,1,39406,2,1,8,1,2,1,1),_BWagVlanPortIndex_Type())
bWagVlanPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bWagVlanPortIndex.setStatus(_A)
_BWagVlanIndex_Type=Integer32
_BWagVlanIndex_Object=MibTableColumn
bWagVlanIndex=_BWagVlanIndex_Object((1,3,6,1,4,1,39406,2,1,8,1,2,1,2),_BWagVlanIndex_Type())
bWagVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bWagVlanIndex.setStatus(_A)
_BWagVlanSubscriberCount_Type=Unsigned32
_BWagVlanSubscriberCount_Object=MibTableColumn
bWagVlanSubscriberCount=_BWagVlanSubscriberCount_Object((1,3,6,1,4,1,39406,2,1,8,1,2,1,3),_BWagVlanSubscriberCount_Type())
bWagVlanSubscriberCount.setMaxAccess(_C)
if mibBuilder.loadTexts:bWagVlanSubscriberCount.setStatus(_A)
_BWagVlanStatsTable_Object=MibTable
bWagVlanStatsTable=_BWagVlanStatsTable_Object((1,3,6,1,4,1,39406,2,1,8,1,3))
if mibBuilder.loadTexts:bWagVlanStatsTable.setStatus(_A)
_BWagVlanStatsEntry_Object=MibTableRow
bWagVlanStatsEntry=_BWagVlanStatsEntry_Object((1,3,6,1,4,1,39406,2,1,8,1,3,1))
bWagVlanStatsEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:bWagVlanStatsEntry.setStatus(_A)
_BWagVlanStatsPortIndex_Type=Integer32
_BWagVlanStatsPortIndex_Object=MibTableColumn
bWagVlanStatsPortIndex=_BWagVlanStatsPortIndex_Object((1,3,6,1,4,1,39406,2,1,8,1,3,1,1),_BWagVlanStatsPortIndex_Type())
bWagVlanStatsPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bWagVlanStatsPortIndex.setStatus(_A)
_BWagVlanStatsIndex_Type=Integer32
_BWagVlanStatsIndex_Object=MibTableColumn
bWagVlanStatsIndex=_BWagVlanStatsIndex_Object((1,3,6,1,4,1,39406,2,1,8,1,3,1,2),_BWagVlanStatsIndex_Type())
bWagVlanStatsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bWagVlanStatsIndex.setStatus(_A)
_BWagVlanTotalPktsRcvd_Type=Counter64
_BWagVlanTotalPktsRcvd_Object=MibTableColumn
bWagVlanTotalPktsRcvd=_BWagVlanTotalPktsRcvd_Object((1,3,6,1,4,1,39406,2,1,8,1,3,1,3),_BWagVlanTotalPktsRcvd_Type())
bWagVlanTotalPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:bWagVlanTotalPktsRcvd.setStatus(_A)
_BWagVlanTotalPktsSent_Type=Counter64
_BWagVlanTotalPktsSent_Object=MibTableColumn
bWagVlanTotalPktsSent=_BWagVlanTotalPktsSent_Object((1,3,6,1,4,1,39406,2,1,8,1,3,1,4),_BWagVlanTotalPktsSent_Type())
bWagVlanTotalPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:bWagVlanTotalPktsSent.setStatus(_A)
_BWagVlanTotalBytesRcvd_Type=Counter64
_BWagVlanTotalBytesRcvd_Object=MibTableColumn
bWagVlanTotalBytesRcvd=_BWagVlanTotalBytesRcvd_Object((1,3,6,1,4,1,39406,2,1,8,1,3,1,5),_BWagVlanTotalBytesRcvd_Type())
bWagVlanTotalBytesRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:bWagVlanTotalBytesRcvd.setStatus(_A)
_BWagVlanTotalBytesSent_Type=Counter64
_BWagVlanTotalBytesSent_Object=MibTableColumn
bWagVlanTotalBytesSent=_BWagVlanTotalBytesSent_Object((1,3,6,1,4,1,39406,2,1,8,1,3,1,6),_BWagVlanTotalBytesSent_Type())
bWagVlanTotalBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:bWagVlanTotalBytesSent.setStatus(_A)
_BVlanPortTable_Object=MibTable
bVlanPortTable=_BVlanPortTable_Object((1,3,6,1,4,1,39406,2,1,8,1,4))
if mibBuilder.loadTexts:bVlanPortTable.setStatus(_A)
_BVlanPortEntry_Object=MibTableRow
bVlanPortEntry=_BVlanPortEntry_Object((1,3,6,1,4,1,39406,2,1,8,1,4,1))
bVlanPortEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:bVlanPortEntry.setStatus(_A)
_BVlanPerPortIndex_Type=Integer32
_BVlanPerPortIndex_Object=MibTableColumn
bVlanPerPortIndex=_BVlanPerPortIndex_Object((1,3,6,1,4,1,39406,2,1,8,1,4,1,1),_BVlanPerPortIndex_Type())
bVlanPerPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bVlanPerPortIndex.setStatus(_A)
_BVlanTotal_Type=Unsigned32
_BVlanTotal_Object=MibTableColumn
bVlanTotal=_BVlanTotal_Object((1,3,6,1,4,1,39406,2,1,8,1,4,1,2),_BVlanTotal_Type())
bVlanTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:bVlanTotal.setStatus(_A)
_BVlanActive_Type=Unsigned32
_BVlanActive_Object=MibTableColumn
bVlanActive=_BVlanActive_Object((1,3,6,1,4,1,39406,2,1,8,1,4,1,3),_BVlanActive_Type())
bVlanActive.setMaxAccess(_C)
if mibBuilder.loadTexts:bVlanActive.setStatus(_A)
class _BVlanCurrentNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_BVlanCurrentNumber_Type.__name__=_F
_BVlanCurrentNumber_Object=MibScalar
bVlanCurrentNumber=_BVlanCurrentNumber_Object((1,3,6,1,4,1,39406,2,1,8,1,5),_BVlanCurrentNumber_Type())
bVlanCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:bVlanCurrentNumber.setStatus(_A)
_BVlanAssocSub_Type=Integer32
_BVlanAssocSub_Object=MibScalar
bVlanAssocSub=_BVlanAssocSub_Object((1,3,6,1,4,1,39406,2,1,8,1,6),_BVlanAssocSub_Type())
bVlanAssocSub.setMaxAccess(_C)
if mibBuilder.loadTexts:bVlanAssocSub.setStatus(_A)
_BVLANNotifVariables_ObjectIdentity=ObjectIdentity
bVLANNotifVariables=_BVLANNotifVariables_ObjectIdentity((1,3,6,1,4,1,39406,2,1,8,2))
if mibBuilder.loadTexts:bVLANNotifVariables.setStatus(_A)
_BVlanPortId_Type=Unsigned32
_BVlanPortId_Object=MibScalar
bVlanPortId=_BVlanPortId_Object((1,3,6,1,4,1,39406,2,1,8,2,1),_BVlanPortId_Type())
bVlanPortId.setMaxAccess(_O)
if mibBuilder.loadTexts:bVlanPortId.setStatus(_A)
_BVlanId_Type=Unsigned32
_BVlanId_Object=MibScalar
bVlanId=_BVlanId_Object((1,3,6,1,4,1,39406,2,1,8,2,2),_BVlanId_Type())
bVlanId.setMaxAccess(_O)
if mibBuilder.loadTexts:bVlanId.setStatus(_A)
bVlanEncapEnable=NotificationType((1,3,6,1,4,1,39406,2,1,8,0,1))
bVlanEncapEnable.setObjects((_B,_E))
if mibBuilder.loadTexts:bVlanEncapEnable.setStatus(_A)
bVlanEncapDisable=NotificationType((1,3,6,1,4,1,39406,2,1,8,0,2))
bVlanEncapDisable.setObjects((_B,_E))
if mibBuilder.loadTexts:bVlanEncapDisable.setStatus(_A)
bVlanCreate=NotificationType((1,3,6,1,4,1,39406,2,1,8,0,3))
bVlanCreate.setObjects(*((_B,_E),(_B,_G)))
if mibBuilder.loadTexts:bVlanCreate.setStatus(_A)
bVlanDelete=NotificationType((1,3,6,1,4,1,39406,2,1,8,0,4))
bVlanDelete.setObjects(*((_B,_E),(_B,_G)))
if mibBuilder.loadTexts:bVlanDelete.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bVLANMIB':bVLANMIB,'bVLANNotifObjects':bVLANNotifObjects,'bVlanEncapEnable':bVlanEncapEnable,'bVlanEncapDisable':bVlanEncapDisable,'bVlanCreate':bVlanCreate,'bVlanDelete':bVlanDelete,'bVLANMIBObjects':bVLANMIBObjects,'bVlanTable':bVlanTable,'bVlanEntry':bVlanEntry,_H:bVlanPortIndex,_I:bVlanIndex,'bVlanName':bVlanName,'bVlanMTU':bVlanMTU,'bVlanEncapName':bVlanEncapName,'bVlanAdminStatus':bVlanAdminStatus,'bVlanOperStatus':bVlanOperStatus,'bWagVlanTable':bWagVlanTable,'bWagVlanEntry':bWagVlanEntry,_J:bWagVlanPortIndex,_K:bWagVlanIndex,'bWagVlanSubscriberCount':bWagVlanSubscriberCount,'bWagVlanStatsTable':bWagVlanStatsTable,'bWagVlanStatsEntry':bWagVlanStatsEntry,_L:bWagVlanStatsPortIndex,_M:bWagVlanStatsIndex,'bWagVlanTotalPktsRcvd':bWagVlanTotalPktsRcvd,'bWagVlanTotalPktsSent':bWagVlanTotalPktsSent,'bWagVlanTotalBytesRcvd':bWagVlanTotalBytesRcvd,'bWagVlanTotalBytesSent':bWagVlanTotalBytesSent,'bVlanPortTable':bVlanPortTable,'bVlanPortEntry':bVlanPortEntry,_N:bVlanPerPortIndex,'bVlanTotal':bVlanTotal,'bVlanActive':bVlanActive,'bVlanCurrentNumber':bVlanCurrentNumber,'bVlanAssocSub':bVlanAssocSub,'bVLANNotifVariables':bVLANNotifVariables,_E:bVlanPortId,_G:bVlanId})