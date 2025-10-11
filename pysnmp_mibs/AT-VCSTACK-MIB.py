# SNMP MIB module (AT-VCSTACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/AT-VCSTACK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:23:35 2025
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

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "sysinfo")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vcstack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13)
)
if mibBuilder.loadTexts:
    vcstack.setRevisions(
        ("2009-06-08 00:00",
         "2008-03-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _VcstackStatus_Type(Integer32):
    """Custom type vcstackStatus based on Integer32"""
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
        *(("normalOperation", 1),
          ("operatingInFailoverState", 2),
          ("standaloneUnit", 3),
          ("ringTopologyBroken", 4))
    )


_VcstackStatus_Type.__name__ = "Integer32"
_VcstackStatus_Object = MibScalar
vcstackStatus = _VcstackStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 1),
    _VcstackStatus_Type()
)
vcstackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStatus.setStatus("current")


class _VcstackOperationalStatus_Type(Integer32):
    """Custom type vcstackOperationalStatus based on Integer32"""
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


_VcstackOperationalStatus_Type.__name__ = "Integer32"
_VcstackOperationalStatus_Object = MibScalar
vcstackOperationalStatus = _VcstackOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 2),
    _VcstackOperationalStatus_Type()
)
vcstackOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackOperationalStatus.setStatus("current")
_VcstackMgmtVlanId_Type = Integer32
_VcstackMgmtVlanId_Object = MibScalar
vcstackMgmtVlanId = _VcstackMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 3),
    _VcstackMgmtVlanId_Type()
)
vcstackMgmtVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackMgmtVlanId.setStatus("current")
_VcstackMgmtVlanSubnetAddr_Type = IpAddress
_VcstackMgmtVlanSubnetAddr_Object = MibScalar
vcstackMgmtVlanSubnetAddr = _VcstackMgmtVlanSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 4),
    _VcstackMgmtVlanSubnetAddr_Type()
)
vcstackMgmtVlanSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackMgmtVlanSubnetAddr.setStatus("current")
_VcstackTable_Object = MibTable
vcstackTable = _VcstackTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5)
)
if mibBuilder.loadTexts:
    vcstackTable.setStatus("current")
_VcstackEntry_Object = MibTableRow
vcstackEntry = _VcstackEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1)
)
vcstackEntry.setIndexNames(
    (0, "AT-VCSTACK-MIB", "vcstackId"),
)
if mibBuilder.loadTexts:
    vcstackEntry.setStatus("current")


class _VcstackId_Type(Unsigned32):
    """Custom type vcstackId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcstackId_Type.__name__ = "Unsigned32"
_VcstackId_Object = MibTableColumn
vcstackId = _VcstackId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 1),
    _VcstackId_Type()
)
vcstackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackId.setStatus("current")


class _VcstackPendingId_Type(Unsigned32):
    """Custom type vcstackPendingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcstackPendingId_Type.__name__ = "Unsigned32"
_VcstackPendingId_Object = MibTableColumn
vcstackPendingId = _VcstackPendingId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 2),
    _VcstackPendingId_Type()
)
vcstackPendingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackPendingId.setStatus("current")
_VcstackMacAddr_Type = MacAddress
_VcstackMacAddr_Object = MibTableColumn
vcstackMacAddr = _VcstackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 3),
    _VcstackMacAddr_Type()
)
vcstackMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackMacAddr.setStatus("current")


class _VcstackPriority_Type(Unsigned32):
    """Custom type vcstackPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VcstackPriority_Type.__name__ = "Unsigned32"
_VcstackPriority_Object = MibTableColumn
vcstackPriority = _VcstackPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 4),
    _VcstackPriority_Type()
)
vcstackPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackPriority.setStatus("current")


class _VcstackRole_Type(Integer32):
    """Custom type vcstackRole based on Integer32"""
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
        *(("leaving", 1),
          ("discovering", 2),
          ("synchronizing", 3),
          ("backupMember", 4),
          ("pendingMaster", 5),
          ("disabledMaster", 6),
          ("fallbackMaster", 7),
          ("activeMaster", 8))
    )


_VcstackRole_Type.__name__ = "Integer32"
_VcstackRole_Object = MibTableColumn
vcstackRole = _VcstackRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 5),
    _VcstackRole_Type()
)
vcstackRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackRole.setStatus("current")
_VcstackLastRoleChange_Type = DisplayString
_VcstackLastRoleChange_Object = MibTableColumn
vcstackLastRoleChange = _VcstackLastRoleChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 6),
    _VcstackLastRoleChange_Type()
)
vcstackLastRoleChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackLastRoleChange.setStatus("current")
_VcstackHostname_Type = DisplayString
_VcstackHostname_Object = MibTableColumn
vcstackHostname = _VcstackHostname_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 7),
    _VcstackHostname_Type()
)
vcstackHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackHostname.setStatus("current")
_VcstackProductType_Type = DisplayString
_VcstackProductType_Object = MibTableColumn
vcstackProductType = _VcstackProductType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 8),
    _VcstackProductType_Type()
)
vcstackProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackProductType.setStatus("current")
_VcstackSWVersionAutoSync_Type = TruthValue
_VcstackSWVersionAutoSync_Object = MibTableColumn
vcstackSWVersionAutoSync = _VcstackSWVersionAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 9),
    _VcstackSWVersionAutoSync_Type()
)
vcstackSWVersionAutoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackSWVersionAutoSync.setStatus("current")


class _VcstackFallbackConfigStatus_Type(Integer32):
    """Custom type vcstackFallbackConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fileExists", 1),
          ("fileNotFound", 2),
          ("notConfigured", 3))
    )


_VcstackFallbackConfigStatus_Type.__name__ = "Integer32"
_VcstackFallbackConfigStatus_Object = MibTableColumn
vcstackFallbackConfigStatus = _VcstackFallbackConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 10),
    _VcstackFallbackConfigStatus_Type()
)
vcstackFallbackConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackFallbackConfigStatus.setStatus("current")
_VcstackFallbackConfigFilename_Type = DisplayString
_VcstackFallbackConfigFilename_Object = MibTableColumn
vcstackFallbackConfigFilename = _VcstackFallbackConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 11),
    _VcstackFallbackConfigFilename_Type()
)
vcstackFallbackConfigFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackFallbackConfigFilename.setStatus("current")


class _VcstackResiliencyLinkStatus_Type(Integer32):
    """Custom type vcstackResiliencyLinkStatus based on Integer32"""
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
        *(("configured", 1),
          ("successful", 2),
          ("failed", 3),
          ("notConfigured", 4))
    )


_VcstackResiliencyLinkStatus_Type.__name__ = "Integer32"
_VcstackResiliencyLinkStatus_Object = MibTableColumn
vcstackResiliencyLinkStatus = _VcstackResiliencyLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 12),
    _VcstackResiliencyLinkStatus_Type()
)
vcstackResiliencyLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackResiliencyLinkStatus.setStatus("current")
_VcstackResiliencyLinkInterfaceName_Type = DisplayString
_VcstackResiliencyLinkInterfaceName_Object = MibTableColumn
vcstackResiliencyLinkInterfaceName = _VcstackResiliencyLinkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 13),
    _VcstackResiliencyLinkInterfaceName_Type()
)
vcstackResiliencyLinkInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackResiliencyLinkInterfaceName.setStatus("current")


class _VcstackActiveStkHardware_Type(Integer32):
    """Custom type vcstackActiveStkHardware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("xemStk", 1),
          ("builtinStackingPorts", 2),
          ("none", 3))
    )


_VcstackActiveStkHardware_Type.__name__ = "Integer32"
_VcstackActiveStkHardware_Object = MibTableColumn
vcstackActiveStkHardware = _VcstackActiveStkHardware_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 14),
    _VcstackActiveStkHardware_Type()
)
vcstackActiveStkHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackActiveStkHardware.setStatus("current")


class _VcstackStkPort1Status_Type(Integer32):
    """Custom type vcstackStkPort1Status based on Integer32"""
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
        *(("down", 1),
          ("neighbourIncompatible", 2),
          ("discoveringNeighbour", 3),
          ("learntNeighbour", 4))
    )


_VcstackStkPort1Status_Type.__name__ = "Integer32"
_VcstackStkPort1Status_Object = MibTableColumn
vcstackStkPort1Status = _VcstackStkPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 15),
    _VcstackStkPort1Status_Type()
)
vcstackStkPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStkPort1Status.setStatus("current")


class _VcstackStkPort1NeighbourId_Type(Unsigned32):
    """Custom type vcstackStkPort1NeighbourId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VcstackStkPort1NeighbourId_Type.__name__ = "Unsigned32"
_VcstackStkPort1NeighbourId_Object = MibTableColumn
vcstackStkPort1NeighbourId = _VcstackStkPort1NeighbourId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 16),
    _VcstackStkPort1NeighbourId_Type()
)
vcstackStkPort1NeighbourId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStkPort1NeighbourId.setStatus("current")


class _VcstackStkPort2Status_Type(Integer32):
    """Custom type vcstackStkPort2Status based on Integer32"""
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
        *(("down", 1),
          ("neighbourIncompatible", 2),
          ("discoveringNeighbour", 3),
          ("learntNeighbour", 4))
    )


_VcstackStkPort2Status_Type.__name__ = "Integer32"
_VcstackStkPort2Status_Object = MibTableColumn
vcstackStkPort2Status = _VcstackStkPort2Status_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 17),
    _VcstackStkPort2Status_Type()
)
vcstackStkPort2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStkPort2Status.setStatus("current")


class _VcstackStkPort2NeighbourId_Type(Unsigned32):
    """Custom type vcstackStkPort2NeighbourId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VcstackStkPort2NeighbourId_Type.__name__ = "Unsigned32"
_VcstackStkPort2NeighbourId_Object = MibTableColumn
vcstackStkPort2NeighbourId = _VcstackStkPort2NeighbourId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 18),
    _VcstackStkPort2NeighbourId_Type()
)
vcstackStkPort2NeighbourId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackStkPort2NeighbourId.setStatus("current")
_VcstackNumMembersJoined_Type = Counter32
_VcstackNumMembersJoined_Object = MibTableColumn
vcstackNumMembersJoined = _VcstackNumMembersJoined_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 19),
    _VcstackNumMembersJoined_Type()
)
vcstackNumMembersJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumMembersJoined.setStatus("current")
_VcstackNumMembersLeft_Type = Counter32
_VcstackNumMembersLeft_Object = MibTableColumn
vcstackNumMembersLeft = _VcstackNumMembersLeft_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 20),
    _VcstackNumMembersLeft_Type()
)
vcstackNumMembersLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumMembersLeft.setStatus("current")
_VcstackNumIdConflict_Type = Counter32
_VcstackNumIdConflict_Object = MibTableColumn
vcstackNumIdConflict = _VcstackNumIdConflict_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 21),
    _VcstackNumIdConflict_Type()
)
vcstackNumIdConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumIdConflict.setStatus("current")
_VcstackNumMasterConflict_Type = Counter32
_VcstackNumMasterConflict_Object = MibTableColumn
vcstackNumMasterConflict = _VcstackNumMasterConflict_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 22),
    _VcstackNumMasterConflict_Type()
)
vcstackNumMasterConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumMasterConflict.setStatus("current")
_VcstackNumMasterFailover_Type = Counter32
_VcstackNumMasterFailover_Object = MibTableColumn
vcstackNumMasterFailover = _VcstackNumMasterFailover_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 23),
    _VcstackNumMasterFailover_Type()
)
vcstackNumMasterFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumMasterFailover.setStatus("current")
_VcstackNumStkPort1NbrIncompatible_Type = Counter32
_VcstackNumStkPort1NbrIncompatible_Object = MibTableColumn
vcstackNumStkPort1NbrIncompatible = _VcstackNumStkPort1NbrIncompatible_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 24),
    _VcstackNumStkPort1NbrIncompatible_Type()
)
vcstackNumStkPort1NbrIncompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumStkPort1NbrIncompatible.setStatus("current")
_VcstackNumStkPort2NbrIncompatible_Type = Counter32
_VcstackNumStkPort2NbrIncompatible_Object = MibTableColumn
vcstackNumStkPort2NbrIncompatible = _VcstackNumStkPort2NbrIncompatible_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 5, 1, 25),
    _VcstackNumStkPort2NbrIncompatible_Type()
)
vcstackNumStkPort2NbrIncompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcstackNumStkPort2NbrIncompatible.setStatus("current")
_VcstackTraps_ObjectIdentity = ObjectIdentity
vcstackTraps = _VcstackTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6)
)


class _VcstackNbrMemberId_Type(Unsigned32):
    """Custom type vcstackNbrMemberId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcstackNbrMemberId_Type.__name__ = "Unsigned32"
_VcstackNbrMemberId_Object = MibScalar
vcstackNbrMemberId = _VcstackNbrMemberId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 8),
    _VcstackNbrMemberId_Type()
)
vcstackNbrMemberId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vcstackNbrMemberId.setStatus("current")
_VcstackStkPortName_Type = DisplayString
_VcstackStkPortName_Object = MibScalar
vcstackStkPortName = _VcstackStkPortName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 9),
    _VcstackStkPortName_Type()
)
vcstackStkPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vcstackStkPortName.setStatus("current")

# Managed Objects groups


# Notification objects

vcstackRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 1)
)
vcstackRoleChange.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackRole"))
)
if mibBuilder.loadTexts:
    vcstackRoleChange.setStatus(
        "current"
    )

vcstackMemberJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 2)
)
vcstackMemberJoin.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackNbrMemberId"))
)
if mibBuilder.loadTexts:
    vcstackMemberJoin.setStatus(
        "current"
    )

vcstackMemberLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 3)
)
vcstackMemberLeave.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackNbrMemberId"))
)
if mibBuilder.loadTexts:
    vcstackMemberLeave.setStatus(
        "current"
    )

vcstackResiliencyLinkHealthCheckReceiving = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 4)
)
vcstackResiliencyLinkHealthCheckReceiving.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
)
if mibBuilder.loadTexts:
    vcstackResiliencyLinkHealthCheckReceiving.setStatus(
        "current"
    )

vcstackResiliencyLinkHealthCheckTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 5)
)
vcstackResiliencyLinkHealthCheckTimeOut.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackResiliencyLinkInterfaceName"))
)
if mibBuilder.loadTexts:
    vcstackResiliencyLinkHealthCheckTimeOut.setStatus(
        "current"
    )

vcstackStkPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 6)
)
vcstackStkPortLinkUp.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackStkPortName"))
)
if mibBuilder.loadTexts:
    vcstackStkPortLinkUp.setStatus(
        "current"
    )

vcstackStkPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 13, 6, 7)
)
vcstackStkPortLinkDown.setObjects(
      *(("AT-VCSTACK-MIB", "vcstackId"),
        ("AT-VCSTACK-MIB", "vcstackStkPortName"))
)
if mibBuilder.loadTexts:
    vcstackStkPortLinkDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-VCSTACK-MIB",
    **{"vcstack": vcstack,
       "vcstackStatus": vcstackStatus,
       "vcstackOperationalStatus": vcstackOperationalStatus,
       "vcstackMgmtVlanId": vcstackMgmtVlanId,
       "vcstackMgmtVlanSubnetAddr": vcstackMgmtVlanSubnetAddr,
       "vcstackTable": vcstackTable,
       "vcstackEntry": vcstackEntry,
       "vcstackId": vcstackId,
       "vcstackPendingId": vcstackPendingId,
       "vcstackMacAddr": vcstackMacAddr,
       "vcstackPriority": vcstackPriority,
       "vcstackRole": vcstackRole,
       "vcstackLastRoleChange": vcstackLastRoleChange,
       "vcstackHostname": vcstackHostname,
       "vcstackProductType": vcstackProductType,
       "vcstackSWVersionAutoSync": vcstackSWVersionAutoSync,
       "vcstackFallbackConfigStatus": vcstackFallbackConfigStatus,
       "vcstackFallbackConfigFilename": vcstackFallbackConfigFilename,
       "vcstackResiliencyLinkStatus": vcstackResiliencyLinkStatus,
       "vcstackResiliencyLinkInterfaceName": vcstackResiliencyLinkInterfaceName,
       "vcstackActiveStkHardware": vcstackActiveStkHardware,
       "vcstackStkPort1Status": vcstackStkPort1Status,
       "vcstackStkPort1NeighbourId": vcstackStkPort1NeighbourId,
       "vcstackStkPort2Status": vcstackStkPort2Status,
       "vcstackStkPort2NeighbourId": vcstackStkPort2NeighbourId,
       "vcstackNumMembersJoined": vcstackNumMembersJoined,
       "vcstackNumMembersLeft": vcstackNumMembersLeft,
       "vcstackNumIdConflict": vcstackNumIdConflict,
       "vcstackNumMasterConflict": vcstackNumMasterConflict,
       "vcstackNumMasterFailover": vcstackNumMasterFailover,
       "vcstackNumStkPort1NbrIncompatible": vcstackNumStkPort1NbrIncompatible,
       "vcstackNumStkPort2NbrIncompatible": vcstackNumStkPort2NbrIncompatible,
       "vcstackTraps": vcstackTraps,
       "vcstackRoleChange": vcstackRoleChange,
       "vcstackMemberJoin": vcstackMemberJoin,
       "vcstackMemberLeave": vcstackMemberLeave,
       "vcstackResiliencyLinkHealthCheckReceiving": vcstackResiliencyLinkHealthCheckReceiving,
       "vcstackResiliencyLinkHealthCheckTimeOut": vcstackResiliencyLinkHealthCheckTimeOut,
       "vcstackStkPortLinkUp": vcstackStkPortLinkUp,
       "vcstackStkPortLinkDown": vcstackStkPortLinkDown,
       "vcstackNbrMemberId": vcstackNbrMemberId,
       "vcstackStkPortName": vcstackStkPortName}
)
