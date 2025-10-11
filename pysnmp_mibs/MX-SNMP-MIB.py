# SNMP MIB module (MX-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SNMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:45 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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

snmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpMIBObjects_ObjectIdentity = ObjectIdentity
snmpMIBObjects = _SnmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1)
)
_ProtocolGroup_ObjectIdentity = ObjectIdentity
protocolGroup = _ProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 200)
)


class _EnableSnmpV1_Type(MxEnableState):
    """Custom type enableSnmpV1 based on MxEnableState"""
    defaultValue = 0


_EnableSnmpV1_Type.__name__ = "MxEnableState"
_EnableSnmpV1_Object = MibScalar
enableSnmpV1 = _EnableSnmpV1_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 200, 200),
    _EnableSnmpV1_Type()
)
enableSnmpV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSnmpV1.setStatus("current")


class _EnableSnmpV2_Type(MxEnableState):
    """Custom type enableSnmpV2 based on MxEnableState"""
    defaultValue = 0


_EnableSnmpV2_Type.__name__ = "MxEnableState"
_EnableSnmpV2_Object = MibScalar
enableSnmpV2 = _EnableSnmpV2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 200, 300),
    _EnableSnmpV2_Type()
)
enableSnmpV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSnmpV2.setStatus("current")


class _EnableSnmpV3_Type(MxEnableState):
    """Custom type enableSnmpV3 based on MxEnableState"""
    defaultValue = 1


_EnableSnmpV3_Type.__name__ = "MxEnableState"
_EnableSnmpV3_Object = MibScalar
enableSnmpV3 = _EnableSnmpV3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 200, 400),
    _EnableSnmpV3_Type()
)
enableSnmpV3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSnmpV3.setStatus("current")


class _AuthProtocol_Type(Integer32):
    """Custom type authProtocol based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("md5", 100),
          ("sha1", 200))
    )


_AuthProtocol_Type.__name__ = "Integer32"
_AuthProtocol_Object = MibScalar
authProtocol = _AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 200, 500),
    _AuthProtocol_Type()
)
authProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authProtocol.setStatus("current")


class _PrivProtocol_Type(Integer32):
    """Custom type privProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des", 100))
    )


_PrivProtocol_Type.__name__ = "Integer32"
_PrivProtocol_Object = MibScalar
privProtocol = _PrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 200, 600),
    _PrivProtocol_Type()
)
privProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privProtocol.setStatus("current")


class _PrivPassword_Type(OctetString):
    """Custom type privPassword based on OctetString"""
    defaultValue = OctetString("PrivPassword")


_PrivPassword_Type.__name__ = "OctetString"
_PrivPassword_Object = MibScalar
privPassword = _PrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 200, 700),
    _PrivPassword_Type()
)
privPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privPassword.setStatus("current")


class _Community_Type(OctetString):
    """Custom type community based on OctetString"""
    defaultValue = OctetString("public")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Community_Type.__name__ = "OctetString"
_Community_Object = MibScalar
community = _Community_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 200, 800),
    _Community_Type()
)
community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    community.setStatus("current")


class _SnmpUser_Type(OctetString):
    """Custom type snmpUser based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SnmpUser_Type.__name__ = "OctetString"
_SnmpUser_Object = MibScalar
snmpUser = _SnmpUser_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 200, 900),
    _SnmpUser_Type()
)
snmpUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUser.setStatus("current")
_StandardTrapsGroup_ObjectIdentity = ObjectIdentity
standardTrapsGroup = _StandardTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 300)
)


class _TrapDest_Type(OctetString):
    """Custom type trapDest based on OctetString"""
    defaultValue = OctetString("192.168.10.10:162")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDest_Type.__name__ = "OctetString"
_TrapDest_Object = MibScalar
trapDest = _TrapDest_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 300, 100),
    _TrapDest_Type()
)
trapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDest.setStatus("current")


class _EnableTrap_Type(MxEnableState):
    """Custom type enableTrap based on MxEnableState"""
    defaultValue = 1


_EnableTrap_Type.__name__ = "MxEnableState"
_EnableTrap_Object = MibScalar
enableTrap = _EnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 300, 200),
    _EnableTrap_Type()
)
enableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTrap.setStatus("current")


class _Port_Type(MxIpPort):
    """Custom type port based on MxIpPort"""
    defaultValue = 161


_Port_Type.__name__ = "MxIpPort"
_Port_Object = MibScalar
port = _Port_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 400),
    _Port_Type()
)
port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port.setStatus("current")
_StatisticsGroup_ObjectIdentity = ObjectIdentity
statisticsGroup = _StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 10000)
)
_StatsGetRequest_Type = Unsigned32
_StatsGetRequest_Object = MibScalar
statsGetRequest = _StatsGetRequest_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 10000, 100),
    _StatsGetRequest_Type()
)
statsGetRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsGetRequest.setStatus("current")
_StatsGetNextRequest_Type = Unsigned32
_StatsGetNextRequest_Object = MibScalar
statsGetNextRequest = _StatsGetNextRequest_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 10000, 200),
    _StatsGetNextRequest_Type()
)
statsGetNextRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsGetNextRequest.setStatus("current")
_StatsSetRequest_Type = Unsigned32
_StatsSetRequest_Object = MibScalar
statsSetRequest = _StatsSetRequest_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 10000, 300),
    _StatsSetRequest_Type()
)
statsSetRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsSetRequest.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SNMP-MIB",
    **{"snmpMIB": snmpMIB,
       "snmpMIBObjects": snmpMIBObjects,
       "protocolGroup": protocolGroup,
       "enableSnmpV1": enableSnmpV1,
       "enableSnmpV2": enableSnmpV2,
       "enableSnmpV3": enableSnmpV3,
       "authProtocol": authProtocol,
       "privProtocol": privProtocol,
       "privPassword": privPassword,
       "community": community,
       "snmpUser": snmpUser,
       "standardTrapsGroup": standardTrapsGroup,
       "trapDest": trapDest,
       "enableTrap": enableTrap,
       "port": port,
       "statisticsGroup": statisticsGroup,
       "statsGetRequest": statsGetRequest,
       "statsGetNextRequest": statsGetNextRequest,
       "statsSetRequest": statsSetRequest,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
