#
# PySNMP MIB module FORCE10-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/force10/FORCE10-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 11:10:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
force10 = ModuleIdentity((1, 3, 6, 1, 4, 1, 6027))
force10.setRevisions(('2007-06-15 12:00', '1900-10-10 00:00',))
if mibBuilder.loadTexts: force10.setLastUpdated('200706151200Z')
if mibBuilder.loadTexts: force10.setOrganization('Dell Inc')
f10Products = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 1))
if mibBuilder.loadTexts: f10Products.setStatus('current')
f10Common = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 2))
if mibBuilder.loadTexts: f10Common.setStatus('current')
f10Mgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 3))
if mibBuilder.loadTexts: f10Mgmt.setStatus('current')
f10Modules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 4))
if mibBuilder.loadTexts: f10Modules.setStatus('current')
f10Experiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 6027, 20))
if mibBuilder.loadTexts: f10Experiment.setStatus('current')
mibBuilder.exportSymbols("FORCE10-SMI", f10Experiment=f10Experiment, PYSNMP_MODULE_ID=force10, force10=force10, f10Mgmt=f10Mgmt, f10Common=f10Common, f10Products=f10Products, f10Modules=f10Modules)
