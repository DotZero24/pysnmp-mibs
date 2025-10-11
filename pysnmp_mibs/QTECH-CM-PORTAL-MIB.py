# SNMP MIB module (QTECH-CM-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CM-PORTAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:01 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

qtechCMPortalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74)
)
if mibBuilder.loadTexts:
    qtechCMPortalMIB.setRevisions(
        ("2010-03-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechCMPortalMIBTrap_ObjectIdentity = ObjectIdentity
qtechCMPortalMIBTrap = _QtechCMPortalMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 0)
)
_QtechCMPortalMIBObjects_ObjectIdentity = ObjectIdentity
qtechCMPortalMIBObjects = _QtechCMPortalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1)
)
_QtechCMPortalMaxAuthNum_Type = Integer32
_QtechCMPortalMaxAuthNum_Object = MibScalar
qtechCMPortalMaxAuthNum = _QtechCMPortalMaxAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 1),
    _QtechCMPortalMaxAuthNum_Type()
)
qtechCMPortalMaxAuthNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCMPortalMaxAuthNum.setStatus("current")
_QtechCMPortalCurAuthNum_Type = Integer32
_QtechCMPortalCurAuthNum_Object = MibScalar
qtechCMPortalCurAuthNum = _QtechCMPortalCurAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 2),
    _QtechCMPortalCurAuthNum_Type()
)
qtechCMPortalCurAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalCurAuthNum.setStatus("current")
_QtechCMPortalServerInetAddressType_Type = InetAddressType
_QtechCMPortalServerInetAddressType_Object = MibScalar
qtechCMPortalServerInetAddressType = _QtechCMPortalServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 3),
    _QtechCMPortalServerInetAddressType_Type()
)
qtechCMPortalServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCMPortalServerInetAddressType.setStatus("current")
_QtechCMPortalServerInetAddress_Type = InetAddress
_QtechCMPortalServerInetAddress_Object = MibScalar
qtechCMPortalServerInetAddress = _QtechCMPortalServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 4),
    _QtechCMPortalServerInetAddress_Type()
)
qtechCMPortalServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCMPortalServerInetAddress.setStatus("current")
_QtechCMPortalServerInetPortNumber_Type = Integer32
_QtechCMPortalServerInetPortNumber_Object = MibScalar
qtechCMPortalServerInetPortNumber = _QtechCMPortalServerInetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 5),
    _QtechCMPortalServerInetPortNumber_Type()
)
qtechCMPortalServerInetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCMPortalServerInetPortNumber.setStatus("current")


class _QtechCMPortalServerUnavailableCode_Type(Integer32):
    """Custom type qtechCMPortalServerUnavailableCode based on Integer32"""
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


_QtechCMPortalServerUnavailableCode_Type.__name__ = "Integer32"
_QtechCMPortalServerUnavailableCode_Object = MibScalar
qtechCMPortalServerUnavailableCode = _QtechCMPortalServerUnavailableCode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 6),
    _QtechCMPortalServerUnavailableCode_Type()
)
qtechCMPortalServerUnavailableCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalServerUnavailableCode.setStatus("current")
_QtechCMPortalAuthReqCount_Type = Counter32
_QtechCMPortalAuthReqCount_Object = MibScalar
qtechCMPortalAuthReqCount = _QtechCMPortalAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 7),
    _QtechCMPortalAuthReqCount_Type()
)
qtechCMPortalAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalAuthReqCount.setStatus("current")
_QtechCMPortalAuthRespCount_Type = Counter32
_QtechCMPortalAuthRespCount_Object = MibScalar
qtechCMPortalAuthRespCount = _QtechCMPortalAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 8),
    _QtechCMPortalAuthRespCount_Type()
)
qtechCMPortalAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalAuthRespCount.setStatus("current")
_QtechCMPortalChallengeReqCount_Type = Counter32
_QtechCMPortalChallengeReqCount_Object = MibScalar
qtechCMPortalChallengeReqCount = _QtechCMPortalChallengeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 9),
    _QtechCMPortalChallengeReqCount_Type()
)
qtechCMPortalChallengeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalChallengeReqCount.setStatus("current")
_QtechCMPortalChallengeRespCount_Type = Counter32
_QtechCMPortalChallengeRespCount_Object = MibScalar
qtechCMPortalChallengeRespCount = _QtechCMPortalChallengeRespCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 10),
    _QtechCMPortalChallengeRespCount_Type()
)
qtechCMPortalChallengeRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalChallengeRespCount.setStatus("current")


class _QtechCMPortalGlobalServerURL_Type(DisplayString):
    """Custom type qtechCMPortalGlobalServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechCMPortalGlobalServerURL_Type.__name__ = "DisplayString"
_QtechCMPortalGlobalServerURL_Object = MibScalar
qtechCMPortalGlobalServerURL = _QtechCMPortalGlobalServerURL_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 11),
    _QtechCMPortalGlobalServerURL_Type()
)
qtechCMPortalGlobalServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCMPortalGlobalServerURL.setStatus("current")
_QtechCMPortalServerURLTable_Object = MibTable
qtechCMPortalServerURLTable = _QtechCMPortalServerURLTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 12)
)
if mibBuilder.loadTexts:
    qtechCMPortalServerURLTable.setStatus("current")
_QtechCMPortalServerURLEntry_Object = MibTableRow
qtechCMPortalServerURLEntry = _QtechCMPortalServerURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 12, 1)
)
qtechCMPortalServerURLEntry.setIndexNames(
    (0, "QTECH-CM-PORTAL-MIB", "qtechCMPortalServerURLId"),
)
if mibBuilder.loadTexts:
    qtechCMPortalServerURLEntry.setStatus("current")
_QtechCMPortalServerURLId_Type = Unsigned32
_QtechCMPortalServerURLId_Object = MibTableColumn
qtechCMPortalServerURLId = _QtechCMPortalServerURLId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 12, 1, 1),
    _QtechCMPortalServerURLId_Type()
)
qtechCMPortalServerURLId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalServerURLId.setStatus("current")


class _QtechCMPortalServerURL_Type(DisplayString):
    """Custom type qtechCMPortalServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechCMPortalServerURL_Type.__name__ = "DisplayString"
_QtechCMPortalServerURL_Object = MibTableColumn
qtechCMPortalServerURL = _QtechCMPortalServerURL_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 12, 1, 2),
    _QtechCMPortalServerURL_Type()
)
qtechCMPortalServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCMPortalServerURL.setStatus("current")


class _QtechCMPortalServerName_Type(DisplayString):
    """Custom type qtechCMPortalServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechCMPortalServerName_Type.__name__ = "DisplayString"
_QtechCMPortalServerName_Object = MibTableColumn
qtechCMPortalServerName = _QtechCMPortalServerName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 12, 1, 3),
    _QtechCMPortalServerName_Type()
)
qtechCMPortalServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCMPortalServerName.setStatus("current")
_QtechCMPortalServerInUsedCount_Type = Unsigned32
_QtechCMPortalServerInUsedCount_Object = MibTableColumn
qtechCMPortalServerInUsedCount = _QtechCMPortalServerInUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 12, 1, 4),
    _QtechCMPortalServerInUsedCount_Type()
)
qtechCMPortalServerInUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalServerInUsedCount.setStatus("current")
_QtechCMPortalServerConfigStatus_Type = RowStatus
_QtechCMPortalServerConfigStatus_Object = MibTableColumn
qtechCMPortalServerConfigStatus = _QtechCMPortalServerConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 12, 1, 5),
    _QtechCMPortalServerConfigStatus_Type()
)
qtechCMPortalServerConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechCMPortalServerConfigStatus.setStatus("current")
_QtechCMPortalHttpReqCount_Type = Counter32
_QtechCMPortalHttpReqCount_Object = MibScalar
qtechCMPortalHttpReqCount = _QtechCMPortalHttpReqCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 13),
    _QtechCMPortalHttpReqCount_Type()
)
qtechCMPortalHttpReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalHttpReqCount.setStatus("current")
_QtechCMPortalHttpRespCount_Type = Counter32
_QtechCMPortalHttpRespCount_Object = MibScalar
qtechCMPortalHttpRespCount = _QtechCMPortalHttpRespCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 14),
    _QtechCMPortalHttpRespCount_Type()
)
qtechCMPortalHttpRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalHttpRespCount.setStatus("current")
_QtechCMPortalExceptionFailCount_Type = Counter32
_QtechCMPortalExceptionFailCount_Object = MibScalar
qtechCMPortalExceptionFailCount = _QtechCMPortalExceptionFailCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 15),
    _QtechCMPortalExceptionFailCount_Type()
)
qtechCMPortalExceptionFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalExceptionFailCount.setStatus("current")
_QtechCMPortalAuthSuccessedCount_Type = Counter32
_QtechCMPortalAuthSuccessedCount_Object = MibScalar
qtechCMPortalAuthSuccessedCount = _QtechCMPortalAuthSuccessedCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 16),
    _QtechCMPortalAuthSuccessedCount_Type()
)
qtechCMPortalAuthSuccessedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalAuthSuccessedCount.setStatus("current")
_QtechCMPortalNormalAuthReqCount_Type = Counter32
_QtechCMPortalNormalAuthReqCount_Object = MibScalar
qtechCMPortalNormalAuthReqCount = _QtechCMPortalNormalAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 17),
    _QtechCMPortalNormalAuthReqCount_Type()
)
qtechCMPortalNormalAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalNormalAuthReqCount.setStatus("current")
_QtechCMPortalEDUAuthReqCount_Type = Counter32
_QtechCMPortalEDUAuthReqCount_Object = MibScalar
qtechCMPortalEDUAuthReqCount = _QtechCMPortalEDUAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 18),
    _QtechCMPortalEDUAuthReqCount_Type()
)
qtechCMPortalEDUAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalEDUAuthReqCount.setStatus("current")
_QtechCMPortalStarbucksAuthReqCount_Type = Counter32
_QtechCMPortalStarbucksAuthReqCount_Object = MibScalar
qtechCMPortalStarbucksAuthReqCount = _QtechCMPortalStarbucksAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 19),
    _QtechCMPortalStarbucksAuthReqCount_Type()
)
qtechCMPortalStarbucksAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalStarbucksAuthReqCount.setStatus("current")
_QtechCMPortalNormalAuthRespCount_Type = Counter32
_QtechCMPortalNormalAuthRespCount_Object = MibScalar
qtechCMPortalNormalAuthRespCount = _QtechCMPortalNormalAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 20),
    _QtechCMPortalNormalAuthRespCount_Type()
)
qtechCMPortalNormalAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalNormalAuthRespCount.setStatus("current")
_QtechCMPortalEDUAuthRespCount_Type = Counter32
_QtechCMPortalEDUAuthRespCount_Object = MibScalar
qtechCMPortalEDUAuthRespCount = _QtechCMPortalEDUAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 21),
    _QtechCMPortalEDUAuthRespCount_Type()
)
qtechCMPortalEDUAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalEDUAuthRespCount.setStatus("current")
_QtechCMPortalStarbucksAuthRespCount_Type = Counter32
_QtechCMPortalStarbucksAuthRespCount_Object = MibScalar
qtechCMPortalStarbucksAuthRespCount = _QtechCMPortalStarbucksAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 22),
    _QtechCMPortalStarbucksAuthRespCount_Type()
)
qtechCMPortalStarbucksAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCMPortalStarbucksAuthRespCount.setStatus("current")
_QtechACPortalMaxAuthNum_Type = Integer32
_QtechACPortalMaxAuthNum_Object = MibScalar
qtechACPortalMaxAuthNum = _QtechACPortalMaxAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 23),
    _QtechACPortalMaxAuthNum_Type()
)
qtechACPortalMaxAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechACPortalMaxAuthNum.setStatus("current")
_QtechACPortalCurrentMaxAuthNum_Type = Integer32
_QtechACPortalCurrentMaxAuthNum_Object = MibScalar
qtechACPortalCurrentMaxAuthNum = _QtechACPortalCurrentMaxAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 1, 24),
    _QtechACPortalCurrentMaxAuthNum_Type()
)
qtechACPortalCurrentMaxAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechACPortalCurrentMaxAuthNum.setStatus("current")
_QtechCMPortalMIBConformance_ObjectIdentity = ObjectIdentity
qtechCMPortalMIBConformance = _QtechCMPortalMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 2)
)
_QtechCMPortalMIBCompliances_ObjectIdentity = ObjectIdentity
qtechCMPortalMIBCompliances = _QtechCMPortalMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 2, 1)
)
_QtechCMPortalMIBGroups_ObjectIdentity = ObjectIdentity
qtechCMPortalMIBGroups = _QtechCMPortalMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 2, 2)
)

# Managed Objects groups

qtechCMPortalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 2, 2, 1)
)
qtechCMPortalMIBGroup.setObjects(
      *(("QTECH-CM-PORTAL-MIB", "qtechCMPortalMaxAuthNum"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalCurAuthNum"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInetAddressType"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInetAddress"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInetPortNumber"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerUnavailableCode"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalAuthReqCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalAuthRespCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalChallengeReqCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalChallengeRespCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalGlobalServerURL"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerURL"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerName"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInUsedCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerConfigStatus"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalHttpReqCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalHttpRespCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalExceptionFailCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalAuthSuccessedCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalNormalAuthReqCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalEDUAuthReqCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalStarbucksAuthReqCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalNormalAuthRespCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalEDUAuthRespCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalStarbucksAuthRespCount"),
        ("QTECH-CM-PORTAL-MIB", "qtechACPortalMaxAuthNum"),
        ("QTECH-CM-PORTAL-MIB", "qtechACPortalCurrentMaxAuthNum"))
)
if mibBuilder.loadTexts:
    qtechCMPortalMIBGroup.setStatus("deprecated")


# Notification objects

qtechCMPortalServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 0, 1)
)
qtechCMPortalServerDownTrap.setObjects(
      *(("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInetAddressType"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInetAddress"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInetPortNumber"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerUnavailableCode"))
)
if mibBuilder.loadTexts:
    qtechCMPortalServerDownTrap.setStatus(
        "current"
    )

qtechCMPortalServerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 0, 2)
)
qtechCMPortalServerRecoverTrap.setObjects(
      *(("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInetAddressType"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInetAddress"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerInetPortNumber"),
        ("QTECH-CM-PORTAL-MIB", "qtechCMPortalServerUnavailableCode"))
)
if mibBuilder.loadTexts:
    qtechCMPortalServerRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechCMPortalMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 74, 2, 1, 1)
)
qtechCMPortalMIBCompliance.setObjects(
    ("QTECH-CM-PORTAL-MIB", "qtechCMPortalMIBGroup")
)
if mibBuilder.loadTexts:
    qtechCMPortalMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CM-PORTAL-MIB",
    **{"qtechCMPortalMIB": qtechCMPortalMIB,
       "qtechCMPortalMIBTrap": qtechCMPortalMIBTrap,
       "qtechCMPortalServerDownTrap": qtechCMPortalServerDownTrap,
       "qtechCMPortalServerRecoverTrap": qtechCMPortalServerRecoverTrap,
       "qtechCMPortalMIBObjects": qtechCMPortalMIBObjects,
       "qtechCMPortalMaxAuthNum": qtechCMPortalMaxAuthNum,
       "qtechCMPortalCurAuthNum": qtechCMPortalCurAuthNum,
       "qtechCMPortalServerInetAddressType": qtechCMPortalServerInetAddressType,
       "qtechCMPortalServerInetAddress": qtechCMPortalServerInetAddress,
       "qtechCMPortalServerInetPortNumber": qtechCMPortalServerInetPortNumber,
       "qtechCMPortalServerUnavailableCode": qtechCMPortalServerUnavailableCode,
       "qtechCMPortalAuthReqCount": qtechCMPortalAuthReqCount,
       "qtechCMPortalAuthRespCount": qtechCMPortalAuthRespCount,
       "qtechCMPortalChallengeReqCount": qtechCMPortalChallengeReqCount,
       "qtechCMPortalChallengeRespCount": qtechCMPortalChallengeRespCount,
       "qtechCMPortalGlobalServerURL": qtechCMPortalGlobalServerURL,
       "qtechCMPortalServerURLTable": qtechCMPortalServerURLTable,
       "qtechCMPortalServerURLEntry": qtechCMPortalServerURLEntry,
       "qtechCMPortalServerURLId": qtechCMPortalServerURLId,
       "qtechCMPortalServerURL": qtechCMPortalServerURL,
       "qtechCMPortalServerName": qtechCMPortalServerName,
       "qtechCMPortalServerInUsedCount": qtechCMPortalServerInUsedCount,
       "qtechCMPortalServerConfigStatus": qtechCMPortalServerConfigStatus,
       "qtechCMPortalHttpReqCount": qtechCMPortalHttpReqCount,
       "qtechCMPortalHttpRespCount": qtechCMPortalHttpRespCount,
       "qtechCMPortalExceptionFailCount": qtechCMPortalExceptionFailCount,
       "qtechCMPortalAuthSuccessedCount": qtechCMPortalAuthSuccessedCount,
       "qtechCMPortalNormalAuthReqCount": qtechCMPortalNormalAuthReqCount,
       "qtechCMPortalEDUAuthReqCount": qtechCMPortalEDUAuthReqCount,
       "qtechCMPortalStarbucksAuthReqCount": qtechCMPortalStarbucksAuthReqCount,
       "qtechCMPortalNormalAuthRespCount": qtechCMPortalNormalAuthRespCount,
       "qtechCMPortalEDUAuthRespCount": qtechCMPortalEDUAuthRespCount,
       "qtechCMPortalStarbucksAuthRespCount": qtechCMPortalStarbucksAuthRespCount,
       "qtechACPortalMaxAuthNum": qtechACPortalMaxAuthNum,
       "qtechACPortalCurrentMaxAuthNum": qtechACPortalCurrentMaxAuthNum,
       "qtechCMPortalMIBConformance": qtechCMPortalMIBConformance,
       "qtechCMPortalMIBCompliances": qtechCMPortalMIBCompliances,
       "qtechCMPortalMIBCompliance": qtechCMPortalMIBCompliance,
       "qtechCMPortalMIBGroups": qtechCMPortalMIBGroups,
       "qtechCMPortalMIBGroup": qtechCMPortalMIBGroup}
)
