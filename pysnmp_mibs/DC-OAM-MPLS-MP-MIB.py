# SNMP MIB module (DC-OAM-MPLS-MP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DC-OAM-MPLS-MP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:41 2025
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

(AdminStatus,
 BaseOperStatus,
 NumericIndex) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "AdminStatus",
    "BaseOperStatus",
    "NumericIndex")

(oammEntApplIndex,) = mibBuilder.importSymbols(
    "DC-OAMM-MIB",
    "oammEntApplIndex")

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

mplsMpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 16)
)
if mibBuilder.loadTexts:
    mplsMpMib.setRevisions(
        ("2014-12-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_Opx_ObjectIdentity = ObjectIdentity
opx = _Opx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10)
)
_MplsMpObjects_ObjectIdentity = ObjectIdentity
mplsMpObjects = _MplsMpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1)
)
_MplsMpTable_Object = MibTable
mplsMpTable = _MplsMpTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2)
)
if mibBuilder.loadTexts:
    mplsMpTable.setStatus("current")
_MplsMpEntry_Object = MibTableRow
mplsMpEntry = _MplsMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1)
)
mplsMpEntry.setIndexNames(
    (0, "DC-OAMM-MIB", "oammEntApplIndex"),
    (0, "DC-OAM-MPLS-MP-MIB", "mplsMpIndex"),
)
if mibBuilder.loadTexts:
    mplsMpEntry.setStatus("current")
_MplsMpIndex_Type = NumericIndex
_MplsMpIndex_Object = MibTableColumn
mplsMpIndex = _MplsMpIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 1),
    _MplsMpIndex_Type()
)
mplsMpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsMpIndex.setStatus("current")
_MplsMpRowStatus_Type = RowStatus
_MplsMpRowStatus_Object = MibTableColumn
mplsMpRowStatus = _MplsMpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 2),
    _MplsMpRowStatus_Type()
)
mplsMpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsMpRowStatus.setStatus("current")


class _MplsMpAdminStatus_Type(AdminStatus):
    """Custom type mplsMpAdminStatus based on AdminStatus"""
    defaultValue = 1


_MplsMpAdminStatus_Type.__name__ = "AdminStatus"
_MplsMpAdminStatus_Object = MibTableColumn
mplsMpAdminStatus = _MplsMpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 3),
    _MplsMpAdminStatus_Type()
)
mplsMpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsMpAdminStatus.setStatus("current")
_MplsMpOperStatus_Type = BaseOperStatus
_MplsMpOperStatus_Object = MibTableColumn
mplsMpOperStatus = _MplsMpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 4),
    _MplsMpOperStatus_Type()
)
mplsMpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsMpOperStatus.setStatus("current")


class _MplsMpProactiveBfdContCheck_Type(TruthValue):
    """Custom type mplsMpProactiveBfdContCheck based on TruthValue"""
    defaultValue = 2


_MplsMpProactiveBfdContCheck_Type.__name__ = "TruthValue"
_MplsMpProactiveBfdContCheck_Object = MibTableColumn
mplsMpProactiveBfdContCheck = _MplsMpProactiveBfdContCheck_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 5),
    _MplsMpProactiveBfdContCheck_Type()
)
mplsMpProactiveBfdContCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsMpProactiveBfdContCheck.setStatus("current")


class _MplsMpProactiveBfdConnVerif_Type(TruthValue):
    """Custom type mplsMpProactiveBfdConnVerif based on TruthValue"""
    defaultValue = 2


_MplsMpProactiveBfdConnVerif_Type.__name__ = "TruthValue"
_MplsMpProactiveBfdConnVerif_Object = MibTableColumn
mplsMpProactiveBfdConnVerif = _MplsMpProactiveBfdConnVerif_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 6),
    _MplsMpProactiveBfdConnVerif_Type()
)
mplsMpProactiveBfdConnVerif.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsMpProactiveBfdConnVerif.setStatus("current")


class _MplsMpLoopback_Type(TruthValue):
    """Custom type mplsMpLoopback based on TruthValue"""
    defaultValue = 2


_MplsMpLoopback_Type.__name__ = "TruthValue"
_MplsMpLoopback_Object = MibTableColumn
mplsMpLoopback = _MplsMpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 1, 2, 1, 100),
    _MplsMpLoopback_Type()
)
mplsMpLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsMpLoopback.setStatus("current")
_MplsMpConformance_ObjectIdentity = ObjectIdentity
mplsMpConformance = _MplsMpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 2)
)
_MplsMpGroups_ObjectIdentity = ObjectIdentity
mplsMpGroups = _MplsMpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 1)
)
_MplsMpCompliances_ObjectIdentity = ObjectIdentity
mplsMpCompliances = _MplsMpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 2)
)

# Managed Objects groups

mplsMpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 1, 1)
)
mplsMpGeneralGroup.setObjects(
      *(("DC-OAM-MPLS-MP-MIB", "mplsMpRowStatus"),
        ("DC-OAM-MPLS-MP-MIB", "mplsMpAdminStatus"),
        ("DC-OAM-MPLS-MP-MIB", "mplsMpOperStatus"),
        ("DC-OAM-MPLS-MP-MIB", "mplsMpProactiveBfdContCheck"),
        ("DC-OAM-MPLS-MP-MIB", "mplsMpProactiveBfdConnVerif"),
        ("DC-OAM-MPLS-MP-MIB", "mplsMpLoopback"))
)
if mibBuilder.loadTexts:
    mplsMpGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsMpModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 2, 1)
)
mplsMpModuleFullCompliance.setObjects(
    ("DC-OAM-MPLS-MP-MIB", "mplsMpGeneralGroup")
)
if mibBuilder.loadTexts:
    mplsMpModuleFullCompliance.setStatus(
        "current"
    )

mplsMpModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 16, 2, 2, 2)
)
mplsMpModuleReadOnlyCompliance.setObjects(
    ("DC-OAM-MPLS-MP-MIB", "mplsMpGeneralGroup")
)
if mibBuilder.loadTexts:
    mplsMpModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-OAM-MPLS-MP-MIB",
    **{"nbase": nbase,
       "opx": opx,
       "mplsMpMib": mplsMpMib,
       "mplsMpObjects": mplsMpObjects,
       "mplsMpTable": mplsMpTable,
       "mplsMpEntry": mplsMpEntry,
       "mplsMpIndex": mplsMpIndex,
       "mplsMpRowStatus": mplsMpRowStatus,
       "mplsMpAdminStatus": mplsMpAdminStatus,
       "mplsMpOperStatus": mplsMpOperStatus,
       "mplsMpProactiveBfdContCheck": mplsMpProactiveBfdContCheck,
       "mplsMpProactiveBfdConnVerif": mplsMpProactiveBfdConnVerif,
       "mplsMpLoopback": mplsMpLoopback,
       "mplsMpConformance": mplsMpConformance,
       "mplsMpGroups": mplsMpGroups,
       "mplsMpGeneralGroup": mplsMpGeneralGroup,
       "mplsMpCompliances": mplsMpCompliances,
       "mplsMpModuleFullCompliance": mplsMpModuleFullCompliance,
       "mplsMpModuleReadOnlyCompliance": mplsMpModuleReadOnlyCompliance}
)
