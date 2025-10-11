# SNMP MIB module (RAD-BROADBAND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-BROADBAND-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:19:07 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(diverseIfWanGen,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "diverseIfWanGen")

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

broadbandIf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BdbandConfig_ObjectIdentity = ObjectIdentity
bdbandConfig = _BdbandConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1)
)
_PrtBdbandIndTable_Object = MibTable
prtBdbandIndTable = _PrtBdbandIndTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 1)
)
if mibBuilder.loadTexts:
    prtBdbandIndTable.setStatus("current")
_PrtBdbandIndEntry_Object = MibTableRow
prtBdbandIndEntry = _PrtBdbandIndEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 1, 1)
)
prtBdbandIndEntry.setIndexNames(
    (0, "RAD-BROADBAND-MIB", "prtBdbandCnfgIdx"),
    (0, "RAD-BROADBAND-MIB", "prtBdbandIdx"),
    (0, "RAD-BROADBAND-MIB", "prtBdbandIndSig"),
    (0, "RAD-BROADBAND-MIB", "prtBdbandIndEvent"),
)
if mibBuilder.loadTexts:
    prtBdbandIndEntry.setStatus("current")


class _PrtBdbandCnfgIdx_Type(Integer32):
    """Custom type prtBdbandCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtBdbandCnfgIdx_Type.__name__ = "Integer32"
_PrtBdbandCnfgIdx_Object = MibTableColumn
prtBdbandCnfgIdx = _PrtBdbandCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 1, 1, 1),
    _PrtBdbandCnfgIdx_Type()
)
prtBdbandCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBdbandCnfgIdx.setStatus("current")
_PrtBdbandIdx_Type = Integer32
_PrtBdbandIdx_Object = MibTableColumn
prtBdbandIdx = _PrtBdbandIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 1, 1, 2),
    _PrtBdbandIdx_Type()
)
prtBdbandIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBdbandIdx.setStatus("current")


class _PrtBdbandIndSig_Type(Integer32):
    """Custom type prtBdbandIndSig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ais", 1),
          ("rdi", 2),
          ("aisAndRdi", 3))
    )


_PrtBdbandIndSig_Type.__name__ = "Integer32"
_PrtBdbandIndSig_Object = MibTableColumn
prtBdbandIndSig = _PrtBdbandIndSig_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 1, 1, 3),
    _PrtBdbandIndSig_Type()
)
prtBdbandIndSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBdbandIndSig.setStatus("current")


class _PrtBdbandIndEvent_Type(Integer32):
    """Custom type prtBdbandIndEvent based on Integer32"""
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
        *(("notApplicable", 1),
          ("slm", 2),
          ("fail", 3),
          ("eed", 4),
          ("pathTrace", 5),
          ("lom", 6),
          ("lop", 7),
          ("slu", 8))
    )


_PrtBdbandIndEvent_Type.__name__ = "Integer32"
_PrtBdbandIndEvent_Object = MibTableColumn
prtBdbandIndEvent = _PrtBdbandIndEvent_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 1, 1, 4),
    _PrtBdbandIndEvent_Type()
)
prtBdbandIndEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtBdbandIndEvent.setStatus("current")


class _PrtBdbandIndSigEnable_Type(Integer32):
    """Custom type prtBdbandIndSigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_PrtBdbandIndSigEnable_Type.__name__ = "Integer32"
_PrtBdbandIndSigEnable_Object = MibTableColumn
prtBdbandIndSigEnable = _PrtBdbandIndSigEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 1, 1, 5),
    _PrtBdbandIndSigEnable_Type()
)
prtBdbandIndSigEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtBdbandIndSigEnable.setStatus("current")
_PrtBdbandRowStatus_Type = RowStatus
_PrtBdbandRowStatus_Object = MibTableColumn
prtBdbandRowStatus = _PrtBdbandRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 1, 1, 6),
    _PrtBdbandRowStatus_Type()
)
prtBdbandRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtBdbandRowStatus.setStatus("current")
_PrtPhyConfigTable_Object = MibTable
prtPhyConfigTable = _PrtPhyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 2)
)
if mibBuilder.loadTexts:
    prtPhyConfigTable.setStatus("current")
_PrtPhyConfigEntry_Object = MibTableRow
prtPhyConfigEntry = _PrtPhyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 2, 1)
)
prtPhyConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtPhyConfigEntry.setStatus("current")


class _PrtPhyTimeElapsed_Type(Integer32):
    """Custom type prtPhyTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_PrtPhyTimeElapsed_Type.__name__ = "Integer32"
_PrtPhyTimeElapsed_Object = MibTableColumn
prtPhyTimeElapsed = _PrtPhyTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 2, 1, 1),
    _PrtPhyTimeElapsed_Type()
)
prtPhyTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyTimeElapsed.setStatus("current")


class _PrtPhyValidIntervals_Type(Integer32):
    """Custom type prtPhyValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_PrtPhyValidIntervals_Type.__name__ = "Integer32"
_PrtPhyValidIntervals_Object = MibTableColumn
prtPhyValidIntervals = _PrtPhyValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 1, 2, 1, 2),
    _PrtPhyValidIntervals_Type()
)
prtPhyValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyValidIntervals.setStatus("current")
_PrtPhyPerfHistory_ObjectIdentity = ObjectIdentity
prtPhyPerfHistory = _PrtPhyPerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2)
)
_PrtPhyCurrentTable_Object = MibTable
prtPhyCurrentTable = _PrtPhyCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 1)
)
if mibBuilder.loadTexts:
    prtPhyCurrentTable.setStatus("current")
_PrtPhyCurrentEntry_Object = MibTableRow
prtPhyCurrentEntry = _PrtPhyCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 1, 1)
)
prtPhyCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtPhyCurrentEntry.setStatus("current")
_PrtPhyCurrentLOS_Type = Gauge32
_PrtPhyCurrentLOS_Object = MibTableColumn
prtPhyCurrentLOS = _PrtPhyCurrentLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 1, 1, 1),
    _PrtPhyCurrentLOS_Type()
)
prtPhyCurrentLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyCurrentLOS.setStatus("current")
_PrtPhyCurrentLSV_Type = Gauge32
_PrtPhyCurrentLSV_Object = MibTableColumn
prtPhyCurrentLSV = _PrtPhyCurrentLSV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 1, 1, 2),
    _PrtPhyCurrentLSV_Type()
)
prtPhyCurrentLSV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyCurrentLSV.setStatus("current")
_PrtPhyCurrentUAS_Type = Gauge32
_PrtPhyCurrentUAS_Object = MibTableColumn
prtPhyCurrentUAS = _PrtPhyCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 1, 1, 3),
    _PrtPhyCurrentUAS_Type()
)
prtPhyCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyCurrentUAS.setStatus("current")
_PrtPhyCurrentSES_Type = Gauge32
_PrtPhyCurrentSES_Object = MibTableColumn
prtPhyCurrentSES = _PrtPhyCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 1, 1, 4),
    _PrtPhyCurrentSES_Type()
)
prtPhyCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyCurrentSES.setStatus("current")
_PrtPhyCurrentES_Type = Gauge32
_PrtPhyCurrentES_Object = MibTableColumn
prtPhyCurrentES = _PrtPhyCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 1, 1, 5),
    _PrtPhyCurrentES_Type()
)
prtPhyCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyCurrentES.setStatus("current")


class _PrtPhyCurrentStatus_Type(OctetString):
    """Custom type prtPhyCurrentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PrtPhyCurrentStatus_Type.__name__ = "OctetString"
_PrtPhyCurrentStatus_Object = MibTableColumn
prtPhyCurrentStatus = _PrtPhyCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 1, 1, 6),
    _PrtPhyCurrentStatus_Type()
)
prtPhyCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyCurrentStatus.setStatus("current")
_PrtPhyCurrentLOF_Type = Gauge32
_PrtPhyCurrentLOF_Object = MibTableColumn
prtPhyCurrentLOF = _PrtPhyCurrentLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 1, 1, 7),
    _PrtPhyCurrentLOF_Type()
)
prtPhyCurrentLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyCurrentLOF.setStatus("current")
_PrtPhyIntervalTable_Object = MibTable
prtPhyIntervalTable = _PrtPhyIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2)
)
if mibBuilder.loadTexts:
    prtPhyIntervalTable.setStatus("current")
_PrtPhyIntervalEntry_Object = MibTableRow
prtPhyIntervalEntry = _PrtPhyIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2, 1)
)
prtPhyIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-BROADBAND-MIB", "prtPhyIntervalNumber"),
)
if mibBuilder.loadTexts:
    prtPhyIntervalEntry.setStatus("current")


class _PrtPhyIntervalNumber_Type(Integer32):
    """Custom type prtPhyIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PrtPhyIntervalNumber_Type.__name__ = "Integer32"
_PrtPhyIntervalNumber_Object = MibTableColumn
prtPhyIntervalNumber = _PrtPhyIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2, 1, 1),
    _PrtPhyIntervalNumber_Type()
)
prtPhyIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyIntervalNumber.setStatus("current")
_PrtPhyIntervalLOS_Type = Gauge32
_PrtPhyIntervalLOS_Object = MibTableColumn
prtPhyIntervalLOS = _PrtPhyIntervalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2, 1, 2),
    _PrtPhyIntervalLOS_Type()
)
prtPhyIntervalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyIntervalLOS.setStatus("current")
_PrtPhyIntervalLSV_Type = Gauge32
_PrtPhyIntervalLSV_Object = MibTableColumn
prtPhyIntervalLSV = _PrtPhyIntervalLSV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2, 1, 3),
    _PrtPhyIntervalLSV_Type()
)
prtPhyIntervalLSV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyIntervalLSV.setStatus("current")
_PrtPhyIntervalUAS_Type = Gauge32
_PrtPhyIntervalUAS_Object = MibTableColumn
prtPhyIntervalUAS = _PrtPhyIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2, 1, 4),
    _PrtPhyIntervalUAS_Type()
)
prtPhyIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyIntervalUAS.setStatus("current")
_PrtPhyIntervalSES_Type = Gauge32
_PrtPhyIntervalSES_Object = MibTableColumn
prtPhyIntervalSES = _PrtPhyIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2, 1, 5),
    _PrtPhyIntervalSES_Type()
)
prtPhyIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyIntervalSES.setStatus("current")
_PrtPhyIntervalES_Type = Gauge32
_PrtPhyIntervalES_Object = MibTableColumn
prtPhyIntervalES = _PrtPhyIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2, 1, 6),
    _PrtPhyIntervalES_Type()
)
prtPhyIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyIntervalES.setStatus("current")


class _PrtPhyIntervalStatus_Type(OctetString):
    """Custom type prtPhyIntervalStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PrtPhyIntervalStatus_Type.__name__ = "OctetString"
_PrtPhyIntervalStatus_Object = MibTableColumn
prtPhyIntervalStatus = _PrtPhyIntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2, 1, 7),
    _PrtPhyIntervalStatus_Type()
)
prtPhyIntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyIntervalStatus.setStatus("current")
_PrtPhyIntervalLOF_Type = Gauge32
_PrtPhyIntervalLOF_Object = MibTableColumn
prtPhyIntervalLOF = _PrtPhyIntervalLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 8, 2, 2, 1, 8),
    _PrtPhyIntervalLOF_Type()
)
prtPhyIntervalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhyIntervalLOF.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-BROADBAND-MIB",
    **{"broadbandIf": broadbandIf,
       "bdbandConfig": bdbandConfig,
       "prtBdbandIndTable": prtBdbandIndTable,
       "prtBdbandIndEntry": prtBdbandIndEntry,
       "prtBdbandCnfgIdx": prtBdbandCnfgIdx,
       "prtBdbandIdx": prtBdbandIdx,
       "prtBdbandIndSig": prtBdbandIndSig,
       "prtBdbandIndEvent": prtBdbandIndEvent,
       "prtBdbandIndSigEnable": prtBdbandIndSigEnable,
       "prtBdbandRowStatus": prtBdbandRowStatus,
       "prtPhyConfigTable": prtPhyConfigTable,
       "prtPhyConfigEntry": prtPhyConfigEntry,
       "prtPhyTimeElapsed": prtPhyTimeElapsed,
       "prtPhyValidIntervals": prtPhyValidIntervals,
       "prtPhyPerfHistory": prtPhyPerfHistory,
       "prtPhyCurrentTable": prtPhyCurrentTable,
       "prtPhyCurrentEntry": prtPhyCurrentEntry,
       "prtPhyCurrentLOS": prtPhyCurrentLOS,
       "prtPhyCurrentLSV": prtPhyCurrentLSV,
       "prtPhyCurrentUAS": prtPhyCurrentUAS,
       "prtPhyCurrentSES": prtPhyCurrentSES,
       "prtPhyCurrentES": prtPhyCurrentES,
       "prtPhyCurrentStatus": prtPhyCurrentStatus,
       "prtPhyCurrentLOF": prtPhyCurrentLOF,
       "prtPhyIntervalTable": prtPhyIntervalTable,
       "prtPhyIntervalEntry": prtPhyIntervalEntry,
       "prtPhyIntervalNumber": prtPhyIntervalNumber,
       "prtPhyIntervalLOS": prtPhyIntervalLOS,
       "prtPhyIntervalLSV": prtPhyIntervalLSV,
       "prtPhyIntervalUAS": prtPhyIntervalUAS,
       "prtPhyIntervalSES": prtPhyIntervalSES,
       "prtPhyIntervalES": prtPhyIntervalES,
       "prtPhyIntervalStatus": prtPhyIntervalStatus,
       "prtPhyIntervalLOF": prtPhyIntervalLOF}
)
