# SNMP MIB module (ZYXEL-CLIENT-PROXY-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-CLIENT-PROXY-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:02:08 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelClientProxyServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelClientProxyServerSetup_ObjectIdentity = ObjectIdentity
zyxelClientProxyServerSetup = _ZyxelClientProxyServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1)
)
_ZyClientProxyServerHttpState_Type = EnabledStatus
_ZyClientProxyServerHttpState_Object = MibScalar
zyClientProxyServerHttpState = _ZyClientProxyServerHttpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 1),
    _ZyClientProxyServerHttpState_Type()
)
zyClientProxyServerHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyClientProxyServerHttpState.setStatus("current")
_ZyClientProxyServerHttpServer_Type = DisplayString
_ZyClientProxyServerHttpServer_Object = MibScalar
zyClientProxyServerHttpServer = _ZyClientProxyServerHttpServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 2),
    _ZyClientProxyServerHttpServer_Type()
)
zyClientProxyServerHttpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyClientProxyServerHttpServer.setStatus("current")
_ZyClientProxyServerHttpPort_Type = Integer32
_ZyClientProxyServerHttpPort_Object = MibScalar
zyClientProxyServerHttpPort = _ZyClientProxyServerHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 3),
    _ZyClientProxyServerHttpPort_Type()
)
zyClientProxyServerHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyClientProxyServerHttpPort.setStatus("current")
_ZyClientProxyServerHttpAuthenticationState_Type = EnabledStatus
_ZyClientProxyServerHttpAuthenticationState_Object = MibScalar
zyClientProxyServerHttpAuthenticationState = _ZyClientProxyServerHttpAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 4),
    _ZyClientProxyServerHttpAuthenticationState_Type()
)
zyClientProxyServerHttpAuthenticationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyClientProxyServerHttpAuthenticationState.setStatus("current")
_ZyClientProxyServerHttpUsername_Type = DisplayString
_ZyClientProxyServerHttpUsername_Object = MibScalar
zyClientProxyServerHttpUsername = _ZyClientProxyServerHttpUsername_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 5),
    _ZyClientProxyServerHttpUsername_Type()
)
zyClientProxyServerHttpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyClientProxyServerHttpUsername.setStatus("current")
_ZyClientProxyServerHttpPassword_Type = DisplayString
_ZyClientProxyServerHttpPassword_Object = MibScalar
zyClientProxyServerHttpPassword = _ZyClientProxyServerHttpPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 121, 1, 6),
    _ZyClientProxyServerHttpPassword_Type()
)
zyClientProxyServerHttpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyClientProxyServerHttpPassword.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-CLIENT-PROXY-SERVER-MIB",
    **{"zyxelClientProxyServer": zyxelClientProxyServer,
       "zyxelClientProxyServerSetup": zyxelClientProxyServerSetup,
       "zyClientProxyServerHttpState": zyClientProxyServerHttpState,
       "zyClientProxyServerHttpServer": zyClientProxyServerHttpServer,
       "zyClientProxyServerHttpPort": zyClientProxyServerHttpPort,
       "zyClientProxyServerHttpAuthenticationState": zyClientProxyServerHttpAuthenticationState,
       "zyClientProxyServerHttpUsername": zyClientProxyServerHttpUsername,
       "zyClientProxyServerHttpPassword": zyClientProxyServerHttpPassword}
)
