#
# PySNMP MIB module NORTEL-OME40G-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NORTEL-OME40G-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
opterametro, = mibBuilder.importSymbols("NORTEL-OPTICAL-GENERIC-MIB", "opterametro")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nnOme40G = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 11, 3))
nnOme40G.setRevisions(('2007-02-02 00:00', '2008-02-07 00:00', '2008-05-01 00:00',))
if mibBuilder.loadTexts: nnOme40G.setLastUpdated('200805010000Z')
if mibBuilder.loadTexts: nnOme40G.setOrganization('Nortel')
ome6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 11))
mibBuilder.exportSymbols("NORTEL-OME40G-MIB", nnOme40G=nnOme40G, PYSNMP_MODULE_ID=nnOme40G, ome6500=ome6500)
