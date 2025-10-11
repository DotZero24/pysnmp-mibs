# SNMP MIB module (MX-DSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-DSL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:58 2025
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

(mediatrixConfig,
 mediatrixMgmt) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig",
    "mediatrixMgmt")

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

dslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 250)
)
if mibBuilder.loadTexts:
    dslMIB.setRevisions(
        ("2005-01-26 00:00",
         "2005-01-31 00:00",
         "2005-02-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DslStatus_ObjectIdentity = ObjectIdentity
dslStatus = _DslStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100)
)


class _DslModemState_Type(Integer32):
    """Custom type dslModemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unconnected", 0),
          ("connecting", 1),
          ("connected", 2))
    )


_DslModemState_Type.__name__ = "Integer32"
_DslModemState_Object = MibScalar
dslModemState = _DslModemState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 100),
    _DslModemState_Type()
)
dslModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemState.setStatus("current")


class _DslTrainedPath_Type(Integer32):
    """Custom type dslTrainedPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fast", 0),
          ("interleaved", 1))
    )


_DslTrainedPath_Type.__name__ = "Integer32"
_DslTrainedPath_Object = MibScalar
dslTrainedPath = _DslTrainedPath_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 150),
    _DslTrainedPath_Type()
)
dslTrainedPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslTrainedPath.setStatus("current")


class _DslTrainedModulation_Type(Integer32):
    """Custom type dslTrainedModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              8,
              9,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("notTrained", 0),
          ("t1413", 2),
          ("gDmt", 3),
          ("gLite", 4),
          ("adsl2", 8),
          ("adsl2Delt", 9),
          ("adsl2Plus", 16),
          ("adsl2PlusDelt", 17))
    )


_DslTrainedModulation_Type.__name__ = "Integer32"
_DslTrainedModulation_Object = MibScalar
dslTrainedModulation = _DslTrainedModulation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 200),
    _DslTrainedModulation_Type()
)
dslTrainedModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslTrainedModulation.setStatus("current")
_DslModemStats_ObjectIdentity = ObjectIdentity
dslModemStats = _DslModemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000)
)
_DslModemTxConnectionRate_Type = Unsigned32
_DslModemTxConnectionRate_Object = MibScalar
dslModemTxConnectionRate = _DslModemTxConnectionRate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 50),
    _DslModemTxConnectionRate_Type()
)
dslModemTxConnectionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemTxConnectionRate.setStatus("current")
_DslModemRxConnectionRate_Type = Unsigned32
_DslModemRxConnectionRate_Object = MibScalar
dslModemRxConnectionRate = _DslModemRxConnectionRate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 100),
    _DslModemRxConnectionRate_Type()
)
dslModemRxConnectionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemRxConnectionRate.setStatus("current")
_DslModemTxLineAttenuation_Type = Unsigned32
_DslModemTxLineAttenuation_Object = MibScalar
dslModemTxLineAttenuation = _DslModemTxLineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 150),
    _DslModemTxLineAttenuation_Type()
)
dslModemTxLineAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemTxLineAttenuation.setStatus("current")
_DslModemRxLineAttenuation_Type = Unsigned32
_DslModemRxLineAttenuation_Object = MibScalar
dslModemRxLineAttenuation = _DslModemRxLineAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 200),
    _DslModemRxLineAttenuation_Type()
)
dslModemRxLineAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemRxLineAttenuation.setStatus("current")
_DslModemTxMargin_Type = Unsigned32
_DslModemTxMargin_Object = MibScalar
dslModemTxMargin = _DslModemTxMargin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 250),
    _DslModemTxMargin_Type()
)
dslModemTxMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemTxMargin.setStatus("current")
_DslModemRxMargin_Type = Unsigned32
_DslModemRxMargin_Object = MibScalar
dslModemRxMargin = _DslModemRxMargin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 300),
    _DslModemRxMargin_Type()
)
dslModemRxMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemRxMargin.setStatus("current")
_DslModemTxPayload_Type = Unsigned32
_DslModemTxPayload_Object = MibScalar
dslModemTxPayload = _DslModemTxPayload_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 350),
    _DslModemTxPayload_Type()
)
dslModemTxPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemTxPayload.setStatus("current")
_DslModemRxPayload_Type = Unsigned32
_DslModemRxPayload_Object = MibScalar
dslModemRxPayload = _DslModemRxPayload_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 400),
    _DslModemRxPayload_Type()
)
dslModemRxPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemRxPayload.setStatus("current")
_DslModemTxSuperframeCnt_Type = Unsigned32
_DslModemTxSuperframeCnt_Object = MibScalar
dslModemTxSuperframeCnt = _DslModemTxSuperframeCnt_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 450),
    _DslModemTxSuperframeCnt_Type()
)
dslModemTxSuperframeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemTxSuperframeCnt.setStatus("current")
_DslModemRxSuperframeCnt_Type = Unsigned32
_DslModemRxSuperframeCnt_Object = MibScalar
dslModemRxSuperframeCnt = _DslModemRxSuperframeCnt_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 500),
    _DslModemRxSuperframeCnt_Type()
)
dslModemRxSuperframeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemRxSuperframeCnt.setStatus("current")
_DslModemLossOfSignalCount_Type = Unsigned32
_DslModemLossOfSignalCount_Object = MibScalar
dslModemLossOfSignalCount = _DslModemLossOfSignalCount_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 650),
    _DslModemLossOfSignalCount_Type()
)
dslModemLossOfSignalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemLossOfSignalCount.setStatus("current")
_DslModemSeverlyErroredFrameCount_Type = Unsigned32
_DslModemSeverlyErroredFrameCount_Object = MibScalar
dslModemSeverlyErroredFrameCount = _DslModemSeverlyErroredFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 700),
    _DslModemSeverlyErroredFrameCount_Type()
)
dslModemSeverlyErroredFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemSeverlyErroredFrameCount.setStatus("current")
_DslModemTxPeakCellRate_Type = Unsigned32
_DslModemTxPeakCellRate_Object = MibScalar
dslModemTxPeakCellRate = _DslModemTxPeakCellRate_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 750),
    _DslModemTxPeakCellRate_Type()
)
dslModemTxPeakCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslModemTxPeakCellRate.setStatus("current")
_InterleavedPath_ObjectIdentity = ObjectIdentity
interleavedPath = _InterleavedPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 5000)
)
_InterleavedPathTxCrcError_Type = Unsigned32
_InterleavedPathTxCrcError_Object = MibScalar
interleavedPathTxCrcError = _InterleavedPathTxCrcError_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 5000, 50),
    _InterleavedPathTxCrcError_Type()
)
interleavedPathTxCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interleavedPathTxCrcError.setStatus("current")
_InterleavedPathRxCrcError_Type = Unsigned32
_InterleavedPathRxCrcError_Object = MibScalar
interleavedPathRxCrcError = _InterleavedPathRxCrcError_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 5000, 100),
    _InterleavedPathRxCrcError_Type()
)
interleavedPathRxCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interleavedPathRxCrcError.setStatus("current")
_FastPath_ObjectIdentity = ObjectIdentity
fastPath = _FastPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 8000)
)
_FastPathTxCrcError_Type = Unsigned32
_FastPathTxCrcError_Object = MibScalar
fastPathTxCrcError = _FastPathTxCrcError_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 8000, 50),
    _FastPathTxCrcError_Type()
)
fastPathTxCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastPathTxCrcError.setStatus("current")
_FastPathRxCrcError_Type = Unsigned32
_FastPathRxCrcError_Object = MibScalar
fastPathRxCrcError = _FastPathRxCrcError_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 100, 5000, 8000, 100),
    _FastPathRxCrcError_Type()
)
fastPathRxCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastPathRxCrcError.setStatus("current")
_DslMIBObjects_ObjectIdentity = ObjectIdentity
dslMIBObjects = _DslMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 250, 1)
)


class _DslModulation_Type(Integer32):
    """Custom type dslModulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              9,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("mMode", 1),
          ("t1413", 2),
          ("gDmt", 3),
          ("gLite", 4),
          ("adsl2", 8),
          ("adsl2Delt", 9),
          ("adsl2Plus", 16),
          ("adsl2PlusDelt", 17))
    )


_DslModulation_Type.__name__ = "Integer32"
_DslModulation_Object = MibScalar
dslModulation = _DslModulation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 250, 1, 50),
    _DslModulation_Type()
)
dslModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dslModulation.setStatus("current")
_DslConformance_ObjectIdentity = ObjectIdentity
dslConformance = _DslConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 250, 2)
)
_DslCompliances_ObjectIdentity = ObjectIdentity
dslCompliances = _DslCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 250, 2, 1)
)
_DslGroups_ObjectIdentity = ObjectIdentity
dslGroups = _DslGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 250, 2, 5)
)

# Managed Objects groups

dslModemVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 250, 2, 5, 50)
)
dslModemVer1.setObjects(
    ("MX-DSL-MIB", "dslModulation")
)
if mibBuilder.loadTexts:
    dslModemVer1.setStatus("current")

dslStatsVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 250, 2, 5, 100)
)
dslStatsVer1.setObjects(
      *(("MX-DSL-MIB", "dslModemState"),
        ("MX-DSL-MIB", "dslTrainedPath"),
        ("MX-DSL-MIB", "dslTrainedModulation"),
        ("MX-DSL-MIB", "dslModemTxConnectionRate"),
        ("MX-DSL-MIB", "dslModemRxConnectionRate"),
        ("MX-DSL-MIB", "dslModemTxLineAttenuation"),
        ("MX-DSL-MIB", "dslModemRxLineAttenuation"),
        ("MX-DSL-MIB", "dslModemTxMargin"),
        ("MX-DSL-MIB", "dslModemRxMargin"),
        ("MX-DSL-MIB", "dslModemTxPayload"),
        ("MX-DSL-MIB", "dslModemRxPayload"),
        ("MX-DSL-MIB", "dslModemTxSuperframeCnt"),
        ("MX-DSL-MIB", "dslModemRxSuperframeCnt"),
        ("MX-DSL-MIB", "dslModemLossOfSignalCount"),
        ("MX-DSL-MIB", "dslModemSeverlyErroredFrameCount"),
        ("MX-DSL-MIB", "dslModemTxPeakCellRate"),
        ("MX-DSL-MIB", "interleavedPathRxCrcError"),
        ("MX-DSL-MIB", "interleavedPathTxCrcError"),
        ("MX-DSL-MIB", "fastPathTxCrcError"),
        ("MX-DSL-MIB", "fastPathRxCrcError"))
)
if mibBuilder.loadTexts:
    dslStatsVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dslComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 250, 2, 1, 1)
)
dslComplVer1.setObjects(
      *(("MX-DSL-MIB", "dslModemVer1"),
        ("MX-DSL-MIB", "dslStatsVer1"))
)
if mibBuilder.loadTexts:
    dslComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-DSL-MIB",
    **{"dslStatus": dslStatus,
       "dslModemState": dslModemState,
       "dslTrainedPath": dslTrainedPath,
       "dslTrainedModulation": dslTrainedModulation,
       "dslModemStats": dslModemStats,
       "dslModemTxConnectionRate": dslModemTxConnectionRate,
       "dslModemRxConnectionRate": dslModemRxConnectionRate,
       "dslModemTxLineAttenuation": dslModemTxLineAttenuation,
       "dslModemRxLineAttenuation": dslModemRxLineAttenuation,
       "dslModemTxMargin": dslModemTxMargin,
       "dslModemRxMargin": dslModemRxMargin,
       "dslModemTxPayload": dslModemTxPayload,
       "dslModemRxPayload": dslModemRxPayload,
       "dslModemTxSuperframeCnt": dslModemTxSuperframeCnt,
       "dslModemRxSuperframeCnt": dslModemRxSuperframeCnt,
       "dslModemLossOfSignalCount": dslModemLossOfSignalCount,
       "dslModemSeverlyErroredFrameCount": dslModemSeverlyErroredFrameCount,
       "dslModemTxPeakCellRate": dslModemTxPeakCellRate,
       "interleavedPath": interleavedPath,
       "interleavedPathTxCrcError": interleavedPathTxCrcError,
       "interleavedPathRxCrcError": interleavedPathRxCrcError,
       "fastPath": fastPath,
       "fastPathTxCrcError": fastPathTxCrcError,
       "fastPathRxCrcError": fastPathRxCrcError,
       "dslMIB": dslMIB,
       "dslMIBObjects": dslMIBObjects,
       "dslModulation": dslModulation,
       "dslConformance": dslConformance,
       "dslCompliances": dslCompliances,
       "dslComplVer1": dslComplVer1,
       "dslGroups": dslGroups,
       "dslModemVer1": dslModemVer1,
       "dslStatsVer1": dslStatsVer1}
)
