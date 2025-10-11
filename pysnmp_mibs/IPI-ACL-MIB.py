# SNMP MIB module (IPI-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ipinfusion/IPI-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:17 2025
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

(ipi,) = mibBuilder.importSymbols(
    "OCNOS-IPI-MODULE-MIB",
    "ipi")

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

ipiACLMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 106)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpiAclObjects_ObjectIdentity = ObjectIdentity
ipiAclObjects = _IpiAclObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1)
)
_IpiMacACLTable_Object = MibTable
ipiMacACLTable = _IpiMacACLTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 1)
)
if mibBuilder.loadTexts:
    ipiMacACLTable.setStatus("current")
_IpiMacACLEntry_Object = MibTableRow
ipiMacACLEntry = _IpiMacACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 1, 1)
)
ipiMacACLEntry.setIndexNames(
    (0, "IPI-ACL-MIB", "macAclNumber"),
)
if mibBuilder.loadTexts:
    ipiMacACLEntry.setStatus("current")


class _MacAclNumber_Type(Unsigned32):
    """Custom type macAclNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MacAclNumber_Type.__name__ = "Unsigned32"
_MacAclNumber_Object = MibTableColumn
macAclNumber = _MacAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 1, 1, 1),
    _MacAclNumber_Type()
)
macAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAclNumber.setStatus("current")
_MacACLName_Type = DisplayString
_MacACLName_Object = MibTableColumn
macACLName = _MacACLName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 1, 1, 2),
    _MacACLName_Type()
)
macACLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macACLName.setStatus("current")
_MacACLFilterCount_Type = Unsigned32
_MacACLFilterCount_Object = MibTableColumn
macACLFilterCount = _MacACLFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 1, 1, 3),
    _MacACLFilterCount_Type()
)
macACLFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macACLFilterCount.setStatus("current")
_MacACLDefaultFilterMatchPkts_Type = Counter64
_MacACLDefaultFilterMatchPkts_Object = MibTableColumn
macACLDefaultFilterMatchPkts = _MacACLDefaultFilterMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 1, 1, 4),
    _MacACLDefaultFilterMatchPkts_Type()
)
macACLDefaultFilterMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macACLDefaultFilterMatchPkts.setStatus("current")
_IpiMacACLFilterTable_Object = MibTable
ipiMacACLFilterTable = _IpiMacACLFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 2)
)
if mibBuilder.loadTexts:
    ipiMacACLFilterTable.setStatus("current")
_IpiMacACLFilterEntry_Object = MibTableRow
ipiMacACLFilterEntry = _IpiMacACLFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 2, 1)
)
ipiMacACLFilterEntry.setIndexNames(
    (0, "IPI-ACL-MIB", "macAclNumber"),
    (0, "IPI-ACL-MIB", "macAclFilterSequenceNumber"),
)
if mibBuilder.loadTexts:
    ipiMacACLFilterEntry.setStatus("current")


class _MacAclFilterSequenceNumber_Type(Unsigned32):
    """Custom type macAclFilterSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MacAclFilterSequenceNumber_Type.__name__ = "Unsigned32"
_MacAclFilterSequenceNumber_Object = MibTableColumn
macAclFilterSequenceNumber = _MacAclFilterSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 2, 1, 1),
    _MacAclFilterSequenceNumber_Type()
)
macAclFilterSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAclFilterSequenceNumber.setStatus("current")
_MacACLFilterMatchPkts_Type = Counter64
_MacACLFilterMatchPkts_Object = MibTableColumn
macACLFilterMatchPkts = _MacACLFilterMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 2, 1, 2),
    _MacACLFilterMatchPkts_Type()
)
macACLFilterMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macACLFilterMatchPkts.setStatus("current")
_IpiIpACLTable_Object = MibTable
ipiIpACLTable = _IpiIpACLTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 3)
)
if mibBuilder.loadTexts:
    ipiIpACLTable.setStatus("current")
_IpiIpACLEntry_Object = MibTableRow
ipiIpACLEntry = _IpiIpACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 3, 1)
)
ipiIpACLEntry.setIndexNames(
    (0, "IPI-ACL-MIB", "ipAclNumber"),
)
if mibBuilder.loadTexts:
    ipiIpACLEntry.setStatus("current")


class _IpAclNumber_Type(Unsigned32):
    """Custom type ipAclNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpAclNumber_Type.__name__ = "Unsigned32"
_IpAclNumber_Object = MibTableColumn
ipAclNumber = _IpAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 3, 1, 1),
    _IpAclNumber_Type()
)
ipAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAclNumber.setStatus("current")
_IpACLName_Type = DisplayString
_IpACLName_Object = MibTableColumn
ipACLName = _IpACLName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 3, 1, 2),
    _IpACLName_Type()
)
ipACLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipACLName.setStatus("current")
_IpACLFilterCount_Type = Unsigned32
_IpACLFilterCount_Object = MibTableColumn
ipACLFilterCount = _IpACLFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 3, 1, 3),
    _IpACLFilterCount_Type()
)
ipACLFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipACLFilterCount.setStatus("current")
_IpACLDefaultFilterMatchPkts_Type = Counter64
_IpACLDefaultFilterMatchPkts_Object = MibTableColumn
ipACLDefaultFilterMatchPkts = _IpACLDefaultFilterMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 3, 1, 4),
    _IpACLDefaultFilterMatchPkts_Type()
)
ipACLDefaultFilterMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipACLDefaultFilterMatchPkts.setStatus("current")
_IpiIpACLFilterTable_Object = MibTable
ipiIpACLFilterTable = _IpiIpACLFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 4)
)
if mibBuilder.loadTexts:
    ipiIpACLFilterTable.setStatus("current")
_IpiIpACLFilterEntry_Object = MibTableRow
ipiIpACLFilterEntry = _IpiIpACLFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 4, 1)
)
ipiIpACLFilterEntry.setIndexNames(
    (0, "IPI-ACL-MIB", "ipAclNumber"),
    (0, "IPI-ACL-MIB", "ipAclFilterSequenceNumber"),
)
if mibBuilder.loadTexts:
    ipiIpACLFilterEntry.setStatus("current")


class _IpAclFilterSequenceNumber_Type(Unsigned32):
    """Custom type ipAclFilterSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpAclFilterSequenceNumber_Type.__name__ = "Unsigned32"
_IpAclFilterSequenceNumber_Object = MibTableColumn
ipAclFilterSequenceNumber = _IpAclFilterSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 4, 1, 1),
    _IpAclFilterSequenceNumber_Type()
)
ipAclFilterSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAclFilterSequenceNumber.setStatus("current")
_IpACLFilterMatchPkts_Type = Counter64
_IpACLFilterMatchPkts_Object = MibTableColumn
ipACLFilterMatchPkts = _IpACLFilterMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 4, 1, 2),
    _IpACLFilterMatchPkts_Type()
)
ipACLFilterMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipACLFilterMatchPkts.setStatus("current")
_IpiIpv6ACLTable_Object = MibTable
ipiIpv6ACLTable = _IpiIpv6ACLTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 5)
)
if mibBuilder.loadTexts:
    ipiIpv6ACLTable.setStatus("current")
_IpiIpv6ACLEntry_Object = MibTableRow
ipiIpv6ACLEntry = _IpiIpv6ACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 5, 1)
)
ipiIpv6ACLEntry.setIndexNames(
    (0, "IPI-ACL-MIB", "ipv6AclNumber"),
)
if mibBuilder.loadTexts:
    ipiIpv6ACLEntry.setStatus("current")


class _Ipv6AclNumber_Type(Unsigned32):
    """Custom type ipv6AclNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ipv6AclNumber_Type.__name__ = "Unsigned32"
_Ipv6AclNumber_Object = MibTableColumn
ipv6AclNumber = _Ipv6AclNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 5, 1, 1),
    _Ipv6AclNumber_Type()
)
ipv6AclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6AclNumber.setStatus("current")
_Ipv6ACLName_Type = DisplayString
_Ipv6ACLName_Object = MibTableColumn
ipv6ACLName = _Ipv6ACLName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 5, 1, 2),
    _Ipv6ACLName_Type()
)
ipv6ACLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ACLName.setStatus("current")
_Ipv6ACLFilterCount_Type = Unsigned32
_Ipv6ACLFilterCount_Object = MibTableColumn
ipv6ACLFilterCount = _Ipv6ACLFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 5, 1, 3),
    _Ipv6ACLFilterCount_Type()
)
ipv6ACLFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ACLFilterCount.setStatus("current")
_Ipv6ACLDefaultFilterMatchPkts_Type = Counter64
_Ipv6ACLDefaultFilterMatchPkts_Object = MibTableColumn
ipv6ACLDefaultFilterMatchPkts = _Ipv6ACLDefaultFilterMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 5, 1, 4),
    _Ipv6ACLDefaultFilterMatchPkts_Type()
)
ipv6ACLDefaultFilterMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ACLDefaultFilterMatchPkts.setStatus("current")
_IpiIpv6ACLFilterTable_Object = MibTable
ipiIpv6ACLFilterTable = _IpiIpv6ACLFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 6)
)
if mibBuilder.loadTexts:
    ipiIpv6ACLFilterTable.setStatus("current")
_IpiIpv6ACLFilterEntry_Object = MibTableRow
ipiIpv6ACLFilterEntry = _IpiIpv6ACLFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 6, 1)
)
ipiIpv6ACLFilterEntry.setIndexNames(
    (0, "IPI-ACL-MIB", "ipv6AclNumber"),
    (0, "IPI-ACL-MIB", "ipv6AclFilterSequenceNumber"),
)
if mibBuilder.loadTexts:
    ipiIpv6ACLFilterEntry.setStatus("current")


class _Ipv6AclFilterSequenceNumber_Type(Unsigned32):
    """Custom type ipv6AclFilterSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ipv6AclFilterSequenceNumber_Type.__name__ = "Unsigned32"
_Ipv6AclFilterSequenceNumber_Object = MibTableColumn
ipv6AclFilterSequenceNumber = _Ipv6AclFilterSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 6, 1, 1),
    _Ipv6AclFilterSequenceNumber_Type()
)
ipv6AclFilterSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6AclFilterSequenceNumber.setStatus("current")
_Ipv6ACLFilterMatchPkts_Type = Counter64
_Ipv6ACLFilterMatchPkts_Object = MibTableColumn
ipv6ACLFilterMatchPkts = _Ipv6ACLFilterMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 106, 1, 6, 1, 2),
    _Ipv6ACLFilterMatchPkts_Type()
)
ipv6ACLFilterMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ACLFilterMatchPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPI-ACL-MIB",
    **{"ipiACLMib": ipiACLMib,
       "ipiAclObjects": ipiAclObjects,
       "ipiMacACLTable": ipiMacACLTable,
       "ipiMacACLEntry": ipiMacACLEntry,
       "macAclNumber": macAclNumber,
       "macACLName": macACLName,
       "macACLFilterCount": macACLFilterCount,
       "macACLDefaultFilterMatchPkts": macACLDefaultFilterMatchPkts,
       "ipiMacACLFilterTable": ipiMacACLFilterTable,
       "ipiMacACLFilterEntry": ipiMacACLFilterEntry,
       "macAclFilterSequenceNumber": macAclFilterSequenceNumber,
       "macACLFilterMatchPkts": macACLFilterMatchPkts,
       "ipiIpACLTable": ipiIpACLTable,
       "ipiIpACLEntry": ipiIpACLEntry,
       "ipAclNumber": ipAclNumber,
       "ipACLName": ipACLName,
       "ipACLFilterCount": ipACLFilterCount,
       "ipACLDefaultFilterMatchPkts": ipACLDefaultFilterMatchPkts,
       "ipiIpACLFilterTable": ipiIpACLFilterTable,
       "ipiIpACLFilterEntry": ipiIpACLFilterEntry,
       "ipAclFilterSequenceNumber": ipAclFilterSequenceNumber,
       "ipACLFilterMatchPkts": ipACLFilterMatchPkts,
       "ipiIpv6ACLTable": ipiIpv6ACLTable,
       "ipiIpv6ACLEntry": ipiIpv6ACLEntry,
       "ipv6AclNumber": ipv6AclNumber,
       "ipv6ACLName": ipv6ACLName,
       "ipv6ACLFilterCount": ipv6ACLFilterCount,
       "ipv6ACLDefaultFilterMatchPkts": ipv6ACLDefaultFilterMatchPkts,
       "ipiIpv6ACLFilterTable": ipiIpv6ACLFilterTable,
       "ipiIpv6ACLFilterEntry": ipiIpv6ACLFilterEntry,
       "ipv6AclFilterSequenceNumber": ipv6AclFilterSequenceNumber,
       "ipv6ACLFilterMatchPkts": ipv6ACLFilterMatchPkts}
)
