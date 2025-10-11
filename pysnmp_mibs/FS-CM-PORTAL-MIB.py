# SNMP MIB module (FS-CM-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-CM-PORTAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:11 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsCMPortalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74)
)
if mibBuilder.loadTexts:
    fsCMPortalMIB.setRevisions(
        ("2010-03-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsCMPortalMIBTrap_ObjectIdentity = ObjectIdentity
fsCMPortalMIBTrap = _FsCMPortalMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 0)
)
_FsCMPortalMIBObjects_ObjectIdentity = ObjectIdentity
fsCMPortalMIBObjects = _FsCMPortalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1)
)
_FsCMPortalMaxAuthNum_Type = Integer32
_FsCMPortalMaxAuthNum_Object = MibScalar
fsCMPortalMaxAuthNum = _FsCMPortalMaxAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 1),
    _FsCMPortalMaxAuthNum_Type()
)
fsCMPortalMaxAuthNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCMPortalMaxAuthNum.setStatus("current")
_FsCMPortalCurAuthNum_Type = Integer32
_FsCMPortalCurAuthNum_Object = MibScalar
fsCMPortalCurAuthNum = _FsCMPortalCurAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 2),
    _FsCMPortalCurAuthNum_Type()
)
fsCMPortalCurAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalCurAuthNum.setStatus("current")
_FsCMPortalServerInetAddressType_Type = InetAddressType
_FsCMPortalServerInetAddressType_Object = MibScalar
fsCMPortalServerInetAddressType = _FsCMPortalServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 3),
    _FsCMPortalServerInetAddressType_Type()
)
fsCMPortalServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCMPortalServerInetAddressType.setStatus("current")
_FsCMPortalServerInetAddress_Type = InetAddress
_FsCMPortalServerInetAddress_Object = MibScalar
fsCMPortalServerInetAddress = _FsCMPortalServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 4),
    _FsCMPortalServerInetAddress_Type()
)
fsCMPortalServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCMPortalServerInetAddress.setStatus("current")
_FsCMPortalServerInetPortNumber_Type = Integer32
_FsCMPortalServerInetPortNumber_Object = MibScalar
fsCMPortalServerInetPortNumber = _FsCMPortalServerInetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 5),
    _FsCMPortalServerInetPortNumber_Type()
)
fsCMPortalServerInetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCMPortalServerInetPortNumber.setStatus("current")


class _FsCMPortalServerUnavailableCode_Type(Integer32):
    """Custom type fsCMPortalServerUnavailableCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-configured", 0),
          ("ping-failed", 1))
    )


_FsCMPortalServerUnavailableCode_Type.__name__ = "Integer32"
_FsCMPortalServerUnavailableCode_Object = MibScalar
fsCMPortalServerUnavailableCode = _FsCMPortalServerUnavailableCode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 6),
    _FsCMPortalServerUnavailableCode_Type()
)
fsCMPortalServerUnavailableCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalServerUnavailableCode.setStatus("current")
_FsCMPortalAuthReqCount_Type = Counter32
_FsCMPortalAuthReqCount_Object = MibScalar
fsCMPortalAuthReqCount = _FsCMPortalAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 7),
    _FsCMPortalAuthReqCount_Type()
)
fsCMPortalAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalAuthReqCount.setStatus("current")
_FsCMPortalAuthRespCount_Type = Counter32
_FsCMPortalAuthRespCount_Object = MibScalar
fsCMPortalAuthRespCount = _FsCMPortalAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 8),
    _FsCMPortalAuthRespCount_Type()
)
fsCMPortalAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalAuthRespCount.setStatus("current")
_FsCMPortalChallengeReqCount_Type = Counter32
_FsCMPortalChallengeReqCount_Object = MibScalar
fsCMPortalChallengeReqCount = _FsCMPortalChallengeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 9),
    _FsCMPortalChallengeReqCount_Type()
)
fsCMPortalChallengeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalChallengeReqCount.setStatus("current")
_FsCMPortalChallengeRespCount_Type = Counter32
_FsCMPortalChallengeRespCount_Object = MibScalar
fsCMPortalChallengeRespCount = _FsCMPortalChallengeRespCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 10),
    _FsCMPortalChallengeRespCount_Type()
)
fsCMPortalChallengeRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalChallengeRespCount.setStatus("current")


class _FsCMPortalGlobalServerURL_Type(DisplayString):
    """Custom type fsCMPortalGlobalServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsCMPortalGlobalServerURL_Type.__name__ = "DisplayString"
_FsCMPortalGlobalServerURL_Object = MibScalar
fsCMPortalGlobalServerURL = _FsCMPortalGlobalServerURL_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 11),
    _FsCMPortalGlobalServerURL_Type()
)
fsCMPortalGlobalServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCMPortalGlobalServerURL.setStatus("current")
_FsCMPortalServerURLTable_Object = MibTable
fsCMPortalServerURLTable = _FsCMPortalServerURLTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 12)
)
if mibBuilder.loadTexts:
    fsCMPortalServerURLTable.setStatus("current")
_FsCMPortalServerURLEntry_Object = MibTableRow
fsCMPortalServerURLEntry = _FsCMPortalServerURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 12, 1)
)
fsCMPortalServerURLEntry.setIndexNames(
    (0, "FS-CM-PORTAL-MIB", "fsCMPortalServerURLId"),
)
if mibBuilder.loadTexts:
    fsCMPortalServerURLEntry.setStatus("current")
_FsCMPortalServerURLId_Type = Unsigned32
_FsCMPortalServerURLId_Object = MibTableColumn
fsCMPortalServerURLId = _FsCMPortalServerURLId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 12, 1, 1),
    _FsCMPortalServerURLId_Type()
)
fsCMPortalServerURLId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalServerURLId.setStatus("current")


class _FsCMPortalServerURL_Type(DisplayString):
    """Custom type fsCMPortalServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsCMPortalServerURL_Type.__name__ = "DisplayString"
_FsCMPortalServerURL_Object = MibTableColumn
fsCMPortalServerURL = _FsCMPortalServerURL_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 12, 1, 2),
    _FsCMPortalServerURL_Type()
)
fsCMPortalServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCMPortalServerURL.setStatus("current")


class _FsCMPortalServerName_Type(DisplayString):
    """Custom type fsCMPortalServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsCMPortalServerName_Type.__name__ = "DisplayString"
_FsCMPortalServerName_Object = MibTableColumn
fsCMPortalServerName = _FsCMPortalServerName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 12, 1, 3),
    _FsCMPortalServerName_Type()
)
fsCMPortalServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCMPortalServerName.setStatus("current")
_FsCMPortalServerInUsedCount_Type = Unsigned32
_FsCMPortalServerInUsedCount_Object = MibTableColumn
fsCMPortalServerInUsedCount = _FsCMPortalServerInUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 12, 1, 4),
    _FsCMPortalServerInUsedCount_Type()
)
fsCMPortalServerInUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalServerInUsedCount.setStatus("current")
_FsCMPortalServerConfigStatus_Type = RowStatus
_FsCMPortalServerConfigStatus_Object = MibTableColumn
fsCMPortalServerConfigStatus = _FsCMPortalServerConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 12, 1, 5),
    _FsCMPortalServerConfigStatus_Type()
)
fsCMPortalServerConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCMPortalServerConfigStatus.setStatus("current")
_FsCMPortalHttpReqCount_Type = Counter32
_FsCMPortalHttpReqCount_Object = MibScalar
fsCMPortalHttpReqCount = _FsCMPortalHttpReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 13),
    _FsCMPortalHttpReqCount_Type()
)
fsCMPortalHttpReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalHttpReqCount.setStatus("current")
_FsCMPortalHttpRespCount_Type = Counter32
_FsCMPortalHttpRespCount_Object = MibScalar
fsCMPortalHttpRespCount = _FsCMPortalHttpRespCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 14),
    _FsCMPortalHttpRespCount_Type()
)
fsCMPortalHttpRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalHttpRespCount.setStatus("current")
_FsCMPortalExceptionFailCount_Type = Counter32
_FsCMPortalExceptionFailCount_Object = MibScalar
fsCMPortalExceptionFailCount = _FsCMPortalExceptionFailCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 15),
    _FsCMPortalExceptionFailCount_Type()
)
fsCMPortalExceptionFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalExceptionFailCount.setStatus("current")
_FsCMPortalAuthSuccessedCount_Type = Counter32
_FsCMPortalAuthSuccessedCount_Object = MibScalar
fsCMPortalAuthSuccessedCount = _FsCMPortalAuthSuccessedCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 16),
    _FsCMPortalAuthSuccessedCount_Type()
)
fsCMPortalAuthSuccessedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalAuthSuccessedCount.setStatus("current")
_FsCMPortalNormalAuthReqCount_Type = Counter32
_FsCMPortalNormalAuthReqCount_Object = MibScalar
fsCMPortalNormalAuthReqCount = _FsCMPortalNormalAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 17),
    _FsCMPortalNormalAuthReqCount_Type()
)
fsCMPortalNormalAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalNormalAuthReqCount.setStatus("current")
_FsCMPortalEDUAuthReqCount_Type = Counter32
_FsCMPortalEDUAuthReqCount_Object = MibScalar
fsCMPortalEDUAuthReqCount = _FsCMPortalEDUAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 18),
    _FsCMPortalEDUAuthReqCount_Type()
)
fsCMPortalEDUAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalEDUAuthReqCount.setStatus("current")
_FsCMPortalStarbucksAuthReqCount_Type = Counter32
_FsCMPortalStarbucksAuthReqCount_Object = MibScalar
fsCMPortalStarbucksAuthReqCount = _FsCMPortalStarbucksAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 19),
    _FsCMPortalStarbucksAuthReqCount_Type()
)
fsCMPortalStarbucksAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalStarbucksAuthReqCount.setStatus("current")
_FsCMPortalNormalAuthRespCount_Type = Counter32
_FsCMPortalNormalAuthRespCount_Object = MibScalar
fsCMPortalNormalAuthRespCount = _FsCMPortalNormalAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 20),
    _FsCMPortalNormalAuthRespCount_Type()
)
fsCMPortalNormalAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalNormalAuthRespCount.setStatus("current")
_FsCMPortalEDUAuthRespCount_Type = Counter32
_FsCMPortalEDUAuthRespCount_Object = MibScalar
fsCMPortalEDUAuthRespCount = _FsCMPortalEDUAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 21),
    _FsCMPortalEDUAuthRespCount_Type()
)
fsCMPortalEDUAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalEDUAuthRespCount.setStatus("current")
_FsCMPortalStarbucksAuthRespCount_Type = Counter32
_FsCMPortalStarbucksAuthRespCount_Object = MibScalar
fsCMPortalStarbucksAuthRespCount = _FsCMPortalStarbucksAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 22),
    _FsCMPortalStarbucksAuthRespCount_Type()
)
fsCMPortalStarbucksAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalStarbucksAuthRespCount.setStatus("current")
_FsACPortalMaxAuthNum_Type = Integer32
_FsACPortalMaxAuthNum_Object = MibScalar
fsACPortalMaxAuthNum = _FsACPortalMaxAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 23),
    _FsACPortalMaxAuthNum_Type()
)
fsACPortalMaxAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsACPortalMaxAuthNum.setStatus("current")
_FsACPortalCurrentMaxAuthNum_Type = Integer32
_FsACPortalCurrentMaxAuthNum_Object = MibScalar
fsACPortalCurrentMaxAuthNum = _FsACPortalCurrentMaxAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 24),
    _FsACPortalCurrentMaxAuthNum_Type()
)
fsACPortalCurrentMaxAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsACPortalCurrentMaxAuthNum.setStatus("current")
_FsCMPortalAuthFailCauseTable_Object = MibTable
fsCMPortalAuthFailCauseTable = _FsCMPortalAuthFailCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 25)
)
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCauseTable.setStatus("current")
_FsCMPortalAuthFailCauseEntry_Object = MibTableRow
fsCMPortalAuthFailCauseEntry = _FsCMPortalAuthFailCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 25, 1)
)
fsCMPortalAuthFailCauseEntry.setIndexNames(
    (0, "FS-CM-PORTAL-MIB", "fsCMPortalAuthFailCauseErrId"),
)
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCauseEntry.setStatus("current")


class _FsCMPortalAuthFailCauseErrId_Type(DisplayString):
    """Custom type fsCMPortalAuthFailCauseErrId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsCMPortalAuthFailCauseErrId_Type.__name__ = "DisplayString"
_FsCMPortalAuthFailCauseErrId_Object = MibTableColumn
fsCMPortalAuthFailCauseErrId = _FsCMPortalAuthFailCauseErrId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 25, 1, 1),
    _FsCMPortalAuthFailCauseErrId_Type()
)
fsCMPortalAuthFailCauseErrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCauseErrId.setStatus("current")
_FsCMPortalAuthFailCauseCount_Type = Unsigned32
_FsCMPortalAuthFailCauseCount_Object = MibTableColumn
fsCMPortalAuthFailCauseCount = _FsCMPortalAuthFailCauseCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 25, 1, 2),
    _FsCMPortalAuthFailCauseCount_Type()
)
fsCMPortalAuthFailCauseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCauseCount.setStatus("current")
_FsCMPortalAuthFailCodeTable_Object = MibTable
fsCMPortalAuthFailCodeTable = _FsCMPortalAuthFailCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 26)
)
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCodeTable.setStatus("current")
_FsCMPortalAuthFailCodeEntry_Object = MibTableRow
fsCMPortalAuthFailCodeEntry = _FsCMPortalAuthFailCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 26, 1)
)
fsCMPortalAuthFailCodeEntry.setIndexNames(
    (0, "FS-CM-PORTAL-MIB", "fsCMPortalAuthFailCodeIndex"),
)
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCodeEntry.setStatus("current")
_FsCMPortalAuthFailCodeIndex_Type = Unsigned32
_FsCMPortalAuthFailCodeIndex_Object = MibTableColumn
fsCMPortalAuthFailCodeIndex = _FsCMPortalAuthFailCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 26, 1, 1),
    _FsCMPortalAuthFailCodeIndex_Type()
)
fsCMPortalAuthFailCodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCodeIndex.setStatus("current")
_FsCMPortalAuthFailCode_Type = Unsigned32
_FsCMPortalAuthFailCode_Object = MibTableColumn
fsCMPortalAuthFailCode = _FsCMPortalAuthFailCode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 26, 1, 2),
    _FsCMPortalAuthFailCode_Type()
)
fsCMPortalAuthFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCode.setStatus("current")
_FsCMPortalAuthFailCodeCount_Type = Unsigned32
_FsCMPortalAuthFailCodeCount_Object = MibTableColumn
fsCMPortalAuthFailCodeCount = _FsCMPortalAuthFailCodeCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 26, 1, 3),
    _FsCMPortalAuthFailCodeCount_Type()
)
fsCMPortalAuthFailCodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCodeCount.setStatus("current")
_FsCMPortalLogoutReqCount_Type = Counter32
_FsCMPortalLogoutReqCount_Object = MibScalar
fsCMPortalLogoutReqCount = _FsCMPortalLogoutReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 27),
    _FsCMPortalLogoutReqCount_Type()
)
fsCMPortalLogoutReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalLogoutReqCount.setStatus("current")
_FsCMPortalLogoutRespCount_Type = Counter32
_FsCMPortalLogoutRespCount_Object = MibScalar
fsCMPortalLogoutRespCount = _FsCMPortalLogoutRespCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 28),
    _FsCMPortalLogoutRespCount_Type()
)
fsCMPortalLogoutRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalLogoutRespCount.setStatus("current")
_FsCMPortalNtfLogoutReqCount_Type = Counter32
_FsCMPortalNtfLogoutReqCount_Object = MibScalar
fsCMPortalNtfLogoutReqCount = _FsCMPortalNtfLogoutReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 29),
    _FsCMPortalNtfLogoutReqCount_Type()
)
fsCMPortalNtfLogoutReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalNtfLogoutReqCount.setStatus("current")
_FsCMPortalNtfLogoutRespCount_Type = Counter32
_FsCMPortalNtfLogoutRespCount_Object = MibScalar
fsCMPortalNtfLogoutRespCount = _FsCMPortalNtfLogoutRespCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 30),
    _FsCMPortalNtfLogoutRespCount_Type()
)
fsCMPortalNtfLogoutRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalNtfLogoutRespCount.setStatus("current")
_FsApNasPortIdTable_Object = MibTable
fsApNasPortIdTable = _FsApNasPortIdTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 31)
)
if mibBuilder.loadTexts:
    fsApNasPortIdTable.setStatus("current")
_FsApNasPortIdEntry_Object = MibTableRow
fsApNasPortIdEntry = _FsApNasPortIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 31, 1)
)
fsApNasPortIdEntry.setIndexNames(
    (0, "FS-CM-PORTAL-MIB", "fsApNasPortIdApMacAddress"),
    (0, "FS-CM-PORTAL-MIB", "fsApNasPortIdRadioId"),
    (0, "FS-CM-PORTAL-MIB", "fsApNasPortIdWlanId"),
)
if mibBuilder.loadTexts:
    fsApNasPortIdEntry.setStatus("current")
_FsApNasPortIdApMacAddress_Type = MacAddress
_FsApNasPortIdApMacAddress_Object = MibTableColumn
fsApNasPortIdApMacAddress = _FsApNasPortIdApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 31, 1, 1),
    _FsApNasPortIdApMacAddress_Type()
)
fsApNasPortIdApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApNasPortIdApMacAddress.setStatus("current")
_FsApNasPortIdRadioId_Type = Unsigned32
_FsApNasPortIdRadioId_Object = MibTableColumn
fsApNasPortIdRadioId = _FsApNasPortIdRadioId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 31, 1, 2),
    _FsApNasPortIdRadioId_Type()
)
fsApNasPortIdRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApNasPortIdRadioId.setStatus("current")
_FsApNasPortIdWlanId_Type = Unsigned32
_FsApNasPortIdWlanId_Object = MibTableColumn
fsApNasPortIdWlanId = _FsApNasPortIdWlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 31, 1, 3),
    _FsApNasPortIdWlanId_Type()
)
fsApNasPortIdWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApNasPortIdWlanId.setStatus("current")
_FsApNasPortIdNasPortId_Type = DisplayString
_FsApNasPortIdNasPortId_Object = MibTableColumn
fsApNasPortIdNasPortId = _FsApNasPortIdNasPortId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 31, 1, 4),
    _FsApNasPortIdNasPortId_Type()
)
fsApNasPortIdNasPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApNasPortIdNasPortId.setStatus("current")
_FsCMPortalAuthFailCount_Type = Counter32
_FsCMPortalAuthFailCount_Object = MibScalar
fsCMPortalAuthFailCount = _FsCMPortalAuthFailCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 32),
    _FsCMPortalAuthFailCount_Type()
)
fsCMPortalAuthFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalAuthFailCount.setStatus("current")
_FsCMPortalMaxHttpConnectionNum_Type = Counter32
_FsCMPortalMaxHttpConnectionNum_Object = MibScalar
fsCMPortalMaxHttpConnectionNum = _FsCMPortalMaxHttpConnectionNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 1, 33),
    _FsCMPortalMaxHttpConnectionNum_Type()
)
fsCMPortalMaxHttpConnectionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCMPortalMaxHttpConnectionNum.setStatus("current")
_FsCMPortalMIBConformance_ObjectIdentity = ObjectIdentity
fsCMPortalMIBConformance = _FsCMPortalMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 2)
)
_FsCMPortalMIBCompliances_ObjectIdentity = ObjectIdentity
fsCMPortalMIBCompliances = _FsCMPortalMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 2, 1)
)
_FsCMPortalMIBGroups_ObjectIdentity = ObjectIdentity
fsCMPortalMIBGroups = _FsCMPortalMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 2, 2)
)

# Managed Objects groups

fsCMPortalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 2, 2, 1)
)
fsCMPortalMIBGroup.setObjects(
      *(("FS-CM-PORTAL-MIB", "fsCMPortalMaxAuthNum"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalCurAuthNum"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerInetAddressType"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerInetAddress"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerInetPortNumber"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerUnavailableCode"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalAuthReqCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalAuthRespCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalChallengeReqCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalChallengeRespCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalGlobalServerURL"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerURL"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerName"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerInUsedCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerConfigStatus"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalHttpReqCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalHttpRespCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalExceptionFailCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalAuthSuccessedCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalNormalAuthReqCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalEDUAuthReqCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalStarbucksAuthReqCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalNormalAuthRespCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalEDUAuthRespCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalStarbucksAuthRespCount"),
        ("FS-CM-PORTAL-MIB", "fsACPortalMaxAuthNum"),
        ("FS-CM-PORTAL-MIB", "fsACPortalCurrentMaxAuthNum"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalAuthFailCauseCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalAuthFailCode"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalAuthFailCodeCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalLogoutReqCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalLogoutRespCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalNtfLogoutReqCount"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalNtfLogoutRespCount"),
        ("FS-CM-PORTAL-MIB", "fsApNasPortIdApMacAddress"),
        ("FS-CM-PORTAL-MIB", "fsApNasPortIdRadioId"),
        ("FS-CM-PORTAL-MIB", "fsApNasPortIdWlanId"),
        ("FS-CM-PORTAL-MIB", "fsApNasPortIdNasPortId"))
)
if mibBuilder.loadTexts:
    fsCMPortalMIBGroup.setStatus("deprecated")


# Notification objects

fsCMPortalServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 0, 1)
)
fsCMPortalServerDownTrap.setObjects(
      *(("FS-CM-PORTAL-MIB", "fsCMPortalServerInetAddressType"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerInetAddress"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerInetPortNumber"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerUnavailableCode"))
)
if mibBuilder.loadTexts:
    fsCMPortalServerDownTrap.setStatus(
        "current"
    )

fsCMPortalServerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 0, 2)
)
fsCMPortalServerRecoverTrap.setObjects(
      *(("FS-CM-PORTAL-MIB", "fsCMPortalServerInetAddressType"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerInetAddress"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerInetPortNumber"),
        ("FS-CM-PORTAL-MIB", "fsCMPortalServerUnavailableCode"))
)
if mibBuilder.loadTexts:
    fsCMPortalServerRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsCMPortalMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 74, 2, 1, 1)
)
fsCMPortalMIBCompliance.setObjects(
    ("FS-CM-PORTAL-MIB", "fsCMPortalMIBGroup")
)
if mibBuilder.loadTexts:
    fsCMPortalMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-CM-PORTAL-MIB",
    **{"fsCMPortalMIB": fsCMPortalMIB,
       "fsCMPortalMIBTrap": fsCMPortalMIBTrap,
       "fsCMPortalServerDownTrap": fsCMPortalServerDownTrap,
       "fsCMPortalServerRecoverTrap": fsCMPortalServerRecoverTrap,
       "fsCMPortalMIBObjects": fsCMPortalMIBObjects,
       "fsCMPortalMaxAuthNum": fsCMPortalMaxAuthNum,
       "fsCMPortalCurAuthNum": fsCMPortalCurAuthNum,
       "fsCMPortalServerInetAddressType": fsCMPortalServerInetAddressType,
       "fsCMPortalServerInetAddress": fsCMPortalServerInetAddress,
       "fsCMPortalServerInetPortNumber": fsCMPortalServerInetPortNumber,
       "fsCMPortalServerUnavailableCode": fsCMPortalServerUnavailableCode,
       "fsCMPortalAuthReqCount": fsCMPortalAuthReqCount,
       "fsCMPortalAuthRespCount": fsCMPortalAuthRespCount,
       "fsCMPortalChallengeReqCount": fsCMPortalChallengeReqCount,
       "fsCMPortalChallengeRespCount": fsCMPortalChallengeRespCount,
       "fsCMPortalGlobalServerURL": fsCMPortalGlobalServerURL,
       "fsCMPortalServerURLTable": fsCMPortalServerURLTable,
       "fsCMPortalServerURLEntry": fsCMPortalServerURLEntry,
       "fsCMPortalServerURLId": fsCMPortalServerURLId,
       "fsCMPortalServerURL": fsCMPortalServerURL,
       "fsCMPortalServerName": fsCMPortalServerName,
       "fsCMPortalServerInUsedCount": fsCMPortalServerInUsedCount,
       "fsCMPortalServerConfigStatus": fsCMPortalServerConfigStatus,
       "fsCMPortalHttpReqCount": fsCMPortalHttpReqCount,
       "fsCMPortalHttpRespCount": fsCMPortalHttpRespCount,
       "fsCMPortalExceptionFailCount": fsCMPortalExceptionFailCount,
       "fsCMPortalAuthSuccessedCount": fsCMPortalAuthSuccessedCount,
       "fsCMPortalNormalAuthReqCount": fsCMPortalNormalAuthReqCount,
       "fsCMPortalEDUAuthReqCount": fsCMPortalEDUAuthReqCount,
       "fsCMPortalStarbucksAuthReqCount": fsCMPortalStarbucksAuthReqCount,
       "fsCMPortalNormalAuthRespCount": fsCMPortalNormalAuthRespCount,
       "fsCMPortalEDUAuthRespCount": fsCMPortalEDUAuthRespCount,
       "fsCMPortalStarbucksAuthRespCount": fsCMPortalStarbucksAuthRespCount,
       "fsACPortalMaxAuthNum": fsACPortalMaxAuthNum,
       "fsACPortalCurrentMaxAuthNum": fsACPortalCurrentMaxAuthNum,
       "fsCMPortalAuthFailCauseTable": fsCMPortalAuthFailCauseTable,
       "fsCMPortalAuthFailCauseEntry": fsCMPortalAuthFailCauseEntry,
       "fsCMPortalAuthFailCauseErrId": fsCMPortalAuthFailCauseErrId,
       "fsCMPortalAuthFailCauseCount": fsCMPortalAuthFailCauseCount,
       "fsCMPortalAuthFailCodeTable": fsCMPortalAuthFailCodeTable,
       "fsCMPortalAuthFailCodeEntry": fsCMPortalAuthFailCodeEntry,
       "fsCMPortalAuthFailCodeIndex": fsCMPortalAuthFailCodeIndex,
       "fsCMPortalAuthFailCode": fsCMPortalAuthFailCode,
       "fsCMPortalAuthFailCodeCount": fsCMPortalAuthFailCodeCount,
       "fsCMPortalLogoutReqCount": fsCMPortalLogoutReqCount,
       "fsCMPortalLogoutRespCount": fsCMPortalLogoutRespCount,
       "fsCMPortalNtfLogoutReqCount": fsCMPortalNtfLogoutReqCount,
       "fsCMPortalNtfLogoutRespCount": fsCMPortalNtfLogoutRespCount,
       "fsApNasPortIdTable": fsApNasPortIdTable,
       "fsApNasPortIdEntry": fsApNasPortIdEntry,
       "fsApNasPortIdApMacAddress": fsApNasPortIdApMacAddress,
       "fsApNasPortIdRadioId": fsApNasPortIdRadioId,
       "fsApNasPortIdWlanId": fsApNasPortIdWlanId,
       "fsApNasPortIdNasPortId": fsApNasPortIdNasPortId,
       "fsCMPortalAuthFailCount": fsCMPortalAuthFailCount,
       "fsCMPortalMaxHttpConnectionNum": fsCMPortalMaxHttpConnectionNum,
       "fsCMPortalMIBConformance": fsCMPortalMIBConformance,
       "fsCMPortalMIBCompliances": fsCMPortalMIBCompliances,
       "fsCMPortalMIBCompliance": fsCMPortalMIBCompliance,
       "fsCMPortalMIBGroups": fsCMPortalMIBGroups,
       "fsCMPortalMIBGroup": fsCMPortalMIBGroup}
)
