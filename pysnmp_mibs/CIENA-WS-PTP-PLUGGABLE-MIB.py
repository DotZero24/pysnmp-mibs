#
# PySNMP MIB module CIENA-WS-PTP-PLUGGABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-WS-PTP-PLUGGABLE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaWsConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsConfig")
cwsPtpTxStatusEntry, = mibBuilder.importSymbols("CIENA-WS-PTP-MIB", "cwsPtpTxStatusEntry")
ChannelsNumber, PtpId = mibBuilder.importSymbols("CIENA-WS-TYPEDEFS-MIB", "ChannelsNumber", "PtpId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cienaWsPtpPluggableMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10))
cienaWsPtpPluggableMIB.setRevisions(('2017-02-28 00:00', '2016-12-12 00:00', '2016-06-14 00:00', '2015-04-29 00:00',))
if mibBuilder.loadTexts: cienaWsPtpPluggableMIB.setLastUpdated('201702280000Z')
if mibBuilder.loadTexts: cienaWsPtpPluggableMIB.setOrganization('Ciena Corporation')
cwsPtpAugPtpPluggableTxStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 3), )
if mibBuilder.loadTexts: cwsPtpAugPtpPluggableTxStatusTable.setStatus('current')
cwsPtpAugPtpPluggableTxStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 3, 1), )
cwsPtpTxStatusEntry.registerAugmentions(("CIENA-WS-PTP-PLUGGABLE-MIB", "cwsPtpAugPtpPluggableTxStatusEntry"))
cwsPtpAugPtpPluggableTxStatusEntry.setIndexNames(*cwsPtpTxStatusEntry.getIndexNames())
if mibBuilder.loadTexts: cwsPtpAugPtpPluggableTxStatusEntry.setStatus('current')
cwsPtpPluggableTxStatusLossOfSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 3, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPtpPluggableTxStatusLossOfSignal.setStatus('current')
cwsPtpPluggableTxStatusLossOfLock = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsPtpPluggableTxStatusLossOfLock.setStatus('current')
cienaWsPtpPluggableObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 1))
cienaWsPtpPluggableConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2))
cienaWsPtpPluggableGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2, 1))
cienaWsPtpPluggableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2, 1, 1)).setObjects(("CIENA-WS-PTP-PLUGGABLE-MIB", "cwsPtpPluggableTxStatusLossOfSignal"), ("CIENA-WS-PTP-PLUGGABLE-MIB", "cwsPtpPluggableTxStatusLossOfLock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsPtpPluggableGroup = cienaWsPtpPluggableGroup.setStatus('current')
cienaWsPtpPluggableCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2, 2))
cienaWsPtpPluggableCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1271, 3, 4, 10, 2, 2, 1)).setObjects(("CIENA-WS-PTP-PLUGGABLE-MIB", "cienaWsPtpPluggableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsPtpPluggableCompliance = cienaWsPtpPluggableCompliance.setStatus('current')
mibBuilder.exportSymbols("CIENA-WS-PTP-PLUGGABLE-MIB", cienaWsPtpPluggableConformance=cienaWsPtpPluggableConformance, cwsPtpPluggableTxStatusLossOfLock=cwsPtpPluggableTxStatusLossOfLock, cwsPtpAugPtpPluggableTxStatusEntry=cwsPtpAugPtpPluggableTxStatusEntry, cienaWsPtpPluggableCompliances=cienaWsPtpPluggableCompliances, cienaWsPtpPluggableMIB=cienaWsPtpPluggableMIB, cienaWsPtpPluggableObjects=cienaWsPtpPluggableObjects, cienaWsPtpPluggableGroup=cienaWsPtpPluggableGroup, cienaWsPtpPluggableCompliance=cienaWsPtpPluggableCompliance, PYSNMP_MODULE_ID=cienaWsPtpPluggableMIB, cwsPtpPluggableTxStatusLossOfSignal=cwsPtpPluggableTxStatusLossOfSignal, cwsPtpAugPtpPluggableTxStatusTable=cwsPtpAugPtpPluggableTxStatusTable, cienaWsPtpPluggableGroups=cienaWsPtpPluggableGroups)
