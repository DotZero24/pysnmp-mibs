# SNMP MIB module (LUM-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:33 2025
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

(lumModules,
 lumMulticastMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumMulticastMIB")

(CommandString,
 EnableDisable,
 MgmtNameString,
 PmReset) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "EnableDisable",
    "MgmtNameString",
    "PmReset")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lumMulticastMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 38)
)
if mibBuilder.loadTexts:
    lumMulticastMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2011-05-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumMulticastConfs_ObjectIdentity = ObjectIdentity
lumMulticastConfs = _LumMulticastConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1)
)
_LumMulticastGroups_ObjectIdentity = ObjectIdentity
lumMulticastGroups = _LumMulticastGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1, 1)
)
_LumMulticastCompl_ObjectIdentity = ObjectIdentity
lumMulticastCompl = _LumMulticastCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1, 2)
)
_LumMulticastMIBObjects_ObjectIdentity = ObjectIdentity
lumMulticastMIBObjects = _LumMulticastMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2)
)
_MulticastGeneral_ObjectIdentity = ObjectIdentity
multicastGeneral = _MulticastGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 1)
)
_MulticastGeneralLastChangeTime_Type = DateAndTime
_MulticastGeneralLastChangeTime_Object = MibScalar
multicastGeneralLastChangeTime = _MulticastGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 1, 1),
    _MulticastGeneralLastChangeTime_Type()
)
multicastGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastGeneralLastChangeTime.setStatus("current")
_MulticastGeneralStateLastChangeTime_Type = DateAndTime
_MulticastGeneralStateLastChangeTime_Object = MibScalar
multicastGeneralStateLastChangeTime = _MulticastGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 1, 2),
    _MulticastGeneralStateLastChangeTime_Type()
)
multicastGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastGeneralStateLastChangeTime.setStatus("current")
_MulticastGeneralMulticastIfTableSize_Type = Unsigned32
_MulticastGeneralMulticastIfTableSize_Object = MibScalar
multicastGeneralMulticastIfTableSize = _MulticastGeneralMulticastIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 1, 3),
    _MulticastGeneralMulticastIfTableSize_Type()
)
multicastGeneralMulticastIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastGeneralMulticastIfTableSize.setStatus("current")
_MulticastGeneralMulticastMembershipTableSize_Type = Unsigned32
_MulticastGeneralMulticastMembershipTableSize_Object = MibScalar
multicastGeneralMulticastMembershipTableSize = _MulticastGeneralMulticastMembershipTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 1, 4),
    _MulticastGeneralMulticastMembershipTableSize_Type()
)
multicastGeneralMulticastMembershipTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastGeneralMulticastMembershipTableSize.setStatus("current")
_MulticastGeneralMulticastForwardingTableSize_Type = Unsigned32
_MulticastGeneralMulticastForwardingTableSize_Object = MibScalar
multicastGeneralMulticastForwardingTableSize = _MulticastGeneralMulticastForwardingTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 1, 5),
    _MulticastGeneralMulticastForwardingTableSize_Type()
)
multicastGeneralMulticastForwardingTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastGeneralMulticastForwardingTableSize.setStatus("current")
_MulticastGeneralPmIgmpPortTableSize_Type = Unsigned32
_MulticastGeneralPmIgmpPortTableSize_Object = MibScalar
multicastGeneralPmIgmpPortTableSize = _MulticastGeneralPmIgmpPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 1, 6),
    _MulticastGeneralPmIgmpPortTableSize_Type()
)
multicastGeneralPmIgmpPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastGeneralPmIgmpPortTableSize.setStatus("current")
_MulticastIfList_ObjectIdentity = ObjectIdentity
multicastIfList = _MulticastIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2)
)
_MulticastIfTable_Object = MibTable
multicastIfTable = _MulticastIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1)
)
if mibBuilder.loadTexts:
    multicastIfTable.setStatus("current")
_MulticastIfEntry_Object = MibTableRow
multicastIfEntry = _MulticastIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1)
)
multicastIfEntry.setIndexNames(
    (0, "LUM-MULTICAST-MIB", "multicastIfIndex"),
)
if mibBuilder.loadTexts:
    multicastIfEntry.setStatus("current")


class _MulticastIfIndex_Type(Unsigned32):
    """Custom type multicastIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MulticastIfIndex_Type.__name__ = "Unsigned32"
_MulticastIfIndex_Object = MibTableColumn
multicastIfIndex = _MulticastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 1),
    _MulticastIfIndex_Type()
)
multicastIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIfIndex.setStatus("current")
_MulticastIfName_Type = MgmtNameString
_MulticastIfName_Object = MibTableColumn
multicastIfName = _MulticastIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 2),
    _MulticastIfName_Type()
)
multicastIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIfName.setStatus("current")


class _MulticastIfDescr_Type(DisplayString):
    """Custom type multicastIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_MulticastIfDescr_Type.__name__ = "DisplayString"
_MulticastIfDescr_Object = MibTableColumn
multicastIfDescr = _MulticastIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 3),
    _MulticastIfDescr_Type()
)
multicastIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastIfDescr.setStatus("current")


class _MulticastIfProtocol_Type(Integer32):
    """Custom type multicastIfProtocol based on Integer32"""
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
          ("igmp", 2))
    )


_MulticastIfProtocol_Type.__name__ = "Integer32"
_MulticastIfProtocol_Object = MibTableColumn
multicastIfProtocol = _MulticastIfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 4),
    _MulticastIfProtocol_Type()
)
multicastIfProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastIfProtocol.setStatus("current")


class _MulticastIfRouterEnable_Type(EnableDisable):
    """Custom type multicastIfRouterEnable based on EnableDisable"""
    defaultValue = 1


_MulticastIfRouterEnable_Type.__name__ = "EnableDisable"
_MulticastIfRouterEnable_Object = MibTableColumn
multicastIfRouterEnable = _MulticastIfRouterEnable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 5),
    _MulticastIfRouterEnable_Type()
)
multicastIfRouterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastIfRouterEnable.setStatus("current")


class _MulticastIfFastLeave_Type(EnableDisable):
    """Custom type multicastIfFastLeave based on EnableDisable"""
    defaultValue = 2


_MulticastIfFastLeave_Type.__name__ = "EnableDisable"
_MulticastIfFastLeave_Object = MibTableColumn
multicastIfFastLeave = _MulticastIfFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 6),
    _MulticastIfFastLeave_Type()
)
multicastIfFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastIfFastLeave.setStatus("current")


class _MulticastIfRobustness_Type(Unsigned32):
    """Custom type multicastIfRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MulticastIfRobustness_Type.__name__ = "Unsigned32"
_MulticastIfRobustness_Object = MibTableColumn
multicastIfRobustness = _MulticastIfRobustness_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 7),
    _MulticastIfRobustness_Type()
)
multicastIfRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastIfRobustness.setStatus("current")


class _MulticastIfReservedFlooding_Type(EnableDisable):
    """Custom type multicastIfReservedFlooding based on EnableDisable"""
    defaultValue = 2


_MulticastIfReservedFlooding_Type.__name__ = "EnableDisable"
_MulticastIfReservedFlooding_Object = MibTableColumn
multicastIfReservedFlooding = _MulticastIfReservedFlooding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 8),
    _MulticastIfReservedFlooding_Type()
)
multicastIfReservedFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastIfReservedFlooding.setStatus("current")
_MulticastIfAssociateStaticMember_Type = CommandString
_MulticastIfAssociateStaticMember_Object = MibTableColumn
multicastIfAssociateStaticMember = _MulticastIfAssociateStaticMember_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 9),
    _MulticastIfAssociateStaticMember_Type()
)
multicastIfAssociateStaticMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIfAssociateStaticMember.setStatus("current")


class _MulticastIfMembersMax_Type(Unsigned32):
    """Custom type multicastIfMembersMax based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MulticastIfMembersMax_Type.__name__ = "Unsigned32"
_MulticastIfMembersMax_Object = MibTableColumn
multicastIfMembersMax = _MulticastIfMembersMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 10),
    _MulticastIfMembersMax_Type()
)
multicastIfMembersMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastIfMembersMax.setStatus("current")


class _MulticastIfNoOfStaticMembers_Type(Unsigned32):
    """Custom type multicastIfNoOfStaticMembers based on Unsigned32"""
    defaultValue = 0


_MulticastIfNoOfStaticMembers_Type.__name__ = "Unsigned32"
_MulticastIfNoOfStaticMembers_Object = MibTableColumn
multicastIfNoOfStaticMembers = _MulticastIfNoOfStaticMembers_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 11),
    _MulticastIfNoOfStaticMembers_Type()
)
multicastIfNoOfStaticMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIfNoOfStaticMembers.setStatus("current")
_MulticastIfMembershipFiltering_Type = CommandString
_MulticastIfMembershipFiltering_Object = MibTableColumn
multicastIfMembershipFiltering = _MulticastIfMembershipFiltering_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 12),
    _MulticastIfMembershipFiltering_Type()
)
multicastIfMembershipFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIfMembershipFiltering.setStatus("current")
_MulticastIfForwardingFiltering_Type = CommandString
_MulticastIfForwardingFiltering_Object = MibTableColumn
multicastIfForwardingFiltering = _MulticastIfForwardingFiltering_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 13),
    _MulticastIfForwardingFiltering_Type()
)
multicastIfForwardingFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIfForwardingFiltering.setStatus("current")
_MulticastIfDeleteMembers_Type = CommandString
_MulticastIfDeleteMembers_Object = MibTableColumn
multicastIfDeleteMembers = _MulticastIfDeleteMembers_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 2, 1, 1, 15),
    _MulticastIfDeleteMembers_Type()
)
multicastIfDeleteMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIfDeleteMembers.setStatus("current")
_MulticastMembershipList_ObjectIdentity = ObjectIdentity
multicastMembershipList = _MulticastMembershipList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3)
)
_MulticastMembershipTable_Object = MibTable
multicastMembershipTable = _MulticastMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1)
)
if mibBuilder.loadTexts:
    multicastMembershipTable.setStatus("current")
_MulticastMembershipEntry_Object = MibTableRow
multicastMembershipEntry = _MulticastMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1)
)
multicastMembershipEntry.setIndexNames(
    (0, "LUM-MULTICAST-MIB", "multicastMembershipIndex"),
)
if mibBuilder.loadTexts:
    multicastMembershipEntry.setStatus("current")


class _MulticastMembershipIndex_Type(Unsigned32):
    """Custom type multicastMembershipIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MulticastMembershipIndex_Type.__name__ = "Unsigned32"
_MulticastMembershipIndex_Object = MibTableColumn
multicastMembershipIndex = _MulticastMembershipIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 1),
    _MulticastMembershipIndex_Type()
)
multicastMembershipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastMembershipIndex.setStatus("current")
_MulticastMembershipName_Type = MgmtNameString
_MulticastMembershipName_Object = MibTableColumn
multicastMembershipName = _MulticastMembershipName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 2),
    _MulticastMembershipName_Type()
)
multicastMembershipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastMembershipName.setStatus("current")


class _MulticastMembershipInternalReference_Type(Unsigned32):
    """Custom type multicastMembershipInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MulticastMembershipInternalReference_Type.__name__ = "Unsigned32"
_MulticastMembershipInternalReference_Object = MibTableColumn
multicastMembershipInternalReference = _MulticastMembershipInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 3),
    _MulticastMembershipInternalReference_Type()
)
multicastMembershipInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastMembershipInternalReference.setStatus("current")


class _MulticastMembershipIdentifier_Type(DisplayString):
    """Custom type multicastMembershipIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 21),
    )


_MulticastMembershipIdentifier_Type.__name__ = "DisplayString"
_MulticastMembershipIdentifier_Object = MibTableColumn
multicastMembershipIdentifier = _MulticastMembershipIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 4),
    _MulticastMembershipIdentifier_Type()
)
multicastMembershipIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastMembershipIdentifier.setStatus("current")


class _MulticastMembershipSource_Type(IpAddress):
    """Custom type multicastMembershipSource based on IpAddress"""
    defaultHexValue = "00000000"


_MulticastMembershipSource_Type.__name__ = "IpAddress"
_MulticastMembershipSource_Object = MibTableColumn
multicastMembershipSource = _MulticastMembershipSource_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 5),
    _MulticastMembershipSource_Type()
)
multicastMembershipSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastMembershipSource.setStatus("current")
_MulticastMembershipGroup_Type = IpAddress
_MulticastMembershipGroup_Object = MibTableColumn
multicastMembershipGroup = _MulticastMembershipGroup_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 6),
    _MulticastMembershipGroup_Type()
)
multicastMembershipGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastMembershipGroup.setStatus("current")


class _MulticastMembershipVlan_Type(Unsigned32):
    """Custom type multicastMembershipVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MulticastMembershipVlan_Type.__name__ = "Unsigned32"
_MulticastMembershipVlan_Object = MibTableColumn
multicastMembershipVlan = _MulticastMembershipVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 7),
    _MulticastMembershipVlan_Type()
)
multicastMembershipVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastMembershipVlan.setStatus("current")


class _MulticastMembershipPorts_Type(Unsigned32):
    """Custom type multicastMembershipPorts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MulticastMembershipPorts_Type.__name__ = "Unsigned32"
_MulticastMembershipPorts_Object = MibTableColumn
multicastMembershipPorts = _MulticastMembershipPorts_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 8),
    _MulticastMembershipPorts_Type()
)
multicastMembershipPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastMembershipPorts.setStatus("current")


class _MulticastMembershipUpTime_Type(TimeTicks):
    """Custom type multicastMembershipUpTime based on TimeTicks"""
    defaultValue = 0


_MulticastMembershipUpTime_Type.__name__ = "TimeTicks"
_MulticastMembershipUpTime_Object = MibTableColumn
multicastMembershipUpTime = _MulticastMembershipUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 9),
    _MulticastMembershipUpTime_Type()
)
multicastMembershipUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastMembershipUpTime.setStatus("current")


class _MulticastMembershipExpiryTime_Type(TimeTicks):
    """Custom type multicastMembershipExpiryTime based on TimeTicks"""
    defaultValue = 0


_MulticastMembershipExpiryTime_Type.__name__ = "TimeTicks"
_MulticastMembershipExpiryTime_Object = MibTableColumn
multicastMembershipExpiryTime = _MulticastMembershipExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 10),
    _MulticastMembershipExpiryTime_Type()
)
multicastMembershipExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastMembershipExpiryTime.setStatus("current")


class _MulticastMembershipType_Type(Integer32):
    """Custom type multicastMembershipType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("user", 1),
          ("dynamic", 2))
    )


_MulticastMembershipType_Type.__name__ = "Integer32"
_MulticastMembershipType_Object = MibTableColumn
multicastMembershipType = _MulticastMembershipType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 11),
    _MulticastMembershipType_Type()
)
multicastMembershipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastMembershipType.setStatus("current")
_MulticastMembershipReporter_Type = IpAddress
_MulticastMembershipReporter_Object = MibTableColumn
multicastMembershipReporter = _MulticastMembershipReporter_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 3, 1, 1, 12),
    _MulticastMembershipReporter_Type()
)
multicastMembershipReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastMembershipReporter.setStatus("current")
_MulticastForwardingList_ObjectIdentity = ObjectIdentity
multicastForwardingList = _MulticastForwardingList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4)
)
_MulticastForwardingTable_Object = MibTable
multicastForwardingTable = _MulticastForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1)
)
if mibBuilder.loadTexts:
    multicastForwardingTable.setStatus("current")
_MulticastForwardingEntry_Object = MibTableRow
multicastForwardingEntry = _MulticastForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1, 1)
)
multicastForwardingEntry.setIndexNames(
    (0, "LUM-MULTICAST-MIB", "multicastForwardingIndex"),
)
if mibBuilder.loadTexts:
    multicastForwardingEntry.setStatus("current")


class _MulticastForwardingIndex_Type(Unsigned32):
    """Custom type multicastForwardingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MulticastForwardingIndex_Type.__name__ = "Unsigned32"
_MulticastForwardingIndex_Object = MibTableColumn
multicastForwardingIndex = _MulticastForwardingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1, 1, 1),
    _MulticastForwardingIndex_Type()
)
multicastForwardingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastForwardingIndex.setStatus("current")
_MulticastForwardingName_Type = MgmtNameString
_MulticastForwardingName_Object = MibTableColumn
multicastForwardingName = _MulticastForwardingName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1, 1, 2),
    _MulticastForwardingName_Type()
)
multicastForwardingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastForwardingName.setStatus("current")


class _MulticastForwardingInternalReference_Type(Unsigned32):
    """Custom type multicastForwardingInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MulticastForwardingInternalReference_Type.__name__ = "Unsigned32"
_MulticastForwardingInternalReference_Object = MibTableColumn
multicastForwardingInternalReference = _MulticastForwardingInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1, 1, 3),
    _MulticastForwardingInternalReference_Type()
)
multicastForwardingInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastForwardingInternalReference.setStatus("current")
_MulticastForwardingSource_Type = IpAddress
_MulticastForwardingSource_Object = MibTableColumn
multicastForwardingSource = _MulticastForwardingSource_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1, 1, 4),
    _MulticastForwardingSource_Type()
)
multicastForwardingSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastForwardingSource.setStatus("current")
_MulticastForwardingGroup_Type = IpAddress
_MulticastForwardingGroup_Object = MibTableColumn
multicastForwardingGroup = _MulticastForwardingGroup_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1, 1, 5),
    _MulticastForwardingGroup_Type()
)
multicastForwardingGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastForwardingGroup.setStatus("current")


class _MulticastForwardingVlan_Type(Unsigned32):
    """Custom type multicastForwardingVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MulticastForwardingVlan_Type.__name__ = "Unsigned32"
_MulticastForwardingVlan_Object = MibTableColumn
multicastForwardingVlan = _MulticastForwardingVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1, 1, 6),
    _MulticastForwardingVlan_Type()
)
multicastForwardingVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastForwardingVlan.setStatus("current")
_MulticastForwardingFwd_Type = TruthValue
_MulticastForwardingFwd_Object = MibTableColumn
multicastForwardingFwd = _MulticastForwardingFwd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1, 1, 7),
    _MulticastForwardingFwd_Type()
)
multicastForwardingFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastForwardingFwd.setStatus("current")


class _MulticastForwardingPorts_Type(Unsigned32):
    """Custom type multicastForwardingPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MulticastForwardingPorts_Type.__name__ = "Unsigned32"
_MulticastForwardingPorts_Object = MibTableColumn
multicastForwardingPorts = _MulticastForwardingPorts_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 4, 1, 1, 8),
    _MulticastForwardingPorts_Type()
)
multicastForwardingPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastForwardingPorts.setStatus("current")
_MulticastIgmpPmList_ObjectIdentity = ObjectIdentity
multicastIgmpPmList = _MulticastIgmpPmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5)
)
_MulticastIgmpPmTable_Object = MibTable
multicastIgmpPmTable = _MulticastIgmpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1)
)
if mibBuilder.loadTexts:
    multicastIgmpPmTable.setStatus("current")
_MulticastIgmpPmEntry_Object = MibTableRow
multicastIgmpPmEntry = _MulticastIgmpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1)
)
multicastIgmpPmEntry.setIndexNames(
    (0, "LUM-MULTICAST-MIB", "multicastIgmpPmIndex"),
)
if mibBuilder.loadTexts:
    multicastIgmpPmEntry.setStatus("current")


class _MulticastIgmpPmIndex_Type(Unsigned32):
    """Custom type multicastIgmpPmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MulticastIgmpPmIndex_Type.__name__ = "Unsigned32"
_MulticastIgmpPmIndex_Object = MibTableColumn
multicastIgmpPmIndex = _MulticastIgmpPmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 1),
    _MulticastIgmpPmIndex_Type()
)
multicastIgmpPmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmIndex.setStatus("current")
_MulticastIgmpPmName_Type = MgmtNameString
_MulticastIgmpPmName_Object = MibTableColumn
multicastIgmpPmName = _MulticastIgmpPmName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 2),
    _MulticastIgmpPmName_Type()
)
multicastIgmpPmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmName.setStatus("current")
_MulticastIgmpPmRxReportsV1_Type = Gauge32
_MulticastIgmpPmRxReportsV1_Object = MibTableColumn
multicastIgmpPmRxReportsV1 = _MulticastIgmpPmRxReportsV1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 3),
    _MulticastIgmpPmRxReportsV1_Type()
)
multicastIgmpPmRxReportsV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmRxReportsV1.setStatus("current")
_MulticastIgmpPmRxReportsV2_Type = Gauge32
_MulticastIgmpPmRxReportsV2_Object = MibTableColumn
multicastIgmpPmRxReportsV2 = _MulticastIgmpPmRxReportsV2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 4),
    _MulticastIgmpPmRxReportsV2_Type()
)
multicastIgmpPmRxReportsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmRxReportsV2.setStatus("current")
_MulticastIgmpPmRxReportsV3_Type = Gauge32
_MulticastIgmpPmRxReportsV3_Object = MibTableColumn
multicastIgmpPmRxReportsV3 = _MulticastIgmpPmRxReportsV3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 5),
    _MulticastIgmpPmRxReportsV3_Type()
)
multicastIgmpPmRxReportsV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmRxReportsV3.setStatus("current")
_MulticastIgmpPmTxReportsV1_Type = Gauge32
_MulticastIgmpPmTxReportsV1_Object = MibTableColumn
multicastIgmpPmTxReportsV1 = _MulticastIgmpPmTxReportsV1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 6),
    _MulticastIgmpPmTxReportsV1_Type()
)
multicastIgmpPmTxReportsV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmTxReportsV1.setStatus("current")
_MulticastIgmpPmTxReportsV2_Type = Gauge32
_MulticastIgmpPmTxReportsV2_Object = MibTableColumn
multicastIgmpPmTxReportsV2 = _MulticastIgmpPmTxReportsV2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 7),
    _MulticastIgmpPmTxReportsV2_Type()
)
multicastIgmpPmTxReportsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmTxReportsV2.setStatus("current")
_MulticastIgmpPmTxReportsV3_Type = Gauge32
_MulticastIgmpPmTxReportsV3_Object = MibTableColumn
multicastIgmpPmTxReportsV3 = _MulticastIgmpPmTxReportsV3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 8),
    _MulticastIgmpPmTxReportsV3_Type()
)
multicastIgmpPmTxReportsV3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmTxReportsV3.setStatus("current")
_MulticastIgmpPmRxQueries_Type = Gauge32
_MulticastIgmpPmRxQueries_Object = MibTableColumn
multicastIgmpPmRxQueries = _MulticastIgmpPmRxQueries_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 9),
    _MulticastIgmpPmRxQueries_Type()
)
multicastIgmpPmRxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmRxQueries.setStatus("current")
_MulticastIgmpPmTxQueries_Type = Gauge32
_MulticastIgmpPmTxQueries_Object = MibTableColumn
multicastIgmpPmTxQueries = _MulticastIgmpPmTxQueries_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 10),
    _MulticastIgmpPmTxQueries_Type()
)
multicastIgmpPmTxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmTxQueries.setStatus("current")
_MulticastIgmpPmRxLeavesV2_Type = Gauge32
_MulticastIgmpPmRxLeavesV2_Object = MibTableColumn
multicastIgmpPmRxLeavesV2 = _MulticastIgmpPmRxLeavesV2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 11),
    _MulticastIgmpPmRxLeavesV2_Type()
)
multicastIgmpPmRxLeavesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmRxLeavesV2.setStatus("current")
_MulticastIgmpPmTxLeavesV2_Type = Gauge32
_MulticastIgmpPmTxLeavesV2_Object = MibTableColumn
multicastIgmpPmTxLeavesV2 = _MulticastIgmpPmTxLeavesV2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 12),
    _MulticastIgmpPmTxLeavesV2_Type()
)
multicastIgmpPmTxLeavesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmTxLeavesV2.setStatus("current")
_MulticastIgmpPmRxChksumErrors_Type = Gauge32
_MulticastIgmpPmRxChksumErrors_Object = MibTableColumn
multicastIgmpPmRxChksumErrors = _MulticastIgmpPmRxChksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 13),
    _MulticastIgmpPmRxChksumErrors_Type()
)
multicastIgmpPmRxChksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmRxChksumErrors.setStatus("current")
_MulticastIgmpPmRxUnknownType_Type = Gauge32
_MulticastIgmpPmRxUnknownType_Object = MibTableColumn
multicastIgmpPmRxUnknownType = _MulticastIgmpPmRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 14),
    _MulticastIgmpPmRxUnknownType_Type()
)
multicastIgmpPmRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmRxUnknownType.setStatus("current")
_MulticastIgmpPmRxIllegalLength_Type = Gauge32
_MulticastIgmpPmRxIllegalLength_Object = MibTableColumn
multicastIgmpPmRxIllegalLength = _MulticastIgmpPmRxIllegalLength_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 15),
    _MulticastIgmpPmRxIllegalLength_Type()
)
multicastIgmpPmRxIllegalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmRxIllegalLength.setStatus("current")
_MulticastIgmpPmDropHosts_Type = Gauge32
_MulticastIgmpPmDropHosts_Object = MibTableColumn
multicastIgmpPmDropHosts = _MulticastIgmpPmDropHosts_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 16),
    _MulticastIgmpPmDropHosts_Type()
)
multicastIgmpPmDropHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmDropHosts.setStatus("current")
_MulticastIgmpPmMembers_Type = Gauge32
_MulticastIgmpPmMembers_Object = MibTableColumn
multicastIgmpPmMembers = _MulticastIgmpPmMembers_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 17),
    _MulticastIgmpPmMembers_Type()
)
multicastIgmpPmMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multicastIgmpPmMembers.setStatus("current")


class _MulticastIgmpPmReset_Type(PmReset):
    """Custom type multicastIgmpPmReset based on PmReset"""
    defaultValue = 1


_MulticastIgmpPmReset_Type.__name__ = "PmReset"
_MulticastIgmpPmReset_Object = MibTableColumn
multicastIgmpPmReset = _MulticastIgmpPmReset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 2, 5, 1, 1, 18),
    _MulticastIgmpPmReset_Type()
)
multicastIgmpPmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastIgmpPmReset.setStatus("current")

# Managed Objects groups

multicastGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1, 1, 1)
)
multicastGeneralGroupV1.setObjects(
      *(("LUM-MULTICAST-MIB", "multicastGeneralLastChangeTime"),
        ("LUM-MULTICAST-MIB", "multicastGeneralStateLastChangeTime"),
        ("LUM-MULTICAST-MIB", "multicastGeneralMulticastIfTableSize"),
        ("LUM-MULTICAST-MIB", "multicastGeneralMulticastMembershipTableSize"))
)
if mibBuilder.loadTexts:
    multicastGeneralGroupV1.setStatus("current")

multicastIfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1, 1, 2)
)
multicastIfGroupV1.setObjects(
      *(("LUM-MULTICAST-MIB", "multicastIfIndex"),
        ("LUM-MULTICAST-MIB", "multicastIfName"),
        ("LUM-MULTICAST-MIB", "multicastIfDescr"),
        ("LUM-MULTICAST-MIB", "multicastIfProtocol"),
        ("LUM-MULTICAST-MIB", "multicastIfRouterEnable"),
        ("LUM-MULTICAST-MIB", "multicastIfFastLeave"),
        ("LUM-MULTICAST-MIB", "multicastIfReservedFlooding"),
        ("LUM-MULTICAST-MIB", "multicastIfRobustness"),
        ("LUM-MULTICAST-MIB", "multicastIfAssociateStaticMember"),
        ("LUM-MULTICAST-MIB", "multicastIfMembersMax"),
        ("LUM-MULTICAST-MIB", "multicastIfNoOfStaticMembers"),
        ("LUM-MULTICAST-MIB", "multicastIfMembershipFiltering"),
        ("LUM-MULTICAST-MIB", "multicastIfForwardingFiltering"),
        ("LUM-MULTICAST-MIB", "multicastIfDeleteMembers"))
)
if mibBuilder.loadTexts:
    multicastIfGroupV1.setStatus("current")

multicastMembershipGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1, 1, 3)
)
multicastMembershipGroupV1.setObjects(
      *(("LUM-MULTICAST-MIB", "multicastMembershipIndex"),
        ("LUM-MULTICAST-MIB", "multicastMembershipName"),
        ("LUM-MULTICAST-MIB", "multicastMembershipInternalReference"),
        ("LUM-MULTICAST-MIB", "multicastMembershipIdentifier"),
        ("LUM-MULTICAST-MIB", "multicastMembershipSource"),
        ("LUM-MULTICAST-MIB", "multicastMembershipGroup"),
        ("LUM-MULTICAST-MIB", "multicastMembershipVlan"),
        ("LUM-MULTICAST-MIB", "multicastMembershipPorts"),
        ("LUM-MULTICAST-MIB", "multicastMembershipUpTime"),
        ("LUM-MULTICAST-MIB", "multicastMembershipExpiryTime"),
        ("LUM-MULTICAST-MIB", "multicastMembershipType"),
        ("LUM-MULTICAST-MIB", "multicastMembershipReporter"))
)
if mibBuilder.loadTexts:
    multicastMembershipGroupV1.setStatus("current")

multicastForwardingGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1, 1, 4)
)
multicastForwardingGroupV1.setObjects(
      *(("LUM-MULTICAST-MIB", "multicastForwardingIndex"),
        ("LUM-MULTICAST-MIB", "multicastForwardingName"),
        ("LUM-MULTICAST-MIB", "multicastForwardingInternalReference"),
        ("LUM-MULTICAST-MIB", "multicastForwardingSource"),
        ("LUM-MULTICAST-MIB", "multicastForwardingGroup"),
        ("LUM-MULTICAST-MIB", "multicastForwardingVlan"),
        ("LUM-MULTICAST-MIB", "multicastForwardingFwd"),
        ("LUM-MULTICAST-MIB", "multicastForwardingPorts"))
)
if mibBuilder.loadTexts:
    multicastForwardingGroupV1.setStatus("current")

multicastIgmpPmGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1, 1, 5)
)
multicastIgmpPmGroupV1.setObjects(
      *(("LUM-MULTICAST-MIB", "multicastIgmpPmIndex"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmName"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmRxReportsV1"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmRxReportsV2"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmRxReportsV3"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmTxReportsV1"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmTxReportsV2"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmTxReportsV3"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmRxQueries"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmTxQueries"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmRxLeavesV2"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmTxLeavesV2"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmRxChksumErrors"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmRxUnknownType"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmRxIllegalLength"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmDropHosts"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmMembers"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmReset"))
)
if mibBuilder.loadTexts:
    multicastIgmpPmGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumMulticastBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1, 2, 3)
)
lumMulticastBasicComplV1.setObjects(
      *(("LUM-MULTICAST-MIB", "multicastGeneralGroupV1"),
        ("LUM-MULTICAST-MIB", "multicastIfGroupV1"),
        ("LUM-MULTICAST-MIB", "multicastMembershipGroupV1"),
        ("LUM-MULTICAST-MIB", "multicastForwardingGroupV1"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmGroupV1"))
)
if mibBuilder.loadTexts:
    lumMulticastBasicComplV1.setStatus(
        "deprecated"
    )

lumMulticastBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 37, 1, 2, 4)
)
lumMulticastBasicComplV2.setObjects(
      *(("LUM-MULTICAST-MIB", "multicastGeneralGroupV1"),
        ("LUM-MULTICAST-MIB", "multicastIfGroupV1"),
        ("LUM-MULTICAST-MIB", "multicastMembershipGroupV1"),
        ("LUM-MULTICAST-MIB", "multicastForwardingGroupV1"),
        ("LUM-MULTICAST-MIB", "multicastIgmpPmGroupV1"))
)
if mibBuilder.loadTexts:
    lumMulticastBasicComplV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-MULTICAST-MIB",
    **{"lumMulticastMIBModule": lumMulticastMIBModule,
       "lumMulticastConfs": lumMulticastConfs,
       "lumMulticastGroups": lumMulticastGroups,
       "multicastGeneralGroupV1": multicastGeneralGroupV1,
       "multicastIfGroupV1": multicastIfGroupV1,
       "multicastMembershipGroupV1": multicastMembershipGroupV1,
       "multicastForwardingGroupV1": multicastForwardingGroupV1,
       "multicastIgmpPmGroupV1": multicastIgmpPmGroupV1,
       "lumMulticastCompl": lumMulticastCompl,
       "lumMulticastBasicComplV1": lumMulticastBasicComplV1,
       "lumMulticastBasicComplV2": lumMulticastBasicComplV2,
       "lumMulticastMIBObjects": lumMulticastMIBObjects,
       "multicastGeneral": multicastGeneral,
       "multicastGeneralLastChangeTime": multicastGeneralLastChangeTime,
       "multicastGeneralStateLastChangeTime": multicastGeneralStateLastChangeTime,
       "multicastGeneralMulticastIfTableSize": multicastGeneralMulticastIfTableSize,
       "multicastGeneralMulticastMembershipTableSize": multicastGeneralMulticastMembershipTableSize,
       "multicastGeneralMulticastForwardingTableSize": multicastGeneralMulticastForwardingTableSize,
       "multicastGeneralPmIgmpPortTableSize": multicastGeneralPmIgmpPortTableSize,
       "multicastIfList": multicastIfList,
       "multicastIfTable": multicastIfTable,
       "multicastIfEntry": multicastIfEntry,
       "multicastIfIndex": multicastIfIndex,
       "multicastIfName": multicastIfName,
       "multicastIfDescr": multicastIfDescr,
       "multicastIfProtocol": multicastIfProtocol,
       "multicastIfRouterEnable": multicastIfRouterEnable,
       "multicastIfFastLeave": multicastIfFastLeave,
       "multicastIfRobustness": multicastIfRobustness,
       "multicastIfReservedFlooding": multicastIfReservedFlooding,
       "multicastIfAssociateStaticMember": multicastIfAssociateStaticMember,
       "multicastIfMembersMax": multicastIfMembersMax,
       "multicastIfNoOfStaticMembers": multicastIfNoOfStaticMembers,
       "multicastIfMembershipFiltering": multicastIfMembershipFiltering,
       "multicastIfForwardingFiltering": multicastIfForwardingFiltering,
       "multicastIfDeleteMembers": multicastIfDeleteMembers,
       "multicastMembershipList": multicastMembershipList,
       "multicastMembershipTable": multicastMembershipTable,
       "multicastMembershipEntry": multicastMembershipEntry,
       "multicastMembershipIndex": multicastMembershipIndex,
       "multicastMembershipName": multicastMembershipName,
       "multicastMembershipInternalReference": multicastMembershipInternalReference,
       "multicastMembershipIdentifier": multicastMembershipIdentifier,
       "multicastMembershipSource": multicastMembershipSource,
       "multicastMembershipGroup": multicastMembershipGroup,
       "multicastMembershipVlan": multicastMembershipVlan,
       "multicastMembershipPorts": multicastMembershipPorts,
       "multicastMembershipUpTime": multicastMembershipUpTime,
       "multicastMembershipExpiryTime": multicastMembershipExpiryTime,
       "multicastMembershipType": multicastMembershipType,
       "multicastMembershipReporter": multicastMembershipReporter,
       "multicastForwardingList": multicastForwardingList,
       "multicastForwardingTable": multicastForwardingTable,
       "multicastForwardingEntry": multicastForwardingEntry,
       "multicastForwardingIndex": multicastForwardingIndex,
       "multicastForwardingName": multicastForwardingName,
       "multicastForwardingInternalReference": multicastForwardingInternalReference,
       "multicastForwardingSource": multicastForwardingSource,
       "multicastForwardingGroup": multicastForwardingGroup,
       "multicastForwardingVlan": multicastForwardingVlan,
       "multicastForwardingFwd": multicastForwardingFwd,
       "multicastForwardingPorts": multicastForwardingPorts,
       "multicastIgmpPmList": multicastIgmpPmList,
       "multicastIgmpPmTable": multicastIgmpPmTable,
       "multicastIgmpPmEntry": multicastIgmpPmEntry,
       "multicastIgmpPmIndex": multicastIgmpPmIndex,
       "multicastIgmpPmName": multicastIgmpPmName,
       "multicastIgmpPmRxReportsV1": multicastIgmpPmRxReportsV1,
       "multicastIgmpPmRxReportsV2": multicastIgmpPmRxReportsV2,
       "multicastIgmpPmRxReportsV3": multicastIgmpPmRxReportsV3,
       "multicastIgmpPmTxReportsV1": multicastIgmpPmTxReportsV1,
       "multicastIgmpPmTxReportsV2": multicastIgmpPmTxReportsV2,
       "multicastIgmpPmTxReportsV3": multicastIgmpPmTxReportsV3,
       "multicastIgmpPmRxQueries": multicastIgmpPmRxQueries,
       "multicastIgmpPmTxQueries": multicastIgmpPmTxQueries,
       "multicastIgmpPmRxLeavesV2": multicastIgmpPmRxLeavesV2,
       "multicastIgmpPmTxLeavesV2": multicastIgmpPmTxLeavesV2,
       "multicastIgmpPmRxChksumErrors": multicastIgmpPmRxChksumErrors,
       "multicastIgmpPmRxUnknownType": multicastIgmpPmRxUnknownType,
       "multicastIgmpPmRxIllegalLength": multicastIgmpPmRxIllegalLength,
       "multicastIgmpPmDropHosts": multicastIgmpPmDropHosts,
       "multicastIgmpPmMembers": multicastIgmpPmMembers,
       "multicastIgmpPmReset": multicastIgmpPmReset}
)
