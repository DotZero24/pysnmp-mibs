#
# PySNMP MIB module ALU-BOOT-LOADER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/ALU-BOOT-LOADER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:36:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
aluChassisNotification, aluCardObjs = mibBuilder.importSymbols("ALU-CHASSIS-MIB", "aluChassisNotification", "aluCardObjs")
aluSARConfs, aluSARMIBModules = mibBuilder.importSymbols("ALU-SAR-GLOBAL-MIB", "aluSARConfs", "aluSARMIBModules")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aluBootLoaderMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 17))
aluBootLoaderMIBModule.setRevisions(('1914-06-02 00:00',))
if mibBuilder.loadTexts: aluBootLoaderMIBModule.setLastUpdated('1406020000Z')
if mibBuilder.loadTexts: aluBootLoaderMIBModule.setOrganization('Nokia')
aluBootLoaderMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27))
aluBootLoaderUpdateFile = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 180)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluBootLoaderUpdateFile.setStatus('current')
aluBootLoaderForceUpdateFile = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 180)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluBootLoaderForceUpdateFile.setStatus('current')
aluBootLoaderUpdateResultMessage = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 180)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluBootLoaderUpdateResultMessage.setStatus('current')
aluBootLoaderUpdateResult = NotificationType((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 18)).setObjects(("ALU-BOOT-LOADER-MIB", "aluBootLoaderUpdateResultMessage"))
if mibBuilder.loadTexts: aluBootLoaderUpdateResult.setStatus('current')
aluBootLoaderMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 1))
aluBootLoaderMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 2))
aluBootLoader7705V6v2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 1, 1)).setObjects(("ALU-BOOT-LOADER-MIB", "aluBootLoaderGroup"), ("ALU-BOOT-LOADER-MIB", "aluBootLoaderNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluBootLoader7705V6v2Compliance = aluBootLoader7705V6v2Compliance.setStatus('current')
aluBootLoaderGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 2, 1)).setObjects(("ALU-BOOT-LOADER-MIB", "aluBootLoaderForceUpdateFile"), ("ALU-BOOT-LOADER-MIB", "aluBootLoaderUpdateFile"), ("ALU-BOOT-LOADER-MIB", "aluBootLoaderUpdateResultMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluBootLoaderGroup = aluBootLoaderGroup.setStatus('current')
aluBootLoaderNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 2, 2)).setObjects(("ALU-BOOT-LOADER-MIB", "aluBootLoaderUpdateResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluBootLoaderNotificationGroup = aluBootLoaderNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ALU-BOOT-LOADER-MIB", aluBootLoaderUpdateResult=aluBootLoaderUpdateResult, aluBootLoader7705V6v2Compliance=aluBootLoader7705V6v2Compliance, aluBootLoaderUpdateFile=aluBootLoaderUpdateFile, aluBootLoaderMIBGroups=aluBootLoaderMIBGroups, aluBootLoaderForceUpdateFile=aluBootLoaderForceUpdateFile, PYSNMP_MODULE_ID=aluBootLoaderMIBModule, aluBootLoaderGroup=aluBootLoaderGroup, aluBootLoaderNotificationGroup=aluBootLoaderNotificationGroup, aluBootLoaderUpdateResultMessage=aluBootLoaderUpdateResultMessage, aluBootLoaderMIBModule=aluBootLoaderMIBModule, aluBootLoaderMIBCompliances=aluBootLoaderMIBCompliances, aluBootLoaderMIBConformance=aluBootLoaderMIBConformance)
