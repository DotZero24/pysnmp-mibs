# SNMP MIB module (BUFFALO-NAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/buffalo/BUFFALO-NAS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:18 2025
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

(buffalo,) = mibBuilder.importSymbols(
    "BUFFALO-ROOT-MIB",
    "buffalo")

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
 enterprises,
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
    "enterprises",
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

teraStation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 27)
)
if mibBuilder.loadTexts:
    teraStation.setRevisions(
        ("2020-03-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DayOfWeek(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sun", 1),
          ("mon", 2),
          ("tue", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )



class LongUTF8String(TextualConvention, OctetString):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_TeraStationObjects_ObjectIdentity = ObjectIdentity
teraStationObjects = _TeraStationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1)
)
_NasBackupTable_Object = MibTable
nasBackupTable = _NasBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 1)
)
if mibBuilder.loadTexts:
    nasBackupTable.setStatus("current")
_NasBackupEntry_Object = MibTableRow
nasBackupEntry = _NasBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 1, 1)
)
nasBackupEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasBackupIndex"),
)
if mibBuilder.loadTexts:
    nasBackupEntry.setStatus("current")


class _NasBackupIndex_Type(Integer32):
    """Custom type nasBackupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NasBackupIndex_Type.__name__ = "Integer32"
_NasBackupIndex_Object = MibTableColumn
nasBackupIndex = _NasBackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 1, 1, 1),
    _NasBackupIndex_Type()
)
nasBackupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasBackupIndex.setStatus("current")


class _NasBackupStatus_Type(Integer32):
    """Custom type nasBackupStatus based on Integer32"""
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
        *(("ready", 1),
          ("run", 2),
          ("done", 3),
          ("error", 4))
    )


_NasBackupStatus_Type.__name__ = "Integer32"
_NasBackupStatus_Object = MibTableColumn
nasBackupStatus = _NasBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 1, 1, 3),
    _NasBackupStatus_Type()
)
nasBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasBackupStatus.setStatus("current")
_NasDiskTable_Object = MibTable
nasDiskTable = _NasDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2)
)
if mibBuilder.loadTexts:
    nasDiskTable.setStatus("current")
_NasDiskEntry_Object = MibTableRow
nasDiskEntry = _NasDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1)
)
nasDiskEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasDiskIndex"),
)
if mibBuilder.loadTexts:
    nasDiskEntry.setStatus("current")
_NasDiskIndex_Type = Integer32
_NasDiskIndex_Object = MibTableColumn
nasDiskIndex = _NasDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 1),
    _NasDiskIndex_Type()
)
nasDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasDiskIndex.setStatus("current")


class _NasDiskStatus_Type(Integer32):
    """Custom type nasDiskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", -1),
          ("normal", 1),
          ("array1", 2),
          ("array2", 3),
          ("standby", 4),
          ("degrade", 5),
          ("remove", 6),
          ("standbyRemoved", 7),
          ("degradeRemoved", 8),
          ("removeRemoved", 9),
          ("array3", 10),
          ("array4", 11),
          ("mediaCartridge", 12),
          ("array5", 13),
          ("array6", 14))
    )


_NasDiskStatus_Type.__name__ = "Integer32"
_NasDiskStatus_Object = MibTableColumn
nasDiskStatus = _NasDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 2),
    _NasDiskStatus_Type()
)
nasDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskStatus.setStatus("current")
_NasDiskCapacity_Type = Integer32
_NasDiskCapacity_Object = MibTableColumn
nasDiskCapacity = _NasDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 3),
    _NasDiskCapacity_Type()
)
nasDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskCapacity.setStatus("current")


class _NasDiskUsed_Type(Integer32):
    """Custom type nasDiskUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_NasDiskUsed_Type.__name__ = "Integer32"
_NasDiskUsed_Object = MibTableColumn
nasDiskUsed = _NasDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 4),
    _NasDiskUsed_Type()
)
nasDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskUsed.setStatus("current")
if mibBuilder.loadTexts:
    nasDiskUsed.setUnits("%")


class _NasDiskSMARTStatus_Type(Integer32):
    """Custom type nasDiskSMARTStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", -2),
          ("unknown", -1),
          ("normal", 1),
          ("caution", 2),
          ("fail", 3))
    )


_NasDiskSMARTStatus_Type.__name__ = "Integer32"
_NasDiskSMARTStatus_Object = MibTableColumn
nasDiskSMARTStatus = _NasDiskSMARTStatus_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 5),
    _NasDiskSMARTStatus_Type()
)
nasDiskSMARTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTStatus.setStatus("current")
_NasDiskSMARTReallocatedSectorCtValue_Type = Integer32
_NasDiskSMARTReallocatedSectorCtValue_Object = MibTableColumn
nasDiskSMARTReallocatedSectorCtValue = _NasDiskSMARTReallocatedSectorCtValue_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 6),
    _NasDiskSMARTReallocatedSectorCtValue_Type()
)
nasDiskSMARTReallocatedSectorCtValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTReallocatedSectorCtValue.setStatus("current")
_NasDiskSMARTReallocatedSectorCtWorst_Type = Integer32
_NasDiskSMARTReallocatedSectorCtWorst_Object = MibTableColumn
nasDiskSMARTReallocatedSectorCtWorst = _NasDiskSMARTReallocatedSectorCtWorst_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 7),
    _NasDiskSMARTReallocatedSectorCtWorst_Type()
)
nasDiskSMARTReallocatedSectorCtWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTReallocatedSectorCtWorst.setStatus("current")
_NasDiskSMARTReallocatedSectorCtThresh_Type = Integer32
_NasDiskSMARTReallocatedSectorCtThresh_Object = MibTableColumn
nasDiskSMARTReallocatedSectorCtThresh = _NasDiskSMARTReallocatedSectorCtThresh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 8),
    _NasDiskSMARTReallocatedSectorCtThresh_Type()
)
nasDiskSMARTReallocatedSectorCtThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTReallocatedSectorCtThresh.setStatus("current")
_NasDiskSMARTReallocatedSectorCtRAW_Type = DisplayString
_NasDiskSMARTReallocatedSectorCtRAW_Object = MibTableColumn
nasDiskSMARTReallocatedSectorCtRAW = _NasDiskSMARTReallocatedSectorCtRAW_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 9),
    _NasDiskSMARTReallocatedSectorCtRAW_Type()
)
nasDiskSMARTReallocatedSectorCtRAW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTReallocatedSectorCtRAW.setStatus("current")
_NasDiskSMARTCurrentPendingSectorValue_Type = Integer32
_NasDiskSMARTCurrentPendingSectorValue_Object = MibTableColumn
nasDiskSMARTCurrentPendingSectorValue = _NasDiskSMARTCurrentPendingSectorValue_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 10),
    _NasDiskSMARTCurrentPendingSectorValue_Type()
)
nasDiskSMARTCurrentPendingSectorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTCurrentPendingSectorValue.setStatus("current")
_NasDiskSMARTCurrentPendingSectorWorst_Type = Integer32
_NasDiskSMARTCurrentPendingSectorWorst_Object = MibTableColumn
nasDiskSMARTCurrentPendingSectorWorst = _NasDiskSMARTCurrentPendingSectorWorst_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 11),
    _NasDiskSMARTCurrentPendingSectorWorst_Type()
)
nasDiskSMARTCurrentPendingSectorWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTCurrentPendingSectorWorst.setStatus("current")
_NasDiskSMARTCurrentPendingSectorThresh_Type = Integer32
_NasDiskSMARTCurrentPendingSectorThresh_Object = MibTableColumn
nasDiskSMARTCurrentPendingSectorThresh = _NasDiskSMARTCurrentPendingSectorThresh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 12),
    _NasDiskSMARTCurrentPendingSectorThresh_Type()
)
nasDiskSMARTCurrentPendingSectorThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTCurrentPendingSectorThresh.setStatus("current")
_NasDiskSMARTCurrentPendingSectorRAW_Type = DisplayString
_NasDiskSMARTCurrentPendingSectorRAW_Object = MibTableColumn
nasDiskSMARTCurrentPendingSectorRAW = _NasDiskSMARTCurrentPendingSectorRAW_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 13),
    _NasDiskSMARTCurrentPendingSectorRAW_Type()
)
nasDiskSMARTCurrentPendingSectorRAW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTCurrentPendingSectorRAW.setStatus("current")
_NasDiskSMARTOfflineUncorrectableValue_Type = Integer32
_NasDiskSMARTOfflineUncorrectableValue_Object = MibTableColumn
nasDiskSMARTOfflineUncorrectableValue = _NasDiskSMARTOfflineUncorrectableValue_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 14),
    _NasDiskSMARTOfflineUncorrectableValue_Type()
)
nasDiskSMARTOfflineUncorrectableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTOfflineUncorrectableValue.setStatus("current")
_NasDiskSMARTOfflineUncorrectableWorst_Type = Integer32
_NasDiskSMARTOfflineUncorrectableWorst_Object = MibTableColumn
nasDiskSMARTOfflineUncorrectableWorst = _NasDiskSMARTOfflineUncorrectableWorst_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 15),
    _NasDiskSMARTOfflineUncorrectableWorst_Type()
)
nasDiskSMARTOfflineUncorrectableWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTOfflineUncorrectableWorst.setStatus("current")
_NasDiskSMARTOfflineUncorrectableThresh_Type = Integer32
_NasDiskSMARTOfflineUncorrectableThresh_Object = MibTableColumn
nasDiskSMARTOfflineUncorrectableThresh = _NasDiskSMARTOfflineUncorrectableThresh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 16),
    _NasDiskSMARTOfflineUncorrectableThresh_Type()
)
nasDiskSMARTOfflineUncorrectableThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTOfflineUncorrectableThresh.setStatus("current")
_NasDiskSMARTOfflineUncorrectableRAW_Type = DisplayString
_NasDiskSMARTOfflineUncorrectableRAW_Object = MibTableColumn
nasDiskSMARTOfflineUncorrectableRAW = _NasDiskSMARTOfflineUncorrectableRAW_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 17),
    _NasDiskSMARTOfflineUncorrectableRAW_Type()
)
nasDiskSMARTOfflineUncorrectableRAW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTOfflineUncorrectableRAW.setStatus("current")
_NasSSDSMARTRemainingLifeValue_Type = Integer32
_NasSSDSMARTRemainingLifeValue_Object = MibTableColumn
nasSSDSMARTRemainingLifeValue = _NasSSDSMARTRemainingLifeValue_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 18),
    _NasSSDSMARTRemainingLifeValue_Type()
)
nasSSDSMARTRemainingLifeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasSSDSMARTRemainingLifeValue.setStatus("current")
_NasSSDSMARTRemainingLifeWorst_Type = Integer32
_NasSSDSMARTRemainingLifeWorst_Object = MibTableColumn
nasSSDSMARTRemainingLifeWorst = _NasSSDSMARTRemainingLifeWorst_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 19),
    _NasSSDSMARTRemainingLifeWorst_Type()
)
nasSSDSMARTRemainingLifeWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasSSDSMARTRemainingLifeWorst.setStatus("current")
_NasSSDSMARTRemainingLifeThresh_Type = Integer32
_NasSSDSMARTRemainingLifeThresh_Object = MibTableColumn
nasSSDSMARTRemainingLifeThresh = _NasSSDSMARTRemainingLifeThresh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 20),
    _NasSSDSMARTRemainingLifeThresh_Type()
)
nasSSDSMARTRemainingLifeThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasSSDSMARTRemainingLifeThresh.setStatus("current")
_NasSSDSMARTBadBlockCountValue_Type = Integer32
_NasSSDSMARTBadBlockCountValue_Object = MibTableColumn
nasSSDSMARTBadBlockCountValue = _NasSSDSMARTBadBlockCountValue_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 21),
    _NasSSDSMARTBadBlockCountValue_Type()
)
nasSSDSMARTBadBlockCountValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasSSDSMARTBadBlockCountValue.setStatus("current")
_NasSSDSMARTBadBlockCountWorst_Type = Integer32
_NasSSDSMARTBadBlockCountWorst_Object = MibTableColumn
nasSSDSMARTBadBlockCountWorst = _NasSSDSMARTBadBlockCountWorst_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 22),
    _NasSSDSMARTBadBlockCountWorst_Type()
)
nasSSDSMARTBadBlockCountWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasSSDSMARTBadBlockCountWorst.setStatus("current")
_NasSSDSMARTBadBlockCountThresh_Type = Integer32
_NasSSDSMARTBadBlockCountThresh_Object = MibTableColumn
nasSSDSMARTBadBlockCountThresh = _NasSSDSMARTBadBlockCountThresh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 23),
    _NasSSDSMARTBadBlockCountThresh_Type()
)
nasSSDSMARTBadBlockCountThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasSSDSMARTBadBlockCountThresh.setStatus("current")
_NasDiskCapacityGiB_Type = Integer32
_NasDiskCapacityGiB_Object = MibTableColumn
nasDiskCapacityGiB = _NasDiskCapacityGiB_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 24),
    _NasDiskCapacityGiB_Type()
)
nasDiskCapacityGiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskCapacityGiB.setStatus("current")
_NasDiskCapacityLow_Type = Unsigned32
_NasDiskCapacityLow_Object = MibTableColumn
nasDiskCapacityLow = _NasDiskCapacityLow_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 25),
    _NasDiskCapacityLow_Type()
)
nasDiskCapacityLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskCapacityLow.setStatus("current")
_NasDiskCapacityHigh_Type = Unsigned32
_NasDiskCapacityHigh_Object = MibTableColumn
nasDiskCapacityHigh = _NasDiskCapacityHigh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 26),
    _NasDiskCapacityHigh_Type()
)
nasDiskCapacityHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskCapacityHigh.setStatus("current")
_NasDiskUsedGiB_Type = Integer32
_NasDiskUsedGiB_Object = MibTableColumn
nasDiskUsedGiB = _NasDiskUsedGiB_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 27),
    _NasDiskUsedGiB_Type()
)
nasDiskUsedGiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskUsedGiB.setStatus("current")
_NasDiskUsedLow_Type = Unsigned32
_NasDiskUsedLow_Object = MibTableColumn
nasDiskUsedLow = _NasDiskUsedLow_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 28),
    _NasDiskUsedLow_Type()
)
nasDiskUsedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskUsedLow.setStatus("current")
_NasDiskUsedHigh_Type = Unsigned32
_NasDiskUsedHigh_Object = MibTableColumn
nasDiskUsedHigh = _NasDiskUsedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 29),
    _NasDiskUsedHigh_Type()
)
nasDiskUsedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskUsedHigh.setStatus("current")
_NasDiskModelName_Type = DisplayString
_NasDiskModelName_Object = MibTableColumn
nasDiskModelName = _NasDiskModelName_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 30),
    _NasDiskModelName_Type()
)
nasDiskModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskModelName.setStatus("current")


class _NasDiskSMARTReallocatedSectorCtHealth_Type(Integer32):
    """Custom type nasDiskSMARTReallocatedSectorCtHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", -2),
          ("normal", 1),
          ("fail", 3))
    )


_NasDiskSMARTReallocatedSectorCtHealth_Type.__name__ = "Integer32"
_NasDiskSMARTReallocatedSectorCtHealth_Object = MibTableColumn
nasDiskSMARTReallocatedSectorCtHealth = _NasDiskSMARTReallocatedSectorCtHealth_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 31),
    _NasDiskSMARTReallocatedSectorCtHealth_Type()
)
nasDiskSMARTReallocatedSectorCtHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTReallocatedSectorCtHealth.setStatus("current")


class _NasDiskSMARTCurrentPendingSectorHealth_Type(Integer32):
    """Custom type nasDiskSMARTCurrentPendingSectorHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", -2),
          ("normal", 1),
          ("fail", 3))
    )


_NasDiskSMARTCurrentPendingSectorHealth_Type.__name__ = "Integer32"
_NasDiskSMARTCurrentPendingSectorHealth_Object = MibTableColumn
nasDiskSMARTCurrentPendingSectorHealth = _NasDiskSMARTCurrentPendingSectorHealth_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 32),
    _NasDiskSMARTCurrentPendingSectorHealth_Type()
)
nasDiskSMARTCurrentPendingSectorHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTCurrentPendingSectorHealth.setStatus("current")


class _NasDiskSMARTOfflineUncorrectableHealth_Type(Integer32):
    """Custom type nasDiskSMARTOfflineUncorrectableHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", -2),
          ("normal", 1),
          ("fail", 3))
    )


_NasDiskSMARTOfflineUncorrectableHealth_Type.__name__ = "Integer32"
_NasDiskSMARTOfflineUncorrectableHealth_Object = MibTableColumn
nasDiskSMARTOfflineUncorrectableHealth = _NasDiskSMARTOfflineUncorrectableHealth_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 33),
    _NasDiskSMARTOfflineUncorrectableHealth_Type()
)
nasDiskSMARTOfflineUncorrectableHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTOfflineUncorrectableHealth.setStatus("current")
_NasDiskSMARTRawReadErrorRateValue_Type = Integer32
_NasDiskSMARTRawReadErrorRateValue_Object = MibTableColumn
nasDiskSMARTRawReadErrorRateValue = _NasDiskSMARTRawReadErrorRateValue_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 34),
    _NasDiskSMARTRawReadErrorRateValue_Type()
)
nasDiskSMARTRawReadErrorRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTRawReadErrorRateValue.setStatus("current")
_NasDiskSMARTRawReadErrorRateWorst_Type = Integer32
_NasDiskSMARTRawReadErrorRateWorst_Object = MibTableColumn
nasDiskSMARTRawReadErrorRateWorst = _NasDiskSMARTRawReadErrorRateWorst_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 35),
    _NasDiskSMARTRawReadErrorRateWorst_Type()
)
nasDiskSMARTRawReadErrorRateWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTRawReadErrorRateWorst.setStatus("current")
_NasDiskSMARTRawReadErrorRateThresh_Type = Integer32
_NasDiskSMARTRawReadErrorRateThresh_Object = MibTableColumn
nasDiskSMARTRawReadErrorRateThresh = _NasDiskSMARTRawReadErrorRateThresh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 36),
    _NasDiskSMARTRawReadErrorRateThresh_Type()
)
nasDiskSMARTRawReadErrorRateThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTRawReadErrorRateThresh.setStatus("current")
_NasDiskSMARTRawReadErrorRateRAW_Type = DisplayString
_NasDiskSMARTRawReadErrorRateRAW_Object = MibTableColumn
nasDiskSMARTRawReadErrorRateRAW = _NasDiskSMARTRawReadErrorRateRAW_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 37),
    _NasDiskSMARTRawReadErrorRateRAW_Type()
)
nasDiskSMARTRawReadErrorRateRAW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTRawReadErrorRateRAW.setStatus("current")
_NasDiskSMARTRawReadErrorRateHealth_Type = Integer32
_NasDiskSMARTRawReadErrorRateHealth_Object = MibTableColumn
nasDiskSMARTRawReadErrorRateHealth = _NasDiskSMARTRawReadErrorRateHealth_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 38),
    _NasDiskSMARTRawReadErrorRateHealth_Type()
)
nasDiskSMARTRawReadErrorRateHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTRawReadErrorRateHealth.setStatus("current")
_NasDiskSMARTPowerOnHoursValue_Type = Integer32
_NasDiskSMARTPowerOnHoursValue_Object = MibTableColumn
nasDiskSMARTPowerOnHoursValue = _NasDiskSMARTPowerOnHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 39),
    _NasDiskSMARTPowerOnHoursValue_Type()
)
nasDiskSMARTPowerOnHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTPowerOnHoursValue.setStatus("current")
_NasDiskSMARTPowerOnHoursWorst_Type = Integer32
_NasDiskSMARTPowerOnHoursWorst_Object = MibTableColumn
nasDiskSMARTPowerOnHoursWorst = _NasDiskSMARTPowerOnHoursWorst_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 40),
    _NasDiskSMARTPowerOnHoursWorst_Type()
)
nasDiskSMARTPowerOnHoursWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTPowerOnHoursWorst.setStatus("current")
_NasDiskSMARTPowerOnHoursThresh_Type = Integer32
_NasDiskSMARTPowerOnHoursThresh_Object = MibTableColumn
nasDiskSMARTPowerOnHoursThresh = _NasDiskSMARTPowerOnHoursThresh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 41),
    _NasDiskSMARTPowerOnHoursThresh_Type()
)
nasDiskSMARTPowerOnHoursThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTPowerOnHoursThresh.setStatus("current")
_NasDiskSMARTPowerOnHoursRAW_Type = DisplayString
_NasDiskSMARTPowerOnHoursRAW_Object = MibTableColumn
nasDiskSMARTPowerOnHoursRAW = _NasDiskSMARTPowerOnHoursRAW_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 42),
    _NasDiskSMARTPowerOnHoursRAW_Type()
)
nasDiskSMARTPowerOnHoursRAW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTPowerOnHoursRAW.setStatus("current")
_NasDiskSMARTPowerOnHoursHealth_Type = Integer32
_NasDiskSMARTPowerOnHoursHealth_Object = MibTableColumn
nasDiskSMARTPowerOnHoursHealth = _NasDiskSMARTPowerOnHoursHealth_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 2, 1, 43),
    _NasDiskSMARTPowerOnHoursHealth_Type()
)
nasDiskSMARTPowerOnHoursHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDiskSMARTPowerOnHoursHealth.setStatus("current")
_NasArrayTable_Object = MibTable
nasArrayTable = _NasArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3)
)
if mibBuilder.loadTexts:
    nasArrayTable.setStatus("current")
_NasArrayEntry_Object = MibTableRow
nasArrayEntry = _NasArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1)
)
nasArrayEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasArrayIndex"),
)
if mibBuilder.loadTexts:
    nasArrayEntry.setStatus("current")
_NasArrayIndex_Type = Integer32
_NasArrayIndex_Object = MibTableColumn
nasArrayIndex = _NasArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 1),
    _NasArrayIndex_Type()
)
nasArrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasArrayIndex.setStatus("current")


class _NasArrayStatus_Type(Integer32):
    """Custom type nasArrayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", -1),
          ("off", 1),
          ("raid0", 2),
          ("raid1", 3),
          ("raid5", 4),
          ("raid6", 5),
          ("raid10", 6),
          ("raid50", 7),
          ("raid51", 8),
          ("raid60", 9),
          ("raid61", 10))
    )


_NasArrayStatus_Type.__name__ = "Integer32"
_NasArrayStatus_Object = MibTableColumn
nasArrayStatus = _NasArrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 2),
    _NasArrayStatus_Type()
)
nasArrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasArrayStatus.setStatus("current")
_NasArrayCapacity_Type = Integer32
_NasArrayCapacity_Object = MibTableColumn
nasArrayCapacity = _NasArrayCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 3),
    _NasArrayCapacity_Type()
)
nasArrayCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasArrayCapacity.setStatus("current")


class _NasArrayUsed_Type(Integer32):
    """Custom type nasArrayUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_NasArrayUsed_Type.__name__ = "Integer32"
_NasArrayUsed_Object = MibTableColumn
nasArrayUsed = _NasArrayUsed_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 4),
    _NasArrayUsed_Type()
)
nasArrayUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasArrayUsed.setStatus("current")
if mibBuilder.loadTexts:
    nasArrayUsed.setUnits("%")
_NasArrayCapacityGiB_Type = Integer32
_NasArrayCapacityGiB_Object = MibTableColumn
nasArrayCapacityGiB = _NasArrayCapacityGiB_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 5),
    _NasArrayCapacityGiB_Type()
)
nasArrayCapacityGiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasArrayCapacityGiB.setStatus("current")
_NasArrayCapacityLow_Type = Unsigned32
_NasArrayCapacityLow_Object = MibTableColumn
nasArrayCapacityLow = _NasArrayCapacityLow_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 6),
    _NasArrayCapacityLow_Type()
)
nasArrayCapacityLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasArrayCapacityLow.setStatus("current")
_NasArrayCapacityHigh_Type = Unsigned32
_NasArrayCapacityHigh_Object = MibTableColumn
nasArrayCapacityHigh = _NasArrayCapacityHigh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 7),
    _NasArrayCapacityHigh_Type()
)
nasArrayCapacityHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasArrayCapacityHigh.setStatus("current")
_NasArrayUsedGiB_Type = Integer32
_NasArrayUsedGiB_Object = MibTableColumn
nasArrayUsedGiB = _NasArrayUsedGiB_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 8),
    _NasArrayUsedGiB_Type()
)
nasArrayUsedGiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasArrayUsedGiB.setStatus("current")
_NasArrayUsedLow_Type = Unsigned32
_NasArrayUsedLow_Object = MibTableColumn
nasArrayUsedLow = _NasArrayUsedLow_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 9),
    _NasArrayUsedLow_Type()
)
nasArrayUsedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasArrayUsedLow.setStatus("current")
_NasArrayUsedHigh_Type = Unsigned32
_NasArrayUsedHigh_Object = MibTableColumn
nasArrayUsedHigh = _NasArrayUsedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 3, 1, 10),
    _NasArrayUsedHigh_Type()
)
nasArrayUsedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasArrayUsedHigh.setStatus("current")
_NasErrorTable_Object = MibTable
nasErrorTable = _NasErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 4)
)
if mibBuilder.loadTexts:
    nasErrorTable.setStatus("current")
_NasErrorEntry_Object = MibTableRow
nasErrorEntry = _NasErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 4, 1)
)
nasErrorEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasErrorIndex"),
)
if mibBuilder.loadTexts:
    nasErrorEntry.setStatus("current")


class _NasErrorIndex_Type(Integer32):
    """Custom type nasErrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_NasErrorIndex_Type.__name__ = "Integer32"
_NasErrorIndex_Object = MibTableColumn
nasErrorIndex = _NasErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 4, 1, 1),
    _NasErrorIndex_Type()
)
nasErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasErrorIndex.setStatus("current")
_NasErrorMsg_Type = DisplayString
_NasErrorMsg_Object = MibTableColumn
nasErrorMsg = _NasErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 4, 1, 2),
    _NasErrorMsg_Type()
)
nasErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasErrorMsg.setStatus("current")
_NasErrorDate_Type = DisplayString
_NasErrorDate_Object = MibTableColumn
nasErrorDate = _NasErrorDate_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 4, 1, 3),
    _NasErrorDate_Type()
)
nasErrorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasErrorDate.setStatus("current")
_NasErrorDateAndTime_Type = DateAndTime
_NasErrorDateAndTime_Object = MibTableColumn
nasErrorDateAndTime = _NasErrorDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 4, 1, 4),
    _NasErrorDateAndTime_Type()
)
nasErrorDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasErrorDateAndTime.setStatus("current")
_NasInformationTable_Object = MibTable
nasInformationTable = _NasInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 5)
)
if mibBuilder.loadTexts:
    nasInformationTable.setStatus("current")
_NasInformationEntry_Object = MibTableRow
nasInformationEntry = _NasInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 5, 1)
)
nasInformationEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasInformationIndex"),
)
if mibBuilder.loadTexts:
    nasInformationEntry.setStatus("current")


class _NasInformationIndex_Type(Integer32):
    """Custom type nasInformationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_NasInformationIndex_Type.__name__ = "Integer32"
_NasInformationIndex_Object = MibTableColumn
nasInformationIndex = _NasInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 5, 1, 1),
    _NasInformationIndex_Type()
)
nasInformationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasInformationIndex.setStatus("current")
_NasInformationMsg_Type = DisplayString
_NasInformationMsg_Object = MibTableColumn
nasInformationMsg = _NasInformationMsg_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 5, 1, 2),
    _NasInformationMsg_Type()
)
nasInformationMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInformationMsg.setStatus("current")
_NasInformationDate_Type = DisplayString
_NasInformationDate_Object = MibTableColumn
nasInformationDate = _NasInformationDate_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 5, 1, 3),
    _NasInformationDate_Type()
)
nasInformationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInformationDate.setStatus("current")
_NasInformationDateAndTime_Type = DateAndTime
_NasInformationDateAndTime_Object = MibTableColumn
nasInformationDateAndTime = _NasInformationDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 5, 1, 4),
    _NasInformationDateAndTime_Type()
)
nasInformationDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInformationDateAndTime.setStatus("current")
_NasLVMParams_ObjectIdentity = ObjectIdentity
nasLVMParams = _NasLVMParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6)
)
_NasVGTable_Object = MibTable
nasVGTable = _NasVGTable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1)
)
if mibBuilder.loadTexts:
    nasVGTable.setStatus("current")
_NasVGEntry_Object = MibTableRow
nasVGEntry = _NasVGEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1)
)
nasVGEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasVGIndex"),
)
if mibBuilder.loadTexts:
    nasVGEntry.setStatus("current")
_NasVGIndex_Type = Integer32
_NasVGIndex_Object = MibTableColumn
nasVGIndex = _NasVGIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 1),
    _NasVGIndex_Type()
)
nasVGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasVGIndex.setStatus("current")
_NasVGPESize_Type = Integer32
_NasVGPESize_Object = MibTableColumn
nasVGPESize = _NasVGPESize_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 2),
    _NasVGPESize_Type()
)
nasVGPESize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasVGPESize.setStatus("current")
if mibBuilder.loadTexts:
    nasVGPESize.setUnits("GB")
_NasVGPETotal_Type = Integer32
_NasVGPETotal_Object = MibTableColumn
nasVGPETotal = _NasVGPETotal_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 3),
    _NasVGPETotal_Type()
)
nasVGPETotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasVGPETotal.setStatus("current")
_NasVGPEUsed_Type = Integer32
_NasVGPEUsed_Object = MibTableColumn
nasVGPEUsed = _NasVGPEUsed_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 4),
    _NasVGPEUsed_Type()
)
nasVGPEUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasVGPEUsed.setStatus("current")
_NasLVTable_Object = MibTable
nasLVTable = _NasLVTable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    nasLVTable.setStatus("current")
_NasLVEntry_Object = MibTableRow
nasLVEntry = _NasLVEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1)
)
nasLVEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasVGIndex"),
    (0, "BUFFALO-NAS-MIB", "nasLVIndex"),
)
if mibBuilder.loadTexts:
    nasLVEntry.setStatus("current")


class _NasLVIndex_Type(Integer32):
    """Custom type nasLVIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NasLVIndex_Type.__name__ = "Integer32"
_NasLVIndex_Object = MibTableColumn
nasLVIndex = _NasLVIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 1),
    _NasLVIndex_Type()
)
nasLVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasLVIndex.setStatus("current")
_NasLVName_Type = DisplayString
_NasLVName_Object = MibTableColumn
nasLVName = _NasLVName_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 2),
    _NasLVName_Type()
)
nasLVName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasLVName.setStatus("current")
_NasLVCapacity_Type = Integer32
_NasLVCapacity_Object = MibTableColumn
nasLVCapacity = _NasLVCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 3),
    _NasLVCapacity_Type()
)
nasLVCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasLVCapacity.setStatus("current")


class _NasLVUsed_Type(Integer32):
    """Custom type nasLVUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_NasLVUsed_Type.__name__ = "Integer32"
_NasLVUsed_Object = MibTableColumn
nasLVUsed = _NasLVUsed_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 4),
    _NasLVUsed_Type()
)
nasLVUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasLVUsed.setStatus("current")
if mibBuilder.loadTexts:
    nasLVUsed.setUnits("%")
_NasLVCapacityGiB_Type = Integer32
_NasLVCapacityGiB_Object = MibTableColumn
nasLVCapacityGiB = _NasLVCapacityGiB_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 5),
    _NasLVCapacityGiB_Type()
)
nasLVCapacityGiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasLVCapacityGiB.setStatus("current")
_NasLVCapacityLow_Type = Unsigned32
_NasLVCapacityLow_Object = MibTableColumn
nasLVCapacityLow = _NasLVCapacityLow_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 6),
    _NasLVCapacityLow_Type()
)
nasLVCapacityLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasLVCapacityLow.setStatus("current")
_NasLVCapacityHigh_Type = Unsigned32
_NasLVCapacityHigh_Object = MibTableColumn
nasLVCapacityHigh = _NasLVCapacityHigh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 7),
    _NasLVCapacityHigh_Type()
)
nasLVCapacityHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasLVCapacityHigh.setStatus("current")
_NasLVUsedGiB_Type = Integer32
_NasLVUsedGiB_Object = MibTableColumn
nasLVUsedGiB = _NasLVUsedGiB_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 8),
    _NasLVUsedGiB_Type()
)
nasLVUsedGiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasLVUsedGiB.setStatus("current")
_NasLVUsedLow_Type = Unsigned32
_NasLVUsedLow_Object = MibTableColumn
nasLVUsedLow = _NasLVUsedLow_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 9),
    _NasLVUsedLow_Type()
)
nasLVUsedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasLVUsedLow.setStatus("current")
_NasLVUsedHigh_Type = Unsigned32
_NasLVUsedHigh_Object = MibTableColumn
nasLVUsedHigh = _NasLVUsedHigh_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 5, 1, 10),
    _NasLVUsedHigh_Type()
)
nasLVUsedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasLVUsedHigh.setStatus("current")
_NasPVTable_Object = MibTable
nasPVTable = _NasPVTable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 6)
)
if mibBuilder.loadTexts:
    nasPVTable.setStatus("current")
_NasPVEntry_Object = MibTableRow
nasPVEntry = _NasPVEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 6, 1)
)
nasPVEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasVGIndex"),
    (0, "BUFFALO-NAS-MIB", "nasPVIndex"),
)
if mibBuilder.loadTexts:
    nasPVEntry.setStatus("current")
_NasPVIndex_Type = Integer32
_NasPVIndex_Object = MibTableColumn
nasPVIndex = _NasPVIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 6, 1, 1),
    _NasPVIndex_Type()
)
nasPVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasPVIndex.setStatus("current")
_NasPVName_Type = DisplayString
_NasPVName_Object = MibTableColumn
nasPVName = _NasPVName_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 6, 1, 1, 6, 1, 2),
    _NasPVName_Type()
)
nasPVName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasPVName.setStatus("current")
_NasFailoverParams_ObjectIdentity = ObjectIdentity
nasFailoverParams = _NasFailoverParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 7)
)


class _NasFailoverRole_Type(Integer32):
    """Custom type nasFailoverRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("main", 2),
          ("aloneMain", 4),
          ("backup", 8),
          ("aloneBackup", 16),
          ("maintenanceMain", 32),
          ("maintenanceBackup", 64),
          ("emMode", 128))
    )


_NasFailoverRole_Type.__name__ = "Integer32"
_NasFailoverRole_Object = MibScalar
nasFailoverRole = _NasFailoverRole_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 7, 1),
    _NasFailoverRole_Type()
)
nasFailoverRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasFailoverRole.setStatus("current")


class _NasFailoverStatus_Type(Integer32):
    """Custom type nasFailoverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("busy", 1),
          ("startingMain", 2),
          ("startingBackup", 3),
          ("initializing", 4),
          ("stopping", 32))
    )


_NasFailoverStatus_Type.__name__ = "Integer32"
_NasFailoverStatus_Object = MibScalar
nasFailoverStatus = _NasFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 7, 2),
    _NasFailoverStatus_Type()
)
nasFailoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasFailoverStatus.setStatus("current")
_NasFailoverPartner_Type = IpAddress
_NasFailoverPartner_Object = MibScalar
nasFailoverPartner = _NasFailoverPartner_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 7, 3),
    _NasFailoverPartner_Type()
)
nasFailoverPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasFailoverPartner.setStatus("current")
_NasRPSUTable_Object = MibTable
nasRPSUTable = _NasRPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 8)
)
if mibBuilder.loadTexts:
    nasRPSUTable.setStatus("current")
_NasRPSUEntry_Object = MibTableRow
nasRPSUEntry = _NasRPSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 8, 1)
)
nasRPSUEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasRPSUIndex"),
)
if mibBuilder.loadTexts:
    nasRPSUEntry.setStatus("current")
_NasRPSUIndex_Type = Integer32
_NasRPSUIndex_Object = MibTableColumn
nasRPSUIndex = _NasRPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 8, 1, 1),
    _NasRPSUIndex_Type()
)
nasRPSUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasRPSUIndex.setStatus("current")


class _NasRPSUStatus_Type(Integer32):
    """Custom type nasRPSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("fine", 1),
          ("broken", 2))
    )


_NasRPSUStatus_Type.__name__ = "Integer32"
_NasRPSUStatus_Object = MibTableColumn
nasRPSUStatus = _NasRPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 8, 1, 2),
    _NasRPSUStatus_Type()
)
nasRPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasRPSUStatus.setStatus("current")
_NasISCSITable_Object = MibTable
nasISCSITable = _NasISCSITable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 9)
)
if mibBuilder.loadTexts:
    nasISCSITable.setStatus("current")
_NasISCSIEntry_Object = MibTableRow
nasISCSIEntry = _NasISCSIEntry_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 9, 1)
)
nasISCSIEntry.setIndexNames(
    (0, "BUFFALO-NAS-MIB", "nasISCSIIndex"),
)
if mibBuilder.loadTexts:
    nasISCSIEntry.setStatus("current")
_NasISCSIIndex_Type = Integer32
_NasISCSIIndex_Object = MibTableColumn
nasISCSIIndex = _NasISCSIIndex_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 9, 1, 1),
    _NasISCSIIndex_Type()
)
nasISCSIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nasISCSIIndex.setStatus("current")
_NasISCSIName_Type = DisplayString
_NasISCSIName_Object = MibTableColumn
nasISCSIName = _NasISCSIName_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 9, 1, 2),
    _NasISCSIName_Type()
)
nasISCSIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasISCSIName.setStatus("current")


class _NasISCSIStatus_Type(Integer32):
    """Custom type nasISCSIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("connected", 1),
          ("standing-by", 2))
    )


_NasISCSIStatus_Type.__name__ = "Integer32"
_NasISCSIStatus_Object = MibTableColumn
nasISCSIStatus = _NasISCSIStatus_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 9, 1, 3),
    _NasISCSIStatus_Type()
)
nasISCSIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasISCSIStatus.setStatus("current")
_NasSystemInformation_ObjectIdentity = ObjectIdentity
nasSystemInformation = _NasSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 10)
)


class _NasProductName_Type(OctetString):
    """Custom type nasProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NasProductName_Type.__name__ = "OctetString"
_NasProductName_Object = MibScalar
nasProductName = _NasProductName_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 10, 1),
    _NasProductName_Type()
)
nasProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasProductName.setStatus("current")


class _NasSerialNumber_Type(OctetString):
    """Custom type nasSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NasSerialNumber_Type.__name__ = "OctetString"
_NasSerialNumber_Object = MibScalar
nasSerialNumber = _NasSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 10, 2),
    _NasSerialNumber_Type()
)
nasSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasSerialNumber.setStatus("current")


class _NasFWVersionMajor_Type(OctetString):
    """Custom type nasFWVersionMajor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NasFWVersionMajor_Type.__name__ = "OctetString"
_NasFWVersionMajor_Object = MibScalar
nasFWVersionMajor = _NasFWVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 10, 3),
    _NasFWVersionMajor_Type()
)
nasFWVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasFWVersionMajor.setStatus("current")


class _NasFWVersionMinor_Type(OctetString):
    """Custom type nasFWVersionMinor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NasFWVersionMinor_Type.__name__ = "OctetString"
_NasFWVersionMinor_Object = MibScalar
nasFWVersionMinor = _NasFWVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 10, 4),
    _NasFWVersionMinor_Type()
)
nasFWVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasFWVersionMinor.setStatus("current")


class _NasIsFWUpdateAvailable_Type(Integer32):
    """Custom type nasIsFWUpdateAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("available", 1),
          ("unavailable", 2),
          ("latest", 3))
    )


_NasIsFWUpdateAvailable_Type.__name__ = "Integer32"
_NasIsFWUpdateAvailable_Object = MibScalar
nasIsFWUpdateAvailable = _NasIsFWUpdateAvailable_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 10, 5),
    _NasIsFWUpdateAvailable_Type()
)
nasIsFWUpdateAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasIsFWUpdateAvailable.setStatus("current")
_NasSystemDateAndTime_Type = DateAndTime
_NasSystemDateAndTime_Object = MibScalar
nasSystemDateAndTime = _NasSystemDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 10, 6),
    _NasSystemDateAndTime_Type()
)
nasSystemDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasSystemDateAndTime.setStatus("current")
_NasServiceStatus_ObjectIdentity = ObjectIdentity
nasServiceStatus = _NasServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11)
)


class _NasServiceStatusSMB_Type(Integer32):
    """Custom type nasServiceStatusSMB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusSMB_Type.__name__ = "Integer32"
_NasServiceStatusSMB_Object = MibScalar
nasServiceStatusSMB = _NasServiceStatusSMB_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 1),
    _NasServiceStatusSMB_Type()
)
nasServiceStatusSMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusSMB.setStatus("current")


class _NasServiceStatusDFS_Type(Integer32):
    """Custom type nasServiceStatusDFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusDFS_Type.__name__ = "Integer32"
_NasServiceStatusDFS_Object = MibScalar
nasServiceStatusDFS = _NasServiceStatusDFS_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 2),
    _NasServiceStatusDFS_Type()
)
nasServiceStatusDFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusDFS.setStatus("current")


class _NasServiceStatusAFP_Type(Integer32):
    """Custom type nasServiceStatusAFP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusAFP_Type.__name__ = "Integer32"
_NasServiceStatusAFP_Object = MibScalar
nasServiceStatusAFP = _NasServiceStatusAFP_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 3),
    _NasServiceStatusAFP_Type()
)
nasServiceStatusAFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusAFP.setStatus("current")


class _NasServiceStatusFTP_Type(Integer32):
    """Custom type nasServiceStatusFTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusFTP_Type.__name__ = "Integer32"
_NasServiceStatusFTP_Object = MibScalar
nasServiceStatusFTP = _NasServiceStatusFTP_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 4),
    _NasServiceStatusFTP_Type()
)
nasServiceStatusFTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusFTP.setStatus("current")


class _NasServiceStatusSFTP_Type(Integer32):
    """Custom type nasServiceStatusSFTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusSFTP_Type.__name__ = "Integer32"
_NasServiceStatusSFTP_Object = MibScalar
nasServiceStatusSFTP = _NasServiceStatusSFTP_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 5),
    _NasServiceStatusSFTP_Type()
)
nasServiceStatusSFTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusSFTP.setStatus("current")


class _NasServiceStatusWebAxs_Type(Integer32):
    """Custom type nasServiceStatusWebAxs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusWebAxs_Type.__name__ = "Integer32"
_NasServiceStatusWebAxs_Object = MibScalar
nasServiceStatusWebAxs = _NasServiceStatusWebAxs_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 6),
    _NasServiceStatusWebAxs_Type()
)
nasServiceStatusWebAxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusWebAxs.setStatus("current")


class _NasServiceStatusNFS_Type(Integer32):
    """Custom type nasServiceStatusNFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusNFS_Type.__name__ = "Integer32"
_NasServiceStatusNFS_Object = MibScalar
nasServiceStatusNFS = _NasServiceStatusNFS_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 7),
    _NasServiceStatusNFS_Type()
)
nasServiceStatusNFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusNFS.setStatus("current")


class _NasServiceStatusRAIDMaintenance_Type(Integer32):
    """Custom type nasServiceStatusRAIDMaintenance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusRAIDMaintenance_Type.__name__ = "Integer32"
_NasServiceStatusRAIDMaintenance_Object = MibScalar
nasServiceStatusRAIDMaintenance = _NasServiceStatusRAIDMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 8),
    _NasServiceStatusRAIDMaintenance_Type()
)
nasServiceStatusRAIDMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusRAIDMaintenance.setStatus("current")


class _NasServiceStatusiSCSI_Type(Integer32):
    """Custom type nasServiceStatusiSCSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusiSCSI_Type.__name__ = "Integer32"
_NasServiceStatusiSCSI_Object = MibScalar
nasServiceStatusiSCSI = _NasServiceStatusiSCSI_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 9),
    _NasServiceStatusiSCSI_Type()
)
nasServiceStatusiSCSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusiSCSI.setStatus("current")


class _NasServiceStatusDLNAServer_Type(Integer32):
    """Custom type nasServiceStatusDLNAServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusDLNAServer_Type.__name__ = "Integer32"
_NasServiceStatusDLNAServer_Object = MibScalar
nasServiceStatusDLNAServer = _NasServiceStatusDLNAServer_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 10),
    _NasServiceStatusDLNAServer_Type()
)
nasServiceStatusDLNAServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusDLNAServer.setStatus("current")


class _NasServiceStatusiTunesServer_Type(Integer32):
    """Custom type nasServiceStatusiTunesServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusiTunesServer_Type.__name__ = "Integer32"
_NasServiceStatusiTunesServer_Object = MibScalar
nasServiceStatusiTunesServer = _NasServiceStatusiTunesServer_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 11),
    _NasServiceStatusiTunesServer_Type()
)
nasServiceStatusiTunesServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusiTunesServer.setStatus("current")


class _NasServiceStatusSqueezeboxServer_Type(Integer32):
    """Custom type nasServiceStatusSqueezeboxServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusSqueezeboxServer_Type.__name__ = "Integer32"
_NasServiceStatusSqueezeboxServer_Object = MibScalar
nasServiceStatusSqueezeboxServer = _NasServiceStatusSqueezeboxServer_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 12),
    _NasServiceStatusSqueezeboxServer_Type()
)
nasServiceStatusSqueezeboxServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusSqueezeboxServer.setStatus("current")


class _NasServiceStatusPrintServer_Type(Integer32):
    """Custom type nasServiceStatusPrintServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusPrintServer_Type.__name__ = "Integer32"
_NasServiceStatusPrintServer_Object = MibScalar
nasServiceStatusPrintServer = _NasServiceStatusPrintServer_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 13),
    _NasServiceStatusPrintServer_Type()
)
nasServiceStatusPrintServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusPrintServer.setStatus("current")


class _NasServiceStatusWebServer_Type(Integer32):
    """Custom type nasServiceStatusWebServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusWebServer_Type.__name__ = "Integer32"
_NasServiceStatusWebServer_Object = MibScalar
nasServiceStatusWebServer = _NasServiceStatusWebServer_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 14),
    _NasServiceStatusWebServer_Type()
)
nasServiceStatusWebServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusWebServer.setStatus("current")


class _NasServiceStatusMySQLServer_Type(Integer32):
    """Custom type nasServiceStatusMySQLServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusMySQLServer_Type.__name__ = "Integer32"
_NasServiceStatusMySQLServer_Object = MibScalar
nasServiceStatusMySQLServer = _NasServiceStatusMySQLServer_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 15),
    _NasServiceStatusMySQLServer_Type()
)
nasServiceStatusMySQLServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusMySQLServer.setStatus("current")


class _NasServiceStatusWebAxsSync_Type(Integer32):
    """Custom type nasServiceStatusWebAxsSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusWebAxsSync_Type.__name__ = "Integer32"
_NasServiceStatusWebAxsSync_Object = MibScalar
nasServiceStatusWebAxsSync = _NasServiceStatusWebAxsSync_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 16),
    _NasServiceStatusWebAxsSync_Type()
)
nasServiceStatusWebAxsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusWebAxsSync.setStatus("current")


class _NasServiceStatusCloudService_Type(Integer32):
    """Custom type nasServiceStatusCloudService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusCloudService_Type.__name__ = "Integer32"
_NasServiceStatusCloudService_Object = MibScalar
nasServiceStatusCloudService = _NasServiceStatusCloudService_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 17),
    _NasServiceStatusCloudService_Type()
)
nasServiceStatusCloudService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusCloudService.setStatus("current")


class _NasServiceStatusBitTorrent_Type(Integer32):
    """Custom type nasServiceStatusBitTorrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusBitTorrent_Type.__name__ = "Integer32"
_NasServiceStatusBitTorrent_Object = MibScalar
nasServiceStatusBitTorrent = _NasServiceStatusBitTorrent_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 18),
    _NasServiceStatusBitTorrent_Type()
)
nasServiceStatusBitTorrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusBitTorrent.setStatus("current")


class _NasServiceStatusTeraSearch_Type(Integer32):
    """Custom type nasServiceStatusTeraSearch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusTeraSearch_Type.__name__ = "Integer32"
_NasServiceStatusTeraSearch_Object = MibScalar
nasServiceStatusTeraSearch = _NasServiceStatusTeraSearch_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 19),
    _NasServiceStatusTeraSearch_Type()
)
nasServiceStatusTeraSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusTeraSearch.setStatus("current")


class _NasServiceStatusIpCamera_Type(Integer32):
    """Custom type nasServiceStatusIpCamera based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusIpCamera_Type.__name__ = "Integer32"
_NasServiceStatusIpCamera_Object = MibScalar
nasServiceStatusIpCamera = _NasServiceStatusIpCamera_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 20),
    _NasServiceStatusIpCamera_Type()
)
nasServiceStatusIpCamera.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusIpCamera.setStatus("current")


class _NasServiceStatusVirusScan_Type(Integer32):
    """Custom type nasServiceStatusVirusScan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusVirusScan_Type.__name__ = "Integer32"
_NasServiceStatusVirusScan_Object = MibScalar
nasServiceStatusVirusScan = _NasServiceStatusVirusScan_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 21),
    _NasServiceStatusVirusScan_Type()
)
nasServiceStatusVirusScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusVirusScan.setStatus("current")


class _NasServiceStatusSNMP_Type(Integer32):
    """Custom type nasServiceStatusSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusSNMP_Type.__name__ = "Integer32"
_NasServiceStatusSNMP_Object = MibScalar
nasServiceStatusSNMP = _NasServiceStatusSNMP_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 22),
    _NasServiceStatusSNMP_Type()
)
nasServiceStatusSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusSNMP.setStatus("current")


class _NasServiceStatusTimeMachine_Type(Integer32):
    """Custom type nasServiceStatusTimeMachine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusTimeMachine_Type.__name__ = "Integer32"
_NasServiceStatusTimeMachine_Object = MibScalar
nasServiceStatusTimeMachine = _NasServiceStatusTimeMachine_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 23),
    _NasServiceStatusTimeMachine_Type()
)
nasServiceStatusTimeMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusTimeMachine.setStatus("current")


class _NasServiceStatusDirectCopy_Type(Integer32):
    """Custom type nasServiceStatusDirectCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusDirectCopy_Type.__name__ = "Integer32"
_NasServiceStatusDirectCopy_Object = MibScalar
nasServiceStatusDirectCopy = _NasServiceStatusDirectCopy_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 24),
    _NasServiceStatusDirectCopy_Type()
)
nasServiceStatusDirectCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusDirectCopy.setStatus("current")


class _NasServiceStatusMailNotification_Type(Integer32):
    """Custom type nasServiceStatusMailNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusMailNotification_Type.__name__ = "Integer32"
_NasServiceStatusMailNotification_Object = MibScalar
nasServiceStatusMailNotification = _NasServiceStatusMailNotification_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 25),
    _NasServiceStatusMailNotification_Type()
)
nasServiceStatusMailNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusMailNotification.setStatus("current")


class _NasServiceStatusWorkingFolder_Type(Integer32):
    """Custom type nasServiceStatusWorkingFolder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("on", 1),
          ("off", 2))
    )


_NasServiceStatusWorkingFolder_Type.__name__ = "Integer32"
_NasServiceStatusWorkingFolder_Object = MibScalar
nasServiceStatusWorkingFolder = _NasServiceStatusWorkingFolder_Object(
    (1, 3, 6, 1, 4, 1, 5227, 27, 1, 11, 26),
    _NasServiceStatusWorkingFolder_Type()
)
nasServiceStatusWorkingFolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasServiceStatusWorkingFolder.setStatus("current")
_TeraStationNotifications_ObjectIdentity = ObjectIdentity
teraStationNotifications = _TeraStationNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 27, 2)
)

# Managed Objects groups


# Notification objects

nasErrorOccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 5227, 27, 2, 1)
)
nasErrorOccur.setObjects(
      *(("BUFFALO-NAS-MIB", "nasErrorMsg"),
        ("BUFFALO-NAS-MIB", "nasErrorDate"),
        ("BUFFALO-NAS-MIB", "nasErrorDateAndTime"))
)
if mibBuilder.loadTexts:
    nasErrorOccur.setStatus(
        "current"
    )

nasInformationOccur = NotificationType(
    (1, 3, 6, 1, 4, 1, 5227, 27, 2, 2)
)
nasInformationOccur.setObjects(
      *(("BUFFALO-NAS-MIB", "nasInformationMsg"),
        ("BUFFALO-NAS-MIB", "nasInformationDate"),
        ("BUFFALO-NAS-MIB", "nasInformationDateAndTime"))
)
if mibBuilder.loadTexts:
    nasInformationOccur.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BUFFALO-NAS-MIB",
    **{"DayOfWeek": DayOfWeek,
       "LongUTF8String": LongUTF8String,
       "teraStation": teraStation,
       "teraStationObjects": teraStationObjects,
       "nasBackupTable": nasBackupTable,
       "nasBackupEntry": nasBackupEntry,
       "nasBackupIndex": nasBackupIndex,
       "nasBackupStatus": nasBackupStatus,
       "nasDiskTable": nasDiskTable,
       "nasDiskEntry": nasDiskEntry,
       "nasDiskIndex": nasDiskIndex,
       "nasDiskStatus": nasDiskStatus,
       "nasDiskCapacity": nasDiskCapacity,
       "nasDiskUsed": nasDiskUsed,
       "nasDiskSMARTStatus": nasDiskSMARTStatus,
       "nasDiskSMARTReallocatedSectorCtValue": nasDiskSMARTReallocatedSectorCtValue,
       "nasDiskSMARTReallocatedSectorCtWorst": nasDiskSMARTReallocatedSectorCtWorst,
       "nasDiskSMARTReallocatedSectorCtThresh": nasDiskSMARTReallocatedSectorCtThresh,
       "nasDiskSMARTReallocatedSectorCtRAW": nasDiskSMARTReallocatedSectorCtRAW,
       "nasDiskSMARTCurrentPendingSectorValue": nasDiskSMARTCurrentPendingSectorValue,
       "nasDiskSMARTCurrentPendingSectorWorst": nasDiskSMARTCurrentPendingSectorWorst,
       "nasDiskSMARTCurrentPendingSectorThresh": nasDiskSMARTCurrentPendingSectorThresh,
       "nasDiskSMARTCurrentPendingSectorRAW": nasDiskSMARTCurrentPendingSectorRAW,
       "nasDiskSMARTOfflineUncorrectableValue": nasDiskSMARTOfflineUncorrectableValue,
       "nasDiskSMARTOfflineUncorrectableWorst": nasDiskSMARTOfflineUncorrectableWorst,
       "nasDiskSMARTOfflineUncorrectableThresh": nasDiskSMARTOfflineUncorrectableThresh,
       "nasDiskSMARTOfflineUncorrectableRAW": nasDiskSMARTOfflineUncorrectableRAW,
       "nasSSDSMARTRemainingLifeValue": nasSSDSMARTRemainingLifeValue,
       "nasSSDSMARTRemainingLifeWorst": nasSSDSMARTRemainingLifeWorst,
       "nasSSDSMARTRemainingLifeThresh": nasSSDSMARTRemainingLifeThresh,
       "nasSSDSMARTBadBlockCountValue": nasSSDSMARTBadBlockCountValue,
       "nasSSDSMARTBadBlockCountWorst": nasSSDSMARTBadBlockCountWorst,
       "nasSSDSMARTBadBlockCountThresh": nasSSDSMARTBadBlockCountThresh,
       "nasDiskCapacityGiB": nasDiskCapacityGiB,
       "nasDiskCapacityLow": nasDiskCapacityLow,
       "nasDiskCapacityHigh": nasDiskCapacityHigh,
       "nasDiskUsedGiB": nasDiskUsedGiB,
       "nasDiskUsedLow": nasDiskUsedLow,
       "nasDiskUsedHigh": nasDiskUsedHigh,
       "nasDiskModelName": nasDiskModelName,
       "nasDiskSMARTReallocatedSectorCtHealth": nasDiskSMARTReallocatedSectorCtHealth,
       "nasDiskSMARTCurrentPendingSectorHealth": nasDiskSMARTCurrentPendingSectorHealth,
       "nasDiskSMARTOfflineUncorrectableHealth": nasDiskSMARTOfflineUncorrectableHealth,
       "nasDiskSMARTRawReadErrorRateValue": nasDiskSMARTRawReadErrorRateValue,
       "nasDiskSMARTRawReadErrorRateWorst": nasDiskSMARTRawReadErrorRateWorst,
       "nasDiskSMARTRawReadErrorRateThresh": nasDiskSMARTRawReadErrorRateThresh,
       "nasDiskSMARTRawReadErrorRateRAW": nasDiskSMARTRawReadErrorRateRAW,
       "nasDiskSMARTRawReadErrorRateHealth": nasDiskSMARTRawReadErrorRateHealth,
       "nasDiskSMARTPowerOnHoursValue": nasDiskSMARTPowerOnHoursValue,
       "nasDiskSMARTPowerOnHoursWorst": nasDiskSMARTPowerOnHoursWorst,
       "nasDiskSMARTPowerOnHoursThresh": nasDiskSMARTPowerOnHoursThresh,
       "nasDiskSMARTPowerOnHoursRAW": nasDiskSMARTPowerOnHoursRAW,
       "nasDiskSMARTPowerOnHoursHealth": nasDiskSMARTPowerOnHoursHealth,
       "nasArrayTable": nasArrayTable,
       "nasArrayEntry": nasArrayEntry,
       "nasArrayIndex": nasArrayIndex,
       "nasArrayStatus": nasArrayStatus,
       "nasArrayCapacity": nasArrayCapacity,
       "nasArrayUsed": nasArrayUsed,
       "nasArrayCapacityGiB": nasArrayCapacityGiB,
       "nasArrayCapacityLow": nasArrayCapacityLow,
       "nasArrayCapacityHigh": nasArrayCapacityHigh,
       "nasArrayUsedGiB": nasArrayUsedGiB,
       "nasArrayUsedLow": nasArrayUsedLow,
       "nasArrayUsedHigh": nasArrayUsedHigh,
       "nasErrorTable": nasErrorTable,
       "nasErrorEntry": nasErrorEntry,
       "nasErrorIndex": nasErrorIndex,
       "nasErrorMsg": nasErrorMsg,
       "nasErrorDate": nasErrorDate,
       "nasErrorDateAndTime": nasErrorDateAndTime,
       "nasInformationTable": nasInformationTable,
       "nasInformationEntry": nasInformationEntry,
       "nasInformationIndex": nasInformationIndex,
       "nasInformationMsg": nasInformationMsg,
       "nasInformationDate": nasInformationDate,
       "nasInformationDateAndTime": nasInformationDateAndTime,
       "nasLVMParams": nasLVMParams,
       "nasVGTable": nasVGTable,
       "nasVGEntry": nasVGEntry,
       "nasVGIndex": nasVGIndex,
       "nasVGPESize": nasVGPESize,
       "nasVGPETotal": nasVGPETotal,
       "nasVGPEUsed": nasVGPEUsed,
       "nasLVTable": nasLVTable,
       "nasLVEntry": nasLVEntry,
       "nasLVIndex": nasLVIndex,
       "nasLVName": nasLVName,
       "nasLVCapacity": nasLVCapacity,
       "nasLVUsed": nasLVUsed,
       "nasLVCapacityGiB": nasLVCapacityGiB,
       "nasLVCapacityLow": nasLVCapacityLow,
       "nasLVCapacityHigh": nasLVCapacityHigh,
       "nasLVUsedGiB": nasLVUsedGiB,
       "nasLVUsedLow": nasLVUsedLow,
       "nasLVUsedHigh": nasLVUsedHigh,
       "nasPVTable": nasPVTable,
       "nasPVEntry": nasPVEntry,
       "nasPVIndex": nasPVIndex,
       "nasPVName": nasPVName,
       "nasFailoverParams": nasFailoverParams,
       "nasFailoverRole": nasFailoverRole,
       "nasFailoverStatus": nasFailoverStatus,
       "nasFailoverPartner": nasFailoverPartner,
       "nasRPSUTable": nasRPSUTable,
       "nasRPSUEntry": nasRPSUEntry,
       "nasRPSUIndex": nasRPSUIndex,
       "nasRPSUStatus": nasRPSUStatus,
       "nasISCSITable": nasISCSITable,
       "nasISCSIEntry": nasISCSIEntry,
       "nasISCSIIndex": nasISCSIIndex,
       "nasISCSIName": nasISCSIName,
       "nasISCSIStatus": nasISCSIStatus,
       "nasSystemInformation": nasSystemInformation,
       "nasProductName": nasProductName,
       "nasSerialNumber": nasSerialNumber,
       "nasFWVersionMajor": nasFWVersionMajor,
       "nasFWVersionMinor": nasFWVersionMinor,
       "nasIsFWUpdateAvailable": nasIsFWUpdateAvailable,
       "nasSystemDateAndTime": nasSystemDateAndTime,
       "nasServiceStatus": nasServiceStatus,
       "nasServiceStatusSMB": nasServiceStatusSMB,
       "nasServiceStatusDFS": nasServiceStatusDFS,
       "nasServiceStatusAFP": nasServiceStatusAFP,
       "nasServiceStatusFTP": nasServiceStatusFTP,
       "nasServiceStatusSFTP": nasServiceStatusSFTP,
       "nasServiceStatusWebAxs": nasServiceStatusWebAxs,
       "nasServiceStatusNFS": nasServiceStatusNFS,
       "nasServiceStatusRAIDMaintenance": nasServiceStatusRAIDMaintenance,
       "nasServiceStatusiSCSI": nasServiceStatusiSCSI,
       "nasServiceStatusDLNAServer": nasServiceStatusDLNAServer,
       "nasServiceStatusiTunesServer": nasServiceStatusiTunesServer,
       "nasServiceStatusSqueezeboxServer": nasServiceStatusSqueezeboxServer,
       "nasServiceStatusPrintServer": nasServiceStatusPrintServer,
       "nasServiceStatusWebServer": nasServiceStatusWebServer,
       "nasServiceStatusMySQLServer": nasServiceStatusMySQLServer,
       "nasServiceStatusWebAxsSync": nasServiceStatusWebAxsSync,
       "nasServiceStatusCloudService": nasServiceStatusCloudService,
       "nasServiceStatusBitTorrent": nasServiceStatusBitTorrent,
       "nasServiceStatusTeraSearch": nasServiceStatusTeraSearch,
       "nasServiceStatusIpCamera": nasServiceStatusIpCamera,
       "nasServiceStatusVirusScan": nasServiceStatusVirusScan,
       "nasServiceStatusSNMP": nasServiceStatusSNMP,
       "nasServiceStatusTimeMachine": nasServiceStatusTimeMachine,
       "nasServiceStatusDirectCopy": nasServiceStatusDirectCopy,
       "nasServiceStatusMailNotification": nasServiceStatusMailNotification,
       "nasServiceStatusWorkingFolder": nasServiceStatusWorkingFolder,
       "teraStationNotifications": teraStationNotifications,
       "nasErrorOccur": nasErrorOccur,
       "nasInformationOccur": nasInformationOccur}
)
