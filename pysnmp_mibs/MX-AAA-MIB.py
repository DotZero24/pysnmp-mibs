# SNMP MIB module (MX-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-AAA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:27 2025
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

aaaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AaaMIBObjects_ObjectIdentity = ObjectIdentity
aaaMIBObjects = _AaaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1)
)
_UsersTable_Object = MibTable
usersTable = _UsersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 100)
)
if mibBuilder.loadTexts:
    usersTable.setStatus("current")
_UsersEntry_Object = MibTableRow
usersEntry = _UsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 100, 1)
)
usersEntry.setIndexNames(
    (0, "MX-AAA-MIB", "usersUserName"),
)
if mibBuilder.loadTexts:
    usersEntry.setStatus("current")


class _UsersUserName_Type(OctetString):
    """Custom type usersUserName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_UsersUserName_Type.__name__ = "OctetString"
_UsersUserName_Object = MibTableColumn
usersUserName = _UsersUserName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 100, 1, 100),
    _UsersUserName_Type()
)
usersUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersUserName.setStatus("current")


class _UsersPassword_Type(OctetString):
    """Custom type usersPassword based on OctetString"""
    defaultValue = OctetString("")


_UsersPassword_Type.__name__ = "OctetString"
_UsersPassword_Object = MibTableColumn
usersPassword = _UsersPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 100, 1, 200),
    _UsersPassword_Type()
)
usersPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usersPassword.setStatus("current")


class _UsersAccessRights_Type(Integer32):
    """Custom type usersAccessRights based on Integer32"""
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
        *(("admin", 100),
          ("user", 200),
          ("observer", 300))
    )


_UsersAccessRights_Type.__name__ = "Integer32"
_UsersAccessRights_Object = MibTableColumn
usersAccessRights = _UsersAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 100, 1, 250),
    _UsersAccessRights_Type()
)
usersAccessRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usersAccessRights.setStatus("current")


class _UsersLockProtectionEnable_Type(MxEnableState):
    """Custom type usersLockProtectionEnable based on MxEnableState"""
    defaultValue = 1


_UsersLockProtectionEnable_Type.__name__ = "MxEnableState"
_UsersLockProtectionEnable_Object = MibTableColumn
usersLockProtectionEnable = _UsersLockProtectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 100, 1, 275),
    _UsersLockProtectionEnable_Type()
)
usersLockProtectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usersLockProtectionEnable.setStatus("current")


class _UsersDelete_Type(Integer32):
    """Custom type usersDelete based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("delete", 10))
    )


_UsersDelete_Type.__name__ = "Integer32"
_UsersDelete_Object = MibTableColumn
usersDelete = _UsersDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 100, 1, 300),
    _UsersDelete_Type()
)
usersDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usersDelete.setStatus("current")
_UsersStatusTable_Object = MibTable
usersStatusTable = _UsersStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 150)
)
if mibBuilder.loadTexts:
    usersStatusTable.setStatus("current")
_UsersStatusEntry_Object = MibTableRow
usersStatusEntry = _UsersStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 150, 1)
)
usersStatusEntry.setIndexNames(
    (0, "MX-AAA-MIB", "usersStatusUserName"),
)
if mibBuilder.loadTexts:
    usersStatusEntry.setStatus("current")
_UsersStatusUserName_Type = OctetString
_UsersStatusUserName_Object = MibTableColumn
usersStatusUserName = _UsersStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 150, 1, 100),
    _UsersStatusUserName_Type()
)
usersStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersStatusUserName.setStatus("current")
_UsersStatusPassword_Type = OctetString
_UsersStatusPassword_Object = MibTableColumn
usersStatusPassword = _UsersStatusPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 150, 1, 200),
    _UsersStatusPassword_Type()
)
usersStatusPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersStatusPassword.setStatus("current")


class _UsersStatusLocked_Type(Integer32):
    """Custom type usersStatusLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 100),
          ("locked", 200))
    )


_UsersStatusLocked_Type.__name__ = "Integer32"
_UsersStatusLocked_Object = MibTableColumn
usersStatusLocked = _UsersStatusLocked_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 150, 1, 300),
    _UsersStatusLocked_Type()
)
usersStatusLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usersStatusLocked.setStatus("current")


class _BatchUser_Type(OctetString):
    """Custom type batchUser based on OctetString"""
    defaultValue = OctetString("")


_BatchUser_Type.__name__ = "OctetString"
_BatchUser_Object = MibScalar
batchUser = _BatchUser_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 200),
    _BatchUser_Type()
)
batchUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batchUser.setStatus("current")
_ServicesAaaTypeTable_Object = MibTable
servicesAaaTypeTable = _ServicesAaaTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 300)
)
if mibBuilder.loadTexts:
    servicesAaaTypeTable.setStatus("current")
_ServicesAaaTypeEntry_Object = MibTableRow
servicesAaaTypeEntry = _ServicesAaaTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 300, 1)
)
servicesAaaTypeEntry.setIndexNames(
    (0, "MX-AAA-MIB", "servicesAaaTypeService"),
)
if mibBuilder.loadTexts:
    servicesAaaTypeEntry.setStatus("current")


class _ServicesAaaTypeService_Type(OctetString):
    """Custom type servicesAaaTypeService based on OctetString"""
    defaultValue = OctetString("")


_ServicesAaaTypeService_Type.__name__ = "OctetString"
_ServicesAaaTypeService_Object = MibTableColumn
servicesAaaTypeService = _ServicesAaaTypeService_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 300, 1, 100),
    _ServicesAaaTypeService_Type()
)
servicesAaaTypeService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicesAaaTypeService.setStatus("current")


class _ServicesAaaTypeAuthenticationType_Type(Integer32):
    """Custom type servicesAaaTypeAuthenticationType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("local", 100),
          ("radius", 200))
    )


_ServicesAaaTypeAuthenticationType_Type.__name__ = "Integer32"
_ServicesAaaTypeAuthenticationType_Object = MibTableColumn
servicesAaaTypeAuthenticationType = _ServicesAaaTypeAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 300, 1, 200),
    _ServicesAaaTypeAuthenticationType_Type()
)
servicesAaaTypeAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servicesAaaTypeAuthenticationType.setStatus("current")


class _ServicesAaaTypeAccountingType_Type(Integer32):
    """Custom type servicesAaaTypeAccountingType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("radius", 200))
    )


_ServicesAaaTypeAccountingType_Type.__name__ = "Integer32"
_ServicesAaaTypeAccountingType_Object = MibTableColumn
servicesAaaTypeAccountingType = _ServicesAaaTypeAccountingType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 300, 1, 300),
    _ServicesAaaTypeAccountingType_Type()
)
servicesAaaTypeAccountingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servicesAaaTypeAccountingType.setStatus("current")
_RadiusGroup_ObjectIdentity = ObjectIdentity
radiusGroup = _RadiusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000)
)


class _RadiusServersTimeoutS_Type(Unsigned32):
    """Custom type radiusServersTimeoutS based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RadiusServersTimeoutS_Type.__name__ = "Unsigned32"
_RadiusServersTimeoutS_Object = MibScalar
radiusServersTimeoutS = _RadiusServersTimeoutS_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 100),
    _RadiusServersTimeoutS_Type()
)
radiusServersTimeoutS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServersTimeoutS.setStatus("current")


class _RadiusUserAccessRights_Type(Integer32):
    """Custom type radiusUserAccessRights based on Integer32"""
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
        *(("admin", 100),
          ("user", 200),
          ("observer", 300))
    )


_RadiusUserAccessRights_Type.__name__ = "Integer32"
_RadiusUserAccessRights_Object = MibScalar
radiusUserAccessRights = _RadiusUserAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 200),
    _RadiusUserAccessRights_Type()
)
radiusUserAccessRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusUserAccessRights.setStatus("current")
_RadiusServersTable_Object = MibTable
radiusServersTable = _RadiusServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 1000)
)
if mibBuilder.loadTexts:
    radiusServersTable.setStatus("current")
_RadiusServersEntry_Object = MibTableRow
radiusServersEntry = _RadiusServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 1000, 1)
)
radiusServersEntry.setIndexNames(
    (0, "MX-AAA-MIB", "radiusServersService"),
    (0, "MX-AAA-MIB", "radiusServersPriority"),
)
if mibBuilder.loadTexts:
    radiusServersEntry.setStatus("current")
_RadiusServersService_Type = OctetString
_RadiusServersService_Object = MibTableColumn
radiusServersService = _RadiusServersService_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 1000, 1, 100),
    _RadiusServersService_Type()
)
radiusServersService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServersService.setStatus("current")
_RadiusServersPriority_Type = Unsigned32
_RadiusServersPriority_Object = MibTableColumn
radiusServersPriority = _RadiusServersPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 1000, 1, 200),
    _RadiusServersPriority_Type()
)
radiusServersPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServersPriority.setStatus("current")


class _RadiusServersAuthenticationHost_Type(MxIpHostNamePort):
    """Custom type radiusServersAuthenticationHost based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_RadiusServersAuthenticationHost_Type.__name__ = "MxIpHostNamePort"
_RadiusServersAuthenticationHost_Object = MibTableColumn
radiusServersAuthenticationHost = _RadiusServersAuthenticationHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 1000, 1, 300),
    _RadiusServersAuthenticationHost_Type()
)
radiusServersAuthenticationHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServersAuthenticationHost.setStatus("current")


class _RadiusServersAuthenticationSecret_Type(OctetString):
    """Custom type radiusServersAuthenticationSecret based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RadiusServersAuthenticationSecret_Type.__name__ = "OctetString"
_RadiusServersAuthenticationSecret_Object = MibTableColumn
radiusServersAuthenticationSecret = _RadiusServersAuthenticationSecret_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 1000, 1, 400),
    _RadiusServersAuthenticationSecret_Type()
)
radiusServersAuthenticationSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServersAuthenticationSecret.setStatus("current")


class _RadiusServersAccountingHost_Type(MxIpHostNamePort):
    """Custom type radiusServersAccountingHost based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_RadiusServersAccountingHost_Type.__name__ = "MxIpHostNamePort"
_RadiusServersAccountingHost_Object = MibTableColumn
radiusServersAccountingHost = _RadiusServersAccountingHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 1000, 1, 500),
    _RadiusServersAccountingHost_Type()
)
radiusServersAccountingHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServersAccountingHost.setStatus("current")


class _RadiusServersAccountingSecret_Type(OctetString):
    """Custom type radiusServersAccountingSecret based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RadiusServersAccountingSecret_Type.__name__ = "OctetString"
_RadiusServersAccountingSecret_Object = MibTableColumn
radiusServersAccountingSecret = _RadiusServersAccountingSecret_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 10000, 1000, 1, 600),
    _RadiusServersAccountingSecret_Type()
)
radiusServersAccountingSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServersAccountingSecret.setStatus("current")
_SecurityGroup_ObjectIdentity = ObjectIdentity
securityGroup = _SecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 20000)
)


class _LoginLockedMaxRetry_Type(Unsigned32):
    """Custom type loginLockedMaxRetry based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_LoginLockedMaxRetry_Type.__name__ = "Unsigned32"
_LoginLockedMaxRetry_Object = MibScalar
loginLockedMaxRetry = _LoginLockedMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 20000, 100),
    _LoginLockedMaxRetry_Type()
)
loginLockedMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginLockedMaxRetry.setStatus("current")


class _LoginLockedTimeoutS_Type(Unsigned32):
    """Custom type loginLockedTimeoutS based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_LoginLockedTimeoutS_Type.__name__ = "Unsigned32"
_LoginLockedTimeoutS_Object = MibScalar
loginLockedTimeoutS = _LoginLockedTimeoutS_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 20000, 200),
    _LoginLockedTimeoutS_Type()
)
loginLockedTimeoutS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginLockedTimeoutS.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1000, 1, 60020, 100),
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
    "MX-AAA-MIB",
    **{"aaaMIB": aaaMIB,
       "aaaMIBObjects": aaaMIBObjects,
       "usersTable": usersTable,
       "usersEntry": usersEntry,
       "usersUserName": usersUserName,
       "usersPassword": usersPassword,
       "usersAccessRights": usersAccessRights,
       "usersLockProtectionEnable": usersLockProtectionEnable,
       "usersDelete": usersDelete,
       "usersStatusTable": usersStatusTable,
       "usersStatusEntry": usersStatusEntry,
       "usersStatusUserName": usersStatusUserName,
       "usersStatusPassword": usersStatusPassword,
       "usersStatusLocked": usersStatusLocked,
       "batchUser": batchUser,
       "servicesAaaTypeTable": servicesAaaTypeTable,
       "servicesAaaTypeEntry": servicesAaaTypeEntry,
       "servicesAaaTypeService": servicesAaaTypeService,
       "servicesAaaTypeAuthenticationType": servicesAaaTypeAuthenticationType,
       "servicesAaaTypeAccountingType": servicesAaaTypeAccountingType,
       "radiusGroup": radiusGroup,
       "radiusServersTimeoutS": radiusServersTimeoutS,
       "radiusUserAccessRights": radiusUserAccessRights,
       "radiusServersTable": radiusServersTable,
       "radiusServersEntry": radiusServersEntry,
       "radiusServersService": radiusServersService,
       "radiusServersPriority": radiusServersPriority,
       "radiusServersAuthenticationHost": radiusServersAuthenticationHost,
       "radiusServersAuthenticationSecret": radiusServersAuthenticationSecret,
       "radiusServersAccountingHost": radiusServersAccountingHost,
       "radiusServersAccountingSecret": radiusServersAccountingSecret,
       "securityGroup": securityGroup,
       "loginLockedMaxRetry": loginLockedMaxRetry,
       "loginLockedTimeoutS": loginLockedTimeoutS,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
