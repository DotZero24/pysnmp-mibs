# SNMP MIB module (FS-RRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-RRM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:10 2025
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

fsRrmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63)
)
if mibBuilder.loadTexts:
    fsRrmMIB.setRevisions(
        ("2009-12-15 00:00",)
    )


# Types definitions



class ProfileState(Integer32):
    """Custom type ProfileState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("pass", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsRrmMIBObjects_ObjectIdentity = ObjectIdentity
fsRrmMIBObjects = _FsRrmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1)
)
_FsRrmObjectsGroup_ObjectIdentity = ObjectIdentity
fsRrmObjectsGroup = _FsRrmObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 1)
)


class _FsRrmRFNetworkName_Type(DisplayString):
    """Custom type fsRrmRFNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_FsRrmRFNetworkName_Type.__name__ = "DisplayString"
_FsRrmRFNetworkName_Object = MibScalar
fsRrmRFNetworkName = _FsRrmRFNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 1, 1),
    _FsRrmRFNetworkName_Type()
)
fsRrmRFNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmRFNetworkName.setStatus("current")
_FsRrmObjectsDot11a_ObjectIdentity = ObjectIdentity
fsRrmObjectsDot11a = _FsRrmObjectsDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2)
)
_FsRrmDCADot11a_ObjectIdentity = ObjectIdentity
fsRrmDCADot11a = _FsRrmDCADot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1)
)


class _FsRrmDot11aDynamicChannelAssignment_Type(Integer32):
    """Custom type fsRrmDot11aDynamicChannelAssignment based on Integer32"""
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
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_FsRrmDot11aDynamicChannelAssignment_Type.__name__ = "Integer32"
_FsRrmDot11aDynamicChannelAssignment_Object = MibScalar
fsRrmDot11aDynamicChannelAssignment = _FsRrmDot11aDynamicChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 1),
    _FsRrmDot11aDynamicChannelAssignment_Type()
)
fsRrmDot11aDynamicChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aDynamicChannelAssignment.setStatus("current")


class _FsRrmDot11aAnchorTime_Type(Unsigned32):
    """Custom type fsRrmDot11aAnchorTime based on Unsigned32"""
    defaultValue = 0


_FsRrmDot11aAnchorTime_Type.__name__ = "Unsigned32"
_FsRrmDot11aAnchorTime_Object = MibScalar
fsRrmDot11aAnchorTime = _FsRrmDot11aAnchorTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 2),
    _FsRrmDot11aAnchorTime_Type()
)
fsRrmDot11aAnchorTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aAnchorTime.setStatus("current")


class _FsRrmDot11aChannalWidth11n_Type(Unsigned32):
    """Custom type fsRrmDot11aChannalWidth11n based on Unsigned32"""
    defaultValue = 20


_FsRrmDot11aChannalWidth11n_Type.__name__ = "Unsigned32"
_FsRrmDot11aChannalWidth11n_Object = MibScalar
fsRrmDot11aChannalWidth11n = _FsRrmDot11aChannalWidth11n_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 3),
    _FsRrmDot11aChannalWidth11n_Type()
)
fsRrmDot11aChannalWidth11n.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aChannalWidth11n.setStatus("current")


class _FsRrmDot11aDynamicChannelUpdateInterval_Type(Unsigned32):
    """Custom type fsRrmDot11aDynamicChannelUpdateInterval based on Unsigned32"""
    defaultValue = 600


_FsRrmDot11aDynamicChannelUpdateInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11aDynamicChannelUpdateInterval_Object = MibScalar
fsRrmDot11aDynamicChannelUpdateInterval = _FsRrmDot11aDynamicChannelUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 4),
    _FsRrmDot11aDynamicChannelUpdateInterval_Type()
)
fsRrmDot11aDynamicChannelUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aDynamicChannelUpdateInterval.setStatus("current")


class _FsRrmDot11aDCASensitivity_Type(Integer32):
    """Custom type fsRrmDot11aDCASensitivity based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_FsRrmDot11aDCASensitivity_Type.__name__ = "Integer32"
_FsRrmDot11aDCASensitivity_Object = MibScalar
fsRrmDot11aDCASensitivity = _FsRrmDot11aDCASensitivity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 5),
    _FsRrmDot11aDCASensitivity_Type()
)
fsRrmDot11aDCASensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aDCASensitivity.setStatus("current")


class _FsRrmDot11aForeignInterfereFactorEnable_Type(Integer32):
    """Custom type fsRrmDot11aForeignInterfereFactorEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11aForeignInterfereFactorEnable_Type.__name__ = "Integer32"
_FsRrmDot11aForeignInterfereFactorEnable_Object = MibScalar
fsRrmDot11aForeignInterfereFactorEnable = _FsRrmDot11aForeignInterfereFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 6),
    _FsRrmDot11aForeignInterfereFactorEnable_Type()
)
fsRrmDot11aForeignInterfereFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aForeignInterfereFactorEnable.setStatus("current")


class _FsRrmDot11aLoadFactorEnable_Type(Integer32):
    """Custom type fsRrmDot11aLoadFactorEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11aLoadFactorEnable_Type.__name__ = "Integer32"
_FsRrmDot11aLoadFactorEnable_Object = MibScalar
fsRrmDot11aLoadFactorEnable = _FsRrmDot11aLoadFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 7),
    _FsRrmDot11aLoadFactorEnable_Type()
)
fsRrmDot11aLoadFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aLoadFactorEnable.setStatus("current")


class _FsRrmDot11aNoiseFactorEnable_Type(Integer32):
    """Custom type fsRrmDot11aNoiseFactorEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11aNoiseFactorEnable_Type.__name__ = "Integer32"
_FsRrmDot11aNoiseFactorEnable_Object = MibScalar
fsRrmDot11aNoiseFactorEnable = _FsRrmDot11aNoiseFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 8),
    _FsRrmDot11aNoiseFactorEnable_Type()
)
fsRrmDot11aNoiseFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aNoiseFactorEnable.setStatus("current")


class _FsRrmDot11aChannelUpdateCmdInvoke_Type(Integer32):
    """Custom type fsRrmDot11aChannelUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_FsRrmDot11aChannelUpdateCmdInvoke_Type.__name__ = "Integer32"
_FsRrmDot11aChannelUpdateCmdInvoke_Object = MibScalar
fsRrmDot11aChannelUpdateCmdInvoke = _FsRrmDot11aChannelUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 9),
    _FsRrmDot11aChannelUpdateCmdInvoke_Type()
)
fsRrmDot11aChannelUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aChannelUpdateCmdInvoke.setStatus("current")
_FsRrmDot11aDCAChannelTable_Object = MibTable
fsRrmDot11aDCAChannelTable = _FsRrmDot11aDCAChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    fsRrmDot11aDCAChannelTable.setStatus("current")
_FsRrmDot11aDCAChannelEntry_Object = MibTableRow
fsRrmDot11aDCAChannelEntry = _FsRrmDot11aDCAChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 10, 1)
)
fsRrmDot11aDCAChannelEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmDot11aDCAChannelIndex"),
)
if mibBuilder.loadTexts:
    fsRrmDot11aDCAChannelEntry.setStatus("current")
_FsRrmDot11aDCAChannelIndex_Type = Integer32
_FsRrmDot11aDCAChannelIndex_Object = MibTableColumn
fsRrmDot11aDCAChannelIndex = _FsRrmDot11aDCAChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 10, 1, 1),
    _FsRrmDot11aDCAChannelIndex_Type()
)
fsRrmDot11aDCAChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aDCAChannelIndex.setStatus("current")


class _FsRrmDot11aDCAChannelOperation_Type(Integer32):
    """Custom type fsRrmDot11aDCAChannelOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 0),
          ("add", 1))
    )


_FsRrmDot11aDCAChannelOperation_Type.__name__ = "Integer32"
_FsRrmDot11aDCAChannelOperation_Object = MibTableColumn
fsRrmDot11aDCAChannelOperation = _FsRrmDot11aDCAChannelOperation_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 1, 10, 1, 2),
    _FsRrmDot11aDCAChannelOperation_Type()
)
fsRrmDot11aDCAChannelOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aDCAChannelOperation.setStatus("current")
_FsRrmTPCDot11a_ObjectIdentity = ObjectIdentity
fsRrmTPCDot11a = _FsRrmTPCDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 2)
)


class _FsRrmDot11aDTPCSupport_Type(Integer32):
    """Custom type fsRrmDot11aDTPCSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11aDTPCSupport_Type.__name__ = "Integer32"
_FsRrmDot11aDTPCSupport_Object = MibScalar
fsRrmDot11aDTPCSupport = _FsRrmDot11aDTPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 2, 1),
    _FsRrmDot11aDTPCSupport_Type()
)
fsRrmDot11aDTPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aDTPCSupport.setStatus("current")


class _FsRrmDot11aDynamicTransmitPowerControl_Type(Integer32):
    """Custom type fsRrmDot11aDynamicTransmitPowerControl based on Integer32"""
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
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_FsRrmDot11aDynamicTransmitPowerControl_Type.__name__ = "Integer32"
_FsRrmDot11aDynamicTransmitPowerControl_Object = MibScalar
fsRrmDot11aDynamicTransmitPowerControl = _FsRrmDot11aDynamicTransmitPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 2, 2),
    _FsRrmDot11aDynamicTransmitPowerControl_Type()
)
fsRrmDot11aDynamicTransmitPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aDynamicTransmitPowerControl.setStatus("current")


class _FsRrmDot11aDynamicTxPowerControlInterval_Type(Unsigned32):
    """Custom type fsRrmDot11aDynamicTxPowerControlInterval based on Unsigned32"""
    defaultValue = 600


_FsRrmDot11aDynamicTxPowerControlInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11aDynamicTxPowerControlInterval_Object = MibScalar
fsRrmDot11aDynamicTxPowerControlInterval = _FsRrmDot11aDynamicTxPowerControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 2, 3),
    _FsRrmDot11aDynamicTxPowerControlInterval_Type()
)
fsRrmDot11aDynamicTxPowerControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aDynamicTxPowerControlInterval.setStatus("current")


class _FsRrmDot11aCurrentTxPowerLevel_Type(Integer32):
    """Custom type fsRrmDot11aCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FsRrmDot11aCurrentTxPowerLevel_Type.__name__ = "Integer32"
_FsRrmDot11aCurrentTxPowerLevel_Object = MibScalar
fsRrmDot11aCurrentTxPowerLevel = _FsRrmDot11aCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 2, 4),
    _FsRrmDot11aCurrentTxPowerLevel_Type()
)
fsRrmDot11aCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCurrentTxPowerLevel.setStatus("current")


class _FsRrmDot11aPowerUpdateCmdInvoke_Type(Integer32):
    """Custom type fsRrmDot11aPowerUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_FsRrmDot11aPowerUpdateCmdInvoke_Type.__name__ = "Integer32"
_FsRrmDot11aPowerUpdateCmdInvoke_Object = MibScalar
fsRrmDot11aPowerUpdateCmdInvoke = _FsRrmDot11aPowerUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 2, 5),
    _FsRrmDot11aPowerUpdateCmdInvoke_Type()
)
fsRrmDot11aPowerUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aPowerUpdateCmdInvoke.setStatus("current")


class _FsRrmDot11aTXPowerThreshold_Type(Integer32):
    """Custom type fsRrmDot11aTXPowerThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_FsRrmDot11aTXPowerThreshold_Type.__name__ = "Integer32"
_FsRrmDot11aTXPowerThreshold_Object = MibScalar
fsRrmDot11aTXPowerThreshold = _FsRrmDot11aTXPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 2, 6),
    _FsRrmDot11aTXPowerThreshold_Type()
)
fsRrmDot11aTXPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aTXPowerThreshold.setStatus("current")


class _FsRrmDot11aTPCNeighborNumber_Type(Integer32):
    """Custom type fsRrmDot11aTPCNeighborNumber based on Integer32"""
    defaultValue = 3


_FsRrmDot11aTPCNeighborNumber_Type.__name__ = "Integer32"
_FsRrmDot11aTPCNeighborNumber_Object = MibScalar
fsRrmDot11aTPCNeighborNumber = _FsRrmDot11aTPCNeighborNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 2, 7),
    _FsRrmDot11aTPCNeighborNumber_Type()
)
fsRrmDot11aTPCNeighborNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aTPCNeighborNumber.setStatus("current")
_FsRrmCHDDot11a_ObjectIdentity = ObjectIdentity
fsRrmCHDDot11a = _FsRrmCHDDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3)
)


class _FsRrmDot11aCoverageEnable_Type(Integer32):
    """Custom type fsRrmDot11aCoverageEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11aCoverageEnable_Type.__name__ = "Integer32"
_FsRrmDot11aCoverageEnable_Object = MibScalar
fsRrmDot11aCoverageEnable = _FsRrmDot11aCoverageEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3, 1),
    _FsRrmDot11aCoverageEnable_Type()
)
fsRrmDot11aCoverageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageEnable.setStatus("current")


class _FsRrmDot11aCoverageExceptionGlobal_Type(Integer32):
    """Custom type fsRrmDot11aCoverageExceptionGlobal based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11aCoverageExceptionGlobal_Type.__name__ = "Integer32"
_FsRrmDot11aCoverageExceptionGlobal_Object = MibScalar
fsRrmDot11aCoverageExceptionGlobal = _FsRrmDot11aCoverageExceptionGlobal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3, 2),
    _FsRrmDot11aCoverageExceptionGlobal_Type()
)
fsRrmDot11aCoverageExceptionGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageExceptionGlobal.setStatus("current")


class _FsRrmDot11aCoverageLevelGlobal_Type(Integer32):
    """Custom type fsRrmDot11aCoverageLevelGlobal based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_FsRrmDot11aCoverageLevelGlobal_Type.__name__ = "Integer32"
_FsRrmDot11aCoverageLevelGlobal_Object = MibScalar
fsRrmDot11aCoverageLevelGlobal = _FsRrmDot11aCoverageLevelGlobal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3, 3),
    _FsRrmDot11aCoverageLevelGlobal_Type()
)
fsRrmDot11aCoverageLevelGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageLevelGlobal.setStatus("current")


class _FsRrmDot11aCoverageDataRSSIThreshold_Type(Integer32):
    """Custom type fsRrmDot11aCoverageDataRSSIThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_FsRrmDot11aCoverageDataRSSIThreshold_Type.__name__ = "Integer32"
_FsRrmDot11aCoverageDataRSSIThreshold_Object = MibScalar
fsRrmDot11aCoverageDataRSSIThreshold = _FsRrmDot11aCoverageDataRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3, 4),
    _FsRrmDot11aCoverageDataRSSIThreshold_Type()
)
fsRrmDot11aCoverageDataRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageDataRSSIThreshold.setStatus("current")


class _FsRrmDot11aCoverageVoiceRSSIThreshold_Type(Integer32):
    """Custom type fsRrmDot11aCoverageVoiceRSSIThreshold based on Integer32"""
    defaultValue = -75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_FsRrmDot11aCoverageVoiceRSSIThreshold_Type.__name__ = "Integer32"
_FsRrmDot11aCoverageVoiceRSSIThreshold_Object = MibScalar
fsRrmDot11aCoverageVoiceRSSIThreshold = _FsRrmDot11aCoverageVoiceRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3, 5),
    _FsRrmDot11aCoverageVoiceRSSIThreshold_Type()
)
fsRrmDot11aCoverageVoiceRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageVoiceRSSIThreshold.setStatus("current")


class _FsRrmDot11aCoverageDataPacketCount_Type(Integer32):
    """Custom type fsRrmDot11aCoverageDataPacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsRrmDot11aCoverageDataPacketCount_Type.__name__ = "Integer32"
_FsRrmDot11aCoverageDataPacketCount_Object = MibScalar
fsRrmDot11aCoverageDataPacketCount = _FsRrmDot11aCoverageDataPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3, 6),
    _FsRrmDot11aCoverageDataPacketCount_Type()
)
fsRrmDot11aCoverageDataPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageDataPacketCount.setStatus("current")


class _FsRrmDot11aCoverageVoicePacketCount_Type(Integer32):
    """Custom type fsRrmDot11aCoverageVoicePacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsRrmDot11aCoverageVoicePacketCount_Type.__name__ = "Integer32"
_FsRrmDot11aCoverageVoicePacketCount_Object = MibScalar
fsRrmDot11aCoverageVoicePacketCount = _FsRrmDot11aCoverageVoicePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3, 7),
    _FsRrmDot11aCoverageVoicePacketCount_Type()
)
fsRrmDot11aCoverageVoicePacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageVoicePacketCount.setStatus("current")


class _FsRrmDot11aCoverageDataFailRate_Type(Integer32):
    """Custom type fsRrmDot11aCoverageDataFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11aCoverageDataFailRate_Type.__name__ = "Integer32"
_FsRrmDot11aCoverageDataFailRate_Object = MibScalar
fsRrmDot11aCoverageDataFailRate = _FsRrmDot11aCoverageDataFailRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3, 8),
    _FsRrmDot11aCoverageDataFailRate_Type()
)
fsRrmDot11aCoverageDataFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageDataFailRate.setStatus("current")


class _FsRrmDot11aCoverageVoiceFailRate_Type(Integer32):
    """Custom type fsRrmDot11aCoverageVoiceFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11aCoverageVoiceFailRate_Type.__name__ = "Integer32"
_FsRrmDot11aCoverageVoiceFailRate_Object = MibScalar
fsRrmDot11aCoverageVoiceFailRate = _FsRrmDot11aCoverageVoiceFailRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 3, 9),
    _FsRrmDot11aCoverageVoiceFailRate_Type()
)
fsRrmDot11aCoverageVoiceFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageVoiceFailRate.setStatus("current")
_FsRrmGroupDot11a_ObjectIdentity = ObjectIdentity
fsRrmGroupDot11a = _FsRrmGroupDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4)
)


class _FsRrmDot11aGlobalAutomaticGrouping_Type(Integer32):
    """Custom type fsRrmDot11aGlobalAutomaticGrouping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("automatic", 1))
    )


_FsRrmDot11aGlobalAutomaticGrouping_Type.__name__ = "Integer32"
_FsRrmDot11aGlobalAutomaticGrouping_Object = MibScalar
fsRrmDot11aGlobalAutomaticGrouping = _FsRrmDot11aGlobalAutomaticGrouping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 1),
    _FsRrmDot11aGlobalAutomaticGrouping_Type()
)
fsRrmDot11aGlobalAutomaticGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aGlobalAutomaticGrouping.setStatus("current")
_FsRrmDot11aGroupLeaderMacAddr_Type = MacAddress
_FsRrmDot11aGroupLeaderMacAddr_Object = MibScalar
fsRrmDot11aGroupLeaderMacAddr = _FsRrmDot11aGroupLeaderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 2),
    _FsRrmDot11aGroupLeaderMacAddr_Type()
)
fsRrmDot11aGroupLeaderMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aGroupLeaderMacAddr.setStatus("current")


class _FsRrmDot11aGroupLeader_Type(Integer32):
    """Custom type fsRrmDot11aGroupLeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsRrmDot11aGroupLeader_Type.__name__ = "Integer32"
_FsRrmDot11aGroupLeader_Object = MibScalar
fsRrmDot11aGroupLeader = _FsRrmDot11aGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 3),
    _FsRrmDot11aGroupLeader_Type()
)
fsRrmDot11aGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aGroupLeader.setStatus("current")
_FsRrmDot11aGroupLastUpdateTime_Type = Unsigned32
_FsRrmDot11aGroupLastUpdateTime_Object = MibScalar
fsRrmDot11aGroupLastUpdateTime = _FsRrmDot11aGroupLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 4),
    _FsRrmDot11aGroupLastUpdateTime_Type()
)
fsRrmDot11aGroupLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aGroupLastUpdateTime.setStatus("current")


class _FsRrmDot11aGroupInterval_Type(Unsigned32):
    """Custom type fsRrmDot11aGroupInterval based on Unsigned32"""
    defaultValue = 3600


_FsRrmDot11aGroupInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11aGroupInterval_Object = MibScalar
fsRrmDot11aGroupInterval = _FsRrmDot11aGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 5),
    _FsRrmDot11aGroupInterval_Type()
)
fsRrmDot11aGroupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aGroupInterval.setStatus("current")
_FsRrmDot11aGroupTable_Object = MibTable
fsRrmDot11aGroupTable = _FsRrmDot11aGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 6)
)
if mibBuilder.loadTexts:
    fsRrmDot11aGroupTable.setStatus("current")
_FsRrmDot11aGroupEntry_Object = MibTableRow
fsRrmDot11aGroupEntry = _FsRrmDot11aGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 6, 1)
)
fsRrmDot11aGroupEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmDot11aPeerMacAddress"),
)
if mibBuilder.loadTexts:
    fsRrmDot11aGroupEntry.setStatus("current")
_FsRrmDot11aPeerMacAddress_Type = MacAddress
_FsRrmDot11aPeerMacAddress_Object = MibTableColumn
fsRrmDot11aPeerMacAddress = _FsRrmDot11aPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 6, 1, 1),
    _FsRrmDot11aPeerMacAddress_Type()
)
fsRrmDot11aPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aPeerMacAddress.setStatus("current")
_FsRrmDot11aPeerIpAddress_Type = IpAddress
_FsRrmDot11aPeerIpAddress_Object = MibTableColumn
fsRrmDot11aPeerIpAddress = _FsRrmDot11aPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 6, 1, 2),
    _FsRrmDot11aPeerIpAddress_Type()
)
fsRrmDot11aPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aPeerIpAddress.setStatus("current")
_FsRrmDot11aSummaryTable_Object = MibTable
fsRrmDot11aSummaryTable = _FsRrmDot11aSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 7)
)
if mibBuilder.loadTexts:
    fsRrmDot11aSummaryTable.setStatus("current")
_FsRrmDot11aSummaryEntry_Object = MibTableRow
fsRrmDot11aSummaryEntry = _FsRrmDot11aSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1)
)
fsRrmDot11aSummaryEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmDot11aSummaryMacAddress"),
    (0, "FS-RRM-MIB", "fsRrmDot11aAPRadioID"),
)
if mibBuilder.loadTexts:
    fsRrmDot11aSummaryEntry.setStatus("current")
_FsRrmDot11aAPname_Type = DisplayString
_FsRrmDot11aAPname_Object = MibTableColumn
fsRrmDot11aAPname = _FsRrmDot11aAPname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 1),
    _FsRrmDot11aAPname_Type()
)
fsRrmDot11aAPname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aAPname.setStatus("current")
_FsRrmDot11aAPRadioID_Type = Unsigned32
_FsRrmDot11aAPRadioID_Object = MibTableColumn
fsRrmDot11aAPRadioID = _FsRrmDot11aAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 2),
    _FsRrmDot11aAPRadioID_Type()
)
fsRrmDot11aAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aAPRadioID.setStatus("current")
_FsRrmDot11aAPChannel_Type = Unsigned32
_FsRrmDot11aAPChannel_Object = MibTableColumn
fsRrmDot11aAPChannel = _FsRrmDot11aAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 3),
    _FsRrmDot11aAPChannel_Type()
)
fsRrmDot11aAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aAPChannel.setStatus("current")
_FsRrmDot11aAPTxPower_Type = Unsigned32
_FsRrmDot11aAPTxPower_Object = MibTableColumn
fsRrmDot11aAPTxPower = _FsRrmDot11aAPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 4),
    _FsRrmDot11aAPTxPower_Type()
)
fsRrmDot11aAPTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aAPTxPower.setStatus("current")


class _FsRrmDot11aAPChannelRrmChangeFlag_Type(Integer32):
    """Custom type fsRrmDot11aAPChannelRrmChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsRrmDot11aAPChannelRrmChangeFlag_Type.__name__ = "Integer32"
_FsRrmDot11aAPChannelRrmChangeFlag_Object = MibTableColumn
fsRrmDot11aAPChannelRrmChangeFlag = _FsRrmDot11aAPChannelRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 5),
    _FsRrmDot11aAPChannelRrmChangeFlag_Type()
)
fsRrmDot11aAPChannelRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aAPChannelRrmChangeFlag.setStatus("current")


class _FsRrmDot11aAPTxPowerRrmChangeFlag_Type(Integer32):
    """Custom type fsRrmDot11aAPTxPowerRrmChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsRrmDot11aAPTxPowerRrmChangeFlag_Type.__name__ = "Integer32"
_FsRrmDot11aAPTxPowerRrmChangeFlag_Object = MibTableColumn
fsRrmDot11aAPTxPowerRrmChangeFlag = _FsRrmDot11aAPTxPowerRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 6),
    _FsRrmDot11aAPTxPowerRrmChangeFlag_Type()
)
fsRrmDot11aAPTxPowerRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aAPTxPowerRrmChangeFlag.setStatus("current")
_FsRrmDot11aSummaryMacAddress_Type = MacAddress
_FsRrmDot11aSummaryMacAddress_Object = MibTableColumn
fsRrmDot11aSummaryMacAddress = _FsRrmDot11aSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 7),
    _FsRrmDot11aSummaryMacAddress_Type()
)
fsRrmDot11aSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11aSummaryMacAddress.setStatus("current")
_FsRrmProfileDot11a_ObjectIdentity = ObjectIdentity
fsRrmProfileDot11a = _FsRrmProfileDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 5)
)


class _FsRrmDot11aForeignInterferenceThreshold_Type(Integer32):
    """Custom type fsRrmDot11aForeignInterferenceThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11aForeignInterferenceThreshold_Type.__name__ = "Integer32"
_FsRrmDot11aForeignInterferenceThreshold_Object = MibScalar
fsRrmDot11aForeignInterferenceThreshold = _FsRrmDot11aForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 5, 1),
    _FsRrmDot11aForeignInterferenceThreshold_Type()
)
fsRrmDot11aForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aForeignInterferenceThreshold.setStatus("current")


class _FsRrmDot11aForeignNoiseThreshold_Type(Integer32):
    """Custom type fsRrmDot11aForeignNoiseThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_FsRrmDot11aForeignNoiseThreshold_Type.__name__ = "Integer32"
_FsRrmDot11aForeignNoiseThreshold_Object = MibScalar
fsRrmDot11aForeignNoiseThreshold = _FsRrmDot11aForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 5, 2),
    _FsRrmDot11aForeignNoiseThreshold_Type()
)
fsRrmDot11aForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aForeignNoiseThreshold.setStatus("current")


class _FsRrmDot11aRFUtilizationThreshold_Type(Integer32):
    """Custom type fsRrmDot11aRFUtilizationThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11aRFUtilizationThreshold_Type.__name__ = "Integer32"
_FsRrmDot11aRFUtilizationThreshold_Object = MibScalar
fsRrmDot11aRFUtilizationThreshold = _FsRrmDot11aRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 5, 3),
    _FsRrmDot11aRFUtilizationThreshold_Type()
)
fsRrmDot11aRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aRFUtilizationThreshold.setStatus("current")


class _FsRrmDot11aThroughputThreshold_Type(Unsigned32):
    """Custom type fsRrmDot11aThroughputThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000000),
    )


_FsRrmDot11aThroughputThreshold_Type.__name__ = "Unsigned32"
_FsRrmDot11aThroughputThreshold_Object = MibScalar
fsRrmDot11aThroughputThreshold = _FsRrmDot11aThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 5, 4),
    _FsRrmDot11aThroughputThreshold_Type()
)
fsRrmDot11aThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aThroughputThreshold.setStatus("current")


class _FsRrmDot11aMobilesThreshold_Type(Integer32):
    """Custom type fsRrmDot11aMobilesThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_FsRrmDot11aMobilesThreshold_Type.__name__ = "Integer32"
_FsRrmDot11aMobilesThreshold_Object = MibScalar
fsRrmDot11aMobilesThreshold = _FsRrmDot11aMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 5, 5),
    _FsRrmDot11aMobilesThreshold_Type()
)
fsRrmDot11aMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aMobilesThreshold.setStatus("current")
_FsRrmMonitorDot11a_ObjectIdentity = ObjectIdentity
fsRrmMonitorDot11a = _FsRrmMonitorDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 6)
)


class _FsRrmDot11aMonitorEnable_Type(Integer32):
    """Custom type fsRrmDot11aMonitorEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11aMonitorEnable_Type.__name__ = "Integer32"
_FsRrmDot11aMonitorEnable_Object = MibScalar
fsRrmDot11aMonitorEnable = _FsRrmDot11aMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 6, 1),
    _FsRrmDot11aMonitorEnable_Type()
)
fsRrmDot11aMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aMonitorEnable.setStatus("current")


class _FsRrmDot11aChannelMonitorList_Type(Integer32):
    """Custom type fsRrmDot11aChannelMonitorList based on Integer32"""
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
        *(("all", 1),
          ("country", 2),
          ("dca", 3))
    )


_FsRrmDot11aChannelMonitorList_Type.__name__ = "Integer32"
_FsRrmDot11aChannelMonitorList_Object = MibScalar
fsRrmDot11aChannelMonitorList = _FsRrmDot11aChannelMonitorList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 6, 2),
    _FsRrmDot11aChannelMonitorList_Type()
)
fsRrmDot11aChannelMonitorList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aChannelMonitorList.setStatus("current")


class _FsRrmDot11aMonitorInterval_Type(Unsigned32):
    """Custom type fsRrmDot11aMonitorInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11aMonitorInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11aMonitorInterval_Object = MibScalar
fsRrmDot11aMonitorInterval = _FsRrmDot11aMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 6, 3),
    _FsRrmDot11aMonitorInterval_Type()
)
fsRrmDot11aMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aMonitorInterval.setStatus("current")


class _FsRrmDot11aCoverageMeasurementInterval_Type(Unsigned32):
    """Custom type fsRrmDot11aCoverageMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11aCoverageMeasurementInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11aCoverageMeasurementInterval_Object = MibScalar
fsRrmDot11aCoverageMeasurementInterval = _FsRrmDot11aCoverageMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 6, 4),
    _FsRrmDot11aCoverageMeasurementInterval_Type()
)
fsRrmDot11aCoverageMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aCoverageMeasurementInterval.setStatus("current")


class _FsRrmDot11aLoadMeasurementInterval_Type(Unsigned32):
    """Custom type fsRrmDot11aLoadMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11aLoadMeasurementInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11aLoadMeasurementInterval_Object = MibScalar
fsRrmDot11aLoadMeasurementInterval = _FsRrmDot11aLoadMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 6, 5),
    _FsRrmDot11aLoadMeasurementInterval_Type()
)
fsRrmDot11aLoadMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aLoadMeasurementInterval.setStatus("current")


class _FsRrmDot11aNoiseMeasurementInterval_Type(Unsigned32):
    """Custom type fsRrmDot11aNoiseMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11aNoiseMeasurementInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11aNoiseMeasurementInterval_Object = MibScalar
fsRrmDot11aNoiseMeasurementInterval = _FsRrmDot11aNoiseMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 6, 6),
    _FsRrmDot11aNoiseMeasurementInterval_Type()
)
fsRrmDot11aNoiseMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aNoiseMeasurementInterval.setStatus("current")


class _FsRrmDot11aSignalMeasurementInterval_Type(Unsigned32):
    """Custom type fsRrmDot11aSignalMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11aSignalMeasurementInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11aSignalMeasurementInterval_Object = MibScalar
fsRrmDot11aSignalMeasurementInterval = _FsRrmDot11aSignalMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 6, 7),
    _FsRrmDot11aSignalMeasurementInterval_Type()
)
fsRrmDot11aSignalMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aSignalMeasurementInterval.setStatus("current")


class _FsRrmDot11aNeighborMessageInterval_Type(Unsigned32):
    """Custom type fsRrmDot11aNeighborMessageInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11aNeighborMessageInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11aNeighborMessageInterval_Object = MibScalar
fsRrmDot11aNeighborMessageInterval = _FsRrmDot11aNeighborMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 6, 8),
    _FsRrmDot11aNeighborMessageInterval_Type()
)
fsRrmDot11aNeighborMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aNeighborMessageInterval.setStatus("current")
_FsRrmFactoryDot11a_ObjectIdentity = ObjectIdentity
fsRrmFactoryDot11a = _FsRrmFactoryDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 7)
)


class _FsRrmDot11aSetFactoryDefault_Type(Integer32):
    """Custom type fsRrmDot11aSetFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_FsRrmDot11aSetFactoryDefault_Type.__name__ = "Integer32"
_FsRrmDot11aSetFactoryDefault_Object = MibScalar
fsRrmDot11aSetFactoryDefault = _FsRrmDot11aSetFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 2, 7, 1),
    _FsRrmDot11aSetFactoryDefault_Type()
)
fsRrmDot11aSetFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11aSetFactoryDefault.setStatus("current")
_FsRrmObjectsDot11b_ObjectIdentity = ObjectIdentity
fsRrmObjectsDot11b = _FsRrmObjectsDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3)
)
_FsRrmDCADot11b_ObjectIdentity = ObjectIdentity
fsRrmDCADot11b = _FsRrmDCADot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1)
)


class _FsRrmDot11bDynamicChannelAssignment_Type(Integer32):
    """Custom type fsRrmDot11bDynamicChannelAssignment based on Integer32"""
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
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_FsRrmDot11bDynamicChannelAssignment_Type.__name__ = "Integer32"
_FsRrmDot11bDynamicChannelAssignment_Object = MibScalar
fsRrmDot11bDynamicChannelAssignment = _FsRrmDot11bDynamicChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 1),
    _FsRrmDot11bDynamicChannelAssignment_Type()
)
fsRrmDot11bDynamicChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bDynamicChannelAssignment.setStatus("current")


class _FsRrmDot11bAnchorTime_Type(Unsigned32):
    """Custom type fsRrmDot11bAnchorTime based on Unsigned32"""
    defaultValue = 0


_FsRrmDot11bAnchorTime_Type.__name__ = "Unsigned32"
_FsRrmDot11bAnchorTime_Object = MibScalar
fsRrmDot11bAnchorTime = _FsRrmDot11bAnchorTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 2),
    _FsRrmDot11bAnchorTime_Type()
)
fsRrmDot11bAnchorTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bAnchorTime.setStatus("current")


class _FsRrmDot11bChannalWidth11n_Type(Unsigned32):
    """Custom type fsRrmDot11bChannalWidth11n based on Unsigned32"""
    defaultValue = 20


_FsRrmDot11bChannalWidth11n_Type.__name__ = "Unsigned32"
_FsRrmDot11bChannalWidth11n_Object = MibScalar
fsRrmDot11bChannalWidth11n = _FsRrmDot11bChannalWidth11n_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 3),
    _FsRrmDot11bChannalWidth11n_Type()
)
fsRrmDot11bChannalWidth11n.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bChannalWidth11n.setStatus("current")


class _FsRrmDot11bDynamicChannelUpdateInterval_Type(Unsigned32):
    """Custom type fsRrmDot11bDynamicChannelUpdateInterval based on Unsigned32"""
    defaultValue = 600


_FsRrmDot11bDynamicChannelUpdateInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11bDynamicChannelUpdateInterval_Object = MibScalar
fsRrmDot11bDynamicChannelUpdateInterval = _FsRrmDot11bDynamicChannelUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 4),
    _FsRrmDot11bDynamicChannelUpdateInterval_Type()
)
fsRrmDot11bDynamicChannelUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bDynamicChannelUpdateInterval.setStatus("current")


class _FsRrmDot11bDCASensitivity_Type(Integer32):
    """Custom type fsRrmDot11bDCASensitivity based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_FsRrmDot11bDCASensitivity_Type.__name__ = "Integer32"
_FsRrmDot11bDCASensitivity_Object = MibScalar
fsRrmDot11bDCASensitivity = _FsRrmDot11bDCASensitivity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 5),
    _FsRrmDot11bDCASensitivity_Type()
)
fsRrmDot11bDCASensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bDCASensitivity.setStatus("current")


class _FsRrmDot11bForeignInterfereFactorEnable_Type(Integer32):
    """Custom type fsRrmDot11bForeignInterfereFactorEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11bForeignInterfereFactorEnable_Type.__name__ = "Integer32"
_FsRrmDot11bForeignInterfereFactorEnable_Object = MibScalar
fsRrmDot11bForeignInterfereFactorEnable = _FsRrmDot11bForeignInterfereFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 6),
    _FsRrmDot11bForeignInterfereFactorEnable_Type()
)
fsRrmDot11bForeignInterfereFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bForeignInterfereFactorEnable.setStatus("current")


class _FsRrmDot11bLoadFactorEnable_Type(Integer32):
    """Custom type fsRrmDot11bLoadFactorEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11bLoadFactorEnable_Type.__name__ = "Integer32"
_FsRrmDot11bLoadFactorEnable_Object = MibScalar
fsRrmDot11bLoadFactorEnable = _FsRrmDot11bLoadFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 7),
    _FsRrmDot11bLoadFactorEnable_Type()
)
fsRrmDot11bLoadFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bLoadFactorEnable.setStatus("current")


class _FsRrmDot11bNoiseFactorEnable_Type(Integer32):
    """Custom type fsRrmDot11bNoiseFactorEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11bNoiseFactorEnable_Type.__name__ = "Integer32"
_FsRrmDot11bNoiseFactorEnable_Object = MibScalar
fsRrmDot11bNoiseFactorEnable = _FsRrmDot11bNoiseFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 8),
    _FsRrmDot11bNoiseFactorEnable_Type()
)
fsRrmDot11bNoiseFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bNoiseFactorEnable.setStatus("current")


class _FsRrmDot11bChannelUpdateCmdInvoke_Type(Integer32):
    """Custom type fsRrmDot11bChannelUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_FsRrmDot11bChannelUpdateCmdInvoke_Type.__name__ = "Integer32"
_FsRrmDot11bChannelUpdateCmdInvoke_Object = MibScalar
fsRrmDot11bChannelUpdateCmdInvoke = _FsRrmDot11bChannelUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 9),
    _FsRrmDot11bChannelUpdateCmdInvoke_Type()
)
fsRrmDot11bChannelUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bChannelUpdateCmdInvoke.setStatus("current")
_FsRrmDot11bDCAChannelTable_Object = MibTable
fsRrmDot11bDCAChannelTable = _FsRrmDot11bDCAChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    fsRrmDot11bDCAChannelTable.setStatus("current")
_FsRrmDot11bDCAChannelEntry_Object = MibTableRow
fsRrmDot11bDCAChannelEntry = _FsRrmDot11bDCAChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 10, 1)
)
fsRrmDot11bDCAChannelEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmDot11bDCAChannelIndex"),
)
if mibBuilder.loadTexts:
    fsRrmDot11bDCAChannelEntry.setStatus("current")
_FsRrmDot11bDCAChannelIndex_Type = Integer32
_FsRrmDot11bDCAChannelIndex_Object = MibTableColumn
fsRrmDot11bDCAChannelIndex = _FsRrmDot11bDCAChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 10, 1, 1),
    _FsRrmDot11bDCAChannelIndex_Type()
)
fsRrmDot11bDCAChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bDCAChannelIndex.setStatus("current")


class _FsRrmDot11bDCAChannelOperation_Type(Integer32):
    """Custom type fsRrmDot11bDCAChannelOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 0),
          ("add", 1))
    )


_FsRrmDot11bDCAChannelOperation_Type.__name__ = "Integer32"
_FsRrmDot11bDCAChannelOperation_Object = MibTableColumn
fsRrmDot11bDCAChannelOperation = _FsRrmDot11bDCAChannelOperation_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 1, 10, 1, 2),
    _FsRrmDot11bDCAChannelOperation_Type()
)
fsRrmDot11bDCAChannelOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bDCAChannelOperation.setStatus("current")
_FsRrmTPCDot11b_ObjectIdentity = ObjectIdentity
fsRrmTPCDot11b = _FsRrmTPCDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 2)
)


class _FsRrmDot11bDTPCSupport_Type(Integer32):
    """Custom type fsRrmDot11bDTPCSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11bDTPCSupport_Type.__name__ = "Integer32"
_FsRrmDot11bDTPCSupport_Object = MibScalar
fsRrmDot11bDTPCSupport = _FsRrmDot11bDTPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 2, 1),
    _FsRrmDot11bDTPCSupport_Type()
)
fsRrmDot11bDTPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bDTPCSupport.setStatus("current")


class _FsRrmDot11bDynamicTransmitPowerControl_Type(Integer32):
    """Custom type fsRrmDot11bDynamicTransmitPowerControl based on Integer32"""
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
        *(("automatic", 1),
          ("runOnce", 2),
          ("static", 3))
    )


_FsRrmDot11bDynamicTransmitPowerControl_Type.__name__ = "Integer32"
_FsRrmDot11bDynamicTransmitPowerControl_Object = MibScalar
fsRrmDot11bDynamicTransmitPowerControl = _FsRrmDot11bDynamicTransmitPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 2, 2),
    _FsRrmDot11bDynamicTransmitPowerControl_Type()
)
fsRrmDot11bDynamicTransmitPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bDynamicTransmitPowerControl.setStatus("current")


class _FsRrmDot11bDynamicTxPowerControlInterval_Type(Unsigned32):
    """Custom type fsRrmDot11bDynamicTxPowerControlInterval based on Unsigned32"""
    defaultValue = 600


_FsRrmDot11bDynamicTxPowerControlInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11bDynamicTxPowerControlInterval_Object = MibScalar
fsRrmDot11bDynamicTxPowerControlInterval = _FsRrmDot11bDynamicTxPowerControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 2, 3),
    _FsRrmDot11bDynamicTxPowerControlInterval_Type()
)
fsRrmDot11bDynamicTxPowerControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bDynamicTxPowerControlInterval.setStatus("current")


class _FsRrmDot11bCurrentTxPowerLevel_Type(Integer32):
    """Custom type fsRrmDot11bCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FsRrmDot11bCurrentTxPowerLevel_Type.__name__ = "Integer32"
_FsRrmDot11bCurrentTxPowerLevel_Object = MibScalar
fsRrmDot11bCurrentTxPowerLevel = _FsRrmDot11bCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 2, 4),
    _FsRrmDot11bCurrentTxPowerLevel_Type()
)
fsRrmDot11bCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCurrentTxPowerLevel.setStatus("current")


class _FsRrmDot11bPowerUpdateCmdInvoke_Type(Integer32):
    """Custom type fsRrmDot11bPowerUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_FsRrmDot11bPowerUpdateCmdInvoke_Type.__name__ = "Integer32"
_FsRrmDot11bPowerUpdateCmdInvoke_Object = MibScalar
fsRrmDot11bPowerUpdateCmdInvoke = _FsRrmDot11bPowerUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 2, 5),
    _FsRrmDot11bPowerUpdateCmdInvoke_Type()
)
fsRrmDot11bPowerUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bPowerUpdateCmdInvoke.setStatus("current")


class _FsRrmDot11bTXPowerThreshold_Type(Integer32):
    """Custom type fsRrmDot11bTXPowerThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_FsRrmDot11bTXPowerThreshold_Type.__name__ = "Integer32"
_FsRrmDot11bTXPowerThreshold_Object = MibScalar
fsRrmDot11bTXPowerThreshold = _FsRrmDot11bTXPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 2, 6),
    _FsRrmDot11bTXPowerThreshold_Type()
)
fsRrmDot11bTXPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bTXPowerThreshold.setStatus("current")


class _FsRrmDot11bTPCNeighborNumber_Type(Integer32):
    """Custom type fsRrmDot11bTPCNeighborNumber based on Integer32"""
    defaultValue = 3


_FsRrmDot11bTPCNeighborNumber_Type.__name__ = "Integer32"
_FsRrmDot11bTPCNeighborNumber_Object = MibScalar
fsRrmDot11bTPCNeighborNumber = _FsRrmDot11bTPCNeighborNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 2, 7),
    _FsRrmDot11bTPCNeighborNumber_Type()
)
fsRrmDot11bTPCNeighborNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bTPCNeighborNumber.setStatus("current")
_FsRrmCHDDot11b_ObjectIdentity = ObjectIdentity
fsRrmCHDDot11b = _FsRrmCHDDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3)
)


class _FsRrmDot11bCoverageEnable_Type(Integer32):
    """Custom type fsRrmDot11bCoverageEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11bCoverageEnable_Type.__name__ = "Integer32"
_FsRrmDot11bCoverageEnable_Object = MibScalar
fsRrmDot11bCoverageEnable = _FsRrmDot11bCoverageEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3, 1),
    _FsRrmDot11bCoverageEnable_Type()
)
fsRrmDot11bCoverageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageEnable.setStatus("current")


class _FsRrmDot11bCoverageExceptionGlobal_Type(Integer32):
    """Custom type fsRrmDot11bCoverageExceptionGlobal based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11bCoverageExceptionGlobal_Type.__name__ = "Integer32"
_FsRrmDot11bCoverageExceptionGlobal_Object = MibScalar
fsRrmDot11bCoverageExceptionGlobal = _FsRrmDot11bCoverageExceptionGlobal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3, 2),
    _FsRrmDot11bCoverageExceptionGlobal_Type()
)
fsRrmDot11bCoverageExceptionGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageExceptionGlobal.setStatus("current")


class _FsRrmDot11bCoverageLevelGlobal_Type(Integer32):
    """Custom type fsRrmDot11bCoverageLevelGlobal based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_FsRrmDot11bCoverageLevelGlobal_Type.__name__ = "Integer32"
_FsRrmDot11bCoverageLevelGlobal_Object = MibScalar
fsRrmDot11bCoverageLevelGlobal = _FsRrmDot11bCoverageLevelGlobal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3, 3),
    _FsRrmDot11bCoverageLevelGlobal_Type()
)
fsRrmDot11bCoverageLevelGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageLevelGlobal.setStatus("current")


class _FsRrmDot11bCoverageDataRSSIThreshold_Type(Integer32):
    """Custom type fsRrmDot11bCoverageDataRSSIThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_FsRrmDot11bCoverageDataRSSIThreshold_Type.__name__ = "Integer32"
_FsRrmDot11bCoverageDataRSSIThreshold_Object = MibScalar
fsRrmDot11bCoverageDataRSSIThreshold = _FsRrmDot11bCoverageDataRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3, 4),
    _FsRrmDot11bCoverageDataRSSIThreshold_Type()
)
fsRrmDot11bCoverageDataRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageDataRSSIThreshold.setStatus("current")


class _FsRrmDot11bCoverageVoiceRSSIThreshold_Type(Integer32):
    """Custom type fsRrmDot11bCoverageVoiceRSSIThreshold based on Integer32"""
    defaultValue = -75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_FsRrmDot11bCoverageVoiceRSSIThreshold_Type.__name__ = "Integer32"
_FsRrmDot11bCoverageVoiceRSSIThreshold_Object = MibScalar
fsRrmDot11bCoverageVoiceRSSIThreshold = _FsRrmDot11bCoverageVoiceRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3, 5),
    _FsRrmDot11bCoverageVoiceRSSIThreshold_Type()
)
fsRrmDot11bCoverageVoiceRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageVoiceRSSIThreshold.setStatus("current")


class _FsRrmDot11bCoverageDataPacketCount_Type(Integer32):
    """Custom type fsRrmDot11bCoverageDataPacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsRrmDot11bCoverageDataPacketCount_Type.__name__ = "Integer32"
_FsRrmDot11bCoverageDataPacketCount_Object = MibScalar
fsRrmDot11bCoverageDataPacketCount = _FsRrmDot11bCoverageDataPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3, 6),
    _FsRrmDot11bCoverageDataPacketCount_Type()
)
fsRrmDot11bCoverageDataPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageDataPacketCount.setStatus("current")


class _FsRrmDot11bCoverageVoicePacketCount_Type(Integer32):
    """Custom type fsRrmDot11bCoverageVoicePacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsRrmDot11bCoverageVoicePacketCount_Type.__name__ = "Integer32"
_FsRrmDot11bCoverageVoicePacketCount_Object = MibScalar
fsRrmDot11bCoverageVoicePacketCount = _FsRrmDot11bCoverageVoicePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3, 7),
    _FsRrmDot11bCoverageVoicePacketCount_Type()
)
fsRrmDot11bCoverageVoicePacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageVoicePacketCount.setStatus("current")


class _FsRrmDot11bCoverageDataFailRate_Type(Integer32):
    """Custom type fsRrmDot11bCoverageDataFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11bCoverageDataFailRate_Type.__name__ = "Integer32"
_FsRrmDot11bCoverageDataFailRate_Object = MibScalar
fsRrmDot11bCoverageDataFailRate = _FsRrmDot11bCoverageDataFailRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3, 8),
    _FsRrmDot11bCoverageDataFailRate_Type()
)
fsRrmDot11bCoverageDataFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageDataFailRate.setStatus("current")


class _FsRrmDot11bCoverageVoiceFailRate_Type(Integer32):
    """Custom type fsRrmDot11bCoverageVoiceFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11bCoverageVoiceFailRate_Type.__name__ = "Integer32"
_FsRrmDot11bCoverageVoiceFailRate_Object = MibScalar
fsRrmDot11bCoverageVoiceFailRate = _FsRrmDot11bCoverageVoiceFailRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 3, 9),
    _FsRrmDot11bCoverageVoiceFailRate_Type()
)
fsRrmDot11bCoverageVoiceFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageVoiceFailRate.setStatus("current")
_FsRrmGroupDot11b_ObjectIdentity = ObjectIdentity
fsRrmGroupDot11b = _FsRrmGroupDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4)
)


class _FsRrmDot11bGlobalAutomaticGrouping_Type(Integer32):
    """Custom type fsRrmDot11bGlobalAutomaticGrouping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("automatic", 1))
    )


_FsRrmDot11bGlobalAutomaticGrouping_Type.__name__ = "Integer32"
_FsRrmDot11bGlobalAutomaticGrouping_Object = MibScalar
fsRrmDot11bGlobalAutomaticGrouping = _FsRrmDot11bGlobalAutomaticGrouping_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 1),
    _FsRrmDot11bGlobalAutomaticGrouping_Type()
)
fsRrmDot11bGlobalAutomaticGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bGlobalAutomaticGrouping.setStatus("current")
_FsRrmDot11bGroupLeaderMacAddr_Type = MacAddress
_FsRrmDot11bGroupLeaderMacAddr_Object = MibScalar
fsRrmDot11bGroupLeaderMacAddr = _FsRrmDot11bGroupLeaderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 2),
    _FsRrmDot11bGroupLeaderMacAddr_Type()
)
fsRrmDot11bGroupLeaderMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bGroupLeaderMacAddr.setStatus("current")


class _FsRrmDot11bGroupLeader_Type(Integer32):
    """Custom type fsRrmDot11bGroupLeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsRrmDot11bGroupLeader_Type.__name__ = "Integer32"
_FsRrmDot11bGroupLeader_Object = MibScalar
fsRrmDot11bGroupLeader = _FsRrmDot11bGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 3),
    _FsRrmDot11bGroupLeader_Type()
)
fsRrmDot11bGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bGroupLeader.setStatus("current")
_FsRrmDot11bGroupLastUpdateTime_Type = Unsigned32
_FsRrmDot11bGroupLastUpdateTime_Object = MibScalar
fsRrmDot11bGroupLastUpdateTime = _FsRrmDot11bGroupLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 4),
    _FsRrmDot11bGroupLastUpdateTime_Type()
)
fsRrmDot11bGroupLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bGroupLastUpdateTime.setStatus("current")


class _FsRrmDot11bGroupInterval_Type(Unsigned32):
    """Custom type fsRrmDot11bGroupInterval based on Unsigned32"""
    defaultValue = 3600


_FsRrmDot11bGroupInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11bGroupInterval_Object = MibScalar
fsRrmDot11bGroupInterval = _FsRrmDot11bGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 5),
    _FsRrmDot11bGroupInterval_Type()
)
fsRrmDot11bGroupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bGroupInterval.setStatus("current")
_FsRrmDot11bGroupTable_Object = MibTable
fsRrmDot11bGroupTable = _FsRrmDot11bGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 6)
)
if mibBuilder.loadTexts:
    fsRrmDot11bGroupTable.setStatus("current")
_FsRrmDot11bGroupEntry_Object = MibTableRow
fsRrmDot11bGroupEntry = _FsRrmDot11bGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 6, 1)
)
fsRrmDot11bGroupEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmDot11bPeerMacAddress"),
)
if mibBuilder.loadTexts:
    fsRrmDot11bGroupEntry.setStatus("current")
_FsRrmDot11bPeerMacAddress_Type = MacAddress
_FsRrmDot11bPeerMacAddress_Object = MibTableColumn
fsRrmDot11bPeerMacAddress = _FsRrmDot11bPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 6, 1, 1),
    _FsRrmDot11bPeerMacAddress_Type()
)
fsRrmDot11bPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bPeerMacAddress.setStatus("current")
_FsRrmDot11bPeerIpAddress_Type = IpAddress
_FsRrmDot11bPeerIpAddress_Object = MibTableColumn
fsRrmDot11bPeerIpAddress = _FsRrmDot11bPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 6, 1, 2),
    _FsRrmDot11bPeerIpAddress_Type()
)
fsRrmDot11bPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bPeerIpAddress.setStatus("current")
_FsRrmDot11bSummaryTable_Object = MibTable
fsRrmDot11bSummaryTable = _FsRrmDot11bSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 7)
)
if mibBuilder.loadTexts:
    fsRrmDot11bSummaryTable.setStatus("current")
_FsRrmDot11bSummaryEntry_Object = MibTableRow
fsRrmDot11bSummaryEntry = _FsRrmDot11bSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1)
)
fsRrmDot11bSummaryEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmDot11bSummaryMacAddress"),
    (0, "FS-RRM-MIB", "fsRrmDot11bAPRadioID"),
)
if mibBuilder.loadTexts:
    fsRrmDot11bSummaryEntry.setStatus("current")
_FsRrmDot11bAPname_Type = DisplayString
_FsRrmDot11bAPname_Object = MibTableColumn
fsRrmDot11bAPname = _FsRrmDot11bAPname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 1),
    _FsRrmDot11bAPname_Type()
)
fsRrmDot11bAPname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bAPname.setStatus("current")
_FsRrmDot11bAPRadioID_Type = Unsigned32
_FsRrmDot11bAPRadioID_Object = MibTableColumn
fsRrmDot11bAPRadioID = _FsRrmDot11bAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 2),
    _FsRrmDot11bAPRadioID_Type()
)
fsRrmDot11bAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bAPRadioID.setStatus("current")
_FsRrmDot11bAPChannel_Type = Unsigned32
_FsRrmDot11bAPChannel_Object = MibTableColumn
fsRrmDot11bAPChannel = _FsRrmDot11bAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 3),
    _FsRrmDot11bAPChannel_Type()
)
fsRrmDot11bAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bAPChannel.setStatus("current")
_FsRrmDot11bAPTxPower_Type = Unsigned32
_FsRrmDot11bAPTxPower_Object = MibTableColumn
fsRrmDot11bAPTxPower = _FsRrmDot11bAPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 4),
    _FsRrmDot11bAPTxPower_Type()
)
fsRrmDot11bAPTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bAPTxPower.setStatus("current")


class _FsRrmDot11bAPChannelRrmChangeFlag_Type(Integer32):
    """Custom type fsRrmDot11bAPChannelRrmChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsRrmDot11bAPChannelRrmChangeFlag_Type.__name__ = "Integer32"
_FsRrmDot11bAPChannelRrmChangeFlag_Object = MibTableColumn
fsRrmDot11bAPChannelRrmChangeFlag = _FsRrmDot11bAPChannelRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 5),
    _FsRrmDot11bAPChannelRrmChangeFlag_Type()
)
fsRrmDot11bAPChannelRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bAPChannelRrmChangeFlag.setStatus("current")


class _FsRrmDot11bAPTxPowerRrmChangeFlag_Type(Integer32):
    """Custom type fsRrmDot11bAPTxPowerRrmChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsRrmDot11bAPTxPowerRrmChangeFlag_Type.__name__ = "Integer32"
_FsRrmDot11bAPTxPowerRrmChangeFlag_Object = MibTableColumn
fsRrmDot11bAPTxPowerRrmChangeFlag = _FsRrmDot11bAPTxPowerRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 6),
    _FsRrmDot11bAPTxPowerRrmChangeFlag_Type()
)
fsRrmDot11bAPTxPowerRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bAPTxPowerRrmChangeFlag.setStatus("current")
_FsRrmDot11bSummaryMacAddress_Type = MacAddress
_FsRrmDot11bSummaryMacAddress_Object = MibTableColumn
fsRrmDot11bSummaryMacAddress = _FsRrmDot11bSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 7),
    _FsRrmDot11bSummaryMacAddress_Type()
)
fsRrmDot11bSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmDot11bSummaryMacAddress.setStatus("current")
_FsRrmProfileDot11b_ObjectIdentity = ObjectIdentity
fsRrmProfileDot11b = _FsRrmProfileDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 5)
)


class _FsRrmDot11bForeignInterferenceThreshold_Type(Integer32):
    """Custom type fsRrmDot11bForeignInterferenceThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11bForeignInterferenceThreshold_Type.__name__ = "Integer32"
_FsRrmDot11bForeignInterferenceThreshold_Object = MibScalar
fsRrmDot11bForeignInterferenceThreshold = _FsRrmDot11bForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 5, 1),
    _FsRrmDot11bForeignInterferenceThreshold_Type()
)
fsRrmDot11bForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bForeignInterferenceThreshold.setStatus("current")


class _FsRrmDot11bForeignNoiseThreshold_Type(Integer32):
    """Custom type fsRrmDot11bForeignNoiseThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_FsRrmDot11bForeignNoiseThreshold_Type.__name__ = "Integer32"
_FsRrmDot11bForeignNoiseThreshold_Object = MibScalar
fsRrmDot11bForeignNoiseThreshold = _FsRrmDot11bForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 5, 2),
    _FsRrmDot11bForeignNoiseThreshold_Type()
)
fsRrmDot11bForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bForeignNoiseThreshold.setStatus("current")


class _FsRrmDot11bRFUtilizationThreshold_Type(Integer32):
    """Custom type fsRrmDot11bRFUtilizationThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmDot11bRFUtilizationThreshold_Type.__name__ = "Integer32"
_FsRrmDot11bRFUtilizationThreshold_Object = MibScalar
fsRrmDot11bRFUtilizationThreshold = _FsRrmDot11bRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 5, 3),
    _FsRrmDot11bRFUtilizationThreshold_Type()
)
fsRrmDot11bRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bRFUtilizationThreshold.setStatus("current")


class _FsRrmDot11bThroughputThreshold_Type(Unsigned32):
    """Custom type fsRrmDot11bThroughputThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000000),
    )


_FsRrmDot11bThroughputThreshold_Type.__name__ = "Unsigned32"
_FsRrmDot11bThroughputThreshold_Object = MibScalar
fsRrmDot11bThroughputThreshold = _FsRrmDot11bThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 5, 4),
    _FsRrmDot11bThroughputThreshold_Type()
)
fsRrmDot11bThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bThroughputThreshold.setStatus("current")


class _FsRrmDot11bMobilesThreshold_Type(Integer32):
    """Custom type fsRrmDot11bMobilesThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_FsRrmDot11bMobilesThreshold_Type.__name__ = "Integer32"
_FsRrmDot11bMobilesThreshold_Object = MibScalar
fsRrmDot11bMobilesThreshold = _FsRrmDot11bMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 5, 5),
    _FsRrmDot11bMobilesThreshold_Type()
)
fsRrmDot11bMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bMobilesThreshold.setStatus("current")
_FsRrmMonitorDot11b_ObjectIdentity = ObjectIdentity
fsRrmMonitorDot11b = _FsRrmMonitorDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 6)
)


class _FsRrmDot11bMonitorEnable_Type(Integer32):
    """Custom type fsRrmDot11bMonitorEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsRrmDot11bMonitorEnable_Type.__name__ = "Integer32"
_FsRrmDot11bMonitorEnable_Object = MibScalar
fsRrmDot11bMonitorEnable = _FsRrmDot11bMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 6, 1),
    _FsRrmDot11bMonitorEnable_Type()
)
fsRrmDot11bMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bMonitorEnable.setStatus("current")


class _FsRrmDot11bChannelMonitorList_Type(Integer32):
    """Custom type fsRrmDot11bChannelMonitorList based on Integer32"""
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
        *(("all", 1),
          ("country", 2),
          ("dca", 3))
    )


_FsRrmDot11bChannelMonitorList_Type.__name__ = "Integer32"
_FsRrmDot11bChannelMonitorList_Object = MibScalar
fsRrmDot11bChannelMonitorList = _FsRrmDot11bChannelMonitorList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 6, 2),
    _FsRrmDot11bChannelMonitorList_Type()
)
fsRrmDot11bChannelMonitorList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bChannelMonitorList.setStatus("current")


class _FsRrmDot11bMonitorInterval_Type(Unsigned32):
    """Custom type fsRrmDot11bMonitorInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11bMonitorInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11bMonitorInterval_Object = MibScalar
fsRrmDot11bMonitorInterval = _FsRrmDot11bMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 6, 3),
    _FsRrmDot11bMonitorInterval_Type()
)
fsRrmDot11bMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bMonitorInterval.setStatus("current")


class _FsRrmDot11bCoverageMeasurementInterval_Type(Unsigned32):
    """Custom type fsRrmDot11bCoverageMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11bCoverageMeasurementInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11bCoverageMeasurementInterval_Object = MibScalar
fsRrmDot11bCoverageMeasurementInterval = _FsRrmDot11bCoverageMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 6, 4),
    _FsRrmDot11bCoverageMeasurementInterval_Type()
)
fsRrmDot11bCoverageMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bCoverageMeasurementInterval.setStatus("current")


class _FsRrmDot11bLoadMeasurementInterval_Type(Unsigned32):
    """Custom type fsRrmDot11bLoadMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11bLoadMeasurementInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11bLoadMeasurementInterval_Object = MibScalar
fsRrmDot11bLoadMeasurementInterval = _FsRrmDot11bLoadMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 6, 5),
    _FsRrmDot11bLoadMeasurementInterval_Type()
)
fsRrmDot11bLoadMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bLoadMeasurementInterval.setStatus("current")


class _FsRrmDot11bNoiseMeasurementInterval_Type(Unsigned32):
    """Custom type fsRrmDot11bNoiseMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11bNoiseMeasurementInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11bNoiseMeasurementInterval_Object = MibScalar
fsRrmDot11bNoiseMeasurementInterval = _FsRrmDot11bNoiseMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 6, 6),
    _FsRrmDot11bNoiseMeasurementInterval_Type()
)
fsRrmDot11bNoiseMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bNoiseMeasurementInterval.setStatus("current")


class _FsRrmDot11bSignalMeasurementInterval_Type(Unsigned32):
    """Custom type fsRrmDot11bSignalMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11bSignalMeasurementInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11bSignalMeasurementInterval_Object = MibScalar
fsRrmDot11bSignalMeasurementInterval = _FsRrmDot11bSignalMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 6, 7),
    _FsRrmDot11bSignalMeasurementInterval_Type()
)
fsRrmDot11bSignalMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bSignalMeasurementInterval.setStatus("current")


class _FsRrmDot11bNeighborMessageInterval_Type(Unsigned32):
    """Custom type fsRrmDot11bNeighborMessageInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_FsRrmDot11bNeighborMessageInterval_Type.__name__ = "Unsigned32"
_FsRrmDot11bNeighborMessageInterval_Object = MibScalar
fsRrmDot11bNeighborMessageInterval = _FsRrmDot11bNeighborMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 6, 8),
    _FsRrmDot11bNeighborMessageInterval_Type()
)
fsRrmDot11bNeighborMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bNeighborMessageInterval.setStatus("current")
_FsRrmFactoryDot11b_ObjectIdentity = ObjectIdentity
fsRrmFactoryDot11b = _FsRrmFactoryDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 7)
)


class _FsRrmDot11bSetFactoryDefault_Type(Integer32):
    """Custom type fsRrmDot11bSetFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_FsRrmDot11bSetFactoryDefault_Type.__name__ = "Integer32"
_FsRrmDot11bSetFactoryDefault_Object = MibScalar
fsRrmDot11bSetFactoryDefault = _FsRrmDot11bSetFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 3, 7, 1),
    _FsRrmDot11bSetFactoryDefault_Type()
)
fsRrmDot11bSetFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDot11bSetFactoryDefault.setStatus("current")
_FsRrmObjectsAP_ObjectIdentity = ObjectIdentity
fsRrmObjectsAP = _FsRrmObjectsAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4)
)


class _FsRrmAPIfSlotId_Type(Integer32):
    """Custom type fsRrmAPIfSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfSlotId_Type.__name__ = "Integer32"
_FsRrmAPIfSlotId_Object = MibScalar
fsRrmAPIfSlotId = _FsRrmAPIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 1),
    _FsRrmAPIfSlotId_Type()
)
fsRrmAPIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfSlotId.setStatus("current")


class _FsRrmAPName_Type(DisplayString):
    """Custom type fsRrmAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPName_Type.__name__ = "DisplayString"
_FsRrmAPName_Object = MibScalar
fsRrmAPName = _FsRrmAPName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 2),
    _FsRrmAPName_Type()
)
fsRrmAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPName.setStatus("current")
_FsRrmAPIfProfileThresholdConfigTable_Object = MibTable
fsRrmAPIfProfileThresholdConfigTable = _FsRrmAPIfProfileThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3)
)
if mibBuilder.loadTexts:
    fsRrmAPIfProfileThresholdConfigTable.setStatus("current")
_FsRrmAPIfProfileThresholdConfigEntry_Object = MibTableRow
fsRrmAPIfProfileThresholdConfigEntry = _FsRrmAPIfProfileThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1)
)
fsRrmAPIfProfileThresholdConfigEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfThresholdMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfThresholdRadioType"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfProfileThresholdConfigEntry.setStatus("current")


class _FsRrmAPIfThresholdRadioType_Type(Integer32):
    """Custom type fsRrmAPIfThresholdRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type80211a", 0),
          ("type80211b", 1))
    )


_FsRrmAPIfThresholdRadioType_Type.__name__ = "Integer32"
_FsRrmAPIfThresholdRadioType_Object = MibTableColumn
fsRrmAPIfThresholdRadioType = _FsRrmAPIfThresholdRadioType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 1),
    _FsRrmAPIfThresholdRadioType_Type()
)
fsRrmAPIfThresholdRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThresholdRadioType.setStatus("current")


class _FsRrmAPIfForeignInterferenceThreshold_Type(Integer32):
    """Custom type fsRrmAPIfForeignInterferenceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmAPIfForeignInterferenceThreshold_Type.__name__ = "Integer32"
_FsRrmAPIfForeignInterferenceThreshold_Object = MibTableColumn
fsRrmAPIfForeignInterferenceThreshold = _FsRrmAPIfForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 2),
    _FsRrmAPIfForeignInterferenceThreshold_Type()
)
fsRrmAPIfForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfForeignInterferenceThreshold.setStatus("current")


class _FsRrmAPIfForeignNoiseThreshold_Type(Integer32):
    """Custom type fsRrmAPIfForeignNoiseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_FsRrmAPIfForeignNoiseThreshold_Type.__name__ = "Integer32"
_FsRrmAPIfForeignNoiseThreshold_Object = MibTableColumn
fsRrmAPIfForeignNoiseThreshold = _FsRrmAPIfForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 3),
    _FsRrmAPIfForeignNoiseThreshold_Type()
)
fsRrmAPIfForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfForeignNoiseThreshold.setStatus("current")


class _FsRrmAPIfRFUtilizationThreshold_Type(Integer32):
    """Custom type fsRrmAPIfRFUtilizationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRrmAPIfRFUtilizationThreshold_Type.__name__ = "Integer32"
_FsRrmAPIfRFUtilizationThreshold_Object = MibTableColumn
fsRrmAPIfRFUtilizationThreshold = _FsRrmAPIfRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 4),
    _FsRrmAPIfRFUtilizationThreshold_Type()
)
fsRrmAPIfRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfRFUtilizationThreshold.setStatus("current")


class _FsRrmAPIfThroughputThreshold_Type(Unsigned32):
    """Custom type fsRrmAPIfThroughputThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000000),
    )


_FsRrmAPIfThroughputThreshold_Type.__name__ = "Unsigned32"
_FsRrmAPIfThroughputThreshold_Object = MibTableColumn
fsRrmAPIfThroughputThreshold = _FsRrmAPIfThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 5),
    _FsRrmAPIfThroughputThreshold_Type()
)
fsRrmAPIfThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputThreshold.setStatus("current")


class _FsRrmAPIfMobilesThreshold_Type(Integer32):
    """Custom type fsRrmAPIfMobilesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_FsRrmAPIfMobilesThreshold_Type.__name__ = "Integer32"
_FsRrmAPIfMobilesThreshold_Object = MibTableColumn
fsRrmAPIfMobilesThreshold = _FsRrmAPIfMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 6),
    _FsRrmAPIfMobilesThreshold_Type()
)
fsRrmAPIfMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfMobilesThreshold.setStatus("current")


class _FsRrmAPIfThresholdName_Type(DisplayString):
    """Custom type fsRrmAPIfThresholdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPIfThresholdName_Type.__name__ = "DisplayString"
_FsRrmAPIfThresholdName_Object = MibTableColumn
fsRrmAPIfThresholdName = _FsRrmAPIfThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 7),
    _FsRrmAPIfThresholdName_Type()
)
fsRrmAPIfThresholdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThresholdName.setStatus("current")
_FsRrmAPIfThresholdMacAddr_Type = MacAddress
_FsRrmAPIfThresholdMacAddr_Object = MibTableColumn
fsRrmAPIfThresholdMacAddr = _FsRrmAPIfThresholdMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 8),
    _FsRrmAPIfThresholdMacAddr_Type()
)
fsRrmAPIfThresholdMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThresholdMacAddr.setStatus("current")


class _FsRrmAPIfForeignGlobalConfig_Type(Integer32):
    """Custom type fsRrmAPIfForeignGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRrmAPIfForeignGlobalConfig_Type.__name__ = "Integer32"
_FsRrmAPIfForeignGlobalConfig_Object = MibTableColumn
fsRrmAPIfForeignGlobalConfig = _FsRrmAPIfForeignGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 9),
    _FsRrmAPIfForeignGlobalConfig_Type()
)
fsRrmAPIfForeignGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfForeignGlobalConfig.setStatus("current")


class _FsRrmAPIfNoiseGlobalConfig_Type(Integer32):
    """Custom type fsRrmAPIfNoiseGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRrmAPIfNoiseGlobalConfig_Type.__name__ = "Integer32"
_FsRrmAPIfNoiseGlobalConfig_Object = MibTableColumn
fsRrmAPIfNoiseGlobalConfig = _FsRrmAPIfNoiseGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 10),
    _FsRrmAPIfNoiseGlobalConfig_Type()
)
fsRrmAPIfNoiseGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfNoiseGlobalConfig.setStatus("current")


class _FsRrmAPIfRFUtilizationGlobalConfig_Type(Integer32):
    """Custom type fsRrmAPIfRFUtilizationGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRrmAPIfRFUtilizationGlobalConfig_Type.__name__ = "Integer32"
_FsRrmAPIfRFUtilizationGlobalConfig_Object = MibTableColumn
fsRrmAPIfRFUtilizationGlobalConfig = _FsRrmAPIfRFUtilizationGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 11),
    _FsRrmAPIfRFUtilizationGlobalConfig_Type()
)
fsRrmAPIfRFUtilizationGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfRFUtilizationGlobalConfig.setStatus("current")


class _FsRrmAPIfThroughputGlobalConfig_Type(Integer32):
    """Custom type fsRrmAPIfThroughputGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRrmAPIfThroughputGlobalConfig_Type.__name__ = "Integer32"
_FsRrmAPIfThroughputGlobalConfig_Object = MibTableColumn
fsRrmAPIfThroughputGlobalConfig = _FsRrmAPIfThroughputGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 12),
    _FsRrmAPIfThroughputGlobalConfig_Type()
)
fsRrmAPIfThroughputGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputGlobalConfig.setStatus("current")


class _FsRrmAPIfMobilesGlobalConfig_Type(Integer32):
    """Custom type fsRrmAPIfMobilesGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRrmAPIfMobilesGlobalConfig_Type.__name__ = "Integer32"
_FsRrmAPIfMobilesGlobalConfig_Object = MibTableColumn
fsRrmAPIfMobilesGlobalConfig = _FsRrmAPIfMobilesGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 3, 1, 13),
    _FsRrmAPIfMobilesGlobalConfig_Type()
)
fsRrmAPIfMobilesGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPIfMobilesGlobalConfig.setStatus("current")
_FsRrmAPIfLoadParametersTable_Object = MibTable
fsRrmAPIfLoadParametersTable = _FsRrmAPIfLoadParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4)
)
if mibBuilder.loadTexts:
    fsRrmAPIfLoadParametersTable.setStatus("current")
_FsRrmAPIfLoadParametersEntry_Object = MibTableRow
fsRrmAPIfLoadParametersEntry = _FsRrmAPIfLoadParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1)
)
fsRrmAPIfLoadParametersEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfLoadMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfLoadSlotId"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfLoadParametersEntry.setStatus("current")


class _FsRrmAPIfLoadRxUtilization_Type(Integer32):
    """Custom type fsRrmAPIfLoadRxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsRrmAPIfLoadRxUtilization_Type.__name__ = "Integer32"
_FsRrmAPIfLoadRxUtilization_Object = MibTableColumn
fsRrmAPIfLoadRxUtilization = _FsRrmAPIfLoadRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1, 1),
    _FsRrmAPIfLoadRxUtilization_Type()
)
fsRrmAPIfLoadRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfLoadRxUtilization.setStatus("current")


class _FsRrmAPIfLoadTxUtilization_Type(Integer32):
    """Custom type fsRrmAPIfLoadTxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsRrmAPIfLoadTxUtilization_Type.__name__ = "Integer32"
_FsRrmAPIfLoadTxUtilization_Object = MibTableColumn
fsRrmAPIfLoadTxUtilization = _FsRrmAPIfLoadTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1, 2),
    _FsRrmAPIfLoadTxUtilization_Type()
)
fsRrmAPIfLoadTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfLoadTxUtilization.setStatus("current")


class _FsRrmAPIfLoadChannelUtilization_Type(Integer32):
    """Custom type fsRrmAPIfLoadChannelUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsRrmAPIfLoadChannelUtilization_Type.__name__ = "Integer32"
_FsRrmAPIfLoadChannelUtilization_Object = MibTableColumn
fsRrmAPIfLoadChannelUtilization = _FsRrmAPIfLoadChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1, 3),
    _FsRrmAPIfLoadChannelUtilization_Type()
)
fsRrmAPIfLoadChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfLoadChannelUtilization.setStatus("current")
_FsRrmAPIfLoadNumOfClients_Type = Integer32
_FsRrmAPIfLoadNumOfClients_Object = MibTableColumn
fsRrmAPIfLoadNumOfClients = _FsRrmAPIfLoadNumOfClients_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1, 4),
    _FsRrmAPIfLoadNumOfClients_Type()
)
fsRrmAPIfLoadNumOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfLoadNumOfClients.setStatus("current")
_FsRrmAPIfPoorSNRClients_Type = Integer32
_FsRrmAPIfPoorSNRClients_Object = MibTableColumn
fsRrmAPIfPoorSNRClients = _FsRrmAPIfPoorSNRClients_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1, 5),
    _FsRrmAPIfPoorSNRClients_Type()
)
fsRrmAPIfPoorSNRClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfPoorSNRClients.setStatus("current")


class _FsRrmAPIfLoadName_Type(DisplayString):
    """Custom type fsRrmAPIfLoadName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPIfLoadName_Type.__name__ = "DisplayString"
_FsRrmAPIfLoadName_Object = MibTableColumn
fsRrmAPIfLoadName = _FsRrmAPIfLoadName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1, 6),
    _FsRrmAPIfLoadName_Type()
)
fsRrmAPIfLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfLoadName.setStatus("current")
_FsRrmAPIfLoadMacAddr_Type = MacAddress
_FsRrmAPIfLoadMacAddr_Object = MibTableColumn
fsRrmAPIfLoadMacAddr = _FsRrmAPIfLoadMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1, 7),
    _FsRrmAPIfLoadMacAddr_Type()
)
fsRrmAPIfLoadMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfLoadMacAddr.setStatus("current")


class _FsRrmAPIfLoadSlotId_Type(Integer32):
    """Custom type fsRrmAPIfLoadSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfLoadSlotId_Type.__name__ = "Integer32"
_FsRrmAPIfLoadSlotId_Object = MibTableColumn
fsRrmAPIfLoadSlotId = _FsRrmAPIfLoadSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1, 8),
    _FsRrmAPIfLoadSlotId_Type()
)
fsRrmAPIfLoadSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfLoadSlotId.setStatus("current")
_FsRrmAPIfThroughput_Type = Integer32
_FsRrmAPIfThroughput_Object = MibTableColumn
fsRrmAPIfThroughput = _FsRrmAPIfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 4, 1, 9),
    _FsRrmAPIfThroughput_Type()
)
fsRrmAPIfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThroughput.setStatus("current")
_FsRrmAPIfChannelInterferenceInfoTable_Object = MibTable
fsRrmAPIfChannelInterferenceInfoTable = _FsRrmAPIfChannelInterferenceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 5)
)
if mibBuilder.loadTexts:
    fsRrmAPIfChannelInterferenceInfoTable.setStatus("current")
_FsRrmAPIfChannelInterferenceInfoEntry_Object = MibTableRow
fsRrmAPIfChannelInterferenceInfoEntry = _FsRrmAPIfChannelInterferenceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 5, 1)
)
fsRrmAPIfChannelInterferenceInfoEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfInterferenceMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfInterferenceSlotId"),
    (0, "FS-RRM-MIB", "fsRrmAPIfInterferenceChannelNo"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfChannelInterferenceInfoEntry.setStatus("current")
_FsRrmAPIfInterferenceChannelNo_Type = Integer32
_FsRrmAPIfInterferenceChannelNo_Object = MibTableColumn
fsRrmAPIfInterferenceChannelNo = _FsRrmAPIfInterferenceChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 5, 1, 1),
    _FsRrmAPIfInterferenceChannelNo_Type()
)
fsRrmAPIfInterferenceChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfInterferenceChannelNo.setStatus("current")
_FsRrmAPIfInterferencePower_Type = Integer32
_FsRrmAPIfInterferencePower_Object = MibTableColumn
fsRrmAPIfInterferencePower = _FsRrmAPIfInterferencePower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 5, 1, 2),
    _FsRrmAPIfInterferencePower_Type()
)
fsRrmAPIfInterferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfInterferencePower.setStatus("current")


class _FsRrmAPIfInterferenceUtilization_Type(Integer32):
    """Custom type fsRrmAPIfInterferenceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsRrmAPIfInterferenceUtilization_Type.__name__ = "Integer32"
_FsRrmAPIfInterferenceUtilization_Object = MibTableColumn
fsRrmAPIfInterferenceUtilization = _FsRrmAPIfInterferenceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 5, 1, 3),
    _FsRrmAPIfInterferenceUtilization_Type()
)
fsRrmAPIfInterferenceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfInterferenceUtilization.setStatus("current")


class _FsRrmAPIfInterferenceName_Type(DisplayString):
    """Custom type fsRrmAPIfInterferenceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPIfInterferenceName_Type.__name__ = "DisplayString"
_FsRrmAPIfInterferenceName_Object = MibTableColumn
fsRrmAPIfInterferenceName = _FsRrmAPIfInterferenceName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 5, 1, 4),
    _FsRrmAPIfInterferenceName_Type()
)
fsRrmAPIfInterferenceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfInterferenceName.setStatus("current")
_FsRrmAPIfInterferenceMacAddr_Type = MacAddress
_FsRrmAPIfInterferenceMacAddr_Object = MibTableColumn
fsRrmAPIfInterferenceMacAddr = _FsRrmAPIfInterferenceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 5, 1, 5),
    _FsRrmAPIfInterferenceMacAddr_Type()
)
fsRrmAPIfInterferenceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfInterferenceMacAddr.setStatus("current")


class _FsRrmAPIfInterferenceSlotId_Type(Integer32):
    """Custom type fsRrmAPIfInterferenceSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfInterferenceSlotId_Type.__name__ = "Integer32"
_FsRrmAPIfInterferenceSlotId_Object = MibTableColumn
fsRrmAPIfInterferenceSlotId = _FsRrmAPIfInterferenceSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 5, 1, 6),
    _FsRrmAPIfInterferenceSlotId_Type()
)
fsRrmAPIfInterferenceSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfInterferenceSlotId.setStatus("current")
_FsRrmAPIfChannelNoiseInfoTable_Object = MibTable
fsRrmAPIfChannelNoiseInfoTable = _FsRrmAPIfChannelNoiseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 6)
)
if mibBuilder.loadTexts:
    fsRrmAPIfChannelNoiseInfoTable.setStatus("current")
_FsRrmAPIfChannelNoiseInfoEntry_Object = MibTableRow
fsRrmAPIfChannelNoiseInfoEntry = _FsRrmAPIfChannelNoiseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 6, 1)
)
fsRrmAPIfChannelNoiseInfoEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfNoiseMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfNoiseSlotId"),
    (0, "FS-RRM-MIB", "fsRrmAPIfNoiseChannelNo"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfChannelNoiseInfoEntry.setStatus("current")
_FsRrmAPIfNoiseChannelNo_Type = Integer32
_FsRrmAPIfNoiseChannelNo_Object = MibTableColumn
fsRrmAPIfNoiseChannelNo = _FsRrmAPIfNoiseChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 6, 1, 1),
    _FsRrmAPIfNoiseChannelNo_Type()
)
fsRrmAPIfNoiseChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfNoiseChannelNo.setStatus("current")
_FsRrmAPIfDBNoisePower_Type = Integer32
_FsRrmAPIfDBNoisePower_Object = MibTableColumn
fsRrmAPIfDBNoisePower = _FsRrmAPIfDBNoisePower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 6, 1, 2),
    _FsRrmAPIfDBNoisePower_Type()
)
fsRrmAPIfDBNoisePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfDBNoisePower.setStatus("current")


class _FsRrmAPIfNoiseName_Type(DisplayString):
    """Custom type fsRrmAPIfNoiseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPIfNoiseName_Type.__name__ = "DisplayString"
_FsRrmAPIfNoiseName_Object = MibTableColumn
fsRrmAPIfNoiseName = _FsRrmAPIfNoiseName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 6, 1, 3),
    _FsRrmAPIfNoiseName_Type()
)
fsRrmAPIfNoiseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfNoiseName.setStatus("current")
_FsRrmAPIfNoiseMacAddr_Type = MacAddress
_FsRrmAPIfNoiseMacAddr_Object = MibTableColumn
fsRrmAPIfNoiseMacAddr = _FsRrmAPIfNoiseMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 6, 1, 4),
    _FsRrmAPIfNoiseMacAddr_Type()
)
fsRrmAPIfNoiseMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfNoiseMacAddr.setStatus("current")


class _FsRrmAPIfNoiseSlotId_Type(Integer32):
    """Custom type fsRrmAPIfNoiseSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfNoiseSlotId_Type.__name__ = "Integer32"
_FsRrmAPIfNoiseSlotId_Object = MibTableColumn
fsRrmAPIfNoiseSlotId = _FsRrmAPIfNoiseSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 6, 1, 5),
    _FsRrmAPIfNoiseSlotId_Type()
)
fsRrmAPIfNoiseSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfNoiseSlotId.setStatus("current")
_FsRrmAPIfProfileStateTable_Object = MibTable
fsRrmAPIfProfileStateTable = _FsRrmAPIfProfileStateTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7)
)
if mibBuilder.loadTexts:
    fsRrmAPIfProfileStateTable.setStatus("current")
_FsRrmAPIfProfileStateEntry_Object = MibTableRow
fsRrmAPIfProfileStateEntry = _FsRrmAPIfProfileStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7, 1)
)
fsRrmAPIfProfileStateEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfProfileMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfProfileSlotId"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfProfileStateEntry.setStatus("current")
_FsRrmAPIfLoadProfileState_Type = ProfileState
_FsRrmAPIfLoadProfileState_Object = MibTableColumn
fsRrmAPIfLoadProfileState = _FsRrmAPIfLoadProfileState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7, 1, 1),
    _FsRrmAPIfLoadProfileState_Type()
)
fsRrmAPIfLoadProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfLoadProfileState.setStatus("current")
_FsRrmAPIfInterferenceProfileState_Type = ProfileState
_FsRrmAPIfInterferenceProfileState_Object = MibTableColumn
fsRrmAPIfInterferenceProfileState = _FsRrmAPIfInterferenceProfileState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7, 1, 2),
    _FsRrmAPIfInterferenceProfileState_Type()
)
fsRrmAPIfInterferenceProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfInterferenceProfileState.setStatus("current")
_FsRrmAPIfNoiseProfileState_Type = ProfileState
_FsRrmAPIfNoiseProfileState_Object = MibTableColumn
fsRrmAPIfNoiseProfileState = _FsRrmAPIfNoiseProfileState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7, 1, 3),
    _FsRrmAPIfNoiseProfileState_Type()
)
fsRrmAPIfNoiseProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfNoiseProfileState.setStatus("current")
_FsRrmAPIfCoverageProfileState_Type = ProfileState
_FsRrmAPIfCoverageProfileState_Object = MibTableColumn
fsRrmAPIfCoverageProfileState = _FsRrmAPIfCoverageProfileState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7, 1, 4),
    _FsRrmAPIfCoverageProfileState_Type()
)
fsRrmAPIfCoverageProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfCoverageProfileState.setStatus("current")
_FsRrmAPIfPerformanceProfileState_Type = ProfileState
_FsRrmAPIfPerformanceProfileState_Object = MibTableColumn
fsRrmAPIfPerformanceProfileState = _FsRrmAPIfPerformanceProfileState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7, 1, 5),
    _FsRrmAPIfPerformanceProfileState_Type()
)
fsRrmAPIfPerformanceProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfPerformanceProfileState.setStatus("current")


class _FsRrmAPIfProfileName_Type(DisplayString):
    """Custom type fsRrmAPIfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPIfProfileName_Type.__name__ = "DisplayString"
_FsRrmAPIfProfileName_Object = MibTableColumn
fsRrmAPIfProfileName = _FsRrmAPIfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7, 1, 6),
    _FsRrmAPIfProfileName_Type()
)
fsRrmAPIfProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfProfileName.setStatus("current")
_FsRrmAPIfProfileMacAddr_Type = MacAddress
_FsRrmAPIfProfileMacAddr_Object = MibTableColumn
fsRrmAPIfProfileMacAddr = _FsRrmAPIfProfileMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7, 1, 7),
    _FsRrmAPIfProfileMacAddr_Type()
)
fsRrmAPIfProfileMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfProfileMacAddr.setStatus("current")


class _FsRrmAPIfProfileSlotId_Type(Integer32):
    """Custom type fsRrmAPIfProfileSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfProfileSlotId_Type.__name__ = "Integer32"
_FsRrmAPIfProfileSlotId_Object = MibTableColumn
fsRrmAPIfProfileSlotId = _FsRrmAPIfProfileSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 7, 1, 8),
    _FsRrmAPIfProfileSlotId_Type()
)
fsRrmAPIfProfileSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfProfileSlotId.setStatus("current")
_FsRrmAPIfRxNeighborsTable_Object = MibTable
fsRrmAPIfRxNeighborsTable = _FsRrmAPIfRxNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8)
)
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborsTable.setStatus("current")
_FsRrmAPIfRxNeighborsEntry_Object = MibTableRow
fsRrmAPIfRxNeighborsEntry = _FsRrmAPIfRxNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1)
)
fsRrmAPIfRxNeighborsEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfRxNeighborMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfRxNeighborSlotId"),
    (0, "FS-RRM-MIB", "fsRrmAPIfRxNeighborMacAddress"),
    (0, "FS-RRM-MIB", "fsRrmAPIfRxNeighborSlot"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborsEntry.setStatus("current")
_FsRrmAPIfRxNeighborMacAddress_Type = MacAddress
_FsRrmAPIfRxNeighborMacAddress_Object = MibTableColumn
fsRrmAPIfRxNeighborMacAddress = _FsRrmAPIfRxNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 1),
    _FsRrmAPIfRxNeighborMacAddress_Type()
)
fsRrmAPIfRxNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborMacAddress.setStatus("current")
_FsRrmAPIfRxNeighborSlot_Type = Integer32
_FsRrmAPIfRxNeighborSlot_Object = MibTableColumn
fsRrmAPIfRxNeighborSlot = _FsRrmAPIfRxNeighborSlot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 2),
    _FsRrmAPIfRxNeighborSlot_Type()
)
fsRrmAPIfRxNeighborSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborSlot.setStatus("current")
_FsRrmAPIfRxNeighborIpAddress_Type = IpAddress
_FsRrmAPIfRxNeighborIpAddress_Object = MibTableColumn
fsRrmAPIfRxNeighborIpAddress = _FsRrmAPIfRxNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 3),
    _FsRrmAPIfRxNeighborIpAddress_Type()
)
fsRrmAPIfRxNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborIpAddress.setStatus("current")
_FsRrmAPIfRxNeighborRSSI_Type = Integer32
_FsRrmAPIfRxNeighborRSSI_Object = MibTableColumn
fsRrmAPIfRxNeighborRSSI = _FsRrmAPIfRxNeighborRSSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 4),
    _FsRrmAPIfRxNeighborRSSI_Type()
)
fsRrmAPIfRxNeighborRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborRSSI.setStatus("current")
_FsRrmAPIfRxNeighborSNR_Type = Integer32
_FsRrmAPIfRxNeighborSNR_Object = MibTableColumn
fsRrmAPIfRxNeighborSNR = _FsRrmAPIfRxNeighborSNR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 5),
    _FsRrmAPIfRxNeighborSNR_Type()
)
fsRrmAPIfRxNeighborSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborSNR.setStatus("current")
_FsRrmAPIfRxNeighborChannel_Type = Integer32
_FsRrmAPIfRxNeighborChannel_Object = MibTableColumn
fsRrmAPIfRxNeighborChannel = _FsRrmAPIfRxNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 6),
    _FsRrmAPIfRxNeighborChannel_Type()
)
fsRrmAPIfRxNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborChannel.setStatus("current")


class _FsRrmAPIfRxNeighborChannelWidth_Type(Integer32):
    """Custom type fsRrmAPIfRxNeighborChannelWidth based on Integer32"""
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("aboveforty", 4),
          ("belowforty", 5))
    )


_FsRrmAPIfRxNeighborChannelWidth_Type.__name__ = "Integer32"
_FsRrmAPIfRxNeighborChannelWidth_Object = MibTableColumn
fsRrmAPIfRxNeighborChannelWidth = _FsRrmAPIfRxNeighborChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 7),
    _FsRrmAPIfRxNeighborChannelWidth_Type()
)
fsRrmAPIfRxNeighborChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborChannelWidth.setStatus("current")


class _FsRrmAPIfRxNeighborName_Type(DisplayString):
    """Custom type fsRrmAPIfRxNeighborName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPIfRxNeighborName_Type.__name__ = "DisplayString"
_FsRrmAPIfRxNeighborName_Object = MibTableColumn
fsRrmAPIfRxNeighborName = _FsRrmAPIfRxNeighborName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 8),
    _FsRrmAPIfRxNeighborName_Type()
)
fsRrmAPIfRxNeighborName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborName.setStatus("current")
_FsRrmAPIfRxNeighborMacAddr_Type = MacAddress
_FsRrmAPIfRxNeighborMacAddr_Object = MibTableColumn
fsRrmAPIfRxNeighborMacAddr = _FsRrmAPIfRxNeighborMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 9),
    _FsRrmAPIfRxNeighborMacAddr_Type()
)
fsRrmAPIfRxNeighborMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborMacAddr.setStatus("current")


class _FsRrmAPIfRxNeighborSlotId_Type(Integer32):
    """Custom type fsRrmAPIfRxNeighborSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfRxNeighborSlotId_Type.__name__ = "Integer32"
_FsRrmAPIfRxNeighborSlotId_Object = MibTableColumn
fsRrmAPIfRxNeighborSlotId = _FsRrmAPIfRxNeighborSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 8, 1, 10),
    _FsRrmAPIfRxNeighborSlotId_Type()
)
fsRrmAPIfRxNeighborSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRxNeighborSlotId.setStatus("current")
_FsRrmAPIfStationRSSICoverageInfoTable_Object = MibTable
fsRrmAPIfStationRSSICoverageInfoTable = _FsRrmAPIfStationRSSICoverageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 9)
)
if mibBuilder.loadTexts:
    fsRrmAPIfStationRSSICoverageInfoTable.setStatus("current")
_FsRrmAPIfStationRSSICoverageInfoEntry_Object = MibTableRow
fsRrmAPIfStationRSSICoverageInfoEntry = _FsRrmAPIfStationRSSICoverageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 9, 1)
)
fsRrmAPIfStationRSSICoverageInfoEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfStationRSSIMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfStationRSSISlotId"),
    (0, "FS-RRM-MIB", "fsRrmAPIfStationRSSICoverageIndex"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfStationRSSICoverageInfoEntry.setStatus("current")
_FsRrmAPIfStationRSSICoverageIndex_Type = Integer32
_FsRrmAPIfStationRSSICoverageIndex_Object = MibTableColumn
fsRrmAPIfStationRSSICoverageIndex = _FsRrmAPIfStationRSSICoverageIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 9, 1, 1),
    _FsRrmAPIfStationRSSICoverageIndex_Type()
)
fsRrmAPIfStationRSSICoverageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationRSSICoverageIndex.setStatus("current")
_FsRrmAPIfRSSILevel_Type = Integer32
_FsRrmAPIfRSSILevel_Object = MibTableColumn
fsRrmAPIfRSSILevel = _FsRrmAPIfRSSILevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 9, 1, 2),
    _FsRrmAPIfRSSILevel_Type()
)
fsRrmAPIfRSSILevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRSSILevel.setStatus("current")
_FsRrmAPIfStationCountOnRSSI_Type = Integer32
_FsRrmAPIfStationCountOnRSSI_Object = MibTableColumn
fsRrmAPIfStationCountOnRSSI = _FsRrmAPIfStationCountOnRSSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 9, 1, 3),
    _FsRrmAPIfStationCountOnRSSI_Type()
)
fsRrmAPIfStationCountOnRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationCountOnRSSI.setStatus("current")


class _FsRrmAPIfStationRSSIName_Type(DisplayString):
    """Custom type fsRrmAPIfStationRSSIName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPIfStationRSSIName_Type.__name__ = "DisplayString"
_FsRrmAPIfStationRSSIName_Object = MibTableColumn
fsRrmAPIfStationRSSIName = _FsRrmAPIfStationRSSIName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 9, 1, 4),
    _FsRrmAPIfStationRSSIName_Type()
)
fsRrmAPIfStationRSSIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationRSSIName.setStatus("current")
_FsRrmAPIfStationRSSIMacAddr_Type = MacAddress
_FsRrmAPIfStationRSSIMacAddr_Object = MibTableColumn
fsRrmAPIfStationRSSIMacAddr = _FsRrmAPIfStationRSSIMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 9, 1, 5),
    _FsRrmAPIfStationRSSIMacAddr_Type()
)
fsRrmAPIfStationRSSIMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationRSSIMacAddr.setStatus("current")


class _FsRrmAPIfStationRSSISlotId_Type(Integer32):
    """Custom type fsRrmAPIfStationRSSISlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfStationRSSISlotId_Type.__name__ = "Integer32"
_FsRrmAPIfStationRSSISlotId_Object = MibTableColumn
fsRrmAPIfStationRSSISlotId = _FsRrmAPIfStationRSSISlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 9, 1, 6),
    _FsRrmAPIfStationRSSISlotId_Type()
)
fsRrmAPIfStationRSSISlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationRSSISlotId.setStatus("current")
_FsRrmAPIfStationSNRCoverageInfoTable_Object = MibTable
fsRrmAPIfStationSNRCoverageInfoTable = _FsRrmAPIfStationSNRCoverageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 10)
)
if mibBuilder.loadTexts:
    fsRrmAPIfStationSNRCoverageInfoTable.setStatus("current")
_FsRrmAPIfStationSNRCoverageInfoEntry_Object = MibTableRow
fsRrmAPIfStationSNRCoverageInfoEntry = _FsRrmAPIfStationSNRCoverageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 10, 1)
)
fsRrmAPIfStationSNRCoverageInfoEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfStationSNRMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfStationSNRSlotId"),
    (0, "FS-RRM-MIB", "fsRrmAPIfStationSNRCoverageIndex"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfStationSNRCoverageInfoEntry.setStatus("current")
_FsRrmAPIfStationSNRCoverageIndex_Type = Integer32
_FsRrmAPIfStationSNRCoverageIndex_Object = MibTableColumn
fsRrmAPIfStationSNRCoverageIndex = _FsRrmAPIfStationSNRCoverageIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 10, 1, 1),
    _FsRrmAPIfStationSNRCoverageIndex_Type()
)
fsRrmAPIfStationSNRCoverageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationSNRCoverageIndex.setStatus("current")
_FsRrmAPIfSNRLevel_Type = Integer32
_FsRrmAPIfSNRLevel_Object = MibTableColumn
fsRrmAPIfSNRLevel = _FsRrmAPIfSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 10, 1, 2),
    _FsRrmAPIfSNRLevel_Type()
)
fsRrmAPIfSNRLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfSNRLevel.setStatus("current")
_FsRrmAPIfStationCountOnSNR_Type = Integer32
_FsRrmAPIfStationCountOnSNR_Object = MibTableColumn
fsRrmAPIfStationCountOnSNR = _FsRrmAPIfStationCountOnSNR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 10, 1, 3),
    _FsRrmAPIfStationCountOnSNR_Type()
)
fsRrmAPIfStationCountOnSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationCountOnSNR.setStatus("current")


class _FsRrmAPIfStationSNRName_Type(DisplayString):
    """Custom type fsRrmAPIfStationSNRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPIfStationSNRName_Type.__name__ = "DisplayString"
_FsRrmAPIfStationSNRName_Object = MibTableColumn
fsRrmAPIfStationSNRName = _FsRrmAPIfStationSNRName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 10, 1, 4),
    _FsRrmAPIfStationSNRName_Type()
)
fsRrmAPIfStationSNRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationSNRName.setStatus("current")
_FsRrmAPIfStationSNRMacAddr_Type = MacAddress
_FsRrmAPIfStationSNRMacAddr_Object = MibTableColumn
fsRrmAPIfStationSNRMacAddr = _FsRrmAPIfStationSNRMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 10, 1, 5),
    _FsRrmAPIfStationSNRMacAddr_Type()
)
fsRrmAPIfStationSNRMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationSNRMacAddr.setStatus("current")


class _FsRrmAPIfStationSNRSlotId_Type(Integer32):
    """Custom type fsRrmAPIfStationSNRSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfStationSNRSlotId_Type.__name__ = "Integer32"
_FsRrmAPIfStationSNRSlotId_Object = MibTableColumn
fsRrmAPIfStationSNRSlotId = _FsRrmAPIfStationSNRSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 10, 1, 6),
    _FsRrmAPIfStationSNRSlotId_Type()
)
fsRrmAPIfStationSNRSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfStationSNRSlotId.setStatus("current")
_FsRrmAPIfRecommendedRFParametersTable_Object = MibTable
fsRrmAPIfRecommendedRFParametersTable = _FsRrmAPIfRecommendedRFParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 11)
)
if mibBuilder.loadTexts:
    fsRrmAPIfRecommendedRFParametersTable.setStatus("current")
_FsRrmAPIfRecommendedRFParametersEntry_Object = MibTableRow
fsRrmAPIfRecommendedRFParametersEntry = _FsRrmAPIfRecommendedRFParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 11, 1)
)
fsRrmAPIfRecommendedRFParametersEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfRecommendedMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfRecommendedSlotId"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfRecommendedRFParametersEntry.setStatus("current")
_FsRrmAPIfRecommendedChannelNumber_Type = Integer32
_FsRrmAPIfRecommendedChannelNumber_Object = MibTableColumn
fsRrmAPIfRecommendedChannelNumber = _FsRrmAPIfRecommendedChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 11, 1, 1),
    _FsRrmAPIfRecommendedChannelNumber_Type()
)
fsRrmAPIfRecommendedChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRecommendedChannelNumber.setStatus("current")
_FsRrmAPIfRecommendedTxPowerLevel_Type = Integer32
_FsRrmAPIfRecommendedTxPowerLevel_Object = MibTableColumn
fsRrmAPIfRecommendedTxPowerLevel = _FsRrmAPIfRecommendedTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 11, 1, 2),
    _FsRrmAPIfRecommendedTxPowerLevel_Type()
)
fsRrmAPIfRecommendedTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRecommendedTxPowerLevel.setStatus("current")
_FsRrmAPIfRecommendedRTSThreshold_Type = Integer32
_FsRrmAPIfRecommendedRTSThreshold_Object = MibTableColumn
fsRrmAPIfRecommendedRTSThreshold = _FsRrmAPIfRecommendedRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 11, 1, 3),
    _FsRrmAPIfRecommendedRTSThreshold_Type()
)
fsRrmAPIfRecommendedRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRecommendedRTSThreshold.setStatus("current")
_FsRrmAPIfRecommendedFragmentationThreshold_Type = Integer32
_FsRrmAPIfRecommendedFragmentationThreshold_Object = MibTableColumn
fsRrmAPIfRecommendedFragmentationThreshold = _FsRrmAPIfRecommendedFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 11, 1, 4),
    _FsRrmAPIfRecommendedFragmentationThreshold_Type()
)
fsRrmAPIfRecommendedFragmentationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRecommendedFragmentationThreshold.setStatus("current")


class _FsRrmAPIfRecommendedName_Type(DisplayString):
    """Custom type fsRrmAPIfRecommendedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPIfRecommendedName_Type.__name__ = "DisplayString"
_FsRrmAPIfRecommendedName_Object = MibTableColumn
fsRrmAPIfRecommendedName = _FsRrmAPIfRecommendedName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 11, 1, 5),
    _FsRrmAPIfRecommendedName_Type()
)
fsRrmAPIfRecommendedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRecommendedName.setStatus("current")
_FsRrmAPIfRecommendedMacAddr_Type = MacAddress
_FsRrmAPIfRecommendedMacAddr_Object = MibTableColumn
fsRrmAPIfRecommendedMacAddr = _FsRrmAPIfRecommendedMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 11, 1, 6),
    _FsRrmAPIfRecommendedMacAddr_Type()
)
fsRrmAPIfRecommendedMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRecommendedMacAddr.setStatus("current")


class _FsRrmAPIfRecommendedSlotId_Type(Integer32):
    """Custom type fsRrmAPIfRecommendedSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfRecommendedSlotId_Type.__name__ = "Integer32"
_FsRrmAPIfRecommendedSlotId_Object = MibTableColumn
fsRrmAPIfRecommendedSlotId = _FsRrmAPIfRecommendedSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 11, 1, 7),
    _FsRrmAPIfRecommendedSlotId_Type()
)
fsRrmAPIfRecommendedSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfRecommendedSlotId.setStatus("current")
_FsRrmAPRadioTable_Object = MibTable
fsRrmAPRadioTable = _FsRrmAPRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 12)
)
if mibBuilder.loadTexts:
    fsRrmAPRadioTable.setStatus("current")
_FsRrmAPRadioEntry_Object = MibTableRow
fsRrmAPRadioEntry = _FsRrmAPRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 12, 1)
)
fsRrmAPRadioEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPRadioID"),
)
if mibBuilder.loadTexts:
    fsRrmAPRadioEntry.setStatus("current")


class _FsRrmAPRadioID_Type(Integer32):
    """Custom type fsRrmAPRadioID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPRadioID_Type.__name__ = "Integer32"
_FsRrmAPRadioID_Object = MibTableColumn
fsRrmAPRadioID = _FsRrmAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 12, 1, 1),
    _FsRrmAPRadioID_Type()
)
fsRrmAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPRadioID.setStatus("current")


class _FsRrmAPRadioType_Type(Integer32):
    """Custom type fsRrmAPRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type80211a", 0),
          ("type80211b", 1))
    )


_FsRrmAPRadioType_Type.__name__ = "Integer32"
_FsRrmAPRadioType_Object = MibTableColumn
fsRrmAPRadioType = _FsRrmAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 12, 1, 2),
    _FsRrmAPRadioType_Type()
)
fsRrmAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPRadioType.setStatus("current")


class _FsRrmAPRealName_Type(DisplayString):
    """Custom type fsRrmAPRealName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRrmAPRealName_Type.__name__ = "DisplayString"
_FsRrmAPRealName_Object = MibTableColumn
fsRrmAPRealName = _FsRrmAPRealName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 12, 1, 3),
    _FsRrmAPRealName_Type()
)
fsRrmAPRealName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPRealName.setStatus("current")
_FsRrmAPMacAddr_Type = MacAddress
_FsRrmAPMacAddr_Object = MibTableColumn
fsRrmAPMacAddr = _FsRrmAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 12, 1, 4),
    _FsRrmAPMacAddr_Type()
)
fsRrmAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPMacAddr.setStatus("current")
_FsRrmAPIfThroughputParametersTable_Object = MibTable
fsRrmAPIfThroughputParametersTable = _FsRrmAPIfThroughputParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 13)
)
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputParametersTable.setStatus("current")
_FsRrmAPIfThroughputParametersEntry_Object = MibTableRow
fsRrmAPIfThroughputParametersEntry = _FsRrmAPIfThroughputParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 13, 1)
)
fsRrmAPIfThroughputParametersEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPIfThroughputMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPIfThroughputSlotId"),
)
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputParametersEntry.setStatus("current")
_FsRrmAPIfThroughputMacAddr_Type = MacAddress
_FsRrmAPIfThroughputMacAddr_Object = MibTableColumn
fsRrmAPIfThroughputMacAddr = _FsRrmAPIfThroughputMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 13, 1, 1),
    _FsRrmAPIfThroughputMacAddr_Type()
)
fsRrmAPIfThroughputMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputMacAddr.setStatus("current")


class _FsRrmAPIfThroughputSlotId_Type(Integer32):
    """Custom type fsRrmAPIfThroughputSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPIfThroughputSlotId_Type.__name__ = "Integer32"
_FsRrmAPIfThroughputSlotId_Object = MibTableColumn
fsRrmAPIfThroughputSlotId = _FsRrmAPIfThroughputSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 13, 1, 2),
    _FsRrmAPIfThroughputSlotId_Type()
)
fsRrmAPIfThroughputSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputSlotId.setStatus("current")


class _FsRrmAPIfThroughputAPName_Type(DisplayString):
    """Custom type fsRrmAPIfThroughputAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsRrmAPIfThroughputAPName_Type.__name__ = "DisplayString"
_FsRrmAPIfThroughputAPName_Object = MibTableColumn
fsRrmAPIfThroughputAPName = _FsRrmAPIfThroughputAPName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 13, 1, 3),
    _FsRrmAPIfThroughputAPName_Type()
)
fsRrmAPIfThroughputAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputAPName.setStatus("current")
_FsRrmAPIfThroughputRx_Type = Integer32
_FsRrmAPIfThroughputRx_Object = MibTableColumn
fsRrmAPIfThroughputRx = _FsRrmAPIfThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 13, 1, 4),
    _FsRrmAPIfThroughputRx_Type()
)
fsRrmAPIfThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputRx.setStatus("current")
_FsRrmAPIfThroughputTx_Type = Integer32
_FsRrmAPIfThroughputTx_Object = MibTableColumn
fsRrmAPIfThroughputTx = _FsRrmAPIfThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 13, 1, 5),
    _FsRrmAPIfThroughputTx_Type()
)
fsRrmAPIfThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputTx.setStatus("current")
_FsRrmAPIfThroughputTotal_Type = Integer32
_FsRrmAPIfThroughputTotal_Object = MibTableColumn
fsRrmAPIfThroughputTotal = _FsRrmAPIfThroughputTotal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 13, 1, 6),
    _FsRrmAPIfThroughputTotal_Type()
)
fsRrmAPIfThroughputTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPIfThroughputTotal.setStatus("current")
_FsRrmAPSnrBSSIDTable_Object = MibTable
fsRrmAPSnrBSSIDTable = _FsRrmAPSnrBSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14)
)
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDTable.setStatus("current")
_FsRrmAPSnrBSSIDEntry_Object = MibTableRow
fsRrmAPSnrBSSIDEntry = _FsRrmAPSnrBSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14, 1)
)
fsRrmAPSnrBSSIDEntry.setIndexNames(
    (0, "FS-RRM-MIB", "fsRrmAPSnrBSSIDMacAddr"),
    (0, "FS-RRM-MIB", "fsRrmAPSnrBSSIDSlotId"),
)
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDEntry.setStatus("current")
_FsRrmAPSnrBSSIDMacAddr_Type = MacAddress
_FsRrmAPSnrBSSIDMacAddr_Object = MibTableColumn
fsRrmAPSnrBSSIDMacAddr = _FsRrmAPSnrBSSIDMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14, 1, 1),
    _FsRrmAPSnrBSSIDMacAddr_Type()
)
fsRrmAPSnrBSSIDMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDMacAddr.setStatus("current")


class _FsRrmAPSnrBSSIDSlotId_Type(Integer32):
    """Custom type fsRrmAPSnrBSSIDSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsRrmAPSnrBSSIDSlotId_Type.__name__ = "Integer32"
_FsRrmAPSnrBSSIDSlotId_Object = MibTableColumn
fsRrmAPSnrBSSIDSlotId = _FsRrmAPSnrBSSIDSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14, 1, 2),
    _FsRrmAPSnrBSSIDSlotId_Type()
)
fsRrmAPSnrBSSIDSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDSlotId.setStatus("current")


class _FsRrmAPSnrBSSIDAPName_Type(DisplayString):
    """Custom type fsRrmAPSnrBSSIDAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsRrmAPSnrBSSIDAPName_Type.__name__ = "DisplayString"
_FsRrmAPSnrBSSIDAPName_Object = MibTableColumn
fsRrmAPSnrBSSIDAPName = _FsRrmAPSnrBSSIDAPName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14, 1, 3),
    _FsRrmAPSnrBSSIDAPName_Type()
)
fsRrmAPSnrBSSIDAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDAPName.setStatus("current")
_FsRrmAPSnrBSSIDAverageSignalStrength_Type = Integer32
_FsRrmAPSnrBSSIDAverageSignalStrength_Object = MibTableColumn
fsRrmAPSnrBSSIDAverageSignalStrength = _FsRrmAPSnrBSSIDAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14, 1, 4),
    _FsRrmAPSnrBSSIDAverageSignalStrength_Type()
)
fsRrmAPSnrBSSIDAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDAverageSignalStrength.setStatus("current")
_FsRrmAPSnrBSSIDSignalPkts_Type = Integer32
_FsRrmAPSnrBSSIDSignalPkts_Object = MibTableColumn
fsRrmAPSnrBSSIDSignalPkts = _FsRrmAPSnrBSSIDSignalPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14, 1, 5),
    _FsRrmAPSnrBSSIDSignalPkts_Type()
)
fsRrmAPSnrBSSIDSignalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDSignalPkts.setStatus("current")
_FsRrmAPSnrBSSIDHighestRxSignalStrength_Type = Integer32
_FsRrmAPSnrBSSIDHighestRxSignalStrength_Object = MibTableColumn
fsRrmAPSnrBSSIDHighestRxSignalStrength = _FsRrmAPSnrBSSIDHighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14, 1, 6),
    _FsRrmAPSnrBSSIDHighestRxSignalStrength_Type()
)
fsRrmAPSnrBSSIDHighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDHighestRxSignalStrength.setStatus("current")
_FsRrmAPSnrBSSIDLowestRxSignalStrength_Type = Integer32
_FsRrmAPSnrBSSIDLowestRxSignalStrength_Object = MibTableColumn
fsRrmAPSnrBSSIDLowestRxSignalStrength = _FsRrmAPSnrBSSIDLowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14, 1, 7),
    _FsRrmAPSnrBSSIDLowestRxSignalStrength_Type()
)
fsRrmAPSnrBSSIDLowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDLowestRxSignalStrength.setStatus("current")
_FsRrmAPSnrBSSIDSampleTime_Type = Integer32
_FsRrmAPSnrBSSIDSampleTime_Object = MibTableColumn
fsRrmAPSnrBSSIDSampleTime = _FsRrmAPSnrBSSIDSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 1, 4, 14, 1, 8),
    _FsRrmAPSnrBSSIDSampleTime_Type()
)
fsRrmAPSnrBSSIDSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrmAPSnrBSSIDSampleTime.setStatus("current")
_FsRrmMIBTraps_ObjectIdentity = ObjectIdentity
fsRrmMIBTraps = _FsRrmMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2)
)
_FsRrmTrapControl_ObjectIdentity = ObjectIdentity
fsRrmTrapControl = _FsRrmTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 1)
)


class _FsRrmAPDot11bProfileTrapControlMask_Type(Unsigned32):
    """Custom type fsRrmAPDot11bProfileTrapControlMask based on Unsigned32"""
    defaultValue = 0


_FsRrmAPDot11bProfileTrapControlMask_Type.__name__ = "Unsigned32"
_FsRrmAPDot11bProfileTrapControlMask_Object = MibScalar
fsRrmAPDot11bProfileTrapControlMask = _FsRrmAPDot11bProfileTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 1, 1),
    _FsRrmAPDot11bProfileTrapControlMask_Type()
)
fsRrmAPDot11bProfileTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPDot11bProfileTrapControlMask.setStatus("current")


class _FsRrmAPDot11aProfileTrapControlMask_Type(Unsigned32):
    """Custom type fsRrmAPDot11aProfileTrapControlMask based on Unsigned32"""
    defaultValue = 0


_FsRrmAPDot11aProfileTrapControlMask_Type.__name__ = "Unsigned32"
_FsRrmAPDot11aProfileTrapControlMask_Object = MibScalar
fsRrmAPDot11aProfileTrapControlMask = _FsRrmAPDot11aProfileTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 1, 2),
    _FsRrmAPDot11aProfileTrapControlMask_Type()
)
fsRrmAPDot11aProfileTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPDot11aProfileTrapControlMask.setStatus("current")


class _FsRrmAPDot11bParamUpdateTrapControlMask_Type(Unsigned32):
    """Custom type fsRrmAPDot11bParamUpdateTrapControlMask based on Unsigned32"""
    defaultValue = 0


_FsRrmAPDot11bParamUpdateTrapControlMask_Type.__name__ = "Unsigned32"
_FsRrmAPDot11bParamUpdateTrapControlMask_Object = MibScalar
fsRrmAPDot11bParamUpdateTrapControlMask = _FsRrmAPDot11bParamUpdateTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 1, 3),
    _FsRrmAPDot11bParamUpdateTrapControlMask_Type()
)
fsRrmAPDot11bParamUpdateTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPDot11bParamUpdateTrapControlMask.setStatus("current")


class _FsRrmAPDot11aParamUpdateTrapControlMask_Type(Unsigned32):
    """Custom type fsRrmAPDot11aParamUpdateTrapControlMask based on Unsigned32"""
    defaultValue = 0


_FsRrmAPDot11aParamUpdateTrapControlMask_Type.__name__ = "Unsigned32"
_FsRrmAPDot11aParamUpdateTrapControlMask_Object = MibScalar
fsRrmAPDot11aParamUpdateTrapControlMask = _FsRrmAPDot11aParamUpdateTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 1, 4),
    _FsRrmAPDot11aParamUpdateTrapControlMask_Type()
)
fsRrmAPDot11aParamUpdateTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmAPDot11aParamUpdateTrapControlMask.setStatus("current")
_FsRrmTrapVariable_ObjectIdentity = ObjectIdentity
fsRrmTrapVariable = _FsRrmTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2)
)
_FsRrmAPMacAddrTrapVariable_Type = MacAddress
_FsRrmAPMacAddrTrapVariable_Object = MibScalar
fsRrmAPMacAddrTrapVariable = _FsRrmAPMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 1),
    _FsRrmAPMacAddrTrapVariable_Type()
)
fsRrmAPMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPMacAddrTrapVariable.setStatus("current")
_FsRrmAPRadioIDTrapVariable_Type = Integer32
_FsRrmAPRadioIDTrapVariable_Object = MibScalar
fsRrmAPRadioIDTrapVariable = _FsRrmAPRadioIDTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 2),
    _FsRrmAPRadioIDTrapVariable_Type()
)
fsRrmAPRadioIDTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPRadioIDTrapVariable.setStatus("current")


class _FsRrmAPRadioTypeTrapVariable_Type(Integer32):
    """Custom type fsRrmAPRadioTypeTrapVariable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type80211a", 0),
          ("type80211b", 1))
    )


_FsRrmAPRadioTypeTrapVariable_Type.__name__ = "Integer32"
_FsRrmAPRadioTypeTrapVariable_Object = MibScalar
fsRrmAPRadioTypeTrapVariable = _FsRrmAPRadioTypeTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 3),
    _FsRrmAPRadioTypeTrapVariable_Type()
)
fsRrmAPRadioTypeTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPRadioTypeTrapVariable.setStatus("current")
_FsRrmClientNumberTrapVariable_Type = Integer32
_FsRrmClientNumberTrapVariable_Object = MibScalar
fsRrmClientNumberTrapVariable = _FsRrmClientNumberTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 4),
    _FsRrmClientNumberTrapVariable_Type()
)
fsRrmClientNumberTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmClientNumberTrapVariable.setStatus("current")
_FsRrmForeignInterfereTrapVariable_Type = Integer32
_FsRrmForeignInterfereTrapVariable_Object = MibScalar
fsRrmForeignInterfereTrapVariable = _FsRrmForeignInterfereTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 5),
    _FsRrmForeignInterfereTrapVariable_Type()
)
fsRrmForeignInterfereTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmForeignInterfereTrapVariable.setStatus("current")
_FsRrmNoiseTrapVariable_Type = Integer32
_FsRrmNoiseTrapVariable_Object = MibScalar
fsRrmNoiseTrapVariable = _FsRrmNoiseTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 6),
    _FsRrmNoiseTrapVariable_Type()
)
fsRrmNoiseTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmNoiseTrapVariable.setStatus("current")
_FsRrmThroughputTrapVariable_Type = Unsigned32
_FsRrmThroughputTrapVariable_Object = MibScalar
fsRrmThroughputTrapVariable = _FsRrmThroughputTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 7),
    _FsRrmThroughputTrapVariable_Type()
)
fsRrmThroughputTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmThroughputTrapVariable.setStatus("current")
_FsRrmUtilizationTrapVariable_Type = Integer32
_FsRrmUtilizationTrapVariable_Object = MibScalar
fsRrmUtilizationTrapVariable = _FsRrmUtilizationTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 8),
    _FsRrmUtilizationTrapVariable_Type()
)
fsRrmUtilizationTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmUtilizationTrapVariable.setStatus("current")
_FsRrmAPTxPowerBeforeChange_Type = Integer32
_FsRrmAPTxPowerBeforeChange_Object = MibScalar
fsRrmAPTxPowerBeforeChange = _FsRrmAPTxPowerBeforeChange_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 9),
    _FsRrmAPTxPowerBeforeChange_Type()
)
fsRrmAPTxPowerBeforeChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPTxPowerBeforeChange.setStatus("current")
_FsRrmAPTxPowerAfterChange_Type = Integer32
_FsRrmAPTxPowerAfterChange_Object = MibScalar
fsRrmAPTxPowerAfterChange = _FsRrmAPTxPowerAfterChange_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 10),
    _FsRrmAPTxPowerAfterChange_Type()
)
fsRrmAPTxPowerAfterChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPTxPowerAfterChange.setStatus("current")
_FsRrmAPChannelNumberBeforeChannge_Type = Integer32
_FsRrmAPChannelNumberBeforeChannge_Object = MibScalar
fsRrmAPChannelNumberBeforeChannge = _FsRrmAPChannelNumberBeforeChannge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 11),
    _FsRrmAPChannelNumberBeforeChannge_Type()
)
fsRrmAPChannelNumberBeforeChannge.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPChannelNumberBeforeChannge.setStatus("current")
_FsRrmAPChannelNumberAfterChannge_Type = Integer32
_FsRrmAPChannelNumberAfterChannge_Object = MibScalar
fsRrmAPChannelNumberAfterChannge = _FsRrmAPChannelNumberAfterChannge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 12),
    _FsRrmAPChannelNumberAfterChannge_Type()
)
fsRrmAPChannelNumberAfterChannge.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPChannelNumberAfterChannge.setStatus("current")
_FsRrmDot11bGroupLeaderMacAddrTrapVariable_Type = MacAddress
_FsRrmDot11bGroupLeaderMacAddrTrapVariable_Object = MibScalar
fsRrmDot11bGroupLeaderMacAddrTrapVariable = _FsRrmDot11bGroupLeaderMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 13),
    _FsRrmDot11bGroupLeaderMacAddrTrapVariable_Type()
)
fsRrmDot11bGroupLeaderMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmDot11bGroupLeaderMacAddrTrapVariable.setStatus("current")
_FsRrmDot11aGroupLeaderMacAddrTrapVariable_Type = MacAddress
_FsRrmDot11aGroupLeaderMacAddrTrapVariable_Object = MibScalar
fsRrmDot11aGroupLeaderMacAddrTrapVariable = _FsRrmDot11aGroupLeaderMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 14),
    _FsRrmDot11aGroupLeaderMacAddrTrapVariable_Type()
)
fsRrmDot11aGroupLeaderMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmDot11aGroupLeaderMacAddrTrapVariable.setStatus("current")


class _FsRrmAPChannelChangeReason_Type(Integer32):
    """Custom type fsRrmAPChannelChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("interference", 2),
          ("noise", 3),
          ("load", 4),
          ("radar", 5),
          ("other", 6))
    )


_FsRrmAPChannelChangeReason_Type.__name__ = "Integer32"
_FsRrmAPChannelChangeReason_Object = MibScalar
fsRrmAPChannelChangeReason = _FsRrmAPChannelChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 15),
    _FsRrmAPChannelChangeReason_Type()
)
fsRrmAPChannelChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPChannelChangeReason.setStatus("current")
_FsRrmAPChannelChangeReasonValue_Type = Integer32
_FsRrmAPChannelChangeReasonValue_Object = MibScalar
fsRrmAPChannelChangeReasonValue = _FsRrmAPChannelChangeReasonValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 16),
    _FsRrmAPChannelChangeReasonValue_Type()
)
fsRrmAPChannelChangeReasonValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPChannelChangeReasonValue.setStatus("current")


class _FsRrmAPTxPowerChangeCoverageFlag_Type(Integer32):
    """Custom type fsRrmAPTxPowerChangeCoverageFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsRrmAPTxPowerChangeCoverageFlag_Type.__name__ = "Integer32"
_FsRrmAPTxPowerChangeCoverageFlag_Object = MibScalar
fsRrmAPTxPowerChangeCoverageFlag = _FsRrmAPTxPowerChangeCoverageFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 17),
    _FsRrmAPTxPowerChangeCoverageFlag_Type()
)
fsRrmAPTxPowerChangeCoverageFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPTxPowerChangeCoverageFlag.setStatus("current")
_FsRrmDFSFreeCount_Type = Integer32
_FsRrmDFSFreeCount_Object = MibScalar
fsRrmDFSFreeCount = _FsRrmDFSFreeCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 18),
    _FsRrmDFSFreeCount_Type()
)
fsRrmDFSFreeCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmDFSFreeCount.setStatus("current")
_FsRrmAPChannelChangeCount_Type = Integer32
_FsRrmAPChannelChangeCount_Object = MibScalar
fsRrmAPChannelChangeCount = _FsRrmAPChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 2, 19),
    _FsRrmAPChannelChangeCount_Type()
)
fsRrmAPChannelChangeCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRrmAPChannelChangeCount.setStatus("current")
_FsRrmTraps_ObjectIdentity = ObjectIdentity
fsRrmTraps = _FsRrmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3)
)
_FsRrmMIBConformance_ObjectIdentity = ObjectIdentity
fsRrmMIBConformance = _FsRrmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 3)
)
_FsRrmMIBCompliances_ObjectIdentity = ObjectIdentity
fsRrmMIBCompliances = _FsRrmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 3, 1)
)
_FsRrmMIBGroups_ObjectIdentity = ObjectIdentity
fsRrmMIBGroups = _FsRrmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 3, 2)
)

# Managed Objects groups

fsRrmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 3, 2, 1)
)
fsRrmMIBGroup.setObjects(
      *(("FS-RRM-MIB", "fsRrmRFNetworkName"),
        ("FS-RRM-MIB", "fsRrmAPName"),
        ("FS-RRM-MIB", "fsRrmAPIfThresholdRadioType"),
        ("FS-RRM-MIB", "fsRrmAPIfForeignInterferenceThreshold"),
        ("FS-RRM-MIB", "fsRrmAPIfForeignNoiseThreshold"),
        ("FS-RRM-MIB", "fsRrmAPIfRFUtilizationThreshold"),
        ("FS-RRM-MIB", "fsRrmAPIfThroughputThreshold"),
        ("FS-RRM-MIB", "fsRrmAPIfMobilesThreshold"),
        ("FS-RRM-MIB", "fsRrmAPIfThresholdMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfThresholdRadioType"),
        ("FS-RRM-MIB", "fsRrmAPIfThresholdName"),
        ("FS-RRM-MIB", "fsRrmAPIfLoadRxUtilization"),
        ("FS-RRM-MIB", "fsRrmAPIfLoadTxUtilization"),
        ("FS-RRM-MIB", "fsRrmAPIfLoadChannelUtilization"),
        ("FS-RRM-MIB", "fsRrmAPIfLoadNumOfClients"),
        ("FS-RRM-MIB", "fsRrmAPIfPoorSNRClients"),
        ("FS-RRM-MIB", "fsRrmAPIfLoadName"),
        ("FS-RRM-MIB", "fsRrmAPIfLoadMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfLoadSlotId"),
        ("FS-RRM-MIB", "fsRrmAPIfThroughput"),
        ("FS-RRM-MIB", "fsRrmAPIfInterferenceChannelNo"),
        ("FS-RRM-MIB", "fsRrmAPIfInterferencePower"),
        ("FS-RRM-MIB", "fsRrmAPIfInterferenceUtilization"),
        ("FS-RRM-MIB", "fsRrmAPIfInterferenceName"),
        ("FS-RRM-MIB", "fsRrmAPIfInterferenceMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfInterferenceSlotId"),
        ("FS-RRM-MIB", "fsRrmAPIfNoiseChannelNo"),
        ("FS-RRM-MIB", "fsRrmAPIfDBNoisePower"),
        ("FS-RRM-MIB", "fsRrmAPIfNoiseName"),
        ("FS-RRM-MIB", "fsRrmAPIfNoiseMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfNoiseSlotId"),
        ("FS-RRM-MIB", "fsRrmAPIfLoadProfileState"),
        ("FS-RRM-MIB", "fsRrmAPIfInterferenceProfileState"),
        ("FS-RRM-MIB", "fsRrmAPIfNoiseProfileState"),
        ("FS-RRM-MIB", "fsRrmAPIfCoverageProfileState"),
        ("FS-RRM-MIB", "fsRrmAPIfPerformanceProfileState"),
        ("FS-RRM-MIB", "fsRrmAPIfProfileName"),
        ("FS-RRM-MIB", "fsRrmAPIfProfileMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfProfileSlotId"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborMacAddress"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborSlot"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborIpAddress"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborRSSI"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborSNR"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborChannel"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborChannelWidth"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborName"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfRxNeighborSlotId"),
        ("FS-RRM-MIB", "fsRrmAPIfStationRSSICoverageIndex"),
        ("FS-RRM-MIB", "fsRrmAPIfRSSILevel"),
        ("FS-RRM-MIB", "fsRrmAPIfStationCountOnRSSI"),
        ("FS-RRM-MIB", "fsRrmAPIfStationRSSIName"),
        ("FS-RRM-MIB", "fsRrmAPIfStationRSSIMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfStationRSSISlotId"),
        ("FS-RRM-MIB", "fsRrmAPIfStationSNRCoverageIndex"),
        ("FS-RRM-MIB", "fsRrmAPIfSNRLevel"),
        ("FS-RRM-MIB", "fsRrmAPIfStationCountOnSNR"),
        ("FS-RRM-MIB", "fsRrmAPIfStationSNRName"),
        ("FS-RRM-MIB", "fsRrmAPIfStationSNRMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfStationSNRSlotId"),
        ("FS-RRM-MIB", "fsRrmAPIfRecommendedChannelNumber"),
        ("FS-RRM-MIB", "fsRrmAPIfRecommendedTxPowerLevel"),
        ("FS-RRM-MIB", "fsRrmAPIfRecommendedRTSThreshold"),
        ("FS-RRM-MIB", "fsRrmAPIfRecommendedFragmentationThreshold"),
        ("FS-RRM-MIB", "fsRrmAPIfRecommendedName"),
        ("FS-RRM-MIB", "fsRrmAPIfRecommendedMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfRecommendedSlotId"),
        ("FS-RRM-MIB", "fsRrmAPRadioID"),
        ("FS-RRM-MIB", "fsRrmAPRadioType"),
        ("FS-RRM-MIB", "fsRrmAPRealName"),
        ("FS-RRM-MIB", "fsRrmAPMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfThroughputMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPIfThroughputSlotId"),
        ("FS-RRM-MIB", "fsRrmAPIfThroughputAPName"),
        ("FS-RRM-MIB", "fsRrmAPIfThroughputRx"),
        ("FS-RRM-MIB", "fsRrmAPIfThroughputTx"),
        ("FS-RRM-MIB", "fsRrmAPIfThroughputTotal"),
        ("FS-RRM-MIB", "fsRrmAPSnrBSSIDMacAddr"),
        ("FS-RRM-MIB", "fsRrmAPSnrBSSIDSlotId"),
        ("FS-RRM-MIB", "fsRrmAPSnrBSSIDAPName"),
        ("FS-RRM-MIB", "fsRrmAPSnrBSSIDAverageSignalStrength"),
        ("FS-RRM-MIB", "fsRrmAPSnrBSSIDSignalPkts"),
        ("FS-RRM-MIB", "fsRrmAPSnrBSSIDHighestRxSignalStrength"),
        ("FS-RRM-MIB", "fsRrmAPSnrBSSIDLowestRxSignalStrength"),
        ("FS-RRM-MIB", "fsRrmAPSnrBSSIDSampleTime"),
        ("FS-RRM-MIB", "fsRrmDot11bDynamicChannelAssignment"),
        ("FS-RRM-MIB", "fsRrmDot11bAnchorTime"),
        ("FS-RRM-MIB", "fsRrmDot11bChannalWidth11n"),
        ("FS-RRM-MIB", "fsRrmDot11bDynamicChannelUpdateInterval"),
        ("FS-RRM-MIB", "fsRrmDot11bDCASensitivity"),
        ("FS-RRM-MIB", "fsRrmDot11bForeignInterfereFactorEnable"),
        ("FS-RRM-MIB", "fsRrmDot11bLoadFactorEnable"),
        ("FS-RRM-MIB", "fsRrmDot11bNoiseFactorEnable"),
        ("FS-RRM-MIB", "fsRrmDot11bChannelUpdateCmdInvoke"),
        ("FS-RRM-MIB", "fsRrmDot11bDCAChannelIndex"),
        ("FS-RRM-MIB", "fsRrmDot11bDCAChannelOperation"),
        ("FS-RRM-MIB", "fsRrmDot11aDynamicChannelAssignment"),
        ("FS-RRM-MIB", "fsRrmDot11aAnchorTime"),
        ("FS-RRM-MIB", "fsRrmDot11aChannalWidth11n"),
        ("FS-RRM-MIB", "fsRrmDot11aDynamicChannelUpdateInterval"),
        ("FS-RRM-MIB", "fsRrmDot11aDCASensitivity"),
        ("FS-RRM-MIB", "fsRrmDot11aForeignInterfereFactorEnable"),
        ("FS-RRM-MIB", "fsRrmDot11aLoadFactorEnable"),
        ("FS-RRM-MIB", "fsRrmDot11aNoiseFactorEnable"),
        ("FS-RRM-MIB", "fsRrmDot11aChannelUpdateCmdInvoke"),
        ("FS-RRM-MIB", "fsRrmDot11aDCAChannelIndex"),
        ("FS-RRM-MIB", "fsRrmDot11aDCAChannelOperation"),
        ("FS-RRM-MIB", "fsRrmDot11bDTPCSupport"),
        ("FS-RRM-MIB", "fsRrmDot11bDynamicTransmitPowerControl"),
        ("FS-RRM-MIB", "fsRrmDot11bDynamicTxPowerControlInterval"),
        ("FS-RRM-MIB", "fsRrmDot11bCurrentTxPowerLevel"),
        ("FS-RRM-MIB", "fsRrmDot11bPowerUpdateCmdInvoke"),
        ("FS-RRM-MIB", "fsRrmDot11bTXPowerThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11bTPCNeighborNumber"),
        ("FS-RRM-MIB", "fsRrmDot11aDTPCSupport"),
        ("FS-RRM-MIB", "fsRrmDot11aDynamicTransmitPowerControl"),
        ("FS-RRM-MIB", "fsRrmDot11aDynamicTxPowerControlInterval"),
        ("FS-RRM-MIB", "fsRrmDot11aCurrentTxPowerLevel"),
        ("FS-RRM-MIB", "fsRrmDot11aPowerUpdateCmdInvoke"),
        ("FS-RRM-MIB", "fsRrmDot11aTXPowerThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11aTPCNeighborNumber"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageEnable"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageExceptionGlobal"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageLevelGlobal"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageDataRSSIThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageVoiceRSSIThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageDataPacketCount"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageVoicePacketCount"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageDataFailRate"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageVoiceFailRate"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageEnable"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageExceptionGlobal"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageLevelGlobal"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageDataRSSIThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageVoiceRSSIThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageDataPacketCount"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageVoicePacketCount"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageDataFailRate"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageVoiceFailRate"),
        ("FS-RRM-MIB", "fsRrmDot11bGlobalAutomaticGrouping"),
        ("FS-RRM-MIB", "fsRrmDot11bGroupLeaderMacAddr"),
        ("FS-RRM-MIB", "fsRrmDot11bGroupLeader"),
        ("FS-RRM-MIB", "fsRrmDot11bGroupLastUpdateTime"),
        ("FS-RRM-MIB", "fsRrmDot11bGroupInterval"),
        ("FS-RRM-MIB", "fsRrmDot11bPeerMacAddress"),
        ("FS-RRM-MIB", "fsRrmDot11bPeerIpAddress"),
        ("FS-RRM-MIB", "fsRrmDot11bAPname"),
        ("FS-RRM-MIB", "fsRrmDot11bAPRadioID"),
        ("FS-RRM-MIB", "fsRrmDot11bAPChannel"),
        ("FS-RRM-MIB", "fsRrmDot11bAPTxPower"),
        ("FS-RRM-MIB", "fsRrmDot11bAPChannelRrmChangeFlag"),
        ("FS-RRM-MIB", "fsRrmDot11bAPTxPowerRrmChangeFlag"),
        ("FS-RRM-MIB", "fsRrmDot11bSummaryMacAddress"),
        ("FS-RRM-MIB", "fsRrmDot11aGlobalAutomaticGrouping"),
        ("FS-RRM-MIB", "fsRrmDot11aGroupLeader"),
        ("FS-RRM-MIB", "fsRrmDot11aGroupLastUpdateTime"),
        ("FS-RRM-MIB", "fsRrmDot11aGroupInterval"),
        ("FS-RRM-MIB", "fsRrmDot11aPeerMacAddress"),
        ("FS-RRM-MIB", "fsRrmDot11aPeerIpAddress"),
        ("FS-RRM-MIB", "fsRrmDot11aAPname"),
        ("FS-RRM-MIB", "fsRrmDot11aAPRadioID"),
        ("FS-RRM-MIB", "fsRrmDot11aAPChannel"),
        ("FS-RRM-MIB", "fsRrmDot11aAPTxPower"),
        ("FS-RRM-MIB", "fsRrmDot11aAPChannelRrmChangeFlag"),
        ("FS-RRM-MIB", "fsRrmDot11aAPTxPowerRrmChangeFlag"),
        ("FS-RRM-MIB", "fsRrmDot11aSummaryMacAddress"),
        ("FS-RRM-MIB", "fsRrmDot11bForeignInterferenceThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11bForeignNoiseThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11bRFUtilizationThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11bThroughputThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11bMobilesThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11aForeignInterferenceThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11aForeignNoiseThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11aRFUtilizationThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11aThroughputThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11aMobilesThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11bMonitorEnable"),
        ("FS-RRM-MIB", "fsRrmDot11bChannelMonitorList"),
        ("FS-RRM-MIB", "fsRrmDot11bMonitorInterval"),
        ("FS-RRM-MIB", "fsRrmDot11bCoverageMeasurementInterval"),
        ("FS-RRM-MIB", "fsRrmDot11bLoadMeasurementInterval"),
        ("FS-RRM-MIB", "fsRrmDot11bNoiseMeasurementInterval"),
        ("FS-RRM-MIB", "fsRrmDot11bSignalMeasurementInterval"),
        ("FS-RRM-MIB", "fsRrmDot11bNeighborMessageInterval"),
        ("FS-RRM-MIB", "fsRrmDot11aMonitorEnable"),
        ("FS-RRM-MIB", "fsRrmDot11aChannelMonitorList"),
        ("FS-RRM-MIB", "fsRrmDot11aMonitorInterval"),
        ("FS-RRM-MIB", "fsRrmDot11aCoverageMeasurementInterval"),
        ("FS-RRM-MIB", "fsRrmDot11aLoadMeasurementInterval"),
        ("FS-RRM-MIB", "fsRrmDot11aNoiseMeasurementInterval"),
        ("FS-RRM-MIB", "fsRrmDot11aSignalMeasurementInterval"),
        ("FS-RRM-MIB", "fsRrmDot11aNeighborMessageInterval"),
        ("FS-RRM-MIB", "fsRrmDot11bSetFactoryDefault"),
        ("FS-RRM-MIB", "fsRrmDot11aSetFactoryDefault"))
)
if mibBuilder.loadTexts:
    fsRrmMIBGroup.setStatus("current")

fsRrmTrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 3, 2, 2)
)
fsRrmTrapsGroup.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPDot11bProfileTrapControlMask"),
        ("FS-RRM-MIB", "fsRrmAPDot11aProfileTrapControlMask"),
        ("FS-RRM-MIB", "fsRrmAPDot11bParamUpdateTrapControlMask"),
        ("FS-RRM-MIB", "fsRrmAPDot11aParamUpdateTrapControlMask"),
        ("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmClientNumberTrapVariable"),
        ("FS-RRM-MIB", "fsRrmForeignInterfereTrapVariable"),
        ("FS-RRM-MIB", "fsRrmNoiseTrapVariable"),
        ("FS-RRM-MIB", "fsRrmThroughputTrapVariable"),
        ("FS-RRM-MIB", "fsRrmUtilizationTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPTxPowerBeforeChange"),
        ("FS-RRM-MIB", "fsRrmAPTxPowerAfterChange"),
        ("FS-RRM-MIB", "fsRrmAPTxPowerChangeCoverageFlag"),
        ("FS-RRM-MIB", "fsRrmAPChannelNumberBeforeChannge"),
        ("FS-RRM-MIB", "fsRrmAPChannelNumberAfterChannge"),
        ("FS-RRM-MIB", "fsRrmAPChannelChangeReason"),
        ("FS-RRM-MIB", "fsRrmAPChannelChangeReasonValue"),
        ("FS-RRM-MIB", "fsRrmAPChannelChangeCount"),
        ("FS-RRM-MIB", "fsRrmDFSFreeCount"),
        ("FS-RRM-MIB", "fsRrmDot11bGroupLeaderMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmDot11aGroupLeaderMacAddrTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmTrapsGroup.setStatus("current")


# Notification objects

fsRrmAPClientNumProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 1)
)
fsRrmAPClientNumProfileFailed.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmClientNumberTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPClientNumProfileFailed.setStatus(
        "current"
    )

fsRrmAPLoadProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 2)
)
fsRrmAPLoadProfileFailed.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmUtilizationTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPLoadProfileFailed.setStatus(
        "current"
    )

fsRrmAPNoiseProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 3)
)
fsRrmAPNoiseProfileFailed.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmNoiseTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPNoiseProfileFailed.setStatus(
        "current"
    )

fsRrmAPInterferenceProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 4)
)
fsRrmAPInterferenceProfileFailed.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmForeignInterfereTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPInterferenceProfileFailed.setStatus(
        "current"
    )

fsRrmAPPerformanceProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 5)
)
fsRrmAPPerformanceProfileFailed.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmThroughputTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPPerformanceProfileFailed.setStatus(
        "current"
    )

fsRrmAPClientNumProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 6)
)
fsRrmAPClientNumProfileUpdatedToPass.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmClientNumberTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPClientNumProfileUpdatedToPass.setStatus(
        "current"
    )

fsRrmAPLoadProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 7)
)
fsRrmAPLoadProfileUpdatedToPass.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmUtilizationTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPLoadProfileUpdatedToPass.setStatus(
        "current"
    )

fsRrmAPNoiseProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 8)
)
fsRrmAPNoiseProfileUpdatedToPass.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmNoiseTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPNoiseProfileUpdatedToPass.setStatus(
        "current"
    )

fsRrmAPInterferenceProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 9)
)
fsRrmAPInterferenceProfileUpdatedToPass.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmForeignInterfereTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPInterferenceProfileUpdatedToPass.setStatus(
        "current"
    )

fsRrmAPPerformanceProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 10)
)
fsRrmAPPerformanceProfileUpdatedToPass.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmThroughputTrapVariable"))
)
if mibBuilder.loadTexts:
    fsRrmAPPerformanceProfileUpdatedToPass.setStatus(
        "current"
    )

fsRrmAPCurrentTxPowerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 11)
)
fsRrmAPCurrentTxPowerChanged.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPTxPowerBeforeChange"),
        ("FS-RRM-MIB", "fsRrmAPTxPowerAfterChange"),
        ("FS-RRM-MIB", "fsRrmAPTxPowerChangeCoverageFlag"))
)
if mibBuilder.loadTexts:
    fsRrmAPCurrentTxPowerChanged.setStatus(
        "current"
    )

fsRrmAPCurrentChannelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 12)
)
fsRrmAPCurrentChannelChanged.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioIDTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPRadioTypeTrapVariable"),
        ("FS-RRM-MIB", "fsRrmAPChannelNumberBeforeChannge"),
        ("FS-RRM-MIB", "fsRrmAPChannelNumberAfterChannge"),
        ("FS-RRM-MIB", "fsRrmAPChannelChangeReason"),
        ("FS-RRM-MIB", "fsRrmAPChannelChangeReasonValue"),
        ("FS-RRM-MIB", "fsRrmAPChannelChangeCount"))
)
if mibBuilder.loadTexts:
    fsRrmAPCurrentChannelChanged.setStatus(
        "current"
    )

fsRrmDot11bGroupingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 13)
)
fsRrmDot11bGroupingDone.setObjects(
    ("FS-RRM-MIB", "fsRrmDot11bGroupLeaderMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    fsRrmDot11bGroupingDone.setStatus(
        "current"
    )

fsRrmDot11aGroupingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 14)
)
fsRrmDot11aGroupingDone.setObjects(
    ("FS-RRM-MIB", "fsRrmDot11aGroupLeaderMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    fsRrmDot11aGroupingDone.setStatus(
        "current"
    )

fsRrmDot11bDFSFreeCountBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 15)
)
fsRrmDot11bDFSFreeCountBelowThreshold.setObjects(
    ("FS-RRM-MIB", "fsRrmDFSFreeCount")
)
if mibBuilder.loadTexts:
    fsRrmDot11bDFSFreeCountBelowThreshold.setStatus(
        "current"
    )

fsRrmDot11aDFSFreeCountBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 16)
)
fsRrmDot11aDFSFreeCountBelowThreshold.setObjects(
    ("FS-RRM-MIB", "fsRrmDFSFreeCount")
)
if mibBuilder.loadTexts:
    fsRrmDot11aDFSFreeCountBelowThreshold.setStatus(
        "current"
    )

fsRrmNeighborAPInterference = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 17)
)
fsRrmNeighborAPInterference.setObjects(
    ("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    fsRrmNeighborAPInterference.setStatus(
        "current"
    )

fsRrmStationInterference = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 18)
)
fsRrmStationInterference.setObjects(
    ("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    fsRrmStationInterference.setStatus(
        "current"
    )

fsRrmOtherDiveceInterference = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 2, 3, 19)
)
fsRrmOtherDiveceInterference.setObjects(
    ("FS-RRM-MIB", "fsRrmAPMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    fsRrmOtherDiveceInterference.setStatus(
        "current"
    )


# Notifications groups

fsRrmTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 3, 2, 3)
)
fsRrmTrap.setObjects(
      *(("FS-RRM-MIB", "fsRrmAPClientNumProfileFailed"),
        ("FS-RRM-MIB", "fsRrmAPLoadProfileFailed"),
        ("FS-RRM-MIB", "fsRrmAPNoiseProfileFailed"),
        ("FS-RRM-MIB", "fsRrmAPInterferenceProfileFailed"),
        ("FS-RRM-MIB", "fsRrmAPPerformanceProfileFailed"),
        ("FS-RRM-MIB", "fsRrmAPClientNumProfileUpdatedToPass"),
        ("FS-RRM-MIB", "fsRrmAPLoadProfileUpdatedToPass"),
        ("FS-RRM-MIB", "fsRrmAPNoiseProfileUpdatedToPass"),
        ("FS-RRM-MIB", "fsRrmAPInterferenceProfileUpdatedToPass"),
        ("FS-RRM-MIB", "fsRrmAPPerformanceProfileUpdatedToPass"),
        ("FS-RRM-MIB", "fsRrmAPCurrentTxPowerChanged"),
        ("FS-RRM-MIB", "fsRrmAPCurrentChannelChanged"),
        ("FS-RRM-MIB", "fsRrmDot11bGroupingDone"),
        ("FS-RRM-MIB", "fsRrmDot11aGroupingDone"),
        ("FS-RRM-MIB", "fsRrmDot11bDFSFreeCountBelowThreshold"),
        ("FS-RRM-MIB", "fsRrmDot11aDFSFreeCountBelowThreshold"),
        ("FS-RRM-MIB", "fsRrmNeighborAPInterference"),
        ("FS-RRM-MIB", "fsRrmStationInterference"),
        ("FS-RRM-MIB", "fsRrmOtherDiveceInterference"))
)
if mibBuilder.loadTexts:
    fsRrmTrap.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsRrmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 63, 3, 1, 1)
)
fsRrmMIBCompliance.setObjects(
      *(("FS-RRM-MIB", "fsRrmMIBGroup"),
        ("FS-RRM-MIB", "fsRrmTrapsGroup"))
)
if mibBuilder.loadTexts:
    fsRrmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-RRM-MIB",
    **{"ProfileState": ProfileState,
       "fsRrmMIB": fsRrmMIB,
       "fsRrmMIBObjects": fsRrmMIBObjects,
       "fsRrmObjectsGroup": fsRrmObjectsGroup,
       "fsRrmRFNetworkName": fsRrmRFNetworkName,
       "fsRrmObjectsDot11a": fsRrmObjectsDot11a,
       "fsRrmDCADot11a": fsRrmDCADot11a,
       "fsRrmDot11aDynamicChannelAssignment": fsRrmDot11aDynamicChannelAssignment,
       "fsRrmDot11aAnchorTime": fsRrmDot11aAnchorTime,
       "fsRrmDot11aChannalWidth11n": fsRrmDot11aChannalWidth11n,
       "fsRrmDot11aDynamicChannelUpdateInterval": fsRrmDot11aDynamicChannelUpdateInterval,
       "fsRrmDot11aDCASensitivity": fsRrmDot11aDCASensitivity,
       "fsRrmDot11aForeignInterfereFactorEnable": fsRrmDot11aForeignInterfereFactorEnable,
       "fsRrmDot11aLoadFactorEnable": fsRrmDot11aLoadFactorEnable,
       "fsRrmDot11aNoiseFactorEnable": fsRrmDot11aNoiseFactorEnable,
       "fsRrmDot11aChannelUpdateCmdInvoke": fsRrmDot11aChannelUpdateCmdInvoke,
       "fsRrmDot11aDCAChannelTable": fsRrmDot11aDCAChannelTable,
       "fsRrmDot11aDCAChannelEntry": fsRrmDot11aDCAChannelEntry,
       "fsRrmDot11aDCAChannelIndex": fsRrmDot11aDCAChannelIndex,
       "fsRrmDot11aDCAChannelOperation": fsRrmDot11aDCAChannelOperation,
       "fsRrmTPCDot11a": fsRrmTPCDot11a,
       "fsRrmDot11aDTPCSupport": fsRrmDot11aDTPCSupport,
       "fsRrmDot11aDynamicTransmitPowerControl": fsRrmDot11aDynamicTransmitPowerControl,
       "fsRrmDot11aDynamicTxPowerControlInterval": fsRrmDot11aDynamicTxPowerControlInterval,
       "fsRrmDot11aCurrentTxPowerLevel": fsRrmDot11aCurrentTxPowerLevel,
       "fsRrmDot11aPowerUpdateCmdInvoke": fsRrmDot11aPowerUpdateCmdInvoke,
       "fsRrmDot11aTXPowerThreshold": fsRrmDot11aTXPowerThreshold,
       "fsRrmDot11aTPCNeighborNumber": fsRrmDot11aTPCNeighborNumber,
       "fsRrmCHDDot11a": fsRrmCHDDot11a,
       "fsRrmDot11aCoverageEnable": fsRrmDot11aCoverageEnable,
       "fsRrmDot11aCoverageExceptionGlobal": fsRrmDot11aCoverageExceptionGlobal,
       "fsRrmDot11aCoverageLevelGlobal": fsRrmDot11aCoverageLevelGlobal,
       "fsRrmDot11aCoverageDataRSSIThreshold": fsRrmDot11aCoverageDataRSSIThreshold,
       "fsRrmDot11aCoverageVoiceRSSIThreshold": fsRrmDot11aCoverageVoiceRSSIThreshold,
       "fsRrmDot11aCoverageDataPacketCount": fsRrmDot11aCoverageDataPacketCount,
       "fsRrmDot11aCoverageVoicePacketCount": fsRrmDot11aCoverageVoicePacketCount,
       "fsRrmDot11aCoverageDataFailRate": fsRrmDot11aCoverageDataFailRate,
       "fsRrmDot11aCoverageVoiceFailRate": fsRrmDot11aCoverageVoiceFailRate,
       "fsRrmGroupDot11a": fsRrmGroupDot11a,
       "fsRrmDot11aGlobalAutomaticGrouping": fsRrmDot11aGlobalAutomaticGrouping,
       "fsRrmDot11aGroupLeaderMacAddr": fsRrmDot11aGroupLeaderMacAddr,
       "fsRrmDot11aGroupLeader": fsRrmDot11aGroupLeader,
       "fsRrmDot11aGroupLastUpdateTime": fsRrmDot11aGroupLastUpdateTime,
       "fsRrmDot11aGroupInterval": fsRrmDot11aGroupInterval,
       "fsRrmDot11aGroupTable": fsRrmDot11aGroupTable,
       "fsRrmDot11aGroupEntry": fsRrmDot11aGroupEntry,
       "fsRrmDot11aPeerMacAddress": fsRrmDot11aPeerMacAddress,
       "fsRrmDot11aPeerIpAddress": fsRrmDot11aPeerIpAddress,
       "fsRrmDot11aSummaryTable": fsRrmDot11aSummaryTable,
       "fsRrmDot11aSummaryEntry": fsRrmDot11aSummaryEntry,
       "fsRrmDot11aAPname": fsRrmDot11aAPname,
       "fsRrmDot11aAPRadioID": fsRrmDot11aAPRadioID,
       "fsRrmDot11aAPChannel": fsRrmDot11aAPChannel,
       "fsRrmDot11aAPTxPower": fsRrmDot11aAPTxPower,
       "fsRrmDot11aAPChannelRrmChangeFlag": fsRrmDot11aAPChannelRrmChangeFlag,
       "fsRrmDot11aAPTxPowerRrmChangeFlag": fsRrmDot11aAPTxPowerRrmChangeFlag,
       "fsRrmDot11aSummaryMacAddress": fsRrmDot11aSummaryMacAddress,
       "fsRrmProfileDot11a": fsRrmProfileDot11a,
       "fsRrmDot11aForeignInterferenceThreshold": fsRrmDot11aForeignInterferenceThreshold,
       "fsRrmDot11aForeignNoiseThreshold": fsRrmDot11aForeignNoiseThreshold,
       "fsRrmDot11aRFUtilizationThreshold": fsRrmDot11aRFUtilizationThreshold,
       "fsRrmDot11aThroughputThreshold": fsRrmDot11aThroughputThreshold,
       "fsRrmDot11aMobilesThreshold": fsRrmDot11aMobilesThreshold,
       "fsRrmMonitorDot11a": fsRrmMonitorDot11a,
       "fsRrmDot11aMonitorEnable": fsRrmDot11aMonitorEnable,
       "fsRrmDot11aChannelMonitorList": fsRrmDot11aChannelMonitorList,
       "fsRrmDot11aMonitorInterval": fsRrmDot11aMonitorInterval,
       "fsRrmDot11aCoverageMeasurementInterval": fsRrmDot11aCoverageMeasurementInterval,
       "fsRrmDot11aLoadMeasurementInterval": fsRrmDot11aLoadMeasurementInterval,
       "fsRrmDot11aNoiseMeasurementInterval": fsRrmDot11aNoiseMeasurementInterval,
       "fsRrmDot11aSignalMeasurementInterval": fsRrmDot11aSignalMeasurementInterval,
       "fsRrmDot11aNeighborMessageInterval": fsRrmDot11aNeighborMessageInterval,
       "fsRrmFactoryDot11a": fsRrmFactoryDot11a,
       "fsRrmDot11aSetFactoryDefault": fsRrmDot11aSetFactoryDefault,
       "fsRrmObjectsDot11b": fsRrmObjectsDot11b,
       "fsRrmDCADot11b": fsRrmDCADot11b,
       "fsRrmDot11bDynamicChannelAssignment": fsRrmDot11bDynamicChannelAssignment,
       "fsRrmDot11bAnchorTime": fsRrmDot11bAnchorTime,
       "fsRrmDot11bChannalWidth11n": fsRrmDot11bChannalWidth11n,
       "fsRrmDot11bDynamicChannelUpdateInterval": fsRrmDot11bDynamicChannelUpdateInterval,
       "fsRrmDot11bDCASensitivity": fsRrmDot11bDCASensitivity,
       "fsRrmDot11bForeignInterfereFactorEnable": fsRrmDot11bForeignInterfereFactorEnable,
       "fsRrmDot11bLoadFactorEnable": fsRrmDot11bLoadFactorEnable,
       "fsRrmDot11bNoiseFactorEnable": fsRrmDot11bNoiseFactorEnable,
       "fsRrmDot11bChannelUpdateCmdInvoke": fsRrmDot11bChannelUpdateCmdInvoke,
       "fsRrmDot11bDCAChannelTable": fsRrmDot11bDCAChannelTable,
       "fsRrmDot11bDCAChannelEntry": fsRrmDot11bDCAChannelEntry,
       "fsRrmDot11bDCAChannelIndex": fsRrmDot11bDCAChannelIndex,
       "fsRrmDot11bDCAChannelOperation": fsRrmDot11bDCAChannelOperation,
       "fsRrmTPCDot11b": fsRrmTPCDot11b,
       "fsRrmDot11bDTPCSupport": fsRrmDot11bDTPCSupport,
       "fsRrmDot11bDynamicTransmitPowerControl": fsRrmDot11bDynamicTransmitPowerControl,
       "fsRrmDot11bDynamicTxPowerControlInterval": fsRrmDot11bDynamicTxPowerControlInterval,
       "fsRrmDot11bCurrentTxPowerLevel": fsRrmDot11bCurrentTxPowerLevel,
       "fsRrmDot11bPowerUpdateCmdInvoke": fsRrmDot11bPowerUpdateCmdInvoke,
       "fsRrmDot11bTXPowerThreshold": fsRrmDot11bTXPowerThreshold,
       "fsRrmDot11bTPCNeighborNumber": fsRrmDot11bTPCNeighborNumber,
       "fsRrmCHDDot11b": fsRrmCHDDot11b,
       "fsRrmDot11bCoverageEnable": fsRrmDot11bCoverageEnable,
       "fsRrmDot11bCoverageExceptionGlobal": fsRrmDot11bCoverageExceptionGlobal,
       "fsRrmDot11bCoverageLevelGlobal": fsRrmDot11bCoverageLevelGlobal,
       "fsRrmDot11bCoverageDataRSSIThreshold": fsRrmDot11bCoverageDataRSSIThreshold,
       "fsRrmDot11bCoverageVoiceRSSIThreshold": fsRrmDot11bCoverageVoiceRSSIThreshold,
       "fsRrmDot11bCoverageDataPacketCount": fsRrmDot11bCoverageDataPacketCount,
       "fsRrmDot11bCoverageVoicePacketCount": fsRrmDot11bCoverageVoicePacketCount,
       "fsRrmDot11bCoverageDataFailRate": fsRrmDot11bCoverageDataFailRate,
       "fsRrmDot11bCoverageVoiceFailRate": fsRrmDot11bCoverageVoiceFailRate,
       "fsRrmGroupDot11b": fsRrmGroupDot11b,
       "fsRrmDot11bGlobalAutomaticGrouping": fsRrmDot11bGlobalAutomaticGrouping,
       "fsRrmDot11bGroupLeaderMacAddr": fsRrmDot11bGroupLeaderMacAddr,
       "fsRrmDot11bGroupLeader": fsRrmDot11bGroupLeader,
       "fsRrmDot11bGroupLastUpdateTime": fsRrmDot11bGroupLastUpdateTime,
       "fsRrmDot11bGroupInterval": fsRrmDot11bGroupInterval,
       "fsRrmDot11bGroupTable": fsRrmDot11bGroupTable,
       "fsRrmDot11bGroupEntry": fsRrmDot11bGroupEntry,
       "fsRrmDot11bPeerMacAddress": fsRrmDot11bPeerMacAddress,
       "fsRrmDot11bPeerIpAddress": fsRrmDot11bPeerIpAddress,
       "fsRrmDot11bSummaryTable": fsRrmDot11bSummaryTable,
       "fsRrmDot11bSummaryEntry": fsRrmDot11bSummaryEntry,
       "fsRrmDot11bAPname": fsRrmDot11bAPname,
       "fsRrmDot11bAPRadioID": fsRrmDot11bAPRadioID,
       "fsRrmDot11bAPChannel": fsRrmDot11bAPChannel,
       "fsRrmDot11bAPTxPower": fsRrmDot11bAPTxPower,
       "fsRrmDot11bAPChannelRrmChangeFlag": fsRrmDot11bAPChannelRrmChangeFlag,
       "fsRrmDot11bAPTxPowerRrmChangeFlag": fsRrmDot11bAPTxPowerRrmChangeFlag,
       "fsRrmDot11bSummaryMacAddress": fsRrmDot11bSummaryMacAddress,
       "fsRrmProfileDot11b": fsRrmProfileDot11b,
       "fsRrmDot11bForeignInterferenceThreshold": fsRrmDot11bForeignInterferenceThreshold,
       "fsRrmDot11bForeignNoiseThreshold": fsRrmDot11bForeignNoiseThreshold,
       "fsRrmDot11bRFUtilizationThreshold": fsRrmDot11bRFUtilizationThreshold,
       "fsRrmDot11bThroughputThreshold": fsRrmDot11bThroughputThreshold,
       "fsRrmDot11bMobilesThreshold": fsRrmDot11bMobilesThreshold,
       "fsRrmMonitorDot11b": fsRrmMonitorDot11b,
       "fsRrmDot11bMonitorEnable": fsRrmDot11bMonitorEnable,
       "fsRrmDot11bChannelMonitorList": fsRrmDot11bChannelMonitorList,
       "fsRrmDot11bMonitorInterval": fsRrmDot11bMonitorInterval,
       "fsRrmDot11bCoverageMeasurementInterval": fsRrmDot11bCoverageMeasurementInterval,
       "fsRrmDot11bLoadMeasurementInterval": fsRrmDot11bLoadMeasurementInterval,
       "fsRrmDot11bNoiseMeasurementInterval": fsRrmDot11bNoiseMeasurementInterval,
       "fsRrmDot11bSignalMeasurementInterval": fsRrmDot11bSignalMeasurementInterval,
       "fsRrmDot11bNeighborMessageInterval": fsRrmDot11bNeighborMessageInterval,
       "fsRrmFactoryDot11b": fsRrmFactoryDot11b,
       "fsRrmDot11bSetFactoryDefault": fsRrmDot11bSetFactoryDefault,
       "fsRrmObjectsAP": fsRrmObjectsAP,
       "fsRrmAPIfSlotId": fsRrmAPIfSlotId,
       "fsRrmAPName": fsRrmAPName,
       "fsRrmAPIfProfileThresholdConfigTable": fsRrmAPIfProfileThresholdConfigTable,
       "fsRrmAPIfProfileThresholdConfigEntry": fsRrmAPIfProfileThresholdConfigEntry,
       "fsRrmAPIfThresholdRadioType": fsRrmAPIfThresholdRadioType,
       "fsRrmAPIfForeignInterferenceThreshold": fsRrmAPIfForeignInterferenceThreshold,
       "fsRrmAPIfForeignNoiseThreshold": fsRrmAPIfForeignNoiseThreshold,
       "fsRrmAPIfRFUtilizationThreshold": fsRrmAPIfRFUtilizationThreshold,
       "fsRrmAPIfThroughputThreshold": fsRrmAPIfThroughputThreshold,
       "fsRrmAPIfMobilesThreshold": fsRrmAPIfMobilesThreshold,
       "fsRrmAPIfThresholdName": fsRrmAPIfThresholdName,
       "fsRrmAPIfThresholdMacAddr": fsRrmAPIfThresholdMacAddr,
       "fsRrmAPIfForeignGlobalConfig": fsRrmAPIfForeignGlobalConfig,
       "fsRrmAPIfNoiseGlobalConfig": fsRrmAPIfNoiseGlobalConfig,
       "fsRrmAPIfRFUtilizationGlobalConfig": fsRrmAPIfRFUtilizationGlobalConfig,
       "fsRrmAPIfThroughputGlobalConfig": fsRrmAPIfThroughputGlobalConfig,
       "fsRrmAPIfMobilesGlobalConfig": fsRrmAPIfMobilesGlobalConfig,
       "fsRrmAPIfLoadParametersTable": fsRrmAPIfLoadParametersTable,
       "fsRrmAPIfLoadParametersEntry": fsRrmAPIfLoadParametersEntry,
       "fsRrmAPIfLoadRxUtilization": fsRrmAPIfLoadRxUtilization,
       "fsRrmAPIfLoadTxUtilization": fsRrmAPIfLoadTxUtilization,
       "fsRrmAPIfLoadChannelUtilization": fsRrmAPIfLoadChannelUtilization,
       "fsRrmAPIfLoadNumOfClients": fsRrmAPIfLoadNumOfClients,
       "fsRrmAPIfPoorSNRClients": fsRrmAPIfPoorSNRClients,
       "fsRrmAPIfLoadName": fsRrmAPIfLoadName,
       "fsRrmAPIfLoadMacAddr": fsRrmAPIfLoadMacAddr,
       "fsRrmAPIfLoadSlotId": fsRrmAPIfLoadSlotId,
       "fsRrmAPIfThroughput": fsRrmAPIfThroughput,
       "fsRrmAPIfChannelInterferenceInfoTable": fsRrmAPIfChannelInterferenceInfoTable,
       "fsRrmAPIfChannelInterferenceInfoEntry": fsRrmAPIfChannelInterferenceInfoEntry,
       "fsRrmAPIfInterferenceChannelNo": fsRrmAPIfInterferenceChannelNo,
       "fsRrmAPIfInterferencePower": fsRrmAPIfInterferencePower,
       "fsRrmAPIfInterferenceUtilization": fsRrmAPIfInterferenceUtilization,
       "fsRrmAPIfInterferenceName": fsRrmAPIfInterferenceName,
       "fsRrmAPIfInterferenceMacAddr": fsRrmAPIfInterferenceMacAddr,
       "fsRrmAPIfInterferenceSlotId": fsRrmAPIfInterferenceSlotId,
       "fsRrmAPIfChannelNoiseInfoTable": fsRrmAPIfChannelNoiseInfoTable,
       "fsRrmAPIfChannelNoiseInfoEntry": fsRrmAPIfChannelNoiseInfoEntry,
       "fsRrmAPIfNoiseChannelNo": fsRrmAPIfNoiseChannelNo,
       "fsRrmAPIfDBNoisePower": fsRrmAPIfDBNoisePower,
       "fsRrmAPIfNoiseName": fsRrmAPIfNoiseName,
       "fsRrmAPIfNoiseMacAddr": fsRrmAPIfNoiseMacAddr,
       "fsRrmAPIfNoiseSlotId": fsRrmAPIfNoiseSlotId,
       "fsRrmAPIfProfileStateTable": fsRrmAPIfProfileStateTable,
       "fsRrmAPIfProfileStateEntry": fsRrmAPIfProfileStateEntry,
       "fsRrmAPIfLoadProfileState": fsRrmAPIfLoadProfileState,
       "fsRrmAPIfInterferenceProfileState": fsRrmAPIfInterferenceProfileState,
       "fsRrmAPIfNoiseProfileState": fsRrmAPIfNoiseProfileState,
       "fsRrmAPIfCoverageProfileState": fsRrmAPIfCoverageProfileState,
       "fsRrmAPIfPerformanceProfileState": fsRrmAPIfPerformanceProfileState,
       "fsRrmAPIfProfileName": fsRrmAPIfProfileName,
       "fsRrmAPIfProfileMacAddr": fsRrmAPIfProfileMacAddr,
       "fsRrmAPIfProfileSlotId": fsRrmAPIfProfileSlotId,
       "fsRrmAPIfRxNeighborsTable": fsRrmAPIfRxNeighborsTable,
       "fsRrmAPIfRxNeighborsEntry": fsRrmAPIfRxNeighborsEntry,
       "fsRrmAPIfRxNeighborMacAddress": fsRrmAPIfRxNeighborMacAddress,
       "fsRrmAPIfRxNeighborSlot": fsRrmAPIfRxNeighborSlot,
       "fsRrmAPIfRxNeighborIpAddress": fsRrmAPIfRxNeighborIpAddress,
       "fsRrmAPIfRxNeighborRSSI": fsRrmAPIfRxNeighborRSSI,
       "fsRrmAPIfRxNeighborSNR": fsRrmAPIfRxNeighborSNR,
       "fsRrmAPIfRxNeighborChannel": fsRrmAPIfRxNeighborChannel,
       "fsRrmAPIfRxNeighborChannelWidth": fsRrmAPIfRxNeighborChannelWidth,
       "fsRrmAPIfRxNeighborName": fsRrmAPIfRxNeighborName,
       "fsRrmAPIfRxNeighborMacAddr": fsRrmAPIfRxNeighborMacAddr,
       "fsRrmAPIfRxNeighborSlotId": fsRrmAPIfRxNeighborSlotId,
       "fsRrmAPIfStationRSSICoverageInfoTable": fsRrmAPIfStationRSSICoverageInfoTable,
       "fsRrmAPIfStationRSSICoverageInfoEntry": fsRrmAPIfStationRSSICoverageInfoEntry,
       "fsRrmAPIfStationRSSICoverageIndex": fsRrmAPIfStationRSSICoverageIndex,
       "fsRrmAPIfRSSILevel": fsRrmAPIfRSSILevel,
       "fsRrmAPIfStationCountOnRSSI": fsRrmAPIfStationCountOnRSSI,
       "fsRrmAPIfStationRSSIName": fsRrmAPIfStationRSSIName,
       "fsRrmAPIfStationRSSIMacAddr": fsRrmAPIfStationRSSIMacAddr,
       "fsRrmAPIfStationRSSISlotId": fsRrmAPIfStationRSSISlotId,
       "fsRrmAPIfStationSNRCoverageInfoTable": fsRrmAPIfStationSNRCoverageInfoTable,
       "fsRrmAPIfStationSNRCoverageInfoEntry": fsRrmAPIfStationSNRCoverageInfoEntry,
       "fsRrmAPIfStationSNRCoverageIndex": fsRrmAPIfStationSNRCoverageIndex,
       "fsRrmAPIfSNRLevel": fsRrmAPIfSNRLevel,
       "fsRrmAPIfStationCountOnSNR": fsRrmAPIfStationCountOnSNR,
       "fsRrmAPIfStationSNRName": fsRrmAPIfStationSNRName,
       "fsRrmAPIfStationSNRMacAddr": fsRrmAPIfStationSNRMacAddr,
       "fsRrmAPIfStationSNRSlotId": fsRrmAPIfStationSNRSlotId,
       "fsRrmAPIfRecommendedRFParametersTable": fsRrmAPIfRecommendedRFParametersTable,
       "fsRrmAPIfRecommendedRFParametersEntry": fsRrmAPIfRecommendedRFParametersEntry,
       "fsRrmAPIfRecommendedChannelNumber": fsRrmAPIfRecommendedChannelNumber,
       "fsRrmAPIfRecommendedTxPowerLevel": fsRrmAPIfRecommendedTxPowerLevel,
       "fsRrmAPIfRecommendedRTSThreshold": fsRrmAPIfRecommendedRTSThreshold,
       "fsRrmAPIfRecommendedFragmentationThreshold": fsRrmAPIfRecommendedFragmentationThreshold,
       "fsRrmAPIfRecommendedName": fsRrmAPIfRecommendedName,
       "fsRrmAPIfRecommendedMacAddr": fsRrmAPIfRecommendedMacAddr,
       "fsRrmAPIfRecommendedSlotId": fsRrmAPIfRecommendedSlotId,
       "fsRrmAPRadioTable": fsRrmAPRadioTable,
       "fsRrmAPRadioEntry": fsRrmAPRadioEntry,
       "fsRrmAPRadioID": fsRrmAPRadioID,
       "fsRrmAPRadioType": fsRrmAPRadioType,
       "fsRrmAPRealName": fsRrmAPRealName,
       "fsRrmAPMacAddr": fsRrmAPMacAddr,
       "fsRrmAPIfThroughputParametersTable": fsRrmAPIfThroughputParametersTable,
       "fsRrmAPIfThroughputParametersEntry": fsRrmAPIfThroughputParametersEntry,
       "fsRrmAPIfThroughputMacAddr": fsRrmAPIfThroughputMacAddr,
       "fsRrmAPIfThroughputSlotId": fsRrmAPIfThroughputSlotId,
       "fsRrmAPIfThroughputAPName": fsRrmAPIfThroughputAPName,
       "fsRrmAPIfThroughputRx": fsRrmAPIfThroughputRx,
       "fsRrmAPIfThroughputTx": fsRrmAPIfThroughputTx,
       "fsRrmAPIfThroughputTotal": fsRrmAPIfThroughputTotal,
       "fsRrmAPSnrBSSIDTable": fsRrmAPSnrBSSIDTable,
       "fsRrmAPSnrBSSIDEntry": fsRrmAPSnrBSSIDEntry,
       "fsRrmAPSnrBSSIDMacAddr": fsRrmAPSnrBSSIDMacAddr,
       "fsRrmAPSnrBSSIDSlotId": fsRrmAPSnrBSSIDSlotId,
       "fsRrmAPSnrBSSIDAPName": fsRrmAPSnrBSSIDAPName,
       "fsRrmAPSnrBSSIDAverageSignalStrength": fsRrmAPSnrBSSIDAverageSignalStrength,
       "fsRrmAPSnrBSSIDSignalPkts": fsRrmAPSnrBSSIDSignalPkts,
       "fsRrmAPSnrBSSIDHighestRxSignalStrength": fsRrmAPSnrBSSIDHighestRxSignalStrength,
       "fsRrmAPSnrBSSIDLowestRxSignalStrength": fsRrmAPSnrBSSIDLowestRxSignalStrength,
       "fsRrmAPSnrBSSIDSampleTime": fsRrmAPSnrBSSIDSampleTime,
       "fsRrmMIBTraps": fsRrmMIBTraps,
       "fsRrmTrapControl": fsRrmTrapControl,
       "fsRrmAPDot11bProfileTrapControlMask": fsRrmAPDot11bProfileTrapControlMask,
       "fsRrmAPDot11aProfileTrapControlMask": fsRrmAPDot11aProfileTrapControlMask,
       "fsRrmAPDot11bParamUpdateTrapControlMask": fsRrmAPDot11bParamUpdateTrapControlMask,
       "fsRrmAPDot11aParamUpdateTrapControlMask": fsRrmAPDot11aParamUpdateTrapControlMask,
       "fsRrmTrapVariable": fsRrmTrapVariable,
       "fsRrmAPMacAddrTrapVariable": fsRrmAPMacAddrTrapVariable,
       "fsRrmAPRadioIDTrapVariable": fsRrmAPRadioIDTrapVariable,
       "fsRrmAPRadioTypeTrapVariable": fsRrmAPRadioTypeTrapVariable,
       "fsRrmClientNumberTrapVariable": fsRrmClientNumberTrapVariable,
       "fsRrmForeignInterfereTrapVariable": fsRrmForeignInterfereTrapVariable,
       "fsRrmNoiseTrapVariable": fsRrmNoiseTrapVariable,
       "fsRrmThroughputTrapVariable": fsRrmThroughputTrapVariable,
       "fsRrmUtilizationTrapVariable": fsRrmUtilizationTrapVariable,
       "fsRrmAPTxPowerBeforeChange": fsRrmAPTxPowerBeforeChange,
       "fsRrmAPTxPowerAfterChange": fsRrmAPTxPowerAfterChange,
       "fsRrmAPChannelNumberBeforeChannge": fsRrmAPChannelNumberBeforeChannge,
       "fsRrmAPChannelNumberAfterChannge": fsRrmAPChannelNumberAfterChannge,
       "fsRrmDot11bGroupLeaderMacAddrTrapVariable": fsRrmDot11bGroupLeaderMacAddrTrapVariable,
       "fsRrmDot11aGroupLeaderMacAddrTrapVariable": fsRrmDot11aGroupLeaderMacAddrTrapVariable,
       "fsRrmAPChannelChangeReason": fsRrmAPChannelChangeReason,
       "fsRrmAPChannelChangeReasonValue": fsRrmAPChannelChangeReasonValue,
       "fsRrmAPTxPowerChangeCoverageFlag": fsRrmAPTxPowerChangeCoverageFlag,
       "fsRrmDFSFreeCount": fsRrmDFSFreeCount,
       "fsRrmAPChannelChangeCount": fsRrmAPChannelChangeCount,
       "fsRrmTraps": fsRrmTraps,
       "fsRrmAPClientNumProfileFailed": fsRrmAPClientNumProfileFailed,
       "fsRrmAPLoadProfileFailed": fsRrmAPLoadProfileFailed,
       "fsRrmAPNoiseProfileFailed": fsRrmAPNoiseProfileFailed,
       "fsRrmAPInterferenceProfileFailed": fsRrmAPInterferenceProfileFailed,
       "fsRrmAPPerformanceProfileFailed": fsRrmAPPerformanceProfileFailed,
       "fsRrmAPClientNumProfileUpdatedToPass": fsRrmAPClientNumProfileUpdatedToPass,
       "fsRrmAPLoadProfileUpdatedToPass": fsRrmAPLoadProfileUpdatedToPass,
       "fsRrmAPNoiseProfileUpdatedToPass": fsRrmAPNoiseProfileUpdatedToPass,
       "fsRrmAPInterferenceProfileUpdatedToPass": fsRrmAPInterferenceProfileUpdatedToPass,
       "fsRrmAPPerformanceProfileUpdatedToPass": fsRrmAPPerformanceProfileUpdatedToPass,
       "fsRrmAPCurrentTxPowerChanged": fsRrmAPCurrentTxPowerChanged,
       "fsRrmAPCurrentChannelChanged": fsRrmAPCurrentChannelChanged,
       "fsRrmDot11bGroupingDone": fsRrmDot11bGroupingDone,
       "fsRrmDot11aGroupingDone": fsRrmDot11aGroupingDone,
       "fsRrmDot11bDFSFreeCountBelowThreshold": fsRrmDot11bDFSFreeCountBelowThreshold,
       "fsRrmDot11aDFSFreeCountBelowThreshold": fsRrmDot11aDFSFreeCountBelowThreshold,
       "fsRrmNeighborAPInterference": fsRrmNeighborAPInterference,
       "fsRrmStationInterference": fsRrmStationInterference,
       "fsRrmOtherDiveceInterference": fsRrmOtherDiveceInterference,
       "fsRrmMIBConformance": fsRrmMIBConformance,
       "fsRrmMIBCompliances": fsRrmMIBCompliances,
       "fsRrmMIBCompliance": fsRrmMIBCompliance,
       "fsRrmMIBGroups": fsRrmMIBGroups,
       "fsRrmMIBGroup": fsRrmMIBGroup,
       "fsRrmTrapsGroup": fsRrmTrapsGroup,
       "fsRrmTrap": fsRrmTrap}
)
