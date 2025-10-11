# SNMP MIB module (ENTERASYS-MULTI-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-MULTI-AUTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:12 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(StationAddress,
 StationAddressType) = mibBuilder.importSymbols(
    "ENTERASYS-UPN-TC-MIB",
    "StationAddress",
    "StationAddressType")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

etsysMultiAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46)
)
if mibBuilder.loadTexts:
    etsysMultiAuthMIB.setRevisions(
        ("2013-08-08 15:15",
         "2013-01-07 14:38",
         "2012-09-12 15:37",
         "2012-05-31 18:33",
         "2012-05-09 11:03",
         "2008-02-05 18:40",
         "2006-03-23 13:32",
         "2006-02-03 19:15",
         "2005-04-06 18:10",
         "2004-08-30 13:43",
         "2004-07-20 19:43",
         "2004-03-10 13:56")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysMultiAuthTypes(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021x", 1),
          ("pwa", 2),
          ("macAuth", 3),
          ("cep", 4),
          ("radiusSnooping", 5),
          ("autoTracking", 6),
          ("quarantineAgent", 7))
    )



class EtsysMultiAuthTypePrecedence(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class EtsysMultiAuthStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("authSuccess", 1),
          ("authFailed", 2),
          ("authInProgress", 3),
          ("authServerTimeout", 4),
          ("authTerminated", 5))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysMultiAuthObjects_ObjectIdentity = ObjectIdentity
etsysMultiAuthObjects = _EtsysMultiAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1)
)
_EtsysMultiAuthNotification_ObjectIdentity = ObjectIdentity
etsysMultiAuthNotification = _EtsysMultiAuthNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0)
)
_EtsysMultiAuthSystem_ObjectIdentity = ObjectIdentity
etsysMultiAuthSystem = _EtsysMultiAuthSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1)
)


class _EtsysMultiAuthSystemSupportedTypes_Type(Bits):
    """Custom type etsysMultiAuthSystemSupportedTypes based on Bits"""
    namedValues = NamedValues(
        *(("ieee8021x", 0),
          ("pwa", 1),
          ("macAuth", 2),
          ("cep", 3),
          ("radiusSnooping", 4),
          ("autoTracking", 5),
          ("quarantineAgent", 6))
    )

_EtsysMultiAuthSystemSupportedTypes_Type.__name__ = "Bits"
_EtsysMultiAuthSystemSupportedTypes_Object = MibScalar
etsysMultiAuthSystemSupportedTypes = _EtsysMultiAuthSystemSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 1),
    _EtsysMultiAuthSystemSupportedTypes_Type()
)
etsysMultiAuthSystemSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemSupportedTypes.setStatus("current")
_EtsysMultiAuthSystemMaxNumUsers_Type = Unsigned32
_EtsysMultiAuthSystemMaxNumUsers_Object = MibScalar
etsysMultiAuthSystemMaxNumUsers = _EtsysMultiAuthSystemMaxNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 2),
    _EtsysMultiAuthSystemMaxNumUsers_Type()
)
etsysMultiAuthSystemMaxNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemMaxNumUsers.setStatus("current")
_EtsysMultiAuthSystemCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthSystemCurrentNumUsers_Object = MibScalar
etsysMultiAuthSystemCurrentNumUsers = _EtsysMultiAuthSystemCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 3),
    _EtsysMultiAuthSystemCurrentNumUsers_Type()
)
etsysMultiAuthSystemCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemCurrentNumUsers.setStatus("current")


class _EtsysMultiAuthSystemMode_Type(Integer32):
    """Custom type etsysMultiAuthSystemMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strictIeee8021x", 1),
          ("etsysMultiAuth", 2))
    )


_EtsysMultiAuthSystemMode_Type.__name__ = "Integer32"
_EtsysMultiAuthSystemMode_Object = MibScalar
etsysMultiAuthSystemMode = _EtsysMultiAuthSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 4),
    _EtsysMultiAuthSystemMode_Type()
)
etsysMultiAuthSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemMode.setStatus("current")


class _EtsysMultiAuthSystemDefaultPrecedence_Type(EtsysMultiAuthTypePrecedence):
    """Custom type etsysMultiAuthSystemDefaultPrecedence based on EtsysMultiAuthTypePrecedence"""
    defaultHexValue = "07010203040506"


_EtsysMultiAuthSystemDefaultPrecedence_Type.__name__ = "EtsysMultiAuthTypePrecedence"
_EtsysMultiAuthSystemDefaultPrecedence_Object = MibScalar
etsysMultiAuthSystemDefaultPrecedence = _EtsysMultiAuthSystemDefaultPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 5),
    _EtsysMultiAuthSystemDefaultPrecedence_Type()
)
etsysMultiAuthSystemDefaultPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemDefaultPrecedence.setStatus("current")


class _EtsysMultiAuthSystemAdminPrecedence_Type(EtsysMultiAuthTypePrecedence):
    """Custom type etsysMultiAuthSystemAdminPrecedence based on EtsysMultiAuthTypePrecedence"""
    defaultHexValue = ""


_EtsysMultiAuthSystemAdminPrecedence_Type.__name__ = "EtsysMultiAuthTypePrecedence"
_EtsysMultiAuthSystemAdminPrecedence_Object = MibScalar
etsysMultiAuthSystemAdminPrecedence = _EtsysMultiAuthSystemAdminPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 6),
    _EtsysMultiAuthSystemAdminPrecedence_Type()
)
etsysMultiAuthSystemAdminPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemAdminPrecedence.setStatus("current")
_EtsysMultiAuthSystemOperPrecedence_Type = EtsysMultiAuthTypePrecedence
_EtsysMultiAuthSystemOperPrecedence_Object = MibScalar
etsysMultiAuthSystemOperPrecedence = _EtsysMultiAuthSystemOperPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 7),
    _EtsysMultiAuthSystemOperPrecedence_Type()
)
etsysMultiAuthSystemOperPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemOperPrecedence.setStatus("current")
_EtsysMultiAuthTypePropertiesTable_Object = MibTable
etsysMultiAuthTypePropertiesTable = _EtsysMultiAuthTypePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8)
)
if mibBuilder.loadTexts:
    etsysMultiAuthTypePropertiesTable.setStatus("current")
_EtsysMultiAuthTypePropertiesEntry_Object = MibTableRow
etsysMultiAuthTypePropertiesEntry = _EtsysMultiAuthTypePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1)
)
etsysMultiAuthTypePropertiesEntry.setIndexNames(
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthType"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthTypePropertiesEntry.setStatus("current")
_EtsysMultiAuthType_Type = EtsysMultiAuthTypes
_EtsysMultiAuthType_Object = MibTableColumn
etsysMultiAuthType = _EtsysMultiAuthType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1, 1),
    _EtsysMultiAuthType_Type()
)
etsysMultiAuthType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMultiAuthType.setStatus("current")


class _EtsysMultiAuthSessionTimeout_Type(Unsigned32):
    """Custom type etsysMultiAuthSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 172800),
    )


_EtsysMultiAuthSessionTimeout_Type.__name__ = "Unsigned32"
_EtsysMultiAuthSessionTimeout_Object = MibTableColumn
etsysMultiAuthSessionTimeout = _EtsysMultiAuthSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1, 2),
    _EtsysMultiAuthSessionTimeout_Type()
)
etsysMultiAuthSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionTimeout.setUnits("seconds")


class _EtsysMultiAuthIdleTimeout_Type(Unsigned32):
    """Custom type etsysMultiAuthIdleTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 172800),
    )


_EtsysMultiAuthIdleTimeout_Type.__name__ = "Unsigned32"
_EtsysMultiAuthIdleTimeout_Object = MibTableColumn
etsysMultiAuthIdleTimeout = _EtsysMultiAuthIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1, 3),
    _EtsysMultiAuthIdleTimeout_Type()
)
etsysMultiAuthIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthIdleTimeout.setUnits("seconds")
_EtsysMultiAuthCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthCurrentNumUsers_Object = MibTableColumn
etsysMultiAuthCurrentNumUsers = _EtsysMultiAuthCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1, 4),
    _EtsysMultiAuthCurrentNumUsers_Type()
)
etsysMultiAuthCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthCurrentNumUsers.setStatus("current")


class _EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Type(EnabledStatus):
    """Custom type etsysMultiAuthSystemMaxNumUsersReachedTrapEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Type.__name__ = "EnabledStatus"
_EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Object = MibScalar
etsysMultiAuthSystemMaxNumUsersReachedTrapEnable = _EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 9),
    _EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Type()
)
etsysMultiAuthSystemMaxNumUsersReachedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemMaxNumUsersReachedTrapEnable.setStatus("current")


class _EtsysMultiAuthSessionsUniquePerPort_Type(TruthValue):
    """Custom type etsysMultiAuthSessionsUniquePerPort based on TruthValue"""
    defaultValue = 2


_EtsysMultiAuthSessionsUniquePerPort_Type.__name__ = "TruthValue"
_EtsysMultiAuthSessionsUniquePerPort_Object = MibScalar
etsysMultiAuthSessionsUniquePerPort = _EtsysMultiAuthSessionsUniquePerPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 10),
    _EtsysMultiAuthSessionsUniquePerPort_Type()
)
etsysMultiAuthSessionsUniquePerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionsUniquePerPort.setStatus("current")
_EtsysMultiAuthSessionsUniquePerPortOperStatus_Type = TruthValue
_EtsysMultiAuthSessionsUniquePerPortOperStatus_Object = MibScalar
etsysMultiAuthSessionsUniquePerPortOperStatus = _EtsysMultiAuthSessionsUniquePerPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 11),
    _EtsysMultiAuthSessionsUniquePerPortOperStatus_Type()
)
etsysMultiAuthSessionsUniquePerPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionsUniquePerPortOperStatus.setStatus("current")


class _EtsysMultiAuthSystemReAuthenticationTimeoutAction_Type(Integer32):
    """Custom type etsysMultiAuthSystemReAuthenticationTimeoutAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("terminate", 1),
          ("none", 2))
    )


_EtsysMultiAuthSystemReAuthenticationTimeoutAction_Type.__name__ = "Integer32"
_EtsysMultiAuthSystemReAuthenticationTimeoutAction_Object = MibScalar
etsysMultiAuthSystemReAuthenticationTimeoutAction = _EtsysMultiAuthSystemReAuthenticationTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 12),
    _EtsysMultiAuthSystemReAuthenticationTimeoutAction_Type()
)
etsysMultiAuthSystemReAuthenticationTimeoutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemReAuthenticationTimeoutAction.setStatus("current")
_EtsysMultiAuthPort_ObjectIdentity = ObjectIdentity
etsysMultiAuthPort = _EtsysMultiAuthPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2)
)
_EtsysMultiAuthPortTable_Object = MibTable
etsysMultiAuthPortTable = _EtsysMultiAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortTable.setStatus("current")
_EtsysMultiAuthPortEntry_Object = MibTableRow
etsysMultiAuthPortEntry = _EtsysMultiAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1)
)
etsysMultiAuthPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortEntry.setStatus("current")


class _EtsysMultiAuthPortMode_Type(Integer32):
    """Custom type etsysMultiAuthPortMode based on Integer32"""
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
          ("forceAuthorized", 2),
          ("authOptional", 3),
          ("authRequired", 4))
    )


_EtsysMultiAuthPortMode_Type.__name__ = "Integer32"
_EtsysMultiAuthPortMode_Object = MibTableColumn
etsysMultiAuthPortMode = _EtsysMultiAuthPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 1),
    _EtsysMultiAuthPortMode_Type()
)
etsysMultiAuthPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthPortMode.setStatus("current")
_EtsysMultiAuthPortMaxNumUsers_Type = Unsigned32
_EtsysMultiAuthPortMaxNumUsers_Object = MibTableColumn
etsysMultiAuthPortMaxNumUsers = _EtsysMultiAuthPortMaxNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 2),
    _EtsysMultiAuthPortMaxNumUsers_Type()
)
etsysMultiAuthPortMaxNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthPortMaxNumUsers.setStatus("current")
_EtsysMultiAuthPortNumUsersAllowed_Type = Unsigned32
_EtsysMultiAuthPortNumUsersAllowed_Object = MibTableColumn
etsysMultiAuthPortNumUsersAllowed = _EtsysMultiAuthPortNumUsersAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 3),
    _EtsysMultiAuthPortNumUsersAllowed_Type()
)
etsysMultiAuthPortNumUsersAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthPortNumUsersAllowed.setStatus("current")
_EtsysMultiAuthPortCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthPortCurrentNumUsers_Object = MibTableColumn
etsysMultiAuthPortCurrentNumUsers = _EtsysMultiAuthPortCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 4),
    _EtsysMultiAuthPortCurrentNumUsers_Type()
)
etsysMultiAuthPortCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthPortCurrentNumUsers.setStatus("current")


class _EtsysMultiAuthPortClearUsers_Type(TruthValue):
    """Custom type etsysMultiAuthPortClearUsers based on TruthValue"""
    defaultValue = 2


_EtsysMultiAuthPortClearUsers_Type.__name__ = "TruthValue"
_EtsysMultiAuthPortClearUsers_Object = MibTableColumn
etsysMultiAuthPortClearUsers = _EtsysMultiAuthPortClearUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 5),
    _EtsysMultiAuthPortClearUsers_Type()
)
etsysMultiAuthPortClearUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthPortClearUsers.setStatus("current")


class _EtsysMultiAuthPortTrapEnable_Type(Bits):
    """Custom type etsysMultiAuthPortTrapEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("authSuccessTrap", 0),
          ("authFailedTrap", 1),
          ("authTerminatedTrap", 2),
          ("maxNumUsersReachedTrap", 3))
    )

_EtsysMultiAuthPortTrapEnable_Type.__name__ = "Bits"
_EtsysMultiAuthPortTrapEnable_Object = MibTableColumn
etsysMultiAuthPortTrapEnable = _EtsysMultiAuthPortTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 6),
    _EtsysMultiAuthPortTrapEnable_Type()
)
etsysMultiAuthPortTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthPortTrapEnable.setStatus("current")
_EtsysMultiAuthPortTypeTable_Object = MibTable
etsysMultiAuthPortTypeTable = _EtsysMultiAuthPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortTypeTable.setStatus("current")
_EtsysMultiAuthPortTypeEntry_Object = MibTableRow
etsysMultiAuthPortTypeEntry = _EtsysMultiAuthPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 2, 1)
)
etsysMultiAuthPortTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthType"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortTypeEntry.setStatus("current")
_EtsysMultiAuthPortTypeCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthPortTypeCurrentNumUsers_Object = MibTableColumn
etsysMultiAuthPortTypeCurrentNumUsers = _EtsysMultiAuthPortTypeCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 2, 1, 1),
    _EtsysMultiAuthPortTypeCurrentNumUsers_Type()
)
etsysMultiAuthPortTypeCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthPortTypeCurrentNumUsers.setStatus("current")
_EtsysMultiAuthStation_ObjectIdentity = ObjectIdentity
etsysMultiAuthStation = _EtsysMultiAuthStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3)
)
_EtsysMultiAuthStationTable_Object = MibTable
etsysMultiAuthStationTable = _EtsysMultiAuthStationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthStationTable.setStatus("current")
_EtsysMultiAuthStationEntry_Object = MibTableRow
etsysMultiAuthStationEntry = _EtsysMultiAuthStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1, 1)
)
etsysMultiAuthStationEntry.setIndexNames(
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthStationEntry.setStatus("current")
_EtsysMultiAuthStationAddrType_Type = StationAddressType
_EtsysMultiAuthStationAddrType_Object = MibTableColumn
etsysMultiAuthStationAddrType = _EtsysMultiAuthStationAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1, 1, 1),
    _EtsysMultiAuthStationAddrType_Type()
)
etsysMultiAuthStationAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMultiAuthStationAddrType.setStatus("current")
_EtsysMultiAuthStationAddr_Type = StationAddress
_EtsysMultiAuthStationAddr_Object = MibTableColumn
etsysMultiAuthStationAddr = _EtsysMultiAuthStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1, 1, 2),
    _EtsysMultiAuthStationAddr_Type()
)
etsysMultiAuthStationAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMultiAuthStationAddr.setStatus("current")


class _EtsysMultiAuthStationClearUsers_Type(TruthValue):
    """Custom type etsysMultiAuthStationClearUsers based on TruthValue"""
    defaultValue = 2


_EtsysMultiAuthStationClearUsers_Type.__name__ = "TruthValue"
_EtsysMultiAuthStationClearUsers_Object = MibTableColumn
etsysMultiAuthStationClearUsers = _EtsysMultiAuthStationClearUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1, 1, 3),
    _EtsysMultiAuthStationClearUsers_Type()
)
etsysMultiAuthStationClearUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthStationClearUsers.setStatus("current")
_EtsysMultiAuthSession_ObjectIdentity = ObjectIdentity
etsysMultiAuthSession = _EtsysMultiAuthSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4)
)
_EtsysMultiAuthSessionStationTable_Object = MibTable
etsysMultiAuthSessionStationTable = _EtsysMultiAuthSessionStationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionStationTable.setStatus("current")
_EtsysMultiAuthSessionStationEntry_Object = MibTableRow
etsysMultiAuthSessionStationEntry = _EtsysMultiAuthSessionStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1)
)
etsysMultiAuthSessionStationEntry.setIndexNames(
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionStationEntry.setStatus("current")
_EtsysMultiAuthSessionAgentType_Type = EtsysMultiAuthTypes
_EtsysMultiAuthSessionAgentType_Object = MibTableColumn
etsysMultiAuthSessionAgentType = _EtsysMultiAuthSessionAgentType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 1),
    _EtsysMultiAuthSessionAgentType_Type()
)
etsysMultiAuthSessionAgentType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAgentType.setStatus("current")
_EtsysMultiAuthSessionStationAuthStatus_Type = EtsysMultiAuthStatus
_EtsysMultiAuthSessionStationAuthStatus_Object = MibTableColumn
etsysMultiAuthSessionStationAuthStatus = _EtsysMultiAuthSessionStationAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 2),
    _EtsysMultiAuthSessionStationAuthStatus_Type()
)
etsysMultiAuthSessionStationAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionStationAuthStatus.setStatus("current")
_EtsysMultiAuthSessionAuthAttemptTime_Type = TimeStamp
_EtsysMultiAuthSessionAuthAttemptTime_Object = MibTableColumn
etsysMultiAuthSessionAuthAttemptTime = _EtsysMultiAuthSessionAuthAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 3),
    _EtsysMultiAuthSessionAuthAttemptTime_Type()
)
etsysMultiAuthSessionAuthAttemptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAuthAttemptTime.setStatus("current")


class _EtsysMultiAuthSessionAuthServerType_Type(Integer32):
    """Custom type etsysMultiAuthSessionAuthServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("local", 2))
    )


_EtsysMultiAuthSessionAuthServerType_Type.__name__ = "Integer32"
_EtsysMultiAuthSessionAuthServerType_Object = MibTableColumn
etsysMultiAuthSessionAuthServerType = _EtsysMultiAuthSessionAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 4),
    _EtsysMultiAuthSessionAuthServerType_Type()
)
etsysMultiAuthSessionAuthServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAuthServerType.setStatus("current")
_EtsysMultiAuthSessionAuthServerAddrType_Type = InetAddressType
_EtsysMultiAuthSessionAuthServerAddrType_Object = MibTableColumn
etsysMultiAuthSessionAuthServerAddrType = _EtsysMultiAuthSessionAuthServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 5),
    _EtsysMultiAuthSessionAuthServerAddrType_Type()
)
etsysMultiAuthSessionAuthServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAuthServerAddrType.setStatus("current")
_EtsysMultiAuthSessionAuthServerAddr_Type = InetAddress
_EtsysMultiAuthSessionAuthServerAddr_Object = MibTableColumn
etsysMultiAuthSessionAuthServerAddr = _EtsysMultiAuthSessionAuthServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 6),
    _EtsysMultiAuthSessionAuthServerAddr_Type()
)
etsysMultiAuthSessionAuthServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAuthServerAddr.setStatus("current")


class _EtsysMultiAuthSessionPolicyIndex_Type(Integer32):
    """Custom type etsysMultiAuthSessionPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysMultiAuthSessionPolicyIndex_Type.__name__ = "Integer32"
_EtsysMultiAuthSessionPolicyIndex_Object = MibTableColumn
etsysMultiAuthSessionPolicyIndex = _EtsysMultiAuthSessionPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 7),
    _EtsysMultiAuthSessionPolicyIndex_Type()
)
etsysMultiAuthSessionPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionPolicyIndex.setStatus("current")
_EtsysMultiAuthSessionIsApplied_Type = TruthValue
_EtsysMultiAuthSessionIsApplied_Object = MibTableColumn
etsysMultiAuthSessionIsApplied = _EtsysMultiAuthSessionIsApplied_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 8),
    _EtsysMultiAuthSessionIsApplied_Type()
)
etsysMultiAuthSessionIsApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIsApplied.setStatus("current")


class _EtsysMultiAuthSessionTerminationTime_Type(DateAndTime):
    """Custom type etsysMultiAuthSessionTerminationTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_EtsysMultiAuthSessionTerminationTime_Type.__name__ = "DateAndTime"
_EtsysMultiAuthSessionTerminationTime_Object = MibTableColumn
etsysMultiAuthSessionTerminationTime = _EtsysMultiAuthSessionTerminationTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 9),
    _EtsysMultiAuthSessionTerminationTime_Type()
)
etsysMultiAuthSessionTerminationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionTerminationTime.setStatus("current")


class _EtsysMultiAuthSessionSessionTimeout_Type(Unsigned32):
    """Custom type etsysMultiAuthSessionSessionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 172800),
    )


_EtsysMultiAuthSessionSessionTimeout_Type.__name__ = "Unsigned32"
_EtsysMultiAuthSessionSessionTimeout_Object = MibTableColumn
etsysMultiAuthSessionSessionTimeout = _EtsysMultiAuthSessionSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 10),
    _EtsysMultiAuthSessionSessionTimeout_Type()
)
etsysMultiAuthSessionSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionSessionTimeout.setUnits("seconds")


class _EtsysMultiAuthSessionIdleTimeout_Type(Unsigned32):
    """Custom type etsysMultiAuthSessionIdleTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 172800),
    )


_EtsysMultiAuthSessionIdleTimeout_Type.__name__ = "Unsigned32"
_EtsysMultiAuthSessionIdleTimeout_Object = MibTableColumn
etsysMultiAuthSessionIdleTimeout = _EtsysMultiAuthSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 11),
    _EtsysMultiAuthSessionIdleTimeout_Type()
)
etsysMultiAuthSessionIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIdleTimeout.setUnits("seconds")
_EtsysMultiAuthSessionDuration_Type = Gauge32
_EtsysMultiAuthSessionDuration_Object = MibTableColumn
etsysMultiAuthSessionDuration = _EtsysMultiAuthSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 12),
    _EtsysMultiAuthSessionDuration_Type()
)
etsysMultiAuthSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionDuration.setUnits("seconds")
_EtsysMultiAuthSessionIdleTime_Type = Gauge32
_EtsysMultiAuthSessionIdleTime_Object = MibTableColumn
etsysMultiAuthSessionIdleTime = _EtsysMultiAuthSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 13),
    _EtsysMultiAuthSessionIdleTime_Type()
)
etsysMultiAuthSessionIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIdleTime.setUnits("seconds")


class _EtsysMultiAuthSessionVlanTunnelAttribute_Type(Integer32):
    """Custom type etsysMultiAuthSessionVlanTunnelAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_EtsysMultiAuthSessionVlanTunnelAttribute_Type.__name__ = "Integer32"
_EtsysMultiAuthSessionVlanTunnelAttribute_Object = MibTableColumn
etsysMultiAuthSessionVlanTunnelAttribute = _EtsysMultiAuthSessionVlanTunnelAttribute_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 14),
    _EtsysMultiAuthSessionVlanTunnelAttribute_Type()
)
etsysMultiAuthSessionVlanTunnelAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionVlanTunnelAttribute.setStatus("current")


class _EtsysMultiAuthSessionClear_Type(TruthValue):
    """Custom type etsysMultiAuthSessionClear based on TruthValue"""
    defaultValue = 2


_EtsysMultiAuthSessionClear_Type.__name__ = "TruthValue"
_EtsysMultiAuthSessionClear_Object = MibTableColumn
etsysMultiAuthSessionClear = _EtsysMultiAuthSessionClear_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 15),
    _EtsysMultiAuthSessionClear_Type()
)
etsysMultiAuthSessionClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionClear.setStatus("current")
_EtsysMultiAuthSessionPortTable_Object = MibTable
etsysMultiAuthSessionPortTable = _EtsysMultiAuthSessionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 2)
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionPortTable.setStatus("current")
_EtsysMultiAuthSessionPortEntry_Object = MibTableRow
etsysMultiAuthSessionPortEntry = _EtsysMultiAuthSessionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 2, 1)
)
etsysMultiAuthSessionPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionPortEntry.setStatus("current")
_EtsysMultiAuthSessionPortAuthStatus_Type = EtsysMultiAuthStatus
_EtsysMultiAuthSessionPortAuthStatus_Object = MibTableColumn
etsysMultiAuthSessionPortAuthStatus = _EtsysMultiAuthSessionPortAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 2, 1, 1),
    _EtsysMultiAuthSessionPortAuthStatus_Type()
)
etsysMultiAuthSessionPortAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionPortAuthStatus.setStatus("current")
_EtsysMultiAuthModule_ObjectIdentity = ObjectIdentity
etsysMultiAuthModule = _EtsysMultiAuthModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5)
)
_EtsysMultiAuthModuleTable_Object = MibTable
etsysMultiAuthModuleTable = _EtsysMultiAuthModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleTable.setStatus("current")
_EtsysMultiAuthModuleEntry_Object = MibTableRow
etsysMultiAuthModuleEntry = _EtsysMultiAuthModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 1, 1)
)
etsysMultiAuthModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleEntry.setStatus("current")
_EtsysMultiAuthModuleMaxNumUsers_Type = Unsigned32
_EtsysMultiAuthModuleMaxNumUsers_Object = MibTableColumn
etsysMultiAuthModuleMaxNumUsers = _EtsysMultiAuthModuleMaxNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 1, 1, 1),
    _EtsysMultiAuthModuleMaxNumUsers_Type()
)
etsysMultiAuthModuleMaxNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthModuleMaxNumUsers.setStatus("current")
_EtsysMultiAuthModuleCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthModuleCurrentNumUsers_Object = MibTableColumn
etsysMultiAuthModuleCurrentNumUsers = _EtsysMultiAuthModuleCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 1, 1, 2),
    _EtsysMultiAuthModuleCurrentNumUsers_Type()
)
etsysMultiAuthModuleCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthModuleCurrentNumUsers.setStatus("current")


class _EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Type(EnabledStatus):
    """Custom type etsysMultiAuthModuleMaxNumUsersReachedTrapEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Type.__name__ = "EnabledStatus"
_EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Object = MibScalar
etsysMultiAuthModuleMaxNumUsersReachedTrapEnable = _EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 2),
    _EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Type()
)
etsysMultiAuthModuleMaxNumUsersReachedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthModuleMaxNumUsersReachedTrapEnable.setStatus("current")
_EtsysMultiAuthCounters_ObjectIdentity = ObjectIdentity
etsysMultiAuthCounters = _EtsysMultiAuthCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 6)
)
_EtsysMultiAuthCounterTable_Object = MibTable
etsysMultiAuthCounterTable = _EtsysMultiAuthCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 6, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthCounterTable.setStatus("current")
_EtsysMultiAuthCounterEntry_Object = MibTableRow
etsysMultiAuthCounterEntry = _EtsysMultiAuthCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 6, 1, 1)
)
etsysMultiAuthCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthCounterEntry.setStatus("current")
_EtsysMultiAuthCounterInboundBytes_Type = Counter64
_EtsysMultiAuthCounterInboundBytes_Object = MibTableColumn
etsysMultiAuthCounterInboundBytes = _EtsysMultiAuthCounterInboundBytes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 6, 1, 1, 1),
    _EtsysMultiAuthCounterInboundBytes_Type()
)
etsysMultiAuthCounterInboundBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthCounterInboundBytes.setStatus("current")
_EtsysMultiAuthCounterInboundPackets_Type = Counter64
_EtsysMultiAuthCounterInboundPackets_Object = MibTableColumn
etsysMultiAuthCounterInboundPackets = _EtsysMultiAuthCounterInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 6, 1, 1, 2),
    _EtsysMultiAuthCounterInboundPackets_Type()
)
etsysMultiAuthCounterInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthCounterInboundPackets.setStatus("current")
_EtsysMultiAuthCounterOutboundBytes_Type = Counter64
_EtsysMultiAuthCounterOutboundBytes_Object = MibTableColumn
etsysMultiAuthCounterOutboundBytes = _EtsysMultiAuthCounterOutboundBytes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 6, 1, 1, 3),
    _EtsysMultiAuthCounterOutboundBytes_Type()
)
etsysMultiAuthCounterOutboundBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthCounterOutboundBytes.setStatus("current")
_EtsysMultiAuthCounterOutboundPackets_Type = Counter64
_EtsysMultiAuthCounterOutboundPackets_Object = MibTableColumn
etsysMultiAuthCounterOutboundPackets = _EtsysMultiAuthCounterOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 6, 1, 1, 4),
    _EtsysMultiAuthCounterOutboundPackets_Type()
)
etsysMultiAuthCounterOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthCounterOutboundPackets.setStatus("current")


class _EtsysMultiAuthCounterEnable_Type(EnabledStatus):
    """Custom type etsysMultiAuthCounterEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysMultiAuthCounterEnable_Type.__name__ = "EnabledStatus"
_EtsysMultiAuthCounterEnable_Object = MibScalar
etsysMultiAuthCounterEnable = _EtsysMultiAuthCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 6, 2),
    _EtsysMultiAuthCounterEnable_Type()
)
etsysMultiAuthCounterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthCounterEnable.setStatus("current")
_EtsysMultiAuthConformance_ObjectIdentity = ObjectIdentity
etsysMultiAuthConformance = _EtsysMultiAuthConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2)
)
_EtsysMultiAuthGroups_ObjectIdentity = ObjectIdentity
etsysMultiAuthGroups = _EtsysMultiAuthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1)
)
_EtsysMultiAuthCompliances_ObjectIdentity = ObjectIdentity
etsysMultiAuthCompliances = _EtsysMultiAuthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2)
)

# Managed Objects groups

etsysMultiAuthSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 1)
)
etsysMultiAuthSystemGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemSupportedTypes"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMaxNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemCurrentNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMode"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemDefaultPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemAdminPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemOperPrecedence"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSystemGroup.setStatus("deprecated")

etsysMultiAuthPortBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 2)
)
etsysMultiAuthPortBaseGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortMode"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortMaxNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortNumUsersAllowed"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortCurrentNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortClearUsers"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortBaseGroup.setStatus("current")

etsysMultiAuthPortTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 3)
)
etsysMultiAuthPortTrapGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTrapEnable")
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortTrapGroup.setStatus("current")

etsysMultiAuthStationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 4)
)
etsysMultiAuthStationGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationClearUsers"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthStationGroup.setStatus("current")

etsysMultiAuthSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 5)
)
etsysMultiAuthSessionGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionStationAuthStatus"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthAttemptTime"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddr"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPolicyIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionIsApplied"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPortAuthStatus"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionGroup.setStatus("deprecated")

etsysMultiAuthModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 7)
)
etsysMultiAuthModuleGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleMaxNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleCurrentNumUsers"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleGroup.setStatus("current")

etsysMultiAuthSessionGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 8)
)
etsysMultiAuthSessionGroup2.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionStationAuthStatus"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthAttemptTime"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddr"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPolicyIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionIsApplied"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionTerminationTime"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPortAuthStatus"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionGroup2.setStatus("deprecated")

etsysMultiAuthTimeoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 9)
)
etsysMultiAuthTimeoutGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionTimeout"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthIdleTimeout"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionSessionTimeout"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionIdleTimeout"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionDuration"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionIdleTime"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthTimeoutGroup.setStatus("current")

etsysMultiAuthCurrentNumUsersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 10)
)
etsysMultiAuthCurrentNumUsersGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthCurrentNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTypeCurrentNumUsers"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthCurrentNumUsersGroup.setStatus("current")

etsysMultiAuthModuleTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 11)
)
etsysMultiAuthModuleTrapGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleMaxNumUsersReachedTrapEnable")
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleTrapGroup.setStatus("current")

etsysMultiAuthSystemTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 12)
)
etsysMultiAuthSystemTrapGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMaxNumUsersReachedTrapEnable")
)
if mibBuilder.loadTexts:
    etsysMultiAuthSystemTrapGroup.setStatus("current")

etsysMultiAuthTunnelAttributeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 15)
)
etsysMultiAuthTunnelAttributeGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionVlanTunnelAttribute")
)
if mibBuilder.loadTexts:
    etsysMultiAuthTunnelAttributeGroup.setStatus("current")

etsysMultiAuthCounterEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 16)
)
etsysMultiAuthCounterEnableGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthCounterEnable")
)
if mibBuilder.loadTexts:
    etsysMultiAuthCounterEnableGroup.setStatus("current")

etsysMultiAuthInboundCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 17)
)
etsysMultiAuthInboundCounterGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthCounterInboundBytes"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthCounterInboundPackets"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthInboundCounterGroup.setStatus("current")

etsysMultiAuthOutboundCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 18)
)
etsysMultiAuthOutboundCounterGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthCounterOutboundBytes"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthCounterOutboundPackets"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthOutboundCounterGroup.setStatus("current")

etsysMultiAuthSessionGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 19)
)
etsysMultiAuthSessionGroup3.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionStationAuthStatus"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthAttemptTime"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddr"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPolicyIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionIsApplied"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionTerminationTime"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPortAuthStatus"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionClear"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionGroup3.setStatus("current")

etsysMultiAuthSystemGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 20)
)
etsysMultiAuthSystemGroup2.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemSupportedTypes"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMaxNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemCurrentNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMode"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemDefaultPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemAdminPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemOperPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionsUniquePerPort"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSystemGroup2.setStatus("deprecated")

etsysMultiAuthSystemGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 21)
)
etsysMultiAuthSystemGroup3.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemSupportedTypes"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMaxNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemCurrentNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMode"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemDefaultPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemAdminPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemOperPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionsUniquePerPort"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionsUniquePerPortOperStatus"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemReAuthenticationTimeoutAction"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSystemGroup3.setStatus("current")


# Notification objects

etsysMultiAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 1)
)
etsysMultiAuthSuccess.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
        ("IF-MIB", "ifIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSuccess.setStatus(
        "current"
    )

etsysMultiAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 2)
)
etsysMultiAuthFailed.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
        ("IF-MIB", "ifIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthFailed.setStatus(
        "current"
    )

etsysMultiAuthTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 3)
)
etsysMultiAuthTerminated.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
        ("IF-MIB", "ifIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthTerminated.setStatus(
        "current"
    )

etsysMultiAuthMaxNumUsersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 4)
)
etsysMultiAuthMaxNumUsersReached.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    etsysMultiAuthMaxNumUsersReached.setStatus(
        "current"
    )

etsysMultiAuthModuleMaxNumUsersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 5)
)
etsysMultiAuthModuleMaxNumUsersReached.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleMaxNumUsersReached.setStatus(
        "current"
    )

etsysMultiAuthSystemMaxNumUsersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 6)
)
if mibBuilder.loadTexts:
    etsysMultiAuthSystemMaxNumUsersReached.setStatus(
        "current"
    )


# Notifications groups

etsysMultiAuthNotificationPortGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 6)
)
etsysMultiAuthNotificationPortGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSuccess"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthFailed"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthTerminated"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthMaxNumUsersReached"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthNotificationPortGroup.setStatus(
        "current"
    )

etsysMultiAuthNotificationModuleGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 13)
)
etsysMultiAuthNotificationModuleGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleMaxNumUsersReached")
)
if mibBuilder.loadTexts:
    etsysMultiAuthNotificationModuleGroup.setStatus(
        "current"
    )

etsysMultiAuthNotificationSystemGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 14)
)
etsysMultiAuthNotificationSystemGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMaxNumUsersReached")
)
if mibBuilder.loadTexts:
    etsysMultiAuthNotificationSystemGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysMultiAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 1)
)
etsysMultiAuthCompliance.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortBaseGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationPortGroup"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance.setStatus(
        "deprecated"
    )

etsysMultiAuthCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 2)
)
etsysMultiAuthCompliance2.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortBaseGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationPortGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleGroup"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance2.setStatus(
        "deprecated"
    )

etsysMultiAuthCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 3)
)
etsysMultiAuthCompliance3.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortBaseGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionGroup2"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationPortGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleGroup"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance3.setStatus(
        "deprecated"
    )

etsysMultiAuthTimeoutCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 4)
)
etsysMultiAuthTimeoutCompliance.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthTimeoutGroup")
)
if mibBuilder.loadTexts:
    etsysMultiAuthTimeoutCompliance.setStatus(
        "current"
    )

etsysMultiAuthCurrentNumUserCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 5)
)
etsysMultiAuthCurrentNumUserCompliance.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthCurrentNumUsersGroup")
)
if mibBuilder.loadTexts:
    etsysMultiAuthCurrentNumUserCompliance.setStatus(
        "current"
    )

etsysMultiAuthCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 6)
)
etsysMultiAuthCompliance4.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortBaseGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionGroup2"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationPortGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationModuleGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationSystemGroup"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance4.setStatus(
        "deprecated"
    )

etsysMultiTunnelAttributeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 7)
)
etsysMultiTunnelAttributeCompliance.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthTunnelAttributeGroup")
)
if mibBuilder.loadTexts:
    etsysMultiTunnelAttributeCompliance.setStatus(
        "current"
    )

etsysMultiAuthCounterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 8)
)
etsysMultiAuthCounterCompliance.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthCounterEnableGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthInboundCounterGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthOutboundCounterGroup"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthCounterCompliance.setStatus(
        "current"
    )

etsysMultiAuthCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 9)
)
etsysMultiAuthCompliance5.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemGroup2"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortBaseGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionGroup3"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationPortGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationModuleGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationSystemGroup"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance5.setStatus(
        "deprecated"
    )

etsysMultiAuthCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 10)
)
etsysMultiAuthCompliance6.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemGroup3"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortBaseGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionGroup3"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationPortGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationModuleGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemTrapGroup"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthNotificationSystemGroup"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MULTI-AUTH-MIB",
    **{"EtsysMultiAuthTypes": EtsysMultiAuthTypes,
       "EtsysMultiAuthTypePrecedence": EtsysMultiAuthTypePrecedence,
       "EtsysMultiAuthStatus": EtsysMultiAuthStatus,
       "etsysMultiAuthMIB": etsysMultiAuthMIB,
       "etsysMultiAuthObjects": etsysMultiAuthObjects,
       "etsysMultiAuthNotification": etsysMultiAuthNotification,
       "etsysMultiAuthSuccess": etsysMultiAuthSuccess,
       "etsysMultiAuthFailed": etsysMultiAuthFailed,
       "etsysMultiAuthTerminated": etsysMultiAuthTerminated,
       "etsysMultiAuthMaxNumUsersReached": etsysMultiAuthMaxNumUsersReached,
       "etsysMultiAuthModuleMaxNumUsersReached": etsysMultiAuthModuleMaxNumUsersReached,
       "etsysMultiAuthSystemMaxNumUsersReached": etsysMultiAuthSystemMaxNumUsersReached,
       "etsysMultiAuthSystem": etsysMultiAuthSystem,
       "etsysMultiAuthSystemSupportedTypes": etsysMultiAuthSystemSupportedTypes,
       "etsysMultiAuthSystemMaxNumUsers": etsysMultiAuthSystemMaxNumUsers,
       "etsysMultiAuthSystemCurrentNumUsers": etsysMultiAuthSystemCurrentNumUsers,
       "etsysMultiAuthSystemMode": etsysMultiAuthSystemMode,
       "etsysMultiAuthSystemDefaultPrecedence": etsysMultiAuthSystemDefaultPrecedence,
       "etsysMultiAuthSystemAdminPrecedence": etsysMultiAuthSystemAdminPrecedence,
       "etsysMultiAuthSystemOperPrecedence": etsysMultiAuthSystemOperPrecedence,
       "etsysMultiAuthTypePropertiesTable": etsysMultiAuthTypePropertiesTable,
       "etsysMultiAuthTypePropertiesEntry": etsysMultiAuthTypePropertiesEntry,
       "etsysMultiAuthType": etsysMultiAuthType,
       "etsysMultiAuthSessionTimeout": etsysMultiAuthSessionTimeout,
       "etsysMultiAuthIdleTimeout": etsysMultiAuthIdleTimeout,
       "etsysMultiAuthCurrentNumUsers": etsysMultiAuthCurrentNumUsers,
       "etsysMultiAuthSystemMaxNumUsersReachedTrapEnable": etsysMultiAuthSystemMaxNumUsersReachedTrapEnable,
       "etsysMultiAuthSessionsUniquePerPort": etsysMultiAuthSessionsUniquePerPort,
       "etsysMultiAuthSessionsUniquePerPortOperStatus": etsysMultiAuthSessionsUniquePerPortOperStatus,
       "etsysMultiAuthSystemReAuthenticationTimeoutAction": etsysMultiAuthSystemReAuthenticationTimeoutAction,
       "etsysMultiAuthPort": etsysMultiAuthPort,
       "etsysMultiAuthPortTable": etsysMultiAuthPortTable,
       "etsysMultiAuthPortEntry": etsysMultiAuthPortEntry,
       "etsysMultiAuthPortMode": etsysMultiAuthPortMode,
       "etsysMultiAuthPortMaxNumUsers": etsysMultiAuthPortMaxNumUsers,
       "etsysMultiAuthPortNumUsersAllowed": etsysMultiAuthPortNumUsersAllowed,
       "etsysMultiAuthPortCurrentNumUsers": etsysMultiAuthPortCurrentNumUsers,
       "etsysMultiAuthPortClearUsers": etsysMultiAuthPortClearUsers,
       "etsysMultiAuthPortTrapEnable": etsysMultiAuthPortTrapEnable,
       "etsysMultiAuthPortTypeTable": etsysMultiAuthPortTypeTable,
       "etsysMultiAuthPortTypeEntry": etsysMultiAuthPortTypeEntry,
       "etsysMultiAuthPortTypeCurrentNumUsers": etsysMultiAuthPortTypeCurrentNumUsers,
       "etsysMultiAuthStation": etsysMultiAuthStation,
       "etsysMultiAuthStationTable": etsysMultiAuthStationTable,
       "etsysMultiAuthStationEntry": etsysMultiAuthStationEntry,
       "etsysMultiAuthStationAddrType": etsysMultiAuthStationAddrType,
       "etsysMultiAuthStationAddr": etsysMultiAuthStationAddr,
       "etsysMultiAuthStationClearUsers": etsysMultiAuthStationClearUsers,
       "etsysMultiAuthSession": etsysMultiAuthSession,
       "etsysMultiAuthSessionStationTable": etsysMultiAuthSessionStationTable,
       "etsysMultiAuthSessionStationEntry": etsysMultiAuthSessionStationEntry,
       "etsysMultiAuthSessionAgentType": etsysMultiAuthSessionAgentType,
       "etsysMultiAuthSessionStationAuthStatus": etsysMultiAuthSessionStationAuthStatus,
       "etsysMultiAuthSessionAuthAttemptTime": etsysMultiAuthSessionAuthAttemptTime,
       "etsysMultiAuthSessionAuthServerType": etsysMultiAuthSessionAuthServerType,
       "etsysMultiAuthSessionAuthServerAddrType": etsysMultiAuthSessionAuthServerAddrType,
       "etsysMultiAuthSessionAuthServerAddr": etsysMultiAuthSessionAuthServerAddr,
       "etsysMultiAuthSessionPolicyIndex": etsysMultiAuthSessionPolicyIndex,
       "etsysMultiAuthSessionIsApplied": etsysMultiAuthSessionIsApplied,
       "etsysMultiAuthSessionTerminationTime": etsysMultiAuthSessionTerminationTime,
       "etsysMultiAuthSessionSessionTimeout": etsysMultiAuthSessionSessionTimeout,
       "etsysMultiAuthSessionIdleTimeout": etsysMultiAuthSessionIdleTimeout,
       "etsysMultiAuthSessionDuration": etsysMultiAuthSessionDuration,
       "etsysMultiAuthSessionIdleTime": etsysMultiAuthSessionIdleTime,
       "etsysMultiAuthSessionVlanTunnelAttribute": etsysMultiAuthSessionVlanTunnelAttribute,
       "etsysMultiAuthSessionClear": etsysMultiAuthSessionClear,
       "etsysMultiAuthSessionPortTable": etsysMultiAuthSessionPortTable,
       "etsysMultiAuthSessionPortEntry": etsysMultiAuthSessionPortEntry,
       "etsysMultiAuthSessionPortAuthStatus": etsysMultiAuthSessionPortAuthStatus,
       "etsysMultiAuthModule": etsysMultiAuthModule,
       "etsysMultiAuthModuleTable": etsysMultiAuthModuleTable,
       "etsysMultiAuthModuleEntry": etsysMultiAuthModuleEntry,
       "etsysMultiAuthModuleMaxNumUsers": etsysMultiAuthModuleMaxNumUsers,
       "etsysMultiAuthModuleCurrentNumUsers": etsysMultiAuthModuleCurrentNumUsers,
       "etsysMultiAuthModuleMaxNumUsersReachedTrapEnable": etsysMultiAuthModuleMaxNumUsersReachedTrapEnable,
       "etsysMultiAuthCounters": etsysMultiAuthCounters,
       "etsysMultiAuthCounterTable": etsysMultiAuthCounterTable,
       "etsysMultiAuthCounterEntry": etsysMultiAuthCounterEntry,
       "etsysMultiAuthCounterInboundBytes": etsysMultiAuthCounterInboundBytes,
       "etsysMultiAuthCounterInboundPackets": etsysMultiAuthCounterInboundPackets,
       "etsysMultiAuthCounterOutboundBytes": etsysMultiAuthCounterOutboundBytes,
       "etsysMultiAuthCounterOutboundPackets": etsysMultiAuthCounterOutboundPackets,
       "etsysMultiAuthCounterEnable": etsysMultiAuthCounterEnable,
       "etsysMultiAuthConformance": etsysMultiAuthConformance,
       "etsysMultiAuthGroups": etsysMultiAuthGroups,
       "etsysMultiAuthSystemGroup": etsysMultiAuthSystemGroup,
       "etsysMultiAuthPortBaseGroup": etsysMultiAuthPortBaseGroup,
       "etsysMultiAuthPortTrapGroup": etsysMultiAuthPortTrapGroup,
       "etsysMultiAuthStationGroup": etsysMultiAuthStationGroup,
       "etsysMultiAuthSessionGroup": etsysMultiAuthSessionGroup,
       "etsysMultiAuthNotificationPortGroup": etsysMultiAuthNotificationPortGroup,
       "etsysMultiAuthModuleGroup": etsysMultiAuthModuleGroup,
       "etsysMultiAuthSessionGroup2": etsysMultiAuthSessionGroup2,
       "etsysMultiAuthTimeoutGroup": etsysMultiAuthTimeoutGroup,
       "etsysMultiAuthCurrentNumUsersGroup": etsysMultiAuthCurrentNumUsersGroup,
       "etsysMultiAuthModuleTrapGroup": etsysMultiAuthModuleTrapGroup,
       "etsysMultiAuthSystemTrapGroup": etsysMultiAuthSystemTrapGroup,
       "etsysMultiAuthNotificationModuleGroup": etsysMultiAuthNotificationModuleGroup,
       "etsysMultiAuthNotificationSystemGroup": etsysMultiAuthNotificationSystemGroup,
       "etsysMultiAuthTunnelAttributeGroup": etsysMultiAuthTunnelAttributeGroup,
       "etsysMultiAuthCounterEnableGroup": etsysMultiAuthCounterEnableGroup,
       "etsysMultiAuthInboundCounterGroup": etsysMultiAuthInboundCounterGroup,
       "etsysMultiAuthOutboundCounterGroup": etsysMultiAuthOutboundCounterGroup,
       "etsysMultiAuthSessionGroup3": etsysMultiAuthSessionGroup3,
       "etsysMultiAuthSystemGroup2": etsysMultiAuthSystemGroup2,
       "etsysMultiAuthSystemGroup3": etsysMultiAuthSystemGroup3,
       "etsysMultiAuthCompliances": etsysMultiAuthCompliances,
       "etsysMultiAuthCompliance": etsysMultiAuthCompliance,
       "etsysMultiAuthCompliance2": etsysMultiAuthCompliance2,
       "etsysMultiAuthCompliance3": etsysMultiAuthCompliance3,
       "etsysMultiAuthTimeoutCompliance": etsysMultiAuthTimeoutCompliance,
       "etsysMultiAuthCurrentNumUserCompliance": etsysMultiAuthCurrentNumUserCompliance,
       "etsysMultiAuthCompliance4": etsysMultiAuthCompliance4,
       "etsysMultiTunnelAttributeCompliance": etsysMultiTunnelAttributeCompliance,
       "etsysMultiAuthCounterCompliance": etsysMultiAuthCounterCompliance,
       "etsysMultiAuthCompliance5": etsysMultiAuthCompliance5,
       "etsysMultiAuthCompliance6": etsysMultiAuthCompliance6}
)
