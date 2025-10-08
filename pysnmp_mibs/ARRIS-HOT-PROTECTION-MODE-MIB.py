#
# PySNMP MIB module ARRIS-HOT-PROTECTION-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arris/ARRIS-HOT-PROTECTION-MODE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ARRIS-HOT-PROTECTION-MODE-MIB", arrisHorizOvertempProtModeConfiguration=arrisHorizOvertempProtModeConfiguration, arrisHorizOvertempProtModeMibObjects=arrisHorizOvertempProtModeMibObjects, arrisHorizOvertempProtModeState=arrisHorizOvertempProtModeState, arrisHorizOvertempProtModeMib=arrisHorizOvertempProtModeMib, arrisHorizOvertempProtModeCount=arrisHorizOvertempProtModeCount, arrisHorizOvertempProtModeTier1MaxThreshold=arrisHorizOvertempProtModeTier1MaxThreshold, PYSNMP_MODULE_ID=arrisHorizOvertempProtModeMib, arrisHorizOvertempProtModeMonitoring=arrisHorizOvertempProtModeMonitoring, arrisHorizOvertempProtModeTier1MinThreshold=arrisHorizOvertempProtModeTier1MinThreshold, arrisHorizOvertempProtModeNormalOpRecoveryTemp=arrisHorizOvertempProtModeNormalOpRecoveryTemp)
