#
# PySNMP MIB module SL-OSW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/smartoptics/SL-OSW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slService, = mibBuilder.importSymbols("SL-NE-MIB", "slService")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TruthValue, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "TextualConvention", "DisplayString")
slOSW = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 1, 17))
if mibBuilder.loadTexts: slOSW.setLastUpdated('0508171200Z')
if mibBuilder.loadTexts: slOSW.setOrganization('Smartoptics AS')
slOSWConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1))
slOSWPm = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 2))
slOSWTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 3))
slOSWPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1), )
if mibBuilder.loadTexts: slOSWPortConfigTable.setStatus('current')
slOSWPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1, 1), ).setIndexNames((0, "SL-OSW-MIB", "slOSWPortConfigLineIndex"))
if mibBuilder.loadTexts: slOSWPortConfigEntry.setStatus('current')
slOSWPortConfigLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOSWPortConfigLineIndex.setStatus('current')
slOSWPortConfigInPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOSWPortConfigInPowerLevel.setStatus('current')
slOSWPortConfigLosThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 17, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOSWPortConfigLosThreshold.setStatus('current')
mibBuilder.exportSymbols("SL-OSW-MIB", slOSWPortConfigTable=slOSWPortConfigTable, slOSWPortConfigLosThreshold=slOSWPortConfigLosThreshold, slOSW=slOSW, PYSNMP_MODULE_ID=slOSW, slOSWPortConfigEntry=slOSWPortConfigEntry, slOSWConfig=slOSWConfig, slOSWPortConfigInPowerLevel=slOSWPortConfigInPowerLevel, slOSWTraps=slOSWTraps, slOSWPortConfigLineIndex=slOSWPortConfigLineIndex, slOSWPm=slOSWPm)
