# SNMP MIB module (FS-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-CLUSTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:14 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

fsClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31)
)
if mibBuilder.loadTexts:
    fsClusterMIB.setRevisions(
        ("2012-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsClusterMIBObjects_ObjectIdentity = ObjectIdentity
fsClusterMIBObjects = _FsClusterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1)
)


class _FsClusterName_Type(DisplayString):
    """Custom type fsClusterName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FsClusterName_Type.__name__ = "DisplayString"
_FsClusterName_Object = MibScalar
fsClusterName = _FsClusterName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 1),
    _FsClusterName_Type()
)
fsClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterName.setStatus("current")


class _FsClusterStatus_Type(EnabledStatus):
    """Custom type fsClusterStatus based on EnabledStatus"""
    defaultValue = 1


_FsClusterStatus_Type.__name__ = "EnabledStatus"
_FsClusterStatus_Object = MibScalar
fsClusterStatus = _FsClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 2),
    _FsClusterStatus_Type()
)
fsClusterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterStatus.setStatus("current")
_FsClusterCmdMacAddress_Type = MacAddress
_FsClusterCmdMacAddress_Object = MibScalar
fsClusterCmdMacAddress = _FsClusterCmdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 3),
    _FsClusterCmdMacAddress_Type()
)
fsClusterCmdMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCmdMacAddress.setStatus("current")
_FsClusterCmdName_Type = DisplayString
_FsClusterCmdName_Object = MibScalar
fsClusterCmdName = _FsClusterCmdName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 4),
    _FsClusterCmdName_Type()
)
fsClusterCmdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCmdName.setStatus("current")


class _FsClusterVlan_Type(Integer32):
    """Custom type fsClusterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_FsClusterVlan_Type.__name__ = "Integer32"
_FsClusterVlan_Object = MibScalar
fsClusterVlan = _FsClusterVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 5),
    _FsClusterVlan_Type()
)
fsClusterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterVlan.setStatus("current")


class _FsClusterHopsLimit_Type(Integer32):
    """Custom type fsClusterHopsLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsClusterHopsLimit_Type.__name__ = "Integer32"
_FsClusterHopsLimit_Object = MibScalar
fsClusterHopsLimit = _FsClusterHopsLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 6),
    _FsClusterHopsLimit_Type()
)
fsClusterHopsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterHopsLimit.setStatus("current")


class _FsClusterTimerTopo_Type(Integer32):
    """Custom type fsClusterTimerTopo based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_FsClusterTimerTopo_Type.__name__ = "Integer32"
_FsClusterTimerTopo_Object = MibScalar
fsClusterTimerTopo = _FsClusterTimerTopo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 7),
    _FsClusterTimerTopo_Type()
)
fsClusterTimerTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterTimerTopo.setStatus("current")


class _FsClusterTimerHello_Type(Integer32):
    """Custom type fsClusterTimerHello based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_FsClusterTimerHello_Type.__name__ = "Integer32"
_FsClusterTimerHello_Object = MibScalar
fsClusterTimerHello = _FsClusterTimerHello_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 8),
    _FsClusterTimerHello_Type()
)
fsClusterTimerHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterTimerHello.setStatus("current")


class _FsClusterTimerHold_Type(Integer32):
    """Custom type fsClusterTimerHold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_FsClusterTimerHold_Type.__name__ = "Integer32"
_FsClusterTimerHold_Object = MibScalar
fsClusterTimerHold = _FsClusterTimerHold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 9),
    _FsClusterTimerHold_Type()
)
fsClusterTimerHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterTimerHold.setStatus("current")
_FsClusterTftpServer_Type = IpAddress
_FsClusterTftpServer_Object = MibScalar
fsClusterTftpServer = _FsClusterTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 10),
    _FsClusterTftpServer_Type()
)
fsClusterTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterTftpServer.setStatus("current")


class _FsClusterNumberOfMembers_Type(Integer32):
    """Custom type fsClusterNumberOfMembers based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FsClusterNumberOfMembers_Type.__name__ = "Integer32"
_FsClusterNumberOfMembers_Object = MibScalar
fsClusterNumberOfMembers = _FsClusterNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 11),
    _FsClusterNumberOfMembers_Type()
)
fsClusterNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterNumberOfMembers.setStatus("current")


class _FsClusterMaxNumberOfMembers_Type(Integer32):
    """Custom type fsClusterMaxNumberOfMembers based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FsClusterMaxNumberOfMembers_Type.__name__ = "Integer32"
_FsClusterMaxNumberOfMembers_Object = MibScalar
fsClusterMaxNumberOfMembers = _FsClusterMaxNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 12),
    _FsClusterMaxNumberOfMembers_Type()
)
fsClusterMaxNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMaxNumberOfMembers.setStatus("current")


class _FsClusterDevMaxCapicity_Type(Unsigned32):
    """Custom type fsClusterDevMaxCapicity based on Unsigned32"""
    defaultValue = 0


_FsClusterDevMaxCapicity_Type.__name__ = "Unsigned32"
_FsClusterDevMaxCapicity_Object = MibScalar
fsClusterDevMaxCapicity = _FsClusterDevMaxCapicity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 13),
    _FsClusterDevMaxCapicity_Type()
)
fsClusterDevMaxCapicity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterDevMaxCapicity.setStatus("current")


class _FsClusterAutoAdd_Type(Integer32):
    """Custom type fsClusterAutoAdd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable-with-def", 0),
          ("enable", 1),
          ("disabled-with-static", 2),
          ("disabled-with-del", 3))
    )


_FsClusterAutoAdd_Type.__name__ = "Integer32"
_FsClusterAutoAdd_Object = MibScalar
fsClusterAutoAdd = _FsClusterAutoAdd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 14),
    _FsClusterAutoAdd_Type()
)
fsClusterAutoAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterAutoAdd.setStatus("current")


class _FsClusterExplore_Type(EnabledStatus):
    """Custom type fsClusterExplore based on EnabledStatus"""
    defaultValue = 2


_FsClusterExplore_Type.__name__ = "EnabledStatus"
_FsClusterExplore_Object = MibScalar
fsClusterExplore = _FsClusterExplore_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 15),
    _FsClusterExplore_Type()
)
fsClusterExplore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterExplore.setStatus("current")
_FsClusterSpecifyAdmin_ObjectIdentity = ObjectIdentity
fsClusterSpecifyAdmin = _FsClusterSpecifyAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 16)
)
_FsClusterSpecifyAdminAddress_Type = MacAddress
_FsClusterSpecifyAdminAddress_Object = MibScalar
fsClusterSpecifyAdminAddress = _FsClusterSpecifyAdminAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 16, 1),
    _FsClusterSpecifyAdminAddress_Type()
)
fsClusterSpecifyAdminAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterSpecifyAdminAddress.setStatus("current")


class _FsClusterSpecifyAdminName_Type(DisplayString):
    """Custom type fsClusterSpecifyAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FsClusterSpecifyAdminName_Type.__name__ = "DisplayString"
_FsClusterSpecifyAdminName_Object = MibScalar
fsClusterSpecifyAdminName = _FsClusterSpecifyAdminName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 16, 2),
    _FsClusterSpecifyAdminName_Type()
)
fsClusterSpecifyAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterSpecifyAdminName.setStatus("current")
_FsClusterDeviceInfo_ObjectIdentity = ObjectIdentity
fsClusterDeviceInfo = _FsClusterDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 17)
)


class _FsClusterDeviceEnable_Type(EnabledStatus):
    """Custom type fsClusterDeviceEnable based on EnabledStatus"""
    defaultValue = 1


_FsClusterDeviceEnable_Type.__name__ = "EnabledStatus"
_FsClusterDeviceEnable_Object = MibScalar
fsClusterDeviceEnable = _FsClusterDeviceEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 17, 1),
    _FsClusterDeviceEnable_Type()
)
fsClusterDeviceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterDeviceEnable.setStatus("current")


class _FsClusterDeviceRole_Type(Integer32):
    """Custom type fsClusterDeviceRole based on Integer32"""
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
        *(("candidateDevice", 1),
          ("managerDevice", 2),
          ("memberDevice", 3))
    )


_FsClusterDeviceRole_Type.__name__ = "Integer32"
_FsClusterDeviceRole_Object = MibScalar
fsClusterDeviceRole = _FsClusterDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 17, 2),
    _FsClusterDeviceRole_Type()
)
fsClusterDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterDeviceRole.setStatus("current")
_FsClusterDeviceIP_Type = IpAddress
_FsClusterDeviceIP_Object = MibScalar
fsClusterDeviceIP = _FsClusterDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 17, 3),
    _FsClusterDeviceIP_Type()
)
fsClusterDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterDeviceIP.setStatus("current")


class _FsClusterDeviceSn_Type(Integer32):
    """Custom type fsClusterDeviceSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_FsClusterDeviceSn_Type.__name__ = "Integer32"
_FsClusterDeviceSn_Object = MibScalar
fsClusterDeviceSn = _FsClusterDeviceSn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 17, 4),
    _FsClusterDeviceSn_Type()
)
fsClusterDeviceSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterDeviceSn.setStatus("current")
_FsClusterIpPoolTable_Object = MibTable
fsClusterIpPoolTable = _FsClusterIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 18)
)
if mibBuilder.loadTexts:
    fsClusterIpPoolTable.setStatus("current")
_FsClusterIpPoolEntry_Object = MibTableRow
fsClusterIpPoolEntry = _FsClusterIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 18, 1)
)
fsClusterIpPoolEntry.setIndexNames(
    (0, "FS-CLUSTER-MIB", "fsClusterIpPool"),
    (0, "FS-CLUSTER-MIB", "fsClusterIpMask"),
)
if mibBuilder.loadTexts:
    fsClusterIpPoolEntry.setStatus("current")
_FsClusterIpPool_Type = IpAddress
_FsClusterIpPool_Object = MibTableColumn
fsClusterIpPool = _FsClusterIpPool_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 18, 1, 1),
    _FsClusterIpPool_Type()
)
fsClusterIpPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterIpPool.setStatus("current")
_FsClusterIpMask_Type = IpAddress
_FsClusterIpMask_Object = MibTableColumn
fsClusterIpMask = _FsClusterIpMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 18, 1, 2),
    _FsClusterIpMask_Type()
)
fsClusterIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterIpMask.setStatus("current")
_FsClusterIpPoolRowStatus_Type = RowStatus
_FsClusterIpPoolRowStatus_Object = MibTableColumn
fsClusterIpPoolRowStatus = _FsClusterIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 18, 1, 3),
    _FsClusterIpPoolRowStatus_Type()
)
fsClusterIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsClusterIpPoolRowStatus.setStatus("current")
_FsClusterMemberAddTable_Object = MibTable
fsClusterMemberAddTable = _FsClusterMemberAddTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 19)
)
if mibBuilder.loadTexts:
    fsClusterMemberAddTable.setStatus("current")
_FsClusterMemberAddEntry_Object = MibTableRow
fsClusterMemberAddEntry = _FsClusterMemberAddEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 19, 1)
)
fsClusterMemberAddEntry.setIndexNames(
    (0, "FS-CLUSTER-MIB", "fsClusterMemberAddSn"),
)
if mibBuilder.loadTexts:
    fsClusterMemberAddEntry.setStatus("current")


class _FsClusterMemberAddSn_Type(Integer32):
    """Custom type fsClusterMemberAddSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_FsClusterMemberAddSn_Type.__name__ = "Integer32"
_FsClusterMemberAddSn_Object = MibTableColumn
fsClusterMemberAddSn = _FsClusterMemberAddSn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 19, 1, 1),
    _FsClusterMemberAddSn_Type()
)
fsClusterMemberAddSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberAddSn.setStatus("current")
_FsClusterMemberAddMacAddress_Type = MacAddress
_FsClusterMemberAddMacAddress_Object = MibTableColumn
fsClusterMemberAddMacAddress = _FsClusterMemberAddMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 19, 1, 2),
    _FsClusterMemberAddMacAddress_Type()
)
fsClusterMemberAddMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsClusterMemberAddMacAddress.setStatus("current")
_FsClusterMemberAddRowStatus_Type = RowStatus
_FsClusterMemberAddRowStatus_Object = MibTableColumn
fsClusterMemberAddRowStatus = _FsClusterMemberAddRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 19, 1, 3),
    _FsClusterMemberAddRowStatus_Type()
)
fsClusterMemberAddRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsClusterMemberAddRowStatus.setStatus("current")
_FsClusterMemberTable_Object = MibTable
fsClusterMemberTable = _FsClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20)
)
if mibBuilder.loadTexts:
    fsClusterMemberTable.setStatus("current")
_FsClusterMemberEntry_Object = MibTableRow
fsClusterMemberEntry = _FsClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1)
)
fsClusterMemberEntry.setIndexNames(
    (0, "FS-CLUSTER-MIB", "fsClusterMemberSn"),
    (0, "FS-CLUSTER-MIB", "fsClusterMemberUpMAC"),
    (0, "FS-CLUSTER-MIB", "fsClusterMemberLcIfx"),
    (0, "FS-CLUSTER-MIB", "fsClusterMemberUpIfx"),
)
if mibBuilder.loadTexts:
    fsClusterMemberEntry.setStatus("current")
_FsClusterMemberSn_Type = Unsigned32
_FsClusterMemberSn_Object = MibTableColumn
fsClusterMemberSn = _FsClusterMemberSn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 1),
    _FsClusterMemberSn_Type()
)
fsClusterMemberSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberSn.setStatus("current")
_FsClusterMemberUpMAC_Type = MacAddress
_FsClusterMemberUpMAC_Object = MibTableColumn
fsClusterMemberUpMAC = _FsClusterMemberUpMAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 2),
    _FsClusterMemberUpMAC_Type()
)
fsClusterMemberUpMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberUpMAC.setStatus("current")
_FsClusterMemberLcIfx_Type = Unsigned32
_FsClusterMemberLcIfx_Object = MibTableColumn
fsClusterMemberLcIfx = _FsClusterMemberLcIfx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 3),
    _FsClusterMemberLcIfx_Type()
)
fsClusterMemberLcIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberLcIfx.setStatus("current")
_FsClusterMemberUpIfx_Type = Unsigned32
_FsClusterMemberUpIfx_Object = MibTableColumn
fsClusterMemberUpIfx = _FsClusterMemberUpIfx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 4),
    _FsClusterMemberUpIfx_Type()
)
fsClusterMemberUpIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberUpIfx.setStatus("current")
_FsClusterMemberLcPort_Type = DisplayString
_FsClusterMemberLcPort_Object = MibTableColumn
fsClusterMemberLcPort = _FsClusterMemberLcPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 5),
    _FsClusterMemberLcPort_Type()
)
fsClusterMemberLcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberLcPort.setStatus("current")
_FsClusterMemberUpPort_Type = DisplayString
_FsClusterMemberUpPort_Object = MibTableColumn
fsClusterMemberUpPort = _FsClusterMemberUpPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 6),
    _FsClusterMemberUpPort_Type()
)
fsClusterMemberUpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberUpPort.setStatus("current")
_FsClusterMemberMacAddress_Type = MacAddress
_FsClusterMemberMacAddress_Object = MibTableColumn
fsClusterMemberMacAddress = _FsClusterMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 7),
    _FsClusterMemberMacAddress_Type()
)
fsClusterMemberMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberMacAddress.setStatus("current")
_FsClusterMemberName_Type = DisplayString
_FsClusterMemberName_Object = MibTableColumn
fsClusterMemberName = _FsClusterMemberName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 8),
    _FsClusterMemberName_Type()
)
fsClusterMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberName.setStatus("current")
_FsClusterMemberIp_Type = IpAddress
_FsClusterMemberIp_Object = MibTableColumn
fsClusterMemberIp = _FsClusterMemberIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 9),
    _FsClusterMemberIp_Type()
)
fsClusterMemberIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberIp.setStatus("current")
_FsClusterMemberHops_Type = Unsigned32
_FsClusterMemberHops_Object = MibTableColumn
fsClusterMemberHops = _FsClusterMemberHops_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 10),
    _FsClusterMemberHops_Type()
)
fsClusterMemberHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberHops.setStatus("current")
_FsClusterMemberState_Type = DisplayString
_FsClusterMemberState_Object = MibTableColumn
fsClusterMemberState = _FsClusterMemberState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 11),
    _FsClusterMemberState_Type()
)
fsClusterMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberState.setStatus("current")
_FsClusterMemberUpSn_Type = Unsigned32
_FsClusterMemberUpSn_Object = MibTableColumn
fsClusterMemberUpSn = _FsClusterMemberUpSn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 12),
    _FsClusterMemberUpSn_Type()
)
fsClusterMemberUpSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberUpSn.setStatus("current")
_FsClusterMemberLastTopoUpdateTime_Type = Unsigned32
_FsClusterMemberLastTopoUpdateTime_Object = MibTableColumn
fsClusterMemberLastTopoUpdateTime = _FsClusterMemberLastTopoUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 13),
    _FsClusterMemberLastTopoUpdateTime_Type()
)
fsClusterMemberLastTopoUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberLastTopoUpdateTime.setStatus("current")
_FsClusterMemberLastUdpUpdateTime_Type = Unsigned32
_FsClusterMemberLastUdpUpdateTime_Object = MibTableColumn
fsClusterMemberLastUdpUpdateTime = _FsClusterMemberLastUdpUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 14),
    _FsClusterMemberLastUdpUpdateTime_Type()
)
fsClusterMemberLastUdpUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberLastUdpUpdateTime.setStatus("current")
_FsClusterMemberNoRecvTopoRspCount_Type = Unsigned32
_FsClusterMemberNoRecvTopoRspCount_Object = MibTableColumn
fsClusterMemberNoRecvTopoRspCount = _FsClusterMemberNoRecvTopoRspCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 15),
    _FsClusterMemberNoRecvTopoRspCount_Type()
)
fsClusterMemberNoRecvTopoRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberNoRecvTopoRspCount.setStatus("current")
_FsClusterMemberNoRecvUdpRspCount_Type = Unsigned32
_FsClusterMemberNoRecvUdpRspCount_Object = MibTableColumn
fsClusterMemberNoRecvUdpRspCount = _FsClusterMemberNoRecvUdpRspCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 16),
    _FsClusterMemberNoRecvUdpRspCount_Type()
)
fsClusterMemberNoRecvUdpRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterMemberNoRecvUdpRspCount.setStatus("current")
_FsClusterMemberReload_Type = EnabledStatus
_FsClusterMemberReload_Object = MibTableColumn
fsClusterMemberReload = _FsClusterMemberReload_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 20, 1, 17),
    _FsClusterMemberReload_Type()
)
fsClusterMemberReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClusterMemberReload.setStatus("current")
_FsClusterCandidateTable_Object = MibTable
fsClusterCandidateTable = _FsClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21)
)
if mibBuilder.loadTexts:
    fsClusterCandidateTable.setStatus("current")
_FsClusterCandidateEntry_Object = MibTableRow
fsClusterCandidateEntry = _FsClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1)
)
fsClusterCandidateEntry.setIndexNames(
    (0, "FS-CLUSTER-MIB", "fsClusterCandidateMacAddress"),
    (0, "FS-CLUSTER-MIB", "fsClusterCandidateUpMAC"),
    (0, "FS-CLUSTER-MIB", "fsClusterCandidateLcIfx"),
    (0, "FS-CLUSTER-MIB", "fsClusterCandidateUpIfx"),
)
if mibBuilder.loadTexts:
    fsClusterCandidateEntry.setStatus("current")
_FsClusterCandidateMacAddress_Type = MacAddress
_FsClusterCandidateMacAddress_Object = MibTableColumn
fsClusterCandidateMacAddress = _FsClusterCandidateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1, 1),
    _FsClusterCandidateMacAddress_Type()
)
fsClusterCandidateMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCandidateMacAddress.setStatus("current")
_FsClusterCandidateUpMAC_Type = MacAddress
_FsClusterCandidateUpMAC_Object = MibTableColumn
fsClusterCandidateUpMAC = _FsClusterCandidateUpMAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1, 2),
    _FsClusterCandidateUpMAC_Type()
)
fsClusterCandidateUpMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCandidateUpMAC.setStatus("current")
_FsClusterCandidateLcIfx_Type = Unsigned32
_FsClusterCandidateLcIfx_Object = MibTableColumn
fsClusterCandidateLcIfx = _FsClusterCandidateLcIfx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1, 3),
    _FsClusterCandidateLcIfx_Type()
)
fsClusterCandidateLcIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCandidateLcIfx.setStatus("current")
_FsClusterCandidateUpIfx_Type = Unsigned32
_FsClusterCandidateUpIfx_Object = MibTableColumn
fsClusterCandidateUpIfx = _FsClusterCandidateUpIfx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1, 4),
    _FsClusterCandidateUpIfx_Type()
)
fsClusterCandidateUpIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCandidateUpIfx.setStatus("current")
_FsClusterCandidateLcPort_Type = DisplayString
_FsClusterCandidateLcPort_Object = MibTableColumn
fsClusterCandidateLcPort = _FsClusterCandidateLcPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1, 5),
    _FsClusterCandidateLcPort_Type()
)
fsClusterCandidateLcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCandidateLcPort.setStatus("current")
_FsClusterCandidateUpPort_Type = DisplayString
_FsClusterCandidateUpPort_Object = MibTableColumn
fsClusterCandidateUpPort = _FsClusterCandidateUpPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1, 6),
    _FsClusterCandidateUpPort_Type()
)
fsClusterCandidateUpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCandidateUpPort.setStatus("current")
_FsClusterCandidateUpSn_Type = Unsigned32
_FsClusterCandidateUpSn_Object = MibTableColumn
fsClusterCandidateUpSn = _FsClusterCandidateUpSn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1, 7),
    _FsClusterCandidateUpSn_Type()
)
fsClusterCandidateUpSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCandidateUpSn.setStatus("current")
_FsClusterCandidateHops_Type = Unsigned32
_FsClusterCandidateHops_Object = MibTableColumn
fsClusterCandidateHops = _FsClusterCandidateHops_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1, 8),
    _FsClusterCandidateHops_Type()
)
fsClusterCandidateHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCandidateHops.setStatus("current")
_FsClusterCandidateState_Type = DisplayString
_FsClusterCandidateState_Object = MibTableColumn
fsClusterCandidateState = _FsClusterCandidateState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 21, 1, 9),
    _FsClusterCandidateState_Type()
)
fsClusterCandidateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterCandidateState.setStatus("current")
_FsClusterBlacklistTable_Object = MibTable
fsClusterBlacklistTable = _FsClusterBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 22)
)
if mibBuilder.loadTexts:
    fsClusterBlacklistTable.setStatus("current")
_FsClusterBlacklistEntry_Object = MibTableRow
fsClusterBlacklistEntry = _FsClusterBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 22, 1)
)
fsClusterBlacklistEntry.setIndexNames(
    (0, "FS-CLUSTER-MIB", "fsClusterBlacklistMacAddress"),
)
if mibBuilder.loadTexts:
    fsClusterBlacklistEntry.setStatus("current")
_FsClusterBlacklistMacAddress_Type = MacAddress
_FsClusterBlacklistMacAddress_Object = MibTableColumn
fsClusterBlacklistMacAddress = _FsClusterBlacklistMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 22, 1, 1),
    _FsClusterBlacklistMacAddress_Type()
)
fsClusterBlacklistMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterBlacklistMacAddress.setStatus("current")
_FsClusterBlackListRowStatus_Type = RowStatus
_FsClusterBlackListRowStatus_Object = MibTableColumn
fsClusterBlackListRowStatus = _FsClusterBlackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 22, 1, 2),
    _FsClusterBlackListRowStatus_Type()
)
fsClusterBlackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsClusterBlackListRowStatus.setStatus("current")
_FsClusterPasswordAuth_ObjectIdentity = ObjectIdentity
fsClusterPasswordAuth = _FsClusterPasswordAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23)
)
_FsClusterPasswordAuthPoolTable_Object = MibTable
fsClusterPasswordAuthPoolTable = _FsClusterPasswordAuthPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 1)
)
if mibBuilder.loadTexts:
    fsClusterPasswordAuthPoolTable.setStatus("current")
_FsClusterPasswordAuthPoolEntry_Object = MibTableRow
fsClusterPasswordAuthPoolEntry = _FsClusterPasswordAuthPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 1, 1)
)
fsClusterPasswordAuthPoolEntry.setIndexNames(
    (0, "FS-CLUSTER-MIB", "fsClusterPasswordSn"),
)
if mibBuilder.loadTexts:
    fsClusterPasswordAuthPoolEntry.setStatus("current")


class _FsClusterPasswordSn_Type(Integer32):
    """Custom type fsClusterPasswordSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsClusterPasswordSn_Type.__name__ = "Integer32"
_FsClusterPasswordSn_Object = MibTableColumn
fsClusterPasswordSn = _FsClusterPasswordSn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 1, 1, 1),
    _FsClusterPasswordSn_Type()
)
fsClusterPasswordSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterPasswordSn.setStatus("current")


class _FsClusterPassword_Type(DisplayString):
    """Custom type fsClusterPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_FsClusterPassword_Type.__name__ = "DisplayString"
_FsClusterPassword_Object = MibTableColumn
fsClusterPassword = _FsClusterPassword_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 1, 1, 2),
    _FsClusterPassword_Type()
)
fsClusterPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsClusterPassword.setStatus("current")
_FsClusterPasswordAuthRowStatus_Type = RowStatus
_FsClusterPasswordAuthRowStatus_Object = MibTableColumn
fsClusterPasswordAuthRowStatus = _FsClusterPasswordAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 1, 1, 3),
    _FsClusterPasswordAuthRowStatus_Type()
)
fsClusterPasswordAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsClusterPasswordAuthRowStatus.setStatus("current")
_FsClusterDeviceAuthPasswordTable_Object = MibTable
fsClusterDeviceAuthPasswordTable = _FsClusterDeviceAuthPasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 2)
)
if mibBuilder.loadTexts:
    fsClusterDeviceAuthPasswordTable.setStatus("current")
_FsClusterDeviceAuthPasswordEntry_Object = MibTableRow
fsClusterDeviceAuthPasswordEntry = _FsClusterDeviceAuthPasswordEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 2, 1)
)
fsClusterDeviceAuthPasswordEntry.setIndexNames(
    (0, "FS-CLUSTER-MIB", "fsClusterDeviceMacAddress"),
)
if mibBuilder.loadTexts:
    fsClusterDeviceAuthPasswordEntry.setStatus("current")
_FsClusterDeviceMacAddress_Type = MacAddress
_FsClusterDeviceMacAddress_Object = MibTableColumn
fsClusterDeviceMacAddress = _FsClusterDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 2, 1, 1),
    _FsClusterDeviceMacAddress_Type()
)
fsClusterDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClusterDeviceMacAddress.setStatus("current")


class _FsClusterDevicePassword_Type(DisplayString):
    """Custom type fsClusterDevicePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_FsClusterDevicePassword_Type.__name__ = "DisplayString"
_FsClusterDevicePassword_Object = MibTableColumn
fsClusterDevicePassword = _FsClusterDevicePassword_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 2, 1, 2),
    _FsClusterDevicePassword_Type()
)
fsClusterDevicePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsClusterDevicePassword.setStatus("current")
_FsClusterDevicePasswordRowStatus_Type = RowStatus
_FsClusterDevicePasswordRowStatus_Object = MibTableColumn
fsClusterDevicePasswordRowStatus = _FsClusterDevicePasswordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 1, 23, 2, 1, 3),
    _FsClusterDevicePasswordRowStatus_Type()
)
fsClusterDevicePasswordRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsClusterDevicePasswordRowStatus.setStatus("current")
_FsClusterTraps_ObjectIdentity = ObjectIdentity
fsClusterTraps = _FsClusterTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 2)
)

# Managed Objects groups


# Notification objects

fsClusterMemberStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 2, 1)
)
fsClusterMemberStateChangeTrap.setObjects(
      *(("FS-CLUSTER-MIB", "fsClusterMemberSn"),
        ("FS-CLUSTER-MIB", "fsClusterMemberState"))
)
if mibBuilder.loadTexts:
    fsClusterMemberStateChangeTrap.setStatus(
        "current"
    )

fsClusterMemberFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 2, 2)
)
fsClusterMemberFailureTrap.setObjects(
    ("FS-CLUSTER-MIB", "fsClusterCandidateMacAddress")
)
if mibBuilder.loadTexts:
    fsClusterMemberFailureTrap.setStatus(
        "current"
    )

fsClusterDevMaximumAllowedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 2, 3)
)
if mibBuilder.loadTexts:
    fsClusterDevMaximumAllowedTrap.setStatus(
        "current"
    )

fsClusterMemberMaximumAllowedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 31, 2, 4)
)
if mibBuilder.loadTexts:
    fsClusterMemberMaximumAllowedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-CLUSTER-MIB",
    **{"fsClusterMIB": fsClusterMIB,
       "fsClusterMIBObjects": fsClusterMIBObjects,
       "fsClusterName": fsClusterName,
       "fsClusterStatus": fsClusterStatus,
       "fsClusterCmdMacAddress": fsClusterCmdMacAddress,
       "fsClusterCmdName": fsClusterCmdName,
       "fsClusterVlan": fsClusterVlan,
       "fsClusterHopsLimit": fsClusterHopsLimit,
       "fsClusterTimerTopo": fsClusterTimerTopo,
       "fsClusterTimerHello": fsClusterTimerHello,
       "fsClusterTimerHold": fsClusterTimerHold,
       "fsClusterTftpServer": fsClusterTftpServer,
       "fsClusterNumberOfMembers": fsClusterNumberOfMembers,
       "fsClusterMaxNumberOfMembers": fsClusterMaxNumberOfMembers,
       "fsClusterDevMaxCapicity": fsClusterDevMaxCapicity,
       "fsClusterAutoAdd": fsClusterAutoAdd,
       "fsClusterExplore": fsClusterExplore,
       "fsClusterSpecifyAdmin": fsClusterSpecifyAdmin,
       "fsClusterSpecifyAdminAddress": fsClusterSpecifyAdminAddress,
       "fsClusterSpecifyAdminName": fsClusterSpecifyAdminName,
       "fsClusterDeviceInfo": fsClusterDeviceInfo,
       "fsClusterDeviceEnable": fsClusterDeviceEnable,
       "fsClusterDeviceRole": fsClusterDeviceRole,
       "fsClusterDeviceIP": fsClusterDeviceIP,
       "fsClusterDeviceSn": fsClusterDeviceSn,
       "fsClusterIpPoolTable": fsClusterIpPoolTable,
       "fsClusterIpPoolEntry": fsClusterIpPoolEntry,
       "fsClusterIpPool": fsClusterIpPool,
       "fsClusterIpMask": fsClusterIpMask,
       "fsClusterIpPoolRowStatus": fsClusterIpPoolRowStatus,
       "fsClusterMemberAddTable": fsClusterMemberAddTable,
       "fsClusterMemberAddEntry": fsClusterMemberAddEntry,
       "fsClusterMemberAddSn": fsClusterMemberAddSn,
       "fsClusterMemberAddMacAddress": fsClusterMemberAddMacAddress,
       "fsClusterMemberAddRowStatus": fsClusterMemberAddRowStatus,
       "fsClusterMemberTable": fsClusterMemberTable,
       "fsClusterMemberEntry": fsClusterMemberEntry,
       "fsClusterMemberSn": fsClusterMemberSn,
       "fsClusterMemberUpMAC": fsClusterMemberUpMAC,
       "fsClusterMemberLcIfx": fsClusterMemberLcIfx,
       "fsClusterMemberUpIfx": fsClusterMemberUpIfx,
       "fsClusterMemberLcPort": fsClusterMemberLcPort,
       "fsClusterMemberUpPort": fsClusterMemberUpPort,
       "fsClusterMemberMacAddress": fsClusterMemberMacAddress,
       "fsClusterMemberName": fsClusterMemberName,
       "fsClusterMemberIp": fsClusterMemberIp,
       "fsClusterMemberHops": fsClusterMemberHops,
       "fsClusterMemberState": fsClusterMemberState,
       "fsClusterMemberUpSn": fsClusterMemberUpSn,
       "fsClusterMemberLastTopoUpdateTime": fsClusterMemberLastTopoUpdateTime,
       "fsClusterMemberLastUdpUpdateTime": fsClusterMemberLastUdpUpdateTime,
       "fsClusterMemberNoRecvTopoRspCount": fsClusterMemberNoRecvTopoRspCount,
       "fsClusterMemberNoRecvUdpRspCount": fsClusterMemberNoRecvUdpRspCount,
       "fsClusterMemberReload": fsClusterMemberReload,
       "fsClusterCandidateTable": fsClusterCandidateTable,
       "fsClusterCandidateEntry": fsClusterCandidateEntry,
       "fsClusterCandidateMacAddress": fsClusterCandidateMacAddress,
       "fsClusterCandidateUpMAC": fsClusterCandidateUpMAC,
       "fsClusterCandidateLcIfx": fsClusterCandidateLcIfx,
       "fsClusterCandidateUpIfx": fsClusterCandidateUpIfx,
       "fsClusterCandidateLcPort": fsClusterCandidateLcPort,
       "fsClusterCandidateUpPort": fsClusterCandidateUpPort,
       "fsClusterCandidateUpSn": fsClusterCandidateUpSn,
       "fsClusterCandidateHops": fsClusterCandidateHops,
       "fsClusterCandidateState": fsClusterCandidateState,
       "fsClusterBlacklistTable": fsClusterBlacklistTable,
       "fsClusterBlacklistEntry": fsClusterBlacklistEntry,
       "fsClusterBlacklistMacAddress": fsClusterBlacklistMacAddress,
       "fsClusterBlackListRowStatus": fsClusterBlackListRowStatus,
       "fsClusterPasswordAuth": fsClusterPasswordAuth,
       "fsClusterPasswordAuthPoolTable": fsClusterPasswordAuthPoolTable,
       "fsClusterPasswordAuthPoolEntry": fsClusterPasswordAuthPoolEntry,
       "fsClusterPasswordSn": fsClusterPasswordSn,
       "fsClusterPassword": fsClusterPassword,
       "fsClusterPasswordAuthRowStatus": fsClusterPasswordAuthRowStatus,
       "fsClusterDeviceAuthPasswordTable": fsClusterDeviceAuthPasswordTable,
       "fsClusterDeviceAuthPasswordEntry": fsClusterDeviceAuthPasswordEntry,
       "fsClusterDeviceMacAddress": fsClusterDeviceMacAddress,
       "fsClusterDevicePassword": fsClusterDevicePassword,
       "fsClusterDevicePasswordRowStatus": fsClusterDevicePasswordRowStatus,
       "fsClusterTraps": fsClusterTraps,
       "fsClusterMemberStateChangeTrap": fsClusterMemberStateChangeTrap,
       "fsClusterMemberFailureTrap": fsClusterMemberFailureTrap,
       "fsClusterDevMaximumAllowedTrap": fsClusterDevMaximumAllowedTrap,
       "fsClusterMemberMaximumAllowedTrap": fsClusterMemberMaximumAllowedTrap}
)
