# SNMP MIB module (ZTE-AN-SIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-SIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:44 2025
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

zxAnSipMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxAn_ObjectIdentity = ObjectIdentity
zxAn = _ZxAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015)
)
_ZxAnVoiceMgmt_ObjectIdentity = ObjectIdentity
zxAnVoiceMgmt = _ZxAnVoiceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3)
)
_ZxAnSipConfig_ObjectIdentity = ObjectIdentity
zxAnSipConfig = _ZxAnSipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8)
)
_ZxMsagSipUserTable_Object = MibTable
zxMsagSipUserTable = _ZxMsagSipUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1)
)
if mibBuilder.loadTexts:
    zxMsagSipUserTable.setStatus("current")
_ZxMsagSipUserEntry_Object = MibTableRow
zxMsagSipUserEntry = _ZxMsagSipUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1)
)
zxMsagSipUserEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipUserRack"),
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipUserShelf"),
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipUserSlot"),
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipUserIndex"),
)
if mibBuilder.loadTexts:
    zxMsagSipUserEntry.setStatus("current")


class _ZxMsagSipUserRack_Type(Integer32):
    """Custom type zxMsagSipUserRack based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxMsagSipUserRack_Type.__name__ = "Integer32"
_ZxMsagSipUserRack_Object = MibTableColumn
zxMsagSipUserRack = _ZxMsagSipUserRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 1),
    _ZxMsagSipUserRack_Type()
)
zxMsagSipUserRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipUserRack.setStatus("current")


class _ZxMsagSipUserShelf_Type(Integer32):
    """Custom type zxMsagSipUserShelf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ZxMsagSipUserShelf_Type.__name__ = "Integer32"
_ZxMsagSipUserShelf_Object = MibTableColumn
zxMsagSipUserShelf = _ZxMsagSipUserShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 2),
    _ZxMsagSipUserShelf_Type()
)
zxMsagSipUserShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipUserShelf.setStatus("current")


class _ZxMsagSipUserSlot_Type(Integer32):
    """Custom type zxMsagSipUserSlot based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_ZxMsagSipUserSlot_Type.__name__ = "Integer32"
_ZxMsagSipUserSlot_Object = MibTableColumn
zxMsagSipUserSlot = _ZxMsagSipUserSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 3),
    _ZxMsagSipUserSlot_Type()
)
zxMsagSipUserSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipUserSlot.setStatus("current")


class _ZxMsagSipUserIndex_Type(Integer32):
    """Custom type zxMsagSipUserIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ZxMsagSipUserIndex_Type.__name__ = "Integer32"
_ZxMsagSipUserIndex_Object = MibTableColumn
zxMsagSipUserIndex = _ZxMsagSipUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 4),
    _ZxMsagSipUserIndex_Type()
)
zxMsagSipUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipUserIndex.setStatus("current")


class _ZxMsagSipUserOperNum_Type(Integer32):
    """Custom type zxMsagSipUserOperNum based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ZxMsagSipUserOperNum_Type.__name__ = "Integer32"
_ZxMsagSipUserOperNum_Object = MibTableColumn
zxMsagSipUserOperNum = _ZxMsagSipUserOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 5),
    _ZxMsagSipUserOperNum_Type()
)
zxMsagSipUserOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserOperNum.setStatus("current")


class _ZxMsagSipUserSipDigit_Type(DisplayString):
    """Custom type zxMsagSipUserSipDigit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxMsagSipUserSipDigit_Type.__name__ = "DisplayString"
_ZxMsagSipUserSipDigit_Object = MibTableColumn
zxMsagSipUserSipDigit = _ZxMsagSipUserSipDigit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 6),
    _ZxMsagSipUserSipDigit_Type()
)
zxMsagSipUserSipDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserSipDigit.setStatus("current")


class _ZxMsagSipUserAuthusername_Type(DisplayString):
    """Custom type zxMsagSipUserAuthusername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxMsagSipUserAuthusername_Type.__name__ = "DisplayString"
_ZxMsagSipUserAuthusername_Object = MibTableColumn
zxMsagSipUserAuthusername = _ZxMsagSipUserAuthusername_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 7),
    _ZxMsagSipUserAuthusername_Type()
)
zxMsagSipUserAuthusername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserAuthusername.setStatus("current")


class _ZxMsagSipUserId_Type(DisplayString):
    """Custom type zxMsagSipUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxMsagSipUserId_Type.__name__ = "DisplayString"
_ZxMsagSipUserId_Object = MibTableColumn
zxMsagSipUserId = _ZxMsagSipUserId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 8),
    _ZxMsagSipUserId_Type()
)
zxMsagSipUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserId.setStatus("current")


class _ZxMsagSipUserType_Type(Integer32):
    """Custom type zxMsagSipUserType based on Integer32"""
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
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3))
    )


_ZxMsagSipUserType_Type.__name__ = "Integer32"
_ZxMsagSipUserType_Object = MibTableColumn
zxMsagSipUserType = _ZxMsagSipUserType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 9),
    _ZxMsagSipUserType_Type()
)
zxMsagSipUserType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserType.setStatus("current")


class _ZxMsagSipUserBeginNo_Type(Integer32):
    """Custom type zxMsagSipUserBeginNo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxMsagSipUserBeginNo_Type.__name__ = "Integer32"
_ZxMsagSipUserBeginNo_Object = MibTableColumn
zxMsagSipUserBeginNo = _ZxMsagSipUserBeginNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 10),
    _ZxMsagSipUserBeginNo_Type()
)
zxMsagSipUserBeginNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserBeginNo.setStatus("current")


class _ZxMsagSipUserDigitLen_Type(Integer32):
    """Custom type zxMsagSipUserDigitLen based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ZxMsagSipUserDigitLen_Type.__name__ = "Integer32"
_ZxMsagSipUserDigitLen_Object = MibTableColumn
zxMsagSipUserDigitLen = _ZxMsagSipUserDigitLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 11),
    _ZxMsagSipUserDigitLen_Type()
)
zxMsagSipUserDigitLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserDigitLen.setStatus("current")


class _ZxMsagSipUserPassword_Type(DisplayString):
    """Custom type zxMsagSipUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxMsagSipUserPassword_Type.__name__ = "DisplayString"
_ZxMsagSipUserPassword_Object = MibTableColumn
zxMsagSipUserPassword = _ZxMsagSipUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 12),
    _ZxMsagSipUserPassword_Type()
)
zxMsagSipUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserPassword.setStatus("current")


class _ZxMsagSipUserDstngRing_Type(Integer32):
    """Custom type zxMsagSipUserDstngRing based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZxMsagSipUserDstngRing_Type.__name__ = "Integer32"
_ZxMsagSipUserDstngRing_Object = MibTableColumn
zxMsagSipUserDstngRing = _ZxMsagSipUserDstngRing_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 13),
    _ZxMsagSipUserDstngRing_Type()
)
zxMsagSipUserDstngRing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserDstngRing.setStatus("current")


class _ZxMsagSipUserHotlineType_Type(Integer32):
    """Custom type zxMsagSipUserHotlineType based on Integer32"""
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
        *(("noneHotline", 1),
          ("instantHotline", 2),
          ("delayHotline", 3))
    )


_ZxMsagSipUserHotlineType_Type.__name__ = "Integer32"
_ZxMsagSipUserHotlineType_Object = MibTableColumn
zxMsagSipUserHotlineType = _ZxMsagSipUserHotlineType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 14),
    _ZxMsagSipUserHotlineType_Type()
)
zxMsagSipUserHotlineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserHotlineType.setStatus("current")


class _ZxMsagSipUserHotlineNum_Type(DisplayString):
    """Custom type zxMsagSipUserHotlineNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxMsagSipUserHotlineNum_Type.__name__ = "DisplayString"
_ZxMsagSipUserHotlineNum_Object = MibTableColumn
zxMsagSipUserHotlineNum = _ZxMsagSipUserHotlineNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 15),
    _ZxMsagSipUserHotlineNum_Type()
)
zxMsagSipUserHotlineNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserHotlineNum.setStatus("current")


class _ZxMsagSipUserDigitMap_Type(DisplayString):
    """Custom type zxMsagSipUserDigitMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ZxMsagSipUserDigitMap_Type.__name__ = "DisplayString"
_ZxMsagSipUserDigitMap_Object = MibTableColumn
zxMsagSipUserDigitMap = _ZxMsagSipUserDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 16),
    _ZxMsagSipUserDigitMap_Type()
)
zxMsagSipUserDigitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserDigitMap.setStatus("current")


class _ZxMsagSipUserOperType_Type(Integer32):
    """Custom type zxMsagSipUserOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sipuser", 1),
          ("sipuserid", 2))
    )


_ZxMsagSipUserOperType_Type.__name__ = "Integer32"
_ZxMsagSipUserOperType_Object = MibTableColumn
zxMsagSipUserOperType = _ZxMsagSipUserOperType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 17),
    _ZxMsagSipUserOperType_Type()
)
zxMsagSipUserOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserOperType.setStatus("current")


class _ZxMsagSipUserGroupId_Type(Integer32):
    """Custom type zxMsagSipUserGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ZxMsagSipUserGroupId_Type.__name__ = "Integer32"
_ZxMsagSipUserGroupId_Object = MibTableColumn
zxMsagSipUserGroupId = _ZxMsagSipUserGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 18),
    _ZxMsagSipUserGroupId_Type()
)
zxMsagSipUserGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserGroupId.setStatus("current")


class _ZxMsagSipUserAdminStatus_Type(Integer32):
    """Custom type zxMsagSipUserAdminStatus based on Integer32"""
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


_ZxMsagSipUserAdminStatus_Type.__name__ = "Integer32"
_ZxMsagSipUserAdminStatus_Object = MibTableColumn
zxMsagSipUserAdminStatus = _ZxMsagSipUserAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 19),
    _ZxMsagSipUserAdminStatus_Type()
)
zxMsagSipUserAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserAdminStatus.setStatus("current")


class _ZxMsagSipUserSessionLimit_Type(TruthValue):
    """Custom type zxMsagSipUserSessionLimit based on TruthValue"""
    defaultValue = 2


_ZxMsagSipUserSessionLimit_Type.__name__ = "TruthValue"
_ZxMsagSipUserSessionLimit_Object = MibTableColumn
zxMsagSipUserSessionLimit = _ZxMsagSipUserSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 20),
    _ZxMsagSipUserSessionLimit_Type()
)
zxMsagSipUserSessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserSessionLimit.setStatus("current")


class _ZxMsagSipUserRegisterStatus_Type(Integer32):
    """Custom type zxMsagSipUserRegisterStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2))
    )


_ZxMsagSipUserRegisterStatus_Type.__name__ = "Integer32"
_ZxMsagSipUserRegisterStatus_Object = MibTableColumn
zxMsagSipUserRegisterStatus = _ZxMsagSipUserRegisterStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 21),
    _ZxMsagSipUserRegisterStatus_Type()
)
zxMsagSipUserRegisterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxMsagSipUserRegisterStatus.setStatus("current")
_ZxMsagSipUserRowStatus_Type = RowStatus
_ZxMsagSipUserRowStatus_Object = MibTableColumn
zxMsagSipUserRowStatus = _ZxMsagSipUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 1, 1, 50),
    _ZxMsagSipUserRowStatus_Type()
)
zxMsagSipUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipUserRowStatus.setStatus("current")
_ZxMsagSipAccessCodeTable_Object = MibTable
zxMsagSipAccessCodeTable = _ZxMsagSipAccessCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 2)
)
if mibBuilder.loadTexts:
    zxMsagSipAccessCodeTable.setStatus("current")
_ZxMsagSipAccessCodeEntry_Object = MibTableRow
zxMsagSipAccessCodeEntry = _ZxMsagSipAccessCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 2, 1)
)
zxMsagSipAccessCodeEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipAccessCodeMgId"),
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipAccessCodeId"),
)
if mibBuilder.loadTexts:
    zxMsagSipAccessCodeEntry.setStatus("current")


class _ZxMsagSipAccessCodeMgId_Type(Integer32):
    """Custom type zxMsagSipAccessCodeMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxMsagSipAccessCodeMgId_Type.__name__ = "Integer32"
_ZxMsagSipAccessCodeMgId_Object = MibTableColumn
zxMsagSipAccessCodeMgId = _ZxMsagSipAccessCodeMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 2, 1, 1),
    _ZxMsagSipAccessCodeMgId_Type()
)
zxMsagSipAccessCodeMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipAccessCodeMgId.setStatus("current")


class _ZxMsagSipAccessCodeId_Type(Integer32):
    """Custom type zxMsagSipAccessCodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ZxMsagSipAccessCodeId_Type.__name__ = "Integer32"
_ZxMsagSipAccessCodeId_Object = MibTableColumn
zxMsagSipAccessCodeId = _ZxMsagSipAccessCodeId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 2, 1, 2),
    _ZxMsagSipAccessCodeId_Type()
)
zxMsagSipAccessCodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipAccessCodeId.setStatus("current")


class _ZxMsagSipAccessCodecode_Type(DisplayString):
    """Custom type zxMsagSipAccessCodecode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_ZxMsagSipAccessCodecode_Type.__name__ = "DisplayString"
_ZxMsagSipAccessCodecode_Object = MibTableColumn
zxMsagSipAccessCodecode = _ZxMsagSipAccessCodecode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 2, 1, 3),
    _ZxMsagSipAccessCodecode_Type()
)
zxMsagSipAccessCodecode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipAccessCodecode.setStatus("current")
_ZxMsagSipAccessCodeRowStatus_Type = RowStatus
_ZxMsagSipAccessCodeRowStatus_Object = MibTableColumn
zxMsagSipAccessCodeRowStatus = _ZxMsagSipAccessCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 2, 1, 20),
    _ZxMsagSipAccessCodeRowStatus_Type()
)
zxMsagSipAccessCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipAccessCodeRowStatus.setStatus("current")
_ZxMsagSipServiceCodeTable_Object = MibTable
zxMsagSipServiceCodeTable = _ZxMsagSipServiceCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 3)
)
if mibBuilder.loadTexts:
    zxMsagSipServiceCodeTable.setStatus("current")
_ZxMsagSipServiceCodeEntry_Object = MibTableRow
zxMsagSipServiceCodeEntry = _ZxMsagSipServiceCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 3, 1)
)
zxMsagSipServiceCodeEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipServiceCodeMgId"),
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipServiceCodeType"),
)
if mibBuilder.loadTexts:
    zxMsagSipServiceCodeEntry.setStatus("current")


class _ZxMsagSipServiceCodeMgId_Type(Integer32):
    """Custom type zxMsagSipServiceCodeMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxMsagSipServiceCodeMgId_Type.__name__ = "Integer32"
_ZxMsagSipServiceCodeMgId_Object = MibTableColumn
zxMsagSipServiceCodeMgId = _ZxMsagSipServiceCodeMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 3, 1, 1),
    _ZxMsagSipServiceCodeMgId_Type()
)
zxMsagSipServiceCodeMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipServiceCodeMgId.setStatus("current")


class _ZxMsagSipServiceCodeType_Type(Integer32):
    """Custom type zxMsagSipServiceCodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("conference", 1),
          ("threeWayConference", 2),
          ("refere", 3))
    )


_ZxMsagSipServiceCodeType_Type.__name__ = "Integer32"
_ZxMsagSipServiceCodeType_Object = MibTableColumn
zxMsagSipServiceCodeType = _ZxMsagSipServiceCodeType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 3, 1, 2),
    _ZxMsagSipServiceCodeType_Type()
)
zxMsagSipServiceCodeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipServiceCodeType.setStatus("current")


class _ZxMsagSipServiceCode_Type(DisplayString):
    """Custom type zxMsagSipServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxMsagSipServiceCode_Type.__name__ = "DisplayString"
_ZxMsagSipServiceCode_Object = MibTableColumn
zxMsagSipServiceCode = _ZxMsagSipServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 3, 1, 3),
    _ZxMsagSipServiceCode_Type()
)
zxMsagSipServiceCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipServiceCode.setStatus("current")
_ZxMsagSipServiceCodeRowStatus_Type = RowStatus
_ZxMsagSipServiceCodeRowStatus_Object = MibTableColumn
zxMsagSipServiceCodeRowStatus = _ZxMsagSipServiceCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 3, 1, 20),
    _ZxMsagSipServiceCodeRowStatus_Type()
)
zxMsagSipServiceCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipServiceCodeRowStatus.setStatus("current")
_ZxMsagSipGenFmtTable_Object = MibTable
zxMsagSipGenFmtTable = _ZxMsagSipGenFmtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 4)
)
if mibBuilder.loadTexts:
    zxMsagSipGenFmtTable.setStatus("current")
_ZxMsagSipGenFmtEntry_Object = MibTableRow
zxMsagSipGenFmtEntry = _ZxMsagSipGenFmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 4, 1)
)
zxMsagSipGenFmtEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipGenFmtMgId"),
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipGenFmtField"),
)
if mibBuilder.loadTexts:
    zxMsagSipGenFmtEntry.setStatus("current")


class _ZxMsagSipGenFmtMgId_Type(Integer32):
    """Custom type zxMsagSipGenFmtMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxMsagSipGenFmtMgId_Type.__name__ = "Integer32"
_ZxMsagSipGenFmtMgId_Object = MibTableColumn
zxMsagSipGenFmtMgId = _ZxMsagSipGenFmtMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 4, 1, 1),
    _ZxMsagSipGenFmtMgId_Type()
)
zxMsagSipGenFmtMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipGenFmtMgId.setStatus("current")


class _ZxMsagSipGenFmtField_Type(Integer32):
    """Custom type zxMsagSipGenFmtField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("from", 1),
          ("to", 2),
          ("requireline", 3))
    )


_ZxMsagSipGenFmtField_Type.__name__ = "Integer32"
_ZxMsagSipGenFmtField_Object = MibTableColumn
zxMsagSipGenFmtField = _ZxMsagSipGenFmtField_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 4, 1, 2),
    _ZxMsagSipGenFmtField_Type()
)
zxMsagSipGenFmtField.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipGenFmtField.setStatus("current")


class _ZxMsagSipGenFmtValue_Type(Integer32):
    """Custom type zxMsagSipGenFmtValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sipuserid", 1),
          ("telephone", 2))
    )


_ZxMsagSipGenFmtValue_Type.__name__ = "Integer32"
_ZxMsagSipGenFmtValue_Object = MibTableColumn
zxMsagSipGenFmtValue = _ZxMsagSipGenFmtValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 4, 1, 3),
    _ZxMsagSipGenFmtValue_Type()
)
zxMsagSipGenFmtValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxMsagSipGenFmtValue.setStatus("current")
_ZxMsagSipCapTable_Object = MibTable
zxMsagSipCapTable = _ZxMsagSipCapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5)
)
if mibBuilder.loadTexts:
    zxMsagSipCapTable.setStatus("current")
_ZxMsagSipCapEntry_Object = MibTableRow
zxMsagSipCapEntry = _ZxMsagSipCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1)
)
zxMsagSipCapEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxMsagSipCapMgId"),
)
if mibBuilder.loadTexts:
    zxMsagSipCapEntry.setStatus("current")


class _ZxMsagSipCapMgId_Type(Integer32):
    """Custom type zxMsagSipCapMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxMsagSipCapMgId_Type.__name__ = "Integer32"
_ZxMsagSipCapMgId_Object = MibTableColumn
zxMsagSipCapMgId = _ZxMsagSipCapMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 1),
    _ZxMsagSipCapMgId_Type()
)
zxMsagSipCapMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxMsagSipCapMgId.setStatus("current")


class _ZxMsagSipCapSpPrecondition_Type(TruthValue):
    """Custom type zxMsagSipCapSpPrecondition based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapSpPrecondition_Type.__name__ = "TruthValue"
_ZxMsagSipCapSpPrecondition_Object = MibTableColumn
zxMsagSipCapSpPrecondition = _ZxMsagSipCapSpPrecondition_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 2),
    _ZxMsagSipCapSpPrecondition_Type()
)
zxMsagSipCapSpPrecondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSpPrecondition.setStatus("current")


class _ZxMsagSipCapNeedReserveRes_Type(TruthValue):
    """Custom type zxMsagSipCapNeedReserveRes based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapNeedReserveRes_Type.__name__ = "TruthValue"
_ZxMsagSipCapNeedReserveRes_Object = MibTableColumn
zxMsagSipCapNeedReserveRes = _ZxMsagSipCapNeedReserveRes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 3),
    _ZxMsagSipCapNeedReserveRes_Type()
)
zxMsagSipCapNeedReserveRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapNeedReserveRes.setStatus("current")


class _ZxMsagSipCapSpEarlySession_Type(TruthValue):
    """Custom type zxMsagSipCapSpEarlySession based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapSpEarlySession_Type.__name__ = "TruthValue"
_ZxMsagSipCapSpEarlySession_Object = MibTableColumn
zxMsagSipCapSpEarlySession = _ZxMsagSipCapSpEarlySession_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 4),
    _ZxMsagSipCapSpEarlySession_Type()
)
zxMsagSipCapSpEarlySession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSpEarlySession.setStatus("current")


class _ZxMsagSipCapSp100Rel_Type(TruthValue):
    """Custom type zxMsagSipCapSp100Rel based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapSp100Rel_Type.__name__ = "TruthValue"
_ZxMsagSipCapSp100Rel_Object = MibTableColumn
zxMsagSipCapSp100Rel = _ZxMsagSipCapSp100Rel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 5),
    _ZxMsagSipCapSp100Rel_Type()
)
zxMsagSipCapSp100Rel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSp100Rel.setStatus("current")


class _ZxMsagSipCapSpPath_Type(TruthValue):
    """Custom type zxMsagSipCapSpPath based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapSpPath_Type.__name__ = "TruthValue"
_ZxMsagSipCapSpPath_Object = MibTableColumn
zxMsagSipCapSpPath = _ZxMsagSipCapSpPath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 6),
    _ZxMsagSipCapSpPath_Type()
)
zxMsagSipCapSpPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSpPath.setStatus("current")


class _ZxMsagSipCapSpReplaces_Type(TruthValue):
    """Custom type zxMsagSipCapSpReplaces based on TruthValue"""
    defaultValue = 1


_ZxMsagSipCapSpReplaces_Type.__name__ = "TruthValue"
_ZxMsagSipCapSpReplaces_Object = MibTableColumn
zxMsagSipCapSpReplaces = _ZxMsagSipCapSpReplaces_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 7),
    _ZxMsagSipCapSpReplaces_Type()
)
zxMsagSipCapSpReplaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSpReplaces.setStatus("current")


class _ZxMsagSipCapSpTimer_Type(TruthValue):
    """Custom type zxMsagSipCapSpTimer based on TruthValue"""
    defaultValue = 1


_ZxMsagSipCapSpTimer_Type.__name__ = "TruthValue"
_ZxMsagSipCapSpTimer_Object = MibTableColumn
zxMsagSipCapSpTimer = _ZxMsagSipCapSpTimer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 8),
    _ZxMsagSipCapSpTimer_Type()
)
zxMsagSipCapSpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSpTimer.setStatus("current")


class _ZxMsagSipCapAudioCodePri1_Type(Integer32):
    """Custom type zxMsagSipCapAudioCodePri1 based on Integer32"""
    defaultValue = 1

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("g722", 3),
          ("g723", 4),
          ("g726", 5),
          ("g728", 6),
          ("g729", 7),
          ("unconfig", 255))
    )


_ZxMsagSipCapAudioCodePri1_Type.__name__ = "Integer32"
_ZxMsagSipCapAudioCodePri1_Object = MibTableColumn
zxMsagSipCapAudioCodePri1 = _ZxMsagSipCapAudioCodePri1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 9),
    _ZxMsagSipCapAudioCodePri1_Type()
)
zxMsagSipCapAudioCodePri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapAudioCodePri1.setStatus("current")


class _ZxMsagSipCapAudioCodePri2_Type(Integer32):
    """Custom type zxMsagSipCapAudioCodePri2 based on Integer32"""
    defaultValue = 2

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("g722", 3),
          ("g723", 4),
          ("g726", 5),
          ("g728", 6),
          ("g729", 7),
          ("unconfig", 255))
    )


_ZxMsagSipCapAudioCodePri2_Type.__name__ = "Integer32"
_ZxMsagSipCapAudioCodePri2_Object = MibTableColumn
zxMsagSipCapAudioCodePri2 = _ZxMsagSipCapAudioCodePri2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 10),
    _ZxMsagSipCapAudioCodePri2_Type()
)
zxMsagSipCapAudioCodePri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapAudioCodePri2.setStatus("current")


class _ZxMsagSipCapAudioCodePri3_Type(Integer32):
    """Custom type zxMsagSipCapAudioCodePri3 based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("g722", 3),
          ("g723", 4),
          ("g726", 5),
          ("g728", 6),
          ("g729", 7),
          ("unconfig", 255))
    )


_ZxMsagSipCapAudioCodePri3_Type.__name__ = "Integer32"
_ZxMsagSipCapAudioCodePri3_Object = MibTableColumn
zxMsagSipCapAudioCodePri3 = _ZxMsagSipCapAudioCodePri3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 11),
    _ZxMsagSipCapAudioCodePri3_Type()
)
zxMsagSipCapAudioCodePri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapAudioCodePri3.setStatus("current")


class _ZxMsagSipCapAudioCodePri4_Type(Integer32):
    """Custom type zxMsagSipCapAudioCodePri4 based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("g722", 3),
          ("g723", 4),
          ("g726", 5),
          ("g728", 6),
          ("g729", 7),
          ("unconfig", 255))
    )


_ZxMsagSipCapAudioCodePri4_Type.__name__ = "Integer32"
_ZxMsagSipCapAudioCodePri4_Object = MibTableColumn
zxMsagSipCapAudioCodePri4 = _ZxMsagSipCapAudioCodePri4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 12),
    _ZxMsagSipCapAudioCodePri4_Type()
)
zxMsagSipCapAudioCodePri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapAudioCodePri4.setStatus("current")


class _ZxMsagSipCapAudioCodePri5_Type(Integer32):
    """Custom type zxMsagSipCapAudioCodePri5 based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("g722", 3),
          ("g723", 4),
          ("g726", 5),
          ("g728", 6),
          ("g729", 7),
          ("unconfig", 255))
    )


_ZxMsagSipCapAudioCodePri5_Type.__name__ = "Integer32"
_ZxMsagSipCapAudioCodePri5_Object = MibTableColumn
zxMsagSipCapAudioCodePri5 = _ZxMsagSipCapAudioCodePri5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 13),
    _ZxMsagSipCapAudioCodePri5_Type()
)
zxMsagSipCapAudioCodePri5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapAudioCodePri5.setStatus("current")


class _ZxMsagSipCapAudioCodePri6_Type(Integer32):
    """Custom type zxMsagSipCapAudioCodePri6 based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("g722", 3),
          ("g723", 4),
          ("g726", 5),
          ("g728", 6),
          ("g729", 7),
          ("unconfig", 255))
    )


_ZxMsagSipCapAudioCodePri6_Type.__name__ = "Integer32"
_ZxMsagSipCapAudioCodePri6_Object = MibTableColumn
zxMsagSipCapAudioCodePri6 = _ZxMsagSipCapAudioCodePri6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 14),
    _ZxMsagSipCapAudioCodePri6_Type()
)
zxMsagSipCapAudioCodePri6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapAudioCodePri6.setStatus("current")


class _ZxMsagSipCapAudioCodePri7_Type(Integer32):
    """Custom type zxMsagSipCapAudioCodePri7 based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("g722", 3),
          ("g723", 4),
          ("g726", 5),
          ("g728", 6),
          ("g729", 7),
          ("unconfig", 255))
    )


_ZxMsagSipCapAudioCodePri7_Type.__name__ = "Integer32"
_ZxMsagSipCapAudioCodePri7_Object = MibTableColumn
zxMsagSipCapAudioCodePri7 = _ZxMsagSipCapAudioCodePri7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 15),
    _ZxMsagSipCapAudioCodePri7_Type()
)
zxMsagSipCapAudioCodePri7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapAudioCodePri7.setStatus("current")


class _ZxMsagSipCapDtmfRelayPri1_Type(Integer32):
    """Custom type zxMsagSipCapDtmfRelayPri1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("redunt2833", 1),
          ("noRedunt2833", 2),
          ("unconfig", 255))
    )


_ZxMsagSipCapDtmfRelayPri1_Type.__name__ = "Integer32"
_ZxMsagSipCapDtmfRelayPri1_Object = MibTableColumn
zxMsagSipCapDtmfRelayPri1 = _ZxMsagSipCapDtmfRelayPri1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 16),
    _ZxMsagSipCapDtmfRelayPri1_Type()
)
zxMsagSipCapDtmfRelayPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapDtmfRelayPri1.setStatus("current")


class _ZxMsagSipCapDtmfRelayPri2_Type(Integer32):
    """Custom type zxMsagSipCapDtmfRelayPri2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("redunt2833", 1),
          ("noRedunt2833", 2),
          ("unconfig", 255))
    )


_ZxMsagSipCapDtmfRelayPri2_Type.__name__ = "Integer32"
_ZxMsagSipCapDtmfRelayPri2_Object = MibTableColumn
zxMsagSipCapDtmfRelayPri2 = _ZxMsagSipCapDtmfRelayPri2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 17),
    _ZxMsagSipCapDtmfRelayPri2_Type()
)
zxMsagSipCapDtmfRelayPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapDtmfRelayPri2.setStatus("current")


class _ZxMsagSipCapFaxPri1_Type(Integer32):
    """Custom type zxMsagSipCapFaxPri1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("t30", 1),
          ("t38", 2),
          ("unconfig", 255))
    )


_ZxMsagSipCapFaxPri1_Type.__name__ = "Integer32"
_ZxMsagSipCapFaxPri1_Object = MibTableColumn
zxMsagSipCapFaxPri1 = _ZxMsagSipCapFaxPri1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 18),
    _ZxMsagSipCapFaxPri1_Type()
)
zxMsagSipCapFaxPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapFaxPri1.setStatus("current")


class _ZxMsagSipCapFaxPri2_Type(Integer32):
    """Custom type zxMsagSipCapFaxPri2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("t30", 1),
          ("t38", 2),
          ("unconfig", 255))
    )


_ZxMsagSipCapFaxPri2_Type.__name__ = "Integer32"
_ZxMsagSipCapFaxPri2_Object = MibTableColumn
zxMsagSipCapFaxPri2 = _ZxMsagSipCapFaxPri2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 19),
    _ZxMsagSipCapFaxPri2_Type()
)
zxMsagSipCapFaxPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapFaxPri2.setStatus("current")


class _ZxMsagSipCapSpFaxModem_Type(TruthValue):
    """Custom type zxMsagSipCapSpFaxModem based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapSpFaxModem_Type.__name__ = "TruthValue"
_ZxMsagSipCapSpFaxModem_Object = MibTableColumn
zxMsagSipCapSpFaxModem = _ZxMsagSipCapSpFaxModem_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 20),
    _ZxMsagSipCapSpFaxModem_Type()
)
zxMsagSipCapSpFaxModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSpFaxModem.setStatus("current")


class _ZxMsagSipCapSessionMaxExpire_Type(Integer32):
    """Custom type zxMsagSipCapSessionMaxExpire based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxMsagSipCapSessionMaxExpire_Type.__name__ = "Integer32"
_ZxMsagSipCapSessionMaxExpire_Object = MibTableColumn
zxMsagSipCapSessionMaxExpire = _ZxMsagSipCapSessionMaxExpire_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 21),
    _ZxMsagSipCapSessionMaxExpire_Type()
)
zxMsagSipCapSessionMaxExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSessionMaxExpire.setStatus("current")


class _ZxMsagSipCapSessionMinExpire_Type(Integer32):
    """Custom type zxMsagSipCapSessionMinExpire based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxMsagSipCapSessionMinExpire_Type.__name__ = "Integer32"
_ZxMsagSipCapSessionMinExpire_Object = MibTableColumn
zxMsagSipCapSessionMinExpire = _ZxMsagSipCapSessionMinExpire_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 22),
    _ZxMsagSipCapSessionMinExpire_Type()
)
zxMsagSipCapSessionMinExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSessionMinExpire.setStatus("current")


class _ZxMsagSipCapSessionRefresher_Type(Integer32):
    """Custom type zxMsagSipCapSessionRefresher based on Integer32"""
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
          ("remote", 2))
    )


_ZxMsagSipCapSessionRefresher_Type.__name__ = "Integer32"
_ZxMsagSipCapSessionRefresher_Object = MibTableColumn
zxMsagSipCapSessionRefresher = _ZxMsagSipCapSessionRefresher_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 23),
    _ZxMsagSipCapSessionRefresher_Type()
)
zxMsagSipCapSessionRefresher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSessionRefresher.setStatus("current")


class _ZxMsagSipCapDisplayFrom_Type(Integer32):
    """Custom type zxMsagSipCapDisplayFrom based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("from", 1),
          ("pai", 2))
    )


_ZxMsagSipCapDisplayFrom_Type.__name__ = "Integer32"
_ZxMsagSipCapDisplayFrom_Object = MibTableColumn
zxMsagSipCapDisplayFrom = _ZxMsagSipCapDisplayFrom_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 24),
    _ZxMsagSipCapDisplayFrom_Type()
)
zxMsagSipCapDisplayFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapDisplayFrom.setStatus("current")


class _ZxMsagSipCapRegisterExpire_Type(Integer32):
    """Custom type zxMsagSipCapRegisterExpire based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxMsagSipCapRegisterExpire_Type.__name__ = "Integer32"
_ZxMsagSipCapRegisterExpire_Object = MibTableColumn
zxMsagSipCapRegisterExpire = _ZxMsagSipCapRegisterExpire_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 25),
    _ZxMsagSipCapRegisterExpire_Type()
)
zxMsagSipCapRegisterExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapRegisterExpire.setStatus("current")


class _ZxMsagSipCapReqMsgAuth_Type(TruthValue):
    """Custom type zxMsagSipCapReqMsgAuth based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapReqMsgAuth_Type.__name__ = "TruthValue"
_ZxMsagSipCapReqMsgAuth_Object = MibTableColumn
zxMsagSipCapReqMsgAuth = _ZxMsagSipCapReqMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 26),
    _ZxMsagSipCapReqMsgAuth_Type()
)
zxMsagSipCapReqMsgAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapReqMsgAuth.setStatus("current")


class _ZxMsagSipCapPPreService_Type(TruthValue):
    """Custom type zxMsagSipCapPPreService based on TruthValue"""
    defaultValue = 1


_ZxMsagSipCapPPreService_Type.__name__ = "TruthValue"
_ZxMsagSipCapPPreService_Object = MibTableColumn
zxMsagSipCapPPreService = _ZxMsagSipCapPPreService_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 27),
    _ZxMsagSipCapPPreService_Type()
)
zxMsagSipCapPPreService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapPPreService.setStatus("current")


class _ZxMsagSipCapAuthWithDomain_Type(TruthValue):
    """Custom type zxMsagSipCapAuthWithDomain based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapAuthWithDomain_Type.__name__ = "TruthValue"
_ZxMsagSipCapAuthWithDomain_Object = MibTableColumn
zxMsagSipCapAuthWithDomain = _ZxMsagSipCapAuthWithDomain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 28),
    _ZxMsagSipCapAuthWithDomain_Type()
)
zxMsagSipCapAuthWithDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapAuthWithDomain.setStatus("current")


class _ZxMsagSipCapPackageInterval_Type(Integer32):
    """Custom type zxMsagSipCapPackageInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 50),
    )


_ZxMsagSipCapPackageInterval_Type.__name__ = "Integer32"
_ZxMsagSipCapPackageInterval_Object = MibTableColumn
zxMsagSipCapPackageInterval = _ZxMsagSipCapPackageInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 29),
    _ZxMsagSipCapPackageInterval_Type()
)
zxMsagSipCapPackageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapPackageInterval.setStatus("current")


class _ZxMsagSipCapSessionLimit_Type(TruthValue):
    """Custom type zxMsagSipCapSessionLimit based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapSessionLimit_Type.__name__ = "TruthValue"
_ZxMsagSipCapSessionLimit_Object = MibTableColumn
zxMsagSipCapSessionLimit = _ZxMsagSipCapSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 30),
    _ZxMsagSipCapSessionLimit_Type()
)
zxMsagSipCapSessionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSessionLimit.setStatus("current")


class _ZxMsagSipCapUserParam_Type(Integer32):
    """Custom type zxMsagSipCapUserParam based on Integer32"""
    defaultValue = 2

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
        *(("null", 1),
          ("phone", 2),
          ("ip", 3),
          ("other", 4))
    )


_ZxMsagSipCapUserParam_Type.__name__ = "Integer32"
_ZxMsagSipCapUserParam_Object = MibTableColumn
zxMsagSipCapUserParam = _ZxMsagSipCapUserParam_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 31),
    _ZxMsagSipCapUserParam_Type()
)
zxMsagSipCapUserParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapUserParam.setStatus("current")


class _ZxMsagSipCapDtmfSendingType_Type(Integer32):
    """Custom type zxMsagSipCapDtmfSendingType based on Integer32"""
    defaultValue = 1

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
        *(("rtp", 1),
          ("sipinfo", 2),
          ("broadSoftInfo", 3),
          ("ibx1000Info", 4))
    )


_ZxMsagSipCapDtmfSendingType_Type.__name__ = "Integer32"
_ZxMsagSipCapDtmfSendingType_Object = MibTableColumn
zxMsagSipCapDtmfSendingType = _ZxMsagSipCapDtmfSendingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 32),
    _ZxMsagSipCapDtmfSendingType_Type()
)
zxMsagSipCapDtmfSendingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapDtmfSendingType.setStatus("current")


class _ZxMsagSipCapEarlyMedia_Type(TruthValue):
    """Custom type zxMsagSipCapEarlyMedia based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapEarlyMedia_Type.__name__ = "TruthValue"
_ZxMsagSipCapEarlyMedia_Object = MibTableColumn
zxMsagSipCapEarlyMedia = _ZxMsagSipCapEarlyMedia_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 33),
    _ZxMsagSipCapEarlyMedia_Type()
)
zxMsagSipCapEarlyMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapEarlyMedia.setStatus("current")


class _ZxMsagSipCapEchoCancel_Type(TruthValue):
    """Custom type zxMsagSipCapEchoCancel based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapEchoCancel_Type.__name__ = "TruthValue"
_ZxMsagSipCapEchoCancel_Object = MibTableColumn
zxMsagSipCapEchoCancel = _ZxMsagSipCapEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 34),
    _ZxMsagSipCapEchoCancel_Type()
)
zxMsagSipCapEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapEchoCancel.setStatus("current")


class _ZxMsagSipCapHistoryInfo_Type(TruthValue):
    """Custom type zxMsagSipCapHistoryInfo based on TruthValue"""
    defaultValue = 2


_ZxMsagSipCapHistoryInfo_Type.__name__ = "TruthValue"
_ZxMsagSipCapHistoryInfo_Object = MibTableColumn
zxMsagSipCapHistoryInfo = _ZxMsagSipCapHistoryInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 35),
    _ZxMsagSipCapHistoryInfo_Type()
)
zxMsagSipCapHistoryInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapHistoryInfo.setStatus("current")


class _ZxMsagSipCapThreePartySvrCode_Type(DisplayString):
    """Custom type zxMsagSipCapThreePartySvrCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxMsagSipCapThreePartySvrCode_Type.__name__ = "DisplayString"
_ZxMsagSipCapThreePartySvrCode_Object = MibTableColumn
zxMsagSipCapThreePartySvrCode = _ZxMsagSipCapThreePartySvrCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 36),
    _ZxMsagSipCapThreePartySvrCode_Type()
)
zxMsagSipCapThreePartySvrCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapThreePartySvrCode.setStatus("current")


class _ZxMsagSipCapUserRegisterType_Type(Integer32):
    """Custom type zxMsagSipCapUserRegisterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("explicit", 1),
          ("implicit", 2))
    )


_ZxMsagSipCapUserRegisterType_Type.__name__ = "Integer32"
_ZxMsagSipCapUserRegisterType_Object = MibTableColumn
zxMsagSipCapUserRegisterType = _ZxMsagSipCapUserRegisterType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 37),
    _ZxMsagSipCapUserRegisterType_Type()
)
zxMsagSipCapUserRegisterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapUserRegisterType.setStatus("current")


class _ZxMsagSipCapHeartbeatEnable_Type(Integer32):
    """Custom type zxMsagSipCapHeartbeatEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ZxMsagSipCapHeartbeatEnable_Type.__name__ = "Integer32"
_ZxMsagSipCapHeartbeatEnable_Object = MibTableColumn
zxMsagSipCapHeartbeatEnable = _ZxMsagSipCapHeartbeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 51),
    _ZxMsagSipCapHeartbeatEnable_Type()
)
zxMsagSipCapHeartbeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapHeartbeatEnable.setStatus("current")


class _ZxMsagSipCapHeartbeatInterval_Type(Integer32):
    """Custom type zxMsagSipCapHeartbeatInterval based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxMsagSipCapHeartbeatInterval_Type.__name__ = "Integer32"
_ZxMsagSipCapHeartbeatInterval_Object = MibTableColumn
zxMsagSipCapHeartbeatInterval = _ZxMsagSipCapHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 52),
    _ZxMsagSipCapHeartbeatInterval_Type()
)
zxMsagSipCapHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapHeartbeatInterval.setStatus("current")


class _ZxMsagSipCapSelfswitch_Type(Integer32):
    """Custom type zxMsagSipCapSelfswitch based on Integer32"""
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


_ZxMsagSipCapSelfswitch_Type.__name__ = "Integer32"
_ZxMsagSipCapSelfswitch_Object = MibTableColumn
zxMsagSipCapSelfswitch = _ZxMsagSipCapSelfswitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 53),
    _ZxMsagSipCapSelfswitch_Type()
)
zxMsagSipCapSelfswitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapSelfswitch.setStatus("current")


class _ZxMsagSipCapCallProtection_Type(Integer32):
    """Custom type zxMsagSipCapCallProtection based on Integer32"""
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


_ZxMsagSipCapCallProtection_Type.__name__ = "Integer32"
_ZxMsagSipCapCallProtection_Object = MibTableColumn
zxMsagSipCapCallProtection = _ZxMsagSipCapCallProtection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 54),
    _ZxMsagSipCapCallProtection_Type()
)
zxMsagSipCapCallProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxMsagSipCapCallProtection.setStatus("current")


class _ZxAnSipCapVideoMediaNegotiation_Type(TruthValue):
    """Custom type zxAnSipCapVideoMediaNegotiation based on TruthValue"""
    defaultValue = 2


_ZxAnSipCapVideoMediaNegotiation_Type.__name__ = "TruthValue"
_ZxAnSipCapVideoMediaNegotiation_Object = MibTableColumn
zxAnSipCapVideoMediaNegotiation = _ZxAnSipCapVideoMediaNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 55),
    _ZxAnSipCapVideoMediaNegotiation_Type()
)
zxAnSipCapVideoMediaNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapVideoMediaNegotiation.setStatus("current")


class _ZxAnSipCapUserPhoneAppendEnable_Type(Integer32):
    """Custom type zxAnSipCapUserPhoneAppendEnable based on Integer32"""
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


_ZxAnSipCapUserPhoneAppendEnable_Type.__name__ = "Integer32"
_ZxAnSipCapUserPhoneAppendEnable_Object = MibTableColumn
zxAnSipCapUserPhoneAppendEnable = _ZxAnSipCapUserPhoneAppendEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 56),
    _ZxAnSipCapUserPhoneAppendEnable_Type()
)
zxAnSipCapUserPhoneAppendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapUserPhoneAppendEnable.setStatus("current")


class _ZxAnSipCapSendSubscribeMsgEnable_Type(Integer32):
    """Custom type zxAnSipCapSendSubscribeMsgEnable based on Integer32"""
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


_ZxAnSipCapSendSubscribeMsgEnable_Type.__name__ = "Integer32"
_ZxAnSipCapSendSubscribeMsgEnable_Object = MibTableColumn
zxAnSipCapSendSubscribeMsgEnable = _ZxAnSipCapSendSubscribeMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 57),
    _ZxAnSipCapSendSubscribeMsgEnable_Type()
)
zxAnSipCapSendSubscribeMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapSendSubscribeMsgEnable.setStatus("current")


class _ZxAnSipCapFaxCodePri1_Type(Integer32):
    """Custom type zxAnSipCapFaxCodePri1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("unconfig", 255))
    )


_ZxAnSipCapFaxCodePri1_Type.__name__ = "Integer32"
_ZxAnSipCapFaxCodePri1_Object = MibTableColumn
zxAnSipCapFaxCodePri1 = _ZxAnSipCapFaxCodePri1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 58),
    _ZxAnSipCapFaxCodePri1_Type()
)
zxAnSipCapFaxCodePri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapFaxCodePri1.setStatus("current")


class _ZxAnSipCapFaxCodePri2_Type(Integer32):
    """Custom type zxAnSipCapFaxCodePri2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("unconfig", 255))
    )


_ZxAnSipCapFaxCodePri2_Type.__name__ = "Integer32"
_ZxAnSipCapFaxCodePri2_Object = MibTableColumn
zxAnSipCapFaxCodePri2 = _ZxAnSipCapFaxCodePri2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 59),
    _ZxAnSipCapFaxCodePri2_Type()
)
zxAnSipCapFaxCodePri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapFaxCodePri2.setStatus("current")


class _ZxAnSipCapFaxCodePri3_Type(Integer32):
    """Custom type zxAnSipCapFaxCodePri3 based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("unconfig", 255))
    )


_ZxAnSipCapFaxCodePri3_Type.__name__ = "Integer32"
_ZxAnSipCapFaxCodePri3_Object = MibTableColumn
zxAnSipCapFaxCodePri3 = _ZxAnSipCapFaxCodePri3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 60),
    _ZxAnSipCapFaxCodePri3_Type()
)
zxAnSipCapFaxCodePri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapFaxCodePri3.setStatus("current")


class _ZxAnSipCapFaxCodePri4_Type(Integer32):
    """Custom type zxAnSipCapFaxCodePri4 based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcma", 1),
          ("pcmu", 2),
          ("unconfig", 255))
    )


_ZxAnSipCapFaxCodePri4_Type.__name__ = "Integer32"
_ZxAnSipCapFaxCodePri4_Object = MibTableColumn
zxAnSipCapFaxCodePri4 = _ZxAnSipCapFaxCodePri4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 61),
    _ZxAnSipCapFaxCodePri4_Type()
)
zxAnSipCapFaxCodePri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapFaxCodePri4.setStatus("current")


class _ZxAnSipCapFaxPacketInterval_Type(Integer32):
    """Custom type zxAnSipCapFaxPacketInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 50),
    )


_ZxAnSipCapFaxPacketInterval_Type.__name__ = "Integer32"
_ZxAnSipCapFaxPacketInterval_Object = MibTableColumn
zxAnSipCapFaxPacketInterval = _ZxAnSipCapFaxPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 62),
    _ZxAnSipCapFaxPacketInterval_Type()
)
zxAnSipCapFaxPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapFaxPacketInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipCapFaxPacketInterval.setUnits("ms")


class _ZxAnSipCapAutoRefreshEnable_Type(Integer32):
    """Custom type zxAnSipCapAutoRefreshEnable based on Integer32"""
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


_ZxAnSipCapAutoRefreshEnable_Type.__name__ = "Integer32"
_ZxAnSipCapAutoRefreshEnable_Object = MibTableColumn
zxAnSipCapAutoRefreshEnable = _ZxAnSipCapAutoRefreshEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 63),
    _ZxAnSipCapAutoRefreshEnable_Type()
)
zxAnSipCapAutoRefreshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapAutoRefreshEnable.setStatus("current")


class _ZxAnSipCapImsHotlineValidTime_Type(Integer32):
    """Custom type zxAnSipCapImsHotlineValidTime based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 900000),
    )


_ZxAnSipCapImsHotlineValidTime_Type.__name__ = "Integer32"
_ZxAnSipCapImsHotlineValidTime_Object = MibTableColumn
zxAnSipCapImsHotlineValidTime = _ZxAnSipCapImsHotlineValidTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 64),
    _ZxAnSipCapImsHotlineValidTime_Type()
)
zxAnSipCapImsHotlineValidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapImsHotlineValidTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipCapImsHotlineValidTime.setUnits("seconds")


class _ZxAnSipCapDnsRequestInterval_Type(Integer32):
    """Custom type zxAnSipCapDnsRequestInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_ZxAnSipCapDnsRequestInterval_Type.__name__ = "Integer32"
_ZxAnSipCapDnsRequestInterval_Object = MibTableColumn
zxAnSipCapDnsRequestInterval = _ZxAnSipCapDnsRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 65),
    _ZxAnSipCapDnsRequestInterval_Type()
)
zxAnSipCapDnsRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapDnsRequestInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipCapDnsRequestInterval.setUnits("seconds")


class _ZxAnSipCapCallWaitInvite18xRsp_Type(Integer32):
    """Custom type zxAnSipCapCallWaitInvite18xRsp based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 182),
    )


_ZxAnSipCapCallWaitInvite18xRsp_Type.__name__ = "Integer32"
_ZxAnSipCapCallWaitInvite18xRsp_Object = MibTableColumn
zxAnSipCapCallWaitInvite18xRsp = _ZxAnSipCapCallWaitInvite18xRsp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 66),
    _ZxAnSipCapCallWaitInvite18xRsp_Type()
)
zxAnSipCapCallWaitInvite18xRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapCallWaitInvite18xRsp.setStatus("current")


class _ZxAnSipCapSubscribeUaProfileEn_Type(Integer32):
    """Custom type zxAnSipCapSubscribeUaProfileEn based on Integer32"""
    defaultValue = 1

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


_ZxAnSipCapSubscribeUaProfileEn_Type.__name__ = "Integer32"
_ZxAnSipCapSubscribeUaProfileEn_Object = MibTableColumn
zxAnSipCapSubscribeUaProfileEn = _ZxAnSipCapSubscribeUaProfileEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 67),
    _ZxAnSipCapSubscribeUaProfileEn_Type()
)
zxAnSipCapSubscribeUaProfileEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapSubscribeUaProfileEn.setStatus("current")


class _ZxAnSipCapSubscribeMsgSummaryEn_Type(Integer32):
    """Custom type zxAnSipCapSubscribeMsgSummaryEn based on Integer32"""
    defaultValue = 1

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


_ZxAnSipCapSubscribeMsgSummaryEn_Type.__name__ = "Integer32"
_ZxAnSipCapSubscribeMsgSummaryEn_Object = MibTableColumn
zxAnSipCapSubscribeMsgSummaryEn = _ZxAnSipCapSubscribeMsgSummaryEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 68),
    _ZxAnSipCapSubscribeMsgSummaryEn_Type()
)
zxAnSipCapSubscribeMsgSummaryEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapSubscribeMsgSummaryEn.setStatus("current")


class _ZxAnSipCapCallerControlEnable_Type(Integer32):
    """Custom type zxAnSipCapCallerControlEnable based on Integer32"""
    defaultValue = 1

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


_ZxAnSipCapCallerControlEnable_Type.__name__ = "Integer32"
_ZxAnSipCapCallerControlEnable_Object = MibTableColumn
zxAnSipCapCallerControlEnable = _ZxAnSipCapCallerControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 69),
    _ZxAnSipCapCallerControlEnable_Type()
)
zxAnSipCapCallerControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapCallerControlEnable.setStatus("current")


class _ZxAnSipCapNoDialSendInviteEnable_Type(Integer32):
    """Custom type zxAnSipCapNoDialSendInviteEnable based on Integer32"""
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


_ZxAnSipCapNoDialSendInviteEnable_Type.__name__ = "Integer32"
_ZxAnSipCapNoDialSendInviteEnable_Object = MibTableColumn
zxAnSipCapNoDialSendInviteEnable = _ZxAnSipCapNoDialSendInviteEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 70),
    _ZxAnSipCapNoDialSendInviteEnable_Type()
)
zxAnSipCapNoDialSendInviteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapNoDialSendInviteEnable.setStatus("current")


class _ZxAnSipCapProxySvrAutoDrEnable_Type(Integer32):
    """Custom type zxAnSipCapProxySvrAutoDrEnable based on Integer32"""
    defaultValue = 1

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


_ZxAnSipCapProxySvrAutoDrEnable_Type.__name__ = "Integer32"
_ZxAnSipCapProxySvrAutoDrEnable_Object = MibTableColumn
zxAnSipCapProxySvrAutoDrEnable = _ZxAnSipCapProxySvrAutoDrEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 71),
    _ZxAnSipCapProxySvrAutoDrEnable_Type()
)
zxAnSipCapProxySvrAutoDrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapProxySvrAutoDrEnable.setStatus("current")


class _ZxAnSipCapProxySvrDrMode_Type(Integer32):
    """Custom type zxAnSipCapProxySvrDrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primaryFirst", 1),
          ("roundRobin", 2))
    )


_ZxAnSipCapProxySvrDrMode_Type.__name__ = "Integer32"
_ZxAnSipCapProxySvrDrMode_Object = MibTableColumn
zxAnSipCapProxySvrDrMode = _ZxAnSipCapProxySvrDrMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 5, 1, 72),
    _ZxAnSipCapProxySvrDrMode_Type()
)
zxAnSipCapProxySvrDrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipCapProxySvrDrMode.setStatus("current")
_ZxAnSipGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSipGlobalObjects = _ZxAnSipGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 6)
)


class _ZxAnSipMgmtCapabilities_Type(Bits):
    """Custom type zxAnSipMgmtCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("group", 0),
          ("sipUaIp", 1),
          ("proxySvrDomainName", 2),
          ("nbPlatform", 3),
          ("userAdminStatus", 4),
          ("userSessionLimit", 5))
    )

_ZxAnSipMgmtCapabilities_Type.__name__ = "Bits"
_ZxAnSipMgmtCapabilities_Object = MibScalar
zxAnSipMgmtCapabilities = _ZxAnSipMgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 6, 1),
    _ZxAnSipMgmtCapabilities_Type()
)
zxAnSipMgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipMgmtCapabilities.setStatus("current")


class _ZxAnSipProcessReboot_Type(Integer32):
    """Custom type zxAnSipProcessReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_ZxAnSipProcessReboot_Type.__name__ = "Integer32"
_ZxAnSipProcessReboot_Object = MibScalar
zxAnSipProcessReboot = _ZxAnSipProcessReboot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 6, 2),
    _ZxAnSipProcessReboot_Type()
)
zxAnSipProcessReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipProcessReboot.setStatus("current")
_ZxAnSipProxyServerTable_Object = MibTable
zxAnSipProxyServerTable = _ZxAnSipProxyServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 7)
)
if mibBuilder.loadTexts:
    zxAnSipProxyServerTable.setStatus("current")
_ZxAnSipProxyServerEntry_Object = MibTableRow
zxAnSipProxyServerEntry = _ZxAnSipProxyServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 7, 1)
)
zxAnSipProxyServerEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxAnSipProxySvrId"),
)
if mibBuilder.loadTexts:
    zxAnSipProxyServerEntry.setStatus("current")


class _ZxAnSipProxySvrId_Type(Integer32):
    """Custom type zxAnSipProxySvrId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnSipProxySvrId_Type.__name__ = "Integer32"
_ZxAnSipProxySvrId_Object = MibTableColumn
zxAnSipProxySvrId = _ZxAnSipProxySvrId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 7, 1, 1),
    _ZxAnSipProxySvrId_Type()
)
zxAnSipProxySvrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipProxySvrId.setStatus("current")
_ZxAnSipProxySvrIp_Type = IpAddress
_ZxAnSipProxySvrIp_Object = MibTableColumn
zxAnSipProxySvrIp = _ZxAnSipProxySvrIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 7, 1, 2),
    _ZxAnSipProxySvrIp_Type()
)
zxAnSipProxySvrIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipProxySvrIp.setStatus("current")


class _ZxAnSipProxySvrPort_Type(Integer32):
    """Custom type zxAnSipProxySvrPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnSipProxySvrPort_Type.__name__ = "Integer32"
_ZxAnSipProxySvrPort_Object = MibTableColumn
zxAnSipProxySvrPort = _ZxAnSipProxySvrPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 7, 1, 3),
    _ZxAnSipProxySvrPort_Type()
)
zxAnSipProxySvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipProxySvrPort.setStatus("current")


class _ZxAnSipProxySvrNamingType_Type(Integer32):
    """Custom type zxAnSipProxySvrNamingType based on Integer32"""
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
        *(("useIp", 1),
          ("useDomainName", 2),
          ("dhcpOption120", 3))
    )


_ZxAnSipProxySvrNamingType_Type.__name__ = "Integer32"
_ZxAnSipProxySvrNamingType_Object = MibTableColumn
zxAnSipProxySvrNamingType = _ZxAnSipProxySvrNamingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 7, 1, 4),
    _ZxAnSipProxySvrNamingType_Type()
)
zxAnSipProxySvrNamingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipProxySvrNamingType.setStatus("current")


class _ZxAnSipProxySvrDomainName_Type(DisplayString):
    """Custom type zxAnSipProxySvrDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnSipProxySvrDomainName_Type.__name__ = "DisplayString"
_ZxAnSipProxySvrDomainName_Object = MibTableColumn
zxAnSipProxySvrDomainName = _ZxAnSipProxySvrDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 7, 1, 5),
    _ZxAnSipProxySvrDomainName_Type()
)
zxAnSipProxySvrDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipProxySvrDomainName.setStatus("current")
_ZxAnSipProxySvrRowStatus_Type = RowStatus
_ZxAnSipProxySvrRowStatus_Object = MibTableColumn
zxAnSipProxySvrRowStatus = _ZxAnSipProxySvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 7, 1, 20),
    _ZxAnSipProxySvrRowStatus_Type()
)
zxAnSipProxySvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipProxySvrRowStatus.setStatus("current")
_ZxAnSipUserAgentTable_Object = MibTable
zxAnSipUserAgentTable = _ZxAnSipUserAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8)
)
if mibBuilder.loadTexts:
    zxAnSipUserAgentTable.setStatus("current")
_ZxAnSipUserAgentEntry_Object = MibTableRow
zxAnSipUserAgentEntry = _ZxAnSipUserAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1)
)
zxAnSipUserAgentEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxAnSipUaId"),
)
if mibBuilder.loadTexts:
    zxAnSipUserAgentEntry.setStatus("current")


class _ZxAnSipUaId_Type(Integer32):
    """Custom type zxAnSipUaId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxAnSipUaId_Type.__name__ = "Integer32"
_ZxAnSipUaId_Object = MibTableColumn
zxAnSipUaId = _ZxAnSipUaId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 1),
    _ZxAnSipUaId_Type()
)
zxAnSipUaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipUaId.setStatus("current")


class _ZxAnSipUaPort_Type(Integer32):
    """Custom type zxAnSipUaPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnSipUaPort_Type.__name__ = "Integer32"
_ZxAnSipUaPort_Object = MibTableColumn
zxAnSipUaPort = _ZxAnSipUaPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 2),
    _ZxAnSipUaPort_Type()
)
zxAnSipUaPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaPort.setStatus("current")


class _ZxAnSipUaDomainName_Type(DisplayString):
    """Custom type zxAnSipUaDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnSipUaDomainName_Type.__name__ = "DisplayString"
_ZxAnSipUaDomainName_Object = MibTableColumn
zxAnSipUaDomainName = _ZxAnSipUaDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 3),
    _ZxAnSipUaDomainName_Type()
)
zxAnSipUaDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaDomainName.setStatus("current")


class _ZxAnSipUaProxySvrId1_Type(Integer32):
    """Custom type zxAnSipUaProxySvrId1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnSipUaProxySvrId1_Type.__name__ = "Integer32"
_ZxAnSipUaProxySvrId1_Object = MibTableColumn
zxAnSipUaProxySvrId1 = _ZxAnSipUaProxySvrId1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 4),
    _ZxAnSipUaProxySvrId1_Type()
)
zxAnSipUaProxySvrId1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaProxySvrId1.setStatus("current")


class _ZxAnSipUaProxySvrId2_Type(Integer32):
    """Custom type zxAnSipUaProxySvrId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnSipUaProxySvrId2_Type.__name__ = "Integer32"
_ZxAnSipUaProxySvrId2_Object = MibTableColumn
zxAnSipUaProxySvrId2 = _ZxAnSipUaProxySvrId2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 5),
    _ZxAnSipUaProxySvrId2_Type()
)
zxAnSipUaProxySvrId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaProxySvrId2.setStatus("current")


class _ZxAnSipUaProxySvrId3_Type(Integer32):
    """Custom type zxAnSipUaProxySvrId3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnSipUaProxySvrId3_Type.__name__ = "Integer32"
_ZxAnSipUaProxySvrId3_Object = MibTableColumn
zxAnSipUaProxySvrId3 = _ZxAnSipUaProxySvrId3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 6),
    _ZxAnSipUaProxySvrId3_Type()
)
zxAnSipUaProxySvrId3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaProxySvrId3.setStatus("current")


class _ZxAnSipUaProxySvrId4_Type(Integer32):
    """Custom type zxAnSipUaProxySvrId4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnSipUaProxySvrId4_Type.__name__ = "Integer32"
_ZxAnSipUaProxySvrId4_Object = MibTableColumn
zxAnSipUaProxySvrId4 = _ZxAnSipUaProxySvrId4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 7),
    _ZxAnSipUaProxySvrId4_Type()
)
zxAnSipUaProxySvrId4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaProxySvrId4.setStatus("current")


class _ZxAnSipUaSelfswitch_Type(Integer32):
    """Custom type zxAnSipUaSelfswitch based on Integer32"""
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


_ZxAnSipUaSelfswitch_Type.__name__ = "Integer32"
_ZxAnSipUaSelfswitch_Object = MibTableColumn
zxAnSipUaSelfswitch = _ZxAnSipUaSelfswitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 8),
    _ZxAnSipUaSelfswitch_Type()
)
zxAnSipUaSelfswitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaSelfswitch.setStatus("current")


class _ZxAnSipUaCallProtection_Type(Integer32):
    """Custom type zxAnSipUaCallProtection based on Integer32"""
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


_ZxAnSipUaCallProtection_Type.__name__ = "Integer32"
_ZxAnSipUaCallProtection_Object = MibTableColumn
zxAnSipUaCallProtection = _ZxAnSipUaCallProtection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 9),
    _ZxAnSipUaCallProtection_Type()
)
zxAnSipUaCallProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaCallProtection.setStatus("current")
_ZxAnSipUaIpType_Type = InetAddressType
_ZxAnSipUaIpType_Object = MibTableColumn
zxAnSipUaIpType = _ZxAnSipUaIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 10),
    _ZxAnSipUaIpType_Type()
)
zxAnSipUaIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipUaIpType.setStatus("current")
_ZxAnSipUaIp_Type = InetAddress
_ZxAnSipUaIp_Object = MibTableColumn
zxAnSipUaIp = _ZxAnSipUaIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 11),
    _ZxAnSipUaIp_Type()
)
zxAnSipUaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipUaIp.setStatus("current")


class _ZxAnSipUaSwitchProxySvrId_Type(Integer32):
    """Custom type zxAnSipUaSwitchProxySvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnSipUaSwitchProxySvrId_Type.__name__ = "Integer32"
_ZxAnSipUaSwitchProxySvrId_Object = MibTableColumn
zxAnSipUaSwitchProxySvrId = _ZxAnSipUaSwitchProxySvrId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 12),
    _ZxAnSipUaSwitchProxySvrId_Type()
)
zxAnSipUaSwitchProxySvrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaSwitchProxySvrId.setStatus("current")


class _ZxAnSipUaCurrentProxySvrId_Type(Integer32):
    """Custom type zxAnSipUaCurrentProxySvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnSipUaCurrentProxySvrId_Type.__name__ = "Integer32"
_ZxAnSipUaCurrentProxySvrId_Object = MibTableColumn
zxAnSipUaCurrentProxySvrId = _ZxAnSipUaCurrentProxySvrId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 13),
    _ZxAnSipUaCurrentProxySvrId_Type()
)
zxAnSipUaCurrentProxySvrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipUaCurrentProxySvrId.setStatus("current")
_ZxAnSipUaRowStatus_Type = RowStatus
_ZxAnSipUaRowStatus_Object = MibTableColumn
zxAnSipUaRowStatus = _ZxAnSipUaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 8, 1, 50),
    _ZxAnSipUaRowStatus_Type()
)
zxAnSipUaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipUaRowStatus.setStatus("current")
_ZxAnSipGroupTable_Object = MibTable
zxAnSipGroupTable = _ZxAnSipGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20)
)
if mibBuilder.loadTexts:
    zxAnSipGroupTable.setStatus("current")
_ZxAnSipGroupEntry_Object = MibTableRow
zxAnSipGroupEntry = _ZxAnSipGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1)
)
zxAnSipGroupEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxAnSipGroupMgId"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipGroupId"),
)
if mibBuilder.loadTexts:
    zxAnSipGroupEntry.setStatus("current")


class _ZxAnSipGroupMgId_Type(Integer32):
    """Custom type zxAnSipGroupMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxAnSipGroupMgId_Type.__name__ = "Integer32"
_ZxAnSipGroupMgId_Object = MibTableColumn
zxAnSipGroupMgId = _ZxAnSipGroupMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 1),
    _ZxAnSipGroupMgId_Type()
)
zxAnSipGroupMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipGroupMgId.setStatus("current")


class _ZxAnSipGroupId_Type(Integer32):
    """Custom type zxAnSipGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ZxAnSipGroupId_Type.__name__ = "Integer32"
_ZxAnSipGroupId_Object = MibTableColumn
zxAnSipGroupId = _ZxAnSipGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 2),
    _ZxAnSipGroupId_Type()
)
zxAnSipGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipGroupId.setStatus("current")


class _ZxAnSipGroupName_Type(DisplayString):
    """Custom type zxAnSipGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnSipGroupName_Type.__name__ = "DisplayString"
_ZxAnSipGroupName_Object = MibTableColumn
zxAnSipGroupName = _ZxAnSipGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 3),
    _ZxAnSipGroupName_Type()
)
zxAnSipGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupName.setStatus("current")


class _ZxAnSipGroupType_Type(Integer32):
    """Custom type zxAnSipGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pstn", 1),
          ("isdnbri", 2),
          ("isdnpri", 3))
    )


_ZxAnSipGroupType_Type.__name__ = "Integer32"
_ZxAnSipGroupType_Object = MibTableColumn
zxAnSipGroupType = _ZxAnSipGroupType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 4),
    _ZxAnSipGroupType_Type()
)
zxAnSipGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupType.setStatus("current")


class _ZxAnSipGroupOperNum_Type(Integer32):
    """Custom type zxAnSipGroupOperNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ZxAnSipGroupOperNum_Type.__name__ = "Integer32"
_ZxAnSipGroupOperNum_Object = MibTableColumn
zxAnSipGroupOperNum = _ZxAnSipGroupOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 5),
    _ZxAnSipGroupOperNum_Type()
)
zxAnSipGroupOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupOperNum.setStatus("current")


class _ZxAnSipGroupPhoneNumber_Type(DisplayString):
    """Custom type zxAnSipGroupPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSipGroupPhoneNumber_Type.__name__ = "DisplayString"
_ZxAnSipGroupPhoneNumber_Object = MibTableColumn
zxAnSipGroupPhoneNumber = _ZxAnSipGroupPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 6),
    _ZxAnSipGroupPhoneNumber_Type()
)
zxAnSipGroupPhoneNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupPhoneNumber.setStatus("current")


class _ZxAnSipGroupUserId_Type(DisplayString):
    """Custom type zxAnSipGroupUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSipGroupUserId_Type.__name__ = "DisplayString"
_ZxAnSipGroupUserId_Object = MibTableColumn
zxAnSipGroupUserId = _ZxAnSipGroupUserId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 7),
    _ZxAnSipGroupUserId_Type()
)
zxAnSipGroupUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupUserId.setStatus("current")


class _ZxAnSipGroupAuthUserName_Type(DisplayString):
    """Custom type zxAnSipGroupAuthUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSipGroupAuthUserName_Type.__name__ = "DisplayString"
_ZxAnSipGroupAuthUserName_Object = MibTableColumn
zxAnSipGroupAuthUserName = _ZxAnSipGroupAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 8),
    _ZxAnSipGroupAuthUserName_Type()
)
zxAnSipGroupAuthUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupAuthUserName.setStatus("current")


class _ZxAnSipGroupOperType_Type(Integer32):
    """Custom type zxAnSipGroupOperType based on Integer32"""
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
        *(("username", 1),
          ("userid", 2),
          ("all", 3),
          ("none", 4))
    )


_ZxAnSipGroupOperType_Type.__name__ = "Integer32"
_ZxAnSipGroupOperType_Object = MibTableColumn
zxAnSipGroupOperType = _ZxAnSipGroupOperType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 9),
    _ZxAnSipGroupOperType_Type()
)
zxAnSipGroupOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupOperType.setStatus("current")


class _ZxAnSipGroupUserType_Type(Integer32):
    """Custom type zxAnSipGroupUserType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type2", 2),
          ("type3", 3))
    )


_ZxAnSipGroupUserType_Type.__name__ = "Integer32"
_ZxAnSipGroupUserType_Object = MibTableColumn
zxAnSipGroupUserType = _ZxAnSipGroupUserType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 10),
    _ZxAnSipGroupUserType_Type()
)
zxAnSipGroupUserType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupUserType.setStatus("current")


class _ZxAnSipGroupUserStartNumber_Type(Integer32):
    """Custom type zxAnSipGroupUserStartNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnSipGroupUserStartNumber_Type.__name__ = "Integer32"
_ZxAnSipGroupUserStartNumber_Object = MibTableColumn
zxAnSipGroupUserStartNumber = _ZxAnSipGroupUserStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 11),
    _ZxAnSipGroupUserStartNumber_Type()
)
zxAnSipGroupUserStartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupUserStartNumber.setStatus("current")


class _ZxAnSipGroupUserDigitLen_Type(Integer32):
    """Custom type zxAnSipGroupUserDigitLen based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ZxAnSipGroupUserDigitLen_Type.__name__ = "Integer32"
_ZxAnSipGroupUserDigitLen_Object = MibTableColumn
zxAnSipGroupUserDigitLen = _ZxAnSipGroupUserDigitLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 12),
    _ZxAnSipGroupUserDigitLen_Type()
)
zxAnSipGroupUserDigitLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupUserDigitLen.setStatus("current")


class _ZxAnSipGroupPassword_Type(DisplayString):
    """Custom type zxAnSipGroupPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnSipGroupPassword_Type.__name__ = "DisplayString"
_ZxAnSipGroupPassword_Object = MibTableColumn
zxAnSipGroupPassword = _ZxAnSipGroupPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 13),
    _ZxAnSipGroupPassword_Type()
)
zxAnSipGroupPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupPassword.setStatus("current")
_ZxAnSipGroupRowStatus_Type = RowStatus
_ZxAnSipGroupRowStatus_Object = MibTableColumn
zxAnSipGroupRowStatus = _ZxAnSipGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 20, 1, 30),
    _ZxAnSipGroupRowStatus_Type()
)
zxAnSipGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipGroupRowStatus.setStatus("current")
_ZxAnSipIsdnDLinkTable_Object = MibTable
zxAnSipIsdnDLinkTable = _ZxAnSipIsdnDLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21)
)
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkTable.setStatus("current")
_ZxAnSipIsdnDLinkEntry_Object = MibTableRow
zxAnSipIsdnDLinkEntry = _ZxAnSipIsdnDLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1)
)
zxAnSipIsdnDLinkEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnDLinkMgId"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnDLinkGroupId"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnDLinkLinkId"),
)
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkEntry.setStatus("current")


class _ZxAnSipIsdnDLinkMgId_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxAnSipIsdnDLinkMgId_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkMgId_Object = MibTableColumn
zxAnSipIsdnDLinkMgId = _ZxAnSipIsdnDLinkMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 1),
    _ZxAnSipIsdnDLinkMgId_Type()
)
zxAnSipIsdnDLinkMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkMgId.setStatus("current")


class _ZxAnSipIsdnDLinkGroupId_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ZxAnSipIsdnDLinkGroupId_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkGroupId_Object = MibTableColumn
zxAnSipIsdnDLinkGroupId = _ZxAnSipIsdnDLinkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 2),
    _ZxAnSipIsdnDLinkGroupId_Type()
)
zxAnSipIsdnDLinkGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkGroupId.setStatus("current")


class _ZxAnSipIsdnDLinkLinkId_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_ZxAnSipIsdnDLinkLinkId_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkLinkId_Object = MibTableColumn
zxAnSipIsdnDLinkLinkId = _ZxAnSipIsdnDLinkLinkId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 3),
    _ZxAnSipIsdnDLinkLinkId_Type()
)
zxAnSipIsdnDLinkLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkLinkId.setStatus("current")


class _ZxAnSipIsdnDLinkRack_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnSipIsdnDLinkRack_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkRack_Object = MibTableColumn
zxAnSipIsdnDLinkRack = _ZxAnSipIsdnDLinkRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 4),
    _ZxAnSipIsdnDLinkRack_Type()
)
zxAnSipIsdnDLinkRack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkRack.setStatus("current")


class _ZxAnSipIsdnDLinkShelf_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ZxAnSipIsdnDLinkShelf_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkShelf_Object = MibTableColumn
zxAnSipIsdnDLinkShelf = _ZxAnSipIsdnDLinkShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 5),
    _ZxAnSipIsdnDLinkShelf_Type()
)
zxAnSipIsdnDLinkShelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkShelf.setStatus("current")


class _ZxAnSipIsdnDLinkSlot_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_ZxAnSipIsdnDLinkSlot_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkSlot_Object = MibTableColumn
zxAnSipIsdnDLinkSlot = _ZxAnSipIsdnDLinkSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 6),
    _ZxAnSipIsdnDLinkSlot_Type()
)
zxAnSipIsdnDLinkSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkSlot.setStatus("current")


class _ZxAnSipIsdnDLinkIndex_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnSipIsdnDLinkIndex_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkIndex_Object = MibTableColumn
zxAnSipIsdnDLinkIndex = _ZxAnSipIsdnDLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 7),
    _ZxAnSipIsdnDLinkIndex_Type()
)
zxAnSipIsdnDLinkIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkIndex.setStatus("current")


class _ZxAnSipIsdnDLinkDChanTs_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkDChanTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ZxAnSipIsdnDLinkDChanTs_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkDChanTs_Object = MibTableColumn
zxAnSipIsdnDLinkDChanTs = _ZxAnSipIsdnDLinkDChanTs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 8),
    _ZxAnSipIsdnDLinkDChanTs_Type()
)
zxAnSipIsdnDLinkDChanTs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkDChanTs.setStatus("current")


class _ZxAnSipIsdnDLinkOperNum_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkOperNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnSipIsdnDLinkOperNum_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkOperNum_Object = MibTableColumn
zxAnSipIsdnDLinkOperNum = _ZxAnSipIsdnDLinkOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 9),
    _ZxAnSipIsdnDLinkOperNum_Type()
)
zxAnSipIsdnDLinkOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkOperNum.setStatus("current")


class _ZxAnSipIsdnDLinkType_Type(Integer32):
    """Custom type zxAnSipIsdnDLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link2BplusD", 1),
          ("link30BplusD", 2),
          ("link23BplusD", 3))
    )


_ZxAnSipIsdnDLinkType_Type.__name__ = "Integer32"
_ZxAnSipIsdnDLinkType_Object = MibTableColumn
zxAnSipIsdnDLinkType = _ZxAnSipIsdnDLinkType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 10),
    _ZxAnSipIsdnDLinkType_Type()
)
zxAnSipIsdnDLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkType.setStatus("current")
_ZxAnSipIsdnDLinkRowStatus_Type = RowStatus
_ZxAnSipIsdnDLinkRowStatus_Object = MibTableColumn
zxAnSipIsdnDLinkRowStatus = _ZxAnSipIsdnDLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 21, 1, 20),
    _ZxAnSipIsdnDLinkRowStatus_Type()
)
zxAnSipIsdnDLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnDLinkRowStatus.setStatus("current")
_ZxAnSipIsdnUserTable_Object = MibTable
zxAnSipIsdnUserTable = _ZxAnSipIsdnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22)
)
if mibBuilder.loadTexts:
    zxAnSipIsdnUserTable.setStatus("current")
_ZxAnSipIsdnUserEntry_Object = MibTableRow
zxAnSipIsdnUserEntry = _ZxAnSipIsdnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1)
)
zxAnSipIsdnUserEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnUserMgId"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnUserGroupId"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnUserSipPhoneNumber"),
)
if mibBuilder.loadTexts:
    zxAnSipIsdnUserEntry.setStatus("current")


class _ZxAnSipIsdnUserMgId_Type(Integer32):
    """Custom type zxAnSipIsdnUserMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxAnSipIsdnUserMgId_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserMgId_Object = MibTableColumn
zxAnSipIsdnUserMgId = _ZxAnSipIsdnUserMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 1),
    _ZxAnSipIsdnUserMgId_Type()
)
zxAnSipIsdnUserMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserMgId.setStatus("current")


class _ZxAnSipIsdnUserGroupId_Type(Integer32):
    """Custom type zxAnSipIsdnUserGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ZxAnSipIsdnUserGroupId_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserGroupId_Object = MibTableColumn
zxAnSipIsdnUserGroupId = _ZxAnSipIsdnUserGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 2),
    _ZxAnSipIsdnUserGroupId_Type()
)
zxAnSipIsdnUserGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserGroupId.setStatus("current")


class _ZxAnSipIsdnUserSipPhoneNumber_Type(DisplayString):
    """Custom type zxAnSipIsdnUserSipPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSipIsdnUserSipPhoneNumber_Type.__name__ = "DisplayString"
_ZxAnSipIsdnUserSipPhoneNumber_Object = MibTableColumn
zxAnSipIsdnUserSipPhoneNumber = _ZxAnSipIsdnUserSipPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 3),
    _ZxAnSipIsdnUserSipPhoneNumber_Type()
)
zxAnSipIsdnUserSipPhoneNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserSipPhoneNumber.setStatus("current")


class _ZxAnSipIsdnUserOperNum_Type(Integer32):
    """Custom type zxAnSipIsdnUserOperNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_ZxAnSipIsdnUserOperNum_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserOperNum_Object = MibTableColumn
zxAnSipIsdnUserOperNum = _ZxAnSipIsdnUserOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 4),
    _ZxAnSipIsdnUserOperNum_Type()
)
zxAnSipIsdnUserOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserOperNum.setStatus("current")


class _ZxAnSipIsdnUserOperType_Type(Integer32):
    """Custom type zxAnSipIsdnUserOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sipuser", 1),
          ("sipuserid", 2))
    )


_ZxAnSipIsdnUserOperType_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserOperType_Object = MibTableColumn
zxAnSipIsdnUserOperType = _ZxAnSipIsdnUserOperType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 5),
    _ZxAnSipIsdnUserOperType_Type()
)
zxAnSipIsdnUserOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserOperType.setStatus("current")


class _ZxAnSipIsdnUserAuthUsername_Type(DisplayString):
    """Custom type zxAnSipIsdnUserAuthUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSipIsdnUserAuthUsername_Type.__name__ = "DisplayString"
_ZxAnSipIsdnUserAuthUsername_Object = MibTableColumn
zxAnSipIsdnUserAuthUsername = _ZxAnSipIsdnUserAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 6),
    _ZxAnSipIsdnUserAuthUsername_Type()
)
zxAnSipIsdnUserAuthUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserAuthUsername.setStatus("current")


class _ZxAnSipIsdnUserAuthType_Type(Integer32):
    """Custom type zxAnSipIsdnUserAuthType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type2", 2),
          ("type3", 3))
    )


_ZxAnSipIsdnUserAuthType_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserAuthType_Object = MibTableColumn
zxAnSipIsdnUserAuthType = _ZxAnSipIsdnUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 7),
    _ZxAnSipIsdnUserAuthType_Type()
)
zxAnSipIsdnUserAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserAuthType.setStatus("current")


class _ZxAnSipIsdnUserAuthStartNumber_Type(Integer32):
    """Custom type zxAnSipIsdnUserAuthStartNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnSipIsdnUserAuthStartNumber_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserAuthStartNumber_Object = MibTableColumn
zxAnSipIsdnUserAuthStartNumber = _ZxAnSipIsdnUserAuthStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 8),
    _ZxAnSipIsdnUserAuthStartNumber_Type()
)
zxAnSipIsdnUserAuthStartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserAuthStartNumber.setStatus("current")


class _ZxAnSipIsdnUserAuthDigitLen_Type(Integer32):
    """Custom type zxAnSipIsdnUserAuthDigitLen based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ZxAnSipIsdnUserAuthDigitLen_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserAuthDigitLen_Object = MibTableColumn
zxAnSipIsdnUserAuthDigitLen = _ZxAnSipIsdnUserAuthDigitLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 9),
    _ZxAnSipIsdnUserAuthDigitLen_Type()
)
zxAnSipIsdnUserAuthDigitLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserAuthDigitLen.setStatus("current")


class _ZxAnSipIsdnUserPassword_Type(DisplayString):
    """Custom type zxAnSipIsdnUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnSipIsdnUserPassword_Type.__name__ = "DisplayString"
_ZxAnSipIsdnUserPassword_Object = MibTableColumn
zxAnSipIsdnUserPassword = _ZxAnSipIsdnUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 10),
    _ZxAnSipIsdnUserPassword_Type()
)
zxAnSipIsdnUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserPassword.setStatus("current")


class _ZxAnSipIsdnUserId_Type(DisplayString):
    """Custom type zxAnSipIsdnUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSipIsdnUserId_Type.__name__ = "DisplayString"
_ZxAnSipIsdnUserId_Object = MibTableColumn
zxAnSipIsdnUserId = _ZxAnSipIsdnUserId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 11),
    _ZxAnSipIsdnUserId_Type()
)
zxAnSipIsdnUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserId.setStatus("current")


class _ZxAnSipIsdnUserIdType_Type(Integer32):
    """Custom type zxAnSipIsdnUserIdType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type2", 2),
          ("type3", 3))
    )


_ZxAnSipIsdnUserIdType_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserIdType_Object = MibTableColumn
zxAnSipIsdnUserIdType = _ZxAnSipIsdnUserIdType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 12),
    _ZxAnSipIsdnUserIdType_Type()
)
zxAnSipIsdnUserIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserIdType.setStatus("current")


class _ZxAnSipIsdnUserIdStartNumber_Type(Integer32):
    """Custom type zxAnSipIsdnUserIdStartNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnSipIsdnUserIdStartNumber_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserIdStartNumber_Object = MibTableColumn
zxAnSipIsdnUserIdStartNumber = _ZxAnSipIsdnUserIdStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 13),
    _ZxAnSipIsdnUserIdStartNumber_Type()
)
zxAnSipIsdnUserIdStartNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserIdStartNumber.setStatus("current")


class _ZxAnSipIsdnUserIdDigitLen_Type(Integer32):
    """Custom type zxAnSipIsdnUserIdDigitLen based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ZxAnSipIsdnUserIdDigitLen_Type.__name__ = "Integer32"
_ZxAnSipIsdnUserIdDigitLen_Object = MibTableColumn
zxAnSipIsdnUserIdDigitLen = _ZxAnSipIsdnUserIdDigitLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 14),
    _ZxAnSipIsdnUserIdDigitLen_Type()
)
zxAnSipIsdnUserIdDigitLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserIdDigitLen.setStatus("current")
_ZxAnSipIsdnUserRowStatus_Type = RowStatus
_ZxAnSipIsdnUserRowStatus_Object = MibTableColumn
zxAnSipIsdnUserRowStatus = _ZxAnSipIsdnUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 22, 1, 50),
    _ZxAnSipIsdnUserRowStatus_Type()
)
zxAnSipIsdnUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnUserRowStatus.setStatus("current")
_ZxAnSipIsdnPhoneTable_Object = MibTable
zxAnSipIsdnPhoneTable = _ZxAnSipIsdnPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 23)
)
if mibBuilder.loadTexts:
    zxAnSipIsdnPhoneTable.setStatus("current")
_ZxAnSipIsdnPhoneEntry_Object = MibTableRow
zxAnSipIsdnPhoneEntry = _ZxAnSipIsdnPhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 23, 1)
)
zxAnSipIsdnPhoneEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnPhoneSipPhone"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnPhoneIsdnPhone"),
)
if mibBuilder.loadTexts:
    zxAnSipIsdnPhoneEntry.setStatus("current")


class _ZxAnSipIsdnPhoneSipPhone_Type(DisplayString):
    """Custom type zxAnSipIsdnPhoneSipPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnSipIsdnPhoneSipPhone_Type.__name__ = "DisplayString"
_ZxAnSipIsdnPhoneSipPhone_Object = MibTableColumn
zxAnSipIsdnPhoneSipPhone = _ZxAnSipIsdnPhoneSipPhone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 23, 1, 1),
    _ZxAnSipIsdnPhoneSipPhone_Type()
)
zxAnSipIsdnPhoneSipPhone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnPhoneSipPhone.setStatus("current")


class _ZxAnSipIsdnPhoneIsdnPhone_Type(DisplayString):
    """Custom type zxAnSipIsdnPhoneIsdnPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnSipIsdnPhoneIsdnPhone_Type.__name__ = "DisplayString"
_ZxAnSipIsdnPhoneIsdnPhone_Object = MibTableColumn
zxAnSipIsdnPhoneIsdnPhone = _ZxAnSipIsdnPhoneIsdnPhone_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 23, 1, 2),
    _ZxAnSipIsdnPhoneIsdnPhone_Type()
)
zxAnSipIsdnPhoneIsdnPhone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnPhoneIsdnPhone.setStatus("current")


class _ZxAnSipIsdnPhoneOperNum_Type(Integer32):
    """Custom type zxAnSipIsdnPhoneOperNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_ZxAnSipIsdnPhoneOperNum_Type.__name__ = "Integer32"
_ZxAnSipIsdnPhoneOperNum_Object = MibTableColumn
zxAnSipIsdnPhoneOperNum = _ZxAnSipIsdnPhoneOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 23, 1, 3),
    _ZxAnSipIsdnPhoneOperNum_Type()
)
zxAnSipIsdnPhoneOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnPhoneOperNum.setStatus("current")
_ZxAnSipIsdnPhoneRowStatus_Type = RowStatus
_ZxAnSipIsdnPhoneRowStatus_Object = MibTableColumn
zxAnSipIsdnPhoneRowStatus = _ZxAnSipIsdnPhoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 23, 1, 10),
    _ZxAnSipIsdnPhoneRowStatus_Type()
)
zxAnSipIsdnPhoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSipIsdnPhoneRowStatus.setStatus("current")
_ZxAnSipIsdnBChanTable_Object = MibTable
zxAnSipIsdnBChanTable = _ZxAnSipIsdnBChanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24)
)
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanTable.setStatus("current")
_ZxAnSipIsdnBChanEntry_Object = MibTableRow
zxAnSipIsdnBChanEntry = _ZxAnSipIsdnBChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24, 1)
)
zxAnSipIsdnBChanEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnBChanRack"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnBChanShelf"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnBChanSlot"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnBChanIndex"),
    (0, "ZTE-AN-SIP-MIB", "zxAnSipIsdnBChanTimeSlot"),
)
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanEntry.setStatus("current")


class _ZxAnSipIsdnBChanRack_Type(Integer32):
    """Custom type zxAnSipIsdnBChanRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnSipIsdnBChanRack_Type.__name__ = "Integer32"
_ZxAnSipIsdnBChanRack_Object = MibTableColumn
zxAnSipIsdnBChanRack = _ZxAnSipIsdnBChanRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24, 1, 1),
    _ZxAnSipIsdnBChanRack_Type()
)
zxAnSipIsdnBChanRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanRack.setStatus("current")


class _ZxAnSipIsdnBChanShelf_Type(Integer32):
    """Custom type zxAnSipIsdnBChanShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ZxAnSipIsdnBChanShelf_Type.__name__ = "Integer32"
_ZxAnSipIsdnBChanShelf_Object = MibTableColumn
zxAnSipIsdnBChanShelf = _ZxAnSipIsdnBChanShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24, 1, 2),
    _ZxAnSipIsdnBChanShelf_Type()
)
zxAnSipIsdnBChanShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanShelf.setStatus("current")


class _ZxAnSipIsdnBChanSlot_Type(Integer32):
    """Custom type zxAnSipIsdnBChanSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_ZxAnSipIsdnBChanSlot_Type.__name__ = "Integer32"
_ZxAnSipIsdnBChanSlot_Object = MibTableColumn
zxAnSipIsdnBChanSlot = _ZxAnSipIsdnBChanSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24, 1, 3),
    _ZxAnSipIsdnBChanSlot_Type()
)
zxAnSipIsdnBChanSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanSlot.setStatus("current")


class _ZxAnSipIsdnBChanIndex_Type(Integer32):
    """Custom type zxAnSipIsdnBChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnSipIsdnBChanIndex_Type.__name__ = "Integer32"
_ZxAnSipIsdnBChanIndex_Object = MibTableColumn
zxAnSipIsdnBChanIndex = _ZxAnSipIsdnBChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24, 1, 4),
    _ZxAnSipIsdnBChanIndex_Type()
)
zxAnSipIsdnBChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanIndex.setStatus("current")


class _ZxAnSipIsdnBChanTimeSlot_Type(Integer32):
    """Custom type zxAnSipIsdnBChanTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ZxAnSipIsdnBChanTimeSlot_Type.__name__ = "Integer32"
_ZxAnSipIsdnBChanTimeSlot_Object = MibTableColumn
zxAnSipIsdnBChanTimeSlot = _ZxAnSipIsdnBChanTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24, 1, 5),
    _ZxAnSipIsdnBChanTimeSlot_Type()
)
zxAnSipIsdnBChanTimeSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanTimeSlot.setStatus("current")


class _ZxAnSipIsdnBChanGroupId_Type(Integer32):
    """Custom type zxAnSipIsdnBChanGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_ZxAnSipIsdnBChanGroupId_Type.__name__ = "Integer32"
_ZxAnSipIsdnBChanGroupId_Object = MibTableColumn
zxAnSipIsdnBChanGroupId = _ZxAnSipIsdnBChanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24, 1, 6),
    _ZxAnSipIsdnBChanGroupId_Type()
)
zxAnSipIsdnBChanGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanGroupId.setStatus("current")


class _ZxAnSipIsdnBChanPbxBChan_Type(Integer32):
    """Custom type zxAnSipIsdnBChanPbxBChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_ZxAnSipIsdnBChanPbxBChan_Type.__name__ = "Integer32"
_ZxAnSipIsdnBChanPbxBChan_Object = MibTableColumn
zxAnSipIsdnBChanPbxBChan = _ZxAnSipIsdnBChanPbxBChan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24, 1, 7),
    _ZxAnSipIsdnBChanPbxBChan_Type()
)
zxAnSipIsdnBChanPbxBChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanPbxBChan.setStatus("current")


class _ZxAnSipIsdnBChanOperNum_Type(Integer32):
    """Custom type zxAnSipIsdnBChanOperNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ZxAnSipIsdnBChanOperNum_Type.__name__ = "Integer32"
_ZxAnSipIsdnBChanOperNum_Object = MibTableColumn
zxAnSipIsdnBChanOperNum = _ZxAnSipIsdnBChanOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 24, 1, 8),
    _ZxAnSipIsdnBChanOperNum_Type()
)
zxAnSipIsdnBChanOperNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipIsdnBChanOperNum.setStatus("current")
_ZxAnSipCallPerfTable_ObjectIdentity = ObjectIdentity
zxAnSipCallPerfTable = _ZxAnSipCallPerfTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50)
)
_ZxAnSipRegCurrentUsers_Type = Gauge32
_ZxAnSipRegCurrentUsers_Object = MibScalar
zxAnSipRegCurrentUsers = _ZxAnSipRegCurrentUsers_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 1),
    _ZxAnSipRegCurrentUsers_Type()
)
zxAnSipRegCurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipRegCurrentUsers.setStatus("current")
_ZxAnSipSuccessContactRegs_Type = Counter32
_ZxAnSipSuccessContactRegs_Object = MibScalar
zxAnSipSuccessContactRegs = _ZxAnSipSuccessContactRegs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 2),
    _ZxAnSipSuccessContactRegs_Type()
)
zxAnSipSuccessContactRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipSuccessContactRegs.setStatus("current")
_ZxAnSipFailedContactRegs_Type = Counter32
_ZxAnSipFailedContactRegs_Object = MibScalar
zxAnSipFailedContactRegs = _ZxAnSipFailedContactRegs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 3),
    _ZxAnSipFailedContactRegs_Type()
)
zxAnSipFailedContactRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipFailedContactRegs.setStatus("current")
_ZxAnSipSuccessIncomingCalls_Type = Counter32
_ZxAnSipSuccessIncomingCalls_Object = MibScalar
zxAnSipSuccessIncomingCalls = _ZxAnSipSuccessIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 4),
    _ZxAnSipSuccessIncomingCalls_Type()
)
zxAnSipSuccessIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipSuccessIncomingCalls.setStatus("current")
_ZxAnSipFailedIncomingCalls_Type = Counter32
_ZxAnSipFailedIncomingCalls_Object = MibScalar
zxAnSipFailedIncomingCalls = _ZxAnSipFailedIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 5),
    _ZxAnSipFailedIncomingCalls_Type()
)
zxAnSipFailedIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipFailedIncomingCalls.setStatus("current")
_ZxAnSipSuccessOutgoingCalls_Type = Counter32
_ZxAnSipSuccessOutgoingCalls_Object = MibScalar
zxAnSipSuccessOutgoingCalls = _ZxAnSipSuccessOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 6),
    _ZxAnSipSuccessOutgoingCalls_Type()
)
zxAnSipSuccessOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipSuccessOutgoingCalls.setStatus("current")
_ZxAnSipFailedOutgoingCalls_Type = Counter32
_ZxAnSipFailedOutgoingCalls_Object = MibScalar
zxAnSipFailedOutgoingCalls = _ZxAnSipFailedOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 7),
    _ZxAnSipFailedOutgoingCalls_Type()
)
zxAnSipFailedOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipFailedOutgoingCalls.setStatus("current")
_ZxAnSipPrev15MinSuccessContactRegs_Type = Counter32
_ZxAnSipPrev15MinSuccessContactRegs_Object = MibScalar
zxAnSipPrev15MinSuccessContactRegs = _ZxAnSipPrev15MinSuccessContactRegs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 8),
    _ZxAnSipPrev15MinSuccessContactRegs_Type()
)
zxAnSipPrev15MinSuccessContactRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipPrev15MinSuccessContactRegs.setStatus("current")
_ZxAnSipPrev15MinFailedContactRegs_Type = Counter32
_ZxAnSipPrev15MinFailedContactRegs_Object = MibScalar
zxAnSipPrev15MinFailedContactRegs = _ZxAnSipPrev15MinFailedContactRegs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 9),
    _ZxAnSipPrev15MinFailedContactRegs_Type()
)
zxAnSipPrev15MinFailedContactRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipPrev15MinFailedContactRegs.setStatus("current")
_ZxAnSipPrev15MinSuccessIncomingCalls_Type = Counter32
_ZxAnSipPrev15MinSuccessIncomingCalls_Object = MibScalar
zxAnSipPrev15MinSuccessIncomingCalls = _ZxAnSipPrev15MinSuccessIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 10),
    _ZxAnSipPrev15MinSuccessIncomingCalls_Type()
)
zxAnSipPrev15MinSuccessIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipPrev15MinSuccessIncomingCalls.setStatus("current")
_ZxAnSipPrev15MinFailedIncomingCalls_Type = Counter32
_ZxAnSipPrev15MinFailedIncomingCalls_Object = MibScalar
zxAnSipPrev15MinFailedIncomingCalls = _ZxAnSipPrev15MinFailedIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 11),
    _ZxAnSipPrev15MinFailedIncomingCalls_Type()
)
zxAnSipPrev15MinFailedIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipPrev15MinFailedIncomingCalls.setStatus("current")
_ZxAnSipPrev15MinSuccessOutgoingCalls_Type = Counter32
_ZxAnSipPrev15MinSuccessOutgoingCalls_Object = MibScalar
zxAnSipPrev15MinSuccessOutgoingCalls = _ZxAnSipPrev15MinSuccessOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 12),
    _ZxAnSipPrev15MinSuccessOutgoingCalls_Type()
)
zxAnSipPrev15MinSuccessOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipPrev15MinSuccessOutgoingCalls.setStatus("current")
_ZxAnSipPrev15MinFailedOutgoingCalls_Type = Counter32
_ZxAnSipPrev15MinFailedOutgoingCalls_Object = MibScalar
zxAnSipPrev15MinFailedOutgoingCalls = _ZxAnSipPrev15MinFailedOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 13),
    _ZxAnSipPrev15MinFailedOutgoingCalls_Type()
)
zxAnSipPrev15MinFailedOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipPrev15MinFailedOutgoingCalls.setStatus("current")
_ZxAnSipActiveIncomingCalls_Type = Counter32
_ZxAnSipActiveIncomingCalls_Object = MibScalar
zxAnSipActiveIncomingCalls = _ZxAnSipActiveIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 14),
    _ZxAnSipActiveIncomingCalls_Type()
)
zxAnSipActiveIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipActiveIncomingCalls.setStatus("current")
_ZxAnSipActiveOutgoingCalls_Type = Counter32
_ZxAnSipActiveOutgoingCalls_Object = MibScalar
zxAnSipActiveOutgoingCalls = _ZxAnSipActiveOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 15),
    _ZxAnSipActiveOutgoingCalls_Type()
)
zxAnSipActiveOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipActiveOutgoingCalls.setStatus("current")
_ZxAnSipOutgoingCallTraffic_Type = Integer32
_ZxAnSipOutgoingCallTraffic_Object = MibScalar
zxAnSipOutgoingCallTraffic = _ZxAnSipOutgoingCallTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 16),
    _ZxAnSipOutgoingCallTraffic_Type()
)
zxAnSipOutgoingCallTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipOutgoingCallTraffic.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipOutgoingCallTraffic.setUnits("erl")
_ZxAnSipIncomingCallTraffic_Type = Integer32
_ZxAnSipIncomingCallTraffic_Object = MibScalar
zxAnSipIncomingCallTraffic = _ZxAnSipIncomingCallTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 17),
    _ZxAnSipIncomingCallTraffic_Type()
)
zxAnSipIncomingCallTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipIncomingCallTraffic.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipIncomingCallTraffic.setUnits("erl")
_ZxAnSipTotalCallTraffic_Type = Integer32
_ZxAnSipTotalCallTraffic_Object = MibScalar
zxAnSipTotalCallTraffic = _ZxAnSipTotalCallTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 18),
    _ZxAnSipTotalCallTraffic_Type()
)
zxAnSipTotalCallTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipTotalCallTraffic.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipTotalCallTraffic.setUnits("erl")
_ZxAnSipOutgoingCallKeepingTime_Type = Counter32
_ZxAnSipOutgoingCallKeepingTime_Object = MibScalar
zxAnSipOutgoingCallKeepingTime = _ZxAnSipOutgoingCallKeepingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 19),
    _ZxAnSipOutgoingCallKeepingTime_Type()
)
zxAnSipOutgoingCallKeepingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipOutgoingCallKeepingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipOutgoingCallKeepingTime.setUnits("seconds")
_ZxAnSipIncomingCallKeepingTime_Type = Counter32
_ZxAnSipIncomingCallKeepingTime_Object = MibScalar
zxAnSipIncomingCallKeepingTime = _ZxAnSipIncomingCallKeepingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 20),
    _ZxAnSipIncomingCallKeepingTime_Type()
)
zxAnSipIncomingCallKeepingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipIncomingCallKeepingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipIncomingCallKeepingTime.setUnits("seconds")
_ZxAnSipTotalCallKeepingTime_Type = Counter32
_ZxAnSipTotalCallKeepingTime_Object = MibScalar
zxAnSipTotalCallKeepingTime = _ZxAnSipTotalCallKeepingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 21),
    _ZxAnSipTotalCallKeepingTime_Type()
)
zxAnSipTotalCallKeepingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipTotalCallKeepingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipTotalCallKeepingTime.setUnits("seconds")
_ZxAnSipOutgoingCallAttempts_Type = Counter32
_ZxAnSipOutgoingCallAttempts_Object = MibScalar
zxAnSipOutgoingCallAttempts = _ZxAnSipOutgoingCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 22),
    _ZxAnSipOutgoingCallAttempts_Type()
)
zxAnSipOutgoingCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipOutgoingCallAttempts.setStatus("current")
_ZxAnSipOutgoingCallCompletions_Type = Counter32
_ZxAnSipOutgoingCallCompletions_Object = MibScalar
zxAnSipOutgoingCallCompletions = _ZxAnSipOutgoingCallCompletions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 23),
    _ZxAnSipOutgoingCallCompletions_Type()
)
zxAnSipOutgoingCallCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipOutgoingCallCompletions.setStatus("current")
_ZxAnSipOutgoingCallLosses_Type = Counter32
_ZxAnSipOutgoingCallLosses_Object = MibScalar
zxAnSipOutgoingCallLosses = _ZxAnSipOutgoingCallLosses_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 24),
    _ZxAnSipOutgoingCallLosses_Type()
)
zxAnSipOutgoingCallLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipOutgoingCallLosses.setStatus("current")
_ZxAnSipIncomingCallAttempts_Type = Counter32
_ZxAnSipIncomingCallAttempts_Object = MibScalar
zxAnSipIncomingCallAttempts = _ZxAnSipIncomingCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 25),
    _ZxAnSipIncomingCallAttempts_Type()
)
zxAnSipIncomingCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipIncomingCallAttempts.setStatus("current")
_ZxAnSipIncomingCallCompletions_Type = Counter32
_ZxAnSipIncomingCallCompletions_Object = MibScalar
zxAnSipIncomingCallCompletions = _ZxAnSipIncomingCallCompletions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 26),
    _ZxAnSipIncomingCallCompletions_Type()
)
zxAnSipIncomingCallCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipIncomingCallCompletions.setStatus("current")
_ZxAnSipIncomingCallLosses_Type = Counter32
_ZxAnSipIncomingCallLosses_Object = MibScalar
zxAnSipIncomingCallLosses = _ZxAnSipIncomingCallLosses_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 27),
    _ZxAnSipIncomingCallLosses_Type()
)
zxAnSipIncomingCallLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipIncomingCallLosses.setStatus("current")


class _ZxAnSipOutgoingCallCompleteRatio_Type(Integer32):
    """Custom type zxAnSipOutgoingCallCompleteRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSipOutgoingCallCompleteRatio_Type.__name__ = "Integer32"
_ZxAnSipOutgoingCallCompleteRatio_Object = MibScalar
zxAnSipOutgoingCallCompleteRatio = _ZxAnSipOutgoingCallCompleteRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 28),
    _ZxAnSipOutgoingCallCompleteRatio_Type()
)
zxAnSipOutgoingCallCompleteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipOutgoingCallCompleteRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipOutgoingCallCompleteRatio.setUnits("percent")


class _ZxAnSipIncomingCallCompleteRatio_Type(Integer32):
    """Custom type zxAnSipIncomingCallCompleteRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSipIncomingCallCompleteRatio_Type.__name__ = "Integer32"
_ZxAnSipIncomingCallCompleteRatio_Object = MibScalar
zxAnSipIncomingCallCompleteRatio = _ZxAnSipIncomingCallCompleteRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 29),
    _ZxAnSipIncomingCallCompleteRatio_Type()
)
zxAnSipIncomingCallCompleteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipIncomingCallCompleteRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipIncomingCallCompleteRatio.setUnits("percent")


class _ZxAnSipTotalCallCompleteRatio_Type(Integer32):
    """Custom type zxAnSipTotalCallCompleteRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSipTotalCallCompleteRatio_Type.__name__ = "Integer32"
_ZxAnSipTotalCallCompleteRatio_Object = MibScalar
zxAnSipTotalCallCompleteRatio = _ZxAnSipTotalCallCompleteRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 30),
    _ZxAnSipTotalCallCompleteRatio_Type()
)
zxAnSipTotalCallCompleteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipTotalCallCompleteRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipTotalCallCompleteRatio.setUnits("percent")


class _ZxAnSipTotalCallLossRatio_Type(Integer32):
    """Custom type zxAnSipTotalCallLossRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSipTotalCallLossRatio_Type.__name__ = "Integer32"
_ZxAnSipTotalCallLossRatio_Object = MibScalar
zxAnSipTotalCallLossRatio = _ZxAnSipTotalCallLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 50, 31),
    _ZxAnSipTotalCallLossRatio_Type()
)
zxAnSipTotalCallLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipTotalCallLossRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipTotalCallLossRatio.setUnits("percent")
_ZxAnSipHisPerfObjects_ObjectIdentity = ObjectIdentity
zxAnSipHisPerfObjects = _ZxAnSipHisPerfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51)
)
_ZxAnSipHisPerfGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSipHisPerfGlobalObjects = _ZxAnSipHisPerfGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 1)
)


class _ZxAnSipHisPerfIntervalType_Type(Integer32):
    """Custom type zxAnSipHisPerfIntervalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("oneHour", 2))
    )


_ZxAnSipHisPerfIntervalType_Type.__name__ = "Integer32"
_ZxAnSipHisPerfIntervalType_Object = MibScalar
zxAnSipHisPerfIntervalType = _ZxAnSipHisPerfIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 1, 1),
    _ZxAnSipHisPerfIntervalType_Type()
)
zxAnSipHisPerfIntervalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSipHisPerfIntervalType.setStatus("current")
_ZxAnSipHisPerfIntervalTable_Object = MibTable
zxAnSipHisPerfIntervalTable = _ZxAnSipHisPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2)
)
if mibBuilder.loadTexts:
    zxAnSipHisPerfIntervalTable.setStatus("current")
_ZxAnSipHisPerfIntervalEntry_Object = MibTableRow
zxAnSipHisPerfIntervalEntry = _ZxAnSipHisPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1)
)
zxAnSipHisPerfIntervalEntry.setIndexNames(
    (0, "ZTE-AN-SIP-MIB", "zxAnSipHisPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    zxAnSipHisPerfIntervalEntry.setStatus("current")


class _ZxAnSipHisPerfIntervalNumber_Type(Integer32):
    """Custom type zxAnSipHisPerfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxAnSipHisPerfIntervalNumber_Type.__name__ = "Integer32"
_ZxAnSipHisPerfIntervalNumber_Object = MibTableColumn
zxAnSipHisPerfIntervalNumber = _ZxAnSipHisPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 1),
    _ZxAnSipHisPerfIntervalNumber_Type()
)
zxAnSipHisPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSipHisPerfIntervalNumber.setStatus("current")
_ZxAnSipHisValidData_Type = TruthValue
_ZxAnSipHisValidData_Object = MibTableColumn
zxAnSipHisValidData = _ZxAnSipHisValidData_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 2),
    _ZxAnSipHisValidData_Type()
)
zxAnSipHisValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisValidData.setStatus("current")
_ZxAnSipHisSuccessContactRegs_Type = Counter32
_ZxAnSipHisSuccessContactRegs_Object = MibTableColumn
zxAnSipHisSuccessContactRegs = _ZxAnSipHisSuccessContactRegs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 3),
    _ZxAnSipHisSuccessContactRegs_Type()
)
zxAnSipHisSuccessContactRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisSuccessContactRegs.setStatus("current")
_ZxAnSipHisFailedContactRegs_Type = Counter32
_ZxAnSipHisFailedContactRegs_Object = MibTableColumn
zxAnSipHisFailedContactRegs = _ZxAnSipHisFailedContactRegs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 4),
    _ZxAnSipHisFailedContactRegs_Type()
)
zxAnSipHisFailedContactRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisFailedContactRegs.setStatus("current")
_ZxAnSipHisSuccessInCalls_Type = Counter32
_ZxAnSipHisSuccessInCalls_Object = MibTableColumn
zxAnSipHisSuccessInCalls = _ZxAnSipHisSuccessInCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 5),
    _ZxAnSipHisSuccessInCalls_Type()
)
zxAnSipHisSuccessInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisSuccessInCalls.setStatus("current")
_ZxAnSipHisFailedInCalls_Type = Counter32
_ZxAnSipHisFailedInCalls_Object = MibTableColumn
zxAnSipHisFailedInCalls = _ZxAnSipHisFailedInCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 6),
    _ZxAnSipHisFailedInCalls_Type()
)
zxAnSipHisFailedInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisFailedInCalls.setStatus("current")
_ZxAnSipHisSuccessOutCalls_Type = Counter32
_ZxAnSipHisSuccessOutCalls_Object = MibTableColumn
zxAnSipHisSuccessOutCalls = _ZxAnSipHisSuccessOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 7),
    _ZxAnSipHisSuccessOutCalls_Type()
)
zxAnSipHisSuccessOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisSuccessOutCalls.setStatus("current")
_ZxAnSipHisFailedOutCalls_Type = Counter32
_ZxAnSipHisFailedOutCalls_Object = MibTableColumn
zxAnSipHisFailedOutCalls = _ZxAnSipHisFailedOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 8),
    _ZxAnSipHisFailedOutCalls_Type()
)
zxAnSipHisFailedOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisFailedOutCalls.setStatus("current")
_ZxAnSipHisOutCallTraffic_Type = Integer32
_ZxAnSipHisOutCallTraffic_Object = MibTableColumn
zxAnSipHisOutCallTraffic = _ZxAnSipHisOutCallTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 9),
    _ZxAnSipHisOutCallTraffic_Type()
)
zxAnSipHisOutCallTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisOutCallTraffic.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisOutCallTraffic.setUnits("erl")
_ZxAnSipHisInCallTraffic_Type = Integer32
_ZxAnSipHisInCallTraffic_Object = MibTableColumn
zxAnSipHisInCallTraffic = _ZxAnSipHisInCallTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 10),
    _ZxAnSipHisInCallTraffic_Type()
)
zxAnSipHisInCallTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisInCallTraffic.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisInCallTraffic.setUnits("erl")
_ZxAnSipHisTotalCallTraffic_Type = Integer32
_ZxAnSipHisTotalCallTraffic_Object = MibTableColumn
zxAnSipHisTotalCallTraffic = _ZxAnSipHisTotalCallTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 11),
    _ZxAnSipHisTotalCallTraffic_Type()
)
zxAnSipHisTotalCallTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisTotalCallTraffic.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisTotalCallTraffic.setUnits("erl")
_ZxAnSipHisOutCallKeepTime_Type = Counter32
_ZxAnSipHisOutCallKeepTime_Object = MibTableColumn
zxAnSipHisOutCallKeepTime = _ZxAnSipHisOutCallKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 12),
    _ZxAnSipHisOutCallKeepTime_Type()
)
zxAnSipHisOutCallKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisOutCallKeepTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisOutCallKeepTime.setUnits("seconds")
_ZxAnSipHisInCallKeepTime_Type = Counter32
_ZxAnSipHisInCallKeepTime_Object = MibTableColumn
zxAnSipHisInCallKeepTime = _ZxAnSipHisInCallKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 13),
    _ZxAnSipHisInCallKeepTime_Type()
)
zxAnSipHisInCallKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisInCallKeepTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisInCallKeepTime.setUnits("seconds")
_ZxAnSipHisTotalCallKeepTime_Type = Counter32
_ZxAnSipHisTotalCallKeepTime_Object = MibTableColumn
zxAnSipHisTotalCallKeepTime = _ZxAnSipHisTotalCallKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 14),
    _ZxAnSipHisTotalCallKeepTime_Type()
)
zxAnSipHisTotalCallKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisTotalCallKeepTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisTotalCallKeepTime.setUnits("seconds")
_ZxAnSipHisOutCallAttempts_Type = Counter32
_ZxAnSipHisOutCallAttempts_Object = MibTableColumn
zxAnSipHisOutCallAttempts = _ZxAnSipHisOutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 15),
    _ZxAnSipHisOutCallAttempts_Type()
)
zxAnSipHisOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisOutCallAttempts.setStatus("current")
_ZxAnSipHisOutCallCompletions_Type = Counter32
_ZxAnSipHisOutCallCompletions_Object = MibTableColumn
zxAnSipHisOutCallCompletions = _ZxAnSipHisOutCallCompletions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 16),
    _ZxAnSipHisOutCallCompletions_Type()
)
zxAnSipHisOutCallCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisOutCallCompletions.setStatus("current")
_ZxAnSipHisOutCallLosses_Type = Counter32
_ZxAnSipHisOutCallLosses_Object = MibTableColumn
zxAnSipHisOutCallLosses = _ZxAnSipHisOutCallLosses_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 17),
    _ZxAnSipHisOutCallLosses_Type()
)
zxAnSipHisOutCallLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisOutCallLosses.setStatus("current")
_ZxAnSipHisInCallAttempts_Type = Counter32
_ZxAnSipHisInCallAttempts_Object = MibTableColumn
zxAnSipHisInCallAttempts = _ZxAnSipHisInCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 18),
    _ZxAnSipHisInCallAttempts_Type()
)
zxAnSipHisInCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisInCallAttempts.setStatus("current")
_ZxAnSipHisInCallCompletions_Type = Counter32
_ZxAnSipHisInCallCompletions_Object = MibTableColumn
zxAnSipHisInCallCompletions = _ZxAnSipHisInCallCompletions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 19),
    _ZxAnSipHisInCallCompletions_Type()
)
zxAnSipHisInCallCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisInCallCompletions.setStatus("current")
_ZxAnSipHisInCallLosses_Type = Counter32
_ZxAnSipHisInCallLosses_Object = MibTableColumn
zxAnSipHisInCallLosses = _ZxAnSipHisInCallLosses_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 20),
    _ZxAnSipHisInCallLosses_Type()
)
zxAnSipHisInCallLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisInCallLosses.setStatus("current")


class _ZxAnSipHisOutCallCompleteRatio_Type(Integer32):
    """Custom type zxAnSipHisOutCallCompleteRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSipHisOutCallCompleteRatio_Type.__name__ = "Integer32"
_ZxAnSipHisOutCallCompleteRatio_Object = MibTableColumn
zxAnSipHisOutCallCompleteRatio = _ZxAnSipHisOutCallCompleteRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 21),
    _ZxAnSipHisOutCallCompleteRatio_Type()
)
zxAnSipHisOutCallCompleteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisOutCallCompleteRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisOutCallCompleteRatio.setUnits("percent")


class _ZxAnSipHisInCallCompleteRatio_Type(Integer32):
    """Custom type zxAnSipHisInCallCompleteRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSipHisInCallCompleteRatio_Type.__name__ = "Integer32"
_ZxAnSipHisInCallCompleteRatio_Object = MibTableColumn
zxAnSipHisInCallCompleteRatio = _ZxAnSipHisInCallCompleteRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 22),
    _ZxAnSipHisInCallCompleteRatio_Type()
)
zxAnSipHisInCallCompleteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisInCallCompleteRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisInCallCompleteRatio.setUnits("percent")


class _ZxAnSipHisTotalCallCompleteRatio_Type(Integer32):
    """Custom type zxAnSipHisTotalCallCompleteRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSipHisTotalCallCompleteRatio_Type.__name__ = "Integer32"
_ZxAnSipHisTotalCallCompleteRatio_Object = MibTableColumn
zxAnSipHisTotalCallCompleteRatio = _ZxAnSipHisTotalCallCompleteRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 23),
    _ZxAnSipHisTotalCallCompleteRatio_Type()
)
zxAnSipHisTotalCallCompleteRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisTotalCallCompleteRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisTotalCallCompleteRatio.setUnits("percent")


class _ZxAnSipHisTotalCallLossRatio_Type(Integer32):
    """Custom type zxAnSipHisTotalCallLossRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSipHisTotalCallLossRatio_Type.__name__ = "Integer32"
_ZxAnSipHisTotalCallLossRatio_Object = MibTableColumn
zxAnSipHisTotalCallLossRatio = _ZxAnSipHisTotalCallLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 8, 51, 2, 1, 24),
    _ZxAnSipHisTotalCallLossRatio_Type()
)
zxAnSipHisTotalCallLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipHisTotalCallLossRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSipHisTotalCallLossRatio.setUnits("percent")
_ZxAnSipTrap_ObjectIdentity = ObjectIdentity
zxAnSipTrap = _ZxAnSipTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 100)
)
_ZxAnSipTrapObjects_ObjectIdentity = ObjectIdentity
zxAnSipTrapObjects = _ZxAnSipTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 100, 1)
)
_ZxAnSipTrapBindVar_ObjectIdentity = ObjectIdentity
zxAnSipTrapBindVar = _ZxAnSipTrapBindVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 100, 2)
)
_ZxAnSipTrapReason_Type = Integer32
_ZxAnSipTrapReason_Object = MibScalar
zxAnSipTrapReason = _ZxAnSipTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 100, 2, 1),
    _ZxAnSipTrapReason_Type()
)
zxAnSipTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipTrapReason.setStatus("current")
_ZxAnSipTrapMgcNo_Type = Integer32
_ZxAnSipTrapMgcNo_Object = MibScalar
zxAnSipTrapMgcNo = _ZxAnSipTrapMgcNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 100, 2, 2),
    _ZxAnSipTrapMgcNo_Type()
)
zxAnSipTrapMgcNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSipTrapMgcNo.setStatus("current")

# Managed Objects groups


# Notification objects

zxAnSipLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 100, 1, 1)
)
zxAnSipLinkDown.setObjects(
      *(("ZTE-AN-SIP-MIB", "zxAnSipTrapReason"),
        ("ZTE-AN-SIP-MIB", "zxAnSipTrapMgcNo"))
)
if mibBuilder.loadTexts:
    zxAnSipLinkDown.setStatus(
        "current"
    )

zxAnSipLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 100, 1, 2)
)
zxAnSipLinkUp.setObjects(
      *(("ZTE-AN-SIP-MIB", "zxAnSipTrapReason"),
        ("ZTE-AN-SIP-MIB", "zxAnSipTrapMgcNo"))
)
if mibBuilder.loadTexts:
    zxAnSipLinkUp.setStatus(
        "current"
    )

zxAnSipUserRegisterFailedAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 100, 1, 3)
)
zxAnSipUserRegisterFailedAlm.setObjects(
      *(("ZTE-AN-SIP-MIB", "zxMsagSipUserAuthusername"),
        ("ZTE-AN-SIP-MIB", "zxMsagSipUserId"))
)
if mibBuilder.loadTexts:
    zxAnSipUserRegisterFailedAlm.setStatus(
        "current"
    )

zxAnSipUserRegisterFailedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 100, 1, 4)
)
zxAnSipUserRegisterFailedClr.setObjects(
      *(("ZTE-AN-SIP-MIB", "zxMsagSipUserAuthusername"),
        ("ZTE-AN-SIP-MIB", "zxMsagSipUserId"))
)
if mibBuilder.loadTexts:
    zxAnSipUserRegisterFailedClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-SIP-MIB",
    **{"zte": zte,
       "zxAn": zxAn,
       "zxAnSipMib": zxAnSipMib,
       "zxAnVoiceMgmt": zxAnVoiceMgmt,
       "zxAnSipConfig": zxAnSipConfig,
       "zxMsagSipUserTable": zxMsagSipUserTable,
       "zxMsagSipUserEntry": zxMsagSipUserEntry,
       "zxMsagSipUserRack": zxMsagSipUserRack,
       "zxMsagSipUserShelf": zxMsagSipUserShelf,
       "zxMsagSipUserSlot": zxMsagSipUserSlot,
       "zxMsagSipUserIndex": zxMsagSipUserIndex,
       "zxMsagSipUserOperNum": zxMsagSipUserOperNum,
       "zxMsagSipUserSipDigit": zxMsagSipUserSipDigit,
       "zxMsagSipUserAuthusername": zxMsagSipUserAuthusername,
       "zxMsagSipUserId": zxMsagSipUserId,
       "zxMsagSipUserType": zxMsagSipUserType,
       "zxMsagSipUserBeginNo": zxMsagSipUserBeginNo,
       "zxMsagSipUserDigitLen": zxMsagSipUserDigitLen,
       "zxMsagSipUserPassword": zxMsagSipUserPassword,
       "zxMsagSipUserDstngRing": zxMsagSipUserDstngRing,
       "zxMsagSipUserHotlineType": zxMsagSipUserHotlineType,
       "zxMsagSipUserHotlineNum": zxMsagSipUserHotlineNum,
       "zxMsagSipUserDigitMap": zxMsagSipUserDigitMap,
       "zxMsagSipUserOperType": zxMsagSipUserOperType,
       "zxMsagSipUserGroupId": zxMsagSipUserGroupId,
       "zxMsagSipUserAdminStatus": zxMsagSipUserAdminStatus,
       "zxMsagSipUserSessionLimit": zxMsagSipUserSessionLimit,
       "zxMsagSipUserRegisterStatus": zxMsagSipUserRegisterStatus,
       "zxMsagSipUserRowStatus": zxMsagSipUserRowStatus,
       "zxMsagSipAccessCodeTable": zxMsagSipAccessCodeTable,
       "zxMsagSipAccessCodeEntry": zxMsagSipAccessCodeEntry,
       "zxMsagSipAccessCodeMgId": zxMsagSipAccessCodeMgId,
       "zxMsagSipAccessCodeId": zxMsagSipAccessCodeId,
       "zxMsagSipAccessCodecode": zxMsagSipAccessCodecode,
       "zxMsagSipAccessCodeRowStatus": zxMsagSipAccessCodeRowStatus,
       "zxMsagSipServiceCodeTable": zxMsagSipServiceCodeTable,
       "zxMsagSipServiceCodeEntry": zxMsagSipServiceCodeEntry,
       "zxMsagSipServiceCodeMgId": zxMsagSipServiceCodeMgId,
       "zxMsagSipServiceCodeType": zxMsagSipServiceCodeType,
       "zxMsagSipServiceCode": zxMsagSipServiceCode,
       "zxMsagSipServiceCodeRowStatus": zxMsagSipServiceCodeRowStatus,
       "zxMsagSipGenFmtTable": zxMsagSipGenFmtTable,
       "zxMsagSipGenFmtEntry": zxMsagSipGenFmtEntry,
       "zxMsagSipGenFmtMgId": zxMsagSipGenFmtMgId,
       "zxMsagSipGenFmtField": zxMsagSipGenFmtField,
       "zxMsagSipGenFmtValue": zxMsagSipGenFmtValue,
       "zxMsagSipCapTable": zxMsagSipCapTable,
       "zxMsagSipCapEntry": zxMsagSipCapEntry,
       "zxMsagSipCapMgId": zxMsagSipCapMgId,
       "zxMsagSipCapSpPrecondition": zxMsagSipCapSpPrecondition,
       "zxMsagSipCapNeedReserveRes": zxMsagSipCapNeedReserveRes,
       "zxMsagSipCapSpEarlySession": zxMsagSipCapSpEarlySession,
       "zxMsagSipCapSp100Rel": zxMsagSipCapSp100Rel,
       "zxMsagSipCapSpPath": zxMsagSipCapSpPath,
       "zxMsagSipCapSpReplaces": zxMsagSipCapSpReplaces,
       "zxMsagSipCapSpTimer": zxMsagSipCapSpTimer,
       "zxMsagSipCapAudioCodePri1": zxMsagSipCapAudioCodePri1,
       "zxMsagSipCapAudioCodePri2": zxMsagSipCapAudioCodePri2,
       "zxMsagSipCapAudioCodePri3": zxMsagSipCapAudioCodePri3,
       "zxMsagSipCapAudioCodePri4": zxMsagSipCapAudioCodePri4,
       "zxMsagSipCapAudioCodePri5": zxMsagSipCapAudioCodePri5,
       "zxMsagSipCapAudioCodePri6": zxMsagSipCapAudioCodePri6,
       "zxMsagSipCapAudioCodePri7": zxMsagSipCapAudioCodePri7,
       "zxMsagSipCapDtmfRelayPri1": zxMsagSipCapDtmfRelayPri1,
       "zxMsagSipCapDtmfRelayPri2": zxMsagSipCapDtmfRelayPri2,
       "zxMsagSipCapFaxPri1": zxMsagSipCapFaxPri1,
       "zxMsagSipCapFaxPri2": zxMsagSipCapFaxPri2,
       "zxMsagSipCapSpFaxModem": zxMsagSipCapSpFaxModem,
       "zxMsagSipCapSessionMaxExpire": zxMsagSipCapSessionMaxExpire,
       "zxMsagSipCapSessionMinExpire": zxMsagSipCapSessionMinExpire,
       "zxMsagSipCapSessionRefresher": zxMsagSipCapSessionRefresher,
       "zxMsagSipCapDisplayFrom": zxMsagSipCapDisplayFrom,
       "zxMsagSipCapRegisterExpire": zxMsagSipCapRegisterExpire,
       "zxMsagSipCapReqMsgAuth": zxMsagSipCapReqMsgAuth,
       "zxMsagSipCapPPreService": zxMsagSipCapPPreService,
       "zxMsagSipCapAuthWithDomain": zxMsagSipCapAuthWithDomain,
       "zxMsagSipCapPackageInterval": zxMsagSipCapPackageInterval,
       "zxMsagSipCapSessionLimit": zxMsagSipCapSessionLimit,
       "zxMsagSipCapUserParam": zxMsagSipCapUserParam,
       "zxMsagSipCapDtmfSendingType": zxMsagSipCapDtmfSendingType,
       "zxMsagSipCapEarlyMedia": zxMsagSipCapEarlyMedia,
       "zxMsagSipCapEchoCancel": zxMsagSipCapEchoCancel,
       "zxMsagSipCapHistoryInfo": zxMsagSipCapHistoryInfo,
       "zxMsagSipCapThreePartySvrCode": zxMsagSipCapThreePartySvrCode,
       "zxMsagSipCapUserRegisterType": zxMsagSipCapUserRegisterType,
       "zxMsagSipCapHeartbeatEnable": zxMsagSipCapHeartbeatEnable,
       "zxMsagSipCapHeartbeatInterval": zxMsagSipCapHeartbeatInterval,
       "zxMsagSipCapSelfswitch": zxMsagSipCapSelfswitch,
       "zxMsagSipCapCallProtection": zxMsagSipCapCallProtection,
       "zxAnSipCapVideoMediaNegotiation": zxAnSipCapVideoMediaNegotiation,
       "zxAnSipCapUserPhoneAppendEnable": zxAnSipCapUserPhoneAppendEnable,
       "zxAnSipCapSendSubscribeMsgEnable": zxAnSipCapSendSubscribeMsgEnable,
       "zxAnSipCapFaxCodePri1": zxAnSipCapFaxCodePri1,
       "zxAnSipCapFaxCodePri2": zxAnSipCapFaxCodePri2,
       "zxAnSipCapFaxCodePri3": zxAnSipCapFaxCodePri3,
       "zxAnSipCapFaxCodePri4": zxAnSipCapFaxCodePri4,
       "zxAnSipCapFaxPacketInterval": zxAnSipCapFaxPacketInterval,
       "zxAnSipCapAutoRefreshEnable": zxAnSipCapAutoRefreshEnable,
       "zxAnSipCapImsHotlineValidTime": zxAnSipCapImsHotlineValidTime,
       "zxAnSipCapDnsRequestInterval": zxAnSipCapDnsRequestInterval,
       "zxAnSipCapCallWaitInvite18xRsp": zxAnSipCapCallWaitInvite18xRsp,
       "zxAnSipCapSubscribeUaProfileEn": zxAnSipCapSubscribeUaProfileEn,
       "zxAnSipCapSubscribeMsgSummaryEn": zxAnSipCapSubscribeMsgSummaryEn,
       "zxAnSipCapCallerControlEnable": zxAnSipCapCallerControlEnable,
       "zxAnSipCapNoDialSendInviteEnable": zxAnSipCapNoDialSendInviteEnable,
       "zxAnSipCapProxySvrAutoDrEnable": zxAnSipCapProxySvrAutoDrEnable,
       "zxAnSipCapProxySvrDrMode": zxAnSipCapProxySvrDrMode,
       "zxAnSipGlobalObjects": zxAnSipGlobalObjects,
       "zxAnSipMgmtCapabilities": zxAnSipMgmtCapabilities,
       "zxAnSipProcessReboot": zxAnSipProcessReboot,
       "zxAnSipProxyServerTable": zxAnSipProxyServerTable,
       "zxAnSipProxyServerEntry": zxAnSipProxyServerEntry,
       "zxAnSipProxySvrId": zxAnSipProxySvrId,
       "zxAnSipProxySvrIp": zxAnSipProxySvrIp,
       "zxAnSipProxySvrPort": zxAnSipProxySvrPort,
       "zxAnSipProxySvrNamingType": zxAnSipProxySvrNamingType,
       "zxAnSipProxySvrDomainName": zxAnSipProxySvrDomainName,
       "zxAnSipProxySvrRowStatus": zxAnSipProxySvrRowStatus,
       "zxAnSipUserAgentTable": zxAnSipUserAgentTable,
       "zxAnSipUserAgentEntry": zxAnSipUserAgentEntry,
       "zxAnSipUaId": zxAnSipUaId,
       "zxAnSipUaPort": zxAnSipUaPort,
       "zxAnSipUaDomainName": zxAnSipUaDomainName,
       "zxAnSipUaProxySvrId1": zxAnSipUaProxySvrId1,
       "zxAnSipUaProxySvrId2": zxAnSipUaProxySvrId2,
       "zxAnSipUaProxySvrId3": zxAnSipUaProxySvrId3,
       "zxAnSipUaProxySvrId4": zxAnSipUaProxySvrId4,
       "zxAnSipUaSelfswitch": zxAnSipUaSelfswitch,
       "zxAnSipUaCallProtection": zxAnSipUaCallProtection,
       "zxAnSipUaIpType": zxAnSipUaIpType,
       "zxAnSipUaIp": zxAnSipUaIp,
       "zxAnSipUaSwitchProxySvrId": zxAnSipUaSwitchProxySvrId,
       "zxAnSipUaCurrentProxySvrId": zxAnSipUaCurrentProxySvrId,
       "zxAnSipUaRowStatus": zxAnSipUaRowStatus,
       "zxAnSipGroupTable": zxAnSipGroupTable,
       "zxAnSipGroupEntry": zxAnSipGroupEntry,
       "zxAnSipGroupMgId": zxAnSipGroupMgId,
       "zxAnSipGroupId": zxAnSipGroupId,
       "zxAnSipGroupName": zxAnSipGroupName,
       "zxAnSipGroupType": zxAnSipGroupType,
       "zxAnSipGroupOperNum": zxAnSipGroupOperNum,
       "zxAnSipGroupPhoneNumber": zxAnSipGroupPhoneNumber,
       "zxAnSipGroupUserId": zxAnSipGroupUserId,
       "zxAnSipGroupAuthUserName": zxAnSipGroupAuthUserName,
       "zxAnSipGroupOperType": zxAnSipGroupOperType,
       "zxAnSipGroupUserType": zxAnSipGroupUserType,
       "zxAnSipGroupUserStartNumber": zxAnSipGroupUserStartNumber,
       "zxAnSipGroupUserDigitLen": zxAnSipGroupUserDigitLen,
       "zxAnSipGroupPassword": zxAnSipGroupPassword,
       "zxAnSipGroupRowStatus": zxAnSipGroupRowStatus,
       "zxAnSipIsdnDLinkTable": zxAnSipIsdnDLinkTable,
       "zxAnSipIsdnDLinkEntry": zxAnSipIsdnDLinkEntry,
       "zxAnSipIsdnDLinkMgId": zxAnSipIsdnDLinkMgId,
       "zxAnSipIsdnDLinkGroupId": zxAnSipIsdnDLinkGroupId,
       "zxAnSipIsdnDLinkLinkId": zxAnSipIsdnDLinkLinkId,
       "zxAnSipIsdnDLinkRack": zxAnSipIsdnDLinkRack,
       "zxAnSipIsdnDLinkShelf": zxAnSipIsdnDLinkShelf,
       "zxAnSipIsdnDLinkSlot": zxAnSipIsdnDLinkSlot,
       "zxAnSipIsdnDLinkIndex": zxAnSipIsdnDLinkIndex,
       "zxAnSipIsdnDLinkDChanTs": zxAnSipIsdnDLinkDChanTs,
       "zxAnSipIsdnDLinkOperNum": zxAnSipIsdnDLinkOperNum,
       "zxAnSipIsdnDLinkType": zxAnSipIsdnDLinkType,
       "zxAnSipIsdnDLinkRowStatus": zxAnSipIsdnDLinkRowStatus,
       "zxAnSipIsdnUserTable": zxAnSipIsdnUserTable,
       "zxAnSipIsdnUserEntry": zxAnSipIsdnUserEntry,
       "zxAnSipIsdnUserMgId": zxAnSipIsdnUserMgId,
       "zxAnSipIsdnUserGroupId": zxAnSipIsdnUserGroupId,
       "zxAnSipIsdnUserSipPhoneNumber": zxAnSipIsdnUserSipPhoneNumber,
       "zxAnSipIsdnUserOperNum": zxAnSipIsdnUserOperNum,
       "zxAnSipIsdnUserOperType": zxAnSipIsdnUserOperType,
       "zxAnSipIsdnUserAuthUsername": zxAnSipIsdnUserAuthUsername,
       "zxAnSipIsdnUserAuthType": zxAnSipIsdnUserAuthType,
       "zxAnSipIsdnUserAuthStartNumber": zxAnSipIsdnUserAuthStartNumber,
       "zxAnSipIsdnUserAuthDigitLen": zxAnSipIsdnUserAuthDigitLen,
       "zxAnSipIsdnUserPassword": zxAnSipIsdnUserPassword,
       "zxAnSipIsdnUserId": zxAnSipIsdnUserId,
       "zxAnSipIsdnUserIdType": zxAnSipIsdnUserIdType,
       "zxAnSipIsdnUserIdStartNumber": zxAnSipIsdnUserIdStartNumber,
       "zxAnSipIsdnUserIdDigitLen": zxAnSipIsdnUserIdDigitLen,
       "zxAnSipIsdnUserRowStatus": zxAnSipIsdnUserRowStatus,
       "zxAnSipIsdnPhoneTable": zxAnSipIsdnPhoneTable,
       "zxAnSipIsdnPhoneEntry": zxAnSipIsdnPhoneEntry,
       "zxAnSipIsdnPhoneSipPhone": zxAnSipIsdnPhoneSipPhone,
       "zxAnSipIsdnPhoneIsdnPhone": zxAnSipIsdnPhoneIsdnPhone,
       "zxAnSipIsdnPhoneOperNum": zxAnSipIsdnPhoneOperNum,
       "zxAnSipIsdnPhoneRowStatus": zxAnSipIsdnPhoneRowStatus,
       "zxAnSipIsdnBChanTable": zxAnSipIsdnBChanTable,
       "zxAnSipIsdnBChanEntry": zxAnSipIsdnBChanEntry,
       "zxAnSipIsdnBChanRack": zxAnSipIsdnBChanRack,
       "zxAnSipIsdnBChanShelf": zxAnSipIsdnBChanShelf,
       "zxAnSipIsdnBChanSlot": zxAnSipIsdnBChanSlot,
       "zxAnSipIsdnBChanIndex": zxAnSipIsdnBChanIndex,
       "zxAnSipIsdnBChanTimeSlot": zxAnSipIsdnBChanTimeSlot,
       "zxAnSipIsdnBChanGroupId": zxAnSipIsdnBChanGroupId,
       "zxAnSipIsdnBChanPbxBChan": zxAnSipIsdnBChanPbxBChan,
       "zxAnSipIsdnBChanOperNum": zxAnSipIsdnBChanOperNum,
       "zxAnSipCallPerfTable": zxAnSipCallPerfTable,
       "zxAnSipRegCurrentUsers": zxAnSipRegCurrentUsers,
       "zxAnSipSuccessContactRegs": zxAnSipSuccessContactRegs,
       "zxAnSipFailedContactRegs": zxAnSipFailedContactRegs,
       "zxAnSipSuccessIncomingCalls": zxAnSipSuccessIncomingCalls,
       "zxAnSipFailedIncomingCalls": zxAnSipFailedIncomingCalls,
       "zxAnSipSuccessOutgoingCalls": zxAnSipSuccessOutgoingCalls,
       "zxAnSipFailedOutgoingCalls": zxAnSipFailedOutgoingCalls,
       "zxAnSipPrev15MinSuccessContactRegs": zxAnSipPrev15MinSuccessContactRegs,
       "zxAnSipPrev15MinFailedContactRegs": zxAnSipPrev15MinFailedContactRegs,
       "zxAnSipPrev15MinSuccessIncomingCalls": zxAnSipPrev15MinSuccessIncomingCalls,
       "zxAnSipPrev15MinFailedIncomingCalls": zxAnSipPrev15MinFailedIncomingCalls,
       "zxAnSipPrev15MinSuccessOutgoingCalls": zxAnSipPrev15MinSuccessOutgoingCalls,
       "zxAnSipPrev15MinFailedOutgoingCalls": zxAnSipPrev15MinFailedOutgoingCalls,
       "zxAnSipActiveIncomingCalls": zxAnSipActiveIncomingCalls,
       "zxAnSipActiveOutgoingCalls": zxAnSipActiveOutgoingCalls,
       "zxAnSipOutgoingCallTraffic": zxAnSipOutgoingCallTraffic,
       "zxAnSipIncomingCallTraffic": zxAnSipIncomingCallTraffic,
       "zxAnSipTotalCallTraffic": zxAnSipTotalCallTraffic,
       "zxAnSipOutgoingCallKeepingTime": zxAnSipOutgoingCallKeepingTime,
       "zxAnSipIncomingCallKeepingTime": zxAnSipIncomingCallKeepingTime,
       "zxAnSipTotalCallKeepingTime": zxAnSipTotalCallKeepingTime,
       "zxAnSipOutgoingCallAttempts": zxAnSipOutgoingCallAttempts,
       "zxAnSipOutgoingCallCompletions": zxAnSipOutgoingCallCompletions,
       "zxAnSipOutgoingCallLosses": zxAnSipOutgoingCallLosses,
       "zxAnSipIncomingCallAttempts": zxAnSipIncomingCallAttempts,
       "zxAnSipIncomingCallCompletions": zxAnSipIncomingCallCompletions,
       "zxAnSipIncomingCallLosses": zxAnSipIncomingCallLosses,
       "zxAnSipOutgoingCallCompleteRatio": zxAnSipOutgoingCallCompleteRatio,
       "zxAnSipIncomingCallCompleteRatio": zxAnSipIncomingCallCompleteRatio,
       "zxAnSipTotalCallCompleteRatio": zxAnSipTotalCallCompleteRatio,
       "zxAnSipTotalCallLossRatio": zxAnSipTotalCallLossRatio,
       "zxAnSipHisPerfObjects": zxAnSipHisPerfObjects,
       "zxAnSipHisPerfGlobalObjects": zxAnSipHisPerfGlobalObjects,
       "zxAnSipHisPerfIntervalType": zxAnSipHisPerfIntervalType,
       "zxAnSipHisPerfIntervalTable": zxAnSipHisPerfIntervalTable,
       "zxAnSipHisPerfIntervalEntry": zxAnSipHisPerfIntervalEntry,
       "zxAnSipHisPerfIntervalNumber": zxAnSipHisPerfIntervalNumber,
       "zxAnSipHisValidData": zxAnSipHisValidData,
       "zxAnSipHisSuccessContactRegs": zxAnSipHisSuccessContactRegs,
       "zxAnSipHisFailedContactRegs": zxAnSipHisFailedContactRegs,
       "zxAnSipHisSuccessInCalls": zxAnSipHisSuccessInCalls,
       "zxAnSipHisFailedInCalls": zxAnSipHisFailedInCalls,
       "zxAnSipHisSuccessOutCalls": zxAnSipHisSuccessOutCalls,
       "zxAnSipHisFailedOutCalls": zxAnSipHisFailedOutCalls,
       "zxAnSipHisOutCallTraffic": zxAnSipHisOutCallTraffic,
       "zxAnSipHisInCallTraffic": zxAnSipHisInCallTraffic,
       "zxAnSipHisTotalCallTraffic": zxAnSipHisTotalCallTraffic,
       "zxAnSipHisOutCallKeepTime": zxAnSipHisOutCallKeepTime,
       "zxAnSipHisInCallKeepTime": zxAnSipHisInCallKeepTime,
       "zxAnSipHisTotalCallKeepTime": zxAnSipHisTotalCallKeepTime,
       "zxAnSipHisOutCallAttempts": zxAnSipHisOutCallAttempts,
       "zxAnSipHisOutCallCompletions": zxAnSipHisOutCallCompletions,
       "zxAnSipHisOutCallLosses": zxAnSipHisOutCallLosses,
       "zxAnSipHisInCallAttempts": zxAnSipHisInCallAttempts,
       "zxAnSipHisInCallCompletions": zxAnSipHisInCallCompletions,
       "zxAnSipHisInCallLosses": zxAnSipHisInCallLosses,
       "zxAnSipHisOutCallCompleteRatio": zxAnSipHisOutCallCompleteRatio,
       "zxAnSipHisInCallCompleteRatio": zxAnSipHisInCallCompleteRatio,
       "zxAnSipHisTotalCallCompleteRatio": zxAnSipHisTotalCallCompleteRatio,
       "zxAnSipHisTotalCallLossRatio": zxAnSipHisTotalCallLossRatio,
       "zxAnSipTrap": zxAnSipTrap,
       "zxAnSipTrapObjects": zxAnSipTrapObjects,
       "zxAnSipLinkDown": zxAnSipLinkDown,
       "zxAnSipLinkUp": zxAnSipLinkUp,
       "zxAnSipUserRegisterFailedAlm": zxAnSipUserRegisterFailedAlm,
       "zxAnSipUserRegisterFailedClr": zxAnSipUserRegisterFailedClr,
       "zxAnSipTrapBindVar": zxAnSipTrapBindVar,
       "zxAnSipTrapReason": zxAnSipTrapReason,
       "zxAnSipTrapMgcNo": zxAnSipTrapMgcNo}
)
