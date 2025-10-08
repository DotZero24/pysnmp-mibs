#
# PySNMP MIB module NTNTECH-NMS-TRAPS-V1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zhone/NTNTECH-NMS-TRAPS-V1-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mumStaFanState, = mibBuilder.importSymbols("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState")
ifStaType, ifStaSlotIndex = mibBuilder.importSymbols("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType", "ifStaSlotIndex")
ntntechNMSTraps, = mibBuilder.importSymbols("NTNTECH-ROOT-MIB", "ntntechNMSTraps")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
envFanTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1001)).setLabel("envFanTrap-v1").setObjects(("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState"))
envTempNormal_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1002)).setLabel("envTempNormal-v1")
envTempExceeded_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,1003)).setLabel("envTempExceeded-v1")
invIfModPresentTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,2001)).setLabel("invIfModPresentTrap-v1").setObjects(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"), ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
invIfModRemovedTrap_v1 = NotificationType((1, 3, 6, 1, 4, 1, 8059, 1, 3) + (0,2002)).setLabel("invIfModRemovedTrap-v1").setObjects(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"), ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
mibBuilder.exportSymbols("NTNTECH-NMS-TRAPS-V1-MIB", envTempExceeded_v1=envTempExceeded_v1, invIfModPresentTrap_v1=invIfModPresentTrap_v1, envTempNormal_v1=envTempNormal_v1, invIfModRemovedTrap_v1=invIfModRemovedTrap_v1, envFanTrap_v1=envFanTrap_v1)
