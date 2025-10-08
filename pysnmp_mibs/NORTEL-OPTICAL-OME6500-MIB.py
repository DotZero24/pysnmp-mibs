#
# PySNMP MIB module NORTEL-OPTICAL-OME6500-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NORTEL-OPTICAL-OME6500-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
opterametro, = mibBuilder.importSymbols("NORTEL-OPTICAL-GENERIC-MIB", "opterametro")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ome6500 = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 11))
ome6500.setRevisions(('2007-02-02 00:00', '2008-02-07 00:00',))
if mibBuilder.loadTexts: ome6500.setLastUpdated('200802070000Z')
if mibBuilder.loadTexts: ome6500.setOrganization('Nortel')
nnOme40G = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 11, 3))
mibBuilder.exportSymbols("NORTEL-OPTICAL-OME6500-MIB", nnOme40G=nnOme40G, ome6500=ome6500, PYSNMP_MODULE_ID=ome6500)
