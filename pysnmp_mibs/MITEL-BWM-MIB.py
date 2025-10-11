# SNMP MIB module (MITEL-BWM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mitel/MITEL-BWM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:32 2025
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

(mitelIpera3000Applications,) = mibBuilder.importSymbols(
    "MITEL-IperaVoiceLAN-MIB",
    "mitelIpera3000Applications")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mitelBandWidthManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mitelBandWidthManagement.setRevisions(
        ("2007-03-26 15:41",
         "2006-08-28 16:26")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MitelBWMPercentage(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class MitelBWMZoneID(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )



class MitelBWMZAPID(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )



# MIB Managed Objects in the order of their OIDs

_MitelBWMObjects_ObjectIdentity = ObjectIdentity
mitelBWMObjects = _MitelBWMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1)
)
_MitelBWMCurrentTable_Object = MibTable
mitelBWMCurrentTable = _MitelBWMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mitelBWMCurrentTable.setStatus("current")
_MitelBWMCurrentTableEntry_Object = MibTableRow
mitelBWMCurrentTableEntry = _MitelBWMCurrentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 1, 1)
)
mitelBWMCurrentTableEntry.setIndexNames(
    (0, "MITEL-BWM-MIB", "mitelBWMCurrentZoneID"),
    (0, "MITEL-BWM-MIB", "mitelBWMCurrentParentZoneID"),
    (0, "MITEL-BWM-MIB", "mitelBWMCurrentZAPID"),
)
if mibBuilder.loadTexts:
    mitelBWMCurrentTableEntry.setStatus("current")
_MitelBWMCurrentZoneID_Type = MitelBWMZoneID
_MitelBWMCurrentZoneID_Object = MibTableColumn
mitelBWMCurrentZoneID = _MitelBWMCurrentZoneID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 1, 1, 1),
    _MitelBWMCurrentZoneID_Type()
)
mitelBWMCurrentZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCurrentZoneID.setStatus("current")
_MitelBWMCurrentParentZoneID_Type = MitelBWMZoneID
_MitelBWMCurrentParentZoneID_Object = MibTableColumn
mitelBWMCurrentParentZoneID = _MitelBWMCurrentParentZoneID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 1, 1, 2),
    _MitelBWMCurrentParentZoneID_Type()
)
mitelBWMCurrentParentZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCurrentParentZoneID.setStatus("current")
_MitelBWMCurrentZAPID_Type = MitelBWMZAPID
_MitelBWMCurrentZAPID_Object = MibTableColumn
mitelBWMCurrentZAPID = _MitelBWMCurrentZAPID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 1, 1, 3),
    _MitelBWMCurrentZAPID_Type()
)
mitelBWMCurrentZAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCurrentZAPID.setStatus("current")
_MitelBWMCurrentZAPLabel_Type = DisplayString
_MitelBWMCurrentZAPLabel_Object = MibTableColumn
mitelBWMCurrentZAPLabel = _MitelBWMCurrentZAPLabel_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 1, 1, 4),
    _MitelBWMCurrentZAPLabel_Type()
)
mitelBWMCurrentZAPLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCurrentZAPLabel.setStatus("current")
_MitelBWMCurrentBandwidthInUse_Type = Gauge32
_MitelBWMCurrentBandwidthInUse_Object = MibTableColumn
mitelBWMCurrentBandwidthInUse = _MitelBWMCurrentBandwidthInUse_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 1, 1, 5),
    _MitelBWMCurrentBandwidthInUse_Type()
)
mitelBWMCurrentBandwidthInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCurrentBandwidthInUse.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWMCurrentBandwidthInUse.setUnits("kilobits per second")
_MitelBWMCurrentBandwidthLimit_Type = Gauge32
_MitelBWMCurrentBandwidthLimit_Object = MibTableColumn
mitelBWMCurrentBandwidthLimit = _MitelBWMCurrentBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 1, 1, 6),
    _MitelBWMCurrentBandwidthLimit_Type()
)
mitelBWMCurrentBandwidthLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCurrentBandwidthLimit.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWMCurrentBandwidthLimit.setUnits("kilobits per second")
_MitelBWMCurrentBandwidthRatio_Type = MitelBWMPercentage
_MitelBWMCurrentBandwidthRatio_Object = MibTableColumn
mitelBWMCurrentBandwidthRatio = _MitelBWMCurrentBandwidthRatio_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 1, 1, 7),
    _MitelBWMCurrentBandwidthRatio_Type()
)
mitelBWMCurrentBandwidthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCurrentBandwidthRatio.setStatus("current")
_MitelBWMCumCACTable_Object = MibTable
mitelBWMCumCACTable = _MitelBWMCumCACTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mitelBWMCumCACTable.setStatus("current")
_MitelBWMCumCACTableEntry_Object = MibTableRow
mitelBWMCumCACTableEntry = _MitelBWMCumCACTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 2, 1)
)
mitelBWMCumCACTableEntry.setIndexNames(
    (0, "MITEL-BWM-MIB", "mitelBWMCumZoneID"),
    (0, "MITEL-BWM-MIB", "mitelBWMCumParentZoneID"),
    (0, "MITEL-BWM-MIB", "mitelBWMCumZAPID"),
)
if mibBuilder.loadTexts:
    mitelBWMCumCACTableEntry.setStatus("current")
_MitelBWMCumZoneID_Type = MitelBWMZoneID
_MitelBWMCumZoneID_Object = MibTableColumn
mitelBWMCumZoneID = _MitelBWMCumZoneID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 2, 1, 1),
    _MitelBWMCumZoneID_Type()
)
mitelBWMCumZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCumZoneID.setStatus("current")
_MitelBWMCumParentZoneID_Type = MitelBWMZoneID
_MitelBWMCumParentZoneID_Object = MibTableColumn
mitelBWMCumParentZoneID = _MitelBWMCumParentZoneID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 2, 1, 2),
    _MitelBWMCumParentZoneID_Type()
)
mitelBWMCumParentZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCumParentZoneID.setStatus("current")
_MitelBWMCumZAPID_Type = MitelBWMZAPID
_MitelBWMCumZAPID_Object = MibTableColumn
mitelBWMCumZAPID = _MitelBWMCumZAPID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 2, 1, 3),
    _MitelBWMCumZAPID_Type()
)
mitelBWMCumZAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCumZAPID.setStatus("current")
_MitelBWMCumZAPLabel_Type = DisplayString
_MitelBWMCumZAPLabel_Object = MibTableColumn
mitelBWMCumZAPLabel = _MitelBWMCumZAPLabel_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 2, 1, 4),
    _MitelBWMCumZAPLabel_Type()
)
mitelBWMCumZAPLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCumZAPLabel.setStatus("current")
_MitelBWMCumCACAdmissions_Type = Counter32
_MitelBWMCumCACAdmissions_Object = MibTableColumn
mitelBWMCumCACAdmissions = _MitelBWMCumCACAdmissions_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 2, 1, 5),
    _MitelBWMCumCACAdmissions_Type()
)
mitelBWMCumCACAdmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCumCACAdmissions.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWMCumCACAdmissions.setUnits("calls")
_MitelBWMCumCACRejections_Type = Counter32
_MitelBWMCumCACRejections_Object = MibTableColumn
mitelBWMCumCACRejections = _MitelBWMCumCACRejections_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 2, 1, 6),
    _MitelBWMCumCACRejections_Type()
)
mitelBWMCumCACRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCumCACRejections.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWMCumCACRejections.setUnits("calls")
_MitelBWMCumCACRejectionRatio_Type = MitelBWMPercentage
_MitelBWMCumCACRejectionRatio_Object = MibTableColumn
mitelBWMCumCACRejectionRatio = _MitelBWMCumCACRejectionRatio_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 2, 1, 7),
    _MitelBWMCumCACRejectionRatio_Type()
)
mitelBWMCumCACRejectionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWMCumCACRejectionRatio.setStatus("current")
_MitelBWM15MinHistoryTable_Object = MibTable
mitelBWM15MinHistoryTable = _MitelBWM15MinHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mitelBWM15MinHistoryTable.setStatus("current")
_MitelBWM15MinHistoryTableEntry_Object = MibTableRow
mitelBWM15MinHistoryTableEntry = _MitelBWM15MinHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1)
)
mitelBWM15MinHistoryTableEntry.setIndexNames(
    (0, "MITEL-BWM-MIB", "mitelBWM15MinZoneID"),
    (0, "MITEL-BWM-MIB", "mitelBWM15MinParentZoneID"),
    (0, "MITEL-BWM-MIB", "mitelBWM15MinZAPID"),
    (0, "MITEL-BWM-MIB", "mitelBWM15MinDateAndTime"),
)
if mibBuilder.loadTexts:
    mitelBWM15MinHistoryTableEntry.setStatus("current")
_MitelBWM15MinZoneID_Type = MitelBWMZoneID
_MitelBWM15MinZoneID_Object = MibTableColumn
mitelBWM15MinZoneID = _MitelBWM15MinZoneID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 1),
    _MitelBWM15MinZoneID_Type()
)
mitelBWM15MinZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinZoneID.setStatus("current")
_MitelBWM15MinParentZoneID_Type = MitelBWMZoneID
_MitelBWM15MinParentZoneID_Object = MibTableColumn
mitelBWM15MinParentZoneID = _MitelBWM15MinParentZoneID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 2),
    _MitelBWM15MinParentZoneID_Type()
)
mitelBWM15MinParentZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinParentZoneID.setStatus("current")
_MitelBWM15MinZAPID_Type = MitelBWMZAPID
_MitelBWM15MinZAPID_Object = MibTableColumn
mitelBWM15MinZAPID = _MitelBWM15MinZAPID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 3),
    _MitelBWM15MinZAPID_Type()
)
mitelBWM15MinZAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinZAPID.setStatus("current")
_MitelBWM15MinDateAndTime_Type = DateAndTime
_MitelBWM15MinDateAndTime_Object = MibTableColumn
mitelBWM15MinDateAndTime = _MitelBWM15MinDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 4),
    _MitelBWM15MinDateAndTime_Type()
)
mitelBWM15MinDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinDateAndTime.setStatus("current")
_MitelBWM15MinZAPLabel_Type = DisplayString
_MitelBWM15MinZAPLabel_Object = MibTableColumn
mitelBWM15MinZAPLabel = _MitelBWM15MinZAPLabel_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 5),
    _MitelBWM15MinZAPLabel_Type()
)
mitelBWM15MinZAPLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinZAPLabel.setStatus("current")
_MitelBWM15MinCACAdmissions_Type = Counter32
_MitelBWM15MinCACAdmissions_Object = MibTableColumn
mitelBWM15MinCACAdmissions = _MitelBWM15MinCACAdmissions_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 6),
    _MitelBWM15MinCACAdmissions_Type()
)
mitelBWM15MinCACAdmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinCACAdmissions.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM15MinCACAdmissions.setUnits("calls")
_MitelBWM15MinCACRejections_Type = Counter32
_MitelBWM15MinCACRejections_Object = MibTableColumn
mitelBWM15MinCACRejections = _MitelBWM15MinCACRejections_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 7),
    _MitelBWM15MinCACRejections_Type()
)
mitelBWM15MinCACRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinCACRejections.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM15MinCACRejections.setUnits("calls")
_MitelBWM15MinCACRejectionRatio_Type = MitelBWMPercentage
_MitelBWM15MinCACRejectionRatio_Object = MibTableColumn
mitelBWM15MinCACRejectionRatio = _MitelBWM15MinCACRejectionRatio_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 8),
    _MitelBWM15MinCACRejectionRatio_Type()
)
mitelBWM15MinCACRejectionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinCACRejectionRatio.setStatus("current")
_MitelBWM15MinAverageBandwidthUsed_Type = Gauge32
_MitelBWM15MinAverageBandwidthUsed_Object = MibTableColumn
mitelBWM15MinAverageBandwidthUsed = _MitelBWM15MinAverageBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 9),
    _MitelBWM15MinAverageBandwidthUsed_Type()
)
mitelBWM15MinAverageBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinAverageBandwidthUsed.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM15MinAverageBandwidthUsed.setUnits("kilobits per second")
_MitelBWM15MinPeakBandwidthUsed_Type = Gauge32
_MitelBWM15MinPeakBandwidthUsed_Object = MibTableColumn
mitelBWM15MinPeakBandwidthUsed = _MitelBWM15MinPeakBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 10),
    _MitelBWM15MinPeakBandwidthUsed_Type()
)
mitelBWM15MinPeakBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinPeakBandwidthUsed.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM15MinPeakBandwidthUsed.setUnits("kilobits per second")
_MitelBWM15MinAverageAvailable_Type = Gauge32
_MitelBWM15MinAverageAvailable_Object = MibTableColumn
mitelBWM15MinAverageAvailable = _MitelBWM15MinAverageAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 11),
    _MitelBWM15MinAverageAvailable_Type()
)
mitelBWM15MinAverageAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinAverageAvailable.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM15MinAverageAvailable.setUnits("kilobits per second")
_MitelBWM15MinFinalBandwidthLimit_Type = Gauge32
_MitelBWM15MinFinalBandwidthLimit_Object = MibTableColumn
mitelBWM15MinFinalBandwidthLimit = _MitelBWM15MinFinalBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 12),
    _MitelBWM15MinFinalBandwidthLimit_Type()
)
mitelBWM15MinFinalBandwidthLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinFinalBandwidthLimit.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM15MinFinalBandwidthLimit.setUnits("kilobits per second")
_MitelBWM15MinPeakBandwidthRatio_Type = MitelBWMPercentage
_MitelBWM15MinPeakBandwidthRatio_Object = MibTableColumn
mitelBWM15MinPeakBandwidthRatio = _MitelBWM15MinPeakBandwidthRatio_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 13),
    _MitelBWM15MinPeakBandwidthRatio_Type()
)
mitelBWM15MinPeakBandwidthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinPeakBandwidthRatio.setStatus("current")
_MitelBWM15MinPeakBwdthAboveLimit_Type = Gauge32
_MitelBWM15MinPeakBwdthAboveLimit_Object = MibTableColumn
mitelBWM15MinPeakBwdthAboveLimit = _MitelBWM15MinPeakBwdthAboveLimit_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 3, 1, 14),
    _MitelBWM15MinPeakBwdthAboveLimit_Type()
)
mitelBWM15MinPeakBwdthAboveLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM15MinPeakBwdthAboveLimit.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM15MinPeakBwdthAboveLimit.setUnits("kilobits per second")
_MitelBWM24HrHistoryTable_Object = MibTable
mitelBWM24HrHistoryTable = _MitelBWM24HrHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mitelBWM24HrHistoryTable.setStatus("current")
_MitelBWM24HrHistoryTableEntry_Object = MibTableRow
mitelBWM24HrHistoryTableEntry = _MitelBWM24HrHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1)
)
mitelBWM24HrHistoryTableEntry.setIndexNames(
    (0, "MITEL-BWM-MIB", "mitelBWM24HrZoneID"),
    (0, "MITEL-BWM-MIB", "mitelBWM24HrParentZoneID"),
    (0, "MITEL-BWM-MIB", "mitelBWM24HrZAPID"),
    (0, "MITEL-BWM-MIB", "mitelBWM24HrDateAndTime"),
)
if mibBuilder.loadTexts:
    mitelBWM24HrHistoryTableEntry.setStatus("current")
_MitelBWM24HrZoneID_Type = MitelBWMZoneID
_MitelBWM24HrZoneID_Object = MibTableColumn
mitelBWM24HrZoneID = _MitelBWM24HrZoneID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 1),
    _MitelBWM24HrZoneID_Type()
)
mitelBWM24HrZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrZoneID.setStatus("current")
_MitelBWM24HrParentZoneID_Type = MitelBWMZoneID
_MitelBWM24HrParentZoneID_Object = MibTableColumn
mitelBWM24HrParentZoneID = _MitelBWM24HrParentZoneID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 2),
    _MitelBWM24HrParentZoneID_Type()
)
mitelBWM24HrParentZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrParentZoneID.setStatus("current")
_MitelBWM24HrZAPID_Type = MitelBWMZAPID
_MitelBWM24HrZAPID_Object = MibTableColumn
mitelBWM24HrZAPID = _MitelBWM24HrZAPID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 3),
    _MitelBWM24HrZAPID_Type()
)
mitelBWM24HrZAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrZAPID.setStatus("current")
_MitelBWM24HrDateAndTime_Type = DateAndTime
_MitelBWM24HrDateAndTime_Object = MibTableColumn
mitelBWM24HrDateAndTime = _MitelBWM24HrDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 4),
    _MitelBWM24HrDateAndTime_Type()
)
mitelBWM24HrDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrDateAndTime.setStatus("current")
_MitelBWM24HrZAPLabel_Type = DisplayString
_MitelBWM24HrZAPLabel_Object = MibTableColumn
mitelBWM24HrZAPLabel = _MitelBWM24HrZAPLabel_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 5),
    _MitelBWM24HrZAPLabel_Type()
)
mitelBWM24HrZAPLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrZAPLabel.setStatus("current")
_MitelBWM24HrCACAdmissions_Type = Counter32
_MitelBWM24HrCACAdmissions_Object = MibTableColumn
mitelBWM24HrCACAdmissions = _MitelBWM24HrCACAdmissions_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 6),
    _MitelBWM24HrCACAdmissions_Type()
)
mitelBWM24HrCACAdmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrCACAdmissions.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM24HrCACAdmissions.setUnits("calls")
_MitelBWM24HrCACRejections_Type = Counter32
_MitelBWM24HrCACRejections_Object = MibTableColumn
mitelBWM24HrCACRejections = _MitelBWM24HrCACRejections_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 7),
    _MitelBWM24HrCACRejections_Type()
)
mitelBWM24HrCACRejections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrCACRejections.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM24HrCACRejections.setUnits("calls")
_MitelBWM24HrCACRejectionRatio_Type = MitelBWMPercentage
_MitelBWM24HrCACRejectionRatio_Object = MibTableColumn
mitelBWM24HrCACRejectionRatio = _MitelBWM24HrCACRejectionRatio_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 8),
    _MitelBWM24HrCACRejectionRatio_Type()
)
mitelBWM24HrCACRejectionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrCACRejectionRatio.setStatus("current")
_MitelBWM24HrAverageBandwidthUsed_Type = Gauge32
_MitelBWM24HrAverageBandwidthUsed_Object = MibTableColumn
mitelBWM24HrAverageBandwidthUsed = _MitelBWM24HrAverageBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 9),
    _MitelBWM24HrAverageBandwidthUsed_Type()
)
mitelBWM24HrAverageBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrAverageBandwidthUsed.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM24HrAverageBandwidthUsed.setUnits("kilobits per second")
_MitelBWM24HrPeakBandwidthUsed_Type = Gauge32
_MitelBWM24HrPeakBandwidthUsed_Object = MibTableColumn
mitelBWM24HrPeakBandwidthUsed = _MitelBWM24HrPeakBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 10),
    _MitelBWM24HrPeakBandwidthUsed_Type()
)
mitelBWM24HrPeakBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrPeakBandwidthUsed.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM24HrPeakBandwidthUsed.setUnits("kilobits per second")
_MitelBWM24HrAverageAvailable_Type = Gauge32
_MitelBWM24HrAverageAvailable_Object = MibTableColumn
mitelBWM24HrAverageAvailable = _MitelBWM24HrAverageAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 11),
    _MitelBWM24HrAverageAvailable_Type()
)
mitelBWM24HrAverageAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrAverageAvailable.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM24HrAverageAvailable.setUnits("kilobits per second")
_MitelBWM24HrFinalBandwidthLimit_Type = Gauge32
_MitelBWM24HrFinalBandwidthLimit_Object = MibTableColumn
mitelBWM24HrFinalBandwidthLimit = _MitelBWM24HrFinalBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 12),
    _MitelBWM24HrFinalBandwidthLimit_Type()
)
mitelBWM24HrFinalBandwidthLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrFinalBandwidthLimit.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM24HrFinalBandwidthLimit.setUnits("kilobits per second")
_MitelBWM24HrPeakBandwidthRatio_Type = MitelBWMPercentage
_MitelBWM24HrPeakBandwidthRatio_Object = MibTableColumn
mitelBWM24HrPeakBandwidthRatio = _MitelBWM24HrPeakBandwidthRatio_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 13),
    _MitelBWM24HrPeakBandwidthRatio_Type()
)
mitelBWM24HrPeakBandwidthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrPeakBandwidthRatio.setStatus("current")
_MitelBWM24HrPeakBwdthAboveLimit_Type = Gauge32
_MitelBWM24HrPeakBwdthAboveLimit_Object = MibTableColumn
mitelBWM24HrPeakBwdthAboveLimit = _MitelBWM24HrPeakBwdthAboveLimit_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 1, 4, 1, 14),
    _MitelBWM24HrPeakBwdthAboveLimit_Type()
)
mitelBWM24HrPeakBwdthAboveLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelBWM24HrPeakBwdthAboveLimit.setStatus("current")
if mibBuilder.loadTexts:
    mitelBWM24HrPeakBwdthAboveLimit.setUnits("kilobits per second")
_MitelBWMConformance_ObjectIdentity = ObjectIdentity
mitelBWMConformance = _MitelBWMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 2)
)
_MitelBWMGroups_ObjectIdentity = ObjectIdentity
mitelBWMGroups = _MitelBWMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mitelBWMGroups.setStatus("current")
_MitelBWMCompliances_ObjectIdentity = ObjectIdentity
mitelBWMCompliances = _MitelBWMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mitelBWMCompliances.setStatus("current")

# Managed Objects groups

mitelBWMCurrentStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 2, 1, 1)
)
mitelBWMCurrentStatisticsGroup.setObjects(
      *(("MITEL-BWM-MIB", "mitelBWMCurrentZoneID"),
        ("MITEL-BWM-MIB", "mitelBWMCurrentParentZoneID"),
        ("MITEL-BWM-MIB", "mitelBWMCurrentZAPID"),
        ("MITEL-BWM-MIB", "mitelBWMCurrentZAPLabel"),
        ("MITEL-BWM-MIB", "mitelBWMCurrentBandwidthInUse"),
        ("MITEL-BWM-MIB", "mitelBWMCurrentBandwidthLimit"),
        ("MITEL-BWM-MIB", "mitelBWMCurrentBandwidthRatio"))
)
if mibBuilder.loadTexts:
    mitelBWMCurrentStatisticsGroup.setStatus("current")

mitelBWMCumulativeStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 2, 1, 2)
)
mitelBWMCumulativeStatisticsGroup.setObjects(
      *(("MITEL-BWM-MIB", "mitelBWMCumZoneID"),
        ("MITEL-BWM-MIB", "mitelBWMCumParentZoneID"),
        ("MITEL-BWM-MIB", "mitelBWMCumZAPID"),
        ("MITEL-BWM-MIB", "mitelBWMCumZAPLabel"),
        ("MITEL-BWM-MIB", "mitelBWMCumCACAdmissions"),
        ("MITEL-BWM-MIB", "mitelBWMCumCACRejections"),
        ("MITEL-BWM-MIB", "mitelBWMCumCACRejectionRatio"))
)
if mibBuilder.loadTexts:
    mitelBWMCumulativeStatisticsGroup.setStatus("current")

mitelBWMHistoricalStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 2, 1, 3)
)
mitelBWMHistoricalStatisticsGroup.setObjects(
      *(("MITEL-BWM-MIB", "mitelBWM15MinZoneID"),
        ("MITEL-BWM-MIB", "mitelBWM15MinParentZoneID"),
        ("MITEL-BWM-MIB", "mitelBWM15MinZAPID"),
        ("MITEL-BWM-MIB", "mitelBWM15MinDateAndTime"),
        ("MITEL-BWM-MIB", "mitelBWM15MinZAPLabel"),
        ("MITEL-BWM-MIB", "mitelBWM15MinCACAdmissions"),
        ("MITEL-BWM-MIB", "mitelBWM15MinCACRejections"),
        ("MITEL-BWM-MIB", "mitelBWM15MinCACRejectionRatio"),
        ("MITEL-BWM-MIB", "mitelBWM15MinAverageBandwidthUsed"),
        ("MITEL-BWM-MIB", "mitelBWM15MinPeakBandwidthUsed"),
        ("MITEL-BWM-MIB", "mitelBWM15MinAverageAvailable"),
        ("MITEL-BWM-MIB", "mitelBWM15MinFinalBandwidthLimit"),
        ("MITEL-BWM-MIB", "mitelBWM15MinPeakBandwidthRatio"),
        ("MITEL-BWM-MIB", "mitelBWM15MinPeakBwdthAboveLimit"),
        ("MITEL-BWM-MIB", "mitelBWM24HrZoneID"),
        ("MITEL-BWM-MIB", "mitelBWM24HrParentZoneID"),
        ("MITEL-BWM-MIB", "mitelBWM24HrZAPID"),
        ("MITEL-BWM-MIB", "mitelBWM24HrDateAndTime"),
        ("MITEL-BWM-MIB", "mitelBWM24HrZAPLabel"),
        ("MITEL-BWM-MIB", "mitelBWM24HrCACAdmissions"),
        ("MITEL-BWM-MIB", "mitelBWM24HrCACRejections"),
        ("MITEL-BWM-MIB", "mitelBWM24HrCACRejectionRatio"),
        ("MITEL-BWM-MIB", "mitelBWM24HrAverageBandwidthUsed"),
        ("MITEL-BWM-MIB", "mitelBWM24HrPeakBandwidthUsed"),
        ("MITEL-BWM-MIB", "mitelBWM24HrAverageAvailable"),
        ("MITEL-BWM-MIB", "mitelBWM24HrFinalBandwidthLimit"),
        ("MITEL-BWM-MIB", "mitelBWM24HrPeakBandwidthRatio"),
        ("MITEL-BWM-MIB", "mitelBWM24HrPeakBwdthAboveLimit"))
)
if mibBuilder.loadTexts:
    mitelBWMHistoricalStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mitelBWMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 1, 2, 5, 1, 2, 2, 1)
)
mitelBWMCompliance.setObjects(
      *(("MITEL-BWM-MIB", "mitelBWMCurrentStatisticsGroup"),
        ("MITEL-BWM-MIB", "mitelBWMCumulativeStatisticsGroup"),
        ("MITEL-BWM-MIB", "mitelBWMHistoricalStatisticsGroup"))
)
if mibBuilder.loadTexts:
    mitelBWMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-BWM-MIB",
    **{"MitelBWMPercentage": MitelBWMPercentage,
       "MitelBWMZoneID": MitelBWMZoneID,
       "MitelBWMZAPID": MitelBWMZAPID,
       "mitelBandWidthManagement": mitelBandWidthManagement,
       "mitelBWMObjects": mitelBWMObjects,
       "mitelBWMCurrentTable": mitelBWMCurrentTable,
       "mitelBWMCurrentTableEntry": mitelBWMCurrentTableEntry,
       "mitelBWMCurrentZoneID": mitelBWMCurrentZoneID,
       "mitelBWMCurrentParentZoneID": mitelBWMCurrentParentZoneID,
       "mitelBWMCurrentZAPID": mitelBWMCurrentZAPID,
       "mitelBWMCurrentZAPLabel": mitelBWMCurrentZAPLabel,
       "mitelBWMCurrentBandwidthInUse": mitelBWMCurrentBandwidthInUse,
       "mitelBWMCurrentBandwidthLimit": mitelBWMCurrentBandwidthLimit,
       "mitelBWMCurrentBandwidthRatio": mitelBWMCurrentBandwidthRatio,
       "mitelBWMCumCACTable": mitelBWMCumCACTable,
       "mitelBWMCumCACTableEntry": mitelBWMCumCACTableEntry,
       "mitelBWMCumZoneID": mitelBWMCumZoneID,
       "mitelBWMCumParentZoneID": mitelBWMCumParentZoneID,
       "mitelBWMCumZAPID": mitelBWMCumZAPID,
       "mitelBWMCumZAPLabel": mitelBWMCumZAPLabel,
       "mitelBWMCumCACAdmissions": mitelBWMCumCACAdmissions,
       "mitelBWMCumCACRejections": mitelBWMCumCACRejections,
       "mitelBWMCumCACRejectionRatio": mitelBWMCumCACRejectionRatio,
       "mitelBWM15MinHistoryTable": mitelBWM15MinHistoryTable,
       "mitelBWM15MinHistoryTableEntry": mitelBWM15MinHistoryTableEntry,
       "mitelBWM15MinZoneID": mitelBWM15MinZoneID,
       "mitelBWM15MinParentZoneID": mitelBWM15MinParentZoneID,
       "mitelBWM15MinZAPID": mitelBWM15MinZAPID,
       "mitelBWM15MinDateAndTime": mitelBWM15MinDateAndTime,
       "mitelBWM15MinZAPLabel": mitelBWM15MinZAPLabel,
       "mitelBWM15MinCACAdmissions": mitelBWM15MinCACAdmissions,
       "mitelBWM15MinCACRejections": mitelBWM15MinCACRejections,
       "mitelBWM15MinCACRejectionRatio": mitelBWM15MinCACRejectionRatio,
       "mitelBWM15MinAverageBandwidthUsed": mitelBWM15MinAverageBandwidthUsed,
       "mitelBWM15MinPeakBandwidthUsed": mitelBWM15MinPeakBandwidthUsed,
       "mitelBWM15MinAverageAvailable": mitelBWM15MinAverageAvailable,
       "mitelBWM15MinFinalBandwidthLimit": mitelBWM15MinFinalBandwidthLimit,
       "mitelBWM15MinPeakBandwidthRatio": mitelBWM15MinPeakBandwidthRatio,
       "mitelBWM15MinPeakBwdthAboveLimit": mitelBWM15MinPeakBwdthAboveLimit,
       "mitelBWM24HrHistoryTable": mitelBWM24HrHistoryTable,
       "mitelBWM24HrHistoryTableEntry": mitelBWM24HrHistoryTableEntry,
       "mitelBWM24HrZoneID": mitelBWM24HrZoneID,
       "mitelBWM24HrParentZoneID": mitelBWM24HrParentZoneID,
       "mitelBWM24HrZAPID": mitelBWM24HrZAPID,
       "mitelBWM24HrDateAndTime": mitelBWM24HrDateAndTime,
       "mitelBWM24HrZAPLabel": mitelBWM24HrZAPLabel,
       "mitelBWM24HrCACAdmissions": mitelBWM24HrCACAdmissions,
       "mitelBWM24HrCACRejections": mitelBWM24HrCACRejections,
       "mitelBWM24HrCACRejectionRatio": mitelBWM24HrCACRejectionRatio,
       "mitelBWM24HrAverageBandwidthUsed": mitelBWM24HrAverageBandwidthUsed,
       "mitelBWM24HrPeakBandwidthUsed": mitelBWM24HrPeakBandwidthUsed,
       "mitelBWM24HrAverageAvailable": mitelBWM24HrAverageAvailable,
       "mitelBWM24HrFinalBandwidthLimit": mitelBWM24HrFinalBandwidthLimit,
       "mitelBWM24HrPeakBandwidthRatio": mitelBWM24HrPeakBandwidthRatio,
       "mitelBWM24HrPeakBwdthAboveLimit": mitelBWM24HrPeakBwdthAboveLimit,
       "mitelBWMConformance": mitelBWMConformance,
       "mitelBWMGroups": mitelBWMGroups,
       "mitelBWMCurrentStatisticsGroup": mitelBWMCurrentStatisticsGroup,
       "mitelBWMCumulativeStatisticsGroup": mitelBWMCumulativeStatisticsGroup,
       "mitelBWMHistoricalStatisticsGroup": mitelBWMHistoricalStatisticsGroup,
       "mitelBWMCompliances": mitelBWMCompliances,
       "mitelBWMCompliance": mitelBWMCompliance}
)
