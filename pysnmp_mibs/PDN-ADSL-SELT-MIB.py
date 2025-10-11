# SNMP MIB module (PDN-ADSL-SELT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-ADSL-SELT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:59:58 2025
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

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

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

pdnAdslSeltMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31)
)
if mibBuilder.loadTexts:
    pdnAdslSeltMIB.setRevisions(
        ("2005-03-28 00:00",
         "2005-03-10 00:00",
         "2004-12-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PdnSeltTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopCharacterization", 1),
          ("loopNoiseFloor", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PdnAdslSeltNotifications_ObjectIdentity = ObjectIdentity
pdnAdslSeltNotifications = _PdnAdslSeltNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 0)
)
_PdnAdslSeltObjects_ObjectIdentity = ObjectIdentity
pdnAdslSeltObjects = _PdnAdslSeltObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1)
)


class _PdnAdslSeltWireSize_Type(Integer32):
    """Custom type pdnAdslSeltWireSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("awg", 1),
          ("metric", 2),
          ("metricJapan", 3))
    )


_PdnAdslSeltWireSize_Type.__name__ = "Integer32"
_PdnAdslSeltWireSize_Object = MibScalar
pdnAdslSeltWireSize = _PdnAdslSeltWireSize_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 1),
    _PdnAdslSeltWireSize_Type()
)
pdnAdslSeltWireSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslSeltWireSize.setStatus("current")
_PdnAdslSeltTable_Object = MibTable
pdnAdslSeltTable = _PdnAdslSeltTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2)
)
if mibBuilder.loadTexts:
    pdnAdslSeltTable.setStatus("current")
_PdnAdslSeltEntry_Object = MibTableRow
pdnAdslSeltEntry = _PdnAdslSeltEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1)
)
pdnAdslSeltEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-ADSL-SELT-MIB", "pdnAdslSeltType"),
)
if mibBuilder.loadTexts:
    pdnAdslSeltEntry.setStatus("current")
_PdnAdslSeltType_Type = PdnSeltTypes
_PdnAdslSeltType_Object = MibTableColumn
pdnAdslSeltType = _PdnAdslSeltType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 1),
    _PdnAdslSeltType_Type()
)
pdnAdslSeltType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslSeltType.setStatus("current")


class _PdnAdslSeltCmd_Type(Integer32):
    """Custom type pdnAdslSeltCmd based on Integer32"""
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
        *(("noOp", 1),
          ("start", 2),
          ("stop", 3),
          ("clearResults", 4))
    )


_PdnAdslSeltCmd_Type.__name__ = "Integer32"
_PdnAdslSeltCmd_Object = MibTableColumn
pdnAdslSeltCmd = _PdnAdslSeltCmd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 2),
    _PdnAdslSeltCmd_Type()
)
pdnAdslSeltCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslSeltCmd.setStatus("current")


class _PdnAdslSeltStatus_Type(Integer32):
    """Custom type pdnAdslSeltStatus based on Integer32"""
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
        *(("inProgress", 1),
          ("stoppedInProgress", 2),
          ("complete", 3),
          ("notStarted", 4),
          ("resultsCleared", 5))
    )


_PdnAdslSeltStatus_Type.__name__ = "Integer32"
_PdnAdslSeltStatus_Object = MibTableColumn
pdnAdslSeltStatus = _PdnAdslSeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 3),
    _PdnAdslSeltStatus_Type()
)
pdnAdslSeltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslSeltStatus.setStatus("current")
_PdnAdslSeltDuration_Type = Unsigned32
_PdnAdslSeltDuration_Object = MibTableColumn
pdnAdslSeltDuration = _PdnAdslSeltDuration_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 4),
    _PdnAdslSeltDuration_Type()
)
pdnAdslSeltDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnAdslSeltDuration.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslSeltDuration.setUnits("seconds")
_PdnAdslSeltTimeLeft_Type = Unsigned32
_PdnAdslSeltTimeLeft_Object = MibTableColumn
pdnAdslSeltTimeLeft = _PdnAdslSeltTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 2, 1, 5),
    _PdnAdslSeltTimeLeft_Type()
)
pdnAdslSeltTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslSeltTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    pdnAdslSeltTimeLeft.setUnits("seconds")
_PdnAdslSeltLcTable_Object = MibTable
pdnAdslSeltLcTable = _PdnAdslSeltLcTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3)
)
if mibBuilder.loadTexts:
    pdnAdslSeltLcTable.setStatus("current")
_PdnAdslSeltLcEntry_Object = MibTableRow
pdnAdslSeltLcEntry = _PdnAdslSeltLcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1)
)
pdnAdslSeltLcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-ADSL-SELT-MIB", "pdnAdslSeltLcSegmentIndex"),
)
if mibBuilder.loadTexts:
    pdnAdslSeltLcEntry.setStatus("current")


class _PdnAdslSeltLcSegmentIndex_Type(Integer32):
    """Custom type pdnAdslSeltLcSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_PdnAdslSeltLcSegmentIndex_Type.__name__ = "Integer32"
_PdnAdslSeltLcSegmentIndex_Object = MibTableColumn
pdnAdslSeltLcSegmentIndex = _PdnAdslSeltLcSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1, 1),
    _PdnAdslSeltLcSegmentIndex_Type()
)
pdnAdslSeltLcSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslSeltLcSegmentIndex.setStatus("current")


class _PdnAdslSeltLcSegmentLength_Type(Integer32):
    """Custom type pdnAdslSeltLcSegmentLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_PdnAdslSeltLcSegmentLength_Type.__name__ = "Integer32"
_PdnAdslSeltLcSegmentLength_Object = MibTableColumn
pdnAdslSeltLcSegmentLength = _PdnAdslSeltLcSegmentLength_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1, 2),
    _PdnAdslSeltLcSegmentLength_Type()
)
pdnAdslSeltLcSegmentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslSeltLcSegmentLength.setStatus("current")


class _PdnAdslSeltLcSegmentGauge_Type(Integer32):
    """Custom type pdnAdslSeltLcSegmentGauge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10,
              11,
              12,
              13,
              14,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("awg26", 2),
          ("awg24", 3),
          ("awg22", 4),
          ("awg19", 5),
          ("metric32", 10),
          ("metric40", 11),
          ("metric50", 12),
          ("metric63", 13),
          ("metric90", 14),
          ("metricJapan32", 20),
          ("metricJapan40", 21),
          ("metricJapan50", 22),
          ("metricJapan65", 23),
          ("metricJapan90", 24))
    )


_PdnAdslSeltLcSegmentGauge_Type.__name__ = "Integer32"
_PdnAdslSeltLcSegmentGauge_Object = MibTableColumn
pdnAdslSeltLcSegmentGauge = _PdnAdslSeltLcSegmentGauge_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1, 3),
    _PdnAdslSeltLcSegmentGauge_Type()
)
pdnAdslSeltLcSegmentGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslSeltLcSegmentGauge.setStatus("current")


class _PdnAdslSeltLcSegmentType_Type(Integer32):
    """Custom type pdnAdslSeltLcSegmentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("inline", 2),
          ("bridgeTap", 3))
    )


_PdnAdslSeltLcSegmentType_Type.__name__ = "Integer32"
_PdnAdslSeltLcSegmentType_Object = MibTableColumn
pdnAdslSeltLcSegmentType = _PdnAdslSeltLcSegmentType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 3, 1, 4),
    _PdnAdslSeltLcSegmentType_Type()
)
pdnAdslSeltLcSegmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslSeltLcSegmentType.setStatus("current")
_PdnAdslSeltLnfTable_Object = MibTable
pdnAdslSeltLnfTable = _PdnAdslSeltLnfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4)
)
if mibBuilder.loadTexts:
    pdnAdslSeltLnfTable.setStatus("current")
_PdnAdslSeltLnfEntry_Object = MibTableRow
pdnAdslSeltLnfEntry = _PdnAdslSeltLnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1)
)
pdnAdslSeltLnfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfSubCarrierIndex"),
)
if mibBuilder.loadTexts:
    pdnAdslSeltLnfEntry.setStatus("current")


class _PdnAdslSeltLnfSubCarrierIndex_Type(Integer32):
    """Custom type pdnAdslSeltLnfSubCarrierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PdnAdslSeltLnfSubCarrierIndex_Type.__name__ = "Integer32"
_PdnAdslSeltLnfSubCarrierIndex_Object = MibTableColumn
pdnAdslSeltLnfSubCarrierIndex = _PdnAdslSeltLnfSubCarrierIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1, 1),
    _PdnAdslSeltLnfSubCarrierIndex_Type()
)
pdnAdslSeltLnfSubCarrierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnAdslSeltLnfSubCarrierIndex.setStatus("current")


class _PdnAdslSeltLnfPeakPsd_Type(Integer32):
    """Custom type pdnAdslSeltLnfPeakPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_PdnAdslSeltLnfPeakPsd_Type.__name__ = "Integer32"
_PdnAdslSeltLnfPeakPsd_Object = MibTableColumn
pdnAdslSeltLnfPeakPsd = _PdnAdslSeltLnfPeakPsd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1, 2),
    _PdnAdslSeltLnfPeakPsd_Type()
)
pdnAdslSeltLnfPeakPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslSeltLnfPeakPsd.setStatus("current")


class _PdnAdslSeltLnfTotalPsd_Type(Integer32):
    """Custom type pdnAdslSeltLnfTotalPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_PdnAdslSeltLnfTotalPsd_Type.__name__ = "Integer32"
_PdnAdslSeltLnfTotalPsd_Object = MibTableColumn
pdnAdslSeltLnfTotalPsd = _PdnAdslSeltLnfTotalPsd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1, 3),
    _PdnAdslSeltLnfTotalPsd_Type()
)
pdnAdslSeltLnfTotalPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslSeltLnfTotalPsd.setStatus("current")


class _PdnAdslSeltLnfSignalPsd_Type(Integer32):
    """Custom type pdnAdslSeltLnfSignalPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_PdnAdslSeltLnfSignalPsd_Type.__name__ = "Integer32"
_PdnAdslSeltLnfSignalPsd_Object = MibTableColumn
pdnAdslSeltLnfSignalPsd = _PdnAdslSeltLnfSignalPsd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 1, 4, 1, 4),
    _PdnAdslSeltLnfSignalPsd_Type()
)
pdnAdslSeltLnfSignalPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnAdslSeltLnfSignalPsd.setStatus("current")
_PdnAdslSeltAFNs_ObjectIdentity = ObjectIdentity
pdnAdslSeltAFNs = _PdnAdslSeltAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 2)
)
_PdnAdslSeltConformance_ObjectIdentity = ObjectIdentity
pdnAdslSeltConformance = _PdnAdslSeltConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3)
)
_PdnAdslSeltCompliances_ObjectIdentity = ObjectIdentity
pdnAdslSeltCompliances = _PdnAdslSeltCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 1)
)
_PdnAdslSeltGroups_ObjectIdentity = ObjectIdentity
pdnAdslSeltGroups = _PdnAdslSeltGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2)
)
_PdnAdslSeltObjGroups_ObjectIdentity = ObjectIdentity
pdnAdslSeltObjGroups = _PdnAdslSeltObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 1)
)
_PdnAdslSeltAfnGroups_ObjectIdentity = ObjectIdentity
pdnAdslSeltAfnGroups = _PdnAdslSeltAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 2)
)
_PdnAdslSeltNtfyGroups_ObjectIdentity = ObjectIdentity
pdnAdslSeltNtfyGroups = _PdnAdslSeltNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 3)
)

# Managed Objects groups

pdnAdslSeltGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 1, 1)
)
pdnAdslSeltGroup.setObjects(
      *(("PDN-ADSL-SELT-MIB", "pdnAdslSeltCmd"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltStatus"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltWireSize"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltDuration"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltTimeLeft"))
)
if mibBuilder.loadTexts:
    pdnAdslSeltGroup.setStatus("current")

pdnAdslSeltLcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 1, 2)
)
pdnAdslSeltLcGroup.setObjects(
      *(("PDN-ADSL-SELT-MIB", "pdnAdslSeltLcSegmentLength"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLcSegmentGauge"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLcSegmentType"))
)
if mibBuilder.loadTexts:
    pdnAdslSeltLcGroup.setStatus("current")

pdnAdslSeltLnfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 2, 1, 3)
)
pdnAdslSeltLnfGroup.setObjects(
      *(("PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfPeakPsd"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfTotalPsd"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfSignalPsd"))
)
if mibBuilder.loadTexts:
    pdnAdslSeltLnfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnAdslSeltMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 31, 3, 1, 1)
)
pdnAdslSeltMIBCompliance.setObjects(
      *(("PDN-ADSL-SELT-MIB", "pdnAdslSeltGroup"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLcGroup"),
        ("PDN-ADSL-SELT-MIB", "pdnAdslSeltLnfGroup"))
)
if mibBuilder.loadTexts:
    pdnAdslSeltMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ADSL-SELT-MIB",
    **{"PdnSeltTypes": PdnSeltTypes,
       "pdnAdslSeltMIB": pdnAdslSeltMIB,
       "pdnAdslSeltNotifications": pdnAdslSeltNotifications,
       "pdnAdslSeltObjects": pdnAdslSeltObjects,
       "pdnAdslSeltWireSize": pdnAdslSeltWireSize,
       "pdnAdslSeltTable": pdnAdslSeltTable,
       "pdnAdslSeltEntry": pdnAdslSeltEntry,
       "pdnAdslSeltType": pdnAdslSeltType,
       "pdnAdslSeltCmd": pdnAdslSeltCmd,
       "pdnAdslSeltStatus": pdnAdslSeltStatus,
       "pdnAdslSeltDuration": pdnAdslSeltDuration,
       "pdnAdslSeltTimeLeft": pdnAdslSeltTimeLeft,
       "pdnAdslSeltLcTable": pdnAdslSeltLcTable,
       "pdnAdslSeltLcEntry": pdnAdslSeltLcEntry,
       "pdnAdslSeltLcSegmentIndex": pdnAdslSeltLcSegmentIndex,
       "pdnAdslSeltLcSegmentLength": pdnAdslSeltLcSegmentLength,
       "pdnAdslSeltLcSegmentGauge": pdnAdslSeltLcSegmentGauge,
       "pdnAdslSeltLcSegmentType": pdnAdslSeltLcSegmentType,
       "pdnAdslSeltLnfTable": pdnAdslSeltLnfTable,
       "pdnAdslSeltLnfEntry": pdnAdslSeltLnfEntry,
       "pdnAdslSeltLnfSubCarrierIndex": pdnAdslSeltLnfSubCarrierIndex,
       "pdnAdslSeltLnfPeakPsd": pdnAdslSeltLnfPeakPsd,
       "pdnAdslSeltLnfTotalPsd": pdnAdslSeltLnfTotalPsd,
       "pdnAdslSeltLnfSignalPsd": pdnAdslSeltLnfSignalPsd,
       "pdnAdslSeltAFNs": pdnAdslSeltAFNs,
       "pdnAdslSeltConformance": pdnAdslSeltConformance,
       "pdnAdslSeltCompliances": pdnAdslSeltCompliances,
       "pdnAdslSeltMIBCompliance": pdnAdslSeltMIBCompliance,
       "pdnAdslSeltGroups": pdnAdslSeltGroups,
       "pdnAdslSeltObjGroups": pdnAdslSeltObjGroups,
       "pdnAdslSeltGroup": pdnAdslSeltGroup,
       "pdnAdslSeltLcGroup": pdnAdslSeltLcGroup,
       "pdnAdslSeltLnfGroup": pdnAdslSeltLnfGroup,
       "pdnAdslSeltAfnGroups": pdnAdslSeltAfnGroups,
       "pdnAdslSeltNtfyGroups": pdnAdslSeltNtfyGroups}
)
