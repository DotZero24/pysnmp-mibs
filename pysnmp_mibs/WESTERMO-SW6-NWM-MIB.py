# SNMP MIB module (WESTERMO-SW6-NWM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-SW6-NWM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:26 2025
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

nwm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3)
)
if mibBuilder.loadTexts:
    nwm.setRevisions(
        ("2019-09-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1)
)
_CfgHttpReport_ObjectIdentity = ObjectIdentity
cfgHttpReport = _CfgHttpReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 1)
)


class _CfgHttpRprtServerUrl_Type(DisplayString):
    """Custom type cfgHttpRprtServerUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgHttpRprtServerUrl_Type.__name__ = "DisplayString"
_CfgHttpRprtServerUrl_Object = MibScalar
cfgHttpRprtServerUrl = _CfgHttpRprtServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 1, 1),
    _CfgHttpRprtServerUrl_Type()
)
cfgHttpRprtServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHttpRprtServerUrl.setStatus("current")
_CfgChannelManager_ObjectIdentity = ObjectIdentity
cfgChannelManager = _CfgChannelManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 3)
)


class _CfgChMgrEnabled_Type(Integer32):
    """Custom type cfgChMgrEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgChMgrEnabled_Type.__name__ = "Integer32"
_CfgChMgrEnabled_Object = MibScalar
cfgChMgrEnabled = _CfgChMgrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 3, 1),
    _CfgChMgrEnabled_Type()
)
cfgChMgrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgChMgrEnabled.setStatus("current")


class _CfgChMgrUsableFrequencyList_Type(Integer32):
    """Custom type cfgChMgrUsableFrequencyList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 23),
    )


_CfgChMgrUsableFrequencyList_Type.__name__ = "Integer32"
_CfgChMgrUsableFrequencyList_Object = MibScalar
cfgChMgrUsableFrequencyList = _CfgChMgrUsableFrequencyList_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 3, 2),
    _CfgChMgrUsableFrequencyList_Type()
)
cfgChMgrUsableFrequencyList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgChMgrUsableFrequencyList.setStatus("current")


class _CfgChMgrDfsUseNvram_Type(Integer32):
    """Custom type cfgChMgrDfsUseNvram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgChMgrDfsUseNvram_Type.__name__ = "Integer32"
_CfgChMgrDfsUseNvram_Object = MibScalar
cfgChMgrDfsUseNvram = _CfgChMgrDfsUseNvram_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 3, 3),
    _CfgChMgrDfsUseNvram_Type()
)
cfgChMgrDfsUseNvram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgChMgrDfsUseNvram.setStatus("current")
_CfgNwm_ObjectIdentity = ObjectIdentity
cfgNwm = _CfgNwm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 4)
)


class _CfgNwmEnabled_Type(Integer32):
    """Custom type cfgNwmEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgNwmEnabled_Type.__name__ = "Integer32"
_CfgNwmEnabled_Object = MibScalar
cfgNwmEnabled = _CfgNwmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 4, 1),
    _CfgNwmEnabled_Type()
)
cfgNwmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNwmEnabled.setStatus("current")
_CfgIdf_ObjectIdentity = ObjectIdentity
cfgIdf = _CfgIdf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5)
)


class _CfgIdfEnabled_Type(Integer32):
    """Custom type cfgIdfEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgIdfEnabled_Type.__name__ = "Integer32"
_CfgIdfEnabled_Object = MibScalar
cfgIdfEnabled = _CfgIdfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 1),
    _CfgIdfEnabled_Type()
)
cfgIdfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfEnabled.setStatus("current")


class _CfgIdfInterval_Type(Integer32):
    """Custom type cfgIdfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CfgIdfInterval_Type.__name__ = "Integer32"
_CfgIdfInterval_Object = MibScalar
cfgIdfInterval = _CfgIdfInterval_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 3),
    _CfgIdfInterval_Type()
)
cfgIdfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfInterval.setStatus("current")


class _CfgIdfName_Type(DisplayString):
    """Custom type cfgIdfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgIdfName_Type.__name__ = "DisplayString"
_CfgIdfName_Object = MibScalar
cfgIdfName = _CfgIdfName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 4),
    _CfgIdfName_Type()
)
cfgIdfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfName.setStatus("current")
_CfgIdfTrigger_ObjectIdentity = ObjectIdentity
cfgIdfTrigger = _CfgIdfTrigger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 5)
)
_CfgIdfTrigRadarCntTh_Type = Integer32
_CfgIdfTrigRadarCntTh_Object = MibScalar
cfgIdfTrigRadarCntTh = _CfgIdfTrigRadarCntTh_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 5, 1),
    _CfgIdfTrigRadarCntTh_Type()
)
cfgIdfTrigRadarCntTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfTrigRadarCntTh.setStatus("current")


class _CfgIdfTrigChanLoadTh_Type(Integer32):
    """Custom type cfgIdfTrigChanLoadTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgIdfTrigChanLoadTh_Type.__name__ = "Integer32"
_CfgIdfTrigChanLoadTh_Object = MibScalar
cfgIdfTrigChanLoadTh = _CfgIdfTrigChanLoadTh_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 5, 2),
    _CfgIdfTrigChanLoadTh_Type()
)
cfgIdfTrigChanLoadTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfTrigChanLoadTh.setStatus("current")


class _CfgIdfTrigAlienLoadTh_Type(Integer32):
    """Custom type cfgIdfTrigAlienLoadTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgIdfTrigAlienLoadTh_Type.__name__ = "Integer32"
_CfgIdfTrigAlienLoadTh_Object = MibScalar
cfgIdfTrigAlienLoadTh = _CfgIdfTrigAlienLoadTh_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 5, 3),
    _CfgIdfTrigAlienLoadTh_Type()
)
cfgIdfTrigAlienLoadTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfTrigAlienLoadTh.setStatus("current")


class _CfgIdfTrigDomLoadTh_Type(Integer32):
    """Custom type cfgIdfTrigDomLoadTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgIdfTrigDomLoadTh_Type.__name__ = "Integer32"
_CfgIdfTrigDomLoadTh_Object = MibScalar
cfgIdfTrigDomLoadTh = _CfgIdfTrigDomLoadTh_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 5, 4),
    _CfgIdfTrigDomLoadTh_Type()
)
cfgIdfTrigDomLoadTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfTrigDomLoadTh.setStatus("current")


class _CfgIdfTrigAlienMaxRssiTh_Type(Integer32):
    """Custom type cfgIdfTrigAlienMaxRssiTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CfgIdfTrigAlienMaxRssiTh_Type.__name__ = "Integer32"
_CfgIdfTrigAlienMaxRssiTh_Object = MibScalar
cfgIdfTrigAlienMaxRssiTh = _CfgIdfTrigAlienMaxRssiTh_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 5, 5),
    _CfgIdfTrigAlienMaxRssiTh_Type()
)
cfgIdfTrigAlienMaxRssiTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfTrigAlienMaxRssiTh.setStatus("current")


class _CfgIdfTrigDomMaxRssiTh_Type(Integer32):
    """Custom type cfgIdfTrigDomMaxRssiTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CfgIdfTrigDomMaxRssiTh_Type.__name__ = "Integer32"
_CfgIdfTrigDomMaxRssiTh_Object = MibScalar
cfgIdfTrigDomMaxRssiTh = _CfgIdfTrigDomMaxRssiTh_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 5, 6),
    _CfgIdfTrigDomMaxRssiTh_Type()
)
cfgIdfTrigDomMaxRssiTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfTrigDomMaxRssiTh.setStatus("current")
_CfgIdfScanWorkTable_Object = MibTable
cfgIdfScanWorkTable = _CfgIdfScanWorkTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 10)
)
if mibBuilder.loadTexts:
    cfgIdfScanWorkTable.setStatus("current")
_CfgIdfScanWorkTableEntry_Object = MibTableRow
cfgIdfScanWorkTableEntry = _CfgIdfScanWorkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 10, 1)
)
cfgIdfScanWorkTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-NWM-MIB", "cfgIdfScanWorkIndex"),
)
if mibBuilder.loadTexts:
    cfgIdfScanWorkTableEntry.setStatus("current")


class _CfgIdfScanWorkIndex_Type(Integer32):
    """Custom type cfgIdfScanWorkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CfgIdfScanWorkIndex_Type.__name__ = "Integer32"
_CfgIdfScanWorkIndex_Object = MibTableColumn
cfgIdfScanWorkIndex = _CfgIdfScanWorkIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 10, 1, 1),
    _CfgIdfScanWorkIndex_Type()
)
cfgIdfScanWorkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgIdfScanWorkIndex.setStatus("current")


class _CfgIdfScanWorkFreq_Type(Integer32):
    """Custom type cfgIdfScanWorkFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6100),
    )


_CfgIdfScanWorkFreq_Type.__name__ = "Integer32"
_CfgIdfScanWorkFreq_Object = MibTableColumn
cfgIdfScanWorkFreq = _CfgIdfScanWorkFreq_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 10, 1, 2),
    _CfgIdfScanWorkFreq_Type()
)
cfgIdfScanWorkFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfScanWorkFreq.setStatus("current")


class _CfgIdfScanWorkAction_Type(Integer32):
    """Custom type cfgIdfScanWorkAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("spectral", 2),
          ("radar", 3),
          ("wifi", 4))
    )


_CfgIdfScanWorkAction_Type.__name__ = "Integer32"
_CfgIdfScanWorkAction_Object = MibTableColumn
cfgIdfScanWorkAction = _CfgIdfScanWorkAction_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 10, 1, 3),
    _CfgIdfScanWorkAction_Type()
)
cfgIdfScanWorkAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfScanWorkAction.setStatus("current")


class _CfgIdfScanWorkSeconds_Type(Integer32):
    """Custom type cfgIdfScanWorkSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CfgIdfScanWorkSeconds_Type.__name__ = "Integer32"
_CfgIdfScanWorkSeconds_Object = MibTableColumn
cfgIdfScanWorkSeconds = _CfgIdfScanWorkSeconds_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 5, 10, 1, 4),
    _CfgIdfScanWorkSeconds_Type()
)
cfgIdfScanWorkSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIdfScanWorkSeconds.setStatus("current")
_CfgChannelCleaner_ObjectIdentity = ObjectIdentity
cfgChannelCleaner = _CfgChannelCleaner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 6)
)


class _CfgChanCleanEnabled_Type(Integer32):
    """Custom type cfgChanCleanEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgChanCleanEnabled_Type.__name__ = "Integer32"
_CfgChanCleanEnabled_Object = MibScalar
cfgChanCleanEnabled = _CfgChanCleanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 6, 1),
    _CfgChanCleanEnabled_Type()
)
cfgChanCleanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgChanCleanEnabled.setStatus("current")


class _CfgChanCleanDfsUseNvram_Type(Integer32):
    """Custom type cfgChanCleanDfsUseNvram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgChanCleanDfsUseNvram_Type.__name__ = "Integer32"
_CfgChanCleanDfsUseNvram_Object = MibScalar
cfgChanCleanDfsUseNvram = _CfgChanCleanDfsUseNvram_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 6, 9),
    _CfgChanCleanDfsUseNvram_Type()
)
cfgChanCleanDfsUseNvram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgChanCleanDfsUseNvram.setStatus("current")


class _CfgChanCleanUsableFrequencyList_Type(Integer32):
    """Custom type cfgChanCleanUsableFrequencyList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CfgChanCleanUsableFrequencyList_Type.__name__ = "Integer32"
_CfgChanCleanUsableFrequencyList_Object = MibScalar
cfgChanCleanUsableFrequencyList = _CfgChanCleanUsableFrequencyList_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 6, 10),
    _CfgChanCleanUsableFrequencyList_Type()
)
cfgChanCleanUsableFrequencyList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgChanCleanUsableFrequencyList.setStatus("current")
_CfgAfm_ObjectIdentity = ObjectIdentity
cfgAfm = _CfgAfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7)
)


class _CfgAfmEnabled_Type(Integer32):
    """Custom type cfgAfmEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgAfmEnabled_Type.__name__ = "Integer32"
_CfgAfmEnabled_Object = MibScalar
cfgAfmEnabled = _CfgAfmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 1),
    _CfgAfmEnabled_Type()
)
cfgAfmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmEnabled.setStatus("current")


class _CfgAfmName_Type(DisplayString):
    """Custom type cfgAfmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgAfmName_Type.__name__ = "DisplayString"
_CfgAfmName_Object = MibScalar
cfgAfmName = _CfgAfmName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 2),
    _CfgAfmName_Type()
)
cfgAfmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmName.setStatus("current")
_CfgAfmIndex_Type = Integer32
_CfgAfmIndex_Object = MibScalar
cfgAfmIndex = _CfgAfmIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 3),
    _CfgAfmIndex_Type()
)
cfgAfmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmIndex.setStatus("current")


class _CfgAfmAreaSize_Type(Integer32):
    """Custom type cfgAfmAreaSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CfgAfmAreaSize_Type.__name__ = "Integer32"
_CfgAfmAreaSize_Object = MibScalar
cfgAfmAreaSize = _CfgAfmAreaSize_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 5),
    _CfgAfmAreaSize_Type()
)
cfgAfmAreaSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmAreaSize.setStatus("current")


class _CfgAfmPrimary_Type(Integer32):
    """Custom type cfgAfmPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgAfmPrimary_Type.__name__ = "Integer32"
_CfgAfmPrimary_Object = MibScalar
cfgAfmPrimary = _CfgAfmPrimary_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 6),
    _CfgAfmPrimary_Type()
)
cfgAfmPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmPrimary.setStatus("current")


class _CfgAfmReportEnabled_Type(Integer32):
    """Custom type cfgAfmReportEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgAfmReportEnabled_Type.__name__ = "Integer32"
_CfgAfmReportEnabled_Object = MibScalar
cfgAfmReportEnabled = _CfgAfmReportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 7),
    _CfgAfmReportEnabled_Type()
)
cfgAfmReportEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmReportEnabled.setStatus("current")
_CfgAfmRedundant_ObjectIdentity = ObjectIdentity
cfgAfmRedundant = _CfgAfmRedundant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 10)
)
_CfgAfmRedundantIp_Type = IpAddress
_CfgAfmRedundantIp_Object = MibScalar
cfgAfmRedundantIp = _CfgAfmRedundantIp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 10, 1),
    _CfgAfmRedundantIp_Type()
)
cfgAfmRedundantIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmRedundantIp.setStatus("current")
_CfgAfmRedundantName_Type = DisplayString
_CfgAfmRedundantName_Object = MibScalar
cfgAfmRedundantName = _CfgAfmRedundantName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 10, 2),
    _CfgAfmRedundantName_Type()
)
cfgAfmRedundantName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmRedundantName.setStatus("current")
_CfgAfmNeighbourTable_Object = MibTable
cfgAfmNeighbourTable = _CfgAfmNeighbourTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 20)
)
if mibBuilder.loadTexts:
    cfgAfmNeighbourTable.setStatus("current")
_CfgAfmNeighbourTableEntry_Object = MibTableRow
cfgAfmNeighbourTableEntry = _CfgAfmNeighbourTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 20, 1)
)
cfgAfmNeighbourTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-NWM-MIB", "cfgAfmNeighbourTableIndex"),
)
if mibBuilder.loadTexts:
    cfgAfmNeighbourTableEntry.setStatus("current")


class _CfgAfmNeighbourTableIndex_Type(Integer32):
    """Custom type cfgAfmNeighbourTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CfgAfmNeighbourTableIndex_Type.__name__ = "Integer32"
_CfgAfmNeighbourTableIndex_Object = MibTableColumn
cfgAfmNeighbourTableIndex = _CfgAfmNeighbourTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 20, 1, 1),
    _CfgAfmNeighbourTableIndex_Type()
)
cfgAfmNeighbourTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgAfmNeighbourTableIndex.setStatus("current")
_CfgAfmNeighbourIp_Type = IpAddress
_CfgAfmNeighbourIp_Object = MibTableColumn
cfgAfmNeighbourIp = _CfgAfmNeighbourIp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 20, 1, 2),
    _CfgAfmNeighbourIp_Type()
)
cfgAfmNeighbourIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmNeighbourIp.setStatus("current")
_CfgAfmNeighbourName_Type = DisplayString
_CfgAfmNeighbourName_Object = MibTableColumn
cfgAfmNeighbourName = _CfgAfmNeighbourName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 20, 1, 3),
    _CfgAfmNeighbourName_Type()
)
cfgAfmNeighbourName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmNeighbourName.setStatus("current")
_CfgAfmAfcTable_Object = MibTable
cfgAfmAfcTable = _CfgAfmAfcTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 30)
)
if mibBuilder.loadTexts:
    cfgAfmAfcTable.setStatus("current")
_CfgAfmAfcTableEntry_Object = MibTableRow
cfgAfmAfcTableEntry = _CfgAfmAfcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 30, 1)
)
cfgAfmAfcTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-NWM-MIB", "cfgAfmAfcTableIndex"),
)
if mibBuilder.loadTexts:
    cfgAfmAfcTableEntry.setStatus("current")


class _CfgAfmAfcTableIndex_Type(Integer32):
    """Custom type cfgAfmAfcTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgAfmAfcTableIndex_Type.__name__ = "Integer32"
_CfgAfmAfcTableIndex_Object = MibTableColumn
cfgAfmAfcTableIndex = _CfgAfmAfcTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 30, 1, 1),
    _CfgAfmAfcTableIndex_Type()
)
cfgAfmAfcTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgAfmAfcTableIndex.setStatus("current")


class _CfgAfmAfcName_Type(DisplayString):
    """Custom type cfgAfmAfcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgAfmAfcName_Type.__name__ = "DisplayString"
_CfgAfmAfcName_Object = MibTableColumn
cfgAfmAfcName = _CfgAfmAfcName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 30, 1, 2),
    _CfgAfmAfcName_Type()
)
cfgAfmAfcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmAfcName.setStatus("current")
_CfgAfmAfcIp_Type = IpAddress
_CfgAfmAfcIp_Object = MibTableColumn
cfgAfmAfcIp = _CfgAfmAfcIp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 7, 30, 1, 3),
    _CfgAfmAfcIp_Type()
)
cfgAfmAfcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfmAfcIp.setStatus("current")
_CfgAfc_ObjectIdentity = ObjectIdentity
cfgAfc = _CfgAfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8)
)


class _CfgAfcEnabled_Type(Integer32):
    """Custom type cfgAfcEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgAfcEnabled_Type.__name__ = "Integer32"
_CfgAfcEnabled_Object = MibScalar
cfgAfcEnabled = _CfgAfcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 1),
    _CfgAfcEnabled_Type()
)
cfgAfcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfcEnabled.setStatus("current")


class _CfgAfcName_Type(DisplayString):
    """Custom type cfgAfcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgAfcName_Type.__name__ = "DisplayString"
_CfgAfcName_Object = MibScalar
cfgAfcName = _CfgAfcName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 2),
    _CfgAfcName_Type()
)
cfgAfcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfcName.setStatus("current")


class _CfgAfcIndex_Type(Integer32):
    """Custom type cfgAfcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CfgAfcIndex_Type.__name__ = "Integer32"
_CfgAfcIndex_Object = MibScalar
cfgAfcIndex = _CfgAfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 3),
    _CfgAfcIndex_Type()
)
cfgAfcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfcIndex.setStatus("current")


class _CfgAfcBackupFreq_Type(Integer32):
    """Custom type cfgAfcBackupFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6100),
    )


_CfgAfcBackupFreq_Type.__name__ = "Integer32"
_CfgAfcBackupFreq_Object = MibScalar
cfgAfcBackupFreq = _CfgAfcBackupFreq_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 5),
    _CfgAfcBackupFreq_Type()
)
cfgAfcBackupFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfcBackupFreq.setStatus("current")


class _CfgAfcReportEnabled_Type(Integer32):
    """Custom type cfgAfcReportEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgAfcReportEnabled_Type.__name__ = "Integer32"
_CfgAfcReportEnabled_Object = MibScalar
cfgAfcReportEnabled = _CfgAfcReportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 6),
    _CfgAfcReportEnabled_Type()
)
cfgAfcReportEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfcReportEnabled.setStatus("current")
_CfgAfcAfmTable_Object = MibTable
cfgAfcAfmTable = _CfgAfcAfmTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 10)
)
if mibBuilder.loadTexts:
    cfgAfcAfmTable.setStatus("current")
_CfgAfcAfmTableEntry_Object = MibTableRow
cfgAfcAfmTableEntry = _CfgAfcAfmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 10, 1)
)
cfgAfcAfmTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-NWM-MIB", "cfgAfcAfmTableIndex"),
)
if mibBuilder.loadTexts:
    cfgAfcAfmTableEntry.setStatus("current")


class _CfgAfcAfmTableIndex_Type(Integer32):
    """Custom type cfgAfcAfmTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CfgAfcAfmTableIndex_Type.__name__ = "Integer32"
_CfgAfcAfmTableIndex_Object = MibTableColumn
cfgAfcAfmTableIndex = _CfgAfcAfmTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 10, 1, 1),
    _CfgAfcAfmTableIndex_Type()
)
cfgAfcAfmTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgAfcAfmTableIndex.setStatus("current")


class _CfgAfcAfmName_Type(DisplayString):
    """Custom type cfgAfcAfmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgAfcAfmName_Type.__name__ = "DisplayString"
_CfgAfcAfmName_Object = MibTableColumn
cfgAfcAfmName = _CfgAfcAfmName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 10, 1, 2),
    _CfgAfcAfmName_Type()
)
cfgAfcAfmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfcAfmName.setStatus("current")
_CfgAfcAfmIp_Type = IpAddress
_CfgAfcAfmIp_Object = MibTableColumn
cfgAfcAfmIp = _CfgAfcAfmIp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 10, 1, 3),
    _CfgAfcAfmIp_Type()
)
cfgAfcAfmIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfcAfmIp.setStatus("current")
_CfgAfcNeighbourOffsetTable_Object = MibTable
cfgAfcNeighbourOffsetTable = _CfgAfcNeighbourOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 40)
)
if mibBuilder.loadTexts:
    cfgAfcNeighbourOffsetTable.setStatus("current")
_CfgAfcNeighbourOffsetTableEntry_Object = MibTableRow
cfgAfcNeighbourOffsetTableEntry = _CfgAfcNeighbourOffsetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 40, 1)
)
cfgAfcNeighbourOffsetTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-NWM-MIB", "cfgAfcNeighbourOffsetTableIndex"),
)
if mibBuilder.loadTexts:
    cfgAfcNeighbourOffsetTableEntry.setStatus("current")


class _CfgAfcNeighbourOffsetTableIndex_Type(Integer32):
    """Custom type cfgAfcNeighbourOffsetTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CfgAfcNeighbourOffsetTableIndex_Type.__name__ = "Integer32"
_CfgAfcNeighbourOffsetTableIndex_Object = MibTableColumn
cfgAfcNeighbourOffsetTableIndex = _CfgAfcNeighbourOffsetTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 40, 1, 1),
    _CfgAfcNeighbourOffsetTableIndex_Type()
)
cfgAfcNeighbourOffsetTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgAfcNeighbourOffsetTableIndex.setStatus("current")


class _CfgAfcNeighbourOffset_Type(Integer32):
    """Custom type cfgAfcNeighbourOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 15),
    )


_CfgAfcNeighbourOffset_Type.__name__ = "Integer32"
_CfgAfcNeighbourOffset_Object = MibTableColumn
cfgAfcNeighbourOffset = _CfgAfcNeighbourOffset_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 1, 8, 40, 1, 2),
    _CfgAfcNeighbourOffset_Type()
)
cfgAfcNeighbourOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgAfcNeighbourOffset.setStatus("current")
_Rpc_ObjectIdentity = ObjectIdentity
rpc = _Rpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 3)
)
_RpcChannelManager_ObjectIdentity = ObjectIdentity
rpcChannelManager = _RpcChannelManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 3, 1)
)


class _RpcChMgrHttpReport_Type(Integer32):
    """Custom type rpcChMgrHttpReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nop", 0),
          ("freqstate", 1),
          ("channels", 2))
    )


_RpcChMgrHttpReport_Type.__name__ = "Integer32"
_RpcChMgrHttpReport_Object = MibScalar
rpcChMgrHttpReport = _RpcChMgrHttpReport_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 3, 1, 1),
    _RpcChMgrHttpReport_Type()
)
rpcChMgrHttpReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcChMgrHttpReport.setStatus("current")
_RpcNwm_ObjectIdentity = ObjectIdentity
rpcNwm = _RpcNwm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 3, 2)
)


class _RpcNwmHttpReport_Type(Integer32):
    """Custom type rpcNwmHttpReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nop", 0),
          ("status", 1),
          ("freqstate", 2))
    )


_RpcNwmHttpReport_Type.__name__ = "Integer32"
_RpcNwmHttpReport_Object = MibScalar
rpcNwmHttpReport = _RpcNwmHttpReport_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 3, 2, 1),
    _RpcNwmHttpReport_Type()
)
rpcNwmHttpReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcNwmHttpReport.setStatus("current")
_RpcNvram_ObjectIdentity = ObjectIdentity
rpcNvram = _RpcNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 3, 3)
)


class _RpcNvramFreqStatesReset_Type(Integer32):
    """Custom type rpcNvramFreqStatesReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reset", 0)
    )


_RpcNvramFreqStatesReset_Type.__name__ = "Integer32"
_RpcNvramFreqStatesReset_Object = MibScalar
rpcNvramFreqStatesReset = _RpcNvramFreqStatesReset_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 3, 3, 1),
    _RpcNvramFreqStatesReset_Type()
)
rpcNvramFreqStatesReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpcNvramFreqStatesReset.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1)
)
_GroupConfiguration_ObjectIdentity = ObjectIdentity
groupConfiguration = _GroupConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1)
)
_GroupCfgAfm_ObjectIdentity = ObjectIdentity
groupCfgAfm = _GroupCfgAfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 7)
)
_GroupCfgAfc_ObjectIdentity = ObjectIdentity
groupCfgAfc = _GroupCfgAfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 8)
)
_GroupRpc_ObjectIdentity = ObjectIdentity
groupRpc = _GroupRpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 2)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 2)
)

# Managed Objects groups

groupCfgHttpReport = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 1)
)
groupCfgHttpReport.setObjects(
    ("WESTERMO-SW6-NWM-MIB", "cfgHttpRprtServerUrl")
)
if mibBuilder.loadTexts:
    groupCfgHttpReport.setStatus("current")

groupCfgIdf = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 2)
)
groupCfgIdf.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "cfgIdfEnabled"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfInterval"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfName"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfTrigRadarCntTh"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfTrigChanLoadTh"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfTrigAlienLoadTh"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfTrigDomLoadTh"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfTrigAlienMaxRssiTh"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfTrigDomMaxRssiTh"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfScanWorkFreq"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfScanWorkAction"),
        ("WESTERMO-SW6-NWM-MIB", "cfgIdfScanWorkSeconds"))
)
if mibBuilder.loadTexts:
    groupCfgIdf.setStatus("current")

groupCfgChannelManager = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 4)
)
groupCfgChannelManager.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "cfgChMgrEnabled"),
        ("WESTERMO-SW6-NWM-MIB", "cfgChMgrUsableFrequencyList"),
        ("WESTERMO-SW6-NWM-MIB", "cfgChMgrDfsUseNvram"))
)
if mibBuilder.loadTexts:
    groupCfgChannelManager.setStatus("current")

groupCfgNwm = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 5)
)
groupCfgNwm.setObjects(
    ("WESTERMO-SW6-NWM-MIB", "cfgNwmEnabled")
)
if mibBuilder.loadTexts:
    groupCfgNwm.setStatus("current")

groupCfgChannelCleaner = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 6)
)
groupCfgChannelCleaner.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "cfgChanCleanEnabled"),
        ("WESTERMO-SW6-NWM-MIB", "cfgChanCleanDfsUseNvram"),
        ("WESTERMO-SW6-NWM-MIB", "cfgChanCleanUsableFrequencyList"))
)
if mibBuilder.loadTexts:
    groupCfgChannelCleaner.setStatus("current")

groupCfgAfmGlobal = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 7, 1)
)
groupCfgAfmGlobal.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "cfgAfmEnabled"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfmName"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfmIndex"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfmAreaSize"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfmPrimary"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfmReportEnabled"))
)
if mibBuilder.loadTexts:
    groupCfgAfmGlobal.setStatus("current")

groupCfgAfmRedundant = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 7, 2)
)
groupCfgAfmRedundant.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "cfgAfmRedundantIp"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfmRedundantName"))
)
if mibBuilder.loadTexts:
    groupCfgAfmRedundant.setStatus("current")

groupCfgAfmNeighbourTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 7, 3)
)
groupCfgAfmNeighbourTable.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "cfgAfmNeighbourIp"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfmNeighbourName"))
)
if mibBuilder.loadTexts:
    groupCfgAfmNeighbourTable.setStatus("current")

groupCfgAfmAfcTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 7, 4)
)
groupCfgAfmAfcTable.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "cfgAfmAfcIp"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfmAfcName"))
)
if mibBuilder.loadTexts:
    groupCfgAfmAfcTable.setStatus("current")

groupCfgAfcGlobal = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 8, 1)
)
groupCfgAfcGlobal.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "cfgAfcEnabled"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfcName"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfcIndex"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfcBackupFreq"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfcReportEnabled"))
)
if mibBuilder.loadTexts:
    groupCfgAfcGlobal.setStatus("current")

groupCfgAfcAfmTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 8, 2)
)
groupCfgAfcAfmTable.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "cfgAfcAfmIp"),
        ("WESTERMO-SW6-NWM-MIB", "cfgAfcAfmName"))
)
if mibBuilder.loadTexts:
    groupCfgAfcAfmTable.setStatus("current")

groupCfgAfcNeighbourOffsetTable = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 1, 8, 4)
)
groupCfgAfcNeighbourOffsetTable.setObjects(
    ("WESTERMO-SW6-NWM-MIB", "cfgAfcNeighbourOffset")
)
if mibBuilder.loadTexts:
    groupCfgAfcNeighbourOffsetTable.setStatus("current")

groupRpcChannelManager = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 2, 1)
)
groupRpcChannelManager.setObjects(
    ("WESTERMO-SW6-NWM-MIB", "rpcChMgrHttpReport")
)
if mibBuilder.loadTexts:
    groupRpcChannelManager.setStatus("current")

groupRpcNwm = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 2, 2)
)
groupRpcNwm.setObjects(
    ("WESTERMO-SW6-NWM-MIB", "rpcNwmHttpReport")
)
if mibBuilder.loadTexts:
    groupRpcNwm.setStatus("current")

groupRpcNvram = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 1, 2, 3)
)
groupRpcNvram.setObjects(
    ("WESTERMO-SW6-NWM-MIB", "rpcNvramFreqStatesReset")
)
if mibBuilder.loadTexts:
    groupRpcNvram.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 3, 10000, 2, 1)
)
compliance.setObjects(
      *(("WESTERMO-SW6-NWM-MIB", "groupCfgHttpReport"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgChannelManager"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgNwm"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgIdf"),
        ("WESTERMO-SW6-NWM-MIB", "groupRpcChannelManager"),
        ("WESTERMO-SW6-NWM-MIB", "groupRpcNwm"),
        ("WESTERMO-SW6-NWM-MIB", "groupRpcNvram"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgChannelCleaner"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgAfmGlobal"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgAfmRedundant"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgAfmNeighbourTable"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgAfmAfcTable"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgAfcGlobal"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgAfcAfmTable"),
        ("WESTERMO-SW6-NWM-MIB", "groupCfgAfcNeighbourOffsetTable"))
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-SW6-NWM-MIB",
    **{"nwm": nwm,
       "configuration": configuration,
       "cfgHttpReport": cfgHttpReport,
       "cfgHttpRprtServerUrl": cfgHttpRprtServerUrl,
       "cfgChannelManager": cfgChannelManager,
       "cfgChMgrEnabled": cfgChMgrEnabled,
       "cfgChMgrUsableFrequencyList": cfgChMgrUsableFrequencyList,
       "cfgChMgrDfsUseNvram": cfgChMgrDfsUseNvram,
       "cfgNwm": cfgNwm,
       "cfgNwmEnabled": cfgNwmEnabled,
       "cfgIdf": cfgIdf,
       "cfgIdfEnabled": cfgIdfEnabled,
       "cfgIdfInterval": cfgIdfInterval,
       "cfgIdfName": cfgIdfName,
       "cfgIdfTrigger": cfgIdfTrigger,
       "cfgIdfTrigRadarCntTh": cfgIdfTrigRadarCntTh,
       "cfgIdfTrigChanLoadTh": cfgIdfTrigChanLoadTh,
       "cfgIdfTrigAlienLoadTh": cfgIdfTrigAlienLoadTh,
       "cfgIdfTrigDomLoadTh": cfgIdfTrigDomLoadTh,
       "cfgIdfTrigAlienMaxRssiTh": cfgIdfTrigAlienMaxRssiTh,
       "cfgIdfTrigDomMaxRssiTh": cfgIdfTrigDomMaxRssiTh,
       "cfgIdfScanWorkTable": cfgIdfScanWorkTable,
       "cfgIdfScanWorkTableEntry": cfgIdfScanWorkTableEntry,
       "cfgIdfScanWorkIndex": cfgIdfScanWorkIndex,
       "cfgIdfScanWorkFreq": cfgIdfScanWorkFreq,
       "cfgIdfScanWorkAction": cfgIdfScanWorkAction,
       "cfgIdfScanWorkSeconds": cfgIdfScanWorkSeconds,
       "cfgChannelCleaner": cfgChannelCleaner,
       "cfgChanCleanEnabled": cfgChanCleanEnabled,
       "cfgChanCleanDfsUseNvram": cfgChanCleanDfsUseNvram,
       "cfgChanCleanUsableFrequencyList": cfgChanCleanUsableFrequencyList,
       "cfgAfm": cfgAfm,
       "cfgAfmEnabled": cfgAfmEnabled,
       "cfgAfmName": cfgAfmName,
       "cfgAfmIndex": cfgAfmIndex,
       "cfgAfmAreaSize": cfgAfmAreaSize,
       "cfgAfmPrimary": cfgAfmPrimary,
       "cfgAfmReportEnabled": cfgAfmReportEnabled,
       "cfgAfmRedundant": cfgAfmRedundant,
       "cfgAfmRedundantIp": cfgAfmRedundantIp,
       "cfgAfmRedundantName": cfgAfmRedundantName,
       "cfgAfmNeighbourTable": cfgAfmNeighbourTable,
       "cfgAfmNeighbourTableEntry": cfgAfmNeighbourTableEntry,
       "cfgAfmNeighbourTableIndex": cfgAfmNeighbourTableIndex,
       "cfgAfmNeighbourIp": cfgAfmNeighbourIp,
       "cfgAfmNeighbourName": cfgAfmNeighbourName,
       "cfgAfmAfcTable": cfgAfmAfcTable,
       "cfgAfmAfcTableEntry": cfgAfmAfcTableEntry,
       "cfgAfmAfcTableIndex": cfgAfmAfcTableIndex,
       "cfgAfmAfcName": cfgAfmAfcName,
       "cfgAfmAfcIp": cfgAfmAfcIp,
       "cfgAfc": cfgAfc,
       "cfgAfcEnabled": cfgAfcEnabled,
       "cfgAfcName": cfgAfcName,
       "cfgAfcIndex": cfgAfcIndex,
       "cfgAfcBackupFreq": cfgAfcBackupFreq,
       "cfgAfcReportEnabled": cfgAfcReportEnabled,
       "cfgAfcAfmTable": cfgAfcAfmTable,
       "cfgAfcAfmTableEntry": cfgAfcAfmTableEntry,
       "cfgAfcAfmTableIndex": cfgAfcAfmTableIndex,
       "cfgAfcAfmName": cfgAfcAfmName,
       "cfgAfcAfmIp": cfgAfcAfmIp,
       "cfgAfcNeighbourOffsetTable": cfgAfcNeighbourOffsetTable,
       "cfgAfcNeighbourOffsetTableEntry": cfgAfcNeighbourOffsetTableEntry,
       "cfgAfcNeighbourOffsetTableIndex": cfgAfcNeighbourOffsetTableIndex,
       "cfgAfcNeighbourOffset": cfgAfcNeighbourOffset,
       "rpc": rpc,
       "rpcChannelManager": rpcChannelManager,
       "rpcChMgrHttpReport": rpcChMgrHttpReport,
       "rpcNwm": rpcNwm,
       "rpcNwmHttpReport": rpcNwmHttpReport,
       "rpcNvram": rpcNvram,
       "rpcNvramFreqStatesReset": rpcNvramFreqStatesReset,
       "conformance": conformance,
       "groups": groups,
       "groupConfiguration": groupConfiguration,
       "groupCfgHttpReport": groupCfgHttpReport,
       "groupCfgIdf": groupCfgIdf,
       "groupCfgChannelManager": groupCfgChannelManager,
       "groupCfgNwm": groupCfgNwm,
       "groupCfgChannelCleaner": groupCfgChannelCleaner,
       "groupCfgAfm": groupCfgAfm,
       "groupCfgAfmGlobal": groupCfgAfmGlobal,
       "groupCfgAfmRedundant": groupCfgAfmRedundant,
       "groupCfgAfmNeighbourTable": groupCfgAfmNeighbourTable,
       "groupCfgAfmAfcTable": groupCfgAfmAfcTable,
       "groupCfgAfc": groupCfgAfc,
       "groupCfgAfcGlobal": groupCfgAfcGlobal,
       "groupCfgAfcAfmTable": groupCfgAfcAfmTable,
       "groupCfgAfcNeighbourOffsetTable": groupCfgAfcNeighbourOffsetTable,
       "groupRpc": groupRpc,
       "groupRpcChannelManager": groupRpcChannelManager,
       "groupRpcNwm": groupRpcNwm,
       "groupRpcNvram": groupRpcNvram,
       "compliances": compliances,
       "compliance": compliance}
)
