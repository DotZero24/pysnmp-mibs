# SNMP MIB module (QTECH-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-PIM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:12 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechPimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27)
)
if mibBuilder.loadTexts:
    qtechPimMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechPimMIBObjects_ObjectIdentity = ObjectIdentity
qtechPimMIBObjects = _QtechPimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1)
)
_QtechPim_ObjectIdentity = ObjectIdentity
qtechPim = _QtechPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1)
)


class _QtechPimJoinPruneInterval_Type(Integer32):
    """Custom type qtechPimJoinPruneInterval based on Integer32"""
    defaultValue = 60


_QtechPimJoinPruneInterval_Type.__name__ = "Integer32"
_QtechPimJoinPruneInterval_Object = MibScalar
qtechPimJoinPruneInterval = _QtechPimJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 1),
    _QtechPimJoinPruneInterval_Type()
)
qtechPimJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimJoinPruneInterval.setUnits("seconds")
_QtechPimInterfaceTable_Object = MibTable
qtechPimInterfaceTable = _QtechPimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qtechPimInterfaceTable.setStatus("current")
_QtechPimInterfaceEntry_Object = MibTableRow
qtechPimInterfaceEntry = _QtechPimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1)
)
qtechPimInterfaceEntry.setIndexNames(
    (0, "QTECH-PIM-MIB", "qtechPimInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    qtechPimInterfaceEntry.setStatus("current")
_QtechPimInterfaceIfIndex_Type = InterfaceIndex
_QtechPimInterfaceIfIndex_Object = MibTableColumn
qtechPimInterfaceIfIndex = _QtechPimInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 1),
    _QtechPimInterfaceIfIndex_Type()
)
qtechPimInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimInterfaceIfIndex.setStatus("current")
_QtechPimInterfaceAddress_Type = IpAddress
_QtechPimInterfaceAddress_Object = MibTableColumn
qtechPimInterfaceAddress = _QtechPimInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 2),
    _QtechPimInterfaceAddress_Type()
)
qtechPimInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimInterfaceAddress.setStatus("current")
_QtechPimInterfaceNetMask_Type = IpAddress
_QtechPimInterfaceNetMask_Object = MibTableColumn
qtechPimInterfaceNetMask = _QtechPimInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 3),
    _QtechPimInterfaceNetMask_Type()
)
qtechPimInterfaceNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimInterfaceNetMask.setStatus("current")


class _QtechPimInterfaceMode_Type(Integer32):
    """Custom type qtechPimInterfaceMode based on Integer32"""
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


_QtechPimInterfaceMode_Type.__name__ = "Integer32"
_QtechPimInterfaceMode_Object = MibTableColumn
qtechPimInterfaceMode = _QtechPimInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 4),
    _QtechPimInterfaceMode_Type()
)
qtechPimInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceMode.setStatus("current")
_QtechPimInterfaceDR_Type = IpAddress
_QtechPimInterfaceDR_Object = MibTableColumn
qtechPimInterfaceDR = _QtechPimInterfaceDR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 5),
    _QtechPimInterfaceDR_Type()
)
qtechPimInterfaceDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimInterfaceDR.setStatus("current")


class _QtechPimInterfaceHelloInterval_Type(Integer32):
    """Custom type qtechPimInterfaceHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechPimInterfaceHelloInterval_Type.__name__ = "Integer32"
_QtechPimInterfaceHelloInterval_Object = MibTableColumn
qtechPimInterfaceHelloInterval = _QtechPimInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 6),
    _QtechPimInterfaceHelloInterval_Type()
)
qtechPimInterfaceHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimInterfaceHelloInterval.setUnits("seconds")
_QtechPimInterfaceJoinPruneInterval_Type = Integer32
_QtechPimInterfaceJoinPruneInterval_Object = MibTableColumn
qtechPimInterfaceJoinPruneInterval = _QtechPimInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 7),
    _QtechPimInterfaceJoinPruneInterval_Type()
)
qtechPimInterfaceJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimInterfaceJoinPruneInterval.setUnits("seconds")


class _QtechPimInterfaceCBSRPreference_Type(Integer32):
    """Custom type qtechPimInterfaceCBSRPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_QtechPimInterfaceCBSRPreference_Type.__name__ = "Integer32"
_QtechPimInterfaceCBSRPreference_Object = MibTableColumn
qtechPimInterfaceCBSRPreference = _QtechPimInterfaceCBSRPreference_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 8),
    _QtechPimInterfaceCBSRPreference_Type()
)
qtechPimInterfaceCBSRPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceCBSRPreference.setStatus("current")


class _QtechPimInterfaceTrigHelloInterval_Type(Integer32):
    """Custom type qtechPimInterfaceTrigHelloInterval based on Integer32"""
    defaultValue = 5


_QtechPimInterfaceTrigHelloInterval_Type.__name__ = "Integer32"
_QtechPimInterfaceTrigHelloInterval_Object = MibTableColumn
qtechPimInterfaceTrigHelloInterval = _QtechPimInterfaceTrigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 9),
    _QtechPimInterfaceTrigHelloInterval_Type()
)
qtechPimInterfaceTrigHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceTrigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimInterfaceTrigHelloInterval.setUnits("seconds")


class _QtechPimInterfaceHelloHoldtime_Type(Integer32):
    """Custom type qtechPimInterfaceHelloHoldtime based on Integer32"""
    defaultValue = 105

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechPimInterfaceHelloHoldtime_Type.__name__ = "Integer32"
_QtechPimInterfaceHelloHoldtime_Object = MibTableColumn
qtechPimInterfaceHelloHoldtime = _QtechPimInterfaceHelloHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 10),
    _QtechPimInterfaceHelloHoldtime_Type()
)
qtechPimInterfaceHelloHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceHelloHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimInterfaceHelloHoldtime.setUnits("seconds")


class _QtechPimInterfaceLanPruneDelay_Type(Integer32):
    """Custom type qtechPimInterfaceLanPruneDelay based on Integer32"""
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


_QtechPimInterfaceLanPruneDelay_Type.__name__ = "Integer32"
_QtechPimInterfaceLanPruneDelay_Object = MibTableColumn
qtechPimInterfaceLanPruneDelay = _QtechPimInterfaceLanPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 11),
    _QtechPimInterfaceLanPruneDelay_Type()
)
qtechPimInterfaceLanPruneDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceLanPruneDelay.setStatus("current")


class _QtechPimInterfacePropagationDelay_Type(Integer32):
    """Custom type qtechPimInterfacePropagationDelay based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QtechPimInterfacePropagationDelay_Type.__name__ = "Integer32"
_QtechPimInterfacePropagationDelay_Object = MibTableColumn
qtechPimInterfacePropagationDelay = _QtechPimInterfacePropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 12),
    _QtechPimInterfacePropagationDelay_Type()
)
qtechPimInterfacePropagationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfacePropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimInterfacePropagationDelay.setUnits("milliseconds")


class _QtechPimInterfaceOverrideInterval_Type(Integer32):
    """Custom type qtechPimInterfaceOverrideInterval based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechPimInterfaceOverrideInterval_Type.__name__ = "Integer32"
_QtechPimInterfaceOverrideInterval_Object = MibTableColumn
qtechPimInterfaceOverrideInterval = _QtechPimInterfaceOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 13),
    _QtechPimInterfaceOverrideInterval_Type()
)
qtechPimInterfaceOverrideInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceOverrideInterval.setStatus("current")


class _QtechPimInterfaceGenerationID_Type(Integer32):
    """Custom type qtechPimInterfaceGenerationID based on Integer32"""
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


_QtechPimInterfaceGenerationID_Type.__name__ = "Integer32"
_QtechPimInterfaceGenerationID_Object = MibTableColumn
qtechPimInterfaceGenerationID = _QtechPimInterfaceGenerationID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 14),
    _QtechPimInterfaceGenerationID_Type()
)
qtechPimInterfaceGenerationID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceGenerationID.setStatus("current")


class _QtechPimInterfaceJoinPruneHoldtime_Type(Integer32):
    """Custom type qtechPimInterfaceJoinPruneHoldtime based on Integer32"""
    defaultValue = 210

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechPimInterfaceJoinPruneHoldtime_Type.__name__ = "Integer32"
_QtechPimInterfaceJoinPruneHoldtime_Object = MibTableColumn
qtechPimInterfaceJoinPruneHoldtime = _QtechPimInterfaceJoinPruneHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 15),
    _QtechPimInterfaceJoinPruneHoldtime_Type()
)
qtechPimInterfaceJoinPruneHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceJoinPruneHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimInterfaceJoinPruneHoldtime.setUnits("seconds")


class _QtechPimInterfaceGraftRetryInterval_Type(Integer32):
    """Custom type qtechPimInterfaceGraftRetryInterval based on Integer32"""
    defaultValue = 3


_QtechPimInterfaceGraftRetryInterval_Type.__name__ = "Integer32"
_QtechPimInterfaceGraftRetryInterval_Object = MibTableColumn
qtechPimInterfaceGraftRetryInterval = _QtechPimInterfaceGraftRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 16),
    _QtechPimInterfaceGraftRetryInterval_Type()
)
qtechPimInterfaceGraftRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimInterfaceGraftRetryInterval.setUnits("seconds")


class _QtechPimInterfaceMaxGraftRetries_Type(Integer32):
    """Custom type qtechPimInterfaceMaxGraftRetries based on Integer32"""
    defaultValue = 2


_QtechPimInterfaceMaxGraftRetries_Type.__name__ = "Integer32"
_QtechPimInterfaceMaxGraftRetries_Object = MibTableColumn
qtechPimInterfaceMaxGraftRetries = _QtechPimInterfaceMaxGraftRetries_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 17),
    _QtechPimInterfaceMaxGraftRetries_Type()
)
qtechPimInterfaceMaxGraftRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceMaxGraftRetries.setStatus("current")


class _QtechPimInterfaceSRTTLThreshold_Type(Integer32):
    """Custom type qtechPimInterfaceSRTTLThreshold based on Integer32"""
    defaultValue = 0


_QtechPimInterfaceSRTTLThreshold_Type.__name__ = "Integer32"
_QtechPimInterfaceSRTTLThreshold_Object = MibTableColumn
qtechPimInterfaceSRTTLThreshold = _QtechPimInterfaceSRTTLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 18),
    _QtechPimInterfaceSRTTLThreshold_Type()
)
qtechPimInterfaceSRTTLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceSRTTLThreshold.setStatus("current")
_QtechPimInterfaceLanDelayEnabled_Type = TruthValue
_QtechPimInterfaceLanDelayEnabled_Object = MibTableColumn
qtechPimInterfaceLanDelayEnabled = _QtechPimInterfaceLanDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 19),
    _QtechPimInterfaceLanDelayEnabled_Type()
)
qtechPimInterfaceLanDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimInterfaceLanDelayEnabled.setStatus("current")
_QtechPimInterfaceSRCapable_Type = TruthValue
_QtechPimInterfaceSRCapable_Object = MibTableColumn
qtechPimInterfaceSRCapable = _QtechPimInterfaceSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 20),
    _QtechPimInterfaceSRCapable_Type()
)
qtechPimInterfaceSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimInterfaceSRCapable.setStatus("current")


class _QtechPimInterfaceDRPriority_Type(Integer32):
    """Custom type qtechPimInterfaceDRPriority based on Integer32"""
    defaultValue = 1


_QtechPimInterfaceDRPriority_Type.__name__ = "Integer32"
_QtechPimInterfaceDRPriority_Object = MibTableColumn
qtechPimInterfaceDRPriority = _QtechPimInterfaceDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 21),
    _QtechPimInterfaceDRPriority_Type()
)
qtechPimInterfaceDRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceDRPriority.setStatus("current")
_QtechPimInterfaceNbrCounter_Type = Integer32
_QtechPimInterfaceNbrCounter_Object = MibTableColumn
qtechPimInterfaceNbrCounter = _QtechPimInterfaceNbrCounter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 22),
    _QtechPimInterfaceNbrCounter_Type()
)
qtechPimInterfaceNbrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimInterfaceNbrCounter.setStatus("current")


class _QtechPimInterfaceBsrBorderEnabled_Type(EnabledStatus):
    """Custom type qtechPimInterfaceBsrBorderEnabled based on EnabledStatus"""
    defaultValue = 2


_QtechPimInterfaceBsrBorderEnabled_Type.__name__ = "EnabledStatus"
_QtechPimInterfaceBsrBorderEnabled_Object = MibTableColumn
qtechPimInterfaceBsrBorderEnabled = _QtechPimInterfaceBsrBorderEnabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 23),
    _QtechPimInterfaceBsrBorderEnabled_Type()
)
qtechPimInterfaceBsrBorderEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceBsrBorderEnabled.setStatus("current")
_QtechPimInterfaceCountIn_Type = Integer32
_QtechPimInterfaceCountIn_Object = MibTableColumn
qtechPimInterfaceCountIn = _QtechPimInterfaceCountIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 24),
    _QtechPimInterfaceCountIn_Type()
)
qtechPimInterfaceCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimInterfaceCountIn.setStatus("current")
_QtechPimInterfaceCountOut_Type = Integer32
_QtechPimInterfaceCountOut_Object = MibTableColumn
qtechPimInterfaceCountOut = _QtechPimInterfaceCountOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 25),
    _QtechPimInterfaceCountOut_Type()
)
qtechPimInterfaceCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimInterfaceCountOut.setStatus("current")


class _QtechPimInterfaceEnabled_Type(EnabledStatus):
    """Custom type qtechPimInterfaceEnabled based on EnabledStatus"""
    defaultValue = 2


_QtechPimInterfaceEnabled_Type.__name__ = "EnabledStatus"
_QtechPimInterfaceEnabled_Object = MibTableColumn
qtechPimInterfaceEnabled = _QtechPimInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 26),
    _QtechPimInterfaceEnabled_Type()
)
qtechPimInterfaceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimInterfaceEnabled.setStatus("current")


class _QtechPimNeighborFilterAcl_Type(DisplayString):
    """Custom type qtechPimNeighborFilterAcl based on DisplayString"""
    defaultValue = OctetString("")


_QtechPimNeighborFilterAcl_Type.__name__ = "DisplayString"
_QtechPimNeighborFilterAcl_Object = MibTableColumn
qtechPimNeighborFilterAcl = _QtechPimNeighborFilterAcl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 27),
    _QtechPimNeighborFilterAcl_Type()
)
qtechPimNeighborFilterAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimNeighborFilterAcl.setStatus("current")


class _QtechPimDrSupportAddressBound_Type(DisplayString):
    """Custom type qtechPimDrSupportAddressBound based on DisplayString"""
    defaultValue = OctetString("")


_QtechPimDrSupportAddressBound_Type.__name__ = "DisplayString"
_QtechPimDrSupportAddressBound_Object = MibTableColumn
qtechPimDrSupportAddressBound = _QtechPimDrSupportAddressBound_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 2, 1, 28),
    _QtechPimDrSupportAddressBound_Type()
)
qtechPimDrSupportAddressBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimDrSupportAddressBound.setStatus("current")
_QtechPimNeighborTable_Object = MibTable
qtechPimNeighborTable = _QtechPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qtechPimNeighborTable.setStatus("current")
_QtechPimNeighborEntry_Object = MibTableRow
qtechPimNeighborEntry = _QtechPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1)
)
qtechPimNeighborEntry.setIndexNames(
    (0, "QTECH-PIM-MIB", "qtechPimNeighborAddress"),
)
if mibBuilder.loadTexts:
    qtechPimNeighborEntry.setStatus("current")
_QtechPimNeighborAddress_Type = IpAddress
_QtechPimNeighborAddress_Object = MibTableColumn
qtechPimNeighborAddress = _QtechPimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 1),
    _QtechPimNeighborAddress_Type()
)
qtechPimNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimNeighborAddress.setStatus("current")
_QtechPimNeighborIfIndex_Type = InterfaceIndex
_QtechPimNeighborIfIndex_Object = MibTableColumn
qtechPimNeighborIfIndex = _QtechPimNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 2),
    _QtechPimNeighborIfIndex_Type()
)
qtechPimNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimNeighborIfIndex.setStatus("current")
_QtechPimNeighborUpTime_Type = TimeTicks
_QtechPimNeighborUpTime_Object = MibTableColumn
qtechPimNeighborUpTime = _QtechPimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 3),
    _QtechPimNeighborUpTime_Type()
)
qtechPimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimNeighborUpTime.setStatus("current")
_QtechPimNeighborExpiryTime_Type = TimeTicks
_QtechPimNeighborExpiryTime_Object = MibTableColumn
qtechPimNeighborExpiryTime = _QtechPimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 4),
    _QtechPimNeighborExpiryTime_Type()
)
qtechPimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimNeighborExpiryTime.setStatus("current")


class _QtechPimNeighborMode_Type(Integer32):
    """Custom type qtechPimNeighborMode based on Integer32"""
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


_QtechPimNeighborMode_Type.__name__ = "Integer32"
_QtechPimNeighborMode_Object = MibTableColumn
qtechPimNeighborMode = _QtechPimNeighborMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 5),
    _QtechPimNeighborMode_Type()
)
qtechPimNeighborMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimNeighborMode.setStatus("deprecated")
_QtechPimNeighborLanPruneDelay_Type = Integer32
_QtechPimNeighborLanPruneDelay_Object = MibTableColumn
qtechPimNeighborLanPruneDelay = _QtechPimNeighborLanPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 6),
    _QtechPimNeighborLanPruneDelay_Type()
)
qtechPimNeighborLanPruneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimNeighborLanPruneDelay.setStatus("current")
_QtechPimNeighborOverrideInterval_Type = Integer32
_QtechPimNeighborOverrideInterval_Object = MibTableColumn
qtechPimNeighborOverrideInterval = _QtechPimNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 7),
    _QtechPimNeighborOverrideInterval_Type()
)
qtechPimNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimNeighborOverrideInterval.setStatus("current")
_QtechPimNeighborTBit_Type = Integer32
_QtechPimNeighborTBit_Object = MibTableColumn
qtechPimNeighborTBit = _QtechPimNeighborTBit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 8),
    _QtechPimNeighborTBit_Type()
)
qtechPimNeighborTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimNeighborTBit.setStatus("current")
_QtechPimNeighborSRCapable_Type = TruthValue
_QtechPimNeighborSRCapable_Object = MibTableColumn
qtechPimNeighborSRCapable = _QtechPimNeighborSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 9),
    _QtechPimNeighborSRCapable_Type()
)
qtechPimNeighborSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimNeighborSRCapable.setStatus("current")
_QtechPimNeighborDRPresent_Type = TruthValue
_QtechPimNeighborDRPresent_Object = MibTableColumn
qtechPimNeighborDRPresent = _QtechPimNeighborDRPresent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 3, 1, 10),
    _QtechPimNeighborDRPresent_Type()
)
qtechPimNeighborDRPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimNeighborDRPresent.setStatus("current")
_QtechPimIpMRouteTable_Object = MibTable
qtechPimIpMRouteTable = _QtechPimIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4)
)
if mibBuilder.loadTexts:
    qtechPimIpMRouteTable.setStatus("current")
_QtechPimIpMRouteEntry_Object = MibTableRow
qtechPimIpMRouteEntry = _QtechPimIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4, 1)
)
qtechPimIpMRouteEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    qtechPimIpMRouteEntry.setStatus("current")
_QtechPimIpMRouteUpstreamAssertTimer_Type = TimeTicks
_QtechPimIpMRouteUpstreamAssertTimer_Object = MibTableColumn
qtechPimIpMRouteUpstreamAssertTimer = _QtechPimIpMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4, 1, 1),
    _QtechPimIpMRouteUpstreamAssertTimer_Type()
)
qtechPimIpMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteUpstreamAssertTimer.setStatus("current")
_QtechPimIpMRouteAssertMetric_Type = Integer32
_QtechPimIpMRouteAssertMetric_Object = MibTableColumn
qtechPimIpMRouteAssertMetric = _QtechPimIpMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4, 1, 2),
    _QtechPimIpMRouteAssertMetric_Type()
)
qtechPimIpMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteAssertMetric.setStatus("current")
_QtechPimIpMRouteAssertMetricPref_Type = Integer32
_QtechPimIpMRouteAssertMetricPref_Object = MibTableColumn
qtechPimIpMRouteAssertMetricPref = _QtechPimIpMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4, 1, 3),
    _QtechPimIpMRouteAssertMetricPref_Type()
)
qtechPimIpMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteAssertMetricPref.setStatus("current")
_QtechPimIpMRouteAssertRPTBit_Type = TruthValue
_QtechPimIpMRouteAssertRPTBit_Object = MibTableColumn
qtechPimIpMRouteAssertRPTBit = _QtechPimIpMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4, 1, 4),
    _QtechPimIpMRouteAssertRPTBit_Type()
)
qtechPimIpMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteAssertRPTBit.setStatus("current")


class _QtechPimIpMRouteFlags_Type(Integer32):
    """Custom type qtechPimIpMRouteFlags based on Integer32"""
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


_QtechPimIpMRouteFlags_Type.__name__ = "Integer32"
_QtechPimIpMRouteFlags_Object = MibTableColumn
qtechPimIpMRouteFlags = _QtechPimIpMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4, 1, 5),
    _QtechPimIpMRouteFlags_Type()
)
qtechPimIpMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteFlags.setStatus("current")
_QtechPimIpMRouteRPFNeighbor_Type = IpAddress
_QtechPimIpMRouteRPFNeighbor_Object = MibTableColumn
qtechPimIpMRouteRPFNeighbor = _QtechPimIpMRouteRPFNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4, 1, 6),
    _QtechPimIpMRouteRPFNeighbor_Type()
)
qtechPimIpMRouteRPFNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteRPFNeighbor.setStatus("current")
_QtechPimIpMRouteSourceTimer_Type = TimeTicks
_QtechPimIpMRouteSourceTimer_Object = MibTableColumn
qtechPimIpMRouteSourceTimer = _QtechPimIpMRouteSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4, 1, 7),
    _QtechPimIpMRouteSourceTimer_Type()
)
qtechPimIpMRouteSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteSourceTimer.setStatus("current")
_QtechPimIpMRouteOriginatorSRTTL_Type = Integer32
_QtechPimIpMRouteOriginatorSRTTL_Object = MibTableColumn
qtechPimIpMRouteOriginatorSRTTL = _QtechPimIpMRouteOriginatorSRTTL_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 4, 1, 8),
    _QtechPimIpMRouteOriginatorSRTTL_Type()
)
qtechPimIpMRouteOriginatorSRTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteOriginatorSRTTL.setStatus("current")
_QtechPimIpMRouteNextHopTable_Object = MibTable
qtechPimIpMRouteNextHopTable = _QtechPimIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 5)
)
if mibBuilder.loadTexts:
    qtechPimIpMRouteNextHopTable.setStatus("current")
_QtechPimIpMRouteNextHopEntry_Object = MibTableRow
qtechPimIpMRouteNextHopEntry = _QtechPimIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 5, 1)
)
qtechPimIpMRouteNextHopEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    qtechPimIpMRouteNextHopEntry.setStatus("current")


class _QtechPimIpMRouteNextHopPruneReason_Type(Integer32):
    """Custom type qtechPimIpMRouteNextHopPruneReason based on Integer32"""
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


_QtechPimIpMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_QtechPimIpMRouteNextHopPruneReason_Object = MibTableColumn
qtechPimIpMRouteNextHopPruneReason = _QtechPimIpMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 5, 1, 1),
    _QtechPimIpMRouteNextHopPruneReason_Type()
)
qtechPimIpMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteNextHopPruneReason.setStatus("current")
_QtechPimIpMRouteNextHopAssertWinner_Type = IpAddress
_QtechPimIpMRouteNextHopAssertWinner_Object = MibTableColumn
qtechPimIpMRouteNextHopAssertWinner = _QtechPimIpMRouteNextHopAssertWinner_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 5, 1, 2),
    _QtechPimIpMRouteNextHopAssertWinner_Type()
)
qtechPimIpMRouteNextHopAssertWinner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteNextHopAssertWinner.setStatus("current")
_QtechPimIpMRouteNextHopAssertTimer_Type = TimeTicks
_QtechPimIpMRouteNextHopAssertTimer_Object = MibTableColumn
qtechPimIpMRouteNextHopAssertTimer = _QtechPimIpMRouteNextHopAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 5, 1, 3),
    _QtechPimIpMRouteNextHopAssertTimer_Type()
)
qtechPimIpMRouteNextHopAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteNextHopAssertTimer.setStatus("current")
_QtechPimIpMRouteNextHopAssertMetric_Type = Integer32
_QtechPimIpMRouteNextHopAssertMetric_Object = MibTableColumn
qtechPimIpMRouteNextHopAssertMetric = _QtechPimIpMRouteNextHopAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 5, 1, 4),
    _QtechPimIpMRouteNextHopAssertMetric_Type()
)
qtechPimIpMRouteNextHopAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteNextHopAssertMetric.setStatus("current")
_QtechPimIpMRouteNextHopAssertMetricPref_Type = Integer32
_QtechPimIpMRouteNextHopAssertMetricPref_Object = MibTableColumn
qtechPimIpMRouteNextHopAssertMetricPref = _QtechPimIpMRouteNextHopAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 5, 1, 5),
    _QtechPimIpMRouteNextHopAssertMetricPref_Type()
)
qtechPimIpMRouteNextHopAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteNextHopAssertMetricPref.setStatus("current")
_QtechPimIpMRouteNextHopJoinPruneTimer_Type = TimeTicks
_QtechPimIpMRouteNextHopJoinPruneTimer_Object = MibTableColumn
qtechPimIpMRouteNextHopJoinPruneTimer = _QtechPimIpMRouteNextHopJoinPruneTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 5, 1, 6),
    _QtechPimIpMRouteNextHopJoinPruneTimer_Type()
)
qtechPimIpMRouteNextHopJoinPruneTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimIpMRouteNextHopJoinPruneTimer.setStatus("current")
_QtechPimRPSetTable_Object = MibTable
qtechPimRPSetTable = _QtechPimRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 6)
)
if mibBuilder.loadTexts:
    qtechPimRPSetTable.setStatus("current")
_QtechPimRPSetEntry_Object = MibTableRow
qtechPimRPSetEntry = _QtechPimRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 6, 1)
)
qtechPimRPSetEntry.setIndexNames(
    (0, "QTECH-PIM-MIB", "qtechPimRPSetComponent"),
    (0, "QTECH-PIM-MIB", "qtechPimRPSetGroupAddress"),
    (0, "QTECH-PIM-MIB", "qtechPimRPSetGroupMask"),
    (0, "QTECH-PIM-MIB", "qtechPimRPSetAddress"),
)
if mibBuilder.loadTexts:
    qtechPimRPSetEntry.setStatus("current")
_QtechPimRPSetGroupAddress_Type = IpAddress
_QtechPimRPSetGroupAddress_Object = MibTableColumn
qtechPimRPSetGroupAddress = _QtechPimRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 6, 1, 1),
    _QtechPimRPSetGroupAddress_Type()
)
qtechPimRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimRPSetGroupAddress.setStatus("current")
_QtechPimRPSetGroupMask_Type = IpAddress
_QtechPimRPSetGroupMask_Object = MibTableColumn
qtechPimRPSetGroupMask = _QtechPimRPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 6, 1, 2),
    _QtechPimRPSetGroupMask_Type()
)
qtechPimRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimRPSetGroupMask.setStatus("current")
_QtechPimRPSetAddress_Type = IpAddress
_QtechPimRPSetAddress_Object = MibTableColumn
qtechPimRPSetAddress = _QtechPimRPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 6, 1, 3),
    _QtechPimRPSetAddress_Type()
)
qtechPimRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimRPSetAddress.setStatus("current")


class _QtechPimRPSetHoldTime_Type(Integer32):
    """Custom type qtechPimRPSetHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechPimRPSetHoldTime_Type.__name__ = "Integer32"
_QtechPimRPSetHoldTime_Object = MibTableColumn
qtechPimRPSetHoldTime = _QtechPimRPSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 6, 1, 4),
    _QtechPimRPSetHoldTime_Type()
)
qtechPimRPSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimRPSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimRPSetHoldTime.setUnits("seconds")
_QtechPimRPSetExpiryTime_Type = TimeTicks
_QtechPimRPSetExpiryTime_Object = MibTableColumn
qtechPimRPSetExpiryTime = _QtechPimRPSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 6, 1, 5),
    _QtechPimRPSetExpiryTime_Type()
)
qtechPimRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimRPSetExpiryTime.setStatus("current")


class _QtechPimRPSetComponent_Type(Integer32):
    """Custom type qtechPimRPSetComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechPimRPSetComponent_Type.__name__ = "Integer32"
_QtechPimRPSetComponent_Object = MibTableColumn
qtechPimRPSetComponent = _QtechPimRPSetComponent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 6, 1, 6),
    _QtechPimRPSetComponent_Type()
)
qtechPimRPSetComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimRPSetComponent.setStatus("current")
_QtechPimRPSetUpTime_Type = TimeTicks
_QtechPimRPSetUpTime_Object = MibTableColumn
qtechPimRPSetUpTime = _QtechPimRPSetUpTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 6, 1, 7),
    _QtechPimRPSetUpTime_Type()
)
qtechPimRPSetUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimRPSetUpTime.setStatus("current")
_QtechPimComponentTable_Object = MibTable
qtechPimComponentTable = _QtechPimComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7)
)
if mibBuilder.loadTexts:
    qtechPimComponentTable.setStatus("current")
_QtechPimComponentEntry_Object = MibTableRow
qtechPimComponentEntry = _QtechPimComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1)
)
qtechPimComponentEntry.setIndexNames(
    (0, "QTECH-PIM-MIB", "qtechPimComponentIndex"),
)
if mibBuilder.loadTexts:
    qtechPimComponentEntry.setStatus("current")


class _QtechPimComponentIndex_Type(Integer32):
    """Custom type qtechPimComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechPimComponentIndex_Type.__name__ = "Integer32"
_QtechPimComponentIndex_Object = MibTableColumn
qtechPimComponentIndex = _QtechPimComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1, 1),
    _QtechPimComponentIndex_Type()
)
qtechPimComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimComponentIndex.setStatus("current")
_QtechPimComponentBSRAddress_Type = IpAddress
_QtechPimComponentBSRAddress_Object = MibTableColumn
qtechPimComponentBSRAddress = _QtechPimComponentBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1, 2),
    _QtechPimComponentBSRAddress_Type()
)
qtechPimComponentBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimComponentBSRAddress.setStatus("current")
_QtechPimComponentBSRExpiryTime_Type = TimeTicks
_QtechPimComponentBSRExpiryTime_Object = MibTableColumn
qtechPimComponentBSRExpiryTime = _QtechPimComponentBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1, 3),
    _QtechPimComponentBSRExpiryTime_Type()
)
qtechPimComponentBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimComponentBSRExpiryTime.setStatus("current")


class _QtechPimComponentCRPHoldTime_Type(Integer32):
    """Custom type qtechPimComponentCRPHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechPimComponentCRPHoldTime_Type.__name__ = "Integer32"
_QtechPimComponentCRPHoldTime_Object = MibTableColumn
qtechPimComponentCRPHoldTime = _QtechPimComponentCRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1, 4),
    _QtechPimComponentCRPHoldTime_Type()
)
qtechPimComponentCRPHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPimComponentCRPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimComponentCRPHoldTime.setUnits("seconds")
_QtechPimComponentBSRUptime_Type = TimeTicks
_QtechPimComponentBSRUptime_Object = MibTableColumn
qtechPimComponentBSRUptime = _QtechPimComponentBSRUptime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1, 5),
    _QtechPimComponentBSRUptime_Type()
)
qtechPimComponentBSRUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimComponentBSRUptime.setStatus("current")
_QtechPimComponentBSRPriority_Type = Integer32
_QtechPimComponentBSRPriority_Object = MibTableColumn
qtechPimComponentBSRPriority = _QtechPimComponentBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1, 6),
    _QtechPimComponentBSRPriority_Type()
)
qtechPimComponentBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimComponentBSRPriority.setStatus("current")
_QtechPimComponentBSRHashMaskLength_Type = Integer32
_QtechPimComponentBSRHashMaskLength_Object = MibTableColumn
qtechPimComponentBSRHashMaskLength = _QtechPimComponentBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1, 7),
    _QtechPimComponentBSRHashMaskLength_Type()
)
qtechPimComponentBSRHashMaskLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimComponentBSRHashMaskLength.setStatus("current")
_QtechPimComponentBSRNextBsrMessage_Type = TimeTicks
_QtechPimComponentBSRNextBsrMessage_Object = MibTableColumn
qtechPimComponentBSRNextBsrMessage = _QtechPimComponentBSRNextBsrMessage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1, 8),
    _QtechPimComponentBSRNextBsrMessage_Type()
)
qtechPimComponentBSRNextBsrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimComponentBSRNextBsrMessage.setStatus("current")
_QtechPimComponentNextCandRPAdv_Type = TimeTicks
_QtechPimComponentNextCandRPAdv_Object = MibTableColumn
qtechPimComponentNextCandRPAdv = _QtechPimComponentNextCandRPAdv_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 7, 1, 9),
    _QtechPimComponentNextCandRPAdv_Type()
)
qtechPimComponentNextCandRPAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimComponentNextCandRPAdv.setStatus("current")


class _QtechPimSourceLifetime_Type(Integer32):
    """Custom type qtechPimSourceLifetime based on Integer32"""
    defaultValue = 2100


_QtechPimSourceLifetime_Type.__name__ = "Integer32"
_QtechPimSourceLifetime_Object = MibScalar
qtechPimSourceLifetime = _QtechPimSourceLifetime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 8),
    _QtechPimSourceLifetime_Type()
)
qtechPimSourceLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimSourceLifetime.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimSourceLifetime.setUnits("seconds")


class _QtechPimStateRefreshInterval_Type(Integer32):
    """Custom type qtechPimStateRefreshInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechPimStateRefreshInterval_Type.__name__ = "Integer32"
_QtechPimStateRefreshInterval_Object = MibScalar
qtechPimStateRefreshInterval = _QtechPimStateRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 9),
    _QtechPimStateRefreshInterval_Type()
)
qtechPimStateRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimStateRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechPimStateRefreshInterval.setUnits("seconds")


class _QtechPimStateRefreshLimitInterval_Type(Integer32):
    """Custom type qtechPimStateRefreshLimitInterval based on Integer32"""
    defaultValue = 0


_QtechPimStateRefreshLimitInterval_Type.__name__ = "Integer32"
_QtechPimStateRefreshLimitInterval_Object = MibScalar
qtechPimStateRefreshLimitInterval = _QtechPimStateRefreshLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 10),
    _QtechPimStateRefreshLimitInterval_Type()
)
qtechPimStateRefreshLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimStateRefreshLimitInterval.setStatus("current")


class _QtechPimStateRefreshTimeToLive_Type(Integer32):
    """Custom type qtechPimStateRefreshTimeToLive based on Integer32"""
    defaultValue = 16


_QtechPimStateRefreshTimeToLive_Type.__name__ = "Integer32"
_QtechPimStateRefreshTimeToLive_Object = MibScalar
qtechPimStateRefreshTimeToLive = _QtechPimStateRefreshTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 11),
    _QtechPimStateRefreshTimeToLive_Type()
)
qtechPimStateRefreshTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimStateRefreshTimeToLive.setStatus("current")
_QtechPimBsrCandidateGroup_ObjectIdentity = ObjectIdentity
qtechPimBsrCandidateGroup = _QtechPimBsrCandidateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 12)
)
_QtechPimBsrCandidateIfindex_Type = Integer32
_QtechPimBsrCandidateIfindex_Object = MibScalar
qtechPimBsrCandidateIfindex = _QtechPimBsrCandidateIfindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 12, 1),
    _QtechPimBsrCandidateIfindex_Type()
)
qtechPimBsrCandidateIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimBsrCandidateIfindex.setStatus("current")


class _QtechPimBsrCandidateHashMaskLength_Type(Integer32):
    """Custom type qtechPimBsrCandidateHashMaskLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_QtechPimBsrCandidateHashMaskLength_Type.__name__ = "Integer32"
_QtechPimBsrCandidateHashMaskLength_Object = MibScalar
qtechPimBsrCandidateHashMaskLength = _QtechPimBsrCandidateHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 12, 2),
    _QtechPimBsrCandidateHashMaskLength_Type()
)
qtechPimBsrCandidateHashMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimBsrCandidateHashMaskLength.setStatus("current")


class _QtechPimBsrCandidatePriority_Type(Integer32):
    """Custom type qtechPimBsrCandidatePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechPimBsrCandidatePriority_Type.__name__ = "Integer32"
_QtechPimBsrCandidatePriority_Object = MibScalar
qtechPimBsrCandidatePriority = _QtechPimBsrCandidatePriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 12, 3),
    _QtechPimBsrCandidatePriority_Type()
)
qtechPimBsrCandidatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPimBsrCandidatePriority.setStatus("current")
_QtechPimRPTable_Object = MibTable
qtechPimRPTable = _QtechPimRPTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 13)
)
if mibBuilder.loadTexts:
    qtechPimRPTable.setStatus("current")
_QtechPimRPEntry_Object = MibTableRow
qtechPimRPEntry = _QtechPimRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 13, 1)
)
qtechPimRPEntry.setIndexNames(
    (0, "QTECH-PIM-MIB", "qtechPimRPGroupAddress"),
)
if mibBuilder.loadTexts:
    qtechPimRPEntry.setStatus("current")
_QtechPimRPGroupAddress_Type = IpAddress
_QtechPimRPGroupAddress_Object = MibTableColumn
qtechPimRPGroupAddress = _QtechPimRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 13, 1, 1),
    _QtechPimRPGroupAddress_Type()
)
qtechPimRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimRPGroupAddress.setStatus("current")
_QtechPimRPAddress_Type = IpAddress
_QtechPimRPAddress_Object = MibTableColumn
qtechPimRPAddress = _QtechPimRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 13, 1, 2),
    _QtechPimRPAddress_Type()
)
qtechPimRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimRPAddress.setStatus("current")
_QtechPimRPExpiryTime_Type = TimeTicks
_QtechPimRPExpiryTime_Object = MibTableColumn
qtechPimRPExpiryTime = _QtechPimRPExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 13, 1, 3),
    _QtechPimRPExpiryTime_Type()
)
qtechPimRPExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimRPExpiryTime.setStatus("current")
_QtechPimRPNextRPReachableIn_Type = TimeTicks
_QtechPimRPNextRPReachableIn_Object = MibTableColumn
qtechPimRPNextRPReachableIn = _QtechPimRPNextRPReachableIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 13, 1, 4),
    _QtechPimRPNextRPReachableIn_Type()
)
qtechPimRPNextRPReachableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPimRPNextRPReachableIn.setStatus("current")
_QtechPimStaticRPTable_Object = MibTable
qtechPimStaticRPTable = _QtechPimStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 14)
)
if mibBuilder.loadTexts:
    qtechPimStaticRPTable.setStatus("current")
_QtechPimStaticRPEntry_Object = MibTableRow
qtechPimStaticRPEntry = _QtechPimStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 14, 1)
)
qtechPimStaticRPEntry.setIndexNames(
    (0, "QTECH-PIM-MIB", "qtechPimStaticRPAddress"),
)
if mibBuilder.loadTexts:
    qtechPimStaticRPEntry.setStatus("current")
_QtechPimStaticRPAddress_Type = IpAddress
_QtechPimStaticRPAddress_Object = MibTableColumn
qtechPimStaticRPAddress = _QtechPimStaticRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 14, 1, 1),
    _QtechPimStaticRPAddress_Type()
)
qtechPimStaticRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimStaticRPAddress.setStatus("current")


class _QtechPimStaticRPAddressIsOverride_Type(EnabledStatus):
    """Custom type qtechPimStaticRPAddressIsOverride based on EnabledStatus"""
    defaultValue = 2


_QtechPimStaticRPAddressIsOverride_Type.__name__ = "EnabledStatus"
_QtechPimStaticRPAddressIsOverride_Object = MibTableColumn
qtechPimStaticRPAddressIsOverride = _QtechPimStaticRPAddressIsOverride_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 14, 1, 2),
    _QtechPimStaticRPAddressIsOverride_Type()
)
qtechPimStaticRPAddressIsOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPimStaticRPAddressIsOverride.setStatus("current")


class _QtechPimStaticRPAclName_Type(DisplayString):
    """Custom type qtechPimStaticRPAclName based on DisplayString"""
    defaultValue = OctetString("")


_QtechPimStaticRPAclName_Type.__name__ = "DisplayString"
_QtechPimStaticRPAclName_Object = MibTableColumn
qtechPimStaticRPAclName = _QtechPimStaticRPAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 14, 1, 3),
    _QtechPimStaticRPAclName_Type()
)
qtechPimStaticRPAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPimStaticRPAclName.setStatus("current")
_QtechPimStaticRPStatus_Type = RowStatus
_QtechPimStaticRPStatus_Object = MibTableColumn
qtechPimStaticRPStatus = _QtechPimStaticRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 14, 1, 4),
    _QtechPimStaticRPStatus_Type()
)
qtechPimStaticRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPimStaticRPStatus.setStatus("current")
_QtechPimRpCandidateTable_Object = MibTable
qtechPimRpCandidateTable = _QtechPimRpCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 15)
)
if mibBuilder.loadTexts:
    qtechPimRpCandidateTable.setStatus("current")
_QtechPimRpCandidateEntry_Object = MibTableRow
qtechPimRpCandidateEntry = _QtechPimRpCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 15, 1)
)
qtechPimRpCandidateEntry.setIndexNames(
    (0, "QTECH-PIM-MIB", "qtechPimRpCandidateIfindex"),
)
if mibBuilder.loadTexts:
    qtechPimRpCandidateEntry.setStatus("current")
_QtechPimRpCandidateIfindex_Type = InterfaceIndex
_QtechPimRpCandidateIfindex_Object = MibTableColumn
qtechPimRpCandidateIfindex = _QtechPimRpCandidateIfindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 15, 1, 1),
    _QtechPimRpCandidateIfindex_Type()
)
qtechPimRpCandidateIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechPimRpCandidateIfindex.setStatus("current")


class _QtechPimRpCandidateAclName_Type(DisplayString):
    """Custom type qtechPimRpCandidateAclName based on DisplayString"""
    defaultValue = OctetString("")


_QtechPimRpCandidateAclName_Type.__name__ = "DisplayString"
_QtechPimRpCandidateAclName_Object = MibTableColumn
qtechPimRpCandidateAclName = _QtechPimRpCandidateAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 15, 1, 2),
    _QtechPimRpCandidateAclName_Type()
)
qtechPimRpCandidateAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPimRpCandidateAclName.setStatus("current")
_QtechPimRpCandidateStatus_Type = RowStatus
_QtechPimRpCandidateStatus_Object = MibTableColumn
qtechPimRpCandidateStatus = _QtechPimRpCandidateStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 1, 15, 1, 3),
    _QtechPimRpCandidateStatus_Type()
)
qtechPimRpCandidateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPimRpCandidateStatus.setStatus("current")
_QtechPimTraps_ObjectIdentity = ObjectIdentity
qtechPimTraps = _QtechPimTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 2)
)
_QtechPimMIBConformance_ObjectIdentity = ObjectIdentity
qtechPimMIBConformance = _QtechPimMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 2)
)
_QtechPimMIBCompliances_ObjectIdentity = ObjectIdentity
qtechPimMIBCompliances = _QtechPimMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 2, 1)
)
_QtechPimMIBGroups_ObjectIdentity = ObjectIdentity
qtechPimMIBGroups = _QtechPimMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 2, 2)
)

# Managed Objects groups

qtechPimMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 2, 2, 1)
)
qtechPimMIBGroup.setObjects(
      *(("QTECH-PIM-MIB", "qtechPimJoinPruneInterval"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceAddress"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceNetMask"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceMode"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceDR"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceHelloInterval"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceJoinPruneInterval"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceCBSRPreference"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceTrigHelloInterval"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceHelloHoldtime"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceLanPruneDelay"),
        ("QTECH-PIM-MIB", "qtechPimInterfacePropagationDelay"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceOverrideInterval"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceGenerationID"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceJoinPruneHoldtime"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceGraftRetryInterval"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceMaxGraftRetries"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceSRTTLThreshold"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceLanDelayEnabled"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceSRCapable"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceDRPriority"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceNbrCounter"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceBsrBorderEnabled"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceCountIn"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceCountOut"),
        ("QTECH-PIM-MIB", "qtechPimInterfaceEnabled"),
        ("QTECH-PIM-MIB", "qtechPimNeighborFilterAcl"),
        ("QTECH-PIM-MIB", "qtechPimDrSupportAddressBound"),
        ("QTECH-PIM-MIB", "qtechPimNeighborIfIndex"),
        ("QTECH-PIM-MIB", "qtechPimNeighborUpTime"),
        ("QTECH-PIM-MIB", "qtechPimNeighborExpiryTime"),
        ("QTECH-PIM-MIB", "qtechPimNeighborMode"),
        ("QTECH-PIM-MIB", "qtechPimNeighborLanPruneDelay"),
        ("QTECH-PIM-MIB", "qtechPimNeighborOverrideInterval"),
        ("QTECH-PIM-MIB", "qtechPimNeighborTBit"),
        ("QTECH-PIM-MIB", "qtechPimNeighborSRCapable"),
        ("QTECH-PIM-MIB", "qtechPimNeighborDRPresent"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteUpstreamAssertTimer"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteAssertMetric"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteAssertMetricPref"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteAssertRPTBit"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteFlags"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteRPFNeighbor"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteSourceTimer"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteOriginatorSRTTL"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteNextHopPruneReason"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteNextHopAssertWinner"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteNextHopAssertTimer"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteNextHopAssertMetric"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteNextHopAssertMetricPref"),
        ("QTECH-PIM-MIB", "qtechPimIpMRouteNextHopJoinPruneTimer"),
        ("QTECH-PIM-MIB", "qtechPimRPSetHoldTime"),
        ("QTECH-PIM-MIB", "qtechPimRPSetExpiryTime"),
        ("QTECH-PIM-MIB", "qtechPimRPSetUpTime"),
        ("QTECH-PIM-MIB", "qtechPimComponentBSRAddress"),
        ("QTECH-PIM-MIB", "qtechPimComponentBSRExpiryTime"),
        ("QTECH-PIM-MIB", "qtechPimComponentCRPHoldTime"),
        ("QTECH-PIM-MIB", "qtechPimComponentBSRUptime"),
        ("QTECH-PIM-MIB", "qtechPimComponentBSRPriority"),
        ("QTECH-PIM-MIB", "qtechPimComponentBSRHashMaskLength"),
        ("QTECH-PIM-MIB", "qtechPimComponentBSRNextBsrMessage"),
        ("QTECH-PIM-MIB", "qtechPimComponentNextCandRPAdv"),
        ("QTECH-PIM-MIB", "qtechPimSourceLifetime"),
        ("QTECH-PIM-MIB", "qtechPimStateRefreshInterval"),
        ("QTECH-PIM-MIB", "qtechPimStateRefreshLimitInterval"),
        ("QTECH-PIM-MIB", "qtechPimStateRefreshTimeToLive"),
        ("QTECH-PIM-MIB", "qtechPimBsrCandidateIfindex"),
        ("QTECH-PIM-MIB", "qtechPimBsrCandidateHashMaskLength"),
        ("QTECH-PIM-MIB", "qtechPimBsrCandidatePriority"),
        ("QTECH-PIM-MIB", "qtechPimRPAddress"),
        ("QTECH-PIM-MIB", "qtechPimRPExpiryTime"),
        ("QTECH-PIM-MIB", "qtechPimRPNextRPReachableIn"),
        ("QTECH-PIM-MIB", "qtechPimStaticRPAddressIsOverride"),
        ("QTECH-PIM-MIB", "qtechPimStaticRPAclName"),
        ("QTECH-PIM-MIB", "qtechPimStaticRPStatus"),
        ("QTECH-PIM-MIB", "qtechPimRpCandidateAclName"),
        ("QTECH-PIM-MIB", "qtechPimRpCandidateStatus"))
)
if mibBuilder.loadTexts:
    qtechPimMIBGroup.setStatus("current")


# Notification objects

qtechPimNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 1, 2, 1)
)
qtechPimNeighborLoss.setObjects(
    ("QTECH-PIM-MIB", "qtechPimNeighborIfIndex")
)
if mibBuilder.loadTexts:
    qtechPimNeighborLoss.setStatus(
        "current"
    )


# Notifications groups

qtechPimNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 2, 2, 2)
)
qtechPimNotifyGroup.setObjects(
    ("QTECH-PIM-MIB", "qtechPimNeighborLoss")
)
if mibBuilder.loadTexts:
    qtechPimNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechPimMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 27, 2, 1, 1)
)
qtechPimMIBCompliance.setObjects(
    ("QTECH-PIM-MIB", "qtechPimMIBGroup")
)
if mibBuilder.loadTexts:
    qtechPimMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-PIM-MIB",
    **{"qtechPimMIB": qtechPimMIB,
       "qtechPimMIBObjects": qtechPimMIBObjects,
       "qtechPim": qtechPim,
       "qtechPimJoinPruneInterval": qtechPimJoinPruneInterval,
       "qtechPimInterfaceTable": qtechPimInterfaceTable,
       "qtechPimInterfaceEntry": qtechPimInterfaceEntry,
       "qtechPimInterfaceIfIndex": qtechPimInterfaceIfIndex,
       "qtechPimInterfaceAddress": qtechPimInterfaceAddress,
       "qtechPimInterfaceNetMask": qtechPimInterfaceNetMask,
       "qtechPimInterfaceMode": qtechPimInterfaceMode,
       "qtechPimInterfaceDR": qtechPimInterfaceDR,
       "qtechPimInterfaceHelloInterval": qtechPimInterfaceHelloInterval,
       "qtechPimInterfaceJoinPruneInterval": qtechPimInterfaceJoinPruneInterval,
       "qtechPimInterfaceCBSRPreference": qtechPimInterfaceCBSRPreference,
       "qtechPimInterfaceTrigHelloInterval": qtechPimInterfaceTrigHelloInterval,
       "qtechPimInterfaceHelloHoldtime": qtechPimInterfaceHelloHoldtime,
       "qtechPimInterfaceLanPruneDelay": qtechPimInterfaceLanPruneDelay,
       "qtechPimInterfacePropagationDelay": qtechPimInterfacePropagationDelay,
       "qtechPimInterfaceOverrideInterval": qtechPimInterfaceOverrideInterval,
       "qtechPimInterfaceGenerationID": qtechPimInterfaceGenerationID,
       "qtechPimInterfaceJoinPruneHoldtime": qtechPimInterfaceJoinPruneHoldtime,
       "qtechPimInterfaceGraftRetryInterval": qtechPimInterfaceGraftRetryInterval,
       "qtechPimInterfaceMaxGraftRetries": qtechPimInterfaceMaxGraftRetries,
       "qtechPimInterfaceSRTTLThreshold": qtechPimInterfaceSRTTLThreshold,
       "qtechPimInterfaceLanDelayEnabled": qtechPimInterfaceLanDelayEnabled,
       "qtechPimInterfaceSRCapable": qtechPimInterfaceSRCapable,
       "qtechPimInterfaceDRPriority": qtechPimInterfaceDRPriority,
       "qtechPimInterfaceNbrCounter": qtechPimInterfaceNbrCounter,
       "qtechPimInterfaceBsrBorderEnabled": qtechPimInterfaceBsrBorderEnabled,
       "qtechPimInterfaceCountIn": qtechPimInterfaceCountIn,
       "qtechPimInterfaceCountOut": qtechPimInterfaceCountOut,
       "qtechPimInterfaceEnabled": qtechPimInterfaceEnabled,
       "qtechPimNeighborFilterAcl": qtechPimNeighborFilterAcl,
       "qtechPimDrSupportAddressBound": qtechPimDrSupportAddressBound,
       "qtechPimNeighborTable": qtechPimNeighborTable,
       "qtechPimNeighborEntry": qtechPimNeighborEntry,
       "qtechPimNeighborAddress": qtechPimNeighborAddress,
       "qtechPimNeighborIfIndex": qtechPimNeighborIfIndex,
       "qtechPimNeighborUpTime": qtechPimNeighborUpTime,
       "qtechPimNeighborExpiryTime": qtechPimNeighborExpiryTime,
       "qtechPimNeighborMode": qtechPimNeighborMode,
       "qtechPimNeighborLanPruneDelay": qtechPimNeighborLanPruneDelay,
       "qtechPimNeighborOverrideInterval": qtechPimNeighborOverrideInterval,
       "qtechPimNeighborTBit": qtechPimNeighborTBit,
       "qtechPimNeighborSRCapable": qtechPimNeighborSRCapable,
       "qtechPimNeighborDRPresent": qtechPimNeighborDRPresent,
       "qtechPimIpMRouteTable": qtechPimIpMRouteTable,
       "qtechPimIpMRouteEntry": qtechPimIpMRouteEntry,
       "qtechPimIpMRouteUpstreamAssertTimer": qtechPimIpMRouteUpstreamAssertTimer,
       "qtechPimIpMRouteAssertMetric": qtechPimIpMRouteAssertMetric,
       "qtechPimIpMRouteAssertMetricPref": qtechPimIpMRouteAssertMetricPref,
       "qtechPimIpMRouteAssertRPTBit": qtechPimIpMRouteAssertRPTBit,
       "qtechPimIpMRouteFlags": qtechPimIpMRouteFlags,
       "qtechPimIpMRouteRPFNeighbor": qtechPimIpMRouteRPFNeighbor,
       "qtechPimIpMRouteSourceTimer": qtechPimIpMRouteSourceTimer,
       "qtechPimIpMRouteOriginatorSRTTL": qtechPimIpMRouteOriginatorSRTTL,
       "qtechPimIpMRouteNextHopTable": qtechPimIpMRouteNextHopTable,
       "qtechPimIpMRouteNextHopEntry": qtechPimIpMRouteNextHopEntry,
       "qtechPimIpMRouteNextHopPruneReason": qtechPimIpMRouteNextHopPruneReason,
       "qtechPimIpMRouteNextHopAssertWinner": qtechPimIpMRouteNextHopAssertWinner,
       "qtechPimIpMRouteNextHopAssertTimer": qtechPimIpMRouteNextHopAssertTimer,
       "qtechPimIpMRouteNextHopAssertMetric": qtechPimIpMRouteNextHopAssertMetric,
       "qtechPimIpMRouteNextHopAssertMetricPref": qtechPimIpMRouteNextHopAssertMetricPref,
       "qtechPimIpMRouteNextHopJoinPruneTimer": qtechPimIpMRouteNextHopJoinPruneTimer,
       "qtechPimRPSetTable": qtechPimRPSetTable,
       "qtechPimRPSetEntry": qtechPimRPSetEntry,
       "qtechPimRPSetGroupAddress": qtechPimRPSetGroupAddress,
       "qtechPimRPSetGroupMask": qtechPimRPSetGroupMask,
       "qtechPimRPSetAddress": qtechPimRPSetAddress,
       "qtechPimRPSetHoldTime": qtechPimRPSetHoldTime,
       "qtechPimRPSetExpiryTime": qtechPimRPSetExpiryTime,
       "qtechPimRPSetComponent": qtechPimRPSetComponent,
       "qtechPimRPSetUpTime": qtechPimRPSetUpTime,
       "qtechPimComponentTable": qtechPimComponentTable,
       "qtechPimComponentEntry": qtechPimComponentEntry,
       "qtechPimComponentIndex": qtechPimComponentIndex,
       "qtechPimComponentBSRAddress": qtechPimComponentBSRAddress,
       "qtechPimComponentBSRExpiryTime": qtechPimComponentBSRExpiryTime,
       "qtechPimComponentCRPHoldTime": qtechPimComponentCRPHoldTime,
       "qtechPimComponentBSRUptime": qtechPimComponentBSRUptime,
       "qtechPimComponentBSRPriority": qtechPimComponentBSRPriority,
       "qtechPimComponentBSRHashMaskLength": qtechPimComponentBSRHashMaskLength,
       "qtechPimComponentBSRNextBsrMessage": qtechPimComponentBSRNextBsrMessage,
       "qtechPimComponentNextCandRPAdv": qtechPimComponentNextCandRPAdv,
       "qtechPimSourceLifetime": qtechPimSourceLifetime,
       "qtechPimStateRefreshInterval": qtechPimStateRefreshInterval,
       "qtechPimStateRefreshLimitInterval": qtechPimStateRefreshLimitInterval,
       "qtechPimStateRefreshTimeToLive": qtechPimStateRefreshTimeToLive,
       "qtechPimBsrCandidateGroup": qtechPimBsrCandidateGroup,
       "qtechPimBsrCandidateIfindex": qtechPimBsrCandidateIfindex,
       "qtechPimBsrCandidateHashMaskLength": qtechPimBsrCandidateHashMaskLength,
       "qtechPimBsrCandidatePriority": qtechPimBsrCandidatePriority,
       "qtechPimRPTable": qtechPimRPTable,
       "qtechPimRPEntry": qtechPimRPEntry,
       "qtechPimRPGroupAddress": qtechPimRPGroupAddress,
       "qtechPimRPAddress": qtechPimRPAddress,
       "qtechPimRPExpiryTime": qtechPimRPExpiryTime,
       "qtechPimRPNextRPReachableIn": qtechPimRPNextRPReachableIn,
       "qtechPimStaticRPTable": qtechPimStaticRPTable,
       "qtechPimStaticRPEntry": qtechPimStaticRPEntry,
       "qtechPimStaticRPAddress": qtechPimStaticRPAddress,
       "qtechPimStaticRPAddressIsOverride": qtechPimStaticRPAddressIsOverride,
       "qtechPimStaticRPAclName": qtechPimStaticRPAclName,
       "qtechPimStaticRPStatus": qtechPimStaticRPStatus,
       "qtechPimRpCandidateTable": qtechPimRpCandidateTable,
       "qtechPimRpCandidateEntry": qtechPimRpCandidateEntry,
       "qtechPimRpCandidateIfindex": qtechPimRpCandidateIfindex,
       "qtechPimRpCandidateAclName": qtechPimRpCandidateAclName,
       "qtechPimRpCandidateStatus": qtechPimRpCandidateStatus,
       "qtechPimTraps": qtechPimTraps,
       "qtechPimNeighborLoss": qtechPimNeighborLoss,
       "qtechPimMIBConformance": qtechPimMIBConformance,
       "qtechPimMIBCompliances": qtechPimMIBCompliances,
       "qtechPimMIBCompliance": qtechPimMIBCompliance,
       "qtechPimMIBGroups": qtechPimMIBGroups,
       "qtechPimMIBGroup": qtechPimMIBGroup,
       "qtechPimNotifyGroup": qtechPimNotifyGroup}
)
