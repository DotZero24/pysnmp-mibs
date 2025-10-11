# SNMP MIB module (RAD-Mpmx-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-Mpmx-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:52 2025
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

(ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias",
    "ifIndex")

(agnLed,
 alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "agnLed",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(radWan,
 wanGen) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radWan",
    "wanGen")

(CardType,
 ProtectLastSwitchReasonType) = mibBuilder.importSymbols(
    "RAD-TC",
    "CardType",
    "ProtectLastSwitchReasonType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

chasWanGen = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ChasVersion_Type(DisplayString):
    """Custom type chasVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasVersion_Type.__name__ = "DisplayString"
_ChasVersion_Object = MibScalar
chasVersion = _ChasVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 1, 1),
    _ChasVersion_Type()
)
chasVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasVersion.setStatus("current")
_ChasTotalNoOfSlt_Type = Integer32
_ChasTotalNoOfSlt_Object = MibScalar
chasTotalNoOfSlt = _ChasTotalNoOfSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 1, 2),
    _ChasTotalNoOfSlt_Type()
)
chasTotalNoOfSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTotalNoOfSlt.setStatus("current")
_ChasTotalNoOfIoSlt_Type = Integer32
_ChasTotalNoOfIoSlt_Object = MibScalar
chasTotalNoOfIoSlt = _ChasTotalNoOfIoSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 1, 3),
    _ChasTotalNoOfIoSlt_Type()
)
chasTotalNoOfIoSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTotalNoOfIoSlt.setStatus("current")
_ChasTotalNoOfPsSlt_Type = Integer32
_ChasTotalNoOfPsSlt_Object = MibScalar
chasTotalNoOfPsSlt = _ChasTotalNoOfPsSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 1, 4),
    _ChasTotalNoOfPsSlt_Type()
)
chasTotalNoOfPsSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTotalNoOfPsSlt.setStatus("current")
_ChasTotalNoOfClSlt_Type = Integer32
_ChasTotalNoOfClSlt_Object = MibScalar
chasTotalNoOfClSlt = _ChasTotalNoOfClSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 1, 5),
    _ChasTotalNoOfClSlt_Type()
)
chasTotalNoOfClSlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTotalNoOfClSlt.setStatus("current")
_AgnWanGen_ObjectIdentity = ObjectIdentity
agnWanGen = _AgnWanGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2)
)
_StatAgnGen_ObjectIdentity = ObjectIdentity
statAgnGen = _StatAgnGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1)
)


class _AgnSDateFormat_Type(Integer32):
    """Custom type agnSDateFormat based on Integer32"""
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
        *(("ddMMYYYY", 1),
          ("mmDDYYYY", 2),
          ("yyyyDDMM", 3),
          ("yyyyMMDD", 4))
    )


_AgnSDateFormat_Type.__name__ = "Integer32"
_AgnSDateFormat_Object = MibScalar
agnSDateFormat = _AgnSDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 1),
    _AgnSDateFormat_Type()
)
agnSDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSDateFormat.setStatus("current")


class _AgnSDateCmd_Type(DisplayString):
    """Custom type agnSDateCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgnSDateCmd_Type.__name__ = "DisplayString"
_AgnSDateCmd_Object = MibScalar
agnSDateCmd = _AgnSDateCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 2),
    _AgnSDateCmd_Type()
)
agnSDateCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSDateCmd.setStatus("current")


class _AgnSTimeCmd_Type(DisplayString):
    """Custom type agnSTimeCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgnSTimeCmd_Type.__name__ = "DisplayString"
_AgnSTimeCmd_Object = MibScalar
agnSTimeCmd = _AgnSTimeCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 3),
    _AgnSTimeCmd_Type()
)
agnSTimeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSTimeCmd.setStatus("current")
_AgnSActiveCnfg_Type = Integer32
_AgnSActiveCnfg_Object = MibScalar
agnSActiveCnfg = _AgnSActiveCnfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 4),
    _AgnSActiveCnfg_Type()
)
agnSActiveCnfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSActiveCnfg.setStatus("current")
_AgnSEditCnfg_Type = Integer32
_AgnSEditCnfg_Object = MibScalar
agnSEditCnfg = _AgnSEditCnfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 5),
    _AgnSEditCnfg_Type()
)
agnSEditCnfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSEditCnfg.setStatus("current")


class _AgnSLastCnfgFlipTime_Type(DisplayString):
    """Custom type agnSLastCnfgFlipTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgnSLastCnfgFlipTime_Type.__name__ = "DisplayString"
_AgnSLastCnfgFlipTime_Object = MibScalar
agnSLastCnfgFlipTime = _AgnSLastCnfgFlipTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 6),
    _AgnSLastCnfgFlipTime_Type()
)
agnSLastCnfgFlipTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSLastCnfgFlipTime.setStatus("current")


class _AgnSLastCnfgFlipCause_Type(DisplayString):
    """Custom type agnSLastCnfgFlipCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgnSLastCnfgFlipCause_Type.__name__ = "DisplayString"
_AgnSLastCnfgFlipCause_Object = MibScalar
agnSLastCnfgFlipCause = _AgnSLastCnfgFlipCause_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 7),
    _AgnSLastCnfgFlipCause_Type()
)
agnSLastCnfgFlipCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSLastCnfgFlipCause.setStatus("current")


class _AgnSEditBy_Type(Integer32):
    """Custom type agnSEditBy based on Integer32"""
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
        *(("none", 1),
          ("snmp", 2),
          ("terCon1", 3),
          ("terCon2", 4),
          ("terInbandCon1", 5),
          ("terInbandCon2", 6),
          ("lcd", 7))
    )


_AgnSEditBy_Type.__name__ = "Integer32"
_AgnSEditBy_Object = MibScalar
agnSEditBy = _AgnSEditBy_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 8),
    _AgnSEditBy_Type()
)
agnSEditBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSEditBy.setStatus("current")


class _AgnSClkSrc_Type(Integer32):
    """Custom type agnSClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("fallback", 2),
          ("internal", 3))
    )


_AgnSClkSrc_Type.__name__ = "Integer32"
_AgnSClkSrc_Object = MibScalar
agnSClkSrc = _AgnSClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 9),
    _AgnSClkSrc_Type()
)
agnSClkSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSClkSrc.setStatus("current")


class _AgnSAlrStatus_Type(Integer32):
    """Custom type agnSAlrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnSAlrStatus_Type.__name__ = "Integer32"
_AgnSAlrStatus_Object = MibScalar
agnSAlrStatus = _AgnSAlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 10),
    _AgnSAlrStatus_Type()
)
agnSAlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrStatus.setStatus("current")


class _AgnSAlrStatusAll_Type(Integer32):
    """Custom type agnSAlrStatusAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnSAlrStatusAll_Type.__name__ = "Integer32"
_AgnSAlrStatusAll_Object = MibScalar
agnSAlrStatusAll = _AgnSAlrStatusAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 11),
    _AgnSAlrStatusAll_Type()
)
agnSAlrStatusAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrStatusAll.setStatus("current")


class _AgnSMaskedAlrStat_Type(Integer32):
    """Custom type agnSMaskedAlrStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnSMaskedAlrStat_Type.__name__ = "Integer32"
_AgnSMaskedAlrStat_Object = MibScalar
agnSMaskedAlrStat = _AgnSMaskedAlrStat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 12),
    _AgnSMaskedAlrStat_Type()
)
agnSMaskedAlrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSMaskedAlrStat.setStatus("current")


class _AgnSMaskedAlrStatAll_Type(Integer32):
    """Custom type agnSMaskedAlrStatAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnSMaskedAlrStatAll_Type.__name__ = "Integer32"
_AgnSMaskedAlrStatAll_Object = MibScalar
agnSMaskedAlrStatAll = _AgnSMaskedAlrStatAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 13),
    _AgnSMaskedAlrStatAll_Type()
)
agnSMaskedAlrStatAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSMaskedAlrStatAll.setStatus("current")


class _AgnSTstStatAll_Type(Integer32):
    """Custom type agnSTstStatAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnSTstStatAll_Type.__name__ = "Integer32"
_AgnSTstStatAll_Object = MibScalar
agnSTstStatAll = _AgnSTstStatAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 14),
    _AgnSTstStatAll_Type()
)
agnSTstStatAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSTstStatAll.setStatus("current")
_AgnSAlrTable_Object = MibTable
agnSAlrTable = _AgnSAlrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15)
)
if mibBuilder.loadTexts:
    agnSAlrTable.setStatus("current")
_AgnSAlrEntry_Object = MibTableRow
agnSAlrEntry = _AgnSAlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15, 1)
)
agnSAlrEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnSAlrIdx"),
)
if mibBuilder.loadTexts:
    agnSAlrEntry.setStatus("current")
_AgnSAlrIdx_Type = Integer32
_AgnSAlrIdx_Object = MibTableColumn
agnSAlrIdx = _AgnSAlrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15, 1, 1),
    _AgnSAlrIdx_Type()
)
agnSAlrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrIdx.setStatus("current")


class _AgnSAlrCodeDescription_Type(DisplayString):
    """Custom type agnSAlrCodeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgnSAlrCodeDescription_Type.__name__ = "DisplayString"
_AgnSAlrCodeDescription_Object = MibTableColumn
agnSAlrCodeDescription = _AgnSAlrCodeDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15, 1, 2),
    _AgnSAlrCodeDescription_Type()
)
agnSAlrCodeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrCodeDescription.setStatus("current")
_AgnSAlrCode_Type = Integer32
_AgnSAlrCode_Object = MibTableColumn
agnSAlrCode = _AgnSAlrCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15, 1, 3),
    _AgnSAlrCode_Type()
)
agnSAlrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrCode.setStatus("current")


class _AgnSAlrSeverity_Type(Integer32):
    """Custom type agnSAlrSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnSAlrSeverity_Type.__name__ = "Integer32"
_AgnSAlrSeverity_Object = MibTableColumn
agnSAlrSeverity = _AgnSAlrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15, 1, 4),
    _AgnSAlrSeverity_Type()
)
agnSAlrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrSeverity.setStatus("current")


class _AgnSAlrState_Type(Integer32):
    """Custom type agnSAlrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnSAlrState_Type.__name__ = "Integer32"
_AgnSAlrState_Object = MibTableColumn
agnSAlrState = _AgnSAlrState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15, 1, 5),
    _AgnSAlrState_Type()
)
agnSAlrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrState.setStatus("current")
_AgnSAlrCounter_Type = Integer32
_AgnSAlrCounter_Object = MibTableColumn
agnSAlrCounter = _AgnSAlrCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15, 1, 6),
    _AgnSAlrCounter_Type()
)
agnSAlrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrCounter.setStatus("current")


class _AgnSAlrMask_Type(Integer32):
    """Custom type agnSAlrMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnSAlrMask_Type.__name__ = "Integer32"
_AgnSAlrMask_Object = MibTableColumn
agnSAlrMask = _AgnSAlrMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15, 1, 7),
    _AgnSAlrMask_Type()
)
agnSAlrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrMask.setStatus("current")


class _AgnSAlrInvert_Type(Integer32):
    """Custom type agnSAlrInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnSAlrInvert_Type.__name__ = "Integer32"
_AgnSAlrInvert_Object = MibTableColumn
agnSAlrInvert = _AgnSAlrInvert_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 15, 1, 8),
    _AgnSAlrInvert_Type()
)
agnSAlrInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSAlrInvert.setStatus("current")


class _AgnSClearAlrCmd_Type(Integer32):
    """Custom type agnSClearAlrCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnSClearAlrCmd_Type.__name__ = "Integer32"
_AgnSClearAlrCmd_Object = MibScalar
agnSClearAlrCmd = _AgnSClearAlrCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 16),
    _AgnSClearAlrCmd_Type()
)
agnSClearAlrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSClearAlrCmd.setStatus("current")


class _AgnSClearAllAlrCmd_Type(Integer32):
    """Custom type agnSClearAllAlrCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnSClearAllAlrCmd_Type.__name__ = "Integer32"
_AgnSClearAllAlrCmd_Object = MibScalar
agnSClearAllAlrCmd = _AgnSClearAllAlrCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 17),
    _AgnSClearAllAlrCmd_Type()
)
agnSClearAllAlrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSClearAllAlrCmd.setStatus("current")


class _AgnSSanityCheckStatus_Type(Integer32):
    """Custom type agnSSanityCheckStatus based on Integer32"""
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
        *(("unknown", 1),
          ("fail", 2),
          ("warning", 3),
          ("ok", 4))
    )


_AgnSSanityCheckStatus_Type.__name__ = "Integer32"
_AgnSSanityCheckStatus_Object = MibScalar
agnSSanityCheckStatus = _AgnSSanityCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 18),
    _AgnSSanityCheckStatus_Type()
)
agnSSanityCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSSanityCheckStatus.setStatus("current")
_AgnSNoOfSanityCheckErr_Type = Integer32
_AgnSNoOfSanityCheckErr_Object = MibScalar
agnSNoOfSanityCheckErr = _AgnSNoOfSanityCheckErr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 19),
    _AgnSNoOfSanityCheckErr_Type()
)
agnSNoOfSanityCheckErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSNoOfSanityCheckErr.setStatus("current")
_AgnSErrListTable_Object = MibTable
agnSErrListTable = _AgnSErrListTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 20)
)
if mibBuilder.loadTexts:
    agnSErrListTable.setStatus("current")
_AgnSErrListEntry_Object = MibTableRow
agnSErrListEntry = _AgnSErrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 20, 1)
)
agnSErrListEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnSErrIdx"),
)
if mibBuilder.loadTexts:
    agnSErrListEntry.setStatus("current")
_AgnSErrIdx_Type = Integer32
_AgnSErrIdx_Object = MibTableColumn
agnSErrIdx = _AgnSErrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 20, 1, 1),
    _AgnSErrIdx_Type()
)
agnSErrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSErrIdx.setStatus("current")


class _AgnSErrDescription_Type(DisplayString):
    """Custom type agnSErrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgnSErrDescription_Type.__name__ = "DisplayString"
_AgnSErrDescription_Object = MibTableColumn
agnSErrDescription = _AgnSErrDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 20, 1, 2),
    _AgnSErrDescription_Type()
)
agnSErrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSErrDescription.setStatus("current")
_AgnSMaxNoOfCnfg_Type = Integer32
_AgnSMaxNoOfCnfg_Object = MibScalar
agnSMaxNoOfCnfg = _AgnSMaxNoOfCnfg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 21),
    _AgnSMaxNoOfCnfg_Type()
)
agnSMaxNoOfCnfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSMaxNoOfCnfg.setStatus("current")
_AgnSCnfgTable_Object = MibTable
agnSCnfgTable = _AgnSCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 22)
)
if mibBuilder.loadTexts:
    agnSCnfgTable.setStatus("current")
_AgnSCnfgEntry_Object = MibTableRow
agnSCnfgEntry = _AgnSCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 22, 1)
)
agnSCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnSEntryIdx"),
)
if mibBuilder.loadTexts:
    agnSCnfgEntry.setStatus("current")
_AgnSEntryIdx_Type = Integer32
_AgnSEntryIdx_Object = MibTableColumn
agnSEntryIdx = _AgnSEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 22, 1, 1),
    _AgnSEntryIdx_Type()
)
agnSEntryIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSEntryIdx.setStatus("current")


class _AgnSEntryIsValid_Type(Integer32):
    """Custom type agnSEntryIsValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_AgnSEntryIsValid_Type.__name__ = "Integer32"
_AgnSEntryIsValid_Object = MibTableColumn
agnSEntryIsValid = _AgnSEntryIsValid_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 1, 22, 1, 2),
    _AgnSEntryIsValid_Type()
)
agnSEntryIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSEntryIsValid.setStatus("current")
_CnfgAgnGen_ObjectIdentity = ObjectIdentity
cnfgAgnGen = _CnfgAgnGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2)
)


class _AgnCSanityCheckCmd_Type(Integer32):
    """Custom type agnCSanityCheckCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnCSanityCheckCmd_Type.__name__ = "Integer32"
_AgnCSanityCheckCmd_Object = MibScalar
agnCSanityCheckCmd = _AgnCSanityCheckCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 1),
    _AgnCSanityCheckCmd_Type()
)
agnCSanityCheckCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCSanityCheckCmd.setStatus("current")


class _AgnCSaveCnfgIdxCmd_Type(Integer32):
    """Custom type agnCSaveCnfgIdxCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AgnCSaveCnfgIdxCmd_Type.__name__ = "Integer32"
_AgnCSaveCnfgIdxCmd_Object = MibScalar
agnCSaveCnfgIdxCmd = _AgnCSaveCnfgIdxCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 2),
    _AgnCSaveCnfgIdxCmd_Type()
)
agnCSaveCnfgIdxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCSaveCnfgIdxCmd.setStatus("current")


class _AgnCLoadCnfgIdxCmd_Type(Integer32):
    """Custom type agnCLoadCnfgIdxCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AgnCLoadCnfgIdxCmd_Type.__name__ = "Integer32"
_AgnCLoadCnfgIdxCmd_Object = MibScalar
agnCLoadCnfgIdxCmd = _AgnCLoadCnfgIdxCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 3),
    _AgnCLoadCnfgIdxCmd_Type()
)
agnCLoadCnfgIdxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCLoadCnfgIdxCmd.setStatus("current")
_AgnCClkSrcTable_Object = MibTable
agnCClkSrcTable = _AgnCClkSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    agnCClkSrcTable.setStatus("current")
_AgnCClkSrcEntry_Object = MibTableRow
agnCClkSrcEntry = _AgnCClkSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 4, 1)
)
agnCClkSrcEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCClkCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnCClkSrcIdx"),
)
if mibBuilder.loadTexts:
    agnCClkSrcEntry.setStatus("current")


class _AgnCClkCnfgIdx_Type(Integer32):
    """Custom type agnCClkCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgnCClkCnfgIdx_Type.__name__ = "Integer32"
_AgnCClkCnfgIdx_Object = MibTableColumn
agnCClkCnfgIdx = _AgnCClkCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 4, 1, 1),
    _AgnCClkCnfgIdx_Type()
)
agnCClkCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCClkCnfgIdx.setStatus("current")


class _AgnCClkSrcIdx_Type(Integer32):
    """Custom type agnCClkSrcIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AgnCClkSrcIdx_Type.__name__ = "Integer32"
_AgnCClkSrcIdx_Object = MibTableColumn
agnCClkSrcIdx = _AgnCClkSrcIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 4, 1, 2),
    _AgnCClkSrcIdx_Type()
)
agnCClkSrcIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCClkSrcIdx.setStatus("current")


class _AgnCClkSrcMode_Type(Integer32):
    """Custom type agnCClkSrcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("rxClk", 2),
          ("adaptive", 3))
    )


_AgnCClkSrcMode_Type.__name__ = "Integer32"
_AgnCClkSrcMode_Object = MibTableColumn
agnCClkSrcMode = _AgnCClkSrcMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 4, 1, 3),
    _AgnCClkSrcMode_Type()
)
agnCClkSrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCClkSrcMode.setStatus("current")


class _AgnCClkSrcSlt_Type(Integer32):
    """Custom type agnCClkSrcSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_AgnCClkSrcSlt_Type.__name__ = "Integer32"
_AgnCClkSrcSlt_Object = MibTableColumn
agnCClkSrcSlt = _AgnCClkSrcSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 4, 1, 4),
    _AgnCClkSrcSlt_Type()
)
agnCClkSrcSlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCClkSrcSlt.setStatus("current")
_AgnCClkSrcPrt_Type = Integer32
_AgnCClkSrcPrt_Object = MibTableColumn
agnCClkSrcPrt = _AgnCClkSrcPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 4, 1, 5),
    _AgnCClkSrcPrt_Type()
)
agnCClkSrcPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCClkSrcPrt.setStatus("current")


class _AgnCDeleteCnfgIdxCmd_Type(Integer32):
    """Custom type agnCDeleteCnfgIdxCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AgnCDeleteCnfgIdxCmd_Type.__name__ = "Integer32"
_AgnCDeleteCnfgIdxCmd_Object = MibScalar
agnCDeleteCnfgIdxCmd = _AgnCDeleteCnfgIdxCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 5),
    _AgnCDeleteCnfgIdxCmd_Type()
)
agnCDeleteCnfgIdxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCDeleteCnfgIdxCmd.setStatus("current")


class _AgnCDefaultCnfgIdxCmd_Type(Integer32):
    """Custom type agnCDefaultCnfgIdxCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AgnCDefaultCnfgIdxCmd_Type.__name__ = "Integer32"
_AgnCDefaultCnfgIdxCmd_Object = MibScalar
agnCDefaultCnfgIdxCmd = _AgnCDefaultCnfgIdxCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 6),
    _AgnCDefaultCnfgIdxCmd_Type()
)
agnCDefaultCnfgIdxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCDefaultCnfgIdxCmd.setStatus("current")
_AgnCnfgDataTable_Object = MibTable
agnCnfgDataTable = _AgnCnfgDataTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    agnCnfgDataTable.setStatus("current")
_AgnCnfgDataEntry_Object = MibTableRow
agnCnfgDataEntry = _AgnCnfgDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 7, 1)
)
agnCnfgDataEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCnfgIdx"),
)
if mibBuilder.loadTexts:
    agnCnfgDataEntry.setStatus("current")


class _AgnCnfgIdx_Type(Integer32):
    """Custom type agnCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgnCnfgIdx_Type.__name__ = "Integer32"
_AgnCnfgIdx_Object = MibTableColumn
agnCnfgIdx = _AgnCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 7, 1, 1),
    _AgnCnfgIdx_Type()
)
agnCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCnfgIdx.setStatus("current")


class _AgnCnfgDesc_Type(DisplayString):
    """Custom type agnCnfgDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AgnCnfgDesc_Type.__name__ = "DisplayString"
_AgnCnfgDesc_Object = MibTableColumn
agnCnfgDesc = _AgnCnfgDesc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 7, 1, 2),
    _AgnCnfgDesc_Type()
)
agnCnfgDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgDesc.setStatus("current")


class _AgnCnfgUpdDate_Type(DisplayString):
    """Custom type agnCnfgUpdDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgnCnfgUpdDate_Type.__name__ = "DisplayString"
_AgnCnfgUpdDate_Object = MibTableColumn
agnCnfgUpdDate = _AgnCnfgUpdDate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 7, 1, 3),
    _AgnCnfgUpdDate_Type()
)
agnCnfgUpdDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCnfgUpdDate.setStatus("current")


class _AgnCnfgUpdTime_Type(DisplayString):
    """Custom type agnCnfgUpdTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgnCnfgUpdTime_Type.__name__ = "DisplayString"
_AgnCnfgUpdTime_Object = MibTableColumn
agnCnfgUpdTime = _AgnCnfgUpdTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 7, 1, 4),
    _AgnCnfgUpdTime_Type()
)
agnCnfgUpdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCnfgUpdTime.setStatus("current")
_AgnCnfgUpdMnger_Type = IpAddress
_AgnCnfgUpdMnger_Object = MibTableColumn
agnCnfgUpdMnger = _AgnCnfgUpdMnger_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 7, 1, 5),
    _AgnCnfgUpdMnger_Type()
)
agnCnfgUpdMnger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCnfgUpdMnger.setStatus("current")
_AgnCnfgAlarm_ObjectIdentity = ObjectIdentity
agnCnfgAlarm = _AgnCnfgAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8)
)


class _AgnCnfgAlrFilterWindow_Type(Integer32):
    """Custom type agnCnfgAlrFilterWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgnCnfgAlrFilterWindow_Type.__name__ = "Integer32"
_AgnCnfgAlrFilterWindow_Object = MibScalar
agnCnfgAlrFilterWindow = _AgnCnfgAlrFilterWindow_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 1),
    _AgnCnfgAlrFilterWindow_Type()
)
agnCnfgAlrFilterWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgAlrFilterWindow.setStatus("current")
_AgnCnfgAlrTable_Object = MibTable
agnCnfgAlrTable = _AgnCnfgAlrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2)
)
if mibBuilder.loadTexts:
    agnCnfgAlrTable.setStatus("current")
_AgnCnfgAlrEntry_Object = MibTableRow
agnCnfgAlrEntry = _AgnCnfgAlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1)
)
agnCnfgAlrEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCnfgAlrCode"),
    (0, "RAD-Mpmx-MIB", "agnCnfgAlrSlot"),
    (0, "RAD-Mpmx-MIB", "agnCnfgAlrPort"),
)
if mibBuilder.loadTexts:
    agnCnfgAlrEntry.setStatus("current")
_AgnCnfgAlrCode_Type = Integer32
_AgnCnfgAlrCode_Object = MibTableColumn
agnCnfgAlrCode = _AgnCnfgAlrCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1, 1),
    _AgnCnfgAlrCode_Type()
)
agnCnfgAlrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCnfgAlrCode.setStatus("current")


class _AgnCnfgAlrSlot_Type(Integer32):
    """Custom type agnCnfgAlrSlot based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              200,
              255)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("all", 200),
          ("notApplicable", 255))
    )


_AgnCnfgAlrSlot_Type.__name__ = "Integer32"
_AgnCnfgAlrSlot_Object = MibTableColumn
agnCnfgAlrSlot = _AgnCnfgAlrSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1, 2),
    _AgnCnfgAlrSlot_Type()
)
agnCnfgAlrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCnfgAlrSlot.setStatus("current")
_AgnCnfgAlrPort_Type = Integer32
_AgnCnfgAlrPort_Object = MibTableColumn
agnCnfgAlrPort = _AgnCnfgAlrPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1, 3),
    _AgnCnfgAlrPort_Type()
)
agnCnfgAlrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCnfgAlrPort.setStatus("current")


class _AgnCnfgAlrMask_Type(Integer32):
    """Custom type agnCnfgAlrMask based on Integer32"""
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
        *(("no", 1),
          ("noAndSave", 2),
          ("yes", 3),
          ("yesAndSave", 4))
    )


_AgnCnfgAlrMask_Type.__name__ = "Integer32"
_AgnCnfgAlrMask_Object = MibTableColumn
agnCnfgAlrMask = _AgnCnfgAlrMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1, 4),
    _AgnCnfgAlrMask_Type()
)
agnCnfgAlrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgAlrMask.setStatus("current")


class _AgnCnfgAlrInvert_Type(Integer32):
    """Custom type agnCnfgAlrInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_AgnCnfgAlrInvert_Type.__name__ = "Integer32"
_AgnCnfgAlrInvert_Object = MibTableColumn
agnCnfgAlrInvert = _AgnCnfgAlrInvert_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1, 5),
    _AgnCnfgAlrInvert_Type()
)
agnCnfgAlrInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgAlrInvert.setStatus("current")


class _AgnCnfgAlrFilter_Type(Integer32):
    """Custom type agnCnfgAlrFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_AgnCnfgAlrFilter_Type.__name__ = "Integer32"
_AgnCnfgAlrFilter_Object = MibTableColumn
agnCnfgAlrFilter = _AgnCnfgAlrFilter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1, 6),
    _AgnCnfgAlrFilter_Type()
)
agnCnfgAlrFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgAlrFilter.setStatus("current")
_AgnCnfgAlrFilterSet_Type = Integer32
_AgnCnfgAlrFilterSet_Object = MibTableColumn
agnCnfgAlrFilterSet = _AgnCnfgAlrFilterSet_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1, 7),
    _AgnCnfgAlrFilterSet_Type()
)
agnCnfgAlrFilterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgAlrFilterSet.setStatus("current")
_AgnCnfgAlrFilterReset_Type = Integer32
_AgnCnfgAlrFilterReset_Object = MibTableColumn
agnCnfgAlrFilterReset = _AgnCnfgAlrFilterReset_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1, 8),
    _AgnCnfgAlrFilterReset_Type()
)
agnCnfgAlrFilterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgAlrFilterReset.setStatus("current")


class _AgnCnfgAlrSeverity_Type(Integer32):
    """Custom type agnCnfgAlrSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnCnfgAlrSeverity_Type.__name__ = "Integer32"
_AgnCnfgAlrSeverity_Object = MibTableColumn
agnCnfgAlrSeverity = _AgnCnfgAlrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 2, 1, 9),
    _AgnCnfgAlrSeverity_Type()
)
agnCnfgAlrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgAlrSeverity.setStatus("current")
_AgnCnfgAlrReportTable_Object = MibTable
agnCnfgAlrReportTable = _AgnCnfgAlrReportTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 3)
)
if mibBuilder.loadTexts:
    agnCnfgAlrReportTable.setStatus("current")
_AgnCnfgAlrReportEntry_Object = MibTableRow
agnCnfgAlrReportEntry = _AgnCnfgAlrReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 3, 1)
)
agnCnfgAlrReportEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCnfgAlrReportType"),
)
if mibBuilder.loadTexts:
    agnCnfgAlrReportEntry.setStatus("current")


class _AgnCnfgAlrReportType_Type(Integer32):
    """Custom type agnCnfgAlrReportType based on Integer32"""
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
        *(("trap", 1),
          ("buffer", 2),
          ("relay", 3),
          ("alrLedOn", 4),
          ("alrLedBlink", 5),
          ("relay2", 6))
    )


_AgnCnfgAlrReportType_Type.__name__ = "Integer32"
_AgnCnfgAlrReportType_Object = MibTableColumn
agnCnfgAlrReportType = _AgnCnfgAlrReportType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 3, 1, 1),
    _AgnCnfgAlrReportType_Type()
)
agnCnfgAlrReportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCnfgAlrReportType.setStatus("current")


class _AgnCnfgAlrStartReportOn_Type(Integer32):
    """Custom type agnCnfgAlrStartReportOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noReport", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnCnfgAlrStartReportOn_Type.__name__ = "Integer32"
_AgnCnfgAlrStartReportOn_Object = MibTableColumn
agnCnfgAlrStartReportOn = _AgnCnfgAlrStartReportOn_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 3, 1, 2),
    _AgnCnfgAlrStartReportOn_Type()
)
agnCnfgAlrStartReportOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgAlrStartReportOn.setStatus("current")


class _AgnCnfgAlrStartReportOff_Type(Integer32):
    """Custom type agnCnfgAlrStartReportOff based on Integer32"""
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
        *(("notApplicable", 1),
          ("noReport", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnCnfgAlrStartReportOff_Type.__name__ = "Integer32"
_AgnCnfgAlrStartReportOff_Object = MibTableColumn
agnCnfgAlrStartReportOff = _AgnCnfgAlrStartReportOff_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 8, 3, 1, 3),
    _AgnCnfgAlrStartReportOff_Type()
)
agnCnfgAlrStartReportOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCnfgAlrStartReportOff.setStatus("current")


class _AgnCOffsetCmd_Type(Integer32):
    """Custom type agnCOffsetCmd based on Integer32"""
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
          ("normal", 2),
          ("u1", 3))
    )


_AgnCOffsetCmd_Type.__name__ = "Integer32"
_AgnCOffsetCmd_Object = MibScalar
agnCOffsetCmd = _AgnCOffsetCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 9),
    _AgnCOffsetCmd_Type()
)
agnCOffsetCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCOffsetCmd.setStatus("current")
_AgnCT1E1RingTable_Object = MibTable
agnCT1E1RingTable = _AgnCT1E1RingTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    agnCT1E1RingTable.setStatus("current")
_AgnCT1E1RingEntry_Object = MibTableRow
agnCT1E1RingEntry = _AgnCT1E1RingEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1)
)
agnCT1E1RingEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCT1E1RingCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnCT1E1RingPrimeSlot"),
    (0, "RAD-Mpmx-MIB", "agnCT1E1RingPrimePort"),
)
if mibBuilder.loadTexts:
    agnCT1E1RingEntry.setStatus("current")
_AgnCT1E1RingCnfgIdx_Type = Integer32
_AgnCT1E1RingCnfgIdx_Object = MibTableColumn
agnCT1E1RingCnfgIdx = _AgnCT1E1RingCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1, 1),
    _AgnCT1E1RingCnfgIdx_Type()
)
agnCT1E1RingCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCT1E1RingCnfgIdx.setStatus("current")


class _AgnCT1E1RingPrimeSlot_Type(Integer32):
    """Custom type agnCT1E1RingPrimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_AgnCT1E1RingPrimeSlot_Type.__name__ = "Integer32"
_AgnCT1E1RingPrimeSlot_Object = MibTableColumn
agnCT1E1RingPrimeSlot = _AgnCT1E1RingPrimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1, 2),
    _AgnCT1E1RingPrimeSlot_Type()
)
agnCT1E1RingPrimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCT1E1RingPrimeSlot.setStatus("current")
_AgnCT1E1RingPrimePort_Type = Integer32
_AgnCT1E1RingPrimePort_Object = MibTableColumn
agnCT1E1RingPrimePort = _AgnCT1E1RingPrimePort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1, 3),
    _AgnCT1E1RingPrimePort_Type()
)
agnCT1E1RingPrimePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCT1E1RingPrimePort.setStatus("current")


class _AgnCT1E1RingSecSlot_Type(Integer32):
    """Custom type agnCT1E1RingSecSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_AgnCT1E1RingSecSlot_Type.__name__ = "Integer32"
_AgnCT1E1RingSecSlot_Object = MibTableColumn
agnCT1E1RingSecSlot = _AgnCT1E1RingSecSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1, 4),
    _AgnCT1E1RingSecSlot_Type()
)
agnCT1E1RingSecSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnCT1E1RingSecSlot.setStatus("current")
_AgnCT1E1RingSecPort_Type = Integer32
_AgnCT1E1RingSecPort_Object = MibTableColumn
agnCT1E1RingSecPort = _AgnCT1E1RingSecPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1, 5),
    _AgnCT1E1RingSecPort_Type()
)
agnCT1E1RingSecPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnCT1E1RingSecPort.setStatus("current")
_AgnCT1E1RingRecTime_Type = Integer32
_AgnCT1E1RingRecTime_Object = MibTableColumn
agnCT1E1RingRecTime = _AgnCT1E1RingRecTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1, 6),
    _AgnCT1E1RingRecTime_Type()
)
agnCT1E1RingRecTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnCT1E1RingRecTime.setStatus("current")
_AgnCT1E1RingRowStatus_Type = RowStatus
_AgnCT1E1RingRowStatus_Object = MibTableColumn
agnCT1E1RingRowStatus = _AgnCT1E1RingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1, 7),
    _AgnCT1E1RingRowStatus_Type()
)
agnCT1E1RingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnCT1E1RingRowStatus.setStatus("current")
_AgnCT1E1RingWTR_Type = Unsigned32
_AgnCT1E1RingWTR_Object = MibTableColumn
agnCT1E1RingWTR = _AgnCT1E1RingWTR_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1, 8),
    _AgnCT1E1RingWTR_Type()
)
agnCT1E1RingWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnCT1E1RingWTR.setStatus("current")


class _AgnCT1E1RingDualFailDetection_Type(Integer32):
    """Custom type agnCT1E1RingDualFailDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_AgnCT1E1RingDualFailDetection_Type.__name__ = "Integer32"
_AgnCT1E1RingDualFailDetection_Object = MibTableColumn
agnCT1E1RingDualFailDetection = _AgnCT1E1RingDualFailDetection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 10, 1, 9),
    _AgnCT1E1RingDualFailDetection_Type()
)
agnCT1E1RingDualFailDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnCT1E1RingDualFailDetection.setStatus("current")


class _AgnCMainExitPort_Type(Integer32):
    """Custom type agnCMainExitPort based on Integer32"""
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
          ("eth", 2),
          ("e1T1SerialLink", 3))
    )


_AgnCMainExitPort_Type.__name__ = "Integer32"
_AgnCMainExitPort_Object = MibScalar
agnCMainExitPort = _AgnCMainExitPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 11),
    _AgnCMainExitPort_Type()
)
agnCMainExitPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCMainExitPort.setStatus("current")
_AgnCBuMlTable_Object = MibTable
agnCBuMlTable = _AgnCBuMlTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12)
)
if mibBuilder.loadTexts:
    agnCBuMlTable.setStatus("current")
_AgnCBuMlEntry_Object = MibTableRow
agnCBuMlEntry = _AgnCBuMlEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1)
)
agnCBuMlEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCBuMlCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnCBuMlRole"),
)
if mibBuilder.loadTexts:
    agnCBuMlEntry.setStatus("current")
_AgnCBuMlCnfgIdx_Type = Integer32
_AgnCBuMlCnfgIdx_Object = MibTableColumn
agnCBuMlCnfgIdx = _AgnCBuMlCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1, 1),
    _AgnCBuMlCnfgIdx_Type()
)
agnCBuMlCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agnCBuMlCnfgIdx.setStatus("current")


class _AgnCBuMlRole_Type(Integer32):
    """Custom type agnCBuMlRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("primary", 2),
          ("secondary", 3),
          ("third", 4),
          ("fourth", 5))
    )


_AgnCBuMlRole_Type.__name__ = "Integer32"
_AgnCBuMlRole_Object = MibTableColumn
agnCBuMlRole = _AgnCBuMlRole_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1, 2),
    _AgnCBuMlRole_Type()
)
agnCBuMlRole.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agnCBuMlRole.setStatus("current")


class _AgnCBuMlType_Type(Integer32):
    """Custom type agnCBuMlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("e1T1a", 3),
          ("e1T1b", 4),
          ("eth", 5),
          ("ethNetUser", 6))
    )


_AgnCBuMlType_Type.__name__ = "Integer32"
_AgnCBuMlType_Object = MibTableColumn
agnCBuMlType = _AgnCBuMlType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1, 3),
    _AgnCBuMlType_Type()
)
agnCBuMlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCBuMlType.setStatus("current")
_AgnCBuMlDefaultGateway_Type = IpAddress
_AgnCBuMlDefaultGateway_Object = MibTableColumn
agnCBuMlDefaultGateway = _AgnCBuMlDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1, 4),
    _AgnCBuMlDefaultGateway_Type()
)
agnCBuMlDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCBuMlDefaultGateway.setStatus("current")
_AgnCBuMlSubnetMask_Type = IpAddress
_AgnCBuMlSubnetMask_Object = MibTableColumn
agnCBuMlSubnetMask = _AgnCBuMlSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1, 5),
    _AgnCBuMlSubnetMask_Type()
)
agnCBuMlSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCBuMlSubnetMask.setStatus("current")
_AgnCBuMlOamFrequency_Type = Integer32
_AgnCBuMlOamFrequency_Object = MibTableColumn
agnCBuMlOamFrequency = _AgnCBuMlOamFrequency_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1, 6),
    _AgnCBuMlOamFrequency_Type()
)
agnCBuMlOamFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCBuMlOamFrequency.setStatus("current")
_AgnCBuMlOamTimeoutCycles_Type = Integer32
_AgnCBuMlOamTimeoutCycles_Object = MibTableColumn
agnCBuMlOamTimeoutCycles = _AgnCBuMlOamTimeoutCycles_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1, 7),
    _AgnCBuMlOamTimeoutCycles_Type()
)
agnCBuMlOamTimeoutCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCBuMlOamTimeoutCycles.setStatus("current")
_AgnCBuMlWaitToRestore_Type = Unsigned32
_AgnCBuMlWaitToRestore_Object = MibTableColumn
agnCBuMlWaitToRestore = _AgnCBuMlWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1, 8),
    _AgnCBuMlWaitToRestore_Type()
)
agnCBuMlWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCBuMlWaitToRestore.setStatus("current")
_AgnCBuMlBfdSessionNum_Type = Unsigned32
_AgnCBuMlBfdSessionNum_Object = MibTableColumn
agnCBuMlBfdSessionNum = _AgnCBuMlBfdSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 12, 1, 9),
    _AgnCBuMlBfdSessionNum_Type()
)
agnCBuMlBfdSessionNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCBuMlBfdSessionNum.setStatus("current")
_AgnCQ50Table_Object = MibTable
agnCQ50Table = _AgnCQ50Table_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 13)
)
if mibBuilder.loadTexts:
    agnCQ50Table.setStatus("current")
_AgnCQ50Entry_Object = MibTableRow
agnCQ50Entry = _AgnCQ50Entry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 13, 1)
)
agnCQ50Entry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCQ50CnfgIdx"),
)
if mibBuilder.loadTexts:
    agnCQ50Entry.setStatus("current")
_AgnCQ50CnfgIdx_Type = Integer32
_AgnCQ50CnfgIdx_Object = MibTableColumn
agnCQ50CnfgIdx = _AgnCQ50CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 13, 1, 1),
    _AgnCQ50CnfgIdx_Type()
)
agnCQ50CnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agnCQ50CnfgIdx.setStatus("current")
_AgnCQ50StopCallsThresh_Type = Integer32
_AgnCQ50StopCallsThresh_Object = MibTableColumn
agnCQ50StopCallsThresh = _AgnCQ50StopCallsThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 13, 1, 2),
    _AgnCQ50StopCallsThresh_Type()
)
agnCQ50StopCallsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCQ50StopCallsThresh.setStatus("current")
_AgnCQ50DiscardPktThresh_Type = Integer32
_AgnCQ50DiscardPktThresh_Object = MibTableColumn
agnCQ50DiscardPktThresh = _AgnCQ50DiscardPktThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 13, 1, 3),
    _AgnCQ50DiscardPktThresh_Type()
)
agnCQ50DiscardPktThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCQ50DiscardPktThresh.setStatus("current")
_AgnCQ50BlockNewModemVbdCallsThresh_Type = Integer32
_AgnCQ50BlockNewModemVbdCallsThresh_Object = MibTableColumn
agnCQ50BlockNewModemVbdCallsThresh = _AgnCQ50BlockNewModemVbdCallsThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 13, 1, 4),
    _AgnCQ50BlockNewModemVbdCallsThresh_Type()
)
agnCQ50BlockNewModemVbdCallsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCQ50BlockNewModemVbdCallsThresh.setStatus("current")
_AgnCQ50BlockNewModemRelayCallsThresh_Type = Integer32
_AgnCQ50BlockNewModemRelayCallsThresh_Object = MibTableColumn
agnCQ50BlockNewModemRelayCallsThresh = _AgnCQ50BlockNewModemRelayCallsThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 2, 13, 1, 5),
    _AgnCQ50BlockNewModemRelayCallsThresh_Type()
)
agnCQ50BlockNewModemRelayCallsThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCQ50BlockNewModemRelayCallsThresh.setStatus("current")
_CmprAgnGen_ObjectIdentity = ObjectIdentity
cmprAgnGen = _CmprAgnGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3)
)
_AgnCmprTable_Object = MibTable
agnCmprTable = _AgnCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    agnCmprTable.setStatus("current")
_AgnCmprEntry_Object = MibTableRow
agnCmprEntry = _AgnCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 1, 1)
)
agnCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCmprTypIdx"),
    (0, "RAD-Mpmx-MIB", "agnCmprCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnCmprVersion"),
)
if mibBuilder.loadTexts:
    agnCmprEntry.setStatus("current")
_AgnCmprTypIdx_Type = Integer32
_AgnCmprTypIdx_Object = MibTableColumn
agnCmprTypIdx = _AgnCmprTypIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 1, 1, 1),
    _AgnCmprTypIdx_Type()
)
agnCmprTypIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCmprTypIdx.setStatus("current")
_AgnCmprCnfgIdx_Type = Integer32
_AgnCmprCnfgIdx_Object = MibTableColumn
agnCmprCnfgIdx = _AgnCmprCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 1, 1, 2),
    _AgnCmprCnfgIdx_Type()
)
agnCmprCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCmprCnfgIdx.setStatus("current")
_AgnCmprVersion_Type = Integer32
_AgnCmprVersion_Object = MibTableColumn
agnCmprVersion = _AgnCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 1, 1, 3),
    _AgnCmprVersion_Type()
)
agnCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCmprVersion.setStatus("current")
_AgnCmprObj_Type = OctetString
_AgnCmprObj_Object = MibTableColumn
agnCmprObj = _AgnCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 1, 1, 4),
    _AgnCmprObj_Type()
)
agnCmprObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCmprObj.setStatus("current")
_AgnDlciCmprTable_Object = MibTable
agnDlciCmprTable = _AgnDlciCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    agnDlciCmprTable.setStatus("current")
_AgnDlciCmprEntry_Object = MibTableRow
agnDlciCmprEntry = _AgnDlciCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 2, 1)
)
agnDlciCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnDlciCmprCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnDlciCmprVersion"),
    (0, "RAD-Mpmx-MIB", "agnDlciCmprDlciIdx"),
)
if mibBuilder.loadTexts:
    agnDlciCmprEntry.setStatus("current")
_AgnDlciCmprCnfgIdx_Type = Integer32
_AgnDlciCmprCnfgIdx_Object = MibTableColumn
agnDlciCmprCnfgIdx = _AgnDlciCmprCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 2, 1, 1),
    _AgnDlciCmprCnfgIdx_Type()
)
agnDlciCmprCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciCmprCnfgIdx.setStatus("current")
_AgnDlciCmprVersion_Type = Integer32
_AgnDlciCmprVersion_Object = MibTableColumn
agnDlciCmprVersion = _AgnDlciCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 2, 1, 2),
    _AgnDlciCmprVersion_Type()
)
agnDlciCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciCmprVersion.setStatus("current")
_AgnDlciCmprDlciIdx_Type = Integer32
_AgnDlciCmprDlciIdx_Object = MibTableColumn
agnDlciCmprDlciIdx = _AgnDlciCmprDlciIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 2, 1, 3),
    _AgnDlciCmprDlciIdx_Type()
)
agnDlciCmprDlciIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciCmprDlciIdx.setStatus("current")
_AgnDlciCmprObj_Type = OctetString
_AgnDlciCmprObj_Object = MibTableColumn
agnDlciCmprObj = _AgnDlciCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 2, 1, 4),
    _AgnDlciCmprObj_Type()
)
agnDlciCmprObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnDlciCmprObj.setStatus("current")
_AgnAlarmsCmprTable_Object = MibTable
agnAlarmsCmprTable = _AgnAlarmsCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    agnAlarmsCmprTable.setStatus("current")
_AgnAlarmsCmprEntry_Object = MibTableRow
agnAlarmsCmprEntry = _AgnAlarmsCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 3, 1)
)
agnAlarmsCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnAlarmsCmprVersion"),
    (0, "RAD-Mpmx-MIB", "agnAlarmsCmprAlarmIdx"),
)
if mibBuilder.loadTexts:
    agnAlarmsCmprEntry.setStatus("current")
_AgnAlarmsCmprVersion_Type = Integer32
_AgnAlarmsCmprVersion_Object = MibTableColumn
agnAlarmsCmprVersion = _AgnAlarmsCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 3, 1, 1),
    _AgnAlarmsCmprVersion_Type()
)
agnAlarmsCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnAlarmsCmprVersion.setStatus("current")
_AgnAlarmsCmprAlarmIdx_Type = Integer32
_AgnAlarmsCmprAlarmIdx_Object = MibTableColumn
agnAlarmsCmprAlarmIdx = _AgnAlarmsCmprAlarmIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 3, 1, 2),
    _AgnAlarmsCmprAlarmIdx_Type()
)
agnAlarmsCmprAlarmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnAlarmsCmprAlarmIdx.setStatus("current")
_AgnAlarmsCmprObj_Type = OctetString
_AgnAlarmsCmprObj_Object = MibTableColumn
agnAlarmsCmprObj = _AgnAlarmsCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 3, 1, 3),
    _AgnAlarmsCmprObj_Type()
)
agnAlarmsCmprObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnAlarmsCmprObj.setStatus("current")
_AgnAlrBufCmprTable_Object = MibTable
agnAlrBufCmprTable = _AgnAlrBufCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    agnAlrBufCmprTable.setStatus("current")
_AgnAlrBufCmprEntry_Object = MibTableRow
agnAlrBufCmprEntry = _AgnAlrBufCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 4, 1)
)
agnAlrBufCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnAlrBufCmprVersion"),
    (0, "RAD-Mpmx-MIB", "agnAlrBufCmprAlarmIdx"),
)
if mibBuilder.loadTexts:
    agnAlrBufCmprEntry.setStatus("current")
_AgnAlrBufCmprVersion_Type = Integer32
_AgnAlrBufCmprVersion_Object = MibTableColumn
agnAlrBufCmprVersion = _AgnAlrBufCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 4, 1, 1),
    _AgnAlrBufCmprVersion_Type()
)
agnAlrBufCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnAlrBufCmprVersion.setStatus("current")
_AgnAlrBufCmprAlarmIdx_Type = Integer32
_AgnAlrBufCmprAlarmIdx_Object = MibTableColumn
agnAlrBufCmprAlarmIdx = _AgnAlrBufCmprAlarmIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 4, 1, 2),
    _AgnAlrBufCmprAlarmIdx_Type()
)
agnAlrBufCmprAlarmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnAlrBufCmprAlarmIdx.setStatus("current")
_AgnAlrBufCmprObj_Type = OctetString
_AgnAlrBufCmprObj_Object = MibTableColumn
agnAlrBufCmprObj = _AgnAlrBufCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 4, 1, 3),
    _AgnAlrBufCmprObj_Type()
)
agnAlrBufCmprObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnAlrBufCmprObj.setStatus("current")
_AgnSCmprErrListTable_Object = MibTable
agnSCmprErrListTable = _AgnSCmprErrListTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    agnSCmprErrListTable.setStatus("current")
_AgnSCmprErrListEntry_Object = MibTableRow
agnSCmprErrListEntry = _AgnSCmprErrListEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 5, 1)
)
agnSCmprErrListEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnSCmprErrVersion"),
    (0, "RAD-Mpmx-MIB", "agnSCmprErrIdx"),
)
if mibBuilder.loadTexts:
    agnSCmprErrListEntry.setStatus("current")
_AgnSCmprErrVersion_Type = Integer32
_AgnSCmprErrVersion_Object = MibTableColumn
agnSCmprErrVersion = _AgnSCmprErrVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 5, 1, 1),
    _AgnSCmprErrVersion_Type()
)
agnSCmprErrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSCmprErrVersion.setStatus("current")
_AgnSCmprErrIdx_Type = Integer32
_AgnSCmprErrIdx_Object = MibTableColumn
agnSCmprErrIdx = _AgnSCmprErrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 5, 1, 2),
    _AgnSCmprErrIdx_Type()
)
agnSCmprErrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSCmprErrIdx.setStatus("current")
_AgnSCmprErrObj_Type = OctetString
_AgnSCmprErrObj_Object = MibTableColumn
agnSCmprErrObj = _AgnSCmprErrObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 5, 1, 3),
    _AgnSCmprErrObj_Type()
)
agnSCmprErrObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSCmprErrObj.setStatus("current")
_AgnTsCmprTable_Object = MibTable
agnTsCmprTable = _AgnTsCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    agnTsCmprTable.setStatus("current")
_AgnTsCmprEntry_Object = MibTableRow
agnTsCmprEntry = _AgnTsCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 6, 1)
)
agnTsCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnTsCmprVerIdx"),
    (0, "RAD-Mpmx-MIB", "agnTsCmprCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnTsCmprSlotIdx"),
    (0, "RAD-Mpmx-MIB", "agnTsCmprPortIdx"),
    (0, "RAD-Mpmx-MIB", "agnTsCmprPduIdx"),
)
if mibBuilder.loadTexts:
    agnTsCmprEntry.setStatus("current")
_AgnTsCmprVerIdx_Type = Integer32
_AgnTsCmprVerIdx_Object = MibTableColumn
agnTsCmprVerIdx = _AgnTsCmprVerIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 6, 1, 1),
    _AgnTsCmprVerIdx_Type()
)
agnTsCmprVerIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnTsCmprVerIdx.setStatus("current")
_AgnTsCmprCnfgIdx_Type = Integer32
_AgnTsCmprCnfgIdx_Object = MibTableColumn
agnTsCmprCnfgIdx = _AgnTsCmprCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 6, 1, 2),
    _AgnTsCmprCnfgIdx_Type()
)
agnTsCmprCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnTsCmprCnfgIdx.setStatus("current")
_AgnTsCmprSlotIdx_Type = Integer32
_AgnTsCmprSlotIdx_Object = MibTableColumn
agnTsCmprSlotIdx = _AgnTsCmprSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 6, 1, 3),
    _AgnTsCmprSlotIdx_Type()
)
agnTsCmprSlotIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnTsCmprSlotIdx.setStatus("current")
_AgnTsCmprPortIdx_Type = Integer32
_AgnTsCmprPortIdx_Object = MibTableColumn
agnTsCmprPortIdx = _AgnTsCmprPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 6, 1, 4),
    _AgnTsCmprPortIdx_Type()
)
agnTsCmprPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnTsCmprPortIdx.setStatus("current")
_AgnTsCmprPduIdx_Type = Integer32
_AgnTsCmprPduIdx_Object = MibTableColumn
agnTsCmprPduIdx = _AgnTsCmprPduIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 6, 1, 5),
    _AgnTsCmprPduIdx_Type()
)
agnTsCmprPduIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnTsCmprPduIdx.setStatus("current")
_AgnTsCmprData_Type = OctetString
_AgnTsCmprData_Object = MibTableColumn
agnTsCmprData = _AgnTsCmprData_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 6, 1, 6),
    _AgnTsCmprData_Type()
)
agnTsCmprData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnTsCmprData.setStatus("current")
_AgnXCmprTable_Object = MibTable
agnXCmprTable = _AgnXCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    agnXCmprTable.setStatus("current")
_AgnXCmprEntry_Object = MibTableRow
agnXCmprEntry = _AgnXCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7, 1)
)
agnXCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnXCmprTypIdx"),
    (0, "RAD-Mpmx-MIB", "agnXCmprVersion"),
    (0, "RAD-Mpmx-MIB", "agnXCmprIdx3"),
    (0, "RAD-Mpmx-MIB", "agnXCmprIdx4"),
    (0, "RAD-Mpmx-MIB", "agnXCmprIdx5"),
    (0, "RAD-Mpmx-MIB", "agnXCmprIdx6"),
    (0, "RAD-Mpmx-MIB", "agnXCmprIdx7"),
)
if mibBuilder.loadTexts:
    agnXCmprEntry.setStatus("current")
_AgnXCmprTypIdx_Type = Integer32
_AgnXCmprTypIdx_Object = MibTableColumn
agnXCmprTypIdx = _AgnXCmprTypIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7, 1, 1),
    _AgnXCmprTypIdx_Type()
)
agnXCmprTypIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnXCmprTypIdx.setStatus("current")
_AgnXCmprVersion_Type = Integer32
_AgnXCmprVersion_Object = MibTableColumn
agnXCmprVersion = _AgnXCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7, 1, 2),
    _AgnXCmprVersion_Type()
)
agnXCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnXCmprVersion.setStatus("current")
_AgnXCmprIdx3_Type = Integer32
_AgnXCmprIdx3_Object = MibTableColumn
agnXCmprIdx3 = _AgnXCmprIdx3_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7, 1, 3),
    _AgnXCmprIdx3_Type()
)
agnXCmprIdx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnXCmprIdx3.setStatus("current")
_AgnXCmprIdx4_Type = Integer32
_AgnXCmprIdx4_Object = MibTableColumn
agnXCmprIdx4 = _AgnXCmprIdx4_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7, 1, 4),
    _AgnXCmprIdx4_Type()
)
agnXCmprIdx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnXCmprIdx4.setStatus("current")
_AgnXCmprIdx5_Type = Integer32
_AgnXCmprIdx5_Object = MibTableColumn
agnXCmprIdx5 = _AgnXCmprIdx5_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7, 1, 5),
    _AgnXCmprIdx5_Type()
)
agnXCmprIdx5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnXCmprIdx5.setStatus("current")
_AgnXCmprIdx6_Type = Integer32
_AgnXCmprIdx6_Object = MibTableColumn
agnXCmprIdx6 = _AgnXCmprIdx6_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7, 1, 6),
    _AgnXCmprIdx6_Type()
)
agnXCmprIdx6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnXCmprIdx6.setStatus("current")
_AgnXCmprIdx7_Type = Integer32
_AgnXCmprIdx7_Object = MibTableColumn
agnXCmprIdx7 = _AgnXCmprIdx7_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7, 1, 7),
    _AgnXCmprIdx7_Type()
)
agnXCmprIdx7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnXCmprIdx7.setStatus("current")
_AgnXCmprObj_Type = OctetString
_AgnXCmprObj_Object = MibTableColumn
agnXCmprObj = _AgnXCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 3, 7, 1, 8),
    _AgnXCmprObj_Type()
)
agnXCmprObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnXCmprObj.setStatus("current")
_AlrBuffGen_ObjectIdentity = ObjectIdentity
alrBuffGen = _AlrBuffGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4)
)
_AlrBufTable_Object = MibTable
alrBufTable = _AlrBufTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    alrBufTable.setStatus("current")
_AlrBufEntry_Object = MibTableRow
alrBufEntry = _AlrBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 1, 1)
)
alrBufEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "alrBufIdx"),
)
if mibBuilder.loadTexts:
    alrBufEntry.setStatus("current")
_AlrBufIdx_Type = Integer32
_AlrBufIdx_Object = MibTableColumn
alrBufIdx = _AlrBufIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 1, 1, 1),
    _AlrBufIdx_Type()
)
alrBufIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrBufIdx.setStatus("current")


class _AlrBufDescription_Type(DisplayString):
    """Custom type alrBufDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlrBufDescription_Type.__name__ = "DisplayString"
_AlrBufDescription_Object = MibTableColumn
alrBufDescription = _AlrBufDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 1, 1, 2),
    _AlrBufDescription_Type()
)
alrBufDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrBufDescription.setStatus("current")
_AlrBufCode_Type = Unsigned32
_AlrBufCode_Object = MibTableColumn
alrBufCode = _AlrBufCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 1, 1, 3),
    _AlrBufCode_Type()
)
alrBufCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrBufCode.setStatus("current")


class _AlrBufSlot_Type(Integer32):
    """Custom type alrBufSlot based on Integer32"""
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
              13,
              14,
              255)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("notApplicable", 255))
    )


_AlrBufSlot_Type.__name__ = "Integer32"
_AlrBufSlot_Object = MibTableColumn
alrBufSlot = _AlrBufSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 1, 1, 4),
    _AlrBufSlot_Type()
)
alrBufSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrBufSlot.setStatus("current")
_AlrBufPort_Type = Unsigned32
_AlrBufPort_Object = MibTableColumn
alrBufPort = _AlrBufPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 1, 1, 5),
    _AlrBufPort_Type()
)
alrBufPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrBufPort.setStatus("current")


class _AlrBufSeverity_Type(Integer32):
    """Custom type alrBufSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AlrBufSeverity_Type.__name__ = "Integer32"
_AlrBufSeverity_Object = MibTableColumn
alrBufSeverity = _AlrBufSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 1, 1, 6),
    _AlrBufSeverity_Type()
)
alrBufSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrBufSeverity.setStatus("current")


class _AlrBufState_Type(Integer32):
    """Custom type alrBufState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AlrBufState_Type.__name__ = "Integer32"
_AlrBufState_Object = MibTableColumn
alrBufState = _AlrBufState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 1, 1, 7),
    _AlrBufState_Type()
)
alrBufState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrBufState.setStatus("current")


class _AlrBufferClearCmd_Type(Integer32):
    """Custom type alrBufferClearCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AlrBufferClearCmd_Type.__name__ = "Integer32"
_AlrBufferClearCmd_Object = MibScalar
alrBufferClearCmd = _AlrBufferClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 2),
    _AlrBufferClearCmd_Type()
)
alrBufferClearCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alrBufferClearCmd.setStatus("current")
_AlrBufIdxUponLastAck_Type = Unsigned32
_AlrBufIdxUponLastAck_Object = MibScalar
alrBufIdxUponLastAck = _AlrBufIdxUponLastAck_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 4, 3),
    _AlrBufIdxUponLastAck_Type()
)
alrBufIdxUponLastAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alrBufIdxUponLastAck.setStatus("current")
_AgnFlipDb_ObjectIdentity = ObjectIdentity
agnFlipDb = _AgnFlipDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5)
)
_AgnCAgendaTable_Object = MibTable
agnCAgendaTable = _AgnCAgendaTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    agnCAgendaTable.setStatus("current")
_AgnCAgendaEntry_Object = MibTableRow
agnCAgendaEntry = _AgnCAgendaEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 1, 1)
)
agnCAgendaEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCAgendaCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnCAgendaDayIdx"),
)
if mibBuilder.loadTexts:
    agnCAgendaEntry.setStatus("current")


class _AgnCAgendaCnfgIdx_Type(Integer32):
    """Custom type agnCAgendaCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("temporary", 255))
    )


_AgnCAgendaCnfgIdx_Type.__name__ = "Integer32"
_AgnCAgendaCnfgIdx_Object = MibTableColumn
agnCAgendaCnfgIdx = _AgnCAgendaCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 1, 1, 1),
    _AgnCAgendaCnfgIdx_Type()
)
agnCAgendaCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCAgendaCnfgIdx.setStatus("current")


class _AgnCAgendaDayIdx_Type(Integer32):
    """Custom type agnCAgendaDayIdx based on Integer32"""
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
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_AgnCAgendaDayIdx_Type.__name__ = "Integer32"
_AgnCAgendaDayIdx_Object = MibTableColumn
agnCAgendaDayIdx = _AgnCAgendaDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 1, 1, 2),
    _AgnCAgendaDayIdx_Type()
)
agnCAgendaDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCAgendaDayIdx.setStatus("current")


class _AgnCAgendaDayCategory_Type(Integer32):
    """Custom type agnCAgendaDayCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullWorkday", 1),
          ("partialWorkday", 2),
          ("weekend", 3))
    )


_AgnCAgendaDayCategory_Type.__name__ = "Integer32"
_AgnCAgendaDayCategory_Object = MibTableColumn
agnCAgendaDayCategory = _AgnCAgendaDayCategory_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 1, 1, 3),
    _AgnCAgendaDayCategory_Type()
)
agnCAgendaDayCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCAgendaDayCategory.setStatus("current")
_AgnCFlipNetEventsTable_Object = MibTable
agnCFlipNetEventsTable = _AgnCFlipNetEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    agnCFlipNetEventsTable.setStatus("current")
_AgnCFlipNetEventsEntry_Object = MibTableRow
agnCFlipNetEventsEntry = _AgnCFlipNetEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1)
)
agnCFlipNetEventsEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCFlipNetEventsCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnCFlipNetEventIdx"),
)
if mibBuilder.loadTexts:
    agnCFlipNetEventsEntry.setStatus("current")


class _AgnCFlipNetEventsCnfgIdx_Type(Integer32):
    """Custom type agnCFlipNetEventsCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("temporary", 255))
    )


_AgnCFlipNetEventsCnfgIdx_Type.__name__ = "Integer32"
_AgnCFlipNetEventsCnfgIdx_Object = MibTableColumn
agnCFlipNetEventsCnfgIdx = _AgnCFlipNetEventsCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 1),
    _AgnCFlipNetEventsCnfgIdx_Type()
)
agnCFlipNetEventsCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCFlipNetEventsCnfgIdx.setStatus("current")


class _AgnCFlipNetEventIdx_Type(Integer32):
    """Custom type agnCFlipNetEventIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgnCFlipNetEventIdx_Type.__name__ = "Integer32"
_AgnCFlipNetEventIdx_Object = MibTableColumn
agnCFlipNetEventIdx = _AgnCFlipNetEventIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 2),
    _AgnCFlipNetEventIdx_Type()
)
agnCFlipNetEventIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCFlipNetEventIdx.setStatus("current")


class _AgnCFlipNetEventActive_Type(Integer32):
    """Custom type agnCFlipNetEventActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_AgnCFlipNetEventActive_Type.__name__ = "Integer32"
_AgnCFlipNetEventActive_Object = MibTableColumn
agnCFlipNetEventActive = _AgnCFlipNetEventActive_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 3),
    _AgnCFlipNetEventActive_Type()
)
agnCFlipNetEventActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventActive.setStatus("current")


class _AgnCFlipNetEventType_Type(Integer32):
    """Custom type agnCFlipNetEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("time", 1),
          ("linkDown", 2),
          ("congestion", 3))
    )


_AgnCFlipNetEventType_Type.__name__ = "Integer32"
_AgnCFlipNetEventType_Object = MibTableColumn
agnCFlipNetEventType = _AgnCFlipNetEventType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 4),
    _AgnCFlipNetEventType_Type()
)
agnCFlipNetEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventType.setStatus("current")


class _AgnCFlipNetEventNo_Type(Integer32):
    """Custom type agnCFlipNetEventNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_AgnCFlipNetEventNo_Type.__name__ = "Integer32"
_AgnCFlipNetEventNo_Object = MibTableColumn
agnCFlipNetEventNo = _AgnCFlipNetEventNo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 5),
    _AgnCFlipNetEventNo_Type()
)
agnCFlipNetEventNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventNo.setStatus("current")


class _AgnCFlipNetEventSlot_Type(Integer32):
    """Custom type agnCFlipNetEventSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_AgnCFlipNetEventSlot_Type.__name__ = "Integer32"
_AgnCFlipNetEventSlot_Object = MibTableColumn
agnCFlipNetEventSlot = _AgnCFlipNetEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 6),
    _AgnCFlipNetEventSlot_Type()
)
agnCFlipNetEventSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventSlot.setStatus("current")
_AgnCFlipNetEventPort_Type = Integer32
_AgnCFlipNetEventPort_Object = MibTableColumn
agnCFlipNetEventPort = _AgnCFlipNetEventPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 7),
    _AgnCFlipNetEventPort_Type()
)
agnCFlipNetEventPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventPort.setStatus("current")


class _AgnCFlipNetEventISD_Type(Integer32):
    """Custom type agnCFlipNetEventISD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AgnCFlipNetEventISD_Type.__name__ = "Integer32"
_AgnCFlipNetEventISD_Object = MibTableColumn
agnCFlipNetEventISD = _AgnCFlipNetEventISD_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 8),
    _AgnCFlipNetEventISD_Type()
)
agnCFlipNetEventISD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventISD.setStatus("current")


class _AgnCFlipNetEventOSD_Type(Integer32):
    """Custom type agnCFlipNetEventOSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AgnCFlipNetEventOSD_Type.__name__ = "Integer32"
_AgnCFlipNetEventOSD_Object = MibTableColumn
agnCFlipNetEventOSD = _AgnCFlipNetEventOSD_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 9),
    _AgnCFlipNetEventOSD_Type()
)
agnCFlipNetEventOSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventOSD.setStatus("current")


class _AgnCFlipNetEventDayType_Type(Integer32):
    """Custom type agnCFlipNetEventDayType based on Integer32"""
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
        *(("notApplicable", 1),
          ("fullWorkday", 2),
          ("partialWorkday", 3),
          ("weekend", 4))
    )


_AgnCFlipNetEventDayType_Type.__name__ = "Integer32"
_AgnCFlipNetEventDayType_Object = MibTableColumn
agnCFlipNetEventDayType = _AgnCFlipNetEventDayType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 10),
    _AgnCFlipNetEventDayType_Type()
)
agnCFlipNetEventDayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventDayType.setStatus("current")


class _AgnCFlipNetEventStartTime_Type(DisplayString):
    """Custom type agnCFlipNetEventStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_AgnCFlipNetEventStartTime_Type.__name__ = "DisplayString"
_AgnCFlipNetEventStartTime_Object = MibTableColumn
agnCFlipNetEventStartTime = _AgnCFlipNetEventStartTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 11),
    _AgnCFlipNetEventStartTime_Type()
)
agnCFlipNetEventStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventStartTime.setStatus("current")


class _AgnCFlipNetEventEndTime_Type(DisplayString):
    """Custom type agnCFlipNetEventEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_AgnCFlipNetEventEndTime_Type.__name__ = "DisplayString"
_AgnCFlipNetEventEndTime_Object = MibTableColumn
agnCFlipNetEventEndTime = _AgnCFlipNetEventEndTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 2, 1, 12),
    _AgnCFlipNetEventEndTime_Type()
)
agnCFlipNetEventEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipNetEventEndTime.setStatus("current")
_AgnCFlipTable_Object = MibTable
agnCFlipTable = _AgnCFlipTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    agnCFlipTable.setStatus("current")
_AgnCFlipEntry_Object = MibTableRow
agnCFlipEntry = _AgnCFlipEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 3, 1)
)
agnCFlipEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnCFlipCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnCFlipIdx"),
)
if mibBuilder.loadTexts:
    agnCFlipEntry.setStatus("current")


class _AgnCFlipCnfgIdx_Type(Integer32):
    """Custom type agnCFlipCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("temporary", 255))
    )


_AgnCFlipCnfgIdx_Type.__name__ = "Integer32"
_AgnCFlipCnfgIdx_Object = MibTableColumn
agnCFlipCnfgIdx = _AgnCFlipCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 3, 1, 1),
    _AgnCFlipCnfgIdx_Type()
)
agnCFlipCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCFlipCnfgIdx.setStatus("current")


class _AgnCFlipIdx_Type(Integer32):
    """Custom type agnCFlipIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgnCFlipIdx_Type.__name__ = "Integer32"
_AgnCFlipIdx_Object = MibTableColumn
agnCFlipIdx = _AgnCFlipIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 3, 1, 2),
    _AgnCFlipIdx_Type()
)
agnCFlipIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnCFlipIdx.setStatus("current")


class _AgnCFlipActive_Type(Integer32):
    """Custom type agnCFlipActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_AgnCFlipActive_Type.__name__ = "Integer32"
_AgnCFlipActive_Object = MibTableColumn
agnCFlipActive = _AgnCFlipActive_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 3, 1, 3),
    _AgnCFlipActive_Type()
)
agnCFlipActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipActive.setStatus("current")


class _AgnCFlipLogicalExp_Type(DisplayString):
    """Custom type agnCFlipLogicalExp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AgnCFlipLogicalExp_Type.__name__ = "DisplayString"
_AgnCFlipLogicalExp_Object = MibTableColumn
agnCFlipLogicalExp = _AgnCFlipLogicalExp_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 3, 1, 4),
    _AgnCFlipLogicalExp_Type()
)
agnCFlipLogicalExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipLogicalExp.setStatus("current")


class _AgnCFlipDbNo_Type(Integer32):
    """Custom type agnCFlipDbNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgnCFlipDbNo_Type.__name__ = "Integer32"
_AgnCFlipDbNo_Object = MibTableColumn
agnCFlipDbNo = _AgnCFlipDbNo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 3, 1, 5),
    _AgnCFlipDbNo_Type()
)
agnCFlipDbNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipDbNo.setStatus("current")


class _AgnCFlipDiscardDe_Type(Integer32):
    """Custom type agnCFlipDiscardDe based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_AgnCFlipDiscardDe_Type.__name__ = "Integer32"
_AgnCFlipDiscardDe_Object = MibTableColumn
agnCFlipDiscardDe = _AgnCFlipDiscardDe_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 3, 1, 6),
    _AgnCFlipDiscardDe_Type()
)
agnCFlipDiscardDe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipDiscardDe.setStatus("current")
_AgnFlipDbControls_ObjectIdentity = ObjectIdentity
agnFlipDbControls = _AgnFlipDbControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 4)
)


class _AgnCFlipDbSanityCheckCmd_Type(Integer32):
    """Custom type agnCFlipDbSanityCheckCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnCFlipDbSanityCheckCmd_Type.__name__ = "Integer32"
_AgnCFlipDbSanityCheckCmd_Object = MibScalar
agnCFlipDbSanityCheckCmd = _AgnCFlipDbSanityCheckCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 4, 1),
    _AgnCFlipDbSanityCheckCmd_Type()
)
agnCFlipDbSanityCheckCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCFlipDbSanityCheckCmd.setStatus("current")


class _AgnCSaveFlipDbCmd_Type(Integer32):
    """Custom type agnCSaveFlipDbCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnCSaveFlipDbCmd_Type.__name__ = "Integer32"
_AgnCSaveFlipDbCmd_Object = MibScalar
agnCSaveFlipDbCmd = _AgnCSaveFlipDbCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 4, 2),
    _AgnCSaveFlipDbCmd_Type()
)
agnCSaveFlipDbCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCSaveFlipDbCmd.setStatus("current")


class _AgnCSaveNetCnfgIdxCmd_Type(Integer32):
    """Custom type agnCSaveNetCnfgIdxCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgnCSaveNetCnfgIdxCmd_Type.__name__ = "Integer32"
_AgnCSaveNetCnfgIdxCmd_Object = MibScalar
agnCSaveNetCnfgIdxCmd = _AgnCSaveNetCnfgIdxCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 4, 3),
    _AgnCSaveNetCnfgIdxCmd_Type()
)
agnCSaveNetCnfgIdxCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCSaveNetCnfgIdxCmd.setStatus("current")


class _AgnCSaveNetFlipDbCmd_Type(Integer32):
    """Custom type agnCSaveNetFlipDbCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnCSaveNetFlipDbCmd_Type.__name__ = "Integer32"
_AgnCSaveNetFlipDbCmd_Object = MibScalar
agnCSaveNetFlipDbCmd = _AgnCSaveNetFlipDbCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 4, 4),
    _AgnCSaveNetFlipDbCmd_Type()
)
agnCSaveNetFlipDbCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCSaveNetFlipDbCmd.setStatus("current")


class _AgnCNetGoCmd_Type(Integer32):
    """Custom type agnCNetGoCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnCNetGoCmd_Type.__name__ = "Integer32"
_AgnCNetGoCmd_Object = MibScalar
agnCNetGoCmd = _AgnCNetGoCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 4, 5),
    _AgnCNetGoCmd_Type()
)
agnCNetGoCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCNetGoCmd.setStatus("current")


class _AgnCNetDelay_Type(Integer32):
    """Custom type agnCNetDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AgnCNetDelay_Type.__name__ = "Integer32"
_AgnCNetDelay_Object = MibScalar
agnCNetDelay = _AgnCNetDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 4, 6),
    _AgnCNetDelay_Type()
)
agnCNetDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCNetDelay.setStatus("current")


class _AgnCNetEventsBcast_Type(Integer32):
    """Custom type agnCNetEventsBcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_AgnCNetEventsBcast_Type.__name__ = "Integer32"
_AgnCNetEventsBcast_Object = MibScalar
agnCNetEventsBcast = _AgnCNetEventsBcast_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 4, 7),
    _AgnCNetEventsBcast_Type()
)
agnCNetEventsBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCNetEventsBcast.setStatus("current")


class _AgnCNetEventsBcastInterval_Type(Integer32):
    """Custom type agnCNetEventsBcastInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_AgnCNetEventsBcastInterval_Type.__name__ = "Integer32"
_AgnCNetEventsBcastInterval_Object = MibScalar
agnCNetEventsBcastInterval = _AgnCNetEventsBcastInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 5, 4, 8),
    _AgnCNetEventsBcastInterval_Type()
)
agnCNetEventsBcastInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnCNetEventsBcastInterval.setStatus("current")
_AgnSa_ObjectIdentity = ObjectIdentity
agnSa = _AgnSa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 6)
)
_AgnSaSwchStatus_Type = Integer32
_AgnSaSwchStatus_Object = MibScalar
agnSaSwchStatus = _AgnSaSwchStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 6, 1),
    _AgnSaSwchStatus_Type()
)
agnSaSwchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSaSwchStatus.setStatus("current")
_AgnListDecoding_ObjectIdentity = ObjectIdentity
agnListDecoding = _AgnListDecoding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7)
)
_AgnListDecodingTable_Object = MibTable
agnListDecodingTable = _AgnListDecodingTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    agnListDecodingTable.setStatus("current")
_AgnListDecodingEntry_Object = MibTableRow
agnListDecodingEntry = _AgnListDecodingEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7, 1, 1)
)
agnListDecodingEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnListDecodingType"),
    (0, "RAD-Mpmx-MIB", "agnListDecodingCode"),
)
if mibBuilder.loadTexts:
    agnListDecodingEntry.setStatus("current")


class _AgnListDecodingType_Type(Integer32):
    """Custom type agnListDecodingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alr", 1),
          ("sanity", 2),
          ("counter", 3))
    )


_AgnListDecodingType_Type.__name__ = "Integer32"
_AgnListDecodingType_Object = MibTableColumn
agnListDecodingType = _AgnListDecodingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7, 1, 1, 1),
    _AgnListDecodingType_Type()
)
agnListDecodingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnListDecodingType.setStatus("current")
_AgnListDecodingCode_Type = Integer32
_AgnListDecodingCode_Object = MibTableColumn
agnListDecodingCode = _AgnListDecodingCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7, 1, 1, 2),
    _AgnListDecodingCode_Type()
)
agnListDecodingCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnListDecodingCode.setStatus("current")


class _AgnListDecodingDescription_Type(DisplayString):
    """Custom type agnListDecodingDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgnListDecodingDescription_Type.__name__ = "DisplayString"
_AgnListDecodingDescription_Object = MibTableColumn
agnListDecodingDescription = _AgnListDecodingDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7, 1, 1, 3),
    _AgnListDecodingDescription_Type()
)
agnListDecodingDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnListDecodingDescription.setStatus("current")


class _AgnListDecodingDefState_Type(Integer32):
    """Custom type agnListDecodingDefState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnListDecodingDefState_Type.__name__ = "Integer32"
_AgnListDecodingDefState_Object = MibTableColumn
agnListDecodingDefState = _AgnListDecodingDefState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7, 1, 1, 4),
    _AgnListDecodingDefState_Type()
)
agnListDecodingDefState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnListDecodingDefState.setStatus("current")


class _AgnListDecodingSeverity_Type(Integer32):
    """Custom type agnListDecodingSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AgnListDecodingSeverity_Type.__name__ = "Integer32"
_AgnListDecodingSeverity_Object = MibTableColumn
agnListDecodingSeverity = _AgnListDecodingSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7, 1, 1, 5),
    _AgnListDecodingSeverity_Type()
)
agnListDecodingSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnListDecodingSeverity.setStatus("current")


class _AgnListDecodingAcmRelaySlt_Type(Integer32):
    """Custom type agnListDecodingAcmRelaySlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_AgnListDecodingAcmRelaySlt_Type.__name__ = "Integer32"
_AgnListDecodingAcmRelaySlt_Object = MibTableColumn
agnListDecodingAcmRelaySlt = _AgnListDecodingAcmRelaySlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7, 1, 1, 6),
    _AgnListDecodingAcmRelaySlt_Type()
)
agnListDecodingAcmRelaySlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnListDecodingAcmRelaySlt.setStatus("current")


class _AgnListDecodingAcmRelayPrt_Type(Integer32):
    """Custom type agnListDecodingAcmRelayPrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("notApplicable", 255))
    )


_AgnListDecodingAcmRelayPrt_Type.__name__ = "Integer32"
_AgnListDecodingAcmRelayPrt_Object = MibTableColumn
agnListDecodingAcmRelayPrt = _AgnListDecodingAcmRelayPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 7, 1, 1, 7),
    _AgnListDecodingAcmRelayPrt_Type()
)
agnListDecodingAcmRelayPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnListDecodingAcmRelayPrt.setStatus("current")
_AgnSystemDlci_ObjectIdentity = ObjectIdentity
agnSystemDlci = _AgnSystemDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8)
)
_AgnDlciTable_Object = MibTable
agnDlciTable = _AgnDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    agnDlciTable.setStatus("current")
_AgnDlciEntry_Object = MibTableRow
agnDlciEntry = _AgnDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1)
)
agnDlciEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnDlciCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnDlciLSltIdx"),
    (0, "RAD-Mpmx-MIB", "agnDlciLPrtIdx"),
    (0, "RAD-Mpmx-MIB", "agnDlciHIdx"),
    (0, "RAD-Mpmx-MIB", "agnDlciHSltIdx"),
    (0, "RAD-Mpmx-MIB", "agnDlciHPrtIdx"),
    (0, "RAD-Mpmx-MIB", "agnDlciLIdx"),
)
if mibBuilder.loadTexts:
    agnDlciEntry.setStatus("current")


class _AgnDlciCnfgIdx_Type(Integer32):
    """Custom type agnDlciCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgnDlciCnfgIdx_Type.__name__ = "Integer32"
_AgnDlciCnfgIdx_Object = MibTableColumn
agnDlciCnfgIdx = _AgnDlciCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 1),
    _AgnDlciCnfgIdx_Type()
)
agnDlciCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciCnfgIdx.setStatus("current")


class _AgnDlciLSltIdx_Type(Integer32):
    """Custom type agnDlciLSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cl", 3),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("vs", 254),
          ("notApplicable", 255))
    )


_AgnDlciLSltIdx_Type.__name__ = "Integer32"
_AgnDlciLSltIdx_Object = MibTableColumn
agnDlciLSltIdx = _AgnDlciLSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 2),
    _AgnDlciLSltIdx_Type()
)
agnDlciLSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciLSltIdx.setStatus("current")
_AgnDlciLPrtIdx_Type = Integer32
_AgnDlciLPrtIdx_Object = MibTableColumn
agnDlciLPrtIdx = _AgnDlciLPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 3),
    _AgnDlciLPrtIdx_Type()
)
agnDlciLPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciLPrtIdx.setStatus("current")


class _AgnDlciLIdx_Type(Integer32):
    """Custom type agnDlciLIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 991),
    )


_AgnDlciLIdx_Type.__name__ = "Integer32"
_AgnDlciLIdx_Object = MibTableColumn
agnDlciLIdx = _AgnDlciLIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 4),
    _AgnDlciLIdx_Type()
)
agnDlciLIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciLIdx.setStatus("current")


class _AgnDlciHSltIdx_Type(Integer32):
    """Custom type agnDlciHSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cl", 3),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_AgnDlciHSltIdx_Type.__name__ = "Integer32"
_AgnDlciHSltIdx_Object = MibTableColumn
agnDlciHSltIdx = _AgnDlciHSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 5),
    _AgnDlciHSltIdx_Type()
)
agnDlciHSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciHSltIdx.setStatus("current")
_AgnDlciHPrtIdx_Type = Integer32
_AgnDlciHPrtIdx_Object = MibTableColumn
agnDlciHPrtIdx = _AgnDlciHPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 6),
    _AgnDlciHPrtIdx_Type()
)
agnDlciHPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciHPrtIdx.setStatus("current")


class _AgnDlciHIdx_Type(Integer32):
    """Custom type agnDlciHIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 991),
    )


_AgnDlciHIdx_Type.__name__ = "Integer32"
_AgnDlciHIdx_Object = MibTableColumn
agnDlciHIdx = _AgnDlciHIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 7),
    _AgnDlciHIdx_Type()
)
agnDlciHIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciHIdx.setStatus("current")


class _AgnDlciTxBc_Type(Integer32):
    """Custom type agnDlciTxBc based on Integer32"""
    defaultValue = 1

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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("txBc5100bps", 3),
          ("txBc6400bps", 4),
          ("txBc8300bps", 5),
          ("txBc9600bps", 6),
          ("txBc14400bps", 7),
          ("txBc19200bps", 8),
          ("txBc28800bps", 9),
          ("txBc32000bps", 10),
          ("txBc38400bps", 11),
          ("txBc48000bps", 12),
          ("txBc56000bps", 13),
          ("txBc57600bps", 14),
          ("txBc64Kbps", 15),
          ("txBc128Kbps", 16),
          ("txBc192Kbps", 17),
          ("txBc256Kbps", 18),
          ("txBc320Kbps", 19),
          ("txBc384Kbps", 20),
          ("txBc448Kbps", 21),
          ("txBc512Kbps", 22),
          ("txBc768Kbps", 23),
          ("txBc896Kbps", 24),
          ("txBc1024Kbps", 25),
          ("txBc1152Kbps", 26),
          ("txBc1280Kbps", 27),
          ("txBc1344Kbps", 28),
          ("txBc1472Kbps", 29),
          ("txBc1600Kbps", 30),
          ("txBc1728Kbps", 31),
          ("txBc1856Kbps", 32),
          ("txBc1920Kbps", 33),
          ("txBc1984Kbps", 34),
          ("txBc2048Kbps", 35),
          ("txBc16000bps", 36),
          ("txBc112Kbps", 37),
          ("txBc168Kbps", 38),
          ("txBc224Kbps", 39),
          ("txBc336Kbps", 40),
          ("txBc672Kbps", 41),
          ("txBc1536Kbps", 42),
          ("txBc1792Kbps", 43))
    )


_AgnDlciTxBc_Type.__name__ = "Integer32"
_AgnDlciTxBc_Object = MibTableColumn
agnDlciTxBc = _AgnDlciTxBc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 8),
    _AgnDlciTxBc_Type()
)
agnDlciTxBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnDlciTxBc.setStatus("current")


class _AgnDlciTxBe_Type(Integer32):
    """Custom type agnDlciTxBe based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("txBe5100bps", 3),
          ("txBe6400bps", 4),
          ("txBe8300bps", 5),
          ("txBe9600bps", 6),
          ("txBe14400bps", 7),
          ("txBe19200bps", 8),
          ("txBe28800bps", 9),
          ("txBe32000bps", 10),
          ("txBe38400bps", 11),
          ("txBe48000bps", 12),
          ("txBe56000bps", 13),
          ("txBe57600bps", 14),
          ("txBe64Kbps", 15),
          ("txBe128Kbps", 16),
          ("txBe192Kbps", 17),
          ("txBe256Kbps", 18),
          ("txBe320Kbps", 19),
          ("txBe384Kbps", 20),
          ("txBe448Kbps", 21),
          ("txBe512Kbps", 22),
          ("txBe768Kbps", 23),
          ("txBe896Kbps", 24),
          ("txBe1024Kbps", 25),
          ("txBe1152Kbps", 26),
          ("txBe1280Kbps", 27),
          ("txBe1344Kbps", 28),
          ("txBe1472Kbps", 29),
          ("txBe1600Kbps", 30),
          ("txBe1728Kbps", 31),
          ("txBe1856Kbps", 32),
          ("txBe1920Kbps", 33),
          ("txBe1984Kbps", 34),
          ("txBe2048Kbps", 35),
          ("txBe16000bps", 36),
          ("txBe112Kbps", 37),
          ("txBe168Kbps", 38),
          ("txBe224Kbps", 39),
          ("txBe336Kbps", 40),
          ("txBe672Kbps", 41),
          ("txBe1536Kbps", 42),
          ("txBe1792Kbps", 43))
    )


_AgnDlciTxBe_Type.__name__ = "Integer32"
_AgnDlciTxBe_Object = MibTableColumn
agnDlciTxBe = _AgnDlciTxBe_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 9),
    _AgnDlciTxBe_Type()
)
agnDlciTxBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnDlciTxBe.setStatus("current")


class _AgnDlciRxBc_Type(Integer32):
    """Custom type agnDlciRxBc based on Integer32"""
    defaultValue = 1

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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("rxBc5100bps", 3),
          ("rxBc6400bps", 4),
          ("rxBc8300bps", 5),
          ("rxBc9600bps", 6),
          ("rxBc14400bps", 7),
          ("rxBc19200bps", 8),
          ("rxBc28800bps", 9),
          ("rxBc32000bps", 10),
          ("rxBc38400bps", 11),
          ("rxBc48000bps", 12),
          ("rxBc56000bps", 13),
          ("rxBc57600bps", 14),
          ("rxBc64Kbps", 15),
          ("rxBc128Kbps", 16),
          ("rxBc192Kbps", 17),
          ("rxBc256Kbps", 18),
          ("rxBc320Kbps", 19),
          ("rxBc384Kbps", 20),
          ("rxBc448Kbps", 21),
          ("rxBc512Kbps", 22),
          ("rxBc768Kbps", 23),
          ("rxBc896Kbps", 24),
          ("rxBc1024Kbps", 25),
          ("rxBc1152Kbps", 26),
          ("rxBc1280Kbps", 27),
          ("rxBc1344Kbps", 28),
          ("rxBc1472Kbps", 29),
          ("rxBc1600Kbps", 30),
          ("rxBc1728Kbps", 31),
          ("rxBc1856Kbps", 32),
          ("rxBc1920Kbps", 33),
          ("rxBc1984Kbps", 34),
          ("rxBc2048Kbps", 35),
          ("rxBc16000bps", 36),
          ("rxBc112Kbps", 37),
          ("rxBc168Kbps", 38),
          ("rxBc224Kbps", 39),
          ("rxBc336Kbps", 40),
          ("rxBc672Kbps", 41),
          ("rxBc1536Kbps", 42),
          ("rxBc1792Kbps", 43))
    )


_AgnDlciRxBc_Type.__name__ = "Integer32"
_AgnDlciRxBc_Object = MibTableColumn
agnDlciRxBc = _AgnDlciRxBc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 10),
    _AgnDlciRxBc_Type()
)
agnDlciRxBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnDlciRxBc.setStatus("current")


class _AgnDlciRxBe_Type(Integer32):
    """Custom type agnDlciRxBe based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("rxBe5100bps", 3),
          ("rxBe6400bps", 4),
          ("rxBe8300bps", 5),
          ("rxBe9600bps", 6),
          ("rxBe14400bps", 7),
          ("rxBe19200bps", 8),
          ("rxBe28800bps", 9),
          ("rxBe32000bps", 10),
          ("rxBe38400bps", 11),
          ("rxBe48000bps", 12),
          ("rxBe56000bps", 13),
          ("rxBe57600bps", 14),
          ("rxBe64Kbps", 15),
          ("rxBe128Kbps", 16),
          ("rxBe192Kbps", 17),
          ("rxBe256Kbps", 18),
          ("rxBe320Kbps", 19),
          ("rxBe384Kbps", 20),
          ("rxBe448Kbps", 21),
          ("rxBe512Kbps", 22),
          ("rxBe768Kbps", 23),
          ("rxBe896Kbps", 24),
          ("rxBe1024Kbps", 25),
          ("rxBe1152Kbps", 26),
          ("rxBe1280Kbps", 27),
          ("rxBe1344Kbps", 28),
          ("rxBe1472Kbps", 29),
          ("rxBe1600Kbps", 30),
          ("rxBe1728Kbps", 31),
          ("rxBe1856Kbps", 32),
          ("rxBe1920Kbps", 33),
          ("rxBe1984Kbps", 34),
          ("rxBe2048Kbps", 35),
          ("rxBe16000bps", 36),
          ("rxBe112Kbps", 37),
          ("rxBe168Kbps", 38),
          ("rxBe224Kbps", 39),
          ("rxBe336Kbps", 40),
          ("rxBe672Kbps", 41),
          ("rxBe1536Kbps", 42),
          ("rxBe1792Kbps", 43))
    )


_AgnDlciRxBe_Type.__name__ = "Integer32"
_AgnDlciRxBe_Object = MibTableColumn
agnDlciRxBe = _AgnDlciRxBe_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 11),
    _AgnDlciRxBe_Type()
)
agnDlciRxBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnDlciRxBe.setStatus("current")


class _AgnDlciPriority_Type(Integer32):
    """Custom type agnDlciPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AgnDlciPriority_Type.__name__ = "Integer32"
_AgnDlciPriority_Object = MibTableColumn
agnDlciPriority = _AgnDlciPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 12),
    _AgnDlciPriority_Type()
)
agnDlciPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnDlciPriority.setStatus("current")


class _AgnDlciStatus_Type(Integer32):
    """Custom type agnDlciStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2))
    )


_AgnDlciStatus_Type.__name__ = "Integer32"
_AgnDlciStatus_Object = MibTableColumn
agnDlciStatus = _AgnDlciStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 13),
    _AgnDlciStatus_Type()
)
agnDlciStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDlciStatus.setStatus("current")


class _AgnDlciSpoofing_Type(Integer32):
    """Custom type agnDlciSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_AgnDlciSpoofing_Type.__name__ = "Integer32"
_AgnDlciSpoofing_Object = MibTableColumn
agnDlciSpoofing = _AgnDlciSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 14),
    _AgnDlciSpoofing_Type()
)
agnDlciSpoofing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnDlciSpoofing.setStatus("current")


class _AgnDlciFunnelEnable_Type(Integer32):
    """Custom type agnDlciFunnelEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("source", 4),
          ("destination", 5))
    )


_AgnDlciFunnelEnable_Type.__name__ = "Integer32"
_AgnDlciFunnelEnable_Object = MibTableColumn
agnDlciFunnelEnable = _AgnDlciFunnelEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 15),
    _AgnDlciFunnelEnable_Type()
)
agnDlciFunnelEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnDlciFunnelEnable.setStatus("current")


class _AgnDlciRoutingProtocol_Type(Integer32):
    """Custom type agnDlciRoutingProtocol based on Integer32"""
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
        *(("notApplicable", 1),
          ("rip", 2),
          ("rip2", 3),
          ("none", 4))
    )


_AgnDlciRoutingProtocol_Type.__name__ = "Integer32"
_AgnDlciRoutingProtocol_Object = MibTableColumn
agnDlciRoutingProtocol = _AgnDlciRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 16),
    _AgnDlciRoutingProtocol_Type()
)
agnDlciRoutingProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnDlciRoutingProtocol.setStatus("current")
_AgnDlciRowStatus_Type = RowStatus
_AgnDlciRowStatus_Object = MibTableColumn
agnDlciRowStatus = _AgnDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 8, 1, 1, 17),
    _AgnDlciRowStatus_Type()
)
agnDlciRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnDlciRowStatus.setStatus("current")
_AgnVoiceSwitching_ObjectIdentity = ObjectIdentity
agnVoiceSwitching = _AgnVoiceSwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9)
)
_AgnVoiceSwConfTable_Object = MibTable
agnVoiceSwConfTable = _AgnVoiceSwConfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    agnVoiceSwConfTable.setStatus("current")
_AgnVoiceSwConfEntry_Object = MibTableRow
agnVoiceSwConfEntry = _AgnVoiceSwConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 1, 1)
)
agnVoiceSwConfEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnVoiceSwConfIdx"),
)
if mibBuilder.loadTexts:
    agnVoiceSwConfEntry.setStatus("current")


class _AgnVoiceSwConfIdx_Type(Integer32):
    """Custom type agnVoiceSwConfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("temporary", 255))
    )


_AgnVoiceSwConfIdx_Type.__name__ = "Integer32"
_AgnVoiceSwConfIdx_Object = MibTableColumn
agnVoiceSwConfIdx = _AgnVoiceSwConfIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 1, 1, 1),
    _AgnVoiceSwConfIdx_Type()
)
agnVoiceSwConfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnVoiceSwConfIdx.setStatus("current")


class _AgnVoiceSwConfZoneId_Type(DisplayString):
    """Custom type agnVoiceSwConfZoneId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AgnVoiceSwConfZoneId_Type.__name__ = "DisplayString"
_AgnVoiceSwConfZoneId_Object = MibTableColumn
agnVoiceSwConfZoneId = _AgnVoiceSwConfZoneId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 1, 1, 2),
    _AgnVoiceSwConfZoneId_Type()
)
agnVoiceSwConfZoneId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfZoneId.setStatus("current")


class _AgnVoiceSwConfNodeId_Type(DisplayString):
    """Custom type agnVoiceSwConfNodeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_AgnVoiceSwConfNodeId_Type.__name__ = "DisplayString"
_AgnVoiceSwConfNodeId_Object = MibTableColumn
agnVoiceSwConfNodeId = _AgnVoiceSwConfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 1, 1, 3),
    _AgnVoiceSwConfNodeId_Type()
)
agnVoiceSwConfNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfNodeId.setStatus("current")


class _AgnVoiceSwConfNoOfHops_Type(Integer32):
    """Custom type agnVoiceSwConfNoOfHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AgnVoiceSwConfNoOfHops_Type.__name__ = "Integer32"
_AgnVoiceSwConfNoOfHops_Object = MibTableColumn
agnVoiceSwConfNoOfHops = _AgnVoiceSwConfNoOfHops_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 1, 1, 4),
    _AgnVoiceSwConfNoOfHops_Type()
)
agnVoiceSwConfNoOfHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfNoOfHops.setStatus("current")


class _AgnVoiceSwConfSidt_Type(Integer32):
    """Custom type agnVoiceSwConfSidt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AgnVoiceSwConfSidt_Type.__name__ = "Integer32"
_AgnVoiceSwConfSidt_Object = MibTableColumn
agnVoiceSwConfSidt = _AgnVoiceSwConfSidt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 1, 1, 5),
    _AgnVoiceSwConfSidt_Type()
)
agnVoiceSwConfSidt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfSidt.setStatus("current")


class _AgnVoiceSwConfLidt_Type(Integer32):
    """Custom type agnVoiceSwConfLidt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AgnVoiceSwConfLidt_Type.__name__ = "Integer32"
_AgnVoiceSwConfLidt_Object = MibTableColumn
agnVoiceSwConfLidt = _AgnVoiceSwConfLidt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 1, 1, 6),
    _AgnVoiceSwConfLidt_Type()
)
agnVoiceSwConfLidt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfLidt.setStatus("current")


class _AgnVoiceSwConfDialPlan_Type(Integer32):
    """Custom type agnVoiceSwConfDialPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("staticDialPlan", 2),
          ("staticDialPlanPlus", 3),
          ("flexDialPlan", 4))
    )


_AgnVoiceSwConfDialPlan_Type.__name__ = "Integer32"
_AgnVoiceSwConfDialPlan_Object = MibTableColumn
agnVoiceSwConfDialPlan = _AgnVoiceSwConfDialPlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 1, 1, 7),
    _AgnVoiceSwConfDialPlan_Type()
)
agnVoiceSwConfDialPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfDialPlan.setStatus("current")
_AgnVoiceSwConfRtTable_Object = MibTable
agnVoiceSwConfRtTable = _AgnVoiceSwConfRtTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    agnVoiceSwConfRtTable.setStatus("current")
_AgnVoiceSwConfRtEntry_Object = MibTableRow
agnVoiceSwConfRtEntry = _AgnVoiceSwConfRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1)
)
agnVoiceSwConfRtEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnVoiceSwConfRtDbId"),
    (0, "RAD-Mpmx-MIB", "agnVoiceSwConfRtIdx"),
)
if mibBuilder.loadTexts:
    agnVoiceSwConfRtEntry.setStatus("current")


class _AgnVoiceSwConfRtDbId_Type(Integer32):
    """Custom type agnVoiceSwConfRtDbId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("temporary", 255))
    )


_AgnVoiceSwConfRtDbId_Type.__name__ = "Integer32"
_AgnVoiceSwConfRtDbId_Object = MibTableColumn
agnVoiceSwConfRtDbId = _AgnVoiceSwConfRtDbId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 1),
    _AgnVoiceSwConfRtDbId_Type()
)
agnVoiceSwConfRtDbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtDbId.setStatus("current")
_AgnVoiceSwConfRtIdx_Type = Integer32
_AgnVoiceSwConfRtIdx_Object = MibTableColumn
agnVoiceSwConfRtIdx = _AgnVoiceSwConfRtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 2),
    _AgnVoiceSwConfRtIdx_Type()
)
agnVoiceSwConfRtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtIdx.setStatus("current")


class _AgnVoiceSwConfRtDigits_Type(DisplayString):
    """Custom type agnVoiceSwConfRtDigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_AgnVoiceSwConfRtDigits_Type.__name__ = "DisplayString"
_AgnVoiceSwConfRtDigits_Object = MibTableColumn
agnVoiceSwConfRtDigits = _AgnVoiceSwConfRtDigits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 3),
    _AgnVoiceSwConfRtDigits_Type()
)
agnVoiceSwConfRtDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtDigits.setStatus("current")


class _AgnVoiceSwConfRtAction_Type(Integer32):
    """Custom type agnVoiceSwConfRtAction based on Integer32"""
    defaultValue = 1

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
        *(("notApplicable", 1),
          ("zone", 2),
          ("node", 3),
          ("shortDialing", 4),
          ("in", 5),
          ("hgr", 6),
          ("del", 7),
          ("rep", 8),
          ("pri", 9),
          ("bri", 10),
          ("numDigDP", 11),
          ("route", 12),
          ("ext", 13))
    )


_AgnVoiceSwConfRtAction_Type.__name__ = "Integer32"
_AgnVoiceSwConfRtAction_Object = MibTableColumn
agnVoiceSwConfRtAction = _AgnVoiceSwConfRtAction_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 4),
    _AgnVoiceSwConfRtAction_Type()
)
agnVoiceSwConfRtAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtAction.setStatus("current")


class _AgnVoiceSwConfRtData_Type(DisplayString):
    """Custom type agnVoiceSwConfRtData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_AgnVoiceSwConfRtData_Type.__name__ = "DisplayString"
_AgnVoiceSwConfRtData_Object = MibTableColumn
agnVoiceSwConfRtData = _AgnVoiceSwConfRtData_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 5),
    _AgnVoiceSwConfRtData_Type()
)
agnVoiceSwConfRtData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtData.setStatus("current")


class _AgnVoiceSwConfRtSlot_Type(Integer32):
    """Custom type agnVoiceSwConfRtSlot based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("cl", 3),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_AgnVoiceSwConfRtSlot_Type.__name__ = "Integer32"
_AgnVoiceSwConfRtSlot_Object = MibTableColumn
agnVoiceSwConfRtSlot = _AgnVoiceSwConfRtSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 6),
    _AgnVoiceSwConfRtSlot_Type()
)
agnVoiceSwConfRtSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtSlot.setStatus("current")


class _AgnVoiceSwConfRtPort_Type(Integer32):
    """Custom type agnVoiceSwConfRtPort based on Integer32"""
    defaultValue = 0


_AgnVoiceSwConfRtPort_Type.__name__ = "Integer32"
_AgnVoiceSwConfRtPort_Object = MibTableColumn
agnVoiceSwConfRtPort = _AgnVoiceSwConfRtPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 7),
    _AgnVoiceSwConfRtPort_Type()
)
agnVoiceSwConfRtPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtPort.setStatus("current")


class _AgnVoiceSwConfRtDlci_Type(Integer32):
    """Custom type agnVoiceSwConfRtDlci based on Integer32"""
    defaultValue = 15


_AgnVoiceSwConfRtDlci_Type.__name__ = "Integer32"
_AgnVoiceSwConfRtDlci_Object = MibTableColumn
agnVoiceSwConfRtDlci = _AgnVoiceSwConfRtDlci_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 8),
    _AgnVoiceSwConfRtDlci_Type()
)
agnVoiceSwConfRtDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtDlci.setStatus("current")
_AgnVoiceSwConfRtRowStatus_Type = RowStatus
_AgnVoiceSwConfRtRowStatus_Object = MibTableColumn
agnVoiceSwConfRtRowStatus = _AgnVoiceSwConfRtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 9),
    _AgnVoiceSwConfRtRowStatus_Type()
)
agnVoiceSwConfRtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtRowStatus.setStatus("current")
_AgnVoiceSwConfRtMaxCalls_Type = Integer32
_AgnVoiceSwConfRtMaxCalls_Object = MibTableColumn
agnVoiceSwConfRtMaxCalls = _AgnVoiceSwConfRtMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 10),
    _AgnVoiceSwConfRtMaxCalls_Type()
)
agnVoiceSwConfRtMaxCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtMaxCalls.setStatus("current")
_AgnVoiceSwConfRtPriority_Type = Integer32
_AgnVoiceSwConfRtPriority_Object = MibTableColumn
agnVoiceSwConfRtPriority = _AgnVoiceSwConfRtPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 2, 1, 11),
    _AgnVoiceSwConfRtPriority_Type()
)
agnVoiceSwConfRtPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agnVoiceSwConfRtPriority.setStatus("current")
_AgnVoiceSwConfHGTable_Object = MibTable
agnVoiceSwConfHGTable = _AgnVoiceSwConfHGTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 5)
)
if mibBuilder.loadTexts:
    agnVoiceSwConfHGTable.setStatus("current")
_AgnVoiceSwConfHGEntry_Object = MibTableRow
agnVoiceSwConfHGEntry = _AgnVoiceSwConfHGEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 5, 1)
)
agnVoiceSwConfHGEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnVoiceSwConfHGdbIdx"),
    (0, "RAD-Mpmx-MIB", "agnVoiceSwConfHGIdx"),
)
if mibBuilder.loadTexts:
    agnVoiceSwConfHGEntry.setStatus("current")


class _AgnVoiceSwConfHGdbIdx_Type(Integer32):
    """Custom type agnVoiceSwConfHGdbIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("temporary", 255))
    )


_AgnVoiceSwConfHGdbIdx_Type.__name__ = "Integer32"
_AgnVoiceSwConfHGdbIdx_Object = MibTableColumn
agnVoiceSwConfHGdbIdx = _AgnVoiceSwConfHGdbIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 5, 1, 1),
    _AgnVoiceSwConfHGdbIdx_Type()
)
agnVoiceSwConfHGdbIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnVoiceSwConfHGdbIdx.setStatus("current")
_AgnVoiceSwConfHGIdx_Type = Integer32
_AgnVoiceSwConfHGIdx_Object = MibTableColumn
agnVoiceSwConfHGIdx = _AgnVoiceSwConfHGIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 5, 1, 2),
    _AgnVoiceSwConfHGIdx_Type()
)
agnVoiceSwConfHGIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnVoiceSwConfHGIdx.setStatus("current")


class _AgnVoiceSwConfHGConnect_Type(Integer32):
    """Custom type agnVoiceSwConfHGConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_AgnVoiceSwConfHGConnect_Type.__name__ = "Integer32"
_AgnVoiceSwConfHGConnect_Object = MibTableColumn
agnVoiceSwConfHGConnect = _AgnVoiceSwConfHGConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 5, 1, 3),
    _AgnVoiceSwConfHGConnect_Type()
)
agnVoiceSwConfHGConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfHGConnect.setStatus("current")


class _AgnVoiceSwConfHGExt_Type(Integer32):
    """Custom type agnVoiceSwConfHGExt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AgnVoiceSwConfHGExt_Type.__name__ = "Integer32"
_AgnVoiceSwConfHGExt_Object = MibTableColumn
agnVoiceSwConfHGExt = _AgnVoiceSwConfHGExt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 5, 1, 4),
    _AgnVoiceSwConfHGExt_Type()
)
agnVoiceSwConfHGExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfHGExt.setStatus("current")
_AgnVoiceSwConfHGExtString_Type = SnmpAdminString
_AgnVoiceSwConfHGExtString_Object = MibTableColumn
agnVoiceSwConfHGExtString = _AgnVoiceSwConfHGExtString_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 5, 1, 5),
    _AgnVoiceSwConfHGExtString_Type()
)
agnVoiceSwConfHGExtString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfHGExtString.setStatus("current")
_AgnVoiceSwConfHGUserParams_Type = SnmpAdminString
_AgnVoiceSwConfHGUserParams_Object = MibTableColumn
agnVoiceSwConfHGUserParams = _AgnVoiceSwConfHGUserParams_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 5, 1, 6),
    _AgnVoiceSwConfHGUserParams_Type()
)
agnVoiceSwConfHGUserParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfHGUserParams.setStatus("current")


class _AgnVoiceSwConfHGStatus_Type(Integer32):
    """Custom type agnVoiceSwConfHGStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notApplicable", 255))
    )


_AgnVoiceSwConfHGStatus_Type.__name__ = "Integer32"
_AgnVoiceSwConfHGStatus_Object = MibTableColumn
agnVoiceSwConfHGStatus = _AgnVoiceSwConfHGStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 9, 5, 1, 7),
    _AgnVoiceSwConfHGStatus_Type()
)
agnVoiceSwConfHGStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnVoiceSwConfHGStatus.setStatus("current")
_AgnSigProfile_ObjectIdentity = ObjectIdentity
agnSigProfile = _AgnSigProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10)
)
_AgnSigProfileTable_Object = MibTable
agnSigProfileTable = _AgnSigProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    agnSigProfileTable.setStatus("current")
_AgnSigProfileEntry_Object = MibTableRow
agnSigProfileEntry = _AgnSigProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 1, 1)
)
agnSigProfileEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnSigProfileCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnSigProfileIdx"),
    (0, "RAD-Mpmx-MIB", "agnSigProfileRxTx"),
)
if mibBuilder.loadTexts:
    agnSigProfileEntry.setStatus("current")
_AgnSigProfileCnfgIdx_Type = Integer32
_AgnSigProfileCnfgIdx_Object = MibTableColumn
agnSigProfileCnfgIdx = _AgnSigProfileCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 1, 1, 1),
    _AgnSigProfileCnfgIdx_Type()
)
agnSigProfileCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSigProfileCnfgIdx.setStatus("current")


class _AgnSigProfileIdx_Type(Integer32):
    """Custom type agnSigProfileIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AgnSigProfileIdx_Type.__name__ = "Integer32"
_AgnSigProfileIdx_Object = MibTableColumn
agnSigProfileIdx = _AgnSigProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 1, 1, 2),
    _AgnSigProfileIdx_Type()
)
agnSigProfileIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSigProfileIdx.setStatus("current")


class _AgnSigProfileRxTx_Type(Integer32):
    """Custom type agnSigProfileRxTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )


_AgnSigProfileRxTx_Type.__name__ = "Integer32"
_AgnSigProfileRxTx_Object = MibTableColumn
agnSigProfileRxTx = _AgnSigProfileRxTx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 1, 1, 3),
    _AgnSigProfileRxTx_Type()
)
agnSigProfileRxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSigProfileRxTx.setStatus("current")
_AgnSigProfileABCD_Type = OctetString
_AgnSigProfileABCD_Object = MibTableColumn
agnSigProfileABCD = _AgnSigProfileABCD_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 1, 1, 4),
    _AgnSigProfileABCD_Type()
)
agnSigProfileABCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSigProfileABCD.setStatus("current")


class _AgnSigProfileEcanActSignal_Type(Integer32):
    """Custom type agnSigProfileEcanActSignal based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("aBit1", 2),
          ("aBit0", 3),
          ("bBit1", 4),
          ("bBit0", 5),
          ("cBit1", 6),
          ("cBit0", 7),
          ("dBit1", 8),
          ("dBit0", 9))
    )


_AgnSigProfileEcanActSignal_Type.__name__ = "Integer32"
_AgnSigProfileEcanActSignal_Object = MibTableColumn
agnSigProfileEcanActSignal = _AgnSigProfileEcanActSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 1, 1, 5),
    _AgnSigProfileEcanActSignal_Type()
)
agnSigProfileEcanActSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSigProfileEcanActSignal.setStatus("current")
_AgnSigProfileEcanRespDelay_Type = Unsigned32
_AgnSigProfileEcanRespDelay_Object = MibTableColumn
agnSigProfileEcanRespDelay = _AgnSigProfileEcanRespDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 1, 1, 6),
    _AgnSigProfileEcanRespDelay_Type()
)
agnSigProfileEcanRespDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSigProfileEcanRespDelay.setStatus("current")
_AgnSigProfTable_Object = MibTable
agnSigProfTable = _AgnSigProfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    agnSigProfTable.setStatus("current")
_AgnSigProfEntry_Object = MibTableRow
agnSigProfEntry = _AgnSigProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 2, 1)
)
agnSigProfEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "agnSigProfCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "agnSigProfIdx"),
)
if mibBuilder.loadTexts:
    agnSigProfEntry.setStatus("current")


class _AgnSigProfCnfgIdx_Type(Integer32):
    """Custom type agnSigProfCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgnSigProfCnfgIdx_Type.__name__ = "Integer32"
_AgnSigProfCnfgIdx_Object = MibTableColumn
agnSigProfCnfgIdx = _AgnSigProfCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 2, 1, 1),
    _AgnSigProfCnfgIdx_Type()
)
agnSigProfCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSigProfCnfgIdx.setStatus("current")


class _AgnSigProfIdx_Type(Integer32):
    """Custom type agnSigProfIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AgnSigProfIdx_Type.__name__ = "Integer32"
_AgnSigProfIdx_Object = MibTableColumn
agnSigProfIdx = _AgnSigProfIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 2, 1, 2),
    _AgnSigProfIdx_Type()
)
agnSigProfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSigProfIdx.setStatus("current")


class _AgnSigProfName_Type(DisplayString):
    """Custom type agnSigProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgnSigProfName_Type.__name__ = "DisplayString"
_AgnSigProfName_Object = MibTableColumn
agnSigProfName = _AgnSigProfName_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 2, 1, 3),
    _AgnSigProfName_Type()
)
agnSigProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSigProfName.setStatus("current")


class _AgnSigProfType_Type(Integer32):
    """Custom type agnSigProfType based on Integer32"""
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
          ("legacy", 2),
          ("r2Cas", 3))
    )


_AgnSigProfType_Type.__name__ = "Integer32"
_AgnSigProfType_Object = MibTableColumn
agnSigProfType = _AgnSigProfType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 10, 2, 1, 4),
    _AgnSigProfType_Type()
)
agnSigProfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSigProfType.setStatus("current")
_AgnSystemTs_ObjectIdentity = ObjectIdentity
agnSystemTs = _AgnSystemTs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 11)
)
_SystemVoice_ObjectIdentity = ObjectIdentity
systemVoice = _SystemVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12)
)
_SystemVoiceTable_Object = MibTable
systemVoiceTable = _SystemVoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    systemVoiceTable.setStatus("current")
_SystemVoiceEntry_Object = MibTableRow
systemVoiceEntry = _SystemVoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1)
)
systemVoiceEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "systemVoiceConfIdx"),
)
if mibBuilder.loadTexts:
    systemVoiceEntry.setStatus("current")
_SystemVoiceConfIdx_Type = Integer32
_SystemVoiceConfIdx_Object = MibTableColumn
systemVoiceConfIdx = _SystemVoiceConfIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 1),
    _SystemVoiceConfIdx_Type()
)
systemVoiceConfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVoiceConfIdx.setStatus("current")


class _SystemVoiceNationalTone_Type(Integer32):
    """Custom type systemVoiceNationalTone based on Integer32"""
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
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("usa", 2),
          ("australia", 3),
          ("brazil", 4),
          ("canada", 5),
          ("france", 6),
          ("germany", 7),
          ("israel", 8),
          ("mexico", 9),
          ("portugal", 10),
          ("russia", 11),
          ("spain", 12),
          ("unitedKingdom", 13),
          ("czech", 14),
          ("china", 15))
    )


_SystemVoiceNationalTone_Type.__name__ = "Integer32"
_SystemVoiceNationalTone_Object = MibTableColumn
systemVoiceNationalTone = _SystemVoiceNationalTone_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 2),
    _SystemVoiceNationalTone_Type()
)
systemVoiceNationalTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceNationalTone.setStatus("current")
_SystemVoicePacketRate_Type = Unsigned32
_SystemVoicePacketRate_Object = MibTableColumn
systemVoicePacketRate = _SystemVoicePacketRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 3),
    _SystemVoicePacketRate_Type()
)
systemVoicePacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoicePacketRate.setStatus("current")


class _SystemVoiceFaxSupport_Type(Integer32):
    """Custom type systemVoiceFaxSupport based on Integer32"""
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
        *(("notApplicable", 1),
          ("disable", 2),
          ("faxRelayT38", 3),
          ("vbdPassThrou", 4))
    )


_SystemVoiceFaxSupport_Type.__name__ = "Integer32"
_SystemVoiceFaxSupport_Object = MibTableColumn
systemVoiceFaxSupport = _SystemVoiceFaxSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 4),
    _SystemVoiceFaxSupport_Type()
)
systemVoiceFaxSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceFaxSupport.setStatus("current")


class _SystemVoiceFaxRate_Type(Integer32):
    """Custom type systemVoiceFaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 1),
          ("r4800bps", 2),
          ("r9600bps", 4),
          ("r14400bps", 6))
    )


_SystemVoiceFaxRate_Type.__name__ = "Integer32"
_SystemVoiceFaxRate_Object = MibTableColumn
systemVoiceFaxRate = _SystemVoiceFaxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 5),
    _SystemVoiceFaxRate_Type()
)
systemVoiceFaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceFaxRate.setStatus("current")


class _SystemVoiceModemSupport_Type(Integer32):
    """Custom type systemVoiceModemSupport based on Integer32"""
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
        *(("notApplicable", 1),
          ("disable", 2),
          ("vbdV152", 3),
          ("vbdPassThrou", 4))
    )


_SystemVoiceModemSupport_Type.__name__ = "Integer32"
_SystemVoiceModemSupport_Object = MibTableColumn
systemVoiceModemSupport = _SystemVoiceModemSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 6),
    _SystemVoiceModemSupport_Type()
)
systemVoiceModemSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceModemSupport.setStatus("current")


class _SystemVoiceCoderAndRate_Type(Integer32):
    """Custom type systemVoiceCoderAndRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("g711aLAW", 5),
          ("g711uLAW", 6))
    )


_SystemVoiceCoderAndRate_Type.__name__ = "Integer32"
_SystemVoiceCoderAndRate_Object = MibTableColumn
systemVoiceCoderAndRate = _SystemVoiceCoderAndRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 7),
    _SystemVoiceCoderAndRate_Type()
)
systemVoiceCoderAndRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceCoderAndRate.setStatus("current")


class _SystemVoiceEchoCanceler_Type(Integer32):
    """Custom type systemVoiceEchoCanceler based on Integer32"""
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


_SystemVoiceEchoCanceler_Type.__name__ = "Integer32"
_SystemVoiceEchoCanceler_Object = MibTableColumn
systemVoiceEchoCanceler = _SystemVoiceEchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 8),
    _SystemVoiceEchoCanceler_Type()
)
systemVoiceEchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceEchoCanceler.setStatus("current")
_SystemVoiceTxGain_Type = Integer32
_SystemVoiceTxGain_Object = MibTableColumn
systemVoiceTxGain = _SystemVoiceTxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 9),
    _SystemVoiceTxGain_Type()
)
systemVoiceTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceTxGain.setStatus("current")


class _SystemVoiceDtmfRelayMethod_Type(Integer32):
    """Custom type systemVoiceDtmfRelayMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfc2833", 1),
          ("sipInfo", 2))
    )


_SystemVoiceDtmfRelayMethod_Type.__name__ = "Integer32"
_SystemVoiceDtmfRelayMethod_Object = MibTableColumn
systemVoiceDtmfRelayMethod = _SystemVoiceDtmfRelayMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 10),
    _SystemVoiceDtmfRelayMethod_Type()
)
systemVoiceDtmfRelayMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceDtmfRelayMethod.setStatus("current")
_SystemVoiceDtmfRelayRxPayloadType_Type = Unsigned32
_SystemVoiceDtmfRelayRxPayloadType_Object = MibTableColumn
systemVoiceDtmfRelayRxPayloadType = _SystemVoiceDtmfRelayRxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 11),
    _SystemVoiceDtmfRelayRxPayloadType_Type()
)
systemVoiceDtmfRelayRxPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceDtmfRelayRxPayloadType.setStatus("current")


class _SystemVoiceDtmfRelayPayloadTypeNeg_Type(Integer32):
    """Custom type systemVoiceDtmfRelayPayloadTypeNeg based on Integer32"""
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


_SystemVoiceDtmfRelayPayloadTypeNeg_Type.__name__ = "Integer32"
_SystemVoiceDtmfRelayPayloadTypeNeg_Object = MibTableColumn
systemVoiceDtmfRelayPayloadTypeNeg = _SystemVoiceDtmfRelayPayloadTypeNeg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 12),
    _SystemVoiceDtmfRelayPayloadTypeNeg_Type()
)
systemVoiceDtmfRelayPayloadTypeNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceDtmfRelayPayloadTypeNeg.setStatus("current")
_SystemVoiceDtmfRelayTxPayloadType_Type = Unsigned32
_SystemVoiceDtmfRelayTxPayloadType_Object = MibTableColumn
systemVoiceDtmfRelayTxPayloadType = _SystemVoiceDtmfRelayTxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 1, 1, 13),
    _SystemVoiceDtmfRelayTxPayloadType_Type()
)
systemVoiceDtmfRelayTxPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceDtmfRelayTxPayloadType.setStatus("current")
_SystemVoiceCoderTable_Object = MibTable
systemVoiceCoderTable = _SystemVoiceCoderTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    systemVoiceCoderTable.setStatus("current")
_SystemVoiceCoderEntry_Object = MibTableRow
systemVoiceCoderEntry = _SystemVoiceCoderEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 2, 1)
)
systemVoiceCoderEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "systemVoiceCoderConfIdx"),
    (0, "RAD-Mpmx-MIB", "systemVoiceCoderPriority"),
)
if mibBuilder.loadTexts:
    systemVoiceCoderEntry.setStatus("current")
_SystemVoiceCoderConfIdx_Type = Unsigned32
_SystemVoiceCoderConfIdx_Object = MibTableColumn
systemVoiceCoderConfIdx = _SystemVoiceCoderConfIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 2, 1, 1),
    _SystemVoiceCoderConfIdx_Type()
)
systemVoiceCoderConfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemVoiceCoderConfIdx.setStatus("current")
_SystemVoiceCoderPriority_Type = Unsigned32
_SystemVoiceCoderPriority_Object = MibTableColumn
systemVoiceCoderPriority = _SystemVoiceCoderPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 2, 1, 2),
    _SystemVoiceCoderPriority_Type()
)
systemVoiceCoderPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemVoiceCoderPriority.setStatus("current")


class _SystemVoiceCoderCoderAndRate_Type(Integer32):
    """Custom type systemVoiceCoderCoderAndRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("g7231r6300BPS", 2),
          ("g7231r5300BPS", 3),
          ("g729A8KBPS", 4),
          ("g711aLAW", 5),
          ("g711uLAW", 6),
          ("none", 255))
    )


_SystemVoiceCoderCoderAndRate_Type.__name__ = "Integer32"
_SystemVoiceCoderCoderAndRate_Object = MibTableColumn
systemVoiceCoderCoderAndRate = _SystemVoiceCoderCoderAndRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 2, 12, 2, 1, 3),
    _SystemVoiceCoderCoderAndRate_Type()
)
systemVoiceCoderCoderAndRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemVoiceCoderCoderAndRate.setStatus("current")
_MdlWanGen_ObjectIdentity = ObjectIdentity
mdlWanGen = _MdlWanGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3)
)
_StatMdlGen_ObjectIdentity = ObjectIdentity
statMdlGen = _StatMdlGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1)
)
_MdlSInstTable_Object = MibTable
mdlSInstTable = _MdlSInstTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mdlSInstTable.setStatus("current")
_MdlSInstEntry_Object = MibTableRow
mdlSInstEntry = _MdlSInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1)
)
mdlSInstEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "mdlSInstSltIdx"),
)
if mibBuilder.loadTexts:
    mdlSInstEntry.setStatus("current")


class _MdlSInstSltIdx_Type(Integer32):
    """Custom type mdlSInstSltIdx based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_MdlSInstSltIdx_Type.__name__ = "Integer32"
_MdlSInstSltIdx_Object = MibTableColumn
mdlSInstSltIdx = _MdlSInstSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 1),
    _MdlSInstSltIdx_Type()
)
mdlSInstSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSInstSltIdx.setStatus("current")


class _MdlSInstCardType_Type(Integer32):
    """Custom type mdlSInstCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9,
              10,
              11,
              17,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              60,
              61,
              62,
              63,
              64,
              65,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              271,
              272,
              273,
              281,
              282,
              283,
              284,
              285,
              286,
              291,
              292,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("empty", 2),
          ("acm", 9),
          ("ps60W", 10),
          ("ps100W", 11),
          ("ps", 17),
          ("cl1", 20),
          ("clEth", 21),
          ("cl2", 22),
          ("cl2Eth", 23),
          ("cl3", 24),
          ("cl3Eth", 25),
          ("cl1Clk", 26),
          ("mPh1", 31),
          ("mPh3", 32),
          ("mPh1T1DSU", 33),
          ("mPh1T1CSU", 34),
          ("mPh1E1DSU", 35),
          ("mPh1E1LTU", 36),
          ("mtmlFT1", 37),
          ("mtmlFE1", 38),
          ("mtmlH4E1", 39),
          ("mtmlH4E12W", 40),
          ("mtmlH4T1", 41),
          ("mtmlH4T12W", 42),
          ("mtHsh4E1", 43),
          ("mtHsh4E12W", 44),
          ("mtHsh4T1", 45),
          ("mtHsh4T12W", 46),
          ("mtmlH2E1", 47),
          ("mtmlH2E12W", 48),
          ("mtmlH2T1", 49),
          ("mtmlH2T12W", 50),
          ("hsh2E1", 51),
          ("hsh2E12W", 52),
          ("hsh2T1", 53),
          ("hsh2T12W", 54),
          ("mlIp", 55),
          ("mtml4Ip", 56),
          ("ml20N1", 57),
          ("ml20N2", 58),
          ("mPl6", 60),
          ("mPl3", 61),
          ("vf24T1", 62),
          ("vf30E1", 63),
          ("vf48T1", 64),
          ("vf60E1", 65),
          ("ml2E1", 68),
          ("ml4E1", 69),
          ("ml2T1", 70),
          ("ml4T1", 71),
          ("mPv4", 72),
          ("vc16A", 73),
          ("vc8EandM", 74),
          ("vc8Fxo", 75),
          ("vc8Fxs", 76),
          ("vc16EandM", 77),
          ("vc16Fxo", 78),
          ("vc16Fxs", 79),
          ("vf3EandM", 80),
          ("vf3Fxs", 81),
          ("vf3Fxo", 82),
          ("vfPbx", 83),
          ("vfPbxT1", 84),
          ("vfPbxE1", 85),
          ("mtMlE2S", 86),
          ("mtMlE2D", 87),
          ("mtMlF2T1", 88),
          ("mtMlF2E1", 89),
          ("mtMlT1Fiber", 90),
          ("mtMlE1Fiber", 91),
          ("mtMlT1FiberFb", 92),
          ("mtMlE1FiberFb", 93),
          ("mtmlHE1", 94),
          ("mtmlH1E1", 95),
          ("mtmlHSE1", 96),
          ("ml20", 97),
          ("mtMl4T1", 98),
          ("mtMl4E1", 99),
          ("mtMl1T1DSU", 100),
          ("mtMl1T1CSU", 101),
          ("mtMl1E1DSU", 102),
          ("mtMl1E1LTU", 103),
          ("mtMl1T1DSUfb", 104),
          ("mtMl1T1CSUfb", 105),
          ("mtMl1E1DSUfb", 106),
          ("mtMl1E1LTUfb", 107),
          ("mtMl2T1", 108),
          ("mtMl2E1", 109),
          ("ls2CcittX50", 110),
          ("ls2CcittX58", 111),
          ("ls2ATandTSdm", 112),
          ("ls2ACcittX50", 113),
          ("ls2ACcittX58", 114),
          ("ls2AATandTSdm", 115),
          ("ls2A2Ts", 116),
          ("ls2M", 117),
          ("mtMlT1", 118),
          ("mtMlE1", 119),
          ("hs2", 120),
          ("hs3", 121),
          ("hsq", 122),
          ("hs703", 123),
          ("hsQM", 124),
          ("hsqN", 125),
          ("hs6", 126),
          ("hs12", 127),
          ("hsDp", 128),
          ("hsp", 129),
          ("hs4T1", 130),
          ("hs4E1", 131),
          ("hs4", 132),
          ("hsEth", 133),
          ("ml8T1", 134),
          ("ml8E1", 135),
          ("vc2E1", 136),
          ("vc4E1", 137),
          ("vc2T1", 138),
          ("vc4T1", 139),
          ("vc2EandM", 140),
          ("vc2Fxs1Plar", 141),
          ("vc2Fxo1", 142),
          ("vc2Fxs2", 143),
          ("vc2Fxo2", 144),
          ("vc2Fxs3", 145),
          ("vc2Fxo3", 146),
          ("vc26EandM", 147),
          ("mtvc2", 148),
          ("vc2R2Fxs", 149),
          ("hsu", 150),
          ("mbeA", 151),
          ("mbeB", 152),
          ("mbeU", 153),
          ("tre", 154),
          ("hsuI", 155),
          ("hsr", 156),
          ("hss", 157),
          ("hsu1", 158),
          ("ls12", 159),
          ("ls6", 160),
          ("ls6V1EandM", 161),
          ("ls6V1Fxo", 162),
          ("ls6V1Fxs", 163),
          ("ls6V2EandM", 164),
          ("ls6V2Fxo", 165),
          ("ls6V2Fxs", 166),
          ("ls6VfEandM", 167),
          ("ls6VfFxo", 168),
          ("ls6VfFxs", 169),
          ("vc3EandM", 170),
          ("vc3Fxo", 171),
          ("vc3Fxs", 172),
          ("vcPbx", 173),
          ("vcPbxT1", 174),
          ("vcPbxE1", 175),
          ("vc6EandM", 176),
          ("vc6Fxo", 177),
          ("vc6Fxs", 178),
          ("vcq", 179),
          ("ls6n", 180),
          ("mhs1V36", 181),
          ("mhs1V35", 182),
          ("mhs1G703", 183),
          ("mhs1DDS", 184),
          ("mhs3", 185),
          ("mhs1X21", 186),
          ("mhs1V24", 187),
          ("mhs4", 188),
          ("mhsE1Hs", 189),
          ("mhsT1Hs", 190),
          ("mhsHyE1Hs", 191),
          ("mhsHyT1Hs", 192),
          ("mlfHybE1Hs", 193),
          ("mlfHybT1Hs", 194),
          ("mhs2e1", 195),
          ("mhs2t1", 196),
          ("mhsHy2e1", 197),
          ("mhsHy2t1", 198),
          ("mlfHybE12", 199),
          ("mls6", 200),
          ("mls3", 201),
          ("mlHybAtmE1", 202),
          ("mlHybAtmT1", 203),
          ("mlfHybT12", 204),
          ("mvc8", 205),
          ("mvc8PbxE1", 206),
          ("mvc8PbxT1Dsu", 207),
          ("mvc8PbxT1Csu", 208),
          ("mvc8PbxE1Slave", 209),
          ("mvc4", 210),
          ("mvc4PbxE1", 211),
          ("mvc4PbxT1Dsu", 212),
          ("mvc4PbxT1Csu", 213),
          ("mvc4PbxE1Slave", 214),
          ("mvc4PbxT1Slave", 215),
          ("mvc8PbxT1Slave", 216),
          ("mvc8ExtAnalog", 217),
          ("mvcE1", 218),
          ("mvcT1", 219),
          ("mhsS", 220),
          ("mhsU", 221),
          ("mhsPriE1", 222),
          ("mhsPriT1", 223),
          ("hsEthSwitch", 224),
          ("mPriE1FramerCcs", 225),
          ("mPriT1FramerCcs", 226),
          ("mPriE1SlaveCcs", 227),
          ("mPriT1SlaveCcs", 228),
          ("mDualBri", 229),
          ("vc12EandM", 230),
          ("vc12Fxo", 231),
          ("vc12Fxs", 232),
          ("vc6aEandM", 233),
          ("vc6aFxo", 234),
          ("vc6aFxs", 235),
          ("vc6AgFxo", 236),
          ("vc6AgFxs", 237),
          ("vc6a4LB", 238),
          ("vid", 239),
          ("hsu12", 240),
          ("hsu6", 241),
          ("hss12", 242),
          ("hss6", 243),
          ("hsDp3", 244),
          ("hsDp6", 245),
          ("hsf1", 246),
          ("mhsHyE1", 247),
          ("mhsHyT1", 248),
          ("mhsIp", 249),
          ("mlIpHs", 250),
          ("mlHybIpE1", 251),
          ("mlHybIpT1", 252),
          ("mvg1Lan", 253),
          ("mvg2Lan", 254),
          ("vc4Fxs", 255),
          ("vc4EandM", 256),
          ("vc4Fxo", 257),
          ("hsf2", 258),
          ("mvgSwitch4Lan", 260),
          ("msl4E1W2", 261),
          ("msl4E1W4", 262),
          ("msl8E1W2", 263),
          ("msl4E1W2Eth", 264),
          ("msl8E1W2Eth", 265),
          ("asmi54cE1AndEth", 266),
          ("asmi54cT1AndEth", 267),
          ("asmi54c", 268),
          ("hs6N", 271),
          ("hs12N", 272),
          ("hsNRZ", 273),
          ("evc2E1", 281),
          ("evc4E1", 282),
          ("evc2T1", 283),
          ("evc4T1", 284),
          ("vc2E1Pri", 285),
          ("vc4E1Pri", 286),
          ("vc4OmniEandM", 291),
          ("vc4OmniWestern", 292),
          ("clx1", 301),
          ("clx1GbE", 302),
          ("clx1S155", 303),
          ("clx1S155GbE", 304),
          ("ml8T1Eth", 305),
          ("ml8E1Eth", 306),
          ("op106cEth", 307),
          ("op108cEth", 308),
          ("op106cEthT1", 309),
          ("op108cEthE1", 310),
          ("op108cEthE1Unbal", 311),
          ("mpw1", 312),
          ("vfs24T1", 321),
          ("vfs30E1", 322),
          ("vfs48T1", 323),
          ("vfs60E1", 324),
          ("mm4E1", 325),
          ("mm4T1", 326),
          ("mm8E1", 327),
          ("mm8T1", 328),
          ("mm12E1", 329),
          ("mm12T1", 330),
          ("mm16E1", 331),
          ("mm16T1", 332))
    )


_MdlSInstCardType_Type.__name__ = "Integer32"
_MdlSInstCardType_Object = MibTableColumn
mdlSInstCardType = _MdlSInstCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 2),
    _MdlSInstCardType_Type()
)
mdlSInstCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSInstCardType.setStatus("current")


class _MdlSHwVersion_Type(DisplayString):
    """Custom type mdlSHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlSHwVersion_Type.__name__ = "DisplayString"
_MdlSHwVersion_Object = MibTableColumn
mdlSHwVersion = _MdlSHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 3),
    _MdlSHwVersion_Type()
)
mdlSHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSHwVersion.setStatus("current")


class _MdlSSwVersion_Type(DisplayString):
    """Custom type mdlSSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlSSwVersion_Type.__name__ = "DisplayString"
_MdlSSwVersion_Object = MibTableColumn
mdlSSwVersion = _MdlSSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 4),
    _MdlSSwVersion_Type()
)
mdlSSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSSwVersion.setStatus("current")


class _MdlSAlrStatus_Type(Integer32):
    """Custom type mdlSAlrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_MdlSAlrStatus_Type.__name__ = "Integer32"
_MdlSAlrStatus_Object = MibTableColumn
mdlSAlrStatus = _MdlSAlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 5),
    _MdlSAlrStatus_Type()
)
mdlSAlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrStatus.setStatus("current")


class _MdlSAlrStatusAll_Type(Integer32):
    """Custom type mdlSAlrStatusAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_MdlSAlrStatusAll_Type.__name__ = "Integer32"
_MdlSAlrStatusAll_Object = MibTableColumn
mdlSAlrStatusAll = _MdlSAlrStatusAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 6),
    _MdlSAlrStatusAll_Type()
)
mdlSAlrStatusAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrStatusAll.setStatus("current")


class _MdlSMaskedAlrStat_Type(Integer32):
    """Custom type mdlSMaskedAlrStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_MdlSMaskedAlrStat_Type.__name__ = "Integer32"
_MdlSMaskedAlrStat_Object = MibTableColumn
mdlSMaskedAlrStat = _MdlSMaskedAlrStat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 7),
    _MdlSMaskedAlrStat_Type()
)
mdlSMaskedAlrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSMaskedAlrStat.setStatus("current")


class _MdlSMaskedAlrStatAll_Type(Integer32):
    """Custom type mdlSMaskedAlrStatAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_MdlSMaskedAlrStatAll_Type.__name__ = "Integer32"
_MdlSMaskedAlrStatAll_Object = MibTableColumn
mdlSMaskedAlrStatAll = _MdlSMaskedAlrStatAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 8),
    _MdlSMaskedAlrStatAll_Type()
)
mdlSMaskedAlrStatAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSMaskedAlrStatAll.setStatus("current")


class _MdlSTstStatusAll_Type(Integer32):
    """Custom type mdlSTstStatusAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSTstStatusAll_Type.__name__ = "Integer32"
_MdlSTstStatusAll_Object = MibTableColumn
mdlSTstStatusAll = _MdlSTstStatusAll_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 9),
    _MdlSTstStatusAll_Type()
)
mdlSTstStatusAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSTstStatusAll.setStatus("current")


class _MdlSClearAlrCmd_Type(Integer32):
    """Custom type mdlSClearAlrCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSClearAlrCmd_Type.__name__ = "Integer32"
_MdlSClearAlrCmd_Object = MibTableColumn
mdlSClearAlrCmd = _MdlSClearAlrCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 10),
    _MdlSClearAlrCmd_Type()
)
mdlSClearAlrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlSClearAlrCmd.setStatus("current")


class _MdlSClearAllAlrCmd_Type(Integer32):
    """Custom type mdlSClearAllAlrCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSClearAllAlrCmd_Type.__name__ = "Integer32"
_MdlSClearAllAlrCmd_Object = MibTableColumn
mdlSClearAllAlrCmd = _MdlSClearAllAlrCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 11),
    _MdlSClearAllAlrCmd_Type()
)
mdlSClearAllAlrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlSClearAllAlrCmd.setStatus("current")
_MdlSTemperature_Type = Integer32
_MdlSTemperature_Object = MibTableColumn
mdlSTemperature = _MdlSTemperature_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 1, 1, 12),
    _MdlSTemperature_Type()
)
mdlSTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSTemperature.setStatus("current")
_MdlSAlrTable_Object = MibTable
mdlSAlrTable = _MdlSAlrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    mdlSAlrTable.setStatus("current")
_MdlSAlrEntry_Object = MibTableRow
mdlSAlrEntry = _MdlSAlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1)
)
mdlSAlrEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "mdlSAlrSltIdx"),
    (0, "RAD-Mpmx-MIB", "mdlSAlrIdx"),
)
if mibBuilder.loadTexts:
    mdlSAlrEntry.setStatus("current")
_MdlSAlrIdx_Type = Integer32
_MdlSAlrIdx_Object = MibTableColumn
mdlSAlrIdx = _MdlSAlrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1, 1),
    _MdlSAlrIdx_Type()
)
mdlSAlrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrIdx.setStatus("current")


class _MdlSAlrSltIdx_Type(Integer32):
    """Custom type mdlSAlrSltIdx based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_MdlSAlrSltIdx_Type.__name__ = "Integer32"
_MdlSAlrSltIdx_Object = MibTableColumn
mdlSAlrSltIdx = _MdlSAlrSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1, 2),
    _MdlSAlrSltIdx_Type()
)
mdlSAlrSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrSltIdx.setStatus("current")


class _MdlSAlrCodeDescription_Type(DisplayString):
    """Custom type mdlSAlrCodeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdlSAlrCodeDescription_Type.__name__ = "DisplayString"
_MdlSAlrCodeDescription_Object = MibTableColumn
mdlSAlrCodeDescription = _MdlSAlrCodeDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1, 3),
    _MdlSAlrCodeDescription_Type()
)
mdlSAlrCodeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrCodeDescription.setStatus("current")
_MdlSAlrCode_Type = Integer32
_MdlSAlrCode_Object = MibTableColumn
mdlSAlrCode = _MdlSAlrCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1, 4),
    _MdlSAlrCode_Type()
)
mdlSAlrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrCode.setStatus("current")


class _MdlSAlrSeverity_Type(Integer32):
    """Custom type mdlSAlrSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_MdlSAlrSeverity_Type.__name__ = "Integer32"
_MdlSAlrSeverity_Object = MibTableColumn
mdlSAlrSeverity = _MdlSAlrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1, 5),
    _MdlSAlrSeverity_Type()
)
mdlSAlrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrSeverity.setStatus("current")


class _MdlSAlrState_Type(Integer32):
    """Custom type mdlSAlrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSAlrState_Type.__name__ = "Integer32"
_MdlSAlrState_Object = MibTableColumn
mdlSAlrState = _MdlSAlrState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1, 6),
    _MdlSAlrState_Type()
)
mdlSAlrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrState.setStatus("current")
_MdlSAlrCounter_Type = Integer32
_MdlSAlrCounter_Object = MibTableColumn
mdlSAlrCounter = _MdlSAlrCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1, 7),
    _MdlSAlrCounter_Type()
)
mdlSAlrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrCounter.setStatus("current")


class _MdlSAlrMask_Type(Integer32):
    """Custom type mdlSAlrMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSAlrMask_Type.__name__ = "Integer32"
_MdlSAlrMask_Object = MibTableColumn
mdlSAlrMask = _MdlSAlrMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1, 8),
    _MdlSAlrMask_Type()
)
mdlSAlrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrMask.setStatus("current")


class _MdlSAlrInvert_Type(Integer32):
    """Custom type mdlSAlrInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_MdlSAlrInvert_Type.__name__ = "Integer32"
_MdlSAlrInvert_Object = MibTableColumn
mdlSAlrInvert = _MdlSAlrInvert_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 1, 2, 1, 9),
    _MdlSAlrInvert_Type()
)
mdlSAlrInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlSAlrInvert.setStatus("current")
_CnfgMdlGen_ObjectIdentity = ObjectIdentity
cnfgMdlGen = _CnfgMdlGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2)
)
_MdlCPrgTable_Object = MibTable
mdlCPrgTable = _MdlCPrgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mdlCPrgTable.setStatus("current")
_MdlCPrgEntry_Object = MibTableRow
mdlCPrgEntry = _MdlCPrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1)
)
mdlCPrgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "mdlCCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "mdlCSltIdx"),
)
if mibBuilder.loadTexts:
    mdlCPrgEntry.setStatus("current")


class _MdlCCnfgIdx_Type(Integer32):
    """Custom type mdlCCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MdlCCnfgIdx_Type.__name__ = "Integer32"
_MdlCCnfgIdx_Object = MibTableColumn
mdlCCnfgIdx = _MdlCCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1, 1),
    _MdlCCnfgIdx_Type()
)
mdlCCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCCnfgIdx.setStatus("current")


class _MdlCSltIdx_Type(Integer32):
    """Custom type mdlCSltIdx based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_MdlCSltIdx_Type.__name__ = "Integer32"
_MdlCSltIdx_Object = MibTableColumn
mdlCSltIdx = _MdlCSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1, 2),
    _MdlCSltIdx_Type()
)
mdlCSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCSltIdx.setStatus("current")


class _MdlCPrgCardType_Type(Integer32):
    """Custom type mdlCPrgCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              60,
              62,
              63,
              64,
              65,
              68,
              69,
              70,
              71,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              271,
              272,
              273,
              281,
              282,
              283,
              284,
              285,
              286,
              291,
              292,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              340,
              341,
              342,
              343,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              370,
              371,
              372,
              373,
              374,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              401,
              411,
              412,
              413,
              414)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("empty", 2),
          ("acm", 9),
          ("ps48x60W", 10),
          ("ps48x100W", 11),
          ("ps110x60W", 12),
          ("ps110x100W", 13),
          ("ps220x60W", 14),
          ("ps220x100W", 15),
          ("ps180W", 16),
          ("ps", 17),
          ("cl1", 20),
          ("clEth", 21),
          ("cl2", 22),
          ("cl2Eth", 23),
          ("cl3", 24),
          ("cl3Eth", 25),
          ("cl1Clk", 26),
          ("mPh1", 31),
          ("mPh3", 32),
          ("mPh1T1DSU", 33),
          ("mPh1T1CSU", 34),
          ("mPh1E1DSU", 35),
          ("mPh1E1LTU", 36),
          ("mtmlFT1", 37),
          ("mtmlFE1", 38),
          ("mtmlH4E1", 39),
          ("mtmlH4E12W", 40),
          ("mtmlH4T1", 41),
          ("mtmlH4T12W", 42),
          ("mtHsh4E1", 43),
          ("mtHsh4E12W", 44),
          ("mtHsh4T1", 45),
          ("mtHsh4T12W", 46),
          ("mtmlH2E1", 47),
          ("mtmlH2E12W", 48),
          ("mtmlH2T1", 49),
          ("mtmlH2T12W", 50),
          ("hsh2E1", 51),
          ("hsh2E12W", 52),
          ("hsh2T1", 53),
          ("hsh2T12W", 54),
          ("mlIp", 55),
          ("mtml4Ip", 56),
          ("ml20N1", 57),
          ("ml20N2", 58),
          ("mPl6", 60),
          ("vf24T1", 62),
          ("vf30E1", 63),
          ("vf48T1", 64),
          ("vf60E1", 65),
          ("ml2E1", 68),
          ("ml4E1", 69),
          ("ml2T1", 70),
          ("ml4T1", 71),
          ("vc16A", 73),
          ("vc8EandM", 74),
          ("vc8Fxo", 75),
          ("vc8Fxs", 76),
          ("vc16EandM", 77),
          ("vc16Fxo", 78),
          ("vc16Fxs", 79),
          ("vf3EandM", 80),
          ("vf3Fxs", 81),
          ("vf3Fxo", 82),
          ("vfPbx", 83),
          ("vfPbxT1", 84),
          ("vfPbxE1", 85),
          ("mtMlE2S", 86),
          ("mtMlE2D", 87),
          ("mtMlF2T1", 88),
          ("mtMlF2E1", 89),
          ("mtMlT1Fiber", 90),
          ("mtMlE1Fiber", 91),
          ("mtMlT1FiberFb", 92),
          ("mtMlE1FiberFb", 93),
          ("mtmlHE1", 94),
          ("mtmlH1E1", 95),
          ("mtmlHSE1", 96),
          ("ml20", 97),
          ("mtMl4T1", 98),
          ("mtMl4E1", 99),
          ("mtMl1T1DSU", 100),
          ("mtMl1T1CSU", 101),
          ("mtMl1E1DSU", 102),
          ("mtMl1E1LTU", 103),
          ("mtMl1T1DSUfb", 104),
          ("mtMl1T1CSUfb", 105),
          ("mtMl1E1DSUfb", 106),
          ("mtMl1E1LTUfb", 107),
          ("mtMl2T1", 108),
          ("mtMl2E1", 109),
          ("ls2CcittX50", 110),
          ("ls2CcittX58", 111),
          ("ls2ATandTSdm", 112),
          ("ls2ACcittX50", 113),
          ("ls2ACcittX58", 114),
          ("ls2AATandTSdm", 115),
          ("ls2A2Ts", 116),
          ("ls2M", 117),
          ("mtMlT1", 118),
          ("mtMlE1", 119),
          ("hs2", 120),
          ("hs3", 121),
          ("hsq", 122),
          ("hs703", 123),
          ("hsQM", 124),
          ("hsqN", 125),
          ("hs6", 126),
          ("hs12", 127),
          ("hsDp", 128),
          ("hsp", 129),
          ("hs4T1", 130),
          ("hs4E1", 131),
          ("hsEth", 133),
          ("ml8T1", 134),
          ("ml8E1", 135),
          ("vc2E1", 136),
          ("vc4E1", 137),
          ("vc2T1", 138),
          ("vc4T1", 139),
          ("vc2EandM", 140),
          ("vc2Fxs1Plar", 141),
          ("vc2Fxo1", 142),
          ("vc2Fxs2", 143),
          ("vc2Fxo2", 144),
          ("vc2Fxs3", 145),
          ("vc2Fxo3", 146),
          ("vc26EandM", 147),
          ("mtvc2", 148),
          ("vc2R2Fxs", 149),
          ("hsu", 150),
          ("mbeA", 151),
          ("mbeB", 152),
          ("mbeU", 153),
          ("tre", 154),
          ("hsuI", 155),
          ("hsr", 156),
          ("hss", 157),
          ("hsu1", 158),
          ("ls12", 159),
          ("ls6", 160),
          ("ls6V1EandM", 161),
          ("ls6V1Fxo", 162),
          ("ls6V1Fxs", 163),
          ("ls6V2EandM", 164),
          ("ls6V2Fxo", 165),
          ("ls6V2Fxs", 166),
          ("ls6VfEandM", 167),
          ("ls6VfFxo", 168),
          ("ls6VfFxs", 169),
          ("vc3EandM", 170),
          ("vc3Fxo", 171),
          ("vc3Fxs", 172),
          ("vcPbx", 173),
          ("vcPbxT1", 174),
          ("vcPbxE1", 175),
          ("vc6EandM", 176),
          ("vc6Fxo", 177),
          ("vc6Fxs", 178),
          ("vcq", 179),
          ("ls6n", 180),
          ("mhs1V36", 181),
          ("mhs1V35", 182),
          ("mhs1G703", 183),
          ("mhs1DDS", 184),
          ("mhs3", 185),
          ("mhs1X21", 186),
          ("mhs1V24", 187),
          ("mhs4", 188),
          ("mhsE1Hs", 189),
          ("mhsT1Hs", 190),
          ("mhsHyE1Hs", 191),
          ("mhsHyT1Hs", 192),
          ("mlfHybE1Hs", 193),
          ("mlfHybT1Hs", 194),
          ("mhs2e1", 195),
          ("mhs2t1", 196),
          ("mhsHy2e1", 197),
          ("mhsHy2t1", 198),
          ("mlfHybE12", 199),
          ("mls6", 200),
          ("mls3", 201),
          ("mlHybAtmE1", 202),
          ("mlHybAtmT1", 203),
          ("mlfHybT12", 204),
          ("mvc8", 205),
          ("mvc8PbxE1", 206),
          ("mvc8PbxT1Dsu", 207),
          ("mvc8PbxT1Csu", 208),
          ("mvc8PbxE1Slave", 209),
          ("mvc4", 210),
          ("mvc4PbxE1", 211),
          ("mvc4PbxT1Dsu", 212),
          ("mvc4PbxT1Csu", 213),
          ("mvc4PbxE1Slave", 214),
          ("mvc4PbxT1Slave", 215),
          ("mvc8PbxT1Slave", 216),
          ("mvc8ExtAnalog", 217),
          ("mvcE1", 218),
          ("mvcT1", 219),
          ("mhsS", 220),
          ("mhsU", 221),
          ("mhsPriE1", 222),
          ("mhsPriT1", 223),
          ("hsEthSwitch", 224),
          ("mPriE1FramerCcs", 225),
          ("mPriT1FramerCcs", 226),
          ("mpriE1SlaveCcs", 227),
          ("mpriT1SlaveCcs", 228),
          ("mDualBri", 229),
          ("vc12EandM", 230),
          ("vc12Fxo", 231),
          ("vc12Fxs", 232),
          ("vc6aEandM", 233),
          ("vc6aFxo", 234),
          ("vc6aFxs", 235),
          ("vc6AgFxo", 236),
          ("vc6AgFxs", 237),
          ("vc6a4LB", 238),
          ("vid", 239),
          ("hsu12", 240),
          ("hsu6", 241),
          ("hss12", 242),
          ("hss6", 243),
          ("hsDp3", 244),
          ("hsDp6", 245),
          ("hsf1", 246),
          ("mhsHyE1", 247),
          ("mhsHyT1", 248),
          ("mhsIp", 249),
          ("mlIpHs", 250),
          ("mlHybIpE1", 251),
          ("mlHybIpT1", 252),
          ("mvg1Lan", 253),
          ("mvg2Lan", 254),
          ("vc4Fxs", 255),
          ("vc4EandM", 256),
          ("vc4Fxo", 257),
          ("hsf2", 258),
          ("mvgSwitch4Lan", 260),
          ("msl4E1W2", 261),
          ("msl4E1W4", 262),
          ("msl8E1W2", 263),
          ("msl4E1W2Eth", 264),
          ("msl8E1W2Eth", 265),
          ("asmi54cE1AndEth", 266),
          ("asmi54cT1AndEth", 267),
          ("asmi54c", 268),
          ("hs6N", 271),
          ("hs12N", 272),
          ("hsNRZ", 273),
          ("evc2E1", 281),
          ("evc4E1", 282),
          ("evc2T1", 283),
          ("evc4T1", 284),
          ("vc2E1Pri", 285),
          ("vc4E1Pri", 286),
          ("vc4OmniEandM", 291),
          ("vc4OmniWestern", 292),
          ("clx1", 301),
          ("clx1GbE", 302),
          ("clx1S155", 303),
          ("clx1S155GbE", 304),
          ("ml8T1Eth", 305),
          ("ml8E1Eth", 306),
          ("op106cEth", 307),
          ("op108cEth", 308),
          ("op106cEthT1", 309),
          ("op108cEthE1", 310),
          ("op108cEthE1Unbal", 311),
          ("mpw1", 312),
          ("op34c", 313),
          ("op25c", 314),
          ("op34cE1", 315),
          ("op25cT1", 316),
          ("m16e1", 317),
          ("m16t1", 318),
          ("op108cE1Unbal", 319),
          ("op108cE1Bal", 320),
          ("vfs24T1", 321),
          ("vfs30E1", 322),
          ("vfs48T1", 323),
          ("vfs60E1", 324),
          ("asmi54cE1N", 340),
          ("asmi54cN", 341),
          ("asmi54cHsN", 342),
          ("asmi54cHsAndEthN", 343),
          ("cl2n", 350),
          ("cl2GbE", 351),
          ("cl2s622", 352),
          ("cl2s622GbE", 353),
          ("cl2s622GbEa", 354),
          ("cl2GbEa", 355),
          ("cl2ds0", 356),
          ("cl2nl", 360),
          ("cl2GbEl", 361),
          ("cl2s622l", 362),
          ("cl2s622GbEl", 363),
          ("cl2s622GbEal", 364),
          ("cl2GbEal", 365),
          ("cl2ds0l", 366),
          ("mEth6", 370),
          ("mEth8", 371),
          ("mTp", 372),
          ("mT3", 373),
          ("mEthPoe", 374),
          ("mp4mSh16", 381),
          ("mp4mVs12", 382),
          ("mp4mVs6s37", 383),
          ("mp4mVs6Bin", 384),
          ("mp4mVs6E1T1", 385),
          ("mp4mE1T1", 386),
          ("mp4mT3", 387),
          ("mp4mVs6Fxs", 388),
          ("mp4mVs6Fxo", 389),
          ("mp4mVs6Em", 390),
          ("mp4mFxsEm", 391),
          ("mp4mshE1", 392),
          ("mp4mshE1Pw", 393),
          ("mp4mvs16E1Eop", 394),
          ("mp4mvs16T1Eop", 395),
          ("mp4mvs16E1Pw", 396),
          ("mp4mvs16T1Pw", 397),
          ("mp4mvs6S8E1Pw", 398),
          ("mp4mvs6S8T1Pw", 399),
          ("mp4mDnfv1", 401),
          ("mp4mvsG703", 411),
          ("mp4mVs6FxsPwAcr", 412),
          ("mp4mVs6FxoPwAcr", 413),
          ("mp4mVs6EmPwAcr", 414))
    )


_MdlCPrgCardType_Type.__name__ = "Integer32"
_MdlCPrgCardType_Object = MibTableColumn
mdlCPrgCardType = _MdlCPrgCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1, 3),
    _MdlCPrgCardType_Type()
)
mdlCPrgCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCPrgCardType.setStatus("current")
_MdlCNoOfExternPrt_Type = Integer32
_MdlCNoOfExternPrt_Object = MibTableColumn
mdlCNoOfExternPrt = _MdlCNoOfExternPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1, 4),
    _MdlCNoOfExternPrt_Type()
)
mdlCNoOfExternPrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCNoOfExternPrt.setStatus("current")
_MdlCNoOfInternPrt_Type = Integer32
_MdlCNoOfInternPrt_Object = MibTableColumn
mdlCNoOfInternPrt = _MdlCNoOfInternPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1, 5),
    _MdlCNoOfInternPrt_Type()
)
mdlCNoOfInternPrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCNoOfInternPrt.setStatus("current")


class _MdlCWorkMode_Type(Integer32):
    """Custom type mdlCWorkMode based on Integer32"""
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
          ("standAlone", 2),
          ("integrated", 3))
    )


_MdlCWorkMode_Type.__name__ = "Integer32"
_MdlCWorkMode_Object = MibTableColumn
mdlCWorkMode = _MdlCWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1, 6),
    _MdlCWorkMode_Type()
)
mdlCWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCWorkMode.setStatus("current")


class _MdlCDhcpClientEnable_Type(Integer32):
    """Custom type mdlCDhcpClientEnable based on Integer32"""
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


_MdlCDhcpClientEnable_Type.__name__ = "Integer32"
_MdlCDhcpClientEnable_Object = MibTableColumn
mdlCDhcpClientEnable = _MdlCDhcpClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1, 7),
    _MdlCDhcpClientEnable_Type()
)
mdlCDhcpClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCDhcpClientEnable.setStatus("current")


class _MdlCRdnExists_Type(Integer32):
    """Custom type mdlCRdnExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_MdlCRdnExists_Type.__name__ = "Integer32"
_MdlCRdnExists_Object = MibTableColumn
mdlCRdnExists = _MdlCRdnExists_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1, 8),
    _MdlCRdnExists_Type()
)
mdlCRdnExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCRdnExists.setStatus("current")
_MdlCInterfaces_Type = OctetString
_MdlCInterfaces_Object = MibTableColumn
mdlCInterfaces = _MdlCInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 2, 1, 1, 9),
    _MdlCInterfaces_Type()
)
mdlCInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCInterfaces.setStatus("current")
_CmprMdlGen_ObjectIdentity = ObjectIdentity
cmprMdlGen = _CmprMdlGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3)
)
_MdlCmprTable_Object = MibTable
mdlCmprTable = _MdlCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mdlCmprTable.setStatus("current")
_MdlCmprEntry_Object = MibTableRow
mdlCmprEntry = _MdlCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 1, 1)
)
mdlCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "mdlCmprTypIdx"),
    (0, "RAD-Mpmx-MIB", "mdlCmprCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "mdlCmprVersion"),
    (0, "RAD-Mpmx-MIB", "mdlCmprSltIdx"),
)
if mibBuilder.loadTexts:
    mdlCmprEntry.setStatus("current")
_MdlCmprTypIdx_Type = Integer32
_MdlCmprTypIdx_Object = MibTableColumn
mdlCmprTypIdx = _MdlCmprTypIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 1, 1, 1),
    _MdlCmprTypIdx_Type()
)
mdlCmprTypIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCmprTypIdx.setStatus("current")
_MdlCmprCnfgIdx_Type = Integer32
_MdlCmprCnfgIdx_Object = MibTableColumn
mdlCmprCnfgIdx = _MdlCmprCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 1, 1, 2),
    _MdlCmprCnfgIdx_Type()
)
mdlCmprCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCmprCnfgIdx.setStatus("current")
_MdlCmprVersion_Type = Integer32
_MdlCmprVersion_Object = MibTableColumn
mdlCmprVersion = _MdlCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 1, 1, 3),
    _MdlCmprVersion_Type()
)
mdlCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCmprVersion.setStatus("current")


class _MdlCmprSltIdx_Type(Integer32):
    """Custom type mdlCmprSltIdx based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_MdlCmprSltIdx_Type.__name__ = "Integer32"
_MdlCmprSltIdx_Object = MibTableColumn
mdlCmprSltIdx = _MdlCmprSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 1, 1, 4),
    _MdlCmprSltIdx_Type()
)
mdlCmprSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlCmprSltIdx.setStatus("current")
_MdlCmprObj_Type = OctetString
_MdlCmprObj_Object = MibTableColumn
mdlCmprObj = _MdlCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 1, 1, 5),
    _MdlCmprObj_Type()
)
mdlCmprObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlCmprObj.setStatus("current")
_MdlAlarmsCmprTable_Object = MibTable
mdlAlarmsCmprTable = _MdlAlarmsCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    mdlAlarmsCmprTable.setStatus("current")
_MdlAlarmsCmprEntry_Object = MibTableRow
mdlAlarmsCmprEntry = _MdlAlarmsCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 2, 1)
)
mdlAlarmsCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "mdlAlarmsCmprVersion"),
    (0, "RAD-Mpmx-MIB", "mdlAlarmsCmprAlarmSlot"),
    (0, "RAD-Mpmx-MIB", "mdlAlarmsCmprAlarmIdx"),
)
if mibBuilder.loadTexts:
    mdlAlarmsCmprEntry.setStatus("current")
_MdlAlarmsCmprVersion_Type = Integer32
_MdlAlarmsCmprVersion_Object = MibTableColumn
mdlAlarmsCmprVersion = _MdlAlarmsCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 2, 1, 1),
    _MdlAlarmsCmprVersion_Type()
)
mdlAlarmsCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlarmsCmprVersion.setStatus("current")
_MdlAlarmsCmprAlarmSlot_Type = Integer32
_MdlAlarmsCmprAlarmSlot_Object = MibTableColumn
mdlAlarmsCmprAlarmSlot = _MdlAlarmsCmprAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 2, 1, 2),
    _MdlAlarmsCmprAlarmSlot_Type()
)
mdlAlarmsCmprAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlarmsCmprAlarmSlot.setStatus("current")
_MdlAlarmsCmprAlarmIdx_Type = Integer32
_MdlAlarmsCmprAlarmIdx_Object = MibTableColumn
mdlAlarmsCmprAlarmIdx = _MdlAlarmsCmprAlarmIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 2, 1, 3),
    _MdlAlarmsCmprAlarmIdx_Type()
)
mdlAlarmsCmprAlarmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlAlarmsCmprAlarmIdx.setStatus("current")
_MdlAlarmsCmprObj_Type = OctetString
_MdlAlarmsCmprObj_Object = MibTableColumn
mdlAlarmsCmprObj = _MdlAlarmsCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 3, 3, 2, 1, 4),
    _MdlAlarmsCmprObj_Type()
)
mdlAlarmsCmprObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlAlarmsCmprObj.setStatus("current")
_PrtWanGen_ObjectIdentity = ObjectIdentity
prtWanGen = _PrtWanGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4)
)
_StatPrtGen_ObjectIdentity = ObjectIdentity
statPrtGen = _StatPrtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1)
)
_PrtSInstTable_Object = MibTable
prtSInstTable = _PrtSInstTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    prtSInstTable.setStatus("current")
_PrtSInstEntry_Object = MibTableRow
prtSInstEntry = _PrtSInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1)
)
prtSInstEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtSInstSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtSInstPrtIdx"),
)
if mibBuilder.loadTexts:
    prtSInstEntry.setStatus("current")


class _PrtSInstSltIdx_Type(Integer32):
    """Custom type prtSInstSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtSInstSltIdx_Type.__name__ = "Integer32"
_PrtSInstSltIdx_Object = MibTableColumn
prtSInstSltIdx = _PrtSInstSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 1),
    _PrtSInstSltIdx_Type()
)
prtSInstSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSInstSltIdx.setStatus("current")
_PrtSInstPrtIdx_Type = Integer32
_PrtSInstPrtIdx_Object = MibTableColumn
prtSInstPrtIdx = _PrtSInstPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 2),
    _PrtSInstPrtIdx_Type()
)
prtSInstPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSInstPrtIdx.setStatus("current")


class _PrtSInstPrtType_Type(Integer32):
    """Custom type prtSInstPrtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 3),
          ("highSpeedV35", 4),
          ("highSpeedV24", 5),
          ("highSpeedV36", 6),
          ("highSpeedX21", 7),
          ("highSpeedG703", 8),
          ("highSpeedDDS", 9),
          ("lowSpeed", 10),
          ("voice", 11),
          ("cl", 12),
          ("isdns", 13),
          ("isdnu", 14),
          ("ethernet", 15),
          ("voiceS0", 16),
          ("voiceU", 17),
          ("voiceQsigS", 18),
          ("voiceQsigU", 19))
    )


_PrtSInstPrtType_Type.__name__ = "Integer32"
_PrtSInstPrtType_Object = MibTableColumn
prtSInstPrtType = _PrtSInstPrtType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 3),
    _PrtSInstPrtType_Type()
)
prtSInstPrtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSInstPrtType.setStatus("current")
_PrtSInstIfIndex_Type = Integer32
_PrtSInstIfIndex_Object = MibTableColumn
prtSInstIfIndex = _PrtSInstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 4),
    _PrtSInstIfIndex_Type()
)
prtSInstIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSInstIfIndex.setStatus("current")


class _PrtSActiveStatus_Type(Integer32):
    """Custom type prtSActiveStatus based on Integer32"""
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
        *(("unknown", 1),
          ("notUsed", 2),
          ("offLine", 3),
          ("onLine", 4),
          ("offLineRedundancy", 5),
          ("onLineRedundancy", 6))
    )


_PrtSActiveStatus_Type.__name__ = "Integer32"
_PrtSActiveStatus_Object = MibTableColumn
prtSActiveStatus = _PrtSActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 5),
    _PrtSActiveStatus_Type()
)
prtSActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSActiveStatus.setStatus("current")


class _PrtSAlrStatus_Type(Integer32):
    """Custom type prtSAlrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_PrtSAlrStatus_Type.__name__ = "Integer32"
_PrtSAlrStatus_Object = MibTableColumn
prtSAlrStatus = _PrtSAlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 6),
    _PrtSAlrStatus_Type()
)
prtSAlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrStatus.setStatus("current")


class _PrtSMaskedAlrStat_Type(Integer32):
    """Custom type prtSMaskedAlrStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_PrtSMaskedAlrStat_Type.__name__ = "Integer32"
_PrtSMaskedAlrStat_Object = MibTableColumn
prtSMaskedAlrStat = _PrtSMaskedAlrStat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 7),
    _PrtSMaskedAlrStat_Type()
)
prtSMaskedAlrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSMaskedAlrStat.setStatus("current")


class _PrtSClearAlrCmd_Type(Integer32):
    """Custom type prtSClearAlrCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtSClearAlrCmd_Type.__name__ = "Integer32"
_PrtSClearAlrCmd_Object = MibTableColumn
prtSClearAlrCmd = _PrtSClearAlrCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 8),
    _PrtSClearAlrCmd_Type()
)
prtSClearAlrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSClearAlrCmd.setStatus("current")
_PrtSTestMask_Type = Integer32
_PrtSTestMask_Object = MibTableColumn
prtSTestMask = _PrtSTestMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 9),
    _PrtSTestMask_Type()
)
prtSTestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSTestMask.setStatus("current")


class _PrtSTstCmd_Type(Integer32):
    """Custom type prtSTstCmd based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("localLoop", 2),
          ("remoteLoop", 3),
          ("locAndRemMainLoops", 4),
          ("remoteAnalogLoop", 5),
          ("remoteDigitalLoop", 6),
          ("remLoopOnExtUnit", 7),
          ("bert", 8),
          ("toneInjection", 9),
          ("dlciLocalLoop", 10),
          ("allDlciLocalLoop", 11),
          ("dlciRemoteLoop", 12),
          ("allDlciRemoteLoop", 13),
          ("extInitLocalLoop", 14),
          ("bertAndRemLoopOnRemUnit", 15),
          ("remLoopOnRemUnit", 16),
          ("block", 17),
          ("backwardToneInject", 18),
          ("llb", 19),
          ("rlb", 20),
          ("ft1Enable", 21),
          ("lbbd", 22),
          ("lb1", 23),
          ("lb2", 24),
          ("llbOnRemUnit", 25),
          ("bertOnRemUnit", 26),
          ("bertOnRemAndLlbOnRemUnit", 27),
          ("localAndBertOnRemUnit", 28),
          ("localLoopOnRemUnit", 29),
          ("localBert", 30),
          ("testPerTS", 31),
          ("csuLoopAndBert", 32),
          ("dsuLoopAndBert", 33),
          ("remoteOcuLoopAndBert", 34),
          ("remoteCsuLoopAndBert", 35),
          ("remoteDsuLoopAndBert", 36))
    )


_PrtSTstCmd_Type.__name__ = "Integer32"
_PrtSTstCmd_Object = MibTableColumn
prtSTstCmd = _PrtSTstCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 10),
    _PrtSTstCmd_Type()
)
prtSTstCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSTstCmd.setStatus("current")
_PrtSTstDuration_Type = Integer32
_PrtSTstDuration_Object = MibTableColumn
prtSTstDuration = _PrtSTstDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 11),
    _PrtSTstDuration_Type()
)
prtSTstDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSTstDuration.setStatus("current")


class _PrtSBertClrCmd_Type(Integer32):
    """Custom type prtSBertClrCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtSBertClrCmd_Type.__name__ = "Integer32"
_PrtSBertClrCmd_Object = MibTableColumn
prtSBertClrCmd = _PrtSBertClrCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 12),
    _PrtSBertClrCmd_Type()
)
prtSBertClrCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSBertClrCmd.setStatus("current")
_PrtSBertTstRslt_Type = Integer32
_PrtSBertTstRslt_Object = MibTableColumn
prtSBertTstRslt = _PrtSBertTstRslt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 13),
    _PrtSBertTstRslt_Type()
)
prtSBertTstRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSBertTstRslt.setStatus("current")


class _PrtSInterfaceType_Type(DisplayString):
    """Custom type prtSInterfaceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtSInterfaceType_Type.__name__ = "DisplayString"
_PrtSInterfaceType_Object = MibTableColumn
prtSInterfaceType = _PrtSInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 14),
    _PrtSInterfaceType_Type()
)
prtSInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSInterfaceType.setStatus("current")
_PrtSParamStatus_Type = OctetString
_PrtSParamStatus_Object = MibTableColumn
prtSParamStatus = _PrtSParamStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 15),
    _PrtSParamStatus_Type()
)
prtSParamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSParamStatus.setStatus("current")
_PrtSTestMaskXp_Type = OctetString
_PrtSTestMaskXp_Object = MibTableColumn
prtSTestMaskXp = _PrtSTestMaskXp_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 16),
    _PrtSTestMaskXp_Type()
)
prtSTestMaskXp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtSTestMaskXp.setStatus("current")


class _PrtSRdnStatus_Type(Integer32):
    """Custom type prtSRdnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRdn", 1),
          ("offline", 2),
          ("online", 3))
    )


_PrtSRdnStatus_Type.__name__ = "Integer32"
_PrtSRdnStatus_Object = MibTableColumn
prtSRdnStatus = _PrtSRdnStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 1, 1, 17),
    _PrtSRdnStatus_Type()
)
prtSRdnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSRdnStatus.setStatus("current")
_PrtSAlrTable_Object = MibTable
prtSAlrTable = _PrtSAlrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    prtSAlrTable.setStatus("current")
_PrtSAlrEntry_Object = MibTableRow
prtSAlrEntry = _PrtSAlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1)
)
prtSAlrEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtSAlrSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtSAlrPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtSAlrIdx"),
)
if mibBuilder.loadTexts:
    prtSAlrEntry.setStatus("current")
_PrtSAlrIdx_Type = Integer32
_PrtSAlrIdx_Object = MibTableColumn
prtSAlrIdx = _PrtSAlrIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 1),
    _PrtSAlrIdx_Type()
)
prtSAlrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrIdx.setStatus("current")


class _PrtSAlrSltIdx_Type(Integer32):
    """Custom type prtSAlrSltIdx based on Integer32"""
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
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtSAlrSltIdx_Type.__name__ = "Integer32"
_PrtSAlrSltIdx_Object = MibTableColumn
prtSAlrSltIdx = _PrtSAlrSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 2),
    _PrtSAlrSltIdx_Type()
)
prtSAlrSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrSltIdx.setStatus("current")
_PrtSAlrPrtIdx_Type = Integer32
_PrtSAlrPrtIdx_Object = MibTableColumn
prtSAlrPrtIdx = _PrtSAlrPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 3),
    _PrtSAlrPrtIdx_Type()
)
prtSAlrPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrPrtIdx.setStatus("current")


class _PrtSAlrCodeDescription_Type(DisplayString):
    """Custom type prtSAlrCodeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrtSAlrCodeDescription_Type.__name__ = "DisplayString"
_PrtSAlrCodeDescription_Object = MibTableColumn
prtSAlrCodeDescription = _PrtSAlrCodeDescription_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 4),
    _PrtSAlrCodeDescription_Type()
)
prtSAlrCodeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrCodeDescription.setStatus("current")
_PrtSAlrCode_Type = Integer32
_PrtSAlrCode_Object = MibTableColumn
prtSAlrCode = _PrtSAlrCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 5),
    _PrtSAlrCode_Type()
)
prtSAlrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrCode.setStatus("current")


class _PrtSAlrSeverity_Type(Integer32):
    """Custom type prtSAlrSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_PrtSAlrSeverity_Type.__name__ = "Integer32"
_PrtSAlrSeverity_Object = MibTableColumn
prtSAlrSeverity = _PrtSAlrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 6),
    _PrtSAlrSeverity_Type()
)
prtSAlrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrSeverity.setStatus("current")


class _PrtSAlrState_Type(Integer32):
    """Custom type prtSAlrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtSAlrState_Type.__name__ = "Integer32"
_PrtSAlrState_Object = MibTableColumn
prtSAlrState = _PrtSAlrState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 7),
    _PrtSAlrState_Type()
)
prtSAlrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrState.setStatus("current")
_PrtSAlrCounter_Type = Integer32
_PrtSAlrCounter_Object = MibTableColumn
prtSAlrCounter = _PrtSAlrCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 8),
    _PrtSAlrCounter_Type()
)
prtSAlrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrCounter.setStatus("current")


class _PrtSAlrMask_Type(Integer32):
    """Custom type prtSAlrMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtSAlrMask_Type.__name__ = "Integer32"
_PrtSAlrMask_Object = MibTableColumn
prtSAlrMask = _PrtSAlrMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 9),
    _PrtSAlrMask_Type()
)
prtSAlrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrMask.setStatus("current")


class _PrtSAlrInvert_Type(Integer32):
    """Custom type prtSAlrInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtSAlrInvert_Type.__name__ = "Integer32"
_PrtSAlrInvert_Object = MibTableColumn
prtSAlrInvert = _PrtSAlrInvert_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 10),
    _PrtSAlrInvert_Type()
)
prtSAlrInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrInvert.setStatus("current")


class _PrtSAlrCardType_Type(Integer32):
    """Custom type prtSAlrCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              17,
              20,
              26,
              62,
              63,
              64,
              65,
              74,
              75,
              76,
              77,
              78,
              79,
              134,
              135,
              156,
              159,
              180,
              224,
              240,
              241,
              255,
              256,
              257,
              261,
              263,
              264,
              265,
              266,
              267,
              268,
              271,
              272,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              321,
              322,
              323,
              324)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("empty", 2),
          ("ps", 17),
          ("cl1", 20),
          ("cl1Clk", 26),
          ("vf24T1", 62),
          ("vf30E1", 63),
          ("vf48T1", 64),
          ("vf60E1", 65),
          ("vc8EandM", 74),
          ("vc8Fxo", 75),
          ("vc8Fxs", 76),
          ("vc16EandM", 77),
          ("vc16Fxo", 78),
          ("vc16Fxs", 79),
          ("ml8T1", 134),
          ("ml8E1", 135),
          ("hsr", 156),
          ("ls12", 159),
          ("ls6n", 180),
          ("hsEthSwitch", 224),
          ("hsu12", 240),
          ("hsu6", 241),
          ("vc4Fxs", 255),
          ("vc4EandM", 256),
          ("vc4Fxo", 257),
          ("msl4E1W2", 261),
          ("msl8E1W2", 263),
          ("msl4E1W2Eth", 264),
          ("msl8E1W2Eth", 265),
          ("asmi54cE1AndEth", 266),
          ("asmi54cT1AndEth", 267),
          ("asmi54c", 268),
          ("hs6N", 271),
          ("hs12N", 272),
          ("clx1", 301),
          ("clx1GbE", 302),
          ("clx1S155", 303),
          ("clx1S155GbE", 304),
          ("ml8T1Eth", 305),
          ("ml8E1Eth", 306),
          ("op106cEth", 307),
          ("op108cEth", 308),
          ("op106cEthT1", 309),
          ("op108cEthE1", 310),
          ("op108cEthE1Unbal", 311),
          ("mpw1", 312),
          ("vfs24T1", 321),
          ("vfs30E1", 322),
          ("vfs48T1", 323),
          ("vfs60E1", 324))
    )


_PrtSAlrCardType_Type.__name__ = "Integer32"
_PrtSAlrCardType_Object = MibTableColumn
prtSAlrCardType = _PrtSAlrCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 2, 1, 11),
    _PrtSAlrCardType_Type()
)
prtSAlrCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSAlrCardType.setStatus("current")
_StatisPrtGen_ObjectIdentity = ObjectIdentity
statisPrtGen = _StatisPrtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3)
)
_PrtFrStatis_ObjectIdentity = ObjectIdentity
prtFrStatis = _PrtFrStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1)
)
_PrtFrStatisTable_Object = MibTable
prtFrStatisTable = _PrtFrStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    prtFrStatisTable.setStatus("current")
_PrtFrStatisEntry_Object = MibTableRow
prtFrStatisEntry = _PrtFrStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1)
)
prtFrStatisEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtFrStatisSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtFrStatisPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtFrStatisInvIdx"),
)
if mibBuilder.loadTexts:
    prtFrStatisEntry.setStatus("current")


class _PrtFrStatisSltIdx_Type(Integer32):
    """Custom type prtFrStatisSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtFrStatisSltIdx_Type.__name__ = "Integer32"
_PrtFrStatisSltIdx_Object = MibTableColumn
prtFrStatisSltIdx = _PrtFrStatisSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 1),
    _PrtFrStatisSltIdx_Type()
)
prtFrStatisSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrStatisSltIdx.setStatus("current")


class _PrtFrStatisPrtIdx_Type(Integer32):
    """Custom type prtFrStatisPrtIdx based on Integer32"""
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
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6))
    )


_PrtFrStatisPrtIdx_Type.__name__ = "Integer32"
_PrtFrStatisPrtIdx_Object = MibTableColumn
prtFrStatisPrtIdx = _PrtFrStatisPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 2),
    _PrtFrStatisPrtIdx_Type()
)
prtFrStatisPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrStatisPrtIdx.setStatus("current")


class _PrtFrStatisInvIdx_Type(Integer32):
    """Custom type prtFrStatisInvIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentInv", 1),
          ("last", 2))
    )


_PrtFrStatisInvIdx_Type.__name__ = "Integer32"
_PrtFrStatisInvIdx_Object = MibTableColumn
prtFrStatisInvIdx = _PrtFrStatisInvIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 3),
    _PrtFrStatisInvIdx_Type()
)
prtFrStatisInvIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrStatisInvIdx.setStatus("current")


class _PrtFrTimeElapsed_Type(Integer32):
    """Custom type prtFrTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_PrtFrTimeElapsed_Type.__name__ = "Integer32"
_PrtFrTimeElapsed_Object = MibTableColumn
prtFrTimeElapsed = _PrtFrTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 4),
    _PrtFrTimeElapsed_Type()
)
prtFrTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTimeElapsed.setStatus("current")
_PrtFrRxTotalFrames_Type = Counter32
_PrtFrRxTotalFrames_Object = MibTableColumn
prtFrRxTotalFrames = _PrtFrRxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 5),
    _PrtFrRxTotalFrames_Type()
)
prtFrRxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxTotalFrames.setStatus("current")
_PrtFrTxTotalFrames_Type = Counter32
_PrtFrTxTotalFrames_Object = MibTableColumn
prtFrTxTotalFrames = _PrtFrTxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 6),
    _PrtFrTxTotalFrames_Type()
)
prtFrTxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxTotalFrames.setStatus("current")
_PrtFrRxTotalBytes_Type = Counter32
_PrtFrRxTotalBytes_Object = MibTableColumn
prtFrRxTotalBytes = _PrtFrRxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 7),
    _PrtFrRxTotalBytes_Type()
)
prtFrRxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxTotalBytes.setStatus("current")
_PrtFrTxTotalBytes_Type = Counter32
_PrtFrTxTotalBytes_Object = MibTableColumn
prtFrTxTotalBytes = _PrtFrTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 8),
    _PrtFrTxTotalBytes_Type()
)
prtFrTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxTotalBytes.setStatus("current")
_PrtFrRxMngFrames_Type = Counter32
_PrtFrRxMngFrames_Object = MibTableColumn
prtFrRxMngFrames = _PrtFrRxMngFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 9),
    _PrtFrRxMngFrames_Type()
)
prtFrRxMngFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxMngFrames.setStatus("current")
_PrtFrTxMngFrames_Type = Counter32
_PrtFrTxMngFrames_Object = MibTableColumn
prtFrTxMngFrames = _PrtFrTxMngFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 10),
    _PrtFrTxMngFrames_Type()
)
prtFrTxMngFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxMngFrames.setStatus("current")
_PrtFrRxDeFrames_Type = Counter32
_PrtFrRxDeFrames_Object = MibTableColumn
prtFrRxDeFrames = _PrtFrRxDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 11),
    _PrtFrRxDeFrames_Type()
)
prtFrRxDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxDeFrames.setStatus("current")
_PrtFrTxDeFrames_Type = Counter32
_PrtFrTxDeFrames_Object = MibTableColumn
prtFrTxDeFrames = _PrtFrTxDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 12),
    _PrtFrTxDeFrames_Type()
)
prtFrTxDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxDeFrames.setStatus("current")
_PrtFrRxDcrdCongDeFr_Type = Counter32
_PrtFrRxDcrdCongDeFr_Object = MibTableColumn
prtFrRxDcrdCongDeFr = _PrtFrRxDcrdCongDeFr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 13),
    _PrtFrRxDcrdCongDeFr_Type()
)
prtFrRxDcrdCongDeFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxDcrdCongDeFr.setStatus("current")
_PrtFrTxDcrdCongDeFr_Type = Counter32
_PrtFrTxDcrdCongDeFr_Object = MibTableColumn
prtFrTxDcrdCongDeFr = _PrtFrTxDcrdCongDeFr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 14),
    _PrtFrTxDcrdCongDeFr_Type()
)
prtFrTxDcrdCongDeFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxDcrdCongDeFr.setStatus("current")
_PrtFrRxDcrdCongAllFr_Type = Counter32
_PrtFrRxDcrdCongAllFr_Object = MibTableColumn
prtFrRxDcrdCongAllFr = _PrtFrRxDcrdCongAllFr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 15),
    _PrtFrRxDcrdCongAllFr_Type()
)
prtFrRxDcrdCongAllFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxDcrdCongAllFr.setStatus("current")
_PrtFrTxDcrdCongAllFr_Type = Counter32
_PrtFrTxDcrdCongAllFr_Object = MibTableColumn
prtFrTxDcrdCongAllFr = _PrtFrTxDcrdCongAllFr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 16),
    _PrtFrTxDcrdCongAllFr_Type()
)
prtFrTxDcrdCongAllFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxDcrdCongAllFr.setStatus("current")
_PrtFrRxFecn_Type = Counter32
_PrtFrRxFecn_Object = MibTableColumn
prtFrRxFecn = _PrtFrRxFecn_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 17),
    _PrtFrRxFecn_Type()
)
prtFrRxFecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxFecn.setStatus("current")
_PrtFrTxFecn_Type = Counter32
_PrtFrTxFecn_Object = MibTableColumn
prtFrTxFecn = _PrtFrTxFecn_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 18),
    _PrtFrTxFecn_Type()
)
prtFrTxFecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxFecn.setStatus("current")
_PrtFrRxBecn_Type = Counter32
_PrtFrRxBecn_Object = MibTableColumn
prtFrRxBecn = _PrtFrRxBecn_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 19),
    _PrtFrRxBecn_Type()
)
prtFrRxBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxBecn.setStatus("current")
_PrtFrTxBecn_Type = Counter32
_PrtFrTxBecn_Object = MibTableColumn
prtFrTxBecn = _PrtFrTxBecn_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 20),
    _PrtFrTxBecn_Type()
)
prtFrTxBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxBecn.setStatus("current")
_PrtFrRxBeViol_Type = Counter32
_PrtFrRxBeViol_Object = MibTableColumn
prtFrRxBeViol = _PrtFrRxBeViol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 21),
    _PrtFrRxBeViol_Type()
)
prtFrRxBeViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxBeViol.setStatus("current")
_PrtFrTxBeViol_Type = Counter32
_PrtFrTxBeViol_Object = MibTableColumn
prtFrTxBeViol = _PrtFrTxBeViol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 22),
    _PrtFrTxBeViol_Type()
)
prtFrTxBeViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxBeViol.setStatus("current")
_PrtFrRxBcViol_Type = Counter32
_PrtFrRxBcViol_Object = MibTableColumn
prtFrRxBcViol = _PrtFrRxBcViol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 23),
    _PrtFrRxBcViol_Type()
)
prtFrRxBcViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrRxBcViol.setStatus("current")
_PrtFrTxBcViol_Type = Counter32
_PrtFrTxBcViol_Object = MibTableColumn
prtFrTxBcViol = _PrtFrTxBcViol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 1, 1, 1, 24),
    _PrtFrTxBcViol_Type()
)
prtFrTxBcViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrTxBcViol.setStatus("current")
_PrtCrStatis_ObjectIdentity = ObjectIdentity
prtCrStatis = _PrtCrStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2)
)
_PrtCrStatisTable_Object = MibTable
prtCrStatisTable = _PrtCrStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    prtCrStatisTable.setStatus("current")
_PrtCrStatisEntry_Object = MibTableRow
prtCrStatisEntry = _PrtCrStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1, 1)
)
prtCrStatisEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtCrStatisSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtCrStatisPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtCrStatisInvIdx"),
)
if mibBuilder.loadTexts:
    prtCrStatisEntry.setStatus("current")


class _PrtCrStatisSltIdx_Type(Integer32):
    """Custom type prtCrStatisSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtCrStatisSltIdx_Type.__name__ = "Integer32"
_PrtCrStatisSltIdx_Object = MibTableColumn
prtCrStatisSltIdx = _PrtCrStatisSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1, 1, 1),
    _PrtCrStatisSltIdx_Type()
)
prtCrStatisSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCrStatisSltIdx.setStatus("current")


class _PrtCrStatisPrtIdx_Type(Integer32):
    """Custom type prtCrStatisPrtIdx based on Integer32"""
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
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6))
    )


_PrtCrStatisPrtIdx_Type.__name__ = "Integer32"
_PrtCrStatisPrtIdx_Object = MibTableColumn
prtCrStatisPrtIdx = _PrtCrStatisPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1, 1, 2),
    _PrtCrStatisPrtIdx_Type()
)
prtCrStatisPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCrStatisPrtIdx.setStatus("current")


class _PrtCrStatisInvIdx_Type(Integer32):
    """Custom type prtCrStatisInvIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentInv", 1),
          ("last", 2))
    )


_PrtCrStatisInvIdx_Type.__name__ = "Integer32"
_PrtCrStatisInvIdx_Object = MibTableColumn
prtCrStatisInvIdx = _PrtCrStatisInvIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1, 1, 3),
    _PrtCrStatisInvIdx_Type()
)
prtCrStatisInvIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCrStatisInvIdx.setStatus("current")


class _PrtCrTimeElapsed_Type(Integer32):
    """Custom type prtCrTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_PrtCrTimeElapsed_Type.__name__ = "Integer32"
_PrtCrTimeElapsed_Object = MibTableColumn
prtCrTimeElapsed = _PrtCrTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1, 1, 4),
    _PrtCrTimeElapsed_Type()
)
prtCrTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCrTimeElapsed.setStatus("current")
_PrtCrRxTotalCells_Type = Counter32
_PrtCrRxTotalCells_Object = MibTableColumn
prtCrRxTotalCells = _PrtCrRxTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1, 1, 5),
    _PrtCrRxTotalCells_Type()
)
prtCrRxTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCrRxTotalCells.setStatus("current")
_PrtCrTxTotalCells_Type = Counter32
_PrtCrTxTotalCells_Object = MibTableColumn
prtCrTxTotalCells = _PrtCrTxTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1, 1, 6),
    _PrtCrTxTotalCells_Type()
)
prtCrTxTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCrTxTotalCells.setStatus("current")
_PrtCrRxDataCells_Type = Counter32
_PrtCrRxDataCells_Object = MibTableColumn
prtCrRxDataCells = _PrtCrRxDataCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1, 1, 7),
    _PrtCrRxDataCells_Type()
)
prtCrRxDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCrRxDataCells.setStatus("current")
_PrtCrTxDataCells_Type = Counter32
_PrtCrTxDataCells_Object = MibTableColumn
prtCrTxDataCells = _PrtCrTxDataCells_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 2, 1, 1, 8),
    _PrtCrTxDataCells_Type()
)
prtCrTxDataCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCrTxDataCells.setStatus("current")
_PrtDlciStatis_ObjectIdentity = ObjectIdentity
prtDlciStatis = _PrtDlciStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3)
)
_PrtDlciStatisTable_Object = MibTable
prtDlciStatisTable = _PrtDlciStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    prtDlciStatisTable.setStatus("current")
_PrtDlciStatisEntry_Object = MibTableRow
prtDlciStatisEntry = _PrtDlciStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1)
)
prtDlciStatisEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtDlciSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtDlciPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtDlciIdx"),
)
if mibBuilder.loadTexts:
    prtDlciStatisEntry.setStatus("current")


class _PrtDlciSltIdx_Type(Integer32):
    """Custom type prtDlciSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtDlciSltIdx_Type.__name__ = "Integer32"
_PrtDlciSltIdx_Object = MibTableColumn
prtDlciSltIdx = _PrtDlciSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 1),
    _PrtDlciSltIdx_Type()
)
prtDlciSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciSltIdx.setStatus("current")


class _PrtDlciPrtIdx_Type(Integer32):
    """Custom type prtDlciPrtIdx based on Integer32"""
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
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6))
    )


_PrtDlciPrtIdx_Type.__name__ = "Integer32"
_PrtDlciPrtIdx_Object = MibTableColumn
prtDlciPrtIdx = _PrtDlciPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 2),
    _PrtDlciPrtIdx_Type()
)
prtDlciPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciPrtIdx.setStatus("current")


class _PrtDlciIdx_Type(Integer32):
    """Custom type prtDlciIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 991),
    )


_PrtDlciIdx_Type.__name__ = "Integer32"
_PrtDlciIdx_Object = MibTableColumn
prtDlciIdx = _PrtDlciIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 3),
    _PrtDlciIdx_Type()
)
prtDlciIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciIdx.setStatus("current")
_PrtDlciRxDeFrames_Type = Counter32
_PrtDlciRxDeFrames_Object = MibTableColumn
prtDlciRxDeFrames = _PrtDlciRxDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 4),
    _PrtDlciRxDeFrames_Type()
)
prtDlciRxDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciRxDeFrames.setStatus("current")
_PrtDlciTxDeFrames_Type = Counter32
_PrtDlciTxDeFrames_Object = MibTableColumn
prtDlciTxDeFrames = _PrtDlciTxDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 5),
    _PrtDlciTxDeFrames_Type()
)
prtDlciTxDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciTxDeFrames.setStatus("current")
_PrtDlciRxDcrdCongDeFr_Type = Counter32
_PrtDlciRxDcrdCongDeFr_Object = MibTableColumn
prtDlciRxDcrdCongDeFr = _PrtDlciRxDcrdCongDeFr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 6),
    _PrtDlciRxDcrdCongDeFr_Type()
)
prtDlciRxDcrdCongDeFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciRxDcrdCongDeFr.setStatus("current")
_PrtDlciTxDcrdCongDeFr_Type = Counter32
_PrtDlciTxDcrdCongDeFr_Object = MibTableColumn
prtDlciTxDcrdCongDeFr = _PrtDlciTxDcrdCongDeFr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 7),
    _PrtDlciTxDcrdCongDeFr_Type()
)
prtDlciTxDcrdCongDeFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciTxDcrdCongDeFr.setStatus("current")
_PrtDlciRxDcrdCongAllFr_Type = Counter32
_PrtDlciRxDcrdCongAllFr_Object = MibTableColumn
prtDlciRxDcrdCongAllFr = _PrtDlciRxDcrdCongAllFr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 8),
    _PrtDlciRxDcrdCongAllFr_Type()
)
prtDlciRxDcrdCongAllFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciRxDcrdCongAllFr.setStatus("current")
_PrtDlciTxDcrdCongAllFr_Type = Counter32
_PrtDlciTxDcrdCongAllFr_Object = MibTableColumn
prtDlciTxDcrdCongAllFr = _PrtDlciTxDcrdCongAllFr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 9),
    _PrtDlciTxDcrdCongAllFr_Type()
)
prtDlciTxDcrdCongAllFr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciTxDcrdCongAllFr.setStatus("current")
_PrtDlciTxFecn_Type = Counter32
_PrtDlciTxFecn_Object = MibTableColumn
prtDlciTxFecn = _PrtDlciTxFecn_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 10),
    _PrtDlciTxFecn_Type()
)
prtDlciTxFecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciTxFecn.setStatus("current")
_PrtDlciTxBecn_Type = Counter32
_PrtDlciTxBecn_Object = MibTableColumn
prtDlciTxBecn = _PrtDlciTxBecn_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 11),
    _PrtDlciTxBecn_Type()
)
prtDlciTxBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciTxBecn.setStatus("current")
_PrtDlciRxBeViol_Type = Counter32
_PrtDlciRxBeViol_Object = MibTableColumn
prtDlciRxBeViol = _PrtDlciRxBeViol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 12),
    _PrtDlciRxBeViol_Type()
)
prtDlciRxBeViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciRxBeViol.setStatus("current")
_PrtDlciTxBeViol_Type = Counter32
_PrtDlciTxBeViol_Object = MibTableColumn
prtDlciTxBeViol = _PrtDlciTxBeViol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 13),
    _PrtDlciTxBeViol_Type()
)
prtDlciTxBeViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciTxBeViol.setStatus("current")
_PrtDlciRxBcViol_Type = Counter32
_PrtDlciRxBcViol_Object = MibTableColumn
prtDlciRxBcViol = _PrtDlciRxBcViol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 14),
    _PrtDlciRxBcViol_Type()
)
prtDlciRxBcViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciRxBcViol.setStatus("current")
_PrtDlciTxBcViol_Type = Counter32
_PrtDlciTxBcViol_Object = MibTableColumn
prtDlciTxBcViol = _PrtDlciTxBcViol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 3, 1, 1, 15),
    _PrtDlciTxBcViol_Type()
)
prtDlciTxBcViol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciTxBcViol.setStatus("current")
_PrtT1Statis_ObjectIdentity = ObjectIdentity
prtT1Statis = _PrtT1Statis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 4)
)
_PrtT1FdlMsgTable_Object = MibTable
prtT1FdlMsgTable = _PrtT1FdlMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    prtT1FdlMsgTable.setStatus("current")
_PrtT1FdlMsgEntry_Object = MibTableRow
prtT1FdlMsgEntry = _PrtT1FdlMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 4, 1, 1)
)
prtT1FdlMsgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtT1FdlMsgSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtT1FdlMsgPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtT1FdlMsgFdlTxRx"),
)
if mibBuilder.loadTexts:
    prtT1FdlMsgEntry.setStatus("current")


class _PrtT1FdlMsgSltIdx_Type(Integer32):
    """Custom type prtT1FdlMsgSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtT1FdlMsgSltIdx_Type.__name__ = "Integer32"
_PrtT1FdlMsgSltIdx_Object = MibTableColumn
prtT1FdlMsgSltIdx = _PrtT1FdlMsgSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 4, 1, 1, 1),
    _PrtT1FdlMsgSltIdx_Type()
)
prtT1FdlMsgSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1FdlMsgSltIdx.setStatus("current")


class _PrtT1FdlMsgPrtIdx_Type(Integer32):
    """Custom type prtT1FdlMsgPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exPrt1", 1)
    )


_PrtT1FdlMsgPrtIdx_Type.__name__ = "Integer32"
_PrtT1FdlMsgPrtIdx_Object = MibTableColumn
prtT1FdlMsgPrtIdx = _PrtT1FdlMsgPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 4, 1, 1, 2),
    _PrtT1FdlMsgPrtIdx_Type()
)
prtT1FdlMsgPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1FdlMsgPrtIdx.setStatus("current")


class _PrtT1FdlMsgFdlTxRx_Type(Integer32):
    """Custom type prtT1FdlMsgFdlTxRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2))
    )


_PrtT1FdlMsgFdlTxRx_Type.__name__ = "Integer32"
_PrtT1FdlMsgFdlTxRx_Object = MibTableColumn
prtT1FdlMsgFdlTxRx = _PrtT1FdlMsgFdlTxRx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 4, 1, 1, 3),
    _PrtT1FdlMsgFdlTxRx_Type()
)
prtT1FdlMsgFdlTxRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1FdlMsgFdlTxRx.setStatus("current")
_PrtT1FdlMsg_Type = OctetString
_PrtT1FdlMsg_Object = MibTableColumn
prtT1FdlMsg = _PrtT1FdlMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 1, 3, 4, 1, 1, 4),
    _PrtT1FdlMsg_Type()
)
prtT1FdlMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtT1FdlMsg.setStatus("current")
_CnfgPrtGen_ObjectIdentity = ObjectIdentity
cnfgPrtGen = _CnfgPrtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2)
)
_PrtExTsSplitTable_Object = MibTable
prtExTsSplitTable = _PrtExTsSplitTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    prtExTsSplitTable.setStatus("current")
_PrtExTsSplitEntry_Object = MibTableRow
prtExTsSplitEntry = _PrtExTsSplitEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1)
)
prtExTsSplitEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExTsCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExTsSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExTsPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtExTsIdx"),
    (0, "RAD-Mpmx-MIB", "prtExTsBit"),
)
if mibBuilder.loadTexts:
    prtExTsSplitEntry.setStatus("current")


class _PrtExTsCnfgIdx_Type(Integer32):
    """Custom type prtExTsCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExTsCnfgIdx_Type.__name__ = "Integer32"
_PrtExTsCnfgIdx_Object = MibTableColumn
prtExTsCnfgIdx = _PrtExTsCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 1),
    _PrtExTsCnfgIdx_Type()
)
prtExTsCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTsCnfgIdx.setStatus("current")


class _PrtExTsSltIdx_Type(Integer32):
    """Custom type prtExTsSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExTsSltIdx_Type.__name__ = "Integer32"
_PrtExTsSltIdx_Object = MibTableColumn
prtExTsSltIdx = _PrtExTsSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 2),
    _PrtExTsSltIdx_Type()
)
prtExTsSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTsSltIdx.setStatus("current")
_PrtExTsPrtIdx_Type = Integer32
_PrtExTsPrtIdx_Object = MibTableColumn
prtExTsPrtIdx = _PrtExTsPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 3),
    _PrtExTsPrtIdx_Type()
)
prtExTsPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTsPrtIdx.setStatus("current")
_PrtExTsIdx_Type = Integer32
_PrtExTsIdx_Object = MibTableColumn
prtExTsIdx = _PrtExTsIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 4),
    _PrtExTsIdx_Type()
)
prtExTsIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTsIdx.setStatus("current")
_PrtExTsBit_Type = Integer32
_PrtExTsBit_Object = MibTableColumn
prtExTsBit = _PrtExTsBit_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 5),
    _PrtExTsBit_Type()
)
prtExTsBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTsBit.setStatus("current")


class _PrtExTsIConSlot_Type(Integer32):
    """Custom type prtExTsIConSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExTsIConSlot_Type.__name__ = "Integer32"
_PrtExTsIConSlot_Object = MibTableColumn
prtExTsIConSlot = _PrtExTsIConSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 6),
    _PrtExTsIConSlot_Type()
)
prtExTsIConSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExTsIConSlot.setStatus("current")
_PrtExTsIConPrt_Type = Integer32
_PrtExTsIConPrt_Object = MibTableColumn
prtExTsIConPrt = _PrtExTsIConPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 7),
    _PrtExTsIConPrt_Type()
)
prtExTsIConPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExTsIConPrt.setStatus("current")


class _PrtExTsBitTest_Type(Integer32):
    """Custom type prtExTsBitTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              30,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remoteBert", 8),
          ("localBert", 30),
          ("notApplicable", 255))
    )


_PrtExTsBitTest_Type.__name__ = "Integer32"
_PrtExTsBitTest_Object = MibTableColumn
prtExTsBitTest = _PrtExTsBitTest_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 8),
    _PrtExTsBitTest_Type()
)
prtExTsBitTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExTsBitTest.setStatus("current")
_PrtExTsTxSignaling_Type = OctetString
_PrtExTsTxSignaling_Object = MibTableColumn
prtExTsTxSignaling = _PrtExTsTxSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 9),
    _PrtExTsTxSignaling_Type()
)
prtExTsTxSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTsTxSignaling.setStatus("current")
_PrtExTsRxSignaling_Type = OctetString
_PrtExTsRxSignaling_Object = MibTableColumn
prtExTsRxSignaling = _PrtExTsRxSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 10),
    _PrtExTsRxSignaling_Type()
)
prtExTsRxSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTsRxSignaling.setStatus("current")
_PrtExTsTxIoSignaling_Type = OctetString
_PrtExTsTxIoSignaling_Object = MibTableColumn
prtExTsTxIoSignaling = _PrtExTsTxIoSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 11),
    _PrtExTsTxIoSignaling_Type()
)
prtExTsTxIoSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTsTxIoSignaling.setStatus("current")
_PrtExTsRxIoSignaling_Type = OctetString
_PrtExTsRxIoSignaling_Object = MibTableColumn
prtExTsRxIoSignaling = _PrtExTsRxIoSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 1, 1, 12),
    _PrtExTsRxIoSignaling_Type()
)
prtExTsRxIoSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTsRxIoSignaling.setStatus("current")
_PrtCnfgAgenda_ObjectIdentity = ObjectIdentity
prtCnfgAgenda = _PrtCnfgAgenda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2)
)
_PrtAgendaBehaviourTable_Object = MibTable
prtAgendaBehaviourTable = _PrtAgendaBehaviourTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    prtAgendaBehaviourTable.setStatus("current")
_PrtAgendaBehaviourEntry_Object = MibTableRow
prtAgendaBehaviourEntry = _PrtAgendaBehaviourEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 1, 1)
)
prtAgendaBehaviourEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtAgendaBehaviourCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtAgendaBehaviourSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtAgendaBehaviourPrtIdx"),
)
if mibBuilder.loadTexts:
    prtAgendaBehaviourEntry.setStatus("current")


class _PrtAgendaBehaviourCnfgIdx_Type(Integer32):
    """Custom type prtAgendaBehaviourCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtAgendaBehaviourCnfgIdx_Type.__name__ = "Integer32"
_PrtAgendaBehaviourCnfgIdx_Object = MibTableColumn
prtAgendaBehaviourCnfgIdx = _PrtAgendaBehaviourCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 1, 1, 1),
    _PrtAgendaBehaviourCnfgIdx_Type()
)
prtAgendaBehaviourCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAgendaBehaviourCnfgIdx.setStatus("current")
_PrtAgendaBehaviourSltIdx_Type = Integer32
_PrtAgendaBehaviourSltIdx_Object = MibTableColumn
prtAgendaBehaviourSltIdx = _PrtAgendaBehaviourSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 1, 1, 2),
    _PrtAgendaBehaviourSltIdx_Type()
)
prtAgendaBehaviourSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAgendaBehaviourSltIdx.setStatus("current")
_PrtAgendaBehaviourPrtIdx_Type = Integer32
_PrtAgendaBehaviourPrtIdx_Object = MibTableColumn
prtAgendaBehaviourPrtIdx = _PrtAgendaBehaviourPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 1, 1, 3),
    _PrtAgendaBehaviourPrtIdx_Type()
)
prtAgendaBehaviourPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAgendaBehaviourPrtIdx.setStatus("current")


class _PrtAgendaBehaviourOnOff_Type(Integer32):
    """Custom type prtAgendaBehaviourOnOff based on Integer32"""
    defaultValue = 2

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
          ("off", 2),
          ("on", 3))
    )


_PrtAgendaBehaviourOnOff_Type.__name__ = "Integer32"
_PrtAgendaBehaviourOnOff_Object = MibTableColumn
prtAgendaBehaviourOnOff = _PrtAgendaBehaviourOnOff_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 1, 1, 4),
    _PrtAgendaBehaviourOnOff_Type()
)
prtAgendaBehaviourOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtAgendaBehaviourOnOff.setStatus("current")
_PrtCnfgAgendaTable_Object = MibTable
prtCnfgAgendaTable = _PrtCnfgAgendaTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    prtCnfgAgendaTable.setStatus("current")
_PrtCnfgAgendaEntry_Object = MibTableRow
prtCnfgAgendaEntry = _PrtCnfgAgendaEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 2, 1)
)
prtCnfgAgendaEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtCnfgAgendaCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtCnfgAgendaSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtCnfgAgendaPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtCnfgAgendaDayIdx"),
    (0, "RAD-Mpmx-MIB", "prtCnfgAgendaSesId"),
)
if mibBuilder.loadTexts:
    prtCnfgAgendaEntry.setStatus("current")


class _PrtCnfgAgendaCnfgIdx_Type(Integer32):
    """Custom type prtCnfgAgendaCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtCnfgAgendaCnfgIdx_Type.__name__ = "Integer32"
_PrtCnfgAgendaCnfgIdx_Object = MibTableColumn
prtCnfgAgendaCnfgIdx = _PrtCnfgAgendaCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 2, 1, 1),
    _PrtCnfgAgendaCnfgIdx_Type()
)
prtCnfgAgendaCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCnfgAgendaCnfgIdx.setStatus("current")
_PrtCnfgAgendaSltIdx_Type = Integer32
_PrtCnfgAgendaSltIdx_Object = MibTableColumn
prtCnfgAgendaSltIdx = _PrtCnfgAgendaSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 2, 1, 2),
    _PrtCnfgAgendaSltIdx_Type()
)
prtCnfgAgendaSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCnfgAgendaSltIdx.setStatus("current")
_PrtCnfgAgendaPrtIdx_Type = Integer32
_PrtCnfgAgendaPrtIdx_Object = MibTableColumn
prtCnfgAgendaPrtIdx = _PrtCnfgAgendaPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 2, 1, 3),
    _PrtCnfgAgendaPrtIdx_Type()
)
prtCnfgAgendaPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCnfgAgendaPrtIdx.setStatus("current")


class _PrtCnfgAgendaDayIdx_Type(Integer32):
    """Custom type prtCnfgAgendaDayIdx based on Integer32"""
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
        *(("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6),
          ("sunday", 7))
    )


_PrtCnfgAgendaDayIdx_Type.__name__ = "Integer32"
_PrtCnfgAgendaDayIdx_Object = MibTableColumn
prtCnfgAgendaDayIdx = _PrtCnfgAgendaDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 2, 1, 4),
    _PrtCnfgAgendaDayIdx_Type()
)
prtCnfgAgendaDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCnfgAgendaDayIdx.setStatus("current")


class _PrtCnfgAgendaSesId_Type(Integer32):
    """Custom type prtCnfgAgendaSesId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PrtCnfgAgendaSesId_Type.__name__ = "Integer32"
_PrtCnfgAgendaSesId_Object = MibTableColumn
prtCnfgAgendaSesId = _PrtCnfgAgendaSesId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 2, 1, 5),
    _PrtCnfgAgendaSesId_Type()
)
prtCnfgAgendaSesId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCnfgAgendaSesId.setStatus("current")


class _PrtCnfgAgendaFrom_Type(Integer32):
    """Custom type prtCnfgAgendaFrom based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PrtCnfgAgendaFrom_Type.__name__ = "Integer32"
_PrtCnfgAgendaFrom_Object = MibTableColumn
prtCnfgAgendaFrom = _PrtCnfgAgendaFrom_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 2, 1, 6),
    _PrtCnfgAgendaFrom_Type()
)
prtCnfgAgendaFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCnfgAgendaFrom.setStatus("current")


class _PrtCnfgAgendaTo_Type(Integer32):
    """Custom type prtCnfgAgendaTo based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PrtCnfgAgendaTo_Type.__name__ = "Integer32"
_PrtCnfgAgendaTo_Object = MibTableColumn
prtCnfgAgendaTo = _PrtCnfgAgendaTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 2, 2, 1, 7),
    _PrtCnfgAgendaTo_Type()
)
prtCnfgAgendaTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCnfgAgendaTo.setStatus("current")
_PrtGenCnfgTable_Object = MibTable
prtGenCnfgTable = _PrtGenCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    prtGenCnfgTable.setStatus("current")
_PrtGenCnfgEntry_Object = MibTableRow
prtGenCnfgEntry = _PrtGenCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1)
)
prtGenCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtGenCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtGenCnfgSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtGenCnfgPrtIdx"),
)
if mibBuilder.loadTexts:
    prtGenCnfgEntry.setStatus("current")


class _PrtGenCnfgIdx_Type(Integer32):
    """Custom type prtGenCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtGenCnfgIdx_Type.__name__ = "Integer32"
_PrtGenCnfgIdx_Object = MibTableColumn
prtGenCnfgIdx = _PrtGenCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 1),
    _PrtGenCnfgIdx_Type()
)
prtGenCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenCnfgIdx.setStatus("current")


class _PrtGenCnfgSltIdx_Type(Integer32):
    """Custom type prtGenCnfgSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtGenCnfgSltIdx_Type.__name__ = "Integer32"
_PrtGenCnfgSltIdx_Object = MibTableColumn
prtGenCnfgSltIdx = _PrtGenCnfgSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 2),
    _PrtGenCnfgSltIdx_Type()
)
prtGenCnfgSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenCnfgSltIdx.setStatus("current")
_PrtGenCnfgPrtIdx_Type = Integer32
_PrtGenCnfgPrtIdx_Object = MibTableColumn
prtGenCnfgPrtIdx = _PrtGenCnfgPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 3),
    _PrtGenCnfgPrtIdx_Type()
)
prtGenCnfgPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtGenCnfgPrtIdx.setStatus("current")


class _PrtGenCnfgLinkToSlot_Type(Integer32):
    """Custom type prtGenCnfgLinkToSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtGenCnfgLinkToSlot_Type.__name__ = "Integer32"
_PrtGenCnfgLinkToSlot_Object = MibTableColumn
prtGenCnfgLinkToSlot = _PrtGenCnfgLinkToSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 4),
    _PrtGenCnfgLinkToSlot_Type()
)
prtGenCnfgLinkToSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenCnfgLinkToSlot.setStatus("current")
_PrtGenCnfgLinkToPort_Type = Integer32
_PrtGenCnfgLinkToPort_Object = MibTableColumn
prtGenCnfgLinkToPort = _PrtGenCnfgLinkToPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 5),
    _PrtGenCnfgLinkToPort_Type()
)
prtGenCnfgLinkToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenCnfgLinkToPort.setStatus("current")


class _PrtGenCnfgPortId_Type(Integer32):
    """Custom type prtGenCnfgPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_PrtGenCnfgPortId_Type.__name__ = "Integer32"
_PrtGenCnfgPortId_Object = MibTableColumn
prtGenCnfgPortId = _PrtGenCnfgPortId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 6),
    _PrtGenCnfgPortId_Type()
)
prtGenCnfgPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenCnfgPortId.setStatus("current")


class _PrtGenCnfgBusConnection_Type(Integer32):
    """Custom type prtGenCnfgBusConnection based on Integer32"""
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
        *(("notApplicable", 1),
          ("partial", 2),
          ("full", 3),
          ("partialCD", 4))
    )


_PrtGenCnfgBusConnection_Type.__name__ = "Integer32"
_PrtGenCnfgBusConnection_Object = MibTableColumn
prtGenCnfgBusConnection = _PrtGenCnfgBusConnection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 7),
    _PrtGenCnfgBusConnection_Type()
)
prtGenCnfgBusConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenCnfgBusConnection.setStatus("current")


class _PrtGenCnfgInbandMng_Type(Integer32):
    """Custom type prtGenCnfgInbandMng based on Integer32"""
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
          ("off", 2),
          ("on", 3))
    )


_PrtGenCnfgInbandMng_Type.__name__ = "Integer32"
_PrtGenCnfgInbandMng_Object = MibTableColumn
prtGenCnfgInbandMng = _PrtGenCnfgInbandMng_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 8),
    _PrtGenCnfgInbandMng_Type()
)
prtGenCnfgInbandMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenCnfgInbandMng.setStatus("current")


class _PrtGenCnfgInbandMngRoutProt_Type(Integer32):
    """Custom type prtGenCnfgInbandMngRoutProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rip2", 2),
          ("proprietaryRip", 3),
          ("notApplicable", 255))
    )


_PrtGenCnfgInbandMngRoutProt_Type.__name__ = "Integer32"
_PrtGenCnfgInbandMngRoutProt_Object = MibTableColumn
prtGenCnfgInbandMngRoutProt = _PrtGenCnfgInbandMngRoutProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 9),
    _PrtGenCnfgInbandMngRoutProt_Type()
)
prtGenCnfgInbandMngRoutProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenCnfgInbandMngRoutProt.setStatus("current")


class _PrtGenCnfgProtectionMode_Type(Integer32):
    """Custom type prtGenCnfgProtectionMode based on Integer32"""
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
          ("secondary", 2),
          ("primary", 3))
    )


_PrtGenCnfgProtectionMode_Type.__name__ = "Integer32"
_PrtGenCnfgProtectionMode_Object = MibTableColumn
prtGenCnfgProtectionMode = _PrtGenCnfgProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 10),
    _PrtGenCnfgProtectionMode_Type()
)
prtGenCnfgProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenCnfgProtectionMode.setStatus("current")


class _PrtGenCnfgConnect_Type(Integer32):
    """Custom type prtGenCnfgConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtGenCnfgConnect_Type.__name__ = "Integer32"
_PrtGenCnfgConnect_Object = MibTableColumn
prtGenCnfgConnect = _PrtGenCnfgConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 11),
    _PrtGenCnfgConnect_Type()
)
prtGenCnfgConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenCnfgConnect.setStatus("current")


class _PrtGenCnfgSignalingType_Type(Integer32):
    """Custom type prtGenCnfgSignalingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("legacy", 3),
          ("abcd", 4),
          ("none", 5))
    )


_PrtGenCnfgSignalingType_Type.__name__ = "Integer32"
_PrtGenCnfgSignalingType_Object = MibTableColumn
prtGenCnfgSignalingType = _PrtGenCnfgSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 2, 3, 1, 12),
    _PrtGenCnfgSignalingType_Type()
)
prtGenCnfgSignalingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtGenCnfgSignalingType.setStatus("current")
_CmprPrtGen_ObjectIdentity = ObjectIdentity
cmprPrtGen = _CmprPrtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3)
)
_PrtCmprTable_Object = MibTable
prtCmprTable = _PrtCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    prtCmprTable.setStatus("current")
_PrtCmprEntry_Object = MibTableRow
prtCmprEntry = _PrtCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 1, 1)
)
prtCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtCmprTypIdx"),
    (0, "RAD-Mpmx-MIB", "prtCmprCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtCmprVersion"),
    (0, "RAD-Mpmx-MIB", "prtCmprSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtCmprPrtIdx"),
)
if mibBuilder.loadTexts:
    prtCmprEntry.setStatus("current")
_PrtCmprTypIdx_Type = Integer32
_PrtCmprTypIdx_Object = MibTableColumn
prtCmprTypIdx = _PrtCmprTypIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 1, 1, 1),
    _PrtCmprTypIdx_Type()
)
prtCmprTypIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCmprTypIdx.setStatus("current")
_PrtCmprCnfgIdx_Type = Integer32
_PrtCmprCnfgIdx_Object = MibTableColumn
prtCmprCnfgIdx = _PrtCmprCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 1, 1, 2),
    _PrtCmprCnfgIdx_Type()
)
prtCmprCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCmprCnfgIdx.setStatus("current")
_PrtCmprVersion_Type = Integer32
_PrtCmprVersion_Object = MibTableColumn
prtCmprVersion = _PrtCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 1, 1, 3),
    _PrtCmprVersion_Type()
)
prtCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCmprVersion.setStatus("current")


class _PrtCmprSltIdx_Type(Integer32):
    """Custom type prtCmprSltIdx based on Integer32"""
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
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtCmprSltIdx_Type.__name__ = "Integer32"
_PrtCmprSltIdx_Object = MibTableColumn
prtCmprSltIdx = _PrtCmprSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 1, 1, 4),
    _PrtCmprSltIdx_Type()
)
prtCmprSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCmprSltIdx.setStatus("current")
_PrtCmprPrtIdx_Type = Integer32
_PrtCmprPrtIdx_Object = MibTableColumn
prtCmprPrtIdx = _PrtCmprPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 1, 1, 5),
    _PrtCmprPrtIdx_Type()
)
prtCmprPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCmprPrtIdx.setStatus("current")
_PrtCmprObj_Type = OctetString
_PrtCmprObj_Object = MibTableColumn
prtCmprObj = _PrtCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 1, 1, 6),
    _PrtCmprObj_Type()
)
prtCmprObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtCmprObj.setStatus("current")
_PrtCmprStatisticObj_Type = OctetString
_PrtCmprStatisticObj_Object = MibTableColumn
prtCmprStatisticObj = _PrtCmprStatisticObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 1, 1, 7),
    _PrtCmprStatisticObj_Type()
)
prtCmprStatisticObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtCmprStatisticObj.setStatus("current")
_PrtDlciCmprTable_Object = MibTable
prtDlciCmprTable = _PrtDlciCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    prtDlciCmprTable.setStatus("current")
_PrtDlciCmprEntry_Object = MibTableRow
prtDlciCmprEntry = _PrtDlciCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 2, 1)
)
prtDlciCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtDlciCmprCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtDlciCmprVersion"),
    (0, "RAD-Mpmx-MIB", "prtDlciCmprSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtDlciCmprPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtDlciCmprDlciIdx"),
)
if mibBuilder.loadTexts:
    prtDlciCmprEntry.setStatus("current")
_PrtDlciCmprCnfgIdx_Type = Integer32
_PrtDlciCmprCnfgIdx_Object = MibTableColumn
prtDlciCmprCnfgIdx = _PrtDlciCmprCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 2, 1, 1),
    _PrtDlciCmprCnfgIdx_Type()
)
prtDlciCmprCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciCmprCnfgIdx.setStatus("current")
_PrtDlciCmprVersion_Type = Integer32
_PrtDlciCmprVersion_Object = MibTableColumn
prtDlciCmprVersion = _PrtDlciCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 2, 1, 2),
    _PrtDlciCmprVersion_Type()
)
prtDlciCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciCmprVersion.setStatus("current")


class _PrtDlciCmprSltIdx_Type(Integer32):
    """Custom type prtDlciCmprSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtDlciCmprSltIdx_Type.__name__ = "Integer32"
_PrtDlciCmprSltIdx_Object = MibTableColumn
prtDlciCmprSltIdx = _PrtDlciCmprSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 2, 1, 3),
    _PrtDlciCmprSltIdx_Type()
)
prtDlciCmprSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciCmprSltIdx.setStatus("current")


class _PrtDlciCmprPrtIdx_Type(Integer32):
    """Custom type prtDlciCmprPrtIdx based on Integer32"""
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
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108),
          ("inPrt9", 109),
          ("inPrt10", 110),
          ("inPrt11", 111),
          ("inPrt12", 112))
    )


_PrtDlciCmprPrtIdx_Type.__name__ = "Integer32"
_PrtDlciCmprPrtIdx_Object = MibTableColumn
prtDlciCmprPrtIdx = _PrtDlciCmprPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 2, 1, 4),
    _PrtDlciCmprPrtIdx_Type()
)
prtDlciCmprPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciCmprPrtIdx.setStatus("current")
_PrtDlciCmprDlciIdx_Type = Integer32
_PrtDlciCmprDlciIdx_Object = MibTableColumn
prtDlciCmprDlciIdx = _PrtDlciCmprDlciIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 2, 1, 5),
    _PrtDlciCmprDlciIdx_Type()
)
prtDlciCmprDlciIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDlciCmprDlciIdx.setStatus("current")
_PrtDlciCmprObj_Type = OctetString
_PrtDlciCmprObj_Object = MibTableColumn
prtDlciCmprObj = _PrtDlciCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 2, 1, 6),
    _PrtDlciCmprObj_Type()
)
prtDlciCmprObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtDlciCmprObj.setStatus("current")
_PrtAlarmsCmprTable_Object = MibTable
prtAlarmsCmprTable = _PrtAlarmsCmprTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    prtAlarmsCmprTable.setStatus("current")
_PrtAlarmsCmprEntry_Object = MibTableRow
prtAlarmsCmprEntry = _PrtAlarmsCmprEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 3, 1)
)
prtAlarmsCmprEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtAlarmsCmprVersion"),
    (0, "RAD-Mpmx-MIB", "prtAlarmsCmprAlarmSlot"),
    (0, "RAD-Mpmx-MIB", "prtAlarmsCmprAlarmPort"),
    (0, "RAD-Mpmx-MIB", "prtAlarmsCmprAlarmIdx"),
)
if mibBuilder.loadTexts:
    prtAlarmsCmprEntry.setStatus("current")
_PrtAlarmsCmprVersion_Type = Integer32
_PrtAlarmsCmprVersion_Object = MibTableColumn
prtAlarmsCmprVersion = _PrtAlarmsCmprVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 3, 1, 1),
    _PrtAlarmsCmprVersion_Type()
)
prtAlarmsCmprVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlarmsCmprVersion.setStatus("current")
_PrtAlarmsCmprAlarmSlot_Type = Integer32
_PrtAlarmsCmprAlarmSlot_Object = MibTableColumn
prtAlarmsCmprAlarmSlot = _PrtAlarmsCmprAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 3, 1, 2),
    _PrtAlarmsCmprAlarmSlot_Type()
)
prtAlarmsCmprAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlarmsCmprAlarmSlot.setStatus("current")
_PrtAlarmsCmprAlarmPort_Type = Integer32
_PrtAlarmsCmprAlarmPort_Object = MibTableColumn
prtAlarmsCmprAlarmPort = _PrtAlarmsCmprAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 3, 1, 3),
    _PrtAlarmsCmprAlarmPort_Type()
)
prtAlarmsCmprAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlarmsCmprAlarmPort.setStatus("current")
_PrtAlarmsCmprAlarmIdx_Type = Integer32
_PrtAlarmsCmprAlarmIdx_Object = MibTableColumn
prtAlarmsCmprAlarmIdx = _PrtAlarmsCmprAlarmIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 3, 1, 4),
    _PrtAlarmsCmprAlarmIdx_Type()
)
prtAlarmsCmprAlarmIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlarmsCmprAlarmIdx.setStatus("current")
_PrtAlarmsCmprObj_Type = OctetString
_PrtAlarmsCmprObj_Object = MibTableColumn
prtAlarmsCmprObj = _PrtAlarmsCmprObj_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 4, 3, 3, 1, 5),
    _PrtAlarmsCmprObj_Type()
)
prtAlarmsCmprObj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAlarmsCmprObj.setStatus("current")
_MapWanGen_ObjectIdentity = ObjectIdentity
mapWanGen = _MapWanGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 5)
)
_AgnLinkMapTable_Object = MibTable
agnLinkMapTable = _AgnLinkMapTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    agnLinkMapTable.setStatus("current")
_AgnLinkMapEntry_Object = MibTableRow
agnLinkMapEntry = _AgnLinkMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 5, 1, 1)
)
agnLinkMapEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "mapLinkId"),
)
if mibBuilder.loadTexts:
    agnLinkMapEntry.setStatus("current")
_MapLinkId_Type = Integer32
_MapLinkId_Object = MibTableColumn
mapLinkId = _MapLinkId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 5, 1, 1, 1),
    _MapLinkId_Type()
)
mapLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapLinkId.setStatus("current")


class _MapLinkSltIdx_Type(Integer32):
    """Custom type mapLinkSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("clA", 3),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_MapLinkSltIdx_Type.__name__ = "Integer32"
_MapLinkSltIdx_Object = MibTableColumn
mapLinkSltIdx = _MapLinkSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 5, 1, 1, 2),
    _MapLinkSltIdx_Type()
)
mapLinkSltIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapLinkSltIdx.setStatus("current")


class _MapLinkPrtIdx_Type(Integer32):
    """Custom type mapLinkPrtIdx based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("exPrt11", 11),
          ("exPrt12", 12),
          ("noConnect", 100),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108),
          ("inPrt9", 109),
          ("inPrt10", 110),
          ("inPrt11", 111),
          ("inPrt12", 112))
    )


_MapLinkPrtIdx_Type.__name__ = "Integer32"
_MapLinkPrtIdx_Object = MibTableColumn
mapLinkPrtIdx = _MapLinkPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 5, 1, 1, 3),
    _MapLinkPrtIdx_Type()
)
mapLinkPrtIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapLinkPrtIdx.setStatus("current")


class _MapLinkStatus_Type(Integer32):
    """Custom type mapLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("down", 2),
          ("up", 3))
    )


_MapLinkStatus_Type.__name__ = "Integer32"
_MapLinkStatus_Object = MibTableColumn
mapLinkStatus = _MapLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 5, 1, 1, 4),
    _MapLinkStatus_Type()
)
mapLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapLinkStatus.setStatus("current")
_DiverseIfWanGen_ObjectIdentity = ObjectIdentity
diverseIfWanGen = _DiverseIfWanGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6)
)
_MuxHub_ObjectIdentity = ObjectIdentity
muxHub = _MuxHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2)
)
_MuxHubEvents_ObjectIdentity = ObjectIdentity
muxHubEvents = _MuxHubEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 0)
)
if mibBuilder.loadTexts:
    muxHubEvents.setStatus("current")
_AgnMux_ObjectIdentity = ObjectIdentity
agnMux = _AgnMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 1)
)
_MdlMux_ObjectIdentity = ObjectIdentity
mdlMux = _MdlMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2)
)
_CnfgMdlMux_ObjectIdentity = ObjectIdentity
cnfgMdlMux = _CnfgMdlMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1)
)
_MdlPbxFramerCnfg_ObjectIdentity = ObjectIdentity
mdlPbxFramerCnfg = _MdlPbxFramerCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1)
)
_MdlPbxFramerCnfgTable_Object = MibTable
mdlPbxFramerCnfgTable = _MdlPbxFramerCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mdlPbxFramerCnfgTable.setStatus("current")
_MdlPbxFramerCnfgEntry_Object = MibTableRow
mdlPbxFramerCnfgEntry = _MdlPbxFramerCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1)
)
mdlPbxFramerCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "mdlPbxFraCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "mdlPbxFraSltIdx"),
)
if mibBuilder.loadTexts:
    mdlPbxFramerCnfgEntry.setStatus("current")
_MdlPbxFraCnfgIdx_Type = Integer32
_MdlPbxFraCnfgIdx_Object = MibTableColumn
mdlPbxFraCnfgIdx = _MdlPbxFraCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 1),
    _MdlPbxFraCnfgIdx_Type()
)
mdlPbxFraCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlPbxFraCnfgIdx.setStatus("current")


class _MdlPbxFraSltIdx_Type(Integer32):
    """Custom type mdlPbxFraSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_MdlPbxFraSltIdx_Type.__name__ = "Integer32"
_MdlPbxFraSltIdx_Object = MibTableColumn
mdlPbxFraSltIdx = _MdlPbxFraSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 2),
    _MdlPbxFraSltIdx_Type()
)
mdlPbxFraSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlPbxFraSltIdx.setStatus("current")


class _MdlPbxFraEnhEcho_Type(Integer32):
    """Custom type mdlPbxFraEnhEcho based on Integer32"""
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
        *(("notApplicable", 1),
          ("disabled", 2),
          ("ms16", 3),
          ("ms32", 4))
    )


_MdlPbxFraEnhEcho_Type.__name__ = "Integer32"
_MdlPbxFraEnhEcho_Object = MibTableColumn
mdlPbxFraEnhEcho = _MdlPbxFraEnhEcho_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 3),
    _MdlPbxFraEnhEcho_Type()
)
mdlPbxFraEnhEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlPbxFraEnhEcho.setStatus("current")


class _MdlPbxFraTSGroupAss_Type(Integer32):
    """Custom type mdlPbxFraTSGroupAss based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group3", 3),
          ("group4", 4),
          ("group5", 5),
          ("group6", 6),
          ("group7", 7),
          ("group8", 8),
          ("notApplicable", 255))
    )


_MdlPbxFraTSGroupAss_Type.__name__ = "Integer32"
_MdlPbxFraTSGroupAss_Object = MibTableColumn
mdlPbxFraTSGroupAss = _MdlPbxFraTSGroupAss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 4),
    _MdlPbxFraTSGroupAss_Type()
)
mdlPbxFraTSGroupAss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlPbxFraTSGroupAss.setStatus("current")


class _MdlPbxFraSignalMode_Type(Integer32):
    """Custom type mdlPbxFraSignalMode based on Integer32"""
    defaultValue = 4

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
        *(("notApplicable", 1),
          ("tieTrunk", 2),
          ("tieInvert", 3),
          ("casTrans", 4),
          ("userDefined", 5),
          ("ccsTrans", 6),
          ("noSignaling", 7))
    )


_MdlPbxFraSignalMode_Type.__name__ = "Integer32"
_MdlPbxFraSignalMode_Object = MibTableColumn
mdlPbxFraSignalMode = _MdlPbxFraSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 5),
    _MdlPbxFraSignalMode_Type()
)
mdlPbxFraSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlPbxFraSignalMode.setStatus("current")


class _MdlPbxFraSignalVector_Type(OctetString):
    """Custom type mdlPbxFraSignalVector based on OctetString"""
    defaultHexValue = "0000"


_MdlPbxFraSignalVector_Type.__name__ = "OctetString"
_MdlPbxFraSignalVector_Object = MibTableColumn
mdlPbxFraSignalVector = _MdlPbxFraSignalVector_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 6),
    _MdlPbxFraSignalVector_Type()
)
mdlPbxFraSignalVector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlPbxFraSignalVector.setStatus("current")


class _MdlPbxFraSignalMask_Type(OctetString):
    """Custom type mdlPbxFraSignalMask based on OctetString"""
    defaultHexValue = "ffff"


_MdlPbxFraSignalMask_Type.__name__ = "OctetString"
_MdlPbxFraSignalMask_Object = MibTableColumn
mdlPbxFraSignalMask = _MdlPbxFraSignalMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 7),
    _MdlPbxFraSignalMask_Type()
)
mdlPbxFraSignalMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlPbxFraSignalMask.setStatus("current")


class _MdlPbxFraFramerSlot_Type(Integer32):
    """Custom type mdlPbxFraFramerSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_MdlPbxFraFramerSlot_Type.__name__ = "Integer32"
_MdlPbxFraFramerSlot_Object = MibTableColumn
mdlPbxFraFramerSlot = _MdlPbxFraFramerSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 8),
    _MdlPbxFraFramerSlot_Type()
)
mdlPbxFraFramerSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlPbxFraFramerSlot.setStatus("current")


class _MdlPbxFraSignaling_Type(Integer32):
    """Custom type mdlPbxFraSignaling based on Integer32"""
    defaultValue = 2

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
          ("endToEnd", 2),
          ("localTermination", 3))
    )


_MdlPbxFraSignaling_Type.__name__ = "Integer32"
_MdlPbxFraSignaling_Object = MibTableColumn
mdlPbxFraSignaling = _MdlPbxFraSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 9),
    _MdlPbxFraSignaling_Type()
)
mdlPbxFraSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlPbxFraSignaling.setStatus("current")
_MdlPbxFraTransSigTs_Type = Integer32
_MdlPbxFraTransSigTs_Object = MibTableColumn
mdlPbxFraTransSigTs = _MdlPbxFraTransSigTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 1, 1, 1, 10),
    _MdlPbxFraTransSigTs_Type()
)
mdlPbxFraTransSigTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdlPbxFraTransSigTs.setStatus("current")
_MdlProtIpTable_Object = MibTable
mdlProtIpTable = _MdlProtIpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mdlProtIpTable.setStatus("current")
_MdlProtIpEntry_Object = MibTableRow
mdlProtIpEntry = _MdlProtIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 2, 1)
)
mdlProtIpEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "mdlProtIpCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "mdlProtIpSlotIdx"),
    (0, "RAD-Mpmx-MIB", "mdlProtIpAddress"),
)
if mibBuilder.loadTexts:
    mdlProtIpEntry.setStatus("current")


class _MdlProtIpCnfgIdx_Type(Integer32):
    """Custom type mdlProtIpCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MdlProtIpCnfgIdx_Type.__name__ = "Integer32"
_MdlProtIpCnfgIdx_Object = MibTableColumn
mdlProtIpCnfgIdx = _MdlProtIpCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 2, 1, 1),
    _MdlProtIpCnfgIdx_Type()
)
mdlProtIpCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlProtIpCnfgIdx.setStatus("current")


class _MdlProtIpSlotIdx_Type(Integer32):
    """Custom type mdlProtIpSlotIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_MdlProtIpSlotIdx_Type.__name__ = "Integer32"
_MdlProtIpSlotIdx_Object = MibTableColumn
mdlProtIpSlotIdx = _MdlProtIpSlotIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 2, 1, 2),
    _MdlProtIpSlotIdx_Type()
)
mdlProtIpSlotIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlProtIpSlotIdx.setStatus("current")
_MdlProtIpAddress_Type = IpAddress
_MdlProtIpAddress_Object = MibTableColumn
mdlProtIpAddress = _MdlProtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 2, 1, 3),
    _MdlProtIpAddress_Type()
)
mdlProtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlProtIpAddress.setStatus("current")
_MdlProtIpRowStatus_Type = RowStatus
_MdlProtIpRowStatus_Object = MibTableColumn
mdlProtIpRowStatus = _MdlProtIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 1, 2, 1, 4),
    _MdlProtIpRowStatus_Type()
)
mdlProtIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mdlProtIpRowStatus.setStatus("current")
_StatMdlMux_ObjectIdentity = ObjectIdentity
statMdlMux = _StatMdlMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 2)
)
_MdlStatTable_Object = MibTable
mdlStatTable = _MdlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mdlStatTable.setStatus("current")
_MdlStatEntry_Object = MibTableRow
mdlStatEntry = _MdlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 2, 1, 1)
)
mdlStatEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "mdlStatSltIdx"),
)
if mibBuilder.loadTexts:
    mdlStatEntry.setStatus("current")


class _MdlStatSltIdx_Type(Integer32):
    """Custom type mdlStatSltIdx based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("psA", 1),
          ("psB", 2),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_MdlStatSltIdx_Type.__name__ = "Integer32"
_MdlStatSltIdx_Object = MibTableColumn
mdlStatSltIdx = _MdlStatSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 2, 1, 1, 1),
    _MdlStatSltIdx_Type()
)
mdlStatSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlStatSltIdx.setStatus("current")
_MdlStatHostIP_Type = IpAddress
_MdlStatHostIP_Object = MibTableColumn
mdlStatHostIP = _MdlStatHostIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 2, 1, 1, 2),
    _MdlStatHostIP_Type()
)
mdlStatHostIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlStatHostIP.setStatus("current")
_MdlStatHostMask_Type = IpAddress
_MdlStatHostMask_Object = MibTableColumn
mdlStatHostMask = _MdlStatHostMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 2, 1, 1, 3),
    _MdlStatHostMask_Type()
)
mdlStatHostMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlStatHostMask.setStatus("current")
_MdlStatDefaultGateway_Type = IpAddress
_MdlStatDefaultGateway_Object = MibTableColumn
mdlStatDefaultGateway = _MdlStatDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 2, 2, 1, 1, 4),
    _MdlStatDefaultGateway_Type()
)
mdlStatDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdlStatDefaultGateway.setStatus("current")
_PrtMux_ObjectIdentity = ObjectIdentity
prtMux = _PrtMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3)
)
_StatPrtMux_ObjectIdentity = ObjectIdentity
statPrtMux = _StatPrtMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1)
)
_PrtSExHsfStatTable_Object = MibTable
prtSExHsfStatTable = _PrtSExHsfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 6)
)
if mibBuilder.loadTexts:
    prtSExHsfStatTable.setStatus("current")
_PrtSExHsfStatEntry_Object = MibTableRow
prtSExHsfStatEntry = _PrtSExHsfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 6, 1)
)
prtSExHsfStatEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtSExHsfSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtSExHsfPrtIdx"),
)
if mibBuilder.loadTexts:
    prtSExHsfStatEntry.setStatus("current")


class _PrtSExHsfSltIdx_Type(Integer32):
    """Custom type prtSExHsfSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtSExHsfSltIdx_Type.__name__ = "Integer32"
_PrtSExHsfSltIdx_Object = MibTableColumn
prtSExHsfSltIdx = _PrtSExHsfSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 6, 1, 1),
    _PrtSExHsfSltIdx_Type()
)
prtSExHsfSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSExHsfSltIdx.setStatus("current")


class _PrtSExHsfPrtIdx_Type(Integer32):
    """Custom type prtSExHsfPrtIdx based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("exPrt11", 11),
          ("exPrt12", 12))
    )


_PrtSExHsfPrtIdx_Type.__name__ = "Integer32"
_PrtSExHsfPrtIdx_Object = MibTableColumn
prtSExHsfPrtIdx = _PrtSExHsfPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 6, 1, 2),
    _PrtSExHsfPrtIdx_Type()
)
prtSExHsfPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSExHsfPrtIdx.setStatus("current")


class _PrtSExHsfInterfaceTyp_Type(Integer32):
    """Custom type prtSExHsfInterfaceTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("v35", 2),
          ("rs422", 3))
    )


_PrtSExHsfInterfaceTyp_Type.__name__ = "Integer32"
_PrtSExHsfInterfaceTyp_Object = MibTableColumn
prtSExHsfInterfaceTyp = _PrtSExHsfInterfaceTyp_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 6, 1, 3),
    _PrtSExHsfInterfaceTyp_Type()
)
prtSExHsfInterfaceTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSExHsfInterfaceTyp.setStatus("current")


class _PrtSExHsfRts_Type(Integer32):
    """Custom type prtSExHsfRts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notActive", 2),
          ("active", 3))
    )


_PrtSExHsfRts_Type.__name__ = "Integer32"
_PrtSExHsfRts_Object = MibTableColumn
prtSExHsfRts = _PrtSExHsfRts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 6, 1, 4),
    _PrtSExHsfRts_Type()
)
prtSExHsfRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtSExHsfRts.setStatus("current")
_PrtIsdnStatusTable_Object = MibTable
prtIsdnStatusTable = _PrtIsdnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 16)
)
if mibBuilder.loadTexts:
    prtIsdnStatusTable.setStatus("current")
_PrtIsdnStatusEntry_Object = MibTableRow
prtIsdnStatusEntry = _PrtIsdnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 16, 1)
)
prtIsdnStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtIsdnStatusEntry.setStatus("current")


class _PrtIsdnStatusDspMode_Type(Integer32):
    """Custom type prtIsdnStatusDspMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("voice", 2),
          ("idle", 3),
          ("fax", 4),
          ("vbd", 5))
    )


_PrtIsdnStatusDspMode_Type.__name__ = "Integer32"
_PrtIsdnStatusDspMode_Object = MibTableColumn
prtIsdnStatusDspMode = _PrtIsdnStatusDspMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 16, 1, 1),
    _PrtIsdnStatusDspMode_Type()
)
prtIsdnStatusDspMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnStatusDspMode.setStatus("current")


class _PrtIsdnStatusCallState_Type(Integer32):
    """Custom type prtIsdnStatusCallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("present", 2),
          ("overlapReceive", 3),
          ("incoming", 4),
          ("receive", 5),
          ("initiated", 6),
          ("overlapSend", 7),
          ("outGoingProceed", 8),
          ("callDeliver", 9),
          ("active", 10),
          ("disconnectIndicate", 11),
          ("releaseRequest", 12),
          ("disconnectReq", 13),
          ("notActive", 14))
    )


_PrtIsdnStatusCallState_Type.__name__ = "Integer32"
_PrtIsdnStatusCallState_Object = MibTableColumn
prtIsdnStatusCallState = _PrtIsdnStatusCallState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 16, 1, 2),
    _PrtIsdnStatusCallState_Type()
)
prtIsdnStatusCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnStatusCallState.setStatus("current")
_PrtIsdnStatusCallingNumber_Type = DisplayString
_PrtIsdnStatusCallingNumber_Object = MibTableColumn
prtIsdnStatusCallingNumber = _PrtIsdnStatusCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 16, 1, 3),
    _PrtIsdnStatusCallingNumber_Type()
)
prtIsdnStatusCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnStatusCallingNumber.setStatus("current")
_PrtIsdnStatusCalledNumber_Type = DisplayString
_PrtIsdnStatusCalledNumber_Object = MibTableColumn
prtIsdnStatusCalledNumber = _PrtIsdnStatusCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 16, 1, 4),
    _PrtIsdnStatusCalledNumber_Type()
)
prtIsdnStatusCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnStatusCalledNumber.setStatus("current")
_PrtIsdnStatusCalledIP_Type = IpAddress
_PrtIsdnStatusCalledIP_Object = MibTableColumn
prtIsdnStatusCalledIP = _PrtIsdnStatusCalledIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 16, 1, 5),
    _PrtIsdnStatusCalledIP_Type()
)
prtIsdnStatusCalledIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnStatusCalledIP.setStatus("current")


class _PrtIsdnStatusCallDirection_Type(Integer32):
    """Custom type prtIsdnStatusCallDirection based on Integer32"""
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
          ("incoming", 2),
          ("outgoing", 3))
    )


_PrtIsdnStatusCallDirection_Type.__name__ = "Integer32"
_PrtIsdnStatusCallDirection_Object = MibTableColumn
prtIsdnStatusCallDirection = _PrtIsdnStatusCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 1, 16, 1, 6),
    _PrtIsdnStatusCallDirection_Type()
)
prtIsdnStatusCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnStatusCallDirection.setStatus("current")
_CnfgPrtMux_ObjectIdentity = ObjectIdentity
cnfgPrtMux = _CnfgPrtMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2)
)
_PrtClCnfg_ObjectIdentity = ObjectIdentity
prtClCnfg = _PrtClCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1)
)
_PrtExClCnfgTable_Object = MibTable
prtExClCnfgTable = _PrtExClCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    prtExClCnfgTable.setStatus("current")
_PrtExClCnfgEntry_Object = MibTableRow
prtExClCnfgEntry = _PrtExClCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1)
)
prtExClCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExClCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExClSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExClPrtIdx"),
)
if mibBuilder.loadTexts:
    prtExClCnfgEntry.setStatus("current")


class _PrtExClCnfgIdx_Type(Integer32):
    """Custom type prtExClCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExClCnfgIdx_Type.__name__ = "Integer32"
_PrtExClCnfgIdx_Object = MibTableColumn
prtExClCnfgIdx = _PrtExClCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 1),
    _PrtExClCnfgIdx_Type()
)
prtExClCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClCnfgIdx.setStatus("current")


class _PrtExClSltIdx_Type(Integer32):
    """Custom type prtExClSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clA", 3),
          ("clB", 4),
          ("notApplicable", 255))
    )


_PrtExClSltIdx_Type.__name__ = "Integer32"
_PrtExClSltIdx_Object = MibTableColumn
prtExClSltIdx = _PrtExClSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 2),
    _PrtExClSltIdx_Type()
)
prtExClSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClSltIdx.setStatus("current")


class _PrtExClPrtIdx_Type(Integer32):
    """Custom type prtExClPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2))
    )


_PrtExClPrtIdx_Type.__name__ = "Integer32"
_PrtExClPrtIdx_Object = MibTableColumn
prtExClPrtIdx = _PrtExClPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 3),
    _PrtExClPrtIdx_Type()
)
prtExClPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClPrtIdx.setStatus("current")


class _PrtExClUsage_Type(Integer32):
    """Custom type prtExClUsage based on Integer32"""
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
        *(("unknown", 1),
          ("noUse", 2),
          ("nmsSlip", 3),
          ("nmsPpp", 4),
          ("muxSlip", 5),
          ("muxPpp", 6),
          ("terminal", 7))
    )


_PrtExClUsage_Type.__name__ = "Integer32"
_PrtExClUsage_Object = MibTableColumn
prtExClUsage = _PrtExClUsage_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 4),
    _PrtExClUsage_Type()
)
prtExClUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClUsage.setStatus("current")


class _PrtExClRate_Type(Integer32):
    """Custom type prtExClRate based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("r300Bps", 1),
          ("r1200Bps", 2),
          ("r2400Bps", 3),
          ("r4800Bps", 4),
          ("r9600Bps", 5),
          ("r19200Bps", 6),
          ("r38400Bps", 7),
          ("r57600Bps", 8),
          ("r115200Bps", 9))
    )


_PrtExClRate_Type.__name__ = "Integer32"
_PrtExClRate_Object = MibTableColumn
prtExClRate = _PrtExClRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 5),
    _PrtExClRate_Type()
)
prtExClRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClRate.setStatus("current")


class _PrtExClDataBits_Type(Integer32):
    """Custom type prtExClDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataBits7Bits", 1),
          ("dataBits8Bits", 2))
    )


_PrtExClDataBits_Type.__name__ = "Integer32"
_PrtExClDataBits_Object = MibTableColumn
prtExClDataBits = _PrtExClDataBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 6),
    _PrtExClDataBits_Type()
)
prtExClDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClDataBits.setStatus("current")


class _PrtExClParity_Type(Integer32):
    """Custom type prtExClParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("odd", 1),
          ("even", 2),
          ("none", 3))
    )


_PrtExClParity_Type.__name__ = "Integer32"
_PrtExClParity_Object = MibTableColumn
prtExClParity = _PrtExClParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 7),
    _PrtExClParity_Type()
)
prtExClParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClParity.setStatus("current")


class _PrtExClStopBits_Type(Integer32):
    """Custom type prtExClStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopBits1Bit", 1),
          ("stopBits1dot5Bits", 2),
          ("stopBits2Bits", 3))
    )


_PrtExClStopBits_Type.__name__ = "Integer32"
_PrtExClStopBits_Object = MibTableColumn
prtExClStopBits = _PrtExClStopBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 8),
    _PrtExClStopBits_Type()
)
prtExClStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClStopBits.setStatus("current")


class _PrtExClRoutingProtocol_Type(Integer32):
    """Custom type prtExClRoutingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rip2", 2))
    )


_PrtExClRoutingProtocol_Type.__name__ = "Integer32"
_PrtExClRoutingProtocol_Object = MibTableColumn
prtExClRoutingProtocol = _PrtExClRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 9),
    _PrtExClRoutingProtocol_Type()
)
prtExClRoutingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClRoutingProtocol.setStatus("current")


class _PrtExClEnabled_Type(Integer32):
    """Custom type prtExClEnabled based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 3))
    )


_PrtExClEnabled_Type.__name__ = "Integer32"
_PrtExClEnabled_Object = MibTableColumn
prtExClEnabled = _PrtExClEnabled_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 1, 1, 1, 10),
    _PrtExClEnabled_Type()
)
prtExClEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExClEnabled.setStatus("current")
_PrtPh1MlCnfg_ObjectIdentity = ObjectIdentity
prtPh1MlCnfg = _PrtPh1MlCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2)
)
_PrtExPh1MlCnfgTable_Object = MibTable
prtExPh1MlCnfgTable = _PrtExPh1MlCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    prtExPh1MlCnfgTable.setStatus("current")
_PrtExPh1MlCnfgEntry_Object = MibTableRow
prtExPh1MlCnfgEntry = _PrtExPh1MlCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1)
)
prtExPh1MlCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExPh1MlCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPh1MlSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPh1MlPrtIdx"),
)
if mibBuilder.loadTexts:
    prtExPh1MlCnfgEntry.setStatus("current")


class _PrtExPh1MlCnfgIdx_Type(Integer32):
    """Custom type prtExPh1MlCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExPh1MlCnfgIdx_Type.__name__ = "Integer32"
_PrtExPh1MlCnfgIdx_Object = MibTableColumn
prtExPh1MlCnfgIdx = _PrtExPh1MlCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 1),
    _PrtExPh1MlCnfgIdx_Type()
)
prtExPh1MlCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPh1MlCnfgIdx.setStatus("current")


class _PrtExPh1MlSltIdx_Type(Integer32):
    """Custom type prtExPh1MlSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExPh1MlSltIdx_Type.__name__ = "Integer32"
_PrtExPh1MlSltIdx_Object = MibTableColumn
prtExPh1MlSltIdx = _PrtExPh1MlSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 2),
    _PrtExPh1MlSltIdx_Type()
)
prtExPh1MlSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPh1MlSltIdx.setStatus("current")


class _PrtExPh1MlPrtIdx_Type(Integer32):
    """Custom type prtExPh1MlPrtIdx based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("exPrt11", 11),
          ("exPrt12", 12),
          ("exPrt13", 13),
          ("exPrt14", 14),
          ("exPrt15", 15),
          ("exPrt16", 16),
          ("exPrt17", 17),
          ("exPrt18", 18),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108),
          ("inPrt9", 109),
          ("inPrt10", 110),
          ("inPrt11", 111),
          ("inPrt12", 112),
          ("inPrt13", 113),
          ("inPrt14", 114),
          ("inPrt15", 115),
          ("inPrt16", 116),
          ("inPrt17", 117),
          ("inPrt18", 118),
          ("inPrt19", 119),
          ("inPrt20", 120),
          ("inPrt21", 121),
          ("inPrt22", 122),
          ("inPrt23", 123),
          ("inPrt24", 124),
          ("inPrt25", 125),
          ("inPrt26", 126),
          ("inPrt27", 127),
          ("inPrt28", 128),
          ("inPrt29", 129),
          ("inPrt30", 130),
          ("inPrt31", 131),
          ("inPrt32", 132),
          ("inPrt33", 133),
          ("inPrt34", 134),
          ("inPrt35", 135),
          ("inPrt36", 136),
          ("inPrt37", 137),
          ("inPrt38", 138),
          ("inPrt39", 139),
          ("inPrt40", 140),
          ("inPrt41", 141),
          ("inPrt42", 142),
          ("inPrt43", 143),
          ("inPrt44", 144),
          ("inPrt45", 145),
          ("inPrt46", 146),
          ("inPrt47", 147),
          ("inPrt48", 148),
          ("inPrt49", 149),
          ("inPrt50", 150),
          ("inPrt51", 151),
          ("inPrt52", 152),
          ("inPrt53", 153),
          ("inPrt54", 154),
          ("inPrt55", 155),
          ("inPrt56", 156),
          ("inPrt57", 157),
          ("inPrt58", 158),
          ("inPrt59", 159),
          ("inPrt60", 160),
          ("inPrt61", 161),
          ("inPrt62", 162),
          ("inPrt63", 163),
          ("inPrt64", 164),
          ("inPrt65", 165),
          ("inPrt66", 166),
          ("inPrt67", 167),
          ("inPrt68", 168),
          ("inPrt69", 169),
          ("inPrt70", 170),
          ("inPrt71", 171),
          ("inPrt72", 172),
          ("inPrt73", 173),
          ("inPrt74", 174),
          ("inPrt75", 175),
          ("inPrt76", 176),
          ("inPrt77", 177),
          ("inPrt78", 178),
          ("inPrt79", 179),
          ("inPrt80", 180),
          ("inPrt81", 181),
          ("inPrt82", 182),
          ("inPrt83", 183),
          ("inPrt84", 184))
    )


_PrtExPh1MlPrtIdx_Type.__name__ = "Integer32"
_PrtExPh1MlPrtIdx_Object = MibTableColumn
prtExPh1MlPrtIdx = _PrtExPh1MlPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 3),
    _PrtExPh1MlPrtIdx_Type()
)
prtExPh1MlPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPh1MlPrtIdx.setStatus("current")


class _PrtExPh1MlConnect_Type(Integer32):
    """Custom type prtExPh1MlConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExPh1MlConnect_Type.__name__ = "Integer32"
_PrtExPh1MlConnect_Object = MibTableColumn
prtExPh1MlConnect = _PrtExPh1MlConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 4),
    _PrtExPh1MlConnect_Type()
)
prtExPh1MlConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlConnect.setStatus("current")


class _PrtExPh1MlLineType_Type(Integer32):
    """Custom type prtExPh1MlLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              101)
        )
    )
    namedValues = NamedValues(
        *(("esfT1", 2),
          ("sfT1", 3),
          ("g732nE1", 4),
          ("g732nE1CRC", 5),
          ("g732sE1", 6),
          ("g732sE1CRC", 7),
          ("g732unframed", 8),
          ("e1Unframed", 9),
          ("framed", 101))
    )


_PrtExPh1MlLineType_Type.__name__ = "Integer32"
_PrtExPh1MlLineType_Object = MibTableColumn
prtExPh1MlLineType = _PrtExPh1MlLineType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 5),
    _PrtExPh1MlLineType_Type()
)
prtExPh1MlLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlLineType.setStatus("current")


class _PrtExPh1MlLineCode_Type(Integer32):
    """Custom type prtExPh1MlLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("b7T1", 1),
          ("b8zsT1", 2),
          ("transT1", 3),
          ("hdb3E1", 4),
          ("notApplicable", 255))
    )


_PrtExPh1MlLineCode_Type.__name__ = "Integer32"
_PrtExPh1MlLineCode_Object = MibTableColumn
prtExPh1MlLineCode = _PrtExPh1MlLineCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 6),
    _PrtExPh1MlLineCode_Type()
)
prtExPh1MlLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlLineCode.setStatus("current")


class _PrtExPh1MlLineLen_Type(Integer32):
    """Custom type prtExPh1MlLineLen based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("len0p133ft", 2),
          ("len134p266ft", 3),
          ("len267p399ft", 4),
          ("len400p533ft", 5),
          ("len534p655ft", 6),
          ("lenFcc68", 7),
          ("notApplicable", 255))
    )


_PrtExPh1MlLineLen_Type.__name__ = "Integer32"
_PrtExPh1MlLineLen_Object = MibTableColumn
prtExPh1MlLineLen = _PrtExPh1MlLineLen_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 7),
    _PrtExPh1MlLineLen_Type()
)
prtExPh1MlLineLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlLineLen.setStatus("current")


class _PrtExPh1MlRestoreTime_Type(Integer32):
    """Custom type prtExPh1MlRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("restoreT1secFast", 2),
          ("restoreT10sec62411", 3),
          ("ccittE1", 4))
    )


_PrtExPh1MlRestoreTime_Type.__name__ = "Integer32"
_PrtExPh1MlRestoreTime_Object = MibTableColumn
prtExPh1MlRestoreTime = _PrtExPh1MlRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 8),
    _PrtExPh1MlRestoreTime_Type()
)
prtExPh1MlRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlRestoreTime.setStatus("current")


class _PrtExPh1MlTxGain_Type(Integer32):
    """Custom type prtExPh1MlTxGain based on Integer32"""
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
        *(("notApplicable", 1),
          ("txGain0db", 2),
          ("txGain7dot5db", 3),
          ("txGain15db", 4),
          ("txGain22dot5db", 5))
    )


_PrtExPh1MlTxGain_Type.__name__ = "Integer32"
_PrtExPh1MlTxGain_Object = MibTableColumn
prtExPh1MlTxGain = _PrtExPh1MlTxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 9),
    _PrtExPh1MlTxGain_Type()
)
prtExPh1MlTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTxGain.setStatus("current")


class _PrtExPh1MlRxSensitivity_Type(Integer32):
    """Custom type prtExPh1MlRxSensitivity based on Integer32"""
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
        *(("notApplicable", 1),
          ("low26dBm", 2),
          ("high36dBm", 3),
          ("shortHaul", 4),
          ("longHaul", 5),
          ("low15dbm", 6))
    )


_PrtExPh1MlRxSensitivity_Type.__name__ = "Integer32"
_PrtExPh1MlRxSensitivity_Object = MibTableColumn
prtExPh1MlRxSensitivity = _PrtExPh1MlRxSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 10),
    _PrtExPh1MlRxSensitivity_Type()
)
prtExPh1MlRxSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlRxSensitivity.setStatus("current")
_PrtExPh1MlIdleCode_Type = Integer32
_PrtExPh1MlIdleCode_Object = MibTableColumn
prtExPh1MlIdleCode = _PrtExPh1MlIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 11),
    _PrtExPh1MlIdleCode_Type()
)
prtExPh1MlIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlIdleCode.setStatus("current")


class _PrtExPh1MlTdmTrunk_Type(Integer32):
    """Custom type prtExPh1MlTdmTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("linkA", 1),
          ("linkB", 2),
          ("none", 3),
          ("notApplicable", 255))
    )


_PrtExPh1MlTdmTrunk_Type.__name__ = "Integer32"
_PrtExPh1MlTdmTrunk_Object = MibTableColumn
prtExPh1MlTdmTrunk = _PrtExPh1MlTdmTrunk_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 12),
    _PrtExPh1MlTdmTrunk_Type()
)
prtExPh1MlTdmTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTdmTrunk.setStatus("current")


class _PrtExPh1MlClkMode_Type(Integer32):
    """Custom type prtExPh1MlClkMode based on Integer32"""
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
        *(("internalLocal", 1),
          ("loopBackLocal", 2),
          ("nodalTiming", 3),
          ("loopBackFromLink", 4),
          ("loopBackFromChannel", 5),
          ("loopbackFromSystem", 6))
    )


_PrtExPh1MlClkMode_Type.__name__ = "Integer32"
_PrtExPh1MlClkMode_Object = MibTableColumn
prtExPh1MlClkMode = _PrtExPh1MlClkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 13),
    _PrtExPh1MlClkMode_Type()
)
prtExPh1MlClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlClkMode.setStatus("current")


class _PrtExPh1MlMfClkSrcSlt_Type(Integer32):
    """Custom type prtExPh1MlMfClkSrcSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("local", 2),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExPh1MlMfClkSrcSlt_Type.__name__ = "Integer32"
_PrtExPh1MlMfClkSrcSlt_Object = MibTableColumn
prtExPh1MlMfClkSrcSlt = _PrtExPh1MlMfClkSrcSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 14),
    _PrtExPh1MlMfClkSrcSlt_Type()
)
prtExPh1MlMfClkSrcSlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlMfClkSrcSlt.setStatus("current")


class _PrtExPh1MlMfClkSrcPrt_Type(Integer32):
    """Custom type prtExPh1MlMfClkSrcPrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              101,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("inPrt1", 101),
          ("notApplicable", 255))
    )


_PrtExPh1MlMfClkSrcPrt_Type.__name__ = "Integer32"
_PrtExPh1MlMfClkSrcPrt_Object = MibTableColumn
prtExPh1MlMfClkSrcPrt = _PrtExPh1MlMfClkSrcPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 15),
    _PrtExPh1MlMfClkSrcPrt_Type()
)
prtExPh1MlMfClkSrcPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlMfClkSrcPrt.setStatus("current")


class _PrtExPh1MlFdlType_Type(Integer32):
    """Custom type prtExPh1MlFdlType based on Integer32"""
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
          ("response", 2),
          ("command", 3))
    )


_PrtExPh1MlFdlType_Type.__name__ = "Integer32"
_PrtExPh1MlFdlType_Object = MibTableColumn
prtExPh1MlFdlType = _PrtExPh1MlFdlType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 16),
    _PrtExPh1MlFdlType_Type()
)
prtExPh1MlFdlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlFdlType.setStatus("current")


class _PrtExPh1MlInbandMng_Type(Integer32):
    """Custom type prtExPh1MlInbandMng based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("fdlOrTs0", 3),
          ("dedicatedTs", 4),
          ("dedicatedPpp", 5),
          ("dedicatedFr", 6),
          ("notApplicable", 255))
    )


_PrtExPh1MlInbandMng_Type.__name__ = "Integer32"
_PrtExPh1MlInbandMng_Object = MibTableColumn
prtExPh1MlInbandMng = _PrtExPh1MlInbandMng_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 17),
    _PrtExPh1MlInbandMng_Type()
)
prtExPh1MlInbandMng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlInbandMng.setStatus("current")


class _PrtExPh1MlInbandMngRate_Type(Integer32):
    """Custom type prtExPh1MlInbandMngRate based on Integer32"""
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
          ("r4k", 2),
          ("r8k", 3),
          ("r12k", 4),
          ("r16k", 5),
          ("r32k", 6),
          ("r64k", 7),
          ("r20k", 8))
    )


_PrtExPh1MlInbandMngRate_Type.__name__ = "Integer32"
_PrtExPh1MlInbandMngRate_Object = MibTableColumn
prtExPh1MlInbandMngRate = _PrtExPh1MlInbandMngRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 18),
    _PrtExPh1MlInbandMngRate_Type()
)
prtExPh1MlInbandMngRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlInbandMngRate.setStatus("current")


class _PrtExPh1MlRedundType_Type(Integer32):
    """Custom type prtExPh1MlRedundType based on Integer32"""
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
        *(("none", 1),
          ("dualCableAIS", 2),
          ("yCable", 3),
          ("dualCableParallelTx", 4))
    )


_PrtExPh1MlRedundType_Type.__name__ = "Integer32"
_PrtExPh1MlRedundType_Object = MibTableColumn
prtExPh1MlRedundType = _PrtExPh1MlRedundType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 19),
    _PrtExPh1MlRedundType_Type()
)
prtExPh1MlRedundType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlRedundType.setStatus("current")


class _PrtExPh1MlRedundSlot_Type(Integer32):
    """Custom type prtExPh1MlRedundSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExPh1MlRedundSlot_Type.__name__ = "Integer32"
_PrtExPh1MlRedundSlot_Object = MibTableColumn
prtExPh1MlRedundSlot = _PrtExPh1MlRedundSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 20),
    _PrtExPh1MlRedundSlot_Type()
)
prtExPh1MlRedundSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlRedundSlot.setStatus("current")


class _PrtExPh1MlRedundPort_Type(Integer32):
    """Custom type prtExPh1MlRedundPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              101,
              102,
              103,
              104,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("notApplicable", 255))
    )


_PrtExPh1MlRedundPort_Type.__name__ = "Integer32"
_PrtExPh1MlRedundPort_Object = MibTableColumn
prtExPh1MlRedundPort = _PrtExPh1MlRedundPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 21),
    _PrtExPh1MlRedundPort_Type()
)
prtExPh1MlRedundPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlRedundPort.setStatus("current")


class _PrtExPh1MlRedundRecTime_Type(Integer32):
    """Custom type prtExPh1MlRedundRecTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PrtExPh1MlRedundRecTime_Type.__name__ = "Integer32"
_PrtExPh1MlRedundRecTime_Object = MibTableColumn
prtExPh1MlRedundRecTime = _PrtExPh1MlRedundRecTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 22),
    _PrtExPh1MlRedundRecTime_Type()
)
prtExPh1MlRedundRecTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlRedundRecTime.setStatus("current")


class _PrtExPh1MlInbandMngRoutProt_Type(Integer32):
    """Custom type prtExPh1MlInbandMngRoutProt based on Integer32"""
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
        *(("none", 1),
          ("rip2", 2),
          ("proprietary", 3),
          ("proprietaryNoNmsTx", 4))
    )


_PrtExPh1MlInbandMngRoutProt_Type.__name__ = "Integer32"
_PrtExPh1MlInbandMngRoutProt_Object = MibTableColumn
prtExPh1MlInbandMngRoutProt = _PrtExPh1MlInbandMngRoutProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 23),
    _PrtExPh1MlInbandMngRoutProt_Type()
)
prtExPh1MlInbandMngRoutProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlInbandMngRoutProt.setStatus("current")


class _PrtExPh1MlIfType_Type(Integer32):
    """Custom type prtExPh1MlIfType based on Integer32"""
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
        *(("notApplicable", 1),
          ("csu", 2),
          ("dsu", 3),
          ("ltu", 4))
    )


_PrtExPh1MlIfType_Type.__name__ = "Integer32"
_PrtExPh1MlIfType_Object = MibTableColumn
prtExPh1MlIfType = _PrtExPh1MlIfType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 24),
    _PrtExPh1MlIfType_Type()
)
prtExPh1MlIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlIfType.setStatus("current")


class _PrtExPh1MlMultiplier_Type(Integer32):
    """Custom type prtExPh1MlMultiplier based on Integer32"""
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
          ("br56", 2),
          ("br64", 3))
    )


_PrtExPh1MlMultiplier_Type.__name__ = "Integer32"
_PrtExPh1MlMultiplier_Object = MibTableColumn
prtExPh1MlMultiplier = _PrtExPh1MlMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 25),
    _PrtExPh1MlMultiplier_Type()
)
prtExPh1MlMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlMultiplier.setStatus("current")
_PrtExPh1MlSupportedTS_Type = Integer32
_PrtExPh1MlSupportedTS_Object = MibTableColumn
prtExPh1MlSupportedTS = _PrtExPh1MlSupportedTS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 26),
    _PrtExPh1MlSupportedTS_Type()
)
prtExPh1MlSupportedTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPh1MlSupportedTS.setStatus("current")


class _PrtExPh1MlImpedance_Type(Integer32):
    """Custom type prtExPh1MlImpedance based on Integer32"""
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
          ("unbalanced", 2),
          ("balanced", 3))
    )


_PrtExPh1MlImpedance_Type.__name__ = "Integer32"
_PrtExPh1MlImpedance_Object = MibTableColumn
prtExPh1MlImpedance = _PrtExPh1MlImpedance_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 27),
    _PrtExPh1MlImpedance_Type()
)
prtExPh1MlImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlImpedance.setStatus("current")


class _PrtExPh1MlQ50BwControl_Type(Integer32):
    """Custom type prtExPh1MlQ50BwControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("annexA", 3),
          ("annexB", 4))
    )


_PrtExPh1MlQ50BwControl_Type.__name__ = "Integer32"
_PrtExPh1MlQ50BwControl_Object = MibTableColumn
prtExPh1MlQ50BwControl = _PrtExPh1MlQ50BwControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 28),
    _PrtExPh1MlQ50BwControl_Type()
)
prtExPh1MlQ50BwControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlQ50BwControl.setStatus("current")


class _PrtExPh1MlQ50SignalPair_Type(Integer32):
    """Custom type prtExPh1MlQ50SignalPair based on Integer32"""
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
          ("aAndB", 2),
          ("cAndD", 3))
    )


_PrtExPh1MlQ50SignalPair_Type.__name__ = "Integer32"
_PrtExPh1MlQ50SignalPair_Object = MibTableColumn
prtExPh1MlQ50SignalPair = _PrtExPh1MlQ50SignalPair_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 29),
    _PrtExPh1MlQ50SignalPair_Type()
)
prtExPh1MlQ50SignalPair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlQ50SignalPair.setStatus("current")


class _PrtExPh1MlInternalSwitch_Type(Integer32):
    """Custom type prtExPh1MlInternalSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_PrtExPh1MlInternalSwitch_Type.__name__ = "Integer32"
_PrtExPh1MlInternalSwitch_Object = MibTableColumn
prtExPh1MlInternalSwitch = _PrtExPh1MlInternalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 30),
    _PrtExPh1MlInternalSwitch_Type()
)
prtExPh1MlInternalSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlInternalSwitch.setStatus("current")


class _PrtExPh1MlSigService_Type(Integer32):
    """Custom type prtExPh1MlSigService based on Integer32"""
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
          ("normal", 2),
          ("advanced", 3))
    )


_PrtExPh1MlSigService_Type.__name__ = "Integer32"
_PrtExPh1MlSigService_Object = MibTableColumn
prtExPh1MlSigService = _PrtExPh1MlSigService_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 31),
    _PrtExPh1MlSigService_Type()
)
prtExPh1MlSigService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlSigService.setStatus("current")
_PrtExPh1MlFragmentSize_Type = Integer32
_PrtExPh1MlFragmentSize_Object = MibTableColumn
prtExPh1MlFragmentSize = _PrtExPh1MlFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 1, 1, 32),
    _PrtExPh1MlFragmentSize_Type()
)
prtExPh1MlFragmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlFragmentSize.setStatus("current")
_PrtExPh1MlTsTable_Object = MibTable
prtExPh1MlTsTable = _PrtExPh1MlTsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    prtExPh1MlTsTable.setStatus("current")
_PrtExPh1MlTsEntry_Object = MibTableRow
prtExPh1MlTsEntry = _PrtExPh1MlTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1)
)
prtExPh1MlTsEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExPh1MlTsCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPh1MlTsSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPh1MlTsPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPh1MlTsIdx"),
)
if mibBuilder.loadTexts:
    prtExPh1MlTsEntry.setStatus("current")


class _PrtExPh1MlTsCnfgIdx_Type(Integer32):
    """Custom type prtExPh1MlTsCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExPh1MlTsCnfgIdx_Type.__name__ = "Integer32"
_PrtExPh1MlTsCnfgIdx_Object = MibTableColumn
prtExPh1MlTsCnfgIdx = _PrtExPh1MlTsCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 1),
    _PrtExPh1MlTsCnfgIdx_Type()
)
prtExPh1MlTsCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPh1MlTsCnfgIdx.setStatus("current")


class _PrtExPh1MlTsSltIdx_Type(Integer32):
    """Custom type prtExPh1MlTsSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExPh1MlTsSltIdx_Type.__name__ = "Integer32"
_PrtExPh1MlTsSltIdx_Object = MibTableColumn
prtExPh1MlTsSltIdx = _PrtExPh1MlTsSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 2),
    _PrtExPh1MlTsSltIdx_Type()
)
prtExPh1MlTsSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPh1MlTsSltIdx.setStatus("current")


class _PrtExPh1MlTsPrtIdx_Type(Integer32):
    """Custom type prtExPh1MlTsPrtIdx based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("exPrt11", 11),
          ("exPrt12", 12),
          ("exPrt13", 13),
          ("exPrt14", 14),
          ("exPrt15", 15),
          ("exPrt16", 16),
          ("exPrt17", 17),
          ("exPrt18", 18),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108),
          ("inPrt9", 109),
          ("inPrt10", 110),
          ("inPrt11", 111),
          ("inPrt12", 112),
          ("inPrt13", 113),
          ("inPrt14", 114),
          ("inPrt15", 115),
          ("inPrt16", 116),
          ("inPrt17", 117),
          ("inPrt18", 118),
          ("inPrt19", 119),
          ("inPrt20", 120))
    )


_PrtExPh1MlTsPrtIdx_Type.__name__ = "Integer32"
_PrtExPh1MlTsPrtIdx_Object = MibTableColumn
prtExPh1MlTsPrtIdx = _PrtExPh1MlTsPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 3),
    _PrtExPh1MlTsPrtIdx_Type()
)
prtExPh1MlTsPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPh1MlTsPrtIdx.setStatus("current")
_PrtExPh1MlTsIdx_Type = Integer32
_PrtExPh1MlTsIdx_Object = MibTableColumn
prtExPh1MlTsIdx = _PrtExPh1MlTsIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 4),
    _PrtExPh1MlTsIdx_Type()
)
prtExPh1MlTsIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPh1MlTsIdx.setStatus("current")


class _PrtExPh1MlTsIConSlot_Type(Integer32):
    """Custom type prtExPh1MlTsIConSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("noConnect", 2),
          ("split", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExPh1MlTsIConSlot_Type.__name__ = "Integer32"
_PrtExPh1MlTsIConSlot_Object = MibTableColumn
prtExPh1MlTsIConSlot = _PrtExPh1MlTsIConSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 5),
    _PrtExPh1MlTsIConSlot_Type()
)
prtExPh1MlTsIConSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsIConSlot.setStatus("current")
_PrtExPh1MlTsIConPrt_Type = Integer32
_PrtExPh1MlTsIConPrt_Object = MibTableColumn
prtExPh1MlTsIConPrt = _PrtExPh1MlTsIConPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 6),
    _PrtExPh1MlTsIConPrt_Type()
)
prtExPh1MlTsIConPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsIConPrt.setStatus("current")
_PrtExPh1MlTsIConTs_Type = Integer32
_PrtExPh1MlTsIConTs_Object = MibTableColumn
prtExPh1MlTsIConTs = _PrtExPh1MlTsIConTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 7),
    _PrtExPh1MlTsIConTs_Type()
)
prtExPh1MlTsIConTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsIConTs.setStatus("current")
_PrtExPh1MlTsExt_Type = ObjectIdentifier
_PrtExPh1MlTsExt_Object = MibTableColumn
prtExPh1MlTsExt = _PrtExPh1MlTsExt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 8),
    _PrtExPh1MlTsExt_Type()
)
prtExPh1MlTsExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPh1MlTsExt.setStatus("current")


class _PrtExPh1MlTsTest_Type(Integer32):
    """Custom type prtExPh1MlTsTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              9,
              18,
              30,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("localLoop", 2),
          ("remoteLoop", 3),
          ("remoteBert", 8),
          ("localToneInjection", 9),
          ("remoteToneInjection", 18),
          ("localBert", 30),
          ("split", 254),
          ("notApplicable", 255))
    )


_PrtExPh1MlTsTest_Type.__name__ = "Integer32"
_PrtExPh1MlTsTest_Object = MibTableColumn
prtExPh1MlTsTest = _PrtExPh1MlTsTest_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 9),
    _PrtExPh1MlTsTest_Type()
)
prtExPh1MlTsTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsTest.setStatus("current")


class _PrtExPh1MlTsType_Type(Integer32):
    """Custom type prtExPh1MlTsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("data", 3),
          ("voice", 4),
          ("cas", 5),
          ("ss7", 6),
          ("transparent", 7),
          ("data2", 8),
          ("data3", 9),
          ("data4", 10),
          ("ss7n2", 11),
          ("hdlcV2Compatible", 12),
          ("subCh1", 13),
          ("subCh2", 14),
          ("subCh3", 15),
          ("subCh4", 16),
          ("subCh5", 17),
          ("subCh6", 18),
          ("subCh7", 19),
          ("subCh8", 20),
          ("trau", 21),
          ("qmux", 22),
          ("dynamic", 23),
          ("signaling", 24),
          ("notApplicable", 255))
    )


_PrtExPh1MlTsType_Type.__name__ = "Integer32"
_PrtExPh1MlTsType_Object = MibTableColumn
prtExPh1MlTsType = _PrtExPh1MlTsType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 10),
    _PrtExPh1MlTsType_Type()
)
prtExPh1MlTsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsType.setStatus("current")
_PrtExPh1MlTsBundle_Type = Integer32
_PrtExPh1MlTsBundle_Object = MibTableColumn
prtExPh1MlTsBundle = _PrtExPh1MlTsBundle_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 11),
    _PrtExPh1MlTsBundle_Type()
)
prtExPh1MlTsBundle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsBundle.setStatus("current")
_PrtExPh1MlTsTestDuration_Type = Integer32
_PrtExPh1MlTsTestDuration_Object = MibTableColumn
prtExPh1MlTsTestDuration = _PrtExPh1MlTsTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 12),
    _PrtExPh1MlTsTestDuration_Type()
)
prtExPh1MlTsTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsTestDuration.setStatus("current")


class _PrtExPh1MlTsSubChType_Type(Integer32):
    """Custom type prtExPh1MlTsSubChType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 1),
          ("transparent", 2),
          ("notApplicable", 255))
    )


_PrtExPh1MlTsSubChType_Type.__name__ = "Integer32"
_PrtExPh1MlTsSubChType_Object = MibTableColumn
prtExPh1MlTsSubChType = _PrtExPh1MlTsSubChType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 13),
    _PrtExPh1MlTsSubChType_Type()
)
prtExPh1MlTsSubChType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsSubChType.setStatus("current")
_PrtExPh1MlTsSubChMask_Type = Integer32
_PrtExPh1MlTsSubChMask_Object = MibTableColumn
prtExPh1MlTsSubChMask = _PrtExPh1MlTsSubChMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 14),
    _PrtExPh1MlTsSubChMask_Type()
)
prtExPh1MlTsSubChMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsSubChMask.setStatus("current")


class _PrtExPh1MlTsChRate_Type(Integer32):
    """Custom type prtExPh1MlTsChRate based on Integer32"""
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
        *(("notApplicable", 1),
          ("r16Kbps", 2),
          ("r32Kbps", 3),
          ("r64Kbps", 4),
          ("r8Kbps", 5),
          ("auto", 6))
    )


_PrtExPh1MlTsChRate_Type.__name__ = "Integer32"
_PrtExPh1MlTsChRate_Object = MibTableColumn
prtExPh1MlTsChRate = _PrtExPh1MlTsChRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 15),
    _PrtExPh1MlTsChRate_Type()
)
prtExPh1MlTsChRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsChRate.setStatus("current")


class _PrtExPh1MlTsByteReversal_Type(Integer32):
    """Custom type prtExPh1MlTsByteReversal based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExPh1MlTsByteReversal_Type.__name__ = "Integer32"
_PrtExPh1MlTsByteReversal_Object = MibTableColumn
prtExPh1MlTsByteReversal = _PrtExPh1MlTsByteReversal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 16),
    _PrtExPh1MlTsByteReversal_Type()
)
prtExPh1MlTsByteReversal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsByteReversal.setStatus("current")


class _PrtExPh1MlTsSigProfile_Type(Integer32):
    """Custom type prtExPh1MlTsSigProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("p1", 3),
          ("p2", 4),
          ("p3", 5),
          ("p4", 6),
          ("p5", 7))
    )


_PrtExPh1MlTsSigProfile_Type.__name__ = "Integer32"
_PrtExPh1MlTsSigProfile_Object = MibTableColumn
prtExPh1MlTsSigProfile = _PrtExPh1MlTsSigProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 2, 1, 17),
    _PrtExPh1MlTsSigProfile_Type()
)
prtExPh1MlTsSigProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPh1MlTsSigProfile.setStatus("current")
_PrtInPh1MlCnfgTable_Object = MibTable
prtInPh1MlCnfgTable = _PrtInPh1MlCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    prtInPh1MlCnfgTable.setStatus("current")
_PrtInPh1MlCnfgEntry_Object = MibTableRow
prtInPh1MlCnfgEntry = _PrtInPh1MlCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1)
)
prtInPh1MlCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtInPh1MlCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtInPh1MlSltType"),
    (0, "RAD-Mpmx-MIB", "prtInPh1MlPrtIdx"),
)
if mibBuilder.loadTexts:
    prtInPh1MlCnfgEntry.setStatus("current")


class _PrtInPh1MlCnfgIdx_Type(Integer32):
    """Custom type prtInPh1MlCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtInPh1MlCnfgIdx_Type.__name__ = "Integer32"
_PrtInPh1MlCnfgIdx_Object = MibTableColumn
prtInPh1MlCnfgIdx = _PrtInPh1MlCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 1),
    _PrtInPh1MlCnfgIdx_Type()
)
prtInPh1MlCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInPh1MlCnfgIdx.setStatus("current")


class _PrtInPh1MlSltType_Type(Integer32):
    """Custom type prtInPh1MlSltType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtInPh1MlSltType_Type.__name__ = "Integer32"
_PrtInPh1MlSltType_Object = MibTableColumn
prtInPh1MlSltType = _PrtInPh1MlSltType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 2),
    _PrtInPh1MlSltType_Type()
)
prtInPh1MlSltType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInPh1MlSltType.setStatus("current")
_PrtInPh1MlPrtIdx_Type = Integer32
_PrtInPh1MlPrtIdx_Object = MibTableColumn
prtInPh1MlPrtIdx = _PrtInPh1MlPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 3),
    _PrtInPh1MlPrtIdx_Type()
)
prtInPh1MlPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInPh1MlPrtIdx.setStatus("current")


class _PrtInPh1MlConnect_Type(Integer32):
    """Custom type prtInPh1MlConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtInPh1MlConnect_Type.__name__ = "Integer32"
_PrtInPh1MlConnect_Object = MibTableColumn
prtInPh1MlConnect = _PrtInPh1MlConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 4),
    _PrtInPh1MlConnect_Type()
)
prtInPh1MlConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlConnect.setStatus("current")


class _PrtInPh1MlRate_Type(Integer32):
    """Custom type prtInPh1MlRate based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              100)
        )
    )
    namedValues = NamedValues(
        *(("r1x56eq56Kbps", 1),
          ("r1x64eq64Kbps", 2),
          ("r2x56eq112Kbps", 3),
          ("r2x64eq128Kbps", 4),
          ("r3x56eq168Kbps", 5),
          ("r3x64eq192Kbps", 6),
          ("r4x56eq224Kbps", 7),
          ("r4x64eq256Kbps", 8),
          ("r5x56eq280Kbps", 9),
          ("r5x64eq320Kbps", 10),
          ("r6x56eq336Kbps", 11),
          ("r6x64eq384Kbps", 12),
          ("r7x56eq392Kbps", 13),
          ("r7x64eq448Kbps", 14),
          ("r8x56eq448Kbps", 15),
          ("r8x64eq512Kbps", 16),
          ("r9x56eq504Kbps", 17),
          ("r9x64eq576Kbps", 18),
          ("r10x56eq560Kbps", 19),
          ("r10x64eq640Kbps", 20),
          ("r11x56eq616Kbps", 21),
          ("r11x64eq704Kbps", 22),
          ("r12x56eq672Kbps", 23),
          ("r12x64eq768Kbps", 24),
          ("r13x56eq728Kbps", 25),
          ("r13x64eq832Kbps", 26),
          ("r14x56eq784Kbps", 27),
          ("r14x64eq896Kbps", 28),
          ("r15x56eq840Kbps", 29),
          ("r15x64eq960Kbps", 30),
          ("r16x56eq896Kbps", 31),
          ("r16x64eq1024Kbps", 32),
          ("r17x56eq952Kbps", 33),
          ("r17x64eq1088Kbps", 34),
          ("r18x56eq1008Kbps", 35),
          ("r18x64eq1152Kbps", 36),
          ("r19x56eq1064Kbps", 37),
          ("r19x64eq1216Kbps", 38),
          ("r20x56eq1120Kbps", 39),
          ("r20x64eq1280Kbps", 40),
          ("r21x56eq1176Kbps", 41),
          ("r21x64eq1344Kbps", 42),
          ("r22x56eq1232Kbps", 43),
          ("r22x64eq1408Kbps", 44),
          ("r23x56eq1288Kbps", 45),
          ("r23x64eq1472Kbps", 46),
          ("r24x56eq1344Kbps", 47),
          ("r24x64eq1536Kbps", 48),
          ("r25x56eq1400Kbps", 49),
          ("r25x64eq1600Kbps", 50),
          ("r26x56eq1456Kbps", 51),
          ("r26x64eq1664Kbps", 52),
          ("r27x56eq1512Kbps", 53),
          ("r27x64eq1728Kbps", 54),
          ("r28x56eq1568Kbps", 55),
          ("r28x64eq1792Kbps", 56),
          ("r29x56eq1624Kbps", 57),
          ("r29x64eq1856Kbps", 58),
          ("r30x56eq1680Kbps", 59),
          ("r30x64eq1920Kbps", 60),
          ("r31x56eq1736Kbps", 61),
          ("r31x64eq1984Kbps", 62),
          ("r32x56eq1792Kbps", 63),
          ("r32x64eq2048Kbps", 64),
          ("r1x1dot5eq1dot5M", 65),
          ("r2x1dot5eq3M", 66),
          ("r3x1dot5eq4dot5M", 67),
          ("r4x1dot5eq6M", 68),
          ("r5x1dot5eq7dot5M", 69),
          ("r6x1dot5eq9M", 70),
          ("r7x1dot5eq10dot5M", 71),
          ("r8x1dot5eq12M", 72),
          ("r1x2Meq2M", 73),
          ("r2x2Meq4M", 74),
          ("r3x2Meq6M", 75),
          ("r4x2Meq8M", 76),
          ("r5x2Meq10M", 77),
          ("r6x2Meq12M", 78),
          ("r7x2Meq14M", 79),
          ("r8x2Meq16M", 80),
          ("noRate", 100))
    )


_PrtInPh1MlRate_Type.__name__ = "Integer32"
_PrtInPh1MlRate_Object = MibTableColumn
prtInPh1MlRate = _PrtInPh1MlRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 5),
    _PrtInPh1MlRate_Type()
)
prtInPh1MlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlRate.setStatus("current")


class _PrtInPh1MlProtocol_Type(Integer32):
    """Custom type prtInPh1MlProtocol based on Integer32"""
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
        *(("fr", 1),
          ("frPlus", 2),
          ("pCellRelay", 3),
          ("hdlcSdlc", 4),
          ("transparentHdlc", 5),
          ("ciscoBridgedEth", 6))
    )


_PrtInPh1MlProtocol_Type.__name__ = "Integer32"
_PrtInPh1MlProtocol_Object = MibTableColumn
prtInPh1MlProtocol = _PrtInPh1MlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 6),
    _PrtInPh1MlProtocol_Type()
)
prtInPh1MlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlProtocol.setStatus("current")


class _PrtInPh1MlConnectionTyp_Type(Integer32):
    """Custom type prtInPh1MlConnectionTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sameNetManaged", 1),
          ("sameNetNotMana", 2),
          ("user", 3),
          ("otherNet", 4),
          ("pubNet", 5),
          ("notApplicable", 255))
    )


_PrtInPh1MlConnectionTyp_Type.__name__ = "Integer32"
_PrtInPh1MlConnectionTyp_Object = MibTableColumn
prtInPh1MlConnectionTyp = _PrtInPh1MlConnectionTyp_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 7),
    _PrtInPh1MlConnectionTyp_Type()
)
prtInPh1MlConnectionTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlConnectionTyp.setStatus("current")


class _PrtInPh1MlCongResponse_Type(Integer32):
    """Custom type prtInPh1MlCongResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("flowControl", 3))
    )


_PrtInPh1MlCongResponse_Type.__name__ = "Integer32"
_PrtInPh1MlCongResponse_Object = MibTableColumn
prtInPh1MlCongResponse = _PrtInPh1MlCongResponse_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 8),
    _PrtInPh1MlCongResponse_Type()
)
prtInPh1MlCongResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlCongResponse.setStatus("current")
_PrtInPh1MlCongLevel_Type = Integer32
_PrtInPh1MlCongLevel_Object = MibTableColumn
prtInPh1MlCongLevel = _PrtInPh1MlCongLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 9),
    _PrtInPh1MlCongLevel_Type()
)
prtInPh1MlCongLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlCongLevel.setStatus("current")


class _PrtInPh1MlTc_Type(Integer32):
    """Custom type prtInPh1MlTc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tc1sec", 1),
          ("tc2sec", 2),
          ("tc3sec", 3),
          ("tc4sec", 4),
          ("notApplicable", 255))
    )


_PrtInPh1MlTc_Type.__name__ = "Integer32"
_PrtInPh1MlTc_Object = MibTableColumn
prtInPh1MlTc = _PrtInPh1MlTc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 10),
    _PrtInPh1MlTc_Type()
)
prtInPh1MlTc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlTc.setStatus("current")


class _PrtInPh1MlFlowControl_Type(Integer32):
    """Custom type prtInPh1MlFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("fecnBecn", 3))
    )


_PrtInPh1MlFlowControl_Type.__name__ = "Integer32"
_PrtInPh1MlFlowControl_Object = MibTableColumn
prtInPh1MlFlowControl = _PrtInPh1MlFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 11),
    _PrtInPh1MlFlowControl_Type()
)
prtInPh1MlFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlFlowControl.setStatus("current")


class _PrtInPh1MlSegment_Type(Integer32):
    """Custom type prtInPh1MlSegment based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("s36Byte", 2),
          ("s150Byte", 3),
          ("s264Byte", 4),
          ("s378Byte", 5),
          ("s492Byte", 6),
          ("s236Byte", 7),
          ("s472Byte", 8),
          ("s708Byte", 9),
          ("s944Byte", 10),
          ("s1180Byte", 11))
    )


_PrtInPh1MlSegment_Type.__name__ = "Integer32"
_PrtInPh1MlSegment_Object = MibTableColumn
prtInPh1MlSegment = _PrtInPh1MlSegment_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 12),
    _PrtInPh1MlSegment_Type()
)
prtInPh1MlSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlSegment.setStatus("current")


class _PrtInPh1MlFrMngProt_Type(Integer32):
    """Custom type prtInPh1MlFrMngProt based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("lmi", 3),
          ("ansiT1", 4),
          ("annexA", 5))
    )


_PrtInPh1MlFrMngProt_Type.__name__ = "Integer32"
_PrtInPh1MlFrMngProt_Object = MibTableColumn
prtInPh1MlFrMngProt = _PrtInPh1MlFrMngProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 13),
    _PrtInPh1MlFrMngProt_Type()
)
prtInPh1MlFrMngProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlFrMngProt.setStatus("current")


class _PrtInPh1MlEnqPeriod_Type(Integer32):
    """Custom type prtInPh1MlEnqPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_PrtInPh1MlEnqPeriod_Type.__name__ = "Integer32"
_PrtInPh1MlEnqPeriod_Object = MibTableColumn
prtInPh1MlEnqPeriod = _PrtInPh1MlEnqPeriod_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 14),
    _PrtInPh1MlEnqPeriod_Type()
)
prtInPh1MlEnqPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlEnqPeriod.setStatus("current")


class _PrtInPh1MlFullRptPeriod_Type(Integer32):
    """Custom type prtInPh1MlFullRptPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrtInPh1MlFullRptPeriod_Type.__name__ = "Integer32"
_PrtInPh1MlFullRptPeriod_Object = MibTableColumn
prtInPh1MlFullRptPeriod = _PrtInPh1MlFullRptPeriod_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 15),
    _PrtInPh1MlFullRptPeriod_Type()
)
prtInPh1MlFullRptPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlFullRptPeriod.setStatus("current")


class _PrtInPh1MlFrWindowSize_Type(Integer32):
    """Custom type prtInPh1MlFrWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PrtInPh1MlFrWindowSize_Type.__name__ = "Integer32"
_PrtInPh1MlFrWindowSize_Object = MibTableColumn
prtInPh1MlFrWindowSize = _PrtInPh1MlFrWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 16),
    _PrtInPh1MlFrWindowSize_Type()
)
prtInPh1MlFrWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlFrWindowSize.setStatus("current")


class _PrtInPh1MlErrorsThreshold_Type(Integer32):
    """Custom type prtInPh1MlErrorsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PrtInPh1MlErrorsThreshold_Type.__name__ = "Integer32"
_PrtInPh1MlErrorsThreshold_Object = MibTableColumn
prtInPh1MlErrorsThreshold = _PrtInPh1MlErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 17),
    _PrtInPh1MlErrorsThreshold_Type()
)
prtInPh1MlErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlErrorsThreshold.setStatus("current")


class _PrtInPh1MlMaxIdleTime_Type(Integer32):
    """Custom type prtInPh1MlMaxIdleTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_PrtInPh1MlMaxIdleTime_Type.__name__ = "Integer32"
_PrtInPh1MlMaxIdleTime_Object = MibTableColumn
prtInPh1MlMaxIdleTime = _PrtInPh1MlMaxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 18),
    _PrtInPh1MlMaxIdleTime_Type()
)
prtInPh1MlMaxIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlMaxIdleTime.setStatus("current")


class _PrtInPh1MlBearerCh_Type(Integer32):
    """Custom type prtInPh1MlBearerCh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("channelB1", 3),
          ("channelB2", 4),
          ("chB1andchB2", 5),
          ("none", 255))
    )


_PrtInPh1MlBearerCh_Type.__name__ = "Integer32"
_PrtInPh1MlBearerCh_Object = MibTableColumn
prtInPh1MlBearerCh = _PrtInPh1MlBearerCh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 19),
    _PrtInPh1MlBearerCh_Type()
)
prtInPh1MlBearerCh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlBearerCh.setStatus("current")


class _PrtInPh1MlAssociatedExCh_Type(Integer32):
    """Custom type prtInPh1MlAssociatedExCh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("notApplicable", 255))
    )


_PrtInPh1MlAssociatedExCh_Type.__name__ = "Integer32"
_PrtInPh1MlAssociatedExCh_Object = MibTableColumn
prtInPh1MlAssociatedExCh = _PrtInPh1MlAssociatedExCh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 20),
    _PrtInPh1MlAssociatedExCh_Type()
)
prtInPh1MlAssociatedExCh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlAssociatedExCh.setStatus("current")


class _PrtInPh1MlClockEncoding_Type(Integer32):
    """Custom type prtInPh1MlClockEncoding based on Integer32"""
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
        *(("notApplicable", 1),
          ("nrz", 2),
          ("nrzI", 3),
          ("fm0", 4),
          ("manchester", 5),
          ("diffManchester", 6))
    )


_PrtInPh1MlClockEncoding_Type.__name__ = "Integer32"
_PrtInPh1MlClockEncoding_Object = MibTableColumn
prtInPh1MlClockEncoding = _PrtInPh1MlClockEncoding_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 21),
    _PrtInPh1MlClockEncoding_Type()
)
prtInPh1MlClockEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlClockEncoding.setStatus("current")


class _PrtInPh1MlMinSeparators_Type(Integer32):
    """Custom type prtInPh1MlMinSeparators based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PrtInPh1MlMinSeparators_Type.__name__ = "Integer32"
_PrtInPh1MlMinSeparators_Object = MibTableColumn
prtInPh1MlMinSeparators = _PrtInPh1MlMinSeparators_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 22),
    _PrtInPh1MlMinSeparators_Type()
)
prtInPh1MlMinSeparators.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlMinSeparators.setStatus("current")


class _PrtInPh1MlCcittCrc_Type(Integer32):
    """Custom type prtInPh1MlCcittCrc based on Integer32"""
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
          ("crc16", 2),
          ("crc32", 3))
    )


_PrtInPh1MlCcittCrc_Type.__name__ = "Integer32"
_PrtInPh1MlCcittCrc_Object = MibTableColumn
prtInPh1MlCcittCrc = _PrtInPh1MlCcittCrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 23),
    _PrtInPh1MlCcittCrc_Type()
)
prtInPh1MlCcittCrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlCcittCrc.setStatus("current")


class _PrtInPh1MlFrameSeparator_Type(Integer32):
    """Custom type prtInPh1MlFrameSeparator based on Integer32"""
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
          ("idles", 2),
          ("flags", 3))
    )


_PrtInPh1MlFrameSeparator_Type.__name__ = "Integer32"
_PrtInPh1MlFrameSeparator_Object = MibTableColumn
prtInPh1MlFrameSeparator = _PrtInPh1MlFrameSeparator_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 3, 1, 24),
    _PrtInPh1MlFrameSeparator_Type()
)
prtInPh1MlFrameSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlFrameSeparator.setStatus("current")
_PrtInPh1MlDlciTable_Object = MibTable
prtInPh1MlDlciTable = _PrtInPh1MlDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4)
)
if mibBuilder.loadTexts:
    prtInPh1MlDlciTable.setStatus("current")
_PrtInPh1MlDlciEntry_Object = MibTableRow
prtInPh1MlDlciEntry = _PrtInPh1MlDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1)
)
prtInPh1MlDlciEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtInPh1MlDlciCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtInPh1MlDlciSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtInPh1MlDlciPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtInPh1MlDlciIdx"),
)
if mibBuilder.loadTexts:
    prtInPh1MlDlciEntry.setStatus("current")


class _PrtInPh1MlDlciCnfgIdx_Type(Integer32):
    """Custom type prtInPh1MlDlciCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtInPh1MlDlciCnfgIdx_Type.__name__ = "Integer32"
_PrtInPh1MlDlciCnfgIdx_Object = MibTableColumn
prtInPh1MlDlciCnfgIdx = _PrtInPh1MlDlciCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 1),
    _PrtInPh1MlDlciCnfgIdx_Type()
)
prtInPh1MlDlciCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInPh1MlDlciCnfgIdx.setStatus("current")


class _PrtInPh1MlDlciSltIdx_Type(Integer32):
    """Custom type prtInPh1MlDlciSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInPh1MlDlciSltIdx_Type.__name__ = "Integer32"
_PrtInPh1MlDlciSltIdx_Object = MibTableColumn
prtInPh1MlDlciSltIdx = _PrtInPh1MlDlciSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 2),
    _PrtInPh1MlDlciSltIdx_Type()
)
prtInPh1MlDlciSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInPh1MlDlciSltIdx.setStatus("current")


class _PrtInPh1MlDlciPrtIdx_Type(Integer32):
    """Custom type prtInPh1MlDlciPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103))
    )


_PrtInPh1MlDlciPrtIdx_Type.__name__ = "Integer32"
_PrtInPh1MlDlciPrtIdx_Object = MibTableColumn
prtInPh1MlDlciPrtIdx = _PrtInPh1MlDlciPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 3),
    _PrtInPh1MlDlciPrtIdx_Type()
)
prtInPh1MlDlciPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInPh1MlDlciPrtIdx.setStatus("current")


class _PrtInPh1MlDlciIdx_Type(Integer32):
    """Custom type prtInPh1MlDlciIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 991),
    )


_PrtInPh1MlDlciIdx_Type.__name__ = "Integer32"
_PrtInPh1MlDlciIdx_Object = MibTableColumn
prtInPh1MlDlciIdx = _PrtInPh1MlDlciIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 4),
    _PrtInPh1MlDlciIdx_Type()
)
prtInPh1MlDlciIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInPh1MlDlciIdx.setStatus("current")


class _PrtInPh1MlDlciValid_Type(Integer32):
    """Custom type prtInPh1MlDlciValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtInPh1MlDlciValid_Type.__name__ = "Integer32"
_PrtInPh1MlDlciValid_Object = MibTableColumn
prtInPh1MlDlciValid = _PrtInPh1MlDlciValid_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 5),
    _PrtInPh1MlDlciValid_Type()
)
prtInPh1MlDlciValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlDlciValid.setStatus("current")


class _PrtInPh1MlDlciIConSlt_Type(Integer32):
    """Custom type prtInPh1MlDlciIConSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("cl", 3),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInPh1MlDlciIConSlt_Type.__name__ = "Integer32"
_PrtInPh1MlDlciIConSlt_Object = MibTableColumn
prtInPh1MlDlciIConSlt = _PrtInPh1MlDlciIConSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 6),
    _PrtInPh1MlDlciIConSlt_Type()
)
prtInPh1MlDlciIConSlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlDlciIConSlt.setStatus("current")


class _PrtInPh1MlDlciIConPrt_Type(Integer32):
    """Custom type prtInPh1MlDlciIConPrt based on Integer32"""
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
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("clNMS", 99),
          ("noConnect", 100),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108),
          ("inPrt9", 109),
          ("inPrt10", 110),
          ("inPrt11", 111),
          ("inPrt12", 112))
    )


_PrtInPh1MlDlciIConPrt_Type.__name__ = "Integer32"
_PrtInPh1MlDlciIConPrt_Object = MibTableColumn
prtInPh1MlDlciIConPrt = _PrtInPh1MlDlciIConPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 7),
    _PrtInPh1MlDlciIConPrt_Type()
)
prtInPh1MlDlciIConPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlDlciIConPrt.setStatus("current")


class _PrtInPh1MlDlciIConDlci_Type(Integer32):
    """Custom type prtInPh1MlDlciIConDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 991),
    )


_PrtInPh1MlDlciIConDlci_Type.__name__ = "Integer32"
_PrtInPh1MlDlciIConDlci_Object = MibTableColumn
prtInPh1MlDlciIConDlci = _PrtInPh1MlDlciIConDlci_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 8),
    _PrtInPh1MlDlciIConDlci_Type()
)
prtInPh1MlDlciIConDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlDlciIConDlci.setStatus("current")


class _PrtInPh1MlDlciTxBc_Type(Integer32):
    """Custom type prtInPh1MlDlciTxBc based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("txBc9600bps", 3),
          ("txBc14200bps", 4),
          ("txBc19200bps", 5),
          ("txBc28800bps", 6),
          ("txBc32000bps", 7),
          ("txBc38400bps", 8),
          ("txBc48000bps", 9),
          ("txBc56000bps", 10),
          ("txBc57600bps", 11),
          ("txBc64Kbps", 12),
          ("txBc128Kbps", 13),
          ("txBc192Kbps", 14),
          ("txBc256Kbps", 15),
          ("txBc320Kbps", 16),
          ("txBc384Kbps", 17),
          ("txBc448Kbps", 18),
          ("txBc512Kbps", 19),
          ("txBc768Kbps", 20),
          ("txBc1024Kbps", 21))
    )


_PrtInPh1MlDlciTxBc_Type.__name__ = "Integer32"
_PrtInPh1MlDlciTxBc_Object = MibTableColumn
prtInPh1MlDlciTxBc = _PrtInPh1MlDlciTxBc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 9),
    _PrtInPh1MlDlciTxBc_Type()
)
prtInPh1MlDlciTxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlDlciTxBc.setStatus("current")


class _PrtInPh1MlDlciTxBe_Type(Integer32):
    """Custom type prtInPh1MlDlciTxBe based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("txBe9600bps", 3),
          ("txBe14200bps", 4),
          ("txBe19200bps", 5),
          ("txBe28800bps", 6),
          ("txBe32000bps", 7),
          ("txBe38400bps", 8),
          ("txBe48000bps", 9),
          ("txBe56000bps", 10),
          ("txBe57600bps", 11),
          ("txBe64Kbps", 12),
          ("txBe128Kbps", 13),
          ("txBe192Kbps", 14),
          ("txBe256Kbps", 15),
          ("txBe320Kbps", 16),
          ("txBe384Kbps", 17),
          ("txBe448Kbps", 18),
          ("txBe512Kbps", 19),
          ("txBe768Kbps", 20),
          ("txBe1024Kbps", 21))
    )


_PrtInPh1MlDlciTxBe_Type.__name__ = "Integer32"
_PrtInPh1MlDlciTxBe_Object = MibTableColumn
prtInPh1MlDlciTxBe = _PrtInPh1MlDlciTxBe_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 10),
    _PrtInPh1MlDlciTxBe_Type()
)
prtInPh1MlDlciTxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlDlciTxBe.setStatus("current")


class _PrtInPh1MlDlciRxBc_Type(Integer32):
    """Custom type prtInPh1MlDlciRxBc based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("rxBc9600bps", 3),
          ("rxBc14200bps", 4),
          ("rxBc19200bps", 5),
          ("rxBc28800bps", 6),
          ("rxBc32000bps", 7),
          ("rxBc38400bps", 8),
          ("rxBc48000bps", 9),
          ("rxBc56000bps", 10),
          ("rxBc57600bps", 11),
          ("rxBc64Kbps", 12),
          ("rxBc128Kbps", 13),
          ("rxBc192Kbps", 14),
          ("rxBc256Kbps", 15),
          ("rxBc320Kbps", 16),
          ("rxBc384Kbps", 17),
          ("rxBc448Kbps", 18),
          ("rxBc512Kbps", 19),
          ("rxBc768Kbps", 20),
          ("rxBc1024Kbps", 21))
    )


_PrtInPh1MlDlciRxBc_Type.__name__ = "Integer32"
_PrtInPh1MlDlciRxBc_Object = MibTableColumn
prtInPh1MlDlciRxBc = _PrtInPh1MlDlciRxBc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 11),
    _PrtInPh1MlDlciRxBc_Type()
)
prtInPh1MlDlciRxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlDlciRxBc.setStatus("current")


class _PrtInPh1MlDlciRxBe_Type(Integer32):
    """Custom type prtInPh1MlDlciRxBe based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("rxBe9600bps", 3),
          ("rxBe14200bps", 4),
          ("rxBe19200bps", 5),
          ("rxBe28800bps", 6),
          ("rxBe32000bps", 7),
          ("rxBe38400bps", 8),
          ("rxBe48000bps", 9),
          ("rxBe56000bps", 10),
          ("rxBe57600bps", 11),
          ("rxBe64Kbps", 12),
          ("rxBe128Kbps", 13),
          ("rxBe192Kbps", 14),
          ("rxBe256Kbps", 15),
          ("rxBe320Kbps", 16),
          ("rxBe384Kbps", 17),
          ("rxBe448Kbps", 18),
          ("rxBe512Kbps", 19),
          ("rxBe768Kbps", 20),
          ("rxBe1024Kbps", 21))
    )


_PrtInPh1MlDlciRxBe_Type.__name__ = "Integer32"
_PrtInPh1MlDlciRxBe_Object = MibTableColumn
prtInPh1MlDlciRxBe = _PrtInPh1MlDlciRxBe_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 12),
    _PrtInPh1MlDlciRxBe_Type()
)
prtInPh1MlDlciRxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlDlciRxBe.setStatus("current")


class _PrtInPh1MlDlciPriority_Type(Integer32):
    """Custom type prtInPh1MlDlciPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PrtInPh1MlDlciPriority_Type.__name__ = "Integer32"
_PrtInPh1MlDlciPriority_Object = MibTableColumn
prtInPh1MlDlciPriority = _PrtInPh1MlDlciPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 13),
    _PrtInPh1MlDlciPriority_Type()
)
prtInPh1MlDlciPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInPh1MlDlciPriority.setStatus("current")


class _PrtInPh1MlDlciStatus_Type(Integer32):
    """Custom type prtInPh1MlDlciStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2))
    )


_PrtInPh1MlDlciStatus_Type.__name__ = "Integer32"
_PrtInPh1MlDlciStatus_Object = MibTableColumn
prtInPh1MlDlciStatus = _PrtInPh1MlDlciStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 4, 1, 14),
    _PrtInPh1MlDlciStatus_Type()
)
prtInPh1MlDlciStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInPh1MlDlciStatus.setStatus("current")
_PrtPhMlCnfgTable_Object = MibTable
prtPhMlCnfgTable = _PrtPhMlCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    prtPhMlCnfgTable.setStatus("current")
_PrtPhMlCnfgEntry_Object = MibTableRow
prtPhMlCnfgEntry = _PrtPhMlCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1)
)
prtPhMlCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtPhMlCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtPhMlSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtPhMlPrtIdx"),
)
if mibBuilder.loadTexts:
    prtPhMlCnfgEntry.setStatus("current")


class _PrtPhMlCnfgIdx_Type(Integer32):
    """Custom type prtPhMlCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtPhMlCnfgIdx_Type.__name__ = "Integer32"
_PrtPhMlCnfgIdx_Object = MibTableColumn
prtPhMlCnfgIdx = _PrtPhMlCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 1),
    _PrtPhMlCnfgIdx_Type()
)
prtPhMlCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhMlCnfgIdx.setStatus("current")


class _PrtPhMlSltIdx_Type(Integer32):
    """Custom type prtPhMlSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtPhMlSltIdx_Type.__name__ = "Integer32"
_PrtPhMlSltIdx_Object = MibTableColumn
prtPhMlSltIdx = _PrtPhMlSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 2),
    _PrtPhMlSltIdx_Type()
)
prtPhMlSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhMlSltIdx.setStatus("current")


class _PrtPhMlPrtIdx_Type(Integer32):
    """Custom type prtPhMlPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exPrt1", 1)
    )


_PrtPhMlPrtIdx_Type.__name__ = "Integer32"
_PrtPhMlPrtIdx_Object = MibTableColumn
prtPhMlPrtIdx = _PrtPhMlPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 3),
    _PrtPhMlPrtIdx_Type()
)
prtPhMlPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtPhMlPrtIdx.setStatus("current")


class _PrtPhMlConnect_Type(Integer32):
    """Custom type prtPhMlConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtPhMlConnect_Type.__name__ = "Integer32"
_PrtPhMlConnect_Object = MibTableColumn
prtPhMlConnect = _PrtPhMlConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 4),
    _PrtPhMlConnect_Type()
)
prtPhMlConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlConnect.setStatus("current")


class _PrtPhMlRate_Type(Integer32):
    """Custom type prtPhMlRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              10,
              12,
              14,
              16,
              18,
              20,
              22,
              24,
              26,
              28,
              30,
              32,
              34,
              36,
              38,
              40,
              42,
              44,
              46,
              48,
              50,
              52,
              54,
              56,
              58,
              60,
              62,
              64,
              70)
        )
    )
    namedValues = NamedValues(
        *(("r1x64eq64Kbps", 2),
          ("r2x64eq128Kbps", 4),
          ("r3x64eq192Kbps", 6),
          ("r4x64eq256Kbps", 8),
          ("r5x64eq320Kbps", 10),
          ("r6x64eq384Kbps", 12),
          ("r7x64eq448Kbps", 14),
          ("r8x64eq512Kbps", 16),
          ("r9x64eq576Kbps", 18),
          ("r10x64eq640Kbps", 20),
          ("r11x64eq704Kbps", 22),
          ("r12x64eq768Kbps", 24),
          ("r13x64eq832Kbps", 26),
          ("r14x64eq896Kbps", 28),
          ("r15x64eq960Kbps", 30),
          ("r16x64eq1024Kbps", 32),
          ("r17x64eq1088Kbps", 34),
          ("r18x64eq1152Kbps", 36),
          ("r19x64eq1216Kbps", 38),
          ("r20x64eq1280Kbps", 40),
          ("r21x64eq1344Kbps", 42),
          ("r22x64eq1408Kbps", 44),
          ("r23x64eq1472Kbps", 46),
          ("r24x64eq1536Kbps", 48),
          ("r25x64eq1600Kbps", 50),
          ("r26x64eq1664Kbps", 52),
          ("r27x64eq1728Kbps", 54),
          ("r28x64eq1792Kbps", 56),
          ("r29x64eq1856Kbps", 58),
          ("r30x64eq1920Kbps", 60),
          ("r31x64eq1984Kbps", 62),
          ("r32x64eq2048Kbps", 64),
          ("auto", 70))
    )


_PrtPhMlRate_Type.__name__ = "Integer32"
_PrtPhMlRate_Object = MibTableColumn
prtPhMlRate = _PrtPhMlRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 5),
    _PrtPhMlRate_Type()
)
prtPhMlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlRate.setStatus("current")


class _PrtPhMlCAS_Type(Integer32):
    """Custom type prtPhMlCAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtPhMlCAS_Type.__name__ = "Integer32"
_PrtPhMlCAS_Object = MibTableColumn
prtPhMlCAS = _PrtPhMlCAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 6),
    _PrtPhMlCAS_Type()
)
prtPhMlCAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlCAS.setStatus("current")


class _PrtPhMlClockMode_Type(Integer32):
    """Custom type prtPhMlClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("ext-dce", 3),
          ("dte", 4))
    )


_PrtPhMlClockMode_Type.__name__ = "Integer32"
_PrtPhMlClockMode_Object = MibTableColumn
prtPhMlClockMode = _PrtPhMlClockMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 7),
    _PrtPhMlClockMode_Type()
)
prtPhMlClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlClockMode.setStatus("current")


class _PrtPhMlSatBuffer_Type(Integer32):
    """Custom type prtPhMlSatBuffer based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtPhMlSatBuffer_Type.__name__ = "Integer32"
_PrtPhMlSatBuffer_Object = MibTableColumn
prtPhMlSatBuffer = _PrtPhMlSatBuffer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 8),
    _PrtPhMlSatBuffer_Type()
)
prtPhMlSatBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlSatBuffer.setStatus("current")


class _PrtPhMlDialProcess_Type(Integer32):
    """Custom type prtPhMlDialProcess based on Integer32"""
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
        *(("notApplicable", 1),
          ("no", 2),
          ("callIn", 3),
          ("callOut", 4))
    )


_PrtPhMlDialProcess_Type.__name__ = "Integer32"
_PrtPhMlDialProcess_Object = MibTableColumn
prtPhMlDialProcess = _PrtPhMlDialProcess_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 9),
    _PrtPhMlDialProcess_Type()
)
prtPhMlDialProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlDialProcess.setStatus("current")


class _PrtPhMlSyncRestore_Type(Integer32):
    """Custom type prtPhMlSyncRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PrtPhMlSyncRestore_Type.__name__ = "Integer32"
_PrtPhMlSyncRestore_Object = MibTableColumn
prtPhMlSyncRestore = _PrtPhMlSyncRestore_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 10),
    _PrtPhMlSyncRestore_Type()
)
prtPhMlSyncRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlSyncRestore.setStatus("current")


class _PrtPhMlBus_Type(Integer32):
    """Custom type prtPhMlBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("busA", 2),
          ("busB", 3))
    )


_PrtPhMlBus_Type.__name__ = "Integer32"
_PrtPhMlBus_Object = MibTableColumn
prtPhMlBus = _PrtPhMlBus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 11),
    _PrtPhMlBus_Type()
)
prtPhMlBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlBus.setStatus("current")


class _PrtPhMlMfSyncSlot_Type(Integer32):
    """Custom type prtPhMlMfSyncSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtPhMlMfSyncSlot_Type.__name__ = "Integer32"
_PrtPhMlMfSyncSlot_Object = MibTableColumn
prtPhMlMfSyncSlot = _PrtPhMlMfSyncSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 12),
    _PrtPhMlMfSyncSlot_Type()
)
prtPhMlMfSyncSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlMfSyncSlot.setStatus("current")


class _PrtPhMlClockSource_Type(Integer32):
    """Custom type prtPhMlClockSource based on Integer32"""
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
          ("txClock", 2),
          ("rxClock", 3))
    )


_PrtPhMlClockSource_Type.__name__ = "Integer32"
_PrtPhMlClockSource_Object = MibTableColumn
prtPhMlClockSource = _PrtPhMlClockSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 13),
    _PrtPhMlClockSource_Type()
)
prtPhMlClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlClockSource.setStatus("current")


class _PrtPhMlErrCorrection_Type(Integer32):
    """Custom type prtPhMlErrCorrection based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtPhMlErrCorrection_Type.__name__ = "Integer32"
_PrtPhMlErrCorrection_Object = MibTableColumn
prtPhMlErrCorrection = _PrtPhMlErrCorrection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 14),
    _PrtPhMlErrCorrection_Type()
)
prtPhMlErrCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlErrCorrection.setStatus("current")


class _PrtPhMlCorrectionMode_Type(Integer32):
    """Custom type prtPhMlCorrectionMode based on Integer32"""
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
          ("random", 2),
          ("bursty", 3))
    )


_PrtPhMlCorrectionMode_Type.__name__ = "Integer32"
_PrtPhMlCorrectionMode_Object = MibTableColumn
prtPhMlCorrectionMode = _PrtPhMlCorrectionMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 15),
    _PrtPhMlCorrectionMode_Type()
)
prtPhMlCorrectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlCorrectionMode.setStatus("current")


class _PrtPhMlControlSignals_Type(Integer32):
    """Custom type prtPhMlControlSignals based on Integer32"""
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
          ("ignore", 2),
          ("implement", 3))
    )


_PrtPhMlControlSignals_Type.__name__ = "Integer32"
_PrtPhMlControlSignals_Object = MibTableColumn
prtPhMlControlSignals = _PrtPhMlControlSignals_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 16),
    _PrtPhMlControlSignals_Type()
)
prtPhMlControlSignals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlControlSignals.setStatus("current")


class _PrtPhMlInterfaceType_Type(Integer32):
    """Custom type prtPhMlInterfaceType based on Integer32"""
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
        *(("notApplicable", 1),
          ("v35", 2),
          ("x21", 3),
          ("rs232", 4),
          ("rs449", 5),
          ("ei530", 6),
          ("ei530a", 7))
    )


_PrtPhMlInterfaceType_Type.__name__ = "Integer32"
_PrtPhMlInterfaceType_Object = MibTableColumn
prtPhMlInterfaceType = _PrtPhMlInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 17),
    _PrtPhMlInterfaceType_Type()
)
prtPhMlInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlInterfaceType.setStatus("current")


class _PrtPhMlClockPolarity_Type(Integer32):
    """Custom type prtPhMlClockPolarity based on Integer32"""
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
          ("normal", 2),
          ("inverted", 3))
    )


_PrtPhMlClockPolarity_Type.__name__ = "Integer32"
_PrtPhMlClockPolarity_Object = MibTableColumn
prtPhMlClockPolarity = _PrtPhMlClockPolarity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 2, 5, 1, 18),
    _PrtPhMlClockPolarity_Type()
)
prtPhMlClockPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtPhMlClockPolarity.setStatus("current")
_PrtPhPlCnfg_ObjectIdentity = ObjectIdentity
prtPhPlCnfg = _PrtPhPlCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3)
)
_PrtExPhPlCnfgTable_Object = MibTable
prtExPhPlCnfgTable = _PrtExPhPlCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    prtExPhPlCnfgTable.setStatus("current")
_PrtExPhPlCnfgEntry_Object = MibTableRow
prtExPhPlCnfgEntry = _PrtExPhPlCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1)
)
prtExPhPlCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExPhPlCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPhPlSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPhPlPrtIdx"),
)
if mibBuilder.loadTexts:
    prtExPhPlCnfgEntry.setStatus("current")


class _PrtExPhPlCnfgIdx_Type(Integer32):
    """Custom type prtExPhPlCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExPhPlCnfgIdx_Type.__name__ = "Integer32"
_PrtExPhPlCnfgIdx_Object = MibTableColumn
prtExPhPlCnfgIdx = _PrtExPhPlCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 1),
    _PrtExPhPlCnfgIdx_Type()
)
prtExPhPlCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlCnfgIdx.setStatus("current")


class _PrtExPhPlSltIdx_Type(Integer32):
    """Custom type prtExPhPlSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExPhPlSltIdx_Type.__name__ = "Integer32"
_PrtExPhPlSltIdx_Object = MibTableColumn
prtExPhPlSltIdx = _PrtExPhPlSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 2),
    _PrtExPhPlSltIdx_Type()
)
prtExPhPlSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlSltIdx.setStatus("current")


class _PrtExPhPlPrtIdx_Type(Integer32):
    """Custom type prtExPhPlPrtIdx based on Integer32"""
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
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6))
    )


_PrtExPhPlPrtIdx_Type.__name__ = "Integer32"
_PrtExPhPlPrtIdx_Object = MibTableColumn
prtExPhPlPrtIdx = _PrtExPhPlPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 3),
    _PrtExPhPlPrtIdx_Type()
)
prtExPhPlPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlPrtIdx.setStatus("current")


class _PrtExPhPlConnect_Type(Integer32):
    """Custom type prtExPhPlConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExPhPlConnect_Type.__name__ = "Integer32"
_PrtExPhPlConnect_Object = MibTableColumn
prtExPhPlConnect = _PrtExPhPlConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 4),
    _PrtExPhPlConnect_Type()
)
prtExPhPlConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlConnect.setStatus("current")


class _PrtExPhPlHRate_Type(Integer32):
    """Custom type prtExPhPlHRate based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("r32KbpsNLE", 2),
          ("r48KbpsNLE", 3),
          ("r56KbpsNLE", 4),
          ("r64KbpsNLE", 5),
          ("r112KbpsNLE", 6),
          ("r128KbpsNLE", 7),
          ("r168KbpsNLE", 8),
          ("r192KbpsNLE", 9),
          ("r224KbpsNLE", 10),
          ("r256KbpsNLE", 11),
          ("r280KbpsE", 12),
          ("r320KbpsE", 13),
          ("r336KbpsNLE", 14),
          ("r384KbpsNLE", 15),
          ("r392KbpsE", 16),
          ("r448KbpsNLE", 17),
          ("r504KbpsLE", 18),
          ("r512KbpsE", 19),
          ("r560KbpsE", 20),
          ("r576KbpsLE", 21),
          ("r616KbpsE", 22),
          ("r640KbpsE", 23),
          ("r672KbpsNLE", 24),
          ("r704KbpsE", 25),
          ("r728KbpsE", 26),
          ("r768KbpsNLE", 27),
          ("r784KbpsE", 28),
          ("r832KbpsE", 29),
          ("r840KbpsE", 30),
          ("r896KbpsNLE", 31),
          ("r952KbpsE", 32),
          ("r960KbpsE", 33),
          ("r1008KbpsLE", 34),
          ("r1024KbpsE", 35),
          ("r1064KbpsE", 36),
          ("r1088KbpsE", 37),
          ("r1120KbpsE", 38),
          ("r1152KbpsLE", 39),
          ("r1176KbpsE", 40),
          ("r1216KbpsE", 41),
          ("r1232KbpsE", 42),
          ("r1280KbpsE", 43),
          ("r1288KbpsE", 44),
          ("r1344KbpsNLE", 45),
          ("r1400KbpsE", 46),
          ("r1408KbpsE", 47),
          ("r1456KbpsE", 48),
          ("r1472KbpsE", 49),
          ("r1512KbpsE", 50),
          ("r1536KbpsE", 51),
          ("r1568KbpsE", 52),
          ("r1600KbpsE", 53),
          ("r1624KbpsE", 54),
          ("r1664KbpsE", 55),
          ("r1680KbpsE", 56),
          ("r1728KbpsE", 57),
          ("r1736KbpsE", 58),
          ("r1792KbpsNLE", 59),
          ("r1856KbpsE", 60),
          ("r1920KbpsE", 61),
          ("r1984KbpsE", 62),
          ("r2048KbpsE", 63),
          ("r9d6KbpsNLE", 65),
          ("r14d4KbpsNLE", 66),
          ("r16KbpsNLE", 67),
          ("r19d2KbpsNLE", 68),
          ("r28d8KbpsNLE", 69),
          ("r38d4KbpsNLE", 70),
          ("r57d6KbpsNLE", 71),
          ("r115d2KbpsNLE", 72),
          ("r24000bps", 73))
    )


_PrtExPhPlHRate_Type.__name__ = "Integer32"
_PrtExPhPlHRate_Object = MibTableColumn
prtExPhPlHRate = _PrtExPhPlHRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 5),
    _PrtExPhPlHRate_Type()
)
prtExPhPlHRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlHRate.setStatus("current")


class _PrtExPhPlLRate_Type(Integer32):
    """Custom type prtExPhPlLRate based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("r300bpsNLE", 2),
          ("r600bpsNLE", 3),
          ("r800bpsNLE", 4),
          ("r1200bpsNLE", 5),
          ("r2400bpsNLE", 6),
          ("r4800bpsNLE", 7),
          ("r9600bpsNLE", 8),
          ("r14400bpsLE", 9),
          ("r19200bpsNLE", 10),
          ("r28800bpsLE", 11),
          ("r32000bpsNLE", 12),
          ("r38400bpsNLE", 13),
          ("r48000bpsNLE", 14),
          ("r56000bpsNLE", 15),
          ("r57600bpsLE", 16),
          ("r64000bpsNLE", 17),
          ("r112000bps", 18),
          ("r115200bps", 19),
          ("r16000bpsNLE", 20),
          ("r100bpsNLE", 21),
          ("r128000bps", 22),
          ("r24000bps", 23))
    )


_PrtExPhPlLRate_Type.__name__ = "Integer32"
_PrtExPhPlLRate_Object = MibTableColumn
prtExPhPlLRate = _PrtExPhPlLRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 6),
    _PrtExPhPlLRate_Type()
)
prtExPhPlLRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlLRate.setStatus("current")


class _PrtExPhPlProtocol_Type(Integer32):
    """Custom type prtExPhPlProtocol based on Integer32"""
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("fr", 1),
          ("frPlus", 2),
          ("pCellRelay", 3),
          ("hdlcSdlc", 4),
          ("transparentHdlc", 5),
          ("async", 6),
          ("asyncReliable", 7),
          ("activePPP", 8),
          ("slip", 9),
          ("pppAgent", 10),
          ("slipAgent", 11),
          ("transparent", 12),
          ("sna", 13),
          ("ft1Dot2", 14))
    )


_PrtExPhPlProtocol_Type.__name__ = "Integer32"
_PrtExPhPlProtocol_Object = MibTableColumn
prtExPhPlProtocol = _PrtExPhPlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 7),
    _PrtExPhPlProtocol_Type()
)
prtExPhPlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlProtocol.setStatus("current")


class _PrtExPhPlConnectionTyp_Type(Integer32):
    """Custom type prtExPhPlConnectionTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sameNetManaged", 1),
          ("sameNetNotMana", 2),
          ("user", 3),
          ("otherNet", 4),
          ("pubNet", 5),
          ("notApplicable", 255))
    )


_PrtExPhPlConnectionTyp_Type.__name__ = "Integer32"
_PrtExPhPlConnectionTyp_Object = MibTableColumn
prtExPhPlConnectionTyp = _PrtExPhPlConnectionTyp_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 8),
    _PrtExPhPlConnectionTyp_Type()
)
prtExPhPlConnectionTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlConnectionTyp.setStatus("current")


class _PrtExPhPlClkMode_Type(Integer32):
    """Custom type prtExPhPlClkMode based on Integer32"""
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
        *(("dce", 1),
          ("extDce", 2),
          ("dte", 3),
          ("int", 4),
          ("lbt", 5))
    )


_PrtExPhPlClkMode_Type.__name__ = "Integer32"
_PrtExPhPlClkMode_Object = MibTableColumn
prtExPhPlClkMode = _PrtExPhPlClkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 9),
    _PrtExPhPlClkMode_Type()
)
prtExPhPlClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlClkMode.setStatus("current")


class _PrtExPhPlDceClkSrc_Type(Integer32):
    """Custom type prtExPhPlDceClkSrc based on Integer32"""
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
          ("local", 2),
          ("nodalTiming", 3))
    )


_PrtExPhPlDceClkSrc_Type.__name__ = "Integer32"
_PrtExPhPlDceClkSrc_Object = MibTableColumn
prtExPhPlDceClkSrc = _PrtExPhPlDceClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 10),
    _PrtExPhPlDceClkSrc_Type()
)
prtExPhPlDceClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDceClkSrc.setStatus("current")


class _PrtExPhPlCongResponse_Type(Integer32):
    """Custom type prtExPhPlCongResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("flowControl", 3),
          ("toFlowControl", 4))
    )


_PrtExPhPlCongResponse_Type.__name__ = "Integer32"
_PrtExPhPlCongResponse_Object = MibTableColumn
prtExPhPlCongResponse = _PrtExPhPlCongResponse_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 11),
    _PrtExPhPlCongResponse_Type()
)
prtExPhPlCongResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlCongResponse.setStatus("current")


class _PrtExPhPlCongLevel_Type(Integer32):
    """Custom type prtExPhPlCongLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70),
    )


_PrtExPhPlCongLevel_Type.__name__ = "Integer32"
_PrtExPhPlCongLevel_Object = MibTableColumn
prtExPhPlCongLevel = _PrtExPhPlCongLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 12),
    _PrtExPhPlCongLevel_Type()
)
prtExPhPlCongLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlCongLevel.setStatus("current")


class _PrtExPhPlTc_Type(Integer32):
    """Custom type prtExPhPlTc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tc1sec", 1),
          ("tc2sec", 2),
          ("tc3sec", 3),
          ("tc4sec", 4),
          ("notApplicable", 255))
    )


_PrtExPhPlTc_Type.__name__ = "Integer32"
_PrtExPhPlTc_Object = MibTableColumn
prtExPhPlTc = _PrtExPhPlTc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 13),
    _PrtExPhPlTc_Type()
)
prtExPhPlTc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlTc.setStatus("current")


class _PrtExPhPlFlowControl_Type(Integer32):
    """Custom type prtExPhPlFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("fecnBecn", 3),
          ("xonXoff", 4),
          ("dtrCts", 5),
          ("speedReduction", 6))
    )


_PrtExPhPlFlowControl_Type.__name__ = "Integer32"
_PrtExPhPlFlowControl_Object = MibTableColumn
prtExPhPlFlowControl = _PrtExPhPlFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 14),
    _PrtExPhPlFlowControl_Type()
)
prtExPhPlFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlFlowControl.setStatus("current")


class _PrtExPhPlDcdRts_Type(Integer32):
    """Custom type prtExPhPlDcdRts based on Integer32"""
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
          ("on", 2),
          ("endToEnd", 3))
    )


_PrtExPhPlDcdRts_Type.__name__ = "Integer32"
_PrtExPhPlDcdRts_Object = MibTableColumn
prtExPhPlDcdRts = _PrtExPhPlDcdRts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 15),
    _PrtExPhPlDcdRts_Type()
)
prtExPhPlDcdRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDcdRts.setStatus("current")


class _PrtExPhPlDcdRtsControlPath_Type(Integer32):
    """Custom type prtExPhPlDcdRtsControlPath based on Integer32"""
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
          ("off", 2),
          ("on", 3))
    )


_PrtExPhPlDcdRtsControlPath_Type.__name__ = "Integer32"
_PrtExPhPlDcdRtsControlPath_Object = MibTableColumn
prtExPhPlDcdRtsControlPath = _PrtExPhPlDcdRtsControlPath_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 16),
    _PrtExPhPlDcdRtsControlPath_Type()
)
prtExPhPlDcdRtsControlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDcdRtsControlPath.setStatus("current")


class _PrtExPhPlDataBits_Type(Integer32):
    """Custom type prtExPhPlDataBits based on Integer32"""
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
          ("dataBits7Bits", 2),
          ("dataBits8Bits", 3))
    )


_PrtExPhPlDataBits_Type.__name__ = "Integer32"
_PrtExPhPlDataBits_Object = MibTableColumn
prtExPhPlDataBits = _PrtExPhPlDataBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 17),
    _PrtExPhPlDataBits_Type()
)
prtExPhPlDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDataBits.setStatus("current")


class _PrtExPhPlParity_Type(Integer32):
    """Custom type prtExPhPlParity based on Integer32"""
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
        *(("notApplicable", 1),
          ("odd", 2),
          ("even", 3),
          ("none", 4))
    )


_PrtExPhPlParity_Type.__name__ = "Integer32"
_PrtExPhPlParity_Object = MibTableColumn
prtExPhPlParity = _PrtExPhPlParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 18),
    _PrtExPhPlParity_Type()
)
prtExPhPlParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlParity.setStatus("current")


class _PrtExPhPlStopBits_Type(Integer32):
    """Custom type prtExPhPlStopBits based on Integer32"""
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
        *(("notApplicable", 1),
          ("sb1Bit", 2),
          ("sb1dot5Bits", 3),
          ("sb2Bits", 4))
    )


_PrtExPhPlStopBits_Type.__name__ = "Integer32"
_PrtExPhPlStopBits_Object = MibTableColumn
prtExPhPlStopBits = _PrtExPhPlStopBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 19),
    _PrtExPhPlStopBits_Type()
)
prtExPhPlStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlStopBits.setStatus("current")
_PrtExPhPlLXon_Type = Integer32
_PrtExPhPlLXon_Object = MibTableColumn
prtExPhPlLXon = _PrtExPhPlLXon_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 20),
    _PrtExPhPlLXon_Type()
)
prtExPhPlLXon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlLXon.setStatus("current")
_PrtExPhPlLXoff_Type = Integer32
_PrtExPhPlLXoff_Object = MibTableColumn
prtExPhPlLXoff = _PrtExPhPlLXoff_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 21),
    _PrtExPhPlLXoff_Type()
)
prtExPhPlLXoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlLXoff.setStatus("current")


class _PrtExPhPlFrMngProt_Type(Integer32):
    """Custom type prtExPhPlFrMngProt based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("lmi", 3),
          ("ansiT1", 4),
          ("annexA", 5))
    )


_PrtExPhPlFrMngProt_Type.__name__ = "Integer32"
_PrtExPhPlFrMngProt_Object = MibTableColumn
prtExPhPlFrMngProt = _PrtExPhPlFrMngProt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 22),
    _PrtExPhPlFrMngProt_Type()
)
prtExPhPlFrMngProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlFrMngProt.setStatus("current")


class _PrtExPhPlEnqPeriod_Type(Integer32):
    """Custom type prtExPhPlEnqPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PrtExPhPlEnqPeriod_Type.__name__ = "Integer32"
_PrtExPhPlEnqPeriod_Object = MibTableColumn
prtExPhPlEnqPeriod = _PrtExPhPlEnqPeriod_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 23),
    _PrtExPhPlEnqPeriod_Type()
)
prtExPhPlEnqPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlEnqPeriod.setStatus("current")


class _PrtExPhPlFullRptPeriod_Type(Integer32):
    """Custom type prtExPhPlFullRptPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExPhPlFullRptPeriod_Type.__name__ = "Integer32"
_PrtExPhPlFullRptPeriod_Object = MibTableColumn
prtExPhPlFullRptPeriod = _PrtExPhPlFullRptPeriod_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 24),
    _PrtExPhPlFullRptPeriod_Type()
)
prtExPhPlFullRptPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlFullRptPeriod.setStatus("current")


class _PrtExPhPlFrWindowSize_Type(Integer32):
    """Custom type prtExPhPlFrWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrtExPhPlFrWindowSize_Type.__name__ = "Integer32"
_PrtExPhPlFrWindowSize_Object = MibTableColumn
prtExPhPlFrWindowSize = _PrtExPhPlFrWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 25),
    _PrtExPhPlFrWindowSize_Type()
)
prtExPhPlFrWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlFrWindowSize.setStatus("current")


class _PrtExPhPlErrorsThreshold_Type(Integer32):
    """Custom type prtExPhPlErrorsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrtExPhPlErrorsThreshold_Type.__name__ = "Integer32"
_PrtExPhPlErrorsThreshold_Object = MibTableColumn
prtExPhPlErrorsThreshold = _PrtExPhPlErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 26),
    _PrtExPhPlErrorsThreshold_Type()
)
prtExPhPlErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlErrorsThreshold.setStatus("current")


class _PrtExPhPlPvcCreateMsg_Type(Integer32):
    """Custom type prtExPhPlPvcCreateMsg based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExPhPlPvcCreateMsg_Type.__name__ = "Integer32"
_PrtExPhPlPvcCreateMsg_Object = MibTableColumn
prtExPhPlPvcCreateMsg = _PrtExPhPlPvcCreateMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 27),
    _PrtExPhPlPvcCreateMsg_Type()
)
prtExPhPlPvcCreateMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlPvcCreateMsg.setStatus("current")


class _PrtExPhPlCllmMsg_Type(Integer32):
    """Custom type prtExPhPlCllmMsg based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExPhPlCllmMsg_Type.__name__ = "Integer32"
_PrtExPhPlCllmMsg_Object = MibTableColumn
prtExPhPlCllmMsg = _PrtExPhPlCllmMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 28),
    _PrtExPhPlCllmMsg_Type()
)
prtExPhPlCllmMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlCllmMsg.setStatus("current")


class _PrtExPhPlProtDelayLevel_Type(Integer32):
    """Custom type prtExPhPlProtDelayLevel based on Integer32"""
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
        *(("notApplicable", 1),
          ("s36Byte", 2),
          ("s150Byte", 3),
          ("s264Byte", 4),
          ("s378Byte", 5),
          ("s492Byte", 6))
    )


_PrtExPhPlProtDelayLevel_Type.__name__ = "Integer32"
_PrtExPhPlProtDelayLevel_Object = MibTableColumn
prtExPhPlProtDelayLevel = _PrtExPhPlProtDelayLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 29),
    _PrtExPhPlProtDelayLevel_Type()
)
prtExPhPlProtDelayLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlProtDelayLevel.setStatus("current")


class _PrtExPhPlClockEncoding_Type(Integer32):
    """Custom type prtExPhPlClockEncoding based on Integer32"""
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
          ("nrz", 2),
          ("nrzI", 3),
          ("fm0", 4),
          ("manchester", 5),
          ("diffManchester", 6),
          ("nrzISpace", 7),
          ("nrzIMark", 8))
    )


_PrtExPhPlClockEncoding_Type.__name__ = "Integer32"
_PrtExPhPlClockEncoding_Object = MibTableColumn
prtExPhPlClockEncoding = _PrtExPhPlClockEncoding_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 30),
    _PrtExPhPlClockEncoding_Type()
)
prtExPhPlClockEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlClockEncoding.setStatus("current")


class _PrtExPhPlMinSeparators_Type(Integer32):
    """Custom type prtExPhPlMinSeparators based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_PrtExPhPlMinSeparators_Type.__name__ = "Integer32"
_PrtExPhPlMinSeparators_Object = MibTableColumn
prtExPhPlMinSeparators = _PrtExPhPlMinSeparators_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 31),
    _PrtExPhPlMinSeparators_Type()
)
prtExPhPlMinSeparators.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlMinSeparators.setStatus("current")


class _PrtExPhPlCcittCrc_Type(Integer32):
    """Custom type prtExPhPlCcittCrc based on Integer32"""
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
          ("crc16", 2),
          ("crc32", 3))
    )


_PrtExPhPlCcittCrc_Type.__name__ = "Integer32"
_PrtExPhPlCcittCrc_Object = MibTableColumn
prtExPhPlCcittCrc = _PrtExPhPlCcittCrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 32),
    _PrtExPhPlCcittCrc_Type()
)
prtExPhPlCcittCrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlCcittCrc.setStatus("current")


class _PrtExPhPlFrameSeparator_Type(Integer32):
    """Custom type prtExPhPlFrameSeparator based on Integer32"""
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
          ("idles", 2),
          ("flags", 3))
    )


_PrtExPhPlFrameSeparator_Type.__name__ = "Integer32"
_PrtExPhPlFrameSeparator_Object = MibTableColumn
prtExPhPlFrameSeparator = _PrtExPhPlFrameSeparator_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 33),
    _PrtExPhPlFrameSeparator_Type()
)
prtExPhPlFrameSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlFrameSeparator.setStatus("current")
_PrtExPhPlIdleCode_Type = Integer32
_PrtExPhPlIdleCode_Object = MibTableColumn
prtExPhPlIdleCode = _PrtExPhPlIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 34),
    _PrtExPhPlIdleCode_Type()
)
prtExPhPlIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlIdleCode.setStatus("current")


class _PrtExPhPlJitter_Type(Integer32):
    """Custom type prtExPhPlJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PrtExPhPlJitter_Type.__name__ = "Integer32"
_PrtExPhPlJitter_Object = MibTableColumn
prtExPhPlJitter = _PrtExPhPlJitter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 1, 1, 35),
    _PrtExPhPlJitter_Type()
)
prtExPhPlJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlJitter.setStatus("current")
_PrtExPhPlDlciTable_Object = MibTable
prtExPhPlDlciTable = _PrtExPhPlDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    prtExPhPlDlciTable.setStatus("current")
_PrtExPhPlDlciEntry_Object = MibTableRow
prtExPhPlDlciEntry = _PrtExPhPlDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1)
)
prtExPhPlDlciEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExPhPlDlciCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPhPlDlciSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPhPlDlciPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPhPlDlciIdx"),
)
if mibBuilder.loadTexts:
    prtExPhPlDlciEntry.setStatus("current")


class _PrtExPhPlDlciCnfgIdx_Type(Integer32):
    """Custom type prtExPhPlDlciCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExPhPlDlciCnfgIdx_Type.__name__ = "Integer32"
_PrtExPhPlDlciCnfgIdx_Object = MibTableColumn
prtExPhPlDlciCnfgIdx = _PrtExPhPlDlciCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 1),
    _PrtExPhPlDlciCnfgIdx_Type()
)
prtExPhPlDlciCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlDlciCnfgIdx.setStatus("current")


class _PrtExPhPlDlciSltIdx_Type(Integer32):
    """Custom type prtExPhPlDlciSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExPhPlDlciSltIdx_Type.__name__ = "Integer32"
_PrtExPhPlDlciSltIdx_Object = MibTableColumn
prtExPhPlDlciSltIdx = _PrtExPhPlDlciSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 2),
    _PrtExPhPlDlciSltIdx_Type()
)
prtExPhPlDlciSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlDlciSltIdx.setStatus("current")


class _PrtExPhPlDlciPrtIdx_Type(Integer32):
    """Custom type prtExPhPlDlciPrtIdx based on Integer32"""
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
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6))
    )


_PrtExPhPlDlciPrtIdx_Type.__name__ = "Integer32"
_PrtExPhPlDlciPrtIdx_Object = MibTableColumn
prtExPhPlDlciPrtIdx = _PrtExPhPlDlciPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 3),
    _PrtExPhPlDlciPrtIdx_Type()
)
prtExPhPlDlciPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlDlciPrtIdx.setStatus("current")


class _PrtExPhPlDlciIdx_Type(Integer32):
    """Custom type prtExPhPlDlciIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 991),
    )


_PrtExPhPlDlciIdx_Type.__name__ = "Integer32"
_PrtExPhPlDlciIdx_Object = MibTableColumn
prtExPhPlDlciIdx = _PrtExPhPlDlciIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 4),
    _PrtExPhPlDlciIdx_Type()
)
prtExPhPlDlciIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlDlciIdx.setStatus("current")


class _PrtExPhPlDlciValid_Type(Integer32):
    """Custom type prtExPhPlDlciValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExPhPlDlciValid_Type.__name__ = "Integer32"
_PrtExPhPlDlciValid_Object = MibTableColumn
prtExPhPlDlciValid = _PrtExPhPlDlciValid_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 5),
    _PrtExPhPlDlciValid_Type()
)
prtExPhPlDlciValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDlciValid.setStatus("current")


class _PrtExPhPlDlciIConSlt_Type(Integer32):
    """Custom type prtExPhPlDlciIConSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("cl", 3),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExPhPlDlciIConSlt_Type.__name__ = "Integer32"
_PrtExPhPlDlciIConSlt_Object = MibTableColumn
prtExPhPlDlciIConSlt = _PrtExPhPlDlciIConSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 6),
    _PrtExPhPlDlciIConSlt_Type()
)
prtExPhPlDlciIConSlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDlciIConSlt.setStatus("current")


class _PrtExPhPlDlciIConPrt_Type(Integer32):
    """Custom type prtExPhPlDlciIConPrt based on Integer32"""
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
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("clNMS", 99),
          ("noConnect", 100),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108),
          ("inPrt9", 109),
          ("inPrt10", 110))
    )


_PrtExPhPlDlciIConPrt_Type.__name__ = "Integer32"
_PrtExPhPlDlciIConPrt_Object = MibTableColumn
prtExPhPlDlciIConPrt = _PrtExPhPlDlciIConPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 7),
    _PrtExPhPlDlciIConPrt_Type()
)
prtExPhPlDlciIConPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDlciIConPrt.setStatus("current")


class _PrtExPhPlDlciIConDlci_Type(Integer32):
    """Custom type prtExPhPlDlciIConDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 991),
    )


_PrtExPhPlDlciIConDlci_Type.__name__ = "Integer32"
_PrtExPhPlDlciIConDlci_Object = MibTableColumn
prtExPhPlDlciIConDlci = _PrtExPhPlDlciIConDlci_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 8),
    _PrtExPhPlDlciIConDlci_Type()
)
prtExPhPlDlciIConDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDlciIConDlci.setStatus("current")


class _PrtExPhPlDlciTxBc_Type(Integer32):
    """Custom type prtExPhPlDlciTxBc based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("txBc9600bps", 3),
          ("txBc14400bps", 4),
          ("txBc19200bps", 5),
          ("txBc28800bps", 6),
          ("txBc32000bps", 7),
          ("txBc38400bps", 8),
          ("txBc48000bps", 9),
          ("txBc56000bps", 10),
          ("txBc57600bps", 11),
          ("txBc64Kbps", 12),
          ("txBc128Kbps", 13),
          ("txBc192Kbps", 14),
          ("txBc256Kbps", 15),
          ("txBc320Kbps", 16),
          ("txBc384Kbps", 17),
          ("txBc448Kbps", 18),
          ("txBc512Kbps", 19),
          ("txBc768Kbps", 20),
          ("txBc1024Kbps", 21),
          ("txBc16000bps", 25),
          ("txBc112Kbps", 26))
    )


_PrtExPhPlDlciTxBc_Type.__name__ = "Integer32"
_PrtExPhPlDlciTxBc_Object = MibTableColumn
prtExPhPlDlciTxBc = _PrtExPhPlDlciTxBc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 9),
    _PrtExPhPlDlciTxBc_Type()
)
prtExPhPlDlciTxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDlciTxBc.setStatus("current")


class _PrtExPhPlDlciTxBe_Type(Integer32):
    """Custom type prtExPhPlDlciTxBe based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("txBe9600bps", 3),
          ("txBe14400bps", 4),
          ("txBe19200bps", 5),
          ("txBe28800bps", 6),
          ("txBe32000bps", 7),
          ("txBe38400bps", 8),
          ("txBe48000bps", 9),
          ("txBe56000bps", 10),
          ("txBe57600bps", 11),
          ("txBe64Kbps", 12),
          ("txBe128Kbps", 13),
          ("txBe192Kbps", 14),
          ("txBe256Kbps", 15),
          ("txBe320Kbps", 16),
          ("txBe384Kbps", 17),
          ("txBe448Kbps", 18),
          ("txBe512Kbps", 19),
          ("txBe768Kbps", 20),
          ("txBe1024Kbps", 21),
          ("txBc16000bps", 25),
          ("txBc112Kbps", 26))
    )


_PrtExPhPlDlciTxBe_Type.__name__ = "Integer32"
_PrtExPhPlDlciTxBe_Object = MibTableColumn
prtExPhPlDlciTxBe = _PrtExPhPlDlciTxBe_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 10),
    _PrtExPhPlDlciTxBe_Type()
)
prtExPhPlDlciTxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDlciTxBe.setStatus("current")


class _PrtExPhPlDlciRxBc_Type(Integer32):
    """Custom type prtExPhPlDlciRxBc based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("rxBc9600bps", 3),
          ("rxBc14400bps", 4),
          ("rxBc19200bps", 5),
          ("rxBc28800bps", 6),
          ("rxBc32000bps", 7),
          ("rxBc38400bps", 8),
          ("rxBc48000bps", 9),
          ("rxBc56000bps", 10),
          ("rxBc57600bps", 11),
          ("rxBc64Kbps", 12),
          ("rxBc128Kbps", 13),
          ("rxBc192Kbps", 14),
          ("rxBc256Kbps", 15),
          ("rxBc320Kbps", 16),
          ("rxBc384Kbps", 17),
          ("rxBc448Kbps", 18),
          ("rxBc512Kbps", 19),
          ("rxBc768Kbps", 20),
          ("rxBc1024Kbps", 21),
          ("rxBc16000bps", 25),
          ("rxBc112Kbps", 26))
    )


_PrtExPhPlDlciRxBc_Type.__name__ = "Integer32"
_PrtExPhPlDlciRxBc_Object = MibTableColumn
prtExPhPlDlciRxBc = _PrtExPhPlDlciRxBc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 11),
    _PrtExPhPlDlciRxBc_Type()
)
prtExPhPlDlciRxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDlciRxBc.setStatus("current")


class _PrtExPhPlDlciRxBe_Type(Integer32):
    """Custom type prtExPhPlDlciRxBe based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("rxBe9600bps", 3),
          ("rxBe14400bps", 4),
          ("rxBe19200bps", 5),
          ("rxBe28800bps", 6),
          ("rxBe32000bps", 7),
          ("rxBe38400bps", 8),
          ("rxBe48000bps", 9),
          ("rxBe56000bps", 10),
          ("rxBe57600bps", 11),
          ("rxBe64Kbps", 12),
          ("rxBe128Kbps", 13),
          ("rxBe192Kbps", 14),
          ("rxBe256Kbps", 15),
          ("rxBe320Kbps", 16),
          ("rxBe384Kbps", 17),
          ("rxBe448Kbps", 18),
          ("rxBe512Kbps", 19),
          ("rxBe768Kbps", 20),
          ("rxBe1024Kbps", 21),
          ("rxBc16000bps", 25),
          ("rxBc112Kbps", 26))
    )


_PrtExPhPlDlciRxBe_Type.__name__ = "Integer32"
_PrtExPhPlDlciRxBe_Object = MibTableColumn
prtExPhPlDlciRxBe = _PrtExPhPlDlciRxBe_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 12),
    _PrtExPhPlDlciRxBe_Type()
)
prtExPhPlDlciRxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDlciRxBe.setStatus("current")


class _PrtExPhPlDlciPriority_Type(Integer32):
    """Custom type prtExPhPlDlciPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PrtExPhPlDlciPriority_Type.__name__ = "Integer32"
_PrtExPhPlDlciPriority_Object = MibTableColumn
prtExPhPlDlciPriority = _PrtExPhPlDlciPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 13),
    _PrtExPhPlDlciPriority_Type()
)
prtExPhPlDlciPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlDlciPriority.setStatus("current")


class _PrtExPhPlDlciStatus_Type(Integer32):
    """Custom type prtExPhPlDlciStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2))
    )


_PrtExPhPlDlciStatus_Type.__name__ = "Integer32"
_PrtExPhPlDlciStatus_Object = MibTableColumn
prtExPhPlDlciStatus = _PrtExPhPlDlciStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 2, 1, 14),
    _PrtExPhPlDlciStatus_Type()
)
prtExPhPlDlciStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlDlciStatus.setStatus("current")
_PrtExPhPlModemTable_Object = MibTable
prtExPhPlModemTable = _PrtExPhPlModemTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    prtExPhPlModemTable.setStatus("current")
_PrtExPhPlModemEntry_Object = MibTableRow
prtExPhPlModemEntry = _PrtExPhPlModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3, 1)
)
prtExPhPlModemEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExPhPlModemCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPhPlModemSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPhPlModemPrtIdx"),
)
if mibBuilder.loadTexts:
    prtExPhPlModemEntry.setStatus("current")


class _PrtExPhPlModemCnfgIdx_Type(Integer32):
    """Custom type prtExPhPlModemCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExPhPlModemCnfgIdx_Type.__name__ = "Integer32"
_PrtExPhPlModemCnfgIdx_Object = MibTableColumn
prtExPhPlModemCnfgIdx = _PrtExPhPlModemCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3, 1, 1),
    _PrtExPhPlModemCnfgIdx_Type()
)
prtExPhPlModemCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlModemCnfgIdx.setStatus("current")


class _PrtExPhPlModemSltIdx_Type(Integer32):
    """Custom type prtExPhPlModemSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExPhPlModemSltIdx_Type.__name__ = "Integer32"
_PrtExPhPlModemSltIdx_Object = MibTableColumn
prtExPhPlModemSltIdx = _PrtExPhPlModemSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3, 1, 2),
    _PrtExPhPlModemSltIdx_Type()
)
prtExPhPlModemSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlModemSltIdx.setStatus("current")


class _PrtExPhPlModemPrtIdx_Type(Integer32):
    """Custom type prtExPhPlModemPrtIdx based on Integer32"""
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
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6))
    )


_PrtExPhPlModemPrtIdx_Type.__name__ = "Integer32"
_PrtExPhPlModemPrtIdx_Object = MibTableColumn
prtExPhPlModemPrtIdx = _PrtExPhPlModemPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3, 1, 3),
    _PrtExPhPlModemPrtIdx_Type()
)
prtExPhPlModemPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPhPlModemPrtIdx.setStatus("current")


class _PrtExPhPlModemStatus_Type(Integer32):
    """Custom type prtExPhPlModemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("relay", 4))
    )


_PrtExPhPlModemStatus_Type.__name__ = "Integer32"
_PrtExPhPlModemStatus_Object = MibTableColumn
prtExPhPlModemStatus = _PrtExPhPlModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3, 1, 4),
    _PrtExPhPlModemStatus_Type()
)
prtExPhPlModemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlModemStatus.setStatus("current")


class _PrtExPhPlModemActivate_Type(Integer32):
    """Custom type prtExPhPlModemActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("onFirstFrame", 2),
          ("always", 3),
          ("notApplicable", 255))
    )


_PrtExPhPlModemActivate_Type.__name__ = "Integer32"
_PrtExPhPlModemActivate_Object = MibTableColumn
prtExPhPlModemActivate = _PrtExPhPlModemActivate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3, 1, 5),
    _PrtExPhPlModemActivate_Type()
)
prtExPhPlModemActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlModemActivate.setStatus("current")
_PrtExPhPlModemMaxIdleTime_Type = Integer32
_PrtExPhPlModemMaxIdleTime_Object = MibTableColumn
prtExPhPlModemMaxIdleTime = _PrtExPhPlModemMaxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3, 1, 6),
    _PrtExPhPlModemMaxIdleTime_Type()
)
prtExPhPlModemMaxIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlModemMaxIdleTime.setStatus("current")
_PrtExPhPlModemTimeBtwnCalls_Type = Integer32
_PrtExPhPlModemTimeBtwnCalls_Object = MibTableColumn
prtExPhPlModemTimeBtwnCalls = _PrtExPhPlModemTimeBtwnCalls_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3, 1, 7),
    _PrtExPhPlModemTimeBtwnCalls_Type()
)
prtExPhPlModemTimeBtwnCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlModemTimeBtwnCalls.setStatus("current")
_PrtExPhPlModemCallDelay_Type = Integer32
_PrtExPhPlModemCallDelay_Object = MibTableColumn
prtExPhPlModemCallDelay = _PrtExPhPlModemCallDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 3, 3, 1, 8),
    _PrtExPhPlModemCallDelay_Type()
)
prtExPhPlModemCallDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPhPlModemCallDelay.setStatus("current")
_PrtLs2Cnfg_ObjectIdentity = ObjectIdentity
prtLs2Cnfg = _PrtLs2Cnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4)
)
_PrtExLs2CnfgTable_Object = MibTable
prtExLs2CnfgTable = _PrtExLs2CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    prtExLs2CnfgTable.setStatus("current")
_PrtExLs2CnfgEntry_Object = MibTableRow
prtExLs2CnfgEntry = _PrtExLs2CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1)
)
prtExLs2CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExLs2CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExLs2SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExLs2PrtIdx"),
)
if mibBuilder.loadTexts:
    prtExLs2CnfgEntry.setStatus("current")


class _PrtExLs2CnfgIdx_Type(Integer32):
    """Custom type prtExLs2CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExLs2CnfgIdx_Type.__name__ = "Integer32"
_PrtExLs2CnfgIdx_Object = MibTableColumn
prtExLs2CnfgIdx = _PrtExLs2CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1, 1),
    _PrtExLs2CnfgIdx_Type()
)
prtExLs2CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExLs2CnfgIdx.setStatus("current")


class _PrtExLs2SltIdx_Type(Integer32):
    """Custom type prtExLs2SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExLs2SltIdx_Type.__name__ = "Integer32"
_PrtExLs2SltIdx_Object = MibTableColumn
prtExLs2SltIdx = _PrtExLs2SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1, 2),
    _PrtExLs2SltIdx_Type()
)
prtExLs2SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExLs2SltIdx.setStatus("current")


class _PrtExLs2PrtIdx_Type(Integer32):
    """Custom type prtExLs2PrtIdx based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10))
    )


_PrtExLs2PrtIdx_Type.__name__ = "Integer32"
_PrtExLs2PrtIdx_Object = MibTableColumn
prtExLs2PrtIdx = _PrtExLs2PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1, 3),
    _PrtExLs2PrtIdx_Type()
)
prtExLs2PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExLs2PrtIdx.setStatus("current")


class _PrtExLs2Connect_Type(Integer32):
    """Custom type prtExLs2Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExLs2Connect_Type.__name__ = "Integer32"
_PrtExLs2Connect_Object = MibTableColumn
prtExLs2Connect = _PrtExLs2Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1, 4),
    _PrtExLs2Connect_Type()
)
prtExLs2Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs2Connect.setStatus("current")


class _PrtExLs2Rate_Type(Integer32):
    """Custom type prtExLs2Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("r2400bps", 2),
          ("r4800bps", 3),
          ("r9600bps", 4),
          ("r19200bps", 5))
    )


_PrtExLs2Rate_Type.__name__ = "Integer32"
_PrtExLs2Rate_Object = MibTableColumn
prtExLs2Rate = _PrtExLs2Rate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1, 5),
    _PrtExLs2Rate_Type()
)
prtExLs2Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs2Rate.setStatus("current")


class _PrtExLs2ClkMode_Type(Integer32):
    """Custom type prtExLs2ClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("ext-dce", 2),
          ("dte", 3))
    )


_PrtExLs2ClkMode_Type.__name__ = "Integer32"
_PrtExLs2ClkMode_Object = MibTableColumn
prtExLs2ClkMode = _PrtExLs2ClkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1, 6),
    _PrtExLs2ClkMode_Type()
)
prtExLs2ClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs2ClkMode.setStatus("current")


class _PrtExLs2Cts_Type(Integer32):
    """Custom type prtExLs2Cts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("rts-min", 3),
          ("rts-max", 4))
    )


_PrtExLs2Cts_Type.__name__ = "Integer32"
_PrtExLs2Cts_Object = MibTableColumn
prtExLs2Cts = _PrtExLs2Cts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1, 7),
    _PrtExLs2Cts_Type()
)
prtExLs2Cts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs2Cts.setStatus("current")


class _PrtExLs2Dcd_Type(Integer32):
    """Custom type prtExLs2Dcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("card-sync", 3))
    )


_PrtExLs2Dcd_Type.__name__ = "Integer32"
_PrtExLs2Dcd_Object = MibTableColumn
prtExLs2Dcd = _PrtExLs2Dcd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1, 8),
    _PrtExLs2Dcd_Type()
)
prtExLs2Dcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs2Dcd.setStatus("current")


class _PrtExLs2EnvIdx_Type(Integer32):
    """Custom type prtExLs2EnvIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PrtExLs2EnvIdx_Type.__name__ = "Integer32"
_PrtExLs2EnvIdx_Object = MibTableColumn
prtExLs2EnvIdx = _PrtExLs2EnvIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 1, 1, 9),
    _PrtExLs2EnvIdx_Type()
)
prtExLs2EnvIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs2EnvIdx.setStatus("current")
_PrtInLs2CnfgTable_Object = MibTable
prtInLs2CnfgTable = _PrtInLs2CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    prtInLs2CnfgTable.setStatus("current")
_PrtInLs2CnfgEntry_Object = MibTableRow
prtInLs2CnfgEntry = _PrtInLs2CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2, 1)
)
prtInLs2CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtInLs2CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtInLs2SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtInLs2PrtIdx"),
)
if mibBuilder.loadTexts:
    prtInLs2CnfgEntry.setStatus("current")


class _PrtInLs2CnfgIdx_Type(Integer32):
    """Custom type prtInLs2CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtInLs2CnfgIdx_Type.__name__ = "Integer32"
_PrtInLs2CnfgIdx_Object = MibTableColumn
prtInLs2CnfgIdx = _PrtInLs2CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2, 1, 1),
    _PrtInLs2CnfgIdx_Type()
)
prtInLs2CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInLs2CnfgIdx.setStatus("current")


class _PrtInLs2SltIdx_Type(Integer32):
    """Custom type prtInLs2SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInLs2SltIdx_Type.__name__ = "Integer32"
_PrtInLs2SltIdx_Object = MibTableColumn
prtInLs2SltIdx = _PrtInLs2SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2, 1, 2),
    _PrtInLs2SltIdx_Type()
)
prtInLs2SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInLs2SltIdx.setStatus("current")


class _PrtInLs2PrtIdx_Type(Integer32):
    """Custom type prtInLs2PrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("inPrt1", 101),
          ("inPrt2", 102))
    )


_PrtInLs2PrtIdx_Type.__name__ = "Integer32"
_PrtInLs2PrtIdx_Object = MibTableColumn
prtInLs2PrtIdx = _PrtInLs2PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2, 1, 3),
    _PrtInLs2PrtIdx_Type()
)
prtInLs2PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInLs2PrtIdx.setStatus("current")


class _PrtInLs2Connect_Type(Integer32):
    """Custom type prtInLs2Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtInLs2Connect_Type.__name__ = "Integer32"
_PrtInLs2Connect_Object = MibTableColumn
prtInLs2Connect = _PrtInLs2Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2, 1, 4),
    _PrtInLs2Connect_Type()
)
prtInLs2Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs2Connect.setStatus("current")


class _PrtInLs2Group_Type(Integer32):
    """Custom type prtInLs2Group based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_PrtInLs2Group_Type.__name__ = "Integer32"
_PrtInLs2Group_Object = MibTableColumn
prtInLs2Group = _PrtInLs2Group_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2, 1, 5),
    _PrtInLs2Group_Type()
)
prtInLs2Group.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs2Group.setStatus("current")


class _PrtInLs2Member_Type(Integer32):
    """Custom type prtInLs2Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PrtInLs2Member_Type.__name__ = "Integer32"
_PrtInLs2Member_Object = MibTableColumn
prtInLs2Member = _PrtInLs2Member_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2, 1, 6),
    _PrtInLs2Member_Type()
)
prtInLs2Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs2Member.setStatus("current")


class _PrtInLs2LinkTo_Type(Integer32):
    """Custom type prtInLs2LinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInLs2LinkTo_Type.__name__ = "Integer32"
_PrtInLs2LinkTo_Object = MibTableColumn
prtInLs2LinkTo = _PrtInLs2LinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2, 1, 7),
    _PrtInLs2LinkTo_Type()
)
prtInLs2LinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs2LinkTo.setStatus("deprecated")


class _PrtInLs2EnvAssign_Type(Integer32):
    """Custom type prtInLs2EnvAssign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 3))
    )


_PrtInLs2EnvAssign_Type.__name__ = "Integer32"
_PrtInLs2EnvAssign_Object = MibTableColumn
prtInLs2EnvAssign = _PrtInLs2EnvAssign_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 4, 2, 1, 8),
    _PrtInLs2EnvAssign_Type()
)
prtInLs2EnvAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs2EnvAssign.setStatus("current")
_PrtVc2CnfgTable_Object = MibTable
prtVc2CnfgTable = _PrtVc2CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5)
)
if mibBuilder.loadTexts:
    prtVc2CnfgTable.setStatus("current")
_PrtVc2CnfgEntry_Object = MibTableRow
prtVc2CnfgEntry = _PrtVc2CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1)
)
prtVc2CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtVc2CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtVc2SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtVc2PrtIdx"),
)
if mibBuilder.loadTexts:
    prtVc2CnfgEntry.setStatus("current")


class _PrtVc2CnfgIdx_Type(Integer32):
    """Custom type prtVc2CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtVc2CnfgIdx_Type.__name__ = "Integer32"
_PrtVc2CnfgIdx_Object = MibTableColumn
prtVc2CnfgIdx = _PrtVc2CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 1),
    _PrtVc2CnfgIdx_Type()
)
prtVc2CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtVc2CnfgIdx.setStatus("current")


class _PrtVc2SltIdx_Type(Integer32):
    """Custom type prtVc2SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtVc2SltIdx_Type.__name__ = "Integer32"
_PrtVc2SltIdx_Object = MibTableColumn
prtVc2SltIdx = _PrtVc2SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 2),
    _PrtVc2SltIdx_Type()
)
prtVc2SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtVc2SltIdx.setStatus("current")
_PrtVc2PrtIdx_Type = Integer32
_PrtVc2PrtIdx_Object = MibTableColumn
prtVc2PrtIdx = _PrtVc2PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 3),
    _PrtVc2PrtIdx_Type()
)
prtVc2PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtVc2PrtIdx.setStatus("current")


class _PrtExVc2Connect_Type(Integer32):
    """Custom type prtExVc2Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3),
          ("v51", 4),
          ("v52", 5))
    )


_PrtExVc2Connect_Type.__name__ = "Integer32"
_PrtExVc2Connect_Object = MibTableColumn
prtExVc2Connect = _PrtExVc2Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 4),
    _PrtExVc2Connect_Type()
)
prtExVc2Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2Connect.setStatus("current")
_PrtExVc2TransGain_Type = Integer32
_PrtExVc2TransGain_Object = MibTableColumn
prtExVc2TransGain = _PrtExVc2TransGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 5),
    _PrtExVc2TransGain_Type()
)
prtExVc2TransGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2TransGain.setStatus("current")
_PrtExVc2ReceiveGain_Type = Integer32
_PrtExVc2ReceiveGain_Object = MibTableColumn
prtExVc2ReceiveGain = _PrtExVc2ReceiveGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 6),
    _PrtExVc2ReceiveGain_Type()
)
prtExVc2ReceiveGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2ReceiveGain.setStatus("current")


class _PrtExVc2Wire_Type(Integer32):
    """Custom type prtExVc2Wire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("w2wire", 1),
          ("w4wire", 2),
          ("notApplicable", 255))
    )


_PrtExVc2Wire_Type.__name__ = "Integer32"
_PrtExVc2Wire_Object = MibTableColumn
prtExVc2Wire = _PrtExVc2Wire_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 7),
    _PrtExVc2Wire_Type()
)
prtExVc2Wire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2Wire.setStatus("current")


class _PrtExVc2CodingLaw_Type(Integer32):
    """Custom type prtExVc2CodingLaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLAW", 1),
          ("uLAW", 2))
    )


_PrtExVc2CodingLaw_Type.__name__ = "Integer32"
_PrtExVc2CodingLaw_Object = MibTableColumn
prtExVc2CodingLaw = _PrtExVc2CodingLaw_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 8),
    _PrtExVc2CodingLaw_Type()
)
prtExVc2CodingLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2CodingLaw.setStatus("current")


class _PrtExVc2Sig_Type(Integer32):
    """Custom type prtExVc2Sig based on Integer32"""
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
        *(("noSignaling", 1),
          ("robbedBitMultiFrame", 2),
          ("chAssociatedE1", 3),
          ("robbedBitFrame", 4))
    )


_PrtExVc2Sig_Type.__name__ = "Integer32"
_PrtExVc2Sig_Object = MibTableColumn
prtExVc2Sig = _PrtExVc2Sig_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 9),
    _PrtExVc2Sig_Type()
)
prtExVc2Sig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2Sig.setStatus("current")


class _PrtExVc2Oos_Type(Integer32):
    """Custom type prtExVc2Oos based on Integer32"""
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
        *(("forcedIdle", 1),
          ("forcedBusy", 2),
          ("busyIdle", 3),
          ("idleBusy", 4),
          ("notApplicable", 5))
    )


_PrtExVc2Oos_Type.__name__ = "Integer32"
_PrtExVc2Oos_Object = MibTableColumn
prtExVc2Oos = _PrtExVc2Oos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 10),
    _PrtExVc2Oos_Type()
)
prtExVc2Oos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2Oos.setStatus("current")


class _PrtExVc2LinkTo_Type(Integer32):
    """Custom type prtExVc2LinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExVc2LinkTo_Type.__name__ = "Integer32"
_PrtExVc2LinkTo_Object = MibTableColumn
prtExVc2LinkTo = _PrtExVc2LinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 11),
    _PrtExVc2LinkTo_Type()
)
prtExVc2LinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2LinkTo.setStatus("deprecated")


class _PrtExVc2OperMode_Type(Integer32):
    """Custom type prtExVc2OperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("unidirectRx", 3),
          ("broadcast", 4))
    )


_PrtExVc2OperMode_Type.__name__ = "Integer32"
_PrtExVc2OperMode_Object = MibTableColumn
prtExVc2OperMode = _PrtExVc2OperMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 12),
    _PrtExVc2OperMode_Type()
)
prtExVc2OperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2OperMode.setStatus("current")


class _PrtExVc2SigProfile_Type(Integer32):
    """Custom type prtExVc2SigProfile based on Integer32"""
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
          ("manual", 2),
          ("p1", 3),
          ("p2", 4),
          ("p3Fxo3S3", 5),
          ("reversePolarity", 6),
          ("meteringPulse", 7),
          ("p4", 8))
    )


_PrtExVc2SigProfile_Type.__name__ = "Integer32"
_PrtExVc2SigProfile_Object = MibTableColumn
prtExVc2SigProfile = _PrtExVc2SigProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 13),
    _PrtExVc2SigProfile_Type()
)
prtExVc2SigProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2SigProfile.setStatus("current")


class _PrtExVc2CallEnable_Type(Integer32):
    """Custom type prtExVc2CallEnable based on Integer32"""
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
        *(("notApplicable", 1),
          ("incoming", 2),
          ("outgoing", 3),
          ("both", 4))
    )


_PrtExVc2CallEnable_Type.__name__ = "Integer32"
_PrtExVc2CallEnable_Object = MibTableColumn
prtExVc2CallEnable = _PrtExVc2CallEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 14),
    _PrtExVc2CallEnable_Type()
)
prtExVc2CallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2CallEnable.setStatus("current")


class _PrtExVc2R2Delay_Type(Integer32):
    """Custom type prtExVc2R2Delay based on Integer32"""
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
          ("terrestrial", 2),
          ("satellite", 3))
    )


_PrtExVc2R2Delay_Type.__name__ = "Integer32"
_PrtExVc2R2Delay_Object = MibTableColumn
prtExVc2R2Delay = _PrtExVc2R2Delay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 15),
    _PrtExVc2R2Delay_Type()
)
prtExVc2R2Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2R2Delay.setStatus("current")


class _PrtExVc2CasStd_Type(Integer32):
    """Custom type prtExVc2CasStd based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("r2Q422", 2),
          ("specialA", 3),
          ("specialB", 4),
          ("specialC", 5),
          ("specialD", 6),
          ("specialE", 7),
          ("specialF", 8),
          ("specialG", 9))
    )


_PrtExVc2CasStd_Type.__name__ = "Integer32"
_PrtExVc2CasStd_Object = MibTableColumn
prtExVc2CasStd = _PrtExVc2CasStd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 16),
    _PrtExVc2CasStd_Type()
)
prtExVc2CasStd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2CasStd.setStatus("current")


class _PrtExVc2EchoCanceler_Type(Integer32):
    """Custom type prtExVc2EchoCanceler based on Integer32"""
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
          ("off", 2),
          ("on", 3))
    )


_PrtExVc2EchoCanceler_Type.__name__ = "Integer32"
_PrtExVc2EchoCanceler_Object = MibTableColumn
prtExVc2EchoCanceler = _PrtExVc2EchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 17),
    _PrtExVc2EchoCanceler_Type()
)
prtExVc2EchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2EchoCanceler.setStatus("current")


class _PrtExVc2IfType_Type(Integer32):
    """Custom type prtExVc2IfType based on Integer32"""
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
        *(("notApplicable", 1),
          ("w2Em", 2),
          ("w4Em", 3),
          ("fxo", 4),
          ("fxs", 5))
    )


_PrtExVc2IfType_Type.__name__ = "Integer32"
_PrtExVc2IfType_Object = MibTableColumn
prtExVc2IfType = _PrtExVc2IfType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 18),
    _PrtExVc2IfType_Type()
)
prtExVc2IfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2IfType.setStatus("current")


class _PrtExVc2Encoding_Type(Integer32):
    """Custom type prtExVc2Encoding based on Integer32"""
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
        *(("notApplicable", 1),
          ("pcm", 2),
          ("adpcm", 3),
          ("linear", 4))
    )


_PrtExVc2Encoding_Type.__name__ = "Integer32"
_PrtExVc2Encoding_Object = MibTableColumn
prtExVc2Encoding = _PrtExVc2Encoding_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 19),
    _PrtExVc2Encoding_Type()
)
prtExVc2Encoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2Encoding.setStatus("current")
_PrtExVc2TxBitCode_Type = OctetString
_PrtExVc2TxBitCode_Object = MibTableColumn
prtExVc2TxBitCode = _PrtExVc2TxBitCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 20),
    _PrtExVc2TxBitCode_Type()
)
prtExVc2TxBitCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2TxBitCode.setStatus("current")
_PrtExVc2RxBitOutput_Type = OctetString
_PrtExVc2RxBitOutput_Object = MibTableColumn
prtExVc2RxBitOutput = _PrtExVc2RxBitOutput_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 21),
    _PrtExVc2RxBitOutput_Type()
)
prtExVc2RxBitOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2RxBitOutput.setStatus("current")


class _PrtExVc2MeterRate_Type(Integer32):
    """Custom type prtExVc2MeterRate based on Integer32"""
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
        *(("notApplicable", 1),
          ("r16Khz", 2),
          ("r12Khz", 3),
          ("disabled", 4))
    )


_PrtExVc2MeterRate_Type.__name__ = "Integer32"
_PrtExVc2MeterRate_Object = MibTableColumn
prtExVc2MeterRate = _PrtExVc2MeterRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 22),
    _PrtExVc2MeterRate_Type()
)
prtExVc2MeterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2MeterRate.setStatus("current")


class _PrtExVc2IfSignaling_Type(Integer32):
    """Custom type prtExVc2IfSignaling based on Integer32"""
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
        *(("notApplicable", 1),
          ("loopStart", 2),
          ("groundStart", 3),
          ("winkStart", 4))
    )


_PrtExVc2IfSignaling_Type.__name__ = "Integer32"
_PrtExVc2IfSignaling_Object = MibTableColumn
prtExVc2IfSignaling = _PrtExVc2IfSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 23),
    _PrtExVc2IfSignaling_Type()
)
prtExVc2IfSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2IfSignaling.setStatus("current")


class _PrtExVc2SeizeAck_Type(Integer32):
    """Custom type prtExVc2SeizeAck based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExVc2SeizeAck_Type.__name__ = "Integer32"
_PrtExVc2SeizeAck_Object = MibTableColumn
prtExVc2SeizeAck = _PrtExVc2SeizeAck_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 24),
    _PrtExVc2SeizeAck_Type()
)
prtExVc2SeizeAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2SeizeAck.setStatus("current")


class _PrtExVc2EandMType_Type(Integer32):
    """Custom type prtExVc2EandMType based on Integer32"""
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
        *(("notApplicable", 1),
          ("type1", 2),
          ("type2", 3),
          ("type3", 4),
          ("type5", 5))
    )


_PrtExVc2EandMType_Type.__name__ = "Integer32"
_PrtExVc2EandMType_Object = MibTableColumn
prtExVc2EandMType = _PrtExVc2EandMType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 25),
    _PrtExVc2EandMType_Type()
)
prtExVc2EandMType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2EandMType.setStatus("current")


class _PrtExVc2RemType_Type(Integer32):
    """Custom type prtExVc2RemType based on Integer32"""
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
        *(("notApplicable", 1),
          ("lb", 2),
          ("pbx", 3),
          ("e1", 4),
          ("t1", 5),
          ("t1D4", 6))
    )


_PrtExVc2RemType_Type.__name__ = "Integer32"
_PrtExVc2RemType_Object = MibTableColumn
prtExVc2RemType = _PrtExVc2RemType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 26),
    _PrtExVc2RemType_Type()
)
prtExVc2RemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2RemType.setStatus("current")


class _PrtExVc2ConvTime_Type(Integer32):
    """Custom type prtExVc2ConvTime based on Integer32"""
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
        *(("notApplicable", 1),
          ("m2", 2),
          ("m3", 3),
          ("m5", 4),
          ("unlimited", 5))
    )


_PrtExVc2ConvTime_Type.__name__ = "Integer32"
_PrtExVc2ConvTime_Object = MibTableColumn
prtExVc2ConvTime = _PrtExVc2ConvTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 27),
    _PrtExVc2ConvTime_Type()
)
prtExVc2ConvTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2ConvTime.setStatus("current")


class _PrtExVc2SigFeedback_Type(Integer32):
    """Custom type prtExVc2SigFeedback based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExVc2SigFeedback_Type.__name__ = "Integer32"
_PrtExVc2SigFeedback_Object = MibTableColumn
prtExVc2SigFeedback = _PrtExVc2SigFeedback_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 28),
    _PrtExVc2SigFeedback_Type()
)
prtExVc2SigFeedback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2SigFeedback.setStatus("current")


class _PrtExVc2EchoCancelerModule_Type(Integer32):
    """Custom type prtExVc2EchoCancelerModule based on Integer32"""
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
          ("notExist", 2),
          ("exist", 3))
    )


_PrtExVc2EchoCancelerModule_Type.__name__ = "Integer32"
_PrtExVc2EchoCancelerModule_Object = MibTableColumn
prtExVc2EchoCancelerModule = _PrtExVc2EchoCancelerModule_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 29),
    _PrtExVc2EchoCancelerModule_Type()
)
prtExVc2EchoCancelerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVc2EchoCancelerModule.setStatus("current")


class _PrtExVc2ReversePolarity_Type(Integer32):
    """Custom type prtExVc2ReversePolarity based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 3))
    )


_PrtExVc2ReversePolarity_Type.__name__ = "Integer32"
_PrtExVc2ReversePolarity_Object = MibTableColumn
prtExVc2ReversePolarity = _PrtExVc2ReversePolarity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 30),
    _PrtExVc2ReversePolarity_Type()
)
prtExVc2ReversePolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2ReversePolarity.setStatus("current")


class _PrtExVc2RingerFrequency_Type(Integer32):
    """Custom type prtExVc2RingerFrequency based on Integer32"""
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
        *(("notApplicable", 1),
          ("f20Hz", 2),
          ("f25Hz", 3),
          ("f50Hz", 4))
    )


_PrtExVc2RingerFrequency_Type.__name__ = "Integer32"
_PrtExVc2RingerFrequency_Object = MibTableColumn
prtExVc2RingerFrequency = _PrtExVc2RingerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 31),
    _PrtExVc2RingerFrequency_Type()
)
prtExVc2RingerFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2RingerFrequency.setStatus("current")


class _PrtExVc2SigService_Type(Integer32):
    """Custom type prtExVc2SigService based on Integer32"""
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
          ("normal", 2),
          ("advanced", 3))
    )


_PrtExVc2SigService_Type.__name__ = "Integer32"
_PrtExVc2SigService_Object = MibTableColumn
prtExVc2SigService = _PrtExVc2SigService_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 32),
    _PrtExVc2SigService_Type()
)
prtExVc2SigService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2SigService.setStatus("current")


class _PrtExVc2CallerIdEnable_Type(Integer32):
    """Custom type prtExVc2CallerIdEnable based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 3))
    )


_PrtExVc2CallerIdEnable_Type.__name__ = "Integer32"
_PrtExVc2CallerIdEnable_Object = MibTableColumn
prtExVc2CallerIdEnable = _PrtExVc2CallerIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 33),
    _PrtExVc2CallerIdEnable_Type()
)
prtExVc2CallerIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2CallerIdEnable.setStatus("current")


class _PrtExVc2CompressMethod_Type(Integer32):
    """Custom type prtExVc2CompressMethod based on Integer32"""
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
          ("g726", 2),
          ("g727", 3))
    )


_PrtExVc2CompressMethod_Type.__name__ = "Integer32"
_PrtExVc2CompressMethod_Object = MibTableColumn
prtExVc2CompressMethod = _PrtExVc2CompressMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 34),
    _PrtExVc2CompressMethod_Type()
)
prtExVc2CompressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2CompressMethod.setStatus("current")


class _PrtExVc2ObMode_Type(Integer32):
    """Custom type prtExVc2ObMode based on Integer32"""
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
        *(("pointToPoint", 1),
          ("omniBus", 2),
          ("pointToMultiPointSrc", 3),
          ("pointToMultiPointDst", 4))
    )


_PrtExVc2ObMode_Type.__name__ = "Integer32"
_PrtExVc2ObMode_Object = MibTableColumn
prtExVc2ObMode = _PrtExVc2ObMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 35),
    _PrtExVc2ObMode_Type()
)
prtExVc2ObMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2ObMode.setStatus("current")


class _PrtExVc2VAD_Type(Integer32):
    """Custom type prtExVc2VAD based on Integer32"""
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
          ("off", 2),
          ("on", 3))
    )


_PrtExVc2VAD_Type.__name__ = "Integer32"
_PrtExVc2VAD_Object = MibTableColumn
prtExVc2VAD = _PrtExVc2VAD_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 36),
    _PrtExVc2VAD_Type()
)
prtExVc2VAD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2VAD.setStatus("current")


class _PrtExVc2NoiseLevelForVAD_Type(Integer32):
    """Custom type prtExVc2NoiseLevelForVAD based on Integer32"""
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
        *(("notApplicable", 1),
          ("low", 2),
          ("medium", 3),
          ("high", 4))
    )


_PrtExVc2NoiseLevelForVAD_Type.__name__ = "Integer32"
_PrtExVc2NoiseLevelForVAD_Object = MibTableColumn
prtExVc2NoiseLevelForVAD = _PrtExVc2NoiseLevelForVAD_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 37),
    _PrtExVc2NoiseLevelForVAD_Type()
)
prtExVc2NoiseLevelForVAD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2NoiseLevelForVAD.setStatus("current")


class _PrtExVc2WesternSigMode_Type(Integer32):
    """Custom type prtExVc2WesternSigMode based on Integer32"""
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
          ("detector", 2),
          ("generator", 3))
    )


_PrtExVc2WesternSigMode_Type.__name__ = "Integer32"
_PrtExVc2WesternSigMode_Object = MibTableColumn
prtExVc2WesternSigMode = _PrtExVc2WesternSigMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 38),
    _PrtExVc2WesternSigMode_Type()
)
prtExVc2WesternSigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2WesternSigMode.setStatus("current")


class _PrtExVc2BusProtectionPoint_Type(Integer32):
    """Custom type prtExVc2BusProtectionPoint based on Integer32"""
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
        *(("notApplicable", 1),
          ("no", 2),
          ("first", 3),
          ("last", 4))
    )


_PrtExVc2BusProtectionPoint_Type.__name__ = "Integer32"
_PrtExVc2BusProtectionPoint_Object = MibTableColumn
prtExVc2BusProtectionPoint = _PrtExVc2BusProtectionPoint_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 39),
    _PrtExVc2BusProtectionPoint_Type()
)
prtExVc2BusProtectionPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2BusProtectionPoint.setStatus("current")


class _PrtExVc2ImpedanceStandard_Type(Integer32):
    """Custom type prtExVc2ImpedanceStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g712", 1),
          ("q552ETSI", 2),
          ("q522Italy", 3))
    )


_PrtExVc2ImpedanceStandard_Type.__name__ = "Integer32"
_PrtExVc2ImpedanceStandard_Object = MibTableColumn
prtExVc2ImpedanceStandard = _PrtExVc2ImpedanceStandard_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 5, 1, 40),
    _PrtExVc2ImpedanceStandard_Type()
)
prtExVc2ImpedanceStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc2ImpedanceStandard.setStatus("current")
_PrtHsfCnfgTable_Object = MibTable
prtHsfCnfgTable = _PrtHsfCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6)
)
if mibBuilder.loadTexts:
    prtHsfCnfgTable.setStatus("current")
_PrtHsfCnfgEntry_Object = MibTableRow
prtHsfCnfgEntry = _PrtHsfCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1)
)
prtHsfCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtHsfCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtHsfSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtHsfPrtIdx"),
)
if mibBuilder.loadTexts:
    prtHsfCnfgEntry.setStatus("current")


class _PrtHsfCnfgIdx_Type(Integer32):
    """Custom type prtHsfCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtHsfCnfgIdx_Type.__name__ = "Integer32"
_PrtHsfCnfgIdx_Object = MibTableColumn
prtHsfCnfgIdx = _PrtHsfCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 1),
    _PrtHsfCnfgIdx_Type()
)
prtHsfCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHsfCnfgIdx.setStatus("current")


class _PrtHsfSltIdx_Type(Integer32):
    """Custom type prtHsfSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtHsfSltIdx_Type.__name__ = "Integer32"
_PrtHsfSltIdx_Object = MibTableColumn
prtHsfSltIdx = _PrtHsfSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 2),
    _PrtHsfSltIdx_Type()
)
prtHsfSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHsfSltIdx.setStatus("current")


class _PrtHsfPrtIdx_Type(Integer32):
    """Custom type prtHsfPrtIdx based on Integer32"""
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
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("exPrt11", 11),
          ("exPrt12", 12),
          ("inPrt1", 101),
          ("inPrt2", 102))
    )


_PrtHsfPrtIdx_Type.__name__ = "Integer32"
_PrtHsfPrtIdx_Object = MibTableColumn
prtHsfPrtIdx = _PrtHsfPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 3),
    _PrtHsfPrtIdx_Type()
)
prtHsfPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtHsfPrtIdx.setStatus("current")


class _PrtExHsfConnect_Type(Integer32):
    """Custom type prtExHsfConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExHsfConnect_Type.__name__ = "Integer32"
_PrtExHsfConnect_Object = MibTableColumn
prtExHsfConnect = _PrtExHsfConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 4),
    _PrtExHsfConnect_Type()
)
prtExHsfConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfConnect.setStatus("current")


class _PrtExHsfRate_Type(Integer32):
    """Custom type prtExHsfRate based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("r1x56eq56Kbps", 1),
          ("r1x64eq64Kbps", 2),
          ("r2x56eq112Kbps", 3),
          ("r2x64eq128Kbps", 4),
          ("r3x56eq168Kbps", 5),
          ("r3x64eq192Kbps", 6),
          ("r4x56eq224Kbps", 7),
          ("r4x64eq256Kbps", 8),
          ("r5x56eq280Kbps", 9),
          ("r5x64eq320Kbps", 10),
          ("r6x56eq336Kbps", 11),
          ("r6x64eq384Kbps", 12),
          ("r7x56eq392Kbps", 13),
          ("r7x64eq448Kbps", 14),
          ("r8x56eq448Kbps", 15),
          ("r8x64eq512Kbps", 16),
          ("r9x56eq504Kbps", 17),
          ("r9x64eq576Kbps", 18),
          ("r10x56eq560Kbps", 19),
          ("r10x64eq640Kbps", 20),
          ("r11x56eq616Kbps", 21),
          ("r11x64eq704Kbps", 22),
          ("r12x56eq672Kbps", 23),
          ("r12x64eq768Kbps", 24),
          ("r13x56eq728Kbps", 25),
          ("r13x64eq832Kbps", 26),
          ("r14x56eq784Kbps", 27),
          ("r14x64eq896Kbps", 28),
          ("r15x56eq840Kbps", 29),
          ("r15x64eq960Kbps", 30),
          ("r16x56eq896Kbps", 31),
          ("r16x64eq1024Kbps", 32),
          ("r17x56eq952Kbps", 33),
          ("r17x64eq1088Kbps", 34),
          ("r18x56eq1008Kbps", 35),
          ("r18x64eq1152Kbps", 36),
          ("r19x56eq1064Kbps", 37),
          ("r19x64eq1216Kbps", 38),
          ("r20x56eq1120Kbps", 39),
          ("r20x64eq1280Kbps", 40),
          ("r21x56eq1176Kbps", 41),
          ("r21x64eq1344Kbps", 42),
          ("r22x56eq1232Kbps", 43),
          ("r22x64eq1408Kbps", 44),
          ("r23x56eq1288Kbps", 45),
          ("r23x64eq1472Kbps", 46),
          ("r24x56eq1344Kbps", 47),
          ("r24x64eq1536Kbps", 48),
          ("r25x56eq1400Kbps", 49),
          ("r25x64eq1600Kbps", 50),
          ("r26x56eq1456Kbps", 51),
          ("r26x64eq1664Kbps", 52),
          ("r27x56eq1512Kbps", 53),
          ("r27x64eq1728Kbps", 54),
          ("r28x56eq1568Kbps", 55),
          ("r28x64eq1792Kbps", 56),
          ("r29x56eq1624Kbps", 57),
          ("r29x64eq1856Kbps", 58),
          ("r30x56eq1680Kbps", 59),
          ("r30x64eq1920Kbps", 60),
          ("r31x56eq1736Kbps", 61),
          ("r31x64eq1984Kbps", 62),
          ("r32Kbps", 63))
    )


_PrtExHsfRate_Type.__name__ = "Integer32"
_PrtExHsfRate_Object = MibTableColumn
prtExHsfRate = _PrtExHsfRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 5),
    _PrtExHsfRate_Type()
)
prtExHsfRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfRate.setStatus("current")


class _PrtExHsfClkMode_Type(Integer32):
    """Custom type prtExHsfClkMode based on Integer32"""
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
        *(("dce", 1),
          ("ext-dce", 2),
          ("dte", 3),
          ("none", 4))
    )


_PrtExHsfClkMode_Type.__name__ = "Integer32"
_PrtExHsfClkMode_Object = MibTableColumn
prtExHsfClkMode = _PrtExHsfClkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 6),
    _PrtExHsfClkMode_Type()
)
prtExHsfClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfClkMode.setStatus("current")


class _PrtExHsfCts_Type(Integer32):
    """Custom type prtExHsfCts based on Integer32"""
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
          ("on", 2),
          ("rts", 3))
    )


_PrtExHsfCts_Type.__name__ = "Integer32"
_PrtExHsfCts_Object = MibTableColumn
prtExHsfCts = _PrtExHsfCts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 7),
    _PrtExHsfCts_Type()
)
prtExHsfCts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfCts.setStatus("current")


class _PrtExHsfFifoSize_Type(Integer32):
    """Custom type prtExHsfFifoSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("s16bits", 3),
          ("s30bits", 4),
          ("s52bits", 5),
          ("s72bits", 6))
    )


_PrtExHsfFifoSize_Type.__name__ = "Integer32"
_PrtExHsfFifoSize_Object = MibTableColumn
prtExHsfFifoSize = _PrtExHsfFifoSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 8),
    _PrtExHsfFifoSize_Type()
)
prtExHsfFifoSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfFifoSize.setStatus("current")


class _PrtExHsfLinkTo_Type(Integer32):
    """Custom type prtExHsfLinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExHsfLinkTo_Type.__name__ = "Integer32"
_PrtExHsfLinkTo_Object = MibTableColumn
prtExHsfLinkTo = _PrtExHsfLinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 9),
    _PrtExHsfLinkTo_Type()
)
prtExHsfLinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfLinkTo.setStatus("deprecated")


class _PrtExHsfOperMode_Type(Integer32):
    """Custom type prtExHsfOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("unidirectRx", 3),
          ("broadcast", 4),
          ("bidirBcastRing", 5))
    )


_PrtExHsfOperMode_Type.__name__ = "Integer32"
_PrtExHsfOperMode_Object = MibTableColumn
prtExHsfOperMode = _PrtExHsfOperMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 10),
    _PrtExHsfOperMode_Type()
)
prtExHsfOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfOperMode.setStatus("current")


class _PrtExHsfInbandLoopback_Type(Integer32):
    """Custom type prtExHsfInbandLoopback based on Integer32"""
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
          ("disabled", 2),
          ("ft1Enabled", 3))
    )


_PrtExHsfInbandLoopback_Type.__name__ = "Integer32"
_PrtExHsfInbandLoopback_Object = MibTableColumn
prtExHsfInbandLoopback = _PrtExHsfInbandLoopback_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 11),
    _PrtExHsfInbandLoopback_Type()
)
prtExHsfInbandLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfInbandLoopback.setStatus("current")


class _PrtExHsfClkPolarity_Type(Integer32):
    """Custom type prtExHsfClkPolarity based on Integer32"""
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
          ("normal", 2),
          ("invert", 3))
    )


_PrtExHsfClkPolarity_Type.__name__ = "Integer32"
_PrtExHsfClkPolarity_Object = MibTableColumn
prtExHsfClkPolarity = _PrtExHsfClkPolarity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 12),
    _PrtExHsfClkPolarity_Type()
)
prtExHsfClkPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfClkPolarity.setStatus("current")


class _PrtExHsfControlSignal_Type(Integer32):
    """Custom type prtExHsfControlSignal based on Integer32"""
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
          ("local", 2),
          ("endToEnd", 3))
    )


_PrtExHsfControlSignal_Type.__name__ = "Integer32"
_PrtExHsfControlSignal_Object = MibTableColumn
prtExHsfControlSignal = _PrtExHsfControlSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 13),
    _PrtExHsfControlSignal_Type()
)
prtExHsfControlSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfControlSignal.setStatus("current")


class _PrtExHsfBcastRingSrcPort_Type(Integer32):
    """Custom type prtExHsfBcastRingSrcPort based on Integer32"""
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
              100,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("exPrt11", 11),
          ("exPrt12", 12),
          ("none", 100),
          ("notApplicable", 255))
    )


_PrtExHsfBcastRingSrcPort_Type.__name__ = "Integer32"
_PrtExHsfBcastRingSrcPort_Object = MibTableColumn
prtExHsfBcastRingSrcPort = _PrtExHsfBcastRingSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 6, 1, 14),
    _PrtExHsfBcastRingSrcPort_Type()
)
prtExHsfBcastRingSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsfBcastRingSrcPort.setStatus("current")
_PrtHs4Cnfg_ObjectIdentity = ObjectIdentity
prtHs4Cnfg = _PrtHs4Cnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7)
)
_PrtExHs4CnfgTable_Object = MibTable
prtExHs4CnfgTable = _PrtExHs4CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    prtExHs4CnfgTable.setStatus("current")
_PrtExHs4CnfgEntry_Object = MibTableRow
prtExHs4CnfgEntry = _PrtExHs4CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1)
)
prtExHs4CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExHs4CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExHs4SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExHs4PrtIdx"),
)
if mibBuilder.loadTexts:
    prtExHs4CnfgEntry.setStatus("current")


class _PrtExHs4CnfgIdx_Type(Integer32):
    """Custom type prtExHs4CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExHs4CnfgIdx_Type.__name__ = "Integer32"
_PrtExHs4CnfgIdx_Object = MibTableColumn
prtExHs4CnfgIdx = _PrtExHs4CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 1),
    _PrtExHs4CnfgIdx_Type()
)
prtExHs4CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHs4CnfgIdx.setStatus("current")


class _PrtExHs4SltIdx_Type(Integer32):
    """Custom type prtExHs4SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExHs4SltIdx_Type.__name__ = "Integer32"
_PrtExHs4SltIdx_Object = MibTableColumn
prtExHs4SltIdx = _PrtExHs4SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 2),
    _PrtExHs4SltIdx_Type()
)
prtExHs4SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHs4SltIdx.setStatus("current")


class _PrtExHs4PrtIdx_Type(Integer32):
    """Custom type prtExHs4PrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exPrt1", 1)
    )


_PrtExHs4PrtIdx_Type.__name__ = "Integer32"
_PrtExHs4PrtIdx_Object = MibTableColumn
prtExHs4PrtIdx = _PrtExHs4PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 3),
    _PrtExHs4PrtIdx_Type()
)
prtExHs4PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHs4PrtIdx.setStatus("current")


class _PrtExHs4Connect_Type(Integer32):
    """Custom type prtExHs4Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExHs4Connect_Type.__name__ = "Integer32"
_PrtExHs4Connect_Object = MibTableColumn
prtExHs4Connect = _PrtExHs4Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 4),
    _PrtExHs4Connect_Type()
)
prtExHs4Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4Connect.setStatus("current")


class _PrtExHs4LineType_Type(Integer32):
    """Custom type prtExHs4LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("esfT1", 2),
          ("sfT1", 3),
          ("g732nE1", 4),
          ("g732nE1CRC", 5),
          ("g732sE1", 6),
          ("g732sE1CRC", 7))
    )


_PrtExHs4LineType_Type.__name__ = "Integer32"
_PrtExHs4LineType_Object = MibTableColumn
prtExHs4LineType = _PrtExHs4LineType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 5),
    _PrtExHs4LineType_Type()
)
prtExHs4LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4LineType.setStatus("current")


class _PrtExHs4LineCode_Type(Integer32):
    """Custom type prtExHs4LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("b7T1", 1),
          ("b8zsT1", 2),
          ("hdb3E1", 4))
    )


_PrtExHs4LineCode_Type.__name__ = "Integer32"
_PrtExHs4LineCode_Object = MibTableColumn
prtExHs4LineCode = _PrtExHs4LineCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 6),
    _PrtExHs4LineCode_Type()
)
prtExHs4LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4LineCode.setStatus("current")


class _PrtExHs4LineLen_Type(Integer32):
    """Custom type prtExHs4LineLen based on Integer32"""
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
        *(("unknown", 1),
          ("len0p133ft", 2),
          ("len134p266ft", 3),
          ("len267p399ft", 4),
          ("len400p533ft", 5),
          ("len534p655ft", 6),
          ("fcc68", 7))
    )


_PrtExHs4LineLen_Type.__name__ = "Integer32"
_PrtExHs4LineLen_Object = MibTableColumn
prtExHs4LineLen = _PrtExHs4LineLen_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 7),
    _PrtExHs4LineLen_Type()
)
prtExHs4LineLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4LineLen.setStatus("current")


class _PrtExHs4RestoreT_Type(Integer32):
    """Custom type prtExHs4RestoreT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("restoreT1secFast", 2),
          ("restoreT10sec62411", 3),
          ("ccittE1", 4))
    )


_PrtExHs4RestoreT_Type.__name__ = "Integer32"
_PrtExHs4RestoreT_Object = MibTableColumn
prtExHs4RestoreT = _PrtExHs4RestoreT_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 8),
    _PrtExHs4RestoreT_Type()
)
prtExHs4RestoreT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4RestoreT.setStatus("current")


class _PrtExHs4OosSig_Type(Integer32):
    """Custom type prtExHs4OosSig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 2),
          ("forcedIdle", 3),
          ("forcedBusy", 4),
          ("busyIdle", 5),
          ("idleBusy", 6))
    )


_PrtExHs4OosSig_Type.__name__ = "Integer32"
_PrtExHs4OosSig_Object = MibTableColumn
prtExHs4OosSig = _PrtExHs4OosSig_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 9),
    _PrtExHs4OosSig_Type()
)
prtExHs4OosSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4OosSig.setStatus("current")


class _PrtExHs4OosCode_Type(Integer32):
    """Custom type prtExHs4OosCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 2),
          ("oosCode00H", 3),
          ("oosCode1aH", 4),
          ("oosCode54H", 5),
          ("oosCode7eH", 6),
          ("oosCode7fH", 7),
          ("oosCode98H", 8),
          ("oosCode9eH", 9),
          ("oosCoded5H", 10),
          ("oosCodee4H", 11),
          ("oosCodeffH", 12))
    )


_PrtExHs4OosCode_Type.__name__ = "Integer32"
_PrtExHs4OosCode_Object = MibTableColumn
prtExHs4OosCode = _PrtExHs4OosCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 10),
    _PrtExHs4OosCode_Type()
)
prtExHs4OosCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4OosCode.setStatus("current")
_PrtExHs4IdleCode_Type = Integer32
_PrtExHs4IdleCode_Object = MibTableColumn
prtExHs4IdleCode = _PrtExHs4IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 11),
    _PrtExHs4IdleCode_Type()
)
prtExHs4IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4IdleCode.setStatus("current")


class _PrtExHs4MfClkSrcSlt_Type(Integer32):
    """Custom type prtExHs4MfClkSrcSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExHs4MfClkSrcSlt_Type.__name__ = "Integer32"
_PrtExHs4MfClkSrcSlt_Object = MibTableColumn
prtExHs4MfClkSrcSlt = _PrtExHs4MfClkSrcSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 12),
    _PrtExHs4MfClkSrcSlt_Type()
)
prtExHs4MfClkSrcSlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4MfClkSrcSlt.setStatus("current")


class _PrtExHs4MfClkSrcPrt_Type(Integer32):
    """Custom type prtExHs4MfClkSrcPrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              101)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("inPrt1", 101))
    )


_PrtExHs4MfClkSrcPrt_Type.__name__ = "Integer32"
_PrtExHs4MfClkSrcPrt_Object = MibTableColumn
prtExHs4MfClkSrcPrt = _PrtExHs4MfClkSrcPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 1, 1, 13),
    _PrtExHs4MfClkSrcPrt_Type()
)
prtExHs4MfClkSrcPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4MfClkSrcPrt.setStatus("current")
_PrtExHs4TsCnfgTable_Object = MibTable
prtExHs4TsCnfgTable = _PrtExHs4TsCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    prtExHs4TsCnfgTable.setStatus("current")
_PrtExHs4TsEntry_Object = MibTableRow
prtExHs4TsEntry = _PrtExHs4TsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 2, 1)
)
prtExHs4TsEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExHs4TsCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExHs4TsSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExHs4TsPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtExHs4TsIdx"),
)
if mibBuilder.loadTexts:
    prtExHs4TsEntry.setStatus("current")


class _PrtExHs4TsCnfgIdx_Type(Integer32):
    """Custom type prtExHs4TsCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExHs4TsCnfgIdx_Type.__name__ = "Integer32"
_PrtExHs4TsCnfgIdx_Object = MibTableColumn
prtExHs4TsCnfgIdx = _PrtExHs4TsCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 2, 1, 1),
    _PrtExHs4TsCnfgIdx_Type()
)
prtExHs4TsCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHs4TsCnfgIdx.setStatus("current")


class _PrtExHs4TsSltIdx_Type(Integer32):
    """Custom type prtExHs4TsSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExHs4TsSltIdx_Type.__name__ = "Integer32"
_PrtExHs4TsSltIdx_Object = MibTableColumn
prtExHs4TsSltIdx = _PrtExHs4TsSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 2, 1, 2),
    _PrtExHs4TsSltIdx_Type()
)
prtExHs4TsSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHs4TsSltIdx.setStatus("current")


class _PrtExHs4TsPrtIdx_Type(Integer32):
    """Custom type prtExHs4TsPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exPrt1", 1)
    )


_PrtExHs4TsPrtIdx_Type.__name__ = "Integer32"
_PrtExHs4TsPrtIdx_Object = MibTableColumn
prtExHs4TsPrtIdx = _PrtExHs4TsPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 2, 1, 3),
    _PrtExHs4TsPrtIdx_Type()
)
prtExHs4TsPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHs4TsPrtIdx.setStatus("current")
_PrtExHs4TsIdx_Type = Integer32
_PrtExHs4TsIdx_Object = MibTableColumn
prtExHs4TsIdx = _PrtExHs4TsIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 2, 1, 4),
    _PrtExHs4TsIdx_Type()
)
prtExHs4TsIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHs4TsIdx.setStatus("current")


class _PrtExHs4TsIConSlot_Type(Integer32):
    """Custom type prtExHs4TsIConSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              100)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("split", 100))
    )


_PrtExHs4TsIConSlot_Type.__name__ = "Integer32"
_PrtExHs4TsIConSlot_Object = MibTableColumn
prtExHs4TsIConSlot = _PrtExHs4TsIConSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 2, 1, 5),
    _PrtExHs4TsIConSlot_Type()
)
prtExHs4TsIConSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4TsIConSlot.setStatus("current")


class _PrtExHs4TsIConPrt_Type(Integer32):
    """Custom type prtExHs4TsIConPrt based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("exPrt11", 11),
          ("exPrt12", 12),
          ("noConnect", 100))
    )


_PrtExHs4TsIConPrt_Type.__name__ = "Integer32"
_PrtExHs4TsIConPrt_Object = MibTableColumn
prtExHs4TsIConPrt = _PrtExHs4TsIConPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 2, 1, 6),
    _PrtExHs4TsIConPrt_Type()
)
prtExHs4TsIConPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4TsIConPrt.setStatus("current")
_PrtExHs4TsIConTs_Type = Integer32
_PrtExHs4TsIConTs_Object = MibTableColumn
prtExHs4TsIConTs = _PrtExHs4TsIConTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 7, 2, 1, 7),
    _PrtExHs4TsIConTs_Type()
)
prtExHs4TsIConTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHs4TsIConTs.setStatus("current")
_PrtHsiCnfg_ObjectIdentity = ObjectIdentity
prtHsiCnfg = _PrtHsiCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8)
)
_PrtExHsiCnfgTable_Object = MibTable
prtExHsiCnfgTable = _PrtExHsiCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1)
)
if mibBuilder.loadTexts:
    prtExHsiCnfgTable.setStatus("current")
_PrtExHsiCnfgEntry_Object = MibTableRow
prtExHsiCnfgEntry = _PrtExHsiCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1, 1)
)
prtExHsiCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExHsiCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExHsiSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExHsiPrtIdx"),
)
if mibBuilder.loadTexts:
    prtExHsiCnfgEntry.setStatus("current")


class _PrtExHsiCnfgIdx_Type(Integer32):
    """Custom type prtExHsiCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExHsiCnfgIdx_Type.__name__ = "Integer32"
_PrtExHsiCnfgIdx_Object = MibTableColumn
prtExHsiCnfgIdx = _PrtExHsiCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1, 1, 1),
    _PrtExHsiCnfgIdx_Type()
)
prtExHsiCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHsiCnfgIdx.setStatus("current")


class _PrtExHsiSltIdx_Type(Integer32):
    """Custom type prtExHsiSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("notApplicable", 255))
    )


_PrtExHsiSltIdx_Type.__name__ = "Integer32"
_PrtExHsiSltIdx_Object = MibTableColumn
prtExHsiSltIdx = _PrtExHsiSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1, 1, 2),
    _PrtExHsiSltIdx_Type()
)
prtExHsiSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHsiSltIdx.setStatus("current")
_PrtExHsiPrtIdx_Type = Integer32
_PrtExHsiPrtIdx_Object = MibTableColumn
prtExHsiPrtIdx = _PrtExHsiPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1, 1, 3),
    _PrtExHsiPrtIdx_Type()
)
prtExHsiPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHsiPrtIdx.setStatus("current")


class _PrtExHsiConnect_Type(Integer32):
    """Custom type prtExHsiConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3),
          ("v51", 4),
          ("v52", 5))
    )


_PrtExHsiConnect_Type.__name__ = "Integer32"
_PrtExHsiConnect_Object = MibTableColumn
prtExHsiConnect = _PrtExHsiConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1, 1, 4),
    _PrtExHsiConnect_Type()
)
prtExHsiConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsiConnect.setStatus("current")


class _PrtExHsiRate_Type(Integer32):
    """Custom type prtExHsiRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("r600bps", 2),
          ("r1200bps", 3),
          ("r2400bps", 4),
          ("r4800bps", 5),
          ("r9600bps", 6),
          ("r19200bps", 7),
          ("r38400bps", 8),
          ("r48kbps", 9),
          ("r56kbps", 10),
          ("r64kbps", 11),
          ("r128kbps", 12),
          ("notApplicable", 255))
    )


_PrtExHsiRate_Type.__name__ = "Integer32"
_PrtExHsiRate_Object = MibTableColumn
prtExHsiRate = _PrtExHsiRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1, 1, 5),
    _PrtExHsiRate_Type()
)
prtExHsiRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsiRate.setStatus("current")


class _PrtExHsiLinkTo_Type(Integer32):
    """Custom type prtExHsiLinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExHsiLinkTo_Type.__name__ = "Integer32"
_PrtExHsiLinkTo_Object = MibTableColumn
prtExHsiLinkTo = _PrtExHsiLinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1, 1, 6),
    _PrtExHsiLinkTo_Type()
)
prtExHsiLinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsiLinkTo.setStatus("deprecated")


class _PrtExHsiInterface_Type(Integer32):
    """Custom type prtExHsiInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("lt", 1),
          ("nt", 2),
          ("te", 3),
          ("lt1", 4),
          ("notApplicable", 255))
    )


_PrtExHsiInterface_Type.__name__ = "Integer32"
_PrtExHsiInterface_Object = MibTableColumn
prtExHsiInterface = _PrtExHsiInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1, 1, 7),
    _PrtExHsiInterface_Type()
)
prtExHsiInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsiInterface.setStatus("current")


class _PrtExHsiActType_Type(Integer32):
    """Custom type prtExHsiActType based on Integer32"""
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
        *(("notApplicable", 1),
          ("type1", 2),
          ("type2", 3),
          ("type3", 4))
    )


_PrtExHsiActType_Type.__name__ = "Integer32"
_PrtExHsiActType_Object = MibTableColumn
prtExHsiActType = _PrtExHsiActType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 1, 1, 8),
    _PrtExHsiActType_Type()
)
prtExHsiActType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsiActType.setStatus("current")
_PrtInHsiCnfgTable_Object = MibTable
prtInHsiCnfgTable = _PrtInHsiCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 2)
)
if mibBuilder.loadTexts:
    prtInHsiCnfgTable.setStatus("current")
_PrtInHsiCnfgEntry_Object = MibTableRow
prtInHsiCnfgEntry = _PrtInHsiCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 2, 1)
)
prtInHsiCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtInHsiCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtInHsiSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtInHsiPrtIdx"),
)
if mibBuilder.loadTexts:
    prtInHsiCnfgEntry.setStatus("current")


class _PrtInHsiCnfgIdx_Type(Integer32):
    """Custom type prtInHsiCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtInHsiCnfgIdx_Type.__name__ = "Integer32"
_PrtInHsiCnfgIdx_Object = MibTableColumn
prtInHsiCnfgIdx = _PrtInHsiCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 2, 1, 1),
    _PrtInHsiCnfgIdx_Type()
)
prtInHsiCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInHsiCnfgIdx.setStatus("current")


class _PrtInHsiSltIdx_Type(Integer32):
    """Custom type prtInHsiSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19),
          ("notApplicable", 255))
    )


_PrtInHsiSltIdx_Type.__name__ = "Integer32"
_PrtInHsiSltIdx_Object = MibTableColumn
prtInHsiSltIdx = _PrtInHsiSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 2, 1, 2),
    _PrtInHsiSltIdx_Type()
)
prtInHsiSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInHsiSltIdx.setStatus("current")
_PrtInHsiPrtIdx_Type = Integer32
_PrtInHsiPrtIdx_Object = MibTableColumn
prtInHsiPrtIdx = _PrtInHsiPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 2, 1, 3),
    _PrtInHsiPrtIdx_Type()
)
prtInHsiPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInHsiPrtIdx.setStatus("current")


class _PrtInHsiConnect_Type(Integer32):
    """Custom type prtInHsiConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtInHsiConnect_Type.__name__ = "Integer32"
_PrtInHsiConnect_Object = MibTableColumn
prtInHsiConnect = _PrtInHsiConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 2, 1, 4),
    _PrtInHsiConnect_Type()
)
prtInHsiConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInHsiConnect.setStatus("current")


class _PrtInHsiRate_Type(Integer32):
    """Custom type prtInHsiRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              13,
              100,
              255)
        )
    )
    namedValues = NamedValues(
        *(("r600bps", 2),
          ("r1200bps", 3),
          ("r2400bps", 4),
          ("r4800bps", 5),
          ("r9600bps", 6),
          ("r19200bps", 7),
          ("r38400bps", 8),
          ("r48kbps", 9),
          ("r56kbps", 10),
          ("r64kbps", 11),
          ("r128kbps", 12),
          ("concentrated", 13),
          ("notConnected", 100),
          ("notApplicable", 255))
    )


_PrtInHsiRate_Type.__name__ = "Integer32"
_PrtInHsiRate_Object = MibTableColumn
prtInHsiRate = _PrtInHsiRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 2, 1, 5),
    _PrtInHsiRate_Type()
)
prtInHsiRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInHsiRate.setStatus("current")
_PrtInHsiConcentratedTo_Type = Integer32
_PrtInHsiConcentratedTo_Object = MibTableColumn
prtInHsiConcentratedTo = _PrtInHsiConcentratedTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 8, 2, 1, 6),
    _PrtInHsiConcentratedTo_Type()
)
prtInHsiConcentratedTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInHsiConcentratedTo.setStatus("current")
_PrtPVc4Cnfg_ObjectIdentity = ObjectIdentity
prtPVc4Cnfg = _PrtPVc4Cnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9)
)
_PrtExPVc4CnfgTable_Object = MibTable
prtExPVc4CnfgTable = _PrtExPVc4CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1)
)
if mibBuilder.loadTexts:
    prtExPVc4CnfgTable.setStatus("current")
_PrtExPVc4CnfgEntry_Object = MibTableRow
prtExPVc4CnfgEntry = _PrtExPVc4CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1)
)
prtExPVc4CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExPVc4CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPVc4SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPVc4PrtIdx"),
)
if mibBuilder.loadTexts:
    prtExPVc4CnfgEntry.setStatus("current")


class _PrtExPVc4CnfgIdx_Type(Integer32):
    """Custom type prtExPVc4CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExPVc4CnfgIdx_Type.__name__ = "Integer32"
_PrtExPVc4CnfgIdx_Object = MibTableColumn
prtExPVc4CnfgIdx = _PrtExPVc4CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 1),
    _PrtExPVc4CnfgIdx_Type()
)
prtExPVc4CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPVc4CnfgIdx.setStatus("current")


class _PrtExPVc4SltIdx_Type(Integer32):
    """Custom type prtExPVc4SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExPVc4SltIdx_Type.__name__ = "Integer32"
_PrtExPVc4SltIdx_Object = MibTableColumn
prtExPVc4SltIdx = _PrtExPVc4SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 2),
    _PrtExPVc4SltIdx_Type()
)
prtExPVc4SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPVc4SltIdx.setStatus("current")


class _PrtExPVc4PrtIdx_Type(Integer32):
    """Custom type prtExPVc4PrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108))
    )


_PrtExPVc4PrtIdx_Type.__name__ = "Integer32"
_PrtExPVc4PrtIdx_Object = MibTableColumn
prtExPVc4PrtIdx = _PrtExPVc4PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 3),
    _PrtExPVc4PrtIdx_Type()
)
prtExPVc4PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPVc4PrtIdx.setStatus("current")


class _PrtExPVc4PrtType_Type(Integer32):
    """Custom type prtExPVc4PrtType based on Integer32"""
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
        *(("eAndM", 1),
          ("fxo", 2),
          ("fxs", 3),
          ("internal", 4),
          ("s0", 5),
          ("u", 6),
          ("sQsig", 7),
          ("uQsig", 8))
    )


_PrtExPVc4PrtType_Type.__name__ = "Integer32"
_PrtExPVc4PrtType_Object = MibTableColumn
prtExPVc4PrtType = _PrtExPVc4PrtType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 4),
    _PrtExPVc4PrtType_Type()
)
prtExPVc4PrtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4PrtType.setStatus("current")


class _PrtExPVc4Connect_Type(Integer32):
    """Custom type prtExPVc4Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExPVc4Connect_Type.__name__ = "Integer32"
_PrtExPVc4Connect_Object = MibTableColumn
prtExPVc4Connect = _PrtExPVc4Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 5),
    _PrtExPVc4Connect_Type()
)
prtExPVc4Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4Connect.setStatus("current")


class _PrtExPVc4IfType_Type(Integer32):
    """Custom type prtExPVc4IfType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("eAndM4wires", 2),
          ("eAndM2wires", 3),
          ("fxoGnd", 4),
          ("fxoLoop", 5),
          ("fxsGnd", 6),
          ("fxsLoop", 7),
          ("e1Framer", 8),
          ("e1Slave", 9),
          ("t1Framer", 10),
          ("t1Slave", 11))
    )


_PrtExPVc4IfType_Type.__name__ = "Integer32"
_PrtExPVc4IfType_Object = MibTableColumn
prtExPVc4IfType = _PrtExPVc4IfType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 6),
    _PrtExPVc4IfType_Type()
)
prtExPVc4IfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4IfType.setStatus("current")
_PrtExPVc4TxGain_Type = Integer32
_PrtExPVc4TxGain_Object = MibTableColumn
prtExPVc4TxGain = _PrtExPVc4TxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 7),
    _PrtExPVc4TxGain_Type()
)
prtExPVc4TxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4TxGain.setStatus("current")
_PrtExPVc4RxGain_Type = Integer32
_PrtExPVc4RxGain_Object = MibTableColumn
prtExPVc4RxGain = _PrtExPVc4RxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 8),
    _PrtExPVc4RxGain_Type()
)
prtExPVc4RxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4RxGain.setStatus("current")


class _PrtExPVc4MaxRate_Type(Integer32):
    """Custom type prtExPVc4MaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 1),
          ("r4800bps", 2),
          ("r7200bps", 3),
          ("r9600bps", 4),
          ("notApplicatble", 255))
    )


_PrtExPVc4MaxRate_Type.__name__ = "Integer32"
_PrtExPVc4MaxRate_Object = MibTableColumn
prtExPVc4MaxRate = _PrtExPVc4MaxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 9),
    _PrtExPVc4MaxRate_Type()
)
prtExPVc4MaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4MaxRate.setStatus("current")


class _PrtExPVc4Tc_Type(Integer32):
    """Custom type prtExPVc4Tc based on Integer32"""
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
        *(("t1sec", 1),
          ("t2sec", 2),
          ("t3sec", 3),
          ("t4sec", 4))
    )


_PrtExPVc4Tc_Type.__name__ = "Integer32"
_PrtExPVc4Tc_Object = MibTableColumn
prtExPVc4Tc = _PrtExPVc4Tc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 10),
    _PrtExPVc4Tc_Type()
)
prtExPVc4Tc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4Tc.setStatus("current")


class _PrtExPVc4Oos_Type(Integer32):
    """Custom type prtExPVc4Oos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("forcedIdle", 3),
          ("forcedBusy", 4),
          ("busyIdle", 5),
          ("idleBusy", 6))
    )


_PrtExPVc4Oos_Type.__name__ = "Integer32"
_PrtExPVc4Oos_Object = MibTableColumn
prtExPVc4Oos = _PrtExPVc4Oos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 11),
    _PrtExPVc4Oos_Type()
)
prtExPVc4Oos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4Oos.setStatus("current")


class _PrtExPVc4EchoCanceler_Type(Integer32):
    """Custom type prtExPVc4EchoCanceler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtExPVc4EchoCanceler_Type.__name__ = "Integer32"
_PrtExPVc4EchoCanceler_Object = MibTableColumn
prtExPVc4EchoCanceler = _PrtExPVc4EchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 12),
    _PrtExPVc4EchoCanceler_Type()
)
prtExPVc4EchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4EchoCanceler.setStatus("current")


class _PrtExPVc4VarDelay_Type(Integer32):
    """Custom type prtExPVc4VarDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_PrtExPVc4VarDelay_Type.__name__ = "Integer32"
_PrtExPVc4VarDelay_Object = MibTableColumn
prtExPVc4VarDelay = _PrtExPVc4VarDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 13),
    _PrtExPVc4VarDelay_Type()
)
prtExPVc4VarDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4VarDelay.setStatus("current")


class _PrtExPVc4CongLevel_Type(Integer32):
    """Custom type prtExPVc4CongLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70),
    )


_PrtExPVc4CongLevel_Type.__name__ = "Integer32"
_PrtExPVc4CongLevel_Object = MibTableColumn
prtExPVc4CongLevel = _PrtExPVc4CongLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 14),
    _PrtExPVc4CongLevel_Type()
)
prtExPVc4CongLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4CongLevel.setStatus("current")


class _PrtExPVc4Wire_Type(Integer32):
    """Custom type prtExPVc4Wire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("w2wire", 1),
          ("w4wire", 2),
          ("notApplicable", 255))
    )


_PrtExPVc4Wire_Type.__name__ = "Integer32"
_PrtExPVc4Wire_Object = MibTableColumn
prtExPVc4Wire = _PrtExPVc4Wire_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 15),
    _PrtExPVc4Wire_Type()
)
prtExPVc4Wire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4Wire.setStatus("current")


class _PrtExPVc4ExtensionType_Type(Integer32):
    """Custom type prtExPVc4ExtensionType based on Integer32"""
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
          ("forceConnect", 2),
          ("voiceSwitching", 3),
          ("transparent", 4),
          ("transparentPlus", 5),
          ("ipForceConnect", 6),
          ("permanentDial", 7),
          ("autoAccept", 8))
    )


_PrtExPVc4ExtensionType_Type.__name__ = "Integer32"
_PrtExPVc4ExtensionType_Object = MibTableColumn
prtExPVc4ExtensionType = _PrtExPVc4ExtensionType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 16),
    _PrtExPVc4ExtensionType_Type()
)
prtExPVc4ExtensionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4ExtensionType.setStatus("current")


class _PrtExPVc4ExtensionNumber_Type(DisplayString):
    """Custom type prtExPVc4ExtensionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_PrtExPVc4ExtensionNumber_Type.__name__ = "DisplayString"
_PrtExPVc4ExtensionNumber_Object = MibTableColumn
prtExPVc4ExtensionNumber = _PrtExPVc4ExtensionNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 17),
    _PrtExPVc4ExtensionNumber_Type()
)
prtExPVc4ExtensionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4ExtensionNumber.setStatus("current")


class _PrtExPVc4OutPulsing_Type(Integer32):
    """Custom type prtExPVc4OutPulsing based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExPVc4OutPulsing_Type.__name__ = "Integer32"
_PrtExPVc4OutPulsing_Object = MibTableColumn
prtExPVc4OutPulsing = _PrtExPVc4OutPulsing_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 18),
    _PrtExPVc4OutPulsing_Type()
)
prtExPVc4OutPulsing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4OutPulsing.setStatus("current")


class _PrtExPVc4HuntGroupMb_Type(Integer32):
    """Custom type prtExPVc4HuntGroupMb based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExPVc4HuntGroupMb_Type.__name__ = "Integer32"
_PrtExPVc4HuntGroupMb_Object = MibTableColumn
prtExPVc4HuntGroupMb = _PrtExPVc4HuntGroupMb_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 19),
    _PrtExPVc4HuntGroupMb_Type()
)
prtExPVc4HuntGroupMb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4HuntGroupMb.setStatus("current")


class _PrtExPVc4HuntGroupIdx_Type(Integer32):
    """Custom type prtExPVc4HuntGroupIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PrtExPVc4HuntGroupIdx_Type.__name__ = "Integer32"
_PrtExPVc4HuntGroupIdx_Object = MibTableColumn
prtExPVc4HuntGroupIdx = _PrtExPVc4HuntGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 20),
    _PrtExPVc4HuntGroupIdx_Type()
)
prtExPVc4HuntGroupIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4HuntGroupIdx.setStatus("current")


class _PrtExPVc4AutoFaxMode_Type(Integer32):
    """Custom type prtExPVc4AutoFaxMode based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExPVc4AutoFaxMode_Type.__name__ = "Integer32"
_PrtExPVc4AutoFaxMode_Object = MibTableColumn
prtExPVc4AutoFaxMode = _PrtExPVc4AutoFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 21),
    _PrtExPVc4AutoFaxMode_Type()
)
prtExPVc4AutoFaxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4AutoFaxMode.setStatus("current")


class _PrtExPVc4FaxRate_Type(Integer32):
    """Custom type prtExPVc4FaxRate based on Integer32"""
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
        *(("notConnected", 1),
          ("r4800bps", 2),
          ("r7200bps", 3),
          ("r9600bps", 4),
          ("r12000bps", 5),
          ("r14400bps", 6),
          ("r2400bps", 7),
          ("vbdFax", 8))
    )


_PrtExPVc4FaxRate_Type.__name__ = "Integer32"
_PrtExPVc4FaxRate_Object = MibTableColumn
prtExPVc4FaxRate = _PrtExPVc4FaxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 22),
    _PrtExPVc4FaxRate_Type()
)
prtExPVc4FaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4FaxRate.setStatus("current")


class _PrtExPVc4SeizeAck_Type(Integer32):
    """Custom type prtExPVc4SeizeAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExPVc4SeizeAck_Type.__name__ = "Integer32"
_PrtExPVc4SeizeAck_Object = MibTableColumn
prtExPVc4SeizeAck = _PrtExPVc4SeizeAck_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 23),
    _PrtExPVc4SeizeAck_Type()
)
prtExPVc4SeizeAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4SeizeAck.setStatus("current")


class _PrtExPVc4SignalingProtocol_Type(Integer32):
    """Custom type prtExPVc4SignalingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delayStart", 2),
          ("immediateStart", 3),
          ("winkStart", 4))
    )


_PrtExPVc4SignalingProtocol_Type.__name__ = "Integer32"
_PrtExPVc4SignalingProtocol_Object = MibTableColumn
prtExPVc4SignalingProtocol = _PrtExPVc4SignalingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 24),
    _PrtExPVc4SignalingProtocol_Type()
)
prtExPVc4SignalingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4SignalingProtocol.setStatus("current")
_PrtExPVc4DelayStart_Type = Integer32
_PrtExPVc4DelayStart_Object = MibTableColumn
prtExPVc4DelayStart = _PrtExPVc4DelayStart_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 25),
    _PrtExPVc4DelayStart_Type()
)
prtExPVc4DelayStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DelayStart.setStatus("current")
_PrtExPVc4WinkMinDuration_Type = Integer32
_PrtExPVc4WinkMinDuration_Object = MibTableColumn
prtExPVc4WinkMinDuration = _PrtExPVc4WinkMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 26),
    _PrtExPVc4WinkMinDuration_Type()
)
prtExPVc4WinkMinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4WinkMinDuration.setStatus("current")
_PrtExPVc4WinkMaxDuration_Type = Integer32
_PrtExPVc4WinkMaxDuration_Object = MibTableColumn
prtExPVc4WinkMaxDuration = _PrtExPVc4WinkMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 27),
    _PrtExPVc4WinkMaxDuration_Type()
)
prtExPVc4WinkMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4WinkMaxDuration.setStatus("current")


class _PrtExPVc4GenerateTone_Type(Integer32):
    """Custom type prtExPVc4GenerateTone based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExPVc4GenerateTone_Type.__name__ = "Integer32"
_PrtExPVc4GenerateTone_Object = MibTableColumn
prtExPVc4GenerateTone = _PrtExPVc4GenerateTone_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 28),
    _PrtExPVc4GenerateTone_Type()
)
prtExPVc4GenerateTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4GenerateTone.setStatus("current")


class _PrtExPVc4CodingLaw_Type(Integer32):
    """Custom type prtExPVc4CodingLaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLAW", 1),
          ("uLAW", 2))
    )


_PrtExPVc4CodingLaw_Type.__name__ = "Integer32"
_PrtExPVc4CodingLaw_Object = MibTableColumn
prtExPVc4CodingLaw = _PrtExPVc4CodingLaw_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 29),
    _PrtExPVc4CodingLaw_Type()
)
prtExPVc4CodingLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4CodingLaw.setStatus("current")


class _PrtExPVc4GenerateRingBack_Type(Integer32):
    """Custom type prtExPVc4GenerateRingBack based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtExPVc4GenerateRingBack_Type.__name__ = "Integer32"
_PrtExPVc4GenerateRingBack_Object = MibTableColumn
prtExPVc4GenerateRingBack = _PrtExPVc4GenerateRingBack_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 30),
    _PrtExPVc4GenerateRingBack_Type()
)
prtExPVc4GenerateRingBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4GenerateRingBack.setStatus("current")


class _PrtExPVc4ChannelId_Type(Integer32):
    """Custom type prtExPVc4ChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PrtExPVc4ChannelId_Type.__name__ = "Integer32"
_PrtExPVc4ChannelId_Object = MibTableColumn
prtExPVc4ChannelId = _PrtExPVc4ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 31),
    _PrtExPVc4ChannelId_Type()
)
prtExPVc4ChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4ChannelId.setStatus("current")


class _PrtExPVc4PortConnection_Type(Integer32):
    """Custom type prtExPVc4PortConnection based on Integer32"""
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
          ("line", 2),
          ("trunk", 3))
    )


_PrtExPVc4PortConnection_Type.__name__ = "Integer32"
_PrtExPVc4PortConnection_Object = MibTableColumn
prtExPVc4PortConnection = _PrtExPVc4PortConnection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 32),
    _PrtExPVc4PortConnection_Type()
)
prtExPVc4PortConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4PortConnection.setStatus("current")


class _PrtExPVc4CoderAndRate_Type(Integer32):
    """Custom type prtExPVc4CoderAndRate based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("g7231r6300BPS", 2),
          ("g7231r5300BPS", 3),
          ("g729A8KBPS", 4),
          ("g711aLAW", 5),
          ("g711uLAW", 6),
          ("g726r16KBPS", 7),
          ("g726r24KBPS", 8),
          ("g726r32KBPS", 9),
          ("g726r40KBPS", 10),
          ("g727r16KBPS", 11),
          ("g727r24r16KBPS", 12),
          ("g727r24KBPS", 13),
          ("g727r16r32KBPS", 14),
          ("g727r32r24KBPS", 15),
          ("g727r32KBPS", 16),
          ("g727r40r16KBPS", 17),
          ("g727r40r24KBPS", 18),
          ("g727r40r32KBPS", 19),
          ("transparent", 20),
          ("netcoder6400BPS", 21),
          ("netcoder7200BPS", 22),
          ("netcoder8KBPS", 23),
          ("netcoder8800BPS", 24),
          ("netcoder9600BPS", 25),
          ("lowBitRateR2660BPS", 26),
          ("amr4750BPS", 27),
          ("amr5150BPS", 28),
          ("amr5900BPS", 29),
          ("amr6700BPS", 30),
          ("amr7400BPS", 31),
          ("amr7950BPS", 32),
          ("amr10200BPS", 33),
          ("amr12200BPS", 34))
    )


_PrtExPVc4CoderAndRate_Type.__name__ = "Integer32"
_PrtExPVc4CoderAndRate_Object = MibTableColumn
prtExPVc4CoderAndRate = _PrtExPVc4CoderAndRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 33),
    _PrtExPVc4CoderAndRate_Type()
)
prtExPVc4CoderAndRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4CoderAndRate.setStatus("current")
_PrtExPVc4DestinationNum_Type = DisplayString
_PrtExPVc4DestinationNum_Object = MibTableColumn
prtExPVc4DestinationNum = _PrtExPVc4DestinationNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 34),
    _PrtExPVc4DestinationNum_Type()
)
prtExPVc4DestinationNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DestinationNum.setStatus("current")


class _PrtExPVc4DtmfRelay_Type(Integer32):
    """Custom type prtExPVc4DtmfRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_PrtExPVc4DtmfRelay_Type.__name__ = "Integer32"
_PrtExPVc4DtmfRelay_Object = MibTableColumn
prtExPVc4DtmfRelay = _PrtExPVc4DtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 35),
    _PrtExPVc4DtmfRelay_Type()
)
prtExPVc4DtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DtmfRelay.setStatus("current")
_PrtExPVc4DiscOnSilence_Type = Integer32
_PrtExPVc4DiscOnSilence_Object = MibTableColumn
prtExPVc4DiscOnSilence = _PrtExPVc4DiscOnSilence_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 36),
    _PrtExPVc4DiscOnSilence_Type()
)
prtExPVc4DiscOnSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DiscOnSilence.setStatus("current")


class _PrtExPVc4DynamicJitter_Type(Integer32):
    """Custom type prtExPVc4DynamicJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_PrtExPVc4DynamicJitter_Type.__name__ = "Integer32"
_PrtExPVc4DynamicJitter_Object = MibTableColumn
prtExPVc4DynamicJitter = _PrtExPVc4DynamicJitter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 37),
    _PrtExPVc4DynamicJitter_Type()
)
prtExPVc4DynamicJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DynamicJitter.setStatus("current")


class _PrtExPVc4EandMType_Type(Integer32):
    """Custom type prtExPVc4EandMType based on Integer32"""
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
        *(("notApplicable", 1),
          ("type1", 2),
          ("type2", 3),
          ("type3", 4),
          ("ssdc5", 5))
    )


_PrtExPVc4EandMType_Type.__name__ = "Integer32"
_PrtExPVc4EandMType_Object = MibTableColumn
prtExPVc4EandMType = _PrtExPVc4EandMType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 38),
    _PrtExPVc4EandMType_Type()
)
prtExPVc4EandMType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4EandMType.setStatus("current")


class _PrtExPVc4Rate_Type(Integer32):
    """Custom type prtExPVc4Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PrtExPVc4Rate_Type.__name__ = "Integer32"
_PrtExPVc4Rate_Object = MibTableColumn
prtExPVc4Rate = _PrtExPVc4Rate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 39),
    _PrtExPVc4Rate_Type()
)
prtExPVc4Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4Rate.setStatus("current")
_PrtExPVc4FrameSize_Type = Integer32
_PrtExPVc4FrameSize_Object = MibTableColumn
prtExPVc4FrameSize = _PrtExPVc4FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 40),
    _PrtExPVc4FrameSize_Type()
)
prtExPVc4FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4FrameSize.setStatus("current")
_PrtExPVc4MultiplexInterval_Type = Integer32
_PrtExPVc4MultiplexInterval_Object = MibTableColumn
prtExPVc4MultiplexInterval = _PrtExPVc4MultiplexInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 41),
    _PrtExPVc4MultiplexInterval_Type()
)
prtExPVc4MultiplexInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4MultiplexInterval.setStatus("current")


class _PrtExPVc4TransportProtocol_Type(Integer32):
    """Custom type prtExPVc4TransportProtocol based on Integer32"""
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
          ("ptp", 2),
          ("aal2oMpls", 3))
    )


_PrtExPVc4TransportProtocol_Type.__name__ = "Integer32"
_PrtExPVc4TransportProtocol_Object = MibTableColumn
prtExPVc4TransportProtocol = _PrtExPVc4TransportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 42),
    _PrtExPVc4TransportProtocol_Type()
)
prtExPVc4TransportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4TransportProtocol.setStatus("current")


class _PrtExPVc4MultiFreqRelay_Type(Integer32):
    """Custom type prtExPVc4MultiFreqRelay based on Integer32"""
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


_PrtExPVc4MultiFreqRelay_Type.__name__ = "Integer32"
_PrtExPVc4MultiFreqRelay_Object = MibTableColumn
prtExPVc4MultiFreqRelay = _PrtExPVc4MultiFreqRelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 43),
    _PrtExPVc4MultiFreqRelay_Type()
)
prtExPVc4MultiFreqRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4MultiFreqRelay.setStatus("current")
_PrtExPVc4MinPulseWidth_Type = Integer32
_PrtExPVc4MinPulseWidth_Object = MibTableColumn
prtExPVc4MinPulseWidth = _PrtExPVc4MinPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 44),
    _PrtExPVc4MinPulseWidth_Type()
)
prtExPVc4MinPulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4MinPulseWidth.setStatus("current")
_PrtExPVc4MinPowerLevel_Type = Integer32
_PrtExPVc4MinPowerLevel_Object = MibTableColumn
prtExPVc4MinPowerLevel = _PrtExPVc4MinPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 45),
    _PrtExPVc4MinPowerLevel_Type()
)
prtExPVc4MinPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4MinPowerLevel.setStatus("current")


class _PrtExPVc4SuperTandem_Type(Integer32):
    """Custom type prtExPVc4SuperTandem based on Integer32"""
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


_PrtExPVc4SuperTandem_Type.__name__ = "Integer32"
_PrtExPVc4SuperTandem_Object = MibTableColumn
prtExPVc4SuperTandem = _PrtExPVc4SuperTandem_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 46),
    _PrtExPVc4SuperTandem_Type()
)
prtExPVc4SuperTandem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4SuperTandem.setStatus("current")
_PrtExPVc4DestIp_Type = IpAddress
_PrtExPVc4DestIp_Object = MibTableColumn
prtExPVc4DestIp = _PrtExPVc4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 47),
    _PrtExPVc4DestIp_Type()
)
prtExPVc4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DestIp.setStatus("current")
_PrtExPVc4DestBundle_Type = Integer32
_PrtExPVc4DestBundle_Object = MibTableColumn
prtExPVc4DestBundle = _PrtExPVc4DestBundle_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 48),
    _PrtExPVc4DestBundle_Type()
)
prtExPVc4DestBundle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DestBundle.setStatus("current")
_PrtExPVc4SrcIpAddress_Type = IpAddress
_PrtExPVc4SrcIpAddress_Object = MibTableColumn
prtExPVc4SrcIpAddress = _PrtExPVc4SrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 49),
    _PrtExPVc4SrcIpAddress_Type()
)
prtExPVc4SrcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4SrcIpAddress.setStatus("current")
_PrtExPVc4SrcIpMask_Type = IpAddress
_PrtExPVc4SrcIpMask_Object = MibTableColumn
prtExPVc4SrcIpMask = _PrtExPVc4SrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 50),
    _PrtExPVc4SrcIpMask_Type()
)
prtExPVc4SrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4SrcIpMask.setStatus("current")
_PrtExPVc4DefaultGateway_Type = IpAddress
_PrtExPVc4DefaultGateway_Object = MibTableColumn
prtExPVc4DefaultGateway = _PrtExPVc4DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 51),
    _PrtExPVc4DefaultGateway_Type()
)
prtExPVc4DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DefaultGateway.setStatus("current")
_PrtExPVc4SigPacketInterval_Type = Unsigned32
_PrtExPVc4SigPacketInterval_Object = MibTableColumn
prtExPVc4SigPacketInterval = _PrtExPVc4SigPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 1, 1, 52),
    _PrtExPVc4SigPacketInterval_Type()
)
prtExPVc4SigPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4SigPacketInterval.setStatus("current")
_PrtExPVc4DlciTable_Object = MibTable
prtExPVc4DlciTable = _PrtExPVc4DlciTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2)
)
if mibBuilder.loadTexts:
    prtExPVc4DlciTable.setStatus("current")
_PrtExPVc4DlciEntry_Object = MibTableRow
prtExPVc4DlciEntry = _PrtExPVc4DlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1)
)
prtExPVc4DlciEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExPVc4DlciCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPVc4DlciSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExPVc4DlciPrtIdx"),
)
if mibBuilder.loadTexts:
    prtExPVc4DlciEntry.setStatus("current")


class _PrtExPVc4DlciCnfgIdx_Type(Integer32):
    """Custom type prtExPVc4DlciCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExPVc4DlciCnfgIdx_Type.__name__ = "Integer32"
_PrtExPVc4DlciCnfgIdx_Object = MibTableColumn
prtExPVc4DlciCnfgIdx = _PrtExPVc4DlciCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 1),
    _PrtExPVc4DlciCnfgIdx_Type()
)
prtExPVc4DlciCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPVc4DlciCnfgIdx.setStatus("current")


class _PrtExPVc4DlciSltIdx_Type(Integer32):
    """Custom type prtExPVc4DlciSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExPVc4DlciSltIdx_Type.__name__ = "Integer32"
_PrtExPVc4DlciSltIdx_Object = MibTableColumn
prtExPVc4DlciSltIdx = _PrtExPVc4DlciSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 2),
    _PrtExPVc4DlciSltIdx_Type()
)
prtExPVc4DlciSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPVc4DlciSltIdx.setStatus("current")


class _PrtExPVc4DlciPrtIdx_Type(Integer32):
    """Custom type prtExPVc4DlciPrtIdx based on Integer32"""
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
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4))
    )


_PrtExPVc4DlciPrtIdx_Type.__name__ = "Integer32"
_PrtExPVc4DlciPrtIdx_Object = MibTableColumn
prtExPVc4DlciPrtIdx = _PrtExPVc4DlciPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 3),
    _PrtExPVc4DlciPrtIdx_Type()
)
prtExPVc4DlciPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPVc4DlciPrtIdx.setStatus("current")


class _PrtExPVc4DlciValid_Type(Integer32):
    """Custom type prtExPVc4DlciValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExPVc4DlciValid_Type.__name__ = "Integer32"
_PrtExPVc4DlciValid_Object = MibTableColumn
prtExPVc4DlciValid = _PrtExPVc4DlciValid_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 4),
    _PrtExPVc4DlciValid_Type()
)
prtExPVc4DlciValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DlciValid.setStatus("current")


class _PrtExPVc4DlciIConSlt_Type(Integer32):
    """Custom type prtExPVc4DlciIConSlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExPVc4DlciIConSlt_Type.__name__ = "Integer32"
_PrtExPVc4DlciIConSlt_Object = MibTableColumn
prtExPVc4DlciIConSlt = _PrtExPVc4DlciIConSlt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 5),
    _PrtExPVc4DlciIConSlt_Type()
)
prtExPVc4DlciIConSlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DlciIConSlt.setStatus("current")


class _PrtExPVc4DlciIConPrt_Type(Integer32):
    """Custom type prtExPVc4DlciIConPrt based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("noConnect", 100),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108),
          ("inPrt9", 109),
          ("inPrt10", 110),
          ("inPrt11", 111),
          ("inPrt12", 112))
    )


_PrtExPVc4DlciIConPrt_Type.__name__ = "Integer32"
_PrtExPVc4DlciIConPrt_Object = MibTableColumn
prtExPVc4DlciIConPrt = _PrtExPVc4DlciIConPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 6),
    _PrtExPVc4DlciIConPrt_Type()
)
prtExPVc4DlciIConPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DlciIConPrt.setStatus("current")


class _PrtExPVc4DlciIConDlci_Type(Integer32):
    """Custom type prtExPVc4DlciIConDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 991),
    )


_PrtExPVc4DlciIConDlci_Type.__name__ = "Integer32"
_PrtExPVc4DlciIConDlci_Object = MibTableColumn
prtExPVc4DlciIConDlci = _PrtExPVc4DlciIConDlci_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 7),
    _PrtExPVc4DlciIConDlci_Type()
)
prtExPVc4DlciIConDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DlciIConDlci.setStatus("current")


class _PrtExPVc4DlciTxBc_Type(Integer32):
    """Custom type prtExPVc4DlciTxBc based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("txBc9600bps", 3),
          ("txBc14400bps", 4),
          ("txBc19200bps", 5),
          ("txBc28800bps", 6),
          ("txBc32000bps", 7),
          ("txBc38400bps", 8),
          ("txBc48000bps", 9),
          ("txBc56000bps", 10),
          ("txBc57600bps", 11),
          ("txBc64Kbps", 12),
          ("txBc128Kbps", 13),
          ("txBc192Kbps", 14),
          ("txBc256Kbps", 15),
          ("txBc320Kbps", 16),
          ("txBc384Kbps", 17),
          ("txBc448Kbps", 18),
          ("txBc512Kbps", 19),
          ("txBc768Kbps", 20),
          ("txBc1024Kbps", 21),
          ("txBc16000bps", 25),
          ("txBc112Kbps", 26))
    )


_PrtExPVc4DlciTxBc_Type.__name__ = "Integer32"
_PrtExPVc4DlciTxBc_Object = MibTableColumn
prtExPVc4DlciTxBc = _PrtExPVc4DlciTxBc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 8),
    _PrtExPVc4DlciTxBc_Type()
)
prtExPVc4DlciTxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DlciTxBc.setStatus("current")


class _PrtExPVc4DlciTxBe_Type(Integer32):
    """Custom type prtExPVc4DlciTxBe based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("txBe9600bps", 3),
          ("txBe14400bps", 4),
          ("txBe19200bps", 5),
          ("txBe28800bps", 6),
          ("txBe32000bps", 7),
          ("txBe38400bps", 8),
          ("txBe48000bps", 9),
          ("txBe56000bps", 10),
          ("txBe57600bps", 11),
          ("txBe64Kbps", 12),
          ("txBe128Kbps", 13),
          ("txBe192Kbps", 14),
          ("txBe256Kbps", 15),
          ("txBe320Kbps", 16),
          ("txBe384Kbps", 17),
          ("txBe448Kbps", 18),
          ("txBe512Kbps", 19),
          ("txBe768Kbps", 20),
          ("txBe1024Kbps", 21),
          ("txBc16000bps", 25),
          ("txBc112Kbps", 26))
    )


_PrtExPVc4DlciTxBe_Type.__name__ = "Integer32"
_PrtExPVc4DlciTxBe_Object = MibTableColumn
prtExPVc4DlciTxBe = _PrtExPVc4DlciTxBe_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 9),
    _PrtExPVc4DlciTxBe_Type()
)
prtExPVc4DlciTxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DlciTxBe.setStatus("current")


class _PrtExPVc4DlciRxBc_Type(Integer32):
    """Custom type prtExPVc4DlciRxBc based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("rxBc9600bps", 3),
          ("rxBc14400bps", 4),
          ("rxBc19200bps", 5),
          ("rxBc28800bps", 6),
          ("rxBc32000bps", 7),
          ("rxBc38400bps", 8),
          ("rxBc48000bps", 9),
          ("rxBc56000bps", 10),
          ("rxBc57600bps", 11),
          ("rxBc64Kbps", 12),
          ("rxBc128Kbps", 13),
          ("rxBc192Kbps", 14),
          ("rxBc256Kbps", 15),
          ("rxBc320Kbps", 16),
          ("rxBc384Kbps", 17),
          ("rxBc448Kbps", 18),
          ("rxBc512Kbps", 19),
          ("rxBc768Kbps", 20),
          ("rxBc1024Kbps", 21),
          ("rxBc16000bps", 25),
          ("rxBc112Kbps", 26))
    )


_PrtExPVc4DlciRxBc_Type.__name__ = "Integer32"
_PrtExPVc4DlciRxBc_Object = MibTableColumn
prtExPVc4DlciRxBc = _PrtExPVc4DlciRxBc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 10),
    _PrtExPVc4DlciRxBc_Type()
)
prtExPVc4DlciRxBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DlciRxBc.setStatus("current")


class _PrtExPVc4DlciRxBe_Type(Integer32):
    """Custom type prtExPVc4DlciRxBe based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("zero", 2),
          ("rxBe9600bps", 3),
          ("rxBe14400bps", 4),
          ("rxBe19200bps", 5),
          ("rxBe28800bps", 6),
          ("rxBe32000bps", 7),
          ("rxBe38400bps", 8),
          ("rxBe48000bps", 9),
          ("rxBe56000bps", 10),
          ("rxBe57600bps", 11),
          ("rxBe64Kbps", 12),
          ("rxBe128Kbps", 13),
          ("rxBe192Kbps", 14),
          ("rxBe256Kbps", 15),
          ("rxBe320Kbps", 16),
          ("rxBe384Kbps", 17),
          ("rxBe448Kbps", 18),
          ("rxBe512Kbps", 19),
          ("rxBe768Kbps", 20),
          ("rxBe1024Kbps", 21),
          ("rxBc16000bps", 25),
          ("rxBc112Kbps", 26))
    )


_PrtExPVc4DlciRxBe_Type.__name__ = "Integer32"
_PrtExPVc4DlciRxBe_Object = MibTableColumn
prtExPVc4DlciRxBe = _PrtExPVc4DlciRxBe_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 11),
    _PrtExPVc4DlciRxBe_Type()
)
prtExPVc4DlciRxBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DlciRxBe.setStatus("current")


class _PrtExPVc4DlciPriority_Type(Integer32):
    """Custom type prtExPVc4DlciPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 8),
    )


_PrtExPVc4DlciPriority_Type.__name__ = "Integer32"
_PrtExPVc4DlciPriority_Object = MibTableColumn
prtExPVc4DlciPriority = _PrtExPVc4DlciPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 12),
    _PrtExPVc4DlciPriority_Type()
)
prtExPVc4DlciPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExPVc4DlciPriority.setStatus("current")


class _PrtExPVc4DlciStatus_Type(Integer32):
    """Custom type prtExPVc4DlciStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2))
    )


_PrtExPVc4DlciStatus_Type.__name__ = "Integer32"
_PrtExPVc4DlciStatus_Object = MibTableColumn
prtExPVc4DlciStatus = _PrtExPVc4DlciStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 9, 2, 1, 13),
    _PrtExPVc4DlciStatus_Type()
)
prtExPVc4DlciStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExPVc4DlciStatus.setStatus("current")
_PrtHsrCnfg_ObjectIdentity = ObjectIdentity
prtHsrCnfg = _PrtHsrCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10)
)
_PrtExHsrCnfgTable_Object = MibTable
prtExHsrCnfgTable = _PrtExHsrCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1)
)
if mibBuilder.loadTexts:
    prtExHsrCnfgTable.setStatus("current")
_PrtExHsrCnfgEntry_Object = MibTableRow
prtExHsrCnfgEntry = _PrtExHsrCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1)
)
prtExHsrCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExHsrCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExHsrSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExHsrPrtIdx"),
)
if mibBuilder.loadTexts:
    prtExHsrCnfgEntry.setStatus("current")


class _PrtExHsrCnfgIdx_Type(Integer32):
    """Custom type prtExHsrCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExHsrCnfgIdx_Type.__name__ = "Integer32"
_PrtExHsrCnfgIdx_Object = MibTableColumn
prtExHsrCnfgIdx = _PrtExHsrCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 1),
    _PrtExHsrCnfgIdx_Type()
)
prtExHsrCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHsrCnfgIdx.setStatus("current")


class _PrtExHsrSltIdx_Type(Integer32):
    """Custom type prtExHsrSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("io13", 17),
          ("io14", 18),
          ("io15", 19))
    )


_PrtExHsrSltIdx_Type.__name__ = "Integer32"
_PrtExHsrSltIdx_Object = MibTableColumn
prtExHsrSltIdx = _PrtExHsrSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 2),
    _PrtExHsrSltIdx_Type()
)
prtExHsrSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHsrSltIdx.setStatus("current")
_PrtExHsrPrtIdx_Type = Integer32
_PrtExHsrPrtIdx_Object = MibTableColumn
prtExHsrPrtIdx = _PrtExHsrPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 3),
    _PrtExHsrPrtIdx_Type()
)
prtExHsrPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExHsrPrtIdx.setStatus("current")


class _PrtExHsrConnect_Type(Integer32):
    """Custom type prtExHsrConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExHsrConnect_Type.__name__ = "Integer32"
_PrtExHsrConnect_Object = MibTableColumn
prtExHsrConnect = _PrtExHsrConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 4),
    _PrtExHsrConnect_Type()
)
prtExHsrConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrConnect.setStatus("current")


class _PrtExHsrProtocol_Type(Integer32):
    """Custom type prtExHsrProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sync", 2),
          ("async", 3))
    )


_PrtExHsrProtocol_Type.__name__ = "Integer32"
_PrtExHsrProtocol_Object = MibTableColumn
prtExHsrProtocol = _PrtExHsrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 5),
    _PrtExHsrProtocol_Type()
)
prtExHsrProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrProtocol.setStatus("current")


class _PrtExHsrRate_Type(Integer32):
    """Custom type prtExHsrRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              100)
        )
    )
    namedValues = NamedValues(
        *(("r600bps", 2),
          ("r1200bps", 3),
          ("r2400bps", 4),
          ("r4800bps", 5),
          ("r9600bps", 6),
          ("r19200bps", 7),
          ("r38400bps", 8),
          ("r48kbps", 9),
          ("r56kbps", 10),
          ("r64kbps", 11),
          ("r16000bps", 12),
          ("r32000bps", 13),
          ("r57600bps", 14),
          ("r115200bps", 15),
          ("r128000bps", 16),
          ("r7200bps", 17),
          ("r14400bps", 18),
          ("r28800bps", 19),
          ("notConnected", 100))
    )


_PrtExHsrRate_Type.__name__ = "Integer32"
_PrtExHsrRate_Object = MibTableColumn
prtExHsrRate = _PrtExHsrRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 6),
    _PrtExHsrRate_Type()
)
prtExHsrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrRate.setStatus("current")


class _PrtExHsrDataBits_Type(Integer32):
    """Custom type prtExHsrDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("d5bits", 1),
          ("d6bits", 2),
          ("d7bits", 3),
          ("d8bits", 4),
          ("notApplicable", 255))
    )


_PrtExHsrDataBits_Type.__name__ = "Integer32"
_PrtExHsrDataBits_Object = MibTableColumn
prtExHsrDataBits = _PrtExHsrDataBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 7),
    _PrtExHsrDataBits_Type()
)
prtExHsrDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrDataBits.setStatus("current")


class _PrtExHsrParity_Type(Integer32):
    """Custom type prtExHsrParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3),
          ("odd", 4),
          ("even", 5),
          ("notApplicable", 255))
    )


_PrtExHsrParity_Type.__name__ = "Integer32"
_PrtExHsrParity_Object = MibTableColumn
prtExHsrParity = _PrtExHsrParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 8),
    _PrtExHsrParity_Type()
)
prtExHsrParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrParity.setStatus("current")


class _PrtExHsrStopBits_Type(Integer32):
    """Custom type prtExHsrStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("stopBits1Bit", 1),
          ("stopBits2Bits", 2),
          ("notApplicable", 255))
    )


_PrtExHsrStopBits_Type.__name__ = "Integer32"
_PrtExHsrStopBits_Object = MibTableColumn
prtExHsrStopBits = _PrtExHsrStopBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 9),
    _PrtExHsrStopBits_Type()
)
prtExHsrStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrStopBits.setStatus("current")


class _PrtExHsrCts_Type(Integer32):
    """Custom type prtExHsrCts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("rts", 3),
          ("notApplicable", 255))
    )


_PrtExHsrCts_Type.__name__ = "Integer32"
_PrtExHsrCts_Object = MibTableColumn
prtExHsrCts = _PrtExHsrCts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 10),
    _PrtExHsrCts_Type()
)
prtExHsrCts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrCts.setStatus("current")


class _PrtExHsrClkMode_Type(Integer32):
    """Custom type prtExHsrClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("extDce", 2),
          ("notApplicable", 255))
    )


_PrtExHsrClkMode_Type.__name__ = "Integer32"
_PrtExHsrClkMode_Object = MibTableColumn
prtExHsrClkMode = _PrtExHsrClkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 11),
    _PrtExHsrClkMode_Type()
)
prtExHsrClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrClkMode.setStatus("current")


class _PrtExHsrLinkTo_Type(Integer32):
    """Custom type prtExHsrLinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExHsrLinkTo_Type.__name__ = "Integer32"
_PrtExHsrLinkTo_Object = MibTableColumn
prtExHsrLinkTo = _PrtExHsrLinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 12),
    _PrtExHsrLinkTo_Type()
)
prtExHsrLinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrLinkTo.setStatus("deprecated")


class _PrtExHsrDcdDsr_Type(Integer32):
    """Custom type prtExHsrDcdDsr based on Integer32"""
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
          ("local", 2),
          ("endToEnd", 3))
    )


_PrtExHsrDcdDsr_Type.__name__ = "Integer32"
_PrtExHsrDcdDsr_Object = MibTableColumn
prtExHsrDcdDsr = _PrtExHsrDcdDsr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 13),
    _PrtExHsrDcdDsr_Type()
)
prtExHsrDcdDsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrDcdDsr.setStatus("current")


class _PrtExHsrOperMode_Type(Integer32):
    """Custom type prtExHsrOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("unidirectRx", 3),
          ("broadcast", 4))
    )


_PrtExHsrOperMode_Type.__name__ = "Integer32"
_PrtExHsrOperMode_Object = MibTableColumn
prtExHsrOperMode = _PrtExHsrOperMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 14),
    _PrtExHsrOperMode_Type()
)
prtExHsrOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrOperMode.setStatus("current")


class _PrtExHsrRtsDtr_Type(Integer32):
    """Custom type prtExHsrRtsDtr based on Integer32"""
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
          ("local", 2),
          ("endToEnd", 3))
    )


_PrtExHsrRtsDtr_Type.__name__ = "Integer32"
_PrtExHsrRtsDtr_Object = MibTableColumn
prtExHsrRtsDtr = _PrtExHsrRtsDtr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 15),
    _PrtExHsrRtsDtr_Type()
)
prtExHsrRtsDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrRtsDtr.setStatus("current")


class _PrtExHsrLlbEnable_Type(Integer32):
    """Custom type prtExHsrLlbEnable based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 3))
    )


_PrtExHsrLlbEnable_Type.__name__ = "Integer32"
_PrtExHsrLlbEnable_Object = MibTableColumn
prtExHsrLlbEnable = _PrtExHsrLlbEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 16),
    _PrtExHsrLlbEnable_Type()
)
prtExHsrLlbEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrLlbEnable.setStatus("current")


class _PrtExHsrRlbEnable_Type(Integer32):
    """Custom type prtExHsrRlbEnable based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 3))
    )


_PrtExHsrRlbEnable_Type.__name__ = "Integer32"
_PrtExHsrRlbEnable_Object = MibTableColumn
prtExHsrRlbEnable = _PrtExHsrRlbEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 17),
    _PrtExHsrRlbEnable_Type()
)
prtExHsrRlbEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrRlbEnable.setStatus("current")


class _PrtExHsrRateAdapt_Type(Integer32):
    """Custom type prtExHsrRateAdapt based on Integer32"""
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
          ("proprietary", 2),
          ("v110", 3))
    )


_PrtExHsrRateAdapt_Type.__name__ = "Integer32"
_PrtExHsrRateAdapt_Object = MibTableColumn
prtExHsrRateAdapt = _PrtExHsrRateAdapt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 18),
    _PrtExHsrRateAdapt_Type()
)
prtExHsrRateAdapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrRateAdapt.setStatus("current")


class _PrtExHsrRemoteModem_Type(Integer32):
    """Custom type prtExHsrRemoteModem based on Integer32"""
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
          ("asmi31", 2),
          ("asmi31s2", 3))
    )


_PrtExHsrRemoteModem_Type.__name__ = "Integer32"
_PrtExHsrRemoteModem_Object = MibTableColumn
prtExHsrRemoteModem = _PrtExHsrRemoteModem_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 19),
    _PrtExHsrRemoteModem_Type()
)
prtExHsrRemoteModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrRemoteModem.setStatus("current")


class _PrtExHsrEncapsMode_Type(Integer32):
    """Custom type prtExHsrEncapsMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("bwOptimized", 2),
          ("latencyOptimized", 3),
          ("asmi31", 4))
    )


_PrtExHsrEncapsMode_Type.__name__ = "Integer32"
_PrtExHsrEncapsMode_Object = MibTableColumn
prtExHsrEncapsMode = _PrtExHsrEncapsMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 10, 1, 1, 20),
    _PrtExHsrEncapsMode_Type()
)
prtExHsrEncapsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExHsrEncapsMode.setStatus("current")
_PrtMbeCnfg_ObjectIdentity = ObjectIdentity
prtMbeCnfg = _PrtMbeCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11)
)
_PrtExMbeCnfgTable_Object = MibTable
prtExMbeCnfgTable = _PrtExMbeCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 1)
)
if mibBuilder.loadTexts:
    prtExMbeCnfgTable.setStatus("current")
_PrtExMbeCnfgEntry_Object = MibTableRow
prtExMbeCnfgEntry = _PrtExMbeCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 1, 1)
)
prtExMbeCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExMbeCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExMbeSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExMbePrtIdx"),
)
if mibBuilder.loadTexts:
    prtExMbeCnfgEntry.setStatus("current")


class _PrtExMbeCnfgIdx_Type(Integer32):
    """Custom type prtExMbeCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExMbeCnfgIdx_Type.__name__ = "Integer32"
_PrtExMbeCnfgIdx_Object = MibTableColumn
prtExMbeCnfgIdx = _PrtExMbeCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 1, 1, 1),
    _PrtExMbeCnfgIdx_Type()
)
prtExMbeCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExMbeCnfgIdx.setStatus("current")


class _PrtExMbeSltIdx_Type(Integer32):
    """Custom type prtExMbeSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExMbeSltIdx_Type.__name__ = "Integer32"
_PrtExMbeSltIdx_Object = MibTableColumn
prtExMbeSltIdx = _PrtExMbeSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 1, 1, 2),
    _PrtExMbeSltIdx_Type()
)
prtExMbeSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExMbeSltIdx.setStatus("current")


class _PrtExMbePrtIdx_Type(Integer32):
    """Custom type prtExMbePrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exPrt1", 1)
    )


_PrtExMbePrtIdx_Type.__name__ = "Integer32"
_PrtExMbePrtIdx_Object = MibTableColumn
prtExMbePrtIdx = _PrtExMbePrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 1, 1, 3),
    _PrtExMbePrtIdx_Type()
)
prtExMbePrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExMbePrtIdx.setStatus("current")


class _PrtExMbeLan_Type(Integer32):
    """Custom type prtExMbeLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remote", 1),
          ("main", 2))
    )


_PrtExMbeLan_Type.__name__ = "Integer32"
_PrtExMbeLan_Object = MibTableColumn
prtExMbeLan = _PrtExMbeLan_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 1, 1, 4),
    _PrtExMbeLan_Type()
)
prtExMbeLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExMbeLan.setStatus("current")
_PrtInMbeCnfgTable_Object = MibTable
prtInMbeCnfgTable = _PrtInMbeCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 2)
)
if mibBuilder.loadTexts:
    prtInMbeCnfgTable.setStatus("current")
_PrtInMbeCnfgEntry_Object = MibTableRow
prtInMbeCnfgEntry = _PrtInMbeCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 2, 1)
)
prtInMbeCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtInMbeCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtInMbeSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtInMbePrtIdx"),
)
if mibBuilder.loadTexts:
    prtInMbeCnfgEntry.setStatus("current")


class _PrtInMbeCnfgIdx_Type(Integer32):
    """Custom type prtInMbeCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtInMbeCnfgIdx_Type.__name__ = "Integer32"
_PrtInMbeCnfgIdx_Object = MibTableColumn
prtInMbeCnfgIdx = _PrtInMbeCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 2, 1, 1),
    _PrtInMbeCnfgIdx_Type()
)
prtInMbeCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInMbeCnfgIdx.setStatus("current")


class _PrtInMbeSltIdx_Type(Integer32):
    """Custom type prtInMbeSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInMbeSltIdx_Type.__name__ = "Integer32"
_PrtInMbeSltIdx_Object = MibTableColumn
prtInMbeSltIdx = _PrtInMbeSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 2, 1, 2),
    _PrtInMbeSltIdx_Type()
)
prtInMbeSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInMbeSltIdx.setStatus("current")


class _PrtInMbePrtIdx_Type(Integer32):
    """Custom type prtInMbePrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            101
        )
    )
    namedValues = NamedValues(
        ("inPrt1", 101)
    )


_PrtInMbePrtIdx_Type.__name__ = "Integer32"
_PrtInMbePrtIdx_Object = MibTableColumn
prtInMbePrtIdx = _PrtInMbePrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 2, 1, 3),
    _PrtInMbePrtIdx_Type()
)
prtInMbePrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInMbePrtIdx.setStatus("current")


class _PrtInMbeConnect_Type(Integer32):
    """Custom type prtInMbeConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtInMbeConnect_Type.__name__ = "Integer32"
_PrtInMbeConnect_Object = MibTableColumn
prtInMbeConnect = _PrtInMbeConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 2, 1, 4),
    _PrtInMbeConnect_Type()
)
prtInMbeConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInMbeConnect.setStatus("current")


class _PrtInMbeRate_Type(Integer32):
    """Custom type prtInMbeRate based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("r1x64eq64Kbps", 1),
          ("r2x64eq128Kbps", 2),
          ("r3x64eq192Kbps", 3),
          ("r4x64eq256Kbps", 4),
          ("r5x64eq320Kbps", 5),
          ("r6x64eq384Kbps", 6),
          ("r7x64eq448Kbps", 7),
          ("r8x64eq512Kbps", 8),
          ("r9x64eq576Kbps", 9),
          ("r10x64eq640Kbps", 10),
          ("r11x64eq704Kbps", 11),
          ("r12x64eq768Kbps", 12),
          ("r13x64eq832Kbps", 13),
          ("r14x64eq896Kbps", 14),
          ("r15x64eq960Kbps", 15),
          ("r16x64eq1024Kbps", 16),
          ("r17x64eq1088Kbps", 17),
          ("r18x64eq1152Kbps", 18),
          ("r19x64eq1216Kbps", 19),
          ("r20x64eq1280Kbps", 20),
          ("r21x64eq1344Kbps", 21),
          ("r22x64eq1408Kbps", 22),
          ("r23x64eq1472Kbps", 23),
          ("r24x64eq1536Kbps", 24))
    )


_PrtInMbeRate_Type.__name__ = "Integer32"
_PrtInMbeRate_Object = MibTableColumn
prtInMbeRate = _PrtInMbeRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 2, 1, 5),
    _PrtInMbeRate_Type()
)
prtInMbeRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInMbeRate.setStatus("current")


class _PrtInMbeLinkTo_Type(Integer32):
    """Custom type prtInMbeLinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInMbeLinkTo_Type.__name__ = "Integer32"
_PrtInMbeLinkTo_Object = MibTableColumn
prtInMbeLinkTo = _PrtInMbeLinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 11, 2, 1, 6),
    _PrtInMbeLinkTo_Type()
)
prtInMbeLinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInMbeLinkTo.setStatus("deprecated")
_PrtTreCnfg_ObjectIdentity = ObjectIdentity
prtTreCnfg = _PrtTreCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12)
)
_PrtExTreCnfgTable_Object = MibTable
prtExTreCnfgTable = _PrtExTreCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 1)
)
if mibBuilder.loadTexts:
    prtExTreCnfgTable.setStatus("current")
_PrtExTreCnfgEntry_Object = MibTableRow
prtExTreCnfgEntry = _PrtExTreCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 1, 1)
)
prtExTreCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExTreCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExTreSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExTrePrtIdx"),
)
if mibBuilder.loadTexts:
    prtExTreCnfgEntry.setStatus("current")


class _PrtExTreCnfgIdx_Type(Integer32):
    """Custom type prtExTreCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExTreCnfgIdx_Type.__name__ = "Integer32"
_PrtExTreCnfgIdx_Object = MibTableColumn
prtExTreCnfgIdx = _PrtExTreCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 1, 1, 1),
    _PrtExTreCnfgIdx_Type()
)
prtExTreCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTreCnfgIdx.setStatus("current")


class _PrtExTreSltIdx_Type(Integer32):
    """Custom type prtExTreSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExTreSltIdx_Type.__name__ = "Integer32"
_PrtExTreSltIdx_Object = MibTableColumn
prtExTreSltIdx = _PrtExTreSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 1, 1, 2),
    _PrtExTreSltIdx_Type()
)
prtExTreSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTreSltIdx.setStatus("current")


class _PrtExTrePrtIdx_Type(Integer32):
    """Custom type prtExTrePrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exPrt1", 1)
    )


_PrtExTrePrtIdx_Type.__name__ = "Integer32"
_PrtExTrePrtIdx_Object = MibTableColumn
prtExTrePrtIdx = _PrtExTrePrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 1, 1, 3),
    _PrtExTrePrtIdx_Type()
)
prtExTrePrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExTrePrtIdx.setStatus("current")


class _PrtExTreLan_Type(Integer32):
    """Custom type prtExTreLan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remote", 1),
          ("main", 2))
    )


_PrtExTreLan_Type.__name__ = "Integer32"
_PrtExTreLan_Object = MibTableColumn
prtExTreLan = _PrtExTreLan_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 1, 1, 4),
    _PrtExTreLan_Type()
)
prtExTreLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExTreLan.setStatus("current")


class _PrtExTreLanRate_Type(Integer32):
    """Custom type prtExTreLanRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("r4M", 1),
          ("r16M", 2))
    )


_PrtExTreLanRate_Type.__name__ = "Integer32"
_PrtExTreLanRate_Object = MibTableColumn
prtExTreLanRate = _PrtExTreLanRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 1, 1, 5),
    _PrtExTreLanRate_Type()
)
prtExTreLanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExTreLanRate.setStatus("current")
_PrtInTreCnfgTable_Object = MibTable
prtInTreCnfgTable = _PrtInTreCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 2)
)
if mibBuilder.loadTexts:
    prtInTreCnfgTable.setStatus("current")
_PrtInTreCnfgEntry_Object = MibTableRow
prtInTreCnfgEntry = _PrtInTreCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 2, 1)
)
prtInTreCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtInTreCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtInTreSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtInTrePrtIdx"),
)
if mibBuilder.loadTexts:
    prtInTreCnfgEntry.setStatus("current")


class _PrtInTreCnfgIdx_Type(Integer32):
    """Custom type prtInTreCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtInTreCnfgIdx_Type.__name__ = "Integer32"
_PrtInTreCnfgIdx_Object = MibTableColumn
prtInTreCnfgIdx = _PrtInTreCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 2, 1, 1),
    _PrtInTreCnfgIdx_Type()
)
prtInTreCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInTreCnfgIdx.setStatus("current")


class _PrtInTreSltIdx_Type(Integer32):
    """Custom type prtInTreSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInTreSltIdx_Type.__name__ = "Integer32"
_PrtInTreSltIdx_Object = MibTableColumn
prtInTreSltIdx = _PrtInTreSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 2, 1, 2),
    _PrtInTreSltIdx_Type()
)
prtInTreSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInTreSltIdx.setStatus("current")


class _PrtInTrePrtIdx_Type(Integer32):
    """Custom type prtInTrePrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            101
        )
    )
    namedValues = NamedValues(
        ("inPrt1", 101)
    )


_PrtInTrePrtIdx_Type.__name__ = "Integer32"
_PrtInTrePrtIdx_Object = MibTableColumn
prtInTrePrtIdx = _PrtInTrePrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 2, 1, 3),
    _PrtInTrePrtIdx_Type()
)
prtInTrePrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInTrePrtIdx.setStatus("current")


class _PrtInTreConnect_Type(Integer32):
    """Custom type prtInTreConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtInTreConnect_Type.__name__ = "Integer32"
_PrtInTreConnect_Object = MibTableColumn
prtInTreConnect = _PrtInTreConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 2, 1, 4),
    _PrtInTreConnect_Type()
)
prtInTreConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInTreConnect.setStatus("current")


class _PrtInTreRate_Type(Integer32):
    """Custom type prtInTreRate based on Integer32"""
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
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("r1x56eq56Kbps", 1),
          ("r1x64eq64Kbps", 2),
          ("r2x56eq112Kbps", 3),
          ("r2x64eq128Kbps", 4),
          ("r3x56eq168Kbps", 5),
          ("r3x64eq192Kbps", 6),
          ("r4x56eq224Kbps", 7),
          ("r4x64eq256Kbps", 8),
          ("r5x56eq280Kbps", 9),
          ("r5x64eq320Kbps", 10),
          ("r6x56eq336Kbps", 11),
          ("r6x64eq384Kbps", 12),
          ("r7x56eq392Kbps", 13),
          ("r7x64eq448Kbps", 14),
          ("r8x56eq448Kbps", 15),
          ("r8x64eq512Kbps", 16),
          ("r9x56eq504Kbps", 17))
    )


_PrtInTreRate_Type.__name__ = "Integer32"
_PrtInTreRate_Object = MibTableColumn
prtInTreRate = _PrtInTreRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 2, 1, 5),
    _PrtInTreRate_Type()
)
prtInTreRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInTreRate.setStatus("current")


class _PrtInTreLinkTo_Type(Integer32):
    """Custom type prtInTreLinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInTreLinkTo_Type.__name__ = "Integer32"
_PrtInTreLinkTo_Object = MibTableColumn
prtInTreLinkTo = _PrtInTreLinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 12, 2, 1, 6),
    _PrtInTreLinkTo_Type()
)
prtInTreLinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInTreLinkTo.setStatus("deprecated")
_PrtLs6Cnfg_ObjectIdentity = ObjectIdentity
prtLs6Cnfg = _PrtLs6Cnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13)
)
_PrtExLs6CnfgTable_Object = MibTable
prtExLs6CnfgTable = _PrtExLs6CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1)
)
if mibBuilder.loadTexts:
    prtExLs6CnfgTable.setStatus("current")
_PrtExLs6CnfgEntry_Object = MibTableRow
prtExLs6CnfgEntry = _PrtExLs6CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1)
)
prtExLs6CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExLs6CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExLs6SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExLs6PrtIdx"),
)
if mibBuilder.loadTexts:
    prtExLs6CnfgEntry.setStatus("current")


class _PrtExLs6CnfgIdx_Type(Integer32):
    """Custom type prtExLs6CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExLs6CnfgIdx_Type.__name__ = "Integer32"
_PrtExLs6CnfgIdx_Object = MibTableColumn
prtExLs6CnfgIdx = _PrtExLs6CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 1),
    _PrtExLs6CnfgIdx_Type()
)
prtExLs6CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExLs6CnfgIdx.setStatus("current")


class _PrtExLs6SltIdx_Type(Integer32):
    """Custom type prtExLs6SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExLs6SltIdx_Type.__name__ = "Integer32"
_PrtExLs6SltIdx_Object = MibTableColumn
prtExLs6SltIdx = _PrtExLs6SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 2),
    _PrtExLs6SltIdx_Type()
)
prtExLs6SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExLs6SltIdx.setStatus("current")


class _PrtExLs6PrtIdx_Type(Integer32):
    """Custom type prtExLs6PrtIdx based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("exPrt11", 11),
          ("exPrt12", 12))
    )


_PrtExLs6PrtIdx_Type.__name__ = "Integer32"
_PrtExLs6PrtIdx_Object = MibTableColumn
prtExLs6PrtIdx = _PrtExLs6PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 3),
    _PrtExLs6PrtIdx_Type()
)
prtExLs6PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExLs6PrtIdx.setStatus("current")


class _PrtExLs6Connect_Type(Integer32):
    """Custom type prtExLs6Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExLs6Connect_Type.__name__ = "Integer32"
_PrtExLs6Connect_Object = MibTableColumn
prtExLs6Connect = _PrtExLs6Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 4),
    _PrtExLs6Connect_Type()
)
prtExLs6Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6Connect.setStatus("current")


class _PrtExLs6Protocol_Type(Integer32):
    """Custom type prtExLs6Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sync", 2),
          ("async", 3))
    )


_PrtExLs6Protocol_Type.__name__ = "Integer32"
_PrtExLs6Protocol_Object = MibTableColumn
prtExLs6Protocol = _PrtExLs6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 5),
    _PrtExLs6Protocol_Type()
)
prtExLs6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6Protocol.setStatus("current")


class _PrtExLs6Rate_Type(Integer32):
    """Custom type prtExLs6Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("r300bps", 2),
          ("r600bps", 3),
          ("r1200bps", 4),
          ("r2400bps", 5),
          ("r4800bps", 6),
          ("r7200bps", 7),
          ("r8000bps", 8),
          ("r9600bps", 9),
          ("r14400bps", 10),
          ("r16000bps", 11),
          ("r19200bps", 12),
          ("r24000bps", 13),
          ("r28800bps", 14),
          ("r32000bps", 15),
          ("r38400bps", 16),
          ("r48000bps", 17),
          ("r56000bps", 18),
          ("r57600bps", 19),
          ("r64000bps", 20))
    )


_PrtExLs6Rate_Type.__name__ = "Integer32"
_PrtExLs6Rate_Object = MibTableColumn
prtExLs6Rate = _PrtExLs6Rate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 6),
    _PrtExLs6Rate_Type()
)
prtExLs6Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6Rate.setStatus("current")


class _PrtExLs6ClkMode_Type(Integer32):
    """Custom type prtExLs6ClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("extDce", 2),
          ("dte1", 3),
          ("notApplicable", 255))
    )


_PrtExLs6ClkMode_Type.__name__ = "Integer32"
_PrtExLs6ClkMode_Object = MibTableColumn
prtExLs6ClkMode = _PrtExLs6ClkMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 7),
    _PrtExLs6ClkMode_Type()
)
prtExLs6ClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6ClkMode.setStatus("current")


class _PrtExLs6CtrlSignal_Type(Integer32):
    """Custom type prtExLs6CtrlSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("rts", 3),
          ("dtrAndRts", 4))
    )


_PrtExLs6CtrlSignal_Type.__name__ = "Integer32"
_PrtExLs6CtrlSignal_Object = MibTableColumn
prtExLs6CtrlSignal = _PrtExLs6CtrlSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 8),
    _PrtExLs6CtrlSignal_Type()
)
prtExLs6CtrlSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6CtrlSignal.setStatus("current")


class _PrtExLs6DataBits_Type(Integer32):
    """Custom type prtExLs6DataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("d6bits", 1),
          ("d7bits", 2),
          ("d8bits", 3),
          ("d9bits", 4),
          ("notApplicable", 255))
    )


_PrtExLs6DataBits_Type.__name__ = "Integer32"
_PrtExLs6DataBits_Object = MibTableColumn
prtExLs6DataBits = _PrtExLs6DataBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 9),
    _PrtExLs6DataBits_Type()
)
prtExLs6DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6DataBits.setStatus("current")


class _PrtExLs6Cts_Type(Integer32):
    """Custom type prtExLs6Cts based on Integer32"""
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
          ("on", 2),
          ("rts", 3))
    )


_PrtExLs6Cts_Type.__name__ = "Integer32"
_PrtExLs6Cts_Object = MibTableColumn
prtExLs6Cts = _PrtExLs6Cts_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 10),
    _PrtExLs6Cts_Type()
)
prtExLs6Cts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6Cts.setStatus("current")


class _PrtExLs6LinkToInternal_Type(Integer32):
    """Custom type prtExLs6LinkToInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102,
              255)
        )
    )
    namedValues = NamedValues(
        *(("inPrt1", 101),
          ("inPrt2", 102),
          ("notApplicable", 255))
    )


_PrtExLs6LinkToInternal_Type.__name__ = "Integer32"
_PrtExLs6LinkToInternal_Object = MibTableColumn
prtExLs6LinkToInternal = _PrtExLs6LinkToInternal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 1, 1, 11),
    _PrtExLs6LinkToInternal_Type()
)
prtExLs6LinkToInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6LinkToInternal.setStatus("current")
_PrtExLs6VCnfgTable_Object = MibTable
prtExLs6VCnfgTable = _PrtExLs6VCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2)
)
if mibBuilder.loadTexts:
    prtExLs6VCnfgTable.setStatus("current")
_PrtExLs6VCnfgEntry_Object = MibTableRow
prtExLs6VCnfgEntry = _PrtExLs6VCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1)
)
prtExLs6VCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExLs6VCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExLs6VSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExLs6VPrtIdx"),
)
if mibBuilder.loadTexts:
    prtExLs6VCnfgEntry.setStatus("current")


class _PrtExLs6VCnfgIdx_Type(Integer32):
    """Custom type prtExLs6VCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExLs6VCnfgIdx_Type.__name__ = "Integer32"
_PrtExLs6VCnfgIdx_Object = MibTableColumn
prtExLs6VCnfgIdx = _PrtExLs6VCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 1),
    _PrtExLs6VCnfgIdx_Type()
)
prtExLs6VCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExLs6VCnfgIdx.setStatus("current")


class _PrtExLs6VSltIdx_Type(Integer32):
    """Custom type prtExLs6VSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExLs6VSltIdx_Type.__name__ = "Integer32"
_PrtExLs6VSltIdx_Object = MibTableColumn
prtExLs6VSltIdx = _PrtExLs6VSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 2),
    _PrtExLs6VSltIdx_Type()
)
prtExLs6VSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExLs6VSltIdx.setStatus("current")


class _PrtExLs6VPrtIdx_Type(Integer32):
    """Custom type prtExLs6VPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("exPrt7", 7),
          ("exPrt8", 8))
    )


_PrtExLs6VPrtIdx_Type.__name__ = "Integer32"
_PrtExLs6VPrtIdx_Object = MibTableColumn
prtExLs6VPrtIdx = _PrtExLs6VPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 3),
    _PrtExLs6VPrtIdx_Type()
)
prtExLs6VPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExLs6VPrtIdx.setStatus("current")


class _PrtExLs6VConnect_Type(Integer32):
    """Custom type prtExLs6VConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExLs6VConnect_Type.__name__ = "Integer32"
_PrtExLs6VConnect_Object = MibTableColumn
prtExLs6VConnect = _PrtExLs6VConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 4),
    _PrtExLs6VConnect_Type()
)
prtExLs6VConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6VConnect.setStatus("current")


class _PrtExLs6VRate_Type(Integer32):
    """Custom type prtExLs6VRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("r6400bps", 2),
          ("r7200bps", 3),
          ("r8000bps", 4),
          ("r9600bps", 5),
          ("r16000bps", 6),
          ("r24000bps", 7),
          ("r32000bps", 8),
          ("r64000bps", 9))
    )


_PrtExLs6VRate_Type.__name__ = "Integer32"
_PrtExLs6VRate_Object = MibTableColumn
prtExLs6VRate = _PrtExLs6VRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 5),
    _PrtExLs6VRate_Type()
)
prtExLs6VRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6VRate.setStatus("current")


class _PrtExLs6VEchoCanceler_Type(Integer32):
    """Custom type prtExLs6VEchoCanceler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtExLs6VEchoCanceler_Type.__name__ = "Integer32"
_PrtExLs6VEchoCanceler_Object = MibTableColumn
prtExLs6VEchoCanceler = _PrtExLs6VEchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 6),
    _PrtExLs6VEchoCanceler_Type()
)
prtExLs6VEchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6VEchoCanceler.setStatus("current")


class _PrtExLs6VIfType_Type(Integer32):
    """Custom type prtExLs6VIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("w2wire", 1),
          ("w4wire", 2))
    )


_PrtExLs6VIfType_Type.__name__ = "Integer32"
_PrtExLs6VIfType_Object = MibTableColumn
prtExLs6VIfType = _PrtExLs6VIfType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 7),
    _PrtExLs6VIfType_Type()
)
prtExLs6VIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6VIfType.setStatus("current")
_PrtExLs6VTxGain_Type = Integer32
_PrtExLs6VTxGain_Object = MibTableColumn
prtExLs6VTxGain = _PrtExLs6VTxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 8),
    _PrtExLs6VTxGain_Type()
)
prtExLs6VTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6VTxGain.setStatus("current")
_PrtExLs6VRxGain_Type = Integer32
_PrtExLs6VRxGain_Object = MibTableColumn
prtExLs6VRxGain = _PrtExLs6VRxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 9),
    _PrtExLs6VRxGain_Type()
)
prtExLs6VRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6VRxGain.setStatus("current")


class _PrtExLs6VOos_Type(Integer32):
    """Custom type prtExLs6VOos based on Integer32"""
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
        *(("forcedIdle", 1),
          ("forcedBusy", 2),
          ("busyIdle", 3),
          ("idleBusy", 4))
    )


_PrtExLs6VOos_Type.__name__ = "Integer32"
_PrtExLs6VOos_Object = MibTableColumn
prtExLs6VOos = _PrtExLs6VOos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 2, 1, 10),
    _PrtExLs6VOos_Type()
)
prtExLs6VOos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExLs6VOos.setStatus("current")
_PrtInLs6CnfgTable_Object = MibTable
prtInLs6CnfgTable = _PrtInLs6CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3)
)
if mibBuilder.loadTexts:
    prtInLs6CnfgTable.setStatus("current")
_PrtInLs6CnfgEntry_Object = MibTableRow
prtInLs6CnfgEntry = _PrtInLs6CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3, 1)
)
prtInLs6CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtInLs6CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtInLs6SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtInLs6PrtIdx"),
)
if mibBuilder.loadTexts:
    prtInLs6CnfgEntry.setStatus("current")


class _PrtInLs6CnfgIdx_Type(Integer32):
    """Custom type prtInLs6CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtInLs6CnfgIdx_Type.__name__ = "Integer32"
_PrtInLs6CnfgIdx_Object = MibTableColumn
prtInLs6CnfgIdx = _PrtInLs6CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3, 1, 1),
    _PrtInLs6CnfgIdx_Type()
)
prtInLs6CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInLs6CnfgIdx.setStatus("current")


class _PrtInLs6SltIdx_Type(Integer32):
    """Custom type prtInLs6SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInLs6SltIdx_Type.__name__ = "Integer32"
_PrtInLs6SltIdx_Object = MibTableColumn
prtInLs6SltIdx = _PrtInLs6SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3, 1, 2),
    _PrtInLs6SltIdx_Type()
)
prtInLs6SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInLs6SltIdx.setStatus("current")


class _PrtInLs6PrtIdx_Type(Integer32):
    """Custom type prtInLs6PrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("inPrt1", 101),
          ("inPrt2", 102))
    )


_PrtInLs6PrtIdx_Type.__name__ = "Integer32"
_PrtInLs6PrtIdx_Object = MibTableColumn
prtInLs6PrtIdx = _PrtInLs6PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3, 1, 3),
    _PrtInLs6PrtIdx_Type()
)
prtInLs6PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInLs6PrtIdx.setStatus("current")


class _PrtInLs6Connect_Type(Integer32):
    """Custom type prtInLs6Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtInLs6Connect_Type.__name__ = "Integer32"
_PrtInLs6Connect_Object = MibTableColumn
prtInLs6Connect = _PrtInLs6Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3, 1, 4),
    _PrtInLs6Connect_Type()
)
prtInLs6Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs6Connect.setStatus("current")


class _PrtInLs6TandemMode_Type(Integer32):
    """Custom type prtInLs6TandemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTandem", 1),
          ("tandemMaster", 2),
          ("tandemSlave", 3))
    )


_PrtInLs6TandemMode_Type.__name__ = "Integer32"
_PrtInLs6TandemMode_Object = MibTableColumn
prtInLs6TandemMode = _PrtInLs6TandemMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3, 1, 5),
    _PrtInLs6TandemMode_Type()
)
prtInLs6TandemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs6TandemMode.setStatus("current")


class _PrtInLs6Rate_Type(Integer32):
    """Custom type prtInLs6Rate based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("r32Kbps", 1),
          ("r56Kbps", 2),
          ("r64Kpbs", 3),
          ("r128Kbps", 4),
          ("r256Kbps", 5),
          ("r384Kbps", 6),
          ("r192Kbps", 7),
          ("r512Kbps", 8),
          ("r768Kbps", 9),
          ("r14400bps", 10))
    )


_PrtInLs6Rate_Type.__name__ = "Integer32"
_PrtInLs6Rate_Object = MibTableColumn
prtInLs6Rate = _PrtInLs6Rate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3, 1, 6),
    _PrtInLs6Rate_Type()
)
prtInLs6Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs6Rate.setStatus("current")


class _PrtInLs6RemoteType_Type(Integer32):
    """Custom type prtInLs6RemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ls6", 1),
          ("km2kSlave", 2),
          ("km2kStandalone", 3),
          ("notApplicable", 255))
    )


_PrtInLs6RemoteType_Type.__name__ = "Integer32"
_PrtInLs6RemoteType_Object = MibTableColumn
prtInLs6RemoteType = _PrtInLs6RemoteType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3, 1, 7),
    _PrtInLs6RemoteType_Type()
)
prtInLs6RemoteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs6RemoteType.setStatus("current")


class _PrtInLs6LinkTo_Type(Integer32):
    """Custom type prtInLs6LinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtInLs6LinkTo_Type.__name__ = "Integer32"
_PrtInLs6LinkTo_Object = MibTableColumn
prtInLs6LinkTo = _PrtInLs6LinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 13, 3, 1, 8),
    _PrtInLs6LinkTo_Type()
)
prtInLs6LinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInLs6LinkTo.setStatus("deprecated")
_PrtVc3Cnfg_ObjectIdentity = ObjectIdentity
prtVc3Cnfg = _PrtVc3Cnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14)
)
_PrtExVc3CnfgTable_Object = MibTable
prtExVc3CnfgTable = _PrtExVc3CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1)
)
if mibBuilder.loadTexts:
    prtExVc3CnfgTable.setStatus("current")
_PrtExVc3CnfgEntry_Object = MibTableRow
prtExVc3CnfgEntry = _PrtExVc3CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1)
)
prtExVc3CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExVc3CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExVc3SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExVc3PrtIdx"),
)
if mibBuilder.loadTexts:
    prtExVc3CnfgEntry.setStatus("current")


class _PrtExVc3CnfgIdx_Type(Integer32):
    """Custom type prtExVc3CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExVc3CnfgIdx_Type.__name__ = "Integer32"
_PrtExVc3CnfgIdx_Object = MibTableColumn
prtExVc3CnfgIdx = _PrtExVc3CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1, 1),
    _PrtExVc3CnfgIdx_Type()
)
prtExVc3CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVc3CnfgIdx.setStatus("current")


class _PrtExVc3SltIdx_Type(Integer32):
    """Custom type prtExVc3SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExVc3SltIdx_Type.__name__ = "Integer32"
_PrtExVc3SltIdx_Object = MibTableColumn
prtExVc3SltIdx = _PrtExVc3SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1, 2),
    _PrtExVc3SltIdx_Type()
)
prtExVc3SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVc3SltIdx.setStatus("current")


class _PrtExVc3PrtIdx_Type(Integer32):
    """Custom type prtExVc3PrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3))
    )


_PrtExVc3PrtIdx_Type.__name__ = "Integer32"
_PrtExVc3PrtIdx_Object = MibTableColumn
prtExVc3PrtIdx = _PrtExVc3PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1, 3),
    _PrtExVc3PrtIdx_Type()
)
prtExVc3PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVc3PrtIdx.setStatus("current")


class _PrtExVc3Connect_Type(Integer32):
    """Custom type prtExVc3Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExVc3Connect_Type.__name__ = "Integer32"
_PrtExVc3Connect_Object = MibTableColumn
prtExVc3Connect = _PrtExVc3Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1, 4),
    _PrtExVc3Connect_Type()
)
prtExVc3Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc3Connect.setStatus("current")
_PrtExVc3TransGain_Type = Integer32
_PrtExVc3TransGain_Object = MibTableColumn
prtExVc3TransGain = _PrtExVc3TransGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1, 5),
    _PrtExVc3TransGain_Type()
)
prtExVc3TransGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc3TransGain.setStatus("current")
_PrtExVc3ReceiveGain_Type = Integer32
_PrtExVc3ReceiveGain_Object = MibTableColumn
prtExVc3ReceiveGain = _PrtExVc3ReceiveGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1, 6),
    _PrtExVc3ReceiveGain_Type()
)
prtExVc3ReceiveGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc3ReceiveGain.setStatus("current")


class _PrtExVc3Wire_Type(Integer32):
    """Custom type prtExVc3Wire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("w2wire", 1),
          ("w4wire", 2))
    )


_PrtExVc3Wire_Type.__name__ = "Integer32"
_PrtExVc3Wire_Object = MibTableColumn
prtExVc3Wire = _PrtExVc3Wire_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1, 7),
    _PrtExVc3Wire_Type()
)
prtExVc3Wire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc3Wire.setStatus("current")


class _PrtExVc3Rate_Type(Integer32):
    """Custom type prtExVc3Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("r9600bps", 1),
          ("r4800bps", 2))
    )


_PrtExVc3Rate_Type.__name__ = "Integer32"
_PrtExVc3Rate_Object = MibTableColumn
prtExVc3Rate = _PrtExVc3Rate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1, 8),
    _PrtExVc3Rate_Type()
)
prtExVc3Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc3Rate.setStatus("current")


class _PrtExVc3EchoCanceler_Type(Integer32):
    """Custom type prtExVc3EchoCanceler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtExVc3EchoCanceler_Type.__name__ = "Integer32"
_PrtExVc3EchoCanceler_Object = MibTableColumn
prtExVc3EchoCanceler = _PrtExVc3EchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 1, 1, 9),
    _PrtExVc3EchoCanceler_Type()
)
prtExVc3EchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVc3EchoCanceler.setStatus("current")
_PrtInVc3CnfgTable_Object = MibTable
prtInVc3CnfgTable = _PrtInVc3CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 2)
)
if mibBuilder.loadTexts:
    prtInVc3CnfgTable.setStatus("current")
_PrtInVc3CnfgEntry_Object = MibTableRow
prtInVc3CnfgEntry = _PrtInVc3CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 2, 1)
)
prtInVc3CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtInVc3CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtInVc3SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtInVc3PrtIdx"),
)
if mibBuilder.loadTexts:
    prtInVc3CnfgEntry.setStatus("current")


class _PrtInVc3CnfgIdx_Type(Integer32):
    """Custom type prtInVc3CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtInVc3CnfgIdx_Type.__name__ = "Integer32"
_PrtInVc3CnfgIdx_Object = MibTableColumn
prtInVc3CnfgIdx = _PrtInVc3CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 2, 1, 1),
    _PrtInVc3CnfgIdx_Type()
)
prtInVc3CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInVc3CnfgIdx.setStatus("current")


class _PrtInVc3SltIdx_Type(Integer32):
    """Custom type prtInVc3SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInVc3SltIdx_Type.__name__ = "Integer32"
_PrtInVc3SltIdx_Object = MibTableColumn
prtInVc3SltIdx = _PrtInVc3SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 2, 1, 2),
    _PrtInVc3SltIdx_Type()
)
prtInVc3SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInVc3SltIdx.setStatus("current")


class _PrtInVc3PrtIdx_Type(Integer32):
    """Custom type prtInVc3PrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            101
        )
    )
    namedValues = NamedValues(
        ("inPrt1", 101)
    )


_PrtInVc3PrtIdx_Type.__name__ = "Integer32"
_PrtInVc3PrtIdx_Object = MibTableColumn
prtInVc3PrtIdx = _PrtInVc3PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 2, 1, 3),
    _PrtInVc3PrtIdx_Type()
)
prtInVc3PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtInVc3PrtIdx.setStatus("current")


class _PrtInVc3Connect_Type(Integer32):
    """Custom type prtInVc3Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtInVc3Connect_Type.__name__ = "Integer32"
_PrtInVc3Connect_Object = MibTableColumn
prtInVc3Connect = _PrtInVc3Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 2, 1, 4),
    _PrtInVc3Connect_Type()
)
prtInVc3Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInVc3Connect.setStatus("current")


class _PrtInVc3Rate_Type(Integer32):
    """Custom type prtInVc3Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("r32000bps", 1),
          ("r16000bps", 2))
    )


_PrtInVc3Rate_Type.__name__ = "Integer32"
_PrtInVc3Rate_Object = MibTableColumn
prtInVc3Rate = _PrtInVc3Rate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 2, 1, 5),
    _PrtInVc3Rate_Type()
)
prtInVc3Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInVc3Rate.setStatus("current")


class _PrtInVc3Oos_Type(Integer32):
    """Custom type prtInVc3Oos based on Integer32"""
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
        *(("forcedIdle", 1),
          ("forcedBusy", 2),
          ("busyIdle", 3),
          ("idleBusy", 4))
    )


_PrtInVc3Oos_Type.__name__ = "Integer32"
_PrtInVc3Oos_Object = MibTableColumn
prtInVc3Oos = _PrtInVc3Oos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 2, 1, 6),
    _PrtInVc3Oos_Type()
)
prtInVc3Oos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInVc3Oos.setStatus("current")


class _PrtInVc3LinkTo_Type(Integer32):
    """Custom type prtInVc3LinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtInVc3LinkTo_Type.__name__ = "Integer32"
_PrtInVc3LinkTo_Object = MibTableColumn
prtInVc3LinkTo = _PrtInVc3LinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 14, 2, 1, 7),
    _PrtInVc3LinkTo_Type()
)
prtInVc3LinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInVc3LinkTo.setStatus("deprecated")
_PrtVcPbxCnfg_ObjectIdentity = ObjectIdentity
prtVcPbxCnfg = _PrtVcPbxCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15)
)
_PrtExVcPbxCnfgTable_Object = MibTable
prtExVcPbxCnfgTable = _PrtExVcPbxCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1)
)
if mibBuilder.loadTexts:
    prtExVcPbxCnfgTable.setStatus("current")
_PrtExVcPbxCnfgEntry_Object = MibTableRow
prtExVcPbxCnfgEntry = _PrtExVcPbxCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1)
)
prtExVcPbxCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExVcPbxCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExVcPbxSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExVcPbxPrtIdx"),
)
if mibBuilder.loadTexts:
    prtExVcPbxCnfgEntry.setStatus("current")


class _PrtExVcPbxCnfgIdx_Type(Integer32):
    """Custom type prtExVcPbxCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExVcPbxCnfgIdx_Type.__name__ = "Integer32"
_PrtExVcPbxCnfgIdx_Object = MibTableColumn
prtExVcPbxCnfgIdx = _PrtExVcPbxCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 1),
    _PrtExVcPbxCnfgIdx_Type()
)
prtExVcPbxCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVcPbxCnfgIdx.setStatus("current")


class _PrtExVcPbxSltIdx_Type(Integer32):
    """Custom type prtExVcPbxSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExVcPbxSltIdx_Type.__name__ = "Integer32"
_PrtExVcPbxSltIdx_Object = MibTableColumn
prtExVcPbxSltIdx = _PrtExVcPbxSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 2),
    _PrtExVcPbxSltIdx_Type()
)
prtExVcPbxSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVcPbxSltIdx.setStatus("current")


class _PrtExVcPbxPrtIdx_Type(Integer32):
    """Custom type prtExVcPbxPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exPrt1", 1)
    )


_PrtExVcPbxPrtIdx_Type.__name__ = "Integer32"
_PrtExVcPbxPrtIdx_Object = MibTableColumn
prtExVcPbxPrtIdx = _PrtExVcPbxPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 3),
    _PrtExVcPbxPrtIdx_Type()
)
prtExVcPbxPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVcPbxPrtIdx.setStatus("current")


class _PrtExVcPbxConnect_Type(Integer32):
    """Custom type prtExVcPbxConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtExVcPbxConnect_Type.__name__ = "Integer32"
_PrtExVcPbxConnect_Object = MibTableColumn
prtExVcPbxConnect = _PrtExVcPbxConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 4),
    _PrtExVcPbxConnect_Type()
)
prtExVcPbxConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxConnect.setStatus("current")


class _PrtExVcPbxGroup_Type(Integer32):
    """Custom type prtExVcPbxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExVcPbxGroup_Type.__name__ = "Integer32"
_PrtExVcPbxGroup_Object = MibTableColumn
prtExVcPbxGroup = _PrtExVcPbxGroup_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 5),
    _PrtExVcPbxGroup_Type()
)
prtExVcPbxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVcPbxGroup.setStatus("current")


class _PrtExVcPbxTransparent_Type(Integer32):
    """Custom type prtExVcPbxTransparent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3),
          ("notApplicable", 255))
    )


_PrtExVcPbxTransparent_Type.__name__ = "Integer32"
_PrtExVcPbxTransparent_Object = MibTableColumn
prtExVcPbxTransparent = _PrtExVcPbxTransparent_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 6),
    _PrtExVcPbxTransparent_Type()
)
prtExVcPbxTransparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTransparent.setStatus("current")
_PrtExVcPbxTransSignalTs_Type = Integer32
_PrtExVcPbxTransSignalTs_Object = MibTableColumn
prtExVcPbxTransSignalTs = _PrtExVcPbxTransSignalTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 7),
    _PrtExVcPbxTransSignalTs_Type()
)
prtExVcPbxTransSignalTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTransSignalTs.setStatus("current")


class _PrtExVcPbxFrame_Type(Integer32):
    """Custom type prtExVcPbxFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("esfT1", 2),
          ("sfT1", 3),
          ("g732nE1", 4),
          ("g732nE1CRC", 5),
          ("g732sE1", 6),
          ("g732sE1CRC", 7),
          ("notApplicable", 255))
    )


_PrtExVcPbxFrame_Type.__name__ = "Integer32"
_PrtExVcPbxFrame_Object = MibTableColumn
prtExVcPbxFrame = _PrtExVcPbxFrame_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 8),
    _PrtExVcPbxFrame_Type()
)
prtExVcPbxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxFrame.setStatus("current")


class _PrtExVcPbxRestoreTime_Type(Integer32):
    """Custom type prtExVcPbxRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("restoreT1secFast", 2),
          ("restoreT10sec62411", 3),
          ("ccittE1", 4),
          ("notApplicable", 255))
    )


_PrtExVcPbxRestoreTime_Type.__name__ = "Integer32"
_PrtExVcPbxRestoreTime_Object = MibTableColumn
prtExVcPbxRestoreTime = _PrtExVcPbxRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 9),
    _PrtExVcPbxRestoreTime_Type()
)
prtExVcPbxRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxRestoreTime.setStatus("current")


class _PrtExVcPbxLineCode_Type(Integer32):
    """Custom type prtExVcPbxLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("b7zsT1", 1),
          ("b8zsT1", 2),
          ("transT1", 3),
          ("hdb3E1", 4),
          ("notApplicable", 255))
    )


_PrtExVcPbxLineCode_Type.__name__ = "Integer32"
_PrtExVcPbxLineCode_Object = MibTableColumn
prtExVcPbxLineCode = _PrtExVcPbxLineCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 10),
    _PrtExVcPbxLineCode_Type()
)
prtExVcPbxLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxLineCode.setStatus("current")


class _PrtExVcPbxLineLength_Type(Integer32):
    """Custom type prtExVcPbxLineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("len0p133ft", 2),
          ("len134p266ft", 3),
          ("len267p399ft", 4),
          ("len400p533ft", 5),
          ("len534p655ft", 6),
          ("notApplicable", 255))
    )


_PrtExVcPbxLineLength_Type.__name__ = "Integer32"
_PrtExVcPbxLineLength_Object = MibTableColumn
prtExVcPbxLineLength = _PrtExVcPbxLineLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 11),
    _PrtExVcPbxLineLength_Type()
)
prtExVcPbxLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxLineLength.setStatus("current")


class _PrtExVcPbxLinkTo_Type(Integer32):
    """Custom type prtExVcPbxLinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtExVcPbxLinkTo_Type.__name__ = "Integer32"
_PrtExVcPbxLinkTo_Object = MibTableColumn
prtExVcPbxLinkTo = _PrtExVcPbxLinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 12),
    _PrtExVcPbxLinkTo_Type()
)
prtExVcPbxLinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxLinkTo.setStatus("deprecated")


class _PrtExVcPbxSignalOper_Type(Integer32):
    """Custom type prtExVcPbxSignalOper based on Integer32"""
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
        *(("notApplicable", 1),
          ("normal", 2),
          ("bEqA", 3),
          ("inverseA", 4))
    )


_PrtExVcPbxSignalOper_Type.__name__ = "Integer32"
_PrtExVcPbxSignalOper_Object = MibTableColumn
prtExVcPbxSignalOper = _PrtExVcPbxSignalOper_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 13),
    _PrtExVcPbxSignalOper_Type()
)
prtExVcPbxSignalOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxSignalOper.setStatus("current")


class _PrtExVcPbxIdleCode_Type(Integer32):
    """Custom type prtExVcPbxIdleCode based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("hff", 2),
          ("he4", 3),
          ("hd5", 4),
          ("h9e", 5),
          ("h98", 6),
          ("h7f", 7),
          ("h7e", 8),
          ("h54", 9),
          ("h1a", 10))
    )


_PrtExVcPbxIdleCode_Type.__name__ = "Integer32"
_PrtExVcPbxIdleCode_Object = MibTableColumn
prtExVcPbxIdleCode = _PrtExVcPbxIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 1, 1, 14),
    _PrtExVcPbxIdleCode_Type()
)
prtExVcPbxIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxIdleCode.setStatus("current")
_PrtIn1p6VcPbxCnfgTable_Object = MibTable
prtIn1p6VcPbxCnfgTable = _PrtIn1p6VcPbxCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 2)
)
if mibBuilder.loadTexts:
    prtIn1p6VcPbxCnfgTable.setStatus("current")
_PrtIn1p6VcPbxCnfgEntry_Object = MibTableRow
prtIn1p6VcPbxCnfgEntry = _PrtIn1p6VcPbxCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 2, 1)
)
prtIn1p6VcPbxCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtIn1p6VcPbxCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtIn1p6VcPbxSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtIn1p6VcPbxPrtIdx"),
)
if mibBuilder.loadTexts:
    prtIn1p6VcPbxCnfgEntry.setStatus("current")


class _PrtIn1p6VcPbxCnfgIdx_Type(Integer32):
    """Custom type prtIn1p6VcPbxCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtIn1p6VcPbxCnfgIdx_Type.__name__ = "Integer32"
_PrtIn1p6VcPbxCnfgIdx_Object = MibTableColumn
prtIn1p6VcPbxCnfgIdx = _PrtIn1p6VcPbxCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 2, 1, 1),
    _PrtIn1p6VcPbxCnfgIdx_Type()
)
prtIn1p6VcPbxCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIn1p6VcPbxCnfgIdx.setStatus("current")


class _PrtIn1p6VcPbxSltIdx_Type(Integer32):
    """Custom type prtIn1p6VcPbxSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtIn1p6VcPbxSltIdx_Type.__name__ = "Integer32"
_PrtIn1p6VcPbxSltIdx_Object = MibTableColumn
prtIn1p6VcPbxSltIdx = _PrtIn1p6VcPbxSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 2, 1, 2),
    _PrtIn1p6VcPbxSltIdx_Type()
)
prtIn1p6VcPbxSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIn1p6VcPbxSltIdx.setStatus("current")


class _PrtIn1p6VcPbxPrtIdx_Type(Integer32):
    """Custom type prtIn1p6VcPbxPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102,
              103,
              104,
              105,
              106)
        )
    )
    namedValues = NamedValues(
        *(("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106))
    )


_PrtIn1p6VcPbxPrtIdx_Type.__name__ = "Integer32"
_PrtIn1p6VcPbxPrtIdx_Object = MibTableColumn
prtIn1p6VcPbxPrtIdx = _PrtIn1p6VcPbxPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 2, 1, 3),
    _PrtIn1p6VcPbxPrtIdx_Type()
)
prtIn1p6VcPbxPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIn1p6VcPbxPrtIdx.setStatus("current")


class _PrtIn1p6VcPbxConnect_Type(Integer32):
    """Custom type prtIn1p6VcPbxConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtIn1p6VcPbxConnect_Type.__name__ = "Integer32"
_PrtIn1p6VcPbxConnect_Object = MibTableColumn
prtIn1p6VcPbxConnect = _PrtIn1p6VcPbxConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 2, 1, 4),
    _PrtIn1p6VcPbxConnect_Type()
)
prtIn1p6VcPbxConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIn1p6VcPbxConnect.setStatus("current")


class _PrtIn1p6VcPbxRate_Type(Integer32):
    """Custom type prtIn1p6VcPbxRate based on Integer32"""
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
        *(("r4800bps", 1),
          ("r6400bps", 2),
          ("r7200bps", 3),
          ("r8000bps", 4),
          ("r9600bps", 5),
          ("r12800bps", 6))
    )


_PrtIn1p6VcPbxRate_Type.__name__ = "Integer32"
_PrtIn1p6VcPbxRate_Object = MibTableColumn
prtIn1p6VcPbxRate = _PrtIn1p6VcPbxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 2, 1, 5),
    _PrtIn1p6VcPbxRate_Type()
)
prtIn1p6VcPbxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIn1p6VcPbxRate.setStatus("current")


class _PrtIn1p6VcPbxEchoCanceler_Type(Integer32):
    """Custom type prtIn1p6VcPbxEchoCanceler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_PrtIn1p6VcPbxEchoCanceler_Type.__name__ = "Integer32"
_PrtIn1p6VcPbxEchoCanceler_Object = MibTableColumn
prtIn1p6VcPbxEchoCanceler = _PrtIn1p6VcPbxEchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 2, 1, 6),
    _PrtIn1p6VcPbxEchoCanceler_Type()
)
prtIn1p6VcPbxEchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIn1p6VcPbxEchoCanceler.setStatus("current")


class _PrtIn1p6VcPbxPabxTs_Type(Integer32):
    """Custom type prtIn1p6VcPbxPabxTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PrtIn1p6VcPbxPabxTs_Type.__name__ = "Integer32"
_PrtIn1p6VcPbxPabxTs_Object = MibTableColumn
prtIn1p6VcPbxPabxTs = _PrtIn1p6VcPbxPabxTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 2, 1, 7),
    _PrtIn1p6VcPbxPabxTs_Type()
)
prtIn1p6VcPbxPabxTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIn1p6VcPbxPabxTs.setStatus("current")
_PrtIn7p8VcPbxCnfgTable_Object = MibTable
prtIn7p8VcPbxCnfgTable = _PrtIn7p8VcPbxCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3)
)
if mibBuilder.loadTexts:
    prtIn7p8VcPbxCnfgTable.setStatus("current")
_PrtIn7p8VcPbxCnfgEntry_Object = MibTableRow
prtIn7p8VcPbxCnfgEntry = _PrtIn7p8VcPbxCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1)
)
prtIn7p8VcPbxCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtIn7p8VcPbxCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtIn7p8VcPbxSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtIn7p8VcPbxPrtIdx"),
)
if mibBuilder.loadTexts:
    prtIn7p8VcPbxCnfgEntry.setStatus("current")


class _PrtIn7p8VcPbxCnfgIdx_Type(Integer32):
    """Custom type prtIn7p8VcPbxCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtIn7p8VcPbxCnfgIdx_Type.__name__ = "Integer32"
_PrtIn7p8VcPbxCnfgIdx_Object = MibTableColumn
prtIn7p8VcPbxCnfgIdx = _PrtIn7p8VcPbxCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1, 1),
    _PrtIn7p8VcPbxCnfgIdx_Type()
)
prtIn7p8VcPbxCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIn7p8VcPbxCnfgIdx.setStatus("current")


class _PrtIn7p8VcPbxSltIdx_Type(Integer32):
    """Custom type prtIn7p8VcPbxSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtIn7p8VcPbxSltIdx_Type.__name__ = "Integer32"
_PrtIn7p8VcPbxSltIdx_Object = MibTableColumn
prtIn7p8VcPbxSltIdx = _PrtIn7p8VcPbxSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1, 2),
    _PrtIn7p8VcPbxSltIdx_Type()
)
prtIn7p8VcPbxSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIn7p8VcPbxSltIdx.setStatus("current")


class _PrtIn7p8VcPbxPrtIdx_Type(Integer32):
    """Custom type prtIn7p8VcPbxPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(107,
              108)
        )
    )
    namedValues = NamedValues(
        *(("inPrt7", 107),
          ("inPrt8", 108))
    )


_PrtIn7p8VcPbxPrtIdx_Type.__name__ = "Integer32"
_PrtIn7p8VcPbxPrtIdx_Object = MibTableColumn
prtIn7p8VcPbxPrtIdx = _PrtIn7p8VcPbxPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1, 3),
    _PrtIn7p8VcPbxPrtIdx_Type()
)
prtIn7p8VcPbxPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIn7p8VcPbxPrtIdx.setStatus("current")


class _PrtIn7p8VcPbxConnect_Type(Integer32):
    """Custom type prtIn7p8VcPbxConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtIn7p8VcPbxConnect_Type.__name__ = "Integer32"
_PrtIn7p8VcPbxConnect_Object = MibTableColumn
prtIn7p8VcPbxConnect = _PrtIn7p8VcPbxConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1, 4),
    _PrtIn7p8VcPbxConnect_Type()
)
prtIn7p8VcPbxConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIn7p8VcPbxConnect.setStatus("current")


class _PrtIn7p8VcPbxMode_Type(Integer32):
    """Custom type prtIn7p8VcPbxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("server", 2))
    )


_PrtIn7p8VcPbxMode_Type.__name__ = "Integer32"
_PrtIn7p8VcPbxMode_Object = MibTableColumn
prtIn7p8VcPbxMode = _PrtIn7p8VcPbxMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1, 5),
    _PrtIn7p8VcPbxMode_Type()
)
prtIn7p8VcPbxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIn7p8VcPbxMode.setStatus("current")


class _PrtIn7p8VcPbxRate_Type(Integer32):
    """Custom type prtIn7p8VcPbxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("r32Kbps", 1),
          ("r16Kbps", 2),
          ("notApplicable", 255))
    )


_PrtIn7p8VcPbxRate_Type.__name__ = "Integer32"
_PrtIn7p8VcPbxRate_Object = MibTableColumn
prtIn7p8VcPbxRate = _PrtIn7p8VcPbxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1, 6),
    _PrtIn7p8VcPbxRate_Type()
)
prtIn7p8VcPbxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIn7p8VcPbxRate.setStatus("current")


class _PrtIn7p8VcPbxSignalMode_Type(Integer32):
    """Custom type prtIn7p8VcPbxSignalMode based on Integer32"""
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
        *(("none", 1),
          ("aBit", 2),
          ("abcBit", 3),
          ("abcdBit", 4))
    )


_PrtIn7p8VcPbxSignalMode_Type.__name__ = "Integer32"
_PrtIn7p8VcPbxSignalMode_Object = MibTableColumn
prtIn7p8VcPbxSignalMode = _PrtIn7p8VcPbxSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1, 7),
    _PrtIn7p8VcPbxSignalMode_Type()
)
prtIn7p8VcPbxSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIn7p8VcPbxSignalMode.setStatus("current")


class _PrtIn7p8VcPbxOos_Type(Integer32):
    """Custom type prtIn7p8VcPbxOos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedIdle", 1),
          ("forcedBusy", 2))
    )


_PrtIn7p8VcPbxOos_Type.__name__ = "Integer32"
_PrtIn7p8VcPbxOos_Object = MibTableColumn
prtIn7p8VcPbxOos = _PrtIn7p8VcPbxOos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1, 8),
    _PrtIn7p8VcPbxOos_Type()
)
prtIn7p8VcPbxOos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIn7p8VcPbxOos.setStatus("current")


class _PrtIn7p8VcPbxLinkTo_Type(Integer32):
    """Custom type prtIn7p8VcPbxLinkTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtIn7p8VcPbxLinkTo_Type.__name__ = "Integer32"
_PrtIn7p8VcPbxLinkTo_Object = MibTableColumn
prtIn7p8VcPbxLinkTo = _PrtIn7p8VcPbxLinkTo_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 3, 1, 9),
    _PrtIn7p8VcPbxLinkTo_Type()
)
prtIn7p8VcPbxLinkTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIn7p8VcPbxLinkTo.setStatus("deprecated")
_PrtExVcPbxTsTable_Object = MibTable
prtExVcPbxTsTable = _PrtExVcPbxTsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4)
)
if mibBuilder.loadTexts:
    prtExVcPbxTsTable.setStatus("current")
_PrtExVcPbxTsEntry_Object = MibTableRow
prtExVcPbxTsEntry = _PrtExVcPbxTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1)
)
prtExVcPbxTsEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtExVcPbxTsCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtExVcPbxTsSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtExVcPbxTsPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtExVcPbxTsIdx"),
)
if mibBuilder.loadTexts:
    prtExVcPbxTsEntry.setStatus("current")


class _PrtExVcPbxTsCnfgIdx_Type(Integer32):
    """Custom type prtExVcPbxTsCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExVcPbxTsCnfgIdx_Type.__name__ = "Integer32"
_PrtExVcPbxTsCnfgIdx_Object = MibTableColumn
prtExVcPbxTsCnfgIdx = _PrtExVcPbxTsCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 1),
    _PrtExVcPbxTsCnfgIdx_Type()
)
prtExVcPbxTsCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVcPbxTsCnfgIdx.setStatus("current")


class _PrtExVcPbxTsSltIdx_Type(Integer32):
    """Custom type prtExVcPbxTsSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExVcPbxTsSltIdx_Type.__name__ = "Integer32"
_PrtExVcPbxTsSltIdx_Object = MibTableColumn
prtExVcPbxTsSltIdx = _PrtExVcPbxTsSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 2),
    _PrtExVcPbxTsSltIdx_Type()
)
prtExVcPbxTsSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVcPbxTsSltIdx.setStatus("current")


class _PrtExVcPbxTsPrtIdx_Type(Integer32):
    """Custom type prtExVcPbxTsPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              109,
              110)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("inPrt9", 109),
          ("inPrt10", 110))
    )


_PrtExVcPbxTsPrtIdx_Type.__name__ = "Integer32"
_PrtExVcPbxTsPrtIdx_Object = MibTableColumn
prtExVcPbxTsPrtIdx = _PrtExVcPbxTsPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 3),
    _PrtExVcPbxTsPrtIdx_Type()
)
prtExVcPbxTsPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVcPbxTsPrtIdx.setStatus("current")
_PrtExVcPbxTsIdx_Type = Integer32
_PrtExVcPbxTsIdx_Object = MibTableColumn
prtExVcPbxTsIdx = _PrtExVcPbxTsIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 4),
    _PrtExVcPbxTsIdx_Type()
)
prtExVcPbxTsIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtExVcPbxTsIdx.setStatus("current")


class _PrtExVcPbxTsMode_Type(Integer32):
    """Custom type prtExVcPbxTsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("compressed", 2),
          ("transparent", 3),
          ("compressedCcs", 4),
          ("mng", 5),
          ("ccs1", 11),
          ("ccs2", 12),
          ("ccs3", 13),
          ("ccs4", 14),
          ("ccs5", 15),
          ("ccs6", 16),
          ("ccs7", 17),
          ("ccs8", 18),
          ("ss7n1", 41),
          ("ss7n2", 42),
          ("ss7n3", 43),
          ("ss7n4", 44),
          ("ss7n5", 45),
          ("ss7n6", 46),
          ("ss7n7", 47),
          ("ss7n8", 48))
    )


_PrtExVcPbxTsMode_Type.__name__ = "Integer32"
_PrtExVcPbxTsMode_Object = MibTableColumn
prtExVcPbxTsMode = _PrtExVcPbxTsMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 5),
    _PrtExVcPbxTsMode_Type()
)
prtExVcPbxTsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTsMode.setStatus("current")


class _PrtExVcPbxTsIConSlot_Type(Integer32):
    """Custom type prtExVcPbxTsIConSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExVcPbxTsIConSlot_Type.__name__ = "Integer32"
_PrtExVcPbxTsIConSlot_Object = MibTableColumn
prtExVcPbxTsIConSlot = _PrtExVcPbxTsIConSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 6),
    _PrtExVcPbxTsIConSlot_Type()
)
prtExVcPbxTsIConSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTsIConSlot.setStatus("current")


class _PrtExVcPbxTsIConPrt_Type(Integer32):
    """Custom type prtExVcPbxTsIConPrt based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("noConnect", 100),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108))
    )


_PrtExVcPbxTsIConPrt_Type.__name__ = "Integer32"
_PrtExVcPbxTsIConPrt_Object = MibTableColumn
prtExVcPbxTsIConPrt = _PrtExVcPbxTsIConPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 7),
    _PrtExVcPbxTsIConPrt_Type()
)
prtExVcPbxTsIConPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTsIConPrt.setStatus("current")


class _PrtExVcPbxTsIConTs_Type(Integer32):
    """Custom type prtExVcPbxTsIConTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtExVcPbxTsIConTs_Type.__name__ = "Integer32"
_PrtExVcPbxTsIConTs_Object = MibTableColumn
prtExVcPbxTsIConTs = _PrtExVcPbxTsIConTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 8),
    _PrtExVcPbxTsIConTs_Type()
)
prtExVcPbxTsIConTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTsIConTs.setStatus("current")


class _PrtExVcPbxTsRemPrt_Type(Integer32):
    """Custom type prtExVcPbxTsRemPrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("noConnect", 100))
    )


_PrtExVcPbxTsRemPrt_Type.__name__ = "Integer32"
_PrtExVcPbxTsRemPrt_Object = MibTableColumn
prtExVcPbxTsRemPrt = _PrtExVcPbxTsRemPrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 9),
    _PrtExVcPbxTsRemPrt_Type()
)
prtExVcPbxTsRemPrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTsRemPrt.setStatus("current")
_PrtExVcPbxTsRemTs_Type = Integer32
_PrtExVcPbxTsRemTs_Object = MibTableColumn
prtExVcPbxTsRemTs = _PrtExVcPbxTsRemTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 10),
    _PrtExVcPbxTsRemTs_Type()
)
prtExVcPbxTsRemTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTsRemTs.setStatus("current")
_PrtExVcPbxTsRemConnID_Type = Unsigned32
_PrtExVcPbxTsRemConnID_Object = MibTableColumn
prtExVcPbxTsRemConnID = _PrtExVcPbxTsRemConnID_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 11),
    _PrtExVcPbxTsRemConnID_Type()
)
prtExVcPbxTsRemConnID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTsRemConnID.setStatus("current")


class _PrtExVcPbxTsSourceSlot_Type(Integer32):
    """Custom type prtExVcPbxTsSourceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtExVcPbxTsSourceSlot_Type.__name__ = "Integer32"
_PrtExVcPbxTsSourceSlot_Object = MibTableColumn
prtExVcPbxTsSourceSlot = _PrtExVcPbxTsSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 12),
    _PrtExVcPbxTsSourceSlot_Type()
)
prtExVcPbxTsSourceSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTsSourceSlot.setStatus("current")
_PrtExVcPbxTsSourcePrt_Type = Unsigned32
_PrtExVcPbxTsSourcePrt_Object = MibTableColumn
prtExVcPbxTsSourcePrt = _PrtExVcPbxTsSourcePrt_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 15, 4, 1, 13),
    _PrtExVcPbxTsSourcePrt_Type()
)
prtExVcPbxTsSourcePrt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtExVcPbxTsSourcePrt.setStatus("current")
_PrtIsdnCnfg_ObjectIdentity = ObjectIdentity
prtIsdnCnfg = _PrtIsdnCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16)
)
_PrtIsdnCnfgTable_Object = MibTable
prtIsdnCnfgTable = _PrtIsdnCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1)
)
if mibBuilder.loadTexts:
    prtIsdnCnfgTable.setStatus("current")
_PrtIsdnCnfgEntry_Object = MibTableRow
prtIsdnCnfgEntry = _PrtIsdnCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1)
)
prtIsdnCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtIsdnCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtIsdnSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtIsdnPrtIdx"),
)
if mibBuilder.loadTexts:
    prtIsdnCnfgEntry.setStatus("current")


class _PrtIsdnCnfgIdx_Type(Integer32):
    """Custom type prtIsdnCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtIsdnCnfgIdx_Type.__name__ = "Integer32"
_PrtIsdnCnfgIdx_Object = MibTableColumn
prtIsdnCnfgIdx = _PrtIsdnCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 1),
    _PrtIsdnCnfgIdx_Type()
)
prtIsdnCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnCnfgIdx.setStatus("current")


class _PrtIsdnSltIdx_Type(Integer32):
    """Custom type prtIsdnSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              103,
              104,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("kmxMlA", 103),
          ("kmxMlB", 104),
          ("notApplicable", 255))
    )


_PrtIsdnSltIdx_Type.__name__ = "Integer32"
_PrtIsdnSltIdx_Object = MibTableColumn
prtIsdnSltIdx = _PrtIsdnSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 2),
    _PrtIsdnSltIdx_Type()
)
prtIsdnSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnSltIdx.setStatus("current")
_PrtIsdnPrtIdx_Type = Integer32
_PrtIsdnPrtIdx_Object = MibTableColumn
prtIsdnPrtIdx = _PrtIsdnPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 3),
    _PrtIsdnPrtIdx_Type()
)
prtIsdnPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnPrtIdx.setStatus("current")


class _PrtIsdnConnect_Type(Integer32):
    """Custom type prtIsdnConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtIsdnConnect_Type.__name__ = "Integer32"
_PrtIsdnConnect_Object = MibTableColumn
prtIsdnConnect = _PrtIsdnConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 4),
    _PrtIsdnConnect_Type()
)
prtIsdnConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnConnect.setStatus("current")


class _PrtIsdnSignalingProtocol_Type(Integer32):
    """Custom type prtIsdnSignalingProtocol based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              7,
              9,
              10,
              17,
              18,
              21,
              255)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("etsi", 3),
          ("ess4", 5),
          ("ess5", 6),
          ("dms100", 7),
          ("ni1", 9),
          ("ni2", 10),
          ("ins64", 17),
          ("ins1500", 18),
          ("qsig", 21),
          ("notApplicable", 255))
    )


_PrtIsdnSignalingProtocol_Type.__name__ = "Integer32"
_PrtIsdnSignalingProtocol_Object = MibTableColumn
prtIsdnSignalingProtocol = _PrtIsdnSignalingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 5),
    _PrtIsdnSignalingProtocol_Type()
)
prtIsdnSignalingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnSignalingProtocol.setStatus("current")


class _PrtIsdnBasicRateLineTopology_Type(Integer32):
    """Custom type prtIsdnBasicRateLineTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 1),
          ("pointToMultipoint", 2),
          ("notApplicable", 255))
    )


_PrtIsdnBasicRateLineTopology_Type.__name__ = "Integer32"
_PrtIsdnBasicRateLineTopology_Object = MibTableColumn
prtIsdnBasicRateLineTopology = _PrtIsdnBasicRateLineTopology_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 6),
    _PrtIsdnBasicRateLineTopology_Type()
)
prtIsdnBasicRateLineTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnBasicRateLineTopology.setStatus("current")


class _PrtIsdnMode_Type(Integer32):
    """Custom type prtIsdnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dialup", 1),
          ("leased", 2),
          ("syncLeased", 3),
          ("notApplicable", 255))
    )


_PrtIsdnMode_Type.__name__ = "Integer32"
_PrtIsdnMode_Object = MibTableColumn
prtIsdnMode = _PrtIsdnMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 7),
    _PrtIsdnMode_Type()
)
prtIsdnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnMode.setStatus("current")


class _PrtIsdnFilter_Type(Integer32):
    """Custom type prtIsdnFilter based on Integer32"""
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
        *(("notApplicable", 1),
          ("answerAll", 2),
          ("rejectAll", 3),
          ("selective", 4),
          ("callBack", 5))
    )


_PrtIsdnFilter_Type.__name__ = "Integer32"
_PrtIsdnFilter_Object = MibTableColumn
prtIsdnFilter = _PrtIsdnFilter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 8),
    _PrtIsdnFilter_Type()
)
prtIsdnFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnFilter.setStatus("current")


class _PrtIsdnSimultaneousCall_Type(Integer32):
    """Custom type prtIsdnSimultaneousCall based on Integer32"""
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
          ("accept", 2),
          ("reject", 3))
    )


_PrtIsdnSimultaneousCall_Type.__name__ = "Integer32"
_PrtIsdnSimultaneousCall_Object = MibTableColumn
prtIsdnSimultaneousCall = _PrtIsdnSimultaneousCall_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 9),
    _PrtIsdnSimultaneousCall_Type()
)
prtIsdnSimultaneousCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnSimultaneousCall.setStatus("current")
_PrtIsdnNumOfAbstractTerm_Type = Integer32
_PrtIsdnNumOfAbstractTerm_Object = MibTableColumn
prtIsdnNumOfAbstractTerm = _PrtIsdnNumOfAbstractTerm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 10),
    _PrtIsdnNumOfAbstractTerm_Type()
)
prtIsdnNumOfAbstractTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnNumOfAbstractTerm.setStatus("current")


class _PrtIsdnSwitchMode_Type(Integer32):
    """Custom type prtIsdnSwitchMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("auto", 2),
          ("manual", 3),
          ("connect", 4))
    )


_PrtIsdnSwitchMode_Type.__name__ = "Integer32"
_PrtIsdnSwitchMode_Object = MibTableColumn
prtIsdnSwitchMode = _PrtIsdnSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 11),
    _PrtIsdnSwitchMode_Type()
)
prtIsdnSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnSwitchMode.setStatus("current")


class _PrtIsdnAbSide_Type(Integer32):
    """Custom type prtIsdnAbSide based on Integer32"""
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
          ("aSide", 2),
          ("bSide", 3))
    )


_PrtIsdnAbSide_Type.__name__ = "Integer32"
_PrtIsdnAbSide_Object = MibTableColumn
prtIsdnAbSide = _PrtIsdnAbSide_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 12),
    _PrtIsdnAbSide_Type()
)
prtIsdnAbSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnAbSide.setStatus("current")


class _PrtIsdnQsigRole_Type(Integer32):
    """Custom type prtIsdnQsigRole based on Integer32"""
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
          ("slave", 2),
          ("master", 3))
    )


_PrtIsdnQsigRole_Type.__name__ = "Integer32"
_PrtIsdnQsigRole_Object = MibTableColumn
prtIsdnQsigRole = _PrtIsdnQsigRole_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 13),
    _PrtIsdnQsigRole_Type()
)
prtIsdnQsigRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnQsigRole.setStatus("current")


class _PrtIsdnInterface_Type(Integer32):
    """Custom type prtIsdnInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("lt", 1),
          ("nt", 2),
          ("te", 3),
          ("notApplicable", 255))
    )


_PrtIsdnInterface_Type.__name__ = "Integer32"
_PrtIsdnInterface_Object = MibTableColumn
prtIsdnInterface = _PrtIsdnInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 14),
    _PrtIsdnInterface_Type()
)
prtIsdnInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnInterface.setStatus("current")


class _PrtIsdnCallMode_Type(Integer32):
    """Custom type prtIsdnCallMode based on Integer32"""
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
          ("initiate", 2),
          ("listen", 3))
    )


_PrtIsdnCallMode_Type.__name__ = "Integer32"
_PrtIsdnCallMode_Object = MibTableColumn
prtIsdnCallMode = _PrtIsdnCallMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 15),
    _PrtIsdnCallMode_Type()
)
prtIsdnCallMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnCallMode.setStatus("current")
_PrtIsdnCallBackTimeout_Type = Integer32
_PrtIsdnCallBackTimeout_Object = MibTableColumn
prtIsdnCallBackTimeout = _PrtIsdnCallBackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 1, 1, 16),
    _PrtIsdnCallBackTimeout_Type()
)
prtIsdnCallBackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtIsdnCallBackTimeout.setStatus("current")
_PrtIsdnEndpointTable_Object = MibTable
prtIsdnEndpointTable = _PrtIsdnEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2)
)
if mibBuilder.loadTexts:
    prtIsdnEndpointTable.setStatus("current")
_PrtIsdnEndpointEntry_Object = MibTableRow
prtIsdnEndpointEntry = _PrtIsdnEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1)
)
prtIsdnEndpointEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtIsdnEndpointCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtIsdnEndpointSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtIsdnEndpointPrtIdx"),
    (0, "RAD-Mpmx-MIB", "prtIsdnEndpointIdx"),
)
if mibBuilder.loadTexts:
    prtIsdnEndpointEntry.setStatus("current")


class _PrtIsdnEndpointCnfgIdx_Type(Integer32):
    """Custom type prtIsdnEndpointCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtIsdnEndpointCnfgIdx_Type.__name__ = "Integer32"
_PrtIsdnEndpointCnfgIdx_Object = MibTableColumn
prtIsdnEndpointCnfgIdx = _PrtIsdnEndpointCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1, 1),
    _PrtIsdnEndpointCnfgIdx_Type()
)
prtIsdnEndpointCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnEndpointCnfgIdx.setStatus("current")


class _PrtIsdnEndpointSltIdx_Type(Integer32):
    """Custom type prtIsdnEndpointSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              103,
              104,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("kmxMlA", 103),
          ("kmxMlB", 104),
          ("notApplicable", 255))
    )


_PrtIsdnEndpointSltIdx_Type.__name__ = "Integer32"
_PrtIsdnEndpointSltIdx_Object = MibTableColumn
prtIsdnEndpointSltIdx = _PrtIsdnEndpointSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1, 2),
    _PrtIsdnEndpointSltIdx_Type()
)
prtIsdnEndpointSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnEndpointSltIdx.setStatus("current")
_PrtIsdnEndpointPrtIdx_Type = Integer32
_PrtIsdnEndpointPrtIdx_Object = MibTableColumn
prtIsdnEndpointPrtIdx = _PrtIsdnEndpointPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1, 3),
    _PrtIsdnEndpointPrtIdx_Type()
)
prtIsdnEndpointPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnEndpointPrtIdx.setStatus("current")


class _PrtIsdnEndpointIdx_Type(Integer32):
    """Custom type prtIsdnEndpointIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atei1", 1),
          ("atei2", 2))
    )


_PrtIsdnEndpointIdx_Type.__name__ = "Integer32"
_PrtIsdnEndpointIdx_Object = MibTableColumn
prtIsdnEndpointIdx = _PrtIsdnEndpointIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1, 4),
    _PrtIsdnEndpointIdx_Type()
)
prtIsdnEndpointIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnEndpointIdx.setStatus("current")


class _PrtIsdnEndpointTeiType_Type(Integer32):
    """Custom type prtIsdnEndpointTeiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2),
          ("notApplicable", 255))
    )


_PrtIsdnEndpointTeiType_Type.__name__ = "Integer32"
_PrtIsdnEndpointTeiType_Object = MibTableColumn
prtIsdnEndpointTeiType = _PrtIsdnEndpointTeiType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1, 5),
    _PrtIsdnEndpointTeiType_Type()
)
prtIsdnEndpointTeiType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnEndpointTeiType.setStatus("current")
_PrtIsdnEndpointTeiValue_Type = Integer32
_PrtIsdnEndpointTeiValue_Object = MibTableColumn
prtIsdnEndpointTeiValue = _PrtIsdnEndpointTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1, 6),
    _PrtIsdnEndpointTeiValue_Type()
)
prtIsdnEndpointTeiValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnEndpointTeiValue.setStatus("current")
_PrtIsdnEndpointSpid_Type = DisplayString
_PrtIsdnEndpointSpid_Object = MibTableColumn
prtIsdnEndpointSpid = _PrtIsdnEndpointSpid_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1, 7),
    _PrtIsdnEndpointSpid_Type()
)
prtIsdnEndpointSpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnEndpointSpid.setStatus("current")


class _PrtIsdnEndpointBearerCh_Type(Integer32):
    """Custom type prtIsdnEndpointBearerCh based on Integer32"""
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
        *(("notApplicable", 1),
          ("anyChannel", 2),
          ("channelB1", 3),
          ("channelB2", 4))
    )


_PrtIsdnEndpointBearerCh_Type.__name__ = "Integer32"
_PrtIsdnEndpointBearerCh_Object = MibTableColumn
prtIsdnEndpointBearerCh = _PrtIsdnEndpointBearerCh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1, 8),
    _PrtIsdnEndpointBearerCh_Type()
)
prtIsdnEndpointBearerCh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnEndpointBearerCh.setStatus("current")
_PrtIsdnEndpointRowStatus_Type = RowStatus
_PrtIsdnEndpointRowStatus_Object = MibTableColumn
prtIsdnEndpointRowStatus = _PrtIsdnEndpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 2, 1, 9),
    _PrtIsdnEndpointRowStatus_Type()
)
prtIsdnEndpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnEndpointRowStatus.setStatus("current")
_PrtIsdnDirectoryTable_Object = MibTable
prtIsdnDirectoryTable = _PrtIsdnDirectoryTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3)
)
if mibBuilder.loadTexts:
    prtIsdnDirectoryTable.setStatus("current")
_PrtIsdnDirectoryEntry_Object = MibTableRow
prtIsdnDirectoryEntry = _PrtIsdnDirectoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1)
)
prtIsdnDirectoryEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtIsdnDirectoryCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtIsdnDirectorySltIdx"),
    (0, "RAD-Mpmx-MIB", "prtIsdnDirectoryPrtIdx"),
)
if mibBuilder.loadTexts:
    prtIsdnDirectoryEntry.setStatus("current")


class _PrtIsdnDirectoryCnfgIdx_Type(Integer32):
    """Custom type prtIsdnDirectoryCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtIsdnDirectoryCnfgIdx_Type.__name__ = "Integer32"
_PrtIsdnDirectoryCnfgIdx_Object = MibTableColumn
prtIsdnDirectoryCnfgIdx = _PrtIsdnDirectoryCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 1),
    _PrtIsdnDirectoryCnfgIdx_Type()
)
prtIsdnDirectoryCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnDirectoryCnfgIdx.setStatus("current")


class _PrtIsdnDirectorySltIdx_Type(Integer32):
    """Custom type prtIsdnDirectorySltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              103,
              104,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("kmxMlA", 103),
          ("kmxMlB", 104),
          ("notApplicable", 255))
    )


_PrtIsdnDirectorySltIdx_Type.__name__ = "Integer32"
_PrtIsdnDirectorySltIdx_Object = MibTableColumn
prtIsdnDirectorySltIdx = _PrtIsdnDirectorySltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 2),
    _PrtIsdnDirectorySltIdx_Type()
)
prtIsdnDirectorySltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnDirectorySltIdx.setStatus("current")
_PrtIsdnDirectoryPrtIdx_Type = Integer32
_PrtIsdnDirectoryPrtIdx_Object = MibTableColumn
prtIsdnDirectoryPrtIdx = _PrtIsdnDirectoryPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 3),
    _PrtIsdnDirectoryPrtIdx_Type()
)
prtIsdnDirectoryPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtIsdnDirectoryPrtIdx.setStatus("current")


class _PrtIsdnDirectoryLocalAddr_Type(DisplayString):
    """Custom type prtIsdnDirectoryLocalAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 20),
    )


_PrtIsdnDirectoryLocalAddr_Type.__name__ = "DisplayString"
_PrtIsdnDirectoryLocalAddr_Object = MibTableColumn
prtIsdnDirectoryLocalAddr = _PrtIsdnDirectoryLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 4),
    _PrtIsdnDirectoryLocalAddr_Type()
)
prtIsdnDirectoryLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryLocalAddr.setStatus("current")


class _PrtIsdnDirectoryLocalSubAddr_Type(DisplayString):
    """Custom type prtIsdnDirectoryLocalSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 6),
    )


_PrtIsdnDirectoryLocalSubAddr_Type.__name__ = "DisplayString"
_PrtIsdnDirectoryLocalSubAddr_Object = MibTableColumn
prtIsdnDirectoryLocalSubAddr = _PrtIsdnDirectoryLocalSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 5),
    _PrtIsdnDirectoryLocalSubAddr_Type()
)
prtIsdnDirectoryLocalSubAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryLocalSubAddr.setStatus("current")


class _PrtIsdnDirectoryRemoteAddr_Type(DisplayString):
    """Custom type prtIsdnDirectoryRemoteAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 20),
    )


_PrtIsdnDirectoryRemoteAddr_Type.__name__ = "DisplayString"
_PrtIsdnDirectoryRemoteAddr_Object = MibTableColumn
prtIsdnDirectoryRemoteAddr = _PrtIsdnDirectoryRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 6),
    _PrtIsdnDirectoryRemoteAddr_Type()
)
prtIsdnDirectoryRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryRemoteAddr.setStatus("current")


class _PrtIsdnDirectoryRemoteSubAddr_Type(DisplayString):
    """Custom type prtIsdnDirectoryRemoteSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 6),
    )


_PrtIsdnDirectoryRemoteSubAddr_Type.__name__ = "DisplayString"
_PrtIsdnDirectoryRemoteSubAddr_Object = MibTableColumn
prtIsdnDirectoryRemoteSubAddr = _PrtIsdnDirectoryRemoteSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 7),
    _PrtIsdnDirectoryRemoteSubAddr_Type()
)
prtIsdnDirectoryRemoteSubAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryRemoteSubAddr.setStatus("current")


class _PrtIsdnDirectoryPrtNu_Type(Integer32):
    """Custom type prtIsdnDirectoryPrtNu based on Integer32"""
    defaultValue = 1


_PrtIsdnDirectoryPrtNu_Type.__name__ = "Integer32"
_PrtIsdnDirectoryPrtNu_Object = MibTableColumn
prtIsdnDirectoryPrtNu = _PrtIsdnDirectoryPrtNu_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 8),
    _PrtIsdnDirectoryPrtNu_Type()
)
prtIsdnDirectoryPrtNu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryPrtNu.setStatus("current")


class _PrtIsdnDirectoryTeiId_Type(Integer32):
    """Custom type prtIsdnDirectoryTeiId based on Integer32"""
    defaultValue = 1


_PrtIsdnDirectoryTeiId_Type.__name__ = "Integer32"
_PrtIsdnDirectoryTeiId_Object = MibTableColumn
prtIsdnDirectoryTeiId = _PrtIsdnDirectoryTeiId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 9),
    _PrtIsdnDirectoryTeiId_Type()
)
prtIsdnDirectoryTeiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryTeiId.setStatus("current")
_PrtIsdnDirectoryRowStatus_Type = RowStatus
_PrtIsdnDirectoryRowStatus_Object = MibTableColumn
prtIsdnDirectoryRowStatus = _PrtIsdnDirectoryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 10),
    _PrtIsdnDirectoryRowStatus_Type()
)
prtIsdnDirectoryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryRowStatus.setStatus("current")


class _PrtIsdnDirectoryLocalAddr2_Type(DisplayString):
    """Custom type prtIsdnDirectoryLocalAddr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 20),
    )


_PrtIsdnDirectoryLocalAddr2_Type.__name__ = "DisplayString"
_PrtIsdnDirectoryLocalAddr2_Object = MibTableColumn
prtIsdnDirectoryLocalAddr2 = _PrtIsdnDirectoryLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 11),
    _PrtIsdnDirectoryLocalAddr2_Type()
)
prtIsdnDirectoryLocalAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryLocalAddr2.setStatus("current")


class _PrtIsdnDirectoryLocalSubAddr2_Type(DisplayString):
    """Custom type prtIsdnDirectoryLocalSubAddr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 6),
    )


_PrtIsdnDirectoryLocalSubAddr2_Type.__name__ = "DisplayString"
_PrtIsdnDirectoryLocalSubAddr2_Object = MibTableColumn
prtIsdnDirectoryLocalSubAddr2 = _PrtIsdnDirectoryLocalSubAddr2_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 12),
    _PrtIsdnDirectoryLocalSubAddr2_Type()
)
prtIsdnDirectoryLocalSubAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryLocalSubAddr2.setStatus("current")


class _PrtIsdnDirectoryRemoteAddr2_Type(DisplayString):
    """Custom type prtIsdnDirectoryRemoteAddr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 20),
    )


_PrtIsdnDirectoryRemoteAddr2_Type.__name__ = "DisplayString"
_PrtIsdnDirectoryRemoteAddr2_Object = MibTableColumn
prtIsdnDirectoryRemoteAddr2 = _PrtIsdnDirectoryRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 13),
    _PrtIsdnDirectoryRemoteAddr2_Type()
)
prtIsdnDirectoryRemoteAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryRemoteAddr2.setStatus("current")


class _PrtIsdnDirectoryRemoteSubAddr2_Type(DisplayString):
    """Custom type prtIsdnDirectoryRemoteSubAddr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 6),
    )


_PrtIsdnDirectoryRemoteSubAddr2_Type.__name__ = "DisplayString"
_PrtIsdnDirectoryRemoteSubAddr2_Object = MibTableColumn
prtIsdnDirectoryRemoteSubAddr2 = _PrtIsdnDirectoryRemoteSubAddr2_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 16, 3, 1, 14),
    _PrtIsdnDirectoryRemoteSubAddr2_Type()
)
prtIsdnDirectoryRemoteSubAddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtIsdnDirectoryRemoteSubAddr2.setStatus("current")
_PrtLogicalCnfg_ObjectIdentity = ObjectIdentity
prtLogicalCnfg = _PrtLogicalCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17)
)
_PrtLogicalCnfgTable_Object = MibTable
prtLogicalCnfgTable = _PrtLogicalCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 1)
)
if mibBuilder.loadTexts:
    prtLogicalCnfgTable.setStatus("current")
_PrtLogicalCnfgEntry_Object = MibTableRow
prtLogicalCnfgEntry = _PrtLogicalCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 1, 1)
)
prtLogicalCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtLogicalCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtLogicalSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtLogicalPrtIdx"),
)
if mibBuilder.loadTexts:
    prtLogicalCnfgEntry.setStatus("current")


class _PrtLogicalCnfgIdx_Type(Integer32):
    """Custom type prtLogicalCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtLogicalCnfgIdx_Type.__name__ = "Integer32"
_PrtLogicalCnfgIdx_Object = MibTableColumn
prtLogicalCnfgIdx = _PrtLogicalCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 1, 1, 1),
    _PrtLogicalCnfgIdx_Type()
)
prtLogicalCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtLogicalCnfgIdx.setStatus("current")


class _PrtLogicalSltIdx_Type(Integer32):
    """Custom type prtLogicalSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtLogicalSltIdx_Type.__name__ = "Integer32"
_PrtLogicalSltIdx_Object = MibTableColumn
prtLogicalSltIdx = _PrtLogicalSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 1, 1, 2),
    _PrtLogicalSltIdx_Type()
)
prtLogicalSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtLogicalSltIdx.setStatus("current")
_PrtLogicalPrtIdx_Type = Integer32
_PrtLogicalPrtIdx_Object = MibTableColumn
prtLogicalPrtIdx = _PrtLogicalPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 1, 1, 3),
    _PrtLogicalPrtIdx_Type()
)
prtLogicalPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtLogicalPrtIdx.setStatus("current")


class _PrtLogicalConnect_Type(Integer32):
    """Custom type prtLogicalConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtLogicalConnect_Type.__name__ = "Integer32"
_PrtLogicalConnect_Object = MibTableColumn
prtLogicalConnect = _PrtLogicalConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 1, 1, 4),
    _PrtLogicalConnect_Type()
)
prtLogicalConnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtLogicalConnect.setStatus("current")


class _PrtLogicalFunction_Type(Integer32):
    """Custom type prtLogicalFunction based on Integer32"""
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
        *(("notApplicable", 1),
          ("linkSelector", 2),
          ("encapsulator", 3),
          ("huntGroup", 4))
    )


_PrtLogicalFunction_Type.__name__ = "Integer32"
_PrtLogicalFunction_Object = MibTableColumn
prtLogicalFunction = _PrtLogicalFunction_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 1, 1, 5),
    _PrtLogicalFunction_Type()
)
prtLogicalFunction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtLogicalFunction.setStatus("current")
_PrtLogicalRowStatus_Type = RowStatus
_PrtLogicalRowStatus_Object = MibTableColumn
prtLogicalRowStatus = _PrtLogicalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 1, 1, 6),
    _PrtLogicalRowStatus_Type()
)
prtLogicalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prtLogicalRowStatus.setStatus("current")
_LinkSelectorCnfgTable_Object = MibTable
linkSelectorCnfgTable = _LinkSelectorCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 2)
)
if mibBuilder.loadTexts:
    linkSelectorCnfgTable.setStatus("current")
_LinkSelectorCnfgEntry_Object = MibTableRow
linkSelectorCnfgEntry = _LinkSelectorCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 2, 1)
)
linkSelectorCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "linkSelectorCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "linkSelectorSltIdx"),
    (0, "RAD-Mpmx-MIB", "linkSelectorPrtIdx"),
)
if mibBuilder.loadTexts:
    linkSelectorCnfgEntry.setStatus("current")


class _LinkSelectorCnfgIdx_Type(Integer32):
    """Custom type linkSelectorCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LinkSelectorCnfgIdx_Type.__name__ = "Integer32"
_LinkSelectorCnfgIdx_Object = MibTableColumn
linkSelectorCnfgIdx = _LinkSelectorCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 2, 1, 1),
    _LinkSelectorCnfgIdx_Type()
)
linkSelectorCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSelectorCnfgIdx.setStatus("current")


class _LinkSelectorSltIdx_Type(Integer32):
    """Custom type linkSelectorSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_LinkSelectorSltIdx_Type.__name__ = "Integer32"
_LinkSelectorSltIdx_Object = MibTableColumn
linkSelectorSltIdx = _LinkSelectorSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 2, 1, 2),
    _LinkSelectorSltIdx_Type()
)
linkSelectorSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSelectorSltIdx.setStatus("current")
_LinkSelectorPrtIdx_Type = Integer32
_LinkSelectorPrtIdx_Object = MibTableColumn
linkSelectorPrtIdx = _LinkSelectorPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 2, 1, 3),
    _LinkSelectorPrtIdx_Type()
)
linkSelectorPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSelectorPrtIdx.setStatus("current")


class _LinkSelectorMaxIdleTime_Type(Integer32):
    """Custom type linkSelectorMaxIdleTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LinkSelectorMaxIdleTime_Type.__name__ = "Integer32"
_LinkSelectorMaxIdleTime_Object = MibTableColumn
linkSelectorMaxIdleTime = _LinkSelectorMaxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 2, 1, 4),
    _LinkSelectorMaxIdleTime_Type()
)
linkSelectorMaxIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkSelectorMaxIdleTime.setStatus("current")


class _LinkSelectorMode_Type(Integer32):
    """Custom type linkSelectorMode based on Integer32"""
    defaultValue = 2

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
          ("backup", 2),
          ("bod", 3))
    )


_LinkSelectorMode_Type.__name__ = "Integer32"
_LinkSelectorMode_Object = MibTableColumn
linkSelectorMode = _LinkSelectorMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 2, 1, 5),
    _LinkSelectorMode_Type()
)
linkSelectorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkSelectorMode.setStatus("current")


class _LinkSelectorRevert_Type(Integer32):
    """Custom type linkSelectorRevert based on Integer32"""
    defaultValue = 2

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
          ("auto", 2),
          ("manual", 3))
    )


_LinkSelectorRevert_Type.__name__ = "Integer32"
_LinkSelectorRevert_Object = MibTableColumn
linkSelectorRevert = _LinkSelectorRevert_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 2, 1, 6),
    _LinkSelectorRevert_Type()
)
linkSelectorRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkSelectorRevert.setStatus("current")


class _LinkSelectorMinBUSession_Type(Integer32):
    """Custom type linkSelectorMinBUSession based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LinkSelectorMinBUSession_Type.__name__ = "Integer32"
_LinkSelectorMinBUSession_Object = MibTableColumn
linkSelectorMinBUSession = _LinkSelectorMinBUSession_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 2, 1, 7),
    _LinkSelectorMinBUSession_Type()
)
linkSelectorMinBUSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkSelectorMinBUSession.setStatus("current")
_LinkSelectorPLinkTable_Object = MibTable
linkSelectorPLinkTable = _LinkSelectorPLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3)
)
if mibBuilder.loadTexts:
    linkSelectorPLinkTable.setStatus("current")
_LinkSelectorPLinkEntry_Object = MibTableRow
linkSelectorPLinkEntry = _LinkSelectorPLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3, 1)
)
linkSelectorPLinkEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "pLinkCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "pLinkSltIdx"),
    (0, "RAD-Mpmx-MIB", "pLinkPrtIdx"),
    (0, "RAD-Mpmx-MIB", "pLinkIdx"),
)
if mibBuilder.loadTexts:
    linkSelectorPLinkEntry.setStatus("current")


class _PLinkCnfgIdx_Type(Integer32):
    """Custom type pLinkCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PLinkCnfgIdx_Type.__name__ = "Integer32"
_PLinkCnfgIdx_Object = MibTableColumn
pLinkCnfgIdx = _PLinkCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3, 1, 1),
    _PLinkCnfgIdx_Type()
)
pLinkCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pLinkCnfgIdx.setStatus("current")


class _PLinkSltIdx_Type(Integer32):
    """Custom type pLinkSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PLinkSltIdx_Type.__name__ = "Integer32"
_PLinkSltIdx_Object = MibTableColumn
pLinkSltIdx = _PLinkSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3, 1, 2),
    _PLinkSltIdx_Type()
)
pLinkSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pLinkSltIdx.setStatus("current")


class _PLinkPrtIdx_Type(Integer32):
    """Custom type pLinkPrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 250),
    )


_PLinkPrtIdx_Type.__name__ = "Integer32"
_PLinkPrtIdx_Object = MibTableColumn
pLinkPrtIdx = _PLinkPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3, 1, 3),
    _PLinkPrtIdx_Type()
)
pLinkPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pLinkPrtIdx.setStatus("current")


class _PLinkIdx_Type(Integer32):
    """Custom type pLinkIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PLinkIdx_Type.__name__ = "Integer32"
_PLinkIdx_Object = MibTableColumn
pLinkIdx = _PLinkIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3, 1, 4),
    _PLinkIdx_Type()
)
pLinkIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pLinkIdx.setStatus("current")


class _PLinkSlotNu_Type(Integer32):
    """Custom type pLinkSlotNu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noConnect", 2),
          ("cl", 3),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PLinkSlotNu_Type.__name__ = "Integer32"
_PLinkSlotNu_Object = MibTableColumn
pLinkSlotNu = _PLinkSlotNu_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3, 1, 5),
    _PLinkSlotNu_Type()
)
pLinkSlotNu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pLinkSlotNu.setStatus("current")


class _PLinkPortNu_Type(Integer32):
    """Custom type pLinkPortNu based on Integer32"""
    defaultValue = 100


_PLinkPortNu_Type.__name__ = "Integer32"
_PLinkPortNu_Object = MibTableColumn
pLinkPortNu = _PLinkPortNu_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3, 1, 6),
    _PLinkPortNu_Type()
)
pLinkPortNu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pLinkPortNu.setStatus("current")


class _PLinkPrioNu_Type(Integer32):
    """Custom type pLinkPrioNu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PLinkPrioNu_Type.__name__ = "Integer32"
_PLinkPrioNu_Object = MibTableColumn
pLinkPrioNu = _PLinkPrioNu_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3, 1, 7),
    _PLinkPrioNu_Type()
)
pLinkPrioNu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pLinkPrioNu.setStatus("current")


class _PLinkVRate_Type(Integer32):
    """Custom type pLinkVRate based on Integer32"""
    defaultValue = 100

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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              100)
        )
    )
    namedValues = NamedValues(
        *(("r1x56eq56Kbps", 1),
          ("r1x64eq64Kbps", 2),
          ("r2x56eq112Kbps", 3),
          ("r2x64eq128Kbps", 4),
          ("r3x56eq168Kbps", 5),
          ("r3x64eq192Kbps", 6),
          ("r4x56eq224Kbps", 7),
          ("r4x64eq256Kbps", 8),
          ("r5x56eq280Kbps", 9),
          ("r5x64eq320Kbps", 10),
          ("r6x56eq336Kbps", 11),
          ("r6x64eq384Kbps", 12),
          ("r7x56eq392Kbps", 13),
          ("r7x64eq448Kbps", 14),
          ("r8x56eq448Kbps", 15),
          ("r8x64eq512Kbps", 16),
          ("r9x56eq504Kbps", 17),
          ("r9x64eq576Kbps", 18),
          ("r10x56eq560Kbps", 19),
          ("r10x64eq640Kbps", 20),
          ("r11x56eq616Kbps", 21),
          ("r11x64eq704Kbps", 22),
          ("r12x56eq672Kbps", 23),
          ("r12x64eq768Kbps", 24),
          ("r13x56eq728Kbps", 25),
          ("r13x64eq832Kbps", 26),
          ("r14x56eq784Kbps", 27),
          ("r14x64eq896Kbps", 28),
          ("r15x56eq840Kbps", 29),
          ("r15x64eq960Kbps", 30),
          ("r16x56eq896Kbps", 31),
          ("r16x64eq1024Kbps", 32),
          ("r17x56eq952Kbps", 33),
          ("r17x64eq1088Kbps", 34),
          ("r18x56eq1008Kbps", 35),
          ("r18x64eq1152Kbps", 36),
          ("r19x56eq1064Kbps", 37),
          ("r19x64eq1216Kbps", 38),
          ("r20x56eq1120Kbps", 39),
          ("r20x64eq1280Kbps", 40),
          ("r21x56eq1176Kbps", 41),
          ("r21x64eq1344Kbps", 42),
          ("r22x56eq1232Kbps", 43),
          ("r22x64eq1408Kbps", 44),
          ("r23x56eq1288Kbps", 45),
          ("r23x64eq1472Kbps", 46),
          ("r24x56eq1344Kbps", 47),
          ("r24x64eq1536Kbps", 48),
          ("r25x56eq1400Kbps", 49),
          ("r25x64eq1600Kbps", 50),
          ("r26x56eq1456Kbps", 51),
          ("r26x64eq1664Kbps", 52),
          ("r27x56eq1512Kbps", 53),
          ("r27x64eq1728Kbps", 54),
          ("r28x56eq1568Kbps", 55),
          ("r28x64eq1792Kbps", 56),
          ("r29x56eq1624Kbps", 57),
          ("r29x64eq1856Kbps", 58),
          ("r30x56eq1680Kbps", 59),
          ("r30x64eq1920Kbps", 60),
          ("r31x56eq1736Kbps", 61),
          ("r31x64eq1984Kbps", 62),
          ("noRate", 100))
    )


_PLinkVRate_Type.__name__ = "Integer32"
_PLinkVRate_Object = MibTableColumn
pLinkVRate = _PLinkVRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 17, 3, 1, 8),
    _PLinkVRate_Type()
)
pLinkVRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pLinkVRate.setStatus("current")
_PrtFrPlusCnfg_ObjectIdentity = ObjectIdentity
prtFrPlusCnfg = _PrtFrPlusCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 18)
)
_PrtFrPlusCnfgTable_Object = MibTable
prtFrPlusCnfgTable = _PrtFrPlusCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 18, 1)
)
if mibBuilder.loadTexts:
    prtFrPlusCnfgTable.setStatus("current")
_PrtFrPlusCnfgEntry_Object = MibTableRow
prtFrPlusCnfgEntry = _PrtFrPlusCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 18, 1, 1)
)
prtFrPlusCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtFrPlusCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtFrPlusSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtFrPlusPrtIdx"),
)
if mibBuilder.loadTexts:
    prtFrPlusCnfgEntry.setStatus("current")


class _PrtFrPlusCnfgIdx_Type(Integer32):
    """Custom type prtFrPlusCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtFrPlusCnfgIdx_Type.__name__ = "Integer32"
_PrtFrPlusCnfgIdx_Object = MibTableColumn
prtFrPlusCnfgIdx = _PrtFrPlusCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 18, 1, 1, 1),
    _PrtFrPlusCnfgIdx_Type()
)
prtFrPlusCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrPlusCnfgIdx.setStatus("current")


class _PrtFrPlusSltIdx_Type(Integer32):
    """Custom type prtFrPlusSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtFrPlusSltIdx_Type.__name__ = "Integer32"
_PrtFrPlusSltIdx_Object = MibTableColumn
prtFrPlusSltIdx = _PrtFrPlusSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 18, 1, 1, 2),
    _PrtFrPlusSltIdx_Type()
)
prtFrPlusSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrPlusSltIdx.setStatus("current")
_PrtFrPlusPrtIdx_Type = Integer32
_PrtFrPlusPrtIdx_Object = MibTableColumn
prtFrPlusPrtIdx = _PrtFrPlusPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 18, 1, 1, 3),
    _PrtFrPlusPrtIdx_Type()
)
prtFrPlusPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtFrPlusPrtIdx.setStatus("current")


class _PrtFrPlusNotSegmentedPriorities_Type(OctetString):
    """Custom type prtFrPlusNotSegmentedPriorities based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_PrtFrPlusNotSegmentedPriorities_Type.__name__ = "OctetString"
_PrtFrPlusNotSegmentedPriorities_Object = MibTableColumn
prtFrPlusNotSegmentedPriorities = _PrtFrPlusNotSegmentedPriorities_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 18, 1, 1, 4),
    _PrtFrPlusNotSegmentedPriorities_Type()
)
prtFrPlusNotSegmentedPriorities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtFrPlusNotSegmentedPriorities.setStatus("current")
_PrtMl4Cnfg_ObjectIdentity = ObjectIdentity
prtMl4Cnfg = _PrtMl4Cnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19)
)
_PrtMl4CnfgTable_Object = MibTable
prtMl4CnfgTable = _PrtMl4CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1)
)
if mibBuilder.loadTexts:
    prtMl4CnfgTable.setStatus("current")
_PrtMl4CnfgEntry_Object = MibTableRow
prtMl4CnfgEntry = _PrtMl4CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1)
)
prtMl4CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtMl4CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtMl4SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtMl4PrtIdx"),
)
if mibBuilder.loadTexts:
    prtMl4CnfgEntry.setStatus("current")


class _PrtMl4CnfgIdx_Type(Integer32):
    """Custom type prtMl4CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtMl4CnfgIdx_Type.__name__ = "Integer32"
_PrtMl4CnfgIdx_Object = MibTableColumn
prtMl4CnfgIdx = _PrtMl4CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 1),
    _PrtMl4CnfgIdx_Type()
)
prtMl4CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMl4CnfgIdx.setStatus("current")


class _PrtMl4SltIdx_Type(Integer32):
    """Custom type prtMl4SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clA", 3),
          ("clB", 4),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtMl4SltIdx_Type.__name__ = "Integer32"
_PrtMl4SltIdx_Object = MibTableColumn
prtMl4SltIdx = _PrtMl4SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 2),
    _PrtMl4SltIdx_Type()
)
prtMl4SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMl4SltIdx.setStatus("current")


class _PrtMl4PrtIdx_Type(Integer32):
    """Custom type prtMl4PrtIdx based on Integer32"""
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
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("inPrt1", 101),
          ("inPrt2", 102),
          ("inPrt3", 103),
          ("inPrt4", 104),
          ("inPrt5", 105),
          ("inPrt6", 106),
          ("inPrt7", 107),
          ("inPrt8", 108),
          ("inPrt9", 109),
          ("inPrt10", 110),
          ("inPrt11", 111),
          ("inPrt12", 112),
          ("inPrt13", 113),
          ("inPrt14", 114),
          ("inPrt15", 115),
          ("inPrt16", 116),
          ("inPrt17", 117),
          ("inPrt18", 118),
          ("inPrt19", 119),
          ("inPrt20", 120),
          ("inPrt21", 121),
          ("inPrt22", 122),
          ("inPrt23", 123),
          ("inPrt24", 124),
          ("inPrt25", 125),
          ("inPrt26", 126),
          ("inPrt27", 127),
          ("inPrt28", 128),
          ("inPrt29", 129),
          ("inPrt30", 130),
          ("inPrt31", 131),
          ("inPrt32", 132),
          ("inPrt33", 133),
          ("inPrt34", 134),
          ("inPrt35", 135),
          ("inPrt36", 136),
          ("inPrt37", 137),
          ("inPrt38", 138),
          ("inPrt39", 139),
          ("inPrt40", 140),
          ("inPrt41", 141),
          ("inPrt42", 142),
          ("inPrt43", 143),
          ("inPrt44", 144),
          ("inPrt45", 145),
          ("inPrt46", 146),
          ("inPrt47", 147),
          ("inPrt48", 148),
          ("inPrt49", 149),
          ("inPrt50", 150),
          ("inPrt51", 151),
          ("inPrt52", 152),
          ("inPrt53", 153),
          ("inPrt54", 154),
          ("inPrt55", 155),
          ("inPrt56", 156),
          ("inPrt57", 157),
          ("inPrt58", 158),
          ("inPrt59", 159),
          ("inPrt60", 160),
          ("inPrt61", 161),
          ("inPrt62", 162),
          ("inPrt63", 163),
          ("inPrt64", 164),
          ("inPrt65", 165),
          ("inPrt66", 166),
          ("inPrt67", 167),
          ("inPrt68", 168),
          ("inPrt69", 169),
          ("inPrt70", 170),
          ("inPrt71", 171),
          ("inPrt72", 172),
          ("inPrt73", 173),
          ("inPrt74", 174),
          ("inPrt75", 175),
          ("inPrt76", 176),
          ("inPrt77", 177),
          ("inPrt78", 178),
          ("inPrt79", 179),
          ("inPrt80", 180),
          ("inPrt81", 181),
          ("inPrt82", 182),
          ("inPrt83", 183),
          ("inPrt84", 184))
    )


_PrtMl4PrtIdx_Type.__name__ = "Integer32"
_PrtMl4PrtIdx_Object = MibTableColumn
prtMl4PrtIdx = _PrtMl4PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 3),
    _PrtMl4PrtIdx_Type()
)
prtMl4PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtMl4PrtIdx.setStatus("current")


class _PrtMl4SigProfile_Type(Integer32):
    """Custom type prtMl4SigProfile based on Integer32"""
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
          ("none", 2),
          ("p1", 3),
          ("p2", 4),
          ("p3", 5),
          ("p4", 6),
          ("p5", 7),
          ("perTS", 8))
    )


_PrtMl4SigProfile_Type.__name__ = "Integer32"
_PrtMl4SigProfile_Object = MibTableColumn
prtMl4SigProfile = _PrtMl4SigProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 4),
    _PrtMl4SigProfile_Type()
)
prtMl4SigProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4SigProfile.setStatus("current")


class _PrtMl4CGA_Type(Integer32):
    """Custom type prtMl4CGA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("trans", 2),
          ("full", 3))
    )


_PrtMl4CGA_Type.__name__ = "Integer32"
_PrtMl4CGA_Object = MibTableColumn
prtMl4CGA = _PrtMl4CGA_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 5),
    _PrtMl4CGA_Type()
)
prtMl4CGA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4CGA.setStatus("current")


class _PrtMl4Oos_Type(Integer32):
    """Custom type prtMl4Oos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("forcedIdle", 3),
          ("forcedBusy", 4),
          ("busyIdle", 5),
          ("idleBusy", 6))
    )


_PrtMl4Oos_Type.__name__ = "Integer32"
_PrtMl4Oos_Object = MibTableColumn
prtMl4Oos = _PrtMl4Oos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 6),
    _PrtMl4Oos_Type()
)
prtMl4Oos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4Oos.setStatus("current")


class _PrtMl4VoiceOos_Type(OctetString):
    """Custom type prtMl4VoiceOos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PrtMl4VoiceOos_Type.__name__ = "OctetString"
_PrtMl4VoiceOos_Object = MibTableColumn
prtMl4VoiceOos = _PrtMl4VoiceOos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 7),
    _PrtMl4VoiceOos_Type()
)
prtMl4VoiceOos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4VoiceOos.setStatus("current")


class _PrtMl4DataOos_Type(OctetString):
    """Custom type prtMl4DataOos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PrtMl4DataOos_Type.__name__ = "OctetString"
_PrtMl4DataOos_Object = MibTableColumn
prtMl4DataOos = _PrtMl4DataOos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 8),
    _PrtMl4DataOos_Type()
)
prtMl4DataOos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4DataOos.setStatus("current")


class _PrtMl4Service_Type(Integer32):
    """Custom type prtMl4Service based on Integer32"""
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
        *(("notApplicable", 1),
          ("leasedLine", 2),
          ("v51", 3),
          ("v52Master", 4),
          ("v52Slave", 5))
    )


_PrtMl4Service_Type.__name__ = "Integer32"
_PrtMl4Service_Object = MibTableColumn
prtMl4Service = _PrtMl4Service_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 9),
    _PrtMl4Service_Type()
)
prtMl4Service.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4Service.setStatus("current")
_PrtMl4IpAddress_Type = IpAddress
_PrtMl4IpAddress_Object = MibTableColumn
prtMl4IpAddress = _PrtMl4IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 10),
    _PrtMl4IpAddress_Type()
)
prtMl4IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4IpAddress.setStatus("current")
_PrtMl4IpMask_Type = IpAddress
_PrtMl4IpMask_Object = MibTableColumn
prtMl4IpMask = _PrtMl4IpMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 11),
    _PrtMl4IpMask_Type()
)
prtMl4IpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4IpMask.setStatus("current")


class _PrtMl4SignalingMode_Type(Integer32):
    """Custom type prtMl4SignalingMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("cas", 2),
          ("ccs", 3),
          ("robbedBit", 4),
          ("other", 5))
    )


_PrtMl4SignalingMode_Type.__name__ = "Integer32"
_PrtMl4SignalingMode_Object = MibTableColumn
prtMl4SignalingMode = _PrtMl4SignalingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 12),
    _PrtMl4SignalingMode_Type()
)
prtMl4SignalingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4SignalingMode.setStatus("current")


class _PrtMl4EchoCanceler_Type(Integer32):
    """Custom type prtMl4EchoCanceler based on Integer32"""
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
          ("off", 2),
          ("on", 3))
    )


_PrtMl4EchoCanceler_Type.__name__ = "Integer32"
_PrtMl4EchoCanceler_Object = MibTableColumn
prtMl4EchoCanceler = _PrtMl4EchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 13),
    _PrtMl4EchoCanceler_Type()
)
prtMl4EchoCanceler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4EchoCanceler.setStatus("current")


class _PrtMl4OosErrorSource_Type(Integer32):
    """Custom type prtMl4OosErrorSource based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("framing", 3),
          ("bpv", 4))
    )


_PrtMl4OosErrorSource_Type.__name__ = "Integer32"
_PrtMl4OosErrorSource_Object = MibTableColumn
prtMl4OosErrorSource = _PrtMl4OosErrorSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 14),
    _PrtMl4OosErrorSource_Type()
)
prtMl4OosErrorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4OosErrorSource.setStatus("current")


class _PrtMl4OosEntryThreshold_Type(Integer32):
    """Custom type prtMl4OosEntryThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_PrtMl4OosEntryThreshold_Type.__name__ = "Integer32"
_PrtMl4OosEntryThreshold_Object = MibTableColumn
prtMl4OosEntryThreshold = _PrtMl4OosEntryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 15),
    _PrtMl4OosEntryThreshold_Type()
)
prtMl4OosEntryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4OosEntryThreshold.setStatus("current")


class _PrtMl4OosExitThreshold_Type(Integer32):
    """Custom type prtMl4OosExitThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_PrtMl4OosExitThreshold_Type.__name__ = "Integer32"
_PrtMl4OosExitThreshold_Object = MibTableColumn
prtMl4OosExitThreshold = _PrtMl4OosExitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 16),
    _PrtMl4OosExitThreshold_Type()
)
prtMl4OosExitThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4OosExitThreshold.setStatus("current")


class _PrtMl4LogicalLinkId_Type(Integer32):
    """Custom type prtMl4LogicalLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 257),
    )


_PrtMl4LogicalLinkId_Type.__name__ = "Integer32"
_PrtMl4LogicalLinkId_Object = MibTableColumn
prtMl4LogicalLinkId = _PrtMl4LogicalLinkId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 17),
    _PrtMl4LogicalLinkId_Type()
)
prtMl4LogicalLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4LogicalLinkId.setStatus("current")


class _PrtMl4DedicatedTs_Type(Integer32):
    """Custom type prtMl4DedicatedTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtMl4DedicatedTs_Type.__name__ = "Integer32"
_PrtMl4DedicatedTs_Object = MibTableColumn
prtMl4DedicatedTs = _PrtMl4DedicatedTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 18),
    _PrtMl4DedicatedTs_Type()
)
prtMl4DedicatedTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4DedicatedTs.setStatus("current")


class _PrtMl4RemCrc_Type(Integer32):
    """Custom type prtMl4RemCrc based on Integer32"""
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
          ("no", 2),
          ("yes", 3))
    )


_PrtMl4RemCrc_Type.__name__ = "Integer32"
_PrtMl4RemCrc_Object = MibTableColumn
prtMl4RemCrc = _PrtMl4RemCrc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 19),
    _PrtMl4RemCrc_Type()
)
prtMl4RemCrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4RemCrc.setStatus("current")


class _PrtMl4CrossConnectLevel_Type(Integer32):
    """Custom type prtMl4CrossConnectLevel based on Integer32"""
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
          ("ds0", 2),
          ("ds1", 3))
    )


_PrtMl4CrossConnectLevel_Type.__name__ = "Integer32"
_PrtMl4CrossConnectLevel_Object = MibTableColumn
prtMl4CrossConnectLevel = _PrtMl4CrossConnectLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 20),
    _PrtMl4CrossConnectLevel_Type()
)
prtMl4CrossConnectLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4CrossConnectLevel.setStatus("current")


class _PrtMl4PppEchoFailDetection_Type(Integer32):
    """Custom type prtMl4PppEchoFailDetection based on Integer32"""
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


_PrtMl4PppEchoFailDetection_Type.__name__ = "Integer32"
_PrtMl4PppEchoFailDetection_Object = MibTableColumn
prtMl4PppEchoFailDetection = _PrtMl4PppEchoFailDetection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 21),
    _PrtMl4PppEchoFailDetection_Type()
)
prtMl4PppEchoFailDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4PppEchoFailDetection.setStatus("current")


class _PrtMl4EcanCasControl_Type(Integer32):
    """Custom type prtMl4EcanCasControl based on Integer32"""
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


_PrtMl4EcanCasControl_Type.__name__ = "Integer32"
_PrtMl4EcanCasControl_Object = MibTableColumn
prtMl4EcanCasControl = _PrtMl4EcanCasControl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 19, 1, 1, 22),
    _PrtMl4EcanCasControl_Type()
)
prtMl4EcanCasControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtMl4EcanCasControl.setStatus("current")
_PrtAcmCnfg_ObjectIdentity = ObjectIdentity
prtAcmCnfg = _PrtAcmCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 20)
)
_PrtAcmCnfgTable_Object = MibTable
prtAcmCnfgTable = _PrtAcmCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 20, 1)
)
if mibBuilder.loadTexts:
    prtAcmCnfgTable.setStatus("current")
_PrtAcmCnfgEntry_Object = MibTableRow
prtAcmCnfgEntry = _PrtAcmCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 20, 1, 1)
)
prtAcmCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtAcmCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtAcmSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtAcmPrtIdx"),
)
if mibBuilder.loadTexts:
    prtAcmCnfgEntry.setStatus("current")


class _PrtAcmCnfgIdx_Type(Integer32):
    """Custom type prtAcmCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtAcmCnfgIdx_Type.__name__ = "Integer32"
_PrtAcmCnfgIdx_Object = MibTableColumn
prtAcmCnfgIdx = _PrtAcmCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 20, 1, 1, 1),
    _PrtAcmCnfgIdx_Type()
)
prtAcmCnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAcmCnfgIdx.setStatus("current")


class _PrtAcmSltIdx_Type(Integer32):
    """Custom type prtAcmSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              255)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16),
          ("notApplicable", 255))
    )


_PrtAcmSltIdx_Type.__name__ = "Integer32"
_PrtAcmSltIdx_Object = MibTableColumn
prtAcmSltIdx = _PrtAcmSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 20, 1, 1, 2),
    _PrtAcmSltIdx_Type()
)
prtAcmSltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAcmSltIdx.setStatus("current")


class _PrtAcmPrtIdx_Type(Integer32):
    """Custom type prtAcmPrtIdx based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2),
          ("exPrt3", 3),
          ("exPrt4", 4),
          ("exPrt5", 5),
          ("exPrt6", 6),
          ("exPrt7", 7),
          ("exPrt8", 8),
          ("exPrt9", 9),
          ("exPrt10", 10),
          ("exPrt11", 11),
          ("exPrt12", 12))
    )


_PrtAcmPrtIdx_Type.__name__ = "Integer32"
_PrtAcmPrtIdx_Object = MibTableColumn
prtAcmPrtIdx = _PrtAcmPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 20, 1, 1, 3),
    _PrtAcmPrtIdx_Type()
)
prtAcmPrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtAcmPrtIdx.setStatus("current")


class _PrtAcmConnect_Type(Integer32):
    """Custom type prtAcmConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtAcmConnect_Type.__name__ = "Integer32"
_PrtAcmConnect_Object = MibTableColumn
prtAcmConnect = _PrtAcmConnect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 20, 1, 1, 4),
    _PrtAcmConnect_Type()
)
prtAcmConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtAcmConnect.setStatus("current")


class _PrtAcmActiveState_Type(Integer32):
    """Custom type prtAcmActiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("high", 3))
    )


_PrtAcmActiveState_Type.__name__ = "Integer32"
_PrtAcmActiveState_Object = MibTableColumn
prtAcmActiveState = _PrtAcmActiveState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 20, 1, 1, 5),
    _PrtAcmActiveState_Type()
)
prtAcmActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtAcmActiveState.setStatus("current")


class _PrtAcmAlrString_Type(DisplayString):
    """Custom type prtAcmAlrString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_PrtAcmAlrString_Type.__name__ = "DisplayString"
_PrtAcmAlrString_Object = MibTableColumn
prtAcmAlrString = _PrtAcmAlrString_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 20, 1, 1, 6),
    _PrtAcmAlrString_Type()
)
prtAcmAlrString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtAcmAlrString.setStatus("current")
_PrtE2Cnfg_ObjectIdentity = ObjectIdentity
prtE2Cnfg = _PrtE2Cnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 21)
)
_PrtE2CnfgTable_Object = MibTable
prtE2CnfgTable = _PrtE2CnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 21, 1)
)
if mibBuilder.loadTexts:
    prtE2CnfgTable.setStatus("current")
_PrtE2CnfgEntry_Object = MibTableRow
prtE2CnfgEntry = _PrtE2CnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 21, 1, 1)
)
prtE2CnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtE2CnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtE2SltIdx"),
    (0, "RAD-Mpmx-MIB", "prtE2PrtIdx"),
)
if mibBuilder.loadTexts:
    prtE2CnfgEntry.setStatus("current")


class _PrtE2CnfgIdx_Type(Integer32):
    """Custom type prtE2CnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtE2CnfgIdx_Type.__name__ = "Integer32"
_PrtE2CnfgIdx_Object = MibTableColumn
prtE2CnfgIdx = _PrtE2CnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 21, 1, 1, 1),
    _PrtE2CnfgIdx_Type()
)
prtE2CnfgIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtE2CnfgIdx.setStatus("current")


class _PrtE2SltIdx_Type(Integer32):
    """Custom type prtE2SltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtE2SltIdx_Type.__name__ = "Integer32"
_PrtE2SltIdx_Object = MibTableColumn
prtE2SltIdx = _PrtE2SltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 21, 1, 1, 2),
    _PrtE2SltIdx_Type()
)
prtE2SltIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtE2SltIdx.setStatus("current")


class _PrtE2PrtIdx_Type(Integer32):
    """Custom type prtE2PrtIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exPrt1", 1),
          ("exPrt2", 2))
    )


_PrtE2PrtIdx_Type.__name__ = "Integer32"
_PrtE2PrtIdx_Object = MibTableColumn
prtE2PrtIdx = _PrtE2PrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 21, 1, 1, 3),
    _PrtE2PrtIdx_Type()
)
prtE2PrtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtE2PrtIdx.setStatus("current")


class _PrtE2Connect_Type(Integer32):
    """Custom type prtE2Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtE2Connect_Type.__name__ = "Integer32"
_PrtE2Connect_Object = MibTableColumn
prtE2Connect = _PrtE2Connect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 21, 1, 1, 4),
    _PrtE2Connect_Type()
)
prtE2Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtE2Connect.setStatus("current")


class _PrtE2MngOnNationalBit_Type(Integer32):
    """Custom type prtE2MngOnNationalBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_PrtE2MngOnNationalBit_Type.__name__ = "Integer32"
_PrtE2MngOnNationalBit_Object = MibTableColumn
prtE2MngOnNationalBit = _PrtE2MngOnNationalBit_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 21, 1, 1, 5),
    _PrtE2MngOnNationalBit_Type()
)
prtE2MngOnNationalBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtE2MngOnNationalBit.setStatus("current")
_PrtLanWanCnfg_ObjectIdentity = ObjectIdentity
prtLanWanCnfg = _PrtLanWanCnfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22)
)
_PrtLanWanCnfgTable_Object = MibTable
prtLanWanCnfgTable = _PrtLanWanCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1)
)
if mibBuilder.loadTexts:
    prtLanWanCnfgTable.setStatus("current")
_PrtLanWanCnfgEntry_Object = MibTableRow
prtLanWanCnfgEntry = _PrtLanWanCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1)
)
prtLanWanCnfgEntry.setIndexNames(
    (0, "RAD-Mpmx-MIB", "prtLanWanCnfgIdx"),
    (0, "RAD-Mpmx-MIB", "prtLanWanSltIdx"),
    (0, "RAD-Mpmx-MIB", "prtLanWanPrtIdx"),
)
if mibBuilder.loadTexts:
    prtLanWanCnfgEntry.setStatus("current")


class _PrtLanWanCnfgIdx_Type(Integer32):
    """Custom type prtLanWanCnfgIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrtLanWanCnfgIdx_Type.__name__ = "Integer32"
_PrtLanWanCnfgIdx_Object = MibTableColumn
prtLanWanCnfgIdx = _PrtLanWanCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 1),
    _PrtLanWanCnfgIdx_Type()
)
prtLanWanCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtLanWanCnfgIdx.setStatus("current")


class _PrtLanWanSltIdx_Type(Integer32):
    """Custom type prtLanWanSltIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("io1", 5),
          ("io2", 6),
          ("io3", 7),
          ("io4", 8),
          ("io5", 9),
          ("io6", 10),
          ("io7", 11),
          ("io8", 12),
          ("io9", 13),
          ("io10", 14),
          ("io11", 15),
          ("io12", 16))
    )


_PrtLanWanSltIdx_Type.__name__ = "Integer32"
_PrtLanWanSltIdx_Object = MibTableColumn
prtLanWanSltIdx = _PrtLanWanSltIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 2),
    _PrtLanWanSltIdx_Type()
)
prtLanWanSltIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtLanWanSltIdx.setStatus("current")
_PrtLanWanPrtIdx_Type = Integer32
_PrtLanWanPrtIdx_Object = MibTableColumn
prtLanWanPrtIdx = _PrtLanWanPrtIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 3),
    _PrtLanWanPrtIdx_Type()
)
prtLanWanPrtIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prtLanWanPrtIdx.setStatus("current")


class _PrtLanWanMode_Type(Integer32):
    """Custom type prtLanWanMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("bridge", 2),
          ("bridgeAndStp", 3),
          ("layer3SubnetSwitch", 4))
    )


_PrtLanWanMode_Type.__name__ = "Integer32"
_PrtLanWanMode_Object = MibTableColumn
prtLanWanMode = _PrtLanWanMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 4),
    _PrtLanWanMode_Type()
)
prtLanWanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanMode.setStatus("current")
_PrtLanWanDestIf_Type = Integer32
_PrtLanWanDestIf_Object = MibTableColumn
prtLanWanDestIf = _PrtLanWanDestIf_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 5),
    _PrtLanWanDestIf_Type()
)
prtLanWanDestIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanDestIf.setStatus("current")


class _PrtLanWanEgressVlanMode_Type(Integer32):
    """Custom type prtLanWanEgressVlanMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("unmodified", 2),
          ("tag", 3),
          ("doubleTag", 4),
          ("untag", 5))
    )


_PrtLanWanEgressVlanMode_Type.__name__ = "Integer32"
_PrtLanWanEgressVlanMode_Object = MibTableColumn
prtLanWanEgressVlanMode = _PrtLanWanEgressVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 6),
    _PrtLanWanEgressVlanMode_Type()
)
prtLanWanEgressVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanEgressVlanMode.setStatus("current")


class _PrtLanWanL2Protocol_Type(Integer32):
    """Custom type prtLanWanL2Protocol based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("ppp", 3),
          ("hdlc", 4),
          ("pppoHdlc", 5),
          ("mlppp", 6))
    )


_PrtLanWanL2Protocol_Type.__name__ = "Integer32"
_PrtLanWanL2Protocol_Object = MibTableColumn
prtLanWanL2Protocol = _PrtLanWanL2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 7),
    _PrtLanWanL2Protocol_Type()
)
prtLanWanL2Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanL2Protocol.setStatus("current")


class _PrtLanWanStpPriority_Type(Integer32):
    """Custom type prtLanWanStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrtLanWanStpPriority_Type.__name__ = "Integer32"
_PrtLanWanStpPriority_Object = MibTableColumn
prtLanWanStpPriority = _PrtLanWanStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 8),
    _PrtLanWanStpPriority_Type()
)
prtLanWanStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanStpPriority.setStatus("current")


class _PrtLanWanStpCost_Type(Integer32):
    """Custom type prtLanWanStpCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrtLanWanStpCost_Type.__name__ = "Integer32"
_PrtLanWanStpCost_Object = MibTableColumn
prtLanWanStpCost = _PrtLanWanStpCost_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 9),
    _PrtLanWanStpCost_Type()
)
prtLanWanStpCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanStpCost.setStatus("current")


class _PrtLanWanToLanVlanMode_Type(Integer32):
    """Custom type prtLanWanToLanVlanMode based on Integer32"""
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
        *(("notApplicable", 1),
          ("unmodified", 2),
          ("tag", 3),
          ("doubleTag", 4),
          ("untag", 5))
    )


_PrtLanWanToLanVlanMode_Type.__name__ = "Integer32"
_PrtLanWanToLanVlanMode_Object = MibTableColumn
prtLanWanToLanVlanMode = _PrtLanWanToLanVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 10),
    _PrtLanWanToLanVlanMode_Type()
)
prtLanWanToLanVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanToLanVlanMode.setStatus("current")


class _PrtLanWanVlanId_Type(Integer32):
    """Custom type prtLanWanVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PrtLanWanVlanId_Type.__name__ = "Integer32"
_PrtLanWanVlanId_Object = MibTableColumn
prtLanWanVlanId = _PrtLanWanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 11),
    _PrtLanWanVlanId_Type()
)
prtLanWanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanVlanId.setStatus("current")
_PrtLanWanVlanPriority_Type = Integer32
_PrtLanWanVlanPriority_Object = MibTableColumn
prtLanWanVlanPriority = _PrtLanWanVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 12),
    _PrtLanWanVlanPriority_Type()
)
prtLanWanVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanVlanPriority.setStatus("current")
_PrtLanWanMtu_Type = Integer32
_PrtLanWanMtu_Object = MibTableColumn
prtLanWanMtu = _PrtLanWanMtu_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 13),
    _PrtLanWanMtu_Type()
)
prtLanWanMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanMtu.setStatus("current")


class _PrtLanWanVlanType_Type(Integer32):
    """Custom type prtLanWanVlanType based on Integer32"""
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
        *(("notApplicable", 1),
          ("portBasedVlan", 2),
          ("ieee802dot1q", 3),
          ("ieee802dot1qTaggedOnly", 4))
    )


_PrtLanWanVlanType_Type.__name__ = "Integer32"
_PrtLanWanVlanType_Object = MibTableColumn
prtLanWanVlanType = _PrtLanWanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 3, 2, 22, 1, 1, 14),
    _PrtLanWanVlanType_Type()
)
prtLanWanVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtLanWanVlanType.setStatus("current")

# Managed Objects groups


# Notification objects

alarmsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 0, 1)
)
alarmsTrap.setObjects(
    ("RAD-Mpmx-MIB", "alrBufDescription")
)
if mibBuilder.loadTexts:
    alarmsTrap.setStatus(
        "current"
    )

sanityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 0, 2)
)
sanityTrap.setObjects(
      *(("RAD-Mpmx-MIB", "agnSSanityCheckStatus"),
        ("RAD-Mpmx-MIB", "agnCSaveCnfgIdxCmd"))
)
if mibBuilder.loadTexts:
    sanityTrap.setStatus(
        "current"
    )

cnfgFlipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 0, 3)
)
cnfgFlipTrap.setObjects(
    ("RAD-Mpmx-MIB", "agnSActiveCnfg")
)
if mibBuilder.loadTexts:
    cnfgFlipTrap.setStatus(
        "current"
    )

flipDbChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 0, 4)
)
if mibBuilder.loadTexts:
    flipDbChangeTrap.setStatus(
        "current"
    )

statusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 2, 0, 5)
)
statusChangedTrap.setObjects(
    ("RAD-GEN-MIB", "agnLed")
)
if mibBuilder.loadTexts:
    statusChangedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-Mpmx-MIB",
    **{"chasWanGen": chasWanGen,
       "chasVersion": chasVersion,
       "chasTotalNoOfSlt": chasTotalNoOfSlt,
       "chasTotalNoOfIoSlt": chasTotalNoOfIoSlt,
       "chasTotalNoOfPsSlt": chasTotalNoOfPsSlt,
       "chasTotalNoOfClSlt": chasTotalNoOfClSlt,
       "agnWanGen": agnWanGen,
       "statAgnGen": statAgnGen,
       "agnSDateFormat": agnSDateFormat,
       "agnSDateCmd": agnSDateCmd,
       "agnSTimeCmd": agnSTimeCmd,
       "agnSActiveCnfg": agnSActiveCnfg,
       "agnSEditCnfg": agnSEditCnfg,
       "agnSLastCnfgFlipTime": agnSLastCnfgFlipTime,
       "agnSLastCnfgFlipCause": agnSLastCnfgFlipCause,
       "agnSEditBy": agnSEditBy,
       "agnSClkSrc": agnSClkSrc,
       "agnSAlrStatus": agnSAlrStatus,
       "agnSAlrStatusAll": agnSAlrStatusAll,
       "agnSMaskedAlrStat": agnSMaskedAlrStat,
       "agnSMaskedAlrStatAll": agnSMaskedAlrStatAll,
       "agnSTstStatAll": agnSTstStatAll,
       "agnSAlrTable": agnSAlrTable,
       "agnSAlrEntry": agnSAlrEntry,
       "agnSAlrIdx": agnSAlrIdx,
       "agnSAlrCodeDescription": agnSAlrCodeDescription,
       "agnSAlrCode": agnSAlrCode,
       "agnSAlrSeverity": agnSAlrSeverity,
       "agnSAlrState": agnSAlrState,
       "agnSAlrCounter": agnSAlrCounter,
       "agnSAlrMask": agnSAlrMask,
       "agnSAlrInvert": agnSAlrInvert,
       "agnSClearAlrCmd": agnSClearAlrCmd,
       "agnSClearAllAlrCmd": agnSClearAllAlrCmd,
       "agnSSanityCheckStatus": agnSSanityCheckStatus,
       "agnSNoOfSanityCheckErr": agnSNoOfSanityCheckErr,
       "agnSErrListTable": agnSErrListTable,
       "agnSErrListEntry": agnSErrListEntry,
       "agnSErrIdx": agnSErrIdx,
       "agnSErrDescription": agnSErrDescription,
       "agnSMaxNoOfCnfg": agnSMaxNoOfCnfg,
       "agnSCnfgTable": agnSCnfgTable,
       "agnSCnfgEntry": agnSCnfgEntry,
       "agnSEntryIdx": agnSEntryIdx,
       "agnSEntryIsValid": agnSEntryIsValid,
       "cnfgAgnGen": cnfgAgnGen,
       "agnCSanityCheckCmd": agnCSanityCheckCmd,
       "agnCSaveCnfgIdxCmd": agnCSaveCnfgIdxCmd,
       "agnCLoadCnfgIdxCmd": agnCLoadCnfgIdxCmd,
       "agnCClkSrcTable": agnCClkSrcTable,
       "agnCClkSrcEntry": agnCClkSrcEntry,
       "agnCClkCnfgIdx": agnCClkCnfgIdx,
       "agnCClkSrcIdx": agnCClkSrcIdx,
       "agnCClkSrcMode": agnCClkSrcMode,
       "agnCClkSrcSlt": agnCClkSrcSlt,
       "agnCClkSrcPrt": agnCClkSrcPrt,
       "agnCDeleteCnfgIdxCmd": agnCDeleteCnfgIdxCmd,
       "agnCDefaultCnfgIdxCmd": agnCDefaultCnfgIdxCmd,
       "agnCnfgDataTable": agnCnfgDataTable,
       "agnCnfgDataEntry": agnCnfgDataEntry,
       "agnCnfgIdx": agnCnfgIdx,
       "agnCnfgDesc": agnCnfgDesc,
       "agnCnfgUpdDate": agnCnfgUpdDate,
       "agnCnfgUpdTime": agnCnfgUpdTime,
       "agnCnfgUpdMnger": agnCnfgUpdMnger,
       "agnCnfgAlarm": agnCnfgAlarm,
       "agnCnfgAlrFilterWindow": agnCnfgAlrFilterWindow,
       "agnCnfgAlrTable": agnCnfgAlrTable,
       "agnCnfgAlrEntry": agnCnfgAlrEntry,
       "agnCnfgAlrCode": agnCnfgAlrCode,
       "agnCnfgAlrSlot": agnCnfgAlrSlot,
       "agnCnfgAlrPort": agnCnfgAlrPort,
       "agnCnfgAlrMask": agnCnfgAlrMask,
       "agnCnfgAlrInvert": agnCnfgAlrInvert,
       "agnCnfgAlrFilter": agnCnfgAlrFilter,
       "agnCnfgAlrFilterSet": agnCnfgAlrFilterSet,
       "agnCnfgAlrFilterReset": agnCnfgAlrFilterReset,
       "agnCnfgAlrSeverity": agnCnfgAlrSeverity,
       "agnCnfgAlrReportTable": agnCnfgAlrReportTable,
       "agnCnfgAlrReportEntry": agnCnfgAlrReportEntry,
       "agnCnfgAlrReportType": agnCnfgAlrReportType,
       "agnCnfgAlrStartReportOn": agnCnfgAlrStartReportOn,
       "agnCnfgAlrStartReportOff": agnCnfgAlrStartReportOff,
       "agnCOffsetCmd": agnCOffsetCmd,
       "agnCT1E1RingTable": agnCT1E1RingTable,
       "agnCT1E1RingEntry": agnCT1E1RingEntry,
       "agnCT1E1RingCnfgIdx": agnCT1E1RingCnfgIdx,
       "agnCT1E1RingPrimeSlot": agnCT1E1RingPrimeSlot,
       "agnCT1E1RingPrimePort": agnCT1E1RingPrimePort,
       "agnCT1E1RingSecSlot": agnCT1E1RingSecSlot,
       "agnCT1E1RingSecPort": agnCT1E1RingSecPort,
       "agnCT1E1RingRecTime": agnCT1E1RingRecTime,
       "agnCT1E1RingRowStatus": agnCT1E1RingRowStatus,
       "agnCT1E1RingWTR": agnCT1E1RingWTR,
       "agnCT1E1RingDualFailDetection": agnCT1E1RingDualFailDetection,
       "agnCMainExitPort": agnCMainExitPort,
       "agnCBuMlTable": agnCBuMlTable,
       "agnCBuMlEntry": agnCBuMlEntry,
       "agnCBuMlCnfgIdx": agnCBuMlCnfgIdx,
       "agnCBuMlRole": agnCBuMlRole,
       "agnCBuMlType": agnCBuMlType,
       "agnCBuMlDefaultGateway": agnCBuMlDefaultGateway,
       "agnCBuMlSubnetMask": agnCBuMlSubnetMask,
       "agnCBuMlOamFrequency": agnCBuMlOamFrequency,
       "agnCBuMlOamTimeoutCycles": agnCBuMlOamTimeoutCycles,
       "agnCBuMlWaitToRestore": agnCBuMlWaitToRestore,
       "agnCBuMlBfdSessionNum": agnCBuMlBfdSessionNum,
       "agnCQ50Table": agnCQ50Table,
       "agnCQ50Entry": agnCQ50Entry,
       "agnCQ50CnfgIdx": agnCQ50CnfgIdx,
       "agnCQ50StopCallsThresh": agnCQ50StopCallsThresh,
       "agnCQ50DiscardPktThresh": agnCQ50DiscardPktThresh,
       "agnCQ50BlockNewModemVbdCallsThresh": agnCQ50BlockNewModemVbdCallsThresh,
       "agnCQ50BlockNewModemRelayCallsThresh": agnCQ50BlockNewModemRelayCallsThresh,
       "cmprAgnGen": cmprAgnGen,
       "agnCmprTable": agnCmprTable,
       "agnCmprEntry": agnCmprEntry,
       "agnCmprTypIdx": agnCmprTypIdx,
       "agnCmprCnfgIdx": agnCmprCnfgIdx,
       "agnCmprVersion": agnCmprVersion,
       "agnCmprObj": agnCmprObj,
       "agnDlciCmprTable": agnDlciCmprTable,
       "agnDlciCmprEntry": agnDlciCmprEntry,
       "agnDlciCmprCnfgIdx": agnDlciCmprCnfgIdx,
       "agnDlciCmprVersion": agnDlciCmprVersion,
       "agnDlciCmprDlciIdx": agnDlciCmprDlciIdx,
       "agnDlciCmprObj": agnDlciCmprObj,
       "agnAlarmsCmprTable": agnAlarmsCmprTable,
       "agnAlarmsCmprEntry": agnAlarmsCmprEntry,
       "agnAlarmsCmprVersion": agnAlarmsCmprVersion,
       "agnAlarmsCmprAlarmIdx": agnAlarmsCmprAlarmIdx,
       "agnAlarmsCmprObj": agnAlarmsCmprObj,
       "agnAlrBufCmprTable": agnAlrBufCmprTable,
       "agnAlrBufCmprEntry": agnAlrBufCmprEntry,
       "agnAlrBufCmprVersion": agnAlrBufCmprVersion,
       "agnAlrBufCmprAlarmIdx": agnAlrBufCmprAlarmIdx,
       "agnAlrBufCmprObj": agnAlrBufCmprObj,
       "agnSCmprErrListTable": agnSCmprErrListTable,
       "agnSCmprErrListEntry": agnSCmprErrListEntry,
       "agnSCmprErrVersion": agnSCmprErrVersion,
       "agnSCmprErrIdx": agnSCmprErrIdx,
       "agnSCmprErrObj": agnSCmprErrObj,
       "agnTsCmprTable": agnTsCmprTable,
       "agnTsCmprEntry": agnTsCmprEntry,
       "agnTsCmprVerIdx": agnTsCmprVerIdx,
       "agnTsCmprCnfgIdx": agnTsCmprCnfgIdx,
       "agnTsCmprSlotIdx": agnTsCmprSlotIdx,
       "agnTsCmprPortIdx": agnTsCmprPortIdx,
       "agnTsCmprPduIdx": agnTsCmprPduIdx,
       "agnTsCmprData": agnTsCmprData,
       "agnXCmprTable": agnXCmprTable,
       "agnXCmprEntry": agnXCmprEntry,
       "agnXCmprTypIdx": agnXCmprTypIdx,
       "agnXCmprVersion": agnXCmprVersion,
       "agnXCmprIdx3": agnXCmprIdx3,
       "agnXCmprIdx4": agnXCmprIdx4,
       "agnXCmprIdx5": agnXCmprIdx5,
       "agnXCmprIdx6": agnXCmprIdx6,
       "agnXCmprIdx7": agnXCmprIdx7,
       "agnXCmprObj": agnXCmprObj,
       "alrBuffGen": alrBuffGen,
       "alrBufTable": alrBufTable,
       "alrBufEntry": alrBufEntry,
       "alrBufIdx": alrBufIdx,
       "alrBufDescription": alrBufDescription,
       "alrBufCode": alrBufCode,
       "alrBufSlot": alrBufSlot,
       "alrBufPort": alrBufPort,
       "alrBufSeverity": alrBufSeverity,
       "alrBufState": alrBufState,
       "alrBufferClearCmd": alrBufferClearCmd,
       "alrBufIdxUponLastAck": alrBufIdxUponLastAck,
       "agnFlipDb": agnFlipDb,
       "agnCAgendaTable": agnCAgendaTable,
       "agnCAgendaEntry": agnCAgendaEntry,
       "agnCAgendaCnfgIdx": agnCAgendaCnfgIdx,
       "agnCAgendaDayIdx": agnCAgendaDayIdx,
       "agnCAgendaDayCategory": agnCAgendaDayCategory,
       "agnCFlipNetEventsTable": agnCFlipNetEventsTable,
       "agnCFlipNetEventsEntry": agnCFlipNetEventsEntry,
       "agnCFlipNetEventsCnfgIdx": agnCFlipNetEventsCnfgIdx,
       "agnCFlipNetEventIdx": agnCFlipNetEventIdx,
       "agnCFlipNetEventActive": agnCFlipNetEventActive,
       "agnCFlipNetEventType": agnCFlipNetEventType,
       "agnCFlipNetEventNo": agnCFlipNetEventNo,
       "agnCFlipNetEventSlot": agnCFlipNetEventSlot,
       "agnCFlipNetEventPort": agnCFlipNetEventPort,
       "agnCFlipNetEventISD": agnCFlipNetEventISD,
       "agnCFlipNetEventOSD": agnCFlipNetEventOSD,
       "agnCFlipNetEventDayType": agnCFlipNetEventDayType,
       "agnCFlipNetEventStartTime": agnCFlipNetEventStartTime,
       "agnCFlipNetEventEndTime": agnCFlipNetEventEndTime,
       "agnCFlipTable": agnCFlipTable,
       "agnCFlipEntry": agnCFlipEntry,
       "agnCFlipCnfgIdx": agnCFlipCnfgIdx,
       "agnCFlipIdx": agnCFlipIdx,
       "agnCFlipActive": agnCFlipActive,
       "agnCFlipLogicalExp": agnCFlipLogicalExp,
       "agnCFlipDbNo": agnCFlipDbNo,
       "agnCFlipDiscardDe": agnCFlipDiscardDe,
       "agnFlipDbControls": agnFlipDbControls,
       "agnCFlipDbSanityCheckCmd": agnCFlipDbSanityCheckCmd,
       "agnCSaveFlipDbCmd": agnCSaveFlipDbCmd,
       "agnCSaveNetCnfgIdxCmd": agnCSaveNetCnfgIdxCmd,
       "agnCSaveNetFlipDbCmd": agnCSaveNetFlipDbCmd,
       "agnCNetGoCmd": agnCNetGoCmd,
       "agnCNetDelay": agnCNetDelay,
       "agnCNetEventsBcast": agnCNetEventsBcast,
       "agnCNetEventsBcastInterval": agnCNetEventsBcastInterval,
       "agnSa": agnSa,
       "agnSaSwchStatus": agnSaSwchStatus,
       "agnListDecoding": agnListDecoding,
       "agnListDecodingTable": agnListDecodingTable,
       "agnListDecodingEntry": agnListDecodingEntry,
       "agnListDecodingType": agnListDecodingType,
       "agnListDecodingCode": agnListDecodingCode,
       "agnListDecodingDescription": agnListDecodingDescription,
       "agnListDecodingDefState": agnListDecodingDefState,
       "agnListDecodingSeverity": agnListDecodingSeverity,
       "agnListDecodingAcmRelaySlt": agnListDecodingAcmRelaySlt,
       "agnListDecodingAcmRelayPrt": agnListDecodingAcmRelayPrt,
       "agnSystemDlci": agnSystemDlci,
       "agnDlciTable": agnDlciTable,
       "agnDlciEntry": agnDlciEntry,
       "agnDlciCnfgIdx": agnDlciCnfgIdx,
       "agnDlciLSltIdx": agnDlciLSltIdx,
       "agnDlciLPrtIdx": agnDlciLPrtIdx,
       "agnDlciLIdx": agnDlciLIdx,
       "agnDlciHSltIdx": agnDlciHSltIdx,
       "agnDlciHPrtIdx": agnDlciHPrtIdx,
       "agnDlciHIdx": agnDlciHIdx,
       "agnDlciTxBc": agnDlciTxBc,
       "agnDlciTxBe": agnDlciTxBe,
       "agnDlciRxBc": agnDlciRxBc,
       "agnDlciRxBe": agnDlciRxBe,
       "agnDlciPriority": agnDlciPriority,
       "agnDlciStatus": agnDlciStatus,
       "agnDlciSpoofing": agnDlciSpoofing,
       "agnDlciFunnelEnable": agnDlciFunnelEnable,
       "agnDlciRoutingProtocol": agnDlciRoutingProtocol,
       "agnDlciRowStatus": agnDlciRowStatus,
       "agnVoiceSwitching": agnVoiceSwitching,
       "agnVoiceSwConfTable": agnVoiceSwConfTable,
       "agnVoiceSwConfEntry": agnVoiceSwConfEntry,
       "agnVoiceSwConfIdx": agnVoiceSwConfIdx,
       "agnVoiceSwConfZoneId": agnVoiceSwConfZoneId,
       "agnVoiceSwConfNodeId": agnVoiceSwConfNodeId,
       "agnVoiceSwConfNoOfHops": agnVoiceSwConfNoOfHops,
       "agnVoiceSwConfSidt": agnVoiceSwConfSidt,
       "agnVoiceSwConfLidt": agnVoiceSwConfLidt,
       "agnVoiceSwConfDialPlan": agnVoiceSwConfDialPlan,
       "agnVoiceSwConfRtTable": agnVoiceSwConfRtTable,
       "agnVoiceSwConfRtEntry": agnVoiceSwConfRtEntry,
       "agnVoiceSwConfRtDbId": agnVoiceSwConfRtDbId,
       "agnVoiceSwConfRtIdx": agnVoiceSwConfRtIdx,
       "agnVoiceSwConfRtDigits": agnVoiceSwConfRtDigits,
       "agnVoiceSwConfRtAction": agnVoiceSwConfRtAction,
       "agnVoiceSwConfRtData": agnVoiceSwConfRtData,
       "agnVoiceSwConfRtSlot": agnVoiceSwConfRtSlot,
       "agnVoiceSwConfRtPort": agnVoiceSwConfRtPort,
       "agnVoiceSwConfRtDlci": agnVoiceSwConfRtDlci,
       "agnVoiceSwConfRtRowStatus": agnVoiceSwConfRtRowStatus,
       "agnVoiceSwConfRtMaxCalls": agnVoiceSwConfRtMaxCalls,
       "agnVoiceSwConfRtPriority": agnVoiceSwConfRtPriority,
       "agnVoiceSwConfHGTable": agnVoiceSwConfHGTable,
       "agnVoiceSwConfHGEntry": agnVoiceSwConfHGEntry,
       "agnVoiceSwConfHGdbIdx": agnVoiceSwConfHGdbIdx,
       "agnVoiceSwConfHGIdx": agnVoiceSwConfHGIdx,
       "agnVoiceSwConfHGConnect": agnVoiceSwConfHGConnect,
       "agnVoiceSwConfHGExt": agnVoiceSwConfHGExt,
       "agnVoiceSwConfHGExtString": agnVoiceSwConfHGExtString,
       "agnVoiceSwConfHGUserParams": agnVoiceSwConfHGUserParams,
       "agnVoiceSwConfHGStatus": agnVoiceSwConfHGStatus,
       "agnSigProfile": agnSigProfile,
       "agnSigProfileTable": agnSigProfileTable,
       "agnSigProfileEntry": agnSigProfileEntry,
       "agnSigProfileCnfgIdx": agnSigProfileCnfgIdx,
       "agnSigProfileIdx": agnSigProfileIdx,
       "agnSigProfileRxTx": agnSigProfileRxTx,
       "agnSigProfileABCD": agnSigProfileABCD,
       "agnSigProfileEcanActSignal": agnSigProfileEcanActSignal,
       "agnSigProfileEcanRespDelay": agnSigProfileEcanRespDelay,
       "agnSigProfTable": agnSigProfTable,
       "agnSigProfEntry": agnSigProfEntry,
       "agnSigProfCnfgIdx": agnSigProfCnfgIdx,
       "agnSigProfIdx": agnSigProfIdx,
       "agnSigProfName": agnSigProfName,
       "agnSigProfType": agnSigProfType,
       "agnSystemTs": agnSystemTs,
       "systemVoice": systemVoice,
       "systemVoiceTable": systemVoiceTable,
       "systemVoiceEntry": systemVoiceEntry,
       "systemVoiceConfIdx": systemVoiceConfIdx,
       "systemVoiceNationalTone": systemVoiceNationalTone,
       "systemVoicePacketRate": systemVoicePacketRate,
       "systemVoiceFaxSupport": systemVoiceFaxSupport,
       "systemVoiceFaxRate": systemVoiceFaxRate,
       "systemVoiceModemSupport": systemVoiceModemSupport,
       "systemVoiceCoderAndRate": systemVoiceCoderAndRate,
       "systemVoiceEchoCanceler": systemVoiceEchoCanceler,
       "systemVoiceTxGain": systemVoiceTxGain,
       "systemVoiceDtmfRelayMethod": systemVoiceDtmfRelayMethod,
       "systemVoiceDtmfRelayRxPayloadType": systemVoiceDtmfRelayRxPayloadType,
       "systemVoiceDtmfRelayPayloadTypeNeg": systemVoiceDtmfRelayPayloadTypeNeg,
       "systemVoiceDtmfRelayTxPayloadType": systemVoiceDtmfRelayTxPayloadType,
       "systemVoiceCoderTable": systemVoiceCoderTable,
       "systemVoiceCoderEntry": systemVoiceCoderEntry,
       "systemVoiceCoderConfIdx": systemVoiceCoderConfIdx,
       "systemVoiceCoderPriority": systemVoiceCoderPriority,
       "systemVoiceCoderCoderAndRate": systemVoiceCoderCoderAndRate,
       "mdlWanGen": mdlWanGen,
       "statMdlGen": statMdlGen,
       "mdlSInstTable": mdlSInstTable,
       "mdlSInstEntry": mdlSInstEntry,
       "mdlSInstSltIdx": mdlSInstSltIdx,
       "mdlSInstCardType": mdlSInstCardType,
       "mdlSHwVersion": mdlSHwVersion,
       "mdlSSwVersion": mdlSSwVersion,
       "mdlSAlrStatus": mdlSAlrStatus,
       "mdlSAlrStatusAll": mdlSAlrStatusAll,
       "mdlSMaskedAlrStat": mdlSMaskedAlrStat,
       "mdlSMaskedAlrStatAll": mdlSMaskedAlrStatAll,
       "mdlSTstStatusAll": mdlSTstStatusAll,
       "mdlSClearAlrCmd": mdlSClearAlrCmd,
       "mdlSClearAllAlrCmd": mdlSClearAllAlrCmd,
       "mdlSTemperature": mdlSTemperature,
       "mdlSAlrTable": mdlSAlrTable,
       "mdlSAlrEntry": mdlSAlrEntry,
       "mdlSAlrIdx": mdlSAlrIdx,
       "mdlSAlrSltIdx": mdlSAlrSltIdx,
       "mdlSAlrCodeDescription": mdlSAlrCodeDescription,
       "mdlSAlrCode": mdlSAlrCode,
       "mdlSAlrSeverity": mdlSAlrSeverity,
       "mdlSAlrState": mdlSAlrState,
       "mdlSAlrCounter": mdlSAlrCounter,
       "mdlSAlrMask": mdlSAlrMask,
       "mdlSAlrInvert": mdlSAlrInvert,
       "cnfgMdlGen": cnfgMdlGen,
       "mdlCPrgTable": mdlCPrgTable,
       "mdlCPrgEntry": mdlCPrgEntry,
       "mdlCCnfgIdx": mdlCCnfgIdx,
       "mdlCSltIdx": mdlCSltIdx,
       "mdlCPrgCardType": mdlCPrgCardType,
       "mdlCNoOfExternPrt": mdlCNoOfExternPrt,
       "mdlCNoOfInternPrt": mdlCNoOfInternPrt,
       "mdlCWorkMode": mdlCWorkMode,
       "mdlCDhcpClientEnable": mdlCDhcpClientEnable,
       "mdlCRdnExists": mdlCRdnExists,
       "mdlCInterfaces": mdlCInterfaces,
       "cmprMdlGen": cmprMdlGen,
       "mdlCmprTable": mdlCmprTable,
       "mdlCmprEntry": mdlCmprEntry,
       "mdlCmprTypIdx": mdlCmprTypIdx,
       "mdlCmprCnfgIdx": mdlCmprCnfgIdx,
       "mdlCmprVersion": mdlCmprVersion,
       "mdlCmprSltIdx": mdlCmprSltIdx,
       "mdlCmprObj": mdlCmprObj,
       "mdlAlarmsCmprTable": mdlAlarmsCmprTable,
       "mdlAlarmsCmprEntry": mdlAlarmsCmprEntry,
       "mdlAlarmsCmprVersion": mdlAlarmsCmprVersion,
       "mdlAlarmsCmprAlarmSlot": mdlAlarmsCmprAlarmSlot,
       "mdlAlarmsCmprAlarmIdx": mdlAlarmsCmprAlarmIdx,
       "mdlAlarmsCmprObj": mdlAlarmsCmprObj,
       "prtWanGen": prtWanGen,
       "statPrtGen": statPrtGen,
       "prtSInstTable": prtSInstTable,
       "prtSInstEntry": prtSInstEntry,
       "prtSInstSltIdx": prtSInstSltIdx,
       "prtSInstPrtIdx": prtSInstPrtIdx,
       "prtSInstPrtType": prtSInstPrtType,
       "prtSInstIfIndex": prtSInstIfIndex,
       "prtSActiveStatus": prtSActiveStatus,
       "prtSAlrStatus": prtSAlrStatus,
       "prtSMaskedAlrStat": prtSMaskedAlrStat,
       "prtSClearAlrCmd": prtSClearAlrCmd,
       "prtSTestMask": prtSTestMask,
       "prtSTstCmd": prtSTstCmd,
       "prtSTstDuration": prtSTstDuration,
       "prtSBertClrCmd": prtSBertClrCmd,
       "prtSBertTstRslt": prtSBertTstRslt,
       "prtSInterfaceType": prtSInterfaceType,
       "prtSParamStatus": prtSParamStatus,
       "prtSTestMaskXp": prtSTestMaskXp,
       "prtSRdnStatus": prtSRdnStatus,
       "prtSAlrTable": prtSAlrTable,
       "prtSAlrEntry": prtSAlrEntry,
       "prtSAlrIdx": prtSAlrIdx,
       "prtSAlrSltIdx": prtSAlrSltIdx,
       "prtSAlrPrtIdx": prtSAlrPrtIdx,
       "prtSAlrCodeDescription": prtSAlrCodeDescription,
       "prtSAlrCode": prtSAlrCode,
       "prtSAlrSeverity": prtSAlrSeverity,
       "prtSAlrState": prtSAlrState,
       "prtSAlrCounter": prtSAlrCounter,
       "prtSAlrMask": prtSAlrMask,
       "prtSAlrInvert": prtSAlrInvert,
       "prtSAlrCardType": prtSAlrCardType,
       "statisPrtGen": statisPrtGen,
       "prtFrStatis": prtFrStatis,
       "prtFrStatisTable": prtFrStatisTable,
       "prtFrStatisEntry": prtFrStatisEntry,
       "prtFrStatisSltIdx": prtFrStatisSltIdx,
       "prtFrStatisPrtIdx": prtFrStatisPrtIdx,
       "prtFrStatisInvIdx": prtFrStatisInvIdx,
       "prtFrTimeElapsed": prtFrTimeElapsed,
       "prtFrRxTotalFrames": prtFrRxTotalFrames,
       "prtFrTxTotalFrames": prtFrTxTotalFrames,
       "prtFrRxTotalBytes": prtFrRxTotalBytes,
       "prtFrTxTotalBytes": prtFrTxTotalBytes,
       "prtFrRxMngFrames": prtFrRxMngFrames,
       "prtFrTxMngFrames": prtFrTxMngFrames,
       "prtFrRxDeFrames": prtFrRxDeFrames,
       "prtFrTxDeFrames": prtFrTxDeFrames,
       "prtFrRxDcrdCongDeFr": prtFrRxDcrdCongDeFr,
       "prtFrTxDcrdCongDeFr": prtFrTxDcrdCongDeFr,
       "prtFrRxDcrdCongAllFr": prtFrRxDcrdCongAllFr,
       "prtFrTxDcrdCongAllFr": prtFrTxDcrdCongAllFr,
       "prtFrRxFecn": prtFrRxFecn,
       "prtFrTxFecn": prtFrTxFecn,
       "prtFrRxBecn": prtFrRxBecn,
       "prtFrTxBecn": prtFrTxBecn,
       "prtFrRxBeViol": prtFrRxBeViol,
       "prtFrTxBeViol": prtFrTxBeViol,
       "prtFrRxBcViol": prtFrRxBcViol,
       "prtFrTxBcViol": prtFrTxBcViol,
       "prtCrStatis": prtCrStatis,
       "prtCrStatisTable": prtCrStatisTable,
       "prtCrStatisEntry": prtCrStatisEntry,
       "prtCrStatisSltIdx": prtCrStatisSltIdx,
       "prtCrStatisPrtIdx": prtCrStatisPrtIdx,
       "prtCrStatisInvIdx": prtCrStatisInvIdx,
       "prtCrTimeElapsed": prtCrTimeElapsed,
       "prtCrRxTotalCells": prtCrRxTotalCells,
       "prtCrTxTotalCells": prtCrTxTotalCells,
       "prtCrRxDataCells": prtCrRxDataCells,
       "prtCrTxDataCells": prtCrTxDataCells,
       "prtDlciStatis": prtDlciStatis,
       "prtDlciStatisTable": prtDlciStatisTable,
       "prtDlciStatisEntry": prtDlciStatisEntry,
       "prtDlciSltIdx": prtDlciSltIdx,
       "prtDlciPrtIdx": prtDlciPrtIdx,
       "prtDlciIdx": prtDlciIdx,
       "prtDlciRxDeFrames": prtDlciRxDeFrames,
       "prtDlciTxDeFrames": prtDlciTxDeFrames,
       "prtDlciRxDcrdCongDeFr": prtDlciRxDcrdCongDeFr,
       "prtDlciTxDcrdCongDeFr": prtDlciTxDcrdCongDeFr,
       "prtDlciRxDcrdCongAllFr": prtDlciRxDcrdCongAllFr,
       "prtDlciTxDcrdCongAllFr": prtDlciTxDcrdCongAllFr,
       "prtDlciTxFecn": prtDlciTxFecn,
       "prtDlciTxBecn": prtDlciTxBecn,
       "prtDlciRxBeViol": prtDlciRxBeViol,
       "prtDlciTxBeViol": prtDlciTxBeViol,
       "prtDlciRxBcViol": prtDlciRxBcViol,
       "prtDlciTxBcViol": prtDlciTxBcViol,
       "prtT1Statis": prtT1Statis,
       "prtT1FdlMsgTable": prtT1FdlMsgTable,
       "prtT1FdlMsgEntry": prtT1FdlMsgEntry,
       "prtT1FdlMsgSltIdx": prtT1FdlMsgSltIdx,
       "prtT1FdlMsgPrtIdx": prtT1FdlMsgPrtIdx,
       "prtT1FdlMsgFdlTxRx": prtT1FdlMsgFdlTxRx,
       "prtT1FdlMsg": prtT1FdlMsg,
       "cnfgPrtGen": cnfgPrtGen,
       "prtExTsSplitTable": prtExTsSplitTable,
       "prtExTsSplitEntry": prtExTsSplitEntry,
       "prtExTsCnfgIdx": prtExTsCnfgIdx,
       "prtExTsSltIdx": prtExTsSltIdx,
       "prtExTsPrtIdx": prtExTsPrtIdx,
       "prtExTsIdx": prtExTsIdx,
       "prtExTsBit": prtExTsBit,
       "prtExTsIConSlot": prtExTsIConSlot,
       "prtExTsIConPrt": prtExTsIConPrt,
       "prtExTsBitTest": prtExTsBitTest,
       "prtExTsTxSignaling": prtExTsTxSignaling,
       "prtExTsRxSignaling": prtExTsRxSignaling,
       "prtExTsTxIoSignaling": prtExTsTxIoSignaling,
       "prtExTsRxIoSignaling": prtExTsRxIoSignaling,
       "prtCnfgAgenda": prtCnfgAgenda,
       "prtAgendaBehaviourTable": prtAgendaBehaviourTable,
       "prtAgendaBehaviourEntry": prtAgendaBehaviourEntry,
       "prtAgendaBehaviourCnfgIdx": prtAgendaBehaviourCnfgIdx,
       "prtAgendaBehaviourSltIdx": prtAgendaBehaviourSltIdx,
       "prtAgendaBehaviourPrtIdx": prtAgendaBehaviourPrtIdx,
       "prtAgendaBehaviourOnOff": prtAgendaBehaviourOnOff,
       "prtCnfgAgendaTable": prtCnfgAgendaTable,
       "prtCnfgAgendaEntry": prtCnfgAgendaEntry,
       "prtCnfgAgendaCnfgIdx": prtCnfgAgendaCnfgIdx,
       "prtCnfgAgendaSltIdx": prtCnfgAgendaSltIdx,
       "prtCnfgAgendaPrtIdx": prtCnfgAgendaPrtIdx,
       "prtCnfgAgendaDayIdx": prtCnfgAgendaDayIdx,
       "prtCnfgAgendaSesId": prtCnfgAgendaSesId,
       "prtCnfgAgendaFrom": prtCnfgAgendaFrom,
       "prtCnfgAgendaTo": prtCnfgAgendaTo,
       "prtGenCnfgTable": prtGenCnfgTable,
       "prtGenCnfgEntry": prtGenCnfgEntry,
       "prtGenCnfgIdx": prtGenCnfgIdx,
       "prtGenCnfgSltIdx": prtGenCnfgSltIdx,
       "prtGenCnfgPrtIdx": prtGenCnfgPrtIdx,
       "prtGenCnfgLinkToSlot": prtGenCnfgLinkToSlot,
       "prtGenCnfgLinkToPort": prtGenCnfgLinkToPort,
       "prtGenCnfgPortId": prtGenCnfgPortId,
       "prtGenCnfgBusConnection": prtGenCnfgBusConnection,
       "prtGenCnfgInbandMng": prtGenCnfgInbandMng,
       "prtGenCnfgInbandMngRoutProt": prtGenCnfgInbandMngRoutProt,
       "prtGenCnfgProtectionMode": prtGenCnfgProtectionMode,
       "prtGenCnfgConnect": prtGenCnfgConnect,
       "prtGenCnfgSignalingType": prtGenCnfgSignalingType,
       "cmprPrtGen": cmprPrtGen,
       "prtCmprTable": prtCmprTable,
       "prtCmprEntry": prtCmprEntry,
       "prtCmprTypIdx": prtCmprTypIdx,
       "prtCmprCnfgIdx": prtCmprCnfgIdx,
       "prtCmprVersion": prtCmprVersion,
       "prtCmprSltIdx": prtCmprSltIdx,
       "prtCmprPrtIdx": prtCmprPrtIdx,
       "prtCmprObj": prtCmprObj,
       "prtCmprStatisticObj": prtCmprStatisticObj,
       "prtDlciCmprTable": prtDlciCmprTable,
       "prtDlciCmprEntry": prtDlciCmprEntry,
       "prtDlciCmprCnfgIdx": prtDlciCmprCnfgIdx,
       "prtDlciCmprVersion": prtDlciCmprVersion,
       "prtDlciCmprSltIdx": prtDlciCmprSltIdx,
       "prtDlciCmprPrtIdx": prtDlciCmprPrtIdx,
       "prtDlciCmprDlciIdx": prtDlciCmprDlciIdx,
       "prtDlciCmprObj": prtDlciCmprObj,
       "prtAlarmsCmprTable": prtAlarmsCmprTable,
       "prtAlarmsCmprEntry": prtAlarmsCmprEntry,
       "prtAlarmsCmprVersion": prtAlarmsCmprVersion,
       "prtAlarmsCmprAlarmSlot": prtAlarmsCmprAlarmSlot,
       "prtAlarmsCmprAlarmPort": prtAlarmsCmprAlarmPort,
       "prtAlarmsCmprAlarmIdx": prtAlarmsCmprAlarmIdx,
       "prtAlarmsCmprObj": prtAlarmsCmprObj,
       "mapWanGen": mapWanGen,
       "agnLinkMapTable": agnLinkMapTable,
       "agnLinkMapEntry": agnLinkMapEntry,
       "mapLinkId": mapLinkId,
       "mapLinkSltIdx": mapLinkSltIdx,
       "mapLinkPrtIdx": mapLinkPrtIdx,
       "mapLinkStatus": mapLinkStatus,
       "diverseIfWanGen": diverseIfWanGen,
       "muxHub": muxHub,
       "muxHubEvents": muxHubEvents,
       "alarmsTrap": alarmsTrap,
       "sanityTrap": sanityTrap,
       "cnfgFlipTrap": cnfgFlipTrap,
       "flipDbChangeTrap": flipDbChangeTrap,
       "statusChangedTrap": statusChangedTrap,
       "agnMux": agnMux,
       "mdlMux": mdlMux,
       "cnfgMdlMux": cnfgMdlMux,
       "mdlPbxFramerCnfg": mdlPbxFramerCnfg,
       "mdlPbxFramerCnfgTable": mdlPbxFramerCnfgTable,
       "mdlPbxFramerCnfgEntry": mdlPbxFramerCnfgEntry,
       "mdlPbxFraCnfgIdx": mdlPbxFraCnfgIdx,
       "mdlPbxFraSltIdx": mdlPbxFraSltIdx,
       "mdlPbxFraEnhEcho": mdlPbxFraEnhEcho,
       "mdlPbxFraTSGroupAss": mdlPbxFraTSGroupAss,
       "mdlPbxFraSignalMode": mdlPbxFraSignalMode,
       "mdlPbxFraSignalVector": mdlPbxFraSignalVector,
       "mdlPbxFraSignalMask": mdlPbxFraSignalMask,
       "mdlPbxFraFramerSlot": mdlPbxFraFramerSlot,
       "mdlPbxFraSignaling": mdlPbxFraSignaling,
       "mdlPbxFraTransSigTs": mdlPbxFraTransSigTs,
       "mdlProtIpTable": mdlProtIpTable,
       "mdlProtIpEntry": mdlProtIpEntry,
       "mdlProtIpCnfgIdx": mdlProtIpCnfgIdx,
       "mdlProtIpSlotIdx": mdlProtIpSlotIdx,
       "mdlProtIpAddress": mdlProtIpAddress,
       "mdlProtIpRowStatus": mdlProtIpRowStatus,
       "statMdlMux": statMdlMux,
       "mdlStatTable": mdlStatTable,
       "mdlStatEntry": mdlStatEntry,
       "mdlStatSltIdx": mdlStatSltIdx,
       "mdlStatHostIP": mdlStatHostIP,
       "mdlStatHostMask": mdlStatHostMask,
       "mdlStatDefaultGateway": mdlStatDefaultGateway,
       "prtMux": prtMux,
       "statPrtMux": statPrtMux,
       "prtSExHsfStatTable": prtSExHsfStatTable,
       "prtSExHsfStatEntry": prtSExHsfStatEntry,
       "prtSExHsfSltIdx": prtSExHsfSltIdx,
       "prtSExHsfPrtIdx": prtSExHsfPrtIdx,
       "prtSExHsfInterfaceTyp": prtSExHsfInterfaceTyp,
       "prtSExHsfRts": prtSExHsfRts,
       "prtIsdnStatusTable": prtIsdnStatusTable,
       "prtIsdnStatusEntry": prtIsdnStatusEntry,
       "prtIsdnStatusDspMode": prtIsdnStatusDspMode,
       "prtIsdnStatusCallState": prtIsdnStatusCallState,
       "prtIsdnStatusCallingNumber": prtIsdnStatusCallingNumber,
       "prtIsdnStatusCalledNumber": prtIsdnStatusCalledNumber,
       "prtIsdnStatusCalledIP": prtIsdnStatusCalledIP,
       "prtIsdnStatusCallDirection": prtIsdnStatusCallDirection,
       "cnfgPrtMux": cnfgPrtMux,
       "prtClCnfg": prtClCnfg,
       "prtExClCnfgTable": prtExClCnfgTable,
       "prtExClCnfgEntry": prtExClCnfgEntry,
       "prtExClCnfgIdx": prtExClCnfgIdx,
       "prtExClSltIdx": prtExClSltIdx,
       "prtExClPrtIdx": prtExClPrtIdx,
       "prtExClUsage": prtExClUsage,
       "prtExClRate": prtExClRate,
       "prtExClDataBits": prtExClDataBits,
       "prtExClParity": prtExClParity,
       "prtExClStopBits": prtExClStopBits,
       "prtExClRoutingProtocol": prtExClRoutingProtocol,
       "prtExClEnabled": prtExClEnabled,
       "prtPh1MlCnfg": prtPh1MlCnfg,
       "prtExPh1MlCnfgTable": prtExPh1MlCnfgTable,
       "prtExPh1MlCnfgEntry": prtExPh1MlCnfgEntry,
       "prtExPh1MlCnfgIdx": prtExPh1MlCnfgIdx,
       "prtExPh1MlSltIdx": prtExPh1MlSltIdx,
       "prtExPh1MlPrtIdx": prtExPh1MlPrtIdx,
       "prtExPh1MlConnect": prtExPh1MlConnect,
       "prtExPh1MlLineType": prtExPh1MlLineType,
       "prtExPh1MlLineCode": prtExPh1MlLineCode,
       "prtExPh1MlLineLen": prtExPh1MlLineLen,
       "prtExPh1MlRestoreTime": prtExPh1MlRestoreTime,
       "prtExPh1MlTxGain": prtExPh1MlTxGain,
       "prtExPh1MlRxSensitivity": prtExPh1MlRxSensitivity,
       "prtExPh1MlIdleCode": prtExPh1MlIdleCode,
       "prtExPh1MlTdmTrunk": prtExPh1MlTdmTrunk,
       "prtExPh1MlClkMode": prtExPh1MlClkMode,
       "prtExPh1MlMfClkSrcSlt": prtExPh1MlMfClkSrcSlt,
       "prtExPh1MlMfClkSrcPrt": prtExPh1MlMfClkSrcPrt,
       "prtExPh1MlFdlType": prtExPh1MlFdlType,
       "prtExPh1MlInbandMng": prtExPh1MlInbandMng,
       "prtExPh1MlInbandMngRate": prtExPh1MlInbandMngRate,
       "prtExPh1MlRedundType": prtExPh1MlRedundType,
       "prtExPh1MlRedundSlot": prtExPh1MlRedundSlot,
       "prtExPh1MlRedundPort": prtExPh1MlRedundPort,
       "prtExPh1MlRedundRecTime": prtExPh1MlRedundRecTime,
       "prtExPh1MlInbandMngRoutProt": prtExPh1MlInbandMngRoutProt,
       "prtExPh1MlIfType": prtExPh1MlIfType,
       "prtExPh1MlMultiplier": prtExPh1MlMultiplier,
       "prtExPh1MlSupportedTS": prtExPh1MlSupportedTS,
       "prtExPh1MlImpedance": prtExPh1MlImpedance,
       "prtExPh1MlQ50BwControl": prtExPh1MlQ50BwControl,
       "prtExPh1MlQ50SignalPair": prtExPh1MlQ50SignalPair,
       "prtExPh1MlInternalSwitch": prtExPh1MlInternalSwitch,
       "prtExPh1MlSigService": prtExPh1MlSigService,
       "prtExPh1MlFragmentSize": prtExPh1MlFragmentSize,
       "prtExPh1MlTsTable": prtExPh1MlTsTable,
       "prtExPh1MlTsEntry": prtExPh1MlTsEntry,
       "prtExPh1MlTsCnfgIdx": prtExPh1MlTsCnfgIdx,
       "prtExPh1MlTsSltIdx": prtExPh1MlTsSltIdx,
       "prtExPh1MlTsPrtIdx": prtExPh1MlTsPrtIdx,
       "prtExPh1MlTsIdx": prtExPh1MlTsIdx,
       "prtExPh1MlTsIConSlot": prtExPh1MlTsIConSlot,
       "prtExPh1MlTsIConPrt": prtExPh1MlTsIConPrt,
       "prtExPh1MlTsIConTs": prtExPh1MlTsIConTs,
       "prtExPh1MlTsExt": prtExPh1MlTsExt,
       "prtExPh1MlTsTest": prtExPh1MlTsTest,
       "prtExPh1MlTsType": prtExPh1MlTsType,
       "prtExPh1MlTsBundle": prtExPh1MlTsBundle,
       "prtExPh1MlTsTestDuration": prtExPh1MlTsTestDuration,
       "prtExPh1MlTsSubChType": prtExPh1MlTsSubChType,
       "prtExPh1MlTsSubChMask": prtExPh1MlTsSubChMask,
       "prtExPh1MlTsChRate": prtExPh1MlTsChRate,
       "prtExPh1MlTsByteReversal": prtExPh1MlTsByteReversal,
       "prtExPh1MlTsSigProfile": prtExPh1MlTsSigProfile,
       "prtInPh1MlCnfgTable": prtInPh1MlCnfgTable,
       "prtInPh1MlCnfgEntry": prtInPh1MlCnfgEntry,
       "prtInPh1MlCnfgIdx": prtInPh1MlCnfgIdx,
       "prtInPh1MlSltType": prtInPh1MlSltType,
       "prtInPh1MlPrtIdx": prtInPh1MlPrtIdx,
       "prtInPh1MlConnect": prtInPh1MlConnect,
       "prtInPh1MlRate": prtInPh1MlRate,
       "prtInPh1MlProtocol": prtInPh1MlProtocol,
       "prtInPh1MlConnectionTyp": prtInPh1MlConnectionTyp,
       "prtInPh1MlCongResponse": prtInPh1MlCongResponse,
       "prtInPh1MlCongLevel": prtInPh1MlCongLevel,
       "prtInPh1MlTc": prtInPh1MlTc,
       "prtInPh1MlFlowControl": prtInPh1MlFlowControl,
       "prtInPh1MlSegment": prtInPh1MlSegment,
       "prtInPh1MlFrMngProt": prtInPh1MlFrMngProt,
       "prtInPh1MlEnqPeriod": prtInPh1MlEnqPeriod,
       "prtInPh1MlFullRptPeriod": prtInPh1MlFullRptPeriod,
       "prtInPh1MlFrWindowSize": prtInPh1MlFrWindowSize,
       "prtInPh1MlErrorsThreshold": prtInPh1MlErrorsThreshold,
       "prtInPh1MlMaxIdleTime": prtInPh1MlMaxIdleTime,
       "prtInPh1MlBearerCh": prtInPh1MlBearerCh,
       "prtInPh1MlAssociatedExCh": prtInPh1MlAssociatedExCh,
       "prtInPh1MlClockEncoding": prtInPh1MlClockEncoding,
       "prtInPh1MlMinSeparators": prtInPh1MlMinSeparators,
       "prtInPh1MlCcittCrc": prtInPh1MlCcittCrc,
       "prtInPh1MlFrameSeparator": prtInPh1MlFrameSeparator,
       "prtInPh1MlDlciTable": prtInPh1MlDlciTable,
       "prtInPh1MlDlciEntry": prtInPh1MlDlciEntry,
       "prtInPh1MlDlciCnfgIdx": prtInPh1MlDlciCnfgIdx,
       "prtInPh1MlDlciSltIdx": prtInPh1MlDlciSltIdx,
       "prtInPh1MlDlciPrtIdx": prtInPh1MlDlciPrtIdx,
       "prtInPh1MlDlciIdx": prtInPh1MlDlciIdx,
       "prtInPh1MlDlciValid": prtInPh1MlDlciValid,
       "prtInPh1MlDlciIConSlt": prtInPh1MlDlciIConSlt,
       "prtInPh1MlDlciIConPrt": prtInPh1MlDlciIConPrt,
       "prtInPh1MlDlciIConDlci": prtInPh1MlDlciIConDlci,
       "prtInPh1MlDlciTxBc": prtInPh1MlDlciTxBc,
       "prtInPh1MlDlciTxBe": prtInPh1MlDlciTxBe,
       "prtInPh1MlDlciRxBc": prtInPh1MlDlciRxBc,
       "prtInPh1MlDlciRxBe": prtInPh1MlDlciRxBe,
       "prtInPh1MlDlciPriority": prtInPh1MlDlciPriority,
       "prtInPh1MlDlciStatus": prtInPh1MlDlciStatus,
       "prtPhMlCnfgTable": prtPhMlCnfgTable,
       "prtPhMlCnfgEntry": prtPhMlCnfgEntry,
       "prtPhMlCnfgIdx": prtPhMlCnfgIdx,
       "prtPhMlSltIdx": prtPhMlSltIdx,
       "prtPhMlPrtIdx": prtPhMlPrtIdx,
       "prtPhMlConnect": prtPhMlConnect,
       "prtPhMlRate": prtPhMlRate,
       "prtPhMlCAS": prtPhMlCAS,
       "prtPhMlClockMode": prtPhMlClockMode,
       "prtPhMlSatBuffer": prtPhMlSatBuffer,
       "prtPhMlDialProcess": prtPhMlDialProcess,
       "prtPhMlSyncRestore": prtPhMlSyncRestore,
       "prtPhMlBus": prtPhMlBus,
       "prtPhMlMfSyncSlot": prtPhMlMfSyncSlot,
       "prtPhMlClockSource": prtPhMlClockSource,
       "prtPhMlErrCorrection": prtPhMlErrCorrection,
       "prtPhMlCorrectionMode": prtPhMlCorrectionMode,
       "prtPhMlControlSignals": prtPhMlControlSignals,
       "prtPhMlInterfaceType": prtPhMlInterfaceType,
       "prtPhMlClockPolarity": prtPhMlClockPolarity,
       "prtPhPlCnfg": prtPhPlCnfg,
       "prtExPhPlCnfgTable": prtExPhPlCnfgTable,
       "prtExPhPlCnfgEntry": prtExPhPlCnfgEntry,
       "prtExPhPlCnfgIdx": prtExPhPlCnfgIdx,
       "prtExPhPlSltIdx": prtExPhPlSltIdx,
       "prtExPhPlPrtIdx": prtExPhPlPrtIdx,
       "prtExPhPlConnect": prtExPhPlConnect,
       "prtExPhPlHRate": prtExPhPlHRate,
       "prtExPhPlLRate": prtExPhPlLRate,
       "prtExPhPlProtocol": prtExPhPlProtocol,
       "prtExPhPlConnectionTyp": prtExPhPlConnectionTyp,
       "prtExPhPlClkMode": prtExPhPlClkMode,
       "prtExPhPlDceClkSrc": prtExPhPlDceClkSrc,
       "prtExPhPlCongResponse": prtExPhPlCongResponse,
       "prtExPhPlCongLevel": prtExPhPlCongLevel,
       "prtExPhPlTc": prtExPhPlTc,
       "prtExPhPlFlowControl": prtExPhPlFlowControl,
       "prtExPhPlDcdRts": prtExPhPlDcdRts,
       "prtExPhPlDcdRtsControlPath": prtExPhPlDcdRtsControlPath,
       "prtExPhPlDataBits": prtExPhPlDataBits,
       "prtExPhPlParity": prtExPhPlParity,
       "prtExPhPlStopBits": prtExPhPlStopBits,
       "prtExPhPlLXon": prtExPhPlLXon,
       "prtExPhPlLXoff": prtExPhPlLXoff,
       "prtExPhPlFrMngProt": prtExPhPlFrMngProt,
       "prtExPhPlEnqPeriod": prtExPhPlEnqPeriod,
       "prtExPhPlFullRptPeriod": prtExPhPlFullRptPeriod,
       "prtExPhPlFrWindowSize": prtExPhPlFrWindowSize,
       "prtExPhPlErrorsThreshold": prtExPhPlErrorsThreshold,
       "prtExPhPlPvcCreateMsg": prtExPhPlPvcCreateMsg,
       "prtExPhPlCllmMsg": prtExPhPlCllmMsg,
       "prtExPhPlProtDelayLevel": prtExPhPlProtDelayLevel,
       "prtExPhPlClockEncoding": prtExPhPlClockEncoding,
       "prtExPhPlMinSeparators": prtExPhPlMinSeparators,
       "prtExPhPlCcittCrc": prtExPhPlCcittCrc,
       "prtExPhPlFrameSeparator": prtExPhPlFrameSeparator,
       "prtExPhPlIdleCode": prtExPhPlIdleCode,
       "prtExPhPlJitter": prtExPhPlJitter,
       "prtExPhPlDlciTable": prtExPhPlDlciTable,
       "prtExPhPlDlciEntry": prtExPhPlDlciEntry,
       "prtExPhPlDlciCnfgIdx": prtExPhPlDlciCnfgIdx,
       "prtExPhPlDlciSltIdx": prtExPhPlDlciSltIdx,
       "prtExPhPlDlciPrtIdx": prtExPhPlDlciPrtIdx,
       "prtExPhPlDlciIdx": prtExPhPlDlciIdx,
       "prtExPhPlDlciValid": prtExPhPlDlciValid,
       "prtExPhPlDlciIConSlt": prtExPhPlDlciIConSlt,
       "prtExPhPlDlciIConPrt": prtExPhPlDlciIConPrt,
       "prtExPhPlDlciIConDlci": prtExPhPlDlciIConDlci,
       "prtExPhPlDlciTxBc": prtExPhPlDlciTxBc,
       "prtExPhPlDlciTxBe": prtExPhPlDlciTxBe,
       "prtExPhPlDlciRxBc": prtExPhPlDlciRxBc,
       "prtExPhPlDlciRxBe": prtExPhPlDlciRxBe,
       "prtExPhPlDlciPriority": prtExPhPlDlciPriority,
       "prtExPhPlDlciStatus": prtExPhPlDlciStatus,
       "prtExPhPlModemTable": prtExPhPlModemTable,
       "prtExPhPlModemEntry": prtExPhPlModemEntry,
       "prtExPhPlModemCnfgIdx": prtExPhPlModemCnfgIdx,
       "prtExPhPlModemSltIdx": prtExPhPlModemSltIdx,
       "prtExPhPlModemPrtIdx": prtExPhPlModemPrtIdx,
       "prtExPhPlModemStatus": prtExPhPlModemStatus,
       "prtExPhPlModemActivate": prtExPhPlModemActivate,
       "prtExPhPlModemMaxIdleTime": prtExPhPlModemMaxIdleTime,
       "prtExPhPlModemTimeBtwnCalls": prtExPhPlModemTimeBtwnCalls,
       "prtExPhPlModemCallDelay": prtExPhPlModemCallDelay,
       "prtLs2Cnfg": prtLs2Cnfg,
       "prtExLs2CnfgTable": prtExLs2CnfgTable,
       "prtExLs2CnfgEntry": prtExLs2CnfgEntry,
       "prtExLs2CnfgIdx": prtExLs2CnfgIdx,
       "prtExLs2SltIdx": prtExLs2SltIdx,
       "prtExLs2PrtIdx": prtExLs2PrtIdx,
       "prtExLs2Connect": prtExLs2Connect,
       "prtExLs2Rate": prtExLs2Rate,
       "prtExLs2ClkMode": prtExLs2ClkMode,
       "prtExLs2Cts": prtExLs2Cts,
       "prtExLs2Dcd": prtExLs2Dcd,
       "prtExLs2EnvIdx": prtExLs2EnvIdx,
       "prtInLs2CnfgTable": prtInLs2CnfgTable,
       "prtInLs2CnfgEntry": prtInLs2CnfgEntry,
       "prtInLs2CnfgIdx": prtInLs2CnfgIdx,
       "prtInLs2SltIdx": prtInLs2SltIdx,
       "prtInLs2PrtIdx": prtInLs2PrtIdx,
       "prtInLs2Connect": prtInLs2Connect,
       "prtInLs2Group": prtInLs2Group,
       "prtInLs2Member": prtInLs2Member,
       "prtInLs2LinkTo": prtInLs2LinkTo,
       "prtInLs2EnvAssign": prtInLs2EnvAssign,
       "prtVc2CnfgTable": prtVc2CnfgTable,
       "prtVc2CnfgEntry": prtVc2CnfgEntry,
       "prtVc2CnfgIdx": prtVc2CnfgIdx,
       "prtVc2SltIdx": prtVc2SltIdx,
       "prtVc2PrtIdx": prtVc2PrtIdx,
       "prtExVc2Connect": prtExVc2Connect,
       "prtExVc2TransGain": prtExVc2TransGain,
       "prtExVc2ReceiveGain": prtExVc2ReceiveGain,
       "prtExVc2Wire": prtExVc2Wire,
       "prtExVc2CodingLaw": prtExVc2CodingLaw,
       "prtExVc2Sig": prtExVc2Sig,
       "prtExVc2Oos": prtExVc2Oos,
       "prtExVc2LinkTo": prtExVc2LinkTo,
       "prtExVc2OperMode": prtExVc2OperMode,
       "prtExVc2SigProfile": prtExVc2SigProfile,
       "prtExVc2CallEnable": prtExVc2CallEnable,
       "prtExVc2R2Delay": prtExVc2R2Delay,
       "prtExVc2CasStd": prtExVc2CasStd,
       "prtExVc2EchoCanceler": prtExVc2EchoCanceler,
       "prtExVc2IfType": prtExVc2IfType,
       "prtExVc2Encoding": prtExVc2Encoding,
       "prtExVc2TxBitCode": prtExVc2TxBitCode,
       "prtExVc2RxBitOutput": prtExVc2RxBitOutput,
       "prtExVc2MeterRate": prtExVc2MeterRate,
       "prtExVc2IfSignaling": prtExVc2IfSignaling,
       "prtExVc2SeizeAck": prtExVc2SeizeAck,
       "prtExVc2EandMType": prtExVc2EandMType,
       "prtExVc2RemType": prtExVc2RemType,
       "prtExVc2ConvTime": prtExVc2ConvTime,
       "prtExVc2SigFeedback": prtExVc2SigFeedback,
       "prtExVc2EchoCancelerModule": prtExVc2EchoCancelerModule,
       "prtExVc2ReversePolarity": prtExVc2ReversePolarity,
       "prtExVc2RingerFrequency": prtExVc2RingerFrequency,
       "prtExVc2SigService": prtExVc2SigService,
       "prtExVc2CallerIdEnable": prtExVc2CallerIdEnable,
       "prtExVc2CompressMethod": prtExVc2CompressMethod,
       "prtExVc2ObMode": prtExVc2ObMode,
       "prtExVc2VAD": prtExVc2VAD,
       "prtExVc2NoiseLevelForVAD": prtExVc2NoiseLevelForVAD,
       "prtExVc2WesternSigMode": prtExVc2WesternSigMode,
       "prtExVc2BusProtectionPoint": prtExVc2BusProtectionPoint,
       "prtExVc2ImpedanceStandard": prtExVc2ImpedanceStandard,
       "prtHsfCnfgTable": prtHsfCnfgTable,
       "prtHsfCnfgEntry": prtHsfCnfgEntry,
       "prtHsfCnfgIdx": prtHsfCnfgIdx,
       "prtHsfSltIdx": prtHsfSltIdx,
       "prtHsfPrtIdx": prtHsfPrtIdx,
       "prtExHsfConnect": prtExHsfConnect,
       "prtExHsfRate": prtExHsfRate,
       "prtExHsfClkMode": prtExHsfClkMode,
       "prtExHsfCts": prtExHsfCts,
       "prtExHsfFifoSize": prtExHsfFifoSize,
       "prtExHsfLinkTo": prtExHsfLinkTo,
       "prtExHsfOperMode": prtExHsfOperMode,
       "prtExHsfInbandLoopback": prtExHsfInbandLoopback,
       "prtExHsfClkPolarity": prtExHsfClkPolarity,
       "prtExHsfControlSignal": prtExHsfControlSignal,
       "prtExHsfBcastRingSrcPort": prtExHsfBcastRingSrcPort,
       "prtHs4Cnfg": prtHs4Cnfg,
       "prtExHs4CnfgTable": prtExHs4CnfgTable,
       "prtExHs4CnfgEntry": prtExHs4CnfgEntry,
       "prtExHs4CnfgIdx": prtExHs4CnfgIdx,
       "prtExHs4SltIdx": prtExHs4SltIdx,
       "prtExHs4PrtIdx": prtExHs4PrtIdx,
       "prtExHs4Connect": prtExHs4Connect,
       "prtExHs4LineType": prtExHs4LineType,
       "prtExHs4LineCode": prtExHs4LineCode,
       "prtExHs4LineLen": prtExHs4LineLen,
       "prtExHs4RestoreT": prtExHs4RestoreT,
       "prtExHs4OosSig": prtExHs4OosSig,
       "prtExHs4OosCode": prtExHs4OosCode,
       "prtExHs4IdleCode": prtExHs4IdleCode,
       "prtExHs4MfClkSrcSlt": prtExHs4MfClkSrcSlt,
       "prtExHs4MfClkSrcPrt": prtExHs4MfClkSrcPrt,
       "prtExHs4TsCnfgTable": prtExHs4TsCnfgTable,
       "prtExHs4TsEntry": prtExHs4TsEntry,
       "prtExHs4TsCnfgIdx": prtExHs4TsCnfgIdx,
       "prtExHs4TsSltIdx": prtExHs4TsSltIdx,
       "prtExHs4TsPrtIdx": prtExHs4TsPrtIdx,
       "prtExHs4TsIdx": prtExHs4TsIdx,
       "prtExHs4TsIConSlot": prtExHs4TsIConSlot,
       "prtExHs4TsIConPrt": prtExHs4TsIConPrt,
       "prtExHs4TsIConTs": prtExHs4TsIConTs,
       "prtHsiCnfg": prtHsiCnfg,
       "prtExHsiCnfgTable": prtExHsiCnfgTable,
       "prtExHsiCnfgEntry": prtExHsiCnfgEntry,
       "prtExHsiCnfgIdx": prtExHsiCnfgIdx,
       "prtExHsiSltIdx": prtExHsiSltIdx,
       "prtExHsiPrtIdx": prtExHsiPrtIdx,
       "prtExHsiConnect": prtExHsiConnect,
       "prtExHsiRate": prtExHsiRate,
       "prtExHsiLinkTo": prtExHsiLinkTo,
       "prtExHsiInterface": prtExHsiInterface,
       "prtExHsiActType": prtExHsiActType,
       "prtInHsiCnfgTable": prtInHsiCnfgTable,
       "prtInHsiCnfgEntry": prtInHsiCnfgEntry,
       "prtInHsiCnfgIdx": prtInHsiCnfgIdx,
       "prtInHsiSltIdx": prtInHsiSltIdx,
       "prtInHsiPrtIdx": prtInHsiPrtIdx,
       "prtInHsiConnect": prtInHsiConnect,
       "prtInHsiRate": prtInHsiRate,
       "prtInHsiConcentratedTo": prtInHsiConcentratedTo,
       "prtPVc4Cnfg": prtPVc4Cnfg,
       "prtExPVc4CnfgTable": prtExPVc4CnfgTable,
       "prtExPVc4CnfgEntry": prtExPVc4CnfgEntry,
       "prtExPVc4CnfgIdx": prtExPVc4CnfgIdx,
       "prtExPVc4SltIdx": prtExPVc4SltIdx,
       "prtExPVc4PrtIdx": prtExPVc4PrtIdx,
       "prtExPVc4PrtType": prtExPVc4PrtType,
       "prtExPVc4Connect": prtExPVc4Connect,
       "prtExPVc4IfType": prtExPVc4IfType,
       "prtExPVc4TxGain": prtExPVc4TxGain,
       "prtExPVc4RxGain": prtExPVc4RxGain,
       "prtExPVc4MaxRate": prtExPVc4MaxRate,
       "prtExPVc4Tc": prtExPVc4Tc,
       "prtExPVc4Oos": prtExPVc4Oos,
       "prtExPVc4EchoCanceler": prtExPVc4EchoCanceler,
       "prtExPVc4VarDelay": prtExPVc4VarDelay,
       "prtExPVc4CongLevel": prtExPVc4CongLevel,
       "prtExPVc4Wire": prtExPVc4Wire,
       "prtExPVc4ExtensionType": prtExPVc4ExtensionType,
       "prtExPVc4ExtensionNumber": prtExPVc4ExtensionNumber,
       "prtExPVc4OutPulsing": prtExPVc4OutPulsing,
       "prtExPVc4HuntGroupMb": prtExPVc4HuntGroupMb,
       "prtExPVc4HuntGroupIdx": prtExPVc4HuntGroupIdx,
       "prtExPVc4AutoFaxMode": prtExPVc4AutoFaxMode,
       "prtExPVc4FaxRate": prtExPVc4FaxRate,
       "prtExPVc4SeizeAck": prtExPVc4SeizeAck,
       "prtExPVc4SignalingProtocol": prtExPVc4SignalingProtocol,
       "prtExPVc4DelayStart": prtExPVc4DelayStart,
       "prtExPVc4WinkMinDuration": prtExPVc4WinkMinDuration,
       "prtExPVc4WinkMaxDuration": prtExPVc4WinkMaxDuration,
       "prtExPVc4GenerateTone": prtExPVc4GenerateTone,
       "prtExPVc4CodingLaw": prtExPVc4CodingLaw,
       "prtExPVc4GenerateRingBack": prtExPVc4GenerateRingBack,
       "prtExPVc4ChannelId": prtExPVc4ChannelId,
       "prtExPVc4PortConnection": prtExPVc4PortConnection,
       "prtExPVc4CoderAndRate": prtExPVc4CoderAndRate,
       "prtExPVc4DestinationNum": prtExPVc4DestinationNum,
       "prtExPVc4DtmfRelay": prtExPVc4DtmfRelay,
       "prtExPVc4DiscOnSilence": prtExPVc4DiscOnSilence,
       "prtExPVc4DynamicJitter": prtExPVc4DynamicJitter,
       "prtExPVc4EandMType": prtExPVc4EandMType,
       "prtExPVc4Rate": prtExPVc4Rate,
       "prtExPVc4FrameSize": prtExPVc4FrameSize,
       "prtExPVc4MultiplexInterval": prtExPVc4MultiplexInterval,
       "prtExPVc4TransportProtocol": prtExPVc4TransportProtocol,
       "prtExPVc4MultiFreqRelay": prtExPVc4MultiFreqRelay,
       "prtExPVc4MinPulseWidth": prtExPVc4MinPulseWidth,
       "prtExPVc4MinPowerLevel": prtExPVc4MinPowerLevel,
       "prtExPVc4SuperTandem": prtExPVc4SuperTandem,
       "prtExPVc4DestIp": prtExPVc4DestIp,
       "prtExPVc4DestBundle": prtExPVc4DestBundle,
       "prtExPVc4SrcIpAddress": prtExPVc4SrcIpAddress,
       "prtExPVc4SrcIpMask": prtExPVc4SrcIpMask,
       "prtExPVc4DefaultGateway": prtExPVc4DefaultGateway,
       "prtExPVc4SigPacketInterval": prtExPVc4SigPacketInterval,
       "prtExPVc4DlciTable": prtExPVc4DlciTable,
       "prtExPVc4DlciEntry": prtExPVc4DlciEntry,
       "prtExPVc4DlciCnfgIdx": prtExPVc4DlciCnfgIdx,
       "prtExPVc4DlciSltIdx": prtExPVc4DlciSltIdx,
       "prtExPVc4DlciPrtIdx": prtExPVc4DlciPrtIdx,
       "prtExPVc4DlciValid": prtExPVc4DlciValid,
       "prtExPVc4DlciIConSlt": prtExPVc4DlciIConSlt,
       "prtExPVc4DlciIConPrt": prtExPVc4DlciIConPrt,
       "prtExPVc4DlciIConDlci": prtExPVc4DlciIConDlci,
       "prtExPVc4DlciTxBc": prtExPVc4DlciTxBc,
       "prtExPVc4DlciTxBe": prtExPVc4DlciTxBe,
       "prtExPVc4DlciRxBc": prtExPVc4DlciRxBc,
       "prtExPVc4DlciRxBe": prtExPVc4DlciRxBe,
       "prtExPVc4DlciPriority": prtExPVc4DlciPriority,
       "prtExPVc4DlciStatus": prtExPVc4DlciStatus,
       "prtHsrCnfg": prtHsrCnfg,
       "prtExHsrCnfgTable": prtExHsrCnfgTable,
       "prtExHsrCnfgEntry": prtExHsrCnfgEntry,
       "prtExHsrCnfgIdx": prtExHsrCnfgIdx,
       "prtExHsrSltIdx": prtExHsrSltIdx,
       "prtExHsrPrtIdx": prtExHsrPrtIdx,
       "prtExHsrConnect": prtExHsrConnect,
       "prtExHsrProtocol": prtExHsrProtocol,
       "prtExHsrRate": prtExHsrRate,
       "prtExHsrDataBits": prtExHsrDataBits,
       "prtExHsrParity": prtExHsrParity,
       "prtExHsrStopBits": prtExHsrStopBits,
       "prtExHsrCts": prtExHsrCts,
       "prtExHsrClkMode": prtExHsrClkMode,
       "prtExHsrLinkTo": prtExHsrLinkTo,
       "prtExHsrDcdDsr": prtExHsrDcdDsr,
       "prtExHsrOperMode": prtExHsrOperMode,
       "prtExHsrRtsDtr": prtExHsrRtsDtr,
       "prtExHsrLlbEnable": prtExHsrLlbEnable,
       "prtExHsrRlbEnable": prtExHsrRlbEnable,
       "prtExHsrRateAdapt": prtExHsrRateAdapt,
       "prtExHsrRemoteModem": prtExHsrRemoteModem,
       "prtExHsrEncapsMode": prtExHsrEncapsMode,
       "prtMbeCnfg": prtMbeCnfg,
       "prtExMbeCnfgTable": prtExMbeCnfgTable,
       "prtExMbeCnfgEntry": prtExMbeCnfgEntry,
       "prtExMbeCnfgIdx": prtExMbeCnfgIdx,
       "prtExMbeSltIdx": prtExMbeSltIdx,
       "prtExMbePrtIdx": prtExMbePrtIdx,
       "prtExMbeLan": prtExMbeLan,
       "prtInMbeCnfgTable": prtInMbeCnfgTable,
       "prtInMbeCnfgEntry": prtInMbeCnfgEntry,
       "prtInMbeCnfgIdx": prtInMbeCnfgIdx,
       "prtInMbeSltIdx": prtInMbeSltIdx,
       "prtInMbePrtIdx": prtInMbePrtIdx,
       "prtInMbeConnect": prtInMbeConnect,
       "prtInMbeRate": prtInMbeRate,
       "prtInMbeLinkTo": prtInMbeLinkTo,
       "prtTreCnfg": prtTreCnfg,
       "prtExTreCnfgTable": prtExTreCnfgTable,
       "prtExTreCnfgEntry": prtExTreCnfgEntry,
       "prtExTreCnfgIdx": prtExTreCnfgIdx,
       "prtExTreSltIdx": prtExTreSltIdx,
       "prtExTrePrtIdx": prtExTrePrtIdx,
       "prtExTreLan": prtExTreLan,
       "prtExTreLanRate": prtExTreLanRate,
       "prtInTreCnfgTable": prtInTreCnfgTable,
       "prtInTreCnfgEntry": prtInTreCnfgEntry,
       "prtInTreCnfgIdx": prtInTreCnfgIdx,
       "prtInTreSltIdx": prtInTreSltIdx,
       "prtInTrePrtIdx": prtInTrePrtIdx,
       "prtInTreConnect": prtInTreConnect,
       "prtInTreRate": prtInTreRate,
       "prtInTreLinkTo": prtInTreLinkTo,
       "prtLs6Cnfg": prtLs6Cnfg,
       "prtExLs6CnfgTable": prtExLs6CnfgTable,
       "prtExLs6CnfgEntry": prtExLs6CnfgEntry,
       "prtExLs6CnfgIdx": prtExLs6CnfgIdx,
       "prtExLs6SltIdx": prtExLs6SltIdx,
       "prtExLs6PrtIdx": prtExLs6PrtIdx,
       "prtExLs6Connect": prtExLs6Connect,
       "prtExLs6Protocol": prtExLs6Protocol,
       "prtExLs6Rate": prtExLs6Rate,
       "prtExLs6ClkMode": prtExLs6ClkMode,
       "prtExLs6CtrlSignal": prtExLs6CtrlSignal,
       "prtExLs6DataBits": prtExLs6DataBits,
       "prtExLs6Cts": prtExLs6Cts,
       "prtExLs6LinkToInternal": prtExLs6LinkToInternal,
       "prtExLs6VCnfgTable": prtExLs6VCnfgTable,
       "prtExLs6VCnfgEntry": prtExLs6VCnfgEntry,
       "prtExLs6VCnfgIdx": prtExLs6VCnfgIdx,
       "prtExLs6VSltIdx": prtExLs6VSltIdx,
       "prtExLs6VPrtIdx": prtExLs6VPrtIdx,
       "prtExLs6VConnect": prtExLs6VConnect,
       "prtExLs6VRate": prtExLs6VRate,
       "prtExLs6VEchoCanceler": prtExLs6VEchoCanceler,
       "prtExLs6VIfType": prtExLs6VIfType,
       "prtExLs6VTxGain": prtExLs6VTxGain,
       "prtExLs6VRxGain": prtExLs6VRxGain,
       "prtExLs6VOos": prtExLs6VOos,
       "prtInLs6CnfgTable": prtInLs6CnfgTable,
       "prtInLs6CnfgEntry": prtInLs6CnfgEntry,
       "prtInLs6CnfgIdx": prtInLs6CnfgIdx,
       "prtInLs6SltIdx": prtInLs6SltIdx,
       "prtInLs6PrtIdx": prtInLs6PrtIdx,
       "prtInLs6Connect": prtInLs6Connect,
       "prtInLs6TandemMode": prtInLs6TandemMode,
       "prtInLs6Rate": prtInLs6Rate,
       "prtInLs6RemoteType": prtInLs6RemoteType,
       "prtInLs6LinkTo": prtInLs6LinkTo,
       "prtVc3Cnfg": prtVc3Cnfg,
       "prtExVc3CnfgTable": prtExVc3CnfgTable,
       "prtExVc3CnfgEntry": prtExVc3CnfgEntry,
       "prtExVc3CnfgIdx": prtExVc3CnfgIdx,
       "prtExVc3SltIdx": prtExVc3SltIdx,
       "prtExVc3PrtIdx": prtExVc3PrtIdx,
       "prtExVc3Connect": prtExVc3Connect,
       "prtExVc3TransGain": prtExVc3TransGain,
       "prtExVc3ReceiveGain": prtExVc3ReceiveGain,
       "prtExVc3Wire": prtExVc3Wire,
       "prtExVc3Rate": prtExVc3Rate,
       "prtExVc3EchoCanceler": prtExVc3EchoCanceler,
       "prtInVc3CnfgTable": prtInVc3CnfgTable,
       "prtInVc3CnfgEntry": prtInVc3CnfgEntry,
       "prtInVc3CnfgIdx": prtInVc3CnfgIdx,
       "prtInVc3SltIdx": prtInVc3SltIdx,
       "prtInVc3PrtIdx": prtInVc3PrtIdx,
       "prtInVc3Connect": prtInVc3Connect,
       "prtInVc3Rate": prtInVc3Rate,
       "prtInVc3Oos": prtInVc3Oos,
       "prtInVc3LinkTo": prtInVc3LinkTo,
       "prtVcPbxCnfg": prtVcPbxCnfg,
       "prtExVcPbxCnfgTable": prtExVcPbxCnfgTable,
       "prtExVcPbxCnfgEntry": prtExVcPbxCnfgEntry,
       "prtExVcPbxCnfgIdx": prtExVcPbxCnfgIdx,
       "prtExVcPbxSltIdx": prtExVcPbxSltIdx,
       "prtExVcPbxPrtIdx": prtExVcPbxPrtIdx,
       "prtExVcPbxConnect": prtExVcPbxConnect,
       "prtExVcPbxGroup": prtExVcPbxGroup,
       "prtExVcPbxTransparent": prtExVcPbxTransparent,
       "prtExVcPbxTransSignalTs": prtExVcPbxTransSignalTs,
       "prtExVcPbxFrame": prtExVcPbxFrame,
       "prtExVcPbxRestoreTime": prtExVcPbxRestoreTime,
       "prtExVcPbxLineCode": prtExVcPbxLineCode,
       "prtExVcPbxLineLength": prtExVcPbxLineLength,
       "prtExVcPbxLinkTo": prtExVcPbxLinkTo,
       "prtExVcPbxSignalOper": prtExVcPbxSignalOper,
       "prtExVcPbxIdleCode": prtExVcPbxIdleCode,
       "prtIn1p6VcPbxCnfgTable": prtIn1p6VcPbxCnfgTable,
       "prtIn1p6VcPbxCnfgEntry": prtIn1p6VcPbxCnfgEntry,
       "prtIn1p6VcPbxCnfgIdx": prtIn1p6VcPbxCnfgIdx,
       "prtIn1p6VcPbxSltIdx": prtIn1p6VcPbxSltIdx,
       "prtIn1p6VcPbxPrtIdx": prtIn1p6VcPbxPrtIdx,
       "prtIn1p6VcPbxConnect": prtIn1p6VcPbxConnect,
       "prtIn1p6VcPbxRate": prtIn1p6VcPbxRate,
       "prtIn1p6VcPbxEchoCanceler": prtIn1p6VcPbxEchoCanceler,
       "prtIn1p6VcPbxPabxTs": prtIn1p6VcPbxPabxTs,
       "prtIn7p8VcPbxCnfgTable": prtIn7p8VcPbxCnfgTable,
       "prtIn7p8VcPbxCnfgEntry": prtIn7p8VcPbxCnfgEntry,
       "prtIn7p8VcPbxCnfgIdx": prtIn7p8VcPbxCnfgIdx,
       "prtIn7p8VcPbxSltIdx": prtIn7p8VcPbxSltIdx,
       "prtIn7p8VcPbxPrtIdx": prtIn7p8VcPbxPrtIdx,
       "prtIn7p8VcPbxConnect": prtIn7p8VcPbxConnect,
       "prtIn7p8VcPbxMode": prtIn7p8VcPbxMode,
       "prtIn7p8VcPbxRate": prtIn7p8VcPbxRate,
       "prtIn7p8VcPbxSignalMode": prtIn7p8VcPbxSignalMode,
       "prtIn7p8VcPbxOos": prtIn7p8VcPbxOos,
       "prtIn7p8VcPbxLinkTo": prtIn7p8VcPbxLinkTo,
       "prtExVcPbxTsTable": prtExVcPbxTsTable,
       "prtExVcPbxTsEntry": prtExVcPbxTsEntry,
       "prtExVcPbxTsCnfgIdx": prtExVcPbxTsCnfgIdx,
       "prtExVcPbxTsSltIdx": prtExVcPbxTsSltIdx,
       "prtExVcPbxTsPrtIdx": prtExVcPbxTsPrtIdx,
       "prtExVcPbxTsIdx": prtExVcPbxTsIdx,
       "prtExVcPbxTsMode": prtExVcPbxTsMode,
       "prtExVcPbxTsIConSlot": prtExVcPbxTsIConSlot,
       "prtExVcPbxTsIConPrt": prtExVcPbxTsIConPrt,
       "prtExVcPbxTsIConTs": prtExVcPbxTsIConTs,
       "prtExVcPbxTsRemPrt": prtExVcPbxTsRemPrt,
       "prtExVcPbxTsRemTs": prtExVcPbxTsRemTs,
       "prtExVcPbxTsRemConnID": prtExVcPbxTsRemConnID,
       "prtExVcPbxTsSourceSlot": prtExVcPbxTsSourceSlot,
       "prtExVcPbxTsSourcePrt": prtExVcPbxTsSourcePrt,
       "prtIsdnCnfg": prtIsdnCnfg,
       "prtIsdnCnfgTable": prtIsdnCnfgTable,
       "prtIsdnCnfgEntry": prtIsdnCnfgEntry,
       "prtIsdnCnfgIdx": prtIsdnCnfgIdx,
       "prtIsdnSltIdx": prtIsdnSltIdx,
       "prtIsdnPrtIdx": prtIsdnPrtIdx,
       "prtIsdnConnect": prtIsdnConnect,
       "prtIsdnSignalingProtocol": prtIsdnSignalingProtocol,
       "prtIsdnBasicRateLineTopology": prtIsdnBasicRateLineTopology,
       "prtIsdnMode": prtIsdnMode,
       "prtIsdnFilter": prtIsdnFilter,
       "prtIsdnSimultaneousCall": prtIsdnSimultaneousCall,
       "prtIsdnNumOfAbstractTerm": prtIsdnNumOfAbstractTerm,
       "prtIsdnSwitchMode": prtIsdnSwitchMode,
       "prtIsdnAbSide": prtIsdnAbSide,
       "prtIsdnQsigRole": prtIsdnQsigRole,
       "prtIsdnInterface": prtIsdnInterface,
       "prtIsdnCallMode": prtIsdnCallMode,
       "prtIsdnCallBackTimeout": prtIsdnCallBackTimeout,
       "prtIsdnEndpointTable": prtIsdnEndpointTable,
       "prtIsdnEndpointEntry": prtIsdnEndpointEntry,
       "prtIsdnEndpointCnfgIdx": prtIsdnEndpointCnfgIdx,
       "prtIsdnEndpointSltIdx": prtIsdnEndpointSltIdx,
       "prtIsdnEndpointPrtIdx": prtIsdnEndpointPrtIdx,
       "prtIsdnEndpointIdx": prtIsdnEndpointIdx,
       "prtIsdnEndpointTeiType": prtIsdnEndpointTeiType,
       "prtIsdnEndpointTeiValue": prtIsdnEndpointTeiValue,
       "prtIsdnEndpointSpid": prtIsdnEndpointSpid,
       "prtIsdnEndpointBearerCh": prtIsdnEndpointBearerCh,
       "prtIsdnEndpointRowStatus": prtIsdnEndpointRowStatus,
       "prtIsdnDirectoryTable": prtIsdnDirectoryTable,
       "prtIsdnDirectoryEntry": prtIsdnDirectoryEntry,
       "prtIsdnDirectoryCnfgIdx": prtIsdnDirectoryCnfgIdx,
       "prtIsdnDirectorySltIdx": prtIsdnDirectorySltIdx,
       "prtIsdnDirectoryPrtIdx": prtIsdnDirectoryPrtIdx,
       "prtIsdnDirectoryLocalAddr": prtIsdnDirectoryLocalAddr,
       "prtIsdnDirectoryLocalSubAddr": prtIsdnDirectoryLocalSubAddr,
       "prtIsdnDirectoryRemoteAddr": prtIsdnDirectoryRemoteAddr,
       "prtIsdnDirectoryRemoteSubAddr": prtIsdnDirectoryRemoteSubAddr,
       "prtIsdnDirectoryPrtNu": prtIsdnDirectoryPrtNu,
       "prtIsdnDirectoryTeiId": prtIsdnDirectoryTeiId,
       "prtIsdnDirectoryRowStatus": prtIsdnDirectoryRowStatus,
       "prtIsdnDirectoryLocalAddr2": prtIsdnDirectoryLocalAddr2,
       "prtIsdnDirectoryLocalSubAddr2": prtIsdnDirectoryLocalSubAddr2,
       "prtIsdnDirectoryRemoteAddr2": prtIsdnDirectoryRemoteAddr2,
       "prtIsdnDirectoryRemoteSubAddr2": prtIsdnDirectoryRemoteSubAddr2,
       "prtLogicalCnfg": prtLogicalCnfg,
       "prtLogicalCnfgTable": prtLogicalCnfgTable,
       "prtLogicalCnfgEntry": prtLogicalCnfgEntry,
       "prtLogicalCnfgIdx": prtLogicalCnfgIdx,
       "prtLogicalSltIdx": prtLogicalSltIdx,
       "prtLogicalPrtIdx": prtLogicalPrtIdx,
       "prtLogicalConnect": prtLogicalConnect,
       "prtLogicalFunction": prtLogicalFunction,
       "prtLogicalRowStatus": prtLogicalRowStatus,
       "linkSelectorCnfgTable": linkSelectorCnfgTable,
       "linkSelectorCnfgEntry": linkSelectorCnfgEntry,
       "linkSelectorCnfgIdx": linkSelectorCnfgIdx,
       "linkSelectorSltIdx": linkSelectorSltIdx,
       "linkSelectorPrtIdx": linkSelectorPrtIdx,
       "linkSelectorMaxIdleTime": linkSelectorMaxIdleTime,
       "linkSelectorMode": linkSelectorMode,
       "linkSelectorRevert": linkSelectorRevert,
       "linkSelectorMinBUSession": linkSelectorMinBUSession,
       "linkSelectorPLinkTable": linkSelectorPLinkTable,
       "linkSelectorPLinkEntry": linkSelectorPLinkEntry,
       "pLinkCnfgIdx": pLinkCnfgIdx,
       "pLinkSltIdx": pLinkSltIdx,
       "pLinkPrtIdx": pLinkPrtIdx,
       "pLinkIdx": pLinkIdx,
       "pLinkSlotNu": pLinkSlotNu,
       "pLinkPortNu": pLinkPortNu,
       "pLinkPrioNu": pLinkPrioNu,
       "pLinkVRate": pLinkVRate,
       "prtFrPlusCnfg": prtFrPlusCnfg,
       "prtFrPlusCnfgTable": prtFrPlusCnfgTable,
       "prtFrPlusCnfgEntry": prtFrPlusCnfgEntry,
       "prtFrPlusCnfgIdx": prtFrPlusCnfgIdx,
       "prtFrPlusSltIdx": prtFrPlusSltIdx,
       "prtFrPlusPrtIdx": prtFrPlusPrtIdx,
       "prtFrPlusNotSegmentedPriorities": prtFrPlusNotSegmentedPriorities,
       "prtMl4Cnfg": prtMl4Cnfg,
       "prtMl4CnfgTable": prtMl4CnfgTable,
       "prtMl4CnfgEntry": prtMl4CnfgEntry,
       "prtMl4CnfgIdx": prtMl4CnfgIdx,
       "prtMl4SltIdx": prtMl4SltIdx,
       "prtMl4PrtIdx": prtMl4PrtIdx,
       "prtMl4SigProfile": prtMl4SigProfile,
       "prtMl4CGA": prtMl4CGA,
       "prtMl4Oos": prtMl4Oos,
       "prtMl4VoiceOos": prtMl4VoiceOos,
       "prtMl4DataOos": prtMl4DataOos,
       "prtMl4Service": prtMl4Service,
       "prtMl4IpAddress": prtMl4IpAddress,
       "prtMl4IpMask": prtMl4IpMask,
       "prtMl4SignalingMode": prtMl4SignalingMode,
       "prtMl4EchoCanceler": prtMl4EchoCanceler,
       "prtMl4OosErrorSource": prtMl4OosErrorSource,
       "prtMl4OosEntryThreshold": prtMl4OosEntryThreshold,
       "prtMl4OosExitThreshold": prtMl4OosExitThreshold,
       "prtMl4LogicalLinkId": prtMl4LogicalLinkId,
       "prtMl4DedicatedTs": prtMl4DedicatedTs,
       "prtMl4RemCrc": prtMl4RemCrc,
       "prtMl4CrossConnectLevel": prtMl4CrossConnectLevel,
       "prtMl4PppEchoFailDetection": prtMl4PppEchoFailDetection,
       "prtMl4EcanCasControl": prtMl4EcanCasControl,
       "prtAcmCnfg": prtAcmCnfg,
       "prtAcmCnfgTable": prtAcmCnfgTable,
       "prtAcmCnfgEntry": prtAcmCnfgEntry,
       "prtAcmCnfgIdx": prtAcmCnfgIdx,
       "prtAcmSltIdx": prtAcmSltIdx,
       "prtAcmPrtIdx": prtAcmPrtIdx,
       "prtAcmConnect": prtAcmConnect,
       "prtAcmActiveState": prtAcmActiveState,
       "prtAcmAlrString": prtAcmAlrString,
       "prtE2Cnfg": prtE2Cnfg,
       "prtE2CnfgTable": prtE2CnfgTable,
       "prtE2CnfgEntry": prtE2CnfgEntry,
       "prtE2CnfgIdx": prtE2CnfgIdx,
       "prtE2SltIdx": prtE2SltIdx,
       "prtE2PrtIdx": prtE2PrtIdx,
       "prtE2Connect": prtE2Connect,
       "prtE2MngOnNationalBit": prtE2MngOnNationalBit,
       "prtLanWanCnfg": prtLanWanCnfg,
       "prtLanWanCnfgTable": prtLanWanCnfgTable,
       "prtLanWanCnfgEntry": prtLanWanCnfgEntry,
       "prtLanWanCnfgIdx": prtLanWanCnfgIdx,
       "prtLanWanSltIdx": prtLanWanSltIdx,
       "prtLanWanPrtIdx": prtLanWanPrtIdx,
       "prtLanWanMode": prtLanWanMode,
       "prtLanWanDestIf": prtLanWanDestIf,
       "prtLanWanEgressVlanMode": prtLanWanEgressVlanMode,
       "prtLanWanL2Protocol": prtLanWanL2Protocol,
       "prtLanWanStpPriority": prtLanWanStpPriority,
       "prtLanWanStpCost": prtLanWanStpCost,
       "prtLanWanToLanVlanMode": prtLanWanToLanVlanMode,
       "prtLanWanVlanId": prtLanWanVlanId,
       "prtLanWanVlanPriority": prtLanWanVlanPriority,
       "prtLanWanMtu": prtLanWanMtu,
       "prtLanWanVlanType": prtLanWanVlanType}
)
