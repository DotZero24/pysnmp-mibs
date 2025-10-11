# SNMP MIB module (QTECH-RRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-RRM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:03 2025
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

qtechRrmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63)
)
if mibBuilder.loadTexts:
    qtechRrmMIB.setRevisions(
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

_QtechRrmMIBObjects_ObjectIdentity = ObjectIdentity
qtechRrmMIBObjects = _QtechRrmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1)
)
_QtechRrmObjectsGroup_ObjectIdentity = ObjectIdentity
qtechRrmObjectsGroup = _QtechRrmObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 1)
)


class _QtechRrmRFNetworkName_Type(DisplayString):
    """Custom type qtechRrmRFNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_QtechRrmRFNetworkName_Type.__name__ = "DisplayString"
_QtechRrmRFNetworkName_Object = MibScalar
qtechRrmRFNetworkName = _QtechRrmRFNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 1, 1),
    _QtechRrmRFNetworkName_Type()
)
qtechRrmRFNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmRFNetworkName.setStatus("current")
_QtechRrmObjectsDot11a_ObjectIdentity = ObjectIdentity
qtechRrmObjectsDot11a = _QtechRrmObjectsDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2)
)
_QtechRrmDCADot11a_ObjectIdentity = ObjectIdentity
qtechRrmDCADot11a = _QtechRrmDCADot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1)
)


class _QtechRrmDot11aDynamicChannelAssignment_Type(Integer32):
    """Custom type qtechRrmDot11aDynamicChannelAssignment based on Integer32"""
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


_QtechRrmDot11aDynamicChannelAssignment_Type.__name__ = "Integer32"
_QtechRrmDot11aDynamicChannelAssignment_Object = MibScalar
qtechRrmDot11aDynamicChannelAssignment = _QtechRrmDot11aDynamicChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 1),
    _QtechRrmDot11aDynamicChannelAssignment_Type()
)
qtechRrmDot11aDynamicChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aDynamicChannelAssignment.setStatus("current")


class _QtechRrmDot11aAnchorTime_Type(Unsigned32):
    """Custom type qtechRrmDot11aAnchorTime based on Unsigned32"""
    defaultValue = 0


_QtechRrmDot11aAnchorTime_Type.__name__ = "Unsigned32"
_QtechRrmDot11aAnchorTime_Object = MibScalar
qtechRrmDot11aAnchorTime = _QtechRrmDot11aAnchorTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 2),
    _QtechRrmDot11aAnchorTime_Type()
)
qtechRrmDot11aAnchorTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aAnchorTime.setStatus("current")


class _QtechRrmDot11aChannalWidth11n_Type(Unsigned32):
    """Custom type qtechRrmDot11aChannalWidth11n based on Unsigned32"""
    defaultValue = 20


_QtechRrmDot11aChannalWidth11n_Type.__name__ = "Unsigned32"
_QtechRrmDot11aChannalWidth11n_Object = MibScalar
qtechRrmDot11aChannalWidth11n = _QtechRrmDot11aChannalWidth11n_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 3),
    _QtechRrmDot11aChannalWidth11n_Type()
)
qtechRrmDot11aChannalWidth11n.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aChannalWidth11n.setStatus("current")


class _QtechRrmDot11aDynamicChannelUpdateInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11aDynamicChannelUpdateInterval based on Unsigned32"""
    defaultValue = 600


_QtechRrmDot11aDynamicChannelUpdateInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11aDynamicChannelUpdateInterval_Object = MibScalar
qtechRrmDot11aDynamicChannelUpdateInterval = _QtechRrmDot11aDynamicChannelUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 4),
    _QtechRrmDot11aDynamicChannelUpdateInterval_Type()
)
qtechRrmDot11aDynamicChannelUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aDynamicChannelUpdateInterval.setStatus("current")


class _QtechRrmDot11aDCASensitivity_Type(Integer32):
    """Custom type qtechRrmDot11aDCASensitivity based on Integer32"""
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


_QtechRrmDot11aDCASensitivity_Type.__name__ = "Integer32"
_QtechRrmDot11aDCASensitivity_Object = MibScalar
qtechRrmDot11aDCASensitivity = _QtechRrmDot11aDCASensitivity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 5),
    _QtechRrmDot11aDCASensitivity_Type()
)
qtechRrmDot11aDCASensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aDCASensitivity.setStatus("current")


class _QtechRrmDot11aForeignInterfereFactorEnable_Type(Integer32):
    """Custom type qtechRrmDot11aForeignInterfereFactorEnable based on Integer32"""
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


_QtechRrmDot11aForeignInterfereFactorEnable_Type.__name__ = "Integer32"
_QtechRrmDot11aForeignInterfereFactorEnable_Object = MibScalar
qtechRrmDot11aForeignInterfereFactorEnable = _QtechRrmDot11aForeignInterfereFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 6),
    _QtechRrmDot11aForeignInterfereFactorEnable_Type()
)
qtechRrmDot11aForeignInterfereFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aForeignInterfereFactorEnable.setStatus("current")


class _QtechRrmDot11aLoadFactorEnable_Type(Integer32):
    """Custom type qtechRrmDot11aLoadFactorEnable based on Integer32"""
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


_QtechRrmDot11aLoadFactorEnable_Type.__name__ = "Integer32"
_QtechRrmDot11aLoadFactorEnable_Object = MibScalar
qtechRrmDot11aLoadFactorEnable = _QtechRrmDot11aLoadFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 7),
    _QtechRrmDot11aLoadFactorEnable_Type()
)
qtechRrmDot11aLoadFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aLoadFactorEnable.setStatus("current")


class _QtechRrmDot11aNoiseFactorEnable_Type(Integer32):
    """Custom type qtechRrmDot11aNoiseFactorEnable based on Integer32"""
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


_QtechRrmDot11aNoiseFactorEnable_Type.__name__ = "Integer32"
_QtechRrmDot11aNoiseFactorEnable_Object = MibScalar
qtechRrmDot11aNoiseFactorEnable = _QtechRrmDot11aNoiseFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 8),
    _QtechRrmDot11aNoiseFactorEnable_Type()
)
qtechRrmDot11aNoiseFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aNoiseFactorEnable.setStatus("current")


class _QtechRrmDot11aChannelUpdateCmdInvoke_Type(Integer32):
    """Custom type qtechRrmDot11aChannelUpdateCmdInvoke based on Integer32"""
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


_QtechRrmDot11aChannelUpdateCmdInvoke_Type.__name__ = "Integer32"
_QtechRrmDot11aChannelUpdateCmdInvoke_Object = MibScalar
qtechRrmDot11aChannelUpdateCmdInvoke = _QtechRrmDot11aChannelUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 9),
    _QtechRrmDot11aChannelUpdateCmdInvoke_Type()
)
qtechRrmDot11aChannelUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aChannelUpdateCmdInvoke.setStatus("current")
_QtechRrmDot11aDCAChannelTable_Object = MibTable
qtechRrmDot11aDCAChannelTable = _QtechRrmDot11aDCAChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    qtechRrmDot11aDCAChannelTable.setStatus("current")
_QtechRrmDot11aDCAChannelEntry_Object = MibTableRow
qtechRrmDot11aDCAChannelEntry = _QtechRrmDot11aDCAChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 10, 1)
)
qtechRrmDot11aDCAChannelEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmDot11aDCAChannelIndex"),
)
if mibBuilder.loadTexts:
    qtechRrmDot11aDCAChannelEntry.setStatus("current")
_QtechRrmDot11aDCAChannelIndex_Type = Integer32
_QtechRrmDot11aDCAChannelIndex_Object = MibTableColumn
qtechRrmDot11aDCAChannelIndex = _QtechRrmDot11aDCAChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 10, 1, 1),
    _QtechRrmDot11aDCAChannelIndex_Type()
)
qtechRrmDot11aDCAChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aDCAChannelIndex.setStatus("current")


class _QtechRrmDot11aDCAChannelOperation_Type(Integer32):
    """Custom type qtechRrmDot11aDCAChannelOperation based on Integer32"""
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


_QtechRrmDot11aDCAChannelOperation_Type.__name__ = "Integer32"
_QtechRrmDot11aDCAChannelOperation_Object = MibTableColumn
qtechRrmDot11aDCAChannelOperation = _QtechRrmDot11aDCAChannelOperation_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 1, 10, 1, 2),
    _QtechRrmDot11aDCAChannelOperation_Type()
)
qtechRrmDot11aDCAChannelOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aDCAChannelOperation.setStatus("current")
_QtechRrmTPCDot11a_ObjectIdentity = ObjectIdentity
qtechRrmTPCDot11a = _QtechRrmTPCDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 2)
)


class _QtechRrmDot11aDTPCSupport_Type(Integer32):
    """Custom type qtechRrmDot11aDTPCSupport based on Integer32"""
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


_QtechRrmDot11aDTPCSupport_Type.__name__ = "Integer32"
_QtechRrmDot11aDTPCSupport_Object = MibScalar
qtechRrmDot11aDTPCSupport = _QtechRrmDot11aDTPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 2, 1),
    _QtechRrmDot11aDTPCSupport_Type()
)
qtechRrmDot11aDTPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aDTPCSupport.setStatus("current")


class _QtechRrmDot11aDynamicTransmitPowerControl_Type(Integer32):
    """Custom type qtechRrmDot11aDynamicTransmitPowerControl based on Integer32"""
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


_QtechRrmDot11aDynamicTransmitPowerControl_Type.__name__ = "Integer32"
_QtechRrmDot11aDynamicTransmitPowerControl_Object = MibScalar
qtechRrmDot11aDynamicTransmitPowerControl = _QtechRrmDot11aDynamicTransmitPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 2, 2),
    _QtechRrmDot11aDynamicTransmitPowerControl_Type()
)
qtechRrmDot11aDynamicTransmitPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aDynamicTransmitPowerControl.setStatus("current")


class _QtechRrmDot11aDynamicTxPowerControlInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11aDynamicTxPowerControlInterval based on Unsigned32"""
    defaultValue = 600


_QtechRrmDot11aDynamicTxPowerControlInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11aDynamicTxPowerControlInterval_Object = MibScalar
qtechRrmDot11aDynamicTxPowerControlInterval = _QtechRrmDot11aDynamicTxPowerControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 2, 3),
    _QtechRrmDot11aDynamicTxPowerControlInterval_Type()
)
qtechRrmDot11aDynamicTxPowerControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aDynamicTxPowerControlInterval.setStatus("current")


class _QtechRrmDot11aCurrentTxPowerLevel_Type(Integer32):
    """Custom type qtechRrmDot11aCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QtechRrmDot11aCurrentTxPowerLevel_Type.__name__ = "Integer32"
_QtechRrmDot11aCurrentTxPowerLevel_Object = MibScalar
qtechRrmDot11aCurrentTxPowerLevel = _QtechRrmDot11aCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 2, 4),
    _QtechRrmDot11aCurrentTxPowerLevel_Type()
)
qtechRrmDot11aCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCurrentTxPowerLevel.setStatus("current")


class _QtechRrmDot11aPowerUpdateCmdInvoke_Type(Integer32):
    """Custom type qtechRrmDot11aPowerUpdateCmdInvoke based on Integer32"""
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


_QtechRrmDot11aPowerUpdateCmdInvoke_Type.__name__ = "Integer32"
_QtechRrmDot11aPowerUpdateCmdInvoke_Object = MibScalar
qtechRrmDot11aPowerUpdateCmdInvoke = _QtechRrmDot11aPowerUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 2, 5),
    _QtechRrmDot11aPowerUpdateCmdInvoke_Type()
)
qtechRrmDot11aPowerUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aPowerUpdateCmdInvoke.setStatus("current")


class _QtechRrmDot11aTXPowerThreshold_Type(Integer32):
    """Custom type qtechRrmDot11aTXPowerThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_QtechRrmDot11aTXPowerThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11aTXPowerThreshold_Object = MibScalar
qtechRrmDot11aTXPowerThreshold = _QtechRrmDot11aTXPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 2, 6),
    _QtechRrmDot11aTXPowerThreshold_Type()
)
qtechRrmDot11aTXPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aTXPowerThreshold.setStatus("current")


class _QtechRrmDot11aTPCNeighborNumber_Type(Integer32):
    """Custom type qtechRrmDot11aTPCNeighborNumber based on Integer32"""
    defaultValue = 3


_QtechRrmDot11aTPCNeighborNumber_Type.__name__ = "Integer32"
_QtechRrmDot11aTPCNeighborNumber_Object = MibScalar
qtechRrmDot11aTPCNeighborNumber = _QtechRrmDot11aTPCNeighborNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 2, 7),
    _QtechRrmDot11aTPCNeighborNumber_Type()
)
qtechRrmDot11aTPCNeighborNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aTPCNeighborNumber.setStatus("current")
_QtechRrmCHDDot11a_ObjectIdentity = ObjectIdentity
qtechRrmCHDDot11a = _QtechRrmCHDDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3)
)


class _QtechRrmDot11aCoverageEnable_Type(Integer32):
    """Custom type qtechRrmDot11aCoverageEnable based on Integer32"""
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


_QtechRrmDot11aCoverageEnable_Type.__name__ = "Integer32"
_QtechRrmDot11aCoverageEnable_Object = MibScalar
qtechRrmDot11aCoverageEnable = _QtechRrmDot11aCoverageEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3, 1),
    _QtechRrmDot11aCoverageEnable_Type()
)
qtechRrmDot11aCoverageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageEnable.setStatus("current")


class _QtechRrmDot11aCoverageExceptionGlobal_Type(Integer32):
    """Custom type qtechRrmDot11aCoverageExceptionGlobal based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11aCoverageExceptionGlobal_Type.__name__ = "Integer32"
_QtechRrmDot11aCoverageExceptionGlobal_Object = MibScalar
qtechRrmDot11aCoverageExceptionGlobal = _QtechRrmDot11aCoverageExceptionGlobal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3, 2),
    _QtechRrmDot11aCoverageExceptionGlobal_Type()
)
qtechRrmDot11aCoverageExceptionGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageExceptionGlobal.setStatus("current")


class _QtechRrmDot11aCoverageLevelGlobal_Type(Integer32):
    """Custom type qtechRrmDot11aCoverageLevelGlobal based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_QtechRrmDot11aCoverageLevelGlobal_Type.__name__ = "Integer32"
_QtechRrmDot11aCoverageLevelGlobal_Object = MibScalar
qtechRrmDot11aCoverageLevelGlobal = _QtechRrmDot11aCoverageLevelGlobal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3, 3),
    _QtechRrmDot11aCoverageLevelGlobal_Type()
)
qtechRrmDot11aCoverageLevelGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageLevelGlobal.setStatus("current")


class _QtechRrmDot11aCoverageDataRSSIThreshold_Type(Integer32):
    """Custom type qtechRrmDot11aCoverageDataRSSIThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_QtechRrmDot11aCoverageDataRSSIThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11aCoverageDataRSSIThreshold_Object = MibScalar
qtechRrmDot11aCoverageDataRSSIThreshold = _QtechRrmDot11aCoverageDataRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3, 4),
    _QtechRrmDot11aCoverageDataRSSIThreshold_Type()
)
qtechRrmDot11aCoverageDataRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageDataRSSIThreshold.setStatus("current")


class _QtechRrmDot11aCoverageVoiceRSSIThreshold_Type(Integer32):
    """Custom type qtechRrmDot11aCoverageVoiceRSSIThreshold based on Integer32"""
    defaultValue = -75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_QtechRrmDot11aCoverageVoiceRSSIThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11aCoverageVoiceRSSIThreshold_Object = MibScalar
qtechRrmDot11aCoverageVoiceRSSIThreshold = _QtechRrmDot11aCoverageVoiceRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3, 5),
    _QtechRrmDot11aCoverageVoiceRSSIThreshold_Type()
)
qtechRrmDot11aCoverageVoiceRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageVoiceRSSIThreshold.setStatus("current")


class _QtechRrmDot11aCoverageDataPacketCount_Type(Integer32):
    """Custom type qtechRrmDot11aCoverageDataPacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechRrmDot11aCoverageDataPacketCount_Type.__name__ = "Integer32"
_QtechRrmDot11aCoverageDataPacketCount_Object = MibScalar
qtechRrmDot11aCoverageDataPacketCount = _QtechRrmDot11aCoverageDataPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3, 6),
    _QtechRrmDot11aCoverageDataPacketCount_Type()
)
qtechRrmDot11aCoverageDataPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageDataPacketCount.setStatus("current")


class _QtechRrmDot11aCoverageVoicePacketCount_Type(Integer32):
    """Custom type qtechRrmDot11aCoverageVoicePacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechRrmDot11aCoverageVoicePacketCount_Type.__name__ = "Integer32"
_QtechRrmDot11aCoverageVoicePacketCount_Object = MibScalar
qtechRrmDot11aCoverageVoicePacketCount = _QtechRrmDot11aCoverageVoicePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3, 7),
    _QtechRrmDot11aCoverageVoicePacketCount_Type()
)
qtechRrmDot11aCoverageVoicePacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageVoicePacketCount.setStatus("current")


class _QtechRrmDot11aCoverageDataFailRate_Type(Integer32):
    """Custom type qtechRrmDot11aCoverageDataFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11aCoverageDataFailRate_Type.__name__ = "Integer32"
_QtechRrmDot11aCoverageDataFailRate_Object = MibScalar
qtechRrmDot11aCoverageDataFailRate = _QtechRrmDot11aCoverageDataFailRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3, 8),
    _QtechRrmDot11aCoverageDataFailRate_Type()
)
qtechRrmDot11aCoverageDataFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageDataFailRate.setStatus("current")


class _QtechRrmDot11aCoverageVoiceFailRate_Type(Integer32):
    """Custom type qtechRrmDot11aCoverageVoiceFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11aCoverageVoiceFailRate_Type.__name__ = "Integer32"
_QtechRrmDot11aCoverageVoiceFailRate_Object = MibScalar
qtechRrmDot11aCoverageVoiceFailRate = _QtechRrmDot11aCoverageVoiceFailRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 3, 9),
    _QtechRrmDot11aCoverageVoiceFailRate_Type()
)
qtechRrmDot11aCoverageVoiceFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageVoiceFailRate.setStatus("current")
_QtechRrmGroupDot11a_ObjectIdentity = ObjectIdentity
qtechRrmGroupDot11a = _QtechRrmGroupDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4)
)


class _QtechRrmDot11aGlobalAutomaticGrouping_Type(Integer32):
    """Custom type qtechRrmDot11aGlobalAutomaticGrouping based on Integer32"""
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


_QtechRrmDot11aGlobalAutomaticGrouping_Type.__name__ = "Integer32"
_QtechRrmDot11aGlobalAutomaticGrouping_Object = MibScalar
qtechRrmDot11aGlobalAutomaticGrouping = _QtechRrmDot11aGlobalAutomaticGrouping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 1),
    _QtechRrmDot11aGlobalAutomaticGrouping_Type()
)
qtechRrmDot11aGlobalAutomaticGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aGlobalAutomaticGrouping.setStatus("current")
_QtechRrmDot11aGroupLeaderMacAddr_Type = MacAddress
_QtechRrmDot11aGroupLeaderMacAddr_Object = MibScalar
qtechRrmDot11aGroupLeaderMacAddr = _QtechRrmDot11aGroupLeaderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 2),
    _QtechRrmDot11aGroupLeaderMacAddr_Type()
)
qtechRrmDot11aGroupLeaderMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aGroupLeaderMacAddr.setStatus("current")


class _QtechRrmDot11aGroupLeader_Type(Integer32):
    """Custom type qtechRrmDot11aGroupLeader based on Integer32"""
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


_QtechRrmDot11aGroupLeader_Type.__name__ = "Integer32"
_QtechRrmDot11aGroupLeader_Object = MibScalar
qtechRrmDot11aGroupLeader = _QtechRrmDot11aGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 3),
    _QtechRrmDot11aGroupLeader_Type()
)
qtechRrmDot11aGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aGroupLeader.setStatus("current")
_QtechRrmDot11aGroupLastUpdateTime_Type = Unsigned32
_QtechRrmDot11aGroupLastUpdateTime_Object = MibScalar
qtechRrmDot11aGroupLastUpdateTime = _QtechRrmDot11aGroupLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 4),
    _QtechRrmDot11aGroupLastUpdateTime_Type()
)
qtechRrmDot11aGroupLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aGroupLastUpdateTime.setStatus("current")


class _QtechRrmDot11aGroupInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11aGroupInterval based on Unsigned32"""
    defaultValue = 3600


_QtechRrmDot11aGroupInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11aGroupInterval_Object = MibScalar
qtechRrmDot11aGroupInterval = _QtechRrmDot11aGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 5),
    _QtechRrmDot11aGroupInterval_Type()
)
qtechRrmDot11aGroupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aGroupInterval.setStatus("current")
_QtechRrmDot11aGroupTable_Object = MibTable
qtechRrmDot11aGroupTable = _QtechRrmDot11aGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 6)
)
if mibBuilder.loadTexts:
    qtechRrmDot11aGroupTable.setStatus("current")
_QtechRrmDot11aGroupEntry_Object = MibTableRow
qtechRrmDot11aGroupEntry = _QtechRrmDot11aGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 6, 1)
)
qtechRrmDot11aGroupEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmDot11aPeerMacAddress"),
)
if mibBuilder.loadTexts:
    qtechRrmDot11aGroupEntry.setStatus("current")
_QtechRrmDot11aPeerMacAddress_Type = MacAddress
_QtechRrmDot11aPeerMacAddress_Object = MibTableColumn
qtechRrmDot11aPeerMacAddress = _QtechRrmDot11aPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 6, 1, 1),
    _QtechRrmDot11aPeerMacAddress_Type()
)
qtechRrmDot11aPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aPeerMacAddress.setStatus("current")
_QtechRrmDot11aPeerIpAddress_Type = IpAddress
_QtechRrmDot11aPeerIpAddress_Object = MibTableColumn
qtechRrmDot11aPeerIpAddress = _QtechRrmDot11aPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 6, 1, 2),
    _QtechRrmDot11aPeerIpAddress_Type()
)
qtechRrmDot11aPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aPeerIpAddress.setStatus("current")
_QtechRrmDot11aSummaryTable_Object = MibTable
qtechRrmDot11aSummaryTable = _QtechRrmDot11aSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 7)
)
if mibBuilder.loadTexts:
    qtechRrmDot11aSummaryTable.setStatus("current")
_QtechRrmDot11aSummaryEntry_Object = MibTableRow
qtechRrmDot11aSummaryEntry = _QtechRrmDot11aSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1)
)
qtechRrmDot11aSummaryEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmDot11aSummaryMacAddress"),
    (0, "QTECH-RRM-MIB", "qtechRrmDot11aAPRadioID"),
)
if mibBuilder.loadTexts:
    qtechRrmDot11aSummaryEntry.setStatus("current")
_QtechRrmDot11aAPname_Type = DisplayString
_QtechRrmDot11aAPname_Object = MibTableColumn
qtechRrmDot11aAPname = _QtechRrmDot11aAPname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 1),
    _QtechRrmDot11aAPname_Type()
)
qtechRrmDot11aAPname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aAPname.setStatus("current")
_QtechRrmDot11aAPRadioID_Type = Unsigned32
_QtechRrmDot11aAPRadioID_Object = MibTableColumn
qtechRrmDot11aAPRadioID = _QtechRrmDot11aAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 2),
    _QtechRrmDot11aAPRadioID_Type()
)
qtechRrmDot11aAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aAPRadioID.setStatus("current")
_QtechRrmDot11aAPChannel_Type = Unsigned32
_QtechRrmDot11aAPChannel_Object = MibTableColumn
qtechRrmDot11aAPChannel = _QtechRrmDot11aAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 3),
    _QtechRrmDot11aAPChannel_Type()
)
qtechRrmDot11aAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aAPChannel.setStatus("current")
_QtechRrmDot11aAPTxPower_Type = Unsigned32
_QtechRrmDot11aAPTxPower_Object = MibTableColumn
qtechRrmDot11aAPTxPower = _QtechRrmDot11aAPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 4),
    _QtechRrmDot11aAPTxPower_Type()
)
qtechRrmDot11aAPTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aAPTxPower.setStatus("current")


class _QtechRrmDot11aAPChannelRrmChangeFlag_Type(Integer32):
    """Custom type qtechRrmDot11aAPChannelRrmChangeFlag based on Integer32"""
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


_QtechRrmDot11aAPChannelRrmChangeFlag_Type.__name__ = "Integer32"
_QtechRrmDot11aAPChannelRrmChangeFlag_Object = MibTableColumn
qtechRrmDot11aAPChannelRrmChangeFlag = _QtechRrmDot11aAPChannelRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 5),
    _QtechRrmDot11aAPChannelRrmChangeFlag_Type()
)
qtechRrmDot11aAPChannelRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aAPChannelRrmChangeFlag.setStatus("current")


class _QtechRrmDot11aAPTxPowerRrmChangeFlag_Type(Integer32):
    """Custom type qtechRrmDot11aAPTxPowerRrmChangeFlag based on Integer32"""
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


_QtechRrmDot11aAPTxPowerRrmChangeFlag_Type.__name__ = "Integer32"
_QtechRrmDot11aAPTxPowerRrmChangeFlag_Object = MibTableColumn
qtechRrmDot11aAPTxPowerRrmChangeFlag = _QtechRrmDot11aAPTxPowerRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 6),
    _QtechRrmDot11aAPTxPowerRrmChangeFlag_Type()
)
qtechRrmDot11aAPTxPowerRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aAPTxPowerRrmChangeFlag.setStatus("current")
_QtechRrmDot11aSummaryMacAddress_Type = MacAddress
_QtechRrmDot11aSummaryMacAddress_Object = MibTableColumn
qtechRrmDot11aSummaryMacAddress = _QtechRrmDot11aSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 4, 7, 1, 7),
    _QtechRrmDot11aSummaryMacAddress_Type()
)
qtechRrmDot11aSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11aSummaryMacAddress.setStatus("current")
_QtechRrmProfileDot11a_ObjectIdentity = ObjectIdentity
qtechRrmProfileDot11a = _QtechRrmProfileDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 5)
)


class _QtechRrmDot11aForeignInterferenceThreshold_Type(Integer32):
    """Custom type qtechRrmDot11aForeignInterferenceThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11aForeignInterferenceThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11aForeignInterferenceThreshold_Object = MibScalar
qtechRrmDot11aForeignInterferenceThreshold = _QtechRrmDot11aForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 5, 1),
    _QtechRrmDot11aForeignInterferenceThreshold_Type()
)
qtechRrmDot11aForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aForeignInterferenceThreshold.setStatus("current")


class _QtechRrmDot11aForeignNoiseThreshold_Type(Integer32):
    """Custom type qtechRrmDot11aForeignNoiseThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_QtechRrmDot11aForeignNoiseThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11aForeignNoiseThreshold_Object = MibScalar
qtechRrmDot11aForeignNoiseThreshold = _QtechRrmDot11aForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 5, 2),
    _QtechRrmDot11aForeignNoiseThreshold_Type()
)
qtechRrmDot11aForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aForeignNoiseThreshold.setStatus("current")


class _QtechRrmDot11aRFUtilizationThreshold_Type(Integer32):
    """Custom type qtechRrmDot11aRFUtilizationThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11aRFUtilizationThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11aRFUtilizationThreshold_Object = MibScalar
qtechRrmDot11aRFUtilizationThreshold = _QtechRrmDot11aRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 5, 3),
    _QtechRrmDot11aRFUtilizationThreshold_Type()
)
qtechRrmDot11aRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aRFUtilizationThreshold.setStatus("current")


class _QtechRrmDot11aThroughputThreshold_Type(Unsigned32):
    """Custom type qtechRrmDot11aThroughputThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000000),
    )


_QtechRrmDot11aThroughputThreshold_Type.__name__ = "Unsigned32"
_QtechRrmDot11aThroughputThreshold_Object = MibScalar
qtechRrmDot11aThroughputThreshold = _QtechRrmDot11aThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 5, 4),
    _QtechRrmDot11aThroughputThreshold_Type()
)
qtechRrmDot11aThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aThroughputThreshold.setStatus("current")


class _QtechRrmDot11aMobilesThreshold_Type(Integer32):
    """Custom type qtechRrmDot11aMobilesThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_QtechRrmDot11aMobilesThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11aMobilesThreshold_Object = MibScalar
qtechRrmDot11aMobilesThreshold = _QtechRrmDot11aMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 5, 5),
    _QtechRrmDot11aMobilesThreshold_Type()
)
qtechRrmDot11aMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aMobilesThreshold.setStatus("current")
_QtechRrmMonitorDot11a_ObjectIdentity = ObjectIdentity
qtechRrmMonitorDot11a = _QtechRrmMonitorDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 6)
)


class _QtechRrmDot11aMonitorEnable_Type(Integer32):
    """Custom type qtechRrmDot11aMonitorEnable based on Integer32"""
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


_QtechRrmDot11aMonitorEnable_Type.__name__ = "Integer32"
_QtechRrmDot11aMonitorEnable_Object = MibScalar
qtechRrmDot11aMonitorEnable = _QtechRrmDot11aMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 6, 1),
    _QtechRrmDot11aMonitorEnable_Type()
)
qtechRrmDot11aMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aMonitorEnable.setStatus("current")


class _QtechRrmDot11aChannelMonitorList_Type(Integer32):
    """Custom type qtechRrmDot11aChannelMonitorList based on Integer32"""
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


_QtechRrmDot11aChannelMonitorList_Type.__name__ = "Integer32"
_QtechRrmDot11aChannelMonitorList_Object = MibScalar
qtechRrmDot11aChannelMonitorList = _QtechRrmDot11aChannelMonitorList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 6, 2),
    _QtechRrmDot11aChannelMonitorList_Type()
)
qtechRrmDot11aChannelMonitorList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aChannelMonitorList.setStatus("current")


class _QtechRrmDot11aMonitorInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11aMonitorInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11aMonitorInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11aMonitorInterval_Object = MibScalar
qtechRrmDot11aMonitorInterval = _QtechRrmDot11aMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 6, 3),
    _QtechRrmDot11aMonitorInterval_Type()
)
qtechRrmDot11aMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aMonitorInterval.setStatus("current")


class _QtechRrmDot11aCoverageMeasurementInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11aCoverageMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11aCoverageMeasurementInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11aCoverageMeasurementInterval_Object = MibScalar
qtechRrmDot11aCoverageMeasurementInterval = _QtechRrmDot11aCoverageMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 6, 4),
    _QtechRrmDot11aCoverageMeasurementInterval_Type()
)
qtechRrmDot11aCoverageMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aCoverageMeasurementInterval.setStatus("current")


class _QtechRrmDot11aLoadMeasurementInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11aLoadMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11aLoadMeasurementInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11aLoadMeasurementInterval_Object = MibScalar
qtechRrmDot11aLoadMeasurementInterval = _QtechRrmDot11aLoadMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 6, 5),
    _QtechRrmDot11aLoadMeasurementInterval_Type()
)
qtechRrmDot11aLoadMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aLoadMeasurementInterval.setStatus("current")


class _QtechRrmDot11aNoiseMeasurementInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11aNoiseMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11aNoiseMeasurementInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11aNoiseMeasurementInterval_Object = MibScalar
qtechRrmDot11aNoiseMeasurementInterval = _QtechRrmDot11aNoiseMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 6, 6),
    _QtechRrmDot11aNoiseMeasurementInterval_Type()
)
qtechRrmDot11aNoiseMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aNoiseMeasurementInterval.setStatus("current")


class _QtechRrmDot11aSignalMeasurementInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11aSignalMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11aSignalMeasurementInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11aSignalMeasurementInterval_Object = MibScalar
qtechRrmDot11aSignalMeasurementInterval = _QtechRrmDot11aSignalMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 6, 7),
    _QtechRrmDot11aSignalMeasurementInterval_Type()
)
qtechRrmDot11aSignalMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aSignalMeasurementInterval.setStatus("current")


class _QtechRrmDot11aNeighborMessageInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11aNeighborMessageInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11aNeighborMessageInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11aNeighborMessageInterval_Object = MibScalar
qtechRrmDot11aNeighborMessageInterval = _QtechRrmDot11aNeighborMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 6, 8),
    _QtechRrmDot11aNeighborMessageInterval_Type()
)
qtechRrmDot11aNeighborMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aNeighborMessageInterval.setStatus("current")
_QtechRrmFactoryDot11a_ObjectIdentity = ObjectIdentity
qtechRrmFactoryDot11a = _QtechRrmFactoryDot11a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 7)
)


class _QtechRrmDot11aSetFactoryDefault_Type(Integer32):
    """Custom type qtechRrmDot11aSetFactoryDefault based on Integer32"""
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


_QtechRrmDot11aSetFactoryDefault_Type.__name__ = "Integer32"
_QtechRrmDot11aSetFactoryDefault_Object = MibScalar
qtechRrmDot11aSetFactoryDefault = _QtechRrmDot11aSetFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 2, 7, 1),
    _QtechRrmDot11aSetFactoryDefault_Type()
)
qtechRrmDot11aSetFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11aSetFactoryDefault.setStatus("current")
_QtechRrmObjectsDot11b_ObjectIdentity = ObjectIdentity
qtechRrmObjectsDot11b = _QtechRrmObjectsDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3)
)
_QtechRrmDCADot11b_ObjectIdentity = ObjectIdentity
qtechRrmDCADot11b = _QtechRrmDCADot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1)
)


class _QtechRrmDot11bDynamicChannelAssignment_Type(Integer32):
    """Custom type qtechRrmDot11bDynamicChannelAssignment based on Integer32"""
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


_QtechRrmDot11bDynamicChannelAssignment_Type.__name__ = "Integer32"
_QtechRrmDot11bDynamicChannelAssignment_Object = MibScalar
qtechRrmDot11bDynamicChannelAssignment = _QtechRrmDot11bDynamicChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 1),
    _QtechRrmDot11bDynamicChannelAssignment_Type()
)
qtechRrmDot11bDynamicChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bDynamicChannelAssignment.setStatus("current")


class _QtechRrmDot11bAnchorTime_Type(Unsigned32):
    """Custom type qtechRrmDot11bAnchorTime based on Unsigned32"""
    defaultValue = 0


_QtechRrmDot11bAnchorTime_Type.__name__ = "Unsigned32"
_QtechRrmDot11bAnchorTime_Object = MibScalar
qtechRrmDot11bAnchorTime = _QtechRrmDot11bAnchorTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 2),
    _QtechRrmDot11bAnchorTime_Type()
)
qtechRrmDot11bAnchorTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bAnchorTime.setStatus("current")


class _QtechRrmDot11bChannalWidth11n_Type(Unsigned32):
    """Custom type qtechRrmDot11bChannalWidth11n based on Unsigned32"""
    defaultValue = 20


_QtechRrmDot11bChannalWidth11n_Type.__name__ = "Unsigned32"
_QtechRrmDot11bChannalWidth11n_Object = MibScalar
qtechRrmDot11bChannalWidth11n = _QtechRrmDot11bChannalWidth11n_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 3),
    _QtechRrmDot11bChannalWidth11n_Type()
)
qtechRrmDot11bChannalWidth11n.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bChannalWidth11n.setStatus("current")


class _QtechRrmDot11bDynamicChannelUpdateInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11bDynamicChannelUpdateInterval based on Unsigned32"""
    defaultValue = 600


_QtechRrmDot11bDynamicChannelUpdateInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11bDynamicChannelUpdateInterval_Object = MibScalar
qtechRrmDot11bDynamicChannelUpdateInterval = _QtechRrmDot11bDynamicChannelUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 4),
    _QtechRrmDot11bDynamicChannelUpdateInterval_Type()
)
qtechRrmDot11bDynamicChannelUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bDynamicChannelUpdateInterval.setStatus("current")


class _QtechRrmDot11bDCASensitivity_Type(Integer32):
    """Custom type qtechRrmDot11bDCASensitivity based on Integer32"""
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


_QtechRrmDot11bDCASensitivity_Type.__name__ = "Integer32"
_QtechRrmDot11bDCASensitivity_Object = MibScalar
qtechRrmDot11bDCASensitivity = _QtechRrmDot11bDCASensitivity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 5),
    _QtechRrmDot11bDCASensitivity_Type()
)
qtechRrmDot11bDCASensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bDCASensitivity.setStatus("current")


class _QtechRrmDot11bForeignInterfereFactorEnable_Type(Integer32):
    """Custom type qtechRrmDot11bForeignInterfereFactorEnable based on Integer32"""
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


_QtechRrmDot11bForeignInterfereFactorEnable_Type.__name__ = "Integer32"
_QtechRrmDot11bForeignInterfereFactorEnable_Object = MibScalar
qtechRrmDot11bForeignInterfereFactorEnable = _QtechRrmDot11bForeignInterfereFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 6),
    _QtechRrmDot11bForeignInterfereFactorEnable_Type()
)
qtechRrmDot11bForeignInterfereFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bForeignInterfereFactorEnable.setStatus("current")


class _QtechRrmDot11bLoadFactorEnable_Type(Integer32):
    """Custom type qtechRrmDot11bLoadFactorEnable based on Integer32"""
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


_QtechRrmDot11bLoadFactorEnable_Type.__name__ = "Integer32"
_QtechRrmDot11bLoadFactorEnable_Object = MibScalar
qtechRrmDot11bLoadFactorEnable = _QtechRrmDot11bLoadFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 7),
    _QtechRrmDot11bLoadFactorEnable_Type()
)
qtechRrmDot11bLoadFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bLoadFactorEnable.setStatus("current")


class _QtechRrmDot11bNoiseFactorEnable_Type(Integer32):
    """Custom type qtechRrmDot11bNoiseFactorEnable based on Integer32"""
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


_QtechRrmDot11bNoiseFactorEnable_Type.__name__ = "Integer32"
_QtechRrmDot11bNoiseFactorEnable_Object = MibScalar
qtechRrmDot11bNoiseFactorEnable = _QtechRrmDot11bNoiseFactorEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 8),
    _QtechRrmDot11bNoiseFactorEnable_Type()
)
qtechRrmDot11bNoiseFactorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bNoiseFactorEnable.setStatus("current")


class _QtechRrmDot11bChannelUpdateCmdInvoke_Type(Integer32):
    """Custom type qtechRrmDot11bChannelUpdateCmdInvoke based on Integer32"""
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


_QtechRrmDot11bChannelUpdateCmdInvoke_Type.__name__ = "Integer32"
_QtechRrmDot11bChannelUpdateCmdInvoke_Object = MibScalar
qtechRrmDot11bChannelUpdateCmdInvoke = _QtechRrmDot11bChannelUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 9),
    _QtechRrmDot11bChannelUpdateCmdInvoke_Type()
)
qtechRrmDot11bChannelUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bChannelUpdateCmdInvoke.setStatus("current")
_QtechRrmDot11bDCAChannelTable_Object = MibTable
qtechRrmDot11bDCAChannelTable = _QtechRrmDot11bDCAChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    qtechRrmDot11bDCAChannelTable.setStatus("current")
_QtechRrmDot11bDCAChannelEntry_Object = MibTableRow
qtechRrmDot11bDCAChannelEntry = _QtechRrmDot11bDCAChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 10, 1)
)
qtechRrmDot11bDCAChannelEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmDot11bDCAChannelIndex"),
)
if mibBuilder.loadTexts:
    qtechRrmDot11bDCAChannelEntry.setStatus("current")
_QtechRrmDot11bDCAChannelIndex_Type = Integer32
_QtechRrmDot11bDCAChannelIndex_Object = MibTableColumn
qtechRrmDot11bDCAChannelIndex = _QtechRrmDot11bDCAChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 10, 1, 1),
    _QtechRrmDot11bDCAChannelIndex_Type()
)
qtechRrmDot11bDCAChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bDCAChannelIndex.setStatus("current")


class _QtechRrmDot11bDCAChannelOperation_Type(Integer32):
    """Custom type qtechRrmDot11bDCAChannelOperation based on Integer32"""
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


_QtechRrmDot11bDCAChannelOperation_Type.__name__ = "Integer32"
_QtechRrmDot11bDCAChannelOperation_Object = MibTableColumn
qtechRrmDot11bDCAChannelOperation = _QtechRrmDot11bDCAChannelOperation_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 1, 10, 1, 2),
    _QtechRrmDot11bDCAChannelOperation_Type()
)
qtechRrmDot11bDCAChannelOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bDCAChannelOperation.setStatus("current")
_QtechRrmTPCDot11b_ObjectIdentity = ObjectIdentity
qtechRrmTPCDot11b = _QtechRrmTPCDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 2)
)


class _QtechRrmDot11bDTPCSupport_Type(Integer32):
    """Custom type qtechRrmDot11bDTPCSupport based on Integer32"""
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


_QtechRrmDot11bDTPCSupport_Type.__name__ = "Integer32"
_QtechRrmDot11bDTPCSupport_Object = MibScalar
qtechRrmDot11bDTPCSupport = _QtechRrmDot11bDTPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 2, 1),
    _QtechRrmDot11bDTPCSupport_Type()
)
qtechRrmDot11bDTPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bDTPCSupport.setStatus("current")


class _QtechRrmDot11bDynamicTransmitPowerControl_Type(Integer32):
    """Custom type qtechRrmDot11bDynamicTransmitPowerControl based on Integer32"""
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


_QtechRrmDot11bDynamicTransmitPowerControl_Type.__name__ = "Integer32"
_QtechRrmDot11bDynamicTransmitPowerControl_Object = MibScalar
qtechRrmDot11bDynamicTransmitPowerControl = _QtechRrmDot11bDynamicTransmitPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 2, 2),
    _QtechRrmDot11bDynamicTransmitPowerControl_Type()
)
qtechRrmDot11bDynamicTransmitPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bDynamicTransmitPowerControl.setStatus("current")


class _QtechRrmDot11bDynamicTxPowerControlInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11bDynamicTxPowerControlInterval based on Unsigned32"""
    defaultValue = 600


_QtechRrmDot11bDynamicTxPowerControlInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11bDynamicTxPowerControlInterval_Object = MibScalar
qtechRrmDot11bDynamicTxPowerControlInterval = _QtechRrmDot11bDynamicTxPowerControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 2, 3),
    _QtechRrmDot11bDynamicTxPowerControlInterval_Type()
)
qtechRrmDot11bDynamicTxPowerControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bDynamicTxPowerControlInterval.setStatus("current")


class _QtechRrmDot11bCurrentTxPowerLevel_Type(Integer32):
    """Custom type qtechRrmDot11bCurrentTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QtechRrmDot11bCurrentTxPowerLevel_Type.__name__ = "Integer32"
_QtechRrmDot11bCurrentTxPowerLevel_Object = MibScalar
qtechRrmDot11bCurrentTxPowerLevel = _QtechRrmDot11bCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 2, 4),
    _QtechRrmDot11bCurrentTxPowerLevel_Type()
)
qtechRrmDot11bCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCurrentTxPowerLevel.setStatus("current")


class _QtechRrmDot11bPowerUpdateCmdInvoke_Type(Integer32):
    """Custom type qtechRrmDot11bPowerUpdateCmdInvoke based on Integer32"""
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


_QtechRrmDot11bPowerUpdateCmdInvoke_Type.__name__ = "Integer32"
_QtechRrmDot11bPowerUpdateCmdInvoke_Object = MibScalar
qtechRrmDot11bPowerUpdateCmdInvoke = _QtechRrmDot11bPowerUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 2, 5),
    _QtechRrmDot11bPowerUpdateCmdInvoke_Type()
)
qtechRrmDot11bPowerUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bPowerUpdateCmdInvoke.setStatus("current")


class _QtechRrmDot11bTXPowerThreshold_Type(Integer32):
    """Custom type qtechRrmDot11bTXPowerThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_QtechRrmDot11bTXPowerThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11bTXPowerThreshold_Object = MibScalar
qtechRrmDot11bTXPowerThreshold = _QtechRrmDot11bTXPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 2, 6),
    _QtechRrmDot11bTXPowerThreshold_Type()
)
qtechRrmDot11bTXPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bTXPowerThreshold.setStatus("current")


class _QtechRrmDot11bTPCNeighborNumber_Type(Integer32):
    """Custom type qtechRrmDot11bTPCNeighborNumber based on Integer32"""
    defaultValue = 3


_QtechRrmDot11bTPCNeighborNumber_Type.__name__ = "Integer32"
_QtechRrmDot11bTPCNeighborNumber_Object = MibScalar
qtechRrmDot11bTPCNeighborNumber = _QtechRrmDot11bTPCNeighborNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 2, 7),
    _QtechRrmDot11bTPCNeighborNumber_Type()
)
qtechRrmDot11bTPCNeighborNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bTPCNeighborNumber.setStatus("current")
_QtechRrmCHDDot11b_ObjectIdentity = ObjectIdentity
qtechRrmCHDDot11b = _QtechRrmCHDDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3)
)


class _QtechRrmDot11bCoverageEnable_Type(Integer32):
    """Custom type qtechRrmDot11bCoverageEnable based on Integer32"""
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


_QtechRrmDot11bCoverageEnable_Type.__name__ = "Integer32"
_QtechRrmDot11bCoverageEnable_Object = MibScalar
qtechRrmDot11bCoverageEnable = _QtechRrmDot11bCoverageEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3, 1),
    _QtechRrmDot11bCoverageEnable_Type()
)
qtechRrmDot11bCoverageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageEnable.setStatus("current")


class _QtechRrmDot11bCoverageExceptionGlobal_Type(Integer32):
    """Custom type qtechRrmDot11bCoverageExceptionGlobal based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11bCoverageExceptionGlobal_Type.__name__ = "Integer32"
_QtechRrmDot11bCoverageExceptionGlobal_Object = MibScalar
qtechRrmDot11bCoverageExceptionGlobal = _QtechRrmDot11bCoverageExceptionGlobal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3, 2),
    _QtechRrmDot11bCoverageExceptionGlobal_Type()
)
qtechRrmDot11bCoverageExceptionGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageExceptionGlobal.setStatus("current")


class _QtechRrmDot11bCoverageLevelGlobal_Type(Integer32):
    """Custom type qtechRrmDot11bCoverageLevelGlobal based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_QtechRrmDot11bCoverageLevelGlobal_Type.__name__ = "Integer32"
_QtechRrmDot11bCoverageLevelGlobal_Object = MibScalar
qtechRrmDot11bCoverageLevelGlobal = _QtechRrmDot11bCoverageLevelGlobal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3, 3),
    _QtechRrmDot11bCoverageLevelGlobal_Type()
)
qtechRrmDot11bCoverageLevelGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageLevelGlobal.setStatus("current")


class _QtechRrmDot11bCoverageDataRSSIThreshold_Type(Integer32):
    """Custom type qtechRrmDot11bCoverageDataRSSIThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_QtechRrmDot11bCoverageDataRSSIThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11bCoverageDataRSSIThreshold_Object = MibScalar
qtechRrmDot11bCoverageDataRSSIThreshold = _QtechRrmDot11bCoverageDataRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3, 4),
    _QtechRrmDot11bCoverageDataRSSIThreshold_Type()
)
qtechRrmDot11bCoverageDataRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageDataRSSIThreshold.setStatus("current")


class _QtechRrmDot11bCoverageVoiceRSSIThreshold_Type(Integer32):
    """Custom type qtechRrmDot11bCoverageVoiceRSSIThreshold based on Integer32"""
    defaultValue = -75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_QtechRrmDot11bCoverageVoiceRSSIThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11bCoverageVoiceRSSIThreshold_Object = MibScalar
qtechRrmDot11bCoverageVoiceRSSIThreshold = _QtechRrmDot11bCoverageVoiceRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3, 5),
    _QtechRrmDot11bCoverageVoiceRSSIThreshold_Type()
)
qtechRrmDot11bCoverageVoiceRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageVoiceRSSIThreshold.setStatus("current")


class _QtechRrmDot11bCoverageDataPacketCount_Type(Integer32):
    """Custom type qtechRrmDot11bCoverageDataPacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechRrmDot11bCoverageDataPacketCount_Type.__name__ = "Integer32"
_QtechRrmDot11bCoverageDataPacketCount_Object = MibScalar
qtechRrmDot11bCoverageDataPacketCount = _QtechRrmDot11bCoverageDataPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3, 6),
    _QtechRrmDot11bCoverageDataPacketCount_Type()
)
qtechRrmDot11bCoverageDataPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageDataPacketCount.setStatus("current")


class _QtechRrmDot11bCoverageVoicePacketCount_Type(Integer32):
    """Custom type qtechRrmDot11bCoverageVoicePacketCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechRrmDot11bCoverageVoicePacketCount_Type.__name__ = "Integer32"
_QtechRrmDot11bCoverageVoicePacketCount_Object = MibScalar
qtechRrmDot11bCoverageVoicePacketCount = _QtechRrmDot11bCoverageVoicePacketCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3, 7),
    _QtechRrmDot11bCoverageVoicePacketCount_Type()
)
qtechRrmDot11bCoverageVoicePacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageVoicePacketCount.setStatus("current")


class _QtechRrmDot11bCoverageDataFailRate_Type(Integer32):
    """Custom type qtechRrmDot11bCoverageDataFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11bCoverageDataFailRate_Type.__name__ = "Integer32"
_QtechRrmDot11bCoverageDataFailRate_Object = MibScalar
qtechRrmDot11bCoverageDataFailRate = _QtechRrmDot11bCoverageDataFailRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3, 8),
    _QtechRrmDot11bCoverageDataFailRate_Type()
)
qtechRrmDot11bCoverageDataFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageDataFailRate.setStatus("current")


class _QtechRrmDot11bCoverageVoiceFailRate_Type(Integer32):
    """Custom type qtechRrmDot11bCoverageVoiceFailRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11bCoverageVoiceFailRate_Type.__name__ = "Integer32"
_QtechRrmDot11bCoverageVoiceFailRate_Object = MibScalar
qtechRrmDot11bCoverageVoiceFailRate = _QtechRrmDot11bCoverageVoiceFailRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 3, 9),
    _QtechRrmDot11bCoverageVoiceFailRate_Type()
)
qtechRrmDot11bCoverageVoiceFailRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageVoiceFailRate.setStatus("current")
_QtechRrmGroupDot11b_ObjectIdentity = ObjectIdentity
qtechRrmGroupDot11b = _QtechRrmGroupDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4)
)


class _QtechRrmDot11bGlobalAutomaticGrouping_Type(Integer32):
    """Custom type qtechRrmDot11bGlobalAutomaticGrouping based on Integer32"""
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


_QtechRrmDot11bGlobalAutomaticGrouping_Type.__name__ = "Integer32"
_QtechRrmDot11bGlobalAutomaticGrouping_Object = MibScalar
qtechRrmDot11bGlobalAutomaticGrouping = _QtechRrmDot11bGlobalAutomaticGrouping_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 1),
    _QtechRrmDot11bGlobalAutomaticGrouping_Type()
)
qtechRrmDot11bGlobalAutomaticGrouping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bGlobalAutomaticGrouping.setStatus("current")
_QtechRrmDot11bGroupLeaderMacAddr_Type = MacAddress
_QtechRrmDot11bGroupLeaderMacAddr_Object = MibScalar
qtechRrmDot11bGroupLeaderMacAddr = _QtechRrmDot11bGroupLeaderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 2),
    _QtechRrmDot11bGroupLeaderMacAddr_Type()
)
qtechRrmDot11bGroupLeaderMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bGroupLeaderMacAddr.setStatus("current")


class _QtechRrmDot11bGroupLeader_Type(Integer32):
    """Custom type qtechRrmDot11bGroupLeader based on Integer32"""
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


_QtechRrmDot11bGroupLeader_Type.__name__ = "Integer32"
_QtechRrmDot11bGroupLeader_Object = MibScalar
qtechRrmDot11bGroupLeader = _QtechRrmDot11bGroupLeader_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 3),
    _QtechRrmDot11bGroupLeader_Type()
)
qtechRrmDot11bGroupLeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bGroupLeader.setStatus("current")
_QtechRrmDot11bGroupLastUpdateTime_Type = Unsigned32
_QtechRrmDot11bGroupLastUpdateTime_Object = MibScalar
qtechRrmDot11bGroupLastUpdateTime = _QtechRrmDot11bGroupLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 4),
    _QtechRrmDot11bGroupLastUpdateTime_Type()
)
qtechRrmDot11bGroupLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bGroupLastUpdateTime.setStatus("current")


class _QtechRrmDot11bGroupInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11bGroupInterval based on Unsigned32"""
    defaultValue = 3600


_QtechRrmDot11bGroupInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11bGroupInterval_Object = MibScalar
qtechRrmDot11bGroupInterval = _QtechRrmDot11bGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 5),
    _QtechRrmDot11bGroupInterval_Type()
)
qtechRrmDot11bGroupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bGroupInterval.setStatus("current")
_QtechRrmDot11bGroupTable_Object = MibTable
qtechRrmDot11bGroupTable = _QtechRrmDot11bGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 6)
)
if mibBuilder.loadTexts:
    qtechRrmDot11bGroupTable.setStatus("current")
_QtechRrmDot11bGroupEntry_Object = MibTableRow
qtechRrmDot11bGroupEntry = _QtechRrmDot11bGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 6, 1)
)
qtechRrmDot11bGroupEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmDot11bPeerMacAddress"),
)
if mibBuilder.loadTexts:
    qtechRrmDot11bGroupEntry.setStatus("current")
_QtechRrmDot11bPeerMacAddress_Type = MacAddress
_QtechRrmDot11bPeerMacAddress_Object = MibTableColumn
qtechRrmDot11bPeerMacAddress = _QtechRrmDot11bPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 6, 1, 1),
    _QtechRrmDot11bPeerMacAddress_Type()
)
qtechRrmDot11bPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bPeerMacAddress.setStatus("current")
_QtechRrmDot11bPeerIpAddress_Type = IpAddress
_QtechRrmDot11bPeerIpAddress_Object = MibTableColumn
qtechRrmDot11bPeerIpAddress = _QtechRrmDot11bPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 6, 1, 2),
    _QtechRrmDot11bPeerIpAddress_Type()
)
qtechRrmDot11bPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bPeerIpAddress.setStatus("current")
_QtechRrmDot11bSummaryTable_Object = MibTable
qtechRrmDot11bSummaryTable = _QtechRrmDot11bSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 7)
)
if mibBuilder.loadTexts:
    qtechRrmDot11bSummaryTable.setStatus("current")
_QtechRrmDot11bSummaryEntry_Object = MibTableRow
qtechRrmDot11bSummaryEntry = _QtechRrmDot11bSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1)
)
qtechRrmDot11bSummaryEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmDot11bSummaryMacAddress"),
    (0, "QTECH-RRM-MIB", "qtechRrmDot11bAPRadioID"),
)
if mibBuilder.loadTexts:
    qtechRrmDot11bSummaryEntry.setStatus("current")
_QtechRrmDot11bAPname_Type = DisplayString
_QtechRrmDot11bAPname_Object = MibTableColumn
qtechRrmDot11bAPname = _QtechRrmDot11bAPname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 1),
    _QtechRrmDot11bAPname_Type()
)
qtechRrmDot11bAPname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bAPname.setStatus("current")
_QtechRrmDot11bAPRadioID_Type = Unsigned32
_QtechRrmDot11bAPRadioID_Object = MibTableColumn
qtechRrmDot11bAPRadioID = _QtechRrmDot11bAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 2),
    _QtechRrmDot11bAPRadioID_Type()
)
qtechRrmDot11bAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bAPRadioID.setStatus("current")
_QtechRrmDot11bAPChannel_Type = Unsigned32
_QtechRrmDot11bAPChannel_Object = MibTableColumn
qtechRrmDot11bAPChannel = _QtechRrmDot11bAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 3),
    _QtechRrmDot11bAPChannel_Type()
)
qtechRrmDot11bAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bAPChannel.setStatus("current")
_QtechRrmDot11bAPTxPower_Type = Unsigned32
_QtechRrmDot11bAPTxPower_Object = MibTableColumn
qtechRrmDot11bAPTxPower = _QtechRrmDot11bAPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 4),
    _QtechRrmDot11bAPTxPower_Type()
)
qtechRrmDot11bAPTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bAPTxPower.setStatus("current")


class _QtechRrmDot11bAPChannelRrmChangeFlag_Type(Integer32):
    """Custom type qtechRrmDot11bAPChannelRrmChangeFlag based on Integer32"""
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


_QtechRrmDot11bAPChannelRrmChangeFlag_Type.__name__ = "Integer32"
_QtechRrmDot11bAPChannelRrmChangeFlag_Object = MibTableColumn
qtechRrmDot11bAPChannelRrmChangeFlag = _QtechRrmDot11bAPChannelRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 5),
    _QtechRrmDot11bAPChannelRrmChangeFlag_Type()
)
qtechRrmDot11bAPChannelRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bAPChannelRrmChangeFlag.setStatus("current")


class _QtechRrmDot11bAPTxPowerRrmChangeFlag_Type(Integer32):
    """Custom type qtechRrmDot11bAPTxPowerRrmChangeFlag based on Integer32"""
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


_QtechRrmDot11bAPTxPowerRrmChangeFlag_Type.__name__ = "Integer32"
_QtechRrmDot11bAPTxPowerRrmChangeFlag_Object = MibTableColumn
qtechRrmDot11bAPTxPowerRrmChangeFlag = _QtechRrmDot11bAPTxPowerRrmChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 6),
    _QtechRrmDot11bAPTxPowerRrmChangeFlag_Type()
)
qtechRrmDot11bAPTxPowerRrmChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bAPTxPowerRrmChangeFlag.setStatus("current")
_QtechRrmDot11bSummaryMacAddress_Type = MacAddress
_QtechRrmDot11bSummaryMacAddress_Object = MibTableColumn
qtechRrmDot11bSummaryMacAddress = _QtechRrmDot11bSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 4, 7, 1, 7),
    _QtechRrmDot11bSummaryMacAddress_Type()
)
qtechRrmDot11bSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmDot11bSummaryMacAddress.setStatus("current")
_QtechRrmProfileDot11b_ObjectIdentity = ObjectIdentity
qtechRrmProfileDot11b = _QtechRrmProfileDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 5)
)


class _QtechRrmDot11bForeignInterferenceThreshold_Type(Integer32):
    """Custom type qtechRrmDot11bForeignInterferenceThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11bForeignInterferenceThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11bForeignInterferenceThreshold_Object = MibScalar
qtechRrmDot11bForeignInterferenceThreshold = _QtechRrmDot11bForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 5, 1),
    _QtechRrmDot11bForeignInterferenceThreshold_Type()
)
qtechRrmDot11bForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bForeignInterferenceThreshold.setStatus("current")


class _QtechRrmDot11bForeignNoiseThreshold_Type(Integer32):
    """Custom type qtechRrmDot11bForeignNoiseThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_QtechRrmDot11bForeignNoiseThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11bForeignNoiseThreshold_Object = MibScalar
qtechRrmDot11bForeignNoiseThreshold = _QtechRrmDot11bForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 5, 2),
    _QtechRrmDot11bForeignNoiseThreshold_Type()
)
qtechRrmDot11bForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bForeignNoiseThreshold.setStatus("current")


class _QtechRrmDot11bRFUtilizationThreshold_Type(Integer32):
    """Custom type qtechRrmDot11bRFUtilizationThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmDot11bRFUtilizationThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11bRFUtilizationThreshold_Object = MibScalar
qtechRrmDot11bRFUtilizationThreshold = _QtechRrmDot11bRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 5, 3),
    _QtechRrmDot11bRFUtilizationThreshold_Type()
)
qtechRrmDot11bRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bRFUtilizationThreshold.setStatus("current")


class _QtechRrmDot11bThroughputThreshold_Type(Unsigned32):
    """Custom type qtechRrmDot11bThroughputThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000000),
    )


_QtechRrmDot11bThroughputThreshold_Type.__name__ = "Unsigned32"
_QtechRrmDot11bThroughputThreshold_Object = MibScalar
qtechRrmDot11bThroughputThreshold = _QtechRrmDot11bThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 5, 4),
    _QtechRrmDot11bThroughputThreshold_Type()
)
qtechRrmDot11bThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bThroughputThreshold.setStatus("current")


class _QtechRrmDot11bMobilesThreshold_Type(Integer32):
    """Custom type qtechRrmDot11bMobilesThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 75),
    )


_QtechRrmDot11bMobilesThreshold_Type.__name__ = "Integer32"
_QtechRrmDot11bMobilesThreshold_Object = MibScalar
qtechRrmDot11bMobilesThreshold = _QtechRrmDot11bMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 5, 5),
    _QtechRrmDot11bMobilesThreshold_Type()
)
qtechRrmDot11bMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bMobilesThreshold.setStatus("current")
_QtechRrmMonitorDot11b_ObjectIdentity = ObjectIdentity
qtechRrmMonitorDot11b = _QtechRrmMonitorDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 6)
)


class _QtechRrmDot11bMonitorEnable_Type(Integer32):
    """Custom type qtechRrmDot11bMonitorEnable based on Integer32"""
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


_QtechRrmDot11bMonitorEnable_Type.__name__ = "Integer32"
_QtechRrmDot11bMonitorEnable_Object = MibScalar
qtechRrmDot11bMonitorEnable = _QtechRrmDot11bMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 6, 1),
    _QtechRrmDot11bMonitorEnable_Type()
)
qtechRrmDot11bMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bMonitorEnable.setStatus("current")


class _QtechRrmDot11bChannelMonitorList_Type(Integer32):
    """Custom type qtechRrmDot11bChannelMonitorList based on Integer32"""
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


_QtechRrmDot11bChannelMonitorList_Type.__name__ = "Integer32"
_QtechRrmDot11bChannelMonitorList_Object = MibScalar
qtechRrmDot11bChannelMonitorList = _QtechRrmDot11bChannelMonitorList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 6, 2),
    _QtechRrmDot11bChannelMonitorList_Type()
)
qtechRrmDot11bChannelMonitorList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bChannelMonitorList.setStatus("current")


class _QtechRrmDot11bMonitorInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11bMonitorInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11bMonitorInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11bMonitorInterval_Object = MibScalar
qtechRrmDot11bMonitorInterval = _QtechRrmDot11bMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 6, 3),
    _QtechRrmDot11bMonitorInterval_Type()
)
qtechRrmDot11bMonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bMonitorInterval.setStatus("current")


class _QtechRrmDot11bCoverageMeasurementInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11bCoverageMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11bCoverageMeasurementInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11bCoverageMeasurementInterval_Object = MibScalar
qtechRrmDot11bCoverageMeasurementInterval = _QtechRrmDot11bCoverageMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 6, 4),
    _QtechRrmDot11bCoverageMeasurementInterval_Type()
)
qtechRrmDot11bCoverageMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bCoverageMeasurementInterval.setStatus("current")


class _QtechRrmDot11bLoadMeasurementInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11bLoadMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11bLoadMeasurementInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11bLoadMeasurementInterval_Object = MibScalar
qtechRrmDot11bLoadMeasurementInterval = _QtechRrmDot11bLoadMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 6, 5),
    _QtechRrmDot11bLoadMeasurementInterval_Type()
)
qtechRrmDot11bLoadMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bLoadMeasurementInterval.setStatus("current")


class _QtechRrmDot11bNoiseMeasurementInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11bNoiseMeasurementInterval based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11bNoiseMeasurementInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11bNoiseMeasurementInterval_Object = MibScalar
qtechRrmDot11bNoiseMeasurementInterval = _QtechRrmDot11bNoiseMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 6, 6),
    _QtechRrmDot11bNoiseMeasurementInterval_Type()
)
qtechRrmDot11bNoiseMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bNoiseMeasurementInterval.setStatus("current")


class _QtechRrmDot11bSignalMeasurementInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11bSignalMeasurementInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11bSignalMeasurementInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11bSignalMeasurementInterval_Object = MibScalar
qtechRrmDot11bSignalMeasurementInterval = _QtechRrmDot11bSignalMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 6, 7),
    _QtechRrmDot11bSignalMeasurementInterval_Type()
)
qtechRrmDot11bSignalMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bSignalMeasurementInterval.setStatus("current")


class _QtechRrmDot11bNeighborMessageInterval_Type(Unsigned32):
    """Custom type qtechRrmDot11bNeighborMessageInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechRrmDot11bNeighborMessageInterval_Type.__name__ = "Unsigned32"
_QtechRrmDot11bNeighborMessageInterval_Object = MibScalar
qtechRrmDot11bNeighborMessageInterval = _QtechRrmDot11bNeighborMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 6, 8),
    _QtechRrmDot11bNeighborMessageInterval_Type()
)
qtechRrmDot11bNeighborMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bNeighborMessageInterval.setStatus("current")
_QtechRrmFactoryDot11b_ObjectIdentity = ObjectIdentity
qtechRrmFactoryDot11b = _QtechRrmFactoryDot11b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 7)
)


class _QtechRrmDot11bSetFactoryDefault_Type(Integer32):
    """Custom type qtechRrmDot11bSetFactoryDefault based on Integer32"""
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


_QtechRrmDot11bSetFactoryDefault_Type.__name__ = "Integer32"
_QtechRrmDot11bSetFactoryDefault_Object = MibScalar
qtechRrmDot11bSetFactoryDefault = _QtechRrmDot11bSetFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 3, 7, 1),
    _QtechRrmDot11bSetFactoryDefault_Type()
)
qtechRrmDot11bSetFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmDot11bSetFactoryDefault.setStatus("current")
_QtechRrmObjectsAP_ObjectIdentity = ObjectIdentity
qtechRrmObjectsAP = _QtechRrmObjectsAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4)
)


class _QtechRrmAPIfSlotId_Type(Integer32):
    """Custom type qtechRrmAPIfSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfSlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfSlotId_Object = MibScalar
qtechRrmAPIfSlotId = _QtechRrmAPIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 1),
    _QtechRrmAPIfSlotId_Type()
)
qtechRrmAPIfSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfSlotId.setStatus("current")


class _QtechRrmAPName_Type(DisplayString):
    """Custom type qtechRrmAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPName_Type.__name__ = "DisplayString"
_QtechRrmAPName_Object = MibScalar
qtechRrmAPName = _QtechRrmAPName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 2),
    _QtechRrmAPName_Type()
)
qtechRrmAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPName.setStatus("current")
_QtechRrmAPIfProfileThresholdConfigTable_Object = MibTable
qtechRrmAPIfProfileThresholdConfigTable = _QtechRrmAPIfProfileThresholdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfProfileThresholdConfigTable.setStatus("current")
_QtechRrmAPIfProfileThresholdConfigEntry_Object = MibTableRow
qtechRrmAPIfProfileThresholdConfigEntry = _QtechRrmAPIfProfileThresholdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1)
)
qtechRrmAPIfProfileThresholdConfigEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfThresholdMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfThresholdRadioType"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfProfileThresholdConfigEntry.setStatus("current")


class _QtechRrmAPIfThresholdRadioType_Type(Integer32):
    """Custom type qtechRrmAPIfThresholdRadioType based on Integer32"""
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


_QtechRrmAPIfThresholdRadioType_Type.__name__ = "Integer32"
_QtechRrmAPIfThresholdRadioType_Object = MibTableColumn
qtechRrmAPIfThresholdRadioType = _QtechRrmAPIfThresholdRadioType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 1),
    _QtechRrmAPIfThresholdRadioType_Type()
)
qtechRrmAPIfThresholdRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThresholdRadioType.setStatus("current")


class _QtechRrmAPIfForeignInterferenceThreshold_Type(Integer32):
    """Custom type qtechRrmAPIfForeignInterferenceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmAPIfForeignInterferenceThreshold_Type.__name__ = "Integer32"
_QtechRrmAPIfForeignInterferenceThreshold_Object = MibTableColumn
qtechRrmAPIfForeignInterferenceThreshold = _QtechRrmAPIfForeignInterferenceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 2),
    _QtechRrmAPIfForeignInterferenceThreshold_Type()
)
qtechRrmAPIfForeignInterferenceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfForeignInterferenceThreshold.setStatus("current")


class _QtechRrmAPIfForeignNoiseThreshold_Type(Integer32):
    """Custom type qtechRrmAPIfForeignNoiseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 0),
    )


_QtechRrmAPIfForeignNoiseThreshold_Type.__name__ = "Integer32"
_QtechRrmAPIfForeignNoiseThreshold_Object = MibTableColumn
qtechRrmAPIfForeignNoiseThreshold = _QtechRrmAPIfForeignNoiseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 3),
    _QtechRrmAPIfForeignNoiseThreshold_Type()
)
qtechRrmAPIfForeignNoiseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfForeignNoiseThreshold.setStatus("current")


class _QtechRrmAPIfRFUtilizationThreshold_Type(Integer32):
    """Custom type qtechRrmAPIfRFUtilizationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechRrmAPIfRFUtilizationThreshold_Type.__name__ = "Integer32"
_QtechRrmAPIfRFUtilizationThreshold_Object = MibTableColumn
qtechRrmAPIfRFUtilizationThreshold = _QtechRrmAPIfRFUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 4),
    _QtechRrmAPIfRFUtilizationThreshold_Type()
)
qtechRrmAPIfRFUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfRFUtilizationThreshold.setStatus("current")


class _QtechRrmAPIfThroughputThreshold_Type(Unsigned32):
    """Custom type qtechRrmAPIfThroughputThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000000),
    )


_QtechRrmAPIfThroughputThreshold_Type.__name__ = "Unsigned32"
_QtechRrmAPIfThroughputThreshold_Object = MibTableColumn
qtechRrmAPIfThroughputThreshold = _QtechRrmAPIfThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 5),
    _QtechRrmAPIfThroughputThreshold_Type()
)
qtechRrmAPIfThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputThreshold.setStatus("current")


class _QtechRrmAPIfMobilesThreshold_Type(Integer32):
    """Custom type qtechRrmAPIfMobilesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_QtechRrmAPIfMobilesThreshold_Type.__name__ = "Integer32"
_QtechRrmAPIfMobilesThreshold_Object = MibTableColumn
qtechRrmAPIfMobilesThreshold = _QtechRrmAPIfMobilesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 6),
    _QtechRrmAPIfMobilesThreshold_Type()
)
qtechRrmAPIfMobilesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfMobilesThreshold.setStatus("current")


class _QtechRrmAPIfThresholdName_Type(DisplayString):
    """Custom type qtechRrmAPIfThresholdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPIfThresholdName_Type.__name__ = "DisplayString"
_QtechRrmAPIfThresholdName_Object = MibTableColumn
qtechRrmAPIfThresholdName = _QtechRrmAPIfThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 7),
    _QtechRrmAPIfThresholdName_Type()
)
qtechRrmAPIfThresholdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThresholdName.setStatus("current")
_QtechRrmAPIfThresholdMacAddr_Type = MacAddress
_QtechRrmAPIfThresholdMacAddr_Object = MibTableColumn
qtechRrmAPIfThresholdMacAddr = _QtechRrmAPIfThresholdMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 8),
    _QtechRrmAPIfThresholdMacAddr_Type()
)
qtechRrmAPIfThresholdMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThresholdMacAddr.setStatus("current")


class _QtechRrmAPIfForeignGlobalConfig_Type(Integer32):
    """Custom type qtechRrmAPIfForeignGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRrmAPIfForeignGlobalConfig_Type.__name__ = "Integer32"
_QtechRrmAPIfForeignGlobalConfig_Object = MibTableColumn
qtechRrmAPIfForeignGlobalConfig = _QtechRrmAPIfForeignGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 9),
    _QtechRrmAPIfForeignGlobalConfig_Type()
)
qtechRrmAPIfForeignGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfForeignGlobalConfig.setStatus("current")


class _QtechRrmAPIfNoiseGlobalConfig_Type(Integer32):
    """Custom type qtechRrmAPIfNoiseGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRrmAPIfNoiseGlobalConfig_Type.__name__ = "Integer32"
_QtechRrmAPIfNoiseGlobalConfig_Object = MibTableColumn
qtechRrmAPIfNoiseGlobalConfig = _QtechRrmAPIfNoiseGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 10),
    _QtechRrmAPIfNoiseGlobalConfig_Type()
)
qtechRrmAPIfNoiseGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfNoiseGlobalConfig.setStatus("current")


class _QtechRrmAPIfRFUtilizationGlobalConfig_Type(Integer32):
    """Custom type qtechRrmAPIfRFUtilizationGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRrmAPIfRFUtilizationGlobalConfig_Type.__name__ = "Integer32"
_QtechRrmAPIfRFUtilizationGlobalConfig_Object = MibTableColumn
qtechRrmAPIfRFUtilizationGlobalConfig = _QtechRrmAPIfRFUtilizationGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 11),
    _QtechRrmAPIfRFUtilizationGlobalConfig_Type()
)
qtechRrmAPIfRFUtilizationGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfRFUtilizationGlobalConfig.setStatus("current")


class _QtechRrmAPIfThroughputGlobalConfig_Type(Integer32):
    """Custom type qtechRrmAPIfThroughputGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRrmAPIfThroughputGlobalConfig_Type.__name__ = "Integer32"
_QtechRrmAPIfThroughputGlobalConfig_Object = MibTableColumn
qtechRrmAPIfThroughputGlobalConfig = _QtechRrmAPIfThroughputGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 12),
    _QtechRrmAPIfThroughputGlobalConfig_Type()
)
qtechRrmAPIfThroughputGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputGlobalConfig.setStatus("current")


class _QtechRrmAPIfMobilesGlobalConfig_Type(Integer32):
    """Custom type qtechRrmAPIfMobilesGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRrmAPIfMobilesGlobalConfig_Type.__name__ = "Integer32"
_QtechRrmAPIfMobilesGlobalConfig_Object = MibTableColumn
qtechRrmAPIfMobilesGlobalConfig = _QtechRrmAPIfMobilesGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 3, 1, 13),
    _QtechRrmAPIfMobilesGlobalConfig_Type()
)
qtechRrmAPIfMobilesGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPIfMobilesGlobalConfig.setStatus("current")
_QtechRrmAPIfLoadParametersTable_Object = MibTable
qtechRrmAPIfLoadParametersTable = _QtechRrmAPIfLoadParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadParametersTable.setStatus("current")
_QtechRrmAPIfLoadParametersEntry_Object = MibTableRow
qtechRrmAPIfLoadParametersEntry = _QtechRrmAPIfLoadParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1)
)
qtechRrmAPIfLoadParametersEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfLoadMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfLoadSlotId"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadParametersEntry.setStatus("current")


class _QtechRrmAPIfLoadRxUtilization_Type(Integer32):
    """Custom type qtechRrmAPIfLoadRxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechRrmAPIfLoadRxUtilization_Type.__name__ = "Integer32"
_QtechRrmAPIfLoadRxUtilization_Object = MibTableColumn
qtechRrmAPIfLoadRxUtilization = _QtechRrmAPIfLoadRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1, 1),
    _QtechRrmAPIfLoadRxUtilization_Type()
)
qtechRrmAPIfLoadRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadRxUtilization.setStatus("current")


class _QtechRrmAPIfLoadTxUtilization_Type(Integer32):
    """Custom type qtechRrmAPIfLoadTxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechRrmAPIfLoadTxUtilization_Type.__name__ = "Integer32"
_QtechRrmAPIfLoadTxUtilization_Object = MibTableColumn
qtechRrmAPIfLoadTxUtilization = _QtechRrmAPIfLoadTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1, 2),
    _QtechRrmAPIfLoadTxUtilization_Type()
)
qtechRrmAPIfLoadTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadTxUtilization.setStatus("current")


class _QtechRrmAPIfLoadChannelUtilization_Type(Integer32):
    """Custom type qtechRrmAPIfLoadChannelUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechRrmAPIfLoadChannelUtilization_Type.__name__ = "Integer32"
_QtechRrmAPIfLoadChannelUtilization_Object = MibTableColumn
qtechRrmAPIfLoadChannelUtilization = _QtechRrmAPIfLoadChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1, 3),
    _QtechRrmAPIfLoadChannelUtilization_Type()
)
qtechRrmAPIfLoadChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadChannelUtilization.setStatus("current")
_QtechRrmAPIfLoadNumOfClients_Type = Integer32
_QtechRrmAPIfLoadNumOfClients_Object = MibTableColumn
qtechRrmAPIfLoadNumOfClients = _QtechRrmAPIfLoadNumOfClients_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1, 4),
    _QtechRrmAPIfLoadNumOfClients_Type()
)
qtechRrmAPIfLoadNumOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadNumOfClients.setStatus("current")
_QtechRrmAPIfPoorSNRClients_Type = Integer32
_QtechRrmAPIfPoorSNRClients_Object = MibTableColumn
qtechRrmAPIfPoorSNRClients = _QtechRrmAPIfPoorSNRClients_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1, 5),
    _QtechRrmAPIfPoorSNRClients_Type()
)
qtechRrmAPIfPoorSNRClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfPoorSNRClients.setStatus("current")


class _QtechRrmAPIfLoadName_Type(DisplayString):
    """Custom type qtechRrmAPIfLoadName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPIfLoadName_Type.__name__ = "DisplayString"
_QtechRrmAPIfLoadName_Object = MibTableColumn
qtechRrmAPIfLoadName = _QtechRrmAPIfLoadName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1, 6),
    _QtechRrmAPIfLoadName_Type()
)
qtechRrmAPIfLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadName.setStatus("current")
_QtechRrmAPIfLoadMacAddr_Type = MacAddress
_QtechRrmAPIfLoadMacAddr_Object = MibTableColumn
qtechRrmAPIfLoadMacAddr = _QtechRrmAPIfLoadMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1, 7),
    _QtechRrmAPIfLoadMacAddr_Type()
)
qtechRrmAPIfLoadMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadMacAddr.setStatus("current")


class _QtechRrmAPIfLoadSlotId_Type(Integer32):
    """Custom type qtechRrmAPIfLoadSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfLoadSlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfLoadSlotId_Object = MibTableColumn
qtechRrmAPIfLoadSlotId = _QtechRrmAPIfLoadSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1, 8),
    _QtechRrmAPIfLoadSlotId_Type()
)
qtechRrmAPIfLoadSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadSlotId.setStatus("current")
_QtechRrmAPIfThroughput_Type = Integer32
_QtechRrmAPIfThroughput_Object = MibTableColumn
qtechRrmAPIfThroughput = _QtechRrmAPIfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 4, 1, 9),
    _QtechRrmAPIfThroughput_Type()
)
qtechRrmAPIfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughput.setStatus("current")
_QtechRrmAPIfChannelInterferenceInfoTable_Object = MibTable
qtechRrmAPIfChannelInterferenceInfoTable = _QtechRrmAPIfChannelInterferenceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 5)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfChannelInterferenceInfoTable.setStatus("current")
_QtechRrmAPIfChannelInterferenceInfoEntry_Object = MibTableRow
qtechRrmAPIfChannelInterferenceInfoEntry = _QtechRrmAPIfChannelInterferenceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 5, 1)
)
qtechRrmAPIfChannelInterferenceInfoEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfInterferenceMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfInterferenceSlotId"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfInterferenceChannelNo"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfChannelInterferenceInfoEntry.setStatus("current")
_QtechRrmAPIfInterferenceChannelNo_Type = Integer32
_QtechRrmAPIfInterferenceChannelNo_Object = MibTableColumn
qtechRrmAPIfInterferenceChannelNo = _QtechRrmAPIfInterferenceChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 5, 1, 1),
    _QtechRrmAPIfInterferenceChannelNo_Type()
)
qtechRrmAPIfInterferenceChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfInterferenceChannelNo.setStatus("current")
_QtechRrmAPIfInterferencePower_Type = Integer32
_QtechRrmAPIfInterferencePower_Object = MibTableColumn
qtechRrmAPIfInterferencePower = _QtechRrmAPIfInterferencePower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 5, 1, 2),
    _QtechRrmAPIfInterferencePower_Type()
)
qtechRrmAPIfInterferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfInterferencePower.setStatus("current")


class _QtechRrmAPIfInterferenceUtilization_Type(Integer32):
    """Custom type qtechRrmAPIfInterferenceUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechRrmAPIfInterferenceUtilization_Type.__name__ = "Integer32"
_QtechRrmAPIfInterferenceUtilization_Object = MibTableColumn
qtechRrmAPIfInterferenceUtilization = _QtechRrmAPIfInterferenceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 5, 1, 3),
    _QtechRrmAPIfInterferenceUtilization_Type()
)
qtechRrmAPIfInterferenceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfInterferenceUtilization.setStatus("current")


class _QtechRrmAPIfInterferenceName_Type(DisplayString):
    """Custom type qtechRrmAPIfInterferenceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPIfInterferenceName_Type.__name__ = "DisplayString"
_QtechRrmAPIfInterferenceName_Object = MibTableColumn
qtechRrmAPIfInterferenceName = _QtechRrmAPIfInterferenceName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 5, 1, 4),
    _QtechRrmAPIfInterferenceName_Type()
)
qtechRrmAPIfInterferenceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfInterferenceName.setStatus("current")
_QtechRrmAPIfInterferenceMacAddr_Type = MacAddress
_QtechRrmAPIfInterferenceMacAddr_Object = MibTableColumn
qtechRrmAPIfInterferenceMacAddr = _QtechRrmAPIfInterferenceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 5, 1, 5),
    _QtechRrmAPIfInterferenceMacAddr_Type()
)
qtechRrmAPIfInterferenceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfInterferenceMacAddr.setStatus("current")


class _QtechRrmAPIfInterferenceSlotId_Type(Integer32):
    """Custom type qtechRrmAPIfInterferenceSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfInterferenceSlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfInterferenceSlotId_Object = MibTableColumn
qtechRrmAPIfInterferenceSlotId = _QtechRrmAPIfInterferenceSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 5, 1, 6),
    _QtechRrmAPIfInterferenceSlotId_Type()
)
qtechRrmAPIfInterferenceSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfInterferenceSlotId.setStatus("current")
_QtechRrmAPIfChannelNoiseInfoTable_Object = MibTable
qtechRrmAPIfChannelNoiseInfoTable = _QtechRrmAPIfChannelNoiseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 6)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfChannelNoiseInfoTable.setStatus("current")
_QtechRrmAPIfChannelNoiseInfoEntry_Object = MibTableRow
qtechRrmAPIfChannelNoiseInfoEntry = _QtechRrmAPIfChannelNoiseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 6, 1)
)
qtechRrmAPIfChannelNoiseInfoEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfNoiseMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfNoiseSlotId"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfNoiseChannelNo"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfChannelNoiseInfoEntry.setStatus("current")
_QtechRrmAPIfNoiseChannelNo_Type = Integer32
_QtechRrmAPIfNoiseChannelNo_Object = MibTableColumn
qtechRrmAPIfNoiseChannelNo = _QtechRrmAPIfNoiseChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 6, 1, 1),
    _QtechRrmAPIfNoiseChannelNo_Type()
)
qtechRrmAPIfNoiseChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfNoiseChannelNo.setStatus("current")
_QtechRrmAPIfDBNoisePower_Type = Integer32
_QtechRrmAPIfDBNoisePower_Object = MibTableColumn
qtechRrmAPIfDBNoisePower = _QtechRrmAPIfDBNoisePower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 6, 1, 2),
    _QtechRrmAPIfDBNoisePower_Type()
)
qtechRrmAPIfDBNoisePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfDBNoisePower.setStatus("current")


class _QtechRrmAPIfNoiseName_Type(DisplayString):
    """Custom type qtechRrmAPIfNoiseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPIfNoiseName_Type.__name__ = "DisplayString"
_QtechRrmAPIfNoiseName_Object = MibTableColumn
qtechRrmAPIfNoiseName = _QtechRrmAPIfNoiseName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 6, 1, 3),
    _QtechRrmAPIfNoiseName_Type()
)
qtechRrmAPIfNoiseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfNoiseName.setStatus("current")
_QtechRrmAPIfNoiseMacAddr_Type = MacAddress
_QtechRrmAPIfNoiseMacAddr_Object = MibTableColumn
qtechRrmAPIfNoiseMacAddr = _QtechRrmAPIfNoiseMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 6, 1, 4),
    _QtechRrmAPIfNoiseMacAddr_Type()
)
qtechRrmAPIfNoiseMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfNoiseMacAddr.setStatus("current")


class _QtechRrmAPIfNoiseSlotId_Type(Integer32):
    """Custom type qtechRrmAPIfNoiseSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfNoiseSlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfNoiseSlotId_Object = MibTableColumn
qtechRrmAPIfNoiseSlotId = _QtechRrmAPIfNoiseSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 6, 1, 5),
    _QtechRrmAPIfNoiseSlotId_Type()
)
qtechRrmAPIfNoiseSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfNoiseSlotId.setStatus("current")
_QtechRrmAPIfProfileStateTable_Object = MibTable
qtechRrmAPIfProfileStateTable = _QtechRrmAPIfProfileStateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfProfileStateTable.setStatus("current")
_QtechRrmAPIfProfileStateEntry_Object = MibTableRow
qtechRrmAPIfProfileStateEntry = _QtechRrmAPIfProfileStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7, 1)
)
qtechRrmAPIfProfileStateEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfProfileMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfProfileSlotId"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfProfileStateEntry.setStatus("current")
_QtechRrmAPIfLoadProfileState_Type = ProfileState
_QtechRrmAPIfLoadProfileState_Object = MibTableColumn
qtechRrmAPIfLoadProfileState = _QtechRrmAPIfLoadProfileState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7, 1, 1),
    _QtechRrmAPIfLoadProfileState_Type()
)
qtechRrmAPIfLoadProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfLoadProfileState.setStatus("current")
_QtechRrmAPIfInterferenceProfileState_Type = ProfileState
_QtechRrmAPIfInterferenceProfileState_Object = MibTableColumn
qtechRrmAPIfInterferenceProfileState = _QtechRrmAPIfInterferenceProfileState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7, 1, 2),
    _QtechRrmAPIfInterferenceProfileState_Type()
)
qtechRrmAPIfInterferenceProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfInterferenceProfileState.setStatus("current")
_QtechRrmAPIfNoiseProfileState_Type = ProfileState
_QtechRrmAPIfNoiseProfileState_Object = MibTableColumn
qtechRrmAPIfNoiseProfileState = _QtechRrmAPIfNoiseProfileState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7, 1, 3),
    _QtechRrmAPIfNoiseProfileState_Type()
)
qtechRrmAPIfNoiseProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfNoiseProfileState.setStatus("current")
_QtechRrmAPIfCoverageProfileState_Type = ProfileState
_QtechRrmAPIfCoverageProfileState_Object = MibTableColumn
qtechRrmAPIfCoverageProfileState = _QtechRrmAPIfCoverageProfileState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7, 1, 4),
    _QtechRrmAPIfCoverageProfileState_Type()
)
qtechRrmAPIfCoverageProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfCoverageProfileState.setStatus("current")
_QtechRrmAPIfPerformanceProfileState_Type = ProfileState
_QtechRrmAPIfPerformanceProfileState_Object = MibTableColumn
qtechRrmAPIfPerformanceProfileState = _QtechRrmAPIfPerformanceProfileState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7, 1, 5),
    _QtechRrmAPIfPerformanceProfileState_Type()
)
qtechRrmAPIfPerformanceProfileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfPerformanceProfileState.setStatus("current")


class _QtechRrmAPIfProfileName_Type(DisplayString):
    """Custom type qtechRrmAPIfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPIfProfileName_Type.__name__ = "DisplayString"
_QtechRrmAPIfProfileName_Object = MibTableColumn
qtechRrmAPIfProfileName = _QtechRrmAPIfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7, 1, 6),
    _QtechRrmAPIfProfileName_Type()
)
qtechRrmAPIfProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfProfileName.setStatus("current")
_QtechRrmAPIfProfileMacAddr_Type = MacAddress
_QtechRrmAPIfProfileMacAddr_Object = MibTableColumn
qtechRrmAPIfProfileMacAddr = _QtechRrmAPIfProfileMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7, 1, 7),
    _QtechRrmAPIfProfileMacAddr_Type()
)
qtechRrmAPIfProfileMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfProfileMacAddr.setStatus("current")


class _QtechRrmAPIfProfileSlotId_Type(Integer32):
    """Custom type qtechRrmAPIfProfileSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfProfileSlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfProfileSlotId_Object = MibTableColumn
qtechRrmAPIfProfileSlotId = _QtechRrmAPIfProfileSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 7, 1, 8),
    _QtechRrmAPIfProfileSlotId_Type()
)
qtechRrmAPIfProfileSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfProfileSlotId.setStatus("current")
_QtechRrmAPIfRxNeighborsTable_Object = MibTable
qtechRrmAPIfRxNeighborsTable = _QtechRrmAPIfRxNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborsTable.setStatus("current")
_QtechRrmAPIfRxNeighborsEntry_Object = MibTableRow
qtechRrmAPIfRxNeighborsEntry = _QtechRrmAPIfRxNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1)
)
qtechRrmAPIfRxNeighborsEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborSlotId"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborMacAddress"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborSlot"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborsEntry.setStatus("current")
_QtechRrmAPIfRxNeighborMacAddress_Type = MacAddress
_QtechRrmAPIfRxNeighborMacAddress_Object = MibTableColumn
qtechRrmAPIfRxNeighborMacAddress = _QtechRrmAPIfRxNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 1),
    _QtechRrmAPIfRxNeighborMacAddress_Type()
)
qtechRrmAPIfRxNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborMacAddress.setStatus("current")
_QtechRrmAPIfRxNeighborSlot_Type = Integer32
_QtechRrmAPIfRxNeighborSlot_Object = MibTableColumn
qtechRrmAPIfRxNeighborSlot = _QtechRrmAPIfRxNeighborSlot_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 2),
    _QtechRrmAPIfRxNeighborSlot_Type()
)
qtechRrmAPIfRxNeighborSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborSlot.setStatus("current")
_QtechRrmAPIfRxNeighborIpAddress_Type = IpAddress
_QtechRrmAPIfRxNeighborIpAddress_Object = MibTableColumn
qtechRrmAPIfRxNeighborIpAddress = _QtechRrmAPIfRxNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 3),
    _QtechRrmAPIfRxNeighborIpAddress_Type()
)
qtechRrmAPIfRxNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborIpAddress.setStatus("current")
_QtechRrmAPIfRxNeighborRSSI_Type = Integer32
_QtechRrmAPIfRxNeighborRSSI_Object = MibTableColumn
qtechRrmAPIfRxNeighborRSSI = _QtechRrmAPIfRxNeighborRSSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 4),
    _QtechRrmAPIfRxNeighborRSSI_Type()
)
qtechRrmAPIfRxNeighborRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborRSSI.setStatus("current")
_QtechRrmAPIfRxNeighborSNR_Type = Integer32
_QtechRrmAPIfRxNeighborSNR_Object = MibTableColumn
qtechRrmAPIfRxNeighborSNR = _QtechRrmAPIfRxNeighborSNR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 5),
    _QtechRrmAPIfRxNeighborSNR_Type()
)
qtechRrmAPIfRxNeighborSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborSNR.setStatus("current")
_QtechRrmAPIfRxNeighborChannel_Type = Integer32
_QtechRrmAPIfRxNeighborChannel_Object = MibTableColumn
qtechRrmAPIfRxNeighborChannel = _QtechRrmAPIfRxNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 6),
    _QtechRrmAPIfRxNeighborChannel_Type()
)
qtechRrmAPIfRxNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborChannel.setStatus("current")


class _QtechRrmAPIfRxNeighborChannelWidth_Type(Integer32):
    """Custom type qtechRrmAPIfRxNeighborChannelWidth based on Integer32"""
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


_QtechRrmAPIfRxNeighborChannelWidth_Type.__name__ = "Integer32"
_QtechRrmAPIfRxNeighborChannelWidth_Object = MibTableColumn
qtechRrmAPIfRxNeighborChannelWidth = _QtechRrmAPIfRxNeighborChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 7),
    _QtechRrmAPIfRxNeighborChannelWidth_Type()
)
qtechRrmAPIfRxNeighborChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborChannelWidth.setStatus("current")


class _QtechRrmAPIfRxNeighborName_Type(DisplayString):
    """Custom type qtechRrmAPIfRxNeighborName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPIfRxNeighborName_Type.__name__ = "DisplayString"
_QtechRrmAPIfRxNeighborName_Object = MibTableColumn
qtechRrmAPIfRxNeighborName = _QtechRrmAPIfRxNeighborName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 8),
    _QtechRrmAPIfRxNeighborName_Type()
)
qtechRrmAPIfRxNeighborName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborName.setStatus("current")
_QtechRrmAPIfRxNeighborMacAddr_Type = MacAddress
_QtechRrmAPIfRxNeighborMacAddr_Object = MibTableColumn
qtechRrmAPIfRxNeighborMacAddr = _QtechRrmAPIfRxNeighborMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 9),
    _QtechRrmAPIfRxNeighborMacAddr_Type()
)
qtechRrmAPIfRxNeighborMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborMacAddr.setStatus("current")


class _QtechRrmAPIfRxNeighborSlotId_Type(Integer32):
    """Custom type qtechRrmAPIfRxNeighborSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfRxNeighborSlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfRxNeighborSlotId_Object = MibTableColumn
qtechRrmAPIfRxNeighborSlotId = _QtechRrmAPIfRxNeighborSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 8, 1, 10),
    _QtechRrmAPIfRxNeighborSlotId_Type()
)
qtechRrmAPIfRxNeighborSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRxNeighborSlotId.setStatus("current")
_QtechRrmAPIfStationRSSICoverageInfoTable_Object = MibTable
qtechRrmAPIfStationRSSICoverageInfoTable = _QtechRrmAPIfStationRSSICoverageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 9)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfStationRSSICoverageInfoTable.setStatus("current")
_QtechRrmAPIfStationRSSICoverageInfoEntry_Object = MibTableRow
qtechRrmAPIfStationRSSICoverageInfoEntry = _QtechRrmAPIfStationRSSICoverageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 9, 1)
)
qtechRrmAPIfStationRSSICoverageInfoEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfStationRSSIMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfStationRSSISlotId"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfStationRSSICoverageIndex"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfStationRSSICoverageInfoEntry.setStatus("current")
_QtechRrmAPIfStationRSSICoverageIndex_Type = Integer32
_QtechRrmAPIfStationRSSICoverageIndex_Object = MibTableColumn
qtechRrmAPIfStationRSSICoverageIndex = _QtechRrmAPIfStationRSSICoverageIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 9, 1, 1),
    _QtechRrmAPIfStationRSSICoverageIndex_Type()
)
qtechRrmAPIfStationRSSICoverageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationRSSICoverageIndex.setStatus("current")
_QtechRrmAPIfRSSILevel_Type = Integer32
_QtechRrmAPIfRSSILevel_Object = MibTableColumn
qtechRrmAPIfRSSILevel = _QtechRrmAPIfRSSILevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 9, 1, 2),
    _QtechRrmAPIfRSSILevel_Type()
)
qtechRrmAPIfRSSILevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRSSILevel.setStatus("current")
_QtechRrmAPIfStationCountOnRSSI_Type = Integer32
_QtechRrmAPIfStationCountOnRSSI_Object = MibTableColumn
qtechRrmAPIfStationCountOnRSSI = _QtechRrmAPIfStationCountOnRSSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 9, 1, 3),
    _QtechRrmAPIfStationCountOnRSSI_Type()
)
qtechRrmAPIfStationCountOnRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationCountOnRSSI.setStatus("current")


class _QtechRrmAPIfStationRSSIName_Type(DisplayString):
    """Custom type qtechRrmAPIfStationRSSIName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPIfStationRSSIName_Type.__name__ = "DisplayString"
_QtechRrmAPIfStationRSSIName_Object = MibTableColumn
qtechRrmAPIfStationRSSIName = _QtechRrmAPIfStationRSSIName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 9, 1, 4),
    _QtechRrmAPIfStationRSSIName_Type()
)
qtechRrmAPIfStationRSSIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationRSSIName.setStatus("current")
_QtechRrmAPIfStationRSSIMacAddr_Type = MacAddress
_QtechRrmAPIfStationRSSIMacAddr_Object = MibTableColumn
qtechRrmAPIfStationRSSIMacAddr = _QtechRrmAPIfStationRSSIMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 9, 1, 5),
    _QtechRrmAPIfStationRSSIMacAddr_Type()
)
qtechRrmAPIfStationRSSIMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationRSSIMacAddr.setStatus("current")


class _QtechRrmAPIfStationRSSISlotId_Type(Integer32):
    """Custom type qtechRrmAPIfStationRSSISlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfStationRSSISlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfStationRSSISlotId_Object = MibTableColumn
qtechRrmAPIfStationRSSISlotId = _QtechRrmAPIfStationRSSISlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 9, 1, 6),
    _QtechRrmAPIfStationRSSISlotId_Type()
)
qtechRrmAPIfStationRSSISlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationRSSISlotId.setStatus("current")
_QtechRrmAPIfStationSNRCoverageInfoTable_Object = MibTable
qtechRrmAPIfStationSNRCoverageInfoTable = _QtechRrmAPIfStationSNRCoverageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 10)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfStationSNRCoverageInfoTable.setStatus("current")
_QtechRrmAPIfStationSNRCoverageInfoEntry_Object = MibTableRow
qtechRrmAPIfStationSNRCoverageInfoEntry = _QtechRrmAPIfStationSNRCoverageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 10, 1)
)
qtechRrmAPIfStationSNRCoverageInfoEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfStationSNRMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfStationSNRSlotId"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfStationSNRCoverageIndex"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfStationSNRCoverageInfoEntry.setStatus("current")
_QtechRrmAPIfStationSNRCoverageIndex_Type = Integer32
_QtechRrmAPIfStationSNRCoverageIndex_Object = MibTableColumn
qtechRrmAPIfStationSNRCoverageIndex = _QtechRrmAPIfStationSNRCoverageIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 10, 1, 1),
    _QtechRrmAPIfStationSNRCoverageIndex_Type()
)
qtechRrmAPIfStationSNRCoverageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationSNRCoverageIndex.setStatus("current")
_QtechRrmAPIfSNRLevel_Type = Integer32
_QtechRrmAPIfSNRLevel_Object = MibTableColumn
qtechRrmAPIfSNRLevel = _QtechRrmAPIfSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 10, 1, 2),
    _QtechRrmAPIfSNRLevel_Type()
)
qtechRrmAPIfSNRLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfSNRLevel.setStatus("current")
_QtechRrmAPIfStationCountOnSNR_Type = Integer32
_QtechRrmAPIfStationCountOnSNR_Object = MibTableColumn
qtechRrmAPIfStationCountOnSNR = _QtechRrmAPIfStationCountOnSNR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 10, 1, 3),
    _QtechRrmAPIfStationCountOnSNR_Type()
)
qtechRrmAPIfStationCountOnSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationCountOnSNR.setStatus("current")


class _QtechRrmAPIfStationSNRName_Type(DisplayString):
    """Custom type qtechRrmAPIfStationSNRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPIfStationSNRName_Type.__name__ = "DisplayString"
_QtechRrmAPIfStationSNRName_Object = MibTableColumn
qtechRrmAPIfStationSNRName = _QtechRrmAPIfStationSNRName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 10, 1, 4),
    _QtechRrmAPIfStationSNRName_Type()
)
qtechRrmAPIfStationSNRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationSNRName.setStatus("current")
_QtechRrmAPIfStationSNRMacAddr_Type = MacAddress
_QtechRrmAPIfStationSNRMacAddr_Object = MibTableColumn
qtechRrmAPIfStationSNRMacAddr = _QtechRrmAPIfStationSNRMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 10, 1, 5),
    _QtechRrmAPIfStationSNRMacAddr_Type()
)
qtechRrmAPIfStationSNRMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationSNRMacAddr.setStatus("current")


class _QtechRrmAPIfStationSNRSlotId_Type(Integer32):
    """Custom type qtechRrmAPIfStationSNRSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfStationSNRSlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfStationSNRSlotId_Object = MibTableColumn
qtechRrmAPIfStationSNRSlotId = _QtechRrmAPIfStationSNRSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 10, 1, 6),
    _QtechRrmAPIfStationSNRSlotId_Type()
)
qtechRrmAPIfStationSNRSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfStationSNRSlotId.setStatus("current")
_QtechRrmAPIfRecommendedRFParametersTable_Object = MibTable
qtechRrmAPIfRecommendedRFParametersTable = _QtechRrmAPIfRecommendedRFParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 11)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfRecommendedRFParametersTable.setStatus("current")
_QtechRrmAPIfRecommendedRFParametersEntry_Object = MibTableRow
qtechRrmAPIfRecommendedRFParametersEntry = _QtechRrmAPIfRecommendedRFParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 11, 1)
)
qtechRrmAPIfRecommendedRFParametersEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfRecommendedMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfRecommendedSlotId"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfRecommendedRFParametersEntry.setStatus("current")
_QtechRrmAPIfRecommendedChannelNumber_Type = Integer32
_QtechRrmAPIfRecommendedChannelNumber_Object = MibTableColumn
qtechRrmAPIfRecommendedChannelNumber = _QtechRrmAPIfRecommendedChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 11, 1, 1),
    _QtechRrmAPIfRecommendedChannelNumber_Type()
)
qtechRrmAPIfRecommendedChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRecommendedChannelNumber.setStatus("current")
_QtechRrmAPIfRecommendedTxPowerLevel_Type = Integer32
_QtechRrmAPIfRecommendedTxPowerLevel_Object = MibTableColumn
qtechRrmAPIfRecommendedTxPowerLevel = _QtechRrmAPIfRecommendedTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 11, 1, 2),
    _QtechRrmAPIfRecommendedTxPowerLevel_Type()
)
qtechRrmAPIfRecommendedTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRecommendedTxPowerLevel.setStatus("current")
_QtechRrmAPIfRecommendedRTSThreshold_Type = Integer32
_QtechRrmAPIfRecommendedRTSThreshold_Object = MibTableColumn
qtechRrmAPIfRecommendedRTSThreshold = _QtechRrmAPIfRecommendedRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 11, 1, 3),
    _QtechRrmAPIfRecommendedRTSThreshold_Type()
)
qtechRrmAPIfRecommendedRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRecommendedRTSThreshold.setStatus("current")
_QtechRrmAPIfRecommendedFragmentationThreshold_Type = Integer32
_QtechRrmAPIfRecommendedFragmentationThreshold_Object = MibTableColumn
qtechRrmAPIfRecommendedFragmentationThreshold = _QtechRrmAPIfRecommendedFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 11, 1, 4),
    _QtechRrmAPIfRecommendedFragmentationThreshold_Type()
)
qtechRrmAPIfRecommendedFragmentationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRecommendedFragmentationThreshold.setStatus("current")


class _QtechRrmAPIfRecommendedName_Type(DisplayString):
    """Custom type qtechRrmAPIfRecommendedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPIfRecommendedName_Type.__name__ = "DisplayString"
_QtechRrmAPIfRecommendedName_Object = MibTableColumn
qtechRrmAPIfRecommendedName = _QtechRrmAPIfRecommendedName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 11, 1, 5),
    _QtechRrmAPIfRecommendedName_Type()
)
qtechRrmAPIfRecommendedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRecommendedName.setStatus("current")
_QtechRrmAPIfRecommendedMacAddr_Type = MacAddress
_QtechRrmAPIfRecommendedMacAddr_Object = MibTableColumn
qtechRrmAPIfRecommendedMacAddr = _QtechRrmAPIfRecommendedMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 11, 1, 6),
    _QtechRrmAPIfRecommendedMacAddr_Type()
)
qtechRrmAPIfRecommendedMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRecommendedMacAddr.setStatus("current")


class _QtechRrmAPIfRecommendedSlotId_Type(Integer32):
    """Custom type qtechRrmAPIfRecommendedSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfRecommendedSlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfRecommendedSlotId_Object = MibTableColumn
qtechRrmAPIfRecommendedSlotId = _QtechRrmAPIfRecommendedSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 11, 1, 7),
    _QtechRrmAPIfRecommendedSlotId_Type()
)
qtechRrmAPIfRecommendedSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfRecommendedSlotId.setStatus("current")
_QtechRrmAPRadioTable_Object = MibTable
qtechRrmAPRadioTable = _QtechRrmAPRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 12)
)
if mibBuilder.loadTexts:
    qtechRrmAPRadioTable.setStatus("current")
_QtechRrmAPRadioEntry_Object = MibTableRow
qtechRrmAPRadioEntry = _QtechRrmAPRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 12, 1)
)
qtechRrmAPRadioEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPRadioID"),
)
if mibBuilder.loadTexts:
    qtechRrmAPRadioEntry.setStatus("current")


class _QtechRrmAPRadioID_Type(Integer32):
    """Custom type qtechRrmAPRadioID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPRadioID_Type.__name__ = "Integer32"
_QtechRrmAPRadioID_Object = MibTableColumn
qtechRrmAPRadioID = _QtechRrmAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 12, 1, 1),
    _QtechRrmAPRadioID_Type()
)
qtechRrmAPRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPRadioID.setStatus("current")


class _QtechRrmAPRadioType_Type(Integer32):
    """Custom type qtechRrmAPRadioType based on Integer32"""
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


_QtechRrmAPRadioType_Type.__name__ = "Integer32"
_QtechRrmAPRadioType_Object = MibTableColumn
qtechRrmAPRadioType = _QtechRrmAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 12, 1, 2),
    _QtechRrmAPRadioType_Type()
)
qtechRrmAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPRadioType.setStatus("current")


class _QtechRrmAPRealName_Type(DisplayString):
    """Custom type qtechRrmAPRealName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRrmAPRealName_Type.__name__ = "DisplayString"
_QtechRrmAPRealName_Object = MibTableColumn
qtechRrmAPRealName = _QtechRrmAPRealName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 12, 1, 3),
    _QtechRrmAPRealName_Type()
)
qtechRrmAPRealName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPRealName.setStatus("current")
_QtechRrmAPMacAddr_Type = MacAddress
_QtechRrmAPMacAddr_Object = MibTableColumn
qtechRrmAPMacAddr = _QtechRrmAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 12, 1, 4),
    _QtechRrmAPMacAddr_Type()
)
qtechRrmAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPMacAddr.setStatus("current")
_QtechRrmAPIfThroughputParametersTable_Object = MibTable
qtechRrmAPIfThroughputParametersTable = _QtechRrmAPIfThroughputParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 13)
)
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputParametersTable.setStatus("current")
_QtechRrmAPIfThroughputParametersEntry_Object = MibTableRow
qtechRrmAPIfThroughputParametersEntry = _QtechRrmAPIfThroughputParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 13, 1)
)
qtechRrmAPIfThroughputParametersEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfThroughputMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPIfThroughputSlotId"),
)
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputParametersEntry.setStatus("current")
_QtechRrmAPIfThroughputMacAddr_Type = MacAddress
_QtechRrmAPIfThroughputMacAddr_Object = MibTableColumn
qtechRrmAPIfThroughputMacAddr = _QtechRrmAPIfThroughputMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 13, 1, 1),
    _QtechRrmAPIfThroughputMacAddr_Type()
)
qtechRrmAPIfThroughputMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputMacAddr.setStatus("current")


class _QtechRrmAPIfThroughputSlotId_Type(Integer32):
    """Custom type qtechRrmAPIfThroughputSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPIfThroughputSlotId_Type.__name__ = "Integer32"
_QtechRrmAPIfThroughputSlotId_Object = MibTableColumn
qtechRrmAPIfThroughputSlotId = _QtechRrmAPIfThroughputSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 13, 1, 2),
    _QtechRrmAPIfThroughputSlotId_Type()
)
qtechRrmAPIfThroughputSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputSlotId.setStatus("current")


class _QtechRrmAPIfThroughputAPName_Type(DisplayString):
    """Custom type qtechRrmAPIfThroughputAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechRrmAPIfThroughputAPName_Type.__name__ = "DisplayString"
_QtechRrmAPIfThroughputAPName_Object = MibTableColumn
qtechRrmAPIfThroughputAPName = _QtechRrmAPIfThroughputAPName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 13, 1, 3),
    _QtechRrmAPIfThroughputAPName_Type()
)
qtechRrmAPIfThroughputAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputAPName.setStatus("current")
_QtechRrmAPIfThroughputRx_Type = Integer32
_QtechRrmAPIfThroughputRx_Object = MibTableColumn
qtechRrmAPIfThroughputRx = _QtechRrmAPIfThroughputRx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 13, 1, 4),
    _QtechRrmAPIfThroughputRx_Type()
)
qtechRrmAPIfThroughputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputRx.setStatus("current")
_QtechRrmAPIfThroughputTx_Type = Integer32
_QtechRrmAPIfThroughputTx_Object = MibTableColumn
qtechRrmAPIfThroughputTx = _QtechRrmAPIfThroughputTx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 13, 1, 5),
    _QtechRrmAPIfThroughputTx_Type()
)
qtechRrmAPIfThroughputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputTx.setStatus("current")
_QtechRrmAPIfThroughputTotal_Type = Integer32
_QtechRrmAPIfThroughputTotal_Object = MibTableColumn
qtechRrmAPIfThroughputTotal = _QtechRrmAPIfThroughputTotal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 13, 1, 6),
    _QtechRrmAPIfThroughputTotal_Type()
)
qtechRrmAPIfThroughputTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPIfThroughputTotal.setStatus("current")
_QtechRrmAPSnrBSSIDTable_Object = MibTable
qtechRrmAPSnrBSSIDTable = _QtechRrmAPSnrBSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14)
)
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDTable.setStatus("current")
_QtechRrmAPSnrBSSIDEntry_Object = MibTableRow
qtechRrmAPSnrBSSIDEntry = _QtechRrmAPSnrBSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14, 1)
)
qtechRrmAPSnrBSSIDEntry.setIndexNames(
    (0, "QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDMacAddr"),
    (0, "QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDSlotId"),
)
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDEntry.setStatus("current")
_QtechRrmAPSnrBSSIDMacAddr_Type = MacAddress
_QtechRrmAPSnrBSSIDMacAddr_Object = MibTableColumn
qtechRrmAPSnrBSSIDMacAddr = _QtechRrmAPSnrBSSIDMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14, 1, 1),
    _QtechRrmAPSnrBSSIDMacAddr_Type()
)
qtechRrmAPSnrBSSIDMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDMacAddr.setStatus("current")


class _QtechRrmAPSnrBSSIDSlotId_Type(Integer32):
    """Custom type qtechRrmAPSnrBSSIDSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_QtechRrmAPSnrBSSIDSlotId_Type.__name__ = "Integer32"
_QtechRrmAPSnrBSSIDSlotId_Object = MibTableColumn
qtechRrmAPSnrBSSIDSlotId = _QtechRrmAPSnrBSSIDSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14, 1, 2),
    _QtechRrmAPSnrBSSIDSlotId_Type()
)
qtechRrmAPSnrBSSIDSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDSlotId.setStatus("current")


class _QtechRrmAPSnrBSSIDAPName_Type(DisplayString):
    """Custom type qtechRrmAPSnrBSSIDAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechRrmAPSnrBSSIDAPName_Type.__name__ = "DisplayString"
_QtechRrmAPSnrBSSIDAPName_Object = MibTableColumn
qtechRrmAPSnrBSSIDAPName = _QtechRrmAPSnrBSSIDAPName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14, 1, 3),
    _QtechRrmAPSnrBSSIDAPName_Type()
)
qtechRrmAPSnrBSSIDAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDAPName.setStatus("current")
_QtechRrmAPSnrBSSIDAverageSignalStrength_Type = Integer32
_QtechRrmAPSnrBSSIDAverageSignalStrength_Object = MibTableColumn
qtechRrmAPSnrBSSIDAverageSignalStrength = _QtechRrmAPSnrBSSIDAverageSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14, 1, 4),
    _QtechRrmAPSnrBSSIDAverageSignalStrength_Type()
)
qtechRrmAPSnrBSSIDAverageSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDAverageSignalStrength.setStatus("current")
_QtechRrmAPSnrBSSIDSignalPkts_Type = Integer32
_QtechRrmAPSnrBSSIDSignalPkts_Object = MibTableColumn
qtechRrmAPSnrBSSIDSignalPkts = _QtechRrmAPSnrBSSIDSignalPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14, 1, 5),
    _QtechRrmAPSnrBSSIDSignalPkts_Type()
)
qtechRrmAPSnrBSSIDSignalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDSignalPkts.setStatus("current")
_QtechRrmAPSnrBSSIDHighestRxSignalStrength_Type = Integer32
_QtechRrmAPSnrBSSIDHighestRxSignalStrength_Object = MibTableColumn
qtechRrmAPSnrBSSIDHighestRxSignalStrength = _QtechRrmAPSnrBSSIDHighestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14, 1, 6),
    _QtechRrmAPSnrBSSIDHighestRxSignalStrength_Type()
)
qtechRrmAPSnrBSSIDHighestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDHighestRxSignalStrength.setStatus("current")
_QtechRrmAPSnrBSSIDLowestRxSignalStrength_Type = Integer32
_QtechRrmAPSnrBSSIDLowestRxSignalStrength_Object = MibTableColumn
qtechRrmAPSnrBSSIDLowestRxSignalStrength = _QtechRrmAPSnrBSSIDLowestRxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14, 1, 7),
    _QtechRrmAPSnrBSSIDLowestRxSignalStrength_Type()
)
qtechRrmAPSnrBSSIDLowestRxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDLowestRxSignalStrength.setStatus("current")
_QtechRrmAPSnrBSSIDSampleTime_Type = Integer32
_QtechRrmAPSnrBSSIDSampleTime_Object = MibTableColumn
qtechRrmAPSnrBSSIDSampleTime = _QtechRrmAPSnrBSSIDSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 1, 4, 14, 1, 8),
    _QtechRrmAPSnrBSSIDSampleTime_Type()
)
qtechRrmAPSnrBSSIDSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRrmAPSnrBSSIDSampleTime.setStatus("current")
_QtechRrmMIBTraps_ObjectIdentity = ObjectIdentity
qtechRrmMIBTraps = _QtechRrmMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2)
)
_QtechRrmTrapControl_ObjectIdentity = ObjectIdentity
qtechRrmTrapControl = _QtechRrmTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 1)
)


class _QtechRrmAPDot11bProfileTrapControlMask_Type(Unsigned32):
    """Custom type qtechRrmAPDot11bProfileTrapControlMask based on Unsigned32"""
    defaultValue = 0


_QtechRrmAPDot11bProfileTrapControlMask_Type.__name__ = "Unsigned32"
_QtechRrmAPDot11bProfileTrapControlMask_Object = MibScalar
qtechRrmAPDot11bProfileTrapControlMask = _QtechRrmAPDot11bProfileTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 1, 1),
    _QtechRrmAPDot11bProfileTrapControlMask_Type()
)
qtechRrmAPDot11bProfileTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPDot11bProfileTrapControlMask.setStatus("current")


class _QtechRrmAPDot11aProfileTrapControlMask_Type(Unsigned32):
    """Custom type qtechRrmAPDot11aProfileTrapControlMask based on Unsigned32"""
    defaultValue = 0


_QtechRrmAPDot11aProfileTrapControlMask_Type.__name__ = "Unsigned32"
_QtechRrmAPDot11aProfileTrapControlMask_Object = MibScalar
qtechRrmAPDot11aProfileTrapControlMask = _QtechRrmAPDot11aProfileTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 1, 2),
    _QtechRrmAPDot11aProfileTrapControlMask_Type()
)
qtechRrmAPDot11aProfileTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPDot11aProfileTrapControlMask.setStatus("current")


class _QtechRrmAPDot11bParamUpdateTrapControlMask_Type(Unsigned32):
    """Custom type qtechRrmAPDot11bParamUpdateTrapControlMask based on Unsigned32"""
    defaultValue = 0


_QtechRrmAPDot11bParamUpdateTrapControlMask_Type.__name__ = "Unsigned32"
_QtechRrmAPDot11bParamUpdateTrapControlMask_Object = MibScalar
qtechRrmAPDot11bParamUpdateTrapControlMask = _QtechRrmAPDot11bParamUpdateTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 1, 3),
    _QtechRrmAPDot11bParamUpdateTrapControlMask_Type()
)
qtechRrmAPDot11bParamUpdateTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPDot11bParamUpdateTrapControlMask.setStatus("current")


class _QtechRrmAPDot11aParamUpdateTrapControlMask_Type(Unsigned32):
    """Custom type qtechRrmAPDot11aParamUpdateTrapControlMask based on Unsigned32"""
    defaultValue = 0


_QtechRrmAPDot11aParamUpdateTrapControlMask_Type.__name__ = "Unsigned32"
_QtechRrmAPDot11aParamUpdateTrapControlMask_Object = MibScalar
qtechRrmAPDot11aParamUpdateTrapControlMask = _QtechRrmAPDot11aParamUpdateTrapControlMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 1, 4),
    _QtechRrmAPDot11aParamUpdateTrapControlMask_Type()
)
qtechRrmAPDot11aParamUpdateTrapControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRrmAPDot11aParamUpdateTrapControlMask.setStatus("current")
_QtechRrmTrapVariable_ObjectIdentity = ObjectIdentity
qtechRrmTrapVariable = _QtechRrmTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2)
)
_QtechRrmAPMacAddrTrapVariable_Type = MacAddress
_QtechRrmAPMacAddrTrapVariable_Object = MibScalar
qtechRrmAPMacAddrTrapVariable = _QtechRrmAPMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 1),
    _QtechRrmAPMacAddrTrapVariable_Type()
)
qtechRrmAPMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPMacAddrTrapVariable.setStatus("current")
_QtechRrmAPRadioIDTrapVariable_Type = Integer32
_QtechRrmAPRadioIDTrapVariable_Object = MibScalar
qtechRrmAPRadioIDTrapVariable = _QtechRrmAPRadioIDTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 2),
    _QtechRrmAPRadioIDTrapVariable_Type()
)
qtechRrmAPRadioIDTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPRadioIDTrapVariable.setStatus("current")


class _QtechRrmAPRadioTypeTrapVariable_Type(Integer32):
    """Custom type qtechRrmAPRadioTypeTrapVariable based on Integer32"""
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


_QtechRrmAPRadioTypeTrapVariable_Type.__name__ = "Integer32"
_QtechRrmAPRadioTypeTrapVariable_Object = MibScalar
qtechRrmAPRadioTypeTrapVariable = _QtechRrmAPRadioTypeTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 3),
    _QtechRrmAPRadioTypeTrapVariable_Type()
)
qtechRrmAPRadioTypeTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPRadioTypeTrapVariable.setStatus("current")
_QtechRrmClientNumberTrapVariable_Type = Integer32
_QtechRrmClientNumberTrapVariable_Object = MibScalar
qtechRrmClientNumberTrapVariable = _QtechRrmClientNumberTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 4),
    _QtechRrmClientNumberTrapVariable_Type()
)
qtechRrmClientNumberTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmClientNumberTrapVariable.setStatus("current")
_QtechRrmForeignInterfereTrapVariable_Type = Integer32
_QtechRrmForeignInterfereTrapVariable_Object = MibScalar
qtechRrmForeignInterfereTrapVariable = _QtechRrmForeignInterfereTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 5),
    _QtechRrmForeignInterfereTrapVariable_Type()
)
qtechRrmForeignInterfereTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmForeignInterfereTrapVariable.setStatus("current")
_QtechRrmNoiseTrapVariable_Type = Integer32
_QtechRrmNoiseTrapVariable_Object = MibScalar
qtechRrmNoiseTrapVariable = _QtechRrmNoiseTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 6),
    _QtechRrmNoiseTrapVariable_Type()
)
qtechRrmNoiseTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmNoiseTrapVariable.setStatus("current")
_QtechRrmThroughputTrapVariable_Type = Unsigned32
_QtechRrmThroughputTrapVariable_Object = MibScalar
qtechRrmThroughputTrapVariable = _QtechRrmThroughputTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 7),
    _QtechRrmThroughputTrapVariable_Type()
)
qtechRrmThroughputTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmThroughputTrapVariable.setStatus("current")
_QtechRrmUtilizationTrapVariable_Type = Integer32
_QtechRrmUtilizationTrapVariable_Object = MibScalar
qtechRrmUtilizationTrapVariable = _QtechRrmUtilizationTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 8),
    _QtechRrmUtilizationTrapVariable_Type()
)
qtechRrmUtilizationTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmUtilizationTrapVariable.setStatus("current")
_QtechRrmAPTxPowerBeforeChange_Type = Integer32
_QtechRrmAPTxPowerBeforeChange_Object = MibScalar
qtechRrmAPTxPowerBeforeChange = _QtechRrmAPTxPowerBeforeChange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 9),
    _QtechRrmAPTxPowerBeforeChange_Type()
)
qtechRrmAPTxPowerBeforeChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPTxPowerBeforeChange.setStatus("current")
_QtechRrmAPTxPowerAfterChange_Type = Integer32
_QtechRrmAPTxPowerAfterChange_Object = MibScalar
qtechRrmAPTxPowerAfterChange = _QtechRrmAPTxPowerAfterChange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 10),
    _QtechRrmAPTxPowerAfterChange_Type()
)
qtechRrmAPTxPowerAfterChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPTxPowerAfterChange.setStatus("current")
_QtechRrmAPChannelNumberBeforeChannge_Type = Integer32
_QtechRrmAPChannelNumberBeforeChannge_Object = MibScalar
qtechRrmAPChannelNumberBeforeChannge = _QtechRrmAPChannelNumberBeforeChannge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 11),
    _QtechRrmAPChannelNumberBeforeChannge_Type()
)
qtechRrmAPChannelNumberBeforeChannge.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPChannelNumberBeforeChannge.setStatus("current")
_QtechRrmAPChannelNumberAfterChannge_Type = Integer32
_QtechRrmAPChannelNumberAfterChannge_Object = MibScalar
qtechRrmAPChannelNumberAfterChannge = _QtechRrmAPChannelNumberAfterChannge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 12),
    _QtechRrmAPChannelNumberAfterChannge_Type()
)
qtechRrmAPChannelNumberAfterChannge.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPChannelNumberAfterChannge.setStatus("current")
_QtechRrmDot11bGroupLeaderMacAddrTrapVariable_Type = MacAddress
_QtechRrmDot11bGroupLeaderMacAddrTrapVariable_Object = MibScalar
qtechRrmDot11bGroupLeaderMacAddrTrapVariable = _QtechRrmDot11bGroupLeaderMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 13),
    _QtechRrmDot11bGroupLeaderMacAddrTrapVariable_Type()
)
qtechRrmDot11bGroupLeaderMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmDot11bGroupLeaderMacAddrTrapVariable.setStatus("current")
_QtechRrmDot11aGroupLeaderMacAddrTrapVariable_Type = MacAddress
_QtechRrmDot11aGroupLeaderMacAddrTrapVariable_Object = MibScalar
qtechRrmDot11aGroupLeaderMacAddrTrapVariable = _QtechRrmDot11aGroupLeaderMacAddrTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 14),
    _QtechRrmDot11aGroupLeaderMacAddrTrapVariable_Type()
)
qtechRrmDot11aGroupLeaderMacAddrTrapVariable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmDot11aGroupLeaderMacAddrTrapVariable.setStatus("current")


class _QtechRrmAPChannelChangeReason_Type(Integer32):
    """Custom type qtechRrmAPChannelChangeReason based on Integer32"""
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


_QtechRrmAPChannelChangeReason_Type.__name__ = "Integer32"
_QtechRrmAPChannelChangeReason_Object = MibScalar
qtechRrmAPChannelChangeReason = _QtechRrmAPChannelChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 15),
    _QtechRrmAPChannelChangeReason_Type()
)
qtechRrmAPChannelChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPChannelChangeReason.setStatus("current")
_QtechRrmAPChannelChangeReasonValue_Type = Integer32
_QtechRrmAPChannelChangeReasonValue_Object = MibScalar
qtechRrmAPChannelChangeReasonValue = _QtechRrmAPChannelChangeReasonValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 16),
    _QtechRrmAPChannelChangeReasonValue_Type()
)
qtechRrmAPChannelChangeReasonValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPChannelChangeReasonValue.setStatus("current")


class _QtechRrmAPTxPowerChangeCoverageFlag_Type(Integer32):
    """Custom type qtechRrmAPTxPowerChangeCoverageFlag based on Integer32"""
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


_QtechRrmAPTxPowerChangeCoverageFlag_Type.__name__ = "Integer32"
_QtechRrmAPTxPowerChangeCoverageFlag_Object = MibScalar
qtechRrmAPTxPowerChangeCoverageFlag = _QtechRrmAPTxPowerChangeCoverageFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 17),
    _QtechRrmAPTxPowerChangeCoverageFlag_Type()
)
qtechRrmAPTxPowerChangeCoverageFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPTxPowerChangeCoverageFlag.setStatus("current")
_QtechRrmDFSFreeCount_Type = Integer32
_QtechRrmDFSFreeCount_Object = MibScalar
qtechRrmDFSFreeCount = _QtechRrmDFSFreeCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 18),
    _QtechRrmDFSFreeCount_Type()
)
qtechRrmDFSFreeCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmDFSFreeCount.setStatus("current")
_QtechRrmAPChannelChangeCount_Type = Integer32
_QtechRrmAPChannelChangeCount_Object = MibScalar
qtechRrmAPChannelChangeCount = _QtechRrmAPChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 2, 19),
    _QtechRrmAPChannelChangeCount_Type()
)
qtechRrmAPChannelChangeCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechRrmAPChannelChangeCount.setStatus("current")
_QtechRrmTraps_ObjectIdentity = ObjectIdentity
qtechRrmTraps = _QtechRrmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3)
)
_QtechRrmMIBConformance_ObjectIdentity = ObjectIdentity
qtechRrmMIBConformance = _QtechRrmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 3)
)
_QtechRrmMIBCompliances_ObjectIdentity = ObjectIdentity
qtechRrmMIBCompliances = _QtechRrmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 3, 1)
)
_QtechRrmMIBGroups_ObjectIdentity = ObjectIdentity
qtechRrmMIBGroups = _QtechRrmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 3, 2)
)

# Managed Objects groups

qtechRrmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 3, 2, 1)
)
qtechRrmMIBGroup.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmRFNetworkName"),
        ("QTECH-RRM-MIB", "qtechRrmAPName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThresholdRadioType"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfForeignInterferenceThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfForeignNoiseThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRFUtilizationThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThroughputThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfMobilesThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThresholdMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThresholdRadioType"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThresholdName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfLoadRxUtilization"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfLoadTxUtilization"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfLoadChannelUtilization"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfLoadNumOfClients"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfPoorSNRClients"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfLoadName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfLoadMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfLoadSlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThroughput"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfInterferenceChannelNo"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfInterferencePower"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfInterferenceUtilization"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfInterferenceName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfInterferenceMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfInterferenceSlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfNoiseChannelNo"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfDBNoisePower"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfNoiseName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfNoiseMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfNoiseSlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfLoadProfileState"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfInterferenceProfileState"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfNoiseProfileState"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfCoverageProfileState"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfPerformanceProfileState"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfProfileName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfProfileMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfProfileSlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborMacAddress"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborSlot"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborIpAddress"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborRSSI"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborSNR"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborChannel"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborChannelWidth"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRxNeighborSlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationRSSICoverageIndex"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRSSILevel"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationCountOnRSSI"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationRSSIName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationRSSIMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationRSSISlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationSNRCoverageIndex"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfSNRLevel"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationCountOnSNR"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationSNRName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationSNRMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfStationSNRSlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRecommendedChannelNumber"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRecommendedTxPowerLevel"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRecommendedRTSThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRecommendedFragmentationThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRecommendedName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRecommendedMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfRecommendedSlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioID"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioType"),
        ("QTECH-RRM-MIB", "qtechRrmAPRealName"),
        ("QTECH-RRM-MIB", "qtechRrmAPMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThroughputMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThroughputSlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThroughputAPName"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThroughputRx"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThroughputTx"),
        ("QTECH-RRM-MIB", "qtechRrmAPIfThroughputTotal"),
        ("QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDSlotId"),
        ("QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDAPName"),
        ("QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDAverageSignalStrength"),
        ("QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDSignalPkts"),
        ("QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDHighestRxSignalStrength"),
        ("QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDLowestRxSignalStrength"),
        ("QTECH-RRM-MIB", "qtechRrmAPSnrBSSIDSampleTime"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bDynamicChannelAssignment"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bAnchorTime"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bChannalWidth11n"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bDynamicChannelUpdateInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bDCASensitivity"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bForeignInterfereFactorEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bLoadFactorEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bNoiseFactorEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bChannelUpdateCmdInvoke"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bDCAChannelIndex"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bDCAChannelOperation"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aDynamicChannelAssignment"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aAnchorTime"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aChannalWidth11n"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aDynamicChannelUpdateInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aDCASensitivity"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aForeignInterfereFactorEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aLoadFactorEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aNoiseFactorEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aChannelUpdateCmdInvoke"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aDCAChannelIndex"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aDCAChannelOperation"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bDTPCSupport"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bDynamicTransmitPowerControl"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bDynamicTxPowerControlInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCurrentTxPowerLevel"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bPowerUpdateCmdInvoke"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bTXPowerThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bTPCNeighborNumber"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aDTPCSupport"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aDynamicTransmitPowerControl"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aDynamicTxPowerControlInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCurrentTxPowerLevel"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aPowerUpdateCmdInvoke"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aTXPowerThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aTPCNeighborNumber"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageExceptionGlobal"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageLevelGlobal"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageDataRSSIThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageVoiceRSSIThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageDataPacketCount"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageVoicePacketCount"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageDataFailRate"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageVoiceFailRate"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageExceptionGlobal"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageLevelGlobal"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageDataRSSIThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageVoiceRSSIThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageDataPacketCount"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageVoicePacketCount"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageDataFailRate"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageVoiceFailRate"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bGlobalAutomaticGrouping"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bGroupLeaderMacAddr"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bGroupLeader"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bGroupLastUpdateTime"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bGroupInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bPeerMacAddress"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bPeerIpAddress"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bAPname"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bAPRadioID"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bAPChannel"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bAPTxPower"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bAPChannelRrmChangeFlag"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bAPTxPowerRrmChangeFlag"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bSummaryMacAddress"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aGlobalAutomaticGrouping"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aGroupLeader"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aGroupLastUpdateTime"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aGroupInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aPeerMacAddress"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aPeerIpAddress"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aAPname"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aAPRadioID"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aAPChannel"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aAPTxPower"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aAPChannelRrmChangeFlag"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aAPTxPowerRrmChangeFlag"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aSummaryMacAddress"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bForeignInterferenceThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bForeignNoiseThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bRFUtilizationThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bThroughputThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bMobilesThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aForeignInterferenceThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aForeignNoiseThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aRFUtilizationThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aThroughputThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aMobilesThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bMonitorEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bChannelMonitorList"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bMonitorInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bCoverageMeasurementInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bLoadMeasurementInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bNoiseMeasurementInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bSignalMeasurementInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bNeighborMessageInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aMonitorEnable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aChannelMonitorList"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aMonitorInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aCoverageMeasurementInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aLoadMeasurementInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aNoiseMeasurementInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aSignalMeasurementInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aNeighborMessageInterval"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bSetFactoryDefault"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aSetFactoryDefault"))
)
if mibBuilder.loadTexts:
    qtechRrmMIBGroup.setStatus("current")

qtechRrmTrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 3, 2, 2)
)
qtechRrmTrapsGroup.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPDot11bProfileTrapControlMask"),
        ("QTECH-RRM-MIB", "qtechRrmAPDot11aProfileTrapControlMask"),
        ("QTECH-RRM-MIB", "qtechRrmAPDot11bParamUpdateTrapControlMask"),
        ("QTECH-RRM-MIB", "qtechRrmAPDot11aParamUpdateTrapControlMask"),
        ("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmClientNumberTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmForeignInterfereTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmNoiseTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmThroughputTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmUtilizationTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPTxPowerBeforeChange"),
        ("QTECH-RRM-MIB", "qtechRrmAPTxPowerAfterChange"),
        ("QTECH-RRM-MIB", "qtechRrmAPTxPowerChangeCoverageFlag"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelNumberBeforeChannge"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelNumberAfterChannge"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelChangeReason"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelChangeReasonValue"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelChangeCount"),
        ("QTECH-RRM-MIB", "qtechRrmDFSFreeCount"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bGroupLeaderMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aGroupLeaderMacAddrTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmTrapsGroup.setStatus("current")


# Notification objects

qtechRrmAPClientNumProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 1)
)
qtechRrmAPClientNumProfileFailed.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmClientNumberTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPClientNumProfileFailed.setStatus(
        "current"
    )

qtechRrmAPLoadProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 2)
)
qtechRrmAPLoadProfileFailed.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmUtilizationTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPLoadProfileFailed.setStatus(
        "current"
    )

qtechRrmAPNoiseProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 3)
)
qtechRrmAPNoiseProfileFailed.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmNoiseTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPNoiseProfileFailed.setStatus(
        "current"
    )

qtechRrmAPInterferenceProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 4)
)
qtechRrmAPInterferenceProfileFailed.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmForeignInterfereTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPInterferenceProfileFailed.setStatus(
        "current"
    )

qtechRrmAPPerformanceProfileFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 5)
)
qtechRrmAPPerformanceProfileFailed.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmThroughputTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPPerformanceProfileFailed.setStatus(
        "current"
    )

qtechRrmAPClientNumProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 6)
)
qtechRrmAPClientNumProfileUpdatedToPass.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmClientNumberTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPClientNumProfileUpdatedToPass.setStatus(
        "current"
    )

qtechRrmAPLoadProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 7)
)
qtechRrmAPLoadProfileUpdatedToPass.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmUtilizationTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPLoadProfileUpdatedToPass.setStatus(
        "current"
    )

qtechRrmAPNoiseProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 8)
)
qtechRrmAPNoiseProfileUpdatedToPass.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmNoiseTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPNoiseProfileUpdatedToPass.setStatus(
        "current"
    )

qtechRrmAPInterferenceProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 9)
)
qtechRrmAPInterferenceProfileUpdatedToPass.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmForeignInterfereTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPInterferenceProfileUpdatedToPass.setStatus(
        "current"
    )

qtechRrmAPPerformanceProfileUpdatedToPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 10)
)
qtechRrmAPPerformanceProfileUpdatedToPass.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmThroughputTrapVariable"))
)
if mibBuilder.loadTexts:
    qtechRrmAPPerformanceProfileUpdatedToPass.setStatus(
        "current"
    )

qtechRrmAPCurrentTxPowerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 11)
)
qtechRrmAPCurrentTxPowerChanged.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPTxPowerBeforeChange"),
        ("QTECH-RRM-MIB", "qtechRrmAPTxPowerAfterChange"),
        ("QTECH-RRM-MIB", "qtechRrmAPTxPowerChangeCoverageFlag"))
)
if mibBuilder.loadTexts:
    qtechRrmAPCurrentTxPowerChanged.setStatus(
        "current"
    )

qtechRrmAPCurrentChannelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 12)
)
qtechRrmAPCurrentChannelChanged.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioIDTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPRadioTypeTrapVariable"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelNumberBeforeChannge"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelNumberAfterChannge"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelChangeReason"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelChangeReasonValue"),
        ("QTECH-RRM-MIB", "qtechRrmAPChannelChangeCount"))
)
if mibBuilder.loadTexts:
    qtechRrmAPCurrentChannelChanged.setStatus(
        "current"
    )

qtechRrmDot11bGroupingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 13)
)
qtechRrmDot11bGroupingDone.setObjects(
    ("QTECH-RRM-MIB", "qtechRrmDot11bGroupLeaderMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    qtechRrmDot11bGroupingDone.setStatus(
        "current"
    )

qtechRrmDot11aGroupingDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 14)
)
qtechRrmDot11aGroupingDone.setObjects(
    ("QTECH-RRM-MIB", "qtechRrmDot11aGroupLeaderMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    qtechRrmDot11aGroupingDone.setStatus(
        "current"
    )

qtechRrmDot11bDFSFreeCountBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 15)
)
qtechRrmDot11bDFSFreeCountBelowThreshold.setObjects(
    ("QTECH-RRM-MIB", "qtechRrmDFSFreeCount")
)
if mibBuilder.loadTexts:
    qtechRrmDot11bDFSFreeCountBelowThreshold.setStatus(
        "current"
    )

qtechRrmDot11aDFSFreeCountBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 16)
)
qtechRrmDot11aDFSFreeCountBelowThreshold.setObjects(
    ("QTECH-RRM-MIB", "qtechRrmDFSFreeCount")
)
if mibBuilder.loadTexts:
    qtechRrmDot11aDFSFreeCountBelowThreshold.setStatus(
        "current"
    )

qtechRrmNeighborAPInterference = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 17)
)
qtechRrmNeighborAPInterference.setObjects(
    ("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    qtechRrmNeighborAPInterference.setStatus(
        "current"
    )

qtechRrmStationInterference = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 18)
)
qtechRrmStationInterference.setObjects(
    ("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    qtechRrmStationInterference.setStatus(
        "current"
    )

qtechRrmOtherDiveceInterference = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 2, 3, 19)
)
qtechRrmOtherDiveceInterference.setObjects(
    ("QTECH-RRM-MIB", "qtechRrmAPMacAddrTrapVariable")
)
if mibBuilder.loadTexts:
    qtechRrmOtherDiveceInterference.setStatus(
        "current"
    )


# Notifications groups

qtechRrmTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 3, 2, 3)
)
qtechRrmTrap.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmAPClientNumProfileFailed"),
        ("QTECH-RRM-MIB", "qtechRrmAPLoadProfileFailed"),
        ("QTECH-RRM-MIB", "qtechRrmAPNoiseProfileFailed"),
        ("QTECH-RRM-MIB", "qtechRrmAPInterferenceProfileFailed"),
        ("QTECH-RRM-MIB", "qtechRrmAPPerformanceProfileFailed"),
        ("QTECH-RRM-MIB", "qtechRrmAPClientNumProfileUpdatedToPass"),
        ("QTECH-RRM-MIB", "qtechRrmAPLoadProfileUpdatedToPass"),
        ("QTECH-RRM-MIB", "qtechRrmAPNoiseProfileUpdatedToPass"),
        ("QTECH-RRM-MIB", "qtechRrmAPInterferenceProfileUpdatedToPass"),
        ("QTECH-RRM-MIB", "qtechRrmAPPerformanceProfileUpdatedToPass"),
        ("QTECH-RRM-MIB", "qtechRrmAPCurrentTxPowerChanged"),
        ("QTECH-RRM-MIB", "qtechRrmAPCurrentChannelChanged"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bGroupingDone"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aGroupingDone"),
        ("QTECH-RRM-MIB", "qtechRrmDot11bDFSFreeCountBelowThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmDot11aDFSFreeCountBelowThreshold"),
        ("QTECH-RRM-MIB", "qtechRrmNeighborAPInterference"),
        ("QTECH-RRM-MIB", "qtechRrmStationInterference"),
        ("QTECH-RRM-MIB", "qtechRrmOtherDiveceInterference"))
)
if mibBuilder.loadTexts:
    qtechRrmTrap.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechRrmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 63, 3, 1, 1)
)
qtechRrmMIBCompliance.setObjects(
      *(("QTECH-RRM-MIB", "qtechRrmMIBGroup"),
        ("QTECH-RRM-MIB", "qtechRrmTrapsGroup"))
)
if mibBuilder.loadTexts:
    qtechRrmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-RRM-MIB",
    **{"ProfileState": ProfileState,
       "qtechRrmMIB": qtechRrmMIB,
       "qtechRrmMIBObjects": qtechRrmMIBObjects,
       "qtechRrmObjectsGroup": qtechRrmObjectsGroup,
       "qtechRrmRFNetworkName": qtechRrmRFNetworkName,
       "qtechRrmObjectsDot11a": qtechRrmObjectsDot11a,
       "qtechRrmDCADot11a": qtechRrmDCADot11a,
       "qtechRrmDot11aDynamicChannelAssignment": qtechRrmDot11aDynamicChannelAssignment,
       "qtechRrmDot11aAnchorTime": qtechRrmDot11aAnchorTime,
       "qtechRrmDot11aChannalWidth11n": qtechRrmDot11aChannalWidth11n,
       "qtechRrmDot11aDynamicChannelUpdateInterval": qtechRrmDot11aDynamicChannelUpdateInterval,
       "qtechRrmDot11aDCASensitivity": qtechRrmDot11aDCASensitivity,
       "qtechRrmDot11aForeignInterfereFactorEnable": qtechRrmDot11aForeignInterfereFactorEnable,
       "qtechRrmDot11aLoadFactorEnable": qtechRrmDot11aLoadFactorEnable,
       "qtechRrmDot11aNoiseFactorEnable": qtechRrmDot11aNoiseFactorEnable,
       "qtechRrmDot11aChannelUpdateCmdInvoke": qtechRrmDot11aChannelUpdateCmdInvoke,
       "qtechRrmDot11aDCAChannelTable": qtechRrmDot11aDCAChannelTable,
       "qtechRrmDot11aDCAChannelEntry": qtechRrmDot11aDCAChannelEntry,
       "qtechRrmDot11aDCAChannelIndex": qtechRrmDot11aDCAChannelIndex,
       "qtechRrmDot11aDCAChannelOperation": qtechRrmDot11aDCAChannelOperation,
       "qtechRrmTPCDot11a": qtechRrmTPCDot11a,
       "qtechRrmDot11aDTPCSupport": qtechRrmDot11aDTPCSupport,
       "qtechRrmDot11aDynamicTransmitPowerControl": qtechRrmDot11aDynamicTransmitPowerControl,
       "qtechRrmDot11aDynamicTxPowerControlInterval": qtechRrmDot11aDynamicTxPowerControlInterval,
       "qtechRrmDot11aCurrentTxPowerLevel": qtechRrmDot11aCurrentTxPowerLevel,
       "qtechRrmDot11aPowerUpdateCmdInvoke": qtechRrmDot11aPowerUpdateCmdInvoke,
       "qtechRrmDot11aTXPowerThreshold": qtechRrmDot11aTXPowerThreshold,
       "qtechRrmDot11aTPCNeighborNumber": qtechRrmDot11aTPCNeighborNumber,
       "qtechRrmCHDDot11a": qtechRrmCHDDot11a,
       "qtechRrmDot11aCoverageEnable": qtechRrmDot11aCoverageEnable,
       "qtechRrmDot11aCoverageExceptionGlobal": qtechRrmDot11aCoverageExceptionGlobal,
       "qtechRrmDot11aCoverageLevelGlobal": qtechRrmDot11aCoverageLevelGlobal,
       "qtechRrmDot11aCoverageDataRSSIThreshold": qtechRrmDot11aCoverageDataRSSIThreshold,
       "qtechRrmDot11aCoverageVoiceRSSIThreshold": qtechRrmDot11aCoverageVoiceRSSIThreshold,
       "qtechRrmDot11aCoverageDataPacketCount": qtechRrmDot11aCoverageDataPacketCount,
       "qtechRrmDot11aCoverageVoicePacketCount": qtechRrmDot11aCoverageVoicePacketCount,
       "qtechRrmDot11aCoverageDataFailRate": qtechRrmDot11aCoverageDataFailRate,
       "qtechRrmDot11aCoverageVoiceFailRate": qtechRrmDot11aCoverageVoiceFailRate,
       "qtechRrmGroupDot11a": qtechRrmGroupDot11a,
       "qtechRrmDot11aGlobalAutomaticGrouping": qtechRrmDot11aGlobalAutomaticGrouping,
       "qtechRrmDot11aGroupLeaderMacAddr": qtechRrmDot11aGroupLeaderMacAddr,
       "qtechRrmDot11aGroupLeader": qtechRrmDot11aGroupLeader,
       "qtechRrmDot11aGroupLastUpdateTime": qtechRrmDot11aGroupLastUpdateTime,
       "qtechRrmDot11aGroupInterval": qtechRrmDot11aGroupInterval,
       "qtechRrmDot11aGroupTable": qtechRrmDot11aGroupTable,
       "qtechRrmDot11aGroupEntry": qtechRrmDot11aGroupEntry,
       "qtechRrmDot11aPeerMacAddress": qtechRrmDot11aPeerMacAddress,
       "qtechRrmDot11aPeerIpAddress": qtechRrmDot11aPeerIpAddress,
       "qtechRrmDot11aSummaryTable": qtechRrmDot11aSummaryTable,
       "qtechRrmDot11aSummaryEntry": qtechRrmDot11aSummaryEntry,
       "qtechRrmDot11aAPname": qtechRrmDot11aAPname,
       "qtechRrmDot11aAPRadioID": qtechRrmDot11aAPRadioID,
       "qtechRrmDot11aAPChannel": qtechRrmDot11aAPChannel,
       "qtechRrmDot11aAPTxPower": qtechRrmDot11aAPTxPower,
       "qtechRrmDot11aAPChannelRrmChangeFlag": qtechRrmDot11aAPChannelRrmChangeFlag,
       "qtechRrmDot11aAPTxPowerRrmChangeFlag": qtechRrmDot11aAPTxPowerRrmChangeFlag,
       "qtechRrmDot11aSummaryMacAddress": qtechRrmDot11aSummaryMacAddress,
       "qtechRrmProfileDot11a": qtechRrmProfileDot11a,
       "qtechRrmDot11aForeignInterferenceThreshold": qtechRrmDot11aForeignInterferenceThreshold,
       "qtechRrmDot11aForeignNoiseThreshold": qtechRrmDot11aForeignNoiseThreshold,
       "qtechRrmDot11aRFUtilizationThreshold": qtechRrmDot11aRFUtilizationThreshold,
       "qtechRrmDot11aThroughputThreshold": qtechRrmDot11aThroughputThreshold,
       "qtechRrmDot11aMobilesThreshold": qtechRrmDot11aMobilesThreshold,
       "qtechRrmMonitorDot11a": qtechRrmMonitorDot11a,
       "qtechRrmDot11aMonitorEnable": qtechRrmDot11aMonitorEnable,
       "qtechRrmDot11aChannelMonitorList": qtechRrmDot11aChannelMonitorList,
       "qtechRrmDot11aMonitorInterval": qtechRrmDot11aMonitorInterval,
       "qtechRrmDot11aCoverageMeasurementInterval": qtechRrmDot11aCoverageMeasurementInterval,
       "qtechRrmDot11aLoadMeasurementInterval": qtechRrmDot11aLoadMeasurementInterval,
       "qtechRrmDot11aNoiseMeasurementInterval": qtechRrmDot11aNoiseMeasurementInterval,
       "qtechRrmDot11aSignalMeasurementInterval": qtechRrmDot11aSignalMeasurementInterval,
       "qtechRrmDot11aNeighborMessageInterval": qtechRrmDot11aNeighborMessageInterval,
       "qtechRrmFactoryDot11a": qtechRrmFactoryDot11a,
       "qtechRrmDot11aSetFactoryDefault": qtechRrmDot11aSetFactoryDefault,
       "qtechRrmObjectsDot11b": qtechRrmObjectsDot11b,
       "qtechRrmDCADot11b": qtechRrmDCADot11b,
       "qtechRrmDot11bDynamicChannelAssignment": qtechRrmDot11bDynamicChannelAssignment,
       "qtechRrmDot11bAnchorTime": qtechRrmDot11bAnchorTime,
       "qtechRrmDot11bChannalWidth11n": qtechRrmDot11bChannalWidth11n,
       "qtechRrmDot11bDynamicChannelUpdateInterval": qtechRrmDot11bDynamicChannelUpdateInterval,
       "qtechRrmDot11bDCASensitivity": qtechRrmDot11bDCASensitivity,
       "qtechRrmDot11bForeignInterfereFactorEnable": qtechRrmDot11bForeignInterfereFactorEnable,
       "qtechRrmDot11bLoadFactorEnable": qtechRrmDot11bLoadFactorEnable,
       "qtechRrmDot11bNoiseFactorEnable": qtechRrmDot11bNoiseFactorEnable,
       "qtechRrmDot11bChannelUpdateCmdInvoke": qtechRrmDot11bChannelUpdateCmdInvoke,
       "qtechRrmDot11bDCAChannelTable": qtechRrmDot11bDCAChannelTable,
       "qtechRrmDot11bDCAChannelEntry": qtechRrmDot11bDCAChannelEntry,
       "qtechRrmDot11bDCAChannelIndex": qtechRrmDot11bDCAChannelIndex,
       "qtechRrmDot11bDCAChannelOperation": qtechRrmDot11bDCAChannelOperation,
       "qtechRrmTPCDot11b": qtechRrmTPCDot11b,
       "qtechRrmDot11bDTPCSupport": qtechRrmDot11bDTPCSupport,
       "qtechRrmDot11bDynamicTransmitPowerControl": qtechRrmDot11bDynamicTransmitPowerControl,
       "qtechRrmDot11bDynamicTxPowerControlInterval": qtechRrmDot11bDynamicTxPowerControlInterval,
       "qtechRrmDot11bCurrentTxPowerLevel": qtechRrmDot11bCurrentTxPowerLevel,
       "qtechRrmDot11bPowerUpdateCmdInvoke": qtechRrmDot11bPowerUpdateCmdInvoke,
       "qtechRrmDot11bTXPowerThreshold": qtechRrmDot11bTXPowerThreshold,
       "qtechRrmDot11bTPCNeighborNumber": qtechRrmDot11bTPCNeighborNumber,
       "qtechRrmCHDDot11b": qtechRrmCHDDot11b,
       "qtechRrmDot11bCoverageEnable": qtechRrmDot11bCoverageEnable,
       "qtechRrmDot11bCoverageExceptionGlobal": qtechRrmDot11bCoverageExceptionGlobal,
       "qtechRrmDot11bCoverageLevelGlobal": qtechRrmDot11bCoverageLevelGlobal,
       "qtechRrmDot11bCoverageDataRSSIThreshold": qtechRrmDot11bCoverageDataRSSIThreshold,
       "qtechRrmDot11bCoverageVoiceRSSIThreshold": qtechRrmDot11bCoverageVoiceRSSIThreshold,
       "qtechRrmDot11bCoverageDataPacketCount": qtechRrmDot11bCoverageDataPacketCount,
       "qtechRrmDot11bCoverageVoicePacketCount": qtechRrmDot11bCoverageVoicePacketCount,
       "qtechRrmDot11bCoverageDataFailRate": qtechRrmDot11bCoverageDataFailRate,
       "qtechRrmDot11bCoverageVoiceFailRate": qtechRrmDot11bCoverageVoiceFailRate,
       "qtechRrmGroupDot11b": qtechRrmGroupDot11b,
       "qtechRrmDot11bGlobalAutomaticGrouping": qtechRrmDot11bGlobalAutomaticGrouping,
       "qtechRrmDot11bGroupLeaderMacAddr": qtechRrmDot11bGroupLeaderMacAddr,
       "qtechRrmDot11bGroupLeader": qtechRrmDot11bGroupLeader,
       "qtechRrmDot11bGroupLastUpdateTime": qtechRrmDot11bGroupLastUpdateTime,
       "qtechRrmDot11bGroupInterval": qtechRrmDot11bGroupInterval,
       "qtechRrmDot11bGroupTable": qtechRrmDot11bGroupTable,
       "qtechRrmDot11bGroupEntry": qtechRrmDot11bGroupEntry,
       "qtechRrmDot11bPeerMacAddress": qtechRrmDot11bPeerMacAddress,
       "qtechRrmDot11bPeerIpAddress": qtechRrmDot11bPeerIpAddress,
       "qtechRrmDot11bSummaryTable": qtechRrmDot11bSummaryTable,
       "qtechRrmDot11bSummaryEntry": qtechRrmDot11bSummaryEntry,
       "qtechRrmDot11bAPname": qtechRrmDot11bAPname,
       "qtechRrmDot11bAPRadioID": qtechRrmDot11bAPRadioID,
       "qtechRrmDot11bAPChannel": qtechRrmDot11bAPChannel,
       "qtechRrmDot11bAPTxPower": qtechRrmDot11bAPTxPower,
       "qtechRrmDot11bAPChannelRrmChangeFlag": qtechRrmDot11bAPChannelRrmChangeFlag,
       "qtechRrmDot11bAPTxPowerRrmChangeFlag": qtechRrmDot11bAPTxPowerRrmChangeFlag,
       "qtechRrmDot11bSummaryMacAddress": qtechRrmDot11bSummaryMacAddress,
       "qtechRrmProfileDot11b": qtechRrmProfileDot11b,
       "qtechRrmDot11bForeignInterferenceThreshold": qtechRrmDot11bForeignInterferenceThreshold,
       "qtechRrmDot11bForeignNoiseThreshold": qtechRrmDot11bForeignNoiseThreshold,
       "qtechRrmDot11bRFUtilizationThreshold": qtechRrmDot11bRFUtilizationThreshold,
       "qtechRrmDot11bThroughputThreshold": qtechRrmDot11bThroughputThreshold,
       "qtechRrmDot11bMobilesThreshold": qtechRrmDot11bMobilesThreshold,
       "qtechRrmMonitorDot11b": qtechRrmMonitorDot11b,
       "qtechRrmDot11bMonitorEnable": qtechRrmDot11bMonitorEnable,
       "qtechRrmDot11bChannelMonitorList": qtechRrmDot11bChannelMonitorList,
       "qtechRrmDot11bMonitorInterval": qtechRrmDot11bMonitorInterval,
       "qtechRrmDot11bCoverageMeasurementInterval": qtechRrmDot11bCoverageMeasurementInterval,
       "qtechRrmDot11bLoadMeasurementInterval": qtechRrmDot11bLoadMeasurementInterval,
       "qtechRrmDot11bNoiseMeasurementInterval": qtechRrmDot11bNoiseMeasurementInterval,
       "qtechRrmDot11bSignalMeasurementInterval": qtechRrmDot11bSignalMeasurementInterval,
       "qtechRrmDot11bNeighborMessageInterval": qtechRrmDot11bNeighborMessageInterval,
       "qtechRrmFactoryDot11b": qtechRrmFactoryDot11b,
       "qtechRrmDot11bSetFactoryDefault": qtechRrmDot11bSetFactoryDefault,
       "qtechRrmObjectsAP": qtechRrmObjectsAP,
       "qtechRrmAPIfSlotId": qtechRrmAPIfSlotId,
       "qtechRrmAPName": qtechRrmAPName,
       "qtechRrmAPIfProfileThresholdConfigTable": qtechRrmAPIfProfileThresholdConfigTable,
       "qtechRrmAPIfProfileThresholdConfigEntry": qtechRrmAPIfProfileThresholdConfigEntry,
       "qtechRrmAPIfThresholdRadioType": qtechRrmAPIfThresholdRadioType,
       "qtechRrmAPIfForeignInterferenceThreshold": qtechRrmAPIfForeignInterferenceThreshold,
       "qtechRrmAPIfForeignNoiseThreshold": qtechRrmAPIfForeignNoiseThreshold,
       "qtechRrmAPIfRFUtilizationThreshold": qtechRrmAPIfRFUtilizationThreshold,
       "qtechRrmAPIfThroughputThreshold": qtechRrmAPIfThroughputThreshold,
       "qtechRrmAPIfMobilesThreshold": qtechRrmAPIfMobilesThreshold,
       "qtechRrmAPIfThresholdName": qtechRrmAPIfThresholdName,
       "qtechRrmAPIfThresholdMacAddr": qtechRrmAPIfThresholdMacAddr,
       "qtechRrmAPIfForeignGlobalConfig": qtechRrmAPIfForeignGlobalConfig,
       "qtechRrmAPIfNoiseGlobalConfig": qtechRrmAPIfNoiseGlobalConfig,
       "qtechRrmAPIfRFUtilizationGlobalConfig": qtechRrmAPIfRFUtilizationGlobalConfig,
       "qtechRrmAPIfThroughputGlobalConfig": qtechRrmAPIfThroughputGlobalConfig,
       "qtechRrmAPIfMobilesGlobalConfig": qtechRrmAPIfMobilesGlobalConfig,
       "qtechRrmAPIfLoadParametersTable": qtechRrmAPIfLoadParametersTable,
       "qtechRrmAPIfLoadParametersEntry": qtechRrmAPIfLoadParametersEntry,
       "qtechRrmAPIfLoadRxUtilization": qtechRrmAPIfLoadRxUtilization,
       "qtechRrmAPIfLoadTxUtilization": qtechRrmAPIfLoadTxUtilization,
       "qtechRrmAPIfLoadChannelUtilization": qtechRrmAPIfLoadChannelUtilization,
       "qtechRrmAPIfLoadNumOfClients": qtechRrmAPIfLoadNumOfClients,
       "qtechRrmAPIfPoorSNRClients": qtechRrmAPIfPoorSNRClients,
       "qtechRrmAPIfLoadName": qtechRrmAPIfLoadName,
       "qtechRrmAPIfLoadMacAddr": qtechRrmAPIfLoadMacAddr,
       "qtechRrmAPIfLoadSlotId": qtechRrmAPIfLoadSlotId,
       "qtechRrmAPIfThroughput": qtechRrmAPIfThroughput,
       "qtechRrmAPIfChannelInterferenceInfoTable": qtechRrmAPIfChannelInterferenceInfoTable,
       "qtechRrmAPIfChannelInterferenceInfoEntry": qtechRrmAPIfChannelInterferenceInfoEntry,
       "qtechRrmAPIfInterferenceChannelNo": qtechRrmAPIfInterferenceChannelNo,
       "qtechRrmAPIfInterferencePower": qtechRrmAPIfInterferencePower,
       "qtechRrmAPIfInterferenceUtilization": qtechRrmAPIfInterferenceUtilization,
       "qtechRrmAPIfInterferenceName": qtechRrmAPIfInterferenceName,
       "qtechRrmAPIfInterferenceMacAddr": qtechRrmAPIfInterferenceMacAddr,
       "qtechRrmAPIfInterferenceSlotId": qtechRrmAPIfInterferenceSlotId,
       "qtechRrmAPIfChannelNoiseInfoTable": qtechRrmAPIfChannelNoiseInfoTable,
       "qtechRrmAPIfChannelNoiseInfoEntry": qtechRrmAPIfChannelNoiseInfoEntry,
       "qtechRrmAPIfNoiseChannelNo": qtechRrmAPIfNoiseChannelNo,
       "qtechRrmAPIfDBNoisePower": qtechRrmAPIfDBNoisePower,
       "qtechRrmAPIfNoiseName": qtechRrmAPIfNoiseName,
       "qtechRrmAPIfNoiseMacAddr": qtechRrmAPIfNoiseMacAddr,
       "qtechRrmAPIfNoiseSlotId": qtechRrmAPIfNoiseSlotId,
       "qtechRrmAPIfProfileStateTable": qtechRrmAPIfProfileStateTable,
       "qtechRrmAPIfProfileStateEntry": qtechRrmAPIfProfileStateEntry,
       "qtechRrmAPIfLoadProfileState": qtechRrmAPIfLoadProfileState,
       "qtechRrmAPIfInterferenceProfileState": qtechRrmAPIfInterferenceProfileState,
       "qtechRrmAPIfNoiseProfileState": qtechRrmAPIfNoiseProfileState,
       "qtechRrmAPIfCoverageProfileState": qtechRrmAPIfCoverageProfileState,
       "qtechRrmAPIfPerformanceProfileState": qtechRrmAPIfPerformanceProfileState,
       "qtechRrmAPIfProfileName": qtechRrmAPIfProfileName,
       "qtechRrmAPIfProfileMacAddr": qtechRrmAPIfProfileMacAddr,
       "qtechRrmAPIfProfileSlotId": qtechRrmAPIfProfileSlotId,
       "qtechRrmAPIfRxNeighborsTable": qtechRrmAPIfRxNeighborsTable,
       "qtechRrmAPIfRxNeighborsEntry": qtechRrmAPIfRxNeighborsEntry,
       "qtechRrmAPIfRxNeighborMacAddress": qtechRrmAPIfRxNeighborMacAddress,
       "qtechRrmAPIfRxNeighborSlot": qtechRrmAPIfRxNeighborSlot,
       "qtechRrmAPIfRxNeighborIpAddress": qtechRrmAPIfRxNeighborIpAddress,
       "qtechRrmAPIfRxNeighborRSSI": qtechRrmAPIfRxNeighborRSSI,
       "qtechRrmAPIfRxNeighborSNR": qtechRrmAPIfRxNeighborSNR,
       "qtechRrmAPIfRxNeighborChannel": qtechRrmAPIfRxNeighborChannel,
       "qtechRrmAPIfRxNeighborChannelWidth": qtechRrmAPIfRxNeighborChannelWidth,
       "qtechRrmAPIfRxNeighborName": qtechRrmAPIfRxNeighborName,
       "qtechRrmAPIfRxNeighborMacAddr": qtechRrmAPIfRxNeighborMacAddr,
       "qtechRrmAPIfRxNeighborSlotId": qtechRrmAPIfRxNeighborSlotId,
       "qtechRrmAPIfStationRSSICoverageInfoTable": qtechRrmAPIfStationRSSICoverageInfoTable,
       "qtechRrmAPIfStationRSSICoverageInfoEntry": qtechRrmAPIfStationRSSICoverageInfoEntry,
       "qtechRrmAPIfStationRSSICoverageIndex": qtechRrmAPIfStationRSSICoverageIndex,
       "qtechRrmAPIfRSSILevel": qtechRrmAPIfRSSILevel,
       "qtechRrmAPIfStationCountOnRSSI": qtechRrmAPIfStationCountOnRSSI,
       "qtechRrmAPIfStationRSSIName": qtechRrmAPIfStationRSSIName,
       "qtechRrmAPIfStationRSSIMacAddr": qtechRrmAPIfStationRSSIMacAddr,
       "qtechRrmAPIfStationRSSISlotId": qtechRrmAPIfStationRSSISlotId,
       "qtechRrmAPIfStationSNRCoverageInfoTable": qtechRrmAPIfStationSNRCoverageInfoTable,
       "qtechRrmAPIfStationSNRCoverageInfoEntry": qtechRrmAPIfStationSNRCoverageInfoEntry,
       "qtechRrmAPIfStationSNRCoverageIndex": qtechRrmAPIfStationSNRCoverageIndex,
       "qtechRrmAPIfSNRLevel": qtechRrmAPIfSNRLevel,
       "qtechRrmAPIfStationCountOnSNR": qtechRrmAPIfStationCountOnSNR,
       "qtechRrmAPIfStationSNRName": qtechRrmAPIfStationSNRName,
       "qtechRrmAPIfStationSNRMacAddr": qtechRrmAPIfStationSNRMacAddr,
       "qtechRrmAPIfStationSNRSlotId": qtechRrmAPIfStationSNRSlotId,
       "qtechRrmAPIfRecommendedRFParametersTable": qtechRrmAPIfRecommendedRFParametersTable,
       "qtechRrmAPIfRecommendedRFParametersEntry": qtechRrmAPIfRecommendedRFParametersEntry,
       "qtechRrmAPIfRecommendedChannelNumber": qtechRrmAPIfRecommendedChannelNumber,
       "qtechRrmAPIfRecommendedTxPowerLevel": qtechRrmAPIfRecommendedTxPowerLevel,
       "qtechRrmAPIfRecommendedRTSThreshold": qtechRrmAPIfRecommendedRTSThreshold,
       "qtechRrmAPIfRecommendedFragmentationThreshold": qtechRrmAPIfRecommendedFragmentationThreshold,
       "qtechRrmAPIfRecommendedName": qtechRrmAPIfRecommendedName,
       "qtechRrmAPIfRecommendedMacAddr": qtechRrmAPIfRecommendedMacAddr,
       "qtechRrmAPIfRecommendedSlotId": qtechRrmAPIfRecommendedSlotId,
       "qtechRrmAPRadioTable": qtechRrmAPRadioTable,
       "qtechRrmAPRadioEntry": qtechRrmAPRadioEntry,
       "qtechRrmAPRadioID": qtechRrmAPRadioID,
       "qtechRrmAPRadioType": qtechRrmAPRadioType,
       "qtechRrmAPRealName": qtechRrmAPRealName,
       "qtechRrmAPMacAddr": qtechRrmAPMacAddr,
       "qtechRrmAPIfThroughputParametersTable": qtechRrmAPIfThroughputParametersTable,
       "qtechRrmAPIfThroughputParametersEntry": qtechRrmAPIfThroughputParametersEntry,
       "qtechRrmAPIfThroughputMacAddr": qtechRrmAPIfThroughputMacAddr,
       "qtechRrmAPIfThroughputSlotId": qtechRrmAPIfThroughputSlotId,
       "qtechRrmAPIfThroughputAPName": qtechRrmAPIfThroughputAPName,
       "qtechRrmAPIfThroughputRx": qtechRrmAPIfThroughputRx,
       "qtechRrmAPIfThroughputTx": qtechRrmAPIfThroughputTx,
       "qtechRrmAPIfThroughputTotal": qtechRrmAPIfThroughputTotal,
       "qtechRrmAPSnrBSSIDTable": qtechRrmAPSnrBSSIDTable,
       "qtechRrmAPSnrBSSIDEntry": qtechRrmAPSnrBSSIDEntry,
       "qtechRrmAPSnrBSSIDMacAddr": qtechRrmAPSnrBSSIDMacAddr,
       "qtechRrmAPSnrBSSIDSlotId": qtechRrmAPSnrBSSIDSlotId,
       "qtechRrmAPSnrBSSIDAPName": qtechRrmAPSnrBSSIDAPName,
       "qtechRrmAPSnrBSSIDAverageSignalStrength": qtechRrmAPSnrBSSIDAverageSignalStrength,
       "qtechRrmAPSnrBSSIDSignalPkts": qtechRrmAPSnrBSSIDSignalPkts,
       "qtechRrmAPSnrBSSIDHighestRxSignalStrength": qtechRrmAPSnrBSSIDHighestRxSignalStrength,
       "qtechRrmAPSnrBSSIDLowestRxSignalStrength": qtechRrmAPSnrBSSIDLowestRxSignalStrength,
       "qtechRrmAPSnrBSSIDSampleTime": qtechRrmAPSnrBSSIDSampleTime,
       "qtechRrmMIBTraps": qtechRrmMIBTraps,
       "qtechRrmTrapControl": qtechRrmTrapControl,
       "qtechRrmAPDot11bProfileTrapControlMask": qtechRrmAPDot11bProfileTrapControlMask,
       "qtechRrmAPDot11aProfileTrapControlMask": qtechRrmAPDot11aProfileTrapControlMask,
       "qtechRrmAPDot11bParamUpdateTrapControlMask": qtechRrmAPDot11bParamUpdateTrapControlMask,
       "qtechRrmAPDot11aParamUpdateTrapControlMask": qtechRrmAPDot11aParamUpdateTrapControlMask,
       "qtechRrmTrapVariable": qtechRrmTrapVariable,
       "qtechRrmAPMacAddrTrapVariable": qtechRrmAPMacAddrTrapVariable,
       "qtechRrmAPRadioIDTrapVariable": qtechRrmAPRadioIDTrapVariable,
       "qtechRrmAPRadioTypeTrapVariable": qtechRrmAPRadioTypeTrapVariable,
       "qtechRrmClientNumberTrapVariable": qtechRrmClientNumberTrapVariable,
       "qtechRrmForeignInterfereTrapVariable": qtechRrmForeignInterfereTrapVariable,
       "qtechRrmNoiseTrapVariable": qtechRrmNoiseTrapVariable,
       "qtechRrmThroughputTrapVariable": qtechRrmThroughputTrapVariable,
       "qtechRrmUtilizationTrapVariable": qtechRrmUtilizationTrapVariable,
       "qtechRrmAPTxPowerBeforeChange": qtechRrmAPTxPowerBeforeChange,
       "qtechRrmAPTxPowerAfterChange": qtechRrmAPTxPowerAfterChange,
       "qtechRrmAPChannelNumberBeforeChannge": qtechRrmAPChannelNumberBeforeChannge,
       "qtechRrmAPChannelNumberAfterChannge": qtechRrmAPChannelNumberAfterChannge,
       "qtechRrmDot11bGroupLeaderMacAddrTrapVariable": qtechRrmDot11bGroupLeaderMacAddrTrapVariable,
       "qtechRrmDot11aGroupLeaderMacAddrTrapVariable": qtechRrmDot11aGroupLeaderMacAddrTrapVariable,
       "qtechRrmAPChannelChangeReason": qtechRrmAPChannelChangeReason,
       "qtechRrmAPChannelChangeReasonValue": qtechRrmAPChannelChangeReasonValue,
       "qtechRrmAPTxPowerChangeCoverageFlag": qtechRrmAPTxPowerChangeCoverageFlag,
       "qtechRrmDFSFreeCount": qtechRrmDFSFreeCount,
       "qtechRrmAPChannelChangeCount": qtechRrmAPChannelChangeCount,
       "qtechRrmTraps": qtechRrmTraps,
       "qtechRrmAPClientNumProfileFailed": qtechRrmAPClientNumProfileFailed,
       "qtechRrmAPLoadProfileFailed": qtechRrmAPLoadProfileFailed,
       "qtechRrmAPNoiseProfileFailed": qtechRrmAPNoiseProfileFailed,
       "qtechRrmAPInterferenceProfileFailed": qtechRrmAPInterferenceProfileFailed,
       "qtechRrmAPPerformanceProfileFailed": qtechRrmAPPerformanceProfileFailed,
       "qtechRrmAPClientNumProfileUpdatedToPass": qtechRrmAPClientNumProfileUpdatedToPass,
       "qtechRrmAPLoadProfileUpdatedToPass": qtechRrmAPLoadProfileUpdatedToPass,
       "qtechRrmAPNoiseProfileUpdatedToPass": qtechRrmAPNoiseProfileUpdatedToPass,
       "qtechRrmAPInterferenceProfileUpdatedToPass": qtechRrmAPInterferenceProfileUpdatedToPass,
       "qtechRrmAPPerformanceProfileUpdatedToPass": qtechRrmAPPerformanceProfileUpdatedToPass,
       "qtechRrmAPCurrentTxPowerChanged": qtechRrmAPCurrentTxPowerChanged,
       "qtechRrmAPCurrentChannelChanged": qtechRrmAPCurrentChannelChanged,
       "qtechRrmDot11bGroupingDone": qtechRrmDot11bGroupingDone,
       "qtechRrmDot11aGroupingDone": qtechRrmDot11aGroupingDone,
       "qtechRrmDot11bDFSFreeCountBelowThreshold": qtechRrmDot11bDFSFreeCountBelowThreshold,
       "qtechRrmDot11aDFSFreeCountBelowThreshold": qtechRrmDot11aDFSFreeCountBelowThreshold,
       "qtechRrmNeighborAPInterference": qtechRrmNeighborAPInterference,
       "qtechRrmStationInterference": qtechRrmStationInterference,
       "qtechRrmOtherDiveceInterference": qtechRrmOtherDiveceInterference,
       "qtechRrmMIBConformance": qtechRrmMIBConformance,
       "qtechRrmMIBCompliances": qtechRrmMIBCompliances,
       "qtechRrmMIBCompliance": qtechRrmMIBCompliance,
       "qtechRrmMIBGroups": qtechRrmMIBGroups,
       "qtechRrmMIBGroup": qtechRrmMIBGroup,
       "qtechRrmTrapsGroup": qtechRrmTrapsGroup,
       "qtechRrmTrap": qtechRrmTrap}
)
