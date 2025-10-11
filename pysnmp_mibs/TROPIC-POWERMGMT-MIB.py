# SNMP MIB module (TROPIC-POWERMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-POWERMGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:01:04 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnPowerMgmtMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnPowerMgmtMIB",
    "tnSystemModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmOtuBitRate,
 AluWdmOtuEncoding,
 TnCommand) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmOtuBitRate",
    "AluWdmOtuEncoding",
    "TnCommand")

(tnChannel,
 tnDirection) = mibBuilder.importSymbols(
    "TROPIC-WAVEKEY-MIB",
    "tnChannel",
    "tnDirection")


# MODULE-IDENTITY

tnPowerMgmtMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnPowerMgmtMibModule.setRevisions(
        ("2020-12-11 12:00",
         "2020-06-12 12:00",
         "2020-05-15 12:00",
         "2020-03-27 12:00",
         "2020-03-20 12:00",
         "2020-03-06 12:00",
         "2020-02-14 12:00",
         "2019-05-17 12:00",
         "2018-11-09 12:00",
         "2018-09-14 12:00",
         "2018-06-22 12:00",
         "2018-02-23 12:00",
         "2017-09-29 12:00",
         "2017-03-17 12:00",
         "2017-03-10 12:00",
         "2017-02-24 12:00",
         "2017-02-10 12:00",
         "2017-01-27 12:00",
         "2016-12-28 12:00",
         "2016-12-19 12:00",
         "2016-11-16 12:00",
         "2016-11-11 12:00",
         "2016-09-16 12:00",
         "2015-11-04 12:00",
         "2014-11-19 12:00",
         "2014-11-07 12:00",
         "2014-09-10 12:00",
         "2013-12-06 12:00",
         "2013-11-25 12:00",
         "2013-05-20 12:00",
         "2013-01-10 12:00",
         "2012-11-05 12:00",
         "2012-09-01 12:00",
         "2012-06-13 12:00",
         "2012-05-18 12:00",
         "2012-01-04 12:00",
         "2011-12-14 12:00",
         "2011-11-26 12:00",
         "2011-11-21 12:00",
         "2011-11-05 12:00",
         "2011-08-12 12:00",
         "2011-08-03 12:00",
         "2011-07-29 12:00",
         "2011-07-22 12:00",
         "2011-05-23 12:00",
         "2011-04-03 12:00",
         "2010-11-10 12:00",
         "2010-06-23 12:00",
         "2010-06-16 12:00",
         "2010-05-10 12:00",
         "2008-10-16 12:00",
         "2008-02-16 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicPowerMgmtStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("completed", 1),
          ("inProgress", 2))
    )



class TropicPowerMgmtResult(SnmpAdminString):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TropicPowerMgmtPercentCompleted(TextualConvention, Unsigned32):
    status = "current"


class TropicPowerMgmtType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )



class AluWdmWTDecoderUsageType(TextualConvention, Integer32):
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
        *(("wtdPpcOnAlmOn", 1),
          ("wtdPpcOffAlmOff", 2),
          ("wtdPpcOnAlmOff", 3),
          ("wtocm", 4),
          ("wtdInferred", 5),
          ("wtocmAd", 6),
          ("maint", 7))
    )



class AluWdmPowerMgmtSRSTiltAdjStatus(TextualConvention, Integer32):
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
        *(("completed", 1),
          ("inProgress", 2),
          ("notInProgress", 3))
    )



class TropicPowerMgmtCapabilitiesCard(TextualConvention, Integer32):
    status = "current"
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
          ("runadjustgetstatusresul", 2),
          ("configandrunadjustgetstatusresult", 3),
          ("getstatusresult", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TnPowerMgmtConf_ObjectIdentity = ObjectIdentity
tnPowerMgmtConf = _TnPowerMgmtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1)
)
_TnPowerMgmtGroups_ObjectIdentity = ObjectIdentity
tnPowerMgmtGroups = _TnPowerMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1)
)
_TnPowerMgmtCompliances_ObjectIdentity = ObjectIdentity
tnPowerMgmtCompliances = _TnPowerMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 2)
)
_TnPowerMgmtObjs_ObjectIdentity = ObjectIdentity
tnPowerMgmtObjs = _TnPowerMgmtObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2)
)
_TnPowerMgmtBasics_ObjectIdentity = ObjectIdentity
tnPowerMgmtBasics = _TnPowerMgmtBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1)
)
_TnPowerMgmtGlobal_ObjectIdentity = ObjectIdentity
tnPowerMgmtGlobal = _TnPowerMgmtGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1)
)
_TnPowerMgmtGlobalMinStepSize_Type = Unsigned32
_TnPowerMgmtGlobalMinStepSize_Object = MibScalar
tnPowerMgmtGlobalMinStepSize = _TnPowerMgmtGlobalMinStepSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 2),
    _TnPowerMgmtGlobalMinStepSize_Type()
)
tnPowerMgmtGlobalMinStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalMinStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalMinStepSize.setUnits("mB")
_TnPowerMgmtGlobalMaxStepSize_Type = Unsigned32
_TnPowerMgmtGlobalMaxStepSize_Object = MibScalar
tnPowerMgmtGlobalMaxStepSize = _TnPowerMgmtGlobalMaxStepSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 3),
    _TnPowerMgmtGlobalMaxStepSize_Type()
)
tnPowerMgmtGlobalMaxStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalMaxStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalMaxStepSize.setUnits("mB")
_TnPowerMgmtGlobalResetToDefaults_Type = TnCommand
_TnPowerMgmtGlobalResetToDefaults_Object = MibScalar
tnPowerMgmtGlobalResetToDefaults = _TnPowerMgmtGlobalResetToDefaults_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 4),
    _TnPowerMgmtGlobalResetToDefaults_Type()
)
tnPowerMgmtGlobalResetToDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalResetToDefaults.setStatus("current")
_TnPowerMgmtGlobalAutoEnabled_Type = TruthValue
_TnPowerMgmtGlobalAutoEnabled_Object = MibScalar
tnPowerMgmtGlobalAutoEnabled = _TnPowerMgmtGlobalAutoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 5),
    _TnPowerMgmtGlobalAutoEnabled_Type()
)
tnPowerMgmtGlobalAutoEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalAutoEnabled.setStatus("current")
_TnPowerMgmtGlobalNumberOfAutoPowerAdjPoints_Type = Unsigned32
_TnPowerMgmtGlobalNumberOfAutoPowerAdjPoints_Object = MibScalar
tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints = _TnPowerMgmtGlobalNumberOfAutoPowerAdjPoints_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 6),
    _TnPowerMgmtGlobalNumberOfAutoPowerAdjPoints_Type()
)
tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints.setStatus("current")
_TnPowerMgmtGlobalAlarmWhenDisabled_Type = TruthValue
_TnPowerMgmtGlobalAlarmWhenDisabled_Object = MibScalar
tnPowerMgmtGlobalAlarmWhenDisabled = _TnPowerMgmtGlobalAlarmWhenDisabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 1, 7),
    _TnPowerMgmtGlobalAlarmWhenDisabled_Type()
)
tnPowerMgmtGlobalAlarmWhenDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalAlarmWhenDisabled.setStatus("current")
_TnPowerMgmtControlTable_Object = MibTable
tnPowerMgmtControlTable = _TnPowerMgmtControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnPowerMgmtControlTable.setStatus("current")
_TnPowerMgmtControlEntry_Object = MibTableRow
tnPowerMgmtControlEntry = _TnPowerMgmtControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2, 1)
)
tnPowerMgmtControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtDirection"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtControlEntry.setStatus("current")


class _TnPowerMgmtDirection_Type(Integer32):
    """Custom type tnPowerMgmtDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2))
    )


_TnPowerMgmtDirection_Type.__name__ = "Integer32"
_TnPowerMgmtDirection_Object = MibTableColumn
tnPowerMgmtDirection = _TnPowerMgmtDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2, 1, 1),
    _TnPowerMgmtDirection_Type()
)
tnPowerMgmtDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPowerMgmtDirection.setStatus("current")
_TnPowerMgmtControlPercentCompleted_Type = TropicPowerMgmtPercentCompleted
_TnPowerMgmtControlPercentCompleted_Object = MibTableColumn
tnPowerMgmtControlPercentCompleted = _TnPowerMgmtControlPercentCompleted_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2, 1, 3),
    _TnPowerMgmtControlPercentCompleted_Type()
)
tnPowerMgmtControlPercentCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtControlPercentCompleted.setStatus("current")
_TnPowerMgmtControlRowStatus_Type = RowStatus
_TnPowerMgmtControlRowStatus_Object = MibTableColumn
tnPowerMgmtControlRowStatus = _TnPowerMgmtControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 2, 1, 5),
    _TnPowerMgmtControlRowStatus_Type()
)
tnPowerMgmtControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtControlRowStatus.setStatus("current")
_TnPowerMgmtIngressTable_Object = MibTable
tnPowerMgmtIngressTable = _TnPowerMgmtIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressTable.setStatus("current")
_TnPowerMgmtIngressEntry_Object = MibTableRow
tnPowerMgmtIngressEntry = _TnPowerMgmtIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1)
)
tnPowerMgmtIngressEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressEntry.setStatus("current")


class _TnPowerMgmtIngressAdjustPowerGain_Type(Integer32):
    """Custom type tnPowerMgmtIngressAdjustPowerGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("execute", 2),
          ("executeWithForce", 3))
    )


_TnPowerMgmtIngressAdjustPowerGain_Type.__name__ = "Integer32"
_TnPowerMgmtIngressAdjustPowerGain_Object = MibTableColumn
tnPowerMgmtIngressAdjustPowerGain = _TnPowerMgmtIngressAdjustPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 1),
    _TnPowerMgmtIngressAdjustPowerGain_Type()
)
tnPowerMgmtIngressAdjustPowerGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGain.setStatus("current")
_TnPowerMgmtIngressAdjustPowerGainLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtIngressAdjustPowerGainLastResult_Object = MibTableColumn
tnPowerMgmtIngressAdjustPowerGainLastResult = _TnPowerMgmtIngressAdjustPowerGainLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 2),
    _TnPowerMgmtIngressAdjustPowerGainLastResult_Type()
)
tnPowerMgmtIngressAdjustPowerGainLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainLastResult.setStatus("current")


class _TnPowerMgmtIngressAcceptPowers_Type(Integer32):
    """Custom type tnPowerMgmtIngressAcceptPowers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("execute", 2),
          ("executeWithClear", 3))
    )


_TnPowerMgmtIngressAcceptPowers_Type.__name__ = "Integer32"
_TnPowerMgmtIngressAcceptPowers_Object = MibTableColumn
tnPowerMgmtIngressAcceptPowers = _TnPowerMgmtIngressAcceptPowers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 3),
    _TnPowerMgmtIngressAcceptPowers_Type()
)
tnPowerMgmtIngressAcceptPowers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAcceptPowers.setStatus("current")
_TnPowerMgmtIngressAcceptPowersLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtIngressAcceptPowersLastResult_Object = MibTableColumn
tnPowerMgmtIngressAcceptPowersLastResult = _TnPowerMgmtIngressAcceptPowersLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 4),
    _TnPowerMgmtIngressAcceptPowersLastResult_Type()
)
tnPowerMgmtIngressAcceptPowersLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAcceptPowersLastResult.setStatus("current")
_TnPowerMgmtIngressRippleAllowance_Type = Integer32
_TnPowerMgmtIngressRippleAllowance_Object = MibTableColumn
tnPowerMgmtIngressRippleAllowance = _TnPowerMgmtIngressRippleAllowance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 5),
    _TnPowerMgmtIngressRippleAllowance_Type()
)
tnPowerMgmtIngressRippleAllowance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressRippleAllowance.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressRippleAllowance.setUnits("mB")
_TnPowerMgmtIngressAdjustPowerGainTargetGain_Type = Unsigned32
_TnPowerMgmtIngressAdjustPowerGainTargetGain_Object = MibTableColumn
tnPowerMgmtIngressAdjustPowerGainTargetGain = _TnPowerMgmtIngressAdjustPowerGainTargetGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 6),
    _TnPowerMgmtIngressAdjustPowerGainTargetGain_Type()
)
tnPowerMgmtIngressAdjustPowerGainTargetGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainTargetGain.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainTargetGain.setUnits("mB")
_TnPowerMgmtIngressAdjustPowerGainStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtIngressAdjustPowerGainStatus_Object = MibTableColumn
tnPowerMgmtIngressAdjustPowerGainStatus = _TnPowerMgmtIngressAdjustPowerGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 7),
    _TnPowerMgmtIngressAdjustPowerGainStatus_Type()
)
tnPowerMgmtIngressAdjustPowerGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainStatus.setStatus("current")
_TnPowerMgmtIngressStartAseAdjust_Type = TnCommand
_TnPowerMgmtIngressStartAseAdjust_Object = MibTableColumn
tnPowerMgmtIngressStartAseAdjust = _TnPowerMgmtIngressStartAseAdjust_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 8),
    _TnPowerMgmtIngressStartAseAdjust_Type()
)
tnPowerMgmtIngressStartAseAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressStartAseAdjust.setStatus("current")
_TnPowerMgmtIngressAseAdjustLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtIngressAseAdjustLastResult_Object = MibTableColumn
tnPowerMgmtIngressAseAdjustLastResult = _TnPowerMgmtIngressAseAdjustLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 9),
    _TnPowerMgmtIngressAseAdjustLastResult_Type()
)
tnPowerMgmtIngressAseAdjustLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAseAdjustLastResult.setStatus("current")
_TnPowerMgmtIngressAseAdjustStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtIngressAseAdjustStatus_Object = MibTableColumn
tnPowerMgmtIngressAseAdjustStatus = _TnPowerMgmtIngressAseAdjustStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 10),
    _TnPowerMgmtIngressAseAdjustStatus_Type()
)
tnPowerMgmtIngressAseAdjustStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAseAdjustStatus.setStatus("current")


class _TnPowerMgmtIngressCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtIngressCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtIngressCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtIngressCommissioned_Object = MibTableColumn
tnPowerMgmtIngressCommissioned = _TnPowerMgmtIngressCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 11),
    _TnPowerMgmtIngressCommissioned_Type()
)
tnPowerMgmtIngressCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressCommissioned.setStatus("current")


class _TnPowerMgmtIngressGainSetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressGainSetOffset based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressGainSetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressGainSetOffset_Object = MibTableColumn
tnPowerMgmtIngressGainSetOffset = _TnPowerMgmtIngressGainSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 12),
    _TnPowerMgmtIngressGainSetOffset_Type()
)
tnPowerMgmtIngressGainSetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressGainSetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressGainSetOffset.setUnits("mB")


class _TnPowerMgmtIngressCommissionedGain_Type(Integer32):
    """Custom type tnPowerMgmtIngressCommissionedGain based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressCommissionedGain_Type.__name__ = "Integer32"
_TnPowerMgmtIngressCommissionedGain_Object = MibTableColumn
tnPowerMgmtIngressCommissionedGain = _TnPowerMgmtIngressCommissionedGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 13),
    _TnPowerMgmtIngressCommissionedGain_Type()
)
tnPowerMgmtIngressCommissionedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressCommissionedGain.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressCommissionedGain.setUnits("mB")


class _TnPowerMgmtIngressSRSTiltPostFraction_Type(Integer32):
    """Custom type tnPowerMgmtIngressSRSTiltPostFraction based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressSRSTiltPostFraction_Type.__name__ = "Integer32"
_TnPowerMgmtIngressSRSTiltPostFraction_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltPostFraction = _TnPowerMgmtIngressSRSTiltPostFraction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 14),
    _TnPowerMgmtIngressSRSTiltPostFraction_Type()
)
tnPowerMgmtIngressSRSTiltPostFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltPostFraction.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltPostFraction.setUnits("100ths")


class _TnPowerMgmtIngressSRSTiltAdjResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtIngressSRSTiltAdjResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtIngressSRSTiltAdjResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtIngressSRSTiltAdjResult_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltAdjResult = _TnPowerMgmtIngressSRSTiltAdjResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 15),
    _TnPowerMgmtIngressSRSTiltAdjResult_Type()
)
tnPowerMgmtIngressSRSTiltAdjResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltAdjResult.setStatus("current")


class _TnPowerMgmtIngressSRSTiltAdjStatus_Type(AluWdmPowerMgmtSRSTiltAdjStatus):
    """Custom type tnPowerMgmtIngressSRSTiltAdjStatus based on AluWdmPowerMgmtSRSTiltAdjStatus"""
    defaultValue = 3


_TnPowerMgmtIngressSRSTiltAdjStatus_Type.__name__ = "AluWdmPowerMgmtSRSTiltAdjStatus"
_TnPowerMgmtIngressSRSTiltAdjStatus_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltAdjStatus = _TnPowerMgmtIngressSRSTiltAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 16),
    _TnPowerMgmtIngressSRSTiltAdjStatus_Type()
)
tnPowerMgmtIngressSRSTiltAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltAdjStatus.setStatus("current")


class _TnPowerMgmtIngressPassed_Type(TruthValue):
    """Custom type tnPowerMgmtIngressPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtIngressPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtIngressPassed_Object = MibTableColumn
tnPowerMgmtIngressPassed = _TnPowerMgmtIngressPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 17),
    _TnPowerMgmtIngressPassed_Type()
)
tnPowerMgmtIngressPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPassed.setStatus("current")


class _TnPowerMgmtIngressSRSTiltCalcOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressSRSTiltCalcOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtIngressSRSTiltCalcOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressSRSTiltCalcOffset_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltCalcOffset = _TnPowerMgmtIngressSRSTiltCalcOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 18),
    _TnPowerMgmtIngressSRSTiltCalcOffset_Type()
)
tnPowerMgmtIngressSRSTiltCalcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltCalcOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltCalcOffset.setUnits("mB")


class _TnPowerMgmtIngressInternodalOaPpcMaxInCurrent_Type(Integer32):
    """Custom type tnPowerMgmtIngressInternodalOaPpcMaxInCurrent based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressInternodalOaPpcMaxInCurrent_Type.__name__ = "Integer32"
_TnPowerMgmtIngressInternodalOaPpcMaxInCurrent_Object = MibTableColumn
tnPowerMgmtIngressInternodalOaPpcMaxInCurrent = _TnPowerMgmtIngressInternodalOaPpcMaxInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 19),
    _TnPowerMgmtIngressInternodalOaPpcMaxInCurrent_Type()
)
tnPowerMgmtIngressInternodalOaPpcMaxInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressInternodalOaPpcMaxInCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressInternodalOaPpcMaxInCurrent.setUnits("mBm")


class _TnPowerMgmtIngressInternodalOaPpcMaxInReference_Type(Integer32):
    """Custom type tnPowerMgmtIngressInternodalOaPpcMaxInReference based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressInternodalOaPpcMaxInReference_Type.__name__ = "Integer32"
_TnPowerMgmtIngressInternodalOaPpcMaxInReference_Object = MibTableColumn
tnPowerMgmtIngressInternodalOaPpcMaxInReference = _TnPowerMgmtIngressInternodalOaPpcMaxInReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 20),
    _TnPowerMgmtIngressInternodalOaPpcMaxInReference_Type()
)
tnPowerMgmtIngressInternodalOaPpcMaxInReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressInternodalOaPpcMaxInReference.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressInternodalOaPpcMaxInReference.setUnits("mBm")


class _TnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent_Type(Integer32):
    """Custom type tnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent_Type.__name__ = "Integer32"
_TnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent_Object = MibTableColumn
tnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent = _TnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 21),
    _TnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent_Type()
)
tnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent.setUnits("mB")


class _TnPowerMgmtIngressInternodalCalculatedSpanLossInReference_Type(Integer32):
    """Custom type tnPowerMgmtIngressInternodalCalculatedSpanLossInReference based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressInternodalCalculatedSpanLossInReference_Type.__name__ = "Integer32"
_TnPowerMgmtIngressInternodalCalculatedSpanLossInReference_Object = MibTableColumn
tnPowerMgmtIngressInternodalCalculatedSpanLossInReference = _TnPowerMgmtIngressInternodalCalculatedSpanLossInReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 22),
    _TnPowerMgmtIngressInternodalCalculatedSpanLossInReference_Type()
)
tnPowerMgmtIngressInternodalCalculatedSpanLossInReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressInternodalCalculatedSpanLossInReference.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressInternodalCalculatedSpanLossInReference.setUnits("mB")


class _TnPowerMgmtIngressSRSTiltPostFractionL_Type(Integer32):
    """Custom type tnPowerMgmtIngressSRSTiltPostFractionL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressSRSTiltPostFractionL_Type.__name__ = "Integer32"
_TnPowerMgmtIngressSRSTiltPostFractionL_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltPostFractionL = _TnPowerMgmtIngressSRSTiltPostFractionL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 23),
    _TnPowerMgmtIngressSRSTiltPostFractionL_Type()
)
tnPowerMgmtIngressSRSTiltPostFractionL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltPostFractionL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltPostFractionL.setUnits("100ths")


class _TnPowerMgmtIngressGainSetOffsetL_Type(Integer32):
    """Custom type tnPowerMgmtIngressGainSetOffsetL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressGainSetOffsetL_Type.__name__ = "Integer32"
_TnPowerMgmtIngressGainSetOffsetL_Object = MibTableColumn
tnPowerMgmtIngressGainSetOffsetL = _TnPowerMgmtIngressGainSetOffsetL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 24),
    _TnPowerMgmtIngressGainSetOffsetL_Type()
)
tnPowerMgmtIngressGainSetOffsetL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressGainSetOffsetL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressGainSetOffsetL.setUnits("mB")
_TnPowerMgmtIngressAdjustPowerGainTargetGainL_Type = Unsigned32
_TnPowerMgmtIngressAdjustPowerGainTargetGainL_Object = MibTableColumn
tnPowerMgmtIngressAdjustPowerGainTargetGainL = _TnPowerMgmtIngressAdjustPowerGainTargetGainL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 25),
    _TnPowerMgmtIngressAdjustPowerGainTargetGainL_Type()
)
tnPowerMgmtIngressAdjustPowerGainTargetGainL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainTargetGainL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressAdjustPowerGainTargetGainL.setUnits("mB")
_TnPowerMgmtIngressCommissionedGainL_Type = Integer32
_TnPowerMgmtIngressCommissionedGainL_Object = MibTableColumn
tnPowerMgmtIngressCommissionedGainL = _TnPowerMgmtIngressCommissionedGainL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 26),
    _TnPowerMgmtIngressCommissionedGainL_Type()
)
tnPowerMgmtIngressCommissionedGainL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressCommissionedGainL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressCommissionedGainL.setUnits("mB")


class _TnPowerMgmtIngressSRSTiltCalcOffsetL_Type(Integer32):
    """Custom type tnPowerMgmtIngressSRSTiltCalcOffsetL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtIngressSRSTiltCalcOffsetL_Type.__name__ = "Integer32"
_TnPowerMgmtIngressSRSTiltCalcOffsetL_Object = MibTableColumn
tnPowerMgmtIngressSRSTiltCalcOffsetL = _TnPowerMgmtIngressSRSTiltCalcOffsetL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 4, 1, 27),
    _TnPowerMgmtIngressSRSTiltCalcOffsetL_Type()
)
tnPowerMgmtIngressSRSTiltCalcOffsetL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltCalcOffsetL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressSRSTiltCalcOffsetL.setUnits("mB")
_TnPowerMgmtEgressTable_Object = MibTable
tnPowerMgmtEgressTable = _TnPowerMgmtEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressTable.setStatus("current")
_TnPowerMgmtEgressEntry_Object = MibTableRow
tnPowerMgmtEgressEntry = _TnPowerMgmtEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1)
)
tnPowerMgmtEgressEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressEntry.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimization_Type = TnCommand
_TnPowerMgmtEgressAdjustPowerWithOptimization_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimization = _TnPowerMgmtEgressAdjustPowerWithOptimization_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 1),
    _TnPowerMgmtEgressAdjustPowerWithOptimization_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimization.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimizationStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtEgressAdjustPowerWithOptimizationStatus_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimizationStatus = _TnPowerMgmtEgressAdjustPowerWithOptimizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 2),
    _TnPowerMgmtEgressAdjustPowerWithOptimizationStatus_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationStatus.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimizationAbort_Type = TnCommand
_TnPowerMgmtEgressAdjustPowerWithOptimizationAbort_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimizationAbort = _TnPowerMgmtEgressAdjustPowerWithOptimizationAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 3),
    _TnPowerMgmtEgressAdjustPowerWithOptimizationAbort_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimizationAbort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationAbort.setStatus("current")
_TnPowerMgmtEgressAcceptPowers_Type = TnCommand
_TnPowerMgmtEgressAcceptPowers_Object = MibTableColumn
tnPowerMgmtEgressAcceptPowers = _TnPowerMgmtEgressAcceptPowers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 4),
    _TnPowerMgmtEgressAcceptPowers_Type()
)
tnPowerMgmtEgressAcceptPowers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAcceptPowers.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimizationLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtEgressAdjustPowerWithOptimizationLastResult_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult = _TnPowerMgmtEgressAdjustPowerWithOptimizationLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 6),
    _TnPowerMgmtEgressAdjustPowerWithOptimizationLastResult_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult.setStatus("current")
_TnPowerMgmtEgressAcceptPowersLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtEgressAcceptPowersLastResult_Object = MibTableColumn
tnPowerMgmtEgressAcceptPowersLastResult = _TnPowerMgmtEgressAcceptPowersLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 7),
    _TnPowerMgmtEgressAcceptPowersLastResult_Type()
)
tnPowerMgmtEgressAcceptPowersLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAcceptPowersLastResult.setStatus("current")
_TnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain_Type = Unsigned32
_TnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain_Object = MibTableColumn
tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain = _TnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 9),
    _TnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain_Type()
)
tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain.setStatus("deprecated")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain.setUnits("mB")
_TnPowerMgmtEgressStartAseAdjust_Type = TnCommand
_TnPowerMgmtEgressStartAseAdjust_Object = MibTableColumn
tnPowerMgmtEgressStartAseAdjust = _TnPowerMgmtEgressStartAseAdjust_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 10),
    _TnPowerMgmtEgressStartAseAdjust_Type()
)
tnPowerMgmtEgressStartAseAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressStartAseAdjust.setStatus("current")
_TnPowerMgmtEgressStopAseAdjust_Type = TnCommand
_TnPowerMgmtEgressStopAseAdjust_Object = MibTableColumn
tnPowerMgmtEgressStopAseAdjust = _TnPowerMgmtEgressStopAseAdjust_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 11),
    _TnPowerMgmtEgressStopAseAdjust_Type()
)
tnPowerMgmtEgressStopAseAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressStopAseAdjust.setStatus("current")
_TnPowerMgmtEgressAseAdjustLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtEgressAseAdjustLastResult_Object = MibTableColumn
tnPowerMgmtEgressAseAdjustLastResult = _TnPowerMgmtEgressAseAdjustLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 12),
    _TnPowerMgmtEgressAseAdjustLastResult_Type()
)
tnPowerMgmtEgressAseAdjustLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAseAdjustLastResult.setStatus("current")
_TnPowerMgmtEgressAseAdjustStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtEgressAseAdjustStatus_Object = MibTableColumn
tnPowerMgmtEgressAseAdjustStatus = _TnPowerMgmtEgressAseAdjustStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 13),
    _TnPowerMgmtEgressAseAdjustStatus_Type()
)
tnPowerMgmtEgressAseAdjustStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAseAdjustStatus.setStatus("current")


class _TnPowerMgmtEgressCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtEgressCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtEgressCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtEgressCommissioned_Object = MibTableColumn
tnPowerMgmtEgressCommissioned = _TnPowerMgmtEgressCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 14),
    _TnPowerMgmtEgressCommissioned_Type()
)
tnPowerMgmtEgressCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressCommissioned.setStatus("current")
_TnPowerMgmtEgressAmpIfIndex_Type = InterfaceIndexOrZero
_TnPowerMgmtEgressAmpIfIndex_Object = MibTableColumn
tnPowerMgmtEgressAmpIfIndex = _TnPowerMgmtEgressAmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 15),
    _TnPowerMgmtEgressAmpIfIndex_Type()
)
tnPowerMgmtEgressAmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressAmpIfIndex.setStatus("current")
_TnPowerMgmtEgressWssIfIndex_Type = InterfaceIndexOrZero
_TnPowerMgmtEgressWssIfIndex_Object = MibTableColumn
tnPowerMgmtEgressWssIfIndex = _TnPowerMgmtEgressWssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 16),
    _TnPowerMgmtEgressWssIfIndex_Type()
)
tnPowerMgmtEgressWssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressWssIfIndex.setStatus("current")


class _TnPowerMgmtEgressSRSTiltCalcMultiplier_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltCalcMultiplier based on Integer32"""
    defaultValue = 100


_TnPowerMgmtEgressSRSTiltCalcMultiplier_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltCalcMultiplier_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltCalcMultiplier = _TnPowerMgmtEgressSRSTiltCalcMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 17),
    _TnPowerMgmtEgressSRSTiltCalcMultiplier_Type()
)
tnPowerMgmtEgressSRSTiltCalcMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcMultiplier.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcMultiplier.setUnits("100ths")


class _TnPowerMgmtEgressSRSTiltPreFraction_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltPreFraction based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressSRSTiltPreFraction_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltPreFraction_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltPreFraction = _TnPowerMgmtEgressSRSTiltPreFraction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 18),
    _TnPowerMgmtEgressSRSTiltPreFraction_Type()
)
tnPowerMgmtEgressSRSTiltPreFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltPreFraction.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltPreFraction.setUnits("100ths")


class _TnPowerMgmtEgressSRSTiltCalcACoeff_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltCalcACoeff based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressSRSTiltCalcACoeff_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltCalcACoeff_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltCalcACoeff = _TnPowerMgmtEgressSRSTiltCalcACoeff_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 19),
    _TnPowerMgmtEgressSRSTiltCalcACoeff_Type()
)
tnPowerMgmtEgressSRSTiltCalcACoeff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcACoeff.setStatus("current")


class _TnPowerMgmtEgressSRSTiltCalcOutputLoss_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltCalcOutputLoss based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressSRSTiltCalcOutputLoss_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltCalcOutputLoss_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltCalcOutputLoss = _TnPowerMgmtEgressSRSTiltCalcOutputLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 20),
    _TnPowerMgmtEgressSRSTiltCalcOutputLoss_Type()
)
tnPowerMgmtEgressSRSTiltCalcOutputLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcOutputLoss.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcOutputLoss.setUnits("mB")


class _TnPowerMgmtEgressSRSTiltAdjResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtEgressSRSTiltAdjResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtEgressSRSTiltAdjResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtEgressSRSTiltAdjResult_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltAdjResult = _TnPowerMgmtEgressSRSTiltAdjResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 22),
    _TnPowerMgmtEgressSRSTiltAdjResult_Type()
)
tnPowerMgmtEgressSRSTiltAdjResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltAdjResult.setStatus("current")


class _TnPowerMgmtEgressSRSTiltAdjStatus_Type(AluWdmPowerMgmtSRSTiltAdjStatus):
    """Custom type tnPowerMgmtEgressSRSTiltAdjStatus based on AluWdmPowerMgmtSRSTiltAdjStatus"""
    defaultValue = 3


_TnPowerMgmtEgressSRSTiltAdjStatus_Type.__name__ = "AluWdmPowerMgmtSRSTiltAdjStatus"
_TnPowerMgmtEgressSRSTiltAdjStatus_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltAdjStatus = _TnPowerMgmtEgressSRSTiltAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 23),
    _TnPowerMgmtEgressSRSTiltAdjStatus_Type()
)
tnPowerMgmtEgressSRSTiltAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltAdjStatus.setStatus("current")


class _TnPowerMgmtEgressPassed_Type(TruthValue):
    """Custom type tnPowerMgmtEgressPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtEgressPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtEgressPassed_Object = MibTableColumn
tnPowerMgmtEgressPassed = _TnPowerMgmtEgressPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 24),
    _TnPowerMgmtEgressPassed_Type()
)
tnPowerMgmtEgressPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPassed.setStatus("current")


class _TnPowerMgmtEgressLHLaunchAtten_Type(Integer32):
    """Custom type tnPowerMgmtEgressLHLaunchAtten based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressLHLaunchAtten_Type.__name__ = "Integer32"
_TnPowerMgmtEgressLHLaunchAtten_Object = MibTableColumn
tnPowerMgmtEgressLHLaunchAtten = _TnPowerMgmtEgressLHLaunchAtten_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 25),
    _TnPowerMgmtEgressLHLaunchAtten_Type()
)
tnPowerMgmtEgressLHLaunchAtten.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressLHLaunchAtten.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressLHLaunchAtten.setUnits("mB")


class _TnPowerMgmtFiberSpanTiltPreComp_Type(Integer32):
    """Custom type tnPowerMgmtFiberSpanTiltPreComp based on Integer32"""
    defaultValue = 0


_TnPowerMgmtFiberSpanTiltPreComp_Type.__name__ = "Integer32"
_TnPowerMgmtFiberSpanTiltPreComp_Object = MibTableColumn
tnPowerMgmtFiberSpanTiltPreComp = _TnPowerMgmtFiberSpanTiltPreComp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 27),
    _TnPowerMgmtFiberSpanTiltPreComp_Type()
)
tnPowerMgmtFiberSpanTiltPreComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtFiberSpanTiltPreComp.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtFiberSpanTiltPreComp.setUnits("mB")


class _TnPowerMgmtEgressInternodalPpcMaxInDownstream_Type(Integer32):
    """Custom type tnPowerMgmtEgressInternodalPpcMaxInDownstream based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressInternodalPpcMaxInDownstream_Type.__name__ = "Integer32"
_TnPowerMgmtEgressInternodalPpcMaxInDownstream_Object = MibTableColumn
tnPowerMgmtEgressInternodalPpcMaxInDownstream = _TnPowerMgmtEgressInternodalPpcMaxInDownstream_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 28),
    _TnPowerMgmtEgressInternodalPpcMaxInDownstream_Type()
)
tnPowerMgmtEgressInternodalPpcMaxInDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressInternodalPpcMaxInDownstream.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressInternodalPpcMaxInDownstream.setUnits("mBm")


class _TnPowerMgmtEgressInternodalSpanLossInDownstream_Type(Integer32):
    """Custom type tnPowerMgmtEgressInternodalSpanLossInDownstream based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressInternodalSpanLossInDownstream_Type.__name__ = "Integer32"
_TnPowerMgmtEgressInternodalSpanLossInDownstream_Object = MibTableColumn
tnPowerMgmtEgressInternodalSpanLossInDownstream = _TnPowerMgmtEgressInternodalSpanLossInDownstream_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 29),
    _TnPowerMgmtEgressInternodalSpanLossInDownstream_Type()
)
tnPowerMgmtEgressInternodalSpanLossInDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressInternodalSpanLossInDownstream.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressInternodalSpanLossInDownstream.setUnits("mB")


class _TnPowerMgmtEgressInternodalPpcMaxInDownstreamReference_Type(Integer32):
    """Custom type tnPowerMgmtEgressInternodalPpcMaxInDownstreamReference based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressInternodalPpcMaxInDownstreamReference_Type.__name__ = "Integer32"
_TnPowerMgmtEgressInternodalPpcMaxInDownstreamReference_Object = MibTableColumn
tnPowerMgmtEgressInternodalPpcMaxInDownstreamReference = _TnPowerMgmtEgressInternodalPpcMaxInDownstreamReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 30),
    _TnPowerMgmtEgressInternodalPpcMaxInDownstreamReference_Type()
)
tnPowerMgmtEgressInternodalPpcMaxInDownstreamReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressInternodalPpcMaxInDownstreamReference.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressInternodalPpcMaxInDownstreamReference.setUnits("mBm")


class _TnPowerMgmtEgressInternodalSpanLossInDownstreamReference_Type(Integer32):
    """Custom type tnPowerMgmtEgressInternodalSpanLossInDownstreamReference based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressInternodalSpanLossInDownstreamReference_Type.__name__ = "Integer32"
_TnPowerMgmtEgressInternodalSpanLossInDownstreamReference_Object = MibTableColumn
tnPowerMgmtEgressInternodalSpanLossInDownstreamReference = _TnPowerMgmtEgressInternodalSpanLossInDownstreamReference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 31),
    _TnPowerMgmtEgressInternodalSpanLossInDownstreamReference_Type()
)
tnPowerMgmtEgressInternodalSpanLossInDownstreamReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressInternodalSpanLossInDownstreamReference.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressInternodalSpanLossInDownstreamReference.setUnits("mB")


class _TnPowerMgmtFiberSpanTiltPreCompL_Type(Integer32):
    """Custom type tnPowerMgmtFiberSpanTiltPreCompL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtFiberSpanTiltPreCompL_Type.__name__ = "Integer32"
_TnPowerMgmtFiberSpanTiltPreCompL_Object = MibTableColumn
tnPowerMgmtFiberSpanTiltPreCompL = _TnPowerMgmtFiberSpanTiltPreCompL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 32),
    _TnPowerMgmtFiberSpanTiltPreCompL_Type()
)
tnPowerMgmtFiberSpanTiltPreCompL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtFiberSpanTiltPreCompL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtFiberSpanTiltPreCompL.setUnits("mB")


class _TnPowerMgmtEgressSRSTiltCalcMultiplierL_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltCalcMultiplierL based on Integer32"""
    defaultValue = 100


_TnPowerMgmtEgressSRSTiltCalcMultiplierL_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltCalcMultiplierL_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltCalcMultiplierL = _TnPowerMgmtEgressSRSTiltCalcMultiplierL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 33),
    _TnPowerMgmtEgressSRSTiltCalcMultiplierL_Type()
)
tnPowerMgmtEgressSRSTiltCalcMultiplierL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcMultiplierL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcMultiplierL.setUnits("100ths")


class _TnPowerMgmtEgressSRSTiltPreFractionL_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltPreFractionL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressSRSTiltPreFractionL_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltPreFractionL_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltPreFractionL = _TnPowerMgmtEgressSRSTiltPreFractionL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 34),
    _TnPowerMgmtEgressSRSTiltPreFractionL_Type()
)
tnPowerMgmtEgressSRSTiltPreFractionL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltPreFractionL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltPreFractionL.setUnits("100ths")


class _TnPowerMgmtEgressSRSTiltCalcACoeffL_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSTiltCalcACoeffL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressSRSTiltCalcACoeffL_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSTiltCalcACoeffL_Object = MibTableColumn
tnPowerMgmtEgressSRSTiltCalcACoeffL = _TnPowerMgmtEgressSRSTiltCalcACoeffL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 35),
    _TnPowerMgmtEgressSRSTiltCalcACoeffL_Type()
)
tnPowerMgmtEgressSRSTiltCalcACoeffL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSTiltCalcACoeffL.setStatus("current")


class _TnPowerMgmtEgressSRSCF_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSCF based on Integer32"""
    defaultValue = 100


_TnPowerMgmtEgressSRSCF_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSCF_Object = MibTableColumn
tnPowerMgmtEgressSRSCF = _TnPowerMgmtEgressSRSCF_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 36),
    _TnPowerMgmtEgressSRSCF_Type()
)
tnPowerMgmtEgressSRSCF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSCF.setStatus("current")


class _TnPowerMgmtEgressSRSCFL_Type(Integer32):
    """Custom type tnPowerMgmtEgressSRSCFL based on Integer32"""
    defaultValue = 100


_TnPowerMgmtEgressSRSCFL_Type.__name__ = "Integer32"
_TnPowerMgmtEgressSRSCFL_Object = MibTableColumn
tnPowerMgmtEgressSRSCFL = _TnPowerMgmtEgressSRSCFL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 37),
    _TnPowerMgmtEgressSRSCFL_Type()
)
tnPowerMgmtEgressSRSCFL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSRSCFL.setStatus("current")


class _TnPowerMgmtEgressExternalOTAddLaunchAtten_Type(Unsigned32):
    """Custom type tnPowerMgmtEgressExternalOTAddLaunchAtten based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_TnPowerMgmtEgressExternalOTAddLaunchAtten_Type.__name__ = "Unsigned32"
_TnPowerMgmtEgressExternalOTAddLaunchAtten_Object = MibTableColumn
tnPowerMgmtEgressExternalOTAddLaunchAtten = _TnPowerMgmtEgressExternalOTAddLaunchAtten_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 38),
    _TnPowerMgmtEgressExternalOTAddLaunchAtten_Type()
)
tnPowerMgmtEgressExternalOTAddLaunchAtten.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressExternalOTAddLaunchAtten.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressExternalOTAddLaunchAtten.setUnits("mB")
_TnPowerMgmtEgressSmoothing_Type = TruthValue
_TnPowerMgmtEgressSmoothing_Object = MibTableColumn
tnPowerMgmtEgressSmoothing = _TnPowerMgmtEgressSmoothing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 39),
    _TnPowerMgmtEgressSmoothing_Type()
)
tnPowerMgmtEgressSmoothing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSmoothing.setStatus("current")


class _TnPowerMgmtEgressSmoothingMaxStepSize_Type(Unsigned32):
    """Custom type tnPowerMgmtEgressSmoothingMaxStepSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_TnPowerMgmtEgressSmoothingMaxStepSize_Type.__name__ = "Unsigned32"
_TnPowerMgmtEgressSmoothingMaxStepSize_Object = MibTableColumn
tnPowerMgmtEgressSmoothingMaxStepSize = _TnPowerMgmtEgressSmoothingMaxStepSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 5, 1, 40),
    _TnPowerMgmtEgressSmoothingMaxStepSize_Type()
)
tnPowerMgmtEgressSmoothingMaxStepSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSmoothingMaxStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressSmoothingMaxStepSize.setUnits("mB")
_TnPowerMgmtPortTable_Object = MibTable
tnPowerMgmtPortTable = _TnPowerMgmtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnPowerMgmtPortTable.setStatus("current")
_TnPowerMgmtPortEntry_Object = MibTableRow
tnPowerMgmtPortEntry = _TnPowerMgmtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1)
)
tnPowerMgmtPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtPortEntry.setStatus("current")


class _TnPowerMgmtPortIsCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtPortIsCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtPortIsCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtPortIsCommissioned_Object = MibTableColumn
tnPowerMgmtPortIsCommissioned = _TnPowerMgmtPortIsCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 1),
    _TnPowerMgmtPortIsCommissioned_Type()
)
tnPowerMgmtPortIsCommissioned.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortIsCommissioned.setStatus("current")
_TnPowerMgmtPortTypeIn_Type = TropicPowerMgmtType
_TnPowerMgmtPortTypeIn_Object = MibTableColumn
tnPowerMgmtPortTypeIn = _TnPowerMgmtPortTypeIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 2),
    _TnPowerMgmtPortTypeIn_Type()
)
tnPowerMgmtPortTypeIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortTypeIn.setStatus("current")
_TnPowerMgmtPortTypeOut_Type = TropicPowerMgmtType
_TnPowerMgmtPortTypeOut_Object = MibTableColumn
tnPowerMgmtPortTypeOut = _TnPowerMgmtPortTypeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 3),
    _TnPowerMgmtPortTypeOut_Type()
)
tnPowerMgmtPortTypeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortTypeOut.setStatus("current")


class _TnPowerMgmtPortWTDecoderUsageTypeIn_Type(AluWdmWTDecoderUsageType):
    """Custom type tnPowerMgmtPortWTDecoderUsageTypeIn based on AluWdmWTDecoderUsageType"""
    defaultValue = 2


_TnPowerMgmtPortWTDecoderUsageTypeIn_Type.__name__ = "AluWdmWTDecoderUsageType"
_TnPowerMgmtPortWTDecoderUsageTypeIn_Object = MibTableColumn
tnPowerMgmtPortWTDecoderUsageTypeIn = _TnPowerMgmtPortWTDecoderUsageTypeIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 6),
    _TnPowerMgmtPortWTDecoderUsageTypeIn_Type()
)
tnPowerMgmtPortWTDecoderUsageTypeIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortWTDecoderUsageTypeIn.setStatus("current")


class _TnPowerMgmtPortWTDecoderUsageTypeOut_Type(AluWdmWTDecoderUsageType):
    """Custom type tnPowerMgmtPortWTDecoderUsageTypeOut based on AluWdmWTDecoderUsageType"""
    defaultValue = 2


_TnPowerMgmtPortWTDecoderUsageTypeOut_Type.__name__ = "AluWdmWTDecoderUsageType"
_TnPowerMgmtPortWTDecoderUsageTypeOut_Object = MibTableColumn
tnPowerMgmtPortWTDecoderUsageTypeOut = _TnPowerMgmtPortWTDecoderUsageTypeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 7),
    _TnPowerMgmtPortWTDecoderUsageTypeOut_Type()
)
tnPowerMgmtPortWTDecoderUsageTypeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortWTDecoderUsageTypeOut.setStatus("current")


class _TnPowerMgmtPortGainAdjSchedBase_Type(Integer32):
    """Custom type tnPowerMgmtPortGainAdjSchedBase based on Integer32"""
    defaultValue = -1


_TnPowerMgmtPortGainAdjSchedBase_Type.__name__ = "Integer32"
_TnPowerMgmtPortGainAdjSchedBase_Object = MibTableColumn
tnPowerMgmtPortGainAdjSchedBase = _TnPowerMgmtPortGainAdjSchedBase_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 8),
    _TnPowerMgmtPortGainAdjSchedBase_Type()
)
tnPowerMgmtPortGainAdjSchedBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortGainAdjSchedBase.setStatus("current")


class _TnPowerMgmtPortGainAdjTimerPeriod_Type(Integer32):
    """Custom type tnPowerMgmtPortGainAdjTimerPeriod based on Integer32"""
    defaultValue = -1


_TnPowerMgmtPortGainAdjTimerPeriod_Type.__name__ = "Integer32"
_TnPowerMgmtPortGainAdjTimerPeriod_Object = MibTableColumn
tnPowerMgmtPortGainAdjTimerPeriod = _TnPowerMgmtPortGainAdjTimerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 9),
    _TnPowerMgmtPortGainAdjTimerPeriod_Type()
)
tnPowerMgmtPortGainAdjTimerPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortGainAdjTimerPeriod.setStatus("current")


class _TnPowerMgmtPortGainAdjTimerLength_Type(Integer32):
    """Custom type tnPowerMgmtPortGainAdjTimerLength based on Integer32"""
    defaultValue = -1


_TnPowerMgmtPortGainAdjTimerLength_Type.__name__ = "Integer32"
_TnPowerMgmtPortGainAdjTimerLength_Object = MibTableColumn
tnPowerMgmtPortGainAdjTimerLength = _TnPowerMgmtPortGainAdjTimerLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 10),
    _TnPowerMgmtPortGainAdjTimerLength_Type()
)
tnPowerMgmtPortGainAdjTimerLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortGainAdjTimerLength.setStatus("current")


class _TnPowerMgmtPortInGainAdjAutoEnabled_Type(TruthValue):
    """Custom type tnPowerMgmtPortInGainAdjAutoEnabled based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtPortInGainAdjAutoEnabled_Type.__name__ = "TruthValue"
_TnPowerMgmtPortInGainAdjAutoEnabled_Object = MibTableColumn
tnPowerMgmtPortInGainAdjAutoEnabled = _TnPowerMgmtPortInGainAdjAutoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 11),
    _TnPowerMgmtPortInGainAdjAutoEnabled_Type()
)
tnPowerMgmtPortInGainAdjAutoEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortInGainAdjAutoEnabled.setStatus("current")


class _TnPowerMgmtPortSRSTiltAdjAutoEnabled_Type(TruthValue):
    """Custom type tnPowerMgmtPortSRSTiltAdjAutoEnabled based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtPortSRSTiltAdjAutoEnabled_Type.__name__ = "TruthValue"
_TnPowerMgmtPortSRSTiltAdjAutoEnabled_Object = MibTableColumn
tnPowerMgmtPortSRSTiltAdjAutoEnabled = _TnPowerMgmtPortSRSTiltAdjAutoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 12),
    _TnPowerMgmtPortSRSTiltAdjAutoEnabled_Type()
)
tnPowerMgmtPortSRSTiltAdjAutoEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortSRSTiltAdjAutoEnabled.setStatus("current")


class _TnPowerMgmtPortFiberSpanTilt_Type(Integer32):
    """Custom type tnPowerMgmtPortFiberSpanTilt based on Integer32"""
    defaultValue = 0


_TnPowerMgmtPortFiberSpanTilt_Type.__name__ = "Integer32"
_TnPowerMgmtPortFiberSpanTilt_Object = MibTableColumn
tnPowerMgmtPortFiberSpanTilt = _TnPowerMgmtPortFiberSpanTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 13),
    _TnPowerMgmtPortFiberSpanTilt_Type()
)
tnPowerMgmtPortFiberSpanTilt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortFiberSpanTilt.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtPortFiberSpanTilt.setUnits("mB")


class _TnPowerMgmtPortSRSTiltMaintenanceMode_Type(TruthValue):
    """Custom type tnPowerMgmtPortSRSTiltMaintenanceMode based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtPortSRSTiltMaintenanceMode_Type.__name__ = "TruthValue"
_TnPowerMgmtPortSRSTiltMaintenanceMode_Object = MibTableColumn
tnPowerMgmtPortSRSTiltMaintenanceMode = _TnPowerMgmtPortSRSTiltMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 14),
    _TnPowerMgmtPortSRSTiltMaintenanceMode_Type()
)
tnPowerMgmtPortSRSTiltMaintenanceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortSRSTiltMaintenanceMode.setStatus("current")


class _TnPowerMgmtPortDegreeFunction_Type(Integer32):
    """Custom type tnPowerMgmtPortDegreeFunction based on Integer32"""
    defaultValue = 1

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
        *(("notDefined", 1),
          ("ila", 2),
          ("dge", 3),
          ("oadm", 4))
    )


_TnPowerMgmtPortDegreeFunction_Type.__name__ = "Integer32"
_TnPowerMgmtPortDegreeFunction_Object = MibTableColumn
tnPowerMgmtPortDegreeFunction = _TnPowerMgmtPortDegreeFunction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 15),
    _TnPowerMgmtPortDegreeFunction_Type()
)
tnPowerMgmtPortDegreeFunction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortDegreeFunction.setStatus("current")


class _TnPowerMgmtPortMaxChannels_Type(Unsigned32):
    """Custom type tnPowerMgmtPortMaxChannels based on Unsigned32"""
    defaultValue = 88


_TnPowerMgmtPortMaxChannels_Type.__name__ = "Unsigned32"
_TnPowerMgmtPortMaxChannels_Object = MibTableColumn
tnPowerMgmtPortMaxChannels = _TnPowerMgmtPortMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 16),
    _TnPowerMgmtPortMaxChannels_Type()
)
tnPowerMgmtPortMaxChannels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortMaxChannels.setStatus("current")
_TnPowerMgmtPortEgressAdjustForDownstreamEnabled_Type = TruthValue
_TnPowerMgmtPortEgressAdjustForDownstreamEnabled_Object = MibTableColumn
tnPowerMgmtPortEgressAdjustForDownstreamEnabled = _TnPowerMgmtPortEgressAdjustForDownstreamEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 17),
    _TnPowerMgmtPortEgressAdjustForDownstreamEnabled_Type()
)
tnPowerMgmtPortEgressAdjustForDownstreamEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortEgressAdjustForDownstreamEnabled.setStatus("current")


class _TnPowerMgmtPortFiberSpanTiltL_Type(Integer32):
    """Custom type tnPowerMgmtPortFiberSpanTiltL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtPortFiberSpanTiltL_Type.__name__ = "Integer32"
_TnPowerMgmtPortFiberSpanTiltL_Object = MibTableColumn
tnPowerMgmtPortFiberSpanTiltL = _TnPowerMgmtPortFiberSpanTiltL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 18),
    _TnPowerMgmtPortFiberSpanTiltL_Type()
)
tnPowerMgmtPortFiberSpanTiltL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortFiberSpanTiltL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtPortFiberSpanTiltL.setUnits("mB")


class _TnPowerMgmtPortWTDecoderUsageTypeInL_Type(AluWdmWTDecoderUsageType):
    """Custom type tnPowerMgmtPortWTDecoderUsageTypeInL based on AluWdmWTDecoderUsageType"""
    defaultValue = 2


_TnPowerMgmtPortWTDecoderUsageTypeInL_Type.__name__ = "AluWdmWTDecoderUsageType"
_TnPowerMgmtPortWTDecoderUsageTypeInL_Object = MibTableColumn
tnPowerMgmtPortWTDecoderUsageTypeInL = _TnPowerMgmtPortWTDecoderUsageTypeInL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 19),
    _TnPowerMgmtPortWTDecoderUsageTypeInL_Type()
)
tnPowerMgmtPortWTDecoderUsageTypeInL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortWTDecoderUsageTypeInL.setStatus("current")


class _TnPowerMgmtPortWTDecoderUsageTypeOutL_Type(AluWdmWTDecoderUsageType):
    """Custom type tnPowerMgmtPortWTDecoderUsageTypeOutL based on AluWdmWTDecoderUsageType"""
    defaultValue = 2


_TnPowerMgmtPortWTDecoderUsageTypeOutL_Type.__name__ = "AluWdmWTDecoderUsageType"
_TnPowerMgmtPortWTDecoderUsageTypeOutL_Object = MibTableColumn
tnPowerMgmtPortWTDecoderUsageTypeOutL = _TnPowerMgmtPortWTDecoderUsageTypeOutL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 20),
    _TnPowerMgmtPortWTDecoderUsageTypeOutL_Type()
)
tnPowerMgmtPortWTDecoderUsageTypeOutL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortWTDecoderUsageTypeOutL.setStatus("current")


class _TnPowerMgmtPortIsCommissionedMethod_Type(Integer32):
    """Custom type tnPowerMgmtPortIsCommissionedMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undetermined", 1),
          ("manual", 2),
          ("autoTurnUp", 3))
    )


_TnPowerMgmtPortIsCommissionedMethod_Type.__name__ = "Integer32"
_TnPowerMgmtPortIsCommissionedMethod_Object = MibTableColumn
tnPowerMgmtPortIsCommissionedMethod = _TnPowerMgmtPortIsCommissionedMethod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 7, 1, 21),
    _TnPowerMgmtPortIsCommissionedMethod_Type()
)
tnPowerMgmtPortIsCommissionedMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtPortIsCommissionedMethod.setStatus("current")
_TnPowerMgmtPowerOffsetInTable_Object = MibTable
tnPowerMgmtPowerOffsetInTable = _TnPowerMgmtPowerOffsetInTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetInTable.setStatus("current")
_TnPowerMgmtPowerOffsetInEntry_Object = MibTableRow
tnPowerMgmtPowerOffsetInEntry = _TnPowerMgmtPowerOffsetInEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9, 1)
)
tnPowerMgmtPowerOffsetInEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtBitRate"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtEncoding"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetInEntry.setStatus("current")
_TnPowerMgmtBitRate_Type = AluWdmOtuBitRate
_TnPowerMgmtBitRate_Object = MibTableColumn
tnPowerMgmtBitRate = _TnPowerMgmtBitRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9, 1, 1),
    _TnPowerMgmtBitRate_Type()
)
tnPowerMgmtBitRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPowerMgmtBitRate.setStatus("current")
_TnPowerMgmtEncoding_Type = AluWdmOtuEncoding
_TnPowerMgmtEncoding_Object = MibTableColumn
tnPowerMgmtEncoding = _TnPowerMgmtEncoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9, 1, 2),
    _TnPowerMgmtEncoding_Type()
)
tnPowerMgmtEncoding.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPowerMgmtEncoding.setStatus("current")


class _TnPowerMgmtOffsetInPowerOffset_Type(Integer32):
    """Custom type tnPowerMgmtOffsetInPowerOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_TnPowerMgmtOffsetInPowerOffset_Type.__name__ = "Integer32"
_TnPowerMgmtOffsetInPowerOffset_Object = MibTableColumn
tnPowerMgmtOffsetInPowerOffset = _TnPowerMgmtOffsetInPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 9, 1, 3),
    _TnPowerMgmtOffsetInPowerOffset_Type()
)
tnPowerMgmtOffsetInPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtOffsetInPowerOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtOffsetInPowerOffset.setUnits("mB")
_TnPowerMgmtPowerOffsetOutTable_Object = MibTable
tnPowerMgmtPowerOffsetOutTable = _TnPowerMgmtPowerOffsetOutTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetOutTable.setStatus("current")
_TnPowerMgmtPowerOffsetOutEntry_Object = MibTableRow
tnPowerMgmtPowerOffsetOutEntry = _TnPowerMgmtPowerOffsetOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 10, 1)
)
tnPowerMgmtPowerOffsetOutEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtBitRate"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtEncoding"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetOutEntry.setStatus("current")


class _TnPowerMgmtOffsetOutPowerOffset_Type(Integer32):
    """Custom type tnPowerMgmtOffsetOutPowerOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 600),
    )


_TnPowerMgmtOffsetOutPowerOffset_Type.__name__ = "Integer32"
_TnPowerMgmtOffsetOutPowerOffset_Object = MibTableColumn
tnPowerMgmtOffsetOutPowerOffset = _TnPowerMgmtOffsetOutPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 10, 1, 1),
    _TnPowerMgmtOffsetOutPowerOffset_Type()
)
tnPowerMgmtOffsetOutPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtOffsetOutPowerOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtOffsetOutPowerOffset.setUnits("mB")
_TnPowerMgmtIngressPerChannelTable_Object = MibTable
tnPowerMgmtIngressPerChannelTable = _TnPowerMgmtIngressPerChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11)
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelTable.setStatus("current")
_TnPowerMgmtIngressPerChannelEntry_Object = MibTableRow
tnPowerMgmtIngressPerChannelEntry = _TnPowerMgmtIngressPerChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1)
)
tnPowerMgmtIngressPerChannelEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelEntry.setStatus("current")


class _TnPowerMgmtIngressPerChannelSystemTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelSystemTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtIngressPerChannelSystemTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelSystemTargetOffset_Object = MibTableColumn
tnPowerMgmtIngressPerChannelSystemTargetOffset = _TnPowerMgmtIngressPerChannelSystemTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 1),
    _TnPowerMgmtIngressPerChannelSystemTargetOffset_Type()
)
tnPowerMgmtIngressPerChannelSystemTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelSystemTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelSystemTargetOffset.setUnits("mB")


class _TnPowerMgmtIngressPerChannelUserTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelUserTargetOffset based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressPerChannelUserTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelUserTargetOffset_Object = MibTableColumn
tnPowerMgmtIngressPerChannelUserTargetOffset = _TnPowerMgmtIngressPerChannelUserTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 2),
    _TnPowerMgmtIngressPerChannelUserTargetOffset_Type()
)
tnPowerMgmtIngressPerChannelUserTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelUserTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelUserTargetOffset.setUnits("mB")


class _TnPowerMgmtIngressPerChannelInUseTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelInUseTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtIngressPerChannelInUseTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelInUseTargetOffset_Object = MibTableColumn
tnPowerMgmtIngressPerChannelInUseTargetOffset = _TnPowerMgmtIngressPerChannelInUseTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 3),
    _TnPowerMgmtIngressPerChannelInUseTargetOffset_Type()
)
tnPowerMgmtIngressPerChannelInUseTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelInUseTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelInUseTargetOffset.setUnits("mB")


class _TnPowerMgmtIngressPerChannelTargetAbsolute_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelTargetAbsolute based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressPerChannelTargetAbsolute_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelTargetAbsolute_Object = MibTableColumn
tnPowerMgmtIngressPerChannelTargetAbsolute = _TnPowerMgmtIngressPerChannelTargetAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 4),
    _TnPowerMgmtIngressPerChannelTargetAbsolute_Type()
)
tnPowerMgmtIngressPerChannelTargetAbsolute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelTargetAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelTargetAbsolute.setUnits("mBm")


class _TnPowerMgmtIngressPerChannelApplicability_Type(Integer32):
    """Custom type tnPowerMgmtIngressPerChannelApplicability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("applicable", 2))
    )


_TnPowerMgmtIngressPerChannelApplicability_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPerChannelApplicability_Object = MibTableColumn
tnPowerMgmtIngressPerChannelApplicability = _TnPowerMgmtIngressPerChannelApplicability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 11, 1, 5),
    _TnPowerMgmtIngressPerChannelApplicability_Type()
)
tnPowerMgmtIngressPerChannelApplicability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelApplicability.setStatus("current")
_TnPowerMgmtEgressPerChannelTable_Object = MibTable
tnPowerMgmtEgressPerChannelTable = _TnPowerMgmtEgressPerChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12)
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelTable.setStatus("current")
_TnPowerMgmtEgressPerChannelEntry_Object = MibTableRow
tnPowerMgmtEgressPerChannelEntry = _TnPowerMgmtEgressPerChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1)
)
tnPowerMgmtEgressPerChannelEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelEntry.setStatus("current")


class _TnPowerMgmtEgressPerChannelSystemTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelSystemTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtEgressPerChannelSystemTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelSystemTargetOffset_Object = MibTableColumn
tnPowerMgmtEgressPerChannelSystemTargetOffset = _TnPowerMgmtEgressPerChannelSystemTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 1),
    _TnPowerMgmtEgressPerChannelSystemTargetOffset_Type()
)
tnPowerMgmtEgressPerChannelSystemTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelSystemTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelSystemTargetOffset.setUnits("mB")


class _TnPowerMgmtEgressPerChannelUserTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelUserTargetOffset based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressPerChannelUserTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelUserTargetOffset_Object = MibTableColumn
tnPowerMgmtEgressPerChannelUserTargetOffset = _TnPowerMgmtEgressPerChannelUserTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 2),
    _TnPowerMgmtEgressPerChannelUserTargetOffset_Type()
)
tnPowerMgmtEgressPerChannelUserTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelUserTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelUserTargetOffset.setUnits("mB")


class _TnPowerMgmtEgressPerChannelInUseTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelInUseTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtEgressPerChannelInUseTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelInUseTargetOffset_Object = MibTableColumn
tnPowerMgmtEgressPerChannelInUseTargetOffset = _TnPowerMgmtEgressPerChannelInUseTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 3),
    _TnPowerMgmtEgressPerChannelInUseTargetOffset_Type()
)
tnPowerMgmtEgressPerChannelInUseTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelInUseTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelInUseTargetOffset.setUnits("mB")


class _TnPowerMgmtEgressPerChannelTargetAbsolute_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelTargetAbsolute based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressPerChannelTargetAbsolute_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelTargetAbsolute_Object = MibTableColumn
tnPowerMgmtEgressPerChannelTargetAbsolute = _TnPowerMgmtEgressPerChannelTargetAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 4),
    _TnPowerMgmtEgressPerChannelTargetAbsolute_Type()
)
tnPowerMgmtEgressPerChannelTargetAbsolute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelTargetAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelTargetAbsolute.setUnits("mBm")


class _TnPowerMgmtEgressPerChannelApplicability_Type(Integer32):
    """Custom type tnPowerMgmtEgressPerChannelApplicability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("applicable", 2))
    )


_TnPowerMgmtEgressPerChannelApplicability_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPerChannelApplicability_Object = MibTableColumn
tnPowerMgmtEgressPerChannelApplicability = _TnPowerMgmtEgressPerChannelApplicability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 12, 1, 5),
    _TnPowerMgmtEgressPerChannelApplicability_Type()
)
tnPowerMgmtEgressPerChannelApplicability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelApplicability.setStatus("current")
_TnPowerMgmtTechnologyTypesTable_Object = MibTable
tnPowerMgmtTechnologyTypesTable = _TnPowerMgmtTechnologyTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13)
)
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesTable.setStatus("current")
_TnPowerMgmtTechnologyTypesEntry_Object = MibTableRow
tnPowerMgmtTechnologyTypesEntry = _TnPowerMgmtTechnologyTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1)
)
tnPowerMgmtTechnologyTypesEntry.setIndexNames(
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtBitRate"),
    (0, "TROPIC-POWERMGMT-MIB", "tnPowerMgmtEncoding"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesEntry.setStatus("current")


class _TnPowerMgmtTechnologyTypesBitRateText_Type(SnmpAdminString):
    """Custom type tnPowerMgmtTechnologyTypesBitRateText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnPowerMgmtTechnologyTypesBitRateText_Type.__name__ = "SnmpAdminString"
_TnPowerMgmtTechnologyTypesBitRateText_Object = MibTableColumn
tnPowerMgmtTechnologyTypesBitRateText = _TnPowerMgmtTechnologyTypesBitRateText_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 1),
    _TnPowerMgmtTechnologyTypesBitRateText_Type()
)
tnPowerMgmtTechnologyTypesBitRateText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesBitRateText.setStatus("current")


class _TnPowerMgmtTechnologyTypesEncodingText_Type(SnmpAdminString):
    """Custom type tnPowerMgmtTechnologyTypesEncodingText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnPowerMgmtTechnologyTypesEncodingText_Type.__name__ = "SnmpAdminString"
_TnPowerMgmtTechnologyTypesEncodingText_Object = MibTableColumn
tnPowerMgmtTechnologyTypesEncodingText = _TnPowerMgmtTechnologyTypesEncodingText_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 2),
    _TnPowerMgmtTechnologyTypesEncodingText_Type()
)
tnPowerMgmtTechnologyTypesEncodingText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesEncodingText.setStatus("current")


class _TnPowerMgmtTechnologyTypesWtocmCalib_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesWtocmCalib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesWtocmCalib_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesWtocmCalib_Object = MibTableColumn
tnPowerMgmtTechnologyTypesWtocmCalib = _TnPowerMgmtTechnologyTypesWtocmCalib_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 3),
    _TnPowerMgmtTechnologyTypesWtocmCalib_Type()
)
tnPowerMgmtTechnologyTypesWtocmCalib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmCalib.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmCalib.setUnits("mB")
_TnPowerMgmtTechnologyTypesRowStatus_Type = RowStatus
_TnPowerMgmtTechnologyTypesRowStatus_Object = MibTableColumn
tnPowerMgmtTechnologyTypesRowStatus = _TnPowerMgmtTechnologyTypesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 4),
    _TnPowerMgmtTechnologyTypesRowStatus_Type()
)
tnPowerMgmtTechnologyTypesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesRowStatus.setStatus("current")


class _TnPowerMgmtTechnologyTypesOsnrCalib_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesOsnrCalib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesOsnrCalib_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesOsnrCalib_Object = MibTableColumn
tnPowerMgmtTechnologyTypesOsnrCalib = _TnPowerMgmtTechnologyTypesOsnrCalib_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 5),
    _TnPowerMgmtTechnologyTypesOsnrCalib_Type()
)
tnPowerMgmtTechnologyTypesOsnrCalib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesOsnrCalib.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesOsnrCalib.setUnits("mB")


class _TnPowerMgmtTechnologyTypesWtocmaCalib_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesWtocmaCalib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesWtocmaCalib_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesWtocmaCalib_Object = MibTableColumn
tnPowerMgmtTechnologyTypesWtocmaCalib = _TnPowerMgmtTechnologyTypesWtocmaCalib_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 6),
    _TnPowerMgmtTechnologyTypesWtocmaCalib_Type()
)
tnPowerMgmtTechnologyTypesWtocmaCalib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmaCalib.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmaCalib.setUnits("mB")


class _TnPowerMgmtTechnologyTypesWtocmfCalib_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesWtocmfCalib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesWtocmfCalib_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesWtocmfCalib_Object = MibTableColumn
tnPowerMgmtTechnologyTypesWtocmfCalib = _TnPowerMgmtTechnologyTypesWtocmfCalib_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 7),
    _TnPowerMgmtTechnologyTypesWtocmfCalib_Type()
)
tnPowerMgmtTechnologyTypesWtocmfCalib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfCalib.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfCalib.setUnits("mB")


class _TnPowerMgmtTechnologyTypesWtocmfLCalib_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesWtocmfLCalib based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesWtocmfLCalib_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesWtocmfLCalib_Object = MibTableColumn
tnPowerMgmtTechnologyTypesWtocmfLCalib = _TnPowerMgmtTechnologyTypesWtocmfLCalib_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 8),
    _TnPowerMgmtTechnologyTypesWtocmfLCalib_Type()
)
tnPowerMgmtTechnologyTypesWtocmfLCalib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfLCalib.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfLCalib.setUnits("mB")


class _TnPowerMgmtTechnologyTypesWtocmfCalib375_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesWtocmfCalib375 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesWtocmfCalib375_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesWtocmfCalib375_Object = MibTableColumn
tnPowerMgmtTechnologyTypesWtocmfCalib375 = _TnPowerMgmtTechnologyTypesWtocmfCalib375_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 9),
    _TnPowerMgmtTechnologyTypesWtocmfCalib375_Type()
)
tnPowerMgmtTechnologyTypesWtocmfCalib375.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfCalib375.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfCalib375.setUnits("mB")


class _TnPowerMgmtTechnologyTypesWtocmfLCalib375_Type(Integer32):
    """Custom type tnPowerMgmtTechnologyTypesWtocmfLCalib375 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtTechnologyTypesWtocmfLCalib375_Type.__name__ = "Integer32"
_TnPowerMgmtTechnologyTypesWtocmfLCalib375_Object = MibTableColumn
tnPowerMgmtTechnologyTypesWtocmfLCalib375 = _TnPowerMgmtTechnologyTypesWtocmfLCalib375_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 10),
    _TnPowerMgmtTechnologyTypesWtocmfLCalib375_Type()
)
tnPowerMgmtTechnologyTypesWtocmfLCalib375.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfLCalib375.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesWtocmfLCalib375.setUnits("mB")
_TnPowerMgmtTechnologyTypesMinXCWidthValue_Type = Unsigned32
_TnPowerMgmtTechnologyTypesMinXCWidthValue_Object = MibTableColumn
tnPowerMgmtTechnologyTypesMinXCWidthValue = _TnPowerMgmtTechnologyTypesMinXCWidthValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 13, 1, 11),
    _TnPowerMgmtTechnologyTypesMinXCWidthValue_Type()
)
tnPowerMgmtTechnologyTypesMinXCWidthValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesMinXCWidthValue.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesMinXCWidthValue.setUnits("MHz")
_TnPowerMgmtAnyAddTable_Object = MibTable
tnPowerMgmtAnyAddTable = _TnPowerMgmtAnyAddTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14)
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddTable.setStatus("current")
_TnPowerMgmtAnyAddEntry_Object = MibTableRow
tnPowerMgmtAnyAddEntry = _TnPowerMgmtAnyAddEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1)
)
tnPowerMgmtAnyAddEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddEntry.setStatus("current")
_TnPowerMgmtAnyAddAdjustPowerGain_Type = TnCommand
_TnPowerMgmtAnyAddAdjustPowerGain_Object = MibTableColumn
tnPowerMgmtAnyAddAdjustPowerGain = _TnPowerMgmtAnyAddAdjustPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 1),
    _TnPowerMgmtAnyAddAdjustPowerGain_Type()
)
tnPowerMgmtAnyAddAdjustPowerGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAdjustPowerGain.setStatus("current")


class _TnPowerMgmtAnyAddAdjustPowerGainLastResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtAnyAddAdjustPowerGainLastResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtAnyAddAdjustPowerGainLastResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtAnyAddAdjustPowerGainLastResult_Object = MibTableColumn
tnPowerMgmtAnyAddAdjustPowerGainLastResult = _TnPowerMgmtAnyAddAdjustPowerGainLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 2),
    _TnPowerMgmtAnyAddAdjustPowerGainLastResult_Type()
)
tnPowerMgmtAnyAddAdjustPowerGainLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAdjustPowerGainLastResult.setStatus("current")


class _TnPowerMgmtAnyAddAdjustPowerGainStatus_Type(TropicPowerMgmtStatus):
    """Custom type tnPowerMgmtAnyAddAdjustPowerGainStatus based on TropicPowerMgmtStatus"""
    defaultValue = 1


_TnPowerMgmtAnyAddAdjustPowerGainStatus_Type.__name__ = "TropicPowerMgmtStatus"
_TnPowerMgmtAnyAddAdjustPowerGainStatus_Object = MibTableColumn
tnPowerMgmtAnyAddAdjustPowerGainStatus = _TnPowerMgmtAnyAddAdjustPowerGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 3),
    _TnPowerMgmtAnyAddAdjustPowerGainStatus_Type()
)
tnPowerMgmtAnyAddAdjustPowerGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAdjustPowerGainStatus.setStatus("current")


class _TnPowerMgmtAnyAddCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtAnyAddCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtAnyAddCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtAnyAddCommissioned_Object = MibTableColumn
tnPowerMgmtAnyAddCommissioned = _TnPowerMgmtAnyAddCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 4),
    _TnPowerMgmtAnyAddCommissioned_Type()
)
tnPowerMgmtAnyAddCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddCommissioned.setStatus("current")


class _TnPowerMgmtAnyAddPassed_Type(TruthValue):
    """Custom type tnPowerMgmtAnyAddPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtAnyAddPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtAnyAddPassed_Object = MibTableColumn
tnPowerMgmtAnyAddPassed = _TnPowerMgmtAnyAddPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 5),
    _TnPowerMgmtAnyAddPassed_Type()
)
tnPowerMgmtAnyAddPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddPassed.setStatus("current")
_TnPowerMgmtAnyAddAmpIfIndex_Type = InterfaceIndex
_TnPowerMgmtAnyAddAmpIfIndex_Object = MibTableColumn
tnPowerMgmtAnyAddAmpIfIndex = _TnPowerMgmtAnyAddAmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 6),
    _TnPowerMgmtAnyAddAmpIfIndex_Type()
)
tnPowerMgmtAnyAddAmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAmpIfIndex.setStatus("current")
_TnPowerMgmtAnyAddAdjustPowerGainAbort_Type = TnCommand
_TnPowerMgmtAnyAddAdjustPowerGainAbort_Object = MibTableColumn
tnPowerMgmtAnyAddAdjustPowerGainAbort = _TnPowerMgmtAnyAddAdjustPowerGainAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 14, 1, 7),
    _TnPowerMgmtAnyAddAdjustPowerGainAbort_Type()
)
tnPowerMgmtAnyAddAdjustPowerGainAbort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddAdjustPowerGainAbort.setStatus("current")
_TnPowerMgmtAnyDropTable_Object = MibTable
tnPowerMgmtAnyDropTable = _TnPowerMgmtAnyDropTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15)
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropTable.setStatus("current")
_TnPowerMgmtAnyDropEntry_Object = MibTableRow
tnPowerMgmtAnyDropEntry = _TnPowerMgmtAnyDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1)
)
tnPowerMgmtAnyDropEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropEntry.setStatus("current")
_TnPowerMgmtAnyDropAdjustPowerGain_Type = TnCommand
_TnPowerMgmtAnyDropAdjustPowerGain_Object = MibTableColumn
tnPowerMgmtAnyDropAdjustPowerGain = _TnPowerMgmtAnyDropAdjustPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 1),
    _TnPowerMgmtAnyDropAdjustPowerGain_Type()
)
tnPowerMgmtAnyDropAdjustPowerGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropAdjustPowerGain.setStatus("current")


class _TnPowerMgmtAnyDropAdjustPowerGainLastResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtAnyDropAdjustPowerGainLastResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtAnyDropAdjustPowerGainLastResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtAnyDropAdjustPowerGainLastResult_Object = MibTableColumn
tnPowerMgmtAnyDropAdjustPowerGainLastResult = _TnPowerMgmtAnyDropAdjustPowerGainLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 2),
    _TnPowerMgmtAnyDropAdjustPowerGainLastResult_Type()
)
tnPowerMgmtAnyDropAdjustPowerGainLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropAdjustPowerGainLastResult.setStatus("current")


class _TnPowerMgmtAnyDropAdjustPowerGainStatus_Type(TropicPowerMgmtStatus):
    """Custom type tnPowerMgmtAnyDropAdjustPowerGainStatus based on TropicPowerMgmtStatus"""
    defaultValue = 1


_TnPowerMgmtAnyDropAdjustPowerGainStatus_Type.__name__ = "TropicPowerMgmtStatus"
_TnPowerMgmtAnyDropAdjustPowerGainStatus_Object = MibTableColumn
tnPowerMgmtAnyDropAdjustPowerGainStatus = _TnPowerMgmtAnyDropAdjustPowerGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 3),
    _TnPowerMgmtAnyDropAdjustPowerGainStatus_Type()
)
tnPowerMgmtAnyDropAdjustPowerGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropAdjustPowerGainStatus.setStatus("current")


class _TnPowerMgmtAnyDropCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtAnyDropCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtAnyDropCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtAnyDropCommissioned_Object = MibTableColumn
tnPowerMgmtAnyDropCommissioned = _TnPowerMgmtAnyDropCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 4),
    _TnPowerMgmtAnyDropCommissioned_Type()
)
tnPowerMgmtAnyDropCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropCommissioned.setStatus("current")


class _TnPowerMgmtAnyDropPassed_Type(TruthValue):
    """Custom type tnPowerMgmtAnyDropPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtAnyDropPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtAnyDropPassed_Object = MibTableColumn
tnPowerMgmtAnyDropPassed = _TnPowerMgmtAnyDropPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 5),
    _TnPowerMgmtAnyDropPassed_Type()
)
tnPowerMgmtAnyDropPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropPassed.setStatus("current")
_TnPowerMgmtAnyDropAmpIfIndex_Type = InterfaceIndex
_TnPowerMgmtAnyDropAmpIfIndex_Object = MibTableColumn
tnPowerMgmtAnyDropAmpIfIndex = _TnPowerMgmtAnyDropAmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 15, 1, 6),
    _TnPowerMgmtAnyDropAmpIfIndex_Type()
)
tnPowerMgmtAnyDropAmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropAmpIfIndex.setStatus("current")
_TnPowerMgmtIroadmAttributeTotal_Type = Integer32
_TnPowerMgmtIroadmAttributeTotal_Object = MibScalar
tnPowerMgmtIroadmAttributeTotal = _TnPowerMgmtIroadmAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 16),
    _TnPowerMgmtIroadmAttributeTotal_Type()
)
tnPowerMgmtIroadmAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIroadmAttributeTotal.setStatus("current")
_TnPowerMgmtIroadmTable_Object = MibTable
tnPowerMgmtIroadmTable = _TnPowerMgmtIroadmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 17)
)
if mibBuilder.loadTexts:
    tnPowerMgmtIroadmTable.setStatus("current")
_TnPowerMgmtIroadmEntry_Object = MibTableRow
tnPowerMgmtIroadmEntry = _TnPowerMgmtIroadmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 17, 1)
)
tnPowerMgmtIroadmEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtIroadmEntry.setStatus("current")
_TnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs_Type = Integer32
_TnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs_Object = MibTableColumn
tnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs = _TnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 17, 1, 1),
    _TnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs_Type()
)
tnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs.setUnits("mBm")
_TnPowerMgmtIroadmEgressOAPpcOut_Type = Integer32
_TnPowerMgmtIroadmEgressOAPpcOut_Object = MibTableColumn
tnPowerMgmtIroadmEgressOAPpcOut = _TnPowerMgmtIroadmEgressOAPpcOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 17, 1, 2),
    _TnPowerMgmtIroadmEgressOAPpcOut_Type()
)
tnPowerMgmtIroadmEgressOAPpcOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIroadmEgressOAPpcOut.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIroadmEgressOAPpcOut.setUnits("mBm")
_TnPowerMgmtCapabilitiesCardAttributeTotal_Type = Integer32
_TnPowerMgmtCapabilitiesCardAttributeTotal_Object = MibScalar
tnPowerMgmtCapabilitiesCardAttributeTotal = _TnPowerMgmtCapabilitiesCardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 18),
    _TnPowerMgmtCapabilitiesCardAttributeTotal_Type()
)
tnPowerMgmtCapabilitiesCardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesCardAttributeTotal.setStatus("current")
_TnPowerMgmtCapabilitiesCardTable_Object = MibTable
tnPowerMgmtCapabilitiesCardTable = _TnPowerMgmtCapabilitiesCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 19)
)
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesCardTable.setStatus("current")
_TnPowerMgmtCapabilitiesCardEntry_Object = MibTableRow
tnPowerMgmtCapabilitiesCardEntry = _TnPowerMgmtCapabilitiesCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 19, 1)
)
tnPowerMgmtCapabilitiesCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesCardEntry.setStatus("current")


class _TnPowerMgmtCapabilitiesCardEgressPower_Type(TropicPowerMgmtCapabilitiesCard):
    """Custom type tnPowerMgmtCapabilitiesCardEgressPower based on TropicPowerMgmtCapabilitiesCard"""
    defaultValue = 1


_TnPowerMgmtCapabilitiesCardEgressPower_Type.__name__ = "TropicPowerMgmtCapabilitiesCard"
_TnPowerMgmtCapabilitiesCardEgressPower_Object = MibTableColumn
tnPowerMgmtCapabilitiesCardEgressPower = _TnPowerMgmtCapabilitiesCardEgressPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 19, 1, 1),
    _TnPowerMgmtCapabilitiesCardEgressPower_Type()
)
tnPowerMgmtCapabilitiesCardEgressPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesCardEgressPower.setStatus("current")


class _TnPowerMgmtCapabilitiesCardIngressPower_Type(TropicPowerMgmtCapabilitiesCard):
    """Custom type tnPowerMgmtCapabilitiesCardIngressPower based on TropicPowerMgmtCapabilitiesCard"""
    defaultValue = 1


_TnPowerMgmtCapabilitiesCardIngressPower_Type.__name__ = "TropicPowerMgmtCapabilitiesCard"
_TnPowerMgmtCapabilitiesCardIngressPower_Object = MibTableColumn
tnPowerMgmtCapabilitiesCardIngressPower = _TnPowerMgmtCapabilitiesCardIngressPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 19, 1, 2),
    _TnPowerMgmtCapabilitiesCardIngressPower_Type()
)
tnPowerMgmtCapabilitiesCardIngressPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesCardIngressPower.setStatus("current")


class _TnPowerMgmtCapabilitiesCardEgressTilt_Type(TropicPowerMgmtCapabilitiesCard):
    """Custom type tnPowerMgmtCapabilitiesCardEgressTilt based on TropicPowerMgmtCapabilitiesCard"""
    defaultValue = 1


_TnPowerMgmtCapabilitiesCardEgressTilt_Type.__name__ = "TropicPowerMgmtCapabilitiesCard"
_TnPowerMgmtCapabilitiesCardEgressTilt_Object = MibTableColumn
tnPowerMgmtCapabilitiesCardEgressTilt = _TnPowerMgmtCapabilitiesCardEgressTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 19, 1, 3),
    _TnPowerMgmtCapabilitiesCardEgressTilt_Type()
)
tnPowerMgmtCapabilitiesCardEgressTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesCardEgressTilt.setStatus("current")


class _TnPowerMgmtCapabilitiesCardIngressTilt_Type(TropicPowerMgmtCapabilitiesCard):
    """Custom type tnPowerMgmtCapabilitiesCardIngressTilt based on TropicPowerMgmtCapabilitiesCard"""
    defaultValue = 1


_TnPowerMgmtCapabilitiesCardIngressTilt_Type.__name__ = "TropicPowerMgmtCapabilitiesCard"
_TnPowerMgmtCapabilitiesCardIngressTilt_Object = MibTableColumn
tnPowerMgmtCapabilitiesCardIngressTilt = _TnPowerMgmtCapabilitiesCardIngressTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 19, 1, 4),
    _TnPowerMgmtCapabilitiesCardIngressTilt_Type()
)
tnPowerMgmtCapabilitiesCardIngressTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesCardIngressTilt.setStatus("current")
_TnPowerMgmtIngressPortTable_Object = MibTable
tnPowerMgmtIngressPortTable = _TnPowerMgmtIngressPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20)
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortTable.setStatus("current")
_TnPowerMgmtIngressPortEntry_Object = MibTableRow
tnPowerMgmtIngressPortEntry = _TnPowerMgmtIngressPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1)
)
tnPowerMgmtIngressPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortEntry.setStatus("current")


class _TnPowerMgmtIngressPortAdjustPowerGain_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortAdjustPowerGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("execute", 2),
          ("executeWithForce", 3))
    )


_TnPowerMgmtIngressPortAdjustPowerGain_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortAdjustPowerGain_Object = MibTableColumn
tnPowerMgmtIngressPortAdjustPowerGain = _TnPowerMgmtIngressPortAdjustPowerGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 1),
    _TnPowerMgmtIngressPortAdjustPowerGain_Type()
)
tnPowerMgmtIngressPortAdjustPowerGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortAdjustPowerGain.setStatus("current")
_TnPowerMgmtIngressPortAdjustPowerGainLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtIngressPortAdjustPowerGainLastResult_Object = MibTableColumn
tnPowerMgmtIngressPortAdjustPowerGainLastResult = _TnPowerMgmtIngressPortAdjustPowerGainLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 2),
    _TnPowerMgmtIngressPortAdjustPowerGainLastResult_Type()
)
tnPowerMgmtIngressPortAdjustPowerGainLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortAdjustPowerGainLastResult.setStatus("current")
_TnPowerMgmtIngressPortAdjustPowerGainStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtIngressPortAdjustPowerGainStatus_Object = MibTableColumn
tnPowerMgmtIngressPortAdjustPowerGainStatus = _TnPowerMgmtIngressPortAdjustPowerGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 3),
    _TnPowerMgmtIngressPortAdjustPowerGainStatus_Type()
)
tnPowerMgmtIngressPortAdjustPowerGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortAdjustPowerGainStatus.setStatus("current")


class _TnPowerMgmtIngressPortSRSTiltAdjStatus_Type(AluWdmPowerMgmtSRSTiltAdjStatus):
    """Custom type tnPowerMgmtIngressPortSRSTiltAdjStatus based on AluWdmPowerMgmtSRSTiltAdjStatus"""
    defaultValue = 3


_TnPowerMgmtIngressPortSRSTiltAdjStatus_Type.__name__ = "AluWdmPowerMgmtSRSTiltAdjStatus"
_TnPowerMgmtIngressPortSRSTiltAdjStatus_Object = MibTableColumn
tnPowerMgmtIngressPortSRSTiltAdjStatus = _TnPowerMgmtIngressPortSRSTiltAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 4),
    _TnPowerMgmtIngressPortSRSTiltAdjStatus_Type()
)
tnPowerMgmtIngressPortSRSTiltAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltAdjStatus.setStatus("current")


class _TnPowerMgmtIngressPortSRSTiltAdjResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtIngressPortSRSTiltAdjResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtIngressPortSRSTiltAdjResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtIngressPortSRSTiltAdjResult_Object = MibTableColumn
tnPowerMgmtIngressPortSRSTiltAdjResult = _TnPowerMgmtIngressPortSRSTiltAdjResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 5),
    _TnPowerMgmtIngressPortSRSTiltAdjResult_Type()
)
tnPowerMgmtIngressPortSRSTiltAdjResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltAdjResult.setStatus("current")


class _TnPowerMgmtIngressPortSRSTiltPostFraction_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortSRSTiltPostFraction based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressPortSRSTiltPostFraction_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortSRSTiltPostFraction_Object = MibTableColumn
tnPowerMgmtIngressPortSRSTiltPostFraction = _TnPowerMgmtIngressPortSRSTiltPostFraction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 6),
    _TnPowerMgmtIngressPortSRSTiltPostFraction_Type()
)
tnPowerMgmtIngressPortSRSTiltPostFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltPostFraction.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltPostFraction.setUnits("100ths")


class _TnPowerMgmtIngressPortSRSTiltPostFractionL_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortSRSTiltPostFractionL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressPortSRSTiltPostFractionL_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortSRSTiltPostFractionL_Object = MibTableColumn
tnPowerMgmtIngressPortSRSTiltPostFractionL = _TnPowerMgmtIngressPortSRSTiltPostFractionL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 7),
    _TnPowerMgmtIngressPortSRSTiltPostFractionL_Type()
)
tnPowerMgmtIngressPortSRSTiltPostFractionL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltPostFractionL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltPostFractionL.setUnits("100ths")


class _TnPowerMgmtIngressPortCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtIngressPortCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtIngressPortCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtIngressPortCommissioned_Object = MibTableColumn
tnPowerMgmtIngressPortCommissioned = _TnPowerMgmtIngressPortCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 8),
    _TnPowerMgmtIngressPortCommissioned_Type()
)
tnPowerMgmtIngressPortCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortCommissioned.setStatus("current")


class _TnPowerMgmtIngressPortPassed_Type(TruthValue):
    """Custom type tnPowerMgmtIngressPortPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtIngressPortPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtIngressPortPassed_Object = MibTableColumn
tnPowerMgmtIngressPortPassed = _TnPowerMgmtIngressPortPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 9),
    _TnPowerMgmtIngressPortPassed_Type()
)
tnPowerMgmtIngressPortPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPassed.setStatus("current")


class _TnPowerMgmtIngressPortGainSetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortGainSetOffset based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressPortGainSetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortGainSetOffset_Object = MibTableColumn
tnPowerMgmtIngressPortGainSetOffset = _TnPowerMgmtIngressPortGainSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 10),
    _TnPowerMgmtIngressPortGainSetOffset_Type()
)
tnPowerMgmtIngressPortGainSetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortGainSetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortGainSetOffset.setUnits("mB")


class _TnPowerMgmtIngressPortGainSetOffsetL_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortGainSetOffsetL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressPortGainSetOffsetL_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortGainSetOffsetL_Object = MibTableColumn
tnPowerMgmtIngressPortGainSetOffsetL = _TnPowerMgmtIngressPortGainSetOffsetL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 11),
    _TnPowerMgmtIngressPortGainSetOffsetL_Type()
)
tnPowerMgmtIngressPortGainSetOffsetL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortGainSetOffsetL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortGainSetOffsetL.setUnits("mB")
_TnPowerMgmtIngressPortAdjustPowerGainTargetGain_Type = Unsigned32
_TnPowerMgmtIngressPortAdjustPowerGainTargetGain_Object = MibTableColumn
tnPowerMgmtIngressPortAdjustPowerGainTargetGain = _TnPowerMgmtIngressPortAdjustPowerGainTargetGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 12),
    _TnPowerMgmtIngressPortAdjustPowerGainTargetGain_Type()
)
tnPowerMgmtIngressPortAdjustPowerGainTargetGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortAdjustPowerGainTargetGain.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortAdjustPowerGainTargetGain.setUnits("mB")
_TnPowerMgmtIngressPortAdjustPowerGainTargetGainL_Type = Unsigned32
_TnPowerMgmtIngressPortAdjustPowerGainTargetGainL_Object = MibTableColumn
tnPowerMgmtIngressPortAdjustPowerGainTargetGainL = _TnPowerMgmtIngressPortAdjustPowerGainTargetGainL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 13),
    _TnPowerMgmtIngressPortAdjustPowerGainTargetGainL_Type()
)
tnPowerMgmtIngressPortAdjustPowerGainTargetGainL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortAdjustPowerGainTargetGainL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortAdjustPowerGainTargetGainL.setUnits("mB")


class _TnPowerMgmtIngressPortCommissionedGain_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortCommissionedGain based on Integer32"""
    defaultValue = 0


_TnPowerMgmtIngressPortCommissionedGain_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortCommissionedGain_Object = MibTableColumn
tnPowerMgmtIngressPortCommissionedGain = _TnPowerMgmtIngressPortCommissionedGain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 14),
    _TnPowerMgmtIngressPortCommissionedGain_Type()
)
tnPowerMgmtIngressPortCommissionedGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortCommissionedGain.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortCommissionedGain.setUnits("mB")
_TnPowerMgmtIngressPortCommissionedGainL_Type = Integer32
_TnPowerMgmtIngressPortCommissionedGainL_Object = MibTableColumn
tnPowerMgmtIngressPortCommissionedGainL = _TnPowerMgmtIngressPortCommissionedGainL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 15),
    _TnPowerMgmtIngressPortCommissionedGainL_Type()
)
tnPowerMgmtIngressPortCommissionedGainL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortCommissionedGainL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortCommissionedGainL.setUnits("mB")


class _TnPowerMgmtIngressPortSRSTiltCalcOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortSRSTiltCalcOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtIngressPortSRSTiltCalcOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortSRSTiltCalcOffset_Object = MibTableColumn
tnPowerMgmtIngressPortSRSTiltCalcOffset = _TnPowerMgmtIngressPortSRSTiltCalcOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 16),
    _TnPowerMgmtIngressPortSRSTiltCalcOffset_Type()
)
tnPowerMgmtIngressPortSRSTiltCalcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltCalcOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltCalcOffset.setUnits("mB")


class _TnPowerMgmtIngressPortSRSTiltCalcOffsetL_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortSRSTiltCalcOffsetL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_TnPowerMgmtIngressPortSRSTiltCalcOffsetL_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortSRSTiltCalcOffsetL_Object = MibTableColumn
tnPowerMgmtIngressPortSRSTiltCalcOffsetL = _TnPowerMgmtIngressPortSRSTiltCalcOffsetL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 20, 1, 17),
    _TnPowerMgmtIngressPortSRSTiltCalcOffsetL_Type()
)
tnPowerMgmtIngressPortSRSTiltCalcOffsetL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltCalcOffsetL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortSRSTiltCalcOffsetL.setUnits("mB")
_TnPowerMgmtEgressPortTable_Object = MibTable
tnPowerMgmtEgressPortTable = _TnPowerMgmtEgressPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21)
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortTable.setStatus("current")
_TnPowerMgmtEgressPortEntry_Object = MibTableRow
tnPowerMgmtEgressPortEntry = _TnPowerMgmtEgressPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1)
)
tnPowerMgmtEgressPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortEntry.setStatus("current")
_TnPowerMgmtEgressPortAdjustPowerWithOptimization_Type = TnCommand
_TnPowerMgmtEgressPortAdjustPowerWithOptimization_Object = MibTableColumn
tnPowerMgmtEgressPortAdjustPowerWithOptimization = _TnPowerMgmtEgressPortAdjustPowerWithOptimization_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 1),
    _TnPowerMgmtEgressPortAdjustPowerWithOptimization_Type()
)
tnPowerMgmtEgressPortAdjustPowerWithOptimization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortAdjustPowerWithOptimization.setStatus("current")
_TnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort_Type = TnCommand
_TnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort_Object = MibTableColumn
tnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort = _TnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 2),
    _TnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort_Type()
)
tnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort.setStatus("current")
_TnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult_Type = TropicPowerMgmtResult
_TnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult_Object = MibTableColumn
tnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult = _TnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 3),
    _TnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult_Type()
)
tnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult.setStatus("current")
_TnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus_Type = TropicPowerMgmtStatus
_TnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus_Object = MibTableColumn
tnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus = _TnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 4),
    _TnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus_Type()
)
tnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus.setStatus("current")


class _TnPowerMgmtEgressPortSRSTiltCalcOutputLoss_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortSRSTiltCalcOutputLoss based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressPortSRSTiltCalcOutputLoss_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortSRSTiltCalcOutputLoss_Object = MibTableColumn
tnPowerMgmtEgressPortSRSTiltCalcOutputLoss = _TnPowerMgmtEgressPortSRSTiltCalcOutputLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 5),
    _TnPowerMgmtEgressPortSRSTiltCalcOutputLoss_Type()
)
tnPowerMgmtEgressPortSRSTiltCalcOutputLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltCalcOutputLoss.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltCalcOutputLoss.setUnits("mB")


class _TnPowerMgmtEgressPortSRSTiltAdjStatus_Type(AluWdmPowerMgmtSRSTiltAdjStatus):
    """Custom type tnPowerMgmtEgressPortSRSTiltAdjStatus based on AluWdmPowerMgmtSRSTiltAdjStatus"""
    defaultValue = 3


_TnPowerMgmtEgressPortSRSTiltAdjStatus_Type.__name__ = "AluWdmPowerMgmtSRSTiltAdjStatus"
_TnPowerMgmtEgressPortSRSTiltAdjStatus_Object = MibTableColumn
tnPowerMgmtEgressPortSRSTiltAdjStatus = _TnPowerMgmtEgressPortSRSTiltAdjStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 6),
    _TnPowerMgmtEgressPortSRSTiltAdjStatus_Type()
)
tnPowerMgmtEgressPortSRSTiltAdjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltAdjStatus.setStatus("current")


class _TnPowerMgmtEgressPortSRSTIltAdjResult_Type(TropicPowerMgmtResult):
    """Custom type tnPowerMgmtEgressPortSRSTIltAdjResult based on TropicPowerMgmtResult"""
    defaultValue = OctetString("Not applicable")


_TnPowerMgmtEgressPortSRSTIltAdjResult_Type.__name__ = "TropicPowerMgmtResult"
_TnPowerMgmtEgressPortSRSTIltAdjResult_Object = MibTableColumn
tnPowerMgmtEgressPortSRSTIltAdjResult = _TnPowerMgmtEgressPortSRSTIltAdjResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 7),
    _TnPowerMgmtEgressPortSRSTIltAdjResult_Type()
)
tnPowerMgmtEgressPortSRSTIltAdjResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTIltAdjResult.setStatus("current")


class _TnPowerMgmtEgressPortSRSTiltCalcACoeff_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortSRSTiltCalcACoeff based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressPortSRSTiltCalcACoeff_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortSRSTiltCalcACoeff_Object = MibTableColumn
tnPowerMgmtEgressPortSRSTiltCalcACoeff = _TnPowerMgmtEgressPortSRSTiltCalcACoeff_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 8),
    _TnPowerMgmtEgressPortSRSTiltCalcACoeff_Type()
)
tnPowerMgmtEgressPortSRSTiltCalcACoeff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltCalcACoeff.setStatus("current")


class _TnPowerMgmtEgressPortSRSTiltCalcACoeffL_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortSRSTiltCalcACoeffL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressPortSRSTiltCalcACoeffL_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortSRSTiltCalcACoeffL_Object = MibTableColumn
tnPowerMgmtEgressPortSRSTiltCalcACoeffL = _TnPowerMgmtEgressPortSRSTiltCalcACoeffL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 9),
    _TnPowerMgmtEgressPortSRSTiltCalcACoeffL_Type()
)
tnPowerMgmtEgressPortSRSTiltCalcACoeffL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltCalcACoeffL.setStatus("current")


class _TnPowerMgmtEgressPortSRSTiltCalcMultiplier_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortSRSTiltCalcMultiplier based on Integer32"""
    defaultValue = 100


_TnPowerMgmtEgressPortSRSTiltCalcMultiplier_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortSRSTiltCalcMultiplier_Object = MibTableColumn
tnPowerMgmtEgressPortSRSTiltCalcMultiplier = _TnPowerMgmtEgressPortSRSTiltCalcMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 10),
    _TnPowerMgmtEgressPortSRSTiltCalcMultiplier_Type()
)
tnPowerMgmtEgressPortSRSTiltCalcMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltCalcMultiplier.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltCalcMultiplier.setUnits("100ths")


class _TnPowerMgmtEgressPortSRSTiltCalcMultiplierL_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortSRSTiltCalcMultiplierL based on Integer32"""
    defaultValue = 100


_TnPowerMgmtEgressPortSRSTiltCalcMultiplierL_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortSRSTiltCalcMultiplierL_Object = MibTableColumn
tnPowerMgmtEgressPortSRSTiltCalcMultiplierL = _TnPowerMgmtEgressPortSRSTiltCalcMultiplierL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 11),
    _TnPowerMgmtEgressPortSRSTiltCalcMultiplierL_Type()
)
tnPowerMgmtEgressPortSRSTiltCalcMultiplierL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltCalcMultiplierL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltCalcMultiplierL.setUnits("100ths")


class _TnPowerMgmtEgressPortFiberSpanTiltPreComp_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortFiberSpanTiltPreComp based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressPortFiberSpanTiltPreComp_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortFiberSpanTiltPreComp_Object = MibTableColumn
tnPowerMgmtEgressPortFiberSpanTiltPreComp = _TnPowerMgmtEgressPortFiberSpanTiltPreComp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 12),
    _TnPowerMgmtEgressPortFiberSpanTiltPreComp_Type()
)
tnPowerMgmtEgressPortFiberSpanTiltPreComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortFiberSpanTiltPreComp.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortFiberSpanTiltPreComp.setUnits("mB")


class _TnPowerMgmtEgressPortFiberSpanTiltPreCompL_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortFiberSpanTiltPreCompL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressPortFiberSpanTiltPreCompL_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortFiberSpanTiltPreCompL_Object = MibTableColumn
tnPowerMgmtEgressPortFiberSpanTiltPreCompL = _TnPowerMgmtEgressPortFiberSpanTiltPreCompL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 13),
    _TnPowerMgmtEgressPortFiberSpanTiltPreCompL_Type()
)
tnPowerMgmtEgressPortFiberSpanTiltPreCompL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortFiberSpanTiltPreCompL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortFiberSpanTiltPreCompL.setUnits("mB")


class _TnPowerMgmtEgressPortSRSCF_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortSRSCF based on Integer32"""
    defaultValue = 100


_TnPowerMgmtEgressPortSRSCF_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortSRSCF_Object = MibTableColumn
tnPowerMgmtEgressPortSRSCF = _TnPowerMgmtEgressPortSRSCF_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 14),
    _TnPowerMgmtEgressPortSRSCF_Type()
)
tnPowerMgmtEgressPortSRSCF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSCF.setStatus("current")


class _TnPowerMgmtEgressPortSRSCFL_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortSRSCFL based on Integer32"""
    defaultValue = 100


_TnPowerMgmtEgressPortSRSCFL_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortSRSCFL_Object = MibTableColumn
tnPowerMgmtEgressPortSRSCFL = _TnPowerMgmtEgressPortSRSCFL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 15),
    _TnPowerMgmtEgressPortSRSCFL_Type()
)
tnPowerMgmtEgressPortSRSCFL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSCFL.setStatus("current")


class _TnPowerMgmtEgressPortSRSTiltPreFraction_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortSRSTiltPreFraction based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressPortSRSTiltPreFraction_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortSRSTiltPreFraction_Object = MibTableColumn
tnPowerMgmtEgressPortSRSTiltPreFraction = _TnPowerMgmtEgressPortSRSTiltPreFraction_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 16),
    _TnPowerMgmtEgressPortSRSTiltPreFraction_Type()
)
tnPowerMgmtEgressPortSRSTiltPreFraction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltPreFraction.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltPreFraction.setUnits("100ths")


class _TnPowerMgmtEgressPortSRSTiltPreFractionL_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortSRSTiltPreFractionL based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressPortSRSTiltPreFractionL_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortSRSTiltPreFractionL_Object = MibTableColumn
tnPowerMgmtEgressPortSRSTiltPreFractionL = _TnPowerMgmtEgressPortSRSTiltPreFractionL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 17),
    _TnPowerMgmtEgressPortSRSTiltPreFractionL_Type()
)
tnPowerMgmtEgressPortSRSTiltPreFractionL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltPreFractionL.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSRSTiltPreFractionL.setUnits("100ths")


class _TnPowerMgmtEgressPortCommissioned_Type(TruthValue):
    """Custom type tnPowerMgmtEgressPortCommissioned based on TruthValue"""
    defaultValue = 2


_TnPowerMgmtEgressPortCommissioned_Type.__name__ = "TruthValue"
_TnPowerMgmtEgressPortCommissioned_Object = MibTableColumn
tnPowerMgmtEgressPortCommissioned = _TnPowerMgmtEgressPortCommissioned_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 18),
    _TnPowerMgmtEgressPortCommissioned_Type()
)
tnPowerMgmtEgressPortCommissioned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortCommissioned.setStatus("current")


class _TnPowerMgmtEgressPortPassed_Type(TruthValue):
    """Custom type tnPowerMgmtEgressPortPassed based on TruthValue"""
    defaultValue = 1


_TnPowerMgmtEgressPortPassed_Type.__name__ = "TruthValue"
_TnPowerMgmtEgressPortPassed_Object = MibTableColumn
tnPowerMgmtEgressPortPassed = _TnPowerMgmtEgressPortPassed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 19),
    _TnPowerMgmtEgressPortPassed_Type()
)
tnPowerMgmtEgressPortPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPassed.setStatus("current")


class _TnPowerMgmtEgressPortLHLaunchAtten_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortLHLaunchAtten based on Integer32"""
    defaultValue = 0


_TnPowerMgmtEgressPortLHLaunchAtten_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortLHLaunchAtten_Object = MibTableColumn
tnPowerMgmtEgressPortLHLaunchAtten = _TnPowerMgmtEgressPortLHLaunchAtten_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 20),
    _TnPowerMgmtEgressPortLHLaunchAtten_Type()
)
tnPowerMgmtEgressPortLHLaunchAtten.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortLHLaunchAtten.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortLHLaunchAtten.setUnits("mB")


class _TnPowerMgmtEgressPortExternalOTAddLaunchAtten_Type(Unsigned32):
    """Custom type tnPowerMgmtEgressPortExternalOTAddLaunchAtten based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_TnPowerMgmtEgressPortExternalOTAddLaunchAtten_Type.__name__ = "Unsigned32"
_TnPowerMgmtEgressPortExternalOTAddLaunchAtten_Object = MibTableColumn
tnPowerMgmtEgressPortExternalOTAddLaunchAtten = _TnPowerMgmtEgressPortExternalOTAddLaunchAtten_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 21),
    _TnPowerMgmtEgressPortExternalOTAddLaunchAtten_Type()
)
tnPowerMgmtEgressPortExternalOTAddLaunchAtten.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortExternalOTAddLaunchAtten.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortExternalOTAddLaunchAtten.setUnits("mB")
_TnPowerMgmtEgressPortSmoothing_Type = TruthValue
_TnPowerMgmtEgressPortSmoothing_Object = MibTableColumn
tnPowerMgmtEgressPortSmoothing = _TnPowerMgmtEgressPortSmoothing_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 22),
    _TnPowerMgmtEgressPortSmoothing_Type()
)
tnPowerMgmtEgressPortSmoothing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSmoothing.setStatus("current")


class _TnPowerMgmtEgressPortSmoothingMaxStepSize_Type(Unsigned32):
    """Custom type tnPowerMgmtEgressPortSmoothingMaxStepSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_TnPowerMgmtEgressPortSmoothingMaxStepSize_Type.__name__ = "Unsigned32"
_TnPowerMgmtEgressPortSmoothingMaxStepSize_Object = MibTableColumn
tnPowerMgmtEgressPortSmoothingMaxStepSize = _TnPowerMgmtEgressPortSmoothingMaxStepSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 21, 1, 23),
    _TnPowerMgmtEgressPortSmoothingMaxStepSize_Type()
)
tnPowerMgmtEgressPortSmoothingMaxStepSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSmoothingMaxStepSize.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortSmoothingMaxStepSize.setUnits("mB")
_TnPowerMgmtIngressPortPerChannelTable_Object = MibTable
tnPowerMgmtIngressPortPerChannelTable = _TnPowerMgmtIngressPortPerChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 22)
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelTable.setStatus("current")
_TnPowerMgmtIngressPortPerChannelEntry_Object = MibTableRow
tnPowerMgmtIngressPortPerChannelEntry = _TnPowerMgmtIngressPortPerChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 22, 1)
)
tnPowerMgmtIngressPortPerChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelEntry.setStatus("current")


class _TnPowerMgmtIngressPortPerChannelSystemTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortPerChannelSystemTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtIngressPortPerChannelSystemTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortPerChannelSystemTargetOffset_Object = MibTableColumn
tnPowerMgmtIngressPortPerChannelSystemTargetOffset = _TnPowerMgmtIngressPortPerChannelSystemTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 22, 1, 1),
    _TnPowerMgmtIngressPortPerChannelSystemTargetOffset_Type()
)
tnPowerMgmtIngressPortPerChannelSystemTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelSystemTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelSystemTargetOffset.setUnits("mB")


class _TnPowerMgmtIngressPortPerChannelUserTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortPerChannelUserTargetOffset based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressPortPerChannelUserTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortPerChannelUserTargetOffset_Object = MibTableColumn
tnPowerMgmtIngressPortPerChannelUserTargetOffset = _TnPowerMgmtIngressPortPerChannelUserTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 22, 1, 2),
    _TnPowerMgmtIngressPortPerChannelUserTargetOffset_Type()
)
tnPowerMgmtIngressPortPerChannelUserTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelUserTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelUserTargetOffset.setUnits("mB")


class _TnPowerMgmtIngressPortPerChannelInUseTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortPerChannelInUseTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtIngressPortPerChannelInUseTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortPerChannelInUseTargetOffset_Object = MibTableColumn
tnPowerMgmtIngressPortPerChannelInUseTargetOffset = _TnPowerMgmtIngressPortPerChannelInUseTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 22, 1, 3),
    _TnPowerMgmtIngressPortPerChannelInUseTargetOffset_Type()
)
tnPowerMgmtIngressPortPerChannelInUseTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelInUseTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelInUseTargetOffset.setUnits("mB")


class _TnPowerMgmtIngressPortPerChannelTargetAbsolute_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortPerChannelTargetAbsolute based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtIngressPortPerChannelTargetAbsolute_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortPerChannelTargetAbsolute_Object = MibTableColumn
tnPowerMgmtIngressPortPerChannelTargetAbsolute = _TnPowerMgmtIngressPortPerChannelTargetAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 22, 1, 4),
    _TnPowerMgmtIngressPortPerChannelTargetAbsolute_Type()
)
tnPowerMgmtIngressPortPerChannelTargetAbsolute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelTargetAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelTargetAbsolute.setUnits("mBm")


class _TnPowerMgmtIngressPortPerChannelApplicability_Type(Integer32):
    """Custom type tnPowerMgmtIngressPortPerChannelApplicability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("applicable", 2))
    )


_TnPowerMgmtIngressPortPerChannelApplicability_Type.__name__ = "Integer32"
_TnPowerMgmtIngressPortPerChannelApplicability_Object = MibTableColumn
tnPowerMgmtIngressPortPerChannelApplicability = _TnPowerMgmtIngressPortPerChannelApplicability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 22, 1, 5),
    _TnPowerMgmtIngressPortPerChannelApplicability_Type()
)
tnPowerMgmtIngressPortPerChannelApplicability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelApplicability.setStatus("current")
_TnPowerMgmtEgressPortPerChannelTable_Object = MibTable
tnPowerMgmtEgressPortPerChannelTable = _TnPowerMgmtEgressPortPerChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 23)
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelTable.setStatus("current")
_TnPowerMgmtEgressPortPerChannelEntry_Object = MibTableRow
tnPowerMgmtEgressPortPerChannelEntry = _TnPowerMgmtEgressPortPerChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 23, 1)
)
tnPowerMgmtEgressPortPerChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-WAVEKEY-MIB", "tnChannel"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelEntry.setStatus("current")


class _TnPowerMgmtEgressPortPerChannelSystemTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortPerChannelSystemTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtEgressPortPerChannelSystemTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortPerChannelSystemTargetOffset_Object = MibTableColumn
tnPowerMgmtEgressPortPerChannelSystemTargetOffset = _TnPowerMgmtEgressPortPerChannelSystemTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 23, 1, 1),
    _TnPowerMgmtEgressPortPerChannelSystemTargetOffset_Type()
)
tnPowerMgmtEgressPortPerChannelSystemTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelSystemTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelSystemTargetOffset.setUnits("mB")


class _TnPowerMgmtEgressPortPerChannelUserTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortPerChannelUserTargetOffset based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressPortPerChannelUserTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortPerChannelUserTargetOffset_Object = MibTableColumn
tnPowerMgmtEgressPortPerChannelUserTargetOffset = _TnPowerMgmtEgressPortPerChannelUserTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 23, 1, 2),
    _TnPowerMgmtEgressPortPerChannelUserTargetOffset_Type()
)
tnPowerMgmtEgressPortPerChannelUserTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelUserTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelUserTargetOffset.setUnits("mB")


class _TnPowerMgmtEgressPortPerChannelInUseTargetOffset_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortPerChannelInUseTargetOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 300),
    )


_TnPowerMgmtEgressPortPerChannelInUseTargetOffset_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortPerChannelInUseTargetOffset_Object = MibTableColumn
tnPowerMgmtEgressPortPerChannelInUseTargetOffset = _TnPowerMgmtEgressPortPerChannelInUseTargetOffset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 23, 1, 3),
    _TnPowerMgmtEgressPortPerChannelInUseTargetOffset_Type()
)
tnPowerMgmtEgressPortPerChannelInUseTargetOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelInUseTargetOffset.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelInUseTargetOffset.setUnits("mB")


class _TnPowerMgmtEgressPortPerChannelTargetAbsolute_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortPerChannelTargetAbsolute based on Integer32"""
    defaultValue = -9900


_TnPowerMgmtEgressPortPerChannelTargetAbsolute_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortPerChannelTargetAbsolute_Object = MibTableColumn
tnPowerMgmtEgressPortPerChannelTargetAbsolute = _TnPowerMgmtEgressPortPerChannelTargetAbsolute_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 23, 1, 4),
    _TnPowerMgmtEgressPortPerChannelTargetAbsolute_Type()
)
tnPowerMgmtEgressPortPerChannelTargetAbsolute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelTargetAbsolute.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelTargetAbsolute.setUnits("mBm")


class _TnPowerMgmtEgressPortPerChannelApplicability_Type(Integer32):
    """Custom type tnPowerMgmtEgressPortPerChannelApplicability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("applicable", 2))
    )


_TnPowerMgmtEgressPortPerChannelApplicability_Type.__name__ = "Integer32"
_TnPowerMgmtEgressPortPerChannelApplicability_Object = MibTableColumn
tnPowerMgmtEgressPortPerChannelApplicability = _TnPowerMgmtEgressPortPerChannelApplicability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 23, 1, 5),
    _TnPowerMgmtEgressPortPerChannelApplicability_Type()
)
tnPowerMgmtEgressPortPerChannelApplicability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelApplicability.setStatus("current")
_TnPowerMgmtCapabilitiesPortAttributeTotal_Type = Integer32
_TnPowerMgmtCapabilitiesPortAttributeTotal_Object = MibScalar
tnPowerMgmtCapabilitiesPortAttributeTotal = _TnPowerMgmtCapabilitiesPortAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 24),
    _TnPowerMgmtCapabilitiesPortAttributeTotal_Type()
)
tnPowerMgmtCapabilitiesPortAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesPortAttributeTotal.setStatus("current")
_TnPowerMgmtCapabilitiesPortTable_Object = MibTable
tnPowerMgmtCapabilitiesPortTable = _TnPowerMgmtCapabilitiesPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 25)
)
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesPortTable.setStatus("current")
_TnPowerMgmtCapabilitiesPortEntry_Object = MibTableRow
tnPowerMgmtCapabilitiesPortEntry = _TnPowerMgmtCapabilitiesPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 25, 1)
)
tnPowerMgmtCapabilitiesPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesPortEntry.setStatus("current")


class _TnPowerMgmtCapabilitiesPortEgressPower_Type(TropicPowerMgmtCapabilitiesCard):
    """Custom type tnPowerMgmtCapabilitiesPortEgressPower based on TropicPowerMgmtCapabilitiesCard"""
    defaultValue = 1


_TnPowerMgmtCapabilitiesPortEgressPower_Type.__name__ = "TropicPowerMgmtCapabilitiesCard"
_TnPowerMgmtCapabilitiesPortEgressPower_Object = MibTableColumn
tnPowerMgmtCapabilitiesPortEgressPower = _TnPowerMgmtCapabilitiesPortEgressPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 25, 1, 1),
    _TnPowerMgmtCapabilitiesPortEgressPower_Type()
)
tnPowerMgmtCapabilitiesPortEgressPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesPortEgressPower.setStatus("current")


class _TnPowerMgmtCapabilitiesPortIngressPower_Type(TropicPowerMgmtCapabilitiesCard):
    """Custom type tnPowerMgmtCapabilitiesPortIngressPower based on TropicPowerMgmtCapabilitiesCard"""
    defaultValue = 1


_TnPowerMgmtCapabilitiesPortIngressPower_Type.__name__ = "TropicPowerMgmtCapabilitiesCard"
_TnPowerMgmtCapabilitiesPortIngressPower_Object = MibTableColumn
tnPowerMgmtCapabilitiesPortIngressPower = _TnPowerMgmtCapabilitiesPortIngressPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 25, 1, 2),
    _TnPowerMgmtCapabilitiesPortIngressPower_Type()
)
tnPowerMgmtCapabilitiesPortIngressPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesPortIngressPower.setStatus("current")


class _TnPowerMgmtCapabilitiesPortEgressTilt_Type(TropicPowerMgmtCapabilitiesCard):
    """Custom type tnPowerMgmtCapabilitiesPortEgressTilt based on TropicPowerMgmtCapabilitiesCard"""
    defaultValue = 1


_TnPowerMgmtCapabilitiesPortEgressTilt_Type.__name__ = "TropicPowerMgmtCapabilitiesCard"
_TnPowerMgmtCapabilitiesPortEgressTilt_Object = MibTableColumn
tnPowerMgmtCapabilitiesPortEgressTilt = _TnPowerMgmtCapabilitiesPortEgressTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 25, 1, 3),
    _TnPowerMgmtCapabilitiesPortEgressTilt_Type()
)
tnPowerMgmtCapabilitiesPortEgressTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesPortEgressTilt.setStatus("current")


class _TnPowerMgmtCapabilitiesPortIngressTilt_Type(TropicPowerMgmtCapabilitiesCard):
    """Custom type tnPowerMgmtCapabilitiesPortIngressTilt based on TropicPowerMgmtCapabilitiesCard"""
    defaultValue = 1


_TnPowerMgmtCapabilitiesPortIngressTilt_Type.__name__ = "TropicPowerMgmtCapabilitiesCard"
_TnPowerMgmtCapabilitiesPortIngressTilt_Object = MibTableColumn
tnPowerMgmtCapabilitiesPortIngressTilt = _TnPowerMgmtCapabilitiesPortIngressTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 2, 1, 25, 1, 4),
    _TnPowerMgmtCapabilitiesPortIngressTilt_Type()
)
tnPowerMgmtCapabilitiesPortIngressTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesPortIngressTilt.setStatus("current")

# Managed Objects groups

tnPowerMgmtGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 1)
)
tnPowerMgmtGlobalGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalMinStepSize"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalMaxStepSize"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalResetToDefaults"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalAutoEnabled"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalAlarmWhenDisabled"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtGlobalGroup.setStatus("current")

tnPowerMgmtControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 2)
)
tnPowerMgmtControlGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtControlPercentCompleted"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtControlRowStatus"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtControlGroup.setStatus("current")

tnPowerMgmtIngressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 4)
)
tnPowerMgmtIngressGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAdjustPowerGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAdjustPowerGainLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAcceptPowers"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAcceptPowersLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressRippleAllowance"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAdjustPowerGainTargetGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAdjustPowerGainStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressStartAseAdjust"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAseAdjustLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAseAdjustStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressGainSetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressCommissionedGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltPostFraction"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltAdjResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltAdjStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltCalcOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressInternodalOaPpcMaxInCurrent"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressInternodalOaPpcMaxInReference"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressInternodalCalculatedSpanLossInReference"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltPostFractionL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressGainSetOffsetL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressAdjustPowerGainTargetGainL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressCommissionedGainL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressSRSTiltCalcOffsetL"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressGroup.setStatus("current")

tnPowerMgmtEgressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 5)
)
tnPowerMgmtEgressGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimization"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimizationStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimizationAbort"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAcceptPowers"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAcceptPowersLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressStartAseAdjust"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressStopAseAdjust"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAseAdjustLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAseAdjustStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressAmpIfIndex"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressWssIfIndex"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltCalcMultiplier"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltPreFraction"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltCalcACoeff"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltCalcOutputLoss"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltAdjResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltAdjStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressLHLaunchAtten"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtFiberSpanTiltPreComp"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressInternodalPpcMaxInDownstream"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressInternodalSpanLossInDownstream"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressInternodalPpcMaxInDownstreamReference"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressInternodalSpanLossInDownstreamReference"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtFiberSpanTiltPreCompL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltCalcMultiplierL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltPreFractionL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSTiltCalcACoeffL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSCF"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSRSCFL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressExternalOTAddLaunchAtten"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSmoothing"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressSmoothingMaxStepSize"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressGroup.setStatus("current")

tnPowerMgmtPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 7)
)
tnPowerMgmtPortGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortIsCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortTypeIn"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortTypeOut"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortWTDecoderUsageTypeIn"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortWTDecoderUsageTypeOut"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortGainAdjSchedBase"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortGainAdjTimerPeriod"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortGainAdjTimerLength"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortInGainAdjAutoEnabled"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortSRSTiltAdjAutoEnabled"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortFiberSpanTilt"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortSRSTiltMaintenanceMode"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortDegreeFunction"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortMaxChannels"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortEgressAdjustForDownstreamEnabled"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortFiberSpanTiltL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortWTDecoderUsageTypeInL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortWTDecoderUsageTypeOutL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortIsCommissionedMethod"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtPortGroup.setStatus("current")

tnPowerMgmtPowerOffsetInGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 9)
)
tnPowerMgmtPowerOffsetInGroup.setObjects(
    ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtOffsetInPowerOffset")
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetInGroup.setStatus("current")

tnPowerMgmtPowerOffsetOutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 10)
)
tnPowerMgmtPowerOffsetOutGroup.setObjects(
    ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtOffsetOutPowerOffset")
)
if mibBuilder.loadTexts:
    tnPowerMgmtPowerOffsetOutGroup.setStatus("current")

tnPowerMgmtIngressPerChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 11)
)
tnPowerMgmtIngressPerChannelGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelSystemTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelUserTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelInUseTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelTargetAbsolute"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelApplicability"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPerChannelGroup.setStatus("current")

tnPowerMgmtEgressPerChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 12)
)
tnPowerMgmtEgressPerChannelGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelSystemTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelUserTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelInUseTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelTargetAbsolute"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelApplicability"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPerChannelGroup.setStatus("current")

tnPowerMgmtTechnologyTypesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 13)
)
tnPowerMgmtTechnologyTypesGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesBitRateText"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesEncodingText"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesWtocmCalib"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesRowStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesOsnrCalib"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesWtocmaCalib"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesWtocmfCalib"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesWtocmfLCalib"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesWtocmfCalib375"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesWtocmfLCalib375"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesMinXCWidthValue"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtTechnologyTypesGroup.setStatus("current")

tnPowerMgmtAnyAddGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 14)
)
tnPowerMgmtAnyAddGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAdjustPowerGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAdjustPowerGainLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAdjustPowerGainStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAmpIfIndex"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddAdjustPowerGainAbort"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyAddGroup.setStatus("current")

tnPowerMgmtAnyDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 15)
)
tnPowerMgmtAnyDropGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropAdjustPowerGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropAdjustPowerGainLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropAdjustPowerGainStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropAmpIfIndex"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtAnyDropGroup.setStatus("current")

tnPowerMgmtIroadmScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 16)
)
tnPowerMgmtIroadmScalarsGroup.setObjects(
    ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIroadmAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPowerMgmtIroadmScalarsGroup.setStatus("current")

tnPowerMgmtIroadmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 17)
)
tnPowerMgmtIroadmGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIroadmEgressOAPpcOut"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtIroadmGroup.setStatus("current")

tnPowerMgmtCapabilitiesCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 18)
)
tnPowerMgmtCapabilitiesCardScalarsGroup.setObjects(
    ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesCardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesCardScalarsGroup.setStatus("current")

tnPowerMgmtCapabilitiesCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 19)
)
tnPowerMgmtCapabilitiesCardGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesCardEgressPower"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesCardIngressPower"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesCardEgressTilt"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesCardIngressTilt"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesCardGroup.setStatus("current")

tnPowerMgmtIngressPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 20)
)
tnPowerMgmtIngressPortGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortAdjustPowerGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortAdjustPowerGainLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortAdjustPowerGainStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortSRSTiltAdjStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortSRSTiltAdjResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortSRSTiltPostFraction"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortSRSTiltPostFractionL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortGainSetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortGainSetOffsetL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortAdjustPowerGainTargetGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortAdjustPowerGainTargetGainL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortCommissionedGain"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortCommissionedGainL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortSRSTiltCalcOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortSRSTiltCalcOffsetL"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortGroup.setStatus("current")

tnPowerMgmtEgressPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 21)
)
tnPowerMgmtEgressPortGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortAdjustPowerWithOptimization"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSTiltCalcOutputLoss"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSTiltAdjStatus"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSTIltAdjResult"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSTiltCalcACoeff"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSTiltCalcACoeffL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSTiltCalcMultiplier"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSTiltCalcMultiplierL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortFiberSpanTiltPreComp"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortFiberSpanTiltPreCompL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSCF"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSCFL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSTiltPreFraction"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSRSTiltPreFractionL"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortCommissioned"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortPassed"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortLHLaunchAtten"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortExternalOTAddLaunchAtten"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSmoothing"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortSmoothingMaxStepSize"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortGroup.setStatus("current")

tnPowerMgmtIngressPortPerChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 22)
)
tnPowerMgmtIngressPortPerChannelGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortPerChannelSystemTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortPerChannelUserTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortPerChannelInUseTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortPerChannelTargetAbsolute"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortPerChannelApplicability"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtIngressPortPerChannelGroup.setStatus("current")

tnPowerMgmtEgressPortPerChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 23)
)
tnPowerMgmtEgressPortPerChannelGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortPerChannelSystemTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortPerChannelUserTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortPerChannelInUseTargetOffset"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortPerChannelTargetAbsolute"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortPerChannelApplicability"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtEgressPortPerChannelGroup.setStatus("current")

tnPowerMgmtCapabilitiesPortScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 24)
)
tnPowerMgmtCapabilitiesPortScalarsGroup.setObjects(
    ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesPortAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesPortScalarsGroup.setStatus("current")

tnPowerMgmtCapabilitiesPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 1, 25)
)
tnPowerMgmtCapabilitiesPortGroup.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesPortEgressPower"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesPortIngressPower"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesPortEgressTilt"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesPortIngressTilt"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtCapabilitiesPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnPowerMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 6, 1, 2, 1)
)
tnPowerMgmtCompliance.setObjects(
      *(("TROPIC-POWERMGMT-MIB", "tnPowerMgmtGlobalGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtControlGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPortGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPowerOffsetInGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtPowerOffsetOutGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPerChannelGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPerChannelGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtTechnologyTypesGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyAddGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtAnyDropGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIroadmScalarsGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIroadmGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesCardScalarsGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesCardGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtIngressPortPerChannelGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtEgressPortPerChannelGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesPortScalarsGroup"),
        ("TROPIC-POWERMGMT-MIB", "tnPowerMgmtCapabilitiesPortGroup"))
)
if mibBuilder.loadTexts:
    tnPowerMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-POWERMGMT-MIB",
    **{"TropicPowerMgmtStatus": TropicPowerMgmtStatus,
       "TropicPowerMgmtResult": TropicPowerMgmtResult,
       "TropicPowerMgmtPercentCompleted": TropicPowerMgmtPercentCompleted,
       "TropicPowerMgmtType": TropicPowerMgmtType,
       "AluWdmWTDecoderUsageType": AluWdmWTDecoderUsageType,
       "AluWdmPowerMgmtSRSTiltAdjStatus": AluWdmPowerMgmtSRSTiltAdjStatus,
       "TropicPowerMgmtCapabilitiesCard": TropicPowerMgmtCapabilitiesCard,
       "tnPowerMgmtMibModule": tnPowerMgmtMibModule,
       "tnPowerMgmtConf": tnPowerMgmtConf,
       "tnPowerMgmtGroups": tnPowerMgmtGroups,
       "tnPowerMgmtGlobalGroup": tnPowerMgmtGlobalGroup,
       "tnPowerMgmtControlGroup": tnPowerMgmtControlGroup,
       "tnPowerMgmtIngressGroup": tnPowerMgmtIngressGroup,
       "tnPowerMgmtEgressGroup": tnPowerMgmtEgressGroup,
       "tnPowerMgmtPortGroup": tnPowerMgmtPortGroup,
       "tnPowerMgmtPowerOffsetInGroup": tnPowerMgmtPowerOffsetInGroup,
       "tnPowerMgmtPowerOffsetOutGroup": tnPowerMgmtPowerOffsetOutGroup,
       "tnPowerMgmtIngressPerChannelGroup": tnPowerMgmtIngressPerChannelGroup,
       "tnPowerMgmtEgressPerChannelGroup": tnPowerMgmtEgressPerChannelGroup,
       "tnPowerMgmtTechnologyTypesGroup": tnPowerMgmtTechnologyTypesGroup,
       "tnPowerMgmtAnyAddGroup": tnPowerMgmtAnyAddGroup,
       "tnPowerMgmtAnyDropGroup": tnPowerMgmtAnyDropGroup,
       "tnPowerMgmtIroadmScalarsGroup": tnPowerMgmtIroadmScalarsGroup,
       "tnPowerMgmtIroadmGroup": tnPowerMgmtIroadmGroup,
       "tnPowerMgmtCapabilitiesCardScalarsGroup": tnPowerMgmtCapabilitiesCardScalarsGroup,
       "tnPowerMgmtCapabilitiesCardGroup": tnPowerMgmtCapabilitiesCardGroup,
       "tnPowerMgmtIngressPortGroup": tnPowerMgmtIngressPortGroup,
       "tnPowerMgmtEgressPortGroup": tnPowerMgmtEgressPortGroup,
       "tnPowerMgmtIngressPortPerChannelGroup": tnPowerMgmtIngressPortPerChannelGroup,
       "tnPowerMgmtEgressPortPerChannelGroup": tnPowerMgmtEgressPortPerChannelGroup,
       "tnPowerMgmtCapabilitiesPortScalarsGroup": tnPowerMgmtCapabilitiesPortScalarsGroup,
       "tnPowerMgmtCapabilitiesPortGroup": tnPowerMgmtCapabilitiesPortGroup,
       "tnPowerMgmtCompliances": tnPowerMgmtCompliances,
       "tnPowerMgmtCompliance": tnPowerMgmtCompliance,
       "tnPowerMgmtObjs": tnPowerMgmtObjs,
       "tnPowerMgmtBasics": tnPowerMgmtBasics,
       "tnPowerMgmtGlobal": tnPowerMgmtGlobal,
       "tnPowerMgmtGlobalMinStepSize": tnPowerMgmtGlobalMinStepSize,
       "tnPowerMgmtGlobalMaxStepSize": tnPowerMgmtGlobalMaxStepSize,
       "tnPowerMgmtGlobalResetToDefaults": tnPowerMgmtGlobalResetToDefaults,
       "tnPowerMgmtGlobalAutoEnabled": tnPowerMgmtGlobalAutoEnabled,
       "tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints": tnPowerMgmtGlobalNumberOfAutoPowerAdjPoints,
       "tnPowerMgmtGlobalAlarmWhenDisabled": tnPowerMgmtGlobalAlarmWhenDisabled,
       "tnPowerMgmtControlTable": tnPowerMgmtControlTable,
       "tnPowerMgmtControlEntry": tnPowerMgmtControlEntry,
       "tnPowerMgmtDirection": tnPowerMgmtDirection,
       "tnPowerMgmtControlPercentCompleted": tnPowerMgmtControlPercentCompleted,
       "tnPowerMgmtControlRowStatus": tnPowerMgmtControlRowStatus,
       "tnPowerMgmtIngressTable": tnPowerMgmtIngressTable,
       "tnPowerMgmtIngressEntry": tnPowerMgmtIngressEntry,
       "tnPowerMgmtIngressAdjustPowerGain": tnPowerMgmtIngressAdjustPowerGain,
       "tnPowerMgmtIngressAdjustPowerGainLastResult": tnPowerMgmtIngressAdjustPowerGainLastResult,
       "tnPowerMgmtIngressAcceptPowers": tnPowerMgmtIngressAcceptPowers,
       "tnPowerMgmtIngressAcceptPowersLastResult": tnPowerMgmtIngressAcceptPowersLastResult,
       "tnPowerMgmtIngressRippleAllowance": tnPowerMgmtIngressRippleAllowance,
       "tnPowerMgmtIngressAdjustPowerGainTargetGain": tnPowerMgmtIngressAdjustPowerGainTargetGain,
       "tnPowerMgmtIngressAdjustPowerGainStatus": tnPowerMgmtIngressAdjustPowerGainStatus,
       "tnPowerMgmtIngressStartAseAdjust": tnPowerMgmtIngressStartAseAdjust,
       "tnPowerMgmtIngressAseAdjustLastResult": tnPowerMgmtIngressAseAdjustLastResult,
       "tnPowerMgmtIngressAseAdjustStatus": tnPowerMgmtIngressAseAdjustStatus,
       "tnPowerMgmtIngressCommissioned": tnPowerMgmtIngressCommissioned,
       "tnPowerMgmtIngressGainSetOffset": tnPowerMgmtIngressGainSetOffset,
       "tnPowerMgmtIngressCommissionedGain": tnPowerMgmtIngressCommissionedGain,
       "tnPowerMgmtIngressSRSTiltPostFraction": tnPowerMgmtIngressSRSTiltPostFraction,
       "tnPowerMgmtIngressSRSTiltAdjResult": tnPowerMgmtIngressSRSTiltAdjResult,
       "tnPowerMgmtIngressSRSTiltAdjStatus": tnPowerMgmtIngressSRSTiltAdjStatus,
       "tnPowerMgmtIngressPassed": tnPowerMgmtIngressPassed,
       "tnPowerMgmtIngressSRSTiltCalcOffset": tnPowerMgmtIngressSRSTiltCalcOffset,
       "tnPowerMgmtIngressInternodalOaPpcMaxInCurrent": tnPowerMgmtIngressInternodalOaPpcMaxInCurrent,
       "tnPowerMgmtIngressInternodalOaPpcMaxInReference": tnPowerMgmtIngressInternodalOaPpcMaxInReference,
       "tnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent": tnPowerMgmtIngressInternodalCalculatedSpanLossInCurrent,
       "tnPowerMgmtIngressInternodalCalculatedSpanLossInReference": tnPowerMgmtIngressInternodalCalculatedSpanLossInReference,
       "tnPowerMgmtIngressSRSTiltPostFractionL": tnPowerMgmtIngressSRSTiltPostFractionL,
       "tnPowerMgmtIngressGainSetOffsetL": tnPowerMgmtIngressGainSetOffsetL,
       "tnPowerMgmtIngressAdjustPowerGainTargetGainL": tnPowerMgmtIngressAdjustPowerGainTargetGainL,
       "tnPowerMgmtIngressCommissionedGainL": tnPowerMgmtIngressCommissionedGainL,
       "tnPowerMgmtIngressSRSTiltCalcOffsetL": tnPowerMgmtIngressSRSTiltCalcOffsetL,
       "tnPowerMgmtEgressTable": tnPowerMgmtEgressTable,
       "tnPowerMgmtEgressEntry": tnPowerMgmtEgressEntry,
       "tnPowerMgmtEgressAdjustPowerWithOptimization": tnPowerMgmtEgressAdjustPowerWithOptimization,
       "tnPowerMgmtEgressAdjustPowerWithOptimizationStatus": tnPowerMgmtEgressAdjustPowerWithOptimizationStatus,
       "tnPowerMgmtEgressAdjustPowerWithOptimizationAbort": tnPowerMgmtEgressAdjustPowerWithOptimizationAbort,
       "tnPowerMgmtEgressAcceptPowers": tnPowerMgmtEgressAcceptPowers,
       "tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult": tnPowerMgmtEgressAdjustPowerWithOptimizationLastResult,
       "tnPowerMgmtEgressAcceptPowersLastResult": tnPowerMgmtEgressAcceptPowersLastResult,
       "tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain": tnPowerMgmtEgressAdjustPowerWithOptimizationTargetGain,
       "tnPowerMgmtEgressStartAseAdjust": tnPowerMgmtEgressStartAseAdjust,
       "tnPowerMgmtEgressStopAseAdjust": tnPowerMgmtEgressStopAseAdjust,
       "tnPowerMgmtEgressAseAdjustLastResult": tnPowerMgmtEgressAseAdjustLastResult,
       "tnPowerMgmtEgressAseAdjustStatus": tnPowerMgmtEgressAseAdjustStatus,
       "tnPowerMgmtEgressCommissioned": tnPowerMgmtEgressCommissioned,
       "tnPowerMgmtEgressAmpIfIndex": tnPowerMgmtEgressAmpIfIndex,
       "tnPowerMgmtEgressWssIfIndex": tnPowerMgmtEgressWssIfIndex,
       "tnPowerMgmtEgressSRSTiltCalcMultiplier": tnPowerMgmtEgressSRSTiltCalcMultiplier,
       "tnPowerMgmtEgressSRSTiltPreFraction": tnPowerMgmtEgressSRSTiltPreFraction,
       "tnPowerMgmtEgressSRSTiltCalcACoeff": tnPowerMgmtEgressSRSTiltCalcACoeff,
       "tnPowerMgmtEgressSRSTiltCalcOutputLoss": tnPowerMgmtEgressSRSTiltCalcOutputLoss,
       "tnPowerMgmtEgressSRSTiltAdjResult": tnPowerMgmtEgressSRSTiltAdjResult,
       "tnPowerMgmtEgressSRSTiltAdjStatus": tnPowerMgmtEgressSRSTiltAdjStatus,
       "tnPowerMgmtEgressPassed": tnPowerMgmtEgressPassed,
       "tnPowerMgmtEgressLHLaunchAtten": tnPowerMgmtEgressLHLaunchAtten,
       "tnPowerMgmtFiberSpanTiltPreComp": tnPowerMgmtFiberSpanTiltPreComp,
       "tnPowerMgmtEgressInternodalPpcMaxInDownstream": tnPowerMgmtEgressInternodalPpcMaxInDownstream,
       "tnPowerMgmtEgressInternodalSpanLossInDownstream": tnPowerMgmtEgressInternodalSpanLossInDownstream,
       "tnPowerMgmtEgressInternodalPpcMaxInDownstreamReference": tnPowerMgmtEgressInternodalPpcMaxInDownstreamReference,
       "tnPowerMgmtEgressInternodalSpanLossInDownstreamReference": tnPowerMgmtEgressInternodalSpanLossInDownstreamReference,
       "tnPowerMgmtFiberSpanTiltPreCompL": tnPowerMgmtFiberSpanTiltPreCompL,
       "tnPowerMgmtEgressSRSTiltCalcMultiplierL": tnPowerMgmtEgressSRSTiltCalcMultiplierL,
       "tnPowerMgmtEgressSRSTiltPreFractionL": tnPowerMgmtEgressSRSTiltPreFractionL,
       "tnPowerMgmtEgressSRSTiltCalcACoeffL": tnPowerMgmtEgressSRSTiltCalcACoeffL,
       "tnPowerMgmtEgressSRSCF": tnPowerMgmtEgressSRSCF,
       "tnPowerMgmtEgressSRSCFL": tnPowerMgmtEgressSRSCFL,
       "tnPowerMgmtEgressExternalOTAddLaunchAtten": tnPowerMgmtEgressExternalOTAddLaunchAtten,
       "tnPowerMgmtEgressSmoothing": tnPowerMgmtEgressSmoothing,
       "tnPowerMgmtEgressSmoothingMaxStepSize": tnPowerMgmtEgressSmoothingMaxStepSize,
       "tnPowerMgmtPortTable": tnPowerMgmtPortTable,
       "tnPowerMgmtPortEntry": tnPowerMgmtPortEntry,
       "tnPowerMgmtPortIsCommissioned": tnPowerMgmtPortIsCommissioned,
       "tnPowerMgmtPortTypeIn": tnPowerMgmtPortTypeIn,
       "tnPowerMgmtPortTypeOut": tnPowerMgmtPortTypeOut,
       "tnPowerMgmtPortWTDecoderUsageTypeIn": tnPowerMgmtPortWTDecoderUsageTypeIn,
       "tnPowerMgmtPortWTDecoderUsageTypeOut": tnPowerMgmtPortWTDecoderUsageTypeOut,
       "tnPowerMgmtPortGainAdjSchedBase": tnPowerMgmtPortGainAdjSchedBase,
       "tnPowerMgmtPortGainAdjTimerPeriod": tnPowerMgmtPortGainAdjTimerPeriod,
       "tnPowerMgmtPortGainAdjTimerLength": tnPowerMgmtPortGainAdjTimerLength,
       "tnPowerMgmtPortInGainAdjAutoEnabled": tnPowerMgmtPortInGainAdjAutoEnabled,
       "tnPowerMgmtPortSRSTiltAdjAutoEnabled": tnPowerMgmtPortSRSTiltAdjAutoEnabled,
       "tnPowerMgmtPortFiberSpanTilt": tnPowerMgmtPortFiberSpanTilt,
       "tnPowerMgmtPortSRSTiltMaintenanceMode": tnPowerMgmtPortSRSTiltMaintenanceMode,
       "tnPowerMgmtPortDegreeFunction": tnPowerMgmtPortDegreeFunction,
       "tnPowerMgmtPortMaxChannels": tnPowerMgmtPortMaxChannels,
       "tnPowerMgmtPortEgressAdjustForDownstreamEnabled": tnPowerMgmtPortEgressAdjustForDownstreamEnabled,
       "tnPowerMgmtPortFiberSpanTiltL": tnPowerMgmtPortFiberSpanTiltL,
       "tnPowerMgmtPortWTDecoderUsageTypeInL": tnPowerMgmtPortWTDecoderUsageTypeInL,
       "tnPowerMgmtPortWTDecoderUsageTypeOutL": tnPowerMgmtPortWTDecoderUsageTypeOutL,
       "tnPowerMgmtPortIsCommissionedMethod": tnPowerMgmtPortIsCommissionedMethod,
       "tnPowerMgmtPowerOffsetInTable": tnPowerMgmtPowerOffsetInTable,
       "tnPowerMgmtPowerOffsetInEntry": tnPowerMgmtPowerOffsetInEntry,
       "tnPowerMgmtBitRate": tnPowerMgmtBitRate,
       "tnPowerMgmtEncoding": tnPowerMgmtEncoding,
       "tnPowerMgmtOffsetInPowerOffset": tnPowerMgmtOffsetInPowerOffset,
       "tnPowerMgmtPowerOffsetOutTable": tnPowerMgmtPowerOffsetOutTable,
       "tnPowerMgmtPowerOffsetOutEntry": tnPowerMgmtPowerOffsetOutEntry,
       "tnPowerMgmtOffsetOutPowerOffset": tnPowerMgmtOffsetOutPowerOffset,
       "tnPowerMgmtIngressPerChannelTable": tnPowerMgmtIngressPerChannelTable,
       "tnPowerMgmtIngressPerChannelEntry": tnPowerMgmtIngressPerChannelEntry,
       "tnPowerMgmtIngressPerChannelSystemTargetOffset": tnPowerMgmtIngressPerChannelSystemTargetOffset,
       "tnPowerMgmtIngressPerChannelUserTargetOffset": tnPowerMgmtIngressPerChannelUserTargetOffset,
       "tnPowerMgmtIngressPerChannelInUseTargetOffset": tnPowerMgmtIngressPerChannelInUseTargetOffset,
       "tnPowerMgmtIngressPerChannelTargetAbsolute": tnPowerMgmtIngressPerChannelTargetAbsolute,
       "tnPowerMgmtIngressPerChannelApplicability": tnPowerMgmtIngressPerChannelApplicability,
       "tnPowerMgmtEgressPerChannelTable": tnPowerMgmtEgressPerChannelTable,
       "tnPowerMgmtEgressPerChannelEntry": tnPowerMgmtEgressPerChannelEntry,
       "tnPowerMgmtEgressPerChannelSystemTargetOffset": tnPowerMgmtEgressPerChannelSystemTargetOffset,
       "tnPowerMgmtEgressPerChannelUserTargetOffset": tnPowerMgmtEgressPerChannelUserTargetOffset,
       "tnPowerMgmtEgressPerChannelInUseTargetOffset": tnPowerMgmtEgressPerChannelInUseTargetOffset,
       "tnPowerMgmtEgressPerChannelTargetAbsolute": tnPowerMgmtEgressPerChannelTargetAbsolute,
       "tnPowerMgmtEgressPerChannelApplicability": tnPowerMgmtEgressPerChannelApplicability,
       "tnPowerMgmtTechnologyTypesTable": tnPowerMgmtTechnologyTypesTable,
       "tnPowerMgmtTechnologyTypesEntry": tnPowerMgmtTechnologyTypesEntry,
       "tnPowerMgmtTechnologyTypesBitRateText": tnPowerMgmtTechnologyTypesBitRateText,
       "tnPowerMgmtTechnologyTypesEncodingText": tnPowerMgmtTechnologyTypesEncodingText,
       "tnPowerMgmtTechnologyTypesWtocmCalib": tnPowerMgmtTechnologyTypesWtocmCalib,
       "tnPowerMgmtTechnologyTypesRowStatus": tnPowerMgmtTechnologyTypesRowStatus,
       "tnPowerMgmtTechnologyTypesOsnrCalib": tnPowerMgmtTechnologyTypesOsnrCalib,
       "tnPowerMgmtTechnologyTypesWtocmaCalib": tnPowerMgmtTechnologyTypesWtocmaCalib,
       "tnPowerMgmtTechnologyTypesWtocmfCalib": tnPowerMgmtTechnologyTypesWtocmfCalib,
       "tnPowerMgmtTechnologyTypesWtocmfLCalib": tnPowerMgmtTechnologyTypesWtocmfLCalib,
       "tnPowerMgmtTechnologyTypesWtocmfCalib375": tnPowerMgmtTechnologyTypesWtocmfCalib375,
       "tnPowerMgmtTechnologyTypesWtocmfLCalib375": tnPowerMgmtTechnologyTypesWtocmfLCalib375,
       "tnPowerMgmtTechnologyTypesMinXCWidthValue": tnPowerMgmtTechnologyTypesMinXCWidthValue,
       "tnPowerMgmtAnyAddTable": tnPowerMgmtAnyAddTable,
       "tnPowerMgmtAnyAddEntry": tnPowerMgmtAnyAddEntry,
       "tnPowerMgmtAnyAddAdjustPowerGain": tnPowerMgmtAnyAddAdjustPowerGain,
       "tnPowerMgmtAnyAddAdjustPowerGainLastResult": tnPowerMgmtAnyAddAdjustPowerGainLastResult,
       "tnPowerMgmtAnyAddAdjustPowerGainStatus": tnPowerMgmtAnyAddAdjustPowerGainStatus,
       "tnPowerMgmtAnyAddCommissioned": tnPowerMgmtAnyAddCommissioned,
       "tnPowerMgmtAnyAddPassed": tnPowerMgmtAnyAddPassed,
       "tnPowerMgmtAnyAddAmpIfIndex": tnPowerMgmtAnyAddAmpIfIndex,
       "tnPowerMgmtAnyAddAdjustPowerGainAbort": tnPowerMgmtAnyAddAdjustPowerGainAbort,
       "tnPowerMgmtAnyDropTable": tnPowerMgmtAnyDropTable,
       "tnPowerMgmtAnyDropEntry": tnPowerMgmtAnyDropEntry,
       "tnPowerMgmtAnyDropAdjustPowerGain": tnPowerMgmtAnyDropAdjustPowerGain,
       "tnPowerMgmtAnyDropAdjustPowerGainLastResult": tnPowerMgmtAnyDropAdjustPowerGainLastResult,
       "tnPowerMgmtAnyDropAdjustPowerGainStatus": tnPowerMgmtAnyDropAdjustPowerGainStatus,
       "tnPowerMgmtAnyDropCommissioned": tnPowerMgmtAnyDropCommissioned,
       "tnPowerMgmtAnyDropPassed": tnPowerMgmtAnyDropPassed,
       "tnPowerMgmtAnyDropAmpIfIndex": tnPowerMgmtAnyDropAmpIfIndex,
       "tnPowerMgmtIroadmAttributeTotal": tnPowerMgmtIroadmAttributeTotal,
       "tnPowerMgmtIroadmTable": tnPowerMgmtIroadmTable,
       "tnPowerMgmtIroadmEntry": tnPowerMgmtIroadmEntry,
       "tnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs": tnPowerMgmtIroadmEgressOAMaxPpcOutFromInputs,
       "tnPowerMgmtIroadmEgressOAPpcOut": tnPowerMgmtIroadmEgressOAPpcOut,
       "tnPowerMgmtCapabilitiesCardAttributeTotal": tnPowerMgmtCapabilitiesCardAttributeTotal,
       "tnPowerMgmtCapabilitiesCardTable": tnPowerMgmtCapabilitiesCardTable,
       "tnPowerMgmtCapabilitiesCardEntry": tnPowerMgmtCapabilitiesCardEntry,
       "tnPowerMgmtCapabilitiesCardEgressPower": tnPowerMgmtCapabilitiesCardEgressPower,
       "tnPowerMgmtCapabilitiesCardIngressPower": tnPowerMgmtCapabilitiesCardIngressPower,
       "tnPowerMgmtCapabilitiesCardEgressTilt": tnPowerMgmtCapabilitiesCardEgressTilt,
       "tnPowerMgmtCapabilitiesCardIngressTilt": tnPowerMgmtCapabilitiesCardIngressTilt,
       "tnPowerMgmtIngressPortTable": tnPowerMgmtIngressPortTable,
       "tnPowerMgmtIngressPortEntry": tnPowerMgmtIngressPortEntry,
       "tnPowerMgmtIngressPortAdjustPowerGain": tnPowerMgmtIngressPortAdjustPowerGain,
       "tnPowerMgmtIngressPortAdjustPowerGainLastResult": tnPowerMgmtIngressPortAdjustPowerGainLastResult,
       "tnPowerMgmtIngressPortAdjustPowerGainStatus": tnPowerMgmtIngressPortAdjustPowerGainStatus,
       "tnPowerMgmtIngressPortSRSTiltAdjStatus": tnPowerMgmtIngressPortSRSTiltAdjStatus,
       "tnPowerMgmtIngressPortSRSTiltAdjResult": tnPowerMgmtIngressPortSRSTiltAdjResult,
       "tnPowerMgmtIngressPortSRSTiltPostFraction": tnPowerMgmtIngressPortSRSTiltPostFraction,
       "tnPowerMgmtIngressPortSRSTiltPostFractionL": tnPowerMgmtIngressPortSRSTiltPostFractionL,
       "tnPowerMgmtIngressPortCommissioned": tnPowerMgmtIngressPortCommissioned,
       "tnPowerMgmtIngressPortPassed": tnPowerMgmtIngressPortPassed,
       "tnPowerMgmtIngressPortGainSetOffset": tnPowerMgmtIngressPortGainSetOffset,
       "tnPowerMgmtIngressPortGainSetOffsetL": tnPowerMgmtIngressPortGainSetOffsetL,
       "tnPowerMgmtIngressPortAdjustPowerGainTargetGain": tnPowerMgmtIngressPortAdjustPowerGainTargetGain,
       "tnPowerMgmtIngressPortAdjustPowerGainTargetGainL": tnPowerMgmtIngressPortAdjustPowerGainTargetGainL,
       "tnPowerMgmtIngressPortCommissionedGain": tnPowerMgmtIngressPortCommissionedGain,
       "tnPowerMgmtIngressPortCommissionedGainL": tnPowerMgmtIngressPortCommissionedGainL,
       "tnPowerMgmtIngressPortSRSTiltCalcOffset": tnPowerMgmtIngressPortSRSTiltCalcOffset,
       "tnPowerMgmtIngressPortSRSTiltCalcOffsetL": tnPowerMgmtIngressPortSRSTiltCalcOffsetL,
       "tnPowerMgmtEgressPortTable": tnPowerMgmtEgressPortTable,
       "tnPowerMgmtEgressPortEntry": tnPowerMgmtEgressPortEntry,
       "tnPowerMgmtEgressPortAdjustPowerWithOptimization": tnPowerMgmtEgressPortAdjustPowerWithOptimization,
       "tnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort": tnPowerMgmtEgressPortAdjustPowerWithOptimizationAbort,
       "tnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult": tnPowerMgmtEgressPortAdjustPowerWithOptimizationLastResult,
       "tnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus": tnPowerMgmtEgressPortAdjustPowerWithOptimizationStatus,
       "tnPowerMgmtEgressPortSRSTiltCalcOutputLoss": tnPowerMgmtEgressPortSRSTiltCalcOutputLoss,
       "tnPowerMgmtEgressPortSRSTiltAdjStatus": tnPowerMgmtEgressPortSRSTiltAdjStatus,
       "tnPowerMgmtEgressPortSRSTIltAdjResult": tnPowerMgmtEgressPortSRSTIltAdjResult,
       "tnPowerMgmtEgressPortSRSTiltCalcACoeff": tnPowerMgmtEgressPortSRSTiltCalcACoeff,
       "tnPowerMgmtEgressPortSRSTiltCalcACoeffL": tnPowerMgmtEgressPortSRSTiltCalcACoeffL,
       "tnPowerMgmtEgressPortSRSTiltCalcMultiplier": tnPowerMgmtEgressPortSRSTiltCalcMultiplier,
       "tnPowerMgmtEgressPortSRSTiltCalcMultiplierL": tnPowerMgmtEgressPortSRSTiltCalcMultiplierL,
       "tnPowerMgmtEgressPortFiberSpanTiltPreComp": tnPowerMgmtEgressPortFiberSpanTiltPreComp,
       "tnPowerMgmtEgressPortFiberSpanTiltPreCompL": tnPowerMgmtEgressPortFiberSpanTiltPreCompL,
       "tnPowerMgmtEgressPortSRSCF": tnPowerMgmtEgressPortSRSCF,
       "tnPowerMgmtEgressPortSRSCFL": tnPowerMgmtEgressPortSRSCFL,
       "tnPowerMgmtEgressPortSRSTiltPreFraction": tnPowerMgmtEgressPortSRSTiltPreFraction,
       "tnPowerMgmtEgressPortSRSTiltPreFractionL": tnPowerMgmtEgressPortSRSTiltPreFractionL,
       "tnPowerMgmtEgressPortCommissioned": tnPowerMgmtEgressPortCommissioned,
       "tnPowerMgmtEgressPortPassed": tnPowerMgmtEgressPortPassed,
       "tnPowerMgmtEgressPortLHLaunchAtten": tnPowerMgmtEgressPortLHLaunchAtten,
       "tnPowerMgmtEgressPortExternalOTAddLaunchAtten": tnPowerMgmtEgressPortExternalOTAddLaunchAtten,
       "tnPowerMgmtEgressPortSmoothing": tnPowerMgmtEgressPortSmoothing,
       "tnPowerMgmtEgressPortSmoothingMaxStepSize": tnPowerMgmtEgressPortSmoothingMaxStepSize,
       "tnPowerMgmtIngressPortPerChannelTable": tnPowerMgmtIngressPortPerChannelTable,
       "tnPowerMgmtIngressPortPerChannelEntry": tnPowerMgmtIngressPortPerChannelEntry,
       "tnPowerMgmtIngressPortPerChannelSystemTargetOffset": tnPowerMgmtIngressPortPerChannelSystemTargetOffset,
       "tnPowerMgmtIngressPortPerChannelUserTargetOffset": tnPowerMgmtIngressPortPerChannelUserTargetOffset,
       "tnPowerMgmtIngressPortPerChannelInUseTargetOffset": tnPowerMgmtIngressPortPerChannelInUseTargetOffset,
       "tnPowerMgmtIngressPortPerChannelTargetAbsolute": tnPowerMgmtIngressPortPerChannelTargetAbsolute,
       "tnPowerMgmtIngressPortPerChannelApplicability": tnPowerMgmtIngressPortPerChannelApplicability,
       "tnPowerMgmtEgressPortPerChannelTable": tnPowerMgmtEgressPortPerChannelTable,
       "tnPowerMgmtEgressPortPerChannelEntry": tnPowerMgmtEgressPortPerChannelEntry,
       "tnPowerMgmtEgressPortPerChannelSystemTargetOffset": tnPowerMgmtEgressPortPerChannelSystemTargetOffset,
       "tnPowerMgmtEgressPortPerChannelUserTargetOffset": tnPowerMgmtEgressPortPerChannelUserTargetOffset,
       "tnPowerMgmtEgressPortPerChannelInUseTargetOffset": tnPowerMgmtEgressPortPerChannelInUseTargetOffset,
       "tnPowerMgmtEgressPortPerChannelTargetAbsolute": tnPowerMgmtEgressPortPerChannelTargetAbsolute,
       "tnPowerMgmtEgressPortPerChannelApplicability": tnPowerMgmtEgressPortPerChannelApplicability,
       "tnPowerMgmtCapabilitiesPortAttributeTotal": tnPowerMgmtCapabilitiesPortAttributeTotal,
       "tnPowerMgmtCapabilitiesPortTable": tnPowerMgmtCapabilitiesPortTable,
       "tnPowerMgmtCapabilitiesPortEntry": tnPowerMgmtCapabilitiesPortEntry,
       "tnPowerMgmtCapabilitiesPortEgressPower": tnPowerMgmtCapabilitiesPortEgressPower,
       "tnPowerMgmtCapabilitiesPortIngressPower": tnPowerMgmtCapabilitiesPortIngressPower,
       "tnPowerMgmtCapabilitiesPortEgressTilt": tnPowerMgmtCapabilitiesPortEgressTilt,
       "tnPowerMgmtCapabilitiesPortIngressTilt": tnPowerMgmtCapabilitiesPortIngressTilt}
)
