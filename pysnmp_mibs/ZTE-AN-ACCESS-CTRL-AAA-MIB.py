# SNMP MIB module (ZTE-AN-ACCESS-CTRL-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ACCESS-CTRL-AAA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:41 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnAccessCtrlAaaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90)
)
if mibBuilder.loadTexts:
    zxAnAccessCtrlAaaMib.setRevisions(
        ("2012-11-07 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ZxAnAaaAuthenMethodPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )



class ZxAnAaaAuthorMethodPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )



# MIB Managed Objects in the order of their OIDs

_ZxAnAaaAuthenticationObjects_ObjectIdentity = ObjectIdentity
zxAnAaaAuthenticationObjects = _ZxAnAaaAuthenticationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2)
)
_ZxAnAaaAuthenGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnAaaAuthenGlobalObjects = _ZxAnAaaAuthenGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 1)
)


class _ZxAnAaaAuthenLocalPriority_Type(ZxAnAaaAuthenMethodPriority):
    """Custom type zxAnAaaAuthenLocalPriority based on ZxAnAaaAuthenMethodPriority"""
    defaultValue = 0


_ZxAnAaaAuthenLocalPriority_Type.__name__ = "ZxAnAaaAuthenMethodPriority"
_ZxAnAaaAuthenLocalPriority_Object = MibScalar
zxAnAaaAuthenLocalPriority = _ZxAnAaaAuthenLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 1, 1),
    _ZxAnAaaAuthenLocalPriority_Type()
)
zxAnAaaAuthenLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnAaaAuthenLocalPriority.setStatus("current")


class _ZxAnAaaAuthenTacacsplusPriority_Type(ZxAnAaaAuthenMethodPriority):
    """Custom type zxAnAaaAuthenTacacsplusPriority based on ZxAnAaaAuthenMethodPriority"""
    defaultValue = 0


_ZxAnAaaAuthenTacacsplusPriority_Type.__name__ = "ZxAnAaaAuthenMethodPriority"
_ZxAnAaaAuthenTacacsplusPriority_Object = MibScalar
zxAnAaaAuthenTacacsplusPriority = _ZxAnAaaAuthenTacacsplusPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 1, 2),
    _ZxAnAaaAuthenTacacsplusPriority_Type()
)
zxAnAaaAuthenTacacsplusPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnAaaAuthenTacacsplusPriority.setStatus("current")


class _ZxAnAaaAuthenNoAuthenMethodEn_Type(Integer32):
    """Custom type zxAnAaaAuthenNoAuthenMethodEn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnAaaAuthenNoAuthenMethodEn_Type.__name__ = "Integer32"
_ZxAnAaaAuthenNoAuthenMethodEn_Object = MibScalar
zxAnAaaAuthenNoAuthenMethodEn = _ZxAnAaaAuthenNoAuthenMethodEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 1, 3),
    _ZxAnAaaAuthenNoAuthenMethodEn_Type()
)
zxAnAaaAuthenNoAuthenMethodEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnAaaAuthenNoAuthenMethodEn.setStatus("current")


class _ZxAnAaaAuthenTacacsplusGroupName_Type(DisplayString):
    """Custom type zxAnAaaAuthenTacacsplusGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnAaaAuthenTacacsplusGroupName_Type.__name__ = "DisplayString"
_ZxAnAaaAuthenTacacsplusGroupName_Object = MibScalar
zxAnAaaAuthenTacacsplusGroupName = _ZxAnAaaAuthenTacacsplusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 1, 4),
    _ZxAnAaaAuthenTacacsplusGroupName_Type()
)
zxAnAaaAuthenTacacsplusGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnAaaAuthenTacacsplusGroupName.setStatus("current")
_ZxAnAaaAuthenticationSession_ObjectIdentity = ObjectIdentity
zxAnAaaAuthenticationSession = _ZxAnAaaAuthenticationSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 2)
)
_ZxAnAaaAuthenSessionTable_Object = MibTable
zxAnAaaAuthenSessionTable = _ZxAnAaaAuthenSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnAaaAuthenSessionTable.setStatus("current")
_ZxAnAaaAuthenSessionEntry_Object = MibTableRow
zxAnAaaAuthenSessionEntry = _ZxAnAaaAuthenSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 2, 2, 1)
)
zxAnAaaAuthenSessionEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-AAA-MIB", "zxAnAaaAuthenSessionType"),
)
if mibBuilder.loadTexts:
    zxAnAaaAuthenSessionEntry.setStatus("current")


class _ZxAnAaaAuthenSessionType_Type(Integer32):
    """Custom type zxAnAaaAuthenSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ssh", 2))
    )


_ZxAnAaaAuthenSessionType_Type.__name__ = "Integer32"
_ZxAnAaaAuthenSessionType_Object = MibTableColumn
zxAnAaaAuthenSessionType = _ZxAnAaaAuthenSessionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 2, 2, 1, 1),
    _ZxAnAaaAuthenSessionType_Type()
)
zxAnAaaAuthenSessionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAaaAuthenSessionType.setStatus("current")


class _ZxAnAaaAuthenSessionMethod_Type(Integer32):
    """Custom type zxAnAaaAuthenSessionMethod based on Integer32"""
    defaultValue = 1

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
          ("tacacsPlus", 2),
          ("radius", 3))
    )


_ZxAnAaaAuthenSessionMethod_Type.__name__ = "Integer32"
_ZxAnAaaAuthenSessionMethod_Object = MibTableColumn
zxAnAaaAuthenSessionMethod = _ZxAnAaaAuthenSessionMethod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 2, 2, 1, 2),
    _ZxAnAaaAuthenSessionMethod_Type()
)
zxAnAaaAuthenSessionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthenSessionMethod.setStatus("current")


class _ZxAnAaaAuthenSessionRadiusGrpId_Type(Integer32):
    """Custom type zxAnAaaAuthenSessionRadiusGrpId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ZxAnAaaAuthenSessionRadiusGrpId_Type.__name__ = "Integer32"
_ZxAnAaaAuthenSessionRadiusGrpId_Object = MibTableColumn
zxAnAaaAuthenSessionRadiusGrpId = _ZxAnAaaAuthenSessionRadiusGrpId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 2, 2, 1, 3),
    _ZxAnAaaAuthenSessionRadiusGrpId_Type()
)
zxAnAaaAuthenSessionRadiusGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthenSessionRadiusGrpId.setStatus("current")
_ZxAnAaaAuthenSessionRowStatus_Type = RowStatus
_ZxAnAaaAuthenSessionRowStatus_Object = MibTableColumn
zxAnAaaAuthenSessionRowStatus = _ZxAnAaaAuthenSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 2, 2, 1, 50),
    _ZxAnAaaAuthenSessionRowStatus_Type()
)
zxAnAaaAuthenSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthenSessionRowStatus.setStatus("current")
_ZxAnAaaAuthenticaitonLogin_ObjectIdentity = ObjectIdentity
zxAnAaaAuthenticaitonLogin = _ZxAnAaaAuthenticaitonLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 3)
)
_ZxAnAaaAuthenLoginTable_Object = MibTable
zxAnAaaAuthenLoginTable = _ZxAnAaaAuthenLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnAaaAuthenLoginTable.setStatus("current")
_ZxAnAaaAuthenLoginEntry_Object = MibTableRow
zxAnAaaAuthenLoginEntry = _ZxAnAaaAuthenLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 3, 2, 1)
)
zxAnAaaAuthenLoginEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-AAA-MIB", "zxAnAaaAuthenLoginMode"),
)
if mibBuilder.loadTexts:
    zxAnAaaAuthenLoginEntry.setStatus("current")


class _ZxAnAaaAuthenLoginMode_Type(Integer32):
    """Custom type zxAnAaaAuthenLoginMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("login", 1),
          ("enable", 2))
    )


_ZxAnAaaAuthenLoginMode_Type.__name__ = "Integer32"
_ZxAnAaaAuthenLoginMode_Object = MibTableColumn
zxAnAaaAuthenLoginMode = _ZxAnAaaAuthenLoginMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 3, 2, 1, 1),
    _ZxAnAaaAuthenLoginMode_Type()
)
zxAnAaaAuthenLoginMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAaaAuthenLoginMode.setStatus("current")


class _ZxAnAaaAuthenLoginLocalPri_Type(ZxAnAaaAuthenMethodPriority):
    """Custom type zxAnAaaAuthenLoginLocalPri based on ZxAnAaaAuthenMethodPriority"""
    defaultValue = 0


_ZxAnAaaAuthenLoginLocalPri_Type.__name__ = "ZxAnAaaAuthenMethodPriority"
_ZxAnAaaAuthenLoginLocalPri_Object = MibTableColumn
zxAnAaaAuthenLoginLocalPri = _ZxAnAaaAuthenLoginLocalPri_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 3, 2, 1, 2),
    _ZxAnAaaAuthenLoginLocalPri_Type()
)
zxAnAaaAuthenLoginLocalPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthenLoginLocalPri.setStatus("current")


class _ZxAnAaaAuthenLoginTacacsplusPri_Type(ZxAnAaaAuthenMethodPriority):
    """Custom type zxAnAaaAuthenLoginTacacsplusPri based on ZxAnAaaAuthenMethodPriority"""
    defaultValue = 0


_ZxAnAaaAuthenLoginTacacsplusPri_Type.__name__ = "ZxAnAaaAuthenMethodPriority"
_ZxAnAaaAuthenLoginTacacsplusPri_Object = MibTableColumn
zxAnAaaAuthenLoginTacacsplusPri = _ZxAnAaaAuthenLoginTacacsplusPri_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 3, 2, 1, 3),
    _ZxAnAaaAuthenLoginTacacsplusPri_Type()
)
zxAnAaaAuthenLoginTacacsplusPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthenLoginTacacsplusPri.setStatus("current")


class _ZxAnAaaAuthenLoginNoAuthMethodEn_Type(Integer32):
    """Custom type zxAnAaaAuthenLoginNoAuthMethodEn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnAaaAuthenLoginNoAuthMethodEn_Type.__name__ = "Integer32"
_ZxAnAaaAuthenLoginNoAuthMethodEn_Object = MibTableColumn
zxAnAaaAuthenLoginNoAuthMethodEn = _ZxAnAaaAuthenLoginNoAuthMethodEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 3, 2, 1, 4),
    _ZxAnAaaAuthenLoginNoAuthMethodEn_Type()
)
zxAnAaaAuthenLoginNoAuthMethodEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthenLoginNoAuthMethodEn.setStatus("current")


class _ZxAnAaaAuthenLoginTacplusGrpName_Type(DisplayString):
    """Custom type zxAnAaaAuthenLoginTacplusGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnAaaAuthenLoginTacplusGrpName_Type.__name__ = "DisplayString"
_ZxAnAaaAuthenLoginTacplusGrpName_Object = MibTableColumn
zxAnAaaAuthenLoginTacplusGrpName = _ZxAnAaaAuthenLoginTacplusGrpName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 3, 2, 1, 5),
    _ZxAnAaaAuthenLoginTacplusGrpName_Type()
)
zxAnAaaAuthenLoginTacplusGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthenLoginTacplusGrpName.setStatus("current")
_ZxAnAaaAuthenLoginRowStatus_Type = RowStatus
_ZxAnAaaAuthenLoginRowStatus_Object = MibTableColumn
zxAnAaaAuthenLoginRowStatus = _ZxAnAaaAuthenLoginRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 2, 3, 2, 1, 50),
    _ZxAnAaaAuthenLoginRowStatus_Type()
)
zxAnAaaAuthenLoginRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthenLoginRowStatus.setStatus("current")
_ZxAnAaaAuthorizationObjects_ObjectIdentity = ObjectIdentity
zxAnAaaAuthorizationObjects = _ZxAnAaaAuthorizationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3)
)
_ZxAnAaaAuthorGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnAaaAuthorGlobalObjects = _ZxAnAaaAuthorGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 1)
)


class _ZxAnAaaAuthorLocalPriority_Type(ZxAnAaaAuthorMethodPriority):
    """Custom type zxAnAaaAuthorLocalPriority based on ZxAnAaaAuthorMethodPriority"""
    defaultValue = 0


_ZxAnAaaAuthorLocalPriority_Type.__name__ = "ZxAnAaaAuthorMethodPriority"
_ZxAnAaaAuthorLocalPriority_Object = MibScalar
zxAnAaaAuthorLocalPriority = _ZxAnAaaAuthorLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 1, 1),
    _ZxAnAaaAuthorLocalPriority_Type()
)
zxAnAaaAuthorLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnAaaAuthorLocalPriority.setStatus("current")


class _ZxAnAaaAuthorTacacsplusPriority_Type(ZxAnAaaAuthorMethodPriority):
    """Custom type zxAnAaaAuthorTacacsplusPriority based on ZxAnAaaAuthorMethodPriority"""
    defaultValue = 0


_ZxAnAaaAuthorTacacsplusPriority_Type.__name__ = "ZxAnAaaAuthorMethodPriority"
_ZxAnAaaAuthorTacacsplusPriority_Object = MibScalar
zxAnAaaAuthorTacacsplusPriority = _ZxAnAaaAuthorTacacsplusPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 1, 2),
    _ZxAnAaaAuthorTacacsplusPriority_Type()
)
zxAnAaaAuthorTacacsplusPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnAaaAuthorTacacsplusPriority.setStatus("current")


class _ZxAnAaaAuthorNoAuthorMethodEn_Type(Integer32):
    """Custom type zxAnAaaAuthorNoAuthorMethodEn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnAaaAuthorNoAuthorMethodEn_Type.__name__ = "Integer32"
_ZxAnAaaAuthorNoAuthorMethodEn_Object = MibScalar
zxAnAaaAuthorNoAuthorMethodEn = _ZxAnAaaAuthorNoAuthorMethodEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 1, 3),
    _ZxAnAaaAuthorNoAuthorMethodEn_Type()
)
zxAnAaaAuthorNoAuthorMethodEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnAaaAuthorNoAuthorMethodEn.setStatus("current")


class _ZxAnAaaAuthorTacacsplusGroupName_Type(DisplayString):
    """Custom type zxAnAaaAuthorTacacsplusGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnAaaAuthorTacacsplusGroupName_Type.__name__ = "DisplayString"
_ZxAnAaaAuthorTacacsplusGroupName_Object = MibScalar
zxAnAaaAuthorTacacsplusGroupName = _ZxAnAaaAuthorTacacsplusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 1, 4),
    _ZxAnAaaAuthorTacacsplusGroupName_Type()
)
zxAnAaaAuthorTacacsplusGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnAaaAuthorTacacsplusGroupName.setStatus("current")
_ZxAnAaaAuthorizationSession_ObjectIdentity = ObjectIdentity
zxAnAaaAuthorizationSession = _ZxAnAaaAuthorizationSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 3)
)
_ZxAnAaaAuthorSessionTable_Object = MibTable
zxAnAaaAuthorSessionTable = _ZxAnAaaAuthorSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnAaaAuthorSessionTable.setStatus("current")
_ZxAnAaaAuthorSessionEntry_Object = MibTableRow
zxAnAaaAuthorSessionEntry = _ZxAnAaaAuthorSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 3, 2, 1)
)
zxAnAaaAuthorSessionEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-AAA-MIB", "zxAnAaaAuthorSessionType"),
)
if mibBuilder.loadTexts:
    zxAnAaaAuthorSessionEntry.setStatus("current")


class _ZxAnAaaAuthorSessionType_Type(Integer32):
    """Custom type zxAnAaaAuthorSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ssh", 2))
    )


_ZxAnAaaAuthorSessionType_Type.__name__ = "Integer32"
_ZxAnAaaAuthorSessionType_Object = MibTableColumn
zxAnAaaAuthorSessionType = _ZxAnAaaAuthorSessionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 3, 2, 1, 1),
    _ZxAnAaaAuthorSessionType_Type()
)
zxAnAaaAuthorSessionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAaaAuthorSessionType.setStatus("current")


class _ZxAnAaaAuthorSessionMethod_Type(Integer32):
    """Custom type zxAnAaaAuthorSessionMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("tacacsPlus", 2))
    )


_ZxAnAaaAuthorSessionMethod_Type.__name__ = "Integer32"
_ZxAnAaaAuthorSessionMethod_Object = MibTableColumn
zxAnAaaAuthorSessionMethod = _ZxAnAaaAuthorSessionMethod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 3, 2, 1, 2),
    _ZxAnAaaAuthorSessionMethod_Type()
)
zxAnAaaAuthorSessionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthorSessionMethod.setStatus("current")


class _ZxAnAaaAuthorSessionSshMode_Type(Integer32):
    """Custom type zxAnAaaAuthorSessionSshMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nouse", 1),
          ("chap", 2),
          ("pap", 3))
    )


_ZxAnAaaAuthorSessionSshMode_Type.__name__ = "Integer32"
_ZxAnAaaAuthorSessionSshMode_Object = MibTableColumn
zxAnAaaAuthorSessionSshMode = _ZxAnAaaAuthorSessionSshMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 3, 2, 1, 3),
    _ZxAnAaaAuthorSessionSshMode_Type()
)
zxAnAaaAuthorSessionSshMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthorSessionSshMode.setStatus("current")
_ZxAnAaaAuthorSessionRowStatus_Type = RowStatus
_ZxAnAaaAuthorSessionRowStatus_Object = MibTableColumn
zxAnAaaAuthorSessionRowStatus = _ZxAnAaaAuthorSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 3, 3, 2, 1, 50),
    _ZxAnAaaAuthorSessionRowStatus_Type()
)
zxAnAaaAuthorSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAuthorSessionRowStatus.setStatus("current")
_ZxAnAaaAccountingObjects_ObjectIdentity = ObjectIdentity
zxAnAaaAccountingObjects = _ZxAnAaaAccountingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 4)
)
_ZxAnAaaAccountPrivilege_ObjectIdentity = ObjectIdentity
zxAnAaaAccountPrivilege = _ZxAnAaaAccountPrivilege_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 4, 2)
)
_ZxAnAaaAccountPrivilegeTable_Object = MibTable
zxAnAaaAccountPrivilegeTable = _ZxAnAaaAccountPrivilegeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 4, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnAaaAccountPrivilegeTable.setStatus("current")
_ZxAnAaaAccountPrivilegeEntry_Object = MibTableRow
zxAnAaaAccountPrivilegeEntry = _ZxAnAaaAccountPrivilegeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 4, 2, 2, 1)
)
zxAnAaaAccountPrivilegeEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-AAA-MIB", "zxAnAaaAccountUserPrivilege"),
)
if mibBuilder.loadTexts:
    zxAnAaaAccountPrivilegeEntry.setStatus("current")


class _ZxAnAaaAccountUserPrivilege_Type(Integer32):
    """Custom type zxAnAaaAccountUserPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ZxAnAaaAccountUserPrivilege_Type.__name__ = "Integer32"
_ZxAnAaaAccountUserPrivilege_Object = MibTableColumn
zxAnAaaAccountUserPrivilege = _ZxAnAaaAccountUserPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 4, 2, 2, 1, 1),
    _ZxAnAaaAccountUserPrivilege_Type()
)
zxAnAaaAccountUserPrivilege.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAaaAccountUserPrivilege.setStatus("current")


class _ZxAnAaaAccountTacacsplusGrpName_Type(DisplayString):
    """Custom type zxAnAaaAccountTacacsplusGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnAaaAccountTacacsplusGrpName_Type.__name__ = "DisplayString"
_ZxAnAaaAccountTacacsplusGrpName_Object = MibTableColumn
zxAnAaaAccountTacacsplusGrpName = _ZxAnAaaAccountTacacsplusGrpName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 4, 2, 2, 1, 2),
    _ZxAnAaaAccountTacacsplusGrpName_Type()
)
zxAnAaaAccountTacacsplusGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAccountTacacsplusGrpName.setStatus("current")
_ZxAnAaaAccountPrivilegeRowStatus_Type = RowStatus
_ZxAnAaaAccountPrivilegeRowStatus_Object = MibTableColumn
zxAnAaaAccountPrivilegeRowStatus = _ZxAnAaaAccountPrivilegeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 90, 4, 2, 2, 1, 50),
    _ZxAnAaaAccountPrivilegeRowStatus_Type()
)
zxAnAaaAccountPrivilegeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAaaAccountPrivilegeRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ACCESS-CTRL-AAA-MIB",
    **{"ZxAnAaaAuthenMethodPriority": ZxAnAaaAuthenMethodPriority,
       "ZxAnAaaAuthorMethodPriority": ZxAnAaaAuthorMethodPriority,
       "zxAnAccessCtrlAaaMib": zxAnAccessCtrlAaaMib,
       "zxAnAaaAuthenticationObjects": zxAnAaaAuthenticationObjects,
       "zxAnAaaAuthenGlobalObjects": zxAnAaaAuthenGlobalObjects,
       "zxAnAaaAuthenLocalPriority": zxAnAaaAuthenLocalPriority,
       "zxAnAaaAuthenTacacsplusPriority": zxAnAaaAuthenTacacsplusPriority,
       "zxAnAaaAuthenNoAuthenMethodEn": zxAnAaaAuthenNoAuthenMethodEn,
       "zxAnAaaAuthenTacacsplusGroupName": zxAnAaaAuthenTacacsplusGroupName,
       "zxAnAaaAuthenticationSession": zxAnAaaAuthenticationSession,
       "zxAnAaaAuthenSessionTable": zxAnAaaAuthenSessionTable,
       "zxAnAaaAuthenSessionEntry": zxAnAaaAuthenSessionEntry,
       "zxAnAaaAuthenSessionType": zxAnAaaAuthenSessionType,
       "zxAnAaaAuthenSessionMethod": zxAnAaaAuthenSessionMethod,
       "zxAnAaaAuthenSessionRadiusGrpId": zxAnAaaAuthenSessionRadiusGrpId,
       "zxAnAaaAuthenSessionRowStatus": zxAnAaaAuthenSessionRowStatus,
       "zxAnAaaAuthenticaitonLogin": zxAnAaaAuthenticaitonLogin,
       "zxAnAaaAuthenLoginTable": zxAnAaaAuthenLoginTable,
       "zxAnAaaAuthenLoginEntry": zxAnAaaAuthenLoginEntry,
       "zxAnAaaAuthenLoginMode": zxAnAaaAuthenLoginMode,
       "zxAnAaaAuthenLoginLocalPri": zxAnAaaAuthenLoginLocalPri,
       "zxAnAaaAuthenLoginTacacsplusPri": zxAnAaaAuthenLoginTacacsplusPri,
       "zxAnAaaAuthenLoginNoAuthMethodEn": zxAnAaaAuthenLoginNoAuthMethodEn,
       "zxAnAaaAuthenLoginTacplusGrpName": zxAnAaaAuthenLoginTacplusGrpName,
       "zxAnAaaAuthenLoginRowStatus": zxAnAaaAuthenLoginRowStatus,
       "zxAnAaaAuthorizationObjects": zxAnAaaAuthorizationObjects,
       "zxAnAaaAuthorGlobalObjects": zxAnAaaAuthorGlobalObjects,
       "zxAnAaaAuthorLocalPriority": zxAnAaaAuthorLocalPriority,
       "zxAnAaaAuthorTacacsplusPriority": zxAnAaaAuthorTacacsplusPriority,
       "zxAnAaaAuthorNoAuthorMethodEn": zxAnAaaAuthorNoAuthorMethodEn,
       "zxAnAaaAuthorTacacsplusGroupName": zxAnAaaAuthorTacacsplusGroupName,
       "zxAnAaaAuthorizationSession": zxAnAaaAuthorizationSession,
       "zxAnAaaAuthorSessionTable": zxAnAaaAuthorSessionTable,
       "zxAnAaaAuthorSessionEntry": zxAnAaaAuthorSessionEntry,
       "zxAnAaaAuthorSessionType": zxAnAaaAuthorSessionType,
       "zxAnAaaAuthorSessionMethod": zxAnAaaAuthorSessionMethod,
       "zxAnAaaAuthorSessionSshMode": zxAnAaaAuthorSessionSshMode,
       "zxAnAaaAuthorSessionRowStatus": zxAnAaaAuthorSessionRowStatus,
       "zxAnAaaAccountingObjects": zxAnAaaAccountingObjects,
       "zxAnAaaAccountPrivilege": zxAnAaaAccountPrivilege,
       "zxAnAaaAccountPrivilegeTable": zxAnAaaAccountPrivilegeTable,
       "zxAnAaaAccountPrivilegeEntry": zxAnAaaAccountPrivilegeEntry,
       "zxAnAaaAccountUserPrivilege": zxAnAaaAccountUserPrivilege,
       "zxAnAaaAccountTacacsplusGrpName": zxAnAaaAccountTacacsplusGrpName,
       "zxAnAaaAccountPrivilegeRowStatus": zxAnAaaAccountPrivilegeRowStatus}
)
