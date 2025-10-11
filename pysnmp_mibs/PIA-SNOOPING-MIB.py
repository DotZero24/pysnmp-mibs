# SNMP MIB module (PIA-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/PIA-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:53 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 enterprises,
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
    "enterprises",
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

fspiasnp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9)
)
if mibBuilder.loadTexts:
    fspiasnp.setRevisions(
        ("2007-11-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPIASnpSystem_ObjectIdentity = ObjectIdentity
fsPIASnpSystem = _FsPIASnpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1)
)


class _FsPIASnoopingSystemControl_Type(Integer32):
    """Custom type fsPIASnoopingSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsPIASnoopingSystemControl_Type.__name__ = "Integer32"
_FsPIASnoopingSystemControl_Object = MibScalar
fsPIASnoopingSystemControl = _FsPIASnoopingSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 1),
    _FsPIASnoopingSystemControl_Type()
)
fsPIASnoopingSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPIASnoopingSystemControl.setStatus("current")


class _FsPIASnoopingAdminStatus_Type(Integer32):
    """Custom type fsPIASnoopingAdminStatus based on Integer32"""
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


_FsPIASnoopingAdminStatus_Type.__name__ = "Integer32"
_FsPIASnoopingAdminStatus_Object = MibScalar
fsPIASnoopingAdminStatus = _FsPIASnoopingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 2),
    _FsPIASnoopingAdminStatus_Type()
)
fsPIASnoopingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPIASnoopingAdminStatus.setStatus("current")


class _FsPIATraceOption_Type(Integer32):
    """Custom type fsPIATraceOption based on Integer32"""
    defaultValue = 8


_FsPIATraceOption_Type.__name__ = "Integer32"
_FsPIATraceOption_Object = MibScalar
fsPIATraceOption = _FsPIATraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 3),
    _FsPIATraceOption_Type()
)
fsPIATraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPIATraceOption.setStatus("current")


class _FsPIASessionTimeOut_Type(Integer32):
    """Custom type fsPIASessionTimeOut based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_FsPIASessionTimeOut_Type.__name__ = "Integer32"
_FsPIASessionTimeOut_Object = MibScalar
fsPIASessionTimeOut = _FsPIASessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 4),
    _FsPIASessionTimeOut_Type()
)
fsPIASessionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPIASessionTimeOut.setStatus("current")
_FsPIASnpSessionTable_Object = MibTable
fsPIASnpSessionTable = _FsPIASnpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 5)
)
if mibBuilder.loadTexts:
    fsPIASnpSessionTable.setStatus("current")
_FsPIASnpSessionEntry_Object = MibTableRow
fsPIASnpSessionEntry = _FsPIASnpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 5, 1)
)
fsPIASnpSessionEntry.setIndexNames(
    (0, "PIA-SNOOPING-MIB", "fsPIASnpSessionVlanId"),
    (0, "PIA-SNOOPING-MIB", "fsPIASnpSessionMacAddress"),
)
if mibBuilder.loadTexts:
    fsPIASnpSessionEntry.setStatus("current")


class _FsPIASnpSessionVlanId_Type(Integer32):
    """Custom type fsPIASnpSessionVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsPIASnpSessionVlanId_Type.__name__ = "Integer32"
_FsPIASnpSessionVlanId_Object = MibTableColumn
fsPIASnpSessionVlanId = _FsPIASnpSessionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 5, 1, 1),
    _FsPIASnpSessionVlanId_Type()
)
fsPIASnpSessionVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPIASnpSessionVlanId.setStatus("current")
_FsPIASnpSessionMacAddress_Type = MacAddress
_FsPIASnpSessionMacAddress_Object = MibTableColumn
fsPIASnpSessionMacAddress = _FsPIASnpSessionMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 5, 1, 2),
    _FsPIASnpSessionMacAddress_Type()
)
fsPIASnpSessionMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPIASnpSessionMacAddress.setStatus("current")
_FsPIASnpSessionPortId_Type = InterfaceIndex
_FsPIASnpSessionPortId_Object = MibTableColumn
fsPIASnpSessionPortId = _FsPIASnpSessionPortId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 5, 1, 3),
    _FsPIASnpSessionPortId_Type()
)
fsPIASnpSessionPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpSessionPortId.setStatus("current")


class _FsPIASnpSessionId_Type(Integer32):
    """Custom type fsPIASnpSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpSessionId_Type.__name__ = "Integer32"
_FsPIASnpSessionId_Object = MibTableColumn
fsPIASnpSessionId = _FsPIASnpSessionId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 1, 5, 1, 4),
    _FsPIASnpSessionId_Type()
)
fsPIASnpSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpSessionId.setStatus("current")
_FsPIASnpVlan_ObjectIdentity = ObjectIdentity
fsPIASnpVlan = _FsPIASnpVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2)
)
_FsPIASnpVlanTable_Object = MibTable
fsPIASnpVlanTable = _FsPIASnpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    fsPIASnpVlanTable.setStatus("current")
_FsPIASnpVlanEntry_Object = MibTableRow
fsPIASnpVlanEntry = _FsPIASnpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1)
)
fsPIASnpVlanEntry.setIndexNames(
    (0, "PIA-SNOOPING-MIB", "fsPIASnpContextId"),
    (0, "PIA-SNOOPING-MIB", "fsPIASnpVlanId"),
)
if mibBuilder.loadTexts:
    fsPIASnpVlanEntry.setStatus("current")


class _FsPIASnpContextId_Type(Integer32):
    """Custom type fsPIASnpContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPIASnpContextId_Type.__name__ = "Integer32"
_FsPIASnpContextId_Object = MibTableColumn
fsPIASnpContextId = _FsPIASnpContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 1),
    _FsPIASnpContextId_Type()
)
fsPIASnpContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPIASnpContextId.setStatus("current")


class _FsPIASnpVlanId_Type(Integer32):
    """Custom type fsPIASnpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsPIASnpVlanId_Type.__name__ = "Integer32"
_FsPIASnpVlanId_Object = MibTableColumn
fsPIASnpVlanId = _FsPIASnpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 2),
    _FsPIASnpVlanId_Type()
)
fsPIASnpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPIASnpVlanId.setStatus("current")


class _FsPIASnpVlanSnpStatus_Type(Integer32):
    """Custom type fsPIASnpVlanSnpStatus based on Integer32"""
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


_FsPIASnpVlanSnpStatus_Type.__name__ = "Integer32"
_FsPIASnpVlanSnpStatus_Object = MibTableColumn
fsPIASnpVlanSnpStatus = _FsPIASnpVlanSnpStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 3),
    _FsPIASnpVlanSnpStatus_Type()
)
fsPIASnpVlanSnpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPIASnpVlanSnpStatus.setStatus("current")


class _FsPIASnpVlanStatsRxPADI_Type(Integer32):
    """Custom type fsPIASnpVlanStatsRxPADI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpVlanStatsRxPADI_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsRxPADI_Object = MibTableColumn
fsPIASnpVlanStatsRxPADI = _FsPIASnpVlanStatsRxPADI_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 4),
    _FsPIASnpVlanStatsRxPADI_Type()
)
fsPIASnpVlanStatsRxPADI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsRxPADI.setStatus("current")


class _FsPIASnpVlanStatsRxPADO_Type(Integer32):
    """Custom type fsPIASnpVlanStatsRxPADO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpVlanStatsRxPADO_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsRxPADO_Object = MibTableColumn
fsPIASnpVlanStatsRxPADO = _FsPIASnpVlanStatsRxPADO_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 5),
    _FsPIASnpVlanStatsRxPADO_Type()
)
fsPIASnpVlanStatsRxPADO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsRxPADO.setStatus("current")


class _FsPIASnpVlanStatsRxPADR_Type(Integer32):
    """Custom type fsPIASnpVlanStatsRxPADR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpVlanStatsRxPADR_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsRxPADR_Object = MibTableColumn
fsPIASnpVlanStatsRxPADR = _FsPIASnpVlanStatsRxPADR_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 6),
    _FsPIASnpVlanStatsRxPADR_Type()
)
fsPIASnpVlanStatsRxPADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsRxPADR.setStatus("current")


class _FsPIASnpVlanStatsRxPADS_Type(Integer32):
    """Custom type fsPIASnpVlanStatsRxPADS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpVlanStatsRxPADS_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsRxPADS_Object = MibTableColumn
fsPIASnpVlanStatsRxPADS = _FsPIASnpVlanStatsRxPADS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 7),
    _FsPIASnpVlanStatsRxPADS_Type()
)
fsPIASnpVlanStatsRxPADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsRxPADS.setStatus("current")


class _FsPIASnpVlanStatsRxPADT_Type(Integer32):
    """Custom type fsPIASnpVlanStatsRxPADT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpVlanStatsRxPADT_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsRxPADT_Object = MibTableColumn
fsPIASnpVlanStatsRxPADT = _FsPIASnpVlanStatsRxPADT_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 8),
    _FsPIASnpVlanStatsRxPADT_Type()
)
fsPIASnpVlanStatsRxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsRxPADT.setStatus("current")


class _FsPIASnpVlanStatsTxPkt_Type(Integer32):
    """Custom type fsPIASnpVlanStatsTxPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpVlanStatsTxPkt_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsTxPkt_Object = MibTableColumn
fsPIASnpVlanStatsTxPkt = _FsPIASnpVlanStatsTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 9),
    _FsPIASnpVlanStatsTxPkt_Type()
)
fsPIASnpVlanStatsTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsTxPkt.setStatus("current")


class _FsPIASnpVlanStatsTxGenError_Type(Integer32):
    """Custom type fsPIASnpVlanStatsTxGenError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpVlanStatsTxGenError_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsTxGenError_Object = MibTableColumn
fsPIASnpVlanStatsTxGenError = _FsPIASnpVlanStatsTxGenError_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 10),
    _FsPIASnpVlanStatsTxGenError_Type()
)
fsPIASnpVlanStatsTxGenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsTxGenError.setStatus("current")


class _FsPIASnpVlanStatsDroppedResUntrusted_Type(Integer32):
    """Custom type fsPIASnpVlanStatsDroppedResUntrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpVlanStatsDroppedResUntrusted_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsDroppedResUntrusted_Object = MibTableColumn
fsPIASnpVlanStatsDroppedResUntrusted = _FsPIASnpVlanStatsDroppedResUntrusted_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 11),
    _FsPIASnpVlanStatsDroppedResUntrusted_Type()
)
fsPIASnpVlanStatsDroppedResUntrusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsDroppedResUntrusted.setStatus("current")


class _FsPIASnpVlanStatsDroppedReqTrusted_Type(Integer32):
    """Custom type fsPIASnpVlanStatsDroppedReqTrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPIASnpVlanStatsDroppedReqTrusted_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsDroppedReqTrusted_Object = MibTableColumn
fsPIASnpVlanStatsDroppedReqTrusted = _FsPIASnpVlanStatsDroppedReqTrusted_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 12),
    _FsPIASnpVlanStatsDroppedReqTrusted_Type()
)
fsPIASnpVlanStatsDroppedReqTrusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsDroppedReqTrusted.setStatus("current")


class _FsPIASnpVlanStatsDroppedPkt_Type(Integer32):
    """Custom type fsPIASnpVlanStatsDroppedPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPIASnpVlanStatsDroppedPkt_Type.__name__ = "Integer32"
_FsPIASnpVlanStatsDroppedPkt_Object = MibTableColumn
fsPIASnpVlanStatsDroppedPkt = _FsPIASnpVlanStatsDroppedPkt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 13),
    _FsPIASnpVlanStatsDroppedPkt_Type()
)
fsPIASnpVlanStatsDroppedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsDroppedPkt.setStatus("current")


class _FsPIASnpVlanStatsClear_Type(TruthValue):
    """Custom type fsPIASnpVlanStatsClear based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPIASnpVlanStatsClear_Type.__name__ = "TruthValue"
_FsPIASnpVlanStatsClear_Object = MibTableColumn
fsPIASnpVlanStatsClear = _FsPIASnpVlanStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 14),
    _FsPIASnpVlanStatsClear_Type()
)
fsPIASnpVlanStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPIASnpVlanStatsClear.setStatus("current")
_FsPIASnpRowStatus_Type = RowStatus
_FsPIASnpRowStatus_Object = MibTableColumn
fsPIASnpRowStatus = _FsPIASnpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 9, 2, 1, 1, 15),
    _FsPIASnpRowStatus_Type()
)
fsPIASnpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPIASnpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PIA-SNOOPING-MIB",
    **{"fspiasnp": fspiasnp,
       "fsPIASnpSystem": fsPIASnpSystem,
       "fsPIASnoopingSystemControl": fsPIASnoopingSystemControl,
       "fsPIASnoopingAdminStatus": fsPIASnoopingAdminStatus,
       "fsPIATraceOption": fsPIATraceOption,
       "fsPIASessionTimeOut": fsPIASessionTimeOut,
       "fsPIASnpSessionTable": fsPIASnpSessionTable,
       "fsPIASnpSessionEntry": fsPIASnpSessionEntry,
       "fsPIASnpSessionVlanId": fsPIASnpSessionVlanId,
       "fsPIASnpSessionMacAddress": fsPIASnpSessionMacAddress,
       "fsPIASnpSessionPortId": fsPIASnpSessionPortId,
       "fsPIASnpSessionId": fsPIASnpSessionId,
       "fsPIASnpVlan": fsPIASnpVlan,
       "fsPIASnpVlanTable": fsPIASnpVlanTable,
       "fsPIASnpVlanEntry": fsPIASnpVlanEntry,
       "fsPIASnpContextId": fsPIASnpContextId,
       "fsPIASnpVlanId": fsPIASnpVlanId,
       "fsPIASnpVlanSnpStatus": fsPIASnpVlanSnpStatus,
       "fsPIASnpVlanStatsRxPADI": fsPIASnpVlanStatsRxPADI,
       "fsPIASnpVlanStatsRxPADO": fsPIASnpVlanStatsRxPADO,
       "fsPIASnpVlanStatsRxPADR": fsPIASnpVlanStatsRxPADR,
       "fsPIASnpVlanStatsRxPADS": fsPIASnpVlanStatsRxPADS,
       "fsPIASnpVlanStatsRxPADT": fsPIASnpVlanStatsRxPADT,
       "fsPIASnpVlanStatsTxPkt": fsPIASnpVlanStatsTxPkt,
       "fsPIASnpVlanStatsTxGenError": fsPIASnpVlanStatsTxGenError,
       "fsPIASnpVlanStatsDroppedResUntrusted": fsPIASnpVlanStatsDroppedResUntrusted,
       "fsPIASnpVlanStatsDroppedReqTrusted": fsPIASnpVlanStatsDroppedReqTrusted,
       "fsPIASnpVlanStatsDroppedPkt": fsPIASnpVlanStatsDroppedPkt,
       "fsPIASnpVlanStatsClear": fsPIASnpVlanStatsClear,
       "fsPIASnpRowStatus": fsPIASnpRowStatus}
)
