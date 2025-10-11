# SNMP MIB module (MX-HTTP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-HTTP-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:20 2025
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

(ipAddressConfig,
 mediatrixConfig) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "mediatrixConfig")

(MxEnableState,
 MxIpAddress,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpAddress",
    "MxIpPort",
    "MxIpSubnetMask")

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

httpServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120)
)
if mibBuilder.loadTexts:
    httpServerMIB.setRevisions(
        ("2009-05-20 00:00",
         "2005-10-07 00:00",
         "2005-04-25 00:00",
         "2004-09-29 00:00",
         "2004-08-31 00:00",
         "2004-02-23 00:00",
         "2004-02-09 00:00",
         "2003-11-13 00:00",
         "2003-11-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressConfigHttpServer_ObjectIdentity = ObjectIdentity
ipAddressConfigHttpServer = _IpAddressConfigHttpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 110)
)


class _HttpServerPort_Type(MxIpPort):
    """Custom type httpServerPort based on MxIpPort"""
    defaultValue = 80


_HttpServerPort_Type.__name__ = "MxIpPort"
_HttpServerPort_Object = MibScalar
httpServerPort = _HttpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 110, 5),
    _HttpServerPort_Type()
)
httpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerPort.setStatus("current")


class _HttpServerAdminPort_Type(MxIpPort):
    """Custom type httpServerAdminPort based on MxIpPort"""
    defaultValue = 8080


_HttpServerAdminPort_Type.__name__ = "MxIpPort"
_HttpServerAdminPort_Object = MibScalar
httpServerAdminPort = _HttpServerAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 110, 10),
    _HttpServerAdminPort_Type()
)
httpServerAdminPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerAdminPort.setStatus("current")
_HttpServerMIBObjects_ObjectIdentity = ObjectIdentity
httpServerMIBObjects = _HttpServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1)
)


class _HttpServerEnable_Type(MxEnableState):
    """Custom type httpServerEnable based on MxEnableState"""
    defaultValue = 1


_HttpServerEnable_Type.__name__ = "MxEnableState"
_HttpServerEnable_Object = MibScalar
httpServerEnable = _HttpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 5),
    _HttpServerEnable_Type()
)
httpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerEnable.setStatus("current")


class _HttpServerAccess_Type(Integer32):
    """Custom type httpServerAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lanOnly", 0),
          ("wanOnly", 1),
          ("all", 2))
    )


_HttpServerAccess_Type.__name__ = "Integer32"
_HttpServerAccess_Object = MibScalar
httpServerAccess = _HttpServerAccess_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 50),
    _HttpServerAccess_Type()
)
httpServerAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerAccess.setStatus("current")


class _HttpServerUsername_Type(OctetString):
    """Custom type httpServerUsername based on OctetString"""
    defaultValue = OctetString("admin")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HttpServerUsername_Type.__name__ = "OctetString"
_HttpServerUsername_Object = MibScalar
httpServerUsername = _HttpServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 100),
    _HttpServerUsername_Type()
)
httpServerUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerUsername.setStatus("current")


class _HttpServerDefaultPassword_Type(OctetString):
    """Custom type httpServerDefaultPassword based on OctetString"""
    defaultValue = OctetString("1234")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HttpServerDefaultPassword_Type.__name__ = "OctetString"
_HttpServerDefaultPassword_Object = MibScalar
httpServerDefaultPassword = _HttpServerDefaultPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 150),
    _HttpServerDefaultPassword_Type()
)
httpServerDefaultPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerDefaultPassword.setStatus("current")


class _HttpServerResetToDefaultPwd_Type(Integer32):
    """Custom type httpServerResetToDefaultPwd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("reset", 1))
    )


_HttpServerResetToDefaultPwd_Type.__name__ = "Integer32"
_HttpServerResetToDefaultPwd_Object = MibScalar
httpServerResetToDefaultPwd = _HttpServerResetToDefaultPwd_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 200),
    _HttpServerResetToDefaultPwd_Type()
)
httpServerResetToDefaultPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerResetToDefaultPwd.setStatus("current")


class _HttpServerAdminAccess_Type(Integer32):
    """Custom type httpServerAdminAccess based on Integer32"""
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
        *(("lanOnly", 0),
          ("wanOnly", 1),
          ("all", 2))
    )


_HttpServerAdminAccess_Type.__name__ = "Integer32"
_HttpServerAdminAccess_Object = MibScalar
httpServerAdminAccess = _HttpServerAdminAccess_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 205),
    _HttpServerAdminAccess_Type()
)
httpServerAdminAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerAdminAccess.setStatus("current")


class _HttpServerAdminUsername_Type(OctetString):
    """Custom type httpServerAdminUsername based on OctetString"""
    defaultValue = OctetString("root")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HttpServerAdminUsername_Type.__name__ = "OctetString"
_HttpServerAdminUsername_Object = MibScalar
httpServerAdminUsername = _HttpServerAdminUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 210),
    _HttpServerAdminUsername_Type()
)
httpServerAdminUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerAdminUsername.setStatus("current")


class _HttpServerDefaultAdminPassword_Type(OctetString):
    """Custom type httpServerDefaultAdminPassword based on OctetString"""
    defaultValue = OctetString("5678")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HttpServerDefaultAdminPassword_Type.__name__ = "OctetString"
_HttpServerDefaultAdminPassword_Object = MibScalar
httpServerDefaultAdminPassword = _HttpServerDefaultAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 215),
    _HttpServerDefaultAdminPassword_Type()
)
httpServerDefaultAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerDefaultAdminPassword.setStatus("current")


class _HttpServerResetToDefaultAdminPwd_Type(Integer32):
    """Custom type httpServerResetToDefaultAdminPwd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("reset", 1))
    )


_HttpServerResetToDefaultAdminPwd_Type.__name__ = "Integer32"
_HttpServerResetToDefaultAdminPwd_Object = MibScalar
httpServerResetToDefaultAdminPwd = _HttpServerResetToDefaultAdminPwd_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 220),
    _HttpServerResetToDefaultAdminPwd_Type()
)
httpServerResetToDefaultAdminPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerResetToDefaultAdminPwd.setStatus("current")


class _HttpServerAdminRealm_Type(OctetString):
    """Custom type httpServerAdminRealm based on OctetString"""
    defaultValue = OctetString("default")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HttpServerAdminRealm_Type.__name__ = "OctetString"
_HttpServerAdminRealm_Object = MibScalar
httpServerAdminRealm = _HttpServerAdminRealm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 225),
    _HttpServerAdminRealm_Type()
)
httpServerAdminRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerAdminRealm.setStatus("current")


class _HttpServerUserRealm_Type(OctetString):
    """Custom type httpServerUserRealm based on OctetString"""
    defaultValue = OctetString("default")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HttpServerUserRealm_Type.__name__ = "OctetString"
_HttpServerUserRealm_Object = MibScalar
httpServerUserRealm = _HttpServerUserRealm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 230),
    _HttpServerUserRealm_Type()
)
httpServerUserRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerUserRealm.setStatus("current")
_HttpServerMIBCustomisation_ObjectIdentity = ObjectIdentity
httpServerMIBCustomisation = _HttpServerMIBCustomisation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 250)
)


class _HttpServerSipAuthenticationEnable_Type(MxEnableState):
    """Custom type httpServerSipAuthenticationEnable based on MxEnableState"""
    defaultValue = 0


_HttpServerSipAuthenticationEnable_Type.__name__ = "MxEnableState"
_HttpServerSipAuthenticationEnable_Object = MibScalar
httpServerSipAuthenticationEnable = _HttpServerSipAuthenticationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 250, 20),
    _HttpServerSipAuthenticationEnable_Type()
)
httpServerSipAuthenticationEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpServerSipAuthenticationEnable.setStatus("current")


class _HttpServerBandwidthControlSectionEnable_Type(MxEnableState):
    """Custom type httpServerBandwidthControlSectionEnable based on MxEnableState"""
    defaultValue = 0


_HttpServerBandwidthControlSectionEnable_Type.__name__ = "MxEnableState"
_HttpServerBandwidthControlSectionEnable_Object = MibScalar
httpServerBandwidthControlSectionEnable = _HttpServerBandwidthControlSectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 1, 250, 30),
    _HttpServerBandwidthControlSectionEnable_Type()
)
httpServerBandwidthControlSectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpServerBandwidthControlSectionEnable.setStatus("current")
_HttpServerConformance_ObjectIdentity = ObjectIdentity
httpServerConformance = _HttpServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 2)
)
_HttpServerCompliances_ObjectIdentity = ObjectIdentity
httpServerCompliances = _HttpServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 2, 1)
)
_HttpServerGroups_ObjectIdentity = ObjectIdentity
httpServerGroups = _HttpServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 2, 5)
)

# Managed Objects groups

httpServerBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 2, 5, 5)
)
httpServerBasicGroupVer1.setObjects(
      *(("MX-HTTP-SERVER-MIB", "httpServerEnable"),
        ("MX-HTTP-SERVER-MIB", "httpServerAccess"),
        ("MX-HTTP-SERVER-MIB", "httpServerUsername"),
        ("MX-HTTP-SERVER-MIB", "httpServerDefaultPassword"),
        ("MX-HTTP-SERVER-MIB", "httpServerResetToDefaultPwd"),
        ("MX-HTTP-SERVER-MIB", "httpServerAdminAccess"),
        ("MX-HTTP-SERVER-MIB", "httpServerAdminUsername"),
        ("MX-HTTP-SERVER-MIB", "httpServerDefaultAdminPassword"),
        ("MX-HTTP-SERVER-MIB", "httpServerResetToDefaultAdminPwd"),
        ("MX-HTTP-SERVER-MIB", "httpServerAdminRealm"),
        ("MX-HTTP-SERVER-MIB", "httpServerUserRealm"))
)
if mibBuilder.loadTexts:
    httpServerBasicGroupVer1.setStatus("current")

httpServerServerGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 2, 5, 10)
)
httpServerServerGroupVer1.setObjects(
    ("MX-HTTP-SERVER-MIB", "httpServerPort")
)
if mibBuilder.loadTexts:
    httpServerServerGroupVer1.setStatus("current")

httpServerCustomisationGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 2, 5, 15)
)
httpServerCustomisationGroupVer1.setObjects(
      *(("MX-HTTP-SERVER-MIB", "httpServerSipAuthenticationEnable"),
        ("MX-HTTP-SERVER-MIB", "httpServerBandwidthControlSectionEnable"))
)
if mibBuilder.loadTexts:
    httpServerCustomisationGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

httpServerComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 120, 2, 1, 1)
)
httpServerComplVer1.setObjects(
      *(("MX-HTTP-SERVER-MIB", "httpServerBasicGroupVer1"),
        ("MX-HTTP-SERVER-MIB", "httpServerServerGroupVer1"),
        ("MX-HTTP-SERVER-MIB", "httpServerCustomisationGroupVer1"))
)
if mibBuilder.loadTexts:
    httpServerComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-HTTP-SERVER-MIB",
    **{"ipAddressConfigHttpServer": ipAddressConfigHttpServer,
       "httpServerPort": httpServerPort,
       "httpServerAdminPort": httpServerAdminPort,
       "httpServerMIB": httpServerMIB,
       "httpServerMIBObjects": httpServerMIBObjects,
       "httpServerEnable": httpServerEnable,
       "httpServerAccess": httpServerAccess,
       "httpServerUsername": httpServerUsername,
       "httpServerDefaultPassword": httpServerDefaultPassword,
       "httpServerResetToDefaultPwd": httpServerResetToDefaultPwd,
       "httpServerAdminAccess": httpServerAdminAccess,
       "httpServerAdminUsername": httpServerAdminUsername,
       "httpServerDefaultAdminPassword": httpServerDefaultAdminPassword,
       "httpServerResetToDefaultAdminPwd": httpServerResetToDefaultAdminPwd,
       "httpServerAdminRealm": httpServerAdminRealm,
       "httpServerUserRealm": httpServerUserRealm,
       "httpServerMIBCustomisation": httpServerMIBCustomisation,
       "httpServerSipAuthenticationEnable": httpServerSipAuthenticationEnable,
       "httpServerBandwidthControlSectionEnable": httpServerBandwidthControlSectionEnable,
       "httpServerConformance": httpServerConformance,
       "httpServerCompliances": httpServerCompliances,
       "httpServerComplVer1": httpServerComplVer1,
       "httpServerGroups": httpServerGroups,
       "httpServerBasicGroupVer1": httpServerBasicGroupVer1,
       "httpServerServerGroupVer1": httpServerServerGroupVer1,
       "httpServerCustomisationGroupVer1": httpServerCustomisationGroupVer1}
)
