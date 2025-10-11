# SNMP MIB module (G6-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-SNMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:12 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65)
)
_DeviceInfoTable_Object = MibTable
deviceInfoTable = _DeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 1)
)
if mibBuilder.loadTexts:
    deviceInfoTable.setStatus("current")
_DeviceInfoEntry_Object = MibTableRow
deviceInfoEntry = _DeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 1, 1)
)
deviceInfoEntry.setIndexNames(
    (0, "G6-SNMP-MIB", "deviceInfoIndex"),
)
if mibBuilder.loadTexts:
    deviceInfoEntry.setStatus("current")


class _DeviceInfoIndex_Type(Integer32):
    """Custom type deviceInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_DeviceInfoIndex_Type.__name__ = "Integer32"
_DeviceInfoIndex_Object = MibTableColumn
deviceInfoIndex = _DeviceInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 1, 1, 1),
    _DeviceInfoIndex_Type()
)
deviceInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceInfoIndex.setStatus("current")
_DeviceInfoSysDescription_Type = DisplayString
_DeviceInfoSysDescription_Object = MibTableColumn
deviceInfoSysDescription = _DeviceInfoSysDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 1, 1, 2),
    _DeviceInfoSysDescription_Type()
)
deviceInfoSysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInfoSysDescription.setStatus("current")
_DeviceInfoSysName_Type = DisplayString
_DeviceInfoSysName_Object = MibTableColumn
deviceInfoSysName = _DeviceInfoSysName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 1, 1, 3),
    _DeviceInfoSysName_Type()
)
deviceInfoSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceInfoSysName.setStatus("current")
_DeviceInfoSysLocation_Type = DisplayString
_DeviceInfoSysLocation_Object = MibTableColumn
deviceInfoSysLocation = _DeviceInfoSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 1, 1, 4),
    _DeviceInfoSysLocation_Type()
)
deviceInfoSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceInfoSysLocation.setStatus("current")
_DeviceInfoSysGroup_Type = DisplayString
_DeviceInfoSysGroup_Object = MibTableColumn
deviceInfoSysGroup = _DeviceInfoSysGroup_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 1, 1, 5),
    _DeviceInfoSysGroup_Type()
)
deviceInfoSysGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceInfoSysGroup.setStatus("current")
_DeviceInfoSysContact_Type = DisplayString
_DeviceInfoSysContact_Object = MibTableColumn
deviceInfoSysContact = _DeviceInfoSysContact_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 1, 1, 6),
    _DeviceInfoSysContact_Type()
)
deviceInfoSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceInfoSysContact.setStatus("current")
_DeviceInfoSysObjectId_Type = DisplayString
_DeviceInfoSysObjectId_Object = MibTableColumn
deviceInfoSysObjectId = _DeviceInfoSysObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 1, 1, 7),
    _DeviceInfoSysObjectId_Type()
)
deviceInfoSysObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceInfoSysObjectId.setStatus("current")
_V1v2ConfigTable_Object = MibTable
v1v2ConfigTable = _V1v2ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 2)
)
if mibBuilder.loadTexts:
    v1v2ConfigTable.setStatus("current")
_V1v2ConfigEntry_Object = MibTableRow
v1v2ConfigEntry = _V1v2ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 2, 1)
)
v1v2ConfigEntry.setIndexNames(
    (0, "G6-SNMP-MIB", "v1v2ConfigIndex"),
)
if mibBuilder.loadTexts:
    v1v2ConfigEntry.setStatus("current")


class _V1v2ConfigIndex_Type(Integer32):
    """Custom type v1v2ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_V1v2ConfigIndex_Type.__name__ = "Integer32"
_V1v2ConfigIndex_Object = MibTableColumn
v1v2ConfigIndex = _V1v2ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 2, 1, 1),
    _V1v2ConfigIndex_Type()
)
v1v2ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v1v2ConfigIndex.setStatus("current")


class _V1v2ConfigEnableSnmpV1_Type(Integer32):
    """Custom type v1v2ConfigEnableSnmpV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_V1v2ConfigEnableSnmpV1_Type.__name__ = "Integer32"
_V1v2ConfigEnableSnmpV1_Object = MibTableColumn
v1v2ConfigEnableSnmpV1 = _V1v2ConfigEnableSnmpV1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 2, 1, 2),
    _V1v2ConfigEnableSnmpV1_Type()
)
v1v2ConfigEnableSnmpV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v1v2ConfigEnableSnmpV1.setStatus("current")


class _V1v2ConfigEnableSnmpV2c_Type(Integer32):
    """Custom type v1v2ConfigEnableSnmpV2c based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_V1v2ConfigEnableSnmpV2c_Type.__name__ = "Integer32"
_V1v2ConfigEnableSnmpV2c_Object = MibTableColumn
v1v2ConfigEnableSnmpV2c = _V1v2ConfigEnableSnmpV2c_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 2, 1, 3),
    _V1v2ConfigEnableSnmpV2c_Type()
)
v1v2ConfigEnableSnmpV2c.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v1v2ConfigEnableSnmpV2c.setStatus("current")
_V1v2ConfigGetCommunity_Type = DisplayString
_V1v2ConfigGetCommunity_Object = MibTableColumn
v1v2ConfigGetCommunity = _V1v2ConfigGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 2, 1, 4),
    _V1v2ConfigGetCommunity_Type()
)
v1v2ConfigGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v1v2ConfigGetCommunity.setStatus("current")
_V1v2ConfigSetCommunity_Type = DisplayString
_V1v2ConfigSetCommunity_Object = MibTableColumn
v1v2ConfigSetCommunity = _V1v2ConfigSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 2, 1, 5),
    _V1v2ConfigSetCommunity_Type()
)
v1v2ConfigSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v1v2ConfigSetCommunity.setStatus("current")
_V1v2ConfigSnmpV1v2Username_Type = DisplayString
_V1v2ConfigSnmpV1v2Username_Object = MibTableColumn
v1v2ConfigSnmpV1v2Username = _V1v2ConfigSnmpV1v2Username_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 2, 1, 6),
    _V1v2ConfigSnmpV1v2Username_Type()
)
v1v2ConfigSnmpV1v2Username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v1v2ConfigSnmpV1v2Username.setStatus("current")


class _V1v2ConfigPermitV1v2SetCommands_Type(Integer32):
    """Custom type v1v2ConfigPermitV1v2SetCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_V1v2ConfigPermitV1v2SetCommands_Type.__name__ = "Integer32"
_V1v2ConfigPermitV1v2SetCommands_Object = MibTableColumn
v1v2ConfigPermitV1v2SetCommands = _V1v2ConfigPermitV1v2SetCommands_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 2, 1, 7),
    _V1v2ConfigPermitV1v2SetCommands_Type()
)
v1v2ConfigPermitV1v2SetCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v1v2ConfigPermitV1v2SetCommands.setStatus("current")
_V3ConfigTable_Object = MibTable
v3ConfigTable = _V3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 3)
)
if mibBuilder.loadTexts:
    v3ConfigTable.setStatus("current")
_V3ConfigEntry_Object = MibTableRow
v3ConfigEntry = _V3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 3, 1)
)
v3ConfigEntry.setIndexNames(
    (0, "G6-SNMP-MIB", "v3ConfigIndex"),
)
if mibBuilder.loadTexts:
    v3ConfigEntry.setStatus("current")


class _V3ConfigIndex_Type(Integer32):
    """Custom type v3ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_V3ConfigIndex_Type.__name__ = "Integer32"
_V3ConfigIndex_Object = MibTableColumn
v3ConfigIndex = _V3ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 3, 1, 1),
    _V3ConfigIndex_Type()
)
v3ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v3ConfigIndex.setStatus("current")


class _V3ConfigEnableSnmpV3_Type(Integer32):
    """Custom type v3ConfigEnableSnmpV3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_V3ConfigEnableSnmpV3_Type.__name__ = "Integer32"
_V3ConfigEnableSnmpV3_Object = MibTableColumn
v3ConfigEnableSnmpV3 = _V3ConfigEnableSnmpV3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 3, 1, 2),
    _V3ConfigEnableSnmpV3_Type()
)
v3ConfigEnableSnmpV3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3ConfigEnableSnmpV3.setStatus("current")


class _V3ConfigSecurityModel_Type(Integer32):
    """Custom type v3ConfigSecurityModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("usm", 0),
          ("vacm", 1))
    )


_V3ConfigSecurityModel_Type.__name__ = "Integer32"
_V3ConfigSecurityModel_Object = MibTableColumn
v3ConfigSecurityModel = _V3ConfigSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 3, 1, 3),
    _V3ConfigSecurityModel_Type()
)
v3ConfigSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3ConfigSecurityModel.setStatus("current")
_V3ConfigSnmpEngineId_Type = DisplayString
_V3ConfigSnmpEngineId_Object = MibTableColumn
v3ConfigSnmpEngineId = _V3ConfigSnmpEngineId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 3, 1, 4),
    _V3ConfigSnmpEngineId_Type()
)
v3ConfigSnmpEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3ConfigSnmpEngineId.setStatus("current")
_V3ConfigTrapEngineId_Type = DisplayString
_V3ConfigTrapEngineId_Object = MibTableColumn
v3ConfigTrapEngineId = _V3ConfigTrapEngineId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 3, 1, 5),
    _V3ConfigTrapEngineId_Type()
)
v3ConfigTrapEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v3ConfigTrapEngineId.setStatus("current")
_BrowserTable_Object = MibTable
browserTable = _BrowserTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 4)
)
if mibBuilder.loadTexts:
    browserTable.setStatus("current")
_BrowserEntry_Object = MibTableRow
browserEntry = _BrowserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 4, 1)
)
browserEntry.setIndexNames(
    (0, "G6-SNMP-MIB", "browserIndex"),
)
if mibBuilder.loadTexts:
    browserEntry.setStatus("current")


class _BrowserIndex_Type(Integer32):
    """Custom type browserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_BrowserIndex_Type.__name__ = "Integer32"
_BrowserIndex_Object = MibTableColumn
browserIndex = _BrowserIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 4, 1, 1),
    _BrowserIndex_Type()
)
browserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    browserIndex.setStatus("current")
_BrowserGet_Type = DisplayString
_BrowserGet_Object = MibTableColumn
browserGet = _BrowserGet_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 4, 1, 2),
    _BrowserGet_Type()
)
browserGet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    browserGet.setStatus("current")
_BrowserNext_Type = DisplayString
_BrowserNext_Object = MibTableColumn
browserNext = _BrowserNext_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 4, 1, 3),
    _BrowserNext_Type()
)
browserNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    browserNext.setStatus("current")
_BrowserSet_Type = DisplayString
_BrowserSet_Object = MibTableColumn
browserSet = _BrowserSet_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 4, 1, 4),
    _BrowserSet_Type()
)
browserSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    browserSet.setStatus("current")
_BrowserWalk_Type = DisplayString
_BrowserWalk_Object = MibTableColumn
browserWalk = _BrowserWalk_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 4, 1, 5),
    _BrowserWalk_Type()
)
browserWalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    browserWalk.setStatus("current")
_SnmpEngineBoots_Type = Unsigned32
_SnmpEngineBoots_Object = MibScalar
snmpEngineBoots = _SnmpEngineBoots_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 100),
    _SnmpEngineBoots_Type()
)
snmpEngineBoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineBoots.setStatus("current")
_SnmpEngineRuntime_Type = Unsigned32
_SnmpEngineRuntime_Object = MibScalar
snmpEngineRuntime = _SnmpEngineRuntime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 65, 101),
    _SnmpEngineRuntime_Type()
)
snmpEngineRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineRuntime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-SNMP-MIB",
    **{"management": management,
       "snmp": snmp,
       "deviceInfoTable": deviceInfoTable,
       "deviceInfoEntry": deviceInfoEntry,
       "deviceInfoIndex": deviceInfoIndex,
       "deviceInfoSysDescription": deviceInfoSysDescription,
       "deviceInfoSysName": deviceInfoSysName,
       "deviceInfoSysLocation": deviceInfoSysLocation,
       "deviceInfoSysGroup": deviceInfoSysGroup,
       "deviceInfoSysContact": deviceInfoSysContact,
       "deviceInfoSysObjectId": deviceInfoSysObjectId,
       "v1v2ConfigTable": v1v2ConfigTable,
       "v1v2ConfigEntry": v1v2ConfigEntry,
       "v1v2ConfigIndex": v1v2ConfigIndex,
       "v1v2ConfigEnableSnmpV1": v1v2ConfigEnableSnmpV1,
       "v1v2ConfigEnableSnmpV2c": v1v2ConfigEnableSnmpV2c,
       "v1v2ConfigGetCommunity": v1v2ConfigGetCommunity,
       "v1v2ConfigSetCommunity": v1v2ConfigSetCommunity,
       "v1v2ConfigSnmpV1v2Username": v1v2ConfigSnmpV1v2Username,
       "v1v2ConfigPermitV1v2SetCommands": v1v2ConfigPermitV1v2SetCommands,
       "v3ConfigTable": v3ConfigTable,
       "v3ConfigEntry": v3ConfigEntry,
       "v3ConfigIndex": v3ConfigIndex,
       "v3ConfigEnableSnmpV3": v3ConfigEnableSnmpV3,
       "v3ConfigSecurityModel": v3ConfigSecurityModel,
       "v3ConfigSnmpEngineId": v3ConfigSnmpEngineId,
       "v3ConfigTrapEngineId": v3ConfigTrapEngineId,
       "browserTable": browserTable,
       "browserEntry": browserEntry,
       "browserIndex": browserIndex,
       "browserGet": browserGet,
       "browserNext": browserNext,
       "browserSet": browserSet,
       "browserWalk": browserWalk,
       "snmpEngineBoots": snmpEngineBoots,
       "snmpEngineRuntime": snmpEngineRuntime}
)
