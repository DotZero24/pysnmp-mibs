_g='qtechVlanMIBGroup'
_f='qtechVlanConfigPortMember'
_e='qtechVlanConfigName'
_d='qtechVlanConfigAction'
_c='qtechIfVlanID'
_b='qtechVlanPortAllowedVlanList'
_a='qtechVlanPortNativeVlan'
_Z='qtechVlanPortAccessVlan'
_Y='qtechVlanPortConfigMode'
_X='qtechVlanEntryStatus'
_W='qtechVlanAlias'
_V='qtechVlanPortMemberAction'
_U='qtechVlanApMemberAction'
_T='qtechVlanIfAllowedVlanList'
_S='qtechVlanIfNativeVlan'
_R='qtechVlanIfAccessVlan'
_Q='qtechSystemMaxVID'
_P='qtechVlanCurrentNumber'
_O='qtechVlanMaxNumber'
_N='qtechVlanPortConfigIndex'
_M='read-create'
_L='not-accessible'
_K='qtechVlanIfConfigIfIndex'
_J='DisplayString'
_I='Integer32'
_H='OctetString'
_G='qtechVlanConfigVID'
_F='qtechVlanVID'
_E='read-write'
_D='read-only'
_C='obsolete'
_B='current'
_A='QTECH-VLAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,IfIndex,MemberMap=mibBuilder.importSymbols('QTECH-TC','ConfigStatus','IfIndex','MemberMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
qtechVlanMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,9))
if mibBuilder.loadTexts:qtechVlanMIB.setRevisions(('2002-03-20 00:00',))
class VlanList(TextualConvention,OctetString):status=_B
_QtechVlanMIBObjects_ObjectIdentity=ObjectIdentity
qtechVlanMIBObjects=_QtechVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,9,1))
_QtechVlanMaxNumber_Type=Integer32
_QtechVlanMaxNumber_Object=MibScalar
qtechVlanMaxNumber=_QtechVlanMaxNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,1),_QtechVlanMaxNumber_Type())
qtechVlanMaxNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVlanMaxNumber.setStatus(_B)
_QtechVlanCurrentNumber_Type=Integer32
_QtechVlanCurrentNumber_Object=MibScalar
qtechVlanCurrentNumber=_QtechVlanCurrentNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,2),_QtechVlanCurrentNumber_Type())
qtechVlanCurrentNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVlanCurrentNumber.setStatus(_B)
_QtechSystemMaxVID_Type=Integer32
_QtechSystemMaxVID_Object=MibScalar
qtechSystemMaxVID=_QtechSystemMaxVID_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,3),_QtechSystemMaxVID_Type())
qtechSystemMaxVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechSystemMaxVID.setStatus(_B)
_QtechVlanIfConfigTable_Object=MibTable
qtechVlanIfConfigTable=_QtechVlanIfConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,4))
if mibBuilder.loadTexts:qtechVlanIfConfigTable.setStatus(_C)
_QtechVlanIfConfigEntry_Object=MibTableRow
qtechVlanIfConfigEntry=_QtechVlanIfConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,4,1))
qtechVlanIfConfigEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:qtechVlanIfConfigEntry.setStatus(_C)
_QtechVlanIfConfigIfIndex_Type=IfIndex
_QtechVlanIfConfigIfIndex_Object=MibTableColumn
qtechVlanIfConfigIfIndex=_QtechVlanIfConfigIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,4,1,1),_QtechVlanIfConfigIfIndex_Type())
qtechVlanIfConfigIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:qtechVlanIfConfigIfIndex.setStatus(_C)
_QtechVlanIfAccessVlan_Type=VlanId
_QtechVlanIfAccessVlan_Object=MibTableColumn
qtechVlanIfAccessVlan=_QtechVlanIfAccessVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,4,1,2),_QtechVlanIfAccessVlan_Type())
qtechVlanIfAccessVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVlanIfAccessVlan.setStatus(_C)
_QtechVlanIfNativeVlan_Type=VlanId
_QtechVlanIfNativeVlan_Object=MibTableColumn
qtechVlanIfNativeVlan=_QtechVlanIfNativeVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,4,1,3),_QtechVlanIfNativeVlan_Type())
qtechVlanIfNativeVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVlanIfNativeVlan.setStatus(_C)
class _QtechVlanIfAllowedVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_QtechVlanIfAllowedVlanList_Type.__name__=_H
_QtechVlanIfAllowedVlanList_Object=MibTableColumn
qtechVlanIfAllowedVlanList=_QtechVlanIfAllowedVlanList_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,4,1,4),_QtechVlanIfAllowedVlanList_Type())
qtechVlanIfAllowedVlanList.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVlanIfAllowedVlanList.setStatus(_C)
_QtechVlanTable_Object=MibTable
qtechVlanTable=_QtechVlanTable_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,5))
if mibBuilder.loadTexts:qtechVlanTable.setStatus(_C)
_QtechVlanEntry_Object=MibTableRow
qtechVlanEntry=_QtechVlanEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,5,1))
qtechVlanEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:qtechVlanEntry.setStatus(_C)
_QtechVlanVID_Type=VlanId
_QtechVlanVID_Object=MibTableColumn
qtechVlanVID=_QtechVlanVID_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,5,1,1),_QtechVlanVID_Type())
qtechVlanVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVlanVID.setStatus(_C)
_QtechVlanPortMemberAction_Type=MemberMap
_QtechVlanPortMemberAction_Object=MibTableColumn
qtechVlanPortMemberAction=_QtechVlanPortMemberAction_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,5,1,2),_QtechVlanPortMemberAction_Type())
qtechVlanPortMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVlanPortMemberAction.setStatus(_C)
_QtechVlanApMemberAction_Type=MemberMap
_QtechVlanApMemberAction_Object=MibTableColumn
qtechVlanApMemberAction=_QtechVlanApMemberAction_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,5,1,3),_QtechVlanApMemberAction_Type())
qtechVlanApMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVlanApMemberAction.setStatus(_C)
class _QtechVlanAlias_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechVlanAlias_Type.__name__=_J
_QtechVlanAlias_Object=MibTableColumn
qtechVlanAlias=_QtechVlanAlias_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,5,1,4),_QtechVlanAlias_Type())
qtechVlanAlias.setMaxAccess(_M)
if mibBuilder.loadTexts:qtechVlanAlias.setStatus(_C)
_QtechVlanEntryStatus_Type=ConfigStatus
_QtechVlanEntryStatus_Object=MibTableColumn
qtechVlanEntryStatus=_QtechVlanEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,5,1,5),_QtechVlanEntryStatus_Type())
qtechVlanEntryStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:qtechVlanEntryStatus.setStatus(_C)
_QtechVlanPortConfigTable_Object=MibTable
qtechVlanPortConfigTable=_QtechVlanPortConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,6))
if mibBuilder.loadTexts:qtechVlanPortConfigTable.setStatus(_B)
_QtechVlanPortConfigEntry_Object=MibTableRow
qtechVlanPortConfigEntry=_QtechVlanPortConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,6,1))
qtechVlanPortConfigEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:qtechVlanPortConfigEntry.setStatus(_B)
_QtechVlanPortConfigIndex_Type=IfIndex
_QtechVlanPortConfigIndex_Object=MibTableColumn
qtechVlanPortConfigIndex=_QtechVlanPortConfigIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,6,1,1),_QtechVlanPortConfigIndex_Type())
qtechVlanPortConfigIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:qtechVlanPortConfigIndex.setStatus(_B)
class _QtechVlanPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('access',1),('trunk',2),('dot1q-tunnel',3),('hybrid',4),('other',5),('uplink',6),('host',7),('promiscuous',8)))
_QtechVlanPortConfigMode_Type.__name__=_I
_QtechVlanPortConfigMode_Object=MibTableColumn
qtechVlanPortConfigMode=_QtechVlanPortConfigMode_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,6,1,2),_QtechVlanPortConfigMode_Type())
qtechVlanPortConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVlanPortConfigMode.setStatus(_B)
_QtechVlanPortAccessVlan_Type=VlanId
_QtechVlanPortAccessVlan_Object=MibTableColumn
qtechVlanPortAccessVlan=_QtechVlanPortAccessVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,6,1,3),_QtechVlanPortAccessVlan_Type())
qtechVlanPortAccessVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVlanPortAccessVlan.setStatus(_B)
_QtechVlanPortNativeVlan_Type=VlanId
_QtechVlanPortNativeVlan_Object=MibTableColumn
qtechVlanPortNativeVlan=_QtechVlanPortNativeVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,6,1,4),_QtechVlanPortNativeVlan_Type())
qtechVlanPortNativeVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVlanPortNativeVlan.setStatus(_B)
_QtechVlanPortAllowedVlanList_Type=VlanList
_QtechVlanPortAllowedVlanList_Object=MibTableColumn
qtechVlanPortAllowedVlanList=_QtechVlanPortAllowedVlanList_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,6,1,5),_QtechVlanPortAllowedVlanList_Type())
qtechVlanPortAllowedVlanList.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVlanPortAllowedVlanList.setStatus(_B)
_QtechIfVlanID_Type=Integer32
_QtechIfVlanID_Object=MibTableColumn
qtechIfVlanID=_QtechIfVlanID_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,6,1,6),_QtechIfVlanID_Type())
qtechIfVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIfVlanID.setStatus(_B)
_QtechVlanConfigTable_Object=MibTable
qtechVlanConfigTable=_QtechVlanConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,7))
if mibBuilder.loadTexts:qtechVlanConfigTable.setStatus(_B)
_QtechVlanConfigEntry_Object=MibTableRow
qtechVlanConfigEntry=_QtechVlanConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,7,1))
qtechVlanConfigEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:qtechVlanConfigEntry.setStatus(_B)
_QtechVlanConfigVID_Type=VlanId
_QtechVlanConfigVID_Object=MibTableColumn
qtechVlanConfigVID=_QtechVlanConfigVID_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,7,1,1),_QtechVlanConfigVID_Type())
qtechVlanConfigVID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVlanConfigVID.setStatus(_B)
_QtechVlanConfigAction_Type=Integer32
_QtechVlanConfigAction_Object=MibTableColumn
qtechVlanConfigAction=_QtechVlanConfigAction_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,7,1,2),_QtechVlanConfigAction_Type())
qtechVlanConfigAction.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVlanConfigAction.setStatus(_B)
_QtechVlanConfigName_Type=DisplayString
_QtechVlanConfigName_Object=MibTableColumn
qtechVlanConfigName=_QtechVlanConfigName_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,7,1,3),_QtechVlanConfigName_Type())
qtechVlanConfigName.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechVlanConfigName.setStatus(_B)
_QtechVlanConfigPortMember_Type=PortList
_QtechVlanConfigPortMember_Object=MibTableColumn
qtechVlanConfigPortMember=_QtechVlanConfigPortMember_Object((1,3,6,1,4,1,27514,1,1,10,2,9,1,7,1,4),_QtechVlanConfigPortMember_Type())
qtechVlanConfigPortMember.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechVlanConfigPortMember.setStatus(_B)
_QtechVlanMIBConformance_ObjectIdentity=ObjectIdentity
qtechVlanMIBConformance=_QtechVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,9,2))
_QtechVlanMIBCompliances_ObjectIdentity=ObjectIdentity
qtechVlanMIBCompliances=_QtechVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,9,2,1))
_QtechVlanMIBGroups_ObjectIdentity=ObjectIdentity
qtechVlanMIBGroups=_QtechVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,9,2,2))
qtechVlanMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,9,2,2,1))
qtechVlanMIBGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_F),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_G),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:qtechVlanMIBGroup.setStatus(_B)
qtechVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,9,2,1,1))
qtechVlanMIBCompliance.setObjects((_A,_g))
if mibBuilder.loadTexts:qtechVlanMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VlanList':VlanList,'qtechVlanMIB':qtechVlanMIB,'qtechVlanMIBObjects':qtechVlanMIBObjects,_O:qtechVlanMaxNumber,_P:qtechVlanCurrentNumber,_Q:qtechSystemMaxVID,'qtechVlanIfConfigTable':qtechVlanIfConfigTable,'qtechVlanIfConfigEntry':qtechVlanIfConfigEntry,_K:qtechVlanIfConfigIfIndex,_R:qtechVlanIfAccessVlan,_S:qtechVlanIfNativeVlan,_T:qtechVlanIfAllowedVlanList,'qtechVlanTable':qtechVlanTable,'qtechVlanEntry':qtechVlanEntry,_F:qtechVlanVID,_V:qtechVlanPortMemberAction,_U:qtechVlanApMemberAction,_W:qtechVlanAlias,_X:qtechVlanEntryStatus,'qtechVlanPortConfigTable':qtechVlanPortConfigTable,'qtechVlanPortConfigEntry':qtechVlanPortConfigEntry,_N:qtechVlanPortConfigIndex,_Y:qtechVlanPortConfigMode,_Z:qtechVlanPortAccessVlan,_a:qtechVlanPortNativeVlan,_b:qtechVlanPortAllowedVlanList,_c:qtechIfVlanID,'qtechVlanConfigTable':qtechVlanConfigTable,'qtechVlanConfigEntry':qtechVlanConfigEntry,_G:qtechVlanConfigVID,_d:qtechVlanConfigAction,_e:qtechVlanConfigName,_f:qtechVlanConfigPortMember,'qtechVlanMIBConformance':qtechVlanMIBConformance,'qtechVlanMIBCompliances':qtechVlanMIBCompliances,'qtechVlanMIBCompliance':qtechVlanMIBCompliance,'qtechVlanMIBGroups':qtechVlanMIBGroups,_g:qtechVlanMIBGroup})