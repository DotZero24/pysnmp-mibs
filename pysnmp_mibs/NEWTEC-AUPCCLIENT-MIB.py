# SNMP MIB module (NEWTEC-AUPCCLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-AUPCCLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:13 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcAupcClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100)
)
if mibBuilder.loadTexts:
    ntcAupcClient.setRevisions(
        ("2014-10-31 08:00",
         "2013-09-18 08:00",
         "2013-05-22 06:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcAupcClientObjects_ObjectIdentity = ObjectIdentity
ntcAupcClientObjects = _NtcAupcClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1)
)
if mibBuilder.loadTexts:
    ntcAupcClientObjects.setStatus("current")
_NtcAupcClientAlarm_ObjectIdentity = ObjectIdentity
ntcAupcClientAlarm = _NtcAupcClientAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 1)
)
if mibBuilder.loadTexts:
    ntcAupcClientAlarm.setStatus("current")
_NtcAupcClientAlmCalibAbsent_Type = NtcAlarmState
_NtcAupcClientAlmCalibAbsent_Object = MibScalar
ntcAupcClientAlmCalibAbsent = _NtcAupcClientAlmCalibAbsent_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 1, 1),
    _NtcAupcClientAlmCalibAbsent_Type()
)
ntcAupcClientAlmCalibAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcClientAlmCalibAbsent.setStatus("current")
_NtcAupcClientAlmCalibViolation_Type = NtcAlarmState
_NtcAupcClientAlmCalibViolation_Object = MibScalar
ntcAupcClientAlmCalibViolation = _NtcAupcClientAlmCalibViolation_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 1, 2),
    _NtcAupcClientAlmCalibViolation_Type()
)
ntcAupcClientAlmCalibViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcClientAlmCalibViolation.setStatus("current")
_NtcAupcClientAlarmStateTable_Object = MibTable
ntcAupcClientAlarmStateTable = _NtcAupcClientAlarmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 2)
)
if mibBuilder.loadTexts:
    ntcAupcClientAlarmStateTable.setStatus("current")
_NtcAupcClientAlarmStateEntry_Object = MibTableRow
ntcAupcClientAlarmStateEntry = _NtcAupcClientAlarmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 2, 1)
)
ntcAupcClientAlarmStateEntry.setIndexNames(
    (0, "NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientASDemodId"),
)
if mibBuilder.loadTexts:
    ntcAupcClientAlarmStateEntry.setStatus("current")


class _NtcAupcClientASDemodId_Type(Integer32):
    """Custom type ntcAupcClientASDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcAupcClientASDemodId_Type.__name__ = "Integer32"
_NtcAupcClientASDemodId_Object = MibTableColumn
ntcAupcClientASDemodId = _NtcAupcClientASDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 2, 1, 1),
    _NtcAupcClientASDemodId_Type()
)
ntcAupcClientASDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAupcClientASDemodId.setStatus("current")
_NtcAupcClientASCalibAbsent_Type = NtcAlarmState
_NtcAupcClientASCalibAbsent_Object = MibTableColumn
ntcAupcClientASCalibAbsent = _NtcAupcClientASCalibAbsent_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 2, 1, 2),
    _NtcAupcClientASCalibAbsent_Type()
)
ntcAupcClientASCalibAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcClientASCalibAbsent.setStatus("current")
_NtcAupcClientASCalibViolation_Type = NtcAlarmState
_NtcAupcClientASCalibViolation_Object = MibTableColumn
ntcAupcClientASCalibViolation = _NtcAupcClientASCalibViolation_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 2, 1, 3),
    _NtcAupcClientASCalibViolation_Type()
)
ntcAupcClientASCalibViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcClientASCalibViolation.setStatus("current")
_NtcAupcClientCfgTable_Object = MibTable
ntcAupcClientCfgTable = _NtcAupcClientCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 3)
)
if mibBuilder.loadTexts:
    ntcAupcClientCfgTable.setStatus("current")
_NtcAupcClientCfgEntry_Object = MibTableRow
ntcAupcClientCfgEntry = _NtcAupcClientCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 3, 1)
)
ntcAupcClientCfgEntry.setIndexNames(
    (0, "NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientCfgDemodId"),
)
if mibBuilder.loadTexts:
    ntcAupcClientCfgEntry.setStatus("current")


class _NtcAupcClientCfgDemodId_Type(Integer32):
    """Custom type ntcAupcClientCfgDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcAupcClientCfgDemodId_Type.__name__ = "Integer32"
_NtcAupcClientCfgDemodId_Object = MibTableColumn
ntcAupcClientCfgDemodId = _NtcAupcClientCfgDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 3, 1, 1),
    _NtcAupcClientCfgDemodId_Type()
)
ntcAupcClientCfgDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAupcClientCfgDemodId.setStatus("current")


class _NtcAupcClientCfgEnable_Type(NtcEnable):
    """Custom type ntcAupcClientCfgEnable based on NtcEnable"""
    defaultValue = 0


_NtcAupcClientCfgEnable_Type.__name__ = "NtcEnable"
_NtcAupcClientCfgEnable_Object = MibTableColumn
ntcAupcClientCfgEnable = _NtcAupcClientCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 3, 1, 2),
    _NtcAupcClientCfgEnable_Type()
)
ntcAupcClientCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcClientCfgEnable.setStatus("current")


class _NtcAupcClientCfgRemoteTermId_Type(Unsigned32):
    """Custom type ntcAupcClientCfgRemoteTermId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65277),
    )


_NtcAupcClientCfgRemoteTermId_Type.__name__ = "Unsigned32"
_NtcAupcClientCfgRemoteTermId_Object = MibTableColumn
ntcAupcClientCfgRemoteTermId = _NtcAupcClientCfgRemoteTermId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 3, 1, 3),
    _NtcAupcClientCfgRemoteTermId_Type()
)
ntcAupcClientCfgRemoteTermId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcClientCfgRemoteTermId.setStatus("current")
_NtcAupcClientCalibTable_Object = MibTable
ntcAupcClientCalibTable = _NtcAupcClientCalibTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 4)
)
if mibBuilder.loadTexts:
    ntcAupcClientCalibTable.setStatus("current")
_NtcAupcClientCalibEntry_Object = MibTableRow
ntcAupcClientCalibEntry = _NtcAupcClientCalibEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 4, 1)
)
ntcAupcClientCalibEntry.setIndexNames(
    (0, "NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientCalibDemodId"),
)
if mibBuilder.loadTexts:
    ntcAupcClientCalibEntry.setStatus("current")


class _NtcAupcClientCalibDemodId_Type(Integer32):
    """Custom type ntcAupcClientCalibDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcAupcClientCalibDemodId_Type.__name__ = "Integer32"
_NtcAupcClientCalibDemodId_Object = MibTableColumn
ntcAupcClientCalibDemodId = _NtcAupcClientCalibDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 4, 1, 1),
    _NtcAupcClientCalibDemodId_Type()
)
ntcAupcClientCalibDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAupcClientCalibDemodId.setStatus("current")


class _NtcAupcClientCalibNomInputLvl_Type(Integer32):
    """Custom type ntcAupcClientCalibNomInputLvl based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 500),
    )


_NtcAupcClientCalibNomInputLvl_Type.__name__ = "Integer32"
_NtcAupcClientCalibNomInputLvl_Object = MibTableColumn
ntcAupcClientCalibNomInputLvl = _NtcAupcClientCalibNomInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 4, 1, 2),
    _NtcAupcClientCalibNomInputLvl_Type()
)
ntcAupcClientCalibNomInputLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcClientCalibNomInputLvl.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcClientCalibNomInputLvl.setUnits("dBm")


class _NtcAupcClientCalibNomEsNo_Type(Integer32):
    """Custom type ntcAupcClientCalibNomEsNo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 4000),
    )


_NtcAupcClientCalibNomEsNo_Type.__name__ = "Integer32"
_NtcAupcClientCalibNomEsNo_Object = MibTableColumn
ntcAupcClientCalibNomEsNo = _NtcAupcClientCalibNomEsNo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 4, 1, 3),
    _NtcAupcClientCalibNomEsNo_Type()
)
ntcAupcClientCalibNomEsNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcClientCalibNomEsNo.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcClientCalibNomEsNo.setUnits("dB")
_NtcAupcClientMonTable_Object = MibTable
ntcAupcClientMonTable = _NtcAupcClientMonTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 5)
)
if mibBuilder.loadTexts:
    ntcAupcClientMonTable.setStatus("current")
_NtcAupcClientMonEntry_Object = MibTableRow
ntcAupcClientMonEntry = _NtcAupcClientMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 5, 1)
)
ntcAupcClientMonEntry.setIndexNames(
    (0, "NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientMonDemodId"),
)
if mibBuilder.loadTexts:
    ntcAupcClientMonEntry.setStatus("current")


class _NtcAupcClientMonDemodId_Type(Integer32):
    """Custom type ntcAupcClientMonDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcAupcClientMonDemodId_Type.__name__ = "Integer32"
_NtcAupcClientMonDemodId_Object = MibTableColumn
ntcAupcClientMonDemodId = _NtcAupcClientMonDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 5, 1, 1),
    _NtcAupcClientMonDemodId_Type()
)
ntcAupcClientMonDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcAupcClientMonDemodId.setStatus("current")


class _NtcAupcClientMonState_Type(Integer32):
    """Custom type ntcAupcClientMonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("notCalibrated", 1),
          ("calibrated", 2),
          ("waitingForController", 3),
          ("reporting", 4),
          ("nolock", 5),
          ("alarm", 6))
    )


_NtcAupcClientMonState_Type.__name__ = "Integer32"
_NtcAupcClientMonState_Object = MibTableColumn
ntcAupcClientMonState = _NtcAupcClientMonState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 5, 1, 2),
    _NtcAupcClientMonState_Type()
)
ntcAupcClientMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcClientMonState.setStatus("current")


class _NtcAupcClientMonInputLvl_Type(Integer32):
    """Custom type ntcAupcClientMonInputLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 500),
    )


_NtcAupcClientMonInputLvl_Type.__name__ = "Integer32"
_NtcAupcClientMonInputLvl_Object = MibTableColumn
ntcAupcClientMonInputLvl = _NtcAupcClientMonInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 5, 1, 3),
    _NtcAupcClientMonInputLvl_Type()
)
ntcAupcClientMonInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcClientMonInputLvl.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcClientMonInputLvl.setUnits("dBm")


class _NtcAupcClientMonEsNo_Type(Integer32):
    """Custom type ntcAupcClientMonEsNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 4000),
    )


_NtcAupcClientMonEsNo_Type.__name__ = "Integer32"
_NtcAupcClientMonEsNo_Object = MibTableColumn
ntcAupcClientMonEsNo = _NtcAupcClientMonEsNo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 5, 1, 4),
    _NtcAupcClientMonEsNo_Type()
)
ntcAupcClientMonEsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcClientMonEsNo.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcClientMonEsNo.setUnits("dB")


class _NtcAupcClientMonCurPwrCompen_Type(Integer32):
    """Custom type ntcAupcClientMonCurPwrCompen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 5000),
    )


_NtcAupcClientMonCurPwrCompen_Type.__name__ = "Integer32"
_NtcAupcClientMonCurPwrCompen_Object = MibTableColumn
ntcAupcClientMonCurPwrCompen = _NtcAupcClientMonCurPwrCompen_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 5, 1, 5),
    _NtcAupcClientMonCurPwrCompen_Type()
)
ntcAupcClientMonCurPwrCompen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcClientMonCurPwrCompen.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcClientMonCurPwrCompen.setUnits("dB")


class _NtcAupcClientMonEstRmtUpFading_Type(Integer32):
    """Custom type ntcAupcClientMonEstRmtUpFading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 5000),
    )


_NtcAupcClientMonEstRmtUpFading_Type.__name__ = "Integer32"
_NtcAupcClientMonEstRmtUpFading_Object = MibTableColumn
ntcAupcClientMonEstRmtUpFading = _NtcAupcClientMonEstRmtUpFading_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 1, 5, 1, 6),
    _NtcAupcClientMonEstRmtUpFading_Type()
)
ntcAupcClientMonEstRmtUpFading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcClientMonEstRmtUpFading.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcClientMonEstRmtUpFading.setUnits("dB")
_NtcAupcClntConformance_ObjectIdentity = ObjectIdentity
ntcAupcClntConformance = _NtcAupcClntConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 2)
)
if mibBuilder.loadTexts:
    ntcAupcClntConformance.setStatus("current")
_NtcAupcClntConfCompliance_ObjectIdentity = ObjectIdentity
ntcAupcClntConfCompliance = _NtcAupcClntConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 2, 1)
)
if mibBuilder.loadTexts:
    ntcAupcClntConfCompliance.setStatus("current")
_NtcAupcClntConfGroup_ObjectIdentity = ObjectIdentity
ntcAupcClntConfGroup = _NtcAupcClntConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 2, 2)
)
if mibBuilder.loadTexts:
    ntcAupcClntConfGroup.setStatus("current")

# Managed Objects groups

ntcAupcClntConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 2, 2, 1)
)
ntcAupcClntConfGrpV1Standard.setObjects(
      *(("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientAlmCalibAbsent"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientAlmCalibViolation"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientASCalibAbsent"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientASCalibViolation"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientCfgEnable"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientCfgRemoteTermId"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientCalibNomInputLvl"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientCalibNomEsNo"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientMonState"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientMonInputLvl"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientMonEsNo"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientMonCurPwrCompen"),
        ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClientMonEstRmtUpFading"))
)
if mibBuilder.loadTexts:
    ntcAupcClntConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcAupcClntConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4100, 2, 1, 1)
)
ntcAupcClntConfCompV1Standard.setObjects(
    ("NEWTEC-AUPCCLIENT-MIB", "ntcAupcClntConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcAupcClntConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-AUPCCLIENT-MIB",
    **{"ntcAupcClient": ntcAupcClient,
       "ntcAupcClientObjects": ntcAupcClientObjects,
       "ntcAupcClientAlarm": ntcAupcClientAlarm,
       "ntcAupcClientAlmCalibAbsent": ntcAupcClientAlmCalibAbsent,
       "ntcAupcClientAlmCalibViolation": ntcAupcClientAlmCalibViolation,
       "ntcAupcClientAlarmStateTable": ntcAupcClientAlarmStateTable,
       "ntcAupcClientAlarmStateEntry": ntcAupcClientAlarmStateEntry,
       "ntcAupcClientASDemodId": ntcAupcClientASDemodId,
       "ntcAupcClientASCalibAbsent": ntcAupcClientASCalibAbsent,
       "ntcAupcClientASCalibViolation": ntcAupcClientASCalibViolation,
       "ntcAupcClientCfgTable": ntcAupcClientCfgTable,
       "ntcAupcClientCfgEntry": ntcAupcClientCfgEntry,
       "ntcAupcClientCfgDemodId": ntcAupcClientCfgDemodId,
       "ntcAupcClientCfgEnable": ntcAupcClientCfgEnable,
       "ntcAupcClientCfgRemoteTermId": ntcAupcClientCfgRemoteTermId,
       "ntcAupcClientCalibTable": ntcAupcClientCalibTable,
       "ntcAupcClientCalibEntry": ntcAupcClientCalibEntry,
       "ntcAupcClientCalibDemodId": ntcAupcClientCalibDemodId,
       "ntcAupcClientCalibNomInputLvl": ntcAupcClientCalibNomInputLvl,
       "ntcAupcClientCalibNomEsNo": ntcAupcClientCalibNomEsNo,
       "ntcAupcClientMonTable": ntcAupcClientMonTable,
       "ntcAupcClientMonEntry": ntcAupcClientMonEntry,
       "ntcAupcClientMonDemodId": ntcAupcClientMonDemodId,
       "ntcAupcClientMonState": ntcAupcClientMonState,
       "ntcAupcClientMonInputLvl": ntcAupcClientMonInputLvl,
       "ntcAupcClientMonEsNo": ntcAupcClientMonEsNo,
       "ntcAupcClientMonCurPwrCompen": ntcAupcClientMonCurPwrCompen,
       "ntcAupcClientMonEstRmtUpFading": ntcAupcClientMonEstRmtUpFading,
       "ntcAupcClntConformance": ntcAupcClntConformance,
       "ntcAupcClntConfCompliance": ntcAupcClntConfCompliance,
       "ntcAupcClntConfCompV1Standard": ntcAupcClntConfCompV1Standard,
       "ntcAupcClntConfGroup": ntcAupcClntConfGroup,
       "ntcAupcClntConfGrpV1Standard": ntcAupcClntConfGrpV1Standard}
)
