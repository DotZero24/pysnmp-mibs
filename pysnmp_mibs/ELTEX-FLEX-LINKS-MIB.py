_R='eltexFlexLinksPreemptionGroup'
_Q='eltexFlexLinksNotifGroup'
_P='eltexFlexLinksEnableNotifGroup'
_O='eltexFlexLinksIfStatusGroup'
_N='eltexFlexLinksIfConfigGroup'
_M='eltexFlIfStatusChangeNotif'
_L='eltexFlIfConfigPreemptionDelay'
_K='eltexFlIfConfigPreemptionMode'
_J='eltexFlEnableStatusChangeNotif'
_I='eltexFlIfConfigBackUp'
_H='read-only'
_G='eltexFlIfStatus'
_F='eltexFlIfIndex'
_E='read-write'
_D='eltexFlIfConfigPrimary'
_C='Integer32'
_B='ELTEX-FLEX-LINKS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
eltexFlexLinksMIB=ModuleIdentity((1,3,6,1,4,1,35265,31))
_EltexFlexLinksMIBNotifs_ObjectIdentity=ObjectIdentity
eltexFlexLinksMIBNotifs=_EltexFlexLinksMIBNotifs_ObjectIdentity((1,3,6,1,4,1,35265,31,0))
_EltexFlexLinksMIBObjects_ObjectIdentity=ObjectIdentity
eltexFlexLinksMIBObjects=_EltexFlexLinksMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,31,1))
_EltexFlConfig_ObjectIdentity=ObjectIdentity
eltexFlConfig=_EltexFlConfig_ObjectIdentity((1,3,6,1,4,1,35265,31,1,1))
_EltexFlIfConfigTable_Object=MibTable
eltexFlIfConfigTable=_EltexFlIfConfigTable_Object((1,3,6,1,4,1,35265,31,1,1,1))
if mibBuilder.loadTexts:eltexFlIfConfigTable.setStatus(_A)
_EltexFlIfConfigEntry_Object=MibTableRow
eltexFlIfConfigEntry=_EltexFlIfConfigEntry_Object((1,3,6,1,4,1,35265,31,1,1,1,1))
eltexFlIfConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:eltexFlIfConfigEntry.setStatus(_A)
_EltexFlIfConfigPrimary_Type=InterfaceIndex
_EltexFlIfConfigPrimary_Object=MibTableColumn
eltexFlIfConfigPrimary=_EltexFlIfConfigPrimary_Object((1,3,6,1,4,1,35265,31,1,1,1,1,1),_EltexFlIfConfigPrimary_Type())
eltexFlIfConfigPrimary.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltexFlIfConfigPrimary.setStatus(_A)
_EltexFlIfConfigBackUp_Type=InterfaceIndexOrZero
_EltexFlIfConfigBackUp_Object=MibTableColumn
eltexFlIfConfigBackUp=_EltexFlIfConfigBackUp_Object((1,3,6,1,4,1,35265,31,1,1,1,1,2),_EltexFlIfConfigBackUp_Type())
eltexFlIfConfigBackUp.setMaxAccess('read-create')
if mibBuilder.loadTexts:eltexFlIfConfigBackUp.setStatus(_A)
_EltexFlEnableStatusChangeNotif_Type=TruthValue
_EltexFlEnableStatusChangeNotif_Object=MibScalar
eltexFlEnableStatusChangeNotif=_EltexFlEnableStatusChangeNotif_Object((1,3,6,1,4,1,35265,31,1,1,2),_EltexFlEnableStatusChangeNotif_Type())
eltexFlEnableStatusChangeNotif.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexFlEnableStatusChangeNotif.setStatus(_A)
_EltexFlIfConfigExtTable_Object=MibTable
eltexFlIfConfigExtTable=_EltexFlIfConfigExtTable_Object((1,3,6,1,4,1,35265,31,1,1,3))
if mibBuilder.loadTexts:eltexFlIfConfigExtTable.setStatus(_A)
_EltexFlIfConfigExtEntry_Object=MibTableRow
eltexFlIfConfigExtEntry=_EltexFlIfConfigExtEntry_Object((1,3,6,1,4,1,35265,31,1,1,3,1))
eltexFlIfConfigExtEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:eltexFlIfConfigExtEntry.setStatus(_A)
class _EltexFlIfConfigPreemptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('forced',2),('bandwidth',3)))
_EltexFlIfConfigPreemptionMode_Type.__name__=_C
_EltexFlIfConfigPreemptionMode_Object=MibTableColumn
eltexFlIfConfigPreemptionMode=_EltexFlIfConfigPreemptionMode_Object((1,3,6,1,4,1,35265,31,1,1,3,1,1),_EltexFlIfConfigPreemptionMode_Type())
eltexFlIfConfigPreemptionMode.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexFlIfConfigPreemptionMode.setStatus(_A)
_EltexFlIfConfigPreemptionDelay_Type=Unsigned32
_EltexFlIfConfigPreemptionDelay_Object=MibTableColumn
eltexFlIfConfigPreemptionDelay=_EltexFlIfConfigPreemptionDelay_Object((1,3,6,1,4,1,35265,31,1,1,3,1,2),_EltexFlIfConfigPreemptionDelay_Type())
eltexFlIfConfigPreemptionDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexFlIfConfigPreemptionDelay.setStatus(_A)
if mibBuilder.loadTexts:eltexFlIfConfigPreemptionDelay.setUnits('seconds')
_EltexFlStatus_ObjectIdentity=ObjectIdentity
eltexFlStatus=_EltexFlStatus_ObjectIdentity((1,3,6,1,4,1,35265,31,1,2))
_EltexFlIfStatusTable_Object=MibTable
eltexFlIfStatusTable=_EltexFlIfStatusTable_Object((1,3,6,1,4,1,35265,31,1,2,1))
if mibBuilder.loadTexts:eltexFlIfStatusTable.setStatus(_A)
_EltexFlIfStatusEntry_Object=MibTableRow
eltexFlIfStatusEntry=_EltexFlIfStatusEntry_Object((1,3,6,1,4,1,35265,31,1,2,1,1))
eltexFlIfStatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:eltexFlIfStatusEntry.setStatus(_A)
_EltexFlIfIndex_Type=InterfaceIndex
_EltexFlIfIndex_Object=MibTableColumn
eltexFlIfIndex=_EltexFlIfIndex_Object((1,3,6,1,4,1,35265,31,1,2,1,1,1),_EltexFlIfIndex_Type())
eltexFlIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexFlIfIndex.setStatus(_A)
class _EltexFlIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forwarding',1),('blocking',2),('down',3),('unknown',4)))
_EltexFlIfStatus_Type.__name__=_C
_EltexFlIfStatus_Object=MibTableColumn
eltexFlIfStatus=_EltexFlIfStatus_Object((1,3,6,1,4,1,35265,31,1,2,1,1,2),_EltexFlIfStatus_Type())
eltexFlIfStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexFlIfStatus.setStatus(_A)
_EltexFlexLinksMIBConformance_ObjectIdentity=ObjectIdentity
eltexFlexLinksMIBConformance=_EltexFlexLinksMIBConformance_ObjectIdentity((1,3,6,1,4,1,35265,31,2))
_EltexFlexLinksMIBCompliances_ObjectIdentity=ObjectIdentity
eltexFlexLinksMIBCompliances=_EltexFlexLinksMIBCompliances_ObjectIdentity((1,3,6,1,4,1,35265,31,2,1))
_EltexFlexLinksMIBGroups_ObjectIdentity=ObjectIdentity
eltexFlexLinksMIBGroups=_EltexFlexLinksMIBGroups_ObjectIdentity((1,3,6,1,4,1,35265,31,2,2))
eltexFlexLinksIfConfigGroup=ObjectGroup((1,3,6,1,4,1,35265,31,2,2,1))
eltexFlexLinksIfConfigGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:eltexFlexLinksIfConfigGroup.setStatus(_A)
eltexFlexLinksIfStatusGroup=ObjectGroup((1,3,6,1,4,1,35265,31,2,2,2))
eltexFlexLinksIfStatusGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:eltexFlexLinksIfStatusGroup.setStatus(_A)
eltexFlexLinksEnableNotifGroup=ObjectGroup((1,3,6,1,4,1,35265,31,2,2,3))
eltexFlexLinksEnableNotifGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:eltexFlexLinksEnableNotifGroup.setStatus(_A)
eltexFlexLinksPreemptionGroup=ObjectGroup((1,3,6,1,4,1,35265,31,2,2,5))
eltexFlexLinksPreemptionGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:eltexFlexLinksPreemptionGroup.setStatus(_A)
eltexFlIfStatusChangeNotif=NotificationType((1,3,6,1,4,1,35265,31,0,1))
eltexFlIfStatusChangeNotif.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:eltexFlIfStatusChangeNotif.setStatus(_A)
eltexFlexLinksNotifGroup=NotificationGroup((1,3,6,1,4,1,35265,31,2,2,4))
eltexFlexLinksNotifGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:eltexFlexLinksNotifGroup.setStatus(_A)
eltexFlexLinksMIBCompliance=ModuleCompliance((1,3,6,1,4,1,35265,31,2,1,1))
eltexFlexLinksMIBCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:eltexFlexLinksMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eltexFlexLinksMIB':eltexFlexLinksMIB,'eltexFlexLinksMIBNotifs':eltexFlexLinksMIBNotifs,_M:eltexFlIfStatusChangeNotif,'eltexFlexLinksMIBObjects':eltexFlexLinksMIBObjects,'eltexFlConfig':eltexFlConfig,'eltexFlIfConfigTable':eltexFlIfConfigTable,'eltexFlIfConfigEntry':eltexFlIfConfigEntry,_D:eltexFlIfConfigPrimary,_I:eltexFlIfConfigBackUp,_J:eltexFlEnableStatusChangeNotif,'eltexFlIfConfigExtTable':eltexFlIfConfigExtTable,'eltexFlIfConfigExtEntry':eltexFlIfConfigExtEntry,_K:eltexFlIfConfigPreemptionMode,_L:eltexFlIfConfigPreemptionDelay,'eltexFlStatus':eltexFlStatus,'eltexFlIfStatusTable':eltexFlIfStatusTable,'eltexFlIfStatusEntry':eltexFlIfStatusEntry,_F:eltexFlIfIndex,_G:eltexFlIfStatus,'eltexFlexLinksMIBConformance':eltexFlexLinksMIBConformance,'eltexFlexLinksMIBCompliances':eltexFlexLinksMIBCompliances,'eltexFlexLinksMIBCompliance':eltexFlexLinksMIBCompliance,'eltexFlexLinksMIBGroups':eltexFlexLinksMIBGroups,_N:eltexFlexLinksIfConfigGroup,_O:eltexFlexLinksIfStatusGroup,_P:eltexFlexLinksEnableNotifGroup,_Q:eltexFlexLinksNotifGroup,_R:eltexFlexLinksPreemptionGroup})