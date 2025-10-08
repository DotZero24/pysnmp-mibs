#
# PySNMP MIB module HP-CAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-CAR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
snCAR, = mibBuilder.importSymbols("HP-SN-SWITCH-GROUP-MIB", "snCAR")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HP-CAR-MIB", PacketSource=PacketSource, snPortCAREntry=snPortCAREntry, snPortCARs=snPortCARs, snPortCARLimit=snPortCARLimit, snPortCARStatFilteredBytes=snPortCARStatFilteredBytes, snPortCARRate=snPortCARRate, snPortCARStatSwitchedBytes=snPortCARStatSwitchedBytes, snPortCARifIndex=snPortCARifIndex, snPortCARStatCurBurst=snPortCARStatCurBurst, snPortCARAccIdx=snPortCARAccIdx, RateLimitType=RateLimitType, snPortCARConformAction=snPortCARConformAction, snPortCARDirection=snPortCARDirection, snPortCARTable=snPortCARTable, snPortCARExceedAction=snPortCARExceedAction, snPortCARRowIndex=snPortCARRowIndex, snPortCARStatSwitchedPkts=snPortCARStatSwitchedPkts, snPortCARExtLimit=snPortCARExtLimit, snPortCARType=snPortCARType, snPortCARStatFilteredPkts=snPortCARStatFilteredPkts, RateLimitAction=RateLimitAction)
