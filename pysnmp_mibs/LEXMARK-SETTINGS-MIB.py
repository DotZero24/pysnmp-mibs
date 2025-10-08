#
# PySNMP MIB module LEXMARK-SETTINGS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/lexmark/LEXMARK-SETTINGS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lexmark, lexmarkModules = mibBuilder.importSymbols("LEXMARK-ROOT-MIB", "lexmark", "lexmarkModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
settings = ModuleIdentity((1, 3, 6, 1, 4, 1, 641, 7))
settings.setRevisions(('2014-03-16 12:42',))
if mibBuilder.loadTexts: settings.setLastUpdated('201403161242Z')
if mibBuilder.loadTexts: settings.setOrganization('Lexmark International, Inc.')
settingsMIBAdminInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 1))
settingsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 1, 1))
settingsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 1, 2))
settingsControl = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 2))
settingsDefinition = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 3))
mibBuilder.exportSymbols("LEXMARK-SETTINGS-MIB", settingsMIBAdminInfo=settingsMIBAdminInfo, PYSNMP_MODULE_ID=settings, settingsControl=settingsControl, settings=settings, settingsMIBCompliances=settingsMIBCompliances, settingsMIBGroups=settingsMIBGroups, settingsDefinition=settingsDefinition)
