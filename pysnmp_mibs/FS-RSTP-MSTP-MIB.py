# SNMP MIB module (FS-RSTP-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-RSTP-MSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:19 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsStpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16)
)
if mibBuilder.loadTexts:
    fsStpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsStpMIBObjects_ObjectIdentity = ObjectIdentity
fsStpMIBObjects = _FsStpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 1)
)


class _FsSysStpStatus_Type(EnabledStatus):
    """Custom type fsSysStpStatus based on EnabledStatus"""
    defaultValue = 2


_FsSysStpStatus_Type.__name__ = "EnabledStatus"
_FsSysStpStatus_Object = MibScalar
fsSysStpStatus = _FsSysStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 1, 1),
    _FsSysStpStatus_Type()
)
fsSysStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSysStpStatus.setStatus("current")
_FsSysStpReset_Type = Integer32
_FsSysStpReset_Object = MibScalar
fsSysStpReset = _FsSysStpReset_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 1, 2),
    _FsSysStpReset_Type()
)
fsSysStpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSysStpReset.setStatus("current")
_FsStpExtPortTable_Object = MibTable
fsStpExtPortTable = _FsStpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 1, 3)
)
if mibBuilder.loadTexts:
    fsStpExtPortTable.setStatus("current")
_FsStpExtPortEntry_Object = MibTableRow
fsStpExtPortEntry = _FsStpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 1, 3, 1)
)
fsStpExtPortEntry.setIndexNames(
    (0, "FS-RSTP-MSTP-MIB", "fsStpPortIfIndex"),
)
if mibBuilder.loadTexts:
    fsStpExtPortEntry.setStatus("current")
_FsStpPortIfIndex_Type = IfIndex
_FsStpPortIfIndex_Object = MibTableColumn
fsStpPortIfIndex = _FsStpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 1, 3, 1, 1),
    _FsStpPortIfIndex_Type()
)
fsStpPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortIfIndex.setStatus("current")


class _FsStpPortAdminPathCost_Type(Integer32):
    """Custom type fsStpPortAdminPathCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_FsStpPortAdminPathCost_Type.__name__ = "Integer32"
_FsStpPortAdminPathCost_Object = MibTableColumn
fsStpPortAdminPathCost = _FsStpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 1, 3, 1, 2),
    _FsStpPortAdminPathCost_Type()
)
fsStpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpPortAdminPathCost.setStatus("current")


class _FsStpPortOperPathCost_Type(Integer32):
    """Custom type fsStpPortOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_FsStpPortOperPathCost_Type.__name__ = "Integer32"
_FsStpPortOperPathCost_Object = MibTableColumn
fsStpPortOperPathCost = _FsStpPortOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 1, 3, 1, 3),
    _FsStpPortOperPathCost_Type()
)
fsStpPortOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortOperPathCost.setStatus("current")


class _FsStpPortRole_Type(Integer32):
    """Custom type fsStpPortRole based on Integer32"""
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


_FsStpPortRole_Type.__name__ = "Integer32"
_FsStpPortRole_Object = MibTableColumn
fsStpPortRole = _FsStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 1, 3, 1, 4),
    _FsStpPortRole_Type()
)
fsStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortRole.setStatus("current")
_FsRstpMIBObjects_ObjectIdentity = ObjectIdentity
fsRstpMIBObjects = _FsRstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2)
)


class _FsStpVersion_Type(Integer32):
    """Custom type fsStpVersion based on Integer32"""
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


_FsStpVersion_Type.__name__ = "Integer32"
_FsStpVersion_Object = MibScalar
fsStpVersion = _FsStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 1),
    _FsStpVersion_Type()
)
fsStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpVersion.setStatus("current")


class _FsStpTxHoldCount_Type(Integer32):
    """Custom type fsStpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsStpTxHoldCount_Type.__name__ = "Integer32"
_FsStpTxHoldCount_Object = MibScalar
fsStpTxHoldCount = _FsStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 2),
    _FsStpTxHoldCount_Type()
)
fsStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpTxHoldCount.setStatus("current")


class _FsStpPathCostDefault_Type(Integer32):
    """Custom type fsStpPathCostDefault based on Integer32"""
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


_FsStpPathCostDefault_Type.__name__ = "Integer32"
_FsStpPathCostDefault_Object = MibScalar
fsStpPathCostDefault = _FsStpPathCostDefault_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 3),
    _FsStpPathCostDefault_Type()
)
fsStpPathCostDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpPathCostDefault.setStatus("current")
_FsRstpExtPortTable_Object = MibTable
fsRstpExtPortTable = _FsRstpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4)
)
if mibBuilder.loadTexts:
    fsRstpExtPortTable.setStatus("current")
_FsRstpExtPortEntry_Object = MibTableRow
fsRstpExtPortEntry = _FsRstpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4, 1)
)
fsRstpExtPortEntry.setIndexNames(
    (0, "FS-RSTP-MSTP-MIB", "fsRstpExtPortIfIndex"),
)
if mibBuilder.loadTexts:
    fsRstpExtPortEntry.setStatus("current")
_FsRstpExtPortIfIndex_Type = IfIndex
_FsRstpExtPortIfIndex_Object = MibTableColumn
fsRstpExtPortIfIndex = _FsRstpExtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4, 1, 1),
    _FsRstpExtPortIfIndex_Type()
)
fsRstpExtPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRstpExtPortIfIndex.setStatus("current")
_FsStpPortProtocolMigration_Type = TruthValue
_FsStpPortProtocolMigration_Object = MibTableColumn
fsStpPortProtocolMigration = _FsStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4, 1, 2),
    _FsStpPortProtocolMigration_Type()
)
fsStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpPortProtocolMigration.setStatus("current")
_FsStpPortAdminEdgePort_Type = TruthValue
_FsStpPortAdminEdgePort_Object = MibTableColumn
fsStpPortAdminEdgePort = _FsStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4, 1, 3),
    _FsStpPortAdminEdgePort_Type()
)
fsStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpPortAdminEdgePort.setStatus("current")
_FsStpPortOperEdgePort_Type = TruthValue
_FsStpPortOperEdgePort_Object = MibTableColumn
fsStpPortOperEdgePort = _FsStpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4, 1, 4),
    _FsStpPortOperEdgePort_Type()
)
fsStpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortOperEdgePort.setStatus("current")


class _FsStpPortAdminPointToPoint_Type(Integer32):
    """Custom type fsStpPortAdminPointToPoint based on Integer32"""
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


_FsStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_FsStpPortAdminPointToPoint_Object = MibTableColumn
fsStpPortAdminPointToPoint = _FsStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4, 1, 5),
    _FsStpPortAdminPointToPoint_Type()
)
fsStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpPortAdminPointToPoint.setStatus("current")
_FsStpPortOperPointToPoint_Type = TruthValue
_FsStpPortOperPointToPoint_Object = MibTableColumn
fsStpPortOperPointToPoint = _FsStpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4, 1, 6),
    _FsStpPortOperPointToPoint_Type()
)
fsStpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortOperPointToPoint.setStatus("current")
_FsStpPortBpduGuard_Type = EnabledStatus
_FsStpPortBpduGuard_Object = MibTableColumn
fsStpPortBpduGuard = _FsStpPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4, 1, 7),
    _FsStpPortBpduGuard_Type()
)
fsStpPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpPortBpduGuard.setStatus("current")
_FsStpPortBpduFilter_Type = EnabledStatus
_FsStpPortBpduFilter_Object = MibTableColumn
fsStpPortBpduFilter = _FsStpPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 4, 1, 8),
    _FsStpPortBpduFilter_Type()
)
fsStpPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpPortBpduFilter.setStatus("current")
_FsStpBpduGuard_Type = EnabledStatus
_FsStpBpduGuard_Object = MibScalar
fsStpBpduGuard = _FsStpBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 5),
    _FsStpBpduGuard_Type()
)
fsStpBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpBpduGuard.setStatus("current")
_FsStpBpduFilter_Type = EnabledStatus
_FsStpBpduFilter_Object = MibScalar
fsStpBpduFilter = _FsStpBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 6),
    _FsStpBpduFilter_Type()
)
fsStpBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpBpduFilter.setStatus("current")
_FsStpCistRegionRoot_Type = BridgeId
_FsStpCistRegionRoot_Object = MibScalar
fsStpCistRegionRoot = _FsStpCistRegionRoot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 7),
    _FsStpCistRegionRoot_Type()
)
fsStpCistRegionRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpCistRegionRoot.setStatus("current")
_FsStpCistPathCost_Type = Integer32
_FsStpCistPathCost_Object = MibScalar
fsStpCistPathCost = _FsStpCistPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 2, 8),
    _FsStpCistPathCost_Type()
)
fsStpCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpCistPathCost.setStatus("current")
_FsMstpMIBObjects_ObjectIdentity = ObjectIdentity
fsMstpMIBObjects = _FsMstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3)
)
_FsStpMstiMaxInstanceNumber_Type = Integer32
_FsStpMstiMaxInstanceNumber_Object = MibScalar
fsStpMstiMaxInstanceNumber = _FsStpMstiMaxInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 1),
    _FsStpMstiMaxInstanceNumber_Type()
)
fsStpMstiMaxInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpMstiMaxInstanceNumber.setStatus("current")


class _FsStpMstiRegionName_Type(DisplayString):
    """Custom type fsStpMstiRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsStpMstiRegionName_Type.__name__ = "DisplayString"
_FsStpMstiRegionName_Object = MibScalar
fsStpMstiRegionName = _FsStpMstiRegionName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 2),
    _FsStpMstiRegionName_Type()
)
fsStpMstiRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpMstiRegionName.setStatus("current")


class _FsStpMstiRegionRevision_Type(Integer32):
    """Custom type fsStpMstiRegionRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsStpMstiRegionRevision_Type.__name__ = "Integer32"
_FsStpMstiRegionRevision_Object = MibScalar
fsStpMstiRegionRevision = _FsStpMstiRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 3),
    _FsStpMstiRegionRevision_Type()
)
fsStpMstiRegionRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpMstiRegionRevision.setStatus("current")


class _FsStpMstiMaxHopNumber_Type(Integer32):
    """Custom type fsStpMstiMaxHopNumber based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_FsStpMstiMaxHopNumber_Type.__name__ = "Integer32"
_FsStpMstiMaxHopNumber_Object = MibScalar
fsStpMstiMaxHopNumber = _FsStpMstiMaxHopNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 4),
    _FsStpMstiMaxHopNumber_Type()
)
fsStpMstiMaxHopNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpMstiMaxHopNumber.setStatus("current")
_FsStpMstiInstanceTable_Object = MibTable
fsStpMstiInstanceTable = _FsStpMstiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5)
)
if mibBuilder.loadTexts:
    fsStpMstiInstanceTable.setStatus("current")
_FsStpMstiInstanceEntry_Object = MibTableRow
fsStpMstiInstanceEntry = _FsStpMstiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1)
)
fsStpMstiInstanceEntry.setIndexNames(
    (0, "FS-RSTP-MSTP-MIB", "fsStpMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    fsStpMstiInstanceEntry.setStatus("current")


class _FsStpMstiInstanceIndex_Type(Integer32):
    """Custom type fsStpMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FsStpMstiInstanceIndex_Type.__name__ = "Integer32"
_FsStpMstiInstanceIndex_Object = MibTableColumn
fsStpMstiInstanceIndex = _FsStpMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 1),
    _FsStpMstiInstanceIndex_Type()
)
fsStpMstiInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpMstiInstanceIndex.setStatus("current")


class _FsStpMstiInstanceVlansAddMapped_Type(OctetString):
    """Custom type fsStpMstiInstanceVlansAddMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_FsStpMstiInstanceVlansAddMapped_Type.__name__ = "OctetString"
_FsStpMstiInstanceVlansAddMapped_Object = MibTableColumn
fsStpMstiInstanceVlansAddMapped = _FsStpMstiInstanceVlansAddMapped_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 2),
    _FsStpMstiInstanceVlansAddMapped_Type()
)
fsStpMstiInstanceVlansAddMapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsStpMstiInstanceVlansAddMapped.setStatus("current")


class _FsStpMstiInstanceVlansDeleteMapped_Type(OctetString):
    """Custom type fsStpMstiInstanceVlansDeleteMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_FsStpMstiInstanceVlansDeleteMapped_Type.__name__ = "OctetString"
_FsStpMstiInstanceVlansDeleteMapped_Object = MibTableColumn
fsStpMstiInstanceVlansDeleteMapped = _FsStpMstiInstanceVlansDeleteMapped_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 3),
    _FsStpMstiInstanceVlansDeleteMapped_Type()
)
fsStpMstiInstanceVlansDeleteMapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsStpMstiInstanceVlansDeleteMapped.setStatus("current")


class _FsStpMstiInstanceVlansGetMapped_Type(OctetString):
    """Custom type fsStpMstiInstanceVlansGetMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_FsStpMstiInstanceVlansGetMapped_Type.__name__ = "OctetString"
_FsStpMstiInstanceVlansGetMapped_Object = MibTableColumn
fsStpMstiInstanceVlansGetMapped = _FsStpMstiInstanceVlansGetMapped_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 4),
    _FsStpMstiInstanceVlansGetMapped_Type()
)
fsStpMstiInstanceVlansGetMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpMstiInstanceVlansGetMapped.setStatus("current")


class _FsStpMstiInstanceRemainingHopCount_Type(Integer32):
    """Custom type fsStpMstiInstanceRemainingHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_FsStpMstiInstanceRemainingHopCount_Type.__name__ = "Integer32"
_FsStpMstiInstanceRemainingHopCount_Object = MibTableColumn
fsStpMstiInstanceRemainingHopCount = _FsStpMstiInstanceRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 5),
    _FsStpMstiInstanceRemainingHopCount_Type()
)
fsStpMstiInstanceRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpMstiInstanceRemainingHopCount.setStatus("current")


class _FsStpMstiPriority_Type(Integer32):
    """Custom type fsStpMstiPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsStpMstiPriority_Type.__name__ = "Integer32"
_FsStpMstiPriority_Object = MibTableColumn
fsStpMstiPriority = _FsStpMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 6),
    _FsStpMstiPriority_Type()
)
fsStpMstiPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsStpMstiPriority.setStatus("current")
_FsStpMstiTimeSinceTopologyChange_Type = TimeTicks
_FsStpMstiTimeSinceTopologyChange_Object = MibTableColumn
fsStpMstiTimeSinceTopologyChange = _FsStpMstiTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 7),
    _FsStpMstiTimeSinceTopologyChange_Type()
)
fsStpMstiTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpMstiTimeSinceTopologyChange.setStatus("current")
_FsStpMstiTopChanges_Type = Integer32
_FsStpMstiTopChanges_Object = MibTableColumn
fsStpMstiTopChanges = _FsStpMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 8),
    _FsStpMstiTopChanges_Type()
)
fsStpMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpMstiTopChanges.setStatus("current")
_FsStpMstiDesignatedRoot_Type = BridgeId
_FsStpMstiDesignatedRoot_Object = MibTableColumn
fsStpMstiDesignatedRoot = _FsStpMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 9),
    _FsStpMstiDesignatedRoot_Type()
)
fsStpMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpMstiDesignatedRoot.setStatus("current")
_FsStpMstiRootCost_Type = Integer32
_FsStpMstiRootCost_Object = MibTableColumn
fsStpMstiRootCost = _FsStpMstiRootCost_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 10),
    _FsStpMstiRootCost_Type()
)
fsStpMstiRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpMstiRootCost.setStatus("current")
_FsStpMstiRootPort_Type = Integer32
_FsStpMstiRootPort_Object = MibTableColumn
fsStpMstiRootPort = _FsStpMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 11),
    _FsStpMstiRootPort_Type()
)
fsStpMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpMstiRootPort.setStatus("current")
_FsStpMstiInstanceEntryStatus_Type = ConfigStatus
_FsStpMstiInstanceEntryStatus_Object = MibTableColumn
fsStpMstiInstanceEntryStatus = _FsStpMstiInstanceEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 5, 1, 12),
    _FsStpMstiInstanceEntryStatus_Type()
)
fsStpMstiInstanceEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsStpMstiInstanceEntryStatus.setStatus("current")
_FsStpPortMstiInstanceTable_Object = MibTable
fsStpPortMstiInstanceTable = _FsStpPortMstiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6)
)
if mibBuilder.loadTexts:
    fsStpPortMstiInstanceTable.setStatus("current")
_FsStpPortMstiInstanceEntry_Object = MibTableRow
fsStpPortMstiInstanceEntry = _FsStpPortMstiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1)
)
fsStpPortMstiInstanceEntry.setIndexNames(
    (0, "FS-RSTP-MSTP-MIB", "fsStpMstiInstanceIndex"),
    (0, "FS-RSTP-MSTP-MIB", "fsStpPortMstiIndex"),
)
if mibBuilder.loadTexts:
    fsStpPortMstiInstanceEntry.setStatus("current")
_FsStpPortMstiIndex_Type = Integer32
_FsStpPortMstiIndex_Object = MibTableColumn
fsStpPortMstiIndex = _FsStpPortMstiIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 1),
    _FsStpPortMstiIndex_Type()
)
fsStpPortMstiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStpPortMstiIndex.setStatus("current")


class _FsStpPortMstiState_Type(Integer32):
    """Custom type fsStpPortMstiState based on Integer32"""
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


_FsStpPortMstiState_Type.__name__ = "Integer32"
_FsStpPortMstiState_Object = MibTableColumn
fsStpPortMstiState = _FsStpPortMstiState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 2),
    _FsStpPortMstiState_Type()
)
fsStpPortMstiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortMstiState.setStatus("current")
_FsStpPortMstiAdminPathCost_Type = Integer32
_FsStpPortMstiAdminPathCost_Object = MibTableColumn
fsStpPortMstiAdminPathCost = _FsStpPortMstiAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 3),
    _FsStpPortMstiAdminPathCost_Type()
)
fsStpPortMstiAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpPortMstiAdminPathCost.setStatus("current")
_FsStpPortMstiOperPathCost_Type = Counter32
_FsStpPortMstiOperPathCost_Object = MibTableColumn
fsStpPortMstiOperPathCost = _FsStpPortMstiOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 4),
    _FsStpPortMstiOperPathCost_Type()
)
fsStpPortMstiOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortMstiOperPathCost.setStatus("current")


class _FsStpPortMstiPriority_Type(Integer32):
    """Custom type fsStpPortMstiPriority based on Integer32"""
    defaultValue = 128


_FsStpPortMstiPriority_Type.__name__ = "Integer32"
_FsStpPortMstiPriority_Object = MibTableColumn
fsStpPortMstiPriority = _FsStpPortMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 5),
    _FsStpPortMstiPriority_Type()
)
fsStpPortMstiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpPortMstiPriority.setStatus("current")
_FsStpPortMstiDesignatedRoot_Type = BridgeId
_FsStpPortMstiDesignatedRoot_Object = MibTableColumn
fsStpPortMstiDesignatedRoot = _FsStpPortMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 6),
    _FsStpPortMstiDesignatedRoot_Type()
)
fsStpPortMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortMstiDesignatedRoot.setStatus("current")
_FsStpPortMstiDesignatedCost_Type = Integer32
_FsStpPortMstiDesignatedCost_Object = MibTableColumn
fsStpPortMstiDesignatedCost = _FsStpPortMstiDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 7),
    _FsStpPortMstiDesignatedCost_Type()
)
fsStpPortMstiDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortMstiDesignatedCost.setStatus("current")
_FsStpPortMstiDesignatedBridge_Type = BridgeId
_FsStpPortMstiDesignatedBridge_Object = MibTableColumn
fsStpPortMstiDesignatedBridge = _FsStpPortMstiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 8),
    _FsStpPortMstiDesignatedBridge_Type()
)
fsStpPortMstiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortMstiDesignatedBridge.setStatus("current")


class _FsStpPortMstiDesignatedPort_Type(OctetString):
    """Custom type fsStpPortMstiDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsStpPortMstiDesignatedPort_Type.__name__ = "OctetString"
_FsStpPortMstiDesignatedPort_Object = MibTableColumn
fsStpPortMstiDesignatedPort = _FsStpPortMstiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 9),
    _FsStpPortMstiDesignatedPort_Type()
)
fsStpPortMstiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortMstiDesignatedPort.setStatus("current")


class _FsStpPortMstiPortRole_Type(Integer32):
    """Custom type fsStpPortMstiPortRole based on Integer32"""
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


_FsStpPortMstiPortRole_Type.__name__ = "Integer32"
_FsStpPortMstiPortRole_Object = MibTableColumn
fsStpPortMstiPortRole = _FsStpPortMstiPortRole_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 10),
    _FsStpPortMstiPortRole_Type()
)
fsStpPortMstiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortMstiPortRole.setStatus("current")
_FsStpPortMstiPortForwardTransitions_Type = Integer32
_FsStpPortMstiPortForwardTransitions_Object = MibTableColumn
fsStpPortMstiPortForwardTransitions = _FsStpPortMstiPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 6, 1, 11),
    _FsStpPortMstiPortForwardTransitions_Type()
)
fsStpPortMstiPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpPortMstiPortForwardTransitions.setStatus("current")
_FsStpMstiReset_Type = Integer32
_FsStpMstiReset_Object = MibScalar
fsStpMstiReset = _FsStpMstiReset_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 7),
    _FsStpMstiReset_Type()
)
fsStpMstiReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpMstiReset.setStatus("current")
_FsStpCistVlansAddMapped_Type = OctetString
_FsStpCistVlansAddMapped_Object = MibScalar
fsStpCistVlansAddMapped = _FsStpCistVlansAddMapped_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 8),
    _FsStpCistVlansAddMapped_Type()
)
fsStpCistVlansAddMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStpCistVlansAddMapped.setStatus("current")
_FsStpCistVlansGetMapped_Type = OctetString
_FsStpCistVlansGetMapped_Object = MibScalar
fsStpCistVlansGetMapped = _FsStpCistVlansGetMapped_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 9),
    _FsStpCistVlansGetMapped_Type()
)
fsStpCistVlansGetMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpCistVlansGetMapped.setStatus("current")
_FsStpCistRemainingHopCount_Type = Integer32
_FsStpCistRemainingHopCount_Object = MibScalar
fsStpCistRemainingHopCount = _FsStpCistRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 3, 10),
    _FsStpCistRemainingHopCount_Type()
)
fsStpCistRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStpCistRemainingHopCount.setStatus("current")
_StpExternConformance_ObjectIdentity = ObjectIdentity
stpExternConformance = _StpExternConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 4)
)
_StpExternGroups_ObjectIdentity = ObjectIdentity
stpExternGroups = _StpExternGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 4, 1)
)
_RstpConformance_ObjectIdentity = ObjectIdentity
rstpConformance = _RstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 5)
)
_RstpGroups_ObjectIdentity = ObjectIdentity
rstpGroups = _RstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 5, 1)
)
_RstpCompliances_ObjectIdentity = ObjectIdentity
rstpCompliances = _RstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 5, 2)
)
_MstpConformance_ObjectIdentity = ObjectIdentity
mstpConformance = _MstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 6)
)
_MstpGroups_ObjectIdentity = ObjectIdentity
mstpGroups = _MstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 6, 1)
)
_MstpCompliances_ObjectIdentity = ObjectIdentity
mstpCompliances = _MstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 6, 2)
)

# Managed Objects groups

stpExternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 4, 1, 1)
)
stpExternGroup.setObjects(
      *(("FS-RSTP-MSTP-MIB", "fsSysStpStatus"),
        ("FS-RSTP-MSTP-MIB", "fsSysStpReset"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortIfIndex"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortAdminPathCost"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortOperPathCost"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortRole"))
)
if mibBuilder.loadTexts:
    stpExternGroup.setStatus("current")

rstpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 5, 1, 1)
)
rstpBridgeGroup.setObjects(
      *(("FS-RSTP-MSTP-MIB", "fsStpVersion"),
        ("FS-RSTP-MSTP-MIB", "fsStpTxHoldCount"),
        ("FS-RSTP-MSTP-MIB", "fsStpBpduGuard"),
        ("FS-RSTP-MSTP-MIB", "fsStpBpduFilter"))
)
if mibBuilder.loadTexts:
    rstpBridgeGroup.setStatus("current")

rstpDefaultPathCostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 5, 1, 2)
)
rstpDefaultPathCostGroup.setObjects(
    ("FS-RSTP-MSTP-MIB", "fsStpPathCostDefault")
)
if mibBuilder.loadTexts:
    rstpDefaultPathCostGroup.setStatus("current")

rstpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 5, 1, 3)
)
rstpPortGroup.setObjects(
      *(("FS-RSTP-MSTP-MIB", "fsRstpExtPortIfIndex"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortProtocolMigration"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortAdminEdgePort"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortOperEdgePort"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortAdminPointToPoint"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortOperPointToPoint"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortBpduGuard"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortBpduFilter"),
        ("FS-RSTP-MSTP-MIB", "fsStpCistRegionRoot"),
        ("FS-RSTP-MSTP-MIB", "fsStpCistPathCost"))
)
if mibBuilder.loadTexts:
    rstpPortGroup.setStatus("current")

mstpBridgeRegionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 6, 1, 1)
)
mstpBridgeRegionGroup.setObjects(
      *(("FS-RSTP-MSTP-MIB", "fsStpMstiMaxInstanceNumber"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiRegionName"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiRegionRevision"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiMaxHopNumber"))
)
if mibBuilder.loadTexts:
    mstpBridgeRegionGroup.setStatus("current")

mstpMstiBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 6, 1, 2)
)
mstpMstiBridgeGroup.setObjects(
      *(("FS-RSTP-MSTP-MIB", "fsStpMstiInstanceIndex"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiInstanceVlansAddMapped"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiInstanceVlansDeleteMapped"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiInstanceVlansGetMapped"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiInstanceRemainingHopCount"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiPriority"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiTimeSinceTopologyChange"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiTopChanges"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiDesignatedRoot"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiRootCost"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiRootPort"),
        ("FS-RSTP-MSTP-MIB", "fsStpMstiInstanceEntryStatus"))
)
if mibBuilder.loadTexts:
    mstpMstiBridgeGroup.setStatus("current")

mstpMstiPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 6, 1, 3)
)
mstpMstiPortGroup.setObjects(
      *(("FS-RSTP-MSTP-MIB", "fsStpPortMstiState"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortMstiAdminPathCost"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortMstiOperPathCost"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortMstiPriority"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortMstiDesignatedRoot"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortMstiDesignatedCost"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortMstiDesignatedBridge"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortMstiDesignatedPort"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortMstiPortRole"),
        ("FS-RSTP-MSTP-MIB", "fsStpPortMstiPortForwardTransitions"))
)
if mibBuilder.loadTexts:
    mstpMstiPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 5, 2, 1)
)
rstpCompliance.setObjects(
      *(("FS-RSTP-MSTP-MIB", "rstpBridgeGroup"),
        ("FS-RSTP-MSTP-MIB", "rstpDefaultPathCostGroup"),
        ("FS-RSTP-MSTP-MIB", "rstpPortGroup"),
        ("FS-RSTP-MSTP-MIB", "rstpDefaultPathCostGroup"))
)
if mibBuilder.loadTexts:
    rstpCompliance.setStatus(
        "current"
    )

mstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 16, 6, 2, 1)
)
mstpCompliance.setObjects(
      *(("FS-RSTP-MSTP-MIB", "mstpBridgeRegionGroup"),
        ("FS-RSTP-MSTP-MIB", "mstpMstiBridgeGroup"),
        ("FS-RSTP-MSTP-MIB", "mstpMstiPortGroup"))
)
if mibBuilder.loadTexts:
    mstpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-RSTP-MSTP-MIB",
    **{"fsStpMIB": fsStpMIB,
       "fsStpMIBObjects": fsStpMIBObjects,
       "fsSysStpStatus": fsSysStpStatus,
       "fsSysStpReset": fsSysStpReset,
       "fsStpExtPortTable": fsStpExtPortTable,
       "fsStpExtPortEntry": fsStpExtPortEntry,
       "fsStpPortIfIndex": fsStpPortIfIndex,
       "fsStpPortAdminPathCost": fsStpPortAdminPathCost,
       "fsStpPortOperPathCost": fsStpPortOperPathCost,
       "fsStpPortRole": fsStpPortRole,
       "fsRstpMIBObjects": fsRstpMIBObjects,
       "fsStpVersion": fsStpVersion,
       "fsStpTxHoldCount": fsStpTxHoldCount,
       "fsStpPathCostDefault": fsStpPathCostDefault,
       "fsRstpExtPortTable": fsRstpExtPortTable,
       "fsRstpExtPortEntry": fsRstpExtPortEntry,
       "fsRstpExtPortIfIndex": fsRstpExtPortIfIndex,
       "fsStpPortProtocolMigration": fsStpPortProtocolMigration,
       "fsStpPortAdminEdgePort": fsStpPortAdminEdgePort,
       "fsStpPortOperEdgePort": fsStpPortOperEdgePort,
       "fsStpPortAdminPointToPoint": fsStpPortAdminPointToPoint,
       "fsStpPortOperPointToPoint": fsStpPortOperPointToPoint,
       "fsStpPortBpduGuard": fsStpPortBpduGuard,
       "fsStpPortBpduFilter": fsStpPortBpduFilter,
       "fsStpBpduGuard": fsStpBpduGuard,
       "fsStpBpduFilter": fsStpBpduFilter,
       "fsStpCistRegionRoot": fsStpCistRegionRoot,
       "fsStpCistPathCost": fsStpCistPathCost,
       "fsMstpMIBObjects": fsMstpMIBObjects,
       "fsStpMstiMaxInstanceNumber": fsStpMstiMaxInstanceNumber,
       "fsStpMstiRegionName": fsStpMstiRegionName,
       "fsStpMstiRegionRevision": fsStpMstiRegionRevision,
       "fsStpMstiMaxHopNumber": fsStpMstiMaxHopNumber,
       "fsStpMstiInstanceTable": fsStpMstiInstanceTable,
       "fsStpMstiInstanceEntry": fsStpMstiInstanceEntry,
       "fsStpMstiInstanceIndex": fsStpMstiInstanceIndex,
       "fsStpMstiInstanceVlansAddMapped": fsStpMstiInstanceVlansAddMapped,
       "fsStpMstiInstanceVlansDeleteMapped": fsStpMstiInstanceVlansDeleteMapped,
       "fsStpMstiInstanceVlansGetMapped": fsStpMstiInstanceVlansGetMapped,
       "fsStpMstiInstanceRemainingHopCount": fsStpMstiInstanceRemainingHopCount,
       "fsStpMstiPriority": fsStpMstiPriority,
       "fsStpMstiTimeSinceTopologyChange": fsStpMstiTimeSinceTopologyChange,
       "fsStpMstiTopChanges": fsStpMstiTopChanges,
       "fsStpMstiDesignatedRoot": fsStpMstiDesignatedRoot,
       "fsStpMstiRootCost": fsStpMstiRootCost,
       "fsStpMstiRootPort": fsStpMstiRootPort,
       "fsStpMstiInstanceEntryStatus": fsStpMstiInstanceEntryStatus,
       "fsStpPortMstiInstanceTable": fsStpPortMstiInstanceTable,
       "fsStpPortMstiInstanceEntry": fsStpPortMstiInstanceEntry,
       "fsStpPortMstiIndex": fsStpPortMstiIndex,
       "fsStpPortMstiState": fsStpPortMstiState,
       "fsStpPortMstiAdminPathCost": fsStpPortMstiAdminPathCost,
       "fsStpPortMstiOperPathCost": fsStpPortMstiOperPathCost,
       "fsStpPortMstiPriority": fsStpPortMstiPriority,
       "fsStpPortMstiDesignatedRoot": fsStpPortMstiDesignatedRoot,
       "fsStpPortMstiDesignatedCost": fsStpPortMstiDesignatedCost,
       "fsStpPortMstiDesignatedBridge": fsStpPortMstiDesignatedBridge,
       "fsStpPortMstiDesignatedPort": fsStpPortMstiDesignatedPort,
       "fsStpPortMstiPortRole": fsStpPortMstiPortRole,
       "fsStpPortMstiPortForwardTransitions": fsStpPortMstiPortForwardTransitions,
       "fsStpMstiReset": fsStpMstiReset,
       "fsStpCistVlansAddMapped": fsStpCistVlansAddMapped,
       "fsStpCistVlansGetMapped": fsStpCistVlansGetMapped,
       "fsStpCistRemainingHopCount": fsStpCistRemainingHopCount,
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
