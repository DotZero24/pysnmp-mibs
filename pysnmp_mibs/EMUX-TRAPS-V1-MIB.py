#
# PySNMP MIB module EMUX-TRAPS-V1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/EMUX-TRAPS-V1-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
tdmLinkStatus, emux, tdmAdminStatus, e1SendStatus, e1RecvStatus = mibBuilder.importSymbols("EMUX-MIB", "tdmLinkStatus", "emux", "tdmAdminStatus", "e1SendStatus", "e1RecvStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
e1LinkChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 42926, 2) + (0,1)).setObjects(("EMUX-MIB", "e1RecvStatus"), ("EMUX-MIB", "e1SendStatus"))
tdmLinkDownV1 = NotificationType((1, 3, 6, 1, 4, 1, 42926, 2) + (0,2)).setObjects(("EMUX-MIB", "tdmAdminStatus"), ("EMUX-MIB", "tdmLinkStatus"))
tdmLinkUpV1 = NotificationType((1, 3, 6, 1, 4, 1, 42926, 2) + (0,3)).setObjects(("EMUX-MIB", "tdmAdminStatus"), ("EMUX-MIB", "tdmLinkStatus"))
trapDyingGasp = NotificationType((1, 3, 6, 1, 4, 1, 42926, 2) + (0,6)).setObjects(("EMUX-TRAPS-V1-MIB", "sysObjectID"))
mibBuilder.exportSymbols("EMUX-TRAPS-V1-MIB", trapDyingGasp=trapDyingGasp, tdmLinkDownV1=tdmLinkDownV1, e1LinkChangeV1=e1LinkChangeV1, tdmLinkUpV1=tdmLinkUpV1)
