# SNMP MIB module (INFINERA-PM-IDLERPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-IDLERPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:09 2025
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

(perfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "perfMon")

(FloatArbitraryPrecision,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

idlerPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85)
)
if mibBuilder.loadTexts:
    idlerPtpPmMIB.setRevisions(
        ("2017-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IdlerPtpPmRealTable_Object = MibTable
idlerPtpPmRealTable = _IdlerPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 1)
)
if mibBuilder.loadTexts:
    idlerPtpPmRealTable.setStatus("current")
_IdlerPtpPmRealEntry_Object = MibTableRow
idlerPtpPmRealEntry = _IdlerPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 1, 1)
)
idlerPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    idlerPtpPmRealEntry.setStatus("current")
_IdlerPtpPmRealIdlerOpt_Type = FloatArbitraryPrecision
_IdlerPtpPmRealIdlerOpt_Object = MibTableColumn
idlerPtpPmRealIdlerOpt = _IdlerPtpPmRealIdlerOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 1, 1, 1),
    _IdlerPtpPmRealIdlerOpt_Type()
)
idlerPtpPmRealIdlerOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmRealIdlerOpt.setStatus("current")
_IdlerPtpPmRealIdlerOpr_Type = FloatArbitraryPrecision
_IdlerPtpPmRealIdlerOpr_Object = MibTableColumn
idlerPtpPmRealIdlerOpr = _IdlerPtpPmRealIdlerOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 1, 1, 2),
    _IdlerPtpPmRealIdlerOpr_Type()
)
idlerPtpPmRealIdlerOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmRealIdlerOpr.setStatus("current")
_IdlerPtpPmRealIdlerPostRxVoa_Type = FloatArbitraryPrecision
_IdlerPtpPmRealIdlerPostRxVoa_Object = MibTableColumn
idlerPtpPmRealIdlerPostRxVoa = _IdlerPtpPmRealIdlerPostRxVoa_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 1, 1, 3),
    _IdlerPtpPmRealIdlerPostRxVoa_Type()
)
idlerPtpPmRealIdlerPostRxVoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmRealIdlerPostRxVoa.setStatus("current")
_IdlerPtpPmRealTotalLaserPwr_Type = FloatArbitraryPrecision
_IdlerPtpPmRealTotalLaserPwr_Object = MibTableColumn
idlerPtpPmRealTotalLaserPwr = _IdlerPtpPmRealTotalLaserPwr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 1, 1, 4),
    _IdlerPtpPmRealTotalLaserPwr_Type()
)
idlerPtpPmRealTotalLaserPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmRealTotalLaserPwr.setStatus("current")
_IdlerPtpPmTable_Object = MibTable
idlerPtpPmTable = _IdlerPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2)
)
if mibBuilder.loadTexts:
    idlerPtpPmTable.setStatus("current")
_IdlerPtpPmEntry_Object = MibTableRow
idlerPtpPmEntry = _IdlerPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1)
)
idlerPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmSampleDuration"),
    (0, "INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    idlerPtpPmEntry.setStatus("current")


class _IdlerPtpPmTimestamp_Type(Integer32):
    """Custom type idlerPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IdlerPtpPmTimestamp_Type.__name__ = "Integer32"
_IdlerPtpPmTimestamp_Object = MibTableColumn
idlerPtpPmTimestamp = _IdlerPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 1),
    _IdlerPtpPmTimestamp_Type()
)
idlerPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    idlerPtpPmTimestamp.setStatus("current")


class _IdlerPtpPmSampleDuration_Type(Integer32):
    """Custom type idlerPtpPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_IdlerPtpPmSampleDuration_Type.__name__ = "Integer32"
_IdlerPtpPmSampleDuration_Object = MibTableColumn
idlerPtpPmSampleDuration = _IdlerPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 2),
    _IdlerPtpPmSampleDuration_Type()
)
idlerPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    idlerPtpPmSampleDuration.setStatus("current")
_IdlerPtpPmValidity_Type = TruthValue
_IdlerPtpPmValidity_Object = MibTableColumn
idlerPtpPmValidity = _IdlerPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 3),
    _IdlerPtpPmValidity_Type()
)
idlerPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmValidity.setStatus("current")
_IdlerPtpPmIdlerOptMin_Type = FloatArbitraryPrecision
_IdlerPtpPmIdlerOptMin_Object = MibTableColumn
idlerPtpPmIdlerOptMin = _IdlerPtpPmIdlerOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 4),
    _IdlerPtpPmIdlerOptMin_Type()
)
idlerPtpPmIdlerOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmIdlerOptMin.setStatus("current")
_IdlerPtpPmIdlerOptMax_Type = FloatArbitraryPrecision
_IdlerPtpPmIdlerOptMax_Object = MibTableColumn
idlerPtpPmIdlerOptMax = _IdlerPtpPmIdlerOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 5),
    _IdlerPtpPmIdlerOptMax_Type()
)
idlerPtpPmIdlerOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmIdlerOptMax.setStatus("current")
_IdlerPtpPmIdlerOptAve_Type = FloatArbitraryPrecision
_IdlerPtpPmIdlerOptAve_Object = MibTableColumn
idlerPtpPmIdlerOptAve = _IdlerPtpPmIdlerOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 6),
    _IdlerPtpPmIdlerOptAve_Type()
)
idlerPtpPmIdlerOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmIdlerOptAve.setStatus("current")
_IdlerPtpPmIdlerOprMin_Type = FloatArbitraryPrecision
_IdlerPtpPmIdlerOprMin_Object = MibTableColumn
idlerPtpPmIdlerOprMin = _IdlerPtpPmIdlerOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 7),
    _IdlerPtpPmIdlerOprMin_Type()
)
idlerPtpPmIdlerOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmIdlerOprMin.setStatus("current")
_IdlerPtpPmIdlerOprMax_Type = FloatArbitraryPrecision
_IdlerPtpPmIdlerOprMax_Object = MibTableColumn
idlerPtpPmIdlerOprMax = _IdlerPtpPmIdlerOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 8),
    _IdlerPtpPmIdlerOprMax_Type()
)
idlerPtpPmIdlerOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmIdlerOprMax.setStatus("current")
_IdlerPtpPmIdlerOprAve_Type = FloatArbitraryPrecision
_IdlerPtpPmIdlerOprAve_Object = MibTableColumn
idlerPtpPmIdlerOprAve = _IdlerPtpPmIdlerOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 9),
    _IdlerPtpPmIdlerOprAve_Type()
)
idlerPtpPmIdlerOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmIdlerOprAve.setStatus("current")
_IdlerPtpPmIdlerPostRxVoaMin_Type = FloatArbitraryPrecision
_IdlerPtpPmIdlerPostRxVoaMin_Object = MibTableColumn
idlerPtpPmIdlerPostRxVoaMin = _IdlerPtpPmIdlerPostRxVoaMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 10),
    _IdlerPtpPmIdlerPostRxVoaMin_Type()
)
idlerPtpPmIdlerPostRxVoaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmIdlerPostRxVoaMin.setStatus("current")
_IdlerPtpPmIdlerPostRxVoaMax_Type = FloatArbitraryPrecision
_IdlerPtpPmIdlerPostRxVoaMax_Object = MibTableColumn
idlerPtpPmIdlerPostRxVoaMax = _IdlerPtpPmIdlerPostRxVoaMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 11),
    _IdlerPtpPmIdlerPostRxVoaMax_Type()
)
idlerPtpPmIdlerPostRxVoaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmIdlerPostRxVoaMax.setStatus("current")
_IdlerPtpPmIdlerPostRxVoaAve_Type = FloatArbitraryPrecision
_IdlerPtpPmIdlerPostRxVoaAve_Object = MibTableColumn
idlerPtpPmIdlerPostRxVoaAve = _IdlerPtpPmIdlerPostRxVoaAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 12),
    _IdlerPtpPmIdlerPostRxVoaAve_Type()
)
idlerPtpPmIdlerPostRxVoaAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmIdlerPostRxVoaAve.setStatus("current")
_IdlerPtpPmTotalLaserPwrMin_Type = FloatArbitraryPrecision
_IdlerPtpPmTotalLaserPwrMin_Object = MibTableColumn
idlerPtpPmTotalLaserPwrMin = _IdlerPtpPmTotalLaserPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 13),
    _IdlerPtpPmTotalLaserPwrMin_Type()
)
idlerPtpPmTotalLaserPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmTotalLaserPwrMin.setStatus("current")
_IdlerPtpPmTotalLaserPwrMax_Type = FloatArbitraryPrecision
_IdlerPtpPmTotalLaserPwrMax_Object = MibTableColumn
idlerPtpPmTotalLaserPwrMax = _IdlerPtpPmTotalLaserPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 14),
    _IdlerPtpPmTotalLaserPwrMax_Type()
)
idlerPtpPmTotalLaserPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmTotalLaserPwrMax.setStatus("current")
_IdlerPtpPmTotalLaserPwrAve_Type = FloatArbitraryPrecision
_IdlerPtpPmTotalLaserPwrAve_Object = MibTableColumn
idlerPtpPmTotalLaserPwrAve = _IdlerPtpPmTotalLaserPwrAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 2, 1, 15),
    _IdlerPtpPmTotalLaserPwrAve_Type()
)
idlerPtpPmTotalLaserPwrAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerPtpPmTotalLaserPwrAve.setStatus("current")
_IdlerPtpPmConformance_ObjectIdentity = ObjectIdentity
idlerPtpPmConformance = _IdlerPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 3)
)
_IdlerPtpPmCompliances_ObjectIdentity = ObjectIdentity
idlerPtpPmCompliances = _IdlerPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 3, 1)
)
_IdlerPtpPmGroups_ObjectIdentity = ObjectIdentity
idlerPtpPmGroups = _IdlerPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 3, 2)
)

# Managed Objects groups

idlerPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 3, 2, 1)
)
idlerPtpPmGroup.setObjects(
      *(("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmTimestamp"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmSampleDuration"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmValidity"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmIdlerOptMin"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmIdlerOptMax"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmIdlerOptAve"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmIdlerOprMin"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmIdlerOprMax"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmIdlerOprAve"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmIdlerPostRxVoaMin"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmIdlerPostRxVoaMax"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmIdlerPostRxVoaAve"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmTotalLaserPwrMin"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmTotalLaserPwrMax"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmTotalLaserPwrAve"))
)
if mibBuilder.loadTexts:
    idlerPtpPmGroup.setStatus("current")

idlerPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 3, 2, 2)
)
idlerPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmRealIdlerOpt"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmRealIdlerOpr"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmRealIdlerPostRxVoa"),
        ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmRealTotalLaserPwr"))
)
if mibBuilder.loadTexts:
    idlerPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

idlerPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 3, 1, 1)
)
idlerPtpPmCompliance.setObjects(
    ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmGroup")
)
if mibBuilder.loadTexts:
    idlerPtpPmCompliance.setStatus(
        "current"
    )

idlerPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 85, 3, 1, 2)
)
idlerPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-IDLERPTP-MIB", "idlerPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    idlerPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-IDLERPTP-MIB",
    **{"idlerPtpPmMIB": idlerPtpPmMIB,
       "idlerPtpPmRealTable": idlerPtpPmRealTable,
       "idlerPtpPmRealEntry": idlerPtpPmRealEntry,
       "idlerPtpPmRealIdlerOpt": idlerPtpPmRealIdlerOpt,
       "idlerPtpPmRealIdlerOpr": idlerPtpPmRealIdlerOpr,
       "idlerPtpPmRealIdlerPostRxVoa": idlerPtpPmRealIdlerPostRxVoa,
       "idlerPtpPmRealTotalLaserPwr": idlerPtpPmRealTotalLaserPwr,
       "idlerPtpPmTable": idlerPtpPmTable,
       "idlerPtpPmEntry": idlerPtpPmEntry,
       "idlerPtpPmTimestamp": idlerPtpPmTimestamp,
       "idlerPtpPmSampleDuration": idlerPtpPmSampleDuration,
       "idlerPtpPmValidity": idlerPtpPmValidity,
       "idlerPtpPmIdlerOptMin": idlerPtpPmIdlerOptMin,
       "idlerPtpPmIdlerOptMax": idlerPtpPmIdlerOptMax,
       "idlerPtpPmIdlerOptAve": idlerPtpPmIdlerOptAve,
       "idlerPtpPmIdlerOprMin": idlerPtpPmIdlerOprMin,
       "idlerPtpPmIdlerOprMax": idlerPtpPmIdlerOprMax,
       "idlerPtpPmIdlerOprAve": idlerPtpPmIdlerOprAve,
       "idlerPtpPmIdlerPostRxVoaMin": idlerPtpPmIdlerPostRxVoaMin,
       "idlerPtpPmIdlerPostRxVoaMax": idlerPtpPmIdlerPostRxVoaMax,
       "idlerPtpPmIdlerPostRxVoaAve": idlerPtpPmIdlerPostRxVoaAve,
       "idlerPtpPmTotalLaserPwrMin": idlerPtpPmTotalLaserPwrMin,
       "idlerPtpPmTotalLaserPwrMax": idlerPtpPmTotalLaserPwrMax,
       "idlerPtpPmTotalLaserPwrAve": idlerPtpPmTotalLaserPwrAve,
       "idlerPtpPmConformance": idlerPtpPmConformance,
       "idlerPtpPmCompliances": idlerPtpPmCompliances,
       "idlerPtpPmCompliance": idlerPtpPmCompliance,
       "idlerPtpPmRealCompliance": idlerPtpPmRealCompliance,
       "idlerPtpPmGroups": idlerPtpPmGroups,
       "idlerPtpPmGroup": idlerPtpPmGroup,
       "idlerPtpPmRealGroup": idlerPtpPmRealGroup}
)
