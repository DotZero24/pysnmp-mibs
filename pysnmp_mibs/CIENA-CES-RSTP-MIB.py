_M='dot1dStpPortOperEdgePort'
_L='RSTP-MIB'
_K='current'
_J='cienaGlobalSeverity'
_I='cienaGlobalMacAddress'
_H='cienaCesPortPgIdMappingNotifSlotIndex'
_G='cienaCesPortPgIdMappingNotifShelfIndex'
_F='cienaCesPortPgIdMappingNotifPortNumber'
_E='cienaCesPortPgIdMappingNotifChassisIndex'
_D='dot1dStpPort'
_C='BRIDGE-MIB'
_B='CIENA-GLOBAL-MIB'
_A='CIENA-CES-PORT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPort,=mibBuilder.importSymbols(_C,_D)
cienaCesPortPgIdMappingNotifChassisIndex,cienaCesPortPgIdMappingNotifPortNumber,cienaCesPortPgIdMappingNotifShelfIndex,cienaCesPortPgIdMappingNotifSlotIndex=mibBuilder.importSymbols(_A,_E,_F,_G,_H)
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_B,_I,_J)
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
dot1dStpPortOperEdgePort,=mibBuilder.importSymbols(_L,_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaCesRstpMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,10))
if mibBuilder.loadTexts:cienaCesRstpMIB.setRevisions(('2010-03-28 00:00',))
_CienaCesRstpMIBConformance_ObjectIdentity=ObjectIdentity
cienaCesRstpMIBConformance=_CienaCesRstpMIBConformance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,10,2))
_CienaCesRstpMIBCompliances_ObjectIdentity=ObjectIdentity
cienaCesRstpMIBCompliances=_CienaCesRstpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1271,2,1,10,2,1))
_CienaCesRstpMIBGroups_ObjectIdentity=ObjectIdentity
cienaCesRstpMIBGroups=_CienaCesRstpMIBGroups_ObjectIdentity((1,3,6,1,4,1,1271,2,1,10,2,2))
_CienaCesRstpMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesRstpMIBNotificationPrefix=_CienaCesRstpMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,10))
_CienaCesRstpMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesRstpMIBNotifications=_CienaCesRstpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,10,0))
cienaCesRstpPortBackupNotification=NotificationType((1,3,6,1,4,1,1271,2,2,10,0,1))
cienaCesRstpPortBackupNotification.setObjects(*((_B,_J),(_B,_I),(_A,_E),(_A,_G),(_A,_H),(_A,_F),(_C,_D)))
if mibBuilder.loadTexts:cienaCesRstpPortBackupNotification.setStatus(_K)
cienaCesRstpPvstBpduReceivedNotification=NotificationType((1,3,6,1,4,1,1271,2,2,10,0,2))
cienaCesRstpPvstBpduReceivedNotification.setObjects(*((_B,_J),(_B,_I),(_A,_E),(_A,_G),(_A,_H),(_A,_F),(_C,_D)))
if mibBuilder.loadTexts:cienaCesRstpPvstBpduReceivedNotification.setStatus(_K)
cienaCesRstpSelfLoopNotification=NotificationType((1,3,6,1,4,1,1271,2,2,10,0,3))
cienaCesRstpSelfLoopNotification.setObjects(*((_B,_J),(_B,_I),(_A,_E),(_A,_G),(_A,_H),(_A,_F),(_C,_D)))
if mibBuilder.loadTexts:cienaCesRstpSelfLoopNotification.setStatus(_K)
cienaCesRstpPortOperEdgeNotification=NotificationType((1,3,6,1,4,1,1271,2,2,10,0,4))
cienaCesRstpPortOperEdgeNotification.setObjects(*((_B,_J),(_B,_I),(_A,_E),(_A,_G),(_A,_H),(_A,_F),(_C,_D),(_L,_M)))
if mibBuilder.loadTexts:cienaCesRstpPortOperEdgeNotification.setStatus(_K)
cienaCesRstpPortFlapNotification=NotificationType((1,3,6,1,4,1,1271,2,2,10,0,5))
cienaCesRstpPortFlapNotification.setObjects(*((_B,_J),(_B,_I),(_A,_E),(_A,_G),(_A,_H),(_A,_F),(_C,_D)))
if mibBuilder.loadTexts:cienaCesRstpPortFlapNotification.setStatus(_K)
cienaCesRstpBridgeRootPortLostNotification=NotificationType((1,3,6,1,4,1,1271,2,2,10,0,6))
cienaCesRstpBridgeRootPortLostNotification.setObjects(*((_B,_J),(_B,_I),(_A,_E),(_A,_G),(_A,_H),(_A,_F),(_C,_D)))
if mibBuilder.loadTexts:cienaCesRstpBridgeRootPortLostNotification.setStatus(_K)
mibBuilder.exportSymbols('CIENA-CES-RSTP-MIB',**{'cienaCesRstpMIB':cienaCesRstpMIB,'cienaCesRstpMIBConformance':cienaCesRstpMIBConformance,'cienaCesRstpMIBCompliances':cienaCesRstpMIBCompliances,'cienaCesRstpMIBGroups':cienaCesRstpMIBGroups,'cienaCesRstpMIBNotificationPrefix':cienaCesRstpMIBNotificationPrefix,'cienaCesRstpMIBNotifications':cienaCesRstpMIBNotifications,'cienaCesRstpPortBackupNotification':cienaCesRstpPortBackupNotification,'cienaCesRstpPvstBpduReceivedNotification':cienaCesRstpPvstBpduReceivedNotification,'cienaCesRstpSelfLoopNotification':cienaCesRstpSelfLoopNotification,'cienaCesRstpPortOperEdgeNotification':cienaCesRstpPortOperEdgeNotification,'cienaCesRstpPortFlapNotification':cienaCesRstpPortFlapNotification,'cienaCesRstpBridgeRootPortLostNotification':cienaCesRstpBridgeRootPortLostNotification})