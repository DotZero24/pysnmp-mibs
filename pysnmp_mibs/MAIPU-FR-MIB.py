# SNMP MIB module (MAIPU-FR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-FR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:00 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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

mpFrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrIfMib_ObjectIdentity = ObjectIdentity
frIfMib = _FrIfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1)
)
if mibBuilder.loadTexts:
    frIfMib.setStatus("current")
_FrConfTable_Object = MibTable
frConfTable = _FrConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    frConfTable.setStatus("current")
_FrConfEntry_Object = MibTableRow
frConfEntry = _FrConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 1, 1)
)
frConfEntry.setIndexNames(
    (0, "MAIPU-FR-MIB", "frConfIfIndex"),
)
if mibBuilder.loadTexts:
    frConfEntry.setStatus("current")
_FrConfIfIndex_Type = Integer32
_FrConfIfIndex_Object = MibTableColumn
frConfIfIndex = _FrConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 1, 1, 1),
    _FrConfIfIndex_Type()
)
frConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frConfIfIndex.setStatus("current")


class _FrConfIfType_Type(Integer32):
    """Custom type frConfIfType based on Integer32"""
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
        *(("dte", 1),
          ("dce", 2),
          ("nni", 3))
    )


_FrConfIfType_Type.__name__ = "Integer32"
_FrConfIfType_Object = MibTableColumn
frConfIfType = _FrConfIfType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 1, 1, 2),
    _FrConfIfType_Type()
)
frConfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frConfIfType.setStatus("current")
_FrConfIfStatus_Type = RowStatus
_FrConfIfStatus_Object = MibTableColumn
frConfIfStatus = _FrConfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 1, 1, 3),
    _FrConfIfStatus_Type()
)
frConfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frConfIfStatus.setStatus("current")
_FrLmiConfTable_Object = MibTable
frLmiConfTable = _FrLmiConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    frLmiConfTable.setStatus("current")
_FrLmiConfEntry_Object = MibTableRow
frLmiConfEntry = _FrLmiConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1)
)
frLmiConfEntry.setIndexNames(
    (0, "MAIPU-FR-MIB", "frLmiConfIfIndex"),
)
if mibBuilder.loadTexts:
    frLmiConfEntry.setStatus("current")
_FrLmiConfIfIndex_Type = Integer32
_FrLmiConfIfIndex_Object = MibTableColumn
frLmiConfIfIndex = _FrLmiConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 1),
    _FrLmiConfIfIndex_Type()
)
frLmiConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLmiConfIfIndex.setStatus("current")


class _FrLmiType_Type(Integer32):
    """Custom type frLmiType based on Integer32"""
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
        *(("ansi", 1),
          ("q933a", 2),
          ("lmi", 3))
    )


_FrLmiType_Type.__name__ = "Integer32"
_FrLmiType_Object = MibTableColumn
frLmiType = _FrLmiType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 2),
    _FrLmiType_Type()
)
frLmiType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frLmiType.setStatus("current")


class _FrLmiN391Dte_Type(Integer32):
    """Custom type frLmiN391Dte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrLmiN391Dte_Type.__name__ = "Integer32"
_FrLmiN391Dte_Object = MibTableColumn
frLmiN391Dte = _FrLmiN391Dte_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 3),
    _FrLmiN391Dte_Type()
)
frLmiN391Dte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frLmiN391Dte.setStatus("current")


class _FrLmiN392Dte_Type(Integer32):
    """Custom type frLmiN392Dte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLmiN392Dte_Type.__name__ = "Integer32"
_FrLmiN392Dte_Object = MibTableColumn
frLmiN392Dte = _FrLmiN392Dte_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 4),
    _FrLmiN392Dte_Type()
)
frLmiN392Dte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frLmiN392Dte.setStatus("current")


class _FrLmiN393Dte_Type(Integer32):
    """Custom type frLmiN393Dte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLmiN393Dte_Type.__name__ = "Integer32"
_FrLmiN393Dte_Object = MibTableColumn
frLmiN393Dte = _FrLmiN393Dte_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 5),
    _FrLmiN393Dte_Type()
)
frLmiN393Dte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frLmiN393Dte.setStatus("current")


class _FrLmiN392Dce_Type(Integer32):
    """Custom type frLmiN392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLmiN392Dce_Type.__name__ = "Integer32"
_FrLmiN392Dce_Object = MibTableColumn
frLmiN392Dce = _FrLmiN392Dce_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 6),
    _FrLmiN392Dce_Type()
)
frLmiN392Dce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frLmiN392Dce.setStatus("current")


class _FrLmiN393Dce_Type(Integer32):
    """Custom type frLmiN393Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLmiN393Dce_Type.__name__ = "Integer32"
_FrLmiN393Dce_Object = MibTableColumn
frLmiN393Dce = _FrLmiN393Dce_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 7),
    _FrLmiN393Dce_Type()
)
frLmiN393Dce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frLmiN393Dce.setStatus("current")


class _FrLmiT392Dce_Type(Integer32):
    """Custom type frLmiT392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrLmiT392Dce_Type.__name__ = "Integer32"
_FrLmiT392Dce_Object = MibTableColumn
frLmiT392Dce = _FrLmiT392Dce_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 8),
    _FrLmiT392Dce_Type()
)
frLmiT392Dce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frLmiT392Dce.setStatus("current")


class _FrLmiKeepalive_Type(Integer32):
    """Custom type frLmiKeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FrLmiKeepalive_Type.__name__ = "Integer32"
_FrLmiKeepalive_Object = MibTableColumn
frLmiKeepalive = _FrLmiKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 9),
    _FrLmiKeepalive_Type()
)
frLmiKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frLmiKeepalive.setStatus("current")
_FrLmiConfStatus_Type = RowStatus
_FrLmiConfStatus_Object = MibTableColumn
frLmiConfStatus = _FrLmiConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 2, 1, 10),
    _FrLmiConfStatus_Type()
)
frLmiConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frLmiConfStatus.setStatus("current")
_FrLmiStatTable_Object = MibTable
frLmiStatTable = _FrLmiStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    frLmiStatTable.setStatus("current")
_FrLmiStatEntry_Object = MibTableRow
frLmiStatEntry = _FrLmiStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 3, 1)
)
frLmiStatEntry.setIndexNames(
    (0, "MAIPU-FR-MIB", "frLmiStatIfIndex"),
)
if mibBuilder.loadTexts:
    frLmiStatEntry.setStatus("current")
_FrLmiStatIfIndex_Type = Integer32
_FrLmiStatIfIndex_Object = MibTableColumn
frLmiStatIfIndex = _FrLmiStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 3, 1, 1),
    _FrLmiStatIfIndex_Type()
)
frLmiStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLmiStatIfIndex.setStatus("current")
_FrLmiStEnqSent_Type = Counter32
_FrLmiStEnqSent_Object = MibTableColumn
frLmiStEnqSent = _FrLmiStEnqSent_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 3, 1, 2),
    _FrLmiStEnqSent_Type()
)
frLmiStEnqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLmiStEnqSent.setStatus("current")
_FrLmiStMsgRecv_Type = Counter32
_FrLmiStMsgRecv_Object = MibTableColumn
frLmiStMsgRecv = _FrLmiStMsgRecv_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 3, 1, 3),
    _FrLmiStMsgRecv_Type()
)
frLmiStMsgRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLmiStMsgRecv.setStatus("current")
_FrLmiStTimeout_Type = Counter32
_FrLmiStTimeout_Object = MibTableColumn
frLmiStTimeout = _FrLmiStTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 3, 1, 4),
    _FrLmiStTimeout_Type()
)
frLmiStTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLmiStTimeout.setStatus("current")
_FrLmiStEnqRecv_Type = Counter32
_FrLmiStEnqRecv_Object = MibTableColumn
frLmiStEnqRecv = _FrLmiStEnqRecv_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 3, 1, 5),
    _FrLmiStEnqRecv_Type()
)
frLmiStEnqRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLmiStEnqRecv.setStatus("current")
_FrLmiStMsgSent_Type = Counter32
_FrLmiStMsgSent_Object = MibTableColumn
frLmiStMsgSent = _FrLmiStMsgSent_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 3, 1, 6),
    _FrLmiStMsgSent_Type()
)
frLmiStMsgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLmiStMsgSent.setStatus("current")
_FrLmiStEnqTimeout_Type = Counter32
_FrLmiStEnqTimeout_Object = MibTableColumn
frLmiStEnqTimeout = _FrLmiStEnqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 3, 1, 7),
    _FrLmiStEnqTimeout_Type()
)
frLmiStEnqTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLmiStEnqTimeout.setStatus("current")
_FrInarpConfTable_Object = MibTable
frInarpConfTable = _FrInarpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 4)
)
if mibBuilder.loadTexts:
    frInarpConfTable.setStatus("current")
_FrInarpConfEntry_Object = MibTableRow
frInarpConfEntry = _FrInarpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 4, 1)
)
frInarpConfEntry.setIndexNames(
    (0, "MAIPU-FR-MIB", "frInarpConfIfIndex"),
)
if mibBuilder.loadTexts:
    frInarpConfEntry.setStatus("current")
_FrInarpConfIfIndex_Type = Integer32
_FrInarpConfIfIndex_Object = MibTableColumn
frInarpConfIfIndex = _FrInarpConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 4, 1, 1),
    _FrInarpConfIfIndex_Type()
)
frInarpConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frInarpConfIfIndex.setStatus("current")


class _FrInarpEnable_Type(Integer32):
    """Custom type frInarpEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FrInarpEnable_Type.__name__ = "Integer32"
_FrInarpEnable_Object = MibTableColumn
frInarpEnable = _FrInarpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 4, 1, 2),
    _FrInarpEnable_Type()
)
frInarpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frInarpEnable.setStatus("current")


class _FrInarpInterval_Type(Integer32):
    """Custom type frInarpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 300),
    )


_FrInarpInterval_Type.__name__ = "Integer32"
_FrInarpInterval_Object = MibTableColumn
frInarpInterval = _FrInarpInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 4, 1, 3),
    _FrInarpInterval_Type()
)
frInarpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frInarpInterval.setStatus("current")


class _FrInarpUpdate_Type(Integer32):
    """Custom type frInarpUpdate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FrInarpUpdate_Type.__name__ = "Integer32"
_FrInarpUpdate_Object = MibTableColumn
frInarpUpdate = _FrInarpUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 4, 1, 4),
    _FrInarpUpdate_Type()
)
frInarpUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frInarpUpdate.setStatus("current")
_FrInarpStatus_Type = RowStatus
_FrInarpStatus_Object = MibTableColumn
frInarpStatus = _FrInarpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 4, 1, 5),
    _FrInarpStatus_Type()
)
frInarpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frInarpStatus.setStatus("current")
_FrInarpStatTable_Object = MibTable
frInarpStatTable = _FrInarpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 5)
)
if mibBuilder.loadTexts:
    frInarpStatTable.setStatus("current")
_FrInarpStatEntry_Object = MibTableRow
frInarpStatEntry = _FrInarpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 5, 1)
)
frInarpStatEntry.setIndexNames(
    (0, "MAIPU-FR-MIB", "frInarpConfIfIndex"),
)
if mibBuilder.loadTexts:
    frInarpStatEntry.setStatus("current")
_FrInarpStatIfIndex_Type = Integer32
_FrInarpStatIfIndex_Object = MibTableColumn
frInarpStatIfIndex = _FrInarpStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 5, 1, 1),
    _FrInarpStatIfIndex_Type()
)
frInarpStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frInarpStatIfIndex.setStatus("current")
_FrInarpReqSent_Type = Counter32
_FrInarpReqSent_Object = MibTableColumn
frInarpReqSent = _FrInarpReqSent_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 5, 1, 2),
    _FrInarpReqSent_Type()
)
frInarpReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frInarpReqSent.setStatus("current")
_FrInarpReqRecv_Type = Counter32
_FrInarpReqRecv_Object = MibTableColumn
frInarpReqRecv = _FrInarpReqRecv_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 5, 1, 3),
    _FrInarpReqRecv_Type()
)
frInarpReqRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frInarpReqRecv.setStatus("current")
_FrInarpReplySent_Type = Counter32
_FrInarpReplySent_Object = MibTableColumn
frInarpReplySent = _FrInarpReplySent_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 5, 1, 4),
    _FrInarpReplySent_Type()
)
frInarpReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frInarpReplySent.setStatus("current")
_FrInarpReplyRecv_Type = Counter32
_FrInarpReplyRecv_Object = MibTableColumn
frInarpReplyRecv = _FrInarpReplyRecv_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 1, 5, 1, 5),
    _FrInarpReplyRecv_Type()
)
frInarpReplyRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frInarpReplyRecv.setStatus("current")
_FrPvcMib_ObjectIdentity = ObjectIdentity
frPvcMib = _FrPvcMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2)
)
if mibBuilder.loadTexts:
    frPvcMib.setStatus("current")
_FrPvcConfTable_Object = MibTable
frPvcConfTable = _FrPvcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    frPvcConfTable.setStatus("current")
_FrPvcConfEntry_Object = MibTableRow
frPvcConfEntry = _FrPvcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1)
)
frPvcConfEntry.setIndexNames(
    (0, "MAIPU-FR-MIB", "frPvcConfIfIndex"),
    (0, "MAIPU-FR-MIB", "frPvcConfDlci"),
)
if mibBuilder.loadTexts:
    frPvcConfEntry.setStatus("current")
_FrPvcConfIfIndex_Type = Integer32
_FrPvcConfIfIndex_Object = MibTableColumn
frPvcConfIfIndex = _FrPvcConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 1),
    _FrPvcConfIfIndex_Type()
)
frPvcConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcConfIfIndex.setStatus("current")


class _FrPvcConfDlci_Type(Integer32):
    """Custom type frPvcConfDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrPvcConfDlci_Type.__name__ = "Integer32"
_FrPvcConfDlci_Object = MibTableColumn
frPvcConfDlci = _FrPvcConfDlci_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 2),
    _FrPvcConfDlci_Type()
)
frPvcConfDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcConfDlci.setStatus("current")


class _FrPvcIntf_Type(DisplayString):
    """Custom type frPvcIntf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FrPvcIntf_Type.__name__ = "DisplayString"
_FrPvcIntf_Object = MibTableColumn
frPvcIntf = _FrPvcIntf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 3),
    _FrPvcIntf_Type()
)
frPvcIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcIntf.setStatus("current")


class _FrPvcUsage_Type(Integer32):
    """Custom type frPvcUsage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("switched", 2))
    )


_FrPvcUsage_Type.__name__ = "Integer32"
_FrPvcUsage_Object = MibTableColumn
frPvcUsage = _FrPvcUsage_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 4),
    _FrPvcUsage_Type()
)
frPvcUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcUsage.setStatus("current")


class _FrPvcStatus_Type(Integer32):
    """Custom type frPvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inActive", 1),
          ("active", 2),
          ("static", 3),
          ("deleted", 4),
          ("defined", 5))
    )


_FrPvcStatus_Type.__name__ = "Integer32"
_FrPvcStatus_Object = MibTableColumn
frPvcStatus = _FrPvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 5),
    _FrPvcStatus_Type()
)
frPvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatus.setStatus("current")


class _FrPvcEncType_Type(Integer32):
    """Custom type frPvcEncType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("cisco", 2))
    )


_FrPvcEncType_Type.__name__ = "Integer32"
_FrPvcEncType_Object = MibTableColumn
frPvcEncType = _FrPvcEncType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 6),
    _FrPvcEncType_Type()
)
frPvcEncType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcEncType.setStatus("current")
_FrPvcMapIp_Type = IpAddress
_FrPvcMapIp_Object = MibTableColumn
frPvcMapIp = _FrPvcMapIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 7),
    _FrPvcMapIp_Type()
)
frPvcMapIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcMapIp.setStatus("current")


class _FrPvcMapType_Type(Integer32):
    """Custom type frPvcMapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_FrPvcMapType_Type.__name__ = "Integer32"
_FrPvcMapType_Object = MibTableColumn
frPvcMapType = _FrPvcMapType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 8),
    _FrPvcMapType_Type()
)
frPvcMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcMapType.setStatus("current")


class _FrPvcRouteOutIntf_Type(DisplayString):
    """Custom type frPvcRouteOutIntf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FrPvcRouteOutIntf_Type.__name__ = "DisplayString"
_FrPvcRouteOutIntf_Object = MibTableColumn
frPvcRouteOutIntf = _FrPvcRouteOutIntf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 9),
    _FrPvcRouteOutIntf_Type()
)
frPvcRouteOutIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcRouteOutIntf.setStatus("current")
_FrPvcRouteOutDlci_Type = Integer32
_FrPvcRouteOutDlci_Object = MibTableColumn
frPvcRouteOutDlci = _FrPvcRouteOutDlci_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 10),
    _FrPvcRouteOutDlci_Type()
)
frPvcRouteOutDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcRouteOutDlci.setStatus("current")


class _FrPvcRouteStatus_Type(Integer32):
    """Custom type frPvcRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("static", 3))
    )


_FrPvcRouteStatus_Type.__name__ = "Integer32"
_FrPvcRouteStatus_Object = MibTableColumn
frPvcRouteStatus = _FrPvcRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 11),
    _FrPvcRouteStatus_Type()
)
frPvcRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcRouteStatus.setStatus("current")


class _FrPvcBroadcast_Type(Integer32):
    """Custom type frPvcBroadcast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FrPvcBroadcast_Type.__name__ = "Integer32"
_FrPvcBroadcast_Object = MibTableColumn
frPvcBroadcast = _FrPvcBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 12),
    _FrPvcBroadcast_Type()
)
frPvcBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcBroadcast.setStatus("current")


class _FrPvcNoInarpIp_Type(Integer32):
    """Custom type frPvcNoInarpIp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FrPvcNoInarpIp_Type.__name__ = "Integer32"
_FrPvcNoInarpIp_Object = MibTableColumn
frPvcNoInarpIp = _FrPvcNoInarpIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 13),
    _FrPvcNoInarpIp_Type()
)
frPvcNoInarpIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcNoInarpIp.setStatus("current")


class _FrPvcGetFromDce_Type(Integer32):
    """Custom type frPvcGetFromDce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FrPvcGetFromDce_Type.__name__ = "Integer32"
_FrPvcGetFromDce_Object = MibTableColumn
frPvcGetFromDce = _FrPvcGetFromDce_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 14),
    _FrPvcGetFromDce_Type()
)
frPvcGetFromDce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcGetFromDce.setStatus("current")
_FrPvcConfTableStatus_Type = RowStatus
_FrPvcConfTableStatus_Object = MibTableColumn
frPvcConfTableStatus = _FrPvcConfTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 1, 1, 15),
    _FrPvcConfTableStatus_Type()
)
frPvcConfTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcConfTableStatus.setStatus("current")
_FrPvcStaticTable_Object = MibTable
frPvcStaticTable = _FrPvcStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2)
)
if mibBuilder.loadTexts:
    frPvcStaticTable.setStatus("current")
_FrPvcStaticEntry_Object = MibTableRow
frPvcStaticEntry = _FrPvcStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1)
)
frPvcStaticEntry.setIndexNames(
    (0, "MAIPU-FR-MIB", "frPvcStatIfIndex"),
    (0, "MAIPU-FR-MIB", "frPvcStatDlci"),
)
if mibBuilder.loadTexts:
    frPvcStaticEntry.setStatus("current")
_FrPvcStatIfIndex_Type = Integer32
_FrPvcStatIfIndex_Object = MibTableColumn
frPvcStatIfIndex = _FrPvcStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 1),
    _FrPvcStatIfIndex_Type()
)
frPvcStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatIfIndex.setStatus("current")


class _FrPvcStatDlci_Type(Integer32):
    """Custom type frPvcStatDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrPvcStatDlci_Type.__name__ = "Integer32"
_FrPvcStatDlci_Object = MibTableColumn
frPvcStatDlci = _FrPvcStatDlci_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 2),
    _FrPvcStatDlci_Type()
)
frPvcStatDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatDlci.setStatus("current")
_FrPvcStatInPkts_Type = Counter32
_FrPvcStatInPkts_Object = MibTableColumn
frPvcStatInPkts = _FrPvcStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 3),
    _FrPvcStatInPkts_Type()
)
frPvcStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatInPkts.setStatus("current")
_FrPvcStatOutPkts_Type = Counter32
_FrPvcStatOutPkts_Object = MibTableColumn
frPvcStatOutPkts = _FrPvcStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 4),
    _FrPvcStatOutPkts_Type()
)
frPvcStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatOutPkts.setStatus("current")
_FrPvcStatInBytes_Type = Counter32
_FrPvcStatInBytes_Object = MibTableColumn
frPvcStatInBytes = _FrPvcStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 5),
    _FrPvcStatInBytes_Type()
)
frPvcStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatInBytes.setStatus("current")
_FrPvcStatOutBytes_Type = Counter32
_FrPvcStatOutBytes_Object = MibTableColumn
frPvcStatOutBytes = _FrPvcStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 6),
    _FrPvcStatOutBytes_Type()
)
frPvcStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatOutBytes.setStatus("current")
_FrPvcStatDroppedPkts_Type = Counter32
_FrPvcStatDroppedPkts_Object = MibTableColumn
frPvcStatDroppedPkts = _FrPvcStatDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 7),
    _FrPvcStatDroppedPkts_Type()
)
frPvcStatDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatDroppedPkts.setStatus("current")
_FrPvcStatInFecnPkts_Type = Counter32
_FrPvcStatInFecnPkts_Object = MibTableColumn
frPvcStatInFecnPkts = _FrPvcStatInFecnPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 8),
    _FrPvcStatInFecnPkts_Type()
)
frPvcStatInFecnPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatInFecnPkts.setStatus("current")
_FrPvcStatOutFecnPkts_Type = Counter32
_FrPvcStatOutFecnPkts_Object = MibTableColumn
frPvcStatOutFecnPkts = _FrPvcStatOutFecnPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 9),
    _FrPvcStatOutFecnPkts_Type()
)
frPvcStatOutFecnPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatOutFecnPkts.setStatus("current")
_FrPvcStatInBecnPkts_Type = Counter32
_FrPvcStatInBecnPkts_Object = MibTableColumn
frPvcStatInBecnPkts = _FrPvcStatInBecnPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 10),
    _FrPvcStatInBecnPkts_Type()
)
frPvcStatInBecnPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatInBecnPkts.setStatus("current")
_FrPvcStatOutBecnPkts_Type = Counter32
_FrPvcStatOutBecnPkts_Object = MibTableColumn
frPvcStatOutBecnPkts = _FrPvcStatOutBecnPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 11),
    _FrPvcStatOutBecnPkts_Type()
)
frPvcStatOutBecnPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatOutBecnPkts.setStatus("current")
_FrPvcStatInDePkts_Type = Counter32
_FrPvcStatInDePkts_Object = MibTableColumn
frPvcStatInDePkts = _FrPvcStatInDePkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 12),
    _FrPvcStatInDePkts_Type()
)
frPvcStatInDePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatInDePkts.setStatus("current")
_FrPvcStatOutDePkts_Type = Counter32
_FrPvcStatOutDePkts_Object = MibTableColumn
frPvcStatOutDePkts = _FrPvcStatOutDePkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 13),
    _FrPvcStatOutDePkts_Type()
)
frPvcStatOutDePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatOutDePkts.setStatus("current")
_FrPvcSwitchPkts_Type = Counter32
_FrPvcSwitchPkts_Object = MibTableColumn
frPvcSwitchPkts = _FrPvcSwitchPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 6, 2, 2, 1, 14),
    _FrPvcSwitchPkts_Type()
)
frPvcSwitchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcSwitchPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-FR-MIB",
    **{"mpFrMib": mpFrMib,
       "frIfMib": frIfMib,
       "frConfTable": frConfTable,
       "frConfEntry": frConfEntry,
       "frConfIfIndex": frConfIfIndex,
       "frConfIfType": frConfIfType,
       "frConfIfStatus": frConfIfStatus,
       "frLmiConfTable": frLmiConfTable,
       "frLmiConfEntry": frLmiConfEntry,
       "frLmiConfIfIndex": frLmiConfIfIndex,
       "frLmiType": frLmiType,
       "frLmiN391Dte": frLmiN391Dte,
       "frLmiN392Dte": frLmiN392Dte,
       "frLmiN393Dte": frLmiN393Dte,
       "frLmiN392Dce": frLmiN392Dce,
       "frLmiN393Dce": frLmiN393Dce,
       "frLmiT392Dce": frLmiT392Dce,
       "frLmiKeepalive": frLmiKeepalive,
       "frLmiConfStatus": frLmiConfStatus,
       "frLmiStatTable": frLmiStatTable,
       "frLmiStatEntry": frLmiStatEntry,
       "frLmiStatIfIndex": frLmiStatIfIndex,
       "frLmiStEnqSent": frLmiStEnqSent,
       "frLmiStMsgRecv": frLmiStMsgRecv,
       "frLmiStTimeout": frLmiStTimeout,
       "frLmiStEnqRecv": frLmiStEnqRecv,
       "frLmiStMsgSent": frLmiStMsgSent,
       "frLmiStEnqTimeout": frLmiStEnqTimeout,
       "frInarpConfTable": frInarpConfTable,
       "frInarpConfEntry": frInarpConfEntry,
       "frInarpConfIfIndex": frInarpConfIfIndex,
       "frInarpEnable": frInarpEnable,
       "frInarpInterval": frInarpInterval,
       "frInarpUpdate": frInarpUpdate,
       "frInarpStatus": frInarpStatus,
       "frInarpStatTable": frInarpStatTable,
       "frInarpStatEntry": frInarpStatEntry,
       "frInarpStatIfIndex": frInarpStatIfIndex,
       "frInarpReqSent": frInarpReqSent,
       "frInarpReqRecv": frInarpReqRecv,
       "frInarpReplySent": frInarpReplySent,
       "frInarpReplyRecv": frInarpReplyRecv,
       "frPvcMib": frPvcMib,
       "frPvcConfTable": frPvcConfTable,
       "frPvcConfEntry": frPvcConfEntry,
       "frPvcConfIfIndex": frPvcConfIfIndex,
       "frPvcConfDlci": frPvcConfDlci,
       "frPvcIntf": frPvcIntf,
       "frPvcUsage": frPvcUsage,
       "frPvcStatus": frPvcStatus,
       "frPvcEncType": frPvcEncType,
       "frPvcMapIp": frPvcMapIp,
       "frPvcMapType": frPvcMapType,
       "frPvcRouteOutIntf": frPvcRouteOutIntf,
       "frPvcRouteOutDlci": frPvcRouteOutDlci,
       "frPvcRouteStatus": frPvcRouteStatus,
       "frPvcBroadcast": frPvcBroadcast,
       "frPvcNoInarpIp": frPvcNoInarpIp,
       "frPvcGetFromDce": frPvcGetFromDce,
       "frPvcConfTableStatus": frPvcConfTableStatus,
       "frPvcStaticTable": frPvcStaticTable,
       "frPvcStaticEntry": frPvcStaticEntry,
       "frPvcStatIfIndex": frPvcStatIfIndex,
       "frPvcStatDlci": frPvcStatDlci,
       "frPvcStatInPkts": frPvcStatInPkts,
       "frPvcStatOutPkts": frPvcStatOutPkts,
       "frPvcStatInBytes": frPvcStatInBytes,
       "frPvcStatOutBytes": frPvcStatOutBytes,
       "frPvcStatDroppedPkts": frPvcStatDroppedPkts,
       "frPvcStatInFecnPkts": frPvcStatInFecnPkts,
       "frPvcStatOutFecnPkts": frPvcStatOutFecnPkts,
       "frPvcStatInBecnPkts": frPvcStatInBecnPkts,
       "frPvcStatOutBecnPkts": frPvcStatOutBecnPkts,
       "frPvcStatInDePkts": frPvcStatInDePkts,
       "frPvcStatOutDePkts": frPvcStatOutDePkts,
       "frPvcSwitchPkts": frPvcSwitchPkts}
)
