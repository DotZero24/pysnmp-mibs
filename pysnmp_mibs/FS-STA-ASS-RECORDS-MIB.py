# SNMP MIB module (FS-STA-ASS-RECORDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-STA-ASS-RECORDS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:19 2025
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

(fsIfIndex,) = mibBuilder.importSymbols(
    "FS-INTERFACE-MIB",
    "fsIfIndex")

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsStaAssRecordsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101)
)
if mibBuilder.loadTexts:
    fsStaAssRecordsMIB.setRevisions(
        ("2009-11-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsStaAssRecordsMIBTrap_ObjectIdentity = ObjectIdentity
fsStaAssRecordsMIBTrap = _FsStaAssRecordsMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 0)
)
_FsStaAssRecordsMIBObjects_ObjectIdentity = ObjectIdentity
fsStaAssRecordsMIBObjects = _FsStaAssRecordsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1)
)
_FsStaAssRecordsGrobal_ObjectIdentity = ObjectIdentity
fsStaAssRecordsGrobal = _FsStaAssRecordsGrobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1)
)
_FsStaAssRecordsGrobalTable_Object = MibTable
fsStaAssRecordsGrobalTable = _FsStaAssRecordsGrobalTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsStaAssRecordsGrobalTable.setStatus("current")
_FsStaAssRecordsGrobalEntry_Object = MibTableRow
fsStaAssRecordsGrobalEntry = _FsStaAssRecordsGrobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1)
)
fsStaAssRecordsGrobalEntry.setIndexNames(
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaMacGrobalAddress"),
)
if mibBuilder.loadTexts:
    fsStaAssRecordsGrobalEntry.setStatus("current")
_FsStaMacGrobalAddress_Type = MacAddress
_FsStaMacGrobalAddress_Object = MibTableColumn
fsStaMacGrobalAddress = _FsStaMacGrobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1, 1),
    _FsStaMacGrobalAddress_Type()
)
fsStaMacGrobalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaMacGrobalAddress.setStatus("current")


class _FsStaMacGrobalAPName_Type(DisplayString):
    """Custom type fsStaMacGrobalAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsStaMacGrobalAPName_Type.__name__ = "DisplayString"
_FsStaMacGrobalAPName_Object = MibTableColumn
fsStaMacGrobalAPName = _FsStaMacGrobalAPName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1, 2),
    _FsStaMacGrobalAPName_Type()
)
fsStaMacGrobalAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaMacGrobalAPName.setStatus("current")


class _FsStaMacGrobalISUP_Type(Integer32):
    """Custom type fsStaMacGrobalISUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_FsStaMacGrobalISUP_Type.__name__ = "Integer32"
_FsStaMacGrobalISUP_Object = MibTableColumn
fsStaMacGrobalISUP = _FsStaMacGrobalISUP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1, 3),
    _FsStaMacGrobalISUP_Type()
)
fsStaMacGrobalISUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaMacGrobalISUP.setStatus("current")
_FsStaMacGrobalStartime_Type = DateAndTime
_FsStaMacGrobalStartime_Object = MibTableColumn
fsStaMacGrobalStartime = _FsStaMacGrobalStartime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1, 4),
    _FsStaMacGrobalStartime_Type()
)
fsStaMacGrobalStartime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaMacGrobalStartime.setStatus("current")
_FsStaMacGrobalupdowntimes_Type = Unsigned32
_FsStaMacGrobalupdowntimes_Object = MibTableColumn
fsStaMacGrobalupdowntimes = _FsStaMacGrobalupdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1, 5),
    _FsStaMacGrobalupdowntimes_Type()
)
fsStaMacGrobalupdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaMacGrobalupdowntimes.setStatus("current")
_FsStaMacGrobalroamtimes_Type = Unsigned32
_FsStaMacGrobalroamtimes_Object = MibTableColumn
fsStaMacGrobalroamtimes = _FsStaMacGrobalroamtimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1, 6),
    _FsStaMacGrobalroamtimes_Type()
)
fsStaMacGrobalroamtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaMacGrobalroamtimes.setStatus("current")
_FsStaMacGrobaltotaltimes_Type = Unsigned32
_FsStaMacGrobaltotaltimes_Object = MibTableColumn
fsStaMacGrobaltotaltimes = _FsStaMacGrobaltotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1, 7),
    _FsStaMacGrobaltotaltimes_Type()
)
fsStaMacGrobaltotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaMacGrobaltotaltimes.setStatus("current")
_FsStaMacGrobalrealdowntimes_Type = Unsigned32
_FsStaMacGrobalrealdowntimes_Object = MibTableColumn
fsStaMacGrobalrealdowntimes = _FsStaMacGrobalrealdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1, 8),
    _FsStaMacGrobalrealdowntimes_Type()
)
fsStaMacGrobalrealdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaMacGrobalrealdowntimes.setStatus("current")


class _FsStaMacGrobalSSID_Type(DisplayString):
    """Custom type fsStaMacGrobalSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsStaMacGrobalSSID_Type.__name__ = "DisplayString"
_FsStaMacGrobalSSID_Object = MibTableColumn
fsStaMacGrobalSSID = _FsStaMacGrobalSSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 1, 1, 1, 9),
    _FsStaMacGrobalSSID_Type()
)
fsStaMacGrobalSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaMacGrobalSSID.setStatus("current")
_FsStaAssRecordsByMAC_ObjectIdentity = ObjectIdentity
fsStaAssRecordsByMAC = _FsStaAssRecordsByMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2)
)
_FsStaAssRecordsByMACTable_Object = MibTable
fsStaAssRecordsByMACTable = _FsStaAssRecordsByMACTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsStaAssRecordsByMACTable.setStatus("current")
_FsStaAssRecordsByMACEntry_Object = MibTableRow
fsStaAssRecordsByMACEntry = _FsStaAssRecordsByMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1)
)
fsStaAssRecordsByMACEntry.setIndexNames(
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaMacAddress"),
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaMacindex"),
)
if mibBuilder.loadTexts:
    fsStaAssRecordsByMACEntry.setStatus("current")
_FsStaMacAddress_Type = MacAddress
_FsStaMacAddress_Object = MibTableColumn
fsStaMacAddress = _FsStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 1),
    _FsStaMacAddress_Type()
)
fsStaMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaMacAddress.setStatus("current")
_FsStaMacindex_Type = Unsigned32
_FsStaMacindex_Object = MibTableColumn
fsStaMacindex = _FsStaMacindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 2),
    _FsStaMacindex_Type()
)
fsStaMacindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaMacindex.setStatus("current")
_FsStaAsstime_Type = DateAndTime
_FsStaAsstime_Object = MibTableColumn
fsStaAsstime = _FsStaAsstime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 3),
    _FsStaAsstime_Type()
)
fsStaAsstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAsstime.setStatus("current")


class _FsStaAssAction_Type(Integer32):
    """Custom type fsStaAssAction based on Integer32"""
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
        *(("join", 1),
          ("leave", 2),
          ("roam", 3),
          ("delete", 4))
    )


_FsStaAssAction_Type.__name__ = "Integer32"
_FsStaAssAction_Object = MibTableColumn
fsStaAssAction = _FsStaAssAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 4),
    _FsStaAssAction_Type()
)
fsStaAssAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssAction.setStatus("current")
_FsStaAssSubAction_Type = Integer32
_FsStaAssSubAction_Object = MibTableColumn
fsStaAssSubAction = _FsStaAssSubAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 5),
    _FsStaAssSubAction_Type()
)
fsStaAssSubAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssSubAction.setStatus("current")


class _FsStaAssResult_Type(Integer32):
    """Custom type fsStaAssResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("failed", 1))
    )


_FsStaAssResult_Type.__name__ = "Integer32"
_FsStaAssResult_Object = MibTableColumn
fsStaAssResult = _FsStaAssResult_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 6),
    _FsStaAssResult_Type()
)
fsStaAssResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssResult.setStatus("current")
_FsStaAssReason_Type = Integer32
_FsStaAssReason_Object = MibTableColumn
fsStaAssReason = _FsStaAssReason_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 7),
    _FsStaAssReason_Type()
)
fsStaAssReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssReason.setStatus("current")


class _FsStaAssApNamePre_Type(DisplayString):
    """Custom type fsStaAssApNamePre based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsStaAssApNamePre_Type.__name__ = "DisplayString"
_FsStaAssApNamePre_Object = MibTableColumn
fsStaAssApNamePre = _FsStaAssApNamePre_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 8),
    _FsStaAssApNamePre_Type()
)
fsStaAssApNamePre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssApNamePre.setStatus("current")


class _FsStaAssApNameNow_Type(DisplayString):
    """Custom type fsStaAssApNameNow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsStaAssApNameNow_Type.__name__ = "DisplayString"
_FsStaAssApNameNow_Object = MibTableColumn
fsStaAssApNameNow = _FsStaAssApNameNow_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 9),
    _FsStaAssApNameNow_Type()
)
fsStaAssApNameNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssApNameNow.setStatus("current")
_FsStaAssSignalQua_Type = Integer32
_FsStaAssSignalQua_Object = MibTableColumn
fsStaAssSignalQua = _FsStaAssSignalQua_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 10),
    _FsStaAssSignalQua_Type()
)
fsStaAssSignalQua.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssSignalQua.setStatus("current")
_FsStaAssRoamtype_Type = Integer32
_FsStaAssRoamtype_Object = MibTableColumn
fsStaAssRoamtype = _FsStaAssRoamtype_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 11),
    _FsStaAssRoamtype_Type()
)
fsStaAssRoamtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssRoamtype.setStatus("current")
_FsStaAssjitter_Type = Integer32
_FsStaAssjitter_Object = MibTableColumn
fsStaAssjitter = _FsStaAssjitter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 12),
    _FsStaAssjitter_Type()
)
fsStaAssjitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssjitter.setStatus("current")
_FsStaAssjointimes_Type = Unsigned32
_FsStaAssjointimes_Object = MibTableColumn
fsStaAssjointimes = _FsStaAssjointimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 13),
    _FsStaAssjointimes_Type()
)
fsStaAssjointimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssjointimes.setStatus("current")
_FsStaAsslatelytime_Type = DateAndTime
_FsStaAsslatelytime_Object = MibTableColumn
fsStaAsslatelytime = _FsStaAsslatelytime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 14),
    _FsStaAsslatelytime_Type()
)
fsStaAsslatelytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAsslatelytime.setStatus("current")
_FsStaAssSSID_Type = DisplayString
_FsStaAssSSID_Object = MibTableColumn
fsStaAssSSID = _FsStaAssSSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 2, 1, 1, 15),
    _FsStaAssSSID_Type()
)
fsStaAssSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAssSSID.setStatus("current")
_FsStaAssRecordsByTime_ObjectIdentity = ObjectIdentity
fsStaAssRecordsByTime = _FsStaAssRecordsByTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3)
)
_FsStaAssRecordsSearchByTimeTable_Object = MibTable
fsStaAssRecordsSearchByTimeTable = _FsStaAssRecordsSearchByTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsStaAssRecordsSearchByTimeTable.setStatus("current")
_FsStaAssRecordsSearchByTimeEntry_Object = MibTableRow
fsStaAssRecordsSearchByTimeEntry = _FsStaAssRecordsSearchByTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1)
)
fsStaAssRecordsSearchByTimeEntry.setIndexNames(
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaUptimeLow"),
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaUptimeHigh"),
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaDowntimeLow"),
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaDowntimeHigh"),
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaTimeindex"),
)
if mibBuilder.loadTexts:
    fsStaAssRecordsSearchByTimeEntry.setStatus("current")
_FsStaUptimeLow_Type = DateAndTime
_FsStaUptimeLow_Object = MibTableColumn
fsStaUptimeLow = _FsStaUptimeLow_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 1),
    _FsStaUptimeLow_Type()
)
fsStaUptimeLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaUptimeLow.setStatus("current")
_FsStaUptimeHigh_Type = DateAndTime
_FsStaUptimeHigh_Object = MibTableColumn
fsStaUptimeHigh = _FsStaUptimeHigh_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 2),
    _FsStaUptimeHigh_Type()
)
fsStaUptimeHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaUptimeHigh.setStatus("current")
_FsStaDowntimeLow_Type = DateAndTime
_FsStaDowntimeLow_Object = MibTableColumn
fsStaDowntimeLow = _FsStaDowntimeLow_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 3),
    _FsStaDowntimeLow_Type()
)
fsStaDowntimeLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaDowntimeLow.setStatus("current")
_FsStaDowntimeHigh_Type = DateAndTime
_FsStaDowntimeHigh_Object = MibTableColumn
fsStaDowntimeHigh = _FsStaDowntimeHigh_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 4),
    _FsStaDowntimeHigh_Type()
)
fsStaDowntimeHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaDowntimeHigh.setStatus("current")
_FsStaTimeindex_Type = Unsigned32
_FsStaTimeindex_Object = MibTableColumn
fsStaTimeindex = _FsStaTimeindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 5),
    _FsStaTimeindex_Type()
)
fsStaTimeindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaTimeindex.setStatus("current")
_FsStaTimeMac_Type = MacAddress
_FsStaTimeMac_Object = MibTableColumn
fsStaTimeMac = _FsStaTimeMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 6),
    _FsStaTimeMac_Type()
)
fsStaTimeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimeMac.setStatus("current")


class _FsStaTimeAPName_Type(DisplayString):
    """Custom type fsStaTimeAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsStaTimeAPName_Type.__name__ = "DisplayString"
_FsStaTimeAPName_Object = MibTableColumn
fsStaTimeAPName = _FsStaTimeAPName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 7),
    _FsStaTimeAPName_Type()
)
fsStaTimeAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimeAPName.setStatus("current")


class _FsStaTimeISUP_Type(Integer32):
    """Custom type fsStaTimeISUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_FsStaTimeISUP_Type.__name__ = "Integer32"
_FsStaTimeISUP_Object = MibTableColumn
fsStaTimeISUP = _FsStaTimeISUP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 8),
    _FsStaTimeISUP_Type()
)
fsStaTimeISUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimeISUP.setStatus("current")
_FsStaTimeStartime_Type = DateAndTime
_FsStaTimeStartime_Object = MibTableColumn
fsStaTimeStartime = _FsStaTimeStartime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 9),
    _FsStaTimeStartime_Type()
)
fsStaTimeStartime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimeStartime.setStatus("current")
_FsStaTimeupdowntimes_Type = Unsigned32
_FsStaTimeupdowntimes_Object = MibTableColumn
fsStaTimeupdowntimes = _FsStaTimeupdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 10),
    _FsStaTimeupdowntimes_Type()
)
fsStaTimeupdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimeupdowntimes.setStatus("current")
_FsStaTimeroamtimes_Type = Unsigned32
_FsStaTimeroamtimes_Object = MibTableColumn
fsStaTimeroamtimes = _FsStaTimeroamtimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 11),
    _FsStaTimeroamtimes_Type()
)
fsStaTimeroamtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimeroamtimes.setStatus("current")
_FsStaTimertotaltimes_Type = Unsigned32
_FsStaTimertotaltimes_Object = MibTableColumn
fsStaTimertotaltimes = _FsStaTimertotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 12),
    _FsStaTimertotaltimes_Type()
)
fsStaTimertotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimertotaltimes.setStatus("current")
_FsStaTimerjitter_Type = Integer32
_FsStaTimerjitter_Object = MibTableColumn
fsStaTimerjitter = _FsStaTimerjitter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 13),
    _FsStaTimerjitter_Type()
)
fsStaTimerjitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimerjitter.setStatus("current")
_FsStaTimerjointimes_Type = Unsigned32
_FsStaTimerjointimes_Object = MibTableColumn
fsStaTimerjointimes = _FsStaTimerjointimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 14),
    _FsStaTimerjointimes_Type()
)
fsStaTimerjointimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimerjointimes.setStatus("current")
_FsStaTimerlatelytime_Type = DateAndTime
_FsStaTimerlatelytime_Object = MibTableColumn
fsStaTimerlatelytime = _FsStaTimerlatelytime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 15),
    _FsStaTimerlatelytime_Type()
)
fsStaTimerlatelytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimerlatelytime.setStatus("current")
_FsStaTimerSSID_Type = DisplayString
_FsStaTimerSSID_Object = MibTableColumn
fsStaTimerSSID = _FsStaTimerSSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 3, 1, 1, 16),
    _FsStaTimerSSID_Type()
)
fsStaTimerSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaTimerSSID.setStatus("current")
_FsStaAssRecordsByAP_ObjectIdentity = ObjectIdentity
fsStaAssRecordsByAP = _FsStaAssRecordsByAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4)
)
_FsStaAssRecordsSearchByAPTable_Object = MibTable
fsStaAssRecordsSearchByAPTable = _FsStaAssRecordsSearchByAPTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsStaAssRecordsSearchByAPTable.setStatus("current")
_FsStaAssRecordsSearchByAPEntry_Object = MibTableRow
fsStaAssRecordsSearchByAPEntry = _FsStaAssRecordsSearchByAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1)
)
fsStaAssRecordsSearchByAPEntry.setIndexNames(
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaAPAPName"),
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaAPindex"),
)
if mibBuilder.loadTexts:
    fsStaAssRecordsSearchByAPEntry.setStatus("current")


class _FsStaAPAPName_Type(DisplayString):
    """Custom type fsStaAPAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsStaAPAPName_Type.__name__ = "DisplayString"
_FsStaAPAPName_Object = MibTableColumn
fsStaAPAPName = _FsStaAPAPName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 1),
    _FsStaAPAPName_Type()
)
fsStaAPAPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaAPAPName.setStatus("current")
_FsStaAPindex_Type = Unsigned32
_FsStaAPindex_Object = MibTableColumn
fsStaAPindex = _FsStaAPindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 2),
    _FsStaAPindex_Type()
)
fsStaAPindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaAPindex.setStatus("current")
_FsStaAPMac_Type = MacAddress
_FsStaAPMac_Object = MibTableColumn
fsStaAPMac = _FsStaAPMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 3),
    _FsStaAPMac_Type()
)
fsStaAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAPMac.setStatus("current")


class _FsStaAPISUP_Type(Integer32):
    """Custom type fsStaAPISUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_FsStaAPISUP_Type.__name__ = "Integer32"
_FsStaAPISUP_Object = MibTableColumn
fsStaAPISUP = _FsStaAPISUP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 4),
    _FsStaAPISUP_Type()
)
fsStaAPISUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAPISUP.setStatus("current")
_FsStaAPStartime_Type = DateAndTime
_FsStaAPStartime_Object = MibTableColumn
fsStaAPStartime = _FsStaAPStartime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 5),
    _FsStaAPStartime_Type()
)
fsStaAPStartime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAPStartime.setStatus("current")
_FsStaAPupdowntimes_Type = Unsigned32
_FsStaAPupdowntimes_Object = MibTableColumn
fsStaAPupdowntimes = _FsStaAPupdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 6),
    _FsStaAPupdowntimes_Type()
)
fsStaAPupdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAPupdowntimes.setStatus("current")
_FsStaAProamtimes_Type = Unsigned32
_FsStaAProamtimes_Object = MibTableColumn
fsStaAProamtimes = _FsStaAProamtimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 7),
    _FsStaAProamtimes_Type()
)
fsStaAProamtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAProamtimes.setStatus("current")
_FsStaAPtotaltimes_Type = Unsigned32
_FsStaAPtotaltimes_Object = MibTableColumn
fsStaAPtotaltimes = _FsStaAPtotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 8),
    _FsStaAPtotaltimes_Type()
)
fsStaAPtotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAPtotaltimes.setStatus("current")
_FsStaAPjitter_Type = Integer32
_FsStaAPjitter_Object = MibTableColumn
fsStaAPjitter = _FsStaAPjitter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 9),
    _FsStaAPjitter_Type()
)
fsStaAPjitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAPjitter.setStatus("current")
_FsStaAPjointimes_Type = Unsigned32
_FsStaAPjointimes_Object = MibTableColumn
fsStaAPjointimes = _FsStaAPjointimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 10),
    _FsStaAPjointimes_Type()
)
fsStaAPjointimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAPjointimes.setStatus("current")
_FsStaAPlatelytime_Type = DateAndTime
_FsStaAPlatelytime_Object = MibTableColumn
fsStaAPlatelytime = _FsStaAPlatelytime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 11),
    _FsStaAPlatelytime_Type()
)
fsStaAPlatelytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAPlatelytime.setStatus("current")
_FsStaAPSSID_Type = DisplayString
_FsStaAPSSID_Object = MibTableColumn
fsStaAPSSID = _FsStaAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 4, 1, 1, 12),
    _FsStaAPSSID_Type()
)
fsStaAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaAPSSID.setStatus("current")
_FsStaAssSignalByMAC_ObjectIdentity = ObjectIdentity
fsStaAssSignalByMAC = _FsStaAssSignalByMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 5)
)
_FsStaAssSignalByMACTable_Object = MibTable
fsStaAssSignalByMACTable = _FsStaAssSignalByMACTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fsStaAssSignalByMACTable.setStatus("current")
_FsStaAssSignalByMACEntry_Object = MibTableRow
fsStaAssSignalByMACEntry = _FsStaAssSignalByMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 5, 1, 1)
)
fsStaAssSignalByMACEntry.setIndexNames(
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaSignalMacAddress"),
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaSignalMacindex"),
)
if mibBuilder.loadTexts:
    fsStaAssSignalByMACEntry.setStatus("current")
_FsStaSignalMacAddress_Type = MacAddress
_FsStaSignalMacAddress_Object = MibTableColumn
fsStaSignalMacAddress = _FsStaSignalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 5, 1, 1, 1),
    _FsStaSignalMacAddress_Type()
)
fsStaSignalMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaSignalMacAddress.setStatus("current")
_FsStaSignalMacindex_Type = Unsigned32
_FsStaSignalMacindex_Object = MibTableColumn
fsStaSignalMacindex = _FsStaSignalMacindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 5, 1, 1, 2),
    _FsStaSignalMacindex_Type()
)
fsStaSignalMacindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaSignalMacindex.setStatus("current")
_FsStaSignaltime_Type = DateAndTime
_FsStaSignaltime_Object = MibTableColumn
fsStaSignaltime = _FsStaSignaltime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 5, 1, 1, 3),
    _FsStaSignaltime_Type()
)
fsStaSignaltime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaSignaltime.setStatus("current")
_FsStaSignalValue_Type = Integer32
_FsStaSignalValue_Object = MibTableColumn
fsStaSignalValue = _FsStaSignalValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 5, 1, 1, 4),
    _FsStaSignalValue_Type()
)
fsStaSignalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaSignalValue.setStatus("current")
_FsStaAssRetryByMAC_ObjectIdentity = ObjectIdentity
fsStaAssRetryByMAC = _FsStaAssRetryByMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 6)
)
_FsStaAssRetryByMACTable_Object = MibTable
fsStaAssRetryByMACTable = _FsStaAssRetryByMACTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fsStaAssRetryByMACTable.setStatus("current")
_FsStaAssRetryByMACEntry_Object = MibTableRow
fsStaAssRetryByMACEntry = _FsStaAssRetryByMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 6, 1, 1)
)
fsStaAssRetryByMACEntry.setIndexNames(
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaRetryMacAddress"),
    (0, "FS-STA-ASS-RECORDS-MIB", "fsStaRetryMacindex"),
)
if mibBuilder.loadTexts:
    fsStaAssRetryByMACEntry.setStatus("current")
_FsStaRetryMacAddress_Type = MacAddress
_FsStaRetryMacAddress_Object = MibTableColumn
fsStaRetryMacAddress = _FsStaRetryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 6, 1, 1, 1),
    _FsStaRetryMacAddress_Type()
)
fsStaRetryMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaRetryMacAddress.setStatus("current")
_FsStaRetryMacindex_Type = Unsigned32
_FsStaRetryMacindex_Object = MibTableColumn
fsStaRetryMacindex = _FsStaRetryMacindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 6, 1, 1, 2),
    _FsStaRetryMacindex_Type()
)
fsStaRetryMacindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsStaRetryMacindex.setStatus("current")
_FsStaRetrytime_Type = DateAndTime
_FsStaRetrytime_Object = MibTableColumn
fsStaRetrytime = _FsStaRetrytime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 6, 1, 1, 3),
    _FsStaRetrytime_Type()
)
fsStaRetrytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaRetrytime.setStatus("current")
_FsStaRetryValue_Type = Integer32
_FsStaRetryValue_Object = MibTableColumn
fsStaRetryValue = _FsStaRetryValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 6, 1, 1, 4),
    _FsStaRetryValue_Type()
)
fsStaRetryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaRetryValue.setStatus("current")
_FsStaAssStatistic_ObjectIdentity = ObjectIdentity
fsStaAssStatistic = _FsStaAssStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 7)
)
_FsAssStatisticsTotalsta_Type = Unsigned32
_FsAssStatisticsTotalsta_Object = MibScalar
fsAssStatisticsTotalsta = _FsAssStatisticsTotalsta_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 7, 1),
    _FsAssStatisticsTotalsta_Type()
)
fsAssStatisticsTotalsta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAssStatisticsTotalsta.setStatus("current")
_FsAssStatisticsTotalinfo_Type = Unsigned32
_FsAssStatisticsTotalinfo_Object = MibScalar
fsAssStatisticsTotalinfo = _FsAssStatisticsTotalinfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 7, 2),
    _FsAssStatisticsTotalinfo_Type()
)
fsAssStatisticsTotalinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAssStatisticsTotalinfo.setStatus("current")
_FsAssStatisticsdown_Type = Unsigned32
_FsAssStatisticsdown_Object = MibScalar
fsAssStatisticsdown = _FsAssStatisticsdown_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 7, 3),
    _FsAssStatisticsdown_Type()
)
fsAssStatisticsdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAssStatisticsdown.setStatus("current")
_FsAssStatisticsObligate1_Type = Unsigned32
_FsAssStatisticsObligate1_Object = MibScalar
fsAssStatisticsObligate1 = _FsAssStatisticsObligate1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 7, 4),
    _FsAssStatisticsObligate1_Type()
)
fsAssStatisticsObligate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAssStatisticsObligate1.setStatus("current")
_FsAssStatisticsObligate2_Type = Unsigned32
_FsAssStatisticsObligate2_Object = MibScalar
fsAssStatisticsObligate2 = _FsAssStatisticsObligate2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 7, 5),
    _FsAssStatisticsObligate2_Type()
)
fsAssStatisticsObligate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAssStatisticsObligate2.setStatus("current")
_FsAssStatisticsObligate3_Type = Unsigned32
_FsAssStatisticsObligate3_Object = MibScalar
fsAssStatisticsObligate3 = _FsAssStatisticsObligate3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 1, 7, 6),
    _FsAssStatisticsObligate3_Type()
)
fsAssStatisticsObligate3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAssStatisticsObligate3.setStatus("current")
_FsStaAssRecordsMIBConformance_ObjectIdentity = ObjectIdentity
fsStaAssRecordsMIBConformance = _FsStaAssRecordsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2)
)
_FsStaAssRecordsMIBCompliances_ObjectIdentity = ObjectIdentity
fsStaAssRecordsMIBCompliances = _FsStaAssRecordsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 1)
)
_FsStaAssRecordsMIBGroups_ObjectIdentity = ObjectIdentity
fsStaAssRecordsMIBGroups = _FsStaAssRecordsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 2)
)

# Managed Objects groups

fsStaAssRecordsGrobalMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 2, 1)
)
fsStaAssRecordsGrobalMIBroup.setObjects(
      *(("FS-STA-ASS-RECORDS-MIB", "fsStaMacGrobalAPName"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaMacGrobalISUP"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaMacGrobalStartime"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaMacGrobalupdowntimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaMacGrobalroamtimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaMacGrobaltotaltimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaMacGrobalrealdowntimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaMacGrobalSSID"))
)
if mibBuilder.loadTexts:
    fsStaAssRecordsGrobalMIBroup.setStatus("current")

fsStaAssRecordsMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 2, 2)
)
fsStaAssRecordsMIBroup.setObjects(
      *(("FS-STA-ASS-RECORDS-MIB", "fsStaAsstime"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssAction"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssSubAction"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssResult"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssReason"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssApNamePre"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssApNameNow"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssSignalQua"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssRoamtype"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssjitter"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssjointimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAsslatelytime"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssSSID"))
)
if mibBuilder.loadTexts:
    fsStaAssRecordsMIBroup.setStatus("current")

fsStaAssRecordsSearchByTimeMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 2, 3)
)
fsStaAssRecordsSearchByTimeMIBroup.setObjects(
      *(("FS-STA-ASS-RECORDS-MIB", "fsStaTimeMac"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimeAPName"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimeISUP"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimeStartime"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimeupdowntimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimeroamtimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimertotaltimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimerjitter"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimerjointimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimerlatelytime"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaTimerSSID"))
)
if mibBuilder.loadTexts:
    fsStaAssRecordsSearchByTimeMIBroup.setStatus("current")

fsStaAssRecordsSearchByAPMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 2, 4)
)
fsStaAssRecordsSearchByAPMIBroup.setObjects(
      *(("FS-STA-ASS-RECORDS-MIB", "fsStaAPMac"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAPISUP"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAPStartime"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAPupdowntimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAProamtimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAPtotaltimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAPjitter"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAPjointimes"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAPlatelytime"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAPSSID"))
)
if mibBuilder.loadTexts:
    fsStaAssRecordsSearchByAPMIBroup.setStatus("current")

fsStaAssSignalSearchByMACMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 2, 5)
)
fsStaAssSignalSearchByMACMIBroup.setObjects(
      *(("FS-STA-ASS-RECORDS-MIB", "fsStaSignaltime"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaSignalValue"))
)
if mibBuilder.loadTexts:
    fsStaAssSignalSearchByMACMIBroup.setStatus("current")

fsStaAssRetrySearchByMACMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 2, 6)
)
fsStaAssRetrySearchByMACMIBroup.setObjects(
      *(("FS-STA-ASS-RECORDS-MIB", "fsStaRetrytime"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaRetryValue"))
)
if mibBuilder.loadTexts:
    fsStaAssRetrySearchByMACMIBroup.setStatus("current")

fsStaAssStatisticsMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 2, 7)
)
fsStaAssStatisticsMIBroup.setObjects(
      *(("FS-STA-ASS-RECORDS-MIB", "fsAssStatisticsTotalsta"),
        ("FS-STA-ASS-RECORDS-MIB", "fsAssStatisticsTotalinfo"),
        ("FS-STA-ASS-RECORDS-MIB", "fsAssStatisticsdown"),
        ("FS-STA-ASS-RECORDS-MIB", "fsAssStatisticsObligate1"),
        ("FS-STA-ASS-RECORDS-MIB", "fsAssStatisticsObligate2"),
        ("FS-STA-ASS-RECORDS-MIB", "fsAssStatisticsObligate3"))
)
if mibBuilder.loadTexts:
    fsStaAssStatisticsMIBroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsStaAssRecordsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 101, 2, 1, 1)
)
fsStaAssRecordsMIBCompliance.setObjects(
      *(("FS-STA-ASS-RECORDS-MIB", "fsStaAssRecordsGrobalMIBroup"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssRecordsMIBroup"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssRecordsSearchByTimeMIBroup"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssRecordsSearchByAPMIBroup"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssSignalSearchByMACMIBroup"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssRetrySearchByMACMIBroup"),
        ("FS-STA-ASS-RECORDS-MIB", "fsStaAssStatisticsMIBroup"))
)
if mibBuilder.loadTexts:
    fsStaAssRecordsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-STA-ASS-RECORDS-MIB",
    **{"fsStaAssRecordsMIB": fsStaAssRecordsMIB,
       "fsStaAssRecordsMIBTrap": fsStaAssRecordsMIBTrap,
       "fsStaAssRecordsMIBObjects": fsStaAssRecordsMIBObjects,
       "fsStaAssRecordsGrobal": fsStaAssRecordsGrobal,
       "fsStaAssRecordsGrobalTable": fsStaAssRecordsGrobalTable,
       "fsStaAssRecordsGrobalEntry": fsStaAssRecordsGrobalEntry,
       "fsStaMacGrobalAddress": fsStaMacGrobalAddress,
       "fsStaMacGrobalAPName": fsStaMacGrobalAPName,
       "fsStaMacGrobalISUP": fsStaMacGrobalISUP,
       "fsStaMacGrobalStartime": fsStaMacGrobalStartime,
       "fsStaMacGrobalupdowntimes": fsStaMacGrobalupdowntimes,
       "fsStaMacGrobalroamtimes": fsStaMacGrobalroamtimes,
       "fsStaMacGrobaltotaltimes": fsStaMacGrobaltotaltimes,
       "fsStaMacGrobalrealdowntimes": fsStaMacGrobalrealdowntimes,
       "fsStaMacGrobalSSID": fsStaMacGrobalSSID,
       "fsStaAssRecordsByMAC": fsStaAssRecordsByMAC,
       "fsStaAssRecordsByMACTable": fsStaAssRecordsByMACTable,
       "fsStaAssRecordsByMACEntry": fsStaAssRecordsByMACEntry,
       "fsStaMacAddress": fsStaMacAddress,
       "fsStaMacindex": fsStaMacindex,
       "fsStaAsstime": fsStaAsstime,
       "fsStaAssAction": fsStaAssAction,
       "fsStaAssSubAction": fsStaAssSubAction,
       "fsStaAssResult": fsStaAssResult,
       "fsStaAssReason": fsStaAssReason,
       "fsStaAssApNamePre": fsStaAssApNamePre,
       "fsStaAssApNameNow": fsStaAssApNameNow,
       "fsStaAssSignalQua": fsStaAssSignalQua,
       "fsStaAssRoamtype": fsStaAssRoamtype,
       "fsStaAssjitter": fsStaAssjitter,
       "fsStaAssjointimes": fsStaAssjointimes,
       "fsStaAsslatelytime": fsStaAsslatelytime,
       "fsStaAssSSID": fsStaAssSSID,
       "fsStaAssRecordsByTime": fsStaAssRecordsByTime,
       "fsStaAssRecordsSearchByTimeTable": fsStaAssRecordsSearchByTimeTable,
       "fsStaAssRecordsSearchByTimeEntry": fsStaAssRecordsSearchByTimeEntry,
       "fsStaUptimeLow": fsStaUptimeLow,
       "fsStaUptimeHigh": fsStaUptimeHigh,
       "fsStaDowntimeLow": fsStaDowntimeLow,
       "fsStaDowntimeHigh": fsStaDowntimeHigh,
       "fsStaTimeindex": fsStaTimeindex,
       "fsStaTimeMac": fsStaTimeMac,
       "fsStaTimeAPName": fsStaTimeAPName,
       "fsStaTimeISUP": fsStaTimeISUP,
       "fsStaTimeStartime": fsStaTimeStartime,
       "fsStaTimeupdowntimes": fsStaTimeupdowntimes,
       "fsStaTimeroamtimes": fsStaTimeroamtimes,
       "fsStaTimertotaltimes": fsStaTimertotaltimes,
       "fsStaTimerjitter": fsStaTimerjitter,
       "fsStaTimerjointimes": fsStaTimerjointimes,
       "fsStaTimerlatelytime": fsStaTimerlatelytime,
       "fsStaTimerSSID": fsStaTimerSSID,
       "fsStaAssRecordsByAP": fsStaAssRecordsByAP,
       "fsStaAssRecordsSearchByAPTable": fsStaAssRecordsSearchByAPTable,
       "fsStaAssRecordsSearchByAPEntry": fsStaAssRecordsSearchByAPEntry,
       "fsStaAPAPName": fsStaAPAPName,
       "fsStaAPindex": fsStaAPindex,
       "fsStaAPMac": fsStaAPMac,
       "fsStaAPISUP": fsStaAPISUP,
       "fsStaAPStartime": fsStaAPStartime,
       "fsStaAPupdowntimes": fsStaAPupdowntimes,
       "fsStaAProamtimes": fsStaAProamtimes,
       "fsStaAPtotaltimes": fsStaAPtotaltimes,
       "fsStaAPjitter": fsStaAPjitter,
       "fsStaAPjointimes": fsStaAPjointimes,
       "fsStaAPlatelytime": fsStaAPlatelytime,
       "fsStaAPSSID": fsStaAPSSID,
       "fsStaAssSignalByMAC": fsStaAssSignalByMAC,
       "fsStaAssSignalByMACTable": fsStaAssSignalByMACTable,
       "fsStaAssSignalByMACEntry": fsStaAssSignalByMACEntry,
       "fsStaSignalMacAddress": fsStaSignalMacAddress,
       "fsStaSignalMacindex": fsStaSignalMacindex,
       "fsStaSignaltime": fsStaSignaltime,
       "fsStaSignalValue": fsStaSignalValue,
       "fsStaAssRetryByMAC": fsStaAssRetryByMAC,
       "fsStaAssRetryByMACTable": fsStaAssRetryByMACTable,
       "fsStaAssRetryByMACEntry": fsStaAssRetryByMACEntry,
       "fsStaRetryMacAddress": fsStaRetryMacAddress,
       "fsStaRetryMacindex": fsStaRetryMacindex,
       "fsStaRetrytime": fsStaRetrytime,
       "fsStaRetryValue": fsStaRetryValue,
       "fsStaAssStatistic": fsStaAssStatistic,
       "fsAssStatisticsTotalsta": fsAssStatisticsTotalsta,
       "fsAssStatisticsTotalinfo": fsAssStatisticsTotalinfo,
       "fsAssStatisticsdown": fsAssStatisticsdown,
       "fsAssStatisticsObligate1": fsAssStatisticsObligate1,
       "fsAssStatisticsObligate2": fsAssStatisticsObligate2,
       "fsAssStatisticsObligate3": fsAssStatisticsObligate3,
       "fsStaAssRecordsMIBConformance": fsStaAssRecordsMIBConformance,
       "fsStaAssRecordsMIBCompliances": fsStaAssRecordsMIBCompliances,
       "fsStaAssRecordsMIBCompliance": fsStaAssRecordsMIBCompliance,
       "fsStaAssRecordsMIBGroups": fsStaAssRecordsMIBGroups,
       "fsStaAssRecordsGrobalMIBroup": fsStaAssRecordsGrobalMIBroup,
       "fsStaAssRecordsMIBroup": fsStaAssRecordsMIBroup,
       "fsStaAssRecordsSearchByTimeMIBroup": fsStaAssRecordsSearchByTimeMIBroup,
       "fsStaAssRecordsSearchByAPMIBroup": fsStaAssRecordsSearchByAPMIBroup,
       "fsStaAssSignalSearchByMACMIBroup": fsStaAssSignalSearchByMACMIBroup,
       "fsStaAssRetrySearchByMACMIBroup": fsStaAssRetrySearchByMACMIBroup,
       "fsStaAssStatisticsMIBroup": fsStaAssStatisticsMIBroup}
)
