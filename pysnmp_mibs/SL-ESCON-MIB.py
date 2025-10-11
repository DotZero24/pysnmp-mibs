# SNMP MIB module (SL-ESCON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-ESCON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:31:06 2025
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

(slService,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "slService")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

esconMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EsconAddressId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class EsconNodeDescription(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_EsconMIBObjects_ObjectIdentity = ObjectIdentity
esconMIBObjects = _EsconMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1)
)
_EsconConfig_ObjectIdentity = ObjectIdentity
esconConfig = _EsconConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1)
)
_EsconPortConfigTable_Object = MibTable
esconPortConfigTable = _EsconPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    esconPortConfigTable.setStatus("current")
_EsconPortConfigEntry_Object = MibTableRow
esconPortConfigEntry = _EsconPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1)
)
esconPortConfigEntry.setIndexNames(
    (0, "SL-ESCON-MIB", "esconPortConfigIndex"),
)
if mibBuilder.loadTexts:
    esconPortConfigEntry.setStatus("current")
_EsconPortConfigIndex_Type = InterfaceIndex
_EsconPortConfigIndex_Object = MibTableColumn
esconPortConfigIndex = _EsconPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 1),
    _EsconPortConfigIndex_Type()
)
esconPortConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortConfigIndex.setStatus("current")
_EsconPortConfigSrcAddress_Type = EsconAddressId
_EsconPortConfigSrcAddress_Object = MibTableColumn
esconPortConfigSrcAddress = _EsconPortConfigSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 2),
    _EsconPortConfigSrcAddress_Type()
)
esconPortConfigSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortConfigSrcAddress.setStatus("current")
_EsconPortConfigSrcDescription_Type = EsconNodeDescription
_EsconPortConfigSrcDescription_Object = MibTableColumn
esconPortConfigSrcDescription = _EsconPortConfigSrcDescription_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 3),
    _EsconPortConfigSrcDescription_Type()
)
esconPortConfigSrcDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortConfigSrcDescription.setStatus("current")


class _EsconPortConfigTranceiverMedia_Type(Integer32):
    """Custom type esconPortConfigTranceiverMedia based on Integer32"""
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
          ("sm", 2),
          ("mm", 3))
    )


_EsconPortConfigTranceiverMedia_Type.__name__ = "Integer32"
_EsconPortConfigTranceiverMedia_Object = MibTableColumn
esconPortConfigTranceiverMedia = _EsconPortConfigTranceiverMedia_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 4),
    _EsconPortConfigTranceiverMedia_Type()
)
esconPortConfigTranceiverMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortConfigTranceiverMedia.setStatus("current")
_EsconPortConfigResetPmCounters_Type = Integer32
_EsconPortConfigResetPmCounters_Object = MibTableColumn
esconPortConfigResetPmCounters = _EsconPortConfigResetPmCounters_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 5),
    _EsconPortConfigResetPmCounters_Type()
)
esconPortConfigResetPmCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortConfigResetPmCounters.setStatus("current")


class _EsconPortConfigTranceiverType_Type(Integer32):
    """Custom type esconPortConfigTranceiverType based on Integer32"""
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
          ("shortWave", 2),
          ("longWave", 3))
    )


_EsconPortConfigTranceiverType_Type.__name__ = "Integer32"
_EsconPortConfigTranceiverType_Object = MibTableColumn
esconPortConfigTranceiverType = _EsconPortConfigTranceiverType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 6),
    _EsconPortConfigTranceiverType_Type()
)
esconPortConfigTranceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortConfigTranceiverType.setStatus("current")


class _EsconPortConfigStatus_Type(Integer32):
    """Custom type esconPortConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EsconPortConfigStatus_Type.__name__ = "Integer32"
_EsconPortConfigStatus_Object = MibTableColumn
esconPortConfigStatus = _EsconPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 7),
    _EsconPortConfigStatus_Type()
)
esconPortConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortConfigStatus.setStatus("current")


class _EsconPortConfigValidIntervals_Type(Integer32):
    """Custom type esconPortConfigValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_EsconPortConfigValidIntervals_Type.__name__ = "Integer32"
_EsconPortConfigValidIntervals_Object = MibTableColumn
esconPortConfigValidIntervals = _EsconPortConfigValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 8),
    _EsconPortConfigValidIntervals_Type()
)
esconPortConfigValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortConfigValidIntervals.setStatus("current")


class _EsconPortConfigLoginState_Type(Bits):
    """Custom type esconPortConfigLoginState based on Bits"""
    namedValues = NamedValues(
        *(("signalSense", 0),
          ("syncPort", 1),
          ("validLogin", 2))
    )

_EsconPortConfigLoginState_Type.__name__ = "Bits"
_EsconPortConfigLoginState_Object = MibTableColumn
esconPortConfigLoginState = _EsconPortConfigLoginState_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 9),
    _EsconPortConfigLoginState_Type()
)
esconPortConfigLoginState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortConfigLoginState.setStatus("current")
_EsconPortResetPmCounters_Type = Integer32
_EsconPortResetPmCounters_Object = MibTableColumn
esconPortResetPmCounters = _EsconPortResetPmCounters_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 1, 1, 1, 10),
    _EsconPortResetPmCounters_Type()
)
esconPortResetPmCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortResetPmCounters.setStatus("current")
_EsconPm_ObjectIdentity = ObjectIdentity
esconPm = _EsconPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2)
)
_EsconPortCurrentTable_Object = MibTable
esconPortCurrentTable = _EsconPortCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    esconPortCurrentTable.setStatus("current")
_EsconPortCurrentEntry_Object = MibTableRow
esconPortCurrentEntry = _EsconPortCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1)
)
esconPortCurrentEntry.setIndexNames(
    (0, "SL-ESCON-MIB", "esconPortCurrentIndex"),
)
if mibBuilder.loadTexts:
    esconPortCurrentEntry.setStatus("current")
_EsconPortCurrentIndex_Type = InterfaceIndex
_EsconPortCurrentIndex_Object = MibTableColumn
esconPortCurrentIndex = _EsconPortCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 1),
    _EsconPortCurrentIndex_Type()
)
esconPortCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentIndex.setStatus("current")
_EsconPortCurrentRxOctets_Type = Counter64
_EsconPortCurrentRxOctets_Object = MibTableColumn
esconPortCurrentRxOctets = _EsconPortCurrentRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 2),
    _EsconPortCurrentRxOctets_Type()
)
esconPortCurrentRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxOctets.setStatus("current")
_EsconPortCurrentRxPkts_Type = Counter64
_EsconPortCurrentRxPkts_Object = MibTableColumn
esconPortCurrentRxPkts = _EsconPortCurrentRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 3),
    _EsconPortCurrentRxPkts_Type()
)
esconPortCurrentRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxPkts.setStatus("current")
_EsconPortCurrentRxSigLosses_Type = Counter64
_EsconPortCurrentRxSigLosses_Object = MibTableColumn
esconPortCurrentRxSigLosses = _EsconPortCurrentRxSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 4),
    _EsconPortCurrentRxSigLosses_Type()
)
esconPortCurrentRxSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxSigLosses.setStatus("current")
_EsconPortCurrentRxSyncLosses_Type = Counter64
_EsconPortCurrentRxSyncLosses_Object = MibTableColumn
esconPortCurrentRxSyncLosses = _EsconPortCurrentRxSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 5),
    _EsconPortCurrentRxSyncLosses_Type()
)
esconPortCurrentRxSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxSyncLosses.setStatus("current")
_EsconPortCurrentRxLinkFailures_Type = Counter64
_EsconPortCurrentRxLinkFailures_Object = MibTableColumn
esconPortCurrentRxLinkFailures = _EsconPortCurrentRxLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 6),
    _EsconPortCurrentRxLinkFailures_Type()
)
esconPortCurrentRxLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxLinkFailures.setStatus("current")
_EsconPortCurrentRxInvalidCrcs_Type = Counter64
_EsconPortCurrentRxInvalidCrcs_Object = MibTableColumn
esconPortCurrentRxInvalidCrcs = _EsconPortCurrentRxInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 7),
    _EsconPortCurrentRxInvalidCrcs_Type()
)
esconPortCurrentRxInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxInvalidCrcs.setStatus("current")
_EsconPortCurrentRxDelimiterErrors_Type = Counter64
_EsconPortCurrentRxDelimiterErrors_Object = MibTableColumn
esconPortCurrentRxDelimiterErrors = _EsconPortCurrentRxDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 8),
    _EsconPortCurrentRxDelimiterErrors_Type()
)
esconPortCurrentRxDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxDelimiterErrors.setStatus("current")
_EsconPortCurrentRxDisparityErrors_Type = Counter64
_EsconPortCurrentRxDisparityErrors_Object = MibTableColumn
esconPortCurrentRxDisparityErrors = _EsconPortCurrentRxDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 9),
    _EsconPortCurrentRxDisparityErrors_Type()
)
esconPortCurrentRxDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxDisparityErrors.setStatus("current")
_EsconPortCurrentRxSizeFrames_Type = Counter64
_EsconPortCurrentRxSizeFrames_Object = MibTableColumn
esconPortCurrentRxSizeFrames = _EsconPortCurrentRxSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 10),
    _EsconPortCurrentRxSizeFrames_Type()
)
esconPortCurrentRxSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxSizeFrames.setStatus("current")
_EsconPortCurrentRxInvalidTxWords_Type = Counter64
_EsconPortCurrentRxInvalidTxWords_Object = MibTableColumn
esconPortCurrentRxInvalidTxWords = _EsconPortCurrentRxInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 11),
    _EsconPortCurrentRxInvalidTxWords_Type()
)
esconPortCurrentRxInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentRxInvalidTxWords.setStatus("current")
_EsconPortCurrentTxOctets_Type = Counter64
_EsconPortCurrentTxOctets_Object = MibTableColumn
esconPortCurrentTxOctets = _EsconPortCurrentTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 12),
    _EsconPortCurrentTxOctets_Type()
)
esconPortCurrentTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentTxOctets.setStatus("current")
_EsconPortCurrentTxPkts_Type = Counter64
_EsconPortCurrentTxPkts_Object = MibTableColumn
esconPortCurrentTxPkts = _EsconPortCurrentTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 13),
    _EsconPortCurrentTxPkts_Type()
)
esconPortCurrentTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentTxPkts.setStatus("current")
_EsconPortCurrentTxHeaderError_Type = Counter64
_EsconPortCurrentTxHeaderError_Object = MibTableColumn
esconPortCurrentTxHeaderError = _EsconPortCurrentTxHeaderError_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 14),
    _EsconPortCurrentTxHeaderError_Type()
)
esconPortCurrentTxHeaderError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentTxHeaderError.setStatus("current")
_EsconPortCurrentTxJitterUnderflow_Type = Counter64
_EsconPortCurrentTxJitterUnderflow_Object = MibTableColumn
esconPortCurrentTxJitterUnderflow = _EsconPortCurrentTxJitterUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 1, 1, 15),
    _EsconPortCurrentTxJitterUnderflow_Type()
)
esconPortCurrentTxJitterUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortCurrentTxJitterUnderflow.setStatus("current")
_EsconPortIntervalTable_Object = MibTable
esconPortIntervalTable = _EsconPortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    esconPortIntervalTable.setStatus("current")
_EsconPortIntervalEntry_Object = MibTableRow
esconPortIntervalEntry = _EsconPortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1)
)
esconPortIntervalEntry.setIndexNames(
    (0, "SL-ESCON-MIB", "esconPortIntervalIndex"),
    (0, "SL-ESCON-MIB", "esconPortIntervalNumber"),
)
if mibBuilder.loadTexts:
    esconPortIntervalEntry.setStatus("current")
_EsconPortIntervalIndex_Type = InterfaceIndex
_EsconPortIntervalIndex_Object = MibTableColumn
esconPortIntervalIndex = _EsconPortIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 1),
    _EsconPortIntervalIndex_Type()
)
esconPortIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalIndex.setStatus("current")


class _EsconPortIntervalNumber_Type(Integer32):
    """Custom type esconPortIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EsconPortIntervalNumber_Type.__name__ = "Integer32"
_EsconPortIntervalNumber_Object = MibTableColumn
esconPortIntervalNumber = _EsconPortIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 2),
    _EsconPortIntervalNumber_Type()
)
esconPortIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalNumber.setStatus("current")
_EsconPortIntervalRxOctets_Type = Counter64
_EsconPortIntervalRxOctets_Object = MibTableColumn
esconPortIntervalRxOctets = _EsconPortIntervalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 3),
    _EsconPortIntervalRxOctets_Type()
)
esconPortIntervalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxOctets.setStatus("current")
_EsconPortIntervalRxPkts_Type = Counter64
_EsconPortIntervalRxPkts_Object = MibTableColumn
esconPortIntervalRxPkts = _EsconPortIntervalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 4),
    _EsconPortIntervalRxPkts_Type()
)
esconPortIntervalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxPkts.setStatus("current")
_EsconPortIntervalRxSigLosses_Type = Counter64
_EsconPortIntervalRxSigLosses_Object = MibTableColumn
esconPortIntervalRxSigLosses = _EsconPortIntervalRxSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 5),
    _EsconPortIntervalRxSigLosses_Type()
)
esconPortIntervalRxSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxSigLosses.setStatus("current")
_EsconPortIntervalRxSyncLosses_Type = Counter64
_EsconPortIntervalRxSyncLosses_Object = MibTableColumn
esconPortIntervalRxSyncLosses = _EsconPortIntervalRxSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 6),
    _EsconPortIntervalRxSyncLosses_Type()
)
esconPortIntervalRxSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxSyncLosses.setStatus("current")
_EsconPortIntervalRxLinkFailures_Type = Counter64
_EsconPortIntervalRxLinkFailures_Object = MibTableColumn
esconPortIntervalRxLinkFailures = _EsconPortIntervalRxLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 7),
    _EsconPortIntervalRxLinkFailures_Type()
)
esconPortIntervalRxLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxLinkFailures.setStatus("current")
_EsconPortIntervalRxInvalidCrcs_Type = Counter64
_EsconPortIntervalRxInvalidCrcs_Object = MibTableColumn
esconPortIntervalRxInvalidCrcs = _EsconPortIntervalRxInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 8),
    _EsconPortIntervalRxInvalidCrcs_Type()
)
esconPortIntervalRxInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxInvalidCrcs.setStatus("current")
_EsconPortIntervalRxDelimiterErrors_Type = Counter64
_EsconPortIntervalRxDelimiterErrors_Object = MibTableColumn
esconPortIntervalRxDelimiterErrors = _EsconPortIntervalRxDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 9),
    _EsconPortIntervalRxDelimiterErrors_Type()
)
esconPortIntervalRxDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxDelimiterErrors.setStatus("current")
_EsconPortIntervalRxDisparityErrors_Type = Counter64
_EsconPortIntervalRxDisparityErrors_Object = MibTableColumn
esconPortIntervalRxDisparityErrors = _EsconPortIntervalRxDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 10),
    _EsconPortIntervalRxDisparityErrors_Type()
)
esconPortIntervalRxDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxDisparityErrors.setStatus("current")
_EsconPortIntervalRxSizeFrames_Type = Counter64
_EsconPortIntervalRxSizeFrames_Object = MibTableColumn
esconPortIntervalRxSizeFrames = _EsconPortIntervalRxSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 11),
    _EsconPortIntervalRxSizeFrames_Type()
)
esconPortIntervalRxSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxSizeFrames.setStatus("current")
_EsconPortIntervalRxInvalidTxWords_Type = Counter64
_EsconPortIntervalRxInvalidTxWords_Object = MibTableColumn
esconPortIntervalRxInvalidTxWords = _EsconPortIntervalRxInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 12),
    _EsconPortIntervalRxInvalidTxWords_Type()
)
esconPortIntervalRxInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalRxInvalidTxWords.setStatus("current")
_EsconPortIntervalTxOctets_Type = Counter64
_EsconPortIntervalTxOctets_Object = MibTableColumn
esconPortIntervalTxOctets = _EsconPortIntervalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 13),
    _EsconPortIntervalTxOctets_Type()
)
esconPortIntervalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalTxOctets.setStatus("current")
_EsconPortIntervalTxPkts_Type = Counter64
_EsconPortIntervalTxPkts_Object = MibTableColumn
esconPortIntervalTxPkts = _EsconPortIntervalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 14),
    _EsconPortIntervalTxPkts_Type()
)
esconPortIntervalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalTxPkts.setStatus("current")
_EsconPortIntervalTxHeaderError_Type = Counter64
_EsconPortIntervalTxHeaderError_Object = MibTableColumn
esconPortIntervalTxHeaderError = _EsconPortIntervalTxHeaderError_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 15),
    _EsconPortIntervalTxHeaderError_Type()
)
esconPortIntervalTxHeaderError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalTxHeaderError.setStatus("current")
_EsconPortIntervalTxJitterUnderflow_Type = Counter64
_EsconPortIntervalTxJitterUnderflow_Object = MibTableColumn
esconPortIntervalTxJitterUnderflow = _EsconPortIntervalTxJitterUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 16),
    _EsconPortIntervalTxJitterUnderflow_Type()
)
esconPortIntervalTxJitterUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalTxJitterUnderflow.setStatus("current")
_EsconPortIntervalValidData_Type = TruthValue
_EsconPortIntervalValidData_Object = MibTableColumn
esconPortIntervalValidData = _EsconPortIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 17),
    _EsconPortIntervalValidData_Type()
)
esconPortIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalValidData.setStatus("current")
_EsconPortIntervalTcaFlag_Type = TruthValue
_EsconPortIntervalTcaFlag_Object = MibTableColumn
esconPortIntervalTcaFlag = _EsconPortIntervalTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 2, 1, 18),
    _EsconPortIntervalTcaFlag_Type()
)
esconPortIntervalTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalTcaFlag.setStatus("current")
_EsconPortTotalTable_Object = MibTable
esconPortTotalTable = _EsconPortTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    esconPortTotalTable.setStatus("current")
_EsconPortTotalEntry_Object = MibTableRow
esconPortTotalEntry = _EsconPortTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1)
)
esconPortTotalEntry.setIndexNames(
    (0, "SL-ESCON-MIB", "esconPortTotalIndex"),
    (0, "SL-ESCON-MIB", "esconPortTotalDayNumber"),
)
if mibBuilder.loadTexts:
    esconPortTotalEntry.setStatus("current")
_EsconPortTotalIndex_Type = InterfaceIndex
_EsconPortTotalIndex_Object = MibTableColumn
esconPortTotalIndex = _EsconPortTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 1),
    _EsconPortTotalIndex_Type()
)
esconPortTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalIndex.setStatus("current")


class _EsconPortTotalDayNumber_Type(Integer32):
    """Custom type esconPortTotalDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_EsconPortTotalDayNumber_Type.__name__ = "Integer32"
_EsconPortTotalDayNumber_Object = MibTableColumn
esconPortTotalDayNumber = _EsconPortTotalDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 2),
    _EsconPortTotalDayNumber_Type()
)
esconPortTotalDayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esconPortTotalDayNumber.setStatus("current")
_EsconPortTotalRxOctets_Type = Counter64
_EsconPortTotalRxOctets_Object = MibTableColumn
esconPortTotalRxOctets = _EsconPortTotalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 3),
    _EsconPortTotalRxOctets_Type()
)
esconPortTotalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxOctets.setStatus("current")
_EsconPortTotalRxPkts_Type = Counter64
_EsconPortTotalRxPkts_Object = MibTableColumn
esconPortTotalRxPkts = _EsconPortTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 4),
    _EsconPortTotalRxPkts_Type()
)
esconPortTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxPkts.setStatus("current")
_EsconPortTotalRxSigLosses_Type = Counter64
_EsconPortTotalRxSigLosses_Object = MibTableColumn
esconPortTotalRxSigLosses = _EsconPortTotalRxSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 5),
    _EsconPortTotalRxSigLosses_Type()
)
esconPortTotalRxSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxSigLosses.setStatus("current")
_EsconPortTotalRxSyncLosses_Type = Counter64
_EsconPortTotalRxSyncLosses_Object = MibTableColumn
esconPortTotalRxSyncLosses = _EsconPortTotalRxSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 6),
    _EsconPortTotalRxSyncLosses_Type()
)
esconPortTotalRxSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxSyncLosses.setStatus("current")
_EsconPortTotalRxLinkFailures_Type = Counter64
_EsconPortTotalRxLinkFailures_Object = MibTableColumn
esconPortTotalRxLinkFailures = _EsconPortTotalRxLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 7),
    _EsconPortTotalRxLinkFailures_Type()
)
esconPortTotalRxLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxLinkFailures.setStatus("current")
_EsconPortTotalRxInvalidCrcs_Type = Counter64
_EsconPortTotalRxInvalidCrcs_Object = MibTableColumn
esconPortTotalRxInvalidCrcs = _EsconPortTotalRxInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 8),
    _EsconPortTotalRxInvalidCrcs_Type()
)
esconPortTotalRxInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxInvalidCrcs.setStatus("current")
_EsconPortTotalRxDelimiterErrors_Type = Counter64
_EsconPortTotalRxDelimiterErrors_Object = MibTableColumn
esconPortTotalRxDelimiterErrors = _EsconPortTotalRxDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 9),
    _EsconPortTotalRxDelimiterErrors_Type()
)
esconPortTotalRxDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxDelimiterErrors.setStatus("current")
_EsconPortTotalRxDisparityErrors_Type = Counter64
_EsconPortTotalRxDisparityErrors_Object = MibTableColumn
esconPortTotalRxDisparityErrors = _EsconPortTotalRxDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 10),
    _EsconPortTotalRxDisparityErrors_Type()
)
esconPortTotalRxDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxDisparityErrors.setStatus("current")
_EsconPortTotalRxSizeFrames_Type = Counter64
_EsconPortTotalRxSizeFrames_Object = MibTableColumn
esconPortTotalRxSizeFrames = _EsconPortTotalRxSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 11),
    _EsconPortTotalRxSizeFrames_Type()
)
esconPortTotalRxSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxSizeFrames.setStatus("current")
_EsconPortTotalRxInvalidTxWords_Type = Counter64
_EsconPortTotalRxInvalidTxWords_Object = MibTableColumn
esconPortTotalRxInvalidTxWords = _EsconPortTotalRxInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 12),
    _EsconPortTotalRxInvalidTxWords_Type()
)
esconPortTotalRxInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalRxInvalidTxWords.setStatus("current")
_EsconPortTotalTxOctets_Type = Counter64
_EsconPortTotalTxOctets_Object = MibTableColumn
esconPortTotalTxOctets = _EsconPortTotalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 13),
    _EsconPortTotalTxOctets_Type()
)
esconPortTotalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalTxOctets.setStatus("current")
_EsconPortTotalTxPkts_Type = Counter64
_EsconPortTotalTxPkts_Object = MibTableColumn
esconPortTotalTxPkts = _EsconPortTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 14),
    _EsconPortTotalTxPkts_Type()
)
esconPortTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalTxPkts.setStatus("current")
_EsconPortTotalTxHeaderError_Type = Counter64
_EsconPortTotalTxHeaderError_Object = MibTableColumn
esconPortTotalTxHeaderError = _EsconPortTotalTxHeaderError_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 15),
    _EsconPortTotalTxHeaderError_Type()
)
esconPortTotalTxHeaderError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalTxHeaderError.setStatus("current")
_EsconPortTotalTxJitterUnderflow_Type = Counter64
_EsconPortTotalTxJitterUnderflow_Object = MibTableColumn
esconPortTotalTxJitterUnderflow = _EsconPortTotalTxJitterUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 16),
    _EsconPortTotalTxJitterUnderflow_Type()
)
esconPortTotalTxJitterUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalTxJitterUnderflow.setStatus("current")
_EsconPortTotalValidData_Type = TruthValue
_EsconPortTotalValidData_Object = MibTableColumn
esconPortTotalValidData = _EsconPortTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 17),
    _EsconPortTotalValidData_Type()
)
esconPortTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalValidData.setStatus("current")
_EsconPortTotalTcaFlag_Type = TruthValue
_EsconPortTotalTcaFlag_Object = MibTableColumn
esconPortTotalTcaFlag = _EsconPortTotalTcaFlag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 3, 1, 18),
    _EsconPortTotalTcaFlag_Type()
)
esconPortTotalTcaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortTotalTcaFlag.setStatus("current")
_EsconPortIntervalThresholdTable_Object = MibTable
esconPortIntervalThresholdTable = _EsconPortIntervalThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    esconPortIntervalThresholdTable.setStatus("current")
_EsconPortIntervalThresholdEntry_Object = MibTableRow
esconPortIntervalThresholdEntry = _EsconPortIntervalThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1)
)
esconPortIntervalThresholdEntry.setIndexNames(
    (0, "SL-ESCON-MIB", "esconPortIntervalThresholdIndex"),
)
if mibBuilder.loadTexts:
    esconPortIntervalThresholdEntry.setStatus("current")
_EsconPortIntervalThresholdIndex_Type = InterfaceIndex
_EsconPortIntervalThresholdIndex_Object = MibTableColumn
esconPortIntervalThresholdIndex = _EsconPortIntervalThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 1),
    _EsconPortIntervalThresholdIndex_Type()
)
esconPortIntervalThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdIndex.setStatus("current")
_EsconPortIntervalThresholdRxSigLosses_Type = Counter64
_EsconPortIntervalThresholdRxSigLosses_Object = MibTableColumn
esconPortIntervalThresholdRxSigLosses = _EsconPortIntervalThresholdRxSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 2),
    _EsconPortIntervalThresholdRxSigLosses_Type()
)
esconPortIntervalThresholdRxSigLosses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdRxSigLosses.setStatus("current")
_EsconPortIntervalThresholdRxSyncLosses_Type = Counter64
_EsconPortIntervalThresholdRxSyncLosses_Object = MibTableColumn
esconPortIntervalThresholdRxSyncLosses = _EsconPortIntervalThresholdRxSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 3),
    _EsconPortIntervalThresholdRxSyncLosses_Type()
)
esconPortIntervalThresholdRxSyncLosses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdRxSyncLosses.setStatus("current")
_EsconPortIntervalThresholdRxLinkFailures_Type = Counter64
_EsconPortIntervalThresholdRxLinkFailures_Object = MibTableColumn
esconPortIntervalThresholdRxLinkFailures = _EsconPortIntervalThresholdRxLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 4),
    _EsconPortIntervalThresholdRxLinkFailures_Type()
)
esconPortIntervalThresholdRxLinkFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdRxLinkFailures.setStatus("current")
_EsconPortIntervalThresholdRxInvalidCrcs_Type = Counter64
_EsconPortIntervalThresholdRxInvalidCrcs_Object = MibTableColumn
esconPortIntervalThresholdRxInvalidCrcs = _EsconPortIntervalThresholdRxInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 5),
    _EsconPortIntervalThresholdRxInvalidCrcs_Type()
)
esconPortIntervalThresholdRxInvalidCrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdRxInvalidCrcs.setStatus("current")
_EsconPortIntervalThresholdRxDelimiterErrors_Type = Counter64
_EsconPortIntervalThresholdRxDelimiterErrors_Object = MibTableColumn
esconPortIntervalThresholdRxDelimiterErrors = _EsconPortIntervalThresholdRxDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 6),
    _EsconPortIntervalThresholdRxDelimiterErrors_Type()
)
esconPortIntervalThresholdRxDelimiterErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdRxDelimiterErrors.setStatus("current")
_EsconPortIntervalThresholdRxDisparityErrors_Type = Counter64
_EsconPortIntervalThresholdRxDisparityErrors_Object = MibTableColumn
esconPortIntervalThresholdRxDisparityErrors = _EsconPortIntervalThresholdRxDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 7),
    _EsconPortIntervalThresholdRxDisparityErrors_Type()
)
esconPortIntervalThresholdRxDisparityErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdRxDisparityErrors.setStatus("current")
_EsconPortIntervalThresholdRxSizeFrames_Type = Counter64
_EsconPortIntervalThresholdRxSizeFrames_Object = MibTableColumn
esconPortIntervalThresholdRxSizeFrames = _EsconPortIntervalThresholdRxSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 8),
    _EsconPortIntervalThresholdRxSizeFrames_Type()
)
esconPortIntervalThresholdRxSizeFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdRxSizeFrames.setStatus("current")
_EsconPortIntervalThresholdRxInvalidTxWords_Type = Counter64
_EsconPortIntervalThresholdRxInvalidTxWords_Object = MibTableColumn
esconPortIntervalThresholdRxInvalidTxWords = _EsconPortIntervalThresholdRxInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 9),
    _EsconPortIntervalThresholdRxInvalidTxWords_Type()
)
esconPortIntervalThresholdRxInvalidTxWords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdRxInvalidTxWords.setStatus("current")
_EsconPortIntervalThresholdTxHeaderError_Type = Counter64
_EsconPortIntervalThresholdTxHeaderError_Object = MibTableColumn
esconPortIntervalThresholdTxHeaderError = _EsconPortIntervalThresholdTxHeaderError_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 10),
    _EsconPortIntervalThresholdTxHeaderError_Type()
)
esconPortIntervalThresholdTxHeaderError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdTxHeaderError.setStatus("current")
_EsconPortIntervalThresholdTxJitterUnderflow_Type = Counter64
_EsconPortIntervalThresholdTxJitterUnderflow_Object = MibTableColumn
esconPortIntervalThresholdTxJitterUnderflow = _EsconPortIntervalThresholdTxJitterUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 4, 1, 11),
    _EsconPortIntervalThresholdTxJitterUnderflow_Type()
)
esconPortIntervalThresholdTxJitterUnderflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortIntervalThresholdTxJitterUnderflow.setStatus("current")
_EsconPortDayThresholdTable_Object = MibTable
esconPortDayThresholdTable = _EsconPortDayThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5)
)
if mibBuilder.loadTexts:
    esconPortDayThresholdTable.setStatus("current")
_EsconPortDayThresholdEntry_Object = MibTableRow
esconPortDayThresholdEntry = _EsconPortDayThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1)
)
esconPortDayThresholdEntry.setIndexNames(
    (0, "SL-ESCON-MIB", "esconPortDayThresholdIndex"),
)
if mibBuilder.loadTexts:
    esconPortDayThresholdEntry.setStatus("current")
_EsconPortDayThresholdIndex_Type = InterfaceIndex
_EsconPortDayThresholdIndex_Object = MibTableColumn
esconPortDayThresholdIndex = _EsconPortDayThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 1),
    _EsconPortDayThresholdIndex_Type()
)
esconPortDayThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconPortDayThresholdIndex.setStatus("current")
_EsconPortDayThresholdRxSigLosses_Type = Counter64
_EsconPortDayThresholdRxSigLosses_Object = MibTableColumn
esconPortDayThresholdRxSigLosses = _EsconPortDayThresholdRxSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 2),
    _EsconPortDayThresholdRxSigLosses_Type()
)
esconPortDayThresholdRxSigLosses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdRxSigLosses.setStatus("current")
_EsconPortDayThresholdRxSyncLosses_Type = Counter64
_EsconPortDayThresholdRxSyncLosses_Object = MibTableColumn
esconPortDayThresholdRxSyncLosses = _EsconPortDayThresholdRxSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 3),
    _EsconPortDayThresholdRxSyncLosses_Type()
)
esconPortDayThresholdRxSyncLosses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdRxSyncLosses.setStatus("current")
_EsconPortDayThresholdRxLinkFailures_Type = Counter64
_EsconPortDayThresholdRxLinkFailures_Object = MibTableColumn
esconPortDayThresholdRxLinkFailures = _EsconPortDayThresholdRxLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 4),
    _EsconPortDayThresholdRxLinkFailures_Type()
)
esconPortDayThresholdRxLinkFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdRxLinkFailures.setStatus("current")
_EsconPortDayThresholdRxInvalidCrcs_Type = Counter64
_EsconPortDayThresholdRxInvalidCrcs_Object = MibTableColumn
esconPortDayThresholdRxInvalidCrcs = _EsconPortDayThresholdRxInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 5),
    _EsconPortDayThresholdRxInvalidCrcs_Type()
)
esconPortDayThresholdRxInvalidCrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdRxInvalidCrcs.setStatus("current")
_EsconPortDayThresholdRxDelimiterErrors_Type = Counter64
_EsconPortDayThresholdRxDelimiterErrors_Object = MibTableColumn
esconPortDayThresholdRxDelimiterErrors = _EsconPortDayThresholdRxDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 6),
    _EsconPortDayThresholdRxDelimiterErrors_Type()
)
esconPortDayThresholdRxDelimiterErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdRxDelimiterErrors.setStatus("current")
_EsconPortDayThresholdRxDisparityErrors_Type = Counter64
_EsconPortDayThresholdRxDisparityErrors_Object = MibTableColumn
esconPortDayThresholdRxDisparityErrors = _EsconPortDayThresholdRxDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 7),
    _EsconPortDayThresholdRxDisparityErrors_Type()
)
esconPortDayThresholdRxDisparityErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdRxDisparityErrors.setStatus("current")
_EsconPortDayThresholdRxSizeFrames_Type = Counter64
_EsconPortDayThresholdRxSizeFrames_Object = MibTableColumn
esconPortDayThresholdRxSizeFrames = _EsconPortDayThresholdRxSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 8),
    _EsconPortDayThresholdRxSizeFrames_Type()
)
esconPortDayThresholdRxSizeFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdRxSizeFrames.setStatus("current")
_EsconPortDayThresholdRxInvalidTxWords_Type = Counter64
_EsconPortDayThresholdRxInvalidTxWords_Object = MibTableColumn
esconPortDayThresholdRxInvalidTxWords = _EsconPortDayThresholdRxInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 9),
    _EsconPortDayThresholdRxInvalidTxWords_Type()
)
esconPortDayThresholdRxInvalidTxWords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdRxInvalidTxWords.setStatus("current")
_EsconPortDayThresholdTxHeaderError_Type = Counter64
_EsconPortDayThresholdTxHeaderError_Object = MibTableColumn
esconPortDayThresholdTxHeaderError = _EsconPortDayThresholdTxHeaderError_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 10),
    _EsconPortDayThresholdTxHeaderError_Type()
)
esconPortDayThresholdTxHeaderError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdTxHeaderError.setStatus("current")
_EsconPortDayThresholdTxJitterUnderflow_Type = Counter64
_EsconPortDayThresholdTxJitterUnderflow_Object = MibTableColumn
esconPortDayThresholdTxJitterUnderflow = _EsconPortDayThresholdTxJitterUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 2, 5, 1, 11),
    _EsconPortDayThresholdTxJitterUnderflow_Type()
)
esconPortDayThresholdTxJitterUnderflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esconPortDayThresholdTxJitterUnderflow.setStatus("current")
_EsconTraps_ObjectIdentity = ObjectIdentity
esconTraps = _EsconTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 3)
)
_EsconCounterId_Type = ObjectIdentifier
_EsconCounterId_Object = MibScalar
esconCounterId = _EsconCounterId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 3, 1),
    _EsconCounterId_Type()
)
esconCounterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconCounterId.setStatus("current")
_EsconCounterValue_Type = Counter64
_EsconCounterValue_Object = MibScalar
esconCounterValue = _EsconCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 3, 2),
    _EsconCounterValue_Type()
)
esconCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esconCounterValue.setStatus("current")

# Managed Objects groups


# Notification objects

esconPortThresholdCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 3, 3)
)
esconPortThresholdCrossing.setObjects(
      *(("SL-ESCON-MIB", "esconCounterId"),
        ("SL-ESCON-MIB", "esconCounterValue"))
)
if mibBuilder.loadTexts:
    esconPortThresholdCrossing.setStatus(
        "current"
    )

esconPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 5, 1, 3, 4)
)
esconPortStatusChange.setObjects(
      *(("SL-ESCON-MIB", "esconPortConfigIndex"),
        ("SL-ESCON-MIB", "esconPortConfigStatus"))
)
if mibBuilder.loadTexts:
    esconPortStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-ESCON-MIB",
    **{"EsconAddressId": EsconAddressId,
       "EsconNodeDescription": EsconNodeDescription,
       "esconMIB": esconMIB,
       "esconMIBObjects": esconMIBObjects,
       "esconConfig": esconConfig,
       "esconPortConfigTable": esconPortConfigTable,
       "esconPortConfigEntry": esconPortConfigEntry,
       "esconPortConfigIndex": esconPortConfigIndex,
       "esconPortConfigSrcAddress": esconPortConfigSrcAddress,
       "esconPortConfigSrcDescription": esconPortConfigSrcDescription,
       "esconPortConfigTranceiverMedia": esconPortConfigTranceiverMedia,
       "esconPortConfigResetPmCounters": esconPortConfigResetPmCounters,
       "esconPortConfigTranceiverType": esconPortConfigTranceiverType,
       "esconPortConfigStatus": esconPortConfigStatus,
       "esconPortConfigValidIntervals": esconPortConfigValidIntervals,
       "esconPortConfigLoginState": esconPortConfigLoginState,
       "esconPortResetPmCounters": esconPortResetPmCounters,
       "esconPm": esconPm,
       "esconPortCurrentTable": esconPortCurrentTable,
       "esconPortCurrentEntry": esconPortCurrentEntry,
       "esconPortCurrentIndex": esconPortCurrentIndex,
       "esconPortCurrentRxOctets": esconPortCurrentRxOctets,
       "esconPortCurrentRxPkts": esconPortCurrentRxPkts,
       "esconPortCurrentRxSigLosses": esconPortCurrentRxSigLosses,
       "esconPortCurrentRxSyncLosses": esconPortCurrentRxSyncLosses,
       "esconPortCurrentRxLinkFailures": esconPortCurrentRxLinkFailures,
       "esconPortCurrentRxInvalidCrcs": esconPortCurrentRxInvalidCrcs,
       "esconPortCurrentRxDelimiterErrors": esconPortCurrentRxDelimiterErrors,
       "esconPortCurrentRxDisparityErrors": esconPortCurrentRxDisparityErrors,
       "esconPortCurrentRxSizeFrames": esconPortCurrentRxSizeFrames,
       "esconPortCurrentRxInvalidTxWords": esconPortCurrentRxInvalidTxWords,
       "esconPortCurrentTxOctets": esconPortCurrentTxOctets,
       "esconPortCurrentTxPkts": esconPortCurrentTxPkts,
       "esconPortCurrentTxHeaderError": esconPortCurrentTxHeaderError,
       "esconPortCurrentTxJitterUnderflow": esconPortCurrentTxJitterUnderflow,
       "esconPortIntervalTable": esconPortIntervalTable,
       "esconPortIntervalEntry": esconPortIntervalEntry,
       "esconPortIntervalIndex": esconPortIntervalIndex,
       "esconPortIntervalNumber": esconPortIntervalNumber,
       "esconPortIntervalRxOctets": esconPortIntervalRxOctets,
       "esconPortIntervalRxPkts": esconPortIntervalRxPkts,
       "esconPortIntervalRxSigLosses": esconPortIntervalRxSigLosses,
       "esconPortIntervalRxSyncLosses": esconPortIntervalRxSyncLosses,
       "esconPortIntervalRxLinkFailures": esconPortIntervalRxLinkFailures,
       "esconPortIntervalRxInvalidCrcs": esconPortIntervalRxInvalidCrcs,
       "esconPortIntervalRxDelimiterErrors": esconPortIntervalRxDelimiterErrors,
       "esconPortIntervalRxDisparityErrors": esconPortIntervalRxDisparityErrors,
       "esconPortIntervalRxSizeFrames": esconPortIntervalRxSizeFrames,
       "esconPortIntervalRxInvalidTxWords": esconPortIntervalRxInvalidTxWords,
       "esconPortIntervalTxOctets": esconPortIntervalTxOctets,
       "esconPortIntervalTxPkts": esconPortIntervalTxPkts,
       "esconPortIntervalTxHeaderError": esconPortIntervalTxHeaderError,
       "esconPortIntervalTxJitterUnderflow": esconPortIntervalTxJitterUnderflow,
       "esconPortIntervalValidData": esconPortIntervalValidData,
       "esconPortIntervalTcaFlag": esconPortIntervalTcaFlag,
       "esconPortTotalTable": esconPortTotalTable,
       "esconPortTotalEntry": esconPortTotalEntry,
       "esconPortTotalIndex": esconPortTotalIndex,
       "esconPortTotalDayNumber": esconPortTotalDayNumber,
       "esconPortTotalRxOctets": esconPortTotalRxOctets,
       "esconPortTotalRxPkts": esconPortTotalRxPkts,
       "esconPortTotalRxSigLosses": esconPortTotalRxSigLosses,
       "esconPortTotalRxSyncLosses": esconPortTotalRxSyncLosses,
       "esconPortTotalRxLinkFailures": esconPortTotalRxLinkFailures,
       "esconPortTotalRxInvalidCrcs": esconPortTotalRxInvalidCrcs,
       "esconPortTotalRxDelimiterErrors": esconPortTotalRxDelimiterErrors,
       "esconPortTotalRxDisparityErrors": esconPortTotalRxDisparityErrors,
       "esconPortTotalRxSizeFrames": esconPortTotalRxSizeFrames,
       "esconPortTotalRxInvalidTxWords": esconPortTotalRxInvalidTxWords,
       "esconPortTotalTxOctets": esconPortTotalTxOctets,
       "esconPortTotalTxPkts": esconPortTotalTxPkts,
       "esconPortTotalTxHeaderError": esconPortTotalTxHeaderError,
       "esconPortTotalTxJitterUnderflow": esconPortTotalTxJitterUnderflow,
       "esconPortTotalValidData": esconPortTotalValidData,
       "esconPortTotalTcaFlag": esconPortTotalTcaFlag,
       "esconPortIntervalThresholdTable": esconPortIntervalThresholdTable,
       "esconPortIntervalThresholdEntry": esconPortIntervalThresholdEntry,
       "esconPortIntervalThresholdIndex": esconPortIntervalThresholdIndex,
       "esconPortIntervalThresholdRxSigLosses": esconPortIntervalThresholdRxSigLosses,
       "esconPortIntervalThresholdRxSyncLosses": esconPortIntervalThresholdRxSyncLosses,
       "esconPortIntervalThresholdRxLinkFailures": esconPortIntervalThresholdRxLinkFailures,
       "esconPortIntervalThresholdRxInvalidCrcs": esconPortIntervalThresholdRxInvalidCrcs,
       "esconPortIntervalThresholdRxDelimiterErrors": esconPortIntervalThresholdRxDelimiterErrors,
       "esconPortIntervalThresholdRxDisparityErrors": esconPortIntervalThresholdRxDisparityErrors,
       "esconPortIntervalThresholdRxSizeFrames": esconPortIntervalThresholdRxSizeFrames,
       "esconPortIntervalThresholdRxInvalidTxWords": esconPortIntervalThresholdRxInvalidTxWords,
       "esconPortIntervalThresholdTxHeaderError": esconPortIntervalThresholdTxHeaderError,
       "esconPortIntervalThresholdTxJitterUnderflow": esconPortIntervalThresholdTxJitterUnderflow,
       "esconPortDayThresholdTable": esconPortDayThresholdTable,
       "esconPortDayThresholdEntry": esconPortDayThresholdEntry,
       "esconPortDayThresholdIndex": esconPortDayThresholdIndex,
       "esconPortDayThresholdRxSigLosses": esconPortDayThresholdRxSigLosses,
       "esconPortDayThresholdRxSyncLosses": esconPortDayThresholdRxSyncLosses,
       "esconPortDayThresholdRxLinkFailures": esconPortDayThresholdRxLinkFailures,
       "esconPortDayThresholdRxInvalidCrcs": esconPortDayThresholdRxInvalidCrcs,
       "esconPortDayThresholdRxDelimiterErrors": esconPortDayThresholdRxDelimiterErrors,
       "esconPortDayThresholdRxDisparityErrors": esconPortDayThresholdRxDisparityErrors,
       "esconPortDayThresholdRxSizeFrames": esconPortDayThresholdRxSizeFrames,
       "esconPortDayThresholdRxInvalidTxWords": esconPortDayThresholdRxInvalidTxWords,
       "esconPortDayThresholdTxHeaderError": esconPortDayThresholdTxHeaderError,
       "esconPortDayThresholdTxJitterUnderflow": esconPortDayThresholdTxJitterUnderflow,
       "esconTraps": esconTraps,
       "esconCounterId": esconCounterId,
       "esconCounterValue": esconCounterValue,
       "esconPortThresholdCrossing": esconPortThresholdCrossing,
       "esconPortStatusChange": esconPortStatusChange}
)
