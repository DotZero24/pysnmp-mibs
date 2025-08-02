_g='fsVlanMIBGroup'
_f='fsVlanConfigPortMember'
_e='fsVlanConfigName'
_d='fsVlanConfigAction'
_c='fsIfVlanID'
_b='fsVlanPortAllowedVlanList'
_a='fsVlanPortNativeVlan'
_Z='fsVlanPortAccessVlan'
_Y='fsVlanPortConfigMode'
_X='fsVlanEntryStatus'
_W='fsVlanAlias'
_V='fsVlanPortMemberAction'
_U='fsVlanApMemberAction'
_T='fsVlanIfAllowedVlanList'
_S='fsVlanIfNativeVlan'
_R='fsVlanIfAccessVlan'
_Q='fsSystemMaxVID'
_P='fsVlanCurrentNumber'
_O='fsVlanMaxNumber'
_N='fsVlanPortConfigIndex'
_M='read-create'
_L='not-accessible'
_K='fsVlanIfConfigIfIndex'
_J='DisplayString'
_I='Integer32'
_H='OctetString'
_G='fsVlanConfigVID'
_F='fsVlanVID'
_E='read-write'
_D='read-only'
_C='obsolete'
_B='current'
_A='FS-VLAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex,MemberMap=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex','MemberMap')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
fsVlanMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,9))
if mibBuilder.loadTexts:fsVlanMIB.setRevisions(('2002-03-20 00:00',))
class VlanList(TextualConvention,OctetString):status=_B
_FsVlanMIBObjects_ObjectIdentity=ObjectIdentity
fsVlanMIBObjects=_FsVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,9,1))
_FsVlanMaxNumber_Type=Integer32
_FsVlanMaxNumber_Object=MibScalar
fsVlanMaxNumber=_FsVlanMaxNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,1),_FsVlanMaxNumber_Type())
fsVlanMaxNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVlanMaxNumber.setStatus(_B)
_FsVlanCurrentNumber_Type=Integer32
_FsVlanCurrentNumber_Object=MibScalar
fsVlanCurrentNumber=_FsVlanCurrentNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,2),_FsVlanCurrentNumber_Type())
fsVlanCurrentNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVlanCurrentNumber.setStatus(_B)
_FsSystemMaxVID_Type=Integer32
_FsSystemMaxVID_Object=MibScalar
fsSystemMaxVID=_FsSystemMaxVID_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,3),_FsSystemMaxVID_Type())
fsSystemMaxVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSystemMaxVID.setStatus(_B)
_FsVlanIfConfigTable_Object=MibTable
fsVlanIfConfigTable=_FsVlanIfConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,4))
if mibBuilder.loadTexts:fsVlanIfConfigTable.setStatus(_C)
_FsVlanIfConfigEntry_Object=MibTableRow
fsVlanIfConfigEntry=_FsVlanIfConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,4,1))
fsVlanIfConfigEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:fsVlanIfConfigEntry.setStatus(_C)
_FsVlanIfConfigIfIndex_Type=IfIndex
_FsVlanIfConfigIfIndex_Object=MibTableColumn
fsVlanIfConfigIfIndex=_FsVlanIfConfigIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,4,1,1),_FsVlanIfConfigIfIndex_Type())
fsVlanIfConfigIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:fsVlanIfConfigIfIndex.setStatus(_C)
_FsVlanIfAccessVlan_Type=VlanId
_FsVlanIfAccessVlan_Object=MibTableColumn
fsVlanIfAccessVlan=_FsVlanIfAccessVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,4,1,2),_FsVlanIfAccessVlan_Type())
fsVlanIfAccessVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVlanIfAccessVlan.setStatus(_C)
_FsVlanIfNativeVlan_Type=VlanId
_FsVlanIfNativeVlan_Object=MibTableColumn
fsVlanIfNativeVlan=_FsVlanIfNativeVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,4,1,3),_FsVlanIfNativeVlan_Type())
fsVlanIfNativeVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVlanIfNativeVlan.setStatus(_C)
class _FsVlanIfAllowedVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_FsVlanIfAllowedVlanList_Type.__name__=_H
_FsVlanIfAllowedVlanList_Object=MibTableColumn
fsVlanIfAllowedVlanList=_FsVlanIfAllowedVlanList_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,4,1,4),_FsVlanIfAllowedVlanList_Type())
fsVlanIfAllowedVlanList.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVlanIfAllowedVlanList.setStatus(_C)
_FsVlanTable_Object=MibTable
fsVlanTable=_FsVlanTable_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,5))
if mibBuilder.loadTexts:fsVlanTable.setStatus(_C)
_FsVlanEntry_Object=MibTableRow
fsVlanEntry=_FsVlanEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,5,1))
fsVlanEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:fsVlanEntry.setStatus(_C)
_FsVlanVID_Type=VlanId
_FsVlanVID_Object=MibTableColumn
fsVlanVID=_FsVlanVID_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,5,1,1),_FsVlanVID_Type())
fsVlanVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVlanVID.setStatus(_C)
_FsVlanPortMemberAction_Type=MemberMap
_FsVlanPortMemberAction_Object=MibTableColumn
fsVlanPortMemberAction=_FsVlanPortMemberAction_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,5,1,2),_FsVlanPortMemberAction_Type())
fsVlanPortMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVlanPortMemberAction.setStatus(_C)
_FsVlanApMemberAction_Type=MemberMap
_FsVlanApMemberAction_Object=MibTableColumn
fsVlanApMemberAction=_FsVlanApMemberAction_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,5,1,3),_FsVlanApMemberAction_Type())
fsVlanApMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVlanApMemberAction.setStatus(_C)
class _FsVlanAlias_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsVlanAlias_Type.__name__=_J
_FsVlanAlias_Object=MibTableColumn
fsVlanAlias=_FsVlanAlias_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,5,1,4),_FsVlanAlias_Type())
fsVlanAlias.setMaxAccess(_M)
if mibBuilder.loadTexts:fsVlanAlias.setStatus(_C)
_FsVlanEntryStatus_Type=ConfigStatus
_FsVlanEntryStatus_Object=MibTableColumn
fsVlanEntryStatus=_FsVlanEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,5,1,5),_FsVlanEntryStatus_Type())
fsVlanEntryStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:fsVlanEntryStatus.setStatus(_C)
_FsVlanPortConfigTable_Object=MibTable
fsVlanPortConfigTable=_FsVlanPortConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,6))
if mibBuilder.loadTexts:fsVlanPortConfigTable.setStatus(_B)
_FsVlanPortConfigEntry_Object=MibTableRow
fsVlanPortConfigEntry=_FsVlanPortConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,6,1))
fsVlanPortConfigEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:fsVlanPortConfigEntry.setStatus(_B)
_FsVlanPortConfigIndex_Type=IfIndex
_FsVlanPortConfigIndex_Object=MibTableColumn
fsVlanPortConfigIndex=_FsVlanPortConfigIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,6,1,1),_FsVlanPortConfigIndex_Type())
fsVlanPortConfigIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:fsVlanPortConfigIndex.setStatus(_B)
class _FsVlanPortConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('access',1),('trunk',2),('dot1q-tunnel',3),('hybrid',4),('other',5),('uplink',6),('host',7),('promiscuous',8)))
_FsVlanPortConfigMode_Type.__name__=_I
_FsVlanPortConfigMode_Object=MibTableColumn
fsVlanPortConfigMode=_FsVlanPortConfigMode_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,6,1,2),_FsVlanPortConfigMode_Type())
fsVlanPortConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVlanPortConfigMode.setStatus(_B)
_FsVlanPortAccessVlan_Type=VlanId
_FsVlanPortAccessVlan_Object=MibTableColumn
fsVlanPortAccessVlan=_FsVlanPortAccessVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,6,1,3),_FsVlanPortAccessVlan_Type())
fsVlanPortAccessVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVlanPortAccessVlan.setStatus(_B)
_FsVlanPortNativeVlan_Type=VlanId
_FsVlanPortNativeVlan_Object=MibTableColumn
fsVlanPortNativeVlan=_FsVlanPortNativeVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,6,1,4),_FsVlanPortNativeVlan_Type())
fsVlanPortNativeVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVlanPortNativeVlan.setStatus(_B)
_FsVlanPortAllowedVlanList_Type=VlanList
_FsVlanPortAllowedVlanList_Object=MibTableColumn
fsVlanPortAllowedVlanList=_FsVlanPortAllowedVlanList_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,6,1,5),_FsVlanPortAllowedVlanList_Type())
fsVlanPortAllowedVlanList.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVlanPortAllowedVlanList.setStatus(_B)
_FsIfVlanID_Type=Integer32
_FsIfVlanID_Object=MibTableColumn
fsIfVlanID=_FsIfVlanID_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,6,1,6),_FsIfVlanID_Type())
fsIfVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIfVlanID.setStatus(_B)
_FsVlanConfigTable_Object=MibTable
fsVlanConfigTable=_FsVlanConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,7))
if mibBuilder.loadTexts:fsVlanConfigTable.setStatus(_B)
_FsVlanConfigEntry_Object=MibTableRow
fsVlanConfigEntry=_FsVlanConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,7,1))
fsVlanConfigEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:fsVlanConfigEntry.setStatus(_B)
_FsVlanConfigVID_Type=VlanId
_FsVlanConfigVID_Object=MibTableColumn
fsVlanConfigVID=_FsVlanConfigVID_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,7,1,1),_FsVlanConfigVID_Type())
fsVlanConfigVID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVlanConfigVID.setStatus(_B)
_FsVlanConfigAction_Type=Integer32
_FsVlanConfigAction_Object=MibTableColumn
fsVlanConfigAction=_FsVlanConfigAction_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,7,1,2),_FsVlanConfigAction_Type())
fsVlanConfigAction.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVlanConfigAction.setStatus(_B)
_FsVlanConfigName_Type=DisplayString
_FsVlanConfigName_Object=MibTableColumn
fsVlanConfigName=_FsVlanConfigName_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,7,1,3),_FsVlanConfigName_Type())
fsVlanConfigName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVlanConfigName.setStatus(_B)
_FsVlanConfigPortMember_Type=PortList
_FsVlanConfigPortMember_Object=MibTableColumn
fsVlanConfigPortMember=_FsVlanConfigPortMember_Object((1,3,6,1,4,1,52642,1,1,10,2,9,1,7,1,4),_FsVlanConfigPortMember_Type())
fsVlanConfigPortMember.setMaxAccess(_D)
if mibBuilder.loadTexts:fsVlanConfigPortMember.setStatus(_B)
_FsVlanMIBConformance_ObjectIdentity=ObjectIdentity
fsVlanMIBConformance=_FsVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,9,2))
_FsVlanMIBCompliances_ObjectIdentity=ObjectIdentity
fsVlanMIBCompliances=_FsVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,9,2,1))
_FsVlanMIBGroups_ObjectIdentity=ObjectIdentity
fsVlanMIBGroups=_FsVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,9,2,2))
fsVlanMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,9,2,2,1))
fsVlanMIBGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_F),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_G),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:fsVlanMIBGroup.setStatus(_B)
fsVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,9,2,1,1))
fsVlanMIBCompliance.setObjects((_A,_g))
if mibBuilder.loadTexts:fsVlanMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VlanList':VlanList,'fsVlanMIB':fsVlanMIB,'fsVlanMIBObjects':fsVlanMIBObjects,_O:fsVlanMaxNumber,_P:fsVlanCurrentNumber,_Q:fsSystemMaxVID,'fsVlanIfConfigTable':fsVlanIfConfigTable,'fsVlanIfConfigEntry':fsVlanIfConfigEntry,_K:fsVlanIfConfigIfIndex,_R:fsVlanIfAccessVlan,_S:fsVlanIfNativeVlan,_T:fsVlanIfAllowedVlanList,'fsVlanTable':fsVlanTable,'fsVlanEntry':fsVlanEntry,_F:fsVlanVID,_V:fsVlanPortMemberAction,_U:fsVlanApMemberAction,_W:fsVlanAlias,_X:fsVlanEntryStatus,'fsVlanPortConfigTable':fsVlanPortConfigTable,'fsVlanPortConfigEntry':fsVlanPortConfigEntry,_N:fsVlanPortConfigIndex,_Y:fsVlanPortConfigMode,_Z:fsVlanPortAccessVlan,_a:fsVlanPortNativeVlan,_b:fsVlanPortAllowedVlanList,_c:fsIfVlanID,'fsVlanConfigTable':fsVlanConfigTable,'fsVlanConfigEntry':fsVlanConfigEntry,_G:fsVlanConfigVID,_d:fsVlanConfigAction,_e:fsVlanConfigName,_f:fsVlanConfigPortMember,'fsVlanMIBConformance':fsVlanMIBConformance,'fsVlanMIBCompliances':fsVlanMIBCompliances,'fsVlanMIBCompliance':fsVlanMIBCompliance,'fsVlanMIBGroups':fsVlanMIBGroups,_g:fsVlanMIBGroup})