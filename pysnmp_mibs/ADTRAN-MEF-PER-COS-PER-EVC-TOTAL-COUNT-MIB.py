# SNMP MIB module (ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:40 2025
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

(adGenAOSConformance,
 adGenAOSMef) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSMef")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfInvalidIntervals,
 HCPerfTimeElapsed,
 HCPerfTotalCount,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfInvalidIntervals",
    "HCPerfTimeElapsed",
    "HCPerfTotalCount",
    "HCPerfValidIntervals")

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

adGenAosMefPerCosPerEvcTotalCountMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 8)
)
if mibBuilder.loadTexts:
    adGenAosMefPerCosPerEvcTotalCountMib.setRevisions(
        ("2017-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosMefPerCosPerEvcTotalCount_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerEvcTotalCount = _AdGenAosMefPerCosPerEvcTotalCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8)
)
_AdMefPerCosPerEvcTcTable_Object = MibTable
adMefPerCosPerEvcTcTable = _AdMefPerCosPerEvcTcTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8, 1)
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTcTable.setStatus("current")
_AdMefPerCosPerEvcTcEntry_Object = MibTableRow
adMefPerCosPerEvcTcEntry = _AdMefPerCosPerEvcTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8, 1, 1)
)
adMefPerCosPerEvcTcEntry.setIndexNames(
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB", "adMefPerCosPerEvcTcEvcNameFixedLen"),
    (0, "ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB", "adMefPerCosPerEvcTcQueueNumber"),
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTcEntry.setStatus("current")


class _AdMefPerCosPerEvcTcEvcNameFixedLen_Type(OctetString):
    """Custom type adMefPerCosPerEvcTcEvcNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_AdMefPerCosPerEvcTcEvcNameFixedLen_Type.__name__ = "OctetString"
_AdMefPerCosPerEvcTcEvcNameFixedLen_Object = MibTableColumn
adMefPerCosPerEvcTcEvcNameFixedLen = _AdMefPerCosPerEvcTcEvcNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8, 1, 1, 1),
    _AdMefPerCosPerEvcTcEvcNameFixedLen_Type()
)
adMefPerCosPerEvcTcEvcNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTcEvcNameFixedLen.setStatus("current")


class _AdMefPerCosPerEvcTcQueueNumber_Type(Unsigned32):
    """Custom type adMefPerCosPerEvcTcQueueNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdMefPerCosPerEvcTcQueueNumber_Type.__name__ = "Unsigned32"
_AdMefPerCosPerEvcTcQueueNumber_Object = MibTableColumn
adMefPerCosPerEvcTcQueueNumber = _AdMefPerCosPerEvcTcQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8, 1, 1, 2),
    _AdMefPerCosPerEvcTcQueueNumber_Type()
)
adMefPerCosPerEvcTcQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTcQueueNumber.setStatus("current")
_AdMefPerCosPerEvcTotalIngressGreenOctets_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressGreenOctets_Object = MibTableColumn
adMefPerCosPerEvcTotalIngressGreenOctets = _AdMefPerCosPerEvcTotalIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8, 1, 1, 3),
    _AdMefPerCosPerEvcTotalIngressGreenOctets_Type()
)
adMefPerCosPerEvcTotalIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTotalIngressGreenOctets.setStatus("current")
_AdMefPerCosPerEvcTotalIngressGreenFrames_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressGreenFrames_Object = MibTableColumn
adMefPerCosPerEvcTotalIngressGreenFrames = _AdMefPerCosPerEvcTotalIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8, 1, 1, 4),
    _AdMefPerCosPerEvcTotalIngressGreenFrames_Type()
)
adMefPerCosPerEvcTotalIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTotalIngressGreenFrames.setStatus("current")
_AdMefPerCosPerEvcTotalIngressYellowOctets_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressYellowOctets_Object = MibTableColumn
adMefPerCosPerEvcTotalIngressYellowOctets = _AdMefPerCosPerEvcTotalIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8, 1, 1, 5),
    _AdMefPerCosPerEvcTotalIngressYellowOctets_Type()
)
adMefPerCosPerEvcTotalIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTotalIngressYellowOctets.setStatus("current")
_AdMefPerCosPerEvcTotalIngressYellowFrames_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressYellowFrames_Object = MibTableColumn
adMefPerCosPerEvcTotalIngressYellowFrames = _AdMefPerCosPerEvcTotalIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8, 1, 1, 6),
    _AdMefPerCosPerEvcTotalIngressYellowFrames_Type()
)
adMefPerCosPerEvcTotalIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTotalIngressYellowFrames.setStatus("current")
_AdMefPerCosPerEvcTotalIngressRedFrames_Type = HCPerfCurrentCount
_AdMefPerCosPerEvcTotalIngressRedFrames_Object = MibTableColumn
adMefPerCosPerEvcTotalIngressRedFrames = _AdMefPerCosPerEvcTotalIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8, 1, 1, 7),
    _AdMefPerCosPerEvcTotalIngressRedFrames_Type()
)
adMefPerCosPerEvcTotalIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTotalIngressRedFrames.setStatus("current")
_AdGenAosMefPerCosPerEvcTotalCountConformance_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerEvcTotalCountConformance = _AdGenAosMefPerCosPerEvcTotalCountConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 30)
)
_AdMefPerCosPerEvcTotalCountGroups_ObjectIdentity = ObjectIdentity
adMefPerCosPerEvcTotalCountGroups = _AdMefPerCosPerEvcTotalCountGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 30, 1)
)
_AdGenAosMefPerCosPerEvcTotalCountCompliances_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerEvcTotalCountCompliances = _AdGenAosMefPerCosPerEvcTotalCountCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 30, 2)
)

# Managed Objects groups

adMefPerCosPerEvcTotalCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 30, 1, 1)
)
adMefPerCosPerEvcTotalCountGroup.setObjects(
      *(("ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB", "adMefPerCosPerEvcTotalIngressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB", "adMefPerCosPerEvcTotalIngressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB", "adMefPerCosPerEvcTotalIngressYellowOctets"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB", "adMefPerCosPerEvcTotalIngressYellowFrames"),
        ("ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB", "adMefPerCosPerEvcTotalIngressRedFrames"))
)
if mibBuilder.loadTexts:
    adMefPerCosPerEvcTotalCountGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosMefPerUniTotalCountCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 30, 2, 1)
)
adGenAosMefPerUniTotalCountCompliance.setObjects(
    ("ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB", "adMefPerCosPerEvcTotalCountGroup")
)
if mibBuilder.loadTexts:
    adGenAosMefPerUniTotalCountCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-MEF-PER-COS-PER-EVC-TOTAL-COUNT-MIB",
    **{"adGenAosMefPerCosPerEvcTotalCount": adGenAosMefPerCosPerEvcTotalCount,
       "adMefPerCosPerEvcTcTable": adMefPerCosPerEvcTcTable,
       "adMefPerCosPerEvcTcEntry": adMefPerCosPerEvcTcEntry,
       "adMefPerCosPerEvcTcEvcNameFixedLen": adMefPerCosPerEvcTcEvcNameFixedLen,
       "adMefPerCosPerEvcTcQueueNumber": adMefPerCosPerEvcTcQueueNumber,
       "adMefPerCosPerEvcTotalIngressGreenOctets": adMefPerCosPerEvcTotalIngressGreenOctets,
       "adMefPerCosPerEvcTotalIngressGreenFrames": adMefPerCosPerEvcTotalIngressGreenFrames,
       "adMefPerCosPerEvcTotalIngressYellowOctets": adMefPerCosPerEvcTotalIngressYellowOctets,
       "adMefPerCosPerEvcTotalIngressYellowFrames": adMefPerCosPerEvcTotalIngressYellowFrames,
       "adMefPerCosPerEvcTotalIngressRedFrames": adMefPerCosPerEvcTotalIngressRedFrames,
       "adGenAosMefPerCosPerEvcTotalCountConformance": adGenAosMefPerCosPerEvcTotalCountConformance,
       "adMefPerCosPerEvcTotalCountGroups": adMefPerCosPerEvcTotalCountGroups,
       "adMefPerCosPerEvcTotalCountGroup": adMefPerCosPerEvcTotalCountGroup,
       "adGenAosMefPerCosPerEvcTotalCountCompliances": adGenAosMefPerCosPerEvcTotalCountCompliances,
       "adGenAosMefPerUniTotalCountCompliance": adGenAosMefPerUniTotalCountCompliance,
       "adGenAosMefPerCosPerEvcTotalCountMib": adGenAosMefPerCosPerEvcTotalCountMib}
)
