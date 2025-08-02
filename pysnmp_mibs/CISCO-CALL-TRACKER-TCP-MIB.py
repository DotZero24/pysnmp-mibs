_R='ccttHistoryGroup'
_Q='ccttActiveGroup'
_P='ccttHistoryDestinationFailures'
_O='ccttHistoryRemoteTcpPort'
_N='ccttHistoryRemoteIpAddress'
_M='ccttHistoryLocalTcpPort'
_L='ccttHistoryLocalIpAddress'
_K='ccttActiveDestinationFailures'
_J='ccttActiveRemoteTcpPort'
_I='ccttActiveRemoteIpAddress'
_H='ccttActiveLocalTcpPort'
_G='ccttActiveLocalIpAddress'
_F='cctHistoryIndex'
_E='cctActiveCallId'
_D='CISCO-CALL-TRACKER-MIB'
_C='read-only'
_B='CISCO-CALL-TRACKER-TCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cctActiveCallId,cctHistoryIndex=mibBuilder.importSymbols(_D,_E,_F)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,=mibBuilder.importSymbols('CISCO-TC','CiscoPort')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoCallTrackerTCPMIB=ModuleIdentity((1,3,6,1,4,1,9,9,164))
if mibBuilder.loadTexts:ciscoCallTrackerTCPMIB.setRevisions(('2005-12-06 00:00','2000-06-07 00:00'))
_CcttMIBObjects_ObjectIdentity=ObjectIdentity
ccttMIBObjects=_CcttMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,164,1))
_CcttActive_ObjectIdentity=ObjectIdentity
ccttActive=_CcttActive_ObjectIdentity((1,3,6,1,4,1,9,9,164,1,1))
_CcttActiveTable_Object=MibTable
ccttActiveTable=_CcttActiveTable_Object((1,3,6,1,4,1,9,9,164,1,1,1))
if mibBuilder.loadTexts:ccttActiveTable.setStatus(_A)
_CcttActiveEntry_Object=MibTableRow
ccttActiveEntry=_CcttActiveEntry_Object((1,3,6,1,4,1,9,9,164,1,1,1,1))
ccttActiveEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ccttActiveEntry.setStatus(_A)
_CcttActiveLocalIpAddress_Type=IpAddress
_CcttActiveLocalIpAddress_Object=MibTableColumn
ccttActiveLocalIpAddress=_CcttActiveLocalIpAddress_Object((1,3,6,1,4,1,9,9,164,1,1,1,1,1),_CcttActiveLocalIpAddress_Type())
ccttActiveLocalIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttActiveLocalIpAddress.setStatus(_A)
_CcttActiveLocalTcpPort_Type=CiscoPort
_CcttActiveLocalTcpPort_Object=MibTableColumn
ccttActiveLocalTcpPort=_CcttActiveLocalTcpPort_Object((1,3,6,1,4,1,9,9,164,1,1,1,1,2),_CcttActiveLocalTcpPort_Type())
ccttActiveLocalTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttActiveLocalTcpPort.setStatus(_A)
_CcttActiveRemoteIpAddress_Type=IpAddress
_CcttActiveRemoteIpAddress_Object=MibTableColumn
ccttActiveRemoteIpAddress=_CcttActiveRemoteIpAddress_Object((1,3,6,1,4,1,9,9,164,1,1,1,1,3),_CcttActiveRemoteIpAddress_Type())
ccttActiveRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttActiveRemoteIpAddress.setStatus(_A)
_CcttActiveRemoteTcpPort_Type=CiscoPort
_CcttActiveRemoteTcpPort_Object=MibTableColumn
ccttActiveRemoteTcpPort=_CcttActiveRemoteTcpPort_Object((1,3,6,1,4,1,9,9,164,1,1,1,1,4),_CcttActiveRemoteTcpPort_Type())
ccttActiveRemoteTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttActiveRemoteTcpPort.setStatus(_A)
_CcttActiveDestinationFailures_Type=Counter32
_CcttActiveDestinationFailures_Object=MibTableColumn
ccttActiveDestinationFailures=_CcttActiveDestinationFailures_Object((1,3,6,1,4,1,9,9,164,1,1,1,1,5),_CcttActiveDestinationFailures_Type())
ccttActiveDestinationFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttActiveDestinationFailures.setStatus(_A)
_CcttHistory_ObjectIdentity=ObjectIdentity
ccttHistory=_CcttHistory_ObjectIdentity((1,3,6,1,4,1,9,9,164,1,2))
_CcttHistoryTable_Object=MibTable
ccttHistoryTable=_CcttHistoryTable_Object((1,3,6,1,4,1,9,9,164,1,2,1))
if mibBuilder.loadTexts:ccttHistoryTable.setStatus(_A)
_CcttHistoryEntry_Object=MibTableRow
ccttHistoryEntry=_CcttHistoryEntry_Object((1,3,6,1,4,1,9,9,164,1,2,1,1))
ccttHistoryEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:ccttHistoryEntry.setStatus(_A)
_CcttHistoryLocalIpAddress_Type=IpAddress
_CcttHistoryLocalIpAddress_Object=MibTableColumn
ccttHistoryLocalIpAddress=_CcttHistoryLocalIpAddress_Object((1,3,6,1,4,1,9,9,164,1,2,1,1,1),_CcttHistoryLocalIpAddress_Type())
ccttHistoryLocalIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttHistoryLocalIpAddress.setStatus(_A)
_CcttHistoryLocalTcpPort_Type=CiscoPort
_CcttHistoryLocalTcpPort_Object=MibTableColumn
ccttHistoryLocalTcpPort=_CcttHistoryLocalTcpPort_Object((1,3,6,1,4,1,9,9,164,1,2,1,1,2),_CcttHistoryLocalTcpPort_Type())
ccttHistoryLocalTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttHistoryLocalTcpPort.setStatus(_A)
_CcttHistoryRemoteIpAddress_Type=IpAddress
_CcttHistoryRemoteIpAddress_Object=MibTableColumn
ccttHistoryRemoteIpAddress=_CcttHistoryRemoteIpAddress_Object((1,3,6,1,4,1,9,9,164,1,2,1,1,3),_CcttHistoryRemoteIpAddress_Type())
ccttHistoryRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttHistoryRemoteIpAddress.setStatus(_A)
_CcttHistoryRemoteTcpPort_Type=CiscoPort
_CcttHistoryRemoteTcpPort_Object=MibTableColumn
ccttHistoryRemoteTcpPort=_CcttHistoryRemoteTcpPort_Object((1,3,6,1,4,1,9,9,164,1,2,1,1,4),_CcttHistoryRemoteTcpPort_Type())
ccttHistoryRemoteTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttHistoryRemoteTcpPort.setStatus(_A)
_CcttHistoryDestinationFailures_Type=Counter32
_CcttHistoryDestinationFailures_Object=MibTableColumn
ccttHistoryDestinationFailures=_CcttHistoryDestinationFailures_Object((1,3,6,1,4,1,9,9,164,1,2,1,1,5),_CcttHistoryDestinationFailures_Type())
ccttHistoryDestinationFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:ccttHistoryDestinationFailures.setStatus(_A)
_CcttMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ccttMIBNotificationPrefix=_CcttMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,164,2))
_CcttMIBNotifications_ObjectIdentity=ObjectIdentity
ccttMIBNotifications=_CcttMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,164,2,0))
_CcttMIBConformance_ObjectIdentity=ObjectIdentity
ccttMIBConformance=_CcttMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,164,3))
_CcttMIBCompliances_ObjectIdentity=ObjectIdentity
ccttMIBCompliances=_CcttMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,164,3,1))
_CcttMIBGroups_ObjectIdentity=ObjectIdentity
ccttMIBGroups=_CcttMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,164,3,2))
ccttActiveGroup=ObjectGroup((1,3,6,1,4,1,9,9,164,3,2,2))
ccttActiveGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ccttActiveGroup.setStatus(_A)
ccttHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,164,3,2,3))
ccttHistoryGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ccttHistoryGroup.setStatus(_A)
ccttMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,164,3,1,1))
ccttMIBCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ccttMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCallTrackerTCPMIB':ciscoCallTrackerTCPMIB,'ccttMIBObjects':ccttMIBObjects,'ccttActive':ccttActive,'ccttActiveTable':ccttActiveTable,'ccttActiveEntry':ccttActiveEntry,_G:ccttActiveLocalIpAddress,_H:ccttActiveLocalTcpPort,_I:ccttActiveRemoteIpAddress,_J:ccttActiveRemoteTcpPort,_K:ccttActiveDestinationFailures,'ccttHistory':ccttHistory,'ccttHistoryTable':ccttHistoryTable,'ccttHistoryEntry':ccttHistoryEntry,_L:ccttHistoryLocalIpAddress,_M:ccttHistoryLocalTcpPort,_N:ccttHistoryRemoteIpAddress,_O:ccttHistoryRemoteTcpPort,_P:ccttHistoryDestinationFailures,'ccttMIBNotificationPrefix':ccttMIBNotificationPrefix,'ccttMIBNotifications':ccttMIBNotifications,'ccttMIBConformance':ccttMIBConformance,'ccttMIBCompliances':ccttMIBCompliances,'ccttMIBCompliance':ccttMIBCompliance,'ccttMIBGroups':ccttMIBGroups,_Q:ccttActiveGroup,_R:ccttHistoryGroup})