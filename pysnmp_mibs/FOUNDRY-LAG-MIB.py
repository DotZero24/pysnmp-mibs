_M='testing'
_L='DisplayString'
_K='PhysAddress'
_J='down'
_I='ifIndex'
_H='IF-MIB'
_G='read-write'
_F='fdryLinkAggregationGroupName'
_E='FOUNDRY-LAG-MIB'
_D='read-create'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','snSwitch')
PhysAddress,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB',_K)
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex','InterfaceIndexOrZero',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress',_K,'RowStatus','TextualConvention')
fdryLinkAggregationGroupMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,33))
if mibBuilder.loadTexts:fdryLinkAggregationGroupMIB.setRevisions(('2009-09-30 00:00','2017-08-07 00:00'))
_FdryLinkAggregationGroupTableObjects_ObjectIdentity=ObjectIdentity
fdryLinkAggregationGroupTableObjects=_FdryLinkAggregationGroupTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,33,1))
_FdryLinkAggregationGroupTable_Object=MibTable
fdryLinkAggregationGroupTable=_FdryLinkAggregationGroupTable_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1))
if mibBuilder.loadTexts:fdryLinkAggregationGroupTable.setStatus(_A)
_FdryLinkAggregationGroupEntry_Object=MibTableRow
fdryLinkAggregationGroupEntry=_FdryLinkAggregationGroupEntry_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1))
fdryLinkAggregationGroupEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fdryLinkAggregationGroupEntry.setStatus(_A)
class _FdryLinkAggregationGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FdryLinkAggregationGroupName_Type.__name__=_L
_FdryLinkAggregationGroupName_Object=MibTableColumn
fdryLinkAggregationGroupName=_FdryLinkAggregationGroupName_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,1),_FdryLinkAggregationGroupName_Type())
fdryLinkAggregationGroupName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fdryLinkAggregationGroupName.setStatus(_A)
class _FdryLinkAggregationGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('dynamic',2),('keepalive',3),('auto',4),('spx',5)))
_FdryLinkAggregationGroupType_Type.__name__=_B
_FdryLinkAggregationGroupType_Object=MibTableColumn
fdryLinkAggregationGroupType=_FdryLinkAggregationGroupType_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,2),_FdryLinkAggregationGroupType_Type())
fdryLinkAggregationGroupType.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryLinkAggregationGroupType.setStatus(_A)
class _FdryLinkAggregationGroupAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('deploy',1),('deployPassive',2),('undeploy',3),('undeployForced',4),('other',5)))
_FdryLinkAggregationGroupAdminStatus_Type.__name__=_B
_FdryLinkAggregationGroupAdminStatus_Object=MibTableColumn
fdryLinkAggregationGroupAdminStatus=_FdryLinkAggregationGroupAdminStatus_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,3),_FdryLinkAggregationGroupAdminStatus_Type())
fdryLinkAggregationGroupAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryLinkAggregationGroupAdminStatus.setStatus(_A)
_FdryLinkAggregationGroupIfList_Type=OctetString
_FdryLinkAggregationGroupIfList_Object=MibTableColumn
fdryLinkAggregationGroupIfList=_FdryLinkAggregationGroupIfList_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,4),_FdryLinkAggregationGroupIfList_Type())
fdryLinkAggregationGroupIfList.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryLinkAggregationGroupIfList.setStatus(_A)
_FdryLinkAggregationGroupPrimaryPort_Type=InterfaceIndexOrZero
_FdryLinkAggregationGroupPrimaryPort_Object=MibTableColumn
fdryLinkAggregationGroupPrimaryPort=_FdryLinkAggregationGroupPrimaryPort_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,5),_FdryLinkAggregationGroupPrimaryPort_Type())
fdryLinkAggregationGroupPrimaryPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryLinkAggregationGroupPrimaryPort.setStatus(_A)
class _FdryLinkAggregationGroupTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hashBased',1),('perPacket',2)))
_FdryLinkAggregationGroupTrunkType_Type.__name__=_B
_FdryLinkAggregationGroupTrunkType_Object=MibTableColumn
fdryLinkAggregationGroupTrunkType=_FdryLinkAggregationGroupTrunkType_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,6),_FdryLinkAggregationGroupTrunkType_Type())
fdryLinkAggregationGroupTrunkType.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryLinkAggregationGroupTrunkType.setStatus(_A)
_FdryLinkAggregationGroupTrunkThreshold_Type=Unsigned32
_FdryLinkAggregationGroupTrunkThreshold_Object=MibTableColumn
fdryLinkAggregationGroupTrunkThreshold=_FdryLinkAggregationGroupTrunkThreshold_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,7),_FdryLinkAggregationGroupTrunkThreshold_Type())
fdryLinkAggregationGroupTrunkThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryLinkAggregationGroupTrunkThreshold.setStatus(_A)
class _FdryLinkAggregationGroupLacpTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),('long',2),('short',3)))
_FdryLinkAggregationGroupLacpTimeout_Type.__name__=_B
_FdryLinkAggregationGroupLacpTimeout_Object=MibTableColumn
fdryLinkAggregationGroupLacpTimeout=_FdryLinkAggregationGroupLacpTimeout_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,8),_FdryLinkAggregationGroupLacpTimeout_Type())
fdryLinkAggregationGroupLacpTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpTimeout.setStatus(_A)
_FdryLinkAggregationGroupIfIndex_Type=InterfaceIndexOrZero
_FdryLinkAggregationGroupIfIndex_Object=MibTableColumn
fdryLinkAggregationGroupIfIndex=_FdryLinkAggregationGroupIfIndex_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,9),_FdryLinkAggregationGroupIfIndex_Type())
fdryLinkAggregationGroupIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryLinkAggregationGroupIfIndex.setStatus(_A)
_FdryLinkAggregationGroupPortCount_Type=Unsigned32
_FdryLinkAggregationGroupPortCount_Object=MibTableColumn
fdryLinkAggregationGroupPortCount=_FdryLinkAggregationGroupPortCount_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,10),_FdryLinkAggregationGroupPortCount_Type())
fdryLinkAggregationGroupPortCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryLinkAggregationGroupPortCount.setStatus(_A)
_FdryLinkAggregationGroupRowStatus_Type=RowStatus
_FdryLinkAggregationGroupRowStatus_Object=MibTableColumn
fdryLinkAggregationGroupRowStatus=_FdryLinkAggregationGroupRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,11),_FdryLinkAggregationGroupRowStatus_Type())
fdryLinkAggregationGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fdryLinkAggregationGroupRowStatus.setStatus(_A)
_FdryLinkAggregationGroupId_Type=Unsigned32
_FdryLinkAggregationGroupId_Object=MibTableColumn
fdryLinkAggregationGroupId=_FdryLinkAggregationGroupId_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,12),_FdryLinkAggregationGroupId_Type())
fdryLinkAggregationGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:fdryLinkAggregationGroupId.setStatus(_A)
_FdryLinkAggregationGroupLacpMode_Type=Unsigned32
_FdryLinkAggregationGroupLacpMode_Object=MibTableColumn
fdryLinkAggregationGroupLacpMode=_FdryLinkAggregationGroupLacpMode_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,13),_FdryLinkAggregationGroupLacpMode_Type())
fdryLinkAggregationGroupLacpMode.setMaxAccess(_G)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpMode.setStatus(_A)
_FdryLinkAggregationGroupLagMac_Type=MacAddress
_FdryLinkAggregationGroupLagMac_Object=MibTableColumn
fdryLinkAggregationGroupLagMac=_FdryLinkAggregationGroupLagMac_Object((1,3,6,1,4,1,1991,1,1,3,33,1,1,1,14),_FdryLinkAggregationGroupLagMac_Type())
fdryLinkAggregationGroupLagMac.setMaxAccess(_G)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLagMac.setStatus(_A)
_FdryLinkAggregationGroupPortTableObjects_ObjectIdentity=ObjectIdentity
fdryLinkAggregationGroupPortTableObjects=_FdryLinkAggregationGroupPortTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,33,2))
_FdryLinkAggregationGroupPortTable_Object=MibTable
fdryLinkAggregationGroupPortTable=_FdryLinkAggregationGroupPortTable_Object((1,3,6,1,4,1,1991,1,1,3,33,2,1))
if mibBuilder.loadTexts:fdryLinkAggregationGroupPortTable.setStatus(_A)
_FdryLinkAggregationGroupPortEntry_Object=MibTableRow
fdryLinkAggregationGroupPortEntry=_FdryLinkAggregationGroupPortEntry_Object((1,3,6,1,4,1,1991,1,1,3,33,2,1,1))
fdryLinkAggregationGroupPortEntry.setIndexNames((0,_E,_F),(0,_H,_I))
if mibBuilder.loadTexts:fdryLinkAggregationGroupPortEntry.setStatus(_A)
class _FdryLinkAggregationGroupPortLacpPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FdryLinkAggregationGroupPortLacpPriority_Type.__name__=_B
_FdryLinkAggregationGroupPortLacpPriority_Object=MibTableColumn
fdryLinkAggregationGroupPortLacpPriority=_FdryLinkAggregationGroupPortLacpPriority_Object((1,3,6,1,4,1,1991,1,1,3,33,2,1,1,1),_FdryLinkAggregationGroupPortLacpPriority_Type())
fdryLinkAggregationGroupPortLacpPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:fdryLinkAggregationGroupPortLacpPriority.setStatus(_A)
_FdryLinkAggregationGroupLacpPortTableObjects_ObjectIdentity=ObjectIdentity
fdryLinkAggregationGroupLacpPortTableObjects=_FdryLinkAggregationGroupLacpPortTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,33,3))
_FdryLinkAggregationGroupLacpPortTable_Object=MibTable
fdryLinkAggregationGroupLacpPortTable=_FdryLinkAggregationGroupLacpPortTable_Object((1,3,6,1,4,1,1991,1,1,3,33,3,1))
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpPortTable.setStatus(_A)
_FdryLinkAggregationGroupLacpPortEntry_Object=MibTableRow
fdryLinkAggregationGroupLacpPortEntry=_FdryLinkAggregationGroupLacpPortEntry_Object((1,3,6,1,4,1,1991,1,1,3,33,3,1,1))
fdryLinkAggregationGroupLacpPortEntry.setIndexNames((0,_E,_F),(0,_H,_I))
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpPortEntry.setStatus(_A)
class _FdryLinkAggregationGroupLacpPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_J,2),(_M,3)))
_FdryLinkAggregationGroupLacpPortAdminStatus_Type.__name__=_B
_FdryLinkAggregationGroupLacpPortAdminStatus_Object=MibTableColumn
fdryLinkAggregationGroupLacpPortAdminStatus=_FdryLinkAggregationGroupLacpPortAdminStatus_Object((1,3,6,1,4,1,1991,1,1,3,33,3,1,1,1),_FdryLinkAggregationGroupLacpPortAdminStatus_Type())
fdryLinkAggregationGroupLacpPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpPortAdminStatus.setStatus(_A)
class _FdryLinkAggregationGroupLacpPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_J,2),(_M,3)))
_FdryLinkAggregationGroupLacpPortLinkStatus_Type.__name__=_B
_FdryLinkAggregationGroupLacpPortLinkStatus_Object=MibTableColumn
fdryLinkAggregationGroupLacpPortLinkStatus=_FdryLinkAggregationGroupLacpPortLinkStatus_Object((1,3,6,1,4,1,1991,1,1,3,33,3,1,1,2),_FdryLinkAggregationGroupLacpPortLinkStatus_Type())
fdryLinkAggregationGroupLacpPortLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpPortLinkStatus.setStatus(_A)
class _FdryLinkAggregationGroupLacpPortLacpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operation',1),(_J,2),('blocked',3),('inactive',4),('pexforceup',5)))
_FdryLinkAggregationGroupLacpPortLacpStatus_Type.__name__=_B
_FdryLinkAggregationGroupLacpPortLacpStatus_Object=MibTableColumn
fdryLinkAggregationGroupLacpPortLacpStatus=_FdryLinkAggregationGroupLacpPortLacpStatus_Object((1,3,6,1,4,1,1991,1,1,3,33,3,1,1,3),_FdryLinkAggregationGroupLacpPortLacpStatus_Type())
fdryLinkAggregationGroupLacpPortLacpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpPortLacpStatus.setStatus(_A)
_FdryLinkAggregationGroupLacpPortLacpSysID_Type=PhysAddress
_FdryLinkAggregationGroupLacpPortLacpSysID_Object=MibTableColumn
fdryLinkAggregationGroupLacpPortLacpSysID=_FdryLinkAggregationGroupLacpPortLacpSysID_Object((1,3,6,1,4,1,1991,1,1,3,33,3,1,1,4),_FdryLinkAggregationGroupLacpPortLacpSysID_Type())
fdryLinkAggregationGroupLacpPortLacpSysID.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpPortLacpSysID.setStatus(_A)
_FdryLinkAggregationGroupLacpPortLacpKey_Type=Integer32
_FdryLinkAggregationGroupLacpPortLacpKey_Object=MibTableColumn
fdryLinkAggregationGroupLacpPortLacpKey=_FdryLinkAggregationGroupLacpPortLacpKey_Object((1,3,6,1,4,1,1991,1,1,3,33,3,1,1,5),_FdryLinkAggregationGroupLacpPortLacpKey_Type())
fdryLinkAggregationGroupLacpPortLacpKey.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpPortLacpKey.setStatus(_A)
_FdryLinkAggregationGroupLacpPortLacpRemoteSysID_Type=PhysAddress
_FdryLinkAggregationGroupLacpPortLacpRemoteSysID_Object=MibTableColumn
fdryLinkAggregationGroupLacpPortLacpRemoteSysID=_FdryLinkAggregationGroupLacpPortLacpRemoteSysID_Object((1,3,6,1,4,1,1991,1,1,3,33,3,1,1,6),_FdryLinkAggregationGroupLacpPortLacpRemoteSysID_Type())
fdryLinkAggregationGroupLacpPortLacpRemoteSysID.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpPortLacpRemoteSysID.setStatus(_A)
_FdryLinkAggregationGroupLacpPortLacpRemoteKey_Type=Integer32
_FdryLinkAggregationGroupLacpPortLacpRemoteKey_Object=MibTableColumn
fdryLinkAggregationGroupLacpPortLacpRemoteKey=_FdryLinkAggregationGroupLacpPortLacpRemoteKey_Object((1,3,6,1,4,1,1991,1,1,3,33,3,1,1,7),_FdryLinkAggregationGroupLacpPortLacpRemoteKey_Type())
fdryLinkAggregationGroupLacpPortLacpRemoteKey.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryLinkAggregationGroupLacpPortLacpRemoteKey.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fdryLinkAggregationGroupMIB':fdryLinkAggregationGroupMIB,'fdryLinkAggregationGroupTableObjects':fdryLinkAggregationGroupTableObjects,'fdryLinkAggregationGroupTable':fdryLinkAggregationGroupTable,'fdryLinkAggregationGroupEntry':fdryLinkAggregationGroupEntry,_F:fdryLinkAggregationGroupName,'fdryLinkAggregationGroupType':fdryLinkAggregationGroupType,'fdryLinkAggregationGroupAdminStatus':fdryLinkAggregationGroupAdminStatus,'fdryLinkAggregationGroupIfList':fdryLinkAggregationGroupIfList,'fdryLinkAggregationGroupPrimaryPort':fdryLinkAggregationGroupPrimaryPort,'fdryLinkAggregationGroupTrunkType':fdryLinkAggregationGroupTrunkType,'fdryLinkAggregationGroupTrunkThreshold':fdryLinkAggregationGroupTrunkThreshold,'fdryLinkAggregationGroupLacpTimeout':fdryLinkAggregationGroupLacpTimeout,'fdryLinkAggregationGroupIfIndex':fdryLinkAggregationGroupIfIndex,'fdryLinkAggregationGroupPortCount':fdryLinkAggregationGroupPortCount,'fdryLinkAggregationGroupRowStatus':fdryLinkAggregationGroupRowStatus,'fdryLinkAggregationGroupId':fdryLinkAggregationGroupId,'fdryLinkAggregationGroupLacpMode':fdryLinkAggregationGroupLacpMode,'fdryLinkAggregationGroupLagMac':fdryLinkAggregationGroupLagMac,'fdryLinkAggregationGroupPortTableObjects':fdryLinkAggregationGroupPortTableObjects,'fdryLinkAggregationGroupPortTable':fdryLinkAggregationGroupPortTable,'fdryLinkAggregationGroupPortEntry':fdryLinkAggregationGroupPortEntry,'fdryLinkAggregationGroupPortLacpPriority':fdryLinkAggregationGroupPortLacpPriority,'fdryLinkAggregationGroupLacpPortTableObjects':fdryLinkAggregationGroupLacpPortTableObjects,'fdryLinkAggregationGroupLacpPortTable':fdryLinkAggregationGroupLacpPortTable,'fdryLinkAggregationGroupLacpPortEntry':fdryLinkAggregationGroupLacpPortEntry,'fdryLinkAggregationGroupLacpPortAdminStatus':fdryLinkAggregationGroupLacpPortAdminStatus,'fdryLinkAggregationGroupLacpPortLinkStatus':fdryLinkAggregationGroupLacpPortLinkStatus,'fdryLinkAggregationGroupLacpPortLacpStatus':fdryLinkAggregationGroupLacpPortLacpStatus,'fdryLinkAggregationGroupLacpPortLacpSysID':fdryLinkAggregationGroupLacpPortLacpSysID,'fdryLinkAggregationGroupLacpPortLacpKey':fdryLinkAggregationGroupLacpPortLacpKey,'fdryLinkAggregationGroupLacpPortLacpRemoteSysID':fdryLinkAggregationGroupLacpPortLacpRemoteSysID,'fdryLinkAggregationGroupLacpPortLacpRemoteKey':fdryLinkAggregationGroupLacpPortLacpRemoteKey})