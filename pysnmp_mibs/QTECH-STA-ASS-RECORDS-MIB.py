# SNMP MIB module (QTECH-STA-ASS-RECORDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-STA-ASS-RECORDS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:27 2025
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

(qtechIfIndex,) = mibBuilder.importSymbols(
    "QTECH-INTERFACE-MIB",
    "qtechIfIndex")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechStaAssRecordsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101)
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsMIB.setRevisions(
        ("2009-11-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechStaAssRecordsMIBTrap_ObjectIdentity = ObjectIdentity
qtechStaAssRecordsMIBTrap = _QtechStaAssRecordsMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 0)
)
_QtechStaAssRecordsMIBObjects_ObjectIdentity = ObjectIdentity
qtechStaAssRecordsMIBObjects = _QtechStaAssRecordsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1)
)
_QtechStaAssRecordsGrobal_ObjectIdentity = ObjectIdentity
qtechStaAssRecordsGrobal = _QtechStaAssRecordsGrobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1)
)
_QtechStaAssRecordsGrobalTable_Object = MibTable
qtechStaAssRecordsGrobalTable = _QtechStaAssRecordsGrobalTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsGrobalTable.setStatus("current")
_QtechStaAssRecordsGrobalEntry_Object = MibTableRow
qtechStaAssRecordsGrobalEntry = _QtechStaAssRecordsGrobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1)
)
qtechStaAssRecordsGrobalEntry.setIndexNames(
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacGrobalAddress"),
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsGrobalEntry.setStatus("current")
_QtechStaMacGrobalAddress_Type = MacAddress
_QtechStaMacGrobalAddress_Object = MibTableColumn
qtechStaMacGrobalAddress = _QtechStaMacGrobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1, 1),
    _QtechStaMacGrobalAddress_Type()
)
qtechStaMacGrobalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaMacGrobalAddress.setStatus("current")


class _QtechStaMacGrobalAPName_Type(DisplayString):
    """Custom type qtechStaMacGrobalAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechStaMacGrobalAPName_Type.__name__ = "DisplayString"
_QtechStaMacGrobalAPName_Object = MibTableColumn
qtechStaMacGrobalAPName = _QtechStaMacGrobalAPName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1, 2),
    _QtechStaMacGrobalAPName_Type()
)
qtechStaMacGrobalAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaMacGrobalAPName.setStatus("current")


class _QtechStaMacGrobalISUP_Type(Integer32):
    """Custom type qtechStaMacGrobalISUP based on Integer32"""
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


_QtechStaMacGrobalISUP_Type.__name__ = "Integer32"
_QtechStaMacGrobalISUP_Object = MibTableColumn
qtechStaMacGrobalISUP = _QtechStaMacGrobalISUP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1, 3),
    _QtechStaMacGrobalISUP_Type()
)
qtechStaMacGrobalISUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaMacGrobalISUP.setStatus("current")
_QtechStaMacGrobalStartime_Type = DateAndTime
_QtechStaMacGrobalStartime_Object = MibTableColumn
qtechStaMacGrobalStartime = _QtechStaMacGrobalStartime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1, 4),
    _QtechStaMacGrobalStartime_Type()
)
qtechStaMacGrobalStartime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaMacGrobalStartime.setStatus("current")
_QtechStaMacGrobalupdowntimes_Type = Unsigned32
_QtechStaMacGrobalupdowntimes_Object = MibTableColumn
qtechStaMacGrobalupdowntimes = _QtechStaMacGrobalupdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1, 5),
    _QtechStaMacGrobalupdowntimes_Type()
)
qtechStaMacGrobalupdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaMacGrobalupdowntimes.setStatus("current")
_QtechStaMacGrobalroamtimes_Type = Unsigned32
_QtechStaMacGrobalroamtimes_Object = MibTableColumn
qtechStaMacGrobalroamtimes = _QtechStaMacGrobalroamtimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1, 6),
    _QtechStaMacGrobalroamtimes_Type()
)
qtechStaMacGrobalroamtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaMacGrobalroamtimes.setStatus("current")
_QtechStaMacGrobaltotaltimes_Type = Unsigned32
_QtechStaMacGrobaltotaltimes_Object = MibTableColumn
qtechStaMacGrobaltotaltimes = _QtechStaMacGrobaltotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1, 7),
    _QtechStaMacGrobaltotaltimes_Type()
)
qtechStaMacGrobaltotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaMacGrobaltotaltimes.setStatus("current")
_QtechStaMacGrobalrealdowntimes_Type = Unsigned32
_QtechStaMacGrobalrealdowntimes_Object = MibTableColumn
qtechStaMacGrobalrealdowntimes = _QtechStaMacGrobalrealdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1, 8),
    _QtechStaMacGrobalrealdowntimes_Type()
)
qtechStaMacGrobalrealdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaMacGrobalrealdowntimes.setStatus("current")


class _QtechStaMacGrobalSSID_Type(DisplayString):
    """Custom type qtechStaMacGrobalSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechStaMacGrobalSSID_Type.__name__ = "DisplayString"
_QtechStaMacGrobalSSID_Object = MibTableColumn
qtechStaMacGrobalSSID = _QtechStaMacGrobalSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 1, 1, 1, 9),
    _QtechStaMacGrobalSSID_Type()
)
qtechStaMacGrobalSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaMacGrobalSSID.setStatus("current")
_QtechStaAssRecordsByMAC_ObjectIdentity = ObjectIdentity
qtechStaAssRecordsByMAC = _QtechStaAssRecordsByMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2)
)
_QtechStaAssRecordsByMACTable_Object = MibTable
qtechStaAssRecordsByMACTable = _QtechStaAssRecordsByMACTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsByMACTable.setStatus("current")
_QtechStaAssRecordsByMACEntry_Object = MibTableRow
qtechStaAssRecordsByMACEntry = _QtechStaAssRecordsByMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1)
)
qtechStaAssRecordsByMACEntry.setIndexNames(
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacAddress"),
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacindex"),
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsByMACEntry.setStatus("current")
_QtechStaMacAddress_Type = MacAddress
_QtechStaMacAddress_Object = MibTableColumn
qtechStaMacAddress = _QtechStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 1),
    _QtechStaMacAddress_Type()
)
qtechStaMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaMacAddress.setStatus("current")
_QtechStaMacindex_Type = Unsigned32
_QtechStaMacindex_Object = MibTableColumn
qtechStaMacindex = _QtechStaMacindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 2),
    _QtechStaMacindex_Type()
)
qtechStaMacindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaMacindex.setStatus("current")
_QtechStaAsstime_Type = DateAndTime
_QtechStaAsstime_Object = MibTableColumn
qtechStaAsstime = _QtechStaAsstime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 3),
    _QtechStaAsstime_Type()
)
qtechStaAsstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAsstime.setStatus("current")


class _QtechStaAssAction_Type(Integer32):
    """Custom type qtechStaAssAction based on Integer32"""
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


_QtechStaAssAction_Type.__name__ = "Integer32"
_QtechStaAssAction_Object = MibTableColumn
qtechStaAssAction = _QtechStaAssAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 4),
    _QtechStaAssAction_Type()
)
qtechStaAssAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssAction.setStatus("current")
_QtechStaAssSubAction_Type = Integer32
_QtechStaAssSubAction_Object = MibTableColumn
qtechStaAssSubAction = _QtechStaAssSubAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 5),
    _QtechStaAssSubAction_Type()
)
qtechStaAssSubAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssSubAction.setStatus("current")


class _QtechStaAssResult_Type(Integer32):
    """Custom type qtechStaAssResult based on Integer32"""
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


_QtechStaAssResult_Type.__name__ = "Integer32"
_QtechStaAssResult_Object = MibTableColumn
qtechStaAssResult = _QtechStaAssResult_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 6),
    _QtechStaAssResult_Type()
)
qtechStaAssResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssResult.setStatus("current")
_QtechStaAssReason_Type = Integer32
_QtechStaAssReason_Object = MibTableColumn
qtechStaAssReason = _QtechStaAssReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 7),
    _QtechStaAssReason_Type()
)
qtechStaAssReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssReason.setStatus("current")


class _QtechStaAssApNamePre_Type(DisplayString):
    """Custom type qtechStaAssApNamePre based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechStaAssApNamePre_Type.__name__ = "DisplayString"
_QtechStaAssApNamePre_Object = MibTableColumn
qtechStaAssApNamePre = _QtechStaAssApNamePre_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 8),
    _QtechStaAssApNamePre_Type()
)
qtechStaAssApNamePre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssApNamePre.setStatus("current")


class _QtechStaAssApNameNow_Type(DisplayString):
    """Custom type qtechStaAssApNameNow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechStaAssApNameNow_Type.__name__ = "DisplayString"
_QtechStaAssApNameNow_Object = MibTableColumn
qtechStaAssApNameNow = _QtechStaAssApNameNow_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 9),
    _QtechStaAssApNameNow_Type()
)
qtechStaAssApNameNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssApNameNow.setStatus("current")
_QtechStaAssSignalQua_Type = Integer32
_QtechStaAssSignalQua_Object = MibTableColumn
qtechStaAssSignalQua = _QtechStaAssSignalQua_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 10),
    _QtechStaAssSignalQua_Type()
)
qtechStaAssSignalQua.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssSignalQua.setStatus("current")
_QtechStaAssRoamtype_Type = Integer32
_QtechStaAssRoamtype_Object = MibTableColumn
qtechStaAssRoamtype = _QtechStaAssRoamtype_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 11),
    _QtechStaAssRoamtype_Type()
)
qtechStaAssRoamtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssRoamtype.setStatus("current")
_QtechStaAssjitter_Type = Integer32
_QtechStaAssjitter_Object = MibTableColumn
qtechStaAssjitter = _QtechStaAssjitter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 12),
    _QtechStaAssjitter_Type()
)
qtechStaAssjitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssjitter.setStatus("current")
_QtechStaAssjointimes_Type = Unsigned32
_QtechStaAssjointimes_Object = MibTableColumn
qtechStaAssjointimes = _QtechStaAssjointimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 13),
    _QtechStaAssjointimes_Type()
)
qtechStaAssjointimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssjointimes.setStatus("current")
_QtechStaAsslatelytime_Type = DateAndTime
_QtechStaAsslatelytime_Object = MibTableColumn
qtechStaAsslatelytime = _QtechStaAsslatelytime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 14),
    _QtechStaAsslatelytime_Type()
)
qtechStaAsslatelytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAsslatelytime.setStatus("current")
_QtechStaAssSSID_Type = DisplayString
_QtechStaAssSSID_Object = MibTableColumn
qtechStaAssSSID = _QtechStaAssSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 2, 1, 1, 15),
    _QtechStaAssSSID_Type()
)
qtechStaAssSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAssSSID.setStatus("current")
_QtechStaAssRecordsByTime_ObjectIdentity = ObjectIdentity
qtechStaAssRecordsByTime = _QtechStaAssRecordsByTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3)
)
_QtechStaAssRecordsSearchByTimeTable_Object = MibTable
qtechStaAssRecordsSearchByTimeTable = _QtechStaAssRecordsSearchByTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsSearchByTimeTable.setStatus("current")
_QtechStaAssRecordsSearchByTimeEntry_Object = MibTableRow
qtechStaAssRecordsSearchByTimeEntry = _QtechStaAssRecordsSearchByTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1)
)
qtechStaAssRecordsSearchByTimeEntry.setIndexNames(
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaUptimeLow"),
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaUptimeHigh"),
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaDowntimeLow"),
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaDowntimeHigh"),
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimeindex"),
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsSearchByTimeEntry.setStatus("current")
_QtechStaUptimeLow_Type = DateAndTime
_QtechStaUptimeLow_Object = MibTableColumn
qtechStaUptimeLow = _QtechStaUptimeLow_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 1),
    _QtechStaUptimeLow_Type()
)
qtechStaUptimeLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaUptimeLow.setStatus("current")
_QtechStaUptimeHigh_Type = DateAndTime
_QtechStaUptimeHigh_Object = MibTableColumn
qtechStaUptimeHigh = _QtechStaUptimeHigh_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 2),
    _QtechStaUptimeHigh_Type()
)
qtechStaUptimeHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaUptimeHigh.setStatus("current")
_QtechStaDowntimeLow_Type = DateAndTime
_QtechStaDowntimeLow_Object = MibTableColumn
qtechStaDowntimeLow = _QtechStaDowntimeLow_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 3),
    _QtechStaDowntimeLow_Type()
)
qtechStaDowntimeLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaDowntimeLow.setStatus("current")
_QtechStaDowntimeHigh_Type = DateAndTime
_QtechStaDowntimeHigh_Object = MibTableColumn
qtechStaDowntimeHigh = _QtechStaDowntimeHigh_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 4),
    _QtechStaDowntimeHigh_Type()
)
qtechStaDowntimeHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaDowntimeHigh.setStatus("current")
_QtechStaTimeindex_Type = Unsigned32
_QtechStaTimeindex_Object = MibTableColumn
qtechStaTimeindex = _QtechStaTimeindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 5),
    _QtechStaTimeindex_Type()
)
qtechStaTimeindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaTimeindex.setStatus("current")
_QtechStaTimeMac_Type = MacAddress
_QtechStaTimeMac_Object = MibTableColumn
qtechStaTimeMac = _QtechStaTimeMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 6),
    _QtechStaTimeMac_Type()
)
qtechStaTimeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimeMac.setStatus("current")


class _QtechStaTimeAPName_Type(DisplayString):
    """Custom type qtechStaTimeAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechStaTimeAPName_Type.__name__ = "DisplayString"
_QtechStaTimeAPName_Object = MibTableColumn
qtechStaTimeAPName = _QtechStaTimeAPName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 7),
    _QtechStaTimeAPName_Type()
)
qtechStaTimeAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimeAPName.setStatus("current")


class _QtechStaTimeISUP_Type(Integer32):
    """Custom type qtechStaTimeISUP based on Integer32"""
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


_QtechStaTimeISUP_Type.__name__ = "Integer32"
_QtechStaTimeISUP_Object = MibTableColumn
qtechStaTimeISUP = _QtechStaTimeISUP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 8),
    _QtechStaTimeISUP_Type()
)
qtechStaTimeISUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimeISUP.setStatus("current")
_QtechStaTimeStartime_Type = DateAndTime
_QtechStaTimeStartime_Object = MibTableColumn
qtechStaTimeStartime = _QtechStaTimeStartime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 9),
    _QtechStaTimeStartime_Type()
)
qtechStaTimeStartime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimeStartime.setStatus("current")
_QtechStaTimeupdowntimes_Type = Unsigned32
_QtechStaTimeupdowntimes_Object = MibTableColumn
qtechStaTimeupdowntimes = _QtechStaTimeupdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 10),
    _QtechStaTimeupdowntimes_Type()
)
qtechStaTimeupdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimeupdowntimes.setStatus("current")
_QtechStaTimeroamtimes_Type = Unsigned32
_QtechStaTimeroamtimes_Object = MibTableColumn
qtechStaTimeroamtimes = _QtechStaTimeroamtimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 11),
    _QtechStaTimeroamtimes_Type()
)
qtechStaTimeroamtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimeroamtimes.setStatus("current")
_QtechStaTimertotaltimes_Type = Unsigned32
_QtechStaTimertotaltimes_Object = MibTableColumn
qtechStaTimertotaltimes = _QtechStaTimertotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 12),
    _QtechStaTimertotaltimes_Type()
)
qtechStaTimertotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimertotaltimes.setStatus("current")
_QtechStaTimerjitter_Type = Integer32
_QtechStaTimerjitter_Object = MibTableColumn
qtechStaTimerjitter = _QtechStaTimerjitter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 13),
    _QtechStaTimerjitter_Type()
)
qtechStaTimerjitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimerjitter.setStatus("current")
_QtechStaTimerjointimes_Type = Unsigned32
_QtechStaTimerjointimes_Object = MibTableColumn
qtechStaTimerjointimes = _QtechStaTimerjointimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 14),
    _QtechStaTimerjointimes_Type()
)
qtechStaTimerjointimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimerjointimes.setStatus("current")
_QtechStaTimerlatelytime_Type = DateAndTime
_QtechStaTimerlatelytime_Object = MibTableColumn
qtechStaTimerlatelytime = _QtechStaTimerlatelytime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 15),
    _QtechStaTimerlatelytime_Type()
)
qtechStaTimerlatelytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimerlatelytime.setStatus("current")
_QtechStaTimerSSID_Type = DisplayString
_QtechStaTimerSSID_Object = MibTableColumn
qtechStaTimerSSID = _QtechStaTimerSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 3, 1, 1, 16),
    _QtechStaTimerSSID_Type()
)
qtechStaTimerSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaTimerSSID.setStatus("current")
_QtechStaAssRecordsByAP_ObjectIdentity = ObjectIdentity
qtechStaAssRecordsByAP = _QtechStaAssRecordsByAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4)
)
_QtechStaAssRecordsSearchByAPTable_Object = MibTable
qtechStaAssRecordsSearchByAPTable = _QtechStaAssRecordsSearchByAPTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsSearchByAPTable.setStatus("current")
_QtechStaAssRecordsSearchByAPEntry_Object = MibTableRow
qtechStaAssRecordsSearchByAPEntry = _QtechStaAssRecordsSearchByAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1)
)
qtechStaAssRecordsSearchByAPEntry.setIndexNames(
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPAPName"),
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPindex"),
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsSearchByAPEntry.setStatus("current")


class _QtechStaAPAPName_Type(DisplayString):
    """Custom type qtechStaAPAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechStaAPAPName_Type.__name__ = "DisplayString"
_QtechStaAPAPName_Object = MibTableColumn
qtechStaAPAPName = _QtechStaAPAPName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 1),
    _QtechStaAPAPName_Type()
)
qtechStaAPAPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaAPAPName.setStatus("current")
_QtechStaAPindex_Type = Unsigned32
_QtechStaAPindex_Object = MibTableColumn
qtechStaAPindex = _QtechStaAPindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 2),
    _QtechStaAPindex_Type()
)
qtechStaAPindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaAPindex.setStatus("current")
_QtechStaAPMac_Type = MacAddress
_QtechStaAPMac_Object = MibTableColumn
qtechStaAPMac = _QtechStaAPMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 3),
    _QtechStaAPMac_Type()
)
qtechStaAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAPMac.setStatus("current")


class _QtechStaAPISUP_Type(Integer32):
    """Custom type qtechStaAPISUP based on Integer32"""
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


_QtechStaAPISUP_Type.__name__ = "Integer32"
_QtechStaAPISUP_Object = MibTableColumn
qtechStaAPISUP = _QtechStaAPISUP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 4),
    _QtechStaAPISUP_Type()
)
qtechStaAPISUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAPISUP.setStatus("current")
_QtechStaAPStartime_Type = DateAndTime
_QtechStaAPStartime_Object = MibTableColumn
qtechStaAPStartime = _QtechStaAPStartime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 5),
    _QtechStaAPStartime_Type()
)
qtechStaAPStartime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAPStartime.setStatus("current")
_QtechStaAPupdowntimes_Type = Unsigned32
_QtechStaAPupdowntimes_Object = MibTableColumn
qtechStaAPupdowntimes = _QtechStaAPupdowntimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 6),
    _QtechStaAPupdowntimes_Type()
)
qtechStaAPupdowntimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAPupdowntimes.setStatus("current")
_QtechStaAProamtimes_Type = Unsigned32
_QtechStaAProamtimes_Object = MibTableColumn
qtechStaAProamtimes = _QtechStaAProamtimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 7),
    _QtechStaAProamtimes_Type()
)
qtechStaAProamtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAProamtimes.setStatus("current")
_QtechStaAPtotaltimes_Type = Unsigned32
_QtechStaAPtotaltimes_Object = MibTableColumn
qtechStaAPtotaltimes = _QtechStaAPtotaltimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 8),
    _QtechStaAPtotaltimes_Type()
)
qtechStaAPtotaltimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAPtotaltimes.setStatus("current")
_QtechStaAPjitter_Type = Integer32
_QtechStaAPjitter_Object = MibTableColumn
qtechStaAPjitter = _QtechStaAPjitter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 9),
    _QtechStaAPjitter_Type()
)
qtechStaAPjitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAPjitter.setStatus("current")
_QtechStaAPjointimes_Type = Unsigned32
_QtechStaAPjointimes_Object = MibTableColumn
qtechStaAPjointimes = _QtechStaAPjointimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 10),
    _QtechStaAPjointimes_Type()
)
qtechStaAPjointimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAPjointimes.setStatus("current")
_QtechStaAPlatelytime_Type = DateAndTime
_QtechStaAPlatelytime_Object = MibTableColumn
qtechStaAPlatelytime = _QtechStaAPlatelytime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 11),
    _QtechStaAPlatelytime_Type()
)
qtechStaAPlatelytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAPlatelytime.setStatus("current")
_QtechStaAPSSID_Type = DisplayString
_QtechStaAPSSID_Object = MibTableColumn
qtechStaAPSSID = _QtechStaAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 4, 1, 1, 12),
    _QtechStaAPSSID_Type()
)
qtechStaAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaAPSSID.setStatus("current")
_QtechStaAssSignalByMAC_ObjectIdentity = ObjectIdentity
qtechStaAssSignalByMAC = _QtechStaAssSignalByMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 5)
)
_QtechStaAssSignalByMACTable_Object = MibTable
qtechStaAssSignalByMACTable = _QtechStaAssSignalByMACTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 5, 1)
)
if mibBuilder.loadTexts:
    qtechStaAssSignalByMACTable.setStatus("current")
_QtechStaAssSignalByMACEntry_Object = MibTableRow
qtechStaAssSignalByMACEntry = _QtechStaAssSignalByMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 5, 1, 1)
)
qtechStaAssSignalByMACEntry.setIndexNames(
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaSignalMacAddress"),
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaSignalMacindex"),
)
if mibBuilder.loadTexts:
    qtechStaAssSignalByMACEntry.setStatus("current")
_QtechStaSignalMacAddress_Type = MacAddress
_QtechStaSignalMacAddress_Object = MibTableColumn
qtechStaSignalMacAddress = _QtechStaSignalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 5, 1, 1, 1),
    _QtechStaSignalMacAddress_Type()
)
qtechStaSignalMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaSignalMacAddress.setStatus("current")
_QtechStaSignalMacindex_Type = Unsigned32
_QtechStaSignalMacindex_Object = MibTableColumn
qtechStaSignalMacindex = _QtechStaSignalMacindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 5, 1, 1, 2),
    _QtechStaSignalMacindex_Type()
)
qtechStaSignalMacindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaSignalMacindex.setStatus("current")
_QtechStaSignaltime_Type = DateAndTime
_QtechStaSignaltime_Object = MibTableColumn
qtechStaSignaltime = _QtechStaSignaltime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 5, 1, 1, 3),
    _QtechStaSignaltime_Type()
)
qtechStaSignaltime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaSignaltime.setStatus("current")
_QtechStaSignalValue_Type = Integer32
_QtechStaSignalValue_Object = MibTableColumn
qtechStaSignalValue = _QtechStaSignalValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 5, 1, 1, 4),
    _QtechStaSignalValue_Type()
)
qtechStaSignalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaSignalValue.setStatus("current")
_QtechStaAssRetryByMAC_ObjectIdentity = ObjectIdentity
qtechStaAssRetryByMAC = _QtechStaAssRetryByMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 6)
)
_QtechStaAssRetryByMACTable_Object = MibTable
qtechStaAssRetryByMACTable = _QtechStaAssRetryByMACTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 6, 1)
)
if mibBuilder.loadTexts:
    qtechStaAssRetryByMACTable.setStatus("current")
_QtechStaAssRetryByMACEntry_Object = MibTableRow
qtechStaAssRetryByMACEntry = _QtechStaAssRetryByMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 6, 1, 1)
)
qtechStaAssRetryByMACEntry.setIndexNames(
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaRetryMacAddress"),
    (0, "QTECH-STA-ASS-RECORDS-MIB", "qtechStaRetryMacindex"),
)
if mibBuilder.loadTexts:
    qtechStaAssRetryByMACEntry.setStatus("current")
_QtechStaRetryMacAddress_Type = MacAddress
_QtechStaRetryMacAddress_Object = MibTableColumn
qtechStaRetryMacAddress = _QtechStaRetryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 6, 1, 1, 1),
    _QtechStaRetryMacAddress_Type()
)
qtechStaRetryMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaRetryMacAddress.setStatus("current")
_QtechStaRetryMacindex_Type = Unsigned32
_QtechStaRetryMacindex_Object = MibTableColumn
qtechStaRetryMacindex = _QtechStaRetryMacindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 6, 1, 1, 2),
    _QtechStaRetryMacindex_Type()
)
qtechStaRetryMacindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechStaRetryMacindex.setStatus("current")
_QtechStaRetrytime_Type = DateAndTime
_QtechStaRetrytime_Object = MibTableColumn
qtechStaRetrytime = _QtechStaRetrytime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 6, 1, 1, 3),
    _QtechStaRetrytime_Type()
)
qtechStaRetrytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaRetrytime.setStatus("current")
_QtechStaRetryValue_Type = Integer32
_QtechStaRetryValue_Object = MibTableColumn
qtechStaRetryValue = _QtechStaRetryValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 6, 1, 1, 4),
    _QtechStaRetryValue_Type()
)
qtechStaRetryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaRetryValue.setStatus("current")
_QtechStaAssStatistic_ObjectIdentity = ObjectIdentity
qtechStaAssStatistic = _QtechStaAssStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 7)
)
_QtechAssStatisticsTotalsta_Type = Unsigned32
_QtechAssStatisticsTotalsta_Object = MibScalar
qtechAssStatisticsTotalsta = _QtechAssStatisticsTotalsta_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 7, 1),
    _QtechAssStatisticsTotalsta_Type()
)
qtechAssStatisticsTotalsta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAssStatisticsTotalsta.setStatus("current")
_QtechAssStatisticsTotalinfo_Type = Unsigned32
_QtechAssStatisticsTotalinfo_Object = MibScalar
qtechAssStatisticsTotalinfo = _QtechAssStatisticsTotalinfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 7, 2),
    _QtechAssStatisticsTotalinfo_Type()
)
qtechAssStatisticsTotalinfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAssStatisticsTotalinfo.setStatus("current")
_QtechAssStatisticsdown_Type = Unsigned32
_QtechAssStatisticsdown_Object = MibScalar
qtechAssStatisticsdown = _QtechAssStatisticsdown_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 7, 3),
    _QtechAssStatisticsdown_Type()
)
qtechAssStatisticsdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAssStatisticsdown.setStatus("current")
_QtechAssStatisticsObligate1_Type = Unsigned32
_QtechAssStatisticsObligate1_Object = MibScalar
qtechAssStatisticsObligate1 = _QtechAssStatisticsObligate1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 7, 4),
    _QtechAssStatisticsObligate1_Type()
)
qtechAssStatisticsObligate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAssStatisticsObligate1.setStatus("current")
_QtechAssStatisticsObligate2_Type = Unsigned32
_QtechAssStatisticsObligate2_Object = MibScalar
qtechAssStatisticsObligate2 = _QtechAssStatisticsObligate2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 7, 5),
    _QtechAssStatisticsObligate2_Type()
)
qtechAssStatisticsObligate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAssStatisticsObligate2.setStatus("current")
_QtechAssStatisticsObligate3_Type = Unsigned32
_QtechAssStatisticsObligate3_Object = MibScalar
qtechAssStatisticsObligate3 = _QtechAssStatisticsObligate3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 1, 7, 6),
    _QtechAssStatisticsObligate3_Type()
)
qtechAssStatisticsObligate3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAssStatisticsObligate3.setStatus("current")
_QtechStaAssRecordsMIBConformance_ObjectIdentity = ObjectIdentity
qtechStaAssRecordsMIBConformance = _QtechStaAssRecordsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2)
)
_QtechStaAssRecordsMIBCompliances_ObjectIdentity = ObjectIdentity
qtechStaAssRecordsMIBCompliances = _QtechStaAssRecordsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 1)
)
_QtechStaAssRecordsMIBGroups_ObjectIdentity = ObjectIdentity
qtechStaAssRecordsMIBGroups = _QtechStaAssRecordsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 2)
)

# Managed Objects groups

qtechStaAssRecordsGrobalMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 2, 1)
)
qtechStaAssRecordsGrobalMIBroup.setObjects(
      *(("QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacGrobalAPName"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacGrobalISUP"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacGrobalStartime"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacGrobalupdowntimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacGrobalroamtimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacGrobaltotaltimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacGrobalrealdowntimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaMacGrobalSSID"))
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsGrobalMIBroup.setStatus("current")

qtechStaAssRecordsMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 2, 2)
)
qtechStaAssRecordsMIBroup.setObjects(
      *(("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAsstime"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssAction"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssSubAction"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssResult"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssReason"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssApNamePre"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssApNameNow"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssSignalQua"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssRoamtype"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssjitter"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssjointimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAsslatelytime"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssSSID"))
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsMIBroup.setStatus("current")

qtechStaAssRecordsSearchByTimeMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 2, 3)
)
qtechStaAssRecordsSearchByTimeMIBroup.setObjects(
      *(("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimeMac"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimeAPName"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimeISUP"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimeStartime"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimeupdowntimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimeroamtimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimertotaltimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimerjitter"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimerjointimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimerlatelytime"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaTimerSSID"))
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsSearchByTimeMIBroup.setStatus("current")

qtechStaAssRecordsSearchByAPMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 2, 4)
)
qtechStaAssRecordsSearchByAPMIBroup.setObjects(
      *(("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPMac"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPISUP"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPStartime"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPupdowntimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAProamtimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPtotaltimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPjitter"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPjointimes"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPlatelytime"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAPSSID"))
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsSearchByAPMIBroup.setStatus("current")

qtechStaAssSignalSearchByMACMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 2, 5)
)
qtechStaAssSignalSearchByMACMIBroup.setObjects(
      *(("QTECH-STA-ASS-RECORDS-MIB", "qtechStaSignaltime"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaSignalValue"))
)
if mibBuilder.loadTexts:
    qtechStaAssSignalSearchByMACMIBroup.setStatus("current")

qtechStaAssRetrySearchByMACMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 2, 6)
)
qtechStaAssRetrySearchByMACMIBroup.setObjects(
      *(("QTECH-STA-ASS-RECORDS-MIB", "qtechStaRetrytime"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaRetryValue"))
)
if mibBuilder.loadTexts:
    qtechStaAssRetrySearchByMACMIBroup.setStatus("current")

qtechStaAssStatisticsMIBroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 2, 7)
)
qtechStaAssStatisticsMIBroup.setObjects(
      *(("QTECH-STA-ASS-RECORDS-MIB", "qtechAssStatisticsTotalsta"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechAssStatisticsTotalinfo"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechAssStatisticsdown"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechAssStatisticsObligate1"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechAssStatisticsObligate2"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechAssStatisticsObligate3"))
)
if mibBuilder.loadTexts:
    qtechStaAssStatisticsMIBroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechStaAssRecordsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 101, 2, 1, 1)
)
qtechStaAssRecordsMIBCompliance.setObjects(
      *(("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssRecordsGrobalMIBroup"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssRecordsMIBroup"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssRecordsSearchByTimeMIBroup"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssRecordsSearchByAPMIBroup"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssSignalSearchByMACMIBroup"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssRetrySearchByMACMIBroup"),
        ("QTECH-STA-ASS-RECORDS-MIB", "qtechStaAssStatisticsMIBroup"))
)
if mibBuilder.loadTexts:
    qtechStaAssRecordsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-STA-ASS-RECORDS-MIB",
    **{"qtechStaAssRecordsMIB": qtechStaAssRecordsMIB,
       "qtechStaAssRecordsMIBTrap": qtechStaAssRecordsMIBTrap,
       "qtechStaAssRecordsMIBObjects": qtechStaAssRecordsMIBObjects,
       "qtechStaAssRecordsGrobal": qtechStaAssRecordsGrobal,
       "qtechStaAssRecordsGrobalTable": qtechStaAssRecordsGrobalTable,
       "qtechStaAssRecordsGrobalEntry": qtechStaAssRecordsGrobalEntry,
       "qtechStaMacGrobalAddress": qtechStaMacGrobalAddress,
       "qtechStaMacGrobalAPName": qtechStaMacGrobalAPName,
       "qtechStaMacGrobalISUP": qtechStaMacGrobalISUP,
       "qtechStaMacGrobalStartime": qtechStaMacGrobalStartime,
       "qtechStaMacGrobalupdowntimes": qtechStaMacGrobalupdowntimes,
       "qtechStaMacGrobalroamtimes": qtechStaMacGrobalroamtimes,
       "qtechStaMacGrobaltotaltimes": qtechStaMacGrobaltotaltimes,
       "qtechStaMacGrobalrealdowntimes": qtechStaMacGrobalrealdowntimes,
       "qtechStaMacGrobalSSID": qtechStaMacGrobalSSID,
       "qtechStaAssRecordsByMAC": qtechStaAssRecordsByMAC,
       "qtechStaAssRecordsByMACTable": qtechStaAssRecordsByMACTable,
       "qtechStaAssRecordsByMACEntry": qtechStaAssRecordsByMACEntry,
       "qtechStaMacAddress": qtechStaMacAddress,
       "qtechStaMacindex": qtechStaMacindex,
       "qtechStaAsstime": qtechStaAsstime,
       "qtechStaAssAction": qtechStaAssAction,
       "qtechStaAssSubAction": qtechStaAssSubAction,
       "qtechStaAssResult": qtechStaAssResult,
       "qtechStaAssReason": qtechStaAssReason,
       "qtechStaAssApNamePre": qtechStaAssApNamePre,
       "qtechStaAssApNameNow": qtechStaAssApNameNow,
       "qtechStaAssSignalQua": qtechStaAssSignalQua,
       "qtechStaAssRoamtype": qtechStaAssRoamtype,
       "qtechStaAssjitter": qtechStaAssjitter,
       "qtechStaAssjointimes": qtechStaAssjointimes,
       "qtechStaAsslatelytime": qtechStaAsslatelytime,
       "qtechStaAssSSID": qtechStaAssSSID,
       "qtechStaAssRecordsByTime": qtechStaAssRecordsByTime,
       "qtechStaAssRecordsSearchByTimeTable": qtechStaAssRecordsSearchByTimeTable,
       "qtechStaAssRecordsSearchByTimeEntry": qtechStaAssRecordsSearchByTimeEntry,
       "qtechStaUptimeLow": qtechStaUptimeLow,
       "qtechStaUptimeHigh": qtechStaUptimeHigh,
       "qtechStaDowntimeLow": qtechStaDowntimeLow,
       "qtechStaDowntimeHigh": qtechStaDowntimeHigh,
       "qtechStaTimeindex": qtechStaTimeindex,
       "qtechStaTimeMac": qtechStaTimeMac,
       "qtechStaTimeAPName": qtechStaTimeAPName,
       "qtechStaTimeISUP": qtechStaTimeISUP,
       "qtechStaTimeStartime": qtechStaTimeStartime,
       "qtechStaTimeupdowntimes": qtechStaTimeupdowntimes,
       "qtechStaTimeroamtimes": qtechStaTimeroamtimes,
       "qtechStaTimertotaltimes": qtechStaTimertotaltimes,
       "qtechStaTimerjitter": qtechStaTimerjitter,
       "qtechStaTimerjointimes": qtechStaTimerjointimes,
       "qtechStaTimerlatelytime": qtechStaTimerlatelytime,
       "qtechStaTimerSSID": qtechStaTimerSSID,
       "qtechStaAssRecordsByAP": qtechStaAssRecordsByAP,
       "qtechStaAssRecordsSearchByAPTable": qtechStaAssRecordsSearchByAPTable,
       "qtechStaAssRecordsSearchByAPEntry": qtechStaAssRecordsSearchByAPEntry,
       "qtechStaAPAPName": qtechStaAPAPName,
       "qtechStaAPindex": qtechStaAPindex,
       "qtechStaAPMac": qtechStaAPMac,
       "qtechStaAPISUP": qtechStaAPISUP,
       "qtechStaAPStartime": qtechStaAPStartime,
       "qtechStaAPupdowntimes": qtechStaAPupdowntimes,
       "qtechStaAProamtimes": qtechStaAProamtimes,
       "qtechStaAPtotaltimes": qtechStaAPtotaltimes,
       "qtechStaAPjitter": qtechStaAPjitter,
       "qtechStaAPjointimes": qtechStaAPjointimes,
       "qtechStaAPlatelytime": qtechStaAPlatelytime,
       "qtechStaAPSSID": qtechStaAPSSID,
       "qtechStaAssSignalByMAC": qtechStaAssSignalByMAC,
       "qtechStaAssSignalByMACTable": qtechStaAssSignalByMACTable,
       "qtechStaAssSignalByMACEntry": qtechStaAssSignalByMACEntry,
       "qtechStaSignalMacAddress": qtechStaSignalMacAddress,
       "qtechStaSignalMacindex": qtechStaSignalMacindex,
       "qtechStaSignaltime": qtechStaSignaltime,
       "qtechStaSignalValue": qtechStaSignalValue,
       "qtechStaAssRetryByMAC": qtechStaAssRetryByMAC,
       "qtechStaAssRetryByMACTable": qtechStaAssRetryByMACTable,
       "qtechStaAssRetryByMACEntry": qtechStaAssRetryByMACEntry,
       "qtechStaRetryMacAddress": qtechStaRetryMacAddress,
       "qtechStaRetryMacindex": qtechStaRetryMacindex,
       "qtechStaRetrytime": qtechStaRetrytime,
       "qtechStaRetryValue": qtechStaRetryValue,
       "qtechStaAssStatistic": qtechStaAssStatistic,
       "qtechAssStatisticsTotalsta": qtechAssStatisticsTotalsta,
       "qtechAssStatisticsTotalinfo": qtechAssStatisticsTotalinfo,
       "qtechAssStatisticsdown": qtechAssStatisticsdown,
       "qtechAssStatisticsObligate1": qtechAssStatisticsObligate1,
       "qtechAssStatisticsObligate2": qtechAssStatisticsObligate2,
       "qtechAssStatisticsObligate3": qtechAssStatisticsObligate3,
       "qtechStaAssRecordsMIBConformance": qtechStaAssRecordsMIBConformance,
       "qtechStaAssRecordsMIBCompliances": qtechStaAssRecordsMIBCompliances,
       "qtechStaAssRecordsMIBCompliance": qtechStaAssRecordsMIBCompliance,
       "qtechStaAssRecordsMIBGroups": qtechStaAssRecordsMIBGroups,
       "qtechStaAssRecordsGrobalMIBroup": qtechStaAssRecordsGrobalMIBroup,
       "qtechStaAssRecordsMIBroup": qtechStaAssRecordsMIBroup,
       "qtechStaAssRecordsSearchByTimeMIBroup": qtechStaAssRecordsSearchByTimeMIBroup,
       "qtechStaAssRecordsSearchByAPMIBroup": qtechStaAssRecordsSearchByAPMIBroup,
       "qtechStaAssSignalSearchByMACMIBroup": qtechStaAssSignalSearchByMACMIBroup,
       "qtechStaAssRetrySearchByMACMIBroup": qtechStaAssRetrySearchByMACMIBroup,
       "qtechStaAssStatisticsMIBroup": qtechStaAssStatisticsMIBroup}
)
