# SNMP MIB module (ELTEX-MES-ISS-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-AAA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:19 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(mcTrapDescr,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "mcTrapDescr")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssAaaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7)
)
if mibBuilder.loadTexts:
    eltMesIssAaaMIB.setRevisions(
        ("2022-08-03 00:00",
         "2022-02-15 00:00",
         "2021-07-02 00:00",
         "2020-10-29 00:00",
         "2020-06-05 00:00",
         "2019-01-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssAaaAuthenticationMethod(TextualConvention, Integer32):
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
        *(("local", 1),
          ("remoteRadius", 2),
          ("remoteTacacs", 3),
          ("none", 4))
    )



class EltMesIssAaaAuthenticationModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chain", 1),
          ("break", 2))
    )



class EltMesIssAaaLineType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("telnet", 2),
          ("ssh", 3))
    )



class EltMesIssAaaTacacsAuthenticationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("pap", 2))
    )



class EltMesIssAaaAuthorizationMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remoteTacacs", 2),
          ("tacacsFallbackToLocal", 3),
          ("global", 255))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssAaaObjects_ObjectIdentity = ObjectIdentity
eltMesIssAaaObjects = _EltMesIssAaaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1)
)
_EltMesIssAaaGlobalConfig_ObjectIdentity = ObjectIdentity
eltMesIssAaaGlobalConfig = _EltMesIssAaaGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1)
)


class _EltMesIssAaaEnableAuthentication_Type(EltMesIssAaaAuthenticationMethod):
    """Custom type eltMesIssAaaEnableAuthentication based on EltMesIssAaaAuthenticationMethod"""
    defaultValue = 1


_EltMesIssAaaEnableAuthentication_Type.__name__ = "EltMesIssAaaAuthenticationMethod"
_EltMesIssAaaEnableAuthentication_Object = MibScalar
eltMesIssAaaEnableAuthentication = _EltMesIssAaaEnableAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 1),
    _EltMesIssAaaEnableAuthentication_Type()
)
eltMesIssAaaEnableAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaEnableAuthentication.setStatus("deprecated")
_EltMesIssAaaTacacsGlobalConfig_ObjectIdentity = ObjectIdentity
eltMesIssAaaTacacsGlobalConfig = _EltMesIssAaaTacacsGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 2)
)


class _EltMesIssAaaTacacsAuthenticationType_Type(EltMesIssAaaTacacsAuthenticationType):
    """Custom type eltMesIssAaaTacacsAuthenticationType based on EltMesIssAaaTacacsAuthenticationType"""
    defaultValue = 2


_EltMesIssAaaTacacsAuthenticationType_Type.__name__ = "EltMesIssAaaTacacsAuthenticationType"
_EltMesIssAaaTacacsAuthenticationType_Object = MibScalar
eltMesIssAaaTacacsAuthenticationType = _EltMesIssAaaTacacsAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 2, 1),
    _EltMesIssAaaTacacsAuthenticationType_Type()
)
eltMesIssAaaTacacsAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaTacacsAuthenticationType.setStatus("current")
_EltMesIssAaaTacacsAttrConfig_ObjectIdentity = ObjectIdentity
eltMesIssAaaTacacsAttrConfig = _EltMesIssAaaTacacsAttrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 2, 2)
)
_EltMesIssAaaTacacsAttrPortConfigTable_Object = MibTable
eltMesIssAaaTacacsAttrPortConfigTable = _EltMesIssAaaTacacsAttrPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssAaaTacacsAttrPortConfigTable.setStatus("current")
_EltMesIssAaaTacacsAttrPortConfigEntry_Object = MibTableRow
eltMesIssAaaTacacsAttrPortConfigEntry = _EltMesIssAaaTacacsAttrPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 2, 2, 1, 1)
)
eltMesIssAaaTacacsAttrPortConfigEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-AAA-MIB", "eltMesIssAaaTacacsAttrPortLineType"),
)
if mibBuilder.loadTexts:
    eltMesIssAaaTacacsAttrPortConfigEntry.setStatus("current")
_EltMesIssAaaTacacsAttrPortLineType_Type = EltMesIssAaaLineType
_EltMesIssAaaTacacsAttrPortLineType_Object = MibTableColumn
eltMesIssAaaTacacsAttrPortLineType = _EltMesIssAaaTacacsAttrPortLineType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 2, 2, 1, 1, 1),
    _EltMesIssAaaTacacsAttrPortLineType_Type()
)
eltMesIssAaaTacacsAttrPortLineType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssAaaTacacsAttrPortLineType.setStatus("current")


class _EltMesIssAaaTacacsAttrPortFormat_Type(OctetString):
    """Custom type eltMesIssAaaTacacsAttrPortFormat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EltMesIssAaaTacacsAttrPortFormat_Type.__name__ = "OctetString"
_EltMesIssAaaTacacsAttrPortFormat_Object = MibTableColumn
eltMesIssAaaTacacsAttrPortFormat = _EltMesIssAaaTacacsAttrPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 2, 2, 1, 1, 2),
    _EltMesIssAaaTacacsAttrPortFormat_Type()
)
eltMesIssAaaTacacsAttrPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaTacacsAttrPortFormat.setStatus("current")
_EltMesIssAaaRadiusGlobalConfig_ObjectIdentity = ObjectIdentity
eltMesIssAaaRadiusGlobalConfig = _EltMesIssAaaRadiusGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 3)
)
_EltMesIssAaaCommandAuthorizationTable_Object = MibTable
eltMesIssAaaCommandAuthorizationTable = _EltMesIssAaaCommandAuthorizationTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    eltMesIssAaaCommandAuthorizationTable.setStatus("current")
_EltMesIssAaaCommandAuthorizationEntry_Object = MibTableRow
eltMesIssAaaCommandAuthorizationEntry = _EltMesIssAaaCommandAuthorizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 4, 1)
)
eltMesIssAaaCommandAuthorizationEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-AAA-MIB", "eltMesIssAaaCommandAuthorizationPrivilege"),
)
if mibBuilder.loadTexts:
    eltMesIssAaaCommandAuthorizationEntry.setStatus("current")


class _EltMesIssAaaCommandAuthorizationPrivilege_Type(Unsigned32):
    """Custom type eltMesIssAaaCommandAuthorizationPrivilege based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_EltMesIssAaaCommandAuthorizationPrivilege_Type.__name__ = "Unsigned32"
_EltMesIssAaaCommandAuthorizationPrivilege_Object = MibTableColumn
eltMesIssAaaCommandAuthorizationPrivilege = _EltMesIssAaaCommandAuthorizationPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 4, 1, 1),
    _EltMesIssAaaCommandAuthorizationPrivilege_Type()
)
eltMesIssAaaCommandAuthorizationPrivilege.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssAaaCommandAuthorizationPrivilege.setStatus("current")


class _EltMesIssAaaCommandAuthorizationMethod_Type(EltMesIssAaaAuthorizationMethod):
    """Custom type eltMesIssAaaCommandAuthorizationMethod based on EltMesIssAaaAuthorizationMethod"""
    defaultValue = 1


_EltMesIssAaaCommandAuthorizationMethod_Type.__name__ = "EltMesIssAaaAuthorizationMethod"
_EltMesIssAaaCommandAuthorizationMethod_Object = MibTableColumn
eltMesIssAaaCommandAuthorizationMethod = _EltMesIssAaaCommandAuthorizationMethod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 4, 1, 2),
    _EltMesIssAaaCommandAuthorizationMethod_Type()
)
eltMesIssAaaCommandAuthorizationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaCommandAuthorizationMethod.setStatus("current")


class _EltMesIssAaaAuthenticationMode_Type(EltMesIssAaaAuthenticationModeType):
    """Custom type eltMesIssAaaAuthenticationMode based on EltMesIssAaaAuthenticationModeType"""
    defaultValue = 2


_EltMesIssAaaAuthenticationMode_Type.__name__ = "EltMesIssAaaAuthenticationModeType"
_EltMesIssAaaAuthenticationMode_Object = MibScalar
eltMesIssAaaAuthenticationMode = _EltMesIssAaaAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 5),
    _EltMesIssAaaAuthenticationMode_Type()
)
eltMesIssAaaAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaAuthenticationMode.setStatus("current")
_EltMesIssAaaMethodGlobalConfig_ObjectIdentity = ObjectIdentity
eltMesIssAaaMethodGlobalConfig = _EltMesIssAaaMethodGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 6)
)
_EltMesIssAaaMethodListTable_Object = MibTable
eltMesIssAaaMethodListTable = _EltMesIssAaaMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    eltMesIssAaaMethodListTable.setStatus("current")
_EltMesIssAaaMethodListEntry_Object = MibTableRow
eltMesIssAaaMethodListEntry = _EltMesIssAaaMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 6, 1, 1)
)
eltMesIssAaaMethodListEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-AAA-MIB", "eltMesIssAaaMethodListName"),
    (0, "ELTEX-MES-ISS-AAA-MIB", "eltMesIssAaaAuthenticationMethodIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssAaaMethodListEntry.setStatus("current")


class _EltMesIssAaaMethodListName_Type(DisplayString):
    """Custom type eltMesIssAaaMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_EltMesIssAaaMethodListName_Type.__name__ = "DisplayString"
_EltMesIssAaaMethodListName_Object = MibTableColumn
eltMesIssAaaMethodListName = _EltMesIssAaaMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 6, 1, 1, 1),
    _EltMesIssAaaMethodListName_Type()
)
eltMesIssAaaMethodListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssAaaMethodListName.setStatus("current")


class _EltMesIssAaaAuthenticationMethodIndex_Type(Integer32):
    """Custom type eltMesIssAaaAuthenticationMethodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EltMesIssAaaAuthenticationMethodIndex_Type.__name__ = "Integer32"
_EltMesIssAaaAuthenticationMethodIndex_Object = MibTableColumn
eltMesIssAaaAuthenticationMethodIndex = _EltMesIssAaaAuthenticationMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 6, 1, 1, 2),
    _EltMesIssAaaAuthenticationMethodIndex_Type()
)
eltMesIssAaaAuthenticationMethodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssAaaAuthenticationMethodIndex.setStatus("current")
_EltMesIssAaaMethodType_Type = EltMesIssAaaAuthenticationMethod
_EltMesIssAaaMethodType_Object = MibTableColumn
eltMesIssAaaMethodType = _EltMesIssAaaMethodType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 6, 1, 1, 3),
    _EltMesIssAaaMethodType_Type()
)
eltMesIssAaaMethodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaMethodType.setStatus("current")
_EltMesIssAaaMethodRowStatus_Type = RowStatus
_EltMesIssAaaMethodRowStatus_Object = MibTableColumn
eltMesIssAaaMethodRowStatus = _EltMesIssAaaMethodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 1, 6, 1, 1, 4),
    _EltMesIssAaaMethodRowStatus_Type()
)
eltMesIssAaaMethodRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaMethodRowStatus.setStatus("current")
_EltMesIssAaaLineConfig_ObjectIdentity = ObjectIdentity
eltMesIssAaaLineConfig = _EltMesIssAaaLineConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2)
)
_EltMesIssAaaLineLoginAuthenticationTable_Object = MibTable
eltMesIssAaaLineLoginAuthenticationTable = _EltMesIssAaaLineLoginAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssAaaLineLoginAuthenticationTable.setStatus("current")
_EltMesIssAaaLineLoginAuthenticationEntry_Object = MibTableRow
eltMesIssAaaLineLoginAuthenticationEntry = _EltMesIssAaaLineLoginAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 1, 1)
)
eltMesIssAaaLineLoginAuthenticationEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-AAA-MIB", "eltMesIssAaaLineLoginAuthenticationLineType"),
)
if mibBuilder.loadTexts:
    eltMesIssAaaLineLoginAuthenticationEntry.setStatus("current")
_EltMesIssAaaLineLoginAuthenticationLineType_Type = EltMesIssAaaLineType
_EltMesIssAaaLineLoginAuthenticationLineType_Object = MibTableColumn
eltMesIssAaaLineLoginAuthenticationLineType = _EltMesIssAaaLineLoginAuthenticationLineType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 1, 1, 1),
    _EltMesIssAaaLineLoginAuthenticationLineType_Type()
)
eltMesIssAaaLineLoginAuthenticationLineType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssAaaLineLoginAuthenticationLineType.setStatus("current")


class _EltMesIssAaaLineLoginMethodListName_Type(DisplayString):
    """Custom type eltMesIssAaaLineLoginMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_EltMesIssAaaLineLoginMethodListName_Type.__name__ = "DisplayString"
_EltMesIssAaaLineLoginMethodListName_Object = MibTableColumn
eltMesIssAaaLineLoginMethodListName = _EltMesIssAaaLineLoginMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 1, 1, 2),
    _EltMesIssAaaLineLoginMethodListName_Type()
)
eltMesIssAaaLineLoginMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaLineLoginMethodListName.setStatus("current")
_EltMesIssAaaLineEnableAuthenticationTable_Object = MibTable
eltMesIssAaaLineEnableAuthenticationTable = _EltMesIssAaaLineEnableAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltMesIssAaaLineEnableAuthenticationTable.setStatus("current")
_EltMesIssAaaLineEnableAuthenticationEntry_Object = MibTableRow
eltMesIssAaaLineEnableAuthenticationEntry = _EltMesIssAaaLineEnableAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 2, 1)
)
eltMesIssAaaLineEnableAuthenticationEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-AAA-MIB", "eltMesIssAaaLineEnableAuthenticationLineType"),
)
if mibBuilder.loadTexts:
    eltMesIssAaaLineEnableAuthenticationEntry.setStatus("current")
_EltMesIssAaaLineEnableAuthenticationLineType_Type = EltMesIssAaaLineType
_EltMesIssAaaLineEnableAuthenticationLineType_Object = MibTableColumn
eltMesIssAaaLineEnableAuthenticationLineType = _EltMesIssAaaLineEnableAuthenticationLineType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 2, 1, 1),
    _EltMesIssAaaLineEnableAuthenticationLineType_Type()
)
eltMesIssAaaLineEnableAuthenticationLineType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssAaaLineEnableAuthenticationLineType.setStatus("current")


class _EltMesIssAaaLineEnableMethodListName_Type(DisplayString):
    """Custom type eltMesIssAaaLineEnableMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_EltMesIssAaaLineEnableMethodListName_Type.__name__ = "DisplayString"
_EltMesIssAaaLineEnableMethodListName_Object = MibTableColumn
eltMesIssAaaLineEnableMethodListName = _EltMesIssAaaLineEnableMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 2, 1, 2),
    _EltMesIssAaaLineEnableMethodListName_Type()
)
eltMesIssAaaLineEnableMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaLineEnableMethodListName.setStatus("current")
_EltMesIssAaaLineIdleTimeoutTable_Object = MibTable
eltMesIssAaaLineIdleTimeoutTable = _EltMesIssAaaLineIdleTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eltMesIssAaaLineIdleTimeoutTable.setStatus("current")
_EltMesIssAaaLineIdleTimeoutEntry_Object = MibTableRow
eltMesIssAaaLineIdleTimeoutEntry = _EltMesIssAaaLineIdleTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 3, 1)
)
eltMesIssAaaLineIdleTimeoutEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-AAA-MIB", "eltMesIssAaaLineIdleTimeoutLineType"),
)
if mibBuilder.loadTexts:
    eltMesIssAaaLineIdleTimeoutEntry.setStatus("current")
_EltMesIssAaaLineIdleTimeoutLineType_Type = EltMesIssAaaLineType
_EltMesIssAaaLineIdleTimeoutLineType_Object = MibTableColumn
eltMesIssAaaLineIdleTimeoutLineType = _EltMesIssAaaLineIdleTimeoutLineType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 3, 1, 1),
    _EltMesIssAaaLineIdleTimeoutLineType_Type()
)
eltMesIssAaaLineIdleTimeoutLineType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssAaaLineIdleTimeoutLineType.setStatus("current")


class _EltMesIssLineIdleTimeout_Type(Unsigned32):
    """Custom type eltMesIssLineIdleTimeout based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18000),
    )


_EltMesIssLineIdleTimeout_Type.__name__ = "Unsigned32"
_EltMesIssLineIdleTimeout_Object = MibTableColumn
eltMesIssLineIdleTimeout = _EltMesIssLineIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 3, 1, 2),
    _EltMesIssLineIdleTimeout_Type()
)
eltMesIssLineIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssLineIdleTimeout.setStatus("current")
_EltMesIssAaaLineCommandAuthorizationTable_Object = MibTable
eltMesIssAaaLineCommandAuthorizationTable = _EltMesIssAaaLineCommandAuthorizationTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 4)
)
if mibBuilder.loadTexts:
    eltMesIssAaaLineCommandAuthorizationTable.setStatus("current")
_EltMesIssAaaLineCommandAuthorizationEntry_Object = MibTableRow
eltMesIssAaaLineCommandAuthorizationEntry = _EltMesIssAaaLineCommandAuthorizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 4, 1)
)
eltMesIssAaaLineCommandAuthorizationEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-AAA-MIB", "eltMesIssAaaLineCommandAuthorizationLineType"),
)
if mibBuilder.loadTexts:
    eltMesIssAaaLineCommandAuthorizationEntry.setStatus("current")
_EltMesIssAaaLineCommandAuthorizationLineType_Type = EltMesIssAaaLineType
_EltMesIssAaaLineCommandAuthorizationLineType_Object = MibTableColumn
eltMesIssAaaLineCommandAuthorizationLineType = _EltMesIssAaaLineCommandAuthorizationLineType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 4, 1, 1),
    _EltMesIssAaaLineCommandAuthorizationLineType_Type()
)
eltMesIssAaaLineCommandAuthorizationLineType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssAaaLineCommandAuthorizationLineType.setStatus("current")


class _EltMesIssAaaLineCommandAuthorizationMethod_Type(EltMesIssAaaAuthorizationMethod):
    """Custom type eltMesIssAaaLineCommandAuthorizationMethod based on EltMesIssAaaAuthorizationMethod"""
    defaultValue = 255


_EltMesIssAaaLineCommandAuthorizationMethod_Type.__name__ = "EltMesIssAaaAuthorizationMethod"
_EltMesIssAaaLineCommandAuthorizationMethod_Object = MibTableColumn
eltMesIssAaaLineCommandAuthorizationMethod = _EltMesIssAaaLineCommandAuthorizationMethod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 2, 4, 1, 2),
    _EltMesIssAaaLineCommandAuthorizationMethod_Type()
)
eltMesIssAaaLineCommandAuthorizationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaLineCommandAuthorizationMethod.setStatus("current")
_EltMesIssAaaWebConfig_ObjectIdentity = ObjectIdentity
eltMesIssAaaWebConfig = _EltMesIssAaaWebConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 3)
)


class _EltMesIssAaaWebLoginMethodListName_Type(DisplayString):
    """Custom type eltMesIssAaaWebLoginMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_EltMesIssAaaWebLoginMethodListName_Type.__name__ = "DisplayString"
_EltMesIssAaaWebLoginMethodListName_Object = MibScalar
eltMesIssAaaWebLoginMethodListName = _EltMesIssAaaWebLoginMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 1, 3, 1),
    _EltMesIssAaaWebLoginMethodListName_Type()
)
eltMesIssAaaWebLoginMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssAaaWebLoginMethodListName.setStatus("current")
_EltMesIssAaaNotifications_ObjectIdentity = ObjectIdentity
eltMesIssAaaNotifications = _EltMesIssAaaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 2)
)
_EltMesIssAaaNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltMesIssAaaNotificationsPrefix = _EltMesIssAaaNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 2, 0)
)

# Managed Objects groups


# Notification objects

eltMesIssAaaUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7, 2, 0, 1)
)
eltMesIssAaaUserTrap.setObjects(
    ("ELTEX-SMI-ACTUAL", "mcTrapDescr")
)
if mibBuilder.loadTexts:
    eltMesIssAaaUserTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-AAA-MIB",
    **{"EltMesIssAaaAuthenticationMethod": EltMesIssAaaAuthenticationMethod,
       "EltMesIssAaaAuthenticationModeType": EltMesIssAaaAuthenticationModeType,
       "EltMesIssAaaLineType": EltMesIssAaaLineType,
       "EltMesIssAaaTacacsAuthenticationType": EltMesIssAaaTacacsAuthenticationType,
       "EltMesIssAaaAuthorizationMethod": EltMesIssAaaAuthorizationMethod,
       "eltMesIssAaaMIB": eltMesIssAaaMIB,
       "eltMesIssAaaObjects": eltMesIssAaaObjects,
       "eltMesIssAaaGlobalConfig": eltMesIssAaaGlobalConfig,
       "eltMesIssAaaEnableAuthentication": eltMesIssAaaEnableAuthentication,
       "eltMesIssAaaTacacsGlobalConfig": eltMesIssAaaTacacsGlobalConfig,
       "eltMesIssAaaTacacsAuthenticationType": eltMesIssAaaTacacsAuthenticationType,
       "eltMesIssAaaTacacsAttrConfig": eltMesIssAaaTacacsAttrConfig,
       "eltMesIssAaaTacacsAttrPortConfigTable": eltMesIssAaaTacacsAttrPortConfigTable,
       "eltMesIssAaaTacacsAttrPortConfigEntry": eltMesIssAaaTacacsAttrPortConfigEntry,
       "eltMesIssAaaTacacsAttrPortLineType": eltMesIssAaaTacacsAttrPortLineType,
       "eltMesIssAaaTacacsAttrPortFormat": eltMesIssAaaTacacsAttrPortFormat,
       "eltMesIssAaaRadiusGlobalConfig": eltMesIssAaaRadiusGlobalConfig,
       "eltMesIssAaaCommandAuthorizationTable": eltMesIssAaaCommandAuthorizationTable,
       "eltMesIssAaaCommandAuthorizationEntry": eltMesIssAaaCommandAuthorizationEntry,
       "eltMesIssAaaCommandAuthorizationPrivilege": eltMesIssAaaCommandAuthorizationPrivilege,
       "eltMesIssAaaCommandAuthorizationMethod": eltMesIssAaaCommandAuthorizationMethod,
       "eltMesIssAaaAuthenticationMode": eltMesIssAaaAuthenticationMode,
       "eltMesIssAaaMethodGlobalConfig": eltMesIssAaaMethodGlobalConfig,
       "eltMesIssAaaMethodListTable": eltMesIssAaaMethodListTable,
       "eltMesIssAaaMethodListEntry": eltMesIssAaaMethodListEntry,
       "eltMesIssAaaMethodListName": eltMesIssAaaMethodListName,
       "eltMesIssAaaAuthenticationMethodIndex": eltMesIssAaaAuthenticationMethodIndex,
       "eltMesIssAaaMethodType": eltMesIssAaaMethodType,
       "eltMesIssAaaMethodRowStatus": eltMesIssAaaMethodRowStatus,
       "eltMesIssAaaLineConfig": eltMesIssAaaLineConfig,
       "eltMesIssAaaLineLoginAuthenticationTable": eltMesIssAaaLineLoginAuthenticationTable,
       "eltMesIssAaaLineLoginAuthenticationEntry": eltMesIssAaaLineLoginAuthenticationEntry,
       "eltMesIssAaaLineLoginAuthenticationLineType": eltMesIssAaaLineLoginAuthenticationLineType,
       "eltMesIssAaaLineLoginMethodListName": eltMesIssAaaLineLoginMethodListName,
       "eltMesIssAaaLineEnableAuthenticationTable": eltMesIssAaaLineEnableAuthenticationTable,
       "eltMesIssAaaLineEnableAuthenticationEntry": eltMesIssAaaLineEnableAuthenticationEntry,
       "eltMesIssAaaLineEnableAuthenticationLineType": eltMesIssAaaLineEnableAuthenticationLineType,
       "eltMesIssAaaLineEnableMethodListName": eltMesIssAaaLineEnableMethodListName,
       "eltMesIssAaaLineIdleTimeoutTable": eltMesIssAaaLineIdleTimeoutTable,
       "eltMesIssAaaLineIdleTimeoutEntry": eltMesIssAaaLineIdleTimeoutEntry,
       "eltMesIssAaaLineIdleTimeoutLineType": eltMesIssAaaLineIdleTimeoutLineType,
       "eltMesIssLineIdleTimeout": eltMesIssLineIdleTimeout,
       "eltMesIssAaaLineCommandAuthorizationTable": eltMesIssAaaLineCommandAuthorizationTable,
       "eltMesIssAaaLineCommandAuthorizationEntry": eltMesIssAaaLineCommandAuthorizationEntry,
       "eltMesIssAaaLineCommandAuthorizationLineType": eltMesIssAaaLineCommandAuthorizationLineType,
       "eltMesIssAaaLineCommandAuthorizationMethod": eltMesIssAaaLineCommandAuthorizationMethod,
       "eltMesIssAaaWebConfig": eltMesIssAaaWebConfig,
       "eltMesIssAaaWebLoginMethodListName": eltMesIssAaaWebLoginMethodListName,
       "eltMesIssAaaNotifications": eltMesIssAaaNotifications,
       "eltMesIssAaaNotificationsPrefix": eltMesIssAaaNotificationsPrefix,
       "eltMesIssAaaUserTrap": eltMesIssAaaUserTrap}
)
