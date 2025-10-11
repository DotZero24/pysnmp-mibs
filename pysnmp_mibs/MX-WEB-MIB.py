# SNMP MIB module (MX-WEB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-WEB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:35 2025
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

webMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WebMIBObjects_ObjectIdentity = ObjectIdentity
webMIBObjects = _WebMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1)
)
_ServerGroup_ObjectIdentity = ObjectIdentity
serverGroup = _ServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 100)
)


class _HttpMode_Type(Integer32):
    """Custom type httpMode based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("secure", 100),
          ("unsecure", 200),
          ("both", 300))
    )


_HttpMode_Type.__name__ = "Integer32"
_HttpMode_Object = MibScalar
httpMode = _HttpMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 100, 50),
    _HttpMode_Type()
)
httpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpMode.setStatus("current")


class _ServerPort_Type(MxIpPort):
    """Custom type serverPort based on MxIpPort"""
    defaultValue = 80


_ServerPort_Type.__name__ = "MxIpPort"
_ServerPort_Object = MibScalar
serverPort = _ServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 100, 100),
    _ServerPort_Type()
)
serverPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverPort.setStatus("current")


class _SecureServerPort_Type(MxIpPort):
    """Custom type secureServerPort based on MxIpPort"""
    defaultValue = 443


_SecureServerPort_Type.__name__ = "MxIpPort"
_SecureServerPort_Object = MibScalar
secureServerPort = _SecureServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 100, 200),
    _SecureServerPort_Type()
)
secureServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secureServerPort.setStatus("current")


class _HttpsCipherSuite_Type(Integer32):
    """Custom type httpsCipherSuite based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("cS1", 100),
          ("cS2", 200),
          ("cS3", 300))
    )


_HttpsCipherSuite_Type.__name__ = "Integer32"
_HttpsCipherSuite_Object = MibScalar
httpsCipherSuite = _HttpsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 100, 300),
    _HttpsCipherSuite_Type()
)
httpsCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsCipherSuite.setStatus("current")


class _TlsVersion_Type(Integer32):
    """Custom type tlsVersion based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("sSLv3", 100),
          ("tLSv1", 200),
          ("tLSv1-1", 300),
          ("tLSv1-2", 400))
    )


_TlsVersion_Type.__name__ = "Integer32"
_TlsVersion_Object = MibScalar
tlsVersion = _TlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 100, 400),
    _TlsVersion_Type()
)
tlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsVersion.setStatus("current")
_StatisticsGroup_ObjectIdentity = ObjectIdentity
statisticsGroup = _StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 10000)
)
_StatsRequest_Type = Unsigned32
_StatsRequest_Object = MibScalar
statsRequest = _StatsRequest_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 10000, 100),
    _StatsRequest_Type()
)
statsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsRequest.setStatus("current")
_StatsRedirect_Type = Unsigned32
_StatsRedirect_Object = MibScalar
statsRedirect = _StatsRedirect_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 10000, 200),
    _StatsRedirect_Type()
)
statsRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsRedirect.setStatus("current")
_StatsError_Type = Unsigned32
_StatsError_Object = MibScalar
statsError = _StatsError_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 10000, 300),
    _StatsError_Type()
)
statsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsError.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1200, 1, 60020, 100),
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
    "MX-WEB-MIB",
    **{"webMIB": webMIB,
       "webMIBObjects": webMIBObjects,
       "serverGroup": serverGroup,
       "httpMode": httpMode,
       "serverPort": serverPort,
       "secureServerPort": secureServerPort,
       "httpsCipherSuite": httpsCipherSuite,
       "tlsVersion": tlsVersion,
       "statisticsGroup": statisticsGroup,
       "statsRequest": statsRequest,
       "statsRedirect": statsRedirect,
       "statsError": statsError,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
