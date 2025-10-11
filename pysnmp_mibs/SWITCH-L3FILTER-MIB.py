# SNMP MIB module (SWITCH-L3FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-L3FILTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:05 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(PortList,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "PortList")


# MODULE-IDENTITY

rcL3Filter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcL3IpSubnetFilter_ObjectIdentity = ObjectIdentity
rcL3IpSubnetFilter = _RcL3IpSubnetFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1)
)
_RcL3IpSubnetFilterTable_Object = MibTable
rcL3IpSubnetFilterTable = _RcL3IpSubnetFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    rcL3IpSubnetFilterTable.setStatus("current")
_RcL3IpSubnetFilterEntry_Object = MibTableRow
rcL3IpSubnetFilterEntry = _RcL3IpSubnetFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1)
)
rcL3IpSubnetFilterEntry.setIndexNames(
    (0, "SWITCH-L3FILTER-MIB", "rcL3IpSubnetFilterIfIndex"),
    (0, "SWITCH-L3FILTER-MIB", "rcL3IpSubnetFilterIPAclNumber"),
)
if mibBuilder.loadTexts:
    rcL3IpSubnetFilterEntry.setStatus("current")
_RcL3IpSubnetFilterIfIndex_Type = Integer32
_RcL3IpSubnetFilterIfIndex_Object = MibTableColumn
rcL3IpSubnetFilterIfIndex = _RcL3IpSubnetFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1, 1),
    _RcL3IpSubnetFilterIfIndex_Type()
)
rcL3IpSubnetFilterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3IpSubnetFilterIfIndex.setStatus("current")
_RcL3IpSubnetFilterIPAclNumber_Type = Integer32
_RcL3IpSubnetFilterIPAclNumber_Object = MibTableColumn
rcL3IpSubnetFilterIPAclNumber = _RcL3IpSubnetFilterIPAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1, 2),
    _RcL3IpSubnetFilterIPAclNumber_Type()
)
rcL3IpSubnetFilterIPAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcL3IpSubnetFilterIPAclNumber.setStatus("current")
_RcL3IpSubnetFilterStatus_Type = RowStatus
_RcL3IpSubnetFilterStatus_Object = MibTableColumn
rcL3IpSubnetFilterStatus = _RcL3IpSubnetFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1, 3),
    _RcL3IpSubnetFilterStatus_Type()
)
rcL3IpSubnetFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpSubnetFilterStatus.setStatus("current")
_RcL3IpSubnetFilterPorts_Type = PortList
_RcL3IpSubnetFilterPorts_Object = MibTableColumn
rcL3IpSubnetFilterPorts = _RcL3IpSubnetFilterPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1, 4),
    _RcL3IpSubnetFilterPorts_Type()
)
rcL3IpSubnetFilterPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcL3IpSubnetFilterPorts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-L3FILTER-MIB",
    **{"rcL3Filter": rcL3Filter,
       "rcL3IpSubnetFilter": rcL3IpSubnetFilter,
       "rcL3IpSubnetFilterTable": rcL3IpSubnetFilterTable,
       "rcL3IpSubnetFilterEntry": rcL3IpSubnetFilterEntry,
       "rcL3IpSubnetFilterIfIndex": rcL3IpSubnetFilterIfIndex,
       "rcL3IpSubnetFilterIPAclNumber": rcL3IpSubnetFilterIPAclNumber,
       "rcL3IpSubnetFilterStatus": rcL3IpSubnetFilterStatus,
       "rcL3IpSubnetFilterPorts": rcL3IpSubnetFilterPorts}
)
