# SNMP MIB module (ECS4810-28TS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/edgecore/ECS4810-28TS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:54:00 2025
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

(BridgeId,
 Timeout,
 dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(MacAddress,) = mibBuilder.importSymbols(
    "TOKEN-RING-RMON-MIB",
    "MacAddress")


# MODULE-IDENTITY

ecs4810_28tsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18)
)
if mibBuilder.loadTexts:
    ecs4810_28tsMIB.setRevisions(
        ("2001-09-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class KeySegment(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class ValidStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )



class StaPathCostMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("long", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Accton_ObjectIdentity = ObjectIdentity
accton = _Accton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259)
)
_Edgecorenetworks_ObjectIdentity = ObjectIdentity
edgecorenetworks = _Edgecorenetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10)
)
_EdgeCoreNetworksMgt_ObjectIdentity = ObjectIdentity
edgeCoreNetworksMgt = _EdgeCoreNetworksMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1)
)
_Ecs4810_28tsMIBObjects_ObjectIdentity = ObjectIdentity
ecs4810_28tsMIBObjects = _Ecs4810_28tsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1)
)
_SwitchMgt_ObjectIdentity = ObjectIdentity
switchMgt = _SwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1)
)


class _SwitchManagementVlan_Type(Integer32):
    """Custom type switchManagementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4092),
    )


_SwitchManagementVlan_Type.__name__ = "Integer32"
_SwitchManagementVlan_Object = MibScalar
switchManagementVlan = _SwitchManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 1),
    _SwitchManagementVlan_Type()
)
switchManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchManagementVlan.setStatus("current")
_SwitchNumber_Type = Integer32
_SwitchNumber_Object = MibScalar
switchNumber = _SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 2),
    _SwitchNumber_Type()
)
switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumber.setStatus("current")
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1)
)
switchInfoEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")


class _SwUnitIndex_Type(Integer32):
    """Custom type swUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SwUnitIndex_Type.__name__ = "Integer32"
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 1),
    _SwUnitIndex_Type()
)
swUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swUnitIndex.setStatus("current")


class _SwHardwareVer_Type(DisplayString):
    """Custom type swHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwHardwareVer_Type.__name__ = "DisplayString"
_SwHardwareVer_Object = MibTableColumn
swHardwareVer = _SwHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 2),
    _SwHardwareVer_Type()
)
swHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareVer.setStatus("current")


class _SwMicrocodeVer_Type(DisplayString):
    """Custom type swMicrocodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwMicrocodeVer_Type.__name__ = "DisplayString"
_SwMicrocodeVer_Object = MibTableColumn
swMicrocodeVer = _SwMicrocodeVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 3),
    _SwMicrocodeVer_Type()
)
swMicrocodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMicrocodeVer.setStatus("current")


class _SwLoaderVer_Type(DisplayString):
    """Custom type swLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwLoaderVer_Type.__name__ = "DisplayString"
_SwLoaderVer_Object = MibTableColumn
swLoaderVer = _SwLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 4),
    _SwLoaderVer_Type()
)
swLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLoaderVer.setStatus("current")


class _SwBootRomVer_Type(DisplayString):
    """Custom type swBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBootRomVer_Type.__name__ = "DisplayString"
_SwBootRomVer_Object = MibTableColumn
swBootRomVer = _SwBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 5),
    _SwBootRomVer_Type()
)
swBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootRomVer.setStatus("current")


class _SwOpCodeVer_Type(DisplayString):
    """Custom type swOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwOpCodeVer_Type.__name__ = "DisplayString"
_SwOpCodeVer_Object = MibTableColumn
swOpCodeVer = _SwOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 6),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("current")
_SwPortNumber_Type = Integer32
_SwPortNumber_Object = MibTableColumn
swPortNumber = _SwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 7),
    _SwPortNumber_Type()
)
swPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortNumber.setStatus("current")


class _SwPowerStatus_Type(Integer32):
    """Custom type swPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalPower", 1),
          ("redundantPower", 2),
          ("internalAndRedundantPower", 3))
    )


_SwPowerStatus_Type.__name__ = "Integer32"
_SwPowerStatus_Object = MibTableColumn
swPowerStatus = _SwPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 8),
    _SwPowerStatus_Type()
)
swPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerStatus.setStatus("current")


class _SwRoleInSystem_Type(Integer32):
    """Custom type swRoleInSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("backupMaster", 2),
          ("slave", 3))
    )


_SwRoleInSystem_Type.__name__ = "Integer32"
_SwRoleInSystem_Object = MibTableColumn
swRoleInSystem = _SwRoleInSystem_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 9),
    _SwRoleInSystem_Type()
)
swRoleInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRoleInSystem.setStatus("current")


class _SwSerialNumber_Type(DisplayString):
    """Custom type swSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwSerialNumber_Type.__name__ = "DisplayString"
_SwSerialNumber_Object = MibTableColumn
swSerialNumber = _SwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 10),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")


class _SwServiceTag_Type(DisplayString):
    """Custom type swServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwServiceTag_Type.__name__ = "DisplayString"
_SwServiceTag_Object = MibTableColumn
swServiceTag = _SwServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 3, 1, 13),
    _SwServiceTag_Type()
)
swServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swServiceTag.setStatus("current")


class _SwitchOperState_Type(Integer32):
    """Custom type switchOperState based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("noncritical", 4),
          ("critical", 5),
          ("nonrecoverable", 6))
    )


_SwitchOperState_Type.__name__ = "Integer32"
_SwitchOperState_Object = MibScalar
switchOperState = _SwitchOperState_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 4),
    _SwitchOperState_Type()
)
switchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOperState.setStatus("current")
_SwitchProductId_ObjectIdentity = ObjectIdentity
switchProductId = _SwitchProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 5)
)


class _SwProdName_Type(DisplayString):
    """Custom type swProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdName_Type.__name__ = "DisplayString"
_SwProdName_Object = MibScalar
swProdName = _SwProdName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 5, 1),
    _SwProdName_Type()
)
swProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdName.setStatus("current")


class _SwProdManufacturer_Type(DisplayString):
    """Custom type swProdManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdManufacturer_Type.__name__ = "DisplayString"
_SwProdManufacturer_Object = MibScalar
swProdManufacturer = _SwProdManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 5, 2),
    _SwProdManufacturer_Type()
)
swProdManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdManufacturer.setStatus("current")


class _SwProdDescription_Type(DisplayString):
    """Custom type swProdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdDescription_Type.__name__ = "DisplayString"
_SwProdDescription_Object = MibScalar
swProdDescription = _SwProdDescription_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 5, 3),
    _SwProdDescription_Type()
)
swProdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdDescription.setStatus("current")


class _SwProdVersion_Type(DisplayString):
    """Custom type swProdVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdVersion_Type.__name__ = "DisplayString"
_SwProdVersion_Object = MibScalar
swProdVersion = _SwProdVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 5, 4),
    _SwProdVersion_Type()
)
swProdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdVersion.setStatus("current")


class _SwProdUrl_Type(DisplayString):
    """Custom type swProdUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdUrl_Type.__name__ = "DisplayString"
_SwProdUrl_Object = MibScalar
swProdUrl = _SwProdUrl_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 5, 5),
    _SwProdUrl_Type()
)
swProdUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdUrl.setStatus("current")
_SwIdentifier_Type = Integer32
_SwIdentifier_Object = MibScalar
swIdentifier = _SwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 5, 6),
    _SwIdentifier_Type()
)
swIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIdentifier.setStatus("current")


class _SwChassisServiceTag_Type(DisplayString):
    """Custom type swChassisServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwChassisServiceTag_Type.__name__ = "DisplayString"
_SwChassisServiceTag_Object = MibScalar
swChassisServiceTag = _SwChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 5, 7),
    _SwChassisServiceTag_Type()
)
swChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swChassisServiceTag.setStatus("current")
_AmtrMgt_ObjectIdentity = ObjectIdentity
amtrMgt = _AmtrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 8)
)
_AmtrMacAddrAgingStatus_Type = EnabledStatus
_AmtrMacAddrAgingStatus_Object = MibScalar
amtrMacAddrAgingStatus = _AmtrMacAddrAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 1, 8, 3),
    _AmtrMacAddrAgingStatus_Type()
)
amtrMacAddrAgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amtrMacAddrAgingStatus.setStatus("current")
_PortMgt_ObjectIdentity = ObjectIdentity
portMgt = _PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1)
)
portEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = InterfaceIndex
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("other", 1),
          ("hundredBaseTX", 2),
          ("hundredBaseFX", 3),
          ("thousandBaseSX", 4),
          ("thousandBaseLX", 5),
          ("thousandBaseT", 6),
          ("thousandBaseGBIC", 7),
          ("thousandBaseSfp", 8),
          ("hundredBaseFxScSingleMode", 9),
          ("hundredBaseFxScMultiMode", 10))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortSpeedDpxCfg_Type(Integer32):
    """Custom type portSpeedDpxCfg based on Integer32"""
    defaultValue = 2

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
        *(("reserved", 1),
          ("halfDuplex10", 2),
          ("fullDuplex10", 3),
          ("halfDuplex100", 4),
          ("fullDuplex100", 5),
          ("halfDuplex1000", 6),
          ("fullDuplex1000", 7))
    )


_PortSpeedDpxCfg_Type.__name__ = "Integer32"
_PortSpeedDpxCfg_Object = MibTableColumn
portSpeedDpxCfg = _PortSpeedDpxCfg_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 4),
    _PortSpeedDpxCfg_Type()
)
portSpeedDpxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedDpxCfg.setStatus("current")


class _PortFlowCtrlCfg_Type(Integer32):
    """Custom type portFlowCtrlCfg based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("backPressure", 3),
          ("dot3xFlowControl", 4))
    )


_PortFlowCtrlCfg_Type.__name__ = "Integer32"
_PortFlowCtrlCfg_Object = MibTableColumn
portFlowCtrlCfg = _PortFlowCtrlCfg_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 5),
    _PortFlowCtrlCfg_Type()
)
portFlowCtrlCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowCtrlCfg.setStatus("current")


class _PortCapabilities_Type(Bits):
    """Custom type portCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("portCap10half", 0),
          ("portCap10full", 1),
          ("portCap100half", 2),
          ("portCap100full", 3),
          ("portCap1000half", 4),
          ("portCap1000full", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("reserved9", 9),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("portCapSym", 14),
          ("portCapFlowCtrl", 15))
    )

_PortCapabilities_Type.__name__ = "Bits"
_PortCapabilities_Object = MibTableColumn
portCapabilities = _PortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")


class _PortAutonegotiation_Type(Integer32):
    """Custom type portAutonegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PortAutonegotiation_Type.__name__ = "Integer32"
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 7),
    _PortAutonegotiation_Type()
)
portAutonegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutonegotiation.setStatus("current")


class _PortSpeedDpxStatus_Type(Integer32):
    """Custom type portSpeedDpxStatus based on Integer32"""
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
        *(("error", 1),
          ("halfDuplex10", 2),
          ("fullDuplex10", 3),
          ("halfDuplex100", 4),
          ("fullDuplex100", 5),
          ("halfDuplex1000", 6),
          ("fullDuplex1000", 7))
    )


_PortSpeedDpxStatus_Type.__name__ = "Integer32"
_PortSpeedDpxStatus_Object = MibTableColumn
portSpeedDpxStatus = _PortSpeedDpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 8),
    _PortSpeedDpxStatus_Type()
)
portSpeedDpxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeedDpxStatus.setStatus("current")


class _PortFlowCtrlStatus_Type(Integer32):
    """Custom type portFlowCtrlStatus based on Integer32"""
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
        *(("error", 1),
          ("backPressure", 2),
          ("dot3xFlowControl", 3),
          ("none", 4))
    )


_PortFlowCtrlStatus_Type.__name__ = "Integer32"
_PortFlowCtrlStatus_Object = MibTableColumn
portFlowCtrlStatus = _PortFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_PortTrunkIndex_Type = Integer32
_PortTrunkIndex_Object = MibTableColumn
portTrunkIndex = _PortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 2, 1, 1, 10),
    _PortTrunkIndex_Type()
)
portTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkIndex.setStatus("current")
_TrunkMgt_ObjectIdentity = ObjectIdentity
trunkMgt = _TrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 3)
)
_TrunkMaxId_Type = Integer32
_TrunkMaxId_Object = MibScalar
trunkMaxId = _TrunkMaxId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 3, 1),
    _TrunkMaxId_Type()
)
trunkMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMaxId.setStatus("current")
_TrunkValidNumber_Type = Integer32
_TrunkValidNumber_Object = MibScalar
trunkValidNumber = _TrunkValidNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 3, 2),
    _TrunkValidNumber_Type()
)
trunkValidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkValidNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 3, 3, 1)
)
trunkEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")


class _TrunkIndex_Type(Integer32):
    """Custom type trunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TrunkIndex_Type.__name__ = "Integer32"
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 3, 3, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 3, 3, 1, 2),
    _TrunkPorts_Type()
)
trunkPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkPorts.setStatus("current")


class _TrunkCreation_Type(Integer32):
    """Custom type trunkCreation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("lacp", 2))
    )


_TrunkCreation_Type.__name__ = "Integer32"
_TrunkCreation_Object = MibTableColumn
trunkCreation = _TrunkCreation_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 3, 3, 1, 3),
    _TrunkCreation_Type()
)
trunkCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCreation.setStatus("current")
_TrunkStatus_Type = ValidStatus
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 3, 3, 1, 4),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_LacpMgt_ObjectIdentity = ObjectIdentity
lacpMgt = _LacpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 4)
)
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 4, 1, 1)
)
lacpPortEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")
_LacpPortIndex_Type = InterfaceIndex
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 4, 1, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")


class _LacpPortStatus_Type(Integer32):
    """Custom type lacpPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_LacpPortStatus_Type.__name__ = "Integer32"
_LacpPortStatus_Object = MibTableColumn
lacpPortStatus = _LacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 4, 1, 1, 2),
    _LacpPortStatus_Type()
)
lacpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortStatus.setStatus("current")
_StaMgt_ObjectIdentity = ObjectIdentity
staMgt = _StaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5)
)


class _StaSystemStatus_Type(EnabledStatus):
    """Custom type staSystemStatus based on EnabledStatus"""
    defaultValue = 1


_StaSystemStatus_Type.__name__ = "EnabledStatus"
_StaSystemStatus_Object = MibScalar
staSystemStatus = _StaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 1),
    _StaSystemStatus_Type()
)
staSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemStatus.setStatus("current")
_StaPortTable_Object = MibTable
staPortTable = _StaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2)
)
if mibBuilder.loadTexts:
    staPortTable.setStatus("current")
_StaPortEntry_Object = MibTableRow
staPortEntry = _StaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1)
)
staPortEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "staPortIndex"),
)
if mibBuilder.loadTexts:
    staPortEntry.setStatus("current")


class _StaPortIndex_Type(Integer32):
    """Custom type staPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_StaPortIndex_Type.__name__ = "Integer32"
_StaPortIndex_Object = MibTableColumn
staPortIndex = _StaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1, 1),
    _StaPortIndex_Type()
)
staPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staPortIndex.setStatus("current")
_StaPortFastForward_Type = EnabledStatus
_StaPortFastForward_Object = MibTableColumn
staPortFastForward = _StaPortFastForward_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1, 2),
    _StaPortFastForward_Type()
)
staPortFastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortFastForward.setStatus("current")
_StaPortProtocolMigration_Type = TruthValue
_StaPortProtocolMigration_Object = MibTableColumn
staPortProtocolMigration = _StaPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1, 3),
    _StaPortProtocolMigration_Type()
)
staPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortProtocolMigration.setStatus("current")
_StaPortAdminEdgePort_Type = TruthValue
_StaPortAdminEdgePort_Object = MibTableColumn
staPortAdminEdgePort = _StaPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1, 4),
    _StaPortAdminEdgePort_Type()
)
staPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminEdgePort.setStatus("current")
_StaPortOperEdgePort_Type = TruthValue
_StaPortOperEdgePort_Object = MibTableColumn
staPortOperEdgePort = _StaPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1, 5),
    _StaPortOperEdgePort_Type()
)
staPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperEdgePort.setStatus("current")


class _StaPortAdminPointToPoint_Type(Integer32):
    """Custom type staPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_StaPortAdminPointToPoint_Type.__name__ = "Integer32"
_StaPortAdminPointToPoint_Object = MibTableColumn
staPortAdminPointToPoint = _StaPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1, 6),
    _StaPortAdminPointToPoint_Type()
)
staPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminPointToPoint.setStatus("current")
_StaPortOperPointToPoint_Type = TruthValue
_StaPortOperPointToPoint_Object = MibTableColumn
staPortOperPointToPoint = _StaPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1, 7),
    _StaPortOperPointToPoint_Type()
)
staPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperPointToPoint.setStatus("current")


class _StaPortLongPathCost_Type(Integer32):
    """Custom type staPortLongPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StaPortLongPathCost_Type.__name__ = "Integer32"
_StaPortLongPathCost_Object = MibTableColumn
staPortLongPathCost = _StaPortLongPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1, 8),
    _StaPortLongPathCost_Type()
)
staPortLongPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortLongPathCost.setStatus("current")


class _StaPortSystemStatus_Type(EnabledStatus):
    """Custom type staPortSystemStatus based on EnabledStatus"""
    defaultValue = 1


_StaPortSystemStatus_Type.__name__ = "EnabledStatus"
_StaPortSystemStatus_Object = MibTableColumn
staPortSystemStatus = _StaPortSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 2, 1, 9),
    _StaPortSystemStatus_Type()
)
staPortSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortSystemStatus.setStatus("current")


class _StaProtocolType_Type(Integer32):
    """Custom type staProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("rstp", 2),
          ("mstp", 3))
    )


_StaProtocolType_Type.__name__ = "Integer32"
_StaProtocolType_Object = MibScalar
staProtocolType = _StaProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 3),
    _StaProtocolType_Type()
)
staProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staProtocolType.setStatus("current")


class _StaTxHoldCount_Type(Integer32):
    """Custom type staTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StaTxHoldCount_Type.__name__ = "Integer32"
_StaTxHoldCount_Object = MibScalar
staTxHoldCount = _StaTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 4),
    _StaTxHoldCount_Type()
)
staTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staTxHoldCount.setStatus("current")


class _StaPathCostMethod_Type(StaPathCostMode):
    """Custom type staPathCostMethod based on StaPathCostMode"""
    defaultValue = 1


_StaPathCostMethod_Type.__name__ = "StaPathCostMode"
_StaPathCostMethod_Object = MibScalar
staPathCostMethod = _StaPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 5),
    _StaPathCostMethod_Type()
)
staPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPathCostMethod.setStatus("current")
_XstMgt_ObjectIdentity = ObjectIdentity
xstMgt = _XstMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6)
)


class _MstName_Type(DisplayString):
    """Custom type mstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MstName_Type.__name__ = "DisplayString"
_MstName_Object = MibScalar
mstName = _MstName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 1),
    _MstName_Type()
)
mstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstName.setStatus("current")
_MstRevision_Type = Integer32
_MstRevision_Object = MibScalar
mstRevision = _MstRevision_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 2),
    _MstRevision_Type()
)
mstRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstRevision.setStatus("current")


class _MstMaxHops_Type(Integer32):
    """Custom type mstMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_MstMaxHops_Type.__name__ = "Integer32"
_MstMaxHops_Object = MibScalar
mstMaxHops = _MstMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 3),
    _MstMaxHops_Type()
)
mstMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMaxHops.setStatus("current")
_XstInstanceCfgTable_Object = MibTable
xstInstanceCfgTable = _XstInstanceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    xstInstanceCfgTable.setStatus("current")
_XstInstanceCfgEntry_Object = MibTableRow
xstInstanceCfgEntry = _XstInstanceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1)
)
xstInstanceCfgEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "xstInstanceCfgIndex"),
)
if mibBuilder.loadTexts:
    xstInstanceCfgEntry.setStatus("current")


class _XstInstanceCfgIndex_Type(Integer32):
    """Custom type xstInstanceCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_XstInstanceCfgIndex_Type.__name__ = "Integer32"
_XstInstanceCfgIndex_Object = MibTableColumn
xstInstanceCfgIndex = _XstInstanceCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 1),
    _XstInstanceCfgIndex_Type()
)
xstInstanceCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstanceCfgIndex.setStatus("current")


class _XstInstanceCfgPriority_Type(Integer32):
    """Custom type xstInstanceCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_XstInstanceCfgPriority_Type.__name__ = "Integer32"
_XstInstanceCfgPriority_Object = MibTableColumn
xstInstanceCfgPriority = _XstInstanceCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 2),
    _XstInstanceCfgPriority_Type()
)
xstInstanceCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstanceCfgPriority.setStatus("current")
_XstInstanceCfgTimeSinceTopologyChange_Type = TimeTicks
_XstInstanceCfgTimeSinceTopologyChange_Object = MibTableColumn
xstInstanceCfgTimeSinceTopologyChange = _XstInstanceCfgTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 3),
    _XstInstanceCfgTimeSinceTopologyChange_Type()
)
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTimeSinceTopologyChange.setStatus("current")
_XstInstanceCfgTopChanges_Type = Integer32
_XstInstanceCfgTopChanges_Object = MibTableColumn
xstInstanceCfgTopChanges = _XstInstanceCfgTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 4),
    _XstInstanceCfgTopChanges_Type()
)
xstInstanceCfgTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTopChanges.setStatus("current")
_XstInstanceCfgDesignatedRoot_Type = BridgeId
_XstInstanceCfgDesignatedRoot_Object = MibTableColumn
xstInstanceCfgDesignatedRoot = _XstInstanceCfgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 5),
    _XstInstanceCfgDesignatedRoot_Type()
)
xstInstanceCfgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgDesignatedRoot.setStatus("current")
_XstInstanceCfgRootCost_Type = Integer32
_XstInstanceCfgRootCost_Object = MibTableColumn
xstInstanceCfgRootCost = _XstInstanceCfgRootCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 6),
    _XstInstanceCfgRootCost_Type()
)
xstInstanceCfgRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootCost.setStatus("current")
_XstInstanceCfgRootPort_Type = Integer32
_XstInstanceCfgRootPort_Object = MibTableColumn
xstInstanceCfgRootPort = _XstInstanceCfgRootPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 7),
    _XstInstanceCfgRootPort_Type()
)
xstInstanceCfgRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootPort.setStatus("current")
_XstInstanceCfgMaxAge_Type = Timeout
_XstInstanceCfgMaxAge_Object = MibTableColumn
xstInstanceCfgMaxAge = _XstInstanceCfgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 8),
    _XstInstanceCfgMaxAge_Type()
)
xstInstanceCfgMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgMaxAge.setStatus("current")
_XstInstanceCfgHelloTime_Type = Timeout
_XstInstanceCfgHelloTime_Object = MibTableColumn
xstInstanceCfgHelloTime = _XstInstanceCfgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 9),
    _XstInstanceCfgHelloTime_Type()
)
xstInstanceCfgHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHelloTime.setStatus("current")
_XstInstanceCfgHoldTime_Type = Timeout
_XstInstanceCfgHoldTime_Object = MibTableColumn
xstInstanceCfgHoldTime = _XstInstanceCfgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 10),
    _XstInstanceCfgHoldTime_Type()
)
xstInstanceCfgHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHoldTime.setStatus("current")
_XstInstanceCfgForwardDelay_Type = Timeout
_XstInstanceCfgForwardDelay_Object = MibTableColumn
xstInstanceCfgForwardDelay = _XstInstanceCfgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 11),
    _XstInstanceCfgForwardDelay_Type()
)
xstInstanceCfgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgForwardDelay.setStatus("current")
_XstInstanceCfgBridgeMaxAge_Type = Timeout
_XstInstanceCfgBridgeMaxAge_Object = MibTableColumn
xstInstanceCfgBridgeMaxAge = _XstInstanceCfgBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 12),
    _XstInstanceCfgBridgeMaxAge_Type()
)
xstInstanceCfgBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeMaxAge.setStatus("current")
_XstInstanceCfgBridgeHelloTime_Type = Timeout
_XstInstanceCfgBridgeHelloTime_Object = MibTableColumn
xstInstanceCfgBridgeHelloTime = _XstInstanceCfgBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 13),
    _XstInstanceCfgBridgeHelloTime_Type()
)
xstInstanceCfgBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeHelloTime.setStatus("current")
_XstInstanceCfgBridgeForwardDelay_Type = Timeout
_XstInstanceCfgBridgeForwardDelay_Object = MibTableColumn
xstInstanceCfgBridgeForwardDelay = _XstInstanceCfgBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 14),
    _XstInstanceCfgBridgeForwardDelay_Type()
)
xstInstanceCfgBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeForwardDelay.setStatus("current")
_XstInstanceCfgTxHoldCount_Type = Integer32
_XstInstanceCfgTxHoldCount_Object = MibTableColumn
xstInstanceCfgTxHoldCount = _XstInstanceCfgTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 15),
    _XstInstanceCfgTxHoldCount_Type()
)
xstInstanceCfgTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTxHoldCount.setStatus("current")
_XstInstanceCfgPathCostMethod_Type = StaPathCostMode
_XstInstanceCfgPathCostMethod_Object = MibTableColumn
xstInstanceCfgPathCostMethod = _XstInstanceCfgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 4, 1, 16),
    _XstInstanceCfgPathCostMethod_Type()
)
xstInstanceCfgPathCostMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgPathCostMethod.setStatus("current")
_XstInstancePortTable_Object = MibTable
xstInstancePortTable = _XstInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    xstInstancePortTable.setStatus("current")
_XstInstancePortEntry_Object = MibTableRow
xstInstancePortEntry = _XstInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1)
)
xstInstancePortEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "xstInstancePortInstance"),
    (0, "ECS4810-28TS-MIB", "xstInstancePortPort"),
)
if mibBuilder.loadTexts:
    xstInstancePortEntry.setStatus("current")


class _XstInstancePortInstance_Type(Integer32):
    """Custom type xstInstancePortInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_XstInstancePortInstance_Type.__name__ = "Integer32"
_XstInstancePortInstance_Object = MibTableColumn
xstInstancePortInstance = _XstInstancePortInstance_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 1),
    _XstInstancePortInstance_Type()
)
xstInstancePortInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstancePortInstance.setStatus("current")


class _XstInstancePortPort_Type(Integer32):
    """Custom type xstInstancePortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_XstInstancePortPort_Type.__name__ = "Integer32"
_XstInstancePortPort_Object = MibTableColumn
xstInstancePortPort = _XstInstancePortPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 2),
    _XstInstancePortPort_Type()
)
xstInstancePortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstancePortPort.setStatus("current")


class _XstInstancePortPriority_Type(Integer32):
    """Custom type xstInstancePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_XstInstancePortPriority_Type.__name__ = "Integer32"
_XstInstancePortPriority_Object = MibTableColumn
xstInstancePortPriority = _XstInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 3),
    _XstInstancePortPriority_Type()
)
xstInstancePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortPriority.setStatus("current")


class _XstInstancePortState_Type(Integer32):
    """Custom type xstInstancePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("learning", 2),
          ("forwarding", 3))
    )


_XstInstancePortState_Type.__name__ = "Integer32"
_XstInstancePortState_Object = MibTableColumn
xstInstancePortState = _XstInstancePortState_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 4),
    _XstInstancePortState_Type()
)
xstInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortState.setStatus("current")
_XstInstancePortEnable_Type = EnabledStatus
_XstInstancePortEnable_Object = MibTableColumn
xstInstancePortEnable = _XstInstancePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 5),
    _XstInstancePortEnable_Type()
)
xstInstancePortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortEnable.setStatus("current")


class _XstInstancePortPathCost_Type(Integer32):
    """Custom type xstInstancePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_XstInstancePortPathCost_Type.__name__ = "Integer32"
_XstInstancePortPathCost_Object = MibTableColumn
xstInstancePortPathCost = _XstInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 6),
    _XstInstancePortPathCost_Type()
)
xstInstancePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortPathCost.setStatus("current")
_XstInstancePortDesignatedRoot_Type = BridgeId
_XstInstancePortDesignatedRoot_Object = MibTableColumn
xstInstancePortDesignatedRoot = _XstInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 7),
    _XstInstancePortDesignatedRoot_Type()
)
xstInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedRoot.setStatus("current")
_XstInstancePortDesignatedCost_Type = Integer32
_XstInstancePortDesignatedCost_Object = MibTableColumn
xstInstancePortDesignatedCost = _XstInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 8),
    _XstInstancePortDesignatedCost_Type()
)
xstInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedCost.setStatus("current")
_XstInstancePortDesignatedBridge_Type = BridgeId
_XstInstancePortDesignatedBridge_Object = MibTableColumn
xstInstancePortDesignatedBridge = _XstInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 9),
    _XstInstancePortDesignatedBridge_Type()
)
xstInstancePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedBridge.setStatus("current")


class _XstInstancePortDesignatedPort_Type(OctetString):
    """Custom type xstInstancePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_XstInstancePortDesignatedPort_Type.__name__ = "OctetString"
_XstInstancePortDesignatedPort_Object = MibTableColumn
xstInstancePortDesignatedPort = _XstInstancePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 10),
    _XstInstancePortDesignatedPort_Type()
)
xstInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedPort.setStatus("current")
_XstInstancePortForwardTransitions_Type = Counter32
_XstInstancePortForwardTransitions_Object = MibTableColumn
xstInstancePortForwardTransitions = _XstInstancePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 11),
    _XstInstancePortForwardTransitions_Type()
)
xstInstancePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortForwardTransitions.setStatus("current")


class _XstInstancePortPortRole_Type(Integer32):
    """Custom type xstInstancePortPortRole based on Integer32"""
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
        *(("disabled", 1),
          ("root", 2),
          ("designated", 3),
          ("alternate", 4),
          ("backup", 5),
          ("master", 6))
    )


_XstInstancePortPortRole_Type.__name__ = "Integer32"
_XstInstancePortPortRole_Object = MibTableColumn
xstInstancePortPortRole = _XstInstancePortPortRole_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 5, 1, 12),
    _XstInstancePortPortRole_Type()
)
xstInstancePortPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortPortRole.setStatus("current")
_MstInstanceEditTable_Object = MibTable
mstInstanceEditTable = _MstInstanceEditTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    mstInstanceEditTable.setStatus("current")
_MstInstanceEditEntry_Object = MibTableRow
mstInstanceEditEntry = _MstInstanceEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 6, 1)
)
mstInstanceEditEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "mstInstanceEditIndex"),
)
if mibBuilder.loadTexts:
    mstInstanceEditEntry.setStatus("current")


class _MstInstanceEditIndex_Type(Integer32):
    """Custom type mstInstanceEditIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MstInstanceEditIndex_Type.__name__ = "Integer32"
_MstInstanceEditIndex_Object = MibTableColumn
mstInstanceEditIndex = _MstInstanceEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 6, 1, 1),
    _MstInstanceEditIndex_Type()
)
mstInstanceEditIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstInstanceEditIndex.setStatus("current")


class _MstInstanceEditVlansMap_Type(OctetString):
    """Custom type mstInstanceEditVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap_Object = MibTableColumn
mstInstanceEditVlansMap = _MstInstanceEditVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 6, 1, 2),
    _MstInstanceEditVlansMap_Type()
)
mstInstanceEditVlansMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap.setStatus("current")


class _MstInstanceEditVlansMap2k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap2k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap2k_Object = MibTableColumn
mstInstanceEditVlansMap2k = _MstInstanceEditVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 6, 1, 3),
    _MstInstanceEditVlansMap2k_Type()
)
mstInstanceEditVlansMap2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap2k.setStatus("current")


class _MstInstanceEditVlansMap3k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap3k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap3k_Object = MibTableColumn
mstInstanceEditVlansMap3k = _MstInstanceEditVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 6, 1, 4),
    _MstInstanceEditVlansMap3k_Type()
)
mstInstanceEditVlansMap3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap3k.setStatus("current")


class _MstInstanceEditVlansMap4k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap4k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap4k_Object = MibTableColumn
mstInstanceEditVlansMap4k = _MstInstanceEditVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 6, 1, 5),
    _MstInstanceEditVlansMap4k_Type()
)
mstInstanceEditVlansMap4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap4k.setStatus("current")
_MstInstanceEditRemainingHops_Type = Integer32
_MstInstanceEditRemainingHops_Object = MibTableColumn
mstInstanceEditRemainingHops = _MstInstanceEditRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 6, 1, 6),
    _MstInstanceEditRemainingHops_Type()
)
mstInstanceEditRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceEditRemainingHops.setStatus("current")
_MstInstanceOperTable_Object = MibTable
mstInstanceOperTable = _MstInstanceOperTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    mstInstanceOperTable.setStatus("current")
_MstInstanceOperEntry_Object = MibTableRow
mstInstanceOperEntry = _MstInstanceOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 7, 1)
)
mstInstanceOperEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "mstInstanceOperIndex"),
)
if mibBuilder.loadTexts:
    mstInstanceOperEntry.setStatus("current")


class _MstInstanceOperIndex_Type(Integer32):
    """Custom type mstInstanceOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MstInstanceOperIndex_Type.__name__ = "Integer32"
_MstInstanceOperIndex_Object = MibTableColumn
mstInstanceOperIndex = _MstInstanceOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 7, 1, 1),
    _MstInstanceOperIndex_Type()
)
mstInstanceOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstInstanceOperIndex.setStatus("current")


class _MstInstanceOperVlansMap_Type(OctetString):
    """Custom type mstInstanceOperVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap_Object = MibTableColumn
mstInstanceOperVlansMap = _MstInstanceOperVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 7, 1, 2),
    _MstInstanceOperVlansMap_Type()
)
mstInstanceOperVlansMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap.setStatus("current")


class _MstInstanceOperVlansMap2k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap2k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap2k_Object = MibTableColumn
mstInstanceOperVlansMap2k = _MstInstanceOperVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 7, 1, 3),
    _MstInstanceOperVlansMap2k_Type()
)
mstInstanceOperVlansMap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap2k.setStatus("current")


class _MstInstanceOperVlansMap3k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap3k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap3k_Object = MibTableColumn
mstInstanceOperVlansMap3k = _MstInstanceOperVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 7, 1, 4),
    _MstInstanceOperVlansMap3k_Type()
)
mstInstanceOperVlansMap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap3k.setStatus("current")


class _MstInstanceOperVlansMap4k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap4k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap4k_Object = MibTableColumn
mstInstanceOperVlansMap4k = _MstInstanceOperVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 5, 6, 7, 1, 5),
    _MstInstanceOperVlansMap4k_Type()
)
mstInstanceOperVlansMap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap4k.setStatus("current")
_TftpMgt_ObjectIdentity = ObjectIdentity
tftpMgt = _TftpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 6)
)


class _TftpFileType_Type(Integer32):
    """Custom type tftpFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opcode", 1),
          ("config", 2))
    )


_TftpFileType_Type.__name__ = "Integer32"
_TftpFileType_Object = MibScalar
tftpFileType = _TftpFileType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 6, 1),
    _TftpFileType_Type()
)
tftpFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileType.setStatus("current")


class _TftpSrcFile_Type(DisplayString):
    """Custom type tftpSrcFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TftpSrcFile_Type.__name__ = "DisplayString"
_TftpSrcFile_Object = MibScalar
tftpSrcFile = _TftpSrcFile_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 6, 2),
    _TftpSrcFile_Type()
)
tftpSrcFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSrcFile.setStatus("current")


class _TftpDestFile_Type(DisplayString):
    """Custom type tftpDestFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TftpDestFile_Type.__name__ = "DisplayString"
_TftpDestFile_Object = MibScalar
tftpDestFile = _TftpDestFile_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 6, 3),
    _TftpDestFile_Type()
)
tftpDestFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDestFile.setStatus("current")
_TftpServer_Type = IpAddress
_TftpServer_Object = MibScalar
tftpServer = _TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 6, 4),
    _TftpServer_Type()
)
tftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServer.setStatus("current")


class _TftpAction_Type(Integer32):
    """Custom type tftpAction based on Integer32"""
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
        *(("notDownloading", 1),
          ("downloadToPROM", 2),
          ("downloadToRAM", 3),
          ("upload", 4))
    )


_TftpAction_Type.__name__ = "Integer32"
_TftpAction_Object = MibScalar
tftpAction = _TftpAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 6, 5),
    _TftpAction_Type()
)
tftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpAction.setStatus("current")


class _TftpStatus_Type(Integer32):
    """Custom type tftpStatus based on Integer32"""
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
        *(("tftpSuccess", 1),
          ("tftpStatusUnknown", 2),
          ("tftpGeneralError", 3),
          ("tftpNoResponseFromServer", 4),
          ("tftpDownloadChecksumError", 5),
          ("tftpDownloadIncompatibleImage", 6),
          ("tftpTftpFileNotFound", 7),
          ("tftpTftpAccessViolation", 8))
    )


_TftpStatus_Type.__name__ = "Integer32"
_TftpStatus_Object = MibScalar
tftpStatus = _TftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 6, 6),
    _TftpStatus_Type()
)
tftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpStatus.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 7)
)


class _RestartControl_Type(Integer32):
    """Custom type restartControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("warmBoot", 2),
          ("coldBoot", 3))
    )


_RestartControl_Type.__name__ = "Integer32"
_RestartControl_Object = MibScalar
restartControl = _RestartControl_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 7, 3),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIndex_Type = Unsigned32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12, 1, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("current")


class _VlanAddressMethod_Type(Integer32):
    """Custom type vlanAddressMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("user", 1),
          ("dhcp", 2))
    )


_VlanAddressMethod_Type.__name__ = "Integer32"
_VlanAddressMethod_Object = MibTableColumn
vlanAddressMethod = _VlanAddressMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12, 1, 1, 2),
    _VlanAddressMethod_Type()
)
vlanAddressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAddressMethod.setStatus("current")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12, 2)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12, 2, 1)
)
vlanPortEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "vlanPortIndex"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("current")


class _VlanPortIndex_Type(Integer32):
    """Custom type vlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 44),
    )


_VlanPortIndex_Type.__name__ = "Integer32"
_VlanPortIndex_Object = MibTableColumn
vlanPortIndex = _VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12, 2, 1, 1),
    _VlanPortIndex_Type()
)
vlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPortIndex.setStatus("current")


class _VlanPortMode_Type(Integer32):
    """Custom type vlanPortMode based on Integer32"""
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
        *(("hybrid", 1),
          ("dot1qTrunk", 2),
          ("access", 3),
          ("vlanUnaware", 4))
    )


_VlanPortMode_Type.__name__ = "Integer32"
_VlanPortMode_Object = MibTableColumn
vlanPortMode = _VlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12, 2, 1, 2),
    _VlanPortMode_Type()
)
vlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMode.setStatus("current")


class _VlanPortPrivateVlanType_Type(Integer32):
    """Custom type vlanPortPrivateVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-isolated", 1),
          ("isolated", 2))
    )


_VlanPortPrivateVlanType_Type.__name__ = "Integer32"
_VlanPortPrivateVlanType_Object = MibTableColumn
vlanPortPrivateVlanType = _VlanPortPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 12, 2, 1, 3),
    _VlanPortPrivateVlanType_Type()
)
vlanPortPrivateVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortPrivateVlanType.setStatus("current")
_SysTimeMgt_ObjectIdentity = ObjectIdentity
sysTimeMgt = _SysTimeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23)
)
_SntpMgt_ObjectIdentity = ObjectIdentity
sntpMgt = _SntpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 1)
)
_SntpStatus_Type = EnabledStatus
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 1, 1),
    _SntpStatus_Type()
)
sntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpStatus.setStatus("current")


class _SntpServiceMode_Type(Integer32):
    """Custom type sntpServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_SntpServiceMode_Type.__name__ = "Integer32"
_SntpServiceMode_Object = MibScalar
sntpServiceMode = _SntpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 1, 2),
    _SntpServiceMode_Type()
)
sntpServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServiceMode.setStatus("current")


class _SntpPollInterval_Type(Integer32):
    """Custom type sntpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16384),
    )


_SntpPollInterval_Type.__name__ = "Integer32"
_SntpPollInterval_Object = MibScalar
sntpPollInterval = _SntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 1, 3),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 1, 4)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 1, 4, 1)
)
sntpServerEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "sntpServerIndex"),
)
if mibBuilder.loadTexts:
    sntpServerEntry.setStatus("current")


class _SntpServerIndex_Type(Integer32):
    """Custom type sntpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SntpServerIndex_Type.__name__ = "Integer32"
_SntpServerIndex_Object = MibTableColumn
sntpServerIndex = _SntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 1, 4, 1, 1),
    _SntpServerIndex_Type()
)
sntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sntpServerIndex.setStatus("current")
_SntpServerIpAddress_Type = IpAddress
_SntpServerIpAddress_Object = MibTableColumn
sntpServerIpAddress = _SntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 1, 4, 1, 2),
    _SntpServerIpAddress_Type()
)
sntpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerIpAddress.setStatus("current")


class _SysCurrentTime_Type(DisplayString):
    """Custom type sysCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysCurrentTime_Type.__name__ = "DisplayString"
_SysCurrentTime_Object = MibScalar
sysCurrentTime = _SysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 2),
    _SysCurrentTime_Type()
)
sysCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCurrentTime.setStatus("current")


class _SysTimeZone_Type(DisplayString):
    """Custom type sysTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SysTimeZone_Type.__name__ = "DisplayString"
_SysTimeZone_Object = MibScalar
sysTimeZone = _SysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 3),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("current")
_NtpMgt_ObjectIdentity = ObjectIdentity
ntpMgt = _NtpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5)
)
_NtpStatus_Type = EnabledStatus
_NtpStatus_Object = MibScalar
ntpStatus = _NtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 1),
    _NtpStatus_Type()
)
ntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpStatus.setStatus("current")


class _NtpServiceMode_Type(Integer32):
    """Custom type ntpServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_NtpServiceMode_Type.__name__ = "Integer32"
_NtpServiceMode_Object = MibScalar
ntpServiceMode = _NtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 2),
    _NtpServiceMode_Type()
)
ntpServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServiceMode.setStatus("current")


class _NtpPollInterval_Type(Integer32):
    """Custom type ntpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16384),
    )


_NtpPollInterval_Type.__name__ = "Integer32"
_NtpPollInterval_Object = MibScalar
ntpPollInterval = _NtpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 3),
    _NtpPollInterval_Type()
)
ntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPollInterval.setStatus("current")
_NtpAuthenticateStatus_Type = EnabledStatus
_NtpAuthenticateStatus_Object = MibScalar
ntpAuthenticateStatus = _NtpAuthenticateStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 4),
    _NtpAuthenticateStatus_Type()
)
ntpAuthenticateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticateStatus.setStatus("current")
_NtpServerTable_Object = MibTable
ntpServerTable = _NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 5)
)
if mibBuilder.loadTexts:
    ntpServerTable.setStatus("current")
_NtpServerEntry_Object = MibTableRow
ntpServerEntry = _NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 5, 1)
)
ntpServerEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "ntpServerIpAddress"),
)
if mibBuilder.loadTexts:
    ntpServerEntry.setStatus("current")
_NtpServerIpAddress_Type = IpAddress
_NtpServerIpAddress_Object = MibTableColumn
ntpServerIpAddress = _NtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 5, 1, 1),
    _NtpServerIpAddress_Type()
)
ntpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpServerIpAddress.setStatus("current")


class _NtpServerVersion_Type(Integer32):
    """Custom type ntpServerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NtpServerVersion_Type.__name__ = "Integer32"
_NtpServerVersion_Object = MibTableColumn
ntpServerVersion = _NtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 5, 1, 2),
    _NtpServerVersion_Type()
)
ntpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpServerVersion.setStatus("current")


class _NtpServerKeyId_Type(Integer32):
    """Custom type ntpServerKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtpServerKeyId_Type.__name__ = "Integer32"
_NtpServerKeyId_Object = MibTableColumn
ntpServerKeyId = _NtpServerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 5, 1, 3),
    _NtpServerKeyId_Type()
)
ntpServerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerKeyId.setStatus("current")


class _NtpServerStatus_Type(Integer32):
    """Custom type ntpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("active", 2),
          ("destroy", 3))
    )


_NtpServerStatus_Type.__name__ = "Integer32"
_NtpServerStatus_Object = MibTableColumn
ntpServerStatus = _NtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 5, 1, 4),
    _NtpServerStatus_Type()
)
ntpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpServerStatus.setStatus("current")
_NtpAuthKeyTable_Object = MibTable
ntpAuthKeyTable = _NtpAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 6)
)
if mibBuilder.loadTexts:
    ntpAuthKeyTable.setStatus("current")
_NtpAuthKeyEntry_Object = MibTableRow
ntpAuthKeyEntry = _NtpAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 6, 1)
)
ntpAuthKeyEntry.setIndexNames(
    (0, "ECS4810-28TS-MIB", "ntpAuthKeyId"),
)
if mibBuilder.loadTexts:
    ntpAuthKeyEntry.setStatus("current")


class _NtpAuthKeyId_Type(Integer32):
    """Custom type ntpAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_NtpAuthKeyId_Type.__name__ = "Integer32"
_NtpAuthKeyId_Object = MibTableColumn
ntpAuthKeyId = _NtpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 6, 1, 1),
    _NtpAuthKeyId_Type()
)
ntpAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpAuthKeyId.setStatus("current")


class _NtpAuthKeyWord_Type(OctetString):
    """Custom type ntpAuthKeyWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAuthKeyWord_Type.__name__ = "OctetString"
_NtpAuthKeyWord_Object = MibTableColumn
ntpAuthKeyWord = _NtpAuthKeyWord_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 6, 1, 2),
    _NtpAuthKeyWord_Type()
)
ntpAuthKeyWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthKeyWord.setStatus("current")


class _NtpAuthKeyStatus_Type(Integer32):
    """Custom type ntpAuthKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("active", 2),
          ("destroy", 3))
    )


_NtpAuthKeyStatus_Type.__name__ = "Integer32"
_NtpAuthKeyStatus_Object = MibTableColumn
ntpAuthKeyStatus = _NtpAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 23, 5, 6, 1, 3),
    _NtpAuthKeyStatus_Type()
)
ntpAuthKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthKeyStatus.setStatus("current")
_FileMgt_ObjectIdentity = ObjectIdentity
fileMgt = _FileMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24)
)
_FileCopyMgt_ObjectIdentity = ObjectIdentity
fileCopyMgt = _FileCopyMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24, 1)
)


class _FileCopySrcOperType_Type(Integer32):
    """Custom type fileCopySrcOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchDevice", 1),
          ("tftp", 2))
    )


_FileCopySrcOperType_Type.__name__ = "Integer32"
_FileCopySrcOperType_Object = MibScalar
fileCopySrcOperType = _FileCopySrcOperType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24, 1, 1),
    _FileCopySrcOperType_Type()
)
fileCopySrcOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopySrcOperType.setStatus("current")


class _FileCopySrcFileName_Type(DisplayString):
    """Custom type fileCopySrcFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FileCopySrcFileName_Type.__name__ = "DisplayString"
_FileCopySrcFileName_Object = MibScalar
fileCopySrcFileName = _FileCopySrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24, 1, 2),
    _FileCopySrcFileName_Type()
)
fileCopySrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopySrcFileName.setStatus("current")


class _FileCopyDestOperType_Type(Integer32):
    """Custom type fileCopyDestOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchDevice", 1),
          ("tftp", 2))
    )


_FileCopyDestOperType_Type.__name__ = "Integer32"
_FileCopyDestOperType_Object = MibScalar
fileCopyDestOperType = _FileCopyDestOperType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24, 1, 3),
    _FileCopyDestOperType_Type()
)
fileCopyDestOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyDestOperType.setStatus("current")


class _FileCopyDestFileName_Type(DisplayString):
    """Custom type fileCopyDestFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FileCopyDestFileName_Type.__name__ = "DisplayString"
_FileCopyDestFileName_Object = MibScalar
fileCopyDestFileName = _FileCopyDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24, 1, 4),
    _FileCopyDestFileName_Type()
)
fileCopyDestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyDestFileName.setStatus("current")


class _FileCopyFileType_Type(Integer32):
    """Custom type fileCopyFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opcode", 1),
          ("config", 2))
    )


_FileCopyFileType_Type.__name__ = "Integer32"
_FileCopyFileType_Object = MibScalar
fileCopyFileType = _FileCopyFileType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24, 1, 5),
    _FileCopyFileType_Type()
)
fileCopyFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyFileType.setStatus("current")
_FileCopyTftpServer_Type = IpAddress
_FileCopyTftpServer_Object = MibScalar
fileCopyTftpServer = _FileCopyTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24, 1, 6),
    _FileCopyTftpServer_Type()
)
fileCopyTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyTftpServer.setStatus("current")


class _FileCopyAction_Type(Integer32):
    """Custom type fileCopyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notCopying", 1),
          ("copy", 2))
    )


_FileCopyAction_Type.__name__ = "Integer32"
_FileCopyAction_Object = MibScalar
fileCopyAction = _FileCopyAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24, 1, 8),
    _FileCopyAction_Type()
)
fileCopyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyAction.setStatus("current")


class _FileCopyTftpErrMsg_Type(DisplayString):
    """Custom type fileCopyTftpErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FileCopyTftpErrMsg_Type.__name__ = "DisplayString"
_FileCopyTftpErrMsg_Object = MibScalar
fileCopyTftpErrMsg = _FileCopyTftpErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 1, 24, 1, 10),
    _FileCopyTftpErrMsg_Type()
)
fileCopyTftpErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyTftpErrMsg.setStatus("current")
_Ecs4810_28tsNotifications_ObjectIdentity = ObjectIdentity
ecs4810_28tsNotifications = _Ecs4810_28tsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 2)
)
_Ecs4810_28tsTraps_ObjectIdentity = ObjectIdentity
ecs4810_28tsTraps = _Ecs4810_28tsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 2, 1)
)
_Ecs4810_28tsTrapsPrefix_ObjectIdentity = ObjectIdentity
ecs4810_28tsTrapsPrefix = _Ecs4810_28tsTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 2, 1, 0)
)
_Ecs4810_28tsConformance_ObjectIdentity = ObjectIdentity
ecs4810_28tsConformance = _Ecs4810_28tsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 3)
)

# Managed Objects groups


# Notification objects

swPortSecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 18, 2, 1, 0, 36)
)
swPortSecurityTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    swPortSecurityTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ECS4810-28TS-MIB",
    **{"KeySegment": KeySegment,
       "ValidStatus": ValidStatus,
       "StaPathCostMode": StaPathCostMode,
       "accton": accton,
       "edgecorenetworks": edgecorenetworks,
       "edgeCoreNetworksMgt": edgeCoreNetworksMgt,
       "ecs4810-28tsMIB": ecs4810_28tsMIB,
       "ecs4810-28tsMIBObjects": ecs4810_28tsMIBObjects,
       "switchMgt": switchMgt,
       "switchManagementVlan": switchManagementVlan,
       "switchNumber": switchNumber,
       "switchInfoTable": switchInfoTable,
       "switchInfoEntry": switchInfoEntry,
       "swUnitIndex": swUnitIndex,
       "swHardwareVer": swHardwareVer,
       "swMicrocodeVer": swMicrocodeVer,
       "swLoaderVer": swLoaderVer,
       "swBootRomVer": swBootRomVer,
       "swOpCodeVer": swOpCodeVer,
       "swPortNumber": swPortNumber,
       "swPowerStatus": swPowerStatus,
       "swRoleInSystem": swRoleInSystem,
       "swSerialNumber": swSerialNumber,
       "swServiceTag": swServiceTag,
       "switchOperState": switchOperState,
       "switchProductId": switchProductId,
       "swProdName": swProdName,
       "swProdManufacturer": swProdManufacturer,
       "swProdDescription": swProdDescription,
       "swProdVersion": swProdVersion,
       "swProdUrl": swProdUrl,
       "swIdentifier": swIdentifier,
       "swChassisServiceTag": swChassisServiceTag,
       "amtrMgt": amtrMgt,
       "amtrMacAddrAgingStatus": amtrMacAddrAgingStatus,
       "portMgt": portMgt,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portName": portName,
       "portType": portType,
       "portSpeedDpxCfg": portSpeedDpxCfg,
       "portFlowCtrlCfg": portFlowCtrlCfg,
       "portCapabilities": portCapabilities,
       "portAutonegotiation": portAutonegotiation,
       "portSpeedDpxStatus": portSpeedDpxStatus,
       "portFlowCtrlStatus": portFlowCtrlStatus,
       "portTrunkIndex": portTrunkIndex,
       "trunkMgt": trunkMgt,
       "trunkMaxId": trunkMaxId,
       "trunkValidNumber": trunkValidNumber,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkIndex": trunkIndex,
       "trunkPorts": trunkPorts,
       "trunkCreation": trunkCreation,
       "trunkStatus": trunkStatus,
       "lacpMgt": lacpMgt,
       "lacpPortTable": lacpPortTable,
       "lacpPortEntry": lacpPortEntry,
       "lacpPortIndex": lacpPortIndex,
       "lacpPortStatus": lacpPortStatus,
       "staMgt": staMgt,
       "staSystemStatus": staSystemStatus,
       "staPortTable": staPortTable,
       "staPortEntry": staPortEntry,
       "staPortIndex": staPortIndex,
       "staPortFastForward": staPortFastForward,
       "staPortProtocolMigration": staPortProtocolMigration,
       "staPortAdminEdgePort": staPortAdminEdgePort,
       "staPortOperEdgePort": staPortOperEdgePort,
       "staPortAdminPointToPoint": staPortAdminPointToPoint,
       "staPortOperPointToPoint": staPortOperPointToPoint,
       "staPortLongPathCost": staPortLongPathCost,
       "staPortSystemStatus": staPortSystemStatus,
       "staProtocolType": staProtocolType,
       "staTxHoldCount": staTxHoldCount,
       "staPathCostMethod": staPathCostMethod,
       "xstMgt": xstMgt,
       "mstName": mstName,
       "mstRevision": mstRevision,
       "mstMaxHops": mstMaxHops,
       "xstInstanceCfgTable": xstInstanceCfgTable,
       "xstInstanceCfgEntry": xstInstanceCfgEntry,
       "xstInstanceCfgIndex": xstInstanceCfgIndex,
       "xstInstanceCfgPriority": xstInstanceCfgPriority,
       "xstInstanceCfgTimeSinceTopologyChange": xstInstanceCfgTimeSinceTopologyChange,
       "xstInstanceCfgTopChanges": xstInstanceCfgTopChanges,
       "xstInstanceCfgDesignatedRoot": xstInstanceCfgDesignatedRoot,
       "xstInstanceCfgRootCost": xstInstanceCfgRootCost,
       "xstInstanceCfgRootPort": xstInstanceCfgRootPort,
       "xstInstanceCfgMaxAge": xstInstanceCfgMaxAge,
       "xstInstanceCfgHelloTime": xstInstanceCfgHelloTime,
       "xstInstanceCfgHoldTime": xstInstanceCfgHoldTime,
       "xstInstanceCfgForwardDelay": xstInstanceCfgForwardDelay,
       "xstInstanceCfgBridgeMaxAge": xstInstanceCfgBridgeMaxAge,
       "xstInstanceCfgBridgeHelloTime": xstInstanceCfgBridgeHelloTime,
       "xstInstanceCfgBridgeForwardDelay": xstInstanceCfgBridgeForwardDelay,
       "xstInstanceCfgTxHoldCount": xstInstanceCfgTxHoldCount,
       "xstInstanceCfgPathCostMethod": xstInstanceCfgPathCostMethod,
       "xstInstancePortTable": xstInstancePortTable,
       "xstInstancePortEntry": xstInstancePortEntry,
       "xstInstancePortInstance": xstInstancePortInstance,
       "xstInstancePortPort": xstInstancePortPort,
       "xstInstancePortPriority": xstInstancePortPriority,
       "xstInstancePortState": xstInstancePortState,
       "xstInstancePortEnable": xstInstancePortEnable,
       "xstInstancePortPathCost": xstInstancePortPathCost,
       "xstInstancePortDesignatedRoot": xstInstancePortDesignatedRoot,
       "xstInstancePortDesignatedCost": xstInstancePortDesignatedCost,
       "xstInstancePortDesignatedBridge": xstInstancePortDesignatedBridge,
       "xstInstancePortDesignatedPort": xstInstancePortDesignatedPort,
       "xstInstancePortForwardTransitions": xstInstancePortForwardTransitions,
       "xstInstancePortPortRole": xstInstancePortPortRole,
       "mstInstanceEditTable": mstInstanceEditTable,
       "mstInstanceEditEntry": mstInstanceEditEntry,
       "mstInstanceEditIndex": mstInstanceEditIndex,
       "mstInstanceEditVlansMap": mstInstanceEditVlansMap,
       "mstInstanceEditVlansMap2k": mstInstanceEditVlansMap2k,
       "mstInstanceEditVlansMap3k": mstInstanceEditVlansMap3k,
       "mstInstanceEditVlansMap4k": mstInstanceEditVlansMap4k,
       "mstInstanceEditRemainingHops": mstInstanceEditRemainingHops,
       "mstInstanceOperTable": mstInstanceOperTable,
       "mstInstanceOperEntry": mstInstanceOperEntry,
       "mstInstanceOperIndex": mstInstanceOperIndex,
       "mstInstanceOperVlansMap": mstInstanceOperVlansMap,
       "mstInstanceOperVlansMap2k": mstInstanceOperVlansMap2k,
       "mstInstanceOperVlansMap3k": mstInstanceOperVlansMap3k,
       "mstInstanceOperVlansMap4k": mstInstanceOperVlansMap4k,
       "tftpMgt": tftpMgt,
       "tftpFileType": tftpFileType,
       "tftpSrcFile": tftpSrcFile,
       "tftpDestFile": tftpDestFile,
       "tftpServer": tftpServer,
       "tftpAction": tftpAction,
       "tftpStatus": tftpStatus,
       "restartMgt": restartMgt,
       "restartControl": restartControl,
       "vlanMgt": vlanMgt,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanAddressMethod": vlanAddressMethod,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortIndex": vlanPortIndex,
       "vlanPortMode": vlanPortMode,
       "vlanPortPrivateVlanType": vlanPortPrivateVlanType,
       "sysTimeMgt": sysTimeMgt,
       "sntpMgt": sntpMgt,
       "sntpStatus": sntpStatus,
       "sntpServiceMode": sntpServiceMode,
       "sntpPollInterval": sntpPollInterval,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerIndex": sntpServerIndex,
       "sntpServerIpAddress": sntpServerIpAddress,
       "sysCurrentTime": sysCurrentTime,
       "sysTimeZone": sysTimeZone,
       "ntpMgt": ntpMgt,
       "ntpStatus": ntpStatus,
       "ntpServiceMode": ntpServiceMode,
       "ntpPollInterval": ntpPollInterval,
       "ntpAuthenticateStatus": ntpAuthenticateStatus,
       "ntpServerTable": ntpServerTable,
       "ntpServerEntry": ntpServerEntry,
       "ntpServerIpAddress": ntpServerIpAddress,
       "ntpServerVersion": ntpServerVersion,
       "ntpServerKeyId": ntpServerKeyId,
       "ntpServerStatus": ntpServerStatus,
       "ntpAuthKeyTable": ntpAuthKeyTable,
       "ntpAuthKeyEntry": ntpAuthKeyEntry,
       "ntpAuthKeyId": ntpAuthKeyId,
       "ntpAuthKeyWord": ntpAuthKeyWord,
       "ntpAuthKeyStatus": ntpAuthKeyStatus,
       "fileMgt": fileMgt,
       "fileCopyMgt": fileCopyMgt,
       "fileCopySrcOperType": fileCopySrcOperType,
       "fileCopySrcFileName": fileCopySrcFileName,
       "fileCopyDestOperType": fileCopyDestOperType,
       "fileCopyDestFileName": fileCopyDestFileName,
       "fileCopyFileType": fileCopyFileType,
       "fileCopyTftpServer": fileCopyTftpServer,
       "fileCopyAction": fileCopyAction,
       "fileCopyTftpErrMsg": fileCopyTftpErrMsg,
       "ecs4810-28tsNotifications": ecs4810_28tsNotifications,
       "ecs4810-28tsTraps": ecs4810_28tsTraps,
       "ecs4810-28tsTrapsPrefix": ecs4810_28tsTrapsPrefix,
       "swPortSecurityTrap": swPortSecurityTrap,
       "ecs4810-28tsConformance": ecs4810_28tsConformance}
)
