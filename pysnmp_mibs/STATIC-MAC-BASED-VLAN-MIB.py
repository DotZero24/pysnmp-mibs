# SNMP MIB module (STATIC-MAC-BASED-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/STATIC-MAC-BASED-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:45:38 2025
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

swSMBVMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSmbvCtrl_ObjectIdentity = ObjectIdentity
swSmbvCtrl = _SwSmbvCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 1)
)
_SwSmbvInfo_ObjectIdentity = ObjectIdentity
swSmbvInfo = _SwSmbvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 2)
)
_SwSmbvMgmt_ObjectIdentity = ObjectIdentity
swSmbvMgmt = _SwSmbvMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3)
)
_SwStaticMacBasedVlanCtrlTable_Object = MibTable
swStaticMacBasedVlanCtrlTable = _SwStaticMacBasedVlanCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1)
)
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlTable.setStatus("obsolete")
_SwStaticMacBasedVlanCtrlEntry_Object = MibTableRow
swStaticMacBasedVlanCtrlEntry = _SwStaticMacBasedVlanCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1, 1)
)
swStaticMacBasedVlanCtrlEntry.setIndexNames(
    (0, "STATIC-MAC-BASED-VLAN-MIB", "swStaticMacBasedVlanCtrlMacAddr"),
)
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlEntry.setStatus("obsolete")
_SwStaticMacBasedVlanCtrlMacAddr_Type = MacAddress
_SwStaticMacBasedVlanCtrlMacAddr_Object = MibTableColumn
swStaticMacBasedVlanCtrlMacAddr = _SwStaticMacBasedVlanCtrlMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1, 1, 1),
    _SwStaticMacBasedVlanCtrlMacAddr_Type()
)
swStaticMacBasedVlanCtrlMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlMacAddr.setStatus("obsolete")


class _SwStaticMacBasedVlanCtrlVlanName_Type(DisplayString):
    """Custom type swStaticMacBasedVlanCtrlVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwStaticMacBasedVlanCtrlVlanName_Type.__name__ = "DisplayString"
_SwStaticMacBasedVlanCtrlVlanName_Object = MibTableColumn
swStaticMacBasedVlanCtrlVlanName = _SwStaticMacBasedVlanCtrlVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1, 1, 2),
    _SwStaticMacBasedVlanCtrlVlanName_Type()
)
swStaticMacBasedVlanCtrlVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlVlanName.setStatus("obsolete")
_SwStaticMacBasedVlanCtrlStatus_Type = RowStatus
_SwStaticMacBasedVlanCtrlStatus_Object = MibTableColumn
swStaticMacBasedVlanCtrlStatus = _SwStaticMacBasedVlanCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 1, 1, 3),
    _SwStaticMacBasedVlanCtrlStatus_Type()
)
swStaticMacBasedVlanCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlStatus.setStatus("obsolete")
_SwStaticMacBasedVlanCtrlOptionTable_Object = MibTable
swStaticMacBasedVlanCtrlOptionTable = _SwStaticMacBasedVlanCtrlOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2)
)
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlOptionTable.setStatus("current")
_SwStaticMacBasedVlanCtrlOptionEntry_Object = MibTableRow
swStaticMacBasedVlanCtrlOptionEntry = _SwStaticMacBasedVlanCtrlOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1)
)
swStaticMacBasedVlanCtrlOptionEntry.setIndexNames(
    (0, "STATIC-MAC-BASED-VLAN-MIB", "swStaticMacBasedVlanCtrlOptionMacAddr"),
    (0, "STATIC-MAC-BASED-VLAN-MIB", "swStaticMacBasedOptionVlanID"),
)
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlOptionEntry.setStatus("current")
_SwStaticMacBasedVlanCtrlOptionMacAddr_Type = MacAddress
_SwStaticMacBasedVlanCtrlOptionMacAddr_Object = MibTableColumn
swStaticMacBasedVlanCtrlOptionMacAddr = _SwStaticMacBasedVlanCtrlOptionMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1, 1),
    _SwStaticMacBasedVlanCtrlOptionMacAddr_Type()
)
swStaticMacBasedVlanCtrlOptionMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlOptionMacAddr.setStatus("current")


class _SwStaticMacBasedOptionVlanID_Type(Integer32):
    """Custom type swStaticMacBasedOptionVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwStaticMacBasedOptionVlanID_Type.__name__ = "Integer32"
_SwStaticMacBasedOptionVlanID_Object = MibTableColumn
swStaticMacBasedOptionVlanID = _SwStaticMacBasedOptionVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1, 2),
    _SwStaticMacBasedOptionVlanID_Type()
)
swStaticMacBasedOptionVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swStaticMacBasedOptionVlanID.setStatus("current")


class _SwStaticMacBasedVlanCtrlOptionType_Type(Integer32):
    """Custom type swStaticMacBasedVlanCtrlOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("mac-based-access-control", 2),
          ("ieee8021x", 3),
          ("wac", 4),
          ("jwac", 5),
          ("compound-authentication", 6),
          ("others", 7),
          ("voice-vlan", 8),
          ("surveillance-vlan", 9))
    )


_SwStaticMacBasedVlanCtrlOptionType_Type.__name__ = "Integer32"
_SwStaticMacBasedVlanCtrlOptionType_Object = MibTableColumn
swStaticMacBasedVlanCtrlOptionType = _SwStaticMacBasedVlanCtrlOptionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1, 3),
    _SwStaticMacBasedVlanCtrlOptionType_Type()
)
swStaticMacBasedVlanCtrlOptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlOptionType.setStatus("current")
_SwStaticMacBasedVlanCtrlOptionStatus_Type = RowStatus
_SwStaticMacBasedVlanCtrlOptionStatus_Object = MibTableColumn
swStaticMacBasedVlanCtrlOptionStatus = _SwStaticMacBasedVlanCtrlOptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1, 4),
    _SwStaticMacBasedVlanCtrlOptionStatus_Type()
)
swStaticMacBasedVlanCtrlOptionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlOptionStatus.setStatus("current")


class _SwStaticMacBasedVlanCtrlOptionPriority_Type(Integer32):
    """Custom type swStaticMacBasedVlanCtrlOptionPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwStaticMacBasedVlanCtrlOptionPriority_Type.__name__ = "Integer32"
_SwStaticMacBasedVlanCtrlOptionPriority_Object = MibTableColumn
swStaticMacBasedVlanCtrlOptionPriority = _SwStaticMacBasedVlanCtrlOptionPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 56, 3, 2, 1, 5),
    _SwStaticMacBasedVlanCtrlOptionPriority_Type()
)
swStaticMacBasedVlanCtrlOptionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swStaticMacBasedVlanCtrlOptionPriority.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STATIC-MAC-BASED-VLAN-MIB",
    **{"swSMBVMIB": swSMBVMIB,
       "swSmbvCtrl": swSmbvCtrl,
       "swSmbvInfo": swSmbvInfo,
       "swSmbvMgmt": swSmbvMgmt,
       "swStaticMacBasedVlanCtrlTable": swStaticMacBasedVlanCtrlTable,
       "swStaticMacBasedVlanCtrlEntry": swStaticMacBasedVlanCtrlEntry,
       "swStaticMacBasedVlanCtrlMacAddr": swStaticMacBasedVlanCtrlMacAddr,
       "swStaticMacBasedVlanCtrlVlanName": swStaticMacBasedVlanCtrlVlanName,
       "swStaticMacBasedVlanCtrlStatus": swStaticMacBasedVlanCtrlStatus,
       "swStaticMacBasedVlanCtrlOptionTable": swStaticMacBasedVlanCtrlOptionTable,
       "swStaticMacBasedVlanCtrlOptionEntry": swStaticMacBasedVlanCtrlOptionEntry,
       "swStaticMacBasedVlanCtrlOptionMacAddr": swStaticMacBasedVlanCtrlOptionMacAddr,
       "swStaticMacBasedOptionVlanID": swStaticMacBasedOptionVlanID,
       "swStaticMacBasedVlanCtrlOptionType": swStaticMacBasedVlanCtrlOptionType,
       "swStaticMacBasedVlanCtrlOptionStatus": swStaticMacBasedVlanCtrlOptionStatus,
       "swStaticMacBasedVlanCtrlOptionPriority": swStaticMacBasedVlanCtrlOptionPriority}
)
