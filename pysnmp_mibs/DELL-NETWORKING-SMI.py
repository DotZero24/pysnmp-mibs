#
# PySNMP MIB module DELL-NETWORKING-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dell/DELL-NETWORKING-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dellNet = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027))
dellNet.setRevisions(('2007-06-15 12:00', '1900-10-10 00:00',))
if mibBuilder.loadTexts: dellNet.setLastUpdated('200706151200Z')
if mibBuilder.loadTexts: dellNet.setOrganization('Dell Inc')
dellNetProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 1))
if mibBuilder.loadTexts: dellNetProducts.setStatus('current')
dellNetCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 2))
if mibBuilder.loadTexts: dellNetCommon.setStatus('current')
dellNetMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 3))
if mibBuilder.loadTexts: dellNetMgmt.setStatus('current')
dellNetModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 4))
if mibBuilder.loadTexts: dellNetModules.setStatus('current')
dellNetExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 20))
if mibBuilder.loadTexts: dellNetExperiment.setStatus('current')
mibBuilder.exportSymbols("DELL-NETWORKING-SMI", dellNet=dellNet, dellNetCommon=dellNetCommon, dellNetProducts=dellNetProducts, dellNetMgmt=dellNetMgmt, dellNetModules=dellNetModules, PYSNMP_MODULE_ID=dellNet, dellNetExperiment=dellNetExperiment)
