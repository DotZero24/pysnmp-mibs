#
# PySNMP MIB module SW3600PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SW3600PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_products, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dXS_3600Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 127)).setLabel("dXS-3600Series")
dXS_3600_32S = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 127, 1)).setLabel("dXS-3600-32S")
dXS_3600_16S = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 127, 2)).setLabel("dXS-3600-16S")
mibBuilder.exportSymbols("SW3600PRIMGMT-MIB", dXS_3600_32S=dXS_3600_32S, dXS_3600_16S=dXS_3600_16S, dXS_3600Series=dXS_3600Series)
