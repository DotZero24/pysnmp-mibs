# SNMP MIB module (RC-TEImportPolicy-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/RC-TEImportPolicy-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:24:42 2025
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

(rc,) = mibBuilder.importSymbols(
    "RC-SMI",
    "rc")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rcTEImportPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 65000, 2)
)
if mibBuilder.loadTexts:
    rcTEImportPolicy.setRevisions(
        ("2012-12-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcRouteMapTable_Object = MibTable
rcRouteMapTable = _RcRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 1)
)
if mibBuilder.loadTexts:
    rcRouteMapTable.setStatus("current")
_RcRouteMapEntry_Object = MibTableRow
rcRouteMapEntry = _RcRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 1, 1)
)
rcRouteMapEntry.setIndexNames(
    (0, "RC-TEImportPolicy-MIB", "rcRouteMapname"),
    (0, "RC-TEImportPolicy-MIB", "rcRouteMapIndex"),
    (0, "RC-TEImportPolicy-MIB", "rcRouteMapIntanceIndex"),
)
if mibBuilder.loadTexts:
    rcRouteMapEntry.setStatus("current")


class _RcRouteMapname_Type(DisplayString):
    """Custom type rcRouteMapname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcRouteMapname_Type.__name__ = "DisplayString"
_RcRouteMapname_Object = MibTableColumn
rcRouteMapname = _RcRouteMapname_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 1, 1, 1),
    _RcRouteMapname_Type()
)
rcRouteMapname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRouteMapname.setStatus("current")


class _RcRouteMapIndex_Type(Unsigned32):
    """Custom type rcRouteMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RcRouteMapIndex_Type.__name__ = "Unsigned32"
_RcRouteMapIndex_Object = MibTableColumn
rcRouteMapIndex = _RcRouteMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 1, 1, 2),
    _RcRouteMapIndex_Type()
)
rcRouteMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRouteMapIndex.setStatus("current")


class _RcRouteMapIntanceIndex_Type(Unsigned32):
    """Custom type rcRouteMapIntanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcRouteMapIntanceIndex_Type.__name__ = "Unsigned32"
_RcRouteMapIntanceIndex_Object = MibTableColumn
rcRouteMapIntanceIndex = _RcRouteMapIntanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 1, 1, 3),
    _RcRouteMapIntanceIndex_Type()
)
rcRouteMapIntanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRouteMapIntanceIndex.setStatus("current")


class _RcRouteMapMatchAcl_Type(DisplayString):
    """Custom type rcRouteMapMatchAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcRouteMapMatchAcl_Type.__name__ = "DisplayString"
_RcRouteMapMatchAcl_Object = MibTableColumn
rcRouteMapMatchAcl = _RcRouteMapMatchAcl_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 1, 1, 4),
    _RcRouteMapMatchAcl_Type()
)
rcRouteMapMatchAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRouteMapMatchAcl.setStatus("current")


class _RcRouteMapSetIntfTunnelID_Type(Unsigned32):
    """Custom type rcRouteMapSetIntfTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_RcRouteMapSetIntfTunnelID_Type.__name__ = "Unsigned32"
_RcRouteMapSetIntfTunnelID_Object = MibTableColumn
rcRouteMapSetIntfTunnelID = _RcRouteMapSetIntfTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 1, 1, 5),
    _RcRouteMapSetIntfTunnelID_Type()
)
rcRouteMapSetIntfTunnelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRouteMapSetIntfTunnelID.setStatus("current")
_RcRouteMapRowSta_Type = RowStatus
_RcRouteMapRowSta_Object = MibTableColumn
rcRouteMapRowSta = _RcRouteMapRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 1, 1, 6),
    _RcRouteMapRowSta_Type()
)
rcRouteMapRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRouteMapRowSta.setStatus("current")
_RcPolicyRouteTable_Object = MibTable
rcPolicyRouteTable = _RcPolicyRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 2)
)
if mibBuilder.loadTexts:
    rcPolicyRouteTable.setStatus("current")
_RcPolicyRouteEntry_Object = MibTableRow
rcPolicyRouteEntry = _RcPolicyRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 2, 1)
)
rcPolicyRouteEntry.setIndexNames(
    (0, "RC-TEImportPolicy-MIB", "rcInterfacename"),
    (0, "RC-TEImportPolicy-MIB", "rcRefRouteMapname"),
    (0, "RC-TEImportPolicy-MIB", "rcRefRouteMapIndex"),
)
if mibBuilder.loadTexts:
    rcPolicyRouteEntry.setStatus("current")


class _RcInterfacename_Type(DisplayString):
    """Custom type rcInterfacename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcInterfacename_Type.__name__ = "DisplayString"
_RcInterfacename_Object = MibTableColumn
rcInterfacename = _RcInterfacename_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 2, 1, 1),
    _RcInterfacename_Type()
)
rcInterfacename.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcInterfacename.setStatus("current")


class _RcRefRouteMapname_Type(DisplayString):
    """Custom type rcRefRouteMapname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcRefRouteMapname_Type.__name__ = "DisplayString"
_RcRefRouteMapname_Object = MibTableColumn
rcRefRouteMapname = _RcRefRouteMapname_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 2, 1, 2),
    _RcRefRouteMapname_Type()
)
rcRefRouteMapname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRefRouteMapname.setStatus("current")


class _RcRefRouteMapIndex_Type(Unsigned32):
    """Custom type rcRefRouteMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RcRefRouteMapIndex_Type.__name__ = "Unsigned32"
_RcRefRouteMapIndex_Object = MibTableColumn
rcRefRouteMapIndex = _RcRefRouteMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 2, 1, 3),
    _RcRefRouteMapIndex_Type()
)
rcRefRouteMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRefRouteMapIndex.setStatus("current")
_RcPolicyRouteRowSta_Type = RowStatus
_RcPolicyRouteRowSta_Object = MibTableColumn
rcPolicyRouteRowSta = _RcPolicyRouteRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 2, 1, 4),
    _RcPolicyRouteRowSta_Type()
)
rcPolicyRouteRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPolicyRouteRowSta.setStatus("current")
_RcACLTable_Object = MibTable
rcACLTable = _RcACLTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3)
)
if mibBuilder.loadTexts:
    rcACLTable.setStatus("current")
_RcACLEntry_Object = MibTableRow
rcACLEntry = _RcACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1)
)
rcACLEntry.setIndexNames(
    (0, "RC-TEImportPolicy-MIB", "rcIPv4ACLName"),
    (0, "RC-TEImportPolicy-MIB", "rcIPv4ACLRuleID"),
)
if mibBuilder.loadTexts:
    rcACLEntry.setStatus("current")


class _RcIPv4ACLName_Type(DisplayString):
    """Custom type rcIPv4ACLName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RcIPv4ACLName_Type.__name__ = "DisplayString"
_RcIPv4ACLName_Object = MibTableColumn
rcIPv4ACLName = _RcIPv4ACLName_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 1),
    _RcIPv4ACLName_Type()
)
rcIPv4ACLName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIPv4ACLName.setStatus("current")


class _RcIPv4ACLRuleID_Type(Unsigned32):
    """Custom type rcIPv4ACLRuleID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcIPv4ACLRuleID_Type.__name__ = "Unsigned32"
_RcIPv4ACLRuleID_Object = MibTableColumn
rcIPv4ACLRuleID = _RcIPv4ACLRuleID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 2),
    _RcIPv4ACLRuleID_Type()
)
rcIPv4ACLRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIPv4ACLRuleID.setStatus("current")
_RcIPv4ACLSrcAddr_Type = IpAddress
_RcIPv4ACLSrcAddr_Object = MibTableColumn
rcIPv4ACLSrcAddr = _RcIPv4ACLSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 3),
    _RcIPv4ACLSrcAddr_Type()
)
rcIPv4ACLSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLSrcAddr.setStatus("current")
_RcIPv4ACLSrcWildcard_Type = IpAddress
_RcIPv4ACLSrcWildcard_Object = MibTableColumn
rcIPv4ACLSrcWildcard = _RcIPv4ACLSrcWildcard_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 4),
    _RcIPv4ACLSrcWildcard_Type()
)
rcIPv4ACLSrcWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLSrcWildcard.setStatus("current")
_RcIPv4ACLDestAddr_Type = IpAddress
_RcIPv4ACLDestAddr_Object = MibTableColumn
rcIPv4ACLDestAddr = _RcIPv4ACLDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 5),
    _RcIPv4ACLDestAddr_Type()
)
rcIPv4ACLDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLDestAddr.setStatus("current")
_RcIPv4ACLDestWildcard_Type = IpAddress
_RcIPv4ACLDestWildcard_Object = MibTableColumn
rcIPv4ACLDestWildcard = _RcIPv4ACLDestWildcard_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 6),
    _RcIPv4ACLDestWildcard_Type()
)
rcIPv4ACLDestWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLDestWildcard.setStatus("current")


class _RcIPv4ACLProtocol_Type(Unsigned32):
    """Custom type rcIPv4ACLProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RcIPv4ACLProtocol_Type.__name__ = "Unsigned32"
_RcIPv4ACLProtocol_Object = MibTableColumn
rcIPv4ACLProtocol = _RcIPv4ACLProtocol_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 7),
    _RcIPv4ACLProtocol_Type()
)
rcIPv4ACLProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLProtocol.setStatus("current")


class _RcIPv4ACLSrcPortBegin_Type(Unsigned32):
    """Custom type rcIPv4ACLSrcPortBegin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIPv4ACLSrcPortBegin_Type.__name__ = "Unsigned32"
_RcIPv4ACLSrcPortBegin_Object = MibTableColumn
rcIPv4ACLSrcPortBegin = _RcIPv4ACLSrcPortBegin_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 8),
    _RcIPv4ACLSrcPortBegin_Type()
)
rcIPv4ACLSrcPortBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLSrcPortBegin.setStatus("current")


class _RcIPv4ACLSrcPortEnd_Type(Unsigned32):
    """Custom type rcIPv4ACLSrcPortEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIPv4ACLSrcPortEnd_Type.__name__ = "Unsigned32"
_RcIPv4ACLSrcPortEnd_Object = MibTableColumn
rcIPv4ACLSrcPortEnd = _RcIPv4ACLSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 9),
    _RcIPv4ACLSrcPortEnd_Type()
)
rcIPv4ACLSrcPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLSrcPortEnd.setStatus("current")


class _RcIPv4ACLDestPortBegin_Type(Unsigned32):
    """Custom type rcIPv4ACLDestPortBegin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIPv4ACLDestPortBegin_Type.__name__ = "Unsigned32"
_RcIPv4ACLDestPortBegin_Object = MibTableColumn
rcIPv4ACLDestPortBegin = _RcIPv4ACLDestPortBegin_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 10),
    _RcIPv4ACLDestPortBegin_Type()
)
rcIPv4ACLDestPortBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLDestPortBegin.setStatus("current")


class _RcIPv4ACLDestPortEnd_Type(Unsigned32):
    """Custom type rcIPv4ACLDestPortEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIPv4ACLDestPortEnd_Type.__name__ = "Unsigned32"
_RcIPv4ACLDestPortEnd_Object = MibTableColumn
rcIPv4ACLDestPortEnd = _RcIPv4ACLDestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 11),
    _RcIPv4ACLDestPortEnd_Type()
)
rcIPv4ACLDestPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLDestPortEnd.setStatus("current")


class _RcIPv4ACLDSCP_Type(Unsigned32):
    """Custom type rcIPv4ACLDSCP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_RcIPv4ACLDSCP_Type.__name__ = "Unsigned32"
_RcIPv4ACLDSCP_Object = MibTableColumn
rcIPv4ACLDSCP = _RcIPv4ACLDSCP_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 12),
    _RcIPv4ACLDSCP_Type()
)
rcIPv4ACLDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPv4ACLDSCP.setStatus("current")
_RcIPV4ACLRowsta_Type = RowStatus
_RcIPV4ACLRowsta_Object = MibTableColumn
rcIPV4ACLRowsta = _RcIPV4ACLRowsta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 2, 3, 1, 13),
    _RcIPV4ACLRowsta_Type()
)
rcIPV4ACLRowsta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIPV4ACLRowsta.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC-TEImportPolicy-MIB",
    **{"rcTEImportPolicy": rcTEImportPolicy,
       "rcRouteMapTable": rcRouteMapTable,
       "rcRouteMapEntry": rcRouteMapEntry,
       "rcRouteMapname": rcRouteMapname,
       "rcRouteMapIndex": rcRouteMapIndex,
       "rcRouteMapIntanceIndex": rcRouteMapIntanceIndex,
       "rcRouteMapMatchAcl": rcRouteMapMatchAcl,
       "rcRouteMapSetIntfTunnelID": rcRouteMapSetIntfTunnelID,
       "rcRouteMapRowSta": rcRouteMapRowSta,
       "rcPolicyRouteTable": rcPolicyRouteTable,
       "rcPolicyRouteEntry": rcPolicyRouteEntry,
       "rcInterfacename": rcInterfacename,
       "rcRefRouteMapname": rcRefRouteMapname,
       "rcRefRouteMapIndex": rcRefRouteMapIndex,
       "rcPolicyRouteRowSta": rcPolicyRouteRowSta,
       "rcACLTable": rcACLTable,
       "rcACLEntry": rcACLEntry,
       "rcIPv4ACLName": rcIPv4ACLName,
       "rcIPv4ACLRuleID": rcIPv4ACLRuleID,
       "rcIPv4ACLSrcAddr": rcIPv4ACLSrcAddr,
       "rcIPv4ACLSrcWildcard": rcIPv4ACLSrcWildcard,
       "rcIPv4ACLDestAddr": rcIPv4ACLDestAddr,
       "rcIPv4ACLDestWildcard": rcIPv4ACLDestWildcard,
       "rcIPv4ACLProtocol": rcIPv4ACLProtocol,
       "rcIPv4ACLSrcPortBegin": rcIPv4ACLSrcPortBegin,
       "rcIPv4ACLSrcPortEnd": rcIPv4ACLSrcPortEnd,
       "rcIPv4ACLDestPortBegin": rcIPv4ACLDestPortBegin,
       "rcIPv4ACLDestPortEnd": rcIPv4ACLDestPortEnd,
       "rcIPv4ACLDSCP": rcIPv4ACLDSCP,
       "rcIPV4ACLRowsta": rcIPV4ACLRowsta}
)
