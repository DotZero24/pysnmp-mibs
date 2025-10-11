# SNMP MIB module (FS-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-PIM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:06 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ipMRouteGroup,
 ipMRouteNextHopAddress,
 ipMRouteNextHopGroup,
 ipMRouteNextHopIfIndex,
 ipMRouteNextHopSource,
 ipMRouteNextHopSourceMask,
 ipMRouteSource,
 ipMRouteSourceMask) = mibBuilder.importSymbols(
    "IPMROUTE-STD-MIB",
    "ipMRouteGroup",
    "ipMRouteNextHopAddress",
    "ipMRouteNextHopGroup",
    "ipMRouteNextHopIfIndex",
    "ipMRouteNextHopSource",
    "ipMRouteNextHopSourceMask",
    "ipMRouteSource",
    "ipMRouteSourceMask")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

fsPimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27)
)
if mibBuilder.loadTexts:
    fsPimMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPimMIBObjects_ObjectIdentity = ObjectIdentity
fsPimMIBObjects = _FsPimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1)
)
_FsPim_ObjectIdentity = ObjectIdentity
fsPim = _FsPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1)
)


class _FsPimJoinPruneInterval_Type(Integer32):
    """Custom type fsPimJoinPruneInterval based on Integer32"""
    defaultValue = 60


_FsPimJoinPruneInterval_Type.__name__ = "Integer32"
_FsPimJoinPruneInterval_Object = MibScalar
fsPimJoinPruneInterval = _FsPimJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 1),
    _FsPimJoinPruneInterval_Type()
)
fsPimJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimJoinPruneInterval.setUnits("seconds")
_FsPimInterfaceTable_Object = MibTable
fsPimInterfaceTable = _FsPimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsPimInterfaceTable.setStatus("current")
_FsPimInterfaceEntry_Object = MibTableRow
fsPimInterfaceEntry = _FsPimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1)
)
fsPimInterfaceEntry.setIndexNames(
    (0, "FS-PIM-MIB", "fsPimInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsPimInterfaceEntry.setStatus("current")
_FsPimInterfaceIfIndex_Type = InterfaceIndex
_FsPimInterfaceIfIndex_Object = MibTableColumn
fsPimInterfaceIfIndex = _FsPimInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 1),
    _FsPimInterfaceIfIndex_Type()
)
fsPimInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimInterfaceIfIndex.setStatus("current")
_FsPimInterfaceAddress_Type = IpAddress
_FsPimInterfaceAddress_Object = MibTableColumn
fsPimInterfaceAddress = _FsPimInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 2),
    _FsPimInterfaceAddress_Type()
)
fsPimInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceAddress.setStatus("current")
_FsPimInterfaceNetMask_Type = IpAddress
_FsPimInterfaceNetMask_Object = MibTableColumn
fsPimInterfaceNetMask = _FsPimInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 3),
    _FsPimInterfaceNetMask_Type()
)
fsPimInterfaceNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceNetMask.setStatus("current")


class _FsPimInterfaceMode_Type(Integer32):
    """Custom type fsPimInterfaceMode based on Integer32"""
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
        *(("dense", 1),
          ("sparse", 2),
          ("sparseDense", 3))
    )


_FsPimInterfaceMode_Type.__name__ = "Integer32"
_FsPimInterfaceMode_Object = MibTableColumn
fsPimInterfaceMode = _FsPimInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 4),
    _FsPimInterfaceMode_Type()
)
fsPimInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceMode.setStatus("current")
_FsPimInterfaceDR_Type = IpAddress
_FsPimInterfaceDR_Object = MibTableColumn
fsPimInterfaceDR = _FsPimInterfaceDR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 5),
    _FsPimInterfaceDR_Type()
)
fsPimInterfaceDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceDR.setStatus("current")


class _FsPimInterfaceHelloInterval_Type(Integer32):
    """Custom type fsPimInterfaceHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimInterfaceHelloInterval_Type.__name__ = "Integer32"
_FsPimInterfaceHelloInterval_Object = MibTableColumn
fsPimInterfaceHelloInterval = _FsPimInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 6),
    _FsPimInterfaceHelloInterval_Type()
)
fsPimInterfaceHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimInterfaceHelloInterval.setUnits("seconds")
_FsPimInterfaceJoinPruneInterval_Type = Integer32
_FsPimInterfaceJoinPruneInterval_Object = MibTableColumn
fsPimInterfaceJoinPruneInterval = _FsPimInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 7),
    _FsPimInterfaceJoinPruneInterval_Type()
)
fsPimInterfaceJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimInterfaceJoinPruneInterval.setUnits("seconds")


class _FsPimInterfaceCBSRPreference_Type(Integer32):
    """Custom type fsPimInterfaceCBSRPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_FsPimInterfaceCBSRPreference_Type.__name__ = "Integer32"
_FsPimInterfaceCBSRPreference_Object = MibTableColumn
fsPimInterfaceCBSRPreference = _FsPimInterfaceCBSRPreference_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 8),
    _FsPimInterfaceCBSRPreference_Type()
)
fsPimInterfaceCBSRPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceCBSRPreference.setStatus("current")


class _FsPimInterfaceTrigHelloInterval_Type(Integer32):
    """Custom type fsPimInterfaceTrigHelloInterval based on Integer32"""
    defaultValue = 5


_FsPimInterfaceTrigHelloInterval_Type.__name__ = "Integer32"
_FsPimInterfaceTrigHelloInterval_Object = MibTableColumn
fsPimInterfaceTrigHelloInterval = _FsPimInterfaceTrigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 9),
    _FsPimInterfaceTrigHelloInterval_Type()
)
fsPimInterfaceTrigHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceTrigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimInterfaceTrigHelloInterval.setUnits("seconds")


class _FsPimInterfaceHelloHoldtime_Type(Integer32):
    """Custom type fsPimInterfaceHelloHoldtime based on Integer32"""
    defaultValue = 105

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimInterfaceHelloHoldtime_Type.__name__ = "Integer32"
_FsPimInterfaceHelloHoldtime_Object = MibTableColumn
fsPimInterfaceHelloHoldtime = _FsPimInterfaceHelloHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 10),
    _FsPimInterfaceHelloHoldtime_Type()
)
fsPimInterfaceHelloHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceHelloHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    fsPimInterfaceHelloHoldtime.setUnits("seconds")


class _FsPimInterfaceLanPruneDelay_Type(Integer32):
    """Custom type fsPimInterfaceLanPruneDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FsPimInterfaceLanPruneDelay_Type.__name__ = "Integer32"
_FsPimInterfaceLanPruneDelay_Object = MibTableColumn
fsPimInterfaceLanPruneDelay = _FsPimInterfaceLanPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 11),
    _FsPimInterfaceLanPruneDelay_Type()
)
fsPimInterfaceLanPruneDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceLanPruneDelay.setStatus("current")


class _FsPimInterfacePropagationDelay_Type(Integer32):
    """Custom type fsPimInterfacePropagationDelay based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FsPimInterfacePropagationDelay_Type.__name__ = "Integer32"
_FsPimInterfacePropagationDelay_Object = MibTableColumn
fsPimInterfacePropagationDelay = _FsPimInterfacePropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 12),
    _FsPimInterfacePropagationDelay_Type()
)
fsPimInterfacePropagationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfacePropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    fsPimInterfacePropagationDelay.setUnits("milliseconds")


class _FsPimInterfaceOverrideInterval_Type(Integer32):
    """Custom type fsPimInterfaceOverrideInterval based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimInterfaceOverrideInterval_Type.__name__ = "Integer32"
_FsPimInterfaceOverrideInterval_Object = MibTableColumn
fsPimInterfaceOverrideInterval = _FsPimInterfaceOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 13),
    _FsPimInterfaceOverrideInterval_Type()
)
fsPimInterfaceOverrideInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceOverrideInterval.setStatus("current")


class _FsPimInterfaceGenerationID_Type(Integer32):
    """Custom type fsPimInterfaceGenerationID based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FsPimInterfaceGenerationID_Type.__name__ = "Integer32"
_FsPimInterfaceGenerationID_Object = MibTableColumn
fsPimInterfaceGenerationID = _FsPimInterfaceGenerationID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 14),
    _FsPimInterfaceGenerationID_Type()
)
fsPimInterfaceGenerationID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceGenerationID.setStatus("current")


class _FsPimInterfaceJoinPruneHoldtime_Type(Integer32):
    """Custom type fsPimInterfaceJoinPruneHoldtime based on Integer32"""
    defaultValue = 210

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimInterfaceJoinPruneHoldtime_Type.__name__ = "Integer32"
_FsPimInterfaceJoinPruneHoldtime_Object = MibTableColumn
fsPimInterfaceJoinPruneHoldtime = _FsPimInterfaceJoinPruneHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 15),
    _FsPimInterfaceJoinPruneHoldtime_Type()
)
fsPimInterfaceJoinPruneHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceJoinPruneHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    fsPimInterfaceJoinPruneHoldtime.setUnits("seconds")


class _FsPimInterfaceGraftRetryInterval_Type(Integer32):
    """Custom type fsPimInterfaceGraftRetryInterval based on Integer32"""
    defaultValue = 3


_FsPimInterfaceGraftRetryInterval_Type.__name__ = "Integer32"
_FsPimInterfaceGraftRetryInterval_Object = MibTableColumn
fsPimInterfaceGraftRetryInterval = _FsPimInterfaceGraftRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 16),
    _FsPimInterfaceGraftRetryInterval_Type()
)
fsPimInterfaceGraftRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimInterfaceGraftRetryInterval.setUnits("seconds")


class _FsPimInterfaceMaxGraftRetries_Type(Integer32):
    """Custom type fsPimInterfaceMaxGraftRetries based on Integer32"""
    defaultValue = 2


_FsPimInterfaceMaxGraftRetries_Type.__name__ = "Integer32"
_FsPimInterfaceMaxGraftRetries_Object = MibTableColumn
fsPimInterfaceMaxGraftRetries = _FsPimInterfaceMaxGraftRetries_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 17),
    _FsPimInterfaceMaxGraftRetries_Type()
)
fsPimInterfaceMaxGraftRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceMaxGraftRetries.setStatus("current")


class _FsPimInterfaceSRTTLThreshold_Type(Integer32):
    """Custom type fsPimInterfaceSRTTLThreshold based on Integer32"""
    defaultValue = 0


_FsPimInterfaceSRTTLThreshold_Type.__name__ = "Integer32"
_FsPimInterfaceSRTTLThreshold_Object = MibTableColumn
fsPimInterfaceSRTTLThreshold = _FsPimInterfaceSRTTLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 18),
    _FsPimInterfaceSRTTLThreshold_Type()
)
fsPimInterfaceSRTTLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceSRTTLThreshold.setStatus("current")
_FsPimInterfaceLanDelayEnabled_Type = TruthValue
_FsPimInterfaceLanDelayEnabled_Object = MibTableColumn
fsPimInterfaceLanDelayEnabled = _FsPimInterfaceLanDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 19),
    _FsPimInterfaceLanDelayEnabled_Type()
)
fsPimInterfaceLanDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceLanDelayEnabled.setStatus("current")
_FsPimInterfaceSRCapable_Type = TruthValue
_FsPimInterfaceSRCapable_Object = MibTableColumn
fsPimInterfaceSRCapable = _FsPimInterfaceSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 20),
    _FsPimInterfaceSRCapable_Type()
)
fsPimInterfaceSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceSRCapable.setStatus("current")


class _FsPimInterfaceDRPriority_Type(Integer32):
    """Custom type fsPimInterfaceDRPriority based on Integer32"""
    defaultValue = 1


_FsPimInterfaceDRPriority_Type.__name__ = "Integer32"
_FsPimInterfaceDRPriority_Object = MibTableColumn
fsPimInterfaceDRPriority = _FsPimInterfaceDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 21),
    _FsPimInterfaceDRPriority_Type()
)
fsPimInterfaceDRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceDRPriority.setStatus("current")
_FsPimInterfaceNbrCounter_Type = Integer32
_FsPimInterfaceNbrCounter_Object = MibTableColumn
fsPimInterfaceNbrCounter = _FsPimInterfaceNbrCounter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 22),
    _FsPimInterfaceNbrCounter_Type()
)
fsPimInterfaceNbrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceNbrCounter.setStatus("current")


class _FsPimInterfaceBsrBorderEnabled_Type(EnabledStatus):
    """Custom type fsPimInterfaceBsrBorderEnabled based on EnabledStatus"""
    defaultValue = 2


_FsPimInterfaceBsrBorderEnabled_Type.__name__ = "EnabledStatus"
_FsPimInterfaceBsrBorderEnabled_Object = MibTableColumn
fsPimInterfaceBsrBorderEnabled = _FsPimInterfaceBsrBorderEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 23),
    _FsPimInterfaceBsrBorderEnabled_Type()
)
fsPimInterfaceBsrBorderEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceBsrBorderEnabled.setStatus("current")
_FsPimInterfaceCountIn_Type = Integer32
_FsPimInterfaceCountIn_Object = MibTableColumn
fsPimInterfaceCountIn = _FsPimInterfaceCountIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 24),
    _FsPimInterfaceCountIn_Type()
)
fsPimInterfaceCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceCountIn.setStatus("current")
_FsPimInterfaceCountOut_Type = Integer32
_FsPimInterfaceCountOut_Object = MibTableColumn
fsPimInterfaceCountOut = _FsPimInterfaceCountOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 25),
    _FsPimInterfaceCountOut_Type()
)
fsPimInterfaceCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceCountOut.setStatus("current")


class _FsPimInterfaceEnabled_Type(EnabledStatus):
    """Custom type fsPimInterfaceEnabled based on EnabledStatus"""
    defaultValue = 2


_FsPimInterfaceEnabled_Type.__name__ = "EnabledStatus"
_FsPimInterfaceEnabled_Object = MibTableColumn
fsPimInterfaceEnabled = _FsPimInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 26),
    _FsPimInterfaceEnabled_Type()
)
fsPimInterfaceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceEnabled.setStatus("current")


class _FsPimNeighborFilterAcl_Type(DisplayString):
    """Custom type fsPimNeighborFilterAcl based on DisplayString"""
    defaultValue = OctetString("")


_FsPimNeighborFilterAcl_Type.__name__ = "DisplayString"
_FsPimNeighborFilterAcl_Object = MibTableColumn
fsPimNeighborFilterAcl = _FsPimNeighborFilterAcl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 27),
    _FsPimNeighborFilterAcl_Type()
)
fsPimNeighborFilterAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimNeighborFilterAcl.setStatus("current")


class _FsPimDrSupportAddressBound_Type(DisplayString):
    """Custom type fsPimDrSupportAddressBound based on DisplayString"""
    defaultValue = OctetString("")


_FsPimDrSupportAddressBound_Type.__name__ = "DisplayString"
_FsPimDrSupportAddressBound_Object = MibTableColumn
fsPimDrSupportAddressBound = _FsPimDrSupportAddressBound_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 2, 1, 28),
    _FsPimDrSupportAddressBound_Type()
)
fsPimDrSupportAddressBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimDrSupportAddressBound.setStatus("current")
_FsPimNeighborTable_Object = MibTable
fsPimNeighborTable = _FsPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fsPimNeighborTable.setStatus("current")
_FsPimNeighborEntry_Object = MibTableRow
fsPimNeighborEntry = _FsPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1)
)
fsPimNeighborEntry.setIndexNames(
    (0, "FS-PIM-MIB", "fsPimNeighborAddress"),
)
if mibBuilder.loadTexts:
    fsPimNeighborEntry.setStatus("current")
_FsPimNeighborAddress_Type = IpAddress
_FsPimNeighborAddress_Object = MibTableColumn
fsPimNeighborAddress = _FsPimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 1),
    _FsPimNeighborAddress_Type()
)
fsPimNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimNeighborAddress.setStatus("current")
_FsPimNeighborIfIndex_Type = InterfaceIndex
_FsPimNeighborIfIndex_Object = MibTableColumn
fsPimNeighborIfIndex = _FsPimNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 2),
    _FsPimNeighborIfIndex_Type()
)
fsPimNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborIfIndex.setStatus("current")
_FsPimNeighborUpTime_Type = TimeTicks
_FsPimNeighborUpTime_Object = MibTableColumn
fsPimNeighborUpTime = _FsPimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 3),
    _FsPimNeighborUpTime_Type()
)
fsPimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborUpTime.setStatus("current")
_FsPimNeighborExpiryTime_Type = TimeTicks
_FsPimNeighborExpiryTime_Object = MibTableColumn
fsPimNeighborExpiryTime = _FsPimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 4),
    _FsPimNeighborExpiryTime_Type()
)
fsPimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborExpiryTime.setStatus("current")


class _FsPimNeighborMode_Type(Integer32):
    """Custom type fsPimNeighborMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2))
    )


_FsPimNeighborMode_Type.__name__ = "Integer32"
_FsPimNeighborMode_Object = MibTableColumn
fsPimNeighborMode = _FsPimNeighborMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 5),
    _FsPimNeighborMode_Type()
)
fsPimNeighborMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborMode.setStatus("deprecated")
_FsPimNeighborLanPruneDelay_Type = Integer32
_FsPimNeighborLanPruneDelay_Object = MibTableColumn
fsPimNeighborLanPruneDelay = _FsPimNeighborLanPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 6),
    _FsPimNeighborLanPruneDelay_Type()
)
fsPimNeighborLanPruneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborLanPruneDelay.setStatus("current")
_FsPimNeighborOverrideInterval_Type = Integer32
_FsPimNeighborOverrideInterval_Object = MibTableColumn
fsPimNeighborOverrideInterval = _FsPimNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 7),
    _FsPimNeighborOverrideInterval_Type()
)
fsPimNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborOverrideInterval.setStatus("current")
_FsPimNeighborTBit_Type = Integer32
_FsPimNeighborTBit_Object = MibTableColumn
fsPimNeighborTBit = _FsPimNeighborTBit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 8),
    _FsPimNeighborTBit_Type()
)
fsPimNeighborTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborTBit.setStatus("current")
_FsPimNeighborSRCapable_Type = TruthValue
_FsPimNeighborSRCapable_Object = MibTableColumn
fsPimNeighborSRCapable = _FsPimNeighborSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 9),
    _FsPimNeighborSRCapable_Type()
)
fsPimNeighborSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborSRCapable.setStatus("current")
_FsPimNeighborDRPresent_Type = TruthValue
_FsPimNeighborDRPresent_Object = MibTableColumn
fsPimNeighborDRPresent = _FsPimNeighborDRPresent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 3, 1, 10),
    _FsPimNeighborDRPresent_Type()
)
fsPimNeighborDRPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborDRPresent.setStatus("current")
_FsPimIpMRouteTable_Object = MibTable
fsPimIpMRouteTable = _FsPimIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fsPimIpMRouteTable.setStatus("current")
_FsPimIpMRouteEntry_Object = MibTableRow
fsPimIpMRouteEntry = _FsPimIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4, 1)
)
fsPimIpMRouteEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    fsPimIpMRouteEntry.setStatus("current")
_FsPimIpMRouteUpstreamAssertTimer_Type = TimeTicks
_FsPimIpMRouteUpstreamAssertTimer_Object = MibTableColumn
fsPimIpMRouteUpstreamAssertTimer = _FsPimIpMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4, 1, 1),
    _FsPimIpMRouteUpstreamAssertTimer_Type()
)
fsPimIpMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteUpstreamAssertTimer.setStatus("current")
_FsPimIpMRouteAssertMetric_Type = Integer32
_FsPimIpMRouteAssertMetric_Object = MibTableColumn
fsPimIpMRouteAssertMetric = _FsPimIpMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4, 1, 2),
    _FsPimIpMRouteAssertMetric_Type()
)
fsPimIpMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteAssertMetric.setStatus("current")
_FsPimIpMRouteAssertMetricPref_Type = Integer32
_FsPimIpMRouteAssertMetricPref_Object = MibTableColumn
fsPimIpMRouteAssertMetricPref = _FsPimIpMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4, 1, 3),
    _FsPimIpMRouteAssertMetricPref_Type()
)
fsPimIpMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteAssertMetricPref.setStatus("current")
_FsPimIpMRouteAssertRPTBit_Type = TruthValue
_FsPimIpMRouteAssertRPTBit_Object = MibTableColumn
fsPimIpMRouteAssertRPTBit = _FsPimIpMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4, 1, 4),
    _FsPimIpMRouteAssertRPTBit_Type()
)
fsPimIpMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteAssertRPTBit.setStatus("current")


class _FsPimIpMRouteFlags_Type(Integer32):
    """Custom type fsPimIpMRouteFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rpt", 0),
          ("spt", 1))
    )


_FsPimIpMRouteFlags_Type.__name__ = "Integer32"
_FsPimIpMRouteFlags_Object = MibTableColumn
fsPimIpMRouteFlags = _FsPimIpMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4, 1, 5),
    _FsPimIpMRouteFlags_Type()
)
fsPimIpMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteFlags.setStatus("current")
_FsPimIpMRouteRPFNeighbor_Type = IpAddress
_FsPimIpMRouteRPFNeighbor_Object = MibTableColumn
fsPimIpMRouteRPFNeighbor = _FsPimIpMRouteRPFNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4, 1, 6),
    _FsPimIpMRouteRPFNeighbor_Type()
)
fsPimIpMRouteRPFNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteRPFNeighbor.setStatus("current")
_FsPimIpMRouteSourceTimer_Type = TimeTicks
_FsPimIpMRouteSourceTimer_Object = MibTableColumn
fsPimIpMRouteSourceTimer = _FsPimIpMRouteSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4, 1, 7),
    _FsPimIpMRouteSourceTimer_Type()
)
fsPimIpMRouteSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteSourceTimer.setStatus("current")
_FsPimIpMRouteOriginatorSRTTL_Type = Integer32
_FsPimIpMRouteOriginatorSRTTL_Object = MibTableColumn
fsPimIpMRouteOriginatorSRTTL = _FsPimIpMRouteOriginatorSRTTL_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 4, 1, 8),
    _FsPimIpMRouteOriginatorSRTTL_Type()
)
fsPimIpMRouteOriginatorSRTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteOriginatorSRTTL.setStatus("current")
_FsPimIpMRouteNextHopTable_Object = MibTable
fsPimIpMRouteNextHopTable = _FsPimIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopTable.setStatus("current")
_FsPimIpMRouteNextHopEntry_Object = MibTableRow
fsPimIpMRouteNextHopEntry = _FsPimIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 5, 1)
)
fsPimIpMRouteNextHopEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopEntry.setStatus("current")


class _FsPimIpMRouteNextHopPruneReason_Type(Integer32):
    """Custom type fsPimIpMRouteNextHopPruneReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("prune", 2),
          ("assert", 3))
    )


_FsPimIpMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_FsPimIpMRouteNextHopPruneReason_Object = MibTableColumn
fsPimIpMRouteNextHopPruneReason = _FsPimIpMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 5, 1, 1),
    _FsPimIpMRouteNextHopPruneReason_Type()
)
fsPimIpMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopPruneReason.setStatus("current")
_FsPimIpMRouteNextHopAssertWinner_Type = IpAddress
_FsPimIpMRouteNextHopAssertWinner_Object = MibTableColumn
fsPimIpMRouteNextHopAssertWinner = _FsPimIpMRouteNextHopAssertWinner_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 5, 1, 2),
    _FsPimIpMRouteNextHopAssertWinner_Type()
)
fsPimIpMRouteNextHopAssertWinner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopAssertWinner.setStatus("current")
_FsPimIpMRouteNextHopAssertTimer_Type = TimeTicks
_FsPimIpMRouteNextHopAssertTimer_Object = MibTableColumn
fsPimIpMRouteNextHopAssertTimer = _FsPimIpMRouteNextHopAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 5, 1, 3),
    _FsPimIpMRouteNextHopAssertTimer_Type()
)
fsPimIpMRouteNextHopAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopAssertTimer.setStatus("current")
_FsPimIpMRouteNextHopAssertMetric_Type = Integer32
_FsPimIpMRouteNextHopAssertMetric_Object = MibTableColumn
fsPimIpMRouteNextHopAssertMetric = _FsPimIpMRouteNextHopAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 5, 1, 4),
    _FsPimIpMRouteNextHopAssertMetric_Type()
)
fsPimIpMRouteNextHopAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopAssertMetric.setStatus("current")
_FsPimIpMRouteNextHopAssertMetricPref_Type = Integer32
_FsPimIpMRouteNextHopAssertMetricPref_Object = MibTableColumn
fsPimIpMRouteNextHopAssertMetricPref = _FsPimIpMRouteNextHopAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 5, 1, 5),
    _FsPimIpMRouteNextHopAssertMetricPref_Type()
)
fsPimIpMRouteNextHopAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopAssertMetricPref.setStatus("current")
_FsPimIpMRouteNextHopJoinPruneTimer_Type = TimeTicks
_FsPimIpMRouteNextHopJoinPruneTimer_Object = MibTableColumn
fsPimIpMRouteNextHopJoinPruneTimer = _FsPimIpMRouteNextHopJoinPruneTimer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 5, 1, 6),
    _FsPimIpMRouteNextHopJoinPruneTimer_Type()
)
fsPimIpMRouteNextHopJoinPruneTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopJoinPruneTimer.setStatus("current")
_FsPimRPSetTable_Object = MibTable
fsPimRPSetTable = _FsPimRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fsPimRPSetTable.setStatus("current")
_FsPimRPSetEntry_Object = MibTableRow
fsPimRPSetEntry = _FsPimRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 6, 1)
)
fsPimRPSetEntry.setIndexNames(
    (0, "FS-PIM-MIB", "fsPimRPSetComponent"),
    (0, "FS-PIM-MIB", "fsPimRPSetGroupAddress"),
    (0, "FS-PIM-MIB", "fsPimRPSetGroupMask"),
    (0, "FS-PIM-MIB", "fsPimRPSetAddress"),
)
if mibBuilder.loadTexts:
    fsPimRPSetEntry.setStatus("current")
_FsPimRPSetGroupAddress_Type = IpAddress
_FsPimRPSetGroupAddress_Object = MibTableColumn
fsPimRPSetGroupAddress = _FsPimRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 6, 1, 1),
    _FsPimRPSetGroupAddress_Type()
)
fsPimRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimRPSetGroupAddress.setStatus("current")
_FsPimRPSetGroupMask_Type = IpAddress
_FsPimRPSetGroupMask_Object = MibTableColumn
fsPimRPSetGroupMask = _FsPimRPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 6, 1, 2),
    _FsPimRPSetGroupMask_Type()
)
fsPimRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimRPSetGroupMask.setStatus("current")
_FsPimRPSetAddress_Type = IpAddress
_FsPimRPSetAddress_Object = MibTableColumn
fsPimRPSetAddress = _FsPimRPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 6, 1, 3),
    _FsPimRPSetAddress_Type()
)
fsPimRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimRPSetAddress.setStatus("current")


class _FsPimRPSetHoldTime_Type(Integer32):
    """Custom type fsPimRPSetHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimRPSetHoldTime_Type.__name__ = "Integer32"
_FsPimRPSetHoldTime_Object = MibTableColumn
fsPimRPSetHoldTime = _FsPimRPSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 6, 1, 4),
    _FsPimRPSetHoldTime_Type()
)
fsPimRPSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimRPSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fsPimRPSetHoldTime.setUnits("seconds")
_FsPimRPSetExpiryTime_Type = TimeTicks
_FsPimRPSetExpiryTime_Object = MibTableColumn
fsPimRPSetExpiryTime = _FsPimRPSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 6, 1, 5),
    _FsPimRPSetExpiryTime_Type()
)
fsPimRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimRPSetExpiryTime.setStatus("current")


class _FsPimRPSetComponent_Type(Integer32):
    """Custom type fsPimRPSetComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimRPSetComponent_Type.__name__ = "Integer32"
_FsPimRPSetComponent_Object = MibTableColumn
fsPimRPSetComponent = _FsPimRPSetComponent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 6, 1, 6),
    _FsPimRPSetComponent_Type()
)
fsPimRPSetComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimRPSetComponent.setStatus("current")
_FsPimRPSetUpTime_Type = TimeTicks
_FsPimRPSetUpTime_Object = MibTableColumn
fsPimRPSetUpTime = _FsPimRPSetUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 6, 1, 7),
    _FsPimRPSetUpTime_Type()
)
fsPimRPSetUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimRPSetUpTime.setStatus("current")
_FsPimComponentTable_Object = MibTable
fsPimComponentTable = _FsPimComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7)
)
if mibBuilder.loadTexts:
    fsPimComponentTable.setStatus("current")
_FsPimComponentEntry_Object = MibTableRow
fsPimComponentEntry = _FsPimComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1)
)
fsPimComponentEntry.setIndexNames(
    (0, "FS-PIM-MIB", "fsPimComponentIndex"),
)
if mibBuilder.loadTexts:
    fsPimComponentEntry.setStatus("current")


class _FsPimComponentIndex_Type(Integer32):
    """Custom type fsPimComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimComponentIndex_Type.__name__ = "Integer32"
_FsPimComponentIndex_Object = MibTableColumn
fsPimComponentIndex = _FsPimComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1, 1),
    _FsPimComponentIndex_Type()
)
fsPimComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimComponentIndex.setStatus("current")
_FsPimComponentBSRAddress_Type = IpAddress
_FsPimComponentBSRAddress_Object = MibTableColumn
fsPimComponentBSRAddress = _FsPimComponentBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1, 2),
    _FsPimComponentBSRAddress_Type()
)
fsPimComponentBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimComponentBSRAddress.setStatus("current")
_FsPimComponentBSRExpiryTime_Type = TimeTicks
_FsPimComponentBSRExpiryTime_Object = MibTableColumn
fsPimComponentBSRExpiryTime = _FsPimComponentBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1, 3),
    _FsPimComponentBSRExpiryTime_Type()
)
fsPimComponentBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimComponentBSRExpiryTime.setStatus("current")


class _FsPimComponentCRPHoldTime_Type(Integer32):
    """Custom type fsPimComponentCRPHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimComponentCRPHoldTime_Type.__name__ = "Integer32"
_FsPimComponentCRPHoldTime_Object = MibTableColumn
fsPimComponentCRPHoldTime = _FsPimComponentCRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1, 4),
    _FsPimComponentCRPHoldTime_Type()
)
fsPimComponentCRPHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimComponentCRPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fsPimComponentCRPHoldTime.setUnits("seconds")
_FsPimComponentBSRUptime_Type = TimeTicks
_FsPimComponentBSRUptime_Object = MibTableColumn
fsPimComponentBSRUptime = _FsPimComponentBSRUptime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1, 5),
    _FsPimComponentBSRUptime_Type()
)
fsPimComponentBSRUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimComponentBSRUptime.setStatus("current")
_FsPimComponentBSRPriority_Type = Integer32
_FsPimComponentBSRPriority_Object = MibTableColumn
fsPimComponentBSRPriority = _FsPimComponentBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1, 6),
    _FsPimComponentBSRPriority_Type()
)
fsPimComponentBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimComponentBSRPriority.setStatus("current")
_FsPimComponentBSRHashMaskLength_Type = Integer32
_FsPimComponentBSRHashMaskLength_Object = MibTableColumn
fsPimComponentBSRHashMaskLength = _FsPimComponentBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1, 7),
    _FsPimComponentBSRHashMaskLength_Type()
)
fsPimComponentBSRHashMaskLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimComponentBSRHashMaskLength.setStatus("current")
_FsPimComponentBSRNextBsrMessage_Type = TimeTicks
_FsPimComponentBSRNextBsrMessage_Object = MibTableColumn
fsPimComponentBSRNextBsrMessage = _FsPimComponentBSRNextBsrMessage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1, 8),
    _FsPimComponentBSRNextBsrMessage_Type()
)
fsPimComponentBSRNextBsrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimComponentBSRNextBsrMessage.setStatus("current")
_FsPimComponentNextCandRPAdv_Type = TimeTicks
_FsPimComponentNextCandRPAdv_Object = MibTableColumn
fsPimComponentNextCandRPAdv = _FsPimComponentNextCandRPAdv_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 7, 1, 9),
    _FsPimComponentNextCandRPAdv_Type()
)
fsPimComponentNextCandRPAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimComponentNextCandRPAdv.setStatus("current")


class _FsPimSourceLifetime_Type(Integer32):
    """Custom type fsPimSourceLifetime based on Integer32"""
    defaultValue = 2100


_FsPimSourceLifetime_Type.__name__ = "Integer32"
_FsPimSourceLifetime_Object = MibScalar
fsPimSourceLifetime = _FsPimSourceLifetime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 8),
    _FsPimSourceLifetime_Type()
)
fsPimSourceLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimSourceLifetime.setStatus("current")
if mibBuilder.loadTexts:
    fsPimSourceLifetime.setUnits("seconds")


class _FsPimStateRefreshInterval_Type(Integer32):
    """Custom type fsPimStateRefreshInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimStateRefreshInterval_Type.__name__ = "Integer32"
_FsPimStateRefreshInterval_Object = MibScalar
fsPimStateRefreshInterval = _FsPimStateRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 9),
    _FsPimStateRefreshInterval_Type()
)
fsPimStateRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimStateRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimStateRefreshInterval.setUnits("seconds")


class _FsPimStateRefreshLimitInterval_Type(Integer32):
    """Custom type fsPimStateRefreshLimitInterval based on Integer32"""
    defaultValue = 0


_FsPimStateRefreshLimitInterval_Type.__name__ = "Integer32"
_FsPimStateRefreshLimitInterval_Object = MibScalar
fsPimStateRefreshLimitInterval = _FsPimStateRefreshLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 10),
    _FsPimStateRefreshLimitInterval_Type()
)
fsPimStateRefreshLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimStateRefreshLimitInterval.setStatus("current")


class _FsPimStateRefreshTimeToLive_Type(Integer32):
    """Custom type fsPimStateRefreshTimeToLive based on Integer32"""
    defaultValue = 16


_FsPimStateRefreshTimeToLive_Type.__name__ = "Integer32"
_FsPimStateRefreshTimeToLive_Object = MibScalar
fsPimStateRefreshTimeToLive = _FsPimStateRefreshTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 11),
    _FsPimStateRefreshTimeToLive_Type()
)
fsPimStateRefreshTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimStateRefreshTimeToLive.setStatus("current")
_FsPimBsrCandidateGroup_ObjectIdentity = ObjectIdentity
fsPimBsrCandidateGroup = _FsPimBsrCandidateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 12)
)
_FsPimBsrCandidateIfindex_Type = Integer32
_FsPimBsrCandidateIfindex_Object = MibScalar
fsPimBsrCandidateIfindex = _FsPimBsrCandidateIfindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 12, 1),
    _FsPimBsrCandidateIfindex_Type()
)
fsPimBsrCandidateIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimBsrCandidateIfindex.setStatus("current")


class _FsPimBsrCandidateHashMaskLength_Type(Integer32):
    """Custom type fsPimBsrCandidateHashMaskLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsPimBsrCandidateHashMaskLength_Type.__name__ = "Integer32"
_FsPimBsrCandidateHashMaskLength_Object = MibScalar
fsPimBsrCandidateHashMaskLength = _FsPimBsrCandidateHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 12, 2),
    _FsPimBsrCandidateHashMaskLength_Type()
)
fsPimBsrCandidateHashMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimBsrCandidateHashMaskLength.setStatus("current")


class _FsPimBsrCandidatePriority_Type(Integer32):
    """Custom type fsPimBsrCandidatePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimBsrCandidatePriority_Type.__name__ = "Integer32"
_FsPimBsrCandidatePriority_Object = MibScalar
fsPimBsrCandidatePriority = _FsPimBsrCandidatePriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 12, 3),
    _FsPimBsrCandidatePriority_Type()
)
fsPimBsrCandidatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimBsrCandidatePriority.setStatus("current")
_FsPimRPTable_Object = MibTable
fsPimRPTable = _FsPimRPTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 13)
)
if mibBuilder.loadTexts:
    fsPimRPTable.setStatus("current")
_FsPimRPEntry_Object = MibTableRow
fsPimRPEntry = _FsPimRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 13, 1)
)
fsPimRPEntry.setIndexNames(
    (0, "FS-PIM-MIB", "fsPimRPGroupAddress"),
)
if mibBuilder.loadTexts:
    fsPimRPEntry.setStatus("current")
_FsPimRPGroupAddress_Type = IpAddress
_FsPimRPGroupAddress_Object = MibTableColumn
fsPimRPGroupAddress = _FsPimRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 13, 1, 1),
    _FsPimRPGroupAddress_Type()
)
fsPimRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimRPGroupAddress.setStatus("current")
_FsPimRPAddress_Type = IpAddress
_FsPimRPAddress_Object = MibTableColumn
fsPimRPAddress = _FsPimRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 13, 1, 2),
    _FsPimRPAddress_Type()
)
fsPimRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimRPAddress.setStatus("current")
_FsPimRPExpiryTime_Type = TimeTicks
_FsPimRPExpiryTime_Object = MibTableColumn
fsPimRPExpiryTime = _FsPimRPExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 13, 1, 3),
    _FsPimRPExpiryTime_Type()
)
fsPimRPExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimRPExpiryTime.setStatus("current")
_FsPimRPNextRPReachableIn_Type = TimeTicks
_FsPimRPNextRPReachableIn_Object = MibTableColumn
fsPimRPNextRPReachableIn = _FsPimRPNextRPReachableIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 13, 1, 4),
    _FsPimRPNextRPReachableIn_Type()
)
fsPimRPNextRPReachableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimRPNextRPReachableIn.setStatus("current")
_FsPimStaticRPTable_Object = MibTable
fsPimStaticRPTable = _FsPimStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 14)
)
if mibBuilder.loadTexts:
    fsPimStaticRPTable.setStatus("current")
_FsPimStaticRPEntry_Object = MibTableRow
fsPimStaticRPEntry = _FsPimStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 14, 1)
)
fsPimStaticRPEntry.setIndexNames(
    (0, "FS-PIM-MIB", "fsPimStaticRPAddress"),
)
if mibBuilder.loadTexts:
    fsPimStaticRPEntry.setStatus("current")
_FsPimStaticRPAddress_Type = IpAddress
_FsPimStaticRPAddress_Object = MibTableColumn
fsPimStaticRPAddress = _FsPimStaticRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 14, 1, 1),
    _FsPimStaticRPAddress_Type()
)
fsPimStaticRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStaticRPAddress.setStatus("current")


class _FsPimStaticRPAddressIsOverride_Type(EnabledStatus):
    """Custom type fsPimStaticRPAddressIsOverride based on EnabledStatus"""
    defaultValue = 2


_FsPimStaticRPAddressIsOverride_Type.__name__ = "EnabledStatus"
_FsPimStaticRPAddressIsOverride_Object = MibTableColumn
fsPimStaticRPAddressIsOverride = _FsPimStaticRPAddressIsOverride_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 14, 1, 2),
    _FsPimStaticRPAddressIsOverride_Type()
)
fsPimStaticRPAddressIsOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStaticRPAddressIsOverride.setStatus("current")


class _FsPimStaticRPAclName_Type(DisplayString):
    """Custom type fsPimStaticRPAclName based on DisplayString"""
    defaultValue = OctetString("")


_FsPimStaticRPAclName_Type.__name__ = "DisplayString"
_FsPimStaticRPAclName_Object = MibTableColumn
fsPimStaticRPAclName = _FsPimStaticRPAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 14, 1, 3),
    _FsPimStaticRPAclName_Type()
)
fsPimStaticRPAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStaticRPAclName.setStatus("current")
_FsPimStaticRPStatus_Type = RowStatus
_FsPimStaticRPStatus_Object = MibTableColumn
fsPimStaticRPStatus = _FsPimStaticRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 14, 1, 4),
    _FsPimStaticRPStatus_Type()
)
fsPimStaticRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStaticRPStatus.setStatus("current")
_FsPimRpCandidateTable_Object = MibTable
fsPimRpCandidateTable = _FsPimRpCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 15)
)
if mibBuilder.loadTexts:
    fsPimRpCandidateTable.setStatus("current")
_FsPimRpCandidateEntry_Object = MibTableRow
fsPimRpCandidateEntry = _FsPimRpCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 15, 1)
)
fsPimRpCandidateEntry.setIndexNames(
    (0, "FS-PIM-MIB", "fsPimRpCandidateIfindex"),
)
if mibBuilder.loadTexts:
    fsPimRpCandidateEntry.setStatus("current")
_FsPimRpCandidateIfindex_Type = InterfaceIndex
_FsPimRpCandidateIfindex_Object = MibTableColumn
fsPimRpCandidateIfindex = _FsPimRpCandidateIfindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 15, 1, 1),
    _FsPimRpCandidateIfindex_Type()
)
fsPimRpCandidateIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimRpCandidateIfindex.setStatus("current")


class _FsPimRpCandidateAclName_Type(DisplayString):
    """Custom type fsPimRpCandidateAclName based on DisplayString"""
    defaultValue = OctetString("")


_FsPimRpCandidateAclName_Type.__name__ = "DisplayString"
_FsPimRpCandidateAclName_Object = MibTableColumn
fsPimRpCandidateAclName = _FsPimRpCandidateAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 15, 1, 2),
    _FsPimRpCandidateAclName_Type()
)
fsPimRpCandidateAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimRpCandidateAclName.setStatus("current")
_FsPimRpCandidateStatus_Type = RowStatus
_FsPimRpCandidateStatus_Object = MibTableColumn
fsPimRpCandidateStatus = _FsPimRpCandidateStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 1, 15, 1, 3),
    _FsPimRpCandidateStatus_Type()
)
fsPimRpCandidateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimRpCandidateStatus.setStatus("current")
_FsPimTraps_ObjectIdentity = ObjectIdentity
fsPimTraps = _FsPimTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 2)
)
_FsPimMIBConformance_ObjectIdentity = ObjectIdentity
fsPimMIBConformance = _FsPimMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 2)
)
_FsPimMIBCompliances_ObjectIdentity = ObjectIdentity
fsPimMIBCompliances = _FsPimMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 2, 1)
)
_FsPimMIBGroups_ObjectIdentity = ObjectIdentity
fsPimMIBGroups = _FsPimMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 2, 2)
)

# Managed Objects groups

fsPimMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 2, 2, 1)
)
fsPimMIBGroup.setObjects(
      *(("FS-PIM-MIB", "fsPimJoinPruneInterval"),
        ("FS-PIM-MIB", "fsPimInterfaceAddress"),
        ("FS-PIM-MIB", "fsPimInterfaceNetMask"),
        ("FS-PIM-MIB", "fsPimInterfaceMode"),
        ("FS-PIM-MIB", "fsPimInterfaceDR"),
        ("FS-PIM-MIB", "fsPimInterfaceHelloInterval"),
        ("FS-PIM-MIB", "fsPimInterfaceJoinPruneInterval"),
        ("FS-PIM-MIB", "fsPimInterfaceCBSRPreference"),
        ("FS-PIM-MIB", "fsPimInterfaceTrigHelloInterval"),
        ("FS-PIM-MIB", "fsPimInterfaceHelloHoldtime"),
        ("FS-PIM-MIB", "fsPimInterfaceLanPruneDelay"),
        ("FS-PIM-MIB", "fsPimInterfacePropagationDelay"),
        ("FS-PIM-MIB", "fsPimInterfaceOverrideInterval"),
        ("FS-PIM-MIB", "fsPimInterfaceGenerationID"),
        ("FS-PIM-MIB", "fsPimInterfaceJoinPruneHoldtime"),
        ("FS-PIM-MIB", "fsPimInterfaceGraftRetryInterval"),
        ("FS-PIM-MIB", "fsPimInterfaceMaxGraftRetries"),
        ("FS-PIM-MIB", "fsPimInterfaceSRTTLThreshold"),
        ("FS-PIM-MIB", "fsPimInterfaceLanDelayEnabled"),
        ("FS-PIM-MIB", "fsPimInterfaceSRCapable"),
        ("FS-PIM-MIB", "fsPimInterfaceDRPriority"),
        ("FS-PIM-MIB", "fsPimInterfaceNbrCounter"),
        ("FS-PIM-MIB", "fsPimInterfaceBsrBorderEnabled"),
        ("FS-PIM-MIB", "fsPimInterfaceCountIn"),
        ("FS-PIM-MIB", "fsPimInterfaceCountOut"),
        ("FS-PIM-MIB", "fsPimInterfaceEnabled"),
        ("FS-PIM-MIB", "fsPimNeighborFilterAcl"),
        ("FS-PIM-MIB", "fsPimDrSupportAddressBound"),
        ("FS-PIM-MIB", "fsPimNeighborIfIndex"),
        ("FS-PIM-MIB", "fsPimNeighborUpTime"),
        ("FS-PIM-MIB", "fsPimNeighborExpiryTime"),
        ("FS-PIM-MIB", "fsPimNeighborMode"),
        ("FS-PIM-MIB", "fsPimNeighborLanPruneDelay"),
        ("FS-PIM-MIB", "fsPimNeighborOverrideInterval"),
        ("FS-PIM-MIB", "fsPimNeighborTBit"),
        ("FS-PIM-MIB", "fsPimNeighborSRCapable"),
        ("FS-PIM-MIB", "fsPimNeighborDRPresent"),
        ("FS-PIM-MIB", "fsPimIpMRouteUpstreamAssertTimer"),
        ("FS-PIM-MIB", "fsPimIpMRouteAssertMetric"),
        ("FS-PIM-MIB", "fsPimIpMRouteAssertMetricPref"),
        ("FS-PIM-MIB", "fsPimIpMRouteAssertRPTBit"),
        ("FS-PIM-MIB", "fsPimIpMRouteFlags"),
        ("FS-PIM-MIB", "fsPimIpMRouteRPFNeighbor"),
        ("FS-PIM-MIB", "fsPimIpMRouteSourceTimer"),
        ("FS-PIM-MIB", "fsPimIpMRouteOriginatorSRTTL"),
        ("FS-PIM-MIB", "fsPimIpMRouteNextHopPruneReason"),
        ("FS-PIM-MIB", "fsPimIpMRouteNextHopAssertWinner"),
        ("FS-PIM-MIB", "fsPimIpMRouteNextHopAssertTimer"),
        ("FS-PIM-MIB", "fsPimIpMRouteNextHopAssertMetric"),
        ("FS-PIM-MIB", "fsPimIpMRouteNextHopAssertMetricPref"),
        ("FS-PIM-MIB", "fsPimIpMRouteNextHopJoinPruneTimer"),
        ("FS-PIM-MIB", "fsPimRPSetHoldTime"),
        ("FS-PIM-MIB", "fsPimRPSetExpiryTime"),
        ("FS-PIM-MIB", "fsPimRPSetUpTime"),
        ("FS-PIM-MIB", "fsPimComponentBSRAddress"),
        ("FS-PIM-MIB", "fsPimComponentBSRExpiryTime"),
        ("FS-PIM-MIB", "fsPimComponentCRPHoldTime"),
        ("FS-PIM-MIB", "fsPimComponentBSRUptime"),
        ("FS-PIM-MIB", "fsPimComponentBSRPriority"),
        ("FS-PIM-MIB", "fsPimComponentBSRHashMaskLength"),
        ("FS-PIM-MIB", "fsPimComponentBSRNextBsrMessage"),
        ("FS-PIM-MIB", "fsPimComponentNextCandRPAdv"),
        ("FS-PIM-MIB", "fsPimSourceLifetime"),
        ("FS-PIM-MIB", "fsPimStateRefreshInterval"),
        ("FS-PIM-MIB", "fsPimStateRefreshLimitInterval"),
        ("FS-PIM-MIB", "fsPimStateRefreshTimeToLive"),
        ("FS-PIM-MIB", "fsPimBsrCandidateIfindex"),
        ("FS-PIM-MIB", "fsPimBsrCandidateHashMaskLength"),
        ("FS-PIM-MIB", "fsPimBsrCandidatePriority"),
        ("FS-PIM-MIB", "fsPimRPAddress"),
        ("FS-PIM-MIB", "fsPimRPExpiryTime"),
        ("FS-PIM-MIB", "fsPimRPNextRPReachableIn"),
        ("FS-PIM-MIB", "fsPimStaticRPAddressIsOverride"),
        ("FS-PIM-MIB", "fsPimStaticRPAclName"),
        ("FS-PIM-MIB", "fsPimStaticRPStatus"),
        ("FS-PIM-MIB", "fsPimRpCandidateAclName"),
        ("FS-PIM-MIB", "fsPimRpCandidateStatus"))
)
if mibBuilder.loadTexts:
    fsPimMIBGroup.setStatus("current")


# Notification objects

fsPimNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 1, 2, 1)
)
fsPimNeighborLoss.setObjects(
    ("FS-PIM-MIB", "fsPimNeighborIfIndex")
)
if mibBuilder.loadTexts:
    fsPimNeighborLoss.setStatus(
        "current"
    )


# Notifications groups

fsPimNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 2, 2, 2)
)
fsPimNotifyGroup.setObjects(
    ("FS-PIM-MIB", "fsPimNeighborLoss")
)
if mibBuilder.loadTexts:
    fsPimNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsPimMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 27, 2, 1, 1)
)
fsPimMIBCompliance.setObjects(
    ("FS-PIM-MIB", "fsPimMIBGroup")
)
if mibBuilder.loadTexts:
    fsPimMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-PIM-MIB",
    **{"fsPimMIB": fsPimMIB,
       "fsPimMIBObjects": fsPimMIBObjects,
       "fsPim": fsPim,
       "fsPimJoinPruneInterval": fsPimJoinPruneInterval,
       "fsPimInterfaceTable": fsPimInterfaceTable,
       "fsPimInterfaceEntry": fsPimInterfaceEntry,
       "fsPimInterfaceIfIndex": fsPimInterfaceIfIndex,
       "fsPimInterfaceAddress": fsPimInterfaceAddress,
       "fsPimInterfaceNetMask": fsPimInterfaceNetMask,
       "fsPimInterfaceMode": fsPimInterfaceMode,
       "fsPimInterfaceDR": fsPimInterfaceDR,
       "fsPimInterfaceHelloInterval": fsPimInterfaceHelloInterval,
       "fsPimInterfaceJoinPruneInterval": fsPimInterfaceJoinPruneInterval,
       "fsPimInterfaceCBSRPreference": fsPimInterfaceCBSRPreference,
       "fsPimInterfaceTrigHelloInterval": fsPimInterfaceTrigHelloInterval,
       "fsPimInterfaceHelloHoldtime": fsPimInterfaceHelloHoldtime,
       "fsPimInterfaceLanPruneDelay": fsPimInterfaceLanPruneDelay,
       "fsPimInterfacePropagationDelay": fsPimInterfacePropagationDelay,
       "fsPimInterfaceOverrideInterval": fsPimInterfaceOverrideInterval,
       "fsPimInterfaceGenerationID": fsPimInterfaceGenerationID,
       "fsPimInterfaceJoinPruneHoldtime": fsPimInterfaceJoinPruneHoldtime,
       "fsPimInterfaceGraftRetryInterval": fsPimInterfaceGraftRetryInterval,
       "fsPimInterfaceMaxGraftRetries": fsPimInterfaceMaxGraftRetries,
       "fsPimInterfaceSRTTLThreshold": fsPimInterfaceSRTTLThreshold,
       "fsPimInterfaceLanDelayEnabled": fsPimInterfaceLanDelayEnabled,
       "fsPimInterfaceSRCapable": fsPimInterfaceSRCapable,
       "fsPimInterfaceDRPriority": fsPimInterfaceDRPriority,
       "fsPimInterfaceNbrCounter": fsPimInterfaceNbrCounter,
       "fsPimInterfaceBsrBorderEnabled": fsPimInterfaceBsrBorderEnabled,
       "fsPimInterfaceCountIn": fsPimInterfaceCountIn,
       "fsPimInterfaceCountOut": fsPimInterfaceCountOut,
       "fsPimInterfaceEnabled": fsPimInterfaceEnabled,
       "fsPimNeighborFilterAcl": fsPimNeighborFilterAcl,
       "fsPimDrSupportAddressBound": fsPimDrSupportAddressBound,
       "fsPimNeighborTable": fsPimNeighborTable,
       "fsPimNeighborEntry": fsPimNeighborEntry,
       "fsPimNeighborAddress": fsPimNeighborAddress,
       "fsPimNeighborIfIndex": fsPimNeighborIfIndex,
       "fsPimNeighborUpTime": fsPimNeighborUpTime,
       "fsPimNeighborExpiryTime": fsPimNeighborExpiryTime,
       "fsPimNeighborMode": fsPimNeighborMode,
       "fsPimNeighborLanPruneDelay": fsPimNeighborLanPruneDelay,
       "fsPimNeighborOverrideInterval": fsPimNeighborOverrideInterval,
       "fsPimNeighborTBit": fsPimNeighborTBit,
       "fsPimNeighborSRCapable": fsPimNeighborSRCapable,
       "fsPimNeighborDRPresent": fsPimNeighborDRPresent,
       "fsPimIpMRouteTable": fsPimIpMRouteTable,
       "fsPimIpMRouteEntry": fsPimIpMRouteEntry,
       "fsPimIpMRouteUpstreamAssertTimer": fsPimIpMRouteUpstreamAssertTimer,
       "fsPimIpMRouteAssertMetric": fsPimIpMRouteAssertMetric,
       "fsPimIpMRouteAssertMetricPref": fsPimIpMRouteAssertMetricPref,
       "fsPimIpMRouteAssertRPTBit": fsPimIpMRouteAssertRPTBit,
       "fsPimIpMRouteFlags": fsPimIpMRouteFlags,
       "fsPimIpMRouteRPFNeighbor": fsPimIpMRouteRPFNeighbor,
       "fsPimIpMRouteSourceTimer": fsPimIpMRouteSourceTimer,
       "fsPimIpMRouteOriginatorSRTTL": fsPimIpMRouteOriginatorSRTTL,
       "fsPimIpMRouteNextHopTable": fsPimIpMRouteNextHopTable,
       "fsPimIpMRouteNextHopEntry": fsPimIpMRouteNextHopEntry,
       "fsPimIpMRouteNextHopPruneReason": fsPimIpMRouteNextHopPruneReason,
       "fsPimIpMRouteNextHopAssertWinner": fsPimIpMRouteNextHopAssertWinner,
       "fsPimIpMRouteNextHopAssertTimer": fsPimIpMRouteNextHopAssertTimer,
       "fsPimIpMRouteNextHopAssertMetric": fsPimIpMRouteNextHopAssertMetric,
       "fsPimIpMRouteNextHopAssertMetricPref": fsPimIpMRouteNextHopAssertMetricPref,
       "fsPimIpMRouteNextHopJoinPruneTimer": fsPimIpMRouteNextHopJoinPruneTimer,
       "fsPimRPSetTable": fsPimRPSetTable,
       "fsPimRPSetEntry": fsPimRPSetEntry,
       "fsPimRPSetGroupAddress": fsPimRPSetGroupAddress,
       "fsPimRPSetGroupMask": fsPimRPSetGroupMask,
       "fsPimRPSetAddress": fsPimRPSetAddress,
       "fsPimRPSetHoldTime": fsPimRPSetHoldTime,
       "fsPimRPSetExpiryTime": fsPimRPSetExpiryTime,
       "fsPimRPSetComponent": fsPimRPSetComponent,
       "fsPimRPSetUpTime": fsPimRPSetUpTime,
       "fsPimComponentTable": fsPimComponentTable,
       "fsPimComponentEntry": fsPimComponentEntry,
       "fsPimComponentIndex": fsPimComponentIndex,
       "fsPimComponentBSRAddress": fsPimComponentBSRAddress,
       "fsPimComponentBSRExpiryTime": fsPimComponentBSRExpiryTime,
       "fsPimComponentCRPHoldTime": fsPimComponentCRPHoldTime,
       "fsPimComponentBSRUptime": fsPimComponentBSRUptime,
       "fsPimComponentBSRPriority": fsPimComponentBSRPriority,
       "fsPimComponentBSRHashMaskLength": fsPimComponentBSRHashMaskLength,
       "fsPimComponentBSRNextBsrMessage": fsPimComponentBSRNextBsrMessage,
       "fsPimComponentNextCandRPAdv": fsPimComponentNextCandRPAdv,
       "fsPimSourceLifetime": fsPimSourceLifetime,
       "fsPimStateRefreshInterval": fsPimStateRefreshInterval,
       "fsPimStateRefreshLimitInterval": fsPimStateRefreshLimitInterval,
       "fsPimStateRefreshTimeToLive": fsPimStateRefreshTimeToLive,
       "fsPimBsrCandidateGroup": fsPimBsrCandidateGroup,
       "fsPimBsrCandidateIfindex": fsPimBsrCandidateIfindex,
       "fsPimBsrCandidateHashMaskLength": fsPimBsrCandidateHashMaskLength,
       "fsPimBsrCandidatePriority": fsPimBsrCandidatePriority,
       "fsPimRPTable": fsPimRPTable,
       "fsPimRPEntry": fsPimRPEntry,
       "fsPimRPGroupAddress": fsPimRPGroupAddress,
       "fsPimRPAddress": fsPimRPAddress,
       "fsPimRPExpiryTime": fsPimRPExpiryTime,
       "fsPimRPNextRPReachableIn": fsPimRPNextRPReachableIn,
       "fsPimStaticRPTable": fsPimStaticRPTable,
       "fsPimStaticRPEntry": fsPimStaticRPEntry,
       "fsPimStaticRPAddress": fsPimStaticRPAddress,
       "fsPimStaticRPAddressIsOverride": fsPimStaticRPAddressIsOverride,
       "fsPimStaticRPAclName": fsPimStaticRPAclName,
       "fsPimStaticRPStatus": fsPimStaticRPStatus,
       "fsPimRpCandidateTable": fsPimRpCandidateTable,
       "fsPimRpCandidateEntry": fsPimRpCandidateEntry,
       "fsPimRpCandidateIfindex": fsPimRpCandidateIfindex,
       "fsPimRpCandidateAclName": fsPimRpCandidateAclName,
       "fsPimRpCandidateStatus": fsPimRpCandidateStatus,
       "fsPimTraps": fsPimTraps,
       "fsPimNeighborLoss": fsPimNeighborLoss,
       "fsPimMIBConformance": fsPimMIBConformance,
       "fsPimMIBCompliances": fsPimMIBCompliances,
       "fsPimMIBCompliance": fsPimMIBCompliance,
       "fsPimMIBGroups": fsPimMIBGroups,
       "fsPimMIBGroup": fsPimMIBGroup,
       "fsPimNotifyGroup": fsPimNotifyGroup}
)
