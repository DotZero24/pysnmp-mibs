# SNMP MIB module (ADTRAN-GENERIC-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-BRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:00 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenBridge,
 adGenBridgeID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenBridge",
    "adGenBridgeID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 16, 1)
)
if mibBuilder.loadTexts:
    adGenBridgeMIB.setRevisions(
        ("2011-12-23 00:00",
         "2011-12-01 00:00",
         "2011-08-10 00:00",
         "2011-04-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenBridgeProtMode(TextualConvention, Integer32):
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
        *(("unsupported", 1),
          ("unprotected", 2),
          ("protected", 3))
    )



class AdGenBridgeProtAvail(TextualConvention, Integer32):
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
        *(("unsupported", 1),
          ("unavailable", 2),
          ("available", 3))
    )



class AdGenBridgeProtState(TextualConvention, Integer32):
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
        *(("unsupported", 1),
          ("unprotected", 2),
          ("protected", 3))
    )



class AdGenBridgeOperStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("noLinksInGroup", 4),
          ("upPartial", 5))
    )



class AdGenBridgePhylOperStatus(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4))
    )



class AdGenBridgeType(TextualConvention, Integer32):
    status = "current"
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
        *(("notProvisioned", 1),
          ("efm", 2),
          ("tr101", 3),
          ("ima", 4),
          ("linkAggregation", 5),
          ("macSwitched", 6),
          ("ppp", 7),
          ("atm", 8))
    )



class AdGenBridgeRateControl(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rateControlOn", 1),
          ("rateControlOff", 2))
    )



class AdGenBridgeLastChange(TextualConvention, TimeTicks):
    status = "current"


class AdGenBridgeAlarmSuppress(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("suppress", 1),
          ("noSuppress", 2))
    )



class AdGenBridgePhylInstalled(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uninstalled", 1),
          ("installed", 2))
    )



class AdGenBridgeProtectionRevertiveSwitch(TextualConvention, Integer32):
    status = "current"
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



class AdGenBridgeProtectionLockout(TextualConvention, Integer32):
    status = "current"
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



class AdGenBridgeManualSwitch(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchToProtect", 1),
          ("switchToNonProtect", 2))
    )



class AdGenProtectionVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("version1", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenBridgeMIBObjects_ObjectIdentity = ObjectIdentity
adGenBridgeMIBObjects = _AdGenBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1)
)
_AdGenBridgeModuleConfTable_Object = MibTable
adGenBridgeModuleConfTable = _AdGenBridgeModuleConfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    adGenBridgeModuleConfTable.setStatus("current")
_AdGenBridgeModuleConfEntry_Object = MibTableRow
adGenBridgeModuleConfEntry = _AdGenBridgeModuleConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 1, 1)
)
adGenBridgeModuleConfEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenBridgeModuleConfEntry.setStatus("current")


class _AdGenBridgeModuleMaxBridges_Type(Integer32):
    """Custom type adGenBridgeModuleMaxBridges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenBridgeModuleMaxBridges_Type.__name__ = "Integer32"
_AdGenBridgeModuleMaxBridges_Object = MibTableColumn
adGenBridgeModuleMaxBridges = _AdGenBridgeModuleMaxBridges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 1, 1, 1),
    _AdGenBridgeModuleMaxBridges_Type()
)
adGenBridgeModuleMaxBridges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeModuleMaxBridges.setStatus("current")


class _AdGenBridgeModuleMaxPhyls_Type(Integer32):
    """Custom type adGenBridgeModuleMaxPhyls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2200),
    )


_AdGenBridgeModuleMaxPhyls_Type.__name__ = "Integer32"
_AdGenBridgeModuleMaxPhyls_Object = MibTableColumn
adGenBridgeModuleMaxPhyls = _AdGenBridgeModuleMaxPhyls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 1, 1, 2),
    _AdGenBridgeModuleMaxPhyls_Type()
)
adGenBridgeModuleMaxPhyls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeModuleMaxPhyls.setStatus("current")


class _AdGenBridgeModuleConfBridges_Type(Integer32):
    """Custom type adGenBridgeModuleConfBridges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenBridgeModuleConfBridges_Type.__name__ = "Integer32"
_AdGenBridgeModuleConfBridges_Object = MibTableColumn
adGenBridgeModuleConfBridges = _AdGenBridgeModuleConfBridges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 1, 1, 3),
    _AdGenBridgeModuleConfBridges_Type()
)
adGenBridgeModuleConfBridges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeModuleConfBridges.setStatus("current")


class _AdGenBridgeModuleConfPhyls_Type(Integer32):
    """Custom type adGenBridgeModuleConfPhyls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2200),
    )


_AdGenBridgeModuleConfPhyls_Type.__name__ = "Integer32"
_AdGenBridgeModuleConfPhyls_Object = MibTableColumn
adGenBridgeModuleConfPhyls = _AdGenBridgeModuleConfPhyls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 1, 1, 4),
    _AdGenBridgeModuleConfPhyls_Type()
)
adGenBridgeModuleConfPhyls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeModuleConfPhyls.setStatus("current")
_AdGenBridgeModuleMaxBandwidth_Type = Integer32
_AdGenBridgeModuleMaxBandwidth_Object = MibTableColumn
adGenBridgeModuleMaxBandwidth = _AdGenBridgeModuleMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 1, 1, 5),
    _AdGenBridgeModuleMaxBandwidth_Type()
)
adGenBridgeModuleMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenBridgeModuleMaxBandwidth.setStatus("current")
_AdGenBridgeModuleConfBandwidth_Type = Integer32
_AdGenBridgeModuleConfBandwidth_Object = MibTableColumn
adGenBridgeModuleConfBandwidth = _AdGenBridgeModuleConfBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 1, 1, 6),
    _AdGenBridgeModuleConfBandwidth_Type()
)
adGenBridgeModuleConfBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeModuleConfBandwidth.setStatus("current")
_AdGenBridgeStatus_Type = DisplayString
_AdGenBridgeStatus_Object = MibScalar
adGenBridgeStatus = _AdGenBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 2),
    _AdGenBridgeStatus_Type()
)
adGenBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeStatus.setStatus("current")
_AdGenBridgeTable_Object = MibTable
adGenBridgeTable = _AdGenBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3)
)
if mibBuilder.loadTexts:
    adGenBridgeTable.setStatus("current")
_AdGenBridgeEntry_Object = MibTableRow
adGenBridgeEntry = _AdGenBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1)
)
adGenBridgeEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-BRIDGE-MIB", "adGenBridgeIfIndex"),
)
if mibBuilder.loadTexts:
    adGenBridgeEntry.setStatus("current")
_AdGenBridgeIfIndex_Type = InterfaceIndex
_AdGenBridgeIfIndex_Object = MibTableColumn
adGenBridgeIfIndex = _AdGenBridgeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 1),
    _AdGenBridgeIfIndex_Type()
)
adGenBridgeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenBridgeIfIndex.setStatus("current")
_AdGenBridgeType_Type = AdGenBridgeType
_AdGenBridgeType_Object = MibTableColumn
adGenBridgeType = _AdGenBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 2),
    _AdGenBridgeType_Type()
)
adGenBridgeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeType.setStatus("current")
_AdGenBridgeName_Type = DisplayString
_AdGenBridgeName_Object = MibTableColumn
adGenBridgeName = _AdGenBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 3),
    _AdGenBridgeName_Type()
)
adGenBridgeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeName.setStatus("current")
_AdGenBridgeProtMode_Type = AdGenBridgeProtMode
_AdGenBridgeProtMode_Object = MibTableColumn
adGenBridgeProtMode = _AdGenBridgeProtMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 4),
    _AdGenBridgeProtMode_Type()
)
adGenBridgeProtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtMode.setStatus("current")
_AdGenBridgeProtAvail_Type = AdGenBridgeProtAvail
_AdGenBridgeProtAvail_Object = MibTableColumn
adGenBridgeProtAvail = _AdGenBridgeProtAvail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 5),
    _AdGenBridgeProtAvail_Type()
)
adGenBridgeProtAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtAvail.setStatus("current")
_AdGenBridgeProtState_Type = AdGenBridgeProtState
_AdGenBridgeProtState_Object = MibTableColumn
adGenBridgeProtState = _AdGenBridgeProtState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 6),
    _AdGenBridgeProtState_Type()
)
adGenBridgeProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtState.setStatus("current")
_AdGenBridgeProtSlot_Type = Unsigned32
_AdGenBridgeProtSlot_Object = MibTableColumn
adGenBridgeProtSlot = _AdGenBridgeProtSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 7),
    _AdGenBridgeProtSlot_Type()
)
adGenBridgeProtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtSlot.setStatus("current")


class _AdGenBridgeMinNumActivePhyls_Type(Integer32):
    """Custom type adGenBridgeMinNumActivePhyls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AdGenBridgeMinNumActivePhyls_Type.__name__ = "Integer32"
_AdGenBridgeMinNumActivePhyls_Object = MibTableColumn
adGenBridgeMinNumActivePhyls = _AdGenBridgeMinNumActivePhyls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 8),
    _AdGenBridgeMinNumActivePhyls_Type()
)
adGenBridgeMinNumActivePhyls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeMinNumActivePhyls.setStatus("current")
_AdGenBridgeOperStatus_Type = AdGenBridgeOperStatus
_AdGenBridgeOperStatus_Object = MibTableColumn
adGenBridgeOperStatus = _AdGenBridgeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 9),
    _AdGenBridgeOperStatus_Type()
)
adGenBridgeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeOperStatus.setStatus("current")
_AdGenBridgeLastChange_Type = AdGenBridgeLastChange
_AdGenBridgeLastChange_Object = MibTableColumn
adGenBridgeLastChange = _AdGenBridgeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 10),
    _AdGenBridgeLastChange_Type()
)
adGenBridgeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeLastChange.setStatus("current")


class _AdGenBridgeNumCfgEVPLs_Type(Integer32):
    """Custom type adGenBridgeNumCfgEVPLs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenBridgeNumCfgEVPLs_Type.__name__ = "Integer32"
_AdGenBridgeNumCfgEVPLs_Object = MibTableColumn
adGenBridgeNumCfgEVPLs = _AdGenBridgeNumCfgEVPLs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 11),
    _AdGenBridgeNumCfgEVPLs_Type()
)
adGenBridgeNumCfgEVPLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeNumCfgEVPLs.setStatus("current")


class _AdGenBridgeNumCfgEVCLs_Type(Integer32):
    """Custom type adGenBridgeNumCfgEVCLs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenBridgeNumCfgEVCLs_Type.__name__ = "Integer32"
_AdGenBridgeNumCfgEVCLs_Object = MibTableColumn
adGenBridgeNumCfgEVCLs = _AdGenBridgeNumCfgEVCLs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 12),
    _AdGenBridgeNumCfgEVCLs_Type()
)
adGenBridgeNumCfgEVCLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeNumCfgEVCLs.setStatus("current")


class _AdGenBridgeNumCfgPhyls_Type(Integer32):
    """Custom type adGenBridgeNumCfgPhyls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2200),
    )


_AdGenBridgeNumCfgPhyls_Type.__name__ = "Integer32"
_AdGenBridgeNumCfgPhyls_Object = MibTableColumn
adGenBridgeNumCfgPhyls = _AdGenBridgeNumCfgPhyls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 13),
    _AdGenBridgeNumCfgPhyls_Type()
)
adGenBridgeNumCfgPhyls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeNumCfgPhyls.setStatus("current")


class _AdGenBridgeNumActPhyls_Type(Integer32):
    """Custom type adGenBridgeNumActPhyls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2200),
    )


_AdGenBridgeNumActPhyls_Type.__name__ = "Integer32"
_AdGenBridgeNumActPhyls_Object = MibTableColumn
adGenBridgeNumActPhyls = _AdGenBridgeNumActPhyls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 14),
    _AdGenBridgeNumActPhyls_Type()
)
adGenBridgeNumActPhyls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeNumActPhyls.setStatus("current")
_AdGenBridgeLastError_Type = DisplayString
_AdGenBridgeLastError_Object = MibTableColumn
adGenBridgeLastError = _AdGenBridgeLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 15),
    _AdGenBridgeLastError_Type()
)
adGenBridgeLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeLastError.setStatus("current")


class _AdGenBridgeRowStatus_Type(RowStatus):
    """Custom type adGenBridgeRowStatus based on RowStatus"""
    defaultValue = 1


_AdGenBridgeRowStatus_Type.__name__ = "RowStatus"
_AdGenBridgeRowStatus_Object = MibTableColumn
adGenBridgeRowStatus = _AdGenBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 16),
    _AdGenBridgeRowStatus_Type()
)
adGenBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeRowStatus.setStatus("current")
_AdGenBridgeMaxBandwidth_Type = Integer32
_AdGenBridgeMaxBandwidth_Object = MibTableColumn
adGenBridgeMaxBandwidth = _AdGenBridgeMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 17),
    _AdGenBridgeMaxBandwidth_Type()
)
adGenBridgeMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeMaxBandwidth.setStatus("current")
_AdGenBridgeCurrentBandwidth_Type = Integer32
_AdGenBridgeCurrentBandwidth_Object = MibTableColumn
adGenBridgeCurrentBandwidth = _AdGenBridgeCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 18),
    _AdGenBridgeCurrentBandwidth_Type()
)
adGenBridgeCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeCurrentBandwidth.setStatus("current")
_AdGenBridgeUpstreamRate_Type = Unsigned32
_AdGenBridgeUpstreamRate_Object = MibTableColumn
adGenBridgeUpstreamRate = _AdGenBridgeUpstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 19),
    _AdGenBridgeUpstreamRate_Type()
)
adGenBridgeUpstreamRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeUpstreamRate.setStatus("current")
_AdGenBridgeDownstreamRate_Type = Unsigned32
_AdGenBridgeDownstreamRate_Object = MibTableColumn
adGenBridgeDownstreamRate = _AdGenBridgeDownstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 20),
    _AdGenBridgeDownstreamRate_Type()
)
adGenBridgeDownstreamRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeDownstreamRate.setStatus("current")
_AdGenBridgeCurrentUpstreamRate_Type = Unsigned32
_AdGenBridgeCurrentUpstreamRate_Object = MibTableColumn
adGenBridgeCurrentUpstreamRate = _AdGenBridgeCurrentUpstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 21),
    _AdGenBridgeCurrentUpstreamRate_Type()
)
adGenBridgeCurrentUpstreamRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeCurrentUpstreamRate.setStatus("current")
_AdGenBridgeCurrentDownstreamRate_Type = Unsigned32
_AdGenBridgeCurrentDownstreamRate_Object = MibTableColumn
adGenBridgeCurrentDownstreamRate = _AdGenBridgeCurrentDownstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 22),
    _AdGenBridgeCurrentDownstreamRate_Type()
)
adGenBridgeCurrentDownstreamRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeCurrentDownstreamRate.setStatus("current")
_AdGenBridgeRateControl_Type = AdGenBridgeRateControl
_AdGenBridgeRateControl_Object = MibTableColumn
adGenBridgeRateControl = _AdGenBridgeRateControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 23),
    _AdGenBridgeRateControl_Type()
)
adGenBridgeRateControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeRateControl.setStatus("current")
_AdGenBridgeAlarmSuppress_Type = AdGenBridgeAlarmSuppress
_AdGenBridgeAlarmSuppress_Object = MibTableColumn
adGenBridgeAlarmSuppress = _AdGenBridgeAlarmSuppress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 24),
    _AdGenBridgeAlarmSuppress_Type()
)
adGenBridgeAlarmSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeAlarmSuppress.setStatus("current")
_AdGenBridgeSecondaryUpstreamRate_Type = Unsigned32
_AdGenBridgeSecondaryUpstreamRate_Object = MibTableColumn
adGenBridgeSecondaryUpstreamRate = _AdGenBridgeSecondaryUpstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 25),
    _AdGenBridgeSecondaryUpstreamRate_Type()
)
adGenBridgeSecondaryUpstreamRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeSecondaryUpstreamRate.setStatus("current")
_AdGenBridgeSecondaryDownstreamRate_Type = Unsigned32
_AdGenBridgeSecondaryDownstreamRate_Object = MibTableColumn
adGenBridgeSecondaryDownstreamRate = _AdGenBridgeSecondaryDownstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 3, 1, 26),
    _AdGenBridgeSecondaryDownstreamRate_Type()
)
adGenBridgeSecondaryDownstreamRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeSecondaryDownstreamRate.setStatus("current")
_AdGenBridgePhylMapStatus_Type = DisplayString
_AdGenBridgePhylMapStatus_Object = MibScalar
adGenBridgePhylMapStatus = _AdGenBridgePhylMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 4),
    _AdGenBridgePhylMapStatus_Type()
)
adGenBridgePhylMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgePhylMapStatus.setStatus("current")
_AdGenBridgePhylMapTable_Object = MibTable
adGenBridgePhylMapTable = _AdGenBridgePhylMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 5)
)
if mibBuilder.loadTexts:
    adGenBridgePhylMapTable.setStatus("current")
_AdGenBridgePhylMapEntry_Object = MibTableRow
adGenBridgePhylMapEntry = _AdGenBridgePhylMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 5, 1)
)
adGenBridgePhylMapEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-BRIDGE-MIB", "adGenBridgePhylMapBridgeIfIndex"),
    (0, "ADTRAN-GENERIC-BRIDGE-MIB", "adGenBridgePhylMapPhylIfIndex"),
)
if mibBuilder.loadTexts:
    adGenBridgePhylMapEntry.setStatus("current")
_AdGenBridgePhylMapBridgeIfIndex_Type = InterfaceIndex
_AdGenBridgePhylMapBridgeIfIndex_Object = MibTableColumn
adGenBridgePhylMapBridgeIfIndex = _AdGenBridgePhylMapBridgeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 5, 1, 1),
    _AdGenBridgePhylMapBridgeIfIndex_Type()
)
adGenBridgePhylMapBridgeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenBridgePhylMapBridgeIfIndex.setStatus("current")
_AdGenBridgePhylMapPhylIfIndex_Type = InterfaceIndex
_AdGenBridgePhylMapPhylIfIndex_Object = MibTableColumn
adGenBridgePhylMapPhylIfIndex = _AdGenBridgePhylMapPhylIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 5, 1, 2),
    _AdGenBridgePhylMapPhylIfIndex_Type()
)
adGenBridgePhylMapPhylIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenBridgePhylMapPhylIfIndex.setStatus("current")
_AdGenBridgePhylMapOperStatus_Type = AdGenBridgePhylOperStatus
_AdGenBridgePhylMapOperStatus_Object = MibTableColumn
adGenBridgePhylMapOperStatus = _AdGenBridgePhylMapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 5, 1, 3),
    _AdGenBridgePhylMapOperStatus_Type()
)
adGenBridgePhylMapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgePhylMapOperStatus.setStatus("current")
_AdGenBridgePhylMapLastChange_Type = AdGenBridgeLastChange
_AdGenBridgePhylMapLastChange_Object = MibTableColumn
adGenBridgePhylMapLastChange = _AdGenBridgePhylMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 5, 1, 4),
    _AdGenBridgePhylMapLastChange_Type()
)
adGenBridgePhylMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgePhylMapLastChange.setStatus("current")
_AdGenBridgePhylMapLastError_Type = DisplayString
_AdGenBridgePhylMapLastError_Object = MibTableColumn
adGenBridgePhylMapLastError = _AdGenBridgePhylMapLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 5, 1, 5),
    _AdGenBridgePhylMapLastError_Type()
)
adGenBridgePhylMapLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgePhylMapLastError.setStatus("current")


class _AdGenBridgePhylMapRowStatus_Type(RowStatus):
    """Custom type adGenBridgePhylMapRowStatus based on RowStatus"""
    defaultValue = 1


_AdGenBridgePhylMapRowStatus_Type.__name__ = "RowStatus"
_AdGenBridgePhylMapRowStatus_Object = MibTableColumn
adGenBridgePhylMapRowStatus = _AdGenBridgePhylMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 5, 1, 6),
    _AdGenBridgePhylMapRowStatus_Type()
)
adGenBridgePhylMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgePhylMapRowStatus.setStatus("current")
_AdGenBridgePhylStatusTable_Object = MibTable
adGenBridgePhylStatusTable = _AdGenBridgePhylStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 6)
)
if mibBuilder.loadTexts:
    adGenBridgePhylStatusTable.setStatus("current")
_AdGenBridgePhylStatusEntry_Object = MibTableRow
adGenBridgePhylStatusEntry = _AdGenBridgePhylStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 6, 1)
)
adGenBridgePhylStatusEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-BRIDGE-MIB", "adGenBridgePhylStatusPhylIfIndex"),
)
if mibBuilder.loadTexts:
    adGenBridgePhylStatusEntry.setStatus("current")
_AdGenBridgePhylStatusPhylIfIndex_Type = InterfaceIndex
_AdGenBridgePhylStatusPhylIfIndex_Object = MibTableColumn
adGenBridgePhylStatusPhylIfIndex = _AdGenBridgePhylStatusPhylIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 6, 1, 1),
    _AdGenBridgePhylStatusPhylIfIndex_Type()
)
adGenBridgePhylStatusPhylIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenBridgePhylStatusPhylIfIndex.setStatus("current")
_AdGenBridgePhylStatusBridgeIfIndex_Type = InterfaceIndex
_AdGenBridgePhylStatusBridgeIfIndex_Object = MibTableColumn
adGenBridgePhylStatusBridgeIfIndex = _AdGenBridgePhylStatusBridgeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 6, 1, 2),
    _AdGenBridgePhylStatusBridgeIfIndex_Type()
)
adGenBridgePhylStatusBridgeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgePhylStatusBridgeIfIndex.setStatus("current")
_AdGenBridgePhylStatusBridgeType_Type = AdGenBridgeType
_AdGenBridgePhylStatusBridgeType_Object = MibTableColumn
adGenBridgePhylStatusBridgeType = _AdGenBridgePhylStatusBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 6, 1, 3),
    _AdGenBridgePhylStatusBridgeType_Type()
)
adGenBridgePhylStatusBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgePhylStatusBridgeType.setStatus("current")
_AdGenBridgePhylStatusInstallStatus_Type = AdGenBridgePhylInstalled
_AdGenBridgePhylStatusInstallStatus_Object = MibTableColumn
adGenBridgePhylStatusInstallStatus = _AdGenBridgePhylStatusInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 6, 1, 4),
    _AdGenBridgePhylStatusInstallStatus_Type()
)
adGenBridgePhylStatusInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgePhylStatusInstallStatus.setStatus("current")
_AdGenBridgePhylStatusOperStatus_Type = AdGenBridgePhylOperStatus
_AdGenBridgePhylStatusOperStatus_Object = MibTableColumn
adGenBridgePhylStatusOperStatus = _AdGenBridgePhylStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 6, 1, 5),
    _AdGenBridgePhylStatusOperStatus_Type()
)
adGenBridgePhylStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgePhylStatusOperStatus.setStatus("current")


class _AdGenBridgeProtectionGroupIndexNext_Type(Integer32):
    """Custom type adGenBridgeProtectionGroupIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AdGenBridgeProtectionGroupIndexNext_Type.__name__ = "Integer32"
_AdGenBridgeProtectionGroupIndexNext_Object = MibScalar
adGenBridgeProtectionGroupIndexNext = _AdGenBridgeProtectionGroupIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 7),
    _AdGenBridgeProtectionGroupIndexNext_Type()
)
adGenBridgeProtectionGroupIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupIndexNext.setStatus("current")
_AdGenBridgeProtectionGroupStatus_Type = DisplayString
_AdGenBridgeProtectionGroupStatus_Object = MibScalar
adGenBridgeProtectionGroupStatus = _AdGenBridgeProtectionGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 8),
    _AdGenBridgeProtectionGroupStatus_Type()
)
adGenBridgeProtectionGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupStatus.setStatus("current")
_AdGenBridgeProtectionGroupTable_Object = MibTable
adGenBridgeProtectionGroupTable = _AdGenBridgeProtectionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9)
)
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupTable.setStatus("current")
_AdGenBridgeProtectionGroupEntry_Object = MibTableRow
adGenBridgeProtectionGroupEntry = _AdGenBridgeProtectionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1)
)
adGenBridgeProtectionGroupEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-BRIDGE-MIB", "adGenBridgeProtectionGroupGroupIndex"),
)
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupEntry.setStatus("current")


class _AdGenBridgeProtectionGroupGroupIndex_Type(Integer32):
    """Custom type adGenBridgeProtectionGroupGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AdGenBridgeProtectionGroupGroupIndex_Type.__name__ = "Integer32"
_AdGenBridgeProtectionGroupGroupIndex_Object = MibTableColumn
adGenBridgeProtectionGroupGroupIndex = _AdGenBridgeProtectionGroupGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 1),
    _AdGenBridgeProtectionGroupGroupIndex_Type()
)
adGenBridgeProtectionGroupGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupGroupIndex.setStatus("current")
_AdGenBridgeProtectionGroupBridgeType_Type = AdGenBridgeType
_AdGenBridgeProtectionGroupBridgeType_Object = MibTableColumn
adGenBridgeProtectionGroupBridgeType = _AdGenBridgeProtectionGroupBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 2),
    _AdGenBridgeProtectionGroupBridgeType_Type()
)
adGenBridgeProtectionGroupBridgeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupBridgeType.setStatus("current")
_AdGenBridgeProtectionGroupName_Type = DisplayString
_AdGenBridgeProtectionGroupName_Object = MibTableColumn
adGenBridgeProtectionGroupName = _AdGenBridgeProtectionGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 3),
    _AdGenBridgeProtectionGroupName_Type()
)
adGenBridgeProtectionGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupName.setStatus("current")
_AdGenBridgeProtectionGroupProtectingSlots_Type = Unsigned32
_AdGenBridgeProtectionGroupProtectingSlots_Object = MibTableColumn
adGenBridgeProtectionGroupProtectingSlots = _AdGenBridgeProtectionGroupProtectingSlots_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 4),
    _AdGenBridgeProtectionGroupProtectingSlots_Type()
)
adGenBridgeProtectionGroupProtectingSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupProtectingSlots.setStatus("current")
_AdGenBridgeProtectionGroupProtectedSlots_Type = Unsigned32
_AdGenBridgeProtectionGroupProtectedSlots_Object = MibTableColumn
adGenBridgeProtectionGroupProtectedSlots = _AdGenBridgeProtectionGroupProtectedSlots_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 5),
    _AdGenBridgeProtectionGroupProtectedSlots_Type()
)
adGenBridgeProtectionGroupProtectedSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupProtectedSlots.setStatus("current")


class _AdGenBridgeProtectionGroupAddProtectingModule_Type(Integer32):
    """Custom type adGenBridgeProtectionGroupAddProtectingModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdGenBridgeProtectionGroupAddProtectingModule_Type.__name__ = "Integer32"
_AdGenBridgeProtectionGroupAddProtectingModule_Object = MibTableColumn
adGenBridgeProtectionGroupAddProtectingModule = _AdGenBridgeProtectionGroupAddProtectingModule_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 6),
    _AdGenBridgeProtectionGroupAddProtectingModule_Type()
)
adGenBridgeProtectionGroupAddProtectingModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupAddProtectingModule.setStatus("current")


class _AdGenBridgeProtectionGroupAddProtectedModule_Type(Integer32):
    """Custom type adGenBridgeProtectionGroupAddProtectedModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdGenBridgeProtectionGroupAddProtectedModule_Type.__name__ = "Integer32"
_AdGenBridgeProtectionGroupAddProtectedModule_Object = MibTableColumn
adGenBridgeProtectionGroupAddProtectedModule = _AdGenBridgeProtectionGroupAddProtectedModule_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 7),
    _AdGenBridgeProtectionGroupAddProtectedModule_Type()
)
adGenBridgeProtectionGroupAddProtectedModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupAddProtectedModule.setStatus("current")


class _AdGenBridgeProtectionGroupRmvProtectingModule_Type(Integer32):
    """Custom type adGenBridgeProtectionGroupRmvProtectingModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdGenBridgeProtectionGroupRmvProtectingModule_Type.__name__ = "Integer32"
_AdGenBridgeProtectionGroupRmvProtectingModule_Object = MibTableColumn
adGenBridgeProtectionGroupRmvProtectingModule = _AdGenBridgeProtectionGroupRmvProtectingModule_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 8),
    _AdGenBridgeProtectionGroupRmvProtectingModule_Type()
)
adGenBridgeProtectionGroupRmvProtectingModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupRmvProtectingModule.setStatus("current")


class _AdGenBridgeProtectionGroupRmvProtectedModule_Type(Integer32):
    """Custom type adGenBridgeProtectionGroupRmvProtectedModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdGenBridgeProtectionGroupRmvProtectedModule_Type.__name__ = "Integer32"
_AdGenBridgeProtectionGroupRmvProtectedModule_Object = MibTableColumn
adGenBridgeProtectionGroupRmvProtectedModule = _AdGenBridgeProtectionGroupRmvProtectedModule_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 9),
    _AdGenBridgeProtectionGroupRmvProtectedModule_Type()
)
adGenBridgeProtectionGroupRmvProtectedModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupRmvProtectedModule.setStatus("current")


class _AdGenBridgeProtectionGroupWaitToRestoreTime_Type(Integer32):
    """Custom type adGenBridgeProtectionGroupWaitToRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AdGenBridgeProtectionGroupWaitToRestoreTime_Type.__name__ = "Integer32"
_AdGenBridgeProtectionGroupWaitToRestoreTime_Object = MibTableColumn
adGenBridgeProtectionGroupWaitToRestoreTime = _AdGenBridgeProtectionGroupWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 10),
    _AdGenBridgeProtectionGroupWaitToRestoreTime_Type()
)
adGenBridgeProtectionGroupWaitToRestoreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupWaitToRestoreTime.setStatus("current")
_AdGenBridgeProtectionGroupLastError_Type = DisplayString
_AdGenBridgeProtectionGroupLastError_Object = MibTableColumn
adGenBridgeProtectionGroupLastError = _AdGenBridgeProtectionGroupLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 11),
    _AdGenBridgeProtectionGroupLastError_Type()
)
adGenBridgeProtectionGroupLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupLastError.setStatus("current")


class _AdGenBridgeProtectionGroupRowStatus_Type(RowStatus):
    """Custom type adGenBridgeProtectionGroupRowStatus based on RowStatus"""
    defaultValue = 1


_AdGenBridgeProtectionGroupRowStatus_Type.__name__ = "RowStatus"
_AdGenBridgeProtectionGroupRowStatus_Object = MibTableColumn
adGenBridgeProtectionGroupRowStatus = _AdGenBridgeProtectionGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 9, 1, 12),
    _AdGenBridgeProtectionGroupRowStatus_Type()
)
adGenBridgeProtectionGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupRowStatus.setStatus("current")
_AdGenBridgeProtectionTable_Object = MibTable
adGenBridgeProtectionTable = _AdGenBridgeProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10)
)
if mibBuilder.loadTexts:
    adGenBridgeProtectionTable.setStatus("current")
_AdGenBridgeProtectionEntry_Object = MibTableRow
adGenBridgeProtectionEntry = _AdGenBridgeProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1)
)
adGenBridgeProtectionEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenBridgeProtectionEntry.setStatus("current")


class _AdGenBridgeProtectionGroupIndex_Type(Integer32):
    """Custom type adGenBridgeProtectionGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AdGenBridgeProtectionGroupIndex_Type.__name__ = "Integer32"
_AdGenBridgeProtectionGroupIndex_Object = MibTableColumn
adGenBridgeProtectionGroupIndex = _AdGenBridgeProtectionGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 1),
    _AdGenBridgeProtectionGroupIndex_Type()
)
adGenBridgeProtectionGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionGroupIndex.setStatus("current")
_AdGenBridgeProtectionBridgeType_Type = AdGenBridgeType
_AdGenBridgeProtectionBridgeType_Object = MibTableColumn
adGenBridgeProtectionBridgeType = _AdGenBridgeProtectionBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 2),
    _AdGenBridgeProtectionBridgeType_Type()
)
adGenBridgeProtectionBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionBridgeType.setStatus("current")
_AdGenBridgeProtectionVersion_Type = AdGenProtectionVersion
_AdGenBridgeProtectionVersion_Object = MibTableColumn
adGenBridgeProtectionVersion = _AdGenBridgeProtectionVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 3),
    _AdGenBridgeProtectionVersion_Type()
)
adGenBridgeProtectionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionVersion.setStatus("current")


class _AdGenBridgeProtectionSlot_Type(Integer32):
    """Custom type adGenBridgeProtectionSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdGenBridgeProtectionSlot_Type.__name__ = "Integer32"
_AdGenBridgeProtectionSlot_Object = MibTableColumn
adGenBridgeProtectionSlot = _AdGenBridgeProtectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 4),
    _AdGenBridgeProtectionSlot_Type()
)
adGenBridgeProtectionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionSlot.setStatus("current")
_AdGenBridgeProtectionState_Type = Integer32
_AdGenBridgeProtectionState_Object = MibTableColumn
adGenBridgeProtectionState = _AdGenBridgeProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 5),
    _AdGenBridgeProtectionState_Type()
)
adGenBridgeProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionState.setStatus("current")


class _AdGenBridgeProtectionPriority_Type(Integer32):
    """Custom type adGenBridgeProtectionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdGenBridgeProtectionPriority_Type.__name__ = "Integer32"
_AdGenBridgeProtectionPriority_Object = MibTableColumn
adGenBridgeProtectionPriority = _AdGenBridgeProtectionPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 6),
    _AdGenBridgeProtectionPriority_Type()
)
adGenBridgeProtectionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenBridgeProtectionPriority.setStatus("current")
_AdGenBridgeProtectionRevertiveSwitch_Type = AdGenBridgeProtectionRevertiveSwitch
_AdGenBridgeProtectionRevertiveSwitch_Object = MibTableColumn
adGenBridgeProtectionRevertiveSwitch = _AdGenBridgeProtectionRevertiveSwitch_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 7),
    _AdGenBridgeProtectionRevertiveSwitch_Type()
)
adGenBridgeProtectionRevertiveSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenBridgeProtectionRevertiveSwitch.setStatus("current")
_AdGenBridgeProtectionLockout_Type = AdGenBridgeProtectionLockout
_AdGenBridgeProtectionLockout_Object = MibTableColumn
adGenBridgeProtectionLockout = _AdGenBridgeProtectionLockout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 8),
    _AdGenBridgeProtectionLockout_Type()
)
adGenBridgeProtectionLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenBridgeProtectionLockout.setStatus("current")
_AdGenBridgeProtectionManualSwitch_Type = AdGenBridgeManualSwitch
_AdGenBridgeProtectionManualSwitch_Object = MibTableColumn
adGenBridgeProtectionManualSwitch = _AdGenBridgeProtectionManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 9),
    _AdGenBridgeProtectionManualSwitch_Type()
)
adGenBridgeProtectionManualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenBridgeProtectionManualSwitch.setStatus("current")


class _AdGenBridgeProtectionManualSwitchTime_Type(Integer32):
    """Custom type adGenBridgeProtectionManualSwitchTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AdGenBridgeProtectionManualSwitchTime_Type.__name__ = "Integer32"
_AdGenBridgeProtectionManualSwitchTime_Object = MibTableColumn
adGenBridgeProtectionManualSwitchTime = _AdGenBridgeProtectionManualSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 10),
    _AdGenBridgeProtectionManualSwitchTime_Type()
)
adGenBridgeProtectionManualSwitchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenBridgeProtectionManualSwitchTime.setStatus("current")
_AdGenBridgeProtectionErrorStatus_Type = DisplayString
_AdGenBridgeProtectionErrorStatus_Object = MibTableColumn
adGenBridgeProtectionErrorStatus = _AdGenBridgeProtectionErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 10, 1, 11),
    _AdGenBridgeProtectionErrorStatus_Type()
)
adGenBridgeProtectionErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeProtectionErrorStatus.setStatus("current")
_AdGenBridgeBridgeNameLookupStatus_Type = DisplayString
_AdGenBridgeBridgeNameLookupStatus_Object = MibScalar
adGenBridgeBridgeNameLookupStatus = _AdGenBridgeBridgeNameLookupStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 11),
    _AdGenBridgeBridgeNameLookupStatus_Type()
)
adGenBridgeBridgeNameLookupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeBridgeNameLookupStatus.setStatus("current")
_AdGenBridgeNameLookupTable_Object = MibTable
adGenBridgeNameLookupTable = _AdGenBridgeNameLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 12)
)
if mibBuilder.loadTexts:
    adGenBridgeNameLookupTable.setStatus("current")
_AdGenBridgeNameLookupEntry_Object = MibTableRow
adGenBridgeNameLookupEntry = _AdGenBridgeNameLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 12, 1)
)
adGenBridgeNameLookupEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-BRIDGE-MIB", "adGenBridgeNameLookupIndex"),
)
if mibBuilder.loadTexts:
    adGenBridgeNameLookupEntry.setStatus("current")
_AdGenBridgeNameLookupIndex_Type = DisplayString
_AdGenBridgeNameLookupIndex_Object = MibTableColumn
adGenBridgeNameLookupIndex = _AdGenBridgeNameLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 12, 1, 1),
    _AdGenBridgeNameLookupIndex_Type()
)
adGenBridgeNameLookupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeNameLookupIndex.setStatus("current")
_AdGenBridgeNameIfIndex_Type = Unsigned32
_AdGenBridgeNameIfIndex_Object = MibTableColumn
adGenBridgeNameIfIndex = _AdGenBridgeNameIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 12, 1, 2),
    _AdGenBridgeNameIfIndex_Type()
)
adGenBridgeNameIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeNameIfIndex.setStatus("current")
_AdGenBridgeCount_Type = Integer32
_AdGenBridgeCount_Object = MibScalar
adGenBridgeCount = _AdGenBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 1, 13),
    _AdGenBridgeCount_Type()
)
adGenBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeCount.setStatus("current")
_AdGenEasyBridgeMIBObjects_ObjectIdentity = ObjectIdentity
adGenEasyBridgeMIBObjects = _AdGenEasyBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2)
)


class _AdGenEasyBridgeIndexNext_Type(Integer32):
    """Custom type adGenEasyBridgeIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdGenEasyBridgeIndexNext_Type.__name__ = "Integer32"
_AdGenEasyBridgeIndexNext_Object = MibScalar
adGenEasyBridgeIndexNext = _AdGenEasyBridgeIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 1),
    _AdGenEasyBridgeIndexNext_Type()
)
adGenEasyBridgeIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEasyBridgeIndexNext.setStatus("current")
_AdGenEasyBridgeTable_Object = MibTable
adGenEasyBridgeTable = _AdGenEasyBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2)
)
if mibBuilder.loadTexts:
    adGenEasyBridgeTable.setStatus("current")
_AdGenEasyBridgeEntry_Object = MibTableRow
adGenEasyBridgeEntry = _AdGenEasyBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1)
)
adGenEasyBridgeEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-BRIDGE-MIB", "adGenEasyBridgeIndex"),
)
if mibBuilder.loadTexts:
    adGenEasyBridgeEntry.setStatus("current")
_AdGenEasyBridgeIndex_Type = Integer32
_AdGenEasyBridgeIndex_Object = MibTableColumn
adGenEasyBridgeIndex = _AdGenEasyBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 1),
    _AdGenEasyBridgeIndex_Type()
)
adGenEasyBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEasyBridgeIndex.setStatus("current")


class _AdGenEasyBridgeName_Type(DisplayString):
    """Custom type adGenEasyBridgeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenEasyBridgeName_Type.__name__ = "DisplayString"
_AdGenEasyBridgeName_Object = MibTableColumn
adGenEasyBridgeName = _AdGenEasyBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 2),
    _AdGenEasyBridgeName_Type()
)
adGenEasyBridgeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeName.setStatus("current")
_AdGenEasyBridgeType_Type = AdGenBridgeType
_AdGenEasyBridgeType_Object = MibTableColumn
adGenEasyBridgeType = _AdGenEasyBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 3),
    _AdGenEasyBridgeType_Type()
)
adGenEasyBridgeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeType.setStatus("current")


class _AdGenEasyBridgeCreateOrModify_Type(Integer32):
    """Custom type adGenEasyBridgeCreateOrModify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("modify", 2))
    )


_AdGenEasyBridgeCreateOrModify_Type.__name__ = "Integer32"
_AdGenEasyBridgeCreateOrModify_Object = MibTableColumn
adGenEasyBridgeCreateOrModify = _AdGenEasyBridgeCreateOrModify_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 4),
    _AdGenEasyBridgeCreateOrModify_Type()
)
adGenEasyBridgeCreateOrModify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeCreateOrModify.setStatus("current")
_AdGenEasyBridgeUpstreamRate_Type = Integer32
_AdGenEasyBridgeUpstreamRate_Object = MibTableColumn
adGenEasyBridgeUpstreamRate = _AdGenEasyBridgeUpstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 5),
    _AdGenEasyBridgeUpstreamRate_Type()
)
adGenEasyBridgeUpstreamRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeUpstreamRate.setStatus("current")
_AdGenEasyBridgeDownstreamRate_Type = Integer32
_AdGenEasyBridgeDownstreamRate_Object = MibTableColumn
adGenEasyBridgeDownstreamRate = _AdGenEasyBridgeDownstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 6),
    _AdGenEasyBridgeDownstreamRate_Type()
)
adGenEasyBridgeDownstreamRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeDownstreamRate.setStatus("current")
_AdGenEasyBridgeMemberPhyls_Type = DisplayString
_AdGenEasyBridgeMemberPhyls_Object = MibTableColumn
adGenEasyBridgeMemberPhyls = _AdGenEasyBridgeMemberPhyls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 7),
    _AdGenEasyBridgeMemberPhyls_Type()
)
adGenEasyBridgeMemberPhyls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeMemberPhyls.setStatus("current")
_AdGenEasyBridgeMinNumActivePhyls_Type = Integer32
_AdGenEasyBridgeMinNumActivePhyls_Object = MibTableColumn
adGenEasyBridgeMinNumActivePhyls = _AdGenEasyBridgeMinNumActivePhyls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 8),
    _AdGenEasyBridgeMinNumActivePhyls_Type()
)
adGenEasyBridgeMinNumActivePhyls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeMinNumActivePhyls.setStatus("current")
_AdGenEasyBridgeStatusString_Type = DisplayString
_AdGenEasyBridgeStatusString_Object = MibTableColumn
adGenEasyBridgeStatusString = _AdGenEasyBridgeStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 9),
    _AdGenEasyBridgeStatusString_Type()
)
adGenEasyBridgeStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEasyBridgeStatusString.setStatus("current")
_AdGenEasyBridgeRowStatus_Type = RowStatus
_AdGenEasyBridgeRowStatus_Object = MibTableColumn
adGenEasyBridgeRowStatus = _AdGenEasyBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 10),
    _AdGenEasyBridgeRowStatus_Type()
)
adGenEasyBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeRowStatus.setStatus("current")
_AdGenEasyBridgeRateControl_Type = AdGenBridgeRateControl
_AdGenEasyBridgeRateControl_Object = MibTableColumn
adGenEasyBridgeRateControl = _AdGenEasyBridgeRateControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 11),
    _AdGenEasyBridgeRateControl_Type()
)
adGenEasyBridgeRateControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeRateControl.setStatus("current")
_AdGenEasyBridgeAddMemberPhyls_Type = DisplayString
_AdGenEasyBridgeAddMemberPhyls_Object = MibTableColumn
adGenEasyBridgeAddMemberPhyls = _AdGenEasyBridgeAddMemberPhyls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 12),
    _AdGenEasyBridgeAddMemberPhyls_Type()
)
adGenEasyBridgeAddMemberPhyls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeAddMemberPhyls.setStatus("current")
_AdGenEasyBridgeDeleteMemberPhyls_Type = DisplayString
_AdGenEasyBridgeDeleteMemberPhyls_Object = MibTableColumn
adGenEasyBridgeDeleteMemberPhyls = _AdGenEasyBridgeDeleteMemberPhyls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 2, 2, 1, 13),
    _AdGenEasyBridgeDeleteMemberPhyls_Type()
)
adGenEasyBridgeDeleteMemberPhyls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyBridgeDeleteMemberPhyls.setStatus("current")
_AdGenBridgeAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenBridgeAlarmsPrefix = _AdGenBridgeAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3)
)
_AdGenBridgeAlarms_ObjectIdentity = ObjectIdentity
adGenBridgeAlarms = _AdGenBridgeAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0)
)
_AdGenBulkBridge_ObjectIdentity = ObjectIdentity
adGenBulkBridge = _AdGenBulkBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 4)
)
_AdGenBridgeBulkInstanceTable_Object = MibTable
adGenBridgeBulkInstanceTable = _AdGenBridgeBulkInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 4, 1)
)
if mibBuilder.loadTexts:
    adGenBridgeBulkInstanceTable.setStatus("current")
_AdGenBridgeBulkInstanceEntry_Object = MibTableRow
adGenBridgeBulkInstanceEntry = _AdGenBridgeBulkInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 4, 1, 1)
)
adGenBridgeBulkInstanceEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenBridgeBulkInstanceEntry.setStatus("current")
_AdGenBridgeBulkInstance_Type = Integer32
_AdGenBridgeBulkInstance_Object = MibTableColumn
adGenBridgeBulkInstance = _AdGenBridgeBulkInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 4, 1, 1, 1),
    _AdGenBridgeBulkInstance_Type()
)
adGenBridgeBulkInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBridgeBulkInstance.setStatus("current")

# Managed Objects groups


# Notification objects

adGenBridgeNonProtectedAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 2)
)
adGenBridgeNonProtectedAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeNonProtectedAlmCLR.setStatus(
        "current"
    )

adGenBridgeNonProtectedAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 3)
)
adGenBridgeNonProtectedAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeNonProtectedAlmACT.setStatus(
        "current"
    )

adGenBridgeProtectedAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 4)
)
adGenBridgeProtectedAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeProtectedAlmCLR.setStatus(
        "current"
    )

adGenBridgeProtectedAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 5)
)
adGenBridgeProtectedAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeProtectedAlmACT.setStatus(
        "current"
    )

adGenBridgeNeedsProtectionAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 6)
)
adGenBridgeNeedsProtectionAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeNeedsProtectionAlmCLR.setStatus(
        "current"
    )

adGenBridgeNeedsProtectionAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 7)
)
adGenBridgeNeedsProtectionAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeNeedsProtectionAlmACT.setStatus(
        "current"
    )

adGenBridgeManualProtectionAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 8)
)
adGenBridgeManualProtectionAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeManualProtectionAlmCLR.setStatus(
        "current"
    )

adGenBridgeManualProtectionAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 9)
)
adGenBridgeManualProtectionAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeManualProtectionAlmACT.setStatus(
        "current"
    )

adGenBridgeLockoutProtectionAlmCLR = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 10)
)
adGenBridgeLockoutProtectionAlmCLR.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeLockoutProtectionAlmCLR.setStatus(
        "current"
    )

adGenBridgeLockoutProtectionAlmACT = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 16, 3, 0, 11)
)
adGenBridgeLockoutProtectionAlmACT.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenBridgeLockoutProtectionAlmACT.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-BRIDGE-MIB",
    **{"AdGenBridgeProtMode": AdGenBridgeProtMode,
       "AdGenBridgeProtAvail": AdGenBridgeProtAvail,
       "AdGenBridgeProtState": AdGenBridgeProtState,
       "AdGenBridgeOperStatus": AdGenBridgeOperStatus,
       "AdGenBridgePhylOperStatus": AdGenBridgePhylOperStatus,
       "AdGenBridgeType": AdGenBridgeType,
       "AdGenBridgeRateControl": AdGenBridgeRateControl,
       "AdGenBridgeLastChange": AdGenBridgeLastChange,
       "AdGenBridgeAlarmSuppress": AdGenBridgeAlarmSuppress,
       "AdGenBridgePhylInstalled": AdGenBridgePhylInstalled,
       "AdGenBridgeProtectionRevertiveSwitch": AdGenBridgeProtectionRevertiveSwitch,
       "AdGenBridgeProtectionLockout": AdGenBridgeProtectionLockout,
       "AdGenBridgeManualSwitch": AdGenBridgeManualSwitch,
       "AdGenProtectionVersion": AdGenProtectionVersion,
       "adGenBridgeMIBObjects": adGenBridgeMIBObjects,
       "adGenBridgeModuleConfTable": adGenBridgeModuleConfTable,
       "adGenBridgeModuleConfEntry": adGenBridgeModuleConfEntry,
       "adGenBridgeModuleMaxBridges": adGenBridgeModuleMaxBridges,
       "adGenBridgeModuleMaxPhyls": adGenBridgeModuleMaxPhyls,
       "adGenBridgeModuleConfBridges": adGenBridgeModuleConfBridges,
       "adGenBridgeModuleConfPhyls": adGenBridgeModuleConfPhyls,
       "adGenBridgeModuleMaxBandwidth": adGenBridgeModuleMaxBandwidth,
       "adGenBridgeModuleConfBandwidth": adGenBridgeModuleConfBandwidth,
       "adGenBridgeStatus": adGenBridgeStatus,
       "adGenBridgeTable": adGenBridgeTable,
       "adGenBridgeEntry": adGenBridgeEntry,
       "adGenBridgeIfIndex": adGenBridgeIfIndex,
       "adGenBridgeType": adGenBridgeType,
       "adGenBridgeName": adGenBridgeName,
       "adGenBridgeProtMode": adGenBridgeProtMode,
       "adGenBridgeProtAvail": adGenBridgeProtAvail,
       "adGenBridgeProtState": adGenBridgeProtState,
       "adGenBridgeProtSlot": adGenBridgeProtSlot,
       "adGenBridgeMinNumActivePhyls": adGenBridgeMinNumActivePhyls,
       "adGenBridgeOperStatus": adGenBridgeOperStatus,
       "adGenBridgeLastChange": adGenBridgeLastChange,
       "adGenBridgeNumCfgEVPLs": adGenBridgeNumCfgEVPLs,
       "adGenBridgeNumCfgEVCLs": adGenBridgeNumCfgEVCLs,
       "adGenBridgeNumCfgPhyls": adGenBridgeNumCfgPhyls,
       "adGenBridgeNumActPhyls": adGenBridgeNumActPhyls,
       "adGenBridgeLastError": adGenBridgeLastError,
       "adGenBridgeRowStatus": adGenBridgeRowStatus,
       "adGenBridgeMaxBandwidth": adGenBridgeMaxBandwidth,
       "adGenBridgeCurrentBandwidth": adGenBridgeCurrentBandwidth,
       "adGenBridgeUpstreamRate": adGenBridgeUpstreamRate,
       "adGenBridgeDownstreamRate": adGenBridgeDownstreamRate,
       "adGenBridgeCurrentUpstreamRate": adGenBridgeCurrentUpstreamRate,
       "adGenBridgeCurrentDownstreamRate": adGenBridgeCurrentDownstreamRate,
       "adGenBridgeRateControl": adGenBridgeRateControl,
       "adGenBridgeAlarmSuppress": adGenBridgeAlarmSuppress,
       "adGenBridgeSecondaryUpstreamRate": adGenBridgeSecondaryUpstreamRate,
       "adGenBridgeSecondaryDownstreamRate": adGenBridgeSecondaryDownstreamRate,
       "adGenBridgePhylMapStatus": adGenBridgePhylMapStatus,
       "adGenBridgePhylMapTable": adGenBridgePhylMapTable,
       "adGenBridgePhylMapEntry": adGenBridgePhylMapEntry,
       "adGenBridgePhylMapBridgeIfIndex": adGenBridgePhylMapBridgeIfIndex,
       "adGenBridgePhylMapPhylIfIndex": adGenBridgePhylMapPhylIfIndex,
       "adGenBridgePhylMapOperStatus": adGenBridgePhylMapOperStatus,
       "adGenBridgePhylMapLastChange": adGenBridgePhylMapLastChange,
       "adGenBridgePhylMapLastError": adGenBridgePhylMapLastError,
       "adGenBridgePhylMapRowStatus": adGenBridgePhylMapRowStatus,
       "adGenBridgePhylStatusTable": adGenBridgePhylStatusTable,
       "adGenBridgePhylStatusEntry": adGenBridgePhylStatusEntry,
       "adGenBridgePhylStatusPhylIfIndex": adGenBridgePhylStatusPhylIfIndex,
       "adGenBridgePhylStatusBridgeIfIndex": adGenBridgePhylStatusBridgeIfIndex,
       "adGenBridgePhylStatusBridgeType": adGenBridgePhylStatusBridgeType,
       "adGenBridgePhylStatusInstallStatus": adGenBridgePhylStatusInstallStatus,
       "adGenBridgePhylStatusOperStatus": adGenBridgePhylStatusOperStatus,
       "adGenBridgeProtectionGroupIndexNext": adGenBridgeProtectionGroupIndexNext,
       "adGenBridgeProtectionGroupStatus": adGenBridgeProtectionGroupStatus,
       "adGenBridgeProtectionGroupTable": adGenBridgeProtectionGroupTable,
       "adGenBridgeProtectionGroupEntry": adGenBridgeProtectionGroupEntry,
       "adGenBridgeProtectionGroupGroupIndex": adGenBridgeProtectionGroupGroupIndex,
       "adGenBridgeProtectionGroupBridgeType": adGenBridgeProtectionGroupBridgeType,
       "adGenBridgeProtectionGroupName": adGenBridgeProtectionGroupName,
       "adGenBridgeProtectionGroupProtectingSlots": adGenBridgeProtectionGroupProtectingSlots,
       "adGenBridgeProtectionGroupProtectedSlots": adGenBridgeProtectionGroupProtectedSlots,
       "adGenBridgeProtectionGroupAddProtectingModule": adGenBridgeProtectionGroupAddProtectingModule,
       "adGenBridgeProtectionGroupAddProtectedModule": adGenBridgeProtectionGroupAddProtectedModule,
       "adGenBridgeProtectionGroupRmvProtectingModule": adGenBridgeProtectionGroupRmvProtectingModule,
       "adGenBridgeProtectionGroupRmvProtectedModule": adGenBridgeProtectionGroupRmvProtectedModule,
       "adGenBridgeProtectionGroupWaitToRestoreTime": adGenBridgeProtectionGroupWaitToRestoreTime,
       "adGenBridgeProtectionGroupLastError": adGenBridgeProtectionGroupLastError,
       "adGenBridgeProtectionGroupRowStatus": adGenBridgeProtectionGroupRowStatus,
       "adGenBridgeProtectionTable": adGenBridgeProtectionTable,
       "adGenBridgeProtectionEntry": adGenBridgeProtectionEntry,
       "adGenBridgeProtectionGroupIndex": adGenBridgeProtectionGroupIndex,
       "adGenBridgeProtectionBridgeType": adGenBridgeProtectionBridgeType,
       "adGenBridgeProtectionVersion": adGenBridgeProtectionVersion,
       "adGenBridgeProtectionSlot": adGenBridgeProtectionSlot,
       "adGenBridgeProtectionState": adGenBridgeProtectionState,
       "adGenBridgeProtectionPriority": adGenBridgeProtectionPriority,
       "adGenBridgeProtectionRevertiveSwitch": adGenBridgeProtectionRevertiveSwitch,
       "adGenBridgeProtectionLockout": adGenBridgeProtectionLockout,
       "adGenBridgeProtectionManualSwitch": adGenBridgeProtectionManualSwitch,
       "adGenBridgeProtectionManualSwitchTime": adGenBridgeProtectionManualSwitchTime,
       "adGenBridgeProtectionErrorStatus": adGenBridgeProtectionErrorStatus,
       "adGenBridgeBridgeNameLookupStatus": adGenBridgeBridgeNameLookupStatus,
       "adGenBridgeNameLookupTable": adGenBridgeNameLookupTable,
       "adGenBridgeNameLookupEntry": adGenBridgeNameLookupEntry,
       "adGenBridgeNameLookupIndex": adGenBridgeNameLookupIndex,
       "adGenBridgeNameIfIndex": adGenBridgeNameIfIndex,
       "adGenBridgeCount": adGenBridgeCount,
       "adGenEasyBridgeMIBObjects": adGenEasyBridgeMIBObjects,
       "adGenEasyBridgeIndexNext": adGenEasyBridgeIndexNext,
       "adGenEasyBridgeTable": adGenEasyBridgeTable,
       "adGenEasyBridgeEntry": adGenEasyBridgeEntry,
       "adGenEasyBridgeIndex": adGenEasyBridgeIndex,
       "adGenEasyBridgeName": adGenEasyBridgeName,
       "adGenEasyBridgeType": adGenEasyBridgeType,
       "adGenEasyBridgeCreateOrModify": adGenEasyBridgeCreateOrModify,
       "adGenEasyBridgeUpstreamRate": adGenEasyBridgeUpstreamRate,
       "adGenEasyBridgeDownstreamRate": adGenEasyBridgeDownstreamRate,
       "adGenEasyBridgeMemberPhyls": adGenEasyBridgeMemberPhyls,
       "adGenEasyBridgeMinNumActivePhyls": adGenEasyBridgeMinNumActivePhyls,
       "adGenEasyBridgeStatusString": adGenEasyBridgeStatusString,
       "adGenEasyBridgeRowStatus": adGenEasyBridgeRowStatus,
       "adGenEasyBridgeRateControl": adGenEasyBridgeRateControl,
       "adGenEasyBridgeAddMemberPhyls": adGenEasyBridgeAddMemberPhyls,
       "adGenEasyBridgeDeleteMemberPhyls": adGenEasyBridgeDeleteMemberPhyls,
       "adGenBridgeAlarmsPrefix": adGenBridgeAlarmsPrefix,
       "adGenBridgeAlarms": adGenBridgeAlarms,
       "adGenBridgeNonProtectedAlmCLR": adGenBridgeNonProtectedAlmCLR,
       "adGenBridgeNonProtectedAlmACT": adGenBridgeNonProtectedAlmACT,
       "adGenBridgeProtectedAlmCLR": adGenBridgeProtectedAlmCLR,
       "adGenBridgeProtectedAlmACT": adGenBridgeProtectedAlmACT,
       "adGenBridgeNeedsProtectionAlmCLR": adGenBridgeNeedsProtectionAlmCLR,
       "adGenBridgeNeedsProtectionAlmACT": adGenBridgeNeedsProtectionAlmACT,
       "adGenBridgeManualProtectionAlmCLR": adGenBridgeManualProtectionAlmCLR,
       "adGenBridgeManualProtectionAlmACT": adGenBridgeManualProtectionAlmACT,
       "adGenBridgeLockoutProtectionAlmCLR": adGenBridgeLockoutProtectionAlmCLR,
       "adGenBridgeLockoutProtectionAlmACT": adGenBridgeLockoutProtectionAlmACT,
       "adGenBulkBridge": adGenBulkBridge,
       "adGenBridgeBulkInstanceTable": adGenBridgeBulkInstanceTable,
       "adGenBridgeBulkInstanceEntry": adGenBridgeBulkInstanceEntry,
       "adGenBridgeBulkInstance": adGenBridgeBulkInstance,
       "adGenBridgeMIB": adGenBridgeMIB}
)
