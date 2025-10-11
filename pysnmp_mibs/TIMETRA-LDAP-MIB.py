# SNMP MIB module (TIMETRA-LDAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-LDAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:54:33 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TNamedItemOrEmpty,
 TTcpUdpPort,
 TmnxAdminState,
 TmnxLongDisplayString,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TmnxAdminState",
    "TmnxLongDisplayString",
    "TmnxOperState")


# MODULE-IDENTITY

timetraLdapMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 106)
)
if mibBuilder.loadTexts:
    timetraLdapMIBModule.setRevisions(
        ("2016-02-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxLdapConformance_ObjectIdentity = ObjectIdentity
tmnxLdapConformance = _TmnxLdapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 106)
)
_TmnxLdapCompliances_ObjectIdentity = ObjectIdentity
tmnxLdapCompliances = _TmnxLdapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 106, 1)
)
_TmnxLdapGroups_ObjectIdentity = ObjectIdentity
tmnxLdapGroups = _TmnxLdapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 106, 2)
)
_TmnxLdapInitialGroups_ObjectIdentity = ObjectIdentity
tmnxLdapInitialGroups = _TmnxLdapInitialGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 106, 2, 1)
)
_TmnxLdapObjs_ObjectIdentity = ObjectIdentity
tmnxLdapObjs = _TmnxLdapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106)
)
_TmnxLdapScalarObjs_ObjectIdentity = ObjectIdentity
tmnxLdapScalarObjs = _TmnxLdapScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1)
)
_TmnxLdapScalarStatsObjs_ObjectIdentity = ObjectIdentity
tmnxLdapScalarStatsObjs = _TmnxLdapScalarStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1, 1)
)
_TmnxLdapServerTableLastChanged_Type = TimeStamp
_TmnxLdapServerTableLastChanged_Object = MibScalar
tmnxLdapServerTableLastChanged = _TmnxLdapServerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1, 1, 1),
    _TmnxLdapServerTableLastChanged_Type()
)
tmnxLdapServerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLdapServerTableLastChanged.setStatus("current")
_TmnxLdapScalarConfigObjs_ObjectIdentity = ObjectIdentity
tmnxLdapScalarConfigObjs = _TmnxLdapScalarConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1, 2)
)


class _TmnxLdapAdminState_Type(TmnxAdminState):
    """Custom type tmnxLdapAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxLdapAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLdapAdminState_Object = MibScalar
tmnxLdapAdminState = _TmnxLdapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1, 2, 1),
    _TmnxLdapAdminState_Type()
)
tmnxLdapAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLdapAdminState.setStatus("current")
_TmnxLdapOperState_Type = TmnxOperState
_TmnxLdapOperState_Object = MibScalar
tmnxLdapOperState = _TmnxLdapOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1, 2, 2),
    _TmnxLdapOperState_Type()
)
tmnxLdapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLdapOperState.setStatus("current")


class _TmnxLdapRetryAttempts_Type(Unsigned32):
    """Custom type tmnxLdapRetryAttempts based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxLdapRetryAttempts_Type.__name__ = "Unsigned32"
_TmnxLdapRetryAttempts_Object = MibScalar
tmnxLdapRetryAttempts = _TmnxLdapRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1, 2, 3),
    _TmnxLdapRetryAttempts_Type()
)
tmnxLdapRetryAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLdapRetryAttempts.setStatus("current")


class _TmnxLdapTimeout_Type(Unsigned32):
    """Custom type tmnxLdapTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TmnxLdapTimeout_Type.__name__ = "Unsigned32"
_TmnxLdapTimeout_Object = MibScalar
tmnxLdapTimeout = _TmnxLdapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1, 2, 4),
    _TmnxLdapTimeout_Type()
)
tmnxLdapTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLdapTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLdapTimeout.setUnits("Seconds")


class _TmnxLdapUseTemplate_Type(TruthValue):
    """Custom type tmnxLdapUseTemplate based on TruthValue"""
    defaultValue = 1


_TmnxLdapUseTemplate_Type.__name__ = "TruthValue"
_TmnxLdapUseTemplate_Object = MibScalar
tmnxLdapUseTemplate = _TmnxLdapUseTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1, 2, 5),
    _TmnxLdapUseTemplate_Type()
)
tmnxLdapUseTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLdapUseTemplate.setStatus("current")


class _TmnxLdapPublicKeyAuthentication_Type(TruthValue):
    """Custom type tmnxLdapPublicKeyAuthentication based on TruthValue"""
    defaultValue = 2


_TmnxLdapPublicKeyAuthentication_Type.__name__ = "TruthValue"
_TmnxLdapPublicKeyAuthentication_Object = MibScalar
tmnxLdapPublicKeyAuthentication = _TmnxLdapPublicKeyAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 1, 2, 6),
    _TmnxLdapPublicKeyAuthentication_Type()
)
tmnxLdapPublicKeyAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxLdapPublicKeyAuthentication.setStatus("current")
_TmnxLdapConfigObjs_ObjectIdentity = ObjectIdentity
tmnxLdapConfigObjs = _TmnxLdapConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2)
)
_TmnxLdapServerTable_Object = MibTable
tmnxLdapServerTable = _TmnxLdapServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxLdapServerTable.setStatus("current")
_TmnxLdapServerEntry_Object = MibTableRow
tmnxLdapServerEntry = _TmnxLdapServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1)
)
tmnxLdapServerEntry.setIndexNames(
    (0, "TIMETRA-LDAP-MIB", "tmnxLdapServerIndex"),
)
if mibBuilder.loadTexts:
    tmnxLdapServerEntry.setStatus("current")


class _TmnxLdapServerIndex_Type(Unsigned32):
    """Custom type tmnxLdapServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxLdapServerIndex_Type.__name__ = "Unsigned32"
_TmnxLdapServerIndex_Object = MibTableColumn
tmnxLdapServerIndex = _TmnxLdapServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 1),
    _TmnxLdapServerIndex_Type()
)
tmnxLdapServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLdapServerIndex.setStatus("current")
_TmnxLdapServerLastChanged_Type = TimeStamp
_TmnxLdapServerLastChanged_Object = MibTableColumn
tmnxLdapServerLastChanged = _TmnxLdapServerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 2),
    _TmnxLdapServerLastChanged_Type()
)
tmnxLdapServerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLdapServerLastChanged.setStatus("current")
_TmnxLdapServerRowStatus_Type = RowStatus
_TmnxLdapServerRowStatus_Object = MibTableColumn
tmnxLdapServerRowStatus = _TmnxLdapServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 3),
    _TmnxLdapServerRowStatus_Type()
)
tmnxLdapServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerRowStatus.setStatus("current")


class _TmnxLdapServerAdminState_Type(TmnxAdminState):
    """Custom type tmnxLdapServerAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLdapServerAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLdapServerAdminState_Object = MibTableColumn
tmnxLdapServerAdminState = _TmnxLdapServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 4),
    _TmnxLdapServerAdminState_Type()
)
tmnxLdapServerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerAdminState.setStatus("current")
_TmnxLdapServerOperState_Type = TmnxOperState
_TmnxLdapServerOperState_Object = MibTableColumn
tmnxLdapServerOperState = _TmnxLdapServerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 5),
    _TmnxLdapServerOperState_Type()
)
tmnxLdapServerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLdapServerOperState.setStatus("current")


class _TmnxLdapServerInetAddressType_Type(InetAddressType):
    """Custom type tmnxLdapServerInetAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxLdapServerInetAddressType_Type.__name__ = "InetAddressType"
_TmnxLdapServerInetAddressType_Object = MibTableColumn
tmnxLdapServerInetAddressType = _TmnxLdapServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 6),
    _TmnxLdapServerInetAddressType_Type()
)
tmnxLdapServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerInetAddressType.setStatus("current")


class _TmnxLdapServerInetAddress_Type(InetAddress):
    """Custom type tmnxLdapServerInetAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLdapServerInetAddress_Type.__name__ = "InetAddress"
_TmnxLdapServerInetAddress_Object = MibTableColumn
tmnxLdapServerInetAddress = _TmnxLdapServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 7),
    _TmnxLdapServerInetAddress_Type()
)
tmnxLdapServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerInetAddress.setStatus("current")


class _TmnxLdapServerPort_Type(TTcpUdpPort):
    """Custom type tmnxLdapServerPort based on TTcpUdpPort"""
    defaultValue = 389

    subtypeSpec = TTcpUdpPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxLdapServerPort_Type.__name__ = "TTcpUdpPort"
_TmnxLdapServerPort_Object = MibTableColumn
tmnxLdapServerPort = _TmnxLdapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 8),
    _TmnxLdapServerPort_Type()
)
tmnxLdapServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerPort.setStatus("current")


class _TmnxLdapServerBindAuthRootDn_Type(TmnxLongDisplayString):
    """Custom type tmnxLdapServerBindAuthRootDn based on TmnxLongDisplayString"""
    defaultHexValue = ""

    subtypeSpec = TmnxLongDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TmnxLdapServerBindAuthRootDn_Type.__name__ = "TmnxLongDisplayString"
_TmnxLdapServerBindAuthRootDn_Object = MibTableColumn
tmnxLdapServerBindAuthRootDn = _TmnxLdapServerBindAuthRootDn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 9),
    _TmnxLdapServerBindAuthRootDn_Type()
)
tmnxLdapServerBindAuthRootDn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerBindAuthRootDn.setStatus("current")


class _TmnxLdapServerBindAuthPassword_Type(DisplayString):
    """Custom type tmnxLdapServerBindAuthPassword based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TmnxLdapServerBindAuthPassword_Type.__name__ = "DisplayString"
_TmnxLdapServerBindAuthPassword_Object = MibTableColumn
tmnxLdapServerBindAuthPassword = _TmnxLdapServerBindAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 10),
    _TmnxLdapServerBindAuthPassword_Type()
)
tmnxLdapServerBindAuthPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerBindAuthPassword.setStatus("current")


class _TmnxLdapServerName_Type(TNamedItemOrEmpty):
    """Custom type tmnxLdapServerName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLdapServerName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLdapServerName_Object = MibTableColumn
tmnxLdapServerName = _TmnxLdapServerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 11),
    _TmnxLdapServerName_Type()
)
tmnxLdapServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerName.setStatus("current")


class _TmnxLdapServerSearch_Type(TmnxLongDisplayString):
    """Custom type tmnxLdapServerSearch based on TmnxLongDisplayString"""
    defaultHexValue = ""

    subtypeSpec = TmnxLongDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_TmnxLdapServerSearch_Type.__name__ = "TmnxLongDisplayString"
_TmnxLdapServerSearch_Object = MibTableColumn
tmnxLdapServerSearch = _TmnxLdapServerSearch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 12),
    _TmnxLdapServerSearch_Type()
)
tmnxLdapServerSearch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerSearch.setStatus("current")


class _TmnxLdapServerTlsProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxLdapServerTlsProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLdapServerTlsProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLdapServerTlsProfile_Object = MibTableColumn
tmnxLdapServerTlsProfile = _TmnxLdapServerTlsProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 2, 1, 1, 13),
    _TmnxLdapServerTlsProfile_Type()
)
tmnxLdapServerTlsProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLdapServerTlsProfile.setStatus("current")
_TmnxLdapStatsObjs_ObjectIdentity = ObjectIdentity
tmnxLdapStatsObjs = _TmnxLdapStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 3)
)
_TmnxLdapNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxLdapNotificationObjs = _TmnxLdapNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 106, 10)
)
_TmnxLdapNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxLdapNotifyPrefix = _TmnxLdapNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 106)
)
_TmnxLdapNotifications_ObjectIdentity = ObjectIdentity
tmnxLdapNotifications = _TmnxLdapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 106, 0)
)

# Managed Objects groups

tmnxLdapInitialGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 106, 2, 1, 1)
)
tmnxLdapInitialGroup.setObjects(
      *(("TIMETRA-LDAP-MIB", "tmnxLdapAdminState"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapOperState"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapRetryAttempts"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapTimeout"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapUseTemplate"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapPublicKeyAuthentication"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerTableLastChanged"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerLastChanged"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerRowStatus"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerAdminState"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerOperState"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerInetAddressType"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerInetAddress"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerPort"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerBindAuthRootDn"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerBindAuthPassword"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerName"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerSearch"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerTlsProfile"))
)
if mibBuilder.loadTexts:
    tmnxLdapInitialGroup.setStatus("current")


# Notification objects

tmnxLdapOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 106, 0, 1)
)
tmnxLdapOperStateChange.setObjects(
    ("TIMETRA-LDAP-MIB", "tmnxLdapOperState")
)
if mibBuilder.loadTexts:
    tmnxLdapOperStateChange.setStatus(
        "current"
    )

tmnxLdapServerOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 106, 0, 2)
)
tmnxLdapServerOperStateChange.setObjects(
      *(("TIMETRA-LDAP-MIB", "tmnxLdapServerName"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerOperState"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerInetAddressType"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerInetAddress"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerPort"))
)
if mibBuilder.loadTexts:
    tmnxLdapServerOperStateChange.setStatus(
        "current"
    )


# Notifications groups

tmnxLdapNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 106, 2, 1, 2)
)
tmnxLdapNotifyGroup.setObjects(
      *(("TIMETRA-LDAP-MIB", "tmnxLdapOperStateChange"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapServerOperStateChange"))
)
if mibBuilder.loadTexts:
    tmnxLdapNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLdapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 106, 1, 1)
)
tmnxLdapCompliance.setObjects(
      *(("TIMETRA-LDAP-MIB", "tmnxLdapInitialGroup"),
        ("TIMETRA-LDAP-MIB", "tmnxLdapNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxLdapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LDAP-MIB",
    **{"timetraLdapMIBModule": timetraLdapMIBModule,
       "tmnxLdapConformance": tmnxLdapConformance,
       "tmnxLdapCompliances": tmnxLdapCompliances,
       "tmnxLdapCompliance": tmnxLdapCompliance,
       "tmnxLdapGroups": tmnxLdapGroups,
       "tmnxLdapInitialGroups": tmnxLdapInitialGroups,
       "tmnxLdapInitialGroup": tmnxLdapInitialGroup,
       "tmnxLdapNotifyGroup": tmnxLdapNotifyGroup,
       "tmnxLdapObjs": tmnxLdapObjs,
       "tmnxLdapScalarObjs": tmnxLdapScalarObjs,
       "tmnxLdapScalarStatsObjs": tmnxLdapScalarStatsObjs,
       "tmnxLdapServerTableLastChanged": tmnxLdapServerTableLastChanged,
       "tmnxLdapScalarConfigObjs": tmnxLdapScalarConfigObjs,
       "tmnxLdapAdminState": tmnxLdapAdminState,
       "tmnxLdapOperState": tmnxLdapOperState,
       "tmnxLdapRetryAttempts": tmnxLdapRetryAttempts,
       "tmnxLdapTimeout": tmnxLdapTimeout,
       "tmnxLdapUseTemplate": tmnxLdapUseTemplate,
       "tmnxLdapPublicKeyAuthentication": tmnxLdapPublicKeyAuthentication,
       "tmnxLdapConfigObjs": tmnxLdapConfigObjs,
       "tmnxLdapServerTable": tmnxLdapServerTable,
       "tmnxLdapServerEntry": tmnxLdapServerEntry,
       "tmnxLdapServerIndex": tmnxLdapServerIndex,
       "tmnxLdapServerLastChanged": tmnxLdapServerLastChanged,
       "tmnxLdapServerRowStatus": tmnxLdapServerRowStatus,
       "tmnxLdapServerAdminState": tmnxLdapServerAdminState,
       "tmnxLdapServerOperState": tmnxLdapServerOperState,
       "tmnxLdapServerInetAddressType": tmnxLdapServerInetAddressType,
       "tmnxLdapServerInetAddress": tmnxLdapServerInetAddress,
       "tmnxLdapServerPort": tmnxLdapServerPort,
       "tmnxLdapServerBindAuthRootDn": tmnxLdapServerBindAuthRootDn,
       "tmnxLdapServerBindAuthPassword": tmnxLdapServerBindAuthPassword,
       "tmnxLdapServerName": tmnxLdapServerName,
       "tmnxLdapServerSearch": tmnxLdapServerSearch,
       "tmnxLdapServerTlsProfile": tmnxLdapServerTlsProfile,
       "tmnxLdapStatsObjs": tmnxLdapStatsObjs,
       "tmnxLdapNotificationObjs": tmnxLdapNotificationObjs,
       "tmnxLdapNotifyPrefix": tmnxLdapNotifyPrefix,
       "tmnxLdapNotifications": tmnxLdapNotifications,
       "tmnxLdapOperStateChange": tmnxLdapOperStateChange,
       "tmnxLdapServerOperStateChange": tmnxLdapServerOperStateChange}
)
