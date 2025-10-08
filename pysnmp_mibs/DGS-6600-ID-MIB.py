#
# PySNMP MIB module DGS-6600-ID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DGS-6600-ID-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_products, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("DGS-6600-ID-MIB", dgs6604=dgs6604, dgs6600_security=dgs6600_security, dgs6600_mgmt=dgs6600_mgmt, dgs6600_mpls=dgs6600_mpls, dgs6600_others=dgs6600_others, dgs6600_system=dgs6600_system, dgs6600_l3=dgs6600_l3, dgs6600_l2=dgs6600_l2, dgs6600Private=dgs6600Private, dgs6608=dgs6608, dgs6600_qosacl=dgs6600_qosacl, dgs6600Series=dgs6600Series)
