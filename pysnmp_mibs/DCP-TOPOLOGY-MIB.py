# SNMP MIB module (DCP-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/DCP-TOPOLOGY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:31:50 2025
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

(dcpGeneric,) = mibBuilder.importSymbols(
    "DCP-MIB",
    "dcpGeneric")

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

dcpTopology = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5)
)
if mibBuilder.loadTexts:
    dcpTopology.setRevisions(
        ("2021-12-30 08:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcpTopologyObjects_ObjectIdentity = ObjectIdentity
dcpTopologyObjects = _DcpTopologyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1)
)
_DcpTopologyInternalTable_Object = MibTable
dcpTopologyInternalTable = _DcpTopologyInternalTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dcpTopologyInternalTable.setStatus("current")
_DcpTopologyInternalEntry_Object = MibTableRow
dcpTopologyInternalEntry = _DcpTopologyInternalEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1, 1)
)
dcpTopologyInternalEntry.setIndexNames(
    (0, "DCP-TOPOLOGY-MIB", "dcpTopologyInternalId"),
)
if mibBuilder.loadTexts:
    dcpTopologyInternalEntry.setStatus("current")


class _DcpTopologyInternalId_Type(Unsigned32):
    """Custom type dcpTopologyInternalId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_DcpTopologyInternalId_Type.__name__ = "Unsigned32"
_DcpTopologyInternalId_Object = MibTableColumn
dcpTopologyInternalId = _DcpTopologyInternalId_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1, 1, 1),
    _DcpTopologyInternalId_Type()
)
dcpTopologyInternalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcpTopologyInternalId.setStatus("current")
_DcpTopologyInternalSource_Type = DisplayString
_DcpTopologyInternalSource_Object = MibTableColumn
dcpTopologyInternalSource = _DcpTopologyInternalSource_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1, 1, 2),
    _DcpTopologyInternalSource_Type()
)
dcpTopologyInternalSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpTopologyInternalSource.setStatus("current")
_DcpTopologyInternalDestination_Type = DisplayString
_DcpTopologyInternalDestination_Object = MibTableColumn
dcpTopologyInternalDestination = _DcpTopologyInternalDestination_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 1, 1, 1, 3),
    _DcpTopologyInternalDestination_Type()
)
dcpTopologyInternalDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpTopologyInternalDestination.setStatus("current")
_DcpTopologyMIBCompliance_ObjectIdentity = ObjectIdentity
dcpTopologyMIBCompliance = _DcpTopologyMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2)
)
_DcpTopologyMIBGroups_ObjectIdentity = ObjectIdentity
dcpTopologyMIBGroups = _DcpTopologyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2, 1)
)
_DcpTopologyMIBCompliances_ObjectIdentity = ObjectIdentity
dcpTopologyMIBCompliances = _DcpTopologyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2, 2)
)

# Managed Objects groups

dcpTopologyTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2, 1, 1)
)
dcpTopologyTableGroupV1.setObjects(
      *(("DCP-TOPOLOGY-MIB", "dcpTopologyInternalSource"),
        ("DCP-TOPOLOGY-MIB", "dcpTopologyInternalDestination"))
)
if mibBuilder.loadTexts:
    dcpTopologyTableGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dcpTopologyBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 5, 2, 2, 1)
)
dcpTopologyBasicComplV1.setObjects(
    ("DCP-TOPOLOGY-MIB", "dcpTopologyTableGroupV1")
)
if mibBuilder.loadTexts:
    dcpTopologyBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCP-TOPOLOGY-MIB",
    **{"dcpTopology": dcpTopology,
       "dcpTopologyObjects": dcpTopologyObjects,
       "dcpTopologyInternalTable": dcpTopologyInternalTable,
       "dcpTopologyInternalEntry": dcpTopologyInternalEntry,
       "dcpTopologyInternalId": dcpTopologyInternalId,
       "dcpTopologyInternalSource": dcpTopologyInternalSource,
       "dcpTopologyInternalDestination": dcpTopologyInternalDestination,
       "dcpTopologyMIBCompliance": dcpTopologyMIBCompliance,
       "dcpTopologyMIBGroups": dcpTopologyMIBGroups,
       "dcpTopologyTableGroupV1": dcpTopologyTableGroupV1,
       "dcpTopologyMIBCompliances": dcpTopologyMIBCompliances,
       "dcpTopologyBasicComplV1": dcpTopologyBasicComplV1}
)
