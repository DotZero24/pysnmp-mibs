#
# PySNMP MIB module SEAGATESYSTEMTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/seagate/SEAGATESYSTEMTRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
connUnitEventDescr, connUnitEventType, connUnitEventId = mibBuilder.importSymbols("FCMGMT-MIB", "connUnitEventDescr", "connUnitEventType", "connUnitEventId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
seagateSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 347))
seagateEventInfoTrap = NotificationType((1, 3, 6, 1, 4, 1, 347) + (0,1)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
seagateEventWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 347) + (0,2)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
seagateEventErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 347) + (0,3)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
seagateEventCriticalTrap = NotificationType((1, 3, 6, 1, 4, 1, 347) + (0,4)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
seagateEventResolvedTrap = NotificationType((1, 3, 6, 1, 4, 1, 347) + (0,5)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
mibBuilder.exportSymbols("SEAGATESYSTEMTRAP-MIB", seagateEventInfoTrap=seagateEventInfoTrap, seagateEventCriticalTrap=seagateEventCriticalTrap, seagateEventResolvedTrap=seagateEventResolvedTrap, seagateEventErrorTrap=seagateEventErrorTrap, seagateSystems=seagateSystems, seagateEventWarningTrap=seagateEventWarningTrap)
