# SNMP MIB module (RUCKUS-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/RUCKUS-AUTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:02:43 2025
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

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44)
)
if mibBuilder.loadTexts:
    ruckusAuthMIB.setRevisions(
        ("2020-04-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



class Dot1xAuthState(TextualConvention, Integer32):
    status = "current"
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("initialize", 2),
          ("disconnected", 3),
          ("connecting", 4),
          ("authenticating", 5),
          ("authenticated", 6),
          ("aborting", 7),
          ("held", 8),
          ("forceAuth", 9),
          ("forceUnauth", 10))
    )



class RuckusAuthMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("singleUntagged", 1),
          ("multipleUntagged", 2),
          ("singleHost", 3),
          ("multipleHosts", 4))
    )



class RuckusAuthOrder(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1xMauth", 1),
          ("mauthDot1x", 2))
    )



class RuckusAuthFailAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blockTraffic", 1),
          ("restrictVlan", 2))
    )



class RuckusAuthTimeoutAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 2),
          ("criticalVlan", 3),
          ("other", 4))
    )



class RuckusAuthAging(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("deniedSessions", 0),
          ("permittedSessions", 1))
    )


# MIB Managed Objects in the order of their OIDs

_RuckusAuthNotification_ObjectIdentity = ObjectIdentity
ruckusAuthNotification = _RuckusAuthNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 0)
)
_RuckusAuthObjects_ObjectIdentity = ObjectIdentity
ruckusAuthObjects = _RuckusAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1)
)
_RuckusAuthConfig_ObjectIdentity = ObjectIdentity
ruckusAuthConfig = _RuckusAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1)
)
_RuckusAuthDefaultVlan_Type = VlanId
_RuckusAuthDefaultVlan_Object = MibScalar
ruckusAuthDefaultVlan = _RuckusAuthDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 1),
    _RuckusAuthDefaultVlan_Type()
)
ruckusAuthDefaultVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthDefaultVlan.setStatus("current")
_RuckusAuthVoiceVlan_Type = VlanId
_RuckusAuthVoiceVlan_Object = MibScalar
ruckusAuthVoiceVlan = _RuckusAuthVoiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 2),
    _RuckusAuthVoiceVlan_Type()
)
ruckusAuthVoiceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthVoiceVlan.setStatus("current")
_RuckusAuthCriticalVlan_Type = VlanId
_RuckusAuthCriticalVlan_Object = MibScalar
ruckusAuthCriticalVlan = _RuckusAuthCriticalVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 3),
    _RuckusAuthCriticalVlan_Type()
)
ruckusAuthCriticalVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthCriticalVlan.setStatus("current")
_RuckusAuthRestrictVlan_Type = VlanId
_RuckusAuthRestrictVlan_Object = MibScalar
ruckusAuthRestrictVlan = _RuckusAuthRestrictVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 4),
    _RuckusAuthRestrictVlan_Type()
)
ruckusAuthRestrictVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthRestrictVlan.setStatus("current")


class _RuckusAuthEnable_Type(Bits):
    """Custom type ruckusAuthEnable based on Bits"""
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("macAuth", 1))
    )

_RuckusAuthEnable_Type.__name__ = "Bits"
_RuckusAuthEnable_Object = MibScalar
ruckusAuthEnable = _RuckusAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 5),
    _RuckusAuthEnable_Type()
)
ruckusAuthEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthEnable.setStatus("current")


class _RuckusAuthMode_Type(RuckusAuthMode):
    """Custom type ruckusAuthMode based on RuckusAuthMode"""
    defaultValue = 1


_RuckusAuthMode_Type.__name__ = "RuckusAuthMode"
_RuckusAuthMode_Object = MibScalar
ruckusAuthMode = _RuckusAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 6),
    _RuckusAuthMode_Type()
)
ruckusAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthMode.setStatus("current")


class _RuckusAuthMethods_Type(RuckusAuthOrder):
    """Custom type ruckusAuthMethods based on RuckusAuthOrder"""
    defaultValue = 1


_RuckusAuthMethods_Type.__name__ = "RuckusAuthOrder"
_RuckusAuthMethods_Object = MibScalar
ruckusAuthMethods = _RuckusAuthMethods_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 7),
    _RuckusAuthMethods_Type()
)
ruckusAuthMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthMethods.setStatus("current")


class _RuckusAuthMaxSessions_Type(Unsigned32):
    """Custom type ruckusAuthMaxSessions based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuckusAuthMaxSessions_Type.__name__ = "Unsigned32"
_RuckusAuthMaxSessions_Object = MibScalar
ruckusAuthMaxSessions = _RuckusAuthMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 8),
    _RuckusAuthMaxSessions_Type()
)
ruckusAuthMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthMaxSessions.setStatus("current")


class _RuckusAuthFailAction_Type(RuckusAuthFailAction):
    """Custom type ruckusAuthFailAction based on RuckusAuthFailAction"""
    defaultValue = 1


_RuckusAuthFailAction_Type.__name__ = "RuckusAuthFailAction"
_RuckusAuthFailAction_Object = MibScalar
ruckusAuthFailAction = _RuckusAuthFailAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 9),
    _RuckusAuthFailAction_Type()
)
ruckusAuthFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthFailAction.setStatus("current")


class _RuckusAuthTimeoutAction_Type(RuckusAuthTimeoutAction):
    """Custom type ruckusAuthTimeoutAction based on RuckusAuthTimeoutAction"""
    defaultValue = 4


_RuckusAuthTimeoutAction_Type.__name__ = "RuckusAuthTimeoutAction"
_RuckusAuthTimeoutAction_Object = MibScalar
ruckusAuthTimeoutAction = _RuckusAuthTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 10),
    _RuckusAuthTimeoutAction_Type()
)
ruckusAuthTimeoutAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthTimeoutAction.setStatus("current")


class _RuckusAuthReauthEnable_Type(EnabledStatus):
    """Custom type ruckusAuthReauthEnable based on EnabledStatus"""
    defaultValue = 2


_RuckusAuthReauthEnable_Type.__name__ = "EnabledStatus"
_RuckusAuthReauthEnable_Object = MibScalar
ruckusAuthReauthEnable = _RuckusAuthReauthEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 11),
    _RuckusAuthReauthEnable_Type()
)
ruckusAuthReauthEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthReauthEnable.setStatus("current")


class _RuckusAuthReauthPeriod_Type(Unsigned32):
    """Custom type ruckusAuthReauthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuckusAuthReauthPeriod_Type.__name__ = "Unsigned32"
_RuckusAuthReauthPeriod_Object = MibScalar
ruckusAuthReauthPeriod = _RuckusAuthReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 12),
    _RuckusAuthReauthPeriod_Type()
)
ruckusAuthReauthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthReauthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAuthReauthPeriod.setUnits("seconds")


class _RuckusAuthReauthTimeout_Type(Unsigned32):
    """Custom type ruckusAuthReauthTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuckusAuthReauthTimeout_Type.__name__ = "Unsigned32"
_RuckusAuthReauthTimeout_Object = MibScalar
ruckusAuthReauthTimeout = _RuckusAuthReauthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 13),
    _RuckusAuthReauthTimeout_Type()
)
ruckusAuthReauthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthReauthTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAuthReauthTimeout.setUnits("seconds")


class _RuckusAuthIdleTimeout_Type(Unsigned32):
    """Custom type ruckusAuthIdleTimeout based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuckusAuthIdleTimeout_Type.__name__ = "Unsigned32"
_RuckusAuthIdleTimeout_Object = MibScalar
ruckusAuthIdleTimeout = _RuckusAuthIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 14),
    _RuckusAuthIdleTimeout_Type()
)
ruckusAuthIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAuthIdleTimeout.setUnits("seconds")


class _RuckusAuthDeniedTimeout_Type(Unsigned32):
    """Custom type ruckusAuthDeniedTimeout based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuckusAuthDeniedTimeout_Type.__name__ = "Unsigned32"
_RuckusAuthDeniedTimeout_Object = MibScalar
ruckusAuthDeniedTimeout = _RuckusAuthDeniedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 15),
    _RuckusAuthDeniedTimeout_Type()
)
ruckusAuthDeniedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthDeniedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAuthDeniedTimeout.setUnits("seconds")
_RuckusAuthAging_Type = RuckusAuthAging
_RuckusAuthAging_Object = MibScalar
ruckusAuthAging = _RuckusAuthAging_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 16),
    _RuckusAuthAging_Type()
)
ruckusAuthAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthAging.setStatus("current")
_RuckusAuthDefaultV4IngressAcl_Type = DisplayString
_RuckusAuthDefaultV4IngressAcl_Object = MibScalar
ruckusAuthDefaultV4IngressAcl = _RuckusAuthDefaultV4IngressAcl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 17),
    _RuckusAuthDefaultV4IngressAcl_Type()
)
ruckusAuthDefaultV4IngressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthDefaultV4IngressAcl.setStatus("current")
_RuckusAuthDefaultV4EgressAcl_Type = DisplayString
_RuckusAuthDefaultV4EgressAcl_Object = MibScalar
ruckusAuthDefaultV4EgressAcl = _RuckusAuthDefaultV4EgressAcl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 18),
    _RuckusAuthDefaultV4EgressAcl_Type()
)
ruckusAuthDefaultV4EgressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthDefaultV4EgressAcl.setStatus("current")
_RuckusAuthDefaultV6IngressAcl_Type = DisplayString
_RuckusAuthDefaultV6IngressAcl_Object = MibScalar
ruckusAuthDefaultV6IngressAcl = _RuckusAuthDefaultV6IngressAcl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 19),
    _RuckusAuthDefaultV6IngressAcl_Type()
)
ruckusAuthDefaultV6IngressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthDefaultV6IngressAcl.setStatus("current")
_RuckusAuthDefaultV6EgressAcl_Type = DisplayString
_RuckusAuthDefaultV6EgressAcl_Object = MibScalar
ruckusAuthDefaultV6EgressAcl = _RuckusAuthDefaultV6EgressAcl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 1, 20),
    _RuckusAuthDefaultV6EgressAcl_Type()
)
ruckusAuthDefaultV6EgressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthDefaultV6EgressAcl.setStatus("current")
_RuckusDot1xAuthConfig_ObjectIdentity = ObjectIdentity
ruckusDot1xAuthConfig = _RuckusDot1xAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 2)
)


class _RuckusDot1xQuietPeriod_Type(Unsigned32):
    """Custom type ruckusDot1xQuietPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RuckusDot1xQuietPeriod_Type.__name__ = "Unsigned32"
_RuckusDot1xQuietPeriod_Object = MibScalar
ruckusDot1xQuietPeriod = _RuckusDot1xQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 2, 1),
    _RuckusDot1xQuietPeriod_Type()
)
ruckusDot1xQuietPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xQuietPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ruckusDot1xQuietPeriod.setUnits("seconds")


class _RuckusDot1xTxPeriod_Type(Unsigned32):
    """Custom type ruckusDot1xTxPeriod based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuckusDot1xTxPeriod_Type.__name__ = "Unsigned32"
_RuckusDot1xTxPeriod_Object = MibScalar
ruckusDot1xTxPeriod = _RuckusDot1xTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 2, 2),
    _RuckusDot1xTxPeriod_Type()
)
ruckusDot1xTxPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xTxPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ruckusDot1xTxPeriod.setUnits("seconds")


class _RuckusDot1xSuppTimeout_Type(Unsigned32):
    """Custom type ruckusDot1xSuppTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuckusDot1xSuppTimeout_Type.__name__ = "Unsigned32"
_RuckusDot1xSuppTimeout_Object = MibScalar
ruckusDot1xSuppTimeout = _RuckusDot1xSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 2, 3),
    _RuckusDot1xSuppTimeout_Type()
)
ruckusDot1xSuppTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xSuppTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ruckusDot1xSuppTimeout.setUnits("seconds")


class _RuckusDot1xMaxReq_Type(Unsigned32):
    """Custom type ruckusDot1xMaxReq based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RuckusDot1xMaxReq_Type.__name__ = "Unsigned32"
_RuckusDot1xMaxReq_Object = MibScalar
ruckusDot1xMaxReq = _RuckusDot1xMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 2, 4),
    _RuckusDot1xMaxReq_Type()
)
ruckusDot1xMaxReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xMaxReq.setStatus("current")


class _RuckusDot1xMaxReauthReq_Type(Unsigned32):
    """Custom type ruckusDot1xMaxReauthReq based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RuckusDot1xMaxReauthReq_Type.__name__ = "Unsigned32"
_RuckusDot1xMaxReauthReq_Object = MibScalar
ruckusDot1xMaxReauthReq = _RuckusDot1xMaxReauthReq_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 2, 5),
    _RuckusDot1xMaxReauthReq_Type()
)
ruckusDot1xMaxReauthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xMaxReauthReq.setStatus("current")
_RuckusDot1xGuestVlan_Type = VlanId
_RuckusDot1xGuestVlan_Object = MibScalar
ruckusDot1xGuestVlan = _RuckusDot1xGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 2, 6),
    _RuckusDot1xGuestVlan_Type()
)
ruckusDot1xGuestVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xGuestVlan.setStatus("current")


class _RuckusDot1xMacAuthOverride_Type(EnabledStatus):
    """Custom type ruckusDot1xMacAuthOverride based on EnabledStatus"""
    defaultValue = 2


_RuckusDot1xMacAuthOverride_Type.__name__ = "EnabledStatus"
_RuckusDot1xMacAuthOverride_Object = MibScalar
ruckusDot1xMacAuthOverride = _RuckusDot1xMacAuthOverride_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 2, 7),
    _RuckusDot1xMacAuthOverride_Type()
)
ruckusDot1xMacAuthOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xMacAuthOverride.setStatus("current")
_RuckusMacAuthConfig_ObjectIdentity = ObjectIdentity
ruckusMacAuthConfig = _RuckusMacAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 3)
)


class _RuckusMacAuthPasswordFormat_Type(Integer32):
    """Custom type ruckusMacAuthPasswordFormat based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dashFormat", 1),
          ("colonFormat", 2),
          ("dotFormat", 3),
          ("normalFormat", 4))
    )


_RuckusMacAuthPasswordFormat_Type.__name__ = "Integer32"
_RuckusMacAuthPasswordFormat_Object = MibScalar
ruckusMacAuthPasswordFormat = _RuckusMacAuthPasswordFormat_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 3, 1),
    _RuckusMacAuthPasswordFormat_Type()
)
ruckusMacAuthPasswordFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusMacAuthPasswordFormat.setStatus("current")
_RuckusMacAuthPasswordOverride_Type = DisplayString
_RuckusMacAuthPasswordOverride_Object = MibScalar
ruckusMacAuthPasswordOverride = _RuckusMacAuthPasswordOverride_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 3, 2),
    _RuckusMacAuthPasswordOverride_Type()
)
ruckusMacAuthPasswordOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusMacAuthPasswordOverride.setStatus("current")


class _RuckusMacAuthDot1xOverride_Type(EnabledStatus):
    """Custom type ruckusMacAuthDot1xOverride based on EnabledStatus"""
    defaultValue = 2


_RuckusMacAuthDot1xOverride_Type.__name__ = "EnabledStatus"
_RuckusMacAuthDot1xOverride_Object = MibScalar
ruckusMacAuthDot1xOverride = _RuckusMacAuthDot1xOverride_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 3, 3),
    _RuckusMacAuthDot1xOverride_Type()
)
ruckusMacAuthDot1xOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusMacAuthDot1xOverride.setStatus("current")


class _RuckusMacAuthDot1xEnable_Type(EnabledStatus):
    """Custom type ruckusMacAuthDot1xEnable based on EnabledStatus"""
    defaultValue = 1


_RuckusMacAuthDot1xEnable_Type.__name__ = "EnabledStatus"
_RuckusMacAuthDot1xEnable_Object = MibScalar
ruckusMacAuthDot1xEnable = _RuckusMacAuthDot1xEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 3, 4),
    _RuckusMacAuthDot1xEnable_Type()
)
ruckusMacAuthDot1xEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusMacAuthDot1xEnable.setStatus("current")
_RuckusWebAuthConfig_ObjectIdentity = ObjectIdentity
ruckusWebAuthConfig = _RuckusWebAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4)
)
_RuckusWebAuthTable_Object = MibTable
ruckusWebAuthTable = _RuckusWebAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ruckusWebAuthTable.setStatus("current")
_RuckusWebAuthEntry_Object = MibTableRow
ruckusWebAuthEntry = _RuckusWebAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1)
)
ruckusWebAuthEntry.setIndexNames(
    (0, "RUCKUS-AUTH-MIB", "ruckusWebAuthVlan"),
)
if mibBuilder.loadTexts:
    ruckusWebAuthEntry.setStatus("current")
_RuckusWebAuthVlan_Type = VlanId
_RuckusWebAuthVlan_Object = MibTableColumn
ruckusWebAuthVlan = _RuckusWebAuthVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 1),
    _RuckusWebAuthVlan_Type()
)
ruckusWebAuthVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWebAuthVlan.setStatus("current")


class _RuckusWebAuthEnable_Type(EnabledStatus):
    """Custom type ruckusWebAuthEnable based on EnabledStatus"""
    defaultValue = 2


_RuckusWebAuthEnable_Type.__name__ = "EnabledStatus"
_RuckusWebAuthEnable_Object = MibTableColumn
ruckusWebAuthEnable = _RuckusWebAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 2),
    _RuckusWebAuthEnable_Type()
)
ruckusWebAuthEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthEnable.setStatus("current")


class _RuckusWebAuthMode_Type(Integer32):
    """Custom type ruckusWebAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("passcode", 2),
          ("password", 3),
          ("captivePortal", 4))
    )


_RuckusWebAuthMode_Type.__name__ = "Integer32"
_RuckusWebAuthMode_Object = MibTableColumn
ruckusWebAuthMode = _RuckusWebAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 3),
    _RuckusWebAuthMode_Type()
)
ruckusWebAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthMode.setStatus("current")


class _RuckusWebAuthMethod_Type(Integer32):
    """Custom type ruckusWebAuthMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("local", 2),
          ("radiusLocal", 3),
          ("localRadius", 4),
          ("none", 5))
    )


_RuckusWebAuthMethod_Type.__name__ = "Integer32"
_RuckusWebAuthMethod_Object = MibTableColumn
ruckusWebAuthMethod = _RuckusWebAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 4),
    _RuckusWebAuthMethod_Type()
)
ruckusWebAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthMethod.setStatus("current")


class _RuckusWebAuthMaxHosts_Type(Unsigned32):
    """Custom type ruckusWebAuthMaxHosts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_RuckusWebAuthMaxHosts_Type.__name__ = "Unsigned32"
_RuckusWebAuthMaxHosts_Object = MibTableColumn
ruckusWebAuthMaxHosts = _RuckusWebAuthMaxHosts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 5),
    _RuckusWebAuthMaxHosts_Type()
)
ruckusWebAuthMaxHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthMaxHosts.setStatus("current")


class _RuckusWebAuthMaxAuthAttempts_Type(Unsigned32):
    """Custom type ruckusWebAuthMaxAuthAttempts based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_RuckusWebAuthMaxAuthAttempts_Type.__name__ = "Unsigned32"
_RuckusWebAuthMaxAuthAttempts_Object = MibTableColumn
ruckusWebAuthMaxAuthAttempts = _RuckusWebAuthMaxAuthAttempts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 6),
    _RuckusWebAuthMaxAuthAttempts_Type()
)
ruckusWebAuthMaxAuthAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthMaxAuthAttempts.setStatus("current")


class _RuckusWebAuthReauthTime_Type(Unsigned32):
    """Custom type ruckusWebAuthReauthTime based on Unsigned32"""
    defaultValue = 28800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128000),
    )


_RuckusWebAuthReauthTime_Type.__name__ = "Unsigned32"
_RuckusWebAuthReauthTime_Object = MibTableColumn
ruckusWebAuthReauthTime = _RuckusWebAuthReauthTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 7),
    _RuckusWebAuthReauthTime_Type()
)
ruckusWebAuthReauthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthReauthTime.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWebAuthReauthTime.setUnits("seconds")


class _RuckusWebAuthCycleTime_Type(Unsigned32):
    """Custom type ruckusWebAuthCycleTime based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RuckusWebAuthCycleTime_Type.__name__ = "Unsigned32"
_RuckusWebAuthCycleTime_Object = MibTableColumn
ruckusWebAuthCycleTime = _RuckusWebAuthCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 8),
    _RuckusWebAuthCycleTime_Type()
)
ruckusWebAuthCycleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthCycleTime.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWebAuthCycleTime.setUnits("seconds")


class _RuckusWebAuthBlockTime_Type(Unsigned32):
    """Custom type ruckusWebAuthBlockTime based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12800),
    )


_RuckusWebAuthBlockTime_Type.__name__ = "Unsigned32"
_RuckusWebAuthBlockTime_Object = MibTableColumn
ruckusWebAuthBlockTime = _RuckusWebAuthBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 9),
    _RuckusWebAuthBlockTime_Type()
)
ruckusWebAuthBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthBlockTime.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWebAuthBlockTime.setUnits("seconds")


class _RuckusWebAuthMacAgeTime_Type(Unsigned32):
    """Custom type ruckusWebAuthMacAgeTime based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RuckusWebAuthMacAgeTime_Type.__name__ = "Unsigned32"
_RuckusWebAuthMacAgeTime_Object = MibTableColumn
ruckusWebAuthMacAgeTime = _RuckusWebAuthMacAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 10),
    _RuckusWebAuthMacAgeTime_Type()
)
ruckusWebAuthMacAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthMacAgeTime.setStatus("current")
_RuckusWebAuthPasscode_Type = DisplayString
_RuckusWebAuthPasscode_Object = MibTableColumn
ruckusWebAuthPasscode = _RuckusWebAuthPasscode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 11),
    _RuckusWebAuthPasscode_Type()
)
ruckusWebAuthPasscode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthPasscode.setStatus("current")
_RuckusWebAuthLocalUserDb_Type = DisplayString
_RuckusWebAuthLocalUserDb_Object = MibTableColumn
ruckusWebAuthLocalUserDb = _RuckusWebAuthLocalUserDb_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 12),
    _RuckusWebAuthLocalUserDb_Type()
)
ruckusWebAuthLocalUserDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthLocalUserDb.setStatus("current")


class _RuckusWebAuthSecureLogin_Type(EnabledStatus):
    """Custom type ruckusWebAuthSecureLogin based on EnabledStatus"""
    defaultValue = 1


_RuckusWebAuthSecureLogin_Type.__name__ = "EnabledStatus"
_RuckusWebAuthSecureLogin_Object = MibTableColumn
ruckusWebAuthSecureLogin = _RuckusWebAuthSecureLogin_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 13),
    _RuckusWebAuthSecureLogin_Type()
)
ruckusWebAuthSecureLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthSecureLogin.setStatus("current")


class _RuckusWebAuthAccounting_Type(EnabledStatus):
    """Custom type ruckusWebAuthAccounting based on EnabledStatus"""
    defaultValue = 2


_RuckusWebAuthAccounting_Type.__name__ = "EnabledStatus"
_RuckusWebAuthAccounting_Object = MibTableColumn
ruckusWebAuthAccounting = _RuckusWebAuthAccounting_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 14),
    _RuckusWebAuthAccounting_Type()
)
ruckusWebAuthAccounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthAccounting.setStatus("current")
_RuckusWebAuthCaptiveProfile_Type = DisplayString
_RuckusWebAuthCaptiveProfile_Object = MibTableColumn
ruckusWebAuthCaptiveProfile = _RuckusWebAuthCaptiveProfile_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 15),
    _RuckusWebAuthCaptiveProfile_Type()
)
ruckusWebAuthCaptiveProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthCaptiveProfile.setStatus("current")
_RuckusWebAuthRedirectName_Type = DisplayString
_RuckusWebAuthRedirectName_Object = MibTableColumn
ruckusWebAuthRedirectName = _RuckusWebAuthRedirectName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 16),
    _RuckusWebAuthRedirectName_Type()
)
ruckusWebAuthRedirectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthRedirectName.setStatus("current")


class _RuckusWebAuthWebpageRemoveUserId_Type(EnabledStatus):
    """Custom type ruckusWebAuthWebpageRemoveUserId based on EnabledStatus"""
    defaultValue = 2


_RuckusWebAuthWebpageRemoveUserId_Type.__name__ = "EnabledStatus"
_RuckusWebAuthWebpageRemoveUserId_Object = MibTableColumn
ruckusWebAuthWebpageRemoveUserId = _RuckusWebAuthWebpageRemoveUserId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 17),
    _RuckusWebAuthWebpageRemoveUserId_Type()
)
ruckusWebAuthWebpageRemoveUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWebAuthWebpageRemoveUserId.setStatus("current")
_RuckusWebAuthWebpageUsernameLabel_Type = DisplayString
_RuckusWebAuthWebpageUsernameLabel_Object = MibTableColumn
ruckusWebAuthWebpageUsernameLabel = _RuckusWebAuthWebpageUsernameLabel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 18),
    _RuckusWebAuthWebpageUsernameLabel_Type()
)
ruckusWebAuthWebpageUsernameLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWebAuthWebpageUsernameLabel.setStatus("current")
_RuckusWebAuthWebpagePasswordLabel_Type = DisplayString
_RuckusWebAuthWebpagePasswordLabel_Object = MibTableColumn
ruckusWebAuthWebpagePasswordLabel = _RuckusWebAuthWebpagePasswordLabel_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 19),
    _RuckusWebAuthWebpagePasswordLabel_Type()
)
ruckusWebAuthWebpagePasswordLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWebAuthWebpagePasswordLabel.setStatus("current")
_RuckusWebAuthUpLinkPort_Type = InterfaceIndexOrZero
_RuckusWebAuthUpLinkPort_Object = MibTableColumn
ruckusWebAuthUpLinkPort = _RuckusWebAuthUpLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 20),
    _RuckusWebAuthUpLinkPort_Type()
)
ruckusWebAuthUpLinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWebAuthUpLinkPort.setStatus("current")
_RuckusWebAuthWebpageTop_Type = DisplayString
_RuckusWebAuthWebpageTop_Object = MibTableColumn
ruckusWebAuthWebpageTop = _RuckusWebAuthWebpageTop_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 21),
    _RuckusWebAuthWebpageTop_Type()
)
ruckusWebAuthWebpageTop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWebAuthWebpageTop.setStatus("current")
_RuckusWebAuthWebpageBottom_Type = DisplayString
_RuckusWebAuthWebpageBottom_Object = MibTableColumn
ruckusWebAuthWebpageBottom = _RuckusWebAuthWebpageBottom_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 22),
    _RuckusWebAuthWebpageBottom_Type()
)
ruckusWebAuthWebpageBottom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWebAuthWebpageBottom.setStatus("current")
_RuckusWebAuthWebpageTitle_Type = DisplayString
_RuckusWebAuthWebpageTitle_Object = MibTableColumn
ruckusWebAuthWebpageTitle = _RuckusWebAuthWebpageTitle_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 23),
    _RuckusWebAuthWebpageTitle_Type()
)
ruckusWebAuthWebpageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWebAuthWebpageTitle.setStatus("current")
_RuckusWebAuthWebpageLoginButton_Type = DisplayString
_RuckusWebAuthWebpageLoginButton_Object = MibTableColumn
ruckusWebAuthWebpageLoginButton = _RuckusWebAuthWebpageLoginButton_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 1, 1, 24),
    _RuckusWebAuthWebpageLoginButton_Type()
)
ruckusWebAuthWebpageLoginButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWebAuthWebpageLoginButton.setStatus("current")
_RuckusWebAuthTrustPortTable_Object = MibTable
ruckusWebAuthTrustPortTable = _RuckusWebAuthTrustPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ruckusWebAuthTrustPortTable.setStatus("current")
_RuckusWebAuthTrustPortEntry_Object = MibTableRow
ruckusWebAuthTrustPortEntry = _RuckusWebAuthTrustPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 2, 1)
)
ruckusWebAuthTrustPortEntry.setIndexNames(
    (0, "RUCKUS-AUTH-MIB", "ruckusWebAuthVlan"),
    (0, "RUCKUS-AUTH-MIB", "ruckusWebAuthTrustPort"),
)
if mibBuilder.loadTexts:
    ruckusWebAuthTrustPortEntry.setStatus("current")
_RuckusWebAuthTrustPort_Type = InterfaceIndex
_RuckusWebAuthTrustPort_Object = MibTableColumn
ruckusWebAuthTrustPort = _RuckusWebAuthTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 2, 1, 1),
    _RuckusWebAuthTrustPort_Type()
)
ruckusWebAuthTrustPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthTrustPort.setStatus("current")
_RuckusWebAuthDnsFilterTable_Object = MibTable
ruckusWebAuthDnsFilterTable = _RuckusWebAuthDnsFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ruckusWebAuthDnsFilterTable.setStatus("current")
_RuckusWebAuthDnsFilterEntry_Object = MibTableRow
ruckusWebAuthDnsFilterEntry = _RuckusWebAuthDnsFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 3, 1)
)
ruckusWebAuthDnsFilterEntry.setIndexNames(
    (0, "RUCKUS-AUTH-MIB", "ruckusWebAuthVlan"),
    (0, "RUCKUS-AUTH-MIB", "ruckusWebAuthDnsFilterId"),
)
if mibBuilder.loadTexts:
    ruckusWebAuthDnsFilterEntry.setStatus("current")
_RuckusWebAuthDnsFilterId_Type = Integer32
_RuckusWebAuthDnsFilterId_Object = MibTableColumn
ruckusWebAuthDnsFilterId = _RuckusWebAuthDnsFilterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 3, 1, 1),
    _RuckusWebAuthDnsFilterId_Type()
)
ruckusWebAuthDnsFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWebAuthDnsFilterId.setStatus("current")
_RuckusWebAuthDnsFilterType_Type = InetAddressType
_RuckusWebAuthDnsFilterType_Object = MibTableColumn
ruckusWebAuthDnsFilterType = _RuckusWebAuthDnsFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 3, 1, 2),
    _RuckusWebAuthDnsFilterType_Type()
)
ruckusWebAuthDnsFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthDnsFilterType.setStatus("current")
_RuckusWebAuthDnsFilterAddr_Type = InetAddress
_RuckusWebAuthDnsFilterAddr_Object = MibTableColumn
ruckusWebAuthDnsFilterAddr = _RuckusWebAuthDnsFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 3, 1, 3),
    _RuckusWebAuthDnsFilterAddr_Type()
)
ruckusWebAuthDnsFilterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthDnsFilterAddr.setStatus("current")
_RuckusWebAuthDnsFilterPrefix_Type = Unsigned32
_RuckusWebAuthDnsFilterPrefix_Object = MibTableColumn
ruckusWebAuthDnsFilterPrefix = _RuckusWebAuthDnsFilterPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 3, 1, 4),
    _RuckusWebAuthDnsFilterPrefix_Type()
)
ruckusWebAuthDnsFilterPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthDnsFilterPrefix.setStatus("current")
_RuckusWebAuthWhiteListTable_Object = MibTable
ruckusWebAuthWhiteListTable = _RuckusWebAuthWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ruckusWebAuthWhiteListTable.setStatus("current")
_RuckusWebAuthWhiteListEntry_Object = MibTableRow
ruckusWebAuthWhiteListEntry = _RuckusWebAuthWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 4, 1)
)
ruckusWebAuthWhiteListEntry.setIndexNames(
    (0, "RUCKUS-AUTH-MIB", "ruckusWebAuthVlan"),
    (0, "RUCKUS-AUTH-MIB", "ruckusWebAuthWhiteListId"),
)
if mibBuilder.loadTexts:
    ruckusWebAuthWhiteListEntry.setStatus("current")
_RuckusWebAuthWhiteListId_Type = Integer32
_RuckusWebAuthWhiteListId_Object = MibTableColumn
ruckusWebAuthWhiteListId = _RuckusWebAuthWhiteListId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 4, 1, 1),
    _RuckusWebAuthWhiteListId_Type()
)
ruckusWebAuthWhiteListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWebAuthWhiteListId.setStatus("current")
_RuckusWebAuthWhiteListType_Type = InetAddressType
_RuckusWebAuthWhiteListType_Object = MibTableColumn
ruckusWebAuthWhiteListType = _RuckusWebAuthWhiteListType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 4, 1, 2),
    _RuckusWebAuthWhiteListType_Type()
)
ruckusWebAuthWhiteListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthWhiteListType.setStatus("current")
_RuckusWebAuthWhiteListAddr_Type = InetAddress
_RuckusWebAuthWhiteListAddr_Object = MibTableColumn
ruckusWebAuthWhiteListAddr = _RuckusWebAuthWhiteListAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 4, 1, 3),
    _RuckusWebAuthWhiteListAddr_Type()
)
ruckusWebAuthWhiteListAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthWhiteListAddr.setStatus("current")
_RuckusWebAuthWhiteListPrefix_Type = Unsigned32
_RuckusWebAuthWhiteListPrefix_Object = MibTableColumn
ruckusWebAuthWhiteListPrefix = _RuckusWebAuthWhiteListPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 4, 1, 4),
    _RuckusWebAuthWhiteListPrefix_Type()
)
ruckusWebAuthWhiteListPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthWhiteListPrefix.setStatus("current")
_RuckusWebAuthFilterTable_Object = MibTable
ruckusWebAuthFilterTable = _RuckusWebAuthFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 5)
)
if mibBuilder.loadTexts:
    ruckusWebAuthFilterTable.setStatus("current")
_RuckusWebAuthFilterEntry_Object = MibTableRow
ruckusWebAuthFilterEntry = _RuckusWebAuthFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 5, 1)
)
ruckusWebAuthFilterEntry.setIndexNames(
    (0, "RUCKUS-AUTH-MIB", "ruckusWebAuthVlan"),
    (0, "RUCKUS-AUTH-MIB", "ruckusWebAuthFilterMac"),
)
if mibBuilder.loadTexts:
    ruckusWebAuthFilterEntry.setStatus("current")
_RuckusWebAuthFilterMac_Type = MacAddress
_RuckusWebAuthFilterMac_Object = MibTableColumn
ruckusWebAuthFilterMac = _RuckusWebAuthFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 5, 1, 1),
    _RuckusWebAuthFilterMac_Type()
)
ruckusWebAuthFilterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthFilterMac.setStatus("current")
_RuckusWebAuthFilterPort_Type = InterfaceIndexOrZero
_RuckusWebAuthFilterPort_Object = MibTableColumn
ruckusWebAuthFilterPort = _RuckusWebAuthFilterPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 5, 1, 2),
    _RuckusWebAuthFilterPort_Type()
)
ruckusWebAuthFilterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthFilterPort.setStatus("current")


class _RuckusWebAuthFilterDuration_Type(Unsigned32):
    """Custom type ruckusWebAuthFilterDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12800),
    )


_RuckusWebAuthFilterDuration_Type.__name__ = "Unsigned32"
_RuckusWebAuthFilterDuration_Object = MibTableColumn
ruckusWebAuthFilterDuration = _RuckusWebAuthFilterDuration_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 5, 1, 3),
    _RuckusWebAuthFilterDuration_Type()
)
ruckusWebAuthFilterDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthFilterDuration.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWebAuthFilterDuration.setUnits("seconds")


class _RuckusWebAuthFilterAction_Type(Integer32):
    """Custom type ruckusWebAuthFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RuckusWebAuthFilterAction_Type.__name__ = "Integer32"
_RuckusWebAuthFilterAction_Object = MibTableColumn
ruckusWebAuthFilterAction = _RuckusWebAuthFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 5, 1, 4),
    _RuckusWebAuthFilterAction_Type()
)
ruckusWebAuthFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthFilterAction.setStatus("current")
_RuckusWebAuthCaptivePortalTable_Object = MibTable
ruckusWebAuthCaptivePortalTable = _RuckusWebAuthCaptivePortalTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 6)
)
if mibBuilder.loadTexts:
    ruckusWebAuthCaptivePortalTable.setStatus("current")
_RuckusWebAuthCaptivePortalEntry_Object = MibTableRow
ruckusWebAuthCaptivePortalEntry = _RuckusWebAuthCaptivePortalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 6, 1)
)
ruckusWebAuthCaptivePortalEntry.setIndexNames(
    (1, "RUCKUS-AUTH-MIB", "ruckusWebAuthCaptivePortalName"),
)
if mibBuilder.loadTexts:
    ruckusWebAuthCaptivePortalEntry.setStatus("current")


class _RuckusWebAuthCaptivePortalName_Type(DisplayString):
    """Custom type ruckusWebAuthCaptivePortalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusWebAuthCaptivePortalName_Type.__name__ = "DisplayString"
_RuckusWebAuthCaptivePortalName_Object = MibTableColumn
ruckusWebAuthCaptivePortalName = _RuckusWebAuthCaptivePortalName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 6, 1, 1),
    _RuckusWebAuthCaptivePortalName_Type()
)
ruckusWebAuthCaptivePortalName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWebAuthCaptivePortalName.setStatus("current")
_RuckusWebAuthCaptivePortalType_Type = InetAddressType
_RuckusWebAuthCaptivePortalType_Object = MibTableColumn
ruckusWebAuthCaptivePortalType = _RuckusWebAuthCaptivePortalType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 6, 1, 2),
    _RuckusWebAuthCaptivePortalType_Type()
)
ruckusWebAuthCaptivePortalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthCaptivePortalType.setStatus("current")
_RuckusWebAuthCaptivePortalAddr_Type = InetAddress
_RuckusWebAuthCaptivePortalAddr_Object = MibTableColumn
ruckusWebAuthCaptivePortalAddr = _RuckusWebAuthCaptivePortalAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 6, 1, 3),
    _RuckusWebAuthCaptivePortalAddr_Type()
)
ruckusWebAuthCaptivePortalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthCaptivePortalAddr.setStatus("current")


class _RuckusWebAuthCaptivePortalPort_Type(Unsigned32):
    """Custom type ruckusWebAuthCaptivePortalPort based on Unsigned32"""
    defaultValue = 443


_RuckusWebAuthCaptivePortalPort_Type.__name__ = "Unsigned32"
_RuckusWebAuthCaptivePortalPort_Object = MibTableColumn
ruckusWebAuthCaptivePortalPort = _RuckusWebAuthCaptivePortalPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 6, 1, 4),
    _RuckusWebAuthCaptivePortalPort_Type()
)
ruckusWebAuthCaptivePortalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthCaptivePortalPort.setStatus("current")
_RuckusWebAuthCaptivePortalLoginPage_Type = DisplayString
_RuckusWebAuthCaptivePortalLoginPage_Object = MibTableColumn
ruckusWebAuthCaptivePortalLoginPage = _RuckusWebAuthCaptivePortalLoginPage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 4, 6, 1, 5),
    _RuckusWebAuthCaptivePortalLoginPage_Type()
)
ruckusWebAuthCaptivePortalLoginPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWebAuthCaptivePortalLoginPage.setStatus("current")
_RuckusAuthPortConfig_ObjectIdentity = ObjectIdentity
ruckusAuthPortConfig = _RuckusAuthPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5)
)
_RuckusAuthPortTable_Object = MibTable
ruckusAuthPortTable = _RuckusAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ruckusAuthPortTable.setStatus("current")
_RuckusAuthPortEntry_Object = MibTableRow
ruckusAuthPortEntry = _RuckusAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1)
)
ruckusAuthPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusAuthPortEntry.setStatus("current")


class _RuckusAuthPortEnable_Type(Bits):
    """Custom type ruckusAuthPortEnable based on Bits"""
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("macAuth", 1))
    )

_RuckusAuthPortEnable_Type.__name__ = "Bits"
_RuckusAuthPortEnable_Object = MibTableColumn
ruckusAuthPortEnable = _RuckusAuthPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 1),
    _RuckusAuthPortEnable_Type()
)
ruckusAuthPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortEnable.setStatus("current")


class _RuckusAuthPortDot1xControl_Type(Integer32):
    """Custom type ruckusAuthPortDot1xControl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("forceUnauthorized", 1),
          ("controlauto", 2),
          ("forceAuthorized", 3),
          ("other", 4))
    )


_RuckusAuthPortDot1xControl_Type.__name__ = "Integer32"
_RuckusAuthPortDot1xControl_Object = MibTableColumn
ruckusAuthPortDot1xControl = _RuckusAuthPortDot1xControl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 2),
    _RuckusAuthPortDot1xControl_Type()
)
ruckusAuthPortDot1xControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortDot1xControl.setStatus("current")
_RuckusAuthPortDefaultVlan_Type = VlanId
_RuckusAuthPortDefaultVlan_Object = MibTableColumn
ruckusAuthPortDefaultVlan = _RuckusAuthPortDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 3),
    _RuckusAuthPortDefaultVlan_Type()
)
ruckusAuthPortDefaultVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortDefaultVlan.setStatus("current")
_RuckusAuthPortVoiceVlan_Type = VlanId
_RuckusAuthPortVoiceVlan_Object = MibTableColumn
ruckusAuthPortVoiceVlan = _RuckusAuthPortVoiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 4),
    _RuckusAuthPortVoiceVlan_Type()
)
ruckusAuthPortVoiceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortVoiceVlan.setStatus("current")
_RuckusAuthPortCriticalVlan_Type = VlanId
_RuckusAuthPortCriticalVlan_Object = MibTableColumn
ruckusAuthPortCriticalVlan = _RuckusAuthPortCriticalVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 5),
    _RuckusAuthPortCriticalVlan_Type()
)
ruckusAuthPortCriticalVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortCriticalVlan.setStatus("current")
_RuckusAuthPortRestrictVlan_Type = VlanId
_RuckusAuthPortRestrictVlan_Object = MibTableColumn
ruckusAuthPortRestrictVlan = _RuckusAuthPortRestrictVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 6),
    _RuckusAuthPortRestrictVlan_Type()
)
ruckusAuthPortRestrictVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortRestrictVlan.setStatus("current")


class _RuckusAuthPortMode_Type(RuckusAuthMode):
    """Custom type ruckusAuthPortMode based on RuckusAuthMode"""
    defaultValue = 1


_RuckusAuthPortMode_Type.__name__ = "RuckusAuthMode"
_RuckusAuthPortMode_Object = MibTableColumn
ruckusAuthPortMode = _RuckusAuthPortMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 7),
    _RuckusAuthPortMode_Type()
)
ruckusAuthPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortMode.setStatus("current")


class _RuckusAuthPortMethods_Type(RuckusAuthOrder):
    """Custom type ruckusAuthPortMethods based on RuckusAuthOrder"""
    defaultValue = 1


_RuckusAuthPortMethods_Type.__name__ = "RuckusAuthOrder"
_RuckusAuthPortMethods_Object = MibTableColumn
ruckusAuthPortMethods = _RuckusAuthPortMethods_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 8),
    _RuckusAuthPortMethods_Type()
)
ruckusAuthPortMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortMethods.setStatus("current")


class _RuckusAuthPortMaxSessions_Type(Unsigned32):
    """Custom type ruckusAuthPortMaxSessions based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RuckusAuthPortMaxSessions_Type.__name__ = "Unsigned32"
_RuckusAuthPortMaxSessions_Object = MibTableColumn
ruckusAuthPortMaxSessions = _RuckusAuthPortMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 9),
    _RuckusAuthPortMaxSessions_Type()
)
ruckusAuthPortMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortMaxSessions.setStatus("current")


class _RuckusAuthPortFailAction_Type(RuckusAuthFailAction):
    """Custom type ruckusAuthPortFailAction based on RuckusAuthFailAction"""
    defaultValue = 1


_RuckusAuthPortFailAction_Type.__name__ = "RuckusAuthFailAction"
_RuckusAuthPortFailAction_Object = MibTableColumn
ruckusAuthPortFailAction = _RuckusAuthPortFailAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 10),
    _RuckusAuthPortFailAction_Type()
)
ruckusAuthPortFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortFailAction.setStatus("current")


class _RuckusAuthPortTimeoutAction_Type(RuckusAuthTimeoutAction):
    """Custom type ruckusAuthPortTimeoutAction based on RuckusAuthTimeoutAction"""
    defaultValue = 4


_RuckusAuthPortTimeoutAction_Type.__name__ = "RuckusAuthTimeoutAction"
_RuckusAuthPortTimeoutAction_Object = MibTableColumn
ruckusAuthPortTimeoutAction = _RuckusAuthPortTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 11),
    _RuckusAuthPortTimeoutAction_Type()
)
ruckusAuthPortTimeoutAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortTimeoutAction.setStatus("current")


class _RuckusAuthPortReauthTimeout_Type(Unsigned32):
    """Custom type ruckusAuthPortReauthTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RuckusAuthPortReauthTimeout_Type.__name__ = "Unsigned32"
_RuckusAuthPortReauthTimeout_Object = MibTableColumn
ruckusAuthPortReauthTimeout = _RuckusAuthPortReauthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 12),
    _RuckusAuthPortReauthTimeout_Type()
)
ruckusAuthPortReauthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortReauthTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAuthPortReauthTimeout.setUnits("seconds")
_RuckusAuthPortAging_Type = RuckusAuthAging
_RuckusAuthPortAging_Object = MibTableColumn
ruckusAuthPortAging = _RuckusAuthPortAging_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 13),
    _RuckusAuthPortAging_Type()
)
ruckusAuthPortAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortAging.setStatus("current")


class _RuckusAuthPortAllowTagged_Type(EnabledStatus):
    """Custom type ruckusAuthPortAllowTagged based on EnabledStatus"""
    defaultValue = 2


_RuckusAuthPortAllowTagged_Type.__name__ = "EnabledStatus"
_RuckusAuthPortAllowTagged_Object = MibTableColumn
ruckusAuthPortAllowTagged = _RuckusAuthPortAllowTagged_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 14),
    _RuckusAuthPortAllowTagged_Type()
)
ruckusAuthPortAllowTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortAllowTagged.setStatus("current")


class _RuckusAuthPortSourceGuard_Type(EnabledStatus):
    """Custom type ruckusAuthPortSourceGuard based on EnabledStatus"""
    defaultValue = 2


_RuckusAuthPortSourceGuard_Type.__name__ = "EnabledStatus"
_RuckusAuthPortSourceGuard_Object = MibTableColumn
ruckusAuthPortSourceGuard = _RuckusAuthPortSourceGuard_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 15),
    _RuckusAuthPortSourceGuard_Type()
)
ruckusAuthPortSourceGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortSourceGuard.setStatus("current")


class _RuckusAuthPortDosAttacks_Type(EnabledStatus):
    """Custom type ruckusAuthPortDosAttacks based on EnabledStatus"""
    defaultValue = 2


_RuckusAuthPortDosAttacks_Type.__name__ = "EnabledStatus"
_RuckusAuthPortDosAttacks_Object = MibTableColumn
ruckusAuthPortDosAttacks = _RuckusAuthPortDosAttacks_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 16),
    _RuckusAuthPortDosAttacks_Type()
)
ruckusAuthPortDosAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortDosAttacks.setStatus("current")


class _RuckusAuthPortDosAttackLimit_Type(Unsigned32):
    """Custom type ruckusAuthPortDosAttackLimit based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuckusAuthPortDosAttackLimit_Type.__name__ = "Unsigned32"
_RuckusAuthPortDosAttackLimit_Object = MibTableColumn
ruckusAuthPortDosAttackLimit = _RuckusAuthPortDosAttackLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 5, 1, 1, 17),
    _RuckusAuthPortDosAttackLimit_Type()
)
ruckusAuthPortDosAttackLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthPortDosAttackLimit.setStatus("current")
_RuckusAuthFilterConfig_ObjectIdentity = ObjectIdentity
ruckusAuthFilterConfig = _RuckusAuthFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 6)
)
_RuckusAuthFilterTable_Object = MibTable
ruckusAuthFilterTable = _RuckusAuthFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ruckusAuthFilterTable.setStatus("current")
_RuckusAuthFilterEntry_Object = MibTableRow
ruckusAuthFilterEntry = _RuckusAuthFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 6, 1, 1)
)
ruckusAuthFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-AUTH-MIB", "ruckusAuthFilterId"),
)
if mibBuilder.loadTexts:
    ruckusAuthFilterEntry.setStatus("current")
_RuckusAuthFilterId_Type = Integer32
_RuckusAuthFilterId_Object = MibTableColumn
ruckusAuthFilterId = _RuckusAuthFilterId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 6, 1, 1, 1),
    _RuckusAuthFilterId_Type()
)
ruckusAuthFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAuthFilterId.setStatus("current")
_RuckusAuthFilterMac_Type = MacAddress
_RuckusAuthFilterMac_Object = MibTableColumn
ruckusAuthFilterMac = _RuckusAuthFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 6, 1, 1, 2),
    _RuckusAuthFilterMac_Type()
)
ruckusAuthFilterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthFilterMac.setStatus("current")
_RuckusAuthFilterMask_Type = MacAddress
_RuckusAuthFilterMask_Object = MibTableColumn
ruckusAuthFilterMask = _RuckusAuthFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 6, 1, 1, 3),
    _RuckusAuthFilterMask_Type()
)
ruckusAuthFilterMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthFilterMask.setStatus("current")
_RuckusAuthFilterVlan_Type = VlanId
_RuckusAuthFilterVlan_Object = MibTableColumn
ruckusAuthFilterVlan = _RuckusAuthFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 6, 1, 1, 4),
    _RuckusAuthFilterVlan_Type()
)
ruckusAuthFilterVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthFilterVlan.setStatus("current")


class _RuckusAuthFilterAction_Type(Integer32):
    """Custom type ruckusAuthFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RuckusAuthFilterAction_Type.__name__ = "Integer32"
_RuckusAuthFilterAction_Object = MibTableColumn
ruckusAuthFilterAction = _RuckusAuthFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 6, 1, 1, 5),
    _RuckusAuthFilterAction_Type()
)
ruckusAuthFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthFilterAction.setStatus("current")
_RuckusAuthSessions_ObjectIdentity = ObjectIdentity
ruckusAuthSessions = _RuckusAuthSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7)
)
_RuckusAuthSessionTable_Object = MibTable
ruckusAuthSessionTable = _RuckusAuthSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ruckusAuthSessionTable.setStatus("current")
_RuckusAuthSessionEntry_Object = MibTableRow
ruckusAuthSessionEntry = _RuckusAuthSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1)
)
ruckusAuthSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-AUTH-MIB", "ruckusAuthSessionMac"),
)
if mibBuilder.loadTexts:
    ruckusAuthSessionEntry.setStatus("current")
_RuckusAuthSessionMac_Type = MacAddress
_RuckusAuthSessionMac_Object = MibTableColumn
ruckusAuthSessionMac = _RuckusAuthSessionMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 1),
    _RuckusAuthSessionMac_Type()
)
ruckusAuthSessionMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionMac.setStatus("current")
_RuckusAuthSessionVlan_Type = VlanId
_RuckusAuthSessionVlan_Object = MibTableColumn
ruckusAuthSessionVlan = _RuckusAuthSessionVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 2),
    _RuckusAuthSessionVlan_Type()
)
ruckusAuthSessionVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionVlan.setStatus("current")


class _RuckusAuthSessionVlanType_Type(Integer32):
    """Custom type ruckusAuthSessionVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("retrict", 2),
          ("critical", 3),
          ("guest", 4),
          ("radius", 5))
    )


_RuckusAuthSessionVlanType_Type.__name__ = "Integer32"
_RuckusAuthSessionVlanType_Object = MibTableColumn
ruckusAuthSessionVlanType = _RuckusAuthSessionVlanType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 3),
    _RuckusAuthSessionVlanType_Type()
)
ruckusAuthSessionVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionVlanType.setStatus("current")
_RuckusAuthSessionTaggedVlan_Type = VlanId
_RuckusAuthSessionTaggedVlan_Object = MibTableColumn
ruckusAuthSessionTaggedVlan = _RuckusAuthSessionTaggedVlan_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 4),
    _RuckusAuthSessionTaggedVlan_Type()
)
ruckusAuthSessionTaggedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionTaggedVlan.setStatus("current")
_RuckusAuthSessionUserName_Type = DisplayString
_RuckusAuthSessionUserName_Object = MibTableColumn
ruckusAuthSessionUserName = _RuckusAuthSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 5),
    _RuckusAuthSessionUserName_Type()
)
ruckusAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionUserName.setStatus("current")


class _RuckusAuthSessionDeviceType_Type(Integer32):
    """Custom type ruckusAuthSessionDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("phone", 1),
          ("wlanAP", 2),
          ("router", 3),
          ("bridge", 4),
          ("other", 8))
    )


_RuckusAuthSessionDeviceType_Type.__name__ = "Integer32"
_RuckusAuthSessionDeviceType_Object = MibTableColumn
ruckusAuthSessionDeviceType = _RuckusAuthSessionDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 6),
    _RuckusAuthSessionDeviceType_Type()
)
ruckusAuthSessionDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionDeviceType.setStatus("current")


class _RuckusAuthSessionMethod_Type(Integer32):
    """Custom type ruckusAuthSessionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 1),
          ("macAuth", 2))
    )


_RuckusAuthSessionMethod_Type.__name__ = "Integer32"
_RuckusAuthSessionMethod_Object = MibTableColumn
ruckusAuthSessionMethod = _RuckusAuthSessionMethod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 7),
    _RuckusAuthSessionMethod_Type()
)
ruckusAuthSessionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionMethod.setStatus("current")
_RuckusAuthSessionMode_Type = RuckusAuthMode
_RuckusAuthSessionMode_Object = MibTableColumn
ruckusAuthSessionMode = _RuckusAuthSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 8),
    _RuckusAuthSessionMode_Type()
)
ruckusAuthSessionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionMode.setStatus("current")


class _RuckusAuthSessionStatus_Type(Integer32):
    """Custom type ruckusAuthSessionStatus based on Integer32"""
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
        *(("allowed", 1),
          ("blocked", 2),
          ("restrict", 3),
          ("critical", 4),
          ("guest", 5),
          ("other", 6))
    )


_RuckusAuthSessionStatus_Type.__name__ = "Integer32"
_RuckusAuthSessionStatus_Object = MibTableColumn
ruckusAuthSessionStatus = _RuckusAuthSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 9),
    _RuckusAuthSessionStatus_Type()
)
ruckusAuthSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionStatus.setStatus("current")
_RuckusAuthSessionDot1xStatus_Type = Dot1xAuthState
_RuckusAuthSessionDot1xStatus_Object = MibTableColumn
ruckusAuthSessionDot1xStatus = _RuckusAuthSessionDot1xStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 10),
    _RuckusAuthSessionDot1xStatus_Type()
)
ruckusAuthSessionDot1xStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionDot1xStatus.setStatus("current")


class _RuckusAuthSessionAgingType_Type(Integer32):
    """Custom type ruckusAuthSessionAgingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("software", 1),
          ("hardware", 2),
          ("enabled", 3),
          ("disabled", 4))
    )


_RuckusAuthSessionAgingType_Type.__name__ = "Integer32"
_RuckusAuthSessionAgingType_Object = MibTableColumn
ruckusAuthSessionAgingType = _RuckusAuthSessionAgingType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 11),
    _RuckusAuthSessionAgingType_Type()
)
ruckusAuthSessionAgingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionAgingType.setStatus("current")
_RuckusAuthSessionAge_Type = Unsigned32
_RuckusAuthSessionAge_Object = MibTableColumn
ruckusAuthSessionAge = _RuckusAuthSessionAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 12),
    _RuckusAuthSessionAge_Type()
)
ruckusAuthSessionAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionAge.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAuthSessionAge.setUnits("seconds")
_RuckusAuthSessionTimeout_Type = Unsigned32
_RuckusAuthSessionTimeout_Object = MibTableColumn
ruckusAuthSessionTimeout = _RuckusAuthSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 13),
    _RuckusAuthSessionTimeout_Type()
)
ruckusAuthSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAuthSessionTimeout.setUnits("seconds")
_RuckusAuthSessionIdleTimeout_Type = Unsigned32
_RuckusAuthSessionIdleTimeout_Object = MibTableColumn
ruckusAuthSessionIdleTimeout = _RuckusAuthSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 14),
    _RuckusAuthSessionIdleTimeout_Type()
)
ruckusAuthSessionIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAuthSessionIdleTimeout.setUnits("seconds")
_RuckusAuthSessionTime_Type = Unsigned32
_RuckusAuthSessionTime_Object = MibTableColumn
ruckusAuthSessionTime = _RuckusAuthSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 15),
    _RuckusAuthSessionTime_Type()
)
ruckusAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionTime.setStatus("current")
if mibBuilder.loadTexts:
    ruckusAuthSessionTime.setUnits("seconds")
_RuckusAuthSessionV4IngressAcl_Type = DisplayString
_RuckusAuthSessionV4IngressAcl_Object = MibTableColumn
ruckusAuthSessionV4IngressAcl = _RuckusAuthSessionV4IngressAcl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 16),
    _RuckusAuthSessionV4IngressAcl_Type()
)
ruckusAuthSessionV4IngressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionV4IngressAcl.setStatus("current")
_RuckusAuthSessionV4EgressAcl_Type = DisplayString
_RuckusAuthSessionV4EgressAcl_Object = MibTableColumn
ruckusAuthSessionV4EgressAcl = _RuckusAuthSessionV4EgressAcl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 17),
    _RuckusAuthSessionV4EgressAcl_Type()
)
ruckusAuthSessionV4EgressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionV4EgressAcl.setStatus("current")
_RuckusAuthSessionV6IngressAcl_Type = DisplayString
_RuckusAuthSessionV6IngressAcl_Object = MibTableColumn
ruckusAuthSessionV6IngressAcl = _RuckusAuthSessionV6IngressAcl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 18),
    _RuckusAuthSessionV6IngressAcl_Type()
)
ruckusAuthSessionV6IngressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionV6IngressAcl.setStatus("current")
_RuckusAuthSessionV6EgressAcl_Type = DisplayString
_RuckusAuthSessionV6EgressAcl_Object = MibTableColumn
ruckusAuthSessionV6EgressAcl = _RuckusAuthSessionV6EgressAcl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 19),
    _RuckusAuthSessionV6EgressAcl_Type()
)
ruckusAuthSessionV6EgressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionV6EgressAcl.setStatus("current")
_RuckusAuthSessionTxOctets_Type = Counter64
_RuckusAuthSessionTxOctets_Object = MibTableColumn
ruckusAuthSessionTxOctets = _RuckusAuthSessionTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 20),
    _RuckusAuthSessionTxOctets_Type()
)
ruckusAuthSessionTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionTxOctets.setStatus("current")
_RuckusAuthSessionRxOctets_Type = Counter64
_RuckusAuthSessionRxOctets_Object = MibTableColumn
ruckusAuthSessionRxOctets = _RuckusAuthSessionRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 21),
    _RuckusAuthSessionRxOctets_Type()
)
ruckusAuthSessionRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionRxOctets.setStatus("current")
_RuckusAuthSessionTxPkts_Type = Counter64
_RuckusAuthSessionTxPkts_Object = MibTableColumn
ruckusAuthSessionTxPkts = _RuckusAuthSessionTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 22),
    _RuckusAuthSessionTxPkts_Type()
)
ruckusAuthSessionTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionTxPkts.setStatus("current")
_RuckusAuthSessionRxPkts_Type = Counter64
_RuckusAuthSessionRxPkts_Object = MibTableColumn
ruckusAuthSessionRxPkts = _RuckusAuthSessionRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 23),
    _RuckusAuthSessionRxPkts_Type()
)
ruckusAuthSessionRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionRxPkts.setStatus("current")
_RuckusAuthSessionFailureReason_Type = DisplayString
_RuckusAuthSessionFailureReason_Object = MibTableColumn
ruckusAuthSessionFailureReason = _RuckusAuthSessionFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 24),
    _RuckusAuthSessionFailureReason_Type()
)
ruckusAuthSessionFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionFailureReason.setStatus("current")


class _RuckusAuthSessionFlags_Type(Bits):
    """Custom type ruckusAuthSessionFlags based on Bits"""
    namedValues = NamedValues(
        *(("staticAuthenticated", 0),
          ("taggedSession", 1),
          ("dot1xNonCapable", 2),
          ("dot1xEnabled", 3),
          ("masterMacAuth", 4),
          ("v4AclApplied", 5),
          ("v6AclApplied", 6))
    )

_RuckusAuthSessionFlags_Type.__name__ = "Bits"
_RuckusAuthSessionFlags_Object = MibTableColumn
ruckusAuthSessionFlags = _RuckusAuthSessionFlags_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 1, 1, 25),
    _RuckusAuthSessionFlags_Type()
)
ruckusAuthSessionFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionFlags.setStatus("current")
_RuckusAuthSessionAddrTable_Object = MibTable
ruckusAuthSessionAddrTable = _RuckusAuthSessionAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ruckusAuthSessionAddrTable.setStatus("current")
_RuckusAuthSessionAddrEntry_Object = MibTableRow
ruckusAuthSessionAddrEntry = _RuckusAuthSessionAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 2, 1)
)
ruckusAuthSessionAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-AUTH-MIB", "ruckusAuthSessionMac"),
    (0, "RUCKUS-AUTH-MIB", "ruckusAuthSessionAddrId"),
)
if mibBuilder.loadTexts:
    ruckusAuthSessionAddrEntry.setStatus("current")
_RuckusAuthSessionAddrId_Type = Integer32
_RuckusAuthSessionAddrId_Object = MibTableColumn
ruckusAuthSessionAddrId = _RuckusAuthSessionAddrId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 2, 1, 1),
    _RuckusAuthSessionAddrId_Type()
)
ruckusAuthSessionAddrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAuthSessionAddrId.setStatus("current")
_RuckusAuthSessionAddrType_Type = InetAddressType
_RuckusAuthSessionAddrType_Object = MibTableColumn
ruckusAuthSessionAddrType = _RuckusAuthSessionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 2, 1, 2),
    _RuckusAuthSessionAddrType_Type()
)
ruckusAuthSessionAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionAddrType.setStatus("current")
_RuckusAuthSessionAddr_Type = InetAddress
_RuckusAuthSessionAddr_Object = MibTableColumn
ruckusAuthSessionAddr = _RuckusAuthSessionAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 7, 2, 1, 3),
    _RuckusAuthSessionAddr_Type()
)
ruckusAuthSessionAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAuthSessionAddr.setStatus("current")
_RuckusAuthStatistics_ObjectIdentity = ObjectIdentity
ruckusAuthStatistics = _RuckusAuthStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8)
)
_RuckusAuthStatsTable_Object = MibTable
ruckusAuthStatsTable = _RuckusAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ruckusAuthStatsTable.setStatus("current")
_RuckusAuthStatsEntry_Object = MibTableRow
ruckusAuthStatsEntry = _RuckusAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1)
)
ruckusAuthStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusAuthStatsEntry.setStatus("current")
_RuckusDot1xSessionsAttempted_Type = Counter32
_RuckusDot1xSessionsAttempted_Object = MibTableColumn
ruckusDot1xSessionsAttempted = _RuckusDot1xSessionsAttempted_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 1),
    _RuckusDot1xSessionsAttempted_Type()
)
ruckusDot1xSessionsAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xSessionsAttempted.setStatus("current")
_RuckusDot1xSessionsAccepted_Type = Counter32
_RuckusDot1xSessionsAccepted_Object = MibTableColumn
ruckusDot1xSessionsAccepted = _RuckusDot1xSessionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 2),
    _RuckusDot1xSessionsAccepted_Type()
)
ruckusDot1xSessionsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xSessionsAccepted.setStatus("current")
_RuckusDot1xSessionsRejected_Type = Counter32
_RuckusDot1xSessionsRejected_Object = MibTableColumn
ruckusDot1xSessionsRejected = _RuckusDot1xSessionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 3),
    _RuckusDot1xSessionsRejected_Type()
)
ruckusDot1xSessionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xSessionsRejected.setStatus("current")
_RuckusDot1xSessionsInProgress_Type = Counter32
_RuckusDot1xSessionsInProgress_Object = MibTableColumn
ruckusDot1xSessionsInProgress = _RuckusDot1xSessionsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 4),
    _RuckusDot1xSessionsInProgress_Type()
)
ruckusDot1xSessionsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xSessionsInProgress.setStatus("current")
_RuckusDot1xSessionsErrored_Type = Counter32
_RuckusDot1xSessionsErrored_Object = MibTableColumn
ruckusDot1xSessionsErrored = _RuckusDot1xSessionsErrored_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 5),
    _RuckusDot1xSessionsErrored_Type()
)
ruckusDot1xSessionsErrored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xSessionsErrored.setStatus("current")
_RuckusMacAuthSessionsAttempted_Type = Counter32
_RuckusMacAuthSessionsAttempted_Object = MibTableColumn
ruckusMacAuthSessionsAttempted = _RuckusMacAuthSessionsAttempted_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 6),
    _RuckusMacAuthSessionsAttempted_Type()
)
ruckusMacAuthSessionsAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusMacAuthSessionsAttempted.setStatus("current")
_RuckusMacAuthSessionsAccepted_Type = Counter32
_RuckusMacAuthSessionsAccepted_Object = MibTableColumn
ruckusMacAuthSessionsAccepted = _RuckusMacAuthSessionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 7),
    _RuckusMacAuthSessionsAccepted_Type()
)
ruckusMacAuthSessionsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusMacAuthSessionsAccepted.setStatus("current")
_RuckusMacAuthSessionsRejected_Type = Counter32
_RuckusMacAuthSessionsRejected_Object = MibTableColumn
ruckusMacAuthSessionsRejected = _RuckusMacAuthSessionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 8),
    _RuckusMacAuthSessionsRejected_Type()
)
ruckusMacAuthSessionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusMacAuthSessionsRejected.setStatus("current")
_RuckusMacAuthSessionsInProgress_Type = Counter32
_RuckusMacAuthSessionsInProgress_Object = MibTableColumn
ruckusMacAuthSessionsInProgress = _RuckusMacAuthSessionsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 9),
    _RuckusMacAuthSessionsInProgress_Type()
)
ruckusMacAuthSessionsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusMacAuthSessionsInProgress.setStatus("current")
_RuckusMacAuthSessionsErrored_Type = Counter32
_RuckusMacAuthSessionsErrored_Object = MibTableColumn
ruckusMacAuthSessionsErrored = _RuckusMacAuthSessionsErrored_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 1, 1, 10),
    _RuckusMacAuthSessionsErrored_Type()
)
ruckusMacAuthSessionsErrored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusMacAuthSessionsErrored.setStatus("current")
_RuckusDot1xAuthStatsTable_Object = MibTable
ruckusDot1xAuthStatsTable = _RuckusDot1xAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ruckusDot1xAuthStatsTable.setStatus("current")
_RuckusDot1xAuthStatsEntry_Object = MibTableRow
ruckusDot1xAuthStatsEntry = _RuckusDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1)
)
ruckusDot1xAuthStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusDot1xAuthStatsEntry.setStatus("current")
_RuckusDot1xTxEAPFrames_Type = Counter32
_RuckusDot1xTxEAPFrames_Object = MibTableColumn
ruckusDot1xTxEAPFrames = _RuckusDot1xTxEAPFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 1),
    _RuckusDot1xTxEAPFrames_Type()
)
ruckusDot1xTxEAPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xTxEAPFrames.setStatus("current")
_RuckusDot1xTxEAPReqIdFrames_Type = Counter32
_RuckusDot1xTxEAPReqIdFrames_Object = MibTableColumn
ruckusDot1xTxEAPReqIdFrames = _RuckusDot1xTxEAPReqIdFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 2),
    _RuckusDot1xTxEAPReqIdFrames_Type()
)
ruckusDot1xTxEAPReqIdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xTxEAPReqIdFrames.setStatus("current")
_RuckusDot1xTxEAPReqFrames_Type = Counter32
_RuckusDot1xTxEAPReqFrames_Object = MibTableColumn
ruckusDot1xTxEAPReqFrames = _RuckusDot1xTxEAPReqFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 3),
    _RuckusDot1xTxEAPReqFrames_Type()
)
ruckusDot1xTxEAPReqFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xTxEAPReqFrames.setStatus("current")
_RuckusDot1xRxEAPFrames_Type = Counter32
_RuckusDot1xRxEAPFrames_Object = MibTableColumn
ruckusDot1xRxEAPFrames = _RuckusDot1xRxEAPFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 4),
    _RuckusDot1xRxEAPFrames_Type()
)
ruckusDot1xRxEAPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xRxEAPFrames.setStatus("current")
_RuckusDot1xRxEAPStartFrames_Type = Counter32
_RuckusDot1xRxEAPStartFrames_Object = MibTableColumn
ruckusDot1xRxEAPStartFrames = _RuckusDot1xRxEAPStartFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 5),
    _RuckusDot1xRxEAPStartFrames_Type()
)
ruckusDot1xRxEAPStartFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xRxEAPStartFrames.setStatus("current")
_RuckusDot1xRxEAPLogOffFrames_Type = Counter32
_RuckusDot1xRxEAPLogOffFrames_Object = MibTableColumn
ruckusDot1xRxEAPLogOffFrames = _RuckusDot1xRxEAPLogOffFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 6),
    _RuckusDot1xRxEAPLogOffFrames_Type()
)
ruckusDot1xRxEAPLogOffFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xRxEAPLogOffFrames.setStatus("current")
_RuckusDot1xRxEAPRespIdFrames_Type = Counter32
_RuckusDot1xRxEAPRespIdFrames_Object = MibTableColumn
ruckusDot1xRxEAPRespIdFrames = _RuckusDot1xRxEAPRespIdFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 7),
    _RuckusDot1xRxEAPRespIdFrames_Type()
)
ruckusDot1xRxEAPRespIdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xRxEAPRespIdFrames.setStatus("current")
_RuckusDot1xRxEAPRespFrames_Type = Counter32
_RuckusDot1xRxEAPRespFrames_Object = MibTableColumn
ruckusDot1xRxEAPRespFrames = _RuckusDot1xRxEAPRespFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 8),
    _RuckusDot1xRxEAPRespFrames_Type()
)
ruckusDot1xRxEAPRespFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xRxEAPRespFrames.setStatus("current")
_RuckusDot1xRxEAPInvalidFrames_Type = Counter32
_RuckusDot1xRxEAPInvalidFrames_Object = MibTableColumn
ruckusDot1xRxEAPInvalidFrames = _RuckusDot1xRxEAPInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 9),
    _RuckusDot1xRxEAPInvalidFrames_Type()
)
ruckusDot1xRxEAPInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xRxEAPInvalidFrames.setStatus("current")
_RuckusDot1xRxLengthErrorFrames_Type = Integer32
_RuckusDot1xRxLengthErrorFrames_Object = MibTableColumn
ruckusDot1xRxLengthErrorFrames = _RuckusDot1xRxLengthErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 10),
    _RuckusDot1xRxLengthErrorFrames_Type()
)
ruckusDot1xRxLengthErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xRxLengthErrorFrames.setStatus("current")
_RuckusDot1xRxEAPLastFrameVersion_Type = Unsigned32
_RuckusDot1xRxEAPLastFrameVersion_Object = MibTableColumn
ruckusDot1xRxEAPLastFrameVersion = _RuckusDot1xRxEAPLastFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 11),
    _RuckusDot1xRxEAPLastFrameVersion_Type()
)
ruckusDot1xRxEAPLastFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xRxEAPLastFrameVersion.setStatus("current")
_RuckusDot1xRxEAPLastFrameSource_Type = MacAddress
_RuckusDot1xRxEAPLastFrameSource_Object = MibTableColumn
ruckusDot1xRxEAPLastFrameSource = _RuckusDot1xRxEAPLastFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 1, 8, 2, 1, 12),
    _RuckusDot1xRxEAPLastFrameSource_Type()
)
ruckusDot1xRxEAPLastFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDot1xRxEAPLastFrameSource.setStatus("current")
_RuckusAuthConformance_ObjectIdentity = ObjectIdentity
ruckusAuthConformance = _RuckusAuthConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2)
)
_RuckusAuthMIBCompliances_ObjectIdentity = ObjectIdentity
ruckusAuthMIBCompliances = _RuckusAuthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 1)
)
_RuckusAuthMIBGroups_ObjectIdentity = ObjectIdentity
ruckusAuthMIBGroups = _RuckusAuthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2)
)

# Managed Objects groups

ruckusAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2, 1)
)
ruckusAuthConfigGroup.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusAuthDefaultVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthVoiceVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthCriticalVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthRestrictVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthMode"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthMethods"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthMaxSessions"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthFailAction"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthTimeoutAction"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthReauthEnable"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthReauthPeriod"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthReauthTimeout"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthIdleTimeout"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthDeniedTimeout"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthAging"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthEnable"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthDefaultV4IngressAcl"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthDefaultV4EgressAcl"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthDefaultV6IngressAcl"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthDefaultV6EgressAcl"))
)
if mibBuilder.loadTexts:
    ruckusAuthConfigGroup.setStatus("current")

ruckusDot1xAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2, 2)
)
ruckusDot1xAuthConfigGroup.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusDot1xQuietPeriod"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xTxPeriod"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xSuppTimeout"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xMaxReq"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xMaxReauthReq"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xGuestVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xMacAuthOverride"))
)
if mibBuilder.loadTexts:
    ruckusDot1xAuthConfigGroup.setStatus("current")

ruckusMacAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2, 3)
)
ruckusMacAuthConfigGroup.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusMacAuthPasswordFormat"),
        ("RUCKUS-AUTH-MIB", "ruckusMacAuthPasswordOverride"),
        ("RUCKUS-AUTH-MIB", "ruckusMacAuthDot1xOverride"),
        ("RUCKUS-AUTH-MIB", "ruckusMacAuthDot1xEnable"))
)
if mibBuilder.loadTexts:
    ruckusMacAuthConfigGroup.setStatus("current")

ruckusAuthPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2, 4)
)
ruckusAuthPortConfigGroup.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusAuthPortEnable"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortDot1xControl"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortDefaultVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortVoiceVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortCriticalVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortRestrictVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortMode"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortMethods"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortMaxSessions"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortFailAction"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortTimeoutAction"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortReauthTimeout"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortAging"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortAllowTagged"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortSourceGuard"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortDosAttacks"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortDosAttackLimit"))
)
if mibBuilder.loadTexts:
    ruckusAuthPortConfigGroup.setStatus("current")

ruckusAuthFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2, 5)
)
ruckusAuthFilterConfigGroup.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusAuthFilterMac"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthFilterMask"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthFilterVlan"))
)
if mibBuilder.loadTexts:
    ruckusAuthFilterConfigGroup.setStatus("current")

ruckusAuthSessionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2, 6)
)
ruckusAuthSessionsGroup.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusAuthSessionVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionTaggedVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionUserName"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionDeviceType"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionStatus"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionDot1xStatus"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionMethod"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionMode"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionAgingType"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionAge"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionTimeout"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionIdleTimeout"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionTime"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionV4IngressAcl"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionV4EgressAcl"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionV6IngressAcl"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionV6EgressAcl"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionTxOctets"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionRxOctets"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionTxPkts"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionRxPkts"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionFailureReason"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionFlags"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionAddrType"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionAddr"))
)
if mibBuilder.loadTexts:
    ruckusAuthSessionsGroup.setStatus("current")

ruckusAuthStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2, 7)
)
ruckusAuthStatsGroup.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusDot1xSessionsAttempted"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xSessionsAccepted"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xSessionsRejected"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xSessionsInProgress"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xSessionsErrored"),
        ("RUCKUS-AUTH-MIB", "ruckusMacAuthSessionsAttempted"),
        ("RUCKUS-AUTH-MIB", "ruckusMacAuthSessionsAccepted"),
        ("RUCKUS-AUTH-MIB", "ruckusMacAuthSessionsRejected"),
        ("RUCKUS-AUTH-MIB", "ruckusMacAuthSessionsInProgress"),
        ("RUCKUS-AUTH-MIB", "ruckusMacAuthSessionsErrored"))
)
if mibBuilder.loadTexts:
    ruckusAuthStatsGroup.setStatus("current")

ruckusDot1xAuthStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2, 8)
)
ruckusDot1xAuthStatsGroup.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusDot1xTxEAPFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xTxEAPReqIdFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xTxEAPReqFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xRxEAPFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xRxEAPStartFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xRxEAPLogOffFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xRxEAPRespIdFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xRxEAPRespFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xRxEAPInvalidFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xRxLengthErrorFrames"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xRxEAPLastFrameVersion"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xRxEAPLastFrameSource"))
)
if mibBuilder.loadTexts:
    ruckusDot1xAuthStatsGroup.setStatus("current")

ruckusWebAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 2, 9)
)
ruckusWebAuthConfigGroup.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusWebAuthEnable"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthTrustPort"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthMode"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthMethod"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthMaxHosts"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthMaxAuthAttempts"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthReauthTime"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthCycleTime"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthBlockTime"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthMacAgeTime"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthPasscode"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthLocalUserDb"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthSecureLogin"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthAccounting"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthCaptiveProfile"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthRedirectName"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthDnsFilterType"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthDnsFilterAddr"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthDnsFilterPrefix"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthWhiteListType"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthWhiteListAddr"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthWhiteListPrefix"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthFilterPort"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthFilterDuration"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthFilterAction"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthCaptivePortalType"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthCaptivePortalAddr"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthCaptivePortalPort"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthCaptivePortalLoginPage"))
)
if mibBuilder.loadTexts:
    ruckusWebAuthConfigGroup.setStatus("current")


# Notification objects

ruckusAuthPortAuthorizedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 0, 1)
)
ruckusAuthPortAuthorizedNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionMac"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionVlanType"))
)
if mibBuilder.loadTexts:
    ruckusAuthPortAuthorizedNotif.setStatus(
        "current"
    )

ruckusAuthPortUnauthorizedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 0, 2)
)
ruckusAuthPortUnauthorizedNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionMac"))
)
if mibBuilder.loadTexts:
    ruckusAuthPortUnauthorizedNotif.setStatus(
        "current"
    )

ruckusAuthMacAuthorizedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 0, 3)
)
ruckusAuthMacAuthorizedNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionMac"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionVlan"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionVlanType"))
)
if mibBuilder.loadTexts:
    ruckusAuthMacAuthorizedNotif.setStatus(
        "current"
    )

ruckusAuthMacUnauthorizedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 0, 4)
)
ruckusAuthMacUnauthorizedNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionMac"))
)
if mibBuilder.loadTexts:
    ruckusAuthMacUnauthorizedNotif.setStatus(
        "current"
    )

ruckusAuthAclFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 0, 5)
)
ruckusAuthAclFailNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionMac"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionMethod"))
)
if mibBuilder.loadTexts:
    ruckusAuthAclFailNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruckusAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 44, 2, 1, 1)
)
ruckusAuthCompliance.setObjects(
      *(("RUCKUS-AUTH-MIB", "ruckusAuthConfigGroup"),
        ("RUCKUS-AUTH-MIB", "ruckusDot1xAuthConfigGroup"),
        ("RUCKUS-AUTH-MIB", "ruckusMacAuthConfigGroup"),
        ("RUCKUS-AUTH-MIB", "ruckusWebAuthConfigGroup"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthPortConfigGroup"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthFilterConfigGroup"),
        ("RUCKUS-AUTH-MIB", "ruckusAuthSessionsGroup"))
)
if mibBuilder.loadTexts:
    ruckusAuthCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-AUTH-MIB",
    **{"VlanId": VlanId,
       "Dot1xAuthState": Dot1xAuthState,
       "RuckusAuthMode": RuckusAuthMode,
       "RuckusAuthOrder": RuckusAuthOrder,
       "RuckusAuthFailAction": RuckusAuthFailAction,
       "RuckusAuthTimeoutAction": RuckusAuthTimeoutAction,
       "RuckusAuthAging": RuckusAuthAging,
       "ruckusAuthMIB": ruckusAuthMIB,
       "ruckusAuthNotification": ruckusAuthNotification,
       "ruckusAuthPortAuthorizedNotif": ruckusAuthPortAuthorizedNotif,
       "ruckusAuthPortUnauthorizedNotif": ruckusAuthPortUnauthorizedNotif,
       "ruckusAuthMacAuthorizedNotif": ruckusAuthMacAuthorizedNotif,
       "ruckusAuthMacUnauthorizedNotif": ruckusAuthMacUnauthorizedNotif,
       "ruckusAuthAclFailNotif": ruckusAuthAclFailNotif,
       "ruckusAuthObjects": ruckusAuthObjects,
       "ruckusAuthConfig": ruckusAuthConfig,
       "ruckusAuthDefaultVlan": ruckusAuthDefaultVlan,
       "ruckusAuthVoiceVlan": ruckusAuthVoiceVlan,
       "ruckusAuthCriticalVlan": ruckusAuthCriticalVlan,
       "ruckusAuthRestrictVlan": ruckusAuthRestrictVlan,
       "ruckusAuthEnable": ruckusAuthEnable,
       "ruckusAuthMode": ruckusAuthMode,
       "ruckusAuthMethods": ruckusAuthMethods,
       "ruckusAuthMaxSessions": ruckusAuthMaxSessions,
       "ruckusAuthFailAction": ruckusAuthFailAction,
       "ruckusAuthTimeoutAction": ruckusAuthTimeoutAction,
       "ruckusAuthReauthEnable": ruckusAuthReauthEnable,
       "ruckusAuthReauthPeriod": ruckusAuthReauthPeriod,
       "ruckusAuthReauthTimeout": ruckusAuthReauthTimeout,
       "ruckusAuthIdleTimeout": ruckusAuthIdleTimeout,
       "ruckusAuthDeniedTimeout": ruckusAuthDeniedTimeout,
       "ruckusAuthAging": ruckusAuthAging,
       "ruckusAuthDefaultV4IngressAcl": ruckusAuthDefaultV4IngressAcl,
       "ruckusAuthDefaultV4EgressAcl": ruckusAuthDefaultV4EgressAcl,
       "ruckusAuthDefaultV6IngressAcl": ruckusAuthDefaultV6IngressAcl,
       "ruckusAuthDefaultV6EgressAcl": ruckusAuthDefaultV6EgressAcl,
       "ruckusDot1xAuthConfig": ruckusDot1xAuthConfig,
       "ruckusDot1xQuietPeriod": ruckusDot1xQuietPeriod,
       "ruckusDot1xTxPeriod": ruckusDot1xTxPeriod,
       "ruckusDot1xSuppTimeout": ruckusDot1xSuppTimeout,
       "ruckusDot1xMaxReq": ruckusDot1xMaxReq,
       "ruckusDot1xMaxReauthReq": ruckusDot1xMaxReauthReq,
       "ruckusDot1xGuestVlan": ruckusDot1xGuestVlan,
       "ruckusDot1xMacAuthOverride": ruckusDot1xMacAuthOverride,
       "ruckusMacAuthConfig": ruckusMacAuthConfig,
       "ruckusMacAuthPasswordFormat": ruckusMacAuthPasswordFormat,
       "ruckusMacAuthPasswordOverride": ruckusMacAuthPasswordOverride,
       "ruckusMacAuthDot1xOverride": ruckusMacAuthDot1xOverride,
       "ruckusMacAuthDot1xEnable": ruckusMacAuthDot1xEnable,
       "ruckusWebAuthConfig": ruckusWebAuthConfig,
       "ruckusWebAuthTable": ruckusWebAuthTable,
       "ruckusWebAuthEntry": ruckusWebAuthEntry,
       "ruckusWebAuthVlan": ruckusWebAuthVlan,
       "ruckusWebAuthEnable": ruckusWebAuthEnable,
       "ruckusWebAuthMode": ruckusWebAuthMode,
       "ruckusWebAuthMethod": ruckusWebAuthMethod,
       "ruckusWebAuthMaxHosts": ruckusWebAuthMaxHosts,
       "ruckusWebAuthMaxAuthAttempts": ruckusWebAuthMaxAuthAttempts,
       "ruckusWebAuthReauthTime": ruckusWebAuthReauthTime,
       "ruckusWebAuthCycleTime": ruckusWebAuthCycleTime,
       "ruckusWebAuthBlockTime": ruckusWebAuthBlockTime,
       "ruckusWebAuthMacAgeTime": ruckusWebAuthMacAgeTime,
       "ruckusWebAuthPasscode": ruckusWebAuthPasscode,
       "ruckusWebAuthLocalUserDb": ruckusWebAuthLocalUserDb,
       "ruckusWebAuthSecureLogin": ruckusWebAuthSecureLogin,
       "ruckusWebAuthAccounting": ruckusWebAuthAccounting,
       "ruckusWebAuthCaptiveProfile": ruckusWebAuthCaptiveProfile,
       "ruckusWebAuthRedirectName": ruckusWebAuthRedirectName,
       "ruckusWebAuthWebpageRemoveUserId": ruckusWebAuthWebpageRemoveUserId,
       "ruckusWebAuthWebpageUsernameLabel": ruckusWebAuthWebpageUsernameLabel,
       "ruckusWebAuthWebpagePasswordLabel": ruckusWebAuthWebpagePasswordLabel,
       "ruckusWebAuthUpLinkPort": ruckusWebAuthUpLinkPort,
       "ruckusWebAuthWebpageTop": ruckusWebAuthWebpageTop,
       "ruckusWebAuthWebpageBottom": ruckusWebAuthWebpageBottom,
       "ruckusWebAuthWebpageTitle": ruckusWebAuthWebpageTitle,
       "ruckusWebAuthWebpageLoginButton": ruckusWebAuthWebpageLoginButton,
       "ruckusWebAuthTrustPortTable": ruckusWebAuthTrustPortTable,
       "ruckusWebAuthTrustPortEntry": ruckusWebAuthTrustPortEntry,
       "ruckusWebAuthTrustPort": ruckusWebAuthTrustPort,
       "ruckusWebAuthDnsFilterTable": ruckusWebAuthDnsFilterTable,
       "ruckusWebAuthDnsFilterEntry": ruckusWebAuthDnsFilterEntry,
       "ruckusWebAuthDnsFilterId": ruckusWebAuthDnsFilterId,
       "ruckusWebAuthDnsFilterType": ruckusWebAuthDnsFilterType,
       "ruckusWebAuthDnsFilterAddr": ruckusWebAuthDnsFilterAddr,
       "ruckusWebAuthDnsFilterPrefix": ruckusWebAuthDnsFilterPrefix,
       "ruckusWebAuthWhiteListTable": ruckusWebAuthWhiteListTable,
       "ruckusWebAuthWhiteListEntry": ruckusWebAuthWhiteListEntry,
       "ruckusWebAuthWhiteListId": ruckusWebAuthWhiteListId,
       "ruckusWebAuthWhiteListType": ruckusWebAuthWhiteListType,
       "ruckusWebAuthWhiteListAddr": ruckusWebAuthWhiteListAddr,
       "ruckusWebAuthWhiteListPrefix": ruckusWebAuthWhiteListPrefix,
       "ruckusWebAuthFilterTable": ruckusWebAuthFilterTable,
       "ruckusWebAuthFilterEntry": ruckusWebAuthFilterEntry,
       "ruckusWebAuthFilterMac": ruckusWebAuthFilterMac,
       "ruckusWebAuthFilterPort": ruckusWebAuthFilterPort,
       "ruckusWebAuthFilterDuration": ruckusWebAuthFilterDuration,
       "ruckusWebAuthFilterAction": ruckusWebAuthFilterAction,
       "ruckusWebAuthCaptivePortalTable": ruckusWebAuthCaptivePortalTable,
       "ruckusWebAuthCaptivePortalEntry": ruckusWebAuthCaptivePortalEntry,
       "ruckusWebAuthCaptivePortalName": ruckusWebAuthCaptivePortalName,
       "ruckusWebAuthCaptivePortalType": ruckusWebAuthCaptivePortalType,
       "ruckusWebAuthCaptivePortalAddr": ruckusWebAuthCaptivePortalAddr,
       "ruckusWebAuthCaptivePortalPort": ruckusWebAuthCaptivePortalPort,
       "ruckusWebAuthCaptivePortalLoginPage": ruckusWebAuthCaptivePortalLoginPage,
       "ruckusAuthPortConfig": ruckusAuthPortConfig,
       "ruckusAuthPortTable": ruckusAuthPortTable,
       "ruckusAuthPortEntry": ruckusAuthPortEntry,
       "ruckusAuthPortEnable": ruckusAuthPortEnable,
       "ruckusAuthPortDot1xControl": ruckusAuthPortDot1xControl,
       "ruckusAuthPortDefaultVlan": ruckusAuthPortDefaultVlan,
       "ruckusAuthPortVoiceVlan": ruckusAuthPortVoiceVlan,
       "ruckusAuthPortCriticalVlan": ruckusAuthPortCriticalVlan,
       "ruckusAuthPortRestrictVlan": ruckusAuthPortRestrictVlan,
       "ruckusAuthPortMode": ruckusAuthPortMode,
       "ruckusAuthPortMethods": ruckusAuthPortMethods,
       "ruckusAuthPortMaxSessions": ruckusAuthPortMaxSessions,
       "ruckusAuthPortFailAction": ruckusAuthPortFailAction,
       "ruckusAuthPortTimeoutAction": ruckusAuthPortTimeoutAction,
       "ruckusAuthPortReauthTimeout": ruckusAuthPortReauthTimeout,
       "ruckusAuthPortAging": ruckusAuthPortAging,
       "ruckusAuthPortAllowTagged": ruckusAuthPortAllowTagged,
       "ruckusAuthPortSourceGuard": ruckusAuthPortSourceGuard,
       "ruckusAuthPortDosAttacks": ruckusAuthPortDosAttacks,
       "ruckusAuthPortDosAttackLimit": ruckusAuthPortDosAttackLimit,
       "ruckusAuthFilterConfig": ruckusAuthFilterConfig,
       "ruckusAuthFilterTable": ruckusAuthFilterTable,
       "ruckusAuthFilterEntry": ruckusAuthFilterEntry,
       "ruckusAuthFilterId": ruckusAuthFilterId,
       "ruckusAuthFilterMac": ruckusAuthFilterMac,
       "ruckusAuthFilterMask": ruckusAuthFilterMask,
       "ruckusAuthFilterVlan": ruckusAuthFilterVlan,
       "ruckusAuthFilterAction": ruckusAuthFilterAction,
       "ruckusAuthSessions": ruckusAuthSessions,
       "ruckusAuthSessionTable": ruckusAuthSessionTable,
       "ruckusAuthSessionEntry": ruckusAuthSessionEntry,
       "ruckusAuthSessionMac": ruckusAuthSessionMac,
       "ruckusAuthSessionVlan": ruckusAuthSessionVlan,
       "ruckusAuthSessionVlanType": ruckusAuthSessionVlanType,
       "ruckusAuthSessionTaggedVlan": ruckusAuthSessionTaggedVlan,
       "ruckusAuthSessionUserName": ruckusAuthSessionUserName,
       "ruckusAuthSessionDeviceType": ruckusAuthSessionDeviceType,
       "ruckusAuthSessionMethod": ruckusAuthSessionMethod,
       "ruckusAuthSessionMode": ruckusAuthSessionMode,
       "ruckusAuthSessionStatus": ruckusAuthSessionStatus,
       "ruckusAuthSessionDot1xStatus": ruckusAuthSessionDot1xStatus,
       "ruckusAuthSessionAgingType": ruckusAuthSessionAgingType,
       "ruckusAuthSessionAge": ruckusAuthSessionAge,
       "ruckusAuthSessionTimeout": ruckusAuthSessionTimeout,
       "ruckusAuthSessionIdleTimeout": ruckusAuthSessionIdleTimeout,
       "ruckusAuthSessionTime": ruckusAuthSessionTime,
       "ruckusAuthSessionV4IngressAcl": ruckusAuthSessionV4IngressAcl,
       "ruckusAuthSessionV4EgressAcl": ruckusAuthSessionV4EgressAcl,
       "ruckusAuthSessionV6IngressAcl": ruckusAuthSessionV6IngressAcl,
       "ruckusAuthSessionV6EgressAcl": ruckusAuthSessionV6EgressAcl,
       "ruckusAuthSessionTxOctets": ruckusAuthSessionTxOctets,
       "ruckusAuthSessionRxOctets": ruckusAuthSessionRxOctets,
       "ruckusAuthSessionTxPkts": ruckusAuthSessionTxPkts,
       "ruckusAuthSessionRxPkts": ruckusAuthSessionRxPkts,
       "ruckusAuthSessionFailureReason": ruckusAuthSessionFailureReason,
       "ruckusAuthSessionFlags": ruckusAuthSessionFlags,
       "ruckusAuthSessionAddrTable": ruckusAuthSessionAddrTable,
       "ruckusAuthSessionAddrEntry": ruckusAuthSessionAddrEntry,
       "ruckusAuthSessionAddrId": ruckusAuthSessionAddrId,
       "ruckusAuthSessionAddrType": ruckusAuthSessionAddrType,
       "ruckusAuthSessionAddr": ruckusAuthSessionAddr,
       "ruckusAuthStatistics": ruckusAuthStatistics,
       "ruckusAuthStatsTable": ruckusAuthStatsTable,
       "ruckusAuthStatsEntry": ruckusAuthStatsEntry,
       "ruckusDot1xSessionsAttempted": ruckusDot1xSessionsAttempted,
       "ruckusDot1xSessionsAccepted": ruckusDot1xSessionsAccepted,
       "ruckusDot1xSessionsRejected": ruckusDot1xSessionsRejected,
       "ruckusDot1xSessionsInProgress": ruckusDot1xSessionsInProgress,
       "ruckusDot1xSessionsErrored": ruckusDot1xSessionsErrored,
       "ruckusMacAuthSessionsAttempted": ruckusMacAuthSessionsAttempted,
       "ruckusMacAuthSessionsAccepted": ruckusMacAuthSessionsAccepted,
       "ruckusMacAuthSessionsRejected": ruckusMacAuthSessionsRejected,
       "ruckusMacAuthSessionsInProgress": ruckusMacAuthSessionsInProgress,
       "ruckusMacAuthSessionsErrored": ruckusMacAuthSessionsErrored,
       "ruckusDot1xAuthStatsTable": ruckusDot1xAuthStatsTable,
       "ruckusDot1xAuthStatsEntry": ruckusDot1xAuthStatsEntry,
       "ruckusDot1xTxEAPFrames": ruckusDot1xTxEAPFrames,
       "ruckusDot1xTxEAPReqIdFrames": ruckusDot1xTxEAPReqIdFrames,
       "ruckusDot1xTxEAPReqFrames": ruckusDot1xTxEAPReqFrames,
       "ruckusDot1xRxEAPFrames": ruckusDot1xRxEAPFrames,
       "ruckusDot1xRxEAPStartFrames": ruckusDot1xRxEAPStartFrames,
       "ruckusDot1xRxEAPLogOffFrames": ruckusDot1xRxEAPLogOffFrames,
       "ruckusDot1xRxEAPRespIdFrames": ruckusDot1xRxEAPRespIdFrames,
       "ruckusDot1xRxEAPRespFrames": ruckusDot1xRxEAPRespFrames,
       "ruckusDot1xRxEAPInvalidFrames": ruckusDot1xRxEAPInvalidFrames,
       "ruckusDot1xRxLengthErrorFrames": ruckusDot1xRxLengthErrorFrames,
       "ruckusDot1xRxEAPLastFrameVersion": ruckusDot1xRxEAPLastFrameVersion,
       "ruckusDot1xRxEAPLastFrameSource": ruckusDot1xRxEAPLastFrameSource,
       "ruckusAuthConformance": ruckusAuthConformance,
       "ruckusAuthMIBCompliances": ruckusAuthMIBCompliances,
       "ruckusAuthCompliance": ruckusAuthCompliance,
       "ruckusAuthMIBGroups": ruckusAuthMIBGroups,
       "ruckusAuthConfigGroup": ruckusAuthConfigGroup,
       "ruckusDot1xAuthConfigGroup": ruckusDot1xAuthConfigGroup,
       "ruckusMacAuthConfigGroup": ruckusMacAuthConfigGroup,
       "ruckusAuthPortConfigGroup": ruckusAuthPortConfigGroup,
       "ruckusAuthFilterConfigGroup": ruckusAuthFilterConfigGroup,
       "ruckusAuthSessionsGroup": ruckusAuthSessionsGroup,
       "ruckusAuthStatsGroup": ruckusAuthStatsGroup,
       "ruckusDot1xAuthStatsGroup": ruckusDot1xAuthStatsGroup,
       "ruckusWebAuthConfigGroup": ruckusWebAuthConfigGroup}
)
