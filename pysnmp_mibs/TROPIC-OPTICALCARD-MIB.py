# SNMP MIB module (TROPIC-OPTICALCARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-OPTICALCARD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:49:37 2025
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

(tnCardModules,
 tnOpticalCardMIB) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnCardModules",
    "tnOpticalCardMIB")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(AluWdmFcruProtectionRoleType,
 TnCommand,
 TropicLEDColorType,
 TropicLEDStateType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmFcruProtectionRoleType",
    "TnCommand",
    "TropicLEDColorType",
    "TropicLEDStateType")


# MODULE-IDENTITY

tnOpticalCardMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    tnOpticalCardMibModule.setRevisions(
        ("2021-04-02 12:00",
         "2020-10-23 12:00",
         "2020-09-04 12:00",
         "2020-06-26 12:00",
         "2020-06-05 12:00",
         "2020-03-13 12:00",
         "2019-05-24 12:00",
         "2019-03-15 12:00",
         "2019-02-01 12:00",
         "2018-11-09 12:00",
         "2018-10-10 12:00",
         "2018-08-17 12:00",
         "2018-06-22 12:00",
         "2018-02-23 12:00",
         "2017-11-03 12:00",
         "2017-07-28 12:00",
         "2017-07-07 12:00",
         "2017-05-31 12:00",
         "2017-01-20 12:00",
         "2016-11-18 12:00",
         "2016-11-16 12:00",
         "2016-10-26 12:00",
         "2016-10-21 12:00",
         "2016-09-21 12:00",
         "2016-05-31 12:00",
         "2016-05-09 12:00",
         "2016-04-08 12:00",
         "2015-01-08 12:00",
         "2014-11-19 12:00",
         "2014-08-13 12:00",
         "2014-02-26 12:00",
         "2013-10-21 12:00",
         "2013-05-21 12:00",
         "2013-04-26 12:00",
         "2013-04-09 12:00",
         "2013-03-14 12:00",
         "2013-01-07 12:00",
         "2012-10-24 12:00",
         "2012-10-22 12:00",
         "2012-09-06 12:00",
         "2012-09-01 12:00",
         "2012-06-13 12:00",
         "2012-04-27 12:00",
         "2012-03-29 12:00",
         "2012-03-18 12:00",
         "2011-09-30 12:00",
         "2011-08-12 12:00",
         "2011-07-22 12:00",
         "2011-07-19 12:00",
         "2011-05-23 12:00",
         "2011-03-25 12:00",
         "2010-11-08 12:00",
         "2010-11-01 12:00",
         "2010-10-24 12:00",
         "2010-09-28 12:00",
         "2010-07-29 12:00",
         "2010-05-10 12:00",
         "2010-01-27 12:00",
         "2010-01-25 12:00",
         "2010-01-08 12:00",
         "2009-09-26 12:00",
         "2009-08-05 12:00",
         "2009-06-22 12:00",
         "2009-05-31 12:00",
         "2009-05-19 12:00",
         "2009-04-30 12:00",
         "2009-04-23 12:00",
         "2009-04-07 12:00",
         "2009-03-25 12:00",
         "2008-07-25 12:00",
         "2008-06-09 12:00",
         "2008-05-29 12:00",
         "2008-04-11 12:00",
         "2008-02-16 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmSonetSdhPpSectionIfType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("oc3", 2),
          ("oc12", 3),
          ("oc48", 4),
          ("stm1", 5),
          ("stm4", 6),
          ("stm16", 7))
    )



class AluWdmPcsSectionIfType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("gige", 2),
          ("fc100", 3),
          ("fc200", 4),
          ("fc400", 5))
    )



class TropicSfdInvPortLoss(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicSfdInvFiberLength(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )



class TropicDcmInvFiberType(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicDcmInvDcmSize(TextualConvention, OctetString):
    status = "current"
    displayHint = "3a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicDcmInvInsertionLoss(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicDcmInvInsertionLossSlope(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicDcmInvDispersionFit(TextualConvention, OctetString):
    status = "current"
    displayHint = "40a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )



class TropicDcmInvFiberLength(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicDcmInvPmd(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicDcmInvLatencyMismatch(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicDcmInvLatency(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a.1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



# MIB Managed Objects in the order of their OIDs

_TnOpticalCardConf_ObjectIdentity = ObjectIdentity
tnOpticalCardConf = _TnOpticalCardConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1)
)
_TnOpticalCardGroups_ObjectIdentity = ObjectIdentity
tnOpticalCardGroups = _TnOpticalCardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1)
)
_TnOpticalCardCompliances_ObjectIdentity = ObjectIdentity
tnOpticalCardCompliances = _TnOpticalCardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 2)
)
_TnOpticalCardObjs_ObjectIdentity = ObjectIdentity
tnOpticalCardObjs = _TnOpticalCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2)
)
_TnOpticalCardTotal_Type = Integer32
_TnOpticalCardTotal_Object = MibScalar
tnOpticalCardTotal = _TnOpticalCardTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 1),
    _TnOpticalCardTotal_Type()
)
tnOpticalCardTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOpticalCardTotal.setStatus("current")
_TnDcmCardTable_Object = MibTable
tnDcmCardTable = _TnDcmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4)
)
if mibBuilder.loadTexts:
    tnDcmCardTable.setStatus("current")
_TnDcmCardEntry_Object = MibTableRow
tnDcmCardEntry = _TnDcmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1)
)
tnDcmCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnDcmCardEntry.setStatus("current")


class _TnDcmCardProgrammedCompensationDistance_Type(Unsigned32):
    """Custom type tnDcmCardProgrammedCompensationDistance based on Unsigned32"""
    defaultValue = 0


_TnDcmCardProgrammedCompensationDistance_Type.__name__ = "Unsigned32"
_TnDcmCardProgrammedCompensationDistance_Object = MibTableColumn
tnDcmCardProgrammedCompensationDistance = _TnDcmCardProgrammedCompensationDistance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 1),
    _TnDcmCardProgrammedCompensationDistance_Type()
)
tnDcmCardProgrammedCompensationDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDcmCardProgrammedCompensationDistance.setStatus("current")
if mibBuilder.loadTexts:
    tnDcmCardProgrammedCompensationDistance.setUnits("km")
_TnDcmCardPresentCompensationDistance_Type = Unsigned32
_TnDcmCardPresentCompensationDistance_Object = MibTableColumn
tnDcmCardPresentCompensationDistance = _TnDcmCardPresentCompensationDistance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 2),
    _TnDcmCardPresentCompensationDistance_Type()
)
tnDcmCardPresentCompensationDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardPresentCompensationDistance.setStatus("current")
if mibBuilder.loadTexts:
    tnDcmCardPresentCompensationDistance.setUnits("km")


class _TnDcmCardSize_Type(SnmpAdminString):
    """Custom type tnDcmCardSize based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardSize_Type.__name__ = "SnmpAdminString"
_TnDcmCardSize_Object = MibTableColumn
tnDcmCardSize = _TnDcmCardSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 3),
    _TnDcmCardSize_Type()
)
tnDcmCardSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardSize.setStatus("current")


class _TnDcmCardFiberType_Type(SnmpAdminString):
    """Custom type tnDcmCardFiberType based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardFiberType_Type.__name__ = "SnmpAdminString"
_TnDcmCardFiberType_Object = MibTableColumn
tnDcmCardFiberType = _TnDcmCardFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 4),
    _TnDcmCardFiberType_Type()
)
tnDcmCardFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardFiberType.setStatus("current")


class _TnDcmCardAverageInsertionLoss_Type(SnmpAdminString):
    """Custom type tnDcmCardAverageInsertionLoss based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardAverageInsertionLoss_Type.__name__ = "SnmpAdminString"
_TnDcmCardAverageInsertionLoss_Object = MibTableColumn
tnDcmCardAverageInsertionLoss = _TnDcmCardAverageInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 5),
    _TnDcmCardAverageInsertionLoss_Type()
)
tnDcmCardAverageInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardAverageInsertionLoss.setStatus("current")


class _TnDcmCardInsertionLossSlope_Type(SnmpAdminString):
    """Custom type tnDcmCardInsertionLossSlope based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardInsertionLossSlope_Type.__name__ = "SnmpAdminString"
_TnDcmCardInsertionLossSlope_Object = MibTableColumn
tnDcmCardInsertionLossSlope = _TnDcmCardInsertionLossSlope_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 6),
    _TnDcmCardInsertionLossSlope_Type()
)
tnDcmCardInsertionLossSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardInsertionLossSlope.setStatus("current")


class _TnDcmCardAverageInsertionLossPad_Type(SnmpAdminString):
    """Custom type tnDcmCardAverageInsertionLossPad based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardAverageInsertionLossPad_Type.__name__ = "SnmpAdminString"
_TnDcmCardAverageInsertionLossPad_Object = MibTableColumn
tnDcmCardAverageInsertionLossPad = _TnDcmCardAverageInsertionLossPad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 7),
    _TnDcmCardAverageInsertionLossPad_Type()
)
tnDcmCardAverageInsertionLossPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardAverageInsertionLossPad.setStatus("current")


class _TnDcmCardInsertionLossSlopePad_Type(SnmpAdminString):
    """Custom type tnDcmCardInsertionLossSlopePad based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardInsertionLossSlopePad_Type.__name__ = "SnmpAdminString"
_TnDcmCardInsertionLossSlopePad_Object = MibTableColumn
tnDcmCardInsertionLossSlopePad = _TnDcmCardInsertionLossSlopePad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 8),
    _TnDcmCardInsertionLossSlopePad_Type()
)
tnDcmCardInsertionLossSlopePad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardInsertionLossSlopePad.setStatus("current")


class _TnDcmCardTotalDispTilt_Type(SnmpAdminString):
    """Custom type tnDcmCardTotalDispTilt based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardTotalDispTilt_Type.__name__ = "SnmpAdminString"
_TnDcmCardTotalDispTilt_Object = MibTableColumn
tnDcmCardTotalDispTilt = _TnDcmCardTotalDispTilt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 9),
    _TnDcmCardTotalDispTilt_Type()
)
tnDcmCardTotalDispTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardTotalDispTilt.setStatus("current")


class _TnDcmCardDispFiberLength_Type(SnmpAdminString):
    """Custom type tnDcmCardDispFiberLength based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardDispFiberLength_Type.__name__ = "SnmpAdminString"
_TnDcmCardDispFiberLength_Object = MibTableColumn
tnDcmCardDispFiberLength = _TnDcmCardDispFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 10),
    _TnDcmCardDispFiberLength_Type()
)
tnDcmCardDispFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardDispFiberLength.setStatus("current")


class _TnDcmCardPMD_Type(SnmpAdminString):
    """Custom type tnDcmCardPMD based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnDcmCardPMD_Type.__name__ = "SnmpAdminString"
_TnDcmCardPMD_Object = MibTableColumn
tnDcmCardPMD = _TnDcmCardPMD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 11),
    _TnDcmCardPMD_Type()
)
tnDcmCardPMD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmCardPMD.setStatus("current")


class _TnDcmCardProvisionedFiberType_Type(Integer32):
    """Custom type tnDcmCardProvisionedFiberType based on Integer32"""
    defaultValue = 1

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
        *(("ssmf", 1),
          ("eleaf", 2),
          ("twrs", 3),
          ("ssmfb", 4),
          ("eleafb", 5),
          ("smfp", 6))
    )


_TnDcmCardProvisionedFiberType_Type.__name__ = "Integer32"
_TnDcmCardProvisionedFiberType_Object = MibTableColumn
tnDcmCardProvisionedFiberType = _TnDcmCardProvisionedFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 4, 1, 12),
    _TnDcmCardProvisionedFiberType_Type()
)
tnDcmCardProvisionedFiberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnDcmCardProvisionedFiberType.setStatus("current")
_TnPowerControlCardTable_Object = MibTable
tnPowerControlCardTable = _TnPowerControlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8)
)
if mibBuilder.loadTexts:
    tnPowerControlCardTable.setStatus("current")
_TnPowerControlCardEntry_Object = MibTableRow
tnPowerControlCardEntry = _TnPowerControlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8, 1)
)
tnPowerControlCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerControlCardEntry.setStatus("current")


class _TnPowerControlCardCapabilityProgrammed_Type(TruthValue):
    """Custom type tnPowerControlCardCapabilityProgrammed based on TruthValue"""
    defaultValue = 1


_TnPowerControlCardCapabilityProgrammed_Type.__name__ = "TruthValue"
_TnPowerControlCardCapabilityProgrammed_Object = MibTableColumn
tnPowerControlCardCapabilityProgrammed = _TnPowerControlCardCapabilityProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8, 1, 1),
    _TnPowerControlCardCapabilityProgrammed_Type()
)
tnPowerControlCardCapabilityProgrammed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPowerControlCardCapabilityProgrammed.setStatus("current")


class _TnPowerControlCardCapabilityPresent_Type(TruthValue):
    """Custom type tnPowerControlCardCapabilityPresent based on TruthValue"""
    defaultValue = 1


_TnPowerControlCardCapabilityPresent_Type.__name__ = "TruthValue"
_TnPowerControlCardCapabilityPresent_Object = MibTableColumn
tnPowerControlCardCapabilityPresent = _TnPowerControlCardCapabilityPresent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8, 1, 2),
    _TnPowerControlCardCapabilityPresent_Type()
)
tnPowerControlCardCapabilityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerControlCardCapabilityPresent.setStatus("current")
_TnPowerControlCardCapabilityInUse_Type = TruthValue
_TnPowerControlCardCapabilityInUse_Object = MibTableColumn
tnPowerControlCardCapabilityInUse = _TnPowerControlCardCapabilityInUse_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 8, 1, 3),
    _TnPowerControlCardCapabilityInUse_Type()
)
tnPowerControlCardCapabilityInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerControlCardCapabilityInUse.setStatus("current")
_TnWssCardTable_Object = MibTable
tnWssCardTable = _TnWssCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9)
)
if mibBuilder.loadTexts:
    tnWssCardTable.setStatus("current")
_TnWssCardEntry_Object = MibTableRow
tnWssCardEntry = _TnWssCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1)
)
tnWssCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnWssCardEntry.setStatus("current")


class _TnWssCardAddPathTargetPower_Type(Integer32):
    """Custom type tnWssCardAddPathTargetPower based on Integer32"""
    defaultValue = 130


_TnWssCardAddPathTargetPower_Type.__name__ = "Integer32"
_TnWssCardAddPathTargetPower_Object = MibTableColumn
tnWssCardAddPathTargetPower = _TnWssCardAddPathTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 1),
    _TnWssCardAddPathTargetPower_Type()
)
tnWssCardAddPathTargetPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAddPathTargetPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWssCardAddPathTargetPower.setUnits("mBm")


class _TnWssCardAddPathEgressPower_Type(Integer32):
    """Custom type tnWssCardAddPathEgressPower based on Integer32"""
    defaultValue = -900


_TnWssCardAddPathEgressPower_Type.__name__ = "Integer32"
_TnWssCardAddPathEgressPower_Object = MibTableColumn
tnWssCardAddPathEgressPower = _TnWssCardAddPathEgressPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 2),
    _TnWssCardAddPathEgressPower_Type()
)
tnWssCardAddPathEgressPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAddPathEgressPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWssCardAddPathEgressPower.setUnits("mBm")


class _TnWssCardAddPathTotalChannel_Type(Unsigned32):
    """Custom type tnWssCardAddPathTotalChannel based on Unsigned32"""
    defaultValue = 12


_TnWssCardAddPathTotalChannel_Type.__name__ = "Unsigned32"
_TnWssCardAddPathTotalChannel_Object = MibTableColumn
tnWssCardAddPathTotalChannel = _TnWssCardAddPathTotalChannel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 3),
    _TnWssCardAddPathTotalChannel_Type()
)
tnWssCardAddPathTotalChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAddPathTotalChannel.setStatus("current")


class _TnWssCardReservedDegree_Type(Unsigned32):
    """Custom type tnWssCardReservedDegree based on Unsigned32"""
    defaultValue = 2


_TnWssCardReservedDegree_Type.__name__ = "Unsigned32"
_TnWssCardReservedDegree_Object = MibTableColumn
tnWssCardReservedDegree = _TnWssCardReservedDegree_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 4),
    _TnWssCardReservedDegree_Type()
)
tnWssCardReservedDegree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardReservedDegree.setStatus("current")


class _TnWssCardLnsEnable_Type(Integer32):
    """Custom type tnWssCardLnsEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_TnWssCardLnsEnable_Type.__name__ = "Integer32"
_TnWssCardLnsEnable_Object = MibTableColumn
tnWssCardLnsEnable = _TnWssCardLnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 5),
    _TnWssCardLnsEnable_Type()
)
tnWssCardLnsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardLnsEnable.setStatus("current")
_TnWssCardLnsPower_Type = Integer32
_TnWssCardLnsPower_Object = MibTableColumn
tnWssCardLnsPower = _TnWssCardLnsPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 6),
    _TnWssCardLnsPower_Type()
)
tnWssCardLnsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWssCardLnsPower.setStatus("current")
if mibBuilder.loadTexts:
    tnWssCardLnsPower.setUnits("mBm")


class _TnWssCardAdBlockLevelAdd_Type(Unsigned32):
    """Custom type tnWssCardAdBlockLevelAdd based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnWssCardAdBlockLevelAdd_Type.__name__ = "Unsigned32"
_TnWssCardAdBlockLevelAdd_Object = MibTableColumn
tnWssCardAdBlockLevelAdd = _TnWssCardAdBlockLevelAdd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 9),
    _TnWssCardAdBlockLevelAdd_Type()
)
tnWssCardAdBlockLevelAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAdBlockLevelAdd.setStatus("current")


class _TnWssCardAdBlockLevelDrop_Type(Unsigned32):
    """Custom type tnWssCardAdBlockLevelDrop based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TnWssCardAdBlockLevelDrop_Type.__name__ = "Unsigned32"
_TnWssCardAdBlockLevelDrop_Object = MibTableColumn
tnWssCardAdBlockLevelDrop = _TnWssCardAdBlockLevelDrop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 10),
    _TnWssCardAdBlockLevelDrop_Type()
)
tnWssCardAdBlockLevelDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardAdBlockLevelDrop.setStatus("current")


class _TnWssCardIsFlexgrid_Type(Unsigned32):
    """Custom type tnWssCardIsFlexgrid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnWssCardIsFlexgrid_Type.__name__ = "Unsigned32"
_TnWssCardIsFlexgrid_Object = MibTableColumn
tnWssCardIsFlexgrid = _TnWssCardIsFlexgrid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 11),
    _TnWssCardIsFlexgrid_Type()
)
tnWssCardIsFlexgrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWssCardIsFlexgrid.setStatus("current")
if mibBuilder.loadTexts:
    tnWssCardIsFlexgrid.setUnits("MHz")
_TnWssCardGranularityMHz_Type = Integer32
_TnWssCardGranularityMHz_Object = MibTableColumn
tnWssCardGranularityMHz = _TnWssCardGranularityMHz_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 12),
    _TnWssCardGranularityMHz_Type()
)
tnWssCardGranularityMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWssCardGranularityMHz.setStatus("current")
if mibBuilder.loadTexts:
    tnWssCardGranularityMHz.setUnits("MHz")


class _TnWssCardEnableFilterlessDge_Type(TruthValue):
    """Custom type tnWssCardEnableFilterlessDge based on TruthValue"""
    defaultValue = 2


_TnWssCardEnableFilterlessDge_Type.__name__ = "TruthValue"
_TnWssCardEnableFilterlessDge_Object = MibTableColumn
tnWssCardEnableFilterlessDge = _TnWssCardEnableFilterlessDge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 9, 1, 13),
    _TnWssCardEnableFilterlessDge_Type()
)
tnWssCardEnableFilterlessDge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWssCardEnableFilterlessDge.setStatus("current")
_TnSfdCardTable_Object = MibTable
tnSfdCardTable = _TnSfdCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 10)
)
if mibBuilder.loadTexts:
    tnSfdCardTable.setStatus("current")
_TnSfdCardEntry_Object = MibTableRow
tnSfdCardEntry = _TnSfdCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 10, 1)
)
tnSfdCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSfdCardEntry.setStatus("current")


class _TnSfdCardAverageMuxInsertionLoss_Type(SnmpAdminString):
    """Custom type tnSfdCardAverageMuxInsertionLoss based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSfdCardAverageMuxInsertionLoss_Type.__name__ = "SnmpAdminString"
_TnSfdCardAverageMuxInsertionLoss_Object = MibTableColumn
tnSfdCardAverageMuxInsertionLoss = _TnSfdCardAverageMuxInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 10, 1, 1),
    _TnSfdCardAverageMuxInsertionLoss_Type()
)
tnSfdCardAverageMuxInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfdCardAverageMuxInsertionLoss.setStatus("current")


class _TnSfdCardAverageDemuxInsertionLoss_Type(SnmpAdminString):
    """Custom type tnSfdCardAverageDemuxInsertionLoss based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSfdCardAverageDemuxInsertionLoss_Type.__name__ = "SnmpAdminString"
_TnSfdCardAverageDemuxInsertionLoss_Object = MibTableColumn
tnSfdCardAverageDemuxInsertionLoss = _TnSfdCardAverageDemuxInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 10, 1, 2),
    _TnSfdCardAverageDemuxInsertionLoss_Type()
)
tnSfdCardAverageDemuxInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfdCardAverageDemuxInsertionLoss.setStatus("current")
_TnSonetSdhPpSectionCardTable_Object = MibTable
tnSonetSdhPpSectionCardTable = _TnSonetSdhPpSectionCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11)
)
if mibBuilder.loadTexts:
    tnSonetSdhPpSectionCardTable.setStatus("current")
_TnSonetSdhPpSectionCardEntry_Object = MibTableRow
tnSonetSdhPpSectionCardEntry = _TnSonetSdhPpSectionCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1)
)
tnSonetSdhPpSectionCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSonetSdhPpSectionCardEntry.setStatus("current")
_TnSonetSdhPpSection1Port_Type = Unsigned32
_TnSonetSdhPpSection1Port_Object = MibTableColumn
tnSonetSdhPpSection1Port = _TnSonetSdhPpSection1Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 1),
    _TnSonetSdhPpSection1Port_Type()
)
tnSonetSdhPpSection1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection1Port.setStatus("current")
_TnSonetSdhPpSection2Port_Type = Unsigned32
_TnSonetSdhPpSection2Port_Object = MibTableColumn
tnSonetSdhPpSection2Port = _TnSonetSdhPpSection2Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 2),
    _TnSonetSdhPpSection2Port_Type()
)
tnSonetSdhPpSection2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection2Port.setStatus("current")
_TnSonetSdhPpSection3Port_Type = Unsigned32
_TnSonetSdhPpSection3Port_Object = MibTableColumn
tnSonetSdhPpSection3Port = _TnSonetSdhPpSection3Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 3),
    _TnSonetSdhPpSection3Port_Type()
)
tnSonetSdhPpSection3Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection3Port.setStatus("current")
_TnSonetSdhPpSection4Port_Type = Unsigned32
_TnSonetSdhPpSection4Port_Object = MibTableColumn
tnSonetSdhPpSection4Port = _TnSonetSdhPpSection4Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 4),
    _TnSonetSdhPpSection4Port_Type()
)
tnSonetSdhPpSection4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection4Port.setStatus("current")
_TnSonetSdhPpSection5Port_Type = Unsigned32
_TnSonetSdhPpSection5Port_Object = MibTableColumn
tnSonetSdhPpSection5Port = _TnSonetSdhPpSection5Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 5),
    _TnSonetSdhPpSection5Port_Type()
)
tnSonetSdhPpSection5Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection5Port.setStatus("current")
_TnSonetSdhPpSection6Port_Type = Unsigned32
_TnSonetSdhPpSection6Port_Object = MibTableColumn
tnSonetSdhPpSection6Port = _TnSonetSdhPpSection6Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 6),
    _TnSonetSdhPpSection6Port_Type()
)
tnSonetSdhPpSection6Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection6Port.setStatus("current")
_TnSonetSdhPpSection7Port_Type = Unsigned32
_TnSonetSdhPpSection7Port_Object = MibTableColumn
tnSonetSdhPpSection7Port = _TnSonetSdhPpSection7Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 7),
    _TnSonetSdhPpSection7Port_Type()
)
tnSonetSdhPpSection7Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection7Port.setStatus("current")
_TnSonetSdhPpSection8Port_Type = Unsigned32
_TnSonetSdhPpSection8Port_Object = MibTableColumn
tnSonetSdhPpSection8Port = _TnSonetSdhPpSection8Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 8),
    _TnSonetSdhPpSection8Port_Type()
)
tnSonetSdhPpSection8Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection8Port.setStatus("current")
_TnSonetSdhPpSection1IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection1IfType_Object = MibTableColumn
tnSonetSdhPpSection1IfType = _TnSonetSdhPpSection1IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 9),
    _TnSonetSdhPpSection1IfType_Type()
)
tnSonetSdhPpSection1IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection1IfType.setStatus("current")
_TnSonetSdhPpSection2IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection2IfType_Object = MibTableColumn
tnSonetSdhPpSection2IfType = _TnSonetSdhPpSection2IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 10),
    _TnSonetSdhPpSection2IfType_Type()
)
tnSonetSdhPpSection2IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection2IfType.setStatus("current")
_TnSonetSdhPpSection3IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection3IfType_Object = MibTableColumn
tnSonetSdhPpSection3IfType = _TnSonetSdhPpSection3IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 11),
    _TnSonetSdhPpSection3IfType_Type()
)
tnSonetSdhPpSection3IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection3IfType.setStatus("current")
_TnSonetSdhPpSection4IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection4IfType_Object = MibTableColumn
tnSonetSdhPpSection4IfType = _TnSonetSdhPpSection4IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 12),
    _TnSonetSdhPpSection4IfType_Type()
)
tnSonetSdhPpSection4IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection4IfType.setStatus("current")
_TnSonetSdhPpSection5IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection5IfType_Object = MibTableColumn
tnSonetSdhPpSection5IfType = _TnSonetSdhPpSection5IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 13),
    _TnSonetSdhPpSection5IfType_Type()
)
tnSonetSdhPpSection5IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection5IfType.setStatus("current")
_TnSonetSdhPpSection6IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection6IfType_Object = MibTableColumn
tnSonetSdhPpSection6IfType = _TnSonetSdhPpSection6IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 14),
    _TnSonetSdhPpSection6IfType_Type()
)
tnSonetSdhPpSection6IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection6IfType.setStatus("current")
_TnSonetSdhPpSection7IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection7IfType_Object = MibTableColumn
tnSonetSdhPpSection7IfType = _TnSonetSdhPpSection7IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 15),
    _TnSonetSdhPpSection7IfType_Type()
)
tnSonetSdhPpSection7IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection7IfType.setStatus("current")
_TnSonetSdhPpSection8IfType_Type = AluWdmSonetSdhPpSectionIfType
_TnSonetSdhPpSection8IfType_Object = MibTableColumn
tnSonetSdhPpSection8IfType = _TnSonetSdhPpSection8IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 11, 1, 16),
    _TnSonetSdhPpSection8IfType_Type()
)
tnSonetSdhPpSection8IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSonetSdhPpSection8IfType.setStatus("current")
_TnPcsSectionCardTable_Object = MibTable
tnPcsSectionCardTable = _TnPcsSectionCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12)
)
if mibBuilder.loadTexts:
    tnPcsSectionCardTable.setStatus("current")
_TnPcsSectionCardEntry_Object = MibTableRow
tnPcsSectionCardEntry = _TnPcsSectionCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1)
)
tnPcsSectionCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPcsSectionCardEntry.setStatus("current")
_TnPcsSection1Port_Type = Unsigned32
_TnPcsSection1Port_Object = MibTableColumn
tnPcsSection1Port = _TnPcsSection1Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 1),
    _TnPcsSection1Port_Type()
)
tnPcsSection1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection1Port.setStatus("current")
_TnPcsSection2Port_Type = Unsigned32
_TnPcsSection2Port_Object = MibTableColumn
tnPcsSection2Port = _TnPcsSection2Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 2),
    _TnPcsSection2Port_Type()
)
tnPcsSection2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection2Port.setStatus("current")
_TnPcsSection3Port_Type = Unsigned32
_TnPcsSection3Port_Object = MibTableColumn
tnPcsSection3Port = _TnPcsSection3Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 3),
    _TnPcsSection3Port_Type()
)
tnPcsSection3Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection3Port.setStatus("current")
_TnPcsSection4Port_Type = Unsigned32
_TnPcsSection4Port_Object = MibTableColumn
tnPcsSection4Port = _TnPcsSection4Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 4),
    _TnPcsSection4Port_Type()
)
tnPcsSection4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection4Port.setStatus("current")
_TnPcsSection5Port_Type = Unsigned32
_TnPcsSection5Port_Object = MibTableColumn
tnPcsSection5Port = _TnPcsSection5Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 5),
    _TnPcsSection5Port_Type()
)
tnPcsSection5Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection5Port.setStatus("current")
_TnPcsSection6Port_Type = Unsigned32
_TnPcsSection6Port_Object = MibTableColumn
tnPcsSection6Port = _TnPcsSection6Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 6),
    _TnPcsSection6Port_Type()
)
tnPcsSection6Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection6Port.setStatus("current")
_TnPcsSection7Port_Type = Unsigned32
_TnPcsSection7Port_Object = MibTableColumn
tnPcsSection7Port = _TnPcsSection7Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 7),
    _TnPcsSection7Port_Type()
)
tnPcsSection7Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection7Port.setStatus("current")
_TnPcsSection8Port_Type = Unsigned32
_TnPcsSection8Port_Object = MibTableColumn
tnPcsSection8Port = _TnPcsSection8Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 8),
    _TnPcsSection8Port_Type()
)
tnPcsSection8Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection8Port.setStatus("current")
_TnPcsSection9Port_Type = Unsigned32
_TnPcsSection9Port_Object = MibTableColumn
tnPcsSection9Port = _TnPcsSection9Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 9),
    _TnPcsSection9Port_Type()
)
tnPcsSection9Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection9Port.setStatus("current")
_TnPcsSection10Port_Type = Unsigned32
_TnPcsSection10Port_Object = MibTableColumn
tnPcsSection10Port = _TnPcsSection10Port_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 10),
    _TnPcsSection10Port_Type()
)
tnPcsSection10Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection10Port.setStatus("current")
_TnPcsSection1IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection1IfType_Object = MibTableColumn
tnPcsSection1IfType = _TnPcsSection1IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 11),
    _TnPcsSection1IfType_Type()
)
tnPcsSection1IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection1IfType.setStatus("current")
_TnPcsSection2IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection2IfType_Object = MibTableColumn
tnPcsSection2IfType = _TnPcsSection2IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 12),
    _TnPcsSection2IfType_Type()
)
tnPcsSection2IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection2IfType.setStatus("current")
_TnPcsSection3IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection3IfType_Object = MibTableColumn
tnPcsSection3IfType = _TnPcsSection3IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 13),
    _TnPcsSection3IfType_Type()
)
tnPcsSection3IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection3IfType.setStatus("current")
_TnPcsSection4IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection4IfType_Object = MibTableColumn
tnPcsSection4IfType = _TnPcsSection4IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 14),
    _TnPcsSection4IfType_Type()
)
tnPcsSection4IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection4IfType.setStatus("current")
_TnPcsSection5IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection5IfType_Object = MibTableColumn
tnPcsSection5IfType = _TnPcsSection5IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 15),
    _TnPcsSection5IfType_Type()
)
tnPcsSection5IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection5IfType.setStatus("current")
_TnPcsSection6IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection6IfType_Object = MibTableColumn
tnPcsSection6IfType = _TnPcsSection6IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 16),
    _TnPcsSection6IfType_Type()
)
tnPcsSection6IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection6IfType.setStatus("current")
_TnPcsSection7IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection7IfType_Object = MibTableColumn
tnPcsSection7IfType = _TnPcsSection7IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 17),
    _TnPcsSection7IfType_Type()
)
tnPcsSection7IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection7IfType.setStatus("current")
_TnPcsSection8IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection8IfType_Object = MibTableColumn
tnPcsSection8IfType = _TnPcsSection8IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 18),
    _TnPcsSection8IfType_Type()
)
tnPcsSection8IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection8IfType.setStatus("current")
_TnPcsSection9IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection9IfType_Object = MibTableColumn
tnPcsSection9IfType = _TnPcsSection9IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 19),
    _TnPcsSection9IfType_Type()
)
tnPcsSection9IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection9IfType.setStatus("current")
_TnPcsSection10IfType_Type = AluWdmPcsSectionIfType
_TnPcsSection10IfType_Object = MibTableColumn
tnPcsSection10IfType = _TnPcsSection10IfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 12, 1, 20),
    _TnPcsSection10IfType_Type()
)
tnPcsSection10IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPcsSection10IfType.setStatus("current")
_Tn11dpge12CardTable_Object = MibTable
tn11dpge12CardTable = _Tn11dpge12CardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 14)
)
if mibBuilder.loadTexts:
    tn11dpge12CardTable.setStatus("current")
_Tn11dpge12CardEntry_Object = MibTableRow
tn11dpge12CardEntry = _Tn11dpge12CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 14, 1)
)
tn11dpge12CardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn11dpge12CardEntry.setStatus("current")


class _Tn11dpge12CardRateMode_Type(Integer32):
    """Custom type tn11dpge12CardRateMode based on Integer32"""
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
        *(("fullRate", 1),
          ("subRate", 2),
          ("qinqRate", 3))
    )


_Tn11dpge12CardRateMode_Type.__name__ = "Integer32"
_Tn11dpge12CardRateMode_Object = MibTableColumn
tn11dpge12CardRateMode = _Tn11dpge12CardRateMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 14, 1, 1),
    _Tn11dpge12CardRateMode_Type()
)
tn11dpge12CardRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpge12CardRateMode.setStatus("current")
_Tn11dpge12QINQModeTPID_Type = Unsigned32
_Tn11dpge12QINQModeTPID_Object = MibTableColumn
tn11dpge12QINQModeTPID = _Tn11dpge12QINQModeTPID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 14, 1, 2),
    _Tn11dpge12QINQModeTPID_Type()
)
tn11dpge12QINQModeTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpge12QINQModeTPID.setStatus("current")
_TnSfcCardTable_Object = MibTable
tnSfcCardTable = _TnSfcCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 15)
)
if mibBuilder.loadTexts:
    tnSfcCardTable.setStatus("current")
_TnSfcCardEntry_Object = MibTableRow
tnSfcCardEntry = _TnSfcCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 15, 1)
)
tnSfcCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSfcCardEntry.setStatus("current")


class _TnSfcCardFiberMode_Type(Integer32):
    """Custom type tnSfcCardFiberMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoFiber", 1),
          ("oneFiberMux", 2))
    )


_TnSfcCardFiberMode_Type.__name__ = "Integer32"
_TnSfcCardFiberMode_Object = MibTableColumn
tnSfcCardFiberMode = _TnSfcCardFiberMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 15, 1, 1),
    _TnSfcCardFiberMode_Type()
)
tnSfcCardFiberMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSfcCardFiberMode.setStatus("current")
_Tn11dpe12eCardTable_Object = MibTable
tn11dpe12eCardTable = _Tn11dpe12eCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18)
)
if mibBuilder.loadTexts:
    tn11dpe12eCardTable.setStatus("current")
_Tn11dpe12eCardEntry_Object = MibTableRow
tn11dpe12eCardEntry = _Tn11dpe12eCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1)
)
tn11dpe12eCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn11dpe12eCardEntry.setStatus("current")


class _Tn11dpe12eCardRateMode_Type(Integer32):
    """Custom type tn11dpe12eCardRateMode based on Integer32"""
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
        *(("fullRate", 1),
          ("subRate", 2),
          ("qinqRate", 3))
    )


_Tn11dpe12eCardRateMode_Type.__name__ = "Integer32"
_Tn11dpe12eCardRateMode_Object = MibTableColumn
tn11dpe12eCardRateMode = _Tn11dpe12eCardRateMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 1),
    _Tn11dpe12eCardRateMode_Type()
)
tn11dpe12eCardRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eCardRateMode.setStatus("current")
_Tn11dpe12eQINQModeTPID1_Type = Unsigned32
_Tn11dpe12eQINQModeTPID1_Object = MibTableColumn
tn11dpe12eQINQModeTPID1 = _Tn11dpe12eQINQModeTPID1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 2),
    _Tn11dpe12eQINQModeTPID1_Type()
)
tn11dpe12eQINQModeTPID1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeTPID1.setStatus("current")
_Tn11dpe12eQINQModeTPID2_Type = Unsigned32
_Tn11dpe12eQINQModeTPID2_Object = MibTableColumn
tn11dpe12eQINQModeTPID2 = _Tn11dpe12eQINQModeTPID2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 3),
    _Tn11dpe12eQINQModeTPID2_Type()
)
tn11dpe12eQINQModeTPID2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeTPID2.setStatus("current")
_Tn11dpe12eQINQModeTPID3_Type = Unsigned32
_Tn11dpe12eQINQModeTPID3_Object = MibTableColumn
tn11dpe12eQINQModeTPID3 = _Tn11dpe12eQINQModeTPID3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 4),
    _Tn11dpe12eQINQModeTPID3_Type()
)
tn11dpe12eQINQModeTPID3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeTPID3.setStatus("current")
_Tn11dpe12eQINQModeTPID4_Type = Unsigned32
_Tn11dpe12eQINQModeTPID4_Object = MibTableColumn
tn11dpe12eQINQModeTPID4 = _Tn11dpe12eQINQModeTPID4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 5),
    _Tn11dpe12eQINQModeTPID4_Type()
)
tn11dpe12eQINQModeTPID4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeTPID4.setStatus("current")


class _Tn11dpe12eQINQModeFlowCm_Type(Integer32):
    """Custom type tn11dpe12eQINQModeFlowCm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apspcc", 1),
          ("ccm", 2))
    )


_Tn11dpe12eQINQModeFlowCm_Type.__name__ = "Integer32"
_Tn11dpe12eQINQModeFlowCm_Object = MibTableColumn
tn11dpe12eQINQModeFlowCm = _Tn11dpe12eQINQModeFlowCm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 18, 1, 6),
    _Tn11dpe12eQINQModeFlowCm_Type()
)
tn11dpe12eQINQModeFlowCm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12eQINQModeFlowCm.setStatus("current")
_Tn1dpp24mCardTable_Object = MibTable
tn1dpp24mCardTable = _Tn1dpp24mCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 19)
)
if mibBuilder.loadTexts:
    tn1dpp24mCardTable.setStatus("current")
_Tn1dpp24mCardEntry_Object = MibTableRow
tn1dpp24mCardEntry = _Tn1dpp24mCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 19, 1)
)
tn1dpp24mCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn1dpp24mCardEntry.setStatus("current")


class _Tn1dpp24mCardFunctionMode_Type(Integer32):
    """Custom type tn1dpp24mCardFunctionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_Tn1dpp24mCardFunctionMode_Type.__name__ = "Integer32"
_Tn1dpp24mCardFunctionMode_Object = MibTableColumn
tn1dpp24mCardFunctionMode = _Tn1dpp24mCardFunctionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 19, 1, 1),
    _Tn1dpp24mCardFunctionMode_Type()
)
tn1dpp24mCardFunctionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn1dpp24mCardFunctionMode.setStatus("current")


class _Tn1dpp24mCardImpedance_Type(Integer32):
    """Custom type tn1dpp24mCardImpedance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("imp75ohm", 1),
          ("imp120ohm", 2))
    )


_Tn1dpp24mCardImpedance_Type.__name__ = "Integer32"
_Tn1dpp24mCardImpedance_Object = MibTableColumn
tn1dpp24mCardImpedance = _Tn1dpp24mCardImpedance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 19, 1, 2),
    _Tn1dpp24mCardImpedance_Type()
)
tn1dpp24mCardImpedance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn1dpp24mCardImpedance.setStatus("current")
_TnOpsCardTable_Object = MibTable
tnOpsCardTable = _TnOpsCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 21)
)
if mibBuilder.loadTexts:
    tnOpsCardTable.setStatus("current")
_TnOpsCardEntry_Object = MibTableRow
tnOpsCardEntry = _TnOpsCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 21, 1)
)
tnOpsCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnOpsCardEntry.setStatus("current")


class _TnOpsCardProtectionMode_Type(Integer32):
    """Custom type tnOpsCardProtectionMode based on Integer32"""
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
        *(("ochp", 1),
          ("olp", 2),
          ("omsp", 3),
          ("otup", 4))
    )


_TnOpsCardProtectionMode_Type.__name__ = "Integer32"
_TnOpsCardProtectionMode_Object = MibTableColumn
tnOpsCardProtectionMode = _TnOpsCardProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 21, 1, 1),
    _TnOpsCardProtectionMode_Type()
)
tnOpsCardProtectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnOpsCardProtectionMode.setStatus("current")
_Tn11dpe12aCardTable_Object = MibTable
tn11dpe12aCardTable = _Tn11dpe12aCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22)
)
if mibBuilder.loadTexts:
    tn11dpe12aCardTable.setStatus("current")
_Tn11dpe12aCardEntry_Object = MibTableRow
tn11dpe12aCardEntry = _Tn11dpe12aCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1)
)
tn11dpe12aCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn11dpe12aCardEntry.setStatus("current")


class _Tn11dpe12aCardRateMode_Type(Integer32):
    """Custom type tn11dpe12aCardRateMode based on Integer32"""
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
        *(("fullRate", 1),
          ("subRate", 2),
          ("qinqRate", 3))
    )


_Tn11dpe12aCardRateMode_Type.__name__ = "Integer32"
_Tn11dpe12aCardRateMode_Object = MibTableColumn
tn11dpe12aCardRateMode = _Tn11dpe12aCardRateMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 1),
    _Tn11dpe12aCardRateMode_Type()
)
tn11dpe12aCardRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardRateMode.setStatus("current")
_Tn11dpe12aCardQINQModeTPID1_Type = Unsigned32
_Tn11dpe12aCardQINQModeTPID1_Object = MibTableColumn
tn11dpe12aCardQINQModeTPID1 = _Tn11dpe12aCardQINQModeTPID1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 2),
    _Tn11dpe12aCardQINQModeTPID1_Type()
)
tn11dpe12aCardQINQModeTPID1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardQINQModeTPID1.setStatus("current")
_Tn11dpe12aCardQINQModeTPID2_Type = Unsigned32
_Tn11dpe12aCardQINQModeTPID2_Object = MibTableColumn
tn11dpe12aCardQINQModeTPID2 = _Tn11dpe12aCardQINQModeTPID2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 3),
    _Tn11dpe12aCardQINQModeTPID2_Type()
)
tn11dpe12aCardQINQModeTPID2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardQINQModeTPID2.setStatus("current")
_Tn11dpe12aCardQINQModeTPID3_Type = Unsigned32
_Tn11dpe12aCardQINQModeTPID3_Object = MibTableColumn
tn11dpe12aCardQINQModeTPID3 = _Tn11dpe12aCardQINQModeTPID3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 4),
    _Tn11dpe12aCardQINQModeTPID3_Type()
)
tn11dpe12aCardQINQModeTPID3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardQINQModeTPID3.setStatus("current")
_Tn11dpe12aCardQINQModeTPID4_Type = Unsigned32
_Tn11dpe12aCardQINQModeTPID4_Object = MibTableColumn
tn11dpe12aCardQINQModeTPID4 = _Tn11dpe12aCardQINQModeTPID4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 5),
    _Tn11dpe12aCardQINQModeTPID4_Type()
)
tn11dpe12aCardQINQModeTPID4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardQINQModeTPID4.setStatus("current")


class _Tn11dpe12aCardLBMInterval_Type(Unsigned32):
    """Custom type tn11dpe12aCardLBMInterval based on Unsigned32"""
    defaultValue = 1000


_Tn11dpe12aCardLBMInterval_Type.__name__ = "Unsigned32"
_Tn11dpe12aCardLBMInterval_Object = MibTableColumn
tn11dpe12aCardLBMInterval = _Tn11dpe12aCardLBMInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 6),
    _Tn11dpe12aCardLBMInterval_Type()
)
tn11dpe12aCardLBMInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardLBMInterval.setStatus("current")
if mibBuilder.loadTexts:
    tn11dpe12aCardLBMInterval.setUnits("ms")


class _Tn11dpe12aCardLBRTimeout_Type(Unsigned32):
    """Custom type tn11dpe12aCardLBRTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Tn11dpe12aCardLBRTimeout_Type.__name__ = "Unsigned32"
_Tn11dpe12aCardLBRTimeout_Object = MibTableColumn
tn11dpe12aCardLBRTimeout = _Tn11dpe12aCardLBRTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 7),
    _Tn11dpe12aCardLBRTimeout_Type()
)
tn11dpe12aCardLBRTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardLBRTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tn11dpe12aCardLBRTimeout.setUnits("seconds")


class _Tn11dpe12aCardFlowCm_Type(Integer32):
    """Custom type tn11dpe12aCardFlowCm based on Integer32"""
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
        *(("apspcc", 1),
          ("ccm", 2),
          ("csf", 3))
    )


_Tn11dpe12aCardFlowCm_Type.__name__ = "Integer32"
_Tn11dpe12aCardFlowCm_Object = MibTableColumn
tn11dpe12aCardFlowCm = _Tn11dpe12aCardFlowCm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 8),
    _Tn11dpe12aCardFlowCm_Type()
)
tn11dpe12aCardFlowCm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardFlowCm.setStatus("current")


class _Tn11dpe12aCardSLRTimeout_Type(Unsigned32):
    """Custom type tn11dpe12aCardSLRTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Tn11dpe12aCardSLRTimeout_Type.__name__ = "Unsigned32"
_Tn11dpe12aCardSLRTimeout_Object = MibTableColumn
tn11dpe12aCardSLRTimeout = _Tn11dpe12aCardSLRTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 9),
    _Tn11dpe12aCardSLRTimeout_Type()
)
tn11dpe12aCardSLRTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardSLRTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tn11dpe12aCardSLRTimeout.setUnits("seconds")


class _Tn11dpe12aCardCrossPackServiceSupported_Type(Integer32):
    """Custom type tn11dpe12aCardCrossPackServiceSupported based on Integer32"""
    defaultValue = 2

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


_Tn11dpe12aCardCrossPackServiceSupported_Type.__name__ = "Integer32"
_Tn11dpe12aCardCrossPackServiceSupported_Object = MibTableColumn
tn11dpe12aCardCrossPackServiceSupported = _Tn11dpe12aCardCrossPackServiceSupported_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 22, 1, 10),
    _Tn11dpe12aCardCrossPackServiceSupported_Type()
)
tn11dpe12aCardCrossPackServiceSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn11dpe12aCardCrossPackServiceSupported.setStatus("current")
_TnCardFunctionModeTable_Object = MibTable
tnCardFunctionModeTable = _TnCardFunctionModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 23)
)
if mibBuilder.loadTexts:
    tnCardFunctionModeTable.setStatus("current")
_TnCardFunctionModeEntry_Object = MibTableRow
tnCardFunctionModeEntry = _TnCardFunctionModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 23, 1)
)
tnCardFunctionModeEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnCardFunctionModeEntry.setStatus("current")


class _TnCardFunctionMode_Type(Integer32):
    """Custom type tnCardFunctionMode based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("flexMux", 1),
          ("dualTran", 2),
          ("sonetSdh", 3),
          ("otu3", 4),
          ("hundredGbe", 5),
          ("otu4", 6),
          ("pTPIOCTLLocalClock", 7),
          ("pTPIOCTLCentralizedClock", 8),
          ("pTPIOCTLRelay", 9),
          ("pTPIOCTLLambdaConversion", 10),
          ("hundredGBEInterwork", 11),
          ("hundredGBEBkp400", 12),
          ("hundredGBEBjFec", 13),
          ("otl410", 14),
          ("caui", 15),
          ("eth100g", 16),
          ("otn100gbe", 17),
          ("otn100Gbe200Gbe", 18),
          ("threeX100Gbe2xOtu4", 19),
          ("threeX100Gbe2x100GbeBjFec", 20),
          ("threeX100GbeBjFec2xOtu4", 21),
          ("clientLine", 22),
          ("clientHairPin", 23),
          ("otn100GbeEncrypt", 24),
          ("none", 25),
          ("fst", 26),
          ("aes256Ctr", 27),
          ("aes256Gcm", 28),
          ("demo", 29))
    )


_TnCardFunctionMode_Type.__name__ = "Integer32"
_TnCardFunctionMode_Object = MibTableColumn
tnCardFunctionMode = _TnCardFunctionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 23, 1, 1),
    _TnCardFunctionMode_Type()
)
tnCardFunctionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardFunctionMode.setStatus("current")
_Tn112pdm11CardTable_Object = MibTable
tn112pdm11CardTable = _Tn112pdm11CardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 24)
)
if mibBuilder.loadTexts:
    tn112pdm11CardTable.setStatus("current")
_Tn112pdm11CardEntry_Object = MibTableRow
tn112pdm11CardEntry = _Tn112pdm11CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 24, 1)
)
tn112pdm11CardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tn112pdm11CardEntry.setStatus("current")


class _Tn112pdm11CardMaxDMNumbers_Type(Unsigned32):
    """Custom type tn112pdm11CardMaxDMNumbers based on Unsigned32"""
    defaultValue = 1


_Tn112pdm11CardMaxDMNumbers_Type.__name__ = "Unsigned32"
_Tn112pdm11CardMaxDMNumbers_Object = MibTableColumn
tn112pdm11CardMaxDMNumbers = _Tn112pdm11CardMaxDMNumbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 24, 1, 1),
    _Tn112pdm11CardMaxDMNumbers_Type()
)
tn112pdm11CardMaxDMNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112pdm11CardMaxDMNumbers.setStatus("current")


class _Tn112pdm11CardUsedDMNumbers_Type(Unsigned32):
    """Custom type tn112pdm11CardUsedDMNumbers based on Unsigned32"""
    defaultValue = 0


_Tn112pdm11CardUsedDMNumbers_Type.__name__ = "Unsigned32"
_Tn112pdm11CardUsedDMNumbers_Object = MibTableColumn
tn112pdm11CardUsedDMNumbers = _Tn112pdm11CardUsedDMNumbers_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 24, 1, 2),
    _Tn112pdm11CardUsedDMNumbers_Type()
)
tn112pdm11CardUsedDMNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn112pdm11CardUsedDMNumbers.setStatus("current")
_TnPtpctlCardAttributeTotal_Type = Integer32
_TnPtpctlCardAttributeTotal_Object = MibScalar
tnPtpctlCardAttributeTotal = _TnPtpctlCardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 25),
    _TnPtpctlCardAttributeTotal_Type()
)
tnPtpctlCardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardAttributeTotal.setStatus("current")
_TnPtpctlCardTable_Object = MibTable
tnPtpctlCardTable = _TnPtpctlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26)
)
if mibBuilder.loadTexts:
    tnPtpctlCardTable.setStatus("current")
_TnPtpctlCardEntry_Object = MibTableRow
tnPtpctlCardEntry = _TnPtpctlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1)
)
tnPtpctlCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPtpctlCardEntry.setStatus("current")
_TnPtpctlCardEqpsLEDColor_Type = TropicLEDColorType
_TnPtpctlCardEqpsLEDColor_Object = MibTableColumn
tnPtpctlCardEqpsLEDColor = _TnPtpctlCardEqpsLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1, 1),
    _TnPtpctlCardEqpsLEDColor_Type()
)
tnPtpctlCardEqpsLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardEqpsLEDColor.setStatus("current")
_TnPtpctlCardEqpsLEDState_Type = TropicLEDStateType
_TnPtpctlCardEqpsLEDState_Object = MibTableColumn
tnPtpctlCardEqpsLEDState = _TnPtpctlCardEqpsLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1, 2),
    _TnPtpctlCardEqpsLEDState_Type()
)
tnPtpctlCardEqpsLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardEqpsLEDState.setStatus("current")
_TnPtpctlCardPtpLEDColor_Type = TropicLEDColorType
_TnPtpctlCardPtpLEDColor_Object = MibTableColumn
tnPtpctlCardPtpLEDColor = _TnPtpctlCardPtpLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1, 3),
    _TnPtpctlCardPtpLEDColor_Type()
)
tnPtpctlCardPtpLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardPtpLEDColor.setStatus("current")
_TnPtpctlCardPtpLEDState_Type = TropicLEDStateType
_TnPtpctlCardPtpLEDState_Object = MibTableColumn
tnPtpctlCardPtpLEDState = _TnPtpctlCardPtpLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 26, 1, 4),
    _TnPtpctlCardPtpLEDState_Type()
)
tnPtpctlCardPtpLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPtpctlCardPtpLEDState.setStatus("current")
_TnWtocmaCardAttributeTotal_Type = Integer32
_TnWtocmaCardAttributeTotal_Object = MibScalar
tnWtocmaCardAttributeTotal = _TnWtocmaCardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 27),
    _TnWtocmaCardAttributeTotal_Type()
)
tnWtocmaCardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmaCardAttributeTotal.setStatus("current")
_TnWtocmaCardTable_Object = MibTable
tnWtocmaCardTable = _TnWtocmaCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28)
)
if mibBuilder.loadTexts:
    tnWtocmaCardTable.setStatus("current")
_TnWtocmaCardEntry_Object = MibTableRow
tnWtocmaCardEntry = _TnWtocmaCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1)
)
tnWtocmaCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnWtocmaCardEntry.setStatus("current")


class _TnWtocmaCardOsnrScan_Type(TnCommand):
    """Custom type tnWtocmaCardOsnrScan based on TnCommand"""
    defaultValue = 1


_TnWtocmaCardOsnrScan_Type.__name__ = "TnCommand"
_TnWtocmaCardOsnrScan_Object = MibTableColumn
tnWtocmaCardOsnrScan = _TnWtocmaCardOsnrScan_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1, 1),
    _TnWtocmaCardOsnrScan_Type()
)
tnWtocmaCardOsnrScan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtocmaCardOsnrScan.setStatus("current")


class _TnWtocmaCardOsnrScanAbort_Type(TnCommand):
    """Custom type tnWtocmaCardOsnrScanAbort based on TnCommand"""
    defaultValue = 1


_TnWtocmaCardOsnrScanAbort_Type.__name__ = "TnCommand"
_TnWtocmaCardOsnrScanAbort_Object = MibTableColumn
tnWtocmaCardOsnrScanAbort = _TnWtocmaCardOsnrScanAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1, 2),
    _TnWtocmaCardOsnrScanAbort_Type()
)
tnWtocmaCardOsnrScanAbort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnWtocmaCardOsnrScanAbort.setStatus("current")


class _TnWtocmaCardOsnrScanStatus_Type(Integer32):
    """Custom type tnWtocmaCardOsnrScanStatus based on Integer32"""
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
        *(("notInProgress", 1),
          ("inProgress", 2),
          ("waiting", 3))
    )


_TnWtocmaCardOsnrScanStatus_Type.__name__ = "Integer32"
_TnWtocmaCardOsnrScanStatus_Object = MibTableColumn
tnWtocmaCardOsnrScanStatus = _TnWtocmaCardOsnrScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1, 3),
    _TnWtocmaCardOsnrScanStatus_Type()
)
tnWtocmaCardOsnrScanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmaCardOsnrScanStatus.setStatus("current")


class _TnWtocmaCardDspState_Type(Integer32):
    """Custom type tnWtocmaCardDspState based on Integer32"""
    defaultValue = 1

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
        *(("newChan", 1),
          ("osnr", 2),
          ("osnrOnDemand", 3),
          ("misKeyedChan", 4),
          ("idle", 5))
    )


_TnWtocmaCardDspState_Type.__name__ = "Integer32"
_TnWtocmaCardDspState_Object = MibTableColumn
tnWtocmaCardDspState = _TnWtocmaCardDspState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 28, 1, 4),
    _TnWtocmaCardDspState_Type()
)
tnWtocmaCardDspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWtocmaCardDspState.setStatus("current")
_TnCruCardAttributeTotal_Type = Integer32
_TnCruCardAttributeTotal_Object = MibScalar
tnCruCardAttributeTotal = _TnCruCardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 29),
    _TnCruCardAttributeTotal_Type()
)
tnCruCardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCruCardAttributeTotal.setStatus("current")
_TnCruCardTable_Object = MibTable
tnCruCardTable = _TnCruCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30)
)
if mibBuilder.loadTexts:
    tnCruCardTable.setStatus("current")
_TnCruCardEntry_Object = MibTableRow
tnCruCardEntry = _TnCruCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30, 1)
)
tnCruCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnCruCardEntry.setStatus("current")


class _TnCruCardActivityState_Type(Integer32):
    """Custom type tnCruCardActivityState based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 1),
          ("unequipped", 2),
          ("active", 3),
          ("standbyTrackingToActive", 4),
          ("standbyNotTrackingToActive", 5))
    )


_TnCruCardActivityState_Type.__name__ = "Integer32"
_TnCruCardActivityState_Object = MibTableColumn
tnCruCardActivityState = _TnCruCardActivityState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30, 1, 1),
    _TnCruCardActivityState_Type()
)
tnCruCardActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCruCardActivityState.setStatus("current")
_TnCruCardEqpsLEDColor_Type = TropicLEDColorType
_TnCruCardEqpsLEDColor_Object = MibTableColumn
tnCruCardEqpsLEDColor = _TnCruCardEqpsLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30, 1, 2),
    _TnCruCardEqpsLEDColor_Type()
)
tnCruCardEqpsLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCruCardEqpsLEDColor.setStatus("current")
_TnCruCardEqpsLEDState_Type = TropicLEDStateType
_TnCruCardEqpsLEDState_Object = MibTableColumn
tnCruCardEqpsLEDState = _TnCruCardEqpsLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30, 1, 3),
    _TnCruCardEqpsLEDState_Type()
)
tnCruCardEqpsLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCruCardEqpsLEDState.setStatus("current")
_TnFCruProtectionRole_Type = AluWdmFcruProtectionRoleType
_TnFCruProtectionRole_Object = MibTableColumn
tnFCruProtectionRole = _TnFCruProtectionRole_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 30, 1, 4),
    _TnFCruProtectionRole_Type()
)
tnFCruProtectionRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFCruProtectionRole.setStatus("current")
_TnIroadmCardConfigAttributeTotal_Type = Integer32
_TnIroadmCardConfigAttributeTotal_Object = MibScalar
tnIroadmCardConfigAttributeTotal = _TnIroadmCardConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 31),
    _TnIroadmCardConfigAttributeTotal_Type()
)
tnIroadmCardConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIroadmCardConfigAttributeTotal.setStatus("current")
_TnIroadmCardConfigTable_Object = MibTable
tnIroadmCardConfigTable = _TnIroadmCardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 32)
)
if mibBuilder.loadTexts:
    tnIroadmCardConfigTable.setStatus("current")
_TnIroadmCardConfigEntry_Object = MibTableRow
tnIroadmCardConfigEntry = _TnIroadmCardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 32, 1)
)
tnIroadmCardConfigEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnIroadmCardConfigEntry.setStatus("current")


class _TnIroadmCardConfigOptIntDetection_Type(Integer32):
    """Custom type tnIroadmCardConfigOptIntDetection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_TnIroadmCardConfigOptIntDetection_Type.__name__ = "Integer32"
_TnIroadmCardConfigOptIntDetection_Object = MibTableColumn
tnIroadmCardConfigOptIntDetection = _TnIroadmCardConfigOptIntDetection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 32, 1, 1),
    _TnIroadmCardConfigOptIntDetection_Type()
)
tnIroadmCardConfigOptIntDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIroadmCardConfigOptIntDetection.setStatus("current")


class _TnIroadmCardConfigOptIntBaseline_Type(Integer32):
    """Custom type tnIroadmCardConfigOptIntBaseline based on Integer32"""
    defaultValue = -100


_TnIroadmCardConfigOptIntBaseline_Type.__name__ = "Integer32"
_TnIroadmCardConfigOptIntBaseline_Object = MibTableColumn
tnIroadmCardConfigOptIntBaseline = _TnIroadmCardConfigOptIntBaseline_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 32, 1, 2),
    _TnIroadmCardConfigOptIntBaseline_Type()
)
tnIroadmCardConfigOptIntBaseline.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIroadmCardConfigOptIntBaseline.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardConfigOptIntBaseline.setUnits("mB")


class _TnIroadmCardConfigOptIntLossThreshold_Type(Unsigned32):
    """Custom type tnIroadmCardConfigOptIntLossThreshold based on Unsigned32"""
    defaultValue = 150


_TnIroadmCardConfigOptIntLossThreshold_Type.__name__ = "Unsigned32"
_TnIroadmCardConfigOptIntLossThreshold_Object = MibTableColumn
tnIroadmCardConfigOptIntLossThreshold = _TnIroadmCardConfigOptIntLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 32, 1, 3),
    _TnIroadmCardConfigOptIntLossThreshold_Type()
)
tnIroadmCardConfigOptIntLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIroadmCardConfigOptIntLossThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardConfigOptIntLossThreshold.setUnits("mB")


class _TnIroadmCardConfigOptIntPollPeriod_Type(Unsigned32):
    """Custom type tnIroadmCardConfigOptIntPollPeriod based on Unsigned32"""
    defaultValue = 30


_TnIroadmCardConfigOptIntPollPeriod_Type.__name__ = "Unsigned32"
_TnIroadmCardConfigOptIntPollPeriod_Object = MibTableColumn
tnIroadmCardConfigOptIntPollPeriod = _TnIroadmCardConfigOptIntPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 32, 1, 4),
    _TnIroadmCardConfigOptIntPollPeriod_Type()
)
tnIroadmCardConfigOptIntPollPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIroadmCardConfigOptIntPollPeriod.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardConfigOptIntPollPeriod.setUnits("seconds")


class _TnIroadmCardConfigOptIntClearAlarm_Type(TnCommand):
    """Custom type tnIroadmCardConfigOptIntClearAlarm based on TnCommand"""
    defaultValue = 1


_TnIroadmCardConfigOptIntClearAlarm_Type.__name__ = "TnCommand"
_TnIroadmCardConfigOptIntClearAlarm_Object = MibTableColumn
tnIroadmCardConfigOptIntClearAlarm = _TnIroadmCardConfigOptIntClearAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 32, 1, 5),
    _TnIroadmCardConfigOptIntClearAlarm_Type()
)
tnIroadmCardConfigOptIntClearAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIroadmCardConfigOptIntClearAlarm.setStatus("current")
_TnIroadmCardInfoAttributeTotal_Type = Integer32
_TnIroadmCardInfoAttributeTotal_Object = MibScalar
tnIroadmCardInfoAttributeTotal = _TnIroadmCardInfoAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 33),
    _TnIroadmCardInfoAttributeTotal_Type()
)
tnIroadmCardInfoAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIroadmCardInfoAttributeTotal.setStatus("current")
_TnIroadmCardInfoTable_Object = MibTable
tnIroadmCardInfoTable = _TnIroadmCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 34)
)
if mibBuilder.loadTexts:
    tnIroadmCardInfoTable.setStatus("current")
_TnIroadmCardInfoEntry_Object = MibTableRow
tnIroadmCardInfoEntry = _TnIroadmCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 34, 1)
)
tnIroadmCardInfoEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnIroadmCardInfoEntry.setStatus("current")
_TnIroadmCardInfoIngressOAMPumpTemperature_Type = Integer32
_TnIroadmCardInfoIngressOAMPumpTemperature_Object = MibTableColumn
tnIroadmCardInfoIngressOAMPumpTemperature = _TnIroadmCardInfoIngressOAMPumpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 34, 1, 1),
    _TnIroadmCardInfoIngressOAMPumpTemperature_Type()
)
tnIroadmCardInfoIngressOAMPumpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIroadmCardInfoIngressOAMPumpTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardInfoIngressOAMPumpTemperature.setUnits("Celsius")


class _TnIroadmCardInfoIngressOAMPumpBias_Type(Integer32):
    """Custom type tnIroadmCardInfoIngressOAMPumpBias based on Integer32"""
    defaultValue = -100


_TnIroadmCardInfoIngressOAMPumpBias_Type.__name__ = "Integer32"
_TnIroadmCardInfoIngressOAMPumpBias_Object = MibTableColumn
tnIroadmCardInfoIngressOAMPumpBias = _TnIroadmCardInfoIngressOAMPumpBias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 34, 1, 2),
    _TnIroadmCardInfoIngressOAMPumpBias_Type()
)
tnIroadmCardInfoIngressOAMPumpBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIroadmCardInfoIngressOAMPumpBias.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardInfoIngressOAMPumpBias.setUnits("mA")


class _TnIroadmCardInfoEgressOAMPumpTemperature_Type(Integer32):
    """Custom type tnIroadmCardInfoEgressOAMPumpTemperature based on Integer32"""
    defaultValue = 150


_TnIroadmCardInfoEgressOAMPumpTemperature_Type.__name__ = "Integer32"
_TnIroadmCardInfoEgressOAMPumpTemperature_Object = MibTableColumn
tnIroadmCardInfoEgressOAMPumpTemperature = _TnIroadmCardInfoEgressOAMPumpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 34, 1, 3),
    _TnIroadmCardInfoEgressOAMPumpTemperature_Type()
)
tnIroadmCardInfoEgressOAMPumpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIroadmCardInfoEgressOAMPumpTemperature.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardInfoEgressOAMPumpTemperature.setUnits("Celsius")


class _TnIroadmCardInfoEgressOAMPumpBias_Type(Integer32):
    """Custom type tnIroadmCardInfoEgressOAMPumpBias based on Integer32"""
    defaultValue = 30


_TnIroadmCardInfoEgressOAMPumpBias_Type.__name__ = "Integer32"
_TnIroadmCardInfoEgressOAMPumpBias_Object = MibTableColumn
tnIroadmCardInfoEgressOAMPumpBias = _TnIroadmCardInfoEgressOAMPumpBias_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 34, 1, 4),
    _TnIroadmCardInfoEgressOAMPumpBias_Type()
)
tnIroadmCardInfoEgressOAMPumpBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIroadmCardInfoEgressOAMPumpBias.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardInfoEgressOAMPumpBias.setUnits("mA")


class _TnIroadmCardInfoOptIntSpanLoss_Type(Unsigned32):
    """Custom type tnIroadmCardInfoOptIntSpanLoss based on Unsigned32"""
    defaultValue = 9900


_TnIroadmCardInfoOptIntSpanLoss_Type.__name__ = "Unsigned32"
_TnIroadmCardInfoOptIntSpanLoss_Object = MibTableColumn
tnIroadmCardInfoOptIntSpanLoss = _TnIroadmCardInfoOptIntSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 34, 1, 5),
    _TnIroadmCardInfoOptIntSpanLoss_Type()
)
tnIroadmCardInfoOptIntSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIroadmCardInfoOptIntSpanLoss.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardInfoOptIntSpanLoss.setUnits("mB")


class _TnIroadmCardInfoWssIsFlexgrid_Type(Unsigned32):
    """Custom type tnIroadmCardInfoWssIsFlexgrid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TnIroadmCardInfoWssIsFlexgrid_Type.__name__ = "Unsigned32"
_TnIroadmCardInfoWssIsFlexgrid_Object = MibTableColumn
tnIroadmCardInfoWssIsFlexgrid = _TnIroadmCardInfoWssIsFlexgrid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 34, 1, 6),
    _TnIroadmCardInfoWssIsFlexgrid_Type()
)
tnIroadmCardInfoWssIsFlexgrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIroadmCardInfoWssIsFlexgrid.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardInfoWssIsFlexgrid.setUnits("MHz")
_TnIroadmCardInfoWssGranularityMHz_Type = Integer32
_TnIroadmCardInfoWssGranularityMHz_Object = MibTableColumn
tnIroadmCardInfoWssGranularityMHz = _TnIroadmCardInfoWssGranularityMHz_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 34, 1, 7),
    _TnIroadmCardInfoWssGranularityMHz_Type()
)
tnIroadmCardInfoWssGranularityMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIroadmCardInfoWssGranularityMHz.setStatus("current")
if mibBuilder.loadTexts:
    tnIroadmCardInfoWssGranularityMHz.setUnits("MHz")
_TnIsonCardModeAttributeTotal_Type = Integer32
_TnIsonCardModeAttributeTotal_Object = MibScalar
tnIsonCardModeAttributeTotal = _TnIsonCardModeAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 35),
    _TnIsonCardModeAttributeTotal_Type()
)
tnIsonCardModeAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIsonCardModeAttributeTotal.setStatus("current")
_TnIsonCardModeTable_Object = MibTable
tnIsonCardModeTable = _TnIsonCardModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 36)
)
if mibBuilder.loadTexts:
    tnIsonCardModeTable.setStatus("current")
_TnIsonCardModeEntry_Object = MibTableRow
tnIsonCardModeEntry = _TnIsonCardModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 36, 1)
)
tnIsonCardModeEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnIsonCardModeEntry.setStatus("current")


class _TnIsonCardModeSelection_Type(Integer32):
    """Custom type tnIsonCardModeSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("straight", 1),
          ("cross", 2))
    )


_TnIsonCardModeSelection_Type.__name__ = "Integer32"
_TnIsonCardModeSelection_Object = MibTableColumn
tnIsonCardModeSelection = _TnIsonCardModeSelection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 36, 1, 1),
    _TnIsonCardModeSelection_Type()
)
tnIsonCardModeSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIsonCardModeSelection.setStatus("current")
_TnCardEtherTypeProfileAttributeTotal_Type = Integer32
_TnCardEtherTypeProfileAttributeTotal_Object = MibScalar
tnCardEtherTypeProfileAttributeTotal = _TnCardEtherTypeProfileAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 38),
    _TnCardEtherTypeProfileAttributeTotal_Type()
)
tnCardEtherTypeProfileAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCardEtherTypeProfileAttributeTotal.setStatus("current")
_TnCardEtherTypeProfileTable_Object = MibTable
tnCardEtherTypeProfileTable = _TnCardEtherTypeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 39)
)
if mibBuilder.loadTexts:
    tnCardEtherTypeProfileTable.setStatus("current")
_TnCardEtherTypeProfileEntry_Object = MibTableRow
tnCardEtherTypeProfileEntry = _TnCardEtherTypeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 39, 1)
)
tnCardEtherTypeProfileEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-OPTICALCARD-MIB", "tnCardEthertypeQinQID"),
)
if mibBuilder.loadTexts:
    tnCardEtherTypeProfileEntry.setStatus("current")


class _TnCardEthertypeQinQID_Type(Integer32):
    """Custom type tnCardEthertypeQinQID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCardEthertypeQinQID_Type.__name__ = "Integer32"
_TnCardEthertypeQinQID_Object = MibTableColumn
tnCardEthertypeQinQID = _TnCardEthertypeQinQID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 39, 1, 1),
    _TnCardEthertypeQinQID_Type()
)
tnCardEthertypeQinQID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCardEthertypeQinQID.setStatus("current")
_TnCardEthertypeQinQDesc_Type = SnmpAdminString
_TnCardEthertypeQinQDesc_Object = MibTableColumn
tnCardEthertypeQinQDesc = _TnCardEthertypeQinQDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 39, 1, 2),
    _TnCardEthertypeQinQDesc_Type()
)
tnCardEthertypeQinQDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardEthertypeQinQDesc.setStatus("current")


class _TnCardEthertypeQinQEtype_Type(Integer32):
    """Custom type tnCardEthertypeQinQEtype based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_TnCardEthertypeQinQEtype_Type.__name__ = "Integer32"
_TnCardEthertypeQinQEtype_Object = MibTableColumn
tnCardEthertypeQinQEtype = _TnCardEthertypeQinQEtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 39, 1, 3),
    _TnCardEthertypeQinQEtype_Type()
)
tnCardEthertypeQinQEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardEthertypeQinQEtype.setStatus("current")
_TnCardEthertypeQinQRowStatus_Type = RowStatus
_TnCardEthertypeQinQRowStatus_Object = MibTableColumn
tnCardEthertypeQinQRowStatus = _TnCardEthertypeQinQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 39, 1, 4),
    _TnCardEthertypeQinQRowStatus_Type()
)
tnCardEthertypeQinQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnCardEthertypeQinQRowStatus.setStatus("current")
_TnAutomationConfigAttributeTotal_Type = Integer32
_TnAutomationConfigAttributeTotal_Object = MibScalar
tnAutomationConfigAttributeTotal = _TnAutomationConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 40),
    _TnAutomationConfigAttributeTotal_Type()
)
tnAutomationConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAutomationConfigAttributeTotal.setStatus("current")
_TnAutomationConfigTable_Object = MibTable
tnAutomationConfigTable = _TnAutomationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 41)
)
if mibBuilder.loadTexts:
    tnAutomationConfigTable.setStatus("current")
_TnAutomationConfigEntry_Object = MibTableRow
tnAutomationConfigEntry = _TnAutomationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 41, 1)
)
tnAutomationConfigEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnAutomationConfigEntry.setStatus("current")


class _TnAutomationConfigAutoTopoDegreeNumber_Type(Unsigned32):
    """Custom type tnAutomationConfigAutoTopoDegreeNumber based on Unsigned32"""
    defaultValue = 0


_TnAutomationConfigAutoTopoDegreeNumber_Type.__name__ = "Unsigned32"
_TnAutomationConfigAutoTopoDegreeNumber_Object = MibTableColumn
tnAutomationConfigAutoTopoDegreeNumber = _TnAutomationConfigAutoTopoDegreeNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 41, 1, 1),
    _TnAutomationConfigAutoTopoDegreeNumber_Type()
)
tnAutomationConfigAutoTopoDegreeNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAutomationConfigAutoTopoDegreeNumber.setStatus("current")
_TnSfd5CardAttributeTotal_Type = Integer32
_TnSfd5CardAttributeTotal_Object = MibScalar
tnSfd5CardAttributeTotal = _TnSfd5CardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 44),
    _TnSfd5CardAttributeTotal_Type()
)
tnSfd5CardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardAttributeTotal.setStatus("current")
_TnSfd5CardTable_Object = MibTable
tnSfd5CardTable = _TnSfd5CardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45)
)
if mibBuilder.loadTexts:
    tnSfd5CardTable.setStatus("current")
_TnSfd5CardEntry_Object = MibTableRow
tnSfd5CardEntry = _TnSfd5CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1)
)
tnSfd5CardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSfd5CardEntry.setStatus("current")


class _TnSfd5CardPortLossCh1_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh1 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh1_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh1_Object = MibTableColumn
tnSfd5CardPortLossCh1 = _TnSfd5CardPortLossCh1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 1),
    _TnSfd5CardPortLossCh1_Type()
)
tnSfd5CardPortLossCh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh1.setStatus("current")


class _TnSfd5CardPortLossCh2_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh2 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh2_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh2_Object = MibTableColumn
tnSfd5CardPortLossCh2 = _TnSfd5CardPortLossCh2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 2),
    _TnSfd5CardPortLossCh2_Type()
)
tnSfd5CardPortLossCh2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh2.setStatus("current")


class _TnSfd5CardPortLossCh3_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh3 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh3_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh3_Object = MibTableColumn
tnSfd5CardPortLossCh3 = _TnSfd5CardPortLossCh3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 3),
    _TnSfd5CardPortLossCh3_Type()
)
tnSfd5CardPortLossCh3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh3.setStatus("current")


class _TnSfd5CardPortLossCh4_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh4 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh4_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh4_Object = MibTableColumn
tnSfd5CardPortLossCh4 = _TnSfd5CardPortLossCh4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 4),
    _TnSfd5CardPortLossCh4_Type()
)
tnSfd5CardPortLossCh4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh4.setStatus("current")


class _TnSfd5CardPortLossCh5_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh5 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh5_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh5_Object = MibTableColumn
tnSfd5CardPortLossCh5 = _TnSfd5CardPortLossCh5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 5),
    _TnSfd5CardPortLossCh5_Type()
)
tnSfd5CardPortLossCh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh5.setStatus("current")


class _TnSfd5CardPortLossCh6_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh6 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh6_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh6_Object = MibTableColumn
tnSfd5CardPortLossCh6 = _TnSfd5CardPortLossCh6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 6),
    _TnSfd5CardPortLossCh6_Type()
)
tnSfd5CardPortLossCh6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh6.setStatus("current")


class _TnSfd5CardPortLossCh7_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh7 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh7_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh7_Object = MibTableColumn
tnSfd5CardPortLossCh7 = _TnSfd5CardPortLossCh7_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 7),
    _TnSfd5CardPortLossCh7_Type()
)
tnSfd5CardPortLossCh7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh7.setStatus("current")


class _TnSfd5CardPortLossCh8_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh8 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh8_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh8_Object = MibTableColumn
tnSfd5CardPortLossCh8 = _TnSfd5CardPortLossCh8_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 8),
    _TnSfd5CardPortLossCh8_Type()
)
tnSfd5CardPortLossCh8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh8.setStatus("current")


class _TnSfd5CardPortLossCh9_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh9 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh9_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh9_Object = MibTableColumn
tnSfd5CardPortLossCh9 = _TnSfd5CardPortLossCh9_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 9),
    _TnSfd5CardPortLossCh9_Type()
)
tnSfd5CardPortLossCh9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh9.setStatus("current")


class _TnSfd5CardPortLossCh10_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossCh10 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossCh10_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossCh10_Object = MibTableColumn
tnSfd5CardPortLossCh10 = _TnSfd5CardPortLossCh10_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 10),
    _TnSfd5CardPortLossCh10_Type()
)
tnSfd5CardPortLossCh10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossCh10.setStatus("current")


class _TnSfd5CardPortLossEXP_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd5CardPortLossEXP based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd5CardPortLossEXP_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd5CardPortLossEXP_Object = MibTableColumn
tnSfd5CardPortLossEXP = _TnSfd5CardPortLossEXP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 11),
    _TnSfd5CardPortLossEXP_Type()
)
tnSfd5CardPortLossEXP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardPortLossEXP.setStatus("current")


class _TnSfd5CardAveBIUFibLen_Type(TropicSfdInvFiberLength):
    """Custom type tnSfd5CardAveBIUFibLen based on TropicSfdInvFiberLength"""
    defaultValue = OctetString("")


_TnSfd5CardAveBIUFibLen_Type.__name__ = "TropicSfdInvFiberLength"
_TnSfd5CardAveBIUFibLen_Object = MibTableColumn
tnSfd5CardAveBIUFibLen = _TnSfd5CardAveBIUFibLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 12),
    _TnSfd5CardAveBIUFibLen_Type()
)
tnSfd5CardAveBIUFibLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardAveBIUFibLen.setStatus("current")


class _TnSfd5CardAveBIDFibLen_Type(TropicSfdInvFiberLength):
    """Custom type tnSfd5CardAveBIDFibLen based on TropicSfdInvFiberLength"""
    defaultValue = OctetString("")


_TnSfd5CardAveBIDFibLen_Type.__name__ = "TropicSfdInvFiberLength"
_TnSfd5CardAveBIDFibLen_Object = MibTableColumn
tnSfd5CardAveBIDFibLen = _TnSfd5CardAveBIDFibLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 45, 1, 13),
    _TnSfd5CardAveBIDFibLen_Type()
)
tnSfd5CardAveBIDFibLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd5CardAveBIDFibLen.setStatus("current")
_TnSfd10CardAttributeTotal_Type = Integer32
_TnSfd10CardAttributeTotal_Object = MibScalar
tnSfd10CardAttributeTotal = _TnSfd10CardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 46),
    _TnSfd10CardAttributeTotal_Type()
)
tnSfd10CardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardAttributeTotal.setStatus("current")
_TnSfd10CardTable_Object = MibTable
tnSfd10CardTable = _TnSfd10CardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47)
)
if mibBuilder.loadTexts:
    tnSfd10CardTable.setStatus("current")
_TnSfd10CardEntry_Object = MibTableRow
tnSfd10CardEntry = _TnSfd10CardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1)
)
tnSfd10CardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSfd10CardEntry.setStatus("current")


class _TnSfd10CardDMuxPortLossCh1_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh1 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh1_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh1_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh1 = _TnSfd10CardDMuxPortLossCh1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 1),
    _TnSfd10CardDMuxPortLossCh1_Type()
)
tnSfd10CardDMuxPortLossCh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh1.setStatus("current")


class _TnSfd10CardDMuxPortLossCh2_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh2 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh2_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh2_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh2 = _TnSfd10CardDMuxPortLossCh2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 2),
    _TnSfd10CardDMuxPortLossCh2_Type()
)
tnSfd10CardDMuxPortLossCh2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh2.setStatus("current")


class _TnSfd10CardDMuxPortLossCh3_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh3 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh3_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh3_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh3 = _TnSfd10CardDMuxPortLossCh3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 3),
    _TnSfd10CardDMuxPortLossCh3_Type()
)
tnSfd10CardDMuxPortLossCh3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh3.setStatus("current")


class _TnSfd10CardDMuxPortLossCh4_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh4 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh4_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh4_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh4 = _TnSfd10CardDMuxPortLossCh4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 4),
    _TnSfd10CardDMuxPortLossCh4_Type()
)
tnSfd10CardDMuxPortLossCh4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh4.setStatus("current")


class _TnSfd10CardDMuxPortLossCh5_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh5 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh5_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh5_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh5 = _TnSfd10CardDMuxPortLossCh5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 5),
    _TnSfd10CardDMuxPortLossCh5_Type()
)
tnSfd10CardDMuxPortLossCh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh5.setStatus("current")


class _TnSfd10CardDMuxPortLossCh6_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh6 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh6_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh6_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh6 = _TnSfd10CardDMuxPortLossCh6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 6),
    _TnSfd10CardDMuxPortLossCh6_Type()
)
tnSfd10CardDMuxPortLossCh6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh6.setStatus("current")


class _TnSfd10CardDMuxPortLossCh7_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh7 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh7_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh7_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh7 = _TnSfd10CardDMuxPortLossCh7_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 7),
    _TnSfd10CardDMuxPortLossCh7_Type()
)
tnSfd10CardDMuxPortLossCh7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh7.setStatus("current")


class _TnSfd10CardDMuxPortLossCh8_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh8 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh8_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh8_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh8 = _TnSfd10CardDMuxPortLossCh8_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 8),
    _TnSfd10CardDMuxPortLossCh8_Type()
)
tnSfd10CardDMuxPortLossCh8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh8.setStatus("current")


class _TnSfd10CardDMuxPortLossCh9_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh9 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh9_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh9_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh9 = _TnSfd10CardDMuxPortLossCh9_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 9),
    _TnSfd10CardDMuxPortLossCh9_Type()
)
tnSfd10CardDMuxPortLossCh9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh9.setStatus("current")


class _TnSfd10CardDMuxPortLossCh10_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossCh10 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossCh10_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossCh10_Object = MibTableColumn
tnSfd10CardDMuxPortLossCh10 = _TnSfd10CardDMuxPortLossCh10_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 10),
    _TnSfd10CardDMuxPortLossCh10_Type()
)
tnSfd10CardDMuxPortLossCh10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossCh10.setStatus("current")


class _TnSfd10CardDMuxPortLossEXP_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardDMuxPortLossEXP based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardDMuxPortLossEXP_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardDMuxPortLossEXP_Object = MibTableColumn
tnSfd10CardDMuxPortLossEXP = _TnSfd10CardDMuxPortLossEXP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 11),
    _TnSfd10CardDMuxPortLossEXP_Type()
)
tnSfd10CardDMuxPortLossEXP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardDMuxPortLossEXP.setStatus("current")


class _TnSfd10CardMuxPortLossCh1_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh1 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh1_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh1_Object = MibTableColumn
tnSfd10CardMuxPortLossCh1 = _TnSfd10CardMuxPortLossCh1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 12),
    _TnSfd10CardMuxPortLossCh1_Type()
)
tnSfd10CardMuxPortLossCh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh1.setStatus("current")


class _TnSfd10CardMuxPortLossCh2_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh2 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh2_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh2_Object = MibTableColumn
tnSfd10CardMuxPortLossCh2 = _TnSfd10CardMuxPortLossCh2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 13),
    _TnSfd10CardMuxPortLossCh2_Type()
)
tnSfd10CardMuxPortLossCh2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh2.setStatus("current")


class _TnSfd10CardMuxPortLossCh3_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh3 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh3_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh3_Object = MibTableColumn
tnSfd10CardMuxPortLossCh3 = _TnSfd10CardMuxPortLossCh3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 14),
    _TnSfd10CardMuxPortLossCh3_Type()
)
tnSfd10CardMuxPortLossCh3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh3.setStatus("current")


class _TnSfd10CardMuxPortLossCh4_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh4 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh4_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh4_Object = MibTableColumn
tnSfd10CardMuxPortLossCh4 = _TnSfd10CardMuxPortLossCh4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 15),
    _TnSfd10CardMuxPortLossCh4_Type()
)
tnSfd10CardMuxPortLossCh4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh4.setStatus("current")


class _TnSfd10CardMuxPortLossCh5_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh5 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh5_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh5_Object = MibTableColumn
tnSfd10CardMuxPortLossCh5 = _TnSfd10CardMuxPortLossCh5_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 16),
    _TnSfd10CardMuxPortLossCh5_Type()
)
tnSfd10CardMuxPortLossCh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh5.setStatus("current")


class _TnSfd10CardMuxPortLossCh6_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh6 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh6_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh6_Object = MibTableColumn
tnSfd10CardMuxPortLossCh6 = _TnSfd10CardMuxPortLossCh6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 17),
    _TnSfd10CardMuxPortLossCh6_Type()
)
tnSfd10CardMuxPortLossCh6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh6.setStatus("current")


class _TnSfd10CardMuxPortLossCh7_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh7 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh7_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh7_Object = MibTableColumn
tnSfd10CardMuxPortLossCh7 = _TnSfd10CardMuxPortLossCh7_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 18),
    _TnSfd10CardMuxPortLossCh7_Type()
)
tnSfd10CardMuxPortLossCh7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh7.setStatus("current")


class _TnSfd10CardMuxPortLossCh8_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh8 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh8_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh8_Object = MibTableColumn
tnSfd10CardMuxPortLossCh8 = _TnSfd10CardMuxPortLossCh8_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 19),
    _TnSfd10CardMuxPortLossCh8_Type()
)
tnSfd10CardMuxPortLossCh8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh8.setStatus("current")


class _TnSfd10CardMuxPortLossCh9_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh9 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh9_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh9_Object = MibTableColumn
tnSfd10CardMuxPortLossCh9 = _TnSfd10CardMuxPortLossCh9_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 20),
    _TnSfd10CardMuxPortLossCh9_Type()
)
tnSfd10CardMuxPortLossCh9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh9.setStatus("current")


class _TnSfd10CardMuxPortLossCh10_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossCh10 based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossCh10_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossCh10_Object = MibTableColumn
tnSfd10CardMuxPortLossCh10 = _TnSfd10CardMuxPortLossCh10_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 21),
    _TnSfd10CardMuxPortLossCh10_Type()
)
tnSfd10CardMuxPortLossCh10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossCh10.setStatus("current")


class _TnSfd10CardMuxPortLossEXP_Type(TropicSfdInvPortLoss):
    """Custom type tnSfd10CardMuxPortLossEXP based on TropicSfdInvPortLoss"""
    defaultValue = OctetString("")


_TnSfd10CardMuxPortLossEXP_Type.__name__ = "TropicSfdInvPortLoss"
_TnSfd10CardMuxPortLossEXP_Object = MibTableColumn
tnSfd10CardMuxPortLossEXP = _TnSfd10CardMuxPortLossEXP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 22),
    _TnSfd10CardMuxPortLossEXP_Type()
)
tnSfd10CardMuxPortLossEXP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardMuxPortLossEXP.setStatus("current")


class _TnSfd10CardAveMuxFibLen_Type(TropicSfdInvFiberLength):
    """Custom type tnSfd10CardAveMuxFibLen based on TropicSfdInvFiberLength"""
    defaultValue = OctetString("")


_TnSfd10CardAveMuxFibLen_Type.__name__ = "TropicSfdInvFiberLength"
_TnSfd10CardAveMuxFibLen_Object = MibTableColumn
tnSfd10CardAveMuxFibLen = _TnSfd10CardAveMuxFibLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 23),
    _TnSfd10CardAveMuxFibLen_Type()
)
tnSfd10CardAveMuxFibLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardAveMuxFibLen.setStatus("current")


class _TnSfd10CardAveDMUXFibLen_Type(TropicSfdInvFiberLength):
    """Custom type tnSfd10CardAveDMUXFibLen based on TropicSfdInvFiberLength"""
    defaultValue = OctetString("")


_TnSfd10CardAveDMUXFibLen_Type.__name__ = "TropicSfdInvFiberLength"
_TnSfd10CardAveDMUXFibLen_Object = MibTableColumn
tnSfd10CardAveDMUXFibLen = _TnSfd10CardAveDMUXFibLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 47, 1, 24),
    _TnSfd10CardAveDMUXFibLen_Type()
)
tnSfd10CardAveDMUXFibLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSfd10CardAveDMUXFibLen.setStatus("current")
_TnDcmxCardAttributeTotal_Type = Integer32
_TnDcmxCardAttributeTotal_Object = MibScalar
tnDcmxCardAttributeTotal = _TnDcmxCardAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 48),
    _TnDcmxCardAttributeTotal_Type()
)
tnDcmxCardAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardAttributeTotal.setStatus("current")
_TnDcmxCardTable_Object = MibTable
tnDcmxCardTable = _TnDcmxCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49)
)
if mibBuilder.loadTexts:
    tnDcmxCardTable.setStatus("current")
_TnDcmxCardEntry_Object = MibTableRow
tnDcmxCardEntry = _TnDcmxCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1)
)
tnDcmxCardEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnDcmxCardEntry.setStatus("current")


class _TnDcmxCardFiberType_Type(TropicDcmInvFiberType):
    """Custom type tnDcmxCardFiberType based on TropicDcmInvFiberType"""
    defaultValue = OctetString("")


_TnDcmxCardFiberType_Type.__name__ = "TropicDcmInvFiberType"
_TnDcmxCardFiberType_Object = MibTableColumn
tnDcmxCardFiberType = _TnDcmxCardFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 1),
    _TnDcmxCardFiberType_Type()
)
tnDcmxCardFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardFiberType.setStatus("current")


class _TnDcmxCardDcmSize_Type(TropicDcmInvDcmSize):
    """Custom type tnDcmxCardDcmSize based on TropicDcmInvDcmSize"""
    defaultValue = OctetString("")


_TnDcmxCardDcmSize_Type.__name__ = "TropicDcmInvDcmSize"
_TnDcmxCardDcmSize_Object = MibTableColumn
tnDcmxCardDcmSize = _TnDcmxCardDcmSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 2),
    _TnDcmxCardDcmSize_Type()
)
tnDcmxCardDcmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardDcmSize.setStatus("current")


class _TnDcmxCardAverageInsertionLossDCF1_Type(TropicDcmInvInsertionLoss):
    """Custom type tnDcmxCardAverageInsertionLossDCF1 based on TropicDcmInvInsertionLoss"""
    defaultValue = OctetString("")


_TnDcmxCardAverageInsertionLossDCF1_Type.__name__ = "TropicDcmInvInsertionLoss"
_TnDcmxCardAverageInsertionLossDCF1_Object = MibTableColumn
tnDcmxCardAverageInsertionLossDCF1 = _TnDcmxCardAverageInsertionLossDCF1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 3),
    _TnDcmxCardAverageInsertionLossDCF1_Type()
)
tnDcmxCardAverageInsertionLossDCF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardAverageInsertionLossDCF1.setStatus("current")


class _TnDcmxCardInsertionLossSlopeDCF1_Type(TropicDcmInvInsertionLossSlope):
    """Custom type tnDcmxCardInsertionLossSlopeDCF1 based on TropicDcmInvInsertionLossSlope"""
    defaultValue = OctetString("")


_TnDcmxCardInsertionLossSlopeDCF1_Type.__name__ = "TropicDcmInvInsertionLossSlope"
_TnDcmxCardInsertionLossSlopeDCF1_Object = MibTableColumn
tnDcmxCardInsertionLossSlopeDCF1 = _TnDcmxCardInsertionLossSlopeDCF1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 4),
    _TnDcmxCardInsertionLossSlopeDCF1_Type()
)
tnDcmxCardInsertionLossSlopeDCF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardInsertionLossSlopeDCF1.setStatus("current")


class _TnDcmxCardTotalDispFitDCF1_Type(TropicDcmInvDispersionFit):
    """Custom type tnDcmxCardTotalDispFitDCF1 based on TropicDcmInvDispersionFit"""
    defaultValue = OctetString("")


_TnDcmxCardTotalDispFitDCF1_Type.__name__ = "TropicDcmInvDispersionFit"
_TnDcmxCardTotalDispFitDCF1_Object = MibTableColumn
tnDcmxCardTotalDispFitDCF1 = _TnDcmxCardTotalDispFitDCF1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 5),
    _TnDcmxCardTotalDispFitDCF1_Type()
)
tnDcmxCardTotalDispFitDCF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardTotalDispFitDCF1.setStatus("current")


class _TnDcmxCardDispFiberLengthDCF1_Type(TropicDcmInvFiberLength):
    """Custom type tnDcmxCardDispFiberLengthDCF1 based on TropicDcmInvFiberLength"""
    defaultValue = OctetString("")


_TnDcmxCardDispFiberLengthDCF1_Type.__name__ = "TropicDcmInvFiberLength"
_TnDcmxCardDispFiberLengthDCF1_Object = MibTableColumn
tnDcmxCardDispFiberLengthDCF1 = _TnDcmxCardDispFiberLengthDCF1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 6),
    _TnDcmxCardDispFiberLengthDCF1_Type()
)
tnDcmxCardDispFiberLengthDCF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardDispFiberLengthDCF1.setStatus("current")


class _TnDcmxCardPMDDCF1_Type(TropicDcmInvPmd):
    """Custom type tnDcmxCardPMDDCF1 based on TropicDcmInvPmd"""
    defaultValue = OctetString("")


_TnDcmxCardPMDDCF1_Type.__name__ = "TropicDcmInvPmd"
_TnDcmxCardPMDDCF1_Object = MibTableColumn
tnDcmxCardPMDDCF1 = _TnDcmxCardPMDDCF1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 7),
    _TnDcmxCardPMDDCF1_Type()
)
tnDcmxCardPMDDCF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardPMDDCF1.setStatus("current")


class _TnDcmxCardAverageInsertionLossDCF2_Type(TropicDcmInvInsertionLoss):
    """Custom type tnDcmxCardAverageInsertionLossDCF2 based on TropicDcmInvInsertionLoss"""
    defaultValue = OctetString("")


_TnDcmxCardAverageInsertionLossDCF2_Type.__name__ = "TropicDcmInvInsertionLoss"
_TnDcmxCardAverageInsertionLossDCF2_Object = MibTableColumn
tnDcmxCardAverageInsertionLossDCF2 = _TnDcmxCardAverageInsertionLossDCF2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 8),
    _TnDcmxCardAverageInsertionLossDCF2_Type()
)
tnDcmxCardAverageInsertionLossDCF2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardAverageInsertionLossDCF2.setStatus("current")


class _TnDcmxCardInsertionLossSlopeDCF2_Type(TropicDcmInvInsertionLossSlope):
    """Custom type tnDcmxCardInsertionLossSlopeDCF2 based on TropicDcmInvInsertionLossSlope"""
    defaultValue = OctetString("")


_TnDcmxCardInsertionLossSlopeDCF2_Type.__name__ = "TropicDcmInvInsertionLossSlope"
_TnDcmxCardInsertionLossSlopeDCF2_Object = MibTableColumn
tnDcmxCardInsertionLossSlopeDCF2 = _TnDcmxCardInsertionLossSlopeDCF2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 9),
    _TnDcmxCardInsertionLossSlopeDCF2_Type()
)
tnDcmxCardInsertionLossSlopeDCF2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardInsertionLossSlopeDCF2.setStatus("current")


class _TnDcmxCardTotalDispFitDCF2_Type(TropicDcmInvDispersionFit):
    """Custom type tnDcmxCardTotalDispFitDCF2 based on TropicDcmInvDispersionFit"""
    defaultValue = OctetString("")


_TnDcmxCardTotalDispFitDCF2_Type.__name__ = "TropicDcmInvDispersionFit"
_TnDcmxCardTotalDispFitDCF2_Object = MibTableColumn
tnDcmxCardTotalDispFitDCF2 = _TnDcmxCardTotalDispFitDCF2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 10),
    _TnDcmxCardTotalDispFitDCF2_Type()
)
tnDcmxCardTotalDispFitDCF2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardTotalDispFitDCF2.setStatus("current")


class _TnDcmxCardDispFiberLengthDCF2_Type(TropicDcmInvFiberLength):
    """Custom type tnDcmxCardDispFiberLengthDCF2 based on TropicDcmInvFiberLength"""
    defaultValue = OctetString("")


_TnDcmxCardDispFiberLengthDCF2_Type.__name__ = "TropicDcmInvFiberLength"
_TnDcmxCardDispFiberLengthDCF2_Object = MibTableColumn
tnDcmxCardDispFiberLengthDCF2 = _TnDcmxCardDispFiberLengthDCF2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 11),
    _TnDcmxCardDispFiberLengthDCF2_Type()
)
tnDcmxCardDispFiberLengthDCF2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardDispFiberLengthDCF2.setStatus("current")


class _TnDcmxCardPMDDCF2_Type(TropicDcmInvPmd):
    """Custom type tnDcmxCardPMDDCF2 based on TropicDcmInvPmd"""
    defaultValue = OctetString("")


_TnDcmxCardPMDDCF2_Type.__name__ = "TropicDcmInvPmd"
_TnDcmxCardPMDDCF2_Object = MibTableColumn
tnDcmxCardPMDDCF2 = _TnDcmxCardPMDDCF2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 12),
    _TnDcmxCardPMDDCF2_Type()
)
tnDcmxCardPMDDCF2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardPMDDCF2.setStatus("current")


class _TnDcmxCardLatencyMismatch_Type(TropicDcmInvLatencyMismatch):
    """Custom type tnDcmxCardLatencyMismatch based on TropicDcmInvLatencyMismatch"""
    defaultValue = OctetString("")


_TnDcmxCardLatencyMismatch_Type.__name__ = "TropicDcmInvLatencyMismatch"
_TnDcmxCardLatencyMismatch_Object = MibTableColumn
tnDcmxCardLatencyMismatch = _TnDcmxCardLatencyMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 13),
    _TnDcmxCardLatencyMismatch_Type()
)
tnDcmxCardLatencyMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardLatencyMismatch.setStatus("current")


class _TnDcmxCardLatency_Type(TropicDcmInvLatency):
    """Custom type tnDcmxCardLatency based on TropicDcmInvLatency"""
    defaultValue = OctetString("")


_TnDcmxCardLatency_Type.__name__ = "TropicDcmInvLatency"
_TnDcmxCardLatency_Object = MibTableColumn
tnDcmxCardLatency = _TnDcmxCardLatency_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 2, 49, 1, 14),
    _TnDcmxCardLatency_Type()
)
tnDcmxCardLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDcmxCardLatency.setStatus("current")

# Managed Objects groups

tnOpticalCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 1)
)
tnOpticalCardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnOpticalCardTotal")
)
if mibBuilder.loadTexts:
    tnOpticalCardScalarsGroup.setStatus("current")

tnDcmCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 4)
)
tnDcmCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnDcmCardProgrammedCompensationDistance"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardPresentCompensationDistance"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardSize"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardFiberType"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardAverageInsertionLoss"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardInsertionLossSlope"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardAverageInsertionLossPad"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardInsertionLossSlopePad"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardTotalDispTilt"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardDispFiberLength"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardPMD"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardProvisionedFiberType"))
)
if mibBuilder.loadTexts:
    tnDcmCardGroup.setStatus("current")

tnPowerControlCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 8)
)
tnPowerControlCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnPowerControlCardCapabilityProgrammed"),
        ("TROPIC-OPTICALCARD-MIB", "tnPowerControlCardCapabilityPresent"),
        ("TROPIC-OPTICALCARD-MIB", "tnPowerControlCardCapabilityInUse"))
)
if mibBuilder.loadTexts:
    tnPowerControlCardGroup.setStatus("current")

tnWssCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 9)
)
tnWssCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnWssCardAddPathTargetPower"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardAddPathEgressPower"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardAddPathTotalChannel"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardReservedDegree"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardLnsEnable"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardLnsPower"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardAdBlockLevelAdd"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardAdBlockLevelDrop"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardIsFlexgrid"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardGranularityMHz"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardEnableFilterlessDge"))
)
if mibBuilder.loadTexts:
    tnWssCardGroup.setStatus("current")

tnSfdCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 10)
)
tnSfdCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnSfdCardAverageMuxInsertionLoss"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfdCardAverageDemuxInsertionLoss"))
)
if mibBuilder.loadTexts:
    tnSfdCardGroup.setStatus("current")

tnSonetSdhPpSectionCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 11)
)
tnSonetSdhPpSectionCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection1Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection2Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection3Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection4Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection5Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection6Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection7Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection8Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection1IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection2IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection3IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection4IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection5IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection6IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection7IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSection8IfType"))
)
if mibBuilder.loadTexts:
    tnSonetSdhPpSectionCardGroup.setStatus("current")

tnPcsSectionCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 12)
)
tnPcsSectionCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnPcsSection1Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection2Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection3Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection4Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection5Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection6Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection7Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection8Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection9Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection10Port"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection1IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection2IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection3IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection4IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection5IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection6IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection7IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection8IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection9IfType"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSection10IfType"))
)
if mibBuilder.loadTexts:
    tnPcsSectionCardGroup.setStatus("current")

tn11dpge12CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 14)
)
tn11dpge12CardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn11dpge12CardRateMode"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpge12QINQModeTPID"))
)
if mibBuilder.loadTexts:
    tn11dpge12CardGroup.setStatus("current")

tnSfcCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 15)
)
tnSfcCardGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnSfcCardFiberMode")
)
if mibBuilder.loadTexts:
    tnSfcCardGroup.setStatus("current")

tn11dpe12eCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 18)
)
tn11dpe12eCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn11dpe12eCardRateMode"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeTPID1"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeTPID2"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeTPID3"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeTPID4"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eQINQModeFlowCm"))
)
if mibBuilder.loadTexts:
    tn11dpe12eCardGroup.setStatus("current")

tn1dpp24mCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 19)
)
tn1dpp24mCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn1dpp24mCardFunctionMode"),
        ("TROPIC-OPTICALCARD-MIB", "tn1dpp24mCardImpedance"))
)
if mibBuilder.loadTexts:
    tn1dpp24mCardGroup.setStatus("current")

tnOpsCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 21)
)
tnOpsCardGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnOpsCardProtectionMode")
)
if mibBuilder.loadTexts:
    tnOpsCardGroup.setStatus("current")

tn11dpe12aCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 22)
)
tn11dpe12aCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardRateMode"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardQINQModeTPID1"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardQINQModeTPID2"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardQINQModeTPID3"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardQINQModeTPID4"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardLBMInterval"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardLBRTimeout"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardFlowCm"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardSLRTimeout"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardCrossPackServiceSupported"))
)
if mibBuilder.loadTexts:
    tn11dpe12aCardGroup.setStatus("current")

tnCardFunctionModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 23)
)
tnCardFunctionModeGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnCardFunctionMode")
)
if mibBuilder.loadTexts:
    tnCardFunctionModeGroup.setStatus("current")

tn112pdm11CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 24)
)
tn112pdm11CardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tn112pdm11CardMaxDMNumbers"),
        ("TROPIC-OPTICALCARD-MIB", "tn112pdm11CardUsedDMNumbers"))
)
if mibBuilder.loadTexts:
    tn112pdm11CardGroup.setStatus("current")

tnPtpctlCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 25)
)
tnPtpctlCardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPtpctlCardScalarsGroup.setStatus("current")

tnPtpctlCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 26)
)
tnPtpctlCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardEqpsLEDColor"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardEqpsLEDState"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardPtpLEDColor"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardPtpLEDState"))
)
if mibBuilder.loadTexts:
    tnPtpctlCardGroup.setStatus("current")

tnWtocmaCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 27)
)
tnWtocmaCardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnWtocmaCardScalarsGroup.setStatus("current")

tnWtocmaCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 28)
)
tnWtocmaCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardOsnrScan"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardOsnrScanAbort"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardOsnrScanStatus"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardDspState"))
)
if mibBuilder.loadTexts:
    tnWtocmaCardGroup.setStatus("current")

tnCruCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 29)
)
tnCruCardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnCruCardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnCruCardScalarsGroup.setStatus("current")

tnCruCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 30)
)
tnCruCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnCruCardActivityState"),
        ("TROPIC-OPTICALCARD-MIB", "tnCruCardEqpsLEDColor"),
        ("TROPIC-OPTICALCARD-MIB", "tnCruCardEqpsLEDState"),
        ("TROPIC-OPTICALCARD-MIB", "tnFCruProtectionRole"))
)
if mibBuilder.loadTexts:
    tnCruCardGroup.setStatus("current")

tnIroadmCardConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 31)
)
tnIroadmCardConfigScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnIroadmCardConfigScalarsGroup.setStatus("current")

tnIroadmCardConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 32)
)
tnIroadmCardConfigGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnIroadmCardConfigOptIntDetection"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardConfigOptIntBaseline"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardConfigOptIntLossThreshold"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardConfigOptIntPollPeriod"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardConfigOptIntClearAlarm"))
)
if mibBuilder.loadTexts:
    tnIroadmCardConfigGroup.setStatus("current")

tnIroadmCardInfoScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 33)
)
tnIroadmCardInfoScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoAttributeTotal")
)
if mibBuilder.loadTexts:
    tnIroadmCardInfoScalarsGroup.setStatus("current")

tnIroadmCardInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 34)
)
tnIroadmCardInfoGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoIngressOAMPumpTemperature"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoIngressOAMPumpBias"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoEgressOAMPumpTemperature"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoEgressOAMPumpBias"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoOptIntSpanLoss"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoWssIsFlexgrid"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoWssGranularityMHz"))
)
if mibBuilder.loadTexts:
    tnIroadmCardInfoGroup.setStatus("current")

tnIsonCardModeScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 35)
)
tnIsonCardModeScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnIsonCardModeAttributeTotal")
)
if mibBuilder.loadTexts:
    tnIsonCardModeScalarsGroup.setStatus("current")

tnIsonCardModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 36)
)
tnIsonCardModeGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnIsonCardModeSelection")
)
if mibBuilder.loadTexts:
    tnIsonCardModeGroup.setStatus("current")

tnCardEtherTypeProfileScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 38)
)
tnCardEtherTypeProfileScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnCardEtherTypeProfileAttributeTotal")
)
if mibBuilder.loadTexts:
    tnCardEtherTypeProfileScalarsGroup.setStatus("current")

tnCardEtherTypeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 39)
)
tnCardEtherTypeProfileGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnCardEthertypeQinQDesc"),
        ("TROPIC-OPTICALCARD-MIB", "tnCardEthertypeQinQEtype"),
        ("TROPIC-OPTICALCARD-MIB", "tnCardEthertypeQinQRowStatus"))
)
if mibBuilder.loadTexts:
    tnCardEtherTypeProfileGroup.setStatus("current")

tnAutomationConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 40)
)
tnAutomationConfigScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnAutomationConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAutomationConfigScalarsGroup.setStatus("current")

tnAutomationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 41)
)
tnAutomationConfigGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnAutomationConfigAutoTopoDegreeNumber")
)
if mibBuilder.loadTexts:
    tnAutomationConfigGroup.setStatus("current")

tnSfd5CardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 44)
)
tnSfd5CardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSfd5CardScalarsGroup.setStatus("current")

tnSfd5CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 45)
)
tnSfd5CardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh1"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh2"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh3"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh4"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh5"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh6"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh7"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh8"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh9"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossCh10"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardPortLossEXP"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardAveBIUFibLen"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardAveBIDFibLen"))
)
if mibBuilder.loadTexts:
    tnSfd5CardGroup.setStatus("current")

tnSfd10CardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 46)
)
tnSfd10CardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnSfd10CardScalarsGroup.setStatus("current")

tnSfd10CardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 47)
)
tnSfd10CardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh1"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh2"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh3"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh4"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh5"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh6"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh7"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh8"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh9"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossCh10"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardDMuxPortLossEXP"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh1"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh2"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh3"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh4"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh5"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh6"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh7"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh8"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh9"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossCh10"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardMuxPortLossEXP"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardAveMuxFibLen"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardAveDMUXFibLen"))
)
if mibBuilder.loadTexts:
    tnSfd10CardGroup.setStatus("current")

tnDcmxCardScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 48)
)
tnDcmxCardScalarsGroup.setObjects(
    ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardAttributeTotal")
)
if mibBuilder.loadTexts:
    tnDcmxCardScalarsGroup.setStatus("current")

tnDcmxCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 1, 49)
)
tnDcmxCardGroup.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnDcmxCardFiberType"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardDcmSize"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardAverageInsertionLossDCF1"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardInsertionLossSlopeDCF1"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardTotalDispFitDCF1"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardDispFiberLengthDCF1"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardPMDDCF1"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardAverageInsertionLossDCF2"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardInsertionLossSlopeDCF2"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardTotalDispFitDCF2"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardDispFiberLengthDCF2"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardPMDDCF2"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardLatencyMismatch"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardLatency"))
)
if mibBuilder.loadTexts:
    tnDcmxCardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnOpticalCardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 3, 5, 1, 2, 1)
)
tnOpticalCardCompliance.setObjects(
      *(("TROPIC-OPTICALCARD-MIB", "tnOpticalCardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnPowerControlCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnWssCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfdCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSonetSdhPpSectionCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnPcsSectionCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpge12CardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfcCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12eCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn1dpp24mCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnOpsCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn11dpe12aCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnCardFunctionModeGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tn112pdm11CardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnPtpctlCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnWtocmaCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnCruCardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnCruCardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardConfigScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardConfigGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnIroadmCardInfoGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnIsonCardModeScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnIsonCardModeGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnCardEtherTypeProfileScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnCardEtherTypeProfileGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnAutomationConfigScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnAutomationConfigGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd5CardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnSfd10CardGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardScalarsGroup"),
        ("TROPIC-OPTICALCARD-MIB", "tnDcmxCardGroup"))
)
if mibBuilder.loadTexts:
    tnOpticalCardCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-OPTICALCARD-MIB",
    **{"AluWdmSonetSdhPpSectionIfType": AluWdmSonetSdhPpSectionIfType,
       "AluWdmPcsSectionIfType": AluWdmPcsSectionIfType,
       "TropicSfdInvPortLoss": TropicSfdInvPortLoss,
       "TropicSfdInvFiberLength": TropicSfdInvFiberLength,
       "TropicDcmInvFiberType": TropicDcmInvFiberType,
       "TropicDcmInvDcmSize": TropicDcmInvDcmSize,
       "TropicDcmInvInsertionLoss": TropicDcmInvInsertionLoss,
       "TropicDcmInvInsertionLossSlope": TropicDcmInvInsertionLossSlope,
       "TropicDcmInvDispersionFit": TropicDcmInvDispersionFit,
       "TropicDcmInvFiberLength": TropicDcmInvFiberLength,
       "TropicDcmInvPmd": TropicDcmInvPmd,
       "TropicDcmInvLatencyMismatch": TropicDcmInvLatencyMismatch,
       "TropicDcmInvLatency": TropicDcmInvLatency,
       "tnOpticalCardMibModule": tnOpticalCardMibModule,
       "tnOpticalCardConf": tnOpticalCardConf,
       "tnOpticalCardGroups": tnOpticalCardGroups,
       "tnOpticalCardScalarsGroup": tnOpticalCardScalarsGroup,
       "tnDcmCardGroup": tnDcmCardGroup,
       "tnPowerControlCardGroup": tnPowerControlCardGroup,
       "tnWssCardGroup": tnWssCardGroup,
       "tnSfdCardGroup": tnSfdCardGroup,
       "tnSonetSdhPpSectionCardGroup": tnSonetSdhPpSectionCardGroup,
       "tnPcsSectionCardGroup": tnPcsSectionCardGroup,
       "tn11dpge12CardGroup": tn11dpge12CardGroup,
       "tnSfcCardGroup": tnSfcCardGroup,
       "tn11dpe12eCardGroup": tn11dpe12eCardGroup,
       "tn1dpp24mCardGroup": tn1dpp24mCardGroup,
       "tnOpsCardGroup": tnOpsCardGroup,
       "tn11dpe12aCardGroup": tn11dpe12aCardGroup,
       "tnCardFunctionModeGroup": tnCardFunctionModeGroup,
       "tn112pdm11CardGroup": tn112pdm11CardGroup,
       "tnPtpctlCardScalarsGroup": tnPtpctlCardScalarsGroup,
       "tnPtpctlCardGroup": tnPtpctlCardGroup,
       "tnWtocmaCardScalarsGroup": tnWtocmaCardScalarsGroup,
       "tnWtocmaCardGroup": tnWtocmaCardGroup,
       "tnCruCardScalarsGroup": tnCruCardScalarsGroup,
       "tnCruCardGroup": tnCruCardGroup,
       "tnIroadmCardConfigScalarsGroup": tnIroadmCardConfigScalarsGroup,
       "tnIroadmCardConfigGroup": tnIroadmCardConfigGroup,
       "tnIroadmCardInfoScalarsGroup": tnIroadmCardInfoScalarsGroup,
       "tnIroadmCardInfoGroup": tnIroadmCardInfoGroup,
       "tnIsonCardModeScalarsGroup": tnIsonCardModeScalarsGroup,
       "tnIsonCardModeGroup": tnIsonCardModeGroup,
       "tnCardEtherTypeProfileScalarsGroup": tnCardEtherTypeProfileScalarsGroup,
       "tnCardEtherTypeProfileGroup": tnCardEtherTypeProfileGroup,
       "tnAutomationConfigScalarsGroup": tnAutomationConfigScalarsGroup,
       "tnAutomationConfigGroup": tnAutomationConfigGroup,
       "tnSfd5CardScalarsGroup": tnSfd5CardScalarsGroup,
       "tnSfd5CardGroup": tnSfd5CardGroup,
       "tnSfd10CardScalarsGroup": tnSfd10CardScalarsGroup,
       "tnSfd10CardGroup": tnSfd10CardGroup,
       "tnDcmxCardScalarsGroup": tnDcmxCardScalarsGroup,
       "tnDcmxCardGroup": tnDcmxCardGroup,
       "tnOpticalCardCompliances": tnOpticalCardCompliances,
       "tnOpticalCardCompliance": tnOpticalCardCompliance,
       "tnOpticalCardObjs": tnOpticalCardObjs,
       "tnOpticalCardTotal": tnOpticalCardTotal,
       "tnDcmCardTable": tnDcmCardTable,
       "tnDcmCardEntry": tnDcmCardEntry,
       "tnDcmCardProgrammedCompensationDistance": tnDcmCardProgrammedCompensationDistance,
       "tnDcmCardPresentCompensationDistance": tnDcmCardPresentCompensationDistance,
       "tnDcmCardSize": tnDcmCardSize,
       "tnDcmCardFiberType": tnDcmCardFiberType,
       "tnDcmCardAverageInsertionLoss": tnDcmCardAverageInsertionLoss,
       "tnDcmCardInsertionLossSlope": tnDcmCardInsertionLossSlope,
       "tnDcmCardAverageInsertionLossPad": tnDcmCardAverageInsertionLossPad,
       "tnDcmCardInsertionLossSlopePad": tnDcmCardInsertionLossSlopePad,
       "tnDcmCardTotalDispTilt": tnDcmCardTotalDispTilt,
       "tnDcmCardDispFiberLength": tnDcmCardDispFiberLength,
       "tnDcmCardPMD": tnDcmCardPMD,
       "tnDcmCardProvisionedFiberType": tnDcmCardProvisionedFiberType,
       "tnPowerControlCardTable": tnPowerControlCardTable,
       "tnPowerControlCardEntry": tnPowerControlCardEntry,
       "tnPowerControlCardCapabilityProgrammed": tnPowerControlCardCapabilityProgrammed,
       "tnPowerControlCardCapabilityPresent": tnPowerControlCardCapabilityPresent,
       "tnPowerControlCardCapabilityInUse": tnPowerControlCardCapabilityInUse,
       "tnWssCardTable": tnWssCardTable,
       "tnWssCardEntry": tnWssCardEntry,
       "tnWssCardAddPathTargetPower": tnWssCardAddPathTargetPower,
       "tnWssCardAddPathEgressPower": tnWssCardAddPathEgressPower,
       "tnWssCardAddPathTotalChannel": tnWssCardAddPathTotalChannel,
       "tnWssCardReservedDegree": tnWssCardReservedDegree,
       "tnWssCardLnsEnable": tnWssCardLnsEnable,
       "tnWssCardLnsPower": tnWssCardLnsPower,
       "tnWssCardAdBlockLevelAdd": tnWssCardAdBlockLevelAdd,
       "tnWssCardAdBlockLevelDrop": tnWssCardAdBlockLevelDrop,
       "tnWssCardIsFlexgrid": tnWssCardIsFlexgrid,
       "tnWssCardGranularityMHz": tnWssCardGranularityMHz,
       "tnWssCardEnableFilterlessDge": tnWssCardEnableFilterlessDge,
       "tnSfdCardTable": tnSfdCardTable,
       "tnSfdCardEntry": tnSfdCardEntry,
       "tnSfdCardAverageMuxInsertionLoss": tnSfdCardAverageMuxInsertionLoss,
       "tnSfdCardAverageDemuxInsertionLoss": tnSfdCardAverageDemuxInsertionLoss,
       "tnSonetSdhPpSectionCardTable": tnSonetSdhPpSectionCardTable,
       "tnSonetSdhPpSectionCardEntry": tnSonetSdhPpSectionCardEntry,
       "tnSonetSdhPpSection1Port": tnSonetSdhPpSection1Port,
       "tnSonetSdhPpSection2Port": tnSonetSdhPpSection2Port,
       "tnSonetSdhPpSection3Port": tnSonetSdhPpSection3Port,
       "tnSonetSdhPpSection4Port": tnSonetSdhPpSection4Port,
       "tnSonetSdhPpSection5Port": tnSonetSdhPpSection5Port,
       "tnSonetSdhPpSection6Port": tnSonetSdhPpSection6Port,
       "tnSonetSdhPpSection7Port": tnSonetSdhPpSection7Port,
       "tnSonetSdhPpSection8Port": tnSonetSdhPpSection8Port,
       "tnSonetSdhPpSection1IfType": tnSonetSdhPpSection1IfType,
       "tnSonetSdhPpSection2IfType": tnSonetSdhPpSection2IfType,
       "tnSonetSdhPpSection3IfType": tnSonetSdhPpSection3IfType,
       "tnSonetSdhPpSection4IfType": tnSonetSdhPpSection4IfType,
       "tnSonetSdhPpSection5IfType": tnSonetSdhPpSection5IfType,
       "tnSonetSdhPpSection6IfType": tnSonetSdhPpSection6IfType,
       "tnSonetSdhPpSection7IfType": tnSonetSdhPpSection7IfType,
       "tnSonetSdhPpSection8IfType": tnSonetSdhPpSection8IfType,
       "tnPcsSectionCardTable": tnPcsSectionCardTable,
       "tnPcsSectionCardEntry": tnPcsSectionCardEntry,
       "tnPcsSection1Port": tnPcsSection1Port,
       "tnPcsSection2Port": tnPcsSection2Port,
       "tnPcsSection3Port": tnPcsSection3Port,
       "tnPcsSection4Port": tnPcsSection4Port,
       "tnPcsSection5Port": tnPcsSection5Port,
       "tnPcsSection6Port": tnPcsSection6Port,
       "tnPcsSection7Port": tnPcsSection7Port,
       "tnPcsSection8Port": tnPcsSection8Port,
       "tnPcsSection9Port": tnPcsSection9Port,
       "tnPcsSection10Port": tnPcsSection10Port,
       "tnPcsSection1IfType": tnPcsSection1IfType,
       "tnPcsSection2IfType": tnPcsSection2IfType,
       "tnPcsSection3IfType": tnPcsSection3IfType,
       "tnPcsSection4IfType": tnPcsSection4IfType,
       "tnPcsSection5IfType": tnPcsSection5IfType,
       "tnPcsSection6IfType": tnPcsSection6IfType,
       "tnPcsSection7IfType": tnPcsSection7IfType,
       "tnPcsSection8IfType": tnPcsSection8IfType,
       "tnPcsSection9IfType": tnPcsSection9IfType,
       "tnPcsSection10IfType": tnPcsSection10IfType,
       "tn11dpge12CardTable": tn11dpge12CardTable,
       "tn11dpge12CardEntry": tn11dpge12CardEntry,
       "tn11dpge12CardRateMode": tn11dpge12CardRateMode,
       "tn11dpge12QINQModeTPID": tn11dpge12QINQModeTPID,
       "tnSfcCardTable": tnSfcCardTable,
       "tnSfcCardEntry": tnSfcCardEntry,
       "tnSfcCardFiberMode": tnSfcCardFiberMode,
       "tn11dpe12eCardTable": tn11dpe12eCardTable,
       "tn11dpe12eCardEntry": tn11dpe12eCardEntry,
       "tn11dpe12eCardRateMode": tn11dpe12eCardRateMode,
       "tn11dpe12eQINQModeTPID1": tn11dpe12eQINQModeTPID1,
       "tn11dpe12eQINQModeTPID2": tn11dpe12eQINQModeTPID2,
       "tn11dpe12eQINQModeTPID3": tn11dpe12eQINQModeTPID3,
       "tn11dpe12eQINQModeTPID4": tn11dpe12eQINQModeTPID4,
       "tn11dpe12eQINQModeFlowCm": tn11dpe12eQINQModeFlowCm,
       "tn1dpp24mCardTable": tn1dpp24mCardTable,
       "tn1dpp24mCardEntry": tn1dpp24mCardEntry,
       "tn1dpp24mCardFunctionMode": tn1dpp24mCardFunctionMode,
       "tn1dpp24mCardImpedance": tn1dpp24mCardImpedance,
       "tnOpsCardTable": tnOpsCardTable,
       "tnOpsCardEntry": tnOpsCardEntry,
       "tnOpsCardProtectionMode": tnOpsCardProtectionMode,
       "tn11dpe12aCardTable": tn11dpe12aCardTable,
       "tn11dpe12aCardEntry": tn11dpe12aCardEntry,
       "tn11dpe12aCardRateMode": tn11dpe12aCardRateMode,
       "tn11dpe12aCardQINQModeTPID1": tn11dpe12aCardQINQModeTPID1,
       "tn11dpe12aCardQINQModeTPID2": tn11dpe12aCardQINQModeTPID2,
       "tn11dpe12aCardQINQModeTPID3": tn11dpe12aCardQINQModeTPID3,
       "tn11dpe12aCardQINQModeTPID4": tn11dpe12aCardQINQModeTPID4,
       "tn11dpe12aCardLBMInterval": tn11dpe12aCardLBMInterval,
       "tn11dpe12aCardLBRTimeout": tn11dpe12aCardLBRTimeout,
       "tn11dpe12aCardFlowCm": tn11dpe12aCardFlowCm,
       "tn11dpe12aCardSLRTimeout": tn11dpe12aCardSLRTimeout,
       "tn11dpe12aCardCrossPackServiceSupported": tn11dpe12aCardCrossPackServiceSupported,
       "tnCardFunctionModeTable": tnCardFunctionModeTable,
       "tnCardFunctionModeEntry": tnCardFunctionModeEntry,
       "tnCardFunctionMode": tnCardFunctionMode,
       "tn112pdm11CardTable": tn112pdm11CardTable,
       "tn112pdm11CardEntry": tn112pdm11CardEntry,
       "tn112pdm11CardMaxDMNumbers": tn112pdm11CardMaxDMNumbers,
       "tn112pdm11CardUsedDMNumbers": tn112pdm11CardUsedDMNumbers,
       "tnPtpctlCardAttributeTotal": tnPtpctlCardAttributeTotal,
       "tnPtpctlCardTable": tnPtpctlCardTable,
       "tnPtpctlCardEntry": tnPtpctlCardEntry,
       "tnPtpctlCardEqpsLEDColor": tnPtpctlCardEqpsLEDColor,
       "tnPtpctlCardEqpsLEDState": tnPtpctlCardEqpsLEDState,
       "tnPtpctlCardPtpLEDColor": tnPtpctlCardPtpLEDColor,
       "tnPtpctlCardPtpLEDState": tnPtpctlCardPtpLEDState,
       "tnWtocmaCardAttributeTotal": tnWtocmaCardAttributeTotal,
       "tnWtocmaCardTable": tnWtocmaCardTable,
       "tnWtocmaCardEntry": tnWtocmaCardEntry,
       "tnWtocmaCardOsnrScan": tnWtocmaCardOsnrScan,
       "tnWtocmaCardOsnrScanAbort": tnWtocmaCardOsnrScanAbort,
       "tnWtocmaCardOsnrScanStatus": tnWtocmaCardOsnrScanStatus,
       "tnWtocmaCardDspState": tnWtocmaCardDspState,
       "tnCruCardAttributeTotal": tnCruCardAttributeTotal,
       "tnCruCardTable": tnCruCardTable,
       "tnCruCardEntry": tnCruCardEntry,
       "tnCruCardActivityState": tnCruCardActivityState,
       "tnCruCardEqpsLEDColor": tnCruCardEqpsLEDColor,
       "tnCruCardEqpsLEDState": tnCruCardEqpsLEDState,
       "tnFCruProtectionRole": tnFCruProtectionRole,
       "tnIroadmCardConfigAttributeTotal": tnIroadmCardConfigAttributeTotal,
       "tnIroadmCardConfigTable": tnIroadmCardConfigTable,
       "tnIroadmCardConfigEntry": tnIroadmCardConfigEntry,
       "tnIroadmCardConfigOptIntDetection": tnIroadmCardConfigOptIntDetection,
       "tnIroadmCardConfigOptIntBaseline": tnIroadmCardConfigOptIntBaseline,
       "tnIroadmCardConfigOptIntLossThreshold": tnIroadmCardConfigOptIntLossThreshold,
       "tnIroadmCardConfigOptIntPollPeriod": tnIroadmCardConfigOptIntPollPeriod,
       "tnIroadmCardConfigOptIntClearAlarm": tnIroadmCardConfigOptIntClearAlarm,
       "tnIroadmCardInfoAttributeTotal": tnIroadmCardInfoAttributeTotal,
       "tnIroadmCardInfoTable": tnIroadmCardInfoTable,
       "tnIroadmCardInfoEntry": tnIroadmCardInfoEntry,
       "tnIroadmCardInfoIngressOAMPumpTemperature": tnIroadmCardInfoIngressOAMPumpTemperature,
       "tnIroadmCardInfoIngressOAMPumpBias": tnIroadmCardInfoIngressOAMPumpBias,
       "tnIroadmCardInfoEgressOAMPumpTemperature": tnIroadmCardInfoEgressOAMPumpTemperature,
       "tnIroadmCardInfoEgressOAMPumpBias": tnIroadmCardInfoEgressOAMPumpBias,
       "tnIroadmCardInfoOptIntSpanLoss": tnIroadmCardInfoOptIntSpanLoss,
       "tnIroadmCardInfoWssIsFlexgrid": tnIroadmCardInfoWssIsFlexgrid,
       "tnIroadmCardInfoWssGranularityMHz": tnIroadmCardInfoWssGranularityMHz,
       "tnIsonCardModeAttributeTotal": tnIsonCardModeAttributeTotal,
       "tnIsonCardModeTable": tnIsonCardModeTable,
       "tnIsonCardModeEntry": tnIsonCardModeEntry,
       "tnIsonCardModeSelection": tnIsonCardModeSelection,
       "tnCardEtherTypeProfileAttributeTotal": tnCardEtherTypeProfileAttributeTotal,
       "tnCardEtherTypeProfileTable": tnCardEtherTypeProfileTable,
       "tnCardEtherTypeProfileEntry": tnCardEtherTypeProfileEntry,
       "tnCardEthertypeQinQID": tnCardEthertypeQinQID,
       "tnCardEthertypeQinQDesc": tnCardEthertypeQinQDesc,
       "tnCardEthertypeQinQEtype": tnCardEthertypeQinQEtype,
       "tnCardEthertypeQinQRowStatus": tnCardEthertypeQinQRowStatus,
       "tnAutomationConfigAttributeTotal": tnAutomationConfigAttributeTotal,
       "tnAutomationConfigTable": tnAutomationConfigTable,
       "tnAutomationConfigEntry": tnAutomationConfigEntry,
       "tnAutomationConfigAutoTopoDegreeNumber": tnAutomationConfigAutoTopoDegreeNumber,
       "tnSfd5CardAttributeTotal": tnSfd5CardAttributeTotal,
       "tnSfd5CardTable": tnSfd5CardTable,
       "tnSfd5CardEntry": tnSfd5CardEntry,
       "tnSfd5CardPortLossCh1": tnSfd5CardPortLossCh1,
       "tnSfd5CardPortLossCh2": tnSfd5CardPortLossCh2,
       "tnSfd5CardPortLossCh3": tnSfd5CardPortLossCh3,
       "tnSfd5CardPortLossCh4": tnSfd5CardPortLossCh4,
       "tnSfd5CardPortLossCh5": tnSfd5CardPortLossCh5,
       "tnSfd5CardPortLossCh6": tnSfd5CardPortLossCh6,
       "tnSfd5CardPortLossCh7": tnSfd5CardPortLossCh7,
       "tnSfd5CardPortLossCh8": tnSfd5CardPortLossCh8,
       "tnSfd5CardPortLossCh9": tnSfd5CardPortLossCh9,
       "tnSfd5CardPortLossCh10": tnSfd5CardPortLossCh10,
       "tnSfd5CardPortLossEXP": tnSfd5CardPortLossEXP,
       "tnSfd5CardAveBIUFibLen": tnSfd5CardAveBIUFibLen,
       "tnSfd5CardAveBIDFibLen": tnSfd5CardAveBIDFibLen,
       "tnSfd10CardAttributeTotal": tnSfd10CardAttributeTotal,
       "tnSfd10CardTable": tnSfd10CardTable,
       "tnSfd10CardEntry": tnSfd10CardEntry,
       "tnSfd10CardDMuxPortLossCh1": tnSfd10CardDMuxPortLossCh1,
       "tnSfd10CardDMuxPortLossCh2": tnSfd10CardDMuxPortLossCh2,
       "tnSfd10CardDMuxPortLossCh3": tnSfd10CardDMuxPortLossCh3,
       "tnSfd10CardDMuxPortLossCh4": tnSfd10CardDMuxPortLossCh4,
       "tnSfd10CardDMuxPortLossCh5": tnSfd10CardDMuxPortLossCh5,
       "tnSfd10CardDMuxPortLossCh6": tnSfd10CardDMuxPortLossCh6,
       "tnSfd10CardDMuxPortLossCh7": tnSfd10CardDMuxPortLossCh7,
       "tnSfd10CardDMuxPortLossCh8": tnSfd10CardDMuxPortLossCh8,
       "tnSfd10CardDMuxPortLossCh9": tnSfd10CardDMuxPortLossCh9,
       "tnSfd10CardDMuxPortLossCh10": tnSfd10CardDMuxPortLossCh10,
       "tnSfd10CardDMuxPortLossEXP": tnSfd10CardDMuxPortLossEXP,
       "tnSfd10CardMuxPortLossCh1": tnSfd10CardMuxPortLossCh1,
       "tnSfd10CardMuxPortLossCh2": tnSfd10CardMuxPortLossCh2,
       "tnSfd10CardMuxPortLossCh3": tnSfd10CardMuxPortLossCh3,
       "tnSfd10CardMuxPortLossCh4": tnSfd10CardMuxPortLossCh4,
       "tnSfd10CardMuxPortLossCh5": tnSfd10CardMuxPortLossCh5,
       "tnSfd10CardMuxPortLossCh6": tnSfd10CardMuxPortLossCh6,
       "tnSfd10CardMuxPortLossCh7": tnSfd10CardMuxPortLossCh7,
       "tnSfd10CardMuxPortLossCh8": tnSfd10CardMuxPortLossCh8,
       "tnSfd10CardMuxPortLossCh9": tnSfd10CardMuxPortLossCh9,
       "tnSfd10CardMuxPortLossCh10": tnSfd10CardMuxPortLossCh10,
       "tnSfd10CardMuxPortLossEXP": tnSfd10CardMuxPortLossEXP,
       "tnSfd10CardAveMuxFibLen": tnSfd10CardAveMuxFibLen,
       "tnSfd10CardAveDMUXFibLen": tnSfd10CardAveDMUXFibLen,
       "tnDcmxCardAttributeTotal": tnDcmxCardAttributeTotal,
       "tnDcmxCardTable": tnDcmxCardTable,
       "tnDcmxCardEntry": tnDcmxCardEntry,
       "tnDcmxCardFiberType": tnDcmxCardFiberType,
       "tnDcmxCardDcmSize": tnDcmxCardDcmSize,
       "tnDcmxCardAverageInsertionLossDCF1": tnDcmxCardAverageInsertionLossDCF1,
       "tnDcmxCardInsertionLossSlopeDCF1": tnDcmxCardInsertionLossSlopeDCF1,
       "tnDcmxCardTotalDispFitDCF1": tnDcmxCardTotalDispFitDCF1,
       "tnDcmxCardDispFiberLengthDCF1": tnDcmxCardDispFiberLengthDCF1,
       "tnDcmxCardPMDDCF1": tnDcmxCardPMDDCF1,
       "tnDcmxCardAverageInsertionLossDCF2": tnDcmxCardAverageInsertionLossDCF2,
       "tnDcmxCardInsertionLossSlopeDCF2": tnDcmxCardInsertionLossSlopeDCF2,
       "tnDcmxCardTotalDispFitDCF2": tnDcmxCardTotalDispFitDCF2,
       "tnDcmxCardDispFiberLengthDCF2": tnDcmxCardDispFiberLengthDCF2,
       "tnDcmxCardPMDDCF2": tnDcmxCardPMDDCF2,
       "tnDcmxCardLatencyMismatch": tnDcmxCardLatencyMismatch,
       "tnDcmxCardLatency": tnDcmxCardLatency}
)
