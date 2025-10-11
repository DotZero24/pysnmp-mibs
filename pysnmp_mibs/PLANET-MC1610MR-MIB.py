# SNMP MIB module (PLANET-MC1610MR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/planet/PLANET-MC1610MR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:07:57 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

planet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10456)
)
if mibBuilder.loadTexts:
    planet.setRevisions(
        ("2021-05-19 00:00",
         "2008-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MediaConverter_ObjectIdentity = ObjectIdentity
mediaConverter = _MediaConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 2)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625)
)
_ChassisIfNumber_Type = Integer32
_ChassisIfNumber_Object = MibScalar
chassisIfNumber = _ChassisIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 1),
    _ChassisIfNumber_Type()
)
chassisIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIfNumber.setStatus("current")
_ChassisIfInfo_ObjectIdentity = ObjectIdentity
chassisIfInfo = _ChassisIfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2)
)
_ChassisIfStatusTable_Object = MibTable
chassisIfStatusTable = _ChassisIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1)
)
if mibBuilder.loadTexts:
    chassisIfStatusTable.setStatus("current")
_ChassisIfStatusEntry_Object = MibTableRow
chassisIfStatusEntry = _ChassisIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1, 1)
)
chassisIfStatusEntry.setIndexNames(
    (0, "PLANET-MC1610MR-MIB", "chassisIfStatusIndex"),
)
if mibBuilder.loadTexts:
    chassisIfStatusEntry.setStatus("current")


class _ChassisIfStatusIndex_Type(Unsigned32):
    """Custom type chassisIfStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ChassisIfStatusIndex_Type.__name__ = "Unsigned32"
_ChassisIfStatusIndex_Object = MibTableColumn
chassisIfStatusIndex = _ChassisIfStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1, 1, 1),
    _ChassisIfStatusIndex_Type()
)
chassisIfStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIfStatusIndex.setStatus("current")
_ChassisIfStatusName_Type = OctetString
_ChassisIfStatusName_Object = MibTableColumn
chassisIfStatusName = _ChassisIfStatusName_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1, 1, 2),
    _ChassisIfStatusName_Type()
)
chassisIfStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIfStatusName.setStatus("current")


class _ChassisIfStatusTPStatus_Type(Integer32):
    """Custom type chassisIfStatusTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("linkUp", 1))
    )


_ChassisIfStatusTPStatus_Type.__name__ = "Integer32"
_ChassisIfStatusTPStatus_Object = MibTableColumn
chassisIfStatusTPStatus = _ChassisIfStatusTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1, 1, 3),
    _ChassisIfStatusTPStatus_Type()
)
chassisIfStatusTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIfStatusTPStatus.setStatus("current")


class _ChassisIfStatusTPSpeed_Type(Integer32):
    """Custom type chassisIfStatusTPSpeed based on Integer32"""
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
        *(("linkDown", 0),
          ("ifSpeed-10M", 1),
          ("ifSpeed-100M", 2),
          ("ifSpeed-1000M", 3))
    )


_ChassisIfStatusTPSpeed_Type.__name__ = "Integer32"
_ChassisIfStatusTPSpeed_Object = MibTableColumn
chassisIfStatusTPSpeed = _ChassisIfStatusTPSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1, 1, 4),
    _ChassisIfStatusTPSpeed_Type()
)
chassisIfStatusTPSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIfStatusTPSpeed.setStatus("current")


class _ChassisIfStatusTPDuplex_Type(Integer32):
    """Custom type chassisIfStatusTPDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("half", 1),
          ("full", 2))
    )


_ChassisIfStatusTPDuplex_Type.__name__ = "Integer32"
_ChassisIfStatusTPDuplex_Object = MibTableColumn
chassisIfStatusTPDuplex = _ChassisIfStatusTPDuplex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1, 1, 5),
    _ChassisIfStatusTPDuplex_Type()
)
chassisIfStatusTPDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIfStatusTPDuplex.setStatus("current")


class _ChassisIfStatusFXStatus_Type(Integer32):
    """Custom type chassisIfStatusFXStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("linkUp", 1))
    )


_ChassisIfStatusFXStatus_Type.__name__ = "Integer32"
_ChassisIfStatusFXStatus_Object = MibTableColumn
chassisIfStatusFXStatus = _ChassisIfStatusFXStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1, 1, 6),
    _ChassisIfStatusFXStatus_Type()
)
chassisIfStatusFXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIfStatusFXStatus.setStatus("current")


class _ChassisIfStatusFXSpeed_Type(Integer32):
    """Custom type chassisIfStatusFXSpeed based on Integer32"""
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
        *(("linkDown", 0),
          ("ifSpeed-10M", 1),
          ("ifSpeed-100M", 2),
          ("ifSpeed-1000M", 3))
    )


_ChassisIfStatusFXSpeed_Type.__name__ = "Integer32"
_ChassisIfStatusFXSpeed_Object = MibTableColumn
chassisIfStatusFXSpeed = _ChassisIfStatusFXSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1, 1, 7),
    _ChassisIfStatusFXSpeed_Type()
)
chassisIfStatusFXSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIfStatusFXSpeed.setStatus("current")


class _ChassisIfStatusFXDuplex_Type(Integer32):
    """Custom type chassisIfStatusFXDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("half", 1),
          ("full", 2))
    )


_ChassisIfStatusFXDuplex_Type.__name__ = "Integer32"
_ChassisIfStatusFXDuplex_Object = MibTableColumn
chassisIfStatusFXDuplex = _ChassisIfStatusFXDuplex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 1, 1, 8),
    _ChassisIfStatusFXDuplex_Type()
)
chassisIfStatusFXDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIfStatusFXDuplex.setStatus("current")
_ChassisIfConfTable_Object = MibTable
chassisIfConfTable = _ChassisIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2)
)
if mibBuilder.loadTexts:
    chassisIfConfTable.setStatus("current")
_ChassisIfConfEntry_Object = MibTableRow
chassisIfConfEntry = _ChassisIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1)
)
chassisIfConfEntry.setIndexNames(
    (0, "PLANET-MC1610MR-MIB", "chassisIfStatusIndex"),
)
if mibBuilder.loadTexts:
    chassisIfConfEntry.setStatus("current")


class _ChassisIfConfAdmin_Type(Integer32):
    """Custom type chassisIfConfAdmin based on Integer32"""
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


_ChassisIfConfAdmin_Type.__name__ = "Integer32"
_ChassisIfConfAdmin_Object = MibTableColumn
chassisIfConfAdmin = _ChassisIfConfAdmin_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1, 1),
    _ChassisIfConfAdmin_Type()
)
chassisIfConfAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIfConfAdmin.setStatus("current")


class _ChassisIfConfTPANmode_Type(Integer32):
    """Custom type chassisIfConfTPANmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_ChassisIfConfTPANmode_Type.__name__ = "Integer32"
_ChassisIfConfTPANmode_Object = MibTableColumn
chassisIfConfTPANmode = _ChassisIfConfTPANmode_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1, 2),
    _ChassisIfConfTPANmode_Type()
)
chassisIfConfTPANmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIfConfTPANmode.setStatus("current")


class _ChassisIfConfTPSpeed_Type(Integer32):
    """Custom type chassisIfConfTPSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifSpeed-10M", 0),
          ("ifSpeed-100M", 1),
          ("ifSpeed-1000M", 2))
    )


_ChassisIfConfTPSpeed_Type.__name__ = "Integer32"
_ChassisIfConfTPSpeed_Object = MibTableColumn
chassisIfConfTPSpeed = _ChassisIfConfTPSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1, 3),
    _ChassisIfConfTPSpeed_Type()
)
chassisIfConfTPSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIfConfTPSpeed.setStatus("current")


class _ChassisIfConfTPDuplex_Type(Integer32):
    """Custom type chassisIfConfTPDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1))
    )


_ChassisIfConfTPDuplex_Type.__name__ = "Integer32"
_ChassisIfConfTPDuplex_Object = MibTableColumn
chassisIfConfTPDuplex = _ChassisIfConfTPDuplex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1, 4),
    _ChassisIfConfTPDuplex_Type()
)
chassisIfConfTPDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIfConfTPDuplex.setStatus("current")


class _ChassisIfConfTPFlowControl_Type(Integer32):
    """Custom type chassisIfConfTPFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_ChassisIfConfTPFlowControl_Type.__name__ = "Integer32"
_ChassisIfConfTPFlowControl_Object = MibTableColumn
chassisIfConfTPFlowControl = _ChassisIfConfTPFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1, 5),
    _ChassisIfConfTPFlowControl_Type()
)
chassisIfConfTPFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIfConfTPFlowControl.setStatus("current")


class _ChassisIfConfLLCF_Type(Integer32):
    """Custom type chassisIfConfLLCF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_ChassisIfConfLLCF_Type.__name__ = "Integer32"
_ChassisIfConfLLCF_Object = MibTableColumn
chassisIfConfLLCF = _ChassisIfConfLLCF_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1, 6),
    _ChassisIfConfLLCF_Type()
)
chassisIfConfLLCF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIfConfLLCF.setStatus("current")


class _ChassisIfConfFXDuplex_Type(Integer32):
    """Custom type chassisIfConfFXDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1))
    )


_ChassisIfConfFXDuplex_Type.__name__ = "Integer32"
_ChassisIfConfFXDuplex_Object = MibTableColumn
chassisIfConfFXDuplex = _ChassisIfConfFXDuplex_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1, 7),
    _ChassisIfConfFXDuplex_Type()
)
chassisIfConfFXDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIfConfFXDuplex.setStatus("current")


class _ChassisIfConfFXLLR_Type(Integer32):
    """Custom type chassisIfConfFXLLR based on Integer32"""
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


_ChassisIfConfFXLLR_Type.__name__ = "Integer32"
_ChassisIfConfFXLLR_Object = MibTableColumn
chassisIfConfFXLLR = _ChassisIfConfFXLLR_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1, 8),
    _ChassisIfConfFXLLR_Type()
)
chassisIfConfFXLLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIfConfFXLLR.setStatus("current")


class _ChassisIfConfFXANbyPass_Type(Integer32):
    """Custom type chassisIfConfFXANbyPass based on Integer32"""
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


_ChassisIfConfFXANbyPass_Type.__name__ = "Integer32"
_ChassisIfConfFXANbyPass_Object = MibTableColumn
chassisIfConfFXANbyPass = _ChassisIfConfFXANbyPass_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 2, 2, 1, 9),
    _ChassisIfConfFXANbyPass_Type()
)
chassisIfConfFXANbyPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIfConfFXANbyPass.setStatus("current")
_ChassisTemperature_Type = OctetString
_ChassisTemperature_Object = MibScalar
chassisTemperature = _ChassisTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 3),
    _ChassisTemperature_Type()
)
chassisTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperature.setStatus("current")


class _ChassisPowerStatus_Type(Integer32):
    """Custom type chassisPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("fail", 2))
    )


_ChassisPowerStatus_Type.__name__ = "Integer32"
_ChassisPowerStatus_Object = MibScalar
chassisPowerStatus = _ChassisPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 4),
    _ChassisPowerStatus_Type()
)
chassisPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPowerStatus.setStatus("current")


class _ChassisFanStatus_Type(Integer32):
    """Custom type chassisFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("fail", 2))
    )


_ChassisFanStatus_Type.__name__ = "Integer32"
_ChassisFanStatus_Object = MibScalar
chassisFanStatus = _ChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 5),
    _ChassisFanStatus_Type()
)
chassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanStatus.setStatus("current")


class _ChassisRedundant_Type(Integer32):
    """Custom type chassisRedundant based on Integer32"""
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


_ChassisRedundant_Type.__name__ = "Integer32"
_ChassisRedundant_Object = MibScalar
chassisRedundant = _ChassisRedundant_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 6),
    _ChassisRedundant_Type()
)
chassisRedundant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisRedundant.setStatus("current")
_ChassisSlotLocation_Type = OctetString
_ChassisSlotLocation_Object = MibScalar
chassisSlotLocation = _ChassisSlotLocation_Object(
    (1, 3, 6, 1, 4, 1, 10456, 2, 625, 7),
    _ChassisSlotLocation_Type()
)
chassisSlotLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisSlotLocation.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PLANET-MC1610MR-MIB",
    **{"planet": planet,
       "mediaConverter": mediaConverter,
       "chassis": chassis,
       "chassisIfNumber": chassisIfNumber,
       "chassisIfInfo": chassisIfInfo,
       "chassisIfStatusTable": chassisIfStatusTable,
       "chassisIfStatusEntry": chassisIfStatusEntry,
       "chassisIfStatusIndex": chassisIfStatusIndex,
       "chassisIfStatusName": chassisIfStatusName,
       "chassisIfStatusTPStatus": chassisIfStatusTPStatus,
       "chassisIfStatusTPSpeed": chassisIfStatusTPSpeed,
       "chassisIfStatusTPDuplex": chassisIfStatusTPDuplex,
       "chassisIfStatusFXStatus": chassisIfStatusFXStatus,
       "chassisIfStatusFXSpeed": chassisIfStatusFXSpeed,
       "chassisIfStatusFXDuplex": chassisIfStatusFXDuplex,
       "chassisIfConfTable": chassisIfConfTable,
       "chassisIfConfEntry": chassisIfConfEntry,
       "chassisIfConfAdmin": chassisIfConfAdmin,
       "chassisIfConfTPANmode": chassisIfConfTPANmode,
       "chassisIfConfTPSpeed": chassisIfConfTPSpeed,
       "chassisIfConfTPDuplex": chassisIfConfTPDuplex,
       "chassisIfConfTPFlowControl": chassisIfConfTPFlowControl,
       "chassisIfConfLLCF": chassisIfConfLLCF,
       "chassisIfConfFXDuplex": chassisIfConfFXDuplex,
       "chassisIfConfFXLLR": chassisIfConfFXLLR,
       "chassisIfConfFXANbyPass": chassisIfConfFXANbyPass,
       "chassisTemperature": chassisTemperature,
       "chassisPowerStatus": chassisPowerStatus,
       "chassisFanStatus": chassisFanStatus,
       "chassisRedundant": chassisRedundant,
       "chassisSlotLocation": chassisSlotLocation}
)
