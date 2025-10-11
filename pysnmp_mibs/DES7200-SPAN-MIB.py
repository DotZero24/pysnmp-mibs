# SNMP MIB module (DES7200-SPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-SPAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:18 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "DES7200-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mySPANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23)
)
if mibBuilder.loadTexts:
    mySPANMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MySPANMIBObjects_ObjectIdentity = ObjectIdentity
mySPANMIBObjects = _MySPANMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1)
)
_MySPANSessionNum_Type = Integer32
_MySPANSessionNum_Object = MibScalar
mySPANSessionNum = _MySPANSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 1),
    _MySPANSessionNum_Type()
)
mySPANSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySPANSessionNum.setStatus("current")
_MySPANTable_Object = MibTable
mySPANTable = _MySPANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2)
)
if mibBuilder.loadTexts:
    mySPANTable.setStatus("current")
_MySPANEntry_Object = MibTableRow
mySPANEntry = _MySPANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1)
)
mySPANEntry.setIndexNames(
    (0, "DES7200-SPAN-MIB", "mySPANSession"),
    (0, "DES7200-SPAN-MIB", "mySPANIfIndex"),
)
if mibBuilder.loadTexts:
    mySPANEntry.setStatus("current")
_MySPANSession_Type = Integer32
_MySPANSession_Object = MibTableColumn
mySPANSession = _MySPANSession_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1, 1),
    _MySPANSession_Type()
)
mySPANSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySPANSession.setStatus("current")
_MySPANIfIndex_Type = IfIndex
_MySPANIfIndex_Object = MibTableColumn
mySPANIfIndex = _MySPANIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1, 2),
    _MySPANIfIndex_Type()
)
mySPANIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySPANIfIndex.setStatus("current")


class _MySPANIfRole_Type(Integer32):
    """Custom type mySPANIfRole based on Integer32"""
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


_MySPANIfRole_Type.__name__ = "Integer32"
_MySPANIfRole_Object = MibTableColumn
mySPANIfRole = _MySPANIfRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1, 3),
    _MySPANIfRole_Type()
)
mySPANIfRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mySPANIfRole.setStatus("current")
_MySPANEntryStatus_Type = ConfigStatus
_MySPANEntryStatus_Object = MibTableColumn
mySPANEntryStatus = _MySPANEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1, 4),
    _MySPANEntryStatus_Type()
)
mySPANEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySPANEntryStatus.setStatus("current")
_MySPANMIBConformance_ObjectIdentity = ObjectIdentity
mySPANMIBConformance = _MySPANMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3)
)
_MySPANMIBCompliances_ObjectIdentity = ObjectIdentity
mySPANMIBCompliances = _MySPANMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3, 1)
)
_MySPANMIBGroups_ObjectIdentity = ObjectIdentity
mySPANMIBGroups = _MySPANMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3, 2)
)

# Managed Objects groups

mySPANMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3, 2, 1)
)
mySPANMIBGroup.setObjects(
      *(("DES7200-SPAN-MIB", "mySPANSession"),
        ("DES7200-SPAN-MIB", "mySPANIfIndex"),
        ("DES7200-SPAN-MIB", "mySPANIfRole"),
        ("DES7200-SPAN-MIB", "mySPANEntryStatus"))
)
if mibBuilder.loadTexts:
    mySPANMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mySPANMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3, 1, 1)
)
mySPANMIBCompliance.setObjects(
    ("DES7200-SPAN-MIB", "mySPANMIBGroup")
)
if mibBuilder.loadTexts:
    mySPANMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-SPAN-MIB",
    **{"mySPANMIB": mySPANMIB,
       "mySPANMIBObjects": mySPANMIBObjects,
       "mySPANSessionNum": mySPANSessionNum,
       "mySPANTable": mySPANTable,
       "mySPANEntry": mySPANEntry,
       "mySPANSession": mySPANSession,
       "mySPANIfIndex": mySPANIfIndex,
       "mySPANIfRole": mySPANIfRole,
       "mySPANEntryStatus": mySPANEntryStatus,
       "mySPANMIBConformance": mySPANMIBConformance,
       "mySPANMIBCompliances": mySPANMIBCompliances,
       "mySPANMIBCompliance": mySPANMIBCompliance,
       "mySPANMIBGroups": mySPANMIBGroups,
       "mySPANMIBGroup": mySPANMIBGroup}
)
