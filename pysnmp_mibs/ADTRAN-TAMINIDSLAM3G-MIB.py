# SNMP MIB module (ADTRAN-TAMINIDSLAM3G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TAMINIDSLAM3G-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:31 2025
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

(adTAMiniDslam3gID,) = mibBuilder.importSymbols(
    "ADTRAN-GENMINIDSLAM-MIB",
    "adTAMiniDslam3gID")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenMiniDslam3g = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3g.setRevisions(
        ("2014-09-04 00:00",
         "2013-03-22 00:00",
         "2012-06-27 00:00",
         "2011-09-21 00:00",
         "2011-09-09 00:00",
         "2010-10-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenMiniDslam3gMib_ObjectIdentity = ObjectIdentity
adGenMiniDslam3gMib = _AdGenMiniDslam3gMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1)
)
_AdGenMiniDslam3gInfoTable_Object = MibTable
adGenMiniDslam3gInfoTable = _AdGenMiniDslam3gInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoTable.setStatus("current")
_AdGenMiniDslam3gInfoEntry_Object = MibTableRow
adGenMiniDslam3gInfoEntry = _AdGenMiniDslam3gInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1)
)
adGenMiniDslam3gInfoEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoEntry.setStatus("current")


class _AdGenMiniDslam3gInfoUserTempThresh_Type(Integer32):
    """Custom type adGenMiniDslam3gInfoUserTempThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 125),
    )


_AdGenMiniDslam3gInfoUserTempThresh_Type.__name__ = "Integer32"
_AdGenMiniDslam3gInfoUserTempThresh_Object = MibTableColumn
adGenMiniDslam3gInfoUserTempThresh = _AdGenMiniDslam3gInfoUserTempThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 1),
    _AdGenMiniDslam3gInfoUserTempThresh_Type()
)
adGenMiniDslam3gInfoUserTempThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoUserTempThresh.setStatus("current")


class _AdGenMiniDslam3gInfoUserTempTrapEnable_Type(Integer32):
    """Custom type adGenMiniDslam3gInfoUserTempTrapEnable based on Integer32"""
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


_AdGenMiniDslam3gInfoUserTempTrapEnable_Type.__name__ = "Integer32"
_AdGenMiniDslam3gInfoUserTempTrapEnable_Object = MibTableColumn
adGenMiniDslam3gInfoUserTempTrapEnable = _AdGenMiniDslam3gInfoUserTempTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 2),
    _AdGenMiniDslam3gInfoUserTempTrapEnable_Type()
)
adGenMiniDslam3gInfoUserTempTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoUserTempTrapEnable.setStatus("current")


class _AdGenMiniDslam3gInfoDspWarmStartEnable_Type(Integer32):
    """Custom type adGenMiniDslam3gInfoDspWarmStartEnable based on Integer32"""
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


_AdGenMiniDslam3gInfoDspWarmStartEnable_Type.__name__ = "Integer32"
_AdGenMiniDslam3gInfoDspWarmStartEnable_Object = MibTableColumn
adGenMiniDslam3gInfoDspWarmStartEnable = _AdGenMiniDslam3gInfoDspWarmStartEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 3),
    _AdGenMiniDslam3gInfoDspWarmStartEnable_Type()
)
adGenMiniDslam3gInfoDspWarmStartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoDspWarmStartEnable.setStatus("current")


class _AdGenMiniDslam3gInfoCurrentTemp_Type(Integer32):
    """Custom type adGenMiniDslam3gInfoCurrentTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 125),
    )


_AdGenMiniDslam3gInfoCurrentTemp_Type.__name__ = "Integer32"
_AdGenMiniDslam3gInfoCurrentTemp_Object = MibTableColumn
adGenMiniDslam3gInfoCurrentTemp = _AdGenMiniDslam3gInfoCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 4),
    _AdGenMiniDslam3gInfoCurrentTemp_Type()
)
adGenMiniDslam3gInfoCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoCurrentTemp.setStatus("current")


class _AdGenMiniDslam3gInfoFanNumber_Type(Integer32):
    """Custom type adGenMiniDslam3gInfoFanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AdGenMiniDslam3gInfoFanNumber_Type.__name__ = "Integer32"
_AdGenMiniDslam3gInfoFanNumber_Object = MibTableColumn
adGenMiniDslam3gInfoFanNumber = _AdGenMiniDslam3gInfoFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 5),
    _AdGenMiniDslam3gInfoFanNumber_Type()
)
adGenMiniDslam3gInfoFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoFanNumber.setStatus("current")
_AdGenMiniDslam3gInfoDspWarmStartReason_Type = DisplayString
_AdGenMiniDslam3gInfoDspWarmStartReason_Object = MibTableColumn
adGenMiniDslam3gInfoDspWarmStartReason = _AdGenMiniDslam3gInfoDspWarmStartReason_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 6),
    _AdGenMiniDslam3gInfoDspWarmStartReason_Type()
)
adGenMiniDslam3gInfoDspWarmStartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoDspWarmStartReason.setStatus("current")


class _AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Type(Integer32):
    """Custom type adGenMiniDslam3gInfoDownstreamRateLimitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Type.__name__ = "Integer32"
_AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Object = MibTableColumn
adGenMiniDslam3gInfoDownstreamRateLimitPriority = _AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 7),
    _AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Type()
)
adGenMiniDslam3gInfoDownstreamRateLimitPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoDownstreamRateLimitPriority.setStatus("current")
_AdGenMiniDslam3gInfoCircuitIdChanges_Type = DisplayString
_AdGenMiniDslam3gInfoCircuitIdChanges_Object = MibTableColumn
adGenMiniDslam3gInfoCircuitIdChanges = _AdGenMiniDslam3gInfoCircuitIdChanges_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 8),
    _AdGenMiniDslam3gInfoCircuitIdChanges_Type()
)
adGenMiniDslam3gInfoCircuitIdChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoCircuitIdChanges.setStatus("current")
_AdGenMiniDslam3gInfoMCastSessionControlStartIP_Type = IpAddress
_AdGenMiniDslam3gInfoMCastSessionControlStartIP_Object = MibTableColumn
adGenMiniDslam3gInfoMCastSessionControlStartIP = _AdGenMiniDslam3gInfoMCastSessionControlStartIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 9),
    _AdGenMiniDslam3gInfoMCastSessionControlStartIP_Type()
)
adGenMiniDslam3gInfoMCastSessionControlStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoMCastSessionControlStartIP.setStatus("current")
_AdGenMiniDslam3gInfoMCastSessionControlEndIP_Type = IpAddress
_AdGenMiniDslam3gInfoMCastSessionControlEndIP_Object = MibTableColumn
adGenMiniDslam3gInfoMCastSessionControlEndIP = _AdGenMiniDslam3gInfoMCastSessionControlEndIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 10),
    _AdGenMiniDslam3gInfoMCastSessionControlEndIP_Type()
)
adGenMiniDslam3gInfoMCastSessionControlEndIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoMCastSessionControlEndIP.setStatus("current")
_AdGenMiniDslam3gInfoMCastSessionControlBitrate_Type = Integer32
_AdGenMiniDslam3gInfoMCastSessionControlBitrate_Object = MibTableColumn
adGenMiniDslam3gInfoMCastSessionControlBitrate = _AdGenMiniDslam3gInfoMCastSessionControlBitrate_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 11),
    _AdGenMiniDslam3gInfoMCastSessionControlBitrate_Type()
)
adGenMiniDslam3gInfoMCastSessionControlBitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoMCastSessionControlBitrate.setStatus("current")
_AdGenMiniDslam3gInfoMacAgingTime_Type = Unsigned32
_AdGenMiniDslam3gInfoMacAgingTime_Object = MibTableColumn
adGenMiniDslam3gInfoMacAgingTime = _AdGenMiniDslam3gInfoMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 12),
    _AdGenMiniDslam3gInfoMacAgingTime_Type()
)
adGenMiniDslam3gInfoMacAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoMacAgingTime.setStatus("current")


class _AdGenMiniDslam3gInfoLegacyDeployment_Type(Integer32):
    """Custom type adGenMiniDslam3gInfoLegacyDeployment based on Integer32"""
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


_AdGenMiniDslam3gInfoLegacyDeployment_Type.__name__ = "Integer32"
_AdGenMiniDslam3gInfoLegacyDeployment_Object = MibTableColumn
adGenMiniDslam3gInfoLegacyDeployment = _AdGenMiniDslam3gInfoLegacyDeployment_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 13),
    _AdGenMiniDslam3gInfoLegacyDeployment_Type()
)
adGenMiniDslam3gInfoLegacyDeployment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoLegacyDeployment.setStatus("current")


class _AdGenMiniDslam3gInfoBondingMode_Type(Integer32):
    """Custom type adGenMiniDslam3gInfoBondingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("efm", 2))
    )


_AdGenMiniDslam3gInfoBondingMode_Type.__name__ = "Integer32"
_AdGenMiniDslam3gInfoBondingMode_Object = MibTableColumn
adGenMiniDslam3gInfoBondingMode = _AdGenMiniDslam3gInfoBondingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 1, 1, 14),
    _AdGenMiniDslam3gInfoBondingMode_Type()
)
adGenMiniDslam3gInfoBondingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gInfoBondingMode.setStatus("current")
_AdGenMiniDslam3gTraps_ObjectIdentity = ObjectIdentity
adGenMiniDslam3gTraps = _AdGenMiniDslam3gTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2)
)
_AdGenMiniDslam3gTrapsv1Patch_ObjectIdentity = ObjectIdentity
adGenMiniDslam3gTrapsv1Patch = _AdGenMiniDslam3gTrapsv1Patch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0)
)
_AdGenMiniDslam3gTestTable_Object = MibTable
adGenMiniDslam3gTestTable = _AdGenMiniDslam3gTestTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gTestTable.setStatus("current")
_AdGenMiniDslam3gTestEntry_Object = MibTableRow
adGenMiniDslam3gTestEntry = _AdGenMiniDslam3gTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 3, 1)
)
adGenMiniDslam3gTestEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gTestEntry.setStatus("current")


class _AdGenMiniDslam3gTestPortNumber_Type(Integer32):
    """Custom type adGenMiniDslam3gTestPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AdGenMiniDslam3gTestPortNumber_Type.__name__ = "Integer32"
_AdGenMiniDslam3gTestPortNumber_Object = MibTableColumn
adGenMiniDslam3gTestPortNumber = _AdGenMiniDslam3gTestPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 3, 1, 1),
    _AdGenMiniDslam3gTestPortNumber_Type()
)
adGenMiniDslam3gTestPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gTestPortNumber.setStatus("current")
_AdGenMiniDslam3gTestFilename_Type = DisplayString
_AdGenMiniDslam3gTestFilename_Object = MibTableColumn
adGenMiniDslam3gTestFilename = _AdGenMiniDslam3gTestFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 3, 1, 2),
    _AdGenMiniDslam3gTestFilename_Type()
)
adGenMiniDslam3gTestFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gTestFilename.setStatus("current")


class _AdGenMiniDslam3gSELTTestStart_Type(Integer32):
    """Custom type adGenMiniDslam3gSELTTestStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_AdGenMiniDslam3gSELTTestStart_Type.__name__ = "Integer32"
_AdGenMiniDslam3gSELTTestStart_Object = MibTableColumn
adGenMiniDslam3gSELTTestStart = _AdGenMiniDslam3gSELTTestStart_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 3, 1, 3),
    _AdGenMiniDslam3gSELTTestStart_Type()
)
adGenMiniDslam3gSELTTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gSELTTestStart.setStatus("current")


class _AdGenMiniDslam3gDELTTestStart_Type(Integer32):
    """Custom type adGenMiniDslam3gDELTTestStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_AdGenMiniDslam3gDELTTestStart_Type.__name__ = "Integer32"
_AdGenMiniDslam3gDELTTestStart_Object = MibTableColumn
adGenMiniDslam3gDELTTestStart = _AdGenMiniDslam3gDELTTestStart_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 3, 1, 4),
    _AdGenMiniDslam3gDELTTestStart_Type()
)
adGenMiniDslam3gDELTTestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gDELTTestStart.setStatus("current")


class _AdGenMiniDslam3gTestStop_Type(Integer32):
    """Custom type adGenMiniDslam3gTestStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stop", 1)
    )


_AdGenMiniDslam3gTestStop_Type.__name__ = "Integer32"
_AdGenMiniDslam3gTestStop_Object = MibTableColumn
adGenMiniDslam3gTestStop = _AdGenMiniDslam3gTestStop_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 3, 1, 5),
    _AdGenMiniDslam3gTestStop_Type()
)
adGenMiniDslam3gTestStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gTestStop.setStatus("current")
_AdGenMiniDslam3gTestSELTDELTStatus_Type = DisplayString
_AdGenMiniDslam3gTestSELTDELTStatus_Object = MibTableColumn
adGenMiniDslam3gTestSELTDELTStatus = _AdGenMiniDslam3gTestSELTDELTStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 3, 1, 6),
    _AdGenMiniDslam3gTestSELTDELTStatus_Type()
)
adGenMiniDslam3gTestSELTDELTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gTestSELTDELTStatus.setStatus("current")
_AdGenMiniDslam3gAdslProvTable_Object = MibTable
adGenMiniDslam3gAdslProvTable = _AdGenMiniDslam3gAdslProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gAdslProvTable.setStatus("current")
_AdGenMiniDslam3gAdslProvEntry_Object = MibTableRow
adGenMiniDslam3gAdslProvEntry = _AdGenMiniDslam3gAdslProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 4, 1)
)
adGenMiniDslam3gAdslProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gAdslProvEntry.setStatus("current")


class _AdGenMiniDslam3gAdslProvRetrainUasNe_Type(Integer32):
    """Custom type adGenMiniDslam3gAdslProvRetrainUasNe based on Integer32"""
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


_AdGenMiniDslam3gAdslProvRetrainUasNe_Type.__name__ = "Integer32"
_AdGenMiniDslam3gAdslProvRetrainUasNe_Object = MibTableColumn
adGenMiniDslam3gAdslProvRetrainUasNe = _AdGenMiniDslam3gAdslProvRetrainUasNe_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 4, 1, 1),
    _AdGenMiniDslam3gAdslProvRetrainUasNe_Type()
)
adGenMiniDslam3gAdslProvRetrainUasNe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gAdslProvRetrainUasNe.setStatus("current")


class _AdGenMiniDslam3gAdslProvRetrainMarginNe_Type(Integer32):
    """Custom type adGenMiniDslam3gAdslProvRetrainMarginNe based on Integer32"""
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


_AdGenMiniDslam3gAdslProvRetrainMarginNe_Type.__name__ = "Integer32"
_AdGenMiniDslam3gAdslProvRetrainMarginNe_Object = MibTableColumn
adGenMiniDslam3gAdslProvRetrainMarginNe = _AdGenMiniDslam3gAdslProvRetrainMarginNe_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 4, 1, 2),
    _AdGenMiniDslam3gAdslProvRetrainMarginNe_Type()
)
adGenMiniDslam3gAdslProvRetrainMarginNe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gAdslProvRetrainMarginNe.setStatus("current")


class _AdGenMiniDslam3gAdslProvRetrainSesFe_Type(Integer32):
    """Custom type adGenMiniDslam3gAdslProvRetrainSesFe based on Integer32"""
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


_AdGenMiniDslam3gAdslProvRetrainSesFe_Type.__name__ = "Integer32"
_AdGenMiniDslam3gAdslProvRetrainSesFe_Object = MibTableColumn
adGenMiniDslam3gAdslProvRetrainSesFe = _AdGenMiniDslam3gAdslProvRetrainSesFe_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 4, 1, 3),
    _AdGenMiniDslam3gAdslProvRetrainSesFe_Type()
)
adGenMiniDslam3gAdslProvRetrainSesFe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gAdslProvRetrainSesFe.setStatus("current")


class _AdGenMiniDslam3gAdslProvRetrainUasFe_Type(Integer32):
    """Custom type adGenMiniDslam3gAdslProvRetrainUasFe based on Integer32"""
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


_AdGenMiniDslam3gAdslProvRetrainUasFe_Type.__name__ = "Integer32"
_AdGenMiniDslam3gAdslProvRetrainUasFe_Object = MibTableColumn
adGenMiniDslam3gAdslProvRetrainUasFe = _AdGenMiniDslam3gAdslProvRetrainUasFe_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 4, 1, 4),
    _AdGenMiniDslam3gAdslProvRetrainUasFe_Type()
)
adGenMiniDslam3gAdslProvRetrainUasFe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gAdslProvRetrainUasFe.setStatus("current")


class _AdGenMiniDslam3gAdslProvRetrainMarginFe_Type(Integer32):
    """Custom type adGenMiniDslam3gAdslProvRetrainMarginFe based on Integer32"""
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


_AdGenMiniDslam3gAdslProvRetrainMarginFe_Type.__name__ = "Integer32"
_AdGenMiniDslam3gAdslProvRetrainMarginFe_Object = MibTableColumn
adGenMiniDslam3gAdslProvRetrainMarginFe = _AdGenMiniDslam3gAdslProvRetrainMarginFe_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 4, 1, 5),
    _AdGenMiniDslam3gAdslProvRetrainMarginFe_Type()
)
adGenMiniDslam3gAdslProvRetrainMarginFe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gAdslProvRetrainMarginFe.setStatus("current")
_AdGenMiniDslam3gAdslProvDownstreamRateLimit_Type = Integer32
_AdGenMiniDslam3gAdslProvDownstreamRateLimit_Object = MibTableColumn
adGenMiniDslam3gAdslProvDownstreamRateLimit = _AdGenMiniDslam3gAdslProvDownstreamRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 4, 1, 6),
    _AdGenMiniDslam3gAdslProvDownstreamRateLimit_Type()
)
adGenMiniDslam3gAdslProvDownstreamRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gAdslProvDownstreamRateLimit.setStatus("current")
_AdGenMiniDslam3gMacTable_Object = MibTable
adGenMiniDslam3gMacTable = _AdGenMiniDslam3gMacTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacTable.setStatus("current")
_AdGenMiniDslam3gMacEntry_Object = MibTableRow
adGenMiniDslam3gMacEntry = _AdGenMiniDslam3gMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1)
)
adGenMiniDslam3gMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gMacIndex"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacEntry.setStatus("current")
_AdGenMiniDslam3gMacIndex_Type = Unsigned32
_AdGenMiniDslam3gMacIndex_Object = MibTableColumn
adGenMiniDslam3gMacIndex = _AdGenMiniDslam3gMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 1),
    _AdGenMiniDslam3gMacIndex_Type()
)
adGenMiniDslam3gMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacIndex.setStatus("current")
_AdGenMiniDslam3gMacAddress_Type = OctetString
_AdGenMiniDslam3gMacAddress_Object = MibTableColumn
adGenMiniDslam3gMacAddress = _AdGenMiniDslam3gMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 2),
    _AdGenMiniDslam3gMacAddress_Type()
)
adGenMiniDslam3gMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacAddress.setStatus("current")


class _AdGenMiniDslam3gMacVID_Type(Integer32):
    """Custom type adGenMiniDslam3gMacVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AdGenMiniDslam3gMacVID_Type.__name__ = "Integer32"
_AdGenMiniDslam3gMacVID_Object = MibTableColumn
adGenMiniDslam3gMacVID = _AdGenMiniDslam3gMacVID_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 3),
    _AdGenMiniDslam3gMacVID_Type()
)
adGenMiniDslam3gMacVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacVID.setStatus("current")


class _AdGenMiniDslam3gMacType_Type(Integer32):
    """Custom type adGenMiniDslam3gMacType based on Integer32"""
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
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4))
    )


_AdGenMiniDslam3gMacType_Type.__name__ = "Integer32"
_AdGenMiniDslam3gMacType_Object = MibTableColumn
adGenMiniDslam3gMacType = _AdGenMiniDslam3gMacType_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 4),
    _AdGenMiniDslam3gMacType_Type()
)
adGenMiniDslam3gMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacType.setStatus("current")
_AdGenMiniDslam3gMacIP_Type = IpAddress
_AdGenMiniDslam3gMacIP_Object = MibTableColumn
adGenMiniDslam3gMacIP = _AdGenMiniDslam3gMacIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 5),
    _AdGenMiniDslam3gMacIP_Type()
)
adGenMiniDslam3gMacIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacIP.setStatus("current")
_AdGenMiniDslam3gMacLeaseTime_Type = Unsigned32
_AdGenMiniDslam3gMacLeaseTime_Object = MibTableColumn
adGenMiniDslam3gMacLeaseTime = _AdGenMiniDslam3gMacLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 6),
    _AdGenMiniDslam3gMacLeaseTime_Type()
)
adGenMiniDslam3gMacLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacLeaseTime.setStatus("current")
_AdGenMiniDslam3gMacGatewayMac_Type = OctetString
_AdGenMiniDslam3gMacGatewayMac_Object = MibTableColumn
adGenMiniDslam3gMacGatewayMac = _AdGenMiniDslam3gMacGatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 7),
    _AdGenMiniDslam3gMacGatewayMac_Type()
)
adGenMiniDslam3gMacGatewayMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacGatewayMac.setStatus("current")
_AdGenMiniDslam3gMacGatewayIP_Type = IpAddress
_AdGenMiniDslam3gMacGatewayIP_Object = MibTableColumn
adGenMiniDslam3gMacGatewayIP = _AdGenMiniDslam3gMacGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 8),
    _AdGenMiniDslam3gMacGatewayIP_Type()
)
adGenMiniDslam3gMacGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacGatewayIP.setStatus("current")
_AdGenMiniDslam3gMacInterfaceState_Type = Unsigned32
_AdGenMiniDslam3gMacInterfaceState_Object = MibTableColumn
adGenMiniDslam3gMacInterfaceState = _AdGenMiniDslam3gMacInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 9),
    _AdGenMiniDslam3gMacInterfaceState_Type()
)
adGenMiniDslam3gMacInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacInterfaceState.setStatus("current")
_AdGenMiniDslam3gMacXid_Type = Unsigned32
_AdGenMiniDslam3gMacXid_Object = MibTableColumn
adGenMiniDslam3gMacXid = _AdGenMiniDslam3gMacXid_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 10),
    _AdGenMiniDslam3gMacXid_Type()
)
adGenMiniDslam3gMacXid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacXid.setStatus("current")
_AdGenMiniDslam3gMacEncapsulationMode_Type = Unsigned32
_AdGenMiniDslam3gMacEncapsulationMode_Object = MibTableColumn
adGenMiniDslam3gMacEncapsulationMode = _AdGenMiniDslam3gMacEncapsulationMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 11),
    _AdGenMiniDslam3gMacEncapsulationMode_Type()
)
adGenMiniDslam3gMacEncapsulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacEncapsulationMode.setStatus("current")
_AdGenMiniDslam3gMacStartTime_Type = Unsigned32
_AdGenMiniDslam3gMacStartTime_Object = MibTableColumn
adGenMiniDslam3gMacStartTime = _AdGenMiniDslam3gMacStartTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 12),
    _AdGenMiniDslam3gMacStartTime_Type()
)
adGenMiniDslam3gMacStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacStartTime.setStatus("current")
_AdGenMiniDslam3gMacVpi_Type = Unsigned32
_AdGenMiniDslam3gMacVpi_Object = MibTableColumn
adGenMiniDslam3gMacVpi = _AdGenMiniDslam3gMacVpi_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 13),
    _AdGenMiniDslam3gMacVpi_Type()
)
adGenMiniDslam3gMacVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacVpi.setStatus("current")
_AdGenMiniDslam3gMacVci_Type = Unsigned32
_AdGenMiniDslam3gMacVci_Object = MibTableColumn
adGenMiniDslam3gMacVci = _AdGenMiniDslam3gMacVci_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 14),
    _AdGenMiniDslam3gMacVci_Type()
)
adGenMiniDslam3gMacVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacVci.setStatus("current")


class _AdGenMiniDslam3gMacCTag_Type(Integer32):
    """Custom type adGenMiniDslam3gMacCTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4098),
    )


_AdGenMiniDslam3gMacCTag_Type.__name__ = "Integer32"
_AdGenMiniDslam3gMacCTag_Object = MibTableColumn
adGenMiniDslam3gMacCTag = _AdGenMiniDslam3gMacCTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 15),
    _AdGenMiniDslam3gMacCTag_Type()
)
adGenMiniDslam3gMacCTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacCTag.setStatus("current")


class _AdGenMiniDslam3gMacCEVlan_Type(Integer32):
    """Custom type adGenMiniDslam3gMacCEVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4098),
    )


_AdGenMiniDslam3gMacCEVlan_Type.__name__ = "Integer32"
_AdGenMiniDslam3gMacCEVlan_Object = MibTableColumn
adGenMiniDslam3gMacCEVlan = _AdGenMiniDslam3gMacCEVlan_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 16),
    _AdGenMiniDslam3gMacCEVlan_Type()
)
adGenMiniDslam3gMacCEVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacCEVlan.setStatus("current")
_AdGenMiniDslam3gMacIpAddressType_Type = InetAddressType
_AdGenMiniDslam3gMacIpAddressType_Object = MibTableColumn
adGenMiniDslam3gMacIpAddressType = _AdGenMiniDslam3gMacIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 17),
    _AdGenMiniDslam3gMacIpAddressType_Type()
)
adGenMiniDslam3gMacIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacIpAddressType.setStatus("current")
_AdGenMiniDslam3gMacIpAddress_Type = InetAddress
_AdGenMiniDslam3gMacIpAddress_Object = MibTableColumn
adGenMiniDslam3gMacIpAddress = _AdGenMiniDslam3gMacIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 18),
    _AdGenMiniDslam3gMacIpAddress_Type()
)
adGenMiniDslam3gMacIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacIpAddress.setStatus("current")
_AdGenMiniDslam3gMacIpAddressPrefix_Type = InetAddressPrefixLength
_AdGenMiniDslam3gMacIpAddressPrefix_Object = MibTableColumn
adGenMiniDslam3gMacIpAddressPrefix = _AdGenMiniDslam3gMacIpAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 5, 1, 19),
    _AdGenMiniDslam3gMacIpAddressPrefix_Type()
)
adGenMiniDslam3gMacIpAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gMacIpAddressPrefix.setStatus("current")
_AdGenMiniDslam3gPerf_ObjectIdentity = ObjectIdentity
adGenMiniDslam3gPerf = _AdGenMiniDslam3gPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6)
)
_AdGenMiniDslam3gPerf15MinCurrTable_Object = MibTable
adGenMiniDslam3gPerf15MinCurrTable = _AdGenMiniDslam3gPerf15MinCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinCurrTable.setStatus("current")
_AdGenMiniDslam3gPerf15MinCurrEntry_Object = MibTableRow
adGenMiniDslam3gPerf15MinCurrEntry = _AdGenMiniDslam3gPerf15MinCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 1, 1)
)
adGenMiniDslam3gPerf15MinCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinCurrEntry.setStatus("current")
_AdGenMiniDslam3gPerf15MinCurrIngressPackets_Type = Counter32
_AdGenMiniDslam3gPerf15MinCurrIngressPackets_Object = MibTableColumn
adGenMiniDslam3gPerf15MinCurrIngressPackets = _AdGenMiniDslam3gPerf15MinCurrIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 1, 1, 1),
    _AdGenMiniDslam3gPerf15MinCurrIngressPackets_Type()
)
adGenMiniDslam3gPerf15MinCurrIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinCurrIngressPackets.setStatus("current")
_AdGenMiniDslam3gPerf15MinCurrIngressBytes_Type = Counter32
_AdGenMiniDslam3gPerf15MinCurrIngressBytes_Object = MibTableColumn
adGenMiniDslam3gPerf15MinCurrIngressBytes = _AdGenMiniDslam3gPerf15MinCurrIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 1, 1, 2),
    _AdGenMiniDslam3gPerf15MinCurrIngressBytes_Type()
)
adGenMiniDslam3gPerf15MinCurrIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinCurrIngressBytes.setStatus("current")
_AdGenMiniDslam3gPerf15MinCurrEgressPackets_Type = Counter32
_AdGenMiniDslam3gPerf15MinCurrEgressPackets_Object = MibTableColumn
adGenMiniDslam3gPerf15MinCurrEgressPackets = _AdGenMiniDslam3gPerf15MinCurrEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 1, 1, 3),
    _AdGenMiniDslam3gPerf15MinCurrEgressPackets_Type()
)
adGenMiniDslam3gPerf15MinCurrEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinCurrEgressPackets.setStatus("current")
_AdGenMiniDslam3gPerf15MinCurrEgressBytes_Type = Counter32
_AdGenMiniDslam3gPerf15MinCurrEgressBytes_Object = MibTableColumn
adGenMiniDslam3gPerf15MinCurrEgressBytes = _AdGenMiniDslam3gPerf15MinCurrEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 1, 1, 4),
    _AdGenMiniDslam3gPerf15MinCurrEgressBytes_Type()
)
adGenMiniDslam3gPerf15MinCurrEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinCurrEgressBytes.setStatus("current")
_AdGenMiniDslam3gPerf15MinCurrEgressOverflowPackets_Type = Counter32
_AdGenMiniDslam3gPerf15MinCurrEgressOverflowPackets_Object = MibTableColumn
adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets = _AdGenMiniDslam3gPerf15MinCurrEgressOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 1, 1, 5),
    _AdGenMiniDslam3gPerf15MinCurrEgressOverflowPackets_Type()
)
adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets.setStatus("current")
_AdGenMiniDslam3gPerf15MinCurrEgressOverflowBytes_Type = Counter32
_AdGenMiniDslam3gPerf15MinCurrEgressOverflowBytes_Object = MibTableColumn
adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes = _AdGenMiniDslam3gPerf15MinCurrEgressOverflowBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 1, 1, 6),
    _AdGenMiniDslam3gPerf15MinCurrEgressOverflowBytes_Type()
)
adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes.setStatus("current")
_AdGenMiniDslam3gPerf15MinCurrValidIntervals_Type = Unsigned32
_AdGenMiniDslam3gPerf15MinCurrValidIntervals_Object = MibTableColumn
adGenMiniDslam3gPerf15MinCurrValidIntervals = _AdGenMiniDslam3gPerf15MinCurrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 1, 1, 7),
    _AdGenMiniDslam3gPerf15MinCurrValidIntervals_Type()
)
adGenMiniDslam3gPerf15MinCurrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinCurrValidIntervals.setStatus("current")
_AdGenMiniDslam3gPerf15MinIntTable_Object = MibTable
adGenMiniDslam3gPerf15MinIntTable = _AdGenMiniDslam3gPerf15MinIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinIntTable.setStatus("current")
_AdGenMiniDslam3gPerf15MinIntEntry_Object = MibTableRow
adGenMiniDslam3gPerf15MinIntEntry = _AdGenMiniDslam3gPerf15MinIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 2, 1)
)
adGenMiniDslam3gPerf15MinIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gPerf15MinIntInterval"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinIntEntry.setStatus("current")
_AdGenMiniDslam3gPerf15MinIntInterval_Type = Integer32
_AdGenMiniDslam3gPerf15MinIntInterval_Object = MibTableColumn
adGenMiniDslam3gPerf15MinIntInterval = _AdGenMiniDslam3gPerf15MinIntInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 2, 1, 1),
    _AdGenMiniDslam3gPerf15MinIntInterval_Type()
)
adGenMiniDslam3gPerf15MinIntInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinIntInterval.setStatus("current")
_AdGenMiniDslam3gPerf15MinIntIngressPackets_Type = Counter32
_AdGenMiniDslam3gPerf15MinIntIngressPackets_Object = MibTableColumn
adGenMiniDslam3gPerf15MinIntIngressPackets = _AdGenMiniDslam3gPerf15MinIntIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 2, 1, 2),
    _AdGenMiniDslam3gPerf15MinIntIngressPackets_Type()
)
adGenMiniDslam3gPerf15MinIntIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinIntIngressPackets.setStatus("current")
_AdGenMiniDslam3gPerf15MinIntIngressBytes_Type = Counter32
_AdGenMiniDslam3gPerf15MinIntIngressBytes_Object = MibTableColumn
adGenMiniDslam3gPerf15MinIntIngressBytes = _AdGenMiniDslam3gPerf15MinIntIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 2, 1, 3),
    _AdGenMiniDslam3gPerf15MinIntIngressBytes_Type()
)
adGenMiniDslam3gPerf15MinIntIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinIntIngressBytes.setStatus("current")
_AdGenMiniDslam3gPerf15MinIntEgressPackets_Type = Counter32
_AdGenMiniDslam3gPerf15MinIntEgressPackets_Object = MibTableColumn
adGenMiniDslam3gPerf15MinIntEgressPackets = _AdGenMiniDslam3gPerf15MinIntEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 2, 1, 4),
    _AdGenMiniDslam3gPerf15MinIntEgressPackets_Type()
)
adGenMiniDslam3gPerf15MinIntEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinIntEgressPackets.setStatus("current")
_AdGenMiniDslam3gPerf15MinIntEgressBytes_Type = Counter32
_AdGenMiniDslam3gPerf15MinIntEgressBytes_Object = MibTableColumn
adGenMiniDslam3gPerf15MinIntEgressBytes = _AdGenMiniDslam3gPerf15MinIntEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 2, 1, 5),
    _AdGenMiniDslam3gPerf15MinIntEgressBytes_Type()
)
adGenMiniDslam3gPerf15MinIntEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinIntEgressBytes.setStatus("current")
_AdGenMiniDslam3gPerf15MinIntEgressOverflowPackets_Type = Counter32
_AdGenMiniDslam3gPerf15MinIntEgressOverflowPackets_Object = MibTableColumn
adGenMiniDslam3gPerf15MinIntEgressOverflowPackets = _AdGenMiniDslam3gPerf15MinIntEgressOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 2, 1, 6),
    _AdGenMiniDslam3gPerf15MinIntEgressOverflowPackets_Type()
)
adGenMiniDslam3gPerf15MinIntEgressOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinIntEgressOverflowPackets.setStatus("current")
_AdGenMiniDslam3gPerf15MinIntEgressOverflowBytes_Type = Counter32
_AdGenMiniDslam3gPerf15MinIntEgressOverflowBytes_Object = MibTableColumn
adGenMiniDslam3gPerf15MinIntEgressOverflowBytes = _AdGenMiniDslam3gPerf15MinIntEgressOverflowBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 2, 1, 7),
    _AdGenMiniDslam3gPerf15MinIntEgressOverflowBytes_Type()
)
adGenMiniDslam3gPerf15MinIntEgressOverflowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerf15MinIntEgressOverflowBytes.setStatus("current")
_AdGenMiniDslam3gPerfDailyCurrTable_Object = MibTable
adGenMiniDslam3gPerfDailyCurrTable = _AdGenMiniDslam3gPerfDailyCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyCurrTable.setStatus("current")
_AdGenMiniDslam3gPerfDailyCurrEntry_Object = MibTableRow
adGenMiniDslam3gPerfDailyCurrEntry = _AdGenMiniDslam3gPerfDailyCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 3, 1)
)
adGenMiniDslam3gPerfDailyCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyCurrEntry.setStatus("current")
_AdGenMiniDslam3gPerfDailyCurrIngressPackets_Type = Counter32
_AdGenMiniDslam3gPerfDailyCurrIngressPackets_Object = MibTableColumn
adGenMiniDslam3gPerfDailyCurrIngressPackets = _AdGenMiniDslam3gPerfDailyCurrIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 3, 1, 1),
    _AdGenMiniDslam3gPerfDailyCurrIngressPackets_Type()
)
adGenMiniDslam3gPerfDailyCurrIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyCurrIngressPackets.setStatus("current")
_AdGenMiniDslam3gPerfDailyCurrIngressBytes_Type = Counter32
_AdGenMiniDslam3gPerfDailyCurrIngressBytes_Object = MibTableColumn
adGenMiniDslam3gPerfDailyCurrIngressBytes = _AdGenMiniDslam3gPerfDailyCurrIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 3, 1, 2),
    _AdGenMiniDslam3gPerfDailyCurrIngressBytes_Type()
)
adGenMiniDslam3gPerfDailyCurrIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyCurrIngressBytes.setStatus("current")
_AdGenMiniDslam3gPerfDailyCurrEgressPackets_Type = Counter32
_AdGenMiniDslam3gPerfDailyCurrEgressPackets_Object = MibTableColumn
adGenMiniDslam3gPerfDailyCurrEgressPackets = _AdGenMiniDslam3gPerfDailyCurrEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 3, 1, 3),
    _AdGenMiniDslam3gPerfDailyCurrEgressPackets_Type()
)
adGenMiniDslam3gPerfDailyCurrEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyCurrEgressPackets.setStatus("current")
_AdGenMiniDslam3gPerfDailyCurrEgressBytes_Type = Counter32
_AdGenMiniDslam3gPerfDailyCurrEgressBytes_Object = MibTableColumn
adGenMiniDslam3gPerfDailyCurrEgressBytes = _AdGenMiniDslam3gPerfDailyCurrEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 3, 1, 4),
    _AdGenMiniDslam3gPerfDailyCurrEgressBytes_Type()
)
adGenMiniDslam3gPerfDailyCurrEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyCurrEgressBytes.setStatus("current")
_AdGenMiniDslam3gPerfDailyCurrEgressOverflowPackets_Type = Counter32
_AdGenMiniDslam3gPerfDailyCurrEgressOverflowPackets_Object = MibTableColumn
adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets = _AdGenMiniDslam3gPerfDailyCurrEgressOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 3, 1, 5),
    _AdGenMiniDslam3gPerfDailyCurrEgressOverflowPackets_Type()
)
adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets.setStatus("current")
_AdGenMiniDslam3gPerfDailyCurrEgressOverflowBytes_Type = Counter32
_AdGenMiniDslam3gPerfDailyCurrEgressOverflowBytes_Object = MibTableColumn
adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes = _AdGenMiniDslam3gPerfDailyCurrEgressOverflowBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 3, 1, 6),
    _AdGenMiniDslam3gPerfDailyCurrEgressOverflowBytes_Type()
)
adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes.setStatus("current")
_AdGenMiniDslam3gPerfDailyCurrValidIntervals_Type = Unsigned32
_AdGenMiniDslam3gPerfDailyCurrValidIntervals_Object = MibTableColumn
adGenMiniDslam3gPerfDailyCurrValidIntervals = _AdGenMiniDslam3gPerfDailyCurrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 3, 1, 7),
    _AdGenMiniDslam3gPerfDailyCurrValidIntervals_Type()
)
adGenMiniDslam3gPerfDailyCurrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyCurrValidIntervals.setStatus("current")
_AdGenMiniDslam3gPerfDailyIntTable_Object = MibTable
adGenMiniDslam3gPerfDailyIntTable = _AdGenMiniDslam3gPerfDailyIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyIntTable.setStatus("current")
_AdGenMiniDslam3gPerfDailyIntEntry_Object = MibTableRow
adGenMiniDslam3gPerfDailyIntEntry = _AdGenMiniDslam3gPerfDailyIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 4, 1)
)
adGenMiniDslam3gPerfDailyIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gPerfDailyIntInterval"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyIntEntry.setStatus("current")
_AdGenMiniDslam3gPerfDailyIntInterval_Type = Integer32
_AdGenMiniDslam3gPerfDailyIntInterval_Object = MibTableColumn
adGenMiniDslam3gPerfDailyIntInterval = _AdGenMiniDslam3gPerfDailyIntInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 4, 1, 1),
    _AdGenMiniDslam3gPerfDailyIntInterval_Type()
)
adGenMiniDslam3gPerfDailyIntInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyIntInterval.setStatus("current")
_AdGenMiniDslam3gPerfDailyIntIngressPackets_Type = Counter32
_AdGenMiniDslam3gPerfDailyIntIngressPackets_Object = MibTableColumn
adGenMiniDslam3gPerfDailyIntIngressPackets = _AdGenMiniDslam3gPerfDailyIntIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 4, 1, 2),
    _AdGenMiniDslam3gPerfDailyIntIngressPackets_Type()
)
adGenMiniDslam3gPerfDailyIntIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyIntIngressPackets.setStatus("current")
_AdGenMiniDslam3gPerfDailyIntIngressBytes_Type = Counter32
_AdGenMiniDslam3gPerfDailyIntIngressBytes_Object = MibTableColumn
adGenMiniDslam3gPerfDailyIntIngressBytes = _AdGenMiniDslam3gPerfDailyIntIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 4, 1, 3),
    _AdGenMiniDslam3gPerfDailyIntIngressBytes_Type()
)
adGenMiniDslam3gPerfDailyIntIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyIntIngressBytes.setStatus("current")
_AdGenMiniDslam3gPerfDailyIntEgressPackets_Type = Counter32
_AdGenMiniDslam3gPerfDailyIntEgressPackets_Object = MibTableColumn
adGenMiniDslam3gPerfDailyIntEgressPackets = _AdGenMiniDslam3gPerfDailyIntEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 4, 1, 4),
    _AdGenMiniDslam3gPerfDailyIntEgressPackets_Type()
)
adGenMiniDslam3gPerfDailyIntEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyIntEgressPackets.setStatus("current")
_AdGenMiniDslam3gPerfDailyIntEgressBytes_Type = Counter32
_AdGenMiniDslam3gPerfDailyIntEgressBytes_Object = MibTableColumn
adGenMiniDslam3gPerfDailyIntEgressBytes = _AdGenMiniDslam3gPerfDailyIntEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 4, 1, 5),
    _AdGenMiniDslam3gPerfDailyIntEgressBytes_Type()
)
adGenMiniDslam3gPerfDailyIntEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyIntEgressBytes.setStatus("current")
_AdGenMiniDslam3gPerfDailyIntEgressOverflowPackets_Type = Counter32
_AdGenMiniDslam3gPerfDailyIntEgressOverflowPackets_Object = MibTableColumn
adGenMiniDslam3gPerfDailyIntEgressOverflowPackets = _AdGenMiniDslam3gPerfDailyIntEgressOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 4, 1, 6),
    _AdGenMiniDslam3gPerfDailyIntEgressOverflowPackets_Type()
)
adGenMiniDslam3gPerfDailyIntEgressOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyIntEgressOverflowPackets.setStatus("current")
_AdGenMiniDslam3gPerfDailyIntEgressOverflowBytes_Type = Counter32
_AdGenMiniDslam3gPerfDailyIntEgressOverflowBytes_Object = MibTableColumn
adGenMiniDslam3gPerfDailyIntEgressOverflowBytes = _AdGenMiniDslam3gPerfDailyIntEgressOverflowBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 6, 4, 1, 7),
    _AdGenMiniDslam3gPerfDailyIntEgressOverflowBytes_Type()
)
adGenMiniDslam3gPerfDailyIntEgressOverflowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gPerfDailyIntEgressOverflowBytes.setStatus("current")
_AdGenMiniDslam3gVlanVcMapProfileTable_Object = MibTable
adGenMiniDslam3gVlanVcMapProfileTable = _AdGenMiniDslam3gVlanVcMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gVlanVcMapProfileTable.setStatus("current")
_AdGenMiniDslam3gVlanVcMapProfileEntry_Object = MibTableRow
adGenMiniDslam3gVlanVcMapProfileEntry = _AdGenMiniDslam3gVlanVcMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 7, 1)
)
adGenMiniDslam3gVlanVcMapProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gVlanVcVpi"),
    (0, "ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gVlanVcVci"),
    (0, "ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gVlanVcVid"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gVlanVcMapProfileEntry.setStatus("current")
_AdGenMiniDslam3gVlanVcVpi_Type = Unsigned32
_AdGenMiniDslam3gVlanVcVpi_Object = MibTableColumn
adGenMiniDslam3gVlanVcVpi = _AdGenMiniDslam3gVlanVcVpi_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 7, 1, 1),
    _AdGenMiniDslam3gVlanVcVpi_Type()
)
adGenMiniDslam3gVlanVcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gVlanVcVpi.setStatus("current")
_AdGenMiniDslam3gVlanVcVci_Type = Unsigned32
_AdGenMiniDslam3gVlanVcVci_Object = MibTableColumn
adGenMiniDslam3gVlanVcVci = _AdGenMiniDslam3gVlanVcVci_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 7, 1, 2),
    _AdGenMiniDslam3gVlanVcVci_Type()
)
adGenMiniDslam3gVlanVcVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gVlanVcVci.setStatus("current")
_AdGenMiniDslam3gVlanVcVid_Type = Unsigned32
_AdGenMiniDslam3gVlanVcVid_Object = MibTableColumn
adGenMiniDslam3gVlanVcVid = _AdGenMiniDslam3gVlanVcVid_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 7, 1, 3),
    _AdGenMiniDslam3gVlanVcVid_Type()
)
adGenMiniDslam3gVlanVcVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gVlanVcVid.setStatus("current")
_AdGenMiniDslam3gSpanPowerTable_Object = MibTable
adGenMiniDslam3gSpanPowerTable = _AdGenMiniDslam3gSpanPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gSpanPowerTable.setStatus("current")
_AdGenMiniDslam3gSpanPowerEntry_Object = MibTableRow
adGenMiniDslam3gSpanPowerEntry = _AdGenMiniDslam3gSpanPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 8, 1)
)
adGenMiniDslam3gSpanPowerEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gSpanPowerChannel"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gSpanPowerEntry.setStatus("current")
_AdGenMiniDslam3gSpanPowerChannel_Type = Unsigned32
_AdGenMiniDslam3gSpanPowerChannel_Object = MibTableColumn
adGenMiniDslam3gSpanPowerChannel = _AdGenMiniDslam3gSpanPowerChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 8, 1, 1),
    _AdGenMiniDslam3gSpanPowerChannel_Type()
)
adGenMiniDslam3gSpanPowerChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gSpanPowerChannel.setStatus("current")


class _AdGenMiniDslam3gSpanPowerAlarmEnable_Type(Integer32):
    """Custom type adGenMiniDslam3gSpanPowerAlarmEnable based on Integer32"""
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


_AdGenMiniDslam3gSpanPowerAlarmEnable_Type.__name__ = "Integer32"
_AdGenMiniDslam3gSpanPowerAlarmEnable_Object = MibTableColumn
adGenMiniDslam3gSpanPowerAlarmEnable = _AdGenMiniDslam3gSpanPowerAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 8, 1, 2),
    _AdGenMiniDslam3gSpanPowerAlarmEnable_Type()
)
adGenMiniDslam3gSpanPowerAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gSpanPowerAlarmEnable.setStatus("current")


class _AdGenMiniDslam3gSpanPowerStatus_Type(Integer32):
    """Custom type adGenMiniDslam3gSpanPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powered", 1),
          ("unPowered", 2))
    )


_AdGenMiniDslam3gSpanPowerStatus_Type.__name__ = "Integer32"
_AdGenMiniDslam3gSpanPowerStatus_Object = MibTableColumn
adGenMiniDslam3gSpanPowerStatus = _AdGenMiniDslam3gSpanPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 8, 1, 3),
    _AdGenMiniDslam3gSpanPowerStatus_Type()
)
adGenMiniDslam3gSpanPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMiniDslam3gSpanPowerStatus.setStatus("current")
_AdGenMiniDslam3gGigeProvTable_Object = MibTable
adGenMiniDslam3gGigeProvTable = _AdGenMiniDslam3gGigeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvTable.setStatus("current")
_AdGenMiniDslam3gGigeProvEntry_Object = MibTableRow
adGenMiniDslam3gGigeProvEntry = _AdGenMiniDslam3gGigeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1)
)
adGenMiniDslam3gGigeProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvEntry.setStatus("current")


class _AdGenMiniDslam3gGigeProvRemapPbit0_Type(Integer32):
    """Custom type adGenMiniDslam3gGigeProvRemapPbit0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMiniDslam3gGigeProvRemapPbit0_Type.__name__ = "Integer32"
_AdGenMiniDslam3gGigeProvRemapPbit0_Object = MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit0 = _AdGenMiniDslam3gGigeProvRemapPbit0_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1, 1),
    _AdGenMiniDslam3gGigeProvRemapPbit0_Type()
)
adGenMiniDslam3gGigeProvRemapPbit0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvRemapPbit0.setStatus("current")


class _AdGenMiniDslam3gGigeProvRemapPbit1_Type(Integer32):
    """Custom type adGenMiniDslam3gGigeProvRemapPbit1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMiniDslam3gGigeProvRemapPbit1_Type.__name__ = "Integer32"
_AdGenMiniDslam3gGigeProvRemapPbit1_Object = MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit1 = _AdGenMiniDslam3gGigeProvRemapPbit1_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1, 2),
    _AdGenMiniDslam3gGigeProvRemapPbit1_Type()
)
adGenMiniDslam3gGigeProvRemapPbit1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvRemapPbit1.setStatus("current")


class _AdGenMiniDslam3gGigeProvRemapPbit2_Type(Integer32):
    """Custom type adGenMiniDslam3gGigeProvRemapPbit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMiniDslam3gGigeProvRemapPbit2_Type.__name__ = "Integer32"
_AdGenMiniDslam3gGigeProvRemapPbit2_Object = MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit2 = _AdGenMiniDslam3gGigeProvRemapPbit2_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1, 3),
    _AdGenMiniDslam3gGigeProvRemapPbit2_Type()
)
adGenMiniDslam3gGigeProvRemapPbit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvRemapPbit2.setStatus("current")


class _AdGenMiniDslam3gGigeProvRemapPbit3_Type(Integer32):
    """Custom type adGenMiniDslam3gGigeProvRemapPbit3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMiniDslam3gGigeProvRemapPbit3_Type.__name__ = "Integer32"
_AdGenMiniDslam3gGigeProvRemapPbit3_Object = MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit3 = _AdGenMiniDslam3gGigeProvRemapPbit3_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1, 4),
    _AdGenMiniDslam3gGigeProvRemapPbit3_Type()
)
adGenMiniDslam3gGigeProvRemapPbit3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvRemapPbit3.setStatus("current")


class _AdGenMiniDslam3gGigeProvRemapPbit4_Type(Integer32):
    """Custom type adGenMiniDslam3gGigeProvRemapPbit4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMiniDslam3gGigeProvRemapPbit4_Type.__name__ = "Integer32"
_AdGenMiniDslam3gGigeProvRemapPbit4_Object = MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit4 = _AdGenMiniDslam3gGigeProvRemapPbit4_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1, 5),
    _AdGenMiniDslam3gGigeProvRemapPbit4_Type()
)
adGenMiniDslam3gGigeProvRemapPbit4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvRemapPbit4.setStatus("current")


class _AdGenMiniDslam3gGigeProvRemapPbit5_Type(Integer32):
    """Custom type adGenMiniDslam3gGigeProvRemapPbit5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMiniDslam3gGigeProvRemapPbit5_Type.__name__ = "Integer32"
_AdGenMiniDslam3gGigeProvRemapPbit5_Object = MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit5 = _AdGenMiniDslam3gGigeProvRemapPbit5_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1, 6),
    _AdGenMiniDslam3gGigeProvRemapPbit5_Type()
)
adGenMiniDslam3gGigeProvRemapPbit5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvRemapPbit5.setStatus("current")


class _AdGenMiniDslam3gGigeProvRemapPbit6_Type(Integer32):
    """Custom type adGenMiniDslam3gGigeProvRemapPbit6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMiniDslam3gGigeProvRemapPbit6_Type.__name__ = "Integer32"
_AdGenMiniDslam3gGigeProvRemapPbit6_Object = MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit6 = _AdGenMiniDslam3gGigeProvRemapPbit6_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1, 7),
    _AdGenMiniDslam3gGigeProvRemapPbit6_Type()
)
adGenMiniDslam3gGigeProvRemapPbit6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvRemapPbit6.setStatus("current")


class _AdGenMiniDslam3gGigeProvRemapPbit7_Type(Integer32):
    """Custom type adGenMiniDslam3gGigeProvRemapPbit7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMiniDslam3gGigeProvRemapPbit7_Type.__name__ = "Integer32"
_AdGenMiniDslam3gGigeProvRemapPbit7_Object = MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit7 = _AdGenMiniDslam3gGigeProvRemapPbit7_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1, 8),
    _AdGenMiniDslam3gGigeProvRemapPbit7_Type()
)
adGenMiniDslam3gGigeProvRemapPbit7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvRemapPbit7.setStatus("current")


class _AdGenMiniDslam3gGigeProvRemapPbitResetAll_Type(Integer32):
    """Custom type adGenMiniDslam3gGigeProvRemapPbitResetAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenMiniDslam3gGigeProvRemapPbitResetAll_Type.__name__ = "Integer32"
_AdGenMiniDslam3gGigeProvRemapPbitResetAll_Object = MibTableColumn
adGenMiniDslam3gGigeProvRemapPbitResetAll = _AdGenMiniDslam3gGigeProvRemapPbitResetAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 9, 1, 9),
    _AdGenMiniDslam3gGigeProvRemapPbitResetAll_Type()
)
adGenMiniDslam3gGigeProvRemapPbitResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMiniDslam3gGigeProvRemapPbitResetAll.setStatus("current")

# Managed Objects groups


# Notification objects

adGenMiniDslam3gFanFailureActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 1)
)
adGenMiniDslam3gFanFailureActive.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gInfoFanNumber"))
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gFanFailureActive.setStatus(
        "current"
    )

adGenMiniDslam3gFanFailureInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 2)
)
adGenMiniDslam3gFanFailureInactive.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gInfoFanNumber"))
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gFanFailureInactive.setStatus(
        "current"
    )

adGenMiniDslam3gFanTrayRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 3)
)
adGenMiniDslam3gFanTrayRemoved.setObjects(
    ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gFanTrayRemoved.setStatus(
        "current"
    )

adGenMiniDslam3gFanTrayInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 4)
)
adGenMiniDslam3gFanTrayInserted.setObjects(
    ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gFanTrayInserted.setStatus(
        "current"
    )

adGenMiniDslam3gUserTempActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 5)
)
adGenMiniDslam3gUserTempActive.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gInfoCurrentTemp"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gInfoUserTempThresh"))
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gUserTempActive.setStatus(
        "current"
    )

adGenMiniDslam3gUserTempCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 6)
)
adGenMiniDslam3gUserTempCleared.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gInfoCurrentTemp"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gInfoUserTempThresh"))
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gUserTempCleared.setStatus(
        "current"
    )

adGenMiniDslam3gCriticalHiTempActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 7)
)
adGenMiniDslam3gCriticalHiTempActive.setObjects(
    ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gCriticalHiTempActive.setStatus(
        "current"
    )

adGenMiniDslam3gCriticalHiTempCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 8)
)
adGenMiniDslam3gCriticalHiTempCleared.setObjects(
    ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
)
if mibBuilder.loadTexts:
    adGenMiniDslam3gCriticalHiTempCleared.setStatus(
        "current"
    )

adGenMiniDslamDspWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 9)
)
adGenMiniDslamDspWarmStart.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gInfoDspWarmStartReason"))
)
if mibBuilder.loadTexts:
    adGenMiniDslamDspWarmStart.setStatus(
        "current"
    )

adGenMiniDslamImaLinksOutOfOrderActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 11)
)
adGenMiniDslamImaLinksOutOfOrderActive.setObjects(
    ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
)
if mibBuilder.loadTexts:
    adGenMiniDslamImaLinksOutOfOrderActive.setStatus(
        "current"
    )

adGenMiniDslamImaLinksOutOfOrderCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 12)
)
adGenMiniDslamImaLinksOutOfOrderCleared.setObjects(
    ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
)
if mibBuilder.loadTexts:
    adGenMiniDslamImaLinksOutOfOrderCleared.setStatus(
        "current"
    )

adGenMiniDslamConfigErrorActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 13)
)
adGenMiniDslamConfigErrorActive.setObjects(
    ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
)
if mibBuilder.loadTexts:
    adGenMiniDslamConfigErrorActive.setStatus(
        "current"
    )

adGenMiniDslamConfigErrorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 14)
)
adGenMiniDslamConfigErrorCleared.setObjects(
    ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
)
if mibBuilder.loadTexts:
    adGenMiniDslamConfigErrorCleared.setStatus(
        "current"
    )

adGenMiniDslamCircuitIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 15)
)
adGenMiniDslamCircuitIdChange.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gInfoCircuitIdChanges"))
)
if mibBuilder.loadTexts:
    adGenMiniDslamCircuitIdChange.setStatus(
        "current"
    )

adGenMiniDslamSpanPowerFailureActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 16)
)
adGenMiniDslamSpanPowerFailureActive.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gSpanPowerChannel"))
)
if mibBuilder.loadTexts:
    adGenMiniDslamSpanPowerFailureActive.setStatus(
        "current"
    )

adGenMiniDslamSpanPowerFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5, 1, 1, 2, 0, 17)
)
adGenMiniDslamSpanPowerFailureCleared.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gSpanPowerChannel"))
)
if mibBuilder.loadTexts:
    adGenMiniDslamSpanPowerFailureCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TAMINIDSLAM3G-MIB",
    **{"adGenMiniDslam3g": adGenMiniDslam3g,
       "adGenMiniDslam3gMib": adGenMiniDslam3gMib,
       "adGenMiniDslam3gInfoTable": adGenMiniDslam3gInfoTable,
       "adGenMiniDslam3gInfoEntry": adGenMiniDslam3gInfoEntry,
       "adGenMiniDslam3gInfoUserTempThresh": adGenMiniDslam3gInfoUserTempThresh,
       "adGenMiniDslam3gInfoUserTempTrapEnable": adGenMiniDslam3gInfoUserTempTrapEnable,
       "adGenMiniDslam3gInfoDspWarmStartEnable": adGenMiniDslam3gInfoDspWarmStartEnable,
       "adGenMiniDslam3gInfoCurrentTemp": adGenMiniDslam3gInfoCurrentTemp,
       "adGenMiniDslam3gInfoFanNumber": adGenMiniDslam3gInfoFanNumber,
       "adGenMiniDslam3gInfoDspWarmStartReason": adGenMiniDslam3gInfoDspWarmStartReason,
       "adGenMiniDslam3gInfoDownstreamRateLimitPriority": adGenMiniDslam3gInfoDownstreamRateLimitPriority,
       "adGenMiniDslam3gInfoCircuitIdChanges": adGenMiniDslam3gInfoCircuitIdChanges,
       "adGenMiniDslam3gInfoMCastSessionControlStartIP": adGenMiniDslam3gInfoMCastSessionControlStartIP,
       "adGenMiniDslam3gInfoMCastSessionControlEndIP": adGenMiniDslam3gInfoMCastSessionControlEndIP,
       "adGenMiniDslam3gInfoMCastSessionControlBitrate": adGenMiniDslam3gInfoMCastSessionControlBitrate,
       "adGenMiniDslam3gInfoMacAgingTime": adGenMiniDslam3gInfoMacAgingTime,
       "adGenMiniDslam3gInfoLegacyDeployment": adGenMiniDslam3gInfoLegacyDeployment,
       "adGenMiniDslam3gInfoBondingMode": adGenMiniDslam3gInfoBondingMode,
       "adGenMiniDslam3gTraps": adGenMiniDslam3gTraps,
       "adGenMiniDslam3gTrapsv1Patch": adGenMiniDslam3gTrapsv1Patch,
       "adGenMiniDslam3gFanFailureActive": adGenMiniDslam3gFanFailureActive,
       "adGenMiniDslam3gFanFailureInactive": adGenMiniDslam3gFanFailureInactive,
       "adGenMiniDslam3gFanTrayRemoved": adGenMiniDslam3gFanTrayRemoved,
       "adGenMiniDslam3gFanTrayInserted": adGenMiniDslam3gFanTrayInserted,
       "adGenMiniDslam3gUserTempActive": adGenMiniDslam3gUserTempActive,
       "adGenMiniDslam3gUserTempCleared": adGenMiniDslam3gUserTempCleared,
       "adGenMiniDslam3gCriticalHiTempActive": adGenMiniDslam3gCriticalHiTempActive,
       "adGenMiniDslam3gCriticalHiTempCleared": adGenMiniDslam3gCriticalHiTempCleared,
       "adGenMiniDslamDspWarmStart": adGenMiniDslamDspWarmStart,
       "adGenMiniDslamImaLinksOutOfOrderActive": adGenMiniDslamImaLinksOutOfOrderActive,
       "adGenMiniDslamImaLinksOutOfOrderCleared": adGenMiniDslamImaLinksOutOfOrderCleared,
       "adGenMiniDslamConfigErrorActive": adGenMiniDslamConfigErrorActive,
       "adGenMiniDslamConfigErrorCleared": adGenMiniDslamConfigErrorCleared,
       "adGenMiniDslamCircuitIdChange": adGenMiniDslamCircuitIdChange,
       "adGenMiniDslamSpanPowerFailureActive": adGenMiniDslamSpanPowerFailureActive,
       "adGenMiniDslamSpanPowerFailureCleared": adGenMiniDslamSpanPowerFailureCleared,
       "adGenMiniDslam3gTestTable": adGenMiniDslam3gTestTable,
       "adGenMiniDslam3gTestEntry": adGenMiniDslam3gTestEntry,
       "adGenMiniDslam3gTestPortNumber": adGenMiniDslam3gTestPortNumber,
       "adGenMiniDslam3gTestFilename": adGenMiniDslam3gTestFilename,
       "adGenMiniDslam3gSELTTestStart": adGenMiniDslam3gSELTTestStart,
       "adGenMiniDslam3gDELTTestStart": adGenMiniDslam3gDELTTestStart,
       "adGenMiniDslam3gTestStop": adGenMiniDslam3gTestStop,
       "adGenMiniDslam3gTestSELTDELTStatus": adGenMiniDslam3gTestSELTDELTStatus,
       "adGenMiniDslam3gAdslProvTable": adGenMiniDslam3gAdslProvTable,
       "adGenMiniDslam3gAdslProvEntry": adGenMiniDslam3gAdslProvEntry,
       "adGenMiniDslam3gAdslProvRetrainUasNe": adGenMiniDslam3gAdslProvRetrainUasNe,
       "adGenMiniDslam3gAdslProvRetrainMarginNe": adGenMiniDslam3gAdslProvRetrainMarginNe,
       "adGenMiniDslam3gAdslProvRetrainSesFe": adGenMiniDslam3gAdslProvRetrainSesFe,
       "adGenMiniDslam3gAdslProvRetrainUasFe": adGenMiniDslam3gAdslProvRetrainUasFe,
       "adGenMiniDslam3gAdslProvRetrainMarginFe": adGenMiniDslam3gAdslProvRetrainMarginFe,
       "adGenMiniDslam3gAdslProvDownstreamRateLimit": adGenMiniDslam3gAdslProvDownstreamRateLimit,
       "adGenMiniDslam3gMacTable": adGenMiniDslam3gMacTable,
       "adGenMiniDslam3gMacEntry": adGenMiniDslam3gMacEntry,
       "adGenMiniDslam3gMacIndex": adGenMiniDslam3gMacIndex,
       "adGenMiniDslam3gMacAddress": adGenMiniDslam3gMacAddress,
       "adGenMiniDslam3gMacVID": adGenMiniDslam3gMacVID,
       "adGenMiniDslam3gMacType": adGenMiniDslam3gMacType,
       "adGenMiniDslam3gMacIP": adGenMiniDslam3gMacIP,
       "adGenMiniDslam3gMacLeaseTime": adGenMiniDslam3gMacLeaseTime,
       "adGenMiniDslam3gMacGatewayMac": adGenMiniDslam3gMacGatewayMac,
       "adGenMiniDslam3gMacGatewayIP": adGenMiniDslam3gMacGatewayIP,
       "adGenMiniDslam3gMacInterfaceState": adGenMiniDslam3gMacInterfaceState,
       "adGenMiniDslam3gMacXid": adGenMiniDslam3gMacXid,
       "adGenMiniDslam3gMacEncapsulationMode": adGenMiniDslam3gMacEncapsulationMode,
       "adGenMiniDslam3gMacStartTime": adGenMiniDslam3gMacStartTime,
       "adGenMiniDslam3gMacVpi": adGenMiniDslam3gMacVpi,
       "adGenMiniDslam3gMacVci": adGenMiniDslam3gMacVci,
       "adGenMiniDslam3gMacCTag": adGenMiniDslam3gMacCTag,
       "adGenMiniDslam3gMacCEVlan": adGenMiniDslam3gMacCEVlan,
       "adGenMiniDslam3gMacIpAddressType": adGenMiniDslam3gMacIpAddressType,
       "adGenMiniDslam3gMacIpAddress": adGenMiniDslam3gMacIpAddress,
       "adGenMiniDslam3gMacIpAddressPrefix": adGenMiniDslam3gMacIpAddressPrefix,
       "adGenMiniDslam3gPerf": adGenMiniDslam3gPerf,
       "adGenMiniDslam3gPerf15MinCurrTable": adGenMiniDslam3gPerf15MinCurrTable,
       "adGenMiniDslam3gPerf15MinCurrEntry": adGenMiniDslam3gPerf15MinCurrEntry,
       "adGenMiniDslam3gPerf15MinCurrIngressPackets": adGenMiniDslam3gPerf15MinCurrIngressPackets,
       "adGenMiniDslam3gPerf15MinCurrIngressBytes": adGenMiniDslam3gPerf15MinCurrIngressBytes,
       "adGenMiniDslam3gPerf15MinCurrEgressPackets": adGenMiniDslam3gPerf15MinCurrEgressPackets,
       "adGenMiniDslam3gPerf15MinCurrEgressBytes": adGenMiniDslam3gPerf15MinCurrEgressBytes,
       "adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets": adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets,
       "adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes": adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes,
       "adGenMiniDslam3gPerf15MinCurrValidIntervals": adGenMiniDslam3gPerf15MinCurrValidIntervals,
       "adGenMiniDslam3gPerf15MinIntTable": adGenMiniDslam3gPerf15MinIntTable,
       "adGenMiniDslam3gPerf15MinIntEntry": adGenMiniDslam3gPerf15MinIntEntry,
       "adGenMiniDslam3gPerf15MinIntInterval": adGenMiniDslam3gPerf15MinIntInterval,
       "adGenMiniDslam3gPerf15MinIntIngressPackets": adGenMiniDslam3gPerf15MinIntIngressPackets,
       "adGenMiniDslam3gPerf15MinIntIngressBytes": adGenMiniDslam3gPerf15MinIntIngressBytes,
       "adGenMiniDslam3gPerf15MinIntEgressPackets": adGenMiniDslam3gPerf15MinIntEgressPackets,
       "adGenMiniDslam3gPerf15MinIntEgressBytes": adGenMiniDslam3gPerf15MinIntEgressBytes,
       "adGenMiniDslam3gPerf15MinIntEgressOverflowPackets": adGenMiniDslam3gPerf15MinIntEgressOverflowPackets,
       "adGenMiniDslam3gPerf15MinIntEgressOverflowBytes": adGenMiniDslam3gPerf15MinIntEgressOverflowBytes,
       "adGenMiniDslam3gPerfDailyCurrTable": adGenMiniDslam3gPerfDailyCurrTable,
       "adGenMiniDslam3gPerfDailyCurrEntry": adGenMiniDslam3gPerfDailyCurrEntry,
       "adGenMiniDslam3gPerfDailyCurrIngressPackets": adGenMiniDslam3gPerfDailyCurrIngressPackets,
       "adGenMiniDslam3gPerfDailyCurrIngressBytes": adGenMiniDslam3gPerfDailyCurrIngressBytes,
       "adGenMiniDslam3gPerfDailyCurrEgressPackets": adGenMiniDslam3gPerfDailyCurrEgressPackets,
       "adGenMiniDslam3gPerfDailyCurrEgressBytes": adGenMiniDslam3gPerfDailyCurrEgressBytes,
       "adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets": adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets,
       "adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes": adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes,
       "adGenMiniDslam3gPerfDailyCurrValidIntervals": adGenMiniDslam3gPerfDailyCurrValidIntervals,
       "adGenMiniDslam3gPerfDailyIntTable": adGenMiniDslam3gPerfDailyIntTable,
       "adGenMiniDslam3gPerfDailyIntEntry": adGenMiniDslam3gPerfDailyIntEntry,
       "adGenMiniDslam3gPerfDailyIntInterval": adGenMiniDslam3gPerfDailyIntInterval,
       "adGenMiniDslam3gPerfDailyIntIngressPackets": adGenMiniDslam3gPerfDailyIntIngressPackets,
       "adGenMiniDslam3gPerfDailyIntIngressBytes": adGenMiniDslam3gPerfDailyIntIngressBytes,
       "adGenMiniDslam3gPerfDailyIntEgressPackets": adGenMiniDslam3gPerfDailyIntEgressPackets,
       "adGenMiniDslam3gPerfDailyIntEgressBytes": adGenMiniDslam3gPerfDailyIntEgressBytes,
       "adGenMiniDslam3gPerfDailyIntEgressOverflowPackets": adGenMiniDslam3gPerfDailyIntEgressOverflowPackets,
       "adGenMiniDslam3gPerfDailyIntEgressOverflowBytes": adGenMiniDslam3gPerfDailyIntEgressOverflowBytes,
       "adGenMiniDslam3gVlanVcMapProfileTable": adGenMiniDslam3gVlanVcMapProfileTable,
       "adGenMiniDslam3gVlanVcMapProfileEntry": adGenMiniDslam3gVlanVcMapProfileEntry,
       "adGenMiniDslam3gVlanVcVpi": adGenMiniDslam3gVlanVcVpi,
       "adGenMiniDslam3gVlanVcVci": adGenMiniDslam3gVlanVcVci,
       "adGenMiniDslam3gVlanVcVid": adGenMiniDslam3gVlanVcVid,
       "adGenMiniDslam3gSpanPowerTable": adGenMiniDslam3gSpanPowerTable,
       "adGenMiniDslam3gSpanPowerEntry": adGenMiniDslam3gSpanPowerEntry,
       "adGenMiniDslam3gSpanPowerChannel": adGenMiniDslam3gSpanPowerChannel,
       "adGenMiniDslam3gSpanPowerAlarmEnable": adGenMiniDslam3gSpanPowerAlarmEnable,
       "adGenMiniDslam3gSpanPowerStatus": adGenMiniDslam3gSpanPowerStatus,
       "adGenMiniDslam3gGigeProvTable": adGenMiniDslam3gGigeProvTable,
       "adGenMiniDslam3gGigeProvEntry": adGenMiniDslam3gGigeProvEntry,
       "adGenMiniDslam3gGigeProvRemapPbit0": adGenMiniDslam3gGigeProvRemapPbit0,
       "adGenMiniDslam3gGigeProvRemapPbit1": adGenMiniDslam3gGigeProvRemapPbit1,
       "adGenMiniDslam3gGigeProvRemapPbit2": adGenMiniDslam3gGigeProvRemapPbit2,
       "adGenMiniDslam3gGigeProvRemapPbit3": adGenMiniDslam3gGigeProvRemapPbit3,
       "adGenMiniDslam3gGigeProvRemapPbit4": adGenMiniDslam3gGigeProvRemapPbit4,
       "adGenMiniDslam3gGigeProvRemapPbit5": adGenMiniDslam3gGigeProvRemapPbit5,
       "adGenMiniDslam3gGigeProvRemapPbit6": adGenMiniDslam3gGigeProvRemapPbit6,
       "adGenMiniDslam3gGigeProvRemapPbit7": adGenMiniDslam3gGigeProvRemapPbit7,
       "adGenMiniDslam3gGigeProvRemapPbitResetAll": adGenMiniDslam3gGigeProvRemapPbitResetAll}
)
