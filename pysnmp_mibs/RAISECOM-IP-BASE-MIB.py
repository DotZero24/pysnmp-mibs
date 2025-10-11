# SNMP MIB module (RAISECOM-IP-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-IP-BASE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:10 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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


# MODULE-IDENTITY

rcIpBaseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpAddressCatagory(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("sub", 2),
          ("linklocal", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RcL3_ObjectIdentity = ObjectIdentity
rcL3 = _RcL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16)
)
_RcIpBaseMibObjects_ObjectIdentity = ObjectIdentity
rcIpBaseMibObjects = _RcIpBaseMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1)
)
_RcIpBaseScalarGroup_ObjectIdentity = ObjectIdentity
rcIpBaseScalarGroup = _RcIpBaseScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 1)
)
_RcIpBaseTableGroup_ObjectIdentity = ObjectIdentity
rcIpBaseTableGroup = _RcIpBaseTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2)
)
_RcIpBaseAddressTable_Object = MibTable
rcIpBaseAddressTable = _RcIpBaseAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcIpBaseAddressTable.setStatus("current")
_RcIpBaseAddressEntry_Object = MibTableRow
rcIpBaseAddressEntry = _RcIpBaseAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 1, 1)
)
rcIpBaseAddressEntry.setIndexNames(
    (0, "RAISECOM-IP-BASE-MIB", "rcIpBaseAddressIfIndex"),
    (0, "RAISECOM-IP-BASE-MIB", "rcIpBaseAddresstType"),
    (0, "RAISECOM-IP-BASE-MIB", "rcIpBaseAddress"),
)
if mibBuilder.loadTexts:
    rcIpBaseAddressEntry.setStatus("current")
_RcIpBaseAddressIfIndex_Type = Integer32
_RcIpBaseAddressIfIndex_Object = MibTableColumn
rcIpBaseAddressIfIndex = _RcIpBaseAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 1, 1, 1),
    _RcIpBaseAddressIfIndex_Type()
)
rcIpBaseAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpBaseAddressIfIndex.setStatus("current")
_RcIpBaseAddresstType_Type = InetAddressType
_RcIpBaseAddresstType_Object = MibTableColumn
rcIpBaseAddresstType = _RcIpBaseAddresstType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 1, 1, 2),
    _RcIpBaseAddresstType_Type()
)
rcIpBaseAddresstType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpBaseAddresstType.setStatus("current")
_RcIpBaseAddress_Type = InetAddress
_RcIpBaseAddress_Object = MibTableColumn
rcIpBaseAddress = _RcIpBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 1, 1, 3),
    _RcIpBaseAddress_Type()
)
rcIpBaseAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpBaseAddress.setStatus("current")
_RcIpBaseAddressPrefixLength_Type = InetAddressPrefixLength
_RcIpBaseAddressPrefixLength_Object = MibTableColumn
rcIpBaseAddressPrefixLength = _RcIpBaseAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 1, 1, 4),
    _RcIpBaseAddressPrefixLength_Type()
)
rcIpBaseAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpBaseAddressPrefixLength.setStatus("current")


class _RcIpBaseAddressSourceType_Type(Integer32):
    """Custom type rcIpBaseAddressSourceType based on Integer32"""
    defaultValue = 1

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
        *(("assignedIp", 1),
          ("cluster", 2),
          ("dhcp", 3),
          ("bootp", 4),
          ("negotiate", 5),
          ("unnumbered", 6))
    )


_RcIpBaseAddressSourceType_Type.__name__ = "Integer32"
_RcIpBaseAddressSourceType_Object = MibTableColumn
rcIpBaseAddressSourceType = _RcIpBaseAddressSourceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 1, 1, 5),
    _RcIpBaseAddressSourceType_Type()
)
rcIpBaseAddressSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpBaseAddressSourceType.setStatus("current")


class _RcIpBaseAddressCatagory_Type(IpAddressCatagory):
    """Custom type rcIpBaseAddressCatagory based on IpAddressCatagory"""
    defaultValue = 1


_RcIpBaseAddressCatagory_Type.__name__ = "IpAddressCatagory"
_RcIpBaseAddressCatagory_Object = MibTableColumn
rcIpBaseAddressCatagory = _RcIpBaseAddressCatagory_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 1, 1, 6),
    _RcIpBaseAddressCatagory_Type()
)
rcIpBaseAddressCatagory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpBaseAddressCatagory.setStatus("current")
_RcIpBaseAddressRowStatus_Type = RowStatus
_RcIpBaseAddressRowStatus_Object = MibTableColumn
rcIpBaseAddressRowStatus = _RcIpBaseAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 1, 1, 7),
    _RcIpBaseAddressRowStatus_Type()
)
rcIpBaseAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpBaseAddressRowStatus.setStatus("current")
_RcVlanInterfaceIndexTable_Object = MibTable
rcVlanInterfaceIndexTable = _RcVlanInterfaceIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rcVlanInterfaceIndexTable.setStatus("current")
_RcVlanInterfaceIndexEntry_Object = MibTableRow
rcVlanInterfaceIndexEntry = _RcVlanInterfaceIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 2, 1)
)
rcVlanInterfaceIndexEntry.setIndexNames(
    (0, "RAISECOM-IP-BASE-MIB", "rcVlanId"),
)
if mibBuilder.loadTexts:
    rcVlanInterfaceIndexEntry.setStatus("current")
_RcVlanId_Type = Integer32
_RcVlanId_Object = MibTableColumn
rcVlanId = _RcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 2, 1, 1),
    _RcVlanId_Type()
)
rcVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcVlanId.setStatus("current")
_RcVlanIfIndex_Type = Integer32
_RcVlanIfIndex_Object = MibTableColumn
rcVlanIfIndex = _RcVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 2, 1, 2),
    _RcVlanIfIndex_Type()
)
rcVlanIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanIfIndex.setStatus("current")
_RcVlanIfIndexRowStatus_Type = RowStatus
_RcVlanIfIndexRowStatus_Object = MibTableColumn
rcVlanIfIndexRowStatus = _RcVlanIfIndexRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 2, 1, 3),
    _RcVlanIfIndexRowStatus_Type()
)
rcVlanIfIndexRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanIfIndexRowStatus.setStatus("current")
_RcIpBaseManVlanTable_Object = MibTable
rcIpBaseManVlanTable = _RcIpBaseManVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rcIpBaseManVlanTable.setStatus("current")
_RcIpBaseManVlanEntry_Object = MibTableRow
rcIpBaseManVlanEntry = _RcIpBaseManVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 3, 1)
)
rcIpBaseManVlanEntry.setIndexNames(
    (0, "RAISECOM-IP-BASE-MIB", "rcIpBaseManVlanIfIndex"),
)
if mibBuilder.loadTexts:
    rcIpBaseManVlanEntry.setStatus("current")
_RcIpBaseManVlanIfIndex_Type = Integer32
_RcIpBaseManVlanIfIndex_Object = MibTableColumn
rcIpBaseManVlanIfIndex = _RcIpBaseManVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 3, 1, 1),
    _RcIpBaseManVlanIfIndex_Type()
)
rcIpBaseManVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpBaseManVlanIfIndex.setStatus("current")


class _RcIpBaseManVlanMode_Type(Integer32):
    """Custom type rcIpBaseManVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("single-taging", 1),
          ("double-taging", 2))
    )


_RcIpBaseManVlanMode_Type.__name__ = "Integer32"
_RcIpBaseManVlanMode_Object = MibTableColumn
rcIpBaseManVlanMode = _RcIpBaseManVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 3, 1, 2),
    _RcIpBaseManVlanMode_Type()
)
rcIpBaseManVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpBaseManVlanMode.setStatus("current")


class _RcIpBaseInnerVlan_Type(Integer32):
    """Custom type rcIpBaseInnerVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcIpBaseInnerVlan_Type.__name__ = "Integer32"
_RcIpBaseInnerVlan_Object = MibTableColumn
rcIpBaseInnerVlan = _RcIpBaseInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 3, 1, 3),
    _RcIpBaseInnerVlan_Type()
)
rcIpBaseInnerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpBaseInnerVlan.setStatus("current")


class _RcIpBaseCos_Type(Integer32):
    """Custom type rcIpBaseCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcIpBaseCos_Type.__name__ = "Integer32"
_RcIpBaseCos_Object = MibTableColumn
rcIpBaseCos = _RcIpBaseCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 3, 1, 4),
    _RcIpBaseCos_Type()
)
rcIpBaseCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpBaseCos.setStatus("current")


class _RcIpBaseInnerCos_Type(Integer32):
    """Custom type rcIpBaseInnerCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcIpBaseInnerCos_Type.__name__ = "Integer32"
_RcIpBaseInnerCos_Object = MibTableColumn
rcIpBaseInnerCos = _RcIpBaseInnerCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 3, 1, 5),
    _RcIpBaseInnerCos_Type()
)
rcIpBaseInnerCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpBaseInnerCos.setStatus("current")


class _RcIpBaseTpid_Type(Integer32):
    """Custom type rcIpBaseTpid based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIpBaseTpid_Type.__name__ = "Integer32"
_RcIpBaseTpid_Object = MibTableColumn
rcIpBaseTpid = _RcIpBaseTpid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 3, 1, 6),
    _RcIpBaseTpid_Type()
)
rcIpBaseTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpBaseTpid.setStatus("current")


class _RcIpBaseInnerTpid_Type(Integer32):
    """Custom type rcIpBaseInnerTpid based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcIpBaseInnerTpid_Type.__name__ = "Integer32"
_RcIpBaseInnerTpid_Object = MibTableColumn
rcIpBaseInnerTpid = _RcIpBaseInnerTpid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 3, 1, 7),
    _RcIpBaseInnerTpid_Type()
)
rcIpBaseInnerTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpBaseInnerTpid.setStatus("current")
_RcIpIfMtuTable_Object = MibTable
rcIpIfMtuTable = _RcIpIfMtuTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rcIpIfMtuTable.setStatus("current")
_RcIpIfMtuEntry_Object = MibTableRow
rcIpIfMtuEntry = _RcIpIfMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 4, 1)
)
rcIpIfMtuEntry.setIndexNames(
    (0, "RAISECOM-IP-BASE-MIB", "rcIpIfIndex"),
)
if mibBuilder.loadTexts:
    rcIpIfMtuEntry.setStatus("current")
_RcIpIfIndex_Type = Integer32
_RcIpIfIndex_Object = MibTableColumn
rcIpIfIndex = _RcIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 4, 1, 1),
    _RcIpIfIndex_Type()
)
rcIpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpIfIndex.setStatus("current")


class _RcIpIfMtu_Type(Integer32):
    """Custom type rcIpIfMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 9216),
    )


_RcIpIfMtu_Type.__name__ = "Integer32"
_RcIpIfMtu_Object = MibTableColumn
rcIpIfMtu = _RcIpIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 16, 4, 1, 2, 4, 1, 2),
    _RcIpIfMtu_Type()
)
rcIpIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpIfMtu.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-IP-BASE-MIB",
    **{"IpAddressCatagory": IpAddressCatagory,
       "rcL3": rcL3,
       "rcIpBaseMIB": rcIpBaseMIB,
       "rcIpBaseMibObjects": rcIpBaseMibObjects,
       "rcIpBaseScalarGroup": rcIpBaseScalarGroup,
       "rcIpBaseTableGroup": rcIpBaseTableGroup,
       "rcIpBaseAddressTable": rcIpBaseAddressTable,
       "rcIpBaseAddressEntry": rcIpBaseAddressEntry,
       "rcIpBaseAddressIfIndex": rcIpBaseAddressIfIndex,
       "rcIpBaseAddresstType": rcIpBaseAddresstType,
       "rcIpBaseAddress": rcIpBaseAddress,
       "rcIpBaseAddressPrefixLength": rcIpBaseAddressPrefixLength,
       "rcIpBaseAddressSourceType": rcIpBaseAddressSourceType,
       "rcIpBaseAddressCatagory": rcIpBaseAddressCatagory,
       "rcIpBaseAddressRowStatus": rcIpBaseAddressRowStatus,
       "rcVlanInterfaceIndexTable": rcVlanInterfaceIndexTable,
       "rcVlanInterfaceIndexEntry": rcVlanInterfaceIndexEntry,
       "rcVlanId": rcVlanId,
       "rcVlanIfIndex": rcVlanIfIndex,
       "rcVlanIfIndexRowStatus": rcVlanIfIndexRowStatus,
       "rcIpBaseManVlanTable": rcIpBaseManVlanTable,
       "rcIpBaseManVlanEntry": rcIpBaseManVlanEntry,
       "rcIpBaseManVlanIfIndex": rcIpBaseManVlanIfIndex,
       "rcIpBaseManVlanMode": rcIpBaseManVlanMode,
       "rcIpBaseInnerVlan": rcIpBaseInnerVlan,
       "rcIpBaseCos": rcIpBaseCos,
       "rcIpBaseInnerCos": rcIpBaseInnerCos,
       "rcIpBaseTpid": rcIpBaseTpid,
       "rcIpBaseInnerTpid": rcIpBaseInnerTpid,
       "rcIpIfMtuTable": rcIpIfMtuTable,
       "rcIpIfMtuEntry": rcIpIfMtuEntry,
       "rcIpIfIndex": rcIpIfIndex,
       "rcIpIfMtu": rcIpIfMtu}
)
