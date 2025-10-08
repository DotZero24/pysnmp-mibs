#
# PySNMP MIB module CISCO-OPTICAL-OLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-OPTICAL-OLC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:26:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, ifName, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifName", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-OPTICAL-OLC-MIB", cooOlcNodeNum=cooOlcNodeNum, cooOlcRamanTuningStatus=cooOlcRamanTuningStatus, cooOlcRamanTuningBlockedReason=cooOlcRamanTuningBlockedReason, cooOlcBandStatusEntry=cooOlcBandStatusEntry, CiscoOpticalOlcBandPSDType=CiscoOpticalOlcBandPSDType, cooOlcRxSpanLoss=cooOlcRxSpanLoss, cooOlcNbrInterface=cooOlcNbrInterface, CiscoOpticalOlcRamanTuningFailReason=CiscoOpticalOlcRamanTuningFailReason, cooOlcPartnerEntry=cooOlcPartnerEntry, cooOlcIngressEstimatedGain=cooOlcIngressEstimatedGain, cooOlcPathLoss=cooOlcPathLoss, cooOlcApcTable=cooOlcApcTable, cooOlcEgressEstimatedGain=cooOlcEgressEstimatedGain, cooOlcRamanTuningTable=cooOlcRamanTuningTable, cooOlcPartnerBandLossEntry=cooOlcPartnerBandLossEntry, cooOlcApcEntry=cooOlcApcEntry, cooOlcBandPSD=cooOlcBandPSD, CiscoOpticalOlcRamanTuningStatus=CiscoOpticalOlcRamanTuningStatus, cooOlcLossMeasurementTimeStamp=cooOlcLossMeasurementTimeStamp, CiscoOpticalOlcPower=CiscoOpticalOlcPower, cooOlcEgressEstimatedGainMode=cooOlcEgressEstimatedGainMode, cooOlcIngressGainEstStatus=cooOlcIngressGainEstStatus, cooOlcIngressEstimatedGainMode=cooOlcIngressEstimatedGainMode, CiscoOpticalOlcApcInternalState=CiscoOpticalOlcApcInternalState, cooOlcData=cooOlcData, cooOlcGainEstimatorTable=cooOlcGainEstimatorTable, cooOlcBandStatusTable=cooOlcBandStatusTable, cooOlcApcGainRange=cooOlcApcGainRange, CiscoOpticalOlcGainInDb=CiscoOpticalOlcGainInDb, cooOlcNbrIpAddr=cooOlcNbrIpAddr, cooOlcSpanLossEntry=cooOlcSpanLossEntry, cooOlcRamanGainTarget=cooOlcRamanGainTarget, cooOlcEgressGainEstStatus=cooOlcEgressGainEstStatus, CiscoOpticalOlcBandStatus=CiscoOpticalOlcBandStatus, cooOlcTxSpanLossPumpsOffTimeStamp=cooOlcTxSpanLossPumpsOffTimeStamp, cooOlcIngressGainEstTimeStamp=cooOlcIngressGainEstTimeStamp, cooOlcApparentRxSpanLoss=cooOlcApparentRxSpanLoss, cooOlcEstimatedTxSpanLoss=cooOlcEstimatedTxSpanLoss, cooOlcApcLastCorrectionTimeStamp=cooOlcApcLastCorrectionTimeStamp, CiscoOpticalOlcApcAgentDirection=CiscoOpticalOlcApcAgentDirection, cooOlcGainAchievedOnTuningComplete=cooOlcGainAchievedOnTuningComplete, CiscoOpticalOlcGainEstStatus=CiscoOpticalOlcGainEstStatus, cooOlcTxSpanLossPumpsOff=cooOlcTxSpanLossPumpsOff, cooOlcRxSpanLossPumpsOffTimeStamp=cooOlcRxSpanLossPumpsOffTimeStamp, CiscoOpticalOlcPSDInDbm=CiscoOpticalOlcPSDInDbm, cooOlcPartnerInterface=cooOlcPartnerInterface, ciscoOpticalOlcMIB=ciscoOpticalOlcMIB, cooOlcApcInternalState=cooOlcApcInternalState, cooOlcSpanLossTable=cooOlcSpanLossTable, cooOlcApcPsdMin=cooOlcApcPsdMin, cooOlcNodeRID=cooOlcNodeRID, cooOlcEgressGainEstTimeStamp=cooOlcEgressGainEstTimeStamp, CiscoOpticalOlcApcBlockReason=CiscoOpticalOlcApcBlockReason, cooOlcTxSpanLoss=cooOlcTxSpanLoss, cooOlcApcDomainManagerBlockedReason=cooOlcApcDomainManagerBlockedReason, cooOlcGainEstimatorEntry=cooOlcGainEstimatorEntry, cooOlcApcAgentDirection=cooOlcApcAgentDirection, cooOlcRamanTuningEntry=cooOlcRamanTuningEntry, cooOlcPartnerTable=cooOlcPartnerTable, cooOlcEstimatedMaxPossibleGain=cooOlcEstimatedMaxPossibleGain, cooOlcRxSpanLossPumpsOff=cooOlcRxSpanLossPumpsOff, PYSNMP_MODULE_ID=ciscoOpticalOlcMIB, cooOlcPatchcordLoss=cooOlcPatchcordLoss, cooOlcNeighbourTable=cooOlcNeighbourTable, ciscoOpticalOlcMIBObjects=ciscoOpticalOlcMIBObjects, cooOlcRamanTuningFailedReason=cooOlcRamanTuningFailedReason, CiscoOpticalOlcApcManagerState=CiscoOpticalOlcApcManagerState, cooOlcApparentTxSpanLoss=cooOlcApparentTxSpanLoss, cooOlcBandStatus=cooOlcBandStatus, cooOlcEstimatedRxSpanLoss=cooOlcEstimatedRxSpanLoss, cooOlcNeighbourEntry=cooOlcNeighbourEntry, cooOlcApcDomainManagerState=cooOlcApcDomainManagerState, cooOlcApcBlockedReason=cooOlcApcBlockedReason, cooOlcTuningCompleteTimeStamp=cooOlcTuningCompleteTimeStamp, cooOlcApcDomainManager=cooOlcApcDomainManager, cooOlcPartnerIpAddr=cooOlcPartnerIpAddr, cooOlcPartnerBandLossTable=cooOlcPartnerBandLossTable)
