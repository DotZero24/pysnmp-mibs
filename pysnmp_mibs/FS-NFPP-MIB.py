#
# PySNMP MIB module FS-NFPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-NFPP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-NFPP-MIB", fsNFPPMIBNotificationPrefix=fsNFPPMIBNotificationPrefix, fsNFPPMIBCompliances=fsNFPPMIBCompliances, fsNFPPMessageContent=fsNFPPMessageContent, fsNFPPMIBObjects=fsNFPPMIBObjects, PYSNMP_MODULE_ID=fsNFPPMIB, fsNFPPMIB=fsNFPPMIB, fsNFPPMIBGroups=fsNFPPMIBGroups, fsNFPPMessageGenerated=fsNFPPMessageGenerated, fsNFPPMIBCompliance=fsNFPPMIBCompliance, fsNFPPNotificationsGroup=fsNFPPNotificationsGroup, fsNFPPMIBConformance=fsNFPPMIBConformance, fsNFPPNotifObjectsGroup=fsNFPPNotifObjectsGroup, fsNFPPMIBNotifications=fsNFPPMIBNotifications)
