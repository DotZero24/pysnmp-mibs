# SNMP MIB module (LUM-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:14 2025
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

(lumIpMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIpMIB",
    "lumModules")

(CommandString,
 MgmtNameString) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "MgmtNameString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lumIpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 15)
)
if mibBuilder.loadTexts:
    lumIpMIBModule.setRevisions(
        ("2018-12-20 00:00",
         "2018-05-31 00:00",
         "2017-06-15 00:00",
         "2016-06-14 00:00",
         "2016-01-11 00:00",
         "2013-08-14 00:00",
         "2009-01-23 00:00",
         "2004-12-06 00:00",
         "2004-12-03 00:00",
         "2004-10-01 00:00",
         "2003-05-15 00:00",
         "2002-09-13 00:00",
         "2002-03-12 00:00",
         "2001-11-21 00:00",
         "2001-11-20 00:00",
         "2001-11-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIpConfs_ObjectIdentity = ObjectIdentity
lumIpConfs = _LumIpConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1)
)
_LumIpGroups_ObjectIdentity = ObjectIdentity
lumIpGroups = _LumIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1)
)
_LumIpCompl_ObjectIdentity = ObjectIdentity
lumIpCompl = _LumIpCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2)
)
_LumIpMIBObjects_ObjectIdentity = ObjectIdentity
lumIpMIBObjects = _LumIpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2)
)
_IpGeneral_ObjectIdentity = ObjectIdentity
ipGeneral = _IpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1)
)
_IpGeneralLastChangeTime_Type = DateAndTime
_IpGeneralLastChangeTime_Object = MibScalar
ipGeneralLastChangeTime = _IpGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 1),
    _IpGeneralLastChangeTime_Type()
)
ipGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralLastChangeTime.setStatus("current")
_IpGeneralNextMgmtAddress_Type = IpAddress
_IpGeneralNextMgmtAddress_Object = MibScalar
ipGeneralNextMgmtAddress = _IpGeneralNextMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 2),
    _IpGeneralNextMgmtAddress_Type()
)
ipGeneralNextMgmtAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGeneralNextMgmtAddress.setStatus("current")
_IpGeneralStoredMgmtAddress_Type = IpAddress
_IpGeneralStoredMgmtAddress_Object = MibScalar
ipGeneralStoredMgmtAddress = _IpGeneralStoredMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 3),
    _IpGeneralStoredMgmtAddress_Type()
)
ipGeneralStoredMgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralStoredMgmtAddress.setStatus("current")
_IpGeneralNextMgmtNetMask_Type = IpAddress
_IpGeneralNextMgmtNetMask_Object = MibScalar
ipGeneralNextMgmtNetMask = _IpGeneralNextMgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 4),
    _IpGeneralNextMgmtNetMask_Type()
)
ipGeneralNextMgmtNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGeneralNextMgmtNetMask.setStatus("current")
_IpGeneralStoredMgmtNetMask_Type = IpAddress
_IpGeneralStoredMgmtNetMask_Object = MibScalar
ipGeneralStoredMgmtNetMask = _IpGeneralStoredMgmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 5),
    _IpGeneralStoredMgmtNetMask_Type()
)
ipGeneralStoredMgmtNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralStoredMgmtNetMask.setStatus("current")
_IpGeneralConfigLastChangeTime_Type = DateAndTime
_IpGeneralConfigLastChangeTime_Object = MibScalar
ipGeneralConfigLastChangeTime = _IpGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 6),
    _IpGeneralConfigLastChangeTime_Type()
)
ipGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralConfigLastChangeTime.setStatus("current")


class _IpGeneralTelnetMode_Type(Integer32):
    """Custom type ipGeneralTelnetMode based on Integer32"""
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


_IpGeneralTelnetMode_Type.__name__ = "Integer32"
_IpGeneralTelnetMode_Object = MibScalar
ipGeneralTelnetMode = _IpGeneralTelnetMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 7),
    _IpGeneralTelnetMode_Type()
)
ipGeneralTelnetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralTelnetMode.setStatus("current")


class _IpGeneralFtpMode_Type(Integer32):
    """Custom type ipGeneralFtpMode based on Integer32"""
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


_IpGeneralFtpMode_Type.__name__ = "Integer32"
_IpGeneralFtpMode_Object = MibScalar
ipGeneralFtpMode = _IpGeneralFtpMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 8),
    _IpGeneralFtpMode_Type()
)
ipGeneralFtpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralFtpMode.setStatus("current")
_IpGeneralIfTableSize_Type = Unsigned32
_IpGeneralIfTableSize_Object = MibScalar
ipGeneralIfTableSize = _IpGeneralIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 9),
    _IpGeneralIfTableSize_Type()
)
ipGeneralIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralIfTableSize.setStatus("current")
_IpGeneralRouteTableSize_Type = Unsigned32
_IpGeneralRouteTableSize_Object = MibScalar
ipGeneralRouteTableSize = _IpGeneralRouteTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 10),
    _IpGeneralRouteTableSize_Type()
)
ipGeneralRouteTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralRouteTableSize.setStatus("current")
_IpGeneralOspfIfTableSize_Type = Unsigned32
_IpGeneralOspfIfTableSize_Object = MibScalar
ipGeneralOspfIfTableSize = _IpGeneralOspfIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 11),
    _IpGeneralOspfIfTableSize_Type()
)
ipGeneralOspfIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralOspfIfTableSize.setStatus("current")
_IpGeneralOspfNbrTableSize_Type = Unsigned32
_IpGeneralOspfNbrTableSize_Object = MibScalar
ipGeneralOspfNbrTableSize = _IpGeneralOspfNbrTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 12),
    _IpGeneralOspfNbrTableSize_Type()
)
ipGeneralOspfNbrTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralOspfNbrTableSize.setStatus("current")
_IpGeneralChangeNextMgmtAddr_Type = CommandString
_IpGeneralChangeNextMgmtAddr_Object = MibScalar
ipGeneralChangeNextMgmtAddr = _IpGeneralChangeNextMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 13),
    _IpGeneralChangeNextMgmtAddr_Type()
)
ipGeneralChangeNextMgmtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGeneralChangeNextMgmtAddr.setStatus("current")


class _IpGeneralSftpMode_Type(Integer32):
    """Custom type ipGeneralSftpMode based on Integer32"""
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


_IpGeneralSftpMode_Type.__name__ = "Integer32"
_IpGeneralSftpMode_Object = MibScalar
ipGeneralSftpMode = _IpGeneralSftpMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 14),
    _IpGeneralSftpMode_Type()
)
ipGeneralSftpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralSftpMode.setStatus("current")


class _IpGeneralTftpMode_Type(Integer32):
    """Custom type ipGeneralTftpMode based on Integer32"""
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


_IpGeneralTftpMode_Type.__name__ = "Integer32"
_IpGeneralTftpMode_Object = MibScalar
ipGeneralTftpMode = _IpGeneralTftpMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 15),
    _IpGeneralTftpMode_Type()
)
ipGeneralTftpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralTftpMode.setStatus("current")


class _IpGeneralNetconfMode_Type(Integer32):
    """Custom type ipGeneralNetconfMode based on Integer32"""
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


_IpGeneralNetconfMode_Type.__name__ = "Integer32"
_IpGeneralNetconfMode_Object = MibScalar
ipGeneralNetconfMode = _IpGeneralNetconfMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 1, 16),
    _IpGeneralNetconfMode_Type()
)
ipGeneralNetconfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGeneralNetconfMode.setStatus("current")
_IpIfList_ObjectIdentity = ObjectIdentity
ipIfList = _IpIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 2)
)
_IpIfTable_Object = MibTable
ipIfTable = _IpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipIfTable.setStatus("current")
_IpIfEntry_Object = MibTableRow
ipIfEntry = _IpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 2, 1, 1)
)
ipIfEntry.setIndexNames(
    (0, "LUM-IP-MIB", "ipIfIndex"),
)
if mibBuilder.loadTexts:
    ipIfEntry.setStatus("current")


class _IpIfIndex_Type(Unsigned32):
    """Custom type ipIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpIfIndex_Type.__name__ = "Unsigned32"
_IpIfIndex_Object = MibTableColumn
ipIfIndex = _IpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 2, 1, 1, 1),
    _IpIfIndex_Type()
)
ipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfIndex.setStatus("current")
_IpIfName_Type = MgmtNameString
_IpIfName_Object = MibTableColumn
ipIfName = _IpIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 2, 1, 1, 2),
    _IpIfName_Type()
)
ipIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfName.setStatus("current")
_IpIfAddr_Type = IpAddress
_IpIfAddr_Object = MibTableColumn
ipIfAddr = _IpIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 2, 1, 1, 3),
    _IpIfAddr_Type()
)
ipIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfAddr.setStatus("current")
_IpIfNetMask_Type = IpAddress
_IpIfNetMask_Object = MibTableColumn
ipIfNetMask = _IpIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 2, 1, 1, 4),
    _IpIfNetMask_Type()
)
ipIfNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfNetMask.setStatus("current")


class _IpIfOperStatus_Type(Integer32):
    """Custom type ipIfOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_IpIfOperStatus_Type.__name__ = "Integer32"
_IpIfOperStatus_Object = MibTableColumn
ipIfOperStatus = _IpIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 2, 1, 1, 5),
    _IpIfOperStatus_Type()
)
ipIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfOperStatus.setStatus("current")
_IpIfDstAddr_Type = IpAddress
_IpIfDstAddr_Object = MibTableColumn
ipIfDstAddr = _IpIfDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 2, 1, 1, 6),
    _IpIfDstAddr_Type()
)
ipIfDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfDstAddr.setStatus("current")
_IpRouteList_ObjectIdentity = ObjectIdentity
ipRouteList = _IpRouteList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3)
)
_IpRouteTable_Object = MibTable
ipRouteTable = _IpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ipRouteTable.setStatus("current")
_IpRouteEntry_Object = MibTableRow
ipRouteEntry = _IpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1)
)
ipRouteEntry.setIndexNames(
    (0, "LUM-IP-MIB", "ipRouteIndex"),
)
if mibBuilder.loadTexts:
    ipRouteEntry.setStatus("current")


class _IpRouteIndex_Type(Unsigned32):
    """Custom type ipRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpRouteIndex_Type.__name__ = "Unsigned32"
_IpRouteIndex_Object = MibTableColumn
ipRouteIndex = _IpRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 1),
    _IpRouteIndex_Type()
)
ipRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteIndex.setStatus("current")
_IpRouteDest_Type = IpAddress
_IpRouteDest_Object = MibTableColumn
ipRouteDest = _IpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 2),
    _IpRouteDest_Type()
)
ipRouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteDest.setStatus("current")
_IpRouteMask_Type = IpAddress
_IpRouteMask_Object = MibTableColumn
ipRouteMask = _IpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 3),
    _IpRouteMask_Type()
)
ipRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMask.setStatus("current")
_IpRouteNextHop_Type = IpAddress
_IpRouteNextHop_Object = MibTableColumn
ipRouteNextHop = _IpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 4),
    _IpRouteNextHop_Type()
)
ipRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteNextHop.setStatus("current")
_IpRouteIfName_Type = MgmtNameString
_IpRouteIfName_Object = MibTableColumn
ipRouteIfName = _IpRouteIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 5),
    _IpRouteIfName_Type()
)
ipRouteIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteIfName.setStatus("current")
_IpRouteRowStatus_Type = RowStatus
_IpRouteRowStatus_Object = MibTableColumn
ipRouteRowStatus = _IpRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 6),
    _IpRouteRowStatus_Type()
)
ipRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipRouteRowStatus.setStatus("current")


class _IpRouteProto_Type(Integer32):
    """Custom type ipRouteProto based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("kernel", 2),
          ("connect", 3),
          ("static", 4),
          ("rip", 5),
          ("ripng", 6),
          ("ospf", 7),
          ("ospf6", 8),
          ("bgp", 9))
    )


_IpRouteProto_Type.__name__ = "Integer32"
_IpRouteProto_Object = MibTableColumn
ipRouteProto = _IpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 7),
    _IpRouteProto_Type()
)
ipRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteProto.setStatus("current")


class _IpRouteMetric_Type(Unsigned32):
    """Custom type ipRouteMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpRouteMetric_Type.__name__ = "Unsigned32"
_IpRouteMetric_Object = MibTableColumn
ipRouteMetric = _IpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 8),
    _IpRouteMetric_Type()
)
ipRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric.setStatus("current")


class _IpRouteOperStatus_Type(Integer32):
    """Custom type ipRouteOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_IpRouteOperStatus_Type.__name__ = "Integer32"
_IpRouteOperStatus_Object = MibTableColumn
ipRouteOperStatus = _IpRouteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 9),
    _IpRouteOperStatus_Type()
)
ipRouteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteOperStatus.setStatus("current")
_IpRouteName_Type = MgmtNameString
_IpRouteName_Object = MibTableColumn
ipRouteName = _IpRouteName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 3, 1, 1, 10),
    _IpRouteName_Type()
)
ipRouteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteName.setStatus("current")
_OspfGeneral_ObjectIdentity = ObjectIdentity
ospfGeneral = _OspfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 4)
)
_OspfGeneralRouterId_Type = IpAddress
_OspfGeneralRouterId_Object = MibScalar
ospfGeneralRouterId = _OspfGeneralRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 4, 1),
    _OspfGeneralRouterId_Type()
)
ospfGeneralRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGeneralRouterId.setStatus("current")


class _OspfGeneralDistrMode_Type(Integer32):
    """Custom type ospfGeneralDistrMode based on Integer32"""
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


_OspfGeneralDistrMode_Type.__name__ = "Integer32"
_OspfGeneralDistrMode_Object = MibScalar
ospfGeneralDistrMode = _OspfGeneralDistrMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 4, 2),
    _OspfGeneralDistrMode_Type()
)
ospfGeneralDistrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGeneralDistrMode.setStatus("current")


class _OspfGeneralDistrMetricType_Type(Integer32):
    """Custom type ospfGeneralDistrMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("comparableCost", 1),
          ("nonComparable", 2))
    )


_OspfGeneralDistrMetricType_Type.__name__ = "Integer32"
_OspfGeneralDistrMetricType_Object = MibScalar
ospfGeneralDistrMetricType = _OspfGeneralDistrMetricType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 4, 3),
    _OspfGeneralDistrMetricType_Type()
)
ospfGeneralDistrMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGeneralDistrMetricType.setStatus("current")


class _OspfGeneralDistrMetric_Type(Unsigned32):
    """Custom type ospfGeneralDistrMetric based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_OspfGeneralDistrMetric_Type.__name__ = "Unsigned32"
_OspfGeneralDistrMetric_Object = MibScalar
ospfGeneralDistrMetric = _OspfGeneralDistrMetric_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 4, 4),
    _OspfGeneralDistrMetric_Type()
)
ospfGeneralDistrMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGeneralDistrMetric.setStatus("current")
_OspfIfList_ObjectIdentity = ObjectIdentity
ospfIfList = _OspfIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5)
)
_OspfIfTable_Object = MibTable
ospfIfTable = _OspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ospfIfTable.setStatus("current")
_OspfIfEntry_Object = MibTableRow
ospfIfEntry = _OspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1)
)
ospfIfEntry.setIndexNames(
    (0, "LUM-IP-MIB", "ospfIfIndex"),
)
if mibBuilder.loadTexts:
    ospfIfEntry.setStatus("current")


class _OspfIfIndex_Type(Unsigned32):
    """Custom type ospfIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OspfIfIndex_Type.__name__ = "Unsigned32"
_OspfIfIndex_Object = MibTableColumn
ospfIfIndex = _OspfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 1),
    _OspfIfIndex_Type()
)
ospfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfIndex.setStatus("current")
_OspfIfName_Type = MgmtNameString
_OspfIfName_Object = MibTableColumn
ospfIfName = _OspfIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 3),
    _OspfIfName_Type()
)
ospfIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfName.setStatus("current")
_OspfIfAreaId_Type = IpAddress
_OspfIfAreaId_Object = MibTableColumn
ospfIfAreaId = _OspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 4),
    _OspfIfAreaId_Type()
)
ospfIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfAreaId.setStatus("current")


class _OspfIfMetric_Type(Unsigned32):
    """Custom type ospfIfMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OspfIfMetric_Type.__name__ = "Unsigned32"
_OspfIfMetric_Object = MibTableColumn
ospfIfMetric = _OspfIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 5),
    _OspfIfMetric_Type()
)
ospfIfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfMetric.setStatus("current")


class _OspfIfRtrPriority_Type(Integer32):
    """Custom type ospfIfRtrPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfIfRtrPriority_Type.__name__ = "Integer32"
_OspfIfRtrPriority_Object = MibTableColumn
ospfIfRtrPriority = _OspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 6),
    _OspfIfRtrPriority_Type()
)
ospfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfRtrPriority.setStatus("current")
_OspfIfDesignatedRouterId_Type = IpAddress
_OspfIfDesignatedRouterId_Object = MibTableColumn
ospfIfDesignatedRouterId = _OspfIfDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 7),
    _OspfIfDesignatedRouterId_Type()
)
ospfIfDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfDesignatedRouterId.setStatus("current")
_OspfIfBackupDesignatedRouterId_Type = IpAddress
_OspfIfBackupDesignatedRouterId_Object = MibTableColumn
ospfIfBackupDesignatedRouterId = _OspfIfBackupDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 8),
    _OspfIfBackupDesignatedRouterId_Type()
)
ospfIfBackupDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfBackupDesignatedRouterId.setStatus("current")


class _OspfIfAdminStatus_Type(Integer32):
    """Custom type ospfIfAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_OspfIfAdminStatus_Type.__name__ = "Integer32"
_OspfIfAdminStatus_Object = MibTableColumn
ospfIfAdminStatus = _OspfIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 9),
    _OspfIfAdminStatus_Type()
)
ospfIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfAdminStatus.setStatus("current")


class _OspfIfOperStatus_Type(Integer32):
    """Custom type ospfIfOperStatus based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("ptp", 4),
          ("dr", 5),
          ("bdr", 6),
          ("odr", 7))
    )


_OspfIfOperStatus_Type.__name__ = "Integer32"
_OspfIfOperStatus_Object = MibTableColumn
ospfIfOperStatus = _OspfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 10),
    _OspfIfOperStatus_Type()
)
ospfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfOperStatus.setStatus("current")
_OspfIfRowStatus_Type = RowStatus
_OspfIfRowStatus_Object = MibTableColumn
ospfIfRowStatus = _OspfIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 11),
    _OspfIfRowStatus_Type()
)
ospfIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfIfRowStatus.setStatus("current")


class _OspfIfPassive_Type(Integer32):
    """Custom type ospfIfPassive based on Integer32"""
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


_OspfIfPassive_Type.__name__ = "Integer32"
_OspfIfPassive_Object = MibTableColumn
ospfIfPassive = _OspfIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 5, 1, 1, 12),
    _OspfIfPassive_Type()
)
ospfIfPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfPassive.setStatus("current")
_OspfNbrList_ObjectIdentity = ObjectIdentity
ospfNbrList = _OspfNbrList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 6)
)
_OspfNbrTable_Object = MibTable
ospfNbrTable = _OspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ospfNbrTable.setStatus("current")
_OspfNbrEntry_Object = MibTableRow
ospfNbrEntry = _OspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 6, 1, 1)
)
ospfNbrEntry.setIndexNames(
    (0, "LUM-IP-MIB", "ospfNbrIndex"),
)
if mibBuilder.loadTexts:
    ospfNbrEntry.setStatus("current")


class _OspfNbrIndex_Type(Unsigned32):
    """Custom type ospfNbrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OspfNbrIndex_Type.__name__ = "Unsigned32"
_OspfNbrIndex_Object = MibTableColumn
ospfNbrIndex = _OspfNbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 6, 1, 1, 1),
    _OspfNbrIndex_Type()
)
ospfNbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrIndex.setStatus("current")
_OspfNbrIpAddr_Type = IpAddress
_OspfNbrIpAddr_Object = MibTableColumn
ospfNbrIpAddr = _OspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 6, 1, 1, 2),
    _OspfNbrIpAddr_Type()
)
ospfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrIpAddr.setStatus("current")
_OspfNbrRtrId_Type = IpAddress
_OspfNbrRtrId_Object = MibTableColumn
ospfNbrRtrId = _OspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 6, 1, 1, 3),
    _OspfNbrRtrId_Type()
)
ospfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrRtrId.setStatus("current")
_OspfNbrIfName_Type = MgmtNameString
_OspfNbrIfName_Object = MibTableColumn
ospfNbrIfName = _OspfNbrIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 6, 1, 1, 4),
    _OspfNbrIfName_Type()
)
ospfNbrIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrIfName.setStatus("current")


class _OspfNbrOperStatus_Type(Integer32):
    """Custom type ospfNbrOperStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_OspfNbrOperStatus_Type.__name__ = "Integer32"
_OspfNbrOperStatus_Object = MibTableColumn
ospfNbrOperStatus = _OspfNbrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 6, 1, 1, 5),
    _OspfNbrOperStatus_Type()
)
ospfNbrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrOperStatus.setStatus("current")
_OspfNbrName_Type = MgmtNameString
_OspfNbrName_Object = MibTableColumn
ospfNbrName = _OspfNbrName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 2, 6, 1, 1, 6),
    _OspfNbrName_Type()
)
ospfNbrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrName.setStatus("current")

# Managed Objects groups

ipGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 1)
)
ipGeneralGroup.setObjects(
      *(("LUM-IP-MIB", "ipGeneralLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtNetMask"))
)
if mibBuilder.loadTexts:
    ipGeneralGroup.setStatus("current")

ipIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 2)
)
ipIfGroup.setObjects(
      *(("LUM-IP-MIB", "ipIfIndex"),
        ("LUM-IP-MIB", "ipIfName"),
        ("LUM-IP-MIB", "ipIfAddr"),
        ("LUM-IP-MIB", "ipIfNetMask"),
        ("LUM-IP-MIB", "ipIfOperStatus"))
)
if mibBuilder.loadTexts:
    ipIfGroup.setStatus("deprecated")

ipRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 3)
)
ipRouteGroup.setObjects(
      *(("LUM-IP-MIB", "ipRouteIndex"),
        ("LUM-IP-MIB", "ipRouteDest"),
        ("LUM-IP-MIB", "ipRouteMask"),
        ("LUM-IP-MIB", "ipRouteNextHop"),
        ("LUM-IP-MIB", "ipRouteIfName"),
        ("LUM-IP-MIB", "ipRouteRowStatus"),
        ("LUM-IP-MIB", "ipRouteProto"),
        ("LUM-IP-MIB", "ipRouteMetric"),
        ("LUM-IP-MIB", "ipRouteOperStatus"))
)
if mibBuilder.loadTexts:
    ipRouteGroup.setStatus("deprecated")

ospfGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 4)
)
ospfGeneralGroup.setObjects(
      *(("LUM-IP-MIB", "ospfGeneralRouterId"),
        ("LUM-IP-MIB", "ospfGeneralDistrMode"),
        ("LUM-IP-MIB", "ospfGeneralDistrMetricType"),
        ("LUM-IP-MIB", "ospfGeneralDistrMetric"))
)
if mibBuilder.loadTexts:
    ospfGeneralGroup.setStatus("current")

ospfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 5)
)
ospfIfGroup.setObjects(
      *(("LUM-IP-MIB", "ospfIfIndex"),
        ("LUM-IP-MIB", "ospfIfName"),
        ("LUM-IP-MIB", "ospfIfAreaId"),
        ("LUM-IP-MIB", "ospfIfMetric"),
        ("LUM-IP-MIB", "ospfIfRtrPriority"),
        ("LUM-IP-MIB", "ospfIfDesignatedRouterId"),
        ("LUM-IP-MIB", "ospfIfBackupDesignatedRouterId"),
        ("LUM-IP-MIB", "ospfIfAdminStatus"),
        ("LUM-IP-MIB", "ospfIfOperStatus"),
        ("LUM-IP-MIB", "ospfIfRowStatus"))
)
if mibBuilder.loadTexts:
    ospfIfGroup.setStatus("deprecated")

ospfNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 6)
)
ospfNbrGroup.setObjects(
      *(("LUM-IP-MIB", "ospfNbrIndex"),
        ("LUM-IP-MIB", "ospfNbrIpAddr"),
        ("LUM-IP-MIB", "ospfNbrRtrId"),
        ("LUM-IP-MIB", "ospfNbrIfName"),
        ("LUM-IP-MIB", "ospfNbrOperStatus"))
)
if mibBuilder.loadTexts:
    ospfNbrGroup.setStatus("deprecated")

ipGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 7)
)
ipGeneralGroupV2.setObjects(
      *(("LUM-IP-MIB", "ipGeneralLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    ipGeneralGroupV2.setStatus("deprecated")

ipGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 8)
)
ipGeneralGroupV3.setObjects(
      *(("LUM-IP-MIB", "ipGeneralLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralConfigLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralTelnetMode"),
        ("LUM-IP-MIB", "ipGeneralFtpMode"))
)
if mibBuilder.loadTexts:
    ipGeneralGroupV3.setStatus("current")

ipGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 9)
)
ipGeneralGroupV4.setObjects(
      *(("LUM-IP-MIB", "ipGeneralLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralConfigLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralTelnetMode"),
        ("LUM-IP-MIB", "ipGeneralFtpMode"),
        ("LUM-IP-MIB", "ipGeneralIfTableSize"),
        ("LUM-IP-MIB", "ipGeneralRouteTableSize"),
        ("LUM-IP-MIB", "ipGeneralOspfIfTableSize"),
        ("LUM-IP-MIB", "ipGeneralOspfNbrTableSize"))
)
if mibBuilder.loadTexts:
    ipGeneralGroupV4.setStatus("deprecated")

ipRouteGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 10)
)
ipRouteGroupV2.setObjects(
      *(("LUM-IP-MIB", "ipRouteIndex"),
        ("LUM-IP-MIB", "ipRouteDest"),
        ("LUM-IP-MIB", "ipRouteMask"),
        ("LUM-IP-MIB", "ipRouteNextHop"),
        ("LUM-IP-MIB", "ipRouteIfName"),
        ("LUM-IP-MIB", "ipRouteRowStatus"),
        ("LUM-IP-MIB", "ipRouteProto"),
        ("LUM-IP-MIB", "ipRouteMetric"),
        ("LUM-IP-MIB", "ipRouteOperStatus"),
        ("LUM-IP-MIB", "ipRouteName"))
)
if mibBuilder.loadTexts:
    ipRouteGroupV2.setStatus("current")

ospfNbrGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 11)
)
ospfNbrGroupV2.setObjects(
      *(("LUM-IP-MIB", "ospfNbrIndex"),
        ("LUM-IP-MIB", "ospfNbrIpAddr"),
        ("LUM-IP-MIB", "ospfNbrRtrId"),
        ("LUM-IP-MIB", "ospfNbrIfName"),
        ("LUM-IP-MIB", "ospfNbrOperStatus"),
        ("LUM-IP-MIB", "ospfNbrName"))
)
if mibBuilder.loadTexts:
    ospfNbrGroupV2.setStatus("current")

ipGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 12)
)
ipGeneralGroupV5.setObjects(
      *(("LUM-IP-MIB", "ipGeneralLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralConfigLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralTelnetMode"),
        ("LUM-IP-MIB", "ipGeneralFtpMode"),
        ("LUM-IP-MIB", "ipGeneralIfTableSize"),
        ("LUM-IP-MIB", "ipGeneralRouteTableSize"),
        ("LUM-IP-MIB", "ipGeneralOspfIfTableSize"),
        ("LUM-IP-MIB", "ipGeneralOspfNbrTableSize"),
        ("LUM-IP-MIB", "ipGeneralChangeNextMgmtAddr"))
)
if mibBuilder.loadTexts:
    ipGeneralGroupV5.setStatus("deprecated")

ospfIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 13)
)
ospfIfGroupV2.setObjects(
      *(("LUM-IP-MIB", "ospfIfIndex"),
        ("LUM-IP-MIB", "ospfIfName"),
        ("LUM-IP-MIB", "ospfIfAreaId"),
        ("LUM-IP-MIB", "ospfIfMetric"),
        ("LUM-IP-MIB", "ospfIfRtrPriority"),
        ("LUM-IP-MIB", "ospfIfDesignatedRouterId"),
        ("LUM-IP-MIB", "ospfIfBackupDesignatedRouterId"),
        ("LUM-IP-MIB", "ospfIfAdminStatus"),
        ("LUM-IP-MIB", "ospfIfOperStatus"),
        ("LUM-IP-MIB", "ospfIfRowStatus"),
        ("LUM-IP-MIB", "ospfIfPassive"))
)
if mibBuilder.loadTexts:
    ospfIfGroupV2.setStatus("current")

ipGeneralGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 14)
)
ipGeneralGroupV6.setObjects(
      *(("LUM-IP-MIB", "ipGeneralLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralConfigLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralTelnetMode"),
        ("LUM-IP-MIB", "ipGeneralFtpMode"),
        ("LUM-IP-MIB", "ipGeneralIfTableSize"),
        ("LUM-IP-MIB", "ipGeneralRouteTableSize"),
        ("LUM-IP-MIB", "ipGeneralOspfIfTableSize"),
        ("LUM-IP-MIB", "ipGeneralOspfNbrTableSize"),
        ("LUM-IP-MIB", "ipGeneralChangeNextMgmtAddr"),
        ("LUM-IP-MIB", "ipGeneralSftpMode"),
        ("LUM-IP-MIB", "ipGeneralTftpMode"))
)
if mibBuilder.loadTexts:
    ipGeneralGroupV6.setStatus("deprecated")

ipGeneralGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 15)
)
ipGeneralGroupV7.setObjects(
      *(("LUM-IP-MIB", "ipGeneralLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtAddress"),
        ("LUM-IP-MIB", "ipGeneralNextMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralStoredMgmtNetMask"),
        ("LUM-IP-MIB", "ipGeneralConfigLastChangeTime"),
        ("LUM-IP-MIB", "ipGeneralTelnetMode"),
        ("LUM-IP-MIB", "ipGeneralFtpMode"),
        ("LUM-IP-MIB", "ipGeneralIfTableSize"),
        ("LUM-IP-MIB", "ipGeneralRouteTableSize"),
        ("LUM-IP-MIB", "ipGeneralOspfIfTableSize"),
        ("LUM-IP-MIB", "ipGeneralOspfNbrTableSize"),
        ("LUM-IP-MIB", "ipGeneralChangeNextMgmtAddr"),
        ("LUM-IP-MIB", "ipGeneralSftpMode"),
        ("LUM-IP-MIB", "ipGeneralTftpMode"),
        ("LUM-IP-MIB", "ipGeneralNetconfMode"))
)
if mibBuilder.loadTexts:
    ipGeneralGroupV7.setStatus("current")

ipIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 1, 16)
)
ipIfGroupV2.setObjects(
      *(("LUM-IP-MIB", "ipIfIndex"),
        ("LUM-IP-MIB", "ipIfName"),
        ("LUM-IP-MIB", "ipIfAddr"),
        ("LUM-IP-MIB", "ipIfNetMask"),
        ("LUM-IP-MIB", "ipIfOperStatus"),
        ("LUM-IP-MIB", "ipIfDstAddr"))
)
if mibBuilder.loadTexts:
    ipIfGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIpBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 1)
)
lumIpBasicComplV1.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroup"),
        ("LUM-IP-MIB", "ipIfGroup"),
        ("LUM-IP-MIB", "ipRouteGroup"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV1.setStatus(
        "deprecated"
    )

lumIpBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 2)
)
lumIpBasicComplV2.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroup"),
        ("LUM-IP-MIB", "ipIfGroup"),
        ("LUM-IP-MIB", "ipRouteGroup"),
        ("LUM-IP-MIB", "ospfGeneralGroup"),
        ("LUM-IP-MIB", "ospfIfGroup"),
        ("LUM-IP-MIB", "ospfNbrGroup"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV2.setStatus(
        "deprecated"
    )

lumIpBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 3)
)
lumIpBasicComplV3.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroupV2"),
        ("LUM-IP-MIB", "ipIfGroup"),
        ("LUM-IP-MIB", "ipRouteGroup"),
        ("LUM-IP-MIB", "ospfGeneralGroup"),
        ("LUM-IP-MIB", "ospfIfGroup"),
        ("LUM-IP-MIB", "ospfNbrGroup"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV3.setStatus(
        "deprecated"
    )

lumIpBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 4)
)
lumIpBasicComplV4.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroupV3"),
        ("LUM-IP-MIB", "ipIfGroup"),
        ("LUM-IP-MIB", "ipRouteGroup"),
        ("LUM-IP-MIB", "ospfGeneralGroup"),
        ("LUM-IP-MIB", "ospfIfGroup"),
        ("LUM-IP-MIB", "ospfNbrGroup"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV4.setStatus(
        "deprecated"
    )

lumIpBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 5)
)
lumIpBasicComplV5.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroupV4"),
        ("LUM-IP-MIB", "ipIfGroup"),
        ("LUM-IP-MIB", "ipRouteGroup"),
        ("LUM-IP-MIB", "ospfGeneralGroup"),
        ("LUM-IP-MIB", "ospfIfGroup"),
        ("LUM-IP-MIB", "ospfNbrGroup"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV5.setStatus(
        "deprecated"
    )

lumIpBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 6)
)
lumIpBasicComplV6.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroupV5"),
        ("LUM-IP-MIB", "ipIfGroup"),
        ("LUM-IP-MIB", "ipRouteGroupV2"),
        ("LUM-IP-MIB", "ospfGeneralGroup"),
        ("LUM-IP-MIB", "ospfIfGroup"),
        ("LUM-IP-MIB", "ospfNbrGroupV2"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV6.setStatus(
        "deprecated"
    )

lumIpBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 7)
)
lumIpBasicComplV7.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroupV5"),
        ("LUM-IP-MIB", "ipIfGroup"),
        ("LUM-IP-MIB", "ipRouteGroupV2"),
        ("LUM-IP-MIB", "ospfGeneralGroup"),
        ("LUM-IP-MIB", "ospfIfGroupV2"),
        ("LUM-IP-MIB", "ospfNbrGroupV2"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV7.setStatus(
        "deprecated"
    )

lumIpBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 8)
)
lumIpBasicComplV8.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroupV6"),
        ("LUM-IP-MIB", "ipIfGroup"),
        ("LUM-IP-MIB", "ipRouteGroupV2"),
        ("LUM-IP-MIB", "ospfGeneralGroup"),
        ("LUM-IP-MIB", "ospfIfGroupV2"),
        ("LUM-IP-MIB", "ospfNbrGroupV2"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV8.setStatus(
        "deprecated"
    )

lumIpBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 9)
)
lumIpBasicComplV9.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroupV7"),
        ("LUM-IP-MIB", "ipIfGroup"),
        ("LUM-IP-MIB", "ipRouteGroupV2"),
        ("LUM-IP-MIB", "ospfGeneralGroup"),
        ("LUM-IP-MIB", "ospfIfGroupV2"),
        ("LUM-IP-MIB", "ospfNbrGroupV2"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV9.setStatus(
        "deprecated"
    )

lumIpBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 14, 1, 2, 10)
)
lumIpBasicComplV10.setObjects(
      *(("LUM-IP-MIB", "ipGeneralGroupV7"),
        ("LUM-IP-MIB", "ipIfGroupV2"),
        ("LUM-IP-MIB", "ipRouteGroupV2"),
        ("LUM-IP-MIB", "ospfGeneralGroup"),
        ("LUM-IP-MIB", "ospfIfGroupV2"),
        ("LUM-IP-MIB", "ospfNbrGroupV2"))
)
if mibBuilder.loadTexts:
    lumIpBasicComplV10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IP-MIB",
    **{"lumIpMIBModule": lumIpMIBModule,
       "lumIpConfs": lumIpConfs,
       "lumIpGroups": lumIpGroups,
       "ipGeneralGroup": ipGeneralGroup,
       "ipIfGroup": ipIfGroup,
       "ipRouteGroup": ipRouteGroup,
       "ospfGeneralGroup": ospfGeneralGroup,
       "ospfIfGroup": ospfIfGroup,
       "ospfNbrGroup": ospfNbrGroup,
       "ipGeneralGroupV2": ipGeneralGroupV2,
       "ipGeneralGroupV3": ipGeneralGroupV3,
       "ipGeneralGroupV4": ipGeneralGroupV4,
       "ipRouteGroupV2": ipRouteGroupV2,
       "ospfNbrGroupV2": ospfNbrGroupV2,
       "ipGeneralGroupV5": ipGeneralGroupV5,
       "ospfIfGroupV2": ospfIfGroupV2,
       "ipGeneralGroupV6": ipGeneralGroupV6,
       "ipGeneralGroupV7": ipGeneralGroupV7,
       "ipIfGroupV2": ipIfGroupV2,
       "lumIpCompl": lumIpCompl,
       "lumIpBasicComplV1": lumIpBasicComplV1,
       "lumIpBasicComplV2": lumIpBasicComplV2,
       "lumIpBasicComplV3": lumIpBasicComplV3,
       "lumIpBasicComplV4": lumIpBasicComplV4,
       "lumIpBasicComplV5": lumIpBasicComplV5,
       "lumIpBasicComplV6": lumIpBasicComplV6,
       "lumIpBasicComplV7": lumIpBasicComplV7,
       "lumIpBasicComplV8": lumIpBasicComplV8,
       "lumIpBasicComplV9": lumIpBasicComplV9,
       "lumIpBasicComplV10": lumIpBasicComplV10,
       "lumIpMIBObjects": lumIpMIBObjects,
       "ipGeneral": ipGeneral,
       "ipGeneralLastChangeTime": ipGeneralLastChangeTime,
       "ipGeneralNextMgmtAddress": ipGeneralNextMgmtAddress,
       "ipGeneralStoredMgmtAddress": ipGeneralStoredMgmtAddress,
       "ipGeneralNextMgmtNetMask": ipGeneralNextMgmtNetMask,
       "ipGeneralStoredMgmtNetMask": ipGeneralStoredMgmtNetMask,
       "ipGeneralConfigLastChangeTime": ipGeneralConfigLastChangeTime,
       "ipGeneralTelnetMode": ipGeneralTelnetMode,
       "ipGeneralFtpMode": ipGeneralFtpMode,
       "ipGeneralIfTableSize": ipGeneralIfTableSize,
       "ipGeneralRouteTableSize": ipGeneralRouteTableSize,
       "ipGeneralOspfIfTableSize": ipGeneralOspfIfTableSize,
       "ipGeneralOspfNbrTableSize": ipGeneralOspfNbrTableSize,
       "ipGeneralChangeNextMgmtAddr": ipGeneralChangeNextMgmtAddr,
       "ipGeneralSftpMode": ipGeneralSftpMode,
       "ipGeneralTftpMode": ipGeneralTftpMode,
       "ipGeneralNetconfMode": ipGeneralNetconfMode,
       "ipIfList": ipIfList,
       "ipIfTable": ipIfTable,
       "ipIfEntry": ipIfEntry,
       "ipIfIndex": ipIfIndex,
       "ipIfName": ipIfName,
       "ipIfAddr": ipIfAddr,
       "ipIfNetMask": ipIfNetMask,
       "ipIfOperStatus": ipIfOperStatus,
       "ipIfDstAddr": ipIfDstAddr,
       "ipRouteList": ipRouteList,
       "ipRouteTable": ipRouteTable,
       "ipRouteEntry": ipRouteEntry,
       "ipRouteIndex": ipRouteIndex,
       "ipRouteDest": ipRouteDest,
       "ipRouteMask": ipRouteMask,
       "ipRouteNextHop": ipRouteNextHop,
       "ipRouteIfName": ipRouteIfName,
       "ipRouteRowStatus": ipRouteRowStatus,
       "ipRouteProto": ipRouteProto,
       "ipRouteMetric": ipRouteMetric,
       "ipRouteOperStatus": ipRouteOperStatus,
       "ipRouteName": ipRouteName,
       "ospfGeneral": ospfGeneral,
       "ospfGeneralRouterId": ospfGeneralRouterId,
       "ospfGeneralDistrMode": ospfGeneralDistrMode,
       "ospfGeneralDistrMetricType": ospfGeneralDistrMetricType,
       "ospfGeneralDistrMetric": ospfGeneralDistrMetric,
       "ospfIfList": ospfIfList,
       "ospfIfTable": ospfIfTable,
       "ospfIfEntry": ospfIfEntry,
       "ospfIfIndex": ospfIfIndex,
       "ospfIfName": ospfIfName,
       "ospfIfAreaId": ospfIfAreaId,
       "ospfIfMetric": ospfIfMetric,
       "ospfIfRtrPriority": ospfIfRtrPriority,
       "ospfIfDesignatedRouterId": ospfIfDesignatedRouterId,
       "ospfIfBackupDesignatedRouterId": ospfIfBackupDesignatedRouterId,
       "ospfIfAdminStatus": ospfIfAdminStatus,
       "ospfIfOperStatus": ospfIfOperStatus,
       "ospfIfRowStatus": ospfIfRowStatus,
       "ospfIfPassive": ospfIfPassive,
       "ospfNbrList": ospfNbrList,
       "ospfNbrTable": ospfNbrTable,
       "ospfNbrEntry": ospfNbrEntry,
       "ospfNbrIndex": ospfNbrIndex,
       "ospfNbrIpAddr": ospfNbrIpAddr,
       "ospfNbrRtrId": ospfNbrRtrId,
       "ospfNbrIfName": ospfNbrIfName,
       "ospfNbrOperStatus": ospfNbrOperStatus,
       "ospfNbrName": ospfNbrName}
)
