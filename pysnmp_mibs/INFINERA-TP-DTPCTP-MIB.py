# SNMP MIB module (INFINERA-TP-DTPCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-DTPCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:05 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnServiceType,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnServiceType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dtpCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7)
)
if mibBuilder.loadTexts:
    dtpCtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DtpCtpTable_Object = MibTable
dtpCtpTable = _DtpCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    dtpCtpTable.setStatus("current")
_DtpCtpEntry_Object = MibTableRow
dtpCtpEntry = _DtpCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1)
)
dtpCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dtpCtpEntry.setStatus("current")


class _DtpCtpCfgProtSt_Type(Integer32):
    """Custom type dtpCtpCfgProtSt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("wrk", 2),
          ("prot", 3),
          ("relb", 4),
          ("pU", 5))
    )


_DtpCtpCfgProtSt_Type.__name__ = "Integer32"
_DtpCtpCfgProtSt_Object = MibTableColumn
dtpCtpCfgProtSt = _DtpCtpCfgProtSt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 1),
    _DtpCtpCfgProtSt_Type()
)
dtpCtpCfgProtSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpCfgProtSt.setStatus("current")


class _DtpCtpProtMod_Type(Integer32):
    """Custom type dtpCtpProtMod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dtDSNCP", 2),
          ("stDSNCP", 3))
    )


_DtpCtpProtMod_Type.__name__ = "Integer32"
_DtpCtpProtMod_Object = MibTableColumn
dtpCtpProtMod = _DtpCtpProtMod_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 2),
    _DtpCtpProtMod_Type()
)
dtpCtpProtMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpProtMod.setStatus("current")


class _DtpCtpSwReason_Type(Integer32):
    """Custom type dtpCtpSwReason based on Integer32"""
    defaultValue = 6

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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("mSwP", 1),
          ("mSwW", 2),
          ("wLck", 3),
          ("pLck", 4),
          ("auto", 5),
          ("none", 6),
          ("revert", 7),
          ("admLck", 8),
          ("unProv", 9),
          ("eqFlt", 10),
          ("liFlt", 11),
          ("liSF", 12),
          ("clRxFlt", 13),
          ("clTxFlt", 14),
          ("sysLof", 15))
    )


_DtpCtpSwReason_Type.__name__ = "Integer32"
_DtpCtpSwReason_Object = MibTableColumn
dtpCtpSwReason = _DtpCtpSwReason_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 3),
    _DtpCtpSwReason_Type()
)
dtpCtpSwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpSwReason.setStatus("current")
_DtpCtpSupportingTP_Type = DisplayString
_DtpCtpSupportingTP_Object = MibTableColumn
dtpCtpSupportingTP = _DtpCtpSupportingTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 4),
    _DtpCtpSupportingTP_Type()
)
dtpCtpSupportingTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpSupportingTP.setStatus("current")
_DtpCtpExpectedPayload_Type = InfnServiceType
_DtpCtpExpectedPayload_Object = MibTableColumn
dtpCtpExpectedPayload = _DtpCtpExpectedPayload_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 5),
    _DtpCtpExpectedPayload_Type()
)
dtpCtpExpectedPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpExpectedPayload.setStatus("current")
_DtpCtpSupportingCircuitIdList_Type = DisplayString
_DtpCtpSupportingCircuitIdList_Object = MibTableColumn
dtpCtpSupportingCircuitIdList = _DtpCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 6),
    _DtpCtpSupportingCircuitIdList_Type()
)
dtpCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpSupportingCircuitIdList.setStatus("current")
_DtpCtpDetectedPayload_Type = InfnServiceType
_DtpCtpDetectedPayload_Object = MibTableColumn
dtpCtpDetectedPayload = _DtpCtpDetectedPayload_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 7),
    _DtpCtpDetectedPayload_Type()
)
dtpCtpDetectedPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpDetectedPayload.setStatus("current")


class _DtpCtpDataRate_Type(Integer32):
    """Custom type dtpCtpDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rateNotSet", 1),
          ("rate10GigAny", 2),
          ("rate2g500mAny", 3),
          ("rate1GogAny", 4),
          ("rate40GigAny", 5))
    )


_DtpCtpDataRate_Type.__name__ = "Integer32"
_DtpCtpDataRate_Object = MibTableColumn
dtpCtpDataRate = _DtpCtpDataRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 8),
    _DtpCtpDataRate_Type()
)
dtpCtpDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpDataRate.setStatus("current")


class _DtpCtpLoopback_Type(Integer32):
    """Custom type dtpCtpLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("terminal", 2),
          ("facility", 3))
    )


_DtpCtpLoopback_Type.__name__ = "Integer32"
_DtpCtpLoopback_Object = MibTableColumn
dtpCtpLoopback = _DtpCtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 9),
    _DtpCtpLoopback_Type()
)
dtpCtpLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpLoopback.setStatus("current")


class _DtpCtpInsertDtpTti_Type(TruthValue):
    """Custom type dtpCtpInsertDtpTti based on TruthValue"""
    defaultValue = 2


_DtpCtpInsertDtpTti_Type.__name__ = "TruthValue"
_DtpCtpInsertDtpTti_Object = MibTableColumn
dtpCtpInsertDtpTti = _DtpCtpInsertDtpTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 10),
    _DtpCtpInsertDtpTti_Type()
)
dtpCtpInsertDtpTti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpInsertDtpTti.setStatus("current")


class _DtpCtpTtiAlarmReporting_Type(Integer32):
    """Custom type dtpCtpTtiAlarmReporting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DtpCtpTtiAlarmReporting_Type.__name__ = "Integer32"
_DtpCtpTtiAlarmReporting_Object = MibTableColumn
dtpCtpTtiAlarmReporting = _DtpCtpTtiAlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 11),
    _DtpCtpTtiAlarmReporting_Type()
)
dtpCtpTtiAlarmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpTtiAlarmReporting.setStatus("current")


class _DtpCtpTxTtiAlarmReporting_Type(Integer32):
    """Custom type dtpCtpTxTtiAlarmReporting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DtpCtpTxTtiAlarmReporting_Type.__name__ = "Integer32"
_DtpCtpTxTtiAlarmReporting_Object = MibTableColumn
dtpCtpTxTtiAlarmReporting = _DtpCtpTxTtiAlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 12),
    _DtpCtpTxTtiAlarmReporting_Type()
)
dtpCtpTxTtiAlarmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpTxTtiAlarmReporting.setStatus("current")
_DtpCtpTxDtpTti_Type = DisplayString
_DtpCtpTxDtpTti_Object = MibTableColumn
dtpCtpTxDtpTti = _DtpCtpTxDtpTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 13),
    _DtpCtpTxDtpTti_Type()
)
dtpCtpTxDtpTti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpTxDtpTti.setStatus("current")
_DtpCtpRxDtpTtiWrite_Type = DisplayString
_DtpCtpRxDtpTtiWrite_Object = MibTableColumn
dtpCtpRxDtpTtiWrite = _DtpCtpRxDtpTtiWrite_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 14),
    _DtpCtpRxDtpTtiWrite_Type()
)
dtpCtpRxDtpTtiWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpRxDtpTtiWrite.setStatus("current")
_DtpCtpExpectedDtpTti_Type = DisplayString
_DtpCtpExpectedDtpTti_Object = MibTableColumn
dtpCtpExpectedDtpTti = _DtpCtpExpectedDtpTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 15),
    _DtpCtpExpectedDtpTti_Type()
)
dtpCtpExpectedDtpTti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpExpectedDtpTti.setStatus("current")
_DtpCtpExpectedTxDtpTti_Type = DisplayString
_DtpCtpExpectedTxDtpTti_Object = MibTableColumn
dtpCtpExpectedTxDtpTti = _DtpCtpExpectedTxDtpTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 16),
    _DtpCtpExpectedTxDtpTti_Type()
)
dtpCtpExpectedTxDtpTti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpExpectedTxDtpTti.setStatus("current")
_DtpCtpRxDtpTti_Type = DisplayString
_DtpCtpRxDtpTti_Object = MibTableColumn
dtpCtpRxDtpTti = _DtpCtpRxDtpTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 17),
    _DtpCtpRxDtpTti_Type()
)
dtpCtpRxDtpTti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpRxDtpTti.setStatus("current")
_DtpCtpRecvTxDtpTti_Type = DisplayString
_DtpCtpRecvTxDtpTti_Object = MibTableColumn
dtpCtpRecvTxDtpTti = _DtpCtpRecvTxDtpTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 18),
    _DtpCtpRecvTxDtpTti_Type()
)
dtpCtpRecvTxDtpTti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpRecvTxDtpTti.setStatus("current")
_DtpCtpDtpRxCv15MinutesTce_Type = Counter64
_DtpCtpDtpRxCv15MinutesTce_Object = MibTableColumn
dtpCtpDtpRxCv15MinutesTce = _DtpCtpDtpRxCv15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 19),
    _DtpCtpDtpRxCv15MinutesTce_Type()
)
dtpCtpDtpRxCv15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxCv15MinutesTce.setStatus("current")


class _DtpCtpDtpRxEs15MinutesTce_Type(Integer32):
    """Custom type dtpCtpDtpRxEs15MinutesTce based on Integer32"""
    defaultValue = 120


_DtpCtpDtpRxEs15MinutesTce_Type.__name__ = "Integer32"
_DtpCtpDtpRxEs15MinutesTce_Object = MibTableColumn
dtpCtpDtpRxEs15MinutesTce = _DtpCtpDtpRxEs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 20),
    _DtpCtpDtpRxEs15MinutesTce_Type()
)
dtpCtpDtpRxEs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxEs15MinutesTce.setStatus("current")


class _DtpCtpDtpRxSes15MinutesTce_Type(Integer32):
    """Custom type dtpCtpDtpRxSes15MinutesTce based on Integer32"""
    defaultValue = 3


_DtpCtpDtpRxSes15MinutesTce_Type.__name__ = "Integer32"
_DtpCtpDtpRxSes15MinutesTce_Object = MibTableColumn
dtpCtpDtpRxSes15MinutesTce = _DtpCtpDtpRxSes15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 21),
    _DtpCtpDtpRxSes15MinutesTce_Type()
)
dtpCtpDtpRxSes15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxSes15MinutesTce.setStatus("current")


class _DtpCtpDtpRxUas15MinutesTce_Type(Integer32):
    """Custom type dtpCtpDtpRxUas15MinutesTce based on Integer32"""
    defaultValue = 10


_DtpCtpDtpRxUas15MinutesTce_Type.__name__ = "Integer32"
_DtpCtpDtpRxUas15MinutesTce_Object = MibTableColumn
dtpCtpDtpRxUas15MinutesTce = _DtpCtpDtpRxUas15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 22),
    _DtpCtpDtpRxUas15MinutesTce_Type()
)
dtpCtpDtpRxUas15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxUas15MinutesTce.setStatus("current")
_DtpCtpDtpRxCvDayTce_Type = Counter64
_DtpCtpDtpRxCvDayTce_Object = MibTableColumn
dtpCtpDtpRxCvDayTce = _DtpCtpDtpRxCvDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 23),
    _DtpCtpDtpRxCvDayTce_Type()
)
dtpCtpDtpRxCvDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxCvDayTce.setStatus("current")


class _DtpCtpDtpRxEsDayTce_Type(Integer32):
    """Custom type dtpCtpDtpRxEsDayTce based on Integer32"""
    defaultValue = 1200


_DtpCtpDtpRxEsDayTce_Type.__name__ = "Integer32"
_DtpCtpDtpRxEsDayTce_Object = MibTableColumn
dtpCtpDtpRxEsDayTce = _DtpCtpDtpRxEsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 24),
    _DtpCtpDtpRxEsDayTce_Type()
)
dtpCtpDtpRxEsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxEsDayTce.setStatus("current")


class _DtpCtpDtpRxSesDayTce_Type(Integer32):
    """Custom type dtpCtpDtpRxSesDayTce based on Integer32"""
    defaultValue = 7


_DtpCtpDtpRxSesDayTce_Type.__name__ = "Integer32"
_DtpCtpDtpRxSesDayTce_Object = MibTableColumn
dtpCtpDtpRxSesDayTce = _DtpCtpDtpRxSesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 25),
    _DtpCtpDtpRxSesDayTce_Type()
)
dtpCtpDtpRxSesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxSesDayTce.setStatus("current")


class _DtpCtpDtpRxUasDayTce_Type(Integer32):
    """Custom type dtpCtpDtpRxUasDayTce based on Integer32"""
    defaultValue = 10


_DtpCtpDtpRxUasDayTce_Type.__name__ = "Integer32"
_DtpCtpDtpRxUasDayTce_Object = MibTableColumn
dtpCtpDtpRxUasDayTce = _DtpCtpDtpRxUasDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 26),
    _DtpCtpDtpRxUasDayTce_Type()
)
dtpCtpDtpRxUasDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxUasDayTce.setStatus("current")
_DtpCtpDtpTxCv15MinutesTce_Type = Counter64
_DtpCtpDtpTxCv15MinutesTce_Object = MibTableColumn
dtpCtpDtpTxCv15MinutesTce = _DtpCtpDtpTxCv15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 27),
    _DtpCtpDtpTxCv15MinutesTce_Type()
)
dtpCtpDtpTxCv15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxCv15MinutesTce.setStatus("current")


class _DtpCtpDtpTxEs15MinutesTce_Type(Integer32):
    """Custom type dtpCtpDtpTxEs15MinutesTce based on Integer32"""
    defaultValue = 120


_DtpCtpDtpTxEs15MinutesTce_Type.__name__ = "Integer32"
_DtpCtpDtpTxEs15MinutesTce_Object = MibTableColumn
dtpCtpDtpTxEs15MinutesTce = _DtpCtpDtpTxEs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 28),
    _DtpCtpDtpTxEs15MinutesTce_Type()
)
dtpCtpDtpTxEs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxEs15MinutesTce.setStatus("current")


class _DtpCtpDtpTxSes15MinutesTce_Type(Integer32):
    """Custom type dtpCtpDtpTxSes15MinutesTce based on Integer32"""
    defaultValue = 3


_DtpCtpDtpTxSes15MinutesTce_Type.__name__ = "Integer32"
_DtpCtpDtpTxSes15MinutesTce_Object = MibTableColumn
dtpCtpDtpTxSes15MinutesTce = _DtpCtpDtpTxSes15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 29),
    _DtpCtpDtpTxSes15MinutesTce_Type()
)
dtpCtpDtpTxSes15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxSes15MinutesTce.setStatus("current")


class _DtpCtpDtpTxUas15MinutesTce_Type(Integer32):
    """Custom type dtpCtpDtpTxUas15MinutesTce based on Integer32"""
    defaultValue = 10


_DtpCtpDtpTxUas15MinutesTce_Type.__name__ = "Integer32"
_DtpCtpDtpTxUas15MinutesTce_Object = MibTableColumn
dtpCtpDtpTxUas15MinutesTce = _DtpCtpDtpTxUas15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 30),
    _DtpCtpDtpTxUas15MinutesTce_Type()
)
dtpCtpDtpTxUas15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxUas15MinutesTce.setStatus("current")
_DtpCtpDtpTxCvDayTce_Type = Counter64
_DtpCtpDtpTxCvDayTce_Object = MibTableColumn
dtpCtpDtpTxCvDayTce = _DtpCtpDtpTxCvDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 31),
    _DtpCtpDtpTxCvDayTce_Type()
)
dtpCtpDtpTxCvDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxCvDayTce.setStatus("current")


class _DtpCtpDtpTxEsDayTce_Type(Integer32):
    """Custom type dtpCtpDtpTxEsDayTce based on Integer32"""
    defaultValue = 1200


_DtpCtpDtpTxEsDayTce_Type.__name__ = "Integer32"
_DtpCtpDtpTxEsDayTce_Object = MibTableColumn
dtpCtpDtpTxEsDayTce = _DtpCtpDtpTxEsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 32),
    _DtpCtpDtpTxEsDayTce_Type()
)
dtpCtpDtpTxEsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxEsDayTce.setStatus("current")


class _DtpCtpDtpTxSesDayTce_Type(Integer32):
    """Custom type dtpCtpDtpTxSesDayTce based on Integer32"""
    defaultValue = 7


_DtpCtpDtpTxSesDayTce_Type.__name__ = "Integer32"
_DtpCtpDtpTxSesDayTce_Object = MibTableColumn
dtpCtpDtpTxSesDayTce = _DtpCtpDtpTxSesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 33),
    _DtpCtpDtpTxSesDayTce_Type()
)
dtpCtpDtpTxSesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxSesDayTce.setStatus("current")


class _DtpCtpDtpTxUasDayTce_Type(Integer32):
    """Custom type dtpCtpDtpTxUasDayTce based on Integer32"""
    defaultValue = 10


_DtpCtpDtpTxUasDayTce_Type.__name__ = "Integer32"
_DtpCtpDtpTxUasDayTce_Object = MibTableColumn
dtpCtpDtpTxUasDayTce = _DtpCtpDtpTxUasDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 34),
    _DtpCtpDtpTxUasDayTce_Type()
)
dtpCtpDtpTxUasDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxUasDayTce.setStatus("current")


class _DtpCtpDtpRxCv15MinutesTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpRxCv15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpRxCv15MinutesTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpRxCv15MinutesTceReporting_Object = MibTableColumn
dtpCtpDtpRxCv15MinutesTceReporting = _DtpCtpDtpRxCv15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 35),
    _DtpCtpDtpRxCv15MinutesTceReporting_Type()
)
dtpCtpDtpRxCv15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxCv15MinutesTceReporting.setStatus("current")


class _DtpCtpDtpRxEs15MinutesTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpRxEs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpRxEs15MinutesTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpRxEs15MinutesTceReporting_Object = MibTableColumn
dtpCtpDtpRxEs15MinutesTceReporting = _DtpCtpDtpRxEs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 36),
    _DtpCtpDtpRxEs15MinutesTceReporting_Type()
)
dtpCtpDtpRxEs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxEs15MinutesTceReporting.setStatus("current")


class _DtpCtpDtpRxSes15MinutesTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpRxSes15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpRxSes15MinutesTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpRxSes15MinutesTceReporting_Object = MibTableColumn
dtpCtpDtpRxSes15MinutesTceReporting = _DtpCtpDtpRxSes15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 37),
    _DtpCtpDtpRxSes15MinutesTceReporting_Type()
)
dtpCtpDtpRxSes15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxSes15MinutesTceReporting.setStatus("current")


class _DtpCtpDtpRxUas15MinutesTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpRxUas15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpRxUas15MinutesTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpRxUas15MinutesTceReporting_Object = MibTableColumn
dtpCtpDtpRxUas15MinutesTceReporting = _DtpCtpDtpRxUas15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 38),
    _DtpCtpDtpRxUas15MinutesTceReporting_Type()
)
dtpCtpDtpRxUas15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxUas15MinutesTceReporting.setStatus("current")


class _DtpCtpDtpRxCvDayTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpRxCvDayTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpRxCvDayTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpRxCvDayTceReporting_Object = MibTableColumn
dtpCtpDtpRxCvDayTceReporting = _DtpCtpDtpRxCvDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 39),
    _DtpCtpDtpRxCvDayTceReporting_Type()
)
dtpCtpDtpRxCvDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxCvDayTceReporting.setStatus("current")


class _DtpCtpDtpRxEsDayTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpRxEsDayTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpRxEsDayTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpRxEsDayTceReporting_Object = MibTableColumn
dtpCtpDtpRxEsDayTceReporting = _DtpCtpDtpRxEsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 40),
    _DtpCtpDtpRxEsDayTceReporting_Type()
)
dtpCtpDtpRxEsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxEsDayTceReporting.setStatus("current")


class _DtpCtpDtpRxSesDayTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpRxSesDayTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpRxSesDayTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpRxSesDayTceReporting_Object = MibTableColumn
dtpCtpDtpRxSesDayTceReporting = _DtpCtpDtpRxSesDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 41),
    _DtpCtpDtpRxSesDayTceReporting_Type()
)
dtpCtpDtpRxSesDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxSesDayTceReporting.setStatus("current")


class _DtpCtpDtpRxUasDayTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpRxUasDayTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpRxUasDayTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpRxUasDayTceReporting_Object = MibTableColumn
dtpCtpDtpRxUasDayTceReporting = _DtpCtpDtpRxUasDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 42),
    _DtpCtpDtpRxUasDayTceReporting_Type()
)
dtpCtpDtpRxUasDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpRxUasDayTceReporting.setStatus("current")


class _DtpCtpDtpTxCv15MinutesTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpTxCv15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpTxCv15MinutesTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpTxCv15MinutesTceReporting_Object = MibTableColumn
dtpCtpDtpTxCv15MinutesTceReporting = _DtpCtpDtpTxCv15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 43),
    _DtpCtpDtpTxCv15MinutesTceReporting_Type()
)
dtpCtpDtpTxCv15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxCv15MinutesTceReporting.setStatus("current")


class _DtpCtpDtpTxEs15MinutesTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpTxEs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpTxEs15MinutesTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpTxEs15MinutesTceReporting_Object = MibTableColumn
dtpCtpDtpTxEs15MinutesTceReporting = _DtpCtpDtpTxEs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 44),
    _DtpCtpDtpTxEs15MinutesTceReporting_Type()
)
dtpCtpDtpTxEs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxEs15MinutesTceReporting.setStatus("current")


class _DtpCtpDtpTxSes15MinutesTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpTxSes15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpTxSes15MinutesTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpTxSes15MinutesTceReporting_Object = MibTableColumn
dtpCtpDtpTxSes15MinutesTceReporting = _DtpCtpDtpTxSes15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 45),
    _DtpCtpDtpTxSes15MinutesTceReporting_Type()
)
dtpCtpDtpTxSes15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxSes15MinutesTceReporting.setStatus("current")


class _DtpCtpDtpTxUas15MinutesTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpTxUas15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpTxUas15MinutesTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpTxUas15MinutesTceReporting_Object = MibTableColumn
dtpCtpDtpTxUas15MinutesTceReporting = _DtpCtpDtpTxUas15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 46),
    _DtpCtpDtpTxUas15MinutesTceReporting_Type()
)
dtpCtpDtpTxUas15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxUas15MinutesTceReporting.setStatus("current")


class _DtpCtpDtpTxCvDayTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpTxCvDayTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpTxCvDayTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpTxCvDayTceReporting_Object = MibTableColumn
dtpCtpDtpTxCvDayTceReporting = _DtpCtpDtpTxCvDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 47),
    _DtpCtpDtpTxCvDayTceReporting_Type()
)
dtpCtpDtpTxCvDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxCvDayTceReporting.setStatus("current")


class _DtpCtpDtpTxEsDayTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpTxEsDayTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpTxEsDayTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpTxEsDayTceReporting_Object = MibTableColumn
dtpCtpDtpTxEsDayTceReporting = _DtpCtpDtpTxEsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 48),
    _DtpCtpDtpTxEsDayTceReporting_Type()
)
dtpCtpDtpTxEsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxEsDayTceReporting.setStatus("current")


class _DtpCtpDtpTxSesDayTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpTxSesDayTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpTxSesDayTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpTxSesDayTceReporting_Object = MibTableColumn
dtpCtpDtpTxSesDayTceReporting = _DtpCtpDtpTxSesDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 49),
    _DtpCtpDtpTxSesDayTceReporting_Type()
)
dtpCtpDtpTxSesDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxSesDayTceReporting.setStatus("current")


class _DtpCtpDtpTxUasDayTceReporting_Type(TruthValue):
    """Custom type dtpCtpDtpTxUasDayTceReporting based on TruthValue"""
    defaultValue = 2


_DtpCtpDtpTxUasDayTceReporting_Type.__name__ = "TruthValue"
_DtpCtpDtpTxUasDayTceReporting_Object = MibTableColumn
dtpCtpDtpTxUasDayTceReporting = _DtpCtpDtpTxUasDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 50),
    _DtpCtpDtpTxUasDayTceReporting_Type()
)
dtpCtpDtpTxUasDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpDtpTxUasDayTceReporting.setStatus("current")


class _DtpCtpPrbsGenerationMode_Type(Integer32):
    """Custom type dtpCtpPrbsGenerationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DtpCtpPrbsGenerationMode_Type.__name__ = "Integer32"
_DtpCtpPrbsGenerationMode_Object = MibTableColumn
dtpCtpPrbsGenerationMode = _DtpCtpPrbsGenerationMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 51),
    _DtpCtpPrbsGenerationMode_Type()
)
dtpCtpPrbsGenerationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpPrbsGenerationMode.setStatus("current")


class _DtpCtpPrbsMonitoringMode_Type(Integer32):
    """Custom type dtpCtpPrbsMonitoringMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DtpCtpPrbsMonitoringMode_Type.__name__ = "Integer32"
_DtpCtpPrbsMonitoringMode_Object = MibTableColumn
dtpCtpPrbsMonitoringMode = _DtpCtpPrbsMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 52),
    _DtpCtpPrbsMonitoringMode_Type()
)
dtpCtpPrbsMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpPrbsMonitoringMode.setStatus("current")


class _DtpCtpNumDtpSubCh_Type(Integer32):
    """Custom type dtpCtpNumDtpSubCh based on Integer32"""
    defaultValue = 0


_DtpCtpNumDtpSubCh_Type.__name__ = "Integer32"
_DtpCtpNumDtpSubCh_Object = MibTableColumn
dtpCtpNumDtpSubCh = _DtpCtpNumDtpSubCh_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 53),
    _DtpCtpNumDtpSubCh_Type()
)
dtpCtpNumDtpSubCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpNumDtpSubCh.setStatus("current")


class _DtpCtpMuxMode_Type(TruthValue):
    """Custom type dtpCtpMuxMode based on TruthValue"""
    defaultValue = 2


_DtpCtpMuxMode_Type.__name__ = "TruthValue"
_DtpCtpMuxMode_Object = MibTableColumn
dtpCtpMuxMode = _DtpCtpMuxMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 54),
    _DtpCtpMuxMode_Type()
)
dtpCtpMuxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpMuxMode.setStatus("current")


class _DtpCtpPmHistStatsEnable_Type(Integer32):
    """Custom type dtpCtpPmHistStatsEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_DtpCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_DtpCtpPmHistStatsEnable_Object = MibTableColumn
dtpCtpPmHistStatsEnable = _DtpCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 55),
    _DtpCtpPmHistStatsEnable_Type()
)
dtpCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtpCtpPmHistStatsEnable.setStatus("current")


class _DtpCtpCrossConnectType_Type(Integer32):
    """Custom type dtpCtpCrossConnectType based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unidirectionFrom", 2),
          ("unidirectionTo", 3),
          ("unidirectionToAndFrom", 4),
          ("bidirection", 5),
          ("bidirectionUnidirectionFrom", 6),
          ("bidirectionUnidirectionTo", 7),
          ("bidirectionUnidirectionToAndFrom", 8))
    )


_DtpCtpCrossConnectType_Type.__name__ = "Integer32"
_DtpCtpCrossConnectType_Object = MibTableColumn
dtpCtpCrossConnectType = _DtpCtpCrossConnectType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 1, 1, 56),
    _DtpCtpCrossConnectType_Type()
)
dtpCtpCrossConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dtpCtpCrossConnectType.setStatus("current")
_DtpCtpConformance_ObjectIdentity = ObjectIdentity
dtpCtpConformance = _DtpCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 3)
)
_DtpCtpCompliances_ObjectIdentity = ObjectIdentity
dtpCtpCompliances = _DtpCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 3, 1)
)
_DtpCtpGroups_ObjectIdentity = ObjectIdentity
dtpCtpGroups = _DtpCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 3, 2)
)

# Managed Objects groups

dtpCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 3, 2, 1)
)
dtpCtpGroup.setObjects(
      *(("INFINERA-TP-DTPCTP-MIB", "dtpCtpCfgProtSt"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpProtMod"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpSwReason"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpSupportingTP"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpExpectedPayload"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpSupportingCircuitIdList"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDetectedPayload"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDataRate"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpLoopback"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpInsertDtpTti"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpTtiAlarmReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpTxTtiAlarmReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpTxDtpTti"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpRxDtpTtiWrite"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpExpectedDtpTti"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpExpectedTxDtpTti"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpRxDtpTti"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpRecvTxDtpTti"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxCv15MinutesTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxEs15MinutesTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxSes15MinutesTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxUas15MinutesTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxCvDayTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxEsDayTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxSesDayTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxUasDayTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxCv15MinutesTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxEs15MinutesTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxSes15MinutesTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxUas15MinutesTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxCvDayTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxEsDayTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxSesDayTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxUasDayTce"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxCv15MinutesTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxEs15MinutesTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxSes15MinutesTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxUas15MinutesTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxCvDayTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxEsDayTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxSesDayTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpRxUasDayTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxCv15MinutesTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxEs15MinutesTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxSes15MinutesTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxUas15MinutesTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxCvDayTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxEsDayTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxSesDayTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpDtpTxUasDayTceReporting"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpPrbsGenerationMode"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpPrbsMonitoringMode"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpNumDtpSubCh"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpMuxMode"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpPmHistStatsEnable"),
        ("INFINERA-TP-DTPCTP-MIB", "dtpCtpCrossConnectType"))
)
if mibBuilder.loadTexts:
    dtpCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dtpCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 7, 3, 1, 1)
)
dtpCtpCompliance.setObjects(
    ("INFINERA-TP-DTPCTP-MIB", "dtpCtpGroup")
)
if mibBuilder.loadTexts:
    dtpCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-DTPCTP-MIB",
    **{"dtpCtpMIB": dtpCtpMIB,
       "dtpCtpTable": dtpCtpTable,
       "dtpCtpEntry": dtpCtpEntry,
       "dtpCtpCfgProtSt": dtpCtpCfgProtSt,
       "dtpCtpProtMod": dtpCtpProtMod,
       "dtpCtpSwReason": dtpCtpSwReason,
       "dtpCtpSupportingTP": dtpCtpSupportingTP,
       "dtpCtpExpectedPayload": dtpCtpExpectedPayload,
       "dtpCtpSupportingCircuitIdList": dtpCtpSupportingCircuitIdList,
       "dtpCtpDetectedPayload": dtpCtpDetectedPayload,
       "dtpCtpDataRate": dtpCtpDataRate,
       "dtpCtpLoopback": dtpCtpLoopback,
       "dtpCtpInsertDtpTti": dtpCtpInsertDtpTti,
       "dtpCtpTtiAlarmReporting": dtpCtpTtiAlarmReporting,
       "dtpCtpTxTtiAlarmReporting": dtpCtpTxTtiAlarmReporting,
       "dtpCtpTxDtpTti": dtpCtpTxDtpTti,
       "dtpCtpRxDtpTtiWrite": dtpCtpRxDtpTtiWrite,
       "dtpCtpExpectedDtpTti": dtpCtpExpectedDtpTti,
       "dtpCtpExpectedTxDtpTti": dtpCtpExpectedTxDtpTti,
       "dtpCtpRxDtpTti": dtpCtpRxDtpTti,
       "dtpCtpRecvTxDtpTti": dtpCtpRecvTxDtpTti,
       "dtpCtpDtpRxCv15MinutesTce": dtpCtpDtpRxCv15MinutesTce,
       "dtpCtpDtpRxEs15MinutesTce": dtpCtpDtpRxEs15MinutesTce,
       "dtpCtpDtpRxSes15MinutesTce": dtpCtpDtpRxSes15MinutesTce,
       "dtpCtpDtpRxUas15MinutesTce": dtpCtpDtpRxUas15MinutesTce,
       "dtpCtpDtpRxCvDayTce": dtpCtpDtpRxCvDayTce,
       "dtpCtpDtpRxEsDayTce": dtpCtpDtpRxEsDayTce,
       "dtpCtpDtpRxSesDayTce": dtpCtpDtpRxSesDayTce,
       "dtpCtpDtpRxUasDayTce": dtpCtpDtpRxUasDayTce,
       "dtpCtpDtpTxCv15MinutesTce": dtpCtpDtpTxCv15MinutesTce,
       "dtpCtpDtpTxEs15MinutesTce": dtpCtpDtpTxEs15MinutesTce,
       "dtpCtpDtpTxSes15MinutesTce": dtpCtpDtpTxSes15MinutesTce,
       "dtpCtpDtpTxUas15MinutesTce": dtpCtpDtpTxUas15MinutesTce,
       "dtpCtpDtpTxCvDayTce": dtpCtpDtpTxCvDayTce,
       "dtpCtpDtpTxEsDayTce": dtpCtpDtpTxEsDayTce,
       "dtpCtpDtpTxSesDayTce": dtpCtpDtpTxSesDayTce,
       "dtpCtpDtpTxUasDayTce": dtpCtpDtpTxUasDayTce,
       "dtpCtpDtpRxCv15MinutesTceReporting": dtpCtpDtpRxCv15MinutesTceReporting,
       "dtpCtpDtpRxEs15MinutesTceReporting": dtpCtpDtpRxEs15MinutesTceReporting,
       "dtpCtpDtpRxSes15MinutesTceReporting": dtpCtpDtpRxSes15MinutesTceReporting,
       "dtpCtpDtpRxUas15MinutesTceReporting": dtpCtpDtpRxUas15MinutesTceReporting,
       "dtpCtpDtpRxCvDayTceReporting": dtpCtpDtpRxCvDayTceReporting,
       "dtpCtpDtpRxEsDayTceReporting": dtpCtpDtpRxEsDayTceReporting,
       "dtpCtpDtpRxSesDayTceReporting": dtpCtpDtpRxSesDayTceReporting,
       "dtpCtpDtpRxUasDayTceReporting": dtpCtpDtpRxUasDayTceReporting,
       "dtpCtpDtpTxCv15MinutesTceReporting": dtpCtpDtpTxCv15MinutesTceReporting,
       "dtpCtpDtpTxEs15MinutesTceReporting": dtpCtpDtpTxEs15MinutesTceReporting,
       "dtpCtpDtpTxSes15MinutesTceReporting": dtpCtpDtpTxSes15MinutesTceReporting,
       "dtpCtpDtpTxUas15MinutesTceReporting": dtpCtpDtpTxUas15MinutesTceReporting,
       "dtpCtpDtpTxCvDayTceReporting": dtpCtpDtpTxCvDayTceReporting,
       "dtpCtpDtpTxEsDayTceReporting": dtpCtpDtpTxEsDayTceReporting,
       "dtpCtpDtpTxSesDayTceReporting": dtpCtpDtpTxSesDayTceReporting,
       "dtpCtpDtpTxUasDayTceReporting": dtpCtpDtpTxUasDayTceReporting,
       "dtpCtpPrbsGenerationMode": dtpCtpPrbsGenerationMode,
       "dtpCtpPrbsMonitoringMode": dtpCtpPrbsMonitoringMode,
       "dtpCtpNumDtpSubCh": dtpCtpNumDtpSubCh,
       "dtpCtpMuxMode": dtpCtpMuxMode,
       "dtpCtpPmHistStatsEnable": dtpCtpPmHistStatsEnable,
       "dtpCtpCrossConnectType": dtpCtpCrossConnectType,
       "dtpCtpConformance": dtpCtpConformance,
       "dtpCtpCompliances": dtpCtpCompliances,
       "dtpCtpCompliance": dtpCtpCompliance,
       "dtpCtpGroups": dtpCtpGroups,
       "dtpCtpGroup": dtpCtpGroup}
)
