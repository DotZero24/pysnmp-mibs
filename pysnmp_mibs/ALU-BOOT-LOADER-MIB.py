#
# PySNMP MIB module ALU-BOOT-LOADER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/ALU-BOOT-LOADER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:19:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aluCardObjs, aluChassisNotification = mibBuilder.importSymbols("ALU-CHASSIS-MIB", "aluCardObjs", "aluChassisNotification")
aluSARMIBModules, aluSARConfs = mibBuilder.importSymbols("ALU-SAR-GLOBAL-MIB", "aluSARMIBModules", "aluSARConfs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ALU-BOOT-LOADER-MIB", aluBootLoaderMIBGroups=aluBootLoaderMIBGroups, aluBootLoader7705V6v2Compliance=aluBootLoader7705V6v2Compliance, aluBootLoaderMIBConformance=aluBootLoaderMIBConformance, aluBootLoaderMIBModule=aluBootLoaderMIBModule, aluBootLoaderUpdateResult=aluBootLoaderUpdateResult, aluBootLoaderMIBCompliances=aluBootLoaderMIBCompliances, aluBootLoaderNotificationGroup=aluBootLoaderNotificationGroup, aluBootLoaderForceUpdateFile=aluBootLoaderForceUpdateFile, aluBootLoaderUpdateResultMessage=aluBootLoaderUpdateResultMessage, aluBootLoaderGroup=aluBootLoaderGroup, PYSNMP_MODULE_ID=aluBootLoaderMIBModule, aluBootLoaderUpdateFile=aluBootLoaderUpdateFile)
