# SNMP MIB module (ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:14 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

adGenAosMefPerUniTotalCountMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 5)
)
if mibBuilder.loadTexts:
    adGenAosMefPerUniTotalCountMib.setRevisions(
        ("2017-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosMefPerUniTotalCount_ObjectIdentity = ObjectIdentity
adGenAosMefPerUniTotalCount = _AdGenAosMefPerUniTotalCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5)
)
_AdMefPerUniTcTable_Object = MibTable
adMefPerUniTcTable = _AdMefPerUniTcTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1)
)
if mibBuilder.loadTexts:
    adMefPerUniTcTable.setStatus("current")
_AdMefPerUniTcEntry_Object = MibTableRow
adMefPerUniTcEntry = _AdMefPerUniTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1)
)
adMefPerUniTcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adMefPerUniTcEntry.setStatus("current")
_AdMefPerUniTotalIngressGreenOctets_Type = HCPerfCurrentCount
_AdMefPerUniTotalIngressGreenOctets_Object = MibTableColumn
adMefPerUniTotalIngressGreenOctets = _AdMefPerUniTotalIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 1),
    _AdMefPerUniTotalIngressGreenOctets_Type()
)
adMefPerUniTotalIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniTotalIngressGreenOctets.setStatus("current")
_AdMefPerUniTotalIngressGreenFrames_Type = HCPerfCurrentCount
_AdMefPerUniTotalIngressGreenFrames_Object = MibTableColumn
adMefPerUniTotalIngressGreenFrames = _AdMefPerUniTotalIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 2),
    _AdMefPerUniTotalIngressGreenFrames_Type()
)
adMefPerUniTotalIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniTotalIngressGreenFrames.setStatus("current")
_AdMefPerUniTotalIngressYellowOctets_Type = HCPerfCurrentCount
_AdMefPerUniTotalIngressYellowOctets_Object = MibTableColumn
adMefPerUniTotalIngressYellowOctets = _AdMefPerUniTotalIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 3),
    _AdMefPerUniTotalIngressYellowOctets_Type()
)
adMefPerUniTotalIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniTotalIngressYellowOctets.setStatus("current")
_AdMefPerUniTotalIngressYellowFrames_Type = HCPerfCurrentCount
_AdMefPerUniTotalIngressYellowFrames_Object = MibTableColumn
adMefPerUniTotalIngressYellowFrames = _AdMefPerUniTotalIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 4),
    _AdMefPerUniTotalIngressYellowFrames_Type()
)
adMefPerUniTotalIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniTotalIngressYellowFrames.setStatus("current")
_AdMefPerUniTotalIngressRedFrames_Type = HCPerfCurrentCount
_AdMefPerUniTotalIngressRedFrames_Object = MibTableColumn
adMefPerUniTotalIngressRedFrames = _AdMefPerUniTotalIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5, 1, 1, 5),
    _AdMefPerUniTotalIngressRedFrames_Type()
)
adMefPerUniTotalIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerUniTotalIngressRedFrames.setStatus("current")
_AdGenAosMefPerUniTotalCountConformance_ObjectIdentity = ObjectIdentity
adGenAosMefPerUniTotalCountConformance = _AdGenAosMefPerUniTotalCountConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27)
)
_AdMefPerUniTotalCountGroups_ObjectIdentity = ObjectIdentity
adMefPerUniTotalCountGroups = _AdMefPerUniTotalCountGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27, 1)
)
_AdGenAosMefPerUniTotalCountCompliances_ObjectIdentity = ObjectIdentity
adGenAosMefPerUniTotalCountCompliances = _AdGenAosMefPerUniTotalCountCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27, 2)
)

# Managed Objects groups

adMefPerUniTotalCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27, 1, 1)
)
adMefPerUniTotalCountGroup.setObjects(
      *(("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressGreenOctets"),
        ("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressGreenFrames"),
        ("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressYellowOctets"),
        ("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressYellowFrames"),
        ("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalIngressRedFrames"))
)
if mibBuilder.loadTexts:
    adMefPerUniTotalCountGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosMefPerUniTotalCountCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 27, 2, 1)
)
adGenAosMefPerUniTotalCountCompliance.setObjects(
    ("ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB", "adMefPerUniTotalCountGroup")
)
if mibBuilder.loadTexts:
    adGenAosMefPerUniTotalCountCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-MEF-PER-UNI-TOTAL-COUNT-MIB",
    **{"adGenAosMefPerUniTotalCount": adGenAosMefPerUniTotalCount,
       "adMefPerUniTcTable": adMefPerUniTcTable,
       "adMefPerUniTcEntry": adMefPerUniTcEntry,
       "adMefPerUniTotalIngressGreenOctets": adMefPerUniTotalIngressGreenOctets,
       "adMefPerUniTotalIngressGreenFrames": adMefPerUniTotalIngressGreenFrames,
       "adMefPerUniTotalIngressYellowOctets": adMefPerUniTotalIngressYellowOctets,
       "adMefPerUniTotalIngressYellowFrames": adMefPerUniTotalIngressYellowFrames,
       "adMefPerUniTotalIngressRedFrames": adMefPerUniTotalIngressRedFrames,
       "adGenAosMefPerUniTotalCountConformance": adGenAosMefPerUniTotalCountConformance,
       "adMefPerUniTotalCountGroups": adMefPerUniTotalCountGroups,
       "adMefPerUniTotalCountGroup": adMefPerUniTotalCountGroup,
       "adGenAosMefPerUniTotalCountCompliances": adGenAosMefPerUniTotalCountCompliances,
       "adGenAosMefPerUniTotalCountCompliance": adGenAosMefPerUniTotalCountCompliance,
       "adGenAosMefPerUniTotalCountMib": adGenAosMefPerUniTotalCountMib}
)
