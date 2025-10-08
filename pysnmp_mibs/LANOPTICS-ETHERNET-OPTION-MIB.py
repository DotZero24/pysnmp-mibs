#
# PySNMP MIB module LANOPTICS-ETHERNET-OPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/LANOPTICS-ETHERNET-OPTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
lanOpticsDot3Monitor = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 3))
etAlertsLevel = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etAlertsLevel.setStatus('mandatory')
etAlertsBuffer = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etAlertsBuffer.setStatus('mandatory')
etFullStatisticsBuffer = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etFullStatisticsBuffer.setStatus('mandatory')
etResetBuffers = MibScalar((1, 3, 6, 1, 4, 1, 224, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etResetBuffers.setStatus('mandatory')
etSlotsTable = MibTable((1, 3, 6, 1, 4, 1, 224, 3, 5), )
if mibBuilder.loadTexts: etSlotsTable.setStatus('mandatory')
pysmiFakeCol1021 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 3, 5, 1) + (1021, ), Integer32())
etSlotsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 224, 3, 5, 1), ).setIndexNames((0, "LANOPTICS-ETHERNET-OPTION-MIB", "pysmiFakeCol1021"))
if mibBuilder.loadTexts: etSlotsEntry.setStatus('mandatory')
etSlotPollStruct = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 3, 5, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etSlotPollStruct.setStatus('mandatory')
mibBuilder.exportSymbols("LANOPTICS-ETHERNET-OPTION-MIB", etSlotsEntry=etSlotsEntry, etFullStatisticsBuffer=etFullStatisticsBuffer, etResetBuffers=etResetBuffers, pysmiFakeCol1021=pysmiFakeCol1021, etAlertsBuffer=etAlertsBuffer, etSlotPollStruct=etSlotPollStruct, lanOpticsDot3Monitor=lanOpticsDot3Monitor, etAlertsLevel=etAlertsLevel, lanOptics=lanOptics, etSlotsTable=etSlotsTable)
