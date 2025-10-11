# SNMP MIB module (QTECH-AUTH-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-AUTH-GATEWAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:37 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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

qtechWebAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40)
)
if mibBuilder.loadTexts:
    qtechWebAuthMIB.setRevisions(
        ("2010-03-08 00:00",
         "2010-02-22 00:00",
         "2009-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechWebAuthMIBObjects_ObjectIdentity = ObjectIdentity
qtechWebAuthMIBObjects = _QtechWebAuthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1)
)
_QtechWebAuthUserTable_Object = MibTable
qtechWebAuthUserTable = _QtechWebAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    qtechWebAuthUserTable.setStatus("current")
_QtechWebAuthUserEntry_Object = MibTableRow
qtechWebAuthUserEntry = _QtechWebAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1)
)
qtechWebAuthUserEntry.setIndexNames(
    (0, "QTECH-AUTH-GATEWAY-MIB", "authUserIpAddr"),
)
if mibBuilder.loadTexts:
    qtechWebAuthUserEntry.setStatus("current")
_AuthUserIpAddr_Type = IpAddress
_AuthUserIpAddr_Object = MibTableColumn
authUserIpAddr = _AuthUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 1),
    _AuthUserIpAddr_Type()
)
authUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserIpAddr.setStatus("current")
_AuthUserOnlineFlag_Type = Gauge32
_AuthUserOnlineFlag_Object = MibTableColumn
authUserOnlineFlag = _AuthUserOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 2),
    _AuthUserOnlineFlag_Type()
)
authUserOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserOnlineFlag.setStatus("current")
_AuthUserTimeLimit_Type = Gauge32
_AuthUserTimeLimit_Object = MibTableColumn
authUserTimeLimit = _AuthUserTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 3),
    _AuthUserTimeLimit_Type()
)
authUserTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserTimeLimit.setStatus("current")
_AuthUserTimeUsed_Type = Gauge32
_AuthUserTimeUsed_Object = MibTableColumn
authUserTimeUsed = _AuthUserTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 4),
    _AuthUserTimeUsed_Type()
)
authUserTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserTimeUsed.setStatus("current")
_AuthUserStatus_Type = RowStatus
_AuthUserStatus_Object = MibTableColumn
authUserStatus = _AuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 21),
    _AuthUserSecZoneName_Type()
)
authUserSecZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserSecZoneName.setStatus("current")
_AuthUserSecZonePermissionType_Type = Gauge32
_AuthUserSecZonePermissionType_Object = MibTableColumn
authUserSecZonePermissionType = _AuthUserSecZonePermissionType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 23),
    _AuthUserSecZonePermissionList_Type()
)
authUserSecZonePermissionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserSecZonePermissionList.setStatus("current")
_AuthUserOtherPermissionType_Type = Gauge32
_AuthUserOtherPermissionType_Object = MibTableColumn
authUserOtherPermissionType = _AuthUserOtherPermissionType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 24),
    _AuthUserOtherPermissionType_Type()
)
authUserOtherPermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserOtherPermissionType.setStatus("current")
_AuthUserTerminateCause_Type = Gauge32
_AuthUserTerminateCause_Object = MibTableColumn
authUserTerminateCause = _AuthUserTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 1, 1, 25),
    _AuthUserTerminateCause_Type()
)
authUserTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserTerminateCause.setStatus("current")
_QtechWebAuthUserExtTable_Object = MibTable
qtechWebAuthUserExtTable = _QtechWebAuthUserExtTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2)
)
if mibBuilder.loadTexts:
    qtechWebAuthUserExtTable.setStatus("current")
_QtechWebAuthUserExtEntry_Object = MibTableRow
qtechWebAuthUserExtEntry = _QtechWebAuthUserExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1)
)
qtechWebAuthUserExtEntry.setIndexNames(
    (0, "QTECH-AUTH-GATEWAY-MIB", "authUserExtAddrType"),
    (0, "QTECH-AUTH-GATEWAY-MIB", "authUserExtAddr"),
)
if mibBuilder.loadTexts:
    qtechWebAuthUserExtEntry.setStatus("current")
_AuthUserExtAddrType_Type = InetAddressType
_AuthUserExtAddrType_Object = MibTableColumn
authUserExtAddrType = _AuthUserExtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 2),
    _AuthUserExtAddr_Type()
)
authUserExtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtAddr.setStatus("current")
_AuthUserExtMac_Type = MacAddress
_AuthUserExtMac_Object = MibTableColumn
authUserExtMac = _AuthUserExtMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 3),
    _AuthUserExtMac_Type()
)
authUserExtMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtMac.setStatus("current")
_AuthUserExtIfIndex_Type = IfIndex
_AuthUserExtIfIndex_Object = MibTableColumn
authUserExtIfIndex = _AuthUserExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 4),
    _AuthUserExtIfIndex_Type()
)
authUserExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtIfIndex.setStatus("current")
_AuthUserExtVlanId_Type = Unsigned32
_AuthUserExtVlanId_Object = MibTableColumn
authUserExtVlanId = _AuthUserExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 5),
    _AuthUserExtVlanId_Type()
)
authUserExtVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtVlanId.setStatus("current")
_AuthUserExtOnlineFlag_Type = Gauge32
_AuthUserExtOnlineFlag_Object = MibTableColumn
authUserExtOnlineFlag = _AuthUserExtOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 6),
    _AuthUserExtOnlineFlag_Type()
)
authUserExtOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtOnlineFlag.setStatus("current")
_AuthUserExtTimeLimit_Type = Gauge32
_AuthUserExtTimeLimit_Object = MibTableColumn
authUserExtTimeLimit = _AuthUserExtTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 7),
    _AuthUserExtTimeLimit_Type()
)
authUserExtTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserExtTimeLimit.setStatus("current")
_AuthUserExtTimeUsed_Type = Gauge32
_AuthUserExtTimeUsed_Object = MibTableColumn
authUserExtTimeUsed = _AuthUserExtTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 9),
    _AuthUserExtErrCause_Type()
)
authUserExtErrCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtErrCause.setStatus("current")
_AuthUserExtStatus_Type = RowStatus
_AuthUserExtStatus_Object = MibTableColumn
authUserExtStatus = _AuthUserExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 2, 1, 10),
    _AuthUserExtStatus_Type()
)
authUserExtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserExtStatus.setStatus("current")
_QtechWebAuthWhiteListTable_Object = MibTable
qtechWebAuthWhiteListTable = _QtechWebAuthWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3)
)
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListTable.setStatus("current")
_QtechWebAuthWhiteListEntry_Object = MibTableRow
qtechWebAuthWhiteListEntry = _QtechWebAuthWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1)
)
qtechWebAuthWhiteListEntry.setIndexNames(
    (0, "QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListAddress"),
    (0, "QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListNetMask"),
)
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListEntry.setStatus("current")
_QtechWebAuthWhiteListAddress_Type = IpAddress
_QtechWebAuthWhiteListAddress_Object = MibTableColumn
qtechWebAuthWhiteListAddress = _QtechWebAuthWhiteListAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 1),
    _QtechWebAuthWhiteListAddress_Type()
)
qtechWebAuthWhiteListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListAddress.setStatus("current")
_QtechWebAuthWhiteListNetMask_Type = IpAddress
_QtechWebAuthWhiteListNetMask_Object = MibTableColumn
qtechWebAuthWhiteListNetMask = _QtechWebAuthWhiteListNetMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 2),
    _QtechWebAuthWhiteListNetMask_Type()
)
qtechWebAuthWhiteListNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListNetMask.setStatus("current")
_QtechWebAuthWhiteListPort1_Type = Unsigned32
_QtechWebAuthWhiteListPort1_Object = MibTableColumn
qtechWebAuthWhiteListPort1 = _QtechWebAuthWhiteListPort1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 3),
    _QtechWebAuthWhiteListPort1_Type()
)
qtechWebAuthWhiteListPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListPort1.setStatus("current")
_QtechWebAuthWhiteListPort2_Type = Unsigned32
_QtechWebAuthWhiteListPort2_Object = MibTableColumn
qtechWebAuthWhiteListPort2 = _QtechWebAuthWhiteListPort2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 4),
    _QtechWebAuthWhiteListPort2_Type()
)
qtechWebAuthWhiteListPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListPort2.setStatus("current")
_QtechWebAuthWhiteListPort3_Type = Unsigned32
_QtechWebAuthWhiteListPort3_Object = MibTableColumn
qtechWebAuthWhiteListPort3 = _QtechWebAuthWhiteListPort3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 5),
    _QtechWebAuthWhiteListPort3_Type()
)
qtechWebAuthWhiteListPort3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListPort3.setStatus("current")
_QtechWebAuthWhiteListPort4_Type = Unsigned32
_QtechWebAuthWhiteListPort4_Object = MibTableColumn
qtechWebAuthWhiteListPort4 = _QtechWebAuthWhiteListPort4_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 6),
    _QtechWebAuthWhiteListPort4_Type()
)
qtechWebAuthWhiteListPort4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListPort4.setStatus("current")
_QtechWebAuthWhiteListPort5_Type = Unsigned32
_QtechWebAuthWhiteListPort5_Object = MibTableColumn
qtechWebAuthWhiteListPort5 = _QtechWebAuthWhiteListPort5_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 7),
    _QtechWebAuthWhiteListPort5_Type()
)
qtechWebAuthWhiteListPort5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListPort5.setStatus("current")
_QtechWebAuthWhiteListPort6_Type = Unsigned32
_QtechWebAuthWhiteListPort6_Object = MibTableColumn
qtechWebAuthWhiteListPort6 = _QtechWebAuthWhiteListPort6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 8),
    _QtechWebAuthWhiteListPort6_Type()
)
qtechWebAuthWhiteListPort6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListPort6.setStatus("current")
_QtechWebAuthWhiteListPort7_Type = Unsigned32
_QtechWebAuthWhiteListPort7_Object = MibTableColumn
qtechWebAuthWhiteListPort7 = _QtechWebAuthWhiteListPort7_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 9),
    _QtechWebAuthWhiteListPort7_Type()
)
qtechWebAuthWhiteListPort7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListPort7.setStatus("current")
_QtechWebAuthWhiteListPort8_Type = Unsigned32
_QtechWebAuthWhiteListPort8_Object = MibTableColumn
qtechWebAuthWhiteListPort8 = _QtechWebAuthWhiteListPort8_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 10),
    _QtechWebAuthWhiteListPort8_Type()
)
qtechWebAuthWhiteListPort8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListPort8.setStatus("current")


class _QtechWebAuthWhiteListBindArpFlag_Type(Integer32):
    """Custom type qtechWebAuthWhiteListBindArpFlag based on Integer32"""
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


_QtechWebAuthWhiteListBindArpFlag_Type.__name__ = "Integer32"
_QtechWebAuthWhiteListBindArpFlag_Object = MibTableColumn
qtechWebAuthWhiteListBindArpFlag = _QtechWebAuthWhiteListBindArpFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 11),
    _QtechWebAuthWhiteListBindArpFlag_Type()
)
qtechWebAuthWhiteListBindArpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListBindArpFlag.setStatus("current")
_QtechWebAuthWhiteListStatus_Type = RowStatus
_QtechWebAuthWhiteListStatus_Object = MibTableColumn
qtechWebAuthWhiteListStatus = _QtechWebAuthWhiteListStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 3, 1, 12),
    _QtechWebAuthWhiteListStatus_Type()
)
qtechWebAuthWhiteListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWebAuthWhiteListStatus.setStatus("current")
_QtechWebAuthSDGUserTable_Object = MibTable
qtechWebAuthSDGUserTable = _QtechWebAuthSDGUserTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4)
)
if mibBuilder.loadTexts:
    qtechWebAuthSDGUserTable.setStatus("current")
_QtechWebAuthSDGUserEntry_Object = MibTableRow
qtechWebAuthSDGUserEntry = _QtechWebAuthSDGUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1)
)
qtechWebAuthSDGUserEntry.setIndexNames(
    (0, "QTECH-AUTH-GATEWAY-MIB", "authSDGUserVrfg"),
    (0, "QTECH-AUTH-GATEWAY-MIB", "authSDGUserIpAddr"),
)
if mibBuilder.loadTexts:
    qtechWebAuthSDGUserEntry.setStatus("current")


class _AuthSDGUserVrfg_Type(DisplayString):
    """Custom type authSDGUserVrfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AuthSDGUserVrfg_Type.__name__ = "DisplayString"
_AuthSDGUserVrfg_Object = MibTableColumn
authSDGUserVrfg = _AuthSDGUserVrfg_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 1),
    _AuthSDGUserVrfg_Type()
)
authSDGUserVrfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserVrfg.setStatus("current")
_AuthSDGUserIpAddr_Type = IpAddress
_AuthSDGUserIpAddr_Object = MibTableColumn
authSDGUserIpAddr = _AuthSDGUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 2),
    _AuthSDGUserIpAddr_Type()
)
authSDGUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserIpAddr.setStatus("current")
_AuthSDGUserOnlineFlag_Type = Gauge32
_AuthSDGUserOnlineFlag_Object = MibTableColumn
authSDGUserOnlineFlag = _AuthSDGUserOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 3),
    _AuthSDGUserOnlineFlag_Type()
)
authSDGUserOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserOnlineFlag.setStatus("current")
_AuthSDGUserTimeLimit_Type = Gauge32
_AuthSDGUserTimeLimit_Object = MibTableColumn
authSDGUserTimeLimit = _AuthSDGUserTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 4),
    _AuthSDGUserTimeLimit_Type()
)
authSDGUserTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserTimeLimit.setStatus("current")
_AuthSDGUserTimeUsed_Type = Gauge32
_AuthSDGUserTimeUsed_Object = MibTableColumn
authSDGUserTimeUsed = _AuthSDGUserTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 5),
    _AuthSDGUserTimeUsed_Type()
)
authSDGUserTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserTimeUsed.setStatus("current")
_AuthSDGUserVrf_Type = DisplayString
_AuthSDGUserVrf_Object = MibTableColumn
authSDGUserVrf = _AuthSDGUserVrf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 22),
    _AuthSDGUserSecZoneName_Type()
)
authSDGUserSecZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserSecZoneName.setStatus("current")
_AuthSDGUserSecZonePermissionType_Type = Gauge32
_AuthSDGUserSecZonePermissionType_Object = MibTableColumn
authSDGUserSecZonePermissionType = _AuthSDGUserSecZonePermissionType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 24),
    _AuthSDGUserSecZonePermissionList_Type()
)
authSDGUserSecZonePermissionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserSecZonePermissionList.setStatus("current")
_AuthSDGUserOtherPermissionType_Type = Gauge32
_AuthSDGUserOtherPermissionType_Object = MibTableColumn
authSDGUserOtherPermissionType = _AuthSDGUserOtherPermissionType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 25),
    _AuthSDGUserOtherPermissionType_Type()
)
authSDGUserOtherPermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserOtherPermissionType.setStatus("current")
_AuthSDGUserTerminateCause_Type = Gauge32
_AuthSDGUserTerminateCause_Object = MibTableColumn
authSDGUserTerminateCause = _AuthSDGUserTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 26),
    _AuthSDGUserTerminateCause_Type()
)
authSDGUserTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserTerminateCause.setStatus("current")
_AuthSDGUserStatus_Type = RowStatus
_AuthSDGUserStatus_Object = MibTableColumn
authSDGUserStatus = _AuthSDGUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 4, 1, 27),
    _AuthSDGUserStatus_Type()
)
authSDGUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserStatus.setStatus("current")
_QtechWebAuthMacUserTable_Object = MibTable
qtechWebAuthMacUserTable = _QtechWebAuthMacUserTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 5)
)
if mibBuilder.loadTexts:
    qtechWebAuthMacUserTable.setStatus("current")
_QtechWebAuthMacUserEntry_Object = MibTableRow
qtechWebAuthMacUserEntry = _QtechWebAuthMacUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 5, 1)
)
qtechWebAuthMacUserEntry.setIndexNames(
    (0, "QTECH-AUTH-GATEWAY-MIB", "qtechAuthMacUserMacAddr"),
)
if mibBuilder.loadTexts:
    qtechWebAuthMacUserEntry.setStatus("current")
_QtechAuthMacUserMacAddr_Type = MacAddress
_QtechAuthMacUserMacAddr_Object = MibTableColumn
qtechAuthMacUserMacAddr = _QtechAuthMacUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 5, 1, 1),
    _QtechAuthMacUserMacAddr_Type()
)
qtechAuthMacUserMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthMacUserMacAddr.setStatus("current")


class _QtechAuthMacUserName_Type(OctetString):
    """Custom type qtechAuthMacUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(253, 253),
    )
    fixed_length = 253


_QtechAuthMacUserName_Type.__name__ = "OctetString"
_QtechAuthMacUserName_Object = MibTableColumn
qtechAuthMacUserName = _QtechAuthMacUserName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 5, 1, 2),
    _QtechAuthMacUserName_Type()
)
qtechAuthMacUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthMacUserName.setStatus("current")


class _QtechAuthMacUserTerminalId_Type(OctetString):
    """Custom type qtechAuthMacUserTerminalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(253, 253),
    )
    fixed_length = 253


_QtechAuthMacUserTerminalId_Type.__name__ = "OctetString"
_QtechAuthMacUserTerminalId_Object = MibTableColumn
qtechAuthMacUserTerminalId = _QtechAuthMacUserTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 5, 1, 3),
    _QtechAuthMacUserTerminalId_Type()
)
qtechAuthMacUserTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthMacUserTerminalId.setStatus("current")
_QtechWebAuthUserMIB_ObjectIdentity = ObjectIdentity
qtechWebAuthUserMIB = _QtechWebAuthUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6)
)
_QtechWebAuthUserMIBTable_Object = MibTable
qtechWebAuthUserMIBTable = _QtechWebAuthUserMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6, 1)
)
if mibBuilder.loadTexts:
    qtechWebAuthUserMIBTable.setStatus("current")
_QtechWebAuthUserMIBEntry_Object = MibTableRow
qtechWebAuthUserMIBEntry = _QtechWebAuthUserMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6, 1, 1)
)
qtechWebAuthUserMIBEntry.setIndexNames(
    (0, "QTECH-AUTH-GATEWAY-MIB", "qtechAuthUserMIBIpAddress"),
)
if mibBuilder.loadTexts:
    qtechWebAuthUserMIBEntry.setStatus("current")
_QtechAuthUserMIBIpAddress_Type = IpAddress
_QtechAuthUserMIBIpAddress_Object = MibTableColumn
qtechAuthUserMIBIpAddress = _QtechAuthUserMIBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6, 1, 1, 1),
    _QtechAuthUserMIBIpAddress_Type()
)
qtechAuthUserMIBIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserMIBIpAddress.setStatus("current")
_QtechAuthUserMIBName_Type = OctetString
_QtechAuthUserMIBName_Object = MibTableColumn
qtechAuthUserMIBName = _QtechAuthUserMIBName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6, 1, 1, 2),
    _QtechAuthUserMIBName_Type()
)
qtechAuthUserMIBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserMIBName.setStatus("current")
_QtechAuthUserMIBAuthType_Type = Gauge32
_QtechAuthUserMIBAuthType_Object = MibTableColumn
qtechAuthUserMIBAuthType = _QtechAuthUserMIBAuthType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6, 1, 1, 3),
    _QtechAuthUserMIBAuthType_Type()
)
qtechAuthUserMIBAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserMIBAuthType.setStatus("current")
_QtechAuthUserMIBMacAddress_Type = MacAddress
_QtechAuthUserMIBMacAddress_Object = MibTableColumn
qtechAuthUserMIBMacAddress = _QtechAuthUserMIBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6, 1, 1, 4),
    _QtechAuthUserMIBMacAddress_Type()
)
qtechAuthUserMIBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserMIBMacAddress.setStatus("current")
_QtechAuthUserMIBVlanId_Type = Gauge32
_QtechAuthUserMIBVlanId_Object = MibTableColumn
qtechAuthUserMIBVlanId = _QtechAuthUserMIBVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6, 1, 1, 5),
    _QtechAuthUserMIBVlanId_Type()
)
qtechAuthUserMIBVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserMIBVlanId.setStatus("current")
_QtechAuthUserMIBPortIndex_Type = Gauge32
_QtechAuthUserMIBPortIndex_Object = MibTableColumn
qtechAuthUserMIBPortIndex = _QtechAuthUserMIBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6, 1, 1, 6),
    _QtechAuthUserMIBPortIndex_Type()
)
qtechAuthUserMIBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserMIBPortIndex.setStatus("current")
_QtechAuthUserMIBTimeUsed_Type = Gauge32
_QtechAuthUserMIBTimeUsed_Object = MibTableColumn
qtechAuthUserMIBTimeUsed = _QtechAuthUserMIBTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 1, 6, 1, 1, 7),
    _QtechAuthUserMIBTimeUsed_Type()
)
qtechAuthUserMIBTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthUserMIBTimeUsed.setStatus("current")
_QtechWebAuthMIBTraps_ObjectIdentity = ObjectIdentity
qtechWebAuthMIBTraps = _QtechWebAuthMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 2)
)
_QtechWebAuthMIBConformance_ObjectIdentity = ObjectIdentity
qtechWebAuthMIBConformance = _QtechWebAuthMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 3)
)
_QtechWebAuthMIBCompliances_ObjectIdentity = ObjectIdentity
qtechWebAuthMIBCompliances = _QtechWebAuthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 3, 1)
)
_QtechWebAuthMIBGroups_ObjectIdentity = ObjectIdentity
qtechWebAuthMIBGroups = _QtechWebAuthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 3, 2)
)
_QtechWebAuthMIBTrapsObjects_ObjectIdentity = ObjectIdentity
qtechWebAuthMIBTrapsObjects = _QtechWebAuthMIBTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4)
)
_QtechWebAuthApMac_Type = MacAddress
_QtechWebAuthApMac_Object = MibScalar
qtechWebAuthApMac = _QtechWebAuthApMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 1),
    _QtechWebAuthApMac_Type()
)
qtechWebAuthApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthApMac.setStatus("current")
_QtechWebAuthApIp_Type = IpAddress
_QtechWebAuthApIp_Object = MibScalar
qtechWebAuthApIp = _QtechWebAuthApIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 2),
    _QtechWebAuthApIp_Type()
)
qtechWebAuthApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthApIp.setStatus("current")
_QtechWebAuthStaMac_Type = MacAddress
_QtechWebAuthStaMac_Object = MibScalar
qtechWebAuthStaMac = _QtechWebAuthStaMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 3),
    _QtechWebAuthStaMac_Type()
)
qtechWebAuthStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaMac.setStatus("current")
_QtechWebAuthStaIp_Type = IpAddress
_QtechWebAuthStaIp_Object = MibScalar
qtechWebAuthStaIp = _QtechWebAuthStaIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 4),
    _QtechWebAuthStaIp_Type()
)
qtechWebAuthStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaIp.setStatus("current")
_QtechWebAuthStaIpv6_Type = InetAddress
_QtechWebAuthStaIpv6_Object = MibScalar
qtechWebAuthStaIpv6 = _QtechWebAuthStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 5),
    _QtechWebAuthStaIpv6_Type()
)
qtechWebAuthStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaIpv6.setStatus("current")


class _QtechWebAuthStaOperType_Type(Integer32):
    """Custom type qtechWebAuthStaOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_QtechWebAuthStaOperType_Type.__name__ = "Integer32"
_QtechWebAuthStaOperType_Object = MibScalar
qtechWebAuthStaOperType = _QtechWebAuthStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 6),
    _QtechWebAuthStaOperType_Type()
)
qtechWebAuthStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaOperType.setStatus("current")


class _QtechWebAuthStaApRadioId_Type(Integer32):
    """Custom type qtechWebAuthStaApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechWebAuthStaApRadioId_Type.__name__ = "Integer32"
_QtechWebAuthStaApRadioId_Object = MibScalar
qtechWebAuthStaApRadioId = _QtechWebAuthStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 7),
    _QtechWebAuthStaApRadioId_Type()
)
qtechWebAuthStaApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaApRadioId.setStatus("current")


class _QtechWebAuthStaApRadioType_Type(Integer32):
    """Custom type qtechWebAuthStaApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechWebAuthStaApRadioType_Type.__name__ = "Integer32"
_QtechWebAuthStaApRadioType_Object = MibScalar
qtechWebAuthStaApRadioType = _QtechWebAuthStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 8),
    _QtechWebAuthStaApRadioType_Type()
)
qtechWebAuthStaApRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaApRadioType.setStatus("current")


class _QtechWebAuthStaVlanId_Type(Integer32):
    """Custom type qtechWebAuthStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechWebAuthStaVlanId_Type.__name__ = "Integer32"
_QtechWebAuthStaVlanId_Object = MibScalar
qtechWebAuthStaVlanId = _QtechWebAuthStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 9),
    _QtechWebAuthStaVlanId_Type()
)
qtechWebAuthStaVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaVlanId.setStatus("current")


class _QtechWebAuthStaWlanId_Type(Integer32):
    """Custom type qtechWebAuthStaWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_QtechWebAuthStaWlanId_Type.__name__ = "Integer32"
_QtechWebAuthStaWlanId_Object = MibScalar
qtechWebAuthStaWlanId = _QtechWebAuthStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 10),
    _QtechWebAuthStaWlanId_Type()
)
qtechWebAuthStaWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaWlanId.setStatus("current")
_QtechWebAuthOperTime_Type = TimeTicks
_QtechWebAuthOperTime_Object = MibScalar
qtechWebAuthOperTime = _QtechWebAuthOperTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 11),
    _QtechWebAuthOperTime_Type()
)
qtechWebAuthOperTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthOperTime.setStatus("current")


class _QtechWebAuthStaAssoAuthMode_Type(Integer32):
    """Custom type qtechWebAuthStaAssoAuthMode based on Integer32"""
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


_QtechWebAuthStaAssoAuthMode_Type.__name__ = "Integer32"
_QtechWebAuthStaAssoAuthMode_Object = MibScalar
qtechWebAuthStaAssoAuthMode = _QtechWebAuthStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 12),
    _QtechWebAuthStaAssoAuthMode_Type()
)
qtechWebAuthStaAssoAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaAssoAuthMode.setStatus("current")


class _QtechWebAuthStaNetAuthMode_Type(Integer32):
    """Custom type qtechWebAuthStaNetAuthMode based on Integer32"""
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


_QtechWebAuthStaNetAuthMode_Type.__name__ = "Integer32"
_QtechWebAuthStaNetAuthMode_Object = MibScalar
qtechWebAuthStaNetAuthMode = _QtechWebAuthStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 13),
    _QtechWebAuthStaNetAuthMode_Type()
)
qtechWebAuthStaNetAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaNetAuthMode.setStatus("current")
_QtechWebAuthStaRssi_Type = Integer32
_QtechWebAuthStaRssi_Object = MibScalar
qtechWebAuthStaRssi = _QtechWebAuthStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 14),
    _QtechWebAuthStaRssi_Type()
)
qtechWebAuthStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaRssi.setStatus("current")
_QtechWebAuthStaSsid_Type = DisplayString
_QtechWebAuthStaSsid_Object = MibScalar
qtechWebAuthStaSsid = _QtechWebAuthStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 15),
    _QtechWebAuthStaSsid_Type()
)
qtechWebAuthStaSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaSsid.setStatus("current")
_QtechWebAuthStaLinkRate_Type = Integer32
_QtechWebAuthStaLinkRate_Object = MibScalar
qtechWebAuthStaLinkRate = _QtechWebAuthStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 16),
    _QtechWebAuthStaLinkRate_Type()
)
qtechWebAuthStaLinkRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaLinkRate.setStatus("current")
_QtechWebAuthStaCurChannel_Type = Integer32
_QtechWebAuthStaCurChannel_Object = MibScalar
qtechWebAuthStaCurChannel = _QtechWebAuthStaCurChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 17),
    _QtechWebAuthStaCurChannel_Type()
)
qtechWebAuthStaCurChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaCurChannel.setStatus("current")


class _QtechWebAuthStaUsername_Type(DisplayString):
    """Custom type qtechWebAuthStaUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechWebAuthStaUsername_Type.__name__ = "DisplayString"
_QtechWebAuthStaUsername_Object = MibScalar
qtechWebAuthStaUsername = _QtechWebAuthStaUsername_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 18),
    _QtechWebAuthStaUsername_Type()
)
qtechWebAuthStaUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaUsername.setStatus("current")
_QtechWebAuthStaTerminalType_Type = DisplayString
_QtechWebAuthStaTerminalType_Object = MibScalar
qtechWebAuthStaTerminalType = _QtechWebAuthStaTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 19),
    _QtechWebAuthStaTerminalType_Type()
)
qtechWebAuthStaTerminalType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaTerminalType.setStatus("current")
_QtechWebAuthStaTerminateCause_Type = Integer32
_QtechWebAuthStaTerminateCause_Object = MibScalar
qtechWebAuthStaTerminateCause = _QtechWebAuthStaTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 20),
    _QtechWebAuthStaTerminateCause_Type()
)
qtechWebAuthStaTerminateCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaTerminateCause.setStatus("current")
_QtechWebAuthStaReplyMessage_Type = DisplayString
_QtechWebAuthStaReplyMessage_Object = MibScalar
qtechWebAuthStaReplyMessage = _QtechWebAuthStaReplyMessage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 21),
    _QtechWebAuthStaReplyMessage_Type()
)
qtechWebAuthStaReplyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaReplyMessage.setStatus("current")
_QtechWebAuthStaTerminalId_Type = DisplayString
_QtechWebAuthStaTerminalId_Object = MibScalar
qtechWebAuthStaTerminalId = _QtechWebAuthStaTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 22),
    _QtechWebAuthStaTerminalId_Type()
)
qtechWebAuthStaTerminalId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthStaTerminalId.setStatus("current")


class _QtechWebAuthType_Type(Integer32):
    """Custom type qtechWebAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechWebAuthType_Type.__name__ = "Integer32"
_QtechWebAuthType_Object = MibScalar
qtechWebAuthType = _QtechWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 23),
    _QtechWebAuthType_Type()
)
qtechWebAuthType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthType.setStatus("current")
_QtechWebAuthPortIndex_Type = Integer32
_QtechWebAuthPortIndex_Object = MibScalar
qtechWebAuthPortIndex = _QtechWebAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 4, 24),
    _QtechWebAuthPortIndex_Type()
)
qtechWebAuthPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWebAuthPortIndex.setStatus("current")

# Managed Objects groups

qtechWebAuthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 3, 2, 1)
)
qtechWebAuthMIBGroup.setObjects(
      *(("QTECH-AUTH-GATEWAY-MIB", "authUserIpAddr"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserOnlineFlag"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserTimeLimit"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserTimeUsed"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserStatus"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserRoleName"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserSecZoneName"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserSecZonePermissionType"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserSecZonePermissionList"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserOtherPermissionType"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserTerminateCause"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtAddrType"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtAddr"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtMac"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtIfIndex"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtVlanId"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtOnlineFlag"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtTimeLimit"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtTimeUsed"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtErrCause"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtStatus"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListAddress"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListNetMask"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListPort1"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListPort2"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListPort3"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListPort4"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListPort5"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListPort6"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListPort7"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListPort8"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListBindArpFlag"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthWhiteListStatus"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserVrfg"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserIpAddr"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserOnlineFlag"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserTimeLimit"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserTimeUsed"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserVrf"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserRoleName"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserSecZoneName"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserSecZonePermissionType"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserSecZonePermissionList"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserOtherPermissionType"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserTerminateCause"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserStatus"))
)
if mibBuilder.loadTexts:
    qtechWebAuthMIBGroup.setStatus("current")


# Notification objects

qtechWebAuthUserLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 2, 1)
)
qtechWebAuthUserLeave.setObjects(
      *(("QTECH-AUTH-GATEWAY-MIB", "authUserIpAddr"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserTimeUsed"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserTerminateCause"))
)
if mibBuilder.loadTexts:
    qtechWebAuthUserLeave.setStatus(
        "current"
    )

qtechWebAuthUserExtLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 2, 2)
)
qtechWebAuthUserExtLeave.setObjects(
      *(("QTECH-AUTH-GATEWAY-MIB", "authUserExtAddrType"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtAddr"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtMac"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtIfIndex"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtVlanId"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtTimeUsed"),
        ("QTECH-AUTH-GATEWAY-MIB", "authUserExtErrCause"))
)
if mibBuilder.loadTexts:
    qtechWebAuthUserExtLeave.setStatus(
        "current"
    )

qtechWebAuthSDGUserLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 2, 3)
)
qtechWebAuthSDGUserLeave.setObjects(
      *(("QTECH-AUTH-GATEWAY-MIB", "authSDGUserVrfg"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserIpAddr"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserTimeUsed"),
        ("QTECH-AUTH-GATEWAY-MIB", "authSDGUserTerminateCause"))
)
if mibBuilder.loadTexts:
    qtechWebAuthSDGUserLeave.setStatus(
        "current"
    )

qtechWebAuthWlanMgmt = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 2, 4)
)
qtechWebAuthWlanMgmt.setObjects(
      *(("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthApMac"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthApIp"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaMac"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaIp"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaIpv6"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaOperType"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaApRadioId"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaApRadioType"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaVlanId"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaWlanId"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthOperTime"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaAssoAuthMode"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaNetAuthMode"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaRssi"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaSsid"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaLinkRate"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaCurChannel"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaUsername"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaTerminalType"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaTerminateCause"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaReplyMessage"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaTerminalId"))
)
if mibBuilder.loadTexts:
    qtechWebAuthWlanMgmt.setStatus(
        "current"
    )

qtechWebAuthUserOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 2, 5)
)
qtechWebAuthUserOper.setObjects(
      *(("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaOperType"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthType"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaUsername"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaIp"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaMac"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaVlanId"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthPortIndex"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthStaTerminateCause"))
)
if mibBuilder.loadTexts:
    qtechWebAuthUserOper.setStatus(
        "current"
    )


# Notifications groups

qtechWebAuthTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 3, 2, 2)
)
qtechWebAuthTrapGroup.setObjects(
      *(("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthUserLeave"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthUserExtLeave"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthSDGUserLeave"))
)
if mibBuilder.loadTexts:
    qtechWebAuthTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechWebAuthMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 40, 3, 1, 1)
)
qtechWebAuthMIBCompliance.setObjects(
      *(("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthMIBGroup"),
        ("QTECH-AUTH-GATEWAY-MIB", "qtechWebAuthTrapGroup"))
)
if mibBuilder.loadTexts:
    qtechWebAuthMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-AUTH-GATEWAY-MIB",
    **{"qtechWebAuthMIB": qtechWebAuthMIB,
       "qtechWebAuthMIBObjects": qtechWebAuthMIBObjects,
       "qtechWebAuthUserTable": qtechWebAuthUserTable,
       "qtechWebAuthUserEntry": qtechWebAuthUserEntry,
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
       "qtechWebAuthUserExtTable": qtechWebAuthUserExtTable,
       "qtechWebAuthUserExtEntry": qtechWebAuthUserExtEntry,
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
       "qtechWebAuthWhiteListTable": qtechWebAuthWhiteListTable,
       "qtechWebAuthWhiteListEntry": qtechWebAuthWhiteListEntry,
       "qtechWebAuthWhiteListAddress": qtechWebAuthWhiteListAddress,
       "qtechWebAuthWhiteListNetMask": qtechWebAuthWhiteListNetMask,
       "qtechWebAuthWhiteListPort1": qtechWebAuthWhiteListPort1,
       "qtechWebAuthWhiteListPort2": qtechWebAuthWhiteListPort2,
       "qtechWebAuthWhiteListPort3": qtechWebAuthWhiteListPort3,
       "qtechWebAuthWhiteListPort4": qtechWebAuthWhiteListPort4,
       "qtechWebAuthWhiteListPort5": qtechWebAuthWhiteListPort5,
       "qtechWebAuthWhiteListPort6": qtechWebAuthWhiteListPort6,
       "qtechWebAuthWhiteListPort7": qtechWebAuthWhiteListPort7,
       "qtechWebAuthWhiteListPort8": qtechWebAuthWhiteListPort8,
       "qtechWebAuthWhiteListBindArpFlag": qtechWebAuthWhiteListBindArpFlag,
       "qtechWebAuthWhiteListStatus": qtechWebAuthWhiteListStatus,
       "qtechWebAuthSDGUserTable": qtechWebAuthSDGUserTable,
       "qtechWebAuthSDGUserEntry": qtechWebAuthSDGUserEntry,
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
       "qtechWebAuthMacUserTable": qtechWebAuthMacUserTable,
       "qtechWebAuthMacUserEntry": qtechWebAuthMacUserEntry,
       "qtechAuthMacUserMacAddr": qtechAuthMacUserMacAddr,
       "qtechAuthMacUserName": qtechAuthMacUserName,
       "qtechAuthMacUserTerminalId": qtechAuthMacUserTerminalId,
       "qtechWebAuthUserMIB": qtechWebAuthUserMIB,
       "qtechWebAuthUserMIBTable": qtechWebAuthUserMIBTable,
       "qtechWebAuthUserMIBEntry": qtechWebAuthUserMIBEntry,
       "qtechAuthUserMIBIpAddress": qtechAuthUserMIBIpAddress,
       "qtechAuthUserMIBName": qtechAuthUserMIBName,
       "qtechAuthUserMIBAuthType": qtechAuthUserMIBAuthType,
       "qtechAuthUserMIBMacAddress": qtechAuthUserMIBMacAddress,
       "qtechAuthUserMIBVlanId": qtechAuthUserMIBVlanId,
       "qtechAuthUserMIBPortIndex": qtechAuthUserMIBPortIndex,
       "qtechAuthUserMIBTimeUsed": qtechAuthUserMIBTimeUsed,
       "qtechWebAuthMIBTraps": qtechWebAuthMIBTraps,
       "qtechWebAuthUserLeave": qtechWebAuthUserLeave,
       "qtechWebAuthUserExtLeave": qtechWebAuthUserExtLeave,
       "qtechWebAuthSDGUserLeave": qtechWebAuthSDGUserLeave,
       "qtechWebAuthWlanMgmt": qtechWebAuthWlanMgmt,
       "qtechWebAuthUserOper": qtechWebAuthUserOper,
       "qtechWebAuthMIBConformance": qtechWebAuthMIBConformance,
       "qtechWebAuthMIBCompliances": qtechWebAuthMIBCompliances,
       "qtechWebAuthMIBCompliance": qtechWebAuthMIBCompliance,
       "qtechWebAuthMIBGroups": qtechWebAuthMIBGroups,
       "qtechWebAuthMIBGroup": qtechWebAuthMIBGroup,
       "qtechWebAuthTrapGroup": qtechWebAuthTrapGroup,
       "qtechWebAuthMIBTrapsObjects": qtechWebAuthMIBTrapsObjects,
       "qtechWebAuthApMac": qtechWebAuthApMac,
       "qtechWebAuthApIp": qtechWebAuthApIp,
       "qtechWebAuthStaMac": qtechWebAuthStaMac,
       "qtechWebAuthStaIp": qtechWebAuthStaIp,
       "qtechWebAuthStaIpv6": qtechWebAuthStaIpv6,
       "qtechWebAuthStaOperType": qtechWebAuthStaOperType,
       "qtechWebAuthStaApRadioId": qtechWebAuthStaApRadioId,
       "qtechWebAuthStaApRadioType": qtechWebAuthStaApRadioType,
       "qtechWebAuthStaVlanId": qtechWebAuthStaVlanId,
       "qtechWebAuthStaWlanId": qtechWebAuthStaWlanId,
       "qtechWebAuthOperTime": qtechWebAuthOperTime,
       "qtechWebAuthStaAssoAuthMode": qtechWebAuthStaAssoAuthMode,
       "qtechWebAuthStaNetAuthMode": qtechWebAuthStaNetAuthMode,
       "qtechWebAuthStaRssi": qtechWebAuthStaRssi,
       "qtechWebAuthStaSsid": qtechWebAuthStaSsid,
       "qtechWebAuthStaLinkRate": qtechWebAuthStaLinkRate,
       "qtechWebAuthStaCurChannel": qtechWebAuthStaCurChannel,
       "qtechWebAuthStaUsername": qtechWebAuthStaUsername,
       "qtechWebAuthStaTerminalType": qtechWebAuthStaTerminalType,
       "qtechWebAuthStaTerminateCause": qtechWebAuthStaTerminateCause,
       "qtechWebAuthStaReplyMessage": qtechWebAuthStaReplyMessage,
       "qtechWebAuthStaTerminalId": qtechWebAuthStaTerminalId,
       "qtechWebAuthType": qtechWebAuthType,
       "qtechWebAuthPortIndex": qtechWebAuthPortIndex}
)
