# SNMP MIB module (IPDHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/IPDHCP-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:26 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(EnableVar,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "Vlanset")


# MODULE-IDENTITY

rcIpDhcpServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29)
)
if mibBuilder.loadTexts:
    rcIpDhcpServer.setRevisions(
        ("2007-10-15 00:00",
         "2008-06-24 00:00",
         "2009-07-14 00:00",
         "2009-09-02 00:00",
         "2009-09-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcIpDhcpServerConfig_ObjectIdentity = ObjectIdentity
rcIpDhcpServerConfig = _RcIpDhcpServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1)
)


class _RcIpDhcpPropEnable_Type(EnableVar):
    """Custom type rcIpDhcpPropEnable based on EnableVar"""
    defaultValue = 2


_RcIpDhcpPropEnable_Type.__name__ = "EnableVar"
_RcIpDhcpPropEnable_Object = MibScalar
rcIpDhcpPropEnable = _RcIpDhcpPropEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 1),
    _RcIpDhcpPropEnable_Type()
)
rcIpDhcpPropEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpPropEnable.setStatus("current")
_RcIpDhcpIpNextIndex_Type = Integer32
_RcIpDhcpIpNextIndex_Object = MibScalar
rcIpDhcpIpNextIndex = _RcIpDhcpIpNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 2),
    _RcIpDhcpIpNextIndex_Type()
)
rcIpDhcpIpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpIpNextIndex.setStatus("current")


class _RcIpDhcpMaxLease_Type(Integer32):
    """Custom type rcIpDhcpMaxLease based on Integer32"""
    defaultValue = 10080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RcIpDhcpMaxLease_Type.__name__ = "Integer32"
_RcIpDhcpMaxLease_Object = MibScalar
rcIpDhcpMaxLease = _RcIpDhcpMaxLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 3),
    _RcIpDhcpMaxLease_Type()
)
rcIpDhcpMaxLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpMaxLease.setStatus("current")


class _RcIpDhcpMinLease_Type(Integer32):
    """Custom type rcIpDhcpMinLease based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RcIpDhcpMinLease_Type.__name__ = "Integer32"
_RcIpDhcpMinLease_Object = MibScalar
rcIpDhcpMinLease = _RcIpDhcpMinLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 4),
    _RcIpDhcpMinLease_Type()
)
rcIpDhcpMinLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpMinLease.setStatus("current")


class _RcIpDhcpDefLease_Type(Integer32):
    """Custom type rcIpDhcpDefLease based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RcIpDhcpDefLease_Type.__name__ = "Integer32"
_RcIpDhcpDefLease_Object = MibScalar
rcIpDhcpDefLease = _RcIpDhcpDefLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 5),
    _RcIpDhcpDefLease_Type()
)
rcIpDhcpDefLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpDefLease.setStatus("current")
_RcIpDhcpVlanAuth_Type = Vlanset
_RcIpDhcpVlanAuth_Object = MibScalar
rcIpDhcpVlanAuth = _RcIpDhcpVlanAuth_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 6),
    _RcIpDhcpVlanAuth_Type()
)
rcIpDhcpVlanAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpVlanAuth.setStatus("current")
_RcIpDhcpServerStartTime_Type = TimeTicks
_RcIpDhcpServerStartTime_Object = MibScalar
rcIpDhcpServerStartTime = _RcIpDhcpServerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 7),
    _RcIpDhcpServerStartTime_Type()
)
rcIpDhcpServerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStartTime.setStatus("current")
_RcIpDhcpIpIfTable_Object = MibTable
rcIpDhcpIpIfTable = _RcIpDhcpIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 8)
)
if mibBuilder.loadTexts:
    rcIpDhcpIpIfTable.setStatus("current")
_RcIpDhcpIpIfEntry_Object = MibTableRow
rcIpDhcpIpIfEntry = _RcIpDhcpIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 8, 1)
)
rcIpDhcpIpIfEntry.setIndexNames(
    (0, "IPDHCP-SERVER-MIB", "rcIpDhcpIpIfIndex"),
)
if mibBuilder.loadTexts:
    rcIpDhcpIpIfEntry.setStatus("current")
_RcIpDhcpIpIfIndex_Type = Integer32
_RcIpDhcpIpIfIndex_Object = MibTableColumn
rcIpDhcpIpIfIndex = _RcIpDhcpIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 8, 1, 1),
    _RcIpDhcpIpIfIndex_Type()
)
rcIpDhcpIpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpDhcpIpIfIndex.setStatus("current")
_RcIpDhcpIpIfDhcpsEnable_Type = EnableVar
_RcIpDhcpIpIfDhcpsEnable_Object = MibTableColumn
rcIpDhcpIpIfDhcpsEnable = _RcIpDhcpIpIfDhcpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 8, 1, 2),
    _RcIpDhcpIpIfDhcpsEnable_Type()
)
rcIpDhcpIpIfDhcpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpIpIfDhcpsEnable.setStatus("current")
_RcIpDhcpIpTable_Object = MibTable
rcIpDhcpIpTable = _RcIpDhcpIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9)
)
if mibBuilder.loadTexts:
    rcIpDhcpIpTable.setStatus("current")
_RcIpDhcpIpEntry_Object = MibTableRow
rcIpDhcpIpEntry = _RcIpDhcpIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1)
)
rcIpDhcpIpEntry.setIndexNames(
    (0, "IPDHCP-SERVER-MIB", "rcIpDhcpIpIndex"),
)
if mibBuilder.loadTexts:
    rcIpDhcpIpEntry.setStatus("current")
_RcIpDhcpIpIndex_Type = Integer32
_RcIpDhcpIpIndex_Object = MibTableColumn
rcIpDhcpIpIndex = _RcIpDhcpIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 1),
    _RcIpDhcpIpIndex_Type()
)
rcIpDhcpIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpDhcpIpIndex.setStatus("current")


class _RcIpDhcpIpEntryName_Type(OctetString):
    """Custom type rcIpDhcpIpEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcIpDhcpIpEntryName_Type.__name__ = "OctetString"
_RcIpDhcpIpEntryName_Object = MibTableColumn
rcIpDhcpIpEntryName = _RcIpDhcpIpEntryName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 2),
    _RcIpDhcpIpEntryName_Type()
)
rcIpDhcpIpEntryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpEntryName.setStatus("current")
_RcIpDhcpIpInterface_Type = Integer32
_RcIpDhcpIpInterface_Object = MibTableColumn
rcIpDhcpIpInterface = _RcIpDhcpIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 3),
    _RcIpDhcpIpInterface_Type()
)
rcIpDhcpIpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpInterface.setStatus("current")
_RcIpDhcpIpStartIp_Type = IpAddress
_RcIpDhcpIpStartIp_Object = MibTableColumn
rcIpDhcpIpStartIp = _RcIpDhcpIpStartIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 4),
    _RcIpDhcpIpStartIp_Type()
)
rcIpDhcpIpStartIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpStartIp.setStatus("current")
_RcIpDhcpIpEndIp_Type = IpAddress
_RcIpDhcpIpEndIp_Object = MibTableColumn
rcIpDhcpIpEndIp = _RcIpDhcpIpEndIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 5),
    _RcIpDhcpIpEndIp_Type()
)
rcIpDhcpIpEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpEndIp.setStatus("current")
_RcIpDhcpIpNetmask_Type = IpAddress
_RcIpDhcpIpNetmask_Object = MibTableColumn
rcIpDhcpIpNetmask = _RcIpDhcpIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 6),
    _RcIpDhcpIpNetmask_Type()
)
rcIpDhcpIpNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpNetmask.setStatus("current")
_RcIpDhcpIpGateway_Type = IpAddress
_RcIpDhcpIpGateway_Object = MibTableColumn
rcIpDhcpIpGateway = _RcIpDhcpIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 7),
    _RcIpDhcpIpGateway_Type()
)
rcIpDhcpIpGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpGateway.setStatus("current")
_RcIpDhcpIpDnsServer_Type = IpAddress
_RcIpDhcpIpDnsServer_Object = MibTableColumn
rcIpDhcpIpDnsServer = _RcIpDhcpIpDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 8),
    _RcIpDhcpIpDnsServer_Type()
)
rcIpDhcpIpDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpDnsServer.setStatus("current")
_RcIpDhcpIpSecondaryDnsServer_Type = IpAddress
_RcIpDhcpIpSecondaryDnsServer_Object = MibTableColumn
rcIpDhcpIpSecondaryDnsServer = _RcIpDhcpIpSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 9),
    _RcIpDhcpIpSecondaryDnsServer_Type()
)
rcIpDhcpIpSecondaryDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpSecondaryDnsServer.setStatus("current")
_RcIpDhcpIpRowStatus_Type = RowStatus
_RcIpDhcpIpRowStatus_Object = MibTableColumn
rcIpDhcpIpRowStatus = _RcIpDhcpIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 10),
    _RcIpDhcpIpRowStatus_Type()
)
rcIpDhcpIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpRowStatus.setStatus("current")
_RcIpDhcpIpTftpSvrAddress_Type = IpAddress
_RcIpDhcpIpTftpSvrAddress_Object = MibTableColumn
rcIpDhcpIpTftpSvrAddress = _RcIpDhcpIpTftpSvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 11),
    _RcIpDhcpIpTftpSvrAddress_Type()
)
rcIpDhcpIpTftpSvrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpTftpSvrAddress.setStatus("current")


class _RcIpDhcpIpBootfileName_Type(OctetString):
    """Custom type rcIpDhcpIpBootfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RcIpDhcpIpBootfileName_Type.__name__ = "OctetString"
_RcIpDhcpIpBootfileName_Object = MibTableColumn
rcIpDhcpIpBootfileName = _RcIpDhcpIpBootfileName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 12),
    _RcIpDhcpIpBootfileName_Type()
)
rcIpDhcpIpBootfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpBootfileName.setStatus("current")


class _RcIpDhcpIpMaxLease_Type(Integer32):
    """Custom type rcIpDhcpIpMaxLease based on Integer32"""
    defaultValue = 10080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RcIpDhcpIpMaxLease_Type.__name__ = "Integer32"
_RcIpDhcpIpMaxLease_Object = MibTableColumn
rcIpDhcpIpMaxLease = _RcIpDhcpIpMaxLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 13),
    _RcIpDhcpIpMaxLease_Type()
)
rcIpDhcpIpMaxLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpMaxLease.setStatus("current")


class _RcIpDhcpIpMinLease_Type(Integer32):
    """Custom type rcIpDhcpIpMinLease based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RcIpDhcpIpMinLease_Type.__name__ = "Integer32"
_RcIpDhcpIpMinLease_Object = MibTableColumn
rcIpDhcpIpMinLease = _RcIpDhcpIpMinLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 14),
    _RcIpDhcpIpMinLease_Type()
)
rcIpDhcpIpMinLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpMinLease.setStatus("current")


class _RcIpDhcpIpDefLease_Type(Integer32):
    """Custom type rcIpDhcpIpDefLease based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10080),
    )


_RcIpDhcpIpDefLease_Type.__name__ = "Integer32"
_RcIpDhcpIpDefLease_Object = MibTableColumn
rcIpDhcpIpDefLease = _RcIpDhcpIpDefLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 9, 1, 15),
    _RcIpDhcpIpDefLease_Type()
)
rcIpDhcpIpDefLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpDefLease.setStatus("current")


class _RcIpDhcpRelayNextIndex_Type(Integer32):
    """Custom type rcIpDhcpRelayNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcIpDhcpRelayNextIndex_Type.__name__ = "Integer32"
_RcIpDhcpRelayNextIndex_Object = MibScalar
rcIpDhcpRelayNextIndex = _RcIpDhcpRelayNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 10),
    _RcIpDhcpRelayNextIndex_Type()
)
rcIpDhcpRelayNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpRelayNextIndex.setStatus("current")
_RcIpDhcpRelayTable_Object = MibTable
rcIpDhcpRelayTable = _RcIpDhcpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 11)
)
if mibBuilder.loadTexts:
    rcIpDhcpRelayTable.setStatus("current")
_RcIpDhcpRelayEntry_Object = MibTableRow
rcIpDhcpRelayEntry = _RcIpDhcpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 11, 1)
)
rcIpDhcpRelayEntry.setIndexNames(
    (0, "IPDHCP-SERVER-MIB", "rcIpDhcpRelayIndex"),
)
if mibBuilder.loadTexts:
    rcIpDhcpRelayEntry.setStatus("current")
_RcIpDhcpRelayIndex_Type = Integer32
_RcIpDhcpRelayIndex_Object = MibTableColumn
rcIpDhcpRelayIndex = _RcIpDhcpRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 11, 1, 1),
    _RcIpDhcpRelayIndex_Type()
)
rcIpDhcpRelayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpDhcpRelayIndex.setStatus("current")
_RcIpDhcpRelayAddress_Type = IpAddress
_RcIpDhcpRelayAddress_Object = MibTableColumn
rcIpDhcpRelayAddress = _RcIpDhcpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 11, 1, 2),
    _RcIpDhcpRelayAddress_Type()
)
rcIpDhcpRelayAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpRelayAddress.setStatus("current")
_RcIpDhcpRelayMask_Type = IpAddress
_RcIpDhcpRelayMask_Object = MibTableColumn
rcIpDhcpRelayMask = _RcIpDhcpRelayMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 11, 1, 3),
    _RcIpDhcpRelayMask_Type()
)
rcIpDhcpRelayMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpRelayMask.setStatus("current")
_RcIpDhcpRelayRowStatus_Type = RowStatus
_RcIpDhcpRelayRowStatus_Object = MibTableColumn
rcIpDhcpRelayRowStatus = _RcIpDhcpRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 11, 1, 4),
    _RcIpDhcpRelayRowStatus_Type()
)
rcIpDhcpRelayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpRelayRowStatus.setStatus("current")
_RcIpDhcpIpVendorOptTable_Object = MibTable
rcIpDhcpIpVendorOptTable = _RcIpDhcpIpVendorOptTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 12)
)
if mibBuilder.loadTexts:
    rcIpDhcpIpVendorOptTable.setStatus("current")
_RcIpDhcpIpVendorOptEntry_Object = MibTableRow
rcIpDhcpIpVendorOptEntry = _RcIpDhcpIpVendorOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 12, 1)
)
rcIpDhcpIpVendorOptEntry.setIndexNames(
    (0, "IPDHCP-SERVER-MIB", "rcIpDhcpIpIndex"),
    (0, "IPDHCP-SERVER-MIB", "rcIpDhcpIpOptionCode"),
)
if mibBuilder.loadTexts:
    rcIpDhcpIpVendorOptEntry.setStatus("current")


class _RcIpDhcpIpOptionCode_Type(Integer32):
    """Custom type rcIpDhcpIpOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RcIpDhcpIpOptionCode_Type.__name__ = "Integer32"
_RcIpDhcpIpOptionCode_Object = MibTableColumn
rcIpDhcpIpOptionCode = _RcIpDhcpIpOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 12, 1, 1),
    _RcIpDhcpIpOptionCode_Type()
)
rcIpDhcpIpOptionCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpDhcpIpOptionCode.setStatus("current")


class _RcIpDhcpIpOptionType_Type(Integer32):
    """Custom type rcIpDhcpIpOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_RcIpDhcpIpOptionType_Type.__name__ = "Integer32"
_RcIpDhcpIpOptionType_Object = MibTableColumn
rcIpDhcpIpOptionType = _RcIpDhcpIpOptionType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 12, 1, 2),
    _RcIpDhcpIpOptionType_Type()
)
rcIpDhcpIpOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpOptionType.setStatus("current")


class _RcIpDhcpIpOptionContents_Type(OctetString):
    """Custom type rcIpDhcpIpOptionContents based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 192),
    )


_RcIpDhcpIpOptionContents_Type.__name__ = "OctetString"
_RcIpDhcpIpOptionContents_Object = MibTableColumn
rcIpDhcpIpOptionContents = _RcIpDhcpIpOptionContents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 12, 1, 3),
    _RcIpDhcpIpOptionContents_Type()
)
rcIpDhcpIpOptionContents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpOptionContents.setStatus("current")


class _RcIpDhcpIpOptionLength_Type(Integer32):
    """Custom type rcIpDhcpIpOptionLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 192),
    )


_RcIpDhcpIpOptionLength_Type.__name__ = "Integer32"
_RcIpDhcpIpOptionLength_Object = MibTableColumn
rcIpDhcpIpOptionLength = _RcIpDhcpIpOptionLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 12, 1, 4),
    _RcIpDhcpIpOptionLength_Type()
)
rcIpDhcpIpOptionLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpIpOptionLength.setStatus("current")
_RcIpDhcpIpOptionRowStatus_Type = RowStatus
_RcIpDhcpIpOptionRowStatus_Object = MibTableColumn
rcIpDhcpIpOptionRowStatus = _RcIpDhcpIpOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 12, 1, 5),
    _RcIpDhcpIpOptionRowStatus_Type()
)
rcIpDhcpIpOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIpDhcpIpOptionRowStatus.setStatus("current")
_RcIpDhcpIpRelayInformationOption_Type = EnableVar
_RcIpDhcpIpRelayInformationOption_Object = MibScalar
rcIpDhcpIpRelayInformationOption = _RcIpDhcpIpRelayInformationOption_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 13),
    _RcIpDhcpIpRelayInformationOption_Type()
)
rcIpDhcpIpRelayInformationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpDhcpIpRelayInformationOption.setStatus("current")


class _RcIpDhcpIpOptionRowNumCurrent_Type(Integer32):
    """Custom type rcIpDhcpIpOptionRowNumCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RcIpDhcpIpOptionRowNumCurrent_Type.__name__ = "Integer32"
_RcIpDhcpIpOptionRowNumCurrent_Object = MibScalar
rcIpDhcpIpOptionRowNumCurrent = _RcIpDhcpIpOptionRowNumCurrent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 14),
    _RcIpDhcpIpOptionRowNumCurrent_Type()
)
rcIpDhcpIpOptionRowNumCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpIpOptionRowNumCurrent.setStatus("current")


class _RcIpDhcpIpOptionRowNumHistoryMax_Type(Integer32):
    """Custom type rcIpDhcpIpOptionRowNumHistoryMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RcIpDhcpIpOptionRowNumHistoryMax_Type.__name__ = "Integer32"
_RcIpDhcpIpOptionRowNumHistoryMax_Object = MibScalar
rcIpDhcpIpOptionRowNumHistoryMax = _RcIpDhcpIpOptionRowNumHistoryMax_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 1, 15),
    _RcIpDhcpIpOptionRowNumHistoryMax_Type()
)
rcIpDhcpIpOptionRowNumHistoryMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpIpOptionRowNumHistoryMax.setStatus("current")
_RcIpDhcpServerStatistics_ObjectIdentity = ObjectIdentity
rcIpDhcpServerStatistics = _RcIpDhcpServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2)
)
_RcIpDhcpServerStatsBootps_Type = Counter32
_RcIpDhcpServerStatsBootps_Object = MibScalar
rcIpDhcpServerStatsBootps = _RcIpDhcpServerStatsBootps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 1),
    _RcIpDhcpServerStatsBootps_Type()
)
rcIpDhcpServerStatsBootps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsBootps.setStatus("mandatory")
_RcIpDhcpServerStatsDiscovers_Type = Counter32
_RcIpDhcpServerStatsDiscovers_Object = MibScalar
rcIpDhcpServerStatsDiscovers = _RcIpDhcpServerStatsDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 2),
    _RcIpDhcpServerStatsDiscovers_Type()
)
rcIpDhcpServerStatsDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsDiscovers.setStatus("mandatory")
_RcIpDhcpServerStatsRequests_Type = Counter32
_RcIpDhcpServerStatsRequests_Object = MibScalar
rcIpDhcpServerStatsRequests = _RcIpDhcpServerStatsRequests_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 3),
    _RcIpDhcpServerStatsRequests_Type()
)
rcIpDhcpServerStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsRequests.setStatus("mandatory")
_RcIpDhcpServerStatsReleases_Type = Counter32
_RcIpDhcpServerStatsReleases_Object = MibScalar
rcIpDhcpServerStatsReleases = _RcIpDhcpServerStatsReleases_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 4),
    _RcIpDhcpServerStatsReleases_Type()
)
rcIpDhcpServerStatsReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsReleases.setStatus("mandatory")
_RcIpDhcpServerStatsOffers_Type = Counter32
_RcIpDhcpServerStatsOffers_Object = MibScalar
rcIpDhcpServerStatsOffers = _RcIpDhcpServerStatsOffers_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 5),
    _RcIpDhcpServerStatsOffers_Type()
)
rcIpDhcpServerStatsOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsOffers.setStatus("mandatory")
_RcIpDhcpServerStatsAcks_Type = Counter32
_RcIpDhcpServerStatsAcks_Object = MibScalar
rcIpDhcpServerStatsAcks = _RcIpDhcpServerStatsAcks_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 6),
    _RcIpDhcpServerStatsAcks_Type()
)
rcIpDhcpServerStatsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsAcks.setStatus("mandatory")
_RcIpDhcpServerStatsNacks_Type = Counter32
_RcIpDhcpServerStatsNacks_Object = MibScalar
rcIpDhcpServerStatsNacks = _RcIpDhcpServerStatsNacks_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 7),
    _RcIpDhcpServerStatsNacks_Type()
)
rcIpDhcpServerStatsNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsNacks.setStatus("mandatory")
_RcIpDhcpServerStatsDeclines_Type = Counter32
_RcIpDhcpServerStatsDeclines_Object = MibScalar
rcIpDhcpServerStatsDeclines = _RcIpDhcpServerStatsDeclines_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 8),
    _RcIpDhcpServerStatsDeclines_Type()
)
rcIpDhcpServerStatsDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsDeclines.setStatus("mandatory")
_RcIpDhcpServerStatsInformations_Type = Counter32
_RcIpDhcpServerStatsInformations_Object = MibScalar
rcIpDhcpServerStatsInformations = _RcIpDhcpServerStatsInformations_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 9),
    _RcIpDhcpServerStatsInformations_Type()
)
rcIpDhcpServerStatsInformations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsInformations.setStatus("mandatory")
_RcIpDhcpServerStatsUnknows_Type = Counter32
_RcIpDhcpServerStatsUnknows_Object = MibScalar
rcIpDhcpServerStatsUnknows = _RcIpDhcpServerStatsUnknows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 10),
    _RcIpDhcpServerStatsUnknows_Type()
)
rcIpDhcpServerStatsUnknows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsUnknows.setStatus("mandatory")
_RcIpDhcpServerStatsPackets_Type = Counter32
_RcIpDhcpServerStatsPackets_Object = MibScalar
rcIpDhcpServerStatsPackets = _RcIpDhcpServerStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 2, 11),
    _RcIpDhcpServerStatsPackets_Type()
)
rcIpDhcpServerStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpServerStatsPackets.setStatus("mandatory")
_RcIpDhcpIpLease_ObjectIdentity = ObjectIdentity
rcIpDhcpIpLease = _RcIpDhcpIpLease_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 3)
)
_RcIpDhcpIpLeaseTable_Object = MibTable
rcIpDhcpIpLeaseTable = _RcIpDhcpIpLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 3, 1)
)
if mibBuilder.loadTexts:
    rcIpDhcpIpLeaseTable.setStatus("current")
_RcIpDhcpIpLeaseEntry_Object = MibTableRow
rcIpDhcpIpLeaseEntry = _RcIpDhcpIpLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 3, 1, 1)
)
rcIpDhcpIpLeaseEntry.setIndexNames(
    (0, "IPDHCP-SERVER-MIB", "rcIpDhcpIpLeaseIndex"),
)
if mibBuilder.loadTexts:
    rcIpDhcpIpLeaseEntry.setStatus("current")
_RcIpDhcpIpLeaseIndex_Type = Integer32
_RcIpDhcpIpLeaseIndex_Object = MibTableColumn
rcIpDhcpIpLeaseIndex = _RcIpDhcpIpLeaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 3, 1, 1, 1),
    _RcIpDhcpIpLeaseIndex_Type()
)
rcIpDhcpIpLeaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIpDhcpIpLeaseIndex.setStatus("current")
_RcIpDhcpIpLeaseIpAddres_Type = IpAddress
_RcIpDhcpIpLeaseIpAddres_Object = MibTableColumn
rcIpDhcpIpLeaseIpAddres = _RcIpDhcpIpLeaseIpAddres_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 3, 1, 1, 2),
    _RcIpDhcpIpLeaseIpAddres_Type()
)
rcIpDhcpIpLeaseIpAddres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpIpLeaseIpAddres.setStatus("current")
_RcIpDhcpIpLeaseClientMacAddress_Type = MacAddress
_RcIpDhcpIpLeaseClientMacAddress_Object = MibTableColumn
rcIpDhcpIpLeaseClientMacAddress = _RcIpDhcpIpLeaseClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 3, 1, 1, 3),
    _RcIpDhcpIpLeaseClientMacAddress_Type()
)
rcIpDhcpIpLeaseClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpIpLeaseClientMacAddress.setStatus("current")
_RcIpDhcpIpLeaseExpiration_Type = Integer32
_RcIpDhcpIpLeaseExpiration_Object = MibTableColumn
rcIpDhcpIpLeaseExpiration = _RcIpDhcpIpLeaseExpiration_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 3, 1, 1, 4),
    _RcIpDhcpIpLeaseExpiration_Type()
)
rcIpDhcpIpLeaseExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpIpLeaseExpiration.setStatus("current")
_RcIpDhcpIpLeaseIpInterface_Type = Integer32
_RcIpDhcpIpLeaseIpInterface_Object = MibTableColumn
rcIpDhcpIpLeaseIpInterface = _RcIpDhcpIpLeaseIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 29, 3, 1, 1, 5),
    _RcIpDhcpIpLeaseIpInterface_Type()
)
rcIpDhcpIpLeaseIpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIpDhcpIpLeaseIpInterface.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPDHCP-SERVER-MIB",
    **{"rcIpDhcpServer": rcIpDhcpServer,
       "rcIpDhcpServerConfig": rcIpDhcpServerConfig,
       "rcIpDhcpPropEnable": rcIpDhcpPropEnable,
       "rcIpDhcpIpNextIndex": rcIpDhcpIpNextIndex,
       "rcIpDhcpMaxLease": rcIpDhcpMaxLease,
       "rcIpDhcpMinLease": rcIpDhcpMinLease,
       "rcIpDhcpDefLease": rcIpDhcpDefLease,
       "rcIpDhcpVlanAuth": rcIpDhcpVlanAuth,
       "rcIpDhcpServerStartTime": rcIpDhcpServerStartTime,
       "rcIpDhcpIpIfTable": rcIpDhcpIpIfTable,
       "rcIpDhcpIpIfEntry": rcIpDhcpIpIfEntry,
       "rcIpDhcpIpIfIndex": rcIpDhcpIpIfIndex,
       "rcIpDhcpIpIfDhcpsEnable": rcIpDhcpIpIfDhcpsEnable,
       "rcIpDhcpIpTable": rcIpDhcpIpTable,
       "rcIpDhcpIpEntry": rcIpDhcpIpEntry,
       "rcIpDhcpIpIndex": rcIpDhcpIpIndex,
       "rcIpDhcpIpEntryName": rcIpDhcpIpEntryName,
       "rcIpDhcpIpInterface": rcIpDhcpIpInterface,
       "rcIpDhcpIpStartIp": rcIpDhcpIpStartIp,
       "rcIpDhcpIpEndIp": rcIpDhcpIpEndIp,
       "rcIpDhcpIpNetmask": rcIpDhcpIpNetmask,
       "rcIpDhcpIpGateway": rcIpDhcpIpGateway,
       "rcIpDhcpIpDnsServer": rcIpDhcpIpDnsServer,
       "rcIpDhcpIpSecondaryDnsServer": rcIpDhcpIpSecondaryDnsServer,
       "rcIpDhcpIpRowStatus": rcIpDhcpIpRowStatus,
       "rcIpDhcpIpTftpSvrAddress": rcIpDhcpIpTftpSvrAddress,
       "rcIpDhcpIpBootfileName": rcIpDhcpIpBootfileName,
       "rcIpDhcpIpMaxLease": rcIpDhcpIpMaxLease,
       "rcIpDhcpIpMinLease": rcIpDhcpIpMinLease,
       "rcIpDhcpIpDefLease": rcIpDhcpIpDefLease,
       "rcIpDhcpRelayNextIndex": rcIpDhcpRelayNextIndex,
       "rcIpDhcpRelayTable": rcIpDhcpRelayTable,
       "rcIpDhcpRelayEntry": rcIpDhcpRelayEntry,
       "rcIpDhcpRelayIndex": rcIpDhcpRelayIndex,
       "rcIpDhcpRelayAddress": rcIpDhcpRelayAddress,
       "rcIpDhcpRelayMask": rcIpDhcpRelayMask,
       "rcIpDhcpRelayRowStatus": rcIpDhcpRelayRowStatus,
       "rcIpDhcpIpVendorOptTable": rcIpDhcpIpVendorOptTable,
       "rcIpDhcpIpVendorOptEntry": rcIpDhcpIpVendorOptEntry,
       "rcIpDhcpIpOptionCode": rcIpDhcpIpOptionCode,
       "rcIpDhcpIpOptionType": rcIpDhcpIpOptionType,
       "rcIpDhcpIpOptionContents": rcIpDhcpIpOptionContents,
       "rcIpDhcpIpOptionLength": rcIpDhcpIpOptionLength,
       "rcIpDhcpIpOptionRowStatus": rcIpDhcpIpOptionRowStatus,
       "rcIpDhcpIpRelayInformationOption": rcIpDhcpIpRelayInformationOption,
       "rcIpDhcpIpOptionRowNumCurrent": rcIpDhcpIpOptionRowNumCurrent,
       "rcIpDhcpIpOptionRowNumHistoryMax": rcIpDhcpIpOptionRowNumHistoryMax,
       "rcIpDhcpServerStatistics": rcIpDhcpServerStatistics,
       "rcIpDhcpServerStatsBootps": rcIpDhcpServerStatsBootps,
       "rcIpDhcpServerStatsDiscovers": rcIpDhcpServerStatsDiscovers,
       "rcIpDhcpServerStatsRequests": rcIpDhcpServerStatsRequests,
       "rcIpDhcpServerStatsReleases": rcIpDhcpServerStatsReleases,
       "rcIpDhcpServerStatsOffers": rcIpDhcpServerStatsOffers,
       "rcIpDhcpServerStatsAcks": rcIpDhcpServerStatsAcks,
       "rcIpDhcpServerStatsNacks": rcIpDhcpServerStatsNacks,
       "rcIpDhcpServerStatsDeclines": rcIpDhcpServerStatsDeclines,
       "rcIpDhcpServerStatsInformations": rcIpDhcpServerStatsInformations,
       "rcIpDhcpServerStatsUnknows": rcIpDhcpServerStatsUnknows,
       "rcIpDhcpServerStatsPackets": rcIpDhcpServerStatsPackets,
       "rcIpDhcpIpLease": rcIpDhcpIpLease,
       "rcIpDhcpIpLeaseTable": rcIpDhcpIpLeaseTable,
       "rcIpDhcpIpLeaseEntry": rcIpDhcpIpLeaseEntry,
       "rcIpDhcpIpLeaseIndex": rcIpDhcpIpLeaseIndex,
       "rcIpDhcpIpLeaseIpAddres": rcIpDhcpIpLeaseIpAddres,
       "rcIpDhcpIpLeaseClientMacAddress": rcIpDhcpIpLeaseClientMacAddress,
       "rcIpDhcpIpLeaseExpiration": rcIpDhcpIpLeaseExpiration,
       "rcIpDhcpIpLeaseIpInterface": rcIpDhcpIpLeaseIpInterface}
)
