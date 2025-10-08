#
# PySNMP MIB module QTECH-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtech = MibIdentifier((1, 3, 6, 1, 4, 1, 27514))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1))
switchMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10))
switchMib.setRevisions(('2002-03-19 00:00',))
if mibBuilder.loadTexts: switchMib.setLastUpdated('200203190000Z')
if mibBuilder.loadTexts: switchMib.setOrganization('Qtech Networks Co.,Ltd.')
qtechSwitchProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 1))
if mibBuilder.loadTexts: qtechSwitchProducts.setStatus('current')
qtechMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2))
if mibBuilder.loadTexts: qtechMgmt.setStatus('current')
qtechAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 3))
if mibBuilder.loadTexts: qtechAgentCapability.setStatus('current')
qtechModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 4))
if mibBuilder.loadTexts: qtechModules.setStatus('current')
qtechExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 5))
if mibBuilder.loadTexts: qtechExperiment.setStatus('current')
mibBuilder.exportSymbols("QTECH-SMI", qtechMgmt=qtechMgmt, qtechExperiment=qtechExperiment, products=products, switchMib=switchMib, qtechSwitchProducts=qtechSwitchProducts, qtechModules=qtechModules, switch=switch, qtech=qtech, PYSNMP_MODULE_ID=switchMib, qtechAgentCapability=qtechAgentCapability)
