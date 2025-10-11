# SNMP MIB module (RADLAN-ARPSPOOFING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radlan/RADLAN-ARPSPOOFING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:10:39 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rlArpSpoofing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 60)
)
if mibBuilder.loadTexts:
    rlArpSpoofing.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlArpSpoofingMibVersion_Type = Integer32
_RlArpSpoofingMibVersion_Object = MibScalar
rlArpSpoofingMibVersion = _RlArpSpoofingMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 1),
    _RlArpSpoofingMibVersion_Type()
)
rlArpSpoofingMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlArpSpoofingMibVersion.setStatus("current")
_RlArpSpoofingTable_Object = MibTable
rlArpSpoofingTable = _RlArpSpoofingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2)
)
if mibBuilder.loadTexts:
    rlArpSpoofingTable.setStatus("current")
_RlArpSpoofingEntry_Object = MibTableRow
rlArpSpoofingEntry = _RlArpSpoofingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1)
)
rlArpSpoofingEntry.setIndexNames(
    (0, "RADLAN-ARPSPOOFING-MIB", "rlArpSpoofingIfIndex"),
    (0, "RADLAN-ARPSPOOFING-MIB", "rlArpSpoofingLocalIpAddr"),
)
if mibBuilder.loadTexts:
    rlArpSpoofingEntry.setStatus("current")
_RlArpSpoofingIfIndex_Type = InterfaceIndex
_RlArpSpoofingIfIndex_Object = MibTableColumn
rlArpSpoofingIfIndex = _RlArpSpoofingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 1),
    _RlArpSpoofingIfIndex_Type()
)
rlArpSpoofingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingIfIndex.setStatus("current")
_RlArpSpoofingLocalIpAddr_Type = IpAddress
_RlArpSpoofingLocalIpAddr_Object = MibTableColumn
rlArpSpoofingLocalIpAddr = _RlArpSpoofingLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 2),
    _RlArpSpoofingLocalIpAddr_Type()
)
rlArpSpoofingLocalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingLocalIpAddr.setStatus("current")
_RlArpSpoofingMacAddr_Type = PhysAddress
_RlArpSpoofingMacAddr_Object = MibTableColumn
rlArpSpoofingMacAddr = _RlArpSpoofingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 3),
    _RlArpSpoofingMacAddr_Type()
)
rlArpSpoofingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingMacAddr.setStatus("current")
_RlArpSpoofingRemoteIpAddr_Type = IpAddress
_RlArpSpoofingRemoteIpAddr_Object = MibTableColumn
rlArpSpoofingRemoteIpAddr = _RlArpSpoofingRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 4),
    _RlArpSpoofingRemoteIpAddr_Type()
)
rlArpSpoofingRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingRemoteIpAddr.setStatus("current")


class _RlArpSpoofingOutPhysIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rlArpSpoofingOutPhysIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RlArpSpoofingOutPhysIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_RlArpSpoofingOutPhysIfIndex_Object = MibTableColumn
rlArpSpoofingOutPhysIfIndex = _RlArpSpoofingOutPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 5),
    _RlArpSpoofingOutPhysIfIndex_Type()
)
rlArpSpoofingOutPhysIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingOutPhysIfIndex.setStatus("current")
_RlArpSpoofingStatus_Type = RowStatus
_RlArpSpoofingStatus_Object = MibTableColumn
rlArpSpoofingStatus = _RlArpSpoofingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 60, 2, 1, 6),
    _RlArpSpoofingStatus_Type()
)
rlArpSpoofingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlArpSpoofingStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-ARPSPOOFING-MIB",
    **{"rlArpSpoofing": rlArpSpoofing,
       "rlArpSpoofingMibVersion": rlArpSpoofingMibVersion,
       "rlArpSpoofingTable": rlArpSpoofingTable,
       "rlArpSpoofingEntry": rlArpSpoofingEntry,
       "rlArpSpoofingIfIndex": rlArpSpoofingIfIndex,
       "rlArpSpoofingLocalIpAddr": rlArpSpoofingLocalIpAddr,
       "rlArpSpoofingMacAddr": rlArpSpoofingMacAddr,
       "rlArpSpoofingRemoteIpAddr": rlArpSpoofingRemoteIpAddr,
       "rlArpSpoofingOutPhysIfIndex": rlArpSpoofingOutPhysIfIndex,
       "rlArpSpoofingStatus": rlArpSpoofingStatus}
)
