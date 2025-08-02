_N='mellanoxXstpPortState'
_M='mellanoxXstpVlanId'
_L='disabled'
_K='not-accessible'
_J='mellanoxXstpPortMstId'
_I='accessible-for-notify'
_H='mellanoxXstpPortNum'
_G='mellanoxXstpId'
_F='OctetString'
_E='Integer32'
_D='Unsigned32'
_C='MELLANOX-XSTP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
mellanoxXstp,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxXstp')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxXstpMib=ModuleIdentity((1,3,6,1,4,1,33049,13,1))
if mibBuilder.loadTexts:mellanoxXstpMib.setRevisions(('2017-07-26 00:00',))
_MellanoxXstpNotifications_ObjectIdentity=ObjectIdentity
mellanoxXstpNotifications=_MellanoxXstpNotifications_ObjectIdentity((1,3,6,1,4,1,33049,13,1,1))
_MellanoxXstpObjects_ObjectIdentity=ObjectIdentity
mellanoxXstpObjects=_MellanoxXstpObjects_ObjectIdentity((1,3,6,1,4,1,33049,13,1,2))
_MellanoxXstpTable_Object=MibTable
mellanoxXstpTable=_MellanoxXstpTable_Object((1,3,6,1,4,1,33049,13,1,2,1))
if mibBuilder.loadTexts:mellanoxXstpTable.setStatus(_A)
_MellanoxXstpEntry_Object=MibTableRow
mellanoxXstpEntry=_MellanoxXstpEntry_Object((1,3,6,1,4,1,33049,13,1,2,1,1))
mellanoxXstpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:mellanoxXstpEntry.setStatus(_A)
class _MellanoxXstpId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_MellanoxXstpId_Type.__name__=_D
_MellanoxXstpId_Object=MibTableColumn
mellanoxXstpId=_MellanoxXstpId_Object((1,3,6,1,4,1,33049,13,1,2,1,1,1),_MellanoxXstpId_Type())
mellanoxXstpId.setMaxAccess(_I)
if mibBuilder.loadTexts:mellanoxXstpId.setStatus(_A)
_MellanoxXstpBridgeId_Type=BridgeId
_MellanoxXstpBridgeId_Object=MibTableColumn
mellanoxXstpBridgeId=_MellanoxXstpBridgeId_Object((1,3,6,1,4,1,33049,13,1,2,1,1,2),_MellanoxXstpBridgeId_Type())
mellanoxXstpBridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpBridgeId.setStatus(_A)
_MellanoxXstpDesignatedRoot_Type=BridgeId
_MellanoxXstpDesignatedRoot_Object=MibTableColumn
mellanoxXstpDesignatedRoot=_MellanoxXstpDesignatedRoot_Object((1,3,6,1,4,1,33049,13,1,2,1,1,3),_MellanoxXstpDesignatedRoot_Type())
mellanoxXstpDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpDesignatedRoot.setStatus(_A)
_MellanoxXstpRootPathCost_Type=Integer32
_MellanoxXstpRootPathCost_Object=MibTableColumn
mellanoxXstpRootPathCost=_MellanoxXstpRootPathCost_Object((1,3,6,1,4,1,33049,13,1,2,1,1,4),_MellanoxXstpRootPathCost_Type())
mellanoxXstpRootPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpRootPathCost.setStatus(_A)
class _MellanoxXstpRootPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MellanoxXstpRootPort_Type.__name__=_D
_MellanoxXstpRootPort_Object=MibTableColumn
mellanoxXstpRootPort=_MellanoxXstpRootPort_Object((1,3,6,1,4,1,33049,13,1,2,1,1,5),_MellanoxXstpRootPort_Type())
mellanoxXstpRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpRootPort.setStatus(_A)
class _MellanoxXstpBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_MellanoxXstpBridgePriority_Type.__name__=_E
_MellanoxXstpBridgePriority_Object=MibTableColumn
mellanoxXstpBridgePriority=_MellanoxXstpBridgePriority_Object((1,3,6,1,4,1,33049,13,1,2,1,1,6),_MellanoxXstpBridgePriority_Type())
mellanoxXstpBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpBridgePriority.setStatus(_A)
class _MellanoxXstpVids0_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_MellanoxXstpVids0_Type.__name__=_F
_MellanoxXstpVids0_Object=MibTableColumn
mellanoxXstpVids0=_MellanoxXstpVids0_Object((1,3,6,1,4,1,33049,13,1,2,1,1,7),_MellanoxXstpVids0_Type())
mellanoxXstpVids0.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpVids0.setStatus(_A)
class _MellanoxXstpVids1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_MellanoxXstpVids1_Type.__name__=_F
_MellanoxXstpVids1_Object=MibTableColumn
mellanoxXstpVids1=_MellanoxXstpVids1_Object((1,3,6,1,4,1,33049,13,1,2,1,1,8),_MellanoxXstpVids1_Type())
mellanoxXstpVids1.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpVids1.setStatus(_A)
class _MellanoxXstpVids2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_MellanoxXstpVids2_Type.__name__=_F
_MellanoxXstpVids2_Object=MibTableColumn
mellanoxXstpVids2=_MellanoxXstpVids2_Object((1,3,6,1,4,1,33049,13,1,2,1,1,9),_MellanoxXstpVids2_Type())
mellanoxXstpVids2.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpVids2.setStatus(_A)
class _MellanoxXstpVids3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_MellanoxXstpVids3_Type.__name__=_F
_MellanoxXstpVids3_Object=MibTableColumn
mellanoxXstpVids3=_MellanoxXstpVids3_Object((1,3,6,1,4,1,33049,13,1,2,1,1,10),_MellanoxXstpVids3_Type())
mellanoxXstpVids3.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpVids3.setStatus(_A)
_MellanoxXstpPortTable_Object=MibTable
mellanoxXstpPortTable=_MellanoxXstpPortTable_Object((1,3,6,1,4,1,33049,13,1,2,2))
if mibBuilder.loadTexts:mellanoxXstpPortTable.setStatus(_A)
_MellanoxXstpPortEntry_Object=MibTableRow
mellanoxXstpPortEntry=_MellanoxXstpPortEntry_Object((1,3,6,1,4,1,33049,13,1,2,2,1))
mellanoxXstpPortEntry.setIndexNames((0,_C,_J),(0,_C,_H))
if mibBuilder.loadTexts:mellanoxXstpPortEntry.setStatus(_A)
class _MellanoxXstpPortMstId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_MellanoxXstpPortMstId_Type.__name__=_D
_MellanoxXstpPortMstId_Object=MibTableColumn
mellanoxXstpPortMstId=_MellanoxXstpPortMstId_Object((1,3,6,1,4,1,33049,13,1,2,2,1,1),_MellanoxXstpPortMstId_Type())
mellanoxXstpPortMstId.setMaxAccess(_K)
if mibBuilder.loadTexts:mellanoxXstpPortMstId.setStatus(_A)
class _MellanoxXstpPortNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MellanoxXstpPortNum_Type.__name__=_D
_MellanoxXstpPortNum_Object=MibTableColumn
mellanoxXstpPortNum=_MellanoxXstpPortNum_Object((1,3,6,1,4,1,33049,13,1,2,2,1,2),_MellanoxXstpPortNum_Type())
mellanoxXstpPortNum.setMaxAccess(_I)
if mibBuilder.loadTexts:mellanoxXstpPortNum.setStatus(_A)
class _MellanoxXstpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),('listening',2),('learning',3),('forwarding',4),('blocking',5)))
_MellanoxXstpPortState_Type.__name__=_E
_MellanoxXstpPortState_Object=MibTableColumn
mellanoxXstpPortState=_MellanoxXstpPortState_Object((1,3,6,1,4,1,33049,13,1,2,2,1,3),_MellanoxXstpPortState_Type())
mellanoxXstpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpPortState.setStatus(_A)
class _MellanoxXstpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_MellanoxXstpPortPriority_Type.__name__=_E
_MellanoxXstpPortPriority_Object=MibTableColumn
mellanoxXstpPortPriority=_MellanoxXstpPortPriority_Object((1,3,6,1,4,1,33049,13,1,2,2,1,4),_MellanoxXstpPortPriority_Type())
mellanoxXstpPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpPortPriority.setStatus(_A)
class _MellanoxXstpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_MellanoxXstpPortPathCost_Type.__name__=_E
_MellanoxXstpPortPathCost_Object=MibTableColumn
mellanoxXstpPortPathCost=_MellanoxXstpPortPathCost_Object((1,3,6,1,4,1,33049,13,1,2,2,1,5),_MellanoxXstpPortPathCost_Type())
mellanoxXstpPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpPortPathCost.setStatus(_A)
class _MellanoxXstpPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('root',1),('alternate',2),('designated',3),('backup',4),(_L,5)))
_MellanoxXstpPortRole_Type.__name__=_E
_MellanoxXstpPortRole_Object=MibTableColumn
mellanoxXstpPortRole=_MellanoxXstpPortRole_Object((1,3,6,1,4,1,33049,13,1,2,2,1,6),_MellanoxXstpPortRole_Type())
mellanoxXstpPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpPortRole.setStatus(_A)
_MellanoxXstpVlanTable_Object=MibTable
mellanoxXstpVlanTable=_MellanoxXstpVlanTable_Object((1,3,6,1,4,1,33049,13,1,2,3))
if mibBuilder.loadTexts:mellanoxXstpVlanTable.setStatus(_A)
_MellanoxXstpVlanEntry_Object=MibTableRow
mellanoxXstpVlanEntry=_MellanoxXstpVlanEntry_Object((1,3,6,1,4,1,33049,13,1,2,3,1))
mellanoxXstpVlanEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:mellanoxXstpVlanEntry.setStatus(_A)
class _MellanoxXstpVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_MellanoxXstpVlanId_Type.__name__=_D
_MellanoxXstpVlanId_Object=MibTableColumn
mellanoxXstpVlanId=_MellanoxXstpVlanId_Object((1,3,6,1,4,1,33049,13,1,2,3,1,1),_MellanoxXstpVlanId_Type())
mellanoxXstpVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:mellanoxXstpVlanId.setStatus(_A)
class _MellanoxXstpVlanMstId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_MellanoxXstpVlanMstId_Type.__name__=_D
_MellanoxXstpVlanMstId_Object=MibTableColumn
mellanoxXstpVlanMstId=_MellanoxXstpVlanMstId_Object((1,3,6,1,4,1,33049,13,1,2,3,1,2),_MellanoxXstpVlanMstId_Type())
mellanoxXstpVlanMstId.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxXstpVlanMstId.setStatus(_A)
mellanoxXstpRootBridgeChange=NotificationType((1,3,6,1,4,1,33049,13,1,1,1))
mellanoxXstpRootBridgeChange.setObjects((_C,_G))
if mibBuilder.loadTexts:mellanoxXstpRootBridgeChange.setStatus(_A)
mellanoxXstpRootPortChange=NotificationType((1,3,6,1,4,1,33049,13,1,1,2))
mellanoxXstpRootPortChange.setObjects(*((_C,_G),(_C,_H)))
if mibBuilder.loadTexts:mellanoxXstpRootPortChange.setStatus(_A)
mellanoxXstpTopologyChange=NotificationType((1,3,6,1,4,1,33049,13,1,1,3))
mellanoxXstpTopologyChange.setObjects(*((_C,_G),(_C,_H),(_C,_N)))
if mibBuilder.loadTexts:mellanoxXstpTopologyChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mellanoxXstpMib':mellanoxXstpMib,'mellanoxXstpNotifications':mellanoxXstpNotifications,'mellanoxXstpRootBridgeChange':mellanoxXstpRootBridgeChange,'mellanoxXstpRootPortChange':mellanoxXstpRootPortChange,'mellanoxXstpTopologyChange':mellanoxXstpTopologyChange,'mellanoxXstpObjects':mellanoxXstpObjects,'mellanoxXstpTable':mellanoxXstpTable,'mellanoxXstpEntry':mellanoxXstpEntry,_G:mellanoxXstpId,'mellanoxXstpBridgeId':mellanoxXstpBridgeId,'mellanoxXstpDesignatedRoot':mellanoxXstpDesignatedRoot,'mellanoxXstpRootPathCost':mellanoxXstpRootPathCost,'mellanoxXstpRootPort':mellanoxXstpRootPort,'mellanoxXstpBridgePriority':mellanoxXstpBridgePriority,'mellanoxXstpVids0':mellanoxXstpVids0,'mellanoxXstpVids1':mellanoxXstpVids1,'mellanoxXstpVids2':mellanoxXstpVids2,'mellanoxXstpVids3':mellanoxXstpVids3,'mellanoxXstpPortTable':mellanoxXstpPortTable,'mellanoxXstpPortEntry':mellanoxXstpPortEntry,_J:mellanoxXstpPortMstId,_H:mellanoxXstpPortNum,_N:mellanoxXstpPortState,'mellanoxXstpPortPriority':mellanoxXstpPortPriority,'mellanoxXstpPortPathCost':mellanoxXstpPortPathCost,'mellanoxXstpPortRole':mellanoxXstpPortRole,'mellanoxXstpVlanTable':mellanoxXstpVlanTable,'mellanoxXstpVlanEntry':mellanoxXstpVlanEntry,_M:mellanoxXstpVlanId,'mellanoxXstpVlanMstId':mellanoxXstpVlanMstId})