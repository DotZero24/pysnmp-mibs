# SNMP MIB module (ADTRAN-GENGPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENGPON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:46 2025
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

(adGenGponProduct,
 adGenGponProductConformance,
 adGenGponProductID) = mibBuilder.importSymbols(
    "ADTRAN-GENGPONCONTAINER-MIB",
    "adGenGponProduct",
    "adGenGponProductConformance",
    "adGenGponProductID")

(adGenPortInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortInfoIndex")

(adGenSlotAlarmStatus,
 adGenSlotInfoIndex) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotAlarmStatus",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifDescr",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

adGenGponMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1)
)
if mibBuilder.loadTexts:
    adGenGponMIB.setRevisions(
        ("2022-06-07 00:00",
         "2022-05-31 00:00",
         "2022-03-29 00:00",
         "2022-03-14 00:00",
         "2022-03-04 00:00",
         "2022-02-23 00:00",
         "2020-08-27 00:00",
         "2020-03-30 00:00",
         "2020-03-25 00:00",
         "2019-12-20 00:00",
         "2019-04-08 00:00",
         "2018-02-23 00:00",
         "2018-01-26 00:00",
         "2017-10-23 00:00",
         "2017-01-06 00:00",
         "2016-08-16 00:00",
         "2016-04-29 00:00",
         "2016-01-11 00:00",
         "2016-01-04 00:00",
         "2015-08-05 00:00",
         "2015-04-08 00:00",
         "2015-02-20 00:00",
         "2015-01-27 00:00",
         "2015-01-06 00:00",
         "2014-12-10 00:00",
         "2014-12-05 00:00",
         "2014-09-02 00:00",
         "2014-07-31 00:00",
         "2014-05-23 00:00",
         "2014-05-19 00:00",
         "2014-05-13 00:00",
         "2014-04-22 00:00",
         "2014-02-06 00:00",
         "2014-01-09 00:00",
         "2014-01-06 00:00",
         "2013-12-12 01:00",
         "2013-12-12 00:00",
         "2013-12-05 00:00",
         "2013-12-03 00:00",
         "2013-10-10 00:00",
         "2013-09-18 00:00",
         "2013-09-12 00:00",
         "2013-09-04 00:00",
         "2013-08-22 00:00",
         "2013-07-22 00:00",
         "2013-06-10 00:00",
         "2013-04-10 00:00",
         "2013-03-12 00:00",
         "2013-03-08 00:00",
         "2013-02-05 00:00",
         "2013-01-23 00:00",
         "2013-01-17 00:00",
         "2013-01-10 00:00",
         "2012-12-05 00:00",
         "2012-12-04 00:00",
         "2012-11-26 00:00",
         "2012-11-06 00:00",
         "2012-11-02 00:00",
         "2012-10-08 00:00",
         "2012-09-05 00:00",
         "2012-08-20 00:00",
         "2012-08-17 00:00",
         "2012-05-22 00:00",
         "2012-04-12 00:00",
         "2012-02-20 00:00",
         "2012-01-24 00:00",
         "2011-12-01 00:00",
         "2011-11-11 00:00",
         "2011-10-24 00:00",
         "2011-08-25 00:00",
         "2011-05-21 00:00",
         "2011-04-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenGponEnableDisableValue(TextualConvention, Integer32):
    status = "current"
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



class AdGenGponTrueFalseValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



class AdGenGponYesNoValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )



class AdGenGponOntAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfSeriveUAS", 2),
          ("outOfServiceMA", 3))
    )



class AdGenGponOntOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("discovering", 1),
          ("discovered", 2),
          ("rejected", 3),
          ("up", 4),
          ("down", 5))
    )



class AdGenGponOntPortOperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("test", 3))
    )



class AdGenGponOntPortAutoDetectMode(TextualConvention, Integer32):
    status = "deprecated"
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
              7,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("autoAuto", 0),
          ("tenFull", 1),
          ("hundredFull", 2),
          ("thousandFull", 3),
          ("autoFull", 4),
          ("tenGigabitFull", 5),
          ("twentyFiveHundredFull", 6),
          ("fiveGigabitFull", 7),
          ("tenHalf", 17),
          ("hundredHalf", 18),
          ("thousandHalf", 19))
    )



class AdGenGponActivationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("autodiscovery", 2),
          ("autoactivate", 3),
          ("registrationid", 4),
          ("registrationUnlock", 5))
    )



class AdGenGponConfigFileRetrievalMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tftp", 1),
          ("http", 2),
          ("tr69", 3))
    )



class AdGenGponConfigFileState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1),
          ("initializing", 2),
          ("fault", 3))
    )



class AdGenGponConfigFileInterface(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("voipIpHost", 0),
          ("managementIpHost", 1))
    )



class AdGenGponOntVideoPortReturnPathMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              245)
        )
    )
    namedValues = NamedValues(
        *(("scte-1", 0),
          ("scte-2-256", 1),
          ("scte-2-1544", 2),
          ("scte-2-3088", 3),
          ("rf-sample", 245))
    )



class AdGenGponResourceAllocationMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode6416", 1),
          ("mode3232", 2))
    )



class AdGenGponMulticastCacStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admitting", 1),
          ("rejecting", 2),
          ("disabled", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AdGponConfiguration_ObjectIdentity = ObjectIdentity
adGponConfiguration = _AdGponConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 1)
)
_AdGenGponOltConfigTable_Object = MibTable
adGenGponOltConfigTable = _AdGenGponOltConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenGponOltConfigTable.setStatus("current")
_AdGenGponOltConfigEntry_Object = MibTableRow
adGenGponOltConfigEntry = _AdGenGponOltConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 1, 1, 1)
)
adGenGponOltConfigEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOltConfigEntry.setStatus("current")
_AdGenGponOltSystemUpTime_Type = DisplayString
_AdGenGponOltSystemUpTime_Object = MibTableColumn
adGenGponOltSystemUpTime = _AdGenGponOltSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 1, 1, 1, 1),
    _AdGenGponOltSystemUpTime_Type()
)
adGenGponOltSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOltSystemUpTime.setStatus("current")
_AdGenGponOltOntSwVersionOnFlash_Type = DisplayString
_AdGenGponOltOntSwVersionOnFlash_Object = MibTableColumn
adGenGponOltOntSwVersionOnFlash = _AdGenGponOltOntSwVersionOnFlash_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 1, 1, 1, 2),
    _AdGenGponOltOntSwVersionOnFlash_Type()
)
adGenGponOltOntSwVersionOnFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOltOntSwVersionOnFlash.setStatus("current")
_AdGenGponOltOntBootCodeSwVersionOnFlash_Type = DisplayString
_AdGenGponOltOntBootCodeSwVersionOnFlash_Object = MibTableColumn
adGenGponOltOntBootCodeSwVersionOnFlash = _AdGenGponOltOntBootCodeSwVersionOnFlash_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 1, 1, 1, 3),
    _AdGenGponOltOntBootCodeSwVersionOnFlash_Type()
)
adGenGponOltOntBootCodeSwVersionOnFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOltOntBootCodeSwVersionOnFlash.setStatus("current")
_AdGenGponOltMaxOntsPerPon_Type = Integer32
_AdGenGponOltMaxOntsPerPon_Object = MibTableColumn
adGenGponOltMaxOntsPerPon = _AdGenGponOltMaxOntsPerPon_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 1, 1, 1, 4),
    _AdGenGponOltMaxOntsPerPon_Type()
)
adGenGponOltMaxOntsPerPon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOltMaxOntsPerPon.setStatus("current")
_AdGenGponOltNumPons_Type = Integer32
_AdGenGponOltNumPons_Object = MibTableColumn
adGenGponOltNumPons = _AdGenGponOltNumPons_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 1, 1, 1, 5),
    _AdGenGponOltNumPons_Type()
)
adGenGponOltNumPons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOltNumPons.setStatus("current")
_AdGenGponOltOntSwOnFlashGlbFilename_Type = DisplayString
_AdGenGponOltOntSwOnFlashGlbFilename_Object = MibTableColumn
adGenGponOltOntSwOnFlashGlbFilename = _AdGenGponOltOntSwOnFlashGlbFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 1, 1, 1, 6),
    _AdGenGponOltOntSwOnFlashGlbFilename_Type()
)
adGenGponOltOntSwOnFlashGlbFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOltOntSwOnFlashGlbFilename.setStatus("current")
_AdGponProvisioning_ObjectIdentity = ObjectIdentity
adGponProvisioning = _AdGponProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2)
)
_AdGenGponOltProvTable_Object = MibTable
adGenGponOltProvTable = _AdGenGponOltProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenGponOltProvTable.setStatus("current")
_AdGenGponOltProvEntry_Object = MibTableRow
adGenGponOltProvEntry = _AdGenGponOltProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1)
)
adGenGponOltProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOltProvEntry.setStatus("current")
_AdGenGponOltStagTpid_Type = Integer32
_AdGenGponOltStagTpid_Object = MibTableColumn
adGenGponOltStagTpid = _AdGenGponOltStagTpid_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 1),
    _AdGenGponOltStagTpid_Type()
)
adGenGponOltStagTpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOltStagTpid.setStatus("current")
_AdGenGponOltCtagTpid_Type = Integer32
_AdGenGponOltCtagTpid_Object = MibTableColumn
adGenGponOltCtagTpid = _AdGenGponOltCtagTpid_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 2),
    _AdGenGponOltCtagTpid_Type()
)
adGenGponOltCtagTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOltCtagTpid.setStatus("current")


class _AdGenGponOltGponClock_Type(Integer32):
    """Custom type adGenGponOltGponClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("backplane", 2))
    )


_AdGenGponOltGponClock_Type.__name__ = "Integer32"
_AdGenGponOltGponClock_Object = MibTableColumn
adGenGponOltGponClock = _AdGenGponOltGponClock_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 3),
    _AdGenGponOltGponClock_Type()
)
adGenGponOltGponClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOltGponClock.setStatus("current")
_AdGenGponOltBackplaneNegSpeed_Type = DisplayString
_AdGenGponOltBackplaneNegSpeed_Object = MibTableColumn
adGenGponOltBackplaneNegSpeed = _AdGenGponOltBackplaneNegSpeed_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 4),
    _AdGenGponOltBackplaneNegSpeed_Type()
)
adGenGponOltBackplaneNegSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOltBackplaneNegSpeed.setStatus("current")
_AdGenGponOltBipTcaThreshold_Type = Integer32
_AdGenGponOltBipTcaThreshold_Object = MibTableColumn
adGenGponOltBipTcaThreshold = _AdGenGponOltBipTcaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 5),
    _AdGenGponOltBipTcaThreshold_Type()
)
adGenGponOltBipTcaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOltBipTcaThreshold.setStatus("current")


class _AdGenGponProtection_Type(Integer32):
    """Custom type adGenGponProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdGenGponProtection_Type.__name__ = "Integer32"
_AdGenGponProtection_Object = MibTableColumn
adGenGponProtection = _AdGenGponProtection_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 6),
    _AdGenGponProtection_Type()
)
adGenGponProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponProtection.setStatus("current")


class _AdGenGponOntAlarmSlotLosEnable_Type(AdGenGponEnableDisableValue):
    """Custom type adGenGponOntAlarmSlotLosEnable based on AdGenGponEnableDisableValue"""
    defaultValue = 1


_AdGenGponOntAlarmSlotLosEnable_Type.__name__ = "AdGenGponEnableDisableValue"
_AdGenGponOntAlarmSlotLosEnable_Object = MibTableColumn
adGenGponOntAlarmSlotLosEnable = _AdGenGponOntAlarmSlotLosEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 7),
    _AdGenGponOntAlarmSlotLosEnable_Type()
)
adGenGponOntAlarmSlotLosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntAlarmSlotLosEnable.setStatus("current")


class _AdGenGponOntAlarmSlotLosLevel_Type(Integer32):
    """Custom type adGenGponOntAlarmSlotLosLevel based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenGponOntAlarmSlotLosLevel_Type.__name__ = "Integer32"
_AdGenGponOntAlarmSlotLosLevel_Object = MibTableColumn
adGenGponOntAlarmSlotLosLevel = _AdGenGponOntAlarmSlotLosLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 8),
    _AdGenGponOntAlarmSlotLosLevel_Type()
)
adGenGponOntAlarmSlotLosLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntAlarmSlotLosLevel.setStatus("current")


class _AdGenGponOntAlarmSlotPoweringEnable_Type(AdGenGponEnableDisableValue):
    """Custom type adGenGponOntAlarmSlotPoweringEnable based on AdGenGponEnableDisableValue"""
    defaultValue = 1


_AdGenGponOntAlarmSlotPoweringEnable_Type.__name__ = "AdGenGponEnableDisableValue"
_AdGenGponOntAlarmSlotPoweringEnable_Object = MibTableColumn
adGenGponOntAlarmSlotPoweringEnable = _AdGenGponOntAlarmSlotPoweringEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 9),
    _AdGenGponOntAlarmSlotPoweringEnable_Type()
)
adGenGponOntAlarmSlotPoweringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntAlarmSlotPoweringEnable.setStatus("current")


class _AdGenGponOntAlarmSlotPoweringLevel_Type(Integer32):
    """Custom type adGenGponOntAlarmSlotPoweringLevel based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenGponOntAlarmSlotPoweringLevel_Type.__name__ = "Integer32"
_AdGenGponOntAlarmSlotPoweringLevel_Object = MibTableColumn
adGenGponOntAlarmSlotPoweringLevel = _AdGenGponOntAlarmSlotPoweringLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 10),
    _AdGenGponOntAlarmSlotPoweringLevel_Type()
)
adGenGponOntAlarmSlotPoweringLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntAlarmSlotPoweringLevel.setStatus("current")


class _AdGenGponOntAlarmSlotDyingGaspEnable_Type(AdGenGponEnableDisableValue):
    """Custom type adGenGponOntAlarmSlotDyingGaspEnable based on AdGenGponEnableDisableValue"""
    defaultValue = 1


_AdGenGponOntAlarmSlotDyingGaspEnable_Type.__name__ = "AdGenGponEnableDisableValue"
_AdGenGponOntAlarmSlotDyingGaspEnable_Object = MibTableColumn
adGenGponOntAlarmSlotDyingGaspEnable = _AdGenGponOntAlarmSlotDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 11),
    _AdGenGponOntAlarmSlotDyingGaspEnable_Type()
)
adGenGponOntAlarmSlotDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntAlarmSlotDyingGaspEnable.setStatus("current")


class _AdGenGponOntAlarmSlotDyingGaspLevel_Type(Integer32):
    """Custom type adGenGponOntAlarmSlotDyingGaspLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenGponOntAlarmSlotDyingGaspLevel_Type.__name__ = "Integer32"
_AdGenGponOntAlarmSlotDyingGaspLevel_Object = MibTableColumn
adGenGponOntAlarmSlotDyingGaspLevel = _AdGenGponOntAlarmSlotDyingGaspLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 1, 1, 12),
    _AdGenGponOntAlarmSlotDyingGaspLevel_Type()
)
adGenGponOntAlarmSlotDyingGaspLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntAlarmSlotDyingGaspLevel.setStatus("current")
_AdGenGponPonProvTable_Object = MibTable
adGenGponPonProvTable = _AdGenGponPonProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    adGenGponPonProvTable.setStatus("current")
_AdGenGponPonProvEntry_Object = MibTableRow
adGenGponPonProvEntry = _AdGenGponPonProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1)
)
adGenGponPonProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponPonProvEntry.setStatus("current")
_AdGenGponPonDownstreamFec_Type = AdGenGponEnableDisableValue
_AdGenGponPonDownstreamFec_Object = MibTableColumn
adGenGponPonDownstreamFec = _AdGenGponPonDownstreamFec_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 1),
    _AdGenGponPonDownstreamFec_Type()
)
adGenGponPonDownstreamFec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonDownstreamFec.setStatus("current")
_AdGenGponPonAutoDiscoveryMode_Type = AdGenGponEnableDisableValue
_AdGenGponPonAutoDiscoveryMode_Object = MibTableColumn
adGenGponPonAutoDiscoveryMode = _AdGenGponPonAutoDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 2),
    _AdGenGponPonAutoDiscoveryMode_Type()
)
adGenGponPonAutoDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonAutoDiscoveryMode.setStatus("current")
_AdGenGponPonAutoOntActivateMode_Type = AdGenGponEnableDisableValue
_AdGenGponPonAutoOntActivateMode_Object = MibTableColumn
adGenGponPonAutoOntActivateMode = _AdGenGponPonAutoOntActivateMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 3),
    _AdGenGponPonAutoOntActivateMode_Type()
)
adGenGponPonAutoOntActivateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonAutoOntActivateMode.setStatus("current")


class _AdGenGponPonOntSoftwareDownloadFlag_Type(Integer32):
    """Custom type adGenGponPonOntSoftwareDownloadFlag based on Integer32"""
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
        *(("start", 1),
          ("cancel", 2),
          ("startAndDeferActivate", 3),
          ("activateAndCommit", 4))
    )


_AdGenGponPonOntSoftwareDownloadFlag_Type.__name__ = "Integer32"
_AdGenGponPonOntSoftwareDownloadFlag_Object = MibTableColumn
adGenGponPonOntSoftwareDownloadFlag = _AdGenGponPonOntSoftwareDownloadFlag_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 4),
    _AdGenGponPonOntSoftwareDownloadFlag_Type()
)
adGenGponPonOntSoftwareDownloadFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonOntSoftwareDownloadFlag.setStatus("current")
_AdGenGponPonRediscoverFlag_Type = AdGenGponEnableDisableValue
_AdGenGponPonRediscoverFlag_Object = MibTableColumn
adGenGponPonRediscoverFlag = _AdGenGponPonRediscoverFlag_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 5),
    _AdGenGponPonRediscoverFlag_Type()
)
adGenGponPonRediscoverFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonRediscoverFlag.setStatus("current")
_AdGenGponOntLastCreateError_Type = DisplayString
_AdGenGponOntLastCreateError_Object = MibTableColumn
adGenGponOntLastCreateError = _AdGenGponOntLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 6),
    _AdGenGponOntLastCreateError_Type()
)
adGenGponOntLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntLastCreateError.setStatus("current")


class _AdGenGponPonDeploymentRange_Type(Integer32):
    """Custom type adGenGponPonDeploymentRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("extended", 2),
          ("maximum", 3))
    )


_AdGenGponPonDeploymentRange_Type.__name__ = "Integer32"
_AdGenGponPonDeploymentRange_Object = MibTableColumn
adGenGponPonDeploymentRange = _AdGenGponPonDeploymentRange_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 7),
    _AdGenGponPonDeploymentRange_Type()
)
adGenGponPonDeploymentRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonDeploymentRange.setStatus("current")
_AdGenGponPonActivationMode_Type = AdGenGponActivationMode
_AdGenGponPonActivationMode_Object = MibTableColumn
adGenGponPonActivationMode = _AdGenGponPonActivationMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 8),
    _AdGenGponPonActivationMode_Type()
)
adGenGponPonActivationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonActivationMode.setStatus("current")
_AdGenGponPonResourceAllocationMode_Type = AdGenGponResourceAllocationMode
_AdGenGponPonResourceAllocationMode_Object = MibTableColumn
adGenGponPonResourceAllocationMode = _AdGenGponPonResourceAllocationMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 9),
    _AdGenGponPonResourceAllocationMode_Type()
)
adGenGponPonResourceAllocationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonResourceAllocationMode.setStatus("current")


class _AdGenGponPonLosActiveThreshold_Type(Integer32):
    """Custom type adGenGponPonLosActiveThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenGponPonLosActiveThreshold_Type.__name__ = "Integer32"
_AdGenGponPonLosActiveThreshold_Object = MibTableColumn
adGenGponPonLosActiveThreshold = _AdGenGponPonLosActiveThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 10),
    _AdGenGponPonLosActiveThreshold_Type()
)
adGenGponPonLosActiveThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonLosActiveThreshold.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponPonLosActiveThreshold.setUnits("percent")


class _AdGenGponPonMulticastBwThreshold_Type(Integer32):
    """Custom type adGenGponPonMulticastBwThreshold based on Integer32"""
    defaultValue = 0


_AdGenGponPonMulticastBwThreshold_Type.__name__ = "Integer32"
_AdGenGponPonMulticastBwThreshold_Object = MibTableColumn
adGenGponPonMulticastBwThreshold = _AdGenGponPonMulticastBwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 11),
    _AdGenGponPonMulticastBwThreshold_Type()
)
adGenGponPonMulticastBwThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonMulticastBwThreshold.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponPonMulticastBwThreshold.setUnits("Mbps")


class _AdGenGponPonMulticastCac_Type(AdGenGponEnableDisableValue):
    """Custom type adGenGponPonMulticastCac based on AdGenGponEnableDisableValue"""
    defaultValue = 2


_AdGenGponPonMulticastCac_Type.__name__ = "AdGenGponEnableDisableValue"
_AdGenGponPonMulticastCac_Object = MibTableColumn
adGenGponPonMulticastCac = _AdGenGponPonMulticastCac_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 12),
    _AdGenGponPonMulticastCac_Type()
)
adGenGponPonMulticastCac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonMulticastCac.setStatus("current")
_AdGenGponPonDownstreamTotalMinRate_Type = Integer32
_AdGenGponPonDownstreamTotalMinRate_Object = MibTableColumn
adGenGponPonDownstreamTotalMinRate = _AdGenGponPonDownstreamTotalMinRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 13),
    _AdGenGponPonDownstreamTotalMinRate_Type()
)
adGenGponPonDownstreamTotalMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonDownstreamTotalMinRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponPonDownstreamTotalMinRate.setUnits("kbps")


class _AdGenGponPonUpstreamFec_Type(AdGenGponEnableDisableValue):
    """Custom type adGenGponPonUpstreamFec based on AdGenGponEnableDisableValue"""
    defaultValue = 2


_AdGenGponPonUpstreamFec_Type.__name__ = "AdGenGponEnableDisableValue"
_AdGenGponPonUpstreamFec_Object = MibTableColumn
adGenGponPonUpstreamFec = _AdGenGponPonUpstreamFec_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 14),
    _AdGenGponPonUpstreamFec_Type()
)
adGenGponPonUpstreamFec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonUpstreamFec.setStatus("current")


class _AdGenGponPonDescriptionString_Type(DisplayString):
    """Custom type adGenGponPonDescriptionString based on DisplayString"""
    defaultValue = OctetString("")


_AdGenGponPonDescriptionString_Type.__name__ = "DisplayString"
_AdGenGponPonDescriptionString_Object = MibTableColumn
adGenGponPonDescriptionString = _AdGenGponPonDescriptionString_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 15),
    _AdGenGponPonDescriptionString_Type()
)
adGenGponPonDescriptionString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonDescriptionString.setStatus("current")


class _AdGenGponPonTechnologyMode_Type(Integer32):
    """Custom type adGenGponPonTechnologyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              31)
        )
    )
    namedValues = NamedValues(
        *(("gpon", 0),
          ("xgspon", 1),
          ("ngpon2", 2),
          ("technologyNotDefined", 31))
    )


_AdGenGponPonTechnologyMode_Type.__name__ = "Integer32"
_AdGenGponPonTechnologyMode_Object = MibTableColumn
adGenGponPonTechnologyMode = _AdGenGponPonTechnologyMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 2, 1, 16),
    _AdGenGponPonTechnologyMode_Type()
)
adGenGponPonTechnologyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTechnologyMode.setStatus("current")
_AdGenGponOntProvTable_Object = MibTable
adGenGponOntProvTable = _AdGenGponOntProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    adGenGponOntProvTable.setStatus("current")
_AdGenGponOntProvEntry_Object = MibTableRow
adGenGponOntProvEntry = _AdGenGponOntProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1)
)
adGenGponOntProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOntProvEntry.setStatus("current")
_AdGenGponOntSerialNumber_Type = DisplayString
_AdGenGponOntSerialNumber_Object = MibTableColumn
adGenGponOntSerialNumber = _AdGenGponOntSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 1),
    _AdGenGponOntSerialNumber_Type()
)
adGenGponOntSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntSerialNumber.setStatus("current")
_AdGenGponOntDescriptionString_Type = DisplayString
_AdGenGponOntDescriptionString_Object = MibTableColumn
adGenGponOntDescriptionString = _AdGenGponOntDescriptionString_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 2),
    _AdGenGponOntDescriptionString_Type()
)
adGenGponOntDescriptionString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntDescriptionString.setStatus("current")
_AdGenGponOntBatteryBackup_Type = AdGenGponTrueFalseValue
_AdGenGponOntBatteryBackup_Object = MibTableColumn
adGenGponOntBatteryBackup = _AdGenGponOntBatteryBackup_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 3),
    _AdGenGponOntBatteryBackup_Type()
)
adGenGponOntBatteryBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntBatteryBackup.setStatus("current")
_AdGenGponOntAdminState_Type = AdGenGponOntAdminState
_AdGenGponOntAdminState_Object = MibTableColumn
adGenGponOntAdminState = _AdGenGponOntAdminState_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 4),
    _AdGenGponOntAdminState_Type()
)
adGenGponOntAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntAdminState.setStatus("current")
_AdGenGponOntAesMode_Type = AdGenGponEnableDisableValue
_AdGenGponOntAesMode_Object = MibTableColumn
adGenGponOntAesMode = _AdGenGponOntAesMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 5),
    _AdGenGponOntAesMode_Type()
)
adGenGponOntAesMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntAesMode.setStatus("current")


class _AdGenGponOntSecurityMode_Type(Integer32):
    """Custom type adGenGponOntSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntSecurityMode_Type.__name__ = "Integer32"
_AdGenGponOntSecurityMode_Object = MibTableColumn
adGenGponOntSecurityMode = _AdGenGponOntSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 6),
    _AdGenGponOntSecurityMode_Type()
)
adGenGponOntSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntSecurityMode.setStatus("current")
_AdGenGponOntSoftwareVersion_Type = DisplayString
_AdGenGponOntSoftwareVersion_Object = MibTableColumn
adGenGponOntSoftwareVersion = _AdGenGponOntSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 7),
    _AdGenGponOntSoftwareVersion_Type()
)
adGenGponOntSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntSoftwareVersion.setStatus("current")
_AdGenGponOntGr303VoiceMacAddress_Type = PhysAddress
_AdGenGponOntGr303VoiceMacAddress_Object = MibTableColumn
adGenGponOntGr303VoiceMacAddress = _AdGenGponOntGr303VoiceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 8),
    _AdGenGponOntGr303VoiceMacAddress_Type()
)
adGenGponOntGr303VoiceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntGr303VoiceMacAddress.setStatus("current")
_AdGenGponOntUpstreamFixedBandwidth_Type = Integer32
_AdGenGponOntUpstreamFixedBandwidth_Object = MibTableColumn
adGenGponOntUpstreamFixedBandwidth = _AdGenGponOntUpstreamFixedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 9),
    _AdGenGponOntUpstreamFixedBandwidth_Type()
)
adGenGponOntUpstreamFixedBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntUpstreamFixedBandwidth.setStatus("current")
_AdGenGponOntUpstreamAssuredBandwidth_Type = Integer32
_AdGenGponOntUpstreamAssuredBandwidth_Object = MibTableColumn
adGenGponOntUpstreamAssuredBandwidth = _AdGenGponOntUpstreamAssuredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 10),
    _AdGenGponOntUpstreamAssuredBandwidth_Type()
)
adGenGponOntUpstreamAssuredBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntUpstreamAssuredBandwidth.setStatus("current")
_AdGenGponOntUpstreamBestEffortBandwidth_Type = Integer32
_AdGenGponOntUpstreamBestEffortBandwidth_Object = MibTableColumn
adGenGponOntUpstreamBestEffortBandwidth = _AdGenGponOntUpstreamBestEffortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 11),
    _AdGenGponOntUpstreamBestEffortBandwidth_Type()
)
adGenGponOntUpstreamBestEffortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntUpstreamBestEffortBandwidth.setStatus("current")
_AdGenGponOntUpstreamNonAssuredBandwidth_Type = Integer32
_AdGenGponOntUpstreamNonAssuredBandwidth_Object = MibTableColumn
adGenGponOntUpstreamNonAssuredBandwidth = _AdGenGponOntUpstreamNonAssuredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 12),
    _AdGenGponOntUpstreamNonAssuredBandwidth_Type()
)
adGenGponOntUpstreamNonAssuredBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntUpstreamNonAssuredBandwidth.setStatus("current")


class _AdGenGponOntPotsServiceMode_Type(Integer32):
    """Custom type adGenGponOntPotsServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gr303", 1),
          ("sip", 2),
          ("mgcp", 3))
    )


_AdGenGponOntPotsServiceMode_Type.__name__ = "Integer32"
_AdGenGponOntPotsServiceMode_Object = MibTableColumn
adGenGponOntPotsServiceMode = _AdGenGponOntPotsServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 13),
    _AdGenGponOntPotsServiceMode_Type()
)
adGenGponOntPotsServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPotsServiceMode.setStatus("current")
_AdGenGponOntLastError_Type = DisplayString
_AdGenGponOntLastError_Object = MibTableColumn
adGenGponOntLastError = _AdGenGponOntLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 14),
    _AdGenGponOntLastError_Type()
)
adGenGponOntLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntLastError.setStatus("current")
_AdGenGponOntRowStatus_Type = RowStatus
_AdGenGponOntRowStatus_Object = MibTableColumn
adGenGponOntRowStatus = _AdGenGponOntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 15),
    _AdGenGponOntRowStatus_Type()
)
adGenGponOntRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntRowStatus.setStatus("current")
_AdGenGponOntPortLastCreateError_Type = DisplayString
_AdGenGponOntPortLastCreateError_Object = MibTableColumn
adGenGponOntPortLastCreateError = _AdGenGponOntPortLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 16),
    _AdGenGponOntPortLastCreateError_Type()
)
adGenGponOntPortLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortLastCreateError.setStatus("current")
_AdGenGponOntRegistrationId_Type = DisplayString
_AdGenGponOntRegistrationId_Object = MibTableColumn
adGenGponOntRegistrationId = _AdGenGponOntRegistrationId_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 17),
    _AdGenGponOntRegistrationId_Type()
)
adGenGponOntRegistrationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntRegistrationId.setStatus("current")
_AdGenGponOntBootCodeSoftwareVersion_Type = DisplayString
_AdGenGponOntBootCodeSoftwareVersion_Object = MibTableColumn
adGenGponOntBootCodeSoftwareVersion = _AdGenGponOntBootCodeSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 18),
    _AdGenGponOntBootCodeSoftwareVersion_Type()
)
adGenGponOntBootCodeSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntBootCodeSoftwareVersion.setStatus("current")
_AdGenGponConfigFileRetrievalMethod_Type = AdGenGponConfigFileRetrievalMethod
_AdGenGponConfigFileRetrievalMethod_Object = MibTableColumn
adGenGponConfigFileRetrievalMethod = _AdGenGponConfigFileRetrievalMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 19),
    _AdGenGponConfigFileRetrievalMethod_Type()
)
adGenGponConfigFileRetrievalMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponConfigFileRetrievalMethod.setStatus("current")
_AdGenGponConfigFilePrimaryServer_Type = DisplayString
_AdGenGponConfigFilePrimaryServer_Object = MibTableColumn
adGenGponConfigFilePrimaryServer = _AdGenGponConfigFilePrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 20),
    _AdGenGponConfigFilePrimaryServer_Type()
)
adGenGponConfigFilePrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponConfigFilePrimaryServer.setStatus("current")
_AdGenGponConfigFileSecondaryServer_Type = DisplayString
_AdGenGponConfigFileSecondaryServer_Object = MibTableColumn
adGenGponConfigFileSecondaryServer = _AdGenGponConfigFileSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 21),
    _AdGenGponConfigFileSecondaryServer_Type()
)
adGenGponConfigFileSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponConfigFileSecondaryServer.setStatus("current")
_AdGenGponConfigFileInterface_Type = AdGenGponConfigFileInterface
_AdGenGponConfigFileInterface_Object = MibTableColumn
adGenGponConfigFileInterface = _AdGenGponConfigFileInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 22),
    _AdGenGponConfigFileInterface_Type()
)
adGenGponConfigFileInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponConfigFileInterface.setStatus("current")
_AdGenGponConfigFilePath_Type = DisplayString
_AdGenGponConfigFilePath_Object = MibTableColumn
adGenGponConfigFilePath = _AdGenGponConfigFilePath_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 23),
    _AdGenGponConfigFilePath_Type()
)
adGenGponConfigFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponConfigFilePath.setStatus("current")
_AdGenGponConfigFileRetrieve_Type = AdGenGponTrueFalseValue
_AdGenGponConfigFileRetrieve_Object = MibTableColumn
adGenGponConfigFileRetrieve = _AdGenGponConfigFileRetrieve_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 24),
    _AdGenGponConfigFileRetrieve_Type()
)
adGenGponConfigFileRetrieve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponConfigFileRetrieve.setStatus("current")
_AdGenGponMacSpoofingAllowed_Type = AdGenGponEnableDisableValue
_AdGenGponMacSpoofingAllowed_Object = MibTableColumn
adGenGponMacSpoofingAllowed = _AdGenGponMacSpoofingAllowed_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 25),
    _AdGenGponMacSpoofingAllowed_Type()
)
adGenGponMacSpoofingAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponMacSpoofingAllowed.setStatus("current")
_AdGenGponAcsServerProfile_Type = DisplayString
_AdGenGponAcsServerProfile_Object = MibTableColumn
adGenGponAcsServerProfile = _AdGenGponAcsServerProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 26),
    _AdGenGponAcsServerProfile_Type()
)
adGenGponAcsServerProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponAcsServerProfile.setStatus("current")


class _AdGenGponOntVoIPConfigMethod_Type(Integer32):
    """Custom type adGenGponOntVoIPConfigMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localONT", 0),
          ("omci", 1),
          ("fileRetrieval", 2))
    )


_AdGenGponOntVoIPConfigMethod_Type.__name__ = "Integer32"
_AdGenGponOntVoIPConfigMethod_Object = MibTableColumn
adGenGponOntVoIPConfigMethod = _AdGenGponOntVoIPConfigMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 27),
    _AdGenGponOntVoIPConfigMethod_Type()
)
adGenGponOntVoIPConfigMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVoIPConfigMethod.setStatus("current")


class _AdGenGponOntVectoringEnable_Type(Integer32):
    """Custom type adGenGponOntVectoringEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("boardLevelEnabled", 1))
    )


_AdGenGponOntVectoringEnable_Type.__name__ = "Integer32"
_AdGenGponOntVectoringEnable_Object = MibTableColumn
adGenGponOntVectoringEnable = _AdGenGponOntVectoringEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 28),
    _AdGenGponOntVectoringEnable_Type()
)
adGenGponOntVectoringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVectoringEnable.setStatus("current")
_AdGenGponOntSoftwareDownloadOnly_Type = DisplayString
_AdGenGponOntSoftwareDownloadOnly_Object = MibTableColumn
adGenGponOntSoftwareDownloadOnly = _AdGenGponOntSoftwareDownloadOnly_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 29),
    _AdGenGponOntSoftwareDownloadOnly_Type()
)
adGenGponOntSoftwareDownloadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntSoftwareDownloadOnly.setStatus("current")


class _AdGenGponOntSoftwareActivate_Type(Integer32):
    """Custom type adGenGponOntSoftwareActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activateAndCommit", 1)
    )


_AdGenGponOntSoftwareActivate_Type.__name__ = "Integer32"
_AdGenGponOntSoftwareActivate_Object = MibTableColumn
adGenGponOntSoftwareActivate = _AdGenGponOntSoftwareActivate_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 30),
    _AdGenGponOntSoftwareActivate_Type()
)
adGenGponOntSoftwareActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntSoftwareActivate.setStatus("current")


class _AdGenGponOntCpuRateLimitCountersClear_Type(Integer32):
    """Custom type adGenGponOntCpuRateLimitCountersClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-counters", 1)
    )


_AdGenGponOntCpuRateLimitCountersClear_Type.__name__ = "Integer32"
_AdGenGponOntCpuRateLimitCountersClear_Object = MibTableColumn
adGenGponOntCpuRateLimitCountersClear = _AdGenGponOntCpuRateLimitCountersClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 3, 1, 31),
    _AdGenGponOntCpuRateLimitCountersClear_Type()
)
adGenGponOntCpuRateLimitCountersClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntCpuRateLimitCountersClear.setStatus("current")
_AdGenGponOntPortProvTable_Object = MibTable
adGenGponOntPortProvTable = _AdGenGponOntPortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    adGenGponOntPortProvTable.setStatus("current")
_AdGenGponOntPortProvEntry_Object = MibTableRow
adGenGponOntPortProvEntry = _AdGenGponOntPortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1)
)
adGenGponOntPortProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOntPortProvEntry.setStatus("current")
_AdGenGponOntPortAdminState_Type = AdGenGponOntAdminState
_AdGenGponOntPortAdminState_Object = MibTableColumn
adGenGponOntPortAdminState = _AdGenGponOntPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 1),
    _AdGenGponOntPortAdminState_Type()
)
adGenGponOntPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortAdminState.setStatus("current")
_AdGenGponOntPortAutoDetectionConfiguration_Type = AdGenGponOntPortAutoDetectMode
_AdGenGponOntPortAutoDetectionConfiguration_Object = MibTableColumn
adGenGponOntPortAutoDetectionConfiguration = _AdGenGponOntPortAutoDetectionConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 2),
    _AdGenGponOntPortAutoDetectionConfiguration_Type()
)
adGenGponOntPortAutoDetectionConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortAutoDetectionConfiguration.setStatus("deprecated")


class _AdGenGponOntPortBridgeIdorIpInd_Type(Integer32):
    """Custom type adGenGponOntPortBridgeIdorIpInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridged", 0),
          ("ipRouter", 1),
          ("dependsOnParent", 2))
    )


_AdGenGponOntPortBridgeIdorIpInd_Type.__name__ = "Integer32"
_AdGenGponOntPortBridgeIdorIpInd_Object = MibTableColumn
adGenGponOntPortBridgeIdorIpInd = _AdGenGponOntPortBridgeIdorIpInd_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 3),
    _AdGenGponOntPortBridgeIdorIpInd_Type()
)
adGenGponOntPortBridgeIdorIpInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortBridgeIdorIpInd.setStatus("current")


class _AdGenGponOntPortEthLoopbackConfiguration_Type(Integer32):
    """Custom type adGenGponOntPortEthLoopbackConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("loop3", 1))
    )


_AdGenGponOntPortEthLoopbackConfiguration_Type.__name__ = "Integer32"
_AdGenGponOntPortEthLoopbackConfiguration_Object = MibTableColumn
adGenGponOntPortEthLoopbackConfiguration = _AdGenGponOntPortEthLoopbackConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 4),
    _AdGenGponOntPortEthLoopbackConfiguration_Type()
)
adGenGponOntPortEthLoopbackConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortEthLoopbackConfiguration.setStatus("current")
_AdGenGponOntPortMaxFrameSize_Type = Integer32
_AdGenGponOntPortMaxFrameSize_Object = MibTableColumn
adGenGponOntPortMaxFrameSize = _AdGenGponOntPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 5),
    _AdGenGponOntPortMaxFrameSize_Type()
)
adGenGponOntPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortMaxFrameSize.setStatus("current")


class _AdGenGponOntPortDteOrDceInd_Type(Integer32):
    """Custom type adGenGponOntPortDteOrDceInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dce", 0),
          ("dte", 1))
    )


_AdGenGponOntPortDteOrDceInd_Type.__name__ = "Integer32"
_AdGenGponOntPortDteOrDceInd_Object = MibTableColumn
adGenGponOntPortDteOrDceInd = _AdGenGponOntPortDteOrDceInd_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 6),
    _AdGenGponOntPortDteOrDceInd_Type()
)
adGenGponOntPortDteOrDceInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortDteOrDceInd.setStatus("current")
_AdGenGponOntPortPauseTime_Type = Integer32
_AdGenGponOntPortPauseTime_Object = MibTableColumn
adGenGponOntPortPauseTime = _AdGenGponOntPortPauseTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 7),
    _AdGenGponOntPortPauseTime_Type()
)
adGenGponOntPortPauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortPauseTime.setStatus("current")


class _AdGenGponOntPortPPPoEFilter_Type(Integer32):
    """Custom type adGenGponOntPortPPPoEFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowAll", 0),
          ("discardEverything", 1))
    )


_AdGenGponOntPortPPPoEFilter_Type.__name__ = "Integer32"
_AdGenGponOntPortPPPoEFilter_Object = MibTableColumn
adGenGponOntPortPPPoEFilter = _AdGenGponOntPortPPPoEFilter_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 8),
    _AdGenGponOntPortPPPoEFilter_Type()
)
adGenGponOntPortPPPoEFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortPPPoEFilter.setStatus("current")


class _AdGenGponOntPortPowerControl_Type(Integer32):
    """Custom type adGenGponOntPortPowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdGenGponOntPortPowerControl_Type.__name__ = "Integer32"
_AdGenGponOntPortPowerControl_Object = MibTableColumn
adGenGponOntPortPowerControl = _AdGenGponOntPortPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 9),
    _AdGenGponOntPortPowerControl_Type()
)
adGenGponOntPortPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortPowerControl.setStatus("current")


class _AdGenGponOntPortImpedance_Type(Integer32):
    """Custom type adGenGponOntPortImpedance based on Integer32"""
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
        *(("sixHundredOhms", 0),
          ("nineHundredOhms", 1),
          ("c1150NfR1750ohmR2270ohm", 2),
          ("c1115NfR1820ohmR2220ohm", 3),
          ("c1230NfR11050ohmR2320ohm", 4))
    )


_AdGenGponOntPortImpedance_Type.__name__ = "Integer32"
_AdGenGponOntPortImpedance_Object = MibTableColumn
adGenGponOntPortImpedance = _AdGenGponOntPortImpedance_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 10),
    _AdGenGponOntPortImpedance_Type()
)
adGenGponOntPortImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortImpedance.setStatus("current")


class _AdGenGponOntPortTransmissionPath_Type(Integer32):
    """Custom type adGenGponOntPortTransmissionPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fulltimeOnhook", 0),
          ("parttimeOnhook", 1))
    )


_AdGenGponOntPortTransmissionPath_Type.__name__ = "Integer32"
_AdGenGponOntPortTransmissionPath_Object = MibTableColumn
adGenGponOntPortTransmissionPath = _AdGenGponOntPortTransmissionPath_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 11),
    _AdGenGponOntPortTransmissionPath_Type()
)
adGenGponOntPortTransmissionPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortTransmissionPath.setStatus("current")
_AdGenGponOntPortRxGain_Type = Integer32
_AdGenGponOntPortRxGain_Object = MibTableColumn
adGenGponOntPortRxGain = _AdGenGponOntPortRxGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 12),
    _AdGenGponOntPortRxGain_Type()
)
adGenGponOntPortRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortRxGain.setStatus("current")
_AdGenGponOntPortTxGain_Type = Integer32
_AdGenGponOntPortTxGain_Object = MibTableColumn
adGenGponOntPortTxGain = _AdGenGponOntPortTxGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 13),
    _AdGenGponOntPortTxGain_Type()
)
adGenGponOntPortTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortTxGain.setStatus("current")
_AdGenGponOntPortPotsHoldoverTime_Type = Integer32
_AdGenGponOntPortPotsHoldoverTime_Object = MibTableColumn
adGenGponOntPortPotsHoldoverTime = _AdGenGponOntPortPotsHoldoverTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 14),
    _AdGenGponOntPortPotsHoldoverTime_Type()
)
adGenGponOntPortPotsHoldoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortPotsHoldoverTime.setStatus("current")
_AdGenGponOntPortPreprovIndicationFlag_Type = AdGenGponTrueFalseValue
_AdGenGponOntPortPreprovIndicationFlag_Object = MibTableColumn
adGenGponOntPortPreprovIndicationFlag = _AdGenGponOntPortPreprovIndicationFlag_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 15),
    _AdGenGponOntPortPreprovIndicationFlag_Type()
)
adGenGponOntPortPreprovIndicationFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortPreprovIndicationFlag.setStatus("current")
_AdGenGponOntPortLastError_Type = DisplayString
_AdGenGponOntPortLastError_Object = MibTableColumn
adGenGponOntPortLastError = _AdGenGponOntPortLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 16),
    _AdGenGponOntPortLastError_Type()
)
adGenGponOntPortLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortLastError.setStatus("current")
_AdGenGponOntPortRowStatus_Type = RowStatus
_AdGenGponOntPortRowStatus_Object = MibTableColumn
adGenGponOntPortRowStatus = _AdGenGponOntPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 17),
    _AdGenGponOntPortRowStatus_Type()
)
adGenGponOntPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortRowStatus.setStatus("current")


class _AdGenGponOntPortOmciEthProvPrelimCheck_Type(Integer32):
    """Custom type adGenGponOntPortOmciEthProvPrelimCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AdGenGponOntPortOmciEthProvPrelimCheck_Type.__name__ = "Integer32"
_AdGenGponOntPortOmciEthProvPrelimCheck_Object = MibTableColumn
adGenGponOntPortOmciEthProvPrelimCheck = _AdGenGponOntPortOmciEthProvPrelimCheck_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 18),
    _AdGenGponOntPortOmciEthProvPrelimCheck_Type()
)
adGenGponOntPortOmciEthProvPrelimCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortOmciEthProvPrelimCheck.setStatus("current")
_AdGenGponOntVideoPortEnableLOSAlarm_Type = AdGenGponEnableDisableValue
_AdGenGponOntVideoPortEnableLOSAlarm_Object = MibTableColumn
adGenGponOntVideoPortEnableLOSAlarm = _AdGenGponOntVideoPortEnableLOSAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 19),
    _AdGenGponOntVideoPortEnableLOSAlarm_Type()
)
adGenGponOntVideoPortEnableLOSAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVideoPortEnableLOSAlarm.setStatus("current")
_AdGenGponOntVideoPortEnableOORLowAlarm_Type = AdGenGponEnableDisableValue
_AdGenGponOntVideoPortEnableOORLowAlarm_Object = MibTableColumn
adGenGponOntVideoPortEnableOORLowAlarm = _AdGenGponOntVideoPortEnableOORLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 20),
    _AdGenGponOntVideoPortEnableOORLowAlarm_Type()
)
adGenGponOntVideoPortEnableOORLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVideoPortEnableOORLowAlarm.setStatus("current")
_AdGenGponOntVideoPortEnableOORHighAlarm_Type = AdGenGponEnableDisableValue
_AdGenGponOntVideoPortEnableOORHighAlarm_Object = MibTableColumn
adGenGponOntVideoPortEnableOORHighAlarm = _AdGenGponOntVideoPortEnableOORHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 21),
    _AdGenGponOntVideoPortEnableOORHighAlarm_Type()
)
adGenGponOntVideoPortEnableOORHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVideoPortEnableOORHighAlarm.setStatus("current")
_AdGenGponOntVideoPortReturnPathMode_Type = AdGenGponOntVideoPortReturnPathMode
_AdGenGponOntVideoPortReturnPathMode_Object = MibTableColumn
adGenGponOntVideoPortReturnPathMode = _AdGenGponOntVideoPortReturnPathMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 22),
    _AdGenGponOntVideoPortReturnPathMode_Type()
)
adGenGponOntVideoPortReturnPathMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVideoPortReturnPathMode.setStatus("current")


class _AdGenGponOntVideoPortReturnPathFrequency_Type(Integer32):
    """Custom type adGenGponOntVideoPortReturnPathFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8096, 40000),
    )


_AdGenGponOntVideoPortReturnPathFrequency_Type.__name__ = "Integer32"
_AdGenGponOntVideoPortReturnPathFrequency_Object = MibTableColumn
adGenGponOntVideoPortReturnPathFrequency = _AdGenGponOntVideoPortReturnPathFrequency_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 23),
    _AdGenGponOntVideoPortReturnPathFrequency_Type()
)
adGenGponOntVideoPortReturnPathFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVideoPortReturnPathFrequency.setStatus("current")
_AdGenGponOntVideoPortReturnPathDestinationIPAddress_Type = IpAddress
_AdGenGponOntVideoPortReturnPathDestinationIPAddress_Object = MibTableColumn
adGenGponOntVideoPortReturnPathDestinationIPAddress = _AdGenGponOntVideoPortReturnPathDestinationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 24),
    _AdGenGponOntVideoPortReturnPathDestinationIPAddress_Type()
)
adGenGponOntVideoPortReturnPathDestinationIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVideoPortReturnPathDestinationIPAddress.setStatus("current")
_AdGenGponOntVideoPortReturnPathDestinationUDPPort_Type = Integer32
_AdGenGponOntVideoPortReturnPathDestinationUDPPort_Object = MibTableColumn
adGenGponOntVideoPortReturnPathDestinationUDPPort = _AdGenGponOntVideoPortReturnPathDestinationUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 25),
    _AdGenGponOntVideoPortReturnPathDestinationUDPPort_Type()
)
adGenGponOntVideoPortReturnPathDestinationUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVideoPortReturnPathDestinationUDPPort.setStatus("current")
_AdGenGponOntVideoPortReturnPathSourceUDPPort_Type = Integer32
_AdGenGponOntVideoPortReturnPathSourceUDPPort_Object = MibTableColumn
adGenGponOntVideoPortReturnPathSourceUDPPort = _AdGenGponOntVideoPortReturnPathSourceUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 26),
    _AdGenGponOntVideoPortReturnPathSourceUDPPort_Type()
)
adGenGponOntVideoPortReturnPathSourceUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVideoPortReturnPathSourceUDPPort.setStatus("current")
_AdGenGponOntPortDescriptionString_Type = DisplayString
_AdGenGponOntPortDescriptionString_Object = MibTableColumn
adGenGponOntPortDescriptionString = _AdGenGponOntPortDescriptionString_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 27),
    _AdGenGponOntPortDescriptionString_Type()
)
adGenGponOntPortDescriptionString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortDescriptionString.setStatus("current")


class _AdGenGponOntPortMapVEIPIfIndex_Type(InterfaceIndexOrZero):
    """Custom type adGenGponOntPortMapVEIPIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_AdGenGponOntPortMapVEIPIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_AdGenGponOntPortMapVEIPIfIndex_Object = MibTableColumn
adGenGponOntPortMapVEIPIfIndex = _AdGenGponOntPortMapVEIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 28),
    _AdGenGponOntPortMapVEIPIfIndex_Type()
)
adGenGponOntPortMapVEIPIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortMapVEIPIfIndex.setStatus("current")


class _AdGenGponOntPortMapBridgeGroupIfIndex_Type(InterfaceIndexOrZero):
    """Custom type adGenGponOntPortMapBridgeGroupIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_AdGenGponOntPortMapBridgeGroupIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_AdGenGponOntPortMapBridgeGroupIfIndex_Object = MibTableColumn
adGenGponOntPortMapBridgeGroupIfIndex = _AdGenGponOntPortMapBridgeGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 29),
    _AdGenGponOntPortMapBridgeGroupIfIndex_Type()
)
adGenGponOntPortMapBridgeGroupIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortMapBridgeGroupIfIndex.setStatus("current")


class _AdGenGponOntPortBridgeGroupAgingTime_Type(Integer32):
    """Custom type adGenGponOntPortBridgeGroupAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_AdGenGponOntPortBridgeGroupAgingTime_Type.__name__ = "Integer32"
_AdGenGponOntPortBridgeGroupAgingTime_Object = MibTableColumn
adGenGponOntPortBridgeGroupAgingTime = _AdGenGponOntPortBridgeGroupAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 30),
    _AdGenGponOntPortBridgeGroupAgingTime_Type()
)
adGenGponOntPortBridgeGroupAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortBridgeGroupAgingTime.setStatus("current")


class _AdGenGponOntPortBridgeGroupLearningLimit_Type(Integer32):
    """Custom type adGenGponOntPortBridgeGroupLearningLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntPortBridgeGroupLearningLimit_Type.__name__ = "Integer32"
_AdGenGponOntPortBridgeGroupLearningLimit_Object = MibTableColumn
adGenGponOntPortBridgeGroupLearningLimit = _AdGenGponOntPortBridgeGroupLearningLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 31),
    _AdGenGponOntPortBridgeGroupLearningLimit_Type()
)
adGenGponOntPortBridgeGroupLearningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortBridgeGroupLearningLimit.setStatus("current")


class _AdGenGponOntPortBondingPeer_Type(Integer32):
    """Custom type adGenGponOntPortBondingPeer based on Integer32"""
    defaultValue = 0


_AdGenGponOntPortBondingPeer_Type.__name__ = "Integer32"
_AdGenGponOntPortBondingPeer_Object = MibTableColumn
adGenGponOntPortBondingPeer = _AdGenGponOntPortBondingPeer_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 4, 1, 32),
    _AdGenGponOntPortBondingPeer_Type()
)
adGenGponOntPortBondingPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortBondingPeer.setStatus("current")
_AdGenGponOntPortExtendedFeatureProvTable_Object = MibTable
adGenGponOntPortExtendedFeatureProvTable = _AdGenGponOntPortExtendedFeatureProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    adGenGponOntPortExtendedFeatureProvTable.setStatus("current")
_AdGenGponOntPortExtendedFeatureProvEntry_Object = MibTableRow
adGenGponOntPortExtendedFeatureProvEntry = _AdGenGponOntPortExtendedFeatureProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1)
)
adGenGponOntPortExtendedFeatureProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOntPortExtendedFeatureProvEntry.setStatus("current")


class _AdGenGponOntPortArc_Type(Integer32):
    """Custom type adGenGponOntPortArc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntPortArc_Type.__name__ = "Integer32"
_AdGenGponOntPortArc_Object = MibTableColumn
adGenGponOntPortArc = _AdGenGponOntPortArc_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 1),
    _AdGenGponOntPortArc_Type()
)
adGenGponOntPortArc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortArc.setStatus("current")


class _AdGenGponOntPortArcInterval_Type(Integer32):
    """Custom type adGenGponOntPortArcInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntPortArcInterval_Type.__name__ = "Integer32"
_AdGenGponOntPortArcInterval_Object = MibTableColumn
adGenGponOntPortArcInterval = _AdGenGponOntPortArcInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 2),
    _AdGenGponOntPortArcInterval_Type()
)
adGenGponOntPortArcInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortArcInterval.setStatus("current")


class _AdGenGponOntPortSfThreshold_Type(Integer32):
    """Custom type adGenGponOntPortSfThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntPortSfThreshold_Type.__name__ = "Integer32"
_AdGenGponOntPortSfThreshold_Object = MibTableColumn
adGenGponOntPortSfThreshold = _AdGenGponOntPortSfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 3),
    _AdGenGponOntPortSfThreshold_Type()
)
adGenGponOntPortSfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortSfThreshold.setStatus("current")


class _AdGenGponOntPortSdThreshold_Type(Integer32):
    """Custom type adGenGponOntPortSdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntPortSdThreshold_Type.__name__ = "Integer32"
_AdGenGponOntPortSdThreshold_Object = MibTableColumn
adGenGponOntPortSdThreshold = _AdGenGponOntPortSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 4),
    _AdGenGponOntPortSdThreshold_Type()
)
adGenGponOntPortSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortSdThreshold.setStatus("current")


class _AdGenGponOntPortLowerOpticalThreshold_Type(Integer32):
    """Custom type adGenGponOntPortLowerOpticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntPortLowerOpticalThreshold_Type.__name__ = "Integer32"
_AdGenGponOntPortLowerOpticalThreshold_Object = MibTableColumn
adGenGponOntPortLowerOpticalThreshold = _AdGenGponOntPortLowerOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 5),
    _AdGenGponOntPortLowerOpticalThreshold_Type()
)
adGenGponOntPortLowerOpticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortLowerOpticalThreshold.setStatus("current")


class _AdGenGponOntPortUpperOpticalThreshold_Type(Integer32):
    """Custom type adGenGponOntPortUpperOpticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntPortUpperOpticalThreshold_Type.__name__ = "Integer32"
_AdGenGponOntPortUpperOpticalThreshold_Object = MibTableColumn
adGenGponOntPortUpperOpticalThreshold = _AdGenGponOntPortUpperOpticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 6),
    _AdGenGponOntPortUpperOpticalThreshold_Type()
)
adGenGponOntPortUpperOpticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortUpperOpticalThreshold.setStatus("current")
_AdGenGponOntPortGr303signalingCodeMode_Type = Integer32
_AdGenGponOntPortGr303signalingCodeMode_Object = MibTableColumn
adGenGponOntPortGr303signalingCodeMode = _AdGenGponOntPortGr303signalingCodeMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 7),
    _AdGenGponOntPortGr303signalingCodeMode_Type()
)
adGenGponOntPortGr303signalingCodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortGr303signalingCodeMode.setStatus("current")
_AdGenGponOntPortGr303LineLoopBack_Type = Integer32
_AdGenGponOntPortGr303LineLoopBack_Object = MibTableColumn
adGenGponOntPortGr303LineLoopBack = _AdGenGponOntPortGr303LineLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 8),
    _AdGenGponOntPortGr303LineLoopBack_Type()
)
adGenGponOntPortGr303LineLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortGr303LineLoopBack.setStatus("current")
_AdGenGponOntPortGr303PayloadLoopBack_Type = Integer32
_AdGenGponOntPortGr303PayloadLoopBack_Object = MibTableColumn
adGenGponOntPortGr303PayloadLoopBack = _AdGenGponOntPortGr303PayloadLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 9),
    _AdGenGponOntPortGr303PayloadLoopBack_Type()
)
adGenGponOntPortGr303PayloadLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortGr303PayloadLoopBack.setStatus("current")
_AdGenGponOntPortGr303VoiceIpAddress_Type = IpAddress
_AdGenGponOntPortGr303VoiceIpAddress_Object = MibTableColumn
adGenGponOntPortGr303VoiceIpAddress = _AdGenGponOntPortGr303VoiceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 5, 1, 10),
    _AdGenGponOntPortGr303VoiceIpAddress_Type()
)
adGenGponOntPortGr303VoiceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntPortGr303VoiceIpAddress.setStatus("current")
_AdGenGponPonDiscoveredOntSnTable_Object = MibTable
adGenGponPonDiscoveredOntSnTable = _AdGenGponPonDiscoveredOntSnTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    adGenGponPonDiscoveredOntSnTable.setStatus("current")
_AdGenGponPonDiscoveredOntSnEntry_Object = MibTableRow
adGenGponPonDiscoveredOntSnEntry = _AdGenGponPonDiscoveredOntSnEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 6, 1)
)
adGenGponPonDiscoveredOntSnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENGPON-MIB", "adGenGponPonDiscoveredOntSerialNumberIndex"),
)
if mibBuilder.loadTexts:
    adGenGponPonDiscoveredOntSnEntry.setStatus("current")
_AdGenGponPonDiscoveredOntSerialNumberIndex_Type = Integer32
_AdGenGponPonDiscoveredOntSerialNumberIndex_Object = MibTableColumn
adGenGponPonDiscoveredOntSerialNumberIndex = _AdGenGponPonDiscoveredOntSerialNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 6, 1, 1),
    _AdGenGponPonDiscoveredOntSerialNumberIndex_Type()
)
adGenGponPonDiscoveredOntSerialNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDiscoveredOntSerialNumberIndex.setStatus("current")
_AdGenGponPonDiscoveredOntSerialNumber_Type = DisplayString
_AdGenGponPonDiscoveredOntSerialNumber_Object = MibTableColumn
adGenGponPonDiscoveredOntSerialNumber = _AdGenGponPonDiscoveredOntSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 6, 1, 2),
    _AdGenGponPonDiscoveredOntSerialNumber_Type()
)
adGenGponPonDiscoveredOntSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDiscoveredOntSerialNumber.setStatus("current")
_AdGenGponPonDiscoveredRegistrationId_Type = DisplayString
_AdGenGponPonDiscoveredRegistrationId_Object = MibTableColumn
adGenGponPonDiscoveredRegistrationId = _AdGenGponPonDiscoveredRegistrationId_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 2, 6, 1, 3),
    _AdGenGponPonDiscoveredRegistrationId_Type()
)
adGenGponPonDiscoveredRegistrationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDiscoveredRegistrationId.setStatus("current")
_AdGponStatus_ObjectIdentity = ObjectIdentity
adGponStatus = _AdGponStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3)
)
_AdGenGponOntStatusTable_Object = MibTable
adGenGponOntStatusTable = _AdGenGponOntStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adGenGponOntStatusTable.setStatus("current")
_AdGenGponOntStatusEntry_Object = MibTableRow
adGenGponOntStatusEntry = _AdGenGponOntStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1)
)
adGenGponOntStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOntStatusEntry.setStatus("current")


class _AdGenGponOntNumber_Type(Integer32):
    """Custom type adGenGponOntNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AdGenGponOntNumber_Type.__name__ = "Integer32"
_AdGenGponOntNumber_Object = MibTableColumn
adGenGponOntNumber = _AdGenGponOntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 1),
    _AdGenGponOntNumber_Type()
)
adGenGponOntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntNumber.setStatus("current")


class _AdGenGponOntTrafficManagementOption_Type(Integer32):
    """Custom type adGenGponOntTrafficManagementOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("priorityControlled", 0),
          ("rateControlled", 1))
    )


_AdGenGponOntTrafficManagementOption_Type.__name__ = "Integer32"
_AdGenGponOntTrafficManagementOption_Object = MibTableColumn
adGenGponOntTrafficManagementOption = _AdGenGponOntTrafficManagementOption_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 2),
    _AdGenGponOntTrafficManagementOption_Type()
)
adGenGponOntTrafficManagementOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntTrafficManagementOption.setStatus("current")


class _AdGenGponOntOmccVersion_Type(Integer32):
    """Custom type adGenGponOntOmccVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              129,
              130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("g984dot4June04", 128),
          ("g984dot4Amd1", 129),
          ("g984dot4Amd2", 130),
          ("g984dot4Amd3", 131),
          ("g984dot4Latest", 132))
    )


_AdGenGponOntOmccVersion_Type.__name__ = "Integer32"
_AdGenGponOntOmccVersion_Object = MibTableColumn
adGenGponOntOmccVersion = _AdGenGponOntOmccVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 3),
    _AdGenGponOntOmccVersion_Type()
)
adGenGponOntOmccVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntOmccVersion.setStatus("current")


class _AdGenGponOntMode_Type(Integer32):
    """Custom type adGenGponOntMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 0),
          ("gem", 1),
          ("dual", 2))
    )


_AdGenGponOntMode_Type.__name__ = "Integer32"
_AdGenGponOntMode_Object = MibTableColumn
adGenGponOntMode = _AdGenGponOntMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 4),
    _AdGenGponOntMode_Type()
)
adGenGponOntMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntMode.setStatus("current")
_AdGenGponOntEquipmentID_Type = DisplayString
_AdGenGponOntEquipmentID_Object = MibTableColumn
adGenGponOntEquipmentID = _AdGenGponOntEquipmentID_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 5),
    _AdGenGponOntEquipmentID_Type()
)
adGenGponOntEquipmentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntEquipmentID.setStatus("current")
_AdGenGponOntUpTime_Type = DisplayString
_AdGenGponOntUpTime_Object = MibTableColumn
adGenGponOntUpTime = _AdGenGponOntUpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 6),
    _AdGenGponOntUpTime_Type()
)
adGenGponOntUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntUpTime.setStatus("current")
_AdGenGponOntOperState_Type = AdGenGponOntOperState
_AdGenGponOntOperState_Object = MibTableColumn
adGenGponOntOperState = _AdGenGponOntOperState_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 7),
    _AdGenGponOntOperState_Type()
)
adGenGponOntOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntOperState.setStatus("current")


class _AdGenGponOntSoftwareDownloadStatus_Type(Integer32):
    """Custom type adGenGponOntSoftwareDownloadStatus based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 0),
          ("downloadInProgress", 1),
          ("downloadCompleted", 2),
          ("activationAndReboot", 3),
          ("activationCompleted", 4),
          ("commitInProgress", 5),
          ("commitCompleted", 6),
          ("downloadFailed", 7),
          ("activationFailed", 8),
          ("commitFailed", 9),
          ("sameversionSkipped", 10),
          ("downloadPending", 11),
          ("downloadCancelled", 12),
          ("downloadCompletedNotActivated", 13))
    )


_AdGenGponOntSoftwareDownloadStatus_Type.__name__ = "Integer32"
_AdGenGponOntSoftwareDownloadStatus_Object = MibTableColumn
adGenGponOntSoftwareDownloadStatus = _AdGenGponOntSoftwareDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 8),
    _AdGenGponOntSoftwareDownloadStatus_Type()
)
adGenGponOntSoftwareDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntSoftwareDownloadStatus.setStatus("current")


class _AdGenGponOntSoftwareDownloadProgress_Type(Integer32):
    """Custom type adGenGponOntSoftwareDownloadProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenGponOntSoftwareDownloadProgress_Type.__name__ = "Integer32"
_AdGenGponOntSoftwareDownloadProgress_Object = MibTableColumn
adGenGponOntSoftwareDownloadProgress = _AdGenGponOntSoftwareDownloadProgress_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 9),
    _AdGenGponOntSoftwareDownloadProgress_Type()
)
adGenGponOntSoftwareDownloadProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntSoftwareDownloadProgress.setStatus("current")
_AdGenGponOntActiveSoftwareVersion_Type = DisplayString
_AdGenGponOntActiveSoftwareVersion_Object = MibTableColumn
adGenGponOntActiveSoftwareVersion = _AdGenGponOntActiveSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 10),
    _AdGenGponOntActiveSoftwareVersion_Type()
)
adGenGponOntActiveSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntActiveSoftwareVersion.setStatus("current")
_AdGenGponOntCurrentAvailableUpstreamBandwidth_Type = Integer32
_AdGenGponOntCurrentAvailableUpstreamBandwidth_Object = MibTableColumn
adGenGponOntCurrentAvailableUpstreamBandwidth = _AdGenGponOntCurrentAvailableUpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 11),
    _AdGenGponOntCurrentAvailableUpstreamBandwidth_Type()
)
adGenGponOntCurrentAvailableUpstreamBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntCurrentAvailableUpstreamBandwidth.setStatus("current")
_AdGenGponOntPartNumber_Type = DisplayString
_AdGenGponOntPartNumber_Object = MibTableColumn
adGenGponOntPartNumber = _AdGenGponOntPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 12),
    _AdGenGponOntPartNumber_Type()
)
adGenGponOntPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPartNumber.setStatus("current")
_AdGenGponOntHardwareRevision_Type = DisplayString
_AdGenGponOntHardwareRevision_Object = MibTableColumn
adGenGponOntHardwareRevision = _AdGenGponOntHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 13),
    _AdGenGponOntHardwareRevision_Type()
)
adGenGponOntHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntHardwareRevision.setStatus("current")
_AdGenGponOntCurrentAvailableDownstreamBandwidth_Type = Integer32
_AdGenGponOntCurrentAvailableDownstreamBandwidth_Object = MibTableColumn
adGenGponOntCurrentAvailableDownstreamBandwidth = _AdGenGponOntCurrentAvailableDownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 14),
    _AdGenGponOntCurrentAvailableDownstreamBandwidth_Type()
)
adGenGponOntCurrentAvailableDownstreamBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntCurrentAvailableDownstreamBandwidth.setStatus("current")
_AdGenGponOntLearnedSerialNumber_Type = DisplayString
_AdGenGponOntLearnedSerialNumber_Object = MibTableColumn
adGenGponOntLearnedSerialNumber = _AdGenGponOntLearnedSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 15),
    _AdGenGponOntLearnedSerialNumber_Type()
)
adGenGponOntLearnedSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntLearnedSerialNumber.setStatus("current")
_AdGenGponOntRssi_Type = Integer32
_AdGenGponOntRssi_Object = MibTableColumn
adGenGponOntRssi = _AdGenGponOntRssi_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 16),
    _AdGenGponOntRssi_Type()
)
adGenGponOntRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntRssi.setStatus("current")


class _AdGenGponAvailableVOIPConfigMethods_Type(Bits):
    """Custom type adGenGponAvailableVOIPConfigMethods based on Bits"""
    namedValues = NamedValues(
        *(("omci", 0),
          ("configFileRetrieval", 1),
          ("tr69", 2),
          ("ietfSipping", 3))
    )

_AdGenGponAvailableVOIPConfigMethods_Type.__name__ = "Bits"
_AdGenGponAvailableVOIPConfigMethods_Object = MibTableColumn
adGenGponAvailableVOIPConfigMethods = _AdGenGponAvailableVOIPConfigMethods_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 17),
    _AdGenGponAvailableVOIPConfigMethods_Type()
)
adGenGponAvailableVOIPConfigMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponAvailableVOIPConfigMethods.setStatus("current")
_AdGenGponConfigFileState_Type = AdGenGponConfigFileState
_AdGenGponConfigFileState_Object = MibTableColumn
adGenGponConfigFileState = _AdGenGponConfigFileState_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 18),
    _AdGenGponConfigFileState_Type()
)
adGenGponConfigFileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponConfigFileState.setStatus("current")


class _AdGenGponConfigFileChecksum_Type(OctetString):
    """Custom type adGenGponConfigFileChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AdGenGponConfigFileChecksum_Type.__name__ = "OctetString"
_AdGenGponConfigFileChecksum_Object = MibTableColumn
adGenGponConfigFileChecksum = _AdGenGponConfigFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 19),
    _AdGenGponConfigFileChecksum_Type()
)
adGenGponConfigFileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponConfigFileChecksum.setStatus("current")
_AdGenGponConfigErrorString_Type = DisplayString
_AdGenGponConfigErrorString_Object = MibTableColumn
adGenGponConfigErrorString = _AdGenGponConfigErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 20),
    _AdGenGponConfigErrorString_Type()
)
adGenGponConfigErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponConfigErrorString.setStatus("current")
_AdGenGponOntUpstreamBIPError_Type = Counter32
_AdGenGponOntUpstreamBIPError_Object = MibTableColumn
adGenGponOntUpstreamBIPError = _AdGenGponOntUpstreamBIPError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 21),
    _AdGenGponOntUpstreamBIPError_Type()
)
adGenGponOntUpstreamBIPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntUpstreamBIPError.setStatus("current")
_AdGenGponOntDownstreamBIPError_Type = Counter32
_AdGenGponOntDownstreamBIPError_Object = MibTableColumn
adGenGponOntDownstreamBIPError = _AdGenGponOntDownstreamBIPError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 22),
    _AdGenGponOntDownstreamBIPError_Type()
)
adGenGponOntDownstreamBIPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntDownstreamBIPError.setStatus("current")
_AdGenGponOntUpstreamGoodDBRuCounter_Type = Counter32
_AdGenGponOntUpstreamGoodDBRuCounter_Object = MibTableColumn
adGenGponOntUpstreamGoodDBRuCounter = _AdGenGponOntUpstreamGoodDBRuCounter_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 23),
    _AdGenGponOntUpstreamGoodDBRuCounter_Type()
)
adGenGponOntUpstreamGoodDBRuCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntUpstreamGoodDBRuCounter.setStatus("current")
_AdGenGponOntUpstreamBadDBRuCounter_Type = Counter32
_AdGenGponOntUpstreamBadDBRuCounter_Object = MibTableColumn
adGenGponOntUpstreamBadDBRuCounter = _AdGenGponOntUpstreamBadDBRuCounter_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 24),
    _AdGenGponOntUpstreamBadDBRuCounter_Type()
)
adGenGponOntUpstreamBadDBRuCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntUpstreamBadDBRuCounter.setStatus("current")
_AdGenGponAcsServerProfileUserName_Type = DisplayString
_AdGenGponAcsServerProfileUserName_Object = MibTableColumn
adGenGponAcsServerProfileUserName = _AdGenGponAcsServerProfileUserName_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 25),
    _AdGenGponAcsServerProfileUserName_Type()
)
adGenGponAcsServerProfileUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponAcsServerProfileUserName.setStatus("current")
_AdGenGponAcsServerProfilePassword_Type = DisplayString
_AdGenGponAcsServerProfilePassword_Object = MibTableColumn
adGenGponAcsServerProfilePassword = _AdGenGponAcsServerProfilePassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 26),
    _AdGenGponAcsServerProfilePassword_Type()
)
adGenGponAcsServerProfilePassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponAcsServerProfilePassword.setStatus("current")


class _AdGenGponOntFeatureSupport_Type(Bits):
    """Custom type adGenGponOntFeatureSupport based on Bits"""
    namedValues = NamedValues(
        ("ieee8021x", 0)
    )

_AdGenGponOntFeatureSupport_Type.__name__ = "Bits"
_AdGenGponOntFeatureSupport_Object = MibTableColumn
adGenGponOntFeatureSupport = _AdGenGponOntFeatureSupport_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 27),
    _AdGenGponOntFeatureSupport_Type()
)
adGenGponOntFeatureSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntFeatureSupport.setStatus("current")
_AdGenGponOntInactiveSoftwareVersion_Type = DisplayString
_AdGenGponOntInactiveSoftwareVersion_Object = MibTableColumn
adGenGponOntInactiveSoftwareVersion = _AdGenGponOntInactiveSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 28),
    _AdGenGponOntInactiveSoftwareVersion_Type()
)
adGenGponOntInactiveSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntInactiveSoftwareVersion.setStatus("current")
_AdGenGponOntManagementMacAddress_Type = PhysAddress
_AdGenGponOntManagementMacAddress_Object = MibTableColumn
adGenGponOntManagementMacAddress = _AdGenGponOntManagementMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 29),
    _AdGenGponOntManagementMacAddress_Type()
)
adGenGponOntManagementMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntManagementMacAddress.setStatus("current")
_AdGenGponOntFiberLength_Type = Integer32
_AdGenGponOntFiberLength_Object = MibTableColumn
adGenGponOntFiberLength = _AdGenGponOntFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 30),
    _AdGenGponOntFiberLength_Type()
)
adGenGponOntFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntFiberLength.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponOntFiberLength.setUnits("meters")
_AdGenGponOntEqualizationDelay_Type = Integer32
_AdGenGponOntEqualizationDelay_Object = MibTableColumn
adGenGponOntEqualizationDelay = _AdGenGponOntEqualizationDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 31),
    _AdGenGponOntEqualizationDelay_Type()
)
adGenGponOntEqualizationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntEqualizationDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponOntEqualizationDelay.setUnits("bits")
_AdGenGponOntRxPower_Type = Integer32
_AdGenGponOntRxPower_Object = MibTableColumn
adGenGponOntRxPower = _AdGenGponOntRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 32),
    _AdGenGponOntRxPower_Type()
)
adGenGponOntRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntRxPower.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponOntRxPower.setUnits("tenth of dBm")
_AdGenGponOntTxPower_Type = Integer32
_AdGenGponOntTxPower_Object = MibTableColumn
adGenGponOntTxPower = _AdGenGponOntTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 33),
    _AdGenGponOntTxPower_Type()
)
adGenGponOntTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntTxPower.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponOntTxPower.setUnits("tenth of dBm")
_AdGenGponOntProductName_Type = DisplayString
_AdGenGponOntProductName_Object = MibTableColumn
adGenGponOntProductName = _AdGenGponOntProductName_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 34),
    _AdGenGponOntProductName_Type()
)
adGenGponOntProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntProductName.setStatus("current")
_AdGenGponOntEverActivated_Type = AdGenGponTrueFalseValue
_AdGenGponOntEverActivated_Object = MibTableColumn
adGenGponOntEverActivated = _AdGenGponOntEverActivated_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 35),
    _AdGenGponOntEverActivated_Type()
)
adGenGponOntEverActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntEverActivated.setStatus("current")


class _AdGenGponOntTemperature_Type(Integer32):
    """Custom type adGenGponOntTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-64, 63),
    )


_AdGenGponOntTemperature_Type.__name__ = "Integer32"
_AdGenGponOntTemperature_Object = MibTableColumn
adGenGponOntTemperature = _AdGenGponOntTemperature_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 36),
    _AdGenGponOntTemperature_Type()
)
adGenGponOntTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntTemperature.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponOntTemperature.setUnits("degrees Celsius")


class _AdGenGponOntBiasCurrent_Type(Integer32):
    """Custom type adGenGponOntBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_AdGenGponOntBiasCurrent_Type.__name__ = "Integer32"
_AdGenGponOntBiasCurrent_Object = MibTableColumn
adGenGponOntBiasCurrent = _AdGenGponOntBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 37),
    _AdGenGponOntBiasCurrent_Type()
)
adGenGponOntBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponOntBiasCurrent.setUnits("milliamps")


class _AdGenGponOntVoltage_Type(Integer32):
    """Custom type adGenGponOntVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_AdGenGponOntVoltage_Type.__name__ = "Integer32"
_AdGenGponOntVoltage_Object = MibTableColumn
adGenGponOntVoltage = _AdGenGponOntVoltage_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 38),
    _AdGenGponOntVoltage_Type()
)
adGenGponOntVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntVoltage.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponOntVoltage.setUnits("tenths of volt")
_AdGenGponOntUsFecProcessedCodewords_Type = Integer32
_AdGenGponOntUsFecProcessedCodewords_Object = MibTableColumn
adGenGponOntUsFecProcessedCodewords = _AdGenGponOntUsFecProcessedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 39),
    _AdGenGponOntUsFecProcessedCodewords_Type()
)
adGenGponOntUsFecProcessedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntUsFecProcessedCodewords.setStatus("current")
_AdGenGponOntUsFecCorrectedCodewords_Type = Integer32
_AdGenGponOntUsFecCorrectedCodewords_Object = MibTableColumn
adGenGponOntUsFecCorrectedCodewords = _AdGenGponOntUsFecCorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 40),
    _AdGenGponOntUsFecCorrectedCodewords_Type()
)
adGenGponOntUsFecCorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntUsFecCorrectedCodewords.setStatus("current")
_AdGenGponOntUsFecCorrectedCodebytes_Type = Integer32
_AdGenGponOntUsFecCorrectedCodebytes_Object = MibTableColumn
adGenGponOntUsFecCorrectedCodebytes = _AdGenGponOntUsFecCorrectedCodebytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 41),
    _AdGenGponOntUsFecCorrectedCodebytes_Type()
)
adGenGponOntUsFecCorrectedCodebytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntUsFecCorrectedCodebytes.setStatus("current")
_AdGenGponOntUsFecUncorrectedCodewords_Type = Integer32
_AdGenGponOntUsFecUncorrectedCodewords_Object = MibTableColumn
adGenGponOntUsFecUncorrectedCodewords = _AdGenGponOntUsFecUncorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 42),
    _AdGenGponOntUsFecUncorrectedCodewords_Type()
)
adGenGponOntUsFecUncorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntUsFecUncorrectedCodewords.setStatus("current")
_AdGenGponGalEthDiscardedFrames_Type = Integer32
_AdGenGponGalEthDiscardedFrames_Object = MibTableColumn
adGenGponGalEthDiscardedFrames = _AdGenGponGalEthDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 1, 1, 43),
    _AdGenGponGalEthDiscardedFrames_Type()
)
adGenGponGalEthDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponGalEthDiscardedFrames.setStatus("current")
_AdGenGponOntPortStatusTable_Object = MibTable
adGenGponOntPortStatusTable = _AdGenGponOntPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    adGenGponOntPortStatusTable.setStatus("current")
_AdGenGponOntPortStatusEntry_Object = MibTableRow
adGenGponOntPortStatusEntry = _AdGenGponOntPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1)
)
adGenGponOntPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOntPortStatusEntry.setStatus("current")
_AdGenGponOntPortNumber_Type = Integer32
_AdGenGponOntPortNumber_Object = MibTableColumn
adGenGponOntPortNumber = _AdGenGponOntPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 1),
    _AdGenGponOntPortNumber_Type()
)
adGenGponOntPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortNumber.setStatus("current")
_AdGenGponOntPortSrIndication_Type = AdGenGponTrueFalseValue
_AdGenGponOntPortSrIndication_Object = MibTableColumn
adGenGponOntPortSrIndication = _AdGenGponOntPortSrIndication_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 2),
    _AdGenGponOntPortSrIndication_Type()
)
adGenGponOntPortSrIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortSrIndication.setStatus("current")


class _AdGenGponOntPortPiggybackDbaReporting_Type(Integer32):
    """Custom type adGenGponOntPortPiggybackDbaReporting based on Integer32"""
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
        *(("modeZeroOnly", 0),
          ("modesZeroAndOne", 1),
          ("modesZeroAndTwo", 2),
          ("modesZeroOneAndTwo", 3),
          ("noPiggybackDBA", 4))
    )


_AdGenGponOntPortPiggybackDbaReporting_Type.__name__ = "Integer32"
_AdGenGponOntPortPiggybackDbaReporting_Object = MibTableColumn
adGenGponOntPortPiggybackDbaReporting = _AdGenGponOntPortPiggybackDbaReporting_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 3),
    _AdGenGponOntPortPiggybackDbaReporting_Type()
)
adGenGponOntPortPiggybackDbaReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortPiggybackDbaReporting.setStatus("current")


class _AdGenGponOntPortWholeOnuDbaReporting_Type(Integer32):
    """Custom type adGenGponOntPortWholeOnuDbaReporting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_AdGenGponOntPortWholeOnuDbaReporting_Type.__name__ = "Integer32"
_AdGenGponOntPortWholeOnuDbaReporting_Object = MibTableColumn
adGenGponOntPortWholeOnuDbaReporting = _AdGenGponOntPortWholeOnuDbaReporting_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 4),
    _AdGenGponOntPortWholeOnuDbaReporting_Type()
)
adGenGponOntPortWholeOnuDbaReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortWholeOnuDbaReporting.setStatus("current")
_AdGenGponOntPortOpticalSignalLevel_Type = Integer32
_AdGenGponOntPortOpticalSignalLevel_Object = MibTableColumn
adGenGponOntPortOpticalSignalLevel = _AdGenGponOntPortOpticalSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 5),
    _AdGenGponOntPortOpticalSignalLevel_Type()
)
adGenGponOntPortOpticalSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortOpticalSignalLevel.setStatus("current")


class _AdGenGponOntPortType_Type(Integer32):
    """Custom type adGenGponOntPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("pots", 2),
          ("video", 3),
          ("efmGroup", 5),
          ("ds1", 6),
          ("gpon", 7),
          ("iphost", 8),
          ("e1", 9),
          ("virtualEthernet", 10),
          ("bridgeGroup", 11),
          ("pseudowire", 12),
          ("xdsl", 13),
          ("efmPort", 14),
          ("efmLink", 15))
    )


_AdGenGponOntPortType_Type.__name__ = "Integer32"
_AdGenGponOntPortType_Object = MibTableColumn
adGenGponOntPortType = _AdGenGponOntPortType_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 6),
    _AdGenGponOntPortType_Type()
)
adGenGponOntPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortType.setStatus("current")


class _AdGenGponOntPortConfigurationInd_Type(Integer32):
    """Custom type adGenGponOntPortConfigurationInd based on Integer32"""
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
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("tenBaseTFullDuplex", 1),
          ("hundredBaseTFullDuplex", 2),
          ("gigabitEthernetFullDuplex", 3),
          ("tenGigabitEthernetFullDuplex", 4),
          ("twentyFiveHundredEthernetFullDuplex", 5),
          ("fiveGigabitEthernetFullDuplex", 6),
          ("tenBaseTHalfDuplex", 17),
          ("hundredBaseTHalfDuplex", 18),
          ("gigabitEthernetHalfDuplex", 19))
    )


_AdGenGponOntPortConfigurationInd_Type.__name__ = "Integer32"
_AdGenGponOntPortConfigurationInd_Object = MibTableColumn
adGenGponOntPortConfigurationInd = _AdGenGponOntPortConfigurationInd_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 7),
    _AdGenGponOntPortConfigurationInd_Type()
)
adGenGponOntPortConfigurationInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortConfigurationInd.setStatus("current")
_AdGenGponOntPortMaxGemPayloadSize_Type = Integer32
_AdGenGponOntPortMaxGemPayloadSize_Object = MibTableColumn
adGenGponOntPortMaxGemPayloadSize = _AdGenGponOntPortMaxGemPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 8),
    _AdGenGponOntPortMaxGemPayloadSize_Type()
)
adGenGponOntPortMaxGemPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortMaxGemPayloadSize.setStatus("current")


class _AdGenGponOntPortHookState_Type(Integer32):
    """Custom type adGenGponOntPortHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("onHook", 0),
          ("offHook", 1))
    )


_AdGenGponOntPortHookState_Type.__name__ = "Integer32"
_AdGenGponOntPortHookState_Object = MibTableColumn
adGenGponOntPortHookState = _AdGenGponOntPortHookState_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 9),
    _AdGenGponOntPortHookState_Type()
)
adGenGponOntPortHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortHookState.setStatus("current")
_AdGenGponOntPortOperState_Type = AdGenGponOntPortOperState
_AdGenGponOntPortOperState_Object = MibTableColumn
adGenGponOntPortOperState = _AdGenGponOntPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 10),
    _AdGenGponOntPortOperState_Type()
)
adGenGponOntPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortOperState.setStatus("current")
_AdGenGponOntPortGemBlockLength_Type = Integer32
_AdGenGponOntPortGemBlockLength_Object = MibTableColumn
adGenGponOntPortGemBlockLength = _AdGenGponOntPortGemBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 11),
    _AdGenGponOntPortGemBlockLength_Type()
)
adGenGponOntPortGemBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortGemBlockLength.setStatus("current")
_AdGenGponOntPortGr303CrvPortNumber_Type = Integer32
_AdGenGponOntPortGr303CrvPortNumber_Object = MibTableColumn
adGenGponOntPortGr303CrvPortNumber = _AdGenGponOntPortGr303CrvPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 12),
    _AdGenGponOntPortGr303CrvPortNumber_Type()
)
adGenGponOntPortGr303CrvPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortGr303CrvPortNumber.setStatus("current")
_AdGenGponOntPortRFSignalLevel_Type = Integer32
_AdGenGponOntPortRFSignalLevel_Object = MibTableColumn
adGenGponOntPortRFSignalLevel = _AdGenGponOntPortRFSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 13),
    _AdGenGponOntPortRFSignalLevel_Type()
)
adGenGponOntPortRFSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortRFSignalLevel.setStatus("current")
_AdGenGponOntPortRFOpticalSignalLevel_Type = Integer32
_AdGenGponOntPortRFOpticalSignalLevel_Object = MibTableColumn
adGenGponOntPortRFOpticalSignalLevel = _AdGenGponOntPortRFOpticalSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 14),
    _AdGenGponOntPortRFOpticalSignalLevel_Type()
)
adGenGponOntPortRFOpticalSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortRFOpticalSignalLevel.setStatus("current")
_AdGenGponOntPortErrorString_Type = DisplayString
_AdGenGponOntPortErrorString_Object = MibTableColumn
adGenGponOntPortErrorString = _AdGenGponOntPortErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 15),
    _AdGenGponOntPortErrorString_Type()
)
adGenGponOntPortErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortErrorString.setStatus("current")


class _AdGenGponOntPortConnectToVEIP_Type(OctetString):
    """Custom type adGenGponOntPortConnectToVEIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenGponOntPortConnectToVEIP_Type.__name__ = "OctetString"
_AdGenGponOntPortConnectToVEIP_Object = MibTableColumn
adGenGponOntPortConnectToVEIP = _AdGenGponOntPortConnectToVEIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 16),
    _AdGenGponOntPortConnectToVEIP_Type()
)
adGenGponOntPortConnectToVEIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortConnectToVEIP.setStatus("current")


class _AdGenGponOntPortConnectToBridgeGroup_Type(OctetString):
    """Custom type adGenGponOntPortConnectToBridgeGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenGponOntPortConnectToBridgeGroup_Type.__name__ = "OctetString"
_AdGenGponOntPortConnectToBridgeGroup_Object = MibTableColumn
adGenGponOntPortConnectToBridgeGroup = _AdGenGponOntPortConnectToBridgeGroup_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 2, 1, 17),
    _AdGenGponOntPortConnectToBridgeGroup_Type()
)
adGenGponOntPortConnectToBridgeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntPortConnectToBridgeGroup.setStatus("current")
_AdGenGponOntInventoryInfoTable_Object = MibTable
adGenGponOntInventoryInfoTable = _AdGenGponOntInventoryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    adGenGponOntInventoryInfoTable.setStatus("current")
_AdGenGponOntInventoryInfoEntry_Object = MibTableRow
adGenGponOntInventoryInfoEntry = _AdGenGponOntInventoryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 3, 1)
)
adGenGponOntInventoryInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOntInventoryInfoEntry.setStatus("current")


class _AdGenGponOntSupportedType_Type(Integer32):
    """Custom type adGenGponOntSupportedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("pots", 2),
          ("video", 3),
          ("efmGroup", 5),
          ("ds1", 6),
          ("gpon", 7),
          ("iphost", 8),
          ("e1", 9),
          ("virtualEthernet", 10),
          ("bridgeGroup", 11),
          ("pseudowire", 12),
          ("xdsl", 13),
          ("efmPort", 14),
          ("efmLink", 15))
    )


_AdGenGponOntSupportedType_Type.__name__ = "Integer32"
_AdGenGponOntSupportedType_Object = MibTableColumn
adGenGponOntSupportedType = _AdGenGponOntSupportedType_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 3, 1, 1),
    _AdGenGponOntSupportedType_Type()
)
adGenGponOntSupportedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntSupportedType.setStatus("current")
_AdGenGponOntMaxPortsPerType_Type = Integer32
_AdGenGponOntMaxPortsPerType_Object = MibTableColumn
adGenGponOntMaxPortsPerType = _AdGenGponOntMaxPortsPerType_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 3, 1, 2),
    _AdGenGponOntMaxPortsPerType_Type()
)
adGenGponOntMaxPortsPerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntMaxPortsPerType.setStatus("current")
_AdGenGponPonStatusTable_Object = MibTable
adGenGponPonStatusTable = _AdGenGponPonStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    adGenGponPonStatusTable.setStatus("current")
_AdGenGponPonStatusEntry_Object = MibTableRow
adGenGponPonStatusEntry = _AdGenGponPonStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1)
)
adGenGponPonStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponPonStatusEntry.setStatus("current")
_AdGenGponPonOntSoftwareDownloadInProgress_Type = AdGenGponYesNoValue
_AdGenGponPonOntSoftwareDownloadInProgress_Object = MibTableColumn
adGenGponPonOntSoftwareDownloadInProgress = _AdGenGponPonOntSoftwareDownloadInProgress_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 1),
    _AdGenGponPonOntSoftwareDownloadInProgress_Type()
)
adGenGponPonOntSoftwareDownloadInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonOntSoftwareDownloadInProgress.setStatus("current")
_AdGenGponPonConfiguredOnts_Type = Integer32
_AdGenGponPonConfiguredOnts_Object = MibTableColumn
adGenGponPonConfiguredOnts = _AdGenGponPonConfiguredOnts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 2),
    _AdGenGponPonConfiguredOnts_Type()
)
adGenGponPonConfiguredOnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonConfiguredOnts.setStatus("current")
_AdGenGponPonDiscoveringOnts_Type = Integer32
_AdGenGponPonDiscoveringOnts_Object = MibTableColumn
adGenGponPonDiscoveringOnts = _AdGenGponPonDiscoveringOnts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 3),
    _AdGenGponPonDiscoveringOnts_Type()
)
adGenGponPonDiscoveringOnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDiscoveringOnts.setStatus("current")
_AdGenGponPonUnrecognizedOnts_Type = Integer32
_AdGenGponPonUnrecognizedOnts_Object = MibTableColumn
adGenGponPonUnrecognizedOnts = _AdGenGponPonUnrecognizedOnts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 4),
    _AdGenGponPonUnrecognizedOnts_Type()
)
adGenGponPonUnrecognizedOnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonUnrecognizedOnts.setStatus("current")
_AdGenGponPonOperationallyUpOnts_Type = Integer32
_AdGenGponPonOperationallyUpOnts_Object = MibTableColumn
adGenGponPonOperationallyUpOnts = _AdGenGponPonOperationallyUpOnts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 5),
    _AdGenGponPonOperationallyUpOnts_Type()
)
adGenGponPonOperationallyUpOnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonOperationallyUpOnts.setStatus("current")
_AdGenGponPonAvailableUpstreamBandwidth_Type = Integer32
_AdGenGponPonAvailableUpstreamBandwidth_Object = MibTableColumn
adGenGponPonAvailableUpstreamBandwidth = _AdGenGponPonAvailableUpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 6),
    _AdGenGponPonAvailableUpstreamBandwidth_Type()
)
adGenGponPonAvailableUpstreamBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonAvailableUpstreamBandwidth.setStatus("current")
_AdGenGponPonAvailableDownstreamBandwidth_Type = Integer32
_AdGenGponPonAvailableDownstreamBandwidth_Object = MibTableColumn
adGenGponPonAvailableDownstreamBandwidth = _AdGenGponPonAvailableDownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 7),
    _AdGenGponPonAvailableDownstreamBandwidth_Type()
)
adGenGponPonAvailableDownstreamBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonAvailableDownstreamBandwidth.setStatus("current")
_AdGenGponPonLongestFiberDistance_Type = Integer32
_AdGenGponPonLongestFiberDistance_Object = MibTableColumn
adGenGponPonLongestFiberDistance = _AdGenGponPonLongestFiberDistance_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 8),
    _AdGenGponPonLongestFiberDistance_Type()
)
adGenGponPonLongestFiberDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonLongestFiberDistance.setStatus("current")
_AdGenGponPonShortestFiberDistance_Type = Integer32
_AdGenGponPonShortestFiberDistance_Object = MibTableColumn
adGenGponPonShortestFiberDistance = _AdGenGponPonShortestFiberDistance_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 9),
    _AdGenGponPonShortestFiberDistance_Type()
)
adGenGponPonShortestFiberDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonShortestFiberDistance.setStatus("current")
_AdGenGponPonNearestOnt_Type = Integer32
_AdGenGponPonNearestOnt_Object = MibTableColumn
adGenGponPonNearestOnt = _AdGenGponPonNearestOnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 10),
    _AdGenGponPonNearestOnt_Type()
)
adGenGponPonNearestOnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonNearestOnt.setStatus("current")
_AdGenGponPonFarthestOnt_Type = Integer32
_AdGenGponPonFarthestOnt_Object = MibTableColumn
adGenGponPonFarthestOnt = _AdGenGponPonFarthestOnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 11),
    _AdGenGponPonFarthestOnt_Type()
)
adGenGponPonFarthestOnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonFarthestOnt.setStatus("current")
_AdGenGponPonTotalProvDownstreamBandwidth_Type = Integer32
_AdGenGponPonTotalProvDownstreamBandwidth_Object = MibTableColumn
adGenGponPonTotalProvDownstreamBandwidth = _AdGenGponPonTotalProvDownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 12),
    _AdGenGponPonTotalProvDownstreamBandwidth_Type()
)
adGenGponPonTotalProvDownstreamBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTotalProvDownstreamBandwidth.setStatus("current")
_AdGenGponPonTotalProvUpstreamBandwidth_Type = Integer32
_AdGenGponPonTotalProvUpstreamBandwidth_Object = MibTableColumn
adGenGponPonTotalProvUpstreamBandwidth = _AdGenGponPonTotalProvUpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 13),
    _AdGenGponPonTotalProvUpstreamBandwidth_Type()
)
adGenGponPonTotalProvUpstreamBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTotalProvUpstreamBandwidth.setStatus("current")
_AdGenGponPonTotalProvFixedAssuredBandwidth_Type = Integer32
_AdGenGponPonTotalProvFixedAssuredBandwidth_Object = MibTableColumn
adGenGponPonTotalProvFixedAssuredBandwidth = _AdGenGponPonTotalProvFixedAssuredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 14),
    _AdGenGponPonTotalProvFixedAssuredBandwidth_Type()
)
adGenGponPonTotalProvFixedAssuredBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTotalProvFixedAssuredBandwidth.setStatus("current")
_AdGenGponPonNextAvailableOntId_Type = Integer32
_AdGenGponPonNextAvailableOntId_Object = MibTableColumn
adGenGponPonNextAvailableOntId = _AdGenGponPonNextAvailableOntId_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 15),
    _AdGenGponPonNextAvailableOntId_Type()
)
adGenGponPonNextAvailableOntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonNextAvailableOntId.setStatus("current")
_AdGenGponPonAvailableFixedAssuredBandwidth_Type = Integer32
_AdGenGponPonAvailableFixedAssuredBandwidth_Object = MibTableColumn
adGenGponPonAvailableFixedAssuredBandwidth = _AdGenGponPonAvailableFixedAssuredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 16),
    _AdGenGponPonAvailableFixedAssuredBandwidth_Type()
)
adGenGponPonAvailableFixedAssuredBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonAvailableFixedAssuredBandwidth.setStatus("current")
_AdGenGponPonCurrDownstreamBandwidth_Type = Integer32
_AdGenGponPonCurrDownstreamBandwidth_Object = MibTableColumn
adGenGponPonCurrDownstreamBandwidth = _AdGenGponPonCurrDownstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 17),
    _AdGenGponPonCurrDownstreamBandwidth_Type()
)
adGenGponPonCurrDownstreamBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonCurrDownstreamBandwidth.setStatus("current")
_AdGenGponPonCurrUpstreamBandwidth_Type = Integer32
_AdGenGponPonCurrUpstreamBandwidth_Object = MibTableColumn
adGenGponPonCurrUpstreamBandwidth = _AdGenGponPonCurrUpstreamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 18),
    _AdGenGponPonCurrUpstreamBandwidth_Type()
)
adGenGponPonCurrUpstreamBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonCurrUpstreamBandwidth.setStatus("current")
_AdGenGponPonCurrFixedAssuredBandwidth_Type = Integer32
_AdGenGponPonCurrFixedAssuredBandwidth_Object = MibTableColumn
adGenGponPonCurrFixedAssuredBandwidth = _AdGenGponPonCurrFixedAssuredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 19),
    _AdGenGponPonCurrFixedAssuredBandwidth_Type()
)
adGenGponPonCurrFixedAssuredBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonCurrFixedAssuredBandwidth.setStatus("current")
_AdGenGponPonTotalProvFixedBandwidth_Type = Integer32
_AdGenGponPonTotalProvFixedBandwidth_Object = MibTableColumn
adGenGponPonTotalProvFixedBandwidth = _AdGenGponPonTotalProvFixedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 20),
    _AdGenGponPonTotalProvFixedBandwidth_Type()
)
adGenGponPonTotalProvFixedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTotalProvFixedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponPonTotalProvFixedBandwidth.setUnits("kbps")
_AdGenGponPonTotalProvAssuredBandwidth_Type = Integer32
_AdGenGponPonTotalProvAssuredBandwidth_Object = MibTableColumn
adGenGponPonTotalProvAssuredBandwidth = _AdGenGponPonTotalProvAssuredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 21),
    _AdGenGponPonTotalProvAssuredBandwidth_Type()
)
adGenGponPonTotalProvAssuredBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTotalProvAssuredBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponPonTotalProvAssuredBandwidth.setUnits("kbps")
_AdGenGponPonMaxOnts_Type = Integer32
_AdGenGponPonMaxOnts_Object = MibTableColumn
adGenGponPonMaxOnts = _AdGenGponPonMaxOnts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 22),
    _AdGenGponPonMaxOnts_Type()
)
adGenGponPonMaxOnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonMaxOnts.setStatus("current")
_AdGenGponPonMaxServicesPerOnt_Type = Integer32
_AdGenGponPonMaxServicesPerOnt_Object = MibTableColumn
adGenGponPonMaxServicesPerOnt = _AdGenGponPonMaxServicesPerOnt_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 23),
    _AdGenGponPonMaxServicesPerOnt_Type()
)
adGenGponPonMaxServicesPerOnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonMaxServicesPerOnt.setStatus("current")
_AdGenGponPonLosNumOntsDown_Type = Integer32
_AdGenGponPonLosNumOntsDown_Object = MibTableColumn
adGenGponPonLosNumOntsDown = _AdGenGponPonLosNumOntsDown_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 24),
    _AdGenGponPonLosNumOntsDown_Type()
)
adGenGponPonLosNumOntsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonLosNumOntsDown.setStatus("current")
_AdGenGponPonMulticastCacStatus_Type = AdGenGponMulticastCacStatus
_AdGenGponPonMulticastCacStatus_Object = MibTableColumn
adGenGponPonMulticastCacStatus = _AdGenGponPonMulticastCacStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 25),
    _AdGenGponPonMulticastCacStatus_Type()
)
adGenGponPonMulticastCacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonMulticastCacStatus.setStatus("current")
_AdGenGponPonDownstreamAvailableMinRate_Type = Integer32
_AdGenGponPonDownstreamAvailableMinRate_Object = MibTableColumn
adGenGponPonDownstreamAvailableMinRate = _AdGenGponPonDownstreamAvailableMinRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 26),
    _AdGenGponPonDownstreamAvailableMinRate_Type()
)
adGenGponPonDownstreamAvailableMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDownstreamAvailableMinRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponPonDownstreamAvailableMinRate.setUnits("kbps")
_AdGenGponPonDownstreamCurrentMinRate_Type = Integer32
_AdGenGponPonDownstreamCurrentMinRate_Object = MibTableColumn
adGenGponPonDownstreamCurrentMinRate = _AdGenGponPonDownstreamCurrentMinRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 27),
    _AdGenGponPonDownstreamCurrentMinRate_Type()
)
adGenGponPonDownstreamCurrentMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDownstreamCurrentMinRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenGponPonDownstreamCurrentMinRate.setUnits("kbps")


class _AdGenGponPonTechnology_Type(Integer32):
    """Custom type adGenGponPonTechnology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("gpon", 0),
          ("xgspon", 1),
          ("ngpon2", 2),
          ("wdmpon", 3),
          ("cannnotDetectTechnology", 30),
          ("technologyReportingNotSupported", 31))
    )


_AdGenGponPonTechnology_Type.__name__ = "Integer32"
_AdGenGponPonTechnology_Object = MibTableColumn
adGenGponPonTechnology = _AdGenGponPonTechnology_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 28),
    _AdGenGponPonTechnology_Type()
)
adGenGponPonTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTechnology.setStatus("current")


class _AdGenGponPonWavelength_Type(Integer32):
    """Custom type adGenGponPonWavelength based on Integer32"""
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
              7,
              8,
              9,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("wavelength1490down1310up", 0),
          ("wavelength1577down1270up", 1),
          ("wavelength1596down1538up", 2),
          ("wavelength1597down1537up", 3),
          ("wavelength1598down1536up", 4),
          ("wavelength1598down1535up", 5),
          ("wavelength1599down1535up", 6),
          ("wavelength1600down1534up", 7),
          ("wavelength1601down1533up", 8),
          ("wavelength1602down1532up", 9),
          ("cannotDetectWavelength", 30),
          ("wavelengthReportingNotSupported", 31))
    )


_AdGenGponPonWavelength_Type.__name__ = "Integer32"
_AdGenGponPonWavelength_Object = MibTableColumn
adGenGponPonWavelength = _AdGenGponPonWavelength_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 3, 4, 1, 29),
    _AdGenGponPonWavelength_Type()
)
adGenGponPonWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonWavelength.setStatus("current")
_AdGponPerformance_ObjectIdentity = ObjectIdentity
adGponPerformance = _AdGponPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4)
)
_AdGenGponPon15MinPMTable_Object = MibTable
adGenGponPon15MinPMTable = _AdGenGponPon15MinPMTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adGenGponPon15MinPMTable.setStatus("current")
_AdGenGponPon15MinPMEntry_Object = MibTableRow
adGenGponPon15MinPMEntry = _AdGenGponPon15MinPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1)
)
adGenGponPon15MinPMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENGPON-MIB", "adGenGponPon15MinPMIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenGponPon15MinPMEntry.setStatus("current")


class _AdGenGponPon15MinPMIntervalNumber_Type(Integer32):
    """Custom type adGenGponPon15MinPMIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenGponPon15MinPMIntervalNumber_Type.__name__ = "Integer32"
_AdGenGponPon15MinPMIntervalNumber_Object = MibTableColumn
adGenGponPon15MinPMIntervalNumber = _AdGenGponPon15MinPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 1),
    _AdGenGponPon15MinPMIntervalNumber_Type()
)
adGenGponPon15MinPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenGponPon15MinPMIntervalNumber.setStatus("current")
_AdGenGponPon15MinRxEthernetPackets_Type = Gauge32
_AdGenGponPon15MinRxEthernetPackets_Object = MibTableColumn
adGenGponPon15MinRxEthernetPackets = _AdGenGponPon15MinRxEthernetPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 2),
    _AdGenGponPon15MinRxEthernetPackets_Type()
)
adGenGponPon15MinRxEthernetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinRxEthernetPackets.setStatus("current")
_AdGenGponPon15MinRxOMCIPackets_Type = Gauge32
_AdGenGponPon15MinRxOMCIPackets_Object = MibTableColumn
adGenGponPon15MinRxOMCIPackets = _AdGenGponPon15MinRxOMCIPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 3),
    _AdGenGponPon15MinRxOMCIPackets_Type()
)
adGenGponPon15MinRxOMCIPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinRxOMCIPackets.setStatus("current")
_AdGenGponPon15MinTxEthernetPackets_Type = Gauge32
_AdGenGponPon15MinTxEthernetPackets_Object = MibTableColumn
adGenGponPon15MinTxEthernetPackets = _AdGenGponPon15MinTxEthernetPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 4),
    _AdGenGponPon15MinTxEthernetPackets_Type()
)
adGenGponPon15MinTxEthernetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinTxEthernetPackets.setStatus("current")
_AdGenGponPon15MinTxOMCIPackets_Type = Gauge32
_AdGenGponPon15MinTxOMCIPackets_Object = MibTableColumn
adGenGponPon15MinTxOMCIPackets = _AdGenGponPon15MinTxOMCIPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 5),
    _AdGenGponPon15MinTxOMCIPackets_Type()
)
adGenGponPon15MinTxOMCIPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinTxOMCIPackets.setStatus("current")
_AdGenGponPon15MinUpstreamBIPError_Type = Gauge32
_AdGenGponPon15MinUpstreamBIPError_Object = MibTableColumn
adGenGponPon15MinUpstreamBIPError = _AdGenGponPon15MinUpstreamBIPError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 6),
    _AdGenGponPon15MinUpstreamBIPError_Type()
)
adGenGponPon15MinUpstreamBIPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinUpstreamBIPError.setStatus("current")
_AdGenGponPon15MinUpstreamDroppedPackets_Type = Gauge32
_AdGenGponPon15MinUpstreamDroppedPackets_Object = MibTableColumn
adGenGponPon15MinUpstreamDroppedPackets = _AdGenGponPon15MinUpstreamDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 7),
    _AdGenGponPon15MinUpstreamDroppedPackets_Type()
)
adGenGponPon15MinUpstreamDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinUpstreamDroppedPackets.setStatus("current")
_AdGenGponPon15MinBufferOverflow_Type = Gauge32
_AdGenGponPon15MinBufferOverflow_Object = MibTableColumn
adGenGponPon15MinBufferOverflow = _AdGenGponPon15MinBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 8),
    _AdGenGponPon15MinBufferOverflow_Type()
)
adGenGponPon15MinBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinBufferOverflow.setStatus("current")
_AdGenGponPon15MinPacketFragError_Type = Gauge32
_AdGenGponPon15MinPacketFragError_Object = MibTableColumn
adGenGponPon15MinPacketFragError = _AdGenGponPon15MinPacketFragError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 9),
    _AdGenGponPon15MinPacketFragError_Type()
)
adGenGponPon15MinPacketFragError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinPacketFragError.setStatus("current")
_AdGenGponPon15MinIntervalTimeStamp_Type = DisplayString
_AdGenGponPon15MinIntervalTimeStamp_Object = MibTableColumn
adGenGponPon15MinIntervalTimeStamp = _AdGenGponPon15MinIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 10),
    _AdGenGponPon15MinIntervalTimeStamp_Type()
)
adGenGponPon15MinIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinIntervalTimeStamp.setStatus("current")
_AdGenGponPon15MinRxEthernetBytes_Type = Counter64
_AdGenGponPon15MinRxEthernetBytes_Object = MibTableColumn
adGenGponPon15MinRxEthernetBytes = _AdGenGponPon15MinRxEthernetBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 11),
    _AdGenGponPon15MinRxEthernetBytes_Type()
)
adGenGponPon15MinRxEthernetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinRxEthernetBytes.setStatus("current")
_AdGenGponPon15MinTxEthernetBytes_Type = Counter64
_AdGenGponPon15MinTxEthernetBytes_Object = MibTableColumn
adGenGponPon15MinTxEthernetBytes = _AdGenGponPon15MinTxEthernetBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 12),
    _AdGenGponPon15MinTxEthernetBytes_Type()
)
adGenGponPon15MinTxEthernetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinTxEthernetBytes.setStatus("current")
_AdGenGponPon15MinUsBwAverageUtil_Type = Gauge32
_AdGenGponPon15MinUsBwAverageUtil_Object = MibTableColumn
adGenGponPon15MinUsBwAverageUtil = _AdGenGponPon15MinUsBwAverageUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 13),
    _AdGenGponPon15MinUsBwAverageUtil_Type()
)
adGenGponPon15MinUsBwAverageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinUsBwAverageUtil.setStatus("current")
_AdGenGponPon15MinUsBwPeakUtil_Type = Gauge32
_AdGenGponPon15MinUsBwPeakUtil_Object = MibTableColumn
adGenGponPon15MinUsBwPeakUtil = _AdGenGponPon15MinUsBwPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 14),
    _AdGenGponPon15MinUsBwPeakUtil_Type()
)
adGenGponPon15MinUsBwPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinUsBwPeakUtil.setStatus("current")
_AdGenGponPon15MinDsBwAverageUtil_Type = Gauge32
_AdGenGponPon15MinDsBwAverageUtil_Object = MibTableColumn
adGenGponPon15MinDsBwAverageUtil = _AdGenGponPon15MinDsBwAverageUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 15),
    _AdGenGponPon15MinDsBwAverageUtil_Type()
)
adGenGponPon15MinDsBwAverageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinDsBwAverageUtil.setStatus("current")
_AdGenGponPon15MinDsBwPeakUtil_Type = Gauge32
_AdGenGponPon15MinDsBwPeakUtil_Object = MibTableColumn
adGenGponPon15MinDsBwPeakUtil = _AdGenGponPon15MinDsBwPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 16),
    _AdGenGponPon15MinDsBwPeakUtil_Type()
)
adGenGponPon15MinDsBwPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinDsBwPeakUtil.setStatus("current")
_AdGenGponPon15MinDsMulticastPackets_Type = Gauge32
_AdGenGponPon15MinDsMulticastPackets_Object = MibTableColumn
adGenGponPon15MinDsMulticastPackets = _AdGenGponPon15MinDsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 17),
    _AdGenGponPon15MinDsMulticastPackets_Type()
)
adGenGponPon15MinDsMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinDsMulticastPackets.setStatus("current")
_AdGenGponPon15MinDsMulticastBytes_Type = Counter64
_AdGenGponPon15MinDsMulticastBytes_Object = MibTableColumn
adGenGponPon15MinDsMulticastBytes = _AdGenGponPon15MinDsMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 18),
    _AdGenGponPon15MinDsMulticastBytes_Type()
)
adGenGponPon15MinDsMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinDsMulticastBytes.setStatus("current")
_AdGenGponPon15MinDsMulticastBwAverageUtil_Type = Gauge32
_AdGenGponPon15MinDsMulticastBwAverageUtil_Object = MibTableColumn
adGenGponPon15MinDsMulticastBwAverageUtil = _AdGenGponPon15MinDsMulticastBwAverageUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 19),
    _AdGenGponPon15MinDsMulticastBwAverageUtil_Type()
)
adGenGponPon15MinDsMulticastBwAverageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinDsMulticastBwAverageUtil.setStatus("current")
_AdGenGponPon15MinDsMulticastBwPeakUtil_Type = Gauge32
_AdGenGponPon15MinDsMulticastBwPeakUtil_Object = MibTableColumn
adGenGponPon15MinDsMulticastBwPeakUtil = _AdGenGponPon15MinDsMulticastBwPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 20),
    _AdGenGponPon15MinDsMulticastBwPeakUtil_Type()
)
adGenGponPon15MinDsMulticastBwPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinDsMulticastBwPeakUtil.setStatus("current")
_AdGenGponPon15MinDownstreamBIPError_Type = Gauge32
_AdGenGponPon15MinDownstreamBIPError_Object = MibTableColumn
adGenGponPon15MinDownstreamBIPError = _AdGenGponPon15MinDownstreamBIPError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 1, 1, 21),
    _AdGenGponPon15MinDownstreamBIPError_Type()
)
adGenGponPon15MinDownstreamBIPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon15MinDownstreamBIPError.setStatus("current")
_AdGenGponPon24HrPMTable_Object = MibTable
adGenGponPon24HrPMTable = _AdGenGponPon24HrPMTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    adGenGponPon24HrPMTable.setStatus("current")
_AdGenGponPon24HrPMEntry_Object = MibTableRow
adGenGponPon24HrPMEntry = _AdGenGponPon24HrPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1)
)
adGenGponPon24HrPMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENGPON-MIB", "adGenGponPon24HrPMIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenGponPon24HrPMEntry.setStatus("current")


class _AdGenGponPon24HrPMIntervalNumber_Type(Integer32):
    """Custom type adGenGponPon24HrPMIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenGponPon24HrPMIntervalNumber_Type.__name__ = "Integer32"
_AdGenGponPon24HrPMIntervalNumber_Object = MibTableColumn
adGenGponPon24HrPMIntervalNumber = _AdGenGponPon24HrPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 1),
    _AdGenGponPon24HrPMIntervalNumber_Type()
)
adGenGponPon24HrPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenGponPon24HrPMIntervalNumber.setStatus("current")
_AdGenGponPon24HrRxEthernetPackets_Type = Gauge32
_AdGenGponPon24HrRxEthernetPackets_Object = MibTableColumn
adGenGponPon24HrRxEthernetPackets = _AdGenGponPon24HrRxEthernetPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 2),
    _AdGenGponPon24HrRxEthernetPackets_Type()
)
adGenGponPon24HrRxEthernetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrRxEthernetPackets.setStatus("current")
_AdGenGponPon24HrRxOMCIPackets_Type = Gauge32
_AdGenGponPon24HrRxOMCIPackets_Object = MibTableColumn
adGenGponPon24HrRxOMCIPackets = _AdGenGponPon24HrRxOMCIPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 3),
    _AdGenGponPon24HrRxOMCIPackets_Type()
)
adGenGponPon24HrRxOMCIPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrRxOMCIPackets.setStatus("current")
_AdGenGponPon24HrTxEthernetPackets_Type = Gauge32
_AdGenGponPon24HrTxEthernetPackets_Object = MibTableColumn
adGenGponPon24HrTxEthernetPackets = _AdGenGponPon24HrTxEthernetPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 4),
    _AdGenGponPon24HrTxEthernetPackets_Type()
)
adGenGponPon24HrTxEthernetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrTxEthernetPackets.setStatus("current")
_AdGenGponPon24HrTxOMCIPackets_Type = Gauge32
_AdGenGponPon24HrTxOMCIPackets_Object = MibTableColumn
adGenGponPon24HrTxOMCIPackets = _AdGenGponPon24HrTxOMCIPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 5),
    _AdGenGponPon24HrTxOMCIPackets_Type()
)
adGenGponPon24HrTxOMCIPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrTxOMCIPackets.setStatus("current")
_AdGenGponPon24HrUpstreamBIPError_Type = Gauge32
_AdGenGponPon24HrUpstreamBIPError_Object = MibTableColumn
adGenGponPon24HrUpstreamBIPError = _AdGenGponPon24HrUpstreamBIPError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 6),
    _AdGenGponPon24HrUpstreamBIPError_Type()
)
adGenGponPon24HrUpstreamBIPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrUpstreamBIPError.setStatus("current")
_AdGenGponPon24HrUpstreamDroppedPackets_Type = Gauge32
_AdGenGponPon24HrUpstreamDroppedPackets_Object = MibTableColumn
adGenGponPon24HrUpstreamDroppedPackets = _AdGenGponPon24HrUpstreamDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 7),
    _AdGenGponPon24HrUpstreamDroppedPackets_Type()
)
adGenGponPon24HrUpstreamDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrUpstreamDroppedPackets.setStatus("current")
_AdGenGponPon24HrBufferOverflow_Type = Gauge32
_AdGenGponPon24HrBufferOverflow_Object = MibTableColumn
adGenGponPon24HrBufferOverflow = _AdGenGponPon24HrBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 8),
    _AdGenGponPon24HrBufferOverflow_Type()
)
adGenGponPon24HrBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrBufferOverflow.setStatus("current")
_AdGenGponPon24HrPacketFragError_Type = Gauge32
_AdGenGponPon24HrPacketFragError_Object = MibTableColumn
adGenGponPon24HrPacketFragError = _AdGenGponPon24HrPacketFragError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 9),
    _AdGenGponPon24HrPacketFragError_Type()
)
adGenGponPon24HrPacketFragError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrPacketFragError.setStatus("current")
_AdGenGponPon24HrIntervalTimeStamp_Type = DisplayString
_AdGenGponPon24HrIntervalTimeStamp_Object = MibTableColumn
adGenGponPon24HrIntervalTimeStamp = _AdGenGponPon24HrIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 10),
    _AdGenGponPon24HrIntervalTimeStamp_Type()
)
adGenGponPon24HrIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrIntervalTimeStamp.setStatus("current")
_AdGenGponPon24HrRxEthernetBytes_Type = Counter64
_AdGenGponPon24HrRxEthernetBytes_Object = MibTableColumn
adGenGponPon24HrRxEthernetBytes = _AdGenGponPon24HrRxEthernetBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 11),
    _AdGenGponPon24HrRxEthernetBytes_Type()
)
adGenGponPon24HrRxEthernetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrRxEthernetBytes.setStatus("current")
_AdGenGponPon24HrTxEthernetBytes_Type = Counter64
_AdGenGponPon24HrTxEthernetBytes_Object = MibTableColumn
adGenGponPon24HrTxEthernetBytes = _AdGenGponPon24HrTxEthernetBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 12),
    _AdGenGponPon24HrTxEthernetBytes_Type()
)
adGenGponPon24HrTxEthernetBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrTxEthernetBytes.setStatus("current")
_AdGenGponPon24HrUsBwAverageUtil_Type = Gauge32
_AdGenGponPon24HrUsBwAverageUtil_Object = MibTableColumn
adGenGponPon24HrUsBwAverageUtil = _AdGenGponPon24HrUsBwAverageUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 13),
    _AdGenGponPon24HrUsBwAverageUtil_Type()
)
adGenGponPon24HrUsBwAverageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrUsBwAverageUtil.setStatus("current")
_AdGenGponPon24HrUsBwPeakUtil_Type = Gauge32
_AdGenGponPon24HrUsBwPeakUtil_Object = MibTableColumn
adGenGponPon24HrUsBwPeakUtil = _AdGenGponPon24HrUsBwPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 14),
    _AdGenGponPon24HrUsBwPeakUtil_Type()
)
adGenGponPon24HrUsBwPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrUsBwPeakUtil.setStatus("current")
_AdGenGponPon24HrDsBwAverageUtil_Type = Gauge32
_AdGenGponPon24HrDsBwAverageUtil_Object = MibTableColumn
adGenGponPon24HrDsBwAverageUtil = _AdGenGponPon24HrDsBwAverageUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 15),
    _AdGenGponPon24HrDsBwAverageUtil_Type()
)
adGenGponPon24HrDsBwAverageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrDsBwAverageUtil.setStatus("current")
_AdGenGponPon24HrDsBwPeakUtil_Type = Gauge32
_AdGenGponPon24HrDsBwPeakUtil_Object = MibTableColumn
adGenGponPon24HrDsBwPeakUtil = _AdGenGponPon24HrDsBwPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 16),
    _AdGenGponPon24HrDsBwPeakUtil_Type()
)
adGenGponPon24HrDsBwPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrDsBwPeakUtil.setStatus("current")
_AdGenGponPon24HrDsMulticastPackets_Type = Gauge32
_AdGenGponPon24HrDsMulticastPackets_Object = MibTableColumn
adGenGponPon24HrDsMulticastPackets = _AdGenGponPon24HrDsMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 17),
    _AdGenGponPon24HrDsMulticastPackets_Type()
)
adGenGponPon24HrDsMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrDsMulticastPackets.setStatus("current")
_AdGenGponPon24HrDsMulticastBytes_Type = Counter64
_AdGenGponPon24HrDsMulticastBytes_Object = MibTableColumn
adGenGponPon24HrDsMulticastBytes = _AdGenGponPon24HrDsMulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 18),
    _AdGenGponPon24HrDsMulticastBytes_Type()
)
adGenGponPon24HrDsMulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrDsMulticastBytes.setStatus("current")
_AdGenGponPon24HrDsMulticastBwAverageUtil_Type = Gauge32
_AdGenGponPon24HrDsMulticastBwAverageUtil_Object = MibTableColumn
adGenGponPon24HrDsMulticastBwAverageUtil = _AdGenGponPon24HrDsMulticastBwAverageUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 19),
    _AdGenGponPon24HrDsMulticastBwAverageUtil_Type()
)
adGenGponPon24HrDsMulticastBwAverageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrDsMulticastBwAverageUtil.setStatus("current")
_AdGenGponPon24HrDsMulticastBwPeakUtil_Type = Gauge32
_AdGenGponPon24HrDsMulticastBwPeakUtil_Object = MibTableColumn
adGenGponPon24HrDsMulticastBwPeakUtil = _AdGenGponPon24HrDsMulticastBwPeakUtil_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 20),
    _AdGenGponPon24HrDsMulticastBwPeakUtil_Type()
)
adGenGponPon24HrDsMulticastBwPeakUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrDsMulticastBwPeakUtil.setStatus("current")
_AdGenGponPon24HrDownstreamBIPError_Type = Gauge32
_AdGenGponPon24HrDownstreamBIPError_Object = MibTableColumn
adGenGponPon24HrDownstreamBIPError = _AdGenGponPon24HrDownstreamBIPError_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 2, 1, 21),
    _AdGenGponPon24HrDownstreamBIPError_Type()
)
adGenGponPon24HrDownstreamBIPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPon24HrDownstreamBIPError.setStatus("current")
_AdGenGponPonCurrent15MinPMTable_Object = MibTable
adGenGponPonCurrent15MinPMTable = _AdGenGponPonCurrent15MinPMTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    adGenGponPonCurrent15MinPMTable.setStatus("current")
_AdGenGponPonCurrent15MinPMEntry_Object = MibTableRow
adGenGponPonCurrent15MinPMEntry = _AdGenGponPonCurrent15MinPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1)
)
adGenGponPonCurrent15MinPMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponPonCurrent15MinPMEntry.setStatus("current")
_AdGenGponPonRxEthernetPacketsCurrent15Min_Type = Gauge32
_AdGenGponPonRxEthernetPacketsCurrent15Min_Object = MibTableColumn
adGenGponPonRxEthernetPacketsCurrent15Min = _AdGenGponPonRxEthernetPacketsCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 2),
    _AdGenGponPonRxEthernetPacketsCurrent15Min_Type()
)
adGenGponPonRxEthernetPacketsCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonRxEthernetPacketsCurrent15Min.setStatus("current")
_AdGenGponPonRxOMCIPacketsCurrent15Min_Type = Gauge32
_AdGenGponPonRxOMCIPacketsCurrent15Min_Object = MibTableColumn
adGenGponPonRxOMCIPacketsCurrent15Min = _AdGenGponPonRxOMCIPacketsCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 3),
    _AdGenGponPonRxOMCIPacketsCurrent15Min_Type()
)
adGenGponPonRxOMCIPacketsCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonRxOMCIPacketsCurrent15Min.setStatus("current")
_AdGenGponPonTxEthernetPacketsCurrent15Min_Type = Gauge32
_AdGenGponPonTxEthernetPacketsCurrent15Min_Object = MibTableColumn
adGenGponPonTxEthernetPacketsCurrent15Min = _AdGenGponPonTxEthernetPacketsCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 4),
    _AdGenGponPonTxEthernetPacketsCurrent15Min_Type()
)
adGenGponPonTxEthernetPacketsCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTxEthernetPacketsCurrent15Min.setStatus("current")
_AdGenGponPonTxOMCIPacketsCurrent15Min_Type = Gauge32
_AdGenGponPonTxOMCIPacketsCurrent15Min_Object = MibTableColumn
adGenGponPonTxOMCIPacketsCurrent15Min = _AdGenGponPonTxOMCIPacketsCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 5),
    _AdGenGponPonTxOMCIPacketsCurrent15Min_Type()
)
adGenGponPonTxOMCIPacketsCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTxOMCIPacketsCurrent15Min.setStatus("current")
_AdGenGponPonUpstreamBIPErrorCurrent15Min_Type = Gauge32
_AdGenGponPonUpstreamBIPErrorCurrent15Min_Object = MibTableColumn
adGenGponPonUpstreamBIPErrorCurrent15Min = _AdGenGponPonUpstreamBIPErrorCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 6),
    _AdGenGponPonUpstreamBIPErrorCurrent15Min_Type()
)
adGenGponPonUpstreamBIPErrorCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonUpstreamBIPErrorCurrent15Min.setStatus("current")
_AdGenGponPonUpstreamDroppedPacketsCurrent15Min_Type = Gauge32
_AdGenGponPonUpstreamDroppedPacketsCurrent15Min_Object = MibTableColumn
adGenGponPonUpstreamDroppedPacketsCurrent15Min = _AdGenGponPonUpstreamDroppedPacketsCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 7),
    _AdGenGponPonUpstreamDroppedPacketsCurrent15Min_Type()
)
adGenGponPonUpstreamDroppedPacketsCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonUpstreamDroppedPacketsCurrent15Min.setStatus("current")
_AdGenGponPonBufferOverflowCurrent15Min_Type = Gauge32
_AdGenGponPonBufferOverflowCurrent15Min_Object = MibTableColumn
adGenGponPonBufferOverflowCurrent15Min = _AdGenGponPonBufferOverflowCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 8),
    _AdGenGponPonBufferOverflowCurrent15Min_Type()
)
adGenGponPonBufferOverflowCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonBufferOverflowCurrent15Min.setStatus("current")
_AdGenGponPonPacketFragErrorCurrent15Min_Type = Gauge32
_AdGenGponPonPacketFragErrorCurrent15Min_Object = MibTableColumn
adGenGponPonPacketFragErrorCurrent15Min = _AdGenGponPonPacketFragErrorCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 9),
    _AdGenGponPonPacketFragErrorCurrent15Min_Type()
)
adGenGponPonPacketFragErrorCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonPacketFragErrorCurrent15Min.setStatus("current")
_AdGenGponPonRxEthernetBytesCurrent15Min_Type = Counter64
_AdGenGponPonRxEthernetBytesCurrent15Min_Object = MibTableColumn
adGenGponPonRxEthernetBytesCurrent15Min = _AdGenGponPonRxEthernetBytesCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 10),
    _AdGenGponPonRxEthernetBytesCurrent15Min_Type()
)
adGenGponPonRxEthernetBytesCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonRxEthernetBytesCurrent15Min.setStatus("current")
_AdGenGponPonTxEthernetBytesCurrent15Min_Type = Counter64
_AdGenGponPonTxEthernetBytesCurrent15Min_Object = MibTableColumn
adGenGponPonTxEthernetBytesCurrent15Min = _AdGenGponPonTxEthernetBytesCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 11),
    _AdGenGponPonTxEthernetBytesCurrent15Min_Type()
)
adGenGponPonTxEthernetBytesCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTxEthernetBytesCurrent15Min.setStatus("current")
_AdGenGponPonUsBwAverageUtilCurrent15Min_Type = Gauge32
_AdGenGponPonUsBwAverageUtilCurrent15Min_Object = MibTableColumn
adGenGponPonUsBwAverageUtilCurrent15Min = _AdGenGponPonUsBwAverageUtilCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 12),
    _AdGenGponPonUsBwAverageUtilCurrent15Min_Type()
)
adGenGponPonUsBwAverageUtilCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonUsBwAverageUtilCurrent15Min.setStatus("current")
_AdGenGponPonUsBwPeakUtilCurrent15Min_Type = Gauge32
_AdGenGponPonUsBwPeakUtilCurrent15Min_Object = MibTableColumn
adGenGponPonUsBwPeakUtilCurrent15Min = _AdGenGponPonUsBwPeakUtilCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 13),
    _AdGenGponPonUsBwPeakUtilCurrent15Min_Type()
)
adGenGponPonUsBwPeakUtilCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonUsBwPeakUtilCurrent15Min.setStatus("current")
_AdGenGponPonDsBwAverageUtilCurrent15Min_Type = Gauge32
_AdGenGponPonDsBwAverageUtilCurrent15Min_Object = MibTableColumn
adGenGponPonDsBwAverageUtilCurrent15Min = _AdGenGponPonDsBwAverageUtilCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 14),
    _AdGenGponPonDsBwAverageUtilCurrent15Min_Type()
)
adGenGponPonDsBwAverageUtilCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsBwAverageUtilCurrent15Min.setStatus("current")
_AdGenGponPonDsBwPeakUtilCurrent15Min_Type = Gauge32
_AdGenGponPonDsBwPeakUtilCurrent15Min_Object = MibTableColumn
adGenGponPonDsBwPeakUtilCurrent15Min = _AdGenGponPonDsBwPeakUtilCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 15),
    _AdGenGponPonDsBwPeakUtilCurrent15Min_Type()
)
adGenGponPonDsBwPeakUtilCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsBwPeakUtilCurrent15Min.setStatus("current")
_AdGenGponPonDsMulticastPacketsCurrent15Min_Type = Gauge32
_AdGenGponPonDsMulticastPacketsCurrent15Min_Object = MibTableColumn
adGenGponPonDsMulticastPacketsCurrent15Min = _AdGenGponPonDsMulticastPacketsCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 16),
    _AdGenGponPonDsMulticastPacketsCurrent15Min_Type()
)
adGenGponPonDsMulticastPacketsCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsMulticastPacketsCurrent15Min.setStatus("current")
_AdGenGponPonDsMulticastBytesCurrent15Min_Type = Counter64
_AdGenGponPonDsMulticastBytesCurrent15Min_Object = MibTableColumn
adGenGponPonDsMulticastBytesCurrent15Min = _AdGenGponPonDsMulticastBytesCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 17),
    _AdGenGponPonDsMulticastBytesCurrent15Min_Type()
)
adGenGponPonDsMulticastBytesCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsMulticastBytesCurrent15Min.setStatus("current")
_AdGenGponPonDsMulticastBwAverageUtilCurrent15Min_Type = Gauge32
_AdGenGponPonDsMulticastBwAverageUtilCurrent15Min_Object = MibTableColumn
adGenGponPonDsMulticastBwAverageUtilCurrent15Min = _AdGenGponPonDsMulticastBwAverageUtilCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 18),
    _AdGenGponPonDsMulticastBwAverageUtilCurrent15Min_Type()
)
adGenGponPonDsMulticastBwAverageUtilCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsMulticastBwAverageUtilCurrent15Min.setStatus("current")
_AdGenGponPonDsMulticastBwPeakUtilCurrent15Min_Type = Gauge32
_AdGenGponPonDsMulticastBwPeakUtilCurrent15Min_Object = MibTableColumn
adGenGponPonDsMulticastBwPeakUtilCurrent15Min = _AdGenGponPonDsMulticastBwPeakUtilCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 19),
    _AdGenGponPonDsMulticastBwPeakUtilCurrent15Min_Type()
)
adGenGponPonDsMulticastBwPeakUtilCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsMulticastBwPeakUtilCurrent15Min.setStatus("current")
_AdGenGponPonDownstreamBIPErrorCurrent15Min_Type = Gauge32
_AdGenGponPonDownstreamBIPErrorCurrent15Min_Object = MibTableColumn
adGenGponPonDownstreamBIPErrorCurrent15Min = _AdGenGponPonDownstreamBIPErrorCurrent15Min_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 3, 1, 20),
    _AdGenGponPonDownstreamBIPErrorCurrent15Min_Type()
)
adGenGponPonDownstreamBIPErrorCurrent15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDownstreamBIPErrorCurrent15Min.setStatus("current")
_AdGenGponPonCurrent24HrPMTable_Object = MibTable
adGenGponPonCurrent24HrPMTable = _AdGenGponPonCurrent24HrPMTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    adGenGponPonCurrent24HrPMTable.setStatus("current")
_AdGenGponPonCurrent24HrPMEntry_Object = MibTableRow
adGenGponPonCurrent24HrPMEntry = _AdGenGponPonCurrent24HrPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1)
)
adGenGponPonCurrent24HrPMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponPonCurrent24HrPMEntry.setStatus("current")
_AdGenGponPonRxEthernetPacketsCurrent24Hr_Type = Gauge32
_AdGenGponPonRxEthernetPacketsCurrent24Hr_Object = MibTableColumn
adGenGponPonRxEthernetPacketsCurrent24Hr = _AdGenGponPonRxEthernetPacketsCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 2),
    _AdGenGponPonRxEthernetPacketsCurrent24Hr_Type()
)
adGenGponPonRxEthernetPacketsCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonRxEthernetPacketsCurrent24Hr.setStatus("current")
_AdGenGponPonRxOMCIPacketsCurrent24Hr_Type = Gauge32
_AdGenGponPonRxOMCIPacketsCurrent24Hr_Object = MibTableColumn
adGenGponPonRxOMCIPacketsCurrent24Hr = _AdGenGponPonRxOMCIPacketsCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 3),
    _AdGenGponPonRxOMCIPacketsCurrent24Hr_Type()
)
adGenGponPonRxOMCIPacketsCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonRxOMCIPacketsCurrent24Hr.setStatus("current")
_AdGenGponPonTxEthernetPacketsCurrent24Hr_Type = Gauge32
_AdGenGponPonTxEthernetPacketsCurrent24Hr_Object = MibTableColumn
adGenGponPonTxEthernetPacketsCurrent24Hr = _AdGenGponPonTxEthernetPacketsCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 4),
    _AdGenGponPonTxEthernetPacketsCurrent24Hr_Type()
)
adGenGponPonTxEthernetPacketsCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTxEthernetPacketsCurrent24Hr.setStatus("current")
_AdGenGponPonTxOMCIPacketsCurrent24Hr_Type = Gauge32
_AdGenGponPonTxOMCIPacketsCurrent24Hr_Object = MibTableColumn
adGenGponPonTxOMCIPacketsCurrent24Hr = _AdGenGponPonTxOMCIPacketsCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 5),
    _AdGenGponPonTxOMCIPacketsCurrent24Hr_Type()
)
adGenGponPonTxOMCIPacketsCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTxOMCIPacketsCurrent24Hr.setStatus("current")
_AdGenGponPonUpstreamBIPErrorCurrent24Hr_Type = Gauge32
_AdGenGponPonUpstreamBIPErrorCurrent24Hr_Object = MibTableColumn
adGenGponPonUpstreamBIPErrorCurrent24Hr = _AdGenGponPonUpstreamBIPErrorCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 6),
    _AdGenGponPonUpstreamBIPErrorCurrent24Hr_Type()
)
adGenGponPonUpstreamBIPErrorCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonUpstreamBIPErrorCurrent24Hr.setStatus("current")
_AdGenGponPonUpstreamDroppedPacketsCurrent24Hr_Type = Gauge32
_AdGenGponPonUpstreamDroppedPacketsCurrent24Hr_Object = MibTableColumn
adGenGponPonUpstreamDroppedPacketsCurrent24Hr = _AdGenGponPonUpstreamDroppedPacketsCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 7),
    _AdGenGponPonUpstreamDroppedPacketsCurrent24Hr_Type()
)
adGenGponPonUpstreamDroppedPacketsCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonUpstreamDroppedPacketsCurrent24Hr.setStatus("current")
_AdGenGponPonBufferOverflowCurrent24Hr_Type = Gauge32
_AdGenGponPonBufferOverflowCurrent24Hr_Object = MibTableColumn
adGenGponPonBufferOverflowCurrent24Hr = _AdGenGponPonBufferOverflowCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 8),
    _AdGenGponPonBufferOverflowCurrent24Hr_Type()
)
adGenGponPonBufferOverflowCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonBufferOverflowCurrent24Hr.setStatus("current")
_AdGenGponPonPacketFragErrorCurrent24Hr_Type = Gauge32
_AdGenGponPonPacketFragErrorCurrent24Hr_Object = MibTableColumn
adGenGponPonPacketFragErrorCurrent24Hr = _AdGenGponPonPacketFragErrorCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 9),
    _AdGenGponPonPacketFragErrorCurrent24Hr_Type()
)
adGenGponPonPacketFragErrorCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonPacketFragErrorCurrent24Hr.setStatus("current")
_AdGenGponPonRxEthernetBytesCurrent24Hr_Type = Counter64
_AdGenGponPonRxEthernetBytesCurrent24Hr_Object = MibTableColumn
adGenGponPonRxEthernetBytesCurrent24Hr = _AdGenGponPonRxEthernetBytesCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 10),
    _AdGenGponPonRxEthernetBytesCurrent24Hr_Type()
)
adGenGponPonRxEthernetBytesCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonRxEthernetBytesCurrent24Hr.setStatus("current")
_AdGenGponPonTxEthernetBytesCurrent24Hr_Type = Counter64
_AdGenGponPonTxEthernetBytesCurrent24Hr_Object = MibTableColumn
adGenGponPonTxEthernetBytesCurrent24Hr = _AdGenGponPonTxEthernetBytesCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 11),
    _AdGenGponPonTxEthernetBytesCurrent24Hr_Type()
)
adGenGponPonTxEthernetBytesCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonTxEthernetBytesCurrent24Hr.setStatus("current")
_AdGenGponPonUsBwAverageUtilCurrent24Hr_Type = Gauge32
_AdGenGponPonUsBwAverageUtilCurrent24Hr_Object = MibTableColumn
adGenGponPonUsBwAverageUtilCurrent24Hr = _AdGenGponPonUsBwAverageUtilCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 12),
    _AdGenGponPonUsBwAverageUtilCurrent24Hr_Type()
)
adGenGponPonUsBwAverageUtilCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonUsBwAverageUtilCurrent24Hr.setStatus("current")
_AdGenGponPonUsBwPeakUtilCurrent24Hr_Type = Gauge32
_AdGenGponPonUsBwPeakUtilCurrent24Hr_Object = MibTableColumn
adGenGponPonUsBwPeakUtilCurrent24Hr = _AdGenGponPonUsBwPeakUtilCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 13),
    _AdGenGponPonUsBwPeakUtilCurrent24Hr_Type()
)
adGenGponPonUsBwPeakUtilCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonUsBwPeakUtilCurrent24Hr.setStatus("current")
_AdGenGponPonDsBwAverageUtilCurrent24Hr_Type = Gauge32
_AdGenGponPonDsBwAverageUtilCurrent24Hr_Object = MibTableColumn
adGenGponPonDsBwAverageUtilCurrent24Hr = _AdGenGponPonDsBwAverageUtilCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 14),
    _AdGenGponPonDsBwAverageUtilCurrent24Hr_Type()
)
adGenGponPonDsBwAverageUtilCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsBwAverageUtilCurrent24Hr.setStatus("current")
_AdGenGponPonDsBwPeakUtilCurrent24Hr_Type = Gauge32
_AdGenGponPonDsBwPeakUtilCurrent24Hr_Object = MibTableColumn
adGenGponPonDsBwPeakUtilCurrent24Hr = _AdGenGponPonDsBwPeakUtilCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 15),
    _AdGenGponPonDsBwPeakUtilCurrent24Hr_Type()
)
adGenGponPonDsBwPeakUtilCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsBwPeakUtilCurrent24Hr.setStatus("current")
_AdGenGponPonDsMulticastPacketsCurrent24Hr_Type = Gauge32
_AdGenGponPonDsMulticastPacketsCurrent24Hr_Object = MibTableColumn
adGenGponPonDsMulticastPacketsCurrent24Hr = _AdGenGponPonDsMulticastPacketsCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 16),
    _AdGenGponPonDsMulticastPacketsCurrent24Hr_Type()
)
adGenGponPonDsMulticastPacketsCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsMulticastPacketsCurrent24Hr.setStatus("current")
_AdGenGponPonDsMulticastBytesCurrent24Hr_Type = Counter64
_AdGenGponPonDsMulticastBytesCurrent24Hr_Object = MibTableColumn
adGenGponPonDsMulticastBytesCurrent24Hr = _AdGenGponPonDsMulticastBytesCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 17),
    _AdGenGponPonDsMulticastBytesCurrent24Hr_Type()
)
adGenGponPonDsMulticastBytesCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsMulticastBytesCurrent24Hr.setStatus("current")
_AdGenGponPonDsMulticastBwAverageUtilCurrent24Hr_Type = Gauge32
_AdGenGponPonDsMulticastBwAverageUtilCurrent24Hr_Object = MibTableColumn
adGenGponPonDsMulticastBwAverageUtilCurrent24Hr = _AdGenGponPonDsMulticastBwAverageUtilCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 18),
    _AdGenGponPonDsMulticastBwAverageUtilCurrent24Hr_Type()
)
adGenGponPonDsMulticastBwAverageUtilCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsMulticastBwAverageUtilCurrent24Hr.setStatus("current")
_AdGenGponPonDsMulticastBwPeakUtilCurrent24Hr_Type = Gauge32
_AdGenGponPonDsMulticastBwPeakUtilCurrent24Hr_Object = MibTableColumn
adGenGponPonDsMulticastBwPeakUtilCurrent24Hr = _AdGenGponPonDsMulticastBwPeakUtilCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 19),
    _AdGenGponPonDsMulticastBwPeakUtilCurrent24Hr_Type()
)
adGenGponPonDsMulticastBwPeakUtilCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDsMulticastBwPeakUtilCurrent24Hr.setStatus("current")
_AdGenGponPonDownstreamBIPErrorCurrent24Hr_Type = Gauge32
_AdGenGponPonDownstreamBIPErrorCurrent24Hr_Object = MibTableColumn
adGenGponPonDownstreamBIPErrorCurrent24Hr = _AdGenGponPonDownstreamBIPErrorCurrent24Hr_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 4, 1, 20),
    _AdGenGponPonDownstreamBIPErrorCurrent24Hr_Type()
)
adGenGponPonDownstreamBIPErrorCurrent24Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponPonDownstreamBIPErrorCurrent24Hr.setStatus("current")
_AdGenGponPonPerfResetTable_Object = MibTable
adGenGponPonPerfResetTable = _AdGenGponPonPerfResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    adGenGponPonPerfResetTable.setStatus("current")
_AdGenGponPonPerfResetEntry_Object = MibTableRow
adGenGponPonPerfResetEntry = _AdGenGponPonPerfResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 5, 1)
)
adGenGponPonPerfResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponPonPerfResetEntry.setStatus("current")


class _AdGenGponPonPerfReset_Type(Integer32):
    """Custom type adGenGponPonPerfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenGponPonPerfReset_Type.__name__ = "Integer32"
_AdGenGponPonPerfReset_Object = MibTableColumn
adGenGponPonPerfReset = _AdGenGponPonPerfReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 5, 1, 1),
    _AdGenGponPonPerfReset_Type()
)
adGenGponPonPerfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonPerfReset.setStatus("current")
_AdGenGponOntVideoReturnPathCountersResetTable_Object = MibTable
adGenGponOntVideoReturnPathCountersResetTable = _AdGenGponOntVideoReturnPathCountersResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathCountersResetTable.setStatus("current")
_AdGenGponOntVideoReturnPathCountersResetEntry_Object = MibTableRow
adGenGponOntVideoReturnPathCountersResetEntry = _AdGenGponOntVideoReturnPathCountersResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 6, 1)
)
adGenGponOntVideoReturnPathCountersResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathCountersResetEntry.setStatus("current")


class _AdGenGponOntVideoReturnPathCountersReset_Type(Integer32):
    """Custom type adGenGponOntVideoReturnPathCountersReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenGponOntVideoReturnPathCountersReset_Type.__name__ = "Integer32"
_AdGenGponOntVideoReturnPathCountersReset_Object = MibTableColumn
adGenGponOntVideoReturnPathCountersReset = _AdGenGponOntVideoReturnPathCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 6, 1, 1),
    _AdGenGponOntVideoReturnPathCountersReset_Type()
)
adGenGponOntVideoReturnPathCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathCountersReset.setStatus("current")
_AdGenGponOntVideoReturnPathCountersTable_Object = MibTable
adGenGponOntVideoReturnPathCountersTable = _AdGenGponOntVideoReturnPathCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathCountersTable.setStatus("current")
_AdGenGponOntVideoReturnPathCountersEntry_Object = MibTableRow
adGenGponOntVideoReturnPathCountersEntry = _AdGenGponOntVideoReturnPathCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7, 1)
)
adGenGponOntVideoReturnPathCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathCountersEntry.setStatus("current")
_AdGenGponOntVideoReturnPathRxTotalBursts_Type = Counter32
_AdGenGponOntVideoReturnPathRxTotalBursts_Object = MibTableColumn
adGenGponOntVideoReturnPathRxTotalBursts = _AdGenGponOntVideoReturnPathRxTotalBursts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7, 1, 1),
    _AdGenGponOntVideoReturnPathRxTotalBursts_Type()
)
adGenGponOntVideoReturnPathRxTotalBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathRxTotalBursts.setStatus("current")
_AdGenGponOntVideoReturnPathRxGoodBursts_Type = Counter32
_AdGenGponOntVideoReturnPathRxGoodBursts_Object = MibTableColumn
adGenGponOntVideoReturnPathRxGoodBursts = _AdGenGponOntVideoReturnPathRxGoodBursts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7, 1, 2),
    _AdGenGponOntVideoReturnPathRxGoodBursts_Type()
)
adGenGponOntVideoReturnPathRxGoodBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathRxGoodBursts.setStatus("current")
_AdGenGponOntVideoReturnPathRxFECCorrectedBursts_Type = Counter32
_AdGenGponOntVideoReturnPathRxFECCorrectedBursts_Object = MibTableColumn
adGenGponOntVideoReturnPathRxFECCorrectedBursts = _AdGenGponOntVideoReturnPathRxFECCorrectedBursts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7, 1, 3),
    _AdGenGponOntVideoReturnPathRxFECCorrectedBursts_Type()
)
adGenGponOntVideoReturnPathRxFECCorrectedBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathRxFECCorrectedBursts.setStatus("current")
_AdGenGponOntVideoReturnPathRxMissedBursts_Type = Counter32
_AdGenGponOntVideoReturnPathRxMissedBursts_Object = MibTableColumn
adGenGponOntVideoReturnPathRxMissedBursts = _AdGenGponOntVideoReturnPathRxMissedBursts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7, 1, 4),
    _AdGenGponOntVideoReturnPathRxMissedBursts_Type()
)
adGenGponOntVideoReturnPathRxMissedBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathRxMissedBursts.setStatus("current")


class _AdGenGponOntVideoReturnPathRxMinPower_Type(Integer32):
    """Custom type adGenGponOntVideoReturnPathRxMinPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntVideoReturnPathRxMinPower_Type.__name__ = "Integer32"
_AdGenGponOntVideoReturnPathRxMinPower_Object = MibTableColumn
adGenGponOntVideoReturnPathRxMinPower = _AdGenGponOntVideoReturnPathRxMinPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7, 1, 5),
    _AdGenGponOntVideoReturnPathRxMinPower_Type()
)
adGenGponOntVideoReturnPathRxMinPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathRxMinPower.setStatus("current")


class _AdGenGponOntVideoReturnPathRxMaxPower_Type(Integer32):
    """Custom type adGenGponOntVideoReturnPathRxMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntVideoReturnPathRxMaxPower_Type.__name__ = "Integer32"
_AdGenGponOntVideoReturnPathRxMaxPower_Object = MibTableColumn
adGenGponOntVideoReturnPathRxMaxPower = _AdGenGponOntVideoReturnPathRxMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7, 1, 6),
    _AdGenGponOntVideoReturnPathRxMaxPower_Type()
)
adGenGponOntVideoReturnPathRxMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathRxMaxPower.setStatus("current")


class _AdGenGponOntVideoReturnPathRxCurrentPower_Type(Integer32):
    """Custom type adGenGponOntVideoReturnPathRxCurrentPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenGponOntVideoReturnPathRxCurrentPower_Type.__name__ = "Integer32"
_AdGenGponOntVideoReturnPathRxCurrentPower_Object = MibTableColumn
adGenGponOntVideoReturnPathRxCurrentPower = _AdGenGponOntVideoReturnPathRxCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7, 1, 7),
    _AdGenGponOntVideoReturnPathRxCurrentPower_Type()
)
adGenGponOntVideoReturnPathRxCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathRxCurrentPower.setStatus("current")
_AdGenGponOntVideoReturnPathRxFECCorrectedSymbols_Type = Counter32
_AdGenGponOntVideoReturnPathRxFECCorrectedSymbols_Object = MibTableColumn
adGenGponOntVideoReturnPathRxFECCorrectedSymbols = _AdGenGponOntVideoReturnPathRxFECCorrectedSymbols_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 7, 1, 8),
    _AdGenGponOntVideoReturnPathRxFECCorrectedSymbols_Type()
)
adGenGponOntVideoReturnPathRxFECCorrectedSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGponOntVideoReturnPathRxFECCorrectedSymbols.setStatus("current")
_AdGenGponPonCounterResetTable_Object = MibTable
adGenGponPonCounterResetTable = _AdGenGponPonCounterResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    adGenGponPonCounterResetTable.setStatus("current")
_AdGenGponPonCounterResetEntry_Object = MibTableRow
adGenGponPonCounterResetEntry = _AdGenGponPonCounterResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 8, 1)
)
adGenGponPonCounterResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenGponPonCounterResetEntry.setStatus("current")


class _AdGenGponPonBIPCountersReset_Type(Integer32):
    """Custom type adGenGponPonBIPCountersReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenGponPonBIPCountersReset_Type.__name__ = "Integer32"
_AdGenGponPonBIPCountersReset_Object = MibTableColumn
adGenGponPonBIPCountersReset = _AdGenGponPonBIPCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 4, 8, 1, 1),
    _AdGenGponPonBIPCountersReset_Type()
)
adGenGponPonBIPCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponPonBIPCountersReset.setStatus("current")
_AdGponAlarms_ObjectIdentity = ObjectIdentity
adGponAlarms = _AdGponAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5)
)
_AdGponOntAlarmEventsPrefix_ObjectIdentity = ObjectIdentity
adGponOntAlarmEventsPrefix = _AdGponOntAlarmEventsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1)
)
_AdGponOntAlarmEvents_ObjectIdentity = ObjectIdentity
adGponOntAlarmEvents = _AdGponOntAlarmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0)
)
_AdGponOntPortAlarmEventsPrefix_ObjectIdentity = ObjectIdentity
adGponOntPortAlarmEventsPrefix = _AdGponOntPortAlarmEventsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2)
)
_AdGponOntPortAlarmEvents_ObjectIdentity = ObjectIdentity
adGponOntPortAlarmEvents = _AdGponOntPortAlarmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2, 0)
)
_AdGponTests_ObjectIdentity = ObjectIdentity
adGponTests = _AdGponTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 6)
)
_AdGponOntTest_ObjectIdentity = ObjectIdentity
adGponOntTest = _AdGponOntTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 6, 1)
)


class _AdGenGponOntReset_Type(Integer32):
    """Custom type adGenGponOntReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deactivateOnt", 1),
          ("rebootOnt", 2))
    )


_AdGenGponOntReset_Type.__name__ = "Integer32"
_AdGenGponOntReset_Object = MibScalar
adGenGponOntReset = _AdGenGponOntReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 6, 1, 1),
    _AdGenGponOntReset_Type()
)
adGenGponOntReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenGponOntReset.setStatus("current")

# Managed Objects groups


# Notification objects

adGenGponOntClrLOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 1)
)
adGenGponOntClrLOSAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntAlarmSlotLosLevel"))
)
if mibBuilder.loadTexts:
    adGenGponOntClrLOSAlarm.setStatus(
        "current"
    )

adGenGponOntSetLOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 2)
)
adGenGponOntSetLOSAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntAlarmSlotLosLevel"))
)
if mibBuilder.loadTexts:
    adGenGponOntSetLOSAlarm.setStatus(
        "current"
    )

adGenGponOntClrEquipmentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 3)
)
adGenGponOntClrEquipmentAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntClrEquipmentAlarm.setStatus(
        "current"
    )

adGenGponOntSetEquipmentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 4)
)
adGenGponOntSetEquipmentAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntSetEquipmentAlarm.setStatus(
        "current"
    )

adGenGponOntClrPoweringAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 5)
)
adGenGponOntClrPoweringAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntAlarmSlotPoweringLevel"))
)
if mibBuilder.loadTexts:
    adGenGponOntClrPoweringAlarm.setStatus(
        "current"
    )

adGenGponOntSetPoweringAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 6)
)
adGenGponOntSetPoweringAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntAlarmSlotPoweringLevel"))
)
if mibBuilder.loadTexts:
    adGenGponOntSetPoweringAlarm.setStatus(
        "current"
    )

adGenGponOntClrBatteryMissingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 7)
)
adGenGponOntClrBatteryMissingAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntClrBatteryMissingAlarm.setStatus(
        "current"
    )

adGenGponOntSetBatteryMissingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 8)
)
adGenGponOntSetBatteryMissingAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntSetBatteryMissingAlarm.setStatus(
        "current"
    )

adGenGponOntClrBatteryFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 9)
)
adGenGponOntClrBatteryFailureAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntClrBatteryFailureAlarm.setStatus(
        "current"
    )

adGenGponOntSetBatteryFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 10)
)
adGenGponOntSetBatteryFailureAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntSetBatteryFailureAlarm.setStatus(
        "current"
    )

adGenGponOntClrBatteryLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 11)
)
adGenGponOntClrBatteryLowAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntClrBatteryLowAlarm.setStatus(
        "current"
    )

adGenGponOntSetBatteryLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 12)
)
adGenGponOntSetBatteryLowAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntSetBatteryLowAlarm.setStatus(
        "current"
    )

adGenGponOntClrPhyIntrustionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 13)
)
adGenGponOntClrPhyIntrustionAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntClrPhyIntrustionAlarm.setStatus(
        "current"
    )

adGenGponOntSetPhyIntrusionAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 14)
)
adGenGponOntSetPhyIntrusionAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntSetPhyIntrusionAlarm.setStatus(
        "current"
    )

adGenGponOntDiscoveryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 15)
)
adGenGponOntDiscoveryAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonDiscoveredOntSerialNumber"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonDiscoveredRegistrationId"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonTechnology"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonWavelength"))
)
if mibBuilder.loadTexts:
    adGenGponOntDiscoveryAlarm.setStatus(
        "current"
    )

adGenGponOntActivationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 16)
)
adGenGponOntActivationAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntActiveSoftwareVersion"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntPartNumber"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntHardwareRevision"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntLearnedSerialNumber"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntRegistrationId"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntInactiveSoftwareVersion"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntEverActivated"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonTechnology"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonWavelength"))
)
if mibBuilder.loadTexts:
    adGenGponOntActivationAlarm.setStatus(
        "current"
    )

adGenGponConfigServerAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 18)
)
adGenGponConfigServerAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponConfigServerAlarmClear.setStatus(
        "current"
    )

adGenGponConfigServerAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 19)
)
adGenGponConfigServerAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponConfigServerAlarmSet.setStatus(
        "current"
    )

adGenGponConfigFileAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 20)
)
adGenGponConfigFileAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponConfigFileAlarmClear.setStatus(
        "current"
    )

adGenGponConfigFileAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 21)
)
adGenGponConfigFileAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponConfigFileAlarmSet.setStatus(
        "current"
    )

adGenGponConfigChecksumMismatchAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 22)
)
adGenGponConfigChecksumMismatchAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponConfigChecksumMismatchAlarmClear.setStatus(
        "current"
    )

adGenGponConfigChecksumMismatchAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 23)
)
adGenGponConfigChecksumMismatchAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponConfigChecksumMismatchAlarmSet.setStatus(
        "current"
    )

adGenGponOntOMCICommFailAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 24)
)
adGenGponOntOMCICommFailAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntOMCICommFailAlarmClear.setStatus(
        "current"
    )

adGenGponOntOMCICommFailAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 25)
)
adGenGponOntOMCICommFailAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntOMCICommFailAlarmSet.setStatus(
        "current"
    )

adGenGponCirOversubscribedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 26)
)
adGenGponCirOversubscribedAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponCirOversubscribedAlarmClear.setStatus(
        "current"
    )

adGenGponCirOversubscribedAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 27)
)
adGenGponCirOversubscribedAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponCirOversubscribedAlarmSet.setStatus(
        "current"
    )

adGenGponPonLosAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 28)
)
adGenGponPonLosAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonLosNumOntsDown"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonDescriptionString"))
)
if mibBuilder.loadTexts:
    adGenGponPonLosAlarmClear.setStatus(
        "current"
    )

adGenGponPonLosAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 29)
)
adGenGponPonLosAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonLosNumOntsDown"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonDescriptionString"))
)
if mibBuilder.loadTexts:
    adGenGponPonLosAlarmSet.setStatus(
        "current"
    )

adGenGponMulticastBwThresholdAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 30)
)
adGenGponMulticastBwThresholdAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponMulticastBwThresholdAlarmClear.setStatus(
        "current"
    )

adGenGponMulticastBwThresholdAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 31)
)
adGenGponMulticastBwThresholdAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponMulticastBwThresholdAlarmSet.setStatus(
        "current"
    )

adGenGponPonDiscoveredInvalidSNAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 32)
)
adGenGponPonDiscoveredInvalidSNAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponPonDiscoveredOntSerialNumber"))
)
if mibBuilder.loadTexts:
    adGenGponPonDiscoveredInvalidSNAlarm.setStatus(
        "current"
    )

adGenGponOntInvalidSNAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 33)
)
adGenGponOntInvalidSNAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntLearnedSerialNumber"))
)
if mibBuilder.loadTexts:
    adGenGponOntInvalidSNAlarm.setStatus(
        "current"
    )

adGenGponOntUpstreamBipTcaAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 34)
)
adGenGponOntUpstreamBipTcaAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntUpstreamBipTcaAlarmClear.setStatus(
        "current"
    )

adGenGponOntUpstreamBipTcaAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 35)
)
adGenGponOntUpstreamBipTcaAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntUpstreamBipTcaAlarmSet.setStatus(
        "current"
    )

adGenGponOntDownstreamBipTcaAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 36)
)
adGenGponOntDownstreamBipTcaAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntDownstreamBipTcaAlarmClear.setStatus(
        "current"
    )

adGenGponOntDownstreamBipTcaAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 37)
)
adGenGponOntDownstreamBipTcaAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntDownstreamBipTcaAlarmSet.setStatus(
        "current"
    )

adGenGponOntDyingGaspAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 38)
)
adGenGponOntDyingGaspAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntAlarmSlotDyingGaspLevel"))
)
if mibBuilder.loadTexts:
    adGenGponOntDyingGaspAlarm.setStatus(
        "current"
    )

adGenGponPonFailoverAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 39)
)
adGenGponPonFailoverAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponPonFailoverAlarmClear.setStatus(
        "current"
    )

adGenGponPonFailoverAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 40)
)
adGenGponPonFailoverAlarmActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponPonFailoverAlarmActive.setStatus(
        "current"
    )

adGenGponPonHwFailureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 41)
)
adGenGponPonHwFailureAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenGponPonHwFailureAlarmClear.setStatus(
        "current"
    )

adGenGponPonHwFailureAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 42)
)
adGenGponPonHwFailureAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenGponPonHwFailureAlarmSet.setStatus(
        "current"
    )

adGenGponPonDegradationAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 43)
)
adGenGponPonDegradationAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenGponPonDegradationAlarmClear.setStatus(
        "current"
    )

adGenGponPonDegradationAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 44)
)
adGenGponPonDegradationAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenGponPonDegradationAlarmSet.setStatus(
        "current"
    )

adGenGponOntClrDyingGaspAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 45)
)
adGenGponOntClrDyingGaspAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntAlarmSlotDyingGaspLevel"))
)
if mibBuilder.loadTexts:
    adGenGponOntClrDyingGaspAlarm.setStatus(
        "current"
    )

adGenGponOntSetDyingGaspAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 1, 0, 46)
)
adGenGponOntSetDyingGaspAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENGPON-MIB", "adGenGponOntAlarmSlotDyingGaspLevel"))
)
if mibBuilder.loadTexts:
    adGenGponOntSetDyingGaspAlarm.setStatus(
        "current"
    )

adGenGponOntClrLanLOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2, 0, 1)
)
adGenGponOntClrLanLOSAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntClrLanLOSAlarm.setStatus(
        "current"
    )

adGenGponOntPortSetLanLOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2, 0, 2)
)
adGenGponOntPortSetLanLOSAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntPortSetLanLOSAlarm.setStatus(
        "current"
    )

adGenGponOntVideoPortLOSAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2, 0, 3)
)
adGenGponOntVideoPortLOSAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntVideoPortLOSAlarmClear.setStatus(
        "current"
    )

adGenGponOntVideoPortLOSAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2, 0, 4)
)
adGenGponOntVideoPortLOSAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntVideoPortLOSAlarmSet.setStatus(
        "current"
    )

adGenGponOntVideoPortOORLowAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2, 0, 5)
)
adGenGponOntVideoPortOORLowAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntVideoPortOORLowAlarmClear.setStatus(
        "current"
    )

adGenGponOntVideoPortOORLowAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2, 0, 6)
)
adGenGponOntVideoPortOORLowAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntVideoPortOORLowAlarmSet.setStatus(
        "current"
    )

adGenGponOntVideoPortOORHighAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2, 0, 7)
)
adGenGponOntVideoPortOORHighAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntVideoPortOORHighAlarmClear.setStatus(
        "current"
    )

adGenGponOntVideoPortOORHighAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1, 1, 5, 2, 0, 8)
)
adGenGponOntVideoPortOORHighAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenGponOntVideoPortOORHighAlarmSet.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENGPON-MIB",
    **{"AdGenGponEnableDisableValue": AdGenGponEnableDisableValue,
       "AdGenGponTrueFalseValue": AdGenGponTrueFalseValue,
       "AdGenGponYesNoValue": AdGenGponYesNoValue,
       "AdGenGponOntAdminState": AdGenGponOntAdminState,
       "AdGenGponOntOperState": AdGenGponOntOperState,
       "AdGenGponOntPortOperState": AdGenGponOntPortOperState,
       "AdGenGponOntPortAutoDetectMode": AdGenGponOntPortAutoDetectMode,
       "AdGenGponActivationMode": AdGenGponActivationMode,
       "AdGenGponConfigFileRetrievalMethod": AdGenGponConfigFileRetrievalMethod,
       "AdGenGponConfigFileState": AdGenGponConfigFileState,
       "AdGenGponConfigFileInterface": AdGenGponConfigFileInterface,
       "AdGenGponOntVideoPortReturnPathMode": AdGenGponOntVideoPortReturnPathMode,
       "AdGenGponResourceAllocationMode": AdGenGponResourceAllocationMode,
       "AdGenGponMulticastCacStatus": AdGenGponMulticastCacStatus,
       "adGenGponMIB": adGenGponMIB,
       "adGponConfiguration": adGponConfiguration,
       "adGenGponOltConfigTable": adGenGponOltConfigTable,
       "adGenGponOltConfigEntry": adGenGponOltConfigEntry,
       "adGenGponOltSystemUpTime": adGenGponOltSystemUpTime,
       "adGenGponOltOntSwVersionOnFlash": adGenGponOltOntSwVersionOnFlash,
       "adGenGponOltOntBootCodeSwVersionOnFlash": adGenGponOltOntBootCodeSwVersionOnFlash,
       "adGenGponOltMaxOntsPerPon": adGenGponOltMaxOntsPerPon,
       "adGenGponOltNumPons": adGenGponOltNumPons,
       "adGenGponOltOntSwOnFlashGlbFilename": adGenGponOltOntSwOnFlashGlbFilename,
       "adGponProvisioning": adGponProvisioning,
       "adGenGponOltProvTable": adGenGponOltProvTable,
       "adGenGponOltProvEntry": adGenGponOltProvEntry,
       "adGenGponOltStagTpid": adGenGponOltStagTpid,
       "adGenGponOltCtagTpid": adGenGponOltCtagTpid,
       "adGenGponOltGponClock": adGenGponOltGponClock,
       "adGenGponOltBackplaneNegSpeed": adGenGponOltBackplaneNegSpeed,
       "adGenGponOltBipTcaThreshold": adGenGponOltBipTcaThreshold,
       "adGenGponProtection": adGenGponProtection,
       "adGenGponOntAlarmSlotLosEnable": adGenGponOntAlarmSlotLosEnable,
       "adGenGponOntAlarmSlotLosLevel": adGenGponOntAlarmSlotLosLevel,
       "adGenGponOntAlarmSlotPoweringEnable": adGenGponOntAlarmSlotPoweringEnable,
       "adGenGponOntAlarmSlotPoweringLevel": adGenGponOntAlarmSlotPoweringLevel,
       "adGenGponOntAlarmSlotDyingGaspEnable": adGenGponOntAlarmSlotDyingGaspEnable,
       "adGenGponOntAlarmSlotDyingGaspLevel": adGenGponOntAlarmSlotDyingGaspLevel,
       "adGenGponPonProvTable": adGenGponPonProvTable,
       "adGenGponPonProvEntry": adGenGponPonProvEntry,
       "adGenGponPonDownstreamFec": adGenGponPonDownstreamFec,
       "adGenGponPonAutoDiscoveryMode": adGenGponPonAutoDiscoveryMode,
       "adGenGponPonAutoOntActivateMode": adGenGponPonAutoOntActivateMode,
       "adGenGponPonOntSoftwareDownloadFlag": adGenGponPonOntSoftwareDownloadFlag,
       "adGenGponPonRediscoverFlag": adGenGponPonRediscoverFlag,
       "adGenGponOntLastCreateError": adGenGponOntLastCreateError,
       "adGenGponPonDeploymentRange": adGenGponPonDeploymentRange,
       "adGenGponPonActivationMode": adGenGponPonActivationMode,
       "adGenGponPonResourceAllocationMode": adGenGponPonResourceAllocationMode,
       "adGenGponPonLosActiveThreshold": adGenGponPonLosActiveThreshold,
       "adGenGponPonMulticastBwThreshold": adGenGponPonMulticastBwThreshold,
       "adGenGponPonMulticastCac": adGenGponPonMulticastCac,
       "adGenGponPonDownstreamTotalMinRate": adGenGponPonDownstreamTotalMinRate,
       "adGenGponPonUpstreamFec": adGenGponPonUpstreamFec,
       "adGenGponPonDescriptionString": adGenGponPonDescriptionString,
       "adGenGponPonTechnologyMode": adGenGponPonTechnologyMode,
       "adGenGponOntProvTable": adGenGponOntProvTable,
       "adGenGponOntProvEntry": adGenGponOntProvEntry,
       "adGenGponOntSerialNumber": adGenGponOntSerialNumber,
       "adGenGponOntDescriptionString": adGenGponOntDescriptionString,
       "adGenGponOntBatteryBackup": adGenGponOntBatteryBackup,
       "adGenGponOntAdminState": adGenGponOntAdminState,
       "adGenGponOntAesMode": adGenGponOntAesMode,
       "adGenGponOntSecurityMode": adGenGponOntSecurityMode,
       "adGenGponOntSoftwareVersion": adGenGponOntSoftwareVersion,
       "adGenGponOntGr303VoiceMacAddress": adGenGponOntGr303VoiceMacAddress,
       "adGenGponOntUpstreamFixedBandwidth": adGenGponOntUpstreamFixedBandwidth,
       "adGenGponOntUpstreamAssuredBandwidth": adGenGponOntUpstreamAssuredBandwidth,
       "adGenGponOntUpstreamBestEffortBandwidth": adGenGponOntUpstreamBestEffortBandwidth,
       "adGenGponOntUpstreamNonAssuredBandwidth": adGenGponOntUpstreamNonAssuredBandwidth,
       "adGenGponOntPotsServiceMode": adGenGponOntPotsServiceMode,
       "adGenGponOntLastError": adGenGponOntLastError,
       "adGenGponOntRowStatus": adGenGponOntRowStatus,
       "adGenGponOntPortLastCreateError": adGenGponOntPortLastCreateError,
       "adGenGponOntRegistrationId": adGenGponOntRegistrationId,
       "adGenGponOntBootCodeSoftwareVersion": adGenGponOntBootCodeSoftwareVersion,
       "adGenGponConfigFileRetrievalMethod": adGenGponConfigFileRetrievalMethod,
       "adGenGponConfigFilePrimaryServer": adGenGponConfigFilePrimaryServer,
       "adGenGponConfigFileSecondaryServer": adGenGponConfigFileSecondaryServer,
       "adGenGponConfigFileInterface": adGenGponConfigFileInterface,
       "adGenGponConfigFilePath": adGenGponConfigFilePath,
       "adGenGponConfigFileRetrieve": adGenGponConfigFileRetrieve,
       "adGenGponMacSpoofingAllowed": adGenGponMacSpoofingAllowed,
       "adGenGponAcsServerProfile": adGenGponAcsServerProfile,
       "adGenGponOntVoIPConfigMethod": adGenGponOntVoIPConfigMethod,
       "adGenGponOntVectoringEnable": adGenGponOntVectoringEnable,
       "adGenGponOntSoftwareDownloadOnly": adGenGponOntSoftwareDownloadOnly,
       "adGenGponOntSoftwareActivate": adGenGponOntSoftwareActivate,
       "adGenGponOntCpuRateLimitCountersClear": adGenGponOntCpuRateLimitCountersClear,
       "adGenGponOntPortProvTable": adGenGponOntPortProvTable,
       "adGenGponOntPortProvEntry": adGenGponOntPortProvEntry,
       "adGenGponOntPortAdminState": adGenGponOntPortAdminState,
       "adGenGponOntPortAutoDetectionConfiguration": adGenGponOntPortAutoDetectionConfiguration,
       "adGenGponOntPortBridgeIdorIpInd": adGenGponOntPortBridgeIdorIpInd,
       "adGenGponOntPortEthLoopbackConfiguration": adGenGponOntPortEthLoopbackConfiguration,
       "adGenGponOntPortMaxFrameSize": adGenGponOntPortMaxFrameSize,
       "adGenGponOntPortDteOrDceInd": adGenGponOntPortDteOrDceInd,
       "adGenGponOntPortPauseTime": adGenGponOntPortPauseTime,
       "adGenGponOntPortPPPoEFilter": adGenGponOntPortPPPoEFilter,
       "adGenGponOntPortPowerControl": adGenGponOntPortPowerControl,
       "adGenGponOntPortImpedance": adGenGponOntPortImpedance,
       "adGenGponOntPortTransmissionPath": adGenGponOntPortTransmissionPath,
       "adGenGponOntPortRxGain": adGenGponOntPortRxGain,
       "adGenGponOntPortTxGain": adGenGponOntPortTxGain,
       "adGenGponOntPortPotsHoldoverTime": adGenGponOntPortPotsHoldoverTime,
       "adGenGponOntPortPreprovIndicationFlag": adGenGponOntPortPreprovIndicationFlag,
       "adGenGponOntPortLastError": adGenGponOntPortLastError,
       "adGenGponOntPortRowStatus": adGenGponOntPortRowStatus,
       "adGenGponOntPortOmciEthProvPrelimCheck": adGenGponOntPortOmciEthProvPrelimCheck,
       "adGenGponOntVideoPortEnableLOSAlarm": adGenGponOntVideoPortEnableLOSAlarm,
       "adGenGponOntVideoPortEnableOORLowAlarm": adGenGponOntVideoPortEnableOORLowAlarm,
       "adGenGponOntVideoPortEnableOORHighAlarm": adGenGponOntVideoPortEnableOORHighAlarm,
       "adGenGponOntVideoPortReturnPathMode": adGenGponOntVideoPortReturnPathMode,
       "adGenGponOntVideoPortReturnPathFrequency": adGenGponOntVideoPortReturnPathFrequency,
       "adGenGponOntVideoPortReturnPathDestinationIPAddress": adGenGponOntVideoPortReturnPathDestinationIPAddress,
       "adGenGponOntVideoPortReturnPathDestinationUDPPort": adGenGponOntVideoPortReturnPathDestinationUDPPort,
       "adGenGponOntVideoPortReturnPathSourceUDPPort": adGenGponOntVideoPortReturnPathSourceUDPPort,
       "adGenGponOntPortDescriptionString": adGenGponOntPortDescriptionString,
       "adGenGponOntPortMapVEIPIfIndex": adGenGponOntPortMapVEIPIfIndex,
       "adGenGponOntPortMapBridgeGroupIfIndex": adGenGponOntPortMapBridgeGroupIfIndex,
       "adGenGponOntPortBridgeGroupAgingTime": adGenGponOntPortBridgeGroupAgingTime,
       "adGenGponOntPortBridgeGroupLearningLimit": adGenGponOntPortBridgeGroupLearningLimit,
       "adGenGponOntPortBondingPeer": adGenGponOntPortBondingPeer,
       "adGenGponOntPortExtendedFeatureProvTable": adGenGponOntPortExtendedFeatureProvTable,
       "adGenGponOntPortExtendedFeatureProvEntry": adGenGponOntPortExtendedFeatureProvEntry,
       "adGenGponOntPortArc": adGenGponOntPortArc,
       "adGenGponOntPortArcInterval": adGenGponOntPortArcInterval,
       "adGenGponOntPortSfThreshold": adGenGponOntPortSfThreshold,
       "adGenGponOntPortSdThreshold": adGenGponOntPortSdThreshold,
       "adGenGponOntPortLowerOpticalThreshold": adGenGponOntPortLowerOpticalThreshold,
       "adGenGponOntPortUpperOpticalThreshold": adGenGponOntPortUpperOpticalThreshold,
       "adGenGponOntPortGr303signalingCodeMode": adGenGponOntPortGr303signalingCodeMode,
       "adGenGponOntPortGr303LineLoopBack": adGenGponOntPortGr303LineLoopBack,
       "adGenGponOntPortGr303PayloadLoopBack": adGenGponOntPortGr303PayloadLoopBack,
       "adGenGponOntPortGr303VoiceIpAddress": adGenGponOntPortGr303VoiceIpAddress,
       "adGenGponPonDiscoveredOntSnTable": adGenGponPonDiscoveredOntSnTable,
       "adGenGponPonDiscoveredOntSnEntry": adGenGponPonDiscoveredOntSnEntry,
       "adGenGponPonDiscoveredOntSerialNumberIndex": adGenGponPonDiscoveredOntSerialNumberIndex,
       "adGenGponPonDiscoveredOntSerialNumber": adGenGponPonDiscoveredOntSerialNumber,
       "adGenGponPonDiscoveredRegistrationId": adGenGponPonDiscoveredRegistrationId,
       "adGponStatus": adGponStatus,
       "adGenGponOntStatusTable": adGenGponOntStatusTable,
       "adGenGponOntStatusEntry": adGenGponOntStatusEntry,
       "adGenGponOntNumber": adGenGponOntNumber,
       "adGenGponOntTrafficManagementOption": adGenGponOntTrafficManagementOption,
       "adGenGponOntOmccVersion": adGenGponOntOmccVersion,
       "adGenGponOntMode": adGenGponOntMode,
       "adGenGponOntEquipmentID": adGenGponOntEquipmentID,
       "adGenGponOntUpTime": adGenGponOntUpTime,
       "adGenGponOntOperState": adGenGponOntOperState,
       "adGenGponOntSoftwareDownloadStatus": adGenGponOntSoftwareDownloadStatus,
       "adGenGponOntSoftwareDownloadProgress": adGenGponOntSoftwareDownloadProgress,
       "adGenGponOntActiveSoftwareVersion": adGenGponOntActiveSoftwareVersion,
       "adGenGponOntCurrentAvailableUpstreamBandwidth": adGenGponOntCurrentAvailableUpstreamBandwidth,
       "adGenGponOntPartNumber": adGenGponOntPartNumber,
       "adGenGponOntHardwareRevision": adGenGponOntHardwareRevision,
       "adGenGponOntCurrentAvailableDownstreamBandwidth": adGenGponOntCurrentAvailableDownstreamBandwidth,
       "adGenGponOntLearnedSerialNumber": adGenGponOntLearnedSerialNumber,
       "adGenGponOntRssi": adGenGponOntRssi,
       "adGenGponAvailableVOIPConfigMethods": adGenGponAvailableVOIPConfigMethods,
       "adGenGponConfigFileState": adGenGponConfigFileState,
       "adGenGponConfigFileChecksum": adGenGponConfigFileChecksum,
       "adGenGponConfigErrorString": adGenGponConfigErrorString,
       "adGenGponOntUpstreamBIPError": adGenGponOntUpstreamBIPError,
       "adGenGponOntDownstreamBIPError": adGenGponOntDownstreamBIPError,
       "adGenGponOntUpstreamGoodDBRuCounter": adGenGponOntUpstreamGoodDBRuCounter,
       "adGenGponOntUpstreamBadDBRuCounter": adGenGponOntUpstreamBadDBRuCounter,
       "adGenGponAcsServerProfileUserName": adGenGponAcsServerProfileUserName,
       "adGenGponAcsServerProfilePassword": adGenGponAcsServerProfilePassword,
       "adGenGponOntFeatureSupport": adGenGponOntFeatureSupport,
       "adGenGponOntInactiveSoftwareVersion": adGenGponOntInactiveSoftwareVersion,
       "adGenGponOntManagementMacAddress": adGenGponOntManagementMacAddress,
       "adGenGponOntFiberLength": adGenGponOntFiberLength,
       "adGenGponOntEqualizationDelay": adGenGponOntEqualizationDelay,
       "adGenGponOntRxPower": adGenGponOntRxPower,
       "adGenGponOntTxPower": adGenGponOntTxPower,
       "adGenGponOntProductName": adGenGponOntProductName,
       "adGenGponOntEverActivated": adGenGponOntEverActivated,
       "adGenGponOntTemperature": adGenGponOntTemperature,
       "adGenGponOntBiasCurrent": adGenGponOntBiasCurrent,
       "adGenGponOntVoltage": adGenGponOntVoltage,
       "adGenGponOntUsFecProcessedCodewords": adGenGponOntUsFecProcessedCodewords,
       "adGenGponOntUsFecCorrectedCodewords": adGenGponOntUsFecCorrectedCodewords,
       "adGenGponOntUsFecCorrectedCodebytes": adGenGponOntUsFecCorrectedCodebytes,
       "adGenGponOntUsFecUncorrectedCodewords": adGenGponOntUsFecUncorrectedCodewords,
       "adGenGponGalEthDiscardedFrames": adGenGponGalEthDiscardedFrames,
       "adGenGponOntPortStatusTable": adGenGponOntPortStatusTable,
       "adGenGponOntPortStatusEntry": adGenGponOntPortStatusEntry,
       "adGenGponOntPortNumber": adGenGponOntPortNumber,
       "adGenGponOntPortSrIndication": adGenGponOntPortSrIndication,
       "adGenGponOntPortPiggybackDbaReporting": adGenGponOntPortPiggybackDbaReporting,
       "adGenGponOntPortWholeOnuDbaReporting": adGenGponOntPortWholeOnuDbaReporting,
       "adGenGponOntPortOpticalSignalLevel": adGenGponOntPortOpticalSignalLevel,
       "adGenGponOntPortType": adGenGponOntPortType,
       "adGenGponOntPortConfigurationInd": adGenGponOntPortConfigurationInd,
       "adGenGponOntPortMaxGemPayloadSize": adGenGponOntPortMaxGemPayloadSize,
       "adGenGponOntPortHookState": adGenGponOntPortHookState,
       "adGenGponOntPortOperState": adGenGponOntPortOperState,
       "adGenGponOntPortGemBlockLength": adGenGponOntPortGemBlockLength,
       "adGenGponOntPortGr303CrvPortNumber": adGenGponOntPortGr303CrvPortNumber,
       "adGenGponOntPortRFSignalLevel": adGenGponOntPortRFSignalLevel,
       "adGenGponOntPortRFOpticalSignalLevel": adGenGponOntPortRFOpticalSignalLevel,
       "adGenGponOntPortErrorString": adGenGponOntPortErrorString,
       "adGenGponOntPortConnectToVEIP": adGenGponOntPortConnectToVEIP,
       "adGenGponOntPortConnectToBridgeGroup": adGenGponOntPortConnectToBridgeGroup,
       "adGenGponOntInventoryInfoTable": adGenGponOntInventoryInfoTable,
       "adGenGponOntInventoryInfoEntry": adGenGponOntInventoryInfoEntry,
       "adGenGponOntSupportedType": adGenGponOntSupportedType,
       "adGenGponOntMaxPortsPerType": adGenGponOntMaxPortsPerType,
       "adGenGponPonStatusTable": adGenGponPonStatusTable,
       "adGenGponPonStatusEntry": adGenGponPonStatusEntry,
       "adGenGponPonOntSoftwareDownloadInProgress": adGenGponPonOntSoftwareDownloadInProgress,
       "adGenGponPonConfiguredOnts": adGenGponPonConfiguredOnts,
       "adGenGponPonDiscoveringOnts": adGenGponPonDiscoveringOnts,
       "adGenGponPonUnrecognizedOnts": adGenGponPonUnrecognizedOnts,
       "adGenGponPonOperationallyUpOnts": adGenGponPonOperationallyUpOnts,
       "adGenGponPonAvailableUpstreamBandwidth": adGenGponPonAvailableUpstreamBandwidth,
       "adGenGponPonAvailableDownstreamBandwidth": adGenGponPonAvailableDownstreamBandwidth,
       "adGenGponPonLongestFiberDistance": adGenGponPonLongestFiberDistance,
       "adGenGponPonShortestFiberDistance": adGenGponPonShortestFiberDistance,
       "adGenGponPonNearestOnt": adGenGponPonNearestOnt,
       "adGenGponPonFarthestOnt": adGenGponPonFarthestOnt,
       "adGenGponPonTotalProvDownstreamBandwidth": adGenGponPonTotalProvDownstreamBandwidth,
       "adGenGponPonTotalProvUpstreamBandwidth": adGenGponPonTotalProvUpstreamBandwidth,
       "adGenGponPonTotalProvFixedAssuredBandwidth": adGenGponPonTotalProvFixedAssuredBandwidth,
       "adGenGponPonNextAvailableOntId": adGenGponPonNextAvailableOntId,
       "adGenGponPonAvailableFixedAssuredBandwidth": adGenGponPonAvailableFixedAssuredBandwidth,
       "adGenGponPonCurrDownstreamBandwidth": adGenGponPonCurrDownstreamBandwidth,
       "adGenGponPonCurrUpstreamBandwidth": adGenGponPonCurrUpstreamBandwidth,
       "adGenGponPonCurrFixedAssuredBandwidth": adGenGponPonCurrFixedAssuredBandwidth,
       "adGenGponPonTotalProvFixedBandwidth": adGenGponPonTotalProvFixedBandwidth,
       "adGenGponPonTotalProvAssuredBandwidth": adGenGponPonTotalProvAssuredBandwidth,
       "adGenGponPonMaxOnts": adGenGponPonMaxOnts,
       "adGenGponPonMaxServicesPerOnt": adGenGponPonMaxServicesPerOnt,
       "adGenGponPonLosNumOntsDown": adGenGponPonLosNumOntsDown,
       "adGenGponPonMulticastCacStatus": adGenGponPonMulticastCacStatus,
       "adGenGponPonDownstreamAvailableMinRate": adGenGponPonDownstreamAvailableMinRate,
       "adGenGponPonDownstreamCurrentMinRate": adGenGponPonDownstreamCurrentMinRate,
       "adGenGponPonTechnology": adGenGponPonTechnology,
       "adGenGponPonWavelength": adGenGponPonWavelength,
       "adGponPerformance": adGponPerformance,
       "adGenGponPon15MinPMTable": adGenGponPon15MinPMTable,
       "adGenGponPon15MinPMEntry": adGenGponPon15MinPMEntry,
       "adGenGponPon15MinPMIntervalNumber": adGenGponPon15MinPMIntervalNumber,
       "adGenGponPon15MinRxEthernetPackets": adGenGponPon15MinRxEthernetPackets,
       "adGenGponPon15MinRxOMCIPackets": adGenGponPon15MinRxOMCIPackets,
       "adGenGponPon15MinTxEthernetPackets": adGenGponPon15MinTxEthernetPackets,
       "adGenGponPon15MinTxOMCIPackets": adGenGponPon15MinTxOMCIPackets,
       "adGenGponPon15MinUpstreamBIPError": adGenGponPon15MinUpstreamBIPError,
       "adGenGponPon15MinUpstreamDroppedPackets": adGenGponPon15MinUpstreamDroppedPackets,
       "adGenGponPon15MinBufferOverflow": adGenGponPon15MinBufferOverflow,
       "adGenGponPon15MinPacketFragError": adGenGponPon15MinPacketFragError,
       "adGenGponPon15MinIntervalTimeStamp": adGenGponPon15MinIntervalTimeStamp,
       "adGenGponPon15MinRxEthernetBytes": adGenGponPon15MinRxEthernetBytes,
       "adGenGponPon15MinTxEthernetBytes": adGenGponPon15MinTxEthernetBytes,
       "adGenGponPon15MinUsBwAverageUtil": adGenGponPon15MinUsBwAverageUtil,
       "adGenGponPon15MinUsBwPeakUtil": adGenGponPon15MinUsBwPeakUtil,
       "adGenGponPon15MinDsBwAverageUtil": adGenGponPon15MinDsBwAverageUtil,
       "adGenGponPon15MinDsBwPeakUtil": adGenGponPon15MinDsBwPeakUtil,
       "adGenGponPon15MinDsMulticastPackets": adGenGponPon15MinDsMulticastPackets,
       "adGenGponPon15MinDsMulticastBytes": adGenGponPon15MinDsMulticastBytes,
       "adGenGponPon15MinDsMulticastBwAverageUtil": adGenGponPon15MinDsMulticastBwAverageUtil,
       "adGenGponPon15MinDsMulticastBwPeakUtil": adGenGponPon15MinDsMulticastBwPeakUtil,
       "adGenGponPon15MinDownstreamBIPError": adGenGponPon15MinDownstreamBIPError,
       "adGenGponPon24HrPMTable": adGenGponPon24HrPMTable,
       "adGenGponPon24HrPMEntry": adGenGponPon24HrPMEntry,
       "adGenGponPon24HrPMIntervalNumber": adGenGponPon24HrPMIntervalNumber,
       "adGenGponPon24HrRxEthernetPackets": adGenGponPon24HrRxEthernetPackets,
       "adGenGponPon24HrRxOMCIPackets": adGenGponPon24HrRxOMCIPackets,
       "adGenGponPon24HrTxEthernetPackets": adGenGponPon24HrTxEthernetPackets,
       "adGenGponPon24HrTxOMCIPackets": adGenGponPon24HrTxOMCIPackets,
       "adGenGponPon24HrUpstreamBIPError": adGenGponPon24HrUpstreamBIPError,
       "adGenGponPon24HrUpstreamDroppedPackets": adGenGponPon24HrUpstreamDroppedPackets,
       "adGenGponPon24HrBufferOverflow": adGenGponPon24HrBufferOverflow,
       "adGenGponPon24HrPacketFragError": adGenGponPon24HrPacketFragError,
       "adGenGponPon24HrIntervalTimeStamp": adGenGponPon24HrIntervalTimeStamp,
       "adGenGponPon24HrRxEthernetBytes": adGenGponPon24HrRxEthernetBytes,
       "adGenGponPon24HrTxEthernetBytes": adGenGponPon24HrTxEthernetBytes,
       "adGenGponPon24HrUsBwAverageUtil": adGenGponPon24HrUsBwAverageUtil,
       "adGenGponPon24HrUsBwPeakUtil": adGenGponPon24HrUsBwPeakUtil,
       "adGenGponPon24HrDsBwAverageUtil": adGenGponPon24HrDsBwAverageUtil,
       "adGenGponPon24HrDsBwPeakUtil": adGenGponPon24HrDsBwPeakUtil,
       "adGenGponPon24HrDsMulticastPackets": adGenGponPon24HrDsMulticastPackets,
       "adGenGponPon24HrDsMulticastBytes": adGenGponPon24HrDsMulticastBytes,
       "adGenGponPon24HrDsMulticastBwAverageUtil": adGenGponPon24HrDsMulticastBwAverageUtil,
       "adGenGponPon24HrDsMulticastBwPeakUtil": adGenGponPon24HrDsMulticastBwPeakUtil,
       "adGenGponPon24HrDownstreamBIPError": adGenGponPon24HrDownstreamBIPError,
       "adGenGponPonCurrent15MinPMTable": adGenGponPonCurrent15MinPMTable,
       "adGenGponPonCurrent15MinPMEntry": adGenGponPonCurrent15MinPMEntry,
       "adGenGponPonRxEthernetPacketsCurrent15Min": adGenGponPonRxEthernetPacketsCurrent15Min,
       "adGenGponPonRxOMCIPacketsCurrent15Min": adGenGponPonRxOMCIPacketsCurrent15Min,
       "adGenGponPonTxEthernetPacketsCurrent15Min": adGenGponPonTxEthernetPacketsCurrent15Min,
       "adGenGponPonTxOMCIPacketsCurrent15Min": adGenGponPonTxOMCIPacketsCurrent15Min,
       "adGenGponPonUpstreamBIPErrorCurrent15Min": adGenGponPonUpstreamBIPErrorCurrent15Min,
       "adGenGponPonUpstreamDroppedPacketsCurrent15Min": adGenGponPonUpstreamDroppedPacketsCurrent15Min,
       "adGenGponPonBufferOverflowCurrent15Min": adGenGponPonBufferOverflowCurrent15Min,
       "adGenGponPonPacketFragErrorCurrent15Min": adGenGponPonPacketFragErrorCurrent15Min,
       "adGenGponPonRxEthernetBytesCurrent15Min": adGenGponPonRxEthernetBytesCurrent15Min,
       "adGenGponPonTxEthernetBytesCurrent15Min": adGenGponPonTxEthernetBytesCurrent15Min,
       "adGenGponPonUsBwAverageUtilCurrent15Min": adGenGponPonUsBwAverageUtilCurrent15Min,
       "adGenGponPonUsBwPeakUtilCurrent15Min": adGenGponPonUsBwPeakUtilCurrent15Min,
       "adGenGponPonDsBwAverageUtilCurrent15Min": adGenGponPonDsBwAverageUtilCurrent15Min,
       "adGenGponPonDsBwPeakUtilCurrent15Min": adGenGponPonDsBwPeakUtilCurrent15Min,
       "adGenGponPonDsMulticastPacketsCurrent15Min": adGenGponPonDsMulticastPacketsCurrent15Min,
       "adGenGponPonDsMulticastBytesCurrent15Min": adGenGponPonDsMulticastBytesCurrent15Min,
       "adGenGponPonDsMulticastBwAverageUtilCurrent15Min": adGenGponPonDsMulticastBwAverageUtilCurrent15Min,
       "adGenGponPonDsMulticastBwPeakUtilCurrent15Min": adGenGponPonDsMulticastBwPeakUtilCurrent15Min,
       "adGenGponPonDownstreamBIPErrorCurrent15Min": adGenGponPonDownstreamBIPErrorCurrent15Min,
       "adGenGponPonCurrent24HrPMTable": adGenGponPonCurrent24HrPMTable,
       "adGenGponPonCurrent24HrPMEntry": adGenGponPonCurrent24HrPMEntry,
       "adGenGponPonRxEthernetPacketsCurrent24Hr": adGenGponPonRxEthernetPacketsCurrent24Hr,
       "adGenGponPonRxOMCIPacketsCurrent24Hr": adGenGponPonRxOMCIPacketsCurrent24Hr,
       "adGenGponPonTxEthernetPacketsCurrent24Hr": adGenGponPonTxEthernetPacketsCurrent24Hr,
       "adGenGponPonTxOMCIPacketsCurrent24Hr": adGenGponPonTxOMCIPacketsCurrent24Hr,
       "adGenGponPonUpstreamBIPErrorCurrent24Hr": adGenGponPonUpstreamBIPErrorCurrent24Hr,
       "adGenGponPonUpstreamDroppedPacketsCurrent24Hr": adGenGponPonUpstreamDroppedPacketsCurrent24Hr,
       "adGenGponPonBufferOverflowCurrent24Hr": adGenGponPonBufferOverflowCurrent24Hr,
       "adGenGponPonPacketFragErrorCurrent24Hr": adGenGponPonPacketFragErrorCurrent24Hr,
       "adGenGponPonRxEthernetBytesCurrent24Hr": adGenGponPonRxEthernetBytesCurrent24Hr,
       "adGenGponPonTxEthernetBytesCurrent24Hr": adGenGponPonTxEthernetBytesCurrent24Hr,
       "adGenGponPonUsBwAverageUtilCurrent24Hr": adGenGponPonUsBwAverageUtilCurrent24Hr,
       "adGenGponPonUsBwPeakUtilCurrent24Hr": adGenGponPonUsBwPeakUtilCurrent24Hr,
       "adGenGponPonDsBwAverageUtilCurrent24Hr": adGenGponPonDsBwAverageUtilCurrent24Hr,
       "adGenGponPonDsBwPeakUtilCurrent24Hr": adGenGponPonDsBwPeakUtilCurrent24Hr,
       "adGenGponPonDsMulticastPacketsCurrent24Hr": adGenGponPonDsMulticastPacketsCurrent24Hr,
       "adGenGponPonDsMulticastBytesCurrent24Hr": adGenGponPonDsMulticastBytesCurrent24Hr,
       "adGenGponPonDsMulticastBwAverageUtilCurrent24Hr": adGenGponPonDsMulticastBwAverageUtilCurrent24Hr,
       "adGenGponPonDsMulticastBwPeakUtilCurrent24Hr": adGenGponPonDsMulticastBwPeakUtilCurrent24Hr,
       "adGenGponPonDownstreamBIPErrorCurrent24Hr": adGenGponPonDownstreamBIPErrorCurrent24Hr,
       "adGenGponPonPerfResetTable": adGenGponPonPerfResetTable,
       "adGenGponPonPerfResetEntry": adGenGponPonPerfResetEntry,
       "adGenGponPonPerfReset": adGenGponPonPerfReset,
       "adGenGponOntVideoReturnPathCountersResetTable": adGenGponOntVideoReturnPathCountersResetTable,
       "adGenGponOntVideoReturnPathCountersResetEntry": adGenGponOntVideoReturnPathCountersResetEntry,
       "adGenGponOntVideoReturnPathCountersReset": adGenGponOntVideoReturnPathCountersReset,
       "adGenGponOntVideoReturnPathCountersTable": adGenGponOntVideoReturnPathCountersTable,
       "adGenGponOntVideoReturnPathCountersEntry": adGenGponOntVideoReturnPathCountersEntry,
       "adGenGponOntVideoReturnPathRxTotalBursts": adGenGponOntVideoReturnPathRxTotalBursts,
       "adGenGponOntVideoReturnPathRxGoodBursts": adGenGponOntVideoReturnPathRxGoodBursts,
       "adGenGponOntVideoReturnPathRxFECCorrectedBursts": adGenGponOntVideoReturnPathRxFECCorrectedBursts,
       "adGenGponOntVideoReturnPathRxMissedBursts": adGenGponOntVideoReturnPathRxMissedBursts,
       "adGenGponOntVideoReturnPathRxMinPower": adGenGponOntVideoReturnPathRxMinPower,
       "adGenGponOntVideoReturnPathRxMaxPower": adGenGponOntVideoReturnPathRxMaxPower,
       "adGenGponOntVideoReturnPathRxCurrentPower": adGenGponOntVideoReturnPathRxCurrentPower,
       "adGenGponOntVideoReturnPathRxFECCorrectedSymbols": adGenGponOntVideoReturnPathRxFECCorrectedSymbols,
       "adGenGponPonCounterResetTable": adGenGponPonCounterResetTable,
       "adGenGponPonCounterResetEntry": adGenGponPonCounterResetEntry,
       "adGenGponPonBIPCountersReset": adGenGponPonBIPCountersReset,
       "adGponAlarms": adGponAlarms,
       "adGponOntAlarmEventsPrefix": adGponOntAlarmEventsPrefix,
       "adGponOntAlarmEvents": adGponOntAlarmEvents,
       "adGenGponOntClrLOSAlarm": adGenGponOntClrLOSAlarm,
       "adGenGponOntSetLOSAlarm": adGenGponOntSetLOSAlarm,
       "adGenGponOntClrEquipmentAlarm": adGenGponOntClrEquipmentAlarm,
       "adGenGponOntSetEquipmentAlarm": adGenGponOntSetEquipmentAlarm,
       "adGenGponOntClrPoweringAlarm": adGenGponOntClrPoweringAlarm,
       "adGenGponOntSetPoweringAlarm": adGenGponOntSetPoweringAlarm,
       "adGenGponOntClrBatteryMissingAlarm": adGenGponOntClrBatteryMissingAlarm,
       "adGenGponOntSetBatteryMissingAlarm": adGenGponOntSetBatteryMissingAlarm,
       "adGenGponOntClrBatteryFailureAlarm": adGenGponOntClrBatteryFailureAlarm,
       "adGenGponOntSetBatteryFailureAlarm": adGenGponOntSetBatteryFailureAlarm,
       "adGenGponOntClrBatteryLowAlarm": adGenGponOntClrBatteryLowAlarm,
       "adGenGponOntSetBatteryLowAlarm": adGenGponOntSetBatteryLowAlarm,
       "adGenGponOntClrPhyIntrustionAlarm": adGenGponOntClrPhyIntrustionAlarm,
       "adGenGponOntSetPhyIntrusionAlarm": adGenGponOntSetPhyIntrusionAlarm,
       "adGenGponOntDiscoveryAlarm": adGenGponOntDiscoveryAlarm,
       "adGenGponOntActivationAlarm": adGenGponOntActivationAlarm,
       "adGenGponConfigServerAlarmClear": adGenGponConfigServerAlarmClear,
       "adGenGponConfigServerAlarmSet": adGenGponConfigServerAlarmSet,
       "adGenGponConfigFileAlarmClear": adGenGponConfigFileAlarmClear,
       "adGenGponConfigFileAlarmSet": adGenGponConfigFileAlarmSet,
       "adGenGponConfigChecksumMismatchAlarmClear": adGenGponConfigChecksumMismatchAlarmClear,
       "adGenGponConfigChecksumMismatchAlarmSet": adGenGponConfigChecksumMismatchAlarmSet,
       "adGenGponOntOMCICommFailAlarmClear": adGenGponOntOMCICommFailAlarmClear,
       "adGenGponOntOMCICommFailAlarmSet": adGenGponOntOMCICommFailAlarmSet,
       "adGenGponCirOversubscribedAlarmClear": adGenGponCirOversubscribedAlarmClear,
       "adGenGponCirOversubscribedAlarmSet": adGenGponCirOversubscribedAlarmSet,
       "adGenGponPonLosAlarmClear": adGenGponPonLosAlarmClear,
       "adGenGponPonLosAlarmSet": adGenGponPonLosAlarmSet,
       "adGenGponMulticastBwThresholdAlarmClear": adGenGponMulticastBwThresholdAlarmClear,
       "adGenGponMulticastBwThresholdAlarmSet": adGenGponMulticastBwThresholdAlarmSet,
       "adGenGponPonDiscoveredInvalidSNAlarm": adGenGponPonDiscoveredInvalidSNAlarm,
       "adGenGponOntInvalidSNAlarm": adGenGponOntInvalidSNAlarm,
       "adGenGponOntUpstreamBipTcaAlarmClear": adGenGponOntUpstreamBipTcaAlarmClear,
       "adGenGponOntUpstreamBipTcaAlarmSet": adGenGponOntUpstreamBipTcaAlarmSet,
       "adGenGponOntDownstreamBipTcaAlarmClear": adGenGponOntDownstreamBipTcaAlarmClear,
       "adGenGponOntDownstreamBipTcaAlarmSet": adGenGponOntDownstreamBipTcaAlarmSet,
       "adGenGponOntDyingGaspAlarm": adGenGponOntDyingGaspAlarm,
       "adGenGponPonFailoverAlarmClear": adGenGponPonFailoverAlarmClear,
       "adGenGponPonFailoverAlarmActive": adGenGponPonFailoverAlarmActive,
       "adGenGponPonHwFailureAlarmClear": adGenGponPonHwFailureAlarmClear,
       "adGenGponPonHwFailureAlarmSet": adGenGponPonHwFailureAlarmSet,
       "adGenGponPonDegradationAlarmClear": adGenGponPonDegradationAlarmClear,
       "adGenGponPonDegradationAlarmSet": adGenGponPonDegradationAlarmSet,
       "adGenGponOntClrDyingGaspAlarm": adGenGponOntClrDyingGaspAlarm,
       "adGenGponOntSetDyingGaspAlarm": adGenGponOntSetDyingGaspAlarm,
       "adGponOntPortAlarmEventsPrefix": adGponOntPortAlarmEventsPrefix,
       "adGponOntPortAlarmEvents": adGponOntPortAlarmEvents,
       "adGenGponOntClrLanLOSAlarm": adGenGponOntClrLanLOSAlarm,
       "adGenGponOntPortSetLanLOSAlarm": adGenGponOntPortSetLanLOSAlarm,
       "adGenGponOntVideoPortLOSAlarmClear": adGenGponOntVideoPortLOSAlarmClear,
       "adGenGponOntVideoPortLOSAlarmSet": adGenGponOntVideoPortLOSAlarmSet,
       "adGenGponOntVideoPortOORLowAlarmClear": adGenGponOntVideoPortOORLowAlarmClear,
       "adGenGponOntVideoPortOORLowAlarmSet": adGenGponOntVideoPortOORLowAlarmSet,
       "adGenGponOntVideoPortOORHighAlarmClear": adGenGponOntVideoPortOORHighAlarmClear,
       "adGenGponOntVideoPortOORHighAlarmSet": adGenGponOntVideoPortOORHighAlarmSet,
       "adGponTests": adGponTests,
       "adGponOntTest": adGponOntTest,
       "adGenGponOntReset": adGenGponOntReset}
)
