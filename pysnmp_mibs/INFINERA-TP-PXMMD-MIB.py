# SNMP MIB module (INFINERA-TP-PXMMD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMMD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:44 2025
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

(InfnMDNameFormat,
 InfnMHFCreationCriteria,
 InfnSenderIDTLV) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnMDNameFormat",
    "InfnMHFCreationCriteria",
    "InfnSenderIDTLV")

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

mdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MdTable_Object = MibTable
mdTable = _MdTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1)
)
if mibBuilder.loadTexts:
    mdTable.setStatus("current")
_MdEntry_Object = MibTableRow
mdEntry = _MdEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1)
)
mdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mdEntry.setStatus("current")
_MdName_Type = DisplayString
_MdName_Object = MibTableColumn
mdName = _MdName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 1),
    _MdName_Type()
)
mdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdName.setStatus("current")
_MdLevel_Type = Integer32
_MdLevel_Object = MibTableColumn
mdLevel = _MdLevel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 2),
    _MdLevel_Type()
)
mdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdLevel.setStatus("current")
_MdMDNameFormat_Type = InfnMDNameFormat
_MdMDNameFormat_Object = MibTableColumn
mdMDNameFormat = _MdMDNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 3),
    _MdMDNameFormat_Type()
)
mdMDNameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdMDNameFormat.setStatus("current")
_MdMHFCreationCriteria_Type = InfnMHFCreationCriteria
_MdMHFCreationCriteria_Object = MibTableColumn
mdMHFCreationCriteria = _MdMHFCreationCriteria_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 4),
    _MdMHFCreationCriteria_Type()
)
mdMHFCreationCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdMHFCreationCriteria.setStatus("current")
_MdSenderIDTLV_Type = InfnSenderIDTLV
_MdSenderIDTLV_Object = MibTableColumn
mdSenderIDTLV = _MdSenderIDTLV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 5),
    _MdSenderIDTLV_Type()
)
mdSenderIDTLV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdSenderIDTLV.setStatus("current")
_MdConformance_ObjectIdentity = ObjectIdentity
mdConformance = _MdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3)
)
_MdCompliances_ObjectIdentity = ObjectIdentity
mdCompliances = _MdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3, 1)
)
_MdGroups_ObjectIdentity = ObjectIdentity
mdGroups = _MdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3, 2)
)

# Managed Objects groups

mdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3, 2, 1)
)
mdGroup.setObjects(
      *(("INFINERA-TP-PXMMD-MIB", "mdName"),
        ("INFINERA-TP-PXMMD-MIB", "mdLevel"),
        ("INFINERA-TP-PXMMD-MIB", "mdMDNameFormat"),
        ("INFINERA-TP-PXMMD-MIB", "mdMHFCreationCriteria"),
        ("INFINERA-TP-PXMMD-MIB", "mdSenderIDTLV"))
)
if mibBuilder.loadTexts:
    mdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3, 1, 1)
)
mdCompliance.setObjects(
    ("INFINERA-TP-PXMMD-MIB", "mdGroup")
)
if mibBuilder.loadTexts:
    mdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMMD-MIB",
    **{"mdMIB": mdMIB,
       "mdTable": mdTable,
       "mdEntry": mdEntry,
       "mdName": mdName,
       "mdLevel": mdLevel,
       "mdMDNameFormat": mdMDNameFormat,
       "mdMHFCreationCriteria": mdMHFCreationCriteria,
       "mdSenderIDTLV": mdSenderIDTLV,
       "mdConformance": mdConformance,
       "mdCompliances": mdCompliances,
       "mdCompliance": mdCompliance,
       "mdGroups": mdGroups,
       "mdGroup": mdGroup}
)
