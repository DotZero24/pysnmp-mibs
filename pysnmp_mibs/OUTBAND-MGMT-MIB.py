# SNMP MIB module (OUTBAND-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/OUTBAND-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:09 2025
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

(iscomEpon,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomEpon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rcOutbandMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 24, 3)
)
if mibBuilder.loadTexts:
    rcOutbandMgmt.setRevisions(
        ("2007-02-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcOutbandIpSubnet_ObjectIdentity = ObjectIdentity
rcOutbandIpSubnet = _RcOutbandIpSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1)
)
_RcOutbandIpSubnetTable_Object = MibTable
rcOutbandIpSubnetTable = _RcOutbandIpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rcOutbandIpSubnetTable.setStatus("current")
_RcOutbandIpSubnetEntry_Object = MibTableRow
rcOutbandIpSubnetEntry = _RcOutbandIpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1)
)
rcOutbandIpSubnetEntry.setIndexNames(
    (0, "OUTBAND-MGMT-MIB", "rcOutbandIpSubnetIndex"),
)
if mibBuilder.loadTexts:
    rcOutbandIpSubnetEntry.setStatus("current")
_RcOutbandIpSubnetIndex_Type = Integer32
_RcOutbandIpSubnetIndex_Object = MibTableColumn
rcOutbandIpSubnetIndex = _RcOutbandIpSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1, 1),
    _RcOutbandIpSubnetIndex_Type()
)
rcOutbandIpSubnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcOutbandIpSubnetIndex.setStatus("current")
_RcOutbandIpSubnetIpAddress_Type = IpAddress
_RcOutbandIpSubnetIpAddress_Object = MibTableColumn
rcOutbandIpSubnetIpAddress = _RcOutbandIpSubnetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1, 2),
    _RcOutbandIpSubnetIpAddress_Type()
)
rcOutbandIpSubnetIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcOutbandIpSubnetIpAddress.setStatus("current")
_RcOutbandIpSubnetMask_Type = IpAddress
_RcOutbandIpSubnetMask_Object = MibTableColumn
rcOutbandIpSubnetMask = _RcOutbandIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1, 3),
    _RcOutbandIpSubnetMask_Type()
)
rcOutbandIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcOutbandIpSubnetMask.setStatus("current")
_RcOutbandIpSubnetRowStatus_Type = RowStatus
_RcOutbandIpSubnetRowStatus_Object = MibTableColumn
rcOutbandIpSubnetRowStatus = _RcOutbandIpSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 24, 3, 1, 1, 1, 4),
    _RcOutbandIpSubnetRowStatus_Type()
)
rcOutbandIpSubnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcOutbandIpSubnetRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OUTBAND-MGMT-MIB",
    **{"rcOutbandMgmt": rcOutbandMgmt,
       "rcOutbandIpSubnet": rcOutbandIpSubnet,
       "rcOutbandIpSubnetTable": rcOutbandIpSubnetTable,
       "rcOutbandIpSubnetEntry": rcOutbandIpSubnetEntry,
       "rcOutbandIpSubnetIndex": rcOutbandIpSubnetIndex,
       "rcOutbandIpSubnetIpAddress": rcOutbandIpSubnetIpAddress,
       "rcOutbandIpSubnetMask": rcOutbandIpSubnetMask,
       "rcOutbandIpSubnetRowStatus": rcOutbandIpSubnetRowStatus}
)
