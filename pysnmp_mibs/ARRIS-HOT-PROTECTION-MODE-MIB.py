#
# PySNMP MIB module ARRIS-HOT-PROTECTION-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/arris/ARRIS-HOT-PROTECTION-MODE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
arrisHorizOvertempProtModeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 3, 16))
arrisHorizOvertempProtModeMib.setRevisions(('2014-09-05 00:00', '2014-09-24 00:00', '2014-10-01 00:00',))
if mibBuilder.loadTexts: arrisHorizOvertempProtModeMib.setLastUpdated('201410010000Z')
if mibBuilder.loadTexts: arrisHorizOvertempProtModeMib.setOrganization('ARRIS Broadband')
arrisHorizOvertempProtModeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 16, 1))
arrisHorizOvertempProtModeMonitoring = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 16, 1, 1))
arrisHorizOvertempProtModeConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 16, 1, 2))
arrisHorizOvertempProtModeState = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("thresholdExceededHOTPTier1", 2), ("thresholdExceededHOTPTier2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: arrisHorizOvertempProtModeState.setStatus('current')
arrisHorizOvertempProtModeCount = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 16, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arrisHorizOvertempProtModeCount.setStatus('current')
arrisHorizOvertempProtModeTier1MinThreshold = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 16, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 65)).clone(37)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisHorizOvertempProtModeTier1MinThreshold.setStatus('current')
arrisHorizOvertempProtModeTier1MaxThreshold = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 16, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 65)).clone(47)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisHorizOvertempProtModeTier1MaxThreshold.setStatus('current')
arrisHorizOvertempProtModeNormalOpRecoveryTemp = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 16, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(15, 65)).clone(33)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisHorizOvertempProtModeNormalOpRecoveryTemp.setStatus('current')
mibBuilder.exportSymbols("ARRIS-HOT-PROTECTION-MODE-MIB", arrisHorizOvertempProtModeNormalOpRecoveryTemp=arrisHorizOvertempProtModeNormalOpRecoveryTemp, arrisHorizOvertempProtModeTier1MaxThreshold=arrisHorizOvertempProtModeTier1MaxThreshold, arrisHorizOvertempProtModeConfiguration=arrisHorizOvertempProtModeConfiguration, arrisHorizOvertempProtModeMib=arrisHorizOvertempProtModeMib, arrisHorizOvertempProtModeCount=arrisHorizOvertempProtModeCount, arrisHorizOvertempProtModeTier1MinThreshold=arrisHorizOvertempProtModeTier1MinThreshold, arrisHorizOvertempProtModeMibObjects=arrisHorizOvertempProtModeMibObjects, arrisHorizOvertempProtModeState=arrisHorizOvertempProtModeState, PYSNMP_MODULE_ID=arrisHorizOvertempProtModeMib, arrisHorizOvertempProtModeMonitoring=arrisHorizOvertempProtModeMonitoring)
