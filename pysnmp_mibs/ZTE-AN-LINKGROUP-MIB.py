# SNMP MIB module (ZTE-AN-LINKGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-LINKGROUP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:11 2025
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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnLinkGroupMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40)
)
if mibBuilder.loadTexts:
    zxAnLinkGroupMib.setRevisions(
        ("2012-09-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnLinkGroupObjects_ObjectIdentity = ObjectIdentity
zxAnLinkGroupObjects = _ZxAnLinkGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2)
)
_ZxAnLinkGroupGroupObjects_ObjectIdentity = ObjectIdentity
zxAnLinkGroupGroupObjects = _ZxAnLinkGroupGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10)
)
_ZxAnLinkGroupTable_Object = MibTable
zxAnLinkGroupTable = _ZxAnLinkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2)
)
if mibBuilder.loadTexts:
    zxAnLinkGroupTable.setStatus("current")
_ZxAnLinkGroupEntry_Object = MibTableRow
zxAnLinkGroupEntry = _ZxAnLinkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1)
)
zxAnLinkGroupEntry.setIndexNames(
    (0, "ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupId"),
)
if mibBuilder.loadTexts:
    zxAnLinkGroupEntry.setStatus("current")


class _ZxAnLinkGroupId_Type(Integer32):
    """Custom type zxAnLinkGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_ZxAnLinkGroupId_Type.__name__ = "Integer32"
_ZxAnLinkGroupId_Object = MibTableColumn
zxAnLinkGroupId = _ZxAnLinkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 1),
    _ZxAnLinkGroupId_Type()
)
zxAnLinkGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLinkGroupId.setStatus("current")


class _ZxAnLinkGroupName_Type(DisplayString):
    """Custom type zxAnLinkGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupName_Type.__name__ = "DisplayString"
_ZxAnLinkGroupName_Object = MibTableColumn
zxAnLinkGroupName = _ZxAnLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 2),
    _ZxAnLinkGroupName_Type()
)
zxAnLinkGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupName.setStatus("current")


class _ZxAnLinkGroupLoadBalanceMode_Type(Integer32):
    """Custom type zxAnLinkGroupLoadBalanceMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dstIp", 1),
          ("dstMac", 2),
          ("srcDstIp", 3),
          ("srcDstMac", 4),
          ("srcIp", 5),
          ("srcMac", 6))
    )


_ZxAnLinkGroupLoadBalanceMode_Type.__name__ = "Integer32"
_ZxAnLinkGroupLoadBalanceMode_Object = MibTableColumn
zxAnLinkGroupLoadBalanceMode = _ZxAnLinkGroupLoadBalanceMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 3),
    _ZxAnLinkGroupLoadBalanceMode_Type()
)
zxAnLinkGroupLoadBalanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLinkGroupLoadBalanceMode.setStatus("current")


class _ZxAnLinkGroupMemberPortName1_Type(DisplayString):
    """Custom type zxAnLinkGroupMemberPortName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupMemberPortName1_Type.__name__ = "DisplayString"
_ZxAnLinkGroupMemberPortName1_Object = MibTableColumn
zxAnLinkGroupMemberPortName1 = _ZxAnLinkGroupMemberPortName1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 4),
    _ZxAnLinkGroupMemberPortName1_Type()
)
zxAnLinkGroupMemberPortName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupMemberPortName1.setStatus("current")


class _ZxAnLinkGroupMemberPortName2_Type(DisplayString):
    """Custom type zxAnLinkGroupMemberPortName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupMemberPortName2_Type.__name__ = "DisplayString"
_ZxAnLinkGroupMemberPortName2_Object = MibTableColumn
zxAnLinkGroupMemberPortName2 = _ZxAnLinkGroupMemberPortName2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 5),
    _ZxAnLinkGroupMemberPortName2_Type()
)
zxAnLinkGroupMemberPortName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupMemberPortName2.setStatus("current")


class _ZxAnLinkGroupMemberPortName3_Type(DisplayString):
    """Custom type zxAnLinkGroupMemberPortName3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupMemberPortName3_Type.__name__ = "DisplayString"
_ZxAnLinkGroupMemberPortName3_Object = MibTableColumn
zxAnLinkGroupMemberPortName3 = _ZxAnLinkGroupMemberPortName3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 6),
    _ZxAnLinkGroupMemberPortName3_Type()
)
zxAnLinkGroupMemberPortName3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupMemberPortName3.setStatus("current")


class _ZxAnLinkGroupMemberPortName4_Type(DisplayString):
    """Custom type zxAnLinkGroupMemberPortName4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupMemberPortName4_Type.__name__ = "DisplayString"
_ZxAnLinkGroupMemberPortName4_Object = MibTableColumn
zxAnLinkGroupMemberPortName4 = _ZxAnLinkGroupMemberPortName4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 7),
    _ZxAnLinkGroupMemberPortName4_Type()
)
zxAnLinkGroupMemberPortName4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupMemberPortName4.setStatus("current")


class _ZxAnLinkGroupMemberPortName5_Type(DisplayString):
    """Custom type zxAnLinkGroupMemberPortName5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupMemberPortName5_Type.__name__ = "DisplayString"
_ZxAnLinkGroupMemberPortName5_Object = MibTableColumn
zxAnLinkGroupMemberPortName5 = _ZxAnLinkGroupMemberPortName5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 8),
    _ZxAnLinkGroupMemberPortName5_Type()
)
zxAnLinkGroupMemberPortName5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupMemberPortName5.setStatus("current")


class _ZxAnLinkGroupMemberPortName6_Type(DisplayString):
    """Custom type zxAnLinkGroupMemberPortName6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupMemberPortName6_Type.__name__ = "DisplayString"
_ZxAnLinkGroupMemberPortName6_Object = MibTableColumn
zxAnLinkGroupMemberPortName6 = _ZxAnLinkGroupMemberPortName6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 9),
    _ZxAnLinkGroupMemberPortName6_Type()
)
zxAnLinkGroupMemberPortName6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupMemberPortName6.setStatus("current")


class _ZxAnLinkGroupMemberPortName7_Type(DisplayString):
    """Custom type zxAnLinkGroupMemberPortName7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupMemberPortName7_Type.__name__ = "DisplayString"
_ZxAnLinkGroupMemberPortName7_Object = MibTableColumn
zxAnLinkGroupMemberPortName7 = _ZxAnLinkGroupMemberPortName7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 10),
    _ZxAnLinkGroupMemberPortName7_Type()
)
zxAnLinkGroupMemberPortName7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupMemberPortName7.setStatus("current")


class _ZxAnLinkGroupMemberPortName8_Type(DisplayString):
    """Custom type zxAnLinkGroupMemberPortName8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupMemberPortName8_Type.__name__ = "DisplayString"
_ZxAnLinkGroupMemberPortName8_Object = MibTableColumn
zxAnLinkGroupMemberPortName8 = _ZxAnLinkGroupMemberPortName8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 10, 2, 1, 11),
    _ZxAnLinkGroupMemberPortName8_Type()
)
zxAnLinkGroupMemberPortName8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupMemberPortName8.setStatus("current")
_ZxAnLinkGroupPortObjects_ObjectIdentity = ObjectIdentity
zxAnLinkGroupPortObjects = _ZxAnLinkGroupPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 15)
)
_ZxAnLinkGroupPortTable_Object = MibTable
zxAnLinkGroupPortTable = _ZxAnLinkGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 15, 2)
)
if mibBuilder.loadTexts:
    zxAnLinkGroupPortTable.setStatus("current")
_ZxAnLinkGroupPortEntry_Object = MibTableRow
zxAnLinkGroupPortEntry = _ZxAnLinkGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 15, 2, 1)
)
zxAnLinkGroupPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnLinkGroupPortEntry.setStatus("current")


class _ZxAnLinkGroupPortGroupId_Type(Integer32):
    """Custom type zxAnLinkGroupPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_ZxAnLinkGroupPortGroupId_Type.__name__ = "Integer32"
_ZxAnLinkGroupPortGroupId_Object = MibTableColumn
zxAnLinkGroupPortGroupId = _ZxAnLinkGroupPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 15, 2, 1, 1),
    _ZxAnLinkGroupPortGroupId_Type()
)
zxAnLinkGroupPortGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLinkGroupPortGroupId.setStatus("current")


class _ZxAnLinkGroupPortName_Type(DisplayString):
    """Custom type zxAnLinkGroupPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnLinkGroupPortName_Type.__name__ = "DisplayString"
_ZxAnLinkGroupPortName_Object = MibTableColumn
zxAnLinkGroupPortName = _ZxAnLinkGroupPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 15, 2, 1, 2),
    _ZxAnLinkGroupPortName_Type()
)
zxAnLinkGroupPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupPortName.setStatus("current")


class _ZxAnLinkGroupPortStatus_Type(Integer32):
    """Custom type zxAnLinkGroupPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_ZxAnLinkGroupPortStatus_Type.__name__ = "Integer32"
_ZxAnLinkGroupPortStatus_Object = MibTableColumn
zxAnLinkGroupPortStatus = _ZxAnLinkGroupPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 15, 2, 1, 3),
    _ZxAnLinkGroupPortStatus_Type()
)
zxAnLinkGroupPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLinkGroupPortStatus.setStatus("current")
_ZxAnLinkGroupPortRowStatus_Type = RowStatus
_ZxAnLinkGroupPortRowStatus_Object = MibTableColumn
zxAnLinkGroupPortRowStatus = _ZxAnLinkGroupPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 2, 15, 2, 1, 50),
    _ZxAnLinkGroupPortRowStatus_Type()
)
zxAnLinkGroupPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLinkGroupPortRowStatus.setStatus("current")
_ZxAnLinkGroupConformance_ObjectIdentity = ObjectIdentity
zxAnLinkGroupConformance = _ZxAnLinkGroupConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 4)
)
_ZxAnLinkGroupCompliances_ObjectIdentity = ObjectIdentity
zxAnLinkGroupCompliances = _ZxAnLinkGroupCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 4, 1)
)
_ZxAnLinkGroupGroups_ObjectIdentity = ObjectIdentity
zxAnLinkGroupGroups = _ZxAnLinkGroupGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 4, 2)
)

# Managed Objects groups

zxAnLinkGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 4, 2, 3)
)
zxAnLinkGroupGroup.setObjects(
      *(("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupName"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupLoadBalanceMode"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupMemberPortName1"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupMemberPortName2"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupMemberPortName3"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupMemberPortName4"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupMemberPortName5"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupMemberPortName6"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupMemberPortName7"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupMemberPortName8"))
)
if mibBuilder.loadTexts:
    zxAnLinkGroupGroup.setStatus("current")

zxAnLinkGroupPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 4, 2, 5)
)
zxAnLinkGroupPortGroup.setObjects(
      *(("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupPortGroupId"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupPortName"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupPortStatus"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupPortRowStatus"))
)
if mibBuilder.loadTexts:
    zxAnLinkGroupPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zxAnLinkGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 40, 4, 1, 1)
)
zxAnLinkGroupCompliance.setObjects(
      *(("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupGroup"),
        ("ZTE-AN-LINKGROUP-MIB", "zxAnLinkGroupPortGroup"))
)
if mibBuilder.loadTexts:
    zxAnLinkGroupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-LINKGROUP-MIB",
    **{"zxAnLinkGroupMib": zxAnLinkGroupMib,
       "zxAnLinkGroupObjects": zxAnLinkGroupObjects,
       "zxAnLinkGroupGroupObjects": zxAnLinkGroupGroupObjects,
       "zxAnLinkGroupTable": zxAnLinkGroupTable,
       "zxAnLinkGroupEntry": zxAnLinkGroupEntry,
       "zxAnLinkGroupId": zxAnLinkGroupId,
       "zxAnLinkGroupName": zxAnLinkGroupName,
       "zxAnLinkGroupLoadBalanceMode": zxAnLinkGroupLoadBalanceMode,
       "zxAnLinkGroupMemberPortName1": zxAnLinkGroupMemberPortName1,
       "zxAnLinkGroupMemberPortName2": zxAnLinkGroupMemberPortName2,
       "zxAnLinkGroupMemberPortName3": zxAnLinkGroupMemberPortName3,
       "zxAnLinkGroupMemberPortName4": zxAnLinkGroupMemberPortName4,
       "zxAnLinkGroupMemberPortName5": zxAnLinkGroupMemberPortName5,
       "zxAnLinkGroupMemberPortName6": zxAnLinkGroupMemberPortName6,
       "zxAnLinkGroupMemberPortName7": zxAnLinkGroupMemberPortName7,
       "zxAnLinkGroupMemberPortName8": zxAnLinkGroupMemberPortName8,
       "zxAnLinkGroupPortObjects": zxAnLinkGroupPortObjects,
       "zxAnLinkGroupPortTable": zxAnLinkGroupPortTable,
       "zxAnLinkGroupPortEntry": zxAnLinkGroupPortEntry,
       "zxAnLinkGroupPortGroupId": zxAnLinkGroupPortGroupId,
       "zxAnLinkGroupPortName": zxAnLinkGroupPortName,
       "zxAnLinkGroupPortStatus": zxAnLinkGroupPortStatus,
       "zxAnLinkGroupPortRowStatus": zxAnLinkGroupPortRowStatus,
       "zxAnLinkGroupConformance": zxAnLinkGroupConformance,
       "zxAnLinkGroupCompliances": zxAnLinkGroupCompliances,
       "zxAnLinkGroupCompliance": zxAnLinkGroupCompliance,
       "zxAnLinkGroupGroups": zxAnLinkGroupGroups,
       "zxAnLinkGroupGroup": zxAnLinkGroupGroup,
       "zxAnLinkGroupPortGroup": zxAnLinkGroupPortGroup}
)
