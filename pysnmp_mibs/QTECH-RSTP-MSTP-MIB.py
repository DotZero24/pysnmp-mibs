# SNMP MIB module (QTECH-RSTP-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-RSTP-MSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:30 2025
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus",
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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechStpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16)
)
if mibBuilder.loadTexts:
    qtechStpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechStpMIBObjects_ObjectIdentity = ObjectIdentity
qtechStpMIBObjects = _QtechStpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 1)
)


class _QtechSysStpStatus_Type(EnabledStatus):
    """Custom type qtechSysStpStatus based on EnabledStatus"""
    defaultValue = 2


_QtechSysStpStatus_Type.__name__ = "EnabledStatus"
_QtechSysStpStatus_Object = MibScalar
qtechSysStpStatus = _QtechSysStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 1, 1),
    _QtechSysStpStatus_Type()
)
qtechSysStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSysStpStatus.setStatus("current")
_QtechSysStpReset_Type = Integer32
_QtechSysStpReset_Object = MibScalar
qtechSysStpReset = _QtechSysStpReset_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 1, 2),
    _QtechSysStpReset_Type()
)
qtechSysStpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSysStpReset.setStatus("current")
_QtechStpExtPortTable_Object = MibTable
qtechStpExtPortTable = _QtechStpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 1, 3)
)
if mibBuilder.loadTexts:
    qtechStpExtPortTable.setStatus("current")
_QtechStpExtPortEntry_Object = MibTableRow
qtechStpExtPortEntry = _QtechStpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 1, 3, 1)
)
qtechStpExtPortEntry.setIndexNames(
    (0, "QTECH-RSTP-MSTP-MIB", "qtechStpPortIfIndex"),
)
if mibBuilder.loadTexts:
    qtechStpExtPortEntry.setStatus("current")
_QtechStpPortIfIndex_Type = IfIndex
_QtechStpPortIfIndex_Object = MibTableColumn
qtechStpPortIfIndex = _QtechStpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 1, 3, 1, 1),
    _QtechStpPortIfIndex_Type()
)
qtechStpPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortIfIndex.setStatus("current")


class _QtechStpPortAdminPathCost_Type(Integer32):
    """Custom type qtechStpPortAdminPathCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_QtechStpPortAdminPathCost_Type.__name__ = "Integer32"
_QtechStpPortAdminPathCost_Object = MibTableColumn
qtechStpPortAdminPathCost = _QtechStpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 1, 3, 1, 2),
    _QtechStpPortAdminPathCost_Type()
)
qtechStpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpPortAdminPathCost.setStatus("current")


class _QtechStpPortOperPathCost_Type(Integer32):
    """Custom type qtechStpPortOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_QtechStpPortOperPathCost_Type.__name__ = "Integer32"
_QtechStpPortOperPathCost_Object = MibTableColumn
qtechStpPortOperPathCost = _QtechStpPortOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 1, 3, 1, 3),
    _QtechStpPortOperPathCost_Type()
)
qtechStpPortOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortOperPathCost.setStatus("current")


class _QtechStpPortRole_Type(Integer32):
    """Custom type qtechStpPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 1),
          ("alternatePort", 2),
          ("backupPort", 3),
          ("rootPort", 4),
          ("designatedPort", 5),
          ("masterPort", 6))
    )


_QtechStpPortRole_Type.__name__ = "Integer32"
_QtechStpPortRole_Object = MibTableColumn
qtechStpPortRole = _QtechStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 1, 3, 1, 4),
    _QtechStpPortRole_Type()
)
qtechStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortRole.setStatus("current")
_QtechRstpMIBObjects_ObjectIdentity = ObjectIdentity
qtechRstpMIBObjects = _QtechRstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2)
)


class _QtechStpVersion_Type(Integer32):
    """Custom type qtechStpVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2),
          ("mstp", 3))
    )


_QtechStpVersion_Type.__name__ = "Integer32"
_QtechStpVersion_Object = MibScalar
qtechStpVersion = _QtechStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 1),
    _QtechStpVersion_Type()
)
qtechStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpVersion.setStatus("current")


class _QtechStpTxHoldCount_Type(Integer32):
    """Custom type qtechStpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_QtechStpTxHoldCount_Type.__name__ = "Integer32"
_QtechStpTxHoldCount_Object = MibScalar
qtechStpTxHoldCount = _QtechStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 2),
    _QtechStpTxHoldCount_Type()
)
qtechStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpTxHoldCount.setStatus("current")


class _QtechStpPathCostDefault_Type(Integer32):
    """Custom type qtechStpPathCostDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_QtechStpPathCostDefault_Type.__name__ = "Integer32"
_QtechStpPathCostDefault_Object = MibScalar
qtechStpPathCostDefault = _QtechStpPathCostDefault_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 3),
    _QtechStpPathCostDefault_Type()
)
qtechStpPathCostDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpPathCostDefault.setStatus("current")
_QtechRstpExtPortTable_Object = MibTable
qtechRstpExtPortTable = _QtechRstpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4)
)
if mibBuilder.loadTexts:
    qtechRstpExtPortTable.setStatus("current")
_QtechRstpExtPortEntry_Object = MibTableRow
qtechRstpExtPortEntry = _QtechRstpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4, 1)
)
qtechRstpExtPortEntry.setIndexNames(
    (0, "QTECH-RSTP-MSTP-MIB", "qtechRstpExtPortIfIndex"),
)
if mibBuilder.loadTexts:
    qtechRstpExtPortEntry.setStatus("current")
_QtechRstpExtPortIfIndex_Type = IfIndex
_QtechRstpExtPortIfIndex_Object = MibTableColumn
qtechRstpExtPortIfIndex = _QtechRstpExtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4, 1, 1),
    _QtechRstpExtPortIfIndex_Type()
)
qtechRstpExtPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRstpExtPortIfIndex.setStatus("current")
_QtechStpPortProtocolMigration_Type = TruthValue
_QtechStpPortProtocolMigration_Object = MibTableColumn
qtechStpPortProtocolMigration = _QtechStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4, 1, 2),
    _QtechStpPortProtocolMigration_Type()
)
qtechStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpPortProtocolMigration.setStatus("current")
_QtechStpPortAdminEdgePort_Type = TruthValue
_QtechStpPortAdminEdgePort_Object = MibTableColumn
qtechStpPortAdminEdgePort = _QtechStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4, 1, 3),
    _QtechStpPortAdminEdgePort_Type()
)
qtechStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpPortAdminEdgePort.setStatus("current")
_QtechStpPortOperEdgePort_Type = TruthValue
_QtechStpPortOperEdgePort_Object = MibTableColumn
qtechStpPortOperEdgePort = _QtechStpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4, 1, 4),
    _QtechStpPortOperEdgePort_Type()
)
qtechStpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortOperEdgePort.setStatus("current")


class _QtechStpPortAdminPointToPoint_Type(Integer32):
    """Custom type qtechStpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_QtechStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_QtechStpPortAdminPointToPoint_Object = MibTableColumn
qtechStpPortAdminPointToPoint = _QtechStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4, 1, 5),
    _QtechStpPortAdminPointToPoint_Type()
)
qtechStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpPortAdminPointToPoint.setStatus("current")
_QtechStpPortOperPointToPoint_Type = TruthValue
_QtechStpPortOperPointToPoint_Object = MibTableColumn
qtechStpPortOperPointToPoint = _QtechStpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4, 1, 6),
    _QtechStpPortOperPointToPoint_Type()
)
qtechStpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortOperPointToPoint.setStatus("current")
_QtechStpPortBpduGuard_Type = EnabledStatus
_QtechStpPortBpduGuard_Object = MibTableColumn
qtechStpPortBpduGuard = _QtechStpPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4, 1, 7),
    _QtechStpPortBpduGuard_Type()
)
qtechStpPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpPortBpduGuard.setStatus("current")
_QtechStpPortBpduFilter_Type = EnabledStatus
_QtechStpPortBpduFilter_Object = MibTableColumn
qtechStpPortBpduFilter = _QtechStpPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 4, 1, 8),
    _QtechStpPortBpduFilter_Type()
)
qtechStpPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpPortBpduFilter.setStatus("current")
_QtechStpBpduGuard_Type = EnabledStatus
_QtechStpBpduGuard_Object = MibScalar
qtechStpBpduGuard = _QtechStpBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 5),
    _QtechStpBpduGuard_Type()
)
qtechStpBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpBpduGuard.setStatus("current")
_QtechStpBpduFilter_Type = EnabledStatus
_QtechStpBpduFilter_Object = MibScalar
qtechStpBpduFilter = _QtechStpBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 6),
    _QtechStpBpduFilter_Type()
)
qtechStpBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpBpduFilter.setStatus("current")
_QtechStpCistRegionRoot_Type = BridgeId
_QtechStpCistRegionRoot_Object = MibScalar
qtechStpCistRegionRoot = _QtechStpCistRegionRoot_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 7),
    _QtechStpCistRegionRoot_Type()
)
qtechStpCistRegionRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpCistRegionRoot.setStatus("current")
_QtechStpCistPathCost_Type = Integer32
_QtechStpCistPathCost_Object = MibScalar
qtechStpCistPathCost = _QtechStpCistPathCost_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 2, 8),
    _QtechStpCistPathCost_Type()
)
qtechStpCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpCistPathCost.setStatus("current")
_QtechMstpMIBObjects_ObjectIdentity = ObjectIdentity
qtechMstpMIBObjects = _QtechMstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3)
)
_QtechStpMstiMaxInstanceNumber_Type = Integer32
_QtechStpMstiMaxInstanceNumber_Object = MibScalar
qtechStpMstiMaxInstanceNumber = _QtechStpMstiMaxInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 1),
    _QtechStpMstiMaxInstanceNumber_Type()
)
qtechStpMstiMaxInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpMstiMaxInstanceNumber.setStatus("current")


class _QtechStpMstiRegionName_Type(DisplayString):
    """Custom type qtechStpMstiRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechStpMstiRegionName_Type.__name__ = "DisplayString"
_QtechStpMstiRegionName_Object = MibScalar
qtechStpMstiRegionName = _QtechStpMstiRegionName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 2),
    _QtechStpMstiRegionName_Type()
)
qtechStpMstiRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpMstiRegionName.setStatus("current")


class _QtechStpMstiRegionRevision_Type(Integer32):
    """Custom type qtechStpMstiRegionRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechStpMstiRegionRevision_Type.__name__ = "Integer32"
_QtechStpMstiRegionRevision_Object = MibScalar
qtechStpMstiRegionRevision = _QtechStpMstiRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 3),
    _QtechStpMstiRegionRevision_Type()
)
qtechStpMstiRegionRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpMstiRegionRevision.setStatus("current")


class _QtechStpMstiMaxHopNumber_Type(Integer32):
    """Custom type qtechStpMstiMaxHopNumber based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_QtechStpMstiMaxHopNumber_Type.__name__ = "Integer32"
_QtechStpMstiMaxHopNumber_Object = MibScalar
qtechStpMstiMaxHopNumber = _QtechStpMstiMaxHopNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 4),
    _QtechStpMstiMaxHopNumber_Type()
)
qtechStpMstiMaxHopNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpMstiMaxHopNumber.setStatus("current")
_QtechStpMstiInstanceTable_Object = MibTable
qtechStpMstiInstanceTable = _QtechStpMstiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5)
)
if mibBuilder.loadTexts:
    qtechStpMstiInstanceTable.setStatus("current")
_QtechStpMstiInstanceEntry_Object = MibTableRow
qtechStpMstiInstanceEntry = _QtechStpMstiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1)
)
qtechStpMstiInstanceEntry.setIndexNames(
    (0, "QTECH-RSTP-MSTP-MIB", "qtechStpMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    qtechStpMstiInstanceEntry.setStatus("current")


class _QtechStpMstiInstanceIndex_Type(Integer32):
    """Custom type qtechStpMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_QtechStpMstiInstanceIndex_Type.__name__ = "Integer32"
_QtechStpMstiInstanceIndex_Object = MibTableColumn
qtechStpMstiInstanceIndex = _QtechStpMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 1),
    _QtechStpMstiInstanceIndex_Type()
)
qtechStpMstiInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpMstiInstanceIndex.setStatus("current")


class _QtechStpMstiInstanceVlansAddMapped_Type(OctetString):
    """Custom type qtechStpMstiInstanceVlansAddMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_QtechStpMstiInstanceVlansAddMapped_Type.__name__ = "OctetString"
_QtechStpMstiInstanceVlansAddMapped_Object = MibTableColumn
qtechStpMstiInstanceVlansAddMapped = _QtechStpMstiInstanceVlansAddMapped_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 2),
    _QtechStpMstiInstanceVlansAddMapped_Type()
)
qtechStpMstiInstanceVlansAddMapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechStpMstiInstanceVlansAddMapped.setStatus("current")


class _QtechStpMstiInstanceVlansDeleteMapped_Type(OctetString):
    """Custom type qtechStpMstiInstanceVlansDeleteMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_QtechStpMstiInstanceVlansDeleteMapped_Type.__name__ = "OctetString"
_QtechStpMstiInstanceVlansDeleteMapped_Object = MibTableColumn
qtechStpMstiInstanceVlansDeleteMapped = _QtechStpMstiInstanceVlansDeleteMapped_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 3),
    _QtechStpMstiInstanceVlansDeleteMapped_Type()
)
qtechStpMstiInstanceVlansDeleteMapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechStpMstiInstanceVlansDeleteMapped.setStatus("current")


class _QtechStpMstiInstanceVlansGetMapped_Type(OctetString):
    """Custom type qtechStpMstiInstanceVlansGetMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_QtechStpMstiInstanceVlansGetMapped_Type.__name__ = "OctetString"
_QtechStpMstiInstanceVlansGetMapped_Object = MibTableColumn
qtechStpMstiInstanceVlansGetMapped = _QtechStpMstiInstanceVlansGetMapped_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 4),
    _QtechStpMstiInstanceVlansGetMapped_Type()
)
qtechStpMstiInstanceVlansGetMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpMstiInstanceVlansGetMapped.setStatus("current")


class _QtechStpMstiInstanceRemainingHopCount_Type(Integer32):
    """Custom type qtechStpMstiInstanceRemainingHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_QtechStpMstiInstanceRemainingHopCount_Type.__name__ = "Integer32"
_QtechStpMstiInstanceRemainingHopCount_Object = MibTableColumn
qtechStpMstiInstanceRemainingHopCount = _QtechStpMstiInstanceRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 5),
    _QtechStpMstiInstanceRemainingHopCount_Type()
)
qtechStpMstiInstanceRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpMstiInstanceRemainingHopCount.setStatus("current")


class _QtechStpMstiPriority_Type(Integer32):
    """Custom type qtechStpMstiPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechStpMstiPriority_Type.__name__ = "Integer32"
_QtechStpMstiPriority_Object = MibTableColumn
qtechStpMstiPriority = _QtechStpMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 6),
    _QtechStpMstiPriority_Type()
)
qtechStpMstiPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechStpMstiPriority.setStatus("current")
_QtechStpMstiTimeSinceTopologyChange_Type = TimeTicks
_QtechStpMstiTimeSinceTopologyChange_Object = MibTableColumn
qtechStpMstiTimeSinceTopologyChange = _QtechStpMstiTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 7),
    _QtechStpMstiTimeSinceTopologyChange_Type()
)
qtechStpMstiTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpMstiTimeSinceTopologyChange.setStatus("current")
_QtechStpMstiTopChanges_Type = Integer32
_QtechStpMstiTopChanges_Object = MibTableColumn
qtechStpMstiTopChanges = _QtechStpMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 8),
    _QtechStpMstiTopChanges_Type()
)
qtechStpMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpMstiTopChanges.setStatus("current")
_QtechStpMstiDesignatedRoot_Type = BridgeId
_QtechStpMstiDesignatedRoot_Object = MibTableColumn
qtechStpMstiDesignatedRoot = _QtechStpMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 9),
    _QtechStpMstiDesignatedRoot_Type()
)
qtechStpMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpMstiDesignatedRoot.setStatus("current")
_QtechStpMstiRootCost_Type = Integer32
_QtechStpMstiRootCost_Object = MibTableColumn
qtechStpMstiRootCost = _QtechStpMstiRootCost_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 10),
    _QtechStpMstiRootCost_Type()
)
qtechStpMstiRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpMstiRootCost.setStatus("current")
_QtechStpMstiRootPort_Type = Integer32
_QtechStpMstiRootPort_Object = MibTableColumn
qtechStpMstiRootPort = _QtechStpMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 11),
    _QtechStpMstiRootPort_Type()
)
qtechStpMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpMstiRootPort.setStatus("current")
_QtechStpMstiInstanceEntryStatus_Type = ConfigStatus
_QtechStpMstiInstanceEntryStatus_Object = MibTableColumn
qtechStpMstiInstanceEntryStatus = _QtechStpMstiInstanceEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 5, 1, 12),
    _QtechStpMstiInstanceEntryStatus_Type()
)
qtechStpMstiInstanceEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechStpMstiInstanceEntryStatus.setStatus("current")
_QtechStpPortMstiInstanceTable_Object = MibTable
qtechStpPortMstiInstanceTable = _QtechStpPortMstiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6)
)
if mibBuilder.loadTexts:
    qtechStpPortMstiInstanceTable.setStatus("current")
_QtechStpPortMstiInstanceEntry_Object = MibTableRow
qtechStpPortMstiInstanceEntry = _QtechStpPortMstiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1)
)
qtechStpPortMstiInstanceEntry.setIndexNames(
    (0, "QTECH-RSTP-MSTP-MIB", "qtechStpMstiInstanceIndex"),
    (0, "QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiIndex"),
)
if mibBuilder.loadTexts:
    qtechStpPortMstiInstanceEntry.setStatus("current")
_QtechStpPortMstiIndex_Type = Integer32
_QtechStpPortMstiIndex_Object = MibTableColumn
qtechStpPortMstiIndex = _QtechStpPortMstiIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 1),
    _QtechStpPortMstiIndex_Type()
)
qtechStpPortMstiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStpPortMstiIndex.setStatus("current")


class _QtechStpPortMstiState_Type(Integer32):
    """Custom type qtechStpPortMstiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6),
          ("discard", 7))
    )


_QtechStpPortMstiState_Type.__name__ = "Integer32"
_QtechStpPortMstiState_Object = MibTableColumn
qtechStpPortMstiState = _QtechStpPortMstiState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 2),
    _QtechStpPortMstiState_Type()
)
qtechStpPortMstiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortMstiState.setStatus("current")
_QtechStpPortMstiAdminPathCost_Type = Integer32
_QtechStpPortMstiAdminPathCost_Object = MibTableColumn
qtechStpPortMstiAdminPathCost = _QtechStpPortMstiAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 3),
    _QtechStpPortMstiAdminPathCost_Type()
)
qtechStpPortMstiAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpPortMstiAdminPathCost.setStatus("current")
_QtechStpPortMstiOperPathCost_Type = Counter32
_QtechStpPortMstiOperPathCost_Object = MibTableColumn
qtechStpPortMstiOperPathCost = _QtechStpPortMstiOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 4),
    _QtechStpPortMstiOperPathCost_Type()
)
qtechStpPortMstiOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortMstiOperPathCost.setStatus("current")


class _QtechStpPortMstiPriority_Type(Integer32):
    """Custom type qtechStpPortMstiPriority based on Integer32"""
    defaultValue = 128


_QtechStpPortMstiPriority_Type.__name__ = "Integer32"
_QtechStpPortMstiPriority_Object = MibTableColumn
qtechStpPortMstiPriority = _QtechStpPortMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 5),
    _QtechStpPortMstiPriority_Type()
)
qtechStpPortMstiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpPortMstiPriority.setStatus("current")
_QtechStpPortMstiDesignatedRoot_Type = BridgeId
_QtechStpPortMstiDesignatedRoot_Object = MibTableColumn
qtechStpPortMstiDesignatedRoot = _QtechStpPortMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 6),
    _QtechStpPortMstiDesignatedRoot_Type()
)
qtechStpPortMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortMstiDesignatedRoot.setStatus("current")
_QtechStpPortMstiDesignatedCost_Type = Integer32
_QtechStpPortMstiDesignatedCost_Object = MibTableColumn
qtechStpPortMstiDesignatedCost = _QtechStpPortMstiDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 7),
    _QtechStpPortMstiDesignatedCost_Type()
)
qtechStpPortMstiDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortMstiDesignatedCost.setStatus("current")
_QtechStpPortMstiDesignatedBridge_Type = BridgeId
_QtechStpPortMstiDesignatedBridge_Object = MibTableColumn
qtechStpPortMstiDesignatedBridge = _QtechStpPortMstiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 8),
    _QtechStpPortMstiDesignatedBridge_Type()
)
qtechStpPortMstiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortMstiDesignatedBridge.setStatus("current")


class _QtechStpPortMstiDesignatedPort_Type(OctetString):
    """Custom type qtechStpPortMstiDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_QtechStpPortMstiDesignatedPort_Type.__name__ = "OctetString"
_QtechStpPortMstiDesignatedPort_Object = MibTableColumn
qtechStpPortMstiDesignatedPort = _QtechStpPortMstiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 9),
    _QtechStpPortMstiDesignatedPort_Type()
)
qtechStpPortMstiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortMstiDesignatedPort.setStatus("current")


class _QtechStpPortMstiPortRole_Type(Integer32):
    """Custom type qtechStpPortMstiPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 1),
          ("alternatePort", 2),
          ("backupPort", 3),
          ("rootPort", 4),
          ("designatedPort", 5),
          ("masterPort", 6))
    )


_QtechStpPortMstiPortRole_Type.__name__ = "Integer32"
_QtechStpPortMstiPortRole_Object = MibTableColumn
qtechStpPortMstiPortRole = _QtechStpPortMstiPortRole_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 10),
    _QtechStpPortMstiPortRole_Type()
)
qtechStpPortMstiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortMstiPortRole.setStatus("current")
_QtechStpPortMstiPortForwardTransitions_Type = Integer32
_QtechStpPortMstiPortForwardTransitions_Object = MibTableColumn
qtechStpPortMstiPortForwardTransitions = _QtechStpPortMstiPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 6, 1, 11),
    _QtechStpPortMstiPortForwardTransitions_Type()
)
qtechStpPortMstiPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpPortMstiPortForwardTransitions.setStatus("current")
_QtechStpMstiReset_Type = Integer32
_QtechStpMstiReset_Object = MibScalar
qtechStpMstiReset = _QtechStpMstiReset_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 7),
    _QtechStpMstiReset_Type()
)
qtechStpMstiReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpMstiReset.setStatus("current")
_QtechStpCistVlansAddMapped_Type = OctetString
_QtechStpCistVlansAddMapped_Object = MibScalar
qtechStpCistVlansAddMapped = _QtechStpCistVlansAddMapped_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 8),
    _QtechStpCistVlansAddMapped_Type()
)
qtechStpCistVlansAddMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechStpCistVlansAddMapped.setStatus("current")
_QtechStpCistVlansGetMapped_Type = OctetString
_QtechStpCistVlansGetMapped_Object = MibScalar
qtechStpCistVlansGetMapped = _QtechStpCistVlansGetMapped_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 9),
    _QtechStpCistVlansGetMapped_Type()
)
qtechStpCistVlansGetMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpCistVlansGetMapped.setStatus("current")
_QtechStpCistRemainingHopCount_Type = Integer32
_QtechStpCistRemainingHopCount_Object = MibScalar
qtechStpCistRemainingHopCount = _QtechStpCistRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 3, 10),
    _QtechStpCistRemainingHopCount_Type()
)
qtechStpCistRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStpCistRemainingHopCount.setStatus("current")
_StpExternConformance_ObjectIdentity = ObjectIdentity
stpExternConformance = _StpExternConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 4)
)
_StpExternGroups_ObjectIdentity = ObjectIdentity
stpExternGroups = _StpExternGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 4, 1)
)
_RstpConformance_ObjectIdentity = ObjectIdentity
rstpConformance = _RstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 5)
)
_RstpGroups_ObjectIdentity = ObjectIdentity
rstpGroups = _RstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 5, 1)
)
_RstpCompliances_ObjectIdentity = ObjectIdentity
rstpCompliances = _RstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 5, 2)
)
_MstpConformance_ObjectIdentity = ObjectIdentity
mstpConformance = _MstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 6)
)
_MstpGroups_ObjectIdentity = ObjectIdentity
mstpGroups = _MstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 6, 1)
)
_MstpCompliances_ObjectIdentity = ObjectIdentity
mstpCompliances = _MstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 6, 2)
)

# Managed Objects groups

stpExternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 4, 1, 1)
)
stpExternGroup.setObjects(
      *(("QTECH-RSTP-MSTP-MIB", "qtechSysStpStatus"),
        ("QTECH-RSTP-MSTP-MIB", "qtechSysStpReset"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortIfIndex"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortAdminPathCost"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortOperPathCost"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortRole"))
)
if mibBuilder.loadTexts:
    stpExternGroup.setStatus("current")

rstpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 5, 1, 1)
)
rstpBridgeGroup.setObjects(
      *(("QTECH-RSTP-MSTP-MIB", "qtechStpVersion"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpTxHoldCount"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpBpduGuard"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpBpduFilter"))
)
if mibBuilder.loadTexts:
    rstpBridgeGroup.setStatus("current")

rstpDefaultPathCostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 5, 1, 2)
)
rstpDefaultPathCostGroup.setObjects(
    ("QTECH-RSTP-MSTP-MIB", "qtechStpPathCostDefault")
)
if mibBuilder.loadTexts:
    rstpDefaultPathCostGroup.setStatus("current")

rstpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 5, 1, 3)
)
rstpPortGroup.setObjects(
      *(("QTECH-RSTP-MSTP-MIB", "qtechRstpExtPortIfIndex"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortProtocolMigration"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortAdminEdgePort"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortOperEdgePort"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortAdminPointToPoint"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortOperPointToPoint"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortBpduGuard"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortBpduFilter"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpCistRegionRoot"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpCistPathCost"))
)
if mibBuilder.loadTexts:
    rstpPortGroup.setStatus("current")

mstpBridgeRegionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 6, 1, 1)
)
mstpBridgeRegionGroup.setObjects(
      *(("QTECH-RSTP-MSTP-MIB", "qtechStpMstiMaxInstanceNumber"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiRegionName"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiRegionRevision"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiMaxHopNumber"))
)
if mibBuilder.loadTexts:
    mstpBridgeRegionGroup.setStatus("current")

mstpMstiBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 6, 1, 2)
)
mstpMstiBridgeGroup.setObjects(
      *(("QTECH-RSTP-MSTP-MIB", "qtechStpMstiInstanceIndex"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiInstanceVlansAddMapped"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiInstanceVlansDeleteMapped"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiInstanceVlansGetMapped"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiInstanceRemainingHopCount"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiPriority"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiTimeSinceTopologyChange"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiTopChanges"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiDesignatedRoot"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiRootCost"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiRootPort"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpMstiInstanceEntryStatus"))
)
if mibBuilder.loadTexts:
    mstpMstiBridgeGroup.setStatus("current")

mstpMstiPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 6, 1, 3)
)
mstpMstiPortGroup.setObjects(
      *(("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiState"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiAdminPathCost"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiOperPathCost"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiPriority"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiDesignatedRoot"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiDesignatedCost"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiDesignatedBridge"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiDesignatedPort"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiPortRole"),
        ("QTECH-RSTP-MSTP-MIB", "qtechStpPortMstiPortForwardTransitions"))
)
if mibBuilder.loadTexts:
    mstpMstiPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 5, 2, 1)
)
rstpCompliance.setObjects(
      *(("QTECH-RSTP-MSTP-MIB", "rstpBridgeGroup"),
        ("QTECH-RSTP-MSTP-MIB", "rstpDefaultPathCostGroup"),
        ("QTECH-RSTP-MSTP-MIB", "rstpPortGroup"),
        ("QTECH-RSTP-MSTP-MIB", "rstpDefaultPathCostGroup"))
)
if mibBuilder.loadTexts:
    rstpCompliance.setStatus(
        "current"
    )

mstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 16, 6, 2, 1)
)
mstpCompliance.setObjects(
      *(("QTECH-RSTP-MSTP-MIB", "mstpBridgeRegionGroup"),
        ("QTECH-RSTP-MSTP-MIB", "mstpMstiBridgeGroup"),
        ("QTECH-RSTP-MSTP-MIB", "mstpMstiPortGroup"))
)
if mibBuilder.loadTexts:
    mstpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-RSTP-MSTP-MIB",
    **{"qtechStpMIB": qtechStpMIB,
       "qtechStpMIBObjects": qtechStpMIBObjects,
       "qtechSysStpStatus": qtechSysStpStatus,
       "qtechSysStpReset": qtechSysStpReset,
       "qtechStpExtPortTable": qtechStpExtPortTable,
       "qtechStpExtPortEntry": qtechStpExtPortEntry,
       "qtechStpPortIfIndex": qtechStpPortIfIndex,
       "qtechStpPortAdminPathCost": qtechStpPortAdminPathCost,
       "qtechStpPortOperPathCost": qtechStpPortOperPathCost,
       "qtechStpPortRole": qtechStpPortRole,
       "qtechRstpMIBObjects": qtechRstpMIBObjects,
       "qtechStpVersion": qtechStpVersion,
       "qtechStpTxHoldCount": qtechStpTxHoldCount,
       "qtechStpPathCostDefault": qtechStpPathCostDefault,
       "qtechRstpExtPortTable": qtechRstpExtPortTable,
       "qtechRstpExtPortEntry": qtechRstpExtPortEntry,
       "qtechRstpExtPortIfIndex": qtechRstpExtPortIfIndex,
       "qtechStpPortProtocolMigration": qtechStpPortProtocolMigration,
       "qtechStpPortAdminEdgePort": qtechStpPortAdminEdgePort,
       "qtechStpPortOperEdgePort": qtechStpPortOperEdgePort,
       "qtechStpPortAdminPointToPoint": qtechStpPortAdminPointToPoint,
       "qtechStpPortOperPointToPoint": qtechStpPortOperPointToPoint,
       "qtechStpPortBpduGuard": qtechStpPortBpduGuard,
       "qtechStpPortBpduFilter": qtechStpPortBpduFilter,
       "qtechStpBpduGuard": qtechStpBpduGuard,
       "qtechStpBpduFilter": qtechStpBpduFilter,
       "qtechStpCistRegionRoot": qtechStpCistRegionRoot,
       "qtechStpCistPathCost": qtechStpCistPathCost,
       "qtechMstpMIBObjects": qtechMstpMIBObjects,
       "qtechStpMstiMaxInstanceNumber": qtechStpMstiMaxInstanceNumber,
       "qtechStpMstiRegionName": qtechStpMstiRegionName,
       "qtechStpMstiRegionRevision": qtechStpMstiRegionRevision,
       "qtechStpMstiMaxHopNumber": qtechStpMstiMaxHopNumber,
       "qtechStpMstiInstanceTable": qtechStpMstiInstanceTable,
       "qtechStpMstiInstanceEntry": qtechStpMstiInstanceEntry,
       "qtechStpMstiInstanceIndex": qtechStpMstiInstanceIndex,
       "qtechStpMstiInstanceVlansAddMapped": qtechStpMstiInstanceVlansAddMapped,
       "qtechStpMstiInstanceVlansDeleteMapped": qtechStpMstiInstanceVlansDeleteMapped,
       "qtechStpMstiInstanceVlansGetMapped": qtechStpMstiInstanceVlansGetMapped,
       "qtechStpMstiInstanceRemainingHopCount": qtechStpMstiInstanceRemainingHopCount,
       "qtechStpMstiPriority": qtechStpMstiPriority,
       "qtechStpMstiTimeSinceTopologyChange": qtechStpMstiTimeSinceTopologyChange,
       "qtechStpMstiTopChanges": qtechStpMstiTopChanges,
       "qtechStpMstiDesignatedRoot": qtechStpMstiDesignatedRoot,
       "qtechStpMstiRootCost": qtechStpMstiRootCost,
       "qtechStpMstiRootPort": qtechStpMstiRootPort,
       "qtechStpMstiInstanceEntryStatus": qtechStpMstiInstanceEntryStatus,
       "qtechStpPortMstiInstanceTable": qtechStpPortMstiInstanceTable,
       "qtechStpPortMstiInstanceEntry": qtechStpPortMstiInstanceEntry,
       "qtechStpPortMstiIndex": qtechStpPortMstiIndex,
       "qtechStpPortMstiState": qtechStpPortMstiState,
       "qtechStpPortMstiAdminPathCost": qtechStpPortMstiAdminPathCost,
       "qtechStpPortMstiOperPathCost": qtechStpPortMstiOperPathCost,
       "qtechStpPortMstiPriority": qtechStpPortMstiPriority,
       "qtechStpPortMstiDesignatedRoot": qtechStpPortMstiDesignatedRoot,
       "qtechStpPortMstiDesignatedCost": qtechStpPortMstiDesignatedCost,
       "qtechStpPortMstiDesignatedBridge": qtechStpPortMstiDesignatedBridge,
       "qtechStpPortMstiDesignatedPort": qtechStpPortMstiDesignatedPort,
       "qtechStpPortMstiPortRole": qtechStpPortMstiPortRole,
       "qtechStpPortMstiPortForwardTransitions": qtechStpPortMstiPortForwardTransitions,
       "qtechStpMstiReset": qtechStpMstiReset,
       "qtechStpCistVlansAddMapped": qtechStpCistVlansAddMapped,
       "qtechStpCistVlansGetMapped": qtechStpCistVlansGetMapped,
       "qtechStpCistRemainingHopCount": qtechStpCistRemainingHopCount,
       "stpExternConformance": stpExternConformance,
       "stpExternGroups": stpExternGroups,
       "stpExternGroup": stpExternGroup,
       "rstpConformance": rstpConformance,
       "rstpGroups": rstpGroups,
       "rstpBridgeGroup": rstpBridgeGroup,
       "rstpDefaultPathCostGroup": rstpDefaultPathCostGroup,
       "rstpPortGroup": rstpPortGroup,
       "rstpCompliances": rstpCompliances,
       "rstpCompliance": rstpCompliance,
       "mstpConformance": mstpConformance,
       "mstpGroups": mstpGroups,
       "mstpBridgeRegionGroup": mstpBridgeRegionGroup,
       "mstpMstiBridgeGroup": mstpMstiBridgeGroup,
       "mstpMstiPortGroup": mstpMstiPortGroup,
       "mstpCompliances": mstpCompliances,
       "mstpCompliance": mstpCompliance}
)
