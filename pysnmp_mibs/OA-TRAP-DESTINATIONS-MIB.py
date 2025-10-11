# SNMP MIB module (OA-TRAP-DESTINATIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-TRAP-DESTINATIONS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:25 2025
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

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

oaTrapDestinations = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21)
)
if mibBuilder.loadTexts:
    oaTrapDestinations.setRevisions(
        ("2018-06-10 00:00",
         "2012-04-22 00:00",
         "2011-04-12 00:00",
         "2006-12-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbDeviceConfig_ObjectIdentity = ObjectIdentity
nbDeviceConfig = _NbDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11)
)
_NbDevGen_ObjectIdentity = ObjectIdentity
nbDevGen = _NbDevGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1)
)


class _OaTrapDestGenSupport_Type(Integer32):
    """Custom type oaTrapDestGenSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OaTrapDestGenSupport_Type.__name__ = "Integer32"
_OaTrapDestGenSupport_Object = MibScalar
oaTrapDestGenSupport = _OaTrapDestGenSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 1),
    _OaTrapDestGenSupport_Type()
)
oaTrapDestGenSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaTrapDestGenSupport.setStatus("current")
_OaTrapDestTable_Object = MibTable
oaTrapDestTable = _OaTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 2)
)
if mibBuilder.loadTexts:
    oaTrapDestTable.setStatus("current")
_OaTrapDestEntry_Object = MibTableRow
oaTrapDestEntry = _OaTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 2, 1)
)
oaTrapDestEntry.setIndexNames(
    (0, "OA-TRAP-DESTINATIONS-MIB", "oaTrapDestHostAddress"),
)
if mibBuilder.loadTexts:
    oaTrapDestEntry.setStatus("current")


class _OaTrapDestHostAddress_Type(DisplayString):
    """Custom type oaTrapDestHostAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OaTrapDestHostAddress_Type.__name__ = "DisplayString"
_OaTrapDestHostAddress_Object = MibTableColumn
oaTrapDestHostAddress = _OaTrapDestHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 2, 1, 1),
    _OaTrapDestHostAddress_Type()
)
oaTrapDestHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaTrapDestHostAddress.setStatus("current")


class _OaTrapDestVersion_Type(Integer32):
    """Custom type oaTrapDestVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("snmpV1", 1),
          ("snmpV2C", 2),
          ("snmpV3", 3))
    )


_OaTrapDestVersion_Type.__name__ = "Integer32"
_OaTrapDestVersion_Object = MibTableColumn
oaTrapDestVersion = _OaTrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 2, 1, 2),
    _OaTrapDestVersion_Type()
)
oaTrapDestVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaTrapDestVersion.setStatus("current")


class _OaTrapDestAuthentication_Type(DisplayString):
    """Custom type oaTrapDestAuthentication based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OaTrapDestAuthentication_Type.__name__ = "DisplayString"
_OaTrapDestAuthentication_Object = MibTableColumn
oaTrapDestAuthentication = _OaTrapDestAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 2, 1, 3),
    _OaTrapDestAuthentication_Type()
)
oaTrapDestAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaTrapDestAuthentication.setStatus("current")


class _OaTrapDestTrapType_Type(Integer32):
    """Custom type oaTrapDestTrapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("snmpTrap", 1),
          ("snmpInform", 2))
    )


_OaTrapDestTrapType_Type.__name__ = "Integer32"
_OaTrapDestTrapType_Object = MibTableColumn
oaTrapDestTrapType = _OaTrapDestTrapType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 2, 1, 4),
    _OaTrapDestTrapType_Type()
)
oaTrapDestTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaTrapDestTrapType.setStatus("current")


class _OaTrapDestAdminStatus_Type(Integer32):
    """Custom type oaTrapDestAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_OaTrapDestAdminStatus_Type.__name__ = "Integer32"
_OaTrapDestAdminStatus_Object = MibTableColumn
oaTrapDestAdminStatus = _OaTrapDestAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 2, 1, 5),
    _OaTrapDestAdminStatus_Type()
)
oaTrapDestAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaTrapDestAdminStatus.setStatus("current")


class _OaTrapDestEnableMode_Type(Integer32):
    """Custom type oaTrapDestEnableMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_OaTrapDestEnableMode_Type.__name__ = "Integer32"
_OaTrapDestEnableMode_Object = MibScalar
oaTrapDestEnableMode = _OaTrapDestEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 3),
    _OaTrapDestEnableMode_Type()
)
oaTrapDestEnableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaTrapDestEnableMode.setStatus("current")


class _OaTrapDestMaxLimit_Type(Unsigned32):
    """Custom type oaTrapDestMaxLimit based on Unsigned32"""
    defaultValue = 11


_OaTrapDestMaxLimit_Type.__name__ = "Unsigned32"
_OaTrapDestMaxLimit_Object = MibScalar
oaTrapDestMaxLimit = _OaTrapDestMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 4),
    _OaTrapDestMaxLimit_Type()
)
oaTrapDestMaxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaTrapDestMaxLimit.setStatus("current")


class _OaTrapDestInsertLogInfo_Type(Integer32):
    """Custom type oaTrapDestInsertLogInfo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_OaTrapDestInsertLogInfo_Type.__name__ = "Integer32"
_OaTrapDestInsertLogInfo_Object = MibScalar
oaTrapDestInsertLogInfo = _OaTrapDestInsertLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 5),
    _OaTrapDestInsertLogInfo_Type()
)
oaTrapDestInsertLogInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaTrapDestInsertLogInfo.setStatus("current")


class _OaTrapDestInsertHostNameInfo_Type(Integer32):
    """Custom type oaTrapDestInsertHostNameInfo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_OaTrapDestInsertHostNameInfo_Type.__name__ = "Integer32"
_OaTrapDestInsertHostNameInfo_Object = MibScalar
oaTrapDestInsertHostNameInfo = _OaTrapDestInsertHostNameInfo_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 6),
    _OaTrapDestInsertHostNameInfo_Type()
)
oaTrapDestInsertHostNameInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaTrapDestInsertHostNameInfo.setStatus("current")
_OaTrapDestConformance_ObjectIdentity = ObjectIdentity
oaTrapDestConformance = _OaTrapDestConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 101)
)
_OaTrapDestMIBCompliances_ObjectIdentity = ObjectIdentity
oaTrapDestMIBCompliances = _OaTrapDestMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 101, 1)
)
_OaTrapDestMIBGroups_ObjectIdentity = ObjectIdentity
oaTrapDestMIBGroups = _OaTrapDestMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 101, 2)
)

# Managed Objects groups

oaTrapDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 101, 2, 1)
)
oaTrapDestGroup.setObjects(
      *(("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestGenSupport"),
        ("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestVersion"),
        ("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestAuthentication"),
        ("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestTrapType"),
        ("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestAdminStatus"),
        ("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestEnableMode"),
        ("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestMaxLimit"),
        ("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestInsertLogInfo"),
        ("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestInsertHostNameInfo"))
)
if mibBuilder.loadTexts:
    oaTrapDestGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaTrapDestMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 21, 101, 1, 1)
)
oaTrapDestMIBCompliance.setObjects(
    ("OA-TRAP-DESTINATIONS-MIB", "oaTrapDestGroup")
)
if mibBuilder.loadTexts:
    oaTrapDestMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-TRAP-DESTINATIONS-MIB",
    **{"nbDeviceConfig": nbDeviceConfig,
       "nbDevGen": nbDevGen,
       "oaTrapDestinations": oaTrapDestinations,
       "oaTrapDestGenSupport": oaTrapDestGenSupport,
       "oaTrapDestTable": oaTrapDestTable,
       "oaTrapDestEntry": oaTrapDestEntry,
       "oaTrapDestHostAddress": oaTrapDestHostAddress,
       "oaTrapDestVersion": oaTrapDestVersion,
       "oaTrapDestAuthentication": oaTrapDestAuthentication,
       "oaTrapDestTrapType": oaTrapDestTrapType,
       "oaTrapDestAdminStatus": oaTrapDestAdminStatus,
       "oaTrapDestEnableMode": oaTrapDestEnableMode,
       "oaTrapDestMaxLimit": oaTrapDestMaxLimit,
       "oaTrapDestInsertLogInfo": oaTrapDestInsertLogInfo,
       "oaTrapDestInsertHostNameInfo": oaTrapDestInsertHostNameInfo,
       "oaTrapDestConformance": oaTrapDestConformance,
       "oaTrapDestMIBCompliances": oaTrapDestMIBCompliances,
       "oaTrapDestMIBCompliance": oaTrapDestMIBCompliance,
       "oaTrapDestMIBGroups": oaTrapDestMIBGroups,
       "oaTrapDestGroup": oaTrapDestGroup}
)
