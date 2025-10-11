# SNMP MIB module (ADTRAN-TA5K-DS3-EXTRAPERFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-DS3-EXTRAPERFS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:43 2025
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

(adTa5kSingleDs3,
 adTa5kSingleDs3ModuleIdentity) = mibBuilder.importSymbols(
    "ADTRAN-TA5K-SingleDS3-MIB",
    "adTa5kSingleDs3",
    "adTa5kSingleDs3ModuleIdentity")

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

adTa5kDs3PMModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 896, 1)
)
if mibBuilder.loadTexts:
    adTa5kDs3PMModuleIdentity.setRevisions(
        ("2011-08-30 00:00",)
    )


# Types definitions



class AdTADS3PerfCurrentCount(Counter32):
    """Custom type AdTADS3PerfCurrentCount based on Counter32"""




class AdTADS3PerfIntervalCount(Counter32):
    """Custom type AdTADS3PerfIntervalCount based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kDS3PM_ObjectIdentity = ObjectIdentity
adTa5kDS3PM = _AdTa5kDS3PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2)
)
_AdTa5kDs3PMCurrentDayTable_Object = MibTable
adTa5kDs3PMCurrentDayTable = _AdTa5kDs3PMCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1)
)
if mibBuilder.loadTexts:
    adTa5kDs3PMCurrentDayTable.setStatus("current")
_AdTa5kDs3PMCurrentDayEntry_Object = MibTableRow
adTa5kDs3PMCurrentDayEntry = _AdTa5kDs3PMCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1)
)
adTa5kDs3PMCurrentDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kDs3PMCurrentDayEntry.setStatus("current")
_AdTa5kDs3PMDayCurrentPESs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentPESs_Object = MibTableColumn
adTa5kDs3PMDayCurrentPESs = _AdTa5kDs3PMDayCurrentPESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 1),
    _AdTa5kDs3PMDayCurrentPESs_Type()
)
adTa5kDs3PMDayCurrentPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentPESs.setStatus("current")
_AdTa5kDs3PMDayCurrentPSESs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentPSESs_Object = MibTableColumn
adTa5kDs3PMDayCurrentPSESs = _AdTa5kDs3PMDayCurrentPSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 2),
    _AdTa5kDs3PMDayCurrentPSESs_Type()
)
adTa5kDs3PMDayCurrentPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentPSESs.setStatus("current")
_AdTa5kDs3PMDayCurrentSEFSs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentSEFSs_Object = MibTableColumn
adTa5kDs3PMDayCurrentSEFSs = _AdTa5kDs3PMDayCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 3),
    _AdTa5kDs3PMDayCurrentSEFSs_Type()
)
adTa5kDs3PMDayCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentSEFSs.setStatus("current")
_AdTa5kDs3PMDayCurrentUASs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentUASs_Object = MibTableColumn
adTa5kDs3PMDayCurrentUASs = _AdTa5kDs3PMDayCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 4),
    _AdTa5kDs3PMDayCurrentUASs_Type()
)
adTa5kDs3PMDayCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentUASs.setStatus("current")
_AdTa5kDs3PMDayCurrentLCVs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentLCVs_Object = MibTableColumn
adTa5kDs3PMDayCurrentLCVs = _AdTa5kDs3PMDayCurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 5),
    _AdTa5kDs3PMDayCurrentLCVs_Type()
)
adTa5kDs3PMDayCurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentLCVs.setStatus("current")
_AdTa5kDs3PMDayCurrentPCVs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentPCVs_Object = MibTableColumn
adTa5kDs3PMDayCurrentPCVs = _AdTa5kDs3PMDayCurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 6),
    _AdTa5kDs3PMDayCurrentPCVs_Type()
)
adTa5kDs3PMDayCurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentPCVs.setStatus("current")
_AdTa5kDs3PMDayCurrentLESs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentLESs_Object = MibTableColumn
adTa5kDs3PMDayCurrentLESs = _AdTa5kDs3PMDayCurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 7),
    _AdTa5kDs3PMDayCurrentLESs_Type()
)
adTa5kDs3PMDayCurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentLESs.setStatus("current")
_AdTa5kDs3PMDayCurrentCCVs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentCCVs_Object = MibTableColumn
adTa5kDs3PMDayCurrentCCVs = _AdTa5kDs3PMDayCurrentCCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 8),
    _AdTa5kDs3PMDayCurrentCCVs_Type()
)
adTa5kDs3PMDayCurrentCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentCCVs.setStatus("current")
_AdTa5kDs3PMDayCurrentCESs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentCESs_Object = MibTableColumn
adTa5kDs3PMDayCurrentCESs = _AdTa5kDs3PMDayCurrentCESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 9),
    _AdTa5kDs3PMDayCurrentCESs_Type()
)
adTa5kDs3PMDayCurrentCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentCESs.setStatus("current")
_AdTa5kDs3PMDayCurrentCSESs_Type = AdTADS3PerfCurrentCount
_AdTa5kDs3PMDayCurrentCSESs_Object = MibTableColumn
adTa5kDs3PMDayCurrentCSESs = _AdTa5kDs3PMDayCurrentCSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 1, 1, 10),
    _AdTa5kDs3PMDayCurrentCSESs_Type()
)
adTa5kDs3PMDayCurrentCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayCurrentCSESs.setStatus("current")
_AdTa5kDs3PMIntervalDayTable_Object = MibTable
adTa5kDs3PMIntervalDayTable = _AdTa5kDs3PMIntervalDayTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2)
)
if mibBuilder.loadTexts:
    adTa5kDs3PMIntervalDayTable.setStatus("current")
_AdTa5kDs3PMIntervalDayEntry_Object = MibTableRow
adTa5kDs3PMIntervalDayEntry = _AdTa5kDs3PMIntervalDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1)
)
adTa5kDs3PMIntervalDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-TA5K-DS3-EXTRAPERFS-MIB", "adTa5kDs3PMDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adTa5kDs3PMIntervalDayEntry.setStatus("current")
_AdTa5kDs3PMDayIntervalPESs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalPESs_Object = MibTableColumn
adTa5kDs3PMDayIntervalPESs = _AdTa5kDs3PMDayIntervalPESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 1),
    _AdTa5kDs3PMDayIntervalPESs_Type()
)
adTa5kDs3PMDayIntervalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalPESs.setStatus("current")
_AdTa5kDs3PMDayIntervalPSESs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalPSESs_Object = MibTableColumn
adTa5kDs3PMDayIntervalPSESs = _AdTa5kDs3PMDayIntervalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 2),
    _AdTa5kDs3PMDayIntervalPSESs_Type()
)
adTa5kDs3PMDayIntervalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalPSESs.setStatus("current")
_AdTa5kDs3PMDayIntervalSEFSs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalSEFSs_Object = MibTableColumn
adTa5kDs3PMDayIntervalSEFSs = _AdTa5kDs3PMDayIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 3),
    _AdTa5kDs3PMDayIntervalSEFSs_Type()
)
adTa5kDs3PMDayIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalSEFSs.setStatus("current")
_AdTa5kDs3PMDayIntervalUASs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalUASs_Object = MibTableColumn
adTa5kDs3PMDayIntervalUASs = _AdTa5kDs3PMDayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 4),
    _AdTa5kDs3PMDayIntervalUASs_Type()
)
adTa5kDs3PMDayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalUASs.setStatus("current")
_AdTa5kDs3PMDayIntervalLCVs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalLCVs_Object = MibTableColumn
adTa5kDs3PMDayIntervalLCVs = _AdTa5kDs3PMDayIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 5),
    _AdTa5kDs3PMDayIntervalLCVs_Type()
)
adTa5kDs3PMDayIntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalLCVs.setStatus("current")
_AdTa5kDs3PMDayIntervalPCVs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalPCVs_Object = MibTableColumn
adTa5kDs3PMDayIntervalPCVs = _AdTa5kDs3PMDayIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 6),
    _AdTa5kDs3PMDayIntervalPCVs_Type()
)
adTa5kDs3PMDayIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalPCVs.setStatus("current")
_AdTa5kDs3PMDayIntervalLESs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalLESs_Object = MibTableColumn
adTa5kDs3PMDayIntervalLESs = _AdTa5kDs3PMDayIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 7),
    _AdTa5kDs3PMDayIntervalLESs_Type()
)
adTa5kDs3PMDayIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalLESs.setStatus("current")
_AdTa5kDs3PMDayIntervalCCVs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalCCVs_Object = MibTableColumn
adTa5kDs3PMDayIntervalCCVs = _AdTa5kDs3PMDayIntervalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 8),
    _AdTa5kDs3PMDayIntervalCCVs_Type()
)
adTa5kDs3PMDayIntervalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalCCVs.setStatus("current")
_AdTa5kDs3PMDayIntervalCESs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalCESs_Object = MibTableColumn
adTa5kDs3PMDayIntervalCESs = _AdTa5kDs3PMDayIntervalCESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 9),
    _AdTa5kDs3PMDayIntervalCESs_Type()
)
adTa5kDs3PMDayIntervalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalCESs.setStatus("current")
_AdTa5kDs3PMDayIntervalCSESs_Type = AdTADS3PerfIntervalCount
_AdTa5kDs3PMDayIntervalCSESs_Object = MibTableColumn
adTa5kDs3PMDayIntervalCSESs = _AdTa5kDs3PMDayIntervalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 10),
    _AdTa5kDs3PMDayIntervalCSESs_Type()
)
adTa5kDs3PMDayIntervalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalCSESs.setStatus("current")


class _AdTa5kDs3PMDayIntervalNumber_Type(Integer32):
    """Custom type adTa5kDs3PMDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdTa5kDs3PMDayIntervalNumber_Type.__name__ = "Integer32"
_AdTa5kDs3PMDayIntervalNumber_Object = MibTableColumn
adTa5kDs3PMDayIntervalNumber = _AdTa5kDs3PMDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 2, 1, 11),
    _AdTa5kDs3PMDayIntervalNumber_Type()
)
adTa5kDs3PMDayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3PMDayIntervalNumber.setStatus("current")
_AdTa5kDs3PMResetTable_Object = MibTable
adTa5kDs3PMResetTable = _AdTa5kDs3PMResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 3)
)
if mibBuilder.loadTexts:
    adTa5kDs3PMResetTable.setStatus("current")
_AdTa5kDs3PMResetEntry_Object = MibTableRow
adTa5kDs3PMResetEntry = _AdTa5kDs3PMResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 3, 1)
)
adTa5kDs3PMResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kDs3PMResetEntry.setStatus("current")


class _AdTa5kDs3PMReset_Type(Integer32):
    """Custom type adTa5kDs3PMReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdTa5kDs3PMReset_Type.__name__ = "Integer32"
_AdTa5kDs3PMReset_Object = MibTableColumn
adTa5kDs3PMReset = _AdTa5kDs3PMReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 3, 1, 1),
    _AdTa5kDs3PMReset_Type()
)
adTa5kDs3PMReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3PMReset.setStatus("current")
_AdTa5kDs3RollingCountTable_Object = MibTable
adTa5kDs3RollingCountTable = _AdTa5kDs3RollingCountTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4)
)
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountTable.setStatus("current")
_AdTa5kDs3RollingCountEntry_Object = MibTableRow
adTa5kDs3RollingCountEntry = _AdTa5kDs3RollingCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1)
)
adTa5kDs3RollingCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountEntry.setStatus("current")
_AdTa5kDs3RollingCountPESs_Type = Counter32
_AdTa5kDs3RollingCountPESs_Object = MibTableColumn
adTa5kDs3RollingCountPESs = _AdTa5kDs3RollingCountPESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 1),
    _AdTa5kDs3RollingCountPESs_Type()
)
adTa5kDs3RollingCountPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountPESs.setStatus("current")
_AdTa5kDs3RollingCountPSESs_Type = Counter32
_AdTa5kDs3RollingCountPSESs_Object = MibTableColumn
adTa5kDs3RollingCountPSESs = _AdTa5kDs3RollingCountPSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 2),
    _AdTa5kDs3RollingCountPSESs_Type()
)
adTa5kDs3RollingCountPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountPSESs.setStatus("current")
_AdTa5kDs3RollingCountSEFSs_Type = Counter32
_AdTa5kDs3RollingCountSEFSs_Object = MibTableColumn
adTa5kDs3RollingCountSEFSs = _AdTa5kDs3RollingCountSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 3),
    _AdTa5kDs3RollingCountSEFSs_Type()
)
adTa5kDs3RollingCountSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountSEFSs.setStatus("current")
_AdTa5kDs3RollingCountUASs_Type = Counter32
_AdTa5kDs3RollingCountUASs_Object = MibTableColumn
adTa5kDs3RollingCountUASs = _AdTa5kDs3RollingCountUASs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 4),
    _AdTa5kDs3RollingCountUASs_Type()
)
adTa5kDs3RollingCountUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountUASs.setStatus("current")
_AdTa5kDs3RollingCountLCVs_Type = Counter32
_AdTa5kDs3RollingCountLCVs_Object = MibTableColumn
adTa5kDs3RollingCountLCVs = _AdTa5kDs3RollingCountLCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 5),
    _AdTa5kDs3RollingCountLCVs_Type()
)
adTa5kDs3RollingCountLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountLCVs.setStatus("current")
_AdTa5kDs3RollingCountPCVs_Type = Counter32
_AdTa5kDs3RollingCountPCVs_Object = MibTableColumn
adTa5kDs3RollingCountPCVs = _AdTa5kDs3RollingCountPCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 6),
    _AdTa5kDs3RollingCountPCVs_Type()
)
adTa5kDs3RollingCountPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountPCVs.setStatus("current")
_AdTa5kDs3RollingCountLESs_Type = Counter32
_AdTa5kDs3RollingCountLESs_Object = MibTableColumn
adTa5kDs3RollingCountLESs = _AdTa5kDs3RollingCountLESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 7),
    _AdTa5kDs3RollingCountLESs_Type()
)
adTa5kDs3RollingCountLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountLESs.setStatus("current")
_AdTa5kDs3RollingCountCCVs_Type = Counter32
_AdTa5kDs3RollingCountCCVs_Object = MibTableColumn
adTa5kDs3RollingCountCCVs = _AdTa5kDs3RollingCountCCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 8),
    _AdTa5kDs3RollingCountCCVs_Type()
)
adTa5kDs3RollingCountCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountCCVs.setStatus("current")
_AdTa5kDs3RollingCountCESs_Type = Counter32
_AdTa5kDs3RollingCountCESs_Object = MibTableColumn
adTa5kDs3RollingCountCESs = _AdTa5kDs3RollingCountCESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 9),
    _AdTa5kDs3RollingCountCESs_Type()
)
adTa5kDs3RollingCountCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountCESs.setStatus("current")
_AdTa5kDs3RollingCountCSESs_Type = Counter32
_AdTa5kDs3RollingCountCSESs_Object = MibTableColumn
adTa5kDs3RollingCountCSESs = _AdTa5kDs3RollingCountCSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 10),
    _AdTa5kDs3RollingCountCSESs_Type()
)
adTa5kDs3RollingCountCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountCSESs.setStatus("current")


class _AdTa5kDs3RollingCountReset_Type(Integer32):
    """Custom type adTa5kDs3RollingCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdTa5kDs3RollingCountReset_Type.__name__ = "Integer32"
_AdTa5kDs3RollingCountReset_Object = MibTableColumn
adTa5kDs3RollingCountReset = _AdTa5kDs3RollingCountReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 2, 4, 1, 11),
    _AdTa5kDs3RollingCountReset_Type()
)
adTa5kDs3RollingCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kDs3RollingCountReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-DS3-EXTRAPERFS-MIB",
    **{"AdTADS3PerfCurrentCount": AdTADS3PerfCurrentCount,
       "AdTADS3PerfIntervalCount": AdTADS3PerfIntervalCount,
       "adTa5kDS3PM": adTa5kDS3PM,
       "adTa5kDs3PMCurrentDayTable": adTa5kDs3PMCurrentDayTable,
       "adTa5kDs3PMCurrentDayEntry": adTa5kDs3PMCurrentDayEntry,
       "adTa5kDs3PMDayCurrentPESs": adTa5kDs3PMDayCurrentPESs,
       "adTa5kDs3PMDayCurrentPSESs": adTa5kDs3PMDayCurrentPSESs,
       "adTa5kDs3PMDayCurrentSEFSs": adTa5kDs3PMDayCurrentSEFSs,
       "adTa5kDs3PMDayCurrentUASs": adTa5kDs3PMDayCurrentUASs,
       "adTa5kDs3PMDayCurrentLCVs": adTa5kDs3PMDayCurrentLCVs,
       "adTa5kDs3PMDayCurrentPCVs": adTa5kDs3PMDayCurrentPCVs,
       "adTa5kDs3PMDayCurrentLESs": adTa5kDs3PMDayCurrentLESs,
       "adTa5kDs3PMDayCurrentCCVs": adTa5kDs3PMDayCurrentCCVs,
       "adTa5kDs3PMDayCurrentCESs": adTa5kDs3PMDayCurrentCESs,
       "adTa5kDs3PMDayCurrentCSESs": adTa5kDs3PMDayCurrentCSESs,
       "adTa5kDs3PMIntervalDayTable": adTa5kDs3PMIntervalDayTable,
       "adTa5kDs3PMIntervalDayEntry": adTa5kDs3PMIntervalDayEntry,
       "adTa5kDs3PMDayIntervalPESs": adTa5kDs3PMDayIntervalPESs,
       "adTa5kDs3PMDayIntervalPSESs": adTa5kDs3PMDayIntervalPSESs,
       "adTa5kDs3PMDayIntervalSEFSs": adTa5kDs3PMDayIntervalSEFSs,
       "adTa5kDs3PMDayIntervalUASs": adTa5kDs3PMDayIntervalUASs,
       "adTa5kDs3PMDayIntervalLCVs": adTa5kDs3PMDayIntervalLCVs,
       "adTa5kDs3PMDayIntervalPCVs": adTa5kDs3PMDayIntervalPCVs,
       "adTa5kDs3PMDayIntervalLESs": adTa5kDs3PMDayIntervalLESs,
       "adTa5kDs3PMDayIntervalCCVs": adTa5kDs3PMDayIntervalCCVs,
       "adTa5kDs3PMDayIntervalCESs": adTa5kDs3PMDayIntervalCESs,
       "adTa5kDs3PMDayIntervalCSESs": adTa5kDs3PMDayIntervalCSESs,
       "adTa5kDs3PMDayIntervalNumber": adTa5kDs3PMDayIntervalNumber,
       "adTa5kDs3PMResetTable": adTa5kDs3PMResetTable,
       "adTa5kDs3PMResetEntry": adTa5kDs3PMResetEntry,
       "adTa5kDs3PMReset": adTa5kDs3PMReset,
       "adTa5kDs3RollingCountTable": adTa5kDs3RollingCountTable,
       "adTa5kDs3RollingCountEntry": adTa5kDs3RollingCountEntry,
       "adTa5kDs3RollingCountPESs": adTa5kDs3RollingCountPESs,
       "adTa5kDs3RollingCountPSESs": adTa5kDs3RollingCountPSESs,
       "adTa5kDs3RollingCountSEFSs": adTa5kDs3RollingCountSEFSs,
       "adTa5kDs3RollingCountUASs": adTa5kDs3RollingCountUASs,
       "adTa5kDs3RollingCountLCVs": adTa5kDs3RollingCountLCVs,
       "adTa5kDs3RollingCountPCVs": adTa5kDs3RollingCountPCVs,
       "adTa5kDs3RollingCountLESs": adTa5kDs3RollingCountLESs,
       "adTa5kDs3RollingCountCCVs": adTa5kDs3RollingCountCCVs,
       "adTa5kDs3RollingCountCESs": adTa5kDs3RollingCountCESs,
       "adTa5kDs3RollingCountCSESs": adTa5kDs3RollingCountCSESs,
       "adTa5kDs3RollingCountReset": adTa5kDs3RollingCountReset,
       "adTa5kDs3PMModuleIdentity": adTa5kDs3PMModuleIdentity}
)
