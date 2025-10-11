# SNMP MIB module (INFINERA-ENTITY-OLX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OLX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:20 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(InfnAutoTunable,
 InfnChannelPlan,
 InfnEqptType,
 InfnOcgType,
 InfnOperatingMode,
 InfnSlteOpMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnAutoTunable",
    "InfnChannelPlan",
    "InfnEqptType",
    "InfnOcgType",
    "InfnOperatingMode",
    "InfnSlteOpMode")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

olxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OlxTable_Object = MibTable
olxTable = _OlxTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1)
)
if mibBuilder.loadTexts:
    olxTable.setStatus("current")
_OlxEntry_Object = MibTableRow
olxEntry = _OlxEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1)
)
olxEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    olxEntry.setStatus("current")
_OlxMoId_Type = DisplayString
_OlxMoId_Object = MibTableColumn
olxMoId = _OlxMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 1),
    _OlxMoId_Type()
)
olxMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olxMoId.setStatus("current")
_OlxProvEqptType_Type = InfnEqptType
_OlxProvEqptType_Object = MibTableColumn
olxProvEqptType = _OlxProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 2),
    _OlxProvEqptType_Type()
)
olxProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olxProvEqptType.setStatus("current")


class _OlxOperatingMode_Type(InfnOperatingMode):
    """Custom type olxOperatingMode based on InfnOperatingMode"""
    defaultValue = 2


_OlxOperatingMode_Type.__name__ = "InfnOperatingMode"
_OlxOperatingMode_Object = MibTableColumn
olxOperatingMode = _OlxOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 3),
    _OlxOperatingMode_Type()
)
olxOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olxOperatingMode.setStatus("current")
_OlxAvailableTunableOcgNumbers_Type = Integer32
_OlxAvailableTunableOcgNumbers_Object = MibTableColumn
olxAvailableTunableOcgNumbers = _OlxAvailableTunableOcgNumbers_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 4),
    _OlxAvailableTunableOcgNumbers_Type()
)
olxAvailableTunableOcgNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olxAvailableTunableOcgNumbers.setStatus("current")
_OlxTunableOcgNumber_Type = Integer32
_OlxTunableOcgNumber_Object = MibTableColumn
olxTunableOcgNumber = _OlxTunableOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 5),
    _OlxTunableOcgNumber_Type()
)
olxTunableOcgNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olxTunableOcgNumber.setStatus("current")
_OlxCurOcgNumber_Type = Integer32
_OlxCurOcgNumber_Object = MibTableColumn
olxCurOcgNumber = _OlxCurOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 6),
    _OlxCurOcgNumber_Type()
)
olxCurOcgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olxCurOcgNumber.setStatus("current")
_OlxPicDspVer_Type = DisplayString
_OlxPicDspVer_Object = MibTableColumn
olxPicDspVer = _OlxPicDspVer_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 7),
    _OlxPicDspVer_Type()
)
olxPicDspVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olxPicDspVer.setStatus("current")
_OlxOcgNumber_Type = Integer32
_OlxOcgNumber_Object = MibTableColumn
olxOcgNumber = _OlxOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 8),
    _OlxOcgNumber_Type()
)
olxOcgNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olxOcgNumber.setStatus("current")
_OlxRowStatus_Type = RowStatus
_OlxRowStatus_Object = MibTableColumn
olxRowStatus = _OlxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 9),
    _OlxRowStatus_Type()
)
olxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olxRowStatus.setStatus("current")
_ActvTimingSource_Type = DisplayString
_ActvTimingSource_Object = MibTableColumn
actvTimingSource = _ActvTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 10),
    _ActvTimingSource_Type()
)
actvTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvTimingSource.setStatus("current")
_OlxRxEdfaGain_Type = Integer32
_OlxRxEdfaGain_Object = MibTableColumn
olxRxEdfaGain = _OlxRxEdfaGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 11),
    _OlxRxEdfaGain_Type()
)
olxRxEdfaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olxRxEdfaGain.setStatus("current")
_OlxRxEdfaOutputTargetPower_Type = Integer32
_OlxRxEdfaOutputTargetPower_Object = MibTableColumn
olxRxEdfaOutputTargetPower = _OlxRxEdfaOutputTargetPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 1, 1, 12),
    _OlxRxEdfaOutputTargetPower_Type()
)
olxRxEdfaOutputTargetPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olxRxEdfaOutputTargetPower.setStatus("current")
_OlxConformance_ObjectIdentity = ObjectIdentity
olxConformance = _OlxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 3)
)
_OlxCompliances_ObjectIdentity = ObjectIdentity
olxCompliances = _OlxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 3, 1)
)
_OlxGroups_ObjectIdentity = ObjectIdentity
olxGroups = _OlxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 3, 2)
)

# Managed Objects groups

olxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 3, 2, 1)
)
olxGroup.setObjects(
      *(("INFINERA-ENTITY-OLX-MIB", "olxMoId"),
        ("INFINERA-ENTITY-OLX-MIB", "olxProvEqptType"),
        ("INFINERA-ENTITY-OLX-MIB", "olxOperatingMode"),
        ("INFINERA-ENTITY-OLX-MIB", "olxAvailableTunableOcgNumbers"),
        ("INFINERA-ENTITY-OLX-MIB", "olxTunableOcgNumber"),
        ("INFINERA-ENTITY-OLX-MIB", "olxCurOcgNumber"),
        ("INFINERA-ENTITY-OLX-MIB", "olxPicDspVer"),
        ("INFINERA-ENTITY-OLX-MIB", "olxOcgNumber"),
        ("INFINERA-ENTITY-OLX-MIB", "olxRowStatus"),
        ("INFINERA-ENTITY-OLX-MIB", "actvTimingSource"),
        ("INFINERA-ENTITY-OLX-MIB", "olxRxEdfaGain"),
        ("INFINERA-ENTITY-OLX-MIB", "olxRxEdfaOutputTargetPower"))
)
if mibBuilder.loadTexts:
    olxGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

olxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 26, 3, 1, 1)
)
olxCompliance.setObjects(
    ("INFINERA-ENTITY-OLX-MIB", "olxGroup")
)
if mibBuilder.loadTexts:
    olxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OLX-MIB",
    **{"olxMIB": olxMIB,
       "olxTable": olxTable,
       "olxEntry": olxEntry,
       "olxMoId": olxMoId,
       "olxProvEqptType": olxProvEqptType,
       "olxOperatingMode": olxOperatingMode,
       "olxAvailableTunableOcgNumbers": olxAvailableTunableOcgNumbers,
       "olxTunableOcgNumber": olxTunableOcgNumber,
       "olxCurOcgNumber": olxCurOcgNumber,
       "olxPicDspVer": olxPicDspVer,
       "olxOcgNumber": olxOcgNumber,
       "olxRowStatus": olxRowStatus,
       "actvTimingSource": actvTimingSource,
       "olxRxEdfaGain": olxRxEdfaGain,
       "olxRxEdfaOutputTargetPower": olxRxEdfaOutputTargetPower,
       "olxConformance": olxConformance,
       "olxCompliances": olxCompliances,
       "olxCompliance": olxCompliance,
       "olxGroups": olxGroups,
       "olxGroup": olxGroup}
)
