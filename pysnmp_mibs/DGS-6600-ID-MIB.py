#
# PySNMP MIB module DGS-6600-ID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DGS-6600-ID-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_products, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dgs6600Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120))
dgs6604 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 1))
dgs6608 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 2))
dgs6600Private = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100))
dgs6600_system = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1)).setLabel("dgs6600-system")
dgs6600_l2 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 2)).setLabel("dgs6600-l2")
dgs6600_l3 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 3)).setLabel("dgs6600-l3")
dgs6600_mpls = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 4)).setLabel("dgs6600-mpls")
dgs6600_qosacl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 5)).setLabel("dgs6600-qosacl")
dgs6600_security = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 6)).setLabel("dgs6600-security")
dgs6600_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 7)).setLabel("dgs6600-mgmt")
dgs6600_others = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 8)).setLabel("dgs6600-others")
mibBuilder.exportSymbols("DGS-6600-ID-MIB", dgs6600_qosacl=dgs6600_qosacl, dgs6604=dgs6604, dgs6600_l2=dgs6600_l2, dgs6600_l3=dgs6600_l3, dgs6600Series=dgs6600Series, dgs6600_system=dgs6600_system, dgs6600_security=dgs6600_security, dgs6600_others=dgs6600_others, dgs6600Private=dgs6600Private, dgs6608=dgs6608, dgs6600_mgmt=dgs6600_mgmt, dgs6600_mpls=dgs6600_mpls)
