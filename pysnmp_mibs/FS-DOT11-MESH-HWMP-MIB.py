# SNMP MIB module (FS-DOT11-MESH-HWMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-DOT11-MESH-HWMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:00 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

fsDot11MeshHWMPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92)
)
if mibBuilder.loadTexts:
    fsDot11MeshHWMPMIB.setRevisions(
        ("2010-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Apdot11MeshHWMPConfigObjects_ObjectIdentity = ObjectIdentity
apdot11MeshHWMPConfigObjects = _Apdot11MeshHWMPConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1)
)
_Dot11MeshHWMPConfigTable_Object = MibTable
dot11MeshHWMPConfigTable = _Dot11MeshHWMPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1)
)
if mibBuilder.loadTexts:
    dot11MeshHWMPConfigTable.setStatus("current")
_Dot11MeshHWMPConfigEntry_Object = MibTableRow
dot11MeshHWMPConfigEntry = _Dot11MeshHWMPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1)
)
dot11MeshHWMPConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dot11MeshHWMPConfigEntry.setStatus("current")


class _Dot11MeshHWMPmaxPREQretries_Type(Integer32):
    """Custom type dot11MeshHWMPmaxPREQretries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11MeshHWMPmaxPREQretries_Type.__name__ = "Integer32"
_Dot11MeshHWMPmaxPREQretries_Object = MibTableColumn
dot11MeshHWMPmaxPREQretries = _Dot11MeshHWMPmaxPREQretries_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 1),
    _Dot11MeshHWMPmaxPREQretries_Type()
)
dot11MeshHWMPmaxPREQretries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPmaxPREQretries.setStatus("current")


class _Dot11MeshHWMPnetDiameter_Type(Integer32):
    """Custom type dot11MeshHWMPnetDiameter based on Integer32"""
    defaultValue = 31

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Dot11MeshHWMPnetDiameter_Type.__name__ = "Integer32"
_Dot11MeshHWMPnetDiameter_Object = MibTableColumn
dot11MeshHWMPnetDiameter = _Dot11MeshHWMPnetDiameter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 2),
    _Dot11MeshHWMPnetDiameter_Type()
)
dot11MeshHWMPnetDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPnetDiameter.setStatus("current")


class _Dot11MeshHWMPnetDiameterTraversalTime_Type(Integer32):
    """Custom type dot11MeshHWMPnetDiameterTraversalTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MeshHWMPnetDiameterTraversalTime_Type.__name__ = "Integer32"
_Dot11MeshHWMPnetDiameterTraversalTime_Object = MibTableColumn
dot11MeshHWMPnetDiameterTraversalTime = _Dot11MeshHWMPnetDiameterTraversalTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 3),
    _Dot11MeshHWMPnetDiameterTraversalTime_Type()
)
dot11MeshHWMPnetDiameterTraversalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPnetDiameterTraversalTime.setStatus("current")


class _Dot11MeshHWMPpreqMinInterval_Type(Integer32):
    """Custom type dot11MeshHWMPpreqMinInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MeshHWMPpreqMinInterval_Type.__name__ = "Integer32"
_Dot11MeshHWMPpreqMinInterval_Object = MibTableColumn
dot11MeshHWMPpreqMinInterval = _Dot11MeshHWMPpreqMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 4),
    _Dot11MeshHWMPpreqMinInterval_Type()
)
dot11MeshHWMPpreqMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPpreqMinInterval.setStatus("current")


class _Dot11MeshHWMPperrMinInterval_Type(Integer32):
    """Custom type dot11MeshHWMPperrMinInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MeshHWMPperrMinInterval_Type.__name__ = "Integer32"
_Dot11MeshHWMPperrMinInterval_Object = MibTableColumn
dot11MeshHWMPperrMinInterval = _Dot11MeshHWMPperrMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 5),
    _Dot11MeshHWMPperrMinInterval_Type()
)
dot11MeshHWMPperrMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPperrMinInterval.setStatus("current")


class _Dot11MeshHWMPactivePathToRootTimeout_Type(Integer32):
    """Custom type dot11MeshHWMPactivePathToRootTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MeshHWMPactivePathToRootTimeout_Type.__name__ = "Integer32"
_Dot11MeshHWMPactivePathToRootTimeout_Object = MibTableColumn
dot11MeshHWMPactivePathToRootTimeout = _Dot11MeshHWMPactivePathToRootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 6),
    _Dot11MeshHWMPactivePathToRootTimeout_Type()
)
dot11MeshHWMPactivePathToRootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPactivePathToRootTimeout.setStatus("current")


class _Dot11MeshHWMPactivePathTimeout_Type(Integer32):
    """Custom type dot11MeshHWMPactivePathTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MeshHWMPactivePathTimeout_Type.__name__ = "Integer32"
_Dot11MeshHWMPactivePathTimeout_Object = MibTableColumn
dot11MeshHWMPactivePathTimeout = _Dot11MeshHWMPactivePathTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 7),
    _Dot11MeshHWMPactivePathTimeout_Type()
)
dot11MeshHWMPactivePathTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPactivePathTimeout.setStatus("current")


class _Dot11MeshHWMProotMode_Type(Integer32):
    """Custom type dot11MeshHWMProotMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noRoot", 0),
          ("proactivePREQnoPREP", 2),
          ("proactivePREQwithPREP", 3),
          ("rann", 4))
    )


_Dot11MeshHWMProotMode_Type.__name__ = "Integer32"
_Dot11MeshHWMProotMode_Object = MibTableColumn
dot11MeshHWMProotMode = _Dot11MeshHWMProotMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 8),
    _Dot11MeshHWMProotMode_Type()
)
dot11MeshHWMProotMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMProotMode.setStatus("current")


class _Dot11MeshHWMProotInterval_Type(Integer32):
    """Custom type dot11MeshHWMProotInterval based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MeshHWMProotInterval_Type.__name__ = "Integer32"
_Dot11MeshHWMProotInterval_Object = MibTableColumn
dot11MeshHWMProotInterval = _Dot11MeshHWMProotInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 9),
    _Dot11MeshHWMProotInterval_Type()
)
dot11MeshHWMProotInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMProotInterval.setStatus("current")


class _Dot11MeshHWMPrannInterval_Type(Integer32):
    """Custom type dot11MeshHWMPrannInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MeshHWMPrannInterval_Type.__name__ = "Integer32"
_Dot11MeshHWMPrannInterval_Object = MibTableColumn
dot11MeshHWMPrannInterval = _Dot11MeshHWMPrannInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 10),
    _Dot11MeshHWMPrannInterval_Type()
)
dot11MeshHWMPrannInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPrannInterval.setStatus("current")


class _Dot11MeshHWMPtargetOnly_Type(Integer32):
    """Custom type dot11MeshHWMPtargetOnly based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("intermediateMSTA", 0),
          ("targetOnly", 1))
    )


_Dot11MeshHWMPtargetOnly_Type.__name__ = "Integer32"
_Dot11MeshHWMPtargetOnly_Object = MibTableColumn
dot11MeshHWMPtargetOnly = _Dot11MeshHWMPtargetOnly_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 11),
    _Dot11MeshHWMPtargetOnly_Type()
)
dot11MeshHWMPtargetOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPtargetOnly.setStatus("current")


class _Dot11MeshHWMPmaintenanceInterval_Type(Integer32):
    """Custom type dot11MeshHWMPmaintenanceInterval based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MeshHWMPmaintenanceInterval_Type.__name__ = "Integer32"
_Dot11MeshHWMPmaintenanceInterval_Object = MibTableColumn
dot11MeshHWMPmaintenanceInterval = _Dot11MeshHWMPmaintenanceInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 12),
    _Dot11MeshHWMPmaintenanceInterval_Type()
)
dot11MeshHWMPmaintenanceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPmaintenanceInterval.setStatus("current")


class _Dot11MeshHWMPconfirmationInterval_Type(Integer32):
    """Custom type dot11MeshHWMPconfirmationInterval based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot11MeshHWMPconfirmationInterval_Type.__name__ = "Integer32"
_Dot11MeshHWMPconfirmationInterval_Object = MibTableColumn
dot11MeshHWMPconfirmationInterval = _Dot11MeshHWMPconfirmationInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 1, 1, 1, 13),
    _Dot11MeshHWMPconfirmationInterval_Type()
)
dot11MeshHWMPconfirmationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MeshHWMPconfirmationInterval.setStatus("current")
_FsDot11MeshHWMPConformance_ObjectIdentity = ObjectIdentity
fsDot11MeshHWMPConformance = _FsDot11MeshHWMPConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 2)
)
_FsDot11MeshHWMPCompliances_ObjectIdentity = ObjectIdentity
fsDot11MeshHWMPCompliances = _FsDot11MeshHWMPCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 2, 1)
)
_FsDot11MeshHWMPGroups_ObjectIdentity = ObjectIdentity
fsDot11MeshHWMPGroups = _FsDot11MeshHWMPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 2, 2)
)

# Managed Objects groups

fsDot11MeshHWMPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 2, 2, 1)
)
fsDot11MeshHWMPGroup.setObjects(
      *(("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPmaxPREQretries"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPnetDiameter"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPnetDiameterTraversalTime"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPpreqMinInterval"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPperrMinInterval"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPactivePathToRootTimeout"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPactivePathTimeout"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMProotMode"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMProotInterval"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPrannInterval"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPtargetOnly"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPmaintenanceInterval"),
        ("FS-DOT11-MESH-HWMP-MIB", "dot11MeshHWMPconfirmationInterval"))
)
if mibBuilder.loadTexts:
    fsDot11MeshHWMPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsDot11MeshHWMPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 92, 2, 1, 1)
)
fsDot11MeshHWMPCompliance.setObjects(
    ("FS-DOT11-MESH-HWMP-MIB", "fsDot11MeshHWMPGroup")
)
if mibBuilder.loadTexts:
    fsDot11MeshHWMPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-DOT11-MESH-HWMP-MIB",
    **{"fsDot11MeshHWMPMIB": fsDot11MeshHWMPMIB,
       "apdot11MeshHWMPConfigObjects": apdot11MeshHWMPConfigObjects,
       "dot11MeshHWMPConfigTable": dot11MeshHWMPConfigTable,
       "dot11MeshHWMPConfigEntry": dot11MeshHWMPConfigEntry,
       "dot11MeshHWMPmaxPREQretries": dot11MeshHWMPmaxPREQretries,
       "dot11MeshHWMPnetDiameter": dot11MeshHWMPnetDiameter,
       "dot11MeshHWMPnetDiameterTraversalTime": dot11MeshHWMPnetDiameterTraversalTime,
       "dot11MeshHWMPpreqMinInterval": dot11MeshHWMPpreqMinInterval,
       "dot11MeshHWMPperrMinInterval": dot11MeshHWMPperrMinInterval,
       "dot11MeshHWMPactivePathToRootTimeout": dot11MeshHWMPactivePathToRootTimeout,
       "dot11MeshHWMPactivePathTimeout": dot11MeshHWMPactivePathTimeout,
       "dot11MeshHWMProotMode": dot11MeshHWMProotMode,
       "dot11MeshHWMProotInterval": dot11MeshHWMProotInterval,
       "dot11MeshHWMPrannInterval": dot11MeshHWMPrannInterval,
       "dot11MeshHWMPtargetOnly": dot11MeshHWMPtargetOnly,
       "dot11MeshHWMPmaintenanceInterval": dot11MeshHWMPmaintenanceInterval,
       "dot11MeshHWMPconfirmationInterval": dot11MeshHWMPconfirmationInterval,
       "fsDot11MeshHWMPConformance": fsDot11MeshHWMPConformance,
       "fsDot11MeshHWMPCompliances": fsDot11MeshHWMPCompliances,
       "fsDot11MeshHWMPCompliance": fsDot11MeshHWMPCompliance,
       "fsDot11MeshHWMPGroups": fsDot11MeshHWMPGroups,
       "fsDot11MeshHWMPGroup": fsDot11MeshHWMPGroup}
)
