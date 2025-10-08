#
# PySNMP MIB module LEXMARK-SETTINGS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/lexmark/LEXMARK-SETTINGS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lexmarkModules, lexmark = mibBuilder.importSymbols("LEXMARK-ROOT-MIB", "lexmarkModules", "lexmark")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
settings = ModuleIdentity((1, 3, 6, 1, 4, 1, 641, 7))
settings.setRevisions(('2014-03-16 12:42',))
if mibBuilder.loadTexts: settings.setLastUpdated('201403161242Z')
if mibBuilder.loadTexts: settings.setOrganization('Lexmark International, Inc.')
settingsMIBAdminInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 1))
settingsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 1, 1))
settingsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 1, 2))
settingsControl = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 2))
settingsDefinition = MibIdentifier((1, 3, 6, 1, 4, 1, 641, 7, 3))
mibBuilder.exportSymbols("LEXMARK-SETTINGS-MIB", settingsControl=settingsControl, settings=settings, settingsMIBCompliances=settingsMIBCompliances, PYSNMP_MODULE_ID=settings, settingsMIBAdminInfo=settingsMIBAdminInfo, settingsMIBGroups=settingsMIBGroups, settingsDefinition=settingsDefinition)
