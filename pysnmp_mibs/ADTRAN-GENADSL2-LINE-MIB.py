# SNMP MIB module (ADTRAN-GENADSL2-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENADSL2-LINE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:11 2025
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

(adGenAdsl2,
 adGenAdsl2ID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-ADSL2-MIB",
    "adGenAdsl2",
    "adGenAdsl2ID")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenAdslID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 82, 1, 1)
)
if mibBuilder.loadTexts:
    adGenAdslID.setRevisions(
        ("2012-01-19 15:00",
         "2011-12-22 00:00",
         "2011-10-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAdsl2PM_ObjectIdentity = ObjectIdentity
adGenAdsl2PM = _AdGenAdsl2PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1)
)
_AdGenAdsl2Atuc1DayIntervalTable_Object = MibTable
adGenAdsl2Atuc1DayIntervalTable = _AdGenAdsl2Atuc1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalTable.setStatus("current")
_AdGenAdsl2Atuc1DayIntervalEntry_Object = MibTableRow
adGenAdsl2Atuc1DayIntervalEntry = _AdGenAdsl2Atuc1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1)
)
adGenAdsl2Atuc1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalEntry.setStatus("current")


class _AdGenAdsl2Atuc1DayIntervalNumber_Type(Integer32):
    """Custom type adGenAdsl2Atuc1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenAdsl2Atuc1DayIntervalNumber_Type.__name__ = "Integer32"
_AdGenAdsl2Atuc1DayIntervalNumber_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalNumber = _AdGenAdsl2Atuc1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 1),
    _AdGenAdsl2Atuc1DayIntervalNumber_Type()
)
adGenAdsl2Atuc1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalNumber.setStatus("current")


class _AdGenAdsl2Atuc1DayIntervalValidData_Type(Integer32):
    """Custom type adGenAdsl2Atuc1DayIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenAdsl2Atuc1DayIntervalValidData_Type.__name__ = "Integer32"
_AdGenAdsl2Atuc1DayIntervalValidData_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalValidData = _AdGenAdsl2Atuc1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 2),
    _AdGenAdsl2Atuc1DayIntervalValidData_Type()
)
adGenAdsl2Atuc1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalValidData.setStatus("current")
_AdGenAdsl2Atuc1DayIntervalMoniSecs_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalMoniSecs_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalMoniSecs = _AdGenAdsl2Atuc1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 3),
    _AdGenAdsl2Atuc1DayIntervalMoniSecs_Type()
)
adGenAdsl2Atuc1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalMoniSecs.setUnits("seconds")
_AdGenAdsl2Atuc1DayIntervalLofs_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalLofs_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalLofs = _AdGenAdsl2Atuc1DayIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 4),
    _AdGenAdsl2Atuc1DayIntervalLofs_Type()
)
adGenAdsl2Atuc1DayIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalLofs.setUnits("seconds")
_AdGenAdsl2Atuc1DayIntervalLoss_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalLoss_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalLoss = _AdGenAdsl2Atuc1DayIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 5),
    _AdGenAdsl2Atuc1DayIntervalLoss_Type()
)
adGenAdsl2Atuc1DayIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalLoss.setUnits("seconds")
_AdGenAdsl2Atuc1DayIntervalLols_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalLols_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalLols = _AdGenAdsl2Atuc1DayIntervalLols_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 6),
    _AdGenAdsl2Atuc1DayIntervalLols_Type()
)
adGenAdsl2Atuc1DayIntervalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalLols.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalLols.setUnits("seconds")
_AdGenAdsl2Atuc1DayIntervalES_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalES_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalES = _AdGenAdsl2Atuc1DayIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 7),
    _AdGenAdsl2Atuc1DayIntervalES_Type()
)
adGenAdsl2Atuc1DayIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalES.setUnits("seconds")
_AdGenAdsl2Atuc1DayIntervalInits_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalInits_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalInits = _AdGenAdsl2Atuc1DayIntervalInits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 8),
    _AdGenAdsl2Atuc1DayIntervalInits_Type()
)
adGenAdsl2Atuc1DayIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalInits.setStatus("current")
_AdGenAdsl2Atuc1DayIntervalCorrectedBlks_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalCorrectedBlks_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalCorrectedBlks = _AdGenAdsl2Atuc1DayIntervalCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 9),
    _AdGenAdsl2Atuc1DayIntervalCorrectedBlks_Type()
)
adGenAdsl2Atuc1DayIntervalCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalCorrectedBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalCorrectedBlks.setUnits("blocks")
_AdGenAdsl2Atuc1DayIntervalUncorrectedBlks_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalUncorrectedBlks_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalUncorrectedBlks = _AdGenAdsl2Atuc1DayIntervalUncorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 10),
    _AdGenAdsl2Atuc1DayIntervalUncorrectedBlks_Type()
)
adGenAdsl2Atuc1DayIntervalUncorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalUncorrectedBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalUncorrectedBlks.setUnits("blocks")
_AdGenAdsl2Atuc1DayIntervalTxBlks_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalTxBlks_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalTxBlks = _AdGenAdsl2Atuc1DayIntervalTxBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 11),
    _AdGenAdsl2Atuc1DayIntervalTxBlks_Type()
)
adGenAdsl2Atuc1DayIntervalTxBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalTxBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalTxBlks.setUnits("blocks")
_AdGenAdsl2Atuc1DayIntervalRxBlks_Type = Counter32
_AdGenAdsl2Atuc1DayIntervalRxBlks_Object = MibTableColumn
adGenAdsl2Atuc1DayIntervalRxBlks = _AdGenAdsl2Atuc1DayIntervalRxBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 1, 1, 12),
    _AdGenAdsl2Atuc1DayIntervalRxBlks_Type()
)
adGenAdsl2Atuc1DayIntervalRxBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalRxBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayIntervalRxBlks.setUnits("blocks")
_AdGenAdsl2Atur1DayIntervalTable_Object = MibTable
adGenAdsl2Atur1DayIntervalTable = _AdGenAdsl2Atur1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2)
)
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalTable.setStatus("current")
_AdGenAdsl2Atur1DayIntervalEntry_Object = MibTableRow
adGenAdsl2Atur1DayIntervalEntry = _AdGenAdsl2Atur1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1)
)
adGenAdsl2Atur1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalEntry.setStatus("current")


class _AdGenAdsl2Atur1DayIntervalNumber_Type(Integer32):
    """Custom type adGenAdsl2Atur1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenAdsl2Atur1DayIntervalNumber_Type.__name__ = "Integer32"
_AdGenAdsl2Atur1DayIntervalNumber_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalNumber = _AdGenAdsl2Atur1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 1),
    _AdGenAdsl2Atur1DayIntervalNumber_Type()
)
adGenAdsl2Atur1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalNumber.setStatus("current")


class _AdGenAdsl2Atur1DayIntervalValidData_Type(Integer32):
    """Custom type adGenAdsl2Atur1DayIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenAdsl2Atur1DayIntervalValidData_Type.__name__ = "Integer32"
_AdGenAdsl2Atur1DayIntervalValidData_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalValidData = _AdGenAdsl2Atur1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 2),
    _AdGenAdsl2Atur1DayIntervalValidData_Type()
)
adGenAdsl2Atur1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalValidData.setStatus("current")
_AdGenAdsl2Atur1DayIntervalMoniSecs_Type = Counter32
_AdGenAdsl2Atur1DayIntervalMoniSecs_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalMoniSecs = _AdGenAdsl2Atur1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 3),
    _AdGenAdsl2Atur1DayIntervalMoniSecs_Type()
)
adGenAdsl2Atur1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalMoniSecs.setUnits("seconds")
_AdGenAdsl2Atur1DayIntervalLofs_Type = Counter32
_AdGenAdsl2Atur1DayIntervalLofs_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalLofs = _AdGenAdsl2Atur1DayIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 4),
    _AdGenAdsl2Atur1DayIntervalLofs_Type()
)
adGenAdsl2Atur1DayIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalLofs.setUnits("seconds")
_AdGenAdsl2Atur1DayIntervalLoss_Type = Counter32
_AdGenAdsl2Atur1DayIntervalLoss_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalLoss = _AdGenAdsl2Atur1DayIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 5),
    _AdGenAdsl2Atur1DayIntervalLoss_Type()
)
adGenAdsl2Atur1DayIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalLoss.setUnits("seconds")
_AdGenAdsl2Atur1DayIntervalLprs_Type = Counter32
_AdGenAdsl2Atur1DayIntervalLprs_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalLprs = _AdGenAdsl2Atur1DayIntervalLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 6),
    _AdGenAdsl2Atur1DayIntervalLprs_Type()
)
adGenAdsl2Atur1DayIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalLprs.setUnits("seconds")
_AdGenAdsl2Atur1DayIntervalES_Type = Counter32
_AdGenAdsl2Atur1DayIntervalES_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalES = _AdGenAdsl2Atur1DayIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 7),
    _AdGenAdsl2Atur1DayIntervalES_Type()
)
adGenAdsl2Atur1DayIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalES.setUnits("seconds")
_AdGenAdsl2Atur1DayIntervalCorrectedBlks_Type = Counter32
_AdGenAdsl2Atur1DayIntervalCorrectedBlks_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalCorrectedBlks = _AdGenAdsl2Atur1DayIntervalCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 8),
    _AdGenAdsl2Atur1DayIntervalCorrectedBlks_Type()
)
adGenAdsl2Atur1DayIntervalCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalCorrectedBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalCorrectedBlks.setUnits("blocks")
_AdGenAdsl2Atur1DayIntervalUncorrectedBlks_Type = Counter32
_AdGenAdsl2Atur1DayIntervalUncorrectedBlks_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalUncorrectedBlks = _AdGenAdsl2Atur1DayIntervalUncorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 9),
    _AdGenAdsl2Atur1DayIntervalUncorrectedBlks_Type()
)
adGenAdsl2Atur1DayIntervalUncorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalUncorrectedBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalUncorrectedBlks.setUnits("blocks")
_AdGenAdsl2Atur1DayIntervalTxBlks_Type = Counter32
_AdGenAdsl2Atur1DayIntervalTxBlks_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalTxBlks = _AdGenAdsl2Atur1DayIntervalTxBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 10),
    _AdGenAdsl2Atur1DayIntervalTxBlks_Type()
)
adGenAdsl2Atur1DayIntervalTxBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalTxBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalTxBlks.setUnits("blocks")
_AdGenAdsl2Atur1DayIntervalRxBlks_Type = Counter32
_AdGenAdsl2Atur1DayIntervalRxBlks_Object = MibTableColumn
adGenAdsl2Atur1DayIntervalRxBlks = _AdGenAdsl2Atur1DayIntervalRxBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 2, 1, 11),
    _AdGenAdsl2Atur1DayIntervalRxBlks_Type()
)
adGenAdsl2Atur1DayIntervalRxBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalRxBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayIntervalRxBlks.setUnits("blocks")
_AdGenAdsl2AtucCurrentIntervalTable_Object = MibTable
adGenAdsl2AtucCurrentIntervalTable = _AdGenAdsl2AtucCurrentIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adGenAdsl2AtucCurrentIntervalTable.setStatus("current")
_AdGenAdsl2AtucCurrentIntervalEntry_Object = MibTableRow
adGenAdsl2AtucCurrentIntervalEntry = _AdGenAdsl2AtucCurrentIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 3, 1)
)
adGenAdsl2AtucCurrentIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAdsl2AtucCurrentIntervalEntry.setStatus("current")
_AdGenAdsl2Atuc1DayCurrentIntervalTxBlks_Type = Counter32
_AdGenAdsl2Atuc1DayCurrentIntervalTxBlks_Object = MibTableColumn
adGenAdsl2Atuc1DayCurrentIntervalTxBlks = _AdGenAdsl2Atuc1DayCurrentIntervalTxBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 3, 1, 1),
    _AdGenAdsl2Atuc1DayCurrentIntervalTxBlks_Type()
)
adGenAdsl2Atuc1DayCurrentIntervalTxBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayCurrentIntervalTxBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayCurrentIntervalTxBlks.setUnits("blocks")
_AdGenAdsl2Atuc1DayCurrentIntervalRxBlks_Type = Counter32
_AdGenAdsl2Atuc1DayCurrentIntervalRxBlks_Object = MibTableColumn
adGenAdsl2Atuc1DayCurrentIntervalRxBlks = _AdGenAdsl2Atuc1DayCurrentIntervalRxBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 3, 1, 2),
    _AdGenAdsl2Atuc1DayCurrentIntervalRxBlks_Type()
)
adGenAdsl2Atuc1DayCurrentIntervalRxBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayCurrentIntervalRxBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atuc1DayCurrentIntervalRxBlks.setUnits("blocks")
_AdGenAdsl2AturCurrentIntervalTable_Object = MibTable
adGenAdsl2AturCurrentIntervalTable = _AdGenAdsl2AturCurrentIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 4)
)
if mibBuilder.loadTexts:
    adGenAdsl2AturCurrentIntervalTable.setStatus("current")
_AdGenAdsl2AturCurrentIntervalEntry_Object = MibTableRow
adGenAdsl2AturCurrentIntervalEntry = _AdGenAdsl2AturCurrentIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 4, 1)
)
adGenAdsl2AturCurrentIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAdsl2AturCurrentIntervalEntry.setStatus("current")
_AdGenAdsl2Atur1DayCurrentIntervalTxBlks_Type = Counter32
_AdGenAdsl2Atur1DayCurrentIntervalTxBlks_Object = MibTableColumn
adGenAdsl2Atur1DayCurrentIntervalTxBlks = _AdGenAdsl2Atur1DayCurrentIntervalTxBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 4, 1, 1),
    _AdGenAdsl2Atur1DayCurrentIntervalTxBlks_Type()
)
adGenAdsl2Atur1DayCurrentIntervalTxBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayCurrentIntervalTxBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayCurrentIntervalTxBlks.setUnits("blocks")
_AdGenAdsl2Atur1DayCurrentIntervalRxBlks_Type = Counter32
_AdGenAdsl2Atur1DayCurrentIntervalRxBlks_Object = MibTableColumn
adGenAdsl2Atur1DayCurrentIntervalRxBlks = _AdGenAdsl2Atur1DayCurrentIntervalRxBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 1, 4, 1, 2),
    _AdGenAdsl2Atur1DayCurrentIntervalRxBlks_Type()
)
adGenAdsl2Atur1DayCurrentIntervalRxBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayCurrentIntervalRxBlks.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2Atur1DayCurrentIntervalRxBlks.setUnits("blocks")
_AdGenAdsl2MibConformance_ObjectIdentity = ObjectIdentity
adGenAdsl2MibConformance = _AdGenAdsl2MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 2)
)
_AdGenAdsl2MibGroups_ObjectIdentity = ObjectIdentity
adGenAdsl2MibGroups = _AdGenAdsl2MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 2, 1)
)
_AdGenAdsl2Status_ObjectIdentity = ObjectIdentity
adGenAdsl2Status = _AdGenAdsl2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 3)
)
_AdGenAdsl2LineTable_Object = MibTable
adGenAdsl2LineTable = _AdGenAdsl2LineTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adGenAdsl2LineTable.setStatus("current")
_AdGenAdsl2LineEntry_Object = MibTableRow
adGenAdsl2LineEntry = _AdGenAdsl2LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 3, 1, 1)
)
adGenAdsl2LineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAdsl2LineEntry.setStatus("current")
_AdGenAdsl2LineUpTime_Type = Gauge32
_AdGenAdsl2LineUpTime_Object = MibTableColumn
adGenAdsl2LineUpTime = _AdGenAdsl2LineUpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 3, 1, 1, 1),
    _AdGenAdsl2LineUpTime_Type()
)
adGenAdsl2LineUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdsl2LineUpTime.setStatus("current")
if mibBuilder.loadTexts:
    adGenAdsl2LineUpTime.setUnits("seconds")

# Managed Objects groups

adGenAdsl2PMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 82, 1, 2, 1, 1)
)
adGenAdsl2PMGroup.setObjects(
      *(("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalNumber"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalValidData"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalMoniSecs"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalLofs"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalLoss"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalLols"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalES"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalInits"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalCorrectedBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalUncorrectedBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalTxBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayIntervalRxBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayCurrentIntervalTxBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atuc1DayCurrentIntervalRxBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalNumber"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalValidData"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalMoniSecs"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalLofs"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalLoss"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalLprs"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalES"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalCorrectedBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalUncorrectedBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayCurrentIntervalTxBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayCurrentIntervalRxBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalTxBlks"),
        ("ADTRAN-GENADSL2-LINE-MIB", "adGenAdsl2Atur1DayIntervalRxBlks"))
)
if mibBuilder.loadTexts:
    adGenAdsl2PMGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENADSL2-LINE-MIB",
    **{"adGenAdsl2PM": adGenAdsl2PM,
       "adGenAdsl2Atuc1DayIntervalTable": adGenAdsl2Atuc1DayIntervalTable,
       "adGenAdsl2Atuc1DayIntervalEntry": adGenAdsl2Atuc1DayIntervalEntry,
       "adGenAdsl2Atuc1DayIntervalNumber": adGenAdsl2Atuc1DayIntervalNumber,
       "adGenAdsl2Atuc1DayIntervalValidData": adGenAdsl2Atuc1DayIntervalValidData,
       "adGenAdsl2Atuc1DayIntervalMoniSecs": adGenAdsl2Atuc1DayIntervalMoniSecs,
       "adGenAdsl2Atuc1DayIntervalLofs": adGenAdsl2Atuc1DayIntervalLofs,
       "adGenAdsl2Atuc1DayIntervalLoss": adGenAdsl2Atuc1DayIntervalLoss,
       "adGenAdsl2Atuc1DayIntervalLols": adGenAdsl2Atuc1DayIntervalLols,
       "adGenAdsl2Atuc1DayIntervalES": adGenAdsl2Atuc1DayIntervalES,
       "adGenAdsl2Atuc1DayIntervalInits": adGenAdsl2Atuc1DayIntervalInits,
       "adGenAdsl2Atuc1DayIntervalCorrectedBlks": adGenAdsl2Atuc1DayIntervalCorrectedBlks,
       "adGenAdsl2Atuc1DayIntervalUncorrectedBlks": adGenAdsl2Atuc1DayIntervalUncorrectedBlks,
       "adGenAdsl2Atuc1DayIntervalTxBlks": adGenAdsl2Atuc1DayIntervalTxBlks,
       "adGenAdsl2Atuc1DayIntervalRxBlks": adGenAdsl2Atuc1DayIntervalRxBlks,
       "adGenAdsl2Atur1DayIntervalTable": adGenAdsl2Atur1DayIntervalTable,
       "adGenAdsl2Atur1DayIntervalEntry": adGenAdsl2Atur1DayIntervalEntry,
       "adGenAdsl2Atur1DayIntervalNumber": adGenAdsl2Atur1DayIntervalNumber,
       "adGenAdsl2Atur1DayIntervalValidData": adGenAdsl2Atur1DayIntervalValidData,
       "adGenAdsl2Atur1DayIntervalMoniSecs": adGenAdsl2Atur1DayIntervalMoniSecs,
       "adGenAdsl2Atur1DayIntervalLofs": adGenAdsl2Atur1DayIntervalLofs,
       "adGenAdsl2Atur1DayIntervalLoss": adGenAdsl2Atur1DayIntervalLoss,
       "adGenAdsl2Atur1DayIntervalLprs": adGenAdsl2Atur1DayIntervalLprs,
       "adGenAdsl2Atur1DayIntervalES": adGenAdsl2Atur1DayIntervalES,
       "adGenAdsl2Atur1DayIntervalCorrectedBlks": adGenAdsl2Atur1DayIntervalCorrectedBlks,
       "adGenAdsl2Atur1DayIntervalUncorrectedBlks": adGenAdsl2Atur1DayIntervalUncorrectedBlks,
       "adGenAdsl2Atur1DayIntervalTxBlks": adGenAdsl2Atur1DayIntervalTxBlks,
       "adGenAdsl2Atur1DayIntervalRxBlks": adGenAdsl2Atur1DayIntervalRxBlks,
       "adGenAdsl2AtucCurrentIntervalTable": adGenAdsl2AtucCurrentIntervalTable,
       "adGenAdsl2AtucCurrentIntervalEntry": adGenAdsl2AtucCurrentIntervalEntry,
       "adGenAdsl2Atuc1DayCurrentIntervalTxBlks": adGenAdsl2Atuc1DayCurrentIntervalTxBlks,
       "adGenAdsl2Atuc1DayCurrentIntervalRxBlks": adGenAdsl2Atuc1DayCurrentIntervalRxBlks,
       "adGenAdsl2AturCurrentIntervalTable": adGenAdsl2AturCurrentIntervalTable,
       "adGenAdsl2AturCurrentIntervalEntry": adGenAdsl2AturCurrentIntervalEntry,
       "adGenAdsl2Atur1DayCurrentIntervalTxBlks": adGenAdsl2Atur1DayCurrentIntervalTxBlks,
       "adGenAdsl2Atur1DayCurrentIntervalRxBlks": adGenAdsl2Atur1DayCurrentIntervalRxBlks,
       "adGenAdsl2MibConformance": adGenAdsl2MibConformance,
       "adGenAdsl2MibGroups": adGenAdsl2MibGroups,
       "adGenAdsl2PMGroup": adGenAdsl2PMGroup,
       "adGenAdsl2Status": adGenAdsl2Status,
       "adGenAdsl2LineTable": adGenAdsl2LineTable,
       "adGenAdsl2LineEntry": adGenAdsl2LineEntry,
       "adGenAdsl2LineUpTime": adGenAdsl2LineUpTime,
       "adGenAdslID": adGenAdslID}
)
