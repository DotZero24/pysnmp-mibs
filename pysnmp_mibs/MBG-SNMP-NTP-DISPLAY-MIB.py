#
# PySNMP MIB module MBG-SNMP-NTP-DISPLAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/meinberg/MBG-SNMP-NTP-DISPLAY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mbgSnmpRoot, = mibBuilder.importSymbols("MBG-SNMP-ROOT-MIB", "mbgSnmpRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mbgNtpDisp = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 20))
mbgNtpDispInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 20, 2))
mbgNtpDispTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 20, 3))
mbgNtpDispClockType = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispClockType.setStatus('mandatory')
mbgNtpDispClockTypeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispClockTypeVal.setStatus('mandatory')
mbgNtpDispMode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispMode.setStatus('mandatory')
mbgNtpDispModeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispModeVal.setStatus('mandatory')
mbgNtpDispState = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispState.setStatus('mandatory')
mbgNtpDispTrapBoot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 20, 3) + (0,1))
mbgNtpDispTrapSync = NotificationType((1, 3, 6, 1, 4, 1, 5597, 20, 3) + (0,2))
mbgNtpDispTrapNotSync = NotificationType((1, 3, 6, 1, 4, 1, 5597, 20, 3) + (0,3))
mbgNtpDispTrapTestNotification = NotificationType((1, 3, 6, 1, 4, 1, 5597, 20, 3) + (0,4))
mibBuilder.exportSymbols("MBG-SNMP-NTP-DISPLAY-MIB", mbgNtpDispTrapTestNotification=mbgNtpDispTrapTestNotification, mbgNtpDisp=mbgNtpDisp, mbgNtpDispClockTypeVal=mbgNtpDispClockTypeVal, mbgNtpDispTrapNotSync=mbgNtpDispTrapNotSync, mbgNtpDispTraps=mbgNtpDispTraps, mbgNtpDispMode=mbgNtpDispMode, mbgNtpDispModeVal=mbgNtpDispModeVal, mbgNtpDispState=mbgNtpDispState, mbgNtpDispInfo=mbgNtpDispInfo, mbgNtpDispClockType=mbgNtpDispClockType, mbgNtpDispTrapBoot=mbgNtpDispTrapBoot, mbgNtpDispTrapSync=mbgNtpDispTrapSync)
