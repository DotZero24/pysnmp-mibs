# SNMP MIB module (DC-OAM-LSP-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DC-OAM-LSP-PING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:34 2025
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

(NumericIndex,) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "NumericIndex")

(mplsMpEntry,
 mplsMpIndex) = mibBuilder.importSymbols(
    "DC-OAM-MPLS-MP-MIB",
    "mplsMpEntry",
    "mplsMpIndex")

(oammEntApplIndex,) = mibBuilder.importSymbols(
    "DC-OAMM-MIB",
    "oammEntApplIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel")

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
 enterprises,
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
    "enterprises",
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

lspPingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 12)
)
if mibBuilder.loadTexts:
    lspPingMib.setRevisions(
        ("2014-12-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_Opx_ObjectIdentity = ObjectIdentity
opx = _Opx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10)
)
_LsppObjects_ObjectIdentity = ObjectIdentity
lsppObjects = _LsppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1)
)
_MplsCvTrMpTable_Object = MibTable
mplsCvTrMpTable = _MplsCvTrMpTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1)
)
if mibBuilder.loadTexts:
    mplsCvTrMpTable.setStatus("current")
_MplsCvTrMpEntry_Object = MibTableRow
mplsCvTrMpEntry = _MplsCvTrMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1)
)
mplsCvTrMpEntry.setIndexNames(
    (0, "DC-OAMM-MIB", "oammEntApplIndex"),
    (0, "DC-OAM-LSP-PING-MIB", "mplsCvTrMpIndex"),
)
if mibBuilder.loadTexts:
    mplsCvTrMpEntry.setStatus("current")
_MplsCvTrMpIndex_Type = NumericIndex
_MplsCvTrMpIndex_Object = MibTableColumn
mplsCvTrMpIndex = _MplsCvTrMpIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 1),
    _MplsCvTrMpIndex_Type()
)
mplsCvTrMpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsCvTrMpIndex.setStatus("current")
_MplsCvTrMpRowStatus_Type = RowStatus
_MplsCvTrMpRowStatus_Object = MibTableColumn
mplsCvTrMpRowStatus = _MplsCvTrMpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 2),
    _MplsCvTrMpRowStatus_Type()
)
mplsCvTrMpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsCvTrMpRowStatus.setStatus("current")


class _MplsCvTrMpPhb_Type(Integer32):
    """Custom type mplsCvTrMpPhb based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsCvTrMpPhb_Type.__name__ = "Integer32"
_MplsCvTrMpPhb_Object = MibTableColumn
mplsCvTrMpPhb = _MplsCvTrMpPhb_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 3),
    _MplsCvTrMpPhb_Type()
)
mplsCvTrMpPhb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsCvTrMpPhb.setStatus("current")


class _MplsCvTrMpCvStatus_Type(TruthValue):
    """Custom type mplsCvTrMpCvStatus based on TruthValue"""
    defaultValue = 2


_MplsCvTrMpCvStatus_Type.__name__ = "TruthValue"
_MplsCvTrMpCvStatus_Object = MibTableColumn
mplsCvTrMpCvStatus = _MplsCvTrMpCvStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 4),
    _MplsCvTrMpCvStatus_Type()
)
mplsCvTrMpCvStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsCvTrMpCvStatus.setStatus("current")


class _MplsCvTrMpCvMessages_Type(Unsigned32):
    """Custom type mplsCvTrMpCvMessages based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MplsCvTrMpCvMessages_Type.__name__ = "Unsigned32"
_MplsCvTrMpCvMessages_Object = MibTableColumn
mplsCvTrMpCvMessages = _MplsCvTrMpCvMessages_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 5),
    _MplsCvTrMpCvMessages_Type()
)
mplsCvTrMpCvMessages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsCvTrMpCvMessages.setStatus("current")


class _MplsCvTrMpCvInterval_Type(Unsigned32):
    """Custom type mplsCvTrMpCvInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_MplsCvTrMpCvInterval_Type.__name__ = "Unsigned32"
_MplsCvTrMpCvInterval_Object = MibTableColumn
mplsCvTrMpCvInterval = _MplsCvTrMpCvInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 6),
    _MplsCvTrMpCvInterval_Type()
)
mplsCvTrMpCvInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsCvTrMpCvInterval.setStatus("current")
if mibBuilder.loadTexts:
    mplsCvTrMpCvInterval.setUnits("milliseconds")


class _MplsCvTrMpCvVerifyReverse_Type(TruthValue):
    """Custom type mplsCvTrMpCvVerifyReverse based on TruthValue"""
    defaultValue = 2


_MplsCvTrMpCvVerifyReverse_Type.__name__ = "TruthValue"
_MplsCvTrMpCvVerifyReverse_Object = MibTableColumn
mplsCvTrMpCvVerifyReverse = _MplsCvTrMpCvVerifyReverse_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 7),
    _MplsCvTrMpCvVerifyReverse_Type()
)
mplsCvTrMpCvVerifyReverse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsCvTrMpCvVerifyReverse.setStatus("current")


class _MplsCvTrMpCvTtl_Type(Unsigned32):
    """Custom type mplsCvTrMpCvTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MplsCvTrMpCvTtl_Type.__name__ = "Unsigned32"
_MplsCvTrMpCvTtl_Object = MibTableColumn
mplsCvTrMpCvTtl = _MplsCvTrMpCvTtl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 8),
    _MplsCvTrMpCvTtl_Type()
)
mplsCvTrMpCvTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsCvTrMpCvTtl.setStatus("current")


class _MplsCvTrMpCvReturnCode_Type(Integer32):
    """Custom type mplsCvTrMpCvReturnCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              256,
              257,
              258,
              259,
              260)
        )
    )
    namedValues = NamedValues(
        *(("noRC", 0),
          ("badRequestSent", 1),
          ("unrecognizedTlv", 2),
          ("egress", 3),
          ("noMapping", 4),
          ("mappingMismatch", 5),
          ("interfaceUnknown", 6),
          ("labelSwitch", 8),
          ("noForwarding", 9),
          ("wrongLabel", 10),
          ("noLabel", 11),
          ("unknownFec", 12),
          ("singleLabel", 13),
          ("timeout", 256),
          ("requestNotSent", 257),
          ("resourceFailure", 258),
          ("badReplyReceived", 259),
          ("ttlLimitReached", 260))
    )


_MplsCvTrMpCvReturnCode_Type.__name__ = "Integer32"
_MplsCvTrMpCvReturnCode_Object = MibTableColumn
mplsCvTrMpCvReturnCode = _MplsCvTrMpCvReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 9),
    _MplsCvTrMpCvReturnCode_Type()
)
mplsCvTrMpCvReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrMpCvReturnCode.setStatus("current")


class _MplsCvTrMpCvRvsReturnCode_Type(Integer32):
    """Custom type mplsCvTrMpCvRvsReturnCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              256,
              257,
              258,
              259,
              260)
        )
    )
    namedValues = NamedValues(
        *(("noRC", 0),
          ("badRequestSent", 1),
          ("unrecognizedTlv", 2),
          ("egress", 3),
          ("noMapping", 4),
          ("mappingMismatch", 5),
          ("interfaceUnknown", 6),
          ("labelSwitch", 8),
          ("noForwarding", 9),
          ("wrongLabel", 10),
          ("noLabel", 11),
          ("unknownFec", 12),
          ("singleLabel", 13),
          ("timeout", 256),
          ("requestNotSent", 257),
          ("resourceFailure", 258),
          ("badReplyReceived", 259),
          ("ttlLimitReached", 260))
    )


_MplsCvTrMpCvRvsReturnCode_Type.__name__ = "Integer32"
_MplsCvTrMpCvRvsReturnCode_Object = MibTableColumn
mplsCvTrMpCvRvsReturnCode = _MplsCvTrMpCvRvsReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 10),
    _MplsCvTrMpCvRvsReturnCode_Type()
)
mplsCvTrMpCvRvsReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrMpCvRvsReturnCode.setStatus("current")


class _MplsCvTrMpCvRepliesRcvd_Type(Counter32):
    """Custom type mplsCvTrMpCvRepliesRcvd based on Counter32"""
    defaultValue = 0


_MplsCvTrMpCvRepliesRcvd_Type.__name__ = "Counter32"
_MplsCvTrMpCvRepliesRcvd_Object = MibTableColumn
mplsCvTrMpCvRepliesRcvd = _MplsCvTrMpCvRepliesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 11),
    _MplsCvTrMpCvRepliesRcvd_Type()
)
mplsCvTrMpCvRepliesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrMpCvRepliesRcvd.setStatus("current")


class _MplsCvTrMpCvRoundTripMin_Type(Unsigned32):
    """Custom type mplsCvTrMpCvRoundTripMin based on Unsigned32"""
    defaultValue = 0


_MplsCvTrMpCvRoundTripMin_Type.__name__ = "Unsigned32"
_MplsCvTrMpCvRoundTripMin_Object = MibTableColumn
mplsCvTrMpCvRoundTripMin = _MplsCvTrMpCvRoundTripMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 12),
    _MplsCvTrMpCvRoundTripMin_Type()
)
mplsCvTrMpCvRoundTripMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrMpCvRoundTripMin.setStatus("current")
if mibBuilder.loadTexts:
    mplsCvTrMpCvRoundTripMin.setUnits("milliseconds")


class _MplsCvTrMpCvRoundTripAve_Type(Unsigned32):
    """Custom type mplsCvTrMpCvRoundTripAve based on Unsigned32"""
    defaultValue = 0


_MplsCvTrMpCvRoundTripAve_Type.__name__ = "Unsigned32"
_MplsCvTrMpCvRoundTripAve_Object = MibTableColumn
mplsCvTrMpCvRoundTripAve = _MplsCvTrMpCvRoundTripAve_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 13),
    _MplsCvTrMpCvRoundTripAve_Type()
)
mplsCvTrMpCvRoundTripAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrMpCvRoundTripAve.setStatus("current")
if mibBuilder.loadTexts:
    mplsCvTrMpCvRoundTripAve.setUnits("milliseconds")


class _MplsCvTrMpCvRoundTripMax_Type(Unsigned32):
    """Custom type mplsCvTrMpCvRoundTripMax based on Unsigned32"""
    defaultValue = 0


_MplsCvTrMpCvRoundTripMax_Type.__name__ = "Unsigned32"
_MplsCvTrMpCvRoundTripMax_Object = MibTableColumn
mplsCvTrMpCvRoundTripMax = _MplsCvTrMpCvRoundTripMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 14),
    _MplsCvTrMpCvRoundTripMax_Type()
)
mplsCvTrMpCvRoundTripMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrMpCvRoundTripMax.setStatus("current")
if mibBuilder.loadTexts:
    mplsCvTrMpCvRoundTripMax.setUnits("milliseconds")


class _MplsCvTrMpTrStatus_Type(TruthValue):
    """Custom type mplsCvTrMpTrStatus based on TruthValue"""
    defaultValue = 2


_MplsCvTrMpTrStatus_Type.__name__ = "TruthValue"
_MplsCvTrMpTrStatus_Object = MibTableColumn
mplsCvTrMpTrStatus = _MplsCvTrMpTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 15),
    _MplsCvTrMpTrStatus_Type()
)
mplsCvTrMpTrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsCvTrMpTrStatus.setStatus("current")


class _MplsCvTrMpTimeout_Type(Unsigned32):
    """Custom type mplsCvTrMpTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_MplsCvTrMpTimeout_Type.__name__ = "Unsigned32"
_MplsCvTrMpTimeout_Object = MibTableColumn
mplsCvTrMpTimeout = _MplsCvTrMpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 16),
    _MplsCvTrMpTimeout_Type()
)
mplsCvTrMpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsCvTrMpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    mplsCvTrMpTimeout.setUnits("milliseconds")


class _MplsCvTrMpTrReturnCode_Type(Integer32):
    """Custom type mplsCvTrMpTrReturnCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              256,
              257,
              258,
              259,
              260)
        )
    )
    namedValues = NamedValues(
        *(("noRC", 0),
          ("badRequestSent", 1),
          ("unrecognizedTlv", 2),
          ("egress", 3),
          ("noMapping", 4),
          ("mappingMismatch", 5),
          ("interfaceUnknown", 6),
          ("labelSwitch", 8),
          ("noForwarding", 9),
          ("wrongLabel", 10),
          ("noLabel", 11),
          ("unknownFec", 12),
          ("singleLabel", 13),
          ("timeout", 256),
          ("requestNotSent", 257),
          ("resourceFailure", 258),
          ("badReplyReceived", 259),
          ("ttlLimitReached", 260))
    )


_MplsCvTrMpTrReturnCode_Type.__name__ = "Integer32"
_MplsCvTrMpTrReturnCode_Object = MibTableColumn
mplsCvTrMpTrReturnCode = _MplsCvTrMpTrReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 1, 1, 17),
    _MplsCvTrMpTrReturnCode_Type()
)
mplsCvTrMpTrReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrMpTrReturnCode.setStatus("current")
_MplsTrHopMpTable_Object = MibTable
mplsTrHopMpTable = _MplsTrHopMpTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2)
)
if mibBuilder.loadTexts:
    mplsTrHopMpTable.setStatus("current")
_MplsTrHopMpEntry_Object = MibTableRow
mplsTrHopMpEntry = _MplsTrHopMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1)
)
mplsTrHopMpEntry.setIndexNames(
    (0, "DC-OAMM-MIB", "oammEntApplIndex"),
    (0, "DC-OAM-LSP-PING-MIB", "mplsCvTrMpIndex"),
    (0, "DC-OAM-LSP-PING-MIB", "mplsTrHopNumber"),
)
if mibBuilder.loadTexts:
    mplsTrHopMpEntry.setStatus("current")
_MplsTrHopNumber_Type = Unsigned32
_MplsTrHopNumber_Object = MibTableColumn
mplsTrHopNumber = _MplsTrHopNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 1),
    _MplsTrHopNumber_Type()
)
mplsTrHopNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTrHopNumber.setStatus("current")


class _MplsTrHopMpReturnCode_Type(Integer32):
    """Custom type mplsTrHopMpReturnCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              256,
              257,
              258,
              259,
              260)
        )
    )
    namedValues = NamedValues(
        *(("noRC", 0),
          ("badRequestSent", 1),
          ("unrecognizedTlv", 2),
          ("egress", 3),
          ("noMapping", 4),
          ("mappingMismatch", 5),
          ("interfaceUnknown", 6),
          ("labelSwitch", 8),
          ("noForwarding", 9),
          ("wrongLabel", 10),
          ("noLabel", 11),
          ("unknownFec", 12),
          ("singleLabel", 13),
          ("timeout", 256),
          ("requestNotSent", 257),
          ("resourceFailure", 258),
          ("badReplyReceived", 259),
          ("ttlLimitReached", 260))
    )


_MplsTrHopMpReturnCode_Type.__name__ = "Integer32"
_MplsTrHopMpReturnCode_Object = MibTableColumn
mplsTrHopMpReturnCode = _MplsTrHopMpReturnCode_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 2),
    _MplsTrHopMpReturnCode_Type()
)
mplsTrHopMpReturnCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrHopMpReturnCode.setStatus("current")
_MplsTrHopMpNextHopAddressType_Type = InetAddressType
_MplsTrHopMpNextHopAddressType_Object = MibTableColumn
mplsTrHopMpNextHopAddressType = _MplsTrHopMpNextHopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 3),
    _MplsTrHopMpNextHopAddressType_Type()
)
mplsTrHopMpNextHopAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrHopMpNextHopAddressType.setStatus("current")
_MplsTrHopMpNextHopAddress_Type = InetAddress
_MplsTrHopMpNextHopAddress_Object = MibTableColumn
mplsTrHopMpNextHopAddress = _MplsTrHopMpNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 4),
    _MplsTrHopMpNextHopAddress_Type()
)
mplsTrHopMpNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrHopMpNextHopAddress.setStatus("current")
_MplsTrHopMpLabel_Type = MplsLabel
_MplsTrHopMpLabel_Object = MibTableColumn
mplsTrHopMpLabel = _MplsTrHopMpLabel_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 5),
    _MplsTrHopMpLabel_Type()
)
mplsTrHopMpLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrHopMpLabel.setStatus("current")
_MplsTrHopMpRoundTrip_Type = Unsigned32
_MplsTrHopMpRoundTrip_Object = MibTableColumn
mplsTrHopMpRoundTrip = _MplsTrHopMpRoundTrip_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 6),
    _MplsTrHopMpRoundTrip_Type()
)
mplsTrHopMpRoundTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrHopMpRoundTrip.setStatus("current")
if mibBuilder.loadTexts:
    mplsTrHopMpRoundTrip.setUnits("milliseconds")


class _MplsTrHopMpMtu_Type(Unsigned32):
    """Custom type mplsTrHopMpMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsTrHopMpMtu_Type.__name__ = "Unsigned32"
_MplsTrHopMpMtu_Object = MibTableColumn
mplsTrHopMpMtu = _MplsTrHopMpMtu_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 7),
    _MplsTrHopMpMtu_Type()
)
mplsTrHopMpMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrHopMpMtu.setStatus("current")
_MplsTrHopMpDownstreamIfAddrType_Type = InetAddressType
_MplsTrHopMpDownstreamIfAddrType_Object = MibTableColumn
mplsTrHopMpDownstreamIfAddrType = _MplsTrHopMpDownstreamIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 100),
    _MplsTrHopMpDownstreamIfAddrType_Type()
)
mplsTrHopMpDownstreamIfAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrHopMpDownstreamIfAddrType.setStatus("current")
_MplsTrHopMpDownstreamIfAddr_Type = InetAddress
_MplsTrHopMpDownstreamIfAddr_Object = MibTableColumn
mplsTrHopMpDownstreamIfAddr = _MplsTrHopMpDownstreamIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 101),
    _MplsTrHopMpDownstreamIfAddr_Type()
)
mplsTrHopMpDownstreamIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrHopMpDownstreamIfAddr.setStatus("current")
_MplsTrHopMpDownstreamIfIndex_Type = Unsigned32
_MplsTrHopMpDownstreamIfIndex_Object = MibTableColumn
mplsTrHopMpDownstreamIfIndex = _MplsTrHopMpDownstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 2, 1, 102),
    _MplsTrHopMpDownstreamIfIndex_Type()
)
mplsTrHopMpDownstreamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTrHopMpDownstreamIfIndex.setStatus("current")
_MplsCvTrSysCounterTable_Object = MibTable
mplsCvTrSysCounterTable = _MplsCvTrSysCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3)
)
if mibBuilder.loadTexts:
    mplsCvTrSysCounterTable.setStatus("current")
_MplsCvTrSysCounterEntry_Object = MibTableRow
mplsCvTrSysCounterEntry = _MplsCvTrSysCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1)
)
mplsCvTrSysCounterEntry.setIndexNames(
    (0, "DC-OAMM-MIB", "oammEntApplIndex"),
)
if mibBuilder.loadTexts:
    mplsCvTrSysCounterEntry.setStatus("current")
_MplsCvTrSysCounterReqsSent_Type = Counter32
_MplsCvTrSysCounterReqsSent_Object = MibTableColumn
mplsCvTrSysCounterReqsSent = _MplsCvTrSysCounterReqsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 1),
    _MplsCvTrSysCounterReqsSent_Type()
)
mplsCvTrSysCounterReqsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterReqsSent.setStatus("current")
_MplsCvTrSysCounterReqsRcvd_Type = Counter32
_MplsCvTrSysCounterReqsRcvd_Object = MibTableColumn
mplsCvTrSysCounterReqsRcvd = _MplsCvTrSysCounterReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 2),
    _MplsCvTrSysCounterReqsRcvd_Type()
)
mplsCvTrSysCounterReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterReqsRcvd.setStatus("current")
_MplsCvTrSysCounterTotalRepsSent_Type = Counter32
_MplsCvTrSysCounterTotalRepsSent_Object = MibTableColumn
mplsCvTrSysCounterTotalRepsSent = _MplsCvTrSysCounterTotalRepsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 3),
    _MplsCvTrSysCounterTotalRepsSent_Type()
)
mplsCvTrSysCounterTotalRepsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterTotalRepsSent.setStatus("current")
_MplsCvTrSysCounterTotalRepsRcvd_Type = Counter32
_MplsCvTrSysCounterTotalRepsRcvd_Object = MibTableColumn
mplsCvTrSysCounterTotalRepsRcvd = _MplsCvTrSysCounterTotalRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 4),
    _MplsCvTrSysCounterTotalRepsRcvd_Type()
)
mplsCvTrSysCounterTotalRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterTotalRepsRcvd.setStatus("current")
_MplsCvTrSysCounterOKRepsSent_Type = Counter32
_MplsCvTrSysCounterOKRepsSent_Object = MibTableColumn
mplsCvTrSysCounterOKRepsSent = _MplsCvTrSysCounterOKRepsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 5),
    _MplsCvTrSysCounterOKRepsSent_Type()
)
mplsCvTrSysCounterOKRepsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterOKRepsSent.setStatus("current")
_MplsCvTrSysCounterOKRepsRcvd_Type = Counter32
_MplsCvTrSysCounterOKRepsRcvd_Object = MibTableColumn
mplsCvTrSysCounterOKRepsRcvd = _MplsCvTrSysCounterOKRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 6),
    _MplsCvTrSysCounterOKRepsRcvd_Type()
)
mplsCvTrSysCounterOKRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterOKRepsRcvd.setStatus("current")
_MplsCvTrSysCounterBadRepsSent_Type = Counter32
_MplsCvTrSysCounterBadRepsSent_Object = MibTableColumn
mplsCvTrSysCounterBadRepsSent = _MplsCvTrSysCounterBadRepsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 7),
    _MplsCvTrSysCounterBadRepsSent_Type()
)
mplsCvTrSysCounterBadRepsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterBadRepsSent.setStatus("current")
_MplsCvTrSysCounterIllRepsSent_Type = Counter32
_MplsCvTrSysCounterIllRepsSent_Object = MibTableColumn
mplsCvTrSysCounterIllRepsSent = _MplsCvTrSysCounterIllRepsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 8),
    _MplsCvTrSysCounterIllRepsSent_Type()
)
mplsCvTrSysCounterIllRepsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterIllRepsSent.setStatus("current")
_MplsCvTrSysCounterBadRepsRcvd_Type = Counter32
_MplsCvTrSysCounterBadRepsRcvd_Object = MibTableColumn
mplsCvTrSysCounterBadRepsRcvd = _MplsCvTrSysCounterBadRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 9),
    _MplsCvTrSysCounterBadRepsRcvd_Type()
)
mplsCvTrSysCounterBadRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterBadRepsRcvd.setStatus("current")
_MplsCvTrSysCounterIllRepsRcvd_Type = Counter32
_MplsCvTrSysCounterIllRepsRcvd_Object = MibTableColumn
mplsCvTrSysCounterIllRepsRcvd = _MplsCvTrSysCounterIllRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 10),
    _MplsCvTrSysCounterIllRepsRcvd_Type()
)
mplsCvTrSysCounterIllRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterIllRepsRcvd.setStatus("current")
_MplsCvTrSysCounterTmoRepsRcvd_Type = Counter32
_MplsCvTrSysCounterTmoRepsRcvd_Object = MibTableColumn
mplsCvTrSysCounterTmoRepsRcvd = _MplsCvTrSysCounterTmoRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 11),
    _MplsCvTrSysCounterTmoRepsRcvd_Type()
)
mplsCvTrSysCounterTmoRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterTmoRepsRcvd.setStatus("current")
_MplsCvTrSysCounterBadSeqRepsRcvd_Type = Counter32
_MplsCvTrSysCounterBadSeqRepsRcvd_Object = MibTableColumn
mplsCvTrSysCounterBadSeqRepsRcvd = _MplsCvTrSysCounterBadSeqRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 3, 1, 12),
    _MplsCvTrSysCounterBadSeqRepsRcvd_Type()
)
mplsCvTrSysCounterBadSeqRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsCvTrSysCounterBadSeqRepsRcvd.setStatus("current")
_MplsMpCvTrCntrTable_Object = MibTable
mplsMpCvTrCntrTable = _MplsMpCvTrCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4)
)
if mibBuilder.loadTexts:
    mplsMpCvTrCntrTable.setStatus("current")
_MplsMpCvTrCntrEntry_Object = MibTableRow
mplsMpCvTrCntrEntry = _MplsMpCvTrCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1)
)
mplsMpCvTrCntrEntry.setIndexNames(
    (0, "DC-OAMM-MIB", "oammEntApplIndex"),
    (0, "DC-OAM-MPLS-MP-MIB", "mplsMpIndex"),
)
if mibBuilder.loadTexts:
    mplsMpCvTrCntrEntry.setStatus("current")
_MplsMpCvTrCntrNextSeqToSend_Type = Unsigned32
_MplsMpCvTrCntrNextSeqToSend_Object = MibTableColumn
mplsMpCvTrCntrNextSeqToSend = _MplsMpCvTrCntrNextSeqToSend_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 1),
    _MplsMpCvTrCntrNextSeqToSend_Type()
)
mplsMpCvTrCntrNextSeqToSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrNextSeqToSend.setStatus("current")


class _MplsMpCvTrCntrLastRcvdRetCode_Type(Integer32):
    """Custom type mplsMpCvTrCntrLastRcvdRetCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              256,
              257,
              258,
              259,
              260)
        )
    )
    namedValues = NamedValues(
        *(("noRC", 0),
          ("badRequestSent", 1),
          ("unrecognizedTlv", 2),
          ("egress", 3),
          ("noMapping", 4),
          ("mappingMismatch", 5),
          ("interfaceUnknown", 6),
          ("labelSwitch", 8),
          ("noForwarding", 9),
          ("wrongLabel", 10),
          ("noLabel", 11),
          ("unknownFec", 12),
          ("singleLabel", 13),
          ("timeout", 256),
          ("requestNotSent", 257),
          ("resourceFailure", 258),
          ("badReplyReceived", 259),
          ("ttlLimitReached", 260))
    )


_MplsMpCvTrCntrLastRcvdRetCode_Type.__name__ = "Integer32"
_MplsMpCvTrCntrLastRcvdRetCode_Object = MibTableColumn
mplsMpCvTrCntrLastRcvdRetCode = _MplsMpCvTrCntrLastRcvdRetCode_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 2),
    _MplsMpCvTrCntrLastRcvdRetCode_Type()
)
mplsMpCvTrCntrLastRcvdRetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrLastRcvdRetCode.setStatus("current")
_MplsMpCvTrCntrReqsSent_Type = Counter32
_MplsMpCvTrCntrReqsSent_Object = MibTableColumn
mplsMpCvTrCntrReqsSent = _MplsMpCvTrCntrReqsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 3),
    _MplsMpCvTrCntrReqsSent_Type()
)
mplsMpCvTrCntrReqsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrReqsSent.setStatus("current")
_MplsMpCvTrCntrReqsRcvd_Type = Counter32
_MplsMpCvTrCntrReqsRcvd_Object = MibTableColumn
mplsMpCvTrCntrReqsRcvd = _MplsMpCvTrCntrReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 4),
    _MplsMpCvTrCntrReqsRcvd_Type()
)
mplsMpCvTrCntrReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrReqsRcvd.setStatus("current")
_MplsMpCvTrCntrTotalRepsSent_Type = Counter32
_MplsMpCvTrCntrTotalRepsSent_Object = MibTableColumn
mplsMpCvTrCntrTotalRepsSent = _MplsMpCvTrCntrTotalRepsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 5),
    _MplsMpCvTrCntrTotalRepsSent_Type()
)
mplsMpCvTrCntrTotalRepsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrTotalRepsSent.setStatus("current")
_MplsMpCvTrCntrTotalRepsRcvd_Type = Counter32
_MplsMpCvTrCntrTotalRepsRcvd_Object = MibTableColumn
mplsMpCvTrCntrTotalRepsRcvd = _MplsMpCvTrCntrTotalRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 6),
    _MplsMpCvTrCntrTotalRepsRcvd_Type()
)
mplsMpCvTrCntrTotalRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrTotalRepsRcvd.setStatus("current")
_MplsMpCvTrCntrOKRepsSent_Type = Counter32
_MplsMpCvTrCntrOKRepsSent_Object = MibTableColumn
mplsMpCvTrCntrOKRepsSent = _MplsMpCvTrCntrOKRepsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 7),
    _MplsMpCvTrCntrOKRepsSent_Type()
)
mplsMpCvTrCntrOKRepsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrOKRepsSent.setStatus("current")
_MplsMpCvTrCntrOKRepsRcvd_Type = Counter32
_MplsMpCvTrCntrOKRepsRcvd_Object = MibTableColumn
mplsMpCvTrCntrOKRepsRcvd = _MplsMpCvTrCntrOKRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 8),
    _MplsMpCvTrCntrOKRepsRcvd_Type()
)
mplsMpCvTrCntrOKRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrOKRepsRcvd.setStatus("current")
_MplsMpCvTrCntrBadRepsSent_Type = Counter32
_MplsMpCvTrCntrBadRepsSent_Object = MibTableColumn
mplsMpCvTrCntrBadRepsSent = _MplsMpCvTrCntrBadRepsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 9),
    _MplsMpCvTrCntrBadRepsSent_Type()
)
mplsMpCvTrCntrBadRepsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrBadRepsSent.setStatus("current")
_MplsMpCvTrCntrIllRepsSent_Type = Counter32
_MplsMpCvTrCntrIllRepsSent_Object = MibTableColumn
mplsMpCvTrCntrIllRepsSent = _MplsMpCvTrCntrIllRepsSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 10),
    _MplsMpCvTrCntrIllRepsSent_Type()
)
mplsMpCvTrCntrIllRepsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrIllRepsSent.setStatus("current")
_MplsMpCvTrCntrBadRepsRcvd_Type = Counter32
_MplsMpCvTrCntrBadRepsRcvd_Object = MibTableColumn
mplsMpCvTrCntrBadRepsRcvd = _MplsMpCvTrCntrBadRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 11),
    _MplsMpCvTrCntrBadRepsRcvd_Type()
)
mplsMpCvTrCntrBadRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrBadRepsRcvd.setStatus("current")
_MplsMpCvTrCntrIllRepsRcvd_Type = Counter32
_MplsMpCvTrCntrIllRepsRcvd_Object = MibTableColumn
mplsMpCvTrCntrIllRepsRcvd = _MplsMpCvTrCntrIllRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 12),
    _MplsMpCvTrCntrIllRepsRcvd_Type()
)
mplsMpCvTrCntrIllRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrIllRepsRcvd.setStatus("current")
_MplsMpCvTrCntrTmoRepsRcvd_Type = Counter32
_MplsMpCvTrCntrTmoRepsRcvd_Object = MibTableColumn
mplsMpCvTrCntrTmoRepsRcvd = _MplsMpCvTrCntrTmoRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 13),
    _MplsMpCvTrCntrTmoRepsRcvd_Type()
)
mplsMpCvTrCntrTmoRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrTmoRepsRcvd.setStatus("current")
_MplsMpCvTrCntrBadSeqRepsRcvd_Type = Counter32
_MplsMpCvTrCntrBadSeqRepsRcvd_Object = MibTableColumn
mplsMpCvTrCntrBadSeqRepsRcvd = _MplsMpCvTrCntrBadSeqRepsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 1, 4, 1, 14),
    _MplsMpCvTrCntrBadSeqRepsRcvd_Type()
)
mplsMpCvTrCntrBadSeqRepsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpCvTrCntrBadSeqRepsRcvd.setStatus("current")
_LsppConformance_ObjectIdentity = ObjectIdentity
lsppConformance = _LsppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 2)
)
_LsppGroups_ObjectIdentity = ObjectIdentity
lsppGroups = _LsppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 2, 1)
)
_LsppCompliances_ObjectIdentity = ObjectIdentity
lsppCompliances = _LsppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 2, 2)
)

# Managed Objects groups

lsppGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 2, 1, 1)
)
lsppGeneralGroup.setObjects(
      *(("DC-OAM-LSP-PING-MIB", "mplsCvTrMpRowStatus"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpPhb"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvStatus"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvMessages"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvInterval"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvVerifyReverse"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvTtl"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvReturnCode"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvRvsReturnCode"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvRepliesRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvRoundTripMin"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvRoundTripAve"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpCvRoundTripMax"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpTrStatus"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpTimeout"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrMpTrReturnCode"),
        ("DC-OAM-LSP-PING-MIB", "mplsTrHopMpReturnCode"),
        ("DC-OAM-LSP-PING-MIB", "mplsTrHopMpNextHopAddressType"),
        ("DC-OAM-LSP-PING-MIB", "mplsTrHopMpNextHopAddress"),
        ("DC-OAM-LSP-PING-MIB", "mplsTrHopMpLabel"),
        ("DC-OAM-LSP-PING-MIB", "mplsTrHopMpRoundTrip"),
        ("DC-OAM-LSP-PING-MIB", "mplsTrHopMpMtu"),
        ("DC-OAM-LSP-PING-MIB", "mplsTrHopMpDownstreamIfAddrType"),
        ("DC-OAM-LSP-PING-MIB", "mplsTrHopMpDownstreamIfAddr"),
        ("DC-OAM-LSP-PING-MIB", "mplsTrHopMpDownstreamIfIndex"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterReqsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterReqsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterTotalRepsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterTotalRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterOKRepsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterOKRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterBadRepsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterIllRepsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterBadRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterIllRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterTmoRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsCvTrSysCounterBadSeqRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrNextSeqToSend"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrLastRcvdRetCode"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrReqsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrReqsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrTotalRepsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrTotalRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrOKRepsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrOKRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrBadRepsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrIllRepsSent"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrBadRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrIllRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrTmoRepsRcvd"),
        ("DC-OAM-LSP-PING-MIB", "mplsMpCvTrCntrBadSeqRepsRcvd"))
)
if mibBuilder.loadTexts:
    lsppGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lsppModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 2, 2, 1)
)
lsppModuleFullCompliance.setObjects(
    ("DC-OAM-LSP-PING-MIB", "lsppGeneralGroup")
)
if mibBuilder.loadTexts:
    lsppModuleFullCompliance.setStatus(
        "current"
    )

lsppModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 12, 2, 2, 2)
)
lsppModuleReadOnlyCompliance.setObjects(
    ("DC-OAM-LSP-PING-MIB", "lsppGeneralGroup")
)
if mibBuilder.loadTexts:
    lsppModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-OAM-LSP-PING-MIB",
    **{"nbase": nbase,
       "opx": opx,
       "lspPingMib": lspPingMib,
       "lsppObjects": lsppObjects,
       "mplsCvTrMpTable": mplsCvTrMpTable,
       "mplsCvTrMpEntry": mplsCvTrMpEntry,
       "mplsCvTrMpIndex": mplsCvTrMpIndex,
       "mplsCvTrMpRowStatus": mplsCvTrMpRowStatus,
       "mplsCvTrMpPhb": mplsCvTrMpPhb,
       "mplsCvTrMpCvStatus": mplsCvTrMpCvStatus,
       "mplsCvTrMpCvMessages": mplsCvTrMpCvMessages,
       "mplsCvTrMpCvInterval": mplsCvTrMpCvInterval,
       "mplsCvTrMpCvVerifyReverse": mplsCvTrMpCvVerifyReverse,
       "mplsCvTrMpCvTtl": mplsCvTrMpCvTtl,
       "mplsCvTrMpCvReturnCode": mplsCvTrMpCvReturnCode,
       "mplsCvTrMpCvRvsReturnCode": mplsCvTrMpCvRvsReturnCode,
       "mplsCvTrMpCvRepliesRcvd": mplsCvTrMpCvRepliesRcvd,
       "mplsCvTrMpCvRoundTripMin": mplsCvTrMpCvRoundTripMin,
       "mplsCvTrMpCvRoundTripAve": mplsCvTrMpCvRoundTripAve,
       "mplsCvTrMpCvRoundTripMax": mplsCvTrMpCvRoundTripMax,
       "mplsCvTrMpTrStatus": mplsCvTrMpTrStatus,
       "mplsCvTrMpTimeout": mplsCvTrMpTimeout,
       "mplsCvTrMpTrReturnCode": mplsCvTrMpTrReturnCode,
       "mplsTrHopMpTable": mplsTrHopMpTable,
       "mplsTrHopMpEntry": mplsTrHopMpEntry,
       "mplsTrHopNumber": mplsTrHopNumber,
       "mplsTrHopMpReturnCode": mplsTrHopMpReturnCode,
       "mplsTrHopMpNextHopAddressType": mplsTrHopMpNextHopAddressType,
       "mplsTrHopMpNextHopAddress": mplsTrHopMpNextHopAddress,
       "mplsTrHopMpLabel": mplsTrHopMpLabel,
       "mplsTrHopMpRoundTrip": mplsTrHopMpRoundTrip,
       "mplsTrHopMpMtu": mplsTrHopMpMtu,
       "mplsTrHopMpDownstreamIfAddrType": mplsTrHopMpDownstreamIfAddrType,
       "mplsTrHopMpDownstreamIfAddr": mplsTrHopMpDownstreamIfAddr,
       "mplsTrHopMpDownstreamIfIndex": mplsTrHopMpDownstreamIfIndex,
       "mplsCvTrSysCounterTable": mplsCvTrSysCounterTable,
       "mplsCvTrSysCounterEntry": mplsCvTrSysCounterEntry,
       "mplsCvTrSysCounterReqsSent": mplsCvTrSysCounterReqsSent,
       "mplsCvTrSysCounterReqsRcvd": mplsCvTrSysCounterReqsRcvd,
       "mplsCvTrSysCounterTotalRepsSent": mplsCvTrSysCounterTotalRepsSent,
       "mplsCvTrSysCounterTotalRepsRcvd": mplsCvTrSysCounterTotalRepsRcvd,
       "mplsCvTrSysCounterOKRepsSent": mplsCvTrSysCounterOKRepsSent,
       "mplsCvTrSysCounterOKRepsRcvd": mplsCvTrSysCounterOKRepsRcvd,
       "mplsCvTrSysCounterBadRepsSent": mplsCvTrSysCounterBadRepsSent,
       "mplsCvTrSysCounterIllRepsSent": mplsCvTrSysCounterIllRepsSent,
       "mplsCvTrSysCounterBadRepsRcvd": mplsCvTrSysCounterBadRepsRcvd,
       "mplsCvTrSysCounterIllRepsRcvd": mplsCvTrSysCounterIllRepsRcvd,
       "mplsCvTrSysCounterTmoRepsRcvd": mplsCvTrSysCounterTmoRepsRcvd,
       "mplsCvTrSysCounterBadSeqRepsRcvd": mplsCvTrSysCounterBadSeqRepsRcvd,
       "mplsMpCvTrCntrTable": mplsMpCvTrCntrTable,
       "mplsMpCvTrCntrEntry": mplsMpCvTrCntrEntry,
       "mplsMpCvTrCntrNextSeqToSend": mplsMpCvTrCntrNextSeqToSend,
       "mplsMpCvTrCntrLastRcvdRetCode": mplsMpCvTrCntrLastRcvdRetCode,
       "mplsMpCvTrCntrReqsSent": mplsMpCvTrCntrReqsSent,
       "mplsMpCvTrCntrReqsRcvd": mplsMpCvTrCntrReqsRcvd,
       "mplsMpCvTrCntrTotalRepsSent": mplsMpCvTrCntrTotalRepsSent,
       "mplsMpCvTrCntrTotalRepsRcvd": mplsMpCvTrCntrTotalRepsRcvd,
       "mplsMpCvTrCntrOKRepsSent": mplsMpCvTrCntrOKRepsSent,
       "mplsMpCvTrCntrOKRepsRcvd": mplsMpCvTrCntrOKRepsRcvd,
       "mplsMpCvTrCntrBadRepsSent": mplsMpCvTrCntrBadRepsSent,
       "mplsMpCvTrCntrIllRepsSent": mplsMpCvTrCntrIllRepsSent,
       "mplsMpCvTrCntrBadRepsRcvd": mplsMpCvTrCntrBadRepsRcvd,
       "mplsMpCvTrCntrIllRepsRcvd": mplsMpCvTrCntrIllRepsRcvd,
       "mplsMpCvTrCntrTmoRepsRcvd": mplsMpCvTrCntrTmoRepsRcvd,
       "mplsMpCvTrCntrBadSeqRepsRcvd": mplsMpCvTrCntrBadSeqRepsRcvd,
       "lsppConformance": lsppConformance,
       "lsppGroups": lsppGroups,
       "lsppGeneralGroup": lsppGeneralGroup,
       "lsppCompliances": lsppCompliances,
       "lsppModuleFullCompliance": lsppModuleFullCompliance,
       "lsppModuleReadOnlyCompliance": lsppModuleReadOnlyCompliance}
)
