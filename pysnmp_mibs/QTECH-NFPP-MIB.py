#
# PySNMP MIB module QTECH-NFPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-NFPP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("QTECH-NFPP-MIB", qtechNFPPMIBGroups=qtechNFPPMIBGroups, qtechNFPPMIBCompliances=qtechNFPPMIBCompliances, qtechNFPPMIBCompliance=qtechNFPPMIBCompliance, qtechNFPPMIBNotificationPrefix=qtechNFPPMIBNotificationPrefix, qtechNFPPMIBObjects=qtechNFPPMIBObjects, qtechNFPPMessageGenerated=qtechNFPPMessageGenerated, qtechNFPPNotificationsGroup=qtechNFPPNotificationsGroup, qtechNFPPMIBNotifications=qtechNFPPMIBNotifications, qtechNFPPMIBConformance=qtechNFPPMIBConformance, qtechNFPPMessageContent=qtechNFPPMessageContent, qtechNFPPMIB=qtechNFPPMIB, qtechNFPPNotifObjectsGroup=qtechNFPPNotifObjectsGroup, PYSNMP_MODULE_ID=qtechNFPPMIB)
