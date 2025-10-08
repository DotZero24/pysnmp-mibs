#
# PySNMP MIB module DES7200-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES7200-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
my = MibIdentifier((1, 3, 6, 1, 4, 1, 171))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10))
switchMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97))
switchMib.setRevisions(('2002-03-19 00:00',))
if mibBuilder.loadTexts: switchMib.setLastUpdated('200203190000Z')
if mibBuilder.loadTexts: switchMib.setOrganization('D-Link Crop.')
mySwitchProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 1))
if mibBuilder.loadTexts: mySwitchProducts.setStatus('current')
myMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2))
if mibBuilder.loadTexts: myMgmt.setStatus('current')
myAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 3))
if mibBuilder.loadTexts: myAgentCapability.setStatus('current')
myModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 4))
if mibBuilder.loadTexts: myModules.setStatus('current')
myExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 5))
if mibBuilder.loadTexts: myExperiment.setStatus('current')
mibBuilder.exportSymbols("DES7200-SMI", myModules=myModules, my=my, products=products, switchMib=switchMib, mySwitchProducts=mySwitchProducts, myAgentCapability=myAgentCapability, myExperiment=myExperiment, myMgmt=myMgmt, PYSNMP_MODULE_ID=switchMib)
