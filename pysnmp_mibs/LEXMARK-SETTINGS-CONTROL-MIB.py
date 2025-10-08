#
# PySNMP MIB module LEXMARK-SETTINGS-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/lexmark/LEXMARK-SETTINGS-CONTROL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lexmarkModules, = mibBuilder.importSymbols("LEXMARK-ROOT-MIB", "lexmarkModules")
settingsMIBGroups, settingsControl, settingsMIBCompliances = mibBuilder.importSymbols("LEXMARK-SETTINGS-MIB", "settingsMIBGroups", "settingsControl", "settingsMIBCompliances")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LEXMARK-SETTINGS-CONTROL-MIB", controlMIBCompliance=controlMIBCompliance, mibLocalizeControl=mibLocalizeControl, mibWalkControl=mibWalkControl, settingsControlMibModule=settingsControlMibModule, controlGroup=controlGroup, PYSNMP_MODULE_ID=settingsControlMibModule)
