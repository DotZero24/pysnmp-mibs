#
# PySNMP MIB module NTNTECH-NMS-TRAPS-V1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zhone/NTNTECH-NMS-TRAPS-V1-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mumStaFanState, = mibBuilder.importSymbols("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState")
ifStaType, ifStaSlotIndex = mibBuilder.importSymbols("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType", "ifStaSlotIndex")
ntntechNMSTraps, = mibBuilder.importSymbols("NTNTECH-ROOT-MIB", "ntntechNMSTraps")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
envFanTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1001)).setLabel("envFanTrap-v1").setObjects(("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState"))
envTempNormal_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1002)).setLabel("envTempNormal-v1")
envTempExceeded_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1003)).setLabel("envTempExceeded-v1")
invIfModPresentTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,2001)).setLabel("invIfModPresentTrap-v1").setObjects(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"), ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
invIfModRemovedTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,2002)).setLabel("invIfModRemovedTrap-v1").setObjects(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"), ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
mibBuilder.exportSymbols("NTNTECH-NMS-TRAPS-V1-MIB", invIfModPresentTrap_v1=invIfModPresentTrap_v1, invIfModRemovedTrap_v1=invIfModRemovedTrap_v1, envTempExceeded_v1=envTempExceeded_v1, envFanTrap_v1=envFanTrap_v1, envTempNormal_v1=envTempNormal_v1)
