# SNMP MIB module (QTECH-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CLUSTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:51 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

qtechClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31)
)
if mibBuilder.loadTexts:
    qtechClusterMIB.setRevisions(
        ("2012-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechClusterMIBObjects_ObjectIdentity = ObjectIdentity
qtechClusterMIBObjects = _QtechClusterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1)
)


class _QtechClusterName_Type(DisplayString):
    """Custom type qtechClusterName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QtechClusterName_Type.__name__ = "DisplayString"
_QtechClusterName_Object = MibScalar
qtechClusterName = _QtechClusterName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 1),
    _QtechClusterName_Type()
)
qtechClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterName.setStatus("current")


class _QtechClusterStatus_Type(EnabledStatus):
    """Custom type qtechClusterStatus based on EnabledStatus"""
    defaultValue = 1


_QtechClusterStatus_Type.__name__ = "EnabledStatus"
_QtechClusterStatus_Object = MibScalar
qtechClusterStatus = _QtechClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 2),
    _QtechClusterStatus_Type()
)
qtechClusterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterStatus.setStatus("current")
_QtechClusterCmdMacAddress_Type = MacAddress
_QtechClusterCmdMacAddress_Object = MibScalar
qtechClusterCmdMacAddress = _QtechClusterCmdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 3),
    _QtechClusterCmdMacAddress_Type()
)
qtechClusterCmdMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCmdMacAddress.setStatus("current")
_QtechClusterCmdName_Type = DisplayString
_QtechClusterCmdName_Object = MibScalar
qtechClusterCmdName = _QtechClusterCmdName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 4),
    _QtechClusterCmdName_Type()
)
qtechClusterCmdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCmdName.setStatus("current")


class _QtechClusterVlan_Type(Integer32):
    """Custom type qtechClusterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_QtechClusterVlan_Type.__name__ = "Integer32"
_QtechClusterVlan_Object = MibScalar
qtechClusterVlan = _QtechClusterVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 5),
    _QtechClusterVlan_Type()
)
qtechClusterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterVlan.setStatus("current")


class _QtechClusterHopsLimit_Type(Integer32):
    """Custom type qtechClusterHopsLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QtechClusterHopsLimit_Type.__name__ = "Integer32"
_QtechClusterHopsLimit_Object = MibScalar
qtechClusterHopsLimit = _QtechClusterHopsLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 6),
    _QtechClusterHopsLimit_Type()
)
qtechClusterHopsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterHopsLimit.setStatus("current")


class _QtechClusterTimerTopo_Type(Integer32):
    """Custom type qtechClusterTimerTopo based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_QtechClusterTimerTopo_Type.__name__ = "Integer32"
_QtechClusterTimerTopo_Object = MibScalar
qtechClusterTimerTopo = _QtechClusterTimerTopo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 7),
    _QtechClusterTimerTopo_Type()
)
qtechClusterTimerTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterTimerTopo.setStatus("current")


class _QtechClusterTimerHello_Type(Integer32):
    """Custom type qtechClusterTimerHello based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_QtechClusterTimerHello_Type.__name__ = "Integer32"
_QtechClusterTimerHello_Object = MibScalar
qtechClusterTimerHello = _QtechClusterTimerHello_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 8),
    _QtechClusterTimerHello_Type()
)
qtechClusterTimerHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterTimerHello.setStatus("current")


class _QtechClusterTimerHold_Type(Integer32):
    """Custom type qtechClusterTimerHold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_QtechClusterTimerHold_Type.__name__ = "Integer32"
_QtechClusterTimerHold_Object = MibScalar
qtechClusterTimerHold = _QtechClusterTimerHold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 9),
    _QtechClusterTimerHold_Type()
)
qtechClusterTimerHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterTimerHold.setStatus("current")
_QtechClusterTftpServer_Type = IpAddress
_QtechClusterTftpServer_Object = MibScalar
qtechClusterTftpServer = _QtechClusterTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 10),
    _QtechClusterTftpServer_Type()
)
qtechClusterTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterTftpServer.setStatus("current")


class _QtechClusterNumberOfMembers_Type(Integer32):
    """Custom type qtechClusterNumberOfMembers based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_QtechClusterNumberOfMembers_Type.__name__ = "Integer32"
_QtechClusterNumberOfMembers_Object = MibScalar
qtechClusterNumberOfMembers = _QtechClusterNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 11),
    _QtechClusterNumberOfMembers_Type()
)
qtechClusterNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterNumberOfMembers.setStatus("current")


class _QtechClusterMaxNumberOfMembers_Type(Integer32):
    """Custom type qtechClusterMaxNumberOfMembers based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_QtechClusterMaxNumberOfMembers_Type.__name__ = "Integer32"
_QtechClusterMaxNumberOfMembers_Object = MibScalar
qtechClusterMaxNumberOfMembers = _QtechClusterMaxNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 12),
    _QtechClusterMaxNumberOfMembers_Type()
)
qtechClusterMaxNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMaxNumberOfMembers.setStatus("current")


class _QtechClusterDevMaxCapicity_Type(Unsigned32):
    """Custom type qtechClusterDevMaxCapicity based on Unsigned32"""
    defaultValue = 0


_QtechClusterDevMaxCapicity_Type.__name__ = "Unsigned32"
_QtechClusterDevMaxCapicity_Object = MibScalar
qtechClusterDevMaxCapicity = _QtechClusterDevMaxCapicity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 13),
    _QtechClusterDevMaxCapicity_Type()
)
qtechClusterDevMaxCapicity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterDevMaxCapicity.setStatus("current")


class _QtechClusterAutoAdd_Type(Integer32):
    """Custom type qtechClusterAutoAdd based on Integer32"""
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


_QtechClusterAutoAdd_Type.__name__ = "Integer32"
_QtechClusterAutoAdd_Object = MibScalar
qtechClusterAutoAdd = _QtechClusterAutoAdd_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 14),
    _QtechClusterAutoAdd_Type()
)
qtechClusterAutoAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterAutoAdd.setStatus("current")


class _QtechClusterExplore_Type(EnabledStatus):
    """Custom type qtechClusterExplore based on EnabledStatus"""
    defaultValue = 2


_QtechClusterExplore_Type.__name__ = "EnabledStatus"
_QtechClusterExplore_Object = MibScalar
qtechClusterExplore = _QtechClusterExplore_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 15),
    _QtechClusterExplore_Type()
)
qtechClusterExplore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterExplore.setStatus("current")
_QtechClusterSpecifyAdmin_ObjectIdentity = ObjectIdentity
qtechClusterSpecifyAdmin = _QtechClusterSpecifyAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 16)
)
_QtechClusterSpecifyAdminAddress_Type = MacAddress
_QtechClusterSpecifyAdminAddress_Object = MibScalar
qtechClusterSpecifyAdminAddress = _QtechClusterSpecifyAdminAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 16, 1),
    _QtechClusterSpecifyAdminAddress_Type()
)
qtechClusterSpecifyAdminAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterSpecifyAdminAddress.setStatus("current")


class _QtechClusterSpecifyAdminName_Type(DisplayString):
    """Custom type qtechClusterSpecifyAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QtechClusterSpecifyAdminName_Type.__name__ = "DisplayString"
_QtechClusterSpecifyAdminName_Object = MibScalar
qtechClusterSpecifyAdminName = _QtechClusterSpecifyAdminName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 16, 2),
    _QtechClusterSpecifyAdminName_Type()
)
qtechClusterSpecifyAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterSpecifyAdminName.setStatus("current")
_QtechClusterDeviceInfo_ObjectIdentity = ObjectIdentity
qtechClusterDeviceInfo = _QtechClusterDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 17)
)


class _QtechClusterDeviceEnable_Type(EnabledStatus):
    """Custom type qtechClusterDeviceEnable based on EnabledStatus"""
    defaultValue = 1


_QtechClusterDeviceEnable_Type.__name__ = "EnabledStatus"
_QtechClusterDeviceEnable_Object = MibScalar
qtechClusterDeviceEnable = _QtechClusterDeviceEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 17, 1),
    _QtechClusterDeviceEnable_Type()
)
qtechClusterDeviceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterDeviceEnable.setStatus("current")


class _QtechClusterDeviceRole_Type(Integer32):
    """Custom type qtechClusterDeviceRole based on Integer32"""
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


_QtechClusterDeviceRole_Type.__name__ = "Integer32"
_QtechClusterDeviceRole_Object = MibScalar
qtechClusterDeviceRole = _QtechClusterDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 17, 2),
    _QtechClusterDeviceRole_Type()
)
qtechClusterDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterDeviceRole.setStatus("current")
_QtechClusterDeviceIP_Type = IpAddress
_QtechClusterDeviceIP_Object = MibScalar
qtechClusterDeviceIP = _QtechClusterDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 17, 3),
    _QtechClusterDeviceIP_Type()
)
qtechClusterDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterDeviceIP.setStatus("current")


class _QtechClusterDeviceSn_Type(Integer32):
    """Custom type qtechClusterDeviceSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_QtechClusterDeviceSn_Type.__name__ = "Integer32"
_QtechClusterDeviceSn_Object = MibScalar
qtechClusterDeviceSn = _QtechClusterDeviceSn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 17, 4),
    _QtechClusterDeviceSn_Type()
)
qtechClusterDeviceSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterDeviceSn.setStatus("current")
_QtechClusterIpPoolTable_Object = MibTable
qtechClusterIpPoolTable = _QtechClusterIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 18)
)
if mibBuilder.loadTexts:
    qtechClusterIpPoolTable.setStatus("current")
_QtechClusterIpPoolEntry_Object = MibTableRow
qtechClusterIpPoolEntry = _QtechClusterIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 18, 1)
)
qtechClusterIpPoolEntry.setIndexNames(
    (0, "QTECH-CLUSTER-MIB", "qtechClusterIpPool"),
    (0, "QTECH-CLUSTER-MIB", "qtechClusterIpMask"),
)
if mibBuilder.loadTexts:
    qtechClusterIpPoolEntry.setStatus("current")
_QtechClusterIpPool_Type = IpAddress
_QtechClusterIpPool_Object = MibTableColumn
qtechClusterIpPool = _QtechClusterIpPool_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 18, 1, 1),
    _QtechClusterIpPool_Type()
)
qtechClusterIpPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterIpPool.setStatus("current")
_QtechClusterIpMask_Type = IpAddress
_QtechClusterIpMask_Object = MibTableColumn
qtechClusterIpMask = _QtechClusterIpMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 18, 1, 2),
    _QtechClusterIpMask_Type()
)
qtechClusterIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterIpMask.setStatus("current")
_QtechClusterIpPoolRowStatus_Type = RowStatus
_QtechClusterIpPoolRowStatus_Object = MibTableColumn
qtechClusterIpPoolRowStatus = _QtechClusterIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 18, 1, 3),
    _QtechClusterIpPoolRowStatus_Type()
)
qtechClusterIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechClusterIpPoolRowStatus.setStatus("current")
_QtechClusterMemberAddTable_Object = MibTable
qtechClusterMemberAddTable = _QtechClusterMemberAddTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 19)
)
if mibBuilder.loadTexts:
    qtechClusterMemberAddTable.setStatus("current")
_QtechClusterMemberAddEntry_Object = MibTableRow
qtechClusterMemberAddEntry = _QtechClusterMemberAddEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 19, 1)
)
qtechClusterMemberAddEntry.setIndexNames(
    (0, "QTECH-CLUSTER-MIB", "qtechClusterMemberAddSn"),
)
if mibBuilder.loadTexts:
    qtechClusterMemberAddEntry.setStatus("current")


class _QtechClusterMemberAddSn_Type(Integer32):
    """Custom type qtechClusterMemberAddSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_QtechClusterMemberAddSn_Type.__name__ = "Integer32"
_QtechClusterMemberAddSn_Object = MibTableColumn
qtechClusterMemberAddSn = _QtechClusterMemberAddSn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 19, 1, 1),
    _QtechClusterMemberAddSn_Type()
)
qtechClusterMemberAddSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberAddSn.setStatus("current")
_QtechClusterMemberAddMacAddress_Type = MacAddress
_QtechClusterMemberAddMacAddress_Object = MibTableColumn
qtechClusterMemberAddMacAddress = _QtechClusterMemberAddMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 19, 1, 2),
    _QtechClusterMemberAddMacAddress_Type()
)
qtechClusterMemberAddMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechClusterMemberAddMacAddress.setStatus("current")
_QtechClusterMemberAddRowStatus_Type = RowStatus
_QtechClusterMemberAddRowStatus_Object = MibTableColumn
qtechClusterMemberAddRowStatus = _QtechClusterMemberAddRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 19, 1, 3),
    _QtechClusterMemberAddRowStatus_Type()
)
qtechClusterMemberAddRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechClusterMemberAddRowStatus.setStatus("current")
_QtechClusterMemberTable_Object = MibTable
qtechClusterMemberTable = _QtechClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20)
)
if mibBuilder.loadTexts:
    qtechClusterMemberTable.setStatus("current")
_QtechClusterMemberEntry_Object = MibTableRow
qtechClusterMemberEntry = _QtechClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1)
)
qtechClusterMemberEntry.setIndexNames(
    (0, "QTECH-CLUSTER-MIB", "qtechClusterMemberSn"),
    (0, "QTECH-CLUSTER-MIB", "qtechClusterMemberUpMAC"),
    (0, "QTECH-CLUSTER-MIB", "qtechClusterMemberLcIfx"),
    (0, "QTECH-CLUSTER-MIB", "qtechClusterMemberUpIfx"),
)
if mibBuilder.loadTexts:
    qtechClusterMemberEntry.setStatus("current")
_QtechClusterMemberSn_Type = Unsigned32
_QtechClusterMemberSn_Object = MibTableColumn
qtechClusterMemberSn = _QtechClusterMemberSn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 1),
    _QtechClusterMemberSn_Type()
)
qtechClusterMemberSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberSn.setStatus("current")
_QtechClusterMemberUpMAC_Type = MacAddress
_QtechClusterMemberUpMAC_Object = MibTableColumn
qtechClusterMemberUpMAC = _QtechClusterMemberUpMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 2),
    _QtechClusterMemberUpMAC_Type()
)
qtechClusterMemberUpMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberUpMAC.setStatus("current")
_QtechClusterMemberLcIfx_Type = Unsigned32
_QtechClusterMemberLcIfx_Object = MibTableColumn
qtechClusterMemberLcIfx = _QtechClusterMemberLcIfx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 3),
    _QtechClusterMemberLcIfx_Type()
)
qtechClusterMemberLcIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberLcIfx.setStatus("current")
_QtechClusterMemberUpIfx_Type = Unsigned32
_QtechClusterMemberUpIfx_Object = MibTableColumn
qtechClusterMemberUpIfx = _QtechClusterMemberUpIfx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 4),
    _QtechClusterMemberUpIfx_Type()
)
qtechClusterMemberUpIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberUpIfx.setStatus("current")
_QtechClusterMemberLcPort_Type = DisplayString
_QtechClusterMemberLcPort_Object = MibTableColumn
qtechClusterMemberLcPort = _QtechClusterMemberLcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 5),
    _QtechClusterMemberLcPort_Type()
)
qtechClusterMemberLcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberLcPort.setStatus("current")
_QtechClusterMemberUpPort_Type = DisplayString
_QtechClusterMemberUpPort_Object = MibTableColumn
qtechClusterMemberUpPort = _QtechClusterMemberUpPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 6),
    _QtechClusterMemberUpPort_Type()
)
qtechClusterMemberUpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberUpPort.setStatus("current")
_QtechClusterMemberMacAddress_Type = MacAddress
_QtechClusterMemberMacAddress_Object = MibTableColumn
qtechClusterMemberMacAddress = _QtechClusterMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 7),
    _QtechClusterMemberMacAddress_Type()
)
qtechClusterMemberMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberMacAddress.setStatus("current")
_QtechClusterMemberName_Type = DisplayString
_QtechClusterMemberName_Object = MibTableColumn
qtechClusterMemberName = _QtechClusterMemberName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 8),
    _QtechClusterMemberName_Type()
)
qtechClusterMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberName.setStatus("current")
_QtechClusterMemberIp_Type = IpAddress
_QtechClusterMemberIp_Object = MibTableColumn
qtechClusterMemberIp = _QtechClusterMemberIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 9),
    _QtechClusterMemberIp_Type()
)
qtechClusterMemberIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberIp.setStatus("current")
_QtechClusterMemberHops_Type = Unsigned32
_QtechClusterMemberHops_Object = MibTableColumn
qtechClusterMemberHops = _QtechClusterMemberHops_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 10),
    _QtechClusterMemberHops_Type()
)
qtechClusterMemberHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberHops.setStatus("current")
_QtechClusterMemberState_Type = DisplayString
_QtechClusterMemberState_Object = MibTableColumn
qtechClusterMemberState = _QtechClusterMemberState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 11),
    _QtechClusterMemberState_Type()
)
qtechClusterMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberState.setStatus("current")
_QtechClusterMemberUpSn_Type = Unsigned32
_QtechClusterMemberUpSn_Object = MibTableColumn
qtechClusterMemberUpSn = _QtechClusterMemberUpSn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 12),
    _QtechClusterMemberUpSn_Type()
)
qtechClusterMemberUpSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberUpSn.setStatus("current")
_QtechClusterMemberLastTopoUpdateTime_Type = Unsigned32
_QtechClusterMemberLastTopoUpdateTime_Object = MibTableColumn
qtechClusterMemberLastTopoUpdateTime = _QtechClusterMemberLastTopoUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 13),
    _QtechClusterMemberLastTopoUpdateTime_Type()
)
qtechClusterMemberLastTopoUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberLastTopoUpdateTime.setStatus("current")
_QtechClusterMemberLastUdpUpdateTime_Type = Unsigned32
_QtechClusterMemberLastUdpUpdateTime_Object = MibTableColumn
qtechClusterMemberLastUdpUpdateTime = _QtechClusterMemberLastUdpUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 14),
    _QtechClusterMemberLastUdpUpdateTime_Type()
)
qtechClusterMemberLastUdpUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberLastUdpUpdateTime.setStatus("current")
_QtechClusterMemberNoRecvTopoRspCount_Type = Unsigned32
_QtechClusterMemberNoRecvTopoRspCount_Object = MibTableColumn
qtechClusterMemberNoRecvTopoRspCount = _QtechClusterMemberNoRecvTopoRspCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 15),
    _QtechClusterMemberNoRecvTopoRspCount_Type()
)
qtechClusterMemberNoRecvTopoRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberNoRecvTopoRspCount.setStatus("current")
_QtechClusterMemberNoRecvUdpRspCount_Type = Unsigned32
_QtechClusterMemberNoRecvUdpRspCount_Object = MibTableColumn
qtechClusterMemberNoRecvUdpRspCount = _QtechClusterMemberNoRecvUdpRspCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 16),
    _QtechClusterMemberNoRecvUdpRspCount_Type()
)
qtechClusterMemberNoRecvUdpRspCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterMemberNoRecvUdpRspCount.setStatus("current")
_QtechClusterMemberReload_Type = EnabledStatus
_QtechClusterMemberReload_Object = MibTableColumn
qtechClusterMemberReload = _QtechClusterMemberReload_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 20, 1, 17),
    _QtechClusterMemberReload_Type()
)
qtechClusterMemberReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClusterMemberReload.setStatus("current")
_QtechClusterCandidateTable_Object = MibTable
qtechClusterCandidateTable = _QtechClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21)
)
if mibBuilder.loadTexts:
    qtechClusterCandidateTable.setStatus("current")
_QtechClusterCandidateEntry_Object = MibTableRow
qtechClusterCandidateEntry = _QtechClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1)
)
qtechClusterCandidateEntry.setIndexNames(
    (0, "QTECH-CLUSTER-MIB", "qtechClusterCandidateMacAddress"),
    (0, "QTECH-CLUSTER-MIB", "qtechClusterCandidateUpMAC"),
    (0, "QTECH-CLUSTER-MIB", "qtechClusterCandidateLcIfx"),
    (0, "QTECH-CLUSTER-MIB", "qtechClusterCandidateUpIfx"),
)
if mibBuilder.loadTexts:
    qtechClusterCandidateEntry.setStatus("current")
_QtechClusterCandidateMacAddress_Type = MacAddress
_QtechClusterCandidateMacAddress_Object = MibTableColumn
qtechClusterCandidateMacAddress = _QtechClusterCandidateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1, 1),
    _QtechClusterCandidateMacAddress_Type()
)
qtechClusterCandidateMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCandidateMacAddress.setStatus("current")
_QtechClusterCandidateUpMAC_Type = MacAddress
_QtechClusterCandidateUpMAC_Object = MibTableColumn
qtechClusterCandidateUpMAC = _QtechClusterCandidateUpMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1, 2),
    _QtechClusterCandidateUpMAC_Type()
)
qtechClusterCandidateUpMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCandidateUpMAC.setStatus("current")
_QtechClusterCandidateLcIfx_Type = Unsigned32
_QtechClusterCandidateLcIfx_Object = MibTableColumn
qtechClusterCandidateLcIfx = _QtechClusterCandidateLcIfx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1, 3),
    _QtechClusterCandidateLcIfx_Type()
)
qtechClusterCandidateLcIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCandidateLcIfx.setStatus("current")
_QtechClusterCandidateUpIfx_Type = Unsigned32
_QtechClusterCandidateUpIfx_Object = MibTableColumn
qtechClusterCandidateUpIfx = _QtechClusterCandidateUpIfx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1, 4),
    _QtechClusterCandidateUpIfx_Type()
)
qtechClusterCandidateUpIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCandidateUpIfx.setStatus("current")
_QtechClusterCandidateLcPort_Type = DisplayString
_QtechClusterCandidateLcPort_Object = MibTableColumn
qtechClusterCandidateLcPort = _QtechClusterCandidateLcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1, 5),
    _QtechClusterCandidateLcPort_Type()
)
qtechClusterCandidateLcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCandidateLcPort.setStatus("current")
_QtechClusterCandidateUpPort_Type = DisplayString
_QtechClusterCandidateUpPort_Object = MibTableColumn
qtechClusterCandidateUpPort = _QtechClusterCandidateUpPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1, 6),
    _QtechClusterCandidateUpPort_Type()
)
qtechClusterCandidateUpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCandidateUpPort.setStatus("current")
_QtechClusterCandidateUpSn_Type = Unsigned32
_QtechClusterCandidateUpSn_Object = MibTableColumn
qtechClusterCandidateUpSn = _QtechClusterCandidateUpSn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1, 7),
    _QtechClusterCandidateUpSn_Type()
)
qtechClusterCandidateUpSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCandidateUpSn.setStatus("current")
_QtechClusterCandidateHops_Type = Unsigned32
_QtechClusterCandidateHops_Object = MibTableColumn
qtechClusterCandidateHops = _QtechClusterCandidateHops_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1, 8),
    _QtechClusterCandidateHops_Type()
)
qtechClusterCandidateHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCandidateHops.setStatus("current")
_QtechClusterCandidateState_Type = DisplayString
_QtechClusterCandidateState_Object = MibTableColumn
qtechClusterCandidateState = _QtechClusterCandidateState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 21, 1, 9),
    _QtechClusterCandidateState_Type()
)
qtechClusterCandidateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterCandidateState.setStatus("current")
_QtechClusterBlacklistTable_Object = MibTable
qtechClusterBlacklistTable = _QtechClusterBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 22)
)
if mibBuilder.loadTexts:
    qtechClusterBlacklistTable.setStatus("current")
_QtechClusterBlacklistEntry_Object = MibTableRow
qtechClusterBlacklistEntry = _QtechClusterBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 22, 1)
)
qtechClusterBlacklistEntry.setIndexNames(
    (0, "QTECH-CLUSTER-MIB", "qtechClusterBlacklistMacAddress"),
)
if mibBuilder.loadTexts:
    qtechClusterBlacklistEntry.setStatus("current")
_QtechClusterBlacklistMacAddress_Type = MacAddress
_QtechClusterBlacklistMacAddress_Object = MibTableColumn
qtechClusterBlacklistMacAddress = _QtechClusterBlacklistMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 22, 1, 1),
    _QtechClusterBlacklistMacAddress_Type()
)
qtechClusterBlacklistMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterBlacklistMacAddress.setStatus("current")
_QtechClusterBlackListRowStatus_Type = RowStatus
_QtechClusterBlackListRowStatus_Object = MibTableColumn
qtechClusterBlackListRowStatus = _QtechClusterBlackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 22, 1, 2),
    _QtechClusterBlackListRowStatus_Type()
)
qtechClusterBlackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechClusterBlackListRowStatus.setStatus("current")
_QtechClusterPasswordAuth_ObjectIdentity = ObjectIdentity
qtechClusterPasswordAuth = _QtechClusterPasswordAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23)
)
_QtechClusterPasswordAuthPoolTable_Object = MibTable
qtechClusterPasswordAuthPoolTable = _QtechClusterPasswordAuthPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 1)
)
if mibBuilder.loadTexts:
    qtechClusterPasswordAuthPoolTable.setStatus("current")
_QtechClusterPasswordAuthPoolEntry_Object = MibTableRow
qtechClusterPasswordAuthPoolEntry = _QtechClusterPasswordAuthPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 1, 1)
)
qtechClusterPasswordAuthPoolEntry.setIndexNames(
    (0, "QTECH-CLUSTER-MIB", "qtechClusterPasswordSn"),
)
if mibBuilder.loadTexts:
    qtechClusterPasswordAuthPoolEntry.setStatus("current")


class _QtechClusterPasswordSn_Type(Integer32):
    """Custom type qtechClusterPasswordSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QtechClusterPasswordSn_Type.__name__ = "Integer32"
_QtechClusterPasswordSn_Object = MibTableColumn
qtechClusterPasswordSn = _QtechClusterPasswordSn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 1, 1, 1),
    _QtechClusterPasswordSn_Type()
)
qtechClusterPasswordSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterPasswordSn.setStatus("current")


class _QtechClusterPassword_Type(DisplayString):
    """Custom type qtechClusterPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_QtechClusterPassword_Type.__name__ = "DisplayString"
_QtechClusterPassword_Object = MibTableColumn
qtechClusterPassword = _QtechClusterPassword_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 1, 1, 2),
    _QtechClusterPassword_Type()
)
qtechClusterPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechClusterPassword.setStatus("current")
_QtechClusterPasswordAuthRowStatus_Type = RowStatus
_QtechClusterPasswordAuthRowStatus_Object = MibTableColumn
qtechClusterPasswordAuthRowStatus = _QtechClusterPasswordAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 1, 1, 3),
    _QtechClusterPasswordAuthRowStatus_Type()
)
qtechClusterPasswordAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechClusterPasswordAuthRowStatus.setStatus("current")
_QtechClusterDeviceAuthPasswordTable_Object = MibTable
qtechClusterDeviceAuthPasswordTable = _QtechClusterDeviceAuthPasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 2)
)
if mibBuilder.loadTexts:
    qtechClusterDeviceAuthPasswordTable.setStatus("current")
_QtechClusterDeviceAuthPasswordEntry_Object = MibTableRow
qtechClusterDeviceAuthPasswordEntry = _QtechClusterDeviceAuthPasswordEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 2, 1)
)
qtechClusterDeviceAuthPasswordEntry.setIndexNames(
    (0, "QTECH-CLUSTER-MIB", "qtechClusterDeviceMacAddress"),
)
if mibBuilder.loadTexts:
    qtechClusterDeviceAuthPasswordEntry.setStatus("current")
_QtechClusterDeviceMacAddress_Type = MacAddress
_QtechClusterDeviceMacAddress_Object = MibTableColumn
qtechClusterDeviceMacAddress = _QtechClusterDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 2, 1, 1),
    _QtechClusterDeviceMacAddress_Type()
)
qtechClusterDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClusterDeviceMacAddress.setStatus("current")


class _QtechClusterDevicePassword_Type(DisplayString):
    """Custom type qtechClusterDevicePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_QtechClusterDevicePassword_Type.__name__ = "DisplayString"
_QtechClusterDevicePassword_Object = MibTableColumn
qtechClusterDevicePassword = _QtechClusterDevicePassword_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 2, 1, 2),
    _QtechClusterDevicePassword_Type()
)
qtechClusterDevicePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechClusterDevicePassword.setStatus("current")
_QtechClusterDevicePasswordRowStatus_Type = RowStatus
_QtechClusterDevicePasswordRowStatus_Object = MibTableColumn
qtechClusterDevicePasswordRowStatus = _QtechClusterDevicePasswordRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 1, 23, 2, 1, 3),
    _QtechClusterDevicePasswordRowStatus_Type()
)
qtechClusterDevicePasswordRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechClusterDevicePasswordRowStatus.setStatus("current")
_QtechClusterTraps_ObjectIdentity = ObjectIdentity
qtechClusterTraps = _QtechClusterTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 2)
)
_QtechClusterMIBConformance_ObjectIdentity = ObjectIdentity
qtechClusterMIBConformance = _QtechClusterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3)
)
_QtechClusterMIBCompliances_ObjectIdentity = ObjectIdentity
qtechClusterMIBCompliances = _QtechClusterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 1)
)
_QtechClusterMIBGroups_ObjectIdentity = ObjectIdentity
qtechClusterMIBGroups = _QtechClusterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2)
)

# Managed Objects groups

qtechClusterStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2, 1)
)
qtechClusterStatusGroup.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterName"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCmdMacAddress"),
        ("QTECH-CLUSTER-MIB", "qtechClusterIpPool"),
        ("QTECH-CLUSTER-MIB", "qtechClusterIpMask"),
        ("QTECH-CLUSTER-MIB", "qtechClusterVlan"),
        ("QTECH-CLUSTER-MIB", "qtechClusterHopsLimit"),
        ("QTECH-CLUSTER-MIB", "qtechClusterHopsLimit"),
        ("QTECH-CLUSTER-MIB", "qtechClusterTimerTopo"),
        ("QTECH-CLUSTER-MIB", "qtechClusterTimerHello"),
        ("QTECH-CLUSTER-MIB", "qtechClusterTimerHold"),
        ("QTECH-CLUSTER-MIB", "qtechClusterTftpServer"),
        ("QTECH-CLUSTER-MIB", "qtechClusterNumberOfMembers"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMaxNumberOfMembers"),
        ("QTECH-CLUSTER-MIB", "qtechClusterDevMaxCapicity"))
)
if mibBuilder.loadTexts:
    qtechClusterStatusGroup.setStatus("current")

qtechClusterMemberStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2, 2)
)
qtechClusterMemberStatusGroup.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterName"),
        ("QTECH-CLUSTER-MIB", "qtechClusterDeviceEnable"),
        ("QTECH-CLUSTER-MIB", "qtechClusterDeviceRole"),
        ("QTECH-CLUSTER-MIB", "qtechClusterDeviceIP"),
        ("QTECH-CLUSTER-MIB", "qtechClusterDeviceSn"))
)
if mibBuilder.loadTexts:
    qtechClusterMemberStatusGroup.setStatus("current")

qtechClusterCandidateStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2, 3)
)
qtechClusterCandidateStatusGroup.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterName"),
        ("QTECH-CLUSTER-MIB", "qtechClusterDeviceRole"),
        ("QTECH-CLUSTER-MIB", "qtechClusterDeviceEnable"))
)
if mibBuilder.loadTexts:
    qtechClusterCandidateStatusGroup.setStatus("current")

qtechClusterMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2, 4)
)
qtechClusterMemberGroup.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterMemberSn"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberMacAddress"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberLcIfx"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberUpIfx"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberLcPort"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberUpPort"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberName"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberIp"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberHops"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberState"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberUpSn"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberUpMAC"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberLastTopoUpdateTime"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberLastUdpUpdateTime"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberNoRecvTopoRspCount"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberNoRecvUdpRspCount"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberReload"))
)
if mibBuilder.loadTexts:
    qtechClusterMemberGroup.setStatus("current")

qtechClusterCandidateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2, 5)
)
qtechClusterCandidateGroup.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterCandidateMacAddress"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateUpMAC"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateLcIfx"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateUpIfx"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateLcPort"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateUpPort"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateHops"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateUpSn"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateState"))
)
if mibBuilder.loadTexts:
    qtechClusterCandidateGroup.setStatus("current")

qtechClusterMemberAddGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2, 6)
)
qtechClusterMemberAddGroup.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterMemberAddMacAddress"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberAddSn"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberAddRowStatus"))
)
if mibBuilder.loadTexts:
    qtechClusterMemberAddGroup.setStatus("current")

qtechClusterBlackListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2, 7)
)
qtechClusterBlackListGroup.setObjects(
    ("QTECH-CLUSTER-MIB", "qtechClusterBlacklistMacAddress")
)
if mibBuilder.loadTexts:
    qtechClusterBlackListGroup.setStatus("current")

qtechClusterPasswordAuthPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2, 8)
)
qtechClusterPasswordAuthPoolGroup.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterPasswordSn"),
        ("QTECH-CLUSTER-MIB", "qtechClusterPassword"))
)
if mibBuilder.loadTexts:
    qtechClusterPasswordAuthPoolGroup.setStatus("current")

qtechClsuterDeviceAuthPasswordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 2, 9)
)
qtechClsuterDeviceAuthPasswordGroup.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterDeviceMacAddress"),
        ("QTECH-CLUSTER-MIB", "qtechClusterDevicePassword"))
)
if mibBuilder.loadTexts:
    qtechClsuterDeviceAuthPasswordGroup.setStatus("current")


# Notification objects

qtechClusterMemberStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 2, 1)
)
qtechClusterMemberStateChangeTrap.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterMemberSn"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberState"))
)
if mibBuilder.loadTexts:
    qtechClusterMemberStateChangeTrap.setStatus(
        "current"
    )

qtechClusterMemberFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 2, 2)
)
qtechClusterMemberFailureTrap.setObjects(
    ("QTECH-CLUSTER-MIB", "qtechClusterCandidateMacAddress")
)
if mibBuilder.loadTexts:
    qtechClusterMemberFailureTrap.setStatus(
        "current"
    )

qtechClusterDevMaximumAllowedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 2, 3)
)
if mibBuilder.loadTexts:
    qtechClusterDevMaximumAllowedTrap.setStatus(
        "current"
    )

qtechClusterMemberMaximumAllowedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 2, 4)
)
if mibBuilder.loadTexts:
    qtechClusterMemberMaximumAllowedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechClusterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 31, 3, 1, 1)
)
qtechClusterCompliance.setObjects(
      *(("QTECH-CLUSTER-MIB", "qtechClusterStatusGroup"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberStatusGroup"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberGroup"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateGroup"),
        ("QTECH-CLUSTER-MIB", "qtechClusterMemberAddGroup"),
        ("QTECH-CLUSTER-MIB", "qtechClusterBlackListGroup"),
        ("QTECH-CLUSTER-MIB", "uijieClusterPasswordAuthPoolGroup"),
        ("QTECH-CLUSTER-MIB", "qtechDeviceAuthPasswordGroup"),
        ("QTECH-CLUSTER-MIB", "qtechClusterCandidateStatusGroup"))
)
if mibBuilder.loadTexts:
    qtechClusterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CLUSTER-MIB",
    **{"qtechClusterMIB": qtechClusterMIB,
       "qtechClusterMIBObjects": qtechClusterMIBObjects,
       "qtechClusterName": qtechClusterName,
       "qtechClusterStatus": qtechClusterStatus,
       "qtechClusterCmdMacAddress": qtechClusterCmdMacAddress,
       "qtechClusterCmdName": qtechClusterCmdName,
       "qtechClusterVlan": qtechClusterVlan,
       "qtechClusterHopsLimit": qtechClusterHopsLimit,
       "qtechClusterTimerTopo": qtechClusterTimerTopo,
       "qtechClusterTimerHello": qtechClusterTimerHello,
       "qtechClusterTimerHold": qtechClusterTimerHold,
       "qtechClusterTftpServer": qtechClusterTftpServer,
       "qtechClusterNumberOfMembers": qtechClusterNumberOfMembers,
       "qtechClusterMaxNumberOfMembers": qtechClusterMaxNumberOfMembers,
       "qtechClusterDevMaxCapicity": qtechClusterDevMaxCapicity,
       "qtechClusterAutoAdd": qtechClusterAutoAdd,
       "qtechClusterExplore": qtechClusterExplore,
       "qtechClusterSpecifyAdmin": qtechClusterSpecifyAdmin,
       "qtechClusterSpecifyAdminAddress": qtechClusterSpecifyAdminAddress,
       "qtechClusterSpecifyAdminName": qtechClusterSpecifyAdminName,
       "qtechClusterDeviceInfo": qtechClusterDeviceInfo,
       "qtechClusterDeviceEnable": qtechClusterDeviceEnable,
       "qtechClusterDeviceRole": qtechClusterDeviceRole,
       "qtechClusterDeviceIP": qtechClusterDeviceIP,
       "qtechClusterDeviceSn": qtechClusterDeviceSn,
       "qtechClusterIpPoolTable": qtechClusterIpPoolTable,
       "qtechClusterIpPoolEntry": qtechClusterIpPoolEntry,
       "qtechClusterIpPool": qtechClusterIpPool,
       "qtechClusterIpMask": qtechClusterIpMask,
       "qtechClusterIpPoolRowStatus": qtechClusterIpPoolRowStatus,
       "qtechClusterMemberAddTable": qtechClusterMemberAddTable,
       "qtechClusterMemberAddEntry": qtechClusterMemberAddEntry,
       "qtechClusterMemberAddSn": qtechClusterMemberAddSn,
       "qtechClusterMemberAddMacAddress": qtechClusterMemberAddMacAddress,
       "qtechClusterMemberAddRowStatus": qtechClusterMemberAddRowStatus,
       "qtechClusterMemberTable": qtechClusterMemberTable,
       "qtechClusterMemberEntry": qtechClusterMemberEntry,
       "qtechClusterMemberSn": qtechClusterMemberSn,
       "qtechClusterMemberUpMAC": qtechClusterMemberUpMAC,
       "qtechClusterMemberLcIfx": qtechClusterMemberLcIfx,
       "qtechClusterMemberUpIfx": qtechClusterMemberUpIfx,
       "qtechClusterMemberLcPort": qtechClusterMemberLcPort,
       "qtechClusterMemberUpPort": qtechClusterMemberUpPort,
       "qtechClusterMemberMacAddress": qtechClusterMemberMacAddress,
       "qtechClusterMemberName": qtechClusterMemberName,
       "qtechClusterMemberIp": qtechClusterMemberIp,
       "qtechClusterMemberHops": qtechClusterMemberHops,
       "qtechClusterMemberState": qtechClusterMemberState,
       "qtechClusterMemberUpSn": qtechClusterMemberUpSn,
       "qtechClusterMemberLastTopoUpdateTime": qtechClusterMemberLastTopoUpdateTime,
       "qtechClusterMemberLastUdpUpdateTime": qtechClusterMemberLastUdpUpdateTime,
       "qtechClusterMemberNoRecvTopoRspCount": qtechClusterMemberNoRecvTopoRspCount,
       "qtechClusterMemberNoRecvUdpRspCount": qtechClusterMemberNoRecvUdpRspCount,
       "qtechClusterMemberReload": qtechClusterMemberReload,
       "qtechClusterCandidateTable": qtechClusterCandidateTable,
       "qtechClusterCandidateEntry": qtechClusterCandidateEntry,
       "qtechClusterCandidateMacAddress": qtechClusterCandidateMacAddress,
       "qtechClusterCandidateUpMAC": qtechClusterCandidateUpMAC,
       "qtechClusterCandidateLcIfx": qtechClusterCandidateLcIfx,
       "qtechClusterCandidateUpIfx": qtechClusterCandidateUpIfx,
       "qtechClusterCandidateLcPort": qtechClusterCandidateLcPort,
       "qtechClusterCandidateUpPort": qtechClusterCandidateUpPort,
       "qtechClusterCandidateUpSn": qtechClusterCandidateUpSn,
       "qtechClusterCandidateHops": qtechClusterCandidateHops,
       "qtechClusterCandidateState": qtechClusterCandidateState,
       "qtechClusterBlacklistTable": qtechClusterBlacklistTable,
       "qtechClusterBlacklistEntry": qtechClusterBlacklistEntry,
       "qtechClusterBlacklistMacAddress": qtechClusterBlacklistMacAddress,
       "qtechClusterBlackListRowStatus": qtechClusterBlackListRowStatus,
       "qtechClusterPasswordAuth": qtechClusterPasswordAuth,
       "qtechClusterPasswordAuthPoolTable": qtechClusterPasswordAuthPoolTable,
       "qtechClusterPasswordAuthPoolEntry": qtechClusterPasswordAuthPoolEntry,
       "qtechClusterPasswordSn": qtechClusterPasswordSn,
       "qtechClusterPassword": qtechClusterPassword,
       "qtechClusterPasswordAuthRowStatus": qtechClusterPasswordAuthRowStatus,
       "qtechClusterDeviceAuthPasswordTable": qtechClusterDeviceAuthPasswordTable,
       "qtechClusterDeviceAuthPasswordEntry": qtechClusterDeviceAuthPasswordEntry,
       "qtechClusterDeviceMacAddress": qtechClusterDeviceMacAddress,
       "qtechClusterDevicePassword": qtechClusterDevicePassword,
       "qtechClusterDevicePasswordRowStatus": qtechClusterDevicePasswordRowStatus,
       "qtechClusterTraps": qtechClusterTraps,
       "qtechClusterMemberStateChangeTrap": qtechClusterMemberStateChangeTrap,
       "qtechClusterMemberFailureTrap": qtechClusterMemberFailureTrap,
       "qtechClusterDevMaximumAllowedTrap": qtechClusterDevMaximumAllowedTrap,
       "qtechClusterMemberMaximumAllowedTrap": qtechClusterMemberMaximumAllowedTrap,
       "qtechClusterMIBConformance": qtechClusterMIBConformance,
       "qtechClusterMIBCompliances": qtechClusterMIBCompliances,
       "qtechClusterCompliance": qtechClusterCompliance,
       "qtechClusterMIBGroups": qtechClusterMIBGroups,
       "qtechClusterStatusGroup": qtechClusterStatusGroup,
       "qtechClusterMemberStatusGroup": qtechClusterMemberStatusGroup,
       "qtechClusterCandidateStatusGroup": qtechClusterCandidateStatusGroup,
       "qtechClusterMemberGroup": qtechClusterMemberGroup,
       "qtechClusterCandidateGroup": qtechClusterCandidateGroup,
       "qtechClusterMemberAddGroup": qtechClusterMemberAddGroup,
       "qtechClusterBlackListGroup": qtechClusterBlackListGroup,
       "qtechClusterPasswordAuthPoolGroup": qtechClusterPasswordAuthPoolGroup,
       "qtechClsuterDeviceAuthPasswordGroup": qtechClsuterDeviceAuthPasswordGroup}
)
