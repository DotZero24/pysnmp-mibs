_S='cSCLinkNotifControlGroup'
_R='cSCLinkMIBNotificationGroup'
_Q='cSCLinkMIBObjectGroup'
_P='ciscoServiceControlLinkModeChange'
_O='cscLinkNotifsEnabled'
_N='cscLinkAdminReflectionState'
_M='cscLinkNetworkSidePortIndex'
_L='cscLinkSubscriberSidePortIndex'
_K='cscLinkAdminReflectionEnable'
_J='cscLinkAdminModeOnFailure'
_I='cscLinkAdminModeOnActive'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='cscLinkOperMode'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='CISCO-SERVICE-CONTROL-LINK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_G,'PhysicalIndex',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoServiceControlLinkMIB=ModuleIdentity((1,3,6,1,4,1,9,9,631))
if mibBuilder.loadTexts:ciscoServiceControlLinkMIB.setRevisions(('2007-06-26 00:00',))
class CsceLinkModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('bypass',2),('forwarding',3),('cutoff',4),('sniffing',5)))
_CiscoSCLinkMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSCLinkMIBNotifs=_CiscoSCLinkMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,631,0))
_CiscoSCLinkMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSCLinkMIBObjects=_CiscoSCLinkMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,631,1))
_CscLinkNotifsEnabled_Type=TruthValue
_CscLinkNotifsEnabled_Object=MibScalar
cscLinkNotifsEnabled=_CscLinkNotifsEnabled_Object((1,3,6,1,4,1,9,9,631,1,1),_CscLinkNotifsEnabled_Type())
cscLinkNotifsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cscLinkNotifsEnabled.setStatus(_A)
_CscLinkStatusTable_Object=MibTable
cscLinkStatusTable=_CscLinkStatusTable_Object((1,3,6,1,4,1,9,9,631,1,2))
if mibBuilder.loadTexts:cscLinkStatusTable.setStatus(_A)
_CscLinkStatusEntry_Object=MibTableRow
cscLinkStatusEntry=_CscLinkStatusEntry_Object((1,3,6,1,4,1,9,9,631,1,2,1))
cscLinkStatusEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cscLinkStatusEntry.setStatus(_A)
_CscLinkAdminModeOnActive_Type=CsceLinkModeType
_CscLinkAdminModeOnActive_Object=MibTableColumn
cscLinkAdminModeOnActive=_CscLinkAdminModeOnActive_Object((1,3,6,1,4,1,9,9,631,1,2,1,1),_CscLinkAdminModeOnActive_Type())
cscLinkAdminModeOnActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cscLinkAdminModeOnActive.setStatus(_A)
_CscLinkAdminModeOnFailure_Type=CsceLinkModeType
_CscLinkAdminModeOnFailure_Object=MibTableColumn
cscLinkAdminModeOnFailure=_CscLinkAdminModeOnFailure_Object((1,3,6,1,4,1,9,9,631,1,2,1,2),_CscLinkAdminModeOnFailure_Type())
cscLinkAdminModeOnFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:cscLinkAdminModeOnFailure.setStatus(_A)
_CscLinkOperMode_Type=CsceLinkModeType
_CscLinkOperMode_Object=MibTableColumn
cscLinkOperMode=_CscLinkOperMode_Object((1,3,6,1,4,1,9,9,631,1,2,1,3),_CscLinkOperMode_Type())
cscLinkOperMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cscLinkOperMode.setStatus(_A)
class _CscLinkAdminReflectionEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reflectionEnabled',1),('reflectionOnAllPortsEnabled',2),('reflectionDisabled',3)))
_CscLinkAdminReflectionEnable_Type.__name__=_D
_CscLinkAdminReflectionEnable_Object=MibTableColumn
cscLinkAdminReflectionEnable=_CscLinkAdminReflectionEnable_Object((1,3,6,1,4,1,9,9,631,1,2,1,4),_CscLinkAdminReflectionEnable_Type())
cscLinkAdminReflectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cscLinkAdminReflectionEnable.setStatus(_A)
_CscLinkSubscriberSidePortIndex_Type=EntPhysicalIndexOrZero
_CscLinkSubscriberSidePortIndex_Object=MibTableColumn
cscLinkSubscriberSidePortIndex=_CscLinkSubscriberSidePortIndex_Object((1,3,6,1,4,1,9,9,631,1,2,1,5),_CscLinkSubscriberSidePortIndex_Type())
cscLinkSubscriberSidePortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cscLinkSubscriberSidePortIndex.setStatus(_A)
_CscLinkNetworkSidePortIndex_Type=EntPhysicalIndexOrZero
_CscLinkNetworkSidePortIndex_Object=MibTableColumn
cscLinkNetworkSidePortIndex=_CscLinkNetworkSidePortIndex_Object((1,3,6,1,4,1,9,9,631,1,2,1,6),_CscLinkNetworkSidePortIndex_Type())
cscLinkNetworkSidePortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cscLinkNetworkSidePortIndex.setStatus(_A)
class _CscLinkAdminReflectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noLinkReflection',1),('reflectingFailureToNetwork',2),('reflectingFailureToSubscriber',3),('reflectingFailureToBoth',4)))
_CscLinkAdminReflectionState_Type.__name__=_D
_CscLinkAdminReflectionState_Object=MibTableColumn
cscLinkAdminReflectionState=_CscLinkAdminReflectionState_Object((1,3,6,1,4,1,9,9,631,1,2,1,7),_CscLinkAdminReflectionState_Type())
cscLinkAdminReflectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:cscLinkAdminReflectionState.setStatus(_A)
_CiscoSCLinkMIBConform_ObjectIdentity=ObjectIdentity
ciscoSCLinkMIBConform=_CiscoSCLinkMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,631,2))
_CiscoSCLinkMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSCLinkMIBCompliances=_CiscoSCLinkMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,631,2,1))
_CiscoSCLinkMIBObjectGroups_ObjectIdentity=ObjectIdentity
ciscoSCLinkMIBObjectGroups=_CiscoSCLinkMIBObjectGroups_ObjectIdentity((1,3,6,1,4,1,9,9,631,2,2))
cSCLinkMIBObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,631,2,2,1))
cSCLinkMIBObjectGroup.setObjects(*((_B,_I),(_B,_J),(_B,_F),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cSCLinkMIBObjectGroup.setStatus(_A)
cSCLinkNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,631,2,2,3))
cSCLinkNotifControlGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:cSCLinkNotifControlGroup.setStatus(_A)
ciscoServiceControlLinkModeChange=NotificationType((1,3,6,1,4,1,9,9,631,0,1))
ciscoServiceControlLinkModeChange.setObjects((_B,_F))
if mibBuilder.loadTexts:ciscoServiceControlLinkModeChange.setStatus(_A)
cSCLinkMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,631,2,2,2))
cSCLinkMIBNotificationGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:cSCLinkMIBNotificationGroup.setStatus(_A)
cServiceLinkMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,631,2,1,1))
cServiceLinkMIBCompliance.setObjects(*((_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cServiceLinkMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CsceLinkModeType':CsceLinkModeType,'ciscoServiceControlLinkMIB':ciscoServiceControlLinkMIB,'ciscoSCLinkMIBNotifs':ciscoSCLinkMIBNotifs,_P:ciscoServiceControlLinkModeChange,'ciscoSCLinkMIBObjects':ciscoSCLinkMIBObjects,_O:cscLinkNotifsEnabled,'cscLinkStatusTable':cscLinkStatusTable,'cscLinkStatusEntry':cscLinkStatusEntry,_I:cscLinkAdminModeOnActive,_J:cscLinkAdminModeOnFailure,_F:cscLinkOperMode,_K:cscLinkAdminReflectionEnable,_L:cscLinkSubscriberSidePortIndex,_M:cscLinkNetworkSidePortIndex,_N:cscLinkAdminReflectionState,'ciscoSCLinkMIBConform':ciscoSCLinkMIBConform,'ciscoSCLinkMIBCompliances':ciscoSCLinkMIBCompliances,'cServiceLinkMIBCompliance':cServiceLinkMIBCompliance,'ciscoSCLinkMIBObjectGroups':ciscoSCLinkMIBObjectGroups,_Q:cSCLinkMIBObjectGroup,_R:cSCLinkMIBNotificationGroup,_S:cSCLinkNotifControlGroup})