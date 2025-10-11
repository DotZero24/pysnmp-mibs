# SNMP MIB module (FS-SPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-SPAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:34 2025
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

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

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

fsSPANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23)
)
if mibBuilder.loadTexts:
    fsSPANMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSPANMIBObjects_ObjectIdentity = ObjectIdentity
fsSPANMIBObjects = _FsSPANMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1)
)
_FsSPANSessionNum_Type = Integer32
_FsSPANSessionNum_Object = MibScalar
fsSPANSessionNum = _FsSPANSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 1),
    _FsSPANSessionNum_Type()
)
fsSPANSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSPANSessionNum.setStatus("current")
_FsSPANTable_Object = MibTable
fsSPANTable = _FsSPANTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    fsSPANTable.setStatus("current")
_FsSPANEntry_Object = MibTableRow
fsSPANEntry = _FsSPANEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1)
)
fsSPANEntry.setIndexNames(
    (0, "FS-SPAN-MIB", "fsSPANSession"),
    (0, "FS-SPAN-MIB", "fsSPANIfIndex"),
)
if mibBuilder.loadTexts:
    fsSPANEntry.setStatus("current")
_FsSPANSession_Type = Integer32
_FsSPANSession_Object = MibTableColumn
fsSPANSession = _FsSPANSession_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1, 1),
    _FsSPANSession_Type()
)
fsSPANSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSPANSession.setStatus("current")
_FsSPANIfIndex_Type = IfIndex
_FsSPANIfIndex_Object = MibTableColumn
fsSPANIfIndex = _FsSPANIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1, 2),
    _FsSPANIfIndex_Type()
)
fsSPANIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSPANIfIndex.setStatus("current")


class _FsSPANIfRole_Type(Integer32):
    """Custom type fsSPANIfRole based on Integer32"""
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
        *(("span-desc", 1),
          ("span-src-rx", 2),
          ("span-src-tx", 3),
          ("span-src-all", 4))
    )


_FsSPANIfRole_Type.__name__ = "Integer32"
_FsSPANIfRole_Object = MibTableColumn
fsSPANIfRole = _FsSPANIfRole_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1, 3),
    _FsSPANIfRole_Type()
)
fsSPANIfRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSPANIfRole.setStatus("current")
_FsSPANEntryStatus_Type = ConfigStatus
_FsSPANEntryStatus_Object = MibTableColumn
fsSPANEntryStatus = _FsSPANEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1, 4),
    _FsSPANEntryStatus_Type()
)
fsSPANEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSPANEntryStatus.setStatus("current")
_FsSPANMIBConformance_ObjectIdentity = ObjectIdentity
fsSPANMIBConformance = _FsSPANMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3)
)
_FsSPANMIBCompliances_ObjectIdentity = ObjectIdentity
fsSPANMIBCompliances = _FsSPANMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3, 1)
)
_FsSPANMIBGroups_ObjectIdentity = ObjectIdentity
fsSPANMIBGroups = _FsSPANMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3, 2)
)

# Managed Objects groups

fsSPANMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3, 2, 1)
)
fsSPANMIBGroup.setObjects(
      *(("FS-SPAN-MIB", "fsSPANSession"),
        ("FS-SPAN-MIB", "fsSPANIfIndex"),
        ("FS-SPAN-MIB", "fsSPANIfRole"),
        ("FS-SPAN-MIB", "fsSPANEntryStatus"))
)
if mibBuilder.loadTexts:
    fsSPANMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsSPANMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3, 1, 1)
)
fsSPANMIBCompliance.setObjects(
    ("FS-SPAN-MIB", "fsSPANMIBGroup")
)
if mibBuilder.loadTexts:
    fsSPANMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-SPAN-MIB",
    **{"fsSPANMIB": fsSPANMIB,
       "fsSPANMIBObjects": fsSPANMIBObjects,
       "fsSPANSessionNum": fsSPANSessionNum,
       "fsSPANTable": fsSPANTable,
       "fsSPANEntry": fsSPANEntry,
       "fsSPANSession": fsSPANSession,
       "fsSPANIfIndex": fsSPANIfIndex,
       "fsSPANIfRole": fsSPANIfRole,
       "fsSPANEntryStatus": fsSPANEntryStatus,
       "fsSPANMIBConformance": fsSPANMIBConformance,
       "fsSPANMIBCompliances": fsSPANMIBCompliances,
       "fsSPANMIBCompliance": fsSPANMIBCompliance,
       "fsSPANMIBGroups": fsSPANMIBGroups,
       "fsSPANMIBGroup": fsSPANMIBGroup}
)
