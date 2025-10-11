# SNMP MIB module (ADTRAN-DSX1COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-DSX1COMMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:31 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotAlarmStatus,
 adGenSlotInfoIndex) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotAlarmStatus",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

(dsx1LineIndex,) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1LineIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfTotalCount,) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfTotalCount")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adDSX1commonModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 21)
)
if mibBuilder.loadTexts:
    adDSX1commonModuleIdentity.setRevisions(
        ("2014-04-28 00:00",
         "2011-08-30 00:00",
         "2011-07-08 00:00",
         "2011-07-07 00:00",
         "2007-10-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdDSX1Common_ObjectIdentity = ObjectIdentity
adDSX1Common = _AdDSX1Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21)
)
_AdDSX1CommonAlm_ObjectIdentity = ObjectIdentity
adDSX1CommonAlm = _AdDSX1CommonAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0)
)
_AdDSX1CommonProv_ObjectIdentity = ObjectIdentity
adDSX1CommonProv = _AdDSX1CommonProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1)
)
_AdDSX1CommonProvTable_Object = MibTable
adDSX1CommonProvTable = _AdDSX1CommonProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1)
)
if mibBuilder.loadTexts:
    adDSX1CommonProvTable.setStatus("current")
_AdDSX1CommonProvEntry_Object = MibTableRow
adDSX1CommonProvEntry = _AdDSX1CommonProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1)
)
adDSX1CommonProvEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonProvEntry.setStatus("current")


class _AdDSX1CommonProvLBO_Type(Integer32):
    """Custom type adDSX1CommonProvLBO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("lbo0", 1),
          ("lbo133", 2),
          ("lbo266", 3),
          ("lbo399", 4),
          ("lbo533", 5),
          ("db0", 6),
          ("dbneg7point5", 7),
          ("dbneg15", 8),
          ("dbneg22point5", 9))
    )


_AdDSX1CommonProvLBO_Type.__name__ = "Integer32"
_AdDSX1CommonProvLBO_Object = MibTableColumn
adDSX1CommonProvLBO = _AdDSX1CommonProvLBO_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 1),
    _AdDSX1CommonProvLBO_Type()
)
adDSX1CommonProvLBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvLBO.setStatus("current")


class _AdDSX1CommonProvFrame_Type(Integer32):
    """Custom type adDSX1CommonProvFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("slc96", 8),
          ("unframed", 9),
          ("notapplicable", 10))
    )


_AdDSX1CommonProvFrame_Type.__name__ = "Integer32"
_AdDSX1CommonProvFrame_Object = MibTableColumn
adDSX1CommonProvFrame = _AdDSX1CommonProvFrame_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 2),
    _AdDSX1CommonProvFrame_Type()
)
adDSX1CommonProvFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvFrame.setStatus("current")


class _AdDSX1CommonProvInbandLoopback_Type(Integer32):
    """Custom type adDSX1CommonProvInbandLoopback based on Integer32"""
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


_AdDSX1CommonProvInbandLoopback_Type.__name__ = "Integer32"
_AdDSX1CommonProvInbandLoopback_Object = MibTableColumn
adDSX1CommonProvInbandLoopback = _AdDSX1CommonProvInbandLoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 3),
    _AdDSX1CommonProvInbandLoopback_Type()
)
adDSX1CommonProvInbandLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvInbandLoopback.setStatus("current")


class _AdDSX1CommonProvBPVRatio_Type(Integer32):
    """Custom type adDSX1CommonProvBPVRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tenneg4", 1),
          ("tenneg5", 2),
          ("tenneg6", 3))
    )


_AdDSX1CommonProvBPVRatio_Type.__name__ = "Integer32"
_AdDSX1CommonProvBPVRatio_Object = MibTableColumn
adDSX1CommonProvBPVRatio = _AdDSX1CommonProvBPVRatio_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 4),
    _AdDSX1CommonProvBPVRatio_Type()
)
adDSX1CommonProvBPVRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvBPVRatio.setStatus("current")


class _AdDSX1CommonProvAutoFailoverLOS_Type(Integer32):
    """Custom type adDSX1CommonProvAutoFailoverLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdDSX1CommonProvAutoFailoverLOS_Type.__name__ = "Integer32"
_AdDSX1CommonProvAutoFailoverLOS_Object = MibTableColumn
adDSX1CommonProvAutoFailoverLOS = _AdDSX1CommonProvAutoFailoverLOS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 5),
    _AdDSX1CommonProvAutoFailoverLOS_Type()
)
adDSX1CommonProvAutoFailoverLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvAutoFailoverLOS.setStatus("current")


class _AdDSX1CommonProvAutoFailoverLOF_Type(Integer32):
    """Custom type adDSX1CommonProvAutoFailoverLOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdDSX1CommonProvAutoFailoverLOF_Type.__name__ = "Integer32"
_AdDSX1CommonProvAutoFailoverLOF_Object = MibTableColumn
adDSX1CommonProvAutoFailoverLOF = _AdDSX1CommonProvAutoFailoverLOF_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 6),
    _AdDSX1CommonProvAutoFailoverLOF_Type()
)
adDSX1CommonProvAutoFailoverLOF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvAutoFailoverLOF.setStatus("current")


class _AdDSX1CommonProvAutoFailoverBERThresh_Type(Integer32):
    """Custom type adDSX1CommonProvAutoFailoverBERThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tennegthree", 2),
          ("tennegfour", 3),
          ("tennegfive", 4),
          ("tennegsix", 5),
          ("tennegseven", 6))
    )


_AdDSX1CommonProvAutoFailoverBERThresh_Type.__name__ = "Integer32"
_AdDSX1CommonProvAutoFailoverBERThresh_Object = MibTableColumn
adDSX1CommonProvAutoFailoverBERThresh = _AdDSX1CommonProvAutoFailoverBERThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 7),
    _AdDSX1CommonProvAutoFailoverBERThresh_Type()
)
adDSX1CommonProvAutoFailoverBERThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvAutoFailoverBERThresh.setStatus("current")


class _AdDSX1CommonProvT1OpState_Type(Integer32):
    """Custom type adDSX1CommonProvT1OpState based on Integer32"""
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


_AdDSX1CommonProvT1OpState_Type.__name__ = "Integer32"
_AdDSX1CommonProvT1OpState_Object = MibTableColumn
adDSX1CommonProvT1OpState = _AdDSX1CommonProvT1OpState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 8),
    _AdDSX1CommonProvT1OpState_Type()
)
adDSX1CommonProvT1OpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvT1OpState.setStatus("current")


class _AdDSX1CommonProvRAI_Type(Integer32):
    """Custom type adDSX1CommonProvRAI based on Integer32"""
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


_AdDSX1CommonProvRAI_Type.__name__ = "Integer32"
_AdDSX1CommonProvRAI_Object = MibTableColumn
adDSX1CommonProvRAI = _AdDSX1CommonProvRAI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 9),
    _AdDSX1CommonProvRAI_Type()
)
adDSX1CommonProvRAI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvRAI.setStatus("current")


class _AdDSX1CommonProvEBit_Type(Integer32):
    """Custom type adDSX1CommonProvEBit based on Integer32"""
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


_AdDSX1CommonProvEBit_Type.__name__ = "Integer32"
_AdDSX1CommonProvEBit_Object = MibTableColumn
adDSX1CommonProvEBit = _AdDSX1CommonProvEBit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 1, 1, 1, 10),
    _AdDSX1CommonProvEBit_Type()
)
adDSX1CommonProvEBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonProvEBit.setStatus("current")
_AdDSX1CommonAlmProv_ObjectIdentity = ObjectIdentity
adDSX1CommonAlmProv = _AdDSX1CommonAlmProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2)
)
_AdDSX1CommonAlmTable_Object = MibTable
adDSX1CommonAlmTable = _AdDSX1CommonAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1)
)
if mibBuilder.loadTexts:
    adDSX1CommonAlmTable.setStatus("current")
_AdDSX1CommonAlmEntry_Object = MibTableRow
adDSX1CommonAlmEntry = _AdDSX1CommonAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1)
)
adDSX1CommonAlmEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonAlmEntry.setStatus("current")


class _AdDSX1CommonAlmSetThrsDefaults_Type(Integer32):
    """Custom type adDSX1CommonAlmSetThrsDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AdDSX1CommonAlmSetThrsDefaults_Type.__name__ = "Integer32"
_AdDSX1CommonAlmSetThrsDefaults_Object = MibTableColumn
adDSX1CommonAlmSetThrsDefaults = _AdDSX1CommonAlmSetThrsDefaults_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 1),
    _AdDSX1CommonAlmSetThrsDefaults_Type()
)
adDSX1CommonAlmSetThrsDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmSetThrsDefaults.setStatus("current")


class _AdDSX1CommonAlmEnableAllThrsAlarms_Type(Integer32):
    """Custom type adDSX1CommonAlmEnableAllThrsAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AdDSX1CommonAlmEnableAllThrsAlarms_Type.__name__ = "Integer32"
_AdDSX1CommonAlmEnableAllThrsAlarms_Object = MibTableColumn
adDSX1CommonAlmEnableAllThrsAlarms = _AdDSX1CommonAlmEnableAllThrsAlarms_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 2),
    _AdDSX1CommonAlmEnableAllThrsAlarms_Type()
)
adDSX1CommonAlmEnableAllThrsAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmEnableAllThrsAlarms.setStatus("current")


class _AdDSX1CommonAlmDisableAllThrsAlarms_Type(Integer32):
    """Custom type adDSX1CommonAlmDisableAllThrsAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AdDSX1CommonAlmDisableAllThrsAlarms_Type.__name__ = "Integer32"
_AdDSX1CommonAlmDisableAllThrsAlarms_Object = MibTableColumn
adDSX1CommonAlmDisableAllThrsAlarms = _AdDSX1CommonAlmDisableAllThrsAlarms_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 3),
    _AdDSX1CommonAlmDisableAllThrsAlarms_Type()
)
adDSX1CommonAlmDisableAllThrsAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmDisableAllThrsAlarms.setStatus("current")


class _AdDSX1CommonAlmResetPerfMonRegisters_Type(Integer32):
    """Custom type adDSX1CommonAlmResetPerfMonRegisters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AdDSX1CommonAlmResetPerfMonRegisters_Type.__name__ = "Integer32"
_AdDSX1CommonAlmResetPerfMonRegisters_Object = MibTableColumn
adDSX1CommonAlmResetPerfMonRegisters = _AdDSX1CommonAlmResetPerfMonRegisters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 4),
    _AdDSX1CommonAlmResetPerfMonRegisters_Type()
)
adDSX1CommonAlmResetPerfMonRegisters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmResetPerfMonRegisters.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsEnable_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsEnable_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsEnable = _AdDSX1CommonAlmNearQtrThrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 5),
    _AdDSX1CommonAlmNearQtrThrsEnable_Type()
)
adDSX1CommonAlmNearQtrThrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsEnable.setStatus("current")
_AdDSX1CommonAlmNearDayThrsEnable_Type = Integer32
_AdDSX1CommonAlmNearDayThrsEnable_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsEnable = _AdDSX1CommonAlmNearDayThrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 6),
    _AdDSX1CommonAlmNearDayThrsEnable_Type()
)
adDSX1CommonAlmNearDayThrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsEnable.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsEnable_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsEnable_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsEnable = _AdDSX1CommonAlmFarQtrThrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 7),
    _AdDSX1CommonAlmFarQtrThrsEnable_Type()
)
adDSX1CommonAlmFarQtrThrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsEnable.setStatus("current")
_AdDSX1CommonAlmFarDayThrsEnable_Type = Integer32
_AdDSX1CommonAlmFarDayThrsEnable_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsEnable = _AdDSX1CommonAlmFarDayThrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 8),
    _AdDSX1CommonAlmFarDayThrsEnable_Type()
)
adDSX1CommonAlmFarDayThrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsEnable.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsESP_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsESP_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsESP = _AdDSX1CommonAlmNearQtrThrsESP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 9),
    _AdDSX1CommonAlmNearQtrThrsESP_Type()
)
adDSX1CommonAlmNearQtrThrsESP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsESP.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsSESP_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsSESP_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsSESP = _AdDSX1CommonAlmNearQtrThrsSESP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 10),
    _AdDSX1CommonAlmNearQtrThrsSESP_Type()
)
adDSX1CommonAlmNearQtrThrsSESP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsSESP.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsSEFSP_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsSEFSP_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsSEFSP = _AdDSX1CommonAlmNearQtrThrsSEFSP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 11),
    _AdDSX1CommonAlmNearQtrThrsSEFSP_Type()
)
adDSX1CommonAlmNearQtrThrsSEFSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsSEFSP.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsUASP_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsUASP_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsUASP = _AdDSX1CommonAlmNearQtrThrsUASP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 12),
    _AdDSX1CommonAlmNearQtrThrsUASP_Type()
)
adDSX1CommonAlmNearQtrThrsUASP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsUASP.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsCSS_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsCSS_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsCSS = _AdDSX1CommonAlmNearQtrThrsCSS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 13),
    _AdDSX1CommonAlmNearQtrThrsCSS_Type()
)
adDSX1CommonAlmNearQtrThrsCSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsCSS.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsCVP_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsCVP_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsCVP = _AdDSX1CommonAlmNearQtrThrsCVP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 14),
    _AdDSX1CommonAlmNearQtrThrsCVP_Type()
)
adDSX1CommonAlmNearQtrThrsCVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsCVP.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsESL_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsESL_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsESL = _AdDSX1CommonAlmNearQtrThrsESL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 15),
    _AdDSX1CommonAlmNearQtrThrsESL_Type()
)
adDSX1CommonAlmNearQtrThrsESL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsESL.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsSESL_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsSESL_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsSESL = _AdDSX1CommonAlmNearQtrThrsSESL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 16),
    _AdDSX1CommonAlmNearQtrThrsSESL_Type()
)
adDSX1CommonAlmNearQtrThrsSESL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsSESL.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsESBP_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsESBP_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsESBP = _AdDSX1CommonAlmNearQtrThrsESBP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 17),
    _AdDSX1CommonAlmNearQtrThrsESBP_Type()
)
adDSX1CommonAlmNearQtrThrsESBP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsESBP.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsDGRM_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsDGRM_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsDGRM = _AdDSX1CommonAlmNearQtrThrsDGRM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 18),
    _AdDSX1CommonAlmNearQtrThrsDGRM_Type()
)
adDSX1CommonAlmNearQtrThrsDGRM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsDGRM.setStatus("current")
_AdDSX1CommonAlmNearQtrThrsCVL_Type = Integer32
_AdDSX1CommonAlmNearQtrThrsCVL_Object = MibTableColumn
adDSX1CommonAlmNearQtrThrsCVL = _AdDSX1CommonAlmNearQtrThrsCVL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 19),
    _AdDSX1CommonAlmNearQtrThrsCVL_Type()
)
adDSX1CommonAlmNearQtrThrsCVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearQtrThrsCVL.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsESPFE_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsESPFE_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsESPFE = _AdDSX1CommonAlmFarQtrThrsESPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 20),
    _AdDSX1CommonAlmFarQtrThrsESPFE_Type()
)
adDSX1CommonAlmFarQtrThrsESPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsESPFE.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsSESPFE_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsSESPFE_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsSESPFE = _AdDSX1CommonAlmFarQtrThrsSESPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 21),
    _AdDSX1CommonAlmFarQtrThrsSESPFE_Type()
)
adDSX1CommonAlmFarQtrThrsSESPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsSESPFE.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsSEFSPFE_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsSEFSPFE_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsSEFSPFE = _AdDSX1CommonAlmFarQtrThrsSEFSPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 22),
    _AdDSX1CommonAlmFarQtrThrsSEFSPFE_Type()
)
adDSX1CommonAlmFarQtrThrsSEFSPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsSEFSPFE.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsUASPFE_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsUASPFE_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsUASPFE = _AdDSX1CommonAlmFarQtrThrsUASPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 23),
    _AdDSX1CommonAlmFarQtrThrsUASPFE_Type()
)
adDSX1CommonAlmFarQtrThrsUASPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsUASPFE.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsCSSPFE_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsCSSPFE_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsCSSPFE = _AdDSX1CommonAlmFarQtrThrsCSSPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 24),
    _AdDSX1CommonAlmFarQtrThrsCSSPFE_Type()
)
adDSX1CommonAlmFarQtrThrsCSSPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsCSSPFE.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsCVPFE_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsCVPFE_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsCVPFE = _AdDSX1CommonAlmFarQtrThrsCVPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 25),
    _AdDSX1CommonAlmFarQtrThrsCVPFE_Type()
)
adDSX1CommonAlmFarQtrThrsCVPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsCVPFE.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsESLFE_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsESLFE_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsESLFE = _AdDSX1CommonAlmFarQtrThrsESLFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 26),
    _AdDSX1CommonAlmFarQtrThrsESLFE_Type()
)
adDSX1CommonAlmFarQtrThrsESLFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsESLFE.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsESBPFE_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsESBPFE_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsESBPFE = _AdDSX1CommonAlmFarQtrThrsESBPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 27),
    _AdDSX1CommonAlmFarQtrThrsESBPFE_Type()
)
adDSX1CommonAlmFarQtrThrsESBPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsESBPFE.setStatus("current")
_AdDSX1CommonAlmFarQtrThrsDGRMPFE_Type = Integer32
_AdDSX1CommonAlmFarQtrThrsDGRMPFE_Object = MibTableColumn
adDSX1CommonAlmFarQtrThrsDGRMPFE = _AdDSX1CommonAlmFarQtrThrsDGRMPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 28),
    _AdDSX1CommonAlmFarQtrThrsDGRMPFE_Type()
)
adDSX1CommonAlmFarQtrThrsDGRMPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarQtrThrsDGRMPFE.setStatus("current")
_AdDSX1CommonAlmNearDayThrsESP_Type = Integer32
_AdDSX1CommonAlmNearDayThrsESP_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsESP = _AdDSX1CommonAlmNearDayThrsESP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 29),
    _AdDSX1CommonAlmNearDayThrsESP_Type()
)
adDSX1CommonAlmNearDayThrsESP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsESP.setStatus("current")
_AdDSX1CommonAlmNearDayThrsSESP_Type = Integer32
_AdDSX1CommonAlmNearDayThrsSESP_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsSESP = _AdDSX1CommonAlmNearDayThrsSESP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 30),
    _AdDSX1CommonAlmNearDayThrsSESP_Type()
)
adDSX1CommonAlmNearDayThrsSESP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsSESP.setStatus("current")
_AdDSX1CommonAlmNearDayThrsSEFSP_Type = Integer32
_AdDSX1CommonAlmNearDayThrsSEFSP_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsSEFSP = _AdDSX1CommonAlmNearDayThrsSEFSP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 31),
    _AdDSX1CommonAlmNearDayThrsSEFSP_Type()
)
adDSX1CommonAlmNearDayThrsSEFSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsSEFSP.setStatus("current")
_AdDSX1CommonAlmNearDayThrsUASP_Type = Integer32
_AdDSX1CommonAlmNearDayThrsUASP_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsUASP = _AdDSX1CommonAlmNearDayThrsUASP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 32),
    _AdDSX1CommonAlmNearDayThrsUASP_Type()
)
adDSX1CommonAlmNearDayThrsUASP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsUASP.setStatus("current")
_AdDSX1CommonAlmNearDayThrsCSS_Type = Integer32
_AdDSX1CommonAlmNearDayThrsCSS_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsCSS = _AdDSX1CommonAlmNearDayThrsCSS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 33),
    _AdDSX1CommonAlmNearDayThrsCSS_Type()
)
adDSX1CommonAlmNearDayThrsCSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsCSS.setStatus("current")
_AdDSX1CommonAlmNearDayThrsCVP_Type = Integer32
_AdDSX1CommonAlmNearDayThrsCVP_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsCVP = _AdDSX1CommonAlmNearDayThrsCVP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 34),
    _AdDSX1CommonAlmNearDayThrsCVP_Type()
)
adDSX1CommonAlmNearDayThrsCVP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsCVP.setStatus("current")
_AdDSX1CommonAlmNearDayThrsESL_Type = Integer32
_AdDSX1CommonAlmNearDayThrsESL_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsESL = _AdDSX1CommonAlmNearDayThrsESL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 35),
    _AdDSX1CommonAlmNearDayThrsESL_Type()
)
adDSX1CommonAlmNearDayThrsESL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsESL.setStatus("current")
_AdDSX1CommonAlmNearDayThrsSESL_Type = Integer32
_AdDSX1CommonAlmNearDayThrsSESL_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsSESL = _AdDSX1CommonAlmNearDayThrsSESL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 36),
    _AdDSX1CommonAlmNearDayThrsSESL_Type()
)
adDSX1CommonAlmNearDayThrsSESL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsSESL.setStatus("current")
_AdDSX1CommonAlmNearDayThrsESBP_Type = Integer32
_AdDSX1CommonAlmNearDayThrsESBP_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsESBP = _AdDSX1CommonAlmNearDayThrsESBP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 37),
    _AdDSX1CommonAlmNearDayThrsESBP_Type()
)
adDSX1CommonAlmNearDayThrsESBP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsESBP.setStatus("current")
_AdDSX1CommonAlmNearDayThrsDGRM_Type = Integer32
_AdDSX1CommonAlmNearDayThrsDGRM_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsDGRM = _AdDSX1CommonAlmNearDayThrsDGRM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 38),
    _AdDSX1CommonAlmNearDayThrsDGRM_Type()
)
adDSX1CommonAlmNearDayThrsDGRM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsDGRM.setStatus("current")
_AdDSX1CommonAlmNearDayThrsCVL_Type = Integer32
_AdDSX1CommonAlmNearDayThrsCVL_Object = MibTableColumn
adDSX1CommonAlmNearDayThrsCVL = _AdDSX1CommonAlmNearDayThrsCVL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 39),
    _AdDSX1CommonAlmNearDayThrsCVL_Type()
)
adDSX1CommonAlmNearDayThrsCVL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmNearDayThrsCVL.setStatus("current")
_AdDSX1CommonAlmFarDayThrsESPFE_Type = Integer32
_AdDSX1CommonAlmFarDayThrsESPFE_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsESPFE = _AdDSX1CommonAlmFarDayThrsESPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 40),
    _AdDSX1CommonAlmFarDayThrsESPFE_Type()
)
adDSX1CommonAlmFarDayThrsESPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsESPFE.setStatus("current")
_AdDSX1CommonAlmFarDayThrsSESPFE_Type = Integer32
_AdDSX1CommonAlmFarDayThrsSESPFE_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsSESPFE = _AdDSX1CommonAlmFarDayThrsSESPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 41),
    _AdDSX1CommonAlmFarDayThrsSESPFE_Type()
)
adDSX1CommonAlmFarDayThrsSESPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsSESPFE.setStatus("current")
_AdDSX1CommonAlmFarDayThrsSEFSPFE_Type = Integer32
_AdDSX1CommonAlmFarDayThrsSEFSPFE_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsSEFSPFE = _AdDSX1CommonAlmFarDayThrsSEFSPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 42),
    _AdDSX1CommonAlmFarDayThrsSEFSPFE_Type()
)
adDSX1CommonAlmFarDayThrsSEFSPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsSEFSPFE.setStatus("current")
_AdDSX1CommonAlmFarDayThrsUASPFE_Type = Integer32
_AdDSX1CommonAlmFarDayThrsUASPFE_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsUASPFE = _AdDSX1CommonAlmFarDayThrsUASPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 43),
    _AdDSX1CommonAlmFarDayThrsUASPFE_Type()
)
adDSX1CommonAlmFarDayThrsUASPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsUASPFE.setStatus("current")
_AdDSX1CommonAlmFarDayThrsCSSPFE_Type = Integer32
_AdDSX1CommonAlmFarDayThrsCSSPFE_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsCSSPFE = _AdDSX1CommonAlmFarDayThrsCSSPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 44),
    _AdDSX1CommonAlmFarDayThrsCSSPFE_Type()
)
adDSX1CommonAlmFarDayThrsCSSPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsCSSPFE.setStatus("current")
_AdDSX1CommonAlmFarDayThrsCVPFE_Type = Integer32
_AdDSX1CommonAlmFarDayThrsCVPFE_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsCVPFE = _AdDSX1CommonAlmFarDayThrsCVPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 45),
    _AdDSX1CommonAlmFarDayThrsCVPFE_Type()
)
adDSX1CommonAlmFarDayThrsCVPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsCVPFE.setStatus("current")
_AdDSX1CommonAlmFarDayThrsESLFE_Type = Integer32
_AdDSX1CommonAlmFarDayThrsESLFE_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsESLFE = _AdDSX1CommonAlmFarDayThrsESLFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 46),
    _AdDSX1CommonAlmFarDayThrsESLFE_Type()
)
adDSX1CommonAlmFarDayThrsESLFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsESLFE.setStatus("current")
_AdDSX1CommonAlmFarDayThrsESBPFE_Type = Integer32
_AdDSX1CommonAlmFarDayThrsESBPFE_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsESBPFE = _AdDSX1CommonAlmFarDayThrsESBPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 47),
    _AdDSX1CommonAlmFarDayThrsESBPFE_Type()
)
adDSX1CommonAlmFarDayThrsESBPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsESBPFE.setStatus("current")
_AdDSX1CommonAlmFarDayThrsDGRMPFE_Type = Integer32
_AdDSX1CommonAlmFarDayThrsDGRMPFE_Object = MibTableColumn
adDSX1CommonAlmFarDayThrsDGRMPFE = _AdDSX1CommonAlmFarDayThrsDGRMPFE_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 48),
    _AdDSX1CommonAlmFarDayThrsDGRMPFE_Type()
)
adDSX1CommonAlmFarDayThrsDGRMPFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmFarDayThrsDGRMPFE.setStatus("current")


class _AdDSX1CommonAlmPHTLThrsEnable_Type(Integer32):
    """Custom type adDSX1CommonAlmPHTLThrsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdDSX1CommonAlmPHTLThrsEnable_Type.__name__ = "Integer32"
_AdDSX1CommonAlmPHTLThrsEnable_Object = MibTableColumn
adDSX1CommonAlmPHTLThrsEnable = _AdDSX1CommonAlmPHTLThrsEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 1, 1, 49),
    _AdDSX1CommonAlmPHTLThrsEnable_Type()
)
adDSX1CommonAlmPHTLThrsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonAlmPHTLThrsEnable.setStatus("current")
_AdDSX1CommonEnhancedAlmSlotTable_Object = MibTable
adDSX1CommonEnhancedAlmSlotTable = _AdDSX1CommonEnhancedAlmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2)
)
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotTable.setStatus("current")
_AdDSX1CommonEnhancedAlmSlotEntry_Object = MibTableRow
adDSX1CommonEnhancedAlmSlotEntry = _AdDSX1CommonEnhancedAlmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1)
)
adDSX1CommonEnhancedAlmSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotEntry.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSALOSSeverity_Type(Integer32):
    """Custom type adDSX1CommonEnhancedAlmSlotSALOSSeverity based on Integer32"""
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


_AdDSX1CommonEnhancedAlmSlotSALOSSeverity_Type.__name__ = "Integer32"
_AdDSX1CommonEnhancedAlmSlotSALOSSeverity_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSALOSSeverity = _AdDSX1CommonEnhancedAlmSlotSALOSSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 1),
    _AdDSX1CommonEnhancedAlmSlotSALOSSeverity_Type()
)
adDSX1CommonEnhancedAlmSlotSALOSSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSALOSSeverity.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSALOSSuppression_Type(Integer32):
    """Custom type adDSX1CommonEnhancedAlmSlotSALOSSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdDSX1CommonEnhancedAlmSlotSALOSSuppression_Type.__name__ = "Integer32"
_AdDSX1CommonEnhancedAlmSlotSALOSSuppression_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSALOSSuppression = _AdDSX1CommonEnhancedAlmSlotSALOSSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 2),
    _AdDSX1CommonEnhancedAlmSlotSALOSSuppression_Type()
)
adDSX1CommonEnhancedAlmSlotSALOSSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSALOSSuppression.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSALOFSeverity_Type(Integer32):
    """Custom type adDSX1CommonEnhancedAlmSlotSALOFSeverity based on Integer32"""
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


_AdDSX1CommonEnhancedAlmSlotSALOFSeverity_Type.__name__ = "Integer32"
_AdDSX1CommonEnhancedAlmSlotSALOFSeverity_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSALOFSeverity = _AdDSX1CommonEnhancedAlmSlotSALOFSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 3),
    _AdDSX1CommonEnhancedAlmSlotSALOFSeverity_Type()
)
adDSX1CommonEnhancedAlmSlotSALOFSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSALOFSeverity.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSALOFSuppression_Type(Integer32):
    """Custom type adDSX1CommonEnhancedAlmSlotSALOFSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdDSX1CommonEnhancedAlmSlotSALOFSuppression_Type.__name__ = "Integer32"
_AdDSX1CommonEnhancedAlmSlotSALOFSuppression_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSALOFSuppression = _AdDSX1CommonEnhancedAlmSlotSALOFSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 4),
    _AdDSX1CommonEnhancedAlmSlotSALOFSuppression_Type()
)
adDSX1CommonEnhancedAlmSlotSALOFSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSALOFSuppression.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSAAISSeverity_Type(Integer32):
    """Custom type adDSX1CommonEnhancedAlmSlotSAAISSeverity based on Integer32"""
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


_AdDSX1CommonEnhancedAlmSlotSAAISSeverity_Type.__name__ = "Integer32"
_AdDSX1CommonEnhancedAlmSlotSAAISSeverity_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSAAISSeverity = _AdDSX1CommonEnhancedAlmSlotSAAISSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 5),
    _AdDSX1CommonEnhancedAlmSlotSAAISSeverity_Type()
)
adDSX1CommonEnhancedAlmSlotSAAISSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSAAISSeverity.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSAAISSSuppression_Type(Integer32):
    """Custom type adDSX1CommonEnhancedAlmSlotSAAISSSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdDSX1CommonEnhancedAlmSlotSAAISSSuppression_Type.__name__ = "Integer32"
_AdDSX1CommonEnhancedAlmSlotSAAISSSuppression_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSAAISSSuppression = _AdDSX1CommonEnhancedAlmSlotSAAISSSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 6),
    _AdDSX1CommonEnhancedAlmSlotSAAISSSuppression_Type()
)
adDSX1CommonEnhancedAlmSlotSAAISSSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSAAISSSuppression.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSARAISeverity_Type(Integer32):
    """Custom type adDSX1CommonEnhancedAlmSlotSARAISeverity based on Integer32"""
    defaultValue = 4

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


_AdDSX1CommonEnhancedAlmSlotSARAISeverity_Type.__name__ = "Integer32"
_AdDSX1CommonEnhancedAlmSlotSARAISeverity_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSARAISeverity = _AdDSX1CommonEnhancedAlmSlotSARAISeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 7),
    _AdDSX1CommonEnhancedAlmSlotSARAISeverity_Type()
)
adDSX1CommonEnhancedAlmSlotSARAISeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSARAISeverity.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSARAISuppression_Type(Integer32):
    """Custom type adDSX1CommonEnhancedAlmSlotSARAISuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdDSX1CommonEnhancedAlmSlotSARAISuppression_Type.__name__ = "Integer32"
_AdDSX1CommonEnhancedAlmSlotSARAISuppression_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSARAISuppression = _AdDSX1CommonEnhancedAlmSlotSARAISuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 8),
    _AdDSX1CommonEnhancedAlmSlotSARAISuppression_Type()
)
adDSX1CommonEnhancedAlmSlotSARAISuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSARAISuppression.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSALOSEnable_Type(TruthValue):
    """Custom type adDSX1CommonEnhancedAlmSlotSALOSEnable based on TruthValue"""
    defaultValue = 1


_AdDSX1CommonEnhancedAlmSlotSALOSEnable_Type.__name__ = "TruthValue"
_AdDSX1CommonEnhancedAlmSlotSALOSEnable_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSALOSEnable = _AdDSX1CommonEnhancedAlmSlotSALOSEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 9),
    _AdDSX1CommonEnhancedAlmSlotSALOSEnable_Type()
)
adDSX1CommonEnhancedAlmSlotSALOSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSALOSEnable.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSALOFEnable_Type(TruthValue):
    """Custom type adDSX1CommonEnhancedAlmSlotSALOFEnable based on TruthValue"""
    defaultValue = 1


_AdDSX1CommonEnhancedAlmSlotSALOFEnable_Type.__name__ = "TruthValue"
_AdDSX1CommonEnhancedAlmSlotSALOFEnable_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSALOFEnable = _AdDSX1CommonEnhancedAlmSlotSALOFEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 10),
    _AdDSX1CommonEnhancedAlmSlotSALOFEnable_Type()
)
adDSX1CommonEnhancedAlmSlotSALOFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSALOFEnable.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSAAISEnable_Type(TruthValue):
    """Custom type adDSX1CommonEnhancedAlmSlotSAAISEnable based on TruthValue"""
    defaultValue = 1


_AdDSX1CommonEnhancedAlmSlotSAAISEnable_Type.__name__ = "TruthValue"
_AdDSX1CommonEnhancedAlmSlotSAAISEnable_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSAAISEnable = _AdDSX1CommonEnhancedAlmSlotSAAISEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 11),
    _AdDSX1CommonEnhancedAlmSlotSAAISEnable_Type()
)
adDSX1CommonEnhancedAlmSlotSAAISEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSAAISEnable.setStatus("current")


class _AdDSX1CommonEnhancedAlmSlotSARAIEnable_Type(TruthValue):
    """Custom type adDSX1CommonEnhancedAlmSlotSARAIEnable based on TruthValue"""
    defaultValue = 1


_AdDSX1CommonEnhancedAlmSlotSARAIEnable_Type.__name__ = "TruthValue"
_AdDSX1CommonEnhancedAlmSlotSARAIEnable_Object = MibTableColumn
adDSX1CommonEnhancedAlmSlotSARAIEnable = _AdDSX1CommonEnhancedAlmSlotSARAIEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 2, 2, 1, 12),
    _AdDSX1CommonEnhancedAlmSlotSARAIEnable_Type()
)
adDSX1CommonEnhancedAlmSlotSARAIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonEnhancedAlmSlotSARAIEnable.setStatus("current")
_AdDSX1CommonTest_ObjectIdentity = ObjectIdentity
adDSX1CommonTest = _AdDSX1CommonTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 3)
)
_AdDSX1CommonTestTable_Object = MibTable
adDSX1CommonTestTable = _AdDSX1CommonTestTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 3, 1)
)
if mibBuilder.loadTexts:
    adDSX1CommonTestTable.setStatus("current")
_AdDSX1CommonTestEntry_Object = MibTableRow
adDSX1CommonTestEntry = _AdDSX1CommonTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 3, 1, 1)
)
adDSX1CommonTestEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonTestEntry.setStatus("current")


class _AdDSX1CommonTestFarEndLoopback_Type(Integer32):
    """Custom type adDSX1CommonTestFarEndLoopback based on Integer32"""
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


_AdDSX1CommonTestFarEndLoopback_Type.__name__ = "Integer32"
_AdDSX1CommonTestFarEndLoopback_Object = MibTableColumn
adDSX1CommonTestFarEndLoopback = _AdDSX1CommonTestFarEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 3, 1, 1, 1),
    _AdDSX1CommonTestFarEndLoopback_Type()
)
adDSX1CommonTestFarEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonTestFarEndLoopback.setStatus("current")


class _AdDSX1CommonTestT1ProtectSelect_Type(Integer32):
    """Custom type adDSX1CommonTestT1ProtectSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("notprotected", 2))
    )


_AdDSX1CommonTestT1ProtectSelect_Type.__name__ = "Integer32"
_AdDSX1CommonTestT1ProtectSelect_Object = MibTableColumn
adDSX1CommonTestT1ProtectSelect = _AdDSX1CommonTestT1ProtectSelect_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 3, 1, 1, 2),
    _AdDSX1CommonTestT1ProtectSelect_Type()
)
adDSX1CommonTestT1ProtectSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonTestT1ProtectSelect.setStatus("deprecated")
_AdDSX1CommonStatus_ObjectIdentity = ObjectIdentity
adDSX1CommonStatus = _AdDSX1CommonStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 4)
)
_AdDSX1CommonStatusTable_Object = MibTable
adDSX1CommonStatusTable = _AdDSX1CommonStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 4, 1)
)
if mibBuilder.loadTexts:
    adDSX1CommonStatusTable.setStatus("current")
_AdDSX1CommonStatusEntry_Object = MibTableRow
adDSX1CommonStatusEntry = _AdDSX1CommonStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 4, 1, 1)
)
adDSX1CommonStatusEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonStatusEntry.setStatus("current")


class _AdDSX1CommonStatusLoopStatus_Type(Integer32):
    """Custom type adDSX1CommonStatusLoopStatus based on Integer32"""
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
        *(("na", 1),
          ("ok", 2),
          ("los", 3),
          ("lof", 4),
          ("ais", 5),
          ("rai", 6),
          ("bpv", 7))
    )


_AdDSX1CommonStatusLoopStatus_Type.__name__ = "Integer32"
_AdDSX1CommonStatusLoopStatus_Object = MibTableColumn
adDSX1CommonStatusLoopStatus = _AdDSX1CommonStatusLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 4, 1, 1, 1),
    _AdDSX1CommonStatusLoopStatus_Type()
)
adDSX1CommonStatusLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonStatusLoopStatus.setStatus("current")
_AdDSX1CommonSLC2PerfMon_ObjectIdentity = ObjectIdentity
adDSX1CommonSLC2PerfMon = _AdDSX1CommonSLC2PerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 5)
)
_AdDSX1CommonSLC2PerfMonTable_Object = MibTable
adDSX1CommonSLC2PerfMonTable = _AdDSX1CommonSLC2PerfMonTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 5, 1)
)
if mibBuilder.loadTexts:
    adDSX1CommonSLC2PerfMonTable.setStatus("current")
_AdDSX1CommonSLC2PerfMonEntry_Object = MibTableRow
adDSX1CommonSLC2PerfMonEntry = _AdDSX1CommonSLC2PerfMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 5, 1, 1)
)
adDSX1CommonSLC2PerfMonEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonSLC2PerfMonEntry.setStatus("current")
_AdDSX1CommonSLC2PerfMonBlockCall_Type = Integer32
_AdDSX1CommonSLC2PerfMonBlockCall_Object = MibTableColumn
adDSX1CommonSLC2PerfMonBlockCall = _AdDSX1CommonSLC2PerfMonBlockCall_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 5, 1, 1, 1),
    _AdDSX1CommonSLC2PerfMonBlockCall_Type()
)
adDSX1CommonSLC2PerfMonBlockCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonSLC2PerfMonBlockCall.setStatus("current")
_AdDSX1CommonSLC2PerfMonAllTrunkBusy_Type = Integer32
_AdDSX1CommonSLC2PerfMonAllTrunkBusy_Object = MibTableColumn
adDSX1CommonSLC2PerfMonAllTrunkBusy = _AdDSX1CommonSLC2PerfMonAllTrunkBusy_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 5, 1, 1, 2),
    _AdDSX1CommonSLC2PerfMonAllTrunkBusy_Type()
)
adDSX1CommonSLC2PerfMonAllTrunkBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonSLC2PerfMonAllTrunkBusy.setStatus("current")
_AdDSX1CommonSLC2PerfMonNailedTimeSlot_Type = Integer32
_AdDSX1CommonSLC2PerfMonNailedTimeSlot_Object = MibTableColumn
adDSX1CommonSLC2PerfMonNailedTimeSlot = _AdDSX1CommonSLC2PerfMonNailedTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 5, 1, 1, 3),
    _AdDSX1CommonSLC2PerfMonNailedTimeSlot_Type()
)
adDSX1CommonSLC2PerfMonNailedTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonSLC2PerfMonNailedTimeSlot.setStatus("current")
_AdDSX1CommonSLC2PerfMonPHTL_Type = Integer32
_AdDSX1CommonSLC2PerfMonPHTL_Object = MibTableColumn
adDSX1CommonSLC2PerfMonPHTL = _AdDSX1CommonSLC2PerfMonPHTL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 5, 1, 1, 4),
    _AdDSX1CommonSLC2PerfMonPHTL_Type()
)
adDSX1CommonSLC2PerfMonPHTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonSLC2PerfMonPHTL.setStatus("current")
_AdDSX1CommonSLC2PerfMonPHTLThreshold_Type = Integer32
_AdDSX1CommonSLC2PerfMonPHTLThreshold_Object = MibTableColumn
adDSX1CommonSLC2PerfMonPHTLThreshold = _AdDSX1CommonSLC2PerfMonPHTLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 5, 1, 1, 5),
    _AdDSX1CommonSLC2PerfMonPHTLThreshold_Type()
)
adDSX1CommonSLC2PerfMonPHTLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonSLC2PerfMonPHTLThreshold.setStatus("current")
_AdDSX1CommonMibConformance_ObjectIdentity = ObjectIdentity
adDSX1CommonMibConformance = _AdDSX1CommonMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6)
)
_AdDSX1CommonMibGroups_ObjectIdentity = ObjectIdentity
adDSX1CommonMibGroups = _AdDSX1CommonMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6, 1)
)
_AdDSX1CommonDailyPmInt_ObjectIdentity = ObjectIdentity
adDSX1CommonDailyPmInt = _AdDSX1CommonDailyPmInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7)
)
_AdDSX1CommonDailyPmIntervalTable_Object = MibTable
adDSX1CommonDailyPmIntervalTable = _AdDSX1CommonDailyPmIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 1)
)
if mibBuilder.loadTexts:
    adDSX1CommonDailyPmIntervalTable.setStatus("current")
_AdDSX1CommonDailyPmIntervalEntry_Object = MibTableRow
adDSX1CommonDailyPmIntervalEntry = _AdDSX1CommonDailyPmIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 1, 1)
)
adDSX1CommonDailyPmIntervalEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
    (0, "ADTRAN-DSX1COMMON-MIB", "adDSX1CommonDailyPmInterval"),
)
if mibBuilder.loadTexts:
    adDSX1CommonDailyPmIntervalEntry.setStatus("current")
_AdDSX1CommonDailyPmInterval_Type = Integer32
_AdDSX1CommonDailyPmInterval_Object = MibTableColumn
adDSX1CommonDailyPmInterval = _AdDSX1CommonDailyPmInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 1, 1, 1),
    _AdDSX1CommonDailyPmInterval_Type()
)
adDSX1CommonDailyPmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonDailyPmInterval.setStatus("current")
_AdDSX1CommonDailyPmESP_Type = PerfTotalCount
_AdDSX1CommonDailyPmESP_Object = MibTableColumn
adDSX1CommonDailyPmESP = _AdDSX1CommonDailyPmESP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 1, 1, 2),
    _AdDSX1CommonDailyPmESP_Type()
)
adDSX1CommonDailyPmESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonDailyPmESP.setStatus("current")
_AdDSX1CommonDailyPmSESP_Type = PerfTotalCount
_AdDSX1CommonDailyPmSESP_Object = MibTableColumn
adDSX1CommonDailyPmSESP = _AdDSX1CommonDailyPmSESP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 1, 1, 3),
    _AdDSX1CommonDailyPmSESP_Type()
)
adDSX1CommonDailyPmSESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonDailyPmSESP.setStatus("current")
_AdDSX1CommonDailyPmUASP_Type = PerfTotalCount
_AdDSX1CommonDailyPmUASP_Object = MibTableColumn
adDSX1CommonDailyPmUASP = _AdDSX1CommonDailyPmUASP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 1, 1, 4),
    _AdDSX1CommonDailyPmUASP_Type()
)
adDSX1CommonDailyPmUASP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonDailyPmUASP.setStatus("current")
_AdDSX1CommonDailyPmCVP_Type = PerfTotalCount
_AdDSX1CommonDailyPmCVP_Object = MibTableColumn
adDSX1CommonDailyPmCVP = _AdDSX1CommonDailyPmCVP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 1, 1, 5),
    _AdDSX1CommonDailyPmCVP_Type()
)
adDSX1CommonDailyPmCVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonDailyPmCVP.setStatus("current")
_AdDSX1CommonDailyPmESL_Type = PerfTotalCount
_AdDSX1CommonDailyPmESL_Object = MibTableColumn
adDSX1CommonDailyPmESL = _AdDSX1CommonDailyPmESL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 1, 1, 6),
    _AdDSX1CommonDailyPmESL_Type()
)
adDSX1CommonDailyPmESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonDailyPmESL.setStatus("current")
_AdDSX1CommonDailyPmCVL_Type = PerfTotalCount
_AdDSX1CommonDailyPmCVL_Object = MibTableColumn
adDSX1CommonDailyPmCVL = _AdDSX1CommonDailyPmCVL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 1, 1, 7),
    _AdDSX1CommonDailyPmCVL_Type()
)
adDSX1CommonDailyPmCVL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonDailyPmCVL.setStatus("current")
_AdDSX1CommonCurrentDayTable_Object = MibTable
adDSX1CommonCurrentDayTable = _AdDSX1CommonCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 2)
)
if mibBuilder.loadTexts:
    adDSX1CommonCurrentDayTable.setStatus("current")
_AdDSX1CommonCurrentDayEntry_Object = MibTableRow
adDSX1CommonCurrentDayEntry = _AdDSX1CommonCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 2, 1)
)
adDSX1CommonCurrentDayEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonCurrentDayEntry.setStatus("current")
_AdDSX1CommonCurrentDayESP_Type = PerfTotalCount
_AdDSX1CommonCurrentDayESP_Object = MibTableColumn
adDSX1CommonCurrentDayESP = _AdDSX1CommonCurrentDayESP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 2, 1, 1),
    _AdDSX1CommonCurrentDayESP_Type()
)
adDSX1CommonCurrentDayESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonCurrentDayESP.setStatus("current")
_AdDSX1CommonCurrentDaySESP_Type = PerfTotalCount
_AdDSX1CommonCurrentDaySESP_Object = MibTableColumn
adDSX1CommonCurrentDaySESP = _AdDSX1CommonCurrentDaySESP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 2, 1, 2),
    _AdDSX1CommonCurrentDaySESP_Type()
)
adDSX1CommonCurrentDaySESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonCurrentDaySESP.setStatus("current")
_AdDSX1CommonCurrentDayUASP_Type = PerfTotalCount
_AdDSX1CommonCurrentDayUASP_Object = MibTableColumn
adDSX1CommonCurrentDayUASP = _AdDSX1CommonCurrentDayUASP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 2, 1, 3),
    _AdDSX1CommonCurrentDayUASP_Type()
)
adDSX1CommonCurrentDayUASP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonCurrentDayUASP.setStatus("current")
_AdDSX1CommonCurrentDayCVP_Type = PerfTotalCount
_AdDSX1CommonCurrentDayCVP_Object = MibTableColumn
adDSX1CommonCurrentDayCVP = _AdDSX1CommonCurrentDayCVP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 2, 1, 4),
    _AdDSX1CommonCurrentDayCVP_Type()
)
adDSX1CommonCurrentDayCVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonCurrentDayCVP.setStatus("current")
_AdDSX1CommonCurrentDayESL_Type = PerfTotalCount
_AdDSX1CommonCurrentDayESL_Object = MibTableColumn
adDSX1CommonCurrentDayESL = _AdDSX1CommonCurrentDayESL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 2, 1, 5),
    _AdDSX1CommonCurrentDayESL_Type()
)
adDSX1CommonCurrentDayESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonCurrentDayESL.setStatus("current")
_AdDSX1CommonCurrentDayCVL_Type = PerfTotalCount
_AdDSX1CommonCurrentDayCVL_Object = MibTableColumn
adDSX1CommonCurrentDayCVL = _AdDSX1CommonCurrentDayCVL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 2, 1, 6),
    _AdDSX1CommonCurrentDayCVL_Type()
)
adDSX1CommonCurrentDayCVL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonCurrentDayCVL.setStatus("current")
_AdDSX1CommonTotalTable_Object = MibTable
adDSX1CommonTotalTable = _AdDSX1CommonTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3)
)
if mibBuilder.loadTexts:
    adDSX1CommonTotalTable.setStatus("current")
_AdDSX1CommonTotalEntry_Object = MibTableRow
adDSX1CommonTotalEntry = _AdDSX1CommonTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1)
)
adDSX1CommonTotalEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonTotalEntry.setStatus("current")
_AdDSX1CommonTotalESs_Type = PerfTotalCount
_AdDSX1CommonTotalESs_Object = MibTableColumn
adDSX1CommonTotalESs = _AdDSX1CommonTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 1),
    _AdDSX1CommonTotalESs_Type()
)
adDSX1CommonTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalESs.setStatus("current")
_AdDSX1CommonTotalSESs_Type = PerfTotalCount
_AdDSX1CommonTotalSESs_Object = MibTableColumn
adDSX1CommonTotalSESs = _AdDSX1CommonTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 2),
    _AdDSX1CommonTotalSESs_Type()
)
adDSX1CommonTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalSESs.setStatus("current")
_AdDSX1CommonTotalSEFSs_Type = PerfTotalCount
_AdDSX1CommonTotalSEFSs_Object = MibTableColumn
adDSX1CommonTotalSEFSs = _AdDSX1CommonTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 3),
    _AdDSX1CommonTotalSEFSs_Type()
)
adDSX1CommonTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalSEFSs.setStatus("current")
_AdDSX1CommonTotalUASs_Type = PerfTotalCount
_AdDSX1CommonTotalUASs_Object = MibTableColumn
adDSX1CommonTotalUASs = _AdDSX1CommonTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 4),
    _AdDSX1CommonTotalUASs_Type()
)
adDSX1CommonTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalUASs.setStatus("current")
_AdDSX1CommonTotalCSSs_Type = PerfTotalCount
_AdDSX1CommonTotalCSSs_Object = MibTableColumn
adDSX1CommonTotalCSSs = _AdDSX1CommonTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 5),
    _AdDSX1CommonTotalCSSs_Type()
)
adDSX1CommonTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalCSSs.setStatus("current")
_AdDSX1CommonTotalPCVs_Type = PerfTotalCount
_AdDSX1CommonTotalPCVs_Object = MibTableColumn
adDSX1CommonTotalPCVs = _AdDSX1CommonTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 6),
    _AdDSX1CommonTotalPCVs_Type()
)
adDSX1CommonTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalPCVs.setStatus("current")
_AdDSX1CommonTotalLESs_Type = PerfTotalCount
_AdDSX1CommonTotalLESs_Object = MibTableColumn
adDSX1CommonTotalLESs = _AdDSX1CommonTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 7),
    _AdDSX1CommonTotalLESs_Type()
)
adDSX1CommonTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalLESs.setStatus("current")
_AdDSX1CommonTotalBESs_Type = PerfTotalCount
_AdDSX1CommonTotalBESs_Object = MibTableColumn
adDSX1CommonTotalBESs = _AdDSX1CommonTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 8),
    _AdDSX1CommonTotalBESs_Type()
)
adDSX1CommonTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalBESs.setStatus("current")
_AdDSX1CommonTotalDMs_Type = PerfTotalCount
_AdDSX1CommonTotalDMs_Object = MibTableColumn
adDSX1CommonTotalDMs = _AdDSX1CommonTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 9),
    _AdDSX1CommonTotalDMs_Type()
)
adDSX1CommonTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalDMs.setStatus("current")
_AdDSX1CommonTotalLCVs_Type = PerfTotalCount
_AdDSX1CommonTotalLCVs_Object = MibTableColumn
adDSX1CommonTotalLCVs = _AdDSX1CommonTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 3, 1, 10),
    _AdDSX1CommonTotalLCVs_Type()
)
adDSX1CommonTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonTotalLCVs.setStatus("current")
_AdDSX1CommonRollingCountTable_Object = MibTable
adDSX1CommonRollingCountTable = _AdDSX1CommonRollingCountTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4)
)
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountTable.setStatus("current")
_AdDSX1CommonRollingCountEntry_Object = MibTableRow
adDSX1CommonRollingCountEntry = _AdDSX1CommonRollingCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1)
)
adDSX1CommonRollingCountEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountEntry.setStatus("current")
_AdDSX1CommonRollingCountESs_Type = Counter32
_AdDSX1CommonRollingCountESs_Object = MibTableColumn
adDSX1CommonRollingCountESs = _AdDSX1CommonRollingCountESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 1),
    _AdDSX1CommonRollingCountESs_Type()
)
adDSX1CommonRollingCountESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountESs.setStatus("current")
_AdDSX1CommonRollingCountSESs_Type = Counter32
_AdDSX1CommonRollingCountSESs_Object = MibTableColumn
adDSX1CommonRollingCountSESs = _AdDSX1CommonRollingCountSESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 2),
    _AdDSX1CommonRollingCountSESs_Type()
)
adDSX1CommonRollingCountSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountSESs.setStatus("current")
_AdDSX1CommonRollingCountSEFSs_Type = Counter32
_AdDSX1CommonRollingCountSEFSs_Object = MibTableColumn
adDSX1CommonRollingCountSEFSs = _AdDSX1CommonRollingCountSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 3),
    _AdDSX1CommonRollingCountSEFSs_Type()
)
adDSX1CommonRollingCountSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountSEFSs.setStatus("current")
_AdDSX1CommonRollingCountUASs_Type = Counter32
_AdDSX1CommonRollingCountUASs_Object = MibTableColumn
adDSX1CommonRollingCountUASs = _AdDSX1CommonRollingCountUASs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 4),
    _AdDSX1CommonRollingCountUASs_Type()
)
adDSX1CommonRollingCountUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountUASs.setStatus("current")
_AdDSX1CommonRollingCountCSSs_Type = Counter32
_AdDSX1CommonRollingCountCSSs_Object = MibTableColumn
adDSX1CommonRollingCountCSSs = _AdDSX1CommonRollingCountCSSs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 5),
    _AdDSX1CommonRollingCountCSSs_Type()
)
adDSX1CommonRollingCountCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountCSSs.setStatus("current")
_AdDSX1CommonRollingCountPCVs_Type = Counter32
_AdDSX1CommonRollingCountPCVs_Object = MibTableColumn
adDSX1CommonRollingCountPCVs = _AdDSX1CommonRollingCountPCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 6),
    _AdDSX1CommonRollingCountPCVs_Type()
)
adDSX1CommonRollingCountPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountPCVs.setStatus("current")
_AdDSX1CommonRollingCountLESs_Type = Counter32
_AdDSX1CommonRollingCountLESs_Object = MibTableColumn
adDSX1CommonRollingCountLESs = _AdDSX1CommonRollingCountLESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 7),
    _AdDSX1CommonRollingCountLESs_Type()
)
adDSX1CommonRollingCountLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountLESs.setStatus("current")
_AdDSX1CommonRollingCountBESs_Type = Counter32
_AdDSX1CommonRollingCountBESs_Object = MibTableColumn
adDSX1CommonRollingCountBESs = _AdDSX1CommonRollingCountBESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 8),
    _AdDSX1CommonRollingCountBESs_Type()
)
adDSX1CommonRollingCountBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountBESs.setStatus("current")
_AdDSX1CommonRollingCountDMs_Type = Counter32
_AdDSX1CommonRollingCountDMs_Object = MibTableColumn
adDSX1CommonRollingCountDMs = _AdDSX1CommonRollingCountDMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 9),
    _AdDSX1CommonRollingCountDMs_Type()
)
adDSX1CommonRollingCountDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountDMs.setStatus("current")
_AdDSX1CommonRollingCountLCVs_Type = Counter32
_AdDSX1CommonRollingCountLCVs_Object = MibTableColumn
adDSX1CommonRollingCountLCVs = _AdDSX1CommonRollingCountLCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 10),
    _AdDSX1CommonRollingCountLCVs_Type()
)
adDSX1CommonRollingCountLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountLCVs.setStatus("current")


class _AdDSX1CommonRollingCountReset_Type(Integer32):
    """Custom type adDSX1CommonRollingCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdDSX1CommonRollingCountReset_Type.__name__ = "Integer32"
_AdDSX1CommonRollingCountReset_Object = MibTableColumn
adDSX1CommonRollingCountReset = _AdDSX1CommonRollingCountReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 7, 4, 1, 11),
    _AdDSX1CommonRollingCountReset_Type()
)
adDSX1CommonRollingCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonRollingCountReset.setStatus("current")
_AdDSX1CommonDailyPm_ObjectIdentity = ObjectIdentity
adDSX1CommonDailyPm = _AdDSX1CommonDailyPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 8)
)
_AdDSX1CommonPmResetTable_Object = MibTable
adDSX1CommonPmResetTable = _AdDSX1CommonPmResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 8, 1)
)
if mibBuilder.loadTexts:
    adDSX1CommonPmResetTable.setStatus("current")
_AdDSX1CommonPmResetEntry_Object = MibTableRow
adDSX1CommonPmResetEntry = _AdDSX1CommonPmResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 8, 1, 1)
)
adDSX1CommonPmResetEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonPmResetEntry.setStatus("current")


class _AdDSX1CommonPmReset_Type(Integer32):
    """Custom type adDSX1CommonPmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdDSX1CommonPmReset_Type.__name__ = "Integer32"
_AdDSX1CommonPmReset_Object = MibTableColumn
adDSX1CommonPmReset = _AdDSX1CommonPmReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 8, 1, 1, 1),
    _AdDSX1CommonPmReset_Type()
)
adDSX1CommonPmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adDSX1CommonPmReset.setStatus("current")
_AdDSX1CommonModuleInfo_ObjectIdentity = ObjectIdentity
adDSX1CommonModuleInfo = _AdDSX1CommonModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 9)
)
_AdDSX1CommonModuleInfoTable_Object = MibTable
adDSX1CommonModuleInfoTable = _AdDSX1CommonModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 9, 1)
)
if mibBuilder.loadTexts:
    adDSX1CommonModuleInfoTable.setStatus("current")
_AdDSX1CommonModuleInfoEntry_Object = MibTableRow
adDSX1CommonModuleInfoEntry = _AdDSX1CommonModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 9, 1, 1)
)
adDSX1CommonModuleInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adDSX1CommonModuleInfoEntry.setStatus("current")


class _AdDSX1CommonModuleT1E1Mode_Type(Integer32):
    """Custom type adDSX1CommonModuleT1E1Mode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1", 1),
          ("e1", 2))
    )


_AdDSX1CommonModuleT1E1Mode_Type.__name__ = "Integer32"
_AdDSX1CommonModuleT1E1Mode_Object = MibTableColumn
adDSX1CommonModuleT1E1Mode = _AdDSX1CommonModuleT1E1Mode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 9, 1, 1, 1),
    _AdDSX1CommonModuleT1E1Mode_Type()
)
adDSX1CommonModuleT1E1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adDSX1CommonModuleT1E1Mode.setStatus("current")

# Managed Objects groups

adDSX1CommonProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6, 1, 1)
)
adDSX1CommonProvGroup.setObjects(
      *(("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvLBO"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvFrame"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvInbandLoopback"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvBPVRatio"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvAutoFailoverLOS"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvAutoFailoverLOF"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvAutoFailoverBERThresh"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvT1OpState"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvRAI"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonProvEBit"))
)
if mibBuilder.loadTexts:
    adDSX1CommonProvGroup.setStatus("current")

adDSX1CommonAlmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6, 1, 2)
)
adDSX1CommonAlmGroup.setObjects(
      *(("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmSetThrsDefaults"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmEnableAllThrsAlarms"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmDisableAllThrsAlarms"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmResetPerfMonRegisters"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsEnable"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsEnable"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsEnable"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsEnable"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsESP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsSESP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsSEFSP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsUASP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsCSS"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsCVP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsESL"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsSESL"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsESBP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsDGRM"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearQtrThrsCVL"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsESPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsSESPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsSEFSPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsUASPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsCSSPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsCVPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsESLFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsESBPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarQtrThrsDGRMPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsESP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsSESP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsSEFSP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsUASP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsCSS"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsCVP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsESL"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsSESL"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsESBP"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsDGRM"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmNearDayThrsCVL"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsESPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsSESPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsSEFSPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsUASPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsCSSPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsCVPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsESLFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsESBPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmFarDayThrsDGRMPFE"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonAlmPHTLThrsEnable"))
)
if mibBuilder.loadTexts:
    adDSX1CommonAlmGroup.setStatus("current")

adDSX1CommonTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6, 1, 3)
)
adDSX1CommonTestGroup.setObjects(
    ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonTestFarEndLoopback")
)
if mibBuilder.loadTexts:
    adDSX1CommonTestGroup.setStatus("current")

adDSX1CommonStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6, 1, 4)
)
adDSX1CommonStatusGroup.setObjects(
    ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonStatusLoopStatus")
)
if mibBuilder.loadTexts:
    adDSX1CommonStatusGroup.setStatus("current")

adDSX1CommonSLC2PerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6, 1, 5)
)
adDSX1CommonSLC2PerfGroup.setObjects(
      *(("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonSLC2PerfMonBlockCall"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonSLC2PerfMonAllTrunkBusy"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonSLC2PerfMonNailedTimeSlot"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonSLC2PerfMonPHTL"),
        ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonSLC2PerfMonPHTLThreshold"))
)
if mibBuilder.loadTexts:
    adDSX1CommonSLC2PerfGroup.setStatus("current")

adDSX1CommonDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6, 1, 6)
)
adDSX1CommonDeprecatedGroup.setObjects(
    ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonTestT1ProtectSelect")
)
if mibBuilder.loadTexts:
    adDSX1CommonDeprecatedGroup.setStatus("deprecated")

adDSX1CommonPmResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6, 1, 8)
)
adDSX1CommonPmResetGroup.setObjects(
    ("ADTRAN-DSX1COMMON-MIB", "adDSX1CommonPmReset")
)
if mibBuilder.loadTexts:
    adDSX1CommonPmResetGroup.setStatus("current")


# Notification objects

dsx1almNearQtrThrsESPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002101)
)
dsx1almNearQtrThrsESPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsESPexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsSESPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002103)
)
dsx1almNearQtrThrsSESPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsSESPexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsSEFSPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002105)
)
dsx1almNearQtrThrsSEFSPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsSEFSPexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsUASPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002107)
)
dsx1almNearQtrThrsUASPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsUASPexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsCSSexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002109)
)
dsx1almNearQtrThrsCSSexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsCSSexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsCVPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002111)
)
dsx1almNearQtrThrsCVPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsCVPexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsESLexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002113)
)
dsx1almNearQtrThrsESLexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsESLexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsSESLexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002115)
)
dsx1almNearQtrThrsSESLexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsSESLexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsESBPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002117)
)
dsx1almNearQtrThrsESBPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsESBPexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsDGRMexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002119)
)
dsx1almNearQtrThrsDGRMexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsDGRMexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsCVLexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002121)
)
dsx1almNearQtrThrsCVLexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsCVLexeed.setStatus(
        "current"
    )

dsx1almFarQtrThrsESPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002123)
)
dsx1almFarQtrThrsESPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarQtrThrsESPFEexeed.setStatus(
        "current"
    )

dsx1almFarQtrThrsSESPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002125)
)
dsx1almFarQtrThrsSESPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarQtrThrsSESPFEexeed.setStatus(
        "current"
    )

dsx1almFarQtrThrsSEFSPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002127)
)
dsx1almFarQtrThrsSEFSPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarQtrThrsSEFSPFEexeed.setStatus(
        "current"
    )

dsx1almFarQtrThrsuUASPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002129)
)
dsx1almFarQtrThrsuUASPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarQtrThrsuUASPFEexeed.setStatus(
        "current"
    )

dsx1almFarQtrThrsCSSPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002131)
)
dsx1almFarQtrThrsCSSPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarQtrThrsCSSPFEexeed.setStatus(
        "current"
    )

dsx1almFarQtrThrsCVPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002133)
)
dsx1almFarQtrThrsCVPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarQtrThrsCVPFEexeed.setStatus(
        "current"
    )

dsx1almFarQtrThrsESLFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002135)
)
dsx1almFarQtrThrsESLFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarQtrThrsESLFEexeed.setStatus(
        "current"
    )

dsx1almFarQtrThrsESBPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002137)
)
dsx1almFarQtrThrsESBPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarQtrThrsESBPFEexeed.setStatus(
        "current"
    )

dsx1almFarQtrThrsDGRMPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002139)
)
dsx1almFarQtrThrsDGRMPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarQtrThrsDGRMPFEexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsESPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002141)
)
dsx1almNearDayThrsESPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsESPexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsSESPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002143)
)
dsx1almNearDayThrsSESPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsSESPexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsSEFSPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002145)
)
dsx1almNearDayThrsSEFSPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsSEFSPexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsUASPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002147)
)
dsx1almNearDayThrsUASPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsUASPexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsCSSexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002149)
)
dsx1almNearDayThrsCSSexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsCSSexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsCVPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002151)
)
dsx1almNearDayThrsCVPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsCVPexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsESLexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002153)
)
dsx1almNearDayThrsESLexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsESLexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsSESLexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002155)
)
dsx1almNearDayThrsSESLexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsSESLexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsESBPexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002157)
)
dsx1almNearDayThrsESBPexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsESBPexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsDGRMexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002159)
)
dsx1almNearDayThrsDGRMexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsDGRMexeed.setStatus(
        "current"
    )

dsx1almNearDayThrsCVLexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002161)
)
dsx1almNearDayThrsCVLexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearDayThrsCVLexeed.setStatus(
        "current"
    )

dsx1almFarDayThrsESPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002163)
)
dsx1almFarDayThrsESPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarDayThrsESPFEexeed.setStatus(
        "current"
    )

dsx1almFarDayThrsSESFPEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002165)
)
dsx1almFarDayThrsSESFPEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarDayThrsSESFPEexeed.setStatus(
        "current"
    )

dsx1almFarDayThrsSEFSPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002167)
)
dsx1almFarDayThrsSEFSPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarDayThrsSEFSPFEexeed.setStatus(
        "current"
    )

dsx1almFarDayThrsUASPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002169)
)
dsx1almFarDayThrsUASPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarDayThrsUASPFEexeed.setStatus(
        "current"
    )

dsx1almFarDayThrsCSSPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002171)
)
dsx1almFarDayThrsCSSPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarDayThrsCSSPFEexeed.setStatus(
        "current"
    )

dsx1almFarDayThrsCVPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002173)
)
dsx1almFarDayThrsCVPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarDayThrsCVPFEexeed.setStatus(
        "current"
    )

dsx1almFarDayThrsESLFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002175)
)
dsx1almFarDayThrsESLFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarDayThrsESLFEexeed.setStatus(
        "current"
    )

dsx1almFarDayThrsESBPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002177)
)
dsx1almFarDayThrsESBPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarDayThrsESBPFEexeed.setStatus(
        "current"
    )

dsx1almFarDayThrsDGRMPFEexeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002179)
)
dsx1almFarDayThrsDGRMPFEexeed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almFarDayThrsDGRMPFEexeed.setStatus(
        "current"
    )

dsx1almNearQtrThrsCVPRemoteExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002181)
)
dsx1almNearQtrThrsCVPRemoteExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsCVPRemoteExceeded.setStatus(
        "current"
    )

dsx1almNearQtrThrsESPRemoteExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002183)
)
dsx1almNearQtrThrsESPRemoteExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsESPRemoteExceeded.setStatus(
        "current"
    )

dsx1almNearQtrThrsSESPRemoteExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002185)
)
dsx1almNearQtrThrsSESPRemoteExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsSESPRemoteExceeded.setStatus(
        "current"
    )

dsx1almNearQtrThrsUASPRemoteExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002187)
)
dsx1almNearQtrThrsUASPRemoteExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsUASPRemoteExceeded.setStatus(
        "current"
    )

dsx1almNearQtrThrsCVLRemoteExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002189)
)
dsx1almNearQtrThrsCVLRemoteExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsCVLRemoteExceeded.setStatus(
        "current"
    )

dsx1almNearQtrThrsESLRemoteExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002191)
)
dsx1almNearQtrThrsESLRemoteExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsESLRemoteExceeded.setStatus(
        "current"
    )

dsx1almNearQtrThrsESBPRemoteExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002193)
)
dsx1almNearQtrThrsESBPRemoteExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsESBPRemoteExceeded.setStatus(
        "current"
    )

dsx1almNearQtrThrsCSSPRemoteExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002195)
)
dsx1almNearQtrThrsCSSPRemoteExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsCSSPRemoteExceeded.setStatus(
        "current"
    )

dsx1almNearQtrThrsSEFSPRemoteExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 0, 1002197)
)
dsx1almNearQtrThrsSEFSPRemoteExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"))
)
if mibBuilder.loadTexts:
    dsx1almNearQtrThrsSEFSPRemoteExceeded.setStatus(
        "current"
    )


# Notifications groups

adDSX1CommonEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 21, 6, 1, 7)
)
adDSX1CommonEventGroup.setObjects(
      *(("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsESPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsSESPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsSEFSPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsUASPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsCSSexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsCVPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsESLexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsSESLexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsESBPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsDGRMexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsCVLexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarQtrThrsESPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarQtrThrsSESPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarQtrThrsSEFSPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarQtrThrsuUASPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarQtrThrsCSSPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarQtrThrsCVPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarQtrThrsESLFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarQtrThrsESBPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarQtrThrsDGRMPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsESPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsSESPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsSEFSPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsUASPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsCSSexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsCVPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsESLexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsSESLexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsESBPexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsDGRMexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearDayThrsCVLexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarDayThrsESPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarDayThrsSESFPEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarDayThrsSEFSPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarDayThrsUASPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarDayThrsCSSPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarDayThrsCVPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarDayThrsESLFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarDayThrsESBPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almFarDayThrsDGRMPFEexeed"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsCVPRemoteExceeded"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsESPRemoteExceeded"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsSESPRemoteExceeded"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsUASPRemoteExceeded"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsCVLRemoteExceeded"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsESLRemoteExceeded"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsESBPRemoteExceeded"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsCSSPRemoteExceeded"),
        ("ADTRAN-DSX1COMMON-MIB", "dsx1almNearQtrThrsSEFSPRemoteExceeded"))
)
if mibBuilder.loadTexts:
    adDSX1CommonEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-DSX1COMMON-MIB",
    **{"adDSX1Common": adDSX1Common,
       "adDSX1CommonAlm": adDSX1CommonAlm,
       "dsx1almNearQtrThrsESPexeed": dsx1almNearQtrThrsESPexeed,
       "dsx1almNearQtrThrsSESPexeed": dsx1almNearQtrThrsSESPexeed,
       "dsx1almNearQtrThrsSEFSPexeed": dsx1almNearQtrThrsSEFSPexeed,
       "dsx1almNearQtrThrsUASPexeed": dsx1almNearQtrThrsUASPexeed,
       "dsx1almNearQtrThrsCSSexeed": dsx1almNearQtrThrsCSSexeed,
       "dsx1almNearQtrThrsCVPexeed": dsx1almNearQtrThrsCVPexeed,
       "dsx1almNearQtrThrsESLexeed": dsx1almNearQtrThrsESLexeed,
       "dsx1almNearQtrThrsSESLexeed": dsx1almNearQtrThrsSESLexeed,
       "dsx1almNearQtrThrsESBPexeed": dsx1almNearQtrThrsESBPexeed,
       "dsx1almNearQtrThrsDGRMexeed": dsx1almNearQtrThrsDGRMexeed,
       "dsx1almNearQtrThrsCVLexeed": dsx1almNearQtrThrsCVLexeed,
       "dsx1almFarQtrThrsESPFEexeed": dsx1almFarQtrThrsESPFEexeed,
       "dsx1almFarQtrThrsSESPFEexeed": dsx1almFarQtrThrsSESPFEexeed,
       "dsx1almFarQtrThrsSEFSPFEexeed": dsx1almFarQtrThrsSEFSPFEexeed,
       "dsx1almFarQtrThrsuUASPFEexeed": dsx1almFarQtrThrsuUASPFEexeed,
       "dsx1almFarQtrThrsCSSPFEexeed": dsx1almFarQtrThrsCSSPFEexeed,
       "dsx1almFarQtrThrsCVPFEexeed": dsx1almFarQtrThrsCVPFEexeed,
       "dsx1almFarQtrThrsESLFEexeed": dsx1almFarQtrThrsESLFEexeed,
       "dsx1almFarQtrThrsESBPFEexeed": dsx1almFarQtrThrsESBPFEexeed,
       "dsx1almFarQtrThrsDGRMPFEexeed": dsx1almFarQtrThrsDGRMPFEexeed,
       "dsx1almNearDayThrsESPexeed": dsx1almNearDayThrsESPexeed,
       "dsx1almNearDayThrsSESPexeed": dsx1almNearDayThrsSESPexeed,
       "dsx1almNearDayThrsSEFSPexeed": dsx1almNearDayThrsSEFSPexeed,
       "dsx1almNearDayThrsUASPexeed": dsx1almNearDayThrsUASPexeed,
       "dsx1almNearDayThrsCSSexeed": dsx1almNearDayThrsCSSexeed,
       "dsx1almNearDayThrsCVPexeed": dsx1almNearDayThrsCVPexeed,
       "dsx1almNearDayThrsESLexeed": dsx1almNearDayThrsESLexeed,
       "dsx1almNearDayThrsSESLexeed": dsx1almNearDayThrsSESLexeed,
       "dsx1almNearDayThrsESBPexeed": dsx1almNearDayThrsESBPexeed,
       "dsx1almNearDayThrsDGRMexeed": dsx1almNearDayThrsDGRMexeed,
       "dsx1almNearDayThrsCVLexeed": dsx1almNearDayThrsCVLexeed,
       "dsx1almFarDayThrsESPFEexeed": dsx1almFarDayThrsESPFEexeed,
       "dsx1almFarDayThrsSESFPEexeed": dsx1almFarDayThrsSESFPEexeed,
       "dsx1almFarDayThrsSEFSPFEexeed": dsx1almFarDayThrsSEFSPFEexeed,
       "dsx1almFarDayThrsUASPFEexeed": dsx1almFarDayThrsUASPFEexeed,
       "dsx1almFarDayThrsCSSPFEexeed": dsx1almFarDayThrsCSSPFEexeed,
       "dsx1almFarDayThrsCVPFEexeed": dsx1almFarDayThrsCVPFEexeed,
       "dsx1almFarDayThrsESLFEexeed": dsx1almFarDayThrsESLFEexeed,
       "dsx1almFarDayThrsESBPFEexeed": dsx1almFarDayThrsESBPFEexeed,
       "dsx1almFarDayThrsDGRMPFEexeed": dsx1almFarDayThrsDGRMPFEexeed,
       "dsx1almNearQtrThrsCVPRemoteExceeded": dsx1almNearQtrThrsCVPRemoteExceeded,
       "dsx1almNearQtrThrsESPRemoteExceeded": dsx1almNearQtrThrsESPRemoteExceeded,
       "dsx1almNearQtrThrsSESPRemoteExceeded": dsx1almNearQtrThrsSESPRemoteExceeded,
       "dsx1almNearQtrThrsUASPRemoteExceeded": dsx1almNearQtrThrsUASPRemoteExceeded,
       "dsx1almNearQtrThrsCVLRemoteExceeded": dsx1almNearQtrThrsCVLRemoteExceeded,
       "dsx1almNearQtrThrsESLRemoteExceeded": dsx1almNearQtrThrsESLRemoteExceeded,
       "dsx1almNearQtrThrsESBPRemoteExceeded": dsx1almNearQtrThrsESBPRemoteExceeded,
       "dsx1almNearQtrThrsCSSPRemoteExceeded": dsx1almNearQtrThrsCSSPRemoteExceeded,
       "dsx1almNearQtrThrsSEFSPRemoteExceeded": dsx1almNearQtrThrsSEFSPRemoteExceeded,
       "adDSX1CommonProv": adDSX1CommonProv,
       "adDSX1CommonProvTable": adDSX1CommonProvTable,
       "adDSX1CommonProvEntry": adDSX1CommonProvEntry,
       "adDSX1CommonProvLBO": adDSX1CommonProvLBO,
       "adDSX1CommonProvFrame": adDSX1CommonProvFrame,
       "adDSX1CommonProvInbandLoopback": adDSX1CommonProvInbandLoopback,
       "adDSX1CommonProvBPVRatio": adDSX1CommonProvBPVRatio,
       "adDSX1CommonProvAutoFailoverLOS": adDSX1CommonProvAutoFailoverLOS,
       "adDSX1CommonProvAutoFailoverLOF": adDSX1CommonProvAutoFailoverLOF,
       "adDSX1CommonProvAutoFailoverBERThresh": adDSX1CommonProvAutoFailoverBERThresh,
       "adDSX1CommonProvT1OpState": adDSX1CommonProvT1OpState,
       "adDSX1CommonProvRAI": adDSX1CommonProvRAI,
       "adDSX1CommonProvEBit": adDSX1CommonProvEBit,
       "adDSX1CommonAlmProv": adDSX1CommonAlmProv,
       "adDSX1CommonAlmTable": adDSX1CommonAlmTable,
       "adDSX1CommonAlmEntry": adDSX1CommonAlmEntry,
       "adDSX1CommonAlmSetThrsDefaults": adDSX1CommonAlmSetThrsDefaults,
       "adDSX1CommonAlmEnableAllThrsAlarms": adDSX1CommonAlmEnableAllThrsAlarms,
       "adDSX1CommonAlmDisableAllThrsAlarms": adDSX1CommonAlmDisableAllThrsAlarms,
       "adDSX1CommonAlmResetPerfMonRegisters": adDSX1CommonAlmResetPerfMonRegisters,
       "adDSX1CommonAlmNearQtrThrsEnable": adDSX1CommonAlmNearQtrThrsEnable,
       "adDSX1CommonAlmNearDayThrsEnable": adDSX1CommonAlmNearDayThrsEnable,
       "adDSX1CommonAlmFarQtrThrsEnable": adDSX1CommonAlmFarQtrThrsEnable,
       "adDSX1CommonAlmFarDayThrsEnable": adDSX1CommonAlmFarDayThrsEnable,
       "adDSX1CommonAlmNearQtrThrsESP": adDSX1CommonAlmNearQtrThrsESP,
       "adDSX1CommonAlmNearQtrThrsSESP": adDSX1CommonAlmNearQtrThrsSESP,
       "adDSX1CommonAlmNearQtrThrsSEFSP": adDSX1CommonAlmNearQtrThrsSEFSP,
       "adDSX1CommonAlmNearQtrThrsUASP": adDSX1CommonAlmNearQtrThrsUASP,
       "adDSX1CommonAlmNearQtrThrsCSS": adDSX1CommonAlmNearQtrThrsCSS,
       "adDSX1CommonAlmNearQtrThrsCVP": adDSX1CommonAlmNearQtrThrsCVP,
       "adDSX1CommonAlmNearQtrThrsESL": adDSX1CommonAlmNearQtrThrsESL,
       "adDSX1CommonAlmNearQtrThrsSESL": adDSX1CommonAlmNearQtrThrsSESL,
       "adDSX1CommonAlmNearQtrThrsESBP": adDSX1CommonAlmNearQtrThrsESBP,
       "adDSX1CommonAlmNearQtrThrsDGRM": adDSX1CommonAlmNearQtrThrsDGRM,
       "adDSX1CommonAlmNearQtrThrsCVL": adDSX1CommonAlmNearQtrThrsCVL,
       "adDSX1CommonAlmFarQtrThrsESPFE": adDSX1CommonAlmFarQtrThrsESPFE,
       "adDSX1CommonAlmFarQtrThrsSESPFE": adDSX1CommonAlmFarQtrThrsSESPFE,
       "adDSX1CommonAlmFarQtrThrsSEFSPFE": adDSX1CommonAlmFarQtrThrsSEFSPFE,
       "adDSX1CommonAlmFarQtrThrsUASPFE": adDSX1CommonAlmFarQtrThrsUASPFE,
       "adDSX1CommonAlmFarQtrThrsCSSPFE": adDSX1CommonAlmFarQtrThrsCSSPFE,
       "adDSX1CommonAlmFarQtrThrsCVPFE": adDSX1CommonAlmFarQtrThrsCVPFE,
       "adDSX1CommonAlmFarQtrThrsESLFE": adDSX1CommonAlmFarQtrThrsESLFE,
       "adDSX1CommonAlmFarQtrThrsESBPFE": adDSX1CommonAlmFarQtrThrsESBPFE,
       "adDSX1CommonAlmFarQtrThrsDGRMPFE": adDSX1CommonAlmFarQtrThrsDGRMPFE,
       "adDSX1CommonAlmNearDayThrsESP": adDSX1CommonAlmNearDayThrsESP,
       "adDSX1CommonAlmNearDayThrsSESP": adDSX1CommonAlmNearDayThrsSESP,
       "adDSX1CommonAlmNearDayThrsSEFSP": adDSX1CommonAlmNearDayThrsSEFSP,
       "adDSX1CommonAlmNearDayThrsUASP": adDSX1CommonAlmNearDayThrsUASP,
       "adDSX1CommonAlmNearDayThrsCSS": adDSX1CommonAlmNearDayThrsCSS,
       "adDSX1CommonAlmNearDayThrsCVP": adDSX1CommonAlmNearDayThrsCVP,
       "adDSX1CommonAlmNearDayThrsESL": adDSX1CommonAlmNearDayThrsESL,
       "adDSX1CommonAlmNearDayThrsSESL": adDSX1CommonAlmNearDayThrsSESL,
       "adDSX1CommonAlmNearDayThrsESBP": adDSX1CommonAlmNearDayThrsESBP,
       "adDSX1CommonAlmNearDayThrsDGRM": adDSX1CommonAlmNearDayThrsDGRM,
       "adDSX1CommonAlmNearDayThrsCVL": adDSX1CommonAlmNearDayThrsCVL,
       "adDSX1CommonAlmFarDayThrsESPFE": adDSX1CommonAlmFarDayThrsESPFE,
       "adDSX1CommonAlmFarDayThrsSESPFE": adDSX1CommonAlmFarDayThrsSESPFE,
       "adDSX1CommonAlmFarDayThrsSEFSPFE": adDSX1CommonAlmFarDayThrsSEFSPFE,
       "adDSX1CommonAlmFarDayThrsUASPFE": adDSX1CommonAlmFarDayThrsUASPFE,
       "adDSX1CommonAlmFarDayThrsCSSPFE": adDSX1CommonAlmFarDayThrsCSSPFE,
       "adDSX1CommonAlmFarDayThrsCVPFE": adDSX1CommonAlmFarDayThrsCVPFE,
       "adDSX1CommonAlmFarDayThrsESLFE": adDSX1CommonAlmFarDayThrsESLFE,
       "adDSX1CommonAlmFarDayThrsESBPFE": adDSX1CommonAlmFarDayThrsESBPFE,
       "adDSX1CommonAlmFarDayThrsDGRMPFE": adDSX1CommonAlmFarDayThrsDGRMPFE,
       "adDSX1CommonAlmPHTLThrsEnable": adDSX1CommonAlmPHTLThrsEnable,
       "adDSX1CommonEnhancedAlmSlotTable": adDSX1CommonEnhancedAlmSlotTable,
       "adDSX1CommonEnhancedAlmSlotEntry": adDSX1CommonEnhancedAlmSlotEntry,
       "adDSX1CommonEnhancedAlmSlotSALOSSeverity": adDSX1CommonEnhancedAlmSlotSALOSSeverity,
       "adDSX1CommonEnhancedAlmSlotSALOSSuppression": adDSX1CommonEnhancedAlmSlotSALOSSuppression,
       "adDSX1CommonEnhancedAlmSlotSALOFSeverity": adDSX1CommonEnhancedAlmSlotSALOFSeverity,
       "adDSX1CommonEnhancedAlmSlotSALOFSuppression": adDSX1CommonEnhancedAlmSlotSALOFSuppression,
       "adDSX1CommonEnhancedAlmSlotSAAISSeverity": adDSX1CommonEnhancedAlmSlotSAAISSeverity,
       "adDSX1CommonEnhancedAlmSlotSAAISSSuppression": adDSX1CommonEnhancedAlmSlotSAAISSSuppression,
       "adDSX1CommonEnhancedAlmSlotSARAISeverity": adDSX1CommonEnhancedAlmSlotSARAISeverity,
       "adDSX1CommonEnhancedAlmSlotSARAISuppression": adDSX1CommonEnhancedAlmSlotSARAISuppression,
       "adDSX1CommonEnhancedAlmSlotSALOSEnable": adDSX1CommonEnhancedAlmSlotSALOSEnable,
       "adDSX1CommonEnhancedAlmSlotSALOFEnable": adDSX1CommonEnhancedAlmSlotSALOFEnable,
       "adDSX1CommonEnhancedAlmSlotSAAISEnable": adDSX1CommonEnhancedAlmSlotSAAISEnable,
       "adDSX1CommonEnhancedAlmSlotSARAIEnable": adDSX1CommonEnhancedAlmSlotSARAIEnable,
       "adDSX1CommonTest": adDSX1CommonTest,
       "adDSX1CommonTestTable": adDSX1CommonTestTable,
       "adDSX1CommonTestEntry": adDSX1CommonTestEntry,
       "adDSX1CommonTestFarEndLoopback": adDSX1CommonTestFarEndLoopback,
       "adDSX1CommonTestT1ProtectSelect": adDSX1CommonTestT1ProtectSelect,
       "adDSX1CommonStatus": adDSX1CommonStatus,
       "adDSX1CommonStatusTable": adDSX1CommonStatusTable,
       "adDSX1CommonStatusEntry": adDSX1CommonStatusEntry,
       "adDSX1CommonStatusLoopStatus": adDSX1CommonStatusLoopStatus,
       "adDSX1CommonSLC2PerfMon": adDSX1CommonSLC2PerfMon,
       "adDSX1CommonSLC2PerfMonTable": adDSX1CommonSLC2PerfMonTable,
       "adDSX1CommonSLC2PerfMonEntry": adDSX1CommonSLC2PerfMonEntry,
       "adDSX1CommonSLC2PerfMonBlockCall": adDSX1CommonSLC2PerfMonBlockCall,
       "adDSX1CommonSLC2PerfMonAllTrunkBusy": adDSX1CommonSLC2PerfMonAllTrunkBusy,
       "adDSX1CommonSLC2PerfMonNailedTimeSlot": adDSX1CommonSLC2PerfMonNailedTimeSlot,
       "adDSX1CommonSLC2PerfMonPHTL": adDSX1CommonSLC2PerfMonPHTL,
       "adDSX1CommonSLC2PerfMonPHTLThreshold": adDSX1CommonSLC2PerfMonPHTLThreshold,
       "adDSX1CommonMibConformance": adDSX1CommonMibConformance,
       "adDSX1CommonMibGroups": adDSX1CommonMibGroups,
       "adDSX1CommonProvGroup": adDSX1CommonProvGroup,
       "adDSX1CommonAlmGroup": adDSX1CommonAlmGroup,
       "adDSX1CommonTestGroup": adDSX1CommonTestGroup,
       "adDSX1CommonStatusGroup": adDSX1CommonStatusGroup,
       "adDSX1CommonSLC2PerfGroup": adDSX1CommonSLC2PerfGroup,
       "adDSX1CommonDeprecatedGroup": adDSX1CommonDeprecatedGroup,
       "adDSX1CommonEventGroup": adDSX1CommonEventGroup,
       "adDSX1CommonPmResetGroup": adDSX1CommonPmResetGroup,
       "adDSX1CommonDailyPmInt": adDSX1CommonDailyPmInt,
       "adDSX1CommonDailyPmIntervalTable": adDSX1CommonDailyPmIntervalTable,
       "adDSX1CommonDailyPmIntervalEntry": adDSX1CommonDailyPmIntervalEntry,
       "adDSX1CommonDailyPmInterval": adDSX1CommonDailyPmInterval,
       "adDSX1CommonDailyPmESP": adDSX1CommonDailyPmESP,
       "adDSX1CommonDailyPmSESP": adDSX1CommonDailyPmSESP,
       "adDSX1CommonDailyPmUASP": adDSX1CommonDailyPmUASP,
       "adDSX1CommonDailyPmCVP": adDSX1CommonDailyPmCVP,
       "adDSX1CommonDailyPmESL": adDSX1CommonDailyPmESL,
       "adDSX1CommonDailyPmCVL": adDSX1CommonDailyPmCVL,
       "adDSX1CommonCurrentDayTable": adDSX1CommonCurrentDayTable,
       "adDSX1CommonCurrentDayEntry": adDSX1CommonCurrentDayEntry,
       "adDSX1CommonCurrentDayESP": adDSX1CommonCurrentDayESP,
       "adDSX1CommonCurrentDaySESP": adDSX1CommonCurrentDaySESP,
       "adDSX1CommonCurrentDayUASP": adDSX1CommonCurrentDayUASP,
       "adDSX1CommonCurrentDayCVP": adDSX1CommonCurrentDayCVP,
       "adDSX1CommonCurrentDayESL": adDSX1CommonCurrentDayESL,
       "adDSX1CommonCurrentDayCVL": adDSX1CommonCurrentDayCVL,
       "adDSX1CommonTotalTable": adDSX1CommonTotalTable,
       "adDSX1CommonTotalEntry": adDSX1CommonTotalEntry,
       "adDSX1CommonTotalESs": adDSX1CommonTotalESs,
       "adDSX1CommonTotalSESs": adDSX1CommonTotalSESs,
       "adDSX1CommonTotalSEFSs": adDSX1CommonTotalSEFSs,
       "adDSX1CommonTotalUASs": adDSX1CommonTotalUASs,
       "adDSX1CommonTotalCSSs": adDSX1CommonTotalCSSs,
       "adDSX1CommonTotalPCVs": adDSX1CommonTotalPCVs,
       "adDSX1CommonTotalLESs": adDSX1CommonTotalLESs,
       "adDSX1CommonTotalBESs": adDSX1CommonTotalBESs,
       "adDSX1CommonTotalDMs": adDSX1CommonTotalDMs,
       "adDSX1CommonTotalLCVs": adDSX1CommonTotalLCVs,
       "adDSX1CommonRollingCountTable": adDSX1CommonRollingCountTable,
       "adDSX1CommonRollingCountEntry": adDSX1CommonRollingCountEntry,
       "adDSX1CommonRollingCountESs": adDSX1CommonRollingCountESs,
       "adDSX1CommonRollingCountSESs": adDSX1CommonRollingCountSESs,
       "adDSX1CommonRollingCountSEFSs": adDSX1CommonRollingCountSEFSs,
       "adDSX1CommonRollingCountUASs": adDSX1CommonRollingCountUASs,
       "adDSX1CommonRollingCountCSSs": adDSX1CommonRollingCountCSSs,
       "adDSX1CommonRollingCountPCVs": adDSX1CommonRollingCountPCVs,
       "adDSX1CommonRollingCountLESs": adDSX1CommonRollingCountLESs,
       "adDSX1CommonRollingCountBESs": adDSX1CommonRollingCountBESs,
       "adDSX1CommonRollingCountDMs": adDSX1CommonRollingCountDMs,
       "adDSX1CommonRollingCountLCVs": adDSX1CommonRollingCountLCVs,
       "adDSX1CommonRollingCountReset": adDSX1CommonRollingCountReset,
       "adDSX1CommonDailyPm": adDSX1CommonDailyPm,
       "adDSX1CommonPmResetTable": adDSX1CommonPmResetTable,
       "adDSX1CommonPmResetEntry": adDSX1CommonPmResetEntry,
       "adDSX1CommonPmReset": adDSX1CommonPmReset,
       "adDSX1CommonModuleInfo": adDSX1CommonModuleInfo,
       "adDSX1CommonModuleInfoTable": adDSX1CommonModuleInfoTable,
       "adDSX1CommonModuleInfoEntry": adDSX1CommonModuleInfoEntry,
       "adDSX1CommonModuleT1E1Mode": adDSX1CommonModuleT1E1Mode,
       "adDSX1commonModuleIdentity": adDSX1commonModuleIdentity}
)
