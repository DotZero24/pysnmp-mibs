#
# PySNMP MIB module WAN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/WAN-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, extremenetworks = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent", "extremenetworks")
dsx1LineStatus, dsx1LineIndex, dsx1IfIndex = mibBuilder.importSymbols("RFC1406-MIB", "dsx1LineStatus", "dsx1LineIndex", "dsx1IfIndex")
dsx3LineStatus, dsx3IfIndex, dsx3LineIndex = mibBuilder.importSymbols("RFC1407-MIB", "dsx3LineStatus", "dsx3IfIndex", "dsx3LineIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, sysDescr = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime", "sysDescr")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wanDsx1LineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,100)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
wanDsx1LossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,101)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
wanDsx1NoLossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,102)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
wanDsx3LineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,103)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
wanDsx3LossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,104)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
wanDsx3NoLossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,105)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
mibBuilder.exportSymbols("WAN-TRAP-MIB", wanDsx1LossOfMasterClock=wanDsx1LossOfMasterClock, wanDsx3NoLossOfMasterClock=wanDsx3NoLossOfMasterClock, wanDsx3LineStatusChange=wanDsx3LineStatusChange, wanDsx3LossOfMasterClock=wanDsx3LossOfMasterClock, wanDsx1LineStatusChange=wanDsx1LineStatusChange, wanDsx1NoLossOfMasterClock=wanDsx1NoLossOfMasterClock)
