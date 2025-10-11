# SNMP MIB module (MRV-PRIV-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/MRV-PRIV-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:02 2025
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

nbPrivTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21)
)
if mibBuilder.loadTexts:
    nbPrivTraps.setRevisions(
        ("2006-02-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TCEventClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serviceAffecting", 1),
          ("nonServiceAffecting", 2))
    )



class TCEventLevel(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4),
          ("clear", 5))
    )



class NbEthOamMepId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class NbEthOamMDLevel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class NbEthOamCcmHighestDefectPri(TextualConvention, Integer32):
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
        *(("none", 0),
          ("defRDICCM", 1),
          ("defMACstatus", 2),
          ("defRemoteCCM", 3),
          ("defErrorCCM", 4),
          ("defXconCCM", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_MrvPrivateTraps_ObjectIdentity = ObjectIdentity
mrvPrivateTraps = _MrvPrivateTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3)
)
_MrvTrapParameters_ObjectIdentity = ObjectIdentity
mrvTrapParameters = _MrvTrapParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1)
)
_MrvElementID_Type = DisplayString
_MrvElementID_Object = MibScalar
mrvElementID = _MrvElementID_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 2),
    _MrvElementID_Type()
)
mrvElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvElementID.setStatus("current")


class _MrvPortIndex_Type(Integer32):
    """Custom type mrvPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MrvPortIndex_Type.__name__ = "Integer32"
_MrvPortIndex_Object = MibScalar
mrvPortIndex = _MrvPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 5),
    _MrvPortIndex_Type()
)
mrvPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvPortIndex.setStatus("current")
_MrvEventDescription_Type = DisplayString
_MrvEventDescription_Object = MibScalar
mrvEventDescription = _MrvEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 7),
    _MrvEventDescription_Type()
)
mrvEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEventDescription.setStatus("current")
_MrvEventClass_Type = TCEventClass
_MrvEventClass_Object = MibScalar
mrvEventClass = _MrvEventClass_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 8),
    _MrvEventClass_Type()
)
mrvEventClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEventClass.setStatus("current")
_MrvEventLevel_Type = TCEventLevel
_MrvEventLevel_Object = MibScalar
mrvEventLevel = _MrvEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 9),
    _MrvEventLevel_Type()
)
mrvEventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEventLevel.setStatus("current")
_MrvDevPSIndex_Type = Integer32
_MrvDevPSIndex_Object = MibScalar
mrvDevPSIndex = _MrvDevPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 10),
    _MrvDevPSIndex_Type()
)
mrvDevPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvDevPSIndex.setStatus("current")
_MrvDevFANIndex_Type = Integer32
_MrvDevFANIndex_Object = MibScalar
mrvDevFANIndex = _MrvDevFANIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 11),
    _MrvDevFANIndex_Type()
)
mrvDevFANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvDevFANIndex.setStatus("current")
_MrvEthOamMdLevel_Type = NbEthOamMDLevel
_MrvEthOamMdLevel_Object = MibScalar
mrvEthOamMdLevel = _MrvEthOamMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 12),
    _MrvEthOamMdLevel_Type()
)
mrvEthOamMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEthOamMdLevel.setStatus("current")


class _MrvEthOamMaIndex_Type(Unsigned32):
    """Custom type mrvEthOamMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MrvEthOamMaIndex_Type.__name__ = "Unsigned32"
_MrvEthOamMaIndex_Object = MibScalar
mrvEthOamMaIndex = _MrvEthOamMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 13),
    _MrvEthOamMaIndex_Type()
)
mrvEthOamMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEthOamMaIndex.setStatus("current")
_MrvEthOamMepIdentifier_Type = NbEthOamMepId
_MrvEthOamMepIdentifier_Object = MibScalar
mrvEthOamMepIdentifier = _MrvEthOamMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 14),
    _MrvEthOamMepIdentifier_Type()
)
mrvEthOamMepIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEthOamMepIdentifier.setStatus("current")
_MrvEthOamTrapCcmHighestPrDefect_Type = NbEthOamCcmHighestDefectPri
_MrvEthOamTrapCcmHighestPrDefect_Object = MibScalar
mrvEthOamTrapCcmHighestPrDefect = _MrvEthOamTrapCcmHighestPrDefect_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 15),
    _MrvEthOamTrapCcmHighestPrDefect_Type()
)
mrvEthOamTrapCcmHighestPrDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEthOamTrapCcmHighestPrDefect.setStatus("current")
_MrvDevLosGrActivePortNumber_Type = Integer32
_MrvDevLosGrActivePortNumber_Object = MibScalar
mrvDevLosGrActivePortNumber = _MrvDevLosGrActivePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 16),
    _MrvDevLosGrActivePortNumber_Type()
)
mrvDevLosGrActivePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrvDevLosGrActivePortNumber.setStatus("current")


class _MrvDevLosGrPrimaryPort_Type(Integer32):
    """Custom type mrvDevLosGrPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MrvDevLosGrPrimaryPort_Type.__name__ = "Integer32"
_MrvDevLosGrPrimaryPort_Object = MibScalar
mrvDevLosGrPrimaryPort = _MrvDevLosGrPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 17),
    _MrvDevLosGrPrimaryPort_Type()
)
mrvDevLosGrPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrvDevLosGrPrimaryPort.setStatus("current")


class _MrvDevLosGrSecondaryPort_Type(Integer32):
    """Custom type mrvDevLosGrSecondaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MrvDevLosGrSecondaryPort_Type.__name__ = "Integer32"
_MrvDevLosGrSecondaryPort_Object = MibScalar
mrvDevLosGrSecondaryPort = _MrvDevLosGrSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 18),
    _MrvDevLosGrSecondaryPort_Type()
)
mrvDevLosGrSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvDevLosGrSecondaryPort.setStatus("current")


class _MrvDevLosGrActionCause_Type(Integer32):
    """Custom type mrvDevLosGrActionCause based on Integer32"""
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
        *(("noAction", 1),
          ("portLinkUp", 2),
          ("portLinkDown", 3),
          ("agRMepDiscardEvent", 4),
          ("agRMepNoConnEvent", 5),
          ("agRMepAliveEvent", 6),
          ("activePortAdminSet", 7))
    )


_MrvDevLosGrActionCause_Type.__name__ = "Integer32"
_MrvDevLosGrActionCause_Object = MibScalar
mrvDevLosGrActionCause = _MrvDevLosGrActionCause_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 19),
    _MrvDevLosGrActionCause_Type()
)
mrvDevLosGrActionCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvDevLosGrActionCause.setStatus("current")


class _MrvPortLinSlavePorts_Type(OctetString):
    """Custom type mrvPortLinSlavePorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MrvPortLinSlavePorts_Type.__name__ = "OctetString"
_MrvPortLinSlavePorts_Object = MibScalar
mrvPortLinSlavePorts = _MrvPortLinSlavePorts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 20),
    _MrvPortLinSlavePorts_Type()
)
mrvPortLinSlavePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrvPortLinSlavePorts.setStatus("current")


class _MrvPortLinActionCause_Type(Integer32):
    """Custom type mrvPortLinActionCause based on Integer32"""
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
        *(("noAction", 1),
          ("portLinkUp", 2),
          ("portLinkDown", 3),
          ("agRMepDiscardEvent", 4),
          ("agRMepNoConnEvent", 5),
          ("agRMepAliveEvent", 6))
    )


_MrvPortLinActionCause_Type.__name__ = "Integer32"
_MrvPortLinActionCause_Object = MibScalar
mrvPortLinActionCause = _MrvPortLinActionCause_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 1, 21),
    _MrvPortLinActionCause_Type()
)
mrvPortLinActionCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvPortLinActionCause.setStatus("current")
_MrvPrivateGenTraps_ObjectIdentity = ObjectIdentity
mrvPrivateGenTraps = _MrvPrivateGenTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6)
)
_MrvPrivateGenTrapPrefix_ObjectIdentity = ObjectIdentity
mrvPrivateGenTrapPrefix = _MrvPrivateGenTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0)
)
_MrvPrivateSpecTraps_ObjectIdentity = ObjectIdentity
mrvPrivateSpecTraps = _MrvPrivateSpecTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7)
)
_MrvPrivateSpecTrapPrefix_ObjectIdentity = ObjectIdentity
mrvPrivateSpecTrapPrefix = _MrvPrivateSpecTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0)
)
_MrvPrivateTrapsConformance_ObjectIdentity = ObjectIdentity
mrvPrivateTrapsConformance = _MrvPrivateTrapsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100)
)
_MrvPrivateTrapsMIBCompliances_ObjectIdentity = ObjectIdentity
mrvPrivateTrapsMIBCompliances = _MrvPrivateTrapsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 1)
)
_MrvPrivateTrapsMIBGroups_ObjectIdentity = ObjectIdentity
mrvPrivateTrapsMIBGroups = _MrvPrivateTrapsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 2)
)

# Managed Objects groups

mrvPrivateTrapsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 2, 1)
)
mrvPrivateTrapsMandatoryGroup.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevPSIndex"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevFANIndex"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMdLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMaIndex"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMepIdentifier"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamTrapCcmHighestPrDefect"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActivePortNumber"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrPrimaryPort"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrSecondaryPort"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActionCause"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortLinSlavePorts"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortLinActionCause"))
)
if mibBuilder.loadTexts:
    mrvPrivateTrapsMandatoryGroup.setStatus("current")


# Notification objects

mrvColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 1)
)
mrvColdStart.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
)
if mibBuilder.loadTexts:
    mrvColdStart.setStatus(
        "current"
    )

mrvWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 2)
)
mrvWarmStart.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
)
if mibBuilder.loadTexts:
    mrvWarmStart.setStatus(
        "current"
    )

mrvPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 3)
)
mrvPortLinkDown.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"))
)
if mibBuilder.loadTexts:
    mrvPortLinkDown.setStatus(
        "current"
    )

mrvPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 4)
)
mrvPortLinkUp.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"))
)
if mibBuilder.loadTexts:
    mrvPortLinkUp.setStatus(
        "current"
    )

mrvAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 6, 0, 5)
)
mrvAuthenticationFailure.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
)
if mibBuilder.loadTexts:
    mrvAuthenticationFailure.setStatus(
        "current"
    )

mrvPowerSupplyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 1)
)
mrvPowerSupplyUp.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevPSIndex"))
)
if mibBuilder.loadTexts:
    mrvPowerSupplyUp.setStatus(
        "current"
    )

mrvPowerSupplyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 2)
)
mrvPowerSupplyDown.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevPSIndex"))
)
if mibBuilder.loadTexts:
    mrvPowerSupplyDown.setStatus(
        "current"
    )

mrvFANUnitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 3)
)
mrvFANUnitUp.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevFANIndex"))
)
if mibBuilder.loadTexts:
    mrvFANUnitUp.setStatus(
        "current"
    )

mrvFANUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 4)
)
mrvFANUnitDown.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevFANIndex"))
)
if mibBuilder.loadTexts:
    mrvFANUnitDown.setStatus(
        "current"
    )

mrvDeviceTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 5)
)
mrvDeviceTemperatureNormal.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
)
if mibBuilder.loadTexts:
    mrvDeviceTemperatureNormal.setStatus(
        "current"
    )

mrvDeviceTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 6)
)
mrvDeviceTemperatureHigh.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"))
)
if mibBuilder.loadTexts:
    mrvDeviceTemperatureHigh.setStatus(
        "current"
    )

mrvDot1agCfmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 7)
)
mrvDot1agCfmFault.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMdLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMaIndex"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMepIdentifier"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamTrapCcmHighestPrDefect"))
)
if mibBuilder.loadTexts:
    mrvDot1agCfmFault.setStatus(
        "current"
    )

mrvDot1agCfmRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 8)
)
mrvDot1agCfmRecovery.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMdLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMaIndex"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamMepIdentifier"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEthOamTrapCcmHighestPrDefect"))
)
if mibBuilder.loadTexts:
    mrvDot1agCfmRecovery.setStatus(
        "current"
    )

mrvPortProtectionBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 9)
)
mrvPortProtectionBackup.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActivePortNumber"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrPrimaryPort"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrSecondaryPort"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActionCause"))
)
if mibBuilder.loadTexts:
    mrvPortProtectionBackup.setStatus(
        "current"
    )

mrvPortProtectionPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 10)
)
mrvPortProtectionPrimary.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActivePortNumber"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrPrimaryPort"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrSecondaryPort"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDevLosGrActionCause"))
)
if mibBuilder.loadTexts:
    mrvPortProtectionPrimary.setStatus(
        "current"
    )

mrvPortReflectionLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 11)
)
mrvPortReflectionLinkDown.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortLinSlavePorts"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortLinActionCause"))
)
if mibBuilder.loadTexts:
    mrvPortReflectionLinkDown.setStatus(
        "current"
    )

mrvPortReflectionLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 3, 7, 0, 12)
)
mrvPortReflectionLinkUp.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvElementID"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventDescription"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventLevel"),
        ("MRV-PRIV-TRAPS-MIB", "mrvEventClass"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortIndex"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortLinSlavePorts"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortLinActionCause"))
)
if mibBuilder.loadTexts:
    mrvPortReflectionLinkUp.setStatus(
        "current"
    )


# Notifications groups

mrvPrivateTrapsNotifGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 2, 2)
)
mrvPrivateTrapsNotifGrp.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvColdStart"),
        ("MRV-PRIV-TRAPS-MIB", "mrvWarmStart"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortLinkUp"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortLinkDown"),
        ("MRV-PRIV-TRAPS-MIB", "mrvAuthenticationFailure"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPowerSupplyUp"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPowerSupplyDown"),
        ("MRV-PRIV-TRAPS-MIB", "mrvFANUnitUp"),
        ("MRV-PRIV-TRAPS-MIB", "mrvFANUnitDown"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDeviceTemperatureNormal"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDeviceTemperatureHigh"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDot1agCfmFault"),
        ("MRV-PRIV-TRAPS-MIB", "mrvDot1agCfmRecovery"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortProtectionBackup"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortProtectionPrimary"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortReflectionLinkDown"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPortReflectionLinkUp"))
)
if mibBuilder.loadTexts:
    mrvPrivateTrapsNotifGrp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mrvPrivateTrapsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 21, 100, 1, 1)
)
mrvPrivateTrapsMIBCompliance.setObjects(
      *(("MRV-PRIV-TRAPS-MIB", "mrvPrivateTrapsMandatoryGroup"),
        ("MRV-PRIV-TRAPS-MIB", "mrvPrivateTrapsNotifGrp"))
)
if mibBuilder.loadTexts:
    mrvPrivateTrapsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-PRIV-TRAPS-MIB",
    **{"TCEventClass": TCEventClass,
       "TCEventLevel": TCEventLevel,
       "NbEthOamMepId": NbEthOamMepId,
       "NbEthOamMDLevel": NbEthOamMDLevel,
       "NbEthOamCcmHighestDefectPri": NbEthOamCcmHighestDefectPri,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbPrivTraps": nbPrivTraps,
       "mrvPrivateTraps": mrvPrivateTraps,
       "mrvTrapParameters": mrvTrapParameters,
       "mrvElementID": mrvElementID,
       "mrvPortIndex": mrvPortIndex,
       "mrvEventDescription": mrvEventDescription,
       "mrvEventClass": mrvEventClass,
       "mrvEventLevel": mrvEventLevel,
       "mrvDevPSIndex": mrvDevPSIndex,
       "mrvDevFANIndex": mrvDevFANIndex,
       "mrvEthOamMdLevel": mrvEthOamMdLevel,
       "mrvEthOamMaIndex": mrvEthOamMaIndex,
       "mrvEthOamMepIdentifier": mrvEthOamMepIdentifier,
       "mrvEthOamTrapCcmHighestPrDefect": mrvEthOamTrapCcmHighestPrDefect,
       "mrvDevLosGrActivePortNumber": mrvDevLosGrActivePortNumber,
       "mrvDevLosGrPrimaryPort": mrvDevLosGrPrimaryPort,
       "mrvDevLosGrSecondaryPort": mrvDevLosGrSecondaryPort,
       "mrvDevLosGrActionCause": mrvDevLosGrActionCause,
       "mrvPortLinSlavePorts": mrvPortLinSlavePorts,
       "mrvPortLinActionCause": mrvPortLinActionCause,
       "mrvPrivateGenTraps": mrvPrivateGenTraps,
       "mrvPrivateGenTrapPrefix": mrvPrivateGenTrapPrefix,
       "mrvColdStart": mrvColdStart,
       "mrvWarmStart": mrvWarmStart,
       "mrvPortLinkDown": mrvPortLinkDown,
       "mrvPortLinkUp": mrvPortLinkUp,
       "mrvAuthenticationFailure": mrvAuthenticationFailure,
       "mrvPrivateSpecTraps": mrvPrivateSpecTraps,
       "mrvPrivateSpecTrapPrefix": mrvPrivateSpecTrapPrefix,
       "mrvPowerSupplyUp": mrvPowerSupplyUp,
       "mrvPowerSupplyDown": mrvPowerSupplyDown,
       "mrvFANUnitUp": mrvFANUnitUp,
       "mrvFANUnitDown": mrvFANUnitDown,
       "mrvDeviceTemperatureNormal": mrvDeviceTemperatureNormal,
       "mrvDeviceTemperatureHigh": mrvDeviceTemperatureHigh,
       "mrvDot1agCfmFault": mrvDot1agCfmFault,
       "mrvDot1agCfmRecovery": mrvDot1agCfmRecovery,
       "mrvPortProtectionBackup": mrvPortProtectionBackup,
       "mrvPortProtectionPrimary": mrvPortProtectionPrimary,
       "mrvPortReflectionLinkDown": mrvPortReflectionLinkDown,
       "mrvPortReflectionLinkUp": mrvPortReflectionLinkUp,
       "mrvPrivateTrapsConformance": mrvPrivateTrapsConformance,
       "mrvPrivateTrapsMIBCompliances": mrvPrivateTrapsMIBCompliances,
       "mrvPrivateTrapsMIBCompliance": mrvPrivateTrapsMIBCompliance,
       "mrvPrivateTrapsMIBGroups": mrvPrivateTrapsMIBGroups,
       "mrvPrivateTrapsMandatoryGroup": mrvPrivateTrapsMandatoryGroup,
       "mrvPrivateTrapsNotifGrp": mrvPrivateTrapsNotifGrp}
)
