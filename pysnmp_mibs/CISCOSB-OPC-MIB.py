# SNMP MIB module (CISCOSB-OPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ciscosb/CISCOSB-OPC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:41:51 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlOpc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248)
)
if mibBuilder.loadTexts:
    rlOpc.setRevisions(
        ("2024-01-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlOpcCapturePointTable_Object = MibTable
rlOpcCapturePointTable = _RlOpcCapturePointTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1)
)
if mibBuilder.loadTexts:
    rlOpcCapturePointTable.setStatus("current")
_RlOpcCapturePointEntry_Object = MibTableRow
rlOpcCapturePointEntry = _RlOpcCapturePointEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1)
)
rlOpcCapturePointEntry.setIndexNames(
    (0, "CISCOSB-OPC-MIB", "rlOpcName"),
)
if mibBuilder.loadTexts:
    rlOpcCapturePointEntry.setStatus("current")


class _RlOpcName_Type(DisplayString):
    """Custom type rlOpcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlOpcName_Type.__name__ = "DisplayString"
_RlOpcName_Object = MibTableColumn
rlOpcName = _RlOpcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 1),
    _RlOpcName_Type()
)
rlOpcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcName.setStatus("current")


class _RlOpcBufferType_Type(Integer32):
    """Custom type rlOpcBufferType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linear", 1),
          ("circular", 2))
    )


_RlOpcBufferType_Type.__name__ = "Integer32"
_RlOpcBufferType_Object = MibTableColumn
rlOpcBufferType = _RlOpcBufferType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 2),
    _RlOpcBufferType_Type()
)
rlOpcBufferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcBufferType.setStatus("current")
_RlOpcBufferSize_Type = Unsigned32
_RlOpcBufferSize_Object = MibTableColumn
rlOpcBufferSize = _RlOpcBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 3),
    _RlOpcBufferSize_Type()
)
rlOpcBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcBufferSize.setStatus("current")


class _RlOpcBufferUsed_Type(Unsigned32):
    """Custom type rlOpcBufferUsed based on Unsigned32"""
    defaultValue = 0


_RlOpcBufferUsed_Type.__name__ = "Unsigned32"
_RlOpcBufferUsed_Object = MibTableColumn
rlOpcBufferUsed = _RlOpcBufferUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 4),
    _RlOpcBufferUsed_Type()
)
rlOpcBufferUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOpcBufferUsed.setStatus("current")


class _RlOpcBufferPacketNum_Type(Unsigned32):
    """Custom type rlOpcBufferPacketNum based on Unsigned32"""
    defaultValue = 0


_RlOpcBufferPacketNum_Type.__name__ = "Unsigned32"
_RlOpcBufferPacketNum_Object = MibTableColumn
rlOpcBufferPacketNum = _RlOpcBufferPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 5),
    _RlOpcBufferPacketNum_Type()
)
rlOpcBufferPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOpcBufferPacketNum.setStatus("current")


class _RlOpcBufferPacketsDropped_Type(Unsigned32):
    """Custom type rlOpcBufferPacketsDropped based on Unsigned32"""
    defaultValue = 0


_RlOpcBufferPacketsDropped_Type.__name__ = "Unsigned32"
_RlOpcBufferPacketsDropped_Object = MibTableColumn
rlOpcBufferPacketsDropped = _RlOpcBufferPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 6),
    _RlOpcBufferPacketsDropped_Type()
)
rlOpcBufferPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOpcBufferPacketsDropped.setStatus("current")


class _RlOpcBufferPacketsPerSecond_Type(Unsigned32):
    """Custom type rlOpcBufferPacketsPerSecond based on Unsigned32"""
    defaultValue = 0


_RlOpcBufferPacketsPerSecond_Type.__name__ = "Unsigned32"
_RlOpcBufferPacketsPerSecond_Object = MibTableColumn
rlOpcBufferPacketsPerSecond = _RlOpcBufferPacketsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 7),
    _RlOpcBufferPacketsPerSecond_Type()
)
rlOpcBufferPacketsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOpcBufferPacketsPerSecond.setStatus("current")


class _RlOpcFilterType_Type(Integer32):
    """Custom type rlOpcFilterType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("match-none", 0),
          ("match-any", 1),
          ("match-access-list", 2))
    )


_RlOpcFilterType_Type.__name__ = "Integer32"
_RlOpcFilterType_Object = MibTableColumn
rlOpcFilterType = _RlOpcFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 8),
    _RlOpcFilterType_Type()
)
rlOpcFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcFilterType.setStatus("current")


class _RlOpcFilterAclName_Type(DisplayString):
    """Custom type rlOpcFilterAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlOpcFilterAclName_Type.__name__ = "DisplayString"
_RlOpcFilterAclName_Object = MibTableColumn
rlOpcFilterAclName = _RlOpcFilterAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 9),
    _RlOpcFilterAclName_Type()
)
rlOpcFilterAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcFilterAclName.setStatus("current")


class _RlOpcLimitDuration_Type(Unsigned32):
    """Custom type rlOpcLimitDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RlOpcLimitDuration_Type.__name__ = "Unsigned32"
_RlOpcLimitDuration_Object = MibTableColumn
rlOpcLimitDuration = _RlOpcLimitDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 10),
    _RlOpcLimitDuration_Type()
)
rlOpcLimitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcLimitDuration.setStatus("current")
if mibBuilder.loadTexts:
    rlOpcLimitDuration.setUnits("seconds")


class _RlOpcLimitNumOfPackets_Type(Unsigned32):
    """Custom type rlOpcLimitNumOfPackets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RlOpcLimitNumOfPackets_Type.__name__ = "Unsigned32"
_RlOpcLimitNumOfPackets_Object = MibTableColumn
rlOpcLimitNumOfPackets = _RlOpcLimitNumOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 11),
    _RlOpcLimitNumOfPackets_Type()
)
rlOpcLimitNumOfPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcLimitNumOfPackets.setStatus("current")


class _RlOpcLimitMaxPacketLen_Type(Unsigned32):
    """Custom type rlOpcLimitMaxPacketLen based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9500),
        ValueRangeConstraint(0, 0),
    )


_RlOpcLimitMaxPacketLen_Type.__name__ = "Unsigned32"
_RlOpcLimitMaxPacketLen_Object = MibTableColumn
rlOpcLimitMaxPacketLen = _RlOpcLimitMaxPacketLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 12),
    _RlOpcLimitMaxPacketLen_Type()
)
rlOpcLimitMaxPacketLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcLimitMaxPacketLen.setStatus("current")


class _RlOpcState_Type(Integer32):
    """Custom type rlOpcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RlOpcState_Type.__name__ = "Integer32"
_RlOpcState_Object = MibTableColumn
rlOpcState = _RlOpcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 13),
    _RlOpcState_Type()
)
rlOpcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOpcState.setStatus("current")
_RlOpcCapturePointRowStatus_Type = RowStatus
_RlOpcCapturePointRowStatus_Object = MibTableColumn
rlOpcCapturePointRowStatus = _RlOpcCapturePointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 1, 1, 14),
    _RlOpcCapturePointRowStatus_Type()
)
rlOpcCapturePointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOpcCapturePointRowStatus.setStatus("current")
_RlOpcInterfaceTable_Object = MibTable
rlOpcInterfaceTable = _RlOpcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 2)
)
if mibBuilder.loadTexts:
    rlOpcInterfaceTable.setStatus("current")
_RlOpcInterfaceEntry_Object = MibTableRow
rlOpcInterfaceEntry = _RlOpcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 2, 1)
)
rlOpcInterfaceEntry.setIndexNames(
    (0, "CISCOSB-OPC-MIB", "rlOpcInterfaceCaptureName"),
    (0, "CISCOSB-OPC-MIB", "rlOpcInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    rlOpcInterfaceEntry.setStatus("current")


class _RlOpcInterfaceCaptureName_Type(DisplayString):
    """Custom type rlOpcInterfaceCaptureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlOpcInterfaceCaptureName_Type.__name__ = "DisplayString"
_RlOpcInterfaceCaptureName_Object = MibTableColumn
rlOpcInterfaceCaptureName = _RlOpcInterfaceCaptureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 2, 1, 1),
    _RlOpcInterfaceCaptureName_Type()
)
rlOpcInterfaceCaptureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcInterfaceCaptureName.setStatus("current")
_RlOpcInterfaceIfIndex_Type = InterfaceIndexOrZero
_RlOpcInterfaceIfIndex_Object = MibTableColumn
rlOpcInterfaceIfIndex = _RlOpcInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 2, 1, 2),
    _RlOpcInterfaceIfIndex_Type()
)
rlOpcInterfaceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcInterfaceIfIndex.setStatus("current")


class _RlOpcInterfaceCaptureDirection_Type(Integer32):
    """Custom type rlOpcInterfaceCaptureDirection based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("in", 1),
          ("out", 2),
          ("both", 3))
    )


_RlOpcInterfaceCaptureDirection_Type.__name__ = "Integer32"
_RlOpcInterfaceCaptureDirection_Object = MibTableColumn
rlOpcInterfaceCaptureDirection = _RlOpcInterfaceCaptureDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 2, 1, 3),
    _RlOpcInterfaceCaptureDirection_Type()
)
rlOpcInterfaceCaptureDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcInterfaceCaptureDirection.setStatus("current")
_RlOpcInterfaceRowStatus_Type = RowStatus
_RlOpcInterfaceRowStatus_Object = MibTableColumn
rlOpcInterfaceRowStatus = _RlOpcInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 2, 1, 4),
    _RlOpcInterfaceRowStatus_Type()
)
rlOpcInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOpcInterfaceRowStatus.setStatus("current")
_RlOpcActionTable_Object = MibTable
rlOpcActionTable = _RlOpcActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 3)
)
if mibBuilder.loadTexts:
    rlOpcActionTable.setStatus("current")
_RlOpcActionEntry_Object = MibTableRow
rlOpcActionEntry = _RlOpcActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 3, 1)
)
rlOpcActionEntry.setIndexNames(
    (0, "CISCOSB-OPC-MIB", "rlOpcActionCaptureName"),
)
if mibBuilder.loadTexts:
    rlOpcActionEntry.setStatus("current")


class _RlOpcActionCaptureName_Type(DisplayString):
    """Custom type rlOpcActionCaptureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlOpcActionCaptureName_Type.__name__ = "DisplayString"
_RlOpcActionCaptureName_Object = MibTableColumn
rlOpcActionCaptureName = _RlOpcActionCaptureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 3, 1, 1),
    _RlOpcActionCaptureName_Type()
)
rlOpcActionCaptureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcActionCaptureName.setStatus("current")


class _RlOpcExportDestLocationType_Type(Integer32):
    """Custom type rlOpcExportDestLocationType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flash", 0),
          ("usb", 1))
    )


_RlOpcExportDestLocationType_Type.__name__ = "Integer32"
_RlOpcExportDestLocationType_Object = MibTableColumn
rlOpcExportDestLocationType = _RlOpcExportDestLocationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 3, 1, 2),
    _RlOpcExportDestLocationType_Type()
)
rlOpcExportDestLocationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcExportDestLocationType.setStatus("current")


class _RlOpcExportFileName_Type(OctetString):
    """Custom type rlOpcExportFileName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlOpcExportFileName_Type.__name__ = "OctetString"
_RlOpcExportFileName_Object = MibTableColumn
rlOpcExportFileName = _RlOpcExportFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 3, 1, 3),
    _RlOpcExportFileName_Type()
)
rlOpcExportFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcExportFileName.setStatus("current")


class _RlOpcAction_Type(Integer32):
    """Custom type rlOpcAction based on Integer32"""
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
        *(("start", 1),
          ("stop", 2),
          ("export", 3),
          ("clear", 4))
    )


_RlOpcAction_Type.__name__ = "Integer32"
_RlOpcAction_Object = MibTableColumn
rlOpcAction = _RlOpcAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 3, 1, 4),
    _RlOpcAction_Type()
)
rlOpcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcAction.setStatus("current")
_RlOpcActionRowStatus_Type = RowStatus
_RlOpcActionRowStatus_Object = MibTableColumn
rlOpcActionRowStatus = _RlOpcActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 3, 1, 5),
    _RlOpcActionRowStatus_Type()
)
rlOpcActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlOpcActionRowStatus.setStatus("current")


class _RlOpcCrashExportDestination_Type(Integer32):
    """Custom type rlOpcCrashExportDestination based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flash", 0),
          ("usb", 1))
    )


_RlOpcCrashExportDestination_Type.__name__ = "Integer32"
_RlOpcCrashExportDestination_Object = MibScalar
rlOpcCrashExportDestination = _RlOpcCrashExportDestination_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 5),
    _RlOpcCrashExportDestination_Type()
)
rlOpcCrashExportDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpcCrashExportDestination.setStatus("current")


class _RlOpcOperState_Type(Integer32):
    """Custom type rlOpcOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RlOpcOperState_Type.__name__ = "Integer32"
_RlOpcOperState_Object = MibScalar
rlOpcOperState = _RlOpcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 248, 6),
    _RlOpcOperState_Type()
)
rlOpcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOpcOperState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-OPC-MIB",
    **{"rlOpc": rlOpc,
       "rlOpcCapturePointTable": rlOpcCapturePointTable,
       "rlOpcCapturePointEntry": rlOpcCapturePointEntry,
       "rlOpcName": rlOpcName,
       "rlOpcBufferType": rlOpcBufferType,
       "rlOpcBufferSize": rlOpcBufferSize,
       "rlOpcBufferUsed": rlOpcBufferUsed,
       "rlOpcBufferPacketNum": rlOpcBufferPacketNum,
       "rlOpcBufferPacketsDropped": rlOpcBufferPacketsDropped,
       "rlOpcBufferPacketsPerSecond": rlOpcBufferPacketsPerSecond,
       "rlOpcFilterType": rlOpcFilterType,
       "rlOpcFilterAclName": rlOpcFilterAclName,
       "rlOpcLimitDuration": rlOpcLimitDuration,
       "rlOpcLimitNumOfPackets": rlOpcLimitNumOfPackets,
       "rlOpcLimitMaxPacketLen": rlOpcLimitMaxPacketLen,
       "rlOpcState": rlOpcState,
       "rlOpcCapturePointRowStatus": rlOpcCapturePointRowStatus,
       "rlOpcInterfaceTable": rlOpcInterfaceTable,
       "rlOpcInterfaceEntry": rlOpcInterfaceEntry,
       "rlOpcInterfaceCaptureName": rlOpcInterfaceCaptureName,
       "rlOpcInterfaceIfIndex": rlOpcInterfaceIfIndex,
       "rlOpcInterfaceCaptureDirection": rlOpcInterfaceCaptureDirection,
       "rlOpcInterfaceRowStatus": rlOpcInterfaceRowStatus,
       "rlOpcActionTable": rlOpcActionTable,
       "rlOpcActionEntry": rlOpcActionEntry,
       "rlOpcActionCaptureName": rlOpcActionCaptureName,
       "rlOpcExportDestLocationType": rlOpcExportDestLocationType,
       "rlOpcExportFileName": rlOpcExportFileName,
       "rlOpcAction": rlOpcAction,
       "rlOpcActionRowStatus": rlOpcActionRowStatus,
       "rlOpcCrashExportDestination": rlOpcCrashExportDestination,
       "rlOpcOperState": rlOpcOperState}
)
