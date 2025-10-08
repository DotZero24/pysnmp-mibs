#
# PySNMP MIB module DELLTRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DELLTRAPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
connUnitEventDescr, connUnitEventId, connUnitEventType = mibBuilder.importSymbols("FCMGMT-MIB", "connUnitEventDescr", "connUnitEventId", "connUnitEventType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
dellEventInfoTrap = NotificationType((1, 3, 6, 1, 4, 1, 674) + (0,1)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
dellEventWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 674) + (0,2)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
dellEventErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 674) + (0,3)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
dellEventCriticalTrap = NotificationType((1, 3, 6, 1, 4, 1, 674) + (0,4)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
dellEventResolvedTrap = NotificationType((1, 3, 6, 1, 4, 1, 674) + (0,5)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
mibBuilder.exportSymbols("DELLTRAPS-MIB", dellEventWarningTrap=dellEventWarningTrap, dell=dell, dellEventInfoTrap=dellEventInfoTrap, dellEventErrorTrap=dellEventErrorTrap, dellEventCriticalTrap=dellEventCriticalTrap, dellEventResolvedTrap=dellEventResolvedTrap)
