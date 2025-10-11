# SNMP MIB module (IPI-VRF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/IPI-VRF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:05 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ipiVrfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35)
)
if mibBuilder.loadTexts:
    ipiVrfMIB.setRevisions(
        ("2014-05-16 12:25",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaOptiSwitch_ObjectIdentity = ObjectIdentity
oaOptiSwitch = _OaOptiSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2)
)
_IpiVrfMIBNotifs_ObjectIdentity = ObjectIdentity
ipiVrfMIBNotifs = _IpiVrfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 0)
)
_IpiVrfMIBObjects_ObjectIdentity = ObjectIdentity
ipiVrfMIBObjects = _IpiVrfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1)
)
_IpiVrf_ObjectIdentity = ObjectIdentity
ipiVrf = _IpiVrf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 1)
)
_IpiVrfTable_Object = MibTable
ipiVrfTable = _IpiVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipiVrfTable.setStatus("current")
_IpiVrfEntry_Object = MibTableRow
ipiVrfEntry = _IpiVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 1, 1, 1)
)
ipiVrfEntry.setIndexNames(
    (0, "IPI-VRF-MIB", "ipiVrfIndex"),
)
if mibBuilder.loadTexts:
    ipiVrfEntry.setStatus("current")


class _IpiVrfIndex_Type(Unsigned32):
    """Custom type ipiVrfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpiVrfIndex_Type.__name__ = "Unsigned32"
_IpiVrfIndex_Object = MibTableColumn
ipiVrfIndex = _IpiVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 1, 1, 1, 1),
    _IpiVrfIndex_Type()
)
ipiVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiVrfIndex.setStatus("current")


class _IpiVrfName_Type(SnmpAdminString):
    """Custom type ipiVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IpiVrfName_Type.__name__ = "SnmpAdminString"
_IpiVrfName_Object = MibTableColumn
ipiVrfName = _IpiVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 1, 1, 1, 2),
    _IpiVrfName_Type()
)
ipiVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiVrfName.setStatus("current")


class _IpiVrfOperStatus_Type(Integer32):
    """Custom type ipiVrfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_IpiVrfOperStatus_Type.__name__ = "Integer32"
_IpiVrfOperStatus_Object = MibTableColumn
ipiVrfOperStatus = _IpiVrfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 1, 1, 1, 3),
    _IpiVrfOperStatus_Type()
)
ipiVrfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiVrfOperStatus.setStatus("current")


class _IpiVrfRouteDistProt_Type(Bits):
    """Custom type ipiVrfRouteDistProt based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("other", 1),
          ("static", 2),
          ("ospf", 3),
          ("bgp", 4),
          ("pim", 5),
          ("igmp", 6))
    )

_IpiVrfRouteDistProt_Type.__name__ = "Bits"
_IpiVrfRouteDistProt_Object = MibTableColumn
ipiVrfRouteDistProt = _IpiVrfRouteDistProt_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 1, 1, 1, 4),
    _IpiVrfRouteDistProt_Type()
)
ipiVrfRouteDistProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiVrfRouteDistProt.setStatus("current")
_IpiVrfStorageType_Type = StorageType
_IpiVrfStorageType_Object = MibTableColumn
ipiVrfStorageType = _IpiVrfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 1, 1, 1, 5),
    _IpiVrfStorageType_Type()
)
ipiVrfStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiVrfStorageType.setStatus("current")
_IpiVrfRowStatus_Type = RowStatus
_IpiVrfRowStatus_Object = MibTableColumn
ipiVrfRowStatus = _IpiVrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 1, 1, 1, 6),
    _IpiVrfRowStatus_Type()
)
ipiVrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiVrfRowStatus.setStatus("current")
_IpiInterface_ObjectIdentity = ObjectIdentity
ipiInterface = _IpiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 2)
)
_IpiVrfInterfaceTable_Object = MibTable
ipiVrfInterfaceTable = _IpiVrfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipiVrfInterfaceTable.setStatus("current")
_IpiVrfInterfaceEntry_Object = MibTableRow
ipiVrfInterfaceEntry = _IpiVrfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 2, 1, 1)
)
ipiVrfInterfaceEntry.setIndexNames(
    (0, "IPI-VRF-MIB", "ipiVrfInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ipiVrfInterfaceEntry.setStatus("current")


class _IpiVrfInterfaceIndex_Type(InterfaceIndex):
    """Custom type ipiVrfInterfaceIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpiVrfInterfaceIndex_Type.__name__ = "InterfaceIndex"
_IpiVrfInterfaceIndex_Object = MibTableColumn
ipiVrfInterfaceIndex = _IpiVrfInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 2, 1, 1, 1),
    _IpiVrfInterfaceIndex_Type()
)
ipiVrfInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiVrfInterfaceIndex.setStatus("current")


class _IpiVrfInterfaceName_Type(SnmpAdminString):
    """Custom type ipiVrfInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IpiVrfInterfaceName_Type.__name__ = "SnmpAdminString"
_IpiVrfInterfaceName_Object = MibTableColumn
ipiVrfInterfaceName = _IpiVrfInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 2, 1, 1, 2),
    _IpiVrfInterfaceName_Type()
)
ipiVrfInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiVrfInterfaceName.setStatus("current")
_IpiVrfInterfaceStorageType_Type = StorageType
_IpiVrfInterfaceStorageType_Object = MibTableColumn
ipiVrfInterfaceStorageType = _IpiVrfInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 2, 1, 1, 3),
    _IpiVrfInterfaceStorageType_Type()
)
ipiVrfInterfaceStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiVrfInterfaceStorageType.setStatus("current")
_IpiVrfInterfaceRowStatus_Type = RowStatus
_IpiVrfInterfaceRowStatus_Object = MibTableColumn
ipiVrfInterfaceRowStatus = _IpiVrfInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 1, 2, 1, 1, 4),
    _IpiVrfInterfaceRowStatus_Type()
)
ipiVrfInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiVrfInterfaceRowStatus.setStatus("current")
_IpiVrfMIBConform_ObjectIdentity = ObjectIdentity
ipiVrfMIBConform = _IpiVrfMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 2)
)
_IpiMIBGroups_ObjectIdentity = ObjectIdentity
ipiMIBGroups = _IpiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 2, 1)
)
_IpiMIBCompliances_ObjectIdentity = ObjectIdentity
ipiMIBCompliances = _IpiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 2, 2)
)

# Managed Objects groups

ipiMIBVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 2, 1, 1)
)
ipiMIBVrfGroup.setObjects(
      *(("IPI-VRF-MIB", "ipiVrfOperStatus"),
        ("IPI-VRF-MIB", "ipiVrfStorageType"),
        ("IPI-VRF-MIB", "ipiVrfRowStatus"),
        ("IPI-VRF-MIB", "ipiVrfRouteDistProt"),
        ("IPI-VRF-MIB", "ipiVrfInterfaceIndex"),
        ("IPI-VRF-MIB", "ipiVrfInterfaceName"),
        ("IPI-VRF-MIB", "ipiVrfInterfaceStorageType"),
        ("IPI-VRF-MIB", "ipiVrfInterfaceRowStatus"),
        ("IPI-VRF-MIB", "ipiVrfName"))
)
if mibBuilder.loadTexts:
    ipiMIBVrfGroup.setStatus("current")


# Notification objects

ipiVrfIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 0, 1)
)
ipiVrfIfUp.setObjects(
      *(("IPI-VRF-MIB", "ipiVrfInterfaceIndex"),
        ("IPI-VRF-MIB", "ipiVrfName"),
        ("IPI-VRF-MIB", "ipiVrfOperStatus"))
)
if mibBuilder.loadTexts:
    ipiVrfIfUp.setStatus(
        "current"
    )

ipiVrfIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 0, 2)
)
ipiVrfIfDown.setObjects(
      *(("IPI-VRF-MIB", "ipiVrfInterfaceIndex"),
        ("IPI-VRF-MIB", "ipiVrfName"),
        ("IPI-VRF-MIB", "ipiVrfOperStatus"))
)
if mibBuilder.loadTexts:
    ipiVrfIfDown.setStatus(
        "current"
    )


# Notifications groups

ipiMIBVrfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 2, 1, 2)
)
ipiMIBVrfNotifGroup.setObjects(
      *(("IPI-VRF-MIB", "ipiVrfIfUp"),
        ("IPI-VRF-MIB", "ipiVrfIfDown"))
)
if mibBuilder.loadTexts:
    ipiMIBVrfNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ipiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 35, 2, 2, 1)
)
ipiMIBCompliance.setObjects(
      *(("IPI-VRF-MIB", "ipiMIBVrfGroup"),
        ("IPI-VRF-MIB", "ipiMIBVrfNotifGroup"))
)
if mibBuilder.loadTexts:
    ipiMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPI-VRF-MIB",
    **{"oaccess": oaccess,
       "oaOptiSwitch": oaOptiSwitch,
       "ipiVrfMIB": ipiVrfMIB,
       "ipiVrfMIBNotifs": ipiVrfMIBNotifs,
       "ipiVrfIfUp": ipiVrfIfUp,
       "ipiVrfIfDown": ipiVrfIfDown,
       "ipiVrfMIBObjects": ipiVrfMIBObjects,
       "ipiVrf": ipiVrf,
       "ipiVrfTable": ipiVrfTable,
       "ipiVrfEntry": ipiVrfEntry,
       "ipiVrfIndex": ipiVrfIndex,
       "ipiVrfName": ipiVrfName,
       "ipiVrfOperStatus": ipiVrfOperStatus,
       "ipiVrfRouteDistProt": ipiVrfRouteDistProt,
       "ipiVrfStorageType": ipiVrfStorageType,
       "ipiVrfRowStatus": ipiVrfRowStatus,
       "ipiInterface": ipiInterface,
       "ipiVrfInterfaceTable": ipiVrfInterfaceTable,
       "ipiVrfInterfaceEntry": ipiVrfInterfaceEntry,
       "ipiVrfInterfaceIndex": ipiVrfInterfaceIndex,
       "ipiVrfInterfaceName": ipiVrfInterfaceName,
       "ipiVrfInterfaceStorageType": ipiVrfInterfaceStorageType,
       "ipiVrfInterfaceRowStatus": ipiVrfInterfaceRowStatus,
       "ipiVrfMIBConform": ipiVrfMIBConform,
       "ipiMIBGroups": ipiMIBGroups,
       "ipiMIBVrfGroup": ipiMIBVrfGroup,
       "ipiMIBVrfNotifGroup": ipiMIBVrfNotifGroup,
       "ipiMIBCompliances": ipiMIBCompliances,
       "ipiMIBCompliance": ipiMIBCompliance}
)
