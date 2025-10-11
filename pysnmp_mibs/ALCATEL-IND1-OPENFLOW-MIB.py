# SNMP MIB module (ALCATEL-IND1-OPENFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel/ALCATEL-IND1-OPENFLOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:08:58 2025
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

(softentIND1OpenflowMIB,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1OpenflowMIB")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

alcatelIND1OpenflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIB.setRevisions(
        ("2013-11-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1OpenflowMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBNotifications = _AlcatelIND1OpenflowMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 0)
)
_AlcatelIND1OpenflowMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBObjects = _AlcatelIND1OpenflowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIBObjects.setStatus("current")
_AlaOpenflowGlobalConfigObjects_ObjectIdentity = ObjectIdentity
alaOpenflowGlobalConfigObjects = _AlaOpenflowGlobalConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 1)
)


class _AlaOpenflowGlobalBackoffMax_Type(Integer32):
    """Custom type alaOpenflowGlobalBackoffMax based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AlaOpenflowGlobalBackoffMax_Type.__name__ = "Integer32"
_AlaOpenflowGlobalBackoffMax_Object = MibScalar
alaOpenflowGlobalBackoffMax = _AlaOpenflowGlobalBackoffMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 1, 1),
    _AlaOpenflowGlobalBackoffMax_Type()
)
alaOpenflowGlobalBackoffMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOpenflowGlobalBackoffMax.setStatus("current")


class _AlaOpenflowGlobalIdleProbeTimeout_Type(Integer32):
    """Custom type alaOpenflowGlobalIdleProbeTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AlaOpenflowGlobalIdleProbeTimeout_Type.__name__ = "Integer32"
_AlaOpenflowGlobalIdleProbeTimeout_Object = MibScalar
alaOpenflowGlobalIdleProbeTimeout = _AlaOpenflowGlobalIdleProbeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 1, 2),
    _AlaOpenflowGlobalIdleProbeTimeout_Type()
)
alaOpenflowGlobalIdleProbeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOpenflowGlobalIdleProbeTimeout.setStatus("current")
_AlaOpenflowLogicalSwitchTable_Object = MibTable
alaOpenflowLogicalSwitchTable = _AlaOpenflowLogicalSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchTable.setStatus("current")
_AlaOpenflowLogicalSwitchEntry_Object = MibTableRow
alaOpenflowLogicalSwitchEntry = _AlaOpenflowLogicalSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1)
)
alaOpenflowLogicalSwitchEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitch"),
)
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchEntry.setStatus("current")


class _AlaOpenflowLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowLogicalSwitch_Object = MibTableColumn
alaOpenflowLogicalSwitch = _AlaOpenflowLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 1),
    _AlaOpenflowLogicalSwitch_Type()
)
alaOpenflowLogicalSwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitch.setStatus("current")


class _AlaOpenflowLogicalSwitchAdminState_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchAdminState based on Integer32"""
    defaultValue = 1

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


_AlaOpenflowLogicalSwitchAdminState_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchAdminState_Object = MibTableColumn
alaOpenflowLogicalSwitchAdminState = _AlaOpenflowLogicalSwitchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 2),
    _AlaOpenflowLogicalSwitchAdminState_Type()
)
alaOpenflowLogicalSwitchAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchAdminState.setStatus("current")


class _AlaOpenflowLogicalSwitchMode_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("api", 2))
    )


_AlaOpenflowLogicalSwitchMode_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchMode_Object = MibTableColumn
alaOpenflowLogicalSwitchMode = _AlaOpenflowLogicalSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 3),
    _AlaOpenflowLogicalSwitchMode_Type()
)
alaOpenflowLogicalSwitchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchMode.setStatus("current")


class _AlaOpenflowLogicalSwitchVersions_Type(Bits):
    """Custom type alaOpenflowLogicalSwitchVersions based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("v1dot0", 0),
          ("v1dot3dot1", 1))
    )

_AlaOpenflowLogicalSwitchVersions_Type.__name__ = "Bits"
_AlaOpenflowLogicalSwitchVersions_Object = MibTableColumn
alaOpenflowLogicalSwitchVersions = _AlaOpenflowLogicalSwitchVersions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 4),
    _AlaOpenflowLogicalSwitchVersions_Type()
)
alaOpenflowLogicalSwitchVersions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchVersions.setStatus("current")


class _AlaOpenflowLogicalSwitchVlan_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4093),
    )


_AlaOpenflowLogicalSwitchVlan_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchVlan_Object = MibTableColumn
alaOpenflowLogicalSwitchVlan = _AlaOpenflowLogicalSwitchVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 5),
    _AlaOpenflowLogicalSwitchVlan_Type()
)
alaOpenflowLogicalSwitchVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchVlan.setStatus("current")


class _AlaOpenflowLogicalSwitchControllerCount_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchControllerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaOpenflowLogicalSwitchControllerCount_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchControllerCount_Object = MibTableColumn
alaOpenflowLogicalSwitchControllerCount = _AlaOpenflowLogicalSwitchControllerCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 6),
    _AlaOpenflowLogicalSwitchControllerCount_Type()
)
alaOpenflowLogicalSwitchControllerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchControllerCount.setStatus("current")


class _AlaOpenflowLogicalSwitchInterfaceCount_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchInterfaceCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AlaOpenflowLogicalSwitchInterfaceCount_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchInterfaceCount_Object = MibTableColumn
alaOpenflowLogicalSwitchInterfaceCount = _AlaOpenflowLogicalSwitchInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 7),
    _AlaOpenflowLogicalSwitchInterfaceCount_Type()
)
alaOpenflowLogicalSwitchInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchInterfaceCount.setStatus("current")


class _AlaOpenflowLogicalSwitchFlowCount_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchFlowCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AlaOpenflowLogicalSwitchFlowCount_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchFlowCount_Object = MibTableColumn
alaOpenflowLogicalSwitchFlowCount = _AlaOpenflowLogicalSwitchFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 8),
    _AlaOpenflowLogicalSwitchFlowCount_Type()
)
alaOpenflowLogicalSwitchFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchFlowCount.setStatus("current")
_AlaOpenflowLogicalSwitchRowStatus_Type = RowStatus
_AlaOpenflowLogicalSwitchRowStatus_Object = MibTableColumn
alaOpenflowLogicalSwitchRowStatus = _AlaOpenflowLogicalSwitchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 9),
    _AlaOpenflowLogicalSwitchRowStatus_Type()
)
alaOpenflowLogicalSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchRowStatus.setStatus("current")
_AlaOpenflowControllerTable_Object = MibTable
alaOpenflowControllerTable = _AlaOpenflowControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaOpenflowControllerTable.setStatus("current")
_AlaOpenflowControllerEntry_Object = MibTableRow
alaOpenflowControllerEntry = _AlaOpenflowControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1)
)
alaOpenflowControllerEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerLogicalSwitch"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerIpType"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerIp"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerPort"),
)
if mibBuilder.loadTexts:
    alaOpenflowControllerEntry.setStatus("current")


class _AlaOpenflowControllerLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowControllerLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowControllerLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowControllerLogicalSwitch_Object = MibTableColumn
alaOpenflowControllerLogicalSwitch = _AlaOpenflowControllerLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 1),
    _AlaOpenflowControllerLogicalSwitch_Type()
)
alaOpenflowControllerLogicalSwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowControllerLogicalSwitch.setStatus("current")


class _AlaOpenflowControllerIpType_Type(InetAddressType):
    """Custom type alaOpenflowControllerIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaOpenflowControllerIpType_Type.__name__ = "InetAddressType"
_AlaOpenflowControllerIpType_Object = MibTableColumn
alaOpenflowControllerIpType = _AlaOpenflowControllerIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 2),
    _AlaOpenflowControllerIpType_Type()
)
alaOpenflowControllerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowControllerIpType.setStatus("current")


class _AlaOpenflowControllerIp_Type(InetAddress):
    """Custom type alaOpenflowControllerIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaOpenflowControllerIp_Type.__name__ = "InetAddress"
_AlaOpenflowControllerIp_Object = MibTableColumn
alaOpenflowControllerIp = _AlaOpenflowControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 3),
    _AlaOpenflowControllerIp_Type()
)
alaOpenflowControllerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowControllerIp.setStatus("current")


class _AlaOpenflowControllerPort_Type(Integer32):
    """Custom type alaOpenflowControllerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaOpenflowControllerPort_Type.__name__ = "Integer32"
_AlaOpenflowControllerPort_Object = MibTableColumn
alaOpenflowControllerPort = _AlaOpenflowControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 4),
    _AlaOpenflowControllerPort_Type()
)
alaOpenflowControllerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowControllerPort.setStatus("current")


class _AlaOpenflowControllerRole_Type(Integer32):
    """Custom type alaOpenflowControllerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("master", 2),
          ("slave", 3))
    )


_AlaOpenflowControllerRole_Type.__name__ = "Integer32"
_AlaOpenflowControllerRole_Object = MibTableColumn
alaOpenflowControllerRole = _AlaOpenflowControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 5),
    _AlaOpenflowControllerRole_Type()
)
alaOpenflowControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowControllerRole.setStatus("current")


class _AlaOpenflowControllerAdminState_Type(Integer32):
    """Custom type alaOpenflowControllerAdminState based on Integer32"""
    defaultValue = 1

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


_AlaOpenflowControllerAdminState_Type.__name__ = "Integer32"
_AlaOpenflowControllerAdminState_Object = MibTableColumn
alaOpenflowControllerAdminState = _AlaOpenflowControllerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 6),
    _AlaOpenflowControllerAdminState_Type()
)
alaOpenflowControllerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowControllerAdminState.setStatus("current")


class _AlaOpenflowControllerOperState_Type(Integer32):
    """Custom type alaOpenflowControllerOperState based on Integer32"""
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
        *(("invalid", 1),
          ("disabled", 2),
          ("sendError", 3),
          ("init", 4),
          ("connecting", 5),
          ("backoff", 6),
          ("exchangingHello", 7),
          ("active", 8),
          ("idle", 9),
          ("disconnected", 10))
    )


_AlaOpenflowControllerOperState_Type.__name__ = "Integer32"
_AlaOpenflowControllerOperState_Object = MibTableColumn
alaOpenflowControllerOperState = _AlaOpenflowControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 7),
    _AlaOpenflowControllerOperState_Type()
)
alaOpenflowControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowControllerOperState.setStatus("current")
_AlaOpenflowControllerRowStatus_Type = RowStatus
_AlaOpenflowControllerRowStatus_Object = MibTableColumn
alaOpenflowControllerRowStatus = _AlaOpenflowControllerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 8),
    _AlaOpenflowControllerRowStatus_Type()
)
alaOpenflowControllerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowControllerRowStatus.setStatus("current")
_AlaOpenflowInterfaceTable_Object = MibTable
alaOpenflowInterfaceTable = _AlaOpenflowInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaOpenflowInterfaceTable.setStatus("current")
_AlaOpenflowInterfaceEntry_Object = MibTableRow
alaOpenflowInterfaceEntry = _AlaOpenflowInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1)
)
alaOpenflowInterfaceEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceLogicalSwitch"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterface"),
)
if mibBuilder.loadTexts:
    alaOpenflowInterfaceEntry.setStatus("current")


class _AlaOpenflowInterfaceLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowInterfaceLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowInterfaceLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowInterfaceLogicalSwitch_Object = MibTableColumn
alaOpenflowInterfaceLogicalSwitch = _AlaOpenflowInterfaceLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 1),
    _AlaOpenflowInterfaceLogicalSwitch_Type()
)
alaOpenflowInterfaceLogicalSwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceLogicalSwitch.setStatus("current")


class _AlaOpenflowInterface_Type(Integer32):
    """Custom type alaOpenflowInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaOpenflowInterface_Type.__name__ = "Integer32"
_AlaOpenflowInterface_Object = MibTableColumn
alaOpenflowInterface = _AlaOpenflowInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 2),
    _AlaOpenflowInterface_Type()
)
alaOpenflowInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowInterface.setStatus("current")


class _AlaOpenflowInterfaceMode_Type(Integer32):
    """Custom type alaOpenflowInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("api", 2))
    )


_AlaOpenflowInterfaceMode_Type.__name__ = "Integer32"
_AlaOpenflowInterfaceMode_Object = MibTableColumn
alaOpenflowInterfaceMode = _AlaOpenflowInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 3),
    _AlaOpenflowInterfaceMode_Type()
)
alaOpenflowInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceMode.setStatus("current")
_AlaOpenflowInterfaceRowStatus_Type = RowStatus
_AlaOpenflowInterfaceRowStatus_Object = MibTableColumn
alaOpenflowInterfaceRowStatus = _AlaOpenflowInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 4),
    _AlaOpenflowInterfaceRowStatus_Type()
)
alaOpenflowInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceRowStatus.setStatus("current")
_AlaOpenflowFlowStatsTable_Object = MibTable
alaOpenflowFlowStatsTable = _AlaOpenflowFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaOpenflowFlowStatsTable.setStatus("current")
_AlaOpenflowFlowStatsEntry_Object = MibTableRow
alaOpenflowFlowStatsEntry = _AlaOpenflowFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 5, 1)
)
alaOpenflowFlowStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowFlowStatsLogicalSwitch"),
)
if mibBuilder.loadTexts:
    alaOpenflowFlowStatsEntry.setStatus("current")


class _AlaOpenflowFlowStatsLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowFlowStatsLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowFlowStatsLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowFlowStatsLogicalSwitch_Object = MibTableColumn
alaOpenflowFlowStatsLogicalSwitch = _AlaOpenflowFlowStatsLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 5, 1, 1),
    _AlaOpenflowFlowStatsLogicalSwitch_Type()
)
alaOpenflowFlowStatsLogicalSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowFlowStatsLogicalSwitch.setStatus("current")


class _AlaOpenflowFlowStatsExactCount_Type(Integer32):
    """Custom type alaOpenflowFlowStatsExactCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_AlaOpenflowFlowStatsExactCount_Type.__name__ = "Integer32"
_AlaOpenflowFlowStatsExactCount_Object = MibTableColumn
alaOpenflowFlowStatsExactCount = _AlaOpenflowFlowStatsExactCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 5, 1, 2),
    _AlaOpenflowFlowStatsExactCount_Type()
)
alaOpenflowFlowStatsExactCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowFlowStatsExactCount.setStatus("current")


class _AlaOpenflowFlowStatsWildCount_Type(Integer32):
    """Custom type alaOpenflowFlowStatsWildCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_AlaOpenflowFlowStatsWildCount_Type.__name__ = "Integer32"
_AlaOpenflowFlowStatsWildCount_Object = MibTableColumn
alaOpenflowFlowStatsWildCount = _AlaOpenflowFlowStatsWildCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 5, 1, 3),
    _AlaOpenflowFlowStatsWildCount_Type()
)
alaOpenflowFlowStatsWildCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowFlowStatsWildCount.setStatus("current")
_AlaOpenflowFlowEntryStatsTable_Object = MibTable
alaOpenflowFlowEntryStatsTable = _AlaOpenflowFlowEntryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaOpenflowFlowEntryStatsTable.setStatus("current")
_AlaOpenflowFlowEntryStatsEntry_Object = MibTableRow
alaOpenflowFlowEntryStatsEntry = _AlaOpenflowFlowEntryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 6, 1)
)
alaOpenflowFlowEntryStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowFlowEntryStatsLogicalSwitch"),
)
if mibBuilder.loadTexts:
    alaOpenflowFlowEntryStatsEntry.setStatus("current")


class _AlaOpenflowFlowEntryStatsLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowFlowEntryStatsLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowFlowEntryStatsLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowFlowEntryStatsLogicalSwitch_Object = MibTableColumn
alaOpenflowFlowEntryStatsLogicalSwitch = _AlaOpenflowFlowEntryStatsLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 6, 1, 1),
    _AlaOpenflowFlowEntryStatsLogicalSwitch_Type()
)
alaOpenflowFlowEntryStatsLogicalSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowFlowEntryStatsLogicalSwitch.setStatus("current")


class _AlaOpenflowFlowEntryStatsFlowId_Type(Integer32):
    """Custom type alaOpenflowFlowEntryStatsFlowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_AlaOpenflowFlowEntryStatsFlowId_Type.__name__ = "Integer32"
_AlaOpenflowFlowEntryStatsFlowId_Object = MibTableColumn
alaOpenflowFlowEntryStatsFlowId = _AlaOpenflowFlowEntryStatsFlowId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 6, 1, 2),
    _AlaOpenflowFlowEntryStatsFlowId_Type()
)
alaOpenflowFlowEntryStatsFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowFlowEntryStatsFlowId.setStatus("current")
_AlaOpenflowFlowEntryStatsRcvdPcks_Type = Counter32
_AlaOpenflowFlowEntryStatsRcvdPcks_Object = MibTableColumn
alaOpenflowFlowEntryStatsRcvdPcks = _AlaOpenflowFlowEntryStatsRcvdPcks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 6, 1, 3),
    _AlaOpenflowFlowEntryStatsRcvdPcks_Type()
)
alaOpenflowFlowEntryStatsRcvdPcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowFlowEntryStatsRcvdPcks.setStatus("current")
_AlaOpenflowFlowEntryStatsRcvdbytes_Type = Counter32
_AlaOpenflowFlowEntryStatsRcvdbytes_Object = MibTableColumn
alaOpenflowFlowEntryStatsRcvdbytes = _AlaOpenflowFlowEntryStatsRcvdbytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 6, 1, 4),
    _AlaOpenflowFlowEntryStatsRcvdbytes_Type()
)
alaOpenflowFlowEntryStatsRcvdbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowFlowEntryStatsRcvdbytes.setStatus("current")
_AlaOpenflowFlowEntryStatsDuration_Type = TimeStamp
_AlaOpenflowFlowEntryStatsDuration_Object = MibTableColumn
alaOpenflowFlowEntryStatsDuration = _AlaOpenflowFlowEntryStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 6, 1, 5),
    _AlaOpenflowFlowEntryStatsDuration_Type()
)
alaOpenflowFlowEntryStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowFlowEntryStatsDuration.setStatus("current")
_AlaOpenflowPortStatsTable_Object = MibTable
alaOpenflowPortStatsTable = _AlaOpenflowPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaOpenflowPortStatsTable.setStatus("current")
_AlaOpenflowPortStatsEntry_Object = MibTableRow
alaOpenflowPortStatsEntry = _AlaOpenflowPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 7, 1)
)
alaOpenflowPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowPortStatsLogicalSwitch"),
)
if mibBuilder.loadTexts:
    alaOpenflowPortStatsEntry.setStatus("current")


class _AlaOpenflowPortStatsLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowPortStatsLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowPortStatsLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowPortStatsLogicalSwitch_Object = MibTableColumn
alaOpenflowPortStatsLogicalSwitch = _AlaOpenflowPortStatsLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 7, 1, 1),
    _AlaOpenflowPortStatsLogicalSwitch_Type()
)
alaOpenflowPortStatsLogicalSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowPortStatsLogicalSwitch.setStatus("current")


class _AlaOpenflowPortStatsSlotNumber_Type(Integer32):
    """Custom type alaOpenflowPortStatsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaOpenflowPortStatsSlotNumber_Type.__name__ = "Integer32"
_AlaOpenflowPortStatsSlotNumber_Object = MibTableColumn
alaOpenflowPortStatsSlotNumber = _AlaOpenflowPortStatsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 7, 1, 2),
    _AlaOpenflowPortStatsSlotNumber_Type()
)
alaOpenflowPortStatsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowPortStatsSlotNumber.setStatus("current")


class _AlaOpenflowPortStatsPortNumber_Type(Integer32):
    """Custom type alaOpenflowPortStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaOpenflowPortStatsPortNumber_Type.__name__ = "Integer32"
_AlaOpenflowPortStatsPortNumber_Object = MibTableColumn
alaOpenflowPortStatsPortNumber = _AlaOpenflowPortStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 7, 1, 3),
    _AlaOpenflowPortStatsPortNumber_Type()
)
alaOpenflowPortStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowPortStatsPortNumber.setStatus("current")
_AlaOpenflowPortStatsTransPcks_Type = Counter32
_AlaOpenflowPortStatsTransPcks_Object = MibTableColumn
alaOpenflowPortStatsTransPcks = _AlaOpenflowPortStatsTransPcks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 7, 1, 4),
    _AlaOpenflowPortStatsTransPcks_Type()
)
alaOpenflowPortStatsTransPcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowPortStatsTransPcks.setStatus("current")
_AlaOpenflowPortStatsRcvdPcks_Type = Counter32
_AlaOpenflowPortStatsRcvdPcks_Object = MibTableColumn
alaOpenflowPortStatsRcvdPcks = _AlaOpenflowPortStatsRcvdPcks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 7, 1, 5),
    _AlaOpenflowPortStatsRcvdPcks_Type()
)
alaOpenflowPortStatsRcvdPcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowPortStatsRcvdPcks.setStatus("current")
_AlaOpenflowPortStatsDuration_Type = TimeStamp
_AlaOpenflowPortStatsDuration_Object = MibTableColumn
alaOpenflowPortStatsDuration = _AlaOpenflowPortStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 7, 1, 6),
    _AlaOpenflowPortStatsDuration_Type()
)
alaOpenflowPortStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowPortStatsDuration.setStatus("current")
_AlaOpenflowGroupStatsTable_Object = MibTable
alaOpenflowGroupStatsTable = _AlaOpenflowGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaOpenflowGroupStatsTable.setStatus("current")
_AlaOpenflowGroupStatsEntry_Object = MibTableRow
alaOpenflowGroupStatsEntry = _AlaOpenflowGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 8, 1)
)
alaOpenflowGroupStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowGroupStatsLogicalSwitch"),
)
if mibBuilder.loadTexts:
    alaOpenflowGroupStatsEntry.setStatus("current")


class _AlaOpenflowGroupStatsLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowGroupStatsLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowGroupStatsLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowGroupStatsLogicalSwitch_Object = MibTableColumn
alaOpenflowGroupStatsLogicalSwitch = _AlaOpenflowGroupStatsLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 8, 1, 1),
    _AlaOpenflowGroupStatsLogicalSwitch_Type()
)
alaOpenflowGroupStatsLogicalSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowGroupStatsLogicalSwitch.setStatus("current")


class _AlaOpenflowGroupStatsId_Type(Integer32):
    """Custom type alaOpenflowGroupStatsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_AlaOpenflowGroupStatsId_Type.__name__ = "Integer32"
_AlaOpenflowGroupStatsId_Object = MibTableColumn
alaOpenflowGroupStatsId = _AlaOpenflowGroupStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 8, 1, 2),
    _AlaOpenflowGroupStatsId_Type()
)
alaOpenflowGroupStatsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowGroupStatsId.setStatus("current")
_AlaOpenflowGroupStatsDuration_Type = TimeStamp
_AlaOpenflowGroupStatsDuration_Object = MibTableColumn
alaOpenflowGroupStatsDuration = _AlaOpenflowGroupStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 8, 1, 3),
    _AlaOpenflowGroupStatsDuration_Type()
)
alaOpenflowGroupStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowGroupStatsDuration.setStatus("current")
_AlcatelIND1OpenflowMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBConformance = _AlcatelIND1OpenflowMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIBConformance.setStatus("current")
_AlcatelIND1OpenflowMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBGroups = _AlcatelIND1OpenflowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIBGroups.setStatus("current")
_AlcatelIND1OpenflowMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBCompliances = _AlcatelIND1OpenflowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIBCompliances.setStatus("current")

# Managed Objects groups

alaOpenflowModuleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 1)
)
alaOpenflowModuleConfigGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowGlobalBackoffMax"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowGlobalIdleProbeTimeout"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleConfigGroup.setStatus("current")

alaOpenflowModuleLogicalSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 2)
)
alaOpenflowModuleLogicalSwitchGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchAdminState"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchMode"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchVersions"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchVlan"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchControllerCount"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchInterfaceCount"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchFlowCount"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchRowStatus"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleLogicalSwitchGroup.setStatus("current")

alaOpenflowModuleControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 3)
)
alaOpenflowModuleControllerGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerRole"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerAdminState"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerOperState"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerRowStatus"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleControllerGroup.setStatus("current")

alaOpenflowModuleInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 4)
)
alaOpenflowModuleInterfaceGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceMode"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleInterfaceGroup.setStatus("current")

alaOpenflowModuleFlowStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 5)
)
alaOpenflowModuleFlowStatsGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowFlowStatsExactCount"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowFlowStatsWildCount"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleFlowStatsGroup.setStatus("current")

alaOpenflowModuleFlowEntryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 6)
)
alaOpenflowModuleFlowEntryStatsGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowFlowEntryStatsFlowId"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowFlowEntryStatsRcvdPcks"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowFlowEntryStatsRcvdbytes"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowFlowEntryStatsDuration"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleFlowEntryStatsGroup.setStatus("current")

alaOpenflowModulePortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 7)
)
alaOpenflowModulePortStatsGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowPortStatsSlotNumber"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowPortStatsPortNumber"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowPortStatsTransPcks"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowPortStatsRcvdPcks"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowPortStatsDuration"))
)
if mibBuilder.loadTexts:
    alaOpenflowModulePortStatsGroup.setStatus("current")

alaOpenflowModuleGroupStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 8)
)
alaOpenflowModuleGroupStatsGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowGroupStatsId"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowGroupStatsDuration"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleGroupStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaOpenflowMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 2, 1)
)
alaOpenflowMIBCompliance.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleConfigGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleLogicalSwitchGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleControllerGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleInterfaceGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleFlowStatsGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleFlowEntryStatsGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModulePortStatsGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleGroupStatsGroup"))
)
if mibBuilder.loadTexts:
    alaOpenflowMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-OPENFLOW-MIB",
    **{"alcatelIND1OpenflowMIB": alcatelIND1OpenflowMIB,
       "alcatelIND1OpenflowMIBNotifications": alcatelIND1OpenflowMIBNotifications,
       "alcatelIND1OpenflowMIBObjects": alcatelIND1OpenflowMIBObjects,
       "alaOpenflowGlobalConfigObjects": alaOpenflowGlobalConfigObjects,
       "alaOpenflowGlobalBackoffMax": alaOpenflowGlobalBackoffMax,
       "alaOpenflowGlobalIdleProbeTimeout": alaOpenflowGlobalIdleProbeTimeout,
       "alaOpenflowLogicalSwitchTable": alaOpenflowLogicalSwitchTable,
       "alaOpenflowLogicalSwitchEntry": alaOpenflowLogicalSwitchEntry,
       "alaOpenflowLogicalSwitch": alaOpenflowLogicalSwitch,
       "alaOpenflowLogicalSwitchAdminState": alaOpenflowLogicalSwitchAdminState,
       "alaOpenflowLogicalSwitchMode": alaOpenflowLogicalSwitchMode,
       "alaOpenflowLogicalSwitchVersions": alaOpenflowLogicalSwitchVersions,
       "alaOpenflowLogicalSwitchVlan": alaOpenflowLogicalSwitchVlan,
       "alaOpenflowLogicalSwitchControllerCount": alaOpenflowLogicalSwitchControllerCount,
       "alaOpenflowLogicalSwitchInterfaceCount": alaOpenflowLogicalSwitchInterfaceCount,
       "alaOpenflowLogicalSwitchFlowCount": alaOpenflowLogicalSwitchFlowCount,
       "alaOpenflowLogicalSwitchRowStatus": alaOpenflowLogicalSwitchRowStatus,
       "alaOpenflowControllerTable": alaOpenflowControllerTable,
       "alaOpenflowControllerEntry": alaOpenflowControllerEntry,
       "alaOpenflowControllerLogicalSwitch": alaOpenflowControllerLogicalSwitch,
       "alaOpenflowControllerIpType": alaOpenflowControllerIpType,
       "alaOpenflowControllerIp": alaOpenflowControllerIp,
       "alaOpenflowControllerPort": alaOpenflowControllerPort,
       "alaOpenflowControllerRole": alaOpenflowControllerRole,
       "alaOpenflowControllerAdminState": alaOpenflowControllerAdminState,
       "alaOpenflowControllerOperState": alaOpenflowControllerOperState,
       "alaOpenflowControllerRowStatus": alaOpenflowControllerRowStatus,
       "alaOpenflowInterfaceTable": alaOpenflowInterfaceTable,
       "alaOpenflowInterfaceEntry": alaOpenflowInterfaceEntry,
       "alaOpenflowInterfaceLogicalSwitch": alaOpenflowInterfaceLogicalSwitch,
       "alaOpenflowInterface": alaOpenflowInterface,
       "alaOpenflowInterfaceMode": alaOpenflowInterfaceMode,
       "alaOpenflowInterfaceRowStatus": alaOpenflowInterfaceRowStatus,
       "alaOpenflowFlowStatsTable": alaOpenflowFlowStatsTable,
       "alaOpenflowFlowStatsEntry": alaOpenflowFlowStatsEntry,
       "alaOpenflowFlowStatsLogicalSwitch": alaOpenflowFlowStatsLogicalSwitch,
       "alaOpenflowFlowStatsExactCount": alaOpenflowFlowStatsExactCount,
       "alaOpenflowFlowStatsWildCount": alaOpenflowFlowStatsWildCount,
       "alaOpenflowFlowEntryStatsTable": alaOpenflowFlowEntryStatsTable,
       "alaOpenflowFlowEntryStatsEntry": alaOpenflowFlowEntryStatsEntry,
       "alaOpenflowFlowEntryStatsLogicalSwitch": alaOpenflowFlowEntryStatsLogicalSwitch,
       "alaOpenflowFlowEntryStatsFlowId": alaOpenflowFlowEntryStatsFlowId,
       "alaOpenflowFlowEntryStatsRcvdPcks": alaOpenflowFlowEntryStatsRcvdPcks,
       "alaOpenflowFlowEntryStatsRcvdbytes": alaOpenflowFlowEntryStatsRcvdbytes,
       "alaOpenflowFlowEntryStatsDuration": alaOpenflowFlowEntryStatsDuration,
       "alaOpenflowPortStatsTable": alaOpenflowPortStatsTable,
       "alaOpenflowPortStatsEntry": alaOpenflowPortStatsEntry,
       "alaOpenflowPortStatsLogicalSwitch": alaOpenflowPortStatsLogicalSwitch,
       "alaOpenflowPortStatsSlotNumber": alaOpenflowPortStatsSlotNumber,
       "alaOpenflowPortStatsPortNumber": alaOpenflowPortStatsPortNumber,
       "alaOpenflowPortStatsTransPcks": alaOpenflowPortStatsTransPcks,
       "alaOpenflowPortStatsRcvdPcks": alaOpenflowPortStatsRcvdPcks,
       "alaOpenflowPortStatsDuration": alaOpenflowPortStatsDuration,
       "alaOpenflowGroupStatsTable": alaOpenflowGroupStatsTable,
       "alaOpenflowGroupStatsEntry": alaOpenflowGroupStatsEntry,
       "alaOpenflowGroupStatsLogicalSwitch": alaOpenflowGroupStatsLogicalSwitch,
       "alaOpenflowGroupStatsId": alaOpenflowGroupStatsId,
       "alaOpenflowGroupStatsDuration": alaOpenflowGroupStatsDuration,
       "alcatelIND1OpenflowMIBConformance": alcatelIND1OpenflowMIBConformance,
       "alcatelIND1OpenflowMIBGroups": alcatelIND1OpenflowMIBGroups,
       "alaOpenflowModuleConfigGroup": alaOpenflowModuleConfigGroup,
       "alaOpenflowModuleLogicalSwitchGroup": alaOpenflowModuleLogicalSwitchGroup,
       "alaOpenflowModuleControllerGroup": alaOpenflowModuleControllerGroup,
       "alaOpenflowModuleInterfaceGroup": alaOpenflowModuleInterfaceGroup,
       "alaOpenflowModuleFlowStatsGroup": alaOpenflowModuleFlowStatsGroup,
       "alaOpenflowModuleFlowEntryStatsGroup": alaOpenflowModuleFlowEntryStatsGroup,
       "alaOpenflowModulePortStatsGroup": alaOpenflowModulePortStatsGroup,
       "alaOpenflowModuleGroupStatsGroup": alaOpenflowModuleGroupStatsGroup,
       "alcatelIND1OpenflowMIBCompliances": alcatelIND1OpenflowMIBCompliances,
       "alaOpenflowMIBCompliance": alaOpenflowMIBCompliance}
)
