#
# PySNMP MIB module SNWL-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/sonicwall/SNWL-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonicwallCommon, = mibBuilder.importSymbols("SONICWALL-SMI", "sonicwallCommon")
snwlCommonModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8741, 2, 1))
snwlCommonModule.setRevisions(('2017-01-06 00:00', '2007-11-09 00:00',))
if mibBuilder.loadTexts: snwlCommonModule.setLastUpdated('201701060000Z')
if mibBuilder.loadTexts: snwlCommonModule.setOrganization('SonicWall')
snwlSys = MibIdentifier((1, 3, 6, 1, 4, 1, 8741, 2, 1, 1))
snwlSysModel = MibScalar((1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snwlSysModel.setStatus('current')
snwlSysSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snwlSysSerialNumber.setStatus('current')
snwlSysFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snwlSysFirmwareVersion.setStatus('current')
snwlSysROMVersion = MibScalar((1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snwlSysROMVersion.setStatus('current')
snwlSysAssetNumber = MibScalar((1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snwlSysAssetNumber.setStatus('current')
mibBuilder.exportSymbols("SNWL-COMMON-MIB", snwlSysAssetNumber=snwlSysAssetNumber, snwlSysModel=snwlSysModel, snwlSysSerialNumber=snwlSysSerialNumber, PYSNMP_MODULE_ID=snwlCommonModule, snwlSysFirmwareVersion=snwlSysFirmwareVersion, snwlCommonModule=snwlCommonModule, snwlSysROMVersion=snwlSysROMVersion, snwlSys=snwlSys)
