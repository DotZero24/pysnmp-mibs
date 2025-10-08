#
# PySNMP MIB module ELECTROLINE-DHT-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DHT-STATUS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cfgSleepVoltage, = mibBuilder.importSymbols("ELECTROLINE-DHT-CONFIG-MIB", "cfgSleepVoltage")
electrolineDHT, dhtStatus = mibBuilder.importSymbols("ELECTROLINE-DHT-ROOT-MIB", "electrolineDHT", "dhtStatus")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
commonLogicalID, commonPhysAddress = mibBuilder.importSymbols("SCTE-HMS-COMMON-MIB", "commonLogicalID", "commonPhysAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
class TenthdBmV(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class TenthdB(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HundredthsVolts(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

dhtTrapAcknowledgeStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtTrapAcknowledgeStatusTable.setStatus('current')
dhtTrapAcknowledgeStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 1, 1), ).setIndexNames((0, "ELECTROLINE-DHT-STATUS-MIB", "dhtTrapAckAddressIndex"))
if mibBuilder.loadTexts: dhtTrapAcknowledgeStatusEntry.setStatus('current')
dhtTrapAckAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtTrapAckAddressIndex.setStatus('current')
dhtTrapAckValue = MibTableColumn((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtTrapAckValue.setStatus('current')
dhtNetworkAddress = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtNetworkAddress.setStatus('deprecated')
dhtHmsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3))
dhtHmsTibStatusInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1))
dhtHmsTibLineStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1))
dhtHmsTibLineRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtHmsTibLineRxBytes.setStatus('current')
dhtHmsTibLineTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtHmsTibLineTxBytes.setStatus('current')
dhtHmsTibLineTxFifoError = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtHmsTibLineTxFifoError.setStatus('current')
dhtHmsTibLineRxFifoError = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtHmsTibLineRxFifoError.setStatus('current')
dhtHmsTibLineRxLineError = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtHmsTibLineRxLineError.setStatus('current')
dhtMonitoringNetworkAddress = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtMonitoringNetworkAddress.setStatus('deprecated')
dhtInternalTemperature = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 130))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtInternalTemperature.setStatus('deprecated')
dhtDlmStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6))
fiberNodeStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7))
dhtInetNetworkAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 8), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtInetNetworkAddressType.setStatus('deprecated')
dhtInetNetworkAddress = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 9), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtInetNetworkAddress.setStatus('deprecated')
dhtInetMonitoringNetworkAddressType = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 10), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtInetMonitoringNetworkAddressType.setStatus('deprecated')
dhtInetMonitoringNetworkAddress = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 11), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtInetMonitoringNetworkAddress.setStatus('deprecated')
dhtSleepModeEvent = NotificationType((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2) + (0,10)).setObjects(("SCTE-HMS-COMMON-MIB", "commonPhysAddress"), ("SCTE-HMS-COMMON-MIB", "commonLogicalID"), ("ELECTROLINE-DHT-CONFIG-MIB", "cfgSleepVoltage"))
dhtAlarmAssuranceEvent = NotificationType((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2) + (0,11)).setObjects(("SCTE-HMS-COMMON-MIB", "commonPhysAddress"), ("SCTE-HMS-COMMON-MIB", "commonLogicalID"), ("ELECTROLINE-DHT-STATUS-MIB", "dhtTrapAckValue"))
dlmAcInputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 1), HundredthsVolts()).setUnits('Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmAcInputVoltage.setStatus('current')
dlmDhtInputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 2), HundredthsVolts()).setUnits('Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmDhtInputVoltage.setStatus('current')
dlmRxPowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 3), TenthdBmV()).setUnits('dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmRxPowerLevel.setStatus('current')
dlmTxPowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 4), TenthdBmV()).setUnits('dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmTxPowerLevel.setStatus('current')
dlmRxAttenuatorPad = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 5), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmRxAttenuatorPad.setStatus('current')
dlmTxAttenuatorPad = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 6), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: dlmTxAttenuatorPad.setStatus('current')
dhtFnOpticalReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7, 1), )
if mibBuilder.loadTexts: dhtFnOpticalReceiverTable.setStatus('mandatory')
dhtFnOpticalReceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7, 1, 1), ).setIndexNames((0, "ELECTROLINE-DHT-STATUS-MIB", "dhtFnOpticalReceiverIndex"))
if mibBuilder.loadTexts: dhtFnOpticalReceiverEntry.setStatus('mandatory')
dhtFnOpticalReceiverIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtFnOpticalReceiverIndex.setStatus('mandatory')
dhtFnOpticalReceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtFnOpticalReceiverType.setStatus('optional')
mibBuilder.exportSymbols("ELECTROLINE-DHT-STATUS-MIB", dhtHmsStatus=dhtHmsStatus, dhtHmsTibLineStatus=dhtHmsTibLineStatus, dhtHmsTibLineRxBytes=dhtHmsTibLineRxBytes, dhtInetMonitoringNetworkAddress=dhtInetMonitoringNetworkAddress, dhtInetMonitoringNetworkAddressType=dhtInetMonitoringNetworkAddressType, dhtDlmStatus=dhtDlmStatus, dhtFnOpticalReceiverIndex=dhtFnOpticalReceiverIndex, dlmTxAttenuatorPad=dlmTxAttenuatorPad, dhtHmsTibLineRxLineError=dhtHmsTibLineRxLineError, dhtHmsTibLineTxFifoError=dhtHmsTibLineTxFifoError, TenthdB=TenthdB, dhtTrapAckAddressIndex=dhtTrapAckAddressIndex, TenthdBmV=TenthdBmV, dlmDhtInputVoltage=dlmDhtInputVoltage, dhtTrapAcknowledgeStatusTable=dhtTrapAcknowledgeStatusTable, dhtHmsTibStatusInfo=dhtHmsTibStatusInfo, dhtMonitoringNetworkAddress=dhtMonitoringNetworkAddress, dlmRxPowerLevel=dlmRxPowerLevel, dhtFnOpticalReceiverEntry=dhtFnOpticalReceiverEntry, dhtHmsTibLineTxBytes=dhtHmsTibLineTxBytes, dhtInetNetworkAddress=dhtInetNetworkAddress, dhtTrapAcknowledgeStatusEntry=dhtTrapAcknowledgeStatusEntry, dhtAlarmAssuranceEvent=dhtAlarmAssuranceEvent, dhtTrapAckValue=dhtTrapAckValue, dhtInetNetworkAddressType=dhtInetNetworkAddressType, dhtSleepModeEvent=dhtSleepModeEvent, dhtNetworkAddress=dhtNetworkAddress, dhtHmsTibLineRxFifoError=dhtHmsTibLineRxFifoError, fiberNodeStatus=fiberNodeStatus, dhtFnOpticalReceiverTable=dhtFnOpticalReceiverTable, dhtFnOpticalReceiverType=dhtFnOpticalReceiverType, dlmTxPowerLevel=dlmTxPowerLevel, HundredthsVolts=HundredthsVolts, dlmRxAttenuatorPad=dlmRxAttenuatorPad, dhtInternalTemperature=dhtInternalTemperature, dlmAcInputVoltage=dlmAcInputVoltage)
