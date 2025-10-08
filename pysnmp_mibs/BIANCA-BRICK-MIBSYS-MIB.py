#
# PySNMP MIB module BIANCA-BRICK-MIBSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bintec/BIANCA-BRICK-MIBSYS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:59:02 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
sys = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17))
sysPCMTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 17, 1), )
if mibBuilder.loadTexts: sysPCMTable.setStatus('mandatory')
sysPCMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-MIBSYS-MIB", "sysPCMSlot"), (0, "BIANCA-BRICK-MIBSYS-MIB", "sysPCMUnit"))
if mibBuilder.loadTexts: sysPCMEntry.setStatus('mandatory')
sysPCMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMSlot.setStatus('mandatory')
sysPCMUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMUnit.setStatus('mandatory')
sysPCMClockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("not-ready", 2))).clone('not-ready')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMClockStatus.setStatus('mandatory')
sysPCMClockMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("candidate", 1), ("master", 2))).clone('candidate')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMClockMaster.setStatus('mandatory')
sysPCMMasterPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysPCMMasterPrio.setStatus('mandatory')
sysPCMChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysPCMChanges.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-MIBSYS-MIB", sysPCMClockStatus=sysPCMClockStatus, sysPCMUnit=sysPCMUnit, bintec=bintec, sysPCMEntry=sysPCMEntry, sysPCMChanges=sysPCMChanges, sysPCMMasterPrio=sysPCMMasterPrio, sysPCMTable=sysPCMTable, sysPCMClockMaster=sysPCMClockMaster, sys=sys, sysPCMSlot=sysPCMSlot, bibo=bibo)
