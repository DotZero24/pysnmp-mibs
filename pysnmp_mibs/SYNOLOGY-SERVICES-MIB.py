# SNMP MIB module (SYNOLOGY-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-SERVICES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:19 2025
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

synologyService = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 6)
)
if mibBuilder.loadTexts:
    synologyService.setRevisions(
        ("2016-05-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_ServiceTable_Object = MibTable
serviceTable = _ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 6, 1)
)
if mibBuilder.loadTexts:
    serviceTable.setStatus("current")
_ServiceEntry_Object = MibTableRow
serviceEntry = _ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 6, 1, 1)
)
serviceEntry.setIndexNames(
    (0, "SYNOLOGY-SERVICES-MIB", "serviceInfoIndex"),
)
if mibBuilder.loadTexts:
    serviceEntry.setStatus("current")


class _ServiceInfoIndex_Type(Integer32):
    """Custom type serviceInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ServiceInfoIndex_Type.__name__ = "Integer32"
_ServiceInfoIndex_Object = MibTableColumn
serviceInfoIndex = _ServiceInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 6, 1, 1, 1),
    _ServiceInfoIndex_Type()
)
serviceInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceInfoIndex.setStatus("current")
_ServiceName_Type = OctetString
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 6, 1, 1, 2),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceName.setStatus("current")
_ServiceUsers_Type = Integer32
_ServiceUsers_Object = MibTableColumn
serviceUsers = _ServiceUsers_Object(
    (1, 3, 6, 1, 4, 1, 6574, 6, 1, 1, 3),
    _ServiceUsers_Type()
)
serviceUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceUsers.setStatus("current")
_SynologyServiceConformance_ObjectIdentity = ObjectIdentity
synologyServiceConformance = _SynologyServiceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 6, 2)
)
_SynologyServiceCompliances_ObjectIdentity = ObjectIdentity
synologyServiceCompliances = _SynologyServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 6, 2, 1)
)
_SynologyServiceGroups_ObjectIdentity = ObjectIdentity
synologyServiceGroups = _SynologyServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 6, 2, 2)
)

# Managed Objects groups

synologyServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 6, 2, 2, 1)
)
synologyServiceGroup.setObjects(
      *(("SYNOLOGY-SERVICES-MIB", "serviceName"),
        ("SYNOLOGY-SERVICES-MIB", "serviceUsers"))
)
if mibBuilder.loadTexts:
    synologyServiceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

synologyServiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 6, 2, 1, 1)
)
synologyServiceCompliance.setObjects(
    ("SYNOLOGY-SERVICES-MIB", "synologyServiceGroup")
)
if mibBuilder.loadTexts:
    synologyServiceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-SERVICES-MIB",
    **{"synology": synology,
       "synologyService": synologyService,
       "serviceTable": serviceTable,
       "serviceEntry": serviceEntry,
       "serviceInfoIndex": serviceInfoIndex,
       "serviceName": serviceName,
       "serviceUsers": serviceUsers,
       "synologyServiceConformance": synologyServiceConformance,
       "synologyServiceCompliances": synologyServiceCompliances,
       "synologyServiceCompliance": synologyServiceCompliance,
       "synologyServiceGroups": synologyServiceGroups,
       "synologyServiceGroup": synologyServiceGroup}
)
