# SNMP MIB module (ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:01 2025
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

(adGenPortInfoIndex,
 adGenPortTrapIdentifier) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortInfoIndex",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenTa5kDs3,
 adGenTa5kDs3ID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kDs3",
    "adGenTa5kDs3ID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adIdentity,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adMgmt",
    "adProducts")

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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adTa5kDs3PMThresholdModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 21, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTA5kds3TrapsPrefix_ObjectIdentity = ObjectIdentity
adTA5kds3TrapsPrefix = _AdTA5kds3TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1)
)
_AdTA5kds3Traps_ObjectIdentity = ObjectIdentity
adTA5kds3Traps = _AdTA5kds3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0)
)
_AdTA5kds3PMThreshold_ObjectIdentity = ObjectIdentity
adTA5kds3PMThreshold = _AdTA5kds3PMThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2)
)
_AdTa5kDS3PMqtrThresholdTable_Object = MibTable
adTa5kDS3PMqtrThresholdTable = _AdTa5kDS3PMqtrThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1)
)
if mibBuilder.loadTexts:
    adTa5kDS3PMqtrThresholdTable.setStatus("current")
_AdTa5kDS3PMqtrThresholdEntry_Object = MibTableRow
adTa5kDS3PMqtrThresholdEntry = _AdTa5kDS3PMqtrThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1)
)
adTa5kDS3PMqtrThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kDS3PMqtrThresholdEntry.setStatus("current")
_AdTa5kDs3PMqtrThresholdPESs_Type = Integer32
_AdTa5kDs3PMqtrThresholdPESs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdPESs = _AdTa5kDs3PMqtrThresholdPESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 1),
    _AdTa5kDs3PMqtrThresholdPESs_Type()
)
adTa5kDs3PMqtrThresholdPESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdPESs.setStatus("current")
_AdTa5kDs3PMqtrThresholdPSESs_Type = Integer32
_AdTa5kDs3PMqtrThresholdPSESs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdPSESs = _AdTa5kDs3PMqtrThresholdPSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 2),
    _AdTa5kDs3PMqtrThresholdPSESs_Type()
)
adTa5kDs3PMqtrThresholdPSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdPSESs.setStatus("current")
_AdTa5kDs3PMqtrThresholdSEFSs_Type = Integer32
_AdTa5kDs3PMqtrThresholdSEFSs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdSEFSs = _AdTa5kDs3PMqtrThresholdSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 3),
    _AdTa5kDs3PMqtrThresholdSEFSs_Type()
)
adTa5kDs3PMqtrThresholdSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdSEFSs.setStatus("current")
_AdTa5kDs3PMqtrThresholdUASs_Type = Integer32
_AdTa5kDs3PMqtrThresholdUASs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdUASs = _AdTa5kDs3PMqtrThresholdUASs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 4),
    _AdTa5kDs3PMqtrThresholdUASs_Type()
)
adTa5kDs3PMqtrThresholdUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdUASs.setStatus("current")
_AdTa5kDs3PMqtrThresholdLCVs_Type = Integer32
_AdTa5kDs3PMqtrThresholdLCVs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdLCVs = _AdTa5kDs3PMqtrThresholdLCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 5),
    _AdTa5kDs3PMqtrThresholdLCVs_Type()
)
adTa5kDs3PMqtrThresholdLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdLCVs.setStatus("current")
_AdTa5kDs3PMqtrThresholdPCVs_Type = Integer32
_AdTa5kDs3PMqtrThresholdPCVs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdPCVs = _AdTa5kDs3PMqtrThresholdPCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 6),
    _AdTa5kDs3PMqtrThresholdPCVs_Type()
)
adTa5kDs3PMqtrThresholdPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdPCVs.setStatus("current")
_AdTa5kDs3PMqtrThresholdLESs_Type = Integer32
_AdTa5kDs3PMqtrThresholdLESs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdLESs = _AdTa5kDs3PMqtrThresholdLESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 7),
    _AdTa5kDs3PMqtrThresholdLESs_Type()
)
adTa5kDs3PMqtrThresholdLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdLESs.setStatus("current")
_AdTa5kDs3PMqtrThresholdCCVs_Type = Integer32
_AdTa5kDs3PMqtrThresholdCCVs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdCCVs = _AdTa5kDs3PMqtrThresholdCCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 8),
    _AdTa5kDs3PMqtrThresholdCCVs_Type()
)
adTa5kDs3PMqtrThresholdCCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdCCVs.setStatus("current")
_AdTa5kDs3PMqtrThresholdCESs_Type = Integer32
_AdTa5kDs3PMqtrThresholdCESs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdCESs = _AdTa5kDs3PMqtrThresholdCESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 9),
    _AdTa5kDs3PMqtrThresholdCESs_Type()
)
adTa5kDs3PMqtrThresholdCESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdCESs.setStatus("current")
_AdTa5kDs3PMqtrThresholdCSESs_Type = Integer32
_AdTa5kDs3PMqtrThresholdCSESs_Object = MibTableColumn
adTa5kDs3PMqtrThresholdCSESs = _AdTa5kDs3PMqtrThresholdCSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 1, 1, 10),
    _AdTa5kDs3PMqtrThresholdCSESs_Type()
)
adTa5kDs3PMqtrThresholdCSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMqtrThresholdCSESs.setStatus("current")
_AdTa5kDs3PMDayThresholdTable_Object = MibTable
adTa5kDs3PMDayThresholdTable = _AdTa5kDs3PMDayThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2)
)
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdTable.setStatus("current")
_AdTa5kDs3PMDayThresholdEntry_Object = MibTableRow
adTa5kDs3PMDayThresholdEntry = _AdTa5kDs3PMDayThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1)
)
adTa5kDs3PMDayThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdEntry.setStatus("current")
_AdTa5kDs3PMDayThresholdPES_Type = Integer32
_AdTa5kDs3PMDayThresholdPES_Object = MibTableColumn
adTa5kDs3PMDayThresholdPES = _AdTa5kDs3PMDayThresholdPES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 1),
    _AdTa5kDs3PMDayThresholdPES_Type()
)
adTa5kDs3PMDayThresholdPES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdPES.setStatus("current")
_AdTa5kDs3PMDayThresholdPSES_Type = Integer32
_AdTa5kDs3PMDayThresholdPSES_Object = MibTableColumn
adTa5kDs3PMDayThresholdPSES = _AdTa5kDs3PMDayThresholdPSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 2),
    _AdTa5kDs3PMDayThresholdPSES_Type()
)
adTa5kDs3PMDayThresholdPSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdPSES.setStatus("current")
_AdTa5kDs3PMDayThresholdSEFS_Type = Integer32
_AdTa5kDs3PMDayThresholdSEFS_Object = MibTableColumn
adTa5kDs3PMDayThresholdSEFS = _AdTa5kDs3PMDayThresholdSEFS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 3),
    _AdTa5kDs3PMDayThresholdSEFS_Type()
)
adTa5kDs3PMDayThresholdSEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdSEFS.setStatus("current")
_AdTa5kDs3PMDayThresholdUAS_Type = Integer32
_AdTa5kDs3PMDayThresholdUAS_Object = MibTableColumn
adTa5kDs3PMDayThresholdUAS = _AdTa5kDs3PMDayThresholdUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 4),
    _AdTa5kDs3PMDayThresholdUAS_Type()
)
adTa5kDs3PMDayThresholdUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdUAS.setStatus("current")
_AdTa5kDs3PMDayThresholdLCV_Type = Integer32
_AdTa5kDs3PMDayThresholdLCV_Object = MibTableColumn
adTa5kDs3PMDayThresholdLCV = _AdTa5kDs3PMDayThresholdLCV_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 5),
    _AdTa5kDs3PMDayThresholdLCV_Type()
)
adTa5kDs3PMDayThresholdLCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdLCV.setStatus("current")
_AdTa5kDs3PMDayThresholdPCV_Type = Integer32
_AdTa5kDs3PMDayThresholdPCV_Object = MibTableColumn
adTa5kDs3PMDayThresholdPCV = _AdTa5kDs3PMDayThresholdPCV_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 6),
    _AdTa5kDs3PMDayThresholdPCV_Type()
)
adTa5kDs3PMDayThresholdPCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdPCV.setStatus("current")
_AdTa5kDs3PMDayThresholdLES_Type = Integer32
_AdTa5kDs3PMDayThresholdLES_Object = MibTableColumn
adTa5kDs3PMDayThresholdLES = _AdTa5kDs3PMDayThresholdLES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 7),
    _AdTa5kDs3PMDayThresholdLES_Type()
)
adTa5kDs3PMDayThresholdLES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdLES.setStatus("current")
_AdTa5kDs3PMDayThresholdCCV_Type = Integer32
_AdTa5kDs3PMDayThresholdCCV_Object = MibTableColumn
adTa5kDs3PMDayThresholdCCV = _AdTa5kDs3PMDayThresholdCCV_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 8),
    _AdTa5kDs3PMDayThresholdCCV_Type()
)
adTa5kDs3PMDayThresholdCCV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdCCV.setStatus("current")
_AdTa5kDs3PMDayThresholdCES_Type = Integer32
_AdTa5kDs3PMDayThresholdCES_Object = MibTableColumn
adTa5kDs3PMDayThresholdCES = _AdTa5kDs3PMDayThresholdCES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 9),
    _AdTa5kDs3PMDayThresholdCES_Type()
)
adTa5kDs3PMDayThresholdCES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdCES.setStatus("current")
_AdTa5kDs3PMDayThresholdCSES_Type = Integer32
_AdTa5kDs3PMDayThresholdCSES_Object = MibTableColumn
adTa5kDs3PMDayThresholdCSES = _AdTa5kDs3PMDayThresholdCSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 2, 2, 1, 10),
    _AdTa5kDs3PMDayThresholdCSES_Type()
)
adTa5kDs3PMDayThresholdCSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayThresholdCSES.setStatus("current")
_AdTA5kds3MibConformance_ObjectIdentity = ObjectIdentity
adTA5kds3MibConformance = _AdTA5kds3MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 3)
)
_AdTA5kds3MibGroups_ObjectIdentity = ObjectIdentity
adTA5kds3MibGroups = _AdTA5kds3MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 3, 1)
)

# Managed Objects groups

adTa5kDS3PMqtrThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 3, 1, 1)
)
adTa5kDS3PMqtrThresholdGroup.setObjects(
      *(("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdPESs"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdPSESs"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdSEFSs"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdUASs"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdLCVs"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdPCVs"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdLESs"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdCCVs"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdCESs"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMqtrThresholdCSESs"))
)
if mibBuilder.loadTexts:
    adTa5kDS3PMqtrThresholdGroup.setStatus("current")

adTa5kDS3PMdayThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 3, 1, 2)
)
adTa5kDS3PMdayThresholdGroup.setObjects(
      *(("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdPES"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdPSES"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdSEFS"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdUAS"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdLCV"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdPCV"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdLES"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdCCV"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdCES"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTa5kDs3PMDayThresholdCSES"))
)
if mibBuilder.loadTexts:
    adTa5kDS3PMdayThresholdGroup.setStatus("current")


# Notification objects

adTA5kds3LOSTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 1)
)
adTA5kds3LOSTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kds3LOSTrapActive.setStatus(
        "current"
    )

adTA5kds3LOSTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 2)
)
adTA5kds3LOSTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kds3LOSTrapClear.setStatus(
        "current"
    )

adTA5kds3LOFTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 3)
)
adTA5kds3LOFTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kds3LOFTrapActive.setStatus(
        "current"
    )

adTA5kds3LOFTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 4)
)
adTA5kds3LOFTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kds3LOFTrapClear.setStatus(
        "current"
    )

adTA5kds3RAITrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 5)
)
adTA5kds3RAITrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kds3RAITrapActive.setStatus(
        "current"
    )

adTA5kds3RAITrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 6)
)
adTA5kds3RAITrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kds3RAITrapClear.setStatus(
        "current"
    )

adTA5kds3AISTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 7)
)
adTA5kds3AISTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kds3AISTrapActive.setStatus(
        "current"
    )

adTA5kds3AISTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 8)
)
adTA5kds3AISTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adTA5kds3AISTrapClear.setStatus(
        "current"
    )

adTA5kds3almQtrPESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 9)
)
adTA5kds3almQtrPESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrPESThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3almQtrPSESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 10)
)
adTA5kds3almQtrPSESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrPSESThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3almQtrSEFSThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 11)
)
adTA5kds3almQtrSEFSThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrSEFSThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3almQtrUASThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 12)
)
adTA5kds3almQtrUASThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrUASThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3almQtrLCVThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 13)
)
adTA5kds3almQtrLCVThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrLCVThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3almQtrPCVThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 14)
)
adTA5kds3almQtrPCVThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrPCVThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3almQtrLESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 15)
)
adTA5kds3almQtrLESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrLESThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3almQtrCCVThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 16)
)
adTA5kds3almQtrCCVThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrCCVThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3almQtrCESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 17)
)
adTA5kds3almQtrCESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrCESThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3almQtrCSESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 18)
)
adTA5kds3almQtrCSESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3almQtrCSESThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDayPESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 19)
)
adTA5kds3PMDayPESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDayPESThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDayPSESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 20)
)
adTA5kds3PMDayPSESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDayPSESThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDaySEFSThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 21)
)
adTA5kds3PMDaySEFSThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDaySEFSThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDayUASThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 22)
)
adTA5kds3PMDayUASThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDayUASThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDayLCVThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 23)
)
adTA5kds3PMDayLCVThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDayLCVThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDayPCVThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 24)
)
adTA5kds3PMDayPCVThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDayPCVThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDayLESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 25)
)
adTA5kds3PMDayLESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDayLESThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDayCCVThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 26)
)
adTA5kds3PMDayCCVThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDayCCVThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDayCESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 27)
)
adTA5kds3PMDayCESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDayCESThresholdCrossed.setStatus(
        "current"
    )

adTA5kds3PMDayCSESThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 1, 0, 28)
)
adTA5kds3PMDayCSESThresholdCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTA5kds3PMDayCSESThresholdCrossed.setStatus(
        "current"
    )


# Notifications groups

adTa5kDS3EventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 21, 3, 1, 3)
)
adTa5kDS3EventGroup.setObjects(
      *(("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3LOSTrapActive"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3LOSTrapClear"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3LOFTrapActive"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3LOFTrapClear"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3RAITrapActive"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3RAITrapClear"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3AISTrapActive"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3AISTrapClear"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrPESThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrPSESThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrSEFSThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrUASThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrLCVThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrPCVThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrLESThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrCCVThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrCESThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3almQtrCSESThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDayPESThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDayPSESThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDaySEFSThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDayUASThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDayLCVThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDayPCVThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDayLESThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDayCCVThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDayCESThresholdCrossed"),
        ("ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB", "adTA5kds3PMDayCSESThresholdCrossed"))
)
if mibBuilder.loadTexts:
    adTa5kDS3EventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-DS3-PM-THRESHOLD-MIB",
    **{"adTA5kds3TrapsPrefix": adTA5kds3TrapsPrefix,
       "adTA5kds3Traps": adTA5kds3Traps,
       "adTA5kds3LOSTrapActive": adTA5kds3LOSTrapActive,
       "adTA5kds3LOSTrapClear": adTA5kds3LOSTrapClear,
       "adTA5kds3LOFTrapActive": adTA5kds3LOFTrapActive,
       "adTA5kds3LOFTrapClear": adTA5kds3LOFTrapClear,
       "adTA5kds3RAITrapActive": adTA5kds3RAITrapActive,
       "adTA5kds3RAITrapClear": adTA5kds3RAITrapClear,
       "adTA5kds3AISTrapActive": adTA5kds3AISTrapActive,
       "adTA5kds3AISTrapClear": adTA5kds3AISTrapClear,
       "adTA5kds3almQtrPESThresholdCrossed": adTA5kds3almQtrPESThresholdCrossed,
       "adTA5kds3almQtrPSESThresholdCrossed": adTA5kds3almQtrPSESThresholdCrossed,
       "adTA5kds3almQtrSEFSThresholdCrossed": adTA5kds3almQtrSEFSThresholdCrossed,
       "adTA5kds3almQtrUASThresholdCrossed": adTA5kds3almQtrUASThresholdCrossed,
       "adTA5kds3almQtrLCVThresholdCrossed": adTA5kds3almQtrLCVThresholdCrossed,
       "adTA5kds3almQtrPCVThresholdCrossed": adTA5kds3almQtrPCVThresholdCrossed,
       "adTA5kds3almQtrLESThresholdCrossed": adTA5kds3almQtrLESThresholdCrossed,
       "adTA5kds3almQtrCCVThresholdCrossed": adTA5kds3almQtrCCVThresholdCrossed,
       "adTA5kds3almQtrCESThresholdCrossed": adTA5kds3almQtrCESThresholdCrossed,
       "adTA5kds3almQtrCSESThresholdCrossed": adTA5kds3almQtrCSESThresholdCrossed,
       "adTA5kds3PMDayPESThresholdCrossed": adTA5kds3PMDayPESThresholdCrossed,
       "adTA5kds3PMDayPSESThresholdCrossed": adTA5kds3PMDayPSESThresholdCrossed,
       "adTA5kds3PMDaySEFSThresholdCrossed": adTA5kds3PMDaySEFSThresholdCrossed,
       "adTA5kds3PMDayUASThresholdCrossed": adTA5kds3PMDayUASThresholdCrossed,
       "adTA5kds3PMDayLCVThresholdCrossed": adTA5kds3PMDayLCVThresholdCrossed,
       "adTA5kds3PMDayPCVThresholdCrossed": adTA5kds3PMDayPCVThresholdCrossed,
       "adTA5kds3PMDayLESThresholdCrossed": adTA5kds3PMDayLESThresholdCrossed,
       "adTA5kds3PMDayCCVThresholdCrossed": adTA5kds3PMDayCCVThresholdCrossed,
       "adTA5kds3PMDayCESThresholdCrossed": adTA5kds3PMDayCESThresholdCrossed,
       "adTA5kds3PMDayCSESThresholdCrossed": adTA5kds3PMDayCSESThresholdCrossed,
       "adTA5kds3PMThreshold": adTA5kds3PMThreshold,
       "adTa5kDS3PMqtrThresholdTable": adTa5kDS3PMqtrThresholdTable,
       "adTa5kDS3PMqtrThresholdEntry": adTa5kDS3PMqtrThresholdEntry,
       "adTa5kDs3PMqtrThresholdPESs": adTa5kDs3PMqtrThresholdPESs,
       "adTa5kDs3PMqtrThresholdPSESs": adTa5kDs3PMqtrThresholdPSESs,
       "adTa5kDs3PMqtrThresholdSEFSs": adTa5kDs3PMqtrThresholdSEFSs,
       "adTa5kDs3PMqtrThresholdUASs": adTa5kDs3PMqtrThresholdUASs,
       "adTa5kDs3PMqtrThresholdLCVs": adTa5kDs3PMqtrThresholdLCVs,
       "adTa5kDs3PMqtrThresholdPCVs": adTa5kDs3PMqtrThresholdPCVs,
       "adTa5kDs3PMqtrThresholdLESs": adTa5kDs3PMqtrThresholdLESs,
       "adTa5kDs3PMqtrThresholdCCVs": adTa5kDs3PMqtrThresholdCCVs,
       "adTa5kDs3PMqtrThresholdCESs": adTa5kDs3PMqtrThresholdCESs,
       "adTa5kDs3PMqtrThresholdCSESs": adTa5kDs3PMqtrThresholdCSESs,
       "adTa5kDs3PMDayThresholdTable": adTa5kDs3PMDayThresholdTable,
       "adTa5kDs3PMDayThresholdEntry": adTa5kDs3PMDayThresholdEntry,
       "adTa5kDs3PMDayThresholdPES": adTa5kDs3PMDayThresholdPES,
       "adTa5kDs3PMDayThresholdPSES": adTa5kDs3PMDayThresholdPSES,
       "adTa5kDs3PMDayThresholdSEFS": adTa5kDs3PMDayThresholdSEFS,
       "adTa5kDs3PMDayThresholdUAS": adTa5kDs3PMDayThresholdUAS,
       "adTa5kDs3PMDayThresholdLCV": adTa5kDs3PMDayThresholdLCV,
       "adTa5kDs3PMDayThresholdPCV": adTa5kDs3PMDayThresholdPCV,
       "adTa5kDs3PMDayThresholdLES": adTa5kDs3PMDayThresholdLES,
       "adTa5kDs3PMDayThresholdCCV": adTa5kDs3PMDayThresholdCCV,
       "adTa5kDs3PMDayThresholdCES": adTa5kDs3PMDayThresholdCES,
       "adTa5kDs3PMDayThresholdCSES": adTa5kDs3PMDayThresholdCSES,
       "adTA5kds3MibConformance": adTA5kds3MibConformance,
       "adTA5kds3MibGroups": adTA5kds3MibGroups,
       "adTa5kDS3PMqtrThresholdGroup": adTa5kDS3PMqtrThresholdGroup,
       "adTa5kDS3PMdayThresholdGroup": adTa5kDS3PMdayThresholdGroup,
       "adTa5kDS3EventGroup": adTa5kDS3EventGroup,
       "adTa5kDs3PMThresholdModuleIdentity": adTa5kDs3PMThresholdModuleIdentity}
)
