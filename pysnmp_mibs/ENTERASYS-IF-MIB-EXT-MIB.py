# SNMP MIB module (ENTERASYS-IF-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-IF-MIB-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:28 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

etsysIfMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57)
)
if mibBuilder.loadTexts:
    etsysIfMibExtMIB.setRevisions(
        ("2015-04-14 12:39",
         "2014-07-24 13:22",
         "2013-04-12 13:14",
         "2013-02-11 18:14",
         "2012-02-02 20:08",
         "2011-12-07 15:58",
         "2011-10-25 19:48",
         "2011-06-08 12:12",
         "2011-05-12 14:15",
         "2005-01-13 21:35")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysIfOperStatusCauses(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("adminStatus", 0),
          ("linkLoss", 1),
          ("linkFlap", 2),
          ("self", 3),
          ("initialization", 4),
          ("flowLimiting", 5),
          ("policy", 6),
          ("classOfService", 7),
          ("ieee8021x", 8),
          ("ieee8023lag", 9),
          ("enetOam", 10),
          ("enetOamLb", 11),
          ("macLock", 12),
          ("chassisBonding", 13),
          ("linkState", 14),
          ("enetOamUld", 15),
          ("txqMonitor", 16),
          ("priorityFlowControl", 17),
          ("macSec", 18))
    )


# MIB Managed Objects in the order of their OIDs

_EtsysIfMibExtObjects_ObjectIdentity = ObjectIdentity
etsysIfMibExtObjects = _EtsysIfMibExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1)
)
_EtsysIfMibExtSystem_ObjectIdentity = ObjectIdentity
etsysIfMibExtSystem = _EtsysIfMibExtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1)
)


class _EtsysIfOperStateLinkChange_Type(EnabledStatus):
    """Custom type etsysIfOperStateLinkChange based on EnabledStatus"""
    defaultValue = 2


_EtsysIfOperStateLinkChange_Type.__name__ = "EnabledStatus"
_EtsysIfOperStateLinkChange_Object = MibScalar
etsysIfOperStateLinkChange = _EtsysIfOperStateLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1, 1),
    _EtsysIfOperStateLinkChange_Type()
)
etsysIfOperStateLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIfOperStateLinkChange.setStatus("current")
_EtsysIfMibExtInterface_ObjectIdentity = ObjectIdentity
etsysIfMibExtInterface = _EtsysIfMibExtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2)
)
_EtsysInterfaceExtTable_Object = MibTable
etsysInterfaceExtTable = _EtsysInterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysInterfaceExtTable.setStatus("current")
_EtsysInterfaceExtEntry_Object = MibTableRow
etsysInterfaceExtEntry = _EtsysInterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysInterfaceExtEntry.setStatus("current")
_EtsysIfOperStatusCause_Type = EtsysIfOperStatusCauses
_EtsysIfOperStatusCause_Object = MibTableColumn
etsysIfOperStatusCause = _EtsysIfOperStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1, 1),
    _EtsysIfOperStatusCause_Type()
)
etsysIfOperStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIfOperStatusCause.setStatus("current")
_EtsysIfMibExtConformance_ObjectIdentity = ObjectIdentity
etsysIfMibExtConformance = _EtsysIfMibExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2)
)
_EtsysIfMibExtGroups_ObjectIdentity = ObjectIdentity
etsysIfMibExtGroups = _EtsysIfMibExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1)
)
_EtsysIfMibExtCompliances_ObjectIdentity = ObjectIdentity
etsysIfMibExtCompliances = _EtsysIfMibExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2)
)
ifEntry.registerAugmentions(
    ("ENTERASYS-IF-MIB-EXT-MIB",
     "etsysInterfaceExtEntry")
)
etsysInterfaceExtEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

etsysIfMibExtOperLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 1)
)
etsysIfMibExtOperLinkGroup.setObjects(
    ("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStateLinkChange")
)
if mibBuilder.loadTexts:
    etsysIfMibExtOperLinkGroup.setStatus("current")

etsysIfMibExtOperStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 2)
)
etsysIfMibExtOperStatusGroup.setObjects(
    ("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStatusCause")
)
if mibBuilder.loadTexts:
    etsysIfMibExtOperStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysIfMibExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2, 1)
)
etsysIfMibExtCompliance.setObjects(
      *(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfMibExtOperLinkGroup"),
        ("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfMibExtOperStatusGroup"))
)
if mibBuilder.loadTexts:
    etsysIfMibExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IF-MIB-EXT-MIB",
    **{"EtsysIfOperStatusCauses": EtsysIfOperStatusCauses,
       "etsysIfMibExtMIB": etsysIfMibExtMIB,
       "etsysIfMibExtObjects": etsysIfMibExtObjects,
       "etsysIfMibExtSystem": etsysIfMibExtSystem,
       "etsysIfOperStateLinkChange": etsysIfOperStateLinkChange,
       "etsysIfMibExtInterface": etsysIfMibExtInterface,
       "etsysInterfaceExtTable": etsysInterfaceExtTable,
       "etsysInterfaceExtEntry": etsysInterfaceExtEntry,
       "etsysIfOperStatusCause": etsysIfOperStatusCause,
       "etsysIfMibExtConformance": etsysIfMibExtConformance,
       "etsysIfMibExtGroups": etsysIfMibExtGroups,
       "etsysIfMibExtOperLinkGroup": etsysIfMibExtOperLinkGroup,
       "etsysIfMibExtOperStatusGroup": etsysIfMibExtOperStatusGroup,
       "etsysIfMibExtCompliances": etsysIfMibExtCompliances,
       "etsysIfMibExtCompliance": etsysIfMibExtCompliance}
)
