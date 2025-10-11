# SNMP MIB module (HM2-DUAL-RSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-DUAL-RSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:02 2025
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2DualRstpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 150)
)
if mibBuilder.loadTexts:
    hm2DualRstpMib.setRevisions(
        ("2019-03-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2DualRstpMibNotifications_ObjectIdentity = ObjectIdentity
hm2DualRstpMibNotifications = _Hm2DualRstpMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 0)
)
_Hm2DualRstpMibObjects_ObjectIdentity = ObjectIdentity
hm2DualRstpMibObjects = _Hm2DualRstpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1)
)
_Hm2DualRstpCstConfigGroup_ObjectIdentity = ObjectIdentity
hm2DualRstpCstConfigGroup = _Hm2DualRstpCstConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0)
)


class _Hm2DualRstpAdminMode_Type(HmEnabledStatus):
    """Custom type hm2DualRstpAdminMode based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DualRstpAdminMode_Type.__name__ = "HmEnabledStatus"
_Hm2DualRstpAdminMode_Object = MibScalar
hm2DualRstpAdminMode = _Hm2DualRstpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 1),
    _Hm2DualRstpAdminMode_Type()
)
hm2DualRstpAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpAdminMode.setStatus("current")
_Hm2DualRstpCstHelloTime_Type = Unsigned32
_Hm2DualRstpCstHelloTime_Object = MibScalar
hm2DualRstpCstHelloTime = _Hm2DualRstpCstHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 2),
    _Hm2DualRstpCstHelloTime_Type()
)
hm2DualRstpCstHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstHelloTime.setStatus("current")
_Hm2DualRstpCstMaxAge_Type = Unsigned32
_Hm2DualRstpCstMaxAge_Object = MibScalar
hm2DualRstpCstMaxAge = _Hm2DualRstpCstMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 3),
    _Hm2DualRstpCstMaxAge_Type()
)
hm2DualRstpCstMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstMaxAge.setStatus("current")


class _Hm2DualRstpCstRegionalRootId_Type(OctetString):
    """Custom type hm2DualRstpCstRegionalRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Hm2DualRstpCstRegionalRootId_Type.__name__ = "OctetString"
_Hm2DualRstpCstRegionalRootId_Object = MibScalar
hm2DualRstpCstRegionalRootId = _Hm2DualRstpCstRegionalRootId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 4),
    _Hm2DualRstpCstRegionalRootId_Type()
)
hm2DualRstpCstRegionalRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstRegionalRootId.setStatus("current")
_Hm2DualRstpCstRegionalRootPathCost_Type = Unsigned32
_Hm2DualRstpCstRegionalRootPathCost_Object = MibScalar
hm2DualRstpCstRegionalRootPathCost = _Hm2DualRstpCstRegionalRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 5),
    _Hm2DualRstpCstRegionalRootPathCost_Type()
)
hm2DualRstpCstRegionalRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstRegionalRootPathCost.setStatus("current")
_Hm2DualRstpCstRootFwdDelay_Type = Unsigned32
_Hm2DualRstpCstRootFwdDelay_Object = MibScalar
hm2DualRstpCstRootFwdDelay = _Hm2DualRstpCstRootFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 6),
    _Hm2DualRstpCstRootFwdDelay_Type()
)
hm2DualRstpCstRootFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstRootFwdDelay.setStatus("current")


class _Hm2DualRstpCstBridgeMaxAge_Type(Unsigned32):
    """Custom type hm2DualRstpCstBridgeMaxAge based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Hm2DualRstpCstBridgeMaxAge_Type.__name__ = "Unsigned32"
_Hm2DualRstpCstBridgeMaxAge_Object = MibScalar
hm2DualRstpCstBridgeMaxAge = _Hm2DualRstpCstBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 7),
    _Hm2DualRstpCstBridgeMaxAge_Type()
)
hm2DualRstpCstBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeMaxAge.setStatus("current")


class _Hm2DualRstpCstBridgeHelloTime_Type(Unsigned32):
    """Custom type hm2DualRstpCstBridgeHelloTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hm2DualRstpCstBridgeHelloTime_Type.__name__ = "Unsigned32"
_Hm2DualRstpCstBridgeHelloTime_Object = MibScalar
hm2DualRstpCstBridgeHelloTime = _Hm2DualRstpCstBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 8),
    _Hm2DualRstpCstBridgeHelloTime_Type()
)
hm2DualRstpCstBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeHelloTime.setStatus("current")
_Hm2DualRstpCstBridgeHoldTime_Type = Unsigned32
_Hm2DualRstpCstBridgeHoldTime_Object = MibScalar
hm2DualRstpCstBridgeHoldTime = _Hm2DualRstpCstBridgeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 9),
    _Hm2DualRstpCstBridgeHoldTime_Type()
)
hm2DualRstpCstBridgeHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeHoldTime.setStatus("current")


class _Hm2DualRstpCstBridgeFwdDelay_Type(Unsigned32):
    """Custom type hm2DualRstpCstBridgeFwdDelay based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Hm2DualRstpCstBridgeFwdDelay_Type.__name__ = "Unsigned32"
_Hm2DualRstpCstBridgeFwdDelay_Object = MibScalar
hm2DualRstpCstBridgeFwdDelay = _Hm2DualRstpCstBridgeFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 10),
    _Hm2DualRstpCstBridgeFwdDelay_Type()
)
hm2DualRstpCstBridgeFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeFwdDelay.setStatus("current")


class _Hm2DualRstpCstBridgeMaxHops_Type(Unsigned32):
    """Custom type hm2DualRstpCstBridgeMaxHops based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Hm2DualRstpCstBridgeMaxHops_Type.__name__ = "Unsigned32"
_Hm2DualRstpCstBridgeMaxHops_Object = MibScalar
hm2DualRstpCstBridgeMaxHops = _Hm2DualRstpCstBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 11),
    _Hm2DualRstpCstBridgeMaxHops_Type()
)
hm2DualRstpCstBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeMaxHops.setStatus("current")


class _Hm2DualRstpCstBridgePriority_Type(Unsigned32):
    """Custom type hm2DualRstpCstBridgePriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Hm2DualRstpCstBridgePriority_Type.__name__ = "Unsigned32"
_Hm2DualRstpCstBridgePriority_Object = MibScalar
hm2DualRstpCstBridgePriority = _Hm2DualRstpCstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 12),
    _Hm2DualRstpCstBridgePriority_Type()
)
hm2DualRstpCstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgePriority.setStatus("current")
_Hm2DualRstpCstBridgeTimeSinceTopologyChange_Type = TimeTicks
_Hm2DualRstpCstBridgeTimeSinceTopologyChange_Object = MibScalar
hm2DualRstpCstBridgeTimeSinceTopologyChange = _Hm2DualRstpCstBridgeTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 13),
    _Hm2DualRstpCstBridgeTimeSinceTopologyChange_Type()
)
hm2DualRstpCstBridgeTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeTimeSinceTopologyChange.setStatus("current")
_Hm2DualRstpCstBridgeTopChanges_Type = Counter32
_Hm2DualRstpCstBridgeTopChanges_Object = MibScalar
hm2DualRstpCstBridgeTopChanges = _Hm2DualRstpCstBridgeTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 14),
    _Hm2DualRstpCstBridgeTopChanges_Type()
)
hm2DualRstpCstBridgeTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeTopChanges.setStatus("current")


class _Hm2DualRstpCstBridgeTopologyChangeParm_Type(Integer32):
    """Custom type hm2DualRstpCstBridgeTopologyChangeParm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Hm2DualRstpCstBridgeTopologyChangeParm_Type.__name__ = "Integer32"
_Hm2DualRstpCstBridgeTopologyChangeParm_Object = MibScalar
hm2DualRstpCstBridgeTopologyChangeParm = _Hm2DualRstpCstBridgeTopologyChangeParm_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 15),
    _Hm2DualRstpCstBridgeTopologyChangeParm_Type()
)
hm2DualRstpCstBridgeTopologyChangeParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeTopologyChangeParm.setStatus("current")
_Hm2DualRstpCstBridgeRootCost_Type = Unsigned32
_Hm2DualRstpCstBridgeRootCost_Object = MibScalar
hm2DualRstpCstBridgeRootCost = _Hm2DualRstpCstBridgeRootCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 16),
    _Hm2DualRstpCstBridgeRootCost_Type()
)
hm2DualRstpCstBridgeRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeRootCost.setStatus("current")


class _Hm2DualRstpCstBridgeRootPort_Type(OctetString):
    """Custom type hm2DualRstpCstBridgeRootPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Hm2DualRstpCstBridgeRootPort_Type.__name__ = "OctetString"
_Hm2DualRstpCstBridgeRootPort_Object = MibScalar
hm2DualRstpCstBridgeRootPort = _Hm2DualRstpCstBridgeRootPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 17),
    _Hm2DualRstpCstBridgeRootPort_Type()
)
hm2DualRstpCstBridgeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeRootPort.setStatus("current")


class _Hm2DualRstpCstBridgeHoldCount_Type(Unsigned32):
    """Custom type hm2DualRstpCstBridgeHoldCount based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Hm2DualRstpCstBridgeHoldCount_Type.__name__ = "Unsigned32"
_Hm2DualRstpCstBridgeHoldCount_Object = MibScalar
hm2DualRstpCstBridgeHoldCount = _Hm2DualRstpCstBridgeHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 18),
    _Hm2DualRstpCstBridgeHoldCount_Type()
)
hm2DualRstpCstBridgeHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeHoldCount.setStatus("current")


class _Hm2DualRstpBpduGuardMode_Type(HmEnabledStatus):
    """Custom type hm2DualRstpBpduGuardMode based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DualRstpBpduGuardMode_Type.__name__ = "HmEnabledStatus"
_Hm2DualRstpBpduGuardMode_Object = MibScalar
hm2DualRstpBpduGuardMode = _Hm2DualRstpBpduGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 19),
    _Hm2DualRstpBpduGuardMode_Type()
)
hm2DualRstpBpduGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpBpduGuardMode.setStatus("current")


class _Hm2DualRstpBpduFilterDefault_Type(HmEnabledStatus):
    """Custom type hm2DualRstpBpduFilterDefault based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DualRstpBpduFilterDefault_Type.__name__ = "HmEnabledStatus"
_Hm2DualRstpBpduFilterDefault_Object = MibScalar
hm2DualRstpBpduFilterDefault = _Hm2DualRstpBpduFilterDefault_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 20),
    _Hm2DualRstpBpduFilterDefault_Type()
)
hm2DualRstpBpduFilterDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpBpduFilterDefault.setStatus("current")


class _Hm2DualRstpBridgeIdentifier_Type(OctetString):
    """Custom type hm2DualRstpBridgeIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Hm2DualRstpBridgeIdentifier_Type.__name__ = "OctetString"
_Hm2DualRstpBridgeIdentifier_Object = MibScalar
hm2DualRstpBridgeIdentifier = _Hm2DualRstpBridgeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 21),
    _Hm2DualRstpBridgeIdentifier_Type()
)
hm2DualRstpBridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpBridgeIdentifier.setStatus("current")


class _Hm2DualRstpCstBridgeDesignatedRoot_Type(OctetString):
    """Custom type hm2DualRstpCstBridgeDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Hm2DualRstpCstBridgeDesignatedRoot_Type.__name__ = "OctetString"
_Hm2DualRstpCstBridgeDesignatedRoot_Object = MibScalar
hm2DualRstpCstBridgeDesignatedRoot = _Hm2DualRstpCstBridgeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 22),
    _Hm2DualRstpCstBridgeDesignatedRoot_Type()
)
hm2DualRstpCstBridgeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstBridgeDesignatedRoot.setStatus("current")


class _Hm2DualRstpRingOnlyMode_Type(HmEnabledStatus):
    """Custom type hm2DualRstpRingOnlyMode based on HmEnabledStatus"""
    defaultValue = 2


_Hm2DualRstpRingOnlyMode_Type.__name__ = "HmEnabledStatus"
_Hm2DualRstpRingOnlyMode_Object = MibScalar
hm2DualRstpRingOnlyMode = _Hm2DualRstpRingOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 23),
    _Hm2DualRstpRingOnlyMode_Type()
)
hm2DualRstpRingOnlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpRingOnlyMode.setStatus("current")


class _Hm2DualRstpRingOnlyModeIntfOne_Type(InterfaceIndexOrZero):
    """Custom type hm2DualRstpRingOnlyModeIntfOne based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2DualRstpRingOnlyModeIntfOne_Type.__name__ = "InterfaceIndexOrZero"
_Hm2DualRstpRingOnlyModeIntfOne_Object = MibScalar
hm2DualRstpRingOnlyModeIntfOne = _Hm2DualRstpRingOnlyModeIntfOne_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 24),
    _Hm2DualRstpRingOnlyModeIntfOne_Type()
)
hm2DualRstpRingOnlyModeIntfOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpRingOnlyModeIntfOne.setStatus("current")


class _Hm2DualRstpRingOnlyModeIntfTwo_Type(InterfaceIndexOrZero):
    """Custom type hm2DualRstpRingOnlyModeIntfTwo based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2DualRstpRingOnlyModeIntfTwo_Type.__name__ = "InterfaceIndexOrZero"
_Hm2DualRstpRingOnlyModeIntfTwo_Object = MibScalar
hm2DualRstpRingOnlyModeIntfTwo = _Hm2DualRstpRingOnlyModeIntfTwo_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 25),
    _Hm2DualRstpRingOnlyModeIntfTwo_Type()
)
hm2DualRstpRingOnlyModeIntfTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpRingOnlyModeIntfTwo.setStatus("current")


class _Hm2DualRstpTrapMode_Type(HmEnabledStatus):
    """Custom type hm2DualRstpTrapMode based on HmEnabledStatus"""
    defaultValue = 1


_Hm2DualRstpTrapMode_Type.__name__ = "HmEnabledStatus"
_Hm2DualRstpTrapMode_Object = MibScalar
hm2DualRstpTrapMode = _Hm2DualRstpTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 26),
    _Hm2DualRstpTrapMode_Type()
)
hm2DualRstpTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DualRstpTrapMode.setStatus("current")


class _Hm2DualRstpMstId_Type(Unsigned32):
    """Custom type hm2DualRstpMstId based on Unsigned32"""
    defaultValue = 0


_Hm2DualRstpMstId_Type.__name__ = "Unsigned32"
_Hm2DualRstpMstId_Object = MibScalar
hm2DualRstpMstId = _Hm2DualRstpMstId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 0, 27),
    _Hm2DualRstpMstId_Type()
)
hm2DualRstpMstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpMstId.setStatus("current")
_Hm2DualRstpCstPortConfigGroup_ObjectIdentity = ObjectIdentity
hm2DualRstpCstPortConfigGroup = _Hm2DualRstpCstPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 1)
)
_Hm2DualRstpCstPortTable_Object = MibTable
hm2DualRstpCstPortTable = _Hm2DualRstpCstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hm2DualRstpCstPortTable.setStatus("current")
_Hm2DualRstpCstPortEntry_Object = MibTableRow
hm2DualRstpCstPortEntry = _Hm2DualRstpCstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 1, 1, 1)
)
hm2DualRstpCstPortEntry.setIndexNames(
    (0, "HM2-DUAL-RSTP-MIB", "hm2DualRstpMstId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2DualRstpCstPortEntry.setStatus("current")


class _Hm2DualRstpCstPortDrstpInstance_Type(Integer32):
    """Custom type hm2DualRstpCstPortDrstpInstance based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Hm2DualRstpCstPortDrstpInstance_Type.__name__ = "Integer32"
_Hm2DualRstpCstPortDrstpInstance_Object = MibTableColumn
hm2DualRstpCstPortDrstpInstance = _Hm2DualRstpCstPortDrstpInstance_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 150, 1, 1, 1, 1, 1),
    _Hm2DualRstpCstPortDrstpInstance_Type()
)
hm2DualRstpCstPortDrstpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DualRstpCstPortDrstpInstance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-DUAL-RSTP-MIB",
    **{"hm2DualRstpMib": hm2DualRstpMib,
       "hm2DualRstpMibNotifications": hm2DualRstpMibNotifications,
       "hm2DualRstpMibObjects": hm2DualRstpMibObjects,
       "hm2DualRstpCstConfigGroup": hm2DualRstpCstConfigGroup,
       "hm2DualRstpAdminMode": hm2DualRstpAdminMode,
       "hm2DualRstpCstHelloTime": hm2DualRstpCstHelloTime,
       "hm2DualRstpCstMaxAge": hm2DualRstpCstMaxAge,
       "hm2DualRstpCstRegionalRootId": hm2DualRstpCstRegionalRootId,
       "hm2DualRstpCstRegionalRootPathCost": hm2DualRstpCstRegionalRootPathCost,
       "hm2DualRstpCstRootFwdDelay": hm2DualRstpCstRootFwdDelay,
       "hm2DualRstpCstBridgeMaxAge": hm2DualRstpCstBridgeMaxAge,
       "hm2DualRstpCstBridgeHelloTime": hm2DualRstpCstBridgeHelloTime,
       "hm2DualRstpCstBridgeHoldTime": hm2DualRstpCstBridgeHoldTime,
       "hm2DualRstpCstBridgeFwdDelay": hm2DualRstpCstBridgeFwdDelay,
       "hm2DualRstpCstBridgeMaxHops": hm2DualRstpCstBridgeMaxHops,
       "hm2DualRstpCstBridgePriority": hm2DualRstpCstBridgePriority,
       "hm2DualRstpCstBridgeTimeSinceTopologyChange": hm2DualRstpCstBridgeTimeSinceTopologyChange,
       "hm2DualRstpCstBridgeTopChanges": hm2DualRstpCstBridgeTopChanges,
       "hm2DualRstpCstBridgeTopologyChangeParm": hm2DualRstpCstBridgeTopologyChangeParm,
       "hm2DualRstpCstBridgeRootCost": hm2DualRstpCstBridgeRootCost,
       "hm2DualRstpCstBridgeRootPort": hm2DualRstpCstBridgeRootPort,
       "hm2DualRstpCstBridgeHoldCount": hm2DualRstpCstBridgeHoldCount,
       "hm2DualRstpBpduGuardMode": hm2DualRstpBpduGuardMode,
       "hm2DualRstpBpduFilterDefault": hm2DualRstpBpduFilterDefault,
       "hm2DualRstpBridgeIdentifier": hm2DualRstpBridgeIdentifier,
       "hm2DualRstpCstBridgeDesignatedRoot": hm2DualRstpCstBridgeDesignatedRoot,
       "hm2DualRstpRingOnlyMode": hm2DualRstpRingOnlyMode,
       "hm2DualRstpRingOnlyModeIntfOne": hm2DualRstpRingOnlyModeIntfOne,
       "hm2DualRstpRingOnlyModeIntfTwo": hm2DualRstpRingOnlyModeIntfTwo,
       "hm2DualRstpTrapMode": hm2DualRstpTrapMode,
       "hm2DualRstpMstId": hm2DualRstpMstId,
       "hm2DualRstpCstPortConfigGroup": hm2DualRstpCstPortConfigGroup,
       "hm2DualRstpCstPortTable": hm2DualRstpCstPortTable,
       "hm2DualRstpCstPortEntry": hm2DualRstpCstPortEntry,
       "hm2DualRstpCstPortDrstpInstance": hm2DualRstpCstPortDrstpInstance}
)
