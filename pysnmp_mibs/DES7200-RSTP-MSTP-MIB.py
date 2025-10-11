# SNMP MIB module (DES7200-RSTP-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-RSTP-MSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:49:44 2025
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

(BridgeId,
 dot1dBridge,
 dot1dStp,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "dot1dBridge",
    "dot1dStp",
    "dot1dStpPortEntry")

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "DES7200-TC",
    "ConfigStatus",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myStpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16)
)
if mibBuilder.loadTexts:
    myStpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyStpMIBObjects_ObjectIdentity = ObjectIdentity
myStpMIBObjects = _MyStpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 1)
)


class _MySysStpStatus_Type(EnabledStatus):
    """Custom type mySysStpStatus based on EnabledStatus"""
    defaultValue = 2


_MySysStpStatus_Type.__name__ = "EnabledStatus"
_MySysStpStatus_Object = MibScalar
mySysStpStatus = _MySysStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 1, 1),
    _MySysStpStatus_Type()
)
mySysStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySysStpStatus.setStatus("current")
_MySysStpReset_Type = Integer32
_MySysStpReset_Object = MibScalar
mySysStpReset = _MySysStpReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 1, 2),
    _MySysStpReset_Type()
)
mySysStpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySysStpReset.setStatus("current")
_MyStpExtPortTable_Object = MibTable
myStpExtPortTable = _MyStpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 1, 3)
)
if mibBuilder.loadTexts:
    myStpExtPortTable.setStatus("current")
_MyStpExtPortEntry_Object = MibTableRow
myStpExtPortEntry = _MyStpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 1, 3, 1)
)
myStpExtPortEntry.setIndexNames(
    (0, "DES7200-RSTP-MSTP-MIB", "myStpPortIfIndex"),
)
if mibBuilder.loadTexts:
    myStpExtPortEntry.setStatus("current")
_MyStpPortIfIndex_Type = IfIndex
_MyStpPortIfIndex_Object = MibTableColumn
myStpPortIfIndex = _MyStpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 1, 3, 1, 1),
    _MyStpPortIfIndex_Type()
)
myStpPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortIfIndex.setStatus("current")


class _MyStpPortAdminPathCost_Type(Integer32):
    """Custom type myStpPortAdminPathCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MyStpPortAdminPathCost_Type.__name__ = "Integer32"
_MyStpPortAdminPathCost_Object = MibTableColumn
myStpPortAdminPathCost = _MyStpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 1, 3, 1, 2),
    _MyStpPortAdminPathCost_Type()
)
myStpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpPortAdminPathCost.setStatus("current")


class _MyStpPortOperPathCost_Type(Integer32):
    """Custom type myStpPortOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_MyStpPortOperPathCost_Type.__name__ = "Integer32"
_MyStpPortOperPathCost_Object = MibTableColumn
myStpPortOperPathCost = _MyStpPortOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 1, 3, 1, 3),
    _MyStpPortOperPathCost_Type()
)
myStpPortOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortOperPathCost.setStatus("current")


class _MyStpPortRole_Type(Integer32):
    """Custom type myStpPortRole based on Integer32"""
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


_MyStpPortRole_Type.__name__ = "Integer32"
_MyStpPortRole_Object = MibTableColumn
myStpPortRole = _MyStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 1, 3, 1, 4),
    _MyStpPortRole_Type()
)
myStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortRole.setStatus("current")
_MyRstpMIBObjects_ObjectIdentity = ObjectIdentity
myRstpMIBObjects = _MyRstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2)
)


class _MyStpVersion_Type(Integer32):
    """Custom type myStpVersion based on Integer32"""
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


_MyStpVersion_Type.__name__ = "Integer32"
_MyStpVersion_Object = MibScalar
myStpVersion = _MyStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 1),
    _MyStpVersion_Type()
)
myStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpVersion.setStatus("current")


class _MyStpTxHoldCount_Type(Integer32):
    """Custom type myStpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MyStpTxHoldCount_Type.__name__ = "Integer32"
_MyStpTxHoldCount_Object = MibScalar
myStpTxHoldCount = _MyStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 2),
    _MyStpTxHoldCount_Type()
)
myStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpTxHoldCount.setStatus("current")


class _MyStpPathCostDefault_Type(Integer32):
    """Custom type myStpPathCostDefault based on Integer32"""
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


_MyStpPathCostDefault_Type.__name__ = "Integer32"
_MyStpPathCostDefault_Object = MibScalar
myStpPathCostDefault = _MyStpPathCostDefault_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 3),
    _MyStpPathCostDefault_Type()
)
myStpPathCostDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpPathCostDefault.setStatus("current")
_MyRstpExtPortTable_Object = MibTable
myRstpExtPortTable = _MyRstpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4)
)
if mibBuilder.loadTexts:
    myRstpExtPortTable.setStatus("current")
_MyRstpExtPortEntry_Object = MibTableRow
myRstpExtPortEntry = _MyRstpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4, 1)
)
myRstpExtPortEntry.setIndexNames(
    (0, "DES7200-RSTP-MSTP-MIB", "myRstpExtPortIfIndex"),
)
if mibBuilder.loadTexts:
    myRstpExtPortEntry.setStatus("current")
_MyRstpExtPortIfIndex_Type = IfIndex
_MyRstpExtPortIfIndex_Object = MibTableColumn
myRstpExtPortIfIndex = _MyRstpExtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4, 1, 1),
    _MyRstpExtPortIfIndex_Type()
)
myRstpExtPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRstpExtPortIfIndex.setStatus("current")
_MyStpPortProtocolMigration_Type = TruthValue
_MyStpPortProtocolMigration_Object = MibTableColumn
myStpPortProtocolMigration = _MyStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4, 1, 2),
    _MyStpPortProtocolMigration_Type()
)
myStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpPortProtocolMigration.setStatus("current")
_MyStpPortAdminEdgePort_Type = TruthValue
_MyStpPortAdminEdgePort_Object = MibTableColumn
myStpPortAdminEdgePort = _MyStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4, 1, 3),
    _MyStpPortAdminEdgePort_Type()
)
myStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpPortAdminEdgePort.setStatus("current")
_MyStpPortOperEdgePort_Type = TruthValue
_MyStpPortOperEdgePort_Object = MibTableColumn
myStpPortOperEdgePort = _MyStpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4, 1, 4),
    _MyStpPortOperEdgePort_Type()
)
myStpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortOperEdgePort.setStatus("current")


class _MyStpPortAdminPointToPoint_Type(Integer32):
    """Custom type myStpPortAdminPointToPoint based on Integer32"""
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


_MyStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_MyStpPortAdminPointToPoint_Object = MibTableColumn
myStpPortAdminPointToPoint = _MyStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4, 1, 5),
    _MyStpPortAdminPointToPoint_Type()
)
myStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpPortAdminPointToPoint.setStatus("current")
_MyStpPortOperPointToPoint_Type = TruthValue
_MyStpPortOperPointToPoint_Object = MibTableColumn
myStpPortOperPointToPoint = _MyStpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4, 1, 6),
    _MyStpPortOperPointToPoint_Type()
)
myStpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortOperPointToPoint.setStatus("current")
_MyStpPortBpduGuard_Type = EnabledStatus
_MyStpPortBpduGuard_Object = MibTableColumn
myStpPortBpduGuard = _MyStpPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4, 1, 7),
    _MyStpPortBpduGuard_Type()
)
myStpPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpPortBpduGuard.setStatus("current")
_MyStpPortBpduFilter_Type = EnabledStatus
_MyStpPortBpduFilter_Object = MibTableColumn
myStpPortBpduFilter = _MyStpPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 4, 1, 8),
    _MyStpPortBpduFilter_Type()
)
myStpPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpPortBpduFilter.setStatus("current")
_MyStpBpduGuard_Type = EnabledStatus
_MyStpBpduGuard_Object = MibScalar
myStpBpduGuard = _MyStpBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 5),
    _MyStpBpduGuard_Type()
)
myStpBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpBpduGuard.setStatus("current")
_MyStpBpduFilter_Type = EnabledStatus
_MyStpBpduFilter_Object = MibScalar
myStpBpduFilter = _MyStpBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 6),
    _MyStpBpduFilter_Type()
)
myStpBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpBpduFilter.setStatus("current")
_MyStpCistRegionRoot_Type = BridgeId
_MyStpCistRegionRoot_Object = MibScalar
myStpCistRegionRoot = _MyStpCistRegionRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 7),
    _MyStpCistRegionRoot_Type()
)
myStpCistRegionRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpCistRegionRoot.setStatus("mandatory")
_MyStpCistPathCost_Type = Integer32
_MyStpCistPathCost_Object = MibScalar
myStpCistPathCost = _MyStpCistPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 2, 8),
    _MyStpCistPathCost_Type()
)
myStpCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpCistPathCost.setStatus("mandatory")
_MyMstpMIBObjects_ObjectIdentity = ObjectIdentity
myMstpMIBObjects = _MyMstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3)
)
_MyStpMstiMaxInstanceNumber_Type = Integer32
_MyStpMstiMaxInstanceNumber_Object = MibScalar
myStpMstiMaxInstanceNumber = _MyStpMstiMaxInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 1),
    _MyStpMstiMaxInstanceNumber_Type()
)
myStpMstiMaxInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpMstiMaxInstanceNumber.setStatus("current")


class _MyStpMstiRegionName_Type(DisplayString):
    """Custom type myStpMstiRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyStpMstiRegionName_Type.__name__ = "DisplayString"
_MyStpMstiRegionName_Object = MibScalar
myStpMstiRegionName = _MyStpMstiRegionName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 2),
    _MyStpMstiRegionName_Type()
)
myStpMstiRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpMstiRegionName.setStatus("current")


class _MyStpMstiRegionRevision_Type(Integer32):
    """Custom type myStpMstiRegionRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MyStpMstiRegionRevision_Type.__name__ = "Integer32"
_MyStpMstiRegionRevision_Object = MibScalar
myStpMstiRegionRevision = _MyStpMstiRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 3),
    _MyStpMstiRegionRevision_Type()
)
myStpMstiRegionRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpMstiRegionRevision.setStatus("current")


class _MyStpMstiMaxHopNumber_Type(Integer32):
    """Custom type myStpMstiMaxHopNumber based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_MyStpMstiMaxHopNumber_Type.__name__ = "Integer32"
_MyStpMstiMaxHopNumber_Object = MibScalar
myStpMstiMaxHopNumber = _MyStpMstiMaxHopNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 4),
    _MyStpMstiMaxHopNumber_Type()
)
myStpMstiMaxHopNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpMstiMaxHopNumber.setStatus("current")
_MyStpMstiInstanceTable_Object = MibTable
myStpMstiInstanceTable = _MyStpMstiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5)
)
if mibBuilder.loadTexts:
    myStpMstiInstanceTable.setStatus("current")
_MyStpMstiInstanceEntry_Object = MibTableRow
myStpMstiInstanceEntry = _MyStpMstiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1)
)
myStpMstiInstanceEntry.setIndexNames(
    (0, "DES7200-RSTP-MSTP-MIB", "myStpMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    myStpMstiInstanceEntry.setStatus("current")


class _MyStpMstiInstanceIndex_Type(Integer32):
    """Custom type myStpMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MyStpMstiInstanceIndex_Type.__name__ = "Integer32"
_MyStpMstiInstanceIndex_Object = MibTableColumn
myStpMstiInstanceIndex = _MyStpMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 1),
    _MyStpMstiInstanceIndex_Type()
)
myStpMstiInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpMstiInstanceIndex.setStatus("current")


class _MyStpMstiInstanceVlansAddMapped_Type(OctetString):
    """Custom type myStpMstiInstanceVlansAddMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_MyStpMstiInstanceVlansAddMapped_Type.__name__ = "OctetString"
_MyStpMstiInstanceVlansAddMapped_Object = MibTableColumn
myStpMstiInstanceVlansAddMapped = _MyStpMstiInstanceVlansAddMapped_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 2),
    _MyStpMstiInstanceVlansAddMapped_Type()
)
myStpMstiInstanceVlansAddMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpMstiInstanceVlansAddMapped.setStatus("current")


class _MyStpMstiInstanceVlansDeleteMapped_Type(OctetString):
    """Custom type myStpMstiInstanceVlansDeleteMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_MyStpMstiInstanceVlansDeleteMapped_Type.__name__ = "OctetString"
_MyStpMstiInstanceVlansDeleteMapped_Object = MibTableColumn
myStpMstiInstanceVlansDeleteMapped = _MyStpMstiInstanceVlansDeleteMapped_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 3),
    _MyStpMstiInstanceVlansDeleteMapped_Type()
)
myStpMstiInstanceVlansDeleteMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpMstiInstanceVlansDeleteMapped.setStatus("current")


class _MyStpMstiInstanceVlansGetMapped_Type(OctetString):
    """Custom type myStpMstiInstanceVlansGetMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_MyStpMstiInstanceVlansGetMapped_Type.__name__ = "OctetString"
_MyStpMstiInstanceVlansGetMapped_Object = MibTableColumn
myStpMstiInstanceVlansGetMapped = _MyStpMstiInstanceVlansGetMapped_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 4),
    _MyStpMstiInstanceVlansGetMapped_Type()
)
myStpMstiInstanceVlansGetMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpMstiInstanceVlansGetMapped.setStatus("current")


class _MyStpMstiInstanceRemainingHopCount_Type(Integer32):
    """Custom type myStpMstiInstanceRemainingHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_MyStpMstiInstanceRemainingHopCount_Type.__name__ = "Integer32"
_MyStpMstiInstanceRemainingHopCount_Object = MibTableColumn
myStpMstiInstanceRemainingHopCount = _MyStpMstiInstanceRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 5),
    _MyStpMstiInstanceRemainingHopCount_Type()
)
myStpMstiInstanceRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpMstiInstanceRemainingHopCount.setStatus("current")


class _MyStpMstiPriority_Type(Integer32):
    """Custom type myStpMstiPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MyStpMstiPriority_Type.__name__ = "Integer32"
_MyStpMstiPriority_Object = MibTableColumn
myStpMstiPriority = _MyStpMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 6),
    _MyStpMstiPriority_Type()
)
myStpMstiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpMstiPriority.setStatus("current")
_MyStpMstiTimeSinceTopologyChange_Type = TimeTicks
_MyStpMstiTimeSinceTopologyChange_Object = MibTableColumn
myStpMstiTimeSinceTopologyChange = _MyStpMstiTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 7),
    _MyStpMstiTimeSinceTopologyChange_Type()
)
myStpMstiTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpMstiTimeSinceTopologyChange.setStatus("current")
_MyStpMstiTopChanges_Type = Integer32
_MyStpMstiTopChanges_Object = MibTableColumn
myStpMstiTopChanges = _MyStpMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 8),
    _MyStpMstiTopChanges_Type()
)
myStpMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpMstiTopChanges.setStatus("current")
_MyStpMstiDesignatedRoot_Type = BridgeId
_MyStpMstiDesignatedRoot_Object = MibTableColumn
myStpMstiDesignatedRoot = _MyStpMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 9),
    _MyStpMstiDesignatedRoot_Type()
)
myStpMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpMstiDesignatedRoot.setStatus("current")
_MyStpMstiRootCost_Type = Integer32
_MyStpMstiRootCost_Object = MibTableColumn
myStpMstiRootCost = _MyStpMstiRootCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 10),
    _MyStpMstiRootCost_Type()
)
myStpMstiRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpMstiRootCost.setStatus("current")
_MyStpMstiRootPort_Type = Integer32
_MyStpMstiRootPort_Object = MibTableColumn
myStpMstiRootPort = _MyStpMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 11),
    _MyStpMstiRootPort_Type()
)
myStpMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpMstiRootPort.setStatus("current")
_MyStpMstiInstanceEntryStatus_Type = ConfigStatus
_MyStpMstiInstanceEntryStatus_Object = MibTableColumn
myStpMstiInstanceEntryStatus = _MyStpMstiInstanceEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 5, 1, 12),
    _MyStpMstiInstanceEntryStatus_Type()
)
myStpMstiInstanceEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myStpMstiInstanceEntryStatus.setStatus("current")
_MyStpPortMstiInstanceTable_Object = MibTable
myStpPortMstiInstanceTable = _MyStpPortMstiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6)
)
if mibBuilder.loadTexts:
    myStpPortMstiInstanceTable.setStatus("current")
_MyStpPortMstiInstanceEntry_Object = MibTableRow
myStpPortMstiInstanceEntry = _MyStpPortMstiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1)
)
myStpPortMstiInstanceEntry.setIndexNames(
    (0, "DES7200-RSTP-MSTP-MIB", "myStpMstiInstanceIndex"),
    (0, "DES7200-RSTP-MSTP-MIB", "myStpPortMstiIndex"),
)
if mibBuilder.loadTexts:
    myStpPortMstiInstanceEntry.setStatus("current")
_MyStpPortMstiIndex_Type = Integer32
_MyStpPortMstiIndex_Object = MibTableColumn
myStpPortMstiIndex = _MyStpPortMstiIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 1),
    _MyStpPortMstiIndex_Type()
)
myStpPortMstiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myStpPortMstiIndex.setStatus("current")


class _MyStpPortMstiState_Type(Integer32):
    """Custom type myStpPortMstiState based on Integer32"""
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


_MyStpPortMstiState_Type.__name__ = "Integer32"
_MyStpPortMstiState_Object = MibTableColumn
myStpPortMstiState = _MyStpPortMstiState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 2),
    _MyStpPortMstiState_Type()
)
myStpPortMstiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortMstiState.setStatus("current")
_MyStpPortMstiAdminPathCost_Type = Integer32
_MyStpPortMstiAdminPathCost_Object = MibTableColumn
myStpPortMstiAdminPathCost = _MyStpPortMstiAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 3),
    _MyStpPortMstiAdminPathCost_Type()
)
myStpPortMstiAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpPortMstiAdminPathCost.setStatus("current")
_MyStpPortMstiOperPathCost_Type = Counter32
_MyStpPortMstiOperPathCost_Object = MibTableColumn
myStpPortMstiOperPathCost = _MyStpPortMstiOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 4),
    _MyStpPortMstiOperPathCost_Type()
)
myStpPortMstiOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortMstiOperPathCost.setStatus("current")


class _MyStpPortMstiPriority_Type(Integer32):
    """Custom type myStpPortMstiPriority based on Integer32"""
    defaultValue = 128


_MyStpPortMstiPriority_Type.__name__ = "Integer32"
_MyStpPortMstiPriority_Object = MibTableColumn
myStpPortMstiPriority = _MyStpPortMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 5),
    _MyStpPortMstiPriority_Type()
)
myStpPortMstiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpPortMstiPriority.setStatus("current")
_MyStpPortMstiDesignatedRoot_Type = BridgeId
_MyStpPortMstiDesignatedRoot_Object = MibTableColumn
myStpPortMstiDesignatedRoot = _MyStpPortMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 6),
    _MyStpPortMstiDesignatedRoot_Type()
)
myStpPortMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortMstiDesignatedRoot.setStatus("current")
_MyStpPortMstiDesignatedCost_Type = Integer32
_MyStpPortMstiDesignatedCost_Object = MibTableColumn
myStpPortMstiDesignatedCost = _MyStpPortMstiDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 7),
    _MyStpPortMstiDesignatedCost_Type()
)
myStpPortMstiDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortMstiDesignatedCost.setStatus("current")
_MyStpPortMstiDesignatedBridge_Type = BridgeId
_MyStpPortMstiDesignatedBridge_Object = MibTableColumn
myStpPortMstiDesignatedBridge = _MyStpPortMstiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 8),
    _MyStpPortMstiDesignatedBridge_Type()
)
myStpPortMstiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortMstiDesignatedBridge.setStatus("current")


class _MyStpPortMstiDesignatedPort_Type(OctetString):
    """Custom type myStpPortMstiDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_MyStpPortMstiDesignatedPort_Type.__name__ = "OctetString"
_MyStpPortMstiDesignatedPort_Object = MibTableColumn
myStpPortMstiDesignatedPort = _MyStpPortMstiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 9),
    _MyStpPortMstiDesignatedPort_Type()
)
myStpPortMstiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortMstiDesignatedPort.setStatus("current")


class _MyStpPortMstiPortRole_Type(Integer32):
    """Custom type myStpPortMstiPortRole based on Integer32"""
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


_MyStpPortMstiPortRole_Type.__name__ = "Integer32"
_MyStpPortMstiPortRole_Object = MibTableColumn
myStpPortMstiPortRole = _MyStpPortMstiPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 10),
    _MyStpPortMstiPortRole_Type()
)
myStpPortMstiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortMstiPortRole.setStatus("current")
_MyStpPortMstiPortForwardTransitions_Type = Integer32
_MyStpPortMstiPortForwardTransitions_Object = MibTableColumn
myStpPortMstiPortForwardTransitions = _MyStpPortMstiPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 6, 1, 11),
    _MyStpPortMstiPortForwardTransitions_Type()
)
myStpPortMstiPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpPortMstiPortForwardTransitions.setStatus("current")
_MyStpMstiReset_Type = Integer32
_MyStpMstiReset_Object = MibScalar
myStpMstiReset = _MyStpMstiReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 7),
    _MyStpMstiReset_Type()
)
myStpMstiReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpMstiReset.setStatus("current")
_MyStpCistVlansAddMapped_Type = OctetString
_MyStpCistVlansAddMapped_Object = MibScalar
myStpCistVlansAddMapped = _MyStpCistVlansAddMapped_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 8),
    _MyStpCistVlansAddMapped_Type()
)
myStpCistVlansAddMapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myStpCistVlansAddMapped.setStatus("mandatory")
_MyStpCistVlansGetMapped_Type = OctetString
_MyStpCistVlansGetMapped_Object = MibScalar
myStpCistVlansGetMapped = _MyStpCistVlansGetMapped_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 9),
    _MyStpCistVlansGetMapped_Type()
)
myStpCistVlansGetMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpCistVlansGetMapped.setStatus("mandatory")
_MyStpCistRemainingHopCount_Type = Integer32
_MyStpCistRemainingHopCount_Object = MibScalar
myStpCistRemainingHopCount = _MyStpCistRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 3, 10),
    _MyStpCistRemainingHopCount_Type()
)
myStpCistRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myStpCistRemainingHopCount.setStatus("mandatory")
_StpExternConformance_ObjectIdentity = ObjectIdentity
stpExternConformance = _StpExternConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 4)
)
_StpExternGroups_ObjectIdentity = ObjectIdentity
stpExternGroups = _StpExternGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 4, 1)
)
_RstpConformance_ObjectIdentity = ObjectIdentity
rstpConformance = _RstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 5)
)
_RstpGroups_ObjectIdentity = ObjectIdentity
rstpGroups = _RstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 5, 1)
)
_RstpCompliances_ObjectIdentity = ObjectIdentity
rstpCompliances = _RstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 5, 2)
)
_MstpConformance_ObjectIdentity = ObjectIdentity
mstpConformance = _MstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 6)
)
_MstpGroups_ObjectIdentity = ObjectIdentity
mstpGroups = _MstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 6, 1)
)
_MstpCompliances_ObjectIdentity = ObjectIdentity
mstpCompliances = _MstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 6, 2)
)

# Managed Objects groups

stpExternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 4, 1, 1)
)
stpExternGroup.setObjects(
      *(("DES7200-RSTP-MSTP-MIB", "mySysStpStatus"),
        ("DES7200-RSTP-MSTP-MIB", "mySysStpReset"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortIfIndex"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortAdminPathCost"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortOperPathCost"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortRole"))
)
if mibBuilder.loadTexts:
    stpExternGroup.setStatus("current")

rstpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 5, 1, 1)
)
rstpBridgeGroup.setObjects(
      *(("DES7200-RSTP-MSTP-MIB", "myStpVersion"),
        ("DES7200-RSTP-MSTP-MIB", "myStpTxHoldCount"),
        ("DES7200-RSTP-MSTP-MIB", "myStpBpduGuard"),
        ("DES7200-RSTP-MSTP-MIB", "myStpBpduFilter"))
)
if mibBuilder.loadTexts:
    rstpBridgeGroup.setStatus("current")

rstpDefaultPathCostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 5, 1, 2)
)
rstpDefaultPathCostGroup.setObjects(
    ("DES7200-RSTP-MSTP-MIB", "myStpPathCostDefault")
)
if mibBuilder.loadTexts:
    rstpDefaultPathCostGroup.setStatus("current")

rstpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 5, 1, 3)
)
rstpPortGroup.setObjects(
      *(("DES7200-RSTP-MSTP-MIB", "myRstpExtPortIfIndex"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortProtocolMigration"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortAdminEdgePort"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortOperEdgePort"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortAdminPointToPoint"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortOperPointToPoint"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortBpduGuard"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortBpduFilter"),
        ("DES7200-RSTP-MSTP-MIB", "myStpCistRegionRoot"),
        ("DES7200-RSTP-MSTP-MIB", "myStpCistPathCost"))
)
if mibBuilder.loadTexts:
    rstpPortGroup.setStatus("current")

mstpBridgeRegionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 6, 1, 1)
)
mstpBridgeRegionGroup.setObjects(
      *(("DES7200-RSTP-MSTP-MIB", "myStpMstiMaxInstanceNumber"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiRegionName"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiRegionRevision"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiMaxHopNumber"))
)
if mibBuilder.loadTexts:
    mstpBridgeRegionGroup.setStatus("current")

mstpMstiBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 6, 1, 2)
)
mstpMstiBridgeGroup.setObjects(
      *(("DES7200-RSTP-MSTP-MIB", "myStpMstiInstanceIndex"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiInstanceVlansAddMapped"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiInstanceVlansDeleteMapped"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiInstanceVlansGetMapped"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiInstanceRemainingHopCount"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiPriority"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiTimeSinceTopologyChange"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiTopChanges"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiDesignatedRoot"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiRootCost"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiRootPort"),
        ("DES7200-RSTP-MSTP-MIB", "myStpMstiInstanceEntryStatus"))
)
if mibBuilder.loadTexts:
    mstpMstiBridgeGroup.setStatus("current")

mstpMstiPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 6, 1, 3)
)
mstpMstiPortGroup.setObjects(
      *(("DES7200-RSTP-MSTP-MIB", "myStpPortMstiIndex"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiState"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiAdminPathCost"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiOperPathCost"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiPriority"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiDesignatedRoot"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiDesignatedCost"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiDesignatedBridge"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiDesignatedPort"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiPortRole"),
        ("DES7200-RSTP-MSTP-MIB", "myStpPortMstiPortForwardTransitions"))
)
if mibBuilder.loadTexts:
    mstpMstiPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 5, 2, 1)
)
rstpCompliance.setObjects(
      *(("DES7200-RSTP-MSTP-MIB", "rstpBridgeGroup"),
        ("DES7200-RSTP-MSTP-MIB", "rstpDefaultPathCostGroup"),
        ("DES7200-RSTP-MSTP-MIB", "rstpPortGroup"),
        ("DES7200-RSTP-MSTP-MIB", "rstpDefaultPathCostGroup"))
)
if mibBuilder.loadTexts:
    rstpCompliance.setStatus(
        "current"
    )

mstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 16, 6, 2, 1)
)
mstpCompliance.setObjects(
      *(("DES7200-RSTP-MSTP-MIB", "mstpBridgeRegionGroup"),
        ("DES7200-RSTP-MSTP-MIB", "mstpMstiBridgeGroup"),
        ("DES7200-RSTP-MSTP-MIB", "mstpMstiPortGroup"))
)
if mibBuilder.loadTexts:
    mstpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-RSTP-MSTP-MIB",
    **{"myStpMIB": myStpMIB,
       "myStpMIBObjects": myStpMIBObjects,
       "mySysStpStatus": mySysStpStatus,
       "mySysStpReset": mySysStpReset,
       "myStpExtPortTable": myStpExtPortTable,
       "myStpExtPortEntry": myStpExtPortEntry,
       "myStpPortIfIndex": myStpPortIfIndex,
       "myStpPortAdminPathCost": myStpPortAdminPathCost,
       "myStpPortOperPathCost": myStpPortOperPathCost,
       "myStpPortRole": myStpPortRole,
       "myRstpMIBObjects": myRstpMIBObjects,
       "myStpVersion": myStpVersion,
       "myStpTxHoldCount": myStpTxHoldCount,
       "myStpPathCostDefault": myStpPathCostDefault,
       "myRstpExtPortTable": myRstpExtPortTable,
       "myRstpExtPortEntry": myRstpExtPortEntry,
       "myRstpExtPortIfIndex": myRstpExtPortIfIndex,
       "myStpPortProtocolMigration": myStpPortProtocolMigration,
       "myStpPortAdminEdgePort": myStpPortAdminEdgePort,
       "myStpPortOperEdgePort": myStpPortOperEdgePort,
       "myStpPortAdminPointToPoint": myStpPortAdminPointToPoint,
       "myStpPortOperPointToPoint": myStpPortOperPointToPoint,
       "myStpPortBpduGuard": myStpPortBpduGuard,
       "myStpPortBpduFilter": myStpPortBpduFilter,
       "myStpBpduGuard": myStpBpduGuard,
       "myStpBpduFilter": myStpBpduFilter,
       "myStpCistRegionRoot": myStpCistRegionRoot,
       "myStpCistPathCost": myStpCistPathCost,
       "myMstpMIBObjects": myMstpMIBObjects,
       "myStpMstiMaxInstanceNumber": myStpMstiMaxInstanceNumber,
       "myStpMstiRegionName": myStpMstiRegionName,
       "myStpMstiRegionRevision": myStpMstiRegionRevision,
       "myStpMstiMaxHopNumber": myStpMstiMaxHopNumber,
       "myStpMstiInstanceTable": myStpMstiInstanceTable,
       "myStpMstiInstanceEntry": myStpMstiInstanceEntry,
       "myStpMstiInstanceIndex": myStpMstiInstanceIndex,
       "myStpMstiInstanceVlansAddMapped": myStpMstiInstanceVlansAddMapped,
       "myStpMstiInstanceVlansDeleteMapped": myStpMstiInstanceVlansDeleteMapped,
       "myStpMstiInstanceVlansGetMapped": myStpMstiInstanceVlansGetMapped,
       "myStpMstiInstanceRemainingHopCount": myStpMstiInstanceRemainingHopCount,
       "myStpMstiPriority": myStpMstiPriority,
       "myStpMstiTimeSinceTopologyChange": myStpMstiTimeSinceTopologyChange,
       "myStpMstiTopChanges": myStpMstiTopChanges,
       "myStpMstiDesignatedRoot": myStpMstiDesignatedRoot,
       "myStpMstiRootCost": myStpMstiRootCost,
       "myStpMstiRootPort": myStpMstiRootPort,
       "myStpMstiInstanceEntryStatus": myStpMstiInstanceEntryStatus,
       "myStpPortMstiInstanceTable": myStpPortMstiInstanceTable,
       "myStpPortMstiInstanceEntry": myStpPortMstiInstanceEntry,
       "myStpPortMstiIndex": myStpPortMstiIndex,
       "myStpPortMstiState": myStpPortMstiState,
       "myStpPortMstiAdminPathCost": myStpPortMstiAdminPathCost,
       "myStpPortMstiOperPathCost": myStpPortMstiOperPathCost,
       "myStpPortMstiPriority": myStpPortMstiPriority,
       "myStpPortMstiDesignatedRoot": myStpPortMstiDesignatedRoot,
       "myStpPortMstiDesignatedCost": myStpPortMstiDesignatedCost,
       "myStpPortMstiDesignatedBridge": myStpPortMstiDesignatedBridge,
       "myStpPortMstiDesignatedPort": myStpPortMstiDesignatedPort,
       "myStpPortMstiPortRole": myStpPortMstiPortRole,
       "myStpPortMstiPortForwardTransitions": myStpPortMstiPortForwardTransitions,
       "myStpMstiReset": myStpMstiReset,
       "myStpCistVlansAddMapped": myStpCistVlansAddMapped,
       "myStpCistVlansGetMapped": myStpCistVlansGetMapped,
       "myStpCistRemainingHopCount": myStpCistRemainingHopCount,
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
