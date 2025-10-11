# SNMP MIB module (ADTRAN-GENCSM2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENCSM2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:58 2025
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

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

(atmTrafficDescrParamIndex,
 atmVcCrossConnectHighIfIndex,
 atmVcCrossConnectHighVci,
 atmVcCrossConnectHighVpi,
 atmVcCrossConnectIndex,
 atmVcCrossConnectLowIfIndex,
 atmVcCrossConnectLowVci,
 atmVcCrossConnectLowVpi,
 atmVclVci,
 atmVclVpi,
 atmVpCrossConnectHighIfIndex,
 atmVpCrossConnectHighVpi,
 atmVpCrossConnectIndex,
 atmVpCrossConnectLowIfIndex,
 atmVpCrossConnectLowVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamIndex",
    "atmVcCrossConnectHighIfIndex",
    "atmVcCrossConnectHighVci",
    "atmVcCrossConnectHighVpi",
    "atmVcCrossConnectIndex",
    "atmVcCrossConnectLowIfIndex",
    "atmVcCrossConnectLowVci",
    "atmVcCrossConnectLowVpi",
    "atmVclVci",
    "atmVclVpi",
    "atmVpCrossConnectHighIfIndex",
    "atmVpCrossConnectHighVpi",
    "atmVpCrossConnectIndex",
    "atmVpCrossConnectLowIfIndex",
    "atmVpCrossConnectLowVpi",
    "atmVplVpi")

(AtmServiceCategory,
 AtmTrafficDescrParamIndex) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmServiceCategory",
    "AtmTrafficDescrParamIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

adGENCSM2ID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenCSMDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wan", 1),
          ("loop", 2))
    )



class AdGenCsmOamIdv2(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class AdGenCSMClassScheduling(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modifiedStrictPriority", 1),
          ("roundRobin", 2),
          ("strictPriority", 3))
    )



class AdGenCSMMonitorScope(TextualConvention, Integer32):
    status = "current"
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
        *(("shelf", 1),
          ("port", 2),
          ("vp", 3),
          ("vc", 4))
    )



class AdGenCSMMonitorCounterType(TextualConvention, Integer32):
    status = "current"
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
        *(("absolute", 1),
          ("cumulative", 2),
          ("average", 3),
          ("minimum", 4),
          ("maximum", 5),
          ("last", 6))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenCSMmg_ObjectIdentity = ObjectIdentity
adGenCSMmg = _AdGenCSMmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 36)
)
_AdGenCSMAtmExtension_ObjectIdentity = ObjectIdentity
adGenCSMAtmExtension = _AdGenCSMAtmExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4)
)
_AdGenCSMTrafficDescrTable_Object = MibTable
adGenCSMTrafficDescrTable = _AdGenCSMTrafficDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 1)
)
if mibBuilder.loadTexts:
    adGenCSMTrafficDescrTable.setStatus("current")
_AdGenCSMTrafficDescrEntry_Object = MibTableRow
adGenCSMTrafficDescrEntry = _AdGenCSMTrafficDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 1, 1)
)
adGenCSMTrafficDescrEntry.setIndexNames(
    (0, "ATM-MIB", "atmTrafficDescrParamIndex"),
)
if mibBuilder.loadTexts:
    adGenCSMTrafficDescrEntry.setStatus("current")
_AdGenCSMTrafficDescrName_Type = DisplayString
_AdGenCSMTrafficDescrName_Object = MibTableColumn
adGenCSMTrafficDescrName = _AdGenCSMTrafficDescrName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 1, 1, 1),
    _AdGenCSMTrafficDescrName_Type()
)
adGenCSMTrafficDescrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMTrafficDescrName.setStatus("current")
_AdGenCSMVpCrossConnectTable_Object = MibTable
adGenCSMVpCrossConnectTable = _AdGenCSMVpCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 2)
)
if mibBuilder.loadTexts:
    adGenCSMVpCrossConnectTable.setStatus("current")
_AdGenCSMVpCrossConnectEntry_Object = MibTableRow
adGenCSMVpCrossConnectEntry = _AdGenCSMVpCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 2, 1)
)
adGenCSMVpCrossConnectEntry.setIndexNames(
    (0, "ATM-MIB", "atmVpCrossConnectIndex"),
    (0, "ATM-MIB", "atmVpCrossConnectLowIfIndex"),
    (0, "ATM-MIB", "atmVpCrossConnectLowVpi"),
    (0, "ATM-MIB", "atmVpCrossConnectHighIfIndex"),
    (0, "ATM-MIB", "atmVpCrossConnectHighVpi"),
)
if mibBuilder.loadTexts:
    adGenCSMVpCrossConnectEntry.setStatus("current")
_AdGenCSMVpCrossConnectName_Type = DisplayString
_AdGenCSMVpCrossConnectName_Object = MibTableColumn
adGenCSMVpCrossConnectName = _AdGenCSMVpCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 2, 1, 1),
    _AdGenCSMVpCrossConnectName_Type()
)
adGenCSMVpCrossConnectName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVpCrossConnectName.setStatus("current")
_AdGenCSMVpCrossConnectStatus_Type = DisplayString
_AdGenCSMVpCrossConnectStatus_Object = MibTableColumn
adGenCSMVpCrossConnectStatus = _AdGenCSMVpCrossConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 2, 1, 2),
    _AdGenCSMVpCrossConnectStatus_Type()
)
adGenCSMVpCrossConnectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVpCrossConnectStatus.setStatus("current")
_AdGenCSMVcCrossConnectTable_Object = MibTable
adGenCSMVcCrossConnectTable = _AdGenCSMVcCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 3)
)
if mibBuilder.loadTexts:
    adGenCSMVcCrossConnectTable.setStatus("current")
_AdGenCSMVcCrossConnectEntry_Object = MibTableRow
adGenCSMVcCrossConnectEntry = _AdGenCSMVcCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 3, 1)
)
adGenCSMVcCrossConnectEntry.setIndexNames(
    (0, "ATM-MIB", "atmVcCrossConnectIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectLowIfIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectLowVpi"),
    (0, "ATM-MIB", "atmVcCrossConnectLowVci"),
    (0, "ATM-MIB", "atmVcCrossConnectHighIfIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectHighVpi"),
    (0, "ATM-MIB", "atmVcCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    adGenCSMVcCrossConnectEntry.setStatus("current")
_AdGenCSMVcCrossConnectName_Type = DisplayString
_AdGenCSMVcCrossConnectName_Object = MibTableColumn
adGenCSMVcCrossConnectName = _AdGenCSMVcCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 3, 1, 1),
    _AdGenCSMVcCrossConnectName_Type()
)
adGenCSMVcCrossConnectName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVcCrossConnectName.setStatus("current")
_AdGenCSMVcCrossConnectStatus_Type = DisplayString
_AdGenCSMVcCrossConnectStatus_Object = MibTableColumn
adGenCSMVcCrossConnectStatus = _AdGenCSMVcCrossConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 3, 1, 2),
    _AdGenCSMVcCrossConnectStatus_Type()
)
adGenCSMVcCrossConnectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVcCrossConnectStatus.setStatus("current")
_AdGenCSMVplTable_Object = MibTable
adGenCSMVplTable = _AdGenCSMVplTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4)
)
if mibBuilder.loadTexts:
    adGenCSMVplTable.setStatus("current")
_AdGenCSMVplEntry_Object = MibTableRow
adGenCSMVplEntry = _AdGenCSMVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1)
)
adGenCSMVplEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    adGenCSMVplEntry.setStatus("current")
_AdGenCSMVplDisableAisRdiGeneration_Type = TruthValue
_AdGenCSMVplDisableAisRdiGeneration_Object = MibTableColumn
adGenCSMVplDisableAisRdiGeneration = _AdGenCSMVplDisableAisRdiGeneration_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 1),
    _AdGenCSMVplDisableAisRdiGeneration_Type()
)
adGenCSMVplDisableAisRdiGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVplDisableAisRdiGeneration.setStatus("current")
_AdGenCSMVplDisablePolicing_Type = TruthValue
_AdGenCSMVplDisablePolicing_Object = MibTableColumn
adGenCSMVplDisablePolicing = _AdGenCSMVplDisablePolicing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 2),
    _AdGenCSMVplDisablePolicing_Type()
)
adGenCSMVplDisablePolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVplDisablePolicing.setStatus("current")
_AdGenCSMVplDisableCAC_Type = TruthValue
_AdGenCSMVplDisableCAC_Object = MibTableColumn
adGenCSMVplDisableCAC = _AdGenCSMVplDisableCAC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 3),
    _AdGenCSMVplDisableCAC_Type()
)
adGenCSMVplDisableCAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVplDisableCAC.setStatus("current")


class _AdGenCSMVplResetATMStats_Type(Integer32):
    """Custom type adGenCSMVplResetATMStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenCSMVplResetATMStats_Type.__name__ = "Integer32"
_AdGenCSMVplResetATMStats_Object = MibTableColumn
adGenCSMVplResetATMStats = _AdGenCSMVplResetATMStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 4),
    _AdGenCSMVplResetATMStats_Type()
)
adGenCSMVplResetATMStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVplResetATMStats.setStatus("current")
_AdGenCSMVplTxCells_Type = Counter32
_AdGenCSMVplTxCells_Object = MibTableColumn
adGenCSMVplTxCells = _AdGenCSMVplTxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 5),
    _AdGenCSMVplTxCells_Type()
)
adGenCSMVplTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplTxCells.setStatus("current")
_AdGenCSMVplRxCells_Type = Counter32
_AdGenCSMVplRxCells_Object = MibTableColumn
adGenCSMVplRxCells = _AdGenCSMVplRxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 6),
    _AdGenCSMVplRxCells_Type()
)
adGenCSMVplRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplRxCells.setStatus("current")
_AdGenCSMVplRxOamCells_Type = Counter32
_AdGenCSMVplRxOamCells_Object = MibTableColumn
adGenCSMVplRxOamCells = _AdGenCSMVplRxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 7),
    _AdGenCSMVplRxOamCells_Type()
)
adGenCSMVplRxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplRxOamCells.setStatus("current")
_AdGenCSMVplDiscardedClp0Cells_Type = Counter32
_AdGenCSMVplDiscardedClp0Cells_Object = MibTableColumn
adGenCSMVplDiscardedClp0Cells = _AdGenCSMVplDiscardedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 8),
    _AdGenCSMVplDiscardedClp0Cells_Type()
)
adGenCSMVplDiscardedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplDiscardedClp0Cells.setStatus("current")
_AdGenCSMVplDiscardedClp01Cells_Type = Counter32
_AdGenCSMVplDiscardedClp01Cells_Object = MibTableColumn
adGenCSMVplDiscardedClp01Cells = _AdGenCSMVplDiscardedClp01Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 9),
    _AdGenCSMVplDiscardedClp01Cells_Type()
)
adGenCSMVplDiscardedClp01Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplDiscardedClp01Cells.setStatus("current")
_AdGenCSMVplTaggedClp0Cells_Type = Counter32
_AdGenCSMVplTaggedClp0Cells_Object = MibTableColumn
adGenCSMVplTaggedClp0Cells = _AdGenCSMVplTaggedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 10),
    _AdGenCSMVplTaggedClp0Cells_Type()
)
adGenCSMVplTaggedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplTaggedClp0Cells.setStatus("current")
_AdGenCSMVplAisStateActive_Type = TruthValue
_AdGenCSMVplAisStateActive_Object = MibTableColumn
adGenCSMVplAisStateActive = _AdGenCSMVplAisStateActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 11),
    _AdGenCSMVplAisStateActive_Type()
)
adGenCSMVplAisStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplAisStateActive.setStatus("current")
_AdGenCSMVplRdiStateActive_Type = TruthValue
_AdGenCSMVplRdiStateActive_Object = MibTableColumn
adGenCSMVplRdiStateActive = _AdGenCSMVplRdiStateActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 12),
    _AdGenCSMVplRdiStateActive_Type()
)
adGenCSMVplRdiStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplRdiStateActive.setStatus("current")
_AdGenCSMVplLastE2EAisOamId_Type = AdGenCsmOamIdv2
_AdGenCSMVplLastE2EAisOamId_Object = MibTableColumn
adGenCSMVplLastE2EAisOamId = _AdGenCSMVplLastE2EAisOamId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 13),
    _AdGenCSMVplLastE2EAisOamId_Type()
)
adGenCSMVplLastE2EAisOamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplLastE2EAisOamId.setStatus("current")
_AdGenCSMVplTxOamLpbkReq_Type = Counter32
_AdGenCSMVplTxOamLpbkReq_Object = MibTableColumn
adGenCSMVplTxOamLpbkReq = _AdGenCSMVplTxOamLpbkReq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 14),
    _AdGenCSMVplTxOamLpbkReq_Type()
)
adGenCSMVplTxOamLpbkReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplTxOamLpbkReq.setStatus("current")
_AdGenCSMVplTxOamLpbkRsp_Type = Counter32
_AdGenCSMVplTxOamLpbkRsp_Object = MibTableColumn
adGenCSMVplTxOamLpbkRsp = _AdGenCSMVplTxOamLpbkRsp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 15),
    _AdGenCSMVplTxOamLpbkRsp_Type()
)
adGenCSMVplTxOamLpbkRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplTxOamLpbkRsp.setStatus("current")
_AdGenCSMVplRxOamLpbkReq_Type = Counter32
_AdGenCSMVplRxOamLpbkReq_Object = MibTableColumn
adGenCSMVplRxOamLpbkReq = _AdGenCSMVplRxOamLpbkReq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 16),
    _AdGenCSMVplRxOamLpbkReq_Type()
)
adGenCSMVplRxOamLpbkReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplRxOamLpbkReq.setStatus("current")
_AdGenCSMVplRxOamLpbkRsp_Type = Counter32
_AdGenCSMVplRxOamLpbkRsp_Object = MibTableColumn
adGenCSMVplRxOamLpbkRsp = _AdGenCSMVplRxOamLpbkRsp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 17),
    _AdGenCSMVplRxOamLpbkRsp_Type()
)
adGenCSMVplRxOamLpbkRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplRxOamLpbkRsp.setStatus("current")
_AdGenCSMVplOamLpbkPassed_Type = Counter32
_AdGenCSMVplOamLpbkPassed_Object = MibTableColumn
adGenCSMVplOamLpbkPassed = _AdGenCSMVplOamLpbkPassed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 18),
    _AdGenCSMVplOamLpbkPassed_Type()
)
adGenCSMVplOamLpbkPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplOamLpbkPassed.setStatus("current")
_AdGenCSMVplOamLpbkFailed_Type = Counter32
_AdGenCSMVplOamLpbkFailed_Object = MibTableColumn
adGenCSMVplOamLpbkFailed = _AdGenCSMVplOamLpbkFailed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 19),
    _AdGenCSMVplOamLpbkFailed_Type()
)
adGenCSMVplOamLpbkFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplOamLpbkFailed.setStatus("current")
_AdGenCSMVplLoopbackEnable_Type = TruthValue
_AdGenCSMVplLoopbackEnable_Object = MibTableColumn
adGenCSMVplLoopbackEnable = _AdGenCSMVplLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 20),
    _AdGenCSMVplLoopbackEnable_Type()
)
adGenCSMVplLoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVplLoopbackEnable.setStatus("current")


class _AdGenCSMVplInfo_Type(OctetString):
    """Custom type adGenCSMVplInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdGenCSMVplInfo_Type.__name__ = "OctetString"
_AdGenCSMVplInfo_Object = MibTableColumn
adGenCSMVplInfo = _AdGenCSMVplInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 21),
    _AdGenCSMVplInfo_Type()
)
adGenCSMVplInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVplInfo.setStatus("current")
_AdGenCSMVplLastError_Type = DisplayString
_AdGenCSMVplLastError_Object = MibTableColumn
adGenCSMVplLastError = _AdGenCSMVplLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 22),
    _AdGenCSMVplLastError_Type()
)
adGenCSMVplLastError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVplLastError.setStatus("current")


class _AdGenCSMVplAal5EncapsType_Type(Integer32):
    """Custom type adGenCSMVplAal5EncapsType based on Integer32"""
    defaultValue = 2

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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("vcMultiplexRoutedProtocol", 1),
          ("vcMultiplexBridgedProtocol8023", 2),
          ("vcMultiplexBridgedProtocol8025", 3),
          ("vcMultiplexBridgedProtocol8026", 4),
          ("vcMultiplexLANemulation8023", 5),
          ("vcMultiplexLANemulation8025", 6),
          ("llcEncapsulation", 7),
          ("multiprotocolFrameRelaySscs", 8),
          ("other", 9),
          ("unknown", 10),
          ("vcMultiplexPppoa", 11),
          ("llcEncapsulatedPppoa", 12),
          ("llcEncapsulatedAutoDiscover", 13))
    )


_AdGenCSMVplAal5EncapsType_Type.__name__ = "Integer32"
_AdGenCSMVplAal5EncapsType_Object = MibTableColumn
adGenCSMVplAal5EncapsType = _AdGenCSMVplAal5EncapsType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 4, 1, 23),
    _AdGenCSMVplAal5EncapsType_Type()
)
adGenCSMVplAal5EncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVplAal5EncapsType.setStatus("current")
_AdGenCSMVclTable_Object = MibTable
adGenCSMVclTable = _AdGenCSMVclTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5)
)
if mibBuilder.loadTexts:
    adGenCSMVclTable.setStatus("current")
_AdGenCSMVclEntry_Object = MibTableRow
adGenCSMVclEntry = _AdGenCSMVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1)
)
adGenCSMVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    adGenCSMVclEntry.setStatus("current")
_AdGenCSMVclDisableAisRdiGeneration_Type = TruthValue
_AdGenCSMVclDisableAisRdiGeneration_Object = MibTableColumn
adGenCSMVclDisableAisRdiGeneration = _AdGenCSMVclDisableAisRdiGeneration_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 1),
    _AdGenCSMVclDisableAisRdiGeneration_Type()
)
adGenCSMVclDisableAisRdiGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVclDisableAisRdiGeneration.setStatus("current")
_AdGenCSMVclDisablePolicing_Type = TruthValue
_AdGenCSMVclDisablePolicing_Object = MibTableColumn
adGenCSMVclDisablePolicing = _AdGenCSMVclDisablePolicing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 2),
    _AdGenCSMVclDisablePolicing_Type()
)
adGenCSMVclDisablePolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVclDisablePolicing.setStatus("current")
_AdGenCSMVclDisableCAC_Type = TruthValue
_AdGenCSMVclDisableCAC_Object = MibTableColumn
adGenCSMVclDisableCAC = _AdGenCSMVclDisableCAC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 3),
    _AdGenCSMVclDisableCAC_Type()
)
adGenCSMVclDisableCAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVclDisableCAC.setStatus("current")


class _AdGenCSMVclResetATMStats_Type(Integer32):
    """Custom type adGenCSMVclResetATMStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenCSMVclResetATMStats_Type.__name__ = "Integer32"
_AdGenCSMVclResetATMStats_Object = MibTableColumn
adGenCSMVclResetATMStats = _AdGenCSMVclResetATMStats_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 4),
    _AdGenCSMVclResetATMStats_Type()
)
adGenCSMVclResetATMStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVclResetATMStats.setStatus("current")
_AdGenCSMVclTxCells_Type = Counter32
_AdGenCSMVclTxCells_Object = MibTableColumn
adGenCSMVclTxCells = _AdGenCSMVclTxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 5),
    _AdGenCSMVclTxCells_Type()
)
adGenCSMVclTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclTxCells.setStatus("current")
_AdGenCSMVclRxCells_Type = Counter32
_AdGenCSMVclRxCells_Object = MibTableColumn
adGenCSMVclRxCells = _AdGenCSMVclRxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 6),
    _AdGenCSMVclRxCells_Type()
)
adGenCSMVclRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclRxCells.setStatus("current")
_AdGenCSMVclRxOamCells_Type = Counter32
_AdGenCSMVclRxOamCells_Object = MibTableColumn
adGenCSMVclRxOamCells = _AdGenCSMVclRxOamCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 7),
    _AdGenCSMVclRxOamCells_Type()
)
adGenCSMVclRxOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclRxOamCells.setStatus("current")
_AdGenCSMVclDiscardedClp0Cells_Type = Counter32
_AdGenCSMVclDiscardedClp0Cells_Object = MibTableColumn
adGenCSMVclDiscardedClp0Cells = _AdGenCSMVclDiscardedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 8),
    _AdGenCSMVclDiscardedClp0Cells_Type()
)
adGenCSMVclDiscardedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclDiscardedClp0Cells.setStatus("current")
_AdGenCSMVclDiscardedClp01Cells_Type = Counter32
_AdGenCSMVclDiscardedClp01Cells_Object = MibTableColumn
adGenCSMVclDiscardedClp01Cells = _AdGenCSMVclDiscardedClp01Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 9),
    _AdGenCSMVclDiscardedClp01Cells_Type()
)
adGenCSMVclDiscardedClp01Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclDiscardedClp01Cells.setStatus("current")
_AdGenCSMVclTaggedClp0Cells_Type = Counter32
_AdGenCSMVclTaggedClp0Cells_Object = MibTableColumn
adGenCSMVclTaggedClp0Cells = _AdGenCSMVclTaggedClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 10),
    _AdGenCSMVclTaggedClp0Cells_Type()
)
adGenCSMVclTaggedClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclTaggedClp0Cells.setStatus("current")
_AdGenCSMVclAisStateActive_Type = TruthValue
_AdGenCSMVclAisStateActive_Object = MibTableColumn
adGenCSMVclAisStateActive = _AdGenCSMVclAisStateActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 11),
    _AdGenCSMVclAisStateActive_Type()
)
adGenCSMVclAisStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclAisStateActive.setStatus("current")
_AdGenCSMVclRdiStateActive_Type = TruthValue
_AdGenCSMVclRdiStateActive_Object = MibTableColumn
adGenCSMVclRdiStateActive = _AdGenCSMVclRdiStateActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 12),
    _AdGenCSMVclRdiStateActive_Type()
)
adGenCSMVclRdiStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclRdiStateActive.setStatus("current")
_AdGenCSMVclLastE2EAisOamId_Type = AdGenCsmOamIdv2
_AdGenCSMVclLastE2EAisOamId_Object = MibTableColumn
adGenCSMVclLastE2EAisOamId = _AdGenCSMVclLastE2EAisOamId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 13),
    _AdGenCSMVclLastE2EAisOamId_Type()
)
adGenCSMVclLastE2EAisOamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclLastE2EAisOamId.setStatus("current")
_AdGenCSMVclTxOamLpbkReq_Type = Counter32
_AdGenCSMVclTxOamLpbkReq_Object = MibTableColumn
adGenCSMVclTxOamLpbkReq = _AdGenCSMVclTxOamLpbkReq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 14),
    _AdGenCSMVclTxOamLpbkReq_Type()
)
adGenCSMVclTxOamLpbkReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclTxOamLpbkReq.setStatus("current")
_AdGenCSMVclTxOamLpbkRsp_Type = Counter32
_AdGenCSMVclTxOamLpbkRsp_Object = MibTableColumn
adGenCSMVclTxOamLpbkRsp = _AdGenCSMVclTxOamLpbkRsp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 15),
    _AdGenCSMVclTxOamLpbkRsp_Type()
)
adGenCSMVclTxOamLpbkRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclTxOamLpbkRsp.setStatus("current")
_AdGenCSMVclRxOamLpbkReq_Type = Counter32
_AdGenCSMVclRxOamLpbkReq_Object = MibTableColumn
adGenCSMVclRxOamLpbkReq = _AdGenCSMVclRxOamLpbkReq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 16),
    _AdGenCSMVclRxOamLpbkReq_Type()
)
adGenCSMVclRxOamLpbkReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclRxOamLpbkReq.setStatus("current")
_AdGenCSMVclRxOamLpbkRsp_Type = Counter32
_AdGenCSMVclRxOamLpbkRsp_Object = MibTableColumn
adGenCSMVclRxOamLpbkRsp = _AdGenCSMVclRxOamLpbkRsp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 17),
    _AdGenCSMVclRxOamLpbkRsp_Type()
)
adGenCSMVclRxOamLpbkRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclRxOamLpbkRsp.setStatus("current")
_AdGenCSMVclOamLpbkPassed_Type = Counter32
_AdGenCSMVclOamLpbkPassed_Object = MibTableColumn
adGenCSMVclOamLpbkPassed = _AdGenCSMVclOamLpbkPassed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 18),
    _AdGenCSMVclOamLpbkPassed_Type()
)
adGenCSMVclOamLpbkPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclOamLpbkPassed.setStatus("current")
_AdGenCSMVclOamLpbkFailed_Type = Counter32
_AdGenCSMVclOamLpbkFailed_Object = MibTableColumn
adGenCSMVclOamLpbkFailed = _AdGenCSMVclOamLpbkFailed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 19),
    _AdGenCSMVclOamLpbkFailed_Type()
)
adGenCSMVclOamLpbkFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclOamLpbkFailed.setStatus("current")
_AdGenCSMVclLoopbackEnable_Type = TruthValue
_AdGenCSMVclLoopbackEnable_Object = MibTableColumn
adGenCSMVclLoopbackEnable = _AdGenCSMVclLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 20),
    _AdGenCSMVclLoopbackEnable_Type()
)
adGenCSMVclLoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVclLoopbackEnable.setStatus("current")


class _AdGenCSMVclInfo_Type(OctetString):
    """Custom type adGenCSMVclInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdGenCSMVclInfo_Type.__name__ = "OctetString"
_AdGenCSMVclInfo_Object = MibTableColumn
adGenCSMVclInfo = _AdGenCSMVclInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 21),
    _AdGenCSMVclInfo_Type()
)
adGenCSMVclInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMVclInfo.setStatus("current")
_AdGenCSMVclLastError_Type = DisplayString
_AdGenCSMVclLastError_Object = MibTableColumn
adGenCSMVclLastError = _AdGenCSMVclLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 22),
    _AdGenCSMVclLastError_Type()
)
adGenCSMVclLastError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVclLastError.setStatus("current")


class _AdGenCSMVclAal5EncapsType_Type(Integer32):
    """Custom type adGenCSMVclAal5EncapsType based on Integer32"""
    defaultValue = 2

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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("vcMultiplexRoutedProtocol", 1),
          ("vcMultiplexBridgedProtocol8023", 2),
          ("vcMultiplexBridgedProtocol8025", 3),
          ("vcMultiplexBridgedProtocol8026", 4),
          ("vcMultiplexLANemulation8023", 5),
          ("vcMultiplexLANemulation8025", 6),
          ("llcEncapsulation", 7),
          ("multiprotocolFrameRelaySscs", 8),
          ("other", 9),
          ("unknown", 10),
          ("vcMultiplexPppoa", 11),
          ("llcEncapsulatedPppoa", 12),
          ("llcEncapsulatedAutoDiscover", 13))
    )


_AdGenCSMVclAal5EncapsType_Type.__name__ = "Integer32"
_AdGenCSMVclAal5EncapsType_Object = MibTableColumn
adGenCSMVclAal5EncapsType = _AdGenCSMVclAal5EncapsType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 23),
    _AdGenCSMVclAal5EncapsType_Type()
)
adGenCSMVclAal5EncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMVclAal5EncapsType.setStatus("current")
_AdGenCSMSubInterfaceIndex_Type = Integer32
_AdGenCSMSubInterfaceIndex_Object = MibTableColumn
adGenCSMSubInterfaceIndex = _AdGenCSMSubInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 5, 1, 24),
    _AdGenCSMSubInterfaceIndex_Type()
)
adGenCSMSubInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMSubInterfaceIndex.setStatus("current")
_AdGenCSMCcNameLookupTable_Object = MibTable
adGenCSMCcNameLookupTable = _AdGenCSMCcNameLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 6)
)
if mibBuilder.loadTexts:
    adGenCSMCcNameLookupTable.setStatus("current")
_AdGenCSMCcNameLookupEntry_Object = MibTableRow
adGenCSMCcNameLookupEntry = _AdGenCSMCcNameLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 6, 1)
)
adGenCSMCcNameLookupEntry.setIndexNames(
    (0, "ADTRAN-GENCSM2-MIB", "adGenCSMCcName"),
)
if mibBuilder.loadTexts:
    adGenCSMCcNameLookupEntry.setStatus("current")
_AdGenCSMCcName_Type = DisplayString
_AdGenCSMCcName_Object = MibTableColumn
adGenCSMCcName = _AdGenCSMCcName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 6, 1, 1),
    _AdGenCSMCcName_Type()
)
adGenCSMCcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenCSMCcName.setStatus("current")


class _AdGenCSMCcFindIndex_Type(Integer32):
    """Custom type adGenCSMCcFindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdGenCSMCcFindIndex_Type.__name__ = "Integer32"
_AdGenCSMCcFindIndex_Object = MibTableColumn
adGenCSMCcFindIndex = _AdGenCSMCcFindIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 6, 1, 2),
    _AdGenCSMCcFindIndex_Type()
)
adGenCSMCcFindIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMCcFindIndex.setStatus("current")
_AdGenCSMTdNameLookupTable_Object = MibTable
adGenCSMTdNameLookupTable = _AdGenCSMTdNameLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 7)
)
if mibBuilder.loadTexts:
    adGenCSMTdNameLookupTable.setStatus("current")
_AdGenCSMTdNameLookupEntry_Object = MibTableRow
adGenCSMTdNameLookupEntry = _AdGenCSMTdNameLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 7, 1)
)
adGenCSMTdNameLookupEntry.setIndexNames(
    (0, "ADTRAN-GENCSM2-MIB", "adGenCSMTdName"),
)
if mibBuilder.loadTexts:
    adGenCSMTdNameLookupEntry.setStatus("current")
_AdGenCSMTdName_Type = DisplayString
_AdGenCSMTdName_Object = MibTableColumn
adGenCSMTdName = _AdGenCSMTdName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 7, 1, 1),
    _AdGenCSMTdName_Type()
)
adGenCSMTdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenCSMTdName.setStatus("current")
_AdGenCSMTdFindIndex_Type = AtmTrafficDescrParamIndex
_AdGenCSMTdFindIndex_Object = MibTableColumn
adGenCSMTdFindIndex = _AdGenCSMTdFindIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 7, 1, 2),
    _AdGenCSMTdFindIndex_Type()
)
adGenCSMTdFindIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMTdFindIndex.setStatus("current")
_AdGenCsmPvpLastChange_Type = TimeTicks
_AdGenCsmPvpLastChange_Object = MibScalar
adGenCsmPvpLastChange = _AdGenCsmPvpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 8),
    _AdGenCsmPvpLastChange_Type()
)
adGenCsmPvpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCsmPvpLastChange.setStatus("current")
_AdGenCsmSvpLastChange_Type = TimeTicks
_AdGenCsmSvpLastChange_Object = MibScalar
adGenCsmSvpLastChange = _AdGenCsmSvpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 9),
    _AdGenCsmSvpLastChange_Type()
)
adGenCsmSvpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCsmSvpLastChange.setStatus("current")
_AdGenCsmPvcLastChange_Type = TimeTicks
_AdGenCsmPvcLastChange_Object = MibScalar
adGenCsmPvcLastChange = _AdGenCsmPvcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 10),
    _AdGenCsmPvcLastChange_Type()
)
adGenCsmPvcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCsmPvcLastChange.setStatus("current")
_AdGenCsmSvcLastChange_Type = TimeTicks
_AdGenCsmSvcLastChange_Object = MibScalar
adGenCsmSvcLastChange = _AdGenCsmSvcLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 11),
    _AdGenCsmSvcLastChange_Type()
)
adGenCsmSvcLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCsmSvcLastChange.setStatus("current")
_AdGenCSMVclOamTable_Object = MibTable
adGenCSMVclOamTable = _AdGenCSMVclOamTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 12)
)
if mibBuilder.loadTexts:
    adGenCSMVclOamTable.setStatus("current")
_AdGenCSMVclOamEntry_Object = MibTableRow
adGenCSMVclOamEntry = _AdGenCSMVclOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 12, 1)
)
adGenCSMVclOamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    adGenCSMVclOamEntry.setStatus("current")


class _AdGenCSMVclOamId_Type(OctetString):
    """Custom type adGenCSMVclOamId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AdGenCSMVclOamId_Type.__name__ = "OctetString"
_AdGenCSMVclOamId_Object = MibTableColumn
adGenCSMVclOamId = _AdGenCSMVclOamId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 12, 1, 1),
    _AdGenCSMVclOamId_Type()
)
adGenCSMVclOamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclOamId.setStatus("current")


class _AdGenCSMVclSendSegLoopback_Type(Integer32):
    """Custom type adGenCSMVclSendSegLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AdGenCSMVclSendSegLoopback_Type.__name__ = "Integer32"
_AdGenCSMVclSendSegLoopback_Object = MibTableColumn
adGenCSMVclSendSegLoopback = _AdGenCSMVclSendSegLoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 12, 1, 2),
    _AdGenCSMVclSendSegLoopback_Type()
)
adGenCSMVclSendSegLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclSendSegLoopback.setStatus("current")


class _AdGenCSMVclSendE2ELoopback_Type(Integer32):
    """Custom type adGenCSMVclSendE2ELoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AdGenCSMVclSendE2ELoopback_Type.__name__ = "Integer32"
_AdGenCSMVclSendE2ELoopback_Object = MibTableColumn
adGenCSMVclSendE2ELoopback = _AdGenCSMVclSendE2ELoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 12, 1, 3),
    _AdGenCSMVclSendE2ELoopback_Type()
)
adGenCSMVclSendE2ELoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclSendE2ELoopback.setStatus("current")


class _AdGenCSMVclOamRowStatus_Type(RowStatus):
    """Custom type adGenCSMVclOamRowStatus based on RowStatus"""
    defaultValue = 5


_AdGenCSMVclOamRowStatus_Type.__name__ = "RowStatus"
_AdGenCSMVclOamRowStatus_Object = MibTableColumn
adGenCSMVclOamRowStatus = _AdGenCSMVclOamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 12, 1, 4),
    _AdGenCSMVclOamRowStatus_Type()
)
adGenCSMVclOamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclOamRowStatus.setStatus("current")
_AdGenCSMVplOamTable_Object = MibTable
adGenCSMVplOamTable = _AdGenCSMVplOamTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 13)
)
if mibBuilder.loadTexts:
    adGenCSMVplOamTable.setStatus("current")
_AdGenCSMVplOamEntry_Object = MibTableRow
adGenCSMVplOamEntry = _AdGenCSMVplOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 13, 1)
)
adGenCSMVplOamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    adGenCSMVplOamEntry.setStatus("current")


class _AdGenCSMVplOamId_Type(OctetString):
    """Custom type adGenCSMVplOamId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AdGenCSMVplOamId_Type.__name__ = "OctetString"
_AdGenCSMVplOamId_Object = MibTableColumn
adGenCSMVplOamId = _AdGenCSMVplOamId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 13, 1, 1),
    _AdGenCSMVplOamId_Type()
)
adGenCSMVplOamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplOamId.setStatus("current")


class _AdGenCSMVplSendSegLoopback_Type(Integer32):
    """Custom type adGenCSMVplSendSegLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AdGenCSMVplSendSegLoopback_Type.__name__ = "Integer32"
_AdGenCSMVplSendSegLoopback_Object = MibTableColumn
adGenCSMVplSendSegLoopback = _AdGenCSMVplSendSegLoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 13, 1, 2),
    _AdGenCSMVplSendSegLoopback_Type()
)
adGenCSMVplSendSegLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplSendSegLoopback.setStatus("current")


class _AdGenCSMVplSendE2ELoopback_Type(Integer32):
    """Custom type adGenCSMVplSendE2ELoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AdGenCSMVplSendE2ELoopback_Type.__name__ = "Integer32"
_AdGenCSMVplSendE2ELoopback_Object = MibTableColumn
adGenCSMVplSendE2ELoopback = _AdGenCSMVplSendE2ELoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 13, 1, 3),
    _AdGenCSMVplSendE2ELoopback_Type()
)
adGenCSMVplSendE2ELoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplSendE2ELoopback.setStatus("current")


class _AdGenCSMVplOamRowStatus_Type(RowStatus):
    """Custom type adGenCSMVplOamRowStatus based on RowStatus"""
    defaultValue = 5


_AdGenCSMVplOamRowStatus_Type.__name__ = "RowStatus"
_AdGenCSMVplOamRowStatus_Object = MibTableColumn
adGenCSMVplOamRowStatus = _AdGenCSMVplOamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 13, 1, 4),
    _AdGenCSMVplOamRowStatus_Type()
)
adGenCSMVplOamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplOamRowStatus.setStatus("current")
_AdGenCSMVclEnhOamTable_Object = MibTable
adGenCSMVclEnhOamTable = _AdGenCSMVclEnhOamTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14)
)
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamTable.setStatus("current")
_AdGenCSMVclEnhOamEntry_Object = MibTableRow
adGenCSMVclEnhOamEntry = _AdGenCSMVclEnhOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1)
)
adGenCSMVclEnhOamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamEntry.setStatus("current")


class _AdGenCSMVclEnhOamId_Type(OctetString):
    """Custom type adGenCSMVclEnhOamId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AdGenCSMVclEnhOamId_Type.__name__ = "OctetString"
_AdGenCSMVclEnhOamId_Object = MibTableColumn
adGenCSMVclEnhOamId = _AdGenCSMVclEnhOamId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1, 1),
    _AdGenCSMVclEnhOamId_Type()
)
adGenCSMVclEnhOamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamId.setStatus("current")


class _AdGenCSMVclEnhOamLpbkReqCount_Type(Integer32):
    """Custom type adGenCSMVclEnhOamLpbkReqCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AdGenCSMVclEnhOamLpbkReqCount_Type.__name__ = "Integer32"
_AdGenCSMVclEnhOamLpbkReqCount_Object = MibTableColumn
adGenCSMVclEnhOamLpbkReqCount = _AdGenCSMVclEnhOamLpbkReqCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1, 2),
    _AdGenCSMVclEnhOamLpbkReqCount_Type()
)
adGenCSMVclEnhOamLpbkReqCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamLpbkReqCount.setStatus("current")


class _AdGenCSMVclEnhOamLpbkTxDelay_Type(Integer32):
    """Custom type adGenCSMVclEnhOamLpbkTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_AdGenCSMVclEnhOamLpbkTxDelay_Type.__name__ = "Integer32"
_AdGenCSMVclEnhOamLpbkTxDelay_Object = MibTableColumn
adGenCSMVclEnhOamLpbkTxDelay = _AdGenCSMVclEnhOamLpbkTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1, 3),
    _AdGenCSMVclEnhOamLpbkTxDelay_Type()
)
adGenCSMVclEnhOamLpbkTxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamLpbkTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamLpbkTxDelay.setUnits("milliseconds")


class _AdGenCSMVclEnhOamLpbkTimeout_Type(Integer32):
    """Custom type adGenCSMVclEnhOamLpbkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdGenCSMVclEnhOamLpbkTimeout_Type.__name__ = "Integer32"
_AdGenCSMVclEnhOamLpbkTimeout_Object = MibTableColumn
adGenCSMVclEnhOamLpbkTimeout = _AdGenCSMVclEnhOamLpbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1, 4),
    _AdGenCSMVclEnhOamLpbkTimeout_Type()
)
adGenCSMVclEnhOamLpbkTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamLpbkTimeout.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamLpbkTimeout.setUnits("milliseconds")
_AdGenCSMVclEnhOamLpbkReqTx_Type = Integer32
_AdGenCSMVclEnhOamLpbkReqTx_Object = MibTableColumn
adGenCSMVclEnhOamLpbkReqTx = _AdGenCSMVclEnhOamLpbkReqTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1, 5),
    _AdGenCSMVclEnhOamLpbkReqTx_Type()
)
adGenCSMVclEnhOamLpbkReqTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamLpbkReqTx.setStatus("current")
_AdGenCSMVclEnhOamLpbkRespRx_Type = Integer32
_AdGenCSMVclEnhOamLpbkRespRx_Object = MibTableColumn
adGenCSMVclEnhOamLpbkRespRx = _AdGenCSMVclEnhOamLpbkRespRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1, 6),
    _AdGenCSMVclEnhOamLpbkRespRx_Type()
)
adGenCSMVclEnhOamLpbkRespRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamLpbkRespRx.setStatus("current")
_AdGenCSMVclEnhOamLpbkRespTimeout_Type = Integer32
_AdGenCSMVclEnhOamLpbkRespTimeout_Object = MibTableColumn
adGenCSMVclEnhOamLpbkRespTimeout = _AdGenCSMVclEnhOamLpbkRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1, 7),
    _AdGenCSMVclEnhOamLpbkRespTimeout_Type()
)
adGenCSMVclEnhOamLpbkRespTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamLpbkRespTimeout.setStatus("current")


class _AdGenCSMVclEnhOamLpbkReqType_Type(Integer32):
    """Custom type adGenCSMVclEnhOamLpbkReqType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("segment", 1),
          ("endtoend", 2))
    )


_AdGenCSMVclEnhOamLpbkReqType_Type.__name__ = "Integer32"
_AdGenCSMVclEnhOamLpbkReqType_Object = MibTableColumn
adGenCSMVclEnhOamLpbkReqType = _AdGenCSMVclEnhOamLpbkReqType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1, 8),
    _AdGenCSMVclEnhOamLpbkReqType_Type()
)
adGenCSMVclEnhOamLpbkReqType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamLpbkReqType.setStatus("current")


class _AdGenCSMVclEnhOamRowStatus_Type(RowStatus):
    """Custom type adGenCSMVclEnhOamRowStatus based on RowStatus"""
    defaultValue = 5


_AdGenCSMVclEnhOamRowStatus_Type.__name__ = "RowStatus"
_AdGenCSMVclEnhOamRowStatus_Object = MibTableColumn
adGenCSMVclEnhOamRowStatus = _AdGenCSMVclEnhOamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 14, 1, 9),
    _AdGenCSMVclEnhOamRowStatus_Type()
)
adGenCSMVclEnhOamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVclEnhOamRowStatus.setStatus("current")
_AdGenCSMVplEnhOamTable_Object = MibTable
adGenCSMVplEnhOamTable = _AdGenCSMVplEnhOamTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15)
)
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamTable.setStatus("current")
_AdGenCSMVplEnhOamEntry_Object = MibTableRow
adGenCSMVplEnhOamEntry = _AdGenCSMVplEnhOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1)
)
adGenCSMVplEnhOamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamEntry.setStatus("current")


class _AdGenCSMVplEnhOamId_Type(OctetString):
    """Custom type adGenCSMVplEnhOamId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AdGenCSMVplEnhOamId_Type.__name__ = "OctetString"
_AdGenCSMVplEnhOamId_Object = MibTableColumn
adGenCSMVplEnhOamId = _AdGenCSMVplEnhOamId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1, 1),
    _AdGenCSMVplEnhOamId_Type()
)
adGenCSMVplEnhOamId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamId.setStatus("current")


class _AdGenCSMVplEnhOamLpbkReqCount_Type(Integer32):
    """Custom type adGenCSMVplEnhOamLpbkReqCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AdGenCSMVplEnhOamLpbkReqCount_Type.__name__ = "Integer32"
_AdGenCSMVplEnhOamLpbkReqCount_Object = MibTableColumn
adGenCSMVplEnhOamLpbkReqCount = _AdGenCSMVplEnhOamLpbkReqCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1, 2),
    _AdGenCSMVplEnhOamLpbkReqCount_Type()
)
adGenCSMVplEnhOamLpbkReqCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamLpbkReqCount.setStatus("current")


class _AdGenCSMVplEnhOamLpbkTxDelay_Type(Integer32):
    """Custom type adGenCSMVplEnhOamLpbkTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_AdGenCSMVplEnhOamLpbkTxDelay_Type.__name__ = "Integer32"
_AdGenCSMVplEnhOamLpbkTxDelay_Object = MibTableColumn
adGenCSMVplEnhOamLpbkTxDelay = _AdGenCSMVplEnhOamLpbkTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1, 3),
    _AdGenCSMVplEnhOamLpbkTxDelay_Type()
)
adGenCSMVplEnhOamLpbkTxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamLpbkTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamLpbkTxDelay.setUnits("milliseconds")


class _AdGenCSMVplEnhOamLpbkTimeout_Type(Integer32):
    """Custom type adGenCSMVplEnhOamLpbkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdGenCSMVplEnhOamLpbkTimeout_Type.__name__ = "Integer32"
_AdGenCSMVplEnhOamLpbkTimeout_Object = MibTableColumn
adGenCSMVplEnhOamLpbkTimeout = _AdGenCSMVplEnhOamLpbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1, 4),
    _AdGenCSMVplEnhOamLpbkTimeout_Type()
)
adGenCSMVplEnhOamLpbkTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamLpbkTimeout.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamLpbkTimeout.setUnits("milliseconds")
_AdGenCSMVplEnhOamLpbkReqTx_Type = Integer32
_AdGenCSMVplEnhOamLpbkReqTx_Object = MibTableColumn
adGenCSMVplEnhOamLpbkReqTx = _AdGenCSMVplEnhOamLpbkReqTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1, 5),
    _AdGenCSMVplEnhOamLpbkReqTx_Type()
)
adGenCSMVplEnhOamLpbkReqTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamLpbkReqTx.setStatus("current")
_AdGenCSMVplEnhOamLpbkRespRx_Type = Integer32
_AdGenCSMVplEnhOamLpbkRespRx_Object = MibTableColumn
adGenCSMVplEnhOamLpbkRespRx = _AdGenCSMVplEnhOamLpbkRespRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1, 6),
    _AdGenCSMVplEnhOamLpbkRespRx_Type()
)
adGenCSMVplEnhOamLpbkRespRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamLpbkRespRx.setStatus("current")
_AdGenCSMVplEnhOamLpbkRespTimeout_Type = Integer32
_AdGenCSMVplEnhOamLpbkRespTimeout_Object = MibTableColumn
adGenCSMVplEnhOamLpbkRespTimeout = _AdGenCSMVplEnhOamLpbkRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1, 7),
    _AdGenCSMVplEnhOamLpbkRespTimeout_Type()
)
adGenCSMVplEnhOamLpbkRespTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamLpbkRespTimeout.setStatus("current")


class _AdGenCSMVplEnhOamLpbkReqType_Type(Integer32):
    """Custom type adGenCSMVplEnhOamLpbkReqType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("segment", 1),
          ("endtoend", 2))
    )


_AdGenCSMVplEnhOamLpbkReqType_Type.__name__ = "Integer32"
_AdGenCSMVplEnhOamLpbkReqType_Object = MibTableColumn
adGenCSMVplEnhOamLpbkReqType = _AdGenCSMVplEnhOamLpbkReqType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1, 8),
    _AdGenCSMVplEnhOamLpbkReqType_Type()
)
adGenCSMVplEnhOamLpbkReqType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamLpbkReqType.setStatus("current")


class _AdGenCSMVplEnhOamRowStatus_Type(RowStatus):
    """Custom type adGenCSMVplEnhOamRowStatus based on RowStatus"""
    defaultValue = 5


_AdGenCSMVplEnhOamRowStatus_Type.__name__ = "RowStatus"
_AdGenCSMVplEnhOamRowStatus_Object = MibTableColumn
adGenCSMVplEnhOamRowStatus = _AdGenCSMVplEnhOamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 15, 1, 9),
    _AdGenCSMVplEnhOamRowStatus_Type()
)
adGenCSMVplEnhOamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMVplEnhOamRowStatus.setStatus("current")


class _AdGenCSMUseFixedIndexes_Type(TruthValue):
    """Custom type adGenCSMUseFixedIndexes based on TruthValue"""
    defaultValue = 2


_AdGenCSMUseFixedIndexes_Type.__name__ = "TruthValue"
_AdGenCSMUseFixedIndexes_Object = MibScalar
adGenCSMUseFixedIndexes = _AdGenCSMUseFixedIndexes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 4, 16),
    _AdGenCSMUseFixedIndexes_Type()
)
adGenCSMUseFixedIndexes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMUseFixedIndexes.setStatus("current")
_AdGenCSMOptionsExtension_ObjectIdentity = ObjectIdentity
adGenCSMOptionsExtension = _AdGenCSMOptionsExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6)
)


class _AdGenCSMOptionMenuLevel_Type(Integer32):
    """Custom type adGenCSMOptionMenuLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AdGenCSMOptionMenuLevel_Type.__name__ = "Integer32"
_AdGenCSMOptionMenuLevel_Object = MibScalar
adGenCSMOptionMenuLevel = _AdGenCSMOptionMenuLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 1),
    _AdGenCSMOptionMenuLevel_Type()
)
adGenCSMOptionMenuLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMOptionMenuLevel.setStatus("current")


class _AdGenCSMOptionMenuDisplayDirection_Type(TruthValue):
    """Custom type adGenCSMOptionMenuDisplayDirection based on TruthValue"""
    defaultValue = 1


_AdGenCSMOptionMenuDisplayDirection_Type.__name__ = "TruthValue"
_AdGenCSMOptionMenuDisplayDirection_Object = MibScalar
adGenCSMOptionMenuDisplayDirection = _AdGenCSMOptionMenuDisplayDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 2),
    _AdGenCSMOptionMenuDisplayDirection_Type()
)
adGenCSMOptionMenuDisplayDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMOptionMenuDisplayDirection.setStatus("current")


class _AdGenCSMOptionMenuDisplayPort_Type(TruthValue):
    """Custom type adGenCSMOptionMenuDisplayPort based on TruthValue"""
    defaultValue = 1


_AdGenCSMOptionMenuDisplayPort_Type.__name__ = "TruthValue"
_AdGenCSMOptionMenuDisplayPort_Object = MibScalar
adGenCSMOptionMenuDisplayPort = _AdGenCSMOptionMenuDisplayPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 3),
    _AdGenCSMOptionMenuDisplayPort_Type()
)
adGenCSMOptionMenuDisplayPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMOptionMenuDisplayPort.setStatus("current")


class _AdGenCSMOptionMenuDisplayClass_Type(TruthValue):
    """Custom type adGenCSMOptionMenuDisplayClass based on TruthValue"""
    defaultValue = 2


_AdGenCSMOptionMenuDisplayClass_Type.__name__ = "TruthValue"
_AdGenCSMOptionMenuDisplayClass_Object = MibScalar
adGenCSMOptionMenuDisplayClass = _AdGenCSMOptionMenuDisplayClass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 4),
    _AdGenCSMOptionMenuDisplayClass_Type()
)
adGenCSMOptionMenuDisplayClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMOptionMenuDisplayClass.setStatus("current")


class _AdGenCSMShelfPolicingDisable_Type(TruthValue):
    """Custom type adGenCSMShelfPolicingDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMShelfPolicingDisable_Type.__name__ = "TruthValue"
_AdGenCSMShelfPolicingDisable_Object = MibScalar
adGenCSMShelfPolicingDisable = _AdGenCSMShelfPolicingDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 5),
    _AdGenCSMShelfPolicingDisable_Type()
)
adGenCSMShelfPolicingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfPolicingDisable.setStatus("current")


class _AdGenCSMShelfCellRateCACDisable_Type(TruthValue):
    """Custom type adGenCSMShelfCellRateCACDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMShelfCellRateCACDisable_Type.__name__ = "TruthValue"
_AdGenCSMShelfCellRateCACDisable_Object = MibScalar
adGenCSMShelfCellRateCACDisable = _AdGenCSMShelfCellRateCACDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 6),
    _AdGenCSMShelfCellRateCACDisable_Type()
)
adGenCSMShelfCellRateCACDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfCellRateCACDisable.setStatus("current")


class _AdGenCSMShelfBufferCACDisable_Type(TruthValue):
    """Custom type adGenCSMShelfBufferCACDisable based on TruthValue"""
    defaultValue = 1


_AdGenCSMShelfBufferCACDisable_Type.__name__ = "TruthValue"
_AdGenCSMShelfBufferCACDisable_Object = MibScalar
adGenCSMShelfBufferCACDisable = _AdGenCSMShelfBufferCACDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 7),
    _AdGenCSMShelfBufferCACDisable_Type()
)
adGenCSMShelfBufferCACDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfBufferCACDisable.setStatus("current")


class _AdGenCSMShelfCbrOverbooking_Type(Integer32):
    """Custom type adGenCSMShelfCbrOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdGenCSMShelfCbrOverbooking_Type.__name__ = "Integer32"
_AdGenCSMShelfCbrOverbooking_Object = MibScalar
adGenCSMShelfCbrOverbooking = _AdGenCSMShelfCbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 8),
    _AdGenCSMShelfCbrOverbooking_Type()
)
adGenCSMShelfCbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfCbrOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfCbrOverbooking.setUnits("percent")


class _AdGenCSMShelfRtVbrOverbooking_Type(Integer32):
    """Custom type adGenCSMShelfRtVbrOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdGenCSMShelfRtVbrOverbooking_Type.__name__ = "Integer32"
_AdGenCSMShelfRtVbrOverbooking_Object = MibScalar
adGenCSMShelfRtVbrOverbooking = _AdGenCSMShelfRtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 9),
    _AdGenCSMShelfRtVbrOverbooking_Type()
)
adGenCSMShelfRtVbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfRtVbrOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfRtVbrOverbooking.setUnits("percent")


class _AdGenCSMShelfNrtVbrOverbooking_Type(Integer32):
    """Custom type adGenCSMShelfNrtVbrOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdGenCSMShelfNrtVbrOverbooking_Type.__name__ = "Integer32"
_AdGenCSMShelfNrtVbrOverbooking_Object = MibScalar
adGenCSMShelfNrtVbrOverbooking = _AdGenCSMShelfNrtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 10),
    _AdGenCSMShelfNrtVbrOverbooking_Type()
)
adGenCSMShelfNrtVbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfNrtVbrOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfNrtVbrOverbooking.setUnits("percent")


class _AdGenCSMShelfNrtVbrSharing_Type(Integer32):
    """Custom type adGenCSMShelfNrtVbrSharing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenCSMShelfNrtVbrSharing_Type.__name__ = "Integer32"
_AdGenCSMShelfNrtVbrSharing_Object = MibScalar
adGenCSMShelfNrtVbrSharing = _AdGenCSMShelfNrtVbrSharing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 11),
    _AdGenCSMShelfNrtVbrSharing_Type()
)
adGenCSMShelfNrtVbrSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfNrtVbrSharing.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfNrtVbrSharing.setUnits("percent")


class _AdGenCSMShelfUbrSharing_Type(Integer32):
    """Custom type adGenCSMShelfUbrSharing based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenCSMShelfUbrSharing_Type.__name__ = "Integer32"
_AdGenCSMShelfUbrSharing_Object = MibScalar
adGenCSMShelfUbrSharing = _AdGenCSMShelfUbrSharing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 12),
    _AdGenCSMShelfUbrSharing_Type()
)
adGenCSMShelfUbrSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrSharing.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrSharing.setUnits("percent")


class _AdGenCSMShelfUbrMaxClp1Thrsh_Type(Integer32):
    """Custom type adGenCSMShelfUbrMaxClp1Thrsh based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMShelfUbrMaxClp1Thrsh_Type.__name__ = "Integer32"
_AdGenCSMShelfUbrMaxClp1Thrsh_Object = MibScalar
adGenCSMShelfUbrMaxClp1Thrsh = _AdGenCSMShelfUbrMaxClp1Thrsh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 13),
    _AdGenCSMShelfUbrMaxClp1Thrsh_Type()
)
adGenCSMShelfUbrMaxClp1Thrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrMaxClp1Thrsh.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrMaxClp1Thrsh.setUnits("cells")


class _AdGenCSMShelfUbrMaxClp0Thrsh_Type(Integer32):
    """Custom type adGenCSMShelfUbrMaxClp0Thrsh based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMShelfUbrMaxClp0Thrsh_Type.__name__ = "Integer32"
_AdGenCSMShelfUbrMaxClp0Thrsh_Object = MibScalar
adGenCSMShelfUbrMaxClp0Thrsh = _AdGenCSMShelfUbrMaxClp0Thrsh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 14),
    _AdGenCSMShelfUbrMaxClp0Thrsh_Type()
)
adGenCSMShelfUbrMaxClp0Thrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrMaxClp0Thrsh.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrMaxClp0Thrsh.setUnits("cells")


class _AdGenCSMShelfUbrMaxMaxThrsh_Type(Integer32):
    """Custom type adGenCSMShelfUbrMaxMaxThrsh based on Integer32"""
    defaultValue = 544

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMShelfUbrMaxMaxThrsh_Type.__name__ = "Integer32"
_AdGenCSMShelfUbrMaxMaxThrsh_Object = MibScalar
adGenCSMShelfUbrMaxMaxThrsh = _AdGenCSMShelfUbrMaxMaxThrsh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 15),
    _AdGenCSMShelfUbrMaxMaxThrsh_Type()
)
adGenCSMShelfUbrMaxMaxThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrMaxMaxThrsh.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrMaxMaxThrsh.setUnits("cells")


class _AdGenCSMShelfUbrMaxFrameMultiplier_Type(Integer32):
    """Custom type adGenCSMShelfUbrMaxFrameMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMShelfUbrMaxFrameMultiplier_Type.__name__ = "Integer32"
_AdGenCSMShelfUbrMaxFrameMultiplier_Object = MibScalar
adGenCSMShelfUbrMaxFrameMultiplier = _AdGenCSMShelfUbrMaxFrameMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 16),
    _AdGenCSMShelfUbrMaxFrameMultiplier_Type()
)
adGenCSMShelfUbrMaxFrameMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrMaxFrameMultiplier.setStatus("current")
_AdGenCSMDirectionOptionTable_Object = MibTable
adGenCSMDirectionOptionTable = _AdGenCSMDirectionOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17)
)
if mibBuilder.loadTexts:
    adGenCSMDirectionOptionTable.setStatus("current")
_AdGenCSMDirectionOptionEntry_Object = MibTableRow
adGenCSMDirectionOptionEntry = _AdGenCSMDirectionOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1)
)
adGenCSMDirectionOptionEntry.setIndexNames(
    (0, "ADTRAN-GENCSM2-MIB", "adGenCSMDirection"),
)
if mibBuilder.loadTexts:
    adGenCSMDirectionOptionEntry.setStatus("current")
_AdGenCSMDirection_Type = AdGenCSMDirection
_AdGenCSMDirection_Object = MibTableColumn
adGenCSMDirection = _AdGenCSMDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 1),
    _AdGenCSMDirection_Type()
)
adGenCSMDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenCSMDirection.setStatus("current")


class _AdGenCSMDirectionPolicingDisable_Type(TruthValue):
    """Custom type adGenCSMDirectionPolicingDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionPolicingDisable_Type.__name__ = "TruthValue"
_AdGenCSMDirectionPolicingDisable_Object = MibTableColumn
adGenCSMDirectionPolicingDisable = _AdGenCSMDirectionPolicingDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 2),
    _AdGenCSMDirectionPolicingDisable_Type()
)
adGenCSMDirectionPolicingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionPolicingDisable.setStatus("current")


class _AdGenCSMDirectionCellRateCACDisable_Type(TruthValue):
    """Custom type adGenCSMDirectionCellRateCACDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionCellRateCACDisable_Type.__name__ = "TruthValue"
_AdGenCSMDirectionCellRateCACDisable_Object = MibTableColumn
adGenCSMDirectionCellRateCACDisable = _AdGenCSMDirectionCellRateCACDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 3),
    _AdGenCSMDirectionCellRateCACDisable_Type()
)
adGenCSMDirectionCellRateCACDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionCellRateCACDisable.setStatus("current")


class _AdGenCSMDirectionBufferCACDisable_Type(TruthValue):
    """Custom type adGenCSMDirectionBufferCACDisable based on TruthValue"""
    defaultValue = 1


_AdGenCSMDirectionBufferCACDisable_Type.__name__ = "TruthValue"
_AdGenCSMDirectionBufferCACDisable_Object = MibTableColumn
adGenCSMDirectionBufferCACDisable = _AdGenCSMDirectionBufferCACDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 4),
    _AdGenCSMDirectionBufferCACDisable_Type()
)
adGenCSMDirectionBufferCACDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionBufferCACDisable.setStatus("current")


class _AdGenCSMDirectionCbrOverbooking_Type(Integer32):
    """Custom type adGenCSMDirectionCbrOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdGenCSMDirectionCbrOverbooking_Type.__name__ = "Integer32"
_AdGenCSMDirectionCbrOverbooking_Object = MibTableColumn
adGenCSMDirectionCbrOverbooking = _AdGenCSMDirectionCbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 5),
    _AdGenCSMDirectionCbrOverbooking_Type()
)
adGenCSMDirectionCbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionCbrOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionCbrOverbooking.setUnits("percent")


class _AdGenCSMDirectionRtVbrOverbooking_Type(Integer32):
    """Custom type adGenCSMDirectionRtVbrOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdGenCSMDirectionRtVbrOverbooking_Type.__name__ = "Integer32"
_AdGenCSMDirectionRtVbrOverbooking_Object = MibTableColumn
adGenCSMDirectionRtVbrOverbooking = _AdGenCSMDirectionRtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 6),
    _AdGenCSMDirectionRtVbrOverbooking_Type()
)
adGenCSMDirectionRtVbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionRtVbrOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionRtVbrOverbooking.setUnits("percent")


class _AdGenCSMDirectionNrtVbrOverbooking_Type(Integer32):
    """Custom type adGenCSMDirectionNrtVbrOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdGenCSMDirectionNrtVbrOverbooking_Type.__name__ = "Integer32"
_AdGenCSMDirectionNrtVbrOverbooking_Object = MibTableColumn
adGenCSMDirectionNrtVbrOverbooking = _AdGenCSMDirectionNrtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 7),
    _AdGenCSMDirectionNrtVbrOverbooking_Type()
)
adGenCSMDirectionNrtVbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionNrtVbrOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionNrtVbrOverbooking.setUnits("percent")


class _AdGenCSMDirectionMaximumThreshold_Type(Integer32):
    """Custom type adGenCSMDirectionMaximumThreshold based on Integer32"""
    defaultValue = 131072

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262143),
    )


_AdGenCSMDirectionMaximumThreshold_Type.__name__ = "Integer32"
_AdGenCSMDirectionMaximumThreshold_Object = MibTableColumn
adGenCSMDirectionMaximumThreshold = _AdGenCSMDirectionMaximumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 8),
    _AdGenCSMDirectionMaximumThreshold_Type()
)
adGenCSMDirectionMaximumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionMaximumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionMaximumThreshold.setUnits("cells")


class _AdGenCSMDirectionNrtVbrSharing_Type(Integer32):
    """Custom type adGenCSMDirectionNrtVbrSharing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenCSMDirectionNrtVbrSharing_Type.__name__ = "Integer32"
_AdGenCSMDirectionNrtVbrSharing_Object = MibTableColumn
adGenCSMDirectionNrtVbrSharing = _AdGenCSMDirectionNrtVbrSharing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 9),
    _AdGenCSMDirectionNrtVbrSharing_Type()
)
adGenCSMDirectionNrtVbrSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionNrtVbrSharing.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionNrtVbrSharing.setUnits("percent")


class _AdGenCSMDirectionUbrSharing_Type(Integer32):
    """Custom type adGenCSMDirectionUbrSharing based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenCSMDirectionUbrSharing_Type.__name__ = "Integer32"
_AdGenCSMDirectionUbrSharing_Object = MibTableColumn
adGenCSMDirectionUbrSharing = _AdGenCSMDirectionUbrSharing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 10),
    _AdGenCSMDirectionUbrSharing_Type()
)
adGenCSMDirectionUbrSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrSharing.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrSharing.setUnits("percent")


class _AdGenCSMDirectionUbrMaxClp1Thrsh_Type(Integer32):
    """Custom type adGenCSMDirectionUbrMaxClp1Thrsh based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMDirectionUbrMaxClp1Thrsh_Type.__name__ = "Integer32"
_AdGenCSMDirectionUbrMaxClp1Thrsh_Object = MibTableColumn
adGenCSMDirectionUbrMaxClp1Thrsh = _AdGenCSMDirectionUbrMaxClp1Thrsh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 11),
    _AdGenCSMDirectionUbrMaxClp1Thrsh_Type()
)
adGenCSMDirectionUbrMaxClp1Thrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxClp1Thrsh.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxClp1Thrsh.setUnits("cells")


class _AdGenCSMDirectionUbrMaxClp0Thrsh_Type(Integer32):
    """Custom type adGenCSMDirectionUbrMaxClp0Thrsh based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMDirectionUbrMaxClp0Thrsh_Type.__name__ = "Integer32"
_AdGenCSMDirectionUbrMaxClp0Thrsh_Object = MibTableColumn
adGenCSMDirectionUbrMaxClp0Thrsh = _AdGenCSMDirectionUbrMaxClp0Thrsh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 12),
    _AdGenCSMDirectionUbrMaxClp0Thrsh_Type()
)
adGenCSMDirectionUbrMaxClp0Thrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxClp0Thrsh.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxClp0Thrsh.setUnits("cells")


class _AdGenCSMDirectionUbrMaxMaxThrsh_Type(Integer32):
    """Custom type adGenCSMDirectionUbrMaxMaxThrsh based on Integer32"""
    defaultValue = 544

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMDirectionUbrMaxMaxThrsh_Type.__name__ = "Integer32"
_AdGenCSMDirectionUbrMaxMaxThrsh_Object = MibTableColumn
adGenCSMDirectionUbrMaxMaxThrsh = _AdGenCSMDirectionUbrMaxMaxThrsh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 13),
    _AdGenCSMDirectionUbrMaxMaxThrsh_Type()
)
adGenCSMDirectionUbrMaxMaxThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxMaxThrsh.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxMaxThrsh.setUnits("cells")


class _AdGenCSMDirectionUbrMaxFrameMultiplier_Type(Integer32):
    """Custom type adGenCSMDirectionUbrMaxFrameMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMDirectionUbrMaxFrameMultiplier_Type.__name__ = "Integer32"
_AdGenCSMDirectionUbrMaxFrameMultiplier_Object = MibTableColumn
adGenCSMDirectionUbrMaxFrameMultiplier = _AdGenCSMDirectionUbrMaxFrameMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 14),
    _AdGenCSMDirectionUbrMaxFrameMultiplier_Type()
)
adGenCSMDirectionUbrMaxFrameMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxFrameMultiplier.setStatus("current")


class _AdGenCSMDirectionPolicingDisableOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionPolicingDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionPolicingDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionPolicingDisableOverride_Object = MibTableColumn
adGenCSMDirectionPolicingDisableOverride = _AdGenCSMDirectionPolicingDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 15),
    _AdGenCSMDirectionPolicingDisableOverride_Type()
)
adGenCSMDirectionPolicingDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionPolicingDisableOverride.setStatus("current")


class _AdGenCSMDirectionCellRateCACDisableOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionCellRateCACDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionCellRateCACDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionCellRateCACDisableOverride_Object = MibTableColumn
adGenCSMDirectionCellRateCACDisableOverride = _AdGenCSMDirectionCellRateCACDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 16),
    _AdGenCSMDirectionCellRateCACDisableOverride_Type()
)
adGenCSMDirectionCellRateCACDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionCellRateCACDisableOverride.setStatus("current")


class _AdGenCSMDirectionBufferCACDisableOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionBufferCACDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionBufferCACDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionBufferCACDisableOverride_Object = MibTableColumn
adGenCSMDirectionBufferCACDisableOverride = _AdGenCSMDirectionBufferCACDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 17),
    _AdGenCSMDirectionBufferCACDisableOverride_Type()
)
adGenCSMDirectionBufferCACDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionBufferCACDisableOverride.setStatus("current")


class _AdGenCSMDirectionCbrOverbookingOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionCbrOverbookingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionCbrOverbookingOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionCbrOverbookingOverride_Object = MibTableColumn
adGenCSMDirectionCbrOverbookingOverride = _AdGenCSMDirectionCbrOverbookingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 18),
    _AdGenCSMDirectionCbrOverbookingOverride_Type()
)
adGenCSMDirectionCbrOverbookingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionCbrOverbookingOverride.setStatus("current")


class _AdGenCSMDirectionRtVbrOverbookingOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionRtVbrOverbookingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionRtVbrOverbookingOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionRtVbrOverbookingOverride_Object = MibTableColumn
adGenCSMDirectionRtVbrOverbookingOverride = _AdGenCSMDirectionRtVbrOverbookingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 19),
    _AdGenCSMDirectionRtVbrOverbookingOverride_Type()
)
adGenCSMDirectionRtVbrOverbookingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionRtVbrOverbookingOverride.setStatus("current")


class _AdGenCSMDirectionNrtVbrOverbookingOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionNrtVbrOverbookingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionNrtVbrOverbookingOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionNrtVbrOverbookingOverride_Object = MibTableColumn
adGenCSMDirectionNrtVbrOverbookingOverride = _AdGenCSMDirectionNrtVbrOverbookingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 20),
    _AdGenCSMDirectionNrtVbrOverbookingOverride_Type()
)
adGenCSMDirectionNrtVbrOverbookingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionNrtVbrOverbookingOverride.setStatus("current")


class _AdGenCSMDirectionNrtVbrSharingOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionNrtVbrSharingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionNrtVbrSharingOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionNrtVbrSharingOverride_Object = MibTableColumn
adGenCSMDirectionNrtVbrSharingOverride = _AdGenCSMDirectionNrtVbrSharingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 21),
    _AdGenCSMDirectionNrtVbrSharingOverride_Type()
)
adGenCSMDirectionNrtVbrSharingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionNrtVbrSharingOverride.setStatus("current")


class _AdGenCSMDirectionUbrSharingOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionUbrSharingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionUbrSharingOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionUbrSharingOverride_Object = MibTableColumn
adGenCSMDirectionUbrSharingOverride = _AdGenCSMDirectionUbrSharingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 22),
    _AdGenCSMDirectionUbrSharingOverride_Type()
)
adGenCSMDirectionUbrSharingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrSharingOverride.setStatus("current")


class _AdGenCSMDirectionUbrMaxClp1ThrshOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionUbrMaxClp1ThrshOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionUbrMaxClp1ThrshOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionUbrMaxClp1ThrshOverride_Object = MibTableColumn
adGenCSMDirectionUbrMaxClp1ThrshOverride = _AdGenCSMDirectionUbrMaxClp1ThrshOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 23),
    _AdGenCSMDirectionUbrMaxClp1ThrshOverride_Type()
)
adGenCSMDirectionUbrMaxClp1ThrshOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxClp1ThrshOverride.setStatus("current")


class _AdGenCSMDirectionUbrMaxClp0ThrshOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionUbrMaxClp0ThrshOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionUbrMaxClp0ThrshOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionUbrMaxClp0ThrshOverride_Object = MibTableColumn
adGenCSMDirectionUbrMaxClp0ThrshOverride = _AdGenCSMDirectionUbrMaxClp0ThrshOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 24),
    _AdGenCSMDirectionUbrMaxClp0ThrshOverride_Type()
)
adGenCSMDirectionUbrMaxClp0ThrshOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxClp0ThrshOverride.setStatus("current")


class _AdGenCSMDirectionUbrMaxMaxThrshOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionUbrMaxMaxThrshOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionUbrMaxMaxThrshOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionUbrMaxMaxThrshOverride_Object = MibTableColumn
adGenCSMDirectionUbrMaxMaxThrshOverride = _AdGenCSMDirectionUbrMaxMaxThrshOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 25),
    _AdGenCSMDirectionUbrMaxMaxThrshOverride_Type()
)
adGenCSMDirectionUbrMaxMaxThrshOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxMaxThrshOverride.setStatus("current")


class _AdGenCSMDirectionUbrMaxFrameMultiplierOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionUbrMaxFrameMultiplierOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionUbrMaxFrameMultiplierOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionUbrMaxFrameMultiplierOverride_Object = MibTableColumn
adGenCSMDirectionUbrMaxFrameMultiplierOverride = _AdGenCSMDirectionUbrMaxFrameMultiplierOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 26),
    _AdGenCSMDirectionUbrMaxFrameMultiplierOverride_Type()
)
adGenCSMDirectionUbrMaxFrameMultiplierOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrMaxFrameMultiplierOverride.setStatus("current")


class _AdGenCSMDirectionDefaultCDVT_Type(Unsigned32):
    """Custom type adGenCSMDirectionDefaultCDVT based on Unsigned32"""
    defaultValue = 0


_AdGenCSMDirectionDefaultCDVT_Type.__name__ = "Unsigned32"
_AdGenCSMDirectionDefaultCDVT_Object = MibTableColumn
adGenCSMDirectionDefaultCDVT = _AdGenCSMDirectionDefaultCDVT_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 27),
    _AdGenCSMDirectionDefaultCDVT_Type()
)
adGenCSMDirectionDefaultCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionDefaultCDVT.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionDefaultCDVT.setUnits("100 nanoseconds")


class _AdGenCSMDirectionAisRdiDisable_Type(TruthValue):
    """Custom type adGenCSMDirectionAisRdiDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionAisRdiDisable_Type.__name__ = "TruthValue"
_AdGenCSMDirectionAisRdiDisable_Object = MibTableColumn
adGenCSMDirectionAisRdiDisable = _AdGenCSMDirectionAisRdiDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 28),
    _AdGenCSMDirectionAisRdiDisable_Type()
)
adGenCSMDirectionAisRdiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionAisRdiDisable.setStatus("current")


class _AdGenCSMDirectionInputCdv_Type(Unsigned32):
    """Custom type adGenCSMDirectionInputCdv based on Unsigned32"""
    defaultValue = 1


_AdGenCSMDirectionInputCdv_Type.__name__ = "Unsigned32"
_AdGenCSMDirectionInputCdv_Object = MibTableColumn
adGenCSMDirectionInputCdv = _AdGenCSMDirectionInputCdv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 29),
    _AdGenCSMDirectionInputCdv_Type()
)
adGenCSMDirectionInputCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionInputCdv.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionInputCdv.setUnits("microseconds")


class _AdGenCSMDirectionOutputCdv_Type(Unsigned32):
    """Custom type adGenCSMDirectionOutputCdv based on Unsigned32"""
    defaultValue = 1


_AdGenCSMDirectionOutputCdv_Type.__name__ = "Unsigned32"
_AdGenCSMDirectionOutputCdv_Object = MibTableColumn
adGenCSMDirectionOutputCdv = _AdGenCSMDirectionOutputCdv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 30),
    _AdGenCSMDirectionOutputCdv_Type()
)
adGenCSMDirectionOutputCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionOutputCdv.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionOutputCdv.setUnits("microseconds")


class _AdGenCSMDirectionInputMaxCtd_Type(Unsigned32):
    """Custom type adGenCSMDirectionInputMaxCtd based on Unsigned32"""
    defaultValue = 21


_AdGenCSMDirectionInputMaxCtd_Type.__name__ = "Unsigned32"
_AdGenCSMDirectionInputMaxCtd_Object = MibTableColumn
adGenCSMDirectionInputMaxCtd = _AdGenCSMDirectionInputMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 31),
    _AdGenCSMDirectionInputMaxCtd_Type()
)
adGenCSMDirectionInputMaxCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionInputMaxCtd.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionInputMaxCtd.setUnits("microseconds")


class _AdGenCSMDirectionOutputMaxCtd_Type(Unsigned32):
    """Custom type adGenCSMDirectionOutputMaxCtd based on Unsigned32"""
    defaultValue = 21


_AdGenCSMDirectionOutputMaxCtd_Type.__name__ = "Unsigned32"
_AdGenCSMDirectionOutputMaxCtd_Object = MibTableColumn
adGenCSMDirectionOutputMaxCtd = _AdGenCSMDirectionOutputMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 32),
    _AdGenCSMDirectionOutputMaxCtd_Type()
)
adGenCSMDirectionOutputMaxCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionOutputMaxCtd.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMDirectionOutputMaxCtd.setUnits("microseconds")


class _AdGenCSMDirectionCbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMDirectionCbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 1


_AdGenCSMDirectionCbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMDirectionCbrClassScheduling_Object = MibTableColumn
adGenCSMDirectionCbrClassScheduling = _AdGenCSMDirectionCbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 33),
    _AdGenCSMDirectionCbrClassScheduling_Type()
)
adGenCSMDirectionCbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionCbrClassScheduling.setStatus("current")


class _AdGenCSMDirectionRtVbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMDirectionRtVbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 1


_AdGenCSMDirectionRtVbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMDirectionRtVbrClassScheduling_Object = MibTableColumn
adGenCSMDirectionRtVbrClassScheduling = _AdGenCSMDirectionRtVbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 34),
    _AdGenCSMDirectionRtVbrClassScheduling_Type()
)
adGenCSMDirectionRtVbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionRtVbrClassScheduling.setStatus("current")


class _AdGenCSMDirectionNrtVbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMDirectionNrtVbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 1


_AdGenCSMDirectionNrtVbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMDirectionNrtVbrClassScheduling_Object = MibTableColumn
adGenCSMDirectionNrtVbrClassScheduling = _AdGenCSMDirectionNrtVbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 35),
    _AdGenCSMDirectionNrtVbrClassScheduling_Type()
)
adGenCSMDirectionNrtVbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionNrtVbrClassScheduling.setStatus("current")


class _AdGenCSMDirectionUbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMDirectionUbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 3


_AdGenCSMDirectionUbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMDirectionUbrClassScheduling_Object = MibTableColumn
adGenCSMDirectionUbrClassScheduling = _AdGenCSMDirectionUbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 36),
    _AdGenCSMDirectionUbrClassScheduling_Type()
)
adGenCSMDirectionUbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrClassScheduling.setStatus("current")


class _AdGenCSMDirectionDefaultCDVTOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionDefaultCDVTOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionDefaultCDVTOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionDefaultCDVTOverride_Object = MibTableColumn
adGenCSMDirectionDefaultCDVTOverride = _AdGenCSMDirectionDefaultCDVTOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 37),
    _AdGenCSMDirectionDefaultCDVTOverride_Type()
)
adGenCSMDirectionDefaultCDVTOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionDefaultCDVTOverride.setStatus("current")


class _AdGenCSMDirectionAisRdiDisableOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionAisRdiDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionAisRdiDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionAisRdiDisableOverride_Object = MibTableColumn
adGenCSMDirectionAisRdiDisableOverride = _AdGenCSMDirectionAisRdiDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 38),
    _AdGenCSMDirectionAisRdiDisableOverride_Type()
)
adGenCSMDirectionAisRdiDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionAisRdiDisableOverride.setStatus("current")


class _AdGenCSMDirectionInputCdvOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionInputCdvOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionInputCdvOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionInputCdvOverride_Object = MibTableColumn
adGenCSMDirectionInputCdvOverride = _AdGenCSMDirectionInputCdvOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 39),
    _AdGenCSMDirectionInputCdvOverride_Type()
)
adGenCSMDirectionInputCdvOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionInputCdvOverride.setStatus("current")


class _AdGenCSMDirectionOutputCdvOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionOutputCdvOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionOutputCdvOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionOutputCdvOverride_Object = MibTableColumn
adGenCSMDirectionOutputCdvOverride = _AdGenCSMDirectionOutputCdvOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 40),
    _AdGenCSMDirectionOutputCdvOverride_Type()
)
adGenCSMDirectionOutputCdvOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionOutputCdvOverride.setStatus("current")


class _AdGenCSMDirectionInputMaxCtdOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionInputMaxCtdOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionInputMaxCtdOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionInputMaxCtdOverride_Object = MibTableColumn
adGenCSMDirectionInputMaxCtdOverride = _AdGenCSMDirectionInputMaxCtdOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 41),
    _AdGenCSMDirectionInputMaxCtdOverride_Type()
)
adGenCSMDirectionInputMaxCtdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionInputMaxCtdOverride.setStatus("current")


class _AdGenCSMDirectionOutputMaxCtdOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionOutputMaxCtdOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionOutputMaxCtdOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionOutputMaxCtdOverride_Object = MibTableColumn
adGenCSMDirectionOutputMaxCtdOverride = _AdGenCSMDirectionOutputMaxCtdOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 42),
    _AdGenCSMDirectionOutputMaxCtdOverride_Type()
)
adGenCSMDirectionOutputMaxCtdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionOutputMaxCtdOverride.setStatus("current")


class _AdGenCSMDirectionCbrClassSchedulingOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionCbrClassSchedulingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionCbrClassSchedulingOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionCbrClassSchedulingOverride_Object = MibTableColumn
adGenCSMDirectionCbrClassSchedulingOverride = _AdGenCSMDirectionCbrClassSchedulingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 43),
    _AdGenCSMDirectionCbrClassSchedulingOverride_Type()
)
adGenCSMDirectionCbrClassSchedulingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionCbrClassSchedulingOverride.setStatus("current")


class _AdGenCSMDirectionRtVbrClassSchedulingOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionRtVbrClassSchedulingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionRtVbrClassSchedulingOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionRtVbrClassSchedulingOverride_Object = MibTableColumn
adGenCSMDirectionRtVbrClassSchedulingOverride = _AdGenCSMDirectionRtVbrClassSchedulingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 44),
    _AdGenCSMDirectionRtVbrClassSchedulingOverride_Type()
)
adGenCSMDirectionRtVbrClassSchedulingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionRtVbrClassSchedulingOverride.setStatus("current")


class _AdGenCSMDirectionNrtVbrClassSchedulingOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionNrtVbrClassSchedulingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionNrtVbrClassSchedulingOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionNrtVbrClassSchedulingOverride_Object = MibTableColumn
adGenCSMDirectionNrtVbrClassSchedulingOverride = _AdGenCSMDirectionNrtVbrClassSchedulingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 45),
    _AdGenCSMDirectionNrtVbrClassSchedulingOverride_Type()
)
adGenCSMDirectionNrtVbrClassSchedulingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionNrtVbrClassSchedulingOverride.setStatus("current")


class _AdGenCSMDirectionUbrClassSchedulingOverride_Type(TruthValue):
    """Custom type adGenCSMDirectionUbrClassSchedulingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMDirectionUbrClassSchedulingOverride_Type.__name__ = "TruthValue"
_AdGenCSMDirectionUbrClassSchedulingOverride_Object = MibTableColumn
adGenCSMDirectionUbrClassSchedulingOverride = _AdGenCSMDirectionUbrClassSchedulingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 17, 1, 46),
    _AdGenCSMDirectionUbrClassSchedulingOverride_Type()
)
adGenCSMDirectionUbrClassSchedulingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMDirectionUbrClassSchedulingOverride.setStatus("current")
_AdGenCSMPortOptionTable_Object = MibTable
adGenCSMPortOptionTable = _AdGenCSMPortOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18)
)
if mibBuilder.loadTexts:
    adGenCSMPortOptionTable.setStatus("current")
_AdGenCSMPortOptionEntry_Object = MibTableRow
adGenCSMPortOptionEntry = _AdGenCSMPortOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1)
)
adGenCSMPortOptionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenCSMPortOptionEntry.setStatus("current")


class _AdGenCSMPortPolicingDisable_Type(TruthValue):
    """Custom type adGenCSMPortPolicingDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortPolicingDisable_Type.__name__ = "TruthValue"
_AdGenCSMPortPolicingDisable_Object = MibTableColumn
adGenCSMPortPolicingDisable = _AdGenCSMPortPolicingDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 1),
    _AdGenCSMPortPolicingDisable_Type()
)
adGenCSMPortPolicingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortPolicingDisable.setStatus("current")


class _AdGenCSMPortCellRateCACDisable_Type(TruthValue):
    """Custom type adGenCSMPortCellRateCACDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortCellRateCACDisable_Type.__name__ = "TruthValue"
_AdGenCSMPortCellRateCACDisable_Object = MibTableColumn
adGenCSMPortCellRateCACDisable = _AdGenCSMPortCellRateCACDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 2),
    _AdGenCSMPortCellRateCACDisable_Type()
)
adGenCSMPortCellRateCACDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortCellRateCACDisable.setStatus("current")


class _AdGenCSMPortBufferCACDisable_Type(TruthValue):
    """Custom type adGenCSMPortBufferCACDisable based on TruthValue"""
    defaultValue = 1


_AdGenCSMPortBufferCACDisable_Type.__name__ = "TruthValue"
_AdGenCSMPortBufferCACDisable_Object = MibTableColumn
adGenCSMPortBufferCACDisable = _AdGenCSMPortBufferCACDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 3),
    _AdGenCSMPortBufferCACDisable_Type()
)
adGenCSMPortBufferCACDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortBufferCACDisable.setStatus("current")


class _AdGenCSMPortCbrOverbooking_Type(Integer32):
    """Custom type adGenCSMPortCbrOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdGenCSMPortCbrOverbooking_Type.__name__ = "Integer32"
_AdGenCSMPortCbrOverbooking_Object = MibTableColumn
adGenCSMPortCbrOverbooking = _AdGenCSMPortCbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 4),
    _AdGenCSMPortCbrOverbooking_Type()
)
adGenCSMPortCbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortCbrOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortCbrOverbooking.setUnits("percent")


class _AdGenCSMPortRtVbrOverbooking_Type(Integer32):
    """Custom type adGenCSMPortRtVbrOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdGenCSMPortRtVbrOverbooking_Type.__name__ = "Integer32"
_AdGenCSMPortRtVbrOverbooking_Object = MibTableColumn
adGenCSMPortRtVbrOverbooking = _AdGenCSMPortRtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 5),
    _AdGenCSMPortRtVbrOverbooking_Type()
)
adGenCSMPortRtVbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortRtVbrOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortRtVbrOverbooking.setUnits("percent")


class _AdGenCSMPortNrtVbrOverbooking_Type(Integer32):
    """Custom type adGenCSMPortNrtVbrOverbooking based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AdGenCSMPortNrtVbrOverbooking_Type.__name__ = "Integer32"
_AdGenCSMPortNrtVbrOverbooking_Object = MibTableColumn
adGenCSMPortNrtVbrOverbooking = _AdGenCSMPortNrtVbrOverbooking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 6),
    _AdGenCSMPortNrtVbrOverbooking_Type()
)
adGenCSMPortNrtVbrOverbooking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortNrtVbrOverbooking.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortNrtVbrOverbooking.setUnits("percent")


class _AdGenCSMPortMaximumThreshold_Type(Integer32):
    """Custom type adGenCSMPortMaximumThreshold based on Integer32"""
    defaultValue = 131072

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262143),
    )


_AdGenCSMPortMaximumThreshold_Type.__name__ = "Integer32"
_AdGenCSMPortMaximumThreshold_Object = MibTableColumn
adGenCSMPortMaximumThreshold = _AdGenCSMPortMaximumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 7),
    _AdGenCSMPortMaximumThreshold_Type()
)
adGenCSMPortMaximumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortMaximumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortMaximumThreshold.setUnits("cells")


class _AdGenCSMPortUbrMaxClp1Thrsh_Type(Integer32):
    """Custom type adGenCSMPortUbrMaxClp1Thrsh based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMPortUbrMaxClp1Thrsh_Type.__name__ = "Integer32"
_AdGenCSMPortUbrMaxClp1Thrsh_Object = MibTableColumn
adGenCSMPortUbrMaxClp1Thrsh = _AdGenCSMPortUbrMaxClp1Thrsh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 8),
    _AdGenCSMPortUbrMaxClp1Thrsh_Type()
)
adGenCSMPortUbrMaxClp1Thrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxClp1Thrsh.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxClp1Thrsh.setUnits("cells")


class _AdGenCSMPortUbrMaxClp0Thrsh_Type(Integer32):
    """Custom type adGenCSMPortUbrMaxClp0Thrsh based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMPortUbrMaxClp0Thrsh_Type.__name__ = "Integer32"
_AdGenCSMPortUbrMaxClp0Thrsh_Object = MibTableColumn
adGenCSMPortUbrMaxClp0Thrsh = _AdGenCSMPortUbrMaxClp0Thrsh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 9),
    _AdGenCSMPortUbrMaxClp0Thrsh_Type()
)
adGenCSMPortUbrMaxClp0Thrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxClp0Thrsh.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxClp0Thrsh.setUnits("cells")


class _AdGenCSMPortUbrMaxMaxThrsh_Type(Integer32):
    """Custom type adGenCSMPortUbrMaxMaxThrsh based on Integer32"""
    defaultValue = 544

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMPortUbrMaxMaxThrsh_Type.__name__ = "Integer32"
_AdGenCSMPortUbrMaxMaxThrsh_Object = MibTableColumn
adGenCSMPortUbrMaxMaxThrsh = _AdGenCSMPortUbrMaxMaxThrsh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 10),
    _AdGenCSMPortUbrMaxMaxThrsh_Type()
)
adGenCSMPortUbrMaxMaxThrsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxMaxThrsh.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxMaxThrsh.setUnits("cells")


class _AdGenCSMPortUbrMaxFrameMultiplier_Type(Integer32):
    """Custom type adGenCSMPortUbrMaxFrameMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenCSMPortUbrMaxFrameMultiplier_Type.__name__ = "Integer32"
_AdGenCSMPortUbrMaxFrameMultiplier_Object = MibTableColumn
adGenCSMPortUbrMaxFrameMultiplier = _AdGenCSMPortUbrMaxFrameMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 11),
    _AdGenCSMPortUbrMaxFrameMultiplier_Type()
)
adGenCSMPortUbrMaxFrameMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxFrameMultiplier.setStatus("current")


class _AdGenCSMPortPolicingDisableOverride_Type(TruthValue):
    """Custom type adGenCSMPortPolicingDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortPolicingDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortPolicingDisableOverride_Object = MibTableColumn
adGenCSMPortPolicingDisableOverride = _AdGenCSMPortPolicingDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 12),
    _AdGenCSMPortPolicingDisableOverride_Type()
)
adGenCSMPortPolicingDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortPolicingDisableOverride.setStatus("current")


class _AdGenCSMPortCellRateCACDisableOverride_Type(TruthValue):
    """Custom type adGenCSMPortCellRateCACDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortCellRateCACDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortCellRateCACDisableOverride_Object = MibTableColumn
adGenCSMPortCellRateCACDisableOverride = _AdGenCSMPortCellRateCACDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 13),
    _AdGenCSMPortCellRateCACDisableOverride_Type()
)
adGenCSMPortCellRateCACDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortCellRateCACDisableOverride.setStatus("current")


class _AdGenCSMPortBufferCACDisableOverride_Type(TruthValue):
    """Custom type adGenCSMPortBufferCACDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortBufferCACDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortBufferCACDisableOverride_Object = MibTableColumn
adGenCSMPortBufferCACDisableOverride = _AdGenCSMPortBufferCACDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 14),
    _AdGenCSMPortBufferCACDisableOverride_Type()
)
adGenCSMPortBufferCACDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortBufferCACDisableOverride.setStatus("current")


class _AdGenCSMPortCbrOverbookingOverride_Type(TruthValue):
    """Custom type adGenCSMPortCbrOverbookingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortCbrOverbookingOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortCbrOverbookingOverride_Object = MibTableColumn
adGenCSMPortCbrOverbookingOverride = _AdGenCSMPortCbrOverbookingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 15),
    _AdGenCSMPortCbrOverbookingOverride_Type()
)
adGenCSMPortCbrOverbookingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortCbrOverbookingOverride.setStatus("current")


class _AdGenCSMPortRtVbrOverbookingOverride_Type(TruthValue):
    """Custom type adGenCSMPortRtVbrOverbookingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortRtVbrOverbookingOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortRtVbrOverbookingOverride_Object = MibTableColumn
adGenCSMPortRtVbrOverbookingOverride = _AdGenCSMPortRtVbrOverbookingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 16),
    _AdGenCSMPortRtVbrOverbookingOverride_Type()
)
adGenCSMPortRtVbrOverbookingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortRtVbrOverbookingOverride.setStatus("current")


class _AdGenCSMPortNrtVbrOverbookingOverride_Type(TruthValue):
    """Custom type adGenCSMPortNrtVbrOverbookingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortNrtVbrOverbookingOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortNrtVbrOverbookingOverride_Object = MibTableColumn
adGenCSMPortNrtVbrOverbookingOverride = _AdGenCSMPortNrtVbrOverbookingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 17),
    _AdGenCSMPortNrtVbrOverbookingOverride_Type()
)
adGenCSMPortNrtVbrOverbookingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortNrtVbrOverbookingOverride.setStatus("current")


class _AdGenCSMPortMaximumThresholdOverride_Type(TruthValue):
    """Custom type adGenCSMPortMaximumThresholdOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortMaximumThresholdOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortMaximumThresholdOverride_Object = MibTableColumn
adGenCSMPortMaximumThresholdOverride = _AdGenCSMPortMaximumThresholdOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 18),
    _AdGenCSMPortMaximumThresholdOverride_Type()
)
adGenCSMPortMaximumThresholdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortMaximumThresholdOverride.setStatus("current")


class _AdGenCSMPortUbrMaxClp1ThrshOverride_Type(TruthValue):
    """Custom type adGenCSMPortUbrMaxClp1ThrshOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortUbrMaxClp1ThrshOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortUbrMaxClp1ThrshOverride_Object = MibTableColumn
adGenCSMPortUbrMaxClp1ThrshOverride = _AdGenCSMPortUbrMaxClp1ThrshOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 19),
    _AdGenCSMPortUbrMaxClp1ThrshOverride_Type()
)
adGenCSMPortUbrMaxClp1ThrshOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxClp1ThrshOverride.setStatus("current")


class _AdGenCSMPortUbrMaxClp0ThrshOverride_Type(TruthValue):
    """Custom type adGenCSMPortUbrMaxClp0ThrshOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortUbrMaxClp0ThrshOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortUbrMaxClp0ThrshOverride_Object = MibTableColumn
adGenCSMPortUbrMaxClp0ThrshOverride = _AdGenCSMPortUbrMaxClp0ThrshOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 20),
    _AdGenCSMPortUbrMaxClp0ThrshOverride_Type()
)
adGenCSMPortUbrMaxClp0ThrshOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxClp0ThrshOverride.setStatus("current")


class _AdGenCSMPortUbrMaxMaxThrshOverride_Type(TruthValue):
    """Custom type adGenCSMPortUbrMaxMaxThrshOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortUbrMaxMaxThrshOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortUbrMaxMaxThrshOverride_Object = MibTableColumn
adGenCSMPortUbrMaxMaxThrshOverride = _AdGenCSMPortUbrMaxMaxThrshOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 21),
    _AdGenCSMPortUbrMaxMaxThrshOverride_Type()
)
adGenCSMPortUbrMaxMaxThrshOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxMaxThrshOverride.setStatus("current")


class _AdGenCSMPortUbrMaxFrameMultiplierOverride_Type(TruthValue):
    """Custom type adGenCSMPortUbrMaxFrameMultiplierOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortUbrMaxFrameMultiplierOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortUbrMaxFrameMultiplierOverride_Object = MibTableColumn
adGenCSMPortUbrMaxFrameMultiplierOverride = _AdGenCSMPortUbrMaxFrameMultiplierOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 22),
    _AdGenCSMPortUbrMaxFrameMultiplierOverride_Type()
)
adGenCSMPortUbrMaxFrameMultiplierOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrMaxFrameMultiplierOverride.setStatus("current")


class _AdGenCSMPortDefaultCDVT_Type(Unsigned32):
    """Custom type adGenCSMPortDefaultCDVT based on Unsigned32"""
    defaultValue = 0


_AdGenCSMPortDefaultCDVT_Type.__name__ = "Unsigned32"
_AdGenCSMPortDefaultCDVT_Object = MibTableColumn
adGenCSMPortDefaultCDVT = _AdGenCSMPortDefaultCDVT_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 23),
    _AdGenCSMPortDefaultCDVT_Type()
)
adGenCSMPortDefaultCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortDefaultCDVT.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortDefaultCDVT.setUnits("100 nanoseconds")


class _AdGenCSMPortAisRdiDisable_Type(TruthValue):
    """Custom type adGenCSMPortAisRdiDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortAisRdiDisable_Type.__name__ = "TruthValue"
_AdGenCSMPortAisRdiDisable_Object = MibTableColumn
adGenCSMPortAisRdiDisable = _AdGenCSMPortAisRdiDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 24),
    _AdGenCSMPortAisRdiDisable_Type()
)
adGenCSMPortAisRdiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortAisRdiDisable.setStatus("current")


class _AdGenCSMPortInputCdv_Type(Unsigned32):
    """Custom type adGenCSMPortInputCdv based on Unsigned32"""
    defaultValue = 1


_AdGenCSMPortInputCdv_Type.__name__ = "Unsigned32"
_AdGenCSMPortInputCdv_Object = MibTableColumn
adGenCSMPortInputCdv = _AdGenCSMPortInputCdv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 25),
    _AdGenCSMPortInputCdv_Type()
)
adGenCSMPortInputCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortInputCdv.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortInputCdv.setUnits("microseconds")


class _AdGenCSMPortOutputCdv_Type(Unsigned32):
    """Custom type adGenCSMPortOutputCdv based on Unsigned32"""
    defaultValue = 1


_AdGenCSMPortOutputCdv_Type.__name__ = "Unsigned32"
_AdGenCSMPortOutputCdv_Object = MibTableColumn
adGenCSMPortOutputCdv = _AdGenCSMPortOutputCdv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 26),
    _AdGenCSMPortOutputCdv_Type()
)
adGenCSMPortOutputCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortOutputCdv.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortOutputCdv.setUnits("microseconds")


class _AdGenCSMPortInputMaxCtd_Type(Unsigned32):
    """Custom type adGenCSMPortInputMaxCtd based on Unsigned32"""
    defaultValue = 21


_AdGenCSMPortInputMaxCtd_Type.__name__ = "Unsigned32"
_AdGenCSMPortInputMaxCtd_Object = MibTableColumn
adGenCSMPortInputMaxCtd = _AdGenCSMPortInputMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 27),
    _AdGenCSMPortInputMaxCtd_Type()
)
adGenCSMPortInputMaxCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortInputMaxCtd.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortInputMaxCtd.setUnits("microseconds")


class _AdGenCSMPortOutputMaxCtd_Type(Unsigned32):
    """Custom type adGenCSMPortOutputMaxCtd based on Unsigned32"""
    defaultValue = 21


_AdGenCSMPortOutputMaxCtd_Type.__name__ = "Unsigned32"
_AdGenCSMPortOutputMaxCtd_Object = MibTableColumn
adGenCSMPortOutputMaxCtd = _AdGenCSMPortOutputMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 28),
    _AdGenCSMPortOutputMaxCtd_Type()
)
adGenCSMPortOutputMaxCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortOutputMaxCtd.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMPortOutputMaxCtd.setUnits("microseconds")


class _AdGenCSMPortCbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMPortCbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 1


_AdGenCSMPortCbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMPortCbrClassScheduling_Object = MibTableColumn
adGenCSMPortCbrClassScheduling = _AdGenCSMPortCbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 29),
    _AdGenCSMPortCbrClassScheduling_Type()
)
adGenCSMPortCbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortCbrClassScheduling.setStatus("current")


class _AdGenCSMPortRtVbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMPortRtVbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 1


_AdGenCSMPortRtVbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMPortRtVbrClassScheduling_Object = MibTableColumn
adGenCSMPortRtVbrClassScheduling = _AdGenCSMPortRtVbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 30),
    _AdGenCSMPortRtVbrClassScheduling_Type()
)
adGenCSMPortRtVbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortRtVbrClassScheduling.setStatus("current")


class _AdGenCSMPortNrtVbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMPortNrtVbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 1


_AdGenCSMPortNrtVbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMPortNrtVbrClassScheduling_Object = MibTableColumn
adGenCSMPortNrtVbrClassScheduling = _AdGenCSMPortNrtVbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 31),
    _AdGenCSMPortNrtVbrClassScheduling_Type()
)
adGenCSMPortNrtVbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortNrtVbrClassScheduling.setStatus("current")


class _AdGenCSMPortUbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMPortUbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 3


_AdGenCSMPortUbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMPortUbrClassScheduling_Object = MibTableColumn
adGenCSMPortUbrClassScheduling = _AdGenCSMPortUbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 32),
    _AdGenCSMPortUbrClassScheduling_Type()
)
adGenCSMPortUbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrClassScheduling.setStatus("current")


class _AdGenCSMPortDefaultCDVTOverride_Type(TruthValue):
    """Custom type adGenCSMPortDefaultCDVTOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortDefaultCDVTOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortDefaultCDVTOverride_Object = MibTableColumn
adGenCSMPortDefaultCDVTOverride = _AdGenCSMPortDefaultCDVTOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 33),
    _AdGenCSMPortDefaultCDVTOverride_Type()
)
adGenCSMPortDefaultCDVTOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortDefaultCDVTOverride.setStatus("current")


class _AdGenCSMPortAisRdiDisableOverride_Type(TruthValue):
    """Custom type adGenCSMPortAisRdiDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortAisRdiDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortAisRdiDisableOverride_Object = MibTableColumn
adGenCSMPortAisRdiDisableOverride = _AdGenCSMPortAisRdiDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 34),
    _AdGenCSMPortAisRdiDisableOverride_Type()
)
adGenCSMPortAisRdiDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortAisRdiDisableOverride.setStatus("current")


class _AdGenCSMPortInputCdvOverride_Type(TruthValue):
    """Custom type adGenCSMPortInputCdvOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortInputCdvOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortInputCdvOverride_Object = MibTableColumn
adGenCSMPortInputCdvOverride = _AdGenCSMPortInputCdvOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 35),
    _AdGenCSMPortInputCdvOverride_Type()
)
adGenCSMPortInputCdvOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortInputCdvOverride.setStatus("current")


class _AdGenCSMPortOutputCdvOverride_Type(TruthValue):
    """Custom type adGenCSMPortOutputCdvOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortOutputCdvOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortOutputCdvOverride_Object = MibTableColumn
adGenCSMPortOutputCdvOverride = _AdGenCSMPortOutputCdvOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 36),
    _AdGenCSMPortOutputCdvOverride_Type()
)
adGenCSMPortOutputCdvOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortOutputCdvOverride.setStatus("current")


class _AdGenCSMPortInputMaxCtdOverride_Type(TruthValue):
    """Custom type adGenCSMPortInputMaxCtdOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortInputMaxCtdOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortInputMaxCtdOverride_Object = MibTableColumn
adGenCSMPortInputMaxCtdOverride = _AdGenCSMPortInputMaxCtdOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 37),
    _AdGenCSMPortInputMaxCtdOverride_Type()
)
adGenCSMPortInputMaxCtdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortInputMaxCtdOverride.setStatus("current")


class _AdGenCSMPortOutputMaxCtdOverride_Type(TruthValue):
    """Custom type adGenCSMPortOutputMaxCtdOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortOutputMaxCtdOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortOutputMaxCtdOverride_Object = MibTableColumn
adGenCSMPortOutputMaxCtdOverride = _AdGenCSMPortOutputMaxCtdOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 38),
    _AdGenCSMPortOutputMaxCtdOverride_Type()
)
adGenCSMPortOutputMaxCtdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortOutputMaxCtdOverride.setStatus("current")


class _AdGenCSMPortCbrClassSchedulingOverride_Type(TruthValue):
    """Custom type adGenCSMPortCbrClassSchedulingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortCbrClassSchedulingOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortCbrClassSchedulingOverride_Object = MibTableColumn
adGenCSMPortCbrClassSchedulingOverride = _AdGenCSMPortCbrClassSchedulingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 39),
    _AdGenCSMPortCbrClassSchedulingOverride_Type()
)
adGenCSMPortCbrClassSchedulingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortCbrClassSchedulingOverride.setStatus("current")


class _AdGenCSMPortRtVbrClassSchedulingOverride_Type(TruthValue):
    """Custom type adGenCSMPortRtVbrClassSchedulingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortRtVbrClassSchedulingOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortRtVbrClassSchedulingOverride_Object = MibTableColumn
adGenCSMPortRtVbrClassSchedulingOverride = _AdGenCSMPortRtVbrClassSchedulingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 40),
    _AdGenCSMPortRtVbrClassSchedulingOverride_Type()
)
adGenCSMPortRtVbrClassSchedulingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortRtVbrClassSchedulingOverride.setStatus("current")


class _AdGenCSMPortNrtVbrClassSchedulingOverride_Type(TruthValue):
    """Custom type adGenCSMPortNrtVbrClassSchedulingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortNrtVbrClassSchedulingOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortNrtVbrClassSchedulingOverride_Object = MibTableColumn
adGenCSMPortNrtVbrClassSchedulingOverride = _AdGenCSMPortNrtVbrClassSchedulingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 41),
    _AdGenCSMPortNrtVbrClassSchedulingOverride_Type()
)
adGenCSMPortNrtVbrClassSchedulingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortNrtVbrClassSchedulingOverride.setStatus("current")


class _AdGenCSMPortUbrClassSchedulingOverride_Type(TruthValue):
    """Custom type adGenCSMPortUbrClassSchedulingOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMPortUbrClassSchedulingOverride_Type.__name__ = "TruthValue"
_AdGenCSMPortUbrClassSchedulingOverride_Object = MibTableColumn
adGenCSMPortUbrClassSchedulingOverride = _AdGenCSMPortUbrClassSchedulingOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 18, 1, 42),
    _AdGenCSMPortUbrClassSchedulingOverride_Type()
)
adGenCSMPortUbrClassSchedulingOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMPortUbrClassSchedulingOverride.setStatus("current")
_AdGenCSMClassOptionTable_Object = MibTable
adGenCSMClassOptionTable = _AdGenCSMClassOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19)
)
if mibBuilder.loadTexts:
    adGenCSMClassOptionTable.setStatus("current")
_AdGenCSMClassOptionEntry_Object = MibTableRow
adGenCSMClassOptionEntry = _AdGenCSMClassOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1)
)
adGenCSMClassOptionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENCSM2-MIB", "adGenAtmServiceCategory"),
)
if mibBuilder.loadTexts:
    adGenCSMClassOptionEntry.setStatus("current")
_AdGenAtmServiceCategory_Type = AtmServiceCategory
_AdGenAtmServiceCategory_Object = MibTableColumn
adGenAtmServiceCategory = _AdGenAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1, 1),
    _AdGenAtmServiceCategory_Type()
)
adGenAtmServiceCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenAtmServiceCategory.setStatus("current")


class _AdGenCSMClassPolicingDisable_Type(TruthValue):
    """Custom type adGenCSMClassPolicingDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMClassPolicingDisable_Type.__name__ = "TruthValue"
_AdGenCSMClassPolicingDisable_Object = MibTableColumn
adGenCSMClassPolicingDisable = _AdGenCSMClassPolicingDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1, 2),
    _AdGenCSMClassPolicingDisable_Type()
)
adGenCSMClassPolicingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMClassPolicingDisable.setStatus("current")


class _AdGenCSMClassCellRateCACDisable_Type(TruthValue):
    """Custom type adGenCSMClassCellRateCACDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMClassCellRateCACDisable_Type.__name__ = "TruthValue"
_AdGenCSMClassCellRateCACDisable_Object = MibTableColumn
adGenCSMClassCellRateCACDisable = _AdGenCSMClassCellRateCACDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1, 3),
    _AdGenCSMClassCellRateCACDisable_Type()
)
adGenCSMClassCellRateCACDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMClassCellRateCACDisable.setStatus("current")


class _AdGenCSMClassBufferCACDisable_Type(TruthValue):
    """Custom type adGenCSMClassBufferCACDisable based on TruthValue"""
    defaultValue = 1


_AdGenCSMClassBufferCACDisable_Type.__name__ = "TruthValue"
_AdGenCSMClassBufferCACDisable_Object = MibTableColumn
adGenCSMClassBufferCACDisable = _AdGenCSMClassBufferCACDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1, 4),
    _AdGenCSMClassBufferCACDisable_Type()
)
adGenCSMClassBufferCACDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMClassBufferCACDisable.setStatus("current")


class _AdGenCSMClassMaximumThreshold_Type(Integer32):
    """Custom type adGenCSMClassMaximumThreshold based on Integer32"""
    defaultValue = 8091

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262143),
    )


_AdGenCSMClassMaximumThreshold_Type.__name__ = "Integer32"
_AdGenCSMClassMaximumThreshold_Object = MibTableColumn
adGenCSMClassMaximumThreshold = _AdGenCSMClassMaximumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1, 5),
    _AdGenCSMClassMaximumThreshold_Type()
)
adGenCSMClassMaximumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMClassMaximumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMClassMaximumThreshold.setUnits("cells")


class _AdGenCSMClassPolicingDisableOverride_Type(TruthValue):
    """Custom type adGenCSMClassPolicingDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMClassPolicingDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMClassPolicingDisableOverride_Object = MibTableColumn
adGenCSMClassPolicingDisableOverride = _AdGenCSMClassPolicingDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1, 6),
    _AdGenCSMClassPolicingDisableOverride_Type()
)
adGenCSMClassPolicingDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMClassPolicingDisableOverride.setStatus("current")


class _AdGenCSMClassCellRateCACDisableOverride_Type(TruthValue):
    """Custom type adGenCSMClassCellRateCACDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMClassCellRateCACDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMClassCellRateCACDisableOverride_Object = MibTableColumn
adGenCSMClassCellRateCACDisableOverride = _AdGenCSMClassCellRateCACDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1, 7),
    _AdGenCSMClassCellRateCACDisableOverride_Type()
)
adGenCSMClassCellRateCACDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMClassCellRateCACDisableOverride.setStatus("current")


class _AdGenCSMClassBufferCACDisableOverride_Type(TruthValue):
    """Custom type adGenCSMClassBufferCACDisableOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMClassBufferCACDisableOverride_Type.__name__ = "TruthValue"
_AdGenCSMClassBufferCACDisableOverride_Object = MibTableColumn
adGenCSMClassBufferCACDisableOverride = _AdGenCSMClassBufferCACDisableOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1, 8),
    _AdGenCSMClassBufferCACDisableOverride_Type()
)
adGenCSMClassBufferCACDisableOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMClassBufferCACDisableOverride.setStatus("current")


class _AdGenCSMClassMaximumThresholdOverride_Type(TruthValue):
    """Custom type adGenCSMClassMaximumThresholdOverride based on TruthValue"""
    defaultValue = 2


_AdGenCSMClassMaximumThresholdOverride_Type.__name__ = "TruthValue"
_AdGenCSMClassMaximumThresholdOverride_Object = MibTableColumn
adGenCSMClassMaximumThresholdOverride = _AdGenCSMClassMaximumThresholdOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 19, 1, 9),
    _AdGenCSMClassMaximumThresholdOverride_Type()
)
adGenCSMClassMaximumThresholdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMClassMaximumThresholdOverride.setStatus("current")


class _AdGenCSMShelfDefaultCDVT_Type(Unsigned32):
    """Custom type adGenCSMShelfDefaultCDVT based on Unsigned32"""
    defaultValue = 0


_AdGenCSMShelfDefaultCDVT_Type.__name__ = "Unsigned32"
_AdGenCSMShelfDefaultCDVT_Object = MibScalar
adGenCSMShelfDefaultCDVT = _AdGenCSMShelfDefaultCDVT_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 20),
    _AdGenCSMShelfDefaultCDVT_Type()
)
adGenCSMShelfDefaultCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfDefaultCDVT.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfDefaultCDVT.setUnits("100 nanoseconds")


class _AdGenCSMShelfAisRdiDisable_Type(TruthValue):
    """Custom type adGenCSMShelfAisRdiDisable based on TruthValue"""
    defaultValue = 2


_AdGenCSMShelfAisRdiDisable_Type.__name__ = "TruthValue"
_AdGenCSMShelfAisRdiDisable_Object = MibScalar
adGenCSMShelfAisRdiDisable = _AdGenCSMShelfAisRdiDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 21),
    _AdGenCSMShelfAisRdiDisable_Type()
)
adGenCSMShelfAisRdiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfAisRdiDisable.setStatus("current")


class _AdGenCSMShelfInputCdv_Type(Unsigned32):
    """Custom type adGenCSMShelfInputCdv based on Unsigned32"""
    defaultValue = 1


_AdGenCSMShelfInputCdv_Type.__name__ = "Unsigned32"
_AdGenCSMShelfInputCdv_Object = MibScalar
adGenCSMShelfInputCdv = _AdGenCSMShelfInputCdv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 22),
    _AdGenCSMShelfInputCdv_Type()
)
adGenCSMShelfInputCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfInputCdv.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfInputCdv.setUnits("microseconds")


class _AdGenCSMShelfOutputCdv_Type(Unsigned32):
    """Custom type adGenCSMShelfOutputCdv based on Unsigned32"""
    defaultValue = 1


_AdGenCSMShelfOutputCdv_Type.__name__ = "Unsigned32"
_AdGenCSMShelfOutputCdv_Object = MibScalar
adGenCSMShelfOutputCdv = _AdGenCSMShelfOutputCdv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 23),
    _AdGenCSMShelfOutputCdv_Type()
)
adGenCSMShelfOutputCdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfOutputCdv.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfOutputCdv.setUnits("microseconds")


class _AdGenCSMShelfInputMaxCtd_Type(Unsigned32):
    """Custom type adGenCSMShelfInputMaxCtd based on Unsigned32"""
    defaultValue = 21


_AdGenCSMShelfInputMaxCtd_Type.__name__ = "Unsigned32"
_AdGenCSMShelfInputMaxCtd_Object = MibScalar
adGenCSMShelfInputMaxCtd = _AdGenCSMShelfInputMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 24),
    _AdGenCSMShelfInputMaxCtd_Type()
)
adGenCSMShelfInputMaxCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfInputMaxCtd.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfInputMaxCtd.setUnits("microseconds")


class _AdGenCSMShelfOutputMaxCtd_Type(Unsigned32):
    """Custom type adGenCSMShelfOutputMaxCtd based on Unsigned32"""
    defaultValue = 21


_AdGenCSMShelfOutputMaxCtd_Type.__name__ = "Unsigned32"
_AdGenCSMShelfOutputMaxCtd_Object = MibScalar
adGenCSMShelfOutputMaxCtd = _AdGenCSMShelfOutputMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 25),
    _AdGenCSMShelfOutputMaxCtd_Type()
)
adGenCSMShelfOutputMaxCtd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfOutputMaxCtd.setStatus("current")
if mibBuilder.loadTexts:
    adGenCSMShelfOutputMaxCtd.setUnits("microseconds")


class _AdGenCSMShelfCbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMShelfCbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 1


_AdGenCSMShelfCbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMShelfCbrClassScheduling_Object = MibScalar
adGenCSMShelfCbrClassScheduling = _AdGenCSMShelfCbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 26),
    _AdGenCSMShelfCbrClassScheduling_Type()
)
adGenCSMShelfCbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfCbrClassScheduling.setStatus("current")


class _AdGenCSMShelfRtVbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMShelfRtVbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 1


_AdGenCSMShelfRtVbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMShelfRtVbrClassScheduling_Object = MibScalar
adGenCSMShelfRtVbrClassScheduling = _AdGenCSMShelfRtVbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 27),
    _AdGenCSMShelfRtVbrClassScheduling_Type()
)
adGenCSMShelfRtVbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfRtVbrClassScheduling.setStatus("current")


class _AdGenCSMShelfNrtVbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMShelfNrtVbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 1


_AdGenCSMShelfNrtVbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMShelfNrtVbrClassScheduling_Object = MibScalar
adGenCSMShelfNrtVbrClassScheduling = _AdGenCSMShelfNrtVbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 28),
    _AdGenCSMShelfNrtVbrClassScheduling_Type()
)
adGenCSMShelfNrtVbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfNrtVbrClassScheduling.setStatus("current")


class _AdGenCSMShelfUbrClassScheduling_Type(AdGenCSMClassScheduling):
    """Custom type adGenCSMShelfUbrClassScheduling based on AdGenCSMClassScheduling"""
    defaultValue = 3


_AdGenCSMShelfUbrClassScheduling_Type.__name__ = "AdGenCSMClassScheduling"
_AdGenCSMShelfUbrClassScheduling_Object = MibScalar
adGenCSMShelfUbrClassScheduling = _AdGenCSMShelfUbrClassScheduling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 29),
    _AdGenCSMShelfUbrClassScheduling_Type()
)
adGenCSMShelfUbrClassScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrClassScheduling.setStatus("current")


class _AdGenCSMShelfCbrShaping_Type(TruthValue):
    """Custom type adGenCSMShelfCbrShaping based on TruthValue"""
    defaultValue = 2


_AdGenCSMShelfCbrShaping_Type.__name__ = "TruthValue"
_AdGenCSMShelfCbrShaping_Object = MibScalar
adGenCSMShelfCbrShaping = _AdGenCSMShelfCbrShaping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 30),
    _AdGenCSMShelfCbrShaping_Type()
)
adGenCSMShelfCbrShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfCbrShaping.setStatus("current")


class _AdGenCSMShelfRtVbrShaping_Type(TruthValue):
    """Custom type adGenCSMShelfRtVbrShaping based on TruthValue"""
    defaultValue = 2


_AdGenCSMShelfRtVbrShaping_Type.__name__ = "TruthValue"
_AdGenCSMShelfRtVbrShaping_Object = MibScalar
adGenCSMShelfRtVbrShaping = _AdGenCSMShelfRtVbrShaping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 31),
    _AdGenCSMShelfRtVbrShaping_Type()
)
adGenCSMShelfRtVbrShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfRtVbrShaping.setStatus("current")


class _AdGenCSMShelfNrtVbrShaping_Type(TruthValue):
    """Custom type adGenCSMShelfNrtVbrShaping based on TruthValue"""
    defaultValue = 2


_AdGenCSMShelfNrtVbrShaping_Type.__name__ = "TruthValue"
_AdGenCSMShelfNrtVbrShaping_Object = MibScalar
adGenCSMShelfNrtVbrShaping = _AdGenCSMShelfNrtVbrShaping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 32),
    _AdGenCSMShelfNrtVbrShaping_Type()
)
adGenCSMShelfNrtVbrShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfNrtVbrShaping.setStatus("current")


class _AdGenCSMShelfUbrShaping_Type(TruthValue):
    """Custom type adGenCSMShelfUbrShaping based on TruthValue"""
    defaultValue = 2


_AdGenCSMShelfUbrShaping_Type.__name__ = "TruthValue"
_AdGenCSMShelfUbrShaping_Object = MibScalar
adGenCSMShelfUbrShaping = _AdGenCSMShelfUbrShaping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 6, 33),
    _AdGenCSMShelfUbrShaping_Type()
)
adGenCSMShelfUbrShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenCSMShelfUbrShaping.setStatus("current")
_AdGenCSMMonitor_ObjectIdentity = ObjectIdentity
adGenCSMMonitor = _AdGenCSMMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7)
)


class _AdGenCSMMonitorSessionIndexNext_Type(Unsigned32):
    """Custom type adGenCSMMonitorSessionIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenCSMMonitorSessionIndexNext_Type.__name__ = "Unsigned32"
_AdGenCSMMonitorSessionIndexNext_Object = MibScalar
adGenCSMMonitorSessionIndexNext = _AdGenCSMMonitorSessionIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 1),
    _AdGenCSMMonitorSessionIndexNext_Type()
)
adGenCSMMonitorSessionIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionIndexNext.setStatus("current")
_AdGenCSMMonitorSessionTable_Object = MibTable
adGenCSMMonitorSessionTable = _AdGenCSMMonitorSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2)
)
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionTable.setStatus("current")
_AdGenCSMMonitorSessionEntry_Object = MibTableRow
adGenCSMMonitorSessionEntry = _AdGenCSMMonitorSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1)
)
adGenCSMMonitorSessionEntry.setIndexNames(
    (0, "ADTRAN-GENCSM2-MIB", "adGenCSMMonitorSessionId"),
)
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionEntry.setStatus("current")


class _AdGenCSMMonitorSessionId_Type(Unsigned32):
    """Custom type adGenCSMMonitorSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AdGenCSMMonitorSessionId_Type.__name__ = "Unsigned32"
_AdGenCSMMonitorSessionId_Object = MibTableColumn
adGenCSMMonitorSessionId = _AdGenCSMMonitorSessionId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 1),
    _AdGenCSMMonitorSessionId_Type()
)
adGenCSMMonitorSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionId.setStatus("current")


class _AdGenCSMMonitorSessionName_Type(OctetString):
    """Custom type adGenCSMMonitorSessionName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdGenCSMMonitorSessionName_Type.__name__ = "OctetString"
_AdGenCSMMonitorSessionName_Object = MibTableColumn
adGenCSMMonitorSessionName = _AdGenCSMMonitorSessionName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 2),
    _AdGenCSMMonitorSessionName_Type()
)
adGenCSMMonitorSessionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionName.setStatus("current")


class _AdGenCSMMonitorSessionDescription_Type(OctetString):
    """Custom type adGenCSMMonitorSessionDescription based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 236),
    )


_AdGenCSMMonitorSessionDescription_Type.__name__ = "OctetString"
_AdGenCSMMonitorSessionDescription_Object = MibTableColumn
adGenCSMMonitorSessionDescription = _AdGenCSMMonitorSessionDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 3),
    _AdGenCSMMonitorSessionDescription_Type()
)
adGenCSMMonitorSessionDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionDescription.setStatus("current")
_AdGenCSMMonitorSessionRowStatus_Type = RowStatus
_AdGenCSMMonitorSessionRowStatus_Object = MibTableColumn
adGenCSMMonitorSessionRowStatus = _AdGenCSMMonitorSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 4),
    _AdGenCSMMonitorSessionRowStatus_Type()
)
adGenCSMMonitorSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionRowStatus.setStatus("current")
_AdGenCSMMonitorSessionStartTimeStamp_Type = TimeStamp
_AdGenCSMMonitorSessionStartTimeStamp_Object = MibTableColumn
adGenCSMMonitorSessionStartTimeStamp = _AdGenCSMMonitorSessionStartTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 5),
    _AdGenCSMMonitorSessionStartTimeStamp_Type()
)
adGenCSMMonitorSessionStartTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionStartTimeStamp.setStatus("current")


class _AdGenCSMMonitorSessionScope_Type(AdGenCSMMonitorScope):
    """Custom type adGenCSMMonitorSessionScope based on AdGenCSMMonitorScope"""
    defaultValue = 1


_AdGenCSMMonitorSessionScope_Type.__name__ = "AdGenCSMMonitorScope"
_AdGenCSMMonitorSessionScope_Object = MibTableColumn
adGenCSMMonitorSessionScope = _AdGenCSMMonitorSessionScope_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 6),
    _AdGenCSMMonitorSessionScope_Type()
)
adGenCSMMonitorSessionScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionScope.setStatus("current")


class _AdGenCSMMonitorSessionMaxIntervals_Type(Unsigned32):
    """Custom type adGenCSMMonitorSessionMaxIntervals based on Unsigned32"""
    defaultValue = 0


_AdGenCSMMonitorSessionMaxIntervals_Type.__name__ = "Unsigned32"
_AdGenCSMMonitorSessionMaxIntervals_Object = MibTableColumn
adGenCSMMonitorSessionMaxIntervals = _AdGenCSMMonitorSessionMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 7),
    _AdGenCSMMonitorSessionMaxIntervals_Type()
)
adGenCSMMonitorSessionMaxIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionMaxIntervals.setStatus("current")


class _AdGenCSMMonitorSessionIntervalDuration_Type(Integer32):
    """Custom type adGenCSMMonitorSessionIntervalDuration based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_AdGenCSMMonitorSessionIntervalDuration_Type.__name__ = "Integer32"
_AdGenCSMMonitorSessionIntervalDuration_Object = MibTableColumn
adGenCSMMonitorSessionIntervalDuration = _AdGenCSMMonitorSessionIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 8),
    _AdGenCSMMonitorSessionIntervalDuration_Type()
)
adGenCSMMonitorSessionIntervalDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionIntervalDuration.setStatus("current")


class _AdGenCSMMonitorSessionCacheInterval_Type(Integer32):
    """Custom type adGenCSMMonitorSessionCacheInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AdGenCSMMonitorSessionCacheInterval_Type.__name__ = "Integer32"
_AdGenCSMMonitorSessionCacheInterval_Object = MibTableColumn
adGenCSMMonitorSessionCacheInterval = _AdGenCSMMonitorSessionCacheInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 9),
    _AdGenCSMMonitorSessionCacheInterval_Type()
)
adGenCSMMonitorSessionCacheInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionCacheInterval.setStatus("current")
_AdGenCSMMonitorSessionElapsedIntervals_Type = Counter32
_AdGenCSMMonitorSessionElapsedIntervals_Object = MibTableColumn
adGenCSMMonitorSessionElapsedIntervals = _AdGenCSMMonitorSessionElapsedIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 10),
    _AdGenCSMMonitorSessionElapsedIntervals_Type()
)
adGenCSMMonitorSessionElapsedIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionElapsedIntervals.setStatus("current")


class _AdGenCSMMonitorSessionClasses_Type(Integer32):
    """Custom type adGenCSMMonitorSessionClasses based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AdGenCSMMonitorSessionClasses_Type.__name__ = "Integer32"
_AdGenCSMMonitorSessionClasses_Object = MibTableColumn
adGenCSMMonitorSessionClasses = _AdGenCSMMonitorSessionClasses_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 11),
    _AdGenCSMMonitorSessionClasses_Type()
)
adGenCSMMonitorSessionClasses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionClasses.setStatus("current")


class _AdGenCSMMonitorSessionParam1_Type(Unsigned32):
    """Custom type adGenCSMMonitorSessionParam1 based on Unsigned32"""
    defaultValue = 0


_AdGenCSMMonitorSessionParam1_Type.__name__ = "Unsigned32"
_AdGenCSMMonitorSessionParam1_Object = MibTableColumn
adGenCSMMonitorSessionParam1 = _AdGenCSMMonitorSessionParam1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 12),
    _AdGenCSMMonitorSessionParam1_Type()
)
adGenCSMMonitorSessionParam1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionParam1.setStatus("current")


class _AdGenCSMMonitorSessionParam2_Type(Unsigned32):
    """Custom type adGenCSMMonitorSessionParam2 based on Unsigned32"""
    defaultValue = 0


_AdGenCSMMonitorSessionParam2_Type.__name__ = "Unsigned32"
_AdGenCSMMonitorSessionParam2_Object = MibTableColumn
adGenCSMMonitorSessionParam2 = _AdGenCSMMonitorSessionParam2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 13),
    _AdGenCSMMonitorSessionParam2_Type()
)
adGenCSMMonitorSessionParam2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionParam2.setStatus("current")


class _AdGenCSMMonitorSessionParam3_Type(Unsigned32):
    """Custom type adGenCSMMonitorSessionParam3 based on Unsigned32"""
    defaultValue = 0


_AdGenCSMMonitorSessionParam3_Type.__name__ = "Unsigned32"
_AdGenCSMMonitorSessionParam3_Object = MibTableColumn
adGenCSMMonitorSessionParam3 = _AdGenCSMMonitorSessionParam3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 2, 1, 14),
    _AdGenCSMMonitorSessionParam3_Type()
)
adGenCSMMonitorSessionParam3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenCSMMonitorSessionParam3.setStatus("current")
_AdGenCSMMonitorCounterTable_Object = MibTable
adGenCSMMonitorCounterTable = _AdGenCSMMonitorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3)
)
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterTable.setStatus("current")
_AdGenCSMMonitorCounterEntry_Object = MibTableRow
adGenCSMMonitorCounterEntry = _AdGenCSMMonitorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1)
)
adGenCSMMonitorCounterEntry.setIndexNames(
    (0, "ADTRAN-GENCSM2-MIB", "adGenCSMMonitorCounterType"),
    (0, "ADTRAN-GENCSM2-MIB", "adGenCSMMonitorSessionId"),
)
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterEntry.setStatus("current")
_AdGenCSMMonitorCounterType_Type = AdGenCSMMonitorCounterType
_AdGenCSMMonitorCounterType_Object = MibTableColumn
adGenCSMMonitorCounterType = _AdGenCSMMonitorCounterType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 1),
    _AdGenCSMMonitorCounterType_Type()
)
adGenCSMMonitorCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterType.setStatus("current")
_AdGenCSMMonitorCounterTimeStamp_Type = TimeStamp
_AdGenCSMMonitorCounterTimeStamp_Object = MibTableColumn
adGenCSMMonitorCounterTimeStamp = _AdGenCSMMonitorCounterTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 2),
    _AdGenCSMMonitorCounterTimeStamp_Type()
)
adGenCSMMonitorCounterTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterTimeStamp.setStatus("current")
_AdGenCSMMonitorCounterInterval_Type = Integer32
_AdGenCSMMonitorCounterInterval_Object = MibTableColumn
adGenCSMMonitorCounterInterval = _AdGenCSMMonitorCounterInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 3),
    _AdGenCSMMonitorCounterInterval_Type()
)
adGenCSMMonitorCounterInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterInterval.setStatus("current")
_AdGenCSMMonitorCounterTxCells_Type = Counter32
_AdGenCSMMonitorCounterTxCells_Object = MibTableColumn
adGenCSMMonitorCounterTxCells = _AdGenCSMMonitorCounterTxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 4),
    _AdGenCSMMonitorCounterTxCells_Type()
)
adGenCSMMonitorCounterTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterTxCells.setStatus("current")
_AdGenCSMMonitorCounterTxErrors_Type = Counter32
_AdGenCSMMonitorCounterTxErrors_Object = MibTableColumn
adGenCSMMonitorCounterTxErrors = _AdGenCSMMonitorCounterTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 5),
    _AdGenCSMMonitorCounterTxErrors_Type()
)
adGenCSMMonitorCounterTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterTxErrors.setStatus("current")
_AdGenCSMMonitorCounterRxCells_Type = Counter32
_AdGenCSMMonitorCounterRxCells_Object = MibTableColumn
adGenCSMMonitorCounterRxCells = _AdGenCSMMonitorCounterRxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 6),
    _AdGenCSMMonitorCounterRxCells_Type()
)
adGenCSMMonitorCounterRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterRxCells.setStatus("current")
_AdGenCSMMonitorCounterRxOAM_Type = Counter32
_AdGenCSMMonitorCounterRxOAM_Object = MibTableColumn
adGenCSMMonitorCounterRxOAM = _AdGenCSMMonitorCounterRxOAM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 7),
    _AdGenCSMMonitorCounterRxOAM_Type()
)
adGenCSMMonitorCounterRxOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterRxOAM.setStatus("current")
_AdGenCSMMonitorCounterRxDiscardPolicingClp0_Type = Counter32
_AdGenCSMMonitorCounterRxDiscardPolicingClp0_Object = MibTableColumn
adGenCSMMonitorCounterRxDiscardPolicingClp0 = _AdGenCSMMonitorCounterRxDiscardPolicingClp0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 8),
    _AdGenCSMMonitorCounterRxDiscardPolicingClp0_Type()
)
adGenCSMMonitorCounterRxDiscardPolicingClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterRxDiscardPolicingClp0.setStatus("current")
_AdGenCSMMonitorCounterRxDiscardPolicingClp01_Type = Counter32
_AdGenCSMMonitorCounterRxDiscardPolicingClp01_Object = MibTableColumn
adGenCSMMonitorCounterRxDiscardPolicingClp01 = _AdGenCSMMonitorCounterRxDiscardPolicingClp01_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 9),
    _AdGenCSMMonitorCounterRxDiscardPolicingClp01_Type()
)
adGenCSMMonitorCounterRxDiscardPolicingClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterRxDiscardPolicingClp01.setStatus("current")
_AdGenCSMMonitorCounterRxTaggedClp0_Type = Counter32
_AdGenCSMMonitorCounterRxTaggedClp0_Object = MibTableColumn
adGenCSMMonitorCounterRxTaggedClp0 = _AdGenCSMMonitorCounterRxTaggedClp0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 10),
    _AdGenCSMMonitorCounterRxTaggedClp0_Type()
)
adGenCSMMonitorCounterRxTaggedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterRxTaggedClp0.setStatus("current")
_AdGenCSMMonitorCounterRxErrors_Type = Counter32
_AdGenCSMMonitorCounterRxErrors_Object = MibTableColumn
adGenCSMMonitorCounterRxErrors = _AdGenCSMMonitorCounterRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 3, 1, 11),
    _AdGenCSMMonitorCounterRxErrors_Type()
)
adGenCSMMonitorCounterRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterRxErrors.setStatus("current")
_AdGenCSMMonitorCounterHistoryTable_Object = MibTable
adGenCSMMonitorCounterHistoryTable = _AdGenCSMMonitorCounterHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4)
)
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryTable.setStatus("current")
_AdGenCSMMonitorCounterHistoryEntry_Object = MibTableRow
adGenCSMMonitorCounterHistoryEntry = _AdGenCSMMonitorCounterHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1)
)
adGenCSMMonitorCounterHistoryEntry.setIndexNames(
    (0, "ADTRAN-GENCSM2-MIB", "adGenCSMMonitorSessionId"),
    (0, "ADTRAN-GENCSM2-MIB", "adGenCSMMonitorCounterInterval"),
)
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryEntry.setStatus("current")
_AdGenCSMMonitorCounterHistoryTxCells_Type = Counter32
_AdGenCSMMonitorCounterHistoryTxCells_Object = MibTableColumn
adGenCSMMonitorCounterHistoryTxCells = _AdGenCSMMonitorCounterHistoryTxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1, 1),
    _AdGenCSMMonitorCounterHistoryTxCells_Type()
)
adGenCSMMonitorCounterHistoryTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryTxCells.setStatus("current")
_AdGenCSMMonitorCounterHistoryTxErrors_Type = Counter32
_AdGenCSMMonitorCounterHistoryTxErrors_Object = MibTableColumn
adGenCSMMonitorCounterHistoryTxErrors = _AdGenCSMMonitorCounterHistoryTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1, 2),
    _AdGenCSMMonitorCounterHistoryTxErrors_Type()
)
adGenCSMMonitorCounterHistoryTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryTxErrors.setStatus("current")
_AdGenCSMMonitorCounterHistoryRxCells_Type = Counter32
_AdGenCSMMonitorCounterHistoryRxCells_Object = MibTableColumn
adGenCSMMonitorCounterHistoryRxCells = _AdGenCSMMonitorCounterHistoryRxCells_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1, 3),
    _AdGenCSMMonitorCounterHistoryRxCells_Type()
)
adGenCSMMonitorCounterHistoryRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryRxCells.setStatus("current")
_AdGenCSMMonitorCounterHistoryRxOAM_Type = Counter32
_AdGenCSMMonitorCounterHistoryRxOAM_Object = MibTableColumn
adGenCSMMonitorCounterHistoryRxOAM = _AdGenCSMMonitorCounterHistoryRxOAM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1, 4),
    _AdGenCSMMonitorCounterHistoryRxOAM_Type()
)
adGenCSMMonitorCounterHistoryRxOAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryRxOAM.setStatus("current")
_AdGenCSMMonitorCounterHistoryRxDiscardPolicingClp0_Type = Counter32
_AdGenCSMMonitorCounterHistoryRxDiscardPolicingClp0_Object = MibTableColumn
adGenCSMMonitorCounterHistoryRxDiscardPolicingClp0 = _AdGenCSMMonitorCounterHistoryRxDiscardPolicingClp0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1, 5),
    _AdGenCSMMonitorCounterHistoryRxDiscardPolicingClp0_Type()
)
adGenCSMMonitorCounterHistoryRxDiscardPolicingClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryRxDiscardPolicingClp0.setStatus("current")
_AdGenCSMMonitorCounterHistoryRxDiscardPolicingClp01_Type = Counter32
_AdGenCSMMonitorCounterHistoryRxDiscardPolicingClp01_Object = MibTableColumn
adGenCSMMonitorCounterHistoryRxDiscardPolicingClp01 = _AdGenCSMMonitorCounterHistoryRxDiscardPolicingClp01_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1, 6),
    _AdGenCSMMonitorCounterHistoryRxDiscardPolicingClp01_Type()
)
adGenCSMMonitorCounterHistoryRxDiscardPolicingClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryRxDiscardPolicingClp01.setStatus("current")
_AdGenCSMMonitorCounterHistoryRxTaggedClp0_Type = Counter32
_AdGenCSMMonitorCounterHistoryRxTaggedClp0_Object = MibTableColumn
adGenCSMMonitorCounterHistoryRxTaggedClp0 = _AdGenCSMMonitorCounterHistoryRxTaggedClp0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1, 7),
    _AdGenCSMMonitorCounterHistoryRxTaggedClp0_Type()
)
adGenCSMMonitorCounterHistoryRxTaggedClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryRxTaggedClp0.setStatus("current")
_AdGenCSMMonitorCounterHistoryRxErrors_Type = Counter32
_AdGenCSMMonitorCounterHistoryRxErrors_Object = MibTableColumn
adGenCSMMonitorCounterHistoryRxErrors = _AdGenCSMMonitorCounterHistoryRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1, 8),
    _AdGenCSMMonitorCounterHistoryRxErrors_Type()
)
adGenCSMMonitorCounterHistoryRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryRxErrors.setStatus("current")
_AdGenCSMMonitorCounterHistoryTimeStamp_Type = TimeStamp
_AdGenCSMMonitorCounterHistoryTimeStamp_Object = MibTableColumn
adGenCSMMonitorCounterHistoryTimeStamp = _AdGenCSMMonitorCounterHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 36, 7, 4, 1, 11),
    _AdGenCSMMonitorCounterHistoryTimeStamp_Type()
)
adGenCSMMonitorCounterHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenCSMMonitorCounterHistoryTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENCSM2-MIB",
    **{"AdGenCSMDirection": AdGenCSMDirection,
       "AdGenCsmOamIdv2": AdGenCsmOamIdv2,
       "AdGenCSMClassScheduling": AdGenCSMClassScheduling,
       "AdGenCSMMonitorScope": AdGenCSMMonitorScope,
       "AdGenCSMMonitorCounterType": AdGenCSMMonitorCounterType,
       "adGenCSMmg": adGenCSMmg,
       "adGenCSMAtmExtension": adGenCSMAtmExtension,
       "adGenCSMTrafficDescrTable": adGenCSMTrafficDescrTable,
       "adGenCSMTrafficDescrEntry": adGenCSMTrafficDescrEntry,
       "adGenCSMTrafficDescrName": adGenCSMTrafficDescrName,
       "adGenCSMVpCrossConnectTable": adGenCSMVpCrossConnectTable,
       "adGenCSMVpCrossConnectEntry": adGenCSMVpCrossConnectEntry,
       "adGenCSMVpCrossConnectName": adGenCSMVpCrossConnectName,
       "adGenCSMVpCrossConnectStatus": adGenCSMVpCrossConnectStatus,
       "adGenCSMVcCrossConnectTable": adGenCSMVcCrossConnectTable,
       "adGenCSMVcCrossConnectEntry": adGenCSMVcCrossConnectEntry,
       "adGenCSMVcCrossConnectName": adGenCSMVcCrossConnectName,
       "adGenCSMVcCrossConnectStatus": adGenCSMVcCrossConnectStatus,
       "adGenCSMVplTable": adGenCSMVplTable,
       "adGenCSMVplEntry": adGenCSMVplEntry,
       "adGenCSMVplDisableAisRdiGeneration": adGenCSMVplDisableAisRdiGeneration,
       "adGenCSMVplDisablePolicing": adGenCSMVplDisablePolicing,
       "adGenCSMVplDisableCAC": adGenCSMVplDisableCAC,
       "adGenCSMVplResetATMStats": adGenCSMVplResetATMStats,
       "adGenCSMVplTxCells": adGenCSMVplTxCells,
       "adGenCSMVplRxCells": adGenCSMVplRxCells,
       "adGenCSMVplRxOamCells": adGenCSMVplRxOamCells,
       "adGenCSMVplDiscardedClp0Cells": adGenCSMVplDiscardedClp0Cells,
       "adGenCSMVplDiscardedClp01Cells": adGenCSMVplDiscardedClp01Cells,
       "adGenCSMVplTaggedClp0Cells": adGenCSMVplTaggedClp0Cells,
       "adGenCSMVplAisStateActive": adGenCSMVplAisStateActive,
       "adGenCSMVplRdiStateActive": adGenCSMVplRdiStateActive,
       "adGenCSMVplLastE2EAisOamId": adGenCSMVplLastE2EAisOamId,
       "adGenCSMVplTxOamLpbkReq": adGenCSMVplTxOamLpbkReq,
       "adGenCSMVplTxOamLpbkRsp": adGenCSMVplTxOamLpbkRsp,
       "adGenCSMVplRxOamLpbkReq": adGenCSMVplRxOamLpbkReq,
       "adGenCSMVplRxOamLpbkRsp": adGenCSMVplRxOamLpbkRsp,
       "adGenCSMVplOamLpbkPassed": adGenCSMVplOamLpbkPassed,
       "adGenCSMVplOamLpbkFailed": adGenCSMVplOamLpbkFailed,
       "adGenCSMVplLoopbackEnable": adGenCSMVplLoopbackEnable,
       "adGenCSMVplInfo": adGenCSMVplInfo,
       "adGenCSMVplLastError": adGenCSMVplLastError,
       "adGenCSMVplAal5EncapsType": adGenCSMVplAal5EncapsType,
       "adGenCSMVclTable": adGenCSMVclTable,
       "adGenCSMVclEntry": adGenCSMVclEntry,
       "adGenCSMVclDisableAisRdiGeneration": adGenCSMVclDisableAisRdiGeneration,
       "adGenCSMVclDisablePolicing": adGenCSMVclDisablePolicing,
       "adGenCSMVclDisableCAC": adGenCSMVclDisableCAC,
       "adGenCSMVclResetATMStats": adGenCSMVclResetATMStats,
       "adGenCSMVclTxCells": adGenCSMVclTxCells,
       "adGenCSMVclRxCells": adGenCSMVclRxCells,
       "adGenCSMVclRxOamCells": adGenCSMVclRxOamCells,
       "adGenCSMVclDiscardedClp0Cells": adGenCSMVclDiscardedClp0Cells,
       "adGenCSMVclDiscardedClp01Cells": adGenCSMVclDiscardedClp01Cells,
       "adGenCSMVclTaggedClp0Cells": adGenCSMVclTaggedClp0Cells,
       "adGenCSMVclAisStateActive": adGenCSMVclAisStateActive,
       "adGenCSMVclRdiStateActive": adGenCSMVclRdiStateActive,
       "adGenCSMVclLastE2EAisOamId": adGenCSMVclLastE2EAisOamId,
       "adGenCSMVclTxOamLpbkReq": adGenCSMVclTxOamLpbkReq,
       "adGenCSMVclTxOamLpbkRsp": adGenCSMVclTxOamLpbkRsp,
       "adGenCSMVclRxOamLpbkReq": adGenCSMVclRxOamLpbkReq,
       "adGenCSMVclRxOamLpbkRsp": adGenCSMVclRxOamLpbkRsp,
       "adGenCSMVclOamLpbkPassed": adGenCSMVclOamLpbkPassed,
       "adGenCSMVclOamLpbkFailed": adGenCSMVclOamLpbkFailed,
       "adGenCSMVclLoopbackEnable": adGenCSMVclLoopbackEnable,
       "adGenCSMVclInfo": adGenCSMVclInfo,
       "adGenCSMVclLastError": adGenCSMVclLastError,
       "adGenCSMVclAal5EncapsType": adGenCSMVclAal5EncapsType,
       "adGenCSMSubInterfaceIndex": adGenCSMSubInterfaceIndex,
       "adGenCSMCcNameLookupTable": adGenCSMCcNameLookupTable,
       "adGenCSMCcNameLookupEntry": adGenCSMCcNameLookupEntry,
       "adGenCSMCcName": adGenCSMCcName,
       "adGenCSMCcFindIndex": adGenCSMCcFindIndex,
       "adGenCSMTdNameLookupTable": adGenCSMTdNameLookupTable,
       "adGenCSMTdNameLookupEntry": adGenCSMTdNameLookupEntry,
       "adGenCSMTdName": adGenCSMTdName,
       "adGenCSMTdFindIndex": adGenCSMTdFindIndex,
       "adGenCsmPvpLastChange": adGenCsmPvpLastChange,
       "adGenCsmSvpLastChange": adGenCsmSvpLastChange,
       "adGenCsmPvcLastChange": adGenCsmPvcLastChange,
       "adGenCsmSvcLastChange": adGenCsmSvcLastChange,
       "adGenCSMVclOamTable": adGenCSMVclOamTable,
       "adGenCSMVclOamEntry": adGenCSMVclOamEntry,
       "adGenCSMVclOamId": adGenCSMVclOamId,
       "adGenCSMVclSendSegLoopback": adGenCSMVclSendSegLoopback,
       "adGenCSMVclSendE2ELoopback": adGenCSMVclSendE2ELoopback,
       "adGenCSMVclOamRowStatus": adGenCSMVclOamRowStatus,
       "adGenCSMVplOamTable": adGenCSMVplOamTable,
       "adGenCSMVplOamEntry": adGenCSMVplOamEntry,
       "adGenCSMVplOamId": adGenCSMVplOamId,
       "adGenCSMVplSendSegLoopback": adGenCSMVplSendSegLoopback,
       "adGenCSMVplSendE2ELoopback": adGenCSMVplSendE2ELoopback,
       "adGenCSMVplOamRowStatus": adGenCSMVplOamRowStatus,
       "adGenCSMVclEnhOamTable": adGenCSMVclEnhOamTable,
       "adGenCSMVclEnhOamEntry": adGenCSMVclEnhOamEntry,
       "adGenCSMVclEnhOamId": adGenCSMVclEnhOamId,
       "adGenCSMVclEnhOamLpbkReqCount": adGenCSMVclEnhOamLpbkReqCount,
       "adGenCSMVclEnhOamLpbkTxDelay": adGenCSMVclEnhOamLpbkTxDelay,
       "adGenCSMVclEnhOamLpbkTimeout": adGenCSMVclEnhOamLpbkTimeout,
       "adGenCSMVclEnhOamLpbkReqTx": adGenCSMVclEnhOamLpbkReqTx,
       "adGenCSMVclEnhOamLpbkRespRx": adGenCSMVclEnhOamLpbkRespRx,
       "adGenCSMVclEnhOamLpbkRespTimeout": adGenCSMVclEnhOamLpbkRespTimeout,
       "adGenCSMVclEnhOamLpbkReqType": adGenCSMVclEnhOamLpbkReqType,
       "adGenCSMVclEnhOamRowStatus": adGenCSMVclEnhOamRowStatus,
       "adGenCSMVplEnhOamTable": adGenCSMVplEnhOamTable,
       "adGenCSMVplEnhOamEntry": adGenCSMVplEnhOamEntry,
       "adGenCSMVplEnhOamId": adGenCSMVplEnhOamId,
       "adGenCSMVplEnhOamLpbkReqCount": adGenCSMVplEnhOamLpbkReqCount,
       "adGenCSMVplEnhOamLpbkTxDelay": adGenCSMVplEnhOamLpbkTxDelay,
       "adGenCSMVplEnhOamLpbkTimeout": adGenCSMVplEnhOamLpbkTimeout,
       "adGenCSMVplEnhOamLpbkReqTx": adGenCSMVplEnhOamLpbkReqTx,
       "adGenCSMVplEnhOamLpbkRespRx": adGenCSMVplEnhOamLpbkRespRx,
       "adGenCSMVplEnhOamLpbkRespTimeout": adGenCSMVplEnhOamLpbkRespTimeout,
       "adGenCSMVplEnhOamLpbkReqType": adGenCSMVplEnhOamLpbkReqType,
       "adGenCSMVplEnhOamRowStatus": adGenCSMVplEnhOamRowStatus,
       "adGenCSMUseFixedIndexes": adGenCSMUseFixedIndexes,
       "adGenCSMOptionsExtension": adGenCSMOptionsExtension,
       "adGenCSMOptionMenuLevel": adGenCSMOptionMenuLevel,
       "adGenCSMOptionMenuDisplayDirection": adGenCSMOptionMenuDisplayDirection,
       "adGenCSMOptionMenuDisplayPort": adGenCSMOptionMenuDisplayPort,
       "adGenCSMOptionMenuDisplayClass": adGenCSMOptionMenuDisplayClass,
       "adGenCSMShelfPolicingDisable": adGenCSMShelfPolicingDisable,
       "adGenCSMShelfCellRateCACDisable": adGenCSMShelfCellRateCACDisable,
       "adGenCSMShelfBufferCACDisable": adGenCSMShelfBufferCACDisable,
       "adGenCSMShelfCbrOverbooking": adGenCSMShelfCbrOverbooking,
       "adGenCSMShelfRtVbrOverbooking": adGenCSMShelfRtVbrOverbooking,
       "adGenCSMShelfNrtVbrOverbooking": adGenCSMShelfNrtVbrOverbooking,
       "adGenCSMShelfNrtVbrSharing": adGenCSMShelfNrtVbrSharing,
       "adGenCSMShelfUbrSharing": adGenCSMShelfUbrSharing,
       "adGenCSMShelfUbrMaxClp1Thrsh": adGenCSMShelfUbrMaxClp1Thrsh,
       "adGenCSMShelfUbrMaxClp0Thrsh": adGenCSMShelfUbrMaxClp0Thrsh,
       "adGenCSMShelfUbrMaxMaxThrsh": adGenCSMShelfUbrMaxMaxThrsh,
       "adGenCSMShelfUbrMaxFrameMultiplier": adGenCSMShelfUbrMaxFrameMultiplier,
       "adGenCSMDirectionOptionTable": adGenCSMDirectionOptionTable,
       "adGenCSMDirectionOptionEntry": adGenCSMDirectionOptionEntry,
       "adGenCSMDirection": adGenCSMDirection,
       "adGenCSMDirectionPolicingDisable": adGenCSMDirectionPolicingDisable,
       "adGenCSMDirectionCellRateCACDisable": adGenCSMDirectionCellRateCACDisable,
       "adGenCSMDirectionBufferCACDisable": adGenCSMDirectionBufferCACDisable,
       "adGenCSMDirectionCbrOverbooking": adGenCSMDirectionCbrOverbooking,
       "adGenCSMDirectionRtVbrOverbooking": adGenCSMDirectionRtVbrOverbooking,
       "adGenCSMDirectionNrtVbrOverbooking": adGenCSMDirectionNrtVbrOverbooking,
       "adGenCSMDirectionMaximumThreshold": adGenCSMDirectionMaximumThreshold,
       "adGenCSMDirectionNrtVbrSharing": adGenCSMDirectionNrtVbrSharing,
       "adGenCSMDirectionUbrSharing": adGenCSMDirectionUbrSharing,
       "adGenCSMDirectionUbrMaxClp1Thrsh": adGenCSMDirectionUbrMaxClp1Thrsh,
       "adGenCSMDirectionUbrMaxClp0Thrsh": adGenCSMDirectionUbrMaxClp0Thrsh,
       "adGenCSMDirectionUbrMaxMaxThrsh": adGenCSMDirectionUbrMaxMaxThrsh,
       "adGenCSMDirectionUbrMaxFrameMultiplier": adGenCSMDirectionUbrMaxFrameMultiplier,
       "adGenCSMDirectionPolicingDisableOverride": adGenCSMDirectionPolicingDisableOverride,
       "adGenCSMDirectionCellRateCACDisableOverride": adGenCSMDirectionCellRateCACDisableOverride,
       "adGenCSMDirectionBufferCACDisableOverride": adGenCSMDirectionBufferCACDisableOverride,
       "adGenCSMDirectionCbrOverbookingOverride": adGenCSMDirectionCbrOverbookingOverride,
       "adGenCSMDirectionRtVbrOverbookingOverride": adGenCSMDirectionRtVbrOverbookingOverride,
       "adGenCSMDirectionNrtVbrOverbookingOverride": adGenCSMDirectionNrtVbrOverbookingOverride,
       "adGenCSMDirectionNrtVbrSharingOverride": adGenCSMDirectionNrtVbrSharingOverride,
       "adGenCSMDirectionUbrSharingOverride": adGenCSMDirectionUbrSharingOverride,
       "adGenCSMDirectionUbrMaxClp1ThrshOverride": adGenCSMDirectionUbrMaxClp1ThrshOverride,
       "adGenCSMDirectionUbrMaxClp0ThrshOverride": adGenCSMDirectionUbrMaxClp0ThrshOverride,
       "adGenCSMDirectionUbrMaxMaxThrshOverride": adGenCSMDirectionUbrMaxMaxThrshOverride,
       "adGenCSMDirectionUbrMaxFrameMultiplierOverride": adGenCSMDirectionUbrMaxFrameMultiplierOverride,
       "adGenCSMDirectionDefaultCDVT": adGenCSMDirectionDefaultCDVT,
       "adGenCSMDirectionAisRdiDisable": adGenCSMDirectionAisRdiDisable,
       "adGenCSMDirectionInputCdv": adGenCSMDirectionInputCdv,
       "adGenCSMDirectionOutputCdv": adGenCSMDirectionOutputCdv,
       "adGenCSMDirectionInputMaxCtd": adGenCSMDirectionInputMaxCtd,
       "adGenCSMDirectionOutputMaxCtd": adGenCSMDirectionOutputMaxCtd,
       "adGenCSMDirectionCbrClassScheduling": adGenCSMDirectionCbrClassScheduling,
       "adGenCSMDirectionRtVbrClassScheduling": adGenCSMDirectionRtVbrClassScheduling,
       "adGenCSMDirectionNrtVbrClassScheduling": adGenCSMDirectionNrtVbrClassScheduling,
       "adGenCSMDirectionUbrClassScheduling": adGenCSMDirectionUbrClassScheduling,
       "adGenCSMDirectionDefaultCDVTOverride": adGenCSMDirectionDefaultCDVTOverride,
       "adGenCSMDirectionAisRdiDisableOverride": adGenCSMDirectionAisRdiDisableOverride,
       "adGenCSMDirectionInputCdvOverride": adGenCSMDirectionInputCdvOverride,
       "adGenCSMDirectionOutputCdvOverride": adGenCSMDirectionOutputCdvOverride,
       "adGenCSMDirectionInputMaxCtdOverride": adGenCSMDirectionInputMaxCtdOverride,
       "adGenCSMDirectionOutputMaxCtdOverride": adGenCSMDirectionOutputMaxCtdOverride,
       "adGenCSMDirectionCbrClassSchedulingOverride": adGenCSMDirectionCbrClassSchedulingOverride,
       "adGenCSMDirectionRtVbrClassSchedulingOverride": adGenCSMDirectionRtVbrClassSchedulingOverride,
       "adGenCSMDirectionNrtVbrClassSchedulingOverride": adGenCSMDirectionNrtVbrClassSchedulingOverride,
       "adGenCSMDirectionUbrClassSchedulingOverride": adGenCSMDirectionUbrClassSchedulingOverride,
       "adGenCSMPortOptionTable": adGenCSMPortOptionTable,
       "adGenCSMPortOptionEntry": adGenCSMPortOptionEntry,
       "adGenCSMPortPolicingDisable": adGenCSMPortPolicingDisable,
       "adGenCSMPortCellRateCACDisable": adGenCSMPortCellRateCACDisable,
       "adGenCSMPortBufferCACDisable": adGenCSMPortBufferCACDisable,
       "adGenCSMPortCbrOverbooking": adGenCSMPortCbrOverbooking,
       "adGenCSMPortRtVbrOverbooking": adGenCSMPortRtVbrOverbooking,
       "adGenCSMPortNrtVbrOverbooking": adGenCSMPortNrtVbrOverbooking,
       "adGenCSMPortMaximumThreshold": adGenCSMPortMaximumThreshold,
       "adGenCSMPortUbrMaxClp1Thrsh": adGenCSMPortUbrMaxClp1Thrsh,
       "adGenCSMPortUbrMaxClp0Thrsh": adGenCSMPortUbrMaxClp0Thrsh,
       "adGenCSMPortUbrMaxMaxThrsh": adGenCSMPortUbrMaxMaxThrsh,
       "adGenCSMPortUbrMaxFrameMultiplier": adGenCSMPortUbrMaxFrameMultiplier,
       "adGenCSMPortPolicingDisableOverride": adGenCSMPortPolicingDisableOverride,
       "adGenCSMPortCellRateCACDisableOverride": adGenCSMPortCellRateCACDisableOverride,
       "adGenCSMPortBufferCACDisableOverride": adGenCSMPortBufferCACDisableOverride,
       "adGenCSMPortCbrOverbookingOverride": adGenCSMPortCbrOverbookingOverride,
       "adGenCSMPortRtVbrOverbookingOverride": adGenCSMPortRtVbrOverbookingOverride,
       "adGenCSMPortNrtVbrOverbookingOverride": adGenCSMPortNrtVbrOverbookingOverride,
       "adGenCSMPortMaximumThresholdOverride": adGenCSMPortMaximumThresholdOverride,
       "adGenCSMPortUbrMaxClp1ThrshOverride": adGenCSMPortUbrMaxClp1ThrshOverride,
       "adGenCSMPortUbrMaxClp0ThrshOverride": adGenCSMPortUbrMaxClp0ThrshOverride,
       "adGenCSMPortUbrMaxMaxThrshOverride": adGenCSMPortUbrMaxMaxThrshOverride,
       "adGenCSMPortUbrMaxFrameMultiplierOverride": adGenCSMPortUbrMaxFrameMultiplierOverride,
       "adGenCSMPortDefaultCDVT": adGenCSMPortDefaultCDVT,
       "adGenCSMPortAisRdiDisable": adGenCSMPortAisRdiDisable,
       "adGenCSMPortInputCdv": adGenCSMPortInputCdv,
       "adGenCSMPortOutputCdv": adGenCSMPortOutputCdv,
       "adGenCSMPortInputMaxCtd": adGenCSMPortInputMaxCtd,
       "adGenCSMPortOutputMaxCtd": adGenCSMPortOutputMaxCtd,
       "adGenCSMPortCbrClassScheduling": adGenCSMPortCbrClassScheduling,
       "adGenCSMPortRtVbrClassScheduling": adGenCSMPortRtVbrClassScheduling,
       "adGenCSMPortNrtVbrClassScheduling": adGenCSMPortNrtVbrClassScheduling,
       "adGenCSMPortUbrClassScheduling": adGenCSMPortUbrClassScheduling,
       "adGenCSMPortDefaultCDVTOverride": adGenCSMPortDefaultCDVTOverride,
       "adGenCSMPortAisRdiDisableOverride": adGenCSMPortAisRdiDisableOverride,
       "adGenCSMPortInputCdvOverride": adGenCSMPortInputCdvOverride,
       "adGenCSMPortOutputCdvOverride": adGenCSMPortOutputCdvOverride,
       "adGenCSMPortInputMaxCtdOverride": adGenCSMPortInputMaxCtdOverride,
       "adGenCSMPortOutputMaxCtdOverride": adGenCSMPortOutputMaxCtdOverride,
       "adGenCSMPortCbrClassSchedulingOverride": adGenCSMPortCbrClassSchedulingOverride,
       "adGenCSMPortRtVbrClassSchedulingOverride": adGenCSMPortRtVbrClassSchedulingOverride,
       "adGenCSMPortNrtVbrClassSchedulingOverride": adGenCSMPortNrtVbrClassSchedulingOverride,
       "adGenCSMPortUbrClassSchedulingOverride": adGenCSMPortUbrClassSchedulingOverride,
       "adGenCSMClassOptionTable": adGenCSMClassOptionTable,
       "adGenCSMClassOptionEntry": adGenCSMClassOptionEntry,
       "adGenAtmServiceCategory": adGenAtmServiceCategory,
       "adGenCSMClassPolicingDisable": adGenCSMClassPolicingDisable,
       "adGenCSMClassCellRateCACDisable": adGenCSMClassCellRateCACDisable,
       "adGenCSMClassBufferCACDisable": adGenCSMClassBufferCACDisable,
       "adGenCSMClassMaximumThreshold": adGenCSMClassMaximumThreshold,
       "adGenCSMClassPolicingDisableOverride": adGenCSMClassPolicingDisableOverride,
       "adGenCSMClassCellRateCACDisableOverride": adGenCSMClassCellRateCACDisableOverride,
       "adGenCSMClassBufferCACDisableOverride": adGenCSMClassBufferCACDisableOverride,
       "adGenCSMClassMaximumThresholdOverride": adGenCSMClassMaximumThresholdOverride,
       "adGenCSMShelfDefaultCDVT": adGenCSMShelfDefaultCDVT,
       "adGenCSMShelfAisRdiDisable": adGenCSMShelfAisRdiDisable,
       "adGenCSMShelfInputCdv": adGenCSMShelfInputCdv,
       "adGenCSMShelfOutputCdv": adGenCSMShelfOutputCdv,
       "adGenCSMShelfInputMaxCtd": adGenCSMShelfInputMaxCtd,
       "adGenCSMShelfOutputMaxCtd": adGenCSMShelfOutputMaxCtd,
       "adGenCSMShelfCbrClassScheduling": adGenCSMShelfCbrClassScheduling,
       "adGenCSMShelfRtVbrClassScheduling": adGenCSMShelfRtVbrClassScheduling,
       "adGenCSMShelfNrtVbrClassScheduling": adGenCSMShelfNrtVbrClassScheduling,
       "adGenCSMShelfUbrClassScheduling": adGenCSMShelfUbrClassScheduling,
       "adGenCSMShelfCbrShaping": adGenCSMShelfCbrShaping,
       "adGenCSMShelfRtVbrShaping": adGenCSMShelfRtVbrShaping,
       "adGenCSMShelfNrtVbrShaping": adGenCSMShelfNrtVbrShaping,
       "adGenCSMShelfUbrShaping": adGenCSMShelfUbrShaping,
       "adGenCSMMonitor": adGenCSMMonitor,
       "adGenCSMMonitorSessionIndexNext": adGenCSMMonitorSessionIndexNext,
       "adGenCSMMonitorSessionTable": adGenCSMMonitorSessionTable,
       "adGenCSMMonitorSessionEntry": adGenCSMMonitorSessionEntry,
       "adGenCSMMonitorSessionId": adGenCSMMonitorSessionId,
       "adGenCSMMonitorSessionName": adGenCSMMonitorSessionName,
       "adGenCSMMonitorSessionDescription": adGenCSMMonitorSessionDescription,
       "adGenCSMMonitorSessionRowStatus": adGenCSMMonitorSessionRowStatus,
       "adGenCSMMonitorSessionStartTimeStamp": adGenCSMMonitorSessionStartTimeStamp,
       "adGenCSMMonitorSessionScope": adGenCSMMonitorSessionScope,
       "adGenCSMMonitorSessionMaxIntervals": adGenCSMMonitorSessionMaxIntervals,
       "adGenCSMMonitorSessionIntervalDuration": adGenCSMMonitorSessionIntervalDuration,
       "adGenCSMMonitorSessionCacheInterval": adGenCSMMonitorSessionCacheInterval,
       "adGenCSMMonitorSessionElapsedIntervals": adGenCSMMonitorSessionElapsedIntervals,
       "adGenCSMMonitorSessionClasses": adGenCSMMonitorSessionClasses,
       "adGenCSMMonitorSessionParam1": adGenCSMMonitorSessionParam1,
       "adGenCSMMonitorSessionParam2": adGenCSMMonitorSessionParam2,
       "adGenCSMMonitorSessionParam3": adGenCSMMonitorSessionParam3,
       "adGenCSMMonitorCounterTable": adGenCSMMonitorCounterTable,
       "adGenCSMMonitorCounterEntry": adGenCSMMonitorCounterEntry,
       "adGenCSMMonitorCounterType": adGenCSMMonitorCounterType,
       "adGenCSMMonitorCounterTimeStamp": adGenCSMMonitorCounterTimeStamp,
       "adGenCSMMonitorCounterInterval": adGenCSMMonitorCounterInterval,
       "adGenCSMMonitorCounterTxCells": adGenCSMMonitorCounterTxCells,
       "adGenCSMMonitorCounterTxErrors": adGenCSMMonitorCounterTxErrors,
       "adGenCSMMonitorCounterRxCells": adGenCSMMonitorCounterRxCells,
       "adGenCSMMonitorCounterRxOAM": adGenCSMMonitorCounterRxOAM,
       "adGenCSMMonitorCounterRxDiscardPolicingClp0": adGenCSMMonitorCounterRxDiscardPolicingClp0,
       "adGenCSMMonitorCounterRxDiscardPolicingClp01": adGenCSMMonitorCounterRxDiscardPolicingClp01,
       "adGenCSMMonitorCounterRxTaggedClp0": adGenCSMMonitorCounterRxTaggedClp0,
       "adGenCSMMonitorCounterRxErrors": adGenCSMMonitorCounterRxErrors,
       "adGenCSMMonitorCounterHistoryTable": adGenCSMMonitorCounterHistoryTable,
       "adGenCSMMonitorCounterHistoryEntry": adGenCSMMonitorCounterHistoryEntry,
       "adGenCSMMonitorCounterHistoryTxCells": adGenCSMMonitorCounterHistoryTxCells,
       "adGenCSMMonitorCounterHistoryTxErrors": adGenCSMMonitorCounterHistoryTxErrors,
       "adGenCSMMonitorCounterHistoryRxCells": adGenCSMMonitorCounterHistoryRxCells,
       "adGenCSMMonitorCounterHistoryRxOAM": adGenCSMMonitorCounterHistoryRxOAM,
       "adGenCSMMonitorCounterHistoryRxDiscardPolicingClp0": adGenCSMMonitorCounterHistoryRxDiscardPolicingClp0,
       "adGenCSMMonitorCounterHistoryRxDiscardPolicingClp01": adGenCSMMonitorCounterHistoryRxDiscardPolicingClp01,
       "adGenCSMMonitorCounterHistoryRxTaggedClp0": adGenCSMMonitorCounterHistoryRxTaggedClp0,
       "adGenCSMMonitorCounterHistoryRxErrors": adGenCSMMonitorCounterHistoryRxErrors,
       "adGenCSMMonitorCounterHistoryTimeStamp": adGenCSMMonitorCounterHistoryTimeStamp,
       "adGENCSM2ID": adGENCSM2ID}
)
