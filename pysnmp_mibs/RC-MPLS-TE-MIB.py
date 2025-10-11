# SNMP MIB module (RC-MPLS-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/RC-MPLS-TE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:22:48 2025
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

(rc,) = mibBuilder.importSymbols(
    "RC-SMI",
    "rc")

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


# MODULE-IDENTITY

rcMplsTeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 65000, 1)
)
if mibBuilder.loadTexts:
    rcMplsTeMIB.setRevisions(
        ("2012-12-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcMplsTeNotifications_ObjectIdentity = ObjectIdentity
rcMplsTeNotifications = _RcMplsTeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 65000, 1, 0)
)
_RcMplsTETunnelCfgTable_Object = MibTable
rcMplsTETunnelCfgTable = _RcMplsTETunnelCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1)
)
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgTable.setStatus("current")
_RcMplsTETunnelCfgEntry_Object = MibTableRow
rcMplsTETunnelCfgEntry = _RcMplsTETunnelCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1)
)
rcMplsTETunnelCfgEntry.setIndexNames(
    (0, "RC-MPLS-TE-MIB", "rcMplsTETunnelCfgTunnelID"),
)
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgEntry.setStatus("current")


class _RcMplsTETunnelCfgTunnelID_Type(Unsigned32):
    """Custom type rcMplsTETunnelCfgTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_RcMplsTETunnelCfgTunnelID_Type.__name__ = "Unsigned32"
_RcMplsTETunnelCfgTunnelID_Object = MibTableColumn
rcMplsTETunnelCfgTunnelID = _RcMplsTETunnelCfgTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 1),
    _RcMplsTETunnelCfgTunnelID_Type()
)
rcMplsTETunnelCfgTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgTunnelID.setStatus("current")
_RcMplsTETunnelCfgEgressLSRId_Type = IpAddress
_RcMplsTETunnelCfgEgressLSRId_Object = MibTableColumn
rcMplsTETunnelCfgEgressLSRId = _RcMplsTETunnelCfgEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 2),
    _RcMplsTETunnelCfgEgressLSRId_Type()
)
rcMplsTETunnelCfgEgressLSRId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgEgressLSRId.setStatus("current")


class _RcMplsTETunnelCfgSetupPrio_Type(Integer32):
    """Custom type rcMplsTETunnelCfgSetupPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcMplsTETunnelCfgSetupPrio_Type.__name__ = "Integer32"
_RcMplsTETunnelCfgSetupPrio_Object = MibTableColumn
rcMplsTETunnelCfgSetupPrio = _RcMplsTETunnelCfgSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 3),
    _RcMplsTETunnelCfgSetupPrio_Type()
)
rcMplsTETunnelCfgSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgSetupPrio.setStatus("current")


class _RcMplsTETunnelCfgHoldingPrio_Type(Integer32):
    """Custom type rcMplsTETunnelCfgHoldingPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcMplsTETunnelCfgHoldingPrio_Type.__name__ = "Integer32"
_RcMplsTETunnelCfgHoldingPrio_Object = MibTableColumn
rcMplsTETunnelCfgHoldingPrio = _RcMplsTETunnelCfgHoldingPrio_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 4),
    _RcMplsTETunnelCfgHoldingPrio_Type()
)
rcMplsTETunnelCfgHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgHoldingPrio.setStatus("current")


class _RcMplsTETunnelCfgRecordRoute_Type(Integer32):
    """Custom type rcMplsTETunnelCfgRecordRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RcMplsTETunnelCfgRecordRoute_Type.__name__ = "Integer32"
_RcMplsTETunnelCfgRecordRoute_Object = MibTableColumn
rcMplsTETunnelCfgRecordRoute = _RcMplsTETunnelCfgRecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 5),
    _RcMplsTETunnelCfgRecordRoute_Type()
)
rcMplsTETunnelCfgRecordRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgRecordRoute.setStatus("current")
_RcMplsTETunnelCfgBandwidth_Type = Unsigned32
_RcMplsTETunnelCfgBandwidth_Object = MibTableColumn
rcMplsTETunnelCfgBandwidth = _RcMplsTETunnelCfgBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 6),
    _RcMplsTETunnelCfgBandwidth_Type()
)
rcMplsTETunnelCfgBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgBandwidth.setStatus("current")


class _RcMplsTETunnelCfgExplicitPathName_Type(DisplayString):
    """Custom type rcMplsTETunnelCfgExplicitPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_RcMplsTETunnelCfgExplicitPathName_Type.__name__ = "DisplayString"
_RcMplsTETunnelCfgExplicitPathName_Object = MibTableColumn
rcMplsTETunnelCfgExplicitPathName = _RcMplsTETunnelCfgExplicitPathName_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 7),
    _RcMplsTETunnelCfgExplicitPathName_Type()
)
rcMplsTETunnelCfgExplicitPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgExplicitPathName.setStatus("current")


class _RcMplsTETunnelCfgExplicitPathID_Type(Unsigned32):
    """Custom type rcMplsTETunnelCfgExplicitPathID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcMplsTETunnelCfgExplicitPathID_Type.__name__ = "Unsigned32"
_RcMplsTETunnelCfgExplicitPathID_Object = MibTableColumn
rcMplsTETunnelCfgExplicitPathID = _RcMplsTETunnelCfgExplicitPathID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 8),
    _RcMplsTETunnelCfgExplicitPathID_Type()
)
rcMplsTETunnelCfgExplicitPathID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgExplicitPathID.setStatus("current")


class _RcMplsTETunnelCfgHSB_Type(Integer32):
    """Custom type rcMplsTETunnelCfgHSB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RcMplsTETunnelCfgHSB_Type.__name__ = "Integer32"
_RcMplsTETunnelCfgHSB_Object = MibTableColumn
rcMplsTETunnelCfgHSB = _RcMplsTETunnelCfgHSB_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 9),
    _RcMplsTETunnelCfgHSB_Type()
)
rcMplsTETunnelCfgHSB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgHSB.setStatus("current")


class _RcMplsTETunnelCfgHSBExplicitPathName_Type(DisplayString):
    """Custom type rcMplsTETunnelCfgHSBExplicitPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_RcMplsTETunnelCfgHSBExplicitPathName_Type.__name__ = "DisplayString"
_RcMplsTETunnelCfgHSBExplicitPathName_Object = MibTableColumn
rcMplsTETunnelCfgHSBExplicitPathName = _RcMplsTETunnelCfgHSBExplicitPathName_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 10),
    _RcMplsTETunnelCfgHSBExplicitPathName_Type()
)
rcMplsTETunnelCfgHSBExplicitPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgHSBExplicitPathName.setStatus("current")


class _RcMplsTETunnelCfgHSBExplicitPathID_Type(Unsigned32):
    """Custom type rcMplsTETunnelCfgHSBExplicitPathID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcMplsTETunnelCfgHSBExplicitPathID_Type.__name__ = "Unsigned32"
_RcMplsTETunnelCfgHSBExplicitPathID_Object = MibTableColumn
rcMplsTETunnelCfgHSBExplicitPathID = _RcMplsTETunnelCfgHSBExplicitPathID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 11),
    _RcMplsTETunnelCfgHSBExplicitPathID_Type()
)
rcMplsTETunnelCfgHSBExplicitPathID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgHSBExplicitPathID.setStatus("current")
_RcMplsTETunnelCfgRowSta_Type = RowStatus
_RcMplsTETunnelCfgRowSta_Object = MibTableColumn
rcMplsTETunnelCfgRowSta = _RcMplsTETunnelCfgRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 12),
    _RcMplsTETunnelCfgRowSta_Type()
)
rcMplsTETunnelCfgRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelCfgRowSta.setStatus("current")


class _RcMplsTunnelOperStatus_Type(Integer32):
    """Custom type rcMplsTunnelOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_RcMplsTunnelOperStatus_Type.__name__ = "Integer32"
_RcMplsTunnelOperStatus_Object = MibTableColumn
rcMplsTunnelOperStatus = _RcMplsTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 1, 1, 13),
    _RcMplsTunnelOperStatus_Type()
)
rcMplsTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMplsTunnelOperStatus.setStatus("current")
_RcMplsTEPathOptCfgTable_Object = MibTable
rcMplsTEPathOptCfgTable = _RcMplsTEPathOptCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 2)
)
if mibBuilder.loadTexts:
    rcMplsTEPathOptCfgTable.setStatus("current")
_RcMplsTEPathOptCfgEntry_Object = MibTableRow
rcMplsTEPathOptCfgEntry = _RcMplsTEPathOptCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 2, 1)
)
rcMplsTEPathOptCfgEntry.setIndexNames(
    (0, "RC-MPLS-TE-MIB", "rcMplsTEPathOptCfgTunnelID"),
    (0, "RC-MPLS-TE-MIB", "rcMplsTEPathOptCfgNumber"),
)
if mibBuilder.loadTexts:
    rcMplsTEPathOptCfgEntry.setStatus("current")


class _RcMplsTEPathOptCfgTunnelID_Type(Unsigned32):
    """Custom type rcMplsTEPathOptCfgTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_RcMplsTEPathOptCfgTunnelID_Type.__name__ = "Unsigned32"
_RcMplsTEPathOptCfgTunnelID_Object = MibTableColumn
rcMplsTEPathOptCfgTunnelID = _RcMplsTEPathOptCfgTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 2, 1, 1),
    _RcMplsTEPathOptCfgTunnelID_Type()
)
rcMplsTEPathOptCfgTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEPathOptCfgTunnelID.setStatus("current")


class _RcMplsTEPathOptCfgNumber_Type(Unsigned32):
    """Custom type rcMplsTEPathOptCfgNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RcMplsTEPathOptCfgNumber_Type.__name__ = "Unsigned32"
_RcMplsTEPathOptCfgNumber_Object = MibTableColumn
rcMplsTEPathOptCfgNumber = _RcMplsTEPathOptCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 2, 1, 2),
    _RcMplsTEPathOptCfgNumber_Type()
)
rcMplsTEPathOptCfgNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEPathOptCfgNumber.setStatus("current")


class _RcMplsTEPathOptCfgPathType_Type(Integer32):
    """Custom type rcMplsTEPathOptCfgPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("explicitId", 2),
          ("explicitName", 3))
    )


_RcMplsTEPathOptCfgPathType_Type.__name__ = "Integer32"
_RcMplsTEPathOptCfgPathType_Object = MibTableColumn
rcMplsTEPathOptCfgPathType = _RcMplsTEPathOptCfgPathType_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 2, 1, 3),
    _RcMplsTEPathOptCfgPathType_Type()
)
rcMplsTEPathOptCfgPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEPathOptCfgPathType.setStatus("current")


class _RcMplsTEPathOptCfgExpPathName_Type(DisplayString):
    """Custom type rcMplsTEPathOptCfgExpPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_RcMplsTEPathOptCfgExpPathName_Type.__name__ = "DisplayString"
_RcMplsTEPathOptCfgExpPathName_Object = MibTableColumn
rcMplsTEPathOptCfgExpPathName = _RcMplsTEPathOptCfgExpPathName_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 2, 1, 4),
    _RcMplsTEPathOptCfgExpPathName_Type()
)
rcMplsTEPathOptCfgExpPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEPathOptCfgExpPathName.setStatus("current")


class _RcMplsTEPathOptCfgExpPathID_Type(Unsigned32):
    """Custom type rcMplsTEPathOptCfgExpPathID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_RcMplsTEPathOptCfgExpPathID_Type.__name__ = "Unsigned32"
_RcMplsTEPathOptCfgExpPathID_Object = MibTableColumn
rcMplsTEPathOptCfgExpPathID = _RcMplsTEPathOptCfgExpPathID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 2, 1, 5),
    _RcMplsTEPathOptCfgExpPathID_Type()
)
rcMplsTEPathOptCfgExpPathID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEPathOptCfgExpPathID.setStatus("current")
_RcMplsTEPathOptCfgRowSta_Type = RowStatus
_RcMplsTEPathOptCfgRowSta_Object = MibTableColumn
rcMplsTEPathOptCfgRowSta = _RcMplsTEPathOptCfgRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 2, 1, 6),
    _RcMplsTEPathOptCfgRowSta_Type()
)
rcMplsTEPathOptCfgRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEPathOptCfgRowSta.setStatus("current")
_RcMplsTEExplicitPathNameCfgTable_Object = MibTable
rcMplsTEExplicitPathNameCfgTable = _RcMplsTEExplicitPathNameCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 3)
)
if mibBuilder.loadTexts:
    rcMplsTEExplicitPathNameCfgTable.setStatus("current")
_RcMplsTEExplicitPathNameCfgEntry_Object = MibTableRow
rcMplsTEExplicitPathNameCfgEntry = _RcMplsTEExplicitPathNameCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 3, 1)
)
rcMplsTEExplicitPathNameCfgEntry.setIndexNames(
    (0, "RC-MPLS-TE-MIB", "rcMplsTEExplicitPathNameCfgName"),
)
if mibBuilder.loadTexts:
    rcMplsTEExplicitPathNameCfgEntry.setStatus("current")


class _RcMplsTEExplicitPathNameCfgName_Type(DisplayString):
    """Custom type rcMplsTEExplicitPathNameCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_RcMplsTEExplicitPathNameCfgName_Type.__name__ = "DisplayString"
_RcMplsTEExplicitPathNameCfgName_Object = MibTableColumn
rcMplsTEExplicitPathNameCfgName = _RcMplsTEExplicitPathNameCfgName_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 3, 1, 1),
    _RcMplsTEExplicitPathNameCfgName_Type()
)
rcMplsTEExplicitPathNameCfgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEExplicitPathNameCfgName.setStatus("current")
_RcMplsTEExplicitPathNameCfgRowSta_Type = RowStatus
_RcMplsTEExplicitPathNameCfgRowSta_Object = MibTableColumn
rcMplsTEExplicitPathNameCfgRowSta = _RcMplsTEExplicitPathNameCfgRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 3, 1, 2),
    _RcMplsTEExplicitPathNameCfgRowSta_Type()
)
rcMplsTEExplicitPathNameCfgRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitPathNameCfgRowSta.setStatus("current")
_RcMplsTEExplicitPathIDCfgTable_Object = MibTable
rcMplsTEExplicitPathIDCfgTable = _RcMplsTEExplicitPathIDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 4)
)
if mibBuilder.loadTexts:
    rcMplsTEExplicitPathIDCfgTable.setStatus("current")
_RcMplsTEExplicitPathIDCfgEntry_Object = MibTableRow
rcMplsTEExplicitPathIDCfgEntry = _RcMplsTEExplicitPathIDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 4, 1)
)
rcMplsTEExplicitPathIDCfgEntry.setIndexNames(
    (0, "RC-MPLS-TE-MIB", "rcMplsTEExplicitPathIDCfgIdentifer"),
)
if mibBuilder.loadTexts:
    rcMplsTEExplicitPathIDCfgEntry.setStatus("current")


class _RcMplsTEExplicitPathIDCfgIdentifer_Type(Unsigned32):
    """Custom type rcMplsTEExplicitPathIDCfgIdentifer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcMplsTEExplicitPathIDCfgIdentifer_Type.__name__ = "Unsigned32"
_RcMplsTEExplicitPathIDCfgIdentifer_Object = MibTableColumn
rcMplsTEExplicitPathIDCfgIdentifer = _RcMplsTEExplicitPathIDCfgIdentifer_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 4, 1, 1),
    _RcMplsTEExplicitPathIDCfgIdentifer_Type()
)
rcMplsTEExplicitPathIDCfgIdentifer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEExplicitPathIDCfgIdentifer.setStatus("current")
_RcMplsTEExplicitPathIDCfgRowSta_Type = RowStatus
_RcMplsTEExplicitPathIDCfgRowSta_Object = MibTableColumn
rcMplsTEExplicitPathIDCfgRowSta = _RcMplsTEExplicitPathIDCfgRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 4, 1, 2),
    _RcMplsTEExplicitPathIDCfgRowSta_Type()
)
rcMplsTEExplicitPathIDCfgRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitPathIDCfgRowSta.setStatus("current")
_RcMplsTEExplicitRouteNameCfgTable_Object = MibTable
rcMplsTEExplicitRouteNameCfgTable = _RcMplsTEExplicitRouteNameCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 5)
)
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteNameCfgTable.setStatus("current")
_RcMplsTEExplicitRouteNameCfgEntry_Object = MibTableRow
rcMplsTEExplicitRouteNameCfgEntry = _RcMplsTEExplicitRouteNameCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 5, 1)
)
rcMplsTEExplicitRouteNameCfgEntry.setIndexNames(
    (0, "RC-MPLS-TE-MIB", "rcMplsTEExplicitRouteNameCfgName"),
    (0, "RC-MPLS-TE-MIB", "rcMplsTEExplicitRouteNameCfgIndex"),
)
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteNameCfgEntry.setStatus("current")


class _RcMplsTEExplicitRouteNameCfgName_Type(DisplayString):
    """Custom type rcMplsTEExplicitRouteNameCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_RcMplsTEExplicitRouteNameCfgName_Type.__name__ = "DisplayString"
_RcMplsTEExplicitRouteNameCfgName_Object = MibTableColumn
rcMplsTEExplicitRouteNameCfgName = _RcMplsTEExplicitRouteNameCfgName_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 5, 1, 1),
    _RcMplsTEExplicitRouteNameCfgName_Type()
)
rcMplsTEExplicitRouteNameCfgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteNameCfgName.setStatus("current")


class _RcMplsTEExplicitRouteNameCfgIndex_Type(Unsigned32):
    """Custom type rcMplsTEExplicitRouteNameCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_RcMplsTEExplicitRouteNameCfgIndex_Type.__name__ = "Unsigned32"
_RcMplsTEExplicitRouteNameCfgIndex_Object = MibTableColumn
rcMplsTEExplicitRouteNameCfgIndex = _RcMplsTEExplicitRouteNameCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 5, 1, 2),
    _RcMplsTEExplicitRouteNameCfgIndex_Type()
)
rcMplsTEExplicitRouteNameCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteNameCfgIndex.setStatus("current")
_RcMplsTEExplicitRouteNameCfgNextIP_Type = IpAddress
_RcMplsTEExplicitRouteNameCfgNextIP_Object = MibTableColumn
rcMplsTEExplicitRouteNameCfgNextIP = _RcMplsTEExplicitRouteNameCfgNextIP_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 5, 1, 3),
    _RcMplsTEExplicitRouteNameCfgNextIP_Type()
)
rcMplsTEExplicitRouteNameCfgNextIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteNameCfgNextIP.setStatus("current")


class _RcMplsTEExplicitRouteNameCfgHopType_Type(Integer32):
    """Custom type rcMplsTEExplicitRouteNameCfgHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_RcMplsTEExplicitRouteNameCfgHopType_Type.__name__ = "Integer32"
_RcMplsTEExplicitRouteNameCfgHopType_Object = MibTableColumn
rcMplsTEExplicitRouteNameCfgHopType = _RcMplsTEExplicitRouteNameCfgHopType_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 5, 1, 4),
    _RcMplsTEExplicitRouteNameCfgHopType_Type()
)
rcMplsTEExplicitRouteNameCfgHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteNameCfgHopType.setStatus("current")


class _RcMplsTEExplicitRouteNameCfgHopAttribute_Type(Integer32):
    """Custom type rcMplsTEExplicitRouteNameCfgHopAttribute based on Integer32"""
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
        *(("strict", 1),
          ("loose", 2),
          ("interface", 3),
          ("routerid", 4))
    )


_RcMplsTEExplicitRouteNameCfgHopAttribute_Type.__name__ = "Integer32"
_RcMplsTEExplicitRouteNameCfgHopAttribute_Object = MibTableColumn
rcMplsTEExplicitRouteNameCfgHopAttribute = _RcMplsTEExplicitRouteNameCfgHopAttribute_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 5, 1, 5),
    _RcMplsTEExplicitRouteNameCfgHopAttribute_Type()
)
rcMplsTEExplicitRouteNameCfgHopAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteNameCfgHopAttribute.setStatus("current")
_RcMplsTEExplicitRouteNameCfgRowSta_Type = RowStatus
_RcMplsTEExplicitRouteNameCfgRowSta_Object = MibTableColumn
rcMplsTEExplicitRouteNameCfgRowSta = _RcMplsTEExplicitRouteNameCfgRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 5, 1, 6),
    _RcMplsTEExplicitRouteNameCfgRowSta_Type()
)
rcMplsTEExplicitRouteNameCfgRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteNameCfgRowSta.setStatus("current")
_RcMplsTEExplicitRouteIDCfgTable_Object = MibTable
rcMplsTEExplicitRouteIDCfgTable = _RcMplsTEExplicitRouteIDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 6)
)
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteIDCfgTable.setStatus("current")
_RcMplsTEExplicitRouteIDCfgEntry_Object = MibTableRow
rcMplsTEExplicitRouteIDCfgEntry = _RcMplsTEExplicitRouteIDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 6, 1)
)
rcMplsTEExplicitRouteIDCfgEntry.setIndexNames(
    (0, "RC-MPLS-TE-MIB", "rcMplsTEExplicitRouteIDCfgIdentifer"),
    (0, "RC-MPLS-TE-MIB", "rcMplsTEExplicitRouteIDCfgIndex"),
)
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteIDCfgEntry.setStatus("current")


class _RcMplsTEExplicitRouteIDCfgIdentifer_Type(Unsigned32):
    """Custom type rcMplsTEExplicitRouteIDCfgIdentifer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcMplsTEExplicitRouteIDCfgIdentifer_Type.__name__ = "Unsigned32"
_RcMplsTEExplicitRouteIDCfgIdentifer_Object = MibTableColumn
rcMplsTEExplicitRouteIDCfgIdentifer = _RcMplsTEExplicitRouteIDCfgIdentifer_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 6, 1, 1),
    _RcMplsTEExplicitRouteIDCfgIdentifer_Type()
)
rcMplsTEExplicitRouteIDCfgIdentifer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteIDCfgIdentifer.setStatus("current")


class _RcMplsTEExplicitRouteIDCfgIndex_Type(Unsigned32):
    """Custom type rcMplsTEExplicitRouteIDCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_RcMplsTEExplicitRouteIDCfgIndex_Type.__name__ = "Unsigned32"
_RcMplsTEExplicitRouteIDCfgIndex_Object = MibTableColumn
rcMplsTEExplicitRouteIDCfgIndex = _RcMplsTEExplicitRouteIDCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 6, 1, 2),
    _RcMplsTEExplicitRouteIDCfgIndex_Type()
)
rcMplsTEExplicitRouteIDCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteIDCfgIndex.setStatus("current")
_RcMplsTEExplicitRouteIDCfgNextIP_Type = IpAddress
_RcMplsTEExplicitRouteIDCfgNextIP_Object = MibTableColumn
rcMplsTEExplicitRouteIDCfgNextIP = _RcMplsTEExplicitRouteIDCfgNextIP_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 6, 1, 3),
    _RcMplsTEExplicitRouteIDCfgNextIP_Type()
)
rcMplsTEExplicitRouteIDCfgNextIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteIDCfgNextIP.setStatus("current")


class _RcMplsTEExplicitRouteIDCfgHopType_Type(Integer32):
    """Custom type rcMplsTEExplicitRouteIDCfgHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_RcMplsTEExplicitRouteIDCfgHopType_Type.__name__ = "Integer32"
_RcMplsTEExplicitRouteIDCfgHopType_Object = MibTableColumn
rcMplsTEExplicitRouteIDCfgHopType = _RcMplsTEExplicitRouteIDCfgHopType_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 6, 1, 4),
    _RcMplsTEExplicitRouteIDCfgHopType_Type()
)
rcMplsTEExplicitRouteIDCfgHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteIDCfgHopType.setStatus("current")


class _RcMplsTEExplicitRouteIDCfgHopAttribute_Type(Integer32):
    """Custom type rcMplsTEExplicitRouteIDCfgHopAttribute based on Integer32"""
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
        *(("strict", 1),
          ("loose", 2),
          ("interface", 3),
          ("routerid", 4))
    )


_RcMplsTEExplicitRouteIDCfgHopAttribute_Type.__name__ = "Integer32"
_RcMplsTEExplicitRouteIDCfgHopAttribute_Object = MibTableColumn
rcMplsTEExplicitRouteIDCfgHopAttribute = _RcMplsTEExplicitRouteIDCfgHopAttribute_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 6, 1, 5),
    _RcMplsTEExplicitRouteIDCfgHopAttribute_Type()
)
rcMplsTEExplicitRouteIDCfgHopAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteIDCfgHopAttribute.setStatus("current")
_RcMplsTEExplicitRouteIDCfgRowSta_Type = RowStatus
_RcMplsTEExplicitRouteIDCfgRowSta_Object = MibTableColumn
rcMplsTEExplicitRouteIDCfgRowSta = _RcMplsTEExplicitRouteIDCfgRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 6, 1, 6),
    _RcMplsTEExplicitRouteIDCfgRowSta_Type()
)
rcMplsTEExplicitRouteIDCfgRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEExplicitRouteIDCfgRowSta.setStatus("current")
_RcMplsTEHotStandbyCfgTable_Object = MibTable
rcMplsTEHotStandbyCfgTable = _RcMplsTEHotStandbyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 7)
)
if mibBuilder.loadTexts:
    rcMplsTEHotStandbyCfgTable.setStatus("current")
_RcMplsTEHotStandbyCfgEntry_Object = MibTableRow
rcMplsTEHotStandbyCfgEntry = _RcMplsTEHotStandbyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 7, 1)
)
rcMplsTEHotStandbyCfgEntry.setIndexNames(
    (0, "RC-MPLS-TE-MIB", "rcMplsTEHotStandbyCfgTunnelID"),
    (0, "RC-MPLS-TE-MIB", "rcMplsTEHotStandbyCfgProtOptNo"),
)
if mibBuilder.loadTexts:
    rcMplsTEHotStandbyCfgEntry.setStatus("current")


class _RcMplsTEHotStandbyCfgTunnelID_Type(Unsigned32):
    """Custom type rcMplsTEHotStandbyCfgTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_RcMplsTEHotStandbyCfgTunnelID_Type.__name__ = "Unsigned32"
_RcMplsTEHotStandbyCfgTunnelID_Object = MibTableColumn
rcMplsTEHotStandbyCfgTunnelID = _RcMplsTEHotStandbyCfgTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 7, 1, 1),
    _RcMplsTEHotStandbyCfgTunnelID_Type()
)
rcMplsTEHotStandbyCfgTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEHotStandbyCfgTunnelID.setStatus("current")


class _RcMplsTEHotStandbyCfgProtOptNo_Type(Unsigned32):
    """Custom type rcMplsTEHotStandbyCfgProtOptNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RcMplsTEHotStandbyCfgProtOptNo_Type.__name__ = "Unsigned32"
_RcMplsTEHotStandbyCfgProtOptNo_Object = MibTableColumn
rcMplsTEHotStandbyCfgProtOptNo = _RcMplsTEHotStandbyCfgProtOptNo_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 7, 1, 2),
    _RcMplsTEHotStandbyCfgProtOptNo_Type()
)
rcMplsTEHotStandbyCfgProtOptNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTEHotStandbyCfgProtOptNo.setStatus("current")


class _RcMplsTEHotStandbyCfgPathType_Type(Integer32):
    """Custom type rcMplsTEHotStandbyCfgPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("explicitId", 2),
          ("explicitName", 3))
    )


_RcMplsTEHotStandbyCfgPathType_Type.__name__ = "Integer32"
_RcMplsTEHotStandbyCfgPathType_Object = MibTableColumn
rcMplsTEHotStandbyCfgPathType = _RcMplsTEHotStandbyCfgPathType_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 7, 1, 3),
    _RcMplsTEHotStandbyCfgPathType_Type()
)
rcMplsTEHotStandbyCfgPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEHotStandbyCfgPathType.setStatus("current")


class _RcMplsTEHotStandbyCfgExpPathName_Type(DisplayString):
    """Custom type rcMplsTEHotStandbyCfgExpPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_RcMplsTEHotStandbyCfgExpPathName_Type.__name__ = "DisplayString"
_RcMplsTEHotStandbyCfgExpPathName_Object = MibTableColumn
rcMplsTEHotStandbyCfgExpPathName = _RcMplsTEHotStandbyCfgExpPathName_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 7, 1, 4),
    _RcMplsTEHotStandbyCfgExpPathName_Type()
)
rcMplsTEHotStandbyCfgExpPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEHotStandbyCfgExpPathName.setStatus("current")


class _RcMplsTEHotStandbyCfgExpPathID_Type(Unsigned32):
    """Custom type rcMplsTEHotStandbyCfgExpPathID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcMplsTEHotStandbyCfgExpPathID_Type.__name__ = "Unsigned32"
_RcMplsTEHotStandbyCfgExpPathID_Object = MibTableColumn
rcMplsTEHotStandbyCfgExpPathID = _RcMplsTEHotStandbyCfgExpPathID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 7, 1, 5),
    _RcMplsTEHotStandbyCfgExpPathID_Type()
)
rcMplsTEHotStandbyCfgExpPathID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEHotStandbyCfgExpPathID.setStatus("current")
_RcMplsTEHotStandbyCfgRowSta_Type = RowStatus
_RcMplsTEHotStandbyCfgRowSta_Object = MibTableColumn
rcMplsTEHotStandbyCfgRowSta = _RcMplsTEHotStandbyCfgRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 7, 1, 6),
    _RcMplsTEHotStandbyCfgRowSta_Type()
)
rcMplsTEHotStandbyCfgRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTEHotStandbyCfgRowSta.setStatus("current")
_RcMplsTETunnelGroupCfgTable_Object = MibTable
rcMplsTETunnelGroupCfgTable = _RcMplsTETunnelGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 8)
)
if mibBuilder.loadTexts:
    rcMplsTETunnelGroupCfgTable.setStatus("current")
_RcMplsTETunnelGroupCfgEntry_Object = MibTableRow
rcMplsTETunnelGroupCfgEntry = _RcMplsTETunnelGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 8, 1)
)
rcMplsTETunnelGroupCfgEntry.setIndexNames(
    (0, "RC-MPLS-TE-MIB", "rcMplsTETunnelGroupCfgPrimaryTunnelID"),
)
if mibBuilder.loadTexts:
    rcMplsTETunnelGroupCfgEntry.setStatus("current")


class _RcMplsTETunnelGroupCfgPrimaryTunnelID_Type(Unsigned32):
    """Custom type rcMplsTETunnelGroupCfgPrimaryTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_RcMplsTETunnelGroupCfgPrimaryTunnelID_Type.__name__ = "Unsigned32"
_RcMplsTETunnelGroupCfgPrimaryTunnelID_Object = MibTableColumn
rcMplsTETunnelGroupCfgPrimaryTunnelID = _RcMplsTETunnelGroupCfgPrimaryTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 8, 1, 1),
    _RcMplsTETunnelGroupCfgPrimaryTunnelID_Type()
)
rcMplsTETunnelGroupCfgPrimaryTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMplsTETunnelGroupCfgPrimaryTunnelID.setStatus("current")


class _RcMplsTETunnelGroupCfgSecondaryTunnelID_Type(Unsigned32):
    """Custom type rcMplsTETunnelGroupCfgSecondaryTunnelID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_RcMplsTETunnelGroupCfgSecondaryTunnelID_Type.__name__ = "Unsigned32"
_RcMplsTETunnelGroupCfgSecondaryTunnelID_Object = MibTableColumn
rcMplsTETunnelGroupCfgSecondaryTunnelID = _RcMplsTETunnelGroupCfgSecondaryTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 8, 1, 2),
    _RcMplsTETunnelGroupCfgSecondaryTunnelID_Type()
)
rcMplsTETunnelGroupCfgSecondaryTunnelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelGroupCfgSecondaryTunnelID.setStatus("current")
_RcMplsTETunnelGroupCfgRowSta_Type = RowStatus
_RcMplsTETunnelGroupCfgRowSta_Object = MibTableColumn
rcMplsTETunnelGroupCfgRowSta = _RcMplsTETunnelGroupCfgRowSta_Object(
    (1, 3, 6, 1, 4, 1, 65000, 1, 8, 1, 3),
    _RcMplsTETunnelGroupCfgRowSta_Type()
)
rcMplsTETunnelGroupCfgRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMplsTETunnelGroupCfgRowSta.setStatus("current")
_RcMplsTeConformance_ObjectIdentity = ObjectIdentity
rcMplsTeConformance = _RcMplsTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 65000, 1, 9)
)
_RcMplsTeGroups_ObjectIdentity = ObjectIdentity
rcMplsTeGroups = _RcMplsTeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 65000, 1, 9, 1)
)

# Managed Objects groups


# Notification objects

rcMplsLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 65000, 1, 0, 1)
)
rcMplsLspUp.setObjects(
    ("RC-MPLS-TE-MIB", "rcMplsTunnelOperStatus")
)
if mibBuilder.loadTexts:
    rcMplsLspUp.setStatus(
        "current"
    )

rcMplsLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 65000, 1, 0, 2)
)
rcMplsLspDown.setObjects(
    ("RC-MPLS-TE-MIB", "rcMplsTunnelOperStatus")
)
if mibBuilder.loadTexts:
    rcMplsLspDown.setStatus(
        "current"
    )


# Notifications groups

rcMplsTeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 65000, 1, 9, 1, 8)
)
rcMplsTeNotificationGroup.setObjects(
      *(("RC-MPLS-TE-MIB", "rcMplsLspUp"),
        ("RC-MPLS-TE-MIB", "rcMplsLspDown"))
)
if mibBuilder.loadTexts:
    rcMplsTeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC-MPLS-TE-MIB",
    **{"rcMplsTeMIB": rcMplsTeMIB,
       "rcMplsTeNotifications": rcMplsTeNotifications,
       "rcMplsLspUp": rcMplsLspUp,
       "rcMplsLspDown": rcMplsLspDown,
       "rcMplsTETunnelCfgTable": rcMplsTETunnelCfgTable,
       "rcMplsTETunnelCfgEntry": rcMplsTETunnelCfgEntry,
       "rcMplsTETunnelCfgTunnelID": rcMplsTETunnelCfgTunnelID,
       "rcMplsTETunnelCfgEgressLSRId": rcMplsTETunnelCfgEgressLSRId,
       "rcMplsTETunnelCfgSetupPrio": rcMplsTETunnelCfgSetupPrio,
       "rcMplsTETunnelCfgHoldingPrio": rcMplsTETunnelCfgHoldingPrio,
       "rcMplsTETunnelCfgRecordRoute": rcMplsTETunnelCfgRecordRoute,
       "rcMplsTETunnelCfgBandwidth": rcMplsTETunnelCfgBandwidth,
       "rcMplsTETunnelCfgExplicitPathName": rcMplsTETunnelCfgExplicitPathName,
       "rcMplsTETunnelCfgExplicitPathID": rcMplsTETunnelCfgExplicitPathID,
       "rcMplsTETunnelCfgHSB": rcMplsTETunnelCfgHSB,
       "rcMplsTETunnelCfgHSBExplicitPathName": rcMplsTETunnelCfgHSBExplicitPathName,
       "rcMplsTETunnelCfgHSBExplicitPathID": rcMplsTETunnelCfgHSBExplicitPathID,
       "rcMplsTETunnelCfgRowSta": rcMplsTETunnelCfgRowSta,
       "rcMplsTunnelOperStatus": rcMplsTunnelOperStatus,
       "rcMplsTEPathOptCfgTable": rcMplsTEPathOptCfgTable,
       "rcMplsTEPathOptCfgEntry": rcMplsTEPathOptCfgEntry,
       "rcMplsTEPathOptCfgTunnelID": rcMplsTEPathOptCfgTunnelID,
       "rcMplsTEPathOptCfgNumber": rcMplsTEPathOptCfgNumber,
       "rcMplsTEPathOptCfgPathType": rcMplsTEPathOptCfgPathType,
       "rcMplsTEPathOptCfgExpPathName": rcMplsTEPathOptCfgExpPathName,
       "rcMplsTEPathOptCfgExpPathID": rcMplsTEPathOptCfgExpPathID,
       "rcMplsTEPathOptCfgRowSta": rcMplsTEPathOptCfgRowSta,
       "rcMplsTEExplicitPathNameCfgTable": rcMplsTEExplicitPathNameCfgTable,
       "rcMplsTEExplicitPathNameCfgEntry": rcMplsTEExplicitPathNameCfgEntry,
       "rcMplsTEExplicitPathNameCfgName": rcMplsTEExplicitPathNameCfgName,
       "rcMplsTEExplicitPathNameCfgRowSta": rcMplsTEExplicitPathNameCfgRowSta,
       "rcMplsTEExplicitPathIDCfgTable": rcMplsTEExplicitPathIDCfgTable,
       "rcMplsTEExplicitPathIDCfgEntry": rcMplsTEExplicitPathIDCfgEntry,
       "rcMplsTEExplicitPathIDCfgIdentifer": rcMplsTEExplicitPathIDCfgIdentifer,
       "rcMplsTEExplicitPathIDCfgRowSta": rcMplsTEExplicitPathIDCfgRowSta,
       "rcMplsTEExplicitRouteNameCfgTable": rcMplsTEExplicitRouteNameCfgTable,
       "rcMplsTEExplicitRouteNameCfgEntry": rcMplsTEExplicitRouteNameCfgEntry,
       "rcMplsTEExplicitRouteNameCfgName": rcMplsTEExplicitRouteNameCfgName,
       "rcMplsTEExplicitRouteNameCfgIndex": rcMplsTEExplicitRouteNameCfgIndex,
       "rcMplsTEExplicitRouteNameCfgNextIP": rcMplsTEExplicitRouteNameCfgNextIP,
       "rcMplsTEExplicitRouteNameCfgHopType": rcMplsTEExplicitRouteNameCfgHopType,
       "rcMplsTEExplicitRouteNameCfgHopAttribute": rcMplsTEExplicitRouteNameCfgHopAttribute,
       "rcMplsTEExplicitRouteNameCfgRowSta": rcMplsTEExplicitRouteNameCfgRowSta,
       "rcMplsTEExplicitRouteIDCfgTable": rcMplsTEExplicitRouteIDCfgTable,
       "rcMplsTEExplicitRouteIDCfgEntry": rcMplsTEExplicitRouteIDCfgEntry,
       "rcMplsTEExplicitRouteIDCfgIdentifer": rcMplsTEExplicitRouteIDCfgIdentifer,
       "rcMplsTEExplicitRouteIDCfgIndex": rcMplsTEExplicitRouteIDCfgIndex,
       "rcMplsTEExplicitRouteIDCfgNextIP": rcMplsTEExplicitRouteIDCfgNextIP,
       "rcMplsTEExplicitRouteIDCfgHopType": rcMplsTEExplicitRouteIDCfgHopType,
       "rcMplsTEExplicitRouteIDCfgHopAttribute": rcMplsTEExplicitRouteIDCfgHopAttribute,
       "rcMplsTEExplicitRouteIDCfgRowSta": rcMplsTEExplicitRouteIDCfgRowSta,
       "rcMplsTEHotStandbyCfgTable": rcMplsTEHotStandbyCfgTable,
       "rcMplsTEHotStandbyCfgEntry": rcMplsTEHotStandbyCfgEntry,
       "rcMplsTEHotStandbyCfgTunnelID": rcMplsTEHotStandbyCfgTunnelID,
       "rcMplsTEHotStandbyCfgProtOptNo": rcMplsTEHotStandbyCfgProtOptNo,
       "rcMplsTEHotStandbyCfgPathType": rcMplsTEHotStandbyCfgPathType,
       "rcMplsTEHotStandbyCfgExpPathName": rcMplsTEHotStandbyCfgExpPathName,
       "rcMplsTEHotStandbyCfgExpPathID": rcMplsTEHotStandbyCfgExpPathID,
       "rcMplsTEHotStandbyCfgRowSta": rcMplsTEHotStandbyCfgRowSta,
       "rcMplsTETunnelGroupCfgTable": rcMplsTETunnelGroupCfgTable,
       "rcMplsTETunnelGroupCfgEntry": rcMplsTETunnelGroupCfgEntry,
       "rcMplsTETunnelGroupCfgPrimaryTunnelID": rcMplsTETunnelGroupCfgPrimaryTunnelID,
       "rcMplsTETunnelGroupCfgSecondaryTunnelID": rcMplsTETunnelGroupCfgSecondaryTunnelID,
       "rcMplsTETunnelGroupCfgRowSta": rcMplsTETunnelGroupCfgRowSta,
       "rcMplsTeConformance": rcMplsTeConformance,
       "rcMplsTeGroups": rcMplsTeGroups,
       "rcMplsTeNotificationGroup": rcMplsTeNotificationGroup}
)
