# SNMP MIB module (LANCOM-ACL-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-ACL-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:05 2025
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

(fastPath,) = mibBuilder.importSymbols(
    "LANCOM-REF-MIB",
    "fastPath")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aclMgmtGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62)
)
if mibBuilder.loadTexts:
    aclMgmtGroup.setRevisions(
        ("2015-12-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AclMgmtServiceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("allType", 0),
          ("telnet", 1),
          ("http", 2),
          ("https", 3),
          ("snmp", 4),
          ("ssh", 5),
          ("tftp", 6),
          ("sntp", 7))
    )



class AclMgmtActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AclMgmtEnable_Type = TruthValue
_AclMgmtEnable_Object = MibScalar
aclMgmtEnable = _AclMgmtEnable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 1),
    _AclMgmtEnable_Type()
)
aclMgmtEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMgmtEnable.setStatus("current")


class _AclMgmtActiveListName_Type(DisplayString):
    """Custom type aclMgmtActiveListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclMgmtActiveListName_Type.__name__ = "DisplayString"
_AclMgmtActiveListName_Object = MibScalar
aclMgmtActiveListName = _AclMgmtActiveListName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 2),
    _AclMgmtActiveListName_Type()
)
aclMgmtActiveListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclMgmtActiveListName.setStatus("current")
_AclMgmtListTable_Object = MibTable
aclMgmtListTable = _AclMgmtListTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3)
)
if mibBuilder.loadTexts:
    aclMgmtListTable.setStatus("current")
_AclMgmtListEntry_Object = MibTableRow
aclMgmtListEntry = _AclMgmtListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1)
)
aclMgmtListEntry.setIndexNames(
    (0, "LANCOM-ACL-MGMT-MIB", "aclMgmtListName"),
    (0, "LANCOM-ACL-MGMT-MIB", "aclMgmtListPriority"),
)
if mibBuilder.loadTexts:
    aclMgmtListEntry.setStatus("current")


class _AclMgmtListName_Type(DisplayString):
    """Custom type aclMgmtListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AclMgmtListName_Type.__name__ = "DisplayString"
_AclMgmtListName_Object = MibTableColumn
aclMgmtListName = _AclMgmtListName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 1),
    _AclMgmtListName_Type()
)
aclMgmtListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMgmtListName.setStatus("current")


class _AclMgmtListPriority_Type(Unsigned32):
    """Custom type aclMgmtListPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AclMgmtListPriority_Type.__name__ = "Unsigned32"
_AclMgmtListPriority_Object = MibTableColumn
aclMgmtListPriority = _AclMgmtListPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 2),
    _AclMgmtListPriority_Type()
)
aclMgmtListPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMgmtListPriority.setStatus("current")
_AclMgmtListIfIndex_Type = Unsigned32
_AclMgmtListIfIndex_Object = MibTableColumn
aclMgmtListIfIndex = _AclMgmtListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 3),
    _AclMgmtListIfIndex_Type()
)
aclMgmtListIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclMgmtListIfIndex.setStatus("current")
_AclMgmtListIpAddr_Type = IpAddress
_AclMgmtListIpAddr_Object = MibTableColumn
aclMgmtListIpAddr = _AclMgmtListIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 4),
    _AclMgmtListIpAddr_Type()
)
aclMgmtListIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclMgmtListIpAddr.setStatus("current")
_AclMgmtListIpNetMask_Type = IpAddress
_AclMgmtListIpNetMask_Object = MibTableColumn
aclMgmtListIpNetMask = _AclMgmtListIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 5),
    _AclMgmtListIpNetMask_Type()
)
aclMgmtListIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclMgmtListIpNetMask.setStatus("current")
_AclMgmtListService_Type = AclMgmtServiceType
_AclMgmtListService_Object = MibTableColumn
aclMgmtListService = _AclMgmtListService_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 6),
    _AclMgmtListService_Type()
)
aclMgmtListService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclMgmtListService.setStatus("current")
_AclMgmtListAction_Type = AclMgmtActionType
_AclMgmtListAction_Object = MibTableColumn
aclMgmtListAction = _AclMgmtListAction_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 7),
    _AclMgmtListAction_Type()
)
aclMgmtListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclMgmtListAction.setStatus("current")
_AclMgmtListRowStatus_Type = RowStatus
_AclMgmtListRowStatus_Object = MibTableColumn
aclMgmtListRowStatus = _AclMgmtListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 8),
    _AclMgmtListRowStatus_Type()
)
aclMgmtListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMgmtListRowStatus.setStatus("current")
_AclMgmtListVlanId_Type = Unsigned32
_AclMgmtListVlanId_Object = MibTableColumn
aclMgmtListVlanId = _AclMgmtListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 9),
    _AclMgmtListVlanId_Type()
)
aclMgmtListVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclMgmtListVlanId.setStatus("current")
_AclRuleIsConflict_Type = TruthValue
_AclRuleIsConflict_Object = MibTableColumn
aclRuleIsConflict = _AclRuleIsConflict_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 10),
    _AclRuleIsConflict_Type()
)
aclRuleIsConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclRuleIsConflict.setStatus("current")
_AclMgmtTrapReason_Type = DisplayString
_AclMgmtTrapReason_Object = MibScalar
aclMgmtTrapReason = _AclMgmtTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 5),
    _AclMgmtTrapReason_Type()
)
aclMgmtTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMgmtTrapReason.setStatus("current")

# Managed Objects groups


# Notification objects

aclMgmtTrapInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 4)
)
aclMgmtTrapInfo.setObjects(
    ("LANCOM-ACL-MGMT-MIB", "aclMgmtTrapReason")
)
if mibBuilder.loadTexts:
    aclMgmtTrapInfo.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-ACL-MGMT-MIB",
    **{"AclMgmtServiceType": AclMgmtServiceType,
       "AclMgmtActionType": AclMgmtActionType,
       "aclMgmtGroup": aclMgmtGroup,
       "aclMgmtEnable": aclMgmtEnable,
       "aclMgmtActiveListName": aclMgmtActiveListName,
       "aclMgmtListTable": aclMgmtListTable,
       "aclMgmtListEntry": aclMgmtListEntry,
       "aclMgmtListName": aclMgmtListName,
       "aclMgmtListPriority": aclMgmtListPriority,
       "aclMgmtListIfIndex": aclMgmtListIfIndex,
       "aclMgmtListIpAddr": aclMgmtListIpAddr,
       "aclMgmtListIpNetMask": aclMgmtListIpNetMask,
       "aclMgmtListService": aclMgmtListService,
       "aclMgmtListAction": aclMgmtListAction,
       "aclMgmtListRowStatus": aclMgmtListRowStatus,
       "aclMgmtListVlanId": aclMgmtListVlanId,
       "aclRuleIsConflict": aclRuleIsConflict,
       "aclMgmtTrapInfo": aclMgmtTrapInfo,
       "aclMgmtTrapReason": aclMgmtTrapReason}
)
