# SNMP MIB module (ZYXEL-VENDOR-ID-BASED-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-VENDOR-ID-BASED-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:02:48 2025
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelVendorIdBasedVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelVendorIdBasedVlanSetup_ObjectIdentity = ObjectIdentity
zyxelVendorIdBasedVlanSetup = _ZyxelVendorIdBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1)
)
_ZyVendorIdBasedVlanMaxNumberOfVlans_Type = Integer32
_ZyVendorIdBasedVlanMaxNumberOfVlans_Object = MibScalar
zyVendorIdBasedVlanMaxNumberOfVlans = _ZyVendorIdBasedVlanMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 1),
    _ZyVendorIdBasedVlanMaxNumberOfVlans_Type()
)
zyVendorIdBasedVlanMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVendorIdBasedVlanMaxNumberOfVlans.setStatus("current")
_ZyxelVendorIdBasedVlanBindingTable_Object = MibTable
zyxelVendorIdBasedVlanBindingTable = _ZyxelVendorIdBasedVlanBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelVendorIdBasedVlanBindingTable.setStatus("current")
_ZyxelVendorIdBasedVlanBindingEntry_Object = MibTableRow
zyxelVendorIdBasedVlanBindingEntry = _ZyxelVendorIdBasedVlanBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 2, 1)
)
zyxelVendorIdBasedVlanBindingEntry.setIndexNames(
    (0, "ZYXEL-VENDOR-ID-BASED-VLAN-MIB", "zyVendorIdBasedVlanBindingSourceMac"),
    (0, "ZYXEL-VENDOR-ID-BASED-VLAN-MIB", "zyVendorIdBasedVlanBindingMask"),
)
if mibBuilder.loadTexts:
    zyxelVendorIdBasedVlanBindingEntry.setStatus("current")
_ZyVendorIdBasedVlanBindingSourceMac_Type = MacAddress
_ZyVendorIdBasedVlanBindingSourceMac_Object = MibTableColumn
zyVendorIdBasedVlanBindingSourceMac = _ZyVendorIdBasedVlanBindingSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 2, 1, 1),
    _ZyVendorIdBasedVlanBindingSourceMac_Type()
)
zyVendorIdBasedVlanBindingSourceMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVendorIdBasedVlanBindingSourceMac.setStatus("current")
_ZyVendorIdBasedVlanBindingMask_Type = MacAddress
_ZyVendorIdBasedVlanBindingMask_Object = MibTableColumn
zyVendorIdBasedVlanBindingMask = _ZyVendorIdBasedVlanBindingMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 2, 1, 2),
    _ZyVendorIdBasedVlanBindingMask_Type()
)
zyVendorIdBasedVlanBindingMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVendorIdBasedVlanBindingMask.setStatus("current")
_ZyVendorIdBasedVlanBindingName_Type = OctetString
_ZyVendorIdBasedVlanBindingName_Object = MibTableColumn
zyVendorIdBasedVlanBindingName = _ZyVendorIdBasedVlanBindingName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 2, 1, 3),
    _ZyVendorIdBasedVlanBindingName_Type()
)
zyVendorIdBasedVlanBindingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVendorIdBasedVlanBindingName.setStatus("current")


class _ZyVendorIdBasedVlanBindingVlan_Type(Integer32):
    """Custom type zyVendorIdBasedVlanBindingVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyVendorIdBasedVlanBindingVlan_Type.__name__ = "Integer32"
_ZyVendorIdBasedVlanBindingVlan_Object = MibTableColumn
zyVendorIdBasedVlanBindingVlan = _ZyVendorIdBasedVlanBindingVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 2, 1, 4),
    _ZyVendorIdBasedVlanBindingVlan_Type()
)
zyVendorIdBasedVlanBindingVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVendorIdBasedVlanBindingVlan.setStatus("current")


class _ZyVendorIdBasedVlanBindingPriority_Type(Integer32):
    """Custom type zyVendorIdBasedVlanBindingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZyVendorIdBasedVlanBindingPriority_Type.__name__ = "Integer32"
_ZyVendorIdBasedVlanBindingPriority_Object = MibTableColumn
zyVendorIdBasedVlanBindingPriority = _ZyVendorIdBasedVlanBindingPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 2, 1, 5),
    _ZyVendorIdBasedVlanBindingPriority_Type()
)
zyVendorIdBasedVlanBindingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVendorIdBasedVlanBindingPriority.setStatus("current")


class _ZyVendorIdBasedVlanBindingWeight_Type(Integer32):
    """Custom type zyVendorIdBasedVlanBindingWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZyVendorIdBasedVlanBindingWeight_Type.__name__ = "Integer32"
_ZyVendorIdBasedVlanBindingWeight_Object = MibTableColumn
zyVendorIdBasedVlanBindingWeight = _ZyVendorIdBasedVlanBindingWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 2, 1, 6),
    _ZyVendorIdBasedVlanBindingWeight_Type()
)
zyVendorIdBasedVlanBindingWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVendorIdBasedVlanBindingWeight.setStatus("current")
_ZyVendorIdBasedVlanBindingRowStatus_Type = RowStatus
_ZyVendorIdBasedVlanBindingRowStatus_Object = MibTableColumn
zyVendorIdBasedVlanBindingRowStatus = _ZyVendorIdBasedVlanBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 120, 1, 2, 1, 7),
    _ZyVendorIdBasedVlanBindingRowStatus_Type()
)
zyVendorIdBasedVlanBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyVendorIdBasedVlanBindingRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-VENDOR-ID-BASED-VLAN-MIB",
    **{"zyxelVendorIdBasedVlan": zyxelVendorIdBasedVlan,
       "zyxelVendorIdBasedVlanSetup": zyxelVendorIdBasedVlanSetup,
       "zyVendorIdBasedVlanMaxNumberOfVlans": zyVendorIdBasedVlanMaxNumberOfVlans,
       "zyxelVendorIdBasedVlanBindingTable": zyxelVendorIdBasedVlanBindingTable,
       "zyxelVendorIdBasedVlanBindingEntry": zyxelVendorIdBasedVlanBindingEntry,
       "zyVendorIdBasedVlanBindingSourceMac": zyVendorIdBasedVlanBindingSourceMac,
       "zyVendorIdBasedVlanBindingMask": zyVendorIdBasedVlanBindingMask,
       "zyVendorIdBasedVlanBindingName": zyVendorIdBasedVlanBindingName,
       "zyVendorIdBasedVlanBindingVlan": zyVendorIdBasedVlanBindingVlan,
       "zyVendorIdBasedVlanBindingPriority": zyVendorIdBasedVlanBindingPriority,
       "zyVendorIdBasedVlanBindingWeight": zyVendorIdBasedVlanBindingWeight,
       "zyVendorIdBasedVlanBindingRowStatus": zyVendorIdBasedVlanBindingRowStatus}
)
