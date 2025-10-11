# SNMP MIB module (G6-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-ACCESS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:05 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Access_ObjectIdentity = ObjectIdentity
access = _Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76)
)


class _AccessAuthenticationMode_Type(Integer32):
    """Custom type accessAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("localThenRadius", 1),
          ("radius", 2),
          ("localThenTacacs", 3),
          ("tacacs", 4),
          ("radiusThenLocal", 5),
          ("tacacsThenLocal", 6))
    )


_AccessAuthenticationMode_Type.__name__ = "Integer32"
_AccessAuthenticationMode_Object = MibScalar
accessAuthenticationMode = _AccessAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 1),
    _AccessAuthenticationMode_Type()
)
accessAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessAuthenticationMode.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1)
)
userEntry.setIndexNames(
    (0, "G6-ACCESS-MIB", "userIndex"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")


class _UserIndex_Type(Integer32):
    """Custom type userIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_UserIndex_Type.__name__ = "Integer32"
_UserIndex_Object = MibTableColumn
userIndex = _UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 1),
    _UserIndex_Type()
)
userIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userIndex.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserAssociatedGroups_Type = DisplayString
_UserAssociatedGroups_Object = MibTableColumn
userAssociatedGroups = _UserAssociatedGroups_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 3),
    _UserAssociatedGroups_Type()
)
userAssociatedGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAssociatedGroups.setStatus("current")


class _UserGeneralAccessRights_Type(Integer32):
    """Custom type userGeneralAccessRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 0),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_UserGeneralAccessRights_Type.__name__ = "Integer32"
_UserGeneralAccessRights_Object = MibTableColumn
userGeneralAccessRights = _UserGeneralAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 4),
    _UserGeneralAccessRights_Type()
)
userGeneralAccessRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGeneralAccessRights.setStatus("current")


class _UserEnableTelnetAccess_Type(Integer32):
    """Custom type userEnableTelnetAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UserEnableTelnetAccess_Type.__name__ = "Integer32"
_UserEnableTelnetAccess_Object = MibTableColumn
userEnableTelnetAccess = _UserEnableTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 5),
    _UserEnableTelnetAccess_Type()
)
userEnableTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEnableTelnetAccess.setStatus("current")


class _UserEnableSshAccess_Type(Integer32):
    """Custom type userEnableSshAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UserEnableSshAccess_Type.__name__ = "Integer32"
_UserEnableSshAccess_Object = MibTableColumn
userEnableSshAccess = _UserEnableSshAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 6),
    _UserEnableSshAccess_Type()
)
userEnableSshAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEnableSshAccess.setStatus("current")


class _UserEnableWebAccess_Type(Integer32):
    """Custom type userEnableWebAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UserEnableWebAccess_Type.__name__ = "Integer32"
_UserEnableWebAccess_Object = MibTableColumn
userEnableWebAccess = _UserEnableWebAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 7),
    _UserEnableWebAccess_Type()
)
userEnableWebAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEnableWebAccess.setStatus("current")


class _UserEnableSnmpAccess_Type(Integer32):
    """Custom type userEnableSnmpAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UserEnableSnmpAccess_Type.__name__ = "Integer32"
_UserEnableSnmpAccess_Object = MibTableColumn
userEnableSnmpAccess = _UserEnableSnmpAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 8),
    _UserEnableSnmpAccess_Type()
)
userEnableSnmpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEnableSnmpAccess.setStatus("current")


class _UserEnableNmpAccess_Type(Integer32):
    """Custom type userEnableNmpAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UserEnableNmpAccess_Type.__name__ = "Integer32"
_UserEnableNmpAccess_Object = MibTableColumn
userEnableNmpAccess = _UserEnableNmpAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 9),
    _UserEnableNmpAccess_Type()
)
userEnableNmpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEnableNmpAccess.setStatus("current")


class _UserEnableFtpAccess_Type(Integer32):
    """Custom type userEnableFtpAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UserEnableFtpAccess_Type.__name__ = "Integer32"
_UserEnableFtpAccess_Object = MibTableColumn
userEnableFtpAccess = _UserEnableFtpAccess_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 10),
    _UserEnableFtpAccess_Type()
)
userEnableFtpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEnableFtpAccess.setStatus("current")
_UserEnterPassword_Type = DisplayString
_UserEnterPassword_Object = MibTableColumn
userEnterPassword = _UserEnterPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 11),
    _UserEnterPassword_Type()
)
userEnterPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEnterPassword.setStatus("current")
_UserEncryptedAuthPassword_Type = DisplayString
_UserEncryptedAuthPassword_Object = MibTableColumn
userEncryptedAuthPassword = _UserEncryptedAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 12),
    _UserEncryptedAuthPassword_Type()
)
userEncryptedAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEncryptedAuthPassword.setStatus("current")


class _UserSnmpV3SecurityLevel_Type(Integer32):
    """Custom type userSnmpV3SecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 0),
          ("authNoPriv", 1),
          ("authPriv", 2))
    )


_UserSnmpV3SecurityLevel_Type.__name__ = "Integer32"
_UserSnmpV3SecurityLevel_Object = MibTableColumn
userSnmpV3SecurityLevel = _UserSnmpV3SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 13),
    _UserSnmpV3SecurityLevel_Type()
)
userSnmpV3SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSnmpV3SecurityLevel.setStatus("current")


class _UserSnmpV3AuthAlgorithm_Type(Integer32):
    """Custom type userSnmpV3AuthAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuthentication", 0),
          ("md5", 1),
          ("sha", 2))
    )


_UserSnmpV3AuthAlgorithm_Type.__name__ = "Integer32"
_UserSnmpV3AuthAlgorithm_Object = MibTableColumn
userSnmpV3AuthAlgorithm = _UserSnmpV3AuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 14),
    _UserSnmpV3AuthAlgorithm_Type()
)
userSnmpV3AuthAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSnmpV3AuthAlgorithm.setStatus("current")


class _UserSnmpV3PrivacyAlgorithm_Type(Integer32):
    """Custom type userSnmpV3PrivacyAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPrivacy", 0),
          ("des", 1),
          ("aes", 2))
    )


_UserSnmpV3PrivacyAlgorithm_Type.__name__ = "Integer32"
_UserSnmpV3PrivacyAlgorithm_Object = MibTableColumn
userSnmpV3PrivacyAlgorithm = _UserSnmpV3PrivacyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 15),
    _UserSnmpV3PrivacyAlgorithm_Type()
)
userSnmpV3PrivacyAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSnmpV3PrivacyAlgorithm.setStatus("current")
_UserEnterSnmpV3AuthPassword_Type = DisplayString
_UserEnterSnmpV3AuthPassword_Object = MibTableColumn
userEnterSnmpV3AuthPassword = _UserEnterSnmpV3AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 16),
    _UserEnterSnmpV3AuthPassword_Type()
)
userEnterSnmpV3AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEnterSnmpV3AuthPassword.setStatus("current")
_UserEncryptedSnmpAuthPassword_Type = DisplayString
_UserEncryptedSnmpAuthPassword_Object = MibTableColumn
userEncryptedSnmpAuthPassword = _UserEncryptedSnmpAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 17),
    _UserEncryptedSnmpAuthPassword_Type()
)
userEncryptedSnmpAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEncryptedSnmpAuthPassword.setStatus("current")
_UserEnterSnmpV3PrivacyPassword_Type = DisplayString
_UserEnterSnmpV3PrivacyPassword_Object = MibTableColumn
userEnterSnmpV3PrivacyPassword = _UserEnterSnmpV3PrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 18),
    _UserEnterSnmpV3PrivacyPassword_Type()
)
userEnterSnmpV3PrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEnterSnmpV3PrivacyPassword.setStatus("current")
_UserEncryptedSnmpPrivacyPassword_Type = DisplayString
_UserEncryptedSnmpPrivacyPassword_Object = MibTableColumn
userEncryptedSnmpPrivacyPassword = _UserEncryptedSnmpPrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 2, 1, 19),
    _UserEncryptedSnmpPrivacyPassword_Type()
)
userEncryptedSnmpPrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userEncryptedSnmpPrivacyPassword.setStatus("current")
_GroupTable_Object = MibTable
groupTable = _GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 3)
)
if mibBuilder.loadTexts:
    groupTable.setStatus("current")
_GroupEntry_Object = MibTableRow
groupEntry = _GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 3, 1)
)
groupEntry.setIndexNames(
    (0, "G6-ACCESS-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupEntry.setStatus("current")


class _GroupIndex_Type(Integer32):
    """Custom type groupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GroupIndex_Type.__name__ = "Integer32"
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 3, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupIndex.setStatus("current")
_GroupName_Type = DisplayString
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 3, 1, 2),
    _GroupName_Type()
)
groupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupName.setStatus("current")
_GroupAssociatedViews_Type = DisplayString
_GroupAssociatedViews_Object = MibTableColumn
groupAssociatedViews = _GroupAssociatedViews_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 3, 1, 3),
    _GroupAssociatedViews_Type()
)
groupAssociatedViews.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupAssociatedViews.setStatus("current")
_ViewTable_Object = MibTable
viewTable = _ViewTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 4)
)
if mibBuilder.loadTexts:
    viewTable.setStatus("current")
_ViewEntry_Object = MibTableRow
viewEntry = _ViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 4, 1)
)
viewEntry.setIndexNames(
    (0, "G6-ACCESS-MIB", "viewIndex"),
)
if mibBuilder.loadTexts:
    viewEntry.setStatus("current")


class _ViewIndex_Type(Integer32):
    """Custom type viewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ViewIndex_Type.__name__ = "Integer32"
_ViewIndex_Object = MibTableColumn
viewIndex = _ViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 4, 1, 1),
    _ViewIndex_Type()
)
viewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    viewIndex.setStatus("current")
_ViewName_Type = DisplayString
_ViewName_Object = MibTableColumn
viewName = _ViewName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 4, 1, 2),
    _ViewName_Type()
)
viewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    viewName.setStatus("current")
_ViewAssociatedPattern_Type = DisplayString
_ViewAssociatedPattern_Object = MibTableColumn
viewAssociatedPattern = _ViewAssociatedPattern_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 4, 1, 3),
    _ViewAssociatedPattern_Type()
)
viewAssociatedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    viewAssociatedPattern.setStatus("current")
_PatternTable_Object = MibTable
patternTable = _PatternTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 5)
)
if mibBuilder.loadTexts:
    patternTable.setStatus("current")
_PatternEntry_Object = MibTableRow
patternEntry = _PatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 5, 1)
)
patternEntry.setIndexNames(
    (0, "G6-ACCESS-MIB", "patternIndex"),
)
if mibBuilder.loadTexts:
    patternEntry.setStatus("current")


class _PatternIndex_Type(Integer32):
    """Custom type patternIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PatternIndex_Type.__name__ = "Integer32"
_PatternIndex_Object = MibTableColumn
patternIndex = _PatternIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 5, 1, 1),
    _PatternIndex_Type()
)
patternIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    patternIndex.setStatus("current")
_PatternName_Type = DisplayString
_PatternName_Object = MibTableColumn
patternName = _PatternName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 5, 1, 2),
    _PatternName_Type()
)
patternName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patternName.setStatus("current")
_PatternDotstring_Type = DisplayString
_PatternDotstring_Object = MibTableColumn
patternDotstring = _PatternDotstring_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 5, 1, 3),
    _PatternDotstring_Type()
)
patternDotstring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patternDotstring.setStatus("current")


class _PatternAccessRights_Type(Integer32):
    """Custom type patternAccessRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 0),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_PatternAccessRights_Type.__name__ = "Integer32"
_PatternAccessRights_Object = MibTableColumn
patternAccessRights = _PatternAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 5, 1, 4),
    _PatternAccessRights_Type()
)
patternAccessRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patternAccessRights.setStatus("current")
_RadiusTable_Object = MibTable
radiusTable = _RadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 6)
)
if mibBuilder.loadTexts:
    radiusTable.setStatus("current")
_RadiusEntry_Object = MibTableRow
radiusEntry = _RadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 6, 1)
)
radiusEntry.setIndexNames(
    (0, "G6-ACCESS-MIB", "radiusIndex"),
)
if mibBuilder.loadTexts:
    radiusEntry.setStatus("current")


class _RadiusIndex_Type(Integer32):
    """Custom type radiusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_RadiusIndex_Type.__name__ = "Integer32"
_RadiusIndex_Object = MibTableColumn
radiusIndex = _RadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 6, 1, 1),
    _RadiusIndex_Type()
)
radiusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusIndex.setStatus("current")
_RadiusPrimaryAuthServerName_Type = DisplayString
_RadiusPrimaryAuthServerName_Object = MibTableColumn
radiusPrimaryAuthServerName = _RadiusPrimaryAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 6, 1, 2),
    _RadiusPrimaryAuthServerName_Type()
)
radiusPrimaryAuthServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPrimaryAuthServerName.setStatus("current")
_RadiusFallbackAuthServerName_Type = DisplayString
_RadiusFallbackAuthServerName_Object = MibTableColumn
radiusFallbackAuthServerName = _RadiusFallbackAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 6, 1, 3),
    _RadiusFallbackAuthServerName_Type()
)
radiusFallbackAuthServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusFallbackAuthServerName.setStatus("current")
_TacacsTable_Object = MibTable
tacacsTable = _TacacsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 7)
)
if mibBuilder.loadTexts:
    tacacsTable.setStatus("current")
_TacacsEntry_Object = MibTableRow
tacacsEntry = _TacacsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 7, 1)
)
tacacsEntry.setIndexNames(
    (0, "G6-ACCESS-MIB", "tacacsIndex"),
)
if mibBuilder.loadTexts:
    tacacsEntry.setStatus("current")


class _TacacsIndex_Type(Integer32):
    """Custom type tacacsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_TacacsIndex_Type.__name__ = "Integer32"
_TacacsIndex_Object = MibTableColumn
tacacsIndex = _TacacsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 7, 1, 1),
    _TacacsIndex_Type()
)
tacacsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsIndex.setStatus("current")
_TacacsPrimaryAuthServerName_Type = DisplayString
_TacacsPrimaryAuthServerName_Object = MibTableColumn
tacacsPrimaryAuthServerName = _TacacsPrimaryAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 7, 1, 2),
    _TacacsPrimaryAuthServerName_Type()
)
tacacsPrimaryAuthServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPrimaryAuthServerName.setStatus("current")
_TacacsFallbackAuthServerName_Type = DisplayString
_TacacsFallbackAuthServerName_Object = MibTableColumn
tacacsFallbackAuthServerName = _TacacsFallbackAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 7, 1, 3),
    _TacacsFallbackAuthServerName_Type()
)
tacacsFallbackAuthServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsFallbackAuthServerName.setStatus("current")
_TacacsPrivilegeLevel0User_Type = DisplayString
_TacacsPrivilegeLevel0User_Object = MibTableColumn
tacacsPrivilegeLevel0User = _TacacsPrivilegeLevel0User_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 7, 1, 4),
    _TacacsPrivilegeLevel0User_Type()
)
tacacsPrivilegeLevel0User.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPrivilegeLevel0User.setStatus("current")
_TacacsPrivilegeLevel1User_Type = DisplayString
_TacacsPrivilegeLevel1User_Object = MibTableColumn
tacacsPrivilegeLevel1User = _TacacsPrivilegeLevel1User_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 7, 1, 5),
    _TacacsPrivilegeLevel1User_Type()
)
tacacsPrivilegeLevel1User.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPrivilegeLevel1User.setStatus("current")
_TacacsPrivilegeLevel15User_Type = DisplayString
_TacacsPrivilegeLevel15User_Object = MibTableColumn
tacacsPrivilegeLevel15User = _TacacsPrivilegeLevel15User_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 7, 1, 6),
    _TacacsPrivilegeLevel15User_Type()
)
tacacsPrivilegeLevel15User.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPrivilegeLevel15User.setStatus("current")
_RestrictionsTable_Object = MibTable
restrictionsTable = _RestrictionsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 8)
)
if mibBuilder.loadTexts:
    restrictionsTable.setStatus("current")
_RestrictionsEntry_Object = MibTableRow
restrictionsEntry = _RestrictionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 8, 1)
)
restrictionsEntry.setIndexNames(
    (0, "G6-ACCESS-MIB", "restrictionsIndex"),
)
if mibBuilder.loadTexts:
    restrictionsEntry.setStatus("current")


class _RestrictionsIndex_Type(Integer32):
    """Custom type restrictionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RestrictionsIndex_Type.__name__ = "Integer32"
_RestrictionsIndex_Object = MibTableColumn
restrictionsIndex = _RestrictionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 8, 1, 1),
    _RestrictionsIndex_Type()
)
restrictionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    restrictionsIndex.setStatus("current")
_RestrictionsName_Type = DisplayString
_RestrictionsName_Object = MibTableColumn
restrictionsName = _RestrictionsName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 8, 1, 2),
    _RestrictionsName_Type()
)
restrictionsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restrictionsName.setStatus("current")


class _RestrictionsMode_Type(Integer32):
    """Custom type restrictionsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("permit", 1),
          ("deny", 2))
    )


_RestrictionsMode_Type.__name__ = "Integer32"
_RestrictionsMode_Object = MibTableColumn
restrictionsMode = _RestrictionsMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 8, 1, 3),
    _RestrictionsMode_Type()
)
restrictionsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restrictionsMode.setStatus("current")
_RestrictionsIpAddress_Type = DisplayString
_RestrictionsIpAddress_Object = MibTableColumn
restrictionsIpAddress = _RestrictionsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 8, 1, 4),
    _RestrictionsIpAddress_Type()
)
restrictionsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restrictionsIpAddress.setStatus("current")
_AccessNumberOfLogins_Type = Unsigned32
_AccessNumberOfLogins_Object = MibScalar
accessNumberOfLogins = _AccessNumberOfLogins_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 100),
    _AccessNumberOfLogins_Type()
)
accessNumberOfLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessNumberOfLogins.setStatus("current")
_LoginStatusTable_Object = MibTable
loginStatusTable = _LoginStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101)
)
if mibBuilder.loadTexts:
    loginStatusTable.setStatus("current")
_LoginStatusEntry_Object = MibTableRow
loginStatusEntry = _LoginStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1)
)
loginStatusEntry.setIndexNames(
    (0, "G6-ACCESS-MIB", "loginStatusIndex"),
)
if mibBuilder.loadTexts:
    loginStatusEntry.setStatus("current")


class _LoginStatusIndex_Type(Integer32):
    """Custom type loginStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LoginStatusIndex_Type.__name__ = "Integer32"
_LoginStatusIndex_Object = MibTableColumn
loginStatusIndex = _LoginStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 1),
    _LoginStatusIndex_Type()
)
loginStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loginStatusIndex.setStatus("current")


class _LoginStatusState_Type(Integer32):
    """Custom type loginStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("loggedOff", 1),
          ("activeLogin", 2))
    )


_LoginStatusState_Type.__name__ = "Integer32"
_LoginStatusState_Object = MibTableColumn
loginStatusState = _LoginStatusState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 2),
    _LoginStatusState_Type()
)
loginStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatusState.setStatus("current")
_LoginStatusUserName_Type = DisplayString
_LoginStatusUserName_Object = MibTableColumn
loginStatusUserName = _LoginStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 3),
    _LoginStatusUserName_Type()
)
loginStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatusUserName.setStatus("current")
_LoginStatusAuthName_Type = DisplayString
_LoginStatusAuthName_Object = MibTableColumn
loginStatusAuthName = _LoginStatusAuthName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 4),
    _LoginStatusAuthName_Type()
)
loginStatusAuthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatusAuthName.setStatus("current")
_LoginStatusLoginId_Type = Unsigned32
_LoginStatusLoginId_Object = MibTableColumn
loginStatusLoginId = _LoginStatusLoginId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 5),
    _LoginStatusLoginId_Type()
)
loginStatusLoginId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatusLoginId.setStatus("current")
_LoginStatusLoginTimeStamp_Type = DisplayString
_LoginStatusLoginTimeStamp_Object = MibTableColumn
loginStatusLoginTimeStamp = _LoginStatusLoginTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 6),
    _LoginStatusLoginTimeStamp_Type()
)
loginStatusLoginTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatusLoginTimeStamp.setStatus("current")
_LoginStatusLoginEpoch_Type = Unsigned32
_LoginStatusLoginEpoch_Object = MibTableColumn
loginStatusLoginEpoch = _LoginStatusLoginEpoch_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 7),
    _LoginStatusLoginEpoch_Type()
)
loginStatusLoginEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatusLoginEpoch.setStatus("current")
_LoginStatusConnectTime_Type = Counter32
_LoginStatusConnectTime_Object = MibTableColumn
loginStatusConnectTime = _LoginStatusConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 8),
    _LoginStatusConnectTime_Type()
)
loginStatusConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatusConnectTime.setStatus("current")
_LoginStatusService_Type = DisplayString
_LoginStatusService_Object = MibTableColumn
loginStatusService = _LoginStatusService_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 9),
    _LoginStatusService_Type()
)
loginStatusService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatusService.setStatus("current")
_LoginStatusRemoteHost_Type = DisplayString
_LoginStatusRemoteHost_Object = MibTableColumn
loginStatusRemoteHost = _LoginStatusRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 76, 101, 1, 10),
    _LoginStatusRemoteHost_Type()
)
loginStatusRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatusRemoteHost.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-ACCESS-MIB",
    **{"management": management,
       "access": access,
       "accessAuthenticationMode": accessAuthenticationMode,
       "userTable": userTable,
       "userEntry": userEntry,
       "userIndex": userIndex,
       "userName": userName,
       "userAssociatedGroups": userAssociatedGroups,
       "userGeneralAccessRights": userGeneralAccessRights,
       "userEnableTelnetAccess": userEnableTelnetAccess,
       "userEnableSshAccess": userEnableSshAccess,
       "userEnableWebAccess": userEnableWebAccess,
       "userEnableSnmpAccess": userEnableSnmpAccess,
       "userEnableNmpAccess": userEnableNmpAccess,
       "userEnableFtpAccess": userEnableFtpAccess,
       "userEnterPassword": userEnterPassword,
       "userEncryptedAuthPassword": userEncryptedAuthPassword,
       "userSnmpV3SecurityLevel": userSnmpV3SecurityLevel,
       "userSnmpV3AuthAlgorithm": userSnmpV3AuthAlgorithm,
       "userSnmpV3PrivacyAlgorithm": userSnmpV3PrivacyAlgorithm,
       "userEnterSnmpV3AuthPassword": userEnterSnmpV3AuthPassword,
       "userEncryptedSnmpAuthPassword": userEncryptedSnmpAuthPassword,
       "userEnterSnmpV3PrivacyPassword": userEnterSnmpV3PrivacyPassword,
       "userEncryptedSnmpPrivacyPassword": userEncryptedSnmpPrivacyPassword,
       "groupTable": groupTable,
       "groupEntry": groupEntry,
       "groupIndex": groupIndex,
       "groupName": groupName,
       "groupAssociatedViews": groupAssociatedViews,
       "viewTable": viewTable,
       "viewEntry": viewEntry,
       "viewIndex": viewIndex,
       "viewName": viewName,
       "viewAssociatedPattern": viewAssociatedPattern,
       "patternTable": patternTable,
       "patternEntry": patternEntry,
       "patternIndex": patternIndex,
       "patternName": patternName,
       "patternDotstring": patternDotstring,
       "patternAccessRights": patternAccessRights,
       "radiusTable": radiusTable,
       "radiusEntry": radiusEntry,
       "radiusIndex": radiusIndex,
       "radiusPrimaryAuthServerName": radiusPrimaryAuthServerName,
       "radiusFallbackAuthServerName": radiusFallbackAuthServerName,
       "tacacsTable": tacacsTable,
       "tacacsEntry": tacacsEntry,
       "tacacsIndex": tacacsIndex,
       "tacacsPrimaryAuthServerName": tacacsPrimaryAuthServerName,
       "tacacsFallbackAuthServerName": tacacsFallbackAuthServerName,
       "tacacsPrivilegeLevel0User": tacacsPrivilegeLevel0User,
       "tacacsPrivilegeLevel1User": tacacsPrivilegeLevel1User,
       "tacacsPrivilegeLevel15User": tacacsPrivilegeLevel15User,
       "restrictionsTable": restrictionsTable,
       "restrictionsEntry": restrictionsEntry,
       "restrictionsIndex": restrictionsIndex,
       "restrictionsName": restrictionsName,
       "restrictionsMode": restrictionsMode,
       "restrictionsIpAddress": restrictionsIpAddress,
       "accessNumberOfLogins": accessNumberOfLogins,
       "loginStatusTable": loginStatusTable,
       "loginStatusEntry": loginStatusEntry,
       "loginStatusIndex": loginStatusIndex,
       "loginStatusState": loginStatusState,
       "loginStatusUserName": loginStatusUserName,
       "loginStatusAuthName": loginStatusAuthName,
       "loginStatusLoginId": loginStatusLoginId,
       "loginStatusLoginTimeStamp": loginStatusLoginTimeStamp,
       "loginStatusLoginEpoch": loginStatusLoginEpoch,
       "loginStatusConnectTime": loginStatusConnectTime,
       "loginStatusService": loginStatusService,
       "loginStatusRemoteHost": loginStatusRemoteHost}
)
