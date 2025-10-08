#
# PySNMP MIB module CISCO-POE-PD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-POE-PD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPoePdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 414))
ciscoPoePdMIB.setRevisions(('2004-05-05 00:00',))
if mibBuilder.loadTexts: ciscoPoePdMIB.setLastUpdated('200405050000Z')
if mibBuilder.loadTexts: ciscoPoePdMIB.setOrganization('Cisco Systems Inc.')
cpoePdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 0))
cpoePdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1))
cpoePdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2))
cpoePdInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1))
class CpoePdPowerSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("pending", 1), ("acAdaptor", 2), ("thirdParty", 3), ("classic", 4), ("midspan", 5), ("cdpNegotiated", 6), ("highPowerClassic", 7))

cpoePdCurrentPowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerLevel.setStatus('current')
cpoePdCurrentPowerSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 2), CpoePdPowerSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerSource.setStatus('current')
cpoePdSupportedPowerLevelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3), )
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelTable.setStatus('current')
cpoePdSupportedPowerLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-POE-PD-MIB", "cpoePdSupportedPowerLevel"))
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelEntry.setStatus('current')
cpoePdSupportedPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cpoePdSupportedPowerLevel.setStatus('current')
cpoePdSupportedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPower.setStatus('current')
cpoePdSupportedPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPowerMode.setStatus('current')
cpoePdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1))
cpoePdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2))
cpoePdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdMIBCompliance = cpoePdMIBCompliance.setStatus('current')
cpoePdInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdCurrentPowerLevel"), ("CISCO-POE-PD-MIB", "cpoePdCurrentPowerSource"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPower"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPowerMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdInformationGroup = cpoePdInformationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-POE-PD-MIB", cpoePdSupportedPower=cpoePdSupportedPower, cpoePdMIBCompliances=cpoePdMIBCompliances, cpoePdCurrentPowerLevel=cpoePdCurrentPowerLevel, cpoePdMIBObjects=cpoePdMIBObjects, PYSNMP_MODULE_ID=ciscoPoePdMIB, CpoePdPowerSourceType=CpoePdPowerSourceType, cpoePdInformation=cpoePdInformation, cpoePdMIBConformance=cpoePdMIBConformance, cpoePdSupportedPowerLevel=cpoePdSupportedPowerLevel, cpoePdSupportedPowerMode=cpoePdSupportedPowerMode, cpoePdMIBGroups=cpoePdMIBGroups, cpoePdMIBCompliance=cpoePdMIBCompliance, cpoePdInformationGroup=cpoePdInformationGroup, cpoePdSupportedPowerLevelTable=cpoePdSupportedPowerLevelTable, cpoePdSupportedPowerLevelEntry=cpoePdSupportedPowerLevelEntry, cpoePdCurrentPowerSource=cpoePdCurrentPowerSource, ciscoPoePdMIB=ciscoPoePdMIB, cpoePdMIBNotifications=cpoePdMIBNotifications)
