#
# PySNMP MIB module FS-NFPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-NFPP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsNFPPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43))
fsNFPPMIB.setRevisions(('2009-07-09 00:00',))
if mibBuilder.loadTexts: fsNFPPMIB.setLastUpdated('200907090000Z')
if mibBuilder.loadTexts: fsNFPPMIB.setOrganization('FS.COM Inc..')
fsNFPPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 1))
fsNFPPMessageContent = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 1, 0), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fsNFPPMessageContent.setStatus('current')
fsNFPPMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 2))
fsNFPPMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 2, 0))
fsNFPPMessageGenerated = NotificationType((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 2, 0, 1)).setObjects(("FS-NFPP-MIB", "fsNFPPMessageContent"))
if mibBuilder.loadTexts: fsNFPPMessageGenerated.setStatus('current')
fsNFPPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3))
fsNFPPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 1))
fsNFPPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 2))
fsNFPPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 1, 1)).setObjects(("FS-NFPP-MIB", "fsNFPPNotifObjectsGroup"), ("FS-NFPP-MIB", "fsNFPPNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsNFPPMIBCompliance = fsNFPPMIBCompliance.setStatus('current')
fsNFPPNotifObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 2, 1)).setObjects(("FS-NFPP-MIB", "fsNFPPMessageContent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsNFPPNotifObjectsGroup = fsNFPPNotifObjectsGroup.setStatus('current')
fsNFPPNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 43, 3, 2, 2)).setObjects(("FS-NFPP-MIB", "fsNFPPMessageGenerated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsNFPPNotificationsGroup = fsNFPPNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("FS-NFPP-MIB", fsNFPPMIBCompliances=fsNFPPMIBCompliances, fsNFPPMIBNotifications=fsNFPPMIBNotifications, fsNFPPMIBCompliance=fsNFPPMIBCompliance, fsNFPPNotifObjectsGroup=fsNFPPNotifObjectsGroup, fsNFPPMIBConformance=fsNFPPMIBConformance, fsNFPPMessageGenerated=fsNFPPMessageGenerated, fsNFPPMIBGroups=fsNFPPMIBGroups, PYSNMP_MODULE_ID=fsNFPPMIB, fsNFPPMessageContent=fsNFPPMessageContent, fsNFPPMIB=fsNFPPMIB, fsNFPPMIBNotificationPrefix=fsNFPPMIBNotificationPrefix, fsNFPPNotificationsGroup=fsNFPPNotificationsGroup, fsNFPPMIBObjects=fsNFPPMIBObjects)
