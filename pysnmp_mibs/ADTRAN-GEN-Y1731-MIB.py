# SNMP MIB module (ADTRAN-GEN-Y1731-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-Y1731-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:45 2025
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

(adGenY1731,
 adGenY1731ID) = mibBuilder.importSymbols(
    "ADTRAN-GEN-ETHERNET-OAM-MIB",
    "adGenY1731",
    "adGenY1731ID")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(LldpChassisId,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpPortId",
    "LldpPortIdSubtype")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

adGenY1731MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 75, 2, 1)
)
if mibBuilder.loadTexts:
    adGenY1731MIB.setRevisions(
        ("2014-07-21 00:00",
         "2012-11-08 00:00",
         "2012-06-28 00:00",
         "2011-09-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenY1731MIBObjects_ObjectIdentity = ObjectIdentity
adGenY1731MIBObjects = _AdGenY1731MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1)
)
_AdGenY1731Config_ObjectIdentity = ObjectIdentity
adGenY1731Config = _AdGenY1731Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 1)
)


class _AdGenY1731Enable_Type(Integer32):
    """Custom type adGenY1731Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenY1731Enable_Type.__name__ = "Integer32"
_AdGenY1731Enable_Object = MibScalar
adGenY1731Enable = _AdGenY1731Enable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 1, 1),
    _AdGenY1731Enable_Type()
)
adGenY1731Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731Enable.setStatus("current")


class _AdGenY1731BulkDataExportInterval_Type(Integer32):
    """Custom type adGenY1731BulkDataExportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_AdGenY1731BulkDataExportInterval_Type.__name__ = "Integer32"
_AdGenY1731BulkDataExportInterval_Object = MibScalar
adGenY1731BulkDataExportInterval = _AdGenY1731BulkDataExportInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 1, 2),
    _AdGenY1731BulkDataExportInterval_Type()
)
adGenY1731BulkDataExportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731BulkDataExportInterval.setStatus("current")


class _AdGenY1731LinktraceCacheHoldTime_Type(Integer32):
    """Custom type adGenY1731LinktraceCacheHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdGenY1731LinktraceCacheHoldTime_Type.__name__ = "Integer32"
_AdGenY1731LinktraceCacheHoldTime_Object = MibScalar
adGenY1731LinktraceCacheHoldTime = _AdGenY1731LinktraceCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 1, 3),
    _AdGenY1731LinktraceCacheHoldTime_Type()
)
adGenY1731LinktraceCacheHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LinktraceCacheHoldTime.setStatus("current")


class _AdGenY1731LinktraceCacheSize_Type(Integer32):
    """Custom type adGenY1731LinktraceCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AdGenY1731LinktraceCacheSize_Type.__name__ = "Integer32"
_AdGenY1731LinktraceCacheSize_Object = MibScalar
adGenY1731LinktraceCacheSize = _AdGenY1731LinktraceCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 1, 4),
    _AdGenY1731LinktraceCacheSize_Type()
)
adGenY1731LinktraceCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LinktraceCacheSize.setStatus("current")
_AdGenY1731Meg_ObjectIdentity = ObjectIdentity
adGenY1731Meg = _AdGenY1731Meg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2)
)
_AdGenY1731MegMaxNumber_Type = Unsigned32
_AdGenY1731MegMaxNumber_Object = MibScalar
adGenY1731MegMaxNumber = _AdGenY1731MegMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 1),
    _AdGenY1731MegMaxNumber_Type()
)
adGenY1731MegMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731MegMaxNumber.setStatus("current")
_AdGenY1731MegCurrentNumber_Type = Unsigned32
_AdGenY1731MegCurrentNumber_Object = MibScalar
adGenY1731MegCurrentNumber = _AdGenY1731MegCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 2),
    _AdGenY1731MegCurrentNumber_Type()
)
adGenY1731MegCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731MegCurrentNumber.setStatus("current")
_AdGenY1731MegLastCreateError_Type = DisplayString
_AdGenY1731MegLastCreateError_Object = MibScalar
adGenY1731MegLastCreateError = _AdGenY1731MegLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 3),
    _AdGenY1731MegLastCreateError_Type()
)
adGenY1731MegLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731MegLastCreateError.setStatus("current")
_AdGenY1731MegTable_Object = MibTable
adGenY1731MegTable = _AdGenY1731MegTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    adGenY1731MegTable.setStatus("current")
_AdGenY1731MegEntry_Object = MibTableRow
adGenY1731MegEntry = _AdGenY1731MegEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4, 1)
)
adGenY1731MegEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
)
if mibBuilder.loadTexts:
    adGenY1731MegEntry.setStatus("current")


class _AdGenY1731MegLevel_Type(Integer32):
    """Custom type adGenY1731MegLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenY1731MegLevel_Type.__name__ = "Integer32"
_AdGenY1731MegLevel_Object = MibTableColumn
adGenY1731MegLevel = _AdGenY1731MegLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4, 1, 1),
    _AdGenY1731MegLevel_Type()
)
adGenY1731MegLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731MegLevel.setStatus("current")


class _AdGenY1731MegNameFormat_Type(Integer32):
    """Custom type adGenY1731MegNameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              32,
              256)
        )
    )
    namedValues = NamedValues(
        *(("charString", 2),
          ("iccUmc", 32),
          ("cfm", 256))
    )


_AdGenY1731MegNameFormat_Type.__name__ = "Integer32"
_AdGenY1731MegNameFormat_Object = MibTableColumn
adGenY1731MegNameFormat = _AdGenY1731MegNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4, 1, 2),
    _AdGenY1731MegNameFormat_Type()
)
adGenY1731MegNameFormat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731MegNameFormat.setStatus("current")


class _AdGenY1731MegNameLengthAndName_Type(OctetString):
    """Custom type adGenY1731MegNameLengthAndName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 46),
    )


_AdGenY1731MegNameLengthAndName_Type.__name__ = "OctetString"
_AdGenY1731MegNameLengthAndName_Object = MibTableColumn
adGenY1731MegNameLengthAndName = _AdGenY1731MegNameLengthAndName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4, 1, 3),
    _AdGenY1731MegNameLengthAndName_Type()
)
adGenY1731MegNameLengthAndName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731MegNameLengthAndName.setStatus("current")
_AdGenY1731MegRowStatus_Type = RowStatus
_AdGenY1731MegRowStatus_Object = MibTableColumn
adGenY1731MegRowStatus = _AdGenY1731MegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4, 1, 4),
    _AdGenY1731MegRowStatus_Type()
)
adGenY1731MegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731MegRowStatus.setStatus("current")
_AdGenY1731MegServiceTypeValueList_Type = OctetString
_AdGenY1731MegServiceTypeValueList_Object = MibTableColumn
adGenY1731MegServiceTypeValueList = _AdGenY1731MegServiceTypeValueList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4, 1, 5),
    _AdGenY1731MegServiceTypeValueList_Type()
)
adGenY1731MegServiceTypeValueList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731MegServiceTypeValueList.setStatus("current")


class _AdGenY1731MegCcmInterval_Type(Integer32):
    """Custom type adGenY1731MegCcmInterval based on Integer32"""
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
        *(("interval300Hz", 1),
          ("interval10ms", 2),
          ("interval100ms", 3),
          ("interval1s", 4),
          ("interval10s", 5),
          ("interval1min", 6),
          ("interval10min", 7))
    )


_AdGenY1731MegCcmInterval_Type.__name__ = "Integer32"
_AdGenY1731MegCcmInterval_Object = MibTableColumn
adGenY1731MegCcmInterval = _AdGenY1731MegCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4, 1, 6),
    _AdGenY1731MegCcmInterval_Type()
)
adGenY1731MegCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731MegCcmInterval.setStatus("current")
_AdGenY1731MegLocalMepConfigTableLastCreateError_Type = DisplayString
_AdGenY1731MegLocalMepConfigTableLastCreateError_Object = MibTableColumn
adGenY1731MegLocalMepConfigTableLastCreateError = _AdGenY1731MegLocalMepConfigTableLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4, 1, 7),
    _AdGenY1731MegLocalMepConfigTableLastCreateError_Type()
)
adGenY1731MegLocalMepConfigTableLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731MegLocalMepConfigTableLastCreateError.setStatus("current")
_AdGenY1731MegDisplayName_Type = DisplayString
_AdGenY1731MegDisplayName_Object = MibTableColumn
adGenY1731MegDisplayName = _AdGenY1731MegDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 4, 1, 8),
    _AdGenY1731MegDisplayName_Type()
)
adGenY1731MegDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731MegDisplayName.setStatus("current")
_AdGenY1731MegMepList_ObjectIdentity = ObjectIdentity
adGenY1731MegMepList = _AdGenY1731MegMepList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 5)
)
_AdGenY1731MegMepListScalars_ObjectIdentity = ObjectIdentity
adGenY1731MegMepListScalars = _AdGenY1731MegMepListScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 5, 1)
)
_AdGenY1731MegMepListMaxNumber_Type = Unsigned32
_AdGenY1731MegMepListMaxNumber_Object = MibScalar
adGenY1731MegMepListMaxNumber = _AdGenY1731MegMepListMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 5, 1, 1),
    _AdGenY1731MegMepListMaxNumber_Type()
)
adGenY1731MegMepListMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731MegMepListMaxNumber.setStatus("current")
_AdGenY1731MegMepListCurrentNumber_Type = Unsigned32
_AdGenY1731MegMepListCurrentNumber_Object = MibScalar
adGenY1731MegMepListCurrentNumber = _AdGenY1731MegMepListCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 5, 1, 2),
    _AdGenY1731MegMepListCurrentNumber_Type()
)
adGenY1731MegMepListCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731MegMepListCurrentNumber.setStatus("current")
_AdGenY1731MegMepListTableLastCreateError_Type = DisplayString
_AdGenY1731MegMepListTableLastCreateError_Object = MibScalar
adGenY1731MegMepListTableLastCreateError = _AdGenY1731MegMepListTableLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 5, 1, 3),
    _AdGenY1731MegMepListTableLastCreateError_Type()
)
adGenY1731MegMepListTableLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731MegMepListTableLastCreateError.setStatus("current")
_AdGenY1731MegMepListTable_Object = MibTable
adGenY1731MegMepListTable = _AdGenY1731MegMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    adGenY1731MegMepListTable.setStatus("current")
_AdGenY1731MegMepListEntry_Object = MibTableRow
adGenY1731MegMepListEntry = _AdGenY1731MegMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 5, 2, 1)
)
adGenY1731MegMepListEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegMepListIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731MegMepListEntry.setStatus("current")


class _AdGenY1731MegMepListIdentifier_Type(Integer32):
    """Custom type adGenY1731MegMepListIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenY1731MegMepListIdentifier_Type.__name__ = "Integer32"
_AdGenY1731MegMepListIdentifier_Object = MibTableColumn
adGenY1731MegMepListIdentifier = _AdGenY1731MegMepListIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 5, 2, 1, 1),
    _AdGenY1731MegMepListIdentifier_Type()
)
adGenY1731MegMepListIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731MegMepListIdentifier.setStatus("current")
_AdGenY1731MegMepListRowStatus_Type = RowStatus
_AdGenY1731MegMepListRowStatus_Object = MibTableColumn
adGenY1731MegMepListRowStatus = _AdGenY1731MegMepListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 2, 5, 2, 1, 2),
    _AdGenY1731MegMepListRowStatus_Type()
)
adGenY1731MegMepListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731MegMepListRowStatus.setStatus("current")
_AdGenY1731LocalMep_ObjectIdentity = ObjectIdentity
adGenY1731LocalMep = _AdGenY1731LocalMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3)
)
_AdGenY1731LocalMepConfig_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepConfig = _AdGenY1731LocalMepConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1)
)
_AdGenY1731LocalMepConfigScalars_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepConfigScalars = _AdGenY1731LocalMepConfigScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 1)
)
_AdGenY1731LocalMepMaxNumber_Type = Unsigned32
_AdGenY1731LocalMepMaxNumber_Object = MibScalar
adGenY1731LocalMepMaxNumber = _AdGenY1731LocalMepMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 1, 1),
    _AdGenY1731LocalMepMaxNumber_Type()
)
adGenY1731LocalMepMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepMaxNumber.setStatus("current")
_AdGenY1731LocalMepCurrentNumber_Type = Unsigned32
_AdGenY1731LocalMepCurrentNumber_Object = MibScalar
adGenY1731LocalMepCurrentNumber = _AdGenY1731LocalMepCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 1, 2),
    _AdGenY1731LocalMepCurrentNumber_Type()
)
adGenY1731LocalMepCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepCurrentNumber.setStatus("current")
_AdGenY1731LocalMepConfigTableLastCreateError_Type = DisplayString
_AdGenY1731LocalMepConfigTableLastCreateError_Object = MibScalar
adGenY1731LocalMepConfigTableLastCreateError = _AdGenY1731LocalMepConfigTableLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 1, 3),
    _AdGenY1731LocalMepConfigTableLastCreateError_Type()
)
adGenY1731LocalMepConfigTableLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepConfigTableLastCreateError.setStatus("current")
_AdGenY1731LocalMepConfigTable_Object = MibTable
adGenY1731LocalMepConfigTable = _AdGenY1731LocalMepConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepConfigTable.setStatus("current")
_AdGenY1731LocalMepConfigEntry_Object = MibTableRow
adGenY1731LocalMepConfigEntry = _AdGenY1731LocalMepConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1)
)
adGenY1731LocalMepConfigEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepConfigEntry.setStatus("current")


class _AdGenY1731LocalMepIdentifier_Type(Integer32):
    """Custom type adGenY1731LocalMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenY1731LocalMepIdentifier_Type.__name__ = "Integer32"
_AdGenY1731LocalMepIdentifier_Object = MibTableColumn
adGenY1731LocalMepIdentifier = _AdGenY1731LocalMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1, 1),
    _AdGenY1731LocalMepIdentifier_Type()
)
adGenY1731LocalMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731LocalMepIdentifier.setStatus("current")
_AdGenY1731LocalMepRowStatus_Type = RowStatus
_AdGenY1731LocalMepRowStatus_Object = MibTableColumn
adGenY1731LocalMepRowStatus = _AdGenY1731LocalMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1, 2),
    _AdGenY1731LocalMepRowStatus_Type()
)
adGenY1731LocalMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LocalMepRowStatus.setStatus("current")


class _AdGenY1731LocalMepStatus_Type(Integer32):
    """Custom type adGenY1731LocalMepStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notRunning", 2))
    )


_AdGenY1731LocalMepStatus_Type.__name__ = "Integer32"
_AdGenY1731LocalMepStatus_Object = MibTableColumn
adGenY1731LocalMepStatus = _AdGenY1731LocalMepStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1, 3),
    _AdGenY1731LocalMepStatus_Type()
)
adGenY1731LocalMepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepStatus.setStatus("current")
_AdGenY1731LocalMepStatusString_Type = OctetString
_AdGenY1731LocalMepStatusString_Object = MibTableColumn
adGenY1731LocalMepStatusString = _AdGenY1731LocalMepStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1, 4),
    _AdGenY1731LocalMepStatusString_Type()
)
adGenY1731LocalMepStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepStatusString.setStatus("current")
_AdGenY1731LocalMepIfIndex_Type = InterfaceIndexOrZero
_AdGenY1731LocalMepIfIndex_Object = MibTableColumn
adGenY1731LocalMepIfIndex = _AdGenY1731LocalMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1, 5),
    _AdGenY1731LocalMepIfIndex_Type()
)
adGenY1731LocalMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LocalMepIfIndex.setStatus("current")


class _AdGenY1731LocalMepDirection_Type(Integer32):
    """Custom type adGenY1731LocalMepDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 0),
          ("down", 1),
          ("up", 2))
    )


_AdGenY1731LocalMepDirection_Type.__name__ = "Integer32"
_AdGenY1731LocalMepDirection_Object = MibTableColumn
adGenY1731LocalMepDirection = _AdGenY1731LocalMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1, 6),
    _AdGenY1731LocalMepDirection_Type()
)
adGenY1731LocalMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LocalMepDirection.setStatus("current")


class _AdGenY1731LocalMepAdminState_Type(Integer32):
    """Custom type adGenY1731LocalMepAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenY1731LocalMepAdminState_Type.__name__ = "Integer32"
_AdGenY1731LocalMepAdminState_Object = MibTableColumn
adGenY1731LocalMepAdminState = _AdGenY1731LocalMepAdminState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1, 7),
    _AdGenY1731LocalMepAdminState_Type()
)
adGenY1731LocalMepAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LocalMepAdminState.setStatus("current")


class _AdGenY1731LocalMepVlanPriority_Type(Integer32):
    """Custom type adGenY1731LocalMepVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenY1731LocalMepVlanPriority_Type.__name__ = "Integer32"
_AdGenY1731LocalMepVlanPriority_Object = MibTableColumn
adGenY1731LocalMepVlanPriority = _AdGenY1731LocalMepVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1, 8),
    _AdGenY1731LocalMepVlanPriority_Type()
)
adGenY1731LocalMepVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LocalMepVlanPriority.setStatus("current")


class _AdGenY1731LocalMepCcmEnabled_Type(Integer32):
    """Custom type adGenY1731LocalMepCcmEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdGenY1731LocalMepCcmEnabled_Type.__name__ = "Integer32"
_AdGenY1731LocalMepCcmEnabled_Object = MibTableColumn
adGenY1731LocalMepCcmEnabled = _AdGenY1731LocalMepCcmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 1, 2, 1, 9),
    _AdGenY1731LocalMepCcmEnabled_Type()
)
adGenY1731LocalMepCcmEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LocalMepCcmEnabled.setStatus("current")
_AdGenY1731LocalMepRmepDb_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepRmepDb = _AdGenY1731LocalMepRmepDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2)
)
_AdGenY1731LocalMepRmepDbScalars_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepRmepDbScalars = _AdGenY1731LocalMepRmepDbScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 1)
)
_AdGenY1731LocalMepRmepDbMaxNumber_Type = Unsigned32
_AdGenY1731LocalMepRmepDbMaxNumber_Object = MibScalar
adGenY1731LocalMepRmepDbMaxNumber = _AdGenY1731LocalMepRmepDbMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 1, 1),
    _AdGenY1731LocalMepRmepDbMaxNumber_Type()
)
adGenY1731LocalMepRmepDbMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepRmepDbMaxNumber.setStatus("current")
_AdGenY1731LocalMepRmepDbCurrentNumber_Type = Unsigned32
_AdGenY1731LocalMepRmepDbCurrentNumber_Object = MibScalar
adGenY1731LocalMepRmepDbCurrentNumber = _AdGenY1731LocalMepRmepDbCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 1, 2),
    _AdGenY1731LocalMepRmepDbCurrentNumber_Type()
)
adGenY1731LocalMepRmepDbCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepRmepDbCurrentNumber.setStatus("current")
_AdGenY1731LocalMepRmepDbTable_Object = MibTable
adGenY1731LocalMepRmepDbTable = _AdGenY1731LocalMepRmepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepRmepDbTable.setStatus("current")
_AdGenY1731LocalMepRmepDbEntry_Object = MibTableRow
adGenY1731LocalMepRmepDbEntry = _AdGenY1731LocalMepRmepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1)
)
adGenY1731LocalMepRmepDbEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731RemoteMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepRmepDbEntry.setStatus("current")


class _AdGenY1731RemoteMepIdentifier_Type(Integer32):
    """Custom type adGenY1731RemoteMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenY1731RemoteMepIdentifier_Type.__name__ = "Integer32"
_AdGenY1731RemoteMepIdentifier_Object = MibTableColumn
adGenY1731RemoteMepIdentifier = _AdGenY1731RemoteMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 1),
    _AdGenY1731RemoteMepIdentifier_Type()
)
adGenY1731RemoteMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepIdentifier.setStatus("current")


class _AdGenY1731RemoteMepStatus_Type(Integer32):
    """Custom type adGenY1731RemoteMepStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("okay", 1),
          ("failed", 2))
    )


_AdGenY1731RemoteMepStatus_Type.__name__ = "Integer32"
_AdGenY1731RemoteMepStatus_Object = MibTableColumn
adGenY1731RemoteMepStatus = _AdGenY1731RemoteMepStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 2),
    _AdGenY1731RemoteMepStatus_Type()
)
adGenY1731RemoteMepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepStatus.setStatus("current")
_AdGenY1731RemoteMepFailedOkTime_Type = TimeStamp
_AdGenY1731RemoteMepFailedOkTime_Object = MibTableColumn
adGenY1731RemoteMepFailedOkTime = _AdGenY1731RemoteMepFailedOkTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 3),
    _AdGenY1731RemoteMepFailedOkTime_Type()
)
adGenY1731RemoteMepFailedOkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepFailedOkTime.setStatus("current")
_AdGenY1731RemoteMepMacAddress_Type = MacAddress
_AdGenY1731RemoteMepMacAddress_Object = MibTableColumn
adGenY1731RemoteMepMacAddress = _AdGenY1731RemoteMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 4),
    _AdGenY1731RemoteMepMacAddress_Type()
)
adGenY1731RemoteMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepMacAddress.setStatus("current")
_AdGenY1731RemoteMepLastCcmSequenceNumber_Type = Unsigned32
_AdGenY1731RemoteMepLastCcmSequenceNumber_Object = MibTableColumn
adGenY1731RemoteMepLastCcmSequenceNumber = _AdGenY1731RemoteMepLastCcmSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 5),
    _AdGenY1731RemoteMepLastCcmSequenceNumber_Type()
)
adGenY1731RemoteMepLastCcmSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepLastCcmSequenceNumber.setStatus("current")
_AdGenY1731RemoteMepRdi_Type = TruthValue
_AdGenY1731RemoteMepRdi_Object = MibTableColumn
adGenY1731RemoteMepRdi = _AdGenY1731RemoteMepRdi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 6),
    _AdGenY1731RemoteMepRdi_Type()
)
adGenY1731RemoteMepRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepRdi.setStatus("current")


class _AdGenY1731RemoteMepPortStatus_Type(Integer32):
    """Custom type adGenY1731RemoteMepPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psNoPortStatusTlv", 0),
          ("psBlocked", 1),
          ("psUp", 2))
    )


_AdGenY1731RemoteMepPortStatus_Type.__name__ = "Integer32"
_AdGenY1731RemoteMepPortStatus_Object = MibTableColumn
adGenY1731RemoteMepPortStatus = _AdGenY1731RemoteMepPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 7),
    _AdGenY1731RemoteMepPortStatus_Type()
)
adGenY1731RemoteMepPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepPortStatus.setStatus("current")


class _AdGenY1731RemoteMepInterfaceStatus_Type(Integer32):
    """Custom type adGenY1731RemoteMepInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("isNoInterfaceStatusTLV", 0),
          ("isUp", 1),
          ("isDown", 2),
          ("isTesting", 3),
          ("isUnknown", 4),
          ("isDormant", 5),
          ("isNotPresent", 6),
          ("isLowerLayerDown", 7))
    )


_AdGenY1731RemoteMepInterfaceStatus_Type.__name__ = "Integer32"
_AdGenY1731RemoteMepInterfaceStatus_Object = MibTableColumn
adGenY1731RemoteMepInterfaceStatus = _AdGenY1731RemoteMepInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 8),
    _AdGenY1731RemoteMepInterfaceStatus_Type()
)
adGenY1731RemoteMepInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepInterfaceStatus.setStatus("current")


class _AdGenY1731RemoteMepChassisIdSubtype_Type(Integer32):
    """Custom type adGenY1731RemoteMepChassisIdSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("nonePresent", 0),
          ("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7))
    )


_AdGenY1731RemoteMepChassisIdSubtype_Type.__name__ = "Integer32"
_AdGenY1731RemoteMepChassisIdSubtype_Object = MibTableColumn
adGenY1731RemoteMepChassisIdSubtype = _AdGenY1731RemoteMepChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 9),
    _AdGenY1731RemoteMepChassisIdSubtype_Type()
)
adGenY1731RemoteMepChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepChassisIdSubtype.setStatus("current")
_AdGenY1731RemoteMepChassisId_Type = LldpChassisId
_AdGenY1731RemoteMepChassisId_Object = MibTableColumn
adGenY1731RemoteMepChassisId = _AdGenY1731RemoteMepChassisId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 10),
    _AdGenY1731RemoteMepChassisId_Type()
)
adGenY1731RemoteMepChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepChassisId.setStatus("current")
_AdGenY1731RemoteMepManAddressDomain_Type = TDomain
_AdGenY1731RemoteMepManAddressDomain_Object = MibTableColumn
adGenY1731RemoteMepManAddressDomain = _AdGenY1731RemoteMepManAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 11),
    _AdGenY1731RemoteMepManAddressDomain_Type()
)
adGenY1731RemoteMepManAddressDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepManAddressDomain.setStatus("current")
_AdGenY1731RemoteMepManAddress_Type = TAddress
_AdGenY1731RemoteMepManAddress_Object = MibTableColumn
adGenY1731RemoteMepManAddress = _AdGenY1731RemoteMepManAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 2, 2, 1, 12),
    _AdGenY1731RemoteMepManAddress_Type()
)
adGenY1731RemoteMepManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731RemoteMepManAddress.setStatus("current")
_AdGenY1731LocalMepLbm_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepLbm = _AdGenY1731LocalMepLbm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3)
)
_AdGenY1731LocalMepLbmTransmitTable_Object = MibTable
adGenY1731LocalMepLbmTransmitTable = _AdGenY1731LocalMepLbmTransmitTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmTransmitTable.setStatus("current")
_AdGenY1731LocalMepLbmTransmitEntry_Object = MibTableRow
adGenY1731LocalMepLbmTransmitEntry = _AdGenY1731LocalMepLbmTransmitEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1)
)
adGenY1731LocalMepLbmTransmitEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmTransmitEntry.setStatus("current")


class _AdGenY1731LocalMepLbmStatus_Type(TruthValue):
    """Custom type adGenY1731LocalMepLbmStatus based on TruthValue"""
    defaultValue = 2


_AdGenY1731LocalMepLbmStatus_Type.__name__ = "TruthValue"
_AdGenY1731LocalMepLbmStatus_Object = MibTableColumn
adGenY1731LocalMepLbmStatus = _AdGenY1731LocalMepLbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 1),
    _AdGenY1731LocalMepLbmStatus_Type()
)
adGenY1731LocalMepLbmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmStatus.setStatus("current")


class _AdGenY1731LocalMepLbmConfigStatus_Type(TruthValue):
    """Custom type adGenY1731LocalMepLbmConfigStatus based on TruthValue"""
    defaultValue = 1


_AdGenY1731LocalMepLbmConfigStatus_Type.__name__ = "TruthValue"
_AdGenY1731LocalMepLbmConfigStatus_Object = MibTableColumn
adGenY1731LocalMepLbmConfigStatus = _AdGenY1731LocalMepLbmConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 2),
    _AdGenY1731LocalMepLbmConfigStatus_Type()
)
adGenY1731LocalMepLbmConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmConfigStatus.setStatus("current")
_AdGenY1731LocalMepLbmDestMacAddress_Type = MacAddress
_AdGenY1731LocalMepLbmDestMacAddress_Object = MibTableColumn
adGenY1731LocalMepLbmDestMacAddress = _AdGenY1731LocalMepLbmDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 3),
    _AdGenY1731LocalMepLbmDestMacAddress_Type()
)
adGenY1731LocalMepLbmDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmDestMacAddress.setStatus("current")


class _AdGenY1731LocalMepLbmDestMepId_Type(Integer32):
    """Custom type adGenY1731LocalMepLbmDestMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenY1731LocalMepLbmDestMepId_Type.__name__ = "Integer32"
_AdGenY1731LocalMepLbmDestMepId_Object = MibTableColumn
adGenY1731LocalMepLbmDestMepId = _AdGenY1731LocalMepLbmDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 4),
    _AdGenY1731LocalMepLbmDestMepId_Type()
)
adGenY1731LocalMepLbmDestMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmDestMepId.setStatus("current")
_AdGenY1731LocalMepLbmDestIsMepId_Type = TruthValue
_AdGenY1731LocalMepLbmDestIsMepId_Object = MibTableColumn
adGenY1731LocalMepLbmDestIsMepId = _AdGenY1731LocalMepLbmDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 5),
    _AdGenY1731LocalMepLbmDestIsMepId_Type()
)
adGenY1731LocalMepLbmDestIsMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmDestIsMepId.setStatus("current")


class _AdGenY1731LocalMepLbmMessageCount_Type(Integer32):
    """Custom type adGenY1731LocalMepLbmMessageCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AdGenY1731LocalMepLbmMessageCount_Type.__name__ = "Integer32"
_AdGenY1731LocalMepLbmMessageCount_Object = MibTableColumn
adGenY1731LocalMepLbmMessageCount = _AdGenY1731LocalMepLbmMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 6),
    _AdGenY1731LocalMepLbmMessageCount_Type()
)
adGenY1731LocalMepLbmMessageCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmMessageCount.setStatus("current")


class _AdGenY1731LocalMepLbmActive_Type(TruthValue):
    """Custom type adGenY1731LocalMepLbmActive based on TruthValue"""
    defaultValue = 2


_AdGenY1731LocalMepLbmActive_Type.__name__ = "TruthValue"
_AdGenY1731LocalMepLbmActive_Object = MibTableColumn
adGenY1731LocalMepLbmActive = _AdGenY1731LocalMepLbmActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 7),
    _AdGenY1731LocalMepLbmActive_Type()
)
adGenY1731LocalMepLbmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmActive.setStatus("current")


class _AdGenY1731LocalMepLbmDataTlv_Type(OctetString):
    """Custom type adGenY1731LocalMepLbmDataTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1500),
    )


_AdGenY1731LocalMepLbmDataTlv_Type.__name__ = "OctetString"
_AdGenY1731LocalMepLbmDataTlv_Object = MibTableColumn
adGenY1731LocalMepLbmDataTlv = _AdGenY1731LocalMepLbmDataTlv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 8),
    _AdGenY1731LocalMepLbmDataTlv_Type()
)
adGenY1731LocalMepLbmDataTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmDataTlv.setStatus("current")


class _AdGenY1731LocalMepLbmVlanPriority_Type(Integer32):
    """Custom type adGenY1731LocalMepLbmVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenY1731LocalMepLbmVlanPriority_Type.__name__ = "Integer32"
_AdGenY1731LocalMepLbmVlanPriority_Object = MibTableColumn
adGenY1731LocalMepLbmVlanPriority = _AdGenY1731LocalMepLbmVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 9),
    _AdGenY1731LocalMepLbmVlanPriority_Type()
)
adGenY1731LocalMepLbmVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmVlanPriority.setStatus("current")


class _AdGenY1731LocalMepLbmVlanDropEnable_Type(TruthValue):
    """Custom type adGenY1731LocalMepLbmVlanDropEnable based on TruthValue"""
    defaultValue = 1


_AdGenY1731LocalMepLbmVlanDropEnable_Type.__name__ = "TruthValue"
_AdGenY1731LocalMepLbmVlanDropEnable_Object = MibTableColumn
adGenY1731LocalMepLbmVlanDropEnable = _AdGenY1731LocalMepLbmVlanDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 10),
    _AdGenY1731LocalMepLbmVlanDropEnable_Type()
)
adGenY1731LocalMepLbmVlanDropEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmVlanDropEnable.setStatus("current")
_AdGenY1731LocalMepLbmErrorStatus_Type = DisplayString
_AdGenY1731LocalMepLbmErrorStatus_Object = MibTableColumn
adGenY1731LocalMepLbmErrorStatus = _AdGenY1731LocalMepLbmErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 11),
    _AdGenY1731LocalMepLbmErrorStatus_Type()
)
adGenY1731LocalMepLbmErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmErrorStatus.setStatus("current")


class _AdGenY1731LocalMepLbmTimeout_Type(Unsigned32):
    """Custom type adGenY1731LocalMepLbmTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_AdGenY1731LocalMepLbmTimeout_Type.__name__ = "Unsigned32"
_AdGenY1731LocalMepLbmTimeout_Object = MibTableColumn
adGenY1731LocalMepLbmTimeout = _AdGenY1731LocalMepLbmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 12),
    _AdGenY1731LocalMepLbmTimeout_Type()
)
adGenY1731LocalMepLbmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmTimeout.setStatus("current")


class _AdGenY1731LocalMepLbmInterframeDelay_Type(Unsigned32):
    """Custom type adGenY1731LocalMepLbmInterframeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdGenY1731LocalMepLbmInterframeDelay_Type.__name__ = "Unsigned32"
_AdGenY1731LocalMepLbmInterframeDelay_Object = MibTableColumn
adGenY1731LocalMepLbmInterframeDelay = _AdGenY1731LocalMepLbmInterframeDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 13),
    _AdGenY1731LocalMepLbmInterframeDelay_Type()
)
adGenY1731LocalMepLbmInterframeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmInterframeDelay.setStatus("current")
_AdGenY1731LocalMepLbmNextTransId_Type = Unsigned32
_AdGenY1731LocalMepLbmNextTransId_Object = MibTableColumn
adGenY1731LocalMepLbmNextTransId = _AdGenY1731LocalMepLbmNextTransId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 14),
    _AdGenY1731LocalMepLbmNextTransId_Type()
)
adGenY1731LocalMepLbmNextTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmNextTransId.setStatus("current")
_AdGenY1731LocalMepLbmSize_Type = Integer32
_AdGenY1731LocalMepLbmSize_Object = MibTableColumn
adGenY1731LocalMepLbmSize = _AdGenY1731LocalMepLbmSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 15),
    _AdGenY1731LocalMepLbmSize_Type()
)
adGenY1731LocalMepLbmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmSize.setStatus("current")


class _AdGenY1731LocalMepValidateData_Type(TruthValue):
    """Custom type adGenY1731LocalMepValidateData based on TruthValue"""
    defaultValue = 2


_AdGenY1731LocalMepValidateData_Type.__name__ = "TruthValue"
_AdGenY1731LocalMepValidateData_Object = MibTableColumn
adGenY1731LocalMepValidateData = _AdGenY1731LocalMepValidateData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 1, 1, 16),
    _AdGenY1731LocalMepValidateData_Type()
)
adGenY1731LocalMepValidateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepValidateData.setStatus("current")
_AdGenY1731LocalMepLbmResultTable_Object = MibTable
adGenY1731LocalMepLbmResultTable = _AdGenY1731LocalMepLbmResultTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmResultTable.setStatus("current")
_AdGenY1731LocalMepLbmResultEntry_Object = MibTableRow
adGenY1731LocalMepLbmResultEntry = _AdGenY1731LocalMepLbmResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2, 1)
)
adGenY1731LocalMepLbmResultEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmResultEntry.setStatus("current")


class _AdGenY1731LocalMepLbrResultOk_Type(TruthValue):
    """Custom type adGenY1731LocalMepLbrResultOk based on TruthValue"""
    defaultValue = 1


_AdGenY1731LocalMepLbrResultOk_Type.__name__ = "TruthValue"
_AdGenY1731LocalMepLbrResultOk_Object = MibTableColumn
adGenY1731LocalMepLbrResultOk = _AdGenY1731LocalMepLbrResultOk_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2, 1, 1),
    _AdGenY1731LocalMepLbrResultOk_Type()
)
adGenY1731LocalMepLbrResultOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbrResultOk.setStatus("current")
_AdGenY1731LocalMepLbrResponseTimeMin_Type = Unsigned32
_AdGenY1731LocalMepLbrResponseTimeMin_Object = MibTableColumn
adGenY1731LocalMepLbrResponseTimeMin = _AdGenY1731LocalMepLbrResponseTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2, 1, 2),
    _AdGenY1731LocalMepLbrResponseTimeMin_Type()
)
adGenY1731LocalMepLbrResponseTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbrResponseTimeMin.setStatus("current")
_AdGenY1731LocalMepLbrResponseTimeMax_Type = Unsigned32
_AdGenY1731LocalMepLbrResponseTimeMax_Object = MibTableColumn
adGenY1731LocalMepLbrResponseTimeMax = _AdGenY1731LocalMepLbrResponseTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2, 1, 3),
    _AdGenY1731LocalMepLbrResponseTimeMax_Type()
)
adGenY1731LocalMepLbrResponseTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbrResponseTimeMax.setStatus("current")
_AdGenY1731LocalMepLbrResponseTimeAvg_Type = Unsigned32
_AdGenY1731LocalMepLbrResponseTimeAvg_Object = MibTableColumn
adGenY1731LocalMepLbrResponseTimeAvg = _AdGenY1731LocalMepLbrResponseTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2, 1, 4),
    _AdGenY1731LocalMepLbrResponseTimeAvg_Type()
)
adGenY1731LocalMepLbrResponseTimeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbrResponseTimeAvg.setStatus("current")
_AdGenY1731LocalMepLbrIn_Type = Counter32
_AdGenY1731LocalMepLbrIn_Object = MibTableColumn
adGenY1731LocalMepLbrIn = _AdGenY1731LocalMepLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2, 1, 5),
    _AdGenY1731LocalMepLbrIn_Type()
)
adGenY1731LocalMepLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbrIn.setStatus("current")
_AdGenY1731LocalMepLbrInOutOfOrder_Type = Counter32
_AdGenY1731LocalMepLbrInOutOfOrder_Object = MibTableColumn
adGenY1731LocalMepLbrInOutOfOrder = _AdGenY1731LocalMepLbrInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2, 1, 6),
    _AdGenY1731LocalMepLbrInOutOfOrder_Type()
)
adGenY1731LocalMepLbrInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbrInOutOfOrder.setStatus("current")
_AdGenY1731LocalMepLbrBadMsdu_Type = Counter32
_AdGenY1731LocalMepLbrBadMsdu_Object = MibTableColumn
adGenY1731LocalMepLbrBadMsdu = _AdGenY1731LocalMepLbrBadMsdu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2, 1, 7),
    _AdGenY1731LocalMepLbrBadMsdu_Type()
)
adGenY1731LocalMepLbrBadMsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbrBadMsdu.setStatus("current")
_AdGenY1731LocalMepLbmOut_Type = Counter32
_AdGenY1731LocalMepLbmOut_Object = MibTableColumn
adGenY1731LocalMepLbmOut = _AdGenY1731LocalMepLbmOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 2, 1, 8),
    _AdGenY1731LocalMepLbmOut_Type()
)
adGenY1731LocalMepLbmOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmOut.setStatus("current")
_AdGenY1731LocalMepLbmResponderTable_Object = MibTable
adGenY1731LocalMepLbmResponderTable = _AdGenY1731LocalMepLbmResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmResponderTable.setStatus("current")
_AdGenY1731LocalMepLbmResponderEntry_Object = MibTableRow
adGenY1731LocalMepLbmResponderEntry = _AdGenY1731LocalMepLbmResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 3, 1)
)
adGenY1731LocalMepLbmResponderEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmResponderEntry.setStatus("current")
_AdgenY1731LocalMepLbrOut_Type = Counter32
_AdgenY1731LocalMepLbrOut_Object = MibTableColumn
adgenY1731LocalMepLbrOut = _AdgenY1731LocalMepLbrOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 3, 1, 1),
    _AdgenY1731LocalMepLbrOut_Type()
)
adgenY1731LocalMepLbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adgenY1731LocalMepLbrOut.setStatus("current")
_AdGenY1731LocalMepLbmIn_Type = Counter32
_AdGenY1731LocalMepLbmIn_Object = MibTableColumn
adGenY1731LocalMepLbmIn = _AdGenY1731LocalMepLbmIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 3, 3, 1, 2),
    _AdGenY1731LocalMepLbmIn_Type()
)
adGenY1731LocalMepLbmIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLbmIn.setStatus("current")
_AdGenY1731LocalMepDmm_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepDmm = _AdGenY1731LocalMepDmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4)
)
_AdGenY1731DmmScalars_ObjectIdentity = ObjectIdentity
adGenY1731DmmScalars = _AdGenY1731DmmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 1)
)
_AdGenY1731DmmSessionMaxNumber_Type = Unsigned32
_AdGenY1731DmmSessionMaxNumber_Object = MibScalar
adGenY1731DmmSessionMaxNumber = _AdGenY1731DmmSessionMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 1, 1),
    _AdGenY1731DmmSessionMaxNumber_Type()
)
adGenY1731DmmSessionMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionMaxNumber.setStatus("current")
_AdGenY1731DmmSessionCurrentNumber_Type = Unsigned32
_AdGenY1731DmmSessionCurrentNumber_Object = MibScalar
adGenY1731DmmSessionCurrentNumber = _AdGenY1731DmmSessionCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 1, 2),
    _AdGenY1731DmmSessionCurrentNumber_Type()
)
adGenY1731DmmSessionCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionCurrentNumber.setStatus("current")
_AdGenY1731DmmSessionLastCreateError_Type = DisplayString
_AdGenY1731DmmSessionLastCreateError_Object = MibScalar
adGenY1731DmmSessionLastCreateError = _AdGenY1731DmmSessionLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 1, 3),
    _AdGenY1731DmmSessionLastCreateError_Type()
)
adGenY1731DmmSessionLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionLastCreateError.setStatus("current")
_AdGenY1731DmmSessionTransmitTable_Object = MibTable
adGenY1731DmmSessionTransmitTable = _AdGenY1731DmmSessionTransmitTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    adGenY1731DmmSessionTransmitTable.setStatus("current")
_AdGenY1731DmmSessionTransmitEntry_Object = MibTableRow
adGenY1731DmmSessionTransmitEntry = _AdGenY1731DmmSessionTransmitEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1)
)
adGenY1731DmmSessionTransmitEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731DmmSessionTargetRmepIdOrMacAddress"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731DmmSessionTarget"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731DmmSessionVlanPriority"),
)
if mibBuilder.loadTexts:
    adGenY1731DmmSessionTransmitEntry.setStatus("current")


class _AdGenY1731DmmSessionTargetRmepIdOrMacAddress_Type(Integer32):
    """Custom type adGenY1731DmmSessionTargetRmepIdOrMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmepId", 1),
          ("macAddress", 2))
    )


_AdGenY1731DmmSessionTargetRmepIdOrMacAddress_Type.__name__ = "Integer32"
_AdGenY1731DmmSessionTargetRmepIdOrMacAddress_Object = MibTableColumn
adGenY1731DmmSessionTargetRmepIdOrMacAddress = _AdGenY1731DmmSessionTargetRmepIdOrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 1),
    _AdGenY1731DmmSessionTargetRmepIdOrMacAddress_Type()
)
adGenY1731DmmSessionTargetRmepIdOrMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionTargetRmepIdOrMacAddress.setStatus("current")


class _AdGenY1731DmmSessionTarget_Type(OctetString):
    """Custom type adGenY1731DmmSessionTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_AdGenY1731DmmSessionTarget_Type.__name__ = "OctetString"
_AdGenY1731DmmSessionTarget_Object = MibTableColumn
adGenY1731DmmSessionTarget = _AdGenY1731DmmSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 2),
    _AdGenY1731DmmSessionTarget_Type()
)
adGenY1731DmmSessionTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionTarget.setStatus("current")


class _AdGenY1731DmmSessionVlanPriority_Type(Integer32):
    """Custom type adGenY1731DmmSessionVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenY1731DmmSessionVlanPriority_Type.__name__ = "Integer32"
_AdGenY1731DmmSessionVlanPriority_Object = MibTableColumn
adGenY1731DmmSessionVlanPriority = _AdGenY1731DmmSessionVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 3),
    _AdGenY1731DmmSessionVlanPriority_Type()
)
adGenY1731DmmSessionVlanPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionVlanPriority.setStatus("current")


class _AdGenY1731DmmSessionTargetRemoteMepIdentifier_Type(Integer32):
    """Custom type adGenY1731DmmSessionTargetRemoteMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenY1731DmmSessionTargetRemoteMepIdentifier_Type.__name__ = "Integer32"
_AdGenY1731DmmSessionTargetRemoteMepIdentifier_Object = MibTableColumn
adGenY1731DmmSessionTargetRemoteMepIdentifier = _AdGenY1731DmmSessionTargetRemoteMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 4),
    _AdGenY1731DmmSessionTargetRemoteMepIdentifier_Type()
)
adGenY1731DmmSessionTargetRemoteMepIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionTargetRemoteMepIdentifier.setStatus("current")
_AdGenY1731DmmSessionTargetMacAddress_Type = MacAddress
_AdGenY1731DmmSessionTargetMacAddress_Object = MibTableColumn
adGenY1731DmmSessionTargetMacAddress = _AdGenY1731DmmSessionTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 5),
    _AdGenY1731DmmSessionTargetMacAddress_Type()
)
adGenY1731DmmSessionTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionTargetMacAddress.setStatus("current")
_AdGenY1731DmmSessionRowStatus_Type = RowStatus
_AdGenY1731DmmSessionRowStatus_Object = MibTableColumn
adGenY1731DmmSessionRowStatus = _AdGenY1731DmmSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 6),
    _AdGenY1731DmmSessionRowStatus_Type()
)
adGenY1731DmmSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionRowStatus.setStatus("current")
_AdGenY1731DmmSessionAdminState_Type = TruthValue
_AdGenY1731DmmSessionAdminState_Object = MibTableColumn
adGenY1731DmmSessionAdminState = _AdGenY1731DmmSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 7),
    _AdGenY1731DmmSessionAdminState_Type()
)
adGenY1731DmmSessionAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionAdminState.setStatus("current")


class _AdGenY1731DmmSessionStatus_Type(Integer32):
    """Custom type adGenY1731DmmSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notRunning", 2))
    )


_AdGenY1731DmmSessionStatus_Type.__name__ = "Integer32"
_AdGenY1731DmmSessionStatus_Object = MibTableColumn
adGenY1731DmmSessionStatus = _AdGenY1731DmmSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 8),
    _AdGenY1731DmmSessionStatus_Type()
)
adGenY1731DmmSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionStatus.setStatus("current")
_AdGenY1731DmmSessionStatusString_Type = DisplayString
_AdGenY1731DmmSessionStatusString_Object = MibTableColumn
adGenY1731DmmSessionStatusString = _AdGenY1731DmmSessionStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 9),
    _AdGenY1731DmmSessionStatusString_Type()
)
adGenY1731DmmSessionStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionStatusString.setStatus("current")


class _AdGenY1731DmmSessionInterframeDelay_Type(Integer32):
    """Custom type adGenY1731DmmSessionInterframeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdGenY1731DmmSessionInterframeDelay_Type.__name__ = "Integer32"
_AdGenY1731DmmSessionInterframeDelay_Object = MibTableColumn
adGenY1731DmmSessionInterframeDelay = _AdGenY1731DmmSessionInterframeDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 10),
    _AdGenY1731DmmSessionInterframeDelay_Type()
)
adGenY1731DmmSessionInterframeDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionInterframeDelay.setStatus("current")


class _AdGenY1731DmmSessionMeasurementInterval_Type(Integer32):
    """Custom type adGenY1731DmmSessionMeasurementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_AdGenY1731DmmSessionMeasurementInterval_Type.__name__ = "Integer32"
_AdGenY1731DmmSessionMeasurementInterval_Object = MibTableColumn
adGenY1731DmmSessionMeasurementInterval = _AdGenY1731DmmSessionMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 11),
    _AdGenY1731DmmSessionMeasurementInterval_Type()
)
adGenY1731DmmSessionMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionMeasurementInterval.setStatus("current")
_AdGenY1731DmmSessionSize_Type = Integer32
_AdGenY1731DmmSessionSize_Object = MibTableColumn
adGenY1731DmmSessionSize = _AdGenY1731DmmSessionSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 12),
    _AdGenY1731DmmSessionSize_Type()
)
adGenY1731DmmSessionSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionSize.setStatus("current")


class _AdGenY1731DmmSessionData_Type(OctetString):
    """Custom type adGenY1731DmmSessionData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AdGenY1731DmmSessionData_Type.__name__ = "OctetString"
_AdGenY1731DmmSessionData_Object = MibTableColumn
adGenY1731DmmSessionData = _AdGenY1731DmmSessionData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 13),
    _AdGenY1731DmmSessionData_Type()
)
adGenY1731DmmSessionData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionData.setStatus("current")


class _AdGenY1731DmmSessionBulkDataExportFileTypes_Type(Integer32):
    """Custom type adGenY1731DmmSessionBulkDataExportFileTypes based on Integer32"""
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
        *(("none", 1),
          ("average", 2),
          ("raw", 3),
          ("averageAndRaw", 4))
    )


_AdGenY1731DmmSessionBulkDataExportFileTypes_Type.__name__ = "Integer32"
_AdGenY1731DmmSessionBulkDataExportFileTypes_Object = MibTableColumn
adGenY1731DmmSessionBulkDataExportFileTypes = _AdGenY1731DmmSessionBulkDataExportFileTypes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 4, 2, 1, 14),
    _AdGenY1731DmmSessionBulkDataExportFileTypes_Type()
)
adGenY1731DmmSessionBulkDataExportFileTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731DmmSessionBulkDataExportFileTypes.setStatus("current")
_AdGenY1731LocalMepLmm_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepLmm = _AdGenY1731LocalMepLmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5)
)
_AdGenY1731LmmScalars_ObjectIdentity = ObjectIdentity
adGenY1731LmmScalars = _AdGenY1731LmmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 1)
)
_AdGenY1731LmmSessionMaxNumber_Type = Unsigned32
_AdGenY1731LmmSessionMaxNumber_Object = MibScalar
adGenY1731LmmSessionMaxNumber = _AdGenY1731LmmSessionMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 1, 1),
    _AdGenY1731LmmSessionMaxNumber_Type()
)
adGenY1731LmmSessionMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionMaxNumber.setStatus("current")
_AdGenY1731LmmSessionCurrentNumber_Type = Unsigned32
_AdGenY1731LmmSessionCurrentNumber_Object = MibScalar
adGenY1731LmmSessionCurrentNumber = _AdGenY1731LmmSessionCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 1, 2),
    _AdGenY1731LmmSessionCurrentNumber_Type()
)
adGenY1731LmmSessionCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionCurrentNumber.setStatus("current")
_AdGenY1731LmmSessionLastCreateError_Type = DisplayString
_AdGenY1731LmmSessionLastCreateError_Object = MibScalar
adGenY1731LmmSessionLastCreateError = _AdGenY1731LmmSessionLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 1, 3),
    _AdGenY1731LmmSessionLastCreateError_Type()
)
adGenY1731LmmSessionLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionLastCreateError.setStatus("current")
_AdGenY1731LmmSessionTransmitTable_Object = MibTable
adGenY1731LmmSessionTransmitTable = _AdGenY1731LmmSessionTransmitTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    adGenY1731LmmSessionTransmitTable.setStatus("current")
_AdGenY1731LmmSessionTransmitEntry_Object = MibTableRow
adGenY1731LmmSessionTransmitEntry = _AdGenY1731LmmSessionTransmitEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1)
)
adGenY1731LmmSessionTransmitEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LmmSessionTargetRmepIdOrMacAddress"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LmmSessionTarget"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LmmSessionVlanPriority"),
)
if mibBuilder.loadTexts:
    adGenY1731LmmSessionTransmitEntry.setStatus("current")


class _AdGenY1731LmmSessionTargetRmepIdOrMacAddress_Type(Integer32):
    """Custom type adGenY1731LmmSessionTargetRmepIdOrMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmepId", 1),
          ("macAddress", 2))
    )


_AdGenY1731LmmSessionTargetRmepIdOrMacAddress_Type.__name__ = "Integer32"
_AdGenY1731LmmSessionTargetRmepIdOrMacAddress_Object = MibTableColumn
adGenY1731LmmSessionTargetRmepIdOrMacAddress = _AdGenY1731LmmSessionTargetRmepIdOrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 1),
    _AdGenY1731LmmSessionTargetRmepIdOrMacAddress_Type()
)
adGenY1731LmmSessionTargetRmepIdOrMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionTargetRmepIdOrMacAddress.setStatus("current")


class _AdGenY1731LmmSessionTarget_Type(OctetString):
    """Custom type adGenY1731LmmSessionTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_AdGenY1731LmmSessionTarget_Type.__name__ = "OctetString"
_AdGenY1731LmmSessionTarget_Object = MibTableColumn
adGenY1731LmmSessionTarget = _AdGenY1731LmmSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 2),
    _AdGenY1731LmmSessionTarget_Type()
)
adGenY1731LmmSessionTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionTarget.setStatus("current")


class _AdGenY1731LmmSessionVlanPriority_Type(Integer32):
    """Custom type adGenY1731LmmSessionVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenY1731LmmSessionVlanPriority_Type.__name__ = "Integer32"
_AdGenY1731LmmSessionVlanPriority_Object = MibTableColumn
adGenY1731LmmSessionVlanPriority = _AdGenY1731LmmSessionVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 3),
    _AdGenY1731LmmSessionVlanPriority_Type()
)
adGenY1731LmmSessionVlanPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionVlanPriority.setStatus("current")


class _AdGenY1731LmmSessionTargetRemoteMepIdentifier_Type(Integer32):
    """Custom type adGenY1731LmmSessionTargetRemoteMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenY1731LmmSessionTargetRemoteMepIdentifier_Type.__name__ = "Integer32"
_AdGenY1731LmmSessionTargetRemoteMepIdentifier_Object = MibTableColumn
adGenY1731LmmSessionTargetRemoteMepIdentifier = _AdGenY1731LmmSessionTargetRemoteMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 4),
    _AdGenY1731LmmSessionTargetRemoteMepIdentifier_Type()
)
adGenY1731LmmSessionTargetRemoteMepIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionTargetRemoteMepIdentifier.setStatus("current")
_AdGenY1731LmmSessionTargetMacAddress_Type = MacAddress
_AdGenY1731LmmSessionTargetMacAddress_Object = MibTableColumn
adGenY1731LmmSessionTargetMacAddress = _AdGenY1731LmmSessionTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 5),
    _AdGenY1731LmmSessionTargetMacAddress_Type()
)
adGenY1731LmmSessionTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionTargetMacAddress.setStatus("current")
_AdGenY1731LmmSessionRowStatus_Type = RowStatus
_AdGenY1731LmmSessionRowStatus_Object = MibTableColumn
adGenY1731LmmSessionRowStatus = _AdGenY1731LmmSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 6),
    _AdGenY1731LmmSessionRowStatus_Type()
)
adGenY1731LmmSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionRowStatus.setStatus("current")
_AdGenY1731LmmSessionAdminState_Type = TruthValue
_AdGenY1731LmmSessionAdminState_Object = MibTableColumn
adGenY1731LmmSessionAdminState = _AdGenY1731LmmSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 7),
    _AdGenY1731LmmSessionAdminState_Type()
)
adGenY1731LmmSessionAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionAdminState.setStatus("current")


class _AdGenY1731LmmSessionStatus_Type(Integer32):
    """Custom type adGenY1731LmmSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notRunning", 2))
    )


_AdGenY1731LmmSessionStatus_Type.__name__ = "Integer32"
_AdGenY1731LmmSessionStatus_Object = MibTableColumn
adGenY1731LmmSessionStatus = _AdGenY1731LmmSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 8),
    _AdGenY1731LmmSessionStatus_Type()
)
adGenY1731LmmSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionStatus.setStatus("current")
_AdGenY1731LmmSessionStatusString_Type = DisplayString
_AdGenY1731LmmSessionStatusString_Object = MibTableColumn
adGenY1731LmmSessionStatusString = _AdGenY1731LmmSessionStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 9),
    _AdGenY1731LmmSessionStatusString_Type()
)
adGenY1731LmmSessionStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionStatusString.setStatus("current")


class _AdGenY1731LmmSessionInterframeDelay_Type(Integer32):
    """Custom type adGenY1731LmmSessionInterframeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdGenY1731LmmSessionInterframeDelay_Type.__name__ = "Integer32"
_AdGenY1731LmmSessionInterframeDelay_Object = MibTableColumn
adGenY1731LmmSessionInterframeDelay = _AdGenY1731LmmSessionInterframeDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 10),
    _AdGenY1731LmmSessionInterframeDelay_Type()
)
adGenY1731LmmSessionInterframeDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionInterframeDelay.setStatus("current")


class _AdGenY1731LmmSessionMeasurementInterval_Type(Integer32):
    """Custom type adGenY1731LmmSessionMeasurementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_AdGenY1731LmmSessionMeasurementInterval_Type.__name__ = "Integer32"
_AdGenY1731LmmSessionMeasurementInterval_Object = MibTableColumn
adGenY1731LmmSessionMeasurementInterval = _AdGenY1731LmmSessionMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 11),
    _AdGenY1731LmmSessionMeasurementInterval_Type()
)
adGenY1731LmmSessionMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionMeasurementInterval.setStatus("current")
_AdGenY1731LmmSessionSize_Type = Integer32
_AdGenY1731LmmSessionSize_Object = MibTableColumn
adGenY1731LmmSessionSize = _AdGenY1731LmmSessionSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 12),
    _AdGenY1731LmmSessionSize_Type()
)
adGenY1731LmmSessionSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionSize.setStatus("current")


class _AdGenY1731LmmSessionData_Type(OctetString):
    """Custom type adGenY1731LmmSessionData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AdGenY1731LmmSessionData_Type.__name__ = "OctetString"
_AdGenY1731LmmSessionData_Object = MibTableColumn
adGenY1731LmmSessionData = _AdGenY1731LmmSessionData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 13),
    _AdGenY1731LmmSessionData_Type()
)
adGenY1731LmmSessionData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionData.setStatus("current")


class _AdGenY1731LmmSessionBulkDataExportFileTypes_Type(Integer32):
    """Custom type adGenY1731LmmSessionBulkDataExportFileTypes based on Integer32"""
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
        *(("none", 1),
          ("average", 2),
          ("raw", 3),
          ("averageAndRaw", 4))
    )


_AdGenY1731LmmSessionBulkDataExportFileTypes_Type.__name__ = "Integer32"
_AdGenY1731LmmSessionBulkDataExportFileTypes_Object = MibTableColumn
adGenY1731LmmSessionBulkDataExportFileTypes = _AdGenY1731LmmSessionBulkDataExportFileTypes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 5, 2, 1, 14),
    _AdGenY1731LmmSessionBulkDataExportFileTypes_Type()
)
adGenY1731LmmSessionBulkDataExportFileTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731LmmSessionBulkDataExportFileTypes.setStatus("current")
_AdGenY1731LocalMepLtm_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepLtm = _AdGenY1731LocalMepLtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6)
)
_AdGenY1731LocalMepLtmTable_Object = MibTable
adGenY1731LocalMepLtmTable = _AdGenY1731LocalMepLtmTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmTable.setStatus("current")
_AdGenY1731LocalMepLtmEntry_Object = MibTableRow
adGenY1731LocalMepLtmEntry = _AdGenY1731LocalMepLtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1)
)
adGenY1731LocalMepLtmEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmEntry.setStatus("current")
_AdGenY1731LocalMepLtmNextTransactionId_Type = Unsigned32
_AdGenY1731LocalMepLtmNextTransactionId_Object = MibTableColumn
adGenY1731LocalMepLtmNextTransactionId = _AdGenY1731LocalMepLtmNextTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 1),
    _AdGenY1731LocalMepLtmNextTransactionId_Type()
)
adGenY1731LocalMepLtmNextTransactionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmNextTransactionId.setStatus("current")
_AdGenY1731LocalMepUnexpLtrIn_Type = Counter32
_AdGenY1731LocalMepUnexpLtrIn_Object = MibTableColumn
adGenY1731LocalMepUnexpLtrIn = _AdGenY1731LocalMepUnexpLtrIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 2),
    _AdGenY1731LocalMepUnexpLtrIn_Type()
)
adGenY1731LocalMepUnexpLtrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepUnexpLtrIn.setStatus("current")


class _AdGenY1731LocalMepTransmitLtmStatus_Type(TruthValue):
    """Custom type adGenY1731LocalMepTransmitLtmStatus based on TruthValue"""
    defaultValue = 1


_AdGenY1731LocalMepTransmitLtmStatus_Type.__name__ = "TruthValue"
_AdGenY1731LocalMepTransmitLtmStatus_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmStatus = _AdGenY1731LocalMepTransmitLtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 3),
    _AdGenY1731LocalMepTransmitLtmStatus_Type()
)
adGenY1731LocalMepTransmitLtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmStatus.setStatus("current")


class _AdGenY1731LocalMepTransmitLtmFlags_Type(Bits):
    """Custom type adGenY1731LocalMepTransmitLtmFlags based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        ("useFDBonly", 0)
    )

_AdGenY1731LocalMepTransmitLtmFlags_Type.__name__ = "Bits"
_AdGenY1731LocalMepTransmitLtmFlags_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmFlags = _AdGenY1731LocalMepTransmitLtmFlags_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 4),
    _AdGenY1731LocalMepTransmitLtmFlags_Type()
)
adGenY1731LocalMepTransmitLtmFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmFlags.setStatus("current")
_AdGenY1731LocalMepTransmitLtmTargetMacAddress_Type = MacAddress
_AdGenY1731LocalMepTransmitLtmTargetMacAddress_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmTargetMacAddress = _AdGenY1731LocalMepTransmitLtmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 5),
    _AdGenY1731LocalMepTransmitLtmTargetMacAddress_Type()
)
adGenY1731LocalMepTransmitLtmTargetMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmTargetMacAddress.setStatus("current")


class _AdGenY1731LocalMepTransmitLtmTargetMepId_Type(Integer32):
    """Custom type adGenY1731LocalMepTransmitLtmTargetMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenY1731LocalMepTransmitLtmTargetMepId_Type.__name__ = "Integer32"
_AdGenY1731LocalMepTransmitLtmTargetMepId_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmTargetMepId = _AdGenY1731LocalMepTransmitLtmTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 6),
    _AdGenY1731LocalMepTransmitLtmTargetMepId_Type()
)
adGenY1731LocalMepTransmitLtmTargetMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmTargetMepId.setStatus("current")
_AdGenY1731LocalMepTransmitLtmTargetIsMepId_Type = TruthValue
_AdGenY1731LocalMepTransmitLtmTargetIsMepId_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmTargetIsMepId = _AdGenY1731LocalMepTransmitLtmTargetIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 7),
    _AdGenY1731LocalMepTransmitLtmTargetIsMepId_Type()
)
adGenY1731LocalMepTransmitLtmTargetIsMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmTargetIsMepId.setStatus("current")


class _AdGenY1731LocalMepTransmitLtmTtl_Type(Unsigned32):
    """Custom type adGenY1731LocalMepTransmitLtmTtl based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenY1731LocalMepTransmitLtmTtl_Type.__name__ = "Unsigned32"
_AdGenY1731LocalMepTransmitLtmTtl_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmTtl = _AdGenY1731LocalMepTransmitLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 8),
    _AdGenY1731LocalMepTransmitLtmTtl_Type()
)
adGenY1731LocalMepTransmitLtmTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmTtl.setStatus("current")


class _AdGenY1731LocalMepTransmitLtmResult_Type(TruthValue):
    """Custom type adGenY1731LocalMepTransmitLtmResult based on TruthValue"""
    defaultValue = 1


_AdGenY1731LocalMepTransmitLtmResult_Type.__name__ = "TruthValue"
_AdGenY1731LocalMepTransmitLtmResult_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmResult = _AdGenY1731LocalMepTransmitLtmResult_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 9),
    _AdGenY1731LocalMepTransmitLtmResult_Type()
)
adGenY1731LocalMepTransmitLtmResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmResult.setStatus("current")
_AdGenY1731LocalMepTransmitLtmTransactionId_Type = Unsigned32
_AdGenY1731LocalMepTransmitLtmTransactionId_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmTransactionId = _AdGenY1731LocalMepTransmitLtmTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 10),
    _AdGenY1731LocalMepTransmitLtmTransactionId_Type()
)
adGenY1731LocalMepTransmitLtmTransactionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmTransactionId.setStatus("current")


class _AdGenY1731LocalMepTransmitLtmEgressIdentifier_Type(OctetString):
    """Custom type adGenY1731LocalMepTransmitLtmEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AdGenY1731LocalMepTransmitLtmEgressIdentifier_Type.__name__ = "OctetString"
_AdGenY1731LocalMepTransmitLtmEgressIdentifier_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmEgressIdentifier = _AdGenY1731LocalMepTransmitLtmEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 11),
    _AdGenY1731LocalMepTransmitLtmEgressIdentifier_Type()
)
adGenY1731LocalMepTransmitLtmEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmEgressIdentifier.setStatus("current")
_AdGenY1731LocalMepTransmitLtmStatusString_Type = DisplayString
_AdGenY1731LocalMepTransmitLtmStatusString_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmStatusString = _AdGenY1731LocalMepTransmitLtmStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 12),
    _AdGenY1731LocalMepTransmitLtmStatusString_Type()
)
adGenY1731LocalMepTransmitLtmStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmStatusString.setStatus("current")
_AdGenY1731LocalMepTransmitLtmConfigStatus_Type = TruthValue
_AdGenY1731LocalMepTransmitLtmConfigStatus_Object = MibTableColumn
adGenY1731LocalMepTransmitLtmConfigStatus = _AdGenY1731LocalMepTransmitLtmConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 13),
    _AdGenY1731LocalMepTransmitLtmConfigStatus_Type()
)
adGenY1731LocalMepTransmitLtmConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepTransmitLtmConfigStatus.setStatus("current")


class _AdGenY1731LocalMepLtmActive_Type(TruthValue):
    """Custom type adGenY1731LocalMepLtmActive based on TruthValue"""
    defaultValue = 2


_AdGenY1731LocalMepLtmActive_Type.__name__ = "TruthValue"
_AdGenY1731LocalMepLtmActive_Object = MibTableColumn
adGenY1731LocalMepLtmActive = _AdGenY1731LocalMepLtmActive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 14),
    _AdGenY1731LocalMepLtmActive_Type()
)
adGenY1731LocalMepLtmActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmActive.setStatus("current")
_AdGenY1731LocalMepLtmTotalOut_Type = Counter32
_AdGenY1731LocalMepLtmTotalOut_Object = MibTableColumn
adGenY1731LocalMepLtmTotalOut = _AdGenY1731LocalMepLtmTotalOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 15),
    _AdGenY1731LocalMepLtmTotalOut_Type()
)
adGenY1731LocalMepLtmTotalOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmTotalOut.setStatus("current")
_AdGenY1731LocalMepLtrTotalIn_Type = Counter32
_AdGenY1731LocalMepLtrTotalIn_Object = MibTableColumn
adGenY1731LocalMepLtrTotalIn = _AdGenY1731LocalMepLtrTotalIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 16),
    _AdGenY1731LocalMepLtrTotalIn_Type()
)
adGenY1731LocalMepLtrTotalIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrTotalIn.setStatus("current")
_AdGenY1731LocalMepLtrTotalInvalidIn_Type = Counter32
_AdGenY1731LocalMepLtrTotalInvalidIn_Object = MibTableColumn
adGenY1731LocalMepLtrTotalInvalidIn = _AdGenY1731LocalMepLtrTotalInvalidIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 17),
    _AdGenY1731LocalMepLtrTotalInvalidIn_Type()
)
adGenY1731LocalMepLtrTotalInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrTotalInvalidIn.setStatus("current")
_AdGenY1731LocalMepLtrTotalValidIn_Type = Counter32
_AdGenY1731LocalMepLtrTotalValidIn_Object = MibTableColumn
adGenY1731LocalMepLtrTotalValidIn = _AdGenY1731LocalMepLtrTotalValidIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 1, 1, 18),
    _AdGenY1731LocalMepLtrTotalValidIn_Type()
)
adGenY1731LocalMepLtrTotalValidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrTotalValidIn.setStatus("current")
_AdGenY1731LocalMepLtSessionTable_Object = MibTable
adGenY1731LocalMepLtSessionTable = _AdGenY1731LocalMepLtSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtSessionTable.setStatus("current")
_AdGenY1731LocalMepLtSessionEntry_Object = MibTableRow
adGenY1731LocalMepLtSessionEntry = _AdGenY1731LocalMepLtSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 2, 1)
)
adGenY1731LocalMepLtSessionEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepLtmTransactionId"),
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtSessionEntry.setStatus("current")


class _AdGenY1731LocalMepLtmTransactionId_Type(Unsigned32):
    """Custom type adGenY1731LocalMepLtmTransactionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenY1731LocalMepLtmTransactionId_Type.__name__ = "Unsigned32"
_AdGenY1731LocalMepLtmTransactionId_Object = MibTableColumn
adGenY1731LocalMepLtmTransactionId = _AdGenY1731LocalMepLtmTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 2, 1, 1),
    _AdGenY1731LocalMepLtmTransactionId_Type()
)
adGenY1731LocalMepLtmTransactionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmTransactionId.setStatus("current")
_AdGenY1731LocalMepLtmOut_Type = Counter32
_AdGenY1731LocalMepLtmOut_Object = MibTableColumn
adGenY1731LocalMepLtmOut = _AdGenY1731LocalMepLtmOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 2, 1, 2),
    _AdGenY1731LocalMepLtmOut_Type()
)
adGenY1731LocalMepLtmOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmOut.setStatus("current")
_AdGenY1731LocalMepLtrIn_Type = Counter32
_AdGenY1731LocalMepLtrIn_Object = MibTableColumn
adGenY1731LocalMepLtrIn = _AdGenY1731LocalMepLtrIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 2, 1, 3),
    _AdGenY1731LocalMepLtrIn_Type()
)
adGenY1731LocalMepLtrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrIn.setStatus("current")
_AdGenY1731LocalMepLtrInvalidIn_Type = Counter32
_AdGenY1731LocalMepLtrInvalidIn_Object = MibTableColumn
adGenY1731LocalMepLtrInvalidIn = _AdGenY1731LocalMepLtrInvalidIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 2, 1, 4),
    _AdGenY1731LocalMepLtrInvalidIn_Type()
)
adGenY1731LocalMepLtrInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrInvalidIn.setStatus("current")
_AdGenY1731LocalMepLtrValidIn_Type = Counter32
_AdGenY1731LocalMepLtrValidIn_Object = MibTableColumn
adGenY1731LocalMepLtrValidIn = _AdGenY1731LocalMepLtrValidIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 2, 1, 5),
    _AdGenY1731LocalMepLtrValidIn_Type()
)
adGenY1731LocalMepLtrValidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrValidIn.setStatus("current")
_AdGenY1731LocalMepLtTimeRemaining_Type = Unsigned32
_AdGenY1731LocalMepLtTimeRemaining_Object = MibTableColumn
adGenY1731LocalMepLtTimeRemaining = _AdGenY1731LocalMepLtTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 2, 1, 6),
    _AdGenY1731LocalMepLtTimeRemaining_Type()
)
adGenY1731LocalMepLtTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtTimeRemaining.setStatus("current")
_AdGenY1731LocalMepLtrTable_Object = MibTable
adGenY1731LocalMepLtrTable = _AdGenY1731LocalMepLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3)
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrTable.setStatus("current")
_AdGenY1731LocalMepLtrEntry_Object = MibTableRow
adGenY1731LocalMepLtrEntry = _AdGenY1731LocalMepLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1)
)
adGenY1731LocalMepLtrEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepLtrTransactionId"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepLtrReceiveOrder"),
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrEntry.setStatus("current")


class _AdGenY1731LocalMepLtrTransactionId_Type(Unsigned32):
    """Custom type adGenY1731LocalMepLtrTransactionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AdGenY1731LocalMepLtrTransactionId_Type.__name__ = "Unsigned32"
_AdGenY1731LocalMepLtrTransactionId_Object = MibTableColumn
adGenY1731LocalMepLtrTransactionId = _AdGenY1731LocalMepLtrTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 1),
    _AdGenY1731LocalMepLtrTransactionId_Type()
)
adGenY1731LocalMepLtrTransactionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrTransactionId.setStatus("current")


class _AdGenY1731LocalMepLtrReceiveOrder_Type(Unsigned32):
    """Custom type adGenY1731LocalMepLtrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AdGenY1731LocalMepLtrReceiveOrder_Type.__name__ = "Unsigned32"
_AdGenY1731LocalMepLtrReceiveOrder_Object = MibTableColumn
adGenY1731LocalMepLtrReceiveOrder = _AdGenY1731LocalMepLtrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 2),
    _AdGenY1731LocalMepLtrReceiveOrder_Type()
)
adGenY1731LocalMepLtrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrReceiveOrder.setStatus("current")


class _AdGenY1731LocalMepLtrTtl_Type(Unsigned32):
    """Custom type adGenY1731LocalMepLtrTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenY1731LocalMepLtrTtl_Type.__name__ = "Unsigned32"
_AdGenY1731LocalMepLtrTtl_Object = MibTableColumn
adGenY1731LocalMepLtrTtl = _AdGenY1731LocalMepLtrTtl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 3),
    _AdGenY1731LocalMepLtrTtl_Type()
)
adGenY1731LocalMepLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrTtl.setStatus("current")
_AdGenY1731LocalMepLtrForwarded_Type = TruthValue
_AdGenY1731LocalMepLtrForwarded_Object = MibTableColumn
adGenY1731LocalMepLtrForwarded = _AdGenY1731LocalMepLtrForwarded_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 4),
    _AdGenY1731LocalMepLtrForwarded_Type()
)
adGenY1731LocalMepLtrForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrForwarded.setStatus("current")
_AdGenY1731LocalMepLtrTerminalMep_Type = TruthValue
_AdGenY1731LocalMepLtrTerminalMep_Object = MibTableColumn
adGenY1731LocalMepLtrTerminalMep = _AdGenY1731LocalMepLtrTerminalMep_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 5),
    _AdGenY1731LocalMepLtrTerminalMep_Type()
)
adGenY1731LocalMepLtrTerminalMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrTerminalMep.setStatus("current")


class _AdGenY1731LocalMepLtrLastEgressIdentifier_Type(OctetString):
    """Custom type adGenY1731LocalMepLtrLastEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AdGenY1731LocalMepLtrLastEgressIdentifier_Type.__name__ = "OctetString"
_AdGenY1731LocalMepLtrLastEgressIdentifier_Object = MibTableColumn
adGenY1731LocalMepLtrLastEgressIdentifier = _AdGenY1731LocalMepLtrLastEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 6),
    _AdGenY1731LocalMepLtrLastEgressIdentifier_Type()
)
adGenY1731LocalMepLtrLastEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrLastEgressIdentifier.setStatus("current")


class _AdGenY1731LocalMepLtrNextEgressIdentifier_Type(OctetString):
    """Custom type adGenY1731LocalMepLtrNextEgressIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AdGenY1731LocalMepLtrNextEgressIdentifier_Type.__name__ = "OctetString"
_AdGenY1731LocalMepLtrNextEgressIdentifier_Object = MibTableColumn
adGenY1731LocalMepLtrNextEgressIdentifier = _AdGenY1731LocalMepLtrNextEgressIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 7),
    _AdGenY1731LocalMepLtrNextEgressIdentifier_Type()
)
adGenY1731LocalMepLtrNextEgressIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrNextEgressIdentifier.setStatus("current")


class _AdGenY1731LocalMepLtrRelay_Type(Integer32):
    """Custom type adGenY1731LocalMepLtrRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rlyHit", 1),
          ("rlyFdb", 2),
          ("rlyMpdb", 3))
    )


_AdGenY1731LocalMepLtrRelay_Type.__name__ = "Integer32"
_AdGenY1731LocalMepLtrRelay_Object = MibTableColumn
adGenY1731LocalMepLtrRelay = _AdGenY1731LocalMepLtrRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 8),
    _AdGenY1731LocalMepLtrRelay_Type()
)
adGenY1731LocalMepLtrRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrRelay.setStatus("current")


class _AdGenY1731LocalMepLtrChassisIdSubtype_Type(Integer32):
    """Custom type adGenY1731LocalMepLtrChassisIdSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("nonePresent", 0),
          ("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7))
    )


_AdGenY1731LocalMepLtrChassisIdSubtype_Type.__name__ = "Integer32"
_AdGenY1731LocalMepLtrChassisIdSubtype_Object = MibTableColumn
adGenY1731LocalMepLtrChassisIdSubtype = _AdGenY1731LocalMepLtrChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 9),
    _AdGenY1731LocalMepLtrChassisIdSubtype_Type()
)
adGenY1731LocalMepLtrChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrChassisIdSubtype.setStatus("current")
_AdGenY1731LocalMepLtrChassisId_Type = LldpChassisId
_AdGenY1731LocalMepLtrChassisId_Object = MibTableColumn
adGenY1731LocalMepLtrChassisId = _AdGenY1731LocalMepLtrChassisId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 10),
    _AdGenY1731LocalMepLtrChassisId_Type()
)
adGenY1731LocalMepLtrChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrChassisId.setStatus("current")
_AdGenY1731LocalMepLtrManAddressDomain_Type = TDomain
_AdGenY1731LocalMepLtrManAddressDomain_Object = MibTableColumn
adGenY1731LocalMepLtrManAddressDomain = _AdGenY1731LocalMepLtrManAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 11),
    _AdGenY1731LocalMepLtrManAddressDomain_Type()
)
adGenY1731LocalMepLtrManAddressDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrManAddressDomain.setStatus("current")
_AdGenY1731LocalMepLtrManAddress_Type = TAddress
_AdGenY1731LocalMepLtrManAddress_Object = MibTableColumn
adGenY1731LocalMepLtrManAddress = _AdGenY1731LocalMepLtrManAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 12),
    _AdGenY1731LocalMepLtrManAddress_Type()
)
adGenY1731LocalMepLtrManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrManAddress.setStatus("current")


class _AdGenY1731LocalMepLtrIngress_Type(Integer32):
    """Custom type adGenY1731LocalMepLtrIngress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ingNoTlv", 0),
          ("ingOk", 1),
          ("ingDown", 2),
          ("ingBlocked", 3),
          ("ingVid", 4))
    )


_AdGenY1731LocalMepLtrIngress_Type.__name__ = "Integer32"
_AdGenY1731LocalMepLtrIngress_Object = MibTableColumn
adGenY1731LocalMepLtrIngress = _AdGenY1731LocalMepLtrIngress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 13),
    _AdGenY1731LocalMepLtrIngress_Type()
)
adGenY1731LocalMepLtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrIngress.setStatus("current")
_AdGenY1731LocalMepLtrIngressMac_Type = MacAddress
_AdGenY1731LocalMepLtrIngressMac_Object = MibTableColumn
adGenY1731LocalMepLtrIngressMac = _AdGenY1731LocalMepLtrIngressMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 14),
    _AdGenY1731LocalMepLtrIngressMac_Type()
)
adGenY1731LocalMepLtrIngressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrIngressMac.setStatus("current")
_AdGenY1731LocalMepLtrIngressPortIdSubtype_Type = LldpPortIdSubtype
_AdGenY1731LocalMepLtrIngressPortIdSubtype_Object = MibTableColumn
adGenY1731LocalMepLtrIngressPortIdSubtype = _AdGenY1731LocalMepLtrIngressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 15),
    _AdGenY1731LocalMepLtrIngressPortIdSubtype_Type()
)
adGenY1731LocalMepLtrIngressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrIngressPortIdSubtype.setStatus("current")
_AdGenY1731LocalMepLtrIngressPortId_Type = LldpPortId
_AdGenY1731LocalMepLtrIngressPortId_Object = MibTableColumn
adGenY1731LocalMepLtrIngressPortId = _AdGenY1731LocalMepLtrIngressPortId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 16),
    _AdGenY1731LocalMepLtrIngressPortId_Type()
)
adGenY1731LocalMepLtrIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrIngressPortId.setStatus("current")


class _AdGenY1731LocalMepLtrEgress_Type(Integer32):
    """Custom type adGenY1731LocalMepLtrEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("egrNoTlv", 0),
          ("egrOK", 1),
          ("egrDown", 2),
          ("egrBlocked", 3),
          ("egrVid", 4))
    )


_AdGenY1731LocalMepLtrEgress_Type.__name__ = "Integer32"
_AdGenY1731LocalMepLtrEgress_Object = MibTableColumn
adGenY1731LocalMepLtrEgress = _AdGenY1731LocalMepLtrEgress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 17),
    _AdGenY1731LocalMepLtrEgress_Type()
)
adGenY1731LocalMepLtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrEgress.setStatus("current")
_AdGenY1731LocalMepLtrEgressMac_Type = MacAddress
_AdGenY1731LocalMepLtrEgressMac_Object = MibTableColumn
adGenY1731LocalMepLtrEgressMac = _AdGenY1731LocalMepLtrEgressMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 18),
    _AdGenY1731LocalMepLtrEgressMac_Type()
)
adGenY1731LocalMepLtrEgressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrEgressMac.setStatus("current")
_AdGenY1731LocalMepLtrEgressPortIdSubtype_Type = LldpPortIdSubtype
_AdGenY1731LocalMepLtrEgressPortIdSubtype_Object = MibTableColumn
adGenY1731LocalMepLtrEgressPortIdSubtype = _AdGenY1731LocalMepLtrEgressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 19),
    _AdGenY1731LocalMepLtrEgressPortIdSubtype_Type()
)
adGenY1731LocalMepLtrEgressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrEgressPortIdSubtype.setStatus("current")
_AdGenY1731LocalMepLtrEgressPortId_Type = LldpPortId
_AdGenY1731LocalMepLtrEgressPortId_Object = MibTableColumn
adGenY1731LocalMepLtrEgressPortId = _AdGenY1731LocalMepLtrEgressPortId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 20),
    _AdGenY1731LocalMepLtrEgressPortId_Type()
)
adGenY1731LocalMepLtrEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrEgressPortId.setStatus("current")


class _AdGenY1731LocalMepLtrOrganizationSpecificTlv_Type(OctetString):
    """Custom type adGenY1731LocalMepLtrOrganizationSpecificTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 1500),
    )


_AdGenY1731LocalMepLtrOrganizationSpecificTlv_Type.__name__ = "OctetString"
_AdGenY1731LocalMepLtrOrganizationSpecificTlv_Object = MibTableColumn
adGenY1731LocalMepLtrOrganizationSpecificTlv = _AdGenY1731LocalMepLtrOrganizationSpecificTlv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 3, 1, 21),
    _AdGenY1731LocalMepLtrOrganizationSpecificTlv_Type()
)
adGenY1731LocalMepLtrOrganizationSpecificTlv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrOrganizationSpecificTlv.setStatus("current")
_AdGenY1731LocalMepLtmResponderTable_Object = MibTable
adGenY1731LocalMepLtmResponderTable = _AdGenY1731LocalMepLtmResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 4)
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmResponderTable.setStatus("current")
_AdGenY1731LocalMepLtmResponderEntry_Object = MibTableRow
adGenY1731LocalMepLtmResponderEntry = _AdGenY1731LocalMepLtmResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 4, 1)
)
adGenY1731LocalMepLtmResponderEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmResponderEntry.setStatus("current")
_AdGenY1731LocalMepLtmIn_Type = Counter32
_AdGenY1731LocalMepLtmIn_Object = MibTableColumn
adGenY1731LocalMepLtmIn = _AdGenY1731LocalMepLtmIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 4, 1, 1),
    _AdGenY1731LocalMepLtmIn_Type()
)
adGenY1731LocalMepLtmIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmIn.setStatus("current")
_AdGenY1731LocalMepLtmDiscardedInvalidFormat_Type = Counter32
_AdGenY1731LocalMepLtmDiscardedInvalidFormat_Object = MibTableColumn
adGenY1731LocalMepLtmDiscardedInvalidFormat = _AdGenY1731LocalMepLtmDiscardedInvalidFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 4, 1, 2),
    _AdGenY1731LocalMepLtmDiscardedInvalidFormat_Type()
)
adGenY1731LocalMepLtmDiscardedInvalidFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmDiscardedInvalidFormat.setStatus("current")
_AdGenY1731LocalMepLtmDiscardedTtl_Type = Counter32
_AdGenY1731LocalMepLtmDiscardedTtl_Object = MibTableColumn
adGenY1731LocalMepLtmDiscardedTtl = _AdGenY1731LocalMepLtmDiscardedTtl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 4, 1, 3),
    _AdGenY1731LocalMepLtmDiscardedTtl_Type()
)
adGenY1731LocalMepLtmDiscardedTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmDiscardedTtl.setStatus("current")
_AdGenY1731LocalMepLtmDiscardedTargetMac_Type = Counter32
_AdGenY1731LocalMepLtmDiscardedTargetMac_Object = MibTableColumn
adGenY1731LocalMepLtmDiscardedTargetMac = _AdGenY1731LocalMepLtmDiscardedTargetMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 4, 1, 4),
    _AdGenY1731LocalMepLtmDiscardedTargetMac_Type()
)
adGenY1731LocalMepLtmDiscardedTargetMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtmDiscardedTargetMac.setStatus("current")
_AdGenY1731LocalMepLtrOut_Type = Counter32
_AdGenY1731LocalMepLtrOut_Object = MibTableColumn
adGenY1731LocalMepLtrOut = _AdGenY1731LocalMepLtrOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 6, 4, 1, 5),
    _AdGenY1731LocalMepLtrOut_Type()
)
adGenY1731LocalMepLtrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731LocalMepLtrOut.setStatus("current")
_AdGenY1731LocalMepOneDm_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepOneDm = _AdGenY1731LocalMepOneDm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7)
)
_AdGenY1731OneDmScalars_ObjectIdentity = ObjectIdentity
adGenY1731OneDmScalars = _AdGenY1731OneDmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 1)
)
_AdGenY1731OneDmSessionMaxNumber_Type = Unsigned32
_AdGenY1731OneDmSessionMaxNumber_Object = MibScalar
adGenY1731OneDmSessionMaxNumber = _AdGenY1731OneDmSessionMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 1, 1),
    _AdGenY1731OneDmSessionMaxNumber_Type()
)
adGenY1731OneDmSessionMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionMaxNumber.setStatus("current")
_AdGenY1731OneDmSessionCurrentNumber_Type = Unsigned32
_AdGenY1731OneDmSessionCurrentNumber_Object = MibScalar
adGenY1731OneDmSessionCurrentNumber = _AdGenY1731OneDmSessionCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 1, 2),
    _AdGenY1731OneDmSessionCurrentNumber_Type()
)
adGenY1731OneDmSessionCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionCurrentNumber.setStatus("current")
_AdGenY1731OneDmSessionLastCreateError_Type = DisplayString
_AdGenY1731OneDmSessionLastCreateError_Object = MibScalar
adGenY1731OneDmSessionLastCreateError = _AdGenY1731OneDmSessionLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 1, 3),
    _AdGenY1731OneDmSessionLastCreateError_Type()
)
adGenY1731OneDmSessionLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionLastCreateError.setStatus("current")
_AdGenY1731OneDmSessionTransmitTable_Object = MibTable
adGenY1731OneDmSessionTransmitTable = _AdGenY1731OneDmSessionTransmitTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2)
)
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionTransmitTable.setStatus("current")
_AdGenY1731OneDmSessionTransmitEntry_Object = MibTableRow
adGenY1731OneDmSessionTransmitEntry = _AdGenY1731OneDmSessionTransmitEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1)
)
adGenY1731OneDmSessionTransmitEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731OneDmSessionTargetRmepIdOrMacAddress"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731OneDmSessionTarget"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731OneDmSessionVlanPriority"),
)
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionTransmitEntry.setStatus("current")


class _AdGenY1731OneDmSessionTargetRmepIdOrMacAddress_Type(Integer32):
    """Custom type adGenY1731OneDmSessionTargetRmepIdOrMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmepId", 1),
          ("macAddress", 2))
    )


_AdGenY1731OneDmSessionTargetRmepIdOrMacAddress_Type.__name__ = "Integer32"
_AdGenY1731OneDmSessionTargetRmepIdOrMacAddress_Object = MibTableColumn
adGenY1731OneDmSessionTargetRmepIdOrMacAddress = _AdGenY1731OneDmSessionTargetRmepIdOrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 1),
    _AdGenY1731OneDmSessionTargetRmepIdOrMacAddress_Type()
)
adGenY1731OneDmSessionTargetRmepIdOrMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionTargetRmepIdOrMacAddress.setStatus("current")


class _AdGenY1731OneDmSessionTarget_Type(OctetString):
    """Custom type adGenY1731OneDmSessionTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_AdGenY1731OneDmSessionTarget_Type.__name__ = "OctetString"
_AdGenY1731OneDmSessionTarget_Object = MibTableColumn
adGenY1731OneDmSessionTarget = _AdGenY1731OneDmSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 2),
    _AdGenY1731OneDmSessionTarget_Type()
)
adGenY1731OneDmSessionTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionTarget.setStatus("current")


class _AdGenY1731OneDmSessionVlanPriority_Type(Integer32):
    """Custom type adGenY1731OneDmSessionVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenY1731OneDmSessionVlanPriority_Type.__name__ = "Integer32"
_AdGenY1731OneDmSessionVlanPriority_Object = MibTableColumn
adGenY1731OneDmSessionVlanPriority = _AdGenY1731OneDmSessionVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 3),
    _AdGenY1731OneDmSessionVlanPriority_Type()
)
adGenY1731OneDmSessionVlanPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionVlanPriority.setStatus("current")


class _AdGenY1731OneDmSessionTargetRemoteMepIdentifier_Type(Integer32):
    """Custom type adGenY1731OneDmSessionTargetRemoteMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenY1731OneDmSessionTargetRemoteMepIdentifier_Type.__name__ = "Integer32"
_AdGenY1731OneDmSessionTargetRemoteMepIdentifier_Object = MibTableColumn
adGenY1731OneDmSessionTargetRemoteMepIdentifier = _AdGenY1731OneDmSessionTargetRemoteMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 4),
    _AdGenY1731OneDmSessionTargetRemoteMepIdentifier_Type()
)
adGenY1731OneDmSessionTargetRemoteMepIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionTargetRemoteMepIdentifier.setStatus("current")
_AdGenY1731OneDmSessionTargetMacAddress_Type = MacAddress
_AdGenY1731OneDmSessionTargetMacAddress_Object = MibTableColumn
adGenY1731OneDmSessionTargetMacAddress = _AdGenY1731OneDmSessionTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 5),
    _AdGenY1731OneDmSessionTargetMacAddress_Type()
)
adGenY1731OneDmSessionTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionTargetMacAddress.setStatus("current")
_AdGenY1731OneDmSessionRowStatus_Type = RowStatus
_AdGenY1731OneDmSessionRowStatus_Object = MibTableColumn
adGenY1731OneDmSessionRowStatus = _AdGenY1731OneDmSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 6),
    _AdGenY1731OneDmSessionRowStatus_Type()
)
adGenY1731OneDmSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionRowStatus.setStatus("current")
_AdGenY1731OneDmSessionAdminState_Type = TruthValue
_AdGenY1731OneDmSessionAdminState_Object = MibTableColumn
adGenY1731OneDmSessionAdminState = _AdGenY1731OneDmSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 7),
    _AdGenY1731OneDmSessionAdminState_Type()
)
adGenY1731OneDmSessionAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionAdminState.setStatus("current")


class _AdGenY1731OneDmSessionStatus_Type(Integer32):
    """Custom type adGenY1731OneDmSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notRunning", 2))
    )


_AdGenY1731OneDmSessionStatus_Type.__name__ = "Integer32"
_AdGenY1731OneDmSessionStatus_Object = MibTableColumn
adGenY1731OneDmSessionStatus = _AdGenY1731OneDmSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 8),
    _AdGenY1731OneDmSessionStatus_Type()
)
adGenY1731OneDmSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionStatus.setStatus("current")
_AdGenY1731OneDmSessionStatusString_Type = DisplayString
_AdGenY1731OneDmSessionStatusString_Object = MibTableColumn
adGenY1731OneDmSessionStatusString = _AdGenY1731OneDmSessionStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 9),
    _AdGenY1731OneDmSessionStatusString_Type()
)
adGenY1731OneDmSessionStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionStatusString.setStatus("current")


class _AdGenY1731OneDmSessionInterframeDelay_Type(Integer32):
    """Custom type adGenY1731OneDmSessionInterframeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdGenY1731OneDmSessionInterframeDelay_Type.__name__ = "Integer32"
_AdGenY1731OneDmSessionInterframeDelay_Object = MibTableColumn
adGenY1731OneDmSessionInterframeDelay = _AdGenY1731OneDmSessionInterframeDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 10),
    _AdGenY1731OneDmSessionInterframeDelay_Type()
)
adGenY1731OneDmSessionInterframeDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionInterframeDelay.setStatus("current")
_AdGenY1731OneDmSessionSize_Type = Integer32
_AdGenY1731OneDmSessionSize_Object = MibTableColumn
adGenY1731OneDmSessionSize = _AdGenY1731OneDmSessionSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 11),
    _AdGenY1731OneDmSessionSize_Type()
)
adGenY1731OneDmSessionSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionSize.setStatus("current")


class _AdGenY1731OneDmSessionData_Type(OctetString):
    """Custom type adGenY1731OneDmSessionData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AdGenY1731OneDmSessionData_Type.__name__ = "OctetString"
_AdGenY1731OneDmSessionData_Object = MibTableColumn
adGenY1731OneDmSessionData = _AdGenY1731OneDmSessionData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 2, 1, 12),
    _AdGenY1731OneDmSessionData_Type()
)
adGenY1731OneDmSessionData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionData.setStatus("current")
_AdGenY1731OneDmSessionReceiveTable_Object = MibTable
adGenY1731OneDmSessionReceiveTable = _AdGenY1731OneDmSessionReceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 3)
)
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionReceiveTable.setStatus("current")
_AdGenY1731OneDmSessionReceiveEntry_Object = MibTableRow
adGenY1731OneDmSessionReceiveEntry = _AdGenY1731OneDmSessionReceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 3, 1)
)
adGenY1731OneDmSessionReceiveEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionReceiveEntry.setStatus("current")


class _AdGenY1731OneDmSessionMeasurementInterval_Type(Integer32):
    """Custom type adGenY1731OneDmSessionMeasurementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_AdGenY1731OneDmSessionMeasurementInterval_Type.__name__ = "Integer32"
_AdGenY1731OneDmSessionMeasurementInterval_Object = MibTableColumn
adGenY1731OneDmSessionMeasurementInterval = _AdGenY1731OneDmSessionMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 3, 1, 1),
    _AdGenY1731OneDmSessionMeasurementInterval_Type()
)
adGenY1731OneDmSessionMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionMeasurementInterval.setStatus("current")


class _AdGenY1731OneDmSessionBulkDataExportFileTypes_Type(Integer32):
    """Custom type adGenY1731OneDmSessionBulkDataExportFileTypes based on Integer32"""
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
        *(("none", 1),
          ("average", 2),
          ("raw", 3),
          ("averageAndRaw", 4))
    )


_AdGenY1731OneDmSessionBulkDataExportFileTypes_Type.__name__ = "Integer32"
_AdGenY1731OneDmSessionBulkDataExportFileTypes_Object = MibTableColumn
adGenY1731OneDmSessionBulkDataExportFileTypes = _AdGenY1731OneDmSessionBulkDataExportFileTypes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 7, 3, 1, 2),
    _AdGenY1731OneDmSessionBulkDataExportFileTypes_Type()
)
adGenY1731OneDmSessionBulkDataExportFileTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731OneDmSessionBulkDataExportFileTypes.setStatus("current")
_AdGenY1731LocalMepSlm_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepSlm = _AdGenY1731LocalMepSlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8)
)
_AdGenY1731SlmScalars_ObjectIdentity = ObjectIdentity
adGenY1731SlmScalars = _AdGenY1731SlmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 1)
)
_AdGenY1731SlmSessionMaxNumber_Type = Unsigned32
_AdGenY1731SlmSessionMaxNumber_Object = MibScalar
adGenY1731SlmSessionMaxNumber = _AdGenY1731SlmSessionMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 1, 1),
    _AdGenY1731SlmSessionMaxNumber_Type()
)
adGenY1731SlmSessionMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionMaxNumber.setStatus("current")
_AdGenY1731SlmSessionCurrentNumber_Type = Unsigned32
_AdGenY1731SlmSessionCurrentNumber_Object = MibScalar
adGenY1731SlmSessionCurrentNumber = _AdGenY1731SlmSessionCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 1, 2),
    _AdGenY1731SlmSessionCurrentNumber_Type()
)
adGenY1731SlmSessionCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionCurrentNumber.setStatus("current")
_AdGenY1731SlmSessionLastCreateError_Type = DisplayString
_AdGenY1731SlmSessionLastCreateError_Object = MibScalar
adGenY1731SlmSessionLastCreateError = _AdGenY1731SlmSessionLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 1, 3),
    _AdGenY1731SlmSessionLastCreateError_Type()
)
adGenY1731SlmSessionLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionLastCreateError.setStatus("current")
_AdGenY1731SlmSessionTransmitTable_Object = MibTable
adGenY1731SlmSessionTransmitTable = _AdGenY1731SlmSessionTransmitTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    adGenY1731SlmSessionTransmitTable.setStatus("current")
_AdGenY1731SlmSessionTransmitEntry_Object = MibTableRow
adGenY1731SlmSessionTransmitEntry = _AdGenY1731SlmSessionTransmitEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1)
)
adGenY1731SlmSessionTransmitEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731SlmSessionTargetRmepIdOrMacAddress"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731SlmSessionTarget"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731SlmSessionVlanPriority"),
)
if mibBuilder.loadTexts:
    adGenY1731SlmSessionTransmitEntry.setStatus("current")


class _AdGenY1731SlmSessionTargetRmepIdOrMacAddress_Type(Integer32):
    """Custom type adGenY1731SlmSessionTargetRmepIdOrMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmepId", 1),
          ("macAddress", 2))
    )


_AdGenY1731SlmSessionTargetRmepIdOrMacAddress_Type.__name__ = "Integer32"
_AdGenY1731SlmSessionTargetRmepIdOrMacAddress_Object = MibTableColumn
adGenY1731SlmSessionTargetRmepIdOrMacAddress = _AdGenY1731SlmSessionTargetRmepIdOrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 1),
    _AdGenY1731SlmSessionTargetRmepIdOrMacAddress_Type()
)
adGenY1731SlmSessionTargetRmepIdOrMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionTargetRmepIdOrMacAddress.setStatus("current")


class _AdGenY1731SlmSessionTarget_Type(OctetString):
    """Custom type adGenY1731SlmSessionTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_AdGenY1731SlmSessionTarget_Type.__name__ = "OctetString"
_AdGenY1731SlmSessionTarget_Object = MibTableColumn
adGenY1731SlmSessionTarget = _AdGenY1731SlmSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 2),
    _AdGenY1731SlmSessionTarget_Type()
)
adGenY1731SlmSessionTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionTarget.setStatus("current")


class _AdGenY1731SlmSessionVlanPriority_Type(Integer32):
    """Custom type adGenY1731SlmSessionVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenY1731SlmSessionVlanPriority_Type.__name__ = "Integer32"
_AdGenY1731SlmSessionVlanPriority_Object = MibTableColumn
adGenY1731SlmSessionVlanPriority = _AdGenY1731SlmSessionVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 3),
    _AdGenY1731SlmSessionVlanPriority_Type()
)
adGenY1731SlmSessionVlanPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionVlanPriority.setStatus("current")


class _AdGenY1731SlmSessionTargetRemoteMepIdentifier_Type(Integer32):
    """Custom type adGenY1731SlmSessionTargetRemoteMepIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_AdGenY1731SlmSessionTargetRemoteMepIdentifier_Type.__name__ = "Integer32"
_AdGenY1731SlmSessionTargetRemoteMepIdentifier_Object = MibTableColumn
adGenY1731SlmSessionTargetRemoteMepIdentifier = _AdGenY1731SlmSessionTargetRemoteMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 4),
    _AdGenY1731SlmSessionTargetRemoteMepIdentifier_Type()
)
adGenY1731SlmSessionTargetRemoteMepIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionTargetRemoteMepIdentifier.setStatus("current")
_AdGenY1731SlmSessionTargetMacAddress_Type = MacAddress
_AdGenY1731SlmSessionTargetMacAddress_Object = MibTableColumn
adGenY1731SlmSessionTargetMacAddress = _AdGenY1731SlmSessionTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 5),
    _AdGenY1731SlmSessionTargetMacAddress_Type()
)
adGenY1731SlmSessionTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionTargetMacAddress.setStatus("current")
_AdGenY1731SlmSessionRowStatus_Type = RowStatus
_AdGenY1731SlmSessionRowStatus_Object = MibTableColumn
adGenY1731SlmSessionRowStatus = _AdGenY1731SlmSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 6),
    _AdGenY1731SlmSessionRowStatus_Type()
)
adGenY1731SlmSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionRowStatus.setStatus("current")
_AdGenY1731SlmSessionAdminState_Type = TruthValue
_AdGenY1731SlmSessionAdminState_Object = MibTableColumn
adGenY1731SlmSessionAdminState = _AdGenY1731SlmSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 7),
    _AdGenY1731SlmSessionAdminState_Type()
)
adGenY1731SlmSessionAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionAdminState.setStatus("current")


class _AdGenY1731SlmSessionStatus_Type(Integer32):
    """Custom type adGenY1731SlmSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notRunning", 2))
    )


_AdGenY1731SlmSessionStatus_Type.__name__ = "Integer32"
_AdGenY1731SlmSessionStatus_Object = MibTableColumn
adGenY1731SlmSessionStatus = _AdGenY1731SlmSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 8),
    _AdGenY1731SlmSessionStatus_Type()
)
adGenY1731SlmSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionStatus.setStatus("current")
_AdGenY1731SlmSessionStatusString_Type = DisplayString
_AdGenY1731SlmSessionStatusString_Object = MibTableColumn
adGenY1731SlmSessionStatusString = _AdGenY1731SlmSessionStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 9),
    _AdGenY1731SlmSessionStatusString_Type()
)
adGenY1731SlmSessionStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionStatusString.setStatus("current")


class _AdGenY1731SlmSessionInterframeDelay_Type(Integer32):
    """Custom type adGenY1731SlmSessionInterframeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdGenY1731SlmSessionInterframeDelay_Type.__name__ = "Integer32"
_AdGenY1731SlmSessionInterframeDelay_Object = MibTableColumn
adGenY1731SlmSessionInterframeDelay = _AdGenY1731SlmSessionInterframeDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 10),
    _AdGenY1731SlmSessionInterframeDelay_Type()
)
adGenY1731SlmSessionInterframeDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionInterframeDelay.setStatus("current")


class _AdGenY1731SlmSessionMeasurementInterval_Type(Integer32):
    """Custom type adGenY1731SlmSessionMeasurementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_AdGenY1731SlmSessionMeasurementInterval_Type.__name__ = "Integer32"
_AdGenY1731SlmSessionMeasurementInterval_Object = MibTableColumn
adGenY1731SlmSessionMeasurementInterval = _AdGenY1731SlmSessionMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 11),
    _AdGenY1731SlmSessionMeasurementInterval_Type()
)
adGenY1731SlmSessionMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionMeasurementInterval.setStatus("current")
_AdGenY1731SlmSessionSize_Type = Integer32
_AdGenY1731SlmSessionSize_Object = MibTableColumn
adGenY1731SlmSessionSize = _AdGenY1731SlmSessionSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 12),
    _AdGenY1731SlmSessionSize_Type()
)
adGenY1731SlmSessionSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionSize.setStatus("current")


class _AdGenY1731SlmSessionData_Type(OctetString):
    """Custom type adGenY1731SlmSessionData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AdGenY1731SlmSessionData_Type.__name__ = "OctetString"
_AdGenY1731SlmSessionData_Object = MibTableColumn
adGenY1731SlmSessionData = _AdGenY1731SlmSessionData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 13),
    _AdGenY1731SlmSessionData_Type()
)
adGenY1731SlmSessionData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionData.setStatus("current")


class _AdGenY1731SlmSessionBulkDataExportFileTypes_Type(Integer32):
    """Custom type adGenY1731SlmSessionBulkDataExportFileTypes based on Integer32"""
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
        *(("none", 1),
          ("average", 2),
          ("raw", 3),
          ("averageAndRaw", 4))
    )


_AdGenY1731SlmSessionBulkDataExportFileTypes_Type.__name__ = "Integer32"
_AdGenY1731SlmSessionBulkDataExportFileTypes_Object = MibTableColumn
adGenY1731SlmSessionBulkDataExportFileTypes = _AdGenY1731SlmSessionBulkDataExportFileTypes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 8, 2, 1, 14),
    _AdGenY1731SlmSessionBulkDataExportFileTypes_Type()
)
adGenY1731SlmSessionBulkDataExportFileTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenY1731SlmSessionBulkDataExportFileTypes.setStatus("current")
_AdGenY1731LocalMepClm_ObjectIdentity = ObjectIdentity
adGenY1731LocalMepClm = _AdGenY1731LocalMepClm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 9)
)
_AdGenY1731ClmReceiverTable_Object = MibTable
adGenY1731ClmReceiverTable = _AdGenY1731ClmReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 9, 1)
)
if mibBuilder.loadTexts:
    adGenY1731ClmReceiverTable.setStatus("current")
_AdGenY1731ClmReceiverEntry_Object = MibTableRow
adGenY1731ClmReceiverEntry = _AdGenY1731ClmReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 9, 1, 1)
)
adGenY1731ClmReceiverEntry.setIndexNames(
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegLevel"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameFormat"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731MegNameLengthAndName"),
    (0, "ADTRAN-GEN-Y1731-MIB", "adGenY1731LocalMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenY1731ClmReceiverEntry.setStatus("current")
_AdGenY1731ClmReceiverEnabled_Type = TruthValue
_AdGenY1731ClmReceiverEnabled_Object = MibTableColumn
adGenY1731ClmReceiverEnabled = _AdGenY1731ClmReceiverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 9, 1, 1, 1),
    _AdGenY1731ClmReceiverEnabled_Type()
)
adGenY1731ClmReceiverEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731ClmReceiverEnabled.setStatus("current")


class _AdGenY1731ClmReceiverMeasurementInterval_Type(Integer32):
    """Custom type adGenY1731ClmReceiverMeasurementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_AdGenY1731ClmReceiverMeasurementInterval_Type.__name__ = "Integer32"
_AdGenY1731ClmReceiverMeasurementInterval_Object = MibTableColumn
adGenY1731ClmReceiverMeasurementInterval = _AdGenY1731ClmReceiverMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 9, 1, 1, 2),
    _AdGenY1731ClmReceiverMeasurementInterval_Type()
)
adGenY1731ClmReceiverMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731ClmReceiverMeasurementInterval.setStatus("current")


class _AdGenY1731ClmReceiverBulkDataExportFileTypes_Type(Integer32):
    """Custom type adGenY1731ClmReceiverBulkDataExportFileTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("average", 2))
    )


_AdGenY1731ClmReceiverBulkDataExportFileTypes_Type.__name__ = "Integer32"
_AdGenY1731ClmReceiverBulkDataExportFileTypes_Object = MibTableColumn
adGenY1731ClmReceiverBulkDataExportFileTypes = _AdGenY1731ClmReceiverBulkDataExportFileTypes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 3, 9, 1, 1, 3),
    _AdGenY1731ClmReceiverBulkDataExportFileTypes_Type()
)
adGenY1731ClmReceiverBulkDataExportFileTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenY1731ClmReceiverBulkDataExportFileTypes.setStatus("current")
_AdGenY1731Events_ObjectIdentity = ObjectIdentity
adGenY1731Events = _AdGenY1731Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 4)
)
_AdGenY1731Traps_ObjectIdentity = ObjectIdentity
adGenY1731Traps = _AdGenY1731Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 4, 0)
)

# Managed Objects groups


# Notification objects

adGenY1731PMFlashFilesClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 4, 0, 1)
)
adGenY1731PMFlashFilesClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenY1731PMFlashFilesClear.setStatus(
        "current"
    )

adGenY1731PMFlashFilesSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2, 1, 4, 0, 2)
)
adGenY1731PMFlashFilesSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenY1731PMFlashFilesSet.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-Y1731-MIB",
    **{"adGenY1731MIBObjects": adGenY1731MIBObjects,
       "adGenY1731Config": adGenY1731Config,
       "adGenY1731Enable": adGenY1731Enable,
       "adGenY1731BulkDataExportInterval": adGenY1731BulkDataExportInterval,
       "adGenY1731LinktraceCacheHoldTime": adGenY1731LinktraceCacheHoldTime,
       "adGenY1731LinktraceCacheSize": adGenY1731LinktraceCacheSize,
       "adGenY1731Meg": adGenY1731Meg,
       "adGenY1731MegMaxNumber": adGenY1731MegMaxNumber,
       "adGenY1731MegCurrentNumber": adGenY1731MegCurrentNumber,
       "adGenY1731MegLastCreateError": adGenY1731MegLastCreateError,
       "adGenY1731MegTable": adGenY1731MegTable,
       "adGenY1731MegEntry": adGenY1731MegEntry,
       "adGenY1731MegLevel": adGenY1731MegLevel,
       "adGenY1731MegNameFormat": adGenY1731MegNameFormat,
       "adGenY1731MegNameLengthAndName": adGenY1731MegNameLengthAndName,
       "adGenY1731MegRowStatus": adGenY1731MegRowStatus,
       "adGenY1731MegServiceTypeValueList": adGenY1731MegServiceTypeValueList,
       "adGenY1731MegCcmInterval": adGenY1731MegCcmInterval,
       "adGenY1731MegLocalMepConfigTableLastCreateError": adGenY1731MegLocalMepConfigTableLastCreateError,
       "adGenY1731MegDisplayName": adGenY1731MegDisplayName,
       "adGenY1731MegMepList": adGenY1731MegMepList,
       "adGenY1731MegMepListScalars": adGenY1731MegMepListScalars,
       "adGenY1731MegMepListMaxNumber": adGenY1731MegMepListMaxNumber,
       "adGenY1731MegMepListCurrentNumber": adGenY1731MegMepListCurrentNumber,
       "adGenY1731MegMepListTableLastCreateError": adGenY1731MegMepListTableLastCreateError,
       "adGenY1731MegMepListTable": adGenY1731MegMepListTable,
       "adGenY1731MegMepListEntry": adGenY1731MegMepListEntry,
       "adGenY1731MegMepListIdentifier": adGenY1731MegMepListIdentifier,
       "adGenY1731MegMepListRowStatus": adGenY1731MegMepListRowStatus,
       "adGenY1731LocalMep": adGenY1731LocalMep,
       "adGenY1731LocalMepConfig": adGenY1731LocalMepConfig,
       "adGenY1731LocalMepConfigScalars": adGenY1731LocalMepConfigScalars,
       "adGenY1731LocalMepMaxNumber": adGenY1731LocalMepMaxNumber,
       "adGenY1731LocalMepCurrentNumber": adGenY1731LocalMepCurrentNumber,
       "adGenY1731LocalMepConfigTableLastCreateError": adGenY1731LocalMepConfigTableLastCreateError,
       "adGenY1731LocalMepConfigTable": adGenY1731LocalMepConfigTable,
       "adGenY1731LocalMepConfigEntry": adGenY1731LocalMepConfigEntry,
       "adGenY1731LocalMepIdentifier": adGenY1731LocalMepIdentifier,
       "adGenY1731LocalMepRowStatus": adGenY1731LocalMepRowStatus,
       "adGenY1731LocalMepStatus": adGenY1731LocalMepStatus,
       "adGenY1731LocalMepStatusString": adGenY1731LocalMepStatusString,
       "adGenY1731LocalMepIfIndex": adGenY1731LocalMepIfIndex,
       "adGenY1731LocalMepDirection": adGenY1731LocalMepDirection,
       "adGenY1731LocalMepAdminState": adGenY1731LocalMepAdminState,
       "adGenY1731LocalMepVlanPriority": adGenY1731LocalMepVlanPriority,
       "adGenY1731LocalMepCcmEnabled": adGenY1731LocalMepCcmEnabled,
       "adGenY1731LocalMepRmepDb": adGenY1731LocalMepRmepDb,
       "adGenY1731LocalMepRmepDbScalars": adGenY1731LocalMepRmepDbScalars,
       "adGenY1731LocalMepRmepDbMaxNumber": adGenY1731LocalMepRmepDbMaxNumber,
       "adGenY1731LocalMepRmepDbCurrentNumber": adGenY1731LocalMepRmepDbCurrentNumber,
       "adGenY1731LocalMepRmepDbTable": adGenY1731LocalMepRmepDbTable,
       "adGenY1731LocalMepRmepDbEntry": adGenY1731LocalMepRmepDbEntry,
       "adGenY1731RemoteMepIdentifier": adGenY1731RemoteMepIdentifier,
       "adGenY1731RemoteMepStatus": adGenY1731RemoteMepStatus,
       "adGenY1731RemoteMepFailedOkTime": adGenY1731RemoteMepFailedOkTime,
       "adGenY1731RemoteMepMacAddress": adGenY1731RemoteMepMacAddress,
       "adGenY1731RemoteMepLastCcmSequenceNumber": adGenY1731RemoteMepLastCcmSequenceNumber,
       "adGenY1731RemoteMepRdi": adGenY1731RemoteMepRdi,
       "adGenY1731RemoteMepPortStatus": adGenY1731RemoteMepPortStatus,
       "adGenY1731RemoteMepInterfaceStatus": adGenY1731RemoteMepInterfaceStatus,
       "adGenY1731RemoteMepChassisIdSubtype": adGenY1731RemoteMepChassisIdSubtype,
       "adGenY1731RemoteMepChassisId": adGenY1731RemoteMepChassisId,
       "adGenY1731RemoteMepManAddressDomain": adGenY1731RemoteMepManAddressDomain,
       "adGenY1731RemoteMepManAddress": adGenY1731RemoteMepManAddress,
       "adGenY1731LocalMepLbm": adGenY1731LocalMepLbm,
       "adGenY1731LocalMepLbmTransmitTable": adGenY1731LocalMepLbmTransmitTable,
       "adGenY1731LocalMepLbmTransmitEntry": adGenY1731LocalMepLbmTransmitEntry,
       "adGenY1731LocalMepLbmStatus": adGenY1731LocalMepLbmStatus,
       "adGenY1731LocalMepLbmConfigStatus": adGenY1731LocalMepLbmConfigStatus,
       "adGenY1731LocalMepLbmDestMacAddress": adGenY1731LocalMepLbmDestMacAddress,
       "adGenY1731LocalMepLbmDestMepId": adGenY1731LocalMepLbmDestMepId,
       "adGenY1731LocalMepLbmDestIsMepId": adGenY1731LocalMepLbmDestIsMepId,
       "adGenY1731LocalMepLbmMessageCount": adGenY1731LocalMepLbmMessageCount,
       "adGenY1731LocalMepLbmActive": adGenY1731LocalMepLbmActive,
       "adGenY1731LocalMepLbmDataTlv": adGenY1731LocalMepLbmDataTlv,
       "adGenY1731LocalMepLbmVlanPriority": adGenY1731LocalMepLbmVlanPriority,
       "adGenY1731LocalMepLbmVlanDropEnable": adGenY1731LocalMepLbmVlanDropEnable,
       "adGenY1731LocalMepLbmErrorStatus": adGenY1731LocalMepLbmErrorStatus,
       "adGenY1731LocalMepLbmTimeout": adGenY1731LocalMepLbmTimeout,
       "adGenY1731LocalMepLbmInterframeDelay": adGenY1731LocalMepLbmInterframeDelay,
       "adGenY1731LocalMepLbmNextTransId": adGenY1731LocalMepLbmNextTransId,
       "adGenY1731LocalMepLbmSize": adGenY1731LocalMepLbmSize,
       "adGenY1731LocalMepValidateData": adGenY1731LocalMepValidateData,
       "adGenY1731LocalMepLbmResultTable": adGenY1731LocalMepLbmResultTable,
       "adGenY1731LocalMepLbmResultEntry": adGenY1731LocalMepLbmResultEntry,
       "adGenY1731LocalMepLbrResultOk": adGenY1731LocalMepLbrResultOk,
       "adGenY1731LocalMepLbrResponseTimeMin": adGenY1731LocalMepLbrResponseTimeMin,
       "adGenY1731LocalMepLbrResponseTimeMax": adGenY1731LocalMepLbrResponseTimeMax,
       "adGenY1731LocalMepLbrResponseTimeAvg": adGenY1731LocalMepLbrResponseTimeAvg,
       "adGenY1731LocalMepLbrIn": adGenY1731LocalMepLbrIn,
       "adGenY1731LocalMepLbrInOutOfOrder": adGenY1731LocalMepLbrInOutOfOrder,
       "adGenY1731LocalMepLbrBadMsdu": adGenY1731LocalMepLbrBadMsdu,
       "adGenY1731LocalMepLbmOut": adGenY1731LocalMepLbmOut,
       "adGenY1731LocalMepLbmResponderTable": adGenY1731LocalMepLbmResponderTable,
       "adGenY1731LocalMepLbmResponderEntry": adGenY1731LocalMepLbmResponderEntry,
       "adgenY1731LocalMepLbrOut": adgenY1731LocalMepLbrOut,
       "adGenY1731LocalMepLbmIn": adGenY1731LocalMepLbmIn,
       "adGenY1731LocalMepDmm": adGenY1731LocalMepDmm,
       "adGenY1731DmmScalars": adGenY1731DmmScalars,
       "adGenY1731DmmSessionMaxNumber": adGenY1731DmmSessionMaxNumber,
       "adGenY1731DmmSessionCurrentNumber": adGenY1731DmmSessionCurrentNumber,
       "adGenY1731DmmSessionLastCreateError": adGenY1731DmmSessionLastCreateError,
       "adGenY1731DmmSessionTransmitTable": adGenY1731DmmSessionTransmitTable,
       "adGenY1731DmmSessionTransmitEntry": adGenY1731DmmSessionTransmitEntry,
       "adGenY1731DmmSessionTargetRmepIdOrMacAddress": adGenY1731DmmSessionTargetRmepIdOrMacAddress,
       "adGenY1731DmmSessionTarget": adGenY1731DmmSessionTarget,
       "adGenY1731DmmSessionVlanPriority": adGenY1731DmmSessionVlanPriority,
       "adGenY1731DmmSessionTargetRemoteMepIdentifier": adGenY1731DmmSessionTargetRemoteMepIdentifier,
       "adGenY1731DmmSessionTargetMacAddress": adGenY1731DmmSessionTargetMacAddress,
       "adGenY1731DmmSessionRowStatus": adGenY1731DmmSessionRowStatus,
       "adGenY1731DmmSessionAdminState": adGenY1731DmmSessionAdminState,
       "adGenY1731DmmSessionStatus": adGenY1731DmmSessionStatus,
       "adGenY1731DmmSessionStatusString": adGenY1731DmmSessionStatusString,
       "adGenY1731DmmSessionInterframeDelay": adGenY1731DmmSessionInterframeDelay,
       "adGenY1731DmmSessionMeasurementInterval": adGenY1731DmmSessionMeasurementInterval,
       "adGenY1731DmmSessionSize": adGenY1731DmmSessionSize,
       "adGenY1731DmmSessionData": adGenY1731DmmSessionData,
       "adGenY1731DmmSessionBulkDataExportFileTypes": adGenY1731DmmSessionBulkDataExportFileTypes,
       "adGenY1731LocalMepLmm": adGenY1731LocalMepLmm,
       "adGenY1731LmmScalars": adGenY1731LmmScalars,
       "adGenY1731LmmSessionMaxNumber": adGenY1731LmmSessionMaxNumber,
       "adGenY1731LmmSessionCurrentNumber": adGenY1731LmmSessionCurrentNumber,
       "adGenY1731LmmSessionLastCreateError": adGenY1731LmmSessionLastCreateError,
       "adGenY1731LmmSessionTransmitTable": adGenY1731LmmSessionTransmitTable,
       "adGenY1731LmmSessionTransmitEntry": adGenY1731LmmSessionTransmitEntry,
       "adGenY1731LmmSessionTargetRmepIdOrMacAddress": adGenY1731LmmSessionTargetRmepIdOrMacAddress,
       "adGenY1731LmmSessionTarget": adGenY1731LmmSessionTarget,
       "adGenY1731LmmSessionVlanPriority": adGenY1731LmmSessionVlanPriority,
       "adGenY1731LmmSessionTargetRemoteMepIdentifier": adGenY1731LmmSessionTargetRemoteMepIdentifier,
       "adGenY1731LmmSessionTargetMacAddress": adGenY1731LmmSessionTargetMacAddress,
       "adGenY1731LmmSessionRowStatus": adGenY1731LmmSessionRowStatus,
       "adGenY1731LmmSessionAdminState": adGenY1731LmmSessionAdminState,
       "adGenY1731LmmSessionStatus": adGenY1731LmmSessionStatus,
       "adGenY1731LmmSessionStatusString": adGenY1731LmmSessionStatusString,
       "adGenY1731LmmSessionInterframeDelay": adGenY1731LmmSessionInterframeDelay,
       "adGenY1731LmmSessionMeasurementInterval": adGenY1731LmmSessionMeasurementInterval,
       "adGenY1731LmmSessionSize": adGenY1731LmmSessionSize,
       "adGenY1731LmmSessionData": adGenY1731LmmSessionData,
       "adGenY1731LmmSessionBulkDataExportFileTypes": adGenY1731LmmSessionBulkDataExportFileTypes,
       "adGenY1731LocalMepLtm": adGenY1731LocalMepLtm,
       "adGenY1731LocalMepLtmTable": adGenY1731LocalMepLtmTable,
       "adGenY1731LocalMepLtmEntry": adGenY1731LocalMepLtmEntry,
       "adGenY1731LocalMepLtmNextTransactionId": adGenY1731LocalMepLtmNextTransactionId,
       "adGenY1731LocalMepUnexpLtrIn": adGenY1731LocalMepUnexpLtrIn,
       "adGenY1731LocalMepTransmitLtmStatus": adGenY1731LocalMepTransmitLtmStatus,
       "adGenY1731LocalMepTransmitLtmFlags": adGenY1731LocalMepTransmitLtmFlags,
       "adGenY1731LocalMepTransmitLtmTargetMacAddress": adGenY1731LocalMepTransmitLtmTargetMacAddress,
       "adGenY1731LocalMepTransmitLtmTargetMepId": adGenY1731LocalMepTransmitLtmTargetMepId,
       "adGenY1731LocalMepTransmitLtmTargetIsMepId": adGenY1731LocalMepTransmitLtmTargetIsMepId,
       "adGenY1731LocalMepTransmitLtmTtl": adGenY1731LocalMepTransmitLtmTtl,
       "adGenY1731LocalMepTransmitLtmResult": adGenY1731LocalMepTransmitLtmResult,
       "adGenY1731LocalMepTransmitLtmTransactionId": adGenY1731LocalMepTransmitLtmTransactionId,
       "adGenY1731LocalMepTransmitLtmEgressIdentifier": adGenY1731LocalMepTransmitLtmEgressIdentifier,
       "adGenY1731LocalMepTransmitLtmStatusString": adGenY1731LocalMepTransmitLtmStatusString,
       "adGenY1731LocalMepTransmitLtmConfigStatus": adGenY1731LocalMepTransmitLtmConfigStatus,
       "adGenY1731LocalMepLtmActive": adGenY1731LocalMepLtmActive,
       "adGenY1731LocalMepLtmTotalOut": adGenY1731LocalMepLtmTotalOut,
       "adGenY1731LocalMepLtrTotalIn": adGenY1731LocalMepLtrTotalIn,
       "adGenY1731LocalMepLtrTotalInvalidIn": adGenY1731LocalMepLtrTotalInvalidIn,
       "adGenY1731LocalMepLtrTotalValidIn": adGenY1731LocalMepLtrTotalValidIn,
       "adGenY1731LocalMepLtSessionTable": adGenY1731LocalMepLtSessionTable,
       "adGenY1731LocalMepLtSessionEntry": adGenY1731LocalMepLtSessionEntry,
       "adGenY1731LocalMepLtmTransactionId": adGenY1731LocalMepLtmTransactionId,
       "adGenY1731LocalMepLtmOut": adGenY1731LocalMepLtmOut,
       "adGenY1731LocalMepLtrIn": adGenY1731LocalMepLtrIn,
       "adGenY1731LocalMepLtrInvalidIn": adGenY1731LocalMepLtrInvalidIn,
       "adGenY1731LocalMepLtrValidIn": adGenY1731LocalMepLtrValidIn,
       "adGenY1731LocalMepLtTimeRemaining": adGenY1731LocalMepLtTimeRemaining,
       "adGenY1731LocalMepLtrTable": adGenY1731LocalMepLtrTable,
       "adGenY1731LocalMepLtrEntry": adGenY1731LocalMepLtrEntry,
       "adGenY1731LocalMepLtrTransactionId": adGenY1731LocalMepLtrTransactionId,
       "adGenY1731LocalMepLtrReceiveOrder": adGenY1731LocalMepLtrReceiveOrder,
       "adGenY1731LocalMepLtrTtl": adGenY1731LocalMepLtrTtl,
       "adGenY1731LocalMepLtrForwarded": adGenY1731LocalMepLtrForwarded,
       "adGenY1731LocalMepLtrTerminalMep": adGenY1731LocalMepLtrTerminalMep,
       "adGenY1731LocalMepLtrLastEgressIdentifier": adGenY1731LocalMepLtrLastEgressIdentifier,
       "adGenY1731LocalMepLtrNextEgressIdentifier": adGenY1731LocalMepLtrNextEgressIdentifier,
       "adGenY1731LocalMepLtrRelay": adGenY1731LocalMepLtrRelay,
       "adGenY1731LocalMepLtrChassisIdSubtype": adGenY1731LocalMepLtrChassisIdSubtype,
       "adGenY1731LocalMepLtrChassisId": adGenY1731LocalMepLtrChassisId,
       "adGenY1731LocalMepLtrManAddressDomain": adGenY1731LocalMepLtrManAddressDomain,
       "adGenY1731LocalMepLtrManAddress": adGenY1731LocalMepLtrManAddress,
       "adGenY1731LocalMepLtrIngress": adGenY1731LocalMepLtrIngress,
       "adGenY1731LocalMepLtrIngressMac": adGenY1731LocalMepLtrIngressMac,
       "adGenY1731LocalMepLtrIngressPortIdSubtype": adGenY1731LocalMepLtrIngressPortIdSubtype,
       "adGenY1731LocalMepLtrIngressPortId": adGenY1731LocalMepLtrIngressPortId,
       "adGenY1731LocalMepLtrEgress": adGenY1731LocalMepLtrEgress,
       "adGenY1731LocalMepLtrEgressMac": adGenY1731LocalMepLtrEgressMac,
       "adGenY1731LocalMepLtrEgressPortIdSubtype": adGenY1731LocalMepLtrEgressPortIdSubtype,
       "adGenY1731LocalMepLtrEgressPortId": adGenY1731LocalMepLtrEgressPortId,
       "adGenY1731LocalMepLtrOrganizationSpecificTlv": adGenY1731LocalMepLtrOrganizationSpecificTlv,
       "adGenY1731LocalMepLtmResponderTable": adGenY1731LocalMepLtmResponderTable,
       "adGenY1731LocalMepLtmResponderEntry": adGenY1731LocalMepLtmResponderEntry,
       "adGenY1731LocalMepLtmIn": adGenY1731LocalMepLtmIn,
       "adGenY1731LocalMepLtmDiscardedInvalidFormat": adGenY1731LocalMepLtmDiscardedInvalidFormat,
       "adGenY1731LocalMepLtmDiscardedTtl": adGenY1731LocalMepLtmDiscardedTtl,
       "adGenY1731LocalMepLtmDiscardedTargetMac": adGenY1731LocalMepLtmDiscardedTargetMac,
       "adGenY1731LocalMepLtrOut": adGenY1731LocalMepLtrOut,
       "adGenY1731LocalMepOneDm": adGenY1731LocalMepOneDm,
       "adGenY1731OneDmScalars": adGenY1731OneDmScalars,
       "adGenY1731OneDmSessionMaxNumber": adGenY1731OneDmSessionMaxNumber,
       "adGenY1731OneDmSessionCurrentNumber": adGenY1731OneDmSessionCurrentNumber,
       "adGenY1731OneDmSessionLastCreateError": adGenY1731OneDmSessionLastCreateError,
       "adGenY1731OneDmSessionTransmitTable": adGenY1731OneDmSessionTransmitTable,
       "adGenY1731OneDmSessionTransmitEntry": adGenY1731OneDmSessionTransmitEntry,
       "adGenY1731OneDmSessionTargetRmepIdOrMacAddress": adGenY1731OneDmSessionTargetRmepIdOrMacAddress,
       "adGenY1731OneDmSessionTarget": adGenY1731OneDmSessionTarget,
       "adGenY1731OneDmSessionVlanPriority": adGenY1731OneDmSessionVlanPriority,
       "adGenY1731OneDmSessionTargetRemoteMepIdentifier": adGenY1731OneDmSessionTargetRemoteMepIdentifier,
       "adGenY1731OneDmSessionTargetMacAddress": adGenY1731OneDmSessionTargetMacAddress,
       "adGenY1731OneDmSessionRowStatus": adGenY1731OneDmSessionRowStatus,
       "adGenY1731OneDmSessionAdminState": adGenY1731OneDmSessionAdminState,
       "adGenY1731OneDmSessionStatus": adGenY1731OneDmSessionStatus,
       "adGenY1731OneDmSessionStatusString": adGenY1731OneDmSessionStatusString,
       "adGenY1731OneDmSessionInterframeDelay": adGenY1731OneDmSessionInterframeDelay,
       "adGenY1731OneDmSessionSize": adGenY1731OneDmSessionSize,
       "adGenY1731OneDmSessionData": adGenY1731OneDmSessionData,
       "adGenY1731OneDmSessionReceiveTable": adGenY1731OneDmSessionReceiveTable,
       "adGenY1731OneDmSessionReceiveEntry": adGenY1731OneDmSessionReceiveEntry,
       "adGenY1731OneDmSessionMeasurementInterval": adGenY1731OneDmSessionMeasurementInterval,
       "adGenY1731OneDmSessionBulkDataExportFileTypes": adGenY1731OneDmSessionBulkDataExportFileTypes,
       "adGenY1731LocalMepSlm": adGenY1731LocalMepSlm,
       "adGenY1731SlmScalars": adGenY1731SlmScalars,
       "adGenY1731SlmSessionMaxNumber": adGenY1731SlmSessionMaxNumber,
       "adGenY1731SlmSessionCurrentNumber": adGenY1731SlmSessionCurrentNumber,
       "adGenY1731SlmSessionLastCreateError": adGenY1731SlmSessionLastCreateError,
       "adGenY1731SlmSessionTransmitTable": adGenY1731SlmSessionTransmitTable,
       "adGenY1731SlmSessionTransmitEntry": adGenY1731SlmSessionTransmitEntry,
       "adGenY1731SlmSessionTargetRmepIdOrMacAddress": adGenY1731SlmSessionTargetRmepIdOrMacAddress,
       "adGenY1731SlmSessionTarget": adGenY1731SlmSessionTarget,
       "adGenY1731SlmSessionVlanPriority": adGenY1731SlmSessionVlanPriority,
       "adGenY1731SlmSessionTargetRemoteMepIdentifier": adGenY1731SlmSessionTargetRemoteMepIdentifier,
       "adGenY1731SlmSessionTargetMacAddress": adGenY1731SlmSessionTargetMacAddress,
       "adGenY1731SlmSessionRowStatus": adGenY1731SlmSessionRowStatus,
       "adGenY1731SlmSessionAdminState": adGenY1731SlmSessionAdminState,
       "adGenY1731SlmSessionStatus": adGenY1731SlmSessionStatus,
       "adGenY1731SlmSessionStatusString": adGenY1731SlmSessionStatusString,
       "adGenY1731SlmSessionInterframeDelay": adGenY1731SlmSessionInterframeDelay,
       "adGenY1731SlmSessionMeasurementInterval": adGenY1731SlmSessionMeasurementInterval,
       "adGenY1731SlmSessionSize": adGenY1731SlmSessionSize,
       "adGenY1731SlmSessionData": adGenY1731SlmSessionData,
       "adGenY1731SlmSessionBulkDataExportFileTypes": adGenY1731SlmSessionBulkDataExportFileTypes,
       "adGenY1731LocalMepClm": adGenY1731LocalMepClm,
       "adGenY1731ClmReceiverTable": adGenY1731ClmReceiverTable,
       "adGenY1731ClmReceiverEntry": adGenY1731ClmReceiverEntry,
       "adGenY1731ClmReceiverEnabled": adGenY1731ClmReceiverEnabled,
       "adGenY1731ClmReceiverMeasurementInterval": adGenY1731ClmReceiverMeasurementInterval,
       "adGenY1731ClmReceiverBulkDataExportFileTypes": adGenY1731ClmReceiverBulkDataExportFileTypes,
       "adGenY1731Events": adGenY1731Events,
       "adGenY1731Traps": adGenY1731Traps,
       "adGenY1731PMFlashFilesClear": adGenY1731PMFlashFilesClear,
       "adGenY1731PMFlashFilesSet": adGenY1731PMFlashFilesSet,
       "adGenY1731MIB": adGenY1731MIB}
)
