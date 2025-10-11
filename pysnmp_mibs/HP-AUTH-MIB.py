# SNMP MIB module (HP-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-AUTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:32:54 2025
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ospfIfEntry,
 ospfVirtIfEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfIfEntry",
    "ospfVirtIfEntry")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpSwitchAuthenticationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16)
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIB.setRevisions(
        ("2021-11-11 00:00",
         "2020-09-07 00:00",
         "2020-06-15 00:00",
         "2019-06-10 00:00",
         "2019-02-27 00:00",
         "2019-01-14 00:00",
         "2018-12-14 00:00",
         "2018-12-12 00:00",
         "2018-12-05 00:00",
         "2018-11-29 00:00",
         "2018-11-12 00:00",
         "2018-09-07 00:00",
         "2018-08-06 00:00",
         "2018-07-19 00:00",
         "2018-07-18 00:00",
         "2018-05-29 00:00",
         "2018-04-27 00:00",
         "2018-02-21 00:00",
         "2018-01-16 00:00",
         "2017-11-22 00:00",
         "2017-09-28 00:00",
         "2017-05-25 00:00",
         "2017-03-16 00:00",
         "2017-01-19 00:00",
         "2016-11-21 00:00",
         "2016-11-11 00:00",
         "2016-07-29 00:00",
         "2016-06-27 00:00",
         "2016-02-23 00:00",
         "2016-01-22 00:00",
         "2015-10-28 00:00",
         "2015-07-02 00:00",
         "2015-05-24 00:00",
         "2015-04-01 00:00",
         "2015-03-16 00:00",
         "2014-08-04 00:00",
         "2014-03-12 00:00",
         "2013-11-12 00:00",
         "2013-06-12 00:00",
         "2013-05-27 00:00",
         "2012-05-11 00:00",
         "2012-05-01 00:00",
         "2011-06-02 00:00",
         "2011-02-12 00:00",
         "2011-02-07 00:00",
         "2009-06-06 00:00",
         "2009-06-03 00:00",
         "2009-04-02 00:00",
         "2009-02-27 00:00",
         "2009-01-29 00:00",
         "2008-07-11 00:00",
         "2008-06-11 00:00",
         "2007-09-21 00:00",
         "2006-10-05 00:00",
         "2004-09-12 00:00",
         "2004-03-31 00:12",
         "2001-08-10 02:38")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSwitchAuthNotifications_ObjectIdentity = ObjectIdentity
hpSwitchAuthNotifications = _HpSwitchAuthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 0)
)
_HpSwitchAuthenticationConfig_ObjectIdentity = ObjectIdentity
hpSwitchAuthenticationConfig = _HpSwitchAuthenticationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1)
)


class _HpSwitchNumLoginAttempts_Type(Integer32):
    """Custom type hpSwitchNumLoginAttempts based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpSwitchNumLoginAttempts_Type.__name__ = "Integer32"
_HpSwitchNumLoginAttempts_Object = MibScalar
hpSwitchNumLoginAttempts = _HpSwitchNumLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 1),
    _HpSwitchNumLoginAttempts_Type()
)
hpSwitchNumLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchNumLoginAttempts.setStatus("current")


class _HpSwitchAuthRespectPriv_Type(Integer32):
    """Custom type hpSwitchAuthRespectPriv based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpSwitchAuthRespectPriv_Type.__name__ = "Integer32"
_HpSwitchAuthRespectPriv_Object = MibScalar
hpSwitchAuthRespectPriv = _HpSwitchAuthRespectPriv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 2),
    _HpSwitchAuthRespectPriv_Type()
)
hpSwitchAuthRespectPriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthRespectPriv.setStatus("current")


class _HpSwitchAuthenticationEncryptCredentialsMethod_Type(Integer32):
    """Custom type hpSwitchAuthenticationEncryptCredentialsMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("aes256cbc", 1))
    )


_HpSwitchAuthenticationEncryptCredentialsMethod_Type.__name__ = "Integer32"
_HpSwitchAuthenticationEncryptCredentialsMethod_Object = MibScalar
hpSwitchAuthenticationEncryptCredentialsMethod = _HpSwitchAuthenticationEncryptCredentialsMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 3),
    _HpSwitchAuthenticationEncryptCredentialsMethod_Type()
)
hpSwitchAuthenticationEncryptCredentialsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenticationEncryptCredentialsMethod.setStatus("current")


class _HpSwitchAuthLockoutDelay_Type(Integer32):
    """Custom type hpSwitchAuthLockoutDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HpSwitchAuthLockoutDelay_Type.__name__ = "Integer32"
_HpSwitchAuthLockoutDelay_Object = MibScalar
hpSwitchAuthLockoutDelay = _HpSwitchAuthLockoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 4),
    _HpSwitchAuthLockoutDelay_Type()
)
hpSwitchAuthLockoutDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthLockoutDelay.setStatus("current")


class _HpSwitchMinimumPasswordLength_Type(Integer32):
    """Custom type hpSwitchMinimumPasswordLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HpSwitchMinimumPasswordLength_Type.__name__ = "Integer32"
_HpSwitchMinimumPasswordLength_Object = MibScalar
hpSwitchMinimumPasswordLength = _HpSwitchMinimumPasswordLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 5),
    _HpSwitchMinimumPasswordLength_Type()
)
hpSwitchMinimumPasswordLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchMinimumPasswordLength.setStatus("current")


class _HpSwitchAuthAllowVlanTagged_Type(TruthValue):
    """Custom type hpSwitchAuthAllowVlanTagged based on TruthValue"""
    defaultValue = 2


_HpSwitchAuthAllowVlanTagged_Type.__name__ = "TruthValue"
_HpSwitchAuthAllowVlanTagged_Object = MibScalar
hpSwitchAuthAllowVlanTagged = _HpSwitchAuthAllowVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 6),
    _HpSwitchAuthAllowVlanTagged_Type()
)
hpSwitchAuthAllowVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthAllowVlanTagged.setStatus("current")


class _HpSwitchAuthenHideSensitiveData_Type(Integer32):
    """Custom type hpSwitchAuthenHideSensitiveData based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthenHideSensitiveData_Type.__name__ = "Integer32"
_HpSwitchAuthenHideSensitiveData_Object = MibScalar
hpSwitchAuthenHideSensitiveData = _HpSwitchAuthenHideSensitiveData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 7),
    _HpSwitchAuthenHideSensitiveData_Type()
)
hpSwitchAuthenHideSensitiveData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenHideSensitiveData.setStatus("current")


class _HpSwitchAuthUnlockUser_Type(OctetString):
    """Custom type hpSwitchAuthUnlockUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpSwitchAuthUnlockUser_Type.__name__ = "OctetString"
_HpSwitchAuthUnlockUser_Object = MibScalar
hpSwitchAuthUnlockUser = _HpSwitchAuthUnlockUser_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 8),
    _HpSwitchAuthUnlockUser_Type()
)
hpSwitchAuthUnlockUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthUnlockUser.setStatus("current")


class _HpSwitchAuthUserBasedLockout_Type(Integer32):
    """Custom type hpSwitchAuthUserBasedLockout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthUserBasedLockout_Type.__name__ = "Integer32"
_HpSwitchAuthUserBasedLockout_Object = MibScalar
hpSwitchAuthUserBasedLockout = _HpSwitchAuthUserBasedLockout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 9),
    _HpSwitchAuthUserBasedLockout_Type()
)
hpSwitchAuthUserBasedLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthUserBasedLockout.setStatus("current")


class _HpSwitchAuthConsoleLockout_Type(Integer32):
    """Custom type hpSwitchAuthConsoleLockout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthConsoleLockout_Type.__name__ = "Integer32"
_HpSwitchAuthConsoleLockout_Object = MibScalar
hpSwitchAuthConsoleLockout = _HpSwitchAuthConsoleLockout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 10),
    _HpSwitchAuthConsoleLockout_Type()
)
hpSwitchAuthConsoleLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthConsoleLockout.setStatus("current")


class _HpSwitchTrackLoginAttempts_Type(Integer32):
    """Custom type hpSwitchTrackLoginAttempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_HpSwitchTrackLoginAttempts_Type.__name__ = "Integer32"
_HpSwitchTrackLoginAttempts_Object = MibScalar
hpSwitchTrackLoginAttempts = _HpSwitchTrackLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 1, 11),
    _HpSwitchTrackLoginAttempts_Type()
)
hpSwitchTrackLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTrackLoginAttempts.setStatus("current")
_HpSwitchAuthenTable_Object = MibTable
hpSwitchAuthenTable = _HpSwitchAuthenTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2)
)
if mibBuilder.loadTexts:
    hpSwitchAuthenTable.setStatus("current")
_HpSwitchAuthenEntry_Object = MibTableRow
hpSwitchAuthenEntry = _HpSwitchAuthenEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1)
)
hpSwitchAuthenEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpSwitchAuthenIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchAuthenEntry.setStatus("current")


class _HpSwitchAuthenIndex_Type(Integer32):
    """Custom type hpSwitchAuthenIndex based on Integer32"""
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
        *(("console", 1),
          ("telnet", 2),
          ("ieee8021X", 3),
          ("webui", 4),
          ("ssh", 5),
          ("webauth", 6),
          ("macauth", 7),
          ("snmp", 8),
          ("localMacAuth", 9),
          ("rest", 10))
    )


_HpSwitchAuthenIndex_Type.__name__ = "Integer32"
_HpSwitchAuthenIndex_Object = MibTableColumn
hpSwitchAuthenIndex = _HpSwitchAuthenIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 1),
    _HpSwitchAuthenIndex_Type()
)
hpSwitchAuthenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAuthenIndex.setStatus("current")


class _HpSwitchAuthenLoginPrimary_Type(Integer32):
    """Custom type hpSwitchAuthenLoginPrimary based on Integer32"""
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
        *(("local", 1),
          ("tacacs", 2),
          ("radius", 3),
          ("radiusEap", 4),
          ("radiusChap", 5),
          ("sshRsa", 6),
          ("radiusPeapMSChapv2", 7),
          ("x509Certificate", 8),
          ("twoFactor", 9),
          ("radiusPap", 10))
    )


_HpSwitchAuthenLoginPrimary_Type.__name__ = "Integer32"
_HpSwitchAuthenLoginPrimary_Object = MibTableColumn
hpSwitchAuthenLoginPrimary = _HpSwitchAuthenLoginPrimary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 2),
    _HpSwitchAuthenLoginPrimary_Type()
)
hpSwitchAuthenLoginPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenLoginPrimary.setStatus("current")


class _HpSwitchAuthenLoginSecondary_Type(Integer32):
    """Custom type hpSwitchAuthenLoginSecondary based on Integer32"""
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
        *(("local", 1),
          ("none", 2),
          ("authorized", 3),
          ("cachedReauth", 4))
    )


_HpSwitchAuthenLoginSecondary_Type.__name__ = "Integer32"
_HpSwitchAuthenLoginSecondary_Object = MibTableColumn
hpSwitchAuthenLoginSecondary = _HpSwitchAuthenLoginSecondary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 3),
    _HpSwitchAuthenLoginSecondary_Type()
)
hpSwitchAuthenLoginSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenLoginSecondary.setStatus("current")


class _HpSwitchAuthenEnablePrimary_Type(Integer32):
    """Custom type hpSwitchAuthenEnablePrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("tacacs", 2),
          ("radius", 3),
          ("sshPubkey", 6),
          ("radiusPeapMSChapv2", 7),
          ("x509Certificate", 8),
          ("twoFactor", 9),
          ("radiusPap", 10))
    )


_HpSwitchAuthenEnablePrimary_Type.__name__ = "Integer32"
_HpSwitchAuthenEnablePrimary_Object = MibTableColumn
hpSwitchAuthenEnablePrimary = _HpSwitchAuthenEnablePrimary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 4),
    _HpSwitchAuthenEnablePrimary_Type()
)
hpSwitchAuthenEnablePrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenEnablePrimary.setStatus("current")


class _HpSwitchAuthenEnableSecondary_Type(Integer32):
    """Custom type hpSwitchAuthenEnableSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("none", 2),
          ("authorized", 3))
    )


_HpSwitchAuthenEnableSecondary_Type.__name__ = "Integer32"
_HpSwitchAuthenEnableSecondary_Object = MibTableColumn
hpSwitchAuthenEnableSecondary = _HpSwitchAuthenEnableSecondary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 5),
    _HpSwitchAuthenEnableSecondary_Type()
)
hpSwitchAuthenEnableSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenEnableSecondary.setStatus("current")


class _HpSwitchAuthenLoginServerGroupName_Type(DisplayString):
    """Custom type hpSwitchAuthenLoginServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchAuthenLoginServerGroupName_Type.__name__ = "DisplayString"
_HpSwitchAuthenLoginServerGroupName_Object = MibTableColumn
hpSwitchAuthenLoginServerGroupName = _HpSwitchAuthenLoginServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 6),
    _HpSwitchAuthenLoginServerGroupName_Type()
)
hpSwitchAuthenLoginServerGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenLoginServerGroupName.setStatus("current")


class _HpSwitchAuthenEnableServerGroupName_Type(DisplayString):
    """Custom type hpSwitchAuthenEnableServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchAuthenEnableServerGroupName_Type.__name__ = "DisplayString"
_HpSwitchAuthenEnableServerGroupName_Object = MibTableColumn
hpSwitchAuthenEnableServerGroupName = _HpSwitchAuthenEnableServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 7),
    _HpSwitchAuthenEnableServerGroupName_Type()
)
hpSwitchAuthenEnableServerGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenEnableServerGroupName.setStatus("current")


class _HpSwitchAuthenLoginTwoFactorType_Type(Integer32):
    """Custom type hpSwitchAuthenLoginTwoFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("publickeypassword", 1),
          ("certificatepassword", 2))
    )


_HpSwitchAuthenLoginTwoFactorType_Type.__name__ = "Integer32"
_HpSwitchAuthenLoginTwoFactorType_Object = MibTableColumn
hpSwitchAuthenLoginTwoFactorType = _HpSwitchAuthenLoginTwoFactorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 8),
    _HpSwitchAuthenLoginTwoFactorType_Type()
)
hpSwitchAuthenLoginTwoFactorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenLoginTwoFactorType.setStatus("current")


class _HpSwitchAuthenEnableTwoFactorType_Type(Integer32):
    """Custom type hpSwitchAuthenEnableTwoFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("publickeypassword", 1),
          ("certificatepassword", 2))
    )


_HpSwitchAuthenEnableTwoFactorType_Type.__name__ = "Integer32"
_HpSwitchAuthenEnableTwoFactorType_Object = MibTableColumn
hpSwitchAuthenEnableTwoFactorType = _HpSwitchAuthenEnableTwoFactorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 9),
    _HpSwitchAuthenEnableTwoFactorType_Type()
)
hpSwitchAuthenEnableTwoFactorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenEnableTwoFactorType.setStatus("current")


class _HpSwitchAuthenLoginSecondAuthMethod_Type(Integer32):
    """Custom type hpSwitchAuthenLoginSecondAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("tacacs", 2),
          ("radius", 3))
    )


_HpSwitchAuthenLoginSecondAuthMethod_Type.__name__ = "Integer32"
_HpSwitchAuthenLoginSecondAuthMethod_Object = MibTableColumn
hpSwitchAuthenLoginSecondAuthMethod = _HpSwitchAuthenLoginSecondAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 10),
    _HpSwitchAuthenLoginSecondAuthMethod_Type()
)
hpSwitchAuthenLoginSecondAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenLoginSecondAuthMethod.setStatus("current")


class _HpSwitchAuthenEnableSecondAuthMethod_Type(Integer32):
    """Custom type hpSwitchAuthenEnableSecondAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("tacacs", 2),
          ("radius", 3))
    )


_HpSwitchAuthenEnableSecondAuthMethod_Type.__name__ = "Integer32"
_HpSwitchAuthenEnableSecondAuthMethod_Object = MibTableColumn
hpSwitchAuthenEnableSecondAuthMethod = _HpSwitchAuthenEnableSecondAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 11),
    _HpSwitchAuthenEnableSecondAuthMethod_Type()
)
hpSwitchAuthenEnableSecondAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenEnableSecondAuthMethod.setStatus("current")


class _HpSwitchAuthenClientPrimary_Type(Integer32):
    """Custom type hpSwitchAuthenClientPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("x509Certificate", 1),
          ("none", 2))
    )


_HpSwitchAuthenClientPrimary_Type.__name__ = "Integer32"
_HpSwitchAuthenClientPrimary_Object = MibTableColumn
hpSwitchAuthenClientPrimary = _HpSwitchAuthenClientPrimary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 12),
    _HpSwitchAuthenClientPrimary_Type()
)
hpSwitchAuthenClientPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenClientPrimary.setStatus("current")


class _HpSwitchAuthenClientSecondary_Type(Integer32):
    """Custom type hpSwitchAuthenClientSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("none", 1)
    )


_HpSwitchAuthenClientSecondary_Type.__name__ = "Integer32"
_HpSwitchAuthenClientSecondary_Object = MibTableColumn
hpSwitchAuthenClientSecondary = _HpSwitchAuthenClientSecondary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 13),
    _HpSwitchAuthenClientSecondary_Type()
)
hpSwitchAuthenClientSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenClientSecondary.setStatus("current")
_HpSwitchAuthenCachedReauthAuthorized_Type = TruthValue
_HpSwitchAuthenCachedReauthAuthorized_Object = MibTableColumn
hpSwitchAuthenCachedReauthAuthorized = _HpSwitchAuthenCachedReauthAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 2, 1, 14),
    _HpSwitchAuthenCachedReauthAuthorized_Type()
)
hpSwitchAuthenCachedReauthAuthorized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenCachedReauthAuthorized.setStatus("current")
_HpSwitchTacacsConfig_ObjectIdentity = ObjectIdentity
hpSwitchTacacsConfig = _HpSwitchTacacsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 3)
)


class _HpSwitchTacacsTimeout_Type(Integer32):
    """Custom type hpSwitchTacacsTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpSwitchTacacsTimeout_Type.__name__ = "Integer32"
_HpSwitchTacacsTimeout_Object = MibScalar
hpSwitchTacacsTimeout = _HpSwitchTacacsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 3, 1),
    _HpSwitchTacacsTimeout_Type()
)
hpSwitchTacacsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTacacsTimeout.setStatus("current")


class _HpSwitchTacacsAuthKey_Type(OctetString):
    """Custom type hpSwitchTacacsAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HpSwitchTacacsAuthKey_Type.__name__ = "OctetString"
_HpSwitchTacacsAuthKey_Object = MibScalar
hpSwitchTacacsAuthKey = _HpSwitchTacacsAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 3, 2),
    _HpSwitchTacacsAuthKey_Type()
)
hpSwitchTacacsAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTacacsAuthKey.setStatus("current")


class _HpSwitchTacacsAuthKeyEncrypted_Type(OctetString):
    """Custom type hpSwitchTacacsAuthKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchTacacsAuthKeyEncrypted_Type.__name__ = "OctetString"
_HpSwitchTacacsAuthKeyEncrypted_Object = MibScalar
hpSwitchTacacsAuthKeyEncrypted = _HpSwitchTacacsAuthKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 3, 3),
    _HpSwitchTacacsAuthKeyEncrypted_Type()
)
hpSwitchTacacsAuthKeyEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTacacsAuthKeyEncrypted.setStatus("current")


class _HpSwitchTacacsDeadTime_Type(Integer32):
    """Custom type hpSwitchTacacsDeadTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_HpSwitchTacacsDeadTime_Type.__name__ = "Integer32"
_HpSwitchTacacsDeadTime_Object = MibScalar
hpSwitchTacacsDeadTime = _HpSwitchTacacsDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 3, 4),
    _HpSwitchTacacsDeadTime_Type()
)
hpSwitchTacacsDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTacacsDeadTime.setStatus("current")


class _HpSwitchTacacsOrderingSequence_Type(TruthValue):
    """Custom type hpSwitchTacacsOrderingSequence based on TruthValue"""
    defaultValue = 2


_HpSwitchTacacsOrderingSequence_Type.__name__ = "TruthValue"
_HpSwitchTacacsOrderingSequence_Object = MibScalar
hpSwitchTacacsOrderingSequence = _HpSwitchTacacsOrderingSequence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 3, 5),
    _HpSwitchTacacsOrderingSequence_Type()
)
hpSwitchTacacsOrderingSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTacacsOrderingSequence.setStatus("current")


class _HpSwitchTacacsServerFqdnRetry_Type(Integer32):
    """Custom type hpSwitchTacacsServerFqdnRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HpSwitchTacacsServerFqdnRetry_Type.__name__ = "Integer32"
_HpSwitchTacacsServerFqdnRetry_Object = MibScalar
hpSwitchTacacsServerFqdnRetry = _HpSwitchTacacsServerFqdnRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 3, 6),
    _HpSwitchTacacsServerFqdnRetry_Type()
)
hpSwitchTacacsServerFqdnRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerFqdnRetry.setStatus("current")
_HpSwitchTacacsServersTable_Object = MibTable
hpSwitchTacacsServersTable = _HpSwitchTacacsServersTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4)
)
if mibBuilder.loadTexts:
    hpSwitchTacacsServersTable.setStatus("current")
_HpSwitchTacacsServersEntry_Object = MibTableRow
hpSwitchTacacsServersEntry = _HpSwitchTacacsServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1)
)
hpSwitchTacacsServersEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpSwitchTacacsServerIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchTacacsServersEntry.setStatus("current")


class _HpSwitchTacacsServerIndex_Type(Integer32):
    """Custom type hpSwitchTacacsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchTacacsServerIndex_Type.__name__ = "Integer32"
_HpSwitchTacacsServerIndex_Object = MibTableColumn
hpSwitchTacacsServerIndex = _HpSwitchTacacsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1, 1),
    _HpSwitchTacacsServerIndex_Type()
)
hpSwitchTacacsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerIndex.setStatus("current")
_HpSwitchTacacsServerIpAddr_Type = IpAddress
_HpSwitchTacacsServerIpAddr_Object = MibTableColumn
hpSwitchTacacsServerIpAddr = _HpSwitchTacacsServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1, 2),
    _HpSwitchTacacsServerIpAddr_Type()
)
hpSwitchTacacsServerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerIpAddr.setStatus("current")


class _HpSwitchTacacsServerKey_Type(OctetString):
    """Custom type hpSwitchTacacsServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HpSwitchTacacsServerKey_Type.__name__ = "OctetString"
_HpSwitchTacacsServerKey_Object = MibTableColumn
hpSwitchTacacsServerKey = _HpSwitchTacacsServerKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1, 3),
    _HpSwitchTacacsServerKey_Type()
)
hpSwitchTacacsServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerKey.setStatus("current")
_HpSwitchTacacsServerStatus_Type = RowStatus
_HpSwitchTacacsServerStatus_Object = MibTableColumn
hpSwitchTacacsServerStatus = _HpSwitchTacacsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1, 4),
    _HpSwitchTacacsServerStatus_Type()
)
hpSwitchTacacsServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerStatus.setStatus("current")


class _HpSwitchTacacsServerIsOobm_Type(TruthValue):
    """Custom type hpSwitchTacacsServerIsOobm based on TruthValue"""
    defaultValue = 2


_HpSwitchTacacsServerIsOobm_Type.__name__ = "TruthValue"
_HpSwitchTacacsServerIsOobm_Object = MibTableColumn
hpSwitchTacacsServerIsOobm = _HpSwitchTacacsServerIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1, 5),
    _HpSwitchTacacsServerIsOobm_Type()
)
hpSwitchTacacsServerIsOobm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerIsOobm.setStatus("current")


class _HpSwitchTacacsServerKeyEncrypted_Type(OctetString):
    """Custom type hpSwitchTacacsServerKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchTacacsServerKeyEncrypted_Type.__name__ = "OctetString"
_HpSwitchTacacsServerKeyEncrypted_Object = MibTableColumn
hpSwitchTacacsServerKeyEncrypted = _HpSwitchTacacsServerKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1, 6),
    _HpSwitchTacacsServerKeyEncrypted_Type()
)
hpSwitchTacacsServerKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerKeyEncrypted.setStatus("current")
_HpSwitchTacacsServerAddressType_Type = InetAddressType
_HpSwitchTacacsServerAddressType_Object = MibTableColumn
hpSwitchTacacsServerAddressType = _HpSwitchTacacsServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1, 7),
    _HpSwitchTacacsServerAddressType_Type()
)
hpSwitchTacacsServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerAddressType.setStatus("current")
_HpSwitchTacacsServerAddress_Type = InetAddress
_HpSwitchTacacsServerAddress_Object = MibTableColumn
hpSwitchTacacsServerAddress = _HpSwitchTacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1, 8),
    _HpSwitchTacacsServerAddress_Type()
)
hpSwitchTacacsServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerAddress.setStatus("current")


class _HpSwitchTacacsServerFqdn_Type(DisplayString):
    """Custom type hpSwitchTacacsServerFqdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpSwitchTacacsServerFqdn_Type.__name__ = "DisplayString"
_HpSwitchTacacsServerFqdn_Object = MibTableColumn
hpSwitchTacacsServerFqdn = _HpSwitchTacacsServerFqdn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 4, 1, 9),
    _HpSwitchTacacsServerFqdn_Type()
)
hpSwitchTacacsServerFqdn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTacacsServerFqdn.setStatus("current")
_HpTacacsStatsServersTable_Object = MibTable
hpTacacsStatsServersTable = _HpTacacsStatsServersTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5)
)
if mibBuilder.loadTexts:
    hpTacacsStatsServersTable.setStatus("current")
_HpTacacsStatsServersEntry_Object = MibTableRow
hpTacacsStatsServersEntry = _HpTacacsStatsServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1)
)
hpTacacsStatsServersEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpTacacsStatsServerIndex"),
)
if mibBuilder.loadTexts:
    hpTacacsStatsServersEntry.setStatus("current")


class _HpTacacsStatsServerIndex_Type(Integer32):
    """Custom type hpTacacsStatsServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpTacacsStatsServerIndex_Type.__name__ = "Integer32"
_HpTacacsStatsServerIndex_Object = MibTableColumn
hpTacacsStatsServerIndex = _HpTacacsStatsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 1),
    _HpTacacsStatsServerIndex_Type()
)
hpTacacsStatsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpTacacsStatsServerIndex.setStatus("current")
_HpTacacsStatsTacacsServerIpAddr_Type = IpAddress
_HpTacacsStatsTacacsServerIpAddr_Object = MibTableColumn
hpTacacsStatsTacacsServerIpAddr = _HpTacacsStatsTacacsServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 2),
    _HpTacacsStatsTacacsServerIpAddr_Type()
)
hpTacacsStatsTacacsServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsTacacsServerIpAddr.setStatus("current")
_HpTacacsStatsNumSessOpened_Type = Counter32
_HpTacacsStatsNumSessOpened_Object = MibTableColumn
hpTacacsStatsNumSessOpened = _HpTacacsStatsNumSessOpened_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 3),
    _HpTacacsStatsNumSessOpened_Type()
)
hpTacacsStatsNumSessOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumSessOpened.setStatus("current")
_HpTacacsStatsNumSessClosed_Type = Counter32
_HpTacacsStatsNumSessClosed_Object = MibTableColumn
hpTacacsStatsNumSessClosed = _HpTacacsStatsNumSessClosed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 4),
    _HpTacacsStatsNumSessClosed_Type()
)
hpTacacsStatsNumSessClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumSessClosed.setStatus("current")
_HpTacacsStatsNumSessAborted_Type = Counter32
_HpTacacsStatsNumSessAborted_Object = MibTableColumn
hpTacacsStatsNumSessAborted = _HpTacacsStatsNumSessAborted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 5),
    _HpTacacsStatsNumSessAborted_Type()
)
hpTacacsStatsNumSessAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumSessAborted.setStatus("current")
_HpTacacsStatsNumSessErrors_Type = Counter32
_HpTacacsStatsNumSessErrors_Object = MibTableColumn
hpTacacsStatsNumSessErrors = _HpTacacsStatsNumSessErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 6),
    _HpTacacsStatsNumSessErrors_Type()
)
hpTacacsStatsNumSessErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumSessErrors.setStatus("current")
_HpTacacsStatsNumPktsIn_Type = Counter32
_HpTacacsStatsNumPktsIn_Object = MibTableColumn
hpTacacsStatsNumPktsIn = _HpTacacsStatsNumPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 7),
    _HpTacacsStatsNumPktsIn_Type()
)
hpTacacsStatsNumPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumPktsIn.setStatus("current")
_HpTacacsStatsNumPktsOut_Type = Counter32
_HpTacacsStatsNumPktsOut_Object = MibTableColumn
hpTacacsStatsNumPktsOut = _HpTacacsStatsNumPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 8),
    _HpTacacsStatsNumPktsOut_Type()
)
hpTacacsStatsNumPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumPktsOut.setStatus("current")
_HpTacacsStatsNumAuthPktsIn_Type = Counter32
_HpTacacsStatsNumAuthPktsIn_Object = MibTableColumn
hpTacacsStatsNumAuthPktsIn = _HpTacacsStatsNumAuthPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 9),
    _HpTacacsStatsNumAuthPktsIn_Type()
)
hpTacacsStatsNumAuthPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumAuthPktsIn.setStatus("current")
_HpTacacsStatsNumAuthPktsOut_Type = Counter32
_HpTacacsStatsNumAuthPktsOut_Object = MibTableColumn
hpTacacsStatsNumAuthPktsOut = _HpTacacsStatsNumAuthPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 10),
    _HpTacacsStatsNumAuthPktsOut_Type()
)
hpTacacsStatsNumAuthPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumAuthPktsOut.setStatus("current")
_HpTacacsStatsNumAuthPktsTimedOut_Type = Counter32
_HpTacacsStatsNumAuthPktsTimedOut_Object = MibTableColumn
hpTacacsStatsNumAuthPktsTimedOut = _HpTacacsStatsNumAuthPktsTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 11),
    _HpTacacsStatsNumAuthPktsTimedOut_Type()
)
hpTacacsStatsNumAuthPktsTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumAuthPktsTimedOut.setStatus("current")
_HpTacacsStatsNumAutzPktsIn_Type = Counter32
_HpTacacsStatsNumAutzPktsIn_Object = MibTableColumn
hpTacacsStatsNumAutzPktsIn = _HpTacacsStatsNumAutzPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 12),
    _HpTacacsStatsNumAutzPktsIn_Type()
)
hpTacacsStatsNumAutzPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumAutzPktsIn.setStatus("current")
_HpTacacsStatsNumAutzPktsOut_Type = Counter32
_HpTacacsStatsNumAutzPktsOut_Object = MibTableColumn
hpTacacsStatsNumAutzPktsOut = _HpTacacsStatsNumAutzPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 13),
    _HpTacacsStatsNumAutzPktsOut_Type()
)
hpTacacsStatsNumAutzPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumAutzPktsOut.setStatus("current")
_HpTacacsStatsNumAutzPktsTimedOut_Type = Counter32
_HpTacacsStatsNumAutzPktsTimedOut_Object = MibTableColumn
hpTacacsStatsNumAutzPktsTimedOut = _HpTacacsStatsNumAutzPktsTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 14),
    _HpTacacsStatsNumAutzPktsTimedOut_Type()
)
hpTacacsStatsNumAutzPktsTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumAutzPktsTimedOut.setStatus("current")
_HpTacacsStatsNumAcctPktsIn_Type = Counter32
_HpTacacsStatsNumAcctPktsIn_Object = MibTableColumn
hpTacacsStatsNumAcctPktsIn = _HpTacacsStatsNumAcctPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 15),
    _HpTacacsStatsNumAcctPktsIn_Type()
)
hpTacacsStatsNumAcctPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumAcctPktsIn.setStatus("current")
_HpTacacsStatsNumAcctPktsOut_Type = Counter32
_HpTacacsStatsNumAcctPktsOut_Object = MibTableColumn
hpTacacsStatsNumAcctPktsOut = _HpTacacsStatsNumAcctPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 16),
    _HpTacacsStatsNumAcctPktsOut_Type()
)
hpTacacsStatsNumAcctPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumAcctPktsOut.setStatus("current")
_HpTacacsStatsNumAcctPktsTimedOut_Type = Counter32
_HpTacacsStatsNumAcctPktsTimedOut_Object = MibTableColumn
hpTacacsStatsNumAcctPktsTimedOut = _HpTacacsStatsNumAcctPktsTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 17),
    _HpTacacsStatsNumAcctPktsTimedOut_Type()
)
hpTacacsStatsNumAcctPktsTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsNumAcctPktsTimedOut.setStatus("current")
_HpTacacsStatsTacacsServerAdrType_Type = InetAddressType
_HpTacacsStatsTacacsServerAdrType_Object = MibTableColumn
hpTacacsStatsTacacsServerAdrType = _HpTacacsStatsTacacsServerAdrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 18),
    _HpTacacsStatsTacacsServerAdrType_Type()
)
hpTacacsStatsTacacsServerAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsTacacsServerAdrType.setStatus("current")
_HpTacacsStatsTacacsServerAddr_Type = InetAddress
_HpTacacsStatsTacacsServerAddr_Object = MibTableColumn
hpTacacsStatsTacacsServerAddr = _HpTacacsStatsTacacsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 5, 1, 19),
    _HpTacacsStatsTacacsServerAddr_Type()
)
hpTacacsStatsTacacsServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTacacsStatsTacacsServerAddr.setStatus("current")
_HpSwitchRadiusConfig_ObjectIdentity = ObjectIdentity
hpSwitchRadiusConfig = _HpSwitchRadiusConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6)
)


class _HpSwitchRadiusDeadTime_Type(Integer32):
    """Custom type hpSwitchRadiusDeadTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_HpSwitchRadiusDeadTime_Type.__name__ = "Integer32"
_HpSwitchRadiusDeadTime_Object = MibScalar
hpSwitchRadiusDeadTime = _HpSwitchRadiusDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 1),
    _HpSwitchRadiusDeadTime_Type()
)
hpSwitchRadiusDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusDeadTime.setStatus("current")


class _HpSwitchRadiusTimeout_Type(Integer32):
    """Custom type hpSwitchRadiusTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpSwitchRadiusTimeout_Type.__name__ = "Integer32"
_HpSwitchRadiusTimeout_Object = MibScalar
hpSwitchRadiusTimeout = _HpSwitchRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 2),
    _HpSwitchRadiusTimeout_Type()
)
hpSwitchRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTimeout.setStatus("current")


class _HpSwitchRadiusRetransmitAttempts_Type(Integer32):
    """Custom type hpSwitchRadiusRetransmitAttempts based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HpSwitchRadiusRetransmitAttempts_Type.__name__ = "Integer32"
_HpSwitchRadiusRetransmitAttempts_Object = MibScalar
hpSwitchRadiusRetransmitAttempts = _HpSwitchRadiusRetransmitAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 3),
    _HpSwitchRadiusRetransmitAttempts_Type()
)
hpSwitchRadiusRetransmitAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusRetransmitAttempts.setStatus("current")


class _HpSwitchRadiusAuthKey_Type(OctetString):
    """Custom type hpSwitchRadiusAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HpSwitchRadiusAuthKey_Type.__name__ = "OctetString"
_HpSwitchRadiusAuthKey_Object = MibScalar
hpSwitchRadiusAuthKey = _HpSwitchRadiusAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 4),
    _HpSwitchRadiusAuthKey_Type()
)
hpSwitchRadiusAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusAuthKey.setStatus("current")


class _HpSwitchRadiusDynAutzPortNumber_Type(Integer32):
    """Custom type hpSwitchRadiusDynAutzPortNumber based on Integer32"""
    defaultValue = 3799

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchRadiusDynAutzPortNumber_Type.__name__ = "Integer32"
_HpSwitchRadiusDynAutzPortNumber_Object = MibScalar
hpSwitchRadiusDynAutzPortNumber = _HpSwitchRadiusDynAutzPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 5),
    _HpSwitchRadiusDynAutzPortNumber_Type()
)
hpSwitchRadiusDynAutzPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusDynAutzPortNumber.setStatus("current")


class _HpSwitchRadiusAuthKeyEncrypted_Type(OctetString):
    """Custom type hpSwitchRadiusAuthKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchRadiusAuthKeyEncrypted_Type.__name__ = "OctetString"
_HpSwitchRadiusAuthKeyEncrypted_Object = MibScalar
hpSwitchRadiusAuthKeyEncrypted = _HpSwitchRadiusAuthKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 6),
    _HpSwitchRadiusAuthKeyEncrypted_Type()
)
hpSwitchRadiusAuthKeyEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusAuthKeyEncrypted.setStatus("current")


class _HpSwitchRadiusTracking_Type(TruthValue):
    """Custom type hpSwitchRadiusTracking based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusTracking_Type.__name__ = "TruthValue"
_HpSwitchRadiusTracking_Object = MibScalar
hpSwitchRadiusTracking = _HpSwitchRadiusTracking_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 10),
    _HpSwitchRadiusTracking_Type()
)
hpSwitchRadiusTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTracking.setStatus("current")


class _HpSwitchRadiusTrackingUserName_Type(DisplayString):
    """Custom type hpSwitchRadiusTrackingUserName based on DisplayString"""
    defaultValue = OctetString("radius-tracking-user")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpSwitchRadiusTrackingUserName_Type.__name__ = "DisplayString"
_HpSwitchRadiusTrackingUserName_Object = MibScalar
hpSwitchRadiusTrackingUserName = _HpSwitchRadiusTrackingUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 11),
    _HpSwitchRadiusTrackingUserName_Type()
)
hpSwitchRadiusTrackingUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTrackingUserName.setStatus("current")


class _HpSwitchRadiusCppmIdentity_Type(DisplayString):
    """Custom type hpSwitchRadiusCppmIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchRadiusCppmIdentity_Type.__name__ = "DisplayString"
_HpSwitchRadiusCppmIdentity_Object = MibScalar
hpSwitchRadiusCppmIdentity = _HpSwitchRadiusCppmIdentity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 12),
    _HpSwitchRadiusCppmIdentity_Type()
)
hpSwitchRadiusCppmIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusCppmIdentity.setStatus("current")


class _HpSwitchRadiusCppmKey_Type(DisplayString):
    """Custom type hpSwitchRadiusCppmKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 64),
    )


_HpSwitchRadiusCppmKey_Type.__name__ = "DisplayString"
_HpSwitchRadiusCppmKey_Object = MibScalar
hpSwitchRadiusCppmKey = _HpSwitchRadiusCppmKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 13),
    _HpSwitchRadiusCppmKey_Type()
)
hpSwitchRadiusCppmKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusCppmKey.setStatus("current")


class _HpSwitchRadiusCppmEncryptedKey_Type(DisplayString):
    """Custom type hpSwitchRadiusCppmEncryptedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchRadiusCppmEncryptedKey_Type.__name__ = "DisplayString"
_HpSwitchRadiusCppmEncryptedKey_Object = MibScalar
hpSwitchRadiusCppmEncryptedKey = _HpSwitchRadiusCppmEncryptedKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 14),
    _HpSwitchRadiusCppmEncryptedKey_Type()
)
hpSwitchRadiusCppmEncryptedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusCppmEncryptedKey.setStatus("current")


class _HpSwitchRadiusDeadTimeInfinite_Type(TruthValue):
    """Custom type hpSwitchRadiusDeadTimeInfinite based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusDeadTimeInfinite_Type.__name__ = "TruthValue"
_HpSwitchRadiusDeadTimeInfinite_Object = MibScalar
hpSwitchRadiusDeadTimeInfinite = _HpSwitchRadiusDeadTimeInfinite_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 15),
    _HpSwitchRadiusDeadTimeInfinite_Type()
)
hpSwitchRadiusDeadTimeInfinite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusDeadTimeInfinite.setStatus("current")


class _HpSwitchRadiusTrackingInterval_Type(Integer32):
    """Custom type hpSwitchRadiusTrackingInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_HpSwitchRadiusTrackingInterval_Type.__name__ = "Integer32"
_HpSwitchRadiusTrackingInterval_Object = MibScalar
hpSwitchRadiusTrackingInterval = _HpSwitchRadiusTrackingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 16),
    _HpSwitchRadiusTrackingInterval_Type()
)
hpSwitchRadiusTrackingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTrackingInterval.setStatus("current")


class _HpSwitchRadiusTrackingPassword_Type(DisplayString):
    """Custom type hpSwitchRadiusTrackingPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpSwitchRadiusTrackingPassword_Type.__name__ = "DisplayString"
_HpSwitchRadiusTrackingPassword_Object = MibScalar
hpSwitchRadiusTrackingPassword = _HpSwitchRadiusTrackingPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 17),
    _HpSwitchRadiusTrackingPassword_Type()
)
hpSwitchRadiusTrackingPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTrackingPassword.setStatus("current")


class _HpSwitchRadiusTrackDeadOnly_Type(TruthValue):
    """Custom type hpSwitchRadiusTrackDeadOnly based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusTrackDeadOnly_Type.__name__ = "TruthValue"
_HpSwitchRadiusTrackDeadOnly_Object = MibScalar
hpSwitchRadiusTrackDeadOnly = _HpSwitchRadiusTrackDeadOnly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 18),
    _HpSwitchRadiusTrackDeadOnly_Type()
)
hpSwitchRadiusTrackDeadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTrackDeadOnly.setStatus("current")


class _HpSwitchRadiusTrackReqPktCount_Type(Integer32):
    """Custom type hpSwitchRadiusTrackReqPktCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HpSwitchRadiusTrackReqPktCount_Type.__name__ = "Integer32"
_HpSwitchRadiusTrackReqPktCount_Object = MibScalar
hpSwitchRadiusTrackReqPktCount = _HpSwitchRadiusTrackReqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 19),
    _HpSwitchRadiusTrackReqPktCount_Type()
)
hpSwitchRadiusTrackReqPktCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTrackReqPktCount.setStatus("current")


class _HpSwitchRadiusTrackPassEncrypt_Type(DisplayString):
    """Custom type hpSwitchRadiusTrackPassEncrypt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchRadiusTrackPassEncrypt_Type.__name__ = "DisplayString"
_HpSwitchRadiusTrackPassEncrypt_Object = MibScalar
hpSwitchRadiusTrackPassEncrypt = _HpSwitchRadiusTrackPassEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 20),
    _HpSwitchRadiusTrackPassEncrypt_Type()
)
hpSwitchRadiusTrackPassEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTrackPassEncrypt.setStatus("current")


class _HpSwitchRadiusFramedIpv4Address_Type(TruthValue):
    """Custom type hpSwitchRadiusFramedIpv4Address based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusFramedIpv4Address_Type.__name__ = "TruthValue"
_HpSwitchRadiusFramedIpv4Address_Object = MibScalar
hpSwitchRadiusFramedIpv4Address = _HpSwitchRadiusFramedIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 21),
    _HpSwitchRadiusFramedIpv4Address_Type()
)
hpSwitchRadiusFramedIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusFramedIpv4Address.setStatus("current")


class _HpSwitchRadiusFqdnRetry_Type(Integer32):
    """Custom type hpSwitchRadiusFqdnRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HpSwitchRadiusFqdnRetry_Type.__name__ = "Integer32"
_HpSwitchRadiusFqdnRetry_Object = MibScalar
hpSwitchRadiusFqdnRetry = _HpSwitchRadiusFqdnRetry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 22),
    _HpSwitchRadiusFqdnRetry_Type()
)
hpSwitchRadiusFqdnRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusFqdnRetry.setStatus("current")


class _HpSwitchRadiusExcludeVsa_Type(TruthValue):
    """Custom type hpSwitchRadiusExcludeVsa based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusExcludeVsa_Type.__name__ = "TruthValue"
_HpSwitchRadiusExcludeVsa_Object = MibScalar
hpSwitchRadiusExcludeVsa = _HpSwitchRadiusExcludeVsa_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 23),
    _HpSwitchRadiusExcludeVsa_Type()
)
hpSwitchRadiusExcludeVsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusExcludeVsa.setStatus("current")


class _HpSwitchRadiusTLSTimeout_Type(Integer32):
    """Custom type hpSwitchRadiusTLSTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 240),
    )


_HpSwitchRadiusTLSTimeout_Type.__name__ = "Integer32"
_HpSwitchRadiusTLSTimeout_Object = MibScalar
hpSwitchRadiusTLSTimeout = _HpSwitchRadiusTLSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 24),
    _HpSwitchRadiusTLSTimeout_Type()
)
hpSwitchRadiusTLSTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTLSTimeout.setStatus("current")


class _HpSwitchRadiusTLSConnectionTimeout_Type(Integer32):
    """Custom type hpSwitchRadiusTLSConnectionTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_HpSwitchRadiusTLSConnectionTimeout_Type.__name__ = "Integer32"
_HpSwitchRadiusTLSConnectionTimeout_Object = MibScalar
hpSwitchRadiusTLSConnectionTimeout = _HpSwitchRadiusTLSConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 25),
    _HpSwitchRadiusTLSConnectionTimeout_Type()
)
hpSwitchRadiusTLSConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTLSConnectionTimeout.setStatus("current")


class _HpSwitchRadiusTLSDeadTime_Type(Integer32):
    """Custom type hpSwitchRadiusTLSDeadTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_HpSwitchRadiusTLSDeadTime_Type.__name__ = "Integer32"
_HpSwitchRadiusTLSDeadTime_Object = MibScalar
hpSwitchRadiusTLSDeadTime = _HpSwitchRadiusTLSDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 26),
    _HpSwitchRadiusTLSDeadTime_Type()
)
hpSwitchRadiusTLSDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTLSDeadTime.setStatus("current")


class _HpSwitchRadiusTLSDeadTimeInfinite_Type(TruthValue):
    """Custom type hpSwitchRadiusTLSDeadTimeInfinite based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusTLSDeadTimeInfinite_Type.__name__ = "TruthValue"
_HpSwitchRadiusTLSDeadTimeInfinite_Object = MibScalar
hpSwitchRadiusTLSDeadTimeInfinite = _HpSwitchRadiusTLSDeadTimeInfinite_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 27),
    _HpSwitchRadiusTLSDeadTimeInfinite_Type()
)
hpSwitchRadiusTLSDeadTimeInfinite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTLSDeadTimeInfinite.setStatus("current")


class _HpSwitchRadiusTunnelPrivateGroupId_Type(Integer32):
    """Custom type hpSwitchRadiusTunnelPrivateGroupId based on Integer32"""
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
        *(("disable", 0),
          ("static", 1),
          ("dynamic", 2))
    )


_HpSwitchRadiusTunnelPrivateGroupId_Type.__name__ = "Integer32"
_HpSwitchRadiusTunnelPrivateGroupId_Object = MibScalar
hpSwitchRadiusTunnelPrivateGroupId = _HpSwitchRadiusTunnelPrivateGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 6, 28),
    _HpSwitchRadiusTunnelPrivateGroupId_Type()
)
hpSwitchRadiusTunnelPrivateGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRadiusTunnelPrivateGroupId.setStatus("current")
_HpSwitchRadiusServerTable_Object = MibTable
hpSwitchRadiusServerTable = _HpSwitchRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7)
)
if mibBuilder.loadTexts:
    hpSwitchRadiusServerTable.setStatus("current")
_HpSwitchRadiusServerEntry_Object = MibTableRow
hpSwitchRadiusServerEntry = _HpSwitchRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1)
)
hpSwitchRadiusServerEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpSwitchRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchRadiusServerEntry.setStatus("current")


class _HpSwitchRadiusServerIndex_Type(Integer32):
    """Custom type hpSwitchRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchRadiusServerIndex_Type.__name__ = "Integer32"
_HpSwitchRadiusServerIndex_Object = MibTableColumn
hpSwitchRadiusServerIndex = _HpSwitchRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 1),
    _HpSwitchRadiusServerIndex_Type()
)
hpSwitchRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerIndex.setStatus("current")
_HpSwitchRadiusServerIpAddr_Type = IpAddress
_HpSwitchRadiusServerIpAddr_Object = MibTableColumn
hpSwitchRadiusServerIpAddr = _HpSwitchRadiusServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 2),
    _HpSwitchRadiusServerIpAddr_Type()
)
hpSwitchRadiusServerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerIpAddr.setStatus("deprecated")


class _HpSwitchRadiusServerKey_Type(OctetString):
    """Custom type hpSwitchRadiusServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HpSwitchRadiusServerKey_Type.__name__ = "OctetString"
_HpSwitchRadiusServerKey_Object = MibTableColumn
hpSwitchRadiusServerKey = _HpSwitchRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 3),
    _HpSwitchRadiusServerKey_Type()
)
hpSwitchRadiusServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerKey.setStatus("current")


class _HpSwitchRadiusServerAuthPortNumber_Type(Integer32):
    """Custom type hpSwitchRadiusServerAuthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchRadiusServerAuthPortNumber_Type.__name__ = "Integer32"
_HpSwitchRadiusServerAuthPortNumber_Object = MibTableColumn
hpSwitchRadiusServerAuthPortNumber = _HpSwitchRadiusServerAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 4),
    _HpSwitchRadiusServerAuthPortNumber_Type()
)
hpSwitchRadiusServerAuthPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerAuthPortNumber.setStatus("current")


class _HpSwitchRadiusServerAcctPortNumber_Type(Integer32):
    """Custom type hpSwitchRadiusServerAcctPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchRadiusServerAcctPortNumber_Type.__name__ = "Integer32"
_HpSwitchRadiusServerAcctPortNumber_Object = MibTableColumn
hpSwitchRadiusServerAcctPortNumber = _HpSwitchRadiusServerAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 5),
    _HpSwitchRadiusServerAcctPortNumber_Type()
)
hpSwitchRadiusServerAcctPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerAcctPortNumber.setStatus("current")


class _HpSwitchRadiusServerDynAutzEnabled_Type(TruthValue):
    """Custom type hpSwitchRadiusServerDynAutzEnabled based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusServerDynAutzEnabled_Type.__name__ = "TruthValue"
_HpSwitchRadiusServerDynAutzEnabled_Object = MibTableColumn
hpSwitchRadiusServerDynAutzEnabled = _HpSwitchRadiusServerDynAutzEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 6),
    _HpSwitchRadiusServerDynAutzEnabled_Type()
)
hpSwitchRadiusServerDynAutzEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerDynAutzEnabled.setStatus("current")


class _HpSwitchRadiusServerDynAutzTimeWindow_Type(Integer32):
    """Custom type hpSwitchRadiusServerDynAutzTimeWindow based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchRadiusServerDynAutzTimeWindow_Type.__name__ = "Integer32"
_HpSwitchRadiusServerDynAutzTimeWindow_Object = MibTableColumn
hpSwitchRadiusServerDynAutzTimeWindow = _HpSwitchRadiusServerDynAutzTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 7),
    _HpSwitchRadiusServerDynAutzTimeWindow_Type()
)
hpSwitchRadiusServerDynAutzTimeWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerDynAutzTimeWindow.setStatus("current")
_HpSwitchRadiusServerStatus_Type = RowStatus
_HpSwitchRadiusServerStatus_Object = MibTableColumn
hpSwitchRadiusServerStatus = _HpSwitchRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 8),
    _HpSwitchRadiusServerStatus_Type()
)
hpSwitchRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerStatus.setStatus("current")


class _HpSwitchRadiusServerIsOobm_Type(TruthValue):
    """Custom type hpSwitchRadiusServerIsOobm based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusServerIsOobm_Type.__name__ = "TruthValue"
_HpSwitchRadiusServerIsOobm_Object = MibTableColumn
hpSwitchRadiusServerIsOobm = _HpSwitchRadiusServerIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 9),
    _HpSwitchRadiusServerIsOobm_Type()
)
hpSwitchRadiusServerIsOobm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerIsOobm.setStatus("current")


class _HpSwitchRadiusServerKeyEncrypted_Type(OctetString):
    """Custom type hpSwitchRadiusServerKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchRadiusServerKeyEncrypted_Type.__name__ = "OctetString"
_HpSwitchRadiusServerKeyEncrypted_Object = MibTableColumn
hpSwitchRadiusServerKeyEncrypted = _HpSwitchRadiusServerKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 10),
    _HpSwitchRadiusServerKeyEncrypted_Type()
)
hpSwitchRadiusServerKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerKeyEncrypted.setStatus("current")
_HpSwitchRadiusServerAddrType_Type = InetAddressType
_HpSwitchRadiusServerAddrType_Object = MibTableColumn
hpSwitchRadiusServerAddrType = _HpSwitchRadiusServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 11),
    _HpSwitchRadiusServerAddrType_Type()
)
hpSwitchRadiusServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerAddrType.setStatus("current")
_HpSwitchRadiusServerAddress_Type = InetAddress
_HpSwitchRadiusServerAddress_Object = MibTableColumn
hpSwitchRadiusServerAddress = _HpSwitchRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 12),
    _HpSwitchRadiusServerAddress_Type()
)
hpSwitchRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerAddress.setStatus("current")


class _HpSwitchRadiusServerDynAutzTimeWindowType_Type(Integer32):
    """Custom type hpSwitchRadiusServerDynAutzTimeWindowType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("positive", 0),
          ("plusorminus", 1))
    )


_HpSwitchRadiusServerDynAutzTimeWindowType_Type.__name__ = "Integer32"
_HpSwitchRadiusServerDynAutzTimeWindowType_Object = MibTableColumn
hpSwitchRadiusServerDynAutzTimeWindowType = _HpSwitchRadiusServerDynAutzTimeWindowType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 13),
    _HpSwitchRadiusServerDynAutzTimeWindowType_Type()
)
hpSwitchRadiusServerDynAutzTimeWindowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerDynAutzTimeWindowType.setStatus("current")


class _HpSwitchRadiusServerFqdn_Type(DisplayString):
    """Custom type hpSwitchRadiusServerFqdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpSwitchRadiusServerFqdn_Type.__name__ = "DisplayString"
_HpSwitchRadiusServerFqdn_Object = MibTableColumn
hpSwitchRadiusServerFqdn = _HpSwitchRadiusServerFqdn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 14),
    _HpSwitchRadiusServerFqdn_Type()
)
hpSwitchRadiusServerFqdn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerFqdn.setStatus("current")


class _HpSwitchRadiusServerIsClearPass_Type(TruthValue):
    """Custom type hpSwitchRadiusServerIsClearPass based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusServerIsClearPass_Type.__name__ = "TruthValue"
_HpSwitchRadiusServerIsClearPass_Object = MibTableColumn
hpSwitchRadiusServerIsClearPass = _HpSwitchRadiusServerIsClearPass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 15),
    _HpSwitchRadiusServerIsClearPass_Type()
)
hpSwitchRadiusServerIsClearPass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusServerIsClearPass.setStatus("current")


class _HpSwitchRadiusTLSEnable_Type(TruthValue):
    """Custom type hpSwitchRadiusTLSEnable based on TruthValue"""
    defaultValue = 2


_HpSwitchRadiusTLSEnable_Type.__name__ = "TruthValue"
_HpSwitchRadiusTLSEnable_Object = MibTableColumn
hpSwitchRadiusTLSEnable = _HpSwitchRadiusTLSEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 16),
    _HpSwitchRadiusTLSEnable_Type()
)
hpSwitchRadiusTLSEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusTLSEnable.setStatus("current")


class _HpSwitchRadiusTLSPort_Type(Integer32):
    """Custom type hpSwitchRadiusTLSPort based on Integer32"""
    defaultValue = 2083

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_HpSwitchRadiusTLSPort_Type.__name__ = "Integer32"
_HpSwitchRadiusTLSPort_Object = MibTableColumn
hpSwitchRadiusTLSPort = _HpSwitchRadiusTLSPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 17),
    _HpSwitchRadiusTLSPort_Type()
)
hpSwitchRadiusTLSPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRadiusTLSPort.setStatus("current")


class _HpSwitchRadiusTLSRetryTimer_Type(Integer32):
    """Custom type hpSwitchRadiusTLSRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchRadiusTLSRetryTimer_Type.__name__ = "Integer32"
_HpSwitchRadiusTLSRetryTimer_Object = MibTableColumn
hpSwitchRadiusTLSRetryTimer = _HpSwitchRadiusTLSRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 7, 1, 18),
    _HpSwitchRadiusTLSRetryTimer_Type()
)
hpSwitchRadiusTLSRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRadiusTLSRetryTimer.setStatus("current")
_HpSwitchAuthenticationMIBConformance_ObjectIdentity = ObjectIdentity
hpSwitchAuthenticationMIBConformance = _HpSwitchAuthenticationMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11)
)
_HpSwitchAuthenticationMIBCompliances_ObjectIdentity = ObjectIdentity
hpSwitchAuthenticationMIBCompliances = _HpSwitchAuthenticationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1)
)
_HpSwitchAuthenticationMIBGroups_ObjectIdentity = ObjectIdentity
hpSwitchAuthenticationMIBGroups = _HpSwitchAuthenticationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2)
)
_HpSwitchSslConfig_ObjectIdentity = ObjectIdentity
hpSwitchSslConfig = _HpSwitchSslConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 12)
)


class _HpSwitchSslAdminStatus_Type(Integer32):
    """Custom type hpSwitchSslAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpSwitchSslAdminStatus_Type.__name__ = "Integer32"
_HpSwitchSslAdminStatus_Object = MibScalar
hpSwitchSslAdminStatus = _HpSwitchSslAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 12, 1),
    _HpSwitchSslAdminStatus_Type()
)
hpSwitchSslAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSslAdminStatus.setStatus("current")


class _HpSwitchSslPortNumber_Type(Integer32):
    """Custom type hpSwitchSslPortNumber based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchSslPortNumber_Type.__name__ = "Integer32"
_HpSwitchSslPortNumber_Object = MibScalar
hpSwitchSslPortNumber = _HpSwitchSslPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 12, 2),
    _HpSwitchSslPortNumber_Type()
)
hpSwitchSslPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSslPortNumber.setStatus("current")
_HpSwitchCertConfig_ObjectIdentity = ObjectIdentity
hpSwitchCertConfig = _HpSwitchCertConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13)
)


class _HpSwitchServerCertificateOperation_Type(Integer32):
    """Custom type hpSwitchServerCertificateOperation based on Integer32"""
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
        *(("none", 1),
          ("useInstalled", 2),
          ("createAndUseSelfSigned", 3),
          ("createCACertReq", 4),
          ("applyCASignedCert", 5),
          ("abortCASignedRequest", 6))
    )


_HpSwitchServerCertificateOperation_Type.__name__ = "Integer32"
_HpSwitchServerCertificateOperation_Object = MibScalar
hpSwitchServerCertificateOperation = _HpSwitchServerCertificateOperation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 1),
    _HpSwitchServerCertificateOperation_Type()
)
hpSwitchServerCertificateOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateOperation.setStatus("current")


class _HpSwitchServerNewRSAKeyOperation_Type(Integer32):
    """Custom type hpSwitchServerNewRSAKeyOperation based on Integer32"""
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
        *(("useInstalled", 1),
          ("createBits512", 2),
          ("createBits768", 3),
          ("createBits1024", 4),
          ("createBits2048", 5))
    )


_HpSwitchServerNewRSAKeyOperation_Type.__name__ = "Integer32"
_HpSwitchServerNewRSAKeyOperation_Object = MibScalar
hpSwitchServerNewRSAKeyOperation = _HpSwitchServerNewRSAKeyOperation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 2),
    _HpSwitchServerNewRSAKeyOperation_Type()
)
hpSwitchServerNewRSAKeyOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewRSAKeyOperation.setStatus("current")
_HpSwitchServerNewCertificateStartDate_Type = DateAndTime
_HpSwitchServerNewCertificateStartDate_Object = MibScalar
hpSwitchServerNewCertificateStartDate = _HpSwitchServerNewCertificateStartDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 3),
    _HpSwitchServerNewCertificateStartDate_Type()
)
hpSwitchServerNewCertificateStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertificateStartDate.setStatus("current")
_HpSwitchServerNewCertificateEndDate_Type = DateAndTime
_HpSwitchServerNewCertificateEndDate_Object = MibScalar
hpSwitchServerNewCertificateEndDate = _HpSwitchServerNewCertificateEndDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 4),
    _HpSwitchServerNewCertificateEndDate_Type()
)
hpSwitchServerNewCertificateEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertificateEndDate.setStatus("current")


class _HpSwitchServerNewCertificateCommonName_Type(OctetString):
    """Custom type hpSwitchServerNewCertificateCommonName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_HpSwitchServerNewCertificateCommonName_Type.__name__ = "OctetString"
_HpSwitchServerNewCertificateCommonName_Object = MibScalar
hpSwitchServerNewCertificateCommonName = _HpSwitchServerNewCertificateCommonName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 5),
    _HpSwitchServerNewCertificateCommonName_Type()
)
hpSwitchServerNewCertificateCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertificateCommonName.setStatus("deprecated")


class _HpSwitchServerNewCertificateOrgUnit_Type(OctetString):
    """Custom type hpSwitchServerNewCertificateOrgUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_HpSwitchServerNewCertificateOrgUnit_Type.__name__ = "OctetString"
_HpSwitchServerNewCertificateOrgUnit_Object = MibScalar
hpSwitchServerNewCertificateOrgUnit = _HpSwitchServerNewCertificateOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 6),
    _HpSwitchServerNewCertificateOrgUnit_Type()
)
hpSwitchServerNewCertificateOrgUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertificateOrgUnit.setStatus("deprecated")


class _HpSwitchServerNewCertificateOrgName_Type(OctetString):
    """Custom type hpSwitchServerNewCertificateOrgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_HpSwitchServerNewCertificateOrgName_Type.__name__ = "OctetString"
_HpSwitchServerNewCertificateOrgName_Object = MibScalar
hpSwitchServerNewCertificateOrgName = _HpSwitchServerNewCertificateOrgName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 7),
    _HpSwitchServerNewCertificateOrgName_Type()
)
hpSwitchServerNewCertificateOrgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertificateOrgName.setStatus("deprecated")


class _HpSwitchServerNewCertificateCityName_Type(OctetString):
    """Custom type hpSwitchServerNewCertificateCityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_HpSwitchServerNewCertificateCityName_Type.__name__ = "OctetString"
_HpSwitchServerNewCertificateCityName_Object = MibScalar
hpSwitchServerNewCertificateCityName = _HpSwitchServerNewCertificateCityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 8),
    _HpSwitchServerNewCertificateCityName_Type()
)
hpSwitchServerNewCertificateCityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertificateCityName.setStatus("deprecated")


class _HpSwitchServerNewCertificateStateName_Type(OctetString):
    """Custom type hpSwitchServerNewCertificateStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_HpSwitchServerNewCertificateStateName_Type.__name__ = "OctetString"
_HpSwitchServerNewCertificateStateName_Object = MibScalar
hpSwitchServerNewCertificateStateName = _HpSwitchServerNewCertificateStateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 9),
    _HpSwitchServerNewCertificateStateName_Type()
)
hpSwitchServerNewCertificateStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertificateStateName.setStatus("deprecated")


class _HpSwitchServerNewCertificateCountryCode_Type(OctetString):
    """Custom type hpSwitchServerNewCertificateCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_HpSwitchServerNewCertificateCountryCode_Type.__name__ = "OctetString"
_HpSwitchServerNewCertificateCountryCode_Object = MibScalar
hpSwitchServerNewCertificateCountryCode = _HpSwitchServerNewCertificateCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 10),
    _HpSwitchServerNewCertificateCountryCode_Type()
)
hpSwitchServerNewCertificateCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertificateCountryCode.setStatus("current")


class _HpSwitchServerNewCertCommonName_Type(OctetString):
    """Custom type hpSwitchServerNewCertCommonName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HpSwitchServerNewCertCommonName_Type.__name__ = "OctetString"
_HpSwitchServerNewCertCommonName_Object = MibScalar
hpSwitchServerNewCertCommonName = _HpSwitchServerNewCertCommonName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 11),
    _HpSwitchServerNewCertCommonName_Type()
)
hpSwitchServerNewCertCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertCommonName.setStatus("current")


class _HpSwitchServerNewCertOrgUnit_Type(OctetString):
    """Custom type hpSwitchServerNewCertOrgUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HpSwitchServerNewCertOrgUnit_Type.__name__ = "OctetString"
_HpSwitchServerNewCertOrgUnit_Object = MibScalar
hpSwitchServerNewCertOrgUnit = _HpSwitchServerNewCertOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 12),
    _HpSwitchServerNewCertOrgUnit_Type()
)
hpSwitchServerNewCertOrgUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertOrgUnit.setStatus("current")


class _HpSwitchServerNewCertOrgName_Type(OctetString):
    """Custom type hpSwitchServerNewCertOrgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HpSwitchServerNewCertOrgName_Type.__name__ = "OctetString"
_HpSwitchServerNewCertOrgName_Object = MibScalar
hpSwitchServerNewCertOrgName = _HpSwitchServerNewCertOrgName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 13),
    _HpSwitchServerNewCertOrgName_Type()
)
hpSwitchServerNewCertOrgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertOrgName.setStatus("current")


class _HpSwitchServerNewCertCityName_Type(OctetString):
    """Custom type hpSwitchServerNewCertCityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HpSwitchServerNewCertCityName_Type.__name__ = "OctetString"
_HpSwitchServerNewCertCityName_Object = MibScalar
hpSwitchServerNewCertCityName = _HpSwitchServerNewCertCityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 14),
    _HpSwitchServerNewCertCityName_Type()
)
hpSwitchServerNewCertCityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertCityName.setStatus("current")


class _HpSwitchServerNewCertStateName_Type(OctetString):
    """Custom type hpSwitchServerNewCertStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HpSwitchServerNewCertStateName_Type.__name__ = "OctetString"
_HpSwitchServerNewCertStateName_Object = MibScalar
hpSwitchServerNewCertStateName = _HpSwitchServerNewCertStateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 15),
    _HpSwitchServerNewCertStateName_Type()
)
hpSwitchServerNewCertStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertStateName.setStatus("current")


class _HpSwitchServerNewCertKeySizeExists_Type(TruthValue):
    """Custom type hpSwitchServerNewCertKeySizeExists based on TruthValue"""
    defaultValue = 2


_HpSwitchServerNewCertKeySizeExists_Type.__name__ = "TruthValue"
_HpSwitchServerNewCertKeySizeExists_Object = MibScalar
hpSwitchServerNewCertKeySizeExists = _HpSwitchServerNewCertKeySizeExists_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 13, 16),
    _HpSwitchServerNewCertKeySizeExists_Type()
)
hpSwitchServerNewCertKeySizeExists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchServerNewCertKeySizeExists.setStatus("current")
_HpSwitchCertStatus_ObjectIdentity = ObjectIdentity
hpSwitchCertStatus = _HpSwitchCertStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14)
)


class _HpSwitchServerCertificateType_Type(Integer32):
    """Custom type hpSwitchServerCertificateType based on Integer32"""
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
          ("pendCaSigned", 2),
          ("selfSigned", 3),
          ("caSigned", 4))
    )


_HpSwitchServerCertificateType_Type.__name__ = "Integer32"
_HpSwitchServerCertificateType_Object = MibScalar
hpSwitchServerCertificateType = _HpSwitchServerCertificateType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 1),
    _HpSwitchServerCertificateType_Type()
)
hpSwitchServerCertificateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateType.setStatus("current")


class _HpSwitchServerCertificateRSAKeySize_Type(Integer32):
    """Custom type hpSwitchServerCertificateRSAKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("bits512", 1),
          ("bits768", 2),
          ("bits1024", 3),
          ("bits2048", 4))
    )


_HpSwitchServerCertificateRSAKeySize_Type.__name__ = "Integer32"
_HpSwitchServerCertificateRSAKeySize_Object = MibScalar
hpSwitchServerCertificateRSAKeySize = _HpSwitchServerCertificateRSAKeySize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 2),
    _HpSwitchServerCertificateRSAKeySize_Type()
)
hpSwitchServerCertificateRSAKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateRSAKeySize.setStatus("current")


class _HpSwitchServerCertificateSerialNumber_Type(OctetString):
    """Custom type hpSwitchServerCertificateSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpSwitchServerCertificateSerialNumber_Type.__name__ = "OctetString"
_HpSwitchServerCertificateSerialNumber_Object = MibScalar
hpSwitchServerCertificateSerialNumber = _HpSwitchServerCertificateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 3),
    _HpSwitchServerCertificateSerialNumber_Type()
)
hpSwitchServerCertificateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateSerialNumber.setStatus("current")
_HpSwitchServerCertificateStartDate_Type = DateAndTime
_HpSwitchServerCertificateStartDate_Object = MibScalar
hpSwitchServerCertificateStartDate = _HpSwitchServerCertificateStartDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 4),
    _HpSwitchServerCertificateStartDate_Type()
)
hpSwitchServerCertificateStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateStartDate.setStatus("current")
_HpSwitchServerCertificateEndDate_Type = DateAndTime
_HpSwitchServerCertificateEndDate_Object = MibScalar
hpSwitchServerCertificateEndDate = _HpSwitchServerCertificateEndDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 5),
    _HpSwitchServerCertificateEndDate_Type()
)
hpSwitchServerCertificateEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateEndDate.setStatus("current")


class _HpSwitchServerCertificateCommonName_Type(OctetString):
    """Custom type hpSwitchServerCertificateCommonName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpSwitchServerCertificateCommonName_Type.__name__ = "OctetString"
_HpSwitchServerCertificateCommonName_Object = MibScalar
hpSwitchServerCertificateCommonName = _HpSwitchServerCertificateCommonName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 6),
    _HpSwitchServerCertificateCommonName_Type()
)
hpSwitchServerCertificateCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateCommonName.setStatus("current")


class _HpSwitchServerCertificateOrgUnit_Type(OctetString):
    """Custom type hpSwitchServerCertificateOrgUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpSwitchServerCertificateOrgUnit_Type.__name__ = "OctetString"
_HpSwitchServerCertificateOrgUnit_Object = MibScalar
hpSwitchServerCertificateOrgUnit = _HpSwitchServerCertificateOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 7),
    _HpSwitchServerCertificateOrgUnit_Type()
)
hpSwitchServerCertificateOrgUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateOrgUnit.setStatus("current")


class _HpSwitchServerCertificateOrgName_Type(OctetString):
    """Custom type hpSwitchServerCertificateOrgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpSwitchServerCertificateOrgName_Type.__name__ = "OctetString"
_HpSwitchServerCertificateOrgName_Object = MibScalar
hpSwitchServerCertificateOrgName = _HpSwitchServerCertificateOrgName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 8),
    _HpSwitchServerCertificateOrgName_Type()
)
hpSwitchServerCertificateOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateOrgName.setStatus("current")


class _HpSwitchServerCertificateCityName_Type(OctetString):
    """Custom type hpSwitchServerCertificateCityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpSwitchServerCertificateCityName_Type.__name__ = "OctetString"
_HpSwitchServerCertificateCityName_Object = MibScalar
hpSwitchServerCertificateCityName = _HpSwitchServerCertificateCityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 9),
    _HpSwitchServerCertificateCityName_Type()
)
hpSwitchServerCertificateCityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateCityName.setStatus("current")


class _HpSwitchServerCertificateStateName_Type(OctetString):
    """Custom type hpSwitchServerCertificateStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpSwitchServerCertificateStateName_Type.__name__ = "OctetString"
_HpSwitchServerCertificateStateName_Object = MibScalar
hpSwitchServerCertificateStateName = _HpSwitchServerCertificateStateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 10),
    _HpSwitchServerCertificateStateName_Type()
)
hpSwitchServerCertificateStateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateStateName.setStatus("current")


class _HpSwitchServerCertificateCountryCode_Type(OctetString):
    """Custom type hpSwitchServerCertificateCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpSwitchServerCertificateCountryCode_Type.__name__ = "OctetString"
_HpSwitchServerCertificateCountryCode_Object = MibScalar
hpSwitchServerCertificateCountryCode = _HpSwitchServerCertificateCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 11),
    _HpSwitchServerCertificateCountryCode_Type()
)
hpSwitchServerCertificateCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateCountryCode.setStatus("current")


class _HpSwitchServerCertificateFingerprintMD5_Type(OctetString):
    """Custom type hpSwitchServerCertificateFingerprintMD5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HpSwitchServerCertificateFingerprintMD5_Type.__name__ = "OctetString"
_HpSwitchServerCertificateFingerprintMD5_Object = MibScalar
hpSwitchServerCertificateFingerprintMD5 = _HpSwitchServerCertificateFingerprintMD5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 12),
    _HpSwitchServerCertificateFingerprintMD5_Type()
)
hpSwitchServerCertificateFingerprintMD5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateFingerprintMD5.setStatus("current")


class _HpSwitchServerCertificateFingerprintSHA1_Type(OctetString):
    """Custom type hpSwitchServerCertificateFingerprintSHA1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_HpSwitchServerCertificateFingerprintSHA1_Type.__name__ = "OctetString"
_HpSwitchServerCertificateFingerprintSHA1_Object = MibScalar
hpSwitchServerCertificateFingerprintSHA1 = _HpSwitchServerCertificateFingerprintSHA1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 14, 13),
    _HpSwitchServerCertificateFingerprintSHA1_Type()
)
hpSwitchServerCertificateFingerprintSHA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchServerCertificateFingerprintSHA1.setStatus("current")
_HpSwitchKmsChainConfigTable_Object = MibTable
hpSwitchKmsChainConfigTable = _HpSwitchKmsChainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 15)
)
if mibBuilder.loadTexts:
    hpSwitchKmsChainConfigTable.setStatus("current")
_HpSwitchKmsChainConfigEntry_Object = MibTableRow
hpSwitchKmsChainConfigEntry = _HpSwitchKmsChainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 15, 1)
)
hpSwitchKmsChainConfigEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpSwitchKmsChainId"),
)
if mibBuilder.loadTexts:
    hpSwitchKmsChainConfigEntry.setStatus("current")


class _HpSwitchKmsChainId_Type(Integer32):
    """Custom type hpSwitchKmsChainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HpSwitchKmsChainId_Type.__name__ = "Integer32"
_HpSwitchKmsChainId_Object = MibTableColumn
hpSwitchKmsChainId = _HpSwitchKmsChainId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 15, 1, 1),
    _HpSwitchKmsChainId_Type()
)
hpSwitchKmsChainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchKmsChainId.setStatus("current")


class _HpSwitchKmsChainName_Type(DisplayString):
    """Custom type hpSwitchKmsChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpSwitchKmsChainName_Type.__name__ = "DisplayString"
_HpSwitchKmsChainName_Object = MibTableColumn
hpSwitchKmsChainName = _HpSwitchKmsChainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 15, 1, 2),
    _HpSwitchKmsChainName_Type()
)
hpSwitchKmsChainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchKmsChainName.setStatus("current")
_HpSwitchKmsChainKeys_Type = Gauge32
_HpSwitchKmsChainKeys_Object = MibTableColumn
hpSwitchKmsChainKeys = _HpSwitchKmsChainKeys_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 15, 1, 4),
    _HpSwitchKmsChainKeys_Type()
)
hpSwitchKmsChainKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchKmsChainKeys.setStatus("current")
_HpSwitchKmsChainActiveKeys_Type = Gauge32
_HpSwitchKmsChainActiveKeys_Object = MibTableColumn
hpSwitchKmsChainActiveKeys = _HpSwitchKmsChainActiveKeys_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 15, 1, 5),
    _HpSwitchKmsChainActiveKeys_Type()
)
hpSwitchKmsChainActiveKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchKmsChainActiveKeys.setStatus("current")
_HpSwitchKmsChainExpKeys_Type = Gauge32
_HpSwitchKmsChainExpKeys_Object = MibTableColumn
hpSwitchKmsChainExpKeys = _HpSwitchKmsChainExpKeys_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 15, 1, 6),
    _HpSwitchKmsChainExpKeys_Type()
)
hpSwitchKmsChainExpKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchKmsChainExpKeys.setStatus("current")
_HpSwitchKmsChainStatus_Type = RowStatus
_HpSwitchKmsChainStatus_Object = MibTableColumn
hpSwitchKmsChainStatus = _HpSwitchKmsChainStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 15, 1, 7),
    _HpSwitchKmsChainStatus_Type()
)
hpSwitchKmsChainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchKmsChainStatus.setStatus("current")
_HpSwitchKmsKeyConfigTable_Object = MibTable
hpSwitchKmsKeyConfigTable = _HpSwitchKmsKeyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16)
)
if mibBuilder.loadTexts:
    hpSwitchKmsKeyConfigTable.setStatus("current")
_HpSwitchKmsKeyConfigEntry_Object = MibTableRow
hpSwitchKmsKeyConfigEntry = _HpSwitchKmsKeyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1)
)
hpSwitchKmsKeyConfigEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpSwitchKmsKeyChainId"),
    (0, "HP-AUTH-MIB", "hpSwitchKmsKeyId"),
)
if mibBuilder.loadTexts:
    hpSwitchKmsKeyConfigEntry.setStatus("current")


class _HpSwitchKmsKeyChainId_Type(Integer32):
    """Custom type hpSwitchKmsKeyChainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HpSwitchKmsKeyChainId_Type.__name__ = "Integer32"
_HpSwitchKmsKeyChainId_Object = MibTableColumn
hpSwitchKmsKeyChainId = _HpSwitchKmsKeyChainId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1, 1),
    _HpSwitchKmsKeyChainId_Type()
)
hpSwitchKmsKeyChainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchKmsKeyChainId.setStatus("current")


class _HpSwitchKmsKeyId_Type(Integer32):
    """Custom type hpSwitchKmsKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSwitchKmsKeyId_Type.__name__ = "Integer32"
_HpSwitchKmsKeyId_Object = MibTableColumn
hpSwitchKmsKeyId = _HpSwitchKmsKeyId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1, 2),
    _HpSwitchKmsKeyId_Type()
)
hpSwitchKmsKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchKmsKeyId.setStatus("current")


class _HpSwitchKmsKeyStr_Type(OctetString):
    """Custom type hpSwitchKmsKeyStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HpSwitchKmsKeyStr_Type.__name__ = "OctetString"
_HpSwitchKmsKeyStr_Object = MibTableColumn
hpSwitchKmsKeyStr = _HpSwitchKmsKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1, 3),
    _HpSwitchKmsKeyStr_Type()
)
hpSwitchKmsKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchKmsKeyStr.setStatus("current")
_HpSwitchKmsKeyStartTime_Type = Unsigned32
_HpSwitchKmsKeyStartTime_Object = MibTableColumn
hpSwitchKmsKeyStartTime = _HpSwitchKmsKeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1, 4),
    _HpSwitchKmsKeyStartTime_Type()
)
hpSwitchKmsKeyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchKmsKeyStartTime.setStatus("current")
_HpSwitchKmsKeyStopTime_Type = Unsigned32
_HpSwitchKmsKeyStopTime_Object = MibTableColumn
hpSwitchKmsKeyStopTime = _HpSwitchKmsKeyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1, 5),
    _HpSwitchKmsKeyStopTime_Type()
)
hpSwitchKmsKeyStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchKmsKeyStopTime.setStatus("current")
_HpSwitchKmsKeyTxStartTime_Type = Unsigned32
_HpSwitchKmsKeyTxStartTime_Object = MibTableColumn
hpSwitchKmsKeyTxStartTime = _HpSwitchKmsKeyTxStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1, 6),
    _HpSwitchKmsKeyTxStartTime_Type()
)
hpSwitchKmsKeyTxStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchKmsKeyTxStartTime.setStatus("current")
_HpSwitchKmsKeyTxStopTime_Type = Unsigned32
_HpSwitchKmsKeyTxStopTime_Object = MibTableColumn
hpSwitchKmsKeyTxStopTime = _HpSwitchKmsKeyTxStopTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1, 7),
    _HpSwitchKmsKeyTxStopTime_Type()
)
hpSwitchKmsKeyTxStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchKmsKeyTxStopTime.setStatus("current")
_HpSwitchKmsKeyStatus_Type = RowStatus
_HpSwitchKmsKeyStatus_Object = MibTableColumn
hpSwitchKmsKeyStatus = _HpSwitchKmsKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1, 8),
    _HpSwitchKmsKeyStatus_Type()
)
hpSwitchKmsKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchKmsKeyStatus.setStatus("current")


class _HpSwitchKmsKeyEncrypted_Type(OctetString):
    """Custom type hpSwitchKmsKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchKmsKeyEncrypted_Type.__name__ = "OctetString"
_HpSwitchKmsKeyEncrypted_Object = MibTableColumn
hpSwitchKmsKeyEncrypted = _HpSwitchKmsKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 16, 1, 9),
    _HpSwitchKmsKeyEncrypted_Type()
)
hpSwitchKmsKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchKmsKeyEncrypted.setStatus("current")
_HpSwitchOspfIfAuthTable_Object = MibTable
hpSwitchOspfIfAuthTable = _HpSwitchOspfIfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 17)
)
if mibBuilder.loadTexts:
    hpSwitchOspfIfAuthTable.setStatus("current")
_HpSwitchOspfIfAuthEntry_Object = MibTableRow
hpSwitchOspfIfAuthEntry = _HpSwitchOspfIfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 17, 1)
)
if mibBuilder.loadTexts:
    hpSwitchOspfIfAuthEntry.setStatus("current")


class _HpSwitchOspfIfAuthChain_Type(DisplayString):
    """Custom type hpSwitchOspfIfAuthChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpSwitchOspfIfAuthChain_Type.__name__ = "DisplayString"
_HpSwitchOspfIfAuthChain_Object = MibTableColumn
hpSwitchOspfIfAuthChain = _HpSwitchOspfIfAuthChain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 17, 1, 1),
    _HpSwitchOspfIfAuthChain_Type()
)
hpSwitchOspfIfAuthChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchOspfIfAuthChain.setStatus("current")


class _HpSwitchOspfIfAuthKeyEncrypted_Type(OctetString):
    """Custom type hpSwitchOspfIfAuthKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchOspfIfAuthKeyEncrypted_Type.__name__ = "OctetString"
_HpSwitchOspfIfAuthKeyEncrypted_Object = MibTableColumn
hpSwitchOspfIfAuthKeyEncrypted = _HpSwitchOspfIfAuthKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 17, 1, 2),
    _HpSwitchOspfIfAuthKeyEncrypted_Type()
)
hpSwitchOspfIfAuthKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchOspfIfAuthKeyEncrypted.setStatus("current")
_HpSwitchOspfVirtIfAuthTable_Object = MibTable
hpSwitchOspfVirtIfAuthTable = _HpSwitchOspfVirtIfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 18)
)
if mibBuilder.loadTexts:
    hpSwitchOspfVirtIfAuthTable.setStatus("current")
_HpSwitchOspfVirtIfAuthEntry_Object = MibTableRow
hpSwitchOspfVirtIfAuthEntry = _HpSwitchOspfVirtIfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 18, 1)
)
if mibBuilder.loadTexts:
    hpSwitchOspfVirtIfAuthEntry.setStatus("current")


class _HpSwitchOspfVirtIfAuthChain_Type(DisplayString):
    """Custom type hpSwitchOspfVirtIfAuthChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpSwitchOspfVirtIfAuthChain_Type.__name__ = "DisplayString"
_HpSwitchOspfVirtIfAuthChain_Object = MibTableColumn
hpSwitchOspfVirtIfAuthChain = _HpSwitchOspfVirtIfAuthChain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 18, 1, 1),
    _HpSwitchOspfVirtIfAuthChain_Type()
)
hpSwitchOspfVirtIfAuthChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchOspfVirtIfAuthChain.setStatus("current")


class _HpSwitchOspfVirtIfAuthKeyEncrypted_Type(OctetString):
    """Custom type hpSwitchOspfVirtIfAuthKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchOspfVirtIfAuthKeyEncrypted_Type.__name__ = "OctetString"
_HpSwitchOspfVirtIfAuthKeyEncrypted_Object = MibTableColumn
hpSwitchOspfVirtIfAuthKeyEncrypted = _HpSwitchOspfVirtIfAuthKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 18, 1, 2),
    _HpSwitchOspfVirtIfAuthKeyEncrypted_Type()
)
hpSwitchOspfVirtIfAuthKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchOspfVirtIfAuthKeyEncrypted.setStatus("current")
_HpicfSwitchUserConfigTable_Object = MibTable
hpicfSwitchUserConfigTable = _HpicfSwitchUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19)
)
if mibBuilder.loadTexts:
    hpicfSwitchUserConfigTable.setStatus("current")
_HpicfSwitchUserConfigEntry_Object = MibTableRow
hpicfSwitchUserConfigEntry = _HpicfSwitchUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1)
)
hpicfSwitchUserConfigEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpicfSwitchUserConfigIndex"),
)
if mibBuilder.loadTexts:
    hpicfSwitchUserConfigEntry.setStatus("current")


class _HpicfSwitchUserConfigIndex_Type(Integer32):
    """Custom type hpicfSwitchUserConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfSwitchUserConfigIndex_Type.__name__ = "Integer32"
_HpicfSwitchUserConfigIndex_Object = MibTableColumn
hpicfSwitchUserConfigIndex = _HpicfSwitchUserConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 1),
    _HpicfSwitchUserConfigIndex_Type()
)
hpicfSwitchUserConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSwitchUserConfigIndex.setStatus("current")


class _HpicfSwitchUserName_Type(OctetString):
    """Custom type hpicfSwitchUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpicfSwitchUserName_Type.__name__ = "OctetString"
_HpicfSwitchUserName_Object = MibTableColumn
hpicfSwitchUserName = _HpicfSwitchUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 2),
    _HpicfSwitchUserName_Type()
)
hpicfSwitchUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchUserName.setStatus("current")


class _HpicfSwitchOperatorName_Type(OctetString):
    """Custom type hpicfSwitchOperatorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpicfSwitchOperatorName_Type.__name__ = "OctetString"
_HpicfSwitchOperatorName_Object = MibTableColumn
hpicfSwitchOperatorName = _HpicfSwitchOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 3),
    _HpicfSwitchOperatorName_Type()
)
hpicfSwitchOperatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchOperatorName.setStatus("current")


class _HpicfSwitchUserPassword_Type(OctetString):
    """Custom type hpicfSwitchUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpicfSwitchUserPassword_Type.__name__ = "OctetString"
_HpicfSwitchUserPassword_Object = MibTableColumn
hpicfSwitchUserPassword = _HpicfSwitchUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 4),
    _HpicfSwitchUserPassword_Type()
)
hpicfSwitchUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchUserPassword.setStatus("current")


class _HpicfSwitchOperatorPassword_Type(OctetString):
    """Custom type hpicfSwitchOperatorPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpicfSwitchOperatorPassword_Type.__name__ = "OctetString"
_HpicfSwitchOperatorPassword_Object = MibTableColumn
hpicfSwitchOperatorPassword = _HpicfSwitchOperatorPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 5),
    _HpicfSwitchOperatorPassword_Type()
)
hpicfSwitchOperatorPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchOperatorPassword.setStatus("current")
_HpicfSwitchUserConfigStatus_Type = RowStatus
_HpicfSwitchUserConfigStatus_Object = MibTableColumn
hpicfSwitchUserConfigStatus = _HpicfSwitchUserConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 6),
    _HpicfSwitchUserConfigStatus_Type()
)
hpicfSwitchUserConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchUserConfigStatus.setStatus("current")


class _HpicfSwitchPortAccessName_Type(OctetString):
    """Custom type hpicfSwitchPortAccessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpicfSwitchPortAccessName_Type.__name__ = "OctetString"
_HpicfSwitchPortAccessName_Object = MibTableColumn
hpicfSwitchPortAccessName = _HpicfSwitchPortAccessName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 7),
    _HpicfSwitchPortAccessName_Type()
)
hpicfSwitchPortAccessName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchPortAccessName.setStatus("current")


class _HpicfSwitchPortAccessPassword_Type(OctetString):
    """Custom type hpicfSwitchPortAccessPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpicfSwitchPortAccessPassword_Type.__name__ = "OctetString"
_HpicfSwitchPortAccessPassword_Object = MibTableColumn
hpicfSwitchPortAccessPassword = _HpicfSwitchPortAccessPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 8),
    _HpicfSwitchPortAccessPassword_Type()
)
hpicfSwitchPortAccessPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchPortAccessPassword.setStatus("current")


class _HpicfSwitchUserPasswordHashType_Type(Integer32):
    """Custom type hpicfSwitchUserPasswordHashType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("plainText", 1),
          ("sha1", 3),
          ("sha256", 4))
    )


_HpicfSwitchUserPasswordHashType_Type.__name__ = "Integer32"
_HpicfSwitchUserPasswordHashType_Object = MibTableColumn
hpicfSwitchUserPasswordHashType = _HpicfSwitchUserPasswordHashType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 9),
    _HpicfSwitchUserPasswordHashType_Type()
)
hpicfSwitchUserPasswordHashType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchUserPasswordHashType.setStatus("current")


class _HpicfSwitchOperatorPasswordHashType_Type(Integer32):
    """Custom type hpicfSwitchOperatorPasswordHashType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("plainText", 1),
          ("sha1", 3),
          ("sha256", 4))
    )


_HpicfSwitchOperatorPasswordHashType_Type.__name__ = "Integer32"
_HpicfSwitchOperatorPasswordHashType_Object = MibTableColumn
hpicfSwitchOperatorPasswordHashType = _HpicfSwitchOperatorPasswordHashType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 10),
    _HpicfSwitchOperatorPasswordHashType_Type()
)
hpicfSwitchOperatorPasswordHashType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchOperatorPasswordHashType.setStatus("current")


class _HpicfSwitchPortAccessPasswordHashType_Type(Integer32):
    """Custom type hpicfSwitchPortAccessPasswordHashType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("plainText", 1))
    )


_HpicfSwitchPortAccessPasswordHashType_Type.__name__ = "Integer32"
_HpicfSwitchPortAccessPasswordHashType_Object = MibTableColumn
hpicfSwitchPortAccessPasswordHashType = _HpicfSwitchPortAccessPasswordHashType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 11),
    _HpicfSwitchPortAccessPasswordHashType_Type()
)
hpicfSwitchPortAccessPasswordHashType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchPortAccessPasswordHashType.setStatus("current")


class _HpicfSwitchUserPasswordEncrypted_Type(OctetString):
    """Custom type hpicfSwitchUserPasswordEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfSwitchUserPasswordEncrypted_Type.__name__ = "OctetString"
_HpicfSwitchUserPasswordEncrypted_Object = MibTableColumn
hpicfSwitchUserPasswordEncrypted = _HpicfSwitchUserPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 12),
    _HpicfSwitchUserPasswordEncrypted_Type()
)
hpicfSwitchUserPasswordEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchUserPasswordEncrypted.setStatus("current")


class _HpicfSwitchOperatorPasswordEncrypted_Type(OctetString):
    """Custom type hpicfSwitchOperatorPasswordEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfSwitchOperatorPasswordEncrypted_Type.__name__ = "OctetString"
_HpicfSwitchOperatorPasswordEncrypted_Object = MibTableColumn
hpicfSwitchOperatorPasswordEncrypted = _HpicfSwitchOperatorPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 13),
    _HpicfSwitchOperatorPasswordEncrypted_Type()
)
hpicfSwitchOperatorPasswordEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchOperatorPasswordEncrypted.setStatus("current")


class _HpicfSwitchPortAccessPasswordEncrypted_Type(OctetString):
    """Custom type hpicfSwitchPortAccessPasswordEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfSwitchPortAccessPasswordEncrypted_Type.__name__ = "OctetString"
_HpicfSwitchPortAccessPasswordEncrypted_Object = MibTableColumn
hpicfSwitchPortAccessPasswordEncrypted = _HpicfSwitchPortAccessPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 14),
    _HpicfSwitchPortAccessPasswordEncrypted_Type()
)
hpicfSwitchPortAccessPasswordEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchPortAccessPasswordEncrypted.setStatus("current")


class _HpicfSwitchBypassUsername_Type(Integer32):
    """Custom type hpicfSwitchBypassUsername based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpicfSwitchBypassUsername_Type.__name__ = "Integer32"
_HpicfSwitchBypassUsername_Object = MibTableColumn
hpicfSwitchBypassUsername = _HpicfSwitchBypassUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 15),
    _HpicfSwitchBypassUsername_Type()
)
hpicfSwitchBypassUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchBypassUsername.setStatus("current")


class _HpicfSwitchUserPwdAgingInterval_Type(Integer32):
    """Custom type hpicfSwitchUserPwdAgingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_HpicfSwitchUserPwdAgingInterval_Type.__name__ = "Integer32"
_HpicfSwitchUserPwdAgingInterval_Object = MibTableColumn
hpicfSwitchUserPwdAgingInterval = _HpicfSwitchUserPwdAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 16),
    _HpicfSwitchUserPwdAgingInterval_Type()
)
hpicfSwitchUserPwdAgingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchUserPwdAgingInterval.setStatus("current")


class _HpicfSwitchOperatorPwdAgingInterval_Type(Integer32):
    """Custom type hpicfSwitchOperatorPwdAgingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_HpicfSwitchOperatorPwdAgingInterval_Type.__name__ = "Integer32"
_HpicfSwitchOperatorPwdAgingInterval_Object = MibTableColumn
hpicfSwitchOperatorPwdAgingInterval = _HpicfSwitchOperatorPwdAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 17),
    _HpicfSwitchOperatorPwdAgingInterval_Type()
)
hpicfSwitchOperatorPwdAgingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchOperatorPwdAgingInterval.setStatus("current")


class _HpicfSwitchUserPwdLengthValue_Type(Integer32):
    """Custom type hpicfSwitchUserPwdLengthValue based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 64),
    )


_HpicfSwitchUserPwdLengthValue_Type.__name__ = "Integer32"
_HpicfSwitchUserPwdLengthValue_Object = MibTableColumn
hpicfSwitchUserPwdLengthValue = _HpicfSwitchUserPwdLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 18),
    _HpicfSwitchUserPwdLengthValue_Type()
)
hpicfSwitchUserPwdLengthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchUserPwdLengthValue.setStatus("current")


class _HpicfSwitchOperatorPwdLengthValue_Type(Integer32):
    """Custom type hpicfSwitchOperatorPwdLengthValue based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 64),
    )


_HpicfSwitchOperatorPwdLengthValue_Type.__name__ = "Integer32"
_HpicfSwitchOperatorPwdLengthValue_Object = MibTableColumn
hpicfSwitchOperatorPwdLengthValue = _HpicfSwitchOperatorPwdLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 19),
    _HpicfSwitchOperatorPwdLengthValue_Type()
)
hpicfSwitchOperatorPwdLengthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchOperatorPwdLengthValue.setStatus("current")


class _HpicfSwitchNonPlaintextSha256_Type(Integer32):
    """Custom type hpicfSwitchNonPlaintextSha256 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpicfSwitchNonPlaintextSha256_Type.__name__ = "Integer32"
_HpicfSwitchNonPlaintextSha256_Object = MibTableColumn
hpicfSwitchNonPlaintextSha256 = _HpicfSwitchNonPlaintextSha256_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 20),
    _HpicfSwitchNonPlaintextSha256_Type()
)
hpicfSwitchNonPlaintextSha256.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchNonPlaintextSha256.setStatus("current")


class _HpicfSwitchUserPasswordHashSha256_Type(OctetString):
    """Custom type hpicfSwitchUserPasswordHashSha256 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpicfSwitchUserPasswordHashSha256_Type.__name__ = "OctetString"
_HpicfSwitchUserPasswordHashSha256_Object = MibTableColumn
hpicfSwitchUserPasswordHashSha256 = _HpicfSwitchUserPasswordHashSha256_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 21),
    _HpicfSwitchUserPasswordHashSha256_Type()
)
hpicfSwitchUserPasswordHashSha256.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchUserPasswordHashSha256.setStatus("current")


class _HpicfSwitchOperatorPasswordHashSha256_Type(OctetString):
    """Custom type hpicfSwitchOperatorPasswordHashSha256 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HpicfSwitchOperatorPasswordHashSha256_Type.__name__ = "OctetString"
_HpicfSwitchOperatorPasswordHashSha256_Object = MibTableColumn
hpicfSwitchOperatorPasswordHashSha256 = _HpicfSwitchOperatorPasswordHashSha256_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 19, 1, 22),
    _HpicfSwitchOperatorPasswordHashSha256_Type()
)
hpicfSwitchOperatorPasswordHashSha256.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSwitchOperatorPasswordHashSha256.setStatus("current")
_HpSwitchAAAServerGroupTable_Object = MibTable
hpSwitchAAAServerGroupTable = _HpSwitchAAAServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20)
)
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupTable.setStatus("current")
_HpSwitchAAAServerGroupEntry_Object = MibTableRow
hpSwitchAAAServerGroupEntry = _HpSwitchAAAServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1)
)
hpSwitchAAAServerGroupEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpSwitchAAAServerGroupProtocolType"),
    (0, "HP-AUTH-MIB", "hpSwitchAAAServerGroupIndex"),
    (0, "HP-AUTH-MIB", "hpSwitchAAAServerGroupServerIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupEntry.setStatus("current")


class _HpSwitchAAAServerGroupProtocolType_Type(Integer32):
    """Custom type hpSwitchAAAServerGroupProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2))
    )


_HpSwitchAAAServerGroupProtocolType_Type.__name__ = "Integer32"
_HpSwitchAAAServerGroupProtocolType_Object = MibTableColumn
hpSwitchAAAServerGroupProtocolType = _HpSwitchAAAServerGroupProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1, 1),
    _HpSwitchAAAServerGroupProtocolType_Type()
)
hpSwitchAAAServerGroupProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupProtocolType.setStatus("current")


class _HpSwitchAAAServerGroupIndex_Type(Integer32):
    """Custom type hpSwitchAAAServerGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HpSwitchAAAServerGroupIndex_Type.__name__ = "Integer32"
_HpSwitchAAAServerGroupIndex_Object = MibTableColumn
hpSwitchAAAServerGroupIndex = _HpSwitchAAAServerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1, 2),
    _HpSwitchAAAServerGroupIndex_Type()
)
hpSwitchAAAServerGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupIndex.setStatus("current")


class _HpSwitchAAAServerGroupServerIndex_Type(Integer32):
    """Custom type hpSwitchAAAServerGroupServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HpSwitchAAAServerGroupServerIndex_Type.__name__ = "Integer32"
_HpSwitchAAAServerGroupServerIndex_Object = MibTableColumn
hpSwitchAAAServerGroupServerIndex = _HpSwitchAAAServerGroupServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1, 3),
    _HpSwitchAAAServerGroupServerIndex_Type()
)
hpSwitchAAAServerGroupServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupServerIndex.setStatus("current")


class _HpSwitchAAAServerGroupName_Type(DisplayString):
    """Custom type hpSwitchAAAServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchAAAServerGroupName_Type.__name__ = "DisplayString"
_HpSwitchAAAServerGroupName_Object = MibTableColumn
hpSwitchAAAServerGroupName = _HpSwitchAAAServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1, 4),
    _HpSwitchAAAServerGroupName_Type()
)
hpSwitchAAAServerGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupName.setStatus("current")
_HpSwitchAAAServerGroupServerInetType_Type = InetAddressType
_HpSwitchAAAServerGroupServerInetType_Object = MibTableColumn
hpSwitchAAAServerGroupServerInetType = _HpSwitchAAAServerGroupServerInetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1, 5),
    _HpSwitchAAAServerGroupServerInetType_Type()
)
hpSwitchAAAServerGroupServerInetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupServerInetType.setStatus("current")
_HpSwitchAAAServerGroupServerInetAddr_Type = InetAddress
_HpSwitchAAAServerGroupServerInetAddr_Object = MibTableColumn
hpSwitchAAAServerGroupServerInetAddr = _HpSwitchAAAServerGroupServerInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1, 6),
    _HpSwitchAAAServerGroupServerInetAddr_Type()
)
hpSwitchAAAServerGroupServerInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupServerInetAddr.setStatus("current")
_HpSwitchAAAServerGroupStatus_Type = RowStatus
_HpSwitchAAAServerGroupStatus_Object = MibTableColumn
hpSwitchAAAServerGroupStatus = _HpSwitchAAAServerGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1, 7),
    _HpSwitchAAAServerGroupStatus_Type()
)
hpSwitchAAAServerGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupStatus.setStatus("current")


class _HpSwitchAAAServerGroupServerFqdn_Type(DisplayString):
    """Custom type hpSwitchAAAServerGroupServerFqdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpSwitchAAAServerGroupServerFqdn_Type.__name__ = "DisplayString"
_HpSwitchAAAServerGroupServerFqdn_Object = MibTableColumn
hpSwitchAAAServerGroupServerFqdn = _HpSwitchAAAServerGroupServerFqdn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1, 8),
    _HpSwitchAAAServerGroupServerFqdn_Type()
)
hpSwitchAAAServerGroupServerFqdn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupServerFqdn.setStatus("current")


class _HpSwitchAAAServerGroupTLSEnable_Type(TruthValue):
    """Custom type hpSwitchAAAServerGroupTLSEnable based on TruthValue"""
    defaultValue = 2


_HpSwitchAAAServerGroupTLSEnable_Type.__name__ = "TruthValue"
_HpSwitchAAAServerGroupTLSEnable_Object = MibTableColumn
hpSwitchAAAServerGroupTLSEnable = _HpSwitchAAAServerGroupTLSEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 20, 1, 9),
    _HpSwitchAAAServerGroupTLSEnable_Type()
)
hpSwitchAAAServerGroupTLSEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupTLSEnable.setStatus("current")
_HpSwitchLocalMgmtPrivUsernamesTable_Object = MibTable
hpSwitchLocalMgmtPrivUsernamesTable = _HpSwitchLocalMgmtPrivUsernamesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21)
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUsernamesTable.setStatus("current")
_HpSwitchLocalMgmtPrivUsernamesEntry_Object = MibTableRow
hpSwitchLocalMgmtPrivUsernamesEntry = _HpSwitchLocalMgmtPrivUsernamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1)
)
hpSwitchLocalMgmtPrivUsernamesEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernameIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUsernamesEntry.setStatus("current")


class _HpSwitchLocalMgmtPrivUsernameIndex_Type(Integer32):
    """Custom type hpSwitchLocalMgmtPrivUsernameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpSwitchLocalMgmtPrivUsernameIndex_Type.__name__ = "Integer32"
_HpSwitchLocalMgmtPrivUsernameIndex_Object = MibTableColumn
hpSwitchLocalMgmtPrivUsernameIndex = _HpSwitchLocalMgmtPrivUsernameIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1, 1),
    _HpSwitchLocalMgmtPrivUsernameIndex_Type()
)
hpSwitchLocalMgmtPrivUsernameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUsernameIndex.setStatus("current")


class _HpSwitchLocalMgmtPrivUsernameStr_Type(OctetString):
    """Custom type hpSwitchLocalMgmtPrivUsernameStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpSwitchLocalMgmtPrivUsernameStr_Type.__name__ = "OctetString"
_HpSwitchLocalMgmtPrivUsernameStr_Object = MibTableColumn
hpSwitchLocalMgmtPrivUsernameStr = _HpSwitchLocalMgmtPrivUsernameStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1, 2),
    _HpSwitchLocalMgmtPrivUsernameStr_Type()
)
hpSwitchLocalMgmtPrivUsernameStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUsernameStr.setStatus("current")


class _HpSwitchLocalMgmtPrivUsernamePasswdType_Type(Integer32):
    """Custom type hpSwitchLocalMgmtPrivUsernamePasswdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("sha1", 3),
          ("sha256", 4))
    )


_HpSwitchLocalMgmtPrivUsernamePasswdType_Type.__name__ = "Integer32"
_HpSwitchLocalMgmtPrivUsernamePasswdType_Object = MibTableColumn
hpSwitchLocalMgmtPrivUsernamePasswdType = _HpSwitchLocalMgmtPrivUsernamePasswdType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1, 3),
    _HpSwitchLocalMgmtPrivUsernamePasswdType_Type()
)
hpSwitchLocalMgmtPrivUsernamePasswdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUsernamePasswdType.setStatus("current")


class _HpSwitchLocalMgmtPrivUsernamePasswd_Type(OctetString):
    """Custom type hpSwitchLocalMgmtPrivUsernamePasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchLocalMgmtPrivUsernamePasswd_Type.__name__ = "OctetString"
_HpSwitchLocalMgmtPrivUsernamePasswd_Object = MibTableColumn
hpSwitchLocalMgmtPrivUsernamePasswd = _HpSwitchLocalMgmtPrivUsernamePasswd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1, 4),
    _HpSwitchLocalMgmtPrivUsernamePasswd_Type()
)
hpSwitchLocalMgmtPrivUsernamePasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUsernamePasswd.setStatus("current")
_HpSwitchLocalMgmtPrivUsernameGrpIndex_Type = Integer32
_HpSwitchLocalMgmtPrivUsernameGrpIndex_Object = MibTableColumn
hpSwitchLocalMgmtPrivUsernameGrpIndex = _HpSwitchLocalMgmtPrivUsernameGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1, 5),
    _HpSwitchLocalMgmtPrivUsernameGrpIndex_Type()
)
hpSwitchLocalMgmtPrivUsernameGrpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUsernameGrpIndex.setStatus("current")
_HpSwitchLocalMgmtPrivUsernameStatus_Type = RowStatus
_HpSwitchLocalMgmtPrivUsernameStatus_Object = MibTableColumn
hpSwitchLocalMgmtPrivUsernameStatus = _HpSwitchLocalMgmtPrivUsernameStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1, 6),
    _HpSwitchLocalMgmtPrivUsernameStatus_Type()
)
hpSwitchLocalMgmtPrivUsernameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUsernameStatus.setStatus("current")


class _HpSwitchLocalMgmtPwdUserAgingInterval_Type(Integer32):
    """Custom type hpSwitchLocalMgmtPwdUserAgingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_HpSwitchLocalMgmtPwdUserAgingInterval_Type.__name__ = "Integer32"
_HpSwitchLocalMgmtPwdUserAgingInterval_Object = MibTableColumn
hpSwitchLocalMgmtPwdUserAgingInterval = _HpSwitchLocalMgmtPwdUserAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1, 7),
    _HpSwitchLocalMgmtPwdUserAgingInterval_Type()
)
hpSwitchLocalMgmtPwdUserAgingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPwdUserAgingInterval.setStatus("current")


class _HpSwitchLocalMgmtPwdUserPasswdLengthValue_Type(Integer32):
    """Custom type hpSwitchLocalMgmtPwdUserPasswdLengthValue based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpSwitchLocalMgmtPwdUserPasswdLengthValue_Type.__name__ = "Integer32"
_HpSwitchLocalMgmtPwdUserPasswdLengthValue_Object = MibTableColumn
hpSwitchLocalMgmtPwdUserPasswdLengthValue = _HpSwitchLocalMgmtPwdUserPasswdLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1, 8),
    _HpSwitchLocalMgmtPwdUserPasswdLengthValue_Type()
)
hpSwitchLocalMgmtPwdUserPasswdLengthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPwdUserPasswdLengthValue.setStatus("current")


class _HpSwitchLocalMgmtPrivUsernamePasswdSha256_Type(OctetString):
    """Custom type hpSwitchLocalMgmtPrivUsernamePasswdSha256 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchLocalMgmtPrivUsernamePasswdSha256_Type.__name__ = "OctetString"
_HpSwitchLocalMgmtPrivUsernamePasswdSha256_Object = MibTableColumn
hpSwitchLocalMgmtPrivUsernamePasswdSha256 = _HpSwitchLocalMgmtPrivUsernamePasswdSha256_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 21, 1, 9),
    _HpSwitchLocalMgmtPrivUsernamePasswdSha256_Type()
)
hpSwitchLocalMgmtPrivUsernamePasswdSha256.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUsernamePasswdSha256.setStatus("current")
_HpSwitchRipIfAuthTable_Object = MibTable
hpSwitchRipIfAuthTable = _HpSwitchRipIfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 23)
)
if mibBuilder.loadTexts:
    hpSwitchRipIfAuthTable.setStatus("current")
_HpSwitchRipIfAuthEntry_Object = MibTableRow
hpSwitchRipIfAuthEntry = _HpSwitchRipIfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 23, 1)
)
if mibBuilder.loadTexts:
    hpSwitchRipIfAuthEntry.setStatus("current")


class _HpSwitchRipIfAuthChain_Type(DisplayString):
    """Custom type hpSwitchRipIfAuthChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpSwitchRipIfAuthChain_Type.__name__ = "DisplayString"
_HpSwitchRipIfAuthChain_Object = MibTableColumn
hpSwitchRipIfAuthChain = _HpSwitchRipIfAuthChain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 23, 1, 1),
    _HpSwitchRipIfAuthChain_Type()
)
hpSwitchRipIfAuthChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRipIfAuthChain.setStatus("current")


class _HpSwitchRip2IfConfAuthKeyEncrypted_Type(OctetString):
    """Custom type hpSwitchRip2IfConfAuthKeyEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpSwitchRip2IfConfAuthKeyEncrypted_Type.__name__ = "OctetString"
_HpSwitchRip2IfConfAuthKeyEncrypted_Object = MibTableColumn
hpSwitchRip2IfConfAuthKeyEncrypted = _HpSwitchRip2IfConfAuthKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 23, 1, 2),
    _HpSwitchRip2IfConfAuthKeyEncrypted_Type()
)
hpSwitchRip2IfConfAuthKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchRip2IfConfAuthKeyEncrypted.setStatus("current")
_HpSwitchAuthenPwdCompositionTable_Object = MibTable
hpSwitchAuthenPwdCompositionTable = _HpSwitchAuthenPwdCompositionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 24)
)
if mibBuilder.loadTexts:
    hpSwitchAuthenPwdCompositionTable.setStatus("current")
_HpSwitchAuthenPwdCompositionEntry_Object = MibTableRow
hpSwitchAuthenPwdCompositionEntry = _HpSwitchAuthenPwdCompositionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 24, 1)
)
hpSwitchAuthenPwdCompositionEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpSwitchAuthenCompositionIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchAuthenPwdCompositionEntry.setStatus("current")


class _HpSwitchAuthenCompositionIndex_Type(Integer32):
    """Custom type hpSwitchAuthenCompositionIndex based on Integer32"""
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
        *(("lowerCase", 1),
          ("upperCase", 2),
          ("specialCharacter", 3),
          ("number", 4))
    )


_HpSwitchAuthenCompositionIndex_Type.__name__ = "Integer32"
_HpSwitchAuthenCompositionIndex_Object = MibTableColumn
hpSwitchAuthenCompositionIndex = _HpSwitchAuthenCompositionIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 24, 1, 1),
    _HpSwitchAuthenCompositionIndex_Type()
)
hpSwitchAuthenCompositionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAuthenCompositionIndex.setStatus("current")


class _HpSwitchAuthenCompositionValue_Type(Integer32):
    """Custom type hpSwitchAuthenCompositionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_HpSwitchAuthenCompositionValue_Type.__name__ = "Integer32"
_HpSwitchAuthenCompositionValue_Object = MibTableColumn
hpSwitchAuthenCompositionValue = _HpSwitchAuthenCompositionValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 24, 1, 2),
    _HpSwitchAuthenCompositionValue_Type()
)
hpSwitchAuthenCompositionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthenCompositionValue.setStatus("current")
_HpSwitchAuthenticationPasswordConfig_ObjectIdentity = ObjectIdentity
hpSwitchAuthenticationPasswordConfig = _HpSwitchAuthenticationPasswordConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25)
)


class _HpSwitchAuthPwdControlCheck_Type(Integer32):
    """Custom type hpSwitchAuthPwdControlCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthPwdControlCheck_Type.__name__ = "Integer32"
_HpSwitchAuthPwdControlCheck_Object = MibScalar
hpSwitchAuthPwdControlCheck = _HpSwitchAuthPwdControlCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 1),
    _HpSwitchAuthPwdControlCheck_Type()
)
hpSwitchAuthPwdControlCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdControlCheck.setStatus("current")


class _HpSwitchAuthPwdUserNameCheck_Type(Integer32):
    """Custom type hpSwitchAuthPwdUserNameCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthPwdUserNameCheck_Type.__name__ = "Integer32"
_HpSwitchAuthPwdUserNameCheck_Object = MibScalar
hpSwitchAuthPwdUserNameCheck = _HpSwitchAuthPwdUserNameCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 2),
    _HpSwitchAuthPwdUserNameCheck_Type()
)
hpSwitchAuthPwdUserNameCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdUserNameCheck.setStatus("current")


class _HpSwitchAuthPwdRepeatCharactersCheck_Type(Integer32):
    """Custom type hpSwitchAuthPwdRepeatCharactersCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthPwdRepeatCharactersCheck_Type.__name__ = "Integer32"
_HpSwitchAuthPwdRepeatCharactersCheck_Object = MibScalar
hpSwitchAuthPwdRepeatCharactersCheck = _HpSwitchAuthPwdRepeatCharactersCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 3),
    _HpSwitchAuthPwdRepeatCharactersCheck_Type()
)
hpSwitchAuthPwdRepeatCharactersCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdRepeatCharactersCheck.setStatus("current")


class _HpSwitchAuthPwdRepeatPasswordCheck_Type(Integer32):
    """Custom type hpSwitchAuthPwdRepeatPasswordCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthPwdRepeatPasswordCheck_Type.__name__ = "Integer32"
_HpSwitchAuthPwdRepeatPasswordCheck_Object = MibScalar
hpSwitchAuthPwdRepeatPasswordCheck = _HpSwitchAuthPwdRepeatPasswordCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 4),
    _HpSwitchAuthPwdRepeatPasswordCheck_Type()
)
hpSwitchAuthPwdRepeatPasswordCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdRepeatPasswordCheck.setStatus("current")


class _HpSwitchAuthPwdAgingCheck_Type(Integer32):
    """Custom type hpSwitchAuthPwdAgingCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthPwdAgingCheck_Type.__name__ = "Integer32"
_HpSwitchAuthPwdAgingCheck_Object = MibScalar
hpSwitchAuthPwdAgingCheck = _HpSwitchAuthPwdAgingCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 5),
    _HpSwitchAuthPwdAgingCheck_Type()
)
hpSwitchAuthPwdAgingCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdAgingCheck.setStatus("current")


class _HpSwitchAuthPwdLogonDetailsCheck_Type(Integer32):
    """Custom type hpSwitchAuthPwdLogonDetailsCheck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthPwdLogonDetailsCheck_Type.__name__ = "Integer32"
_HpSwitchAuthPwdLogonDetailsCheck_Object = MibScalar
hpSwitchAuthPwdLogonDetailsCheck = _HpSwitchAuthPwdLogonDetailsCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 6),
    _HpSwitchAuthPwdLogonDetailsCheck_Type()
)
hpSwitchAuthPwdLogonDetailsCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdLogonDetailsCheck.setStatus("current")


class _HpSwitchAuthPwdAgingValue_Type(Integer32):
    """Custom type hpSwitchAuthPwdAgingValue based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 365),
    )


_HpSwitchAuthPwdAgingValue_Type.__name__ = "Integer32"
_HpSwitchAuthPwdAgingValue_Object = MibScalar
hpSwitchAuthPwdAgingValue = _HpSwitchAuthPwdAgingValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 7),
    _HpSwitchAuthPwdAgingValue_Type()
)
hpSwitchAuthPwdAgingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdAgingValue.setStatus("current")


class _HpSwitchAuthPwdHistoryCheck_Type(Integer32):
    """Custom type hpSwitchAuthPwdHistoryCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpSwitchAuthPwdHistoryCheck_Type.__name__ = "Integer32"
_HpSwitchAuthPwdHistoryCheck_Object = MibScalar
hpSwitchAuthPwdHistoryCheck = _HpSwitchAuthPwdHistoryCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 8),
    _HpSwitchAuthPwdHistoryCheck_Type()
)
hpSwitchAuthPwdHistoryCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdHistoryCheck.setStatus("current")


class _HpSwitchAuthPwdHistoryRecordsRange_Type(Integer32):
    """Custom type hpSwitchAuthPwdHistoryRecordsRange based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_HpSwitchAuthPwdHistoryRecordsRange_Type.__name__ = "Integer32"
_HpSwitchAuthPwdHistoryRecordsRange_Object = MibScalar
hpSwitchAuthPwdHistoryRecordsRange = _HpSwitchAuthPwdHistoryRecordsRange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 9),
    _HpSwitchAuthPwdHistoryRecordsRange_Type()
)
hpSwitchAuthPwdHistoryRecordsRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdHistoryRecordsRange.setStatus("current")


class _HpSwitchAuthPwdAlertBeforeExpiry_Type(Integer32):
    """Custom type hpSwitchAuthPwdAlertBeforeExpiry based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HpSwitchAuthPwdAlertBeforeExpiry_Type.__name__ = "Integer32"
_HpSwitchAuthPwdAlertBeforeExpiry_Object = MibScalar
hpSwitchAuthPwdAlertBeforeExpiry = _HpSwitchAuthPwdAlertBeforeExpiry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 10),
    _HpSwitchAuthPwdAlertBeforeExpiry_Type()
)
hpSwitchAuthPwdAlertBeforeExpiry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdAlertBeforeExpiry.setStatus("current")


class _HpSwitchAuthPwdExpiredUserLoginDays_Type(Integer32):
    """Custom type hpSwitchAuthPwdExpiredUserLoginDays based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_HpSwitchAuthPwdExpiredUserLoginDays_Type.__name__ = "Integer32"
_HpSwitchAuthPwdExpiredUserLoginDays_Object = MibScalar
hpSwitchAuthPwdExpiredUserLoginDays = _HpSwitchAuthPwdExpiredUserLoginDays_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 11),
    _HpSwitchAuthPwdExpiredUserLoginDays_Type()
)
hpSwitchAuthPwdExpiredUserLoginDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdExpiredUserLoginDays.setStatus("current")


class _HpSwitchAuthPwdExpiredUserLoginAttempts_Type(Integer32):
    """Custom type hpSwitchAuthPwdExpiredUserLoginAttempts based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpSwitchAuthPwdExpiredUserLoginAttempts_Type.__name__ = "Integer32"
_HpSwitchAuthPwdExpiredUserLoginAttempts_Object = MibScalar
hpSwitchAuthPwdExpiredUserLoginAttempts = _HpSwitchAuthPwdExpiredUserLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 12),
    _HpSwitchAuthPwdExpiredUserLoginAttempts_Type()
)
hpSwitchAuthPwdExpiredUserLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdExpiredUserLoginAttempts.setStatus("current")


class _HpSwitchAuthPwdUpdateInterval_Type(Integer32):
    """Custom type hpSwitchAuthPwdUpdateInterval based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_HpSwitchAuthPwdUpdateInterval_Type.__name__ = "Integer32"
_HpSwitchAuthPwdUpdateInterval_Object = MibScalar
hpSwitchAuthPwdUpdateInterval = _HpSwitchAuthPwdUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 13),
    _HpSwitchAuthPwdUpdateInterval_Type()
)
hpSwitchAuthPwdUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdUpdateInterval.setStatus("current")


class _HpSwitchAuthPwdCharPositionCheckValue_Type(Integer32):
    """Custom type hpSwitchAuthPwdCharPositionCheckValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 64),
    )


_HpSwitchAuthPwdCharPositionCheckValue_Type.__name__ = "Integer32"
_HpSwitchAuthPwdCharPositionCheckValue_Object = MibScalar
hpSwitchAuthPwdCharPositionCheckValue = _HpSwitchAuthPwdCharPositionCheckValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 25, 14),
    _HpSwitchAuthPwdCharPositionCheckValue_Type()
)
hpSwitchAuthPwdCharPositionCheckValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAuthPwdCharPositionCheckValue.setStatus("current")
_HpSwitchFrontPanelSecurity_ObjectIdentity = ObjectIdentity
hpSwitchFrontPanelSecurity = _HpSwitchFrontPanelSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 26)
)


class _HpSwitchFpsPasswordClear_Type(Integer32):
    """Custom type hpSwitchFpsPasswordClear based on Integer32"""
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
        *(("enable", 0),
          ("enablewithreset", 1),
          ("disable", 2))
    )


_HpSwitchFpsPasswordClear_Type.__name__ = "Integer32"
_HpSwitchFpsPasswordClear_Object = MibScalar
hpSwitchFpsPasswordClear = _HpSwitchFpsPasswordClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 26, 1),
    _HpSwitchFpsPasswordClear_Type()
)
hpSwitchFpsPasswordClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFpsPasswordClear.setStatus("current")


class _HpSwitchFpsFactoryReset_Type(Integer32):
    """Custom type hpSwitchFpsFactoryReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_HpSwitchFpsFactoryReset_Type.__name__ = "Integer32"
_HpSwitchFpsFactoryReset_Object = MibScalar
hpSwitchFpsFactoryReset = _HpSwitchFpsFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 26, 2),
    _HpSwitchFpsFactoryReset_Type()
)
hpSwitchFpsFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFpsFactoryReset.setStatus("current")


class _HpSwitchFpsPasswordRecovery_Type(Integer32):
    """Custom type hpSwitchFpsPasswordRecovery based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("normal", 1),
          ("strong", 2))
    )


_HpSwitchFpsPasswordRecovery_Type.__name__ = "Integer32"
_HpSwitchFpsPasswordRecovery_Object = MibScalar
hpSwitchFpsPasswordRecovery = _HpSwitchFpsPasswordRecovery_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 26, 3),
    _HpSwitchFpsPasswordRecovery_Type()
)
hpSwitchFpsPasswordRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFpsPasswordRecovery.setStatus("current")


class _HpSwitchFpsDiagnosticResetClearButton_Type(Integer32):
    """Custom type hpSwitchFpsDiagnosticResetClearButton based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_HpSwitchFpsDiagnosticResetClearButton_Type.__name__ = "Integer32"
_HpSwitchFpsDiagnosticResetClearButton_Object = MibScalar
hpSwitchFpsDiagnosticResetClearButton = _HpSwitchFpsDiagnosticResetClearButton_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 26, 4),
    _HpSwitchFpsDiagnosticResetClearButton_Type()
)
hpSwitchFpsDiagnosticResetClearButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFpsDiagnosticResetClearButton.setStatus("current")


class _HpSwitchFpsDiagnosticResetSerialConsole_Type(Integer32):
    """Custom type hpSwitchFpsDiagnosticResetSerialConsole based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_HpSwitchFpsDiagnosticResetSerialConsole_Type.__name__ = "Integer32"
_HpSwitchFpsDiagnosticResetSerialConsole_Object = MibScalar
hpSwitchFpsDiagnosticResetSerialConsole = _HpSwitchFpsDiagnosticResetSerialConsole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 26, 5),
    _HpSwitchFpsDiagnosticResetSerialConsole_Type()
)
hpSwitchFpsDiagnosticResetSerialConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFpsDiagnosticResetSerialConsole.setStatus("current")


class _HpSwitchFpsDisplayInConfig_Type(Integer32):
    """Custom type hpSwitchFpsDisplayInConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_HpSwitchFpsDisplayInConfig_Type.__name__ = "Integer32"
_HpSwitchFpsDisplayInConfig_Object = MibScalar
hpSwitchFpsDisplayInConfig = _HpSwitchFpsDisplayInConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 26, 6),
    _HpSwitchFpsDisplayInConfig_Type()
)
hpSwitchFpsDisplayInConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFpsDisplayInConfig.setStatus("current")
_HpSwitchAAAServerGroupNasTable_Object = MibTable
hpSwitchAAAServerGroupNasTable = _HpSwitchAAAServerGroupNasTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 27)
)
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupNasTable.setStatus("current")
_HpSwitchAAAServerGroupNasEntry_Object = MibTableRow
hpSwitchAAAServerGroupNasEntry = _HpSwitchAAAServerGroupNasEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 27, 1)
)
hpSwitchAAAServerGroupNasEntry.setIndexNames(
    (0, "HP-AUTH-MIB", "hpSwitchAAAServerGroupNasProtocolType"),
    (0, "HP-AUTH-MIB", "hpSwitchAAAServerGroupNasIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupNasEntry.setStatus("current")


class _HpSwitchAAAServerGroupNasProtocolType_Type(Integer32):
    """Custom type hpSwitchAAAServerGroupNasProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacacs", 2))
    )


_HpSwitchAAAServerGroupNasProtocolType_Type.__name__ = "Integer32"
_HpSwitchAAAServerGroupNasProtocolType_Object = MibTableColumn
hpSwitchAAAServerGroupNasProtocolType = _HpSwitchAAAServerGroupNasProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 27, 1, 1),
    _HpSwitchAAAServerGroupNasProtocolType_Type()
)
hpSwitchAAAServerGroupNasProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupNasProtocolType.setStatus("current")


class _HpSwitchAAAServerGroupNasIndex_Type(Integer32):
    """Custom type hpSwitchAAAServerGroupNasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HpSwitchAAAServerGroupNasIndex_Type.__name__ = "Integer32"
_HpSwitchAAAServerGroupNasIndex_Object = MibTableColumn
hpSwitchAAAServerGroupNasIndex = _HpSwitchAAAServerGroupNasIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 27, 1, 2),
    _HpSwitchAAAServerGroupNasIndex_Type()
)
hpSwitchAAAServerGroupNasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupNasIndex.setStatus("current")


class _HpSwitchAAAServerGroupNasName_Type(DisplayString):
    """Custom type hpSwitchAAAServerGroupNasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchAAAServerGroupNasName_Type.__name__ = "DisplayString"
_HpSwitchAAAServerGroupNasName_Object = MibTableColumn
hpSwitchAAAServerGroupNasName = _HpSwitchAAAServerGroupNasName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 27, 1, 3),
    _HpSwitchAAAServerGroupNasName_Type()
)
hpSwitchAAAServerGroupNasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupNasName.setStatus("current")


class _HpSwitchAAAServerGroupNasId_Type(DisplayString):
    """Custom type hpSwitchAAAServerGroupNasId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchAAAServerGroupNasId_Type.__name__ = "DisplayString"
_HpSwitchAAAServerGroupNasId_Object = MibTableColumn
hpSwitchAAAServerGroupNasId = _HpSwitchAAAServerGroupNasId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 27, 1, 4),
    _HpSwitchAAAServerGroupNasId_Type()
)
hpSwitchAAAServerGroupNasId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupNasId.setStatus("current")
_HpSwitchAAAServerGroupNasStatus_Type = RowStatus
_HpSwitchAAAServerGroupNasStatus_Object = MibTableColumn
hpSwitchAAAServerGroupNasStatus = _HpSwitchAAAServerGroupNasStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 27, 1, 5),
    _HpSwitchAAAServerGroupNasStatus_Type()
)
hpSwitchAAAServerGroupNasStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroupNasStatus.setStatus("current")
ospfIfEntry.registerAugmentions(
    ("HP-AUTH-MIB",
     "hpSwitchOspfIfAuthEntry")
)
hpSwitchOspfIfAuthEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("HP-AUTH-MIB",
     "hpSwitchOspfVirtIfAuthEntry")
)
hpSwitchOspfVirtIfAuthEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
rip2IfConfEntry.registerAugmentions(
    ("HP-AUTH-MIB",
     "hpSwitchRipIfAuthEntry")
)
hpSwitchRipIfAuthEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())

# Managed Objects groups

hpSwitchAuthenticationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 1)
)
hpSwitchAuthenticationConfigGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup.setStatus("deprecated")

hpSwitchTacacsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 2)
)
hpSwitchTacacsConfigGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsTimeout"),
        ("HP-AUTH-MIB", "hpSwitchTacacsAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchTacacsDeadTime"))
)
if mibBuilder.loadTexts:
    hpSwitchTacacsConfigGroup.setStatus("deprecated")

hpSwitchTacacsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 3)
)
hpSwitchTacacsStatsGroup.setObjects(
      *(("HP-AUTH-MIB", "hpTacacsStatsTacacsServerIpAddr"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumSessOpened"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumSessClosed"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumSessAborted"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumSessErrors"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumPktsIn"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumPktsOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAuthPktsIn"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAuthPktsOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAuthPktsTimedOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAutzPktsIn"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAutzPktsOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAutzPktsTimedOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAcctPktsIn"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAcctPktsOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAcctPktsTimedOut"))
)
if mibBuilder.loadTexts:
    hpSwitchTacacsStatsGroup.setStatus("deprecated")

hpSwitchRadiusConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 4)
)
hpSwitchRadiusConfigGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup.setStatus("deprecated")

hpSwitchKmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 6)
)
hpSwitchKmsGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchKmsChainName"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainKeys"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainActiveKeys"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainExpKeys"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainStatus"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyStr"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyStartTime"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyStopTime"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyTxStartTime"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyTxStopTime"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainStatus"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchKmsGroup.setStatus("deprecated")

hpSwitchOspfAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 7)
)
hpSwitchOspfAuthGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchOspfVirtIfAuthChain"),
        ("HP-AUTH-MIB", "hpSwitchOspfIfAuthChain"))
)
if mibBuilder.loadTexts:
    hpSwitchOspfAuthGroup.setStatus("deprecated")

hpSwitchAuthenticationConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 8)
)
hpSwitchAuthenticationConfigGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthRespectPriv"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationEncryptCredentialsMethod"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup1.setStatus("deprecated")

hpSwitchSslGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 9)
)
hpSwitchSslGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchSslAdminStatus"),
        ("HP-AUTH-MIB", "hpSwitchSslPortNumber"))
)
if mibBuilder.loadTexts:
    hpSwitchSslGroup.setStatus("current")

hpSwitchCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 10)
)
hpSwitchCertGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchServerCertificateType"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateRSAKeySize"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateSerialNumber"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateStartDate"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateEndDate"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateCommonName"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateOrgUnit"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateOrgName"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateCityName"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateStateName"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateCountryCode"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateFingerprintMD5"),
        ("HP-AUTH-MIB", "hpSwitchServerCertificateFingerprintSHA1"))
)
if mibBuilder.loadTexts:
    hpSwitchCertGroup.setStatus("current")

hpSwitchCertStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 11)
)
hpSwitchCertStatusGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchServerCertificateOperation"),
        ("HP-AUTH-MIB", "hpSwitchServerNewRSAKeyOperation"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertificateStartDate"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertificateEndDate"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertCommonName"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertOrgUnit"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertOrgName"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertCityName"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertStateName"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertificateCountryCode"))
)
if mibBuilder.loadTexts:
    hpSwitchCertStatusGroup.setStatus("current")

hpSwitchTacacsOobmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 12)
)
hpSwitchTacacsOobmGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerIsOobm"))
)
if mibBuilder.loadTexts:
    hpSwitchTacacsOobmGroup.setStatus("deprecated")

hpSwitchRadiusOobmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 13)
)
hpSwitchRadiusOobmGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusOobmGroup.setStatus("deprecated")

hpSwitchCertStatusGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 14)
)
hpSwitchCertStatusGroup2.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchServerNewCertificateCommonName"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertificateOrgUnit"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertificateOrgName"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertificateCityName"),
        ("HP-AUTH-MIB", "hpSwitchServerNewCertificateStateName"))
)
if mibBuilder.loadTexts:
    hpSwitchCertStatusGroup2.setStatus("deprecated")

hpSwitchUserConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 15)
)
hpSwitchUserConfigGroup.setObjects(
      *(("HP-AUTH-MIB", "hpicfSwitchUserName"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorName"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessName"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchUserConfigStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchUserConfigGroup.setStatus("deprecated")

hpSwitchAAAServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 16)
)
hpSwitchAAAServerGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAAAServerGroupName"),
        ("HP-AUTH-MIB", "hpSwitchAAAServerGroupServerInetType"),
        ("HP-AUTH-MIB", "hpSwitchAAAServerGroupServerInetAddr"),
        ("HP-AUTH-MIB", "hpSwitchAAAServerGroupStatus"),
        ("HP-AUTH-MIB", "hpSwitchAAAServerGroupServerFqdn"))
)
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroup.setStatus("deprecated")

hpSwitchAuthenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 17)
)
hpSwitchAuthenGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenLoginServerGroupName"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableServerGroupName"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondAuthMethod"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenGroup.setStatus("current")

hpSwitchAuthLocalMgmtPrivUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 18)
)
hpSwitchAuthLocalMgmtPrivUserGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernameStr"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernamePasswdType"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernamePasswd"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernameGrpIndex"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthLocalMgmtPrivUserGroup.setStatus("deprecated")

hpSwitchTacacsConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 19)
)
hpSwitchTacacsConfigGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsTimeout"),
        ("HP-AUTH-MIB", "hpSwitchTacacsAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchTacacsDeadTime"))
)
if mibBuilder.loadTexts:
    hpSwitchTacacsConfigGroup1.setStatus("deprecated")

hpSwitchRadiusConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 20)
)
hpSwitchRadiusConfigGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup1.setStatus("deprecated")

hpSwitchKmsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 21)
)
hpSwitchKmsGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchKmsChainName"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainKeys"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainActiveKeys"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainExpKeys"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainStatus"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyStr"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyStartTime"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyStopTime"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyTxStartTime"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyTxStopTime"),
        ("HP-AUTH-MIB", "hpSwitchKmsChainStatus"),
        ("HP-AUTH-MIB", "hpSwitchKmsKeyStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchKmsGroup1.setStatus("current")

hpSwitchUserConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 22)
)
hpSwitchUserConfigGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpicfSwitchUserName"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorName"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessName"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPasswordEncrypted"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPasswordEncrypted"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPasswordEncrypted"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchUserConfigStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchUserConfigGroup1.setStatus("deprecated")

hpSwitchAuthLocalMgmtPrivUserGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 23)
)
hpSwitchAuthLocalMgmtPrivUserGroup1.setObjects(
    ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernameStatus")
)
if mibBuilder.loadTexts:
    hpSwitchAuthLocalMgmtPrivUserGroup1.setStatus("current")

hpSwitchCertStatusGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 24)
)
hpSwitchCertStatusGroup3.setObjects(
    ("HP-AUTH-MIB", "hpSwitchServerNewCertKeySizeExists")
)
if mibBuilder.loadTexts:
    hpSwitchCertStatusGroup3.setStatus("current")

hpSwitchAuthenticationConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 25)
)
hpSwitchAuthenticationConfigGroup2.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthLockoutDelay"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthRespectPriv"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationEncryptCredentialsMethod"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup2.setStatus("deprecated")

hpSwitchRadiusConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 26)
)
hpSwitchRadiusConfigGroup2.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup2.setStatus("deprecated")

hpSwitchAuthenticationConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 27)
)
hpSwitchAuthenticationConfigGroup3.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthLockoutDelay"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthRespectPriv"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationEncryptCredentialsMethod"),
        ("HP-AUTH-MIB", "hpSwitchMinimumPasswordLength"),
        ("HP-AUTH-MIB", "hpSwitchAuthAllowVlanTagged"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup3.setStatus("deprecated")

hpSwitchAuthenticationConfigGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 28)
)
hpSwitchAuthenticationConfigGroup4.setObjects(
    ("HP-AUTH-MIB", "hpicfSwitchBypassUsername")
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup4.setStatus("current")

hpSwitchRadiusConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 29)
)
hpSwitchRadiusConfigGroup3.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTracking"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingUserName"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup3.setStatus("deprecated")

hpSwitchRipAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 31)
)
hpSwitchRipAuthGroup.setObjects(
    ("HP-AUTH-MIB", "hpSwitchRipIfAuthChain")
)
if mibBuilder.loadTexts:
    hpSwitchRipAuthGroup.setStatus("deprecated")

hpSwitchAuthenticationPasswordConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 32)
)
hpSwitchAuthenticationPasswordConfigGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthPwdControlCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdUserNameCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdRepeatCharactersCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdRepeatPasswordCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdAgingCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdLogonDetailsCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdAgingValue"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdHistoryCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdHistoryRecordsRange"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdAlertBeforeExpiry"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdExpiredUserLoginDays"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdExpiredUserLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdUpdateInterval"),
        ("HP-AUTH-MIB", "hpSwitchAuthenCompositionValue"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationPasswordConfigGroup.setStatus("deprecated")

hpSwitchUserConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 33)
)
hpSwitchUserConfigGroup2.setObjects(
      *(("HP-AUTH-MIB", "hpicfSwitchUserName"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorName"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessName"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPasswordEncrypted"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPasswordEncrypted"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPasswordEncrypted"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchUserConfigStatus"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPwdAgingInterval"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPwdAgingInterval"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPwdLengthValue"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPwdLengthValue"))
)
if mibBuilder.loadTexts:
    hpSwitchUserConfigGroup2.setStatus("deprecated")

hpSwitchAuthLocalMgmtPrivUserGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 34)
)
hpSwitchAuthLocalMgmtPrivUserGroup2.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernameStr"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernamePasswdType"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernamePasswd"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernameGrpIndex"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPwdUserAgingInterval"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPwdUserPasswdLengthValue"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthLocalMgmtPrivUserGroup2.setStatus("deprecated")

hpSwitchRadiusConfigGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 36)
)
hpSwitchRadiusConfigGroup4.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup4.setStatus("deprecated")

hpSwitchAuthenticationConfigGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 37)
)
hpSwitchAuthenticationConfigGroup5.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthLockoutDelay"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthRespectPriv"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationEncryptCredentialsMethod"),
        ("HP-AUTH-MIB", "hpSwitchMinimumPasswordLength"),
        ("HP-AUTH-MIB", "hpSwitchAuthAllowVlanTagged"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientSecondary"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup5.setStatus("deprecated")

hpSwitchUserConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 38)
)
hpSwitchUserConfigGroup3.setObjects(
      *(("HP-AUTH-MIB", "hpicfSwitchUserName"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorName"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessName"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPassword"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPasswordEncrypted"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPasswordEncrypted"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPasswordEncrypted"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchPortAccessPasswordHashType"),
        ("HP-AUTH-MIB", "hpicfSwitchUserConfigStatus"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPwdAgingInterval"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPwdAgingInterval"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPwdLengthValue"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPwdLengthValue"),
        ("HP-AUTH-MIB", "hpicfSwitchNonPlaintextSha256"),
        ("HP-AUTH-MIB", "hpicfSwitchUserPasswordHashSha256"),
        ("HP-AUTH-MIB", "hpicfSwitchOperatorPasswordHashSha256"))
)
if mibBuilder.loadTexts:
    hpSwitchUserConfigGroup3.setStatus("current")

hpSwitchAuthLocalMgmtPrivUserGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 39)
)
hpSwitchAuthLocalMgmtPrivUserGroup3.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernameStr"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernamePasswdType"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernamePasswd"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernameGrpIndex"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPwdUserAgingInterval"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPwdUserPasswdLengthValue"),
        ("HP-AUTH-MIB", "hpSwitchLocalMgmtPrivUsernamePasswdSha256"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthLocalMgmtPrivUserGroup3.setStatus("current")

hpSwitchOspfAuthGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 40)
)
hpSwitchOspfAuthGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchOspfVirtIfAuthChain"),
        ("HP-AUTH-MIB", "hpSwitchOspfIfAuthChain"),
        ("HP-AUTH-MIB", "hpSwitchOspfVirtIfAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchOspfIfAuthKeyEncrypted"))
)
if mibBuilder.loadTexts:
    hpSwitchOspfAuthGroup1.setStatus("current")

hpSwitchRipAuthGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 41)
)
hpSwitchRipAuthGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRipIfAuthChain"),
        ("HP-AUTH-MIB", "hpSwitchRip2IfConfAuthKeyEncrypted"))
)
if mibBuilder.loadTexts:
    hpSwitchRipAuthGroup1.setStatus("current")

hpSwitchAuthenticationConfigGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 42)
)
hpSwitchAuthenticationConfigGroup6.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthLockoutDelay"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthRespectPriv"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationEncryptCredentialsMethod"),
        ("HP-AUTH-MIB", "hpSwitchMinimumPasswordLength"),
        ("HP-AUTH-MIB", "hpSwitchAuthAllowVlanTagged"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenHideSensitiveData"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup6.setStatus("deprecated")

hpSwitchAuthenticationConfigGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 43)
)
hpSwitchAuthenticationConfigGroup7.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthLockoutDelay"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthRespectPriv"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationEncryptCredentialsMethod"),
        ("HP-AUTH-MIB", "hpSwitchMinimumPasswordLength"),
        ("HP-AUTH-MIB", "hpSwitchAuthAllowVlanTagged"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenHideSensitiveData"),
        ("HP-AUTH-MIB", "hpSwitchAuthUnlockUser"),
        ("HP-AUTH-MIB", "hpSwitchAuthUserBasedLockout"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup7.setStatus("deprecated")

hpSwitchRadiusConfigGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 44)
)
hpSwitchRadiusConfigGroup5.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmIdentity"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmEncryptedKey"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup5.setStatus("deprecated")

hpSwitchFrontPanelSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 45)
)
hpSwitchFrontPanelSecurityGroup.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchFpsPasswordClear"),
        ("HP-AUTH-MIB", "hpSwitchFpsFactoryReset"),
        ("HP-AUTH-MIB", "hpSwitchFpsPasswordRecovery"),
        ("HP-AUTH-MIB", "hpSwitchFpsDiagnosticResetClearButton"),
        ("HP-AUTH-MIB", "hpSwitchFpsDiagnosticResetSerialConsole"),
        ("HP-AUTH-MIB", "hpSwitchFpsDisplayInConfig"))
)
if mibBuilder.loadTexts:
    hpSwitchFrontPanelSecurityGroup.setStatus("current")

hpSwitchRadiusConfigGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 46)
)
hpSwitchRadiusConfigGroup6.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmIdentity"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmEncryptedKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingInterval"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup6.setStatus("deprecated")

hpSwitchAuthenticationConfigGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 47)
)
hpSwitchAuthenticationConfigGroup8.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthLockoutDelay"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthRespectPriv"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationEncryptCredentialsMethod"),
        ("HP-AUTH-MIB", "hpSwitchMinimumPasswordLength"),
        ("HP-AUTH-MIB", "hpSwitchAuthAllowVlanTagged"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenHideSensitiveData"),
        ("HP-AUTH-MIB", "hpSwitchAuthUnlockUser"),
        ("HP-AUTH-MIB", "hpSwitchAuthUserBasedLockout"),
        ("HP-AUTH-MIB", "hpSwitchAuthenCachedReauthAuthorized"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup8.setStatus("deprecated")

hpSwitchRadiusConfigGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 48)
)
hpSwitchRadiusConfigGroup7.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmIdentity"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmEncryptedKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingInterval"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingPassword"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackDeadOnly"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackReqPktCount"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackPassEncrypt"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup7.setStatus("deprecated")

hpSwitchAuthenticationConfigGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 49)
)
hpSwitchAuthenticationConfigGroup9.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthLockoutDelay"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthRespectPriv"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationEncryptCredentialsMethod"),
        ("HP-AUTH-MIB", "hpSwitchMinimumPasswordLength"),
        ("HP-AUTH-MIB", "hpSwitchAuthAllowVlanTagged"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenHideSensitiveData"),
        ("HP-AUTH-MIB", "hpSwitchAuthUnlockUser"),
        ("HP-AUTH-MIB", "hpSwitchAuthUserBasedLockout"),
        ("HP-AUTH-MIB", "hpSwitchAuthenCachedReauthAuthorized"),
        ("HP-AUTH-MIB", "hpSwitchAuthConsoleLockout"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup9.setStatus("deprecated")

hpSwitchTacacsConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 50)
)
hpSwitchTacacsConfigGroup2.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsTimeout"),
        ("HP-AUTH-MIB", "hpSwitchTacacsAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerAddressType"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchTacacsDeadTime"))
)
if mibBuilder.loadTexts:
    hpSwitchTacacsConfigGroup2.setStatus("deprecated")

hpSwitchTacacsStatsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 51)
)
hpSwitchTacacsStatsGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpTacacsStatsTacacsServerIpAddr"),
        ("HP-AUTH-MIB", "hpTacacsStatsTacacsServerAdrType"),
        ("HP-AUTH-MIB", "hpTacacsStatsTacacsServerAddr"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumSessOpened"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumSessClosed"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumSessAborted"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumSessErrors"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumPktsIn"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumPktsOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAuthPktsIn"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAuthPktsOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAuthPktsTimedOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAutzPktsIn"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAutzPktsOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAutzPktsTimedOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAcctPktsIn"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAcctPktsOut"),
        ("HP-AUTH-MIB", "hpTacacsStatsNumAcctPktsTimedOut"))
)
if mibBuilder.loadTexts:
    hpSwitchTacacsStatsGroup1.setStatus("current")

hpSwitchTacacsOobmGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 52)
)
hpSwitchTacacsOobmGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerAddressType"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerIsOobm"))
)
if mibBuilder.loadTexts:
    hpSwitchTacacsOobmGroup1.setStatus("current")

hpSwitchRadiusConfigGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 53)
)
hpSwitchRadiusConfigGroup8.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmIdentity"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmEncryptedKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingInterval"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingPassword"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackDeadOnly"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackReqPktCount"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackPassEncrypt"),
        ("HP-AUTH-MIB", "hpSwitchRadiusFramedIpv4Address"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup8.setStatus("deprecated")

hpSwitchRadiusConfigGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 54)
)
hpSwitchRadiusConfigGroup9.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmIdentity"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmEncryptedKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingInterval"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingPassword"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackDeadOnly"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackReqPktCount"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackPassEncrypt"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerFqdn"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsClearPass"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup9.setStatus("deprecated")

hpSwitchRadiusConfigGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 55)
)
hpSwitchRadiusConfigGroup10.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmIdentity"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmEncryptedKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingInterval"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingPassword"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackDeadOnly"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackReqPktCount"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackPassEncrypt"),
        ("HP-AUTH-MIB", "hpSwitchRadiusFramedIpv4Address"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerFqdn"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsClearPass"),
        ("HP-AUTH-MIB", "hpSwitchRadiusFqdnRetry"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup10.setStatus("deprecated")

hpSwitchRadiusConfigGroup11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 56)
)
hpSwitchRadiusConfigGroup11.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmIdentity"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmEncryptedKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingInterval"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingPassword"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackDeadOnly"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackReqPktCount"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackPassEncrypt"),
        ("HP-AUTH-MIB", "hpSwitchRadiusFramedIpv4Address"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerFqdn"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsClearPass"),
        ("HP-AUTH-MIB", "hpSwitchRadiusFqdnRetry"),
        ("HP-AUTH-MIB", "hpSwitchRadiusExcludeVsa"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup11.setStatus("deprecated")

hpSwitchAuthenticationPasswordConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 57)
)
hpSwitchAuthenticationPasswordConfigGroup1.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthPwdControlCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdUserNameCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdRepeatCharactersCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdRepeatPasswordCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdAgingCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdLogonDetailsCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdAgingValue"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdHistoryCheck"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdHistoryRecordsRange"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdAlertBeforeExpiry"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdExpiredUserLoginDays"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdExpiredUserLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdUpdateInterval"),
        ("HP-AUTH-MIB", "hpSwitchAuthenCompositionValue"),
        ("HP-AUTH-MIB", "hpSwitchAuthPwdCharPositionCheckValue"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationPasswordConfigGroup1.setStatus("current")

hpSwitchAuthenticationConfigGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 58)
)
hpSwitchAuthenticationConfigGroup10.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchNumLoginAttempts"),
        ("HP-AUTH-MIB", "hpSwitchAuthLockoutDelay"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnablePrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthRespectPriv"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationEncryptCredentialsMethod"),
        ("HP-AUTH-MIB", "hpSwitchMinimumPasswordLength"),
        ("HP-AUTH-MIB", "hpSwitchAuthAllowVlanTagged"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableTwoFactorType"),
        ("HP-AUTH-MIB", "hpSwitchAuthenLoginSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenEnableSecondAuthMethod"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientPrimary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenClientSecondary"),
        ("HP-AUTH-MIB", "hpSwitchAuthenHideSensitiveData"),
        ("HP-AUTH-MIB", "hpSwitchAuthUnlockUser"),
        ("HP-AUTH-MIB", "hpSwitchAuthUserBasedLockout"),
        ("HP-AUTH-MIB", "hpSwitchAuthenCachedReauthAuthorized"),
        ("HP-AUTH-MIB", "hpSwitchAuthConsoleLockout"),
        ("HP-AUTH-MIB", "hpSwitchTrackLoginAttempts"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationConfigGroup10.setStatus("current")

hpSwitchTacacsConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 59)
)
hpSwitchTacacsConfigGroup3.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsTimeout"),
        ("HP-AUTH-MIB", "hpSwitchTacacsAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerAddressType"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchTacacsDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchTacacsOrderingSequence"))
)
if mibBuilder.loadTexts:
    hpSwitchTacacsConfigGroup3.setStatus("deprecated")

hpSwitchRadiusConfigGroup12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 60)
)
hpSwitchRadiusConfigGroup12.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmIdentity"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmEncryptedKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingInterval"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingPassword"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackDeadOnly"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackReqPktCount"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackPassEncrypt"),
        ("HP-AUTH-MIB", "hpSwitchRadiusFramedIpv4Address"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerFqdn"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsClearPass"),
        ("HP-AUTH-MIB", "hpSwitchRadiusFqdnRetry"),
        ("HP-AUTH-MIB", "hpSwitchRadiusExcludeVsa"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSConnectionTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSEnable"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSPort"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSRetryTimer"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup12.setStatus("deprecated")

hpSwitchAAAServerGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 61)
)
hpSwitchAAAServerGroup2.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAAAServerGroupName"),
        ("HP-AUTH-MIB", "hpSwitchAAAServerGroupServerInetType"),
        ("HP-AUTH-MIB", "hpSwitchAAAServerGroupServerInetAddr"),
        ("HP-AUTH-MIB", "hpSwitchAAAServerGroupStatus"),
        ("HP-AUTH-MIB", "hpSwitchAAAServerGroupServerFqdn"),
        ("HP-AUTH-MIB", "hpSwitchAAAServerGroupTLSEnable"))
)
if mibBuilder.loadTexts:
    hpSwitchAAAServerGroup2.setStatus("current")

hpSwitchTacacsConfigGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 62)
)
hpSwitchTacacsConfigGroup4.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsTimeout"),
        ("HP-AUTH-MIB", "hpSwitchTacacsAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerIpAddr"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerAddressType"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerKey"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchTacacsDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchTacacsOrderingSequence"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerFqdn"),
        ("HP-AUTH-MIB", "hpSwitchTacacsServerFqdnRetry"))
)
if mibBuilder.loadTexts:
    hpSwitchTacacsConfigGroup4.setStatus("current")

hpSwitchRadiusConfigGroup13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 63)
)
hpSwitchRadiusConfigGroup13.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusRetransmitAttempts"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusAuthKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDynAutzPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddrType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAddress"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerKeyEncrypted"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAuthPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerAcctPortNumber"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzEnabled"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindow"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsOobm"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerStatus"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerDynAutzTimeWindowType"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmIdentity"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusCppmEncryptedKey"),
        ("HP-AUTH-MIB", "hpSwitchRadiusDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingInterval"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackingPassword"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackDeadOnly"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackReqPktCount"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTrackPassEncrypt"),
        ("HP-AUTH-MIB", "hpSwitchRadiusFramedIpv4Address"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerFqdn"),
        ("HP-AUTH-MIB", "hpSwitchRadiusServerIsClearPass"),
        ("HP-AUTH-MIB", "hpSwitchRadiusFqdnRetry"),
        ("HP-AUTH-MIB", "hpSwitchRadiusExcludeVsa"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSConnectionTimeout"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSDeadTime"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSDeadTimeInfinite"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSEnable"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSPort"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTLSRetryTimer"),
        ("HP-AUTH-MIB", "hpSwitchRadiusTunnelPrivateGroupId"))
)
if mibBuilder.loadTexts:
    hpSwitchRadiusConfigGroup13.setStatus("current")


# Notification objects

hpSwitchPasswordExpiryNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 0, 1)
)
hpSwitchPasswordExpiryNotify.setObjects(
    ("HP-AUTH-MIB", "hpicfSwitchUserName")
)
if mibBuilder.loadTexts:
    hpSwitchPasswordExpiryNotify.setStatus(
        "current"
    )


# Notifications groups

hpSwitchAuthNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 2, 35)
)
hpSwitchAuthNotificationGroup.setObjects(
    ("HP-AUTH-MIB", "hpSwitchPasswordExpiryNotify")
)
if mibBuilder.loadTexts:
    hpSwitchAuthNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpSwitchAuthenticationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 1)
)
hpSwitchAuthenticationMIBCompliance.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup"),
        ("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 2)
)
hpSwitchAuthenticationMIBCompliance1.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup"),
        ("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup2"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance1.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 3)
)
hpSwitchAuthenticationMIBCompliance2.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance2.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBComplianceOobm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 4)
)
hpSwitchAuthenticationMIBComplianceOobm.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchRadiusOobmGroup"),
        ("HP-AUTH-MIB", "hpSwitchTacacsOobmGroup"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBComplianceOobm.setStatus(
        "deprecated"
    )

hpSwitchUserConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 5)
)
hpSwitchUserConfigMIBCompliance.setObjects(
    ("HP-AUTH-MIB", "hpSwitchUserConfigGroup")
)
if mibBuilder.loadTexts:
    hpSwitchUserConfigMIBCompliance.setStatus(
        "deprecated"
    )

hpSwitchAAAServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 6)
)
hpSwitchAAAServerMIBCompliance.setObjects(
    ("HP-AUTH-MIB", "hpSwitchAAAServerGroup")
)
if mibBuilder.loadTexts:
    hpSwitchAAAServerMIBCompliance.setStatus(
        "deprecated"
    )

hpSwitchAuthenMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 7)
)
hpSwitchAuthenMIBCompliance.setObjects(
    ("HP-AUTH-MIB", "hpSwitchAuthenGroup")
)
if mibBuilder.loadTexts:
    hpSwitchAuthenMIBCompliance.setStatus(
        "current"
    )

hpSwitchLocalMgmtPrivUserMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 8)
)
hpSwitchLocalMgmtPrivUserMIBCompliance.setObjects(
    ("HP-AUTH-MIB", "hpSwitchAuthLocalMgmtPrivUserGroup")
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUserMIBCompliance.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 9)
)
hpSwitchAuthenticationMIBCompliance3.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance3.setStatus(
        "deprecated"
    )

hpSwitchUserConfigMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 10)
)
hpSwitchUserConfigMIBCompliance1.setObjects(
    ("HP-AUTH-MIB", "hpSwitchUserConfigGroup1")
)
if mibBuilder.loadTexts:
    hpSwitchUserConfigMIBCompliance1.setStatus(
        "deprecated"
    )

hpSwitchLocalMgmtPrivUserMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 11)
)
hpSwitchLocalMgmtPrivUserMIBCompliance1.setObjects(
    ("HP-AUTH-MIB", "hpSwitchAuthLocalMgmtPrivUserGroup1")
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUserMIBCompliance1.setStatus(
        "current"
    )

hpSwitchAuthenticationMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 12)
)
hpSwitchAuthenticationMIBCompliance4.setObjects(
    ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3")
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance4.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 13)
)
hpSwitchAuthenticationMIBCompliance5.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup2"),
        ("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance5.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBComplianceOobm1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 14)
)
hpSwitchAuthenticationMIBComplianceOobm1.setObjects(
    ("HP-AUTH-MIB", "hpSwitchTacacsOobmGroup")
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBComplianceOobm1.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 15)
)
hpSwitchAuthenticationMIBCompliance6.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup2"),
        ("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup2"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance6.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 16)
)
hpSwitchAuthenticationMIBCompliance7.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup3"),
        ("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup2"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance7.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 17)
)
hpSwitchAuthenticationMIBCompliance8.setObjects(
    ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup4")
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance8.setStatus(
        "current"
    )

hpSwitchAuthenticationMIBCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 18)
)
hpSwitchAuthenticationMIBCompliance9.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup3"),
        ("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup3"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance9.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 19)
)
hpSwitchAuthenticationMIBCompliance10.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationPasswordConfigGroup"),
        ("HP-AUTH-MIB", "hpSwitchAuthNotificationGroup"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance10.setStatus(
        "deprecated"
    )

hpSwitchLocalMgmtPrivUserMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 20)
)
hpSwitchLocalMgmtPrivUserMIBCompliance2.setObjects(
    ("HP-AUTH-MIB", "hpSwitchAuthLocalMgmtPrivUserGroup2")
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUserMIBCompliance2.setStatus(
        "deprecated"
    )

hpSwitchUserConfigMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 21)
)
hpSwitchUserConfigMIBCompliance2.setObjects(
    ("HP-AUTH-MIB", "hpSwitchUserConfigGroup2")
)
if mibBuilder.loadTexts:
    hpSwitchUserConfigMIBCompliance2.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 22)
)
hpSwitchAuthenticationMIBCompliance11.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup3"),
        ("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup4"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance11.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 23)
)
hpSwitchAuthenticationMIBCompliance12.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup4"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup5"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance12.setStatus(
        "deprecated"
    )

hpSwitchUserConfigMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 24)
)
hpSwitchUserConfigMIBCompliance3.setObjects(
    ("HP-AUTH-MIB", "hpSwitchUserConfigGroup3")
)
if mibBuilder.loadTexts:
    hpSwitchUserConfigMIBCompliance3.setStatus(
        "current"
    )

hpSwitchLocalMgmtPrivUserMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 25)
)
hpSwitchLocalMgmtPrivUserMIBCompliance3.setObjects(
    ("HP-AUTH-MIB", "hpSwitchAuthLocalMgmtPrivUserGroup3")
)
if mibBuilder.loadTexts:
    hpSwitchLocalMgmtPrivUserMIBCompliance3.setStatus(
        "current"
    )

hpSwitchAuthenticationMIBCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 26)
)
hpSwitchAuthenticationMIBCompliance13.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup4"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup5"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance13.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 27)
)
hpSwitchAuthenticationMIBCompliance14.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup4"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup6"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance14.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 28)
)
hpSwitchAuthenticationMIBCompliance15.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup4"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup7"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance15.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 29)
)
hpSwitchAuthenticationMIBCompliance16.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup5"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup7"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance16.setStatus(
        "deprecated"
    )

hpSwitchFrontPanelSecurityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 30)
)
hpSwitchFrontPanelSecurityCompliance.setObjects(
    ("HP-AUTH-MIB", "hpSwitchFrontPanelSecurityGroup")
)
if mibBuilder.loadTexts:
    hpSwitchFrontPanelSecurityCompliance.setStatus(
        "current"
    )

hpSwitchAuthenticationMIBCompliance17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 31)
)
hpSwitchAuthenticationMIBCompliance17.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup6"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup8"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance17.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 32)
)
hpSwitchAuthenticationMIBCompliance18.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup7"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup9"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance18.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 33)
)
hpSwitchAuthenticationMIBCompliance19.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup2"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup7"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup9"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance19.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBComplianceOobm2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 34)
)
hpSwitchAuthenticationMIBComplianceOobm2.setObjects(
    ("HP-AUTH-MIB", "hpSwitchTacacsOobmGroup1")
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBComplianceOobm2.setStatus(
        "current"
    )

hpSwitchAuthenticationMIBCompliance20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 35)
)
hpSwitchAuthenticationMIBCompliance20.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup2"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup8"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup9"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance20.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 37)
)
hpSwitchAuthenticationMIBCompliance21.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup2"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup9"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup9"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance21.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 38)
)
hpSwitchAuthenticationMIBCompliance22.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup2"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup10"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup9"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance22.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 39)
)
hpSwitchAuthenticationMIBCompliance23.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup2"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup11"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup9"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance23.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance24 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 40)
)
hpSwitchAuthenticationMIBCompliance24.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchAuthenticationPasswordConfigGroup1"),
        ("HP-AUTH-MIB", "hpSwitchAuthNotificationGroup"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance24.setStatus(
        "current"
    )

hpSwitchAuthenticationMIBCompliance26 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 42)
)
hpSwitchAuthenticationMIBCompliance26.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup3"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup10"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup9"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance26.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance27 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 43)
)
hpSwitchAuthenticationMIBCompliance27.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup3"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup12"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup10"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance27.setStatus(
        "deprecated"
    )

hpSwitchAAAServerMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 44)
)
hpSwitchAAAServerMIBCompliance2.setObjects(
    ("HP-AUTH-MIB", "hpSwitchAAAServerGroup2")
)
if mibBuilder.loadTexts:
    hpSwitchAAAServerMIBCompliance2.setStatus(
        "current"
    )

hpSwitchAuthenticationMIBCompliance28 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 45)
)
hpSwitchAuthenticationMIBCompliance28.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup4"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup12"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup10"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance28.setStatus(
        "deprecated"
    )

hpSwitchAuthenticationMIBCompliance29 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16, 11, 1, 46)
)
hpSwitchAuthenticationMIBCompliance29.setObjects(
      *(("HP-AUTH-MIB", "hpSwitchTacacsConfigGroup4"),
        ("HP-AUTH-MIB", "hpSwitchTacacsStatsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchRadiusConfigGroup13"),
        ("HP-AUTH-MIB", "hpSwitchAuthenticationConfigGroup10"),
        ("HP-AUTH-MIB", "hpSwitchKmsGroup1"),
        ("HP-AUTH-MIB", "hpSwitchOspfAuthGroup1"),
        ("HP-AUTH-MIB", "hpSwitchSslGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup"),
        ("HP-AUTH-MIB", "hpSwitchCertStatusGroup3"),
        ("HP-AUTH-MIB", "hpSwitchRipAuthGroup1"))
)
if mibBuilder.loadTexts:
    hpSwitchAuthenticationMIBCompliance29.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-AUTH-MIB",
    **{"hpSwitchAuthenticationMIB": hpSwitchAuthenticationMIB,
       "hpSwitchAuthNotifications": hpSwitchAuthNotifications,
       "hpSwitchPasswordExpiryNotify": hpSwitchPasswordExpiryNotify,
       "hpSwitchAuthenticationConfig": hpSwitchAuthenticationConfig,
       "hpSwitchNumLoginAttempts": hpSwitchNumLoginAttempts,
       "hpSwitchAuthRespectPriv": hpSwitchAuthRespectPriv,
       "hpSwitchAuthenticationEncryptCredentialsMethod": hpSwitchAuthenticationEncryptCredentialsMethod,
       "hpSwitchAuthLockoutDelay": hpSwitchAuthLockoutDelay,
       "hpSwitchMinimumPasswordLength": hpSwitchMinimumPasswordLength,
       "hpSwitchAuthAllowVlanTagged": hpSwitchAuthAllowVlanTagged,
       "hpSwitchAuthenHideSensitiveData": hpSwitchAuthenHideSensitiveData,
       "hpSwitchAuthUnlockUser": hpSwitchAuthUnlockUser,
       "hpSwitchAuthUserBasedLockout": hpSwitchAuthUserBasedLockout,
       "hpSwitchAuthConsoleLockout": hpSwitchAuthConsoleLockout,
       "hpSwitchTrackLoginAttempts": hpSwitchTrackLoginAttempts,
       "hpSwitchAuthenTable": hpSwitchAuthenTable,
       "hpSwitchAuthenEntry": hpSwitchAuthenEntry,
       "hpSwitchAuthenIndex": hpSwitchAuthenIndex,
       "hpSwitchAuthenLoginPrimary": hpSwitchAuthenLoginPrimary,
       "hpSwitchAuthenLoginSecondary": hpSwitchAuthenLoginSecondary,
       "hpSwitchAuthenEnablePrimary": hpSwitchAuthenEnablePrimary,
       "hpSwitchAuthenEnableSecondary": hpSwitchAuthenEnableSecondary,
       "hpSwitchAuthenLoginServerGroupName": hpSwitchAuthenLoginServerGroupName,
       "hpSwitchAuthenEnableServerGroupName": hpSwitchAuthenEnableServerGroupName,
       "hpSwitchAuthenLoginTwoFactorType": hpSwitchAuthenLoginTwoFactorType,
       "hpSwitchAuthenEnableTwoFactorType": hpSwitchAuthenEnableTwoFactorType,
       "hpSwitchAuthenLoginSecondAuthMethod": hpSwitchAuthenLoginSecondAuthMethod,
       "hpSwitchAuthenEnableSecondAuthMethod": hpSwitchAuthenEnableSecondAuthMethod,
       "hpSwitchAuthenClientPrimary": hpSwitchAuthenClientPrimary,
       "hpSwitchAuthenClientSecondary": hpSwitchAuthenClientSecondary,
       "hpSwitchAuthenCachedReauthAuthorized": hpSwitchAuthenCachedReauthAuthorized,
       "hpSwitchTacacsConfig": hpSwitchTacacsConfig,
       "hpSwitchTacacsTimeout": hpSwitchTacacsTimeout,
       "hpSwitchTacacsAuthKey": hpSwitchTacacsAuthKey,
       "hpSwitchTacacsAuthKeyEncrypted": hpSwitchTacacsAuthKeyEncrypted,
       "hpSwitchTacacsDeadTime": hpSwitchTacacsDeadTime,
       "hpSwitchTacacsOrderingSequence": hpSwitchTacacsOrderingSequence,
       "hpSwitchTacacsServerFqdnRetry": hpSwitchTacacsServerFqdnRetry,
       "hpSwitchTacacsServersTable": hpSwitchTacacsServersTable,
       "hpSwitchTacacsServersEntry": hpSwitchTacacsServersEntry,
       "hpSwitchTacacsServerIndex": hpSwitchTacacsServerIndex,
       "hpSwitchTacacsServerIpAddr": hpSwitchTacacsServerIpAddr,
       "hpSwitchTacacsServerKey": hpSwitchTacacsServerKey,
       "hpSwitchTacacsServerStatus": hpSwitchTacacsServerStatus,
       "hpSwitchTacacsServerIsOobm": hpSwitchTacacsServerIsOobm,
       "hpSwitchTacacsServerKeyEncrypted": hpSwitchTacacsServerKeyEncrypted,
       "hpSwitchTacacsServerAddressType": hpSwitchTacacsServerAddressType,
       "hpSwitchTacacsServerAddress": hpSwitchTacacsServerAddress,
       "hpSwitchTacacsServerFqdn": hpSwitchTacacsServerFqdn,
       "hpTacacsStatsServersTable": hpTacacsStatsServersTable,
       "hpTacacsStatsServersEntry": hpTacacsStatsServersEntry,
       "hpTacacsStatsServerIndex": hpTacacsStatsServerIndex,
       "hpTacacsStatsTacacsServerIpAddr": hpTacacsStatsTacacsServerIpAddr,
       "hpTacacsStatsNumSessOpened": hpTacacsStatsNumSessOpened,
       "hpTacacsStatsNumSessClosed": hpTacacsStatsNumSessClosed,
       "hpTacacsStatsNumSessAborted": hpTacacsStatsNumSessAborted,
       "hpTacacsStatsNumSessErrors": hpTacacsStatsNumSessErrors,
       "hpTacacsStatsNumPktsIn": hpTacacsStatsNumPktsIn,
       "hpTacacsStatsNumPktsOut": hpTacacsStatsNumPktsOut,
       "hpTacacsStatsNumAuthPktsIn": hpTacacsStatsNumAuthPktsIn,
       "hpTacacsStatsNumAuthPktsOut": hpTacacsStatsNumAuthPktsOut,
       "hpTacacsStatsNumAuthPktsTimedOut": hpTacacsStatsNumAuthPktsTimedOut,
       "hpTacacsStatsNumAutzPktsIn": hpTacacsStatsNumAutzPktsIn,
       "hpTacacsStatsNumAutzPktsOut": hpTacacsStatsNumAutzPktsOut,
       "hpTacacsStatsNumAutzPktsTimedOut": hpTacacsStatsNumAutzPktsTimedOut,
       "hpTacacsStatsNumAcctPktsIn": hpTacacsStatsNumAcctPktsIn,
       "hpTacacsStatsNumAcctPktsOut": hpTacacsStatsNumAcctPktsOut,
       "hpTacacsStatsNumAcctPktsTimedOut": hpTacacsStatsNumAcctPktsTimedOut,
       "hpTacacsStatsTacacsServerAdrType": hpTacacsStatsTacacsServerAdrType,
       "hpTacacsStatsTacacsServerAddr": hpTacacsStatsTacacsServerAddr,
       "hpSwitchRadiusConfig": hpSwitchRadiusConfig,
       "hpSwitchRadiusDeadTime": hpSwitchRadiusDeadTime,
       "hpSwitchRadiusTimeout": hpSwitchRadiusTimeout,
       "hpSwitchRadiusRetransmitAttempts": hpSwitchRadiusRetransmitAttempts,
       "hpSwitchRadiusAuthKey": hpSwitchRadiusAuthKey,
       "hpSwitchRadiusDynAutzPortNumber": hpSwitchRadiusDynAutzPortNumber,
       "hpSwitchRadiusAuthKeyEncrypted": hpSwitchRadiusAuthKeyEncrypted,
       "hpSwitchRadiusTracking": hpSwitchRadiusTracking,
       "hpSwitchRadiusTrackingUserName": hpSwitchRadiusTrackingUserName,
       "hpSwitchRadiusCppmIdentity": hpSwitchRadiusCppmIdentity,
       "hpSwitchRadiusCppmKey": hpSwitchRadiusCppmKey,
       "hpSwitchRadiusCppmEncryptedKey": hpSwitchRadiusCppmEncryptedKey,
       "hpSwitchRadiusDeadTimeInfinite": hpSwitchRadiusDeadTimeInfinite,
       "hpSwitchRadiusTrackingInterval": hpSwitchRadiusTrackingInterval,
       "hpSwitchRadiusTrackingPassword": hpSwitchRadiusTrackingPassword,
       "hpSwitchRadiusTrackDeadOnly": hpSwitchRadiusTrackDeadOnly,
       "hpSwitchRadiusTrackReqPktCount": hpSwitchRadiusTrackReqPktCount,
       "hpSwitchRadiusTrackPassEncrypt": hpSwitchRadiusTrackPassEncrypt,
       "hpSwitchRadiusFramedIpv4Address": hpSwitchRadiusFramedIpv4Address,
       "hpSwitchRadiusFqdnRetry": hpSwitchRadiusFqdnRetry,
       "hpSwitchRadiusExcludeVsa": hpSwitchRadiusExcludeVsa,
       "hpSwitchRadiusTLSTimeout": hpSwitchRadiusTLSTimeout,
       "hpSwitchRadiusTLSConnectionTimeout": hpSwitchRadiusTLSConnectionTimeout,
       "hpSwitchRadiusTLSDeadTime": hpSwitchRadiusTLSDeadTime,
       "hpSwitchRadiusTLSDeadTimeInfinite": hpSwitchRadiusTLSDeadTimeInfinite,
       "hpSwitchRadiusTunnelPrivateGroupId": hpSwitchRadiusTunnelPrivateGroupId,
       "hpSwitchRadiusServerTable": hpSwitchRadiusServerTable,
       "hpSwitchRadiusServerEntry": hpSwitchRadiusServerEntry,
       "hpSwitchRadiusServerIndex": hpSwitchRadiusServerIndex,
       "hpSwitchRadiusServerIpAddr": hpSwitchRadiusServerIpAddr,
       "hpSwitchRadiusServerKey": hpSwitchRadiusServerKey,
       "hpSwitchRadiusServerAuthPortNumber": hpSwitchRadiusServerAuthPortNumber,
       "hpSwitchRadiusServerAcctPortNumber": hpSwitchRadiusServerAcctPortNumber,
       "hpSwitchRadiusServerDynAutzEnabled": hpSwitchRadiusServerDynAutzEnabled,
       "hpSwitchRadiusServerDynAutzTimeWindow": hpSwitchRadiusServerDynAutzTimeWindow,
       "hpSwitchRadiusServerStatus": hpSwitchRadiusServerStatus,
       "hpSwitchRadiusServerIsOobm": hpSwitchRadiusServerIsOobm,
       "hpSwitchRadiusServerKeyEncrypted": hpSwitchRadiusServerKeyEncrypted,
       "hpSwitchRadiusServerAddrType": hpSwitchRadiusServerAddrType,
       "hpSwitchRadiusServerAddress": hpSwitchRadiusServerAddress,
       "hpSwitchRadiusServerDynAutzTimeWindowType": hpSwitchRadiusServerDynAutzTimeWindowType,
       "hpSwitchRadiusServerFqdn": hpSwitchRadiusServerFqdn,
       "hpSwitchRadiusServerIsClearPass": hpSwitchRadiusServerIsClearPass,
       "hpSwitchRadiusTLSEnable": hpSwitchRadiusTLSEnable,
       "hpSwitchRadiusTLSPort": hpSwitchRadiusTLSPort,
       "hpSwitchRadiusTLSRetryTimer": hpSwitchRadiusTLSRetryTimer,
       "hpSwitchAuthenticationMIBConformance": hpSwitchAuthenticationMIBConformance,
       "hpSwitchAuthenticationMIBCompliances": hpSwitchAuthenticationMIBCompliances,
       "hpSwitchAuthenticationMIBCompliance": hpSwitchAuthenticationMIBCompliance,
       "hpSwitchAuthenticationMIBCompliance1": hpSwitchAuthenticationMIBCompliance1,
       "hpSwitchAuthenticationMIBCompliance2": hpSwitchAuthenticationMIBCompliance2,
       "hpSwitchAuthenticationMIBComplianceOobm": hpSwitchAuthenticationMIBComplianceOobm,
       "hpSwitchUserConfigMIBCompliance": hpSwitchUserConfigMIBCompliance,
       "hpSwitchAAAServerMIBCompliance": hpSwitchAAAServerMIBCompliance,
       "hpSwitchAuthenMIBCompliance": hpSwitchAuthenMIBCompliance,
       "hpSwitchLocalMgmtPrivUserMIBCompliance": hpSwitchLocalMgmtPrivUserMIBCompliance,
       "hpSwitchAuthenticationMIBCompliance3": hpSwitchAuthenticationMIBCompliance3,
       "hpSwitchUserConfigMIBCompliance1": hpSwitchUserConfigMIBCompliance1,
       "hpSwitchLocalMgmtPrivUserMIBCompliance1": hpSwitchLocalMgmtPrivUserMIBCompliance1,
       "hpSwitchAuthenticationMIBCompliance4": hpSwitchAuthenticationMIBCompliance4,
       "hpSwitchAuthenticationMIBCompliance5": hpSwitchAuthenticationMIBCompliance5,
       "hpSwitchAuthenticationMIBComplianceOobm1": hpSwitchAuthenticationMIBComplianceOobm1,
       "hpSwitchAuthenticationMIBCompliance6": hpSwitchAuthenticationMIBCompliance6,
       "hpSwitchAuthenticationMIBCompliance7": hpSwitchAuthenticationMIBCompliance7,
       "hpSwitchAuthenticationMIBCompliance8": hpSwitchAuthenticationMIBCompliance8,
       "hpSwitchAuthenticationMIBCompliance9": hpSwitchAuthenticationMIBCompliance9,
       "hpSwitchAuthenticationMIBCompliance10": hpSwitchAuthenticationMIBCompliance10,
       "hpSwitchLocalMgmtPrivUserMIBCompliance2": hpSwitchLocalMgmtPrivUserMIBCompliance2,
       "hpSwitchUserConfigMIBCompliance2": hpSwitchUserConfigMIBCompliance2,
       "hpSwitchAuthenticationMIBCompliance11": hpSwitchAuthenticationMIBCompliance11,
       "hpSwitchAuthenticationMIBCompliance12": hpSwitchAuthenticationMIBCompliance12,
       "hpSwitchUserConfigMIBCompliance3": hpSwitchUserConfigMIBCompliance3,
       "hpSwitchLocalMgmtPrivUserMIBCompliance3": hpSwitchLocalMgmtPrivUserMIBCompliance3,
       "hpSwitchAuthenticationMIBCompliance13": hpSwitchAuthenticationMIBCompliance13,
       "hpSwitchAuthenticationMIBCompliance14": hpSwitchAuthenticationMIBCompliance14,
       "hpSwitchAuthenticationMIBCompliance15": hpSwitchAuthenticationMIBCompliance15,
       "hpSwitchAuthenticationMIBCompliance16": hpSwitchAuthenticationMIBCompliance16,
       "hpSwitchFrontPanelSecurityCompliance": hpSwitchFrontPanelSecurityCompliance,
       "hpSwitchAuthenticationMIBCompliance17": hpSwitchAuthenticationMIBCompliance17,
       "hpSwitchAuthenticationMIBCompliance18": hpSwitchAuthenticationMIBCompliance18,
       "hpSwitchAuthenticationMIBCompliance19": hpSwitchAuthenticationMIBCompliance19,
       "hpSwitchAuthenticationMIBComplianceOobm2": hpSwitchAuthenticationMIBComplianceOobm2,
       "hpSwitchAuthenticationMIBCompliance20": hpSwitchAuthenticationMIBCompliance20,
       "hpSwitchAuthenticationMIBCompliance21": hpSwitchAuthenticationMIBCompliance21,
       "hpSwitchAuthenticationMIBCompliance22": hpSwitchAuthenticationMIBCompliance22,
       "hpSwitchAuthenticationMIBCompliance23": hpSwitchAuthenticationMIBCompliance23,
       "hpSwitchAuthenticationMIBCompliance24": hpSwitchAuthenticationMIBCompliance24,
       "hpSwitchAuthenticationMIBCompliance26": hpSwitchAuthenticationMIBCompliance26,
       "hpSwitchAuthenticationMIBCompliance27": hpSwitchAuthenticationMIBCompliance27,
       "hpSwitchAAAServerMIBCompliance2": hpSwitchAAAServerMIBCompliance2,
       "hpSwitchAuthenticationMIBCompliance28": hpSwitchAuthenticationMIBCompliance28,
       "hpSwitchAuthenticationMIBCompliance29": hpSwitchAuthenticationMIBCompliance29,
       "hpSwitchAuthenticationMIBGroups": hpSwitchAuthenticationMIBGroups,
       "hpSwitchAuthenticationConfigGroup": hpSwitchAuthenticationConfigGroup,
       "hpSwitchTacacsConfigGroup": hpSwitchTacacsConfigGroup,
       "hpSwitchTacacsStatsGroup": hpSwitchTacacsStatsGroup,
       "hpSwitchRadiusConfigGroup": hpSwitchRadiusConfigGroup,
       "hpSwitchKmsGroup": hpSwitchKmsGroup,
       "hpSwitchOspfAuthGroup": hpSwitchOspfAuthGroup,
       "hpSwitchAuthenticationConfigGroup1": hpSwitchAuthenticationConfigGroup1,
       "hpSwitchSslGroup": hpSwitchSslGroup,
       "hpSwitchCertGroup": hpSwitchCertGroup,
       "hpSwitchCertStatusGroup": hpSwitchCertStatusGroup,
       "hpSwitchTacacsOobmGroup": hpSwitchTacacsOobmGroup,
       "hpSwitchRadiusOobmGroup": hpSwitchRadiusOobmGroup,
       "hpSwitchCertStatusGroup2": hpSwitchCertStatusGroup2,
       "hpSwitchUserConfigGroup": hpSwitchUserConfigGroup,
       "hpSwitchAAAServerGroup": hpSwitchAAAServerGroup,
       "hpSwitchAuthenGroup": hpSwitchAuthenGroup,
       "hpSwitchAuthLocalMgmtPrivUserGroup": hpSwitchAuthLocalMgmtPrivUserGroup,
       "hpSwitchTacacsConfigGroup1": hpSwitchTacacsConfigGroup1,
       "hpSwitchRadiusConfigGroup1": hpSwitchRadiusConfigGroup1,
       "hpSwitchKmsGroup1": hpSwitchKmsGroup1,
       "hpSwitchUserConfigGroup1": hpSwitchUserConfigGroup1,
       "hpSwitchAuthLocalMgmtPrivUserGroup1": hpSwitchAuthLocalMgmtPrivUserGroup1,
       "hpSwitchCertStatusGroup3": hpSwitchCertStatusGroup3,
       "hpSwitchAuthenticationConfigGroup2": hpSwitchAuthenticationConfigGroup2,
       "hpSwitchRadiusConfigGroup2": hpSwitchRadiusConfigGroup2,
       "hpSwitchAuthenticationConfigGroup3": hpSwitchAuthenticationConfigGroup3,
       "hpSwitchAuthenticationConfigGroup4": hpSwitchAuthenticationConfigGroup4,
       "hpSwitchRadiusConfigGroup3": hpSwitchRadiusConfigGroup3,
       "hpSwitchRipAuthGroup": hpSwitchRipAuthGroup,
       "hpSwitchAuthenticationPasswordConfigGroup": hpSwitchAuthenticationPasswordConfigGroup,
       "hpSwitchUserConfigGroup2": hpSwitchUserConfigGroup2,
       "hpSwitchAuthLocalMgmtPrivUserGroup2": hpSwitchAuthLocalMgmtPrivUserGroup2,
       "hpSwitchAuthNotificationGroup": hpSwitchAuthNotificationGroup,
       "hpSwitchRadiusConfigGroup4": hpSwitchRadiusConfigGroup4,
       "hpSwitchAuthenticationConfigGroup5": hpSwitchAuthenticationConfigGroup5,
       "hpSwitchUserConfigGroup3": hpSwitchUserConfigGroup3,
       "hpSwitchAuthLocalMgmtPrivUserGroup3": hpSwitchAuthLocalMgmtPrivUserGroup3,
       "hpSwitchOspfAuthGroup1": hpSwitchOspfAuthGroup1,
       "hpSwitchRipAuthGroup1": hpSwitchRipAuthGroup1,
       "hpSwitchAuthenticationConfigGroup6": hpSwitchAuthenticationConfigGroup6,
       "hpSwitchAuthenticationConfigGroup7": hpSwitchAuthenticationConfigGroup7,
       "hpSwitchRadiusConfigGroup5": hpSwitchRadiusConfigGroup5,
       "hpSwitchFrontPanelSecurityGroup": hpSwitchFrontPanelSecurityGroup,
       "hpSwitchRadiusConfigGroup6": hpSwitchRadiusConfigGroup6,
       "hpSwitchAuthenticationConfigGroup8": hpSwitchAuthenticationConfigGroup8,
       "hpSwitchRadiusConfigGroup7": hpSwitchRadiusConfigGroup7,
       "hpSwitchAuthenticationConfigGroup9": hpSwitchAuthenticationConfigGroup9,
       "hpSwitchTacacsConfigGroup2": hpSwitchTacacsConfigGroup2,
       "hpSwitchTacacsStatsGroup1": hpSwitchTacacsStatsGroup1,
       "hpSwitchTacacsOobmGroup1": hpSwitchTacacsOobmGroup1,
       "hpSwitchRadiusConfigGroup8": hpSwitchRadiusConfigGroup8,
       "hpSwitchRadiusConfigGroup9": hpSwitchRadiusConfigGroup9,
       "hpSwitchRadiusConfigGroup10": hpSwitchRadiusConfigGroup10,
       "hpSwitchRadiusConfigGroup11": hpSwitchRadiusConfigGroup11,
       "hpSwitchAuthenticationPasswordConfigGroup1": hpSwitchAuthenticationPasswordConfigGroup1,
       "hpSwitchAuthenticationConfigGroup10": hpSwitchAuthenticationConfigGroup10,
       "hpSwitchTacacsConfigGroup3": hpSwitchTacacsConfigGroup3,
       "hpSwitchRadiusConfigGroup12": hpSwitchRadiusConfigGroup12,
       "hpSwitchAAAServerGroup2": hpSwitchAAAServerGroup2,
       "hpSwitchTacacsConfigGroup4": hpSwitchTacacsConfigGroup4,
       "hpSwitchRadiusConfigGroup13": hpSwitchRadiusConfigGroup13,
       "hpSwitchSslConfig": hpSwitchSslConfig,
       "hpSwitchSslAdminStatus": hpSwitchSslAdminStatus,
       "hpSwitchSslPortNumber": hpSwitchSslPortNumber,
       "hpSwitchCertConfig": hpSwitchCertConfig,
       "hpSwitchServerCertificateOperation": hpSwitchServerCertificateOperation,
       "hpSwitchServerNewRSAKeyOperation": hpSwitchServerNewRSAKeyOperation,
       "hpSwitchServerNewCertificateStartDate": hpSwitchServerNewCertificateStartDate,
       "hpSwitchServerNewCertificateEndDate": hpSwitchServerNewCertificateEndDate,
       "hpSwitchServerNewCertificateCommonName": hpSwitchServerNewCertificateCommonName,
       "hpSwitchServerNewCertificateOrgUnit": hpSwitchServerNewCertificateOrgUnit,
       "hpSwitchServerNewCertificateOrgName": hpSwitchServerNewCertificateOrgName,
       "hpSwitchServerNewCertificateCityName": hpSwitchServerNewCertificateCityName,
       "hpSwitchServerNewCertificateStateName": hpSwitchServerNewCertificateStateName,
       "hpSwitchServerNewCertificateCountryCode": hpSwitchServerNewCertificateCountryCode,
       "hpSwitchServerNewCertCommonName": hpSwitchServerNewCertCommonName,
       "hpSwitchServerNewCertOrgUnit": hpSwitchServerNewCertOrgUnit,
       "hpSwitchServerNewCertOrgName": hpSwitchServerNewCertOrgName,
       "hpSwitchServerNewCertCityName": hpSwitchServerNewCertCityName,
       "hpSwitchServerNewCertStateName": hpSwitchServerNewCertStateName,
       "hpSwitchServerNewCertKeySizeExists": hpSwitchServerNewCertKeySizeExists,
       "hpSwitchCertStatus": hpSwitchCertStatus,
       "hpSwitchServerCertificateType": hpSwitchServerCertificateType,
       "hpSwitchServerCertificateRSAKeySize": hpSwitchServerCertificateRSAKeySize,
       "hpSwitchServerCertificateSerialNumber": hpSwitchServerCertificateSerialNumber,
       "hpSwitchServerCertificateStartDate": hpSwitchServerCertificateStartDate,
       "hpSwitchServerCertificateEndDate": hpSwitchServerCertificateEndDate,
       "hpSwitchServerCertificateCommonName": hpSwitchServerCertificateCommonName,
       "hpSwitchServerCertificateOrgUnit": hpSwitchServerCertificateOrgUnit,
       "hpSwitchServerCertificateOrgName": hpSwitchServerCertificateOrgName,
       "hpSwitchServerCertificateCityName": hpSwitchServerCertificateCityName,
       "hpSwitchServerCertificateStateName": hpSwitchServerCertificateStateName,
       "hpSwitchServerCertificateCountryCode": hpSwitchServerCertificateCountryCode,
       "hpSwitchServerCertificateFingerprintMD5": hpSwitchServerCertificateFingerprintMD5,
       "hpSwitchServerCertificateFingerprintSHA1": hpSwitchServerCertificateFingerprintSHA1,
       "hpSwitchKmsChainConfigTable": hpSwitchKmsChainConfigTable,
       "hpSwitchKmsChainConfigEntry": hpSwitchKmsChainConfigEntry,
       "hpSwitchKmsChainId": hpSwitchKmsChainId,
       "hpSwitchKmsChainName": hpSwitchKmsChainName,
       "hpSwitchKmsChainKeys": hpSwitchKmsChainKeys,
       "hpSwitchKmsChainActiveKeys": hpSwitchKmsChainActiveKeys,
       "hpSwitchKmsChainExpKeys": hpSwitchKmsChainExpKeys,
       "hpSwitchKmsChainStatus": hpSwitchKmsChainStatus,
       "hpSwitchKmsKeyConfigTable": hpSwitchKmsKeyConfigTable,
       "hpSwitchKmsKeyConfigEntry": hpSwitchKmsKeyConfigEntry,
       "hpSwitchKmsKeyChainId": hpSwitchKmsKeyChainId,
       "hpSwitchKmsKeyId": hpSwitchKmsKeyId,
       "hpSwitchKmsKeyStr": hpSwitchKmsKeyStr,
       "hpSwitchKmsKeyStartTime": hpSwitchKmsKeyStartTime,
       "hpSwitchKmsKeyStopTime": hpSwitchKmsKeyStopTime,
       "hpSwitchKmsKeyTxStartTime": hpSwitchKmsKeyTxStartTime,
       "hpSwitchKmsKeyTxStopTime": hpSwitchKmsKeyTxStopTime,
       "hpSwitchKmsKeyStatus": hpSwitchKmsKeyStatus,
       "hpSwitchKmsKeyEncrypted": hpSwitchKmsKeyEncrypted,
       "hpSwitchOspfIfAuthTable": hpSwitchOspfIfAuthTable,
       "hpSwitchOspfIfAuthEntry": hpSwitchOspfIfAuthEntry,
       "hpSwitchOspfIfAuthChain": hpSwitchOspfIfAuthChain,
       "hpSwitchOspfIfAuthKeyEncrypted": hpSwitchOspfIfAuthKeyEncrypted,
       "hpSwitchOspfVirtIfAuthTable": hpSwitchOspfVirtIfAuthTable,
       "hpSwitchOspfVirtIfAuthEntry": hpSwitchOspfVirtIfAuthEntry,
       "hpSwitchOspfVirtIfAuthChain": hpSwitchOspfVirtIfAuthChain,
       "hpSwitchOspfVirtIfAuthKeyEncrypted": hpSwitchOspfVirtIfAuthKeyEncrypted,
       "hpicfSwitchUserConfigTable": hpicfSwitchUserConfigTable,
       "hpicfSwitchUserConfigEntry": hpicfSwitchUserConfigEntry,
       "hpicfSwitchUserConfigIndex": hpicfSwitchUserConfigIndex,
       "hpicfSwitchUserName": hpicfSwitchUserName,
       "hpicfSwitchOperatorName": hpicfSwitchOperatorName,
       "hpicfSwitchUserPassword": hpicfSwitchUserPassword,
       "hpicfSwitchOperatorPassword": hpicfSwitchOperatorPassword,
       "hpicfSwitchUserConfigStatus": hpicfSwitchUserConfigStatus,
       "hpicfSwitchPortAccessName": hpicfSwitchPortAccessName,
       "hpicfSwitchPortAccessPassword": hpicfSwitchPortAccessPassword,
       "hpicfSwitchUserPasswordHashType": hpicfSwitchUserPasswordHashType,
       "hpicfSwitchOperatorPasswordHashType": hpicfSwitchOperatorPasswordHashType,
       "hpicfSwitchPortAccessPasswordHashType": hpicfSwitchPortAccessPasswordHashType,
       "hpicfSwitchUserPasswordEncrypted": hpicfSwitchUserPasswordEncrypted,
       "hpicfSwitchOperatorPasswordEncrypted": hpicfSwitchOperatorPasswordEncrypted,
       "hpicfSwitchPortAccessPasswordEncrypted": hpicfSwitchPortAccessPasswordEncrypted,
       "hpicfSwitchBypassUsername": hpicfSwitchBypassUsername,
       "hpicfSwitchUserPwdAgingInterval": hpicfSwitchUserPwdAgingInterval,
       "hpicfSwitchOperatorPwdAgingInterval": hpicfSwitchOperatorPwdAgingInterval,
       "hpicfSwitchUserPwdLengthValue": hpicfSwitchUserPwdLengthValue,
       "hpicfSwitchOperatorPwdLengthValue": hpicfSwitchOperatorPwdLengthValue,
       "hpicfSwitchNonPlaintextSha256": hpicfSwitchNonPlaintextSha256,
       "hpicfSwitchUserPasswordHashSha256": hpicfSwitchUserPasswordHashSha256,
       "hpicfSwitchOperatorPasswordHashSha256": hpicfSwitchOperatorPasswordHashSha256,
       "hpSwitchAAAServerGroupTable": hpSwitchAAAServerGroupTable,
       "hpSwitchAAAServerGroupEntry": hpSwitchAAAServerGroupEntry,
       "hpSwitchAAAServerGroupProtocolType": hpSwitchAAAServerGroupProtocolType,
       "hpSwitchAAAServerGroupIndex": hpSwitchAAAServerGroupIndex,
       "hpSwitchAAAServerGroupServerIndex": hpSwitchAAAServerGroupServerIndex,
       "hpSwitchAAAServerGroupName": hpSwitchAAAServerGroupName,
       "hpSwitchAAAServerGroupServerInetType": hpSwitchAAAServerGroupServerInetType,
       "hpSwitchAAAServerGroupServerInetAddr": hpSwitchAAAServerGroupServerInetAddr,
       "hpSwitchAAAServerGroupStatus": hpSwitchAAAServerGroupStatus,
       "hpSwitchAAAServerGroupServerFqdn": hpSwitchAAAServerGroupServerFqdn,
       "hpSwitchAAAServerGroupTLSEnable": hpSwitchAAAServerGroupTLSEnable,
       "hpSwitchLocalMgmtPrivUsernamesTable": hpSwitchLocalMgmtPrivUsernamesTable,
       "hpSwitchLocalMgmtPrivUsernamesEntry": hpSwitchLocalMgmtPrivUsernamesEntry,
       "hpSwitchLocalMgmtPrivUsernameIndex": hpSwitchLocalMgmtPrivUsernameIndex,
       "hpSwitchLocalMgmtPrivUsernameStr": hpSwitchLocalMgmtPrivUsernameStr,
       "hpSwitchLocalMgmtPrivUsernamePasswdType": hpSwitchLocalMgmtPrivUsernamePasswdType,
       "hpSwitchLocalMgmtPrivUsernamePasswd": hpSwitchLocalMgmtPrivUsernamePasswd,
       "hpSwitchLocalMgmtPrivUsernameGrpIndex": hpSwitchLocalMgmtPrivUsernameGrpIndex,
       "hpSwitchLocalMgmtPrivUsernameStatus": hpSwitchLocalMgmtPrivUsernameStatus,
       "hpSwitchLocalMgmtPwdUserAgingInterval": hpSwitchLocalMgmtPwdUserAgingInterval,
       "hpSwitchLocalMgmtPwdUserPasswdLengthValue": hpSwitchLocalMgmtPwdUserPasswdLengthValue,
       "hpSwitchLocalMgmtPrivUsernamePasswdSha256": hpSwitchLocalMgmtPrivUsernamePasswdSha256,
       "hpSwitchRipIfAuthTable": hpSwitchRipIfAuthTable,
       "hpSwitchRipIfAuthEntry": hpSwitchRipIfAuthEntry,
       "hpSwitchRipIfAuthChain": hpSwitchRipIfAuthChain,
       "hpSwitchRip2IfConfAuthKeyEncrypted": hpSwitchRip2IfConfAuthKeyEncrypted,
       "hpSwitchAuthenPwdCompositionTable": hpSwitchAuthenPwdCompositionTable,
       "hpSwitchAuthenPwdCompositionEntry": hpSwitchAuthenPwdCompositionEntry,
       "hpSwitchAuthenCompositionIndex": hpSwitchAuthenCompositionIndex,
       "hpSwitchAuthenCompositionValue": hpSwitchAuthenCompositionValue,
       "hpSwitchAuthenticationPasswordConfig": hpSwitchAuthenticationPasswordConfig,
       "hpSwitchAuthPwdControlCheck": hpSwitchAuthPwdControlCheck,
       "hpSwitchAuthPwdUserNameCheck": hpSwitchAuthPwdUserNameCheck,
       "hpSwitchAuthPwdRepeatCharactersCheck": hpSwitchAuthPwdRepeatCharactersCheck,
       "hpSwitchAuthPwdRepeatPasswordCheck": hpSwitchAuthPwdRepeatPasswordCheck,
       "hpSwitchAuthPwdAgingCheck": hpSwitchAuthPwdAgingCheck,
       "hpSwitchAuthPwdLogonDetailsCheck": hpSwitchAuthPwdLogonDetailsCheck,
       "hpSwitchAuthPwdAgingValue": hpSwitchAuthPwdAgingValue,
       "hpSwitchAuthPwdHistoryCheck": hpSwitchAuthPwdHistoryCheck,
       "hpSwitchAuthPwdHistoryRecordsRange": hpSwitchAuthPwdHistoryRecordsRange,
       "hpSwitchAuthPwdAlertBeforeExpiry": hpSwitchAuthPwdAlertBeforeExpiry,
       "hpSwitchAuthPwdExpiredUserLoginDays": hpSwitchAuthPwdExpiredUserLoginDays,
       "hpSwitchAuthPwdExpiredUserLoginAttempts": hpSwitchAuthPwdExpiredUserLoginAttempts,
       "hpSwitchAuthPwdUpdateInterval": hpSwitchAuthPwdUpdateInterval,
       "hpSwitchAuthPwdCharPositionCheckValue": hpSwitchAuthPwdCharPositionCheckValue,
       "hpSwitchFrontPanelSecurity": hpSwitchFrontPanelSecurity,
       "hpSwitchFpsPasswordClear": hpSwitchFpsPasswordClear,
       "hpSwitchFpsFactoryReset": hpSwitchFpsFactoryReset,
       "hpSwitchFpsPasswordRecovery": hpSwitchFpsPasswordRecovery,
       "hpSwitchFpsDiagnosticResetClearButton": hpSwitchFpsDiagnosticResetClearButton,
       "hpSwitchFpsDiagnosticResetSerialConsole": hpSwitchFpsDiagnosticResetSerialConsole,
       "hpSwitchFpsDisplayInConfig": hpSwitchFpsDisplayInConfig,
       "hpSwitchAAAServerGroupNasTable": hpSwitchAAAServerGroupNasTable,
       "hpSwitchAAAServerGroupNasEntry": hpSwitchAAAServerGroupNasEntry,
       "hpSwitchAAAServerGroupNasProtocolType": hpSwitchAAAServerGroupNasProtocolType,
       "hpSwitchAAAServerGroupNasIndex": hpSwitchAAAServerGroupNasIndex,
       "hpSwitchAAAServerGroupNasName": hpSwitchAAAServerGroupNasName,
       "hpSwitchAAAServerGroupNasId": hpSwitchAAAServerGroupNasId,
       "hpSwitchAAAServerGroupNasStatus": hpSwitchAAAServerGroupNasStatus}
)
