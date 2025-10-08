#
# PySNMP MIB module DELL-NETWORKING-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DELL-NETWORKING-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("DELL-NETWORKING-SMI", dellNetProducts=dellNetProducts, dellNetModules=dellNetModules, dellNetCommon=dellNetCommon, PYSNMP_MODULE_ID=dellNet, dellNet=dellNet, dellNetExperiment=dellNetExperiment, dellNetMgmt=dellNetMgmt)
