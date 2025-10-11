# SNMP MIB module (ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:27 2025
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

adGenAosMefPerEvcTotalCountMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 7)
)
if mibBuilder.loadTexts:
    adGenAosMefPerEvcTotalCountMib.setRevisions(
        ("2017-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosMefPerEvcTotalCount_ObjectIdentity = ObjectIdentity
adGenAosMefPerEvcTotalCount = _AdGenAosMefPerEvcTotalCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7)
)
_AdMefPerEvcTcTable_Object = MibTable
adMefPerEvcTcTable = _AdMefPerEvcTcTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1)
)
if mibBuilder.loadTexts:
    adMefPerEvcTcTable.setStatus("current")
_AdMefPerEvcTcEntry_Object = MibTableRow
adMefPerEvcTcEntry = _AdMefPerEvcTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1)
)
adMefPerEvcTcEntry.setIndexNames(
    (0, "ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTcEvcNameFixedLen"),
)
if mibBuilder.loadTexts:
    adMefPerEvcTcEntry.setStatus("current")


class _AdMefPerEvcTcEvcNameFixedLen_Type(OctetString):
    """Custom type adMefPerEvcTcEvcNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_AdMefPerEvcTcEvcNameFixedLen_Type.__name__ = "OctetString"
_AdMefPerEvcTcEvcNameFixedLen_Object = MibTableColumn
adMefPerEvcTcEvcNameFixedLen = _AdMefPerEvcTcEvcNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 1),
    _AdMefPerEvcTcEvcNameFixedLen_Type()
)
adMefPerEvcTcEvcNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerEvcTcEvcNameFixedLen.setStatus("current")
_AdMefPerEvcTotalIngressGreenOctets_Type = HCPerfCurrentCount
_AdMefPerEvcTotalIngressGreenOctets_Object = MibTableColumn
adMefPerEvcTotalIngressGreenOctets = _AdMefPerEvcTotalIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 2),
    _AdMefPerEvcTotalIngressGreenOctets_Type()
)
adMefPerEvcTotalIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcTotalIngressGreenOctets.setStatus("current")
_AdMefPerEvcTotalIngressGreenFrames_Type = HCPerfCurrentCount
_AdMefPerEvcTotalIngressGreenFrames_Object = MibTableColumn
adMefPerEvcTotalIngressGreenFrames = _AdMefPerEvcTotalIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 3),
    _AdMefPerEvcTotalIngressGreenFrames_Type()
)
adMefPerEvcTotalIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcTotalIngressGreenFrames.setStatus("current")
_AdMefPerEvcTotalIngressYellowOctets_Type = HCPerfCurrentCount
_AdMefPerEvcTotalIngressYellowOctets_Object = MibTableColumn
adMefPerEvcTotalIngressYellowOctets = _AdMefPerEvcTotalIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 4),
    _AdMefPerEvcTotalIngressYellowOctets_Type()
)
adMefPerEvcTotalIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcTotalIngressYellowOctets.setStatus("current")
_AdMefPerEvcTotalIngressYellowFrames_Type = HCPerfCurrentCount
_AdMefPerEvcTotalIngressYellowFrames_Object = MibTableColumn
adMefPerEvcTotalIngressYellowFrames = _AdMefPerEvcTotalIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 5),
    _AdMefPerEvcTotalIngressYellowFrames_Type()
)
adMefPerEvcTotalIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcTotalIngressYellowFrames.setStatus("current")
_AdMefPerEvcTotalIngressRedFrames_Type = HCPerfCurrentCount
_AdMefPerEvcTotalIngressRedFrames_Object = MibTableColumn
adMefPerEvcTotalIngressRedFrames = _AdMefPerEvcTotalIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7, 1, 1, 6),
    _AdMefPerEvcTotalIngressRedFrames_Type()
)
adMefPerEvcTotalIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerEvcTotalIngressRedFrames.setStatus("current")
_AdGenAosMefPerEvcTotalCountConformance_ObjectIdentity = ObjectIdentity
adGenAosMefPerEvcTotalCountConformance = _AdGenAosMefPerEvcTotalCountConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29)
)
_AdMefPerEvcTotalCountGroups_ObjectIdentity = ObjectIdentity
adMefPerEvcTotalCountGroups = _AdMefPerEvcTotalCountGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29, 1)
)
_AdGenAosMefPerEvcTotalCountCompliances_ObjectIdentity = ObjectIdentity
adGenAosMefPerEvcTotalCountCompliances = _AdGenAosMefPerEvcTotalCountCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29, 2)
)

# Managed Objects groups

adMefPerEvcTotalCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29, 1, 1)
)
adMefPerEvcTotalCountGroup.setObjects(
      *(("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressGreenOctets"),
        ("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressGreenFrames"),
        ("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressYellowOctets"),
        ("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressYellowFrames"),
        ("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalIngressRedFrames"))
)
if mibBuilder.loadTexts:
    adMefPerEvcTotalCountGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosMefPerEvcTotalCountCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 29, 2, 1)
)
adGenAosMefPerEvcTotalCountCompliance.setObjects(
    ("ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB", "adMefPerEvcTotalCountGroup")
)
if mibBuilder.loadTexts:
    adGenAosMefPerEvcTotalCountCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-MEF-PER-EVC-TOTAL-COUNT-MIB",
    **{"adGenAosMefPerEvcTotalCount": adGenAosMefPerEvcTotalCount,
       "adMefPerEvcTcTable": adMefPerEvcTcTable,
       "adMefPerEvcTcEntry": adMefPerEvcTcEntry,
       "adMefPerEvcTcEvcNameFixedLen": adMefPerEvcTcEvcNameFixedLen,
       "adMefPerEvcTotalIngressGreenOctets": adMefPerEvcTotalIngressGreenOctets,
       "adMefPerEvcTotalIngressGreenFrames": adMefPerEvcTotalIngressGreenFrames,
       "adMefPerEvcTotalIngressYellowOctets": adMefPerEvcTotalIngressYellowOctets,
       "adMefPerEvcTotalIngressYellowFrames": adMefPerEvcTotalIngressYellowFrames,
       "adMefPerEvcTotalIngressRedFrames": adMefPerEvcTotalIngressRedFrames,
       "adGenAosMefPerEvcTotalCountConformance": adGenAosMefPerEvcTotalCountConformance,
       "adMefPerEvcTotalCountGroups": adMefPerEvcTotalCountGroups,
       "adMefPerEvcTotalCountGroup": adMefPerEvcTotalCountGroup,
       "adGenAosMefPerEvcTotalCountCompliances": adGenAosMefPerEvcTotalCountCompliances,
       "adGenAosMefPerEvcTotalCountCompliance": adGenAosMefPerEvcTotalCountCompliance,
       "adGenAosMefPerEvcTotalCountMib": adGenAosMefPerEvcTotalCountMib}
)
