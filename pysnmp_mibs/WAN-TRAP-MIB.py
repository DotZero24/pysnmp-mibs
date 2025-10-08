#
# PySNMP MIB module WAN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/WAN-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extremeAgent, extremenetworks = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent", "extremenetworks")
dsx1LineStatus, dsx1IfIndex, dsx1LineIndex = mibBuilder.importSymbols("RFC1406-MIB", "dsx1LineStatus", "dsx1IfIndex", "dsx1LineIndex")
dsx3IfIndex, dsx3LineStatus, dsx3LineIndex = mibBuilder.importSymbols("RFC1407-MIB", "dsx3IfIndex", "dsx3LineStatus", "dsx3LineIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysDescr, sysUpTime = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr", "sysUpTime")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wanDsx1LineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,100)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
wanDsx1LossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,101)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
wanDsx1NoLossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,102)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
wanDsx3LineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,103)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
wanDsx3LossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,104)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
wanDsx3NoLossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,105)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
mibBuilder.exportSymbols("WAN-TRAP-MIB", wanDsx1LineStatusChange=wanDsx1LineStatusChange, wanDsx3LossOfMasterClock=wanDsx3LossOfMasterClock, wanDsx3NoLossOfMasterClock=wanDsx3NoLossOfMasterClock, wanDsx1LossOfMasterClock=wanDsx1LossOfMasterClock, wanDsx1NoLossOfMasterClock=wanDsx1NoLossOfMasterClock, wanDsx3LineStatusChange=wanDsx3LineStatusChange)
