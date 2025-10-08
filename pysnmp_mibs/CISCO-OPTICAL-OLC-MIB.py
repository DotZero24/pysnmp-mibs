#
# PySNMP MIB module CISCO-OPTICAL-OLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-OPTICAL-OLC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, InterfaceIndex, ifName = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex", "ifName")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TruthValue", "TextualConvention")
ciscoOpticalOlcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 1057))
ciscoOpticalOlcMIB.setRevisions(('2022-11-03 00:00',))
if mibBuilder.loadTexts: ciscoOpticalOlcMIB.setLastUpdated('202212050000Z')
if mibBuilder.loadTexts: ciscoOpticalOlcMIB.setOrganization('Cisco Systems, Inc.')
class CiscoOpticalOlcRamanTuningStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("startup", 1), ("disabled", 2), ("blocked", 3), ("failed", 4), ("measurementInProgress", 5), ("calculationInProgress", 6), ("optimizationInProgress", 7), ("tuned", 8))

class CiscoOpticalOlcRamanTuningFailReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("measurement", 1), ("calculation", 2), ("optimization", 3))

class CiscoOpticalOlcApcBlockReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("hw-fail", 1), ("edfa-shutdown", 2), ("apr-enabled", 3), ("user-disabled", 4), ("edfa-apr", 5), ("gain-estimation-in-progress", 6), ("band-failure", 7), ("partial-topology", 8), ("node-blocked", 9))

class CiscoOpticalOlcPower(TextualConvention, Integer32):
    status = 'current'

class CiscoOpticalOlcGainInDb(TextualConvention, Integer32):
    status = 'current'

class CiscoOpticalOlcPSDInDbm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-4000, 2300)

class CiscoOpticalOlcGainEstStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("blocked", 1), ("disabled", 2), ("operational", 3), ("idle", 4))

class CiscoOpticalOlcApcAgentDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("transmit", 1), ("receive", 2))

class CiscoOpticalOlcApcInternalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("blocked", 1), ("idle", 2), ("oor", 3), ("discrepancy", 4), ("correcting", 5), ("channel-startup", 6))

class CiscoOpticalOlcApcManagerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("disabled", 1), ("idle", 2), ("blocked", 3), ("working", 4), ("enable", 5), ("paused", 6))

class CiscoOpticalOlcBandStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("active", 2), ("failed", 3), ("recovering", 4))

class CiscoOpticalOlcBandPSDType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown-band-psd", 1), ("single-band-psd", 2), ("dual-band-psd", 3))

ciscoOpticalOlcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1))
cooOlcData = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1))
cooOlcSpanLossTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1), )
if mibBuilder.loadTexts: cooOlcSpanLossTable.setStatus('current')
cooOlcSpanLossEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cooOlcSpanLossEntry.setStatus('current')
cooOlcRxSpanLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 1), CiscoOpticalOlcPower()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcRxSpanLoss.setStatus('current')
cooOlcApparentRxSpanLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 2), CiscoOpticalOlcPower()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcApparentRxSpanLoss.setStatus('current')
cooOlcRxSpanLossPumpsOff = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 3), CiscoOpticalOlcPower()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcRxSpanLossPumpsOff.setStatus('current')
cooOlcRxSpanLossPumpsOffTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcRxSpanLossPumpsOffTimeStamp.setStatus('current')
cooOlcEstimatedRxSpanLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 5), CiscoOpticalOlcPower()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcEstimatedRxSpanLoss.setStatus('current')
cooOlcTxSpanLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 6), CiscoOpticalOlcPower()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcTxSpanLoss.setStatus('current')
cooOlcApparentTxSpanLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 7), CiscoOpticalOlcPower()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcApparentTxSpanLoss.setStatus('current')
cooOlcTxSpanLossPumpsOff = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 8), CiscoOpticalOlcPower()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcTxSpanLossPumpsOff.setStatus('current')
cooOlcTxSpanLossPumpsOffTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcTxSpanLossPumpsOffTimeStamp.setStatus('current')
cooOlcEstimatedTxSpanLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 1, 1, 10), CiscoOpticalOlcPower()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcEstimatedTxSpanLoss.setStatus('current')
cooOlcRamanTuningTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2), )
if mibBuilder.loadTexts: cooOlcRamanTuningTable.setStatus('current')
cooOlcRamanTuningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cooOlcRamanTuningEntry.setStatus('current')
cooOlcRamanTuningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 1), CiscoOpticalOlcRamanTuningStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcRamanTuningStatus.setStatus('current')
cooOlcRamanTuningBlockedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcRamanTuningBlockedReason.setStatus('current')
cooOlcRamanTuningFailedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 3), CiscoOpticalOlcRamanTuningFailReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcRamanTuningFailedReason.setStatus('current')
cooOlcTuningCompleteTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcTuningCompleteTimeStamp.setStatus('current')
cooOlcEstimatedMaxPossibleGain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 5), CiscoOpticalOlcGainInDb()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcEstimatedMaxPossibleGain.setStatus('current')
cooOlcRamanGainTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 6), CiscoOpticalOlcGainInDb()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcRamanGainTarget.setStatus('current')
cooOlcGainAchievedOnTuningComplete = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 2, 1, 7), CiscoOpticalOlcGainInDb()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcGainAchievedOnTuningComplete.setStatus('current')
cooOlcGainEstimatorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3), )
if mibBuilder.loadTexts: cooOlcGainEstimatorTable.setStatus('current')
cooOlcGainEstimatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cooOlcGainEstimatorEntry.setStatus('current')
cooOlcEgressGainEstStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 1), CiscoOpticalOlcGainEstStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcEgressGainEstStatus.setStatus('current')
cooOlcEgressEstimatedGain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 2), CiscoOpticalOlcGainInDb()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcEgressEstimatedGain.setStatus('current')
cooOlcEgressEstimatedGainMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcEgressEstimatedGainMode.setStatus('current')
cooOlcEgressGainEstTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcEgressGainEstTimeStamp.setStatus('current')
cooOlcIngressGainEstStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 5), CiscoOpticalOlcGainEstStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcIngressGainEstStatus.setStatus('current')
cooOlcIngressEstimatedGain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 6), CiscoOpticalOlcGainInDb()).setUnits('1/100 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcIngressEstimatedGain.setStatus('current')
cooOlcIngressEstimatedGainMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcIngressEstimatedGainMode.setStatus('current')
cooOlcIngressGainEstTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 3, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcIngressGainEstTimeStamp.setStatus('current')
cooOlcApcTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4), )
if mibBuilder.loadTexts: cooOlcApcTable.setStatus('current')
cooOlcApcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-OPTICAL-OLC-MIB", "cooOlcApcAgentDirection"))
if mibBuilder.loadTexts: cooOlcApcEntry.setStatus('current')
cooOlcApcAgentDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 1), CiscoOpticalOlcApcAgentDirection())
if mibBuilder.loadTexts: cooOlcApcAgentDirection.setStatus('current')
cooOlcApcDomainManager = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcApcDomainManager.setStatus('current')
cooOlcApcDomainManagerState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 3), CiscoOpticalOlcApcManagerState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcApcDomainManagerState.setStatus('current')
cooOlcApcDomainManagerBlockedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 4), CiscoOpticalOlcApcBlockReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcApcDomainManagerBlockedReason.setStatus('current')
cooOlcApcInternalState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 5), CiscoOpticalOlcApcInternalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcApcInternalState.setStatus('current')
cooOlcApcBlockedReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 6), CiscoOpticalOlcApcBlockReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcApcBlockedReason.setStatus('current')
cooOlcApcPsdMin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 7), CiscoOpticalOlcPSDInDbm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcApcPsdMin.setStatus('current')
cooOlcApcGainRange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cooOlcApcGainRange.setStatus('current')
cooOlcApcLastCorrectionTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 4, 1, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cooOlcApcLastCorrectionTimeStamp.setStatus('current')
cooOlcNeighbourTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 5), )
if mibBuilder.loadTexts: cooOlcNeighbourTable.setStatus('current')
cooOlcNeighbourEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cooOlcNeighbourEntry.setStatus('current')
cooOlcNbrIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcNbrIpAddr.setStatus('current')
cooOlcNbrInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 5, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcNbrInterface.setStatus('current')
cooOlcPartnerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 6), )
if mibBuilder.loadTexts: cooOlcPartnerTable.setStatus('current')
cooOlcPartnerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cooOlcPartnerEntry.setStatus('current')
cooOlcPartnerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcPartnerIpAddr.setStatus('current')
cooOlcPartnerInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 6, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcPartnerInterface.setStatus('current')
cooOlcPartnerBandLossTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7), )
if mibBuilder.loadTexts: cooOlcPartnerBandLossTable.setStatus('current')
cooOlcPartnerBandLossEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cooOlcPartnerBandLossEntry.setStatus('current')
cooOlcPathLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7, 1, 1), CiscoOpticalOlcPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcPathLoss.setStatus('current')
cooOlcPatchcordLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7, 1, 2), CiscoOpticalOlcPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcPatchcordLoss.setStatus('current')
cooOlcLossMeasurementTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 7, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cooOlcLossMeasurementTimeStamp.setStatus('current')
cooOlcBandStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8), )
if mibBuilder.loadTexts: cooOlcBandStatusTable.setStatus('current')
cooOlcBandStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-OPTICAL-OLC-MIB", "cooOlcNodeNum"))
if mibBuilder.loadTexts: cooOlcBandStatusEntry.setStatus('current')
cooOlcNodeNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1, 1), Integer32())
if mibBuilder.loadTexts: cooOlcNodeNum.setStatus('current')
cooOlcNodeRID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcNodeRID.setStatus('current')
cooOlcBandStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1, 3), CiscoOpticalOlcBandStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcBandStatus.setStatus('current')
cooOlcBandPSD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1057, 1, 1, 8, 1, 4), CiscoOpticalOlcBandPSDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cooOlcBandPSD.setStatus('current')
mibBuilder.exportSymbols("CISCO-OPTICAL-OLC-MIB", CiscoOpticalOlcPSDInDbm=CiscoOpticalOlcPSDInDbm, cooOlcApcPsdMin=cooOlcApcPsdMin, cooOlcApcTable=cooOlcApcTable, CiscoOpticalOlcRamanTuningFailReason=CiscoOpticalOlcRamanTuningFailReason, cooOlcEgressEstimatedGainMode=cooOlcEgressEstimatedGainMode, cooOlcBandStatusTable=cooOlcBandStatusTable, cooOlcPartnerIpAddr=cooOlcPartnerIpAddr, cooOlcPartnerEntry=cooOlcPartnerEntry, cooOlcApcBlockedReason=cooOlcApcBlockedReason, cooOlcNeighbourTable=cooOlcNeighbourTable, cooOlcGainEstimatorEntry=cooOlcGainEstimatorEntry, cooOlcApcDomainManagerBlockedReason=cooOlcApcDomainManagerBlockedReason, cooOlcIngressEstimatedGain=cooOlcIngressEstimatedGain, cooOlcBandPSD=cooOlcBandPSD, CiscoOpticalOlcGainInDb=CiscoOpticalOlcGainInDb, cooOlcApcEntry=cooOlcApcEntry, cooOlcBandStatusEntry=cooOlcBandStatusEntry, cooOlcApcDomainManagerState=cooOlcApcDomainManagerState, cooOlcLossMeasurementTimeStamp=cooOlcLossMeasurementTimeStamp, CiscoOpticalOlcGainEstStatus=CiscoOpticalOlcGainEstStatus, cooOlcSpanLossEntry=cooOlcSpanLossEntry, PYSNMP_MODULE_ID=ciscoOpticalOlcMIB, cooOlcApcAgentDirection=cooOlcApcAgentDirection, CiscoOpticalOlcRamanTuningStatus=CiscoOpticalOlcRamanTuningStatus, ciscoOpticalOlcMIB=ciscoOpticalOlcMIB, cooOlcEgressGainEstStatus=cooOlcEgressGainEstStatus, cooOlcTuningCompleteTimeStamp=cooOlcTuningCompleteTimeStamp, cooOlcEgressEstimatedGain=cooOlcEgressEstimatedGain, cooOlcRamanTuningBlockedReason=cooOlcRamanTuningBlockedReason, cooOlcTxSpanLossPumpsOff=cooOlcTxSpanLossPumpsOff, cooOlcEstimatedMaxPossibleGain=cooOlcEstimatedMaxPossibleGain, cooOlcNbrIpAddr=cooOlcNbrIpAddr, cooOlcRamanTuningStatus=cooOlcRamanTuningStatus, cooOlcBandStatus=cooOlcBandStatus, CiscoOpticalOlcApcBlockReason=CiscoOpticalOlcApcBlockReason, CiscoOpticalOlcApcAgentDirection=CiscoOpticalOlcApcAgentDirection, cooOlcNodeRID=cooOlcNodeRID, cooOlcApcLastCorrectionTimeStamp=cooOlcApcLastCorrectionTimeStamp, cooOlcPartnerTable=cooOlcPartnerTable, cooOlcPartnerBandLossEntry=cooOlcPartnerBandLossEntry, cooOlcSpanLossTable=cooOlcSpanLossTable, CiscoOpticalOlcBandStatus=CiscoOpticalOlcBandStatus, cooOlcIngressGainEstStatus=cooOlcIngressGainEstStatus, cooOlcApcDomainManager=cooOlcApcDomainManager, cooOlcPatchcordLoss=cooOlcPatchcordLoss, cooOlcEgressGainEstTimeStamp=cooOlcEgressGainEstTimeStamp, cooOlcPathLoss=cooOlcPathLoss, CiscoOpticalOlcApcInternalState=CiscoOpticalOlcApcInternalState, CiscoOpticalOlcBandPSDType=CiscoOpticalOlcBandPSDType, cooOlcRxSpanLossPumpsOff=cooOlcRxSpanLossPumpsOff, cooOlcRamanTuningTable=cooOlcRamanTuningTable, cooOlcRxSpanLossPumpsOffTimeStamp=cooOlcRxSpanLossPumpsOffTimeStamp, cooOlcIngressEstimatedGainMode=cooOlcIngressEstimatedGainMode, CiscoOpticalOlcPower=CiscoOpticalOlcPower, cooOlcApparentRxSpanLoss=cooOlcApparentRxSpanLoss, cooOlcGainEstimatorTable=cooOlcGainEstimatorTable, cooOlcTxSpanLossPumpsOffTimeStamp=cooOlcTxSpanLossPumpsOffTimeStamp, ciscoOpticalOlcMIBObjects=ciscoOpticalOlcMIBObjects, cooOlcApparentTxSpanLoss=cooOlcApparentTxSpanLoss, cooOlcRamanGainTarget=cooOlcRamanGainTarget, cooOlcApcGainRange=cooOlcApcGainRange, cooOlcNodeNum=cooOlcNodeNum, cooOlcData=cooOlcData, cooOlcApcInternalState=cooOlcApcInternalState, cooOlcEstimatedTxSpanLoss=cooOlcEstimatedTxSpanLoss, cooOlcIngressGainEstTimeStamp=cooOlcIngressGainEstTimeStamp, cooOlcRamanTuningEntry=cooOlcRamanTuningEntry, cooOlcNeighbourEntry=cooOlcNeighbourEntry, cooOlcTxSpanLoss=cooOlcTxSpanLoss, CiscoOpticalOlcApcManagerState=CiscoOpticalOlcApcManagerState, cooOlcRxSpanLoss=cooOlcRxSpanLoss, cooOlcPartnerInterface=cooOlcPartnerInterface, cooOlcPartnerBandLossTable=cooOlcPartnerBandLossTable, cooOlcNbrInterface=cooOlcNbrInterface, cooOlcEstimatedRxSpanLoss=cooOlcEstimatedRxSpanLoss, cooOlcRamanTuningFailedReason=cooOlcRamanTuningFailedReason, cooOlcGainAchievedOnTuningComplete=cooOlcGainAchievedOnTuningComplete)
