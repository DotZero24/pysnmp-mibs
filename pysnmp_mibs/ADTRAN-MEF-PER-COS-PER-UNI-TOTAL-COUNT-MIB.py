# SNMP MIB module (ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:05 2025
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

adGenAosMefPerCosPerUniTotalCountMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 9, 6)
)
if mibBuilder.loadTexts:
    adGenAosMefPerCosPerUniTotalCountMib.setRevisions(
        ("2017-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosMefPerCosPerUniTotalCount_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerUniTotalCount = _AdGenAosMefPerCosPerUniTotalCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6)
)
_AdMefPerCosPerUniTcTable_Object = MibTable
adMefPerCosPerUniTcTable = _AdMefPerCosPerUniTcTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1)
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniTcTable.setStatus("current")
_AdMefPerCosPerUniTcEntry_Object = MibTableRow
adMefPerCosPerUniTcEntry = _AdMefPerCosPerUniTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1)
)
adMefPerCosPerUniTcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTcQueueNumber"),
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniTcEntry.setStatus("current")


class _AdMefPerCosPerUniTcQueueNumber_Type(Unsigned32):
    """Custom type adMefPerCosPerUniTcQueueNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdMefPerCosPerUniTcQueueNumber_Type.__name__ = "Unsigned32"
_AdMefPerCosPerUniTcQueueNumber_Object = MibTableColumn
adMefPerCosPerUniTcQueueNumber = _AdMefPerCosPerUniTcQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 1),
    _AdMefPerCosPerUniTcQueueNumber_Type()
)
adMefPerCosPerUniTcQueueNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adMefPerCosPerUniTcQueueNumber.setStatus("current")
_AdMefPerCosPerUniTotalIngressGreenOctets_Type = HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressGreenOctets_Object = MibTableColumn
adMefPerCosPerUniTotalIngressGreenOctets = _AdMefPerCosPerUniTotalIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 2),
    _AdMefPerCosPerUniTotalIngressGreenOctets_Type()
)
adMefPerCosPerUniTotalIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniTotalIngressGreenOctets.setStatus("current")
_AdMefPerCosPerUniTotalIngressGreenFrames_Type = HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressGreenFrames_Object = MibTableColumn
adMefPerCosPerUniTotalIngressGreenFrames = _AdMefPerCosPerUniTotalIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 3),
    _AdMefPerCosPerUniTotalIngressGreenFrames_Type()
)
adMefPerCosPerUniTotalIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniTotalIngressGreenFrames.setStatus("current")
_AdMefPerCosPerUniTotalIngressYellowOctets_Type = HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressYellowOctets_Object = MibTableColumn
adMefPerCosPerUniTotalIngressYellowOctets = _AdMefPerCosPerUniTotalIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 4),
    _AdMefPerCosPerUniTotalIngressYellowOctets_Type()
)
adMefPerCosPerUniTotalIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniTotalIngressYellowOctets.setStatus("current")
_AdMefPerCosPerUniTotalIngressYellowFrames_Type = HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressYellowFrames_Object = MibTableColumn
adMefPerCosPerUniTotalIngressYellowFrames = _AdMefPerCosPerUniTotalIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 5),
    _AdMefPerCosPerUniTotalIngressYellowFrames_Type()
)
adMefPerCosPerUniTotalIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniTotalIngressYellowFrames.setStatus("current")
_AdMefPerCosPerUniTotalIngressRedFrames_Type = HCPerfCurrentCount
_AdMefPerCosPerUniTotalIngressRedFrames_Object = MibTableColumn
adMefPerCosPerUniTotalIngressRedFrames = _AdMefPerCosPerUniTotalIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6, 1, 1, 6),
    _AdMefPerCosPerUniTotalIngressRedFrames_Type()
)
adMefPerCosPerUniTotalIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adMefPerCosPerUniTotalIngressRedFrames.setStatus("current")
_AdGenAosMefPerCosPerUniTotalCountConformance_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerUniTotalCountConformance = _AdGenAosMefPerCosPerUniTotalCountConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28)
)
_AdMefPerCosPerUniTotalCountGroups_ObjectIdentity = ObjectIdentity
adMefPerCosPerUniTotalCountGroups = _AdMefPerCosPerUniTotalCountGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28, 1)
)
_AdGenAosMefPerCosPerUniTotalCountCompliances_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerUniTotalCountCompliances = _AdGenAosMefPerCosPerUniTotalCountCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28, 2)
)

# Managed Objects groups

adMefPerCosPerUniTotalCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28, 1, 1)
)
adMefPerCosPerUniTotalCountGroup.setObjects(
      *(("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressGreenOctets"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressGreenFrames"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressYellowOctets"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressYellowFrames"),
        ("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalIngressRedFrames"))
)
if mibBuilder.loadTexts:
    adMefPerCosPerUniTotalCountGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAosMefPerUniTotalCountCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 28, 2, 1)
)
adGenAosMefPerUniTotalCountCompliance.setObjects(
    ("ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB", "adMefPerCosPerUniTotalCountGroup")
)
if mibBuilder.loadTexts:
    adGenAosMefPerUniTotalCountCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-MEF-PER-COS-PER-UNI-TOTAL-COUNT-MIB",
    **{"adGenAosMefPerCosPerUniTotalCount": adGenAosMefPerCosPerUniTotalCount,
       "adMefPerCosPerUniTcTable": adMefPerCosPerUniTcTable,
       "adMefPerCosPerUniTcEntry": adMefPerCosPerUniTcEntry,
       "adMefPerCosPerUniTcQueueNumber": adMefPerCosPerUniTcQueueNumber,
       "adMefPerCosPerUniTotalIngressGreenOctets": adMefPerCosPerUniTotalIngressGreenOctets,
       "adMefPerCosPerUniTotalIngressGreenFrames": adMefPerCosPerUniTotalIngressGreenFrames,
       "adMefPerCosPerUniTotalIngressYellowOctets": adMefPerCosPerUniTotalIngressYellowOctets,
       "adMefPerCosPerUniTotalIngressYellowFrames": adMefPerCosPerUniTotalIngressYellowFrames,
       "adMefPerCosPerUniTotalIngressRedFrames": adMefPerCosPerUniTotalIngressRedFrames,
       "adGenAosMefPerCosPerUniTotalCountConformance": adGenAosMefPerCosPerUniTotalCountConformance,
       "adMefPerCosPerUniTotalCountGroups": adMefPerCosPerUniTotalCountGroups,
       "adMefPerCosPerUniTotalCountGroup": adMefPerCosPerUniTotalCountGroup,
       "adGenAosMefPerCosPerUniTotalCountCompliances": adGenAosMefPerCosPerUniTotalCountCompliances,
       "adGenAosMefPerUniTotalCountCompliance": adGenAosMefPerUniTotalCountCompliance,
       "adGenAosMefPerCosPerUniTotalCountMib": adGenAosMefPerCosPerUniTotalCountMib}
)
