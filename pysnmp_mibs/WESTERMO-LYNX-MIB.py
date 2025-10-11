# SNMP MIB module (WESTERMO-LYNX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-LYNX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:25 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(products,) = mibBuilder.importSymbols(
    "WESTERMO-OID-MIB",
    "products")


# MODULE-IDENTITY

lynx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2)
)
if mibBuilder.loadTexts:
    lynx.setRevisions(
        ("2009-05-28 00:00",
         "2006-06-29 23:59",
         "2006-04-12 08:19",
         "2006-04-12 06:19")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1)
)


class _Temperature_Type(Integer32):
    """Custom type temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Temperature_Type.__name__ = "Integer32"
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 1),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
_SwVersion_Type = DisplayString
_SwVersion_Object = MibScalar
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 2),
    _SwVersion_Type()
)
swVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersion.setStatus("current")
_SwVersionBootLoader_Type = DisplayString
_SwVersionBootLoader_Object = MibScalar
swVersionBootLoader = _SwVersionBootLoader_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 3),
    _SwVersionBootLoader_Type()
)
swVersionBootLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersionBootLoader.setStatus("current")
_HwVersionBoard_Type = DisplayString
_HwVersionBoard_Object = MibScalar
hwVersionBoard = _HwVersionBoard_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 4),
    _HwVersionBoard_Type()
)
hwVersionBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVersionBoard.setStatus("current")
_HwVersionPld_Type = DisplayString
_HwVersionPld_Object = MibScalar
hwVersionPld = _HwVersionPld_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 5),
    _HwVersionPld_Type()
)
hwVersionPld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVersionPld.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 6),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_BatchID_Type = DisplayString
_BatchID_Object = MibScalar
batchID = _BatchID_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 7),
    _BatchID_Type()
)
batchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batchID.setStatus("current")


class _HwConfig_Type(Integer32):
    """Custom type hwConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("amd", 22),
          ("intel", 23))
    )


_HwConfig_Type.__name__ = "Integer32"
_HwConfig_Object = MibScalar
hwConfig = _HwConfig_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 8),
    _HwConfig_Type()
)
hwConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConfig.setStatus("current")


class _Reset_Type(Integer32):
    """Custom type reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("factoryDefault", 2))
    )


_Reset_Type.__name__ = "Integer32"
_Reset_Object = MibScalar
reset = _Reset_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 9),
    _Reset_Type()
)
reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reset.setStatus("current")


class _PowerSupply_Type(Integer32):
    """Custom type powerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("okpowerAB", 1),
          ("okpowerA", 2),
          ("okpowerB", 3))
    )


_PowerSupply_Type.__name__ = "Integer32"
_PowerSupply_Object = MibScalar
powerSupply = _PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 10),
    _PowerSupply_Type()
)
powerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupply.setStatus("current")
_TrapHostAddr1_Type = DisplayString
_TrapHostAddr1_Object = MibScalar
trapHostAddr1 = _TrapHostAddr1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 11),
    _TrapHostAddr1_Type()
)
trapHostAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHostAddr1.setStatus("current")
_TrapHostAddr2_Type = DisplayString
_TrapHostAddr2_Object = MibScalar
trapHostAddr2 = _TrapHostAddr2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 12),
    _TrapHostAddr2_Type()
)
trapHostAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapHostAddr2.setStatus("current")
_ReadPassword_Type = DisplayString
_ReadPassword_Object = MibScalar
readPassword = _ReadPassword_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 13),
    _ReadPassword_Type()
)
readPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readPassword.setStatus("current")
_WritePassword_Type = DisplayString
_WritePassword_Object = MibScalar
writePassword = _WritePassword_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 14),
    _WritePassword_Type()
)
writePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    writePassword.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2)
)


class _OntPortNumber_Type(Integer32):
    """Custom type ontPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_OntPortNumber_Type.__name__ = "Integer32"
_OntPortNumber_Object = MibScalar
ontPortNumber = _OntPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 1),
    _OntPortNumber_Type()
)
ontPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ontPortNumber.setStatus("current")
_OntTable_Object = MibTable
ontTable = _OntTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ontTable.setStatus("current")
_OntEntry_Object = MibTableRow
ontEntry = _OntEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1)
)
ontEntry.setIndexNames(
    (0, "WESTERMO-LYNX-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    ontEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortEnable_Type(Integer32):
    """Custom type portEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("disable", 3))
    )


_PortEnable_Type.__name__ = "Integer32"
_PortEnable_Object = MibTableColumn
portEnable = _PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 2),
    _PortEnable_Type()
)
portEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnable.setStatus("current")


class _PortDuplexMode_Type(Integer32):
    """Custom type portDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("half", 2),
          ("full", 3))
    )


_PortDuplexMode_Type.__name__ = "Integer32"
_PortDuplexMode_Object = MibTableColumn
portDuplexMode = _PortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 3),
    _PortDuplexMode_Type()
)
portDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDuplexMode.setStatus("current")


class _PortAutoNegotiate_Type(Integer32):
    """Custom type portAutoNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("disable", 3))
    )


_PortAutoNegotiate_Type.__name__ = "Integer32"
_PortAutoNegotiate_Object = MibTableColumn
portAutoNegotiate = _PortAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 4),
    _PortAutoNegotiate_Type()
)
portAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutoNegotiate.setStatus("current")


class _PortSpeed_Type(Integer32):
    """Custom type portSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("s10M", 10),
          ("s100M", 100),
          ("s1000M", 1000))
    )


_PortSpeed_Type.__name__ = "Integer32"
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 5),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeed.setStatus("current")


class _PortAlarm_Type(Integer32):
    """Custom type portAlarm based on Integer32"""
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


_PortAlarm_Type.__name__ = "Integer32"
_PortAlarm_Object = MibTableColumn
portAlarm = _PortAlarm_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 6),
    _PortAlarm_Type()
)
portAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAlarm.setStatus("current")
_PortType_Type = DisplayString
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 7),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _TimeSyncFilters_Type(Integer32):
    """Custom type timeSyncFilters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonTiming", 1),
          ("timing", 2),
          ("unfiltered", 3))
    )


_TimeSyncFilters_Type.__name__ = "Integer32"
_TimeSyncFilters_Object = MibTableColumn
timeSyncFilters = _TimeSyncFilters_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 8),
    _TimeSyncFilters_Type()
)
timeSyncFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeSyncFilters.setStatus("current")


class _RstpPortTrunk_Type(Integer32):
    """Custom type rstpPortTrunk based on Integer32"""
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


_RstpPortTrunk_Type.__name__ = "Integer32"
_RstpPortTrunk_Object = MibTableColumn
rstpPortTrunk = _RstpPortTrunk_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 9),
    _RstpPortTrunk_Type()
)
rstpPortTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPortTrunk.setStatus("current")


class _IgmpPortTrunk_Type(Integer32):
    """Custom type igmpPortTrunk based on Integer32"""
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


_IgmpPortTrunk_Type.__name__ = "Integer32"
_IgmpPortTrunk_Object = MibTableColumn
igmpPortTrunk = _IgmpPortTrunk_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 10),
    _IgmpPortTrunk_Type()
)
igmpPortTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpPortTrunk.setStatus("current")


class _RemovePortTag_Type(Integer32):
    """Custom type removePortTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keepTag", 1),
          ("removeTag", 2))
    )


_RemovePortTag_Type.__name__ = "Integer32"
_RemovePortTag_Object = MibTableColumn
removePortTag = _RemovePortTag_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 12),
    _RemovePortTag_Type()
)
removePortTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    removePortTag.setStatus("current")


class _VlanId_Type(Integer32):
    """Custom type vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanId_Type.__name__ = "Integer32"
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 13),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")


class _VlanPrio_Type(Integer32):
    """Custom type vlanPrio based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("prio0", 0),
          ("prio1", 1),
          ("prio2", 2),
          ("prio3", 3),
          ("prio4", 4),
          ("prio5", 5),
          ("prio6", 6),
          ("prio7", 7))
    )


_VlanPrio_Type.__name__ = "Integer32"
_VlanPrio_Object = MibTableColumn
vlanPrio = _VlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 14),
    _VlanPrio_Type()
)
vlanPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPrio.setStatus("current")
_PortVlanColors_Type = DisplayString
_PortVlanColors_Object = MibTableColumn
portVlanColors = _PortVlanColors_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 15),
    _PortVlanColors_Type()
)
portVlanColors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanColors.setStatus("current")


class _VlanDefaultColor_Type(Integer32):
    """Custom type vlanDefaultColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("white", 0),
          ("red", 1),
          ("blue", 2),
          ("green", 3),
          ("yellow", 4),
          ("brown", 5),
          ("pink", 6))
    )


_VlanDefaultColor_Type.__name__ = "Integer32"
_VlanDefaultColor_Object = MibTableColumn
vlanDefaultColor = _VlanDefaultColor_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 16),
    _VlanDefaultColor_Type()
)
vlanDefaultColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultColor.setStatus("current")


class _IgmpColor_Type(Integer32):
    """Custom type igmpColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("black", 1),
          ("red", 3))
    )


_IgmpColor_Type.__name__ = "Integer32"
_IgmpColor_Object = MibTableColumn
igmpColor = _IgmpColor_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 17),
    _IgmpColor_Type()
)
igmpColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpColor.setStatus("current")


class _RstpPortStatus_Type(Integer32):
    """Custom type rstpPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("forwarding", 2))
    )


_RstpPortStatus_Type.__name__ = "Integer32"
_RstpPortStatus_Object = MibTableColumn
rstpPortStatus = _RstpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 18),
    _RstpPortStatus_Type()
)
rstpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPortStatus.setStatus("current")


class _LinkStatus_Type(Integer32):
    """Custom type linkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_LinkStatus_Type.__name__ = "Integer32"
_LinkStatus_Object = MibTableColumn
linkStatus = _LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 2, 1, 19),
    _LinkStatus_Type()
)
linkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkStatus.setStatus("current")


class _Snmp_Type(Integer32):
    """Custom type snmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("off", 3))
    )


_Snmp_Type.__name__ = "Integer32"
_Snmp_Object = MibScalar
snmp = _Snmp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 3),
    _Snmp_Type()
)
snmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp.setStatus("current")


class _Frnt_Type(Integer32):
    """Custom type frnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("focalpoint", 3),
          ("member", 4))
    )


_Frnt_Type.__name__ = "Integer32"
_Frnt_Object = MibScalar
frnt = _Frnt_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 4),
    _Frnt_Type()
)
frnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frnt.setStatus("current")


class _FrntPorts_Type(Integer32):
    """Custom type frntPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FrntPorts_Type.__name__ = "Integer32"
_FrntPorts_Object = MibScalar
frntPorts = _FrntPorts_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 5),
    _FrntPorts_Type()
)
frntPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frntPorts.setStatus("current")


class _Dhcp_Type(Integer32):
    """Custom type dhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("off", 3))
    )


_Dhcp_Type.__name__ = "Integer32"
_Dhcp_Object = MibScalar
dhcp = _Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 6),
    _Dhcp_Type()
)
dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp.setStatus("current")


class _EnableVlan_Type(Integer32):
    """Custom type enableVlan based on Integer32"""
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


_EnableVlan_Type.__name__ = "Integer32"
_EnableVlan_Object = MibScalar
enableVlan = _EnableVlan_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 7),
    _EnableVlan_Type()
)
enableVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableVlan.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 8),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_IpNetMask_Type = IpAddress
_IpNetMask_Object = MibScalar
ipNetMask = _IpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 9),
    _IpNetMask_Type()
)
ipNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetMask.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 10),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")


class _DhcpRelayAgent_Type(Integer32):
    """Custom type dhcpRelayAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("off", 3))
    )


_DhcpRelayAgent_Type.__name__ = "Integer32"
_DhcpRelayAgent_Object = MibScalar
dhcpRelayAgent = _DhcpRelayAgent_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 11),
    _DhcpRelayAgent_Type()
)
dhcpRelayAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayAgent.setStatus("current")
_DhcpRelayAgentServer1_Type = IpAddress
_DhcpRelayAgentServer1_Object = MibScalar
dhcpRelayAgentServer1 = _DhcpRelayAgentServer1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 12),
    _DhcpRelayAgentServer1_Type()
)
dhcpRelayAgentServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayAgentServer1.setStatus("current")
_DhcpRelayAgentServer2_Type = IpAddress
_DhcpRelayAgentServer2_Object = MibScalar
dhcpRelayAgentServer2 = _DhcpRelayAgentServer2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 13),
    _DhcpRelayAgentServer2_Type()
)
dhcpRelayAgentServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayAgentServer2.setStatus("current")


class _Rstp_Type(Integer32):
    """Custom type rstp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("root", 1),
          ("on", 2),
          ("off", 3))
    )


_Rstp_Type.__name__ = "Integer32"
_Rstp_Object = MibScalar
rstp = _Rstp_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 2, 14),
    _Rstp_Type()
)
rstp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstp.setStatus("current")
_Igmp_ObjectIdentity = ObjectIdentity
igmp = _Igmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 5)
)


class _Snooping_Type(Integer32):
    """Custom type snooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("off", 3))
    )


_Snooping_Type.__name__ = "Integer32"
_Snooping_Object = MibScalar
snooping = _Snooping_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 5, 1),
    _Snooping_Type()
)
snooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snooping.setStatus("current")


class _Automode_Type(Integer32):
    """Custom type automode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("off", 3))
    )


_Automode_Type.__name__ = "Integer32"
_Automode_Object = MibScalar
automode = _Automode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 5, 2),
    _Automode_Type()
)
automode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automode.setStatus("current")


class _Querier_Type(Integer32):
    """Custom type querier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("off", 3))
    )


_Querier_Type.__name__ = "Integer32"
_Querier_Object = MibScalar
querier = _Querier_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 5, 3),
    _Querier_Type()
)
querier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    querier.setStatus("current")


class _Stopfilter_Type(Integer32):
    """Custom type stopfilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("off", 3))
    )


_Stopfilter_Type.__name__ = "Integer32"
_Stopfilter_Object = MibScalar
stopfilter = _Stopfilter_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 5, 4),
    _Stopfilter_Type()
)
stopfilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stopfilter.setStatus("current")


class _Querytimeout_Type(Integer32):
    """Custom type querytimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              30,
              70,
              150)
        )
    )
    namedValues = NamedValues(
        *(("t12s", 12),
          ("t30s", 30),
          ("t70s", 70),
          ("t150s", 150))
    )


_Querytimeout_Type.__name__ = "Integer32"
_Querytimeout_Object = MibScalar
querytimeout = _Querytimeout_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 5, 6),
    _Querytimeout_Type()
)
querytimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    querytimeout.setStatus("current")
_Stat_ObjectIdentity = ObjectIdentity
stat = _Stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 6)
)


class _StatusCode_Type(Integer32):
    """Custom type statusCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("error", 2))
    )


_StatusCode_Type.__name__ = "Integer32"
_StatusCode_Object = MibScalar
statusCode = _StatusCode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 6, 1),
    _StatusCode_Type()
)
statusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusCode.setStatus("current")


class _EnableStatusTrap_Type(Integer32):
    """Custom type enableStatusTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 2),
          ("off", 3))
    )


_EnableStatusTrap_Type.__name__ = "Integer32"
_EnableStatusTrap_Object = MibScalar
enableStatusTrap = _EnableStatusTrap_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 6, 2),
    _EnableStatusTrap_Type()
)
enableStatusTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableStatusTrap.setStatus("current")
_PrivTraps_ObjectIdentity = ObjectIdentity
privTraps = _PrivTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 7)
)

# Managed Objects groups

portGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 15)
)
portGroup.setObjects(
      *(("WESTERMO-LYNX-MIB", "portIndex"),
        ("WESTERMO-LYNX-MIB", "portEnable"),
        ("WESTERMO-LYNX-MIB", "portDuplexMode"),
        ("WESTERMO-LYNX-MIB", "portAutoNegotiate"),
        ("WESTERMO-LYNX-MIB", "portSpeed"),
        ("WESTERMO-LYNX-MIB", "portAlarm"),
        ("WESTERMO-LYNX-MIB", "portType"),
        ("WESTERMO-LYNX-MIB", "timeSyncFilters"),
        ("WESTERMO-LYNX-MIB", "rstpPortTrunk"),
        ("WESTERMO-LYNX-MIB", "igmpPortTrunk"),
        ("WESTERMO-LYNX-MIB", "portVlanColors"),
        ("WESTERMO-LYNX-MIB", "removePortTag"),
        ("WESTERMO-LYNX-MIB", "vlanId"),
        ("WESTERMO-LYNX-MIB", "vlanPrio"),
        ("WESTERMO-LYNX-MIB", "vlanDefaultColor"),
        ("WESTERMO-LYNX-MIB", "igmpColor"),
        ("WESTERMO-LYNX-MIB", "rstpPortStatus"),
        ("WESTERMO-LYNX-MIB", "linkStatus"))
)
if mibBuilder.loadTexts:
    portGroup.setStatus("current")

miscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 16)
)
miscGroup.setObjects(
      *(("WESTERMO-LYNX-MIB", "temperature"),
        ("WESTERMO-LYNX-MIB", "swVersion"),
        ("WESTERMO-LYNX-MIB", "swVersionBootLoader"),
        ("WESTERMO-LYNX-MIB", "hwVersionBoard"),
        ("WESTERMO-LYNX-MIB", "hwVersionPld"),
        ("WESTERMO-LYNX-MIB", "serialNumber"),
        ("WESTERMO-LYNX-MIB", "batchID"),
        ("WESTERMO-LYNX-MIB", "hwConfig"),
        ("WESTERMO-LYNX-MIB", "reset"),
        ("WESTERMO-LYNX-MIB", "powerSupply"),
        ("WESTERMO-LYNX-MIB", "trapHostAddr1"),
        ("WESTERMO-LYNX-MIB", "trapHostAddr2"),
        ("WESTERMO-LYNX-MIB", "readPassword"),
        ("WESTERMO-LYNX-MIB", "writePassword"),
        ("WESTERMO-LYNX-MIB", "ontPortNumber"),
        ("WESTERMO-LYNX-MIB", "snmp"),
        ("WESTERMO-LYNX-MIB", "frnt"),
        ("WESTERMO-LYNX-MIB", "frntPorts"),
        ("WESTERMO-LYNX-MIB", "dhcp"),
        ("WESTERMO-LYNX-MIB", "enableVlan"),
        ("WESTERMO-LYNX-MIB", "ipAddress"),
        ("WESTERMO-LYNX-MIB", "ipNetMask"),
        ("WESTERMO-LYNX-MIB", "defaultGateway"),
        ("WESTERMO-LYNX-MIB", "dhcpRelayAgent"),
        ("WESTERMO-LYNX-MIB", "dhcpRelayAgentServer1"),
        ("WESTERMO-LYNX-MIB", "dhcpRelayAgentServer2"),
        ("WESTERMO-LYNX-MIB", "rstp"),
        ("WESTERMO-LYNX-MIB", "statusCode"),
        ("WESTERMO-LYNX-MIB", "enableStatusTrap"))
)
if mibBuilder.loadTexts:
    miscGroup.setStatus("current")

igmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 18)
)
igmpGroup.setObjects(
      *(("WESTERMO-LYNX-MIB", "snooping"),
        ("WESTERMO-LYNX-MIB", "querier"),
        ("WESTERMO-LYNX-MIB", "automode"),
        ("WESTERMO-LYNX-MIB", "stopfilter"),
        ("WESTERMO-LYNX-MIB", "querytimeout"))
)
if mibBuilder.loadTexts:
    igmpGroup.setStatus("current")


# Notification objects

statWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    statWarning.setStatus(
        "current"
    )

statNoWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    statNoWarning.setStatus(
        "current"
    )

linkUpChangeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    linkUpChangeWarning.setStatus(
        "current"
    )

linkDownChangeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 7, 4)
)
if mibBuilder.loadTexts:
    linkDownChangeWarning.setStatus(
        "current"
    )


# Notifications groups

trapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 2, 1, 17)
)
trapGroup.setObjects(
      *(("WESTERMO-LYNX-MIB", "statWarning"),
        ("WESTERMO-LYNX-MIB", "statNoWarning"),
        ("WESTERMO-LYNX-MIB", "linkUpChangeWarning"),
        ("WESTERMO-LYNX-MIB", "linkDownChangeWarning"))
)
if mibBuilder.loadTexts:
    trapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-LYNX-MIB",
    **{"lynx": lynx,
       "general": general,
       "temperature": temperature,
       "swVersion": swVersion,
       "swVersionBootLoader": swVersionBootLoader,
       "hwVersionBoard": hwVersionBoard,
       "hwVersionPld": hwVersionPld,
       "serialNumber": serialNumber,
       "batchID": batchID,
       "hwConfig": hwConfig,
       "reset": reset,
       "powerSupply": powerSupply,
       "trapHostAddr1": trapHostAddr1,
       "trapHostAddr2": trapHostAddr2,
       "readPassword": readPassword,
       "writePassword": writePassword,
       "portGroup": portGroup,
       "miscGroup": miscGroup,
       "trapGroup": trapGroup,
       "igmpGroup": igmpGroup,
       "config": config,
       "ontPortNumber": ontPortNumber,
       "ontTable": ontTable,
       "ontEntry": ontEntry,
       "portIndex": portIndex,
       "portEnable": portEnable,
       "portDuplexMode": portDuplexMode,
       "portAutoNegotiate": portAutoNegotiate,
       "portSpeed": portSpeed,
       "portAlarm": portAlarm,
       "portType": portType,
       "timeSyncFilters": timeSyncFilters,
       "rstpPortTrunk": rstpPortTrunk,
       "igmpPortTrunk": igmpPortTrunk,
       "removePortTag": removePortTag,
       "vlanId": vlanId,
       "vlanPrio": vlanPrio,
       "portVlanColors": portVlanColors,
       "vlanDefaultColor": vlanDefaultColor,
       "igmpColor": igmpColor,
       "rstpPortStatus": rstpPortStatus,
       "linkStatus": linkStatus,
       "snmp": snmp,
       "frnt": frnt,
       "frntPorts": frntPorts,
       "dhcp": dhcp,
       "enableVlan": enableVlan,
       "ipAddress": ipAddress,
       "ipNetMask": ipNetMask,
       "defaultGateway": defaultGateway,
       "dhcpRelayAgent": dhcpRelayAgent,
       "dhcpRelayAgentServer1": dhcpRelayAgentServer1,
       "dhcpRelayAgentServer2": dhcpRelayAgentServer2,
       "rstp": rstp,
       "igmp": igmp,
       "snooping": snooping,
       "automode": automode,
       "querier": querier,
       "stopfilter": stopfilter,
       "querytimeout": querytimeout,
       "stat": stat,
       "statusCode": statusCode,
       "enableStatusTrap": enableStatusTrap,
       "privTraps": privTraps,
       "statWarning": statWarning,
       "statNoWarning": statNoWarning,
       "linkUpChangeWarning": linkUpChangeWarning,
       "linkDownChangeWarning": linkDownChangeWarning}
)
