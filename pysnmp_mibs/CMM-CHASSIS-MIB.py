# SNMP MIB module (CMM-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ipinfusion/CMM-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:20 2025
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

(ipi,) = mibBuilder.importSymbols(
    "OCNOS-IPI-MODULE-MIB",
    "ipi")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cmm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LedColorCode(TextualConvention, Integer32):
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("green", 2),
          ("blinking-green", 3),
          ("solid-green", 4),
          ("amber", 5),
          ("blinking-amber", 6),
          ("solid-amber", 7),
          ("red", 8),
          ("blinking-red", 9),
          ("solid-red", 10),
          ("blue", 11),
          ("blinking-blue", 12),
          ("yellow", 13),
          ("blinking-yellow", 14),
          ("orange", 15),
          ("slow-blinking-green", 16),
          ("fast-blinking-green", 17),
          ("unknown", 30))
    )



class SystemStatusCode(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cpu", 0),
          ("ram", 1),
          ("disk", 2),
          ("low-temperature", 3),
          ("high-temperature", 4),
          ("fan", 5),
          ("power", 6),
          ("software", 7))
    )


# MIB Managed Objects in the order of their OIDs

_CmmChassisObject_ObjectIdentity = ObjectIdentity
CmmChassisObject = _CmmChassisObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1)
)
_CmmObjects_ObjectIdentity = ObjectIdentity
cmmObjects = _CmmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 1)
)
_CmmNumStackUnits_Type = Integer32
_CmmNumStackUnits_Object = MibScalar
cmmNumStackUnits = _CmmNumStackUnits_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 1, 1),
    _CmmNumStackUnits_Type()
)
cmmNumStackUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmNumStackUnits.setStatus("current")
_CmmSysObjects_ObjectIdentity = ObjectIdentity
cmmSysObjects = _CmmSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2)
)
_CmmStackUnitTable_Object = MibTable
cmmStackUnitTable = _CmmStackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmmStackUnitTable.setStatus("current")
_CmmStackUnitEntry_Object = MibTableRow
cmmStackUnitEntry = _CmmStackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1)
)
cmmStackUnitEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmStackUnitEntry.setStatus("current")
_CmmStackUnitIndex_Type = Integer32
_CmmStackUnitIndex_Object = MibTableColumn
cmmStackUnitIndex = _CmmStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 1),
    _CmmStackUnitIndex_Type()
)
cmmStackUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmStackUnitIndex.setStatus("current")
_CmmStackUnitModelName_Type = DisplayString
_CmmStackUnitModelName_Object = MibTableColumn
cmmStackUnitModelName = _CmmStackUnitModelName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 2),
    _CmmStackUnitModelName_Type()
)
cmmStackUnitModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitModelName.setStatus("current")
_CmmStackUnitSerialNumber_Type = DisplayString
_CmmStackUnitSerialNumber_Object = MibTableColumn
cmmStackUnitSerialNumber = _CmmStackUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 3),
    _CmmStackUnitSerialNumber_Type()
)
cmmStackUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitSerialNumber.setStatus("current")
_CmmStackUnitUpTime_Type = TimeTicks
_CmmStackUnitUpTime_Object = MibTableColumn
cmmStackUnitUpTime = _CmmStackUnitUpTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 4),
    _CmmStackUnitUpTime_Type()
)
cmmStackUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitUpTime.setStatus("current")
_CmmStackUnitMfgDate_Type = DateAndTime
_CmmStackUnitMfgDate_Object = MibTableColumn
cmmStackUnitMfgDate = _CmmStackUnitMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 5),
    _CmmStackUnitMfgDate_Type()
)
cmmStackUnitMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitMfgDate.setStatus("current")
_CmmStackUnitMacAddress_Type = MacAddress
_CmmStackUnitMacAddress_Object = MibTableColumn
cmmStackUnitMacAddress = _CmmStackUnitMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 6),
    _CmmStackUnitMacAddress_Type()
)
cmmStackUnitMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitMacAddress.setStatus("current")
_CmmStackUnitPartNum_Type = DisplayString
_CmmStackUnitPartNum_Object = MibTableColumn
cmmStackUnitPartNum = _CmmStackUnitPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 7),
    _CmmStackUnitPartNum_Type()
)
cmmStackUnitPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitPartNum.setStatus("current")
_CmmStackLabelRevision_Type = DisplayString
_CmmStackLabelRevision_Object = MibTableColumn
cmmStackLabelRevision = _CmmStackLabelRevision_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 8),
    _CmmStackLabelRevision_Type()
)
cmmStackLabelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackLabelRevision.setStatus("current")


class _CmmStackUnitCountryCode_Type(OctetString):
    """Custom type cmmStackUnitCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CmmStackUnitCountryCode_Type.__name__ = "OctetString"
_CmmStackUnitCountryCode_Object = MibTableColumn
cmmStackUnitCountryCode = _CmmStackUnitCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 9),
    _CmmStackUnitCountryCode_Type()
)
cmmStackUnitCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCountryCode.setStatus("current")


class _CmmStackUnitServiceTag_Type(DisplayString):
    """Custom type cmmStackUnitServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_CmmStackUnitServiceTag_Type.__name__ = "DisplayString"
_CmmStackUnitServiceTag_Object = MibTableColumn
cmmStackUnitServiceTag = _CmmStackUnitServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 10),
    _CmmStackUnitServiceTag_Type()
)
cmmStackUnitServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitServiceTag.setStatus("current")
_CmmStackPlatformName_Type = DisplayString
_CmmStackPlatformName_Object = MibTableColumn
cmmStackPlatformName = _CmmStackPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 11),
    _CmmStackPlatformName_Type()
)
cmmStackPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackPlatformName.setStatus("current")
_CmmStackOnieVersion_Type = DisplayString
_CmmStackOnieVersion_Object = MibTableColumn
cmmStackOnieVersion = _CmmStackOnieVersion_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 12),
    _CmmStackOnieVersion_Type()
)
cmmStackOnieVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackOnieVersion.setStatus("current")
_CmmStackMfgName_Type = DisplayString
_CmmStackMfgName_Object = MibTableColumn
cmmStackMfgName = _CmmStackMfgName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 13),
    _CmmStackMfgName_Type()
)
cmmStackMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackMfgName.setStatus("current")
_CmmStackVendorName_Type = DisplayString
_CmmStackVendorName_Object = MibTableColumn
cmmStackVendorName = _CmmStackVendorName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 14),
    _CmmStackVendorName_Type()
)
cmmStackVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackVendorName.setStatus("current")
_CmmStackDiagVersion_Type = DisplayString
_CmmStackDiagVersion_Object = MibTableColumn
cmmStackDiagVersion = _CmmStackDiagVersion_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 15),
    _CmmStackDiagVersion_Type()
)
cmmStackDiagVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackDiagVersion.setStatus("current")


class _CmmStackCrc32_Type(OctetString):
    """Custom type cmmStackCrc32 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_CmmStackCrc32_Type.__name__ = "OctetString"
_CmmStackCrc32_Object = MibTableColumn
cmmStackCrc32 = _CmmStackCrc32_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 16),
    _CmmStackCrc32_Type()
)
cmmStackCrc32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCrc32.setStatus("current")
_CmmStackUnitNumFanControllers_Type = Integer32
_CmmStackUnitNumFanControllers_Object = MibTableColumn
cmmStackUnitNumFanControllers = _CmmStackUnitNumFanControllers_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 17),
    _CmmStackUnitNumFanControllers_Type()
)
cmmStackUnitNumFanControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumFanControllers.setStatus("current")
_CmmStackUnitNumFanTrays_Type = Integer32
_CmmStackUnitNumFanTrays_Object = MibTableColumn
cmmStackUnitNumFanTrays = _CmmStackUnitNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 18),
    _CmmStackUnitNumFanTrays_Type()
)
cmmStackUnitNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumFanTrays.setStatus("current")
_CmmStackUnitNumPowerSupplies_Type = Integer32
_CmmStackUnitNumPowerSupplies_Object = MibTableColumn
cmmStackUnitNumPowerSupplies = _CmmStackUnitNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 19),
    _CmmStackUnitNumPowerSupplies_Type()
)
cmmStackUnitNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumPowerSupplies.setStatus("current")
_CmmStackUnitNumPluggableModules_Type = Integer32
_CmmStackUnitNumPluggableModules_Object = MibTableColumn
cmmStackUnitNumPluggableModules = _CmmStackUnitNumPluggableModules_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 20),
    _CmmStackUnitNumPluggableModules_Type()
)
cmmStackUnitNumPluggableModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumPluggableModules.setStatus("current")
_CmmStackUnitNumFastEtherPorts_Type = Integer32
_CmmStackUnitNumFastEtherPorts_Object = MibTableColumn
cmmStackUnitNumFastEtherPorts = _CmmStackUnitNumFastEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 21),
    _CmmStackUnitNumFastEtherPorts_Type()
)
cmmStackUnitNumFastEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumFastEtherPorts.setStatus("current")
_CmmStackUnitNumGigEtherPorts_Type = Integer32
_CmmStackUnitNumGigEtherPorts_Object = MibTableColumn
cmmStackUnitNumGigEtherPorts = _CmmStackUnitNumGigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 22),
    _CmmStackUnitNumGigEtherPorts_Type()
)
cmmStackUnitNumGigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumGigEtherPorts.setStatus("current")
_CmmStackUnitNum10GigEtherPorts_Type = Integer32
_CmmStackUnitNum10GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum10GigEtherPorts = _CmmStackUnitNum10GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 23),
    _CmmStackUnitNum10GigEtherPorts_Type()
)
cmmStackUnitNum10GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum10GigEtherPorts.setStatus("current")
_CmmStackUnitNum25GigEtherPorts_Type = Integer32
_CmmStackUnitNum25GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum25GigEtherPorts = _CmmStackUnitNum25GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 24),
    _CmmStackUnitNum25GigEtherPorts_Type()
)
cmmStackUnitNum25GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum25GigEtherPorts.setStatus("current")
_CmmStackUnitNum40GigEtherPorts_Type = Integer32
_CmmStackUnitNum40GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum40GigEtherPorts = _CmmStackUnitNum40GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 25),
    _CmmStackUnitNum40GigEtherPorts_Type()
)
cmmStackUnitNum40GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum40GigEtherPorts.setStatus("current")
_CmmStackUnitNum50GigEtherPorts_Type = Integer32
_CmmStackUnitNum50GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum50GigEtherPorts = _CmmStackUnitNum50GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 26),
    _CmmStackUnitNum50GigEtherPorts_Type()
)
cmmStackUnitNum50GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum50GigEtherPorts.setStatus("current")
_CmmStackUnitNum100GigEtherPorts_Type = Integer32
_CmmStackUnitNum100GigEtherPorts_Object = MibTableColumn
cmmStackUnitNum100GigEtherPorts = _CmmStackUnitNum100GigEtherPorts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 27),
    _CmmStackUnitNum100GigEtherPorts_Type()
)
cmmStackUnitNum100GigEtherPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNum100GigEtherPorts.setStatus("current")
_CmmStackUnitSwitchChipRev_Type = DisplayString
_CmmStackUnitSwitchChipRev_Object = MibTableColumn
cmmStackUnitSwitchChipRev = _CmmStackUnitSwitchChipRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 28),
    _CmmStackUnitSwitchChipRev_Type()
)
cmmStackUnitSwitchChipRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitSwitchChipRev.setStatus("current")
_CmmStackSupportedLabelRevision_Type = DisplayString
_CmmStackSupportedLabelRevision_Object = MibTableColumn
cmmStackSupportedLabelRevision = _CmmStackSupportedLabelRevision_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 29),
    _CmmStackSupportedLabelRevision_Type()
)
cmmStackSupportedLabelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackSupportedLabelRevision.setStatus("current")
_CmmStackUnitSupportedSwitchChipRev_Type = DisplayString
_CmmStackUnitSupportedSwitchChipRev_Object = MibTableColumn
cmmStackUnitSupportedSwitchChipRev = _CmmStackUnitSupportedSwitchChipRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 1, 1, 30),
    _CmmStackUnitSupportedSwitchChipRev_Type()
)
cmmStackUnitSupportedSwitchChipRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitSupportedSwitchChipRev.setStatus("current")
_CmmTransEEPROMTable_Object = MibTable
cmmTransEEPROMTable = _CmmTransEEPROMTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmmTransEEPROMTable.setStatus("current")
_CmmTransEEPROMEntry_Object = MibTableRow
cmmTransEEPROMEntry = _CmmTransEEPROMEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1)
)
cmmTransEEPROMEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmTransIndex"),
)
if mibBuilder.loadTexts:
    cmmTransEEPROMEntry.setStatus("current")
_CmmTransIndex_Type = Integer32
_CmmTransIndex_Object = MibTableColumn
cmmTransIndex = _CmmTransIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 1),
    _CmmTransIndex_Type()
)
cmmTransIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmTransIndex.setStatus("current")


class _CmmTransType_Type(Integer32):
    """Custom type cmmTransType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sfp", 1),
          ("qsfp", 2),
          ("unknown", 3))
    )


_CmmTransType_Type.__name__ = "Integer32"
_CmmTransType_Object = MibTableColumn
cmmTransType = _CmmTransType_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 2),
    _CmmTransType_Type()
)
cmmTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransType.setStatus("current")
_CmmTransNoOfChannels_Type = Integer32
_CmmTransNoOfChannels_Object = MibTableColumn
cmmTransNoOfChannels = _CmmTransNoOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 3),
    _CmmTransNoOfChannels_Type()
)
cmmTransNoOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransNoOfChannels.setStatus("current")


class _CmmTransidentifier_Type(Integer32):
    """Custom type cmmTransidentifier based on Integer32"""
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("gbic", 2),
          ("soldered-to-motherboard", 3),
          ("sfp-or-sfpplus-or-sfp28", 4),
          ("xbi-300pin", 5),
          ("xenpak", 6),
          ("xep", 7),
          ("xff", 8),
          ("xfpe", 9),
          ("xpak", 10),
          ("x2", 11),
          ("dwdmsfp-or-dwdmsfpplus", 12),
          ("qsfp", 13),
          ("qsfpplus-or-later", 14),
          ("cxp-or-later", 15),
          ("shielded-mini-multilane-hd4x", 16),
          ("shielded-mini-multilane-hd8x", 17),
          ("qsfp28-or-later", 18),
          ("cxp2-aka-cxp28-or-later", 19),
          ("cdfpstyle1-or-cdfpstyle2", 20),
          ("shielded-mini-multilane-hd4x-fanoutcable", 21),
          ("shielded-mini-multilane-hd8x-fanoutcable", 22),
          ("cdfpstyle3", 23),
          ("microqsfp", 24),
          ("qsfp-doubledensity-8x-pluggable-transceiver", 25),
          ("reserved", 26),
          ("vendor-specific", 27))
    )


_CmmTransidentifier_Type.__name__ = "Integer32"
_CmmTransidentifier_Object = MibTableColumn
cmmTransidentifier = _CmmTransidentifier_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 4),
    _CmmTransidentifier_Type()
)
cmmTransidentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransidentifier.setStatus("current")


class _CmmTransSFPextendedidentifier_Type(Integer32):
    """Custom type cmmTransSFPextendedidentifier based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("gbic-notspecified-or-compliant-with-moddef", 1),
          ("gbic-compliant-with-moddef1", 2),
          ("gbic-compliant-with-moddef2", 3),
          ("gbic-compliant-with-moddef3", 4),
          ("gbic-or-sfp-definedby-twowire-interfaceid-only", 5),
          ("gbic-compliant-with-moddef5", 6),
          ("gbic-compliant-with-moddef6", 7),
          ("gbic-compliant-with-moddef7", 8),
          ("unallocated", 9),
          ("unknown", 10))
    )


_CmmTransSFPextendedidentifier_Type.__name__ = "Integer32"
_CmmTransSFPextendedidentifier_Object = MibTableColumn
cmmTransSFPextendedidentifier = _CmmTransSFPextendedidentifier_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 5),
    _CmmTransSFPextendedidentifier_Type()
)
cmmTransSFPextendedidentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPextendedidentifier.setStatus("current")


class _CmmTransQSFPextendedidentifier_Type(Bits):
    """Custom type cmmTransQSFPextendedidentifier based on Bits"""
    namedValues = NamedValues(
        *(("powerclass1-1dot5wmax", 0),
          ("powerclass2-2wmax", 1),
          ("powerclass3-2dot5wmax", 2),
          ("powerclass4-3dot5wmax", 3),
          ("cleicode-present", 4),
          ("cdrpresent-in-tx", 5),
          ("cdrpresent-in-rx", 6),
          ("powerclass5-4wmax", 7),
          ("powerclass6-4dot5wmax", 8),
          ("powerclass7-5wmax", 9))
    )

_CmmTransQSFPextendedidentifier_Type.__name__ = "Bits"
_CmmTransQSFPextendedidentifier_Object = MibTableColumn
cmmTransQSFPextendedidentifier = _CmmTransQSFPextendedidentifier_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 6),
    _CmmTransQSFPextendedidentifier_Type()
)
cmmTransQSFPextendedidentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransQSFPextendedidentifier.setStatus("current")


class _CmmTransconnectortype_Type(Integer32):
    """Custom type cmmTransconnectortype based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("subscriber-connector", 2),
          ("fibrechannel-style1-copperconnector", 3),
          ("fibrechannel-style2-copperconnector", 4),
          ("bayonet-or-threaded-neill-concelman", 5),
          ("fibrechannel-coaxheaders", 6),
          ("fiber-jack", 7),
          ("lucent-connector", 8),
          ("mechanical-transfer-registeredjack", 9),
          ("multiple-optical", 10),
          ("sg", 11),
          ("optical-pigtail", 12),
          ("multifiber-paralleloptic-1x12", 13),
          ("multifiber-paralleloptic-1x16", 14),
          ("hssdcii", 16),
          ("copper-pigtail", 17),
          ("rj45", 18),
          ("no-separable-connector", 19),
          ("mxc2-x16", 20),
          ("reserved", 21),
          ("vendor-specific", 22))
    )


_CmmTransconnectortype_Type.__name__ = "Integer32"
_CmmTransconnectortype_Object = MibTableColumn
cmmTransconnectortype = _CmmTransconnectortype_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 7),
    _CmmTransconnectortype_Type()
)
cmmTransconnectortype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransconnectortype.setStatus("current")


class _CmmTransEthCompliance_Type(Integer32):
    """Custom type cmmTransEthCompliance based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("ec-unknown", 1),
          ("ec-10gbase-sr", 2),
          ("ec-10gbase-lr", 3),
          ("ec-10gbase-lrm", 4),
          ("ec-10gbase-er", 5),
          ("ec-1000base-sx", 6),
          ("ec-1000base-lx", 7),
          ("ec-1000base-cx", 8),
          ("ec-1000base-t", 9),
          ("ec-100base-lx-or-lx10", 10),
          ("ec-100base-fx", 11),
          ("ec-base-bx10", 12),
          ("ec-base-px", 13),
          ("ec-40gbase-cr4", 14),
          ("ec-40gbase-sr4", 15),
          ("ec-40gbase-lr4", 16),
          ("ec-40g-activecable", 17))
    )


_CmmTransEthCompliance_Type.__name__ = "Integer32"
_CmmTransEthCompliance_Object = MibTableColumn
cmmTransEthCompliance = _CmmTransEthCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 8),
    _CmmTransEthCompliance_Type()
)
cmmTransEthCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransEthCompliance.setStatus("current")


class _CmmTransExtEthCompliance_Type(Bits):
    """Custom type cmmTransExtEthCompliance based on Bits"""
    namedValues = NamedValues(
        *(("eec-unspecified", 0),
          ("eec-100g-activeopticalcable-or-25g-auic2maoc", 1),
          ("eec-100gbase-sr4-or-25gbase-sr", 2),
          ("eec-100gbase-lr4-or-25gbase-lr", 3),
          ("eec-100gbase-er4-or-25gbase-er", 4),
          ("eec-100gbase-sr10", 5),
          ("eec-100g-cwdm4", 6),
          ("eec-100g-psm4-parallelsmf", 7),
          ("eec-100g-activecoppercable-or-25g-auic2macc", 8),
          ("eec-obsolete", 9),
          ("eec-reserved", 10),
          ("eec-100gbase-cr4-or-25gbase-crca-l", 11),
          ("eec-25gbase-crca-s", 12),
          ("eec-25gbase-crca-n", 13),
          ("eec-40gbase-er4", 14),
          ("eec-4x10gbase-sr", 15),
          ("eec-40g-psm4-parallelsmf", 16),
          ("eec-g959-dot1-profilep1-i1-2d1", 17),
          ("eec-g959-dot1-profilep1-s1-2d2", 18),
          ("eec-g959-dot1-profilep1-l1-2d2", 19),
          ("eec-100gbase-t-with-sfi-electricalinterface", 20),
          ("eec-100g-clr4", 21),
          ("eec-100g-aoc-or-25g-auic2maoc", 22),
          ("eec-100g-acc-or-25g-auic2macc", 23),
          ("eec-100ge-dwdm2", 24))
    )

_CmmTransExtEthCompliance_Type.__name__ = "Bits"
_CmmTransExtEthCompliance_Object = MibTableColumn
cmmTransExtEthCompliance = _CmmTransExtEthCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 9),
    _CmmTransExtEthCompliance_Type()
)
cmmTransExtEthCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransExtEthCompliance.setStatus("current")


class _CmmTransSonetCompliance_Type(Bits):
    """Custom type cmmTransSonetCompliance based on Bits"""
    namedValues = NamedValues(
        *(("oc192-shortreach", 0),
          ("sonet-reachspecifier-bit1", 1),
          ("sonet-reachspecifier-bit2", 2),
          ("oc48-longreach", 3),
          ("oc48-intermediatereach", 4),
          ("oc48-shortreach", 5),
          ("oc12-singlemode-longreach", 6),
          ("oc12-singlemode-intermediatereach", 7),
          ("oc12-singlemode-shortreach", 8),
          ("oc3-singlemode-longreach", 9),
          ("oc3-singlemode-intermediatereach", 10),
          ("oc3-singlemode-shortreach", 11))
    )

_CmmTransSonetCompliance_Type.__name__ = "Bits"
_CmmTransSonetCompliance_Object = MibTableColumn
cmmTransSonetCompliance = _CmmTransSonetCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 10),
    _CmmTransSonetCompliance_Type()
)
cmmTransSonetCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSonetCompliance.setStatus("current")


class _CmmTransFiberChnlLinkLen_Type(Bits):
    """Custom type cmmTransFiberChnlLinkLen based on Bits"""
    namedValues = NamedValues(
        *(("short", 0),
          ("medium", 1),
          ("intermediate", 2),
          ("long", 3),
          ("verylong", 4))
    )

_CmmTransFiberChnlLinkLen_Type.__name__ = "Bits"
_CmmTransFiberChnlLinkLen_Object = MibTableColumn
cmmTransFiberChnlLinkLen = _CmmTransFiberChnlLinkLen_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 11),
    _CmmTransFiberChnlLinkLen_Type()
)
cmmTransFiberChnlLinkLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFiberChnlLinkLen.setStatus("current")


class _CmmTransFiberChnlTransTech_Type(Bits):
    """Custom type cmmTransFiberChnlTransTech based on Bits"""
    namedValues = NamedValues(
        *(("shortwaveLaserLinearRx", 0),
          ("longwaveLaserLC", 1),
          ("electricalInter-Enclosure", 2),
          ("electricalIntra-Enclosure", 3),
          ("shortwaveLaserWithOutOFC", 4),
          ("shortwaveLaserwithOFC", 5),
          ("longwaveLaserLL", 6))
    )

_CmmTransFiberChnlTransTech_Type.__name__ = "Bits"
_CmmTransFiberChnlTransTech_Object = MibTableColumn
cmmTransFiberChnlTransTech = _CmmTransFiberChnlTransTech_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 12),
    _CmmTransFiberChnlTransTech_Type()
)
cmmTransFiberChnlTransTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFiberChnlTransTech.setStatus("current")


class _CmmTransFiberChnlTransMedia_Type(Bits):
    """Custom type cmmTransFiberChnlTransMedia based on Bits"""
    namedValues = NamedValues(
        *(("twinaxial-pair", 0),
          ("twisted-pair", 1),
          ("miniature-coax", 2),
          ("video-coax", 3),
          ("multi-mode62dot5m", 4),
          ("multi-mode50m", 5),
          ("multi-mode50um", 6),
          ("single-mode", 7))
    )

_CmmTransFiberChnlTransMedia_Type.__name__ = "Bits"
_CmmTransFiberChnlTransMedia_Object = MibTableColumn
cmmTransFiberChnlTransMedia = _CmmTransFiberChnlTransMedia_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 13),
    _CmmTransFiberChnlTransMedia_Type()
)
cmmTransFiberChnlTransMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransFiberChnlTransMedia.setStatus("current")


class _CmmTransSFPFiberChnlSpeed_Type(Bits):
    """Custom type cmmTransSFPFiberChnlSpeed based on Bits"""
    namedValues = NamedValues(
        *(("fcs-3200mbps", 0),
          ("fcs-1600mbps", 1),
          ("fcs-1200mbps", 2),
          ("fcs-800mbps", 3),
          ("fcs-400mbps", 4),
          ("fcs-200mbps", 5),
          ("fcs-100mbps", 6))
    )

_CmmTransSFPFiberChnlSpeed_Type.__name__ = "Bits"
_CmmTransSFPFiberChnlSpeed_Object = MibTableColumn
cmmTransSFPFiberChnlSpeed = _CmmTransSFPFiberChnlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 14),
    _CmmTransSFPFiberChnlSpeed_Type()
)
cmmTransSFPFiberChnlSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPFiberChnlSpeed.setStatus("current")


class _CmmTransQSFPFiberChnlSpeed_Type(Bits):
    """Custom type cmmTransQSFPFiberChnlSpeed based on Bits"""
    namedValues = NamedValues(
        *(("fcs-3200mbps", 0),
          ("fcs-1600mbps", 1),
          ("fcs-1200mbps", 2),
          ("fcs-800mbps", 3),
          ("fcs-400mbps", 4),
          ("fcs-200mbps", 5),
          ("fcs-100mbps", 6))
    )

_CmmTransQSFPFiberChnlSpeed_Type.__name__ = "Bits"
_CmmTransQSFPFiberChnlSpeed_Object = MibTableColumn
cmmTransQSFPFiberChnlSpeed = _CmmTransQSFPFiberChnlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 15),
    _CmmTransQSFPFiberChnlSpeed_Type()
)
cmmTransQSFPFiberChnlSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransQSFPFiberChnlSpeed.setStatus("current")


class _CmmTransSFPInfiniBandCompliance_Type(Integer32):
    """Custom type cmmTransSFPInfiniBandCompliance based on Integer32"""
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
        *(("ibc-1xsx", 1),
          ("ibc-1xlx", 2),
          ("ibc-1xcopperactive", 3),
          ("ibc-1xcopperpassive", 4),
          ("ibc-unknown", 5),
          ("ibc-notapplicable", 6))
    )


_CmmTransSFPInfiniBandCompliance_Type.__name__ = "Integer32"
_CmmTransSFPInfiniBandCompliance_Object = MibTableColumn
cmmTransSFPInfiniBandCompliance = _CmmTransSFPInfiniBandCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 16),
    _CmmTransSFPInfiniBandCompliance_Type()
)
cmmTransSFPInfiniBandCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPInfiniBandCompliance.setStatus("current")


class _CmmTransSFPEsconCompliance_Type(Integer32):
    """Custom type cmmTransSFPEsconCompliance based on Integer32"""
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
        *(("escon-mmf-1310nm-led", 1),
          ("escon-smf-1310nm-laser", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmTransSFPEsconCompliance_Type.__name__ = "Integer32"
_CmmTransSFPEsconCompliance_Object = MibTableColumn
cmmTransSFPEsconCompliance = _CmmTransSFPEsconCompliance_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 17),
    _CmmTransSFPEsconCompliance_Type()
)
cmmTransSFPEsconCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPEsconCompliance.setStatus("current")


class _CmmTransSfpPlusCableTech_Type(Integer32):
    """Custom type cmmTransSfpPlusCableTech based on Integer32"""
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
        *(("active", 1),
          ("passive", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmTransSfpPlusCableTech_Type.__name__ = "Integer32"
_CmmTransSfpPlusCableTech_Object = MibTableColumn
cmmTransSfpPlusCableTech = _CmmTransSfpPlusCableTech_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 18),
    _CmmTransSfpPlusCableTech_Type()
)
cmmTransSfpPlusCableTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSfpPlusCableTech.setStatus("current")


class _CmmTransEncoding_Type(Integer32):
    """Custom type cmmTransEncoding based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("enc-unspecified", 1),
          ("enc-8b-or-10b", 2),
          ("enc-4b-or-5b", 3),
          ("enc-nrz", 4),
          ("enc-manchester", 5),
          ("enc-sonet-scrambled", 6),
          ("enc-64b-or-66b", 7),
          ("enc-256b-or-257b", 8),
          ("enc-pam4", 9),
          ("enc-reserved", 10))
    )


_CmmTransEncoding_Type.__name__ = "Integer32"
_CmmTransEncoding_Object = MibTableColumn
cmmTransEncoding = _CmmTransEncoding_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 19),
    _CmmTransEncoding_Type()
)
cmmTransEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransEncoding.setStatus("current")
_CmmTransLengthKmtrs_Type = Integer32
_CmmTransLengthKmtrs_Object = MibTableColumn
cmmTransLengthKmtrs = _CmmTransLengthKmtrs_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 20),
    _CmmTransLengthKmtrs_Type()
)
cmmTransLengthKmtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthKmtrs.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthKmtrs.setUnits("km")
_CmmTransLengthMtrs_Type = Integer32
_CmmTransLengthMtrs_Object = MibTableColumn
cmmTransLengthMtrs = _CmmTransLengthMtrs_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 21),
    _CmmTransLengthMtrs_Type()
)
cmmTransLengthMtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthMtrs.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthMtrs.setUnits("100 m")
_CmmTransLengthOM1_Type = Integer32
_CmmTransLengthOM1_Object = MibTableColumn
cmmTransLengthOM1 = _CmmTransLengthOM1_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 22),
    _CmmTransLengthOM1_Type()
)
cmmTransLengthOM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthOM1.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthOM1.setUnits("10 m")
_CmmTransLengthOM2_Type = Integer32
_CmmTransLengthOM2_Object = MibTableColumn
cmmTransLengthOM2 = _CmmTransLengthOM2_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 23),
    _CmmTransLengthOM2_Type()
)
cmmTransLengthOM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthOM2.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthOM2.setUnits("10 m")
_CmmTransLengthOM3_Type = Integer32
_CmmTransLengthOM3_Object = MibTableColumn
cmmTransLengthOM3 = _CmmTransLengthOM3_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 24),
    _CmmTransLengthOM3_Type()
)
cmmTransLengthOM3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthOM3.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthOM3.setUnits("10 m")
_CmmTransLengthOM4_Type = Integer32
_CmmTransLengthOM4_Object = MibTableColumn
cmmTransLengthOM4 = _CmmTransLengthOM4_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 25),
    _CmmTransLengthOM4_Type()
)
cmmTransLengthOM4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLengthOM4.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLengthOM4.setUnits("10 m")
_CmmTransVendorName_Type = DisplayString
_CmmTransVendorName_Object = MibTableColumn
cmmTransVendorName = _CmmTransVendorName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 26),
    _CmmTransVendorName_Type()
)
cmmTransVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorName.setStatus("current")
_CmmTransVendorOUI_Type = DisplayString
_CmmTransVendorOUI_Object = MibTableColumn
cmmTransVendorOUI = _CmmTransVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 27),
    _CmmTransVendorOUI_Type()
)
cmmTransVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorOUI.setStatus("current")
_CmmTransVendorPartNumber_Type = DisplayString
_CmmTransVendorPartNumber_Object = MibTableColumn
cmmTransVendorPartNumber = _CmmTransVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 28),
    _CmmTransVendorPartNumber_Type()
)
cmmTransVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorPartNumber.setStatus("current")
_CmmTransVendorRevision_Type = DisplayString
_CmmTransVendorRevision_Object = MibTableColumn
cmmTransVendorRevision = _CmmTransVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 29),
    _CmmTransVendorRevision_Type()
)
cmmTransVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorRevision.setStatus("current")


class _CmmTransCheckCode_Type(OctetString):
    """Custom type cmmTransCheckCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_CmmTransCheckCode_Type.__name__ = "OctetString"
_CmmTransCheckCode_Object = MibTableColumn
cmmTransCheckCode = _CmmTransCheckCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 30),
    _CmmTransCheckCode_Type()
)
cmmTransCheckCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransCheckCode.setStatus("current")


class _CmmTransCheckCodeExtended_Type(OctetString):
    """Custom type cmmTransCheckCodeExtended based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_CmmTransCheckCodeExtended_Type.__name__ = "OctetString"
_CmmTransCheckCodeExtended_Object = MibTableColumn
cmmTransCheckCodeExtended = _CmmTransCheckCodeExtended_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 31),
    _CmmTransCheckCodeExtended_Type()
)
cmmTransCheckCodeExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransCheckCodeExtended.setStatus("current")
_CmmTransNominalBitRate_Type = Integer32
_CmmTransNominalBitRate_Object = MibTableColumn
cmmTransNominalBitRate = _CmmTransNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 32),
    _CmmTransNominalBitRate_Type()
)
cmmTransNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransNominalBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransNominalBitRate.setUnits("100MBd")
_CmmTransBitRateMax_Type = Integer32
_CmmTransBitRateMax_Object = MibTableColumn
cmmTransBitRateMax = _CmmTransBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 33),
    _CmmTransBitRateMax_Type()
)
cmmTransBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransBitRateMax.setStatus("current")
_CmmTransBitRateMin_Type = Integer32
_CmmTransBitRateMin_Object = MibTableColumn
cmmTransBitRateMin = _CmmTransBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 34),
    _CmmTransBitRateMin_Type()
)
cmmTransBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransBitRateMin.setStatus("current")
_CmmTransVendorSerialNumber_Type = DisplayString
_CmmTransVendorSerialNumber_Object = MibTableColumn
cmmTransVendorSerialNumber = _CmmTransVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 35),
    _CmmTransVendorSerialNumber_Type()
)
cmmTransVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVendorSerialNumber.setStatus("current")
_CmmTransDateCode_Type = DisplayString
_CmmTransDateCode_Object = MibTableColumn
cmmTransDateCode = _CmmTransDateCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 36),
    _CmmTransDateCode_Type()
)
cmmTransDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransDateCode.setStatus("current")


class _CmmTransDDMSupport_Type(Integer32):
    """Custom type cmmTransDDMSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2),
          ("unknown", 3))
    )


_CmmTransDDMSupport_Type.__name__ = "Integer32"
_CmmTransDDMSupport_Object = MibTableColumn
cmmTransDDMSupport = _CmmTransDDMSupport_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 37),
    _CmmTransDDMSupport_Type()
)
cmmTransDDMSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransDDMSupport.setStatus("current")
_CmmTransMaxCaseTemp_Type = Integer32
_CmmTransMaxCaseTemp_Object = MibTableColumn
cmmTransMaxCaseTemp = _CmmTransMaxCaseTemp_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 38),
    _CmmTransMaxCaseTemp_Type()
)
cmmTransMaxCaseTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransMaxCaseTemp.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransMaxCaseTemp.setUnits(" 0.01 C ")


class _CmmTransSFPOptionsImp_Type(Bits):
    """Custom type cmmTransSFPOptionsImp based on Bits"""
    namedValues = NamedValues(
        *(("reserved", 0),
          ("power-level3", 1),
          ("paging", 2),
          ("internal-retimer-or-cdr", 3),
          ("cooled-laser-transmitter", 4),
          ("power-level2", 5),
          ("power-level1", 6),
          ("linear-receiver-output", 7),
          ("receiver-decision-threshold", 8),
          ("transmitter-wavelength-or-tunable-frequency", 9),
          ("rate-select", 10),
          ("tx-disable", 11),
          ("tx-fault", 12),
          ("rx-loss-of-signal", 13))
    )

_CmmTransSFPOptionsImp_Type.__name__ = "Bits"
_CmmTransSFPOptionsImp_Object = MibTableColumn
cmmTransSFPOptionsImp = _CmmTransSFPOptionsImp_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 39),
    _CmmTransSFPOptionsImp_Type()
)
cmmTransSFPOptionsImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransSFPOptionsImp.setStatus("current")


class _CmmTransQSFPOptionsImp_Type(Bits):
    """Custom type cmmTransQSFPOptionsImp based on Bits"""
    namedValues = NamedValues(
        *(("reserved", 0),
          ("tx-inputequalization-auto-adaptive", 1),
          ("tx-inputequalization-fixed-programmable", 2),
          ("tx-outputemphasis-fixed-programmable", 3),
          ("tx-outputamplitude-fixed-programmable", 4),
          ("tx-cdr-on-or-off-controllable", 5),
          ("tx-cdr-on-or-off-fixed", 6),
          ("rx-cdr-on-or-off-controllable", 7),
          ("rx-cdr-on-or-off-fixed", 8),
          ("tx-cdr-lossoflock", 9),
          ("rx-cdr-lossoflock", 10),
          ("rx-squelch-disable", 11),
          ("rx-output-disable", 12),
          ("tx-squelch-disable", 13),
          ("tx-squelch", 14),
          ("page2-provided", 15),
          ("page1-provided", 16),
          ("rateselect-controllable", 17),
          ("rateselect-fixed", 18),
          ("tx-disable", 19),
          ("tx-fault", 20),
          ("tx-squelch-to-reduce-pave", 21),
          ("tx-squelch-to-reduce-oma", 22),
          ("tx-loss-of-signal", 23))
    )

_CmmTransQSFPOptionsImp_Type.__name__ = "Bits"
_CmmTransQSFPOptionsImp_Object = MibTableColumn
cmmTransQSFPOptionsImp = _CmmTransQSFPOptionsImp_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 40),
    _CmmTransQSFPOptionsImp_Type()
)
cmmTransQSFPOptionsImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransQSFPOptionsImp.setStatus("current")


class _CmmTransPresence_Type(Integer32):
    """Custom type cmmTransPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("notpresent", 2),
          ("unknown", 3))
    )


_CmmTransPresence_Type.__name__ = "Integer32"
_CmmTransPresence_Object = MibTableColumn
cmmTransPresence = _CmmTransPresence_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 2, 1, 41),
    _CmmTransPresence_Type()
)
cmmTransPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransPresence.setStatus("current")
_CmmTransDDMTable_Object = MibTable
cmmTransDDMTable = _CmmTransDDMTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cmmTransDDMTable.setStatus("current")
_CmmTransDDMEntry_Object = MibTableRow
cmmTransDDMEntry = _CmmTransDDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1)
)
cmmTransDDMEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmTransIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
)
if mibBuilder.loadTexts:
    cmmTransDDMEntry.setStatus("current")
_CmmTransChannelIndex_Type = Integer32
_CmmTransChannelIndex_Object = MibTableColumn
cmmTransChannelIndex = _CmmTransChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 1),
    _CmmTransChannelIndex_Type()
)
cmmTransChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmTransChannelIndex.setStatus("current")
_CmmTransTemperature_Type = Integer32
_CmmTransTemperature_Object = MibTableColumn
cmmTransTemperature = _CmmTransTemperature_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 2),
    _CmmTransTemperature_Type()
)
cmmTransTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTemperature.setUnits("0.01 C")
_CmmTransTempCriticalThresholdMin_Type = Integer32
_CmmTransTempCriticalThresholdMin_Object = MibTableColumn
cmmTransTempCriticalThresholdMin = _CmmTransTempCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 3),
    _CmmTransTempCriticalThresholdMin_Type()
)
cmmTransTempCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTempCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTempCriticalThresholdMin.setUnits("0.01 C")
_CmmTransTempCriticalThresholdMax_Type = Integer32
_CmmTransTempCriticalThresholdMax_Object = MibTableColumn
cmmTransTempCriticalThresholdMax = _CmmTransTempCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 4),
    _CmmTransTempCriticalThresholdMax_Type()
)
cmmTransTempCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTempCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTempCriticalThresholdMax.setUnits("0.01 C")
_CmmTransTempAlertThresholdMin_Type = Integer32
_CmmTransTempAlertThresholdMin_Object = MibTableColumn
cmmTransTempAlertThresholdMin = _CmmTransTempAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 5),
    _CmmTransTempAlertThresholdMin_Type()
)
cmmTransTempAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTempAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTempAlertThresholdMin.setUnits("0.01 C")
_CmmTransTempAlertThresholdMax_Type = Integer32
_CmmTransTempAlertThresholdMax_Object = MibTableColumn
cmmTransTempAlertThresholdMax = _CmmTransTempAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 6),
    _CmmTransTempAlertThresholdMax_Type()
)
cmmTransTempAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTempAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTempAlertThresholdMax.setUnits("0.01 C")
_CmmTransVoltage_Type = Integer32
_CmmTransVoltage_Object = MibTableColumn
cmmTransVoltage = _CmmTransVoltage_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 7),
    _CmmTransVoltage_Type()
)
cmmTransVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltage.setUnits("0.001 V")
_CmmTransVoltCriticalThresholdMin_Type = Integer32
_CmmTransVoltCriticalThresholdMin_Object = MibTableColumn
cmmTransVoltCriticalThresholdMin = _CmmTransVoltCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 8),
    _CmmTransVoltCriticalThresholdMin_Type()
)
cmmTransVoltCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltCriticalThresholdMin.setUnits("0.001 V")
_CmmTransVoltCriticalThresholdMax_Type = Integer32
_CmmTransVoltCriticalThresholdMax_Object = MibTableColumn
cmmTransVoltCriticalThresholdMax = _CmmTransVoltCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 9),
    _CmmTransVoltCriticalThresholdMax_Type()
)
cmmTransVoltCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltCriticalThresholdMax.setUnits("0.001 V")
_CmmTransVoltAlertThresholdMin_Type = Integer32
_CmmTransVoltAlertThresholdMin_Object = MibTableColumn
cmmTransVoltAlertThresholdMin = _CmmTransVoltAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 10),
    _CmmTransVoltAlertThresholdMin_Type()
)
cmmTransVoltAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltAlertThresholdMin.setUnits("0.001 V")
_CmmTransVoltAlertThresholdMax_Type = Integer32
_CmmTransVoltAlertThresholdMax_Object = MibTableColumn
cmmTransVoltAlertThresholdMax = _CmmTransVoltAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 11),
    _CmmTransVoltAlertThresholdMax_Type()
)
cmmTransVoltAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransVoltAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransVoltAlertThresholdMax.setUnits("0.001 V")
_CmmTransLaserBiasCurrent_Type = Integer32
_CmmTransLaserBiasCurrent_Object = MibTableColumn
cmmTransLaserBiasCurrent = _CmmTransLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 12),
    _CmmTransLaserBiasCurrent_Type()
)
cmmTransLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrent.setUnits("0.001 mA")
_CmmTransLaserBiasCurrCriticalThresholdMin_Type = Integer32
_CmmTransLaserBiasCurrCriticalThresholdMin_Object = MibTableColumn
cmmTransLaserBiasCurrCriticalThresholdMin = _CmmTransLaserBiasCurrCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 13),
    _CmmTransLaserBiasCurrCriticalThresholdMin_Type()
)
cmmTransLaserBiasCurrCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrCriticalThresholdMin.setUnits("0.001 mA")
_CmmTransLaserBiasCurrCriticalThresholdMax_Type = Integer32
_CmmTransLaserBiasCurrCriticalThresholdMax_Object = MibTableColumn
cmmTransLaserBiasCurrCriticalThresholdMax = _CmmTransLaserBiasCurrCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 14),
    _CmmTransLaserBiasCurrCriticalThresholdMax_Type()
)
cmmTransLaserBiasCurrCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrCriticalThresholdMax.setUnits("0.001 mA")
_CmmTransLaserBiasCurrAlertThresholdMin_Type = Integer32
_CmmTransLaserBiasCurrAlertThresholdMin_Object = MibTableColumn
cmmTransLaserBiasCurrAlertThresholdMin = _CmmTransLaserBiasCurrAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 15),
    _CmmTransLaserBiasCurrAlertThresholdMin_Type()
)
cmmTransLaserBiasCurrAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrAlertThresholdMin.setUnits("0.001 mA")
_CmmTransLaserBiasCurrAlertThresholdMax_Type = Integer32
_CmmTransLaserBiasCurrAlertThresholdMax_Object = MibTableColumn
cmmTransLaserBiasCurrAlertThresholdMax = _CmmTransLaserBiasCurrAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 16),
    _CmmTransLaserBiasCurrAlertThresholdMax_Type()
)
cmmTransLaserBiasCurrAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransLaserBiasCurrAlertThresholdMax.setUnits("0.001 mA")
_CmmTransTxPower_Type = Integer32
_CmmTransTxPower_Object = MibTableColumn
cmmTransTxPower = _CmmTransTxPower_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 17),
    _CmmTransTxPower_Type()
)
cmmTransTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPower.setUnits("0.001 dBm")
_CmmTransTxPowerCriticalThresholdMin_Type = Integer32
_CmmTransTxPowerCriticalThresholdMin_Object = MibTableColumn
cmmTransTxPowerCriticalThresholdMin = _CmmTransTxPowerCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 18),
    _CmmTransTxPowerCriticalThresholdMin_Type()
)
cmmTransTxPowerCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPowerCriticalThresholdMin.setUnits("0.001 dBm")
_CmmTransTxPowerCriticalThresholdMax_Type = Integer32
_CmmTransTxPowerCriticalThresholdMax_Object = MibTableColumn
cmmTransTxPowerCriticalThresholdMax = _CmmTransTxPowerCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 19),
    _CmmTransTxPowerCriticalThresholdMax_Type()
)
cmmTransTxPowerCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPowerCriticalThresholdMax.setUnits("0.001 dBm")
_CmmTransTxPowerAlertThresholdMin_Type = Integer32
_CmmTransTxPowerAlertThresholdMin_Object = MibTableColumn
cmmTransTxPowerAlertThresholdMin = _CmmTransTxPowerAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 20),
    _CmmTransTxPowerAlertThresholdMin_Type()
)
cmmTransTxPowerAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPowerAlertThresholdMin.setUnits("0.001 dBm")
_CmmTransTxPowerAlertThresholdMax_Type = Integer32
_CmmTransTxPowerAlertThresholdMax_Object = MibTableColumn
cmmTransTxPowerAlertThresholdMax = _CmmTransTxPowerAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 21),
    _CmmTransTxPowerAlertThresholdMax_Type()
)
cmmTransTxPowerAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransTxPowerAlertThresholdMax.setUnits("0.001 dBm")
_CmmTransRxPower_Type = Integer32
_CmmTransRxPower_Object = MibTableColumn
cmmTransRxPower = _CmmTransRxPower_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 22),
    _CmmTransRxPower_Type()
)
cmmTransRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPower.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPower.setUnits("0.001 dBm")
_CmmTransRxPowerCriticalThresholdMin_Type = Integer32
_CmmTransRxPowerCriticalThresholdMin_Object = MibTableColumn
cmmTransRxPowerCriticalThresholdMin = _CmmTransRxPowerCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 23),
    _CmmTransRxPowerCriticalThresholdMin_Type()
)
cmmTransRxPowerCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPowerCriticalThresholdMin.setUnits("0.001 dBm")
_CmmTransRxPowerCriticalThresholdMax_Type = Integer32
_CmmTransRxPowerCriticalThresholdMax_Object = MibTableColumn
cmmTransRxPowerCriticalThresholdMax = _CmmTransRxPowerCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 24),
    _CmmTransRxPowerCriticalThresholdMax_Type()
)
cmmTransRxPowerCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPowerCriticalThresholdMax.setUnits("0.001 dBm")
_CmmTransRxPowerAlertThresholdMin_Type = Integer32
_CmmTransRxPowerAlertThresholdMin_Object = MibTableColumn
cmmTransRxPowerAlertThresholdMin = _CmmTransRxPowerAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 25),
    _CmmTransRxPowerAlertThresholdMin_Type()
)
cmmTransRxPowerAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPowerAlertThresholdMin.setUnits("0.001 dBm")
_CmmTransRxPowerAlertThresholdMax_Type = Integer32
_CmmTransRxPowerAlertThresholdMax_Object = MibTableColumn
cmmTransRxPowerAlertThresholdMax = _CmmTransRxPowerAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 26),
    _CmmTransRxPowerAlertThresholdMax_Type()
)
cmmTransRxPowerAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmTransRxPowerAlertThresholdMax.setUnits("0.001 dBm")


class _CmmTransTxPowerSupported_Type(Integer32):
    """Custom type cmmTransTxPowerSupported based on Integer32"""
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
        *(("supported", 1),
          ("unsupported", 2),
          ("notapplicable", 3),
          ("unknown", 4))
    )


_CmmTransTxPowerSupported_Type.__name__ = "Integer32"
_CmmTransTxPowerSupported_Object = MibTableColumn
cmmTransTxPowerSupported = _CmmTransTxPowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 27),
    _CmmTransTxPowerSupported_Type()
)
cmmTransTxPowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxPowerSupported.setStatus("current")


class _CmmTransRxPowerSupported_Type(Integer32):
    """Custom type cmmTransRxPowerSupported based on Integer32"""
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
        *(("supported", 1),
          ("unsupported", 2),
          ("notapplicable", 3),
          ("unknown", 4))
    )


_CmmTransRxPowerSupported_Type.__name__ = "Integer32"
_CmmTransRxPowerSupported_Object = MibTableColumn
cmmTransRxPowerSupported = _CmmTransRxPowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 28),
    _CmmTransRxPowerSupported_Type()
)
cmmTransRxPowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxPowerSupported.setStatus("current")


class _CmmTransDDMStatus_Type(Integer32):
    """Custom type cmmTransDDMStatus based on Integer32"""
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
        *(("active", 1),
          ("activeunsupported", 2),
          ("inactive", 3),
          ("inactiveunsupported", 4),
          ("notapplicable", 5),
          ("unknown", 6))
    )


_CmmTransDDMStatus_Type.__name__ = "Integer32"
_CmmTransDDMStatus_Object = MibTableColumn
cmmTransDDMStatus = _CmmTransDDMStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 29),
    _CmmTransDDMStatus_Type()
)
cmmTransDDMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransDDMStatus.setStatus("current")


class _CmmTransTxState_Type(Integer32):
    """Custom type cmmTransTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("unknown", 3))
    )


_CmmTransTxState_Type.__name__ = "Integer32"
_CmmTransTxState_Object = MibTableColumn
cmmTransTxState = _CmmTransTxState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 30),
    _CmmTransTxState_Type()
)
cmmTransTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxState.setStatus("current")


class _CmmTransRxLosState_Type(Integer32):
    """Custom type cmmTransRxLosState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("unknown", 3))
    )


_CmmTransRxLosState_Type.__name__ = "Integer32"
_CmmTransRxLosState_Object = MibTableColumn
cmmTransRxLosState = _CmmTransRxLosState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 31),
    _CmmTransRxLosState_Type()
)
cmmTransRxLosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransRxLosState.setStatus("current")


class _CmmTransTxLosState_Type(Integer32):
    """Custom type cmmTransTxLosState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("unknown", 3))
    )


_CmmTransTxLosState_Type.__name__ = "Integer32"
_CmmTransTxLosState_Object = MibTableColumn
cmmTransTxLosState = _CmmTransTxLosState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 32),
    _CmmTransTxLosState_Type()
)
cmmTransTxLosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransTxLosState.setStatus("current")


class _CmmTransResetState_Type(Integer32):
    """Custom type cmmTransResetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2),
          ("unknown", 3))
    )


_CmmTransResetState_Type.__name__ = "Integer32"
_CmmTransResetState_Object = MibTableColumn
cmmTransResetState = _CmmTransResetState_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 33),
    _CmmTransResetState_Type()
)
cmmTransResetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransResetState.setStatus("current")


class _CmmTransPowerMode_Type(Integer32):
    """Custom type cmmTransPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2),
          ("unknown", 3))
    )


_CmmTransPowerMode_Type.__name__ = "Integer32"
_CmmTransPowerMode_Object = MibTableColumn
cmmTransPowerMode = _CmmTransPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 3, 1, 34),
    _CmmTransPowerMode_Type()
)
cmmTransPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmTransPowerMode.setStatus("current")
_CmmSysRamTable_Object = MibTable
cmmSysRamTable = _CmmSysRamTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cmmSysRamTable.setStatus("current")
_CmmSysRamEntry_Object = MibTableRow
cmmSysRamEntry = _CmmSysRamEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1)
)
cmmSysRamEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysRamEntry.setStatus("current")
_CmmSysRamTotalMem_Type = Integer32
_CmmSysRamTotalMem_Object = MibTableColumn
cmmSysRamTotalMem = _CmmSysRamTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 1),
    _CmmSysRamTotalMem_Type()
)
cmmSysRamTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamTotalMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamTotalMem.setUnits(" MBytes ")
_CmmSysRamUsedMem_Type = Integer32
_CmmSysRamUsedMem_Object = MibTableColumn
cmmSysRamUsedMem = _CmmSysRamUsedMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 2),
    _CmmSysRamUsedMem_Type()
)
cmmSysRamUsedMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamUsedMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamUsedMem.setUnits(" % ")
_CmmSysRamFreeMem_Type = Integer32
_CmmSysRamFreeMem_Object = MibTableColumn
cmmSysRamFreeMem = _CmmSysRamFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 3),
    _CmmSysRamFreeMem_Type()
)
cmmSysRamFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamFreeMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamFreeMem.setUnits(" % ")
_CmmSysRamCriticalThreshold_Type = Integer32
_CmmSysRamCriticalThreshold_Object = MibTableColumn
cmmSysRamCriticalThreshold = _CmmSysRamCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 4),
    _CmmSysRamCriticalThreshold_Type()
)
cmmSysRamCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamCriticalThreshold.setUnits(" % ")
_CmmSysRamAlertThreshold_Type = Integer32
_CmmSysRamAlertThreshold_Object = MibTableColumn
cmmSysRamAlertThreshold = _CmmSysRamAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 4, 1, 5),
    _CmmSysRamAlertThreshold_Type()
)
cmmSysRamAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysRamAlertThreshold.setUnits(" % ")
_CmmStackCpuTable_Object = MibTable
cmmStackCpuTable = _CmmStackCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cmmStackCpuTable.setStatus("current")
_CmmStackCpuEntry_Object = MibTableRow
cmmStackCpuEntry = _CmmStackCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1)
)
cmmStackCpuEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmStackCpuEntry.setStatus("current")
_CmmStackUnitNumCpuProcessor_Type = Integer32
_CmmStackUnitNumCpuProcessor_Object = MibTableColumn
cmmStackUnitNumCpuProcessor = _CmmStackUnitNumCpuProcessor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 1),
    _CmmStackUnitNumCpuProcessor_Type()
)
cmmStackUnitNumCpuProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitNumCpuProcessor.setStatus("current")
_CmmStackUnitCpuLoad1Min_Type = Integer32
_CmmStackUnitCpuLoad1Min_Object = MibTableColumn
cmmStackUnitCpuLoad1Min = _CmmStackUnitCpuLoad1Min_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 2),
    _CmmStackUnitCpuLoad1Min_Type()
)
cmmStackUnitCpuLoad1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad1Min.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad1Min.setUnits("0.01 %")
_CmmStackUnitCpuLoad5Min_Type = Integer32
_CmmStackUnitCpuLoad5Min_Object = MibTableColumn
cmmStackUnitCpuLoad5Min = _CmmStackUnitCpuLoad5Min_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 3),
    _CmmStackUnitCpuLoad5Min_Type()
)
cmmStackUnitCpuLoad5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad5Min.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad5Min.setUnits("0.01 %")
_CmmStackUnitCpuLoad15Min_Type = Integer32
_CmmStackUnitCpuLoad15Min_Object = MibTableColumn
cmmStackUnitCpuLoad15Min = _CmmStackUnitCpuLoad15Min_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 4),
    _CmmStackUnitCpuLoad15Min_Type()
)
cmmStackUnitCpuLoad15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad15Min.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuLoad15Min.setUnits("0.01 %")
_CmmStackCpuLoad1minAlertThreshold_Type = Integer32
_CmmStackCpuLoad1minAlertThreshold_Object = MibTableColumn
cmmStackCpuLoad1minAlertThreshold = _CmmStackCpuLoad1minAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 5),
    _CmmStackCpuLoad1minAlertThreshold_Type()
)
cmmStackCpuLoad1minAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCpuLoad1minAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackCpuLoad1minAlertThreshold.setUnits("0.01 %")
_CmmStackCpuLoad1minCriticalThreshold_Type = Integer32
_CmmStackCpuLoad1minCriticalThreshold_Object = MibTableColumn
cmmStackCpuLoad1minCriticalThreshold = _CmmStackCpuLoad1minCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 6),
    _CmmStackCpuLoad1minCriticalThreshold_Type()
)
cmmStackCpuLoad1minCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCpuLoad1minCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackCpuLoad1minCriticalThreshold.setUnits("0.01 %")
_CmmStackCpuLoad5minCriticalThreshold_Type = Integer32
_CmmStackCpuLoad5minCriticalThreshold_Object = MibTableColumn
cmmStackCpuLoad5minCriticalThreshold = _CmmStackCpuLoad5minCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 7),
    _CmmStackCpuLoad5minCriticalThreshold_Type()
)
cmmStackCpuLoad5minCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCpuLoad5minCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackCpuLoad5minCriticalThreshold.setUnits("0.01 %")
_CmmStackCpuLoad15minCriticalThreshold_Type = Integer32
_CmmStackCpuLoad15minCriticalThreshold_Object = MibTableColumn
cmmStackCpuLoad15minCriticalThreshold = _CmmStackCpuLoad15minCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 8),
    _CmmStackCpuLoad15minCriticalThreshold_Type()
)
cmmStackCpuLoad15minCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackCpuLoad15minCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackCpuLoad15minCriticalThreshold.setUnits("0.01 %")
_CmmStackUnitCpuUtilization_Type = Integer32
_CmmStackUnitCpuUtilization_Object = MibTableColumn
cmmStackUnitCpuUtilization = _CmmStackUnitCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 9),
    _CmmStackUnitCpuUtilization_Type()
)
cmmStackUnitCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilization.setUnits("0.01 %")
_CmmStackUnitCpuUtilAlertThreshold_Type = Integer32
_CmmStackUnitCpuUtilAlertThreshold_Object = MibTableColumn
cmmStackUnitCpuUtilAlertThreshold = _CmmStackUnitCpuUtilAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 10),
    _CmmStackUnitCpuUtilAlertThreshold_Type()
)
cmmStackUnitCpuUtilAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilAlertThreshold.setUnits("0.01 %")
_CmmStackUnitCpuUtilCriticalThreshold_Type = Integer32
_CmmStackUnitCpuUtilCriticalThreshold_Object = MibTableColumn
cmmStackUnitCpuUtilCriticalThreshold = _CmmStackUnitCpuUtilCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 5, 1, 11),
    _CmmStackUnitCpuUtilCriticalThreshold_Type()
)
cmmStackUnitCpuUtilCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmStackUnitCpuUtilCriticalThreshold.setUnits("0.01 %")
_CmmSysPowerSupplyTable_Object = MibTable
cmmSysPowerSupplyTable = _CmmSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cmmSysPowerSupplyTable.setStatus("current")
_CmmSysPowerSupplyEntry_Object = MibTableRow
cmmSysPowerSupplyEntry = _CmmSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1)
)
cmmSysPowerSupplyEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
)
if mibBuilder.loadTexts:
    cmmSysPowerSupplyEntry.setStatus("current")
_CmmSysPSUIndex_Type = Integer32
_CmmSysPSUIndex_Object = MibTableColumn
cmmSysPSUIndex = _CmmSysPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 1),
    _CmmSysPSUIndex_Type()
)
cmmSysPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSUIndex.setStatus("current")


class _CmmSysPowerSupplyOperStatus_Type(Integer32):
    """Custom type cmmSysPowerSupplyOperStatus based on Integer32"""
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
        *(("notpresent", 1),
          ("running", 2),
          ("faulty", 3),
          ("unknown", 4))
    )


_CmmSysPowerSupplyOperStatus_Type.__name__ = "Integer32"
_CmmSysPowerSupplyOperStatus_Object = MibTableColumn
cmmSysPowerSupplyOperStatus = _CmmSysPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 2),
    _CmmSysPowerSupplyOperStatus_Type()
)
cmmSysPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPowerSupplyOperStatus.setStatus("current")


class _CmmSysPowerSupplyType_Type(Integer32):
    """Custom type cmmSysPowerSupplyType based on Integer32"""
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
        *(("ac-normal", 1),
          ("ac-reverse", 2),
          ("dc-normal", 3),
          ("dc-reverse", 4),
          ("unknown", 5),
          ("notapplicable", 6))
    )


_CmmSysPowerSupplyType_Type.__name__ = "Integer32"
_CmmSysPowerSupplyType_Object = MibTableColumn
cmmSysPowerSupplyType = _CmmSysPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 3),
    _CmmSysPowerSupplyType_Type()
)
cmmSysPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPowerSupplyType.setStatus("current")


class _CmmSysHotSwapStat_Type(Integer32):
    """Custom type cmmSysHotSwapStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3))
    )


_CmmSysHotSwapStat_Type.__name__ = "Integer32"
_CmmSysHotSwapStat_Object = MibTableColumn
cmmSysHotSwapStat = _CmmSysHotSwapStat_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 4),
    _CmmSysHotSwapStat_Type()
)
cmmSysHotSwapStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHotSwapStat.setStatus("current")
_CmmSysPSConsumption_Type = Integer32
_CmmSysPSConsumption_Object = MibTableColumn
cmmSysPSConsumption = _CmmSysPSConsumption_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 5),
    _CmmSysPSConsumption_Type()
)
cmmSysPSConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSConsumption.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSConsumption.setUnits("0.01 W")
_CmmSysInputPower_Type = Integer32
_CmmSysInputPower_Object = MibTableColumn
cmmSysInputPower = _CmmSysInputPower_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 6),
    _CmmSysInputPower_Type()
)
cmmSysInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputPower.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputPower.setUnits("0.01 W")
_CmmSysInputVoltage_Type = Integer32
_CmmSysInputVoltage_Object = MibTableColumn
cmmSysInputVoltage = _CmmSysInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 7),
    _CmmSysInputVoltage_Type()
)
cmmSysInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputVoltage.setUnits("0.01 V")
_CmmSysOutputVoltage_Type = Integer32
_CmmSysOutputVoltage_Object = MibTableColumn
cmmSysOutputVoltage = _CmmSysOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 8),
    _CmmSysOutputVoltage_Type()
)
cmmSysOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputVoltage.setUnits("0.01 V")
_CmmSysInputCurrent_Type = Integer32
_CmmSysInputCurrent_Object = MibTableColumn
cmmSysInputCurrent = _CmmSysInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 9),
    _CmmSysInputCurrent_Type()
)
cmmSysInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysInputCurrent.setUnits("0.01 A")
_CmmSysOutputCurrent_Type = Integer32
_CmmSysOutputCurrent_Object = MibTableColumn
cmmSysOutputCurrent = _CmmSysOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 10),
    _CmmSysOutputCurrent_Type()
)
cmmSysOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysOutputCurrent.setUnits("0.01 A")
_CmmSysPSTemperature1_Type = Integer32
_CmmSysPSTemperature1_Object = MibTableColumn
cmmSysPSTemperature1 = _CmmSysPSTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 11),
    _CmmSysPSTemperature1_Type()
)
cmmSysPSTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature1.setUnits("0.01 C")
_CmmSysPSTemperature2_Type = Integer32
_CmmSysPSTemperature2_Object = MibTableColumn
cmmSysPSTemperature2 = _CmmSysPSTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 12),
    _CmmSysPSTemperature2_Type()
)
cmmSysPSTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysPSTemperature2.setUnits("0.01 C")
_CmmSysPSFan1Rpm_Type = Integer32
_CmmSysPSFan1Rpm_Object = MibTableColumn
cmmSysPSFan1Rpm = _CmmSysPSFan1Rpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 13),
    _CmmSysPSFan1Rpm_Type()
)
cmmSysPSFan1Rpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSFan1Rpm.setStatus("current")
_CmmSysPSFan2Rpm_Type = Integer32
_CmmSysPSFan2Rpm_Object = MibTableColumn
cmmSysPSFan2Rpm = _CmmSysPSFan2Rpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 14),
    _CmmSysPSFan2Rpm_Type()
)
cmmSysPSFan2Rpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSFan2Rpm.setStatus("current")


class _CmmSysPS12VPg_Type(Integer32):
    """Custom type cmmSysPS12VPg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3))
    )


_CmmSysPS12VPg_Type.__name__ = "Integer32"
_CmmSysPS12VPg_Object = MibTableColumn
cmmSysPS12VPg = _CmmSysPS12VPg_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 15),
    _CmmSysPS12VPg_Type()
)
cmmSysPS12VPg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPS12VPg.setStatus("current")


class _CmmSysPSAcAlert_Type(Integer32):
    """Custom type cmmSysPSAcAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3))
    )


_CmmSysPSAcAlert_Type.__name__ = "Integer32"
_CmmSysPSAcAlert_Object = MibTableColumn
cmmSysPSAcAlert = _CmmSysPSAcAlert_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 16),
    _CmmSysPSAcAlert_Type()
)
cmmSysPSAcAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSAcAlert.setStatus("current")


class _CmmSysPSParamsSupport_Type(Bits):
    """Custom type cmmSysPSParamsSupport based on Bits"""
    namedValues = NamedValues(
        *(("volt-in", 0),
          ("volt-out", 1),
          ("curr-in", 2),
          ("curr-out", 3),
          ("power-in", 4),
          ("power-out", 5),
          ("temp-1", 6),
          ("temp-2", 7),
          ("fan-1", 8),
          ("fan-2", 9))
    )

_CmmSysPSParamsSupport_Type.__name__ = "Bits"
_CmmSysPSParamsSupport_Object = MibTableColumn
cmmSysPSParamsSupport = _CmmSysPSParamsSupport_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 6, 1, 17),
    _CmmSysPSParamsSupport_Type()
)
cmmSysPSParamsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPSParamsSupport.setStatus("current")
_CmmSysPowerRailTable_Object = MibTable
cmmSysPowerRailTable = _CmmSysPowerRailTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cmmSysPowerRailTable.setStatus("current")
_CmmSysPowerRailEntry_Object = MibTableRow
cmmSysPowerRailEntry = _CmmSysPowerRailEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1)
)
cmmSysPowerRailEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysPowerRailEntry.setStatus("current")


class _CmmSysPOWERVDDR_Type(Integer32):
    """Custom type cmmSysPOWERVDDR based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysPOWERVDDR_Type.__name__ = "Integer32"
_CmmSysPOWERVDDR_Object = MibTableColumn
cmmSysPOWERVDDR = _CmmSysPOWERVDDR_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 1),
    _CmmSysPOWERVDDR_Type()
)
cmmSysPOWERVDDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPOWERVDDR.setStatus("current")


class _CmmSysPOWERCORE_Type(Integer32):
    """Custom type cmmSysPOWERCORE based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysPOWERCORE_Type.__name__ = "Integer32"
_CmmSysPOWERCORE_Object = MibTableColumn
cmmSysPOWERCORE = _CmmSysPOWERCORE_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 2),
    _CmmSysPOWERCORE_Type()
)
cmmSysPOWERCORE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPOWERCORE.setStatus("current")


class _CmmSysV1P1POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P1POWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysV1P1POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P1POWERRAIL_Object = MibTableColumn
cmmSysV1P1POWERRAIL = _CmmSysV1P1POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 3),
    _CmmSysV1P1POWERRAIL_Type()
)
cmmSysV1P1POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P1POWERRAIL.setStatus("current")


class _CmmSysMAINBOARDPOWERRAIL_Type(Integer32):
    """Custom type cmmSysMAINBOARDPOWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysMAINBOARDPOWERRAIL_Type.__name__ = "Integer32"
_CmmSysMAINBOARDPOWERRAIL_Object = MibTableColumn
cmmSysMAINBOARDPOWERRAIL = _CmmSysMAINBOARDPOWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 4),
    _CmmSysMAINBOARDPOWERRAIL_Type()
)
cmmSysMAINBOARDPOWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysMAINBOARDPOWERRAIL.setStatus("current")


class _CmmSysV1P05POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P05POWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysV1P05POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P05POWERRAIL_Object = MibTableColumn
cmmSysV1P05POWERRAIL = _CmmSysV1P05POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 5),
    _CmmSysV1P05POWERRAIL_Type()
)
cmmSysV1P05POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P05POWERRAIL.setStatus("current")


class _CmmSysV1P5POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P5POWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysV1P5POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P5POWERRAIL_Object = MibTableColumn
cmmSysV1P5POWERRAIL = _CmmSysV1P5POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 6),
    _CmmSysV1P5POWERRAIL_Type()
)
cmmSysV1P5POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P5POWERRAIL.setStatus("current")


class _CmmSysVCCPOWERRAIL_Type(Integer32):
    """Custom type cmmSysVCCPOWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysVCCPOWERRAIL_Type.__name__ = "Integer32"
_CmmSysVCCPOWERRAIL_Object = MibTableColumn
cmmSysVCCPOWERRAIL = _CmmSysVCCPOWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 7),
    _CmmSysVCCPOWERRAIL_Type()
)
cmmSysVCCPOWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCPOWERRAIL.setStatus("current")


class _CmmSysSBV1P5POWERRAIL_Type(Integer32):
    """Custom type cmmSysSBV1P5POWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysSBV1P5POWERRAIL_Type.__name__ = "Integer32"
_CmmSysSBV1P5POWERRAIL_Object = MibTableColumn
cmmSysSBV1P5POWERRAIL = _CmmSysSBV1P5POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 8),
    _CmmSysSBV1P5POWERRAIL_Type()
)
cmmSysSBV1P5POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysSBV1P5POWERRAIL.setStatus("current")


class _CmmSysV1P0POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P0POWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysV1P0POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P0POWERRAIL_Object = MibTableColumn
cmmSysV1P0POWERRAIL = _CmmSysV1P0POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 9),
    _CmmSysV1P0POWERRAIL_Type()
)
cmmSysV1P0POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P0POWERRAIL.setStatus("current")


class _CmmSysV3P3POWERRAIL_Type(Integer32):
    """Custom type cmmSysV3P3POWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysV3P3POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV3P3POWERRAIL_Object = MibTableColumn
cmmSysV3P3POWERRAIL = _CmmSysV3P3POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 10),
    _CmmSysV3P3POWERRAIL_Type()
)
cmmSysV3P3POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV3P3POWERRAIL.setStatus("current")


class _CmmSysV1P8POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P8POWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysV1P8POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P8POWERRAIL_Object = MibTableColumn
cmmSysV1P8POWERRAIL = _CmmSysV1P8POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 11),
    _CmmSysV1P8POWERRAIL_Type()
)
cmmSysV1P8POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P8POWERRAIL.setStatus("current")


class _CmmSysV1P35POWERRAIL_Type(Integer32):
    """Custom type cmmSysV1P35POWERRAIL based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysV1P35POWERRAIL_Type.__name__ = "Integer32"
_CmmSysV1P35POWERRAIL_Object = MibTableColumn
cmmSysV1P35POWERRAIL = _CmmSysV1P35POWERRAIL_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 12),
    _CmmSysV1P35POWERRAIL_Type()
)
cmmSysV1P35POWERRAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysV1P35POWERRAIL.setStatus("current")


class _CmmSysVCC5V_Type(Integer32):
    """Custom type cmmSysVCC5V based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysVCC5V_Type.__name__ = "Integer32"
_CmmSysVCC5V_Object = MibTableColumn
cmmSysVCC5V = _CmmSysVCC5V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 13),
    _CmmSysVCC5V_Type()
)
cmmSysVCC5V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCC5V.setStatus("current")


class _CmmSysVCC33V_Type(Integer32):
    """Custom type cmmSysVCC33V based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysVCC33V_Type.__name__ = "Integer32"
_CmmSysVCC33V_Object = MibTableColumn
cmmSysVCC33V = _CmmSysVCC33V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 14),
    _CmmSysVCC33V_Type()
)
cmmSysVCC33V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCC33V.setStatus("current")


class _CmmSysVCCMAC1V_Type(Integer32):
    """Custom type cmmSysVCCMAC1V based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysVCCMAC1V_Type.__name__ = "Integer32"
_CmmSysVCCMAC1V_Object = MibTableColumn
cmmSysVCCMAC1V = _CmmSysVCCMAC1V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 15),
    _CmmSysVCCMAC1V_Type()
)
cmmSysVCCMAC1V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCMAC1V.setStatus("current")


class _CmmSysVCCMACAVS1V_Type(Integer32):
    """Custom type cmmSysVCCMACAVS1V based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysVCCMACAVS1V_Type.__name__ = "Integer32"
_CmmSysVCCMACAVS1V_Object = MibTableColumn
cmmSysVCCMACAVS1V = _CmmSysVCCMACAVS1V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 16),
    _CmmSysVCCMACAVS1V_Type()
)
cmmSysVCCMACAVS1V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCMACAVS1V.setStatus("current")


class _CmmSysVCCV1P05_Type(Integer32):
    """Custom type cmmSysVCCV1P05 based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysVCCV1P05_Type.__name__ = "Integer32"
_CmmSysVCCV1P05_Object = MibTableColumn
cmmSysVCCV1P05 = _CmmSysVCCV1P05_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 17),
    _CmmSysVCCV1P05_Type()
)
cmmSysVCCV1P05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCV1P05.setStatus("current")


class _CmmSysVCCV1P5_Type(Integer32):
    """Custom type cmmSysVCCV1P5 based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysVCCV1P5_Type.__name__ = "Integer32"
_CmmSysVCCV1P5_Object = MibTableColumn
cmmSysVCCV1P5 = _CmmSysVCCV1P5_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 18),
    _CmmSysVCCV1P5_Type()
)
cmmSysVCCV1P5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCV1P5.setStatus("current")


class _CmmSysVCCV1P8_Type(Integer32):
    """Custom type cmmSysVCCV1P8 based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysVCCV1P8_Type.__name__ = "Integer32"
_CmmSysVCCV1P8_Object = MibTableColumn
cmmSysVCCV1P8 = _CmmSysVCCV1P8_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 19),
    _CmmSysVCCV1P8_Type()
)
cmmSysVCCV1P8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCV1P8.setStatus("current")


class _CmmSysVCCAVS1V_Type(Integer32):
    """Custom type cmmSysVCCAVS1V based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysVCCAVS1V_Type.__name__ = "Integer32"
_CmmSysVCCAVS1V_Object = MibTableColumn
cmmSysVCCAVS1V = _CmmSysVCCAVS1V_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 20),
    _CmmSysVCCAVS1V_Type()
)
cmmSysVCCAVS1V.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysVCCAVS1V.setStatus("current")


class _CmmSysDDRVTT_Type(Integer32):
    """Custom type cmmSysDDRVTT based on Integer32"""
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
        *(("good", 1),
          ("fail", 2),
          ("unknown", 3),
          ("notapplicable", 4))
    )


_CmmSysDDRVTT_Type.__name__ = "Integer32"
_CmmSysDDRVTT_Object = MibTableColumn
cmmSysDDRVTT = _CmmSysDDRVTT_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 7, 1, 21),
    _CmmSysDDRVTT_Type()
)
cmmSysDDRVTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysDDRVTT.setStatus("current")
_CmmFanTrayTable_Object = MibTable
cmmFanTrayTable = _CmmFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cmmFanTrayTable.setStatus("current")
_CmmFanTrayEntry_Object = MibTableRow
cmmFanTrayEntry = _CmmFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8, 1)
)
cmmFanTrayEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
)
if mibBuilder.loadTexts:
    cmmFanTrayEntry.setStatus("current")
_CmmFanTrayNumber_Type = Integer32
_CmmFanTrayNumber_Object = MibTableColumn
cmmFanTrayNumber = _CmmFanTrayNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8, 1, 1),
    _CmmFanTrayNumber_Type()
)
cmmFanTrayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanTrayNumber.setStatus("current")


class _CmmFanTrayStatus_Type(Integer32):
    """Custom type cmmFanTrayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 1),
          ("present", 2),
          ("unknown", 3))
    )


_CmmFanTrayStatus_Type.__name__ = "Integer32"
_CmmFanTrayStatus_Object = MibTableColumn
cmmFanTrayStatus = _CmmFanTrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8, 1, 2),
    _CmmFanTrayStatus_Type()
)
cmmFanTrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanTrayStatus.setStatus("current")
_CmmFanTrayLedColor_Type = LedColorCode
_CmmFanTrayLedColor_Object = MibTableColumn
cmmFanTrayLedColor = _CmmFanTrayLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 8, 1, 3),
    _CmmFanTrayLedColor_Type()
)
cmmFanTrayLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanTrayLedColor.setStatus("current")
_CmmFanTable_Object = MibTable
cmmFanTable = _CmmFanTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cmmFanTable.setStatus("current")
_CmmFanEntry_Object = MibTableRow
cmmFanEntry = _CmmFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1)
)
cmmFanEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
    (0, "CMM-CHASSIS-MIB", "cmmFanIndex"),
)
if mibBuilder.loadTexts:
    cmmFanEntry.setStatus("current")
_CmmFanIndex_Type = Integer32
_CmmFanIndex_Object = MibTableColumn
cmmFanIndex = _CmmFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 1),
    _CmmFanIndex_Type()
)
cmmFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanIndex.setStatus("current")
_CmmFanRpm_Type = Integer32
_CmmFanRpm_Object = MibTableColumn
cmmFanRpm = _CmmFanRpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 2),
    _CmmFanRpm_Type()
)
cmmFanRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanRpm.setStatus("current")
_CmmFanRpmMin_Type = Integer32
_CmmFanRpmMin_Object = MibTableColumn
cmmFanRpmMin = _CmmFanRpmMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 3),
    _CmmFanRpmMin_Type()
)
cmmFanRpmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanRpmMin.setStatus("current")
_CmmFanRpmMax_Type = Integer32
_CmmFanRpmMax_Object = MibTableColumn
cmmFanRpmMax = _CmmFanRpmMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 4),
    _CmmFanRpmMax_Type()
)
cmmFanRpmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanRpmMax.setStatus("current")


class _CmmFanStatus_Type(Integer32):
    """Custom type cmmFanStatus based on Integer32"""
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
        *(("notpresent", 1),
          ("running", 2),
          ("faulty", 3),
          ("stalled", 4),
          ("unknown", 5))
    )


_CmmFanStatus_Type.__name__ = "Integer32"
_CmmFanStatus_Object = MibTableColumn
cmmFanStatus = _CmmFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 5),
    _CmmFanStatus_Type()
)
cmmFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanStatus.setStatus("current")


class _CmmFanLocation_Type(Integer32):
    """Custom type cmmFanLocation based on Integer32"""
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
        *(("front", 1),
          ("rear", 2),
          ("unknown", 3),
          ("not-applicable", 4))
    )


_CmmFanLocation_Type.__name__ = "Integer32"
_CmmFanLocation_Object = MibTableColumn
cmmFanLocation = _CmmFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 9, 1, 6),
    _CmmFanLocation_Type()
)
cmmFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanLocation.setStatus("current")
_CmmSysTemperatureTable_Object = MibTable
cmmSysTemperatureTable = _CmmSysTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cmmSysTemperatureTable.setStatus("current")
_CmmSysTemperatureEntry_Object = MibTableRow
cmmSysTemperatureEntry = _CmmSysTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1)
)
cmmSysTemperatureEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    cmmSysTemperatureEntry.setStatus("current")
_CmmSysTemperatureSensorIndex_Type = Integer32
_CmmSysTemperatureSensorIndex_Object = MibTableColumn
cmmSysTemperatureSensorIndex = _CmmSysTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 1),
    _CmmSysTemperatureSensorIndex_Type()
)
cmmSysTemperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTemperatureSensorIndex.setStatus("current")
_CmmSysTemperatureSensorName_Type = DisplayString
_CmmSysTemperatureSensorName_Object = MibTableColumn
cmmSysTemperatureSensorName = _CmmSysTemperatureSensorName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 2),
    _CmmSysTemperatureSensorName_Type()
)
cmmSysTemperatureSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTemperatureSensorName.setStatus("current")
_CmmSysTemperatureValue_Type = Integer32
_CmmSysTemperatureValue_Object = MibTableColumn
cmmSysTemperatureValue = _CmmSysTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 3),
    _CmmSysTemperatureValue_Type()
)
cmmSysTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTemperatureValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTemperatureValue.setUnits("0.01 C")
_CmmSysTempEmergencyThresholdMin_Type = Integer32
_CmmSysTempEmergencyThresholdMin_Object = MibTableColumn
cmmSysTempEmergencyThresholdMin = _CmmSysTempEmergencyThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 4),
    _CmmSysTempEmergencyThresholdMin_Type()
)
cmmSysTempEmergencyThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempEmergencyThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempEmergencyThresholdMin.setUnits("0.01 C")
_CmmSysTempEmergencyThresholdMax_Type = Integer32
_CmmSysTempEmergencyThresholdMax_Object = MibTableColumn
cmmSysTempEmergencyThresholdMax = _CmmSysTempEmergencyThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 5),
    _CmmSysTempEmergencyThresholdMax_Type()
)
cmmSysTempEmergencyThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempEmergencyThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempEmergencyThresholdMax.setUnits("0.01 C")
_CmmSysTempAlertThresholdMin_Type = Integer32
_CmmSysTempAlertThresholdMin_Object = MibTableColumn
cmmSysTempAlertThresholdMin = _CmmSysTempAlertThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 6),
    _CmmSysTempAlertThresholdMin_Type()
)
cmmSysTempAlertThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempAlertThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempAlertThresholdMin.setUnits("0.01 C")
_CmmSysTempAlertThresholdMax_Type = Integer32
_CmmSysTempAlertThresholdMax_Object = MibTableColumn
cmmSysTempAlertThresholdMax = _CmmSysTempAlertThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 7),
    _CmmSysTempAlertThresholdMax_Type()
)
cmmSysTempAlertThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempAlertThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempAlertThresholdMax.setUnits("0.01 C")
_CmmSysTempCriticalThresholdMin_Type = Integer32
_CmmSysTempCriticalThresholdMin_Object = MibTableColumn
cmmSysTempCriticalThresholdMin = _CmmSysTempCriticalThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 8),
    _CmmSysTempCriticalThresholdMin_Type()
)
cmmSysTempCriticalThresholdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempCriticalThresholdMin.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempCriticalThresholdMin.setUnits("0.01 C")
_CmmSysTempCriticalThresholdMax_Type = Integer32
_CmmSysTempCriticalThresholdMax_Object = MibTableColumn
cmmSysTempCriticalThresholdMax = _CmmSysTempCriticalThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 10, 1, 9),
    _CmmSysTempCriticalThresholdMax_Type()
)
cmmSysTempCriticalThresholdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTempCriticalThresholdMax.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysTempCriticalThresholdMax.setUnits("0.01 C")
_CmmSysComponentStatusTable_Object = MibTable
cmmSysComponentStatusTable = _CmmSysComponentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cmmSysComponentStatusTable.setStatus("current")
_CmmSysComponentStatusEntry_Object = MibTableRow
cmmSysComponentStatusEntry = _CmmSysComponentStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1)
)
cmmSysComponentStatusEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysComponentStatusEntry.setStatus("current")


class _CmmSysPsu1Status_Type(Integer32):
    """Custom type cmmSysPsu1Status based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysPsu1Status_Type.__name__ = "Integer32"
_CmmSysPsu1Status_Object = MibTableColumn
cmmSysPsu1Status = _CmmSysPsu1Status_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 1),
    _CmmSysPsu1Status_Type()
)
cmmSysPsu1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsu1Status.setStatus("current")
_CmmSysPsu1LedColor_Type = LedColorCode
_CmmSysPsu1LedColor_Object = MibTableColumn
cmmSysPsu1LedColor = _CmmSysPsu1LedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 2),
    _CmmSysPsu1LedColor_Type()
)
cmmSysPsu1LedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsu1LedColor.setStatus("current")


class _CmmSysPsu2Status_Type(Integer32):
    """Custom type cmmSysPsu2Status based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysPsu2Status_Type.__name__ = "Integer32"
_CmmSysPsu2Status_Object = MibTableColumn
cmmSysPsu2Status = _CmmSysPsu2Status_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 3),
    _CmmSysPsu2Status_Type()
)
cmmSysPsu2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsu2Status.setStatus("current")
_CmmSysPsu2LedColor_Type = LedColorCode
_CmmSysPsu2LedColor_Object = MibTableColumn
cmmSysPsu2LedColor = _CmmSysPsu2LedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 4),
    _CmmSysPsu2LedColor_Type()
)
cmmSysPsu2LedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysPsu2LedColor.setStatus("current")


class _CmmSysLocatorLedStatus_Type(Integer32):
    """Custom type cmmSysLocatorLedStatus based on Integer32"""
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
        *(("notpresent", 1),
          ("on", 2),
          ("off", 3),
          ("unknown", 4))
    )


_CmmSysLocatorLedStatus_Type.__name__ = "Integer32"
_CmmSysLocatorLedStatus_Object = MibTableColumn
cmmSysLocatorLedStatus = _CmmSysLocatorLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 5),
    _CmmSysLocatorLedStatus_Type()
)
cmmSysLocatorLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysLocatorLedStatus.setStatus("current")
_CmmSysLocatorLedColor_Type = LedColorCode
_CmmSysLocatorLedColor_Object = MibTableColumn
cmmSysLocatorLedColor = _CmmSysLocatorLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 6),
    _CmmSysLocatorLedColor_Type()
)
cmmSysLocatorLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysLocatorLedColor.setStatus("current")


class _CmmSysMasterLedStatus_Type(Integer32):
    """Custom type cmmSysMasterLedStatus based on Integer32"""
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
        *(("notpresent", 1),
          ("on", 2),
          ("off", 3),
          ("unknown", 4))
    )


_CmmSysMasterLedStatus_Type.__name__ = "Integer32"
_CmmSysMasterLedStatus_Object = MibTableColumn
cmmSysMasterLedStatus = _CmmSysMasterLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 7),
    _CmmSysMasterLedStatus_Type()
)
cmmSysMasterLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysMasterLedStatus.setStatus("current")
_CmmSysMasterLedColor_Type = LedColorCode
_CmmSysMasterLedColor_Object = MibTableColumn
cmmSysMasterLedColor = _CmmSysMasterLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 8),
    _CmmSysMasterLedColor_Type()
)
cmmSysMasterLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysMasterLedColor.setStatus("current")


class _CmmSysFanStatus_Type(Integer32):
    """Custom type cmmSysFanStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysFanStatus_Type.__name__ = "Integer32"
_CmmSysFanStatus_Object = MibTableColumn
cmmSysFanStatus = _CmmSysFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 9),
    _CmmSysFanStatus_Type()
)
cmmSysFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysFanStatus.setStatus("current")
_CmmSysFrontFanLedColor_Type = LedColorCode
_CmmSysFrontFanLedColor_Object = MibTableColumn
cmmSysFrontFanLedColor = _CmmSysFrontFanLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 10),
    _CmmSysFrontFanLedColor_Type()
)
cmmSysFrontFanLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysFrontFanLedColor.setStatus("current")


class _CmmSysRamStatus_Type(Integer32):
    """Custom type cmmSysRamStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysRamStatus_Type.__name__ = "Integer32"
_CmmSysRamStatus_Object = MibTableColumn
cmmSysRamStatus = _CmmSysRamStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 11),
    _CmmSysRamStatus_Type()
)
cmmSysRamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysRamStatus.setStatus("current")


class _CmmSysCpuStatus_Type(Integer32):
    """Custom type cmmSysCpuStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysCpuStatus_Type.__name__ = "Integer32"
_CmmSysCpuStatus_Object = MibTableColumn
cmmSysCpuStatus = _CmmSysCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 12),
    _CmmSysCpuStatus_Type()
)
cmmSysCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysCpuStatus.setStatus("current")


class _CmmSysDiskStatus_Type(Integer32):
    """Custom type cmmSysDiskStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysDiskStatus_Type.__name__ = "Integer32"
_CmmSysDiskStatus_Object = MibTableColumn
cmmSysDiskStatus = _CmmSysDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 13),
    _CmmSysDiskStatus_Type()
)
cmmSysDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysDiskStatus.setStatus("current")


class _CmmSysTemperatureStatus_Type(Integer32):
    """Custom type cmmSysTemperatureStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysTemperatureStatus_Type.__name__ = "Integer32"
_CmmSysTemperatureStatus_Object = MibTableColumn
cmmSysTemperatureStatus = _CmmSysTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 11, 1, 14),
    _CmmSysTemperatureStatus_Type()
)
cmmSysTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysTemperatureStatus.setStatus("current")
_CmmSysSwModuleTable_Object = MibTable
cmmSysSwModuleTable = _CmmSysSwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cmmSysSwModuleTable.setStatus("current")
_CmmSysSwModuleEntry_Object = MibTableRow
cmmSysSwModuleEntry = _CmmSysSwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 12, 1)
)
cmmSysSwModuleEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysSwModuleEntry.setStatus("current")
_CmmSysSwRuntimeImgVersion_Type = DisplayString
_CmmSysSwRuntimeImgVersion_Object = MibTableColumn
cmmSysSwRuntimeImgVersion = _CmmSysSwRuntimeImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 12, 1, 1),
    _CmmSysSwRuntimeImgVersion_Type()
)
cmmSysSwRuntimeImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysSwRuntimeImgVersion.setStatus("current")
_CmmSysSwRuntimeImgDate_Type = DateAndTime
_CmmSysSwRuntimeImgDate_Object = MibTableColumn
cmmSysSwRuntimeImgDate = _CmmSysSwRuntimeImgDate_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 12, 1, 2),
    _CmmSysSwRuntimeImgDate_Type()
)
cmmSysSwRuntimeImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysSwRuntimeImgDate.setStatus("current")
_CmmSwitchTemperatureTable_Object = MibTable
cmmSwitchTemperatureTable = _CmmSwitchTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13)
)
if mibBuilder.loadTexts:
    cmmSwitchTemperatureTable.setStatus("current")
_CmmSwitchTemperatureEntry_Object = MibTableRow
cmmSwitchTemperatureEntry = _CmmSwitchTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13, 1)
)
cmmSwitchTemperatureEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmSwitchTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    cmmSwitchTemperatureEntry.setStatus("current")
_CmmSwitchTemperatureSensorIndex_Type = Integer32
_CmmSwitchTemperatureSensorIndex_Object = MibTableColumn
cmmSwitchTemperatureSensorIndex = _CmmSwitchTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13, 1, 1),
    _CmmSwitchTemperatureSensorIndex_Type()
)
cmmSwitchTemperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSwitchTemperatureSensorIndex.setStatus("current")
_CmmSwitchTemperatureValue_Type = Integer32
_CmmSwitchTemperatureValue_Object = MibTableColumn
cmmSwitchTemperatureValue = _CmmSwitchTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13, 1, 2),
    _CmmSwitchTemperatureValue_Type()
)
cmmSwitchTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSwitchTemperatureValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmSwitchTemperatureValue.setUnits("0.01 C")
_CmmSwitchTempPeakValue_Type = Integer32
_CmmSwitchTempPeakValue_Object = MibTableColumn
cmmSwitchTempPeakValue = _CmmSwitchTempPeakValue_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 13, 1, 3),
    _CmmSwitchTempPeakValue_Type()
)
cmmSwitchTempPeakValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSwitchTempPeakValue.setStatus("current")
if mibBuilder.loadTexts:
    cmmSwitchTempPeakValue.setUnits("0.01 C")
_CmmSysHardDiskTable_Object = MibTable
cmmSysHardDiskTable = _CmmSysHardDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14)
)
if mibBuilder.loadTexts:
    cmmSysHardDiskTable.setStatus("current")
_CmmSysHardDiskEntry_Object = MibTableRow
cmmSysHardDiskEntry = _CmmSysHardDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1)
)
cmmSysHardDiskEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSysHardDiskEntry.setStatus("current")
_CmmSysHarddiskSerialno_Type = DisplayString
_CmmSysHarddiskSerialno_Object = MibTableColumn
cmmSysHarddiskSerialno = _CmmSysHarddiskSerialno_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 1),
    _CmmSysHarddiskSerialno_Type()
)
cmmSysHarddiskSerialno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskSerialno.setStatus("current")
_CmmSysHarddiskModelno_Type = DisplayString
_CmmSysHarddiskModelno_Object = MibTableColumn
cmmSysHarddiskModelno = _CmmSysHarddiskModelno_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 2),
    _CmmSysHarddiskModelno_Type()
)
cmmSysHarddiskModelno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskModelno.setStatus("current")
_CmmSysHarddiskFirmwarerev_Type = DisplayString
_CmmSysHarddiskFirmwarerev_Object = MibTableColumn
cmmSysHarddiskFirmwarerev = _CmmSysHarddiskFirmwarerev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 3),
    _CmmSysHarddiskFirmwarerev_Type()
)
cmmSysHarddiskFirmwarerev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskFirmwarerev.setStatus("current")
_CmmSysHarddiskCylinders_Type = Integer32
_CmmSysHarddiskCylinders_Object = MibTableColumn
cmmSysHarddiskCylinders = _CmmSysHarddiskCylinders_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 4),
    _CmmSysHarddiskCylinders_Type()
)
cmmSysHarddiskCylinders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskCylinders.setStatus("current")
_CmmSysHarddiskHeads_Type = Integer32
_CmmSysHarddiskHeads_Object = MibTableColumn
cmmSysHarddiskHeads = _CmmSysHarddiskHeads_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 5),
    _CmmSysHarddiskHeads_Type()
)
cmmSysHarddiskHeads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskHeads.setStatus("current")
_CmmSysHarddiskSectors_Type = Integer32
_CmmSysHarddiskSectors_Object = MibTableColumn
cmmSysHarddiskSectors = _CmmSysHarddiskSectors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 6),
    _CmmSysHarddiskSectors_Type()
)
cmmSysHarddiskSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskSectors.setStatus("current")
_CmmSysHarddiskUnformattedBytesorTrack_Type = Integer32
_CmmSysHarddiskUnformattedBytesorTrack_Object = MibTableColumn
cmmSysHarddiskUnformattedBytesorTrack = _CmmSysHarddiskUnformattedBytesorTrack_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 7),
    _CmmSysHarddiskUnformattedBytesorTrack_Type()
)
cmmSysHarddiskUnformattedBytesorTrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskUnformattedBytesorTrack.setStatus("current")
_CmmSysHarddiskUnformattedBytesorSector_Type = Integer32
_CmmSysHarddiskUnformattedBytesorSector_Object = MibTableColumn
cmmSysHarddiskUnformattedBytesorSector = _CmmSysHarddiskUnformattedBytesorSector_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 8),
    _CmmSysHarddiskUnformattedBytesorSector_Type()
)
cmmSysHarddiskUnformattedBytesorSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskUnformattedBytesorSector.setStatus("current")
_CmmSysHarddiskRevisionNum_Type = DisplayString
_CmmSysHarddiskRevisionNum_Object = MibTableColumn
cmmSysHarddiskRevisionNum = _CmmSysHarddiskRevisionNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 9),
    _CmmSysHarddiskRevisionNum_Type()
)
cmmSysHarddiskRevisionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskRevisionNum.setStatus("current")
_CmmSysHarddiskTotalsize_Type = Integer32
_CmmSysHarddiskTotalsize_Object = MibTableColumn
cmmSysHarddiskTotalsize = _CmmSysHarddiskTotalsize_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 10),
    _CmmSysHarddiskTotalsize_Type()
)
cmmSysHarddiskTotalsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskTotalsize.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHarddiskTotalsize.setUnits(" MBytes ")
_CmmSysHarddiskUsedMem_Type = Integer32
_CmmSysHarddiskUsedMem_Object = MibTableColumn
cmmSysHarddiskUsedMem = _CmmSysHarddiskUsedMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 11),
    _CmmSysHarddiskUsedMem_Type()
)
cmmSysHarddiskUsedMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskUsedMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHarddiskUsedMem.setUnits(" % ")
_CmmSysHarddiskFreeMem_Type = Integer32
_CmmSysHarddiskFreeMem_Object = MibTableColumn
cmmSysHarddiskFreeMem = _CmmSysHarddiskFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 12),
    _CmmSysHarddiskFreeMem_Type()
)
cmmSysHarddiskFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskFreeMem.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHarddiskFreeMem.setUnits(" % ")
_CmmSysHarddiskCriticalThreshold_Type = Integer32
_CmmSysHarddiskCriticalThreshold_Object = MibTableColumn
cmmSysHarddiskCriticalThreshold = _CmmSysHarddiskCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 13),
    _CmmSysHarddiskCriticalThreshold_Type()
)
cmmSysHarddiskCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHarddiskCriticalThreshold.setUnits(" % ")
_CmmSysHarddiskAlertThreshold_Type = Integer32
_CmmSysHarddiskAlertThreshold_Object = MibTableColumn
cmmSysHarddiskAlertThreshold = _CmmSysHarddiskAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 14, 1, 14),
    _CmmSysHarddiskAlertThreshold_Type()
)
cmmSysHarddiskAlertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysHarddiskAlertThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmmSysHarddiskAlertThreshold.setUnits(" % ")
_CmmSystemStatusTable_Object = MibTable
cmmSystemStatusTable = _CmmSystemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cmmSystemStatusTable.setStatus("current")
_CmmSystemStatusEntry_Object = MibTableRow
cmmSystemStatusEntry = _CmmSystemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1)
)
cmmSystemStatusEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
)
if mibBuilder.loadTexts:
    cmmSystemStatusEntry.setStatus("current")
_CmmSystemMinorFaultStatus_Type = SystemStatusCode
_CmmSystemMinorFaultStatus_Object = MibTableColumn
cmmSystemMinorFaultStatus = _CmmSystemMinorFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1, 1),
    _CmmSystemMinorFaultStatus_Type()
)
cmmSystemMinorFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSystemMinorFaultStatus.setStatus("current")
_CmmSystemMajorFaultStatus_Type = SystemStatusCode
_CmmSystemMajorFaultStatus_Object = MibTableColumn
cmmSystemMajorFaultStatus = _CmmSystemMajorFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1, 2),
    _CmmSystemMajorFaultStatus_Type()
)
cmmSystemMajorFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSystemMajorFaultStatus.setStatus("current")


class _CmmSysStatus_Type(Integer32):
    """Custom type cmmSysStatus based on Integer32"""
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
        *(("normal", 1),
          ("minor-fault", 2),
          ("major-fault", 3),
          ("unknown", 4))
    )


_CmmSysStatus_Type.__name__ = "Integer32"
_CmmSysStatus_Object = MibTableColumn
cmmSysStatus = _CmmSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1, 3),
    _CmmSysStatus_Type()
)
cmmSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysStatus.setStatus("current")
_CmmSysLedColor_Type = LedColorCode
_CmmSysLedColor_Object = MibTableColumn
cmmSysLedColor = _CmmSysLedColor_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 15, 1, 4),
    _CmmSysLedColor_Type()
)
cmmSysLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysLedColor.setStatus("current")
_CmmCpuCoreUtilTable_Object = MibTable
cmmCpuCoreUtilTable = _CmmCpuCoreUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16)
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilTable.setStatus("current")
_CmmCpuCoreUtilEntry_Object = MibTableRow
cmmCpuCoreUtilEntry = _CmmCpuCoreUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16, 1)
)
cmmCpuCoreUtilEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmCpuCoreIndex"),
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilEntry.setStatus("current")
_CmmCpuCoreIndex_Type = Integer32
_CmmCpuCoreIndex_Object = MibTableColumn
cmmCpuCoreIndex = _CmmCpuCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16, 1, 1),
    _CmmCpuCoreIndex_Type()
)
cmmCpuCoreIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmCpuCoreIndex.setStatus("current")
_CmmCpuCoreUtilization_Type = Integer32
_CmmCpuCoreUtilization_Object = MibTableColumn
cmmCpuCoreUtilization = _CmmCpuCoreUtilization_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16, 1, 2),
    _CmmCpuCoreUtilization_Type()
)
cmmCpuCoreUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCpuCoreUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cmmCpuCoreUtilization.setUnits("0.01 %")
_CmmCpuCoreModelName_Type = DisplayString
_CmmCpuCoreModelName_Object = MibTableColumn
cmmCpuCoreModelName = _CmmCpuCoreModelName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 16, 1, 3),
    _CmmCpuCoreModelName_Type()
)
cmmCpuCoreModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmCpuCoreModelName.setStatus("current")
_CmmPsuFruTable_Object = MibTable
cmmPsuFruTable = _CmmPsuFruTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17)
)
if mibBuilder.loadTexts:
    cmmPsuFruTable.setStatus("current")
_CmmPsuFruEntry_Object = MibTableRow
cmmPsuFruEntry = _CmmPsuFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1)
)
cmmPsuFruEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
)
if mibBuilder.loadTexts:
    cmmPsuFruEntry.setStatus("current")
_CmmPsuPpid_Type = DisplayString
_CmmPsuPpid_Object = MibTableColumn
cmmPsuPpid = _CmmPsuPpid_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 1),
    _CmmPsuPpid_Type()
)
cmmPsuPpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPpid.setStatus("current")
_CmmPsuCountryofOrigin_Type = DisplayString
_CmmPsuCountryofOrigin_Object = MibTableColumn
cmmPsuCountryofOrigin = _CmmPsuCountryofOrigin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 2),
    _CmmPsuCountryofOrigin_Type()
)
cmmPsuCountryofOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuCountryofOrigin.setStatus("current")
_CmmPsuPpidPartNum_Type = DisplayString
_CmmPsuPpidPartNum_Object = MibTableColumn
cmmPsuPpidPartNum = _CmmPsuPpidPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 3),
    _CmmPsuPpidPartNum_Type()
)
cmmPsuPpidPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPpidPartNum.setStatus("current")
_CmmPsuPpidPartNumRev_Type = DisplayString
_CmmPsuPpidPartNumRev_Object = MibTableColumn
cmmPsuPpidPartNumRev = _CmmPsuPpidPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 4),
    _CmmPsuPpidPartNumRev_Type()
)
cmmPsuPpidPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPpidPartNumRev.setStatus("current")
_CmmPsuManufactureId_Type = DisplayString
_CmmPsuManufactureId_Object = MibTableColumn
cmmPsuManufactureId = _CmmPsuManufactureId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 5),
    _CmmPsuManufactureId_Type()
)
cmmPsuManufactureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuManufactureId.setStatus("current")


class _CmmPsuDateCode_Type(OctetString):
    """Custom type cmmPsuDateCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )


_CmmPsuDateCode_Type.__name__ = "OctetString"
_CmmPsuDateCode_Object = MibTableColumn
cmmPsuDateCode = _CmmPsuDateCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 6),
    _CmmPsuDateCode_Type()
)
cmmPsuDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuDateCode.setStatus("current")
_CmmPsuSerialNumber_Type = DisplayString
_CmmPsuSerialNumber_Object = MibTableColumn
cmmPsuSerialNumber = _CmmPsuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 7),
    _CmmPsuSerialNumber_Type()
)
cmmPsuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuSerialNumber.setStatus("current")
_CmmPsuPartNum_Type = DisplayString
_CmmPsuPartNum_Object = MibTableColumn
cmmPsuPartNum = _CmmPsuPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 8),
    _CmmPsuPartNum_Type()
)
cmmPsuPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPartNum.setStatus("current")
_CmmPsuPartNumRev_Type = DisplayString
_CmmPsuPartNumRev_Object = MibTableColumn
cmmPsuPartNumRev = _CmmPsuPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 9),
    _CmmPsuPartNumRev_Type()
)
cmmPsuPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuPartNumRev.setStatus("current")
_CmmPsuNumOfFanPerTray_Type = Integer32
_CmmPsuNumOfFanPerTray_Object = MibTableColumn
cmmPsuNumOfFanPerTray = _CmmPsuNumOfFanPerTray_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 10),
    _CmmPsuNumOfFanPerTray_Type()
)
cmmPsuNumOfFanPerTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuNumOfFanPerTray.setStatus("current")


class _CmmPsuType_Type(Integer32):
    """Custom type cmmPsuType based on Integer32"""
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
        *(("ac-normal", 1),
          ("ac-reverse", 2),
          ("dc-normal", 3),
          ("dc-reverse", 4),
          ("not-applicable", 5))
    )


_CmmPsuType_Type.__name__ = "Integer32"
_CmmPsuType_Object = MibTableColumn
cmmPsuType = _CmmPsuType_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 11),
    _CmmPsuType_Type()
)
cmmPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuType.setStatus("current")
_CmmPsuServiceTag_Type = DisplayString
_CmmPsuServiceTag_Object = MibTableColumn
cmmPsuServiceTag = _CmmPsuServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 12),
    _CmmPsuServiceTag_Type()
)
cmmPsuServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuServiceTag.setStatus("current")
_CmmPsuIanaNum_Type = DisplayString
_CmmPsuIanaNum_Object = MibTableColumn
cmmPsuIanaNum = _CmmPsuIanaNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 13),
    _CmmPsuIanaNum_Type()
)
cmmPsuIanaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuIanaNum.setStatus("current")
_CmmPsuFanMaxRpm_Type = Integer32
_CmmPsuFanMaxRpm_Object = MibTableColumn
cmmPsuFanMaxRpm = _CmmPsuFanMaxRpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 14),
    _CmmPsuFanMaxRpm_Type()
)
cmmPsuFanMaxRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuFanMaxRpm.setStatus("current")
_CmmPsuAirFlowDir_Type = DisplayString
_CmmPsuAirFlowDir_Object = MibTableColumn
cmmPsuAirFlowDir = _CmmPsuAirFlowDir_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 15),
    _CmmPsuAirFlowDir_Type()
)
cmmPsuAirFlowDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuAirFlowDir.setStatus("current")
_CmmPsuMaxOutputWatt_Type = Integer32
_CmmPsuMaxOutputWatt_Object = MibTableColumn
cmmPsuMaxOutputWatt = _CmmPsuMaxOutputWatt_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 17, 1, 16),
    _CmmPsuMaxOutputWatt_Type()
)
cmmPsuMaxOutputWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPsuMaxOutputWatt.setStatus("current")
_CmmFanFruTable_Object = MibTable
cmmFanFruTable = _CmmFanFruTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18)
)
if mibBuilder.loadTexts:
    cmmFanFruTable.setStatus("current")
_CmmFanFruEntry_Object = MibTableRow
cmmFanFruEntry = _CmmFanFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1)
)
cmmFanFruEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
)
if mibBuilder.loadTexts:
    cmmFanFruEntry.setStatus("current")
_CmmFanPpid_Type = DisplayString
_CmmFanPpid_Object = MibTableColumn
cmmFanPpid = _CmmFanPpid_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 1),
    _CmmFanPpid_Type()
)
cmmFanPpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPpid.setStatus("current")
_CmmFanCountryofOrigin_Type = DisplayString
_CmmFanCountryofOrigin_Object = MibTableColumn
cmmFanCountryofOrigin = _CmmFanCountryofOrigin_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 2),
    _CmmFanCountryofOrigin_Type()
)
cmmFanCountryofOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanCountryofOrigin.setStatus("current")
_CmmFanPpidPartNum_Type = DisplayString
_CmmFanPpidPartNum_Object = MibTableColumn
cmmFanPpidPartNum = _CmmFanPpidPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 3),
    _CmmFanPpidPartNum_Type()
)
cmmFanPpidPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPpidPartNum.setStatus("current")
_CmmFanPpidPartNumRev_Type = DisplayString
_CmmFanPpidPartNumRev_Object = MibTableColumn
cmmFanPpidPartNumRev = _CmmFanPpidPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 4),
    _CmmFanPpidPartNumRev_Type()
)
cmmFanPpidPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPpidPartNumRev.setStatus("current")
_CmmFanManufactureId_Type = DisplayString
_CmmFanManufactureId_Object = MibTableColumn
cmmFanManufactureId = _CmmFanManufactureId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 5),
    _CmmFanManufactureId_Type()
)
cmmFanManufactureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanManufactureId.setStatus("current")
_CmmFanDateCode_Type = DisplayString
_CmmFanDateCode_Object = MibTableColumn
cmmFanDateCode = _CmmFanDateCode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 6),
    _CmmFanDateCode_Type()
)
cmmFanDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanDateCode.setStatus("current")
_CmmFanSerialNumber_Type = DisplayString
_CmmFanSerialNumber_Object = MibTableColumn
cmmFanSerialNumber = _CmmFanSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 7),
    _CmmFanSerialNumber_Type()
)
cmmFanSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanSerialNumber.setStatus("current")
_CmmFanPartNum_Type = DisplayString
_CmmFanPartNum_Object = MibTableColumn
cmmFanPartNum = _CmmFanPartNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 8),
    _CmmFanPartNum_Type()
)
cmmFanPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPartNum.setStatus("current")
_CmmFanPartNumRev_Type = DisplayString
_CmmFanPartNumRev_Object = MibTableColumn
cmmFanPartNumRev = _CmmFanPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 9),
    _CmmFanPartNumRev_Type()
)
cmmFanPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanPartNumRev.setStatus("current")
_CmmFanNumOfFanPerTray_Type = Integer32
_CmmFanNumOfFanPerTray_Object = MibTableColumn
cmmFanNumOfFanPerTray = _CmmFanNumOfFanPerTray_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 10),
    _CmmFanNumOfFanPerTray_Type()
)
cmmFanNumOfFanPerTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanNumOfFanPerTray.setStatus("current")


class _CmmFanType_Type(Integer32):
    """Custom type cmmFanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blow-outfan", 1),
          ("blow-infan", 2),
          ("not-applicable", 3))
    )


_CmmFanType_Type.__name__ = "Integer32"
_CmmFanType_Object = MibTableColumn
cmmFanType = _CmmFanType_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 11),
    _CmmFanType_Type()
)
cmmFanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanType.setStatus("current")
_CmmFanServiceTag_Type = DisplayString
_CmmFanServiceTag_Object = MibTableColumn
cmmFanServiceTag = _CmmFanServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 12),
    _CmmFanServiceTag_Type()
)
cmmFanServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanServiceTag.setStatus("current")
_CmmFanIanaNum_Type = DisplayString
_CmmFanIanaNum_Object = MibTableColumn
cmmFanIanaNum = _CmmFanIanaNum_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 13),
    _CmmFanIanaNum_Type()
)
cmmFanIanaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanIanaNum.setStatus("current")
_CmmFanMaxRpm_Type = Integer32
_CmmFanMaxRpm_Object = MibTableColumn
cmmFanMaxRpm = _CmmFanMaxRpm_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 18, 1, 14),
    _CmmFanMaxRpm_Type()
)
cmmFanMaxRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFanMaxRpm.setStatus("current")
_CmmSysCpldTable_Object = MibTable
cmmSysCpldTable = _CmmSysCpldTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19)
)
if mibBuilder.loadTexts:
    cmmSysCpldTable.setStatus("current")
_CmmSysCpldEntry_Object = MibTableRow
cmmSysCpldEntry = _CmmSysCpldEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1)
)
cmmSysCpldEntry.setIndexNames(
    (0, "CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
    (0, "CMM-CHASSIS-MIB", "cmmSysCpldIndex"),
)
if mibBuilder.loadTexts:
    cmmSysCpldEntry.setStatus("current")
_CmmSysCpldIndex_Type = Integer32
_CmmSysCpldIndex_Object = MibTableColumn
cmmSysCpldIndex = _CmmSysCpldIndex_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1, 1),
    _CmmSysCpldIndex_Type()
)
cmmSysCpldIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmSysCpldIndex.setStatus("current")
_CmmSysCpldName_Type = DisplayString
_CmmSysCpldName_Object = MibTableColumn
cmmSysCpldName = _CmmSysCpldName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1, 2),
    _CmmSysCpldName_Type()
)
cmmSysCpldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysCpldName.setStatus("current")
_CmmSysCpldSupportedVer_Type = DisplayString
_CmmSysCpldSupportedVer_Object = MibTableColumn
cmmSysCpldSupportedVer = _CmmSysCpldSupportedVer_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1, 3),
    _CmmSysCpldSupportedVer_Type()
)
cmmSysCpldSupportedVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysCpldSupportedVer.setStatus("current")
_CmmSysCpldCurrentVer_Type = DisplayString
_CmmSysCpldCurrentVer_Object = MibTableColumn
cmmSysCpldCurrentVer = _CmmSysCpldCurrentVer_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 2, 19, 1, 4),
    _CmmSysCpldCurrentVer_Type()
)
cmmSysCpldCurrentVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSysCpldCurrentVer.setStatus("current")
_CmmAlarmObjects_ObjectIdentity = ObjectIdentity
cmmAlarmObjects = _CmmAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3)
)
_CmmAlarmVariable_ObjectIdentity = ObjectIdentity
cmmAlarmVariable = _CmmAlarmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 0)
)
_CmmAlarmVarInteger_Type = Integer32
_CmmAlarmVarInteger_Object = MibScalar
cmmAlarmVarInteger = _CmmAlarmVarInteger_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 0, 1),
    _CmmAlarmVarInteger_Type()
)
cmmAlarmVarInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmAlarmVarInteger.setStatus("current")
_CmmAlarmVarString_Type = OctetString
_CmmAlarmVarString_Object = MibScalar
cmmAlarmVarString = _CmmAlarmVarString_Object(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 0, 2),
    _CmmAlarmVarString_Type()
)
cmmAlarmVarString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmmAlarmVarString.setStatus("current")
_CmmAlarmMibNotifications_ObjectIdentity = ObjectIdentity
cmmAlarmMibNotifications = _CmmAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1)
)
_CmmTransMibNotifications_ObjectIdentity = ObjectIdentity
cmmTransMibNotifications = _CmmTransMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2)
)

# Managed Objects groups


# Notification objects

cmmCpuLoad15MinCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 1)
)
cmmCpuLoad15MinCritical.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackCpuLoad15minCriticalThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad15Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad15MinCritical.setStatus(
        "current"
    )

cmmCpuLoad5MinCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 2)
)
cmmCpuLoad5MinCritical.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackCpuLoad5minCriticalThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad5Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad5MinCritical.setStatus(
        "current"
    )

cmmCpuLoad1MinAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 3)
)
cmmCpuLoad1MinAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackCpuLoad1minAlertThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad1Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad1MinAlert.setStatus(
        "current"
    )

cmmCpuLoad1MinCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 4)
)
cmmCpuLoad1MinCritical.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackCpuLoad1minCriticalThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad1Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad1MinCritical.setStatus(
        "current"
    )

cmmCpuLoad1MinAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 5)
)
cmmCpuLoad1MinAlertRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackCpuLoad1minAlertThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad1Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad1MinAlertRecovery.setStatus(
        "current"
    )

cmmCpuLoad15MinCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 6)
)
cmmCpuLoad15MinCriticalRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackCpuLoad15minCriticalThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad15Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad15MinCriticalRecovery.setStatus(
        "current"
    )

cmmCpuLoad5MinCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 7)
)
cmmCpuLoad5MinCriticalRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackCpuLoad5minCriticalThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad5Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad5MinCriticalRecovery.setStatus(
        "current"
    )

cmmCpuLoad1MinCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 8)
)
cmmCpuLoad1MinCriticalRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackCpuLoad1minCriticalThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuLoad1Min"))
)
if mibBuilder.loadTexts:
    cmmCpuLoad1MinCriticalRecovery.setStatus(
        "current"
    )

cmmCpuCoreUtilHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 9)
)
cmmCpuCoreUtilHighAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilAlertThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilization"))
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilHighAlert.setStatus(
        "current"
    )

cmmCpuCoreUtilHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 10)
)
cmmCpuCoreUtilHighCritical.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilCriticalThreshold"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilization"))
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilHighCritical.setStatus(
        "current"
    )

cmmCpuCoreUtilHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 11)
)
cmmCpuCoreUtilHighAlertRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilization"))
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilHighAlertRecovery.setStatus(
        "current"
    )

cmmCpuCoreUtilHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 12)
)
cmmCpuCoreUtilHighCriticalRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmStackUnitCpuUtilization"))
)
if mibBuilder.loadTexts:
    cmmCpuCoreUtilHighCriticalRecovery.setStatus(
        "current"
    )

cmmRamUsageRisingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 21)
)
cmmRamUsageRisingAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysRamUsedMem"),
        ("CMM-CHASSIS-MIB", "cmmSysRamAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmRamUsageRisingAlert.setStatus(
        "current"
    )

cmmRamUsageRisingCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 22)
)
cmmRamUsageRisingCritical.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysRamUsedMem"),
        ("CMM-CHASSIS-MIB", "cmmSysRamCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmRamUsageRisingCritical.setStatus(
        "current"
    )

cmmRamUsageAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 23)
)
cmmRamUsageAlertRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysRamUsedMem"),
        ("CMM-CHASSIS-MIB", "cmmSysRamAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmRamUsageAlertRecovery.setStatus(
        "current"
    )

cmmRamUsageCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 24)
)
cmmRamUsageCriticalRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysRamUsedMem"),
        ("CMM-CHASSIS-MIB", "cmmSysRamCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmRamUsageCriticalRecovery.setStatus(
        "current"
    )

cmmHardDiskUsageRisingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 25)
)
cmmHardDiskUsageRisingAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysHarddiskUsedMem"),
        ("CMM-CHASSIS-MIB", "cmmSysHarddiskAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmHardDiskUsageRisingAlert.setStatus(
        "current"
    )

cmmHardDiskUsageRisingCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 26)
)
cmmHardDiskUsageRisingCritical.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysHarddiskUsedMem"),
        ("CMM-CHASSIS-MIB", "cmmSysHarddiskCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmHardDiskUsageRisingCritical.setStatus(
        "current"
    )

cmmHardDiskUsageAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 27)
)
cmmHardDiskUsageAlertRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysHarddiskUsedMem"),
        ("CMM-CHASSIS-MIB", "cmmSysHarddiskAlertThreshold"))
)
if mibBuilder.loadTexts:
    cmmHardDiskUsageAlertRecovery.setStatus(
        "current"
    )

cmmHardDiskUsageCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 28)
)
cmmHardDiskUsageCriticalRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysHarddiskUsedMem"),
        ("CMM-CHASSIS-MIB", "cmmSysHarddiskCriticalThreshold"))
)
if mibBuilder.loadTexts:
    cmmHardDiskUsageCriticalRecovery.setStatus(
        "current"
    )

cmmTemperatureLowEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 31)
)
cmmTemperatureLowEmergency.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempEmergencyThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempEmergencyThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowEmergency.setStatus(
        "current"
    )

cmmTemperatureHighEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 32)
)
cmmTemperatureHighEmergency.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempEmergencyThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempEmergencyThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighEmergency.setStatus(
        "current"
    )

cmmTemperatureLowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 33)
)
cmmTemperatureLowAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowAlert.setStatus(
        "current"
    )

cmmTemperatureHighAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 34)
)
cmmTemperatureHighAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighAlert.setStatus(
        "current"
    )

cmmTemperatureLowCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 35)
)
cmmTemperatureLowCritical.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowCritical.setStatus(
        "current"
    )

cmmTemperatureHighCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 36)
)
cmmTemperatureHighCritical.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighCritical.setStatus(
        "current"
    )

cmmTemperatureHighAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 37)
)
cmmTemperatureHighAlertRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighAlertRecovery.setStatus(
        "current"
    )

cmmTemperatureLowAlertRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 38)
)
cmmTemperatureLowAlertRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempAlertThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowAlertRecovery.setStatus(
        "current"
    )

cmmTemperatureHighCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 39)
)
cmmTemperatureHighCriticalRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureHighCriticalRecovery.setStatus(
        "current"
    )

cmmTemperatureLowCriticalRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 40)
)
cmmTemperatureLowCriticalRecovery.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureValue"),
        ("CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmSysTempCriticalThresholdMax"),
        ("CMM-CHASSIS-MIB", "cmmSysTemperatureSensorName"))
)
if mibBuilder.loadTexts:
    cmmTemperatureLowCriticalRecovery.setStatus(
        "current"
    )

cmmPsuInsertedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 41)
)
cmmPsuInsertedNotify.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysPowerSupplyOperStatus"),
        ("CMM-CHASSIS-MIB", "cmmPsuSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmPsuInsertedNotify.setStatus(
        "current"
    )

cmmPsuRemovedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 42)
)
cmmPsuRemovedAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysPSUIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysPowerSupplyOperStatus"),
        ("CMM-CHASSIS-MIB", "cmmPsuSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmPsuRemovedAlert.setStatus(
        "current"
    )

cmmPsuAcFailedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 43)
)
cmmPsuAcFailedAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysPSUIndex"))
)
if mibBuilder.loadTexts:
    cmmPsuAcFailedAlert.setStatus(
        "current"
    )

cmmPsuAcRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 44)
)
cmmPsuAcRecover.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysPSUIndex"))
)
if mibBuilder.loadTexts:
    cmmPsuAcRecover.setStatus(
        "current"
    )

cmmPsu12vPgFailedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 45)
)
cmmPsu12vPgFailedAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysPSUIndex"))
)
if mibBuilder.loadTexts:
    cmmPsu12vPgFailedAlert.setStatus(
        "current"
    )

cmmPsu12vPgRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 46)
)
cmmPsu12vPgRecover.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmSysPSUIndex"))
)
if mibBuilder.loadTexts:
    cmmPsu12vPgRecover.setStatus(
        "current"
    )

cmmFanTrayInsertedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 51)
)
cmmFanTrayInsertedNotify.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("CMM-CHASSIS-MIB", "cmmFanSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmFanTrayInsertedNotify.setStatus(
        "current"
    )

cmmFanTrayRemovedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 52)
)
cmmFanTrayRemovedAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("CMM-CHASSIS-MIB", "cmmFanSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmFanTrayRemovedAlert.setStatus(
        "current"
    )

cmmFanTrayFaultyAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 53)
)
cmmFanTrayFaultyAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("CMM-CHASSIS-MIB", "cmmFanIndex"))
)
if mibBuilder.loadTexts:
    cmmFanTrayFaultyAlert.setStatus(
        "current"
    )

cmmFanTrayRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 54)
)
cmmFanTrayRecovered.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("CMM-CHASSIS-MIB", "cmmFanIndex"))
)
if mibBuilder.loadTexts:
    cmmFanTrayRecovered.setStatus(
        "current"
    )

cmmFanTrayStallAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 55)
)
cmmFanTrayStallAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("CMM-CHASSIS-MIB", "cmmFanIndex"))
)
if mibBuilder.loadTexts:
    cmmFanTrayStallAlert.setStatus(
        "current"
    )

cmmFanTrayStallRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 56)
)
cmmFanTrayStallRecovered.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("CMM-CHASSIS-MIB", "cmmFanIndex"))
)
if mibBuilder.loadTexts:
    cmmFanTrayStallRecovered.setStatus(
        "current"
    )

cmmFanRPMMinAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 57)
)
cmmFanRPMMinAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("CMM-CHASSIS-MIB", "cmmFanIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanRpmMin"))
)
if mibBuilder.loadTexts:
    cmmFanRPMMinAlert.setStatus(
        "current"
    )

cmmFanRPMMaxAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 1, 58)
)
cmmFanRPMMaxAlert.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanTrayNumber"),
        ("CMM-CHASSIS-MIB", "cmmFanIndex"),
        ("CMM-CHASSIS-MIB", "cmmFanRpmMax"))
)
if mibBuilder.loadTexts:
    cmmFanRPMMaxAlert.setStatus(
        "current"
    )

cmmTransCriticalTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 1)
)
cmmTransCriticalTempHigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransTemperature"),
        ("CMM-CHASSIS-MIB", "cmmTransTempCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransTempCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTempHigh.setStatus(
        "current"
    )

cmmTransCriticalTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 2)
)
cmmTransCriticalTempLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransTemperature"),
        ("CMM-CHASSIS-MIB", "cmmTransTempCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransTempCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTempLow.setStatus(
        "current"
    )

cmmTransAlertTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 3)
)
cmmTransAlertTempHigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransTemperature"),
        ("CMM-CHASSIS-MIB", "cmmTransTempAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransTempAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTempHigh.setStatus(
        "current"
    )

cmmTransAlertTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 4)
)
cmmTransAlertTempLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransTemperature"),
        ("CMM-CHASSIS-MIB", "cmmTransTempAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransTempAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTempLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverTempRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 5)
)
cmmTransNotifyTransceiverTempRecovered.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransTemperature"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverTempRecovered.setStatus(
        "current"
    )

cmmTransCriticalVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 11)
)
cmmTransCriticalVoltageHigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltage"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalVoltageHigh.setStatus(
        "current"
    )

cmmTransCriticalVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 12)
)
cmmTransCriticalVoltageLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltage"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalVoltageLow.setStatus(
        "current"
    )

cmmTransAlertVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 13)
)
cmmTransAlertVoltageHigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltage"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertVoltageHigh.setStatus(
        "current"
    )

cmmTransAlertVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 14)
)
cmmTransAlertVoltageLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltage"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertVoltageLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverVoltRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 15)
)
cmmTransNotifyTransceiverVoltRecovered.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransVoltage"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverVoltRecovered.setStatus(
        "current"
    )

cmmTransCriticalBiasHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 21)
)
cmmTransCriticalBiasHigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalBiasHigh.setStatus(
        "current"
    )

cmmTransCriticalBiasLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 22)
)
cmmTransCriticalBiasLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalBiasLow.setStatus(
        "current"
    )

cmmTransAlertBiashigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 23)
)
cmmTransAlertBiashigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertBiashigh.setStatus(
        "current"
    )

cmmTransAlertBiasLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 24)
)
cmmTransAlertBiasLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertBiasLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverBiasRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 25)
)
cmmTransNotifyTransceiverBiasRecovered.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransLaserBiasCurrent"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverBiasRecovered.setStatus(
        "current"
    )

cmmTransCriticalRxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 31)
)
cmmTransCriticalRxPowerHigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPower"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPowerCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalRxPowerHigh.setStatus(
        "current"
    )

cmmTransCriticalRxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 32)
)
cmmTransCriticalRxPowerLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPower"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPowerCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalRxPowerLow.setStatus(
        "current"
    )

cmmTransAlertRxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 33)
)
cmmTransAlertRxPowerHigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPower"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPowerAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertRxPowerHigh.setStatus(
        "current"
    )

cmmTransAlertRxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 34)
)
cmmTransAlertRxPowerLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPower"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPowerAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertRxPowerLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverRxPowRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 35)
)
cmmTransNotifyTransceiverRxPowRecovered.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransRxPower"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverRxPowRecovered.setStatus(
        "current"
    )

cmmTransCriticalTxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 41)
)
cmmTransCriticalTxPowerHigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPower"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPowerCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTxPowerHigh.setStatus(
        "current"
    )

cmmTransCriticalTxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 42)
)
cmmTransCriticalTxPowerLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPower"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPowerCriticalThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPowerCriticalThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransCriticalTxPowerLow.setStatus(
        "current"
    )

cmmTransAlertTxPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 43)
)
cmmTransAlertTxPowerHigh.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPower"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPowerAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTxPowerHigh.setStatus(
        "current"
    )

cmmTransAlertTxPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 44)
)
cmmTransAlertTxPowerLow.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPower"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPowerAlertThresholdMin"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPowerAlertThresholdMax"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTxPowerLow.setStatus(
        "current"
    )

cmmTransNotifyTransceiverTxPowRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 45)
)
cmmTransNotifyTransceiverTxPowRecovered.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransChannelIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransTxPower"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverTxPowRecovered.setStatus(
        "current"
    )

cmmTransNotifyTransceiverInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 51)
)
cmmTransNotifyTransceiverInserted.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransVendorName"),
        ("CMM-CHASSIS-MIB", "cmmTransVendorSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmTransNotifyTransceiverInserted.setStatus(
        "current"
    )

cmmTransAlertTransceiverRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 52)
)
cmmTransAlertTransceiverRemoved.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"),
        ("CMM-CHASSIS-MIB", "cmmTransVendorName"),
        ("CMM-CHASSIS-MIB", "cmmTransVendorSerialNumber"))
)
if mibBuilder.loadTexts:
    cmmTransAlertTransceiverRemoved.setStatus(
        "current"
    )

cmmTransAlertFaultyTransceiverInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 100, 1, 3, 2, 53)
)
cmmTransAlertFaultyTransceiverInserted.setObjects(
      *(("CMM-CHASSIS-MIB", "cmmStackUnitIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransIndex"),
        ("CMM-CHASSIS-MIB", "cmmTransType"))
)
if mibBuilder.loadTexts:
    cmmTransAlertFaultyTransceiverInserted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CMM-CHASSIS-MIB",
    **{"LedColorCode": LedColorCode,
       "SystemStatusCode": SystemStatusCode,
       "cmm": cmm,
       "CmmChassisObject": CmmChassisObject,
       "cmmObjects": cmmObjects,
       "cmmNumStackUnits": cmmNumStackUnits,
       "cmmSysObjects": cmmSysObjects,
       "cmmStackUnitTable": cmmStackUnitTable,
       "cmmStackUnitEntry": cmmStackUnitEntry,
       "cmmStackUnitIndex": cmmStackUnitIndex,
       "cmmStackUnitModelName": cmmStackUnitModelName,
       "cmmStackUnitSerialNumber": cmmStackUnitSerialNumber,
       "cmmStackUnitUpTime": cmmStackUnitUpTime,
       "cmmStackUnitMfgDate": cmmStackUnitMfgDate,
       "cmmStackUnitMacAddress": cmmStackUnitMacAddress,
       "cmmStackUnitPartNum": cmmStackUnitPartNum,
       "cmmStackLabelRevision": cmmStackLabelRevision,
       "cmmStackUnitCountryCode": cmmStackUnitCountryCode,
       "cmmStackUnitServiceTag": cmmStackUnitServiceTag,
       "cmmStackPlatformName": cmmStackPlatformName,
       "cmmStackOnieVersion": cmmStackOnieVersion,
       "cmmStackMfgName": cmmStackMfgName,
       "cmmStackVendorName": cmmStackVendorName,
       "cmmStackDiagVersion": cmmStackDiagVersion,
       "cmmStackCrc32": cmmStackCrc32,
       "cmmStackUnitNumFanControllers": cmmStackUnitNumFanControllers,
       "cmmStackUnitNumFanTrays": cmmStackUnitNumFanTrays,
       "cmmStackUnitNumPowerSupplies": cmmStackUnitNumPowerSupplies,
       "cmmStackUnitNumPluggableModules": cmmStackUnitNumPluggableModules,
       "cmmStackUnitNumFastEtherPorts": cmmStackUnitNumFastEtherPorts,
       "cmmStackUnitNumGigEtherPorts": cmmStackUnitNumGigEtherPorts,
       "cmmStackUnitNum10GigEtherPorts": cmmStackUnitNum10GigEtherPorts,
       "cmmStackUnitNum25GigEtherPorts": cmmStackUnitNum25GigEtherPorts,
       "cmmStackUnitNum40GigEtherPorts": cmmStackUnitNum40GigEtherPorts,
       "cmmStackUnitNum50GigEtherPorts": cmmStackUnitNum50GigEtherPorts,
       "cmmStackUnitNum100GigEtherPorts": cmmStackUnitNum100GigEtherPorts,
       "cmmStackUnitSwitchChipRev": cmmStackUnitSwitchChipRev,
       "cmmStackSupportedLabelRevision": cmmStackSupportedLabelRevision,
       "cmmStackUnitSupportedSwitchChipRev": cmmStackUnitSupportedSwitchChipRev,
       "cmmTransEEPROMTable": cmmTransEEPROMTable,
       "cmmTransEEPROMEntry": cmmTransEEPROMEntry,
       "cmmTransIndex": cmmTransIndex,
       "cmmTransType": cmmTransType,
       "cmmTransNoOfChannels": cmmTransNoOfChannels,
       "cmmTransidentifier": cmmTransidentifier,
       "cmmTransSFPextendedidentifier": cmmTransSFPextendedidentifier,
       "cmmTransQSFPextendedidentifier": cmmTransQSFPextendedidentifier,
       "cmmTransconnectortype": cmmTransconnectortype,
       "cmmTransEthCompliance": cmmTransEthCompliance,
       "cmmTransExtEthCompliance": cmmTransExtEthCompliance,
       "cmmTransSonetCompliance": cmmTransSonetCompliance,
       "cmmTransFiberChnlLinkLen": cmmTransFiberChnlLinkLen,
       "cmmTransFiberChnlTransTech": cmmTransFiberChnlTransTech,
       "cmmTransFiberChnlTransMedia": cmmTransFiberChnlTransMedia,
       "cmmTransSFPFiberChnlSpeed": cmmTransSFPFiberChnlSpeed,
       "cmmTransQSFPFiberChnlSpeed": cmmTransQSFPFiberChnlSpeed,
       "cmmTransSFPInfiniBandCompliance": cmmTransSFPInfiniBandCompliance,
       "cmmTransSFPEsconCompliance": cmmTransSFPEsconCompliance,
       "cmmTransSfpPlusCableTech": cmmTransSfpPlusCableTech,
       "cmmTransEncoding": cmmTransEncoding,
       "cmmTransLengthKmtrs": cmmTransLengthKmtrs,
       "cmmTransLengthMtrs": cmmTransLengthMtrs,
       "cmmTransLengthOM1": cmmTransLengthOM1,
       "cmmTransLengthOM2": cmmTransLengthOM2,
       "cmmTransLengthOM3": cmmTransLengthOM3,
       "cmmTransLengthOM4": cmmTransLengthOM4,
       "cmmTransVendorName": cmmTransVendorName,
       "cmmTransVendorOUI": cmmTransVendorOUI,
       "cmmTransVendorPartNumber": cmmTransVendorPartNumber,
       "cmmTransVendorRevision": cmmTransVendorRevision,
       "cmmTransCheckCode": cmmTransCheckCode,
       "cmmTransCheckCodeExtended": cmmTransCheckCodeExtended,
       "cmmTransNominalBitRate": cmmTransNominalBitRate,
       "cmmTransBitRateMax": cmmTransBitRateMax,
       "cmmTransBitRateMin": cmmTransBitRateMin,
       "cmmTransVendorSerialNumber": cmmTransVendorSerialNumber,
       "cmmTransDateCode": cmmTransDateCode,
       "cmmTransDDMSupport": cmmTransDDMSupport,
       "cmmTransMaxCaseTemp": cmmTransMaxCaseTemp,
       "cmmTransSFPOptionsImp": cmmTransSFPOptionsImp,
       "cmmTransQSFPOptionsImp": cmmTransQSFPOptionsImp,
       "cmmTransPresence": cmmTransPresence,
       "cmmTransDDMTable": cmmTransDDMTable,
       "cmmTransDDMEntry": cmmTransDDMEntry,
       "cmmTransChannelIndex": cmmTransChannelIndex,
       "cmmTransTemperature": cmmTransTemperature,
       "cmmTransTempCriticalThresholdMin": cmmTransTempCriticalThresholdMin,
       "cmmTransTempCriticalThresholdMax": cmmTransTempCriticalThresholdMax,
       "cmmTransTempAlertThresholdMin": cmmTransTempAlertThresholdMin,
       "cmmTransTempAlertThresholdMax": cmmTransTempAlertThresholdMax,
       "cmmTransVoltage": cmmTransVoltage,
       "cmmTransVoltCriticalThresholdMin": cmmTransVoltCriticalThresholdMin,
       "cmmTransVoltCriticalThresholdMax": cmmTransVoltCriticalThresholdMax,
       "cmmTransVoltAlertThresholdMin": cmmTransVoltAlertThresholdMin,
       "cmmTransVoltAlertThresholdMax": cmmTransVoltAlertThresholdMax,
       "cmmTransLaserBiasCurrent": cmmTransLaserBiasCurrent,
       "cmmTransLaserBiasCurrCriticalThresholdMin": cmmTransLaserBiasCurrCriticalThresholdMin,
       "cmmTransLaserBiasCurrCriticalThresholdMax": cmmTransLaserBiasCurrCriticalThresholdMax,
       "cmmTransLaserBiasCurrAlertThresholdMin": cmmTransLaserBiasCurrAlertThresholdMin,
       "cmmTransLaserBiasCurrAlertThresholdMax": cmmTransLaserBiasCurrAlertThresholdMax,
       "cmmTransTxPower": cmmTransTxPower,
       "cmmTransTxPowerCriticalThresholdMin": cmmTransTxPowerCriticalThresholdMin,
       "cmmTransTxPowerCriticalThresholdMax": cmmTransTxPowerCriticalThresholdMax,
       "cmmTransTxPowerAlertThresholdMin": cmmTransTxPowerAlertThresholdMin,
       "cmmTransTxPowerAlertThresholdMax": cmmTransTxPowerAlertThresholdMax,
       "cmmTransRxPower": cmmTransRxPower,
       "cmmTransRxPowerCriticalThresholdMin": cmmTransRxPowerCriticalThresholdMin,
       "cmmTransRxPowerCriticalThresholdMax": cmmTransRxPowerCriticalThresholdMax,
       "cmmTransRxPowerAlertThresholdMin": cmmTransRxPowerAlertThresholdMin,
       "cmmTransRxPowerAlertThresholdMax": cmmTransRxPowerAlertThresholdMax,
       "cmmTransTxPowerSupported": cmmTransTxPowerSupported,
       "cmmTransRxPowerSupported": cmmTransRxPowerSupported,
       "cmmTransDDMStatus": cmmTransDDMStatus,
       "cmmTransTxState": cmmTransTxState,
       "cmmTransRxLosState": cmmTransRxLosState,
       "cmmTransTxLosState": cmmTransTxLosState,
       "cmmTransResetState": cmmTransResetState,
       "cmmTransPowerMode": cmmTransPowerMode,
       "cmmSysRamTable": cmmSysRamTable,
       "cmmSysRamEntry": cmmSysRamEntry,
       "cmmSysRamTotalMem": cmmSysRamTotalMem,
       "cmmSysRamUsedMem": cmmSysRamUsedMem,
       "cmmSysRamFreeMem": cmmSysRamFreeMem,
       "cmmSysRamCriticalThreshold": cmmSysRamCriticalThreshold,
       "cmmSysRamAlertThreshold": cmmSysRamAlertThreshold,
       "cmmStackCpuTable": cmmStackCpuTable,
       "cmmStackCpuEntry": cmmStackCpuEntry,
       "cmmStackUnitNumCpuProcessor": cmmStackUnitNumCpuProcessor,
       "cmmStackUnitCpuLoad1Min": cmmStackUnitCpuLoad1Min,
       "cmmStackUnitCpuLoad5Min": cmmStackUnitCpuLoad5Min,
       "cmmStackUnitCpuLoad15Min": cmmStackUnitCpuLoad15Min,
       "cmmStackCpuLoad1minAlertThreshold": cmmStackCpuLoad1minAlertThreshold,
       "cmmStackCpuLoad1minCriticalThreshold": cmmStackCpuLoad1minCriticalThreshold,
       "cmmStackCpuLoad5minCriticalThreshold": cmmStackCpuLoad5minCriticalThreshold,
       "cmmStackCpuLoad15minCriticalThreshold": cmmStackCpuLoad15minCriticalThreshold,
       "cmmStackUnitCpuUtilization": cmmStackUnitCpuUtilization,
       "cmmStackUnitCpuUtilAlertThreshold": cmmStackUnitCpuUtilAlertThreshold,
       "cmmStackUnitCpuUtilCriticalThreshold": cmmStackUnitCpuUtilCriticalThreshold,
       "cmmSysPowerSupplyTable": cmmSysPowerSupplyTable,
       "cmmSysPowerSupplyEntry": cmmSysPowerSupplyEntry,
       "cmmSysPSUIndex": cmmSysPSUIndex,
       "cmmSysPowerSupplyOperStatus": cmmSysPowerSupplyOperStatus,
       "cmmSysPowerSupplyType": cmmSysPowerSupplyType,
       "cmmSysHotSwapStat": cmmSysHotSwapStat,
       "cmmSysPSConsumption": cmmSysPSConsumption,
       "cmmSysInputPower": cmmSysInputPower,
       "cmmSysInputVoltage": cmmSysInputVoltage,
       "cmmSysOutputVoltage": cmmSysOutputVoltage,
       "cmmSysInputCurrent": cmmSysInputCurrent,
       "cmmSysOutputCurrent": cmmSysOutputCurrent,
       "cmmSysPSTemperature1": cmmSysPSTemperature1,
       "cmmSysPSTemperature2": cmmSysPSTemperature2,
       "cmmSysPSFan1Rpm": cmmSysPSFan1Rpm,
       "cmmSysPSFan2Rpm": cmmSysPSFan2Rpm,
       "cmmSysPS12VPg": cmmSysPS12VPg,
       "cmmSysPSAcAlert": cmmSysPSAcAlert,
       "cmmSysPSParamsSupport": cmmSysPSParamsSupport,
       "cmmSysPowerRailTable": cmmSysPowerRailTable,
       "cmmSysPowerRailEntry": cmmSysPowerRailEntry,
       "cmmSysPOWERVDDR": cmmSysPOWERVDDR,
       "cmmSysPOWERCORE": cmmSysPOWERCORE,
       "cmmSysV1P1POWERRAIL": cmmSysV1P1POWERRAIL,
       "cmmSysMAINBOARDPOWERRAIL": cmmSysMAINBOARDPOWERRAIL,
       "cmmSysV1P05POWERRAIL": cmmSysV1P05POWERRAIL,
       "cmmSysV1P5POWERRAIL": cmmSysV1P5POWERRAIL,
       "cmmSysVCCPOWERRAIL": cmmSysVCCPOWERRAIL,
       "cmmSysSBV1P5POWERRAIL": cmmSysSBV1P5POWERRAIL,
       "cmmSysV1P0POWERRAIL": cmmSysV1P0POWERRAIL,
       "cmmSysV3P3POWERRAIL": cmmSysV3P3POWERRAIL,
       "cmmSysV1P8POWERRAIL": cmmSysV1P8POWERRAIL,
       "cmmSysV1P35POWERRAIL": cmmSysV1P35POWERRAIL,
       "cmmSysVCC5V": cmmSysVCC5V,
       "cmmSysVCC33V": cmmSysVCC33V,
       "cmmSysVCCMAC1V": cmmSysVCCMAC1V,
       "cmmSysVCCMACAVS1V": cmmSysVCCMACAVS1V,
       "cmmSysVCCV1P05": cmmSysVCCV1P05,
       "cmmSysVCCV1P5": cmmSysVCCV1P5,
       "cmmSysVCCV1P8": cmmSysVCCV1P8,
       "cmmSysVCCAVS1V": cmmSysVCCAVS1V,
       "cmmSysDDRVTT": cmmSysDDRVTT,
       "cmmFanTrayTable": cmmFanTrayTable,
       "cmmFanTrayEntry": cmmFanTrayEntry,
       "cmmFanTrayNumber": cmmFanTrayNumber,
       "cmmFanTrayStatus": cmmFanTrayStatus,
       "cmmFanTrayLedColor": cmmFanTrayLedColor,
       "cmmFanTable": cmmFanTable,
       "cmmFanEntry": cmmFanEntry,
       "cmmFanIndex": cmmFanIndex,
       "cmmFanRpm": cmmFanRpm,
       "cmmFanRpmMin": cmmFanRpmMin,
       "cmmFanRpmMax": cmmFanRpmMax,
       "cmmFanStatus": cmmFanStatus,
       "cmmFanLocation": cmmFanLocation,
       "cmmSysTemperatureTable": cmmSysTemperatureTable,
       "cmmSysTemperatureEntry": cmmSysTemperatureEntry,
       "cmmSysTemperatureSensorIndex": cmmSysTemperatureSensorIndex,
       "cmmSysTemperatureSensorName": cmmSysTemperatureSensorName,
       "cmmSysTemperatureValue": cmmSysTemperatureValue,
       "cmmSysTempEmergencyThresholdMin": cmmSysTempEmergencyThresholdMin,
       "cmmSysTempEmergencyThresholdMax": cmmSysTempEmergencyThresholdMax,
       "cmmSysTempAlertThresholdMin": cmmSysTempAlertThresholdMin,
       "cmmSysTempAlertThresholdMax": cmmSysTempAlertThresholdMax,
       "cmmSysTempCriticalThresholdMin": cmmSysTempCriticalThresholdMin,
       "cmmSysTempCriticalThresholdMax": cmmSysTempCriticalThresholdMax,
       "cmmSysComponentStatusTable": cmmSysComponentStatusTable,
       "cmmSysComponentStatusEntry": cmmSysComponentStatusEntry,
       "cmmSysPsu1Status": cmmSysPsu1Status,
       "cmmSysPsu1LedColor": cmmSysPsu1LedColor,
       "cmmSysPsu2Status": cmmSysPsu2Status,
       "cmmSysPsu2LedColor": cmmSysPsu2LedColor,
       "cmmSysLocatorLedStatus": cmmSysLocatorLedStatus,
       "cmmSysLocatorLedColor": cmmSysLocatorLedColor,
       "cmmSysMasterLedStatus": cmmSysMasterLedStatus,
       "cmmSysMasterLedColor": cmmSysMasterLedColor,
       "cmmSysFanStatus": cmmSysFanStatus,
       "cmmSysFrontFanLedColor": cmmSysFrontFanLedColor,
       "cmmSysRamStatus": cmmSysRamStatus,
       "cmmSysCpuStatus": cmmSysCpuStatus,
       "cmmSysDiskStatus": cmmSysDiskStatus,
       "cmmSysTemperatureStatus": cmmSysTemperatureStatus,
       "cmmSysSwModuleTable": cmmSysSwModuleTable,
       "cmmSysSwModuleEntry": cmmSysSwModuleEntry,
       "cmmSysSwRuntimeImgVersion": cmmSysSwRuntimeImgVersion,
       "cmmSysSwRuntimeImgDate": cmmSysSwRuntimeImgDate,
       "cmmSwitchTemperatureTable": cmmSwitchTemperatureTable,
       "cmmSwitchTemperatureEntry": cmmSwitchTemperatureEntry,
       "cmmSwitchTemperatureSensorIndex": cmmSwitchTemperatureSensorIndex,
       "cmmSwitchTemperatureValue": cmmSwitchTemperatureValue,
       "cmmSwitchTempPeakValue": cmmSwitchTempPeakValue,
       "cmmSysHardDiskTable": cmmSysHardDiskTable,
       "cmmSysHardDiskEntry": cmmSysHardDiskEntry,
       "cmmSysHarddiskSerialno": cmmSysHarddiskSerialno,
       "cmmSysHarddiskModelno": cmmSysHarddiskModelno,
       "cmmSysHarddiskFirmwarerev": cmmSysHarddiskFirmwarerev,
       "cmmSysHarddiskCylinders": cmmSysHarddiskCylinders,
       "cmmSysHarddiskHeads": cmmSysHarddiskHeads,
       "cmmSysHarddiskSectors": cmmSysHarddiskSectors,
       "cmmSysHarddiskUnformattedBytesorTrack": cmmSysHarddiskUnformattedBytesorTrack,
       "cmmSysHarddiskUnformattedBytesorSector": cmmSysHarddiskUnformattedBytesorSector,
       "cmmSysHarddiskRevisionNum": cmmSysHarddiskRevisionNum,
       "cmmSysHarddiskTotalsize": cmmSysHarddiskTotalsize,
       "cmmSysHarddiskUsedMem": cmmSysHarddiskUsedMem,
       "cmmSysHarddiskFreeMem": cmmSysHarddiskFreeMem,
       "cmmSysHarddiskCriticalThreshold": cmmSysHarddiskCriticalThreshold,
       "cmmSysHarddiskAlertThreshold": cmmSysHarddiskAlertThreshold,
       "cmmSystemStatusTable": cmmSystemStatusTable,
       "cmmSystemStatusEntry": cmmSystemStatusEntry,
       "cmmSystemMinorFaultStatus": cmmSystemMinorFaultStatus,
       "cmmSystemMajorFaultStatus": cmmSystemMajorFaultStatus,
       "cmmSysStatus": cmmSysStatus,
       "cmmSysLedColor": cmmSysLedColor,
       "cmmCpuCoreUtilTable": cmmCpuCoreUtilTable,
       "cmmCpuCoreUtilEntry": cmmCpuCoreUtilEntry,
       "cmmCpuCoreIndex": cmmCpuCoreIndex,
       "cmmCpuCoreUtilization": cmmCpuCoreUtilization,
       "cmmCpuCoreModelName": cmmCpuCoreModelName,
       "cmmPsuFruTable": cmmPsuFruTable,
       "cmmPsuFruEntry": cmmPsuFruEntry,
       "cmmPsuPpid": cmmPsuPpid,
       "cmmPsuCountryofOrigin": cmmPsuCountryofOrigin,
       "cmmPsuPpidPartNum": cmmPsuPpidPartNum,
       "cmmPsuPpidPartNumRev": cmmPsuPpidPartNumRev,
       "cmmPsuManufactureId": cmmPsuManufactureId,
       "cmmPsuDateCode": cmmPsuDateCode,
       "cmmPsuSerialNumber": cmmPsuSerialNumber,
       "cmmPsuPartNum": cmmPsuPartNum,
       "cmmPsuPartNumRev": cmmPsuPartNumRev,
       "cmmPsuNumOfFanPerTray": cmmPsuNumOfFanPerTray,
       "cmmPsuType": cmmPsuType,
       "cmmPsuServiceTag": cmmPsuServiceTag,
       "cmmPsuIanaNum": cmmPsuIanaNum,
       "cmmPsuFanMaxRpm": cmmPsuFanMaxRpm,
       "cmmPsuAirFlowDir": cmmPsuAirFlowDir,
       "cmmPsuMaxOutputWatt": cmmPsuMaxOutputWatt,
       "cmmFanFruTable": cmmFanFruTable,
       "cmmFanFruEntry": cmmFanFruEntry,
       "cmmFanPpid": cmmFanPpid,
       "cmmFanCountryofOrigin": cmmFanCountryofOrigin,
       "cmmFanPpidPartNum": cmmFanPpidPartNum,
       "cmmFanPpidPartNumRev": cmmFanPpidPartNumRev,
       "cmmFanManufactureId": cmmFanManufactureId,
       "cmmFanDateCode": cmmFanDateCode,
       "cmmFanSerialNumber": cmmFanSerialNumber,
       "cmmFanPartNum": cmmFanPartNum,
       "cmmFanPartNumRev": cmmFanPartNumRev,
       "cmmFanNumOfFanPerTray": cmmFanNumOfFanPerTray,
       "cmmFanType": cmmFanType,
       "cmmFanServiceTag": cmmFanServiceTag,
       "cmmFanIanaNum": cmmFanIanaNum,
       "cmmFanMaxRpm": cmmFanMaxRpm,
       "cmmSysCpldTable": cmmSysCpldTable,
       "cmmSysCpldEntry": cmmSysCpldEntry,
       "cmmSysCpldIndex": cmmSysCpldIndex,
       "cmmSysCpldName": cmmSysCpldName,
       "cmmSysCpldSupportedVer": cmmSysCpldSupportedVer,
       "cmmSysCpldCurrentVer": cmmSysCpldCurrentVer,
       "cmmAlarmObjects": cmmAlarmObjects,
       "cmmAlarmVariable": cmmAlarmVariable,
       "cmmAlarmVarInteger": cmmAlarmVarInteger,
       "cmmAlarmVarString": cmmAlarmVarString,
       "cmmAlarmMibNotifications": cmmAlarmMibNotifications,
       "cmmCpuLoad15MinCritical": cmmCpuLoad15MinCritical,
       "cmmCpuLoad5MinCritical": cmmCpuLoad5MinCritical,
       "cmmCpuLoad1MinAlert": cmmCpuLoad1MinAlert,
       "cmmCpuLoad1MinCritical": cmmCpuLoad1MinCritical,
       "cmmCpuLoad1MinAlertRecovery": cmmCpuLoad1MinAlertRecovery,
       "cmmCpuLoad15MinCriticalRecovery": cmmCpuLoad15MinCriticalRecovery,
       "cmmCpuLoad5MinCriticalRecovery": cmmCpuLoad5MinCriticalRecovery,
       "cmmCpuLoad1MinCriticalRecovery": cmmCpuLoad1MinCriticalRecovery,
       "cmmCpuCoreUtilHighAlert": cmmCpuCoreUtilHighAlert,
       "cmmCpuCoreUtilHighCritical": cmmCpuCoreUtilHighCritical,
       "cmmCpuCoreUtilHighAlertRecovery": cmmCpuCoreUtilHighAlertRecovery,
       "cmmCpuCoreUtilHighCriticalRecovery": cmmCpuCoreUtilHighCriticalRecovery,
       "cmmRamUsageRisingAlert": cmmRamUsageRisingAlert,
       "cmmRamUsageRisingCritical": cmmRamUsageRisingCritical,
       "cmmRamUsageAlertRecovery": cmmRamUsageAlertRecovery,
       "cmmRamUsageCriticalRecovery": cmmRamUsageCriticalRecovery,
       "cmmHardDiskUsageRisingAlert": cmmHardDiskUsageRisingAlert,
       "cmmHardDiskUsageRisingCritical": cmmHardDiskUsageRisingCritical,
       "cmmHardDiskUsageAlertRecovery": cmmHardDiskUsageAlertRecovery,
       "cmmHardDiskUsageCriticalRecovery": cmmHardDiskUsageCriticalRecovery,
       "cmmTemperatureLowEmergency": cmmTemperatureLowEmergency,
       "cmmTemperatureHighEmergency": cmmTemperatureHighEmergency,
       "cmmTemperatureLowAlert": cmmTemperatureLowAlert,
       "cmmTemperatureHighAlert": cmmTemperatureHighAlert,
       "cmmTemperatureLowCritical": cmmTemperatureLowCritical,
       "cmmTemperatureHighCritical": cmmTemperatureHighCritical,
       "cmmTemperatureHighAlertRecovery": cmmTemperatureHighAlertRecovery,
       "cmmTemperatureLowAlertRecovery": cmmTemperatureLowAlertRecovery,
       "cmmTemperatureHighCriticalRecovery": cmmTemperatureHighCriticalRecovery,
       "cmmTemperatureLowCriticalRecovery": cmmTemperatureLowCriticalRecovery,
       "cmmPsuInsertedNotify": cmmPsuInsertedNotify,
       "cmmPsuRemovedAlert": cmmPsuRemovedAlert,
       "cmmPsuAcFailedAlert": cmmPsuAcFailedAlert,
       "cmmPsuAcRecover": cmmPsuAcRecover,
       "cmmPsu12vPgFailedAlert": cmmPsu12vPgFailedAlert,
       "cmmPsu12vPgRecover": cmmPsu12vPgRecover,
       "cmmFanTrayInsertedNotify": cmmFanTrayInsertedNotify,
       "cmmFanTrayRemovedAlert": cmmFanTrayRemovedAlert,
       "cmmFanTrayFaultyAlert": cmmFanTrayFaultyAlert,
       "cmmFanTrayRecovered": cmmFanTrayRecovered,
       "cmmFanTrayStallAlert": cmmFanTrayStallAlert,
       "cmmFanTrayStallRecovered": cmmFanTrayStallRecovered,
       "cmmFanRPMMinAlert": cmmFanRPMMinAlert,
       "cmmFanRPMMaxAlert": cmmFanRPMMaxAlert,
       "cmmTransMibNotifications": cmmTransMibNotifications,
       "cmmTransCriticalTempHigh": cmmTransCriticalTempHigh,
       "cmmTransCriticalTempLow": cmmTransCriticalTempLow,
       "cmmTransAlertTempHigh": cmmTransAlertTempHigh,
       "cmmTransAlertTempLow": cmmTransAlertTempLow,
       "cmmTransNotifyTransceiverTempRecovered": cmmTransNotifyTransceiverTempRecovered,
       "cmmTransCriticalVoltageHigh": cmmTransCriticalVoltageHigh,
       "cmmTransCriticalVoltageLow": cmmTransCriticalVoltageLow,
       "cmmTransAlertVoltageHigh": cmmTransAlertVoltageHigh,
       "cmmTransAlertVoltageLow": cmmTransAlertVoltageLow,
       "cmmTransNotifyTransceiverVoltRecovered": cmmTransNotifyTransceiverVoltRecovered,
       "cmmTransCriticalBiasHigh": cmmTransCriticalBiasHigh,
       "cmmTransCriticalBiasLow": cmmTransCriticalBiasLow,
       "cmmTransAlertBiashigh": cmmTransAlertBiashigh,
       "cmmTransAlertBiasLow": cmmTransAlertBiasLow,
       "cmmTransNotifyTransceiverBiasRecovered": cmmTransNotifyTransceiverBiasRecovered,
       "cmmTransCriticalRxPowerHigh": cmmTransCriticalRxPowerHigh,
       "cmmTransCriticalRxPowerLow": cmmTransCriticalRxPowerLow,
       "cmmTransAlertRxPowerHigh": cmmTransAlertRxPowerHigh,
       "cmmTransAlertRxPowerLow": cmmTransAlertRxPowerLow,
       "cmmTransNotifyTransceiverRxPowRecovered": cmmTransNotifyTransceiverRxPowRecovered,
       "cmmTransCriticalTxPowerHigh": cmmTransCriticalTxPowerHigh,
       "cmmTransCriticalTxPowerLow": cmmTransCriticalTxPowerLow,
       "cmmTransAlertTxPowerHigh": cmmTransAlertTxPowerHigh,
       "cmmTransAlertTxPowerLow": cmmTransAlertTxPowerLow,
       "cmmTransNotifyTransceiverTxPowRecovered": cmmTransNotifyTransceiverTxPowRecovered,
       "cmmTransNotifyTransceiverInserted": cmmTransNotifyTransceiverInserted,
       "cmmTransAlertTransceiverRemoved": cmmTransAlertTransceiverRemoved,
       "cmmTransAlertFaultyTransceiverInserted": cmmTransAlertFaultyTransceiverInserted}
)
