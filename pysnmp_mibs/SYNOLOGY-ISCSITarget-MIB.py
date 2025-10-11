# SNMP MIB module (SYNOLOGY-ISCSITarget-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-ISCSITarget-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:24 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

synologyiSCSITarget = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 110)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_ISCSITargetTable_Object = MibTable
iSCSITargetTable = _ISCSITargetTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 110, 1)
)
if mibBuilder.loadTexts:
    iSCSITargetTable.setStatus("current")
_ISCSITargetEntry_Object = MibTableRow
iSCSITargetEntry = _ISCSITargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 110, 1, 1)
)
iSCSITargetEntry.setIndexNames(
    (0, "SYNOLOGY-ISCSITarget-MIB", "iSCSITargetInfoIndex"),
)
if mibBuilder.loadTexts:
    iSCSITargetEntry.setStatus("current")


class _ISCSITargetInfoIndex_Type(Integer32):
    """Custom type iSCSITargetInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ISCSITargetInfoIndex_Type.__name__ = "Integer32"
_ISCSITargetInfoIndex_Object = MibTableColumn
iSCSITargetInfoIndex = _ISCSITargetInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 110, 1, 1, 1),
    _ISCSITargetInfoIndex_Type()
)
iSCSITargetInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iSCSITargetInfoIndex.setStatus("current")


class _ISCSITargetName_Type(OctetString):
    """Custom type iSCSITargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ISCSITargetName_Type.__name__ = "OctetString"
_ISCSITargetName_Object = MibTableColumn
iSCSITargetName = _ISCSITargetName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 110, 1, 1, 2),
    _ISCSITargetName_Type()
)
iSCSITargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSITargetName.setStatus("current")


class _ISCSITargetIQN_Type(OctetString):
    """Custom type iSCSITargetIQN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ISCSITargetIQN_Type.__name__ = "OctetString"
_ISCSITargetIQN_Object = MibTableColumn
iSCSITargetIQN = _ISCSITargetIQN_Object(
    (1, 3, 6, 1, 4, 1, 6574, 110, 1, 1, 3),
    _ISCSITargetIQN_Type()
)
iSCSITargetIQN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSITargetIQN.setStatus("current")


class _ISCSITargetConnectionStatus_Type(OctetString):
    """Custom type iSCSITargetConnectionStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_ISCSITargetConnectionStatus_Type.__name__ = "OctetString"
_ISCSITargetConnectionStatus_Object = MibTableColumn
iSCSITargetConnectionStatus = _ISCSITargetConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 110, 1, 1, 4),
    _ISCSITargetConnectionStatus_Type()
)
iSCSITargetConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSITargetConnectionStatus.setStatus("current")
_SynologyiSCSITargetConformance_ObjectIdentity = ObjectIdentity
synologyiSCSITargetConformance = _SynologyiSCSITargetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 110, 2)
)
_SynologyiSCSITargetCompliances_ObjectIdentity = ObjectIdentity
synologyiSCSITargetCompliances = _SynologyiSCSITargetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 110, 2, 1)
)
_SynologyiSCSITargetGroups_ObjectIdentity = ObjectIdentity
synologyiSCSITargetGroups = _SynologyiSCSITargetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 110, 2, 2)
)

# Managed Objects groups

synologyiSCSITargetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 110, 2, 2, 1)
)
synologyiSCSITargetGroup.setObjects(
      *(("SYNOLOGY-ISCSITarget-MIB", "iSCSITargetName"),
        ("SYNOLOGY-ISCSITarget-MIB", "iSCSITargetIQN"),
        ("SYNOLOGY-ISCSITarget-MIB", "iSCSITargetConnectionStatus"))
)
if mibBuilder.loadTexts:
    synologyiSCSITargetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

synologyiSCSITargetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 110, 2, 1, 1)
)
synologyiSCSITargetCompliance.setObjects(
    ("SYNOLOGY-ISCSITarget-MIB", "synologyiSCSITargetGroup")
)
if mibBuilder.loadTexts:
    synologyiSCSITargetCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-ISCSITarget-MIB",
    **{"synology": synology,
       "synologyiSCSITarget": synologyiSCSITarget,
       "iSCSITargetTable": iSCSITargetTable,
       "iSCSITargetEntry": iSCSITargetEntry,
       "iSCSITargetInfoIndex": iSCSITargetInfoIndex,
       "iSCSITargetName": iSCSITargetName,
       "iSCSITargetIQN": iSCSITargetIQN,
       "iSCSITargetConnectionStatus": iSCSITargetConnectionStatus,
       "synologyiSCSITargetConformance": synologyiSCSITargetConformance,
       "synologyiSCSITargetCompliances": synologyiSCSITargetCompliances,
       "synologyiSCSITargetCompliance": synologyiSCSITargetCompliance,
       "synologyiSCSITargetGroups": synologyiSCSITargetGroups,
       "synologyiSCSITargetGroup": synologyiSCSITargetGroup}
)
