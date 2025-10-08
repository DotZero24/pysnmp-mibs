#
# PySNMP MIB module BIANCA-BRICK-MIBSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bintec/BIANCA-BRICK-MIBSYS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BIANCA-BRICK-MIBSYS-MIB", sys=sys, sysPCMUnit=sysPCMUnit, sysPCMClockStatus=sysPCMClockStatus, sysPCMEntry=sysPCMEntry, sysPCMClockMaster=sysPCMClockMaster, sysPCMMasterPrio=sysPCMMasterPrio, sysPCMTable=sysPCMTable, bintec=bintec, bibo=bibo, sysPCMChanges=sysPCMChanges, sysPCMSlot=sysPCMSlot)
