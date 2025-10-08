#
# PySNMP MIB module CENTRECOM-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/allied-old/CENTRECOM-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extSwitchMIB, = mibBuilder.importSymbols("CENTRECOM-MIB", "extSwitchMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, sysDescr = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime", "sysDescr")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
overheat = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,6)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
fanfailed = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,7)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
fanOK = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,8)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
invalidLoginAttempt = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,9)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
powerSupplyFail = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,10)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
powerSupplyGood = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,11)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
rpsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,12)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
rpsNoAlarm = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,13)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
mibBuilder.exportSymbols("CENTRECOM-TRAP-MIB", fanfailed=fanfailed, rpsAlarm=rpsAlarm, overheat=overheat, invalidLoginAttempt=invalidLoginAttempt, rpsNoAlarm=rpsNoAlarm, powerSupplyFail=powerSupplyFail, fanOK=fanOK, powerSupplyGood=powerSupplyGood)
