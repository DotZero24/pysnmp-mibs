#
# PySNMP MIB module SL-OSW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/smartoptics/SL-OSW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slService, = mibBuilder.importSymbols("SL-NE-MIB", "slService")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("SL-OSW-MIB", slOSWPortConfigTable=slOSWPortConfigTable, slOSWPm=slOSWPm, slOSWPortConfigLosThreshold=slOSWPortConfigLosThreshold, slOSWPortConfigInPowerLevel=slOSWPortConfigInPowerLevel, slOSW=slOSW, PYSNMP_MODULE_ID=slOSW, slOSWConfig=slOSWConfig, slOSWPortConfigLineIndex=slOSWPortConfigLineIndex, slOSWTraps=slOSWTraps, slOSWPortConfigEntry=slOSWPortConfigEntry)
