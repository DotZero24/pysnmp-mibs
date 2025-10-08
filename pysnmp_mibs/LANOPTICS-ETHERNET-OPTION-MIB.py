#
# PySNMP MIB module LANOPTICS-ETHERNET-OPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/LANOPTICS-ETHERNET-OPTION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:28:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("LANOPTICS-ETHERNET-OPTION-MIB", etSlotsTable=etSlotsTable, etSlotsEntry=etSlotsEntry, etAlertsLevel=etAlertsLevel, lanOpticsDot3Monitor=lanOpticsDot3Monitor, etResetBuffers=etResetBuffers, etFullStatisticsBuffer=etFullStatisticsBuffer, etAlertsBuffer=etAlertsBuffer, pysmiFakeCol1021=pysmiFakeCol1021, lanOptics=lanOptics, etSlotPollStruct=etSlotPollStruct)
