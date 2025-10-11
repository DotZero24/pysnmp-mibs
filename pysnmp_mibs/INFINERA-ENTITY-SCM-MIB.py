# SNMP MIB module (INFINERA-ENTITY-SCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-SCM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:11 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatTenths,
 InfnEqptType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnEqptType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

scmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ScmTable_Object = MibTable
scmTable = _ScmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1)
)
if mibBuilder.loadTexts:
    scmTable.setStatus("current")
_ScmEntry_Object = MibTableRow
scmEntry = _ScmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1)
)
scmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    scmEntry.setStatus("current")
_ScmMoId_Type = DisplayString
_ScmMoId_Object = MibTableColumn
scmMoId = _ScmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 1),
    _ScmMoId_Type()
)
scmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmMoId.setStatus("current")
_ScmProvEqptType_Type = InfnEqptType
_ScmProvEqptType_Object = MibTableColumn
scmProvEqptType = _ScmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 2),
    _ScmProvEqptType_Type()
)
scmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmProvEqptType.setStatus("current")
_ScmIdlerVoaAttenuation_Type = FloatTenths
_ScmIdlerVoaAttenuation_Object = MibTableColumn
scmIdlerVoaAttenuation = _ScmIdlerVoaAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 3),
    _ScmIdlerVoaAttenuation_Type()
)
scmIdlerVoaAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmIdlerVoaAttenuation.setStatus("current")
_ScmProvisionedRemoteSCM_Type = DisplayString
_ScmProvisionedRemoteSCM_Object = MibTableColumn
scmProvisionedRemoteSCM = _ScmProvisionedRemoteSCM_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 4),
    _ScmProvisionedRemoteSCM_Type()
)
scmProvisionedRemoteSCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmProvisionedRemoteSCM.setStatus("current")
_ScmAssociatedDegree_Type = DisplayString
_ScmAssociatedDegree_Object = MibTableColumn
scmAssociatedDegree = _ScmAssociatedDegree_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 5),
    _ScmAssociatedDegree_Type()
)
scmAssociatedDegree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmAssociatedDegree.setStatus("current")
_ScmRowStatus_Type = RowStatus
_ScmRowStatus_Object = MibTableColumn
scmRowStatus = _ScmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 1, 1, 6),
    _ScmRowStatus_Type()
)
scmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scmRowStatus.setStatus("current")
_ScmConformance_ObjectIdentity = ObjectIdentity
scmConformance = _ScmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3)
)
_ScmCompliances_ObjectIdentity = ObjectIdentity
scmCompliances = _ScmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3, 1)
)
_ScmGroups_ObjectIdentity = ObjectIdentity
scmGroups = _ScmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3, 2)
)

# Managed Objects groups

scmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3, 2, 1)
)
scmGroup.setObjects(
      *(("INFINERA-ENTITY-SCM-MIB", "scmMoId"),
        ("INFINERA-ENTITY-SCM-MIB", "scmProvEqptType"),
        ("INFINERA-ENTITY-SCM-MIB", "scmRowStatus"),
        ("INFINERA-ENTITY-SCM-MIB", "scmIdlerVoaAttenuation"),
        ("INFINERA-ENTITY-SCM-MIB", "scmProvisionedRemoteSCM"),
        ("INFINERA-ENTITY-SCM-MIB", "scmAssociatedDegree"))
)
if mibBuilder.loadTexts:
    scmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

scmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 18, 3, 1, 1)
)
scmCompliance.setObjects(
    ("INFINERA-ENTITY-SCM-MIB", "scmGroup")
)
if mibBuilder.loadTexts:
    scmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-SCM-MIB",
    **{"scmMIB": scmMIB,
       "scmTable": scmTable,
       "scmEntry": scmEntry,
       "scmMoId": scmMoId,
       "scmProvEqptType": scmProvEqptType,
       "scmIdlerVoaAttenuation": scmIdlerVoaAttenuation,
       "scmProvisionedRemoteSCM": scmProvisionedRemoteSCM,
       "scmAssociatedDegree": scmAssociatedDegree,
       "scmRowStatus": scmRowStatus,
       "scmConformance": scmConformance,
       "scmCompliances": scmCompliances,
       "scmCompliance": scmCompliance,
       "scmGroups": scmGroups,
       "scmGroup": scmGroup}
)
