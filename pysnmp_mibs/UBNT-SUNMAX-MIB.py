# SNMP MIB module (UBNT-SUNMAX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ubiquiti/UBNT-SUNMAX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:27 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(ubntSunMax,
 ubntSunMaxGroups) = mibBuilder.importSymbols(
    "UBNT-MIB",
    "ubntSunMax",
    "ubntSunMaxGroups")


# MODULE-IDENTITY

sunMaxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1)
)
if mibBuilder.loadTexts:
    sunMaxMIB.setRevisions(
        ("2019-11-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SunMaxCompliances_ObjectIdentity = ObjectIdentity
sunMaxCompliances = _SunMaxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 10, 1)
)
_SunMaxGroups_ObjectIdentity = ObjectIdentity
sunMaxGroups = _SunMaxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 10, 2)
)
_SunMaxBatteryStats_ObjectIdentity = ObjectIdentity
sunMaxBatteryStats = _SunMaxBatteryStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 1)
)
_SunMaxBatCurrent_Type = Integer32
_SunMaxBatCurrent_Object = MibScalar
sunMaxBatCurrent = _SunMaxBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 1, 1),
    _SunMaxBatCurrent_Type()
)
sunMaxBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxBatCurrent.setStatus("current")
_SunMaxBatVoltage_Type = Integer32
_SunMaxBatVoltage_Object = MibScalar
sunMaxBatVoltage = _SunMaxBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 1, 2),
    _SunMaxBatVoltage_Type()
)
sunMaxBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxBatVoltage.setStatus("current")
_SunMaxBatPower_Type = Integer32
_SunMaxBatPower_Object = MibScalar
sunMaxBatPower = _SunMaxBatPower_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 1, 3),
    _SunMaxBatPower_Type()
)
sunMaxBatPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxBatPower.setStatus("current")
_SunMaxBatTemp_Type = Integer32
_SunMaxBatTemp_Object = MibScalar
sunMaxBatTemp = _SunMaxBatTemp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 1, 4),
    _SunMaxBatTemp_Type()
)
sunMaxBatTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxBatTemp.setStatus("current")
_SunMaxPvPanelStats_ObjectIdentity = ObjectIdentity
sunMaxPvPanelStats = _SunMaxPvPanelStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 2)
)
_SunMaxPVCurrent_Type = Integer32
_SunMaxPVCurrent_Object = MibScalar
sunMaxPVCurrent = _SunMaxPVCurrent_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 2, 1),
    _SunMaxPVCurrent_Type()
)
sunMaxPVCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxPVCurrent.setStatus("current")
_SunMaxPVVoltage_Type = Integer32
_SunMaxPVVoltage_Object = MibScalar
sunMaxPVVoltage = _SunMaxPVVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 2, 2),
    _SunMaxPVVoltage_Type()
)
sunMaxPVVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxPVVoltage.setStatus("current")
_SunMaxPVPower_Type = Integer32
_SunMaxPVPower_Object = MibScalar
sunMaxPVPower = _SunMaxPVPower_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 2, 3),
    _SunMaxPVPower_Type()
)
sunMaxPVPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxPVPower.setStatus("current")
_SunMaxOutPutStats_ObjectIdentity = ObjectIdentity
sunMaxOutPutStats = _SunMaxOutPutStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 3)
)
_SunMaxOutCurrent_Type = Integer32
_SunMaxOutCurrent_Object = MibScalar
sunMaxOutCurrent = _SunMaxOutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 3, 1),
    _SunMaxOutCurrent_Type()
)
sunMaxOutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxOutCurrent.setStatus("current")
_SunMaxOutVoltage_Type = Integer32
_SunMaxOutVoltage_Object = MibScalar
sunMaxOutVoltage = _SunMaxOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 3, 2),
    _SunMaxOutVoltage_Type()
)
sunMaxOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxOutVoltage.setStatus("current")
_SunMaxOutPower_Type = Integer32
_SunMaxOutPower_Object = MibScalar
sunMaxOutPower = _SunMaxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 11, 1, 3, 3),
    _SunMaxOutPower_Type()
)
sunMaxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunMaxOutPower.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBNT-SUNMAX-MIB",
    **{"sunMaxCompliances": sunMaxCompliances,
       "sunMaxGroups": sunMaxGroups,
       "sunMaxMIB": sunMaxMIB,
       "sunMaxBatteryStats": sunMaxBatteryStats,
       "sunMaxBatCurrent": sunMaxBatCurrent,
       "sunMaxBatVoltage": sunMaxBatVoltage,
       "sunMaxBatPower": sunMaxBatPower,
       "sunMaxBatTemp": sunMaxBatTemp,
       "sunMaxPvPanelStats": sunMaxPvPanelStats,
       "sunMaxPVCurrent": sunMaxPVCurrent,
       "sunMaxPVVoltage": sunMaxPVVoltage,
       "sunMaxPVPower": sunMaxPVPower,
       "sunMaxOutPutStats": sunMaxOutPutStats,
       "sunMaxOutCurrent": sunMaxOutCurrent,
       "sunMaxOutVoltage": sunMaxOutVoltage,
       "sunMaxOutPower": sunMaxOutPower}
)
