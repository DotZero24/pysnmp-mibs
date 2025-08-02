_R='eltFlexLinksPreemptionGroup'
_Q='eltFlexLinksNotifGroup'
_P='eltFlexLinksEnableNotifGroup'
_O='eltFlexLinksIfStatusGroup'
_N='eltFlexLinksIfConfigGroup'
_M='eltFlIfStatusChangeNotif'
_L='eltFlIfConfigPreemptionDelay'
_K='eltFlIfConfigPreemptionMode'
_J='eltFlEnableStatusChangeNotif'
_I='eltFlIfConfigBackUp'
_H='read-only'
_G='eltFlIfStatus'
_F='eltFlIfIndex'
_E='read-write'
_D='eltFlIfConfigPrimary'
_C='Integer32'
_B='ELTEX-MES-FLEX-LINKS-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesMng,=mibBuilder.importSymbols('ELTEX-MES','eltMesMng')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
eltMesFlexLinksMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,23,1,5))
if mibBuilder.loadTexts:eltMesFlexLinksMIB.setRevisions(('2015-11-19 00:00',))
_EltMesFlexLinksMIBNotifs_ObjectIdentity=ObjectIdentity
eltMesFlexLinksMIBNotifs=_EltMesFlexLinksMIBNotifs_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,5,0))
_EltMesFlexLinksMIBObjects_ObjectIdentity=ObjectIdentity
eltMesFlexLinksMIBObjects=_EltMesFlexLinksMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,5,1))
_EltMesFlConfig_ObjectIdentity=ObjectIdentity
eltMesFlConfig=_EltMesFlConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,5,1,1))
_EltFlIfConfigTable_Object=MibTable
eltFlIfConfigTable=_EltFlIfConfigTable_Object((1,3,6,1,4,1,35265,1,23,1,5,1,1,1))
if mibBuilder.loadTexts:eltFlIfConfigTable.setStatus(_A)
_EltFlIfConfigEntry_Object=MibTableRow
eltFlIfConfigEntry=_EltFlIfConfigEntry_Object((1,3,6,1,4,1,35265,1,23,1,5,1,1,1,1))
eltFlIfConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:eltFlIfConfigEntry.setStatus(_A)
_EltFlIfConfigPrimary_Type=InterfaceIndex
_EltFlIfConfigPrimary_Object=MibTableColumn
eltFlIfConfigPrimary=_EltFlIfConfigPrimary_Object((1,3,6,1,4,1,35265,1,23,1,5,1,1,1,1,1),_EltFlIfConfigPrimary_Type())
eltFlIfConfigPrimary.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltFlIfConfigPrimary.setStatus(_A)
_EltFlIfConfigBackUp_Type=InterfaceIndexOrZero
_EltFlIfConfigBackUp_Object=MibTableColumn
eltFlIfConfigBackUp=_EltFlIfConfigBackUp_Object((1,3,6,1,4,1,35265,1,23,1,5,1,1,1,1,2),_EltFlIfConfigBackUp_Type())
eltFlIfConfigBackUp.setMaxAccess('read-create')
if mibBuilder.loadTexts:eltFlIfConfigBackUp.setStatus(_A)
_EltFlEnableStatusChangeNotif_Type=TruthValue
_EltFlEnableStatusChangeNotif_Object=MibScalar
eltFlEnableStatusChangeNotif=_EltFlEnableStatusChangeNotif_Object((1,3,6,1,4,1,35265,1,23,1,5,1,1,2),_EltFlEnableStatusChangeNotif_Type())
eltFlEnableStatusChangeNotif.setMaxAccess(_E)
if mibBuilder.loadTexts:eltFlEnableStatusChangeNotif.setStatus(_A)
_EltFlIfConfigExtTable_Object=MibTable
eltFlIfConfigExtTable=_EltFlIfConfigExtTable_Object((1,3,6,1,4,1,35265,1,23,1,5,1,1,3))
if mibBuilder.loadTexts:eltFlIfConfigExtTable.setStatus(_A)
_EltFlIfConfigExtEntry_Object=MibTableRow
eltFlIfConfigExtEntry=_EltFlIfConfigExtEntry_Object((1,3,6,1,4,1,35265,1,23,1,5,1,1,3,1))
eltFlIfConfigExtEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:eltFlIfConfigExtEntry.setStatus(_A)
class _EltFlIfConfigPreemptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('forced',2),('bandwidth',3)))
_EltFlIfConfigPreemptionMode_Type.__name__=_C
_EltFlIfConfigPreemptionMode_Object=MibTableColumn
eltFlIfConfigPreemptionMode=_EltFlIfConfigPreemptionMode_Object((1,3,6,1,4,1,35265,1,23,1,5,1,1,3,1,1),_EltFlIfConfigPreemptionMode_Type())
eltFlIfConfigPreemptionMode.setMaxAccess(_E)
if mibBuilder.loadTexts:eltFlIfConfigPreemptionMode.setStatus(_A)
_EltFlIfConfigPreemptionDelay_Type=Unsigned32
_EltFlIfConfigPreemptionDelay_Object=MibTableColumn
eltFlIfConfigPreemptionDelay=_EltFlIfConfigPreemptionDelay_Object((1,3,6,1,4,1,35265,1,23,1,5,1,1,3,1,2),_EltFlIfConfigPreemptionDelay_Type())
eltFlIfConfigPreemptionDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:eltFlIfConfigPreemptionDelay.setStatus(_A)
if mibBuilder.loadTexts:eltFlIfConfigPreemptionDelay.setUnits('seconds')
_EltMesFlStatus_ObjectIdentity=ObjectIdentity
eltMesFlStatus=_EltMesFlStatus_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,5,1,2))
_EltFlIfStatusTable_Object=MibTable
eltFlIfStatusTable=_EltFlIfStatusTable_Object((1,3,6,1,4,1,35265,1,23,1,5,1,2,1))
if mibBuilder.loadTexts:eltFlIfStatusTable.setStatus(_A)
_EltFlIfStatusEntry_Object=MibTableRow
eltFlIfStatusEntry=_EltFlIfStatusEntry_Object((1,3,6,1,4,1,35265,1,23,1,5,1,2,1,1))
eltFlIfStatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:eltFlIfStatusEntry.setStatus(_A)
_EltFlIfIndex_Type=InterfaceIndex
_EltFlIfIndex_Object=MibTableColumn
eltFlIfIndex=_EltFlIfIndex_Object((1,3,6,1,4,1,35265,1,23,1,5,1,2,1,1,1),_EltFlIfIndex_Type())
eltFlIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltFlIfIndex.setStatus(_A)
class _EltFlIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forwarding',1),('blocking',2),('down',3),('unknown',4)))
_EltFlIfStatus_Type.__name__=_C
_EltFlIfStatus_Object=MibTableColumn
eltFlIfStatus=_EltFlIfStatus_Object((1,3,6,1,4,1,35265,1,23,1,5,1,2,1,1,2),_EltFlIfStatus_Type())
eltFlIfStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:eltFlIfStatus.setStatus(_A)
_EltMesFlexLinksMIBConformance_ObjectIdentity=ObjectIdentity
eltMesFlexLinksMIBConformance=_EltMesFlexLinksMIBConformance_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,5,2))
_EltMesFlexLinksMIBCompliances_ObjectIdentity=ObjectIdentity
eltMesFlexLinksMIBCompliances=_EltMesFlexLinksMIBCompliances_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,5,2,1))
_EltMesFlexLinksMIBGroups_ObjectIdentity=ObjectIdentity
eltMesFlexLinksMIBGroups=_EltMesFlexLinksMIBGroups_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,5,2,2))
eltFlexLinksIfConfigGroup=ObjectGroup((1,3,6,1,4,1,35265,1,23,1,5,2,2,1))
eltFlexLinksIfConfigGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:eltFlexLinksIfConfigGroup.setStatus(_A)
eltFlexLinksIfStatusGroup=ObjectGroup((1,3,6,1,4,1,35265,1,23,1,5,2,2,2))
eltFlexLinksIfStatusGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:eltFlexLinksIfStatusGroup.setStatus(_A)
eltFlexLinksEnableNotifGroup=ObjectGroup((1,3,6,1,4,1,35265,1,23,1,5,2,2,3))
eltFlexLinksEnableNotifGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:eltFlexLinksEnableNotifGroup.setStatus(_A)
eltFlexLinksPreemptionGroup=ObjectGroup((1,3,6,1,4,1,35265,1,23,1,5,2,2,5))
eltFlexLinksPreemptionGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:eltFlexLinksPreemptionGroup.setStatus(_A)
eltFlIfStatusChangeNotif=NotificationType((1,3,6,1,4,1,35265,1,23,1,5,0,1))
eltFlIfStatusChangeNotif.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:eltFlIfStatusChangeNotif.setStatus(_A)
eltFlexLinksNotifGroup=NotificationGroup((1,3,6,1,4,1,35265,1,23,1,5,2,2,4))
eltFlexLinksNotifGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:eltFlexLinksNotifGroup.setStatus(_A)
eltFlexLinksMIBCompliance=ModuleCompliance((1,3,6,1,4,1,35265,1,23,1,5,2,1,1))
eltFlexLinksMIBCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:eltFlexLinksMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eltMesFlexLinksMIB':eltMesFlexLinksMIB,'eltMesFlexLinksMIBNotifs':eltMesFlexLinksMIBNotifs,_M:eltFlIfStatusChangeNotif,'eltMesFlexLinksMIBObjects':eltMesFlexLinksMIBObjects,'eltMesFlConfig':eltMesFlConfig,'eltFlIfConfigTable':eltFlIfConfigTable,'eltFlIfConfigEntry':eltFlIfConfigEntry,_D:eltFlIfConfigPrimary,_I:eltFlIfConfigBackUp,_J:eltFlEnableStatusChangeNotif,'eltFlIfConfigExtTable':eltFlIfConfigExtTable,'eltFlIfConfigExtEntry':eltFlIfConfigExtEntry,_K:eltFlIfConfigPreemptionMode,_L:eltFlIfConfigPreemptionDelay,'eltMesFlStatus':eltMesFlStatus,'eltFlIfStatusTable':eltFlIfStatusTable,'eltFlIfStatusEntry':eltFlIfStatusEntry,_F:eltFlIfIndex,_G:eltFlIfStatus,'eltMesFlexLinksMIBConformance':eltMesFlexLinksMIBConformance,'eltMesFlexLinksMIBCompliances':eltMesFlexLinksMIBCompliances,'eltFlexLinksMIBCompliance':eltFlexLinksMIBCompliance,'eltMesFlexLinksMIBGroups':eltMesFlexLinksMIBGroups,_N:eltFlexLinksIfConfigGroup,_O:eltFlexLinksIfStatusGroup,_P:eltFlexLinksEnableNotifGroup,_Q:eltFlexLinksNotifGroup,_R:eltFlexLinksPreemptionGroup})