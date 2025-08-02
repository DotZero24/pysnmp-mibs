_S='myVlanMIBGroup'
_R='myVlanEntryStatus'
_Q='myVlanAlias'
_P='myVlanPortMemberAction'
_O='myVlanApMemberAction'
_N='myVlanIfAllowedVlanList'
_M='myVlanIfNativeVlan'
_L='myVlanIfAccessVlan'
_K='mySystemMaxVID'
_J='myVlanCurrentNumber'
_I='myVlanMaxNumber'
_H='DisplayString'
_G='OctetString'
_F='myVlanVID'
_E='myVlanIfConfigIfIndex'
_D='read-write'
_C='read-only'
_B='MY-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ConfigStatus,IfIndex,MemberMap=mibBuilder.importSymbols('MY-TC','ConfigStatus','IfIndex','MemberMap')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myVlanMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,9))
if mibBuilder.loadTexts:myVlanMIB.setRevisions(('2002-03-20 00:00',))
_MyVlanMIBObjects_ObjectIdentity=ObjectIdentity
myVlanMIBObjects=_MyVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,9,1))
_MyVlanMaxNumber_Type=Integer32
_MyVlanMaxNumber_Object=MibScalar
myVlanMaxNumber=_MyVlanMaxNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,1),_MyVlanMaxNumber_Type())
myVlanMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myVlanMaxNumber.setStatus(_A)
_MyVlanCurrentNumber_Type=Integer32
_MyVlanCurrentNumber_Object=MibScalar
myVlanCurrentNumber=_MyVlanCurrentNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,2),_MyVlanCurrentNumber_Type())
myVlanCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myVlanCurrentNumber.setStatus(_A)
_MySystemMaxVID_Type=Integer32
_MySystemMaxVID_Object=MibScalar
mySystemMaxVID=_MySystemMaxVID_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,3),_MySystemMaxVID_Type())
mySystemMaxVID.setMaxAccess(_C)
if mibBuilder.loadTexts:mySystemMaxVID.setStatus(_A)
_MyVlanIfConfigTable_Object=MibTable
myVlanIfConfigTable=_MyVlanIfConfigTable_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,4))
if mibBuilder.loadTexts:myVlanIfConfigTable.setStatus(_A)
_MyVlanIfConfigEntry_Object=MibTableRow
myVlanIfConfigEntry=_MyVlanIfConfigEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,4,1))
myVlanIfConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:myVlanIfConfigEntry.setStatus(_A)
_MyVlanIfConfigIfIndex_Type=IfIndex
_MyVlanIfConfigIfIndex_Object=MibTableColumn
myVlanIfConfigIfIndex=_MyVlanIfConfigIfIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,4,1,1),_MyVlanIfConfigIfIndex_Type())
myVlanIfConfigIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:myVlanIfConfigIfIndex.setStatus(_A)
_MyVlanIfAccessVlan_Type=VlanId
_MyVlanIfAccessVlan_Object=MibTableColumn
myVlanIfAccessVlan=_MyVlanIfAccessVlan_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,4,1,2),_MyVlanIfAccessVlan_Type())
myVlanIfAccessVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanIfAccessVlan.setStatus(_A)
_MyVlanIfNativeVlan_Type=VlanId
_MyVlanIfNativeVlan_Object=MibTableColumn
myVlanIfNativeVlan=_MyVlanIfNativeVlan_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,4,1,3),_MyVlanIfNativeVlan_Type())
myVlanIfNativeVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanIfNativeVlan.setStatus(_A)
class _MyVlanIfAllowedVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_MyVlanIfAllowedVlanList_Type.__name__=_G
_MyVlanIfAllowedVlanList_Object=MibTableColumn
myVlanIfAllowedVlanList=_MyVlanIfAllowedVlanList_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,4,1,4),_MyVlanIfAllowedVlanList_Type())
myVlanIfAllowedVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanIfAllowedVlanList.setStatus(_A)
_MyVlanTable_Object=MibTable
myVlanTable=_MyVlanTable_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,5))
if mibBuilder.loadTexts:myVlanTable.setStatus(_A)
_MyVlanEntry_Object=MibTableRow
myVlanEntry=_MyVlanEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,5,1))
myVlanEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:myVlanEntry.setStatus(_A)
_MyVlanVID_Type=VlanId
_MyVlanVID_Object=MibTableColumn
myVlanVID=_MyVlanVID_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,5,1,1),_MyVlanVID_Type())
myVlanVID.setMaxAccess(_C)
if mibBuilder.loadTexts:myVlanVID.setStatus(_A)
_MyVlanPortMemberAction_Type=MemberMap
_MyVlanPortMemberAction_Object=MibTableColumn
myVlanPortMemberAction=_MyVlanPortMemberAction_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,5,1,2),_MyVlanPortMemberAction_Type())
myVlanPortMemberAction.setMaxAccess(_C)
if mibBuilder.loadTexts:myVlanPortMemberAction.setStatus(_A)
_MyVlanApMemberAction_Type=MemberMap
_MyVlanApMemberAction_Object=MibTableColumn
myVlanApMemberAction=_MyVlanApMemberAction_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,5,1,3),_MyVlanApMemberAction_Type())
myVlanApMemberAction.setMaxAccess(_C)
if mibBuilder.loadTexts:myVlanApMemberAction.setStatus(_A)
class _MyVlanAlias_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyVlanAlias_Type.__name__=_H
_MyVlanAlias_Object=MibTableColumn
myVlanAlias=_MyVlanAlias_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,5,1,4),_MyVlanAlias_Type())
myVlanAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:myVlanAlias.setStatus(_A)
_MyVlanEntryStatus_Type=ConfigStatus
_MyVlanEntryStatus_Object=MibTableColumn
myVlanEntryStatus=_MyVlanEntryStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,9,1,5,1,5),_MyVlanEntryStatus_Type())
myVlanEntryStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:myVlanEntryStatus.setStatus(_A)
_MyVlanMIBConformance_ObjectIdentity=ObjectIdentity
myVlanMIBConformance=_MyVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,9,2))
_MyVlanMIBCompliances_ObjectIdentity=ObjectIdentity
myVlanMIBCompliances=_MyVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,9,2,1))
_MyVlanMIBGroups_ObjectIdentity=ObjectIdentity
myVlanMIBGroups=_MyVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,9,2,2))
myVlanMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,9,2,2,1))
myVlanMIBGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_E),(_B,_L),(_B,_M),(_B,_N),(_B,_F),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:myVlanMIBGroup.setStatus(_A)
myVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,9,2,1,1))
myVlanMIBCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:myVlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myVlanMIB':myVlanMIB,'myVlanMIBObjects':myVlanMIBObjects,_I:myVlanMaxNumber,_J:myVlanCurrentNumber,_K:mySystemMaxVID,'myVlanIfConfigTable':myVlanIfConfigTable,'myVlanIfConfigEntry':myVlanIfConfigEntry,_E:myVlanIfConfigIfIndex,_L:myVlanIfAccessVlan,_M:myVlanIfNativeVlan,_N:myVlanIfAllowedVlanList,'myVlanTable':myVlanTable,'myVlanEntry':myVlanEntry,_F:myVlanVID,_P:myVlanPortMemberAction,_O:myVlanApMemberAction,_Q:myVlanAlias,_R:myVlanEntryStatus,'myVlanMIBConformance':myVlanMIBConformance,'myVlanMIBCompliances':myVlanMIBCompliances,'myVlanMIBCompliance':myVlanMIBCompliance,'myVlanMIBGroups':myVlanMIBGroups,_S:myVlanMIBGroup})