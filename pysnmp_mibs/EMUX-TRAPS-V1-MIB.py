#
# PySNMP MIB module EMUX-TRAPS-V1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/EMUX-TRAPS-V1-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
emux, e1SendStatus, tdmLinkStatus, e1RecvStatus, tdmAdminStatus = mibBuilder.importSymbols("EMUX-MIB", "emux", "e1SendStatus", "tdmLinkStatus", "e1RecvStatus", "tdmAdminStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
e1LinkChangeV1 = NotificationType((1, 3, 6, 1, 4, 1, 42926, 2) + (0,1)).setObjects(("EMUX-MIB", "e1RecvStatus"), ("EMUX-MIB", "e1SendStatus"))
tdmLinkDownV1 = NotificationType((1, 3, 6, 1, 4, 1, 42926, 2) + (0,2)).setObjects(("EMUX-MIB", "tdmAdminStatus"), ("EMUX-MIB", "tdmLinkStatus"))
tdmLinkUpV1 = NotificationType((1, 3, 6, 1, 4, 1, 42926, 2) + (0,3)).setObjects(("EMUX-MIB", "tdmAdminStatus"), ("EMUX-MIB", "tdmLinkStatus"))
trapDyingGasp = NotificationType((1, 3, 6, 1, 4, 1, 42926, 2) + (0,6)).setObjects(("EMUX-TRAPS-V1-MIB", "sysObjectID"))
mibBuilder.exportSymbols("EMUX-TRAPS-V1-MIB", tdmLinkDownV1=tdmLinkDownV1, e1LinkChangeV1=e1LinkChangeV1, tdmLinkUpV1=tdmLinkUpV1, trapDyingGasp=trapDyingGasp)
