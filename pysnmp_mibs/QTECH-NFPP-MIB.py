#
# PySNMP MIB module QTECH-NFPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-NFPP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
qtechNFPPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43))
qtechNFPPMIB.setRevisions(('2009-07-09 00:00',))
if mibBuilder.loadTexts: qtechNFPPMIB.setLastUpdated('200907090000Z')
if mibBuilder.loadTexts: qtechNFPPMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechNFPPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 1))
qtechNFPPMessageContent = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 1, 0), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: qtechNFPPMessageContent.setStatus('current')
qtechNFPPMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 2))
qtechNFPPMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 2, 0))
qtechNFPPMessageGenerated = NotificationType((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 2, 0, 1)).setObjects(("QTECH-NFPP-MIB", "qtechNFPPMessageContent"))
if mibBuilder.loadTexts: qtechNFPPMessageGenerated.setStatus('current')
qtechNFPPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3))
qtechNFPPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 1))
qtechNFPPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 2))
qtechNFPPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 1, 1)).setObjects(("QTECH-NFPP-MIB", "qtechNFPPNotifObjectsGroup"), ("QTECH-NFPP-MIB", "qtechNFPPNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechNFPPMIBCompliance = qtechNFPPMIBCompliance.setStatus('current')
qtechNFPPNotifObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 2, 1)).setObjects(("QTECH-NFPP-MIB", "qtechNFPPMessageContent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechNFPPNotifObjectsGroup = qtechNFPPNotifObjectsGroup.setStatus('current')
qtechNFPPNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 43, 3, 2, 2)).setObjects(("QTECH-NFPP-MIB", "qtechNFPPMessageGenerated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechNFPPNotificationsGroup = qtechNFPPNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-NFPP-MIB", qtechNFPPNotifObjectsGroup=qtechNFPPNotifObjectsGroup, qtechNFPPNotificationsGroup=qtechNFPPNotificationsGroup, qtechNFPPMIBObjects=qtechNFPPMIBObjects, qtechNFPPMIBNotifications=qtechNFPPMIBNotifications, qtechNFPPMIBCompliances=qtechNFPPMIBCompliances, qtechNFPPMIBCompliance=qtechNFPPMIBCompliance, qtechNFPPMessageGenerated=qtechNFPPMessageGenerated, qtechNFPPMIBGroups=qtechNFPPMIBGroups, qtechNFPPMIB=qtechNFPPMIB, qtechNFPPMIBNotificationPrefix=qtechNFPPMIBNotificationPrefix, qtechNFPPMessageContent=qtechNFPPMessageContent, PYSNMP_MODULE_ID=qtechNFPPMIB, qtechNFPPMIBConformance=qtechNFPPMIBConformance)
