# SNMP MIB module (SUPERVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/SUPERVLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:45 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

swSuperVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 91)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSuperVlanMIBObjects_ObjectIdentity = ObjectIdentity
swSuperVlanMIBObjects = _SwSuperVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1)
)
_SwSuperVlanTable_Object = MibTable
swSuperVlanTable = _SwSuperVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1)
)
if mibBuilder.loadTexts:
    swSuperVlanTable.setStatus("current")
_SwSuperVlanEntry_Object = MibTableRow
swSuperVlanEntry = _SwSuperVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1)
)
swSuperVlanEntry.setIndexNames(
    (0, "SUPERVLAN-MIB", "swSuperVlanId"),
)
if mibBuilder.loadTexts:
    swSuperVlanEntry.setStatus("current")
_SwSuperVlanId_Type = VlanIndex
_SwSuperVlanId_Object = MibTableColumn
swSuperVlanId = _SwSuperVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 1),
    _SwSuperVlanId_Type()
)
swSuperVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSuperVlanId.setStatus("current")
_SwSuperVlanIPAddress_Type = IpAddress
_SwSuperVlanIPAddress_Object = MibTableColumn
swSuperVlanIPAddress = _SwSuperVlanIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 2),
    _SwSuperVlanIPAddress_Type()
)
swSuperVlanIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSuperVlanIPAddress.setStatus("current")
_SwSuperVlanIPAddrMask_Type = IpAddress
_SwSuperVlanIPAddrMask_Object = MibTableColumn
swSuperVlanIPAddrMask = _SwSuperVlanIPAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 3),
    _SwSuperVlanIPAddrMask_Type()
)
swSuperVlanIPAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSuperVlanIPAddrMask.setStatus("current")


class _SwSubVlanList1to64_Type(OctetString):
    """Custom type swSubVlanList1to64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwSubVlanList1to64_Type.__name__ = "OctetString"
_SwSubVlanList1to64_Object = MibTableColumn
swSubVlanList1to64 = _SwSubVlanList1to64_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 4),
    _SwSubVlanList1to64_Type()
)
swSubVlanList1to64.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubVlanList1to64.setStatus("current")


class _SwSubVlanList65to128_Type(OctetString):
    """Custom type swSubVlanList65to128 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwSubVlanList65to128_Type.__name__ = "OctetString"
_SwSubVlanList65to128_Object = MibTableColumn
swSubVlanList65to128 = _SwSubVlanList65to128_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 5),
    _SwSubVlanList65to128_Type()
)
swSubVlanList65to128.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubVlanList65to128.setStatus("current")


class _SwSubVlanList129to192_Type(OctetString):
    """Custom type swSubVlanList129to192 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwSubVlanList129to192_Type.__name__ = "OctetString"
_SwSubVlanList129to192_Object = MibTableColumn
swSubVlanList129to192 = _SwSubVlanList129to192_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 6),
    _SwSubVlanList129to192_Type()
)
swSubVlanList129to192.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubVlanList129to192.setStatus("current")


class _SwSubVlanList193to256_Type(OctetString):
    """Custom type swSubVlanList193to256 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwSubVlanList193to256_Type.__name__ = "OctetString"
_SwSubVlanList193to256_Object = MibTableColumn
swSubVlanList193to256 = _SwSubVlanList193to256_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 7),
    _SwSubVlanList193to256_Type()
)
swSubVlanList193to256.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubVlanList193to256.setStatus("current")


class _SwSubVlanList257to320_Type(OctetString):
    """Custom type swSubVlanList257to320 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwSubVlanList257to320_Type.__name__ = "OctetString"
_SwSubVlanList257to320_Object = MibTableColumn
swSubVlanList257to320 = _SwSubVlanList257to320_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 8),
    _SwSubVlanList257to320_Type()
)
swSubVlanList257to320.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubVlanList257to320.setStatus("current")


class _SwSubVlanList321to384_Type(OctetString):
    """Custom type swSubVlanList321to384 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwSubVlanList321to384_Type.__name__ = "OctetString"
_SwSubVlanList321to384_Object = MibTableColumn
swSubVlanList321to384 = _SwSubVlanList321to384_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 9),
    _SwSubVlanList321to384_Type()
)
swSubVlanList321to384.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubVlanList321to384.setStatus("current")


class _SwSubVlanList385to448_Type(OctetString):
    """Custom type swSubVlanList385to448 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwSubVlanList385to448_Type.__name__ = "OctetString"
_SwSubVlanList385to448_Object = MibTableColumn
swSubVlanList385to448 = _SwSubVlanList385to448_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 10),
    _SwSubVlanList385to448_Type()
)
swSubVlanList385to448.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubVlanList385to448.setStatus("current")


class _SwSubVlanList449to512_Type(OctetString):
    """Custom type swSubVlanList449to512 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwSubVlanList449to512_Type.__name__ = "OctetString"
_SwSubVlanList449to512_Object = MibTableColumn
swSubVlanList449to512 = _SwSubVlanList449to512_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 11),
    _SwSubVlanList449to512_Type()
)
swSubVlanList449to512.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubVlanList449to512.setStatus("current")


class _SwSuperVlanStatus_Type(Integer32):
    """Custom type swSuperVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SwSuperVlanStatus_Type.__name__ = "Integer32"
_SwSuperVlanStatus_Object = MibTableColumn
swSuperVlanStatus = _SwSuperVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 12),
    _SwSuperVlanStatus_Type()
)
swSuperVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSuperVlanStatus.setStatus("current")
_SwSuperVlanRowStatus_Type = RowStatus
_SwSuperVlanRowStatus_Object = MibTableColumn
swSuperVlanRowStatus = _SwSuperVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 1, 1, 100),
    _SwSuperVlanRowStatus_Type()
)
swSuperVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSuperVlanRowStatus.setStatus("current")
_SwSubVlanTable_Object = MibTable
swSubVlanTable = _SwSubVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 2)
)
if mibBuilder.loadTexts:
    swSubVlanTable.setStatus("current")
_SwSubVlanEntry_Object = MibTableRow
swSubVlanEntry = _SwSubVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 2, 1)
)
swSubVlanEntry.setIndexNames(
    (0, "SUPERVLAN-MIB", "swSubVlanId"),
)
if mibBuilder.loadTexts:
    swSubVlanEntry.setStatus("current")
_SwSubVlanId_Type = VlanIndex
_SwSubVlanId_Object = MibTableColumn
swSubVlanId = _SwSubVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 2, 1, 1),
    _SwSubVlanId_Type()
)
swSubVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSubVlanId.setStatus("current")


class _SwSubVlanOperStatus_Type(Integer32):
    """Custom type swSubVlanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SwSubVlanOperStatus_Type.__name__ = "Integer32"
_SwSubVlanOperStatus_Object = MibTableColumn
swSubVlanOperStatus = _SwSubVlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 2, 1, 2),
    _SwSubVlanOperStatus_Type()
)
swSubVlanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSubVlanOperStatus.setStatus("current")
_SwSubVlanIPRangeTable_Object = MibTable
swSubVlanIPRangeTable = _SwSubVlanIPRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 3)
)
if mibBuilder.loadTexts:
    swSubVlanIPRangeTable.setStatus("current")
_SwSubVlanIPRangeEntry_Object = MibTableRow
swSubVlanIPRangeEntry = _SwSubVlanIPRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 3, 1)
)
swSubVlanIPRangeEntry.setIndexNames(
    (0, "SUPERVLAN-MIB", "swSubVlanId"),
    (0, "SUPERVLAN-MIB", "swSubVlanIPAddressRangeFrom"),
    (0, "SUPERVLAN-MIB", "swSubVlanIPAddressRangeTo"),
)
if mibBuilder.loadTexts:
    swSubVlanIPRangeEntry.setStatus("current")
_SwSubVlanIPAddressRangeFrom_Type = IpAddress
_SwSubVlanIPAddressRangeFrom_Object = MibTableColumn
swSubVlanIPAddressRangeFrom = _SwSubVlanIPAddressRangeFrom_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 3, 1, 1),
    _SwSubVlanIPAddressRangeFrom_Type()
)
swSubVlanIPAddressRangeFrom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSubVlanIPAddressRangeFrom.setStatus("current")
_SwSubVlanIPAddressRangeTo_Type = IpAddress
_SwSubVlanIPAddressRangeTo_Object = MibTableColumn
swSubVlanIPAddressRangeTo = _SwSubVlanIPAddressRangeTo_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 3, 1, 2),
    _SwSubVlanIPAddressRangeTo_Type()
)
swSubVlanIPAddressRangeTo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSubVlanIPAddressRangeTo.setStatus("current")
_SwSubVlanRowStatus_Type = RowStatus
_SwSubVlanRowStatus_Object = MibTableColumn
swSubVlanRowStatus = _SwSubVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 91, 1, 3, 1, 100),
    _SwSubVlanRowStatus_Type()
)
swSubVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERVLAN-MIB",
    **{"swSuperVlanMIB": swSuperVlanMIB,
       "swSuperVlanMIBObjects": swSuperVlanMIBObjects,
       "swSuperVlanTable": swSuperVlanTable,
       "swSuperVlanEntry": swSuperVlanEntry,
       "swSuperVlanId": swSuperVlanId,
       "swSuperVlanIPAddress": swSuperVlanIPAddress,
       "swSuperVlanIPAddrMask": swSuperVlanIPAddrMask,
       "swSubVlanList1to64": swSubVlanList1to64,
       "swSubVlanList65to128": swSubVlanList65to128,
       "swSubVlanList129to192": swSubVlanList129to192,
       "swSubVlanList193to256": swSubVlanList193to256,
       "swSubVlanList257to320": swSubVlanList257to320,
       "swSubVlanList321to384": swSubVlanList321to384,
       "swSubVlanList385to448": swSubVlanList385to448,
       "swSubVlanList449to512": swSubVlanList449to512,
       "swSuperVlanStatus": swSuperVlanStatus,
       "swSuperVlanRowStatus": swSuperVlanRowStatus,
       "swSubVlanTable": swSubVlanTable,
       "swSubVlanEntry": swSubVlanEntry,
       "swSubVlanId": swSubVlanId,
       "swSubVlanOperStatus": swSubVlanOperStatus,
       "swSubVlanIPRangeTable": swSubVlanIPRangeTable,
       "swSubVlanIPRangeEntry": swSubVlanIPRangeEntry,
       "swSubVlanIPAddressRangeFrom": swSubVlanIPAddressRangeFrom,
       "swSubVlanIPAddressRangeTo": swSubVlanIPAddressRangeTo,
       "swSubVlanRowStatus": swSubVlanRowStatus}
)
