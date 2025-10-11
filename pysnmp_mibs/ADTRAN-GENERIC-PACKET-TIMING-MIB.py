# SNMP MIB module (ADTRAN-GENERIC-PACKET-TIMING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-PACKET-TIMING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:20 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenPacketTiming,
 adGenPacketTimingID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenPacketTiming",
    "adGenPacketTimingID")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenPacketTimingModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 32, 1)
)
if mibBuilder.loadTexts:
    adGenPacketTimingModuleIdentity.setRevisions(
        ("2011-06-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPacketTimingProv_ObjectIdentity = ObjectIdentity
adGenPacketTimingProv = _AdGenPacketTimingProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1)
)
_AdGenPacketTimingProvTable_Object = MibTable
adGenPacketTimingProvTable = _AdGenPacketTimingProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPacketTimingProvTable.setStatus("current")
_AdGenPacketTimingProvTableEntry_Object = MibTableRow
adGenPacketTimingProvTableEntry = _AdGenPacketTimingProvTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1, 1)
)
adGenPacketTimingProvTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPacketTimingProvTableEntry.setStatus("current")


class _AdGenPacketTimingMode_Type(Integer32):
    """Custom type adGenPacketTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server", 1),
          ("client", 2))
    )


_AdGenPacketTimingMode_Type.__name__ = "Integer32"
_AdGenPacketTimingMode_Object = MibTableColumn
adGenPacketTimingMode = _AdGenPacketTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1, 1, 1),
    _AdGenPacketTimingMode_Type()
)
adGenPacketTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPacketTimingMode.setStatus("current")


class _AdGenPacketTimingDscp_Type(Integer32):
    """Custom type adGenPacketTimingDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenPacketTimingDscp_Type.__name__ = "Integer32"
_AdGenPacketTimingDscp_Object = MibTableColumn
adGenPacketTimingDscp = _AdGenPacketTimingDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1, 1, 2),
    _AdGenPacketTimingDscp_Type()
)
adGenPacketTimingDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPacketTimingDscp.setStatus("current")
_AdGenPacketTimingServerIPAddress_Type = IpAddress
_AdGenPacketTimingServerIPAddress_Object = MibTableColumn
adGenPacketTimingServerIPAddress = _AdGenPacketTimingServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1, 1, 3),
    _AdGenPacketTimingServerIPAddress_Type()
)
adGenPacketTimingServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPacketTimingServerIPAddress.setStatus("current")
_AdGenPacketTimingServerMacAddress_Type = MacAddress
_AdGenPacketTimingServerMacAddress_Object = MibTableColumn
adGenPacketTimingServerMacAddress = _AdGenPacketTimingServerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1, 1, 4),
    _AdGenPacketTimingServerMacAddress_Type()
)
adGenPacketTimingServerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingServerMacAddress.setStatus("current")


class _AdGenPacketTimingType_Type(Integer32):
    """Custom type adGenPacketTimingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inband", 1),
          ("sntp", 2),
          ("sntpInband", 3))
    )


_AdGenPacketTimingType_Type.__name__ = "Integer32"
_AdGenPacketTimingType_Object = MibTableColumn
adGenPacketTimingType = _AdGenPacketTimingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1, 1, 5),
    _AdGenPacketTimingType_Type()
)
adGenPacketTimingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPacketTimingType.setStatus("current")
_AdGenPacketTimingUncorrelate_Type = TruthValue
_AdGenPacketTimingUncorrelate_Object = MibTableColumn
adGenPacketTimingUncorrelate = _AdGenPacketTimingUncorrelate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1, 1, 6),
    _AdGenPacketTimingUncorrelate_Type()
)
adGenPacketTimingUncorrelate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPacketTimingUncorrelate.setStatus("current")


class _AdGenPacketTimingServiceState_Type(Integer32):
    """Custom type adGenPacketTimingServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("oosUnassigned", 2))
    )


_AdGenPacketTimingServiceState_Type.__name__ = "Integer32"
_AdGenPacketTimingServiceState_Object = MibTableColumn
adGenPacketTimingServiceState = _AdGenPacketTimingServiceState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1, 1, 7),
    _AdGenPacketTimingServiceState_Type()
)
adGenPacketTimingServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPacketTimingServiceState.setStatus("current")
_AdGenPacketTimingErrorInfo_Type = DisplayString
_AdGenPacketTimingErrorInfo_Object = MibTableColumn
adGenPacketTimingErrorInfo = _AdGenPacketTimingErrorInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 1, 1, 1, 8),
    _AdGenPacketTimingErrorInfo_Type()
)
adGenPacketTimingErrorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingErrorInfo.setStatus("current")
_AdGenPacketTimingStatus_ObjectIdentity = ObjectIdentity
adGenPacketTimingStatus = _AdGenPacketTimingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2)
)
_AdGenPacketTimingClientStatus_ObjectIdentity = ObjectIdentity
adGenPacketTimingClientStatus = _AdGenPacketTimingClientStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1)
)
_AdGenPacketTimingStatTable_Object = MibTable
adGenPacketTimingStatTable = _AdGenPacketTimingStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPacketTimingStatTable.setStatus("current")
_AdGenPacketTimingStatTableEntry_Object = MibTableRow
adGenPacketTimingStatTableEntry = _AdGenPacketTimingStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1)
)
adGenPacketTimingStatTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPacketTimingStatTableEntry.setStatus("current")


class _AdGenPacketTimingStatRxState_Type(Integer32):
    """Custom type adGenPacketTimingStatRxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("savePhaseError", 2),
          ("wait", 3),
          ("frequencyEstimate", 4),
          ("jamPhaseBuildout", 5),
          ("locked", 7))
    )


_AdGenPacketTimingStatRxState_Type.__name__ = "Integer32"
_AdGenPacketTimingStatRxState_Object = MibTableColumn
adGenPacketTimingStatRxState = _AdGenPacketTimingStatRxState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 1),
    _AdGenPacketTimingStatRxState_Type()
)
adGenPacketTimingStatRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatRxState.setStatus("current")
_AdGenPacketTimingStatReset_Type = Unsigned32
_AdGenPacketTimingStatReset_Object = MibTableColumn
adGenPacketTimingStatReset = _AdGenPacketTimingStatReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 2),
    _AdGenPacketTimingStatReset_Type()
)
adGenPacketTimingStatReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatReset.setStatus("current")
_AdGenPacketTimingStatTxPackets_Type = Unsigned32
_AdGenPacketTimingStatTxPackets_Object = MibTableColumn
adGenPacketTimingStatTxPackets = _AdGenPacketTimingStatTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 3),
    _AdGenPacketTimingStatTxPackets_Type()
)
adGenPacketTimingStatTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatTxPackets.setStatus("current")
_AdGenPacketTimingStatRxGoodPackets_Type = Unsigned32
_AdGenPacketTimingStatRxGoodPackets_Object = MibTableColumn
adGenPacketTimingStatRxGoodPackets = _AdGenPacketTimingStatRxGoodPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 4),
    _AdGenPacketTimingStatRxGoodPackets_Type()
)
adGenPacketTimingStatRxGoodPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatRxGoodPackets.setStatus("current")
_AdGenPacketTimingStatRxBadPackets_Type = Unsigned32
_AdGenPacketTimingStatRxBadPackets_Object = MibTableColumn
adGenPacketTimingStatRxBadPackets = _AdGenPacketTimingStatRxBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 5),
    _AdGenPacketTimingStatRxBadPackets_Type()
)
adGenPacketTimingStatRxBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatRxBadPackets.setStatus("current")
_AdGenPacketTimingStatFreqOffset_Type = Unsigned32
_AdGenPacketTimingStatFreqOffset_Object = MibTableColumn
adGenPacketTimingStatFreqOffset = _AdGenPacketTimingStatFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 6),
    _AdGenPacketTimingStatFreqOffset_Type()
)
adGenPacketTimingStatFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatFreqOffset.setStatus("current")
_AdGenPacketTimingStatPDV_Type = Unsigned32
_AdGenPacketTimingStatPDV_Object = MibTableColumn
adGenPacketTimingStatPDV = _AdGenPacketTimingStatPDV_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 7),
    _AdGenPacketTimingStatPDV_Type()
)
adGenPacketTimingStatPDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatPDV.setStatus("current")
_AdGenPacketTimingStatMaxDelay_Type = Unsigned32
_AdGenPacketTimingStatMaxDelay_Object = MibTableColumn
adGenPacketTimingStatMaxDelay = _AdGenPacketTimingStatMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 8),
    _AdGenPacketTimingStatMaxDelay_Type()
)
adGenPacketTimingStatMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatMaxDelay.setStatus("current")
_AdGenPacketTimingStatMinDelay_Type = Unsigned32
_AdGenPacketTimingStatMinDelay_Object = MibTableColumn
adGenPacketTimingStatMinDelay = _AdGenPacketTimingStatMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 9),
    _AdGenPacketTimingStatMinDelay_Type()
)
adGenPacketTimingStatMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatMinDelay.setStatus("current")
_AdGenPacketTimingStatHiCapTxPackets_Type = Counter64
_AdGenPacketTimingStatHiCapTxPackets_Object = MibTableColumn
adGenPacketTimingStatHiCapTxPackets = _AdGenPacketTimingStatHiCapTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 10),
    _AdGenPacketTimingStatHiCapTxPackets_Type()
)
adGenPacketTimingStatHiCapTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatHiCapTxPackets.setStatus("current")
_AdGenPacketTimingStatHiCapRxGoodPackets_Type = Counter64
_AdGenPacketTimingStatHiCapRxGoodPackets_Object = MibTableColumn
adGenPacketTimingStatHiCapRxGoodPackets = _AdGenPacketTimingStatHiCapRxGoodPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 11),
    _AdGenPacketTimingStatHiCapRxGoodPackets_Type()
)
adGenPacketTimingStatHiCapRxGoodPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatHiCapRxGoodPackets.setStatus("current")
_AdGenPacketTimingStatHiCapRxBadPackets_Type = Counter64
_AdGenPacketTimingStatHiCapRxBadPackets_Object = MibTableColumn
adGenPacketTimingStatHiCapRxBadPackets = _AdGenPacketTimingStatHiCapRxBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 1, 1, 12),
    _AdGenPacketTimingStatHiCapRxBadPackets_Type()
)
adGenPacketTimingStatHiCapRxBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPacketTimingStatHiCapRxBadPackets.setStatus("current")
_AdGenPacketTimingResetTable_Object = MibTable
adGenPacketTimingResetTable = _AdGenPacketTimingResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 3)
)
if mibBuilder.loadTexts:
    adGenPacketTimingResetTable.setStatus("current")
_AdGenPacketTimingResetTableEntry_Object = MibTableRow
adGenPacketTimingResetTableEntry = _AdGenPacketTimingResetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 3, 1)
)
adGenPacketTimingResetTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPacketTimingResetTableEntry.setStatus("current")


class _AdGenPacketTimingResetCounters_Type(Integer32):
    """Custom type adGenPacketTimingResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenPacketTimingResetCounters_Type.__name__ = "Integer32"
_AdGenPacketTimingResetCounters_Object = MibTableColumn
adGenPacketTimingResetCounters = _AdGenPacketTimingResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 2, 1, 3, 1, 1),
    _AdGenPacketTimingResetCounters_Type()
)
adGenPacketTimingResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPacketTimingResetCounters.setStatus("current")
_AdGenPacketTimingAlarms_ObjectIdentity = ObjectIdentity
adGenPacketTimingAlarms = _AdGenPacketTimingAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 3)
)
_AdGenPacketTimingEvents_ObjectIdentity = ObjectIdentity
adGenPacketTimingEvents = _AdGenPacketTimingEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 3, 0)
)

# Managed Objects groups


# Notification objects

adGenPacketTimingClientLOPSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 3, 0, 1)
)
adGenPacketTimingClientLOPSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenPacketTimingClientLOPSClear.setStatus(
        "current"
    )

adGenPacketTimingClientLOPSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 32, 3, 0, 2)
)
adGenPacketTimingClientLOPSActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenPacketTimingClientLOPSActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-PACKET-TIMING-MIB",
    **{"adGenPacketTimingProv": adGenPacketTimingProv,
       "adGenPacketTimingProvTable": adGenPacketTimingProvTable,
       "adGenPacketTimingProvTableEntry": adGenPacketTimingProvTableEntry,
       "adGenPacketTimingMode": adGenPacketTimingMode,
       "adGenPacketTimingDscp": adGenPacketTimingDscp,
       "adGenPacketTimingServerIPAddress": adGenPacketTimingServerIPAddress,
       "adGenPacketTimingServerMacAddress": adGenPacketTimingServerMacAddress,
       "adGenPacketTimingType": adGenPacketTimingType,
       "adGenPacketTimingUncorrelate": adGenPacketTimingUncorrelate,
       "adGenPacketTimingServiceState": adGenPacketTimingServiceState,
       "adGenPacketTimingErrorInfo": adGenPacketTimingErrorInfo,
       "adGenPacketTimingStatus": adGenPacketTimingStatus,
       "adGenPacketTimingClientStatus": adGenPacketTimingClientStatus,
       "adGenPacketTimingStatTable": adGenPacketTimingStatTable,
       "adGenPacketTimingStatTableEntry": adGenPacketTimingStatTableEntry,
       "adGenPacketTimingStatRxState": adGenPacketTimingStatRxState,
       "adGenPacketTimingStatReset": adGenPacketTimingStatReset,
       "adGenPacketTimingStatTxPackets": adGenPacketTimingStatTxPackets,
       "adGenPacketTimingStatRxGoodPackets": adGenPacketTimingStatRxGoodPackets,
       "adGenPacketTimingStatRxBadPackets": adGenPacketTimingStatRxBadPackets,
       "adGenPacketTimingStatFreqOffset": adGenPacketTimingStatFreqOffset,
       "adGenPacketTimingStatPDV": adGenPacketTimingStatPDV,
       "adGenPacketTimingStatMaxDelay": adGenPacketTimingStatMaxDelay,
       "adGenPacketTimingStatMinDelay": adGenPacketTimingStatMinDelay,
       "adGenPacketTimingStatHiCapTxPackets": adGenPacketTimingStatHiCapTxPackets,
       "adGenPacketTimingStatHiCapRxGoodPackets": adGenPacketTimingStatHiCapRxGoodPackets,
       "adGenPacketTimingStatHiCapRxBadPackets": adGenPacketTimingStatHiCapRxBadPackets,
       "adGenPacketTimingResetTable": adGenPacketTimingResetTable,
       "adGenPacketTimingResetTableEntry": adGenPacketTimingResetTableEntry,
       "adGenPacketTimingResetCounters": adGenPacketTimingResetCounters,
       "adGenPacketTimingAlarms": adGenPacketTimingAlarms,
       "adGenPacketTimingEvents": adGenPacketTimingEvents,
       "adGenPacketTimingClientLOPSClear": adGenPacketTimingClientLOPSClear,
       "adGenPacketTimingClientLOPSActive": adGenPacketTimingClientLOPSActive,
       "adGenPacketTimingModuleIdentity": adGenPacketTimingModuleIdentity}
)
