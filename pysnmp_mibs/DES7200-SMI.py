#
# PySNMP MIB module DES7200-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DES7200-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DES7200-SMI", my=my, myMgmt=myMgmt, switchMib=switchMib, myAgentCapability=myAgentCapability, myModules=myModules, myExperiment=myExperiment, PYSNMP_MODULE_ID=switchMib, products=products, mySwitchProducts=mySwitchProducts)
