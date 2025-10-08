#
# PySNMP MIB module FS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fs = MibIdentifier((1, 3, 6, 1, 4, 1, 52642))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1))
switchMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10))
switchMib.setRevisions(('2002-03-19 00:00',))
if mibBuilder.loadTexts: switchMib.setLastUpdated('200203190000Z')
if mibBuilder.loadTexts: switchMib.setOrganization('FS.COM Inc..')
fsSwitchProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 1))
if mibBuilder.loadTexts: fsSwitchProducts.setStatus('current')
fsMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2))
if mibBuilder.loadTexts: fsMgmt.setStatus('current')
fsAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 3))
if mibBuilder.loadTexts: fsAgentCapability.setStatus('current')
fsModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 4))
if mibBuilder.loadTexts: fsModules.setStatus('current')
fsExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 5))
if mibBuilder.loadTexts: fsExperiment.setStatus('current')
mibBuilder.exportSymbols("FS-SMI", fs=fs, fsAgentCapability=fsAgentCapability, fsModules=fsModules, fsMgmt=fsMgmt, fsSwitchProducts=fsSwitchProducts, fsExperiment=fsExperiment, products=products, switchMib=switchMib, switch=switch, PYSNMP_MODULE_ID=switchMib)
