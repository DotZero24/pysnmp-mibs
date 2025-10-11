# SNMP MIB module (QTECH-SPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SPAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:20 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
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

qtechSPANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23)
)
if mibBuilder.loadTexts:
    qtechSPANMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechSPANMIBObjects_ObjectIdentity = ObjectIdentity
qtechSPANMIBObjects = _QtechSPANMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1)
)
_QtechSPANSessionNum_Type = Integer32
_QtechSPANSessionNum_Object = MibScalar
qtechSPANSessionNum = _QtechSPANSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 1),
    _QtechSPANSessionNum_Type()
)
qtechSPANSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSPANSessionNum.setStatus("current")
_QtechSPANTable_Object = MibTable
qtechSPANTable = _QtechSPANTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    qtechSPANTable.setStatus("current")
_QtechSPANEntry_Object = MibTableRow
qtechSPANEntry = _QtechSPANEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1)
)
qtechSPANEntry.setIndexNames(
    (0, "QTECH-SPAN-MIB", "qtechSPANSession"),
    (0, "QTECH-SPAN-MIB", "qtechSPANIfIndex"),
)
if mibBuilder.loadTexts:
    qtechSPANEntry.setStatus("current")
_QtechSPANSession_Type = Integer32
_QtechSPANSession_Object = MibTableColumn
qtechSPANSession = _QtechSPANSession_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1, 1),
    _QtechSPANSession_Type()
)
qtechSPANSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSPANSession.setStatus("current")
_QtechSPANIfIndex_Type = IfIndex
_QtechSPANIfIndex_Object = MibTableColumn
qtechSPANIfIndex = _QtechSPANIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1, 2),
    _QtechSPANIfIndex_Type()
)
qtechSPANIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSPANIfIndex.setStatus("current")


class _QtechSPANIfRole_Type(Integer32):
    """Custom type qtechSPANIfRole based on Integer32"""
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


_QtechSPANIfRole_Type.__name__ = "Integer32"
_QtechSPANIfRole_Object = MibTableColumn
qtechSPANIfRole = _QtechSPANIfRole_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1, 3),
    _QtechSPANIfRole_Type()
)
qtechSPANIfRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSPANIfRole.setStatus("current")
_QtechSPANEntryStatus_Type = ConfigStatus
_QtechSPANEntryStatus_Object = MibTableColumn
qtechSPANEntryStatus = _QtechSPANEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1, 4),
    _QtechSPANEntryStatus_Type()
)
qtechSPANEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSPANEntryStatus.setStatus("current")
_QtechSPANMIBConformance_ObjectIdentity = ObjectIdentity
qtechSPANMIBConformance = _QtechSPANMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3)
)
_QtechSPANMIBCompliances_ObjectIdentity = ObjectIdentity
qtechSPANMIBCompliances = _QtechSPANMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3, 1)
)
_QtechSPANMIBGroups_ObjectIdentity = ObjectIdentity
qtechSPANMIBGroups = _QtechSPANMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3, 2)
)

# Managed Objects groups

qtechSPANMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3, 2, 1)
)
qtechSPANMIBGroup.setObjects(
      *(("QTECH-SPAN-MIB", "qtechSPANSession"),
        ("QTECH-SPAN-MIB", "qtechSPANIfIndex"),
        ("QTECH-SPAN-MIB", "qtechSPANIfRole"),
        ("QTECH-SPAN-MIB", "qtechSPANEntryStatus"))
)
if mibBuilder.loadTexts:
    qtechSPANMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechSPANMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3, 1, 1)
)
qtechSPANMIBCompliance.setObjects(
    ("QTECH-SPAN-MIB", "qtechSPANMIBGroup")
)
if mibBuilder.loadTexts:
    qtechSPANMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SPAN-MIB",
    **{"qtechSPANMIB": qtechSPANMIB,
       "qtechSPANMIBObjects": qtechSPANMIBObjects,
       "qtechSPANSessionNum": qtechSPANSessionNum,
       "qtechSPANTable": qtechSPANTable,
       "qtechSPANEntry": qtechSPANEntry,
       "qtechSPANSession": qtechSPANSession,
       "qtechSPANIfIndex": qtechSPANIfIndex,
       "qtechSPANIfRole": qtechSPANIfRole,
       "qtechSPANEntryStatus": qtechSPANEntryStatus,
       "qtechSPANMIBConformance": qtechSPANMIBConformance,
       "qtechSPANMIBCompliances": qtechSPANMIBCompliances,
       "qtechSPANMIBCompliance": qtechSPANMIBCompliance,
       "qtechSPANMIBGroups": qtechSPANMIBGroups,
       "qtechSPANMIBGroup": qtechSPANMIBGroup}
)
