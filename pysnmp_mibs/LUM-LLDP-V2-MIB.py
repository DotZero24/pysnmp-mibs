# SNMP MIB module (LUM-LLDP-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-LLDP-V2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:14 2025
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

(lumLldpV2MIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumLldpV2MIB",
    "lumModules")

(MgmtNameString,
 PortNumber,
 SlotNumber,
 SubrackNumber,
 TruthValueWithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "MgmtNameString",
    "PortNumber",
    "SlotNumber",
    "SubrackNumber",
    "TruthValueWithNA")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lumLldpV2MIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 67)
)
if mibBuilder.loadTexts:
    lumLldpV2MIBModule.setRevisions(
        ("2017-12-15 00:00",
         "2017-06-15 00:00",
         "2016-04-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LumAddressFamilyNumbers(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              65535,
              2147483646,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ipV4", 1),
          ("ipV6", 2),
          ("nsap", 3),
          ("hdlc", 4),
          ("bbn1822", 5),
          ("all802", 6),
          ("e163", 7),
          ("e164", 8),
          ("f69", 9),
          ("x121", 10),
          ("ipx", 11),
          ("appleTalk", 12),
          ("decnetIV", 13),
          ("banyanVines", 14),
          ("e164withNsap", 15),
          ("dns", 16),
          ("distinguishedName", 17),
          ("asNumber", 18),
          ("xtpOverIpv4", 19),
          ("xtpOverIpv6", 20),
          ("xtpNativeModeXTP", 21),
          ("fibreChannelWWPN", 22),
          ("fibreChannelWWNN", 23),
          ("gwid", 24),
          ("reserved", 65535),
          ("notAvailable", 2147483646),
          ("notApplicable", 2147483647))
    )



class LldpV2ChassisIdSubtype(TextualConvention, Integer32):
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
              2147483646)
        )
    )
    namedValues = NamedValues(
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7),
          ("notAvailable", 2147483646))
    )



class LldpV2ChassisId(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class LldpV2PortIdSubtype(TextualConvention, Integer32):
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
              2147483646)
        )
    )
    namedValues = NamedValues(
        *(("interfaceAlias", 1),
          ("portComponent", 2),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("interfaceName", 5),
          ("agentCircuitId", 6),
          ("local", 7),
          ("notAvailable", 2147483646))
    )



class LldpV2PortId(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class LldpV2ManAddrIfSubtype(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483646,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ifIndex", 2),
          ("systemPortNumber", 3),
          ("notAvailable", 2147483646),
          ("notApplicable", 2147483647))
    )



class LldpV2ManAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )



# MIB Managed Objects in the order of their OIDs

_LumLldpV2Confs_ObjectIdentity = ObjectIdentity
lumLldpV2Confs = _LumLldpV2Confs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1)
)
_LumLldpV2Groups_ObjectIdentity = ObjectIdentity
lumLldpV2Groups = _LumLldpV2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1, 1)
)
_LumLldpV2Compliances_ObjectIdentity = ObjectIdentity
lumLldpV2Compliances = _LumLldpV2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1, 2)
)
_LumLldpV2MIBObjects_ObjectIdentity = ObjectIdentity
lumLldpV2MIBObjects = _LumLldpV2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2)
)
_LldpGeneral_ObjectIdentity = ObjectIdentity
lldpGeneral = _LldpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 1)
)
_LldpV2GeneralConfigLastChangeTime_Type = DateAndTime
_LldpV2GeneralConfigLastChangeTime_Object = MibScalar
lldpV2GeneralConfigLastChangeTime = _LldpV2GeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 1, 1),
    _LldpV2GeneralConfigLastChangeTime_Type()
)
lldpV2GeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2GeneralConfigLastChangeTime.setStatus("current")
_LldpV2GeneralStateLastChangeTime_Type = DateAndTime
_LldpV2GeneralStateLastChangeTime_Object = MibScalar
lldpV2GeneralStateLastChangeTime = _LldpV2GeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 1, 2),
    _LldpV2GeneralStateLastChangeTime_Type()
)
lldpV2GeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2GeneralStateLastChangeTime.setStatus("current")
_LldpV2SystemInfoTableSize_Type = Unsigned32
_LldpV2SystemInfoTableSize_Object = MibScalar
lldpV2SystemInfoTableSize = _LldpV2SystemInfoTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 1, 3),
    _LldpV2SystemInfoTableSize_Type()
)
lldpV2SystemInfoTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2SystemInfoTableSize.setStatus("current")
_LldpV2AgentConfigTableSize_Type = Unsigned32
_LldpV2AgentConfigTableSize_Object = MibScalar
lldpV2AgentConfigTableSize = _LldpV2AgentConfigTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 1, 4),
    _LldpV2AgentConfigTableSize_Type()
)
lldpV2AgentConfigTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2AgentConfigTableSize.setStatus("current")
_LldpV2RemSystemDataTableSize_Type = Unsigned32
_LldpV2RemSystemDataTableSize_Object = MibScalar
lldpV2RemSystemDataTableSize = _LldpV2RemSystemDataTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 1, 5),
    _LldpV2RemSystemDataTableSize_Type()
)
lldpV2RemSystemDataTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemSystemDataTableSize.setStatus("current")
_LldpV2StaticsTableSize_Type = Unsigned32
_LldpV2StaticsTableSize_Object = MibScalar
lldpV2StaticsTableSize = _LldpV2StaticsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 1, 6),
    _LldpV2StaticsTableSize_Type()
)
lldpV2StaticsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StaticsTableSize.setStatus("current")
_LldpV2SystemInfo_ObjectIdentity = ObjectIdentity
lldpV2SystemInfo = _LldpV2SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2)
)
_LldpV2SystemInfoTable_Object = MibTable
lldpV2SystemInfoTable = _LldpV2SystemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lldpV2SystemInfoTable.setStatus("current")
_LldpV2SystemInfoEntry_Object = MibTableRow
lldpV2SystemInfoEntry = _LldpV2SystemInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1, 1)
)
lldpV2SystemInfoEntry.setIndexNames(
    (0, "LUM-LLDP-V2-MIB", "lldpV2SystemInfoIndex"),
)
if mibBuilder.loadTexts:
    lldpV2SystemInfoEntry.setStatus("current")


class _LldpV2SystemInfoIndex_Type(Unsigned32):
    """Custom type lldpV2SystemInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2SystemInfoIndex_Type.__name__ = "Unsigned32"
_LldpV2SystemInfoIndex_Object = MibTableColumn
lldpV2SystemInfoIndex = _LldpV2SystemInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1, 1, 1),
    _LldpV2SystemInfoIndex_Type()
)
lldpV2SystemInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2SystemInfoIndex.setStatus("current")
_LldpV2SystemInfoName_Type = MgmtNameString
_LldpV2SystemInfoName_Object = MibTableColumn
lldpV2SystemInfoName = _LldpV2SystemInfoName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1, 1, 2),
    _LldpV2SystemInfoName_Type()
)
lldpV2SystemInfoName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2SystemInfoName.setStatus("current")
_LldpV2SystemInfoSystemName_Type = MgmtNameString
_LldpV2SystemInfoSystemName_Object = MibTableColumn
lldpV2SystemInfoSystemName = _LldpV2SystemInfoSystemName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1, 1, 3),
    _LldpV2SystemInfoSystemName_Type()
)
lldpV2SystemInfoSystemName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2SystemInfoSystemName.setStatus("current")
_LldpV2SystemInfoSystemDescription_Type = DisplayString
_LldpV2SystemInfoSystemDescription_Object = MibTableColumn
lldpV2SystemInfoSystemDescription = _LldpV2SystemInfoSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1, 1, 4),
    _LldpV2SystemInfoSystemDescription_Type()
)
lldpV2SystemInfoSystemDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2SystemInfoSystemDescription.setStatus("current")


class _LldpV2SystemInfoSystemMacAddress_Type(OctetString):
    """Custom type lldpV2SystemInfoSystemMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_LldpV2SystemInfoSystemMacAddress_Type.__name__ = "OctetString"
_LldpV2SystemInfoSystemMacAddress_Object = MibTableColumn
lldpV2SystemInfoSystemMacAddress = _LldpV2SystemInfoSystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1, 1, 5),
    _LldpV2SystemInfoSystemMacAddress_Type()
)
lldpV2SystemInfoSystemMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2SystemInfoSystemMacAddress.setStatus("current")
_LldpV2SystemInfoManagementIp_Type = IpAddress
_LldpV2SystemInfoManagementIp_Object = MibTableColumn
lldpV2SystemInfoManagementIp = _LldpV2SystemInfoManagementIp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1, 1, 6),
    _LldpV2SystemInfoManagementIp_Type()
)
lldpV2SystemInfoManagementIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2SystemInfoManagementIp.setStatus("current")


class _LldpV2SystemInfoManagementOID_Type(OctetString):
    """Custom type lldpV2SystemInfoManagementOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_LldpV2SystemInfoManagementOID_Type.__name__ = "OctetString"
_LldpV2SystemInfoManagementOID_Object = MibTableColumn
lldpV2SystemInfoManagementOID = _LldpV2SystemInfoManagementOID_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1, 1, 7),
    _LldpV2SystemInfoManagementOID_Type()
)
lldpV2SystemInfoManagementOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2SystemInfoManagementOID.setStatus("current")


class _LldpV2SystemInfoMaxNeighbors_Type(Unsigned32):
    """Custom type lldpV2SystemInfoMaxNeighbors based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_LldpV2SystemInfoMaxNeighbors_Type.__name__ = "Unsigned32"
_LldpV2SystemInfoMaxNeighbors_Object = MibTableColumn
lldpV2SystemInfoMaxNeighbors = _LldpV2SystemInfoMaxNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 2, 1, 1, 8),
    _LldpV2SystemInfoMaxNeighbors_Type()
)
lldpV2SystemInfoMaxNeighbors.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2SystemInfoMaxNeighbors.setStatus("current")
_LldpV2AgentConfig_ObjectIdentity = ObjectIdentity
lldpV2AgentConfig = _LldpV2AgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3)
)
_LldpV2AgentConfigTable_Object = MibTable
lldpV2AgentConfigTable = _LldpV2AgentConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lldpV2AgentConfigTable.setStatus("current")
_LldpV2AgentConfigEntry_Object = MibTableRow
lldpV2AgentConfigEntry = _LldpV2AgentConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1)
)
lldpV2AgentConfigEntry.setIndexNames(
    (0, "LUM-LLDP-V2-MIB", "lldpV2AgentConfigIndex"),
)
if mibBuilder.loadTexts:
    lldpV2AgentConfigEntry.setStatus("current")


class _LldpV2AgentConfigIndex_Type(Unsigned32):
    """Custom type lldpV2AgentConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2AgentConfigIndex_Type.__name__ = "Unsigned32"
_LldpV2AgentConfigIndex_Object = MibTableColumn
lldpV2AgentConfigIndex = _LldpV2AgentConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 1),
    _LldpV2AgentConfigIndex_Type()
)
lldpV2AgentConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2AgentConfigIndex.setStatus("current")
_LldpV2AgentConfigName_Type = MgmtNameString
_LldpV2AgentConfigName_Object = MibTableColumn
lldpV2AgentConfigName = _LldpV2AgentConfigName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 2),
    _LldpV2AgentConfigName_Type()
)
lldpV2AgentConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2AgentConfigName.setStatus("current")


class _LldpV2AgentConfigLocalMacAddress_Type(OctetString):
    """Custom type lldpV2AgentConfigLocalMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_LldpV2AgentConfigLocalMacAddress_Type.__name__ = "OctetString"
_LldpV2AgentConfigLocalMacAddress_Object = MibTableColumn
lldpV2AgentConfigLocalMacAddress = _LldpV2AgentConfigLocalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 3),
    _LldpV2AgentConfigLocalMacAddress_Type()
)
lldpV2AgentConfigLocalMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2AgentConfigLocalMacAddress.setStatus("current")


class _LldpV2AgentConfigDestMacAddress_Type(OctetString):
    """Custom type lldpV2AgentConfigDestMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_LldpV2AgentConfigDestMacAddress_Type.__name__ = "OctetString"
_LldpV2AgentConfigDestMacAddress_Object = MibTableColumn
lldpV2AgentConfigDestMacAddress = _LldpV2AgentConfigDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 4),
    _LldpV2AgentConfigDestMacAddress_Type()
)
lldpV2AgentConfigDestMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2AgentConfigDestMacAddress.setStatus("current")


class _LldpV2AgentConfigAdminStatus_Type(Integer32):
    """Custom type lldpV2AgentConfigAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("txAndRx", 2))
    )


_LldpV2AgentConfigAdminStatus_Type.__name__ = "Integer32"
_LldpV2AgentConfigAdminStatus_Object = MibTableColumn
lldpV2AgentConfigAdminStatus = _LldpV2AgentConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 5),
    _LldpV2AgentConfigAdminStatus_Type()
)
lldpV2AgentConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2AgentConfigAdminStatus.setStatus("current")


class _LldpV2AgentConfigNotificationEnable_Type(TruthValue):
    """Custom type lldpV2AgentConfigNotificationEnable based on TruthValue"""
    defaultValue = 2


_LldpV2AgentConfigNotificationEnable_Type.__name__ = "TruthValue"
_LldpV2AgentConfigNotificationEnable_Object = MibTableColumn
lldpV2AgentConfigNotificationEnable = _LldpV2AgentConfigNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 6),
    _LldpV2AgentConfigNotificationEnable_Type()
)
lldpV2AgentConfigNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2AgentConfigNotificationEnable.setStatus("current")


class _LldpV2AgentConfigMessageTxInterval_Type(Unsigned32):
    """Custom type lldpV2AgentConfigMessageTxInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_LldpV2AgentConfigMessageTxInterval_Type.__name__ = "Unsigned32"
_LldpV2AgentConfigMessageTxInterval_Object = MibTableColumn
lldpV2AgentConfigMessageTxInterval = _LldpV2AgentConfigMessageTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 7),
    _LldpV2AgentConfigMessageTxInterval_Type()
)
lldpV2AgentConfigMessageTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2AgentConfigMessageTxInterval.setStatus("current")
_LldpV2AgentConfigRxPort_Type = PortNumber
_LldpV2AgentConfigRxPort_Object = MibTableColumn
lldpV2AgentConfigRxPort = _LldpV2AgentConfigRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 8),
    _LldpV2AgentConfigRxPort_Type()
)
lldpV2AgentConfigRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2AgentConfigRxPort.setStatus("current")
_LldpV2AgentConfigTxPort_Type = PortNumber
_LldpV2AgentConfigTxPort_Object = MibTableColumn
lldpV2AgentConfigTxPort = _LldpV2AgentConfigTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 9),
    _LldpV2AgentConfigTxPort_Type()
)
lldpV2AgentConfigTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2AgentConfigTxPort.setStatus("current")


class _LldpV2AgentConfigUpPort_Type(Integer32):
    """Custom type lldpV2AgentConfigUpPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LldpV2AgentConfigUpPort_Type.__name__ = "Integer32"
_LldpV2AgentConfigUpPort_Object = MibTableColumn
lldpV2AgentConfigUpPort = _LldpV2AgentConfigUpPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 10),
    _LldpV2AgentConfigUpPort_Type()
)
lldpV2AgentConfigUpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2AgentConfigUpPort.setStatus("current")


class _LldpV2AgentConfigAgentId_Type(Integer32):
    """Custom type lldpV2AgentConfigAgentId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LldpV2AgentConfigAgentId_Type.__name__ = "Integer32"
_LldpV2AgentConfigAgentId_Object = MibTableColumn
lldpV2AgentConfigAgentId = _LldpV2AgentConfigAgentId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 11),
    _LldpV2AgentConfigAgentId_Type()
)
lldpV2AgentConfigAgentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2AgentConfigAgentId.setStatus("current")
_LldpV2AgentConfigIfNo_Type = PortNumber
_LldpV2AgentConfigIfNo_Object = MibTableColumn
lldpV2AgentConfigIfNo = _LldpV2AgentConfigIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 12),
    _LldpV2AgentConfigIfNo_Type()
)
lldpV2AgentConfigIfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2AgentConfigIfNo.setStatus("current")


class _LldpV2AgentConfigPortDesc_Type(SnmpAdminString):
    """Custom type lldpV2AgentConfigPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LldpV2AgentConfigPortDesc_Type.__name__ = "SnmpAdminString"
_LldpV2AgentConfigPortDesc_Object = MibTableColumn
lldpV2AgentConfigPortDesc = _LldpV2AgentConfigPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 3, 1, 1, 13),
    _LldpV2AgentConfigPortDesc_Type()
)
lldpV2AgentConfigPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2AgentConfigPortDesc.setStatus("current")
_LldpV2RemoteSystemData_ObjectIdentity = ObjectIdentity
lldpV2RemoteSystemData = _LldpV2RemoteSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4)
)
_LldpV2RemTable_Object = MibTable
lldpV2RemTable = _LldpV2RemTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lldpV2RemTable.setStatus("current")
_LldpV2RemEntry_Object = MibTableRow
lldpV2RemEntry = _LldpV2RemEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1)
)
lldpV2RemEntry.setIndexNames(
    (0, "LUM-LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpV2RemEntry.setStatus("current")


class _LldpV2RemIndex_Type(Unsigned32):
    """Custom type lldpV2RemIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemIndex_Type.__name__ = "Unsigned32"
_LldpV2RemIndex_Object = MibTableColumn
lldpV2RemIndex = _LldpV2RemIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 1),
    _LldpV2RemIndex_Type()
)
lldpV2RemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemIndex.setStatus("current")
_LldpV2RemName_Type = MgmtNameString
_LldpV2RemName_Object = MibTableColumn
lldpV2RemName = _LldpV2RemName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 2),
    _LldpV2RemName_Type()
)
lldpV2RemName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemName.setStatus("current")


class _LldpV2RemLocalIfIndex_Type(Unsigned32):
    """Custom type lldpV2RemLocalIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemLocalIfIndex_Type.__name__ = "Unsigned32"
_LldpV2RemLocalIfIndex_Object = MibTableColumn
lldpV2RemLocalIfIndex = _LldpV2RemLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 3),
    _LldpV2RemLocalIfIndex_Type()
)
lldpV2RemLocalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemLocalIfIndex.setStatus("current")


class _LldpV2RemSourceMACAddress_Type(OctetString):
    """Custom type lldpV2RemSourceMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_LldpV2RemSourceMACAddress_Type.__name__ = "OctetString"
_LldpV2RemSourceMACAddress_Object = MibTableColumn
lldpV2RemSourceMACAddress = _LldpV2RemSourceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 4),
    _LldpV2RemSourceMACAddress_Type()
)
lldpV2RemSourceMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemSourceMACAddress.setStatus("current")
_LldpV2RemChassisIdSubtype_Type = LldpV2ChassisIdSubtype
_LldpV2RemChassisIdSubtype_Object = MibTableColumn
lldpV2RemChassisIdSubtype = _LldpV2RemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 5),
    _LldpV2RemChassisIdSubtype_Type()
)
lldpV2RemChassisIdSubtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemChassisIdSubtype.setStatus("current")
_LldpV2RemChassisId_Type = LldpV2ChassisId
_LldpV2RemChassisId_Object = MibTableColumn
lldpV2RemChassisId = _LldpV2RemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 6),
    _LldpV2RemChassisId_Type()
)
lldpV2RemChassisId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemChassisId.setStatus("current")
_LldpV2RemPortIdSubtype_Type = LldpV2PortIdSubtype
_LldpV2RemPortIdSubtype_Object = MibTableColumn
lldpV2RemPortIdSubtype = _LldpV2RemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 7),
    _LldpV2RemPortIdSubtype_Type()
)
lldpV2RemPortIdSubtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemPortIdSubtype.setStatus("current")
_LldpV2RemPortId_Type = LldpV2PortId
_LldpV2RemPortId_Object = MibTableColumn
lldpV2RemPortId = _LldpV2RemPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 8),
    _LldpV2RemPortId_Type()
)
lldpV2RemPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemPortId.setStatus("current")


class _LldpV2RemPortDesc_Type(SnmpAdminString):
    """Custom type lldpV2RemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_LldpV2RemPortDesc_Type.__name__ = "SnmpAdminString"
_LldpV2RemPortDesc_Object = MibTableColumn
lldpV2RemPortDesc = _LldpV2RemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 9),
    _LldpV2RemPortDesc_Type()
)
lldpV2RemPortDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemPortDesc.setStatus("current")


class _LldpV2RemSysName_Type(SnmpAdminString):
    """Custom type lldpV2RemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpV2RemSysName_Type.__name__ = "SnmpAdminString"
_LldpV2RemSysName_Object = MibTableColumn
lldpV2RemSysName = _LldpV2RemSysName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 10),
    _LldpV2RemSysName_Type()
)
lldpV2RemSysName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemSysName.setStatus("current")


class _LldpV2RemSysDesc_Type(SnmpAdminString):
    """Custom type lldpV2RemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpV2RemSysDesc_Type.__name__ = "SnmpAdminString"
_LldpV2RemSysDesc_Object = MibTableColumn
lldpV2RemSysDesc = _LldpV2RemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 11),
    _LldpV2RemSysDesc_Type()
)
lldpV2RemSysDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemSysDesc.setStatus("current")


class _LldpV2RemSysCapEnabled_Type(OctetString):
    """Custom type lldpV2RemSysCapEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LldpV2RemSysCapEnabled_Type.__name__ = "OctetString"
_LldpV2RemSysCapEnabled_Object = MibTableColumn
lldpV2RemSysCapEnabled = _LldpV2RemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 12),
    _LldpV2RemSysCapEnabled_Type()
)
lldpV2RemSysCapEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemSysCapEnabled.setStatus("current")


class _LldpV2RemSysCapSupported_Type(OctetString):
    """Custom type lldpV2RemSysCapSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LldpV2RemSysCapSupported_Type.__name__ = "OctetString"
_LldpV2RemSysCapSupported_Object = MibTableColumn
lldpV2RemSysCapSupported = _LldpV2RemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 13),
    _LldpV2RemSysCapSupported_Type()
)
lldpV2RemSysCapSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemSysCapSupported.setStatus("current")
_LldpV2RemManAddrSubtype_Type = LumAddressFamilyNumbers
_LldpV2RemManAddrSubtype_Object = MibTableColumn
lldpV2RemManAddrSubtype = _LldpV2RemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 14),
    _LldpV2RemManAddrSubtype_Type()
)
lldpV2RemManAddrSubtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemManAddrSubtype.setStatus("current")
_LldpV2RemManAddr_Type = LldpV2ManAddress
_LldpV2RemManAddr_Object = MibTableColumn
lldpV2RemManAddr = _LldpV2RemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 15),
    _LldpV2RemManAddr_Type()
)
lldpV2RemManAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemManAddr.setStatus("current")
_LldpV2RemManAddrIfSubtype_Type = LldpV2ManAddrIfSubtype
_LldpV2RemManAddrIfSubtype_Object = MibTableColumn
lldpV2RemManAddrIfSubtype = _LldpV2RemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 16),
    _LldpV2RemManAddrIfSubtype_Type()
)
lldpV2RemManAddrIfSubtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemManAddrIfSubtype.setStatus("current")


class _LldpV2RemManAddrIfId_Type(Unsigned32):
    """Custom type lldpV2RemManAddrIfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483644),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_LldpV2RemManAddrIfId_Type.__name__ = "Unsigned32"
_LldpV2RemManAddrIfId_Object = MibTableColumn
lldpV2RemManAddrIfId = _LldpV2RemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 17),
    _LldpV2RemManAddrIfId_Type()
)
lldpV2RemManAddrIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemManAddrIfId.setStatus("current")


class _LldpV2RemManAddrOID_Type(OctetString):
    """Custom type lldpV2RemManAddrOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LldpV2RemManAddrOID_Type.__name__ = "OctetString"
_LldpV2RemManAddrOID_Object = MibTableColumn
lldpV2RemManAddrOID = _LldpV2RemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 18),
    _LldpV2RemManAddrOID_Type()
)
lldpV2RemManAddrOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemManAddrOID.setStatus("current")
_LldpV2RemTooManyNeighbors_Type = TruthValue
_LldpV2RemTooManyNeighbors_Object = MibTableColumn
lldpV2RemTooManyNeighbors = _LldpV2RemTooManyNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 19),
    _LldpV2RemTooManyNeighbors_Type()
)
lldpV2RemTooManyNeighbors.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemTooManyNeighbors.setStatus("current")


class _LldpV2RemMtuSize_Type(Unsigned32):
    """Custom type lldpV2RemMtuSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpV2RemMtuSize_Type.__name__ = "Unsigned32"
_LldpV2RemMtuSize_Object = MibTableColumn
lldpV2RemMtuSize = _LldpV2RemMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 20),
    _LldpV2RemMtuSize_Type()
)
lldpV2RemMtuSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemMtuSize.setStatus("current")


class _LldpV2RemLagId_Type(Unsigned32):
    """Custom type lldpV2RemLagId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LldpV2RemLagId_Type.__name__ = "Unsigned32"
_LldpV2RemLagId_Object = MibTableColumn
lldpV2RemLagId = _LldpV2RemLagId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 21),
    _LldpV2RemLagId_Type()
)
lldpV2RemLagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemLagId.setStatus("current")
_LldpV2RemLagisAggCapable_Type = TruthValueWithNA
_LldpV2RemLagisAggCapable_Object = MibTableColumn
lldpV2RemLagisAggCapable = _LldpV2RemLagisAggCapable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 22),
    _LldpV2RemLagisAggCapable_Type()
)
lldpV2RemLagisAggCapable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemLagisAggCapable.setStatus("current")
_LldpV2RemLagisAggregated_Type = TruthValueWithNA
_LldpV2RemLagisAggregated_Object = MibTableColumn
lldpV2RemLagisAggregated = _LldpV2RemLagisAggregated_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 23),
    _LldpV2RemLagisAggregated_Type()
)
lldpV2RemLagisAggregated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemLagisAggregated.setStatus("current")


class _LldpV2RemUpTime_Type(Unsigned32):
    """Custom type lldpV2RemUpTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemUpTime_Type.__name__ = "Unsigned32"
_LldpV2RemUpTime_Object = MibTableColumn
lldpV2RemUpTime = _LldpV2RemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 24),
    _LldpV2RemUpTime_Type()
)
lldpV2RemUpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemUpTime.setStatus("current")


class _LldpV2RemTimeout_Type(Unsigned32):
    """Custom type lldpV2RemTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemTimeout_Type.__name__ = "Unsigned32"
_LldpV2RemTimeout_Object = MibTableColumn
lldpV2RemTimeout = _LldpV2RemTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 25),
    _LldpV2RemTimeout_Type()
)
lldpV2RemTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemTimeout.setStatus("current")


class _LldpV2RemTTL_Type(Unsigned32):
    """Custom type lldpV2RemTTL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemTTL_Type.__name__ = "Unsigned32"
_LldpV2RemTTL_Object = MibTableColumn
lldpV2RemTTL = _LldpV2RemTTL_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 26),
    _LldpV2RemTTL_Type()
)
lldpV2RemTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemTTL.setStatus("current")
_LldpV2RemSubrack_Type = SubrackNumber
_LldpV2RemSubrack_Object = MibTableColumn
lldpV2RemSubrack = _LldpV2RemSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 27),
    _LldpV2RemSubrack_Type()
)
lldpV2RemSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemSubrack.setStatus("current")
_LldpV2RemSlot_Type = SlotNumber
_LldpV2RemSlot_Object = MibTableColumn
lldpV2RemSlot = _LldpV2RemSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 28),
    _LldpV2RemSlot_Type()
)
lldpV2RemSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemSlot.setStatus("current")
_LldpV2RemTxPort_Type = PortNumber
_LldpV2RemTxPort_Object = MibTableColumn
lldpV2RemTxPort = _LldpV2RemTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 29),
    _LldpV2RemTxPort_Type()
)
lldpV2RemTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemTxPort.setStatus("current")
_LldpV2RemRxPort_Type = PortNumber
_LldpV2RemRxPort_Object = MibTableColumn
lldpV2RemRxPort = _LldpV2RemRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 30),
    _LldpV2RemRxPort_Type()
)
lldpV2RemRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemRxPort.setStatus("current")


class _LldpV2RemIdx_Type(Integer32):
    """Custom type lldpV2RemIdx based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LldpV2RemIdx_Type.__name__ = "Integer32"
_LldpV2RemIdx_Object = MibTableColumn
lldpV2RemIdx = _LldpV2RemIdx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 31),
    _LldpV2RemIdx_Type()
)
lldpV2RemIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemIdx.setStatus("current")


class _LldpV2RemIfNo_Type(PortNumber):
    """Custom type lldpV2RemIfNo based on PortNumber"""
    defaultValue = 1


_LldpV2RemIfNo_Type.__name__ = "PortNumber"
_LldpV2RemIfNo_Object = MibTableColumn
lldpV2RemIfNo = _LldpV2RemIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 32),
    _LldpV2RemIfNo_Type()
)
lldpV2RemIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemIfNo.setStatus("current")


class _LldpV2RemUpPortId_Type(Integer32):
    """Custom type lldpV2RemUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LldpV2RemUpPortId_Type.__name__ = "Integer32"
_LldpV2RemUpPortId_Object = MibTableColumn
lldpV2RemUpPortId = _LldpV2RemUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 33),
    _LldpV2RemUpPortId_Type()
)
lldpV2RemUpPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemUpPortId.setStatus("current")


class _LldpV2RemAgentId_Type(Integer32):
    """Custom type lldpV2RemAgentId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LldpV2RemAgentId_Type.__name__ = "Integer32"
_LldpV2RemAgentId_Object = MibTableColumn
lldpV2RemAgentId = _LldpV2RemAgentId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 4, 1, 1, 34),
    _LldpV2RemAgentId_Type()
)
lldpV2RemAgentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2RemAgentId.setStatus("current")
_LldpV2Statistics_ObjectIdentity = ObjectIdentity
lldpV2Statistics = _LldpV2Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5)
)
_LldpV2StatsTable_Object = MibTable
lldpV2StatsTable = _LldpV2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lldpV2StatsTable.setStatus("current")
_LldpV2StatsEntry_Object = MibTableRow
lldpV2StatsEntry = _LldpV2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1)
)
lldpV2StatsEntry.setIndexNames(
    (0, "LUM-LLDP-V2-MIB", "lldpV2StatsIndex"),
)
if mibBuilder.loadTexts:
    lldpV2StatsEntry.setStatus("current")


class _LldpV2StatsIndex_Type(Unsigned32):
    """Custom type lldpV2StatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2StatsIndex_Type.__name__ = "Unsigned32"
_LldpV2StatsIndex_Object = MibTableColumn
lldpV2StatsIndex = _LldpV2StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 1),
    _LldpV2StatsIndex_Type()
)
lldpV2StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsIndex.setStatus("current")


class _LldpV2StatsAgentId_Type(Integer32):
    """Custom type lldpV2StatsAgentId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LldpV2StatsAgentId_Type.__name__ = "Integer32"
_LldpV2StatsAgentId_Object = MibTableColumn
lldpV2StatsAgentId = _LldpV2StatsAgentId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 2),
    _LldpV2StatsAgentId_Type()
)
lldpV2StatsAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsAgentId.setStatus("current")
_LldpV2StatsName_Type = MgmtNameString
_LldpV2StatsName_Object = MibTableColumn
lldpV2StatsName = _LldpV2StatsName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 3),
    _LldpV2StatsName_Type()
)
lldpV2StatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsName.setStatus("current")
_LldpV2StatsTxPortFramesTotal_Type = Counter32
_LldpV2StatsTxPortFramesTotal_Object = MibTableColumn
lldpV2StatsTxPortFramesTotal = _LldpV2StatsTxPortFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 4),
    _LldpV2StatsTxPortFramesTotal_Type()
)
lldpV2StatsTxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsTxPortFramesTotal.setStatus("current")
_LldpV2StatsRxPortFramesDiscardedTotal_Type = Counter32
_LldpV2StatsRxPortFramesDiscardedTotal_Object = MibTableColumn
lldpV2StatsRxPortFramesDiscardedTotal = _LldpV2StatsRxPortFramesDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 5),
    _LldpV2StatsRxPortFramesDiscardedTotal_Type()
)
lldpV2StatsRxPortFramesDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortFramesDiscardedTotal.setStatus("current")
_LldpV2StatsRxPortFramesErrors_Type = Counter32
_LldpV2StatsRxPortFramesErrors_Object = MibTableColumn
lldpV2StatsRxPortFramesErrors = _LldpV2StatsRxPortFramesErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 6),
    _LldpV2StatsRxPortFramesErrors_Type()
)
lldpV2StatsRxPortFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortFramesErrors.setStatus("current")
_LldpV2StatsRxPortFramesTotal_Type = Counter32
_LldpV2StatsRxPortFramesTotal_Object = MibTableColumn
lldpV2StatsRxPortFramesTotal = _LldpV2StatsRxPortFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 7),
    _LldpV2StatsRxPortFramesTotal_Type()
)
lldpV2StatsRxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsRxPortFramesTotal.setStatus("current")
_LldpV2StatsAgeOutsTotal_Type = Counter32
_LldpV2StatsAgeOutsTotal_Object = MibTableColumn
lldpV2StatsAgeOutsTotal = _LldpV2StatsAgeOutsTotal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 8),
    _LldpV2StatsAgeOutsTotal_Type()
)
lldpV2StatsAgeOutsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsAgeOutsTotal.setStatus("current")
_LldpV2StatsTLVSDiscardedTotal_Type = Counter32
_LldpV2StatsTLVSDiscardedTotal_Object = MibTableColumn
lldpV2StatsTLVSDiscardedTotal = _LldpV2StatsTLVSDiscardedTotal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 9),
    _LldpV2StatsTLVSDiscardedTotal_Type()
)
lldpV2StatsTLVSDiscardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsTLVSDiscardedTotal.setStatus("current")
_LldpV2StatsTLVSUnrecognizedTotal_Type = Counter32
_LldpV2StatsTLVSUnrecognizedTotal_Object = MibTableColumn
lldpV2StatsTLVSUnrecognizedTotal = _LldpV2StatsTLVSUnrecognizedTotal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 10),
    _LldpV2StatsTLVSUnrecognizedTotal_Type()
)
lldpV2StatsTLVSUnrecognizedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2StatsTLVSUnrecognizedTotal.setStatus("current")
_LldpV2StatsSubrack_Type = SubrackNumber
_LldpV2StatsSubrack_Object = MibTableColumn
lldpV2StatsSubrack = _LldpV2StatsSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 11),
    _LldpV2StatsSubrack_Type()
)
lldpV2StatsSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2StatsSubrack.setStatus("current")
_LldpV2StatsSlot_Type = SlotNumber
_LldpV2StatsSlot_Object = MibTableColumn
lldpV2StatsSlot = _LldpV2StatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 12),
    _LldpV2StatsSlot_Type()
)
lldpV2StatsSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2StatsSlot.setStatus("current")
_LldpV2StatsTxPort_Type = PortNumber
_LldpV2StatsTxPort_Object = MibTableColumn
lldpV2StatsTxPort = _LldpV2StatsTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 13),
    _LldpV2StatsTxPort_Type()
)
lldpV2StatsTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2StatsTxPort.setStatus("current")
_LldpV2StatsRxPort_Type = PortNumber
_LldpV2StatsRxPort_Object = MibTableColumn
lldpV2StatsRxPort = _LldpV2StatsRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 14),
    _LldpV2StatsRxPort_Type()
)
lldpV2StatsRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2StatsRxPort.setStatus("current")


class _LldpV2StatsIdx_Type(Integer32):
    """Custom type lldpV2StatsIdx based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LldpV2StatsIdx_Type.__name__ = "Integer32"
_LldpV2StatsIdx_Object = MibTableColumn
lldpV2StatsIdx = _LldpV2StatsIdx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 15),
    _LldpV2StatsIdx_Type()
)
lldpV2StatsIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2StatsIdx.setStatus("current")


class _LldpV2StatsIfNo_Type(PortNumber):
    """Custom type lldpV2StatsIfNo based on PortNumber"""
    defaultValue = 1


_LldpV2StatsIfNo_Type.__name__ = "PortNumber"
_LldpV2StatsIfNo_Object = MibTableColumn
lldpV2StatsIfNo = _LldpV2StatsIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 16),
    _LldpV2StatsIfNo_Type()
)
lldpV2StatsIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2StatsIfNo.setStatus("current")


class _LldpV2StatsClientIdx_Type(Integer32):
    """Custom type lldpV2StatsClientIdx based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LldpV2StatsClientIdx_Type.__name__ = "Integer32"
_LldpV2StatsClientIdx_Object = MibTableColumn
lldpV2StatsClientIdx = _LldpV2StatsClientIdx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 17),
    _LldpV2StatsClientIdx_Type()
)
lldpV2StatsClientIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2StatsClientIdx.setStatus("current")


class _LldpV2StatsUpPortId_Type(Integer32):
    """Custom type lldpV2StatsUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LldpV2StatsUpPortId_Type.__name__ = "Integer32"
_LldpV2StatsUpPortId_Object = MibTableColumn
lldpV2StatsUpPortId = _LldpV2StatsUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 18),
    _LldpV2StatsUpPortId_Type()
)
lldpV2StatsUpPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpV2StatsUpPortId.setStatus("current")


class _LldpV2StatsReset_Type(Integer32):
    """Custom type lldpV2StatsReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_LldpV2StatsReset_Type.__name__ = "Integer32"
_LldpV2StatsReset_Object = MibTableColumn
lldpV2StatsReset = _LldpV2StatsReset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 2, 5, 1, 1, 19),
    _LldpV2StatsReset_Type()
)
lldpV2StatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpV2StatsReset.setStatus("current")

# Managed Objects groups

lldpV2GeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1, 1, 1)
)
lldpV2GeneralGroupV1.setObjects(
      *(("LUM-LLDP-V2-MIB", "lldpV2GeneralConfigLastChangeTime"),
        ("LUM-LLDP-V2-MIB", "lldpV2GeneralStateLastChangeTime"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigTableSize"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemSystemDataTableSize"),
        ("LUM-LLDP-V2-MIB", "lldpV2StaticsTableSize"))
)
if mibBuilder.loadTexts:
    lldpV2GeneralGroupV1.setStatus("current")

lldpV2SystemInfoGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1, 1, 2)
)
lldpV2SystemInfoGroupV1.setObjects(
      *(("LUM-LLDP-V2-MIB", "lldpV2SystemInfoIndex"),
        ("LUM-LLDP-V2-MIB", "lldpV2SystemInfoName"),
        ("LUM-LLDP-V2-MIB", "lldpV2SystemInfoSystemName"),
        ("LUM-LLDP-V2-MIB", "lldpV2SystemInfoSystemMacAddress"),
        ("LUM-LLDP-V2-MIB", "lldpV2SystemInfoSystemDescription"),
        ("LUM-LLDP-V2-MIB", "lldpV2SystemInfoManagementIp"),
        ("LUM-LLDP-V2-MIB", "lldpV2SystemInfoManagementOID"),
        ("LUM-LLDP-V2-MIB", "lldpV2SystemInfoMaxNeighbors"))
)
if mibBuilder.loadTexts:
    lldpV2SystemInfoGroupV1.setStatus("current")

lldpV2AgentConfigGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1, 1, 3)
)
lldpV2AgentConfigGroupV1.setObjects(
      *(("LUM-LLDP-V2-MIB", "lldpV2AgentConfigIndex"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigName"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigLocalMacAddress"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigAdminStatus"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigNotificationEnable"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigMessageTxInterval"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigRxPort"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigTxPort"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigUpPort"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigAgentId"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigIfNo"))
)
if mibBuilder.loadTexts:
    lldpV2AgentConfigGroupV1.setStatus("current")

lldpV2RemoteSystemsDataGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1, 1, 4)
)
lldpV2RemoteSystemsDataGroupV1.setObjects(
      *(("LUM-LLDP-V2-MIB", "lldpV2RemIndex"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemName"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemSourceMACAddress"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemChassisIdSubtype"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemChassisId"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemPortIdSubtype"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemPortId"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemPortDesc"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemSysName"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemSysDesc"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemSysCapEnabled"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemSysCapSupported"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemManAddrSubtype"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemManAddr"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemManAddrIfSubtype"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemManAddrIfId"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemManAddrOID"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemTooManyNeighbors"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemMtuSize"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemLagId"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemLagisAggCapable"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemLagisAggregated"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemUpTime"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemTimeout"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemTTL"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemSubrack"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemSlot"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemTxPort"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemRxPort"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemIdx"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemIfNo"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemUpPortId"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemAgentId"))
)
if mibBuilder.loadTexts:
    lldpV2RemoteSystemsDataGroupV1.setStatus("current")

lldpV2StatsGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1, 1, 5)
)
lldpV2StatsGroupV1.setObjects(
      *(("LUM-LLDP-V2-MIB", "lldpV2StatsIndex"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsName"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsAgentId"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsTxPortFramesTotal"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsRxPortFramesDiscardedTotal"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsRxPortFramesErrors"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsRxPortFramesTotal"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsAgeOutsTotal"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsTLVSDiscardedTotal"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsTLVSUnrecognizedTotal"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsSubrack"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsSlot"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsTxPort"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsRxPort"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsIdx"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsIfNo"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsClientIdx"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsUpPortId"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsReset"))
)
if mibBuilder.loadTexts:
    lldpV2StatsGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpV2BasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1, 2, 1)
)
lldpV2BasicComplV1.setObjects(
      *(("LUM-LLDP-V2-MIB", "lldpV2GeneralGroupV1"),
        ("LUM-LLDP-V2-MIB", "lldpV2SystemInfoGroupV1"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigGroupV1"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemoteSystemsDataGroupV1"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsGroupV1"))
)
if mibBuilder.loadTexts:
    lldpV2BasicComplV1.setStatus(
        "deprecated"
    )

lldpV2BasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 67, 1, 2, 2)
)
lldpV2BasicComplV2.setObjects(
      *(("LUM-LLDP-V2-MIB", "lldpV2GeneralGroupV1"),
        ("LUM-LLDP-V2-MIB", "lldpV2SystemInfoGroupV1"),
        ("LUM-LLDP-V2-MIB", "lldpV2AgentConfigGroupV1"),
        ("LUM-LLDP-V2-MIB", "lldpV2RemoteSystemsDataGroupV1"),
        ("LUM-LLDP-V2-MIB", "lldpV2StatsGroupV1"))
)
if mibBuilder.loadTexts:
    lldpV2BasicComplV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-LLDP-V2-MIB",
    **{"LumAddressFamilyNumbers": LumAddressFamilyNumbers,
       "LldpV2ChassisIdSubtype": LldpV2ChassisIdSubtype,
       "LldpV2ChassisId": LldpV2ChassisId,
       "LldpV2PortIdSubtype": LldpV2PortIdSubtype,
       "LldpV2PortId": LldpV2PortId,
       "LldpV2ManAddrIfSubtype": LldpV2ManAddrIfSubtype,
       "LldpV2ManAddress": LldpV2ManAddress,
       "lumLldpV2MIBModule": lumLldpV2MIBModule,
       "lumLldpV2Confs": lumLldpV2Confs,
       "lumLldpV2Groups": lumLldpV2Groups,
       "lldpV2GeneralGroupV1": lldpV2GeneralGroupV1,
       "lldpV2SystemInfoGroupV1": lldpV2SystemInfoGroupV1,
       "lldpV2AgentConfigGroupV1": lldpV2AgentConfigGroupV1,
       "lldpV2RemoteSystemsDataGroupV1": lldpV2RemoteSystemsDataGroupV1,
       "lldpV2StatsGroupV1": lldpV2StatsGroupV1,
       "lumLldpV2Compliances": lumLldpV2Compliances,
       "lldpV2BasicComplV1": lldpV2BasicComplV1,
       "lldpV2BasicComplV2": lldpV2BasicComplV2,
       "lumLldpV2MIBObjects": lumLldpV2MIBObjects,
       "lldpGeneral": lldpGeneral,
       "lldpV2GeneralConfigLastChangeTime": lldpV2GeneralConfigLastChangeTime,
       "lldpV2GeneralStateLastChangeTime": lldpV2GeneralStateLastChangeTime,
       "lldpV2SystemInfoTableSize": lldpV2SystemInfoTableSize,
       "lldpV2AgentConfigTableSize": lldpV2AgentConfigTableSize,
       "lldpV2RemSystemDataTableSize": lldpV2RemSystemDataTableSize,
       "lldpV2StaticsTableSize": lldpV2StaticsTableSize,
       "lldpV2SystemInfo": lldpV2SystemInfo,
       "lldpV2SystemInfoTable": lldpV2SystemInfoTable,
       "lldpV2SystemInfoEntry": lldpV2SystemInfoEntry,
       "lldpV2SystemInfoIndex": lldpV2SystemInfoIndex,
       "lldpV2SystemInfoName": lldpV2SystemInfoName,
       "lldpV2SystemInfoSystemName": lldpV2SystemInfoSystemName,
       "lldpV2SystemInfoSystemDescription": lldpV2SystemInfoSystemDescription,
       "lldpV2SystemInfoSystemMacAddress": lldpV2SystemInfoSystemMacAddress,
       "lldpV2SystemInfoManagementIp": lldpV2SystemInfoManagementIp,
       "lldpV2SystemInfoManagementOID": lldpV2SystemInfoManagementOID,
       "lldpV2SystemInfoMaxNeighbors": lldpV2SystemInfoMaxNeighbors,
       "lldpV2AgentConfig": lldpV2AgentConfig,
       "lldpV2AgentConfigTable": lldpV2AgentConfigTable,
       "lldpV2AgentConfigEntry": lldpV2AgentConfigEntry,
       "lldpV2AgentConfigIndex": lldpV2AgentConfigIndex,
       "lldpV2AgentConfigName": lldpV2AgentConfigName,
       "lldpV2AgentConfigLocalMacAddress": lldpV2AgentConfigLocalMacAddress,
       "lldpV2AgentConfigDestMacAddress": lldpV2AgentConfigDestMacAddress,
       "lldpV2AgentConfigAdminStatus": lldpV2AgentConfigAdminStatus,
       "lldpV2AgentConfigNotificationEnable": lldpV2AgentConfigNotificationEnable,
       "lldpV2AgentConfigMessageTxInterval": lldpV2AgentConfigMessageTxInterval,
       "lldpV2AgentConfigRxPort": lldpV2AgentConfigRxPort,
       "lldpV2AgentConfigTxPort": lldpV2AgentConfigTxPort,
       "lldpV2AgentConfigUpPort": lldpV2AgentConfigUpPort,
       "lldpV2AgentConfigAgentId": lldpV2AgentConfigAgentId,
       "lldpV2AgentConfigIfNo": lldpV2AgentConfigIfNo,
       "lldpV2AgentConfigPortDesc": lldpV2AgentConfigPortDesc,
       "lldpV2RemoteSystemData": lldpV2RemoteSystemData,
       "lldpV2RemTable": lldpV2RemTable,
       "lldpV2RemEntry": lldpV2RemEntry,
       "lldpV2RemIndex": lldpV2RemIndex,
       "lldpV2RemName": lldpV2RemName,
       "lldpV2RemLocalIfIndex": lldpV2RemLocalIfIndex,
       "lldpV2RemSourceMACAddress": lldpV2RemSourceMACAddress,
       "lldpV2RemChassisIdSubtype": lldpV2RemChassisIdSubtype,
       "lldpV2RemChassisId": lldpV2RemChassisId,
       "lldpV2RemPortIdSubtype": lldpV2RemPortIdSubtype,
       "lldpV2RemPortId": lldpV2RemPortId,
       "lldpV2RemPortDesc": lldpV2RemPortDesc,
       "lldpV2RemSysName": lldpV2RemSysName,
       "lldpV2RemSysDesc": lldpV2RemSysDesc,
       "lldpV2RemSysCapEnabled": lldpV2RemSysCapEnabled,
       "lldpV2RemSysCapSupported": lldpV2RemSysCapSupported,
       "lldpV2RemManAddrSubtype": lldpV2RemManAddrSubtype,
       "lldpV2RemManAddr": lldpV2RemManAddr,
       "lldpV2RemManAddrIfSubtype": lldpV2RemManAddrIfSubtype,
       "lldpV2RemManAddrIfId": lldpV2RemManAddrIfId,
       "lldpV2RemManAddrOID": lldpV2RemManAddrOID,
       "lldpV2RemTooManyNeighbors": lldpV2RemTooManyNeighbors,
       "lldpV2RemMtuSize": lldpV2RemMtuSize,
       "lldpV2RemLagId": lldpV2RemLagId,
       "lldpV2RemLagisAggCapable": lldpV2RemLagisAggCapable,
       "lldpV2RemLagisAggregated": lldpV2RemLagisAggregated,
       "lldpV2RemUpTime": lldpV2RemUpTime,
       "lldpV2RemTimeout": lldpV2RemTimeout,
       "lldpV2RemTTL": lldpV2RemTTL,
       "lldpV2RemSubrack": lldpV2RemSubrack,
       "lldpV2RemSlot": lldpV2RemSlot,
       "lldpV2RemTxPort": lldpV2RemTxPort,
       "lldpV2RemRxPort": lldpV2RemRxPort,
       "lldpV2RemIdx": lldpV2RemIdx,
       "lldpV2RemIfNo": lldpV2RemIfNo,
       "lldpV2RemUpPortId": lldpV2RemUpPortId,
       "lldpV2RemAgentId": lldpV2RemAgentId,
       "lldpV2Statistics": lldpV2Statistics,
       "lldpV2StatsTable": lldpV2StatsTable,
       "lldpV2StatsEntry": lldpV2StatsEntry,
       "lldpV2StatsIndex": lldpV2StatsIndex,
       "lldpV2StatsAgentId": lldpV2StatsAgentId,
       "lldpV2StatsName": lldpV2StatsName,
       "lldpV2StatsTxPortFramesTotal": lldpV2StatsTxPortFramesTotal,
       "lldpV2StatsRxPortFramesDiscardedTotal": lldpV2StatsRxPortFramesDiscardedTotal,
       "lldpV2StatsRxPortFramesErrors": lldpV2StatsRxPortFramesErrors,
       "lldpV2StatsRxPortFramesTotal": lldpV2StatsRxPortFramesTotal,
       "lldpV2StatsAgeOutsTotal": lldpV2StatsAgeOutsTotal,
       "lldpV2StatsTLVSDiscardedTotal": lldpV2StatsTLVSDiscardedTotal,
       "lldpV2StatsTLVSUnrecognizedTotal": lldpV2StatsTLVSUnrecognizedTotal,
       "lldpV2StatsSubrack": lldpV2StatsSubrack,
       "lldpV2StatsSlot": lldpV2StatsSlot,
       "lldpV2StatsTxPort": lldpV2StatsTxPort,
       "lldpV2StatsRxPort": lldpV2StatsRxPort,
       "lldpV2StatsIdx": lldpV2StatsIdx,
       "lldpV2StatsIfNo": lldpV2StatsIfNo,
       "lldpV2StatsClientIdx": lldpV2StatsClientIdx,
       "lldpV2StatsUpPortId": lldpV2StatsUpPortId,
       "lldpV2StatsReset": lldpV2StatsReset}
)
