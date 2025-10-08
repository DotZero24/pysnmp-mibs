#
# PySNMP MIB module HP-CAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-CAR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
snCAR, = mibBuilder.importSymbols("HP-SN-SWITCH-GROUP-MIB", "snCAR")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snPortCARs = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1))
class PacketSource(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("input", 0), ("output", 1))

class RateLimitType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 2, 1))
    namedValues = NamedValues(("all", 3), ("quickAcc", 2), ("standardAcc", 1))

class RateLimitAction(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("continue", 1), ("drop", 2), ("precedCont", 3), ("precedXmit", 4), ("xmit", 5))

snPortCARTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1), )
if mibBuilder.loadTexts: snPortCARTable.setStatus('mandatory')
snPortCAREntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1), ).setIndexNames((0, "HP-CAR-MIB", "snPortCARifIndex"), (0, "HP-CAR-MIB", "snPortCARDirection"), (0, "HP-CAR-MIB", "snPortCARRowIndex"))
if mibBuilder.loadTexts: snPortCAREntry.setStatus('mandatory')
snPortCARifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARifIndex.setStatus('mandatory')
snPortCARDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 2), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARDirection.setStatus('mandatory')
snPortCARRowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARRowIndex.setStatus('mandatory')
snPortCARType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 4), RateLimitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARType.setStatus('mandatory')
snPortCARAccIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARAccIdx.setStatus('mandatory')
snPortCARRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARRate.setStatus('mandatory')
snPortCARLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARLimit.setStatus('mandatory')
snPortCARExtLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARExtLimit.setStatus('mandatory')
snPortCARConformAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 9), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARConformAction.setStatus('mandatory')
snPortCARExceedAction = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 10), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARExceedAction.setStatus('mandatory')
snPortCARStatSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatSwitchedPkts.setStatus('mandatory')
snPortCARStatSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatSwitchedBytes.setStatus('mandatory')
snPortCARStatFilteredPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatFilteredPkts.setStatus('mandatory')
snPortCARStatFilteredBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatFilteredBytes.setStatus('mandatory')
snPortCARStatCurBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3, 16, 1, 1, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snPortCARStatCurBurst.setStatus('mandatory')
mibBuilder.exportSymbols("HP-CAR-MIB", snPortCARs=snPortCARs, snPortCARDirection=snPortCARDirection, snPortCARRate=snPortCARRate, RateLimitType=RateLimitType, snPortCARStatFilteredBytes=snPortCARStatFilteredBytes, snPortCARStatSwitchedBytes=snPortCARStatSwitchedBytes, snPortCARLimit=snPortCARLimit, snPortCARExtLimit=snPortCARExtLimit, snPortCARStatFilteredPkts=snPortCARStatFilteredPkts, snPortCARStatCurBurst=snPortCARStatCurBurst, snPortCARConformAction=snPortCARConformAction, snPortCARAccIdx=snPortCARAccIdx, snPortCARRowIndex=snPortCARRowIndex, RateLimitAction=RateLimitAction, PacketSource=PacketSource, snPortCARifIndex=snPortCARifIndex, snPortCARType=snPortCARType, snPortCAREntry=snPortCAREntry, snPortCARStatSwitchedPkts=snPortCARStatSwitchedPkts, snPortCARTable=snPortCARTable, snPortCARExceedAction=snPortCARExceedAction)
