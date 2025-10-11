# SNMP MIB module (ADTRAN-AOS-POE-STATUS-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-AOS-POE-STATUS-INFO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:17 2025
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

(adGenAOSConformance,
 adGenAOSSwitch) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSSwitch")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

adGenAOSPoEStatusInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 4, 2)
)
if mibBuilder.loadTexts:
    adGenAOSPoEStatusInfo.setRevisions(
        ("2018-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSPoEMon_ObjectIdentity = ObjectIdentity
adGenAOSPoEMon = _AdGenAOSPoEMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3)
)
_AdGenAOSPoESysInfo_ObjectIdentity = ObjectIdentity
adGenAOSPoESysInfo = _AdGenAOSPoESysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 1)
)


class _AdGenAOSPoEPseTotalPower_Type(DisplayString):
    """Custom type adGenAOSPoEPseTotalPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenAOSPoEPseTotalPower_Type.__name__ = "DisplayString"
_AdGenAOSPoEPseTotalPower_Object = MibScalar
adGenAOSPoEPseTotalPower = _AdGenAOSPoEPseTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 1, 1),
    _AdGenAOSPoEPseTotalPower_Type()
)
adGenAOSPoEPseTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPseTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    adGenAOSPoEPseTotalPower.setUnits("Watts")


class _AdGenAOSPoEPseTotalPowerUsed_Type(DisplayString):
    """Custom type adGenAOSPoEPseTotalPowerUsed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenAOSPoEPseTotalPowerUsed_Type.__name__ = "DisplayString"
_AdGenAOSPoEPseTotalPowerUsed_Object = MibScalar
adGenAOSPoEPseTotalPowerUsed = _AdGenAOSPoEPseTotalPowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 1, 2),
    _AdGenAOSPoEPseTotalPowerUsed_Type()
)
adGenAOSPoEPseTotalPowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPseTotalPowerUsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenAOSPoEPseTotalPowerUsed.setUnits("Watts")


class _AdGenAOSPoEPseTotalPowerAvailable_Type(DisplayString):
    """Custom type adGenAOSPoEPseTotalPowerAvailable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenAOSPoEPseTotalPowerAvailable_Type.__name__ = "DisplayString"
_AdGenAOSPoEPseTotalPowerAvailable_Object = MibScalar
adGenAOSPoEPseTotalPowerAvailable = _AdGenAOSPoEPseTotalPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 1, 3),
    _AdGenAOSPoEPseTotalPowerAvailable_Type()
)
adGenAOSPoEPseTotalPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPseTotalPowerAvailable.setStatus("current")
if mibBuilder.loadTexts:
    adGenAOSPoEPseTotalPowerAvailable.setUnits("Watts")


class _AdGenAOSPoEPseAverageTotalPowerUsed_Type(DisplayString):
    """Custom type adGenAOSPoEPseAverageTotalPowerUsed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenAOSPoEPseAverageTotalPowerUsed_Type.__name__ = "DisplayString"
_AdGenAOSPoEPseAverageTotalPowerUsed_Object = MibScalar
adGenAOSPoEPseAverageTotalPowerUsed = _AdGenAOSPoEPseAverageTotalPowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 1, 4),
    _AdGenAOSPoEPseAverageTotalPowerUsed_Type()
)
adGenAOSPoEPseAverageTotalPowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPseAverageTotalPowerUsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenAOSPoEPseAverageTotalPowerUsed.setUnits("Watts")
_AdGenAOSPoEPortInfo_ObjectIdentity = ObjectIdentity
adGenAOSPoEPortInfo = _AdGenAOSPoEPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2)
)
_AdGenAOSPoEPortInfoTable_Object = MibTable
adGenAOSPoEPortInfoTable = _AdGenAOSPoEPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSPoEPortInfoTable.setStatus("current")
_AdGenAOSPoEPortInfoTableEntry_Object = MibTableRow
adGenAOSPoEPortInfoTableEntry = _AdGenAOSPoEPortInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1)
)
adGenAOSPoEPortInfoTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSPoEPortInfoTableEntry.setStatus("current")


class _AdGenAOSPoEPsePortIfName_Type(DisplayString):
    """Custom type adGenAOSPoEPsePortIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdGenAOSPoEPsePortIfName_Type.__name__ = "DisplayString"
_AdGenAOSPoEPsePortIfName_Object = MibTableColumn
adGenAOSPoEPsePortIfName = _AdGenAOSPoEPsePortIfName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1, 1),
    _AdGenAOSPoEPsePortIfName_Type()
)
adGenAOSPoEPsePortIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortIfName.setStatus("current")
_AdGenAOSPoEPsePortPowerAdminMode_Type = DisplayString
_AdGenAOSPoEPsePortPowerAdminMode_Object = MibTableColumn
adGenAOSPoEPsePortPowerAdminMode = _AdGenAOSPoEPsePortPowerAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1, 2),
    _AdGenAOSPoEPsePortPowerAdminMode_Type()
)
adGenAOSPoEPsePortPowerAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortPowerAdminMode.setStatus("current")


class _AdGenAOSPoEPsePortPowerStatusMode_Type(Integer32):
    """Custom type adGenAOSPoEPsePortPowerStatusMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("limited", 1),
          ("delivering", 2),
          ("searching", 3),
          ("fault", 4),
          ("denied", 5),
          ("disabledThermal", 6),
          ("disabled", 7),
          ("otherFault", 8))
    )


_AdGenAOSPoEPsePortPowerStatusMode_Type.__name__ = "Integer32"
_AdGenAOSPoEPsePortPowerStatusMode_Object = MibTableColumn
adGenAOSPoEPsePortPowerStatusMode = _AdGenAOSPoEPsePortPowerStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1, 3),
    _AdGenAOSPoEPsePortPowerStatusMode_Type()
)
adGenAOSPoEPsePortPowerStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortPowerStatusMode.setStatus("current")


class _AdGenAOSPoEPsePortPowerUsed_Type(DisplayString):
    """Custom type adGenAOSPoEPsePortPowerUsed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenAOSPoEPsePortPowerUsed_Type.__name__ = "DisplayString"
_AdGenAOSPoEPsePortPowerUsed_Object = MibTableColumn
adGenAOSPoEPsePortPowerUsed = _AdGenAOSPoEPsePortPowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1, 4),
    _AdGenAOSPoEPsePortPowerUsed_Type()
)
adGenAOSPoEPsePortPowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortPowerUsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortPowerUsed.setUnits("Watts")


class _AdGenAOSPoEPsePortPowerClassifications_Type(Integer32):
    """Custom type adGenAOSPoEPsePortPowerClassifications based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("notApplicable", 6))
    )


_AdGenAOSPoEPsePortPowerClassifications_Type.__name__ = "Integer32"
_AdGenAOSPoEPsePortPowerClassifications_Object = MibTableColumn
adGenAOSPoEPsePortPowerClassifications = _AdGenAOSPoEPsePortPowerClassifications_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1, 5),
    _AdGenAOSPoEPsePortPowerClassifications_Type()
)
adGenAOSPoEPsePortPowerClassifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortPowerClassifications.setStatus("current")


class _AdGenAOSPoEPsePortVoltage_Type(DisplayString):
    """Custom type adGenAOSPoEPsePortVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenAOSPoEPsePortVoltage_Type.__name__ = "DisplayString"
_AdGenAOSPoEPsePortVoltage_Object = MibTableColumn
adGenAOSPoEPsePortVoltage = _AdGenAOSPoEPsePortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1, 6),
    _AdGenAOSPoEPsePortVoltage_Type()
)
adGenAOSPoEPsePortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortVoltage.setStatus("current")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortVoltage.setUnits("Volts")


class _AdGenAOSPoEPsePortCurrent_Type(DisplayString):
    """Custom type adGenAOSPoEPsePortCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenAOSPoEPsePortCurrent_Type.__name__ = "DisplayString"
_AdGenAOSPoEPsePortCurrent_Object = MibTableColumn
adGenAOSPoEPsePortCurrent = _AdGenAOSPoEPsePortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1, 7),
    _AdGenAOSPoEPsePortCurrent_Type()
)
adGenAOSPoEPsePortCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortCurrent.setStatus("current")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortCurrent.setUnits("mA")


class _AdGenAOSPoEPsePortMaxPower_Type(DisplayString):
    """Custom type adGenAOSPoEPsePortMaxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenAOSPoEPsePortMaxPower_Type.__name__ = "DisplayString"
_AdGenAOSPoEPsePortMaxPower_Object = MibTableColumn
adGenAOSPoEPsePortMaxPower = _AdGenAOSPoEPsePortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1, 8),
    _AdGenAOSPoEPsePortMaxPower_Type()
)
adGenAOSPoEPsePortMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortMaxPower.setUnits("Watts")


class _AdGenAOSPoEPsePortAveragePower_Type(DisplayString):
    """Custom type adGenAOSPoEPsePortAveragePower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenAOSPoEPsePortAveragePower_Type.__name__ = "DisplayString"
_AdGenAOSPoEPsePortAveragePower_Object = MibTableColumn
adGenAOSPoEPsePortAveragePower = _AdGenAOSPoEPsePortAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 3, 2, 1, 1, 9),
    _AdGenAOSPoEPsePortAveragePower_Type()
)
adGenAOSPoEPsePortAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    adGenAOSPoEPsePortAveragePower.setUnits("Watts")
_AdGenAOSPowerOverEthernetConformance_ObjectIdentity = ObjectIdentity
adGenAOSPowerOverEthernetConformance = _AdGenAOSPowerOverEthernetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 35)
)
_AdGenAOSPowerOverEthernetGroups_ObjectIdentity = ObjectIdentity
adGenAOSPowerOverEthernetGroups = _AdGenAOSPowerOverEthernetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 35, 1)
)
_AdGenAOSPowerOverEthernetCompliances_ObjectIdentity = ObjectIdentity
adGenAOSPowerOverEthernetCompliances = _AdGenAOSPowerOverEthernetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 35, 2)
)

# Managed Objects groups

adGenAOSPoESysInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 35, 1, 1)
)
adGenAOSPoESysInfoGroup.setObjects(
      *(("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPseTotalPower"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPseTotalPowerUsed"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPseTotalPowerAvailable"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPseAverageTotalPowerUsed"))
)
if mibBuilder.loadTexts:
    adGenAOSPoESysInfoGroup.setStatus("current")

adGenAOSPoEPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 35, 1, 2)
)
adGenAOSPoEPortInfoGroup.setObjects(
      *(("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPsePortIfName"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPsePortPowerAdminMode"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPsePortPowerStatusMode"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPsePortPowerUsed"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPsePortPowerClassifications"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPsePortVoltage"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPsePortCurrent"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPsePortMaxPower"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPsePortAveragePower"))
)
if mibBuilder.loadTexts:
    adGenAOSPoEPortInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAOSPowerOverEthernetFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 35, 2, 1)
)
adGenAOSPowerOverEthernetFullCompliance.setObjects(
      *(("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoESysInfoGroup"),
        ("ADTRAN-AOS-POE-STATUS-INFO-MIB", "adGenAOSPoEPortInfoGroup"))
)
if mibBuilder.loadTexts:
    adGenAOSPowerOverEthernetFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-POE-STATUS-INFO-MIB",
    **{"adGenAOSPoEMon": adGenAOSPoEMon,
       "adGenAOSPoESysInfo": adGenAOSPoESysInfo,
       "adGenAOSPoEPseTotalPower": adGenAOSPoEPseTotalPower,
       "adGenAOSPoEPseTotalPowerUsed": adGenAOSPoEPseTotalPowerUsed,
       "adGenAOSPoEPseTotalPowerAvailable": adGenAOSPoEPseTotalPowerAvailable,
       "adGenAOSPoEPseAverageTotalPowerUsed": adGenAOSPoEPseAverageTotalPowerUsed,
       "adGenAOSPoEPortInfo": adGenAOSPoEPortInfo,
       "adGenAOSPoEPortInfoTable": adGenAOSPoEPortInfoTable,
       "adGenAOSPoEPortInfoTableEntry": adGenAOSPoEPortInfoTableEntry,
       "adGenAOSPoEPsePortIfName": adGenAOSPoEPsePortIfName,
       "adGenAOSPoEPsePortPowerAdminMode": adGenAOSPoEPsePortPowerAdminMode,
       "adGenAOSPoEPsePortPowerStatusMode": adGenAOSPoEPsePortPowerStatusMode,
       "adGenAOSPoEPsePortPowerUsed": adGenAOSPoEPsePortPowerUsed,
       "adGenAOSPoEPsePortPowerClassifications": adGenAOSPoEPsePortPowerClassifications,
       "adGenAOSPoEPsePortVoltage": adGenAOSPoEPsePortVoltage,
       "adGenAOSPoEPsePortCurrent": adGenAOSPoEPsePortCurrent,
       "adGenAOSPoEPsePortMaxPower": adGenAOSPoEPsePortMaxPower,
       "adGenAOSPoEPsePortAveragePower": adGenAOSPoEPsePortAveragePower,
       "adGenAOSPowerOverEthernetConformance": adGenAOSPowerOverEthernetConformance,
       "adGenAOSPowerOverEthernetGroups": adGenAOSPowerOverEthernetGroups,
       "adGenAOSPoESysInfoGroup": adGenAOSPoESysInfoGroup,
       "adGenAOSPoEPortInfoGroup": adGenAOSPoEPortInfoGroup,
       "adGenAOSPowerOverEthernetCompliances": adGenAOSPowerOverEthernetCompliances,
       "adGenAOSPowerOverEthernetFullCompliance": adGenAOSPowerOverEthernetFullCompliance,
       "adGenAOSPoEStatusInfo": adGenAOSPoEStatusInfo}
)
