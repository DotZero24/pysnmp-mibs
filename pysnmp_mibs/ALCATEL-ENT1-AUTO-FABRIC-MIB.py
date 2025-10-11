# SNMP MIB module (ALCATEL-ENT1-AUTO-FABRIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-AUTO-FABRIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:08:56 2025
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

(softentIND1AutoFabric,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1AutoFabric")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1AUTOFABRICMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AUTOFABRICMIB.setRevisions(
        ("2012-11-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1AUTOFABRICMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1AUTOFABRICMIBNotifications = _AlcatelIND1AUTOFABRICMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 0)
)
_AlcatelIND1AUTOFABRICMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1AUTOFABRICMIBObjects = _AlcatelIND1AUTOFABRICMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AUTOFABRICMIBObjects.setStatus("current")


class _AlaAutoFabricGlobalStatus_Type(Integer32):
    """Custom type alaAutoFabricGlobalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricGlobalStatus_Type.__name__ = "Integer32"
_AlaAutoFabricGlobalStatus_Object = MibScalar
alaAutoFabricGlobalStatus = _AlaAutoFabricGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 1),
    _AlaAutoFabricGlobalStatus_Type()
)
alaAutoFabricGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalStatus.setStatus("current")


class _AlaAutoFabricGlobalDiscovery_Type(Integer32):
    """Custom type alaAutoFabricGlobalDiscovery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("restart", 2))
    )


_AlaAutoFabricGlobalDiscovery_Type.__name__ = "Integer32"
_AlaAutoFabricGlobalDiscovery_Object = MibScalar
alaAutoFabricGlobalDiscovery = _AlaAutoFabricGlobalDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 2),
    _AlaAutoFabricGlobalDiscovery_Type()
)
alaAutoFabricGlobalDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalDiscovery.setStatus("current")


class _AlaAutoFabricGlobalLACPProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricGlobalLACPProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricGlobalLACPProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricGlobalLACPProtocolStatus_Object = MibScalar
alaAutoFabricGlobalLACPProtocolStatus = _AlaAutoFabricGlobalLACPProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 3),
    _AlaAutoFabricGlobalLACPProtocolStatus_Type()
)
alaAutoFabricGlobalLACPProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalLACPProtocolStatus.setStatus("current")


class _AlaAutoFabricGlobalSPBProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricGlobalSPBProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricGlobalSPBProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricGlobalSPBProtocolStatus_Object = MibScalar
alaAutoFabricGlobalSPBProtocolStatus = _AlaAutoFabricGlobalSPBProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 4),
    _AlaAutoFabricGlobalSPBProtocolStatus_Type()
)
alaAutoFabricGlobalSPBProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalSPBProtocolStatus.setStatus("current")


class _AlaAutoFabricGlobalMVRPProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricGlobalMVRPProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricGlobalMVRPProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricGlobalMVRPProtocolStatus_Object = MibScalar
alaAutoFabricGlobalMVRPProtocolStatus = _AlaAutoFabricGlobalMVRPProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 5),
    _AlaAutoFabricGlobalMVRPProtocolStatus_Type()
)
alaAutoFabricGlobalMVRPProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalMVRPProtocolStatus.setStatus("current")


class _AlaAutoFabricGlobalConfigSaveTimer_Type(Unsigned32):
    """Custom type alaAutoFabricGlobalConfigSaveTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_AlaAutoFabricGlobalConfigSaveTimer_Type.__name__ = "Unsigned32"
_AlaAutoFabricGlobalConfigSaveTimer_Object = MibScalar
alaAutoFabricGlobalConfigSaveTimer = _AlaAutoFabricGlobalConfigSaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 6),
    _AlaAutoFabricGlobalConfigSaveTimer_Type()
)
alaAutoFabricGlobalConfigSaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalConfigSaveTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalConfigSaveTimer.setUnits("seconds")


class _AlaAutoFabricGlobalConfigSaveTimerStatus_Type(Integer32):
    """Custom type alaAutoFabricGlobalConfigSaveTimerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricGlobalConfigSaveTimerStatus_Type.__name__ = "Integer32"
_AlaAutoFabricGlobalConfigSaveTimerStatus_Object = MibScalar
alaAutoFabricGlobalConfigSaveTimerStatus = _AlaAutoFabricGlobalConfigSaveTimerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 7),
    _AlaAutoFabricGlobalConfigSaveTimerStatus_Type()
)
alaAutoFabricGlobalConfigSaveTimerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalConfigSaveTimerStatus.setStatus("current")


class _AlaAutoFabricGlobalDiscoveryTimer_Type(Unsigned32):
    """Custom type alaAutoFabricGlobalDiscoveryTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AlaAutoFabricGlobalDiscoveryTimer_Type.__name__ = "Unsigned32"
_AlaAutoFabricGlobalDiscoveryTimer_Object = MibScalar
alaAutoFabricGlobalDiscoveryTimer = _AlaAutoFabricGlobalDiscoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 8),
    _AlaAutoFabricGlobalDiscoveryTimer_Type()
)
alaAutoFabricGlobalDiscoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalDiscoveryTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalDiscoveryTimer.setUnits("Minutes")
_AlaAutoFabricPortConfig_ObjectIdentity = ObjectIdentity
alaAutoFabricPortConfig = _AlaAutoFabricPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9)
)
_AlaAutoFabricPortConfigTable_Object = MibTable
alaAutoFabricPortConfigTable = _AlaAutoFabricPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alaAutoFabricPortConfigTable.setStatus("current")
_AlaAutoFabricPortConfigEntry_Object = MibTableRow
alaAutoFabricPortConfigEntry = _AlaAutoFabricPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1)
)
alaAutoFabricPortConfigEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    alaAutoFabricPortConfigEntry.setStatus("current")
_AlaAutoFabricPortConfigIfIndex_Type = InterfaceIndex
_AlaAutoFabricPortConfigIfIndex_Object = MibTableColumn
alaAutoFabricPortConfigIfIndex = _AlaAutoFabricPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 1),
    _AlaAutoFabricPortConfigIfIndex_Type()
)
alaAutoFabricPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAutoFabricPortConfigIfIndex.setStatus("current")


class _AlaAutoFabricPortConfigStatus_Type(Integer32):
    """Custom type alaAutoFabricPortConfigStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricPortConfigStatus_Type.__name__ = "Integer32"
_AlaAutoFabricPortConfigStatus_Object = MibTableColumn
alaAutoFabricPortConfigStatus = _AlaAutoFabricPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 2),
    _AlaAutoFabricPortConfigStatus_Type()
)
alaAutoFabricPortConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricPortConfigStatus.setStatus("current")


class _AlaAutoFabricPortLACPProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricPortLACPProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricPortLACPProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricPortLACPProtocolStatus_Object = MibTableColumn
alaAutoFabricPortLACPProtocolStatus = _AlaAutoFabricPortLACPProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 3),
    _AlaAutoFabricPortLACPProtocolStatus_Type()
)
alaAutoFabricPortLACPProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricPortLACPProtocolStatus.setStatus("current")


class _AlaAutoFabricPortSPBProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricPortSPBProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricPortSPBProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricPortSPBProtocolStatus_Object = MibTableColumn
alaAutoFabricPortSPBProtocolStatus = _AlaAutoFabricPortSPBProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 4),
    _AlaAutoFabricPortSPBProtocolStatus_Type()
)
alaAutoFabricPortSPBProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricPortSPBProtocolStatus.setStatus("current")


class _AlaAutoFabricPortMVRPProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricPortMVRPProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricPortMVRPProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricPortMVRPProtocolStatus_Object = MibTableColumn
alaAutoFabricPortMVRPProtocolStatus = _AlaAutoFabricPortMVRPProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 5),
    _AlaAutoFabricPortMVRPProtocolStatus_Type()
)
alaAutoFabricPortMVRPProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricPortMVRPProtocolStatus.setStatus("current")


class _AlaAutoFabricPortStatus_Type(Integer32):
    """Custom type alaAutoFabricPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("pending", 2),
          ("complete", 3))
    )


_AlaAutoFabricPortStatus_Type.__name__ = "Integer32"
_AlaAutoFabricPortStatus_Object = MibTableColumn
alaAutoFabricPortStatus = _AlaAutoFabricPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 6),
    _AlaAutoFabricPortStatus_Type()
)
alaAutoFabricPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaAutoFabricPortStatus.setStatus("current")


class _AlaAutoFabricPortSPBDefaultProfile_Type(Integer32):
    """Custom type alaAutoFabricPortSPBDefaultProfile based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleService", 1),
          ("autoVlan", 2))
    )


_AlaAutoFabricPortSPBDefaultProfile_Type.__name__ = "Integer32"
_AlaAutoFabricPortSPBDefaultProfile_Object = MibTableColumn
alaAutoFabricPortSPBDefaultProfile = _AlaAutoFabricPortSPBDefaultProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 9, 1, 1, 7),
    _AlaAutoFabricPortSPBDefaultProfile_Type()
)
alaAutoFabricPortSPBDefaultProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricPortSPBDefaultProfile.setStatus("current")


class _AlaAutoFabricRemoveGlobalConfig_Type(Integer32):
    """Custom type alaAutoFabricRemoveGlobalConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("removeGlobalConfig", 2))
    )


_AlaAutoFabricRemoveGlobalConfig_Type.__name__ = "Integer32"
_AlaAutoFabricRemoveGlobalConfig_Object = MibScalar
alaAutoFabricRemoveGlobalConfig = _AlaAutoFabricRemoveGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 10),
    _AlaAutoFabricRemoveGlobalConfig_Type()
)
alaAutoFabricRemoveGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricRemoveGlobalConfig.setStatus("deprecated")


class _AlaAutoFabricGlobalOSPFv2ProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricGlobalOSPFv2ProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricGlobalOSPFv2ProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricGlobalOSPFv2ProtocolStatus_Object = MibScalar
alaAutoFabricGlobalOSPFv2ProtocolStatus = _AlaAutoFabricGlobalOSPFv2ProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 11),
    _AlaAutoFabricGlobalOSPFv2ProtocolStatus_Type()
)
alaAutoFabricGlobalOSPFv2ProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalOSPFv2ProtocolStatus.setStatus("current")


class _AlaAutoFabricGlobalOSPFv3ProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricGlobalOSPFv3ProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricGlobalOSPFv3ProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricGlobalOSPFv3ProtocolStatus_Object = MibScalar
alaAutoFabricGlobalOSPFv3ProtocolStatus = _AlaAutoFabricGlobalOSPFv3ProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 12),
    _AlaAutoFabricGlobalOSPFv3ProtocolStatus_Type()
)
alaAutoFabricGlobalOSPFv3ProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalOSPFv3ProtocolStatus.setStatus("current")


class _AlaAutoFabricGlobalISISProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricGlobalISISProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricGlobalISISProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricGlobalISISProtocolStatus_Object = MibScalar
alaAutoFabricGlobalISISProtocolStatus = _AlaAutoFabricGlobalISISProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 13),
    _AlaAutoFabricGlobalISISProtocolStatus_Type()
)
alaAutoFabricGlobalISISProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricGlobalISISProtocolStatus.setStatus("current")


class _AlaAutoFabricSPBDefaultProfile_Type(Integer32):
    """Custom type alaAutoFabricSPBDefaultProfile based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleService", 1),
          ("autoVlan", 2))
    )


_AlaAutoFabricSPBDefaultProfile_Type.__name__ = "Integer32"
_AlaAutoFabricSPBDefaultProfile_Object = MibScalar
alaAutoFabricSPBDefaultProfile = _AlaAutoFabricSPBDefaultProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 14),
    _AlaAutoFabricSPBDefaultProfile_Type()
)
alaAutoFabricSPBDefaultProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricSPBDefaultProfile.setStatus("current")


class _AlaAutoFabricLBDProtocolStatus_Type(Integer32):
    """Custom type alaAutoFabricLBDProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaAutoFabricLBDProtocolStatus_Type.__name__ = "Integer32"
_AlaAutoFabricLBDProtocolStatus_Object = MibScalar
alaAutoFabricLBDProtocolStatus = _AlaAutoFabricLBDProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 15),
    _AlaAutoFabricLBDProtocolStatus_Type()
)
alaAutoFabricLBDProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricLBDProtocolStatus.setStatus("current")
_AlaAutoFabricTrapsObj_ObjectIdentity = ObjectIdentity
alaAutoFabricTrapsObj = _AlaAutoFabricTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 16)
)


class _AlaAutoFabricSTPMode_Type(Integer32):
    """Custom type alaAutoFabricSTPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flatMode", 1),
          ("perVlan", 2))
    )


_AlaAutoFabricSTPMode_Type.__name__ = "Integer32"
_AlaAutoFabricSTPMode_Object = MibScalar
alaAutoFabricSTPMode = _AlaAutoFabricSTPMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 16, 1),
    _AlaAutoFabricSTPMode_Type()
)
alaAutoFabricSTPMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaAutoFabricSTPMode.setStatus("current")


class _AlaAutoFabricRemoveVCReload_Type(Integer32):
    """Custom type alaAutoFabricRemoveVCReload based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("removeVCReload", 2))
    )


_AlaAutoFabricRemoveVCReload_Type.__name__ = "Integer32"
_AlaAutoFabricRemoveVCReload_Object = MibScalar
alaAutoFabricRemoveVCReload = _AlaAutoFabricRemoveVCReload_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 1, 17),
    _AlaAutoFabricRemoveVCReload_Type()
)
alaAutoFabricRemoveVCReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAutoFabricRemoveVCReload.setStatus("current")
_AlcatelIND1AUTOFABRICMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1AUTOFABRICMIBConformance = _AlcatelIND1AUTOFABRICMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AUTOFABRICMIBConformance.setStatus("current")
_AlcatelIND1AUTOFABRICMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1AUTOFABRICMIBGroups = _AlcatelIND1AUTOFABRICMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AUTOFABRICMIBGroups.setStatus("current")
_AlcatelIND1AUTOFABRICMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1AUTOFABRICMIBCompliances = _AlcatelIND1AUTOFABRICMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AUTOFABRICMIBCompliances.setStatus("current")

# Managed Objects groups

alaAutoFabricBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 1)
)
alaAutoFabricBaseGroup.setObjects(
      *(("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalDiscovery"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalLACPProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalSPBProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalMVRPProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalConfigSaveTimer"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalConfigSaveTimerStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalDiscoveryTimer"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricRemoveGlobalConfig"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalOSPFv2ProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalOSPFv3ProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricGlobalISISProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricSPBDefaultProfile"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricLBDProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricRemoveVCReload"))
)
if mibBuilder.loadTexts:
    alaAutoFabricBaseGroup.setStatus("current")

alaAutoFabricPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 2)
)
alaAutoFabricPortConfigGroup.setObjects(
      *(("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricPortConfigStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricPortLACPProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricPortSPBProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricPortMVRPProtocolStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricPortStatus"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricPortSPBDefaultProfile"))
)
if mibBuilder.loadTexts:
    alaAutoFabricPortConfigGroup.setStatus("current")

alaAutoFabricTrapsObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 4)
)
alaAutoFabricTrapsObjGroup.setObjects(
    ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricSTPMode")
)
if mibBuilder.loadTexts:
    alaAutoFabricTrapsObjGroup.setStatus("current")


# Notification objects

alaAutoFabricSTPModeChangeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 0, 1)
)
alaAutoFabricSTPModeChangeAlert.setObjects(
    ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricSTPMode")
)
if mibBuilder.loadTexts:
    alaAutoFabricSTPModeChangeAlert.setStatus(
        "current"
    )


# Notifications groups

alaAutoFabricNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 1, 3)
)
alaAutoFabricNotificationGroup.setObjects(
    ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricSTPModeChangeAlert")
)
if mibBuilder.loadTexts:
    alaAutoFabricNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1AUTOFABRICMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 75, 1, 2, 2, 1)
)
alcatelIND1AUTOFABRICMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricBaseGroup"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricPortConfigGroup"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricNotificationGroup"),
        ("ALCATEL-ENT1-AUTO-FABRIC-MIB", "alaAutoFabricTrapsObjGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1AUTOFABRICMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-AUTO-FABRIC-MIB",
    **{"alcatelIND1AUTOFABRICMIB": alcatelIND1AUTOFABRICMIB,
       "alcatelIND1AUTOFABRICMIBNotifications": alcatelIND1AUTOFABRICMIBNotifications,
       "alaAutoFabricSTPModeChangeAlert": alaAutoFabricSTPModeChangeAlert,
       "alcatelIND1AUTOFABRICMIBObjects": alcatelIND1AUTOFABRICMIBObjects,
       "alaAutoFabricGlobalStatus": alaAutoFabricGlobalStatus,
       "alaAutoFabricGlobalDiscovery": alaAutoFabricGlobalDiscovery,
       "alaAutoFabricGlobalLACPProtocolStatus": alaAutoFabricGlobalLACPProtocolStatus,
       "alaAutoFabricGlobalSPBProtocolStatus": alaAutoFabricGlobalSPBProtocolStatus,
       "alaAutoFabricGlobalMVRPProtocolStatus": alaAutoFabricGlobalMVRPProtocolStatus,
       "alaAutoFabricGlobalConfigSaveTimer": alaAutoFabricGlobalConfigSaveTimer,
       "alaAutoFabricGlobalConfigSaveTimerStatus": alaAutoFabricGlobalConfigSaveTimerStatus,
       "alaAutoFabricGlobalDiscoveryTimer": alaAutoFabricGlobalDiscoveryTimer,
       "alaAutoFabricPortConfig": alaAutoFabricPortConfig,
       "alaAutoFabricPortConfigTable": alaAutoFabricPortConfigTable,
       "alaAutoFabricPortConfigEntry": alaAutoFabricPortConfigEntry,
       "alaAutoFabricPortConfigIfIndex": alaAutoFabricPortConfigIfIndex,
       "alaAutoFabricPortConfigStatus": alaAutoFabricPortConfigStatus,
       "alaAutoFabricPortLACPProtocolStatus": alaAutoFabricPortLACPProtocolStatus,
       "alaAutoFabricPortSPBProtocolStatus": alaAutoFabricPortSPBProtocolStatus,
       "alaAutoFabricPortMVRPProtocolStatus": alaAutoFabricPortMVRPProtocolStatus,
       "alaAutoFabricPortStatus": alaAutoFabricPortStatus,
       "alaAutoFabricPortSPBDefaultProfile": alaAutoFabricPortSPBDefaultProfile,
       "alaAutoFabricRemoveGlobalConfig": alaAutoFabricRemoveGlobalConfig,
       "alaAutoFabricGlobalOSPFv2ProtocolStatus": alaAutoFabricGlobalOSPFv2ProtocolStatus,
       "alaAutoFabricGlobalOSPFv3ProtocolStatus": alaAutoFabricGlobalOSPFv3ProtocolStatus,
       "alaAutoFabricGlobalISISProtocolStatus": alaAutoFabricGlobalISISProtocolStatus,
       "alaAutoFabricSPBDefaultProfile": alaAutoFabricSPBDefaultProfile,
       "alaAutoFabricLBDProtocolStatus": alaAutoFabricLBDProtocolStatus,
       "alaAutoFabricTrapsObj": alaAutoFabricTrapsObj,
       "alaAutoFabricSTPMode": alaAutoFabricSTPMode,
       "alaAutoFabricRemoveVCReload": alaAutoFabricRemoveVCReload,
       "alcatelIND1AUTOFABRICMIBConformance": alcatelIND1AUTOFABRICMIBConformance,
       "alcatelIND1AUTOFABRICMIBGroups": alcatelIND1AUTOFABRICMIBGroups,
       "alaAutoFabricBaseGroup": alaAutoFabricBaseGroup,
       "alaAutoFabricPortConfigGroup": alaAutoFabricPortConfigGroup,
       "alaAutoFabricNotificationGroup": alaAutoFabricNotificationGroup,
       "alaAutoFabricTrapsObjGroup": alaAutoFabricTrapsObjGroup,
       "alcatelIND1AUTOFABRICMIBCompliances": alcatelIND1AUTOFABRICMIBCompliances,
       "alcatelIND1AUTOFABRICMIBCompliance": alcatelIND1AUTOFABRICMIBCompliance}
)
