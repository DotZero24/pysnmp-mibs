#
# PySNMP MIB module CENTRECOM-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/allied-old/CENTRECOM-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extSwitchMIB, = mibBuilder.importSymbols("CENTRECOM-MIB", "extSwitchMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysDescr, sysUpTime = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr", "sysUpTime")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
overheat = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,6)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
fanfailed = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,7)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
fanOK = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,8)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
invalidLoginAttempt = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,9)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
powerSupplyFail = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,10)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
powerSupplyGood = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,11)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
rpsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,12)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
rpsNoAlarm = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 12, 2) + (0,13)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"))
mibBuilder.exportSymbols("CENTRECOM-TRAP-MIB", invalidLoginAttempt=invalidLoginAttempt, overheat=overheat, powerSupplyGood=powerSupplyGood, rpsNoAlarm=rpsNoAlarm, powerSupplyFail=powerSupplyFail, fanfailed=fanfailed, rpsAlarm=rpsAlarm, fanOK=fanOK)
