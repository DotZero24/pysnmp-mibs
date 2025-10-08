#
# PySNMP MIB module OLD-CISCO-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/OLD-CISCO-CPU-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
local, = mibBuilder.importSymbols("CISCO-SMI", "local")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lcpu = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 1))
busyPer = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 56), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: busyPer.setStatus('mandatory')
avgBusy1 = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 57), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgBusy1.setStatus('mandatory')
avgBusy5 = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 58), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avgBusy5.setStatus('mandatory')
idleCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 59), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleCount.setStatus('mandatory')
idleWired = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 1, 60), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: idleWired.setStatus('mandatory')
mibBuilder.exportSymbols("OLD-CISCO-CPU-MIB", avgBusy5=avgBusy5, lcpu=lcpu, avgBusy1=avgBusy1, idleWired=idleWired, busyPer=busyPer, idleCount=idleCount)
