# SNMP MIB module (ADTRAN-TA5K-TLV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-TLV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:23 2025
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

(adGenPortInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortInfoIndex")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenTa5kTlv,
 adGenTa5kTlvID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kTlv",
    "adGenTa5kTlvID")

(adIdentity,
 adIdentityShared,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adIdentityShared",
    "adMgmt",
    "adProducts")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

adTa5kTlvModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 5, 1)
)
if mibBuilder.loadTexts:
    adTa5kTlvModuleIdentity.setRevisions(
        ("2012-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kTlvCountTable_Object = MibTable
adTa5kTlvCountTable = _AdTa5kTlvCountTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 1)
)
if mibBuilder.loadTexts:
    adTa5kTlvCountTable.setStatus("current")
_AdTa5kTlvCountEntry_Object = MibTableRow
adTa5kTlvCountEntry = _AdTa5kTlvCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 1, 1)
)
adTa5kTlvCountEntry.setIndexNames(
    (0, "ADTRAN-TA5K-TLV-MIB", "adTa5kTlvInstance"),
)
if mibBuilder.loadTexts:
    adTa5kTlvCountEntry.setStatus("current")
_AdTa5kTlvCount_Type = Integer32
_AdTa5kTlvCount_Object = MibTableColumn
adTa5kTlvCount = _AdTa5kTlvCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 1, 1, 1),
    _AdTa5kTlvCount_Type()
)
adTa5kTlvCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kTlvCount.setStatus("current")
_AdTa5kTlvInstance_Type = Integer32
_AdTa5kTlvInstance_Object = MibTableColumn
adTa5kTlvInstance = _AdTa5kTlvInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 1, 1, 2),
    _AdTa5kTlvInstance_Type()
)
adTa5kTlvInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTa5kTlvInstance.setStatus("current")
_AdTa5kTlvDelete_Type = Integer32
_AdTa5kTlvDelete_Object = MibTableColumn
adTa5kTlvDelete = _AdTa5kTlvDelete_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 1, 1, 3),
    _AdTa5kTlvDelete_Type()
)
adTa5kTlvDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kTlvDelete.setStatus("current")
_AdTa5kTlvTable_Object = MibTable
adTa5kTlvTable = _AdTa5kTlvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 2)
)
if mibBuilder.loadTexts:
    adTa5kTlvTable.setStatus("current")
_AdTa5kTlvEntry_Object = MibTableRow
adTa5kTlvEntry = _AdTa5kTlvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 2, 1)
)
adTa5kTlvEntry.setIndexNames(
    (0, "ADTRAN-TA5K-TLV-MIB", "adTa5kTlvInstance"),
    (0, "ADTRAN-TA5K-TLV-MIB", "adTa5kTlvSequence"),
)
if mibBuilder.loadTexts:
    adTa5kTlvEntry.setStatus("current")
_AdTa5kTlvBulk_Type = OctetString
_AdTa5kTlvBulk_Object = MibTableColumn
adTa5kTlvBulk = _AdTa5kTlvBulk_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 2, 1, 1),
    _AdTa5kTlvBulk_Type()
)
adTa5kTlvBulk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kTlvBulk.setStatus("current")
_AdTa5kTlvSequence_Type = Integer32
_AdTa5kTlvSequence_Object = MibTableColumn
adTa5kTlvSequence = _AdTa5kTlvSequence_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 2, 1, 2),
    _AdTa5kTlvSequence_Type()
)
adTa5kTlvSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTa5kTlvSequence.setStatus("current")
_AdTa5kTlvBySlotCountTable_Object = MibTable
adTa5kTlvBySlotCountTable = _AdTa5kTlvBySlotCountTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 3)
)
if mibBuilder.loadTexts:
    adTa5kTlvBySlotCountTable.setStatus("current")
_AdTa5kTlvBySlotCountEntry_Object = MibTableRow
adTa5kTlvBySlotCountEntry = _AdTa5kTlvBySlotCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 3, 1)
)
adTa5kTlvBySlotCountEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-TA5K-TLV-MIB", "adTa5kTlvBySlotInstance"),
)
if mibBuilder.loadTexts:
    adTa5kTlvBySlotCountEntry.setStatus("current")
_AdTa5kTlvBySlotCount_Type = Integer32
_AdTa5kTlvBySlotCount_Object = MibTableColumn
adTa5kTlvBySlotCount = _AdTa5kTlvBySlotCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 3, 1, 1),
    _AdTa5kTlvBySlotCount_Type()
)
adTa5kTlvBySlotCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kTlvBySlotCount.setStatus("current")
_AdTa5kTlvBySlotInstance_Type = Integer32
_AdTa5kTlvBySlotInstance_Object = MibTableColumn
adTa5kTlvBySlotInstance = _AdTa5kTlvBySlotInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 3, 1, 2),
    _AdTa5kTlvBySlotInstance_Type()
)
adTa5kTlvBySlotInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTa5kTlvBySlotInstance.setStatus("current")
_AdTa5kTlvBySlotDelete_Type = Integer32
_AdTa5kTlvBySlotDelete_Object = MibTableColumn
adTa5kTlvBySlotDelete = _AdTa5kTlvBySlotDelete_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 3, 1, 3),
    _AdTa5kTlvBySlotDelete_Type()
)
adTa5kTlvBySlotDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kTlvBySlotDelete.setStatus("current")
_AdTa5kTlvBySlotTable_Object = MibTable
adTa5kTlvBySlotTable = _AdTa5kTlvBySlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 4)
)
if mibBuilder.loadTexts:
    adTa5kTlvBySlotTable.setStatus("current")
_AdTa5kTlvBySlotEntry_Object = MibTableRow
adTa5kTlvBySlotEntry = _AdTa5kTlvBySlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 4, 1)
)
adTa5kTlvBySlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-TA5K-TLV-MIB", "adTa5kTlvBySlotInstance"),
    (0, "ADTRAN-TA5K-TLV-MIB", "adTa5kTlvBySlotSequence"),
)
if mibBuilder.loadTexts:
    adTa5kTlvBySlotEntry.setStatus("current")
_AdTa5kTlvBySlotBulk_Type = OctetString
_AdTa5kTlvBySlotBulk_Object = MibTableColumn
adTa5kTlvBySlotBulk = _AdTa5kTlvBySlotBulk_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 4, 1, 1),
    _AdTa5kTlvBySlotBulk_Type()
)
adTa5kTlvBySlotBulk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kTlvBySlotBulk.setStatus("current")
_AdTa5kTlvBySlotSequence_Type = Integer32
_AdTa5kTlvBySlotSequence_Object = MibTableColumn
adTa5kTlvBySlotSequence = _AdTa5kTlvBySlotSequence_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 5, 4, 1, 2),
    _AdTa5kTlvBySlotSequence_Type()
)
adTa5kTlvBySlotSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTa5kTlvBySlotSequence.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-TLV-MIB",
    **{"adTa5kTlvCountTable": adTa5kTlvCountTable,
       "adTa5kTlvCountEntry": adTa5kTlvCountEntry,
       "adTa5kTlvCount": adTa5kTlvCount,
       "adTa5kTlvInstance": adTa5kTlvInstance,
       "adTa5kTlvDelete": adTa5kTlvDelete,
       "adTa5kTlvTable": adTa5kTlvTable,
       "adTa5kTlvEntry": adTa5kTlvEntry,
       "adTa5kTlvBulk": adTa5kTlvBulk,
       "adTa5kTlvSequence": adTa5kTlvSequence,
       "adTa5kTlvBySlotCountTable": adTa5kTlvBySlotCountTable,
       "adTa5kTlvBySlotCountEntry": adTa5kTlvBySlotCountEntry,
       "adTa5kTlvBySlotCount": adTa5kTlvBySlotCount,
       "adTa5kTlvBySlotInstance": adTa5kTlvBySlotInstance,
       "adTa5kTlvBySlotDelete": adTa5kTlvBySlotDelete,
       "adTa5kTlvBySlotTable": adTa5kTlvBySlotTable,
       "adTa5kTlvBySlotEntry": adTa5kTlvBySlotEntry,
       "adTa5kTlvBySlotBulk": adTa5kTlvBySlotBulk,
       "adTa5kTlvBySlotSequence": adTa5kTlvBySlotSequence,
       "adTa5kTlvModuleIdentity": adTa5kTlvModuleIdentity}
)
