#
# PySNMP MIB module MSA2000TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/MSA2000TRAPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:11 2025
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
mibBuilder.exportSymbols("MSA2000TRAPS-MIB", hp=hp, nm=nm, msaEventWarningTrap=msaEventWarningTrap, mibName=mibName, hpMSA=hpMSA, msaEventCriticalTrap=msaEventCriticalTrap, msaEventResolvedTrap=msaEventResolvedTrap, msaEventErrorTrap=msaEventErrorTrap, msaEventInfoTrap=msaEventInfoTrap)
