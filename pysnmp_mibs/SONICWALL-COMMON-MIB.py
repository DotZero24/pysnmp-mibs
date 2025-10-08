#
# PySNMP MIB module SONICWALL-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/sonicwall/SONICWALL-COMMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonicwallCommon, = mibBuilder.importSymbols("SONICWALL-SMI", "sonicwallCommon")
snwlCommonModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8741, 2, 1))
if mibBuilder.loadTexts: snwlCommonModule.setLastUpdated('201804090001Z')
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
mibBuilder.exportSymbols("SONICWALL-COMMON-MIB", snwlSysSerialNumber=snwlSysSerialNumber, snwlSysFirmwareVersion=snwlSysFirmwareVersion, snwlSysModel=snwlSysModel, snwlSys=snwlSys, PYSNMP_MODULE_ID=snwlCommonModule, snwlSysAssetNumber=snwlSysAssetNumber, snwlCommonModule=snwlCommonModule, snwlSysROMVersion=snwlSysROMVersion)
