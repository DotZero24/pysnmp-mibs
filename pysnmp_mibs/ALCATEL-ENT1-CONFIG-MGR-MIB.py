# SNMP MIB module (ALCATEL-ENT1-CONFIG-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-CONFIG-MGR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:09:39 2025
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

(softentIND1Confmgr,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1Confmgr")

(VirtualOperChassisId,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-VIRTUAL-CHASSIS-MIB",
    "VirtualOperChassisId")

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

alcatelIND1ConfigMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1ConfigMgrMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1ConfigMgrMIBObjects = _AlcatelIND1ConfigMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBObjects.setStatus("current")
_ConfigManager_ObjectIdentity = ObjectIdentity
configManager = _ConfigManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1)
)


class _ConfigFileName_Type(SnmpAdminString):
    """Custom type configFileName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_ConfigFileName_Type.__name__ = "SnmpAdminString"
_ConfigFileName_Object = MibScalar
configFileName = _ConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 1),
    _ConfigFileName_Type()
)
configFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileName.setStatus("current")


class _ConfigFileAction_Type(Integer32):
    """Custom type configFileAction based on Integer32"""
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
          ("checkSyntaxOnly", 2),
          ("apply", 3))
    )


_ConfigFileAction_Type.__name__ = "Integer32"
_ConfigFileAction_Object = MibScalar
configFileAction = _ConfigFileAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 2),
    _ConfigFileAction_Type()
)
configFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileAction.setStatus("current")


class _ConfigErrorFileName_Type(SnmpAdminString):
    """Custom type configErrorFileName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigErrorFileName_Type.__name__ = "SnmpAdminString"
_ConfigErrorFileName_Object = MibScalar
configErrorFileName = _ConfigErrorFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 3),
    _ConfigErrorFileName_Type()
)
configErrorFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configErrorFileName.setStatus("current")


class _ConfigFileStatus_Type(Integer32):
    """Custom type configFileStatus based on Integer32"""
    defaultValue = 1

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
        *(("noneAvail", 1),
          ("inProgress", 2),
          ("completeNoErrors", 3),
          ("completeErrors", 4))
    )


_ConfigFileStatus_Type.__name__ = "Integer32"
_ConfigFileStatus_Object = MibScalar
configFileStatus = _ConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 4),
    _ConfigFileStatus_Type()
)
configFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFileStatus.setStatus("current")


class _ConfigFileMode_Type(Integer32):
    """Custom type configFileMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("verbose", 2))
    )


_ConfigFileMode_Type.__name__ = "Integer32"
_ConfigFileMode_Object = MibScalar
configFileMode = _ConfigFileMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 5),
    _ConfigFileMode_Type()
)
configFileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFileMode.setStatus("current")


class _ConfigTimerFileName_Type(SnmpAdminString):
    """Custom type configTimerFileName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_ConfigTimerFileName_Type.__name__ = "SnmpAdminString"
_ConfigTimerFileName_Object = MibScalar
configTimerFileName = _ConfigTimerFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 6),
    _ConfigTimerFileName_Type()
)
configTimerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTimerFileName.setStatus("current")


class _ConfigTimerFileTime_Type(SnmpAdminString):
    """Custom type configTimerFileTime based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConfigTimerFileTime_Type.__name__ = "SnmpAdminString"
_ConfigTimerFileTime_Object = MibScalar
configTimerFileTime = _ConfigTimerFileTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 7),
    _ConfigTimerFileTime_Type()
)
configTimerFileTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTimerFileTime.setStatus("current")


class _ConfigTimerFileStatus_Type(Integer32):
    """Custom type configTimerFileStatus based on Integer32"""
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
        *(("idle", 1),
          ("pending", 2),
          ("inProgress", 3))
    )


_ConfigTimerFileStatus_Type.__name__ = "Integer32"
_ConfigTimerFileStatus_Object = MibScalar
configTimerFileStatus = _ConfigTimerFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 8),
    _ConfigTimerFileStatus_Type()
)
configTimerFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTimerFileStatus.setStatus("current")


class _ConfigTimerClear_Type(Integer32):
    """Custom type configTimerClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigTimerClear_Type.__name__ = "Integer32"
_ConfigTimerClear_Object = MibScalar
configTimerClear = _ConfigTimerClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 9),
    _ConfigTimerClear_Type()
)
configTimerClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTimerClear.setStatus("current")


class _ConfigSnapshotFileName_Type(SnmpAdminString):
    """Custom type configSnapshotFileName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_ConfigSnapshotFileName_Type.__name__ = "SnmpAdminString"
_ConfigSnapshotFileName_Object = MibScalar
configSnapshotFileName = _ConfigSnapshotFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 10),
    _ConfigSnapshotFileName_Type()
)
configSnapshotFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotFileName.setStatus("current")


class _ConfigSnapshotAction_Type(Integer32):
    """Custom type configSnapshotAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAction_Type.__name__ = "Integer32"
_ConfigSnapshotAction_Object = MibScalar
configSnapshotAction = _ConfigSnapshotAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 11),
    _ConfigSnapshotAction_Type()
)
configSnapshotAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAction.setStatus("current")


class _ConfigSnapshotAllSelect_Type(Integer32):
    """Custom type configSnapshotAllSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAllSelect_Type.__name__ = "Integer32"
_ConfigSnapshotAllSelect_Object = MibScalar
configSnapshotAllSelect = _ConfigSnapshotAllSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 12),
    _ConfigSnapshotAllSelect_Type()
)
configSnapshotAllSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAllSelect.setStatus("current")


class _ConfigSnapshotVlanSelect_Type(Integer32):
    """Custom type configSnapshotVlanSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotVlanSelect_Type.__name__ = "Integer32"
_ConfigSnapshotVlanSelect_Object = MibScalar
configSnapshotVlanSelect = _ConfigSnapshotVlanSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 13),
    _ConfigSnapshotVlanSelect_Type()
)
configSnapshotVlanSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotVlanSelect.setStatus("current")


class _ConfigSnapshotSpanningTreeSelect_Type(Integer32):
    """Custom type configSnapshotSpanningTreeSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSpanningTreeSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSpanningTreeSelect_Object = MibScalar
configSnapshotSpanningTreeSelect = _ConfigSnapshotSpanningTreeSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 14),
    _ConfigSnapshotSpanningTreeSelect_Type()
)
configSnapshotSpanningTreeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSpanningTreeSelect.setStatus("current")


class _ConfigSnapshotQOSSelect_Type(Integer32):
    """Custom type configSnapshotQOSSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotQOSSelect_Type.__name__ = "Integer32"
_ConfigSnapshotQOSSelect_Object = MibScalar
configSnapshotQOSSelect = _ConfigSnapshotQOSSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 15),
    _ConfigSnapshotQOSSelect_Type()
)
configSnapshotQOSSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotQOSSelect.setStatus("current")


class _ConfigSnapshotIPSelect_Type(Integer32):
    """Custom type configSnapshotIPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPSelect_Object = MibScalar
configSnapshotIPSelect = _ConfigSnapshotIPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 16),
    _ConfigSnapshotIPSelect_Type()
)
configSnapshotIPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPSelect.setStatus("current")


class _ConfigSnapshotIPXSelect_Type(Integer32):
    """Custom type configSnapshotIPXSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPXSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPXSelect_Object = MibScalar
configSnapshotIPXSelect = _ConfigSnapshotIPXSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 17),
    _ConfigSnapshotIPXSelect_Type()
)
configSnapshotIPXSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPXSelect.setStatus("current")


class _ConfigSnapshotIPMSSelect_Type(Integer32):
    """Custom type configSnapshotIPMSSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPMSSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPMSSelect_Object = MibScalar
configSnapshotIPMSSelect = _ConfigSnapshotIPMSSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 18),
    _ConfigSnapshotIPMSSelect_Type()
)
configSnapshotIPMSSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPMSSelect.setStatus("current")


class _ConfigSnapshotAAASelect_Type(Integer32):
    """Custom type configSnapshotAAASelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAAASelect_Type.__name__ = "Integer32"
_ConfigSnapshotAAASelect_Object = MibScalar
configSnapshotAAASelect = _ConfigSnapshotAAASelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 19),
    _ConfigSnapshotAAASelect_Type()
)
configSnapshotAAASelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAAASelect.setStatus("current")


class _ConfigSnapshotSNMPSelect_Type(Integer32):
    """Custom type configSnapshotSNMPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSNMPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSNMPSelect_Object = MibScalar
configSnapshotSNMPSelect = _ConfigSnapshotSNMPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 20),
    _ConfigSnapshotSNMPSelect_Type()
)
configSnapshotSNMPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSNMPSelect.setStatus("current")


class _ConfigSnapshot8021QSelect_Type(Integer32):
    """Custom type configSnapshot8021QSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshot8021QSelect_Type.__name__ = "Integer32"
_ConfigSnapshot8021QSelect_Object = MibScalar
configSnapshot8021QSelect = _ConfigSnapshot8021QSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 21),
    _ConfigSnapshot8021QSelect_Type()
)
configSnapshot8021QSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshot8021QSelect.setStatus("current")


class _ConfigSnapshotLinkAggregateSelect_Type(Integer32):
    """Custom type configSnapshotLinkAggregateSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotLinkAggregateSelect_Type.__name__ = "Integer32"
_ConfigSnapshotLinkAggregateSelect_Object = MibScalar
configSnapshotLinkAggregateSelect = _ConfigSnapshotLinkAggregateSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 22),
    _ConfigSnapshotLinkAggregateSelect_Type()
)
configSnapshotLinkAggregateSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotLinkAggregateSelect.setStatus("current")


class _ConfigSnapshotPortMirrorSelect_Type(Integer32):
    """Custom type configSnapshotPortMirrorSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPortMirrorSelect_Type.__name__ = "Integer32"
_ConfigSnapshotPortMirrorSelect_Object = MibScalar
configSnapshotPortMirrorSelect = _ConfigSnapshotPortMirrorSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 23),
    _ConfigSnapshotPortMirrorSelect_Type()
)
configSnapshotPortMirrorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPortMirrorSelect.setStatus("current")


class _ConfigSnapshotXIPSelect_Type(Integer32):
    """Custom type configSnapshotXIPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotXIPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotXIPSelect_Object = MibScalar
configSnapshotXIPSelect = _ConfigSnapshotXIPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 24),
    _ConfigSnapshotXIPSelect_Type()
)
configSnapshotXIPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotXIPSelect.setStatus("current")


class _ConfigSnapshotHealthMonitorSelect_Type(Integer32):
    """Custom type configSnapshotHealthMonitorSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotHealthMonitorSelect_Type.__name__ = "Integer32"
_ConfigSnapshotHealthMonitorSelect_Object = MibScalar
configSnapshotHealthMonitorSelect = _ConfigSnapshotHealthMonitorSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 25),
    _ConfigSnapshotHealthMonitorSelect_Type()
)
configSnapshotHealthMonitorSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotHealthMonitorSelect.setStatus("current")


class _ConfigSnapshotBootPSelect_Type(Integer32):
    """Custom type configSnapshotBootPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotBootPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotBootPSelect_Object = MibScalar
configSnapshotBootPSelect = _ConfigSnapshotBootPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 26),
    _ConfigSnapshotBootPSelect_Type()
)
configSnapshotBootPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotBootPSelect.setStatus("current")


class _ConfigSnapshotBridgeSelect_Type(Integer32):
    """Custom type configSnapshotBridgeSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotBridgeSelect_Type.__name__ = "Integer32"
_ConfigSnapshotBridgeSelect_Object = MibScalar
configSnapshotBridgeSelect = _ConfigSnapshotBridgeSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 27),
    _ConfigSnapshotBridgeSelect_Type()
)
configSnapshotBridgeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotBridgeSelect.setStatus("current")


class _ConfigSnapshotChassisSelect_Type(Integer32):
    """Custom type configSnapshotChassisSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotChassisSelect_Type.__name__ = "Integer32"
_ConfigSnapshotChassisSelect_Object = MibScalar
configSnapshotChassisSelect = _ConfigSnapshotChassisSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 28),
    _ConfigSnapshotChassisSelect_Type()
)
configSnapshotChassisSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotChassisSelect.setStatus("current")


class _ConfigSnapshotInterfaceSelect_Type(Integer32):
    """Custom type configSnapshotInterfaceSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotInterfaceSelect_Type.__name__ = "Integer32"
_ConfigSnapshotInterfaceSelect_Object = MibScalar
configSnapshotInterfaceSelect = _ConfigSnapshotInterfaceSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 29),
    _ConfigSnapshotInterfaceSelect_Type()
)
configSnapshotInterfaceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotInterfaceSelect.setStatus("current")


class _ConfigSnapshotPolicySelect_Type(Integer32):
    """Custom type configSnapshotPolicySelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPolicySelect_Type.__name__ = "Integer32"
_ConfigSnapshotPolicySelect_Object = MibScalar
configSnapshotPolicySelect = _ConfigSnapshotPolicySelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 30),
    _ConfigSnapshotPolicySelect_Type()
)
configSnapshotPolicySelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPolicySelect.setStatus("current")


class _ConfigSnapshotSessionSelect_Type(Integer32):
    """Custom type configSnapshotSessionSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSessionSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSessionSelect_Object = MibScalar
configSnapshotSessionSelect = _ConfigSnapshotSessionSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 31),
    _ConfigSnapshotSessionSelect_Type()
)
configSnapshotSessionSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSessionSelect.setStatus("current")


class _ConfigSnapshotServerLoadBalanceSelect_Type(Integer32):
    """Custom type configSnapshotServerLoadBalanceSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotServerLoadBalanceSelect_Type.__name__ = "Integer32"
_ConfigSnapshotServerLoadBalanceSelect_Object = MibScalar
configSnapshotServerLoadBalanceSelect = _ConfigSnapshotServerLoadBalanceSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 32),
    _ConfigSnapshotServerLoadBalanceSelect_Type()
)
configSnapshotServerLoadBalanceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotServerLoadBalanceSelect.setStatus("current")


class _ConfigSnapshotSystemServiceSelect_Type(Integer32):
    """Custom type configSnapshotSystemServiceSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSystemServiceSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSystemServiceSelect_Object = MibScalar
configSnapshotSystemServiceSelect = _ConfigSnapshotSystemServiceSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 33),
    _ConfigSnapshotSystemServiceSelect_Type()
)
configSnapshotSystemServiceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSystemServiceSelect.setStatus("current")


class _ConfigSnapshotVRRPSelect_Type(Integer32):
    """Custom type configSnapshotVRRPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotVRRPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotVRRPSelect_Object = MibScalar
configSnapshotVRRPSelect = _ConfigSnapshotVRRPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 34),
    _ConfigSnapshotVRRPSelect_Type()
)
configSnapshotVRRPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotVRRPSelect.setStatus("current")


class _ConfigSnapshotWebSelect_Type(Integer32):
    """Custom type configSnapshotWebSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotWebSelect_Type.__name__ = "Integer32"
_ConfigSnapshotWebSelect_Object = MibScalar
configSnapshotWebSelect = _ConfigSnapshotWebSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 35),
    _ConfigSnapshotWebSelect_Type()
)
configSnapshotWebSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotWebSelect.setStatus("current")


class _ConfigSnapshotRIPSelect_Type(Integer32):
    """Custom type configSnapshotRIPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotRIPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotRIPSelect_Object = MibScalar
configSnapshotRIPSelect = _ConfigSnapshotRIPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 36),
    _ConfigSnapshotRIPSelect_Type()
)
configSnapshotRIPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotRIPSelect.setStatus("current")


class _ConfigSnapshotOSPFSelect_Type(Integer32):
    """Custom type configSnapshotOSPFSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotOSPFSelect_Type.__name__ = "Integer32"
_ConfigSnapshotOSPFSelect_Object = MibScalar
configSnapshotOSPFSelect = _ConfigSnapshotOSPFSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 37),
    _ConfigSnapshotOSPFSelect_Type()
)
configSnapshotOSPFSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotOSPFSelect.setStatus("current")


class _ConfigSnapshotBGPSelect_Type(Integer32):
    """Custom type configSnapshotBGPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotBGPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotBGPSelect_Object = MibScalar
configSnapshotBGPSelect = _ConfigSnapshotBGPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 38),
    _ConfigSnapshotBGPSelect_Type()
)
configSnapshotBGPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotBGPSelect.setStatus("current")


class _ConfigSnapshotIPRMSelect_Type(Integer32):
    """Custom type configSnapshotIPRMSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPRMSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPRMSelect_Object = MibScalar
configSnapshotIPRMSelect = _ConfigSnapshotIPRMSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 39),
    _ConfigSnapshotIPRMSelect_Type()
)
configSnapshotIPRMSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPRMSelect.setStatus("current")


class _ConfigSnapshotIPMRSelect_Type(Integer32):
    """Custom type configSnapshotIPMRSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPMRSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPMRSelect_Object = MibScalar
configSnapshotIPMRSelect = _ConfigSnapshotIPMRSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 40),
    _ConfigSnapshotIPMRSelect_Type()
)
configSnapshotIPMRSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPMRSelect.setStatus("current")


class _ConfigSnapshotModuleSelect_Type(Integer32):
    """Custom type configSnapshotModuleSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotModuleSelect_Type.__name__ = "Integer32"
_ConfigSnapshotModuleSelect_Object = MibScalar
configSnapshotModuleSelect = _ConfigSnapshotModuleSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 41),
    _ConfigSnapshotModuleSelect_Type()
)
configSnapshotModuleSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotModuleSelect.setStatus("current")


class _ConfigTechSupportLogAction_Type(Integer32):
    """Custom type configTechSupportLogAction based on Integer32"""
    defaultValue = 1

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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("notSignificant", 0),
          ("techSupportBasic", 1),
          ("techSupportL2", 2),
          ("techSupportL3", 3),
          ("techSupportL3Rip", 4),
          ("techSupportL3Ipx", 5),
          ("techSupportL3Ospf", 6),
          ("techSupportL3Bgp", 7),
          ("techSupportL3Pimsm", 8),
          ("techSupportL3Mroute", 9),
          ("techSupportL3Dvmrp", 10),
          ("techSupportL3IPv6", 11),
          ("techSupportL3RIPng", 12),
          ("techSupportL3OSPF3", 13),
          ("techSupportL3Isis", 14),
          ("techSupportL3Pim6", 15),
          ("techSupportL3IPsec", 16),
          ("techSupportL3Bfd", 17))
    )


_ConfigTechSupportLogAction_Type.__name__ = "Integer32"
_ConfigTechSupportLogAction_Object = MibScalar
configTechSupportLogAction = _ConfigTechSupportLogAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 42),
    _ConfigTechSupportLogAction_Type()
)
configTechSupportLogAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTechSupportLogAction.setStatus("current")


class _ConfigWriteMemory_Type(Integer32):
    """Custom type configWriteMemory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigWriteMemory_Type.__name__ = "Integer32"
_ConfigWriteMemory_Object = MibScalar
configWriteMemory = _ConfigWriteMemory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 43),
    _ConfigWriteMemory_Type()
)
configWriteMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configWriteMemory.setStatus("current")


class _ConfigErrorFileMaximum_Type(Integer32):
    """Custom type configErrorFileMaximum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_ConfigErrorFileMaximum_Type.__name__ = "Integer32"
_ConfigErrorFileMaximum_Object = MibScalar
configErrorFileMaximum = _ConfigErrorFileMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 44),
    _ConfigErrorFileMaximum_Type()
)
configErrorFileMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configErrorFileMaximum.setStatus("current")


class _ConfigChangeStatus_Type(Integer32):
    """Custom type configChangeStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("identical", 1),
          ("different", 2))
    )


_ConfigChangeStatus_Type.__name__ = "Integer32"
_ConfigChangeStatus_Object = MibScalar
configChangeStatus = _ConfigChangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 45),
    _ConfigChangeStatus_Type()
)
configChangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configChangeStatus.setStatus("current")


class _ConfigSnapshotRDPSelect_Type(Integer32):
    """Custom type configSnapshotRDPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotRDPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotRDPSelect_Object = MibScalar
configSnapshotRDPSelect = _ConfigSnapshotRDPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 46),
    _ConfigSnapshotRDPSelect_Type()
)
configSnapshotRDPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotRDPSelect.setStatus("current")


class _ConfigSnapshotIPv6Select_Type(Integer32):
    """Custom type configSnapshotIPv6Select based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPv6Select_Type.__name__ = "Integer32"
_ConfigSnapshotIPv6Select_Object = MibScalar
configSnapshotIPv6Select = _ConfigSnapshotIPv6Select_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 47),
    _ConfigSnapshotIPv6Select_Type()
)
configSnapshotIPv6Select.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPv6Select.setStatus("current")


class _ConfigSnapshotRIPngSelect_Type(Integer32):
    """Custom type configSnapshotRIPngSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotRIPngSelect_Type.__name__ = "Integer32"
_ConfigSnapshotRIPngSelect_Object = MibScalar
configSnapshotRIPngSelect = _ConfigSnapshotRIPngSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 48),
    _ConfigSnapshotRIPngSelect_Type()
)
configSnapshotRIPngSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotRIPngSelect.setStatus("current")


class _ConfigSnapshotAtmSelect_Type(Integer32):
    """Custom type configSnapshotAtmSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAtmSelect_Type.__name__ = "Integer32"
_ConfigSnapshotAtmSelect_Object = MibScalar
configSnapshotAtmSelect = _ConfigSnapshotAtmSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 49),
    _ConfigSnapshotAtmSelect_Type()
)
configSnapshotAtmSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAtmSelect.setStatus("current")


class _ConfigSnapshotSonetSelect_Type(Integer32):
    """Custom type configSnapshotSonetSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSonetSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSonetSelect_Object = MibScalar
configSnapshotSonetSelect = _ConfigSnapshotSonetSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 50),
    _ConfigSnapshotSonetSelect_Type()
)
configSnapshotSonetSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSonetSelect.setStatus("current")


class _ConfigSnapshotNTPSelect_Type(Integer32):
    """Custom type configSnapshotNTPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotNTPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotNTPSelect_Object = MibScalar
configSnapshotNTPSelect = _ConfigSnapshotNTPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 51),
    _ConfigSnapshotNTPSelect_Type()
)
configSnapshotNTPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotNTPSelect.setStatus("current")


class _ConfigSnapshotPortMappingSelect_Type(Integer32):
    """Custom type configSnapshotPortMappingSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPortMappingSelect_Type.__name__ = "Integer32"
_ConfigSnapshotPortMappingSelect_Object = MibScalar
configSnapshotPortMappingSelect = _ConfigSnapshotPortMappingSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 52),
    _ConfigSnapshotPortMappingSelect_Type()
)
configSnapshotPortMappingSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPortMappingSelect.setStatus("current")


class _ConfigSnapshotOSPF3Select_Type(Integer32):
    """Custom type configSnapshotOSPF3Select based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotOSPF3Select_Type.__name__ = "Integer32"
_ConfigSnapshotOSPF3Select_Object = MibScalar
configSnapshotOSPF3Select = _ConfigSnapshotOSPF3Select_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 53),
    _ConfigSnapshotOSPF3Select_Type()
)
configSnapshotOSPF3Select.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotOSPF3Select.setStatus("current")


class _ConfigWriteMemoryStatus_Type(Integer32):
    """Custom type configWriteMemoryStatus based on Integer32"""
    defaultValue = 1

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
        *(("noneAvail", 1),
          ("inProgress", 2),
          ("completeNoErrors", 3),
          ("completeErrors", 4))
    )


_ConfigWriteMemoryStatus_Type.__name__ = "Integer32"
_ConfigWriteMemoryStatus_Object = MibScalar
configWriteMemoryStatus = _ConfigWriteMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 54),
    _ConfigWriteMemoryStatus_Type()
)
configWriteMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configWriteMemoryStatus.setStatus("current")


class _ConfigSnapshotStackSelect_Type(Integer32):
    """Custom type configSnapshotStackSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotStackSelect_Type.__name__ = "Integer32"
_ConfigSnapshotStackSelect_Object = MibScalar
configSnapshotStackSelect = _ConfigSnapshotStackSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 55),
    _ConfigSnapshotStackSelect_Type()
)
configSnapshotStackSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotStackSelect.setStatus("current")


class _ConfigSnapshotISISSelect_Type(Integer32):
    """Custom type configSnapshotISISSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotISISSelect_Type.__name__ = "Integer32"
_ConfigSnapshotISISSelect_Object = MibScalar
configSnapshotISISSelect = _ConfigSnapshotISISSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 56),
    _ConfigSnapshotISISSelect_Type()
)
configSnapshotISISSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotISISSelect.setStatus("current")


class _ConfigSnapshotEOAMSelect_Type(Integer32):
    """Custom type configSnapshotEOAMSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotEOAMSelect_Type.__name__ = "Integer32"
_ConfigSnapshotEOAMSelect_Object = MibScalar
configSnapshotEOAMSelect = _ConfigSnapshotEOAMSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 57),
    _ConfigSnapshotEOAMSelect_Type()
)
configSnapshotEOAMSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotEOAMSelect.setStatus("current")


class _ConfigSnapshotUDLDSelect_Type(Integer32):
    """Custom type configSnapshotUDLDSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotUDLDSelect_Type.__name__ = "Integer32"
_ConfigSnapshotUDLDSelect_Object = MibScalar
configSnapshotUDLDSelect = _ConfigSnapshotUDLDSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 58),
    _ConfigSnapshotUDLDSelect_Type()
)
configSnapshotUDLDSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotUDLDSelect.setStatus("current")


class _ConfigSnapshotNETSECSelect_Type(Integer32):
    """Custom type configSnapshotNETSECSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotNETSECSelect_Type.__name__ = "Integer32"
_ConfigSnapshotNETSECSelect_Object = MibScalar
configSnapshotNETSECSelect = _ConfigSnapshotNETSECSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 59),
    _ConfigSnapshotNETSECSelect_Type()
)
configSnapshotNETSECSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotNETSECSelect.setStatus("current")


class _ConfigSnapshotIPsecSelect_Type(Integer32):
    """Custom type configSnapshotIPsecSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotIPsecSelect_Type.__name__ = "Integer32"
_ConfigSnapshotIPsecSelect_Object = MibScalar
configSnapshotIPsecSelect = _ConfigSnapshotIPsecSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 60),
    _ConfigSnapshotIPsecSelect_Type()
)
configSnapshotIPsecSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotIPsecSelect.setStatus("current")


class _ConfigSnapshotBFDSelect_Type(Integer32):
    """Custom type configSnapshotBFDSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotBFDSelect_Type.__name__ = "Integer32"
_ConfigSnapshotBFDSelect_Object = MibScalar
configSnapshotBFDSelect = _ConfigSnapshotBFDSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 61),
    _ConfigSnapshotBFDSelect_Type()
)
configSnapshotBFDSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotBFDSelect.setStatus("current")


class _ConfigSnapshotMultiChassisSelect_Type(Integer32):
    """Custom type configSnapshotMultiChassisSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotMultiChassisSelect_Type.__name__ = "Integer32"
_ConfigSnapshotMultiChassisSelect_Object = MibScalar
configSnapshotMultiChassisSelect = _ConfigSnapshotMultiChassisSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 62),
    _ConfigSnapshotMultiChassisSelect_Type()
)
configSnapshotMultiChassisSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotMultiChassisSelect.setStatus("current")


class _ConfigSnapshotErpSelect_Type(Integer32):
    """Custom type configSnapshotErpSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotErpSelect_Type.__name__ = "Integer32"
_ConfigSnapshotErpSelect_Object = MibScalar
configSnapshotErpSelect = _ConfigSnapshotErpSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 63),
    _ConfigSnapshotErpSelect_Type()
)
configSnapshotErpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotErpSelect.setStatus("current")


class _ConfigSnapshotMPLSSelect_Type(Integer32):
    """Custom type configSnapshotMPLSSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotMPLSSelect_Type.__name__ = "Integer32"
_ConfigSnapshotMPLSSelect_Object = MibScalar
configSnapshotMPLSSelect = _ConfigSnapshotMPLSSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 64),
    _ConfigSnapshotMPLSSelect_Type()
)
configSnapshotMPLSSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotMPLSSelect.setStatus("current")


class _ConfigSnapshotEFMOAMSelect_Type(Integer32):
    """Custom type configSnapshotEFMOAMSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotEFMOAMSelect_Type.__name__ = "Integer32"
_ConfigSnapshotEFMOAMSelect_Object = MibScalar
configSnapshotEFMOAMSelect = _ConfigSnapshotEFMOAMSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 65),
    _ConfigSnapshotEFMOAMSelect_Type()
)
configSnapshotEFMOAMSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotEFMOAMSelect.setStatus("current")


class _ConfigSnapshotCapabilitySelect_Type(Integer32):
    """Custom type configSnapshotCapabilitySelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotCapabilitySelect_Type.__name__ = "Integer32"
_ConfigSnapshotCapabilitySelect_Object = MibScalar
configSnapshotCapabilitySelect = _ConfigSnapshotCapabilitySelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 66),
    _ConfigSnapshotCapabilitySelect_Type()
)
configSnapshotCapabilitySelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotCapabilitySelect.setStatus("current")


class _ConfigSnapshotVfcSelect_Type(Integer32):
    """Custom type configSnapshotVfcSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotVfcSelect_Type.__name__ = "Integer32"
_ConfigSnapshotVfcSelect_Object = MibScalar
configSnapshotVfcSelect = _ConfigSnapshotVfcSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 67),
    _ConfigSnapshotVfcSelect_Type()
)
configSnapshotVfcSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotVfcSelect.setStatus("current")


class _ConfigSnapshotHaVlanSelect_Type(Integer32):
    """Custom type configSnapshotHaVlanSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotHaVlanSelect_Type.__name__ = "Integer32"
_ConfigSnapshotHaVlanSelect_Object = MibScalar
configSnapshotHaVlanSelect = _ConfigSnapshotHaVlanSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 68),
    _ConfigSnapshotHaVlanSelect_Type()
)
configSnapshotHaVlanSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotHaVlanSelect.setStatus("current")


class _ConfigSnapshotDaUnpSelect_Type(Integer32):
    """Custom type configSnapshotDaUnpSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotDaUnpSelect_Type.__name__ = "Integer32"
_ConfigSnapshotDaUnpSelect_Object = MibScalar
configSnapshotDaUnpSelect = _ConfigSnapshotDaUnpSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 69),
    _ConfigSnapshotDaUnpSelect_Type()
)
configSnapshotDaUnpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotDaUnpSelect.setStatus("current")


class _ConfigSnapshotDHLSelect_Type(Integer32):
    """Custom type configSnapshotDHLSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotDHLSelect_Type.__name__ = "Integer32"
_ConfigSnapshotDHLSelect_Object = MibScalar
configSnapshotDHLSelect = _ConfigSnapshotDHLSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 70),
    _ConfigSnapshotDHLSelect_Type()
)
configSnapshotDHLSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotDHLSelect.setStatus("current")


class _ConfigSnapshotMVRPSelect_Type(Integer32):
    """Custom type configSnapshotMVRPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotMVRPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotMVRPSelect_Object = MibScalar
configSnapshotMVRPSelect = _ConfigSnapshotMVRPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 71),
    _ConfigSnapshotMVRPSelect_Type()
)
configSnapshotMVRPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotMVRPSelect.setStatus("current")


class _ConfigSnapshotSAASelect_Type(Integer32):
    """Custom type configSnapshotSAASelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSAASelect_Type.__name__ = "Integer32"
_ConfigSnapshotSAASelect_Object = MibScalar
configSnapshotSAASelect = _ConfigSnapshotSAASelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 72),
    _ConfigSnapshotSAASelect_Type()
)
configSnapshotSAASelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSAASelect.setStatus("current")


class _ConfigSnapshotSPBSelect_Type(Integer32):
    """Custom type configSnapshotSPBSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSPBSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSPBSelect_Object = MibScalar
configSnapshotSPBSelect = _ConfigSnapshotSPBSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 73),
    _ConfigSnapshotSPBSelect_Type()
)
configSnapshotSPBSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSPBSelect.setStatus("current")


class _ConfigSnapshotSPBIsisSelect_Type(Integer32):
    """Custom type configSnapshotSPBIsisSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSPBIsisSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSPBIsisSelect_Object = MibScalar
configSnapshotSPBIsisSelect = _ConfigSnapshotSPBIsisSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 74),
    _ConfigSnapshotSPBIsisSelect_Type()
)
configSnapshotSPBIsisSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSPBIsisSelect.setStatus("current")


class _ConfigSnapshotVirtualChassisSelect_Type(Integer32):
    """Custom type configSnapshotVirtualChassisSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotVirtualChassisSelect_Type.__name__ = "Integer32"
_ConfigSnapshotVirtualChassisSelect_Object = MibScalar
configSnapshotVirtualChassisSelect = _ConfigSnapshotVirtualChassisSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 75),
    _ConfigSnapshotVirtualChassisSelect_Type()
)
configSnapshotVirtualChassisSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotVirtualChassisSelect.setStatus("current")


class _ConfigSnapshotMplsLdpSelect_Type(Integer32):
    """Custom type configSnapshotMplsLdpSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotMplsLdpSelect_Type.__name__ = "Integer32"
_ConfigSnapshotMplsLdpSelect_Object = MibScalar
configSnapshotMplsLdpSelect = _ConfigSnapshotMplsLdpSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 76),
    _ConfigSnapshotMplsLdpSelect_Type()
)
configSnapshotMplsLdpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotMplsLdpSelect.setStatus("current")


class _ConfigSnapshotVCMSpecific_Type(Integer32):
    """Custom type configSnapshotVCMSpecific based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotVCMSpecific_Type.__name__ = "Integer32"
_ConfigSnapshotVCMSpecific_Object = MibScalar
configSnapshotVCMSpecific = _ConfigSnapshotVCMSpecific_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 77),
    _ConfigSnapshotVCMSpecific_Type()
)
configSnapshotVCMSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotVCMSpecific.setStatus("current")


class _ConfigSnapshotChassisId_Type(VirtualOperChassisId):
    """Custom type configSnapshotChassisId based on VirtualOperChassisId"""
    defaultValue = 0


_ConfigSnapshotChassisId_Type.__name__ = "VirtualOperChassisId"
_ConfigSnapshotChassisId_Object = MibScalar
configSnapshotChassisId = _ConfigSnapshotChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 78),
    _ConfigSnapshotChassisId_Type()
)
configSnapshotChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotChassisId.setStatus("current")


class _ConfigSnapshotEvbSelect_Type(Integer32):
    """Custom type configSnapshotEvbSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotEvbSelect_Type.__name__ = "Integer32"
_ConfigSnapshotEvbSelect_Object = MibScalar
configSnapshotEvbSelect = _ConfigSnapshotEvbSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 79),
    _ConfigSnapshotEvbSelect_Type()
)
configSnapshotEvbSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotEvbSelect.setStatus("current")


class _ConfigConvertConfiguration_Type(Integer32):
    """Custom type configConvertConfiguration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSignificant", 0),
          ("virtualChassis", 1))
    )


_ConfigConvertConfiguration_Type.__name__ = "Integer32"
_ConfigConvertConfiguration_Object = MibScalar
configConvertConfiguration = _ConfigConvertConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 80),
    _ConfigConvertConfiguration_Type()
)
configConvertConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configConvertConfiguration.setStatus("current")


class _ConfigConvertConfigurationStatus_Type(Integer32):
    """Custom type configConvertConfigurationStatus based on Integer32"""
    defaultValue = 1

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
        *(("noneAvail", 1),
          ("inProgress", 2),
          ("completeNoErrors", 3),
          ("completeErrors", 4))
    )


_ConfigConvertConfigurationStatus_Type.__name__ = "Integer32"
_ConfigConvertConfigurationStatus_Object = MibScalar
configConvertConfigurationStatus = _ConfigConvertConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 81),
    _ConfigConvertConfigurationStatus_Type()
)
configConvertConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configConvertConfigurationStatus.setStatus("current")


class _ConfigConvertDestinationDirectory_Type(SnmpAdminString):
    """Custom type configConvertDestinationDirectory based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_ConfigConvertDestinationDirectory_Type.__name__ = "SnmpAdminString"
_ConfigConvertDestinationDirectory_Object = MibScalar
configConvertDestinationDirectory = _ConfigConvertDestinationDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 82),
    _ConfigConvertDestinationDirectory_Type()
)
configConvertDestinationDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configConvertDestinationDirectory.setStatus("current")


class _ConfigConvertReload_Type(Integer32):
    """Custom type configConvertReload based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigConvertReload_Type.__name__ = "Integer32"
_ConfigConvertReload_Object = MibScalar
configConvertReload = _ConfigConvertReload_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 83),
    _ConfigConvertReload_Type()
)
configConvertReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configConvertReload.setStatus("current")


class _ConfigSnapshotAppfpSelect_Type(Integer32):
    """Custom type configSnapshotAppfpSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAppfpSelect_Type.__name__ = "Integer32"
_ConfigSnapshotAppfpSelect_Object = MibScalar
configSnapshotAppfpSelect = _ConfigSnapshotAppfpSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 84),
    _ConfigSnapshotAppfpSelect_Type()
)
configSnapshotAppfpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAppfpSelect.setStatus("current")


class _ConfigSnapshotFipsSelect_Type(Integer32):
    """Custom type configSnapshotFipsSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotFipsSelect_Type.__name__ = "Integer32"
_ConfigSnapshotFipsSelect_Object = MibScalar
configSnapshotFipsSelect = _ConfigSnapshotFipsSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 85),
    _ConfigSnapshotFipsSelect_Type()
)
configSnapshotFipsSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotFipsSelect.setStatus("current")


class _ConfigSnapshotLFPSelect_Type(Integer32):
    """Custom type configSnapshotLFPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotLFPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotLFPSelect_Object = MibScalar
configSnapshotLFPSelect = _ConfigSnapshotLFPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 86),
    _ConfigSnapshotLFPSelect_Type()
)
configSnapshotLFPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotLFPSelect.setStatus("current")


class _ConfigSnapshotPmInterfaceSelect_Type(Integer32):
    """Custom type configSnapshotPmInterfaceSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPmInterfaceSelect_Type.__name__ = "Integer32"
_ConfigSnapshotPmInterfaceSelect_Object = MibScalar
configSnapshotPmInterfaceSelect = _ConfigSnapshotPmInterfaceSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 87),
    _ConfigSnapshotPmInterfaceSelect_Type()
)
configSnapshotPmInterfaceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPmInterfaceSelect.setStatus("current")


class _ConfigSnapshotAutofabricSelect_Type(Integer32):
    """Custom type configSnapshotAutofabricSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAutofabricSelect_Type.__name__ = "Integer32"
_ConfigSnapshotAutofabricSelect_Object = MibScalar
configSnapshotAutofabricSelect = _ConfigSnapshotAutofabricSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 88),
    _ConfigSnapshotAutofabricSelect_Type()
)
configSnapshotAutofabricSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAutofabricSelect.setStatus("current")


class _ConfigSnapshotDhcpv6RelaySelect_Type(Integer32):
    """Custom type configSnapshotDhcpv6RelaySelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotDhcpv6RelaySelect_Type.__name__ = "Integer32"
_ConfigSnapshotDhcpv6RelaySelect_Object = MibScalar
configSnapshotDhcpv6RelaySelect = _ConfigSnapshotDhcpv6RelaySelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 89),
    _ConfigSnapshotDhcpv6RelaySelect_Type()
)
configSnapshotDhcpv6RelaySelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotDhcpv6RelaySelect.setStatus("current")


class _ConfigSnapshotSIPSelect_Type(Integer32):
    """Custom type configSnapshotSIPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotSIPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotSIPSelect_Object = MibScalar
configSnapshotSIPSelect = _ConfigSnapshotSIPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 90),
    _ConfigSnapshotSIPSelect_Type()
)
configSnapshotSIPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotSIPSelect.setStatus("current")


class _ConfigSnapshotOpenflowSelect_Type(Integer32):
    """Custom type configSnapshotOpenflowSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotOpenflowSelect_Type.__name__ = "Integer32"
_ConfigSnapshotOpenflowSelect_Object = MibScalar
configSnapshotOpenflowSelect = _ConfigSnapshotOpenflowSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 91),
    _ConfigSnapshotOpenflowSelect_Type()
)
configSnapshotOpenflowSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotOpenflowSelect.setStatus("current")


class _ConfigSnapshotWlanSelect_Type(Integer32):
    """Custom type configSnapshotWlanSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotWlanSelect_Type.__name__ = "Integer32"
_ConfigSnapshotWlanSelect_Object = MibScalar
configSnapshotWlanSelect = _ConfigSnapshotWlanSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 92),
    _ConfigSnapshotWlanSelect_Type()
)
configSnapshotWlanSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotWlanSelect.setStatus("current")


class _ConfigSnapshotDhcpSrvSelect_Type(Integer32):
    """Custom type configSnapshotDhcpSrvSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotDhcpSrvSelect_Type.__name__ = "Integer32"
_ConfigSnapshotDhcpSrvSelect_Object = MibScalar
configSnapshotDhcpSrvSelect = _ConfigSnapshotDhcpSrvSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 93),
    _ConfigSnapshotDhcpSrvSelect_Type()
)
configSnapshotDhcpSrvSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotDhcpSrvSelect.setStatus("current")


class _ConfigSnapshotDPISelect_Type(Integer32):
    """Custom type configSnapshotDPISelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotDPISelect_Type.__name__ = "Integer32"
_ConfigSnapshotDPISelect_Object = MibScalar
configSnapshotDPISelect = _ConfigSnapshotDPISelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 94),
    _ConfigSnapshotDPISelect_Type()
)
configSnapshotDPISelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotDPISelect.setStatus("current")


class _ConfigSnapshotMsgSrvSelect_Type(Integer32):
    """Custom type configSnapshotMsgSrvSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotMsgSrvSelect_Type.__name__ = "Integer32"
_ConfigSnapshotMsgSrvSelect_Object = MibScalar
configSnapshotMsgSrvSelect = _ConfigSnapshotMsgSrvSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 95),
    _ConfigSnapshotMsgSrvSelect_Type()
)
configSnapshotMsgSrvSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotMsgSrvSelect.setStatus("current")


class _ConfigSnapshotAlSrvSelect_Type(Integer32):
    """Custom type configSnapshotAlSrvSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAlSrvSelect_Type.__name__ = "Integer32"
_ConfigSnapshotAlSrvSelect_Object = MibScalar
configSnapshotAlSrvSelect = _ConfigSnapshotAlSrvSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 96),
    _ConfigSnapshotAlSrvSelect_Type()
)
configSnapshotAlSrvSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAlSrvSelect.setStatus("current")


class _ConfigSnapshotDhcpv6SrvSelect_Type(Integer32):
    """Custom type configSnapshotDhcpv6SrvSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotDhcpv6SrvSelect_Type.__name__ = "Integer32"
_ConfigSnapshotDhcpv6SrvSelect_Object = MibScalar
configSnapshotDhcpv6SrvSelect = _ConfigSnapshotDhcpv6SrvSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 97),
    _ConfigSnapshotDhcpv6SrvSelect_Type()
)
configSnapshotDhcpv6SrvSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotDhcpv6SrvSelect.setStatus("current")


class _ConfigSnapshotAGSelect_Type(Integer32):
    """Custom type configSnapshotAGSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAGSelect_Type.__name__ = "Integer32"
_ConfigSnapshotAGSelect_Object = MibScalar
configSnapshotAGSelect = _ConfigSnapshotAGSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 98),
    _ConfigSnapshotAGSelect_Type()
)
configSnapshotAGSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAGSelect.setStatus("current")


class _ConfigSnapshotQMRSelect_Type(Integer32):
    """Custom type configSnapshotQMRSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotQMRSelect_Type.__name__ = "Integer32"
_ConfigSnapshotQMRSelect_Object = MibScalar
configSnapshotQMRSelect = _ConfigSnapshotQMRSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 99),
    _ConfigSnapshotQMRSelect_Type()
)
configSnapshotQMRSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotQMRSelect.setStatus("current")


class _ConfigSnapshotVCSPSelect_Type(Integer32):
    """Custom type configSnapshotVCSPSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotVCSPSelect_Type.__name__ = "Integer32"
_ConfigSnapshotVCSPSelect_Object = MibScalar
configSnapshotVCSPSelect = _ConfigSnapshotVCSPSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 100),
    _ConfigSnapshotVCSPSelect_Type()
)
configSnapshotVCSPSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotVCSPSelect.setStatus("current")


class _ConfigSnapshotDhcpSnoopingSelect_Type(Integer32):
    """Custom type configSnapshotDhcpSnoopingSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotDhcpSnoopingSelect_Type.__name__ = "Integer32"
_ConfigSnapshotDhcpSnoopingSelect_Object = MibScalar
configSnapshotDhcpSnoopingSelect = _ConfigSnapshotDhcpSnoopingSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 101),
    _ConfigSnapshotDhcpSnoopingSelect_Type()
)
configSnapshotDhcpSnoopingSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotDhcpSnoopingSelect.setStatus("current")


class _ConfigSnapshotAppMonSelect_Type(Integer32):
    """Custom type configSnapshotAppMonSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotAppMonSelect_Type.__name__ = "Integer32"
_ConfigSnapshotAppMonSelect_Object = MibScalar
configSnapshotAppMonSelect = _ConfigSnapshotAppMonSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 102),
    _ConfigSnapshotAppMonSelect_Type()
)
configSnapshotAppMonSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotAppMonSelect.setStatus("current")


class _ConfigSnapshotLbdSelect_Type(Integer32):
    """Custom type configSnapshotLbdSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotLbdSelect_Type.__name__ = "Integer32"
_ConfigSnapshotLbdSelect_Object = MibScalar
configSnapshotLbdSelect = _ConfigSnapshotLbdSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 103),
    _ConfigSnapshotLbdSelect_Type()
)
configSnapshotLbdSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotLbdSelect.setStatus("current")


class _ConfigSnapshotVMSnoopSelect_Type(Integer32):
    """Custom type configSnapshotVMSnoopSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotVMSnoopSelect_Type.__name__ = "Integer32"
_ConfigSnapshotVMSnoopSelect_Object = MibScalar
configSnapshotVMSnoopSelect = _ConfigSnapshotVMSnoopSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 104),
    _ConfigSnapshotVMSnoopSelect_Type()
)
configSnapshotVMSnoopSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotVMSnoopSelect.setStatus("current")


class _ConfigSnapshotPppoeIaSelect_Type(Integer32):
    """Custom type configSnapshotPppoeIaSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPppoeIaSelect_Type.__name__ = "Integer32"
_ConfigSnapshotPppoeIaSelect_Object = MibScalar
configSnapshotPppoeIaSelect = _ConfigSnapshotPppoeIaSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 105),
    _ConfigSnapshotPppoeIaSelect_Type()
)
configSnapshotPppoeIaSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPppoeIaSelect.setStatus("current")


class _ConfigSnapshotPmPortViolationSelect_Type(Integer32):
    """Custom type configSnapshotPmPortViolationSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPmPortViolationSelect_Type.__name__ = "Integer32"
_ConfigSnapshotPmPortViolationSelect_Object = MibScalar
configSnapshotPmPortViolationSelect = _ConfigSnapshotPmPortViolationSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 106),
    _ConfigSnapshotPmPortViolationSelect_Type()
)
configSnapshotPmPortViolationSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPmPortViolationSelect.setStatus("current")


class _ConfigSnapshotLanPowerSelect_Type(Integer32):
    """Custom type configSnapshotLanPowerSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotLanPowerSelect_Type.__name__ = "Integer32"
_ConfigSnapshotLanPowerSelect_Object = MibScalar
configSnapshotLanPowerSelect = _ConfigSnapshotLanPowerSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 107),
    _ConfigSnapshotLanPowerSelect_Type()
)
configSnapshotLanPowerSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotLanPowerSelect.setStatus("current")


class _ConfigSnapshotPVLANSelect_Type(Integer32):
    """Custom type configSnapshotPVLANSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ConfigSnapshotPVLANSelect_Type.__name__ = "Integer32"
_ConfigSnapshotPVLANSelect_Object = MibScalar
configSnapshotPVLANSelect = _ConfigSnapshotPVLANSelect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 1, 1, 108),
    _ConfigSnapshotPVLANSelect_Type()
)
configSnapshotPVLANSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnapshotPVLANSelect.setStatus("current")
_AlcatelIND1ConfigMgrMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1ConfigMgrMIBConformance = _AlcatelIND1ConfigMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBConformance.setStatus("current")
_AlcatelIND1ConfigMgrMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1ConfigMgrMIBGroups = _AlcatelIND1ConfigMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBGroups.setStatus("current")
_AlcatelIND1ConfigMgrMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1ConfigMgrMIBCompliances = _AlcatelIND1ConfigMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBCompliances.setStatus("current")

# Managed Objects groups

configFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 1)
)
configFileGroup.setObjects(
      *(("ALCATEL-ENT1-CONFIG-MGR-MIB", "configFileName"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configFileAction"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configErrorFileName"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configFileStatus"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configFileMode"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configErrorFileMaximum"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configChangeStatus"))
)
if mibBuilder.loadTexts:
    configFileGroup.setStatus("current")

configTimerFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 2)
)
configTimerFileGroup.setObjects(
      *(("ALCATEL-ENT1-CONFIG-MGR-MIB", "configTimerFileName"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configTimerFileTime"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configTimerFileStatus"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configTimerClear"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotFileName"))
)
if mibBuilder.loadTexts:
    configTimerFileGroup.setStatus("current")

configSnapshotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 3)
)
configSnapshotGroup.setObjects(
      *(("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotAction"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotAllSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotVCMSpecific"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotChassisId"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotVlanSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotSpanningTreeSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotQOSSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotIPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotIPXSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotIPMSSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotAAASelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotSNMPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshot8021QSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotLinkAggregateSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotPortMirrorSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotXIPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotHealthMonitorSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotBootPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotBridgeSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotChassisSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotInterfaceSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotPolicySelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotSessionSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotServerLoadBalanceSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotSystemServiceSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotVRRPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotWebSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotRIPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotOSPFSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotBGPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotIPRMSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotIPMRSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotModuleSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotRDPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotIPv6Select"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotRIPngSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotAtmSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotSonetSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotNTPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotPortMappingSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotOSPF3Select"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotStackSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configWriteMemoryStatus"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotISISSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotEOAMSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotUDLDSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotNETSECSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotIPsecSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotBFDSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotMultiChassisSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotEFMOAMSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotMPLSSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotErpSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotCapabilitySelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotVfcSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotHaVlanSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotDaUnpSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotDHLSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotMVRPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotSAASelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotSPBSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotSPBIsisSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotVirtualChassisSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotMplsLdpSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotEvbSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotAppfpSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotFipsSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotLFPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotPmInterfaceSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotAutofabricSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotDhcpv6RelaySelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotSIPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotOpenflowSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotWlanSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotDhcpSrvSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotDPISelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotMsgSrvSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotAlSrvSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotDhcpv6SrvSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotAGSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotQMRSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotVCSPSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotDhcpSnoopingSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotAppMonSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotVMSnoopSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotLbdSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotPppoeIaSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotPmPortViolationSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotLanPowerSelect"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotPVLANSelect"))
)
if mibBuilder.loadTexts:
    configSnapshotGroup.setStatus("current")

configTechSupportLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 4)
)
configTechSupportLogGroup.setObjects(
    ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configTechSupportLogAction")
)
if mibBuilder.loadTexts:
    configTechSupportLogGroup.setStatus("current")

configWriteMemoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 5)
)
configWriteMemoryGroup.setObjects(
    ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configWriteMemory")
)
if mibBuilder.loadTexts:
    configWriteMemoryGroup.setStatus("current")

configConvertConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 1, 6)
)
configConvertConfigurationGroup.setObjects(
      *(("ALCATEL-ENT1-CONFIG-MGR-MIB", "configConvertConfiguration"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configConvertConfigurationStatus"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configConvertDestinationDirectory"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configConvertReload"))
)
if mibBuilder.loadTexts:
    configConvertConfigurationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1ConfigMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 11, 1, 2, 2, 1)
)
alcatelIND1ConfigMgrMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-CONFIG-MGR-MIB", "configFileGroup"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configTimerFileGroup"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configSnapshotGroup"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configTechSupportLogGroup"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configWriteMemoryGroup"),
        ("ALCATEL-ENT1-CONFIG-MGR-MIB", "configConvertConfigurationGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1ConfigMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-CONFIG-MGR-MIB",
    **{"alcatelIND1ConfigMgrMIB": alcatelIND1ConfigMgrMIB,
       "alcatelIND1ConfigMgrMIBObjects": alcatelIND1ConfigMgrMIBObjects,
       "configManager": configManager,
       "configFileName": configFileName,
       "configFileAction": configFileAction,
       "configErrorFileName": configErrorFileName,
       "configFileStatus": configFileStatus,
       "configFileMode": configFileMode,
       "configTimerFileName": configTimerFileName,
       "configTimerFileTime": configTimerFileTime,
       "configTimerFileStatus": configTimerFileStatus,
       "configTimerClear": configTimerClear,
       "configSnapshotFileName": configSnapshotFileName,
       "configSnapshotAction": configSnapshotAction,
       "configSnapshotAllSelect": configSnapshotAllSelect,
       "configSnapshotVlanSelect": configSnapshotVlanSelect,
       "configSnapshotSpanningTreeSelect": configSnapshotSpanningTreeSelect,
       "configSnapshotQOSSelect": configSnapshotQOSSelect,
       "configSnapshotIPSelect": configSnapshotIPSelect,
       "configSnapshotIPXSelect": configSnapshotIPXSelect,
       "configSnapshotIPMSSelect": configSnapshotIPMSSelect,
       "configSnapshotAAASelect": configSnapshotAAASelect,
       "configSnapshotSNMPSelect": configSnapshotSNMPSelect,
       "configSnapshot8021QSelect": configSnapshot8021QSelect,
       "configSnapshotLinkAggregateSelect": configSnapshotLinkAggregateSelect,
       "configSnapshotPortMirrorSelect": configSnapshotPortMirrorSelect,
       "configSnapshotXIPSelect": configSnapshotXIPSelect,
       "configSnapshotHealthMonitorSelect": configSnapshotHealthMonitorSelect,
       "configSnapshotBootPSelect": configSnapshotBootPSelect,
       "configSnapshotBridgeSelect": configSnapshotBridgeSelect,
       "configSnapshotChassisSelect": configSnapshotChassisSelect,
       "configSnapshotInterfaceSelect": configSnapshotInterfaceSelect,
       "configSnapshotPolicySelect": configSnapshotPolicySelect,
       "configSnapshotSessionSelect": configSnapshotSessionSelect,
       "configSnapshotServerLoadBalanceSelect": configSnapshotServerLoadBalanceSelect,
       "configSnapshotSystemServiceSelect": configSnapshotSystemServiceSelect,
       "configSnapshotVRRPSelect": configSnapshotVRRPSelect,
       "configSnapshotWebSelect": configSnapshotWebSelect,
       "configSnapshotRIPSelect": configSnapshotRIPSelect,
       "configSnapshotOSPFSelect": configSnapshotOSPFSelect,
       "configSnapshotBGPSelect": configSnapshotBGPSelect,
       "configSnapshotIPRMSelect": configSnapshotIPRMSelect,
       "configSnapshotIPMRSelect": configSnapshotIPMRSelect,
       "configSnapshotModuleSelect": configSnapshotModuleSelect,
       "configTechSupportLogAction": configTechSupportLogAction,
       "configWriteMemory": configWriteMemory,
       "configErrorFileMaximum": configErrorFileMaximum,
       "configChangeStatus": configChangeStatus,
       "configSnapshotRDPSelect": configSnapshotRDPSelect,
       "configSnapshotIPv6Select": configSnapshotIPv6Select,
       "configSnapshotRIPngSelect": configSnapshotRIPngSelect,
       "configSnapshotAtmSelect": configSnapshotAtmSelect,
       "configSnapshotSonetSelect": configSnapshotSonetSelect,
       "configSnapshotNTPSelect": configSnapshotNTPSelect,
       "configSnapshotPortMappingSelect": configSnapshotPortMappingSelect,
       "configSnapshotOSPF3Select": configSnapshotOSPF3Select,
       "configWriteMemoryStatus": configWriteMemoryStatus,
       "configSnapshotStackSelect": configSnapshotStackSelect,
       "configSnapshotISISSelect": configSnapshotISISSelect,
       "configSnapshotEOAMSelect": configSnapshotEOAMSelect,
       "configSnapshotUDLDSelect": configSnapshotUDLDSelect,
       "configSnapshotNETSECSelect": configSnapshotNETSECSelect,
       "configSnapshotIPsecSelect": configSnapshotIPsecSelect,
       "configSnapshotBFDSelect": configSnapshotBFDSelect,
       "configSnapshotMultiChassisSelect": configSnapshotMultiChassisSelect,
       "configSnapshotErpSelect": configSnapshotErpSelect,
       "configSnapshotMPLSSelect": configSnapshotMPLSSelect,
       "configSnapshotEFMOAMSelect": configSnapshotEFMOAMSelect,
       "configSnapshotCapabilitySelect": configSnapshotCapabilitySelect,
       "configSnapshotVfcSelect": configSnapshotVfcSelect,
       "configSnapshotHaVlanSelect": configSnapshotHaVlanSelect,
       "configSnapshotDaUnpSelect": configSnapshotDaUnpSelect,
       "configSnapshotDHLSelect": configSnapshotDHLSelect,
       "configSnapshotMVRPSelect": configSnapshotMVRPSelect,
       "configSnapshotSAASelect": configSnapshotSAASelect,
       "configSnapshotSPBSelect": configSnapshotSPBSelect,
       "configSnapshotSPBIsisSelect": configSnapshotSPBIsisSelect,
       "configSnapshotVirtualChassisSelect": configSnapshotVirtualChassisSelect,
       "configSnapshotMplsLdpSelect": configSnapshotMplsLdpSelect,
       "configSnapshotVCMSpecific": configSnapshotVCMSpecific,
       "configSnapshotChassisId": configSnapshotChassisId,
       "configSnapshotEvbSelect": configSnapshotEvbSelect,
       "configConvertConfiguration": configConvertConfiguration,
       "configConvertConfigurationStatus": configConvertConfigurationStatus,
       "configConvertDestinationDirectory": configConvertDestinationDirectory,
       "configConvertReload": configConvertReload,
       "configSnapshotAppfpSelect": configSnapshotAppfpSelect,
       "configSnapshotFipsSelect": configSnapshotFipsSelect,
       "configSnapshotLFPSelect": configSnapshotLFPSelect,
       "configSnapshotPmInterfaceSelect": configSnapshotPmInterfaceSelect,
       "configSnapshotAutofabricSelect": configSnapshotAutofabricSelect,
       "configSnapshotDhcpv6RelaySelect": configSnapshotDhcpv6RelaySelect,
       "configSnapshotSIPSelect": configSnapshotSIPSelect,
       "configSnapshotOpenflowSelect": configSnapshotOpenflowSelect,
       "configSnapshotWlanSelect": configSnapshotWlanSelect,
       "configSnapshotDhcpSrvSelect": configSnapshotDhcpSrvSelect,
       "configSnapshotDPISelect": configSnapshotDPISelect,
       "configSnapshotMsgSrvSelect": configSnapshotMsgSrvSelect,
       "configSnapshotAlSrvSelect": configSnapshotAlSrvSelect,
       "configSnapshotDhcpv6SrvSelect": configSnapshotDhcpv6SrvSelect,
       "configSnapshotAGSelect": configSnapshotAGSelect,
       "configSnapshotQMRSelect": configSnapshotQMRSelect,
       "configSnapshotVCSPSelect": configSnapshotVCSPSelect,
       "configSnapshotDhcpSnoopingSelect": configSnapshotDhcpSnoopingSelect,
       "configSnapshotAppMonSelect": configSnapshotAppMonSelect,
       "configSnapshotLbdSelect": configSnapshotLbdSelect,
       "configSnapshotVMSnoopSelect": configSnapshotVMSnoopSelect,
       "configSnapshotPppoeIaSelect": configSnapshotPppoeIaSelect,
       "configSnapshotPmPortViolationSelect": configSnapshotPmPortViolationSelect,
       "configSnapshotLanPowerSelect": configSnapshotLanPowerSelect,
       "configSnapshotPVLANSelect": configSnapshotPVLANSelect,
       "alcatelIND1ConfigMgrMIBConformance": alcatelIND1ConfigMgrMIBConformance,
       "alcatelIND1ConfigMgrMIBGroups": alcatelIND1ConfigMgrMIBGroups,
       "configFileGroup": configFileGroup,
       "configTimerFileGroup": configTimerFileGroup,
       "configSnapshotGroup": configSnapshotGroup,
       "configTechSupportLogGroup": configTechSupportLogGroup,
       "configWriteMemoryGroup": configWriteMemoryGroup,
       "configConvertConfigurationGroup": configConvertConfigurationGroup,
       "alcatelIND1ConfigMgrMIBCompliances": alcatelIND1ConfigMgrMIBCompliances,
       "alcatelIND1ConfigMgrMIBCompliance": alcatelIND1ConfigMgrMIBCompliance}
)
