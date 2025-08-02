_e='myVlanMIBGroup'
_d='myVlanConfigPortMember'
_c='myVlanConfigName'
_b='myVlanConfigAction'
_a='myVlanPortAllowedVlanList'
_Z='myVlanPortNativeVlan'
_Y='myVlanPortAccessVlan'
_X='myVlanPortConfigMode'
_W='myVlanEntryStatus'
_V='myVlanAlias'
_U='myVlanPortMemberAction'
_T='myVlanApMemberAction'
_S='myVlanIfAllowedVlanList'
_R='myVlanIfNativeVlan'
_Q='myVlanIfAccessVlan'
_P='mySystemMaxVID'
_O='myVlanCurrentNumber'
_N='myVlanMaxNumber'
_M='myVlanPortConfigIndex'
_L='not-accessible'
_K='myVlanIfConfigIfIndex'
_J='DisplayString'
_I='Integer32'
_H='OctetString'
_G='myVlanConfigVID'
_F='myVlanVID'
_E='read-write'
_D='read-only'
_C='obsolete'
_B='current'
_A='DES7200-VLAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex,MemberMap=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','IfIndex','MemberMap')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myVlanMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,9))
if mibBuilder.loadTexts:myVlanMIB.setRevisions(('2002-03-20 00:00',))
class VlanList(TextualConvention,OctetString):status=_B
_MyVlanMIBObjects_ObjectIdentity=ObjectIdentity
myVlanMIBObjects=_MyVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,9,1))
_MyVlanMaxNumber_Type=Integer32
_MyVlanMaxNumber_Object=MibScalar
myVlanMaxNumber=_MyVlanMaxNumber_Object((1,3,6,1,4,1,171,10,97,2,9,1,1),_MyVlanMaxNumber_Type())
myVlanMaxNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanMaxNumber.setStatus(_B)
_MyVlanCurrentNumber_Type=Integer32
_MyVlanCurrentNumber_Object=MibScalar
myVlanCurrentNumber=_MyVlanCurrentNumber_Object((1,3,6,1,4,1,171,10,97,2,9,1,2),_MyVlanCurrentNumber_Type())
myVlanCurrentNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanCurrentNumber.setStatus(_B)
_MySystemMaxVID_Type=Integer32
_MySystemMaxVID_Object=MibScalar
mySystemMaxVID=_MySystemMaxVID_Object((1,3,6,1,4,1,171,10,97,2,9,1,3),_MySystemMaxVID_Type())
mySystemMaxVID.setMaxAccess(_D)
if mibBuilder.loadTexts:mySystemMaxVID.setStatus(_B)
_MyVlanIfConfigTable_Object=MibTable
myVlanIfConfigTable=_MyVlanIfConfigTable_Object((1,3,6,1,4,1,171,10,97,2,9,1,4))
if mibBuilder.loadTexts:myVlanIfConfigTable.setStatus(_C)
_MyVlanIfConfigEntry_Object=MibTableRow
myVlanIfConfigEntry=_MyVlanIfConfigEntry_Object((1,3,6,1,4,1,171,10,97,2,9,1,4,1))
myVlanIfConfigEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:myVlanIfConfigEntry.setStatus(_C)
_MyVlanIfConfigIfIndex_Type=IfIndex
_MyVlanIfConfigIfIndex_Object=MibTableColumn
myVlanIfConfigIfIndex=_MyVlanIfConfigIfIndex_Object((1,3,6,1,4,1,171,10,97,2,9,1,4,1,1),_MyVlanIfConfigIfIndex_Type())
myVlanIfConfigIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:myVlanIfConfigIfIndex.setStatus(_C)
_MyVlanIfAccessVlan_Type=VlanId
_MyVlanIfAccessVlan_Object=MibTableColumn
myVlanIfAccessVlan=_MyVlanIfAccessVlan_Object((1,3,6,1,4,1,171,10,97,2,9,1,4,1,2),_MyVlanIfAccessVlan_Type())
myVlanIfAccessVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:myVlanIfAccessVlan.setStatus(_C)
_MyVlanIfNativeVlan_Type=VlanId
_MyVlanIfNativeVlan_Object=MibTableColumn
myVlanIfNativeVlan=_MyVlanIfNativeVlan_Object((1,3,6,1,4,1,171,10,97,2,9,1,4,1,3),_MyVlanIfNativeVlan_Type())
myVlanIfNativeVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:myVlanIfNativeVlan.setStatus(_C)
class _MyVlanIfAllowedVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_MyVlanIfAllowedVlanList_Type.__name__=_H
_MyVlanIfAllowedVlanList_Object=MibTableColumn
myVlanIfAllowedVlanList=_MyVlanIfAllowedVlanList_Object((1,3,6,1,4,1,171,10,97,2,9,1,4,1,4),_MyVlanIfAllowedVlanList_Type())
myVlanIfAllowedVlanList.setMaxAccess(_E)
if mibBuilder.loadTexts:myVlanIfAllowedVlanList.setStatus(_C)
_MyVlanTable_Object=MibTable
myVlanTable=_MyVlanTable_Object((1,3,6,1,4,1,171,10,97,2,9,1,5))
if mibBuilder.loadTexts:myVlanTable.setStatus(_C)
_MyVlanEntry_Object=MibTableRow
myVlanEntry=_MyVlanEntry_Object((1,3,6,1,4,1,171,10,97,2,9,1,5,1))
myVlanEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:myVlanEntry.setStatus(_C)
_MyVlanVID_Type=VlanId
_MyVlanVID_Object=MibTableColumn
myVlanVID=_MyVlanVID_Object((1,3,6,1,4,1,171,10,97,2,9,1,5,1,1),_MyVlanVID_Type())
myVlanVID.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanVID.setStatus(_C)
_MyVlanPortMemberAction_Type=MemberMap
_MyVlanPortMemberAction_Object=MibTableColumn
myVlanPortMemberAction=_MyVlanPortMemberAction_Object((1,3,6,1,4,1,171,10,97,2,9,1,5,1,2),_MyVlanPortMemberAction_Type())
myVlanPortMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanPortMemberAction.setStatus(_C)
_MyVlanApMemberAction_Type=MemberMap
_MyVlanApMemberAction_Object=MibTableColumn
myVlanApMemberAction=_MyVlanApMemberAction_Object((1,3,6,1,4,1,171,10,97,2,9,1,5,1,3),_MyVlanApMemberAction_Type())
myVlanApMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanApMemberAction.setStatus(_C)
class _MyVlanAlias_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyVlanAlias_Type.__name__=_J
_MyVlanAlias_Object=MibTableColumn
myVlanAlias=_MyVlanAlias_Object((1,3,6,1,4,1,171,10,97,2,9,1,5,1,4),_MyVlanAlias_Type())
myVlanAlias.setMaxAccess(_E)
if mibBuilder.loadTexts:myVlanAlias.setStatus(_C)
_MyVlanEntryStatus_Type=ConfigStatus
_MyVlanEntryStatus_Object=MibTableColumn
myVlanEntryStatus=_MyVlanEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,9,1,5,1,5),_MyVlanEntryStatus_Type())
myVlanEntryStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:myVlanEntryStatus.setStatus(_C)
_MyVlanPortConfigTable_Object=MibTable
myVlanPortConfigTable=_MyVlanPortConfigTable_Object((1,3,6,1,4,1,171,10,97,2,9,1,6))
if mibBuilder.loadTexts:myVlanPortConfigTable.setStatus(_B)
_MyVlanPortConfigEntry_Object=MibTableRow
myVlanPortConfigEntry=_MyVlanPortConfigEntry_Object((1,3,6,1,4,1,171,10,97,2,9,1,6,1))
myVlanPortConfigEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:myVlanPortConfigEntry.setStatus(_B)
_MyVlanPortConfigIndex_Type=IfIndex
_MyVlanPortConfigIndex_Object=MibTableColumn
myVlanPortConfigIndex=_MyVlanPortConfigIndex_Object((1,3,6,1,4,1,171,10,97,2,9,1,6,1,1),_MyVlanPortConfigIndex_Type())
myVlanPortConfigIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:myVlanPortConfigIndex.setStatus(_B)
class _MyVlanPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('access',1),('trunk',2),('dot1q-tunnel',3),('hybrid',4),('other',5),('uplink',6),('host',7),('promiscuous',8)))
_MyVlanPortConfigMode_Type.__name__=_I
_MyVlanPortConfigMode_Object=MibTableColumn
myVlanPortConfigMode=_MyVlanPortConfigMode_Object((1,3,6,1,4,1,171,10,97,2,9,1,6,1,2),_MyVlanPortConfigMode_Type())
myVlanPortConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanPortConfigMode.setStatus(_B)
_MyVlanPortAccessVlan_Type=VlanId
_MyVlanPortAccessVlan_Object=MibTableColumn
myVlanPortAccessVlan=_MyVlanPortAccessVlan_Object((1,3,6,1,4,1,171,10,97,2,9,1,6,1,3),_MyVlanPortAccessVlan_Type())
myVlanPortAccessVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:myVlanPortAccessVlan.setStatus(_B)
_MyVlanPortNativeVlan_Type=VlanId
_MyVlanPortNativeVlan_Object=MibTableColumn
myVlanPortNativeVlan=_MyVlanPortNativeVlan_Object((1,3,6,1,4,1,171,10,97,2,9,1,6,1,4),_MyVlanPortNativeVlan_Type())
myVlanPortNativeVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:myVlanPortNativeVlan.setStatus(_B)
_MyVlanPortAllowedVlanList_Type=VlanList
_MyVlanPortAllowedVlanList_Object=MibTableColumn
myVlanPortAllowedVlanList=_MyVlanPortAllowedVlanList_Object((1,3,6,1,4,1,171,10,97,2,9,1,6,1,5),_MyVlanPortAllowedVlanList_Type())
myVlanPortAllowedVlanList.setMaxAccess(_E)
if mibBuilder.loadTexts:myVlanPortAllowedVlanList.setStatus(_B)
_MyVlanConfigTable_Object=MibTable
myVlanConfigTable=_MyVlanConfigTable_Object((1,3,6,1,4,1,171,10,97,2,9,1,7))
if mibBuilder.loadTexts:myVlanConfigTable.setStatus(_B)
_MyVlanConfigEntry_Object=MibTableRow
myVlanConfigEntry=_MyVlanConfigEntry_Object((1,3,6,1,4,1,171,10,97,2,9,1,7,1))
myVlanConfigEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:myVlanConfigEntry.setStatus(_B)
_MyVlanConfigVID_Type=VlanId
_MyVlanConfigVID_Object=MibTableColumn
myVlanConfigVID=_MyVlanConfigVID_Object((1,3,6,1,4,1,171,10,97,2,9,1,7,1,1),_MyVlanConfigVID_Type())
myVlanConfigVID.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanConfigVID.setStatus(_B)
_MyVlanConfigAction_Type=Integer32
_MyVlanConfigAction_Object=MibTableColumn
myVlanConfigAction=_MyVlanConfigAction_Object((1,3,6,1,4,1,171,10,97,2,9,1,7,1,2),_MyVlanConfigAction_Type())
myVlanConfigAction.setMaxAccess(_E)
if mibBuilder.loadTexts:myVlanConfigAction.setStatus(_B)
_MyVlanConfigName_Type=DisplayString
_MyVlanConfigName_Object=MibTableColumn
myVlanConfigName=_MyVlanConfigName_Object((1,3,6,1,4,1,171,10,97,2,9,1,7,1,3),_MyVlanConfigName_Type())
myVlanConfigName.setMaxAccess(_E)
if mibBuilder.loadTexts:myVlanConfigName.setStatus(_B)
_MyVlanConfigPortMember_Type=PortList
_MyVlanConfigPortMember_Object=MibTableColumn
myVlanConfigPortMember=_MyVlanConfigPortMember_Object((1,3,6,1,4,1,171,10,97,2,9,1,7,1,4),_MyVlanConfigPortMember_Type())
myVlanConfigPortMember.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanConfigPortMember.setStatus(_B)
_MyVlanMIBConformance_ObjectIdentity=ObjectIdentity
myVlanMIBConformance=_MyVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,9,2))
_MyVlanMIBCompliances_ObjectIdentity=ObjectIdentity
myVlanMIBCompliances=_MyVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,9,2,1))
_MyVlanMIBGroups_ObjectIdentity=ObjectIdentity
myVlanMIBGroups=_MyVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,9,2,2))
myVlanMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,9,2,2,1))
myVlanMIBGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_F),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_G),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:myVlanMIBGroup.setStatus(_B)
myVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,9,2,1,1))
myVlanMIBCompliance.setObjects((_A,_e))
if mibBuilder.loadTexts:myVlanMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VlanList':VlanList,'myVlanMIB':myVlanMIB,'myVlanMIBObjects':myVlanMIBObjects,_N:myVlanMaxNumber,_O:myVlanCurrentNumber,_P:mySystemMaxVID,'myVlanIfConfigTable':myVlanIfConfigTable,'myVlanIfConfigEntry':myVlanIfConfigEntry,_K:myVlanIfConfigIfIndex,_Q:myVlanIfAccessVlan,_R:myVlanIfNativeVlan,_S:myVlanIfAllowedVlanList,'myVlanTable':myVlanTable,'myVlanEntry':myVlanEntry,_F:myVlanVID,_U:myVlanPortMemberAction,_T:myVlanApMemberAction,_V:myVlanAlias,_W:myVlanEntryStatus,'myVlanPortConfigTable':myVlanPortConfigTable,'myVlanPortConfigEntry':myVlanPortConfigEntry,_M:myVlanPortConfigIndex,_X:myVlanPortConfigMode,_Y:myVlanPortAccessVlan,_Z:myVlanPortNativeVlan,_a:myVlanPortAllowedVlanList,'myVlanConfigTable':myVlanConfigTable,'myVlanConfigEntry':myVlanConfigEntry,_G:myVlanConfigVID,_b:myVlanConfigAction,_c:myVlanConfigName,_d:myVlanConfigPortMember,'myVlanMIBConformance':myVlanMIBConformance,'myVlanMIBCompliances':myVlanMIBCompliances,'myVlanMIBCompliance':myVlanMIBCompliance,'myVlanMIBGroups':myVlanMIBGroups,_e:myVlanMIBGroup})