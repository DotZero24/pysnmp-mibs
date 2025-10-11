# SNMP MIB module (ELECTROLINE-DHT-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DHT-STATUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:58 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(cfgSleepVoltage,) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-CONFIG-MIB",
    "cfgSleepVoltage")

(dhtStatus,
 electrolineDHT) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-ROOT-MIB",
    "dhtStatus",
    "electrolineDHT")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(commonLogicalID,
 commonPhysAddress) = mibBuilder.importSymbols(
    "SCTE-HMS-COMMON-MIB",
    "commonLogicalID",
    "commonPhysAddress")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class TenthdBmV(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class TenthdB(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HundredthsVolts(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_DhtTrapAcknowledgeStatusTable_Object = MibTable
dhtTrapAcknowledgeStatusTable = _DhtTrapAcknowledgeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dhtTrapAcknowledgeStatusTable.setStatus("current")
_DhtTrapAcknowledgeStatusEntry_Object = MibTableRow
dhtTrapAcknowledgeStatusEntry = _DhtTrapAcknowledgeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 1, 1)
)
dhtTrapAcknowledgeStatusEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-STATUS-MIB", "dhtTrapAckAddressIndex"),
)
if mibBuilder.loadTexts:
    dhtTrapAcknowledgeStatusEntry.setStatus("current")
_DhtTrapAckAddressIndex_Type = Integer32
_DhtTrapAckAddressIndex_Object = MibTableColumn
dhtTrapAckAddressIndex = _DhtTrapAckAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 1, 1, 1),
    _DhtTrapAckAddressIndex_Type()
)
dhtTrapAckAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtTrapAckAddressIndex.setStatus("current")
_DhtTrapAckValue_Type = Integer32
_DhtTrapAckValue_Object = MibTableColumn
dhtTrapAckValue = _DhtTrapAckValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 1, 1, 2),
    _DhtTrapAckValue_Type()
)
dhtTrapAckValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtTrapAckValue.setStatus("current")
_DhtNetworkAddress_Type = IpAddress
_DhtNetworkAddress_Object = MibScalar
dhtNetworkAddress = _DhtNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 2),
    _DhtNetworkAddress_Type()
)
dhtNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtNetworkAddress.setStatus("deprecated")
_DhtHmsStatus_ObjectIdentity = ObjectIdentity
dhtHmsStatus = _DhtHmsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3)
)
_DhtHmsTibStatusInfo_ObjectIdentity = ObjectIdentity
dhtHmsTibStatusInfo = _DhtHmsTibStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1)
)
_DhtHmsTibLineStatus_ObjectIdentity = ObjectIdentity
dhtHmsTibLineStatus = _DhtHmsTibLineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1)
)
_DhtHmsTibLineRxBytes_Type = Integer32
_DhtHmsTibLineRxBytes_Object = MibScalar
dhtHmsTibLineRxBytes = _DhtHmsTibLineRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 1),
    _DhtHmsTibLineRxBytes_Type()
)
dhtHmsTibLineRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtHmsTibLineRxBytes.setStatus("current")
_DhtHmsTibLineTxBytes_Type = Integer32
_DhtHmsTibLineTxBytes_Object = MibScalar
dhtHmsTibLineTxBytes = _DhtHmsTibLineTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 2),
    _DhtHmsTibLineTxBytes_Type()
)
dhtHmsTibLineTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtHmsTibLineTxBytes.setStatus("current")
_DhtHmsTibLineTxFifoError_Type = Integer32
_DhtHmsTibLineTxFifoError_Object = MibScalar
dhtHmsTibLineTxFifoError = _DhtHmsTibLineTxFifoError_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 3),
    _DhtHmsTibLineTxFifoError_Type()
)
dhtHmsTibLineTxFifoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtHmsTibLineTxFifoError.setStatus("current")
_DhtHmsTibLineRxFifoError_Type = Integer32
_DhtHmsTibLineRxFifoError_Object = MibScalar
dhtHmsTibLineRxFifoError = _DhtHmsTibLineRxFifoError_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 4),
    _DhtHmsTibLineRxFifoError_Type()
)
dhtHmsTibLineRxFifoError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtHmsTibLineRxFifoError.setStatus("current")
_DhtHmsTibLineRxLineError_Type = Integer32
_DhtHmsTibLineRxLineError_Object = MibScalar
dhtHmsTibLineRxLineError = _DhtHmsTibLineRxLineError_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 3, 1, 1, 5),
    _DhtHmsTibLineRxLineError_Type()
)
dhtHmsTibLineRxLineError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtHmsTibLineRxLineError.setStatus("current")
_DhtMonitoringNetworkAddress_Type = IpAddress
_DhtMonitoringNetworkAddress_Object = MibScalar
dhtMonitoringNetworkAddress = _DhtMonitoringNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 4),
    _DhtMonitoringNetworkAddress_Type()
)
dhtMonitoringNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtMonitoringNetworkAddress.setStatus("deprecated")


class _DhtInternalTemperature_Type(Integer32):
    """Custom type dhtInternalTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 130),
    )


_DhtInternalTemperature_Type.__name__ = "Integer32"
_DhtInternalTemperature_Object = MibScalar
dhtInternalTemperature = _DhtInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 5),
    _DhtInternalTemperature_Type()
)
dhtInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtInternalTemperature.setStatus("deprecated")
_DhtDlmStatus_ObjectIdentity = ObjectIdentity
dhtDlmStatus = _DhtDlmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6)
)
_DlmAcInputVoltage_Type = HundredthsVolts
_DlmAcInputVoltage_Object = MibScalar
dlmAcInputVoltage = _DlmAcInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 1),
    _DlmAcInputVoltage_Type()
)
dlmAcInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmAcInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dlmAcInputVoltage.setUnits("Volts")
_DlmDhtInputVoltage_Type = HundredthsVolts
_DlmDhtInputVoltage_Object = MibScalar
dlmDhtInputVoltage = _DlmDhtInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 2),
    _DlmDhtInputVoltage_Type()
)
dlmDhtInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmDhtInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dlmDhtInputVoltage.setUnits("Volts")
_DlmRxPowerLevel_Type = TenthdBmV
_DlmRxPowerLevel_Object = MibScalar
dlmRxPowerLevel = _DlmRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 3),
    _DlmRxPowerLevel_Type()
)
dlmRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmRxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    dlmRxPowerLevel.setUnits("dBmV")
_DlmTxPowerLevel_Type = TenthdBmV
_DlmTxPowerLevel_Object = MibScalar
dlmTxPowerLevel = _DlmTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 4),
    _DlmTxPowerLevel_Type()
)
dlmTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    dlmTxPowerLevel.setUnits("dBmV")
_DlmRxAttenuatorPad_Type = TenthdB
_DlmRxAttenuatorPad_Object = MibScalar
dlmRxAttenuatorPad = _DlmRxAttenuatorPad_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 5),
    _DlmRxAttenuatorPad_Type()
)
dlmRxAttenuatorPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmRxAttenuatorPad.setStatus("current")
if mibBuilder.loadTexts:
    dlmRxAttenuatorPad.setUnits("dB")
_DlmTxAttenuatorPad_Type = TenthdB
_DlmTxAttenuatorPad_Object = MibScalar
dlmTxAttenuatorPad = _DlmTxAttenuatorPad_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 6, 6),
    _DlmTxAttenuatorPad_Type()
)
dlmTxAttenuatorPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmTxAttenuatorPad.setStatus("current")
if mibBuilder.loadTexts:
    dlmTxAttenuatorPad.setUnits("dB")
_FiberNodeStatus_ObjectIdentity = ObjectIdentity
fiberNodeStatus = _FiberNodeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7)
)
_DhtFnOpticalReceiverTable_Object = MibTable
dhtFnOpticalReceiverTable = _DhtFnOpticalReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    dhtFnOpticalReceiverTable.setStatus("mandatory")
_DhtFnOpticalReceiverEntry_Object = MibTableRow
dhtFnOpticalReceiverEntry = _DhtFnOpticalReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7, 1, 1)
)
dhtFnOpticalReceiverEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-STATUS-MIB", "dhtFnOpticalReceiverIndex"),
)
if mibBuilder.loadTexts:
    dhtFnOpticalReceiverEntry.setStatus("mandatory")
_DhtFnOpticalReceiverIndex_Type = Integer32
_DhtFnOpticalReceiverIndex_Object = MibTableColumn
dhtFnOpticalReceiverIndex = _DhtFnOpticalReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7, 1, 1, 1),
    _DhtFnOpticalReceiverIndex_Type()
)
dhtFnOpticalReceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtFnOpticalReceiverIndex.setStatus("mandatory")


class _DhtFnOpticalReceiverType_Type(DisplayString):
    """Custom type dhtFnOpticalReceiverType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DhtFnOpticalReceiverType_Type.__name__ = "DisplayString"
_DhtFnOpticalReceiverType_Object = MibTableColumn
dhtFnOpticalReceiverType = _DhtFnOpticalReceiverType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 7, 1, 1, 2),
    _DhtFnOpticalReceiverType_Type()
)
dhtFnOpticalReceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtFnOpticalReceiverType.setStatus("optional")
_DhtInetNetworkAddressType_Type = InetAddressType
_DhtInetNetworkAddressType_Object = MibScalar
dhtInetNetworkAddressType = _DhtInetNetworkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 8),
    _DhtInetNetworkAddressType_Type()
)
dhtInetNetworkAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtInetNetworkAddressType.setStatus("deprecated")
_DhtInetNetworkAddress_Type = InetAddress
_DhtInetNetworkAddress_Object = MibScalar
dhtInetNetworkAddress = _DhtInetNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 9),
    _DhtInetNetworkAddress_Type()
)
dhtInetNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtInetNetworkAddress.setStatus("deprecated")
_DhtInetMonitoringNetworkAddressType_Type = InetAddressType
_DhtInetMonitoringNetworkAddressType_Object = MibScalar
dhtInetMonitoringNetworkAddressType = _DhtInetMonitoringNetworkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 10),
    _DhtInetMonitoringNetworkAddressType_Type()
)
dhtInetMonitoringNetworkAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtInetMonitoringNetworkAddressType.setStatus("deprecated")
_DhtInetMonitoringNetworkAddress_Type = InetAddress
_DhtInetMonitoringNetworkAddress_Object = MibScalar
dhtInetMonitoringNetworkAddress = _DhtInetMonitoringNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3, 11),
    _DhtInetMonitoringNetworkAddress_Type()
)
dhtInetMonitoringNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtInetMonitoringNetworkAddress.setStatus("deprecated")

# Managed Objects groups


# Notification objects

dhtSleepModeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 0, 10)
)
dhtSleepModeEvent.setObjects(
      *(("SCTE-HMS-COMMON-MIB", "commonPhysAddress"),
        ("SCTE-HMS-COMMON-MIB", "commonLogicalID"),
        ("ELECTROLINE-DHT-CONFIG-MIB", "cfgSleepVoltage"))
)
if mibBuilder.loadTexts:
    dhtSleepModeEvent.setStatus(
        ""
    )

dhtAlarmAssuranceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 0, 11)
)
dhtAlarmAssuranceEvent.setObjects(
      *(("SCTE-HMS-COMMON-MIB", "commonPhysAddress"),
        ("SCTE-HMS-COMMON-MIB", "commonLogicalID"),
        ("ELECTROLINE-DHT-STATUS-MIB", "dhtTrapAckValue"))
)
if mibBuilder.loadTexts:
    dhtAlarmAssuranceEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DHT-STATUS-MIB",
    **{"TenthdBmV": TenthdBmV,
       "TenthdB": TenthdB,
       "HundredthsVolts": HundredthsVolts,
       "dhtSleepModeEvent": dhtSleepModeEvent,
       "dhtAlarmAssuranceEvent": dhtAlarmAssuranceEvent,
       "dhtTrapAcknowledgeStatusTable": dhtTrapAcknowledgeStatusTable,
       "dhtTrapAcknowledgeStatusEntry": dhtTrapAcknowledgeStatusEntry,
       "dhtTrapAckAddressIndex": dhtTrapAckAddressIndex,
       "dhtTrapAckValue": dhtTrapAckValue,
       "dhtNetworkAddress": dhtNetworkAddress,
       "dhtHmsStatus": dhtHmsStatus,
       "dhtHmsTibStatusInfo": dhtHmsTibStatusInfo,
       "dhtHmsTibLineStatus": dhtHmsTibLineStatus,
       "dhtHmsTibLineRxBytes": dhtHmsTibLineRxBytes,
       "dhtHmsTibLineTxBytes": dhtHmsTibLineTxBytes,
       "dhtHmsTibLineTxFifoError": dhtHmsTibLineTxFifoError,
       "dhtHmsTibLineRxFifoError": dhtHmsTibLineRxFifoError,
       "dhtHmsTibLineRxLineError": dhtHmsTibLineRxLineError,
       "dhtMonitoringNetworkAddress": dhtMonitoringNetworkAddress,
       "dhtInternalTemperature": dhtInternalTemperature,
       "dhtDlmStatus": dhtDlmStatus,
       "dlmAcInputVoltage": dlmAcInputVoltage,
       "dlmDhtInputVoltage": dlmDhtInputVoltage,
       "dlmRxPowerLevel": dlmRxPowerLevel,
       "dlmTxPowerLevel": dlmTxPowerLevel,
       "dlmRxAttenuatorPad": dlmRxAttenuatorPad,
       "dlmTxAttenuatorPad": dlmTxAttenuatorPad,
       "fiberNodeStatus": fiberNodeStatus,
       "dhtFnOpticalReceiverTable": dhtFnOpticalReceiverTable,
       "dhtFnOpticalReceiverEntry": dhtFnOpticalReceiverEntry,
       "dhtFnOpticalReceiverIndex": dhtFnOpticalReceiverIndex,
       "dhtFnOpticalReceiverType": dhtFnOpticalReceiverType,
       "dhtInetNetworkAddressType": dhtInetNetworkAddressType,
       "dhtInetNetworkAddress": dhtInetNetworkAddress,
       "dhtInetMonitoringNetworkAddressType": dhtInetMonitoringNetworkAddressType,
       "dhtInetMonitoringNetworkAddress": dhtInetMonitoringNetworkAddress}
)
