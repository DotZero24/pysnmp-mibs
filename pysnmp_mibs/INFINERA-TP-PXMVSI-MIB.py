# SNMP MIB module (INFINERA-TP-PXMVSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMVSI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:03 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnVlanLearningMode,
 InfnVsiCreationType,
 InfnVsiMacLimitAction,
 InfnVsiType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnVlanLearningMode",
    "InfnVsiCreationType",
    "InfnVsiMacLimitAction",
    "InfnVsiType")

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

vsiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VsiTable_Object = MibTable
vsiTable = _VsiTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1)
)
if mibBuilder.loadTexts:
    vsiTable.setStatus("current")
_VsiEntry_Object = MibTableRow
vsiEntry = _VsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1)
)
vsiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vsiEntry.setStatus("current")
_VsiType_Type = InfnVsiType
_VsiType_Object = MibTableColumn
vsiType = _VsiType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1, 1),
    _VsiType_Type()
)
vsiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiType.setStatus("current")
_VsiMTUSize_Type = Integer32
_VsiMTUSize_Object = MibTableColumn
vsiMTUSize = _VsiMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1, 2),
    _VsiMTUSize_Type()
)
vsiMTUSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiMTUSize.setStatus("current")
_VsiServiceId_Type = DisplayString
_VsiServiceId_Object = MibTableColumn
vsiServiceId = _VsiServiceId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1, 3),
    _VsiServiceId_Type()
)
vsiServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiServiceId.setStatus("current")
_VsiCreationType_Type = InfnVsiCreationType
_VsiCreationType_Object = MibTableColumn
vsiCreationType = _VsiCreationType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1, 4),
    _VsiCreationType_Type()
)
vsiCreationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiCreationType.setStatus("current")


class _VsiVlanLearning_Type(Integer32):
    """Custom type vsiVlanLearning based on Integer32"""
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


_VsiVlanLearning_Type.__name__ = "Integer32"
_VsiVlanLearning_Object = MibTableColumn
vsiVlanLearning = _VsiVlanLearning_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1, 5),
    _VsiVlanLearning_Type()
)
vsiVlanLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiVlanLearning.setStatus("current")
_VsiVlanLearningMode_Type = InfnVlanLearningMode
_VsiVlanLearningMode_Object = MibTableColumn
vsiVlanLearningMode = _VsiVlanLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1, 6),
    _VsiVlanLearningMode_Type()
)
vsiVlanLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiVlanLearningMode.setStatus("current")
_VsiMacLimitVsi_Type = Integer32
_VsiMacLimitVsi_Object = MibTableColumn
vsiMacLimitVsi = _VsiMacLimitVsi_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1, 7),
    _VsiMacLimitVsi_Type()
)
vsiMacLimitVsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiMacLimitVsi.setStatus("current")
_VsiMacLimitActionVsi_Type = InfnVsiMacLimitAction
_VsiMacLimitActionVsi_Object = MibTableColumn
vsiMacLimitActionVsi = _VsiMacLimitActionVsi_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1, 8),
    _VsiMacLimitActionVsi_Type()
)
vsiMacLimitActionVsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiMacLimitActionVsi.setStatus("current")


class _VsiMacLimitNotifyVsi_Type(Integer32):
    """Custom type vsiMacLimitNotifyVsi based on Integer32"""
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


_VsiMacLimitNotifyVsi_Type.__name__ = "Integer32"
_VsiMacLimitNotifyVsi_Object = MibTableColumn
vsiMacLimitNotifyVsi = _VsiMacLimitNotifyVsi_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 1, 1, 9),
    _VsiMacLimitNotifyVsi_Type()
)
vsiMacLimitNotifyVsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsiMacLimitNotifyVsi.setStatus("current")
_VsiConformance_ObjectIdentity = ObjectIdentity
vsiConformance = _VsiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 3)
)
_VsiCompliances_ObjectIdentity = ObjectIdentity
vsiCompliances = _VsiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 3, 1)
)
_VsiGroups_ObjectIdentity = ObjectIdentity
vsiGroups = _VsiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 3, 2)
)

# Managed Objects groups

vsiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 3, 2, 1)
)
vsiGroup.setObjects(
      *(("INFINERA-TP-PXMVSI-MIB", "vsiType"),
        ("INFINERA-TP-PXMVSI-MIB", "vsiMTUSize"),
        ("INFINERA-TP-PXMVSI-MIB", "vsiServiceId"),
        ("INFINERA-TP-PXMVSI-MIB", "vsiCreationType"),
        ("INFINERA-TP-PXMVSI-MIB", "vsiVlanLearning"),
        ("INFINERA-TP-PXMVSI-MIB", "vsiVlanLearningMode"),
        ("INFINERA-TP-PXMVSI-MIB", "vsiMacLimitVsi"),
        ("INFINERA-TP-PXMVSI-MIB", "vsiMacLimitActionVsi"),
        ("INFINERA-TP-PXMVSI-MIB", "vsiMacLimitNotifyVsi"))
)
if mibBuilder.loadTexts:
    vsiGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vsiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 70, 3, 1, 1)
)
vsiCompliance.setObjects(
    ("INFINERA-TP-PXMVSI-MIB", "vsiGroup")
)
if mibBuilder.loadTexts:
    vsiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMVSI-MIB",
    **{"vsiMIB": vsiMIB,
       "vsiTable": vsiTable,
       "vsiEntry": vsiEntry,
       "vsiType": vsiType,
       "vsiMTUSize": vsiMTUSize,
       "vsiServiceId": vsiServiceId,
       "vsiCreationType": vsiCreationType,
       "vsiVlanLearning": vsiVlanLearning,
       "vsiVlanLearningMode": vsiVlanLearningMode,
       "vsiMacLimitVsi": vsiMacLimitVsi,
       "vsiMacLimitActionVsi": vsiMacLimitActionVsi,
       "vsiMacLimitNotifyVsi": vsiMacLimitNotifyVsi,
       "vsiConformance": vsiConformance,
       "vsiCompliances": vsiCompliances,
       "vsiCompliance": vsiCompliance,
       "vsiGroups": vsiGroups,
       "vsiGroup": vsiGroup}
)
