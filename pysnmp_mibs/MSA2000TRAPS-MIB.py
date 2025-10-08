#
# PySNMP MIB module MSA2000TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/MSA2000TRAPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:25 2025
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
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpMSA = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 51))
mibName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 51, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mibName.setStatus('mandatory')
msaEventInfoTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 51) + (0,3001)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
msaEventWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 51) + (0,3002)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
msaEventErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 51) + (0,3003)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
msaEventCriticalTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 51) + (0,3004)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
msaEventResolvedTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 51) + (0,3005)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
mibBuilder.exportSymbols("MSA2000TRAPS-MIB", msaEventResolvedTrap=msaEventResolvedTrap, msaEventInfoTrap=msaEventInfoTrap, hpMSA=hpMSA, mibName=mibName, msaEventWarningTrap=msaEventWarningTrap, hp=hp, nm=nm, msaEventCriticalTrap=msaEventCriticalTrap, msaEventErrorTrap=msaEventErrorTrap)
