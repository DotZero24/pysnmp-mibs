#
# PySNMP MIB module QTECH-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-SMI", qtechExperiment=qtechExperiment, switch=switch, switchMib=switchMib, qtechMgmt=qtechMgmt, qtechSwitchProducts=qtechSwitchProducts, qtechAgentCapability=qtechAgentCapability, qtech=qtech, PYSNMP_MODULE_ID=switchMib, products=products, qtechModules=qtechModules)
