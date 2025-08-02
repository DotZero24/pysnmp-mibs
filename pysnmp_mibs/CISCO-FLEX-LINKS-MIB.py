_a='ciscoFlexLinksPreferVlanGroup'
_Z='ciscoFlexLinksPreemptionGroup'
_Y='ciscoFlexLinksMmuPrimaryVlanGroup'
_X='cflIfStatusChangeNotif'
_W='cflIfConfigPrefer4kVlan'
_V='cflIfConfigPrefer2kVlan'
_U='cflIfConfigPreemptionDelay'
_T='cflIfConfigPreemptionMode'
_S='cflIfConfigMmuPrimaryVlan'
_R='cflEnableStatusChangeNotif'
_Q='cflIfConfigStatus'
_P='cflIfConfigStorageType'
_O='cflIfConfigBackUp'
_N='cflIfIndex'
_M='not-accessible'
_L='StorageType'
_K='ciscoFlexLinksNotifGroup'
_J='ciscoFlexLinksEnableNotifGroup'
_I='ciscoFlexLinksIfStatusGroup'
_H='ciscoFlexLinksIfConfigGroup'
_G='cflIfStatus'
_F='read-create'
_E='cflIfConfigPrimary'
_D='Integer32'
_C='read-write'
_B='CISCO-FLEX-LINKS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Cisco2KVlanList,=mibBuilder.importSymbols('CISCO-TC','Cisco2KVlanList')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
VlanIdOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIdOrNone')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_L,'TextualConvention','TruthValue')
ciscoFlexLinksMIB=ModuleIdentity((1,3,6,1,4,1,9,9,471))
if mibBuilder.loadTexts:ciscoFlexLinksMIB.setRevisions(('2010-02-04 00:00','2005-04-25 00:00'))
_CiscoFlexLinksMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFlexLinksMIBNotifs=_CiscoFlexLinksMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,471,0))
_CiscoFlexLinksMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFlexLinksMIBObjects=_CiscoFlexLinksMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,471,1))
_CflConfig_ObjectIdentity=ObjectIdentity
cflConfig=_CflConfig_ObjectIdentity((1,3,6,1,4,1,9,9,471,1,1))
_CflIfConfigTable_Object=MibTable
cflIfConfigTable=_CflIfConfigTable_Object((1,3,6,1,4,1,9,9,471,1,1,1))
if mibBuilder.loadTexts:cflIfConfigTable.setStatus(_A)
_CflIfConfigEntry_Object=MibTableRow
cflIfConfigEntry=_CflIfConfigEntry_Object((1,3,6,1,4,1,9,9,471,1,1,1,1))
cflIfConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cflIfConfigEntry.setStatus(_A)
_CflIfConfigPrimary_Type=InterfaceIndex
_CflIfConfigPrimary_Object=MibTableColumn
cflIfConfigPrimary=_CflIfConfigPrimary_Object((1,3,6,1,4,1,9,9,471,1,1,1,1,1),_CflIfConfigPrimary_Type())
cflIfConfigPrimary.setMaxAccess(_M)
if mibBuilder.loadTexts:cflIfConfigPrimary.setStatus(_A)
_CflIfConfigBackUp_Type=InterfaceIndexOrZero
_CflIfConfigBackUp_Object=MibTableColumn
cflIfConfigBackUp=_CflIfConfigBackUp_Object((1,3,6,1,4,1,9,9,471,1,1,1,1,2),_CflIfConfigBackUp_Type())
cflIfConfigBackUp.setMaxAccess(_F)
if mibBuilder.loadTexts:cflIfConfigBackUp.setStatus(_A)
class _CflIfConfigStorageType_Type(StorageType):defaultValue=3
_CflIfConfigStorageType_Type.__name__=_L
_CflIfConfigStorageType_Object=MibTableColumn
cflIfConfigStorageType=_CflIfConfigStorageType_Object((1,3,6,1,4,1,9,9,471,1,1,1,1,3),_CflIfConfigStorageType_Type())
cflIfConfigStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:cflIfConfigStorageType.setStatus(_A)
_CflIfConfigStatus_Type=RowStatus
_CflIfConfigStatus_Object=MibTableColumn
cflIfConfigStatus=_CflIfConfigStatus_Object((1,3,6,1,4,1,9,9,471,1,1,1,1,4),_CflIfConfigStatus_Type())
cflIfConfigStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cflIfConfigStatus.setStatus(_A)
_CflEnableStatusChangeNotif_Type=TruthValue
_CflEnableStatusChangeNotif_Object=MibScalar
cflEnableStatusChangeNotif=_CflEnableStatusChangeNotif_Object((1,3,6,1,4,1,9,9,471,1,1,2),_CflEnableStatusChangeNotif_Type())
cflEnableStatusChangeNotif.setMaxAccess(_C)
if mibBuilder.loadTexts:cflEnableStatusChangeNotif.setStatus(_A)
_CflIfConfigExtTable_Object=MibTable
cflIfConfigExtTable=_CflIfConfigExtTable_Object((1,3,6,1,4,1,9,9,471,1,1,3))
if mibBuilder.loadTexts:cflIfConfigExtTable.setStatus(_A)
_CflIfConfigExtEntry_Object=MibTableRow
cflIfConfigExtEntry=_CflIfConfigExtEntry_Object((1,3,6,1,4,1,9,9,471,1,1,3,1))
cflIfConfigExtEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cflIfConfigExtEntry.setStatus(_A)
_CflIfConfigMmuPrimaryVlan_Type=VlanIdOrNone
_CflIfConfigMmuPrimaryVlan_Object=MibTableColumn
cflIfConfigMmuPrimaryVlan=_CflIfConfigMmuPrimaryVlan_Object((1,3,6,1,4,1,9,9,471,1,1,3,1,1),_CflIfConfigMmuPrimaryVlan_Type())
cflIfConfigMmuPrimaryVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cflIfConfigMmuPrimaryVlan.setStatus(_A)
class _CflIfConfigPreemptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('forced',2),('bandwidth',3)))
_CflIfConfigPreemptionMode_Type.__name__=_D
_CflIfConfigPreemptionMode_Object=MibTableColumn
cflIfConfigPreemptionMode=_CflIfConfigPreemptionMode_Object((1,3,6,1,4,1,9,9,471,1,1,3,1,2),_CflIfConfigPreemptionMode_Type())
cflIfConfigPreemptionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cflIfConfigPreemptionMode.setStatus(_A)
_CflIfConfigPreemptionDelay_Type=Unsigned32
_CflIfConfigPreemptionDelay_Object=MibTableColumn
cflIfConfigPreemptionDelay=_CflIfConfigPreemptionDelay_Object((1,3,6,1,4,1,9,9,471,1,1,3,1,3),_CflIfConfigPreemptionDelay_Type())
cflIfConfigPreemptionDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cflIfConfigPreemptionDelay.setStatus(_A)
if mibBuilder.loadTexts:cflIfConfigPreemptionDelay.setUnits('seconds')
_CflIfConfigPrefer2kVlan_Type=Cisco2KVlanList
_CflIfConfigPrefer2kVlan_Object=MibTableColumn
cflIfConfigPrefer2kVlan=_CflIfConfigPrefer2kVlan_Object((1,3,6,1,4,1,9,9,471,1,1,3,1,4),_CflIfConfigPrefer2kVlan_Type())
cflIfConfigPrefer2kVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cflIfConfigPrefer2kVlan.setStatus(_A)
_CflIfConfigPrefer4kVlan_Type=Cisco2KVlanList
_CflIfConfigPrefer4kVlan_Object=MibTableColumn
cflIfConfigPrefer4kVlan=_CflIfConfigPrefer4kVlan_Object((1,3,6,1,4,1,9,9,471,1,1,3,1,5),_CflIfConfigPrefer4kVlan_Type())
cflIfConfigPrefer4kVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cflIfConfigPrefer4kVlan.setStatus(_A)
_CflStatus_ObjectIdentity=ObjectIdentity
cflStatus=_CflStatus_ObjectIdentity((1,3,6,1,4,1,9,9,471,1,2))
_CflIfStatusTable_Object=MibTable
cflIfStatusTable=_CflIfStatusTable_Object((1,3,6,1,4,1,9,9,471,1,2,1))
if mibBuilder.loadTexts:cflIfStatusTable.setStatus(_A)
_CflIfStatusEntry_Object=MibTableRow
cflIfStatusEntry=_CflIfStatusEntry_Object((1,3,6,1,4,1,9,9,471,1,2,1,1))
cflIfStatusEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cflIfStatusEntry.setStatus(_A)
_CflIfIndex_Type=InterfaceIndex
_CflIfIndex_Object=MibTableColumn
cflIfIndex=_CflIfIndex_Object((1,3,6,1,4,1,9,9,471,1,2,1,1,1),_CflIfIndex_Type())
cflIfIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:cflIfIndex.setStatus(_A)
class _CflIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('forwarding',1),('blocking',2),('down',3),('waitingToSync',4),('waitingForPeerStrate',5),('unknown',6),('vlbAll',7),('vlbConfig',8),('vlbPreempt',9)))
_CflIfStatus_Type.__name__=_D
_CflIfStatus_Object=MibTableColumn
cflIfStatus=_CflIfStatus_Object((1,3,6,1,4,1,9,9,471,1,2,1,1,2),_CflIfStatus_Type())
cflIfStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:cflIfStatus.setStatus(_A)
_CiscoFlexLinksMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFlexLinksMIBConformance=_CiscoFlexLinksMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,471,2))
_CiscoFlexLinksMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFlexLinksMIBCompliances=_CiscoFlexLinksMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,471,2,1))
_CiscoFlexLinksMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFlexLinksMIBGroups=_CiscoFlexLinksMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,471,2,2))
ciscoFlexLinksIfConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,471,2,2,1))
ciscoFlexLinksIfConfigGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoFlexLinksIfConfigGroup.setStatus(_A)
ciscoFlexLinksIfStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,471,2,2,2))
ciscoFlexLinksIfStatusGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:ciscoFlexLinksIfStatusGroup.setStatus(_A)
ciscoFlexLinksEnableNotifGroup=ObjectGroup((1,3,6,1,4,1,9,9,471,2,2,3))
ciscoFlexLinksEnableNotifGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:ciscoFlexLinksEnableNotifGroup.setStatus(_A)
ciscoFlexLinksMmuPrimaryVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,471,2,2,5))
ciscoFlexLinksMmuPrimaryVlanGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:ciscoFlexLinksMmuPrimaryVlanGroup.setStatus(_A)
ciscoFlexLinksPreemptionGroup=ObjectGroup((1,3,6,1,4,1,9,9,471,2,2,6))
ciscoFlexLinksPreemptionGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoFlexLinksPreemptionGroup.setStatus(_A)
ciscoFlexLinksPreferVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,471,2,2,7))
ciscoFlexLinksPreferVlanGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoFlexLinksPreferVlanGroup.setStatus(_A)
cflIfStatusChangeNotif=NotificationType((1,3,6,1,4,1,9,9,471,0,1))
cflIfStatusChangeNotif.setObjects((_B,_G))
if mibBuilder.loadTexts:cflIfStatusChangeNotif.setStatus(_A)
ciscoFlexLinksNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,471,2,2,4))
ciscoFlexLinksNotifGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:ciscoFlexLinksNotifGroup.setStatus(_A)
ciscoFlexLinksMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,471,2,1,1))
ciscoFlexLinksMIBCompliance.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoFlexLinksMIBCompliance.setStatus('deprecated')
ciscoFlexLinksMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,471,2,1,2))
ciscoFlexLinksMIBCompliance2.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoFlexLinksMIBCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFlexLinksMIB':ciscoFlexLinksMIB,'ciscoFlexLinksMIBNotifs':ciscoFlexLinksMIBNotifs,_X:cflIfStatusChangeNotif,'ciscoFlexLinksMIBObjects':ciscoFlexLinksMIBObjects,'cflConfig':cflConfig,'cflIfConfigTable':cflIfConfigTable,'cflIfConfigEntry':cflIfConfigEntry,_E:cflIfConfigPrimary,_O:cflIfConfigBackUp,_P:cflIfConfigStorageType,_Q:cflIfConfigStatus,_R:cflEnableStatusChangeNotif,'cflIfConfigExtTable':cflIfConfigExtTable,'cflIfConfigExtEntry':cflIfConfigExtEntry,_S:cflIfConfigMmuPrimaryVlan,_T:cflIfConfigPreemptionMode,_U:cflIfConfigPreemptionDelay,_V:cflIfConfigPrefer2kVlan,_W:cflIfConfigPrefer4kVlan,'cflStatus':cflStatus,'cflIfStatusTable':cflIfStatusTable,'cflIfStatusEntry':cflIfStatusEntry,_N:cflIfIndex,_G:cflIfStatus,'ciscoFlexLinksMIBConformance':ciscoFlexLinksMIBConformance,'ciscoFlexLinksMIBCompliances':ciscoFlexLinksMIBCompliances,'ciscoFlexLinksMIBCompliance':ciscoFlexLinksMIBCompliance,'ciscoFlexLinksMIBCompliance2':ciscoFlexLinksMIBCompliance2,'ciscoFlexLinksMIBGroups':ciscoFlexLinksMIBGroups,_H:ciscoFlexLinksIfConfigGroup,_I:ciscoFlexLinksIfStatusGroup,_J:ciscoFlexLinksEnableNotifGroup,_K:ciscoFlexLinksNotifGroup,_Y:ciscoFlexLinksMmuPrimaryVlanGroup,_Z:ciscoFlexLinksPreemptionGroup,_a:ciscoFlexLinksPreferVlanGroup})