# SNMP MIB module (FS-AUTH-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-AUTH-GATEWAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:38 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

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

fsWebAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40)
)
if mibBuilder.loadTexts:
    fsWebAuthMIB.setRevisions(
        ("2010-03-08 00:00",
         "2010-02-22 00:00",
         "2009-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsWebAuthMIBObjects_ObjectIdentity = ObjectIdentity
fsWebAuthMIBObjects = _FsWebAuthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1)
)
_FsWebAuthUserTable_Object = MibTable
fsWebAuthUserTable = _FsWebAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    fsWebAuthUserTable.setStatus("current")
_FsWebAuthUserEntry_Object = MibTableRow
fsWebAuthUserEntry = _FsWebAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1)
)
fsWebAuthUserEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "authUserIpAddr"),
)
if mibBuilder.loadTexts:
    fsWebAuthUserEntry.setStatus("current")
_AuthUserIpAddr_Type = IpAddress
_AuthUserIpAddr_Object = MibTableColumn
authUserIpAddr = _AuthUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 1),
    _AuthUserIpAddr_Type()
)
authUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserIpAddr.setStatus("current")
_AuthUserOnlineFlag_Type = Gauge32
_AuthUserOnlineFlag_Object = MibTableColumn
authUserOnlineFlag = _AuthUserOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 2),
    _AuthUserOnlineFlag_Type()
)
authUserOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserOnlineFlag.setStatus("current")
_AuthUserTimeLimit_Type = Gauge32
_AuthUserTimeLimit_Object = MibTableColumn
authUserTimeLimit = _AuthUserTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 3),
    _AuthUserTimeLimit_Type()
)
authUserTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserTimeLimit.setStatus("current")
_AuthUserTimeUsed_Type = Gauge32
_AuthUserTimeUsed_Object = MibTableColumn
authUserTimeUsed = _AuthUserTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 4),
    _AuthUserTimeUsed_Type()
)
authUserTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserTimeUsed.setStatus("current")
_AuthUserStatus_Type = RowStatus
_AuthUserStatus_Object = MibTableColumn
authUserStatus = _AuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 19),
    _AuthUserStatus_Type()
)
authUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserStatus.setStatus("current")


class _AuthUserRoleName_Type(OctetString):
    """Custom type authUserRoleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_AuthUserRoleName_Type.__name__ = "OctetString"
_AuthUserRoleName_Object = MibTableColumn
authUserRoleName = _AuthUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 20),
    _AuthUserRoleName_Type()
)
authUserRoleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserRoleName.setStatus("current")


class _AuthUserSecZoneName_Type(OctetString):
    """Custom type authUserSecZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_AuthUserSecZoneName_Type.__name__ = "OctetString"
_AuthUserSecZoneName_Object = MibTableColumn
authUserSecZoneName = _AuthUserSecZoneName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 21),
    _AuthUserSecZoneName_Type()
)
authUserSecZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserSecZoneName.setStatus("current")
_AuthUserSecZonePermissionType_Type = Gauge32
_AuthUserSecZonePermissionType_Object = MibTableColumn
authUserSecZonePermissionType = _AuthUserSecZonePermissionType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 22),
    _AuthUserSecZonePermissionType_Type()
)
authUserSecZonePermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserSecZonePermissionType.setStatus("current")


class _AuthUserSecZonePermissionList_Type(OctetString):
    """Custom type authUserSecZonePermissionList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_AuthUserSecZonePermissionList_Type.__name__ = "OctetString"
_AuthUserSecZonePermissionList_Object = MibTableColumn
authUserSecZonePermissionList = _AuthUserSecZonePermissionList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 23),
    _AuthUserSecZonePermissionList_Type()
)
authUserSecZonePermissionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserSecZonePermissionList.setStatus("current")
_AuthUserOtherPermissionType_Type = Gauge32
_AuthUserOtherPermissionType_Object = MibTableColumn
authUserOtherPermissionType = _AuthUserOtherPermissionType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 24),
    _AuthUserOtherPermissionType_Type()
)
authUserOtherPermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserOtherPermissionType.setStatus("current")
_AuthUserTerminateCause_Type = Gauge32
_AuthUserTerminateCause_Object = MibTableColumn
authUserTerminateCause = _AuthUserTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 1, 1, 25),
    _AuthUserTerminateCause_Type()
)
authUserTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserTerminateCause.setStatus("current")
_FsWebAuthUserExtTable_Object = MibTable
fsWebAuthUserExtTable = _FsWebAuthUserExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2)
)
if mibBuilder.loadTexts:
    fsWebAuthUserExtTable.setStatus("current")
_FsWebAuthUserExtEntry_Object = MibTableRow
fsWebAuthUserExtEntry = _FsWebAuthUserExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1)
)
fsWebAuthUserExtEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "authUserExtAddrType"),
    (0, "FS-AUTH-GATEWAY-MIB", "authUserExtAddr"),
)
if mibBuilder.loadTexts:
    fsWebAuthUserExtEntry.setStatus("current")
_AuthUserExtAddrType_Type = InetAddressType
_AuthUserExtAddrType_Object = MibTableColumn
authUserExtAddrType = _AuthUserExtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 1),
    _AuthUserExtAddrType_Type()
)
authUserExtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtAddrType.setStatus("current")


class _AuthUserExtAddr_Type(InetAddress):
    """Custom type authUserExtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AuthUserExtAddr_Type.__name__ = "InetAddress"
_AuthUserExtAddr_Object = MibTableColumn
authUserExtAddr = _AuthUserExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 2),
    _AuthUserExtAddr_Type()
)
authUserExtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtAddr.setStatus("current")
_AuthUserExtMac_Type = MacAddress
_AuthUserExtMac_Object = MibTableColumn
authUserExtMac = _AuthUserExtMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 3),
    _AuthUserExtMac_Type()
)
authUserExtMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtMac.setStatus("current")
_AuthUserExtIfIndex_Type = IfIndex
_AuthUserExtIfIndex_Object = MibTableColumn
authUserExtIfIndex = _AuthUserExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 4),
    _AuthUserExtIfIndex_Type()
)
authUserExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtIfIndex.setStatus("current")
_AuthUserExtVlanId_Type = Unsigned32
_AuthUserExtVlanId_Object = MibTableColumn
authUserExtVlanId = _AuthUserExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 5),
    _AuthUserExtVlanId_Type()
)
authUserExtVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtVlanId.setStatus("current")
_AuthUserExtOnlineFlag_Type = Gauge32
_AuthUserExtOnlineFlag_Object = MibTableColumn
authUserExtOnlineFlag = _AuthUserExtOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 6),
    _AuthUserExtOnlineFlag_Type()
)
authUserExtOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtOnlineFlag.setStatus("current")
_AuthUserExtTimeLimit_Type = Gauge32
_AuthUserExtTimeLimit_Object = MibTableColumn
authUserExtTimeLimit = _AuthUserExtTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 7),
    _AuthUserExtTimeLimit_Type()
)
authUserExtTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserExtTimeLimit.setStatus("current")
_AuthUserExtTimeUsed_Type = Gauge32
_AuthUserExtTimeUsed_Object = MibTableColumn
authUserExtTimeUsed = _AuthUserExtTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 8),
    _AuthUserExtTimeUsed_Type()
)
authUserExtTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtTimeUsed.setStatus("current")


class _AuthUserExtErrCause_Type(DisplayString):
    """Custom type authUserExtErrCause based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AuthUserExtErrCause_Type.__name__ = "DisplayString"
_AuthUserExtErrCause_Object = MibTableColumn
authUserExtErrCause = _AuthUserExtErrCause_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 9),
    _AuthUserExtErrCause_Type()
)
authUserExtErrCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtErrCause.setStatus("current")
_AuthUserExtStatus_Type = RowStatus
_AuthUserExtStatus_Object = MibTableColumn
authUserExtStatus = _AuthUserExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 2, 1, 10),
    _AuthUserExtStatus_Type()
)
authUserExtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserExtStatus.setStatus("current")
_FsWebAuthWhiteListTable_Object = MibTable
fsWebAuthWhiteListTable = _FsWebAuthWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3)
)
if mibBuilder.loadTexts:
    fsWebAuthWhiteListTable.setStatus("current")
_FsWebAuthWhiteListEntry_Object = MibTableRow
fsWebAuthWhiteListEntry = _FsWebAuthWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1)
)
fsWebAuthWhiteListEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListAddress"),
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListNetMask"),
)
if mibBuilder.loadTexts:
    fsWebAuthWhiteListEntry.setStatus("current")
_FsWebAuthWhiteListAddress_Type = IpAddress
_FsWebAuthWhiteListAddress_Object = MibTableColumn
fsWebAuthWhiteListAddress = _FsWebAuthWhiteListAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 1),
    _FsWebAuthWhiteListAddress_Type()
)
fsWebAuthWhiteListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListAddress.setStatus("current")
_FsWebAuthWhiteListNetMask_Type = IpAddress
_FsWebAuthWhiteListNetMask_Object = MibTableColumn
fsWebAuthWhiteListNetMask = _FsWebAuthWhiteListNetMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 2),
    _FsWebAuthWhiteListNetMask_Type()
)
fsWebAuthWhiteListNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListNetMask.setStatus("current")
_FsWebAuthWhiteListPort1_Type = Unsigned32
_FsWebAuthWhiteListPort1_Object = MibTableColumn
fsWebAuthWhiteListPort1 = _FsWebAuthWhiteListPort1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 3),
    _FsWebAuthWhiteListPort1_Type()
)
fsWebAuthWhiteListPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListPort1.setStatus("current")
_FsWebAuthWhiteListPort2_Type = Unsigned32
_FsWebAuthWhiteListPort2_Object = MibTableColumn
fsWebAuthWhiteListPort2 = _FsWebAuthWhiteListPort2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 4),
    _FsWebAuthWhiteListPort2_Type()
)
fsWebAuthWhiteListPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListPort2.setStatus("current")
_FsWebAuthWhiteListPort3_Type = Unsigned32
_FsWebAuthWhiteListPort3_Object = MibTableColumn
fsWebAuthWhiteListPort3 = _FsWebAuthWhiteListPort3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 5),
    _FsWebAuthWhiteListPort3_Type()
)
fsWebAuthWhiteListPort3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListPort3.setStatus("current")
_FsWebAuthWhiteListPort4_Type = Unsigned32
_FsWebAuthWhiteListPort4_Object = MibTableColumn
fsWebAuthWhiteListPort4 = _FsWebAuthWhiteListPort4_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 6),
    _FsWebAuthWhiteListPort4_Type()
)
fsWebAuthWhiteListPort4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListPort4.setStatus("current")
_FsWebAuthWhiteListPort5_Type = Unsigned32
_FsWebAuthWhiteListPort5_Object = MibTableColumn
fsWebAuthWhiteListPort5 = _FsWebAuthWhiteListPort5_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 7),
    _FsWebAuthWhiteListPort5_Type()
)
fsWebAuthWhiteListPort5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListPort5.setStatus("current")
_FsWebAuthWhiteListPort6_Type = Unsigned32
_FsWebAuthWhiteListPort6_Object = MibTableColumn
fsWebAuthWhiteListPort6 = _FsWebAuthWhiteListPort6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 8),
    _FsWebAuthWhiteListPort6_Type()
)
fsWebAuthWhiteListPort6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListPort6.setStatus("current")
_FsWebAuthWhiteListPort7_Type = Unsigned32
_FsWebAuthWhiteListPort7_Object = MibTableColumn
fsWebAuthWhiteListPort7 = _FsWebAuthWhiteListPort7_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 9),
    _FsWebAuthWhiteListPort7_Type()
)
fsWebAuthWhiteListPort7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListPort7.setStatus("current")
_FsWebAuthWhiteListPort8_Type = Unsigned32
_FsWebAuthWhiteListPort8_Object = MibTableColumn
fsWebAuthWhiteListPort8 = _FsWebAuthWhiteListPort8_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 10),
    _FsWebAuthWhiteListPort8_Type()
)
fsWebAuthWhiteListPort8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListPort8.setStatus("current")


class _FsWebAuthWhiteListBindArpFlag_Type(Integer32):
    """Custom type fsWebAuthWhiteListBindArpFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsWebAuthWhiteListBindArpFlag_Type.__name__ = "Integer32"
_FsWebAuthWhiteListBindArpFlag_Object = MibTableColumn
fsWebAuthWhiteListBindArpFlag = _FsWebAuthWhiteListBindArpFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 11),
    _FsWebAuthWhiteListBindArpFlag_Type()
)
fsWebAuthWhiteListBindArpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListBindArpFlag.setStatus("current")
_FsWebAuthWhiteListStatus_Type = RowStatus
_FsWebAuthWhiteListStatus_Object = MibTableColumn
fsWebAuthWhiteListStatus = _FsWebAuthWhiteListStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 3, 1, 12),
    _FsWebAuthWhiteListStatus_Type()
)
fsWebAuthWhiteListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthWhiteListStatus.setStatus("current")
_FsWebAuthSDGUserTable_Object = MibTable
fsWebAuthSDGUserTable = _FsWebAuthSDGUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4)
)
if mibBuilder.loadTexts:
    fsWebAuthSDGUserTable.setStatus("current")
_FsWebAuthSDGUserEntry_Object = MibTableRow
fsWebAuthSDGUserEntry = _FsWebAuthSDGUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1)
)
fsWebAuthSDGUserEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "authSDGUserVrfg"),
    (0, "FS-AUTH-GATEWAY-MIB", "authSDGUserIpAddr"),
)
if mibBuilder.loadTexts:
    fsWebAuthSDGUserEntry.setStatus("current")


class _AuthSDGUserVrfg_Type(DisplayString):
    """Custom type authSDGUserVrfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AuthSDGUserVrfg_Type.__name__ = "DisplayString"
_AuthSDGUserVrfg_Object = MibTableColumn
authSDGUserVrfg = _AuthSDGUserVrfg_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 1),
    _AuthSDGUserVrfg_Type()
)
authSDGUserVrfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserVrfg.setStatus("current")
_AuthSDGUserIpAddr_Type = IpAddress
_AuthSDGUserIpAddr_Object = MibTableColumn
authSDGUserIpAddr = _AuthSDGUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 2),
    _AuthSDGUserIpAddr_Type()
)
authSDGUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserIpAddr.setStatus("current")
_AuthSDGUserOnlineFlag_Type = Gauge32
_AuthSDGUserOnlineFlag_Object = MibTableColumn
authSDGUserOnlineFlag = _AuthSDGUserOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 3),
    _AuthSDGUserOnlineFlag_Type()
)
authSDGUserOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserOnlineFlag.setStatus("current")
_AuthSDGUserTimeLimit_Type = Gauge32
_AuthSDGUserTimeLimit_Object = MibTableColumn
authSDGUserTimeLimit = _AuthSDGUserTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 4),
    _AuthSDGUserTimeLimit_Type()
)
authSDGUserTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserTimeLimit.setStatus("current")
_AuthSDGUserTimeUsed_Type = Gauge32
_AuthSDGUserTimeUsed_Object = MibTableColumn
authSDGUserTimeUsed = _AuthSDGUserTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 5),
    _AuthSDGUserTimeUsed_Type()
)
authSDGUserTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserTimeUsed.setStatus("current")
_AuthSDGUserVrf_Type = DisplayString
_AuthSDGUserVrf_Object = MibTableColumn
authSDGUserVrf = _AuthSDGUserVrf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 6),
    _AuthSDGUserVrf_Type()
)
authSDGUserVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserVrf.setStatus("current")


class _AuthSDGUserRoleName_Type(OctetString):
    """Custom type authSDGUserRoleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_AuthSDGUserRoleName_Type.__name__ = "OctetString"
_AuthSDGUserRoleName_Object = MibTableColumn
authSDGUserRoleName = _AuthSDGUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 21),
    _AuthSDGUserRoleName_Type()
)
authSDGUserRoleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserRoleName.setStatus("current")


class _AuthSDGUserSecZoneName_Type(OctetString):
    """Custom type authSDGUserSecZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_AuthSDGUserSecZoneName_Type.__name__ = "OctetString"
_AuthSDGUserSecZoneName_Object = MibTableColumn
authSDGUserSecZoneName = _AuthSDGUserSecZoneName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 22),
    _AuthSDGUserSecZoneName_Type()
)
authSDGUserSecZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserSecZoneName.setStatus("current")
_AuthSDGUserSecZonePermissionType_Type = Gauge32
_AuthSDGUserSecZonePermissionType_Object = MibTableColumn
authSDGUserSecZonePermissionType = _AuthSDGUserSecZonePermissionType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 23),
    _AuthSDGUserSecZonePermissionType_Type()
)
authSDGUserSecZonePermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserSecZonePermissionType.setStatus("current")


class _AuthSDGUserSecZonePermissionList_Type(OctetString):
    """Custom type authSDGUserSecZonePermissionList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_AuthSDGUserSecZonePermissionList_Type.__name__ = "OctetString"
_AuthSDGUserSecZonePermissionList_Object = MibTableColumn
authSDGUserSecZonePermissionList = _AuthSDGUserSecZonePermissionList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 24),
    _AuthSDGUserSecZonePermissionList_Type()
)
authSDGUserSecZonePermissionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserSecZonePermissionList.setStatus("current")
_AuthSDGUserOtherPermissionType_Type = Gauge32
_AuthSDGUserOtherPermissionType_Object = MibTableColumn
authSDGUserOtherPermissionType = _AuthSDGUserOtherPermissionType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 25),
    _AuthSDGUserOtherPermissionType_Type()
)
authSDGUserOtherPermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserOtherPermissionType.setStatus("current")
_AuthSDGUserTerminateCause_Type = Gauge32
_AuthSDGUserTerminateCause_Object = MibTableColumn
authSDGUserTerminateCause = _AuthSDGUserTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 26),
    _AuthSDGUserTerminateCause_Type()
)
authSDGUserTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserTerminateCause.setStatus("current")
_AuthSDGUserStatus_Type = RowStatus
_AuthSDGUserStatus_Object = MibTableColumn
authSDGUserStatus = _AuthSDGUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 4, 1, 27),
    _AuthSDGUserStatus_Type()
)
authSDGUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserStatus.setStatus("current")
_FsWebAuthMacUserTable_Object = MibTable
fsWebAuthMacUserTable = _FsWebAuthMacUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 5)
)
if mibBuilder.loadTexts:
    fsWebAuthMacUserTable.setStatus("current")
_FsWebAuthMacUserEntry_Object = MibTableRow
fsWebAuthMacUserEntry = _FsWebAuthMacUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 5, 1)
)
fsWebAuthMacUserEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "fsAuthMacUserMacAddr"),
)
if mibBuilder.loadTexts:
    fsWebAuthMacUserEntry.setStatus("current")
_FsAuthMacUserMacAddr_Type = MacAddress
_FsAuthMacUserMacAddr_Object = MibTableColumn
fsAuthMacUserMacAddr = _FsAuthMacUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 5, 1, 1),
    _FsAuthMacUserMacAddr_Type()
)
fsAuthMacUserMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthMacUserMacAddr.setStatus("current")


class _FsAuthMacUserName_Type(OctetString):
    """Custom type fsAuthMacUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(253, 253),
    )
    fixed_length = 253


_FsAuthMacUserName_Type.__name__ = "OctetString"
_FsAuthMacUserName_Object = MibTableColumn
fsAuthMacUserName = _FsAuthMacUserName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 5, 1, 2),
    _FsAuthMacUserName_Type()
)
fsAuthMacUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthMacUserName.setStatus("current")


class _FsAuthMacUserTerminalId_Type(OctetString):
    """Custom type fsAuthMacUserTerminalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(253, 253),
    )
    fixed_length = 253


_FsAuthMacUserTerminalId_Type.__name__ = "OctetString"
_FsAuthMacUserTerminalId_Object = MibTableColumn
fsAuthMacUserTerminalId = _FsAuthMacUserTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 5, 1, 3),
    _FsAuthMacUserTerminalId_Type()
)
fsAuthMacUserTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthMacUserTerminalId.setStatus("current")
_FsWebAuthUserMIB_ObjectIdentity = ObjectIdentity
fsWebAuthUserMIB = _FsWebAuthUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6)
)
_FsWebAuthUserMIBTable_Object = MibTable
fsWebAuthUserMIBTable = _FsWebAuthUserMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fsWebAuthUserMIBTable.setStatus("current")
_FsWebAuthUserMIBEntry_Object = MibTableRow
fsWebAuthUserMIBEntry = _FsWebAuthUserMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6, 1, 1)
)
fsWebAuthUserMIBEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "fsAuthUserMIBIpAddress"),
)
if mibBuilder.loadTexts:
    fsWebAuthUserMIBEntry.setStatus("current")
_FsAuthUserMIBIpAddress_Type = IpAddress
_FsAuthUserMIBIpAddress_Object = MibTableColumn
fsAuthUserMIBIpAddress = _FsAuthUserMIBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6, 1, 1, 1),
    _FsAuthUserMIBIpAddress_Type()
)
fsAuthUserMIBIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserMIBIpAddress.setStatus("current")
_FsAuthUserMIBName_Type = OctetString
_FsAuthUserMIBName_Object = MibTableColumn
fsAuthUserMIBName = _FsAuthUserMIBName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6, 1, 1, 2),
    _FsAuthUserMIBName_Type()
)
fsAuthUserMIBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserMIBName.setStatus("current")
_FsAuthUserMIBAuthType_Type = Gauge32
_FsAuthUserMIBAuthType_Object = MibTableColumn
fsAuthUserMIBAuthType = _FsAuthUserMIBAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6, 1, 1, 3),
    _FsAuthUserMIBAuthType_Type()
)
fsAuthUserMIBAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserMIBAuthType.setStatus("current")
_FsAuthUserMIBMacAddress_Type = MacAddress
_FsAuthUserMIBMacAddress_Object = MibTableColumn
fsAuthUserMIBMacAddress = _FsAuthUserMIBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6, 1, 1, 4),
    _FsAuthUserMIBMacAddress_Type()
)
fsAuthUserMIBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserMIBMacAddress.setStatus("current")
_FsAuthUserMIBVlanId_Type = Gauge32
_FsAuthUserMIBVlanId_Object = MibTableColumn
fsAuthUserMIBVlanId = _FsAuthUserMIBVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6, 1, 1, 5),
    _FsAuthUserMIBVlanId_Type()
)
fsAuthUserMIBVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserMIBVlanId.setStatus("current")
_FsAuthUserMIBPortIndex_Type = Gauge32
_FsAuthUserMIBPortIndex_Object = MibTableColumn
fsAuthUserMIBPortIndex = _FsAuthUserMIBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6, 1, 1, 6),
    _FsAuthUserMIBPortIndex_Type()
)
fsAuthUserMIBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserMIBPortIndex.setStatus("current")
_FsAuthUserMIBTimeUsed_Type = Gauge32
_FsAuthUserMIBTimeUsed_Object = MibTableColumn
fsAuthUserMIBTimeUsed = _FsAuthUserMIBTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 6, 1, 1, 7),
    _FsAuthUserMIBTimeUsed_Type()
)
fsAuthUserMIBTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserMIBTimeUsed.setStatus("current")
_FsWebAuthDirectSiteTable_Object = MibTable
fsWebAuthDirectSiteTable = _FsWebAuthDirectSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 7)
)
if mibBuilder.loadTexts:
    fsWebAuthDirectSiteTable.setStatus("current")
_FsWebAuthDirectSiteEntry_Object = MibTableRow
fsWebAuthDirectSiteEntry = _FsWebAuthDirectSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 7, 1)
)
fsWebAuthDirectSiteEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectSiteAddress"),
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectSiteNetMask"),
)
if mibBuilder.loadTexts:
    fsWebAuthDirectSiteEntry.setStatus("current")
_FsWebAuthDirectSiteAddress_Type = IpAddress
_FsWebAuthDirectSiteAddress_Object = MibTableColumn
fsWebAuthDirectSiteAddress = _FsWebAuthDirectSiteAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 7, 1, 1),
    _FsWebAuthDirectSiteAddress_Type()
)
fsWebAuthDirectSiteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthDirectSiteAddress.setStatus("current")
_FsWebAuthDirectSiteNetMask_Type = IpAddress
_FsWebAuthDirectSiteNetMask_Object = MibTableColumn
fsWebAuthDirectSiteNetMask = _FsWebAuthDirectSiteNetMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 7, 1, 2),
    _FsWebAuthDirectSiteNetMask_Type()
)
fsWebAuthDirectSiteNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthDirectSiteNetMask.setStatus("current")
_FsWebAuthDirectSiteStatus_Type = RowStatus
_FsWebAuthDirectSiteStatus_Object = MibTableColumn
fsWebAuthDirectSiteStatus = _FsWebAuthDirectSiteStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 7, 1, 3),
    _FsWebAuthDirectSiteStatus_Type()
)
fsWebAuthDirectSiteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectSiteStatus.setStatus("current")


class _FsWebAuthDirectSiteBindArpFlag_Type(Integer32):
    """Custom type fsWebAuthDirectSiteBindArpFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsWebAuthDirectSiteBindArpFlag_Type.__name__ = "Integer32"
_FsWebAuthDirectSiteBindArpFlag_Object = MibTableColumn
fsWebAuthDirectSiteBindArpFlag = _FsWebAuthDirectSiteBindArpFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 7, 1, 4),
    _FsWebAuthDirectSiteBindArpFlag_Type()
)
fsWebAuthDirectSiteBindArpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectSiteBindArpFlag.setStatus("current")
_FsWebAuthDirectHostTable_Object = MibTable
fsWebAuthDirectHostTable = _FsWebAuthDirectHostTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8)
)
if mibBuilder.loadTexts:
    fsWebAuthDirectHostTable.setStatus("current")
_FsWebAuthDirectHostEntry_Object = MibTableRow
fsWebAuthDirectHostEntry = _FsWebAuthDirectHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1)
)
fsWebAuthDirectHostEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostAddress"),
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostNetMask"),
)
if mibBuilder.loadTexts:
    fsWebAuthDirectHostEntry.setStatus("current")
_FsWebAuthDirectHostAddress_Type = IpAddress
_FsWebAuthDirectHostAddress_Object = MibTableColumn
fsWebAuthDirectHostAddress = _FsWebAuthDirectHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 1),
    _FsWebAuthDirectHostAddress_Type()
)
fsWebAuthDirectHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostAddress.setStatus("current")
_FsWebAuthDirectHostNetMask_Type = IpAddress
_FsWebAuthDirectHostNetMask_Object = MibTableColumn
fsWebAuthDirectHostNetMask = _FsWebAuthDirectHostNetMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 2),
    _FsWebAuthDirectHostNetMask_Type()
)
fsWebAuthDirectHostNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostNetMask.setStatus("current")
_FsWebAuthDirectHostPort1_Type = Unsigned32
_FsWebAuthDirectHostPort1_Object = MibTableColumn
fsWebAuthDirectHostPort1 = _FsWebAuthDirectHostPort1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 3),
    _FsWebAuthDirectHostPort1_Type()
)
fsWebAuthDirectHostPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostPort1.setStatus("current")
_FsWebAuthDirectHostPort2_Type = Unsigned32
_FsWebAuthDirectHostPort2_Object = MibTableColumn
fsWebAuthDirectHostPort2 = _FsWebAuthDirectHostPort2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 4),
    _FsWebAuthDirectHostPort2_Type()
)
fsWebAuthDirectHostPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostPort2.setStatus("current")
_FsWebAuthDirectHostPort3_Type = Unsigned32
_FsWebAuthDirectHostPort3_Object = MibTableColumn
fsWebAuthDirectHostPort3 = _FsWebAuthDirectHostPort3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 5),
    _FsWebAuthDirectHostPort3_Type()
)
fsWebAuthDirectHostPort3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostPort3.setStatus("current")
_FsWebAuthDirectHostPort4_Type = Unsigned32
_FsWebAuthDirectHostPort4_Object = MibTableColumn
fsWebAuthDirectHostPort4 = _FsWebAuthDirectHostPort4_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 6),
    _FsWebAuthDirectHostPort4_Type()
)
fsWebAuthDirectHostPort4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostPort4.setStatus("current")
_FsWebAuthDirectHostPort5_Type = Unsigned32
_FsWebAuthDirectHostPort5_Object = MibTableColumn
fsWebAuthDirectHostPort5 = _FsWebAuthDirectHostPort5_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 7),
    _FsWebAuthDirectHostPort5_Type()
)
fsWebAuthDirectHostPort5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostPort5.setStatus("current")
_FsWebAuthDirectHostPort6_Type = Unsigned32
_FsWebAuthDirectHostPort6_Object = MibTableColumn
fsWebAuthDirectHostPort6 = _FsWebAuthDirectHostPort6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 8),
    _FsWebAuthDirectHostPort6_Type()
)
fsWebAuthDirectHostPort6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostPort6.setStatus("current")
_FsWebAuthDirectHostPort7_Type = Unsigned32
_FsWebAuthDirectHostPort7_Object = MibTableColumn
fsWebAuthDirectHostPort7 = _FsWebAuthDirectHostPort7_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 9),
    _FsWebAuthDirectHostPort7_Type()
)
fsWebAuthDirectHostPort7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostPort7.setStatus("current")
_FsWebAuthDirectHostPort8_Type = Unsigned32
_FsWebAuthDirectHostPort8_Object = MibTableColumn
fsWebAuthDirectHostPort8 = _FsWebAuthDirectHostPort8_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 10),
    _FsWebAuthDirectHostPort8_Type()
)
fsWebAuthDirectHostPort8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostPort8.setStatus("current")


class _FsWebAuthDirectHostBindArpFlag_Type(Integer32):
    """Custom type fsWebAuthDirectHostBindArpFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsWebAuthDirectHostBindArpFlag_Type.__name__ = "Integer32"
_FsWebAuthDirectHostBindArpFlag_Object = MibTableColumn
fsWebAuthDirectHostBindArpFlag = _FsWebAuthDirectHostBindArpFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 11),
    _FsWebAuthDirectHostBindArpFlag_Type()
)
fsWebAuthDirectHostBindArpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostBindArpFlag.setStatus("current")
_FsWebAuthDirectHostStatus_Type = RowStatus
_FsWebAuthDirectHostStatus_Object = MibTableColumn
fsWebAuthDirectHostStatus = _FsWebAuthDirectHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 12),
    _FsWebAuthDirectHostStatus_Type()
)
fsWebAuthDirectHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostStatus.setStatus("current")
_FsWebAuthDirectHostPortIfx_Type = Gauge32
_FsWebAuthDirectHostPortIfx_Object = MibTableColumn
fsWebAuthDirectHostPortIfx = _FsWebAuthDirectHostPortIfx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 8, 1, 13),
    _FsWebAuthDirectHostPortIfx_Type()
)
fsWebAuthDirectHostPortIfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthDirectHostPortIfx.setStatus("current")
_FsWebAuthFreeAcctIpTable_Object = MibTable
fsWebAuthFreeAcctIpTable = _FsWebAuthFreeAcctIpTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 9)
)
if mibBuilder.loadTexts:
    fsWebAuthFreeAcctIpTable.setStatus("current")
_FsWebAuthFreeAcctIpEntry_Object = MibTableRow
fsWebAuthFreeAcctIpEntry = _FsWebAuthFreeAcctIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 9, 1)
)
fsWebAuthFreeAcctIpEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthFreeAcctIpAddress"),
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthFreeAcctIpNetMask"),
)
if mibBuilder.loadTexts:
    fsWebAuthFreeAcctIpEntry.setStatus("current")
_FsWebAuthFreeAcctIpAddress_Type = IpAddress
_FsWebAuthFreeAcctIpAddress_Object = MibTableColumn
fsWebAuthFreeAcctIpAddress = _FsWebAuthFreeAcctIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 9, 1, 1),
    _FsWebAuthFreeAcctIpAddress_Type()
)
fsWebAuthFreeAcctIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthFreeAcctIpAddress.setStatus("current")
_FsWebAuthFreeAcctIpNetMask_Type = IpAddress
_FsWebAuthFreeAcctIpNetMask_Object = MibTableColumn
fsWebAuthFreeAcctIpNetMask = _FsWebAuthFreeAcctIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 9, 1, 2),
    _FsWebAuthFreeAcctIpNetMask_Type()
)
fsWebAuthFreeAcctIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthFreeAcctIpNetMask.setStatus("current")
_FsWebAuthFreeAcctIpStatus_Type = RowStatus
_FsWebAuthFreeAcctIpStatus_Object = MibTableColumn
fsWebAuthFreeAcctIpStatus = _FsWebAuthFreeAcctIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 9, 1, 3),
    _FsWebAuthFreeAcctIpStatus_Type()
)
fsWebAuthFreeAcctIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthFreeAcctIpStatus.setStatus("current")
_FsWebAuthFreeAcctUrlTable_Object = MibTable
fsWebAuthFreeAcctUrlTable = _FsWebAuthFreeAcctUrlTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 10)
)
if mibBuilder.loadTexts:
    fsWebAuthFreeAcctUrlTable.setStatus("current")
_FsWebAuthFreeAcctUrlEntry_Object = MibTableRow
fsWebAuthFreeAcctUrlEntry = _FsWebAuthFreeAcctUrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 10, 1)
)
fsWebAuthFreeAcctUrlEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthFreeAcctUrl"),
)
if mibBuilder.loadTexts:
    fsWebAuthFreeAcctUrlEntry.setStatus("current")
_FsWebAuthFreeAcctUrl_Type = OctetString
_FsWebAuthFreeAcctUrl_Object = MibTableColumn
fsWebAuthFreeAcctUrl = _FsWebAuthFreeAcctUrl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 10, 1, 1),
    _FsWebAuthFreeAcctUrl_Type()
)
fsWebAuthFreeAcctUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthFreeAcctUrl.setStatus("current")
_FsWebAuthFreeAcctUrlStatus_Type = RowStatus
_FsWebAuthFreeAcctUrlStatus_Object = MibTableColumn
fsWebAuthFreeAcctUrlStatus = _FsWebAuthFreeAcctUrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 10, 1, 2),
    _FsWebAuthFreeAcctUrlStatus_Type()
)
fsWebAuthFreeAcctUrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthFreeAcctUrlStatus.setStatus("current")
_FsWebAuthOfflineDetectTable_Object = MibTable
fsWebAuthOfflineDetectTable = _FsWebAuthOfflineDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 11)
)
if mibBuilder.loadTexts:
    fsWebAuthOfflineDetectTable.setStatus("current")
_FsWebAuthOfflineDetectEntry_Object = MibTableRow
fsWebAuthOfflineDetectEntry = _FsWebAuthOfflineDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 11, 1)
)
fsWebAuthOfflineDetectEntry.setIndexNames(
    (0, "FS-AUTH-GATEWAY-MIB", "fsWebAuthOfflineDetectime"),
)
if mibBuilder.loadTexts:
    fsWebAuthOfflineDetectEntry.setStatus("current")
_FsWebAuthOfflineDetectime_Type = Unsigned32
_FsWebAuthOfflineDetectime_Object = MibTableColumn
fsWebAuthOfflineDetectime = _FsWebAuthOfflineDetectime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 11, 1, 1),
    _FsWebAuthOfflineDetectime_Type()
)
fsWebAuthOfflineDetectime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthOfflineDetectime.setStatus("current")
_FsWebAuthOfflineDetectStatus_Type = RowStatus
_FsWebAuthOfflineDetectStatus_Object = MibTableColumn
fsWebAuthOfflineDetectStatus = _FsWebAuthOfflineDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 11, 1, 2),
    _FsWebAuthOfflineDetectStatus_Type()
)
fsWebAuthOfflineDetectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWebAuthOfflineDetectStatus.setStatus("current")
_FsWebAuthCurrentOnlineUser_Type = Integer32
_FsWebAuthCurrentOnlineUser_Object = MibScalar
fsWebAuthCurrentOnlineUser = _FsWebAuthCurrentOnlineUser_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 12),
    _FsWebAuthCurrentOnlineUser_Type()
)
fsWebAuthCurrentOnlineUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthCurrentOnlineUser.setStatus("current")
_FsWebAuthCurrentUser_Type = Integer32
_FsWebAuthCurrentUser_Object = MibScalar
fsWebAuthCurrentUser = _FsWebAuthCurrentUser_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 13),
    _FsWebAuthCurrentUser_Type()
)
fsWebAuthCurrentUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthCurrentUser.setStatus("current")
_FsWebAuthMaximumOnlineUser_Type = Integer32
_FsWebAuthMaximumOnlineUser_Object = MibScalar
fsWebAuthMaximumOnlineUser = _FsWebAuthMaximumOnlineUser_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 1, 14),
    _FsWebAuthMaximumOnlineUser_Type()
)
fsWebAuthMaximumOnlineUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebAuthMaximumOnlineUser.setStatus("current")
_FsWebAuthMIBTraps_ObjectIdentity = ObjectIdentity
fsWebAuthMIBTraps = _FsWebAuthMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 2)
)
_FsWebAuthMIBConformance_ObjectIdentity = ObjectIdentity
fsWebAuthMIBConformance = _FsWebAuthMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 3)
)
_FsWebAuthMIBCompliances_ObjectIdentity = ObjectIdentity
fsWebAuthMIBCompliances = _FsWebAuthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 3, 1)
)
_FsWebAuthMIBGroups_ObjectIdentity = ObjectIdentity
fsWebAuthMIBGroups = _FsWebAuthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 3, 2)
)
_FsWebAuthMIBTrapsObjects_ObjectIdentity = ObjectIdentity
fsWebAuthMIBTrapsObjects = _FsWebAuthMIBTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4)
)
_FsWebAuthApMac_Type = MacAddress
_FsWebAuthApMac_Object = MibScalar
fsWebAuthApMac = _FsWebAuthApMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 1),
    _FsWebAuthApMac_Type()
)
fsWebAuthApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthApMac.setStatus("current")
_FsWebAuthApIp_Type = IpAddress
_FsWebAuthApIp_Object = MibScalar
fsWebAuthApIp = _FsWebAuthApIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 2),
    _FsWebAuthApIp_Type()
)
fsWebAuthApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthApIp.setStatus("current")
_FsWebAuthStaMac_Type = MacAddress
_FsWebAuthStaMac_Object = MibScalar
fsWebAuthStaMac = _FsWebAuthStaMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 3),
    _FsWebAuthStaMac_Type()
)
fsWebAuthStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaMac.setStatus("current")
_FsWebAuthStaIp_Type = IpAddress
_FsWebAuthStaIp_Object = MibScalar
fsWebAuthStaIp = _FsWebAuthStaIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 4),
    _FsWebAuthStaIp_Type()
)
fsWebAuthStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaIp.setStatus("current")
_FsWebAuthStaIpv6_Type = InetAddress
_FsWebAuthStaIpv6_Object = MibScalar
fsWebAuthStaIpv6 = _FsWebAuthStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 5),
    _FsWebAuthStaIpv6_Type()
)
fsWebAuthStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaIpv6.setStatus("current")


class _FsWebAuthStaOperType_Type(Integer32):
    """Custom type fsWebAuthStaOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsWebAuthStaOperType_Type.__name__ = "Integer32"
_FsWebAuthStaOperType_Object = MibScalar
fsWebAuthStaOperType = _FsWebAuthStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 6),
    _FsWebAuthStaOperType_Type()
)
fsWebAuthStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaOperType.setStatus("current")


class _FsWebAuthStaApRadioId_Type(Integer32):
    """Custom type fsWebAuthStaApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsWebAuthStaApRadioId_Type.__name__ = "Integer32"
_FsWebAuthStaApRadioId_Object = MibScalar
fsWebAuthStaApRadioId = _FsWebAuthStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 7),
    _FsWebAuthStaApRadioId_Type()
)
fsWebAuthStaApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaApRadioId.setStatus("current")


class _FsWebAuthStaApRadioType_Type(Integer32):
    """Custom type fsWebAuthStaApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsWebAuthStaApRadioType_Type.__name__ = "Integer32"
_FsWebAuthStaApRadioType_Object = MibScalar
fsWebAuthStaApRadioType = _FsWebAuthStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 8),
    _FsWebAuthStaApRadioType_Type()
)
fsWebAuthStaApRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaApRadioType.setStatus("current")


class _FsWebAuthStaVlanId_Type(Integer32):
    """Custom type fsWebAuthStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsWebAuthStaVlanId_Type.__name__ = "Integer32"
_FsWebAuthStaVlanId_Object = MibScalar
fsWebAuthStaVlanId = _FsWebAuthStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 9),
    _FsWebAuthStaVlanId_Type()
)
fsWebAuthStaVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaVlanId.setStatus("current")


class _FsWebAuthStaWlanId_Type(Integer32):
    """Custom type fsWebAuthStaWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsWebAuthStaWlanId_Type.__name__ = "Integer32"
_FsWebAuthStaWlanId_Object = MibScalar
fsWebAuthStaWlanId = _FsWebAuthStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 10),
    _FsWebAuthStaWlanId_Type()
)
fsWebAuthStaWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaWlanId.setStatus("current")
_FsWebAuthOperTime_Type = TimeTicks
_FsWebAuthOperTime_Object = MibScalar
fsWebAuthOperTime = _FsWebAuthOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 11),
    _FsWebAuthOperTime_Type()
)
fsWebAuthOperTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthOperTime.setStatus("current")


class _FsWebAuthStaAssoAuthMode_Type(Integer32):
    """Custom type fsWebAuthStaAssoAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("wep", 1),
          ("dot1x-wep", 2),
          ("dot1x-wpa", 3),
          ("dot1x-wpa2", 4),
          ("mab", 5),
          ("psk-wpa", 6),
          ("psk-wpa2", 7),
          ("wapi", 8))
    )


_FsWebAuthStaAssoAuthMode_Type.__name__ = "Integer32"
_FsWebAuthStaAssoAuthMode_Object = MibScalar
fsWebAuthStaAssoAuthMode = _FsWebAuthStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 12),
    _FsWebAuthStaAssoAuthMode_Type()
)
fsWebAuthStaAssoAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaAssoAuthMode.setStatus("current")


class _FsWebAuthStaNetAuthMode_Type(Integer32):
    """Custom type fsWebAuthStaNetAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("web", 1))
    )


_FsWebAuthStaNetAuthMode_Type.__name__ = "Integer32"
_FsWebAuthStaNetAuthMode_Object = MibScalar
fsWebAuthStaNetAuthMode = _FsWebAuthStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 13),
    _FsWebAuthStaNetAuthMode_Type()
)
fsWebAuthStaNetAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaNetAuthMode.setStatus("current")
_FsWebAuthStaRssi_Type = Integer32
_FsWebAuthStaRssi_Object = MibScalar
fsWebAuthStaRssi = _FsWebAuthStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 14),
    _FsWebAuthStaRssi_Type()
)
fsWebAuthStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaRssi.setStatus("current")
_FsWebAuthStaSsid_Type = DisplayString
_FsWebAuthStaSsid_Object = MibScalar
fsWebAuthStaSsid = _FsWebAuthStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 15),
    _FsWebAuthStaSsid_Type()
)
fsWebAuthStaSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaSsid.setStatus("current")
_FsWebAuthStaLinkRate_Type = Integer32
_FsWebAuthStaLinkRate_Object = MibScalar
fsWebAuthStaLinkRate = _FsWebAuthStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 16),
    _FsWebAuthStaLinkRate_Type()
)
fsWebAuthStaLinkRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaLinkRate.setStatus("current")
_FsWebAuthStaCurChannel_Type = Integer32
_FsWebAuthStaCurChannel_Object = MibScalar
fsWebAuthStaCurChannel = _FsWebAuthStaCurChannel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 17),
    _FsWebAuthStaCurChannel_Type()
)
fsWebAuthStaCurChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaCurChannel.setStatus("current")


class _FsWebAuthStaUsername_Type(DisplayString):
    """Custom type fsWebAuthStaUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsWebAuthStaUsername_Type.__name__ = "DisplayString"
_FsWebAuthStaUsername_Object = MibScalar
fsWebAuthStaUsername = _FsWebAuthStaUsername_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 18),
    _FsWebAuthStaUsername_Type()
)
fsWebAuthStaUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaUsername.setStatus("current")
_FsWebAuthStaTerminalType_Type = DisplayString
_FsWebAuthStaTerminalType_Object = MibScalar
fsWebAuthStaTerminalType = _FsWebAuthStaTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 19),
    _FsWebAuthStaTerminalType_Type()
)
fsWebAuthStaTerminalType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaTerminalType.setStatus("current")
_FsWebAuthStaTerminateCause_Type = Integer32
_FsWebAuthStaTerminateCause_Object = MibScalar
fsWebAuthStaTerminateCause = _FsWebAuthStaTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 20),
    _FsWebAuthStaTerminateCause_Type()
)
fsWebAuthStaTerminateCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaTerminateCause.setStatus("current")
_FsWebAuthStaReplyMessage_Type = DisplayString
_FsWebAuthStaReplyMessage_Object = MibScalar
fsWebAuthStaReplyMessage = _FsWebAuthStaReplyMessage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 21),
    _FsWebAuthStaReplyMessage_Type()
)
fsWebAuthStaReplyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaReplyMessage.setStatus("current")
_FsWebAuthStaTerminalId_Type = DisplayString
_FsWebAuthStaTerminalId_Object = MibScalar
fsWebAuthStaTerminalId = _FsWebAuthStaTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 22),
    _FsWebAuthStaTerminalId_Type()
)
fsWebAuthStaTerminalId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthStaTerminalId.setStatus("current")


class _FsWebAuthType_Type(Integer32):
    """Custom type fsWebAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsWebAuthType_Type.__name__ = "Integer32"
_FsWebAuthType_Object = MibScalar
fsWebAuthType = _FsWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 23),
    _FsWebAuthType_Type()
)
fsWebAuthType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthType.setStatus("current")
_FsWebAuthPortIndex_Type = Integer32
_FsWebAuthPortIndex_Object = MibScalar
fsWebAuthPortIndex = _FsWebAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 24),
    _FsWebAuthPortIndex_Type()
)
fsWebAuthPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthPortIndex.setStatus("current")
_FsWebAuthTlvNum_Type = Integer32
_FsWebAuthTlvNum_Object = MibScalar
fsWebAuthTlvNum = _FsWebAuthTlvNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 25),
    _FsWebAuthTlvNum_Type()
)
fsWebAuthTlvNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthTlvNum.setStatus("current")
_FsWebAuthTlv_Type = DisplayString
_FsWebAuthTlv_Object = MibScalar
fsWebAuthTlv = _FsWebAuthTlv_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 4, 26),
    _FsWebAuthTlv_Type()
)
fsWebAuthTlv.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWebAuthTlv.setStatus("current")

# Managed Objects groups

fsWebAuthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 3, 2, 1)
)
fsWebAuthMIBGroup.setObjects(
      *(("FS-AUTH-GATEWAY-MIB", "authUserIpAddr"),
        ("FS-AUTH-GATEWAY-MIB", "authUserOnlineFlag"),
        ("FS-AUTH-GATEWAY-MIB", "authUserTimeLimit"),
        ("FS-AUTH-GATEWAY-MIB", "authUserTimeUsed"),
        ("FS-AUTH-GATEWAY-MIB", "authUserStatus"),
        ("FS-AUTH-GATEWAY-MIB", "authUserRoleName"),
        ("FS-AUTH-GATEWAY-MIB", "authUserSecZoneName"),
        ("FS-AUTH-GATEWAY-MIB", "authUserSecZonePermissionType"),
        ("FS-AUTH-GATEWAY-MIB", "authUserSecZonePermissionList"),
        ("FS-AUTH-GATEWAY-MIB", "authUserOtherPermissionType"),
        ("FS-AUTH-GATEWAY-MIB", "authUserTerminateCause"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtAddrType"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtAddr"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtMac"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtIfIndex"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtVlanId"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtOnlineFlag"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtTimeLimit"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtTimeUsed"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtErrCause"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtStatus"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListAddress"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListNetMask"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListPort1"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListPort2"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListPort3"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListPort4"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListPort5"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListPort6"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListPort7"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListPort8"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListBindArpFlag"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthWhiteListStatus"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserVrfg"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserIpAddr"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserOnlineFlag"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserTimeLimit"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserTimeUsed"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserVrf"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserRoleName"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserSecZoneName"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserSecZonePermissionType"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserSecZonePermissionList"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserOtherPermissionType"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserTerminateCause"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserStatus"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectSiteAddress"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectSiteNetMask"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectSiteStatus"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectSiteBindArpFlag"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostAddress"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostNetMask"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostPort1"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostPort2"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostPort3"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostPort4"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostPort5"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostPort6"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostPort7"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostPort8"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostBindArpFlag"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostStatus"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthDirectHostPortIfx"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthFreeAcctIpAddress"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthFreeAcctIpNetMask"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthFreeAcctIpStatus"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthFreeAcctUrl"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthFreeAcctUrlStatus"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthOfflineDetectime"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthOfflineDetectStatus"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthCurrentOnlineUser"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthCurrentUser"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthMaximumOnlineUser"))
)
if mibBuilder.loadTexts:
    fsWebAuthMIBGroup.setStatus("current")


# Notification objects

fsWebAuthUserLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 2, 1)
)
fsWebAuthUserLeave.setObjects(
      *(("FS-AUTH-GATEWAY-MIB", "authUserIpAddr"),
        ("FS-AUTH-GATEWAY-MIB", "authUserTimeUsed"),
        ("FS-AUTH-GATEWAY-MIB", "authUserTerminateCause"))
)
if mibBuilder.loadTexts:
    fsWebAuthUserLeave.setStatus(
        "current"
    )

fsWebAuthUserExtLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 2, 2)
)
fsWebAuthUserExtLeave.setObjects(
      *(("FS-AUTH-GATEWAY-MIB", "authUserExtAddrType"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtAddr"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtMac"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtIfIndex"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtVlanId"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtTimeUsed"),
        ("FS-AUTH-GATEWAY-MIB", "authUserExtErrCause"))
)
if mibBuilder.loadTexts:
    fsWebAuthUserExtLeave.setStatus(
        "current"
    )

fsWebAuthSDGUserLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 2, 3)
)
fsWebAuthSDGUserLeave.setObjects(
      *(("FS-AUTH-GATEWAY-MIB", "authSDGUserVrfg"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserIpAddr"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserTimeUsed"),
        ("FS-AUTH-GATEWAY-MIB", "authSDGUserTerminateCause"))
)
if mibBuilder.loadTexts:
    fsWebAuthSDGUserLeave.setStatus(
        "current"
    )

fsWebAuthWlanMgmt = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 2, 4)
)
fsWebAuthWlanMgmt.setObjects(
      *(("FS-AUTH-GATEWAY-MIB", "fsWebAuthApMac"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthApIp"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaMac"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaIp"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaIpv6"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaOperType"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaApRadioId"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaApRadioType"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaVlanId"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaWlanId"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthOperTime"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaAssoAuthMode"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaNetAuthMode"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaRssi"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaSsid"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaLinkRate"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaCurChannel"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaUsername"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaTerminalType"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaTerminateCause"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaReplyMessage"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaTerminalId"))
)
if mibBuilder.loadTexts:
    fsWebAuthWlanMgmt.setStatus(
        "current"
    )

fsWebAuthUserOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 2, 5)
)
fsWebAuthUserOper.setObjects(
      *(("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaOperType"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthType"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaUsername"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaIp"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaMac"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaVlanId"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthPortIndex"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthStaTerminateCause"))
)
if mibBuilder.loadTexts:
    fsWebAuthUserOper.setStatus(
        "current"
    )

fsWebAuthRedirectInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 2, 6)
)
fsWebAuthRedirectInfo.setObjects(
      *(("FS-AUTH-GATEWAY-MIB", "fsWebAuthTlvNum"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthTlv"))
)
if mibBuilder.loadTexts:
    fsWebAuthRedirectInfo.setStatus(
        "current"
    )


# Notifications groups

fsWebAuthTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 3, 2, 2)
)
fsWebAuthTrapGroup.setObjects(
      *(("FS-AUTH-GATEWAY-MIB", "fsWebAuthUserLeave"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthUserExtLeave"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthSDGUserLeave"))
)
if mibBuilder.loadTexts:
    fsWebAuthTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsWebAuthMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 40, 3, 1, 1)
)
fsWebAuthMIBCompliance.setObjects(
      *(("FS-AUTH-GATEWAY-MIB", "fsWebAuthMIBGroup"),
        ("FS-AUTH-GATEWAY-MIB", "fsWebAuthTrapGroup"))
)
if mibBuilder.loadTexts:
    fsWebAuthMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-AUTH-GATEWAY-MIB",
    **{"fsWebAuthMIB": fsWebAuthMIB,
       "fsWebAuthMIBObjects": fsWebAuthMIBObjects,
       "fsWebAuthUserTable": fsWebAuthUserTable,
       "fsWebAuthUserEntry": fsWebAuthUserEntry,
       "authUserIpAddr": authUserIpAddr,
       "authUserOnlineFlag": authUserOnlineFlag,
       "authUserTimeLimit": authUserTimeLimit,
       "authUserTimeUsed": authUserTimeUsed,
       "authUserStatus": authUserStatus,
       "authUserRoleName": authUserRoleName,
       "authUserSecZoneName": authUserSecZoneName,
       "authUserSecZonePermissionType": authUserSecZonePermissionType,
       "authUserSecZonePermissionList": authUserSecZonePermissionList,
       "authUserOtherPermissionType": authUserOtherPermissionType,
       "authUserTerminateCause": authUserTerminateCause,
       "fsWebAuthUserExtTable": fsWebAuthUserExtTable,
       "fsWebAuthUserExtEntry": fsWebAuthUserExtEntry,
       "authUserExtAddrType": authUserExtAddrType,
       "authUserExtAddr": authUserExtAddr,
       "authUserExtMac": authUserExtMac,
       "authUserExtIfIndex": authUserExtIfIndex,
       "authUserExtVlanId": authUserExtVlanId,
       "authUserExtOnlineFlag": authUserExtOnlineFlag,
       "authUserExtTimeLimit": authUserExtTimeLimit,
       "authUserExtTimeUsed": authUserExtTimeUsed,
       "authUserExtErrCause": authUserExtErrCause,
       "authUserExtStatus": authUserExtStatus,
       "fsWebAuthWhiteListTable": fsWebAuthWhiteListTable,
       "fsWebAuthWhiteListEntry": fsWebAuthWhiteListEntry,
       "fsWebAuthWhiteListAddress": fsWebAuthWhiteListAddress,
       "fsWebAuthWhiteListNetMask": fsWebAuthWhiteListNetMask,
       "fsWebAuthWhiteListPort1": fsWebAuthWhiteListPort1,
       "fsWebAuthWhiteListPort2": fsWebAuthWhiteListPort2,
       "fsWebAuthWhiteListPort3": fsWebAuthWhiteListPort3,
       "fsWebAuthWhiteListPort4": fsWebAuthWhiteListPort4,
       "fsWebAuthWhiteListPort5": fsWebAuthWhiteListPort5,
       "fsWebAuthWhiteListPort6": fsWebAuthWhiteListPort6,
       "fsWebAuthWhiteListPort7": fsWebAuthWhiteListPort7,
       "fsWebAuthWhiteListPort8": fsWebAuthWhiteListPort8,
       "fsWebAuthWhiteListBindArpFlag": fsWebAuthWhiteListBindArpFlag,
       "fsWebAuthWhiteListStatus": fsWebAuthWhiteListStatus,
       "fsWebAuthSDGUserTable": fsWebAuthSDGUserTable,
       "fsWebAuthSDGUserEntry": fsWebAuthSDGUserEntry,
       "authSDGUserVrfg": authSDGUserVrfg,
       "authSDGUserIpAddr": authSDGUserIpAddr,
       "authSDGUserOnlineFlag": authSDGUserOnlineFlag,
       "authSDGUserTimeLimit": authSDGUserTimeLimit,
       "authSDGUserTimeUsed": authSDGUserTimeUsed,
       "authSDGUserVrf": authSDGUserVrf,
       "authSDGUserRoleName": authSDGUserRoleName,
       "authSDGUserSecZoneName": authSDGUserSecZoneName,
       "authSDGUserSecZonePermissionType": authSDGUserSecZonePermissionType,
       "authSDGUserSecZonePermissionList": authSDGUserSecZonePermissionList,
       "authSDGUserOtherPermissionType": authSDGUserOtherPermissionType,
       "authSDGUserTerminateCause": authSDGUserTerminateCause,
       "authSDGUserStatus": authSDGUserStatus,
       "fsWebAuthMacUserTable": fsWebAuthMacUserTable,
       "fsWebAuthMacUserEntry": fsWebAuthMacUserEntry,
       "fsAuthMacUserMacAddr": fsAuthMacUserMacAddr,
       "fsAuthMacUserName": fsAuthMacUserName,
       "fsAuthMacUserTerminalId": fsAuthMacUserTerminalId,
       "fsWebAuthUserMIB": fsWebAuthUserMIB,
       "fsWebAuthUserMIBTable": fsWebAuthUserMIBTable,
       "fsWebAuthUserMIBEntry": fsWebAuthUserMIBEntry,
       "fsAuthUserMIBIpAddress": fsAuthUserMIBIpAddress,
       "fsAuthUserMIBName": fsAuthUserMIBName,
       "fsAuthUserMIBAuthType": fsAuthUserMIBAuthType,
       "fsAuthUserMIBMacAddress": fsAuthUserMIBMacAddress,
       "fsAuthUserMIBVlanId": fsAuthUserMIBVlanId,
       "fsAuthUserMIBPortIndex": fsAuthUserMIBPortIndex,
       "fsAuthUserMIBTimeUsed": fsAuthUserMIBTimeUsed,
       "fsWebAuthDirectSiteTable": fsWebAuthDirectSiteTable,
       "fsWebAuthDirectSiteEntry": fsWebAuthDirectSiteEntry,
       "fsWebAuthDirectSiteAddress": fsWebAuthDirectSiteAddress,
       "fsWebAuthDirectSiteNetMask": fsWebAuthDirectSiteNetMask,
       "fsWebAuthDirectSiteStatus": fsWebAuthDirectSiteStatus,
       "fsWebAuthDirectSiteBindArpFlag": fsWebAuthDirectSiteBindArpFlag,
       "fsWebAuthDirectHostTable": fsWebAuthDirectHostTable,
       "fsWebAuthDirectHostEntry": fsWebAuthDirectHostEntry,
       "fsWebAuthDirectHostAddress": fsWebAuthDirectHostAddress,
       "fsWebAuthDirectHostNetMask": fsWebAuthDirectHostNetMask,
       "fsWebAuthDirectHostPort1": fsWebAuthDirectHostPort1,
       "fsWebAuthDirectHostPort2": fsWebAuthDirectHostPort2,
       "fsWebAuthDirectHostPort3": fsWebAuthDirectHostPort3,
       "fsWebAuthDirectHostPort4": fsWebAuthDirectHostPort4,
       "fsWebAuthDirectHostPort5": fsWebAuthDirectHostPort5,
       "fsWebAuthDirectHostPort6": fsWebAuthDirectHostPort6,
       "fsWebAuthDirectHostPort7": fsWebAuthDirectHostPort7,
       "fsWebAuthDirectHostPort8": fsWebAuthDirectHostPort8,
       "fsWebAuthDirectHostBindArpFlag": fsWebAuthDirectHostBindArpFlag,
       "fsWebAuthDirectHostStatus": fsWebAuthDirectHostStatus,
       "fsWebAuthDirectHostPortIfx": fsWebAuthDirectHostPortIfx,
       "fsWebAuthFreeAcctIpTable": fsWebAuthFreeAcctIpTable,
       "fsWebAuthFreeAcctIpEntry": fsWebAuthFreeAcctIpEntry,
       "fsWebAuthFreeAcctIpAddress": fsWebAuthFreeAcctIpAddress,
       "fsWebAuthFreeAcctIpNetMask": fsWebAuthFreeAcctIpNetMask,
       "fsWebAuthFreeAcctIpStatus": fsWebAuthFreeAcctIpStatus,
       "fsWebAuthFreeAcctUrlTable": fsWebAuthFreeAcctUrlTable,
       "fsWebAuthFreeAcctUrlEntry": fsWebAuthFreeAcctUrlEntry,
       "fsWebAuthFreeAcctUrl": fsWebAuthFreeAcctUrl,
       "fsWebAuthFreeAcctUrlStatus": fsWebAuthFreeAcctUrlStatus,
       "fsWebAuthOfflineDetectTable": fsWebAuthOfflineDetectTable,
       "fsWebAuthOfflineDetectEntry": fsWebAuthOfflineDetectEntry,
       "fsWebAuthOfflineDetectime": fsWebAuthOfflineDetectime,
       "fsWebAuthOfflineDetectStatus": fsWebAuthOfflineDetectStatus,
       "fsWebAuthCurrentOnlineUser": fsWebAuthCurrentOnlineUser,
       "fsWebAuthCurrentUser": fsWebAuthCurrentUser,
       "fsWebAuthMaximumOnlineUser": fsWebAuthMaximumOnlineUser,
       "fsWebAuthMIBTraps": fsWebAuthMIBTraps,
       "fsWebAuthUserLeave": fsWebAuthUserLeave,
       "fsWebAuthUserExtLeave": fsWebAuthUserExtLeave,
       "fsWebAuthSDGUserLeave": fsWebAuthSDGUserLeave,
       "fsWebAuthWlanMgmt": fsWebAuthWlanMgmt,
       "fsWebAuthUserOper": fsWebAuthUserOper,
       "fsWebAuthRedirectInfo": fsWebAuthRedirectInfo,
       "fsWebAuthMIBConformance": fsWebAuthMIBConformance,
       "fsWebAuthMIBCompliances": fsWebAuthMIBCompliances,
       "fsWebAuthMIBCompliance": fsWebAuthMIBCompliance,
       "fsWebAuthMIBGroups": fsWebAuthMIBGroups,
       "fsWebAuthMIBGroup": fsWebAuthMIBGroup,
       "fsWebAuthTrapGroup": fsWebAuthTrapGroup,
       "fsWebAuthMIBTrapsObjects": fsWebAuthMIBTrapsObjects,
       "fsWebAuthApMac": fsWebAuthApMac,
       "fsWebAuthApIp": fsWebAuthApIp,
       "fsWebAuthStaMac": fsWebAuthStaMac,
       "fsWebAuthStaIp": fsWebAuthStaIp,
       "fsWebAuthStaIpv6": fsWebAuthStaIpv6,
       "fsWebAuthStaOperType": fsWebAuthStaOperType,
       "fsWebAuthStaApRadioId": fsWebAuthStaApRadioId,
       "fsWebAuthStaApRadioType": fsWebAuthStaApRadioType,
       "fsWebAuthStaVlanId": fsWebAuthStaVlanId,
       "fsWebAuthStaWlanId": fsWebAuthStaWlanId,
       "fsWebAuthOperTime": fsWebAuthOperTime,
       "fsWebAuthStaAssoAuthMode": fsWebAuthStaAssoAuthMode,
       "fsWebAuthStaNetAuthMode": fsWebAuthStaNetAuthMode,
       "fsWebAuthStaRssi": fsWebAuthStaRssi,
       "fsWebAuthStaSsid": fsWebAuthStaSsid,
       "fsWebAuthStaLinkRate": fsWebAuthStaLinkRate,
       "fsWebAuthStaCurChannel": fsWebAuthStaCurChannel,
       "fsWebAuthStaUsername": fsWebAuthStaUsername,
       "fsWebAuthStaTerminalType": fsWebAuthStaTerminalType,
       "fsWebAuthStaTerminateCause": fsWebAuthStaTerminateCause,
       "fsWebAuthStaReplyMessage": fsWebAuthStaReplyMessage,
       "fsWebAuthStaTerminalId": fsWebAuthStaTerminalId,
       "fsWebAuthType": fsWebAuthType,
       "fsWebAuthPortIndex": fsWebAuthPortIndex,
       "fsWebAuthTlvNum": fsWebAuthTlvNum,
       "fsWebAuthTlv": fsWebAuthTlv}
)
