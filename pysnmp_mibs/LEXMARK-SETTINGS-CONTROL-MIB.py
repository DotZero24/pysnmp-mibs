#
# PySNMP MIB module LEXMARK-SETTINGS-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/lexmark/LEXMARK-SETTINGS-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lexmarkModules, = mibBuilder.importSymbols("LEXMARK-ROOT-MIB", "lexmarkModules")
settingsMIBCompliances, settingsControl, settingsMIBGroups = mibBuilder.importSymbols("LEXMARK-SETTINGS-MIB", "settingsMIBCompliances", "settingsControl", "settingsMIBGroups")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
settingsControlMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 641, 4, 3))
settingsControlMibModule.setRevisions(('2014-03-16 12:42',))
if mibBuilder.loadTexts: settingsControlMibModule.setLastUpdated('201403161242Z')
if mibBuilder.loadTexts: settingsControlMibModule.setOrganization('Lexmark International, Inc.')
mibWalkControl = MibScalar((1, 3, 6, 1, 4, 1, 641, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("settingDefinition", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibWalkControl.setStatus('current')
mibLocalizeControl = MibScalar((1, 3, 6, 1, 4, 1, 641, 7, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibLocalizeControl.setStatus('current')
controlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 641, 7, 1, 2, 1)).setObjects(("LEXMARK-SETTINGS-CONTROL-MIB", "mibWalkControl"), ("LEXMARK-SETTINGS-CONTROL-MIB", "mibLocalizeControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    controlGroup = controlGroup.setStatus('current')
controlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 641, 7, 1, 1, 1)).setObjects(("LEXMARK-SETTINGS-CONTROL-MIB", "controlGroup"), ("LEXMARK-SETTINGS-CONTROL-MIB", "controlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    controlMIBCompliance = controlMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("LEXMARK-SETTINGS-CONTROL-MIB", PYSNMP_MODULE_ID=settingsControlMibModule, settingsControlMibModule=settingsControlMibModule, mibWalkControl=mibWalkControl, controlMIBCompliance=controlMIBCompliance, controlGroup=controlGroup, mibLocalizeControl=mibLocalizeControl)
