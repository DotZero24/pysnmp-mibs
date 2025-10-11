# SNMP MIB module (NEWTEC-AUPCCONTROLLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-AUPCCONTROLLER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:10 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcEnable,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcEnable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcAupcController = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200)
)
if mibBuilder.loadTexts:
    ntcAupcController.setRevisions(
        ("2017-10-16 12:00",
         "2014-02-03 12:00",
         "2013-05-22 06:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcAupcCtrlObjects_ObjectIdentity = ObjectIdentity
ntcAupcCtrlObjects = _NtcAupcCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1)
)
if mibBuilder.loadTexts:
    ntcAupcCtrlObjects.setStatus("current")


class _NtcAupcCtrlEnable_Type(NtcEnable):
    """Custom type ntcAupcCtrlEnable based on NtcEnable"""
    defaultValue = 0


_NtcAupcCtrlEnable_Type.__name__ = "NtcEnable"
_NtcAupcCtrlEnable_Object = MibScalar
ntcAupcCtrlEnable = _NtcAupcCtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 1),
    _NtcAupcCtrlEnable_Type()
)
ntcAupcCtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcCtrlEnable.setStatus("current")


class _NtcAupcCtrlNominalModPower_Type(Integer32):
    """Custom type ntcAupcCtrlNominalModPower based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 100),
    )


_NtcAupcCtrlNominalModPower_Type.__name__ = "Integer32"
_NtcAupcCtrlNominalModPower_Object = MibScalar
ntcAupcCtrlNominalModPower = _NtcAupcCtrlNominalModPower_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 2),
    _NtcAupcCtrlNominalModPower_Type()
)
ntcAupcCtrlNominalModPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcCtrlNominalModPower.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcCtrlNominalModPower.setUnits("dBm")


class _NtcAupcCtrlMaximumModPower_Type(Integer32):
    """Custom type ntcAupcCtrlMaximumModPower based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 100),
    )


_NtcAupcCtrlMaximumModPower_Type.__name__ = "Integer32"
_NtcAupcCtrlMaximumModPower_Object = MibScalar
ntcAupcCtrlMaximumModPower = _NtcAupcCtrlMaximumModPower_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 3),
    _NtcAupcCtrlMaximumModPower_Type()
)
ntcAupcCtrlMaximumModPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcCtrlMaximumModPower.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcCtrlMaximumModPower.setUnits("dBm")


class _NtcAupcCtrlMaximumPowerStepUp_Type(Integer32):
    """Custom type ntcAupcCtrlMaximumPowerStepUp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NtcAupcCtrlMaximumPowerStepUp_Type.__name__ = "Integer32"
_NtcAupcCtrlMaximumPowerStepUp_Object = MibScalar
ntcAupcCtrlMaximumPowerStepUp = _NtcAupcCtrlMaximumPowerStepUp_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 4),
    _NtcAupcCtrlMaximumPowerStepUp_Type()
)
ntcAupcCtrlMaximumPowerStepUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcCtrlMaximumPowerStepUp.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcCtrlMaximumPowerStepUp.setUnits("dBm/s")


class _NtcAupcCtrlMaximumPowerStepDown_Type(Integer32):
    """Custom type ntcAupcCtrlMaximumPowerStepDown based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NtcAupcCtrlMaximumPowerStepDown_Type.__name__ = "Integer32"
_NtcAupcCtrlMaximumPowerStepDown_Object = MibScalar
ntcAupcCtrlMaximumPowerStepDown = _NtcAupcCtrlMaximumPowerStepDown_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 5),
    _NtcAupcCtrlMaximumPowerStepDown_Type()
)
ntcAupcCtrlMaximumPowerStepDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcCtrlMaximumPowerStepDown.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcCtrlMaximumPowerStepDown.setUnits("dBm/s")


class _NtcAupcCtrlRefTerm_Type(Unsigned32):
    """Custom type ntcAupcCtrlRefTerm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65277),
    )


_NtcAupcCtrlRefTerm_Type.__name__ = "Unsigned32"
_NtcAupcCtrlRefTerm_Object = MibScalar
ntcAupcCtrlRefTerm = _NtcAupcCtrlRefTerm_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 6),
    _NtcAupcCtrlRefTerm_Type()
)
ntcAupcCtrlRefTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAupcCtrlRefTerm.setStatus("current")
_NtcAupcCtrlMonitoring_ObjectIdentity = ObjectIdentity
ntcAupcCtrlMonitoring = _NtcAupcCtrlMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 7)
)
if mibBuilder.loadTexts:
    ntcAupcCtrlMonitoring.setStatus("current")
_NtcAupcCtrlForwardConfigCounter_Type = Counter64
_NtcAupcCtrlForwardConfigCounter_Object = MibScalar
ntcAupcCtrlForwardConfigCounter = _NtcAupcCtrlForwardConfigCounter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 7, 1),
    _NtcAupcCtrlForwardConfigCounter_Type()
)
ntcAupcCtrlForwardConfigCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcCtrlForwardConfigCounter.setStatus("current")
_NtcAupcCtrlClientFeedbackCounter_Type = Counter64
_NtcAupcCtrlClientFeedbackCounter_Object = MibScalar
ntcAupcCtrlClientFeedbackCounter = _NtcAupcCtrlClientFeedbackCounter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 7, 2),
    _NtcAupcCtrlClientFeedbackCounter_Type()
)
ntcAupcCtrlClientFeedbackCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcCtrlClientFeedbackCounter.setStatus("current")
_NtcAupcCtrlPowerRequestCounter_Type = Counter64
_NtcAupcCtrlPowerRequestCounter_Object = MibScalar
ntcAupcCtrlPowerRequestCounter = _NtcAupcCtrlPowerRequestCounter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 7, 3),
    _NtcAupcCtrlPowerRequestCounter_Type()
)
ntcAupcCtrlPowerRequestCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcCtrlPowerRequestCounter.setStatus("current")


class _NtcAupcCtrlReqModulatorPower_Type(Integer32):
    """Custom type ntcAupcCtrlReqModulatorPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 100),
    )


_NtcAupcCtrlReqModulatorPower_Type.__name__ = "Integer32"
_NtcAupcCtrlReqModulatorPower_Object = MibScalar
ntcAupcCtrlReqModulatorPower = _NtcAupcCtrlReqModulatorPower_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 7, 4),
    _NtcAupcCtrlReqModulatorPower_Type()
)
ntcAupcCtrlReqModulatorPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcCtrlReqModulatorPower.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcCtrlReqModulatorPower.setUnits("dBm")


class _NtcAupcCtrlCurModulatorPower_Type(Integer32):
    """Custom type ntcAupcCtrlCurModulatorPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 100),
    )


_NtcAupcCtrlCurModulatorPower_Type.__name__ = "Integer32"
_NtcAupcCtrlCurModulatorPower_Object = MibScalar
ntcAupcCtrlCurModulatorPower = _NtcAupcCtrlCurModulatorPower_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 1, 7, 5),
    _NtcAupcCtrlCurModulatorPower_Type()
)
ntcAupcCtrlCurModulatorPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAupcCtrlCurModulatorPower.setStatus("current")
if mibBuilder.loadTexts:
    ntcAupcCtrlCurModulatorPower.setUnits("dBm")
_NtcAupcCtrlConformance_ObjectIdentity = ObjectIdentity
ntcAupcCtrlConformance = _NtcAupcCtrlConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 2)
)
if mibBuilder.loadTexts:
    ntcAupcCtrlConformance.setStatus("current")
_NtcAupcCtrlConfCompliance_ObjectIdentity = ObjectIdentity
ntcAupcCtrlConfCompliance = _NtcAupcCtrlConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 2, 1)
)
if mibBuilder.loadTexts:
    ntcAupcCtrlConfCompliance.setStatus("current")
_NtcAupcCtrlConfGroup_ObjectIdentity = ObjectIdentity
ntcAupcCtrlConfGroup = _NtcAupcCtrlConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 2, 2)
)
if mibBuilder.loadTexts:
    ntcAupcCtrlConfGroup.setStatus("current")

# Managed Objects groups

ntcAupcCtrlConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 2, 2, 1)
)
ntcAupcCtrlConfGrpV1Standard.setObjects(
      *(("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlEnable"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlNominalModPower"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlMaximumModPower"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlMaximumPowerStepUp"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlMaximumPowerStepDown"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlRefTerm"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlForwardConfigCounter"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlClientFeedbackCounter"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlPowerRequestCounter"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlReqModulatorPower"),
        ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlCurModulatorPower"))
)
if mibBuilder.loadTexts:
    ntcAupcCtrlConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcAupcCtrlConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 4200, 2, 1, 1)
)
ntcAupcCtrlConfCompV1Standard.setObjects(
    ("NEWTEC-AUPCCONTROLLER-MIB", "ntcAupcCtrlConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcAupcCtrlConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-AUPCCONTROLLER-MIB",
    **{"ntcAupcController": ntcAupcController,
       "ntcAupcCtrlObjects": ntcAupcCtrlObjects,
       "ntcAupcCtrlEnable": ntcAupcCtrlEnable,
       "ntcAupcCtrlNominalModPower": ntcAupcCtrlNominalModPower,
       "ntcAupcCtrlMaximumModPower": ntcAupcCtrlMaximumModPower,
       "ntcAupcCtrlMaximumPowerStepUp": ntcAupcCtrlMaximumPowerStepUp,
       "ntcAupcCtrlMaximumPowerStepDown": ntcAupcCtrlMaximumPowerStepDown,
       "ntcAupcCtrlRefTerm": ntcAupcCtrlRefTerm,
       "ntcAupcCtrlMonitoring": ntcAupcCtrlMonitoring,
       "ntcAupcCtrlForwardConfigCounter": ntcAupcCtrlForwardConfigCounter,
       "ntcAupcCtrlClientFeedbackCounter": ntcAupcCtrlClientFeedbackCounter,
       "ntcAupcCtrlPowerRequestCounter": ntcAupcCtrlPowerRequestCounter,
       "ntcAupcCtrlReqModulatorPower": ntcAupcCtrlReqModulatorPower,
       "ntcAupcCtrlCurModulatorPower": ntcAupcCtrlCurModulatorPower,
       "ntcAupcCtrlConformance": ntcAupcCtrlConformance,
       "ntcAupcCtrlConfCompliance": ntcAupcCtrlConfCompliance,
       "ntcAupcCtrlConfCompV1Standard": ntcAupcCtrlConfCompV1Standard,
       "ntcAupcCtrlConfGroup": ntcAupcCtrlConfGroup,
       "ntcAupcCtrlConfGrpV1Standard": ntcAupcCtrlConfGrpV1Standard}
)
