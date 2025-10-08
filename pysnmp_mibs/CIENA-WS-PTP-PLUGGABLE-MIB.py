#
# PySNMP MIB module CIENA-WS-PTP-PLUGGABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-WS-PTP-PLUGGABLE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaWsConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsConfig")
cwsPtpTxStatusEntry, = mibBuilder.importSymbols("CIENA-WS-PTP-MIB", "cwsPtpTxStatusEntry")
ChannelsNumber, PtpId = mibBuilder.importSymbols("CIENA-WS-TYPEDEFS-MIB", "ChannelsNumber", "PtpId")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CIENA-WS-PTP-PLUGGABLE-MIB", PYSNMP_MODULE_ID=cienaWsPtpPluggableMIB, cienaWsPtpPluggableObjects=cienaWsPtpPluggableObjects, cwsPtpPluggableTxStatusLossOfLock=cwsPtpPluggableTxStatusLossOfLock, cienaWsPtpPluggableMIB=cienaWsPtpPluggableMIB, cienaWsPtpPluggableCompliance=cienaWsPtpPluggableCompliance, cwsPtpPluggableTxStatusLossOfSignal=cwsPtpPluggableTxStatusLossOfSignal, cienaWsPtpPluggableGroups=cienaWsPtpPluggableGroups, cienaWsPtpPluggableCompliances=cienaWsPtpPluggableCompliances, cwsPtpAugPtpPluggableTxStatusEntry=cwsPtpAugPtpPluggableTxStatusEntry, cwsPtpAugPtpPluggableTxStatusTable=cwsPtpAugPtpPluggableTxStatusTable, cienaWsPtpPluggableGroup=cienaWsPtpPluggableGroup, cienaWsPtpPluggableConformance=cienaWsPtpPluggableConformance)
