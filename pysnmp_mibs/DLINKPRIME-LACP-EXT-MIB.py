# SNMP MIB module (DLINKPRIME-LACP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-LACP-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:02 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

dlinkPrimeLacpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 6)
)
if mibBuilder.loadTexts:
    dlinkPrimeLacpExtMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpLacpExtMIBObjects_ObjectIdentity = ObjectIdentity
dpLacpExtMIBObjects = _DpLacpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 1)
)
_DpLacpExtGroupTable_Object = MibTable
dpLacpExtGroupTable = _DpLacpExtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1)
)
if mibBuilder.loadTexts:
    dpLacpExtGroupTable.setStatus("current")
_DpLacpExtGroupEntry_Object = MibTableRow
dpLacpExtGroupEntry = _DpLacpExtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1)
)
dpLacpExtGroupEntry.setIndexNames(
    (0, "DLINKPRIME-LACP-EXT-MIB", "dpLacpExtGroupChannelNo"),
)
if mibBuilder.loadTexts:
    dpLacpExtGroupEntry.setStatus("current")


class _DpLacpExtGroupChannelNo_Type(Integer32):
    """Custom type dpLacpExtGroupChannelNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DpLacpExtGroupChannelNo_Type.__name__ = "Integer32"
_DpLacpExtGroupChannelNo_Object = MibTableColumn
dpLacpExtGroupChannelNo = _DpLacpExtGroupChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1, 1),
    _DpLacpExtGroupChannelNo_Type()
)
dpLacpExtGroupChannelNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpLacpExtGroupChannelNo.setStatus("current")


class _DpLacpExtGroupType_Type(Integer32):
    """Custom type dpLacpExtGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static_on", 1),
          ("lacp_active", 2),
          ("lacp_passive", 3))
    )


_DpLacpExtGroupType_Type.__name__ = "Integer32"
_DpLacpExtGroupType_Object = MibTableColumn
dpLacpExtGroupType = _DpLacpExtGroupType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1, 2),
    _DpLacpExtGroupType_Type()
)
dpLacpExtGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpLacpExtGroupType.setStatus("current")
_DpLacpExtGroupMemberPorts_Type = PortList
_DpLacpExtGroupMemberPorts_Object = MibTableColumn
dpLacpExtGroupMemberPorts = _DpLacpExtGroupMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1, 3),
    _DpLacpExtGroupMemberPorts_Type()
)
dpLacpExtGroupMemberPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpLacpExtGroupMemberPorts.setStatus("current")
_DpLacpExtGroupRowStatus_Type = RowStatus
_DpLacpExtGroupRowStatus_Object = MibTableColumn
dpLacpExtGroupRowStatus = _DpLacpExtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 1, 1, 1, 4),
    _DpLacpExtGroupRowStatus_Type()
)
dpLacpExtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpLacpExtGroupRowStatus.setStatus("current")
_DpLacpExtMIBConformance_ObjectIdentity = ObjectIdentity
dpLacpExtMIBConformance = _DpLacpExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 2)
)
_DpLacpExtCompliances_ObjectIdentity = ObjectIdentity
dpLacpExtCompliances = _DpLacpExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 2, 1)
)
_DpLacpExtGroups_ObjectIdentity = ObjectIdentity
dpLacpExtGroups = _DpLacpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 2, 2)
)

# Managed Objects groups

dpLacpExtChannelGrpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 2, 2, 1)
)
dpLacpExtChannelGrpInfoGroup.setObjects(
      *(("DLINKPRIME-LACP-EXT-MIB", "dpLacpExtGroupType"),
        ("DLINKPRIME-LACP-EXT-MIB", "dpLacpExtGroupMemberPorts"),
        ("DLINKPRIME-LACP-EXT-MIB", "dpLacpExtGroupRowStatus"))
)
if mibBuilder.loadTexts:
    dpLacpExtChannelGrpInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpLacpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 6, 2, 1, 1)
)
dpLacpExtCompliance.setObjects(
    ("DLINKPRIME-LACP-EXT-MIB", "dpLacpExtChannelGrpInfoGroup")
)
if mibBuilder.loadTexts:
    dpLacpExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-LACP-EXT-MIB",
    **{"dlinkPrimeLacpExtMIB": dlinkPrimeLacpExtMIB,
       "dpLacpExtMIBObjects": dpLacpExtMIBObjects,
       "dpLacpExtGroupTable": dpLacpExtGroupTable,
       "dpLacpExtGroupEntry": dpLacpExtGroupEntry,
       "dpLacpExtGroupChannelNo": dpLacpExtGroupChannelNo,
       "dpLacpExtGroupType": dpLacpExtGroupType,
       "dpLacpExtGroupMemberPorts": dpLacpExtGroupMemberPorts,
       "dpLacpExtGroupRowStatus": dpLacpExtGroupRowStatus,
       "dpLacpExtMIBConformance": dpLacpExtMIBConformance,
       "dpLacpExtCompliances": dpLacpExtCompliances,
       "dpLacpExtCompliance": dpLacpExtCompliance,
       "dpLacpExtGroups": dpLacpExtGroups,
       "dpLacpExtChannelGrpInfoGroup": dpLacpExtChannelGrpInfoGroup}
)
