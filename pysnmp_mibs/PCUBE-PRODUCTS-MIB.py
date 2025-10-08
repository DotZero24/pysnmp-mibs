#
# PySNMP MIB module PCUBE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/PCUBE-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pcubeModules, pcubeProducts = mibBuilder.importSymbols("PCUBE-SMI", "pcubeModules", "pcubeProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pcubeProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655, 2, 2))
pcubeProductsMIB.setRevisions(('2002-01-14 20:00',))
if mibBuilder.loadTexts: pcubeProductsMIB.setLastUpdated('200201142000Z')
if mibBuilder.loadTexts: pcubeProductsMIB.setOrganization('Cisco Systems, Inc.')
sce100 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 1))
sce1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 2))
sce2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 1, 3))
mibBuilder.exportSymbols("PCUBE-PRODUCTS-MIB", PYSNMP_MODULE_ID=pcubeProductsMIB, sce2000=sce2000, sce100=sce100, pcubeProductsMIB=pcubeProductsMIB, sce1000=sce1000)
