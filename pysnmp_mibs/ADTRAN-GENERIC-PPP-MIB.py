# SNMP MIB module (ADTRAN-GENERIC-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-PPP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:50 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenPpp,
 adGenPppID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenPpp",
    "adGenPppID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenPppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 31, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPppMIBObjects_ObjectIdentity = ObjectIdentity
adGenPppMIBObjects = _AdGenPppMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1)
)
_AdGenPppLinkObjects_ObjectIdentity = ObjectIdentity
adGenPppLinkObjects = _AdGenPppLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1)
)
_AdGenPppLinkProv_ObjectIdentity = ObjectIdentity
adGenPppLinkProv = _AdGenPppLinkProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 1)
)
_AdGenPppLinkAlarmProvTable_Object = MibTable
adGenPppLinkAlarmProvTable = _AdGenPppLinkAlarmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPppLinkAlarmProvTable.setStatus("current")
_AdGenPppLinkAlarmProvEntry_Object = MibTableRow
adGenPppLinkAlarmProvEntry = _AdGenPppLinkAlarmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 1, 1, 1)
)
adGenPppLinkAlarmProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenPppLinkAlarmProvEntry.setStatus("current")


class _AdGenPppLinkAlarmProvLCPAlarmSeverity_Type(Integer32):
    """Custom type adGenPppLinkAlarmProvLCPAlarmSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenPppLinkAlarmProvLCPAlarmSeverity_Type.__name__ = "Integer32"
_AdGenPppLinkAlarmProvLCPAlarmSeverity_Object = MibTableColumn
adGenPppLinkAlarmProvLCPAlarmSeverity = _AdGenPppLinkAlarmProvLCPAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 1, 1, 1, 1),
    _AdGenPppLinkAlarmProvLCPAlarmSeverity_Type()
)
adGenPppLinkAlarmProvLCPAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppLinkAlarmProvLCPAlarmSeverity.setStatus("current")


class _AdGenPppLinkAlarmProvLCPAlarmSuppression_Type(Integer32):
    """Custom type adGenPppLinkAlarmProvLCPAlarmSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdGenPppLinkAlarmProvLCPAlarmSuppression_Type.__name__ = "Integer32"
_AdGenPppLinkAlarmProvLCPAlarmSuppression_Object = MibTableColumn
adGenPppLinkAlarmProvLCPAlarmSuppression = _AdGenPppLinkAlarmProvLCPAlarmSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 1, 1, 1, 2),
    _AdGenPppLinkAlarmProvLCPAlarmSuppression_Type()
)
adGenPppLinkAlarmProvLCPAlarmSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppLinkAlarmProvLCPAlarmSuppression.setStatus("current")


class _AdGenPppLinkAlarmProvLCPAlarmEnable_Type(TruthValue):
    """Custom type adGenPppLinkAlarmProvLCPAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenPppLinkAlarmProvLCPAlarmEnable_Type.__name__ = "TruthValue"
_AdGenPppLinkAlarmProvLCPAlarmEnable_Object = MibTableColumn
adGenPppLinkAlarmProvLCPAlarmEnable = _AdGenPppLinkAlarmProvLCPAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 1, 1, 1, 3),
    _AdGenPppLinkAlarmProvLCPAlarmEnable_Type()
)
adGenPppLinkAlarmProvLCPAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppLinkAlarmProvLCPAlarmEnable.setStatus("current")
_AdGenPppLinkStatus_ObjectIdentity = ObjectIdentity
adGenPppLinkStatus = _AdGenPppLinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 2)
)
_AdGenPppLinkStatusTable_Object = MibTable
adGenPppLinkStatusTable = _AdGenPppLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenPppLinkStatusTable.setStatus("current")
_AdGenPppLinkStatusEntry_Object = MibTableRow
adGenPppLinkStatusEntry = _AdGenPppLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 2, 1, 1)
)
adGenPppLinkStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppLinkStatusEntry.setStatus("current")


class _AdGenPppLinkOperStatus_Type(Integer32):
    """Custom type adGenPppLinkOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opened", 1),
          ("notopened", 2))
    )


_AdGenPppLinkOperStatus_Type.__name__ = "Integer32"
_AdGenPppLinkOperStatus_Object = MibTableColumn
adGenPppLinkOperStatus = _AdGenPppLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 2, 1, 1, 1),
    _AdGenPppLinkOperStatus_Type()
)
adGenPppLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkOperStatus.setStatus("current")


class _AdGenPppLinkCurrentLCPState_Type(Integer32):
    """Custom type adGenPppLinkCurrentLCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("reqsent", 7),
          ("ackrcvd", 8),
          ("acksent", 9),
          ("opened", 10))
    )


_AdGenPppLinkCurrentLCPState_Type.__name__ = "Integer32"
_AdGenPppLinkCurrentLCPState_Object = MibTableColumn
adGenPppLinkCurrentLCPState = _AdGenPppLinkCurrentLCPState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 2, 1, 1, 2),
    _AdGenPppLinkCurrentLCPState_Type()
)
adGenPppLinkCurrentLCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentLCPState.setStatus("current")
_AdGenPppLinkNegotiatedStatus_Type = DisplayString
_AdGenPppLinkNegotiatedStatus_Object = MibTableColumn
adGenPppLinkNegotiatedStatus = _AdGenPppLinkNegotiatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 2, 1, 1, 3),
    _AdGenPppLinkNegotiatedStatus_Type()
)
adGenPppLinkNegotiatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkNegotiatedStatus.setStatus("current")
_AdGenPppLinkPerfStats_ObjectIdentity = ObjectIdentity
adGenPppLinkPerfStats = _AdGenPppLinkPerfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3)
)
_AdGenPppLinkPerfTable_Object = MibTable
adGenPppLinkPerfTable = _AdGenPppLinkPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adGenPppLinkPerfTable.setStatus("current")
_AdGenPppLinkPerfEntry_Object = MibTableRow
adGenPppLinkPerfEntry = _AdGenPppLinkPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1)
)
adGenPppLinkPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppLinkPerfEntry.setStatus("current")
_AdGenPppLinkInOctets_Type = Counter32
_AdGenPppLinkInOctets_Object = MibTableColumn
adGenPppLinkInOctets = _AdGenPppLinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 1),
    _AdGenPppLinkInOctets_Type()
)
adGenPppLinkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkInOctets.setStatus("current")
_AdGenPppLinkInGoodOctets_Type = Counter32
_AdGenPppLinkInGoodOctets_Object = MibTableColumn
adGenPppLinkInGoodOctets = _AdGenPppLinkInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 2),
    _AdGenPppLinkInGoodOctets_Type()
)
adGenPppLinkInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkInGoodOctets.setStatus("current")
_AdGenPppLinkInPkts_Type = Counter32
_AdGenPppLinkInPkts_Object = MibTableColumn
adGenPppLinkInPkts = _AdGenPppLinkInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 3),
    _AdGenPppLinkInPkts_Type()
)
adGenPppLinkInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkInPkts.setStatus("current")
_AdGenPppLinkInDiscards_Type = Counter32
_AdGenPppLinkInDiscards_Object = MibTableColumn
adGenPppLinkInDiscards = _AdGenPppLinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 4),
    _AdGenPppLinkInDiscards_Type()
)
adGenPppLinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkInDiscards.setStatus("current")
_AdGenPppLinkInErrors_Type = Counter32
_AdGenPppLinkInErrors_Object = MibTableColumn
adGenPppLinkInErrors = _AdGenPppLinkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 5),
    _AdGenPppLinkInErrors_Type()
)
adGenPppLinkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkInErrors.setStatus("current")
_AdGenPppLinkOutOctets_Type = Counter32
_AdGenPppLinkOutOctets_Object = MibTableColumn
adGenPppLinkOutOctets = _AdGenPppLinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 6),
    _AdGenPppLinkOutOctets_Type()
)
adGenPppLinkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkOutOctets.setStatus("current")
_AdGenPppLinkOutPkts_Type = Counter32
_AdGenPppLinkOutPkts_Object = MibTableColumn
adGenPppLinkOutPkts = _AdGenPppLinkOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 7),
    _AdGenPppLinkOutPkts_Type()
)
adGenPppLinkOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkOutPkts.setStatus("current")
_AdGenPppLinkOutDiscards_Type = Counter32
_AdGenPppLinkOutDiscards_Object = MibTableColumn
adGenPppLinkOutDiscards = _AdGenPppLinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 8),
    _AdGenPppLinkOutDiscards_Type()
)
adGenPppLinkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkOutDiscards.setStatus("current")
_AdGenPppLinkOutErrors_Type = Counter32
_AdGenPppLinkOutErrors_Object = MibTableColumn
adGenPppLinkOutErrors = _AdGenPppLinkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 9),
    _AdGenPppLinkOutErrors_Type()
)
adGenPppLinkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkOutErrors.setStatus("current")


class _AdGenPppLinkValidIntervals_Type(Integer32):
    """Custom type adGenPppLinkValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenPppLinkValidIntervals_Type.__name__ = "Integer32"
_AdGenPppLinkValidIntervals_Object = MibTableColumn
adGenPppLinkValidIntervals = _AdGenPppLinkValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 10),
    _AdGenPppLinkValidIntervals_Type()
)
adGenPppLinkValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkValidIntervals.setStatus("current")


class _AdGenPppLinkInvalidIntervals_Type(Integer32):
    """Custom type adGenPppLinkInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenPppLinkInvalidIntervals_Type.__name__ = "Integer32"
_AdGenPppLinkInvalidIntervals_Object = MibTableColumn
adGenPppLinkInvalidIntervals = _AdGenPppLinkInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 11),
    _AdGenPppLinkInvalidIntervals_Type()
)
adGenPppLinkInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkInvalidIntervals.setStatus("current")


class _AdGenPppLinkTimeElapsed_Type(Integer32):
    """Custom type adGenPppLinkTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdGenPppLinkTimeElapsed_Type.__name__ = "Integer32"
_AdGenPppLinkTimeElapsed_Object = MibTableColumn
adGenPppLinkTimeElapsed = _AdGenPppLinkTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 12),
    _AdGenPppLinkTimeElapsed_Type()
)
adGenPppLinkTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTimeElapsed.setStatus("current")


class _AdGenPppLinkResetStats_Type(Integer32):
    """Custom type adGenPppLinkResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenPppLinkResetStats_Type.__name__ = "Integer32"
_AdGenPppLinkResetStats_Object = MibTableColumn
adGenPppLinkResetStats = _AdGenPppLinkResetStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 13),
    _AdGenPppLinkResetStats_Type()
)
adGenPppLinkResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppLinkResetStats.setStatus("current")


class _AdGenPppLinkResetPerfHistory_Type(Integer32):
    """Custom type adGenPppLinkResetPerfHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenPppLinkResetPerfHistory_Type.__name__ = "Integer32"
_AdGenPppLinkResetPerfHistory_Object = MibTableColumn
adGenPppLinkResetPerfHistory = _AdGenPppLinkResetPerfHistory_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 1, 1, 14),
    _AdGenPppLinkResetPerfHistory_Type()
)
adGenPppLinkResetPerfHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppLinkResetPerfHistory.setStatus("current")
_AdGenPppLinkCurrentTable_Object = MibTable
adGenPppLinkCurrentTable = _AdGenPppLinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    adGenPppLinkCurrentTable.setStatus("current")
_AdGenPppLinkCurrentEntry_Object = MibTableRow
adGenPppLinkCurrentEntry = _AdGenPppLinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1)
)
adGenPppLinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppLinkCurrentEntry.setStatus("current")
_AdGenPppLinkCurrentInOctets_Type = Gauge32
_AdGenPppLinkCurrentInOctets_Object = MibTableColumn
adGenPppLinkCurrentInOctets = _AdGenPppLinkCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1, 1),
    _AdGenPppLinkCurrentInOctets_Type()
)
adGenPppLinkCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentInOctets.setStatus("current")
_AdGenPppLinkCurrentInGoodOctets_Type = Gauge32
_AdGenPppLinkCurrentInGoodOctets_Object = MibTableColumn
adGenPppLinkCurrentInGoodOctets = _AdGenPppLinkCurrentInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1, 2),
    _AdGenPppLinkCurrentInGoodOctets_Type()
)
adGenPppLinkCurrentInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentInGoodOctets.setStatus("current")
_AdGenPppLinkCurrentInPkts_Type = Gauge32
_AdGenPppLinkCurrentInPkts_Object = MibTableColumn
adGenPppLinkCurrentInPkts = _AdGenPppLinkCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1, 3),
    _AdGenPppLinkCurrentInPkts_Type()
)
adGenPppLinkCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentInPkts.setStatus("current")
_AdGenPppLinkCurrentInDiscards_Type = Gauge32
_AdGenPppLinkCurrentInDiscards_Object = MibTableColumn
adGenPppLinkCurrentInDiscards = _AdGenPppLinkCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1, 4),
    _AdGenPppLinkCurrentInDiscards_Type()
)
adGenPppLinkCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentInDiscards.setStatus("current")
_AdGenPppLinkCurrentInErrors_Type = Gauge32
_AdGenPppLinkCurrentInErrors_Object = MibTableColumn
adGenPppLinkCurrentInErrors = _AdGenPppLinkCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1, 5),
    _AdGenPppLinkCurrentInErrors_Type()
)
adGenPppLinkCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentInErrors.setStatus("current")
_AdGenPppLinkCurrentOutOctets_Type = Gauge32
_AdGenPppLinkCurrentOutOctets_Object = MibTableColumn
adGenPppLinkCurrentOutOctets = _AdGenPppLinkCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1, 6),
    _AdGenPppLinkCurrentOutOctets_Type()
)
adGenPppLinkCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentOutOctets.setStatus("current")
_AdGenPppLinkCurrentOutPkts_Type = Gauge32
_AdGenPppLinkCurrentOutPkts_Object = MibTableColumn
adGenPppLinkCurrentOutPkts = _AdGenPppLinkCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1, 7),
    _AdGenPppLinkCurrentOutPkts_Type()
)
adGenPppLinkCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentOutPkts.setStatus("current")
_AdGenPppLinkCurrentOutDiscards_Type = Gauge32
_AdGenPppLinkCurrentOutDiscards_Object = MibTableColumn
adGenPppLinkCurrentOutDiscards = _AdGenPppLinkCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1, 8),
    _AdGenPppLinkCurrentOutDiscards_Type()
)
adGenPppLinkCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentOutDiscards.setStatus("current")
_AdGenPppLinkCurrentOutErrors_Type = Gauge32
_AdGenPppLinkCurrentOutErrors_Object = MibTableColumn
adGenPppLinkCurrentOutErrors = _AdGenPppLinkCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 2, 1, 9),
    _AdGenPppLinkCurrentOutErrors_Type()
)
adGenPppLinkCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkCurrentOutErrors.setStatus("current")
_AdGenPppLinkIntervalTable_Object = MibTable
adGenPppLinkIntervalTable = _AdGenPppLinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    adGenPppLinkIntervalTable.setStatus("current")
_AdGenPppLinkIntervalEntry_Object = MibTableRow
adGenPppLinkIntervalEntry = _AdGenPppLinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1)
)
adGenPppLinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-PPP-MIB", "adGenPppLinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenPppLinkIntervalEntry.setStatus("current")


class _AdGenPppLinkIntervalNumber_Type(Integer32):
    """Custom type adGenPppLinkIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenPppLinkIntervalNumber_Type.__name__ = "Integer32"
_AdGenPppLinkIntervalNumber_Object = MibTableColumn
adGenPppLinkIntervalNumber = _AdGenPppLinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 1),
    _AdGenPppLinkIntervalNumber_Type()
)
adGenPppLinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalNumber.setStatus("current")
_AdGenPppLinkIntervalInOctets_Type = Gauge32
_AdGenPppLinkIntervalInOctets_Object = MibTableColumn
adGenPppLinkIntervalInOctets = _AdGenPppLinkIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 2),
    _AdGenPppLinkIntervalInOctets_Type()
)
adGenPppLinkIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalInOctets.setStatus("current")
_AdGenPppLinkIntervalInGoodOctets_Type = Gauge32
_AdGenPppLinkIntervalInGoodOctets_Object = MibTableColumn
adGenPppLinkIntervalInGoodOctets = _AdGenPppLinkIntervalInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 3),
    _AdGenPppLinkIntervalInGoodOctets_Type()
)
adGenPppLinkIntervalInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalInGoodOctets.setStatus("current")
_AdGenPppLinkIntervalInPkts_Type = Gauge32
_AdGenPppLinkIntervalInPkts_Object = MibTableColumn
adGenPppLinkIntervalInPkts = _AdGenPppLinkIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 4),
    _AdGenPppLinkIntervalInPkts_Type()
)
adGenPppLinkIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalInPkts.setStatus("current")
_AdGenPppLinkIntervalInDiscards_Type = Gauge32
_AdGenPppLinkIntervalInDiscards_Object = MibTableColumn
adGenPppLinkIntervalInDiscards = _AdGenPppLinkIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 5),
    _AdGenPppLinkIntervalInDiscards_Type()
)
adGenPppLinkIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalInDiscards.setStatus("current")
_AdGenPppLinkIntervalInErrors_Type = Gauge32
_AdGenPppLinkIntervalInErrors_Object = MibTableColumn
adGenPppLinkIntervalInErrors = _AdGenPppLinkIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 6),
    _AdGenPppLinkIntervalInErrors_Type()
)
adGenPppLinkIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalInErrors.setStatus("current")
_AdGenPppLinkIntervalOutOctets_Type = Gauge32
_AdGenPppLinkIntervalOutOctets_Object = MibTableColumn
adGenPppLinkIntervalOutOctets = _AdGenPppLinkIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 7),
    _AdGenPppLinkIntervalOutOctets_Type()
)
adGenPppLinkIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalOutOctets.setStatus("current")
_AdGenPppLinkIntervalOutPkts_Type = Gauge32
_AdGenPppLinkIntervalOutPkts_Object = MibTableColumn
adGenPppLinkIntervalOutPkts = _AdGenPppLinkIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 8),
    _AdGenPppLinkIntervalOutPkts_Type()
)
adGenPppLinkIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalOutPkts.setStatus("current")
_AdGenPppLinkIntervalOutDiscards_Type = Gauge32
_AdGenPppLinkIntervalOutDiscards_Object = MibTableColumn
adGenPppLinkIntervalOutDiscards = _AdGenPppLinkIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 9),
    _AdGenPppLinkIntervalOutDiscards_Type()
)
adGenPppLinkIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalOutDiscards.setStatus("current")
_AdGenPppLinkIntervalOutErrors_Type = Gauge32
_AdGenPppLinkIntervalOutErrors_Object = MibTableColumn
adGenPppLinkIntervalOutErrors = _AdGenPppLinkIntervalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 10),
    _AdGenPppLinkIntervalOutErrors_Type()
)
adGenPppLinkIntervalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalOutErrors.setStatus("current")
_AdGenPppLinkIntervalTimeStamp_Type = DisplayString
_AdGenPppLinkIntervalTimeStamp_Object = MibTableColumn
adGenPppLinkIntervalTimeStamp = _AdGenPppLinkIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 3, 1, 11),
    _AdGenPppLinkIntervalTimeStamp_Type()
)
adGenPppLinkIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkIntervalTimeStamp.setStatus("current")
_AdGenPppLinkTotalTable_Object = MibTable
adGenPppLinkTotalTable = _AdGenPppLinkTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    adGenPppLinkTotalTable.setStatus("current")
_AdGenPppLinkTotalEntry_Object = MibTableRow
adGenPppLinkTotalEntry = _AdGenPppLinkTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1)
)
adGenPppLinkTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppLinkTotalEntry.setStatus("current")
_AdGenPppLinkTotalInOctets_Type = Gauge32
_AdGenPppLinkTotalInOctets_Object = MibTableColumn
adGenPppLinkTotalInOctets = _AdGenPppLinkTotalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1, 1),
    _AdGenPppLinkTotalInOctets_Type()
)
adGenPppLinkTotalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTotalInOctets.setStatus("current")
_AdGenPppLinkTotalInGoodOctets_Type = Gauge32
_AdGenPppLinkTotalInGoodOctets_Object = MibTableColumn
adGenPppLinkTotalInGoodOctets = _AdGenPppLinkTotalInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1, 2),
    _AdGenPppLinkTotalInGoodOctets_Type()
)
adGenPppLinkTotalInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTotalInGoodOctets.setStatus("current")
_AdGenPppLinkTotalInPkts_Type = Gauge32
_AdGenPppLinkTotalInPkts_Object = MibTableColumn
adGenPppLinkTotalInPkts = _AdGenPppLinkTotalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1, 3),
    _AdGenPppLinkTotalInPkts_Type()
)
adGenPppLinkTotalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTotalInPkts.setStatus("current")
_AdGenPppLinkTotalInDiscards_Type = Gauge32
_AdGenPppLinkTotalInDiscards_Object = MibTableColumn
adGenPppLinkTotalInDiscards = _AdGenPppLinkTotalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1, 4),
    _AdGenPppLinkTotalInDiscards_Type()
)
adGenPppLinkTotalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTotalInDiscards.setStatus("current")
_AdGenPppLinkTotalInErrors_Type = Gauge32
_AdGenPppLinkTotalInErrors_Object = MibTableColumn
adGenPppLinkTotalInErrors = _AdGenPppLinkTotalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1, 5),
    _AdGenPppLinkTotalInErrors_Type()
)
adGenPppLinkTotalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTotalInErrors.setStatus("current")
_AdGenPppLinkTotalOutOctets_Type = Gauge32
_AdGenPppLinkTotalOutOctets_Object = MibTableColumn
adGenPppLinkTotalOutOctets = _AdGenPppLinkTotalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1, 6),
    _AdGenPppLinkTotalOutOctets_Type()
)
adGenPppLinkTotalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTotalOutOctets.setStatus("current")
_AdGenPppLinkTotalOutPkts_Type = Gauge32
_AdGenPppLinkTotalOutPkts_Object = MibTableColumn
adGenPppLinkTotalOutPkts = _AdGenPppLinkTotalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1, 7),
    _AdGenPppLinkTotalOutPkts_Type()
)
adGenPppLinkTotalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTotalOutPkts.setStatus("current")
_AdGenPppLinkTotalOutDiscards_Type = Gauge32
_AdGenPppLinkTotalOutDiscards_Object = MibTableColumn
adGenPppLinkTotalOutDiscards = _AdGenPppLinkTotalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1, 8),
    _AdGenPppLinkTotalOutDiscards_Type()
)
adGenPppLinkTotalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTotalOutDiscards.setStatus("current")
_AdGenPppLinkTotalOutErrors_Type = Gauge32
_AdGenPppLinkTotalOutErrors_Object = MibTableColumn
adGenPppLinkTotalOutErrors = _AdGenPppLinkTotalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 4, 1, 9),
    _AdGenPppLinkTotalOutErrors_Type()
)
adGenPppLinkTotalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkTotalOutErrors.setStatus("current")
_AdGenPppLinkDayCurrentTable_Object = MibTable
adGenPppLinkDayCurrentTable = _AdGenPppLinkDayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentTable.setStatus("current")
_AdGenPppLinkDayCurrentEntry_Object = MibTableRow
adGenPppLinkDayCurrentEntry = _AdGenPppLinkDayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1)
)
adGenPppLinkDayCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentEntry.setStatus("current")
_AdGenPppLinkDayCurrentInOctets_Type = Gauge32
_AdGenPppLinkDayCurrentInOctets_Object = MibTableColumn
adGenPppLinkDayCurrentInOctets = _AdGenPppLinkDayCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1, 1),
    _AdGenPppLinkDayCurrentInOctets_Type()
)
adGenPppLinkDayCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentInOctets.setStatus("current")
_AdGenPppLinkDayCurrentInGoodOctets_Type = Gauge32
_AdGenPppLinkDayCurrentInGoodOctets_Object = MibTableColumn
adGenPppLinkDayCurrentInGoodOctets = _AdGenPppLinkDayCurrentInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1, 2),
    _AdGenPppLinkDayCurrentInGoodOctets_Type()
)
adGenPppLinkDayCurrentInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentInGoodOctets.setStatus("current")
_AdGenPppLinkDayCurrentInPkts_Type = Gauge32
_AdGenPppLinkDayCurrentInPkts_Object = MibTableColumn
adGenPppLinkDayCurrentInPkts = _AdGenPppLinkDayCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1, 3),
    _AdGenPppLinkDayCurrentInPkts_Type()
)
adGenPppLinkDayCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentInPkts.setStatus("current")
_AdGenPppLinkDayCurrentInDiscards_Type = Gauge32
_AdGenPppLinkDayCurrentInDiscards_Object = MibTableColumn
adGenPppLinkDayCurrentInDiscards = _AdGenPppLinkDayCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1, 4),
    _AdGenPppLinkDayCurrentInDiscards_Type()
)
adGenPppLinkDayCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentInDiscards.setStatus("current")
_AdGenPppLinkDayCurrentInErrors_Type = Gauge32
_AdGenPppLinkDayCurrentInErrors_Object = MibTableColumn
adGenPppLinkDayCurrentInErrors = _AdGenPppLinkDayCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1, 5),
    _AdGenPppLinkDayCurrentInErrors_Type()
)
adGenPppLinkDayCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentInErrors.setStatus("current")
_AdGenPppLinkDayCurrentOutOctets_Type = Gauge32
_AdGenPppLinkDayCurrentOutOctets_Object = MibTableColumn
adGenPppLinkDayCurrentOutOctets = _AdGenPppLinkDayCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1, 6),
    _AdGenPppLinkDayCurrentOutOctets_Type()
)
adGenPppLinkDayCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentOutOctets.setStatus("current")
_AdGenPppLinkDayCurrentOutPkts_Type = Gauge32
_AdGenPppLinkDayCurrentOutPkts_Object = MibTableColumn
adGenPppLinkDayCurrentOutPkts = _AdGenPppLinkDayCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1, 7),
    _AdGenPppLinkDayCurrentOutPkts_Type()
)
adGenPppLinkDayCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentOutPkts.setStatus("current")
_AdGenPppLinkDayCurrentOutDiscards_Type = Gauge32
_AdGenPppLinkDayCurrentOutDiscards_Object = MibTableColumn
adGenPppLinkDayCurrentOutDiscards = _AdGenPppLinkDayCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1, 8),
    _AdGenPppLinkDayCurrentOutDiscards_Type()
)
adGenPppLinkDayCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentOutDiscards.setStatus("current")
_AdGenPppLinkDayCurrentOutErrors_Type = Gauge32
_AdGenPppLinkDayCurrentOutErrors_Object = MibTableColumn
adGenPppLinkDayCurrentOutErrors = _AdGenPppLinkDayCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 5, 1, 9),
    _AdGenPppLinkDayCurrentOutErrors_Type()
)
adGenPppLinkDayCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayCurrentOutErrors.setStatus("current")
_AdGenPppLinkDayIntervalTable_Object = MibTable
adGenPppLinkDayIntervalTable = _AdGenPppLinkDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalTable.setStatus("current")
_AdGenPppLinkDayIntervalEntry_Object = MibTableRow
adGenPppLinkDayIntervalEntry = _AdGenPppLinkDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1)
)
adGenPppLinkDayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-PPP-MIB", "adGenPppLinkDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalEntry.setStatus("current")


class _AdGenPppLinkDayIntervalNumber_Type(Integer32):
    """Custom type adGenPppLinkDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenPppLinkDayIntervalNumber_Type.__name__ = "Integer32"
_AdGenPppLinkDayIntervalNumber_Object = MibTableColumn
adGenPppLinkDayIntervalNumber = _AdGenPppLinkDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 1),
    _AdGenPppLinkDayIntervalNumber_Type()
)
adGenPppLinkDayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalNumber.setStatus("current")
_AdGenPppLinkDayIntervalInOctets_Type = Gauge32
_AdGenPppLinkDayIntervalInOctets_Object = MibTableColumn
adGenPppLinkDayIntervalInOctets = _AdGenPppLinkDayIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 2),
    _AdGenPppLinkDayIntervalInOctets_Type()
)
adGenPppLinkDayIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalInOctets.setStatus("current")
_AdGenPppLinkDayIntervalInGoodOctets_Type = Gauge32
_AdGenPppLinkDayIntervalInGoodOctets_Object = MibTableColumn
adGenPppLinkDayIntervalInGoodOctets = _AdGenPppLinkDayIntervalInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 3),
    _AdGenPppLinkDayIntervalInGoodOctets_Type()
)
adGenPppLinkDayIntervalInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalInGoodOctets.setStatus("current")
_AdGenPppLinkDayIntervalInPkts_Type = Gauge32
_AdGenPppLinkDayIntervalInPkts_Object = MibTableColumn
adGenPppLinkDayIntervalInPkts = _AdGenPppLinkDayIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 4),
    _AdGenPppLinkDayIntervalInPkts_Type()
)
adGenPppLinkDayIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalInPkts.setStatus("current")
_AdGenPppLinkDayIntervalInDiscards_Type = Gauge32
_AdGenPppLinkDayIntervalInDiscards_Object = MibTableColumn
adGenPppLinkDayIntervalInDiscards = _AdGenPppLinkDayIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 5),
    _AdGenPppLinkDayIntervalInDiscards_Type()
)
adGenPppLinkDayIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalInDiscards.setStatus("current")
_AdGenPppLinkDayIntervalInErrors_Type = Gauge32
_AdGenPppLinkDayIntervalInErrors_Object = MibTableColumn
adGenPppLinkDayIntervalInErrors = _AdGenPppLinkDayIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 6),
    _AdGenPppLinkDayIntervalInErrors_Type()
)
adGenPppLinkDayIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalInErrors.setStatus("current")
_AdGenPppLinkDayIntervalOutOctets_Type = Gauge32
_AdGenPppLinkDayIntervalOutOctets_Object = MibTableColumn
adGenPppLinkDayIntervalOutOctets = _AdGenPppLinkDayIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 7),
    _AdGenPppLinkDayIntervalOutOctets_Type()
)
adGenPppLinkDayIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalOutOctets.setStatus("current")
_AdGenPppLinkDayIntervalOutPkts_Type = Gauge32
_AdGenPppLinkDayIntervalOutPkts_Object = MibTableColumn
adGenPppLinkDayIntervalOutPkts = _AdGenPppLinkDayIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 8),
    _AdGenPppLinkDayIntervalOutPkts_Type()
)
adGenPppLinkDayIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalOutPkts.setStatus("current")
_AdGenPppLinkDayIntervalOutDiscards_Type = Gauge32
_AdGenPppLinkDayIntervalOutDiscards_Object = MibTableColumn
adGenPppLinkDayIntervalOutDiscards = _AdGenPppLinkDayIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 9),
    _AdGenPppLinkDayIntervalOutDiscards_Type()
)
adGenPppLinkDayIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalOutDiscards.setStatus("current")
_AdGenPppLinkDayIntervalOutErrors_Type = Gauge32
_AdGenPppLinkDayIntervalOutErrors_Object = MibTableColumn
adGenPppLinkDayIntervalOutErrors = _AdGenPppLinkDayIntervalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 10),
    _AdGenPppLinkDayIntervalOutErrors_Type()
)
adGenPppLinkDayIntervalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalOutErrors.setStatus("current")
_AdGenPppLinkDayIntervalTimeStamp_Type = DisplayString
_AdGenPppLinkDayIntervalTimeStamp_Object = MibTableColumn
adGenPppLinkDayIntervalTimeStamp = _AdGenPppLinkDayIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 1, 3, 6, 1, 11),
    _AdGenPppLinkDayIntervalTimeStamp_Type()
)
adGenPppLinkDayIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppLinkDayIntervalTimeStamp.setStatus("current")
_AdGenPppGroupObjects_ObjectIdentity = ObjectIdentity
adGenPppGroupObjects = _AdGenPppGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2)
)
_AdGenPppGroupProv_ObjectIdentity = ObjectIdentity
adGenPppGroupProv = _AdGenPppGroupProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1)
)
_AdGenPppGroupProvTable_Object = MibTable
adGenPppGroupProvTable = _AdGenPppGroupProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPppGroupProvTable.setStatus("current")
_AdGenPppGroupProvEntry_Object = MibTableRow
adGenPppGroupProvEntry = _AdGenPppGroupProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1)
)
adGenPppGroupProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppGroupProvEntry.setStatus("current")
_AdGenPppGroupSubscriberIpAddress_Type = IpAddress
_AdGenPppGroupSubscriberIpAddress_Object = MibTableColumn
adGenPppGroupSubscriberIpAddress = _AdGenPppGroupSubscriberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 1),
    _AdGenPppGroupSubscriberIpAddress_Type()
)
adGenPppGroupSubscriberIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupSubscriberIpAddress.setStatus("current")
_AdGenPppGroupGatewayIpAddress_Type = IpAddress
_AdGenPppGroupGatewayIpAddress_Object = MibTableColumn
adGenPppGroupGatewayIpAddress = _AdGenPppGroupGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 2),
    _AdGenPppGroupGatewayIpAddress_Type()
)
adGenPppGroupGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupGatewayIpAddress.setStatus("current")
_AdGenPppGroupPrimaryDNSIpAddress_Type = IpAddress
_AdGenPppGroupPrimaryDNSIpAddress_Object = MibTableColumn
adGenPppGroupPrimaryDNSIpAddress = _AdGenPppGroupPrimaryDNSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 3),
    _AdGenPppGroupPrimaryDNSIpAddress_Type()
)
adGenPppGroupPrimaryDNSIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupPrimaryDNSIpAddress.setStatus("current")
_AdGenPppGroupSecondaryDNSIpAddress_Type = IpAddress
_AdGenPppGroupSecondaryDNSIpAddress_Object = MibTableColumn
adGenPppGroupSecondaryDNSIpAddress = _AdGenPppGroupSecondaryDNSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 4),
    _AdGenPppGroupSecondaryDNSIpAddress_Type()
)
adGenPppGroupSecondaryDNSIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupSecondaryDNSIpAddress.setStatus("current")


class _AdGenPppGroupConfigInitialMRU_Type(Integer32):
    """Custom type adGenPppGroupConfigInitialMRU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AdGenPppGroupConfigInitialMRU_Type.__name__ = "Integer32"
_AdGenPppGroupConfigInitialMRU_Object = MibTableColumn
adGenPppGroupConfigInitialMRU = _AdGenPppGroupConfigInitialMRU_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 5),
    _AdGenPppGroupConfigInitialMRU_Type()
)
adGenPppGroupConfigInitialMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigInitialMRU.setStatus("current")


class _AdGenPppGroupConfigMagicNumber_Type(TruthValue):
    """Custom type adGenPppGroupConfigMagicNumber based on TruthValue"""
    defaultValue = 2


_AdGenPppGroupConfigMagicNumber_Type.__name__ = "TruthValue"
_AdGenPppGroupConfigMagicNumber_Object = MibTableColumn
adGenPppGroupConfigMagicNumber = _AdGenPppGroupConfigMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 6),
    _AdGenPppGroupConfigMagicNumber_Type()
)
adGenPppGroupConfigMagicNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigMagicNumber.setStatus("current")


class _AdGenPppGroupConfigFcsSize_Type(Integer32):
    """Custom type adGenPppGroupConfigFcsSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("zerobits", 1),
          ("sixteenbits", 2),
          ("thirtytwobits", 3))
    )


_AdGenPppGroupConfigFcsSize_Type.__name__ = "Integer32"
_AdGenPppGroupConfigFcsSize_Object = MibTableColumn
adGenPppGroupConfigFcsSize = _AdGenPppGroupConfigFcsSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 7),
    _AdGenPppGroupConfigFcsSize_Type()
)
adGenPppGroupConfigFcsSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigFcsSize.setStatus("current")


class _AdGenPppGroupConfigACCompression_Type(TruthValue):
    """Custom type adGenPppGroupConfigACCompression based on TruthValue"""
    defaultValue = 2


_AdGenPppGroupConfigACCompression_Type.__name__ = "TruthValue"
_AdGenPppGroupConfigACCompression_Object = MibTableColumn
adGenPppGroupConfigACCompression = _AdGenPppGroupConfigACCompression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 8),
    _AdGenPppGroupConfigACCompression_Type()
)
adGenPppGroupConfigACCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigACCompression.setStatus("current")


class _AdGenPppGroupConfigPFCompression_Type(TruthValue):
    """Custom type adGenPppGroupConfigPFCompression based on TruthValue"""
    defaultValue = 2


_AdGenPppGroupConfigPFCompression_Type.__name__ = "TruthValue"
_AdGenPppGroupConfigPFCompression_Object = MibTableColumn
adGenPppGroupConfigPFCompression = _AdGenPppGroupConfigPFCompression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 9),
    _AdGenPppGroupConfigPFCompression_Type()
)
adGenPppGroupConfigPFCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigPFCompression.setStatus("current")


class _AdGenPppGroupConfigLQM_Type(TruthValue):
    """Custom type adGenPppGroupConfigLQM based on TruthValue"""
    defaultValue = 1


_AdGenPppGroupConfigLQM_Type.__name__ = "TruthValue"
_AdGenPppGroupConfigLQM_Object = MibTableColumn
adGenPppGroupConfigLQM = _AdGenPppGroupConfigLQM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 10),
    _AdGenPppGroupConfigLQM_Type()
)
adGenPppGroupConfigLQM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigLQM.setStatus("current")


class _AdGenPppGroupConfigRestartTimer_Type(Integer32):
    """Custom type adGenPppGroupConfigRestartTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AdGenPppGroupConfigRestartTimer_Type.__name__ = "Integer32"
_AdGenPppGroupConfigRestartTimer_Object = MibTableColumn
adGenPppGroupConfigRestartTimer = _AdGenPppGroupConfigRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 11),
    _AdGenPppGroupConfigRestartTimer_Type()
)
adGenPppGroupConfigRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigRestartTimer.setStatus("current")


class _AdGenPppGroupConfigMaxTerminate_Type(Integer32):
    """Custom type adGenPppGroupConfigMaxTerminate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_AdGenPppGroupConfigMaxTerminate_Type.__name__ = "Integer32"
_AdGenPppGroupConfigMaxTerminate_Object = MibTableColumn
adGenPppGroupConfigMaxTerminate = _AdGenPppGroupConfigMaxTerminate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 12),
    _AdGenPppGroupConfigMaxTerminate_Type()
)
adGenPppGroupConfigMaxTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigMaxTerminate.setStatus("current")


class _AdGenPppGroupConfigMaxConfigure_Type(Integer32):
    """Custom type adGenPppGroupConfigMaxConfigure based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_AdGenPppGroupConfigMaxConfigure_Type.__name__ = "Integer32"
_AdGenPppGroupConfigMaxConfigure_Object = MibTableColumn
adGenPppGroupConfigMaxConfigure = _AdGenPppGroupConfigMaxConfigure_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 13),
    _AdGenPppGroupConfigMaxConfigure_Type()
)
adGenPppGroupConfigMaxConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigMaxConfigure.setStatus("current")


class _AdGenPppGroupConfigMaxFailure_Type(Integer32):
    """Custom type adGenPppGroupConfigMaxFailure based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_AdGenPppGroupConfigMaxFailure_Type.__name__ = "Integer32"
_AdGenPppGroupConfigMaxFailure_Object = MibTableColumn
adGenPppGroupConfigMaxFailure = _AdGenPppGroupConfigMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 14),
    _AdGenPppGroupConfigMaxFailure_Type()
)
adGenPppGroupConfigMaxFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigMaxFailure.setStatus("current")


class _AdGenPppGroupConfigKeepAliveRate_Type(Integer32):
    """Custom type adGenPppGroupConfigKeepAliveRate based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AdGenPppGroupConfigKeepAliveRate_Type.__name__ = "Integer32"
_AdGenPppGroupConfigKeepAliveRate_Object = MibTableColumn
adGenPppGroupConfigKeepAliveRate = _AdGenPppGroupConfigKeepAliveRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 15),
    _AdGenPppGroupConfigKeepAliveRate_Type()
)
adGenPppGroupConfigKeepAliveRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigKeepAliveRate.setStatus("current")


class _AdGenPppGroupChapEnabled_Type(TruthValue):
    """Custom type adGenPppGroupChapEnabled based on TruthValue"""
    defaultValue = 2


_AdGenPppGroupChapEnabled_Type.__name__ = "TruthValue"
_AdGenPppGroupChapEnabled_Object = MibTableColumn
adGenPppGroupChapEnabled = _AdGenPppGroupChapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 16),
    _AdGenPppGroupChapEnabled_Type()
)
adGenPppGroupChapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupChapEnabled.setStatus("current")


class _AdGenPppGroupLocalUserName_Type(OctetString):
    """Custom type adGenPppGroupLocalUserName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdGenPppGroupLocalUserName_Type.__name__ = "OctetString"
_AdGenPppGroupLocalUserName_Object = MibTableColumn
adGenPppGroupLocalUserName = _AdGenPppGroupLocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 17),
    _AdGenPppGroupLocalUserName_Type()
)
adGenPppGroupLocalUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupLocalUserName.setStatus("current")


class _AdGenPppGroupLocalPassword_Type(OctetString):
    """Custom type adGenPppGroupLocalPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdGenPppGroupLocalPassword_Type.__name__ = "OctetString"
_AdGenPppGroupLocalPassword_Object = MibTableColumn
adGenPppGroupLocalPassword = _AdGenPppGroupLocalPassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 18),
    _AdGenPppGroupLocalPassword_Type()
)
adGenPppGroupLocalPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupLocalPassword.setStatus("current")


class _AdGenPppGroupPeerUserName_Type(OctetString):
    """Custom type adGenPppGroupPeerUserName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdGenPppGroupPeerUserName_Type.__name__ = "OctetString"
_AdGenPppGroupPeerUserName_Object = MibTableColumn
adGenPppGroupPeerUserName = _AdGenPppGroupPeerUserName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 19),
    _AdGenPppGroupPeerUserName_Type()
)
adGenPppGroupPeerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupPeerUserName.setStatus("current")


class _AdGenPppGroupPeerPassword_Type(OctetString):
    """Custom type adGenPppGroupPeerPassword based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdGenPppGroupPeerPassword_Type.__name__ = "OctetString"
_AdGenPppGroupPeerPassword_Object = MibTableColumn
adGenPppGroupPeerPassword = _AdGenPppGroupPeerPassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 20),
    _AdGenPppGroupPeerPassword_Type()
)
adGenPppGroupPeerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupPeerPassword.setStatus("current")


class _AdGenPppGroupIpAddressAssignment_Type(Integer32):
    """Custom type adGenPppGroupIpAddressAssignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("staticIpv4", 1),
          ("dhcpv4", 2))
    )


_AdGenPppGroupIpAddressAssignment_Type.__name__ = "Integer32"
_AdGenPppGroupIpAddressAssignment_Object = MibTableColumn
adGenPppGroupIpAddressAssignment = _AdGenPppGroupIpAddressAssignment_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 21),
    _AdGenPppGroupIpAddressAssignment_Type()
)
adGenPppGroupIpAddressAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupIpAddressAssignment.setStatus("current")


class _AdGenPppGroupDhcpClientIdentfier_Type(OctetString):
    """Custom type adGenPppGroupDhcpClientIdentfier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 80),
    )


_AdGenPppGroupDhcpClientIdentfier_Type.__name__ = "OctetString"
_AdGenPppGroupDhcpClientIdentfier_Object = MibTableColumn
adGenPppGroupDhcpClientIdentfier = _AdGenPppGroupDhcpClientIdentfier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 22),
    _AdGenPppGroupDhcpClientIdentfier_Type()
)
adGenPppGroupDhcpClientIdentfier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupDhcpClientIdentfier.setStatus("current")


class _AdGenPppGroupDhcpHostname_Type(DisplayString):
    """Custom type adGenPppGroupDhcpHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_AdGenPppGroupDhcpHostname_Type.__name__ = "DisplayString"
_AdGenPppGroupDhcpHostname_Object = MibTableColumn
adGenPppGroupDhcpHostname = _AdGenPppGroupDhcpHostname_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 23),
    _AdGenPppGroupDhcpHostname_Type()
)
adGenPppGroupDhcpHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupDhcpHostname.setStatus("current")


class _AdGenPppGroupConfigMultilink_Type(TruthValue):
    """Custom type adGenPppGroupConfigMultilink based on TruthValue"""
    defaultValue = 2


_AdGenPppGroupConfigMultilink_Type.__name__ = "TruthValue"
_AdGenPppGroupConfigMultilink_Object = MibTableColumn
adGenPppGroupConfigMultilink = _AdGenPppGroupConfigMultilink_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 24),
    _AdGenPppGroupConfigMultilink_Type()
)
adGenPppGroupConfigMultilink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupConfigMultilink.setStatus("current")
_AdGenPppGroupSubscriberIPv6Address_Type = InetAddressIPv6
_AdGenPppGroupSubscriberIPv6Address_Object = MibTableColumn
adGenPppGroupSubscriberIPv6Address = _AdGenPppGroupSubscriberIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 25),
    _AdGenPppGroupSubscriberIPv6Address_Type()
)
adGenPppGroupSubscriberIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupSubscriberIPv6Address.setStatus("current")


class _AdGenPppGroupGatewayIPv6AddressAssignment_Type(Integer32):
    """Custom type adGenPppGroupGatewayIPv6AddressAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("auto", 2))
    )


_AdGenPppGroupGatewayIPv6AddressAssignment_Type.__name__ = "Integer32"
_AdGenPppGroupGatewayIPv6AddressAssignment_Object = MibTableColumn
adGenPppGroupGatewayIPv6AddressAssignment = _AdGenPppGroupGatewayIPv6AddressAssignment_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 26),
    _AdGenPppGroupGatewayIPv6AddressAssignment_Type()
)
adGenPppGroupGatewayIPv6AddressAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupGatewayIPv6AddressAssignment.setStatus("current")
_AdGenPppGroupGatewayIPv6Address_Type = InetAddressIPv6
_AdGenPppGroupGatewayIPv6Address_Object = MibTableColumn
adGenPppGroupGatewayIPv6Address = _AdGenPppGroupGatewayIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 27),
    _AdGenPppGroupGatewayIPv6Address_Type()
)
adGenPppGroupGatewayIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupGatewayIPv6Address.setStatus("current")
_AdGenPppGroupIpEnabled_Type = TruthValue
_AdGenPppGroupIpEnabled_Object = MibTableColumn
adGenPppGroupIpEnabled = _AdGenPppGroupIpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 28),
    _AdGenPppGroupIpEnabled_Type()
)
adGenPppGroupIpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupIpEnabled.setStatus("current")
_AdGenPppGroupIpv6Enabled_Type = TruthValue
_AdGenPppGroupIpv6Enabled_Object = MibTableColumn
adGenPppGroupIpv6Enabled = _AdGenPppGroupIpv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 1, 1, 29),
    _AdGenPppGroupIpv6Enabled_Type()
)
adGenPppGroupIpv6Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupIpv6Enabled.setStatus("current")
_AdGenPppGroupAlarmProvTable_Object = MibTable
adGenPppGroupAlarmProvTable = _AdGenPppGroupAlarmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvTable.setStatus("current")
_AdGenPppGroupAlarmProvEntry_Object = MibTableRow
adGenPppGroupAlarmProvEntry = _AdGenPppGroupAlarmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1)
)
adGenPppGroupAlarmProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvEntry.setStatus("current")


class _AdGenPppGroupAlarmProvNCPAlarmSeverity_Type(Integer32):
    """Custom type adGenPppGroupAlarmProvNCPAlarmSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenPppGroupAlarmProvNCPAlarmSeverity_Type.__name__ = "Integer32"
_AdGenPppGroupAlarmProvNCPAlarmSeverity_Object = MibTableColumn
adGenPppGroupAlarmProvNCPAlarmSeverity = _AdGenPppGroupAlarmProvNCPAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 1),
    _AdGenPppGroupAlarmProvNCPAlarmSeverity_Type()
)
adGenPppGroupAlarmProvNCPAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvNCPAlarmSeverity.setStatus("current")


class _AdGenPppGroupAlarmProvNCPAlarmSuppression_Type(Integer32):
    """Custom type adGenPppGroupAlarmProvNCPAlarmSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdGenPppGroupAlarmProvNCPAlarmSuppression_Type.__name__ = "Integer32"
_AdGenPppGroupAlarmProvNCPAlarmSuppression_Object = MibTableColumn
adGenPppGroupAlarmProvNCPAlarmSuppression = _AdGenPppGroupAlarmProvNCPAlarmSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 2),
    _AdGenPppGroupAlarmProvNCPAlarmSuppression_Type()
)
adGenPppGroupAlarmProvNCPAlarmSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvNCPAlarmSuppression.setStatus("current")


class _AdGenPppGroupAlarmProvNCPAlarmEnable_Type(TruthValue):
    """Custom type adGenPppGroupAlarmProvNCPAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenPppGroupAlarmProvNCPAlarmEnable_Type.__name__ = "TruthValue"
_AdGenPppGroupAlarmProvNCPAlarmEnable_Object = MibTableColumn
adGenPppGroupAlarmProvNCPAlarmEnable = _AdGenPppGroupAlarmProvNCPAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 3),
    _AdGenPppGroupAlarmProvNCPAlarmEnable_Type()
)
adGenPppGroupAlarmProvNCPAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvNCPAlarmEnable.setStatus("current")


class _AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Type(Integer32):
    """Custom type adGenPppGroupAlarmProvIpv6NcpAlarmSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Type.__name__ = "Integer32"
_AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Object = MibTableColumn
adGenPppGroupAlarmProvIpv6NcpAlarmSeverity = _AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 4),
    _AdGenPppGroupAlarmProvIpv6NcpAlarmSeverity_Type()
)
adGenPppGroupAlarmProvIpv6NcpAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvIpv6NcpAlarmSeverity.setStatus("current")


class _AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Type(Integer32):
    """Custom type adGenPppGroupAlarmProvIpv6NcpAlarmSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Type.__name__ = "Integer32"
_AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Object = MibTableColumn
adGenPppGroupAlarmProvIpv6NcpAlarmSuppression = _AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 5),
    _AdGenPppGroupAlarmProvIpv6NcpAlarmSuppression_Type()
)
adGenPppGroupAlarmProvIpv6NcpAlarmSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvIpv6NcpAlarmSuppression.setStatus("current")


class _AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Type(TruthValue):
    """Custom type adGenPppGroupAlarmProvIpv6NcpAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Type.__name__ = "TruthValue"
_AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Object = MibTableColumn
adGenPppGroupAlarmProvIpv6NcpAlarmEnable = _AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 6),
    _AdGenPppGroupAlarmProvIpv6NcpAlarmEnable_Type()
)
adGenPppGroupAlarmProvIpv6NcpAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvIpv6NcpAlarmEnable.setStatus("current")


class _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Type(Integer32):
    """Custom type adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Type.__name__ = "Integer32"
_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Object = MibTableColumn
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity = _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 7),
    _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity_Type()
)
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity.setStatus("current")


class _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Type(Integer32):
    """Custom type adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Type.__name__ = "Integer32"
_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Object = MibTableColumn
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression = _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 8),
    _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression_Type()
)
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression.setStatus("current")


class _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Type(TruthValue):
    """Custom type adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Type.__name__ = "TruthValue"
_AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Object = MibTableColumn
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable = _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 9),
    _AdGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable_Type()
)
adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable.setStatus("current")


class _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Type(Integer32):
    """Custom type adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Type.__name__ = "Integer32"
_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Object = MibTableColumn
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity = _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 10),
    _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity_Type()
)
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity.setStatus("current")


class _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Type(Integer32):
    """Custom type adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Type.__name__ = "Integer32"
_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Object = MibTableColumn
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression = _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 11),
    _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression_Type()
)
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression.setStatus("current")


class _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Type(TruthValue):
    """Custom type adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Type.__name__ = "TruthValue"
_AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Object = MibTableColumn
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable = _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 1, 2, 1, 12),
    _AdGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable_Type()
)
adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable.setStatus("current")
_AdGenPppGroupStatus_ObjectIdentity = ObjectIdentity
adGenPppGroupStatus = _AdGenPppGroupStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2)
)
_AdGenPppGroupStatusTable_Object = MibTable
adGenPppGroupStatusTable = _AdGenPppGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    adGenPppGroupStatusTable.setStatus("current")
_AdGenPppGroupStatusEntry_Object = MibTableRow
adGenPppGroupStatusEntry = _AdGenPppGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1)
)
adGenPppGroupStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppGroupStatusEntry.setStatus("current")


class _AdGenPppGroupNCPState_Type(Integer32):
    """Custom type adGenPppGroupNCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("reqsent", 7),
          ("ackrcvd", 8),
          ("acksent", 9),
          ("opened", 10))
    )


_AdGenPppGroupNCPState_Type.__name__ = "Integer32"
_AdGenPppGroupNCPState_Object = MibTableColumn
adGenPppGroupNCPState = _AdGenPppGroupNCPState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1, 1),
    _AdGenPppGroupNCPState_Type()
)
adGenPppGroupNCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupNCPState.setStatus("current")
_AdGenPppGroupCurrentSubscriberIpAddress_Type = IpAddress
_AdGenPppGroupCurrentSubscriberIpAddress_Object = MibTableColumn
adGenPppGroupCurrentSubscriberIpAddress = _AdGenPppGroupCurrentSubscriberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1, 2),
    _AdGenPppGroupCurrentSubscriberIpAddress_Type()
)
adGenPppGroupCurrentSubscriberIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentSubscriberIpAddress.setStatus("current")
_AdGenPppGroupCurrentGatewayIpAddress_Type = IpAddress
_AdGenPppGroupCurrentGatewayIpAddress_Object = MibTableColumn
adGenPppGroupCurrentGatewayIpAddress = _AdGenPppGroupCurrentGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1, 3),
    _AdGenPppGroupCurrentGatewayIpAddress_Type()
)
adGenPppGroupCurrentGatewayIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentGatewayIpAddress.setStatus("current")
_AdGenPppGroupCurrentPrimaryDNSIpAddress_Type = IpAddress
_AdGenPppGroupCurrentPrimaryDNSIpAddress_Object = MibTableColumn
adGenPppGroupCurrentPrimaryDNSIpAddress = _AdGenPppGroupCurrentPrimaryDNSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1, 4),
    _AdGenPppGroupCurrentPrimaryDNSIpAddress_Type()
)
adGenPppGroupCurrentPrimaryDNSIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentPrimaryDNSIpAddress.setStatus("current")
_AdGenPppGroupCurrentSecondaryDNSIpAddress_Type = IpAddress
_AdGenPppGroupCurrentSecondaryDNSIpAddress_Object = MibTableColumn
adGenPppGroupCurrentSecondaryDNSIpAddress = _AdGenPppGroupCurrentSecondaryDNSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1, 5),
    _AdGenPppGroupCurrentSecondaryDNSIpAddress_Type()
)
adGenPppGroupCurrentSecondaryDNSIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentSecondaryDNSIpAddress.setStatus("current")
_AdGenPppGroupNegotiatedStatus_Type = DisplayString
_AdGenPppGroupNegotiatedStatus_Object = MibTableColumn
adGenPppGroupNegotiatedStatus = _AdGenPppGroupNegotiatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1, 6),
    _AdGenPppGroupNegotiatedStatus_Type()
)
adGenPppGroupNegotiatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupNegotiatedStatus.setStatus("current")


class _AdGenPppGroupIPv6AddressStatus_Type(Integer32):
    """Custom type adGenPppGroupIPv6AddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unverified", 1),
          ("verified", 2),
          ("mismatch", 3))
    )


_AdGenPppGroupIPv6AddressStatus_Type.__name__ = "Integer32"
_AdGenPppGroupIPv6AddressStatus_Object = MibTableColumn
adGenPppGroupIPv6AddressStatus = _AdGenPppGroupIPv6AddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1, 7),
    _AdGenPppGroupIPv6AddressStatus_Type()
)
adGenPppGroupIPv6AddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIPv6AddressStatus.setStatus("current")


class _AdGenPppGroupIPv6GatewayAddressStatus_Type(Integer32):
    """Custom type adGenPppGroupIPv6GatewayAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unverified", 1),
          ("verified", 2),
          ("mismatch", 3),
          ("na", 4))
    )


_AdGenPppGroupIPv6GatewayAddressStatus_Type.__name__ = "Integer32"
_AdGenPppGroupIPv6GatewayAddressStatus_Object = MibTableColumn
adGenPppGroupIPv6GatewayAddressStatus = _AdGenPppGroupIPv6GatewayAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1, 8),
    _AdGenPppGroupIPv6GatewayAddressStatus_Type()
)
adGenPppGroupIPv6GatewayAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIPv6GatewayAddressStatus.setStatus("current")


class _AdGenPppGroupIPv6NCPState_Type(Integer32):
    """Custom type adGenPppGroupIPv6NCPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("reqsent", 7),
          ("ackrcvd", 8),
          ("acksent", 9),
          ("opened", 10))
    )


_AdGenPppGroupIPv6NCPState_Type.__name__ = "Integer32"
_AdGenPppGroupIPv6NCPState_Object = MibTableColumn
adGenPppGroupIPv6NCPState = _AdGenPppGroupIPv6NCPState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 2, 1, 1, 9),
    _AdGenPppGroupIPv6NCPState_Type()
)
adGenPppGroupIPv6NCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIPv6NCPState.setStatus("current")
_AdGenPppGroupPerfStats_ObjectIdentity = ObjectIdentity
adGenPppGroupPerfStats = _AdGenPppGroupPerfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3)
)
_AdGenPppGroupPerfTable_Object = MibTable
adGenPppGroupPerfTable = _AdGenPppGroupPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    adGenPppGroupPerfTable.setStatus("current")
_AdGenPppGroupPerfEntry_Object = MibTableRow
adGenPppGroupPerfEntry = _AdGenPppGroupPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1)
)
adGenPppGroupPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppGroupPerfEntry.setStatus("current")
_AdGenPppGroupInOctets_Type = Counter32
_AdGenPppGroupInOctets_Object = MibTableColumn
adGenPppGroupInOctets = _AdGenPppGroupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 1),
    _AdGenPppGroupInOctets_Type()
)
adGenPppGroupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupInOctets.setStatus("current")
_AdGenPppGroupInPkts_Type = Counter32
_AdGenPppGroupInPkts_Object = MibTableColumn
adGenPppGroupInPkts = _AdGenPppGroupInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 2),
    _AdGenPppGroupInPkts_Type()
)
adGenPppGroupInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupInPkts.setStatus("current")
_AdGenPppGroupInDiscards_Type = Counter32
_AdGenPppGroupInDiscards_Object = MibTableColumn
adGenPppGroupInDiscards = _AdGenPppGroupInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 3),
    _AdGenPppGroupInDiscards_Type()
)
adGenPppGroupInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupInDiscards.setStatus("current")
_AdGenPppGroupInErrors_Type = Counter32
_AdGenPppGroupInErrors_Object = MibTableColumn
adGenPppGroupInErrors = _AdGenPppGroupInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 4),
    _AdGenPppGroupInErrors_Type()
)
adGenPppGroupInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupInErrors.setStatus("current")
_AdGenPppGroupOutOctets_Type = Counter32
_AdGenPppGroupOutOctets_Object = MibTableColumn
adGenPppGroupOutOctets = _AdGenPppGroupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 5),
    _AdGenPppGroupOutOctets_Type()
)
adGenPppGroupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupOutOctets.setStatus("current")
_AdGenPppGroupOutPkts_Type = Counter32
_AdGenPppGroupOutPkts_Object = MibTableColumn
adGenPppGroupOutPkts = _AdGenPppGroupOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 6),
    _AdGenPppGroupOutPkts_Type()
)
adGenPppGroupOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupOutPkts.setStatus("current")
_AdGenPppGroupOutDiscards_Type = Counter32
_AdGenPppGroupOutDiscards_Object = MibTableColumn
adGenPppGroupOutDiscards = _AdGenPppGroupOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 7),
    _AdGenPppGroupOutDiscards_Type()
)
adGenPppGroupOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupOutDiscards.setStatus("current")
_AdGenPppGroupOutErrors_Type = Counter32
_AdGenPppGroupOutErrors_Object = MibTableColumn
adGenPppGroupOutErrors = _AdGenPppGroupOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 8),
    _AdGenPppGroupOutErrors_Type()
)
adGenPppGroupOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupOutErrors.setStatus("current")


class _AdGenPppGroupValidIntervals_Type(Integer32):
    """Custom type adGenPppGroupValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenPppGroupValidIntervals_Type.__name__ = "Integer32"
_AdGenPppGroupValidIntervals_Object = MibTableColumn
adGenPppGroupValidIntervals = _AdGenPppGroupValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 9),
    _AdGenPppGroupValidIntervals_Type()
)
adGenPppGroupValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupValidIntervals.setStatus("current")


class _AdGenPppGroupInvalidIntervals_Type(Integer32):
    """Custom type adGenPppGroupInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenPppGroupInvalidIntervals_Type.__name__ = "Integer32"
_AdGenPppGroupInvalidIntervals_Object = MibTableColumn
adGenPppGroupInvalidIntervals = _AdGenPppGroupInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 10),
    _AdGenPppGroupInvalidIntervals_Type()
)
adGenPppGroupInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupInvalidIntervals.setStatus("current")


class _AdGenPppGroupTimeElapsed_Type(Integer32):
    """Custom type adGenPppGroupTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdGenPppGroupTimeElapsed_Type.__name__ = "Integer32"
_AdGenPppGroupTimeElapsed_Object = MibTableColumn
adGenPppGroupTimeElapsed = _AdGenPppGroupTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 11),
    _AdGenPppGroupTimeElapsed_Type()
)
adGenPppGroupTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTimeElapsed.setStatus("current")


class _AdGenPppGroupResetStats_Type(Integer32):
    """Custom type adGenPppGroupResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenPppGroupResetStats_Type.__name__ = "Integer32"
_AdGenPppGroupResetStats_Object = MibTableColumn
adGenPppGroupResetStats = _AdGenPppGroupResetStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 12),
    _AdGenPppGroupResetStats_Type()
)
adGenPppGroupResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupResetStats.setStatus("current")


class _AdGenPppGroupResetPerfHistory_Type(Integer32):
    """Custom type adGenPppGroupResetPerfHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenPppGroupResetPerfHistory_Type.__name__ = "Integer32"
_AdGenPppGroupResetPerfHistory_Object = MibTableColumn
adGenPppGroupResetPerfHistory = _AdGenPppGroupResetPerfHistory_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 13),
    _AdGenPppGroupResetPerfHistory_Type()
)
adGenPppGroupResetPerfHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPppGroupResetPerfHistory.setStatus("current")
_AdGenPppGroupInL3Pkts_Type = Counter32
_AdGenPppGroupInL3Pkts_Object = MibTableColumn
adGenPppGroupInL3Pkts = _AdGenPppGroupInL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 14),
    _AdGenPppGroupInL3Pkts_Type()
)
adGenPppGroupInL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupInL3Pkts.setStatus("current")
_AdGenPppGroupOutL3Pkts_Type = Counter32
_AdGenPppGroupOutL3Pkts_Object = MibTableColumn
adGenPppGroupOutL3Pkts = _AdGenPppGroupOutL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 1, 1, 15),
    _AdGenPppGroupOutL3Pkts_Type()
)
adGenPppGroupOutL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupOutL3Pkts.setStatus("current")
_AdGenPppGroupCurrentTable_Object = MibTable
adGenPppGroupCurrentTable = _AdGenPppGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    adGenPppGroupCurrentTable.setStatus("current")
_AdGenPppGroupCurrentEntry_Object = MibTableRow
adGenPppGroupCurrentEntry = _AdGenPppGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1)
)
adGenPppGroupCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppGroupCurrentEntry.setStatus("current")
_AdGenPppGroupCurrentInOctets_Type = Gauge32
_AdGenPppGroupCurrentInOctets_Object = MibTableColumn
adGenPppGroupCurrentInOctets = _AdGenPppGroupCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 1),
    _AdGenPppGroupCurrentInOctets_Type()
)
adGenPppGroupCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentInOctets.setStatus("current")
_AdGenPppGroupCurrentInPkts_Type = Gauge32
_AdGenPppGroupCurrentInPkts_Object = MibTableColumn
adGenPppGroupCurrentInPkts = _AdGenPppGroupCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 2),
    _AdGenPppGroupCurrentInPkts_Type()
)
adGenPppGroupCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentInPkts.setStatus("current")
_AdGenPppGroupCurrentInDiscards_Type = Gauge32
_AdGenPppGroupCurrentInDiscards_Object = MibTableColumn
adGenPppGroupCurrentInDiscards = _AdGenPppGroupCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 3),
    _AdGenPppGroupCurrentInDiscards_Type()
)
adGenPppGroupCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentInDiscards.setStatus("current")
_AdGenPppGroupCurrentInErrors_Type = Gauge32
_AdGenPppGroupCurrentInErrors_Object = MibTableColumn
adGenPppGroupCurrentInErrors = _AdGenPppGroupCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 4),
    _AdGenPppGroupCurrentInErrors_Type()
)
adGenPppGroupCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentInErrors.setStatus("current")
_AdGenPppGroupCurrentOutOctets_Type = Gauge32
_AdGenPppGroupCurrentOutOctets_Object = MibTableColumn
adGenPppGroupCurrentOutOctets = _AdGenPppGroupCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 5),
    _AdGenPppGroupCurrentOutOctets_Type()
)
adGenPppGroupCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentOutOctets.setStatus("current")
_AdGenPppGroupCurrentOutPkts_Type = Gauge32
_AdGenPppGroupCurrentOutPkts_Object = MibTableColumn
adGenPppGroupCurrentOutPkts = _AdGenPppGroupCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 6),
    _AdGenPppGroupCurrentOutPkts_Type()
)
adGenPppGroupCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentOutPkts.setStatus("current")
_AdGenPppGroupCurrentOutDiscards_Type = Gauge32
_AdGenPppGroupCurrentOutDiscards_Object = MibTableColumn
adGenPppGroupCurrentOutDiscards = _AdGenPppGroupCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 7),
    _AdGenPppGroupCurrentOutDiscards_Type()
)
adGenPppGroupCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentOutDiscards.setStatus("current")
_AdGenPppGroupCurrentOutErrors_Type = Gauge32
_AdGenPppGroupCurrentOutErrors_Object = MibTableColumn
adGenPppGroupCurrentOutErrors = _AdGenPppGroupCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 8),
    _AdGenPppGroupCurrentOutErrors_Type()
)
adGenPppGroupCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentOutErrors.setStatus("current")
_AdGenPppGroupCurrentInL3Pkts_Type = Gauge32
_AdGenPppGroupCurrentInL3Pkts_Object = MibTableColumn
adGenPppGroupCurrentInL3Pkts = _AdGenPppGroupCurrentInL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 9),
    _AdGenPppGroupCurrentInL3Pkts_Type()
)
adGenPppGroupCurrentInL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentInL3Pkts.setStatus("current")
_AdGenPppGroupCurrentOutL3Pkts_Type = Gauge32
_AdGenPppGroupCurrentOutL3Pkts_Object = MibTableColumn
adGenPppGroupCurrentOutL3Pkts = _AdGenPppGroupCurrentOutL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 2, 1, 10),
    _AdGenPppGroupCurrentOutL3Pkts_Type()
)
adGenPppGroupCurrentOutL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupCurrentOutL3Pkts.setStatus("current")
_AdGenPppGroupIntervalTable_Object = MibTable
adGenPppGroupIntervalTable = _AdGenPppGroupIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    adGenPppGroupIntervalTable.setStatus("current")
_AdGenPppGroupIntervalEntry_Object = MibTableRow
adGenPppGroupIntervalEntry = _AdGenPppGroupIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1)
)
adGenPppGroupIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-PPP-MIB", "adGenPppGroupIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenPppGroupIntervalEntry.setStatus("current")


class _AdGenPppGroupIntervalNumber_Type(Integer32):
    """Custom type adGenPppGroupIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenPppGroupIntervalNumber_Type.__name__ = "Integer32"
_AdGenPppGroupIntervalNumber_Object = MibTableColumn
adGenPppGroupIntervalNumber = _AdGenPppGroupIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 1),
    _AdGenPppGroupIntervalNumber_Type()
)
adGenPppGroupIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalNumber.setStatus("current")
_AdGenPppGroupIntervalInOctets_Type = Gauge32
_AdGenPppGroupIntervalInOctets_Object = MibTableColumn
adGenPppGroupIntervalInOctets = _AdGenPppGroupIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 2),
    _AdGenPppGroupIntervalInOctets_Type()
)
adGenPppGroupIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalInOctets.setStatus("current")
_AdGenPppGroupIntervalInPkts_Type = Gauge32
_AdGenPppGroupIntervalInPkts_Object = MibTableColumn
adGenPppGroupIntervalInPkts = _AdGenPppGroupIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 3),
    _AdGenPppGroupIntervalInPkts_Type()
)
adGenPppGroupIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalInPkts.setStatus("current")
_AdGenPppGroupIntervalInDiscards_Type = Gauge32
_AdGenPppGroupIntervalInDiscards_Object = MibTableColumn
adGenPppGroupIntervalInDiscards = _AdGenPppGroupIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 4),
    _AdGenPppGroupIntervalInDiscards_Type()
)
adGenPppGroupIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalInDiscards.setStatus("current")
_AdGenPppGroupIntervalInErrors_Type = Gauge32
_AdGenPppGroupIntervalInErrors_Object = MibTableColumn
adGenPppGroupIntervalInErrors = _AdGenPppGroupIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 5),
    _AdGenPppGroupIntervalInErrors_Type()
)
adGenPppGroupIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalInErrors.setStatus("current")
_AdGenPppGroupIntervalOutOctets_Type = Gauge32
_AdGenPppGroupIntervalOutOctets_Object = MibTableColumn
adGenPppGroupIntervalOutOctets = _AdGenPppGroupIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 6),
    _AdGenPppGroupIntervalOutOctets_Type()
)
adGenPppGroupIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalOutOctets.setStatus("current")
_AdGenPppGroupIntervalOutPkts_Type = Gauge32
_AdGenPppGroupIntervalOutPkts_Object = MibTableColumn
adGenPppGroupIntervalOutPkts = _AdGenPppGroupIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 7),
    _AdGenPppGroupIntervalOutPkts_Type()
)
adGenPppGroupIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalOutPkts.setStatus("current")
_AdGenPppGroupIntervalOutDiscards_Type = Gauge32
_AdGenPppGroupIntervalOutDiscards_Object = MibTableColumn
adGenPppGroupIntervalOutDiscards = _AdGenPppGroupIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 8),
    _AdGenPppGroupIntervalOutDiscards_Type()
)
adGenPppGroupIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalOutDiscards.setStatus("current")
_AdGenPppGroupIntervalOutErrors_Type = Gauge32
_AdGenPppGroupIntervalOutErrors_Object = MibTableColumn
adGenPppGroupIntervalOutErrors = _AdGenPppGroupIntervalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 9),
    _AdGenPppGroupIntervalOutErrors_Type()
)
adGenPppGroupIntervalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalOutErrors.setStatus("current")
_AdGenPppGroupIntervalTimeStamp_Type = DisplayString
_AdGenPppGroupIntervalTimeStamp_Object = MibTableColumn
adGenPppGroupIntervalTimeStamp = _AdGenPppGroupIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 10),
    _AdGenPppGroupIntervalTimeStamp_Type()
)
adGenPppGroupIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalTimeStamp.setStatus("current")
_AdGenPppGroupIntervalInL3Pkts_Type = Gauge32
_AdGenPppGroupIntervalInL3Pkts_Object = MibTableColumn
adGenPppGroupIntervalInL3Pkts = _AdGenPppGroupIntervalInL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 11),
    _AdGenPppGroupIntervalInL3Pkts_Type()
)
adGenPppGroupIntervalInL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalInL3Pkts.setStatus("current")
_AdGenPppGroupIntervalOutL3Pkts_Type = Gauge32
_AdGenPppGroupIntervalOutL3Pkts_Object = MibTableColumn
adGenPppGroupIntervalOutL3Pkts = _AdGenPppGroupIntervalOutL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 3, 1, 12),
    _AdGenPppGroupIntervalOutL3Pkts_Type()
)
adGenPppGroupIntervalOutL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupIntervalOutL3Pkts.setStatus("current")
_AdGenPppGroupTotalTable_Object = MibTable
adGenPppGroupTotalTable = _AdGenPppGroupTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    adGenPppGroupTotalTable.setStatus("current")
_AdGenPppGroupTotalEntry_Object = MibTableRow
adGenPppGroupTotalEntry = _AdGenPppGroupTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1)
)
adGenPppGroupTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppGroupTotalEntry.setStatus("current")
_AdGenPppGroupTotalInOctets_Type = Gauge32
_AdGenPppGroupTotalInOctets_Object = MibTableColumn
adGenPppGroupTotalInOctets = _AdGenPppGroupTotalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 1),
    _AdGenPppGroupTotalInOctets_Type()
)
adGenPppGroupTotalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalInOctets.setStatus("current")
_AdGenPppGroupTotalInPkts_Type = Gauge32
_AdGenPppGroupTotalInPkts_Object = MibTableColumn
adGenPppGroupTotalInPkts = _AdGenPppGroupTotalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 2),
    _AdGenPppGroupTotalInPkts_Type()
)
adGenPppGroupTotalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalInPkts.setStatus("current")
_AdGenPppGroupTotalInDiscards_Type = Gauge32
_AdGenPppGroupTotalInDiscards_Object = MibTableColumn
adGenPppGroupTotalInDiscards = _AdGenPppGroupTotalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 3),
    _AdGenPppGroupTotalInDiscards_Type()
)
adGenPppGroupTotalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalInDiscards.setStatus("current")
_AdGenPppGroupTotalInErrors_Type = Gauge32
_AdGenPppGroupTotalInErrors_Object = MibTableColumn
adGenPppGroupTotalInErrors = _AdGenPppGroupTotalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 4),
    _AdGenPppGroupTotalInErrors_Type()
)
adGenPppGroupTotalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalInErrors.setStatus("current")
_AdGenPppGroupTotalOutOctets_Type = Gauge32
_AdGenPppGroupTotalOutOctets_Object = MibTableColumn
adGenPppGroupTotalOutOctets = _AdGenPppGroupTotalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 5),
    _AdGenPppGroupTotalOutOctets_Type()
)
adGenPppGroupTotalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalOutOctets.setStatus("current")
_AdGenPppGroupTotalOutPkts_Type = Gauge32
_AdGenPppGroupTotalOutPkts_Object = MibTableColumn
adGenPppGroupTotalOutPkts = _AdGenPppGroupTotalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 6),
    _AdGenPppGroupTotalOutPkts_Type()
)
adGenPppGroupTotalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalOutPkts.setStatus("current")
_AdGenPppGroupTotalOutDiscards_Type = Gauge32
_AdGenPppGroupTotalOutDiscards_Object = MibTableColumn
adGenPppGroupTotalOutDiscards = _AdGenPppGroupTotalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 7),
    _AdGenPppGroupTotalOutDiscards_Type()
)
adGenPppGroupTotalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalOutDiscards.setStatus("current")
_AdGenPppGroupTotalOutErrors_Type = Gauge32
_AdGenPppGroupTotalOutErrors_Object = MibTableColumn
adGenPppGroupTotalOutErrors = _AdGenPppGroupTotalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 8),
    _AdGenPppGroupTotalOutErrors_Type()
)
adGenPppGroupTotalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalOutErrors.setStatus("current")
_AdGenPppGroupTotalInL3Pkts_Type = Gauge32
_AdGenPppGroupTotalInL3Pkts_Object = MibTableColumn
adGenPppGroupTotalInL3Pkts = _AdGenPppGroupTotalInL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 9),
    _AdGenPppGroupTotalInL3Pkts_Type()
)
adGenPppGroupTotalInL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalInL3Pkts.setStatus("current")
_AdGenPppGroupTotalOutL3Pkts_Type = Gauge32
_AdGenPppGroupTotalOutL3Pkts_Object = MibTableColumn
adGenPppGroupTotalOutL3Pkts = _AdGenPppGroupTotalOutL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 4, 1, 10),
    _AdGenPppGroupTotalOutL3Pkts_Type()
)
adGenPppGroupTotalOutL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupTotalOutL3Pkts.setStatus("current")
_AdGenPppGroupDayCurrentTable_Object = MibTable
adGenPppGroupDayCurrentTable = _AdGenPppGroupDayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentTable.setStatus("current")
_AdGenPppGroupDayCurrentEntry_Object = MibTableRow
adGenPppGroupDayCurrentEntry = _AdGenPppGroupDayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1)
)
adGenPppGroupDayCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentEntry.setStatus("current")
_AdGenPppGroupDayCurrentInOctets_Type = Gauge32
_AdGenPppGroupDayCurrentInOctets_Object = MibTableColumn
adGenPppGroupDayCurrentInOctets = _AdGenPppGroupDayCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 1),
    _AdGenPppGroupDayCurrentInOctets_Type()
)
adGenPppGroupDayCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentInOctets.setStatus("current")
_AdGenPppGroupDayCurrentInPkts_Type = Gauge32
_AdGenPppGroupDayCurrentInPkts_Object = MibTableColumn
adGenPppGroupDayCurrentInPkts = _AdGenPppGroupDayCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 2),
    _AdGenPppGroupDayCurrentInPkts_Type()
)
adGenPppGroupDayCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentInPkts.setStatus("current")
_AdGenPppGroupDayCurrentInDiscards_Type = Gauge32
_AdGenPppGroupDayCurrentInDiscards_Object = MibTableColumn
adGenPppGroupDayCurrentInDiscards = _AdGenPppGroupDayCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 3),
    _AdGenPppGroupDayCurrentInDiscards_Type()
)
adGenPppGroupDayCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentInDiscards.setStatus("current")
_AdGenPppGroupDayCurrentInErrors_Type = Gauge32
_AdGenPppGroupDayCurrentInErrors_Object = MibTableColumn
adGenPppGroupDayCurrentInErrors = _AdGenPppGroupDayCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 4),
    _AdGenPppGroupDayCurrentInErrors_Type()
)
adGenPppGroupDayCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentInErrors.setStatus("current")
_AdGenPppGroupDayCurrentOutOctets_Type = Gauge32
_AdGenPppGroupDayCurrentOutOctets_Object = MibTableColumn
adGenPppGroupDayCurrentOutOctets = _AdGenPppGroupDayCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 5),
    _AdGenPppGroupDayCurrentOutOctets_Type()
)
adGenPppGroupDayCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentOutOctets.setStatus("current")
_AdGenPppGroupDayCurrentOutPkts_Type = Gauge32
_AdGenPppGroupDayCurrentOutPkts_Object = MibTableColumn
adGenPppGroupDayCurrentOutPkts = _AdGenPppGroupDayCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 6),
    _AdGenPppGroupDayCurrentOutPkts_Type()
)
adGenPppGroupDayCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentOutPkts.setStatus("current")
_AdGenPppGroupDayCurrentOutDiscards_Type = Gauge32
_AdGenPppGroupDayCurrentOutDiscards_Object = MibTableColumn
adGenPppGroupDayCurrentOutDiscards = _AdGenPppGroupDayCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 7),
    _AdGenPppGroupDayCurrentOutDiscards_Type()
)
adGenPppGroupDayCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentOutDiscards.setStatus("current")
_AdGenPppGroupDayCurrentOutErrors_Type = Gauge32
_AdGenPppGroupDayCurrentOutErrors_Object = MibTableColumn
adGenPppGroupDayCurrentOutErrors = _AdGenPppGroupDayCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 8),
    _AdGenPppGroupDayCurrentOutErrors_Type()
)
adGenPppGroupDayCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentOutErrors.setStatus("current")
_AdGenPppGroupDayCurrentInL3Pkts_Type = Gauge32
_AdGenPppGroupDayCurrentInL3Pkts_Object = MibTableColumn
adGenPppGroupDayCurrentInL3Pkts = _AdGenPppGroupDayCurrentInL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 9),
    _AdGenPppGroupDayCurrentInL3Pkts_Type()
)
adGenPppGroupDayCurrentInL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentInL3Pkts.setStatus("current")
_AdGenPppGroupDayCurrentOutL3Pkts_Type = Gauge32
_AdGenPppGroupDayCurrentOutL3Pkts_Object = MibTableColumn
adGenPppGroupDayCurrentOutL3Pkts = _AdGenPppGroupDayCurrentOutL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 5, 1, 10),
    _AdGenPppGroupDayCurrentOutL3Pkts_Type()
)
adGenPppGroupDayCurrentOutL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayCurrentOutL3Pkts.setStatus("current")
_AdGenPppGroupDayIntervalTable_Object = MibTable
adGenPppGroupDayIntervalTable = _AdGenPppGroupDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalTable.setStatus("current")
_AdGenPppGroupDayIntervalEntry_Object = MibTableRow
adGenPppGroupDayIntervalEntry = _AdGenPppGroupDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1)
)
adGenPppGroupDayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-PPP-MIB", "adGenPppGroupDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalEntry.setStatus("current")


class _AdGenPppGroupDayIntervalNumber_Type(Integer32):
    """Custom type adGenPppGroupDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenPppGroupDayIntervalNumber_Type.__name__ = "Integer32"
_AdGenPppGroupDayIntervalNumber_Object = MibTableColumn
adGenPppGroupDayIntervalNumber = _AdGenPppGroupDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 1),
    _AdGenPppGroupDayIntervalNumber_Type()
)
adGenPppGroupDayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalNumber.setStatus("current")
_AdGenPppGroupDayIntervalInOctets_Type = Gauge32
_AdGenPppGroupDayIntervalInOctets_Object = MibTableColumn
adGenPppGroupDayIntervalInOctets = _AdGenPppGroupDayIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 2),
    _AdGenPppGroupDayIntervalInOctets_Type()
)
adGenPppGroupDayIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalInOctets.setStatus("current")
_AdGenPppGroupDayIntervalInPkts_Type = Gauge32
_AdGenPppGroupDayIntervalInPkts_Object = MibTableColumn
adGenPppGroupDayIntervalInPkts = _AdGenPppGroupDayIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 3),
    _AdGenPppGroupDayIntervalInPkts_Type()
)
adGenPppGroupDayIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalInPkts.setStatus("current")
_AdGenPppGroupDayIntervalInDiscards_Type = Gauge32
_AdGenPppGroupDayIntervalInDiscards_Object = MibTableColumn
adGenPppGroupDayIntervalInDiscards = _AdGenPppGroupDayIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 4),
    _AdGenPppGroupDayIntervalInDiscards_Type()
)
adGenPppGroupDayIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalInDiscards.setStatus("current")
_AdGenPppGroupDayIntervalInErrors_Type = Gauge32
_AdGenPppGroupDayIntervalInErrors_Object = MibTableColumn
adGenPppGroupDayIntervalInErrors = _AdGenPppGroupDayIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 5),
    _AdGenPppGroupDayIntervalInErrors_Type()
)
adGenPppGroupDayIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalInErrors.setStatus("current")
_AdGenPppGroupDayIntervalOutOctets_Type = Gauge32
_AdGenPppGroupDayIntervalOutOctets_Object = MibTableColumn
adGenPppGroupDayIntervalOutOctets = _AdGenPppGroupDayIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 6),
    _AdGenPppGroupDayIntervalOutOctets_Type()
)
adGenPppGroupDayIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalOutOctets.setStatus("current")
_AdGenPppGroupDayIntervalOutPkts_Type = Gauge32
_AdGenPppGroupDayIntervalOutPkts_Object = MibTableColumn
adGenPppGroupDayIntervalOutPkts = _AdGenPppGroupDayIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 7),
    _AdGenPppGroupDayIntervalOutPkts_Type()
)
adGenPppGroupDayIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalOutPkts.setStatus("current")
_AdGenPppGroupDayIntervalOutDiscards_Type = Gauge32
_AdGenPppGroupDayIntervalOutDiscards_Object = MibTableColumn
adGenPppGroupDayIntervalOutDiscards = _AdGenPppGroupDayIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 8),
    _AdGenPppGroupDayIntervalOutDiscards_Type()
)
adGenPppGroupDayIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalOutDiscards.setStatus("current")
_AdGenPppGroupDayIntervalOutErrors_Type = Gauge32
_AdGenPppGroupDayIntervalOutErrors_Object = MibTableColumn
adGenPppGroupDayIntervalOutErrors = _AdGenPppGroupDayIntervalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 9),
    _AdGenPppGroupDayIntervalOutErrors_Type()
)
adGenPppGroupDayIntervalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalOutErrors.setStatus("current")
_AdGenPppGroupDayIntervalTimeStamp_Type = DisplayString
_AdGenPppGroupDayIntervalTimeStamp_Object = MibTableColumn
adGenPppGroupDayIntervalTimeStamp = _AdGenPppGroupDayIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 10),
    _AdGenPppGroupDayIntervalTimeStamp_Type()
)
adGenPppGroupDayIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalTimeStamp.setStatus("current")
_AdGenPppGroupDayIntervalInL3Pkts_Type = Gauge32
_AdGenPppGroupDayIntervalInL3Pkts_Object = MibTableColumn
adGenPppGroupDayIntervalInL3Pkts = _AdGenPppGroupDayIntervalInL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 11),
    _AdGenPppGroupDayIntervalInL3Pkts_Type()
)
adGenPppGroupDayIntervalInL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalInL3Pkts.setStatus("current")
_AdGenPppGroupDayIntervalOutL3Pkts_Type = Gauge32
_AdGenPppGroupDayIntervalOutL3Pkts_Object = MibTableColumn
adGenPppGroupDayIntervalOutL3Pkts = _AdGenPppGroupDayIntervalOutL3Pkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 1, 2, 3, 6, 1, 12),
    _AdGenPppGroupDayIntervalOutL3Pkts_Type()
)
adGenPppGroupDayIntervalOutL3Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPppGroupDayIntervalOutL3Pkts.setStatus("current")
_AdGenPppAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenPppAlarmsPrefix = _AdGenPppAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2)
)
_AdGenPppAlarms_ObjectIdentity = ObjectIdentity
adGenPppAlarms = _AdGenPppAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0)
)

# Managed Objects groups


# Notification objects

adGenPppLinkLcpDownAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 2)
)
adGenPppLinkLcpDownAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppLinkLcpDownAlarmClr.setStatus(
        "current"
    )

adGenPppLinkLcpDownAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 3)
)
adGenPppLinkLcpDownAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppLinkLcpDownAlarmAct.setStatus(
        "current"
    )

adGenPppGroupNcpDownAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 4)
)
adGenPppGroupNcpDownAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppGroupNcpDownAlarmClr.setStatus(
        "current"
    )

adGenPppGroupNcpDownAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 5)
)
adGenPppGroupNcpDownAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppGroupNcpDownAlarmAct.setStatus(
        "current"
    )

adGenPppGroupIpv6NcpDownAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 6)
)
adGenPppGroupIpv6NcpDownAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppGroupIpv6NcpDownAlarmClr.setStatus(
        "current"
    )

adGenPppGroupIpv6NcpDownAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 7)
)
adGenPppGroupIpv6NcpDownAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppGroupIpv6NcpDownAlarmAct.setStatus(
        "current"
    )

adGenPppGroupIpv6AddrMismatchAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 8)
)
adGenPppGroupIpv6AddrMismatchAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppGroupIpv6AddrMismatchAlarmClr.setStatus(
        "current"
    )

adGenPppGroupIpv6AddrMismatchAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 9)
)
adGenPppGroupIpv6AddrMismatchAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppGroupIpv6AddrMismatchAlarmAct.setStatus(
        "current"
    )

adGenPppGroupIpv6GatewayAddrMismatchAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 10)
)
adGenPppGroupIpv6GatewayAddrMismatchAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppGroupIpv6GatewayAddrMismatchAlarmClr.setStatus(
        "current"
    )

adGenPppGroupIpv6GatewayAddrMismatchAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 31, 2, 0, 11)
)
adGenPppGroupIpv6GatewayAddrMismatchAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenPppGroupIpv6GatewayAddrMismatchAlarmAct.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-PPP-MIB",
    **{"adGenPppMIBObjects": adGenPppMIBObjects,
       "adGenPppLinkObjects": adGenPppLinkObjects,
       "adGenPppLinkProv": adGenPppLinkProv,
       "adGenPppLinkAlarmProvTable": adGenPppLinkAlarmProvTable,
       "adGenPppLinkAlarmProvEntry": adGenPppLinkAlarmProvEntry,
       "adGenPppLinkAlarmProvLCPAlarmSeverity": adGenPppLinkAlarmProvLCPAlarmSeverity,
       "adGenPppLinkAlarmProvLCPAlarmSuppression": adGenPppLinkAlarmProvLCPAlarmSuppression,
       "adGenPppLinkAlarmProvLCPAlarmEnable": adGenPppLinkAlarmProvLCPAlarmEnable,
       "adGenPppLinkStatus": adGenPppLinkStatus,
       "adGenPppLinkStatusTable": adGenPppLinkStatusTable,
       "adGenPppLinkStatusEntry": adGenPppLinkStatusEntry,
       "adGenPppLinkOperStatus": adGenPppLinkOperStatus,
       "adGenPppLinkCurrentLCPState": adGenPppLinkCurrentLCPState,
       "adGenPppLinkNegotiatedStatus": adGenPppLinkNegotiatedStatus,
       "adGenPppLinkPerfStats": adGenPppLinkPerfStats,
       "adGenPppLinkPerfTable": adGenPppLinkPerfTable,
       "adGenPppLinkPerfEntry": adGenPppLinkPerfEntry,
       "adGenPppLinkInOctets": adGenPppLinkInOctets,
       "adGenPppLinkInGoodOctets": adGenPppLinkInGoodOctets,
       "adGenPppLinkInPkts": adGenPppLinkInPkts,
       "adGenPppLinkInDiscards": adGenPppLinkInDiscards,
       "adGenPppLinkInErrors": adGenPppLinkInErrors,
       "adGenPppLinkOutOctets": adGenPppLinkOutOctets,
       "adGenPppLinkOutPkts": adGenPppLinkOutPkts,
       "adGenPppLinkOutDiscards": adGenPppLinkOutDiscards,
       "adGenPppLinkOutErrors": adGenPppLinkOutErrors,
       "adGenPppLinkValidIntervals": adGenPppLinkValidIntervals,
       "adGenPppLinkInvalidIntervals": adGenPppLinkInvalidIntervals,
       "adGenPppLinkTimeElapsed": adGenPppLinkTimeElapsed,
       "adGenPppLinkResetStats": adGenPppLinkResetStats,
       "adGenPppLinkResetPerfHistory": adGenPppLinkResetPerfHistory,
       "adGenPppLinkCurrentTable": adGenPppLinkCurrentTable,
       "adGenPppLinkCurrentEntry": adGenPppLinkCurrentEntry,
       "adGenPppLinkCurrentInOctets": adGenPppLinkCurrentInOctets,
       "adGenPppLinkCurrentInGoodOctets": adGenPppLinkCurrentInGoodOctets,
       "adGenPppLinkCurrentInPkts": adGenPppLinkCurrentInPkts,
       "adGenPppLinkCurrentInDiscards": adGenPppLinkCurrentInDiscards,
       "adGenPppLinkCurrentInErrors": adGenPppLinkCurrentInErrors,
       "adGenPppLinkCurrentOutOctets": adGenPppLinkCurrentOutOctets,
       "adGenPppLinkCurrentOutPkts": adGenPppLinkCurrentOutPkts,
       "adGenPppLinkCurrentOutDiscards": adGenPppLinkCurrentOutDiscards,
       "adGenPppLinkCurrentOutErrors": adGenPppLinkCurrentOutErrors,
       "adGenPppLinkIntervalTable": adGenPppLinkIntervalTable,
       "adGenPppLinkIntervalEntry": adGenPppLinkIntervalEntry,
       "adGenPppLinkIntervalNumber": adGenPppLinkIntervalNumber,
       "adGenPppLinkIntervalInOctets": adGenPppLinkIntervalInOctets,
       "adGenPppLinkIntervalInGoodOctets": adGenPppLinkIntervalInGoodOctets,
       "adGenPppLinkIntervalInPkts": adGenPppLinkIntervalInPkts,
       "adGenPppLinkIntervalInDiscards": adGenPppLinkIntervalInDiscards,
       "adGenPppLinkIntervalInErrors": adGenPppLinkIntervalInErrors,
       "adGenPppLinkIntervalOutOctets": adGenPppLinkIntervalOutOctets,
       "adGenPppLinkIntervalOutPkts": adGenPppLinkIntervalOutPkts,
       "adGenPppLinkIntervalOutDiscards": adGenPppLinkIntervalOutDiscards,
       "adGenPppLinkIntervalOutErrors": adGenPppLinkIntervalOutErrors,
       "adGenPppLinkIntervalTimeStamp": adGenPppLinkIntervalTimeStamp,
       "adGenPppLinkTotalTable": adGenPppLinkTotalTable,
       "adGenPppLinkTotalEntry": adGenPppLinkTotalEntry,
       "adGenPppLinkTotalInOctets": adGenPppLinkTotalInOctets,
       "adGenPppLinkTotalInGoodOctets": adGenPppLinkTotalInGoodOctets,
       "adGenPppLinkTotalInPkts": adGenPppLinkTotalInPkts,
       "adGenPppLinkTotalInDiscards": adGenPppLinkTotalInDiscards,
       "adGenPppLinkTotalInErrors": adGenPppLinkTotalInErrors,
       "adGenPppLinkTotalOutOctets": adGenPppLinkTotalOutOctets,
       "adGenPppLinkTotalOutPkts": adGenPppLinkTotalOutPkts,
       "adGenPppLinkTotalOutDiscards": adGenPppLinkTotalOutDiscards,
       "adGenPppLinkTotalOutErrors": adGenPppLinkTotalOutErrors,
       "adGenPppLinkDayCurrentTable": adGenPppLinkDayCurrentTable,
       "adGenPppLinkDayCurrentEntry": adGenPppLinkDayCurrentEntry,
       "adGenPppLinkDayCurrentInOctets": adGenPppLinkDayCurrentInOctets,
       "adGenPppLinkDayCurrentInGoodOctets": adGenPppLinkDayCurrentInGoodOctets,
       "adGenPppLinkDayCurrentInPkts": adGenPppLinkDayCurrentInPkts,
       "adGenPppLinkDayCurrentInDiscards": adGenPppLinkDayCurrentInDiscards,
       "adGenPppLinkDayCurrentInErrors": adGenPppLinkDayCurrentInErrors,
       "adGenPppLinkDayCurrentOutOctets": adGenPppLinkDayCurrentOutOctets,
       "adGenPppLinkDayCurrentOutPkts": adGenPppLinkDayCurrentOutPkts,
       "adGenPppLinkDayCurrentOutDiscards": adGenPppLinkDayCurrentOutDiscards,
       "adGenPppLinkDayCurrentOutErrors": adGenPppLinkDayCurrentOutErrors,
       "adGenPppLinkDayIntervalTable": adGenPppLinkDayIntervalTable,
       "adGenPppLinkDayIntervalEntry": adGenPppLinkDayIntervalEntry,
       "adGenPppLinkDayIntervalNumber": adGenPppLinkDayIntervalNumber,
       "adGenPppLinkDayIntervalInOctets": adGenPppLinkDayIntervalInOctets,
       "adGenPppLinkDayIntervalInGoodOctets": adGenPppLinkDayIntervalInGoodOctets,
       "adGenPppLinkDayIntervalInPkts": adGenPppLinkDayIntervalInPkts,
       "adGenPppLinkDayIntervalInDiscards": adGenPppLinkDayIntervalInDiscards,
       "adGenPppLinkDayIntervalInErrors": adGenPppLinkDayIntervalInErrors,
       "adGenPppLinkDayIntervalOutOctets": adGenPppLinkDayIntervalOutOctets,
       "adGenPppLinkDayIntervalOutPkts": adGenPppLinkDayIntervalOutPkts,
       "adGenPppLinkDayIntervalOutDiscards": adGenPppLinkDayIntervalOutDiscards,
       "adGenPppLinkDayIntervalOutErrors": adGenPppLinkDayIntervalOutErrors,
       "adGenPppLinkDayIntervalTimeStamp": adGenPppLinkDayIntervalTimeStamp,
       "adGenPppGroupObjects": adGenPppGroupObjects,
       "adGenPppGroupProv": adGenPppGroupProv,
       "adGenPppGroupProvTable": adGenPppGroupProvTable,
       "adGenPppGroupProvEntry": adGenPppGroupProvEntry,
       "adGenPppGroupSubscriberIpAddress": adGenPppGroupSubscriberIpAddress,
       "adGenPppGroupGatewayIpAddress": adGenPppGroupGatewayIpAddress,
       "adGenPppGroupPrimaryDNSIpAddress": adGenPppGroupPrimaryDNSIpAddress,
       "adGenPppGroupSecondaryDNSIpAddress": adGenPppGroupSecondaryDNSIpAddress,
       "adGenPppGroupConfigInitialMRU": adGenPppGroupConfigInitialMRU,
       "adGenPppGroupConfigMagicNumber": adGenPppGroupConfigMagicNumber,
       "adGenPppGroupConfigFcsSize": adGenPppGroupConfigFcsSize,
       "adGenPppGroupConfigACCompression": adGenPppGroupConfigACCompression,
       "adGenPppGroupConfigPFCompression": adGenPppGroupConfigPFCompression,
       "adGenPppGroupConfigLQM": adGenPppGroupConfigLQM,
       "adGenPppGroupConfigRestartTimer": adGenPppGroupConfigRestartTimer,
       "adGenPppGroupConfigMaxTerminate": adGenPppGroupConfigMaxTerminate,
       "adGenPppGroupConfigMaxConfigure": adGenPppGroupConfigMaxConfigure,
       "adGenPppGroupConfigMaxFailure": adGenPppGroupConfigMaxFailure,
       "adGenPppGroupConfigKeepAliveRate": adGenPppGroupConfigKeepAliveRate,
       "adGenPppGroupChapEnabled": adGenPppGroupChapEnabled,
       "adGenPppGroupLocalUserName": adGenPppGroupLocalUserName,
       "adGenPppGroupLocalPassword": adGenPppGroupLocalPassword,
       "adGenPppGroupPeerUserName": adGenPppGroupPeerUserName,
       "adGenPppGroupPeerPassword": adGenPppGroupPeerPassword,
       "adGenPppGroupIpAddressAssignment": adGenPppGroupIpAddressAssignment,
       "adGenPppGroupDhcpClientIdentfier": adGenPppGroupDhcpClientIdentfier,
       "adGenPppGroupDhcpHostname": adGenPppGroupDhcpHostname,
       "adGenPppGroupConfigMultilink": adGenPppGroupConfigMultilink,
       "adGenPppGroupSubscriberIPv6Address": adGenPppGroupSubscriberIPv6Address,
       "adGenPppGroupGatewayIPv6AddressAssignment": adGenPppGroupGatewayIPv6AddressAssignment,
       "adGenPppGroupGatewayIPv6Address": adGenPppGroupGatewayIPv6Address,
       "adGenPppGroupIpEnabled": adGenPppGroupIpEnabled,
       "adGenPppGroupIpv6Enabled": adGenPppGroupIpv6Enabled,
       "adGenPppGroupAlarmProvTable": adGenPppGroupAlarmProvTable,
       "adGenPppGroupAlarmProvEntry": adGenPppGroupAlarmProvEntry,
       "adGenPppGroupAlarmProvNCPAlarmSeverity": adGenPppGroupAlarmProvNCPAlarmSeverity,
       "adGenPppGroupAlarmProvNCPAlarmSuppression": adGenPppGroupAlarmProvNCPAlarmSuppression,
       "adGenPppGroupAlarmProvNCPAlarmEnable": adGenPppGroupAlarmProvNCPAlarmEnable,
       "adGenPppGroupAlarmProvIpv6NcpAlarmSeverity": adGenPppGroupAlarmProvIpv6NcpAlarmSeverity,
       "adGenPppGroupAlarmProvIpv6NcpAlarmSuppression": adGenPppGroupAlarmProvIpv6NcpAlarmSuppression,
       "adGenPppGroupAlarmProvIpv6NcpAlarmEnable": adGenPppGroupAlarmProvIpv6NcpAlarmEnable,
       "adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity": adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSeverity,
       "adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression": adGenPppGroupAlarmProvIpv6AddrMismatchAlarmSuppression,
       "adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable": adGenPppGroupAlarmProvIpv6AddrMismatchAlarmEnable,
       "adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity": adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSeverity,
       "adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression": adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmSuppression,
       "adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable": adGenPppGroupAlarmProvIpv6GatewayAddrMismatchAlarmEnable,
       "adGenPppGroupStatus": adGenPppGroupStatus,
       "adGenPppGroupStatusTable": adGenPppGroupStatusTable,
       "adGenPppGroupStatusEntry": adGenPppGroupStatusEntry,
       "adGenPppGroupNCPState": adGenPppGroupNCPState,
       "adGenPppGroupCurrentSubscriberIpAddress": adGenPppGroupCurrentSubscriberIpAddress,
       "adGenPppGroupCurrentGatewayIpAddress": adGenPppGroupCurrentGatewayIpAddress,
       "adGenPppGroupCurrentPrimaryDNSIpAddress": adGenPppGroupCurrentPrimaryDNSIpAddress,
       "adGenPppGroupCurrentSecondaryDNSIpAddress": adGenPppGroupCurrentSecondaryDNSIpAddress,
       "adGenPppGroupNegotiatedStatus": adGenPppGroupNegotiatedStatus,
       "adGenPppGroupIPv6AddressStatus": adGenPppGroupIPv6AddressStatus,
       "adGenPppGroupIPv6GatewayAddressStatus": adGenPppGroupIPv6GatewayAddressStatus,
       "adGenPppGroupIPv6NCPState": adGenPppGroupIPv6NCPState,
       "adGenPppGroupPerfStats": adGenPppGroupPerfStats,
       "adGenPppGroupPerfTable": adGenPppGroupPerfTable,
       "adGenPppGroupPerfEntry": adGenPppGroupPerfEntry,
       "adGenPppGroupInOctets": adGenPppGroupInOctets,
       "adGenPppGroupInPkts": adGenPppGroupInPkts,
       "adGenPppGroupInDiscards": adGenPppGroupInDiscards,
       "adGenPppGroupInErrors": adGenPppGroupInErrors,
       "adGenPppGroupOutOctets": adGenPppGroupOutOctets,
       "adGenPppGroupOutPkts": adGenPppGroupOutPkts,
       "adGenPppGroupOutDiscards": adGenPppGroupOutDiscards,
       "adGenPppGroupOutErrors": adGenPppGroupOutErrors,
       "adGenPppGroupValidIntervals": adGenPppGroupValidIntervals,
       "adGenPppGroupInvalidIntervals": adGenPppGroupInvalidIntervals,
       "adGenPppGroupTimeElapsed": adGenPppGroupTimeElapsed,
       "adGenPppGroupResetStats": adGenPppGroupResetStats,
       "adGenPppGroupResetPerfHistory": adGenPppGroupResetPerfHistory,
       "adGenPppGroupInL3Pkts": adGenPppGroupInL3Pkts,
       "adGenPppGroupOutL3Pkts": adGenPppGroupOutL3Pkts,
       "adGenPppGroupCurrentTable": adGenPppGroupCurrentTable,
       "adGenPppGroupCurrentEntry": adGenPppGroupCurrentEntry,
       "adGenPppGroupCurrentInOctets": adGenPppGroupCurrentInOctets,
       "adGenPppGroupCurrentInPkts": adGenPppGroupCurrentInPkts,
       "adGenPppGroupCurrentInDiscards": adGenPppGroupCurrentInDiscards,
       "adGenPppGroupCurrentInErrors": adGenPppGroupCurrentInErrors,
       "adGenPppGroupCurrentOutOctets": adGenPppGroupCurrentOutOctets,
       "adGenPppGroupCurrentOutPkts": adGenPppGroupCurrentOutPkts,
       "adGenPppGroupCurrentOutDiscards": adGenPppGroupCurrentOutDiscards,
       "adGenPppGroupCurrentOutErrors": adGenPppGroupCurrentOutErrors,
       "adGenPppGroupCurrentInL3Pkts": adGenPppGroupCurrentInL3Pkts,
       "adGenPppGroupCurrentOutL3Pkts": adGenPppGroupCurrentOutL3Pkts,
       "adGenPppGroupIntervalTable": adGenPppGroupIntervalTable,
       "adGenPppGroupIntervalEntry": adGenPppGroupIntervalEntry,
       "adGenPppGroupIntervalNumber": adGenPppGroupIntervalNumber,
       "adGenPppGroupIntervalInOctets": adGenPppGroupIntervalInOctets,
       "adGenPppGroupIntervalInPkts": adGenPppGroupIntervalInPkts,
       "adGenPppGroupIntervalInDiscards": adGenPppGroupIntervalInDiscards,
       "adGenPppGroupIntervalInErrors": adGenPppGroupIntervalInErrors,
       "adGenPppGroupIntervalOutOctets": adGenPppGroupIntervalOutOctets,
       "adGenPppGroupIntervalOutPkts": adGenPppGroupIntervalOutPkts,
       "adGenPppGroupIntervalOutDiscards": adGenPppGroupIntervalOutDiscards,
       "adGenPppGroupIntervalOutErrors": adGenPppGroupIntervalOutErrors,
       "adGenPppGroupIntervalTimeStamp": adGenPppGroupIntervalTimeStamp,
       "adGenPppGroupIntervalInL3Pkts": adGenPppGroupIntervalInL3Pkts,
       "adGenPppGroupIntervalOutL3Pkts": adGenPppGroupIntervalOutL3Pkts,
       "adGenPppGroupTotalTable": adGenPppGroupTotalTable,
       "adGenPppGroupTotalEntry": adGenPppGroupTotalEntry,
       "adGenPppGroupTotalInOctets": adGenPppGroupTotalInOctets,
       "adGenPppGroupTotalInPkts": adGenPppGroupTotalInPkts,
       "adGenPppGroupTotalInDiscards": adGenPppGroupTotalInDiscards,
       "adGenPppGroupTotalInErrors": adGenPppGroupTotalInErrors,
       "adGenPppGroupTotalOutOctets": adGenPppGroupTotalOutOctets,
       "adGenPppGroupTotalOutPkts": adGenPppGroupTotalOutPkts,
       "adGenPppGroupTotalOutDiscards": adGenPppGroupTotalOutDiscards,
       "adGenPppGroupTotalOutErrors": adGenPppGroupTotalOutErrors,
       "adGenPppGroupTotalInL3Pkts": adGenPppGroupTotalInL3Pkts,
       "adGenPppGroupTotalOutL3Pkts": adGenPppGroupTotalOutL3Pkts,
       "adGenPppGroupDayCurrentTable": adGenPppGroupDayCurrentTable,
       "adGenPppGroupDayCurrentEntry": adGenPppGroupDayCurrentEntry,
       "adGenPppGroupDayCurrentInOctets": adGenPppGroupDayCurrentInOctets,
       "adGenPppGroupDayCurrentInPkts": adGenPppGroupDayCurrentInPkts,
       "adGenPppGroupDayCurrentInDiscards": adGenPppGroupDayCurrentInDiscards,
       "adGenPppGroupDayCurrentInErrors": adGenPppGroupDayCurrentInErrors,
       "adGenPppGroupDayCurrentOutOctets": adGenPppGroupDayCurrentOutOctets,
       "adGenPppGroupDayCurrentOutPkts": adGenPppGroupDayCurrentOutPkts,
       "adGenPppGroupDayCurrentOutDiscards": adGenPppGroupDayCurrentOutDiscards,
       "adGenPppGroupDayCurrentOutErrors": adGenPppGroupDayCurrentOutErrors,
       "adGenPppGroupDayCurrentInL3Pkts": adGenPppGroupDayCurrentInL3Pkts,
       "adGenPppGroupDayCurrentOutL3Pkts": adGenPppGroupDayCurrentOutL3Pkts,
       "adGenPppGroupDayIntervalTable": adGenPppGroupDayIntervalTable,
       "adGenPppGroupDayIntervalEntry": adGenPppGroupDayIntervalEntry,
       "adGenPppGroupDayIntervalNumber": adGenPppGroupDayIntervalNumber,
       "adGenPppGroupDayIntervalInOctets": adGenPppGroupDayIntervalInOctets,
       "adGenPppGroupDayIntervalInPkts": adGenPppGroupDayIntervalInPkts,
       "adGenPppGroupDayIntervalInDiscards": adGenPppGroupDayIntervalInDiscards,
       "adGenPppGroupDayIntervalInErrors": adGenPppGroupDayIntervalInErrors,
       "adGenPppGroupDayIntervalOutOctets": adGenPppGroupDayIntervalOutOctets,
       "adGenPppGroupDayIntervalOutPkts": adGenPppGroupDayIntervalOutPkts,
       "adGenPppGroupDayIntervalOutDiscards": adGenPppGroupDayIntervalOutDiscards,
       "adGenPppGroupDayIntervalOutErrors": adGenPppGroupDayIntervalOutErrors,
       "adGenPppGroupDayIntervalTimeStamp": adGenPppGroupDayIntervalTimeStamp,
       "adGenPppGroupDayIntervalInL3Pkts": adGenPppGroupDayIntervalInL3Pkts,
       "adGenPppGroupDayIntervalOutL3Pkts": adGenPppGroupDayIntervalOutL3Pkts,
       "adGenPppAlarmsPrefix": adGenPppAlarmsPrefix,
       "adGenPppAlarms": adGenPppAlarms,
       "adGenPppLinkLcpDownAlarmClr": adGenPppLinkLcpDownAlarmClr,
       "adGenPppLinkLcpDownAlarmAct": adGenPppLinkLcpDownAlarmAct,
       "adGenPppGroupNcpDownAlarmClr": adGenPppGroupNcpDownAlarmClr,
       "adGenPppGroupNcpDownAlarmAct": adGenPppGroupNcpDownAlarmAct,
       "adGenPppGroupIpv6NcpDownAlarmClr": adGenPppGroupIpv6NcpDownAlarmClr,
       "adGenPppGroupIpv6NcpDownAlarmAct": adGenPppGroupIpv6NcpDownAlarmAct,
       "adGenPppGroupIpv6AddrMismatchAlarmClr": adGenPppGroupIpv6AddrMismatchAlarmClr,
       "adGenPppGroupIpv6AddrMismatchAlarmAct": adGenPppGroupIpv6AddrMismatchAlarmAct,
       "adGenPppGroupIpv6GatewayAddrMismatchAlarmClr": adGenPppGroupIpv6GatewayAddrMismatchAlarmClr,
       "adGenPppGroupIpv6GatewayAddrMismatchAlarmAct": adGenPppGroupIpv6GatewayAddrMismatchAlarmAct,
       "adGenPppMIB": adGenPppMIB}
)
