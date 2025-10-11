# SNMP MIB module (AtiStackSwitch9424-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/AtiStackSwitch9424-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:12:15 2025
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


# MODULE-IDENTITY

alliedTelesyn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtiProductType(TextualConvention, Integer32):
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
              18,
              19,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("at8324", 2),
          ("at8316F-MT", 3),
          ("at8316F-VF", 4),
          ("at8316F-SC", 5),
          ("at8524M", 6),
          ("at8550GB", 7),
          ("at8516F", 8),
          ("at8550SP", 9),
          ("at9424T-SP", 10),
          ("at9424T-GB", 11),
          ("at9408LC-SP", 12),
          ("at8524-POE", 13),
          ("at9424Ti-SP", 14),
          ("at9448Ts-XP", 15),
          ("at9448Ts", 16),
          ("at9448T-SP", 17),
          ("at9424Ts-XP", 18),
          ("at9424Ts", 19),
          ("at9424T", 21),
          ("at9424T-POE", 22),
          ("at9424TL", 23))
    )



class AtiPortType(TextualConvention, Integer32):
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
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("notPresent", 2),
          ("mgmt", 3),
          ("tenBaseT", 4),
          ("hundredBaseT", 5),
          ("hundredBaseFX-VF", 6),
          ("hundredBaseFX-MT", 7),
          ("hundredBaseFX-SC", 8),
          ("hundredBaseFX-LC", 9),
          ("thousandBaseT", 10),
          ("gigabit", 11),
          ("gigabitSX", 12),
          ("gigabitSX-SC", 13),
          ("gigabitSX-MT", 14),
          ("gigabitSX-VF", 15),
          ("gigabitSX-LC", 16),
          ("gigabitLX", 17),
          ("gigabitLX-SC", 18),
          ("gigabitLX-MT", 19),
          ("gigabitLX-VF", 20),
          ("gigabitLX-LC", 21),
          ("sm15", 22),
          ("ten-gigabit", 23))
    )



class AtiUplinkType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("other", 2),
          ("applique-at-45-sc-sm", 3),
          ("applique-at-45-sc", 4),
          ("applique-at-45-mt", 5),
          ("applique-at-46", 6),
          ("applique-at-47", 7),
          ("sfp", 8),
          ("gbic", 9),
          ("xfp", 10))
    )



# MIB Managed Objects in the order of their OIDs

_AtiProduct_ObjectIdentity = ObjectIdentity
atiProduct = _AtiProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
_Swhub_ObjectIdentity = ObjectIdentity
swhub = _Swhub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4)
)
_At_8324_ObjectIdentity = ObjectIdentity
at_8324 = _At_8324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 37)
)
_At_8316F_ObjectIdentity = ObjectIdentity
at_8316F = _At_8316F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 77)
)
_At_8524M_ObjectIdentity = ObjectIdentity
at_8524M = _At_8524M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 98)
)
_At_8550GB_ObjectIdentity = ObjectIdentity
at_8550GB = _At_8550GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 99)
)
_At_8516F_ObjectIdentity = ObjectIdentity
at_8516F = _At_8516F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 100)
)
_At_8550SP_ObjectIdentity = ObjectIdentity
at_8550SP = _At_8550SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 104)
)
_At_9424T_SP_ObjectIdentity = ObjectIdentity
at_9424T_SP = _At_9424T_SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 105)
)
_At_9424T_GB_ObjectIdentity = ObjectIdentity
at_9424T_GB = _At_9424T_GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 112)
)
_At_8524POE_ObjectIdentity = ObjectIdentity
at_8524POE = _At_8524POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 113)
)
_At_9408LC_SP_ObjectIdentity = ObjectIdentity
at_9408LC_SP = _At_9408LC_SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 117)
)
_At_9424Ti_SP_ObjectIdentity = ObjectIdentity
at_9424Ti_SP = _At_9424Ti_SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 118)
)
_At_9448Ts_XP_ObjectIdentity = ObjectIdentity
at_9448Ts_XP = _At_9448Ts_XP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 119)
)
_At_9448Ts_ObjectIdentity = ObjectIdentity
at_9448Ts = _At_9448Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 130)
)
_At_9448T_SP_ObjectIdentity = ObjectIdentity
at_9448T_SP = _At_9448T_SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 131)
)
_At_9424Ts_XP_ObjectIdentity = ObjectIdentity
at_9424Ts_XP = _At_9424Ts_XP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 132)
)
_At_9424Ts_ObjectIdentity = ObjectIdentity
at_9424Ts = _At_9424Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 133)
)
_At_9424T_ObjectIdentity = ObjectIdentity
at_9424T = _At_9424T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 146)
)
_At_9424TPOE_ObjectIdentity = ObjectIdentity
at_9424TPOE = _At_9424TPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 152)
)
_At_9424TL_ObjectIdentity = ObjectIdentity
at_9424TL = _At_9424TL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 153)
)
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_AtiStkSwMib_ObjectIdentity = ObjectIdentity
atiStkSwMib = _AtiStkSwMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17)
)
_AtiStkSwSysGroup_ObjectIdentity = ObjectIdentity
atiStkSwSysGroup = _AtiStkSwSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1)
)
_AtiStkSwSysConfig_ObjectIdentity = ObjectIdentity
atiStkSwSysConfig = _AtiStkSwSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1)
)


class _AtiStkSwSysReset_Type(Integer32):
    """Custom type atiStkSwSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2))
    )


_AtiStkSwSysReset_Type.__name__ = "Integer32"
_AtiStkSwSysReset_Object = MibScalar
atiStkSwSysReset = _AtiStkSwSysReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 1),
    _AtiStkSwSysReset_Type()
)
atiStkSwSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysReset.setStatus("current")
_AtiStkSwSysIpAddress_Type = IpAddress
_AtiStkSwSysIpAddress_Object = MibScalar
atiStkSwSysIpAddress = _AtiStkSwSysIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 2),
    _AtiStkSwSysIpAddress_Type()
)
atiStkSwSysIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysIpAddress.setStatus("current")
_AtiStkSwSysSubnetMask_Type = IpAddress
_AtiStkSwSysSubnetMask_Object = MibScalar
atiStkSwSysSubnetMask = _AtiStkSwSysSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 3),
    _AtiStkSwSysSubnetMask_Type()
)
atiStkSwSysSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysSubnetMask.setStatus("current")
_AtiStkSwSysGateway_Type = IpAddress
_AtiStkSwSysGateway_Object = MibScalar
atiStkSwSysGateway = _AtiStkSwSysGateway_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 4),
    _AtiStkSwSysGateway_Type()
)
atiStkSwSysGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysGateway.setStatus("current")


class _AtiStkSwSysIpAddressStatus_Type(Integer32):
    """Custom type atiStkSwSysIpAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fromDhcp", 1),
          ("fromBootp", 2),
          ("static", 3))
    )


_AtiStkSwSysIpAddressStatus_Type.__name__ = "Integer32"
_AtiStkSwSysIpAddressStatus_Object = MibScalar
atiStkSwSysIpAddressStatus = _AtiStkSwSysIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 5),
    _AtiStkSwSysIpAddressStatus_Type()
)
atiStkSwSysIpAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysIpAddressStatus.setStatus("current")
_AtiStkSwSysDnsServer_Type = IpAddress
_AtiStkSwSysDnsServer_Object = MibScalar
atiStkSwSysDnsServer = _AtiStkSwSysDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 6),
    _AtiStkSwSysDnsServer_Type()
)
atiStkSwSysDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysDnsServer.setStatus("current")
_AtiStkSwSysDefaultDomainName_Type = DisplayString
_AtiStkSwSysDefaultDomainName_Object = MibScalar
atiStkSwSysDefaultDomainName = _AtiStkSwSysDefaultDomainName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 7),
    _AtiStkSwSysDefaultDomainName_Type()
)
atiStkSwSysDefaultDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysDefaultDomainName.setStatus("current")
_AtiStkSwSysNumberOfModules_Type = Integer32
_AtiStkSwSysNumberOfModules_Object = MibScalar
atiStkSwSysNumberOfModules = _AtiStkSwSysNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 8),
    _AtiStkSwSysNumberOfModules_Type()
)
atiStkSwSysNumberOfModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysNumberOfModules.setStatus("current")


class _AtiStkSwSysSpanningTreeStatus_Type(Integer32):
    """Custom type atiStkSwSysSpanningTreeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AtiStkSwSysSpanningTreeStatus_Type.__name__ = "Integer32"
_AtiStkSwSysSpanningTreeStatus_Object = MibScalar
atiStkSwSysSpanningTreeStatus = _AtiStkSwSysSpanningTreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 9),
    _AtiStkSwSysSpanningTreeStatus_Type()
)
atiStkSwSysSpanningTreeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysSpanningTreeStatus.setStatus("current")


class _AtiStkSwSysSpanningTreeVersion_Type(Integer32):
    """Custom type atiStkSwSysSpanningTreeVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 1),
          ("stp", 2),
          ("mstp", 3))
    )


_AtiStkSwSysSpanningTreeVersion_Type.__name__ = "Integer32"
_AtiStkSwSysSpanningTreeVersion_Object = MibScalar
atiStkSwSysSpanningTreeVersion = _AtiStkSwSysSpanningTreeVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 10),
    _AtiStkSwSysSpanningTreeVersion_Type()
)
atiStkSwSysSpanningTreeVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysSpanningTreeVersion.setStatus("current")


class _AtiStkSwSysAction_Type(Integer32):
    """Custom type atiStkSwSysAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("saveConfig", 1),
          ("reset", 2),
          ("defaultConfig", 3))
    )


_AtiStkSwSysAction_Type.__name__ = "Integer32"
_AtiStkSwSysAction_Object = MibScalar
atiStkSwSysAction = _AtiStkSwSysAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 11),
    _AtiStkSwSysAction_Type()
)
atiStkSwSysAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysAction.setStatus("current")


class _AtiStkSwSysNumOfModuleInStack_Type(Integer32):
    """Custom type atiStkSwSysNumOfModuleInStack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwSysNumOfModuleInStack_Type.__name__ = "Integer32"
_AtiStkSwSysNumOfModuleInStack_Object = MibScalar
atiStkSwSysNumOfModuleInStack = _AtiStkSwSysNumOfModuleInStack_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 1, 12),
    _AtiStkSwSysNumOfModuleInStack_Type()
)
atiStkSwSysNumOfModuleInStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysNumOfModuleInStack.setStatus("current")
_AtiStkSwSysNwMgmt_ObjectIdentity = ObjectIdentity
atiStkSwSysNwMgmt = _AtiStkSwSysNwMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 2)
)
_AtiStkSwSysTrapRecv1_Type = IpAddress
_AtiStkSwSysTrapRecv1_Object = MibScalar
atiStkSwSysTrapRecv1 = _AtiStkSwSysTrapRecv1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 2, 1),
    _AtiStkSwSysTrapRecv1_Type()
)
atiStkSwSysTrapRecv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysTrapRecv1.setStatus("obsolete")
_AtiStkSwSysTrapRecv2_Type = IpAddress
_AtiStkSwSysTrapRecv2_Object = MibScalar
atiStkSwSysTrapRecv2 = _AtiStkSwSysTrapRecv2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 2, 2),
    _AtiStkSwSysTrapRecv2_Type()
)
atiStkSwSysTrapRecv2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysTrapRecv2.setStatus("obsolete")
_AtiStkSwSysTrapRecv3_Type = IpAddress
_AtiStkSwSysTrapRecv3_Object = MibScalar
atiStkSwSysTrapRecv3 = _AtiStkSwSysTrapRecv3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 2, 3),
    _AtiStkSwSysTrapRecv3_Type()
)
atiStkSwSysTrapRecv3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysTrapRecv3.setStatus("obsolete")
_AtiStkSwSysTrapRecv4_Type = IpAddress
_AtiStkSwSysTrapRecv4_Object = MibScalar
atiStkSwSysTrapRecv4 = _AtiStkSwSysTrapRecv4_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 2, 4),
    _AtiStkSwSysTrapRecv4_Type()
)
atiStkSwSysTrapRecv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysTrapRecv4.setStatus("obsolete")
_AtiStkSwSysProductInfoTable_Object = MibTable
atiStkSwSysProductInfoTable = _AtiStkSwSysProductInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3)
)
if mibBuilder.loadTexts:
    atiStkSwSysProductInfoTable.setStatus("current")
_AtiStkSwSysProductInfoEntry_Object = MibTableRow
atiStkSwSysProductInfoEntry = _AtiStkSwSysProductInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1)
)
atiStkSwSysProductInfoEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwSysModuleId"),
)
if mibBuilder.loadTexts:
    atiStkSwSysProductInfoEntry.setStatus("current")


class _AtiStkSwSysModuleId_Type(Integer32):
    """Custom type atiStkSwSysModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwSysModuleId_Type.__name__ = "Integer32"
_AtiStkSwSysModuleId_Object = MibTableColumn
atiStkSwSysModuleId = _AtiStkSwSysModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 1),
    _AtiStkSwSysModuleId_Type()
)
atiStkSwSysModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysModuleId.setStatus("current")
_AtiStkSwSysProductType_Type = AtiProductType
_AtiStkSwSysProductType_Object = MibTableColumn
atiStkSwSysProductType = _AtiStkSwSysProductType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 2),
    _AtiStkSwSysProductType_Type()
)
atiStkSwSysProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysProductType.setStatus("current")
_AtiStkSwSysMacAddress_Type = MacAddress
_AtiStkSwSysMacAddress_Object = MibTableColumn
atiStkSwSysMacAddress = _AtiStkSwSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 3),
    _AtiStkSwSysMacAddress_Type()
)
atiStkSwSysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysMacAddress.setStatus("current")


class _AtiStkSwSysSwName_Type(DisplayString):
    """Custom type atiStkSwSysSwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwSysSwName_Type.__name__ = "DisplayString"
_AtiStkSwSysSwName_Object = MibTableColumn
atiStkSwSysSwName = _AtiStkSwSysSwName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 4),
    _AtiStkSwSysSwName_Type()
)
atiStkSwSysSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysSwName.setStatus("current")


class _AtiStkSwSysSwVersion_Type(DisplayString):
    """Custom type atiStkSwSysSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwSysSwVersion_Type.__name__ = "DisplayString"
_AtiStkSwSysSwVersion_Object = MibTableColumn
atiStkSwSysSwVersion = _AtiStkSwSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 5),
    _AtiStkSwSysSwVersion_Type()
)
atiStkSwSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysSwVersion.setStatus("current")


class _AtiStkSwSysHwName_Type(DisplayString):
    """Custom type atiStkSwSysHwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwSysHwName_Type.__name__ = "DisplayString"
_AtiStkSwSysHwName_Object = MibTableColumn
atiStkSwSysHwName = _AtiStkSwSysHwName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 6),
    _AtiStkSwSysHwName_Type()
)
atiStkSwSysHwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysHwName.setStatus("current")


class _AtiStkSwSysHwRevision_Type(DisplayString):
    """Custom type atiStkSwSysHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwSysHwRevision_Type.__name__ = "DisplayString"
_AtiStkSwSysHwRevision_Object = MibTableColumn
atiStkSwSysHwRevision = _AtiStkSwSysHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 7),
    _AtiStkSwSysHwRevision_Type()
)
atiStkSwSysHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysHwRevision.setStatus("current")


class _AtiStkSwSysSerialNumber_Type(DisplayString):
    """Custom type atiStkSwSysSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwSysSerialNumber_Type.__name__ = "DisplayString"
_AtiStkSwSysSerialNumber_Object = MibTableColumn
atiStkSwSysSerialNumber = _AtiStkSwSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 8),
    _AtiStkSwSysSerialNumber_Type()
)
atiStkSwSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysSerialNumber.setStatus("current")
_AtiStkSwSysTotalPortCount_Type = Integer32
_AtiStkSwSysTotalPortCount_Object = MibTableColumn
atiStkSwSysTotalPortCount = _AtiStkSwSysTotalPortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 9),
    _AtiStkSwSysTotalPortCount_Type()
)
atiStkSwSysTotalPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysTotalPortCount.setStatus("current")
_AtiStkSwSysBasePortType_Type = AtiPortType
_AtiStkSwSysBasePortType_Object = MibTableColumn
atiStkSwSysBasePortType = _AtiStkSwSysBasePortType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 10),
    _AtiStkSwSysBasePortType_Type()
)
atiStkSwSysBasePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysBasePortType.setStatus("current")
_AtiStkSwSysBasePortCount_Type = Integer32
_AtiStkSwSysBasePortCount_Object = MibTableColumn
atiStkSwSysBasePortCount = _AtiStkSwSysBasePortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 11),
    _AtiStkSwSysBasePortCount_Type()
)
atiStkSwSysBasePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysBasePortCount.setStatus("current")


class _AtiStkSwSysUplinkAModelName_Type(DisplayString):
    """Custom type atiStkSwSysUplinkAModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwSysUplinkAModelName_Type.__name__ = "DisplayString"
_AtiStkSwSysUplinkAModelName_Object = MibTableColumn
atiStkSwSysUplinkAModelName = _AtiStkSwSysUplinkAModelName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 12),
    _AtiStkSwSysUplinkAModelName_Type()
)
atiStkSwSysUplinkAModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkAModelName.setStatus("current")
_AtiStkSwSysUplinkAPortType_Type = AtiPortType
_AtiStkSwSysUplinkAPortType_Object = MibTableColumn
atiStkSwSysUplinkAPortType = _AtiStkSwSysUplinkAPortType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 13),
    _AtiStkSwSysUplinkAPortType_Type()
)
atiStkSwSysUplinkAPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkAPortType.setStatus("current")
_AtiStkSwSysUplinkAPortCount_Type = Integer32
_AtiStkSwSysUplinkAPortCount_Object = MibTableColumn
atiStkSwSysUplinkAPortCount = _AtiStkSwSysUplinkAPortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 14),
    _AtiStkSwSysUplinkAPortCount_Type()
)
atiStkSwSysUplinkAPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkAPortCount.setStatus("current")
_AtiStkSwSysUplinkAPortIdBase_Type = Integer32
_AtiStkSwSysUplinkAPortIdBase_Object = MibTableColumn
atiStkSwSysUplinkAPortIdBase = _AtiStkSwSysUplinkAPortIdBase_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 15),
    _AtiStkSwSysUplinkAPortIdBase_Type()
)
atiStkSwSysUplinkAPortIdBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkAPortIdBase.setStatus("current")
_AtiStkSwSysUplinkAPortIdLimit_Type = Integer32
_AtiStkSwSysUplinkAPortIdLimit_Object = MibTableColumn
atiStkSwSysUplinkAPortIdLimit = _AtiStkSwSysUplinkAPortIdLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 16),
    _AtiStkSwSysUplinkAPortIdLimit_Type()
)
atiStkSwSysUplinkAPortIdLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkAPortIdLimit.setStatus("current")


class _AtiStkSwSysUplinkBModelName_Type(DisplayString):
    """Custom type atiStkSwSysUplinkBModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwSysUplinkBModelName_Type.__name__ = "DisplayString"
_AtiStkSwSysUplinkBModelName_Object = MibTableColumn
atiStkSwSysUplinkBModelName = _AtiStkSwSysUplinkBModelName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 17),
    _AtiStkSwSysUplinkBModelName_Type()
)
atiStkSwSysUplinkBModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkBModelName.setStatus("current")
_AtiStkSwSysUplinkBPortType_Type = AtiPortType
_AtiStkSwSysUplinkBPortType_Object = MibTableColumn
atiStkSwSysUplinkBPortType = _AtiStkSwSysUplinkBPortType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 18),
    _AtiStkSwSysUplinkBPortType_Type()
)
atiStkSwSysUplinkBPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkBPortType.setStatus("current")
_AtiStkSwSysUplinkBPortCount_Type = Integer32
_AtiStkSwSysUplinkBPortCount_Object = MibTableColumn
atiStkSwSysUplinkBPortCount = _AtiStkSwSysUplinkBPortCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 19),
    _AtiStkSwSysUplinkBPortCount_Type()
)
atiStkSwSysUplinkBPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkBPortCount.setStatus("current")
_AtiStkSwSysUplinkBPortIdBase_Type = Integer32
_AtiStkSwSysUplinkBPortIdBase_Object = MibTableColumn
atiStkSwSysUplinkBPortIdBase = _AtiStkSwSysUplinkBPortIdBase_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 20),
    _AtiStkSwSysUplinkBPortIdBase_Type()
)
atiStkSwSysUplinkBPortIdBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkBPortIdBase.setStatus("current")
_AtiStkSwSysUplinkBPortIdLimit_Type = Integer32
_AtiStkSwSysUplinkBPortIdLimit_Object = MibTableColumn
atiStkSwSysUplinkBPortIdLimit = _AtiStkSwSysUplinkBPortIdLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 21),
    _AtiStkSwSysUplinkBPortIdLimit_Type()
)
atiStkSwSysUplinkBPortIdLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkBPortIdLimit.setStatus("current")


class _AtiStkSwSysRPSPresent_Type(Integer32):
    """Custom type atiStkSwSysRPSPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_AtiStkSwSysRPSPresent_Type.__name__ = "Integer32"
_AtiStkSwSysRPSPresent_Object = MibTableColumn
atiStkSwSysRPSPresent = _AtiStkSwSysRPSPresent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 22),
    _AtiStkSwSysRPSPresent_Type()
)
atiStkSwSysRPSPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysRPSPresent.setStatus("current")


class _AtiStkSwSysRPSState_Type(Integer32):
    """Custom type atiStkSwSysRPSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtiStkSwSysRPSState_Type.__name__ = "Integer32"
_AtiStkSwSysRPSState_Object = MibTableColumn
atiStkSwSysRPSState = _AtiStkSwSysRPSState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 23),
    _AtiStkSwSysRPSState_Type()
)
atiStkSwSysRPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysRPSState.setStatus("current")


class _AtiStkSwSysDCState_Type(Integer32):
    """Custom type atiStkSwSysDCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AtiStkSwSysDCState_Type.__name__ = "Integer32"
_AtiStkSwSysDCState_Object = MibTableColumn
atiStkSwSysDCState = _AtiStkSwSysDCState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 24),
    _AtiStkSwSysDCState_Type()
)
atiStkSwSysDCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysDCState.setStatus("current")
_AtiStkSwSysTemperatureLimitValue_Type = Integer32
_AtiStkSwSysTemperatureLimitValue_Object = MibTableColumn
atiStkSwSysTemperatureLimitValue = _AtiStkSwSysTemperatureLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 3, 1, 25),
    _AtiStkSwSysTemperatureLimitValue_Type()
)
atiStkSwSysTemperatureLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysTemperatureLimitValue.setStatus("current")
_AtiStkSwSysUplinkInfoTable_Object = MibTable
atiStkSwSysUplinkInfoTable = _AtiStkSwSysUplinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 4)
)
if mibBuilder.loadTexts:
    atiStkSwSysUplinkInfoTable.setStatus("current")
_AtiStkSwSysUplinkInfoEntry_Object = MibTableRow
atiStkSwSysUplinkInfoEntry = _AtiStkSwSysUplinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 4, 1)
)
atiStkSwSysUplinkInfoEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwSysUplinkModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwSysUplinkPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwSysUplinkInfoEntry.setStatus("current")


class _AtiStkSwSysUplinkModuleId_Type(Integer32):
    """Custom type atiStkSwSysUplinkModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwSysUplinkModuleId_Type.__name__ = "Integer32"
_AtiStkSwSysUplinkModuleId_Object = MibTableColumn
atiStkSwSysUplinkModuleId = _AtiStkSwSysUplinkModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 4, 1, 1),
    _AtiStkSwSysUplinkModuleId_Type()
)
atiStkSwSysUplinkModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkModuleId.setStatus("current")


class _AtiStkSwSysUplinkPortId_Type(Integer32):
    """Custom type atiStkSwSysUplinkPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AtiStkSwSysUplinkPortId_Type.__name__ = "Integer32"
_AtiStkSwSysUplinkPortId_Object = MibTableColumn
atiStkSwSysUplinkPortId = _AtiStkSwSysUplinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 4, 1, 2),
    _AtiStkSwSysUplinkPortId_Type()
)
atiStkSwSysUplinkPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkPortId.setStatus("current")


class _AtiStkSwSysUplinkSetup_Type(Integer32):
    """Custom type atiStkSwSysUplinkSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("pluggable", 2))
    )


_AtiStkSwSysUplinkSetup_Type.__name__ = "Integer32"
_AtiStkSwSysUplinkSetup_Object = MibTableColumn
atiStkSwSysUplinkSetup = _AtiStkSwSysUplinkSetup_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 4, 1, 3),
    _AtiStkSwSysUplinkSetup_Type()
)
atiStkSwSysUplinkSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkSetup.setStatus("current")
_AtiStkSwSysUplinkType_Type = AtiUplinkType
_AtiStkSwSysUplinkType_Object = MibTableColumn
atiStkSwSysUplinkType = _AtiStkSwSysUplinkType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 4, 1, 4),
    _AtiStkSwSysUplinkType_Type()
)
atiStkSwSysUplinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkType.setStatus("current")


class _AtiStkSwSysUplinkDetails_Type(DisplayString):
    """Custom type atiStkSwSysUplinkDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwSysUplinkDetails_Type.__name__ = "DisplayString"
_AtiStkSwSysUplinkDetails_Object = MibTableColumn
atiStkSwSysUplinkDetails = _AtiStkSwSysUplinkDetails_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 4, 1, 5),
    _AtiStkSwSysUplinkDetails_Type()
)
atiStkSwSysUplinkDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkDetails.setStatus("current")
_AtiStkSwSysUplinkPortType_Type = AtiPortType
_AtiStkSwSysUplinkPortType_Object = MibTableColumn
atiStkSwSysUplinkPortType = _AtiStkSwSysUplinkPortType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 4, 1, 6),
    _AtiStkSwSysUplinkPortType_Type()
)
atiStkSwSysUplinkPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysUplinkPortType.setStatus("current")
_AtiStkSwSysSystemTimeConfig_ObjectIdentity = ObjectIdentity
atiStkSwSysSystemTimeConfig = _AtiStkSwSysSystemTimeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 5)
)


class _AtiStkSwSysCurrentTime_Type(DisplayString):
    """Custom type atiStkSwSysCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtiStkSwSysCurrentTime_Type.__name__ = "DisplayString"
_AtiStkSwSysCurrentTime_Object = MibScalar
atiStkSwSysCurrentTime = _AtiStkSwSysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 5, 1),
    _AtiStkSwSysCurrentTime_Type()
)
atiStkSwSysCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysCurrentTime.setStatus("current")


class _AtiStkSwSysCurrentDate_Type(DisplayString):
    """Custom type atiStkSwSysCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtiStkSwSysCurrentDate_Type.__name__ = "DisplayString"
_AtiStkSwSysCurrentDate_Object = MibScalar
atiStkSwSysCurrentDate = _AtiStkSwSysCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 5, 2),
    _AtiStkSwSysCurrentDate_Type()
)
atiStkSwSysCurrentDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysCurrentDate.setStatus("current")


class _AtiStkSwSysSNTPStatus_Type(Integer32):
    """Custom type atiStkSwSysSNTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtiStkSwSysSNTPStatus_Type.__name__ = "Integer32"
_AtiStkSwSysSNTPStatus_Object = MibScalar
atiStkSwSysSNTPStatus = _AtiStkSwSysSNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 5, 3),
    _AtiStkSwSysSNTPStatus_Type()
)
atiStkSwSysSNTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysSNTPStatus.setStatus("current")
_AtiStkSwSysSNTPServerIPAddress_Type = IpAddress
_AtiStkSwSysSNTPServerIPAddress_Object = MibScalar
atiStkSwSysSNTPServerIPAddress = _AtiStkSwSysSNTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 5, 4),
    _AtiStkSwSysSNTPServerIPAddress_Type()
)
atiStkSwSysSNTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysSNTPServerIPAddress.setStatus("current")


class _AtiStkSwSysSNTPUTCOffset_Type(Integer32):
    """Custom type atiStkSwSysSNTPUTCOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_AtiStkSwSysSNTPUTCOffset_Type.__name__ = "Integer32"
_AtiStkSwSysSNTPUTCOffset_Object = MibScalar
atiStkSwSysSNTPUTCOffset = _AtiStkSwSysSNTPUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 5, 5),
    _AtiStkSwSysSNTPUTCOffset_Type()
)
atiStkSwSysSNTPUTCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysSNTPUTCOffset.setStatus("current")


class _AtiStkSwSysSNTPDSTStatus_Type(Integer32):
    """Custom type atiStkSwSysSNTPDSTStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtiStkSwSysSNTPDSTStatus_Type.__name__ = "Integer32"
_AtiStkSwSysSNTPDSTStatus_Object = MibScalar
atiStkSwSysSNTPDSTStatus = _AtiStkSwSysSNTPDSTStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 5, 6),
    _AtiStkSwSysSNTPDSTStatus_Type()
)
atiStkSwSysSNTPDSTStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysSNTPDSTStatus.setStatus("current")


class _AtiStkSwSysSNTPPollingInterval_Type(Integer32):
    """Custom type atiStkSwSysSNTPPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1200),
    )


_AtiStkSwSysSNTPPollingInterval_Type.__name__ = "Integer32"
_AtiStkSwSysSNTPPollingInterval_Object = MibScalar
atiStkSwSysSNTPPollingInterval = _AtiStkSwSysSNTPPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 5, 7),
    _AtiStkSwSysSNTPPollingInterval_Type()
)
atiStkSwSysSNTPPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysSNTPPollingInterval.setStatus("current")
_AtiStkSwSysSNTPLastDelta_Type = Integer32
_AtiStkSwSysSNTPLastDelta_Object = MibScalar
atiStkSwSysSNTPLastDelta = _AtiStkSwSysSNTPLastDelta_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 5, 8),
    _AtiStkSwSysSNTPLastDelta_Type()
)
atiStkSwSysSNTPLastDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysSNTPLastDelta.setStatus("current")
_AtiStkSwSysInfoGroup_ObjectIdentity = ObjectIdentity
atiStkSwSysInfoGroup = _AtiStkSwSysInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6)
)
_AtiStkSwTemperatureInfoTable_Object = MibTable
atiStkSwTemperatureInfoTable = _AtiStkSwTemperatureInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 1)
)
if mibBuilder.loadTexts:
    atiStkSwTemperatureInfoTable.setStatus("current")
_AtiStkSwTemperatureInfoEntry_Object = MibTableRow
atiStkSwTemperatureInfoEntry = _AtiStkSwTemperatureInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 1, 1)
)
atiStkSwTemperatureInfoEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwTemperatureInfoModuleId"),
)
if mibBuilder.loadTexts:
    atiStkSwTemperatureInfoEntry.setStatus("current")


class _AtiStkSwTemperatureInfoModuleId_Type(Integer32):
    """Custom type atiStkSwTemperatureInfoModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwTemperatureInfoModuleId_Type.__name__ = "Integer32"
_AtiStkSwTemperatureInfoModuleId_Object = MibTableColumn
atiStkSwTemperatureInfoModuleId = _AtiStkSwTemperatureInfoModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 1, 1, 1),
    _AtiStkSwTemperatureInfoModuleId_Type()
)
atiStkSwTemperatureInfoModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwTemperatureInfoModuleId.setStatus("current")


class _AtiStkSwTemperatureInfoTemperature_Type(DisplayString):
    """Custom type atiStkSwTemperatureInfoTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AtiStkSwTemperatureInfoTemperature_Type.__name__ = "DisplayString"
_AtiStkSwTemperatureInfoTemperature_Object = MibTableColumn
atiStkSwTemperatureInfoTemperature = _AtiStkSwTemperatureInfoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 1, 1, 2),
    _AtiStkSwTemperatureInfoTemperature_Type()
)
atiStkSwTemperatureInfoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwTemperatureInfoTemperature.setStatus("current")
_AtiStkSwFanInfoTable_Object = MibTable
atiStkSwFanInfoTable = _AtiStkSwFanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 2)
)
if mibBuilder.loadTexts:
    atiStkSwFanInfoTable.setStatus("current")
_AtiStkSwFanInfoEntry_Object = MibTableRow
atiStkSwFanInfoEntry = _AtiStkSwFanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 2, 1)
)
atiStkSwFanInfoEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwFanInfoModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwFanInfoFanId"),
)
if mibBuilder.loadTexts:
    atiStkSwFanInfoEntry.setStatus("current")


class _AtiStkSwFanInfoModuleId_Type(Integer32):
    """Custom type atiStkSwFanInfoModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwFanInfoModuleId_Type.__name__ = "Integer32"
_AtiStkSwFanInfoModuleId_Object = MibTableColumn
atiStkSwFanInfoModuleId = _AtiStkSwFanInfoModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 2, 1, 1),
    _AtiStkSwFanInfoModuleId_Type()
)
atiStkSwFanInfoModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwFanInfoModuleId.setStatus("current")


class _AtiStkSwFanInfoFanId_Type(Integer32):
    """Custom type atiStkSwFanInfoFanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwFanInfoFanId_Type.__name__ = "Integer32"
_AtiStkSwFanInfoFanId_Object = MibTableColumn
atiStkSwFanInfoFanId = _AtiStkSwFanInfoFanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 2, 1, 2),
    _AtiStkSwFanInfoFanId_Type()
)
atiStkSwFanInfoFanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwFanInfoFanId.setStatus("current")


class _AtiStkSwFanInfoState_Type(DisplayString):
    """Custom type atiStkSwFanInfoState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_AtiStkSwFanInfoState_Type.__name__ = "DisplayString"
_AtiStkSwFanInfoState_Object = MibTableColumn
atiStkSwFanInfoState = _AtiStkSwFanInfoState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 2, 1, 3),
    _AtiStkSwFanInfoState_Type()
)
atiStkSwFanInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwFanInfoState.setStatus("current")


class _AtiStkSwFanInfoSpeed_Type(DisplayString):
    """Custom type atiStkSwFanInfoSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_AtiStkSwFanInfoSpeed_Type.__name__ = "DisplayString"
_AtiStkSwFanInfoSpeed_Object = MibTableColumn
atiStkSwFanInfoSpeed = _AtiStkSwFanInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 2, 1, 4),
    _AtiStkSwFanInfoSpeed_Type()
)
atiStkSwFanInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwFanInfoSpeed.setStatus("current")
_AtiStkSwVoltageInfoTable_Object = MibTable
atiStkSwVoltageInfoTable = _AtiStkSwVoltageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 3)
)
if mibBuilder.loadTexts:
    atiStkSwVoltageInfoTable.setStatus("current")
_AtiStkSwVoltageInfoEntry_Object = MibTableRow
atiStkSwVoltageInfoEntry = _AtiStkSwVoltageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 3, 1)
)
atiStkSwVoltageInfoEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwVoltageInfoModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwVoltageInfoIndex"),
)
if mibBuilder.loadTexts:
    atiStkSwVoltageInfoEntry.setStatus("current")


class _AtiStkSwVoltageInfoModuleId_Type(Integer32):
    """Custom type atiStkSwVoltageInfoModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwVoltageInfoModuleId_Type.__name__ = "Integer32"
_AtiStkSwVoltageInfoModuleId_Object = MibTableColumn
atiStkSwVoltageInfoModuleId = _AtiStkSwVoltageInfoModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 3, 1, 1),
    _AtiStkSwVoltageInfoModuleId_Type()
)
atiStkSwVoltageInfoModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwVoltageInfoModuleId.setStatus("current")


class _AtiStkSwVoltageInfoIndex_Type(Integer32):
    """Custom type atiStkSwVoltageInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AtiStkSwVoltageInfoIndex_Type.__name__ = "Integer32"
_AtiStkSwVoltageInfoIndex_Object = MibTableColumn
atiStkSwVoltageInfoIndex = _AtiStkSwVoltageInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 3, 1, 2),
    _AtiStkSwVoltageInfoIndex_Type()
)
atiStkSwVoltageInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwVoltageInfoIndex.setStatus("current")


class _AtiStkSwVoltageInfoLevel_Type(DisplayString):
    """Custom type atiStkSwVoltageInfoLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AtiStkSwVoltageInfoLevel_Type.__name__ = "DisplayString"
_AtiStkSwVoltageInfoLevel_Object = MibTableColumn
atiStkSwVoltageInfoLevel = _AtiStkSwVoltageInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 3, 1, 3),
    _AtiStkSwVoltageInfoLevel_Type()
)
atiStkSwVoltageInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwVoltageInfoLevel.setStatus("current")


class _AtiStkSwVoltageInfoMeasured_Type(DisplayString):
    """Custom type atiStkSwVoltageInfoMeasured based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AtiStkSwVoltageInfoMeasured_Type.__name__ = "DisplayString"
_AtiStkSwVoltageInfoMeasured_Object = MibTableColumn
atiStkSwVoltageInfoMeasured = _AtiStkSwVoltageInfoMeasured_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 3, 1, 4),
    _AtiStkSwVoltageInfoMeasured_Type()
)
atiStkSwVoltageInfoMeasured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwVoltageInfoMeasured.setStatus("current")
_AtiStkSwCPUInfoTable_Object = MibTable
atiStkSwCPUInfoTable = _AtiStkSwCPUInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 4)
)
if mibBuilder.loadTexts:
    atiStkSwCPUInfoTable.setStatus("current")
_AtiStkSwCPUInfoEntry_Object = MibTableRow
atiStkSwCPUInfoEntry = _AtiStkSwCPUInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 4, 1)
)
atiStkSwCPUInfoEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwCPUInfoModuleId"),
)
if mibBuilder.loadTexts:
    atiStkSwCPUInfoEntry.setStatus("current")


class _AtiStkSwCPUInfoModuleId_Type(Integer32):
    """Custom type atiStkSwCPUInfoModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwCPUInfoModuleId_Type.__name__ = "Integer32"
_AtiStkSwCPUInfoModuleId_Object = MibTableColumn
atiStkSwCPUInfoModuleId = _AtiStkSwCPUInfoModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 4, 1, 1),
    _AtiStkSwCPUInfoModuleId_Type()
)
atiStkSwCPUInfoModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwCPUInfoModuleId.setStatus("current")


class _AtiStkSwCPUInfoAvgLastMinute_Type(Integer32):
    """Custom type atiStkSwCPUInfoAvgLastMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtiStkSwCPUInfoAvgLastMinute_Type.__name__ = "Integer32"
_AtiStkSwCPUInfoAvgLastMinute_Object = MibTableColumn
atiStkSwCPUInfoAvgLastMinute = _AtiStkSwCPUInfoAvgLastMinute_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 4, 1, 2),
    _AtiStkSwCPUInfoAvgLastMinute_Type()
)
atiStkSwCPUInfoAvgLastMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwCPUInfoAvgLastMinute.setStatus("current")


class _AtiStkSwCPUInfoAvgLast20Seconds_Type(Integer32):
    """Custom type atiStkSwCPUInfoAvgLast20Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtiStkSwCPUInfoAvgLast20Seconds_Type.__name__ = "Integer32"
_AtiStkSwCPUInfoAvgLast20Seconds_Object = MibTableColumn
atiStkSwCPUInfoAvgLast20Seconds = _AtiStkSwCPUInfoAvgLast20Seconds_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 4, 1, 3),
    _AtiStkSwCPUInfoAvgLast20Seconds_Type()
)
atiStkSwCPUInfoAvgLast20Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwCPUInfoAvgLast20Seconds.setStatus("current")


class _AtiStkSwCPUInfoAvgSecond_Type(Integer32):
    """Custom type atiStkSwCPUInfoAvgSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AtiStkSwCPUInfoAvgSecond_Type.__name__ = "Integer32"
_AtiStkSwCPUInfoAvgSecond_Object = MibTableColumn
atiStkSwCPUInfoAvgSecond = _AtiStkSwCPUInfoAvgSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 4, 1, 4),
    _AtiStkSwCPUInfoAvgSecond_Type()
)
atiStkSwCPUInfoAvgSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwCPUInfoAvgSecond.setStatus("current")
_AtiStkSwMemoryGroup_ObjectIdentity = ObjectIdentity
atiStkSwMemoryGroup = _AtiStkSwMemoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5)
)
_AtiStkSwMemoryInfoTable_Object = MibTable
atiStkSwMemoryInfoTable = _AtiStkSwMemoryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    atiStkSwMemoryInfoTable.setStatus("current")
_AtiStkSwMemoryInfoEntry_Object = MibTableRow
atiStkSwMemoryInfoEntry = _AtiStkSwMemoryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 1, 1)
)
atiStkSwMemoryInfoEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwMemoryInfoModuleId"),
)
if mibBuilder.loadTexts:
    atiStkSwMemoryInfoEntry.setStatus("current")
_AtiStkSwMemoryInfoModuleId_Type = Integer32
_AtiStkSwMemoryInfoModuleId_Object = MibTableColumn
atiStkSwMemoryInfoModuleId = _AtiStkSwMemoryInfoModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 1, 1, 1),
    _AtiStkSwMemoryInfoModuleId_Type()
)
atiStkSwMemoryInfoModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryInfoModuleId.setStatus("current")
_AtiStkSwMemoryInfoTotalBuffers_Type = Integer32
_AtiStkSwMemoryInfoTotalBuffers_Object = MibTableColumn
atiStkSwMemoryInfoTotalBuffers = _AtiStkSwMemoryInfoTotalBuffers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 1, 1, 2),
    _AtiStkSwMemoryInfoTotalBuffers_Type()
)
atiStkSwMemoryInfoTotalBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryInfoTotalBuffers.setStatus("current")
_AtiStkSwMemoryPoolTable_Object = MibTable
atiStkSwMemoryPoolTable = _AtiStkSwMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    atiStkSwMemoryPoolTable.setStatus("current")
_AtiStkSwMemoryPoolEntry_Object = MibTableRow
atiStkSwMemoryPoolEntry = _AtiStkSwMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 2, 1)
)
atiStkSwMemoryPoolEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwMemoryPoolModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    atiStkSwMemoryPoolEntry.setStatus("current")
_AtiStkSwMemoryPoolModuleId_Type = Integer32
_AtiStkSwMemoryPoolModuleId_Object = MibTableColumn
atiStkSwMemoryPoolModuleId = _AtiStkSwMemoryPoolModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 2, 1, 1),
    _AtiStkSwMemoryPoolModuleId_Type()
)
atiStkSwMemoryPoolModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryPoolModuleId.setStatus("current")
_AtiStkSwMemoryPoolIndex_Type = Integer32
_AtiStkSwMemoryPoolIndex_Object = MibTableColumn
atiStkSwMemoryPoolIndex = _AtiStkSwMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 2, 1, 2),
    _AtiStkSwMemoryPoolIndex_Type()
)
atiStkSwMemoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryPoolIndex.setStatus("current")
_AtiStkSwMemoryPoolName_Type = DisplayString
_AtiStkSwMemoryPoolName_Object = MibTableColumn
atiStkSwMemoryPoolName = _AtiStkSwMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 2, 1, 3),
    _AtiStkSwMemoryPoolName_Type()
)
atiStkSwMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryPoolName.setStatus("current")
_AtiStkSwMemoryPoolTotal_Type = Integer32
_AtiStkSwMemoryPoolTotal_Object = MibTableColumn
atiStkSwMemoryPoolTotal = _AtiStkSwMemoryPoolTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 2, 1, 4),
    _AtiStkSwMemoryPoolTotal_Type()
)
atiStkSwMemoryPoolTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryPoolTotal.setStatus("current")
_AtiStkSwMemoryPoolFree_Type = Integer32
_AtiStkSwMemoryPoolFree_Object = MibTableColumn
atiStkSwMemoryPoolFree = _AtiStkSwMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 2, 1, 5),
    _AtiStkSwMemoryPoolFree_Type()
)
atiStkSwMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryPoolFree.setStatus("current")
_AtiStkSwMemoryComBuffersTable_Object = MibTable
atiStkSwMemoryComBuffersTable = _AtiStkSwMemoryComBuffersTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 3)
)
if mibBuilder.loadTexts:
    atiStkSwMemoryComBuffersTable.setStatus("current")
_AtiStkSwMemoryComBuffersEntry_Object = MibTableRow
atiStkSwMemoryComBuffersEntry = _AtiStkSwMemoryComBuffersEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 3, 1)
)
atiStkSwMemoryComBuffersEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwMemoryComBuffersModuleId"),
)
if mibBuilder.loadTexts:
    atiStkSwMemoryComBuffersEntry.setStatus("current")
_AtiStkSwMemoryComBuffersModuleId_Type = Integer32
_AtiStkSwMemoryComBuffersModuleId_Object = MibTableColumn
atiStkSwMemoryComBuffersModuleId = _AtiStkSwMemoryComBuffersModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 3, 1, 1),
    _AtiStkSwMemoryComBuffersModuleId_Type()
)
atiStkSwMemoryComBuffersModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryComBuffersModuleId.setStatus("current")
_AtiStkSwMemoryTotalComBuffers_Type = Integer32
_AtiStkSwMemoryTotalComBuffers_Object = MibTableColumn
atiStkSwMemoryTotalComBuffers = _AtiStkSwMemoryTotalComBuffers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 3, 1, 2),
    _AtiStkSwMemoryTotalComBuffers_Type()
)
atiStkSwMemoryTotalComBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryTotalComBuffers.setStatus("current")
_AtiStkSwMemoryFreeComBuffers_Type = Integer32
_AtiStkSwMemoryFreeComBuffers_Object = MibTableColumn
atiStkSwMemoryFreeComBuffers = _AtiStkSwMemoryFreeComBuffers_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 6, 5, 3, 1, 3),
    _AtiStkSwMemoryFreeComBuffers_Type()
)
atiStkSwMemoryFreeComBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMemoryFreeComBuffers.setStatus("current")
_AtiStkSwSysMgmtACLGroup_ObjectIdentity = ObjectIdentity
atiStkSwSysMgmtACLGroup = _AtiStkSwSysMgmtACLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7)
)


class _AtiStkSwSysMgmtACLStatus_Type(Integer32):
    """Custom type atiStkSwSysMgmtACLStatus based on Integer32"""
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


_AtiStkSwSysMgmtACLStatus_Type.__name__ = "Integer32"
_AtiStkSwSysMgmtACLStatus_Object = MibScalar
atiStkSwSysMgmtACLStatus = _AtiStkSwSysMgmtACLStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7, 1),
    _AtiStkSwSysMgmtACLStatus_Type()
)
atiStkSwSysMgmtACLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysMgmtACLStatus.setStatus("current")
_AtiStkSwSysMgmtACLConfigTable_Object = MibTable
atiStkSwSysMgmtACLConfigTable = _AtiStkSwSysMgmtACLConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7, 2)
)
if mibBuilder.loadTexts:
    atiStkSwSysMgmtACLConfigTable.setStatus("current")
_AtiStkSwSysMgmtACLConfigEntry_Object = MibTableRow
atiStkSwSysMgmtACLConfigEntry = _AtiStkSwSysMgmtACLConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7, 2, 1)
)
atiStkSwSysMgmtACLConfigEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwSysMgmtACLConfigModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwSysMgmtACLConfigId"),
)
if mibBuilder.loadTexts:
    atiStkSwSysMgmtACLConfigEntry.setStatus("current")


class _AtiStkSwSysMgmtACLConfigModuleId_Type(Integer32):
    """Custom type atiStkSwSysMgmtACLConfigModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwSysMgmtACLConfigModuleId_Type.__name__ = "Integer32"
_AtiStkSwSysMgmtACLConfigModuleId_Object = MibTableColumn
atiStkSwSysMgmtACLConfigModuleId = _AtiStkSwSysMgmtACLConfigModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7, 2, 1, 1),
    _AtiStkSwSysMgmtACLConfigModuleId_Type()
)
atiStkSwSysMgmtACLConfigModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysMgmtACLConfigModuleId.setStatus("current")


class _AtiStkSwSysMgmtACLConfigId_Type(Integer32):
    """Custom type atiStkSwSysMgmtACLConfigId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AtiStkSwSysMgmtACLConfigId_Type.__name__ = "Integer32"
_AtiStkSwSysMgmtACLConfigId_Object = MibTableColumn
atiStkSwSysMgmtACLConfigId = _AtiStkSwSysMgmtACLConfigId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7, 2, 1, 2),
    _AtiStkSwSysMgmtACLConfigId_Type()
)
atiStkSwSysMgmtACLConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwSysMgmtACLConfigId.setStatus("current")
_AtiStkSwSysMgmtACLConfigIpAddr_Type = IpAddress
_AtiStkSwSysMgmtACLConfigIpAddr_Object = MibTableColumn
atiStkSwSysMgmtACLConfigIpAddr = _AtiStkSwSysMgmtACLConfigIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7, 2, 1, 3),
    _AtiStkSwSysMgmtACLConfigIpAddr_Type()
)
atiStkSwSysMgmtACLConfigIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysMgmtACLConfigIpAddr.setStatus("current")
_AtiStkSwSysMgmtACLConfigMask_Type = IpAddress
_AtiStkSwSysMgmtACLConfigMask_Object = MibTableColumn
atiStkSwSysMgmtACLConfigMask = _AtiStkSwSysMgmtACLConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7, 2, 1, 4),
    _AtiStkSwSysMgmtACLConfigMask_Type()
)
atiStkSwSysMgmtACLConfigMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysMgmtACLConfigMask.setStatus("current")


class _AtiStkSwSysMgmtACLConfigApplication_Type(Bits):
    """Custom type atiStkSwSysMgmtACLConfigApplication based on Bits"""
    namedValues = NamedValues(
        *(("telnet", 0),
          ("web", 1),
          ("ping", 2))
    )

_AtiStkSwSysMgmtACLConfigApplication_Type.__name__ = "Bits"
_AtiStkSwSysMgmtACLConfigApplication_Object = MibTableColumn
atiStkSwSysMgmtACLConfigApplication = _AtiStkSwSysMgmtACLConfigApplication_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7, 2, 1, 5),
    _AtiStkSwSysMgmtACLConfigApplication_Type()
)
atiStkSwSysMgmtACLConfigApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysMgmtACLConfigApplication.setStatus("current")
_AtiStkSwSysMgmtACLConfigRowStatus_Type = RowStatus
_AtiStkSwSysMgmtACLConfigRowStatus_Object = MibTableColumn
atiStkSwSysMgmtACLConfigRowStatus = _AtiStkSwSysMgmtACLConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 1, 7, 2, 1, 6),
    _AtiStkSwSysMgmtACLConfigRowStatus_Type()
)
atiStkSwSysMgmtACLConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwSysMgmtACLConfigRowStatus.setStatus("current")
_AtiStkSwPortGroup_ObjectIdentity = ObjectIdentity
atiStkSwPortGroup = _AtiStkSwPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2)
)
_AtiStkSwPortConfigTable_Object = MibTable
atiStkSwPortConfigTable = _AtiStkSwPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1)
)
if mibBuilder.loadTexts:
    atiStkSwPortConfigTable.setStatus("current")
_AtiStkSwPortConfigEntry_Object = MibTableRow
atiStkSwPortConfigEntry = _AtiStkSwPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1)
)
atiStkSwPortConfigEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwPortConfigEntry.setStatus("current")


class _AtiStkSwModuleId_Type(Integer32):
    """Custom type atiStkSwModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwModuleId_Type.__name__ = "Integer32"
_AtiStkSwModuleId_Object = MibTableColumn
atiStkSwModuleId = _AtiStkSwModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 1),
    _AtiStkSwModuleId_Type()
)
atiStkSwModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwModuleId.setStatus("current")


class _AtiStkSwPortId_Type(Integer32):
    """Custom type atiStkSwPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AtiStkSwPortId_Type.__name__ = "Integer32"
_AtiStkSwPortId_Object = MibTableColumn
atiStkSwPortId = _AtiStkSwPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 2),
    _AtiStkSwPortId_Type()
)
atiStkSwPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortId.setStatus("current")


class _AtiStkSwPortName_Type(DisplayString):
    """Custom type atiStkSwPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AtiStkSwPortName_Type.__name__ = "DisplayString"
_AtiStkSwPortName_Object = MibTableColumn
atiStkSwPortName = _AtiStkSwPortName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 3),
    _AtiStkSwPortName_Type()
)
atiStkSwPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortName.setStatus("current")


class _AtiStkSwPortState_Type(Integer32):
    """Custom type atiStkSwPortState based on Integer32"""
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


_AtiStkSwPortState_Type.__name__ = "Integer32"
_AtiStkSwPortState_Object = MibTableColumn
atiStkSwPortState = _AtiStkSwPortState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 4),
    _AtiStkSwPortState_Type()
)
atiStkSwPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortState.setStatus("current")


class _AtiStkSwPortLinkState_Type(Integer32):
    """Custom type atiStkSwPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_AtiStkSwPortLinkState_Type.__name__ = "Integer32"
_AtiStkSwPortLinkState_Object = MibTableColumn
atiStkSwPortLinkState = _AtiStkSwPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 5),
    _AtiStkSwPortLinkState_Type()
)
atiStkSwPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortLinkState.setStatus("current")


class _AtiStkSwPortNegotiation_Type(Integer32):
    """Custom type atiStkSwPortNegotiation based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("autosense", 1),
          ("forceHalfDuplex-10M", 2),
          ("forceHalfDuplex-100M", 3),
          ("forceHalfDuplex-1G", 4),
          ("forceFullDuplex-10M", 5),
          ("forceFullDuplex-100M", 6),
          ("forceFullDuplex-1G", 7),
          ("autoHalfDuplex-10M", 8),
          ("autoHalfDuplex-100M", 9),
          ("autoFullDuplex-10M", 10),
          ("autoFullDuplex-100M", 11))
    )


_AtiStkSwPortNegotiation_Type.__name__ = "Integer32"
_AtiStkSwPortNegotiation_Object = MibTableColumn
atiStkSwPortNegotiation = _AtiStkSwPortNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 6),
    _AtiStkSwPortNegotiation_Type()
)
atiStkSwPortNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortNegotiation.setStatus("current")


class _AtiStkSwPortSpeed_Type(Integer32):
    """Custom type atiStkSwPortSpeed based on Integer32"""
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
        *(("unknown", 1),
          ("speed-10M", 2),
          ("speed-100M", 3),
          ("speed-1G", 4))
    )


_AtiStkSwPortSpeed_Type.__name__ = "Integer32"
_AtiStkSwPortSpeed_Object = MibTableColumn
atiStkSwPortSpeed = _AtiStkSwPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 7),
    _AtiStkSwPortSpeed_Type()
)
atiStkSwPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortSpeed.setStatus("current")


class _AtiStkSwPortDuplexStatus_Type(Integer32):
    """Custom type atiStkSwPortDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("halfDuplex", 2),
          ("fullDuplex", 3))
    )


_AtiStkSwPortDuplexStatus_Type.__name__ = "Integer32"
_AtiStkSwPortDuplexStatus_Object = MibTableColumn
atiStkSwPortDuplexStatus = _AtiStkSwPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 8),
    _AtiStkSwPortDuplexStatus_Type()
)
atiStkSwPortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortDuplexStatus.setStatus("current")


class _AtiStkSwPortFlowControl_Type(Integer32):
    """Custom type atiStkSwPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disable", 2),
          ("enable", 3))
    )


_AtiStkSwPortFlowControl_Type.__name__ = "Integer32"
_AtiStkSwPortFlowControl_Object = MibTableColumn
atiStkSwPortFlowControl = _AtiStkSwPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 9),
    _AtiStkSwPortFlowControl_Type()
)
atiStkSwPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortFlowControl.setStatus("current")


class _AtiStkSwPortBackPressure_Type(Integer32):
    """Custom type atiStkSwPortBackPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disable", 2),
          ("enable", 3))
    )


_AtiStkSwPortBackPressure_Type.__name__ = "Integer32"
_AtiStkSwPortBackPressure_Object = MibTableColumn
atiStkSwPortBackPressure = _AtiStkSwPortBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 10),
    _AtiStkSwPortBackPressure_Type()
)
atiStkSwPortBackPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortBackPressure.setStatus("current")


class _AtiStkSwPortPriority_Type(Integer32):
    """Custom type atiStkSwPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("use-vlan-priority", 1),
          ("override-and-use-low-priority", 2),
          ("override-and-use-high-priority", 3))
    )


_AtiStkSwPortPriority_Type.__name__ = "Integer32"
_AtiStkSwPortPriority_Object = MibTableColumn
atiStkSwPortPriority = _AtiStkSwPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 11),
    _AtiStkSwPortPriority_Type()
)
atiStkSwPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortPriority.setStatus("current")


class _AtiStkSwPortBroadcastProcessing_Type(Integer32):
    """Custom type atiStkSwPortBroadcastProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard-broadcasts", 1),
          ("do-not-discard-broadcasts", 2))
    )


_AtiStkSwPortBroadcastProcessing_Type.__name__ = "Integer32"
_AtiStkSwPortBroadcastProcessing_Object = MibTableColumn
atiStkSwPortBroadcastProcessing = _AtiStkSwPortBroadcastProcessing_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 12),
    _AtiStkSwPortBroadcastProcessing_Type()
)
atiStkSwPortBroadcastProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortBroadcastProcessing.setStatus("current")


class _AtiStkSwPortMDIO_Type(Integer32):
    """Custom type atiStkSwPortMDIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2),
          ("auto-mdix", 3))
    )


_AtiStkSwPortMDIO_Type.__name__ = "Integer32"
_AtiStkSwPortMDIO_Object = MibTableColumn
atiStkSwPortMDIO = _AtiStkSwPortMDIO_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 13),
    _AtiStkSwPortMDIO_Type()
)
atiStkSwPortMDIO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortMDIO.setStatus("current")


class _AtiStkSwPortHOLLimit_Type(Integer32):
    """Custom type atiStkSwPortHOLLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_AtiStkSwPortHOLLimit_Type.__name__ = "Integer32"
_AtiStkSwPortHOLLimit_Object = MibTableColumn
atiStkSwPortHOLLimit = _AtiStkSwPortHOLLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 14),
    _AtiStkSwPortHOLLimit_Type()
)
atiStkSwPortHOLLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortHOLLimit.setStatus("current")


class _AtiStkSwPortBackPressureLimit_Type(Integer32):
    """Custom type atiStkSwPortBackPressureLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 57344),
    )


_AtiStkSwPortBackPressureLimit_Type.__name__ = "Integer32"
_AtiStkSwPortBackPressureLimit_Object = MibTableColumn
atiStkSwPortBackPressureLimit = _AtiStkSwPortBackPressureLimit_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 15),
    _AtiStkSwPortBackPressureLimit_Type()
)
atiStkSwPortBackPressureLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortBackPressureLimit.setStatus("current")


class _AtiStkSwPortSTPState_Type(Integer32):
    """Custom type atiStkSwPortSTPState based on Integer32"""
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
        *(("unknown", 1),
          ("disabled", 2),
          ("blocking", 3),
          ("listening", 4),
          ("learning", 5),
          ("forwarding", 6))
    )


_AtiStkSwPortSTPState_Type.__name__ = "Integer32"
_AtiStkSwPortSTPState_Object = MibTableColumn
atiStkSwPortSTPState = _AtiStkSwPortSTPState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 1, 1, 16),
    _AtiStkSwPortSTPState_Type()
)
atiStkSwPortSTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortSTPState.setStatus("current")
_AtiStkSwPortMirroringConfig_ObjectIdentity = ObjectIdentity
atiStkSwPortMirroringConfig = _AtiStkSwPortMirroringConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 2)
)


class _AtiStkSwPortMirroringState_Type(Integer32):
    """Custom type atiStkSwPortMirroringState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("l2-enabled", 2))
    )


_AtiStkSwPortMirroringState_Type.__name__ = "Integer32"
_AtiStkSwPortMirroringState_Object = MibScalar
atiStkSwPortMirroringState = _AtiStkSwPortMirroringState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 2, 1),
    _AtiStkSwPortMirroringState_Type()
)
atiStkSwPortMirroringState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortMirroringState.setStatus("current")


class _AtiStkSwPortMirroringSourceModuleId_Type(Integer32):
    """Custom type atiStkSwPortMirroringSourceModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwPortMirroringSourceModuleId_Type.__name__ = "Integer32"
_AtiStkSwPortMirroringSourceModuleId_Object = MibScalar
atiStkSwPortMirroringSourceModuleId = _AtiStkSwPortMirroringSourceModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 2, 2),
    _AtiStkSwPortMirroringSourceModuleId_Type()
)
atiStkSwPortMirroringSourceModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortMirroringSourceModuleId.setStatus("current")
_AtiStkSwPortMirroringSourcePortId_Type = Integer32
_AtiStkSwPortMirroringSourcePortId_Object = MibScalar
atiStkSwPortMirroringSourcePortId = _AtiStkSwPortMirroringSourcePortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 2, 3),
    _AtiStkSwPortMirroringSourcePortId_Type()
)
atiStkSwPortMirroringSourcePortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortMirroringSourcePortId.setStatus("current")


class _AtiStkSwPortMirroringDestinationModuleId_Type(Integer32):
    """Custom type atiStkSwPortMirroringDestinationModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwPortMirroringDestinationModuleId_Type.__name__ = "Integer32"
_AtiStkSwPortMirroringDestinationModuleId_Object = MibScalar
atiStkSwPortMirroringDestinationModuleId = _AtiStkSwPortMirroringDestinationModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 2, 4),
    _AtiStkSwPortMirroringDestinationModuleId_Type()
)
atiStkSwPortMirroringDestinationModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortMirroringDestinationModuleId.setStatus("current")
_AtiStkSwPortMirroringDestinationPortId_Type = Integer32
_AtiStkSwPortMirroringDestinationPortId_Object = MibScalar
atiStkSwPortMirroringDestinationPortId = _AtiStkSwPortMirroringDestinationPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 2, 5),
    _AtiStkSwPortMirroringDestinationPortId_Type()
)
atiStkSwPortMirroringDestinationPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortMirroringDestinationPortId.setStatus("current")
_AtiStkSwPortMirroringSourceRxList_Type = DisplayString
_AtiStkSwPortMirroringSourceRxList_Object = MibScalar
atiStkSwPortMirroringSourceRxList = _AtiStkSwPortMirroringSourceRxList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 2, 6),
    _AtiStkSwPortMirroringSourceRxList_Type()
)
atiStkSwPortMirroringSourceRxList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortMirroringSourceRxList.setStatus("current")
_AtiStkSwPortMirroringSourceTxList_Type = DisplayString
_AtiStkSwPortMirroringSourceTxList_Object = MibScalar
atiStkSwPortMirroringSourceTxList = _AtiStkSwPortMirroringSourceTxList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 2, 7),
    _AtiStkSwPortMirroringSourceTxList_Type()
)
atiStkSwPortMirroringSourceTxList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortMirroringSourceTxList.setStatus("current")
_AtiStkSwPortSecurityConfig_ObjectIdentity = ObjectIdentity
atiStkSwPortSecurityConfig = _AtiStkSwPortSecurityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 3)
)


class _AtiStkSwPortSecurityMode_Type(Integer32):
    """Custom type atiStkSwPortSecurityMode based on Integer32"""
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
        *(("automatic", 1),
          ("limited", 2),
          ("secured", 3),
          ("locked", 4))
    )


_AtiStkSwPortSecurityMode_Type.__name__ = "Integer32"
_AtiStkSwPortSecurityMode_Object = MibScalar
atiStkSwPortSecurityMode = _AtiStkSwPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 3, 1),
    _AtiStkSwPortSecurityMode_Type()
)
atiStkSwPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortSecurityMode.setStatus("current")
_AtiStkSwPortIntrusionDetectionTable_Object = MibTable
atiStkSwPortIntrusionDetectionTable = _AtiStkSwPortIntrusionDetectionTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 4)
)
if mibBuilder.loadTexts:
    atiStkSwPortIntrusionDetectionTable.setStatus("current")
_AtiStkSwPortIntrusionDetectionEntry_Object = MibTableRow
atiStkSwPortIntrusionDetectionEntry = _AtiStkSwPortIntrusionDetectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 4, 1)
)
atiStkSwPortIntrusionDetectionEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
)
if mibBuilder.loadTexts:
    atiStkSwPortIntrusionDetectionEntry.setStatus("current")


class _AtiStkSwPortIntrusionDetectionAction_Type(Integer32):
    """Custom type atiStkSwPortIntrusionDetectionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-nothing", 1),
          ("send-trap-only", 2),
          ("disable-port-and-send-trap", 3))
    )


_AtiStkSwPortIntrusionDetectionAction_Type.__name__ = "Integer32"
_AtiStkSwPortIntrusionDetectionAction_Object = MibTableColumn
atiStkSwPortIntrusionDetectionAction = _AtiStkSwPortIntrusionDetectionAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 4, 1, 1),
    _AtiStkSwPortIntrusionDetectionAction_Type()
)
atiStkSwPortIntrusionDetectionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortIntrusionDetectionAction.setStatus("current")
_AtiStkSwPortIntrusionDetectionPortList_Type = DisplayString
_AtiStkSwPortIntrusionDetectionPortList_Object = MibTableColumn
atiStkSwPortIntrusionDetectionPortList = _AtiStkSwPortIntrusionDetectionPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 4, 1, 2),
    _AtiStkSwPortIntrusionDetectionPortList_Type()
)
atiStkSwPortIntrusionDetectionPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortIntrusionDetectionPortList.setStatus("current")
_AtiStkPortSecurityConfigTable_Object = MibTable
atiStkPortSecurityConfigTable = _AtiStkPortSecurityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 5)
)
if mibBuilder.loadTexts:
    atiStkPortSecurityConfigTable.setStatus("current")
_AtiStkPortSecurityConfigEntry_Object = MibTableRow
atiStkPortSecurityConfigEntry = _AtiStkPortSecurityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 5, 1)
)
atiStkPortSecurityConfigEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortId"),
)
if mibBuilder.loadTexts:
    atiStkPortSecurityConfigEntry.setStatus("current")


class _AtiStkPortSecurityMode_Type(Integer32):
    """Custom type atiStkPortSecurityMode based on Integer32"""
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
        *(("automatic", 1),
          ("limited", 2),
          ("secured", 3),
          ("locked", 4))
    )


_AtiStkPortSecurityMode_Type.__name__ = "Integer32"
_AtiStkPortSecurityMode_Object = MibTableColumn
atiStkPortSecurityMode = _AtiStkPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 5, 1, 1),
    _AtiStkPortSecurityMode_Type()
)
atiStkPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkPortSecurityMode.setStatus("current")


class _AtiStkPortSecurityThreshold_Type(Integer32):
    """Custom type atiStkPortSecurityThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AtiStkPortSecurityThreshold_Type.__name__ = "Integer32"
_AtiStkPortSecurityThreshold_Object = MibTableColumn
atiStkPortSecurityThreshold = _AtiStkPortSecurityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 5, 1, 2),
    _AtiStkPortSecurityThreshold_Type()
)
atiStkPortSecurityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkPortSecurityThreshold.setStatus("current")


class _AtiStkPortIntrusionAction_Type(Integer32):
    """Custom type atiStkPortIntrusionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("send-trap", 2),
          ("disable-port", 3))
    )


_AtiStkPortIntrusionAction_Type.__name__ = "Integer32"
_AtiStkPortIntrusionAction_Object = MibTableColumn
atiStkPortIntrusionAction = _AtiStkPortIntrusionAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 5, 1, 3),
    _AtiStkPortIntrusionAction_Type()
)
atiStkPortIntrusionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkPortIntrusionAction.setStatus("current")


class _AtiStkPortIntrusionActionStatus_Type(Integer32):
    """Custom type atiStkPortIntrusionActionStatus based on Integer32"""
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


_AtiStkPortIntrusionActionStatus_Type.__name__ = "Integer32"
_AtiStkPortIntrusionActionStatus_Object = MibTableColumn
atiStkPortIntrusionActionStatus = _AtiStkPortIntrusionActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 5, 1, 4),
    _AtiStkPortIntrusionActionStatus_Type()
)
atiStkPortIntrusionActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkPortIntrusionActionStatus.setStatus("current")
_AtiStkDOSConfig_ObjectIdentity = ObjectIdentity
atiStkDOSConfig = _AtiStkDOSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 6)
)
_AtiStkDOSConfigLANIpAddress_Type = IpAddress
_AtiStkDOSConfigLANIpAddress_Object = MibScalar
atiStkDOSConfigLANIpAddress = _AtiStkDOSConfigLANIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 6, 1),
    _AtiStkDOSConfigLANIpAddress_Type()
)
atiStkDOSConfigLANIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkDOSConfigLANIpAddress.setStatus("current")
_AtiStkDOSConfigLANSubnetMask_Type = IpAddress
_AtiStkDOSConfigLANSubnetMask_Object = MibScalar
atiStkDOSConfigLANSubnetMask = _AtiStkDOSConfigLANSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 6, 2),
    _AtiStkDOSConfigLANSubnetMask_Type()
)
atiStkDOSConfigLANSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkDOSConfigLANSubnetMask.setStatus("current")
_AtiStkPortDOSAttackConfigTable_Object = MibTable
atiStkPortDOSAttackConfigTable = _AtiStkPortDOSAttackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 6, 3)
)
if mibBuilder.loadTexts:
    atiStkPortDOSAttackConfigTable.setStatus("current")
_AtiStkPortDOSAttackConfigEntry_Object = MibTableRow
atiStkPortDOSAttackConfigEntry = _AtiStkPortDOSAttackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 6, 3, 1)
)
atiStkPortDOSAttackConfigEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortDOSAttackType"),
)
if mibBuilder.loadTexts:
    atiStkPortDOSAttackConfigEntry.setStatus("current")


class _AtiStkSwPortDOSAttackType_Type(Integer32):
    """Custom type atiStkSwPortDOSAttackType based on Integer32"""
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
        *(("syn-flood", 1),
          ("smurf", 2),
          ("land", 3),
          ("ip-option", 4),
          ("teardrop", 5),
          ("ping-of-death", 6))
    )


_AtiStkSwPortDOSAttackType_Type.__name__ = "Integer32"
_AtiStkSwPortDOSAttackType_Object = MibTableColumn
atiStkSwPortDOSAttackType = _AtiStkSwPortDOSAttackType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 6, 3, 1, 1),
    _AtiStkSwPortDOSAttackType_Type()
)
atiStkSwPortDOSAttackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortDOSAttackType.setStatus("current")


class _AtiStkSwPortDOSAttackActionStatus_Type(Integer32):
    """Custom type atiStkSwPortDOSAttackActionStatus based on Integer32"""
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


_AtiStkSwPortDOSAttackActionStatus_Type.__name__ = "Integer32"
_AtiStkSwPortDOSAttackActionStatus_Object = MibTableColumn
atiStkSwPortDOSAttackActionStatus = _AtiStkSwPortDOSAttackActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 6, 3, 1, 2),
    _AtiStkSwPortDOSAttackActionStatus_Type()
)
atiStkSwPortDOSAttackActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortDOSAttackActionStatus.setStatus("current")
_AtiStkSwPortDOSAttackMirrorPort_Type = Integer32
_AtiStkSwPortDOSAttackMirrorPort_Object = MibTableColumn
atiStkSwPortDOSAttackMirrorPort = _AtiStkSwPortDOSAttackMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 6, 3, 1, 3),
    _AtiStkSwPortDOSAttackMirrorPort_Type()
)
atiStkSwPortDOSAttackMirrorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortDOSAttackMirrorPort.setStatus("obsolete")


class _AtiStkSwPortDOSAttackMirrorPortStatus_Type(Integer32):
    """Custom type atiStkSwPortDOSAttackMirrorPortStatus based on Integer32"""
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


_AtiStkSwPortDOSAttackMirrorPortStatus_Type.__name__ = "Integer32"
_AtiStkSwPortDOSAttackMirrorPortStatus_Object = MibTableColumn
atiStkSwPortDOSAttackMirrorPortStatus = _AtiStkSwPortDOSAttackMirrorPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 6, 3, 1, 4),
    _AtiStkSwPortDOSAttackMirrorPortStatus_Type()
)
atiStkSwPortDOSAttackMirrorPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwPortDOSAttackMirrorPortStatus.setStatus("current")
_AtiStkSwIntrusionAttackTable_Object = MibTable
atiStkSwIntrusionAttackTable = _AtiStkSwIntrusionAttackTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 7)
)
if mibBuilder.loadTexts:
    atiStkSwIntrusionAttackTable.setStatus("current")
_AtiStkSwIntrusionAttackEntry_Object = MibTableRow
atiStkSwIntrusionAttackEntry = _AtiStkSwIntrusionAttackEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 7, 1)
)
atiStkSwIntrusionAttackEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwIntrusionAttackEntry.setStatus("current")
_AtiStkSwIntruderAttackVlanId_Type = Integer32
_AtiStkSwIntruderAttackVlanId_Object = MibTableColumn
atiStkSwIntruderAttackVlanId = _AtiStkSwIntruderAttackVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 7, 1, 1),
    _AtiStkSwIntruderAttackVlanId_Type()
)
atiStkSwIntruderAttackVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwIntruderAttackVlanId.setStatus("current")
_AtiStkSwIntruderAttackMacAddr_Type = MacAddress
_AtiStkSwIntruderAttackMacAddr_Object = MibTableColumn
atiStkSwIntruderAttackMacAddr = _AtiStkSwIntruderAttackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 7, 1, 2),
    _AtiStkSwIntruderAttackMacAddr_Type()
)
atiStkSwIntruderAttackMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwIntruderAttackMacAddr.setStatus("current")
_AtiStkSwPortStormDetectCurrentTable_Object = MibTable
atiStkSwPortStormDetectCurrentTable = _AtiStkSwPortStormDetectCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 8)
)
if mibBuilder.loadTexts:
    atiStkSwPortStormDetectCurrentTable.setStatus("current")
_AtiStkSwPortStormDetectCurrentEntry_Object = MibTableRow
atiStkSwPortStormDetectCurrentEntry = _AtiStkSwPortStormDetectCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 8, 1)
)
atiStkSwPortStormDetectCurrentEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwPortStormDetectCurrentEntry.setStatus("current")


class _AtiStkSwPortStormDetectCurrentHighStatus_Type(Integer32):
    """Custom type atiStkSwPortStormDetectCurrentHighStatus based on Integer32"""
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
        *(("inactive", 1),
          ("normal", 2),
          ("detected", 3),
          ("blocking", 4))
    )


_AtiStkSwPortStormDetectCurrentHighStatus_Type.__name__ = "Integer32"
_AtiStkSwPortStormDetectCurrentHighStatus_Object = MibTableColumn
atiStkSwPortStormDetectCurrentHighStatus = _AtiStkSwPortStormDetectCurrentHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 8, 1, 1),
    _AtiStkSwPortStormDetectCurrentHighStatus_Type()
)
atiStkSwPortStormDetectCurrentHighStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortStormDetectCurrentHighStatus.setStatus("current")


class _AtiStkSwPortStormDetectCurrentHighAction_Type(Integer32):
    """Custom type atiStkSwPortStormDetectCurrentHighAction based on Integer32"""
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
        *(("unknown", 1),
          ("none", 2),
          ("port-disabled", 3),
          ("linkdown", 4),
          ("broadcast-discard", 5))
    )


_AtiStkSwPortStormDetectCurrentHighAction_Type.__name__ = "Integer32"
_AtiStkSwPortStormDetectCurrentHighAction_Object = MibTableColumn
atiStkSwPortStormDetectCurrentHighAction = _AtiStkSwPortStormDetectCurrentHighAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 8, 1, 2),
    _AtiStkSwPortStormDetectCurrentHighAction_Type()
)
atiStkSwPortStormDetectCurrentHighAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortStormDetectCurrentHighAction.setStatus("current")
_AtiStkSwPortStormDetectCurrentHighExpiry_Type = Integer32
_AtiStkSwPortStormDetectCurrentHighExpiry_Object = MibTableColumn
atiStkSwPortStormDetectCurrentHighExpiry = _AtiStkSwPortStormDetectCurrentHighExpiry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 8, 1, 3),
    _AtiStkSwPortStormDetectCurrentHighExpiry_Type()
)
atiStkSwPortStormDetectCurrentHighExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortStormDetectCurrentHighExpiry.setStatus("current")


class _AtiStkSwPortStormDetectCurrentLowStatus_Type(Integer32):
    """Custom type atiStkSwPortStormDetectCurrentLowStatus based on Integer32"""
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
        *(("inactive", 1),
          ("normal", 2),
          ("detected", 3),
          ("blocking", 4))
    )


_AtiStkSwPortStormDetectCurrentLowStatus_Type.__name__ = "Integer32"
_AtiStkSwPortStormDetectCurrentLowStatus_Object = MibTableColumn
atiStkSwPortStormDetectCurrentLowStatus = _AtiStkSwPortStormDetectCurrentLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 8, 1, 4),
    _AtiStkSwPortStormDetectCurrentLowStatus_Type()
)
atiStkSwPortStormDetectCurrentLowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortStormDetectCurrentLowStatus.setStatus("current")


class _AtiStkSwPortStormDetectCurrentLowAction_Type(Integer32):
    """Custom type atiStkSwPortStormDetectCurrentLowAction based on Integer32"""
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
        *(("unknown", 1),
          ("none", 2),
          ("port-disabled", 3),
          ("linkdown", 4),
          ("broadcast-discard", 5))
    )


_AtiStkSwPortStormDetectCurrentLowAction_Type.__name__ = "Integer32"
_AtiStkSwPortStormDetectCurrentLowAction_Object = MibTableColumn
atiStkSwPortStormDetectCurrentLowAction = _AtiStkSwPortStormDetectCurrentLowAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 8, 1, 5),
    _AtiStkSwPortStormDetectCurrentLowAction_Type()
)
atiStkSwPortStormDetectCurrentLowAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortStormDetectCurrentLowAction.setStatus("current")
_AtiStkSwPortStormDetectCurrentLowExpiry_Type = Integer32
_AtiStkSwPortStormDetectCurrentLowExpiry_Object = MibTableColumn
atiStkSwPortStormDetectCurrentLowExpiry = _AtiStkSwPortStormDetectCurrentLowExpiry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 8, 1, 6),
    _AtiStkSwPortStormDetectCurrentLowExpiry_Type()
)
atiStkSwPortStormDetectCurrentLowExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortStormDetectCurrentLowExpiry.setStatus("current")
_AtiStkSwPortLoopDetectCurrentTable_Object = MibTable
atiStkSwPortLoopDetectCurrentTable = _AtiStkSwPortLoopDetectCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 9)
)
if mibBuilder.loadTexts:
    atiStkSwPortLoopDetectCurrentTable.setStatus("current")
_AtiStkSwPortLoopDetectCurrentEntry_Object = MibTableRow
atiStkSwPortLoopDetectCurrentEntry = _AtiStkSwPortLoopDetectCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 9, 1)
)
atiStkSwPortLoopDetectCurrentEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwPortLoopDetectCurrentEntry.setStatus("current")


class _AtiStkSwPortLoopDetectCurrentStatus_Type(Integer32):
    """Custom type atiStkSwPortLoopDetectCurrentStatus based on Integer32"""
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
        *(("inactive", 1),
          ("normal", 2),
          ("detected", 3),
          ("blocking", 4))
    )


_AtiStkSwPortLoopDetectCurrentStatus_Type.__name__ = "Integer32"
_AtiStkSwPortLoopDetectCurrentStatus_Object = MibTableColumn
atiStkSwPortLoopDetectCurrentStatus = _AtiStkSwPortLoopDetectCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 9, 1, 1),
    _AtiStkSwPortLoopDetectCurrentStatus_Type()
)
atiStkSwPortLoopDetectCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortLoopDetectCurrentStatus.setStatus("current")


class _AtiStkSwPortLoopDetectCurrentAction_Type(Integer32):
    """Custom type atiStkSwPortLoopDetectCurrentAction based on Integer32"""
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
        *(("unknown", 1),
          ("none", 2),
          ("port-disabled", 3),
          ("linkdown", 4),
          ("broadcast-discard", 5))
    )


_AtiStkSwPortLoopDetectCurrentAction_Type.__name__ = "Integer32"
_AtiStkSwPortLoopDetectCurrentAction_Object = MibTableColumn
atiStkSwPortLoopDetectCurrentAction = _AtiStkSwPortLoopDetectCurrentAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 9, 1, 2),
    _AtiStkSwPortLoopDetectCurrentAction_Type()
)
atiStkSwPortLoopDetectCurrentAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortLoopDetectCurrentAction.setStatus("current")
_AtiStkSwPortLoopDetectCurrentExpiry_Type = Integer32
_AtiStkSwPortLoopDetectCurrentExpiry_Object = MibTableColumn
atiStkSwPortLoopDetectCurrentExpiry = _AtiStkSwPortLoopDetectCurrentExpiry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 9, 1, 3),
    _AtiStkSwPortLoopDetectCurrentExpiry_Type()
)
atiStkSwPortLoopDetectCurrentExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortLoopDetectCurrentExpiry.setStatus("current")
_AtiStkSwPortLoopDetectCurrentVlanId_Type = Integer32
_AtiStkSwPortLoopDetectCurrentVlanId_Object = MibTableColumn
atiStkSwPortLoopDetectCurrentVlanId = _AtiStkSwPortLoopDetectCurrentVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 2, 9, 1, 4),
    _AtiStkSwPortLoopDetectCurrentVlanId_Type()
)
atiStkSwPortLoopDetectCurrentVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortLoopDetectCurrentVlanId.setStatus("current")
_AtiStkSwVlanGroup_ObjectIdentity = ObjectIdentity
atiStkSwVlanGroup = _AtiStkSwVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3)
)
_AtiStkSwVlanConfigTable_Object = MibTable
atiStkSwVlanConfigTable = _AtiStkSwVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1)
)
if mibBuilder.loadTexts:
    atiStkSwVlanConfigTable.setStatus("current")
_AtiStkSwVlanConfigEntry_Object = MibTableRow
atiStkSwVlanConfigEntry = _AtiStkSwVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1)
)
atiStkSwVlanConfigEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwVlanId"),
)
if mibBuilder.loadTexts:
    atiStkSwVlanConfigEntry.setStatus("current")


class _AtiStkSwVlanId_Type(Integer32):
    """Custom type atiStkSwVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AtiStkSwVlanId_Type.__name__ = "Integer32"
_AtiStkSwVlanId_Object = MibTableColumn
atiStkSwVlanId = _AtiStkSwVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 1),
    _AtiStkSwVlanId_Type()
)
atiStkSwVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwVlanId.setStatus("current")


class _AtiStkSwVlanName_Type(DisplayString):
    """Custom type atiStkSwVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AtiStkSwVlanName_Type.__name__ = "DisplayString"
_AtiStkSwVlanName_Object = MibTableColumn
atiStkSwVlanName = _AtiStkSwVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 2),
    _AtiStkSwVlanName_Type()
)
atiStkSwVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanName.setStatus("current")
_AtiStkSwVlanTaggedPortListModule1_Type = DisplayString
_AtiStkSwVlanTaggedPortListModule1_Object = MibTableColumn
atiStkSwVlanTaggedPortListModule1 = _AtiStkSwVlanTaggedPortListModule1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 3),
    _AtiStkSwVlanTaggedPortListModule1_Type()
)
atiStkSwVlanTaggedPortListModule1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanTaggedPortListModule1.setStatus("current")
_AtiStkSwVlanUntaggedPortListModule1_Type = DisplayString
_AtiStkSwVlanUntaggedPortListModule1_Object = MibTableColumn
atiStkSwVlanUntaggedPortListModule1 = _AtiStkSwVlanUntaggedPortListModule1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 4),
    _AtiStkSwVlanUntaggedPortListModule1_Type()
)
atiStkSwVlanUntaggedPortListModule1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanUntaggedPortListModule1.setStatus("current")
_AtiStkSwVlanTaggedPortListModule2_Type = DisplayString
_AtiStkSwVlanTaggedPortListModule2_Object = MibTableColumn
atiStkSwVlanTaggedPortListModule2 = _AtiStkSwVlanTaggedPortListModule2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 5),
    _AtiStkSwVlanTaggedPortListModule2_Type()
)
atiStkSwVlanTaggedPortListModule2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanTaggedPortListModule2.setStatus("current")
_AtiStkSwVlanUntaggedPortListModule2_Type = DisplayString
_AtiStkSwVlanUntaggedPortListModule2_Object = MibTableColumn
atiStkSwVlanUntaggedPortListModule2 = _AtiStkSwVlanUntaggedPortListModule2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 6),
    _AtiStkSwVlanUntaggedPortListModule2_Type()
)
atiStkSwVlanUntaggedPortListModule2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanUntaggedPortListModule2.setStatus("current")
_AtiStkSwVlanTaggedPortListModule3_Type = DisplayString
_AtiStkSwVlanTaggedPortListModule3_Object = MibTableColumn
atiStkSwVlanTaggedPortListModule3 = _AtiStkSwVlanTaggedPortListModule3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 7),
    _AtiStkSwVlanTaggedPortListModule3_Type()
)
atiStkSwVlanTaggedPortListModule3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanTaggedPortListModule3.setStatus("current")
_AtiStkSwVlanUntaggedPortListModule3_Type = DisplayString
_AtiStkSwVlanUntaggedPortListModule3_Object = MibTableColumn
atiStkSwVlanUntaggedPortListModule3 = _AtiStkSwVlanUntaggedPortListModule3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 8),
    _AtiStkSwVlanUntaggedPortListModule3_Type()
)
atiStkSwVlanUntaggedPortListModule3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanUntaggedPortListModule3.setStatus("current")
_AtiStkSwVlanTaggedPortListModule4_Type = DisplayString
_AtiStkSwVlanTaggedPortListModule4_Object = MibTableColumn
atiStkSwVlanTaggedPortListModule4 = _AtiStkSwVlanTaggedPortListModule4_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 9),
    _AtiStkSwVlanTaggedPortListModule4_Type()
)
atiStkSwVlanTaggedPortListModule4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanTaggedPortListModule4.setStatus("current")
_AtiStkSwVlanUntaggedPortListModule4_Type = DisplayString
_AtiStkSwVlanUntaggedPortListModule4_Object = MibTableColumn
atiStkSwVlanUntaggedPortListModule4 = _AtiStkSwVlanUntaggedPortListModule4_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 10),
    _AtiStkSwVlanUntaggedPortListModule4_Type()
)
atiStkSwVlanUntaggedPortListModule4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanUntaggedPortListModule4.setStatus("current")
_AtiStkSwVlanTaggedPortListModule5_Type = DisplayString
_AtiStkSwVlanTaggedPortListModule5_Object = MibTableColumn
atiStkSwVlanTaggedPortListModule5 = _AtiStkSwVlanTaggedPortListModule5_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 11),
    _AtiStkSwVlanTaggedPortListModule5_Type()
)
atiStkSwVlanTaggedPortListModule5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanTaggedPortListModule5.setStatus("current")
_AtiStkSwVlanUntaggedPortListModule5_Type = DisplayString
_AtiStkSwVlanUntaggedPortListModule5_Object = MibTableColumn
atiStkSwVlanUntaggedPortListModule5 = _AtiStkSwVlanUntaggedPortListModule5_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 12),
    _AtiStkSwVlanUntaggedPortListModule5_Type()
)
atiStkSwVlanUntaggedPortListModule5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanUntaggedPortListModule5.setStatus("current")
_AtiStkSwVlanTaggedPortListModule6_Type = DisplayString
_AtiStkSwVlanTaggedPortListModule6_Object = MibTableColumn
atiStkSwVlanTaggedPortListModule6 = _AtiStkSwVlanTaggedPortListModule6_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 13),
    _AtiStkSwVlanTaggedPortListModule6_Type()
)
atiStkSwVlanTaggedPortListModule6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanTaggedPortListModule6.setStatus("current")
_AtiStkSwVlanUntaggedPortListModule6_Type = DisplayString
_AtiStkSwVlanUntaggedPortListModule6_Object = MibTableColumn
atiStkSwVlanUntaggedPortListModule6 = _AtiStkSwVlanUntaggedPortListModule6_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 14),
    _AtiStkSwVlanUntaggedPortListModule6_Type()
)
atiStkSwVlanUntaggedPortListModule6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanUntaggedPortListModule6.setStatus("current")
_AtiStkSwVlanTaggedPortListModule7_Type = DisplayString
_AtiStkSwVlanTaggedPortListModule7_Object = MibTableColumn
atiStkSwVlanTaggedPortListModule7 = _AtiStkSwVlanTaggedPortListModule7_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 15),
    _AtiStkSwVlanTaggedPortListModule7_Type()
)
atiStkSwVlanTaggedPortListModule7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanTaggedPortListModule7.setStatus("current")
_AtiStkSwVlanUntaggedPortListModule7_Type = DisplayString
_AtiStkSwVlanUntaggedPortListModule7_Object = MibTableColumn
atiStkSwVlanUntaggedPortListModule7 = _AtiStkSwVlanUntaggedPortListModule7_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 16),
    _AtiStkSwVlanUntaggedPortListModule7_Type()
)
atiStkSwVlanUntaggedPortListModule7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanUntaggedPortListModule7.setStatus("current")
_AtiStkSwVlanTaggedPortListModule8_Type = DisplayString
_AtiStkSwVlanTaggedPortListModule8_Object = MibTableColumn
atiStkSwVlanTaggedPortListModule8 = _AtiStkSwVlanTaggedPortListModule8_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 17),
    _AtiStkSwVlanTaggedPortListModule8_Type()
)
atiStkSwVlanTaggedPortListModule8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanTaggedPortListModule8.setStatus("current")
_AtiStkSwVlanUntaggedPortListModule8_Type = DisplayString
_AtiStkSwVlanUntaggedPortListModule8_Object = MibTableColumn
atiStkSwVlanUntaggedPortListModule8 = _AtiStkSwVlanUntaggedPortListModule8_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 18),
    _AtiStkSwVlanUntaggedPortListModule8_Type()
)
atiStkSwVlanUntaggedPortListModule8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanUntaggedPortListModule8.setStatus("current")
_AtiStkSwVlanConfigEntryStatus_Type = RowStatus
_AtiStkSwVlanConfigEntryStatus_Object = MibTableColumn
atiStkSwVlanConfigEntryStatus = _AtiStkSwVlanConfigEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 19),
    _AtiStkSwVlanConfigEntryStatus_Type()
)
atiStkSwVlanConfigEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiStkSwVlanConfigEntryStatus.setStatus("current")
_AtiStkSwVlanActualUntaggedPortListModule1_Type = DisplayString
_AtiStkSwVlanActualUntaggedPortListModule1_Object = MibTableColumn
atiStkSwVlanActualUntaggedPortListModule1 = _AtiStkSwVlanActualUntaggedPortListModule1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 1, 1, 20),
    _AtiStkSwVlanActualUntaggedPortListModule1_Type()
)
atiStkSwVlanActualUntaggedPortListModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwVlanActualUntaggedPortListModule1.setStatus("current")
_AtiStkSwPort2VlanTable_Object = MibTable
atiStkSwPort2VlanTable = _AtiStkSwPort2VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 2)
)
if mibBuilder.loadTexts:
    atiStkSwPort2VlanTable.setStatus("current")
_AtiStkSwPort2VlanEntry_Object = MibTableRow
atiStkSwPort2VlanEntry = _AtiStkSwPort2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 2, 1)
)
atiStkSwPort2VlanEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwPort2VlanEntry.setStatus("current")
_AtiStkSwPortVlanId_Type = Integer32
_AtiStkSwPortVlanId_Object = MibTableColumn
atiStkSwPortVlanId = _AtiStkSwPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 2, 1, 1),
    _AtiStkSwPortVlanId_Type()
)
atiStkSwPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortVlanId.setStatus("current")


class _AtiStkSwPortVlanName_Type(DisplayString):
    """Custom type atiStkSwPortVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AtiStkSwPortVlanName_Type.__name__ = "DisplayString"
_AtiStkSwPortVlanName_Object = MibTableColumn
atiStkSwPortVlanName = _AtiStkSwPortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 2, 1, 2),
    _AtiStkSwPortVlanName_Type()
)
atiStkSwPortVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwPortVlanName.setStatus("current")
_AtiStkSwMacAddr2VlanTable_Object = MibTable
atiStkSwMacAddr2VlanTable = _AtiStkSwMacAddr2VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 3)
)
if mibBuilder.loadTexts:
    atiStkSwMacAddr2VlanTable.setStatus("current")
_AtiStkSwMacAddr2VlanEntry_Object = MibTableRow
atiStkSwMacAddr2VlanEntry = _AtiStkSwMacAddr2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 3, 1)
)
atiStkSwMacAddr2VlanEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwMacAddress"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwMacAddrVlanId"),
)
if mibBuilder.loadTexts:
    atiStkSwMacAddr2VlanEntry.setStatus("current")
_AtiStkSwMacAddress_Type = MacAddress
_AtiStkSwMacAddress_Object = MibTableColumn
atiStkSwMacAddress = _AtiStkSwMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 3, 1, 1),
    _AtiStkSwMacAddress_Type()
)
atiStkSwMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMacAddress.setStatus("current")


class _AtiStkSwMacAddrVlanId_Type(Integer32):
    """Custom type atiStkSwMacAddrVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AtiStkSwMacAddrVlanId_Type.__name__ = "Integer32"
_AtiStkSwMacAddrVlanId_Object = MibTableColumn
atiStkSwMacAddrVlanId = _AtiStkSwMacAddrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 3, 1, 2),
    _AtiStkSwMacAddrVlanId_Type()
)
atiStkSwMacAddrVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMacAddrVlanId.setStatus("current")


class _AtiStkSwMacAddrVlanName_Type(DisplayString):
    """Custom type atiStkSwMacAddrVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AtiStkSwMacAddrVlanName_Type.__name__ = "DisplayString"
_AtiStkSwMacAddrVlanName_Object = MibTableColumn
atiStkSwMacAddrVlanName = _AtiStkSwMacAddrVlanName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 3, 1, 3),
    _AtiStkSwMacAddrVlanName_Type()
)
atiStkSwMacAddrVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMacAddrVlanName.setStatus("current")


class _AtiStkSwMacAddrModuleId_Type(Integer32):
    """Custom type atiStkSwMacAddrModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwMacAddrModuleId_Type.__name__ = "Integer32"
_AtiStkSwMacAddrModuleId_Object = MibTableColumn
atiStkSwMacAddrModuleId = _AtiStkSwMacAddrModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 3, 1, 4),
    _AtiStkSwMacAddrModuleId_Type()
)
atiStkSwMacAddrModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMacAddrModuleId.setStatus("current")
_AtiStkSwMacAddrPortId_Type = Integer32
_AtiStkSwMacAddrPortId_Object = MibTableColumn
atiStkSwMacAddrPortId = _AtiStkSwMacAddrPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 3, 1, 5),
    _AtiStkSwMacAddrPortId_Type()
)
atiStkSwMacAddrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMacAddrPortId.setStatus("current")


class _AtiStkSwMacAddrPortList_Type(DisplayString):
    """Custom type atiStkSwMacAddrPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwMacAddrPortList_Type.__name__ = "DisplayString"
_AtiStkSwMacAddrPortList_Object = MibTableColumn
atiStkSwMacAddrPortList = _AtiStkSwMacAddrPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 3, 1, 6),
    _AtiStkSwMacAddrPortList_Type()
)
atiStkSwMacAddrPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwMacAddrPortList.setStatus("current")


class _AtiStkSwVlanMode_Type(Integer32):
    """Custom type atiStkSwVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("user-configured", 1),
          ("multiple", 2),
          ("multiple-802-1Q", 3))
    )


_AtiStkSwVlanMode_Type.__name__ = "Integer32"
_AtiStkSwVlanMode_Object = MibScalar
atiStkSwVlanMode = _AtiStkSwVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 4),
    _AtiStkSwVlanMode_Type()
)
atiStkSwVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanMode.setStatus("current")
_AtiStkSwVlanUplinkVlanPort_Type = Integer32
_AtiStkSwVlanUplinkVlanPort_Object = MibScalar
atiStkSwVlanUplinkVlanPort = _AtiStkSwVlanUplinkVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 5),
    _AtiStkSwVlanUplinkVlanPort_Type()
)
atiStkSwVlanUplinkVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwVlanUplinkVlanPort.setStatus("current")
_AtiStkSwGVRPConfig_ObjectIdentity = ObjectIdentity
atiStkSwGVRPConfig = _AtiStkSwGVRPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 6)
)


class _AtiStkSwGVRPStatus_Type(Integer32):
    """Custom type atiStkSwGVRPStatus based on Integer32"""
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


_AtiStkSwGVRPStatus_Type.__name__ = "Integer32"
_AtiStkSwGVRPStatus_Object = MibScalar
atiStkSwGVRPStatus = _AtiStkSwGVRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 6, 1),
    _AtiStkSwGVRPStatus_Type()
)
atiStkSwGVRPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwGVRPStatus.setStatus("current")


class _AtiStkSwGVRPGIPStatus_Type(Integer32):
    """Custom type atiStkSwGVRPGIPStatus based on Integer32"""
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


_AtiStkSwGVRPGIPStatus_Type.__name__ = "Integer32"
_AtiStkSwGVRPGIPStatus_Object = MibScalar
atiStkSwGVRPGIPStatus = _AtiStkSwGVRPGIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 6, 2),
    _AtiStkSwGVRPGIPStatus_Type()
)
atiStkSwGVRPGIPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwGVRPGIPStatus.setStatus("current")


class _AtiStkSwGVRPJoinTimer_Type(Integer32):
    """Custom type atiStkSwGVRPJoinTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_AtiStkSwGVRPJoinTimer_Type.__name__ = "Integer32"
_AtiStkSwGVRPJoinTimer_Object = MibScalar
atiStkSwGVRPJoinTimer = _AtiStkSwGVRPJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 6, 3),
    _AtiStkSwGVRPJoinTimer_Type()
)
atiStkSwGVRPJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwGVRPJoinTimer.setStatus("current")


class _AtiStkSwGVRPLeaveTimer_Type(Integer32):
    """Custom type atiStkSwGVRPLeaveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 180),
    )


_AtiStkSwGVRPLeaveTimer_Type.__name__ = "Integer32"
_AtiStkSwGVRPLeaveTimer_Object = MibScalar
atiStkSwGVRPLeaveTimer = _AtiStkSwGVRPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 6, 4),
    _AtiStkSwGVRPLeaveTimer_Type()
)
atiStkSwGVRPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwGVRPLeaveTimer.setStatus("current")


class _AtiStkSwGVRPLeaveAllTimer_Type(Integer32):
    """Custom type atiStkSwGVRPLeaveAllTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 3000),
    )


_AtiStkSwGVRPLeaveAllTimer_Type.__name__ = "Integer32"
_AtiStkSwGVRPLeaveAllTimer_Object = MibScalar
atiStkSwGVRPLeaveAllTimer = _AtiStkSwGVRPLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 6, 5),
    _AtiStkSwGVRPLeaveAllTimer_Type()
)
atiStkSwGVRPLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwGVRPLeaveAllTimer.setStatus("current")
_AtiStkSwGVRPPortConfigTable_Object = MibTable
atiStkSwGVRPPortConfigTable = _AtiStkSwGVRPPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 7)
)
if mibBuilder.loadTexts:
    atiStkSwGVRPPortConfigTable.setStatus("current")
_AtiStkSwGVRPPortConfigEntry_Object = MibTableRow
atiStkSwGVRPPortConfigEntry = _AtiStkSwGVRPPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 7, 1)
)
atiStkSwGVRPPortConfigEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwGVRPPortConfigModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwGVRPPortConfigPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwGVRPPortConfigEntry.setStatus("current")


class _AtiStkSwGVRPPortConfigModuleId_Type(Integer32):
    """Custom type atiStkSwGVRPPortConfigModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwGVRPPortConfigModuleId_Type.__name__ = "Integer32"
_AtiStkSwGVRPPortConfigModuleId_Object = MibTableColumn
atiStkSwGVRPPortConfigModuleId = _AtiStkSwGVRPPortConfigModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 7, 1, 1),
    _AtiStkSwGVRPPortConfigModuleId_Type()
)
atiStkSwGVRPPortConfigModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPPortConfigModuleId.setStatus("current")


class _AtiStkSwGVRPPortConfigPortId_Type(Integer32):
    """Custom type atiStkSwGVRPPortConfigPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AtiStkSwGVRPPortConfigPortId_Type.__name__ = "Integer32"
_AtiStkSwGVRPPortConfigPortId_Object = MibTableColumn
atiStkSwGVRPPortConfigPortId = _AtiStkSwGVRPPortConfigPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 7, 1, 2),
    _AtiStkSwGVRPPortConfigPortId_Type()
)
atiStkSwGVRPPortConfigPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPPortConfigPortId.setStatus("current")


class _AtiStkSwGVRPPortConfigStatus_Type(Integer32):
    """Custom type atiStkSwGVRPPortConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("normal", 2))
    )


_AtiStkSwGVRPPortConfigStatus_Type.__name__ = "Integer32"
_AtiStkSwGVRPPortConfigStatus_Object = MibTableColumn
atiStkSwGVRPPortConfigStatus = _AtiStkSwGVRPPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 7, 1, 3),
    _AtiStkSwGVRPPortConfigStatus_Type()
)
atiStkSwGVRPPortConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwGVRPPortConfigStatus.setStatus("current")
_AtiStkSwGVRPCountersTable_Object = MibTable
atiStkSwGVRPCountersTable = _AtiStkSwGVRPCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8)
)
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersTable.setStatus("current")
_AtiStkSwGVRPCountersEntry_Object = MibTableRow
atiStkSwGVRPCountersEntry = _AtiStkSwGVRPCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1)
)
atiStkSwGVRPCountersEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwGVRPCountersModuleId"),
)
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersEntry.setStatus("current")


class _AtiStkSwGVRPCountersModuleId_Type(Integer32):
    """Custom type atiStkSwGVRPCountersModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwGVRPCountersModuleId_Type.__name__ = "Integer32"
_AtiStkSwGVRPCountersModuleId_Object = MibTableColumn
atiStkSwGVRPCountersModuleId = _AtiStkSwGVRPCountersModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 1),
    _AtiStkSwGVRPCountersModuleId_Type()
)
atiStkSwGVRPCountersModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersModuleId.setStatus("current")
_AtiStkSwGVRPCountersGARPRxPkt_Type = Counter32
_AtiStkSwGVRPCountersGARPRxPkt_Object = MibTableColumn
atiStkSwGVRPCountersGARPRxPkt = _AtiStkSwGVRPCountersGARPRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 2),
    _AtiStkSwGVRPCountersGARPRxPkt_Type()
)
atiStkSwGVRPCountersGARPRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersGARPRxPkt.setStatus("current")
_AtiStkSwGVRPCountersInvalidGARPRxPkt_Type = Counter32
_AtiStkSwGVRPCountersInvalidGARPRxPkt_Object = MibTableColumn
atiStkSwGVRPCountersInvalidGARPRxPkt = _AtiStkSwGVRPCountersInvalidGARPRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 3),
    _AtiStkSwGVRPCountersInvalidGARPRxPkt_Type()
)
atiStkSwGVRPCountersInvalidGARPRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersInvalidGARPRxPkt.setStatus("current")
_AtiStkSwGVRPCountersGARPTxPkt_Type = Counter32
_AtiStkSwGVRPCountersGARPTxPkt_Object = MibTableColumn
atiStkSwGVRPCountersGARPTxPkt = _AtiStkSwGVRPCountersGARPTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 4),
    _AtiStkSwGVRPCountersGARPTxPkt_Type()
)
atiStkSwGVRPCountersGARPTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersGARPTxPkt.setStatus("current")
_AtiStkSwGVRPCountersGARPTxDisabled_Type = Counter32
_AtiStkSwGVRPCountersGARPTxDisabled_Object = MibTableColumn
atiStkSwGVRPCountersGARPTxDisabled = _AtiStkSwGVRPCountersGARPTxDisabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 5),
    _AtiStkSwGVRPCountersGARPTxDisabled_Type()
)
atiStkSwGVRPCountersGARPTxDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersGARPTxDisabled.setStatus("current")
_AtiStkSwGVRPCountersPortNotSending_Type = Counter32
_AtiStkSwGVRPCountersPortNotSending_Object = MibTableColumn
atiStkSwGVRPCountersPortNotSending = _AtiStkSwGVRPCountersPortNotSending_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 6),
    _AtiStkSwGVRPCountersPortNotSending_Type()
)
atiStkSwGVRPCountersPortNotSending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersPortNotSending.setStatus("current")
_AtiStkSwGVRPCountersGARPDisabled_Type = Counter32
_AtiStkSwGVRPCountersGARPDisabled_Object = MibTableColumn
atiStkSwGVRPCountersGARPDisabled = _AtiStkSwGVRPCountersGARPDisabled_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 7),
    _AtiStkSwGVRPCountersGARPDisabled_Type()
)
atiStkSwGVRPCountersGARPDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersGARPDisabled.setStatus("current")
_AtiStkSwGVRPCountersPortNotListening_Type = Counter32
_AtiStkSwGVRPCountersPortNotListening_Object = MibTableColumn
atiStkSwGVRPCountersPortNotListening = _AtiStkSwGVRPCountersPortNotListening_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 8),
    _AtiStkSwGVRPCountersPortNotListening_Type()
)
atiStkSwGVRPCountersPortNotListening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersPortNotListening.setStatus("current")
_AtiStkSwGVRPCountersInvalidPort_Type = Counter32
_AtiStkSwGVRPCountersInvalidPort_Object = MibTableColumn
atiStkSwGVRPCountersInvalidPort = _AtiStkSwGVRPCountersInvalidPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 9),
    _AtiStkSwGVRPCountersInvalidPort_Type()
)
atiStkSwGVRPCountersInvalidPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersInvalidPort.setStatus("current")
_AtiStkSwGVRPCountersInvalidProtocol_Type = Counter32
_AtiStkSwGVRPCountersInvalidProtocol_Object = MibTableColumn
atiStkSwGVRPCountersInvalidProtocol = _AtiStkSwGVRPCountersInvalidProtocol_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 10),
    _AtiStkSwGVRPCountersInvalidProtocol_Type()
)
atiStkSwGVRPCountersInvalidProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersInvalidProtocol.setStatus("current")
_AtiStkSwGVRPCountersInvalidFormat_Type = Counter32
_AtiStkSwGVRPCountersInvalidFormat_Object = MibTableColumn
atiStkSwGVRPCountersInvalidFormat = _AtiStkSwGVRPCountersInvalidFormat_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 11),
    _AtiStkSwGVRPCountersInvalidFormat_Type()
)
atiStkSwGVRPCountersInvalidFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersInvalidFormat.setStatus("current")
_AtiStkSwGVRPCountersDatabaseFull_Type = Counter32
_AtiStkSwGVRPCountersDatabaseFull_Object = MibTableColumn
atiStkSwGVRPCountersDatabaseFull = _AtiStkSwGVRPCountersDatabaseFull_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 12),
    _AtiStkSwGVRPCountersDatabaseFull_Type()
)
atiStkSwGVRPCountersDatabaseFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersDatabaseFull.setStatus("current")
_AtiStkSwGVRPCountersRxMsgLeaveAll_Type = Counter32
_AtiStkSwGVRPCountersRxMsgLeaveAll_Object = MibTableColumn
atiStkSwGVRPCountersRxMsgLeaveAll = _AtiStkSwGVRPCountersRxMsgLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 13),
    _AtiStkSwGVRPCountersRxMsgLeaveAll_Type()
)
atiStkSwGVRPCountersRxMsgLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersRxMsgLeaveAll.setStatus("current")
_AtiStkSwGVRPCountersRxMsgJoinEmpty_Type = Counter32
_AtiStkSwGVRPCountersRxMsgJoinEmpty_Object = MibTableColumn
atiStkSwGVRPCountersRxMsgJoinEmpty = _AtiStkSwGVRPCountersRxMsgJoinEmpty_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 14),
    _AtiStkSwGVRPCountersRxMsgJoinEmpty_Type()
)
atiStkSwGVRPCountersRxMsgJoinEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersRxMsgJoinEmpty.setStatus("current")
_AtiStkSwGVRPCountersRxMsgJoinIn_Type = Counter32
_AtiStkSwGVRPCountersRxMsgJoinIn_Object = MibTableColumn
atiStkSwGVRPCountersRxMsgJoinIn = _AtiStkSwGVRPCountersRxMsgJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 15),
    _AtiStkSwGVRPCountersRxMsgJoinIn_Type()
)
atiStkSwGVRPCountersRxMsgJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersRxMsgJoinIn.setStatus("current")
_AtiStkSwGVRPCountersRxMsgLeaveEmpty_Type = Counter32
_AtiStkSwGVRPCountersRxMsgLeaveEmpty_Object = MibTableColumn
atiStkSwGVRPCountersRxMsgLeaveEmpty = _AtiStkSwGVRPCountersRxMsgLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 16),
    _AtiStkSwGVRPCountersRxMsgLeaveEmpty_Type()
)
atiStkSwGVRPCountersRxMsgLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersRxMsgLeaveEmpty.setStatus("current")
_AtiStkSwGVRPCountersRxMsgLeaveIn_Type = Counter32
_AtiStkSwGVRPCountersRxMsgLeaveIn_Object = MibTableColumn
atiStkSwGVRPCountersRxMsgLeaveIn = _AtiStkSwGVRPCountersRxMsgLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 17),
    _AtiStkSwGVRPCountersRxMsgLeaveIn_Type()
)
atiStkSwGVRPCountersRxMsgLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersRxMsgLeaveIn.setStatus("current")
_AtiStkSwGVRPCountersRxMsgEmpty_Type = Counter32
_AtiStkSwGVRPCountersRxMsgEmpty_Object = MibTableColumn
atiStkSwGVRPCountersRxMsgEmpty = _AtiStkSwGVRPCountersRxMsgEmpty_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 18),
    _AtiStkSwGVRPCountersRxMsgEmpty_Type()
)
atiStkSwGVRPCountersRxMsgEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersRxMsgEmpty.setStatus("current")
_AtiStkSwGVRPCountersRxMsgBadMsg_Type = Counter32
_AtiStkSwGVRPCountersRxMsgBadMsg_Object = MibTableColumn
atiStkSwGVRPCountersRxMsgBadMsg = _AtiStkSwGVRPCountersRxMsgBadMsg_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 19),
    _AtiStkSwGVRPCountersRxMsgBadMsg_Type()
)
atiStkSwGVRPCountersRxMsgBadMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersRxMsgBadMsg.setStatus("current")
_AtiStkSwGVRPCountersRxMsgBadAttribute_Type = Counter32
_AtiStkSwGVRPCountersRxMsgBadAttribute_Object = MibTableColumn
atiStkSwGVRPCountersRxMsgBadAttribute = _AtiStkSwGVRPCountersRxMsgBadAttribute_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 20),
    _AtiStkSwGVRPCountersRxMsgBadAttribute_Type()
)
atiStkSwGVRPCountersRxMsgBadAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersRxMsgBadAttribute.setStatus("current")
_AtiStkSwGVRPCountersTxMsgLeaveAll_Type = Counter32
_AtiStkSwGVRPCountersTxMsgLeaveAll_Object = MibTableColumn
atiStkSwGVRPCountersTxMsgLeaveAll = _AtiStkSwGVRPCountersTxMsgLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 21),
    _AtiStkSwGVRPCountersTxMsgLeaveAll_Type()
)
atiStkSwGVRPCountersTxMsgLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersTxMsgLeaveAll.setStatus("current")
_AtiStkSwGVRPCountersTxMsgJoinEmpty_Type = Counter32
_AtiStkSwGVRPCountersTxMsgJoinEmpty_Object = MibTableColumn
atiStkSwGVRPCountersTxMsgJoinEmpty = _AtiStkSwGVRPCountersTxMsgJoinEmpty_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 22),
    _AtiStkSwGVRPCountersTxMsgJoinEmpty_Type()
)
atiStkSwGVRPCountersTxMsgJoinEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersTxMsgJoinEmpty.setStatus("current")
_AtiStkSwGVRPCountersTxMsgJoinIn_Type = Counter32
_AtiStkSwGVRPCountersTxMsgJoinIn_Object = MibTableColumn
atiStkSwGVRPCountersTxMsgJoinIn = _AtiStkSwGVRPCountersTxMsgJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 23),
    _AtiStkSwGVRPCountersTxMsgJoinIn_Type()
)
atiStkSwGVRPCountersTxMsgJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersTxMsgJoinIn.setStatus("current")
_AtiStkSwGVRPCountersTxMsgLeaveEmpty_Type = Counter32
_AtiStkSwGVRPCountersTxMsgLeaveEmpty_Object = MibTableColumn
atiStkSwGVRPCountersTxMsgLeaveEmpty = _AtiStkSwGVRPCountersTxMsgLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 24),
    _AtiStkSwGVRPCountersTxMsgLeaveEmpty_Type()
)
atiStkSwGVRPCountersTxMsgLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersTxMsgLeaveEmpty.setStatus("current")
_AtiStkSwGVRPCountersTxMsgLeaveIn_Type = Counter32
_AtiStkSwGVRPCountersTxMsgLeaveIn_Object = MibTableColumn
atiStkSwGVRPCountersTxMsgLeaveIn = _AtiStkSwGVRPCountersTxMsgLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 25),
    _AtiStkSwGVRPCountersTxMsgLeaveIn_Type()
)
atiStkSwGVRPCountersTxMsgLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersTxMsgLeaveIn.setStatus("current")
_AtiStkSwGVRPCountersTxMsgEmpty_Type = Counter32
_AtiStkSwGVRPCountersTxMsgEmpty_Object = MibTableColumn
atiStkSwGVRPCountersTxMsgEmpty = _AtiStkSwGVRPCountersTxMsgEmpty_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 3, 8, 1, 26),
    _AtiStkSwGVRPCountersTxMsgEmpty_Type()
)
atiStkSwGVRPCountersTxMsgEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwGVRPCountersTxMsgEmpty.setStatus("current")
_AtiStkSwMacAddrGroup_ObjectIdentity = ObjectIdentity
atiStkSwMacAddrGroup = _AtiStkSwMacAddrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 4)
)
_AtiStkSwStaticMacAddrTable_Object = MibTable
atiStkSwStaticMacAddrTable = _AtiStkSwStaticMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 4, 1)
)
if mibBuilder.loadTexts:
    atiStkSwStaticMacAddrTable.setStatus("current")
_AtiStkSwStaticMacAddrEntry_Object = MibTableRow
atiStkSwStaticMacAddrEntry = _AtiStkSwStaticMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 4, 1, 1)
)
atiStkSwStaticMacAddrEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwStaticMacAddress"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwStaticMacAddrVlanId"),
)
if mibBuilder.loadTexts:
    atiStkSwStaticMacAddrEntry.setStatus("current")
_AtiStkSwStaticMacAddress_Type = MacAddress
_AtiStkSwStaticMacAddress_Object = MibTableColumn
atiStkSwStaticMacAddress = _AtiStkSwStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 4, 1, 1, 1),
    _AtiStkSwStaticMacAddress_Type()
)
atiStkSwStaticMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwStaticMacAddress.setStatus("current")


class _AtiStkSwStaticMacAddrVlanId_Type(Integer32):
    """Custom type atiStkSwStaticMacAddrVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AtiStkSwStaticMacAddrVlanId_Type.__name__ = "Integer32"
_AtiStkSwStaticMacAddrVlanId_Object = MibTableColumn
atiStkSwStaticMacAddrVlanId = _AtiStkSwStaticMacAddrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 4, 1, 1, 2),
    _AtiStkSwStaticMacAddrVlanId_Type()
)
atiStkSwStaticMacAddrVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwStaticMacAddrVlanId.setStatus("current")


class _AtiStkSwStaticMacAddrModuleId_Type(Integer32):
    """Custom type atiStkSwStaticMacAddrModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwStaticMacAddrModuleId_Type.__name__ = "Integer32"
_AtiStkSwStaticMacAddrModuleId_Object = MibTableColumn
atiStkSwStaticMacAddrModuleId = _AtiStkSwStaticMacAddrModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 4, 1, 1, 3),
    _AtiStkSwStaticMacAddrModuleId_Type()
)
atiStkSwStaticMacAddrModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwStaticMacAddrModuleId.setStatus("current")
_AtiStkSwStaticMacAddrPortId_Type = Integer32
_AtiStkSwStaticMacAddrPortId_Object = MibTableColumn
atiStkSwStaticMacAddrPortId = _AtiStkSwStaticMacAddrPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 4, 1, 1, 4),
    _AtiStkSwStaticMacAddrPortId_Type()
)
atiStkSwStaticMacAddrPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwStaticMacAddrPortId.setStatus("current")


class _AtiStkSwStaticMacAddrPortList_Type(DisplayString):
    """Custom type atiStkSwStaticMacAddrPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtiStkSwStaticMacAddrPortList_Type.__name__ = "DisplayString"
_AtiStkSwStaticMacAddrPortList_Object = MibTableColumn
atiStkSwStaticMacAddrPortList = _AtiStkSwStaticMacAddrPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 4, 1, 1, 5),
    _AtiStkSwStaticMacAddrPortList_Type()
)
atiStkSwStaticMacAddrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwStaticMacAddrPortList.setStatus("current")
_AtiStkSwStaticMacAddrEntryStatus_Type = RowStatus
_AtiStkSwStaticMacAddrEntryStatus_Object = MibTableColumn
atiStkSwStaticMacAddrEntryStatus = _AtiStkSwStaticMacAddrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 4, 1, 1, 6),
    _AtiStkSwStaticMacAddrEntryStatus_Type()
)
atiStkSwStaticMacAddrEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiStkSwStaticMacAddrEntryStatus.setStatus("current")
_AtiStkSwEthStatsGroup_ObjectIdentity = ObjectIdentity
atiStkSwEthStatsGroup = _AtiStkSwEthStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5)
)
_AtiStkSwEthModuleMonTable_Object = MibTable
atiStkSwEthModuleMonTable = _AtiStkSwEthModuleMonTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 1)
)
if mibBuilder.loadTexts:
    atiStkSwEthModuleMonTable.setStatus("current")
_AtiStkSwEthModuleMonEntry_Object = MibTableRow
atiStkSwEthModuleMonEntry = _AtiStkSwEthModuleMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 1, 1)
)
atiStkSwEthModuleMonEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
)
if mibBuilder.loadTexts:
    atiStkSwEthModuleMonEntry.setStatus("current")
_AtiStkSwEthModuleMonTxGoodFrames_Type = Counter64
_AtiStkSwEthModuleMonTxGoodFrames_Object = MibTableColumn
atiStkSwEthModuleMonTxGoodFrames = _AtiStkSwEthModuleMonTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 1, 1, 1),
    _AtiStkSwEthModuleMonTxGoodFrames_Type()
)
atiStkSwEthModuleMonTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthModuleMonTxGoodFrames.setStatus("current")
_AtiStkSwEthModuleMonRxGoodFrames_Type = Counter64
_AtiStkSwEthModuleMonRxGoodFrames_Object = MibTableColumn
atiStkSwEthModuleMonRxGoodFrames = _AtiStkSwEthModuleMonRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 1, 1, 2),
    _AtiStkSwEthModuleMonRxGoodFrames_Type()
)
atiStkSwEthModuleMonRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthModuleMonRxGoodFrames.setStatus("current")
_AtiStkSwEthModuleMonTxTotalBytes_Type = Counter64
_AtiStkSwEthModuleMonTxTotalBytes_Object = MibTableColumn
atiStkSwEthModuleMonTxTotalBytes = _AtiStkSwEthModuleMonTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 1, 1, 3),
    _AtiStkSwEthModuleMonTxTotalBytes_Type()
)
atiStkSwEthModuleMonTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthModuleMonTxTotalBytes.setStatus("current")
_AtiStkSwEthModuleMonTxBroadcastFrames_Type = Counter64
_AtiStkSwEthModuleMonTxBroadcastFrames_Object = MibTableColumn
atiStkSwEthModuleMonTxBroadcastFrames = _AtiStkSwEthModuleMonTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 1, 1, 4),
    _AtiStkSwEthModuleMonTxBroadcastFrames_Type()
)
atiStkSwEthModuleMonTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthModuleMonTxBroadcastFrames.setStatus("current")
_AtiStkSwEthModuleMonTxMulticastFrames_Type = Counter64
_AtiStkSwEthModuleMonTxMulticastFrames_Object = MibTableColumn
atiStkSwEthModuleMonTxMulticastFrames = _AtiStkSwEthModuleMonTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 1, 1, 5),
    _AtiStkSwEthModuleMonTxMulticastFrames_Type()
)
atiStkSwEthModuleMonTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthModuleMonTxMulticastFrames.setStatus("current")
_AtiStkSwEthModuleMonRxOverrunFrames_Type = Counter64
_AtiStkSwEthModuleMonRxOverrunFrames_Object = MibTableColumn
atiStkSwEthModuleMonRxOverrunFrames = _AtiStkSwEthModuleMonRxOverrunFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 1, 1, 6),
    _AtiStkSwEthModuleMonRxOverrunFrames_Type()
)
atiStkSwEthModuleMonRxOverrunFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthModuleMonRxOverrunFrames.setStatus("current")
_AtiStkSwEthModuleErrTable_Object = MibTable
atiStkSwEthModuleErrTable = _AtiStkSwEthModuleErrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 2)
)
if mibBuilder.loadTexts:
    atiStkSwEthModuleErrTable.setStatus("current")
_AtiStkSwEthModuleErrEntry_Object = MibTableRow
atiStkSwEthModuleErrEntry = _AtiStkSwEthModuleErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 2, 1)
)
atiStkSwEthModuleErrEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
)
if mibBuilder.loadTexts:
    atiStkSwEthModuleErrEntry.setStatus("current")
_AtiStkSwEthModuleErrRxCRC_Type = Counter64
_AtiStkSwEthModuleErrRxCRC_Object = MibTableColumn
atiStkSwEthModuleErrRxCRC = _AtiStkSwEthModuleErrRxCRC_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 2, 1, 1),
    _AtiStkSwEthModuleErrRxCRC_Type()
)
atiStkSwEthModuleErrRxCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthModuleErrRxCRC.setStatus("current")
_AtiStkSwEthModuleErrRxBadFrames_Type = Counter64
_AtiStkSwEthModuleErrRxBadFrames_Object = MibTableColumn
atiStkSwEthModuleErrRxBadFrames = _AtiStkSwEthModuleErrRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 2, 1, 2),
    _AtiStkSwEthModuleErrRxBadFrames_Type()
)
atiStkSwEthModuleErrRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthModuleErrRxBadFrames.setStatus("current")
_AtiStkSwEthModuleErrCollisions_Type = Counter64
_AtiStkSwEthModuleErrCollisions_Object = MibTableColumn
atiStkSwEthModuleErrCollisions = _AtiStkSwEthModuleErrCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 2, 1, 3),
    _AtiStkSwEthModuleErrCollisions_Type()
)
atiStkSwEthModuleErrCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthModuleErrCollisions.setStatus("current")
_AtiStkSwEthPortMonTable_Object = MibTable
atiStkSwEthPortMonTable = _AtiStkSwEthPortMonTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 3)
)
if mibBuilder.loadTexts:
    atiStkSwEthPortMonTable.setStatus("current")
_AtiStkSwEthPortMonEntry_Object = MibTableRow
atiStkSwEthPortMonEntry = _AtiStkSwEthPortMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 3, 1)
)
atiStkSwEthPortMonEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwEthPortMonEntry.setStatus("current")
_AtiStkSwEthPortMonTxGoodFrames_Type = Counter64
_AtiStkSwEthPortMonTxGoodFrames_Object = MibTableColumn
atiStkSwEthPortMonTxGoodFrames = _AtiStkSwEthPortMonTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 3, 1, 1),
    _AtiStkSwEthPortMonTxGoodFrames_Type()
)
atiStkSwEthPortMonTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthPortMonTxGoodFrames.setStatus("current")
_AtiStkSwEthPortMonRxGoodFrames_Type = Counter64
_AtiStkSwEthPortMonRxGoodFrames_Object = MibTableColumn
atiStkSwEthPortMonRxGoodFrames = _AtiStkSwEthPortMonRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 3, 1, 2),
    _AtiStkSwEthPortMonRxGoodFrames_Type()
)
atiStkSwEthPortMonRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthPortMonRxGoodFrames.setStatus("current")
_AtiStkSwEthPortMonTxTotalBytes_Type = Counter64
_AtiStkSwEthPortMonTxTotalBytes_Object = MibTableColumn
atiStkSwEthPortMonTxTotalBytes = _AtiStkSwEthPortMonTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 3, 1, 3),
    _AtiStkSwEthPortMonTxTotalBytes_Type()
)
atiStkSwEthPortMonTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthPortMonTxTotalBytes.setStatus("current")
_AtiStkSwEthPortMonTxBroadcastFrames_Type = Counter64
_AtiStkSwEthPortMonTxBroadcastFrames_Object = MibTableColumn
atiStkSwEthPortMonTxBroadcastFrames = _AtiStkSwEthPortMonTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 3, 1, 4),
    _AtiStkSwEthPortMonTxBroadcastFrames_Type()
)
atiStkSwEthPortMonTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthPortMonTxBroadcastFrames.setStatus("current")
_AtiStkSwEthPortMonTxMulticastFrames_Type = Counter64
_AtiStkSwEthPortMonTxMulticastFrames_Object = MibTableColumn
atiStkSwEthPortMonTxMulticastFrames = _AtiStkSwEthPortMonTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 3, 1, 5),
    _AtiStkSwEthPortMonTxMulticastFrames_Type()
)
atiStkSwEthPortMonTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthPortMonTxMulticastFrames.setStatus("current")
_AtiStkSwEthPortMonRxOverrunFrames_Type = Counter64
_AtiStkSwEthPortMonRxOverrunFrames_Object = MibTableColumn
atiStkSwEthPortMonRxOverrunFrames = _AtiStkSwEthPortMonRxOverrunFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 3, 1, 6),
    _AtiStkSwEthPortMonRxOverrunFrames_Type()
)
atiStkSwEthPortMonRxOverrunFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthPortMonRxOverrunFrames.setStatus("current")
_AtiStkSwEthPortErrTable_Object = MibTable
atiStkSwEthPortErrTable = _AtiStkSwEthPortErrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 4)
)
if mibBuilder.loadTexts:
    atiStkSwEthPortErrTable.setStatus("current")
_AtiStkSwEthPortErrEntry_Object = MibTableRow
atiStkSwEthPortErrEntry = _AtiStkSwEthPortErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 4, 1)
)
atiStkSwEthPortErrEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwEthPortErrEntry.setStatus("current")
_AtiStkSwEthPortErrRxBadFrames_Type = Counter64
_AtiStkSwEthPortErrRxBadFrames_Object = MibTableColumn
atiStkSwEthPortErrRxBadFrames = _AtiStkSwEthPortErrRxBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 4, 1, 1),
    _AtiStkSwEthPortErrRxBadFrames_Type()
)
atiStkSwEthPortErrRxBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthPortErrRxBadFrames.setStatus("current")
_AtiStkSwEthPortErrCollisions_Type = Counter64
_AtiStkSwEthPortErrCollisions_Object = MibTableColumn
atiStkSwEthPortErrCollisions = _AtiStkSwEthPortErrCollisions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 5, 4, 1, 2),
    _AtiStkSwEthPortErrCollisions_Type()
)
atiStkSwEthPortErrCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwEthPortErrCollisions.setStatus("current")
_AtiStkSwTrapsGroup_ObjectIdentity = ObjectIdentity
atiStkSwTrapsGroup = _AtiStkSwTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6)
)


class _AtiStkSwTrapVarMgmtType_Type(Integer32):
    """Custom type atiStkSwTrapVarMgmtType based on Integer32"""
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
        *(("notrap", 1),
          ("ssh", 2),
          ("telnet", 3),
          ("web", 4))
    )


_AtiStkSwTrapVarMgmtType_Type.__name__ = "Integer32"
_AtiStkSwTrapVarMgmtType_Object = MibScalar
atiStkSwTrapVarMgmtType = _AtiStkSwTrapVarMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 8),
    _AtiStkSwTrapVarMgmtType_Type()
)
atiStkSwTrapVarMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwTrapVarMgmtType.setStatus("current")
_AtiStkSwTrapVarMgmtIpAddr_Type = IpAddress
_AtiStkSwTrapVarMgmtIpAddr_Object = MibScalar
atiStkSwTrapVarMgmtIpAddr = _AtiStkSwTrapVarMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 9),
    _AtiStkSwTrapVarMgmtIpAddr_Type()
)
atiStkSwTrapVarMgmtIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwTrapVarMgmtIpAddr.setStatus("current")
_AtiStkSwQoSGroup_ObjectIdentity = ObjectIdentity
atiStkSwQoSGroup = _AtiStkSwQoSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7)
)
_AtiStkSwQoSGroupNumberOfQueues_Type = Integer32
_AtiStkSwQoSGroupNumberOfQueues_Object = MibScalar
atiStkSwQoSGroupNumberOfQueues = _AtiStkSwQoSGroupNumberOfQueues_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 1),
    _AtiStkSwQoSGroupNumberOfQueues_Type()
)
atiStkSwQoSGroupNumberOfQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupNumberOfQueues.setStatus("current")


class _AtiStkSwQoSGroupSchedulingMode_Type(Integer32):
    """Custom type atiStkSwQoSGroupSchedulingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict-priority", 1),
          ("weighted-round-robin", 2))
    )


_AtiStkSwQoSGroupSchedulingMode_Type.__name__ = "Integer32"
_AtiStkSwQoSGroupSchedulingMode_Object = MibScalar
atiStkSwQoSGroupSchedulingMode = _AtiStkSwQoSGroupSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 2),
    _AtiStkSwQoSGroupSchedulingMode_Type()
)
atiStkSwQoSGroupSchedulingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupSchedulingMode.setStatus("current")
_AtiStkSwQoSGroupCoSToQueueTable_Object = MibTable
atiStkSwQoSGroupCoSToQueueTable = _AtiStkSwQoSGroupCoSToQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 3)
)
if mibBuilder.loadTexts:
    atiStkSwQoSGroupCoSToQueueTable.setStatus("current")
_AtiStkSwQoSGroupCoSToQueueEntry_Object = MibTableRow
atiStkSwQoSGroupCoSToQueueEntry = _AtiStkSwQoSGroupCoSToQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 3, 1)
)
atiStkSwQoSGroupCoSToQueueEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQoSGroupCoSPriority"),
)
if mibBuilder.loadTexts:
    atiStkSwQoSGroupCoSToQueueEntry.setStatus("current")


class _AtiStkSwQoSGroupCoSPriority_Type(Integer32):
    """Custom type atiStkSwQoSGroupCoSPriority based on Integer32"""
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
        *(("cos-priority-0", 1),
          ("cos-priority-1", 2),
          ("cos-priority-2", 3),
          ("cos-priority-3", 4),
          ("cos-priority-4", 5),
          ("cos-priority-5", 6),
          ("cos-priority-6", 7),
          ("cos-priority-7", 8))
    )


_AtiStkSwQoSGroupCoSPriority_Type.__name__ = "Integer32"
_AtiStkSwQoSGroupCoSPriority_Object = MibTableColumn
atiStkSwQoSGroupCoSPriority = _AtiStkSwQoSGroupCoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 3, 1, 1),
    _AtiStkSwQoSGroupCoSPriority_Type()
)
atiStkSwQoSGroupCoSPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupCoSPriority.setStatus("current")


class _AtiStkSwQoSGroupCoSQueue_Type(Integer32):
    """Custom type atiStkSwQoSGroupCoSQueue based on Integer32"""
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
        *(("egress-queue-0", 1),
          ("egress-queue-1", 2),
          ("egress-queue-2", 3),
          ("egress-queue-3", 4),
          ("egress-queue-4", 5),
          ("egress-queue-5", 6),
          ("egress-queue-6", 7),
          ("egress-queue-7", 8))
    )


_AtiStkSwQoSGroupCoSQueue_Type.__name__ = "Integer32"
_AtiStkSwQoSGroupCoSQueue_Object = MibTableColumn
atiStkSwQoSGroupCoSQueue = _AtiStkSwQoSGroupCoSQueue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 3, 1, 2),
    _AtiStkSwQoSGroupCoSQueue_Type()
)
atiStkSwQoSGroupCoSQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupCoSQueue.setStatus("current")
_AtiStkSwQoSGroupQueueToWeightTable_Object = MibTable
atiStkSwQoSGroupQueueToWeightTable = _AtiStkSwQoSGroupQueueToWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 4)
)
if mibBuilder.loadTexts:
    atiStkSwQoSGroupQueueToWeightTable.setStatus("current")
_AtiStkSwQoSGroupQueueToWeightEntry_Object = MibTableRow
atiStkSwQoSGroupQueueToWeightEntry = _AtiStkSwQoSGroupQueueToWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 4, 1)
)
atiStkSwQoSGroupQueueToWeightEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQoSGroupQueue"),
)
if mibBuilder.loadTexts:
    atiStkSwQoSGroupQueueToWeightEntry.setStatus("current")


class _AtiStkSwQoSGroupQueue_Type(Integer32):
    """Custom type atiStkSwQoSGroupQueue based on Integer32"""
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
        *(("egress-queue-0", 1),
          ("egress-queue-1", 2),
          ("egress-queue-2", 3),
          ("egress-queue-3", 4),
          ("egress-queue-4", 5),
          ("egress-queue-5", 6),
          ("egress-queue-6", 7),
          ("egress-queue-7", 8))
    )


_AtiStkSwQoSGroupQueue_Type.__name__ = "Integer32"
_AtiStkSwQoSGroupQueue_Object = MibTableColumn
atiStkSwQoSGroupQueue = _AtiStkSwQoSGroupQueue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 4, 1, 1),
    _AtiStkSwQoSGroupQueue_Type()
)
atiStkSwQoSGroupQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupQueue.setStatus("current")


class _AtiStkSwQoSGroupQueueWeight_Type(Integer32):
    """Custom type atiStkSwQoSGroupQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AtiStkSwQoSGroupQueueWeight_Type.__name__ = "Integer32"
_AtiStkSwQoSGroupQueueWeight_Object = MibTableColumn
atiStkSwQoSGroupQueueWeight = _AtiStkSwQoSGroupQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 4, 1, 2),
    _AtiStkSwQoSGroupQueueWeight_Type()
)
atiStkSwQoSGroupQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupQueueWeight.setStatus("current")
_AtiStkSwQosFlowGrpTable_Object = MibTable
atiStkSwQosFlowGrpTable = _AtiStkSwQosFlowGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5)
)
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpTable.setStatus("current")
_AtiStkSwQosFlowGrpEntry_Object = MibTableRow
atiStkSwQosFlowGrpEntry = _AtiStkSwQosFlowGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1)
)
atiStkSwQosFlowGrpEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQosFlowGrpModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQosFlowGrpId"),
)
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpEntry.setStatus("current")


class _AtiStkSwQosFlowGrpModuleId_Type(Integer32):
    """Custom type atiStkSwQosFlowGrpModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwQosFlowGrpModuleId_Type.__name__ = "Integer32"
_AtiStkSwQosFlowGrpModuleId_Object = MibTableColumn
atiStkSwQosFlowGrpModuleId = _AtiStkSwQosFlowGrpModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 1),
    _AtiStkSwQosFlowGrpModuleId_Type()
)
atiStkSwQosFlowGrpModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpModuleId.setStatus("current")


class _AtiStkSwQosFlowGrpId_Type(Integer32):
    """Custom type atiStkSwQosFlowGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AtiStkSwQosFlowGrpId_Type.__name__ = "Integer32"
_AtiStkSwQosFlowGrpId_Object = MibTableColumn
atiStkSwQosFlowGrpId = _AtiStkSwQosFlowGrpId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 2),
    _AtiStkSwQosFlowGrpId_Type()
)
atiStkSwQosFlowGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpId.setStatus("current")


class _AtiStkSwQosFlowGrpDescription_Type(DisplayString):
    """Custom type atiStkSwQosFlowGrpDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AtiStkSwQosFlowGrpDescription_Type.__name__ = "DisplayString"
_AtiStkSwQosFlowGrpDescription_Object = MibTableColumn
atiStkSwQosFlowGrpDescription = _AtiStkSwQosFlowGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 3),
    _AtiStkSwQosFlowGrpDescription_Type()
)
atiStkSwQosFlowGrpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpDescription.setStatus("current")


class _AtiStkSwQosFlowGrpDSCPValue_Type(DisplayString):
    """Custom type atiStkSwQosFlowGrpDSCPValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AtiStkSwQosFlowGrpDSCPValue_Type.__name__ = "DisplayString"
_AtiStkSwQosFlowGrpDSCPValue_Object = MibTableColumn
atiStkSwQosFlowGrpDSCPValue = _AtiStkSwQosFlowGrpDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 4),
    _AtiStkSwQosFlowGrpDSCPValue_Type()
)
atiStkSwQosFlowGrpDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpDSCPValue.setStatus("current")


class _AtiStkSwQosFlowGrpPriority_Type(DisplayString):
    """Custom type atiStkSwQosFlowGrpPriority based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_AtiStkSwQosFlowGrpPriority_Type.__name__ = "DisplayString"
_AtiStkSwQosFlowGrpPriority_Object = MibTableColumn
atiStkSwQosFlowGrpPriority = _AtiStkSwQosFlowGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 5),
    _AtiStkSwQosFlowGrpPriority_Type()
)
atiStkSwQosFlowGrpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpPriority.setStatus("current")


class _AtiStkSwQosFlowGrpRemarkPriority_Type(Integer32):
    """Custom type atiStkSwQosFlowGrpRemarkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQosFlowGrpRemarkPriority_Type.__name__ = "Integer32"
_AtiStkSwQosFlowGrpRemarkPriority_Object = MibTableColumn
atiStkSwQosFlowGrpRemarkPriority = _AtiStkSwQosFlowGrpRemarkPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 6),
    _AtiStkSwQosFlowGrpRemarkPriority_Type()
)
atiStkSwQosFlowGrpRemarkPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpRemarkPriority.setStatus("current")


class _AtiStkSwQosFlowGrpTos_Type(DisplayString):
    """Custom type atiStkSwQosFlowGrpTos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_AtiStkSwQosFlowGrpTos_Type.__name__ = "DisplayString"
_AtiStkSwQosFlowGrpTos_Object = MibTableColumn
atiStkSwQosFlowGrpTos = _AtiStkSwQosFlowGrpTos_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 7),
    _AtiStkSwQosFlowGrpTos_Type()
)
atiStkSwQosFlowGrpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpTos.setStatus("current")


class _AtiStkSwQosFlowGrpTosToPriority_Type(Integer32):
    """Custom type atiStkSwQosFlowGrpTosToPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQosFlowGrpTosToPriority_Type.__name__ = "Integer32"
_AtiStkSwQosFlowGrpTosToPriority_Object = MibTableColumn
atiStkSwQosFlowGrpTosToPriority = _AtiStkSwQosFlowGrpTosToPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 8),
    _AtiStkSwQosFlowGrpTosToPriority_Type()
)
atiStkSwQosFlowGrpTosToPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpTosToPriority.setStatus("current")


class _AtiStkSwQosFlowGrpPriorityToTos_Type(Integer32):
    """Custom type atiStkSwQosFlowGrpPriorityToTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQosFlowGrpPriorityToTos_Type.__name__ = "Integer32"
_AtiStkSwQosFlowGrpPriorityToTos_Object = MibTableColumn
atiStkSwQosFlowGrpPriorityToTos = _AtiStkSwQosFlowGrpPriorityToTos_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 9),
    _AtiStkSwQosFlowGrpPriorityToTos_Type()
)
atiStkSwQosFlowGrpPriorityToTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpPriorityToTos.setStatus("current")
_AtiStkSwQosFlowGrpClassifierList_Type = DisplayString
_AtiStkSwQosFlowGrpClassifierList_Object = MibTableColumn
atiStkSwQosFlowGrpClassifierList = _AtiStkSwQosFlowGrpClassifierList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 10),
    _AtiStkSwQosFlowGrpClassifierList_Type()
)
atiStkSwQosFlowGrpClassifierList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpClassifierList.setStatus("current")
_AtiStkSwQosFlowGrpRowStatus_Type = RowStatus
_AtiStkSwQosFlowGrpRowStatus_Object = MibTableColumn
atiStkSwQosFlowGrpRowStatus = _AtiStkSwQosFlowGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 5, 1, 11),
    _AtiStkSwQosFlowGrpRowStatus_Type()
)
atiStkSwQosFlowGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiStkSwQosFlowGrpRowStatus.setStatus("current")
_AtiStkSwQosTrafficClassTable_Object = MibTable
atiStkSwQosTrafficClassTable = _AtiStkSwQosTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6)
)
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassTable.setStatus("current")
_AtiStkSwQosTrafficClassEntry_Object = MibTableRow
atiStkSwQosTrafficClassEntry = _AtiStkSwQosTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1)
)
atiStkSwQosTrafficClassEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQosTrafficClassModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQosTrafficClassId"),
)
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassEntry.setStatus("current")


class _AtiStkSwQosTrafficClassModuleId_Type(Integer32):
    """Custom type atiStkSwQosTrafficClassModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwQosTrafficClassModuleId_Type.__name__ = "Integer32"
_AtiStkSwQosTrafficClassModuleId_Object = MibTableColumn
atiStkSwQosTrafficClassModuleId = _AtiStkSwQosTrafficClassModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 1),
    _AtiStkSwQosTrafficClassModuleId_Type()
)
atiStkSwQosTrafficClassModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassModuleId.setStatus("current")


class _AtiStkSwQosTrafficClassId_Type(Integer32):
    """Custom type atiStkSwQosTrafficClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AtiStkSwQosTrafficClassId_Type.__name__ = "Integer32"
_AtiStkSwQosTrafficClassId_Object = MibTableColumn
atiStkSwQosTrafficClassId = _AtiStkSwQosTrafficClassId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 2),
    _AtiStkSwQosTrafficClassId_Type()
)
atiStkSwQosTrafficClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassId.setStatus("current")


class _AtiStkSwQosTrafficClassDescription_Type(DisplayString):
    """Custom type atiStkSwQosTrafficClassDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AtiStkSwQosTrafficClassDescription_Type.__name__ = "DisplayString"
_AtiStkSwQosTrafficClassDescription_Object = MibTableColumn
atiStkSwQosTrafficClassDescription = _AtiStkSwQosTrafficClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 3),
    _AtiStkSwQosTrafficClassDescription_Type()
)
atiStkSwQosTrafficClassDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassDescription.setStatus("current")


class _AtiStkSwQosTrafficClassExceedAction_Type(Integer32):
    """Custom type atiStkSwQosTrafficClassExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("remark", 2))
    )


_AtiStkSwQosTrafficClassExceedAction_Type.__name__ = "Integer32"
_AtiStkSwQosTrafficClassExceedAction_Object = MibTableColumn
atiStkSwQosTrafficClassExceedAction = _AtiStkSwQosTrafficClassExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 4),
    _AtiStkSwQosTrafficClassExceedAction_Type()
)
atiStkSwQosTrafficClassExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassExceedAction.setStatus("current")


class _AtiStkSwQosTrafficClassExceedRemarkValue_Type(Integer32):
    """Custom type atiStkSwQosTrafficClassExceedRemarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AtiStkSwQosTrafficClassExceedRemarkValue_Type.__name__ = "Integer32"
_AtiStkSwQosTrafficClassExceedRemarkValue_Object = MibTableColumn
atiStkSwQosTrafficClassExceedRemarkValue = _AtiStkSwQosTrafficClassExceedRemarkValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 5),
    _AtiStkSwQosTrafficClassExceedRemarkValue_Type()
)
atiStkSwQosTrafficClassExceedRemarkValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassExceedRemarkValue.setStatus("current")


class _AtiStkSwQosTrafficClassDSCPValue_Type(DisplayString):
    """Custom type atiStkSwQosTrafficClassDSCPValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AtiStkSwQosTrafficClassDSCPValue_Type.__name__ = "DisplayString"
_AtiStkSwQosTrafficClassDSCPValue_Object = MibTableColumn
atiStkSwQosTrafficClassDSCPValue = _AtiStkSwQosTrafficClassDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 6),
    _AtiStkSwQosTrafficClassDSCPValue_Type()
)
atiStkSwQosTrafficClassDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassDSCPValue.setStatus("current")


class _AtiStkSwQosTrafficClassMaxBandwidth_Type(DisplayString):
    """Custom type atiStkSwQosTrafficClassMaxBandwidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtiStkSwQosTrafficClassMaxBandwidth_Type.__name__ = "DisplayString"
_AtiStkSwQosTrafficClassMaxBandwidth_Object = MibTableColumn
atiStkSwQosTrafficClassMaxBandwidth = _AtiStkSwQosTrafficClassMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 7),
    _AtiStkSwQosTrafficClassMaxBandwidth_Type()
)
atiStkSwQosTrafficClassMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassMaxBandwidth.setStatus("current")


class _AtiStkSwQosTrafficClassBurstSize_Type(DisplayString):
    """Custom type atiStkSwQosTrafficClassBurstSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtiStkSwQosTrafficClassBurstSize_Type.__name__ = "DisplayString"
_AtiStkSwQosTrafficClassBurstSize_Object = MibTableColumn
atiStkSwQosTrafficClassBurstSize = _AtiStkSwQosTrafficClassBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 8),
    _AtiStkSwQosTrafficClassBurstSize_Type()
)
atiStkSwQosTrafficClassBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassBurstSize.setStatus("current")


class _AtiStkSwQosTrafficClassPriority_Type(DisplayString):
    """Custom type atiStkSwQosTrafficClassPriority based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AtiStkSwQosTrafficClassPriority_Type.__name__ = "DisplayString"
_AtiStkSwQosTrafficClassPriority_Object = MibTableColumn
atiStkSwQosTrafficClassPriority = _AtiStkSwQosTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 9),
    _AtiStkSwQosTrafficClassPriority_Type()
)
atiStkSwQosTrafficClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassPriority.setStatus("current")


class _AtiStkSwQosTrafficClassRemarkPriority_Type(Integer32):
    """Custom type atiStkSwQosTrafficClassRemarkPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQosTrafficClassRemarkPriority_Type.__name__ = "Integer32"
_AtiStkSwQosTrafficClassRemarkPriority_Object = MibTableColumn
atiStkSwQosTrafficClassRemarkPriority = _AtiStkSwQosTrafficClassRemarkPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 10),
    _AtiStkSwQosTrafficClassRemarkPriority_Type()
)
atiStkSwQosTrafficClassRemarkPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassRemarkPriority.setStatus("current")


class _AtiStkSwQosTrafficClassToS_Type(DisplayString):
    """Custom type atiStkSwQosTrafficClassToS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AtiStkSwQosTrafficClassToS_Type.__name__ = "DisplayString"
_AtiStkSwQosTrafficClassToS_Object = MibTableColumn
atiStkSwQosTrafficClassToS = _AtiStkSwQosTrafficClassToS_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 11),
    _AtiStkSwQosTrafficClassToS_Type()
)
atiStkSwQosTrafficClassToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassToS.setStatus("current")


class _AtiStkSwQosTrafficClassMoveToSToPriority_Type(Integer32):
    """Custom type atiStkSwQosTrafficClassMoveToSToPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQosTrafficClassMoveToSToPriority_Type.__name__ = "Integer32"
_AtiStkSwQosTrafficClassMoveToSToPriority_Object = MibTableColumn
atiStkSwQosTrafficClassMoveToSToPriority = _AtiStkSwQosTrafficClassMoveToSToPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 12),
    _AtiStkSwQosTrafficClassMoveToSToPriority_Type()
)
atiStkSwQosTrafficClassMoveToSToPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassMoveToSToPriority.setStatus("current")


class _AtiStkSwQosTrafficClassMovePriorityToToS_Type(Integer32):
    """Custom type atiStkSwQosTrafficClassMovePriorityToToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQosTrafficClassMovePriorityToToS_Type.__name__ = "Integer32"
_AtiStkSwQosTrafficClassMovePriorityToToS_Object = MibTableColumn
atiStkSwQosTrafficClassMovePriorityToToS = _AtiStkSwQosTrafficClassMovePriorityToToS_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 13),
    _AtiStkSwQosTrafficClassMovePriorityToToS_Type()
)
atiStkSwQosTrafficClassMovePriorityToToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassMovePriorityToToS.setStatus("current")
_AtiStkSwQosTrafficClassFlowGroupList_Type = DisplayString
_AtiStkSwQosTrafficClassFlowGroupList_Object = MibTableColumn
atiStkSwQosTrafficClassFlowGroupList = _AtiStkSwQosTrafficClassFlowGroupList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 14),
    _AtiStkSwQosTrafficClassFlowGroupList_Type()
)
atiStkSwQosTrafficClassFlowGroupList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassFlowGroupList.setStatus("current")
_AtiStkSwQosTrafficClassRowStatus_Type = RowStatus
_AtiStkSwQosTrafficClassRowStatus_Object = MibTableColumn
atiStkSwQosTrafficClassRowStatus = _AtiStkSwQosTrafficClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 6, 1, 15),
    _AtiStkSwQosTrafficClassRowStatus_Type()
)
atiStkSwQosTrafficClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiStkSwQosTrafficClassRowStatus.setStatus("current")
_AtiStkSwQosPolicyTable_Object = MibTable
atiStkSwQosPolicyTable = _AtiStkSwQosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7)
)
if mibBuilder.loadTexts:
    atiStkSwQosPolicyTable.setStatus("current")
_AtiStkSwQosPolicyEntry_Object = MibTableRow
atiStkSwQosPolicyEntry = _AtiStkSwQosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1)
)
atiStkSwQosPolicyEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQosPolicyModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQosPolicyId"),
)
if mibBuilder.loadTexts:
    atiStkSwQosPolicyEntry.setStatus("current")


class _AtiStkSwQosPolicyModuleId_Type(Integer32):
    """Custom type atiStkSwQosPolicyModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwQosPolicyModuleId_Type.__name__ = "Integer32"
_AtiStkSwQosPolicyModuleId_Object = MibTableColumn
atiStkSwQosPolicyModuleId = _AtiStkSwQosPolicyModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 1),
    _AtiStkSwQosPolicyModuleId_Type()
)
atiStkSwQosPolicyModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyModuleId.setStatus("current")


class _AtiStkSwQosPolicyId_Type(Integer32):
    """Custom type atiStkSwQosPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AtiStkSwQosPolicyId_Type.__name__ = "Integer32"
_AtiStkSwQosPolicyId_Object = MibTableColumn
atiStkSwQosPolicyId = _AtiStkSwQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 2),
    _AtiStkSwQosPolicyId_Type()
)
atiStkSwQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyId.setStatus("current")


class _AtiStkSwQosPolicyDescription_Type(DisplayString):
    """Custom type atiStkSwQosPolicyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AtiStkSwQosPolicyDescription_Type.__name__ = "DisplayString"
_AtiStkSwQosPolicyDescription_Object = MibTableColumn
atiStkSwQosPolicyDescription = _AtiStkSwQosPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 3),
    _AtiStkSwQosPolicyDescription_Type()
)
atiStkSwQosPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyDescription.setStatus("current")


class _AtiStkSwQosPolicyRemarkDSCP_Type(Integer32):
    """Custom type atiStkSwQosPolicyRemarkDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("none", 2))
    )


_AtiStkSwQosPolicyRemarkDSCP_Type.__name__ = "Integer32"
_AtiStkSwQosPolicyRemarkDSCP_Object = MibTableColumn
atiStkSwQosPolicyRemarkDSCP = _AtiStkSwQosPolicyRemarkDSCP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 4),
    _AtiStkSwQosPolicyRemarkDSCP_Type()
)
atiStkSwQosPolicyRemarkDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyRemarkDSCP.setStatus("current")


class _AtiStkSwQosPolicyDSCPValue_Type(DisplayString):
    """Custom type atiStkSwQosPolicyDSCPValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AtiStkSwQosPolicyDSCPValue_Type.__name__ = "DisplayString"
_AtiStkSwQosPolicyDSCPValue_Object = MibTableColumn
atiStkSwQosPolicyDSCPValue = _AtiStkSwQosPolicyDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 5),
    _AtiStkSwQosPolicyDSCPValue_Type()
)
atiStkSwQosPolicyDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyDSCPValue.setStatus("current")


class _AtiStkSwQosPolicyToS_Type(DisplayString):
    """Custom type atiStkSwQosPolicyToS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AtiStkSwQosPolicyToS_Type.__name__ = "DisplayString"
_AtiStkSwQosPolicyToS_Object = MibTableColumn
atiStkSwQosPolicyToS = _AtiStkSwQosPolicyToS_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 6),
    _AtiStkSwQosPolicyToS_Type()
)
atiStkSwQosPolicyToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyToS.setStatus("current")


class _AtiStkSwQosPolicyMoveToSToPriority_Type(Integer32):
    """Custom type atiStkSwQosPolicyMoveToSToPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQosPolicyMoveToSToPriority_Type.__name__ = "Integer32"
_AtiStkSwQosPolicyMoveToSToPriority_Object = MibTableColumn
atiStkSwQosPolicyMoveToSToPriority = _AtiStkSwQosPolicyMoveToSToPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 7),
    _AtiStkSwQosPolicyMoveToSToPriority_Type()
)
atiStkSwQosPolicyMoveToSToPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyMoveToSToPriority.setStatus("current")


class _AtiStkSwQosPolicyMovePriorityToToS_Type(Integer32):
    """Custom type atiStkSwQosPolicyMovePriorityToToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQosPolicyMovePriorityToToS_Type.__name__ = "Integer32"
_AtiStkSwQosPolicyMovePriorityToToS_Object = MibTableColumn
atiStkSwQosPolicyMovePriorityToToS = _AtiStkSwQosPolicyMovePriorityToToS_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 8),
    _AtiStkSwQosPolicyMovePriorityToToS_Type()
)
atiStkSwQosPolicyMovePriorityToToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyMovePriorityToToS.setStatus("current")


class _AtiStkSwQosPolicySendToMirrorPort_Type(Integer32):
    """Custom type atiStkSwQosPolicySendToMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQosPolicySendToMirrorPort_Type.__name__ = "Integer32"
_AtiStkSwQosPolicySendToMirrorPort_Object = MibTableColumn
atiStkSwQosPolicySendToMirrorPort = _AtiStkSwQosPolicySendToMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 9),
    _AtiStkSwQosPolicySendToMirrorPort_Type()
)
atiStkSwQosPolicySendToMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicySendToMirrorPort.setStatus("current")
_AtiStkSwQosPolicyTrafficClassList_Type = DisplayString
_AtiStkSwQosPolicyTrafficClassList_Object = MibTableColumn
atiStkSwQosPolicyTrafficClassList = _AtiStkSwQosPolicyTrafficClassList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 10),
    _AtiStkSwQosPolicyTrafficClassList_Type()
)
atiStkSwQosPolicyTrafficClassList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyTrafficClassList.setStatus("current")
_AtiStkSwQosPolicyRedirectPort_Type = DisplayString
_AtiStkSwQosPolicyRedirectPort_Object = MibTableColumn
atiStkSwQosPolicyRedirectPort = _AtiStkSwQosPolicyRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 11),
    _AtiStkSwQosPolicyRedirectPort_Type()
)
atiStkSwQosPolicyRedirectPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyRedirectPort.setStatus("current")
_AtiStkSwQosPolicyIngressPortList_Type = DisplayString
_AtiStkSwQosPolicyIngressPortList_Object = MibTableColumn
atiStkSwQosPolicyIngressPortList = _AtiStkSwQosPolicyIngressPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 12),
    _AtiStkSwQosPolicyIngressPortList_Type()
)
atiStkSwQosPolicyIngressPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyIngressPortList.setStatus("current")
_AtiStkSwQosPolicyEgressPortList_Type = DisplayString
_AtiStkSwQosPolicyEgressPortList_Object = MibTableColumn
atiStkSwQosPolicyEgressPortList = _AtiStkSwQosPolicyEgressPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 13),
    _AtiStkSwQosPolicyEgressPortList_Type()
)
atiStkSwQosPolicyEgressPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyEgressPortList.setStatus("current")
_AtiStkSwQosPolicyRowStatus_Type = RowStatus
_AtiStkSwQosPolicyRowStatus_Object = MibTableColumn
atiStkSwQosPolicyRowStatus = _AtiStkSwQosPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 7, 1, 14),
    _AtiStkSwQosPolicyRowStatus_Type()
)
atiStkSwQosPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atiStkSwQosPolicyRowStatus.setStatus("current")
_AtiStkSwQoSGroupPortCoSPriorityTable_Object = MibTable
atiStkSwQoSGroupPortCoSPriorityTable = _AtiStkSwQoSGroupPortCoSPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 8)
)
if mibBuilder.loadTexts:
    atiStkSwQoSGroupPortCoSPriorityTable.setStatus("current")
_AtiStkSwQoSGroupPortCoSPriorityEntry_Object = MibTableRow
atiStkSwQoSGroupPortCoSPriorityEntry = _AtiStkSwQoSGroupPortCoSPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 8, 1)
)
atiStkSwQoSGroupPortCoSPriorityEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQoSGroupPortCoSPriorityModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwQoSGroupPortCoSPriorityPortId"),
)
if mibBuilder.loadTexts:
    atiStkSwQoSGroupPortCoSPriorityEntry.setStatus("current")


class _AtiStkSwQoSGroupPortCoSPriorityModuleId_Type(Integer32):
    """Custom type atiStkSwQoSGroupPortCoSPriorityModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwQoSGroupPortCoSPriorityModuleId_Type.__name__ = "Integer32"
_AtiStkSwQoSGroupPortCoSPriorityModuleId_Object = MibTableColumn
atiStkSwQoSGroupPortCoSPriorityModuleId = _AtiStkSwQoSGroupPortCoSPriorityModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 8, 1, 1),
    _AtiStkSwQoSGroupPortCoSPriorityModuleId_Type()
)
atiStkSwQoSGroupPortCoSPriorityModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupPortCoSPriorityModuleId.setStatus("current")
_AtiStkSwQoSGroupPortCoSPriorityPortId_Type = Integer32
_AtiStkSwQoSGroupPortCoSPriorityPortId_Object = MibTableColumn
atiStkSwQoSGroupPortCoSPriorityPortId = _AtiStkSwQoSGroupPortCoSPriorityPortId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 8, 1, 2),
    _AtiStkSwQoSGroupPortCoSPriorityPortId_Type()
)
atiStkSwQoSGroupPortCoSPriorityPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupPortCoSPriorityPortId.setStatus("current")


class _AtiStkSwQoSGroupPortCoSPriorityPriority_Type(Integer32):
    """Custom type atiStkSwQoSGroupPortCoSPriorityPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AtiStkSwQoSGroupPortCoSPriorityPriority_Type.__name__ = "Integer32"
_AtiStkSwQoSGroupPortCoSPriorityPriority_Object = MibTableColumn
atiStkSwQoSGroupPortCoSPriorityPriority = _AtiStkSwQoSGroupPortCoSPriorityPriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 8, 1, 3),
    _AtiStkSwQoSGroupPortCoSPriorityPriority_Type()
)
atiStkSwQoSGroupPortCoSPriorityPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupPortCoSPriorityPriority.setStatus("current")


class _AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Type(Integer32):
    """Custom type atiStkSwQoSGroupPortCoSPriorityOverridePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Type.__name__ = "Integer32"
_AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Object = MibTableColumn
atiStkSwQoSGroupPortCoSPriorityOverridePriority = _AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 7, 8, 1, 4),
    _AtiStkSwQoSGroupPortCoSPriorityOverridePriority_Type()
)
atiStkSwQoSGroupPortCoSPriorityOverridePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwQoSGroupPortCoSPriorityOverridePriority.setStatus("current")
_AtiStkSwTrunkGroup_ObjectIdentity = ObjectIdentity
atiStkSwTrunkGroup = _AtiStkSwTrunkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8)
)
_AtiStkSwStaticTrunkTable_Object = MibTable
atiStkSwStaticTrunkTable = _AtiStkSwStaticTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1)
)
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkTable.setStatus("current")
_AtiStkSwStaticTrunkEntry_Object = MibTableRow
atiStkSwStaticTrunkEntry = _AtiStkSwStaticTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1, 1)
)
atiStkSwStaticTrunkEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwStaticTrunkModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwStaticTrunkIndex"),
)
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkEntry.setStatus("current")


class _AtiStkSwStaticTrunkModuleId_Type(Integer32):
    """Custom type atiStkSwStaticTrunkModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwStaticTrunkModuleId_Type.__name__ = "Integer32"
_AtiStkSwStaticTrunkModuleId_Object = MibTableColumn
atiStkSwStaticTrunkModuleId = _AtiStkSwStaticTrunkModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1, 1, 1),
    _AtiStkSwStaticTrunkModuleId_Type()
)
atiStkSwStaticTrunkModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkModuleId.setStatus("current")
_AtiStkSwStaticTrunkIndex_Type = Integer32
_AtiStkSwStaticTrunkIndex_Object = MibTableColumn
atiStkSwStaticTrunkIndex = _AtiStkSwStaticTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1, 1, 2),
    _AtiStkSwStaticTrunkIndex_Type()
)
atiStkSwStaticTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkIndex.setStatus("current")
_AtiStkSwStaticTrunkId_Type = Integer32
_AtiStkSwStaticTrunkId_Object = MibTableColumn
atiStkSwStaticTrunkId = _AtiStkSwStaticTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1, 1, 3),
    _AtiStkSwStaticTrunkId_Type()
)
atiStkSwStaticTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkId.setStatus("current")


class _AtiStkSwStaticTrunkName_Type(DisplayString):
    """Custom type atiStkSwStaticTrunkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AtiStkSwStaticTrunkName_Type.__name__ = "DisplayString"
_AtiStkSwStaticTrunkName_Object = MibTableColumn
atiStkSwStaticTrunkName = _AtiStkSwStaticTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1, 1, 4),
    _AtiStkSwStaticTrunkName_Type()
)
atiStkSwStaticTrunkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkName.setStatus("current")


class _AtiStkSwStaticTrunkMethod_Type(Integer32):
    """Custom type atiStkSwStaticTrunkMethod based on Integer32"""
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
        *(("srcIp", 1),
          ("dstIp", 2),
          ("src-dstIp", 3),
          ("srcMac", 4),
          ("dstMac", 5),
          ("src-dstMac", 6))
    )


_AtiStkSwStaticTrunkMethod_Type.__name__ = "Integer32"
_AtiStkSwStaticTrunkMethod_Object = MibTableColumn
atiStkSwStaticTrunkMethod = _AtiStkSwStaticTrunkMethod_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1, 1, 5),
    _AtiStkSwStaticTrunkMethod_Type()
)
atiStkSwStaticTrunkMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkMethod.setStatus("current")
_AtiStkSwStaticTrunkPortList_Type = DisplayString
_AtiStkSwStaticTrunkPortList_Object = MibTableColumn
atiStkSwStaticTrunkPortList = _AtiStkSwStaticTrunkPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1, 1, 6),
    _AtiStkSwStaticTrunkPortList_Type()
)
atiStkSwStaticTrunkPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkPortList.setStatus("current")


class _AtiStkSwStaticTrunkStatus_Type(Integer32):
    """Custom type atiStkSwStaticTrunkStatus based on Integer32"""
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


_AtiStkSwStaticTrunkStatus_Type.__name__ = "Integer32"
_AtiStkSwStaticTrunkStatus_Object = MibTableColumn
atiStkSwStaticTrunkStatus = _AtiStkSwStaticTrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1, 1, 7),
    _AtiStkSwStaticTrunkStatus_Type()
)
atiStkSwStaticTrunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkStatus.setStatus("current")
_AtiStkSwStaticTrunkRowStatus_Type = RowStatus
_AtiStkSwStaticTrunkRowStatus_Object = MibTableColumn
atiStkSwStaticTrunkRowStatus = _AtiStkSwStaticTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 8, 1, 1, 8),
    _AtiStkSwStaticTrunkRowStatus_Type()
)
atiStkSwStaticTrunkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwStaticTrunkRowStatus.setStatus("current")
_AtiStkSwACLGroup_ObjectIdentity = ObjectIdentity
atiStkSwACLGroup = _AtiStkSwACLGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9)
)
_AtiStkSwACLConfigTable_Object = MibTable
atiStkSwACLConfigTable = _AtiStkSwACLConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9, 1)
)
if mibBuilder.loadTexts:
    atiStkSwACLConfigTable.setStatus("current")
_AtiStkSwACLConfigEntry_Object = MibTableRow
atiStkSwACLConfigEntry = _AtiStkSwACLConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9, 1, 1)
)
atiStkSwACLConfigEntry.setIndexNames(
    (0, "AtiStackSwitch9424-MIB", "atiStkSwACLModuleId"),
    (0, "AtiStackSwitch9424-MIB", "atiStkSwACLId"),
)
if mibBuilder.loadTexts:
    atiStkSwACLConfigEntry.setStatus("current")


class _AtiStkSwACLModuleId_Type(Integer32):
    """Custom type atiStkSwACLModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AtiStkSwACLModuleId_Type.__name__ = "Integer32"
_AtiStkSwACLModuleId_Object = MibTableColumn
atiStkSwACLModuleId = _AtiStkSwACLModuleId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9, 1, 1, 1),
    _AtiStkSwACLModuleId_Type()
)
atiStkSwACLModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwACLModuleId.setStatus("current")


class _AtiStkSwACLId_Type(Integer32):
    """Custom type atiStkSwACLId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtiStkSwACLId_Type.__name__ = "Integer32"
_AtiStkSwACLId_Object = MibTableColumn
atiStkSwACLId = _AtiStkSwACLId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9, 1, 1, 2),
    _AtiStkSwACLId_Type()
)
atiStkSwACLId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atiStkSwACLId.setStatus("current")


class _AtiStkSwACLDescription_Type(DisplayString):
    """Custom type atiStkSwACLDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AtiStkSwACLDescription_Type.__name__ = "DisplayString"
_AtiStkSwACLDescription_Object = MibTableColumn
atiStkSwACLDescription = _AtiStkSwACLDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9, 1, 1, 3),
    _AtiStkSwACLDescription_Type()
)
atiStkSwACLDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwACLDescription.setStatus("current")


class _AtiStkSwACLAction_Type(Integer32):
    """Custom type atiStkSwACLAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_AtiStkSwACLAction_Type.__name__ = "Integer32"
_AtiStkSwACLAction_Object = MibTableColumn
atiStkSwACLAction = _AtiStkSwACLAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9, 1, 1, 4),
    _AtiStkSwACLAction_Type()
)
atiStkSwACLAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwACLAction.setStatus("current")
_AtiStkSwACLClassifierList_Type = DisplayString
_AtiStkSwACLClassifierList_Object = MibTableColumn
atiStkSwACLClassifierList = _AtiStkSwACLClassifierList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9, 1, 1, 5),
    _AtiStkSwACLClassifierList_Type()
)
atiStkSwACLClassifierList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwACLClassifierList.setStatus("current")
_AtiStkSwACLPortList_Type = DisplayString
_AtiStkSwACLPortList_Object = MibTableColumn
atiStkSwACLPortList = _AtiStkSwACLPortList_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9, 1, 1, 6),
    _AtiStkSwACLPortList_Type()
)
atiStkSwACLPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwACLPortList.setStatus("current")
_AtiStkSwACLRowStatus_Type = RowStatus
_AtiStkSwACLRowStatus_Object = MibTableColumn
atiStkSwACLRowStatus = _AtiStkSwACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 9, 1, 1, 7),
    _AtiStkSwACLRowStatus_Type()
)
atiStkSwACLRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atiStkSwACLRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

atiStkSwFanStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 1)
)
atiStkSwFanStopTrap.setObjects(
    ("AtiStackSwitch9424-MIB", "atiStkSwSysModuleId")
)
if mibBuilder.loadTexts:
    atiStkSwFanStopTrap.setStatus(
        "current"
    )

atiStkSwTemperatureAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 2)
)
atiStkSwTemperatureAbnormalTrap.setObjects(
    ("AtiStackSwitch9424-MIB", "atiStkSwSysModuleId")
)
if mibBuilder.loadTexts:
    atiStkSwTemperatureAbnormalTrap.setStatus(
        "obsolete"
    )

atiStkSwIntrusionDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 3)
)
atiStkSwIntrusionDetectionTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwIntruderAttackVlanId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwIntruderAttackMacAddr"))
)
if mibBuilder.loadTexts:
    atiStkSwIntrusionDetectionTrap.setStatus(
        "current"
    )

atiStkSwDOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 4)
)
atiStkSwDOSTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortDOSAttackType"))
)
if mibBuilder.loadTexts:
    atiStkSwDOSTrap.setStatus(
        "current"
    )

atiStkSwSTPPortStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 5)
)
atiStkSwSTPPortStateChangeTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"))
)
if mibBuilder.loadTexts:
    atiStkSwSTPPortStateChangeTrap.setStatus(
        "current"
    )

atiStkSwSTPTrunkStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 6)
)
atiStkSwSTPTrunkStateChangeTrap.setObjects(
    ("AtiStackSwitch9424-MIB", "atiStkSwSysModuleId")
)
if mibBuilder.loadTexts:
    atiStkSwSTPTrunkStateChangeTrap.setStatus(
        "current"
    )

atiStkSwSysRPSStateChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 7)
)
atiStkSwSysRPSStateChangedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwSysModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwSysRPSPresent"),
        ("AtiStackSwitch9424-MIB", "atiStkSwSysRPSState"),
        ("AtiStackSwitch9424-MIB", "atiStkSwSysDCState"))
)
if mibBuilder.loadTexts:
    atiStkSwSysRPSStateChangedTrap.setStatus(
        "current"
    )

atiStkSwMgmtDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 15)
)
atiStkSwMgmtDisabledTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwTrapVarMgmtType"),
        ("AtiStackSwitch9424-MIB", "atiStkSwTrapVarMgmtIpAddr"))
)
if mibBuilder.loadTexts:
    atiStkSwMgmtDisabledTrap.setStatus(
        "current"
    )

atiStkSwTemperatureLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 16)
)
atiStkSwTemperatureLimitTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwSysModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwSysTemperatureLimitValue"))
)
if mibBuilder.loadTexts:
    atiStkSwTemperatureLimitTrap.setStatus(
        "current"
    )

atiStkSwFanOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 17)
)
atiStkSwFanOkTrap.setObjects(
    ("AtiStackSwitch9424-MIB", "atiStkSwSysModuleId")
)
if mibBuilder.loadTexts:
    atiStkSwFanOkTrap.setStatus(
        "current"
    )

atiStkSwTemperatureNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 18)
)
atiStkSwTemperatureNormalTrap.setObjects(
    ("AtiStackSwitch9424-MIB", "atiStkSwSysModuleId")
)
if mibBuilder.loadTexts:
    atiStkSwTemperatureNormalTrap.setStatus(
        "current"
    )

atiStkSwHighRateStormDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 19)
)
atiStkSwHighRateStormDetectedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"))
)
if mibBuilder.loadTexts:
    atiStkSwHighRateStormDetectedTrap.setStatus(
        "current"
    )

atiStkSwWarningHighRateStormBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 20)
)
atiStkSwWarningHighRateStormBlockedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortStormDetectCurrentHighAction"))
)
if mibBuilder.loadTexts:
    atiStkSwWarningHighRateStormBlockedTrap.setStatus(
        "current"
    )

atiStkSwRecoverHighRateStormBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 21)
)
atiStkSwRecoverHighRateStormBlockedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"))
)
if mibBuilder.loadTexts:
    atiStkSwRecoverHighRateStormBlockedTrap.setStatus(
        "current"
    )

atiStkSwLowRateStormDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 22)
)
atiStkSwLowRateStormDetectedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"))
)
if mibBuilder.loadTexts:
    atiStkSwLowRateStormDetectedTrap.setStatus(
        "current"
    )

atiStkSwWarningLowRateStormBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 23)
)
atiStkSwWarningLowRateStormBlockedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortStormDetectCurrentLowAction"))
)
if mibBuilder.loadTexts:
    atiStkSwWarningLowRateStormBlockedTrap.setStatus(
        "current"
    )

atiStkSwRecoverLowRateStormBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 24)
)
atiStkSwRecoverLowRateStormBlockedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"))
)
if mibBuilder.loadTexts:
    atiStkSwRecoverLowRateStormBlockedTrap.setStatus(
        "current"
    )

atiStkSwStackTopologyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 25)
)
atiStkSwStackTopologyChangeTrap.setObjects(
    ("AtiStackSwitch9424-MIB", "atiStkSwSysNumOfModuleInStack")
)
if mibBuilder.loadTexts:
    atiStkSwStackTopologyChangeTrap.setStatus(
        "current"
    )

atiStkSwBPDUGuardIsTriggeredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 26)
)
atiStkSwBPDUGuardIsTriggeredTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"))
)
if mibBuilder.loadTexts:
    atiStkSwBPDUGuardIsTriggeredTrap.setStatus(
        "current"
    )

atiStkSwLoopDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 27)
)
atiStkSwLoopDetectedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortLoopDetectCurrentVlanId"))
)
if mibBuilder.loadTexts:
    atiStkSwLoopDetectedTrap.setStatus(
        "current"
    )

atiStkSwWarningLoopBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 28)
)
atiStkSwWarningLoopBlockedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortLoopDetectCurrentAction"))
)
if mibBuilder.loadTexts:
    atiStkSwWarningLoopBlockedTrap.setStatus(
        "current"
    )

atiStkSwRecoverLoopBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 17, 6, 29)
)
atiStkSwRecoverLoopBlockedTrap.setObjects(
      *(("AtiStackSwitch9424-MIB", "atiStkSwModuleId"),
        ("AtiStackSwitch9424-MIB", "atiStkSwPortId"))
)
if mibBuilder.loadTexts:
    atiStkSwRecoverLoopBlockedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AtiStackSwitch9424-MIB",
    **{"AtiProductType": AtiProductType,
       "AtiPortType": AtiPortType,
       "AtiUplinkType": AtiUplinkType,
       "alliedTelesyn": alliedTelesyn,
       "atiProduct": atiProduct,
       "swhub": swhub,
       "at-8324": at_8324,
       "at-8316F": at_8316F,
       "at-8524M": at_8524M,
       "at-8550GB": at_8550GB,
       "at-8516F": at_8516F,
       "at-8550SP": at_8550SP,
       "at-9424T-SP": at_9424T_SP,
       "at-9424T-GB": at_9424T_GB,
       "at-8524POE": at_8524POE,
       "at-9408LC-SP": at_9408LC_SP,
       "at-9424Ti-SP": at_9424Ti_SP,
       "at-9448Ts-XP": at_9448Ts_XP,
       "at-9448Ts": at_9448Ts,
       "at-9448T-SP": at_9448T_SP,
       "at-9424Ts-XP": at_9424Ts_XP,
       "at-9424Ts": at_9424Ts,
       "at-9424T": at_9424T,
       "at-9424TPOE": at_9424TPOE,
       "at-9424TL": at_9424TL,
       "mibObject": mibObject,
       "atiStkSwMib": atiStkSwMib,
       "atiStkSwSysGroup": atiStkSwSysGroup,
       "atiStkSwSysConfig": atiStkSwSysConfig,
       "atiStkSwSysReset": atiStkSwSysReset,
       "atiStkSwSysIpAddress": atiStkSwSysIpAddress,
       "atiStkSwSysSubnetMask": atiStkSwSysSubnetMask,
       "atiStkSwSysGateway": atiStkSwSysGateway,
       "atiStkSwSysIpAddressStatus": atiStkSwSysIpAddressStatus,
       "atiStkSwSysDnsServer": atiStkSwSysDnsServer,
       "atiStkSwSysDefaultDomainName": atiStkSwSysDefaultDomainName,
       "atiStkSwSysNumberOfModules": atiStkSwSysNumberOfModules,
       "atiStkSwSysSpanningTreeStatus": atiStkSwSysSpanningTreeStatus,
       "atiStkSwSysSpanningTreeVersion": atiStkSwSysSpanningTreeVersion,
       "atiStkSwSysAction": atiStkSwSysAction,
       "atiStkSwSysNumOfModuleInStack": atiStkSwSysNumOfModuleInStack,
       "atiStkSwSysNwMgmt": atiStkSwSysNwMgmt,
       "atiStkSwSysTrapRecv1": atiStkSwSysTrapRecv1,
       "atiStkSwSysTrapRecv2": atiStkSwSysTrapRecv2,
       "atiStkSwSysTrapRecv3": atiStkSwSysTrapRecv3,
       "atiStkSwSysTrapRecv4": atiStkSwSysTrapRecv4,
       "atiStkSwSysProductInfoTable": atiStkSwSysProductInfoTable,
       "atiStkSwSysProductInfoEntry": atiStkSwSysProductInfoEntry,
       "atiStkSwSysModuleId": atiStkSwSysModuleId,
       "atiStkSwSysProductType": atiStkSwSysProductType,
       "atiStkSwSysMacAddress": atiStkSwSysMacAddress,
       "atiStkSwSysSwName": atiStkSwSysSwName,
       "atiStkSwSysSwVersion": atiStkSwSysSwVersion,
       "atiStkSwSysHwName": atiStkSwSysHwName,
       "atiStkSwSysHwRevision": atiStkSwSysHwRevision,
       "atiStkSwSysSerialNumber": atiStkSwSysSerialNumber,
       "atiStkSwSysTotalPortCount": atiStkSwSysTotalPortCount,
       "atiStkSwSysBasePortType": atiStkSwSysBasePortType,
       "atiStkSwSysBasePortCount": atiStkSwSysBasePortCount,
       "atiStkSwSysUplinkAModelName": atiStkSwSysUplinkAModelName,
       "atiStkSwSysUplinkAPortType": atiStkSwSysUplinkAPortType,
       "atiStkSwSysUplinkAPortCount": atiStkSwSysUplinkAPortCount,
       "atiStkSwSysUplinkAPortIdBase": atiStkSwSysUplinkAPortIdBase,
       "atiStkSwSysUplinkAPortIdLimit": atiStkSwSysUplinkAPortIdLimit,
       "atiStkSwSysUplinkBModelName": atiStkSwSysUplinkBModelName,
       "atiStkSwSysUplinkBPortType": atiStkSwSysUplinkBPortType,
       "atiStkSwSysUplinkBPortCount": atiStkSwSysUplinkBPortCount,
       "atiStkSwSysUplinkBPortIdBase": atiStkSwSysUplinkBPortIdBase,
       "atiStkSwSysUplinkBPortIdLimit": atiStkSwSysUplinkBPortIdLimit,
       "atiStkSwSysRPSPresent": atiStkSwSysRPSPresent,
       "atiStkSwSysRPSState": atiStkSwSysRPSState,
       "atiStkSwSysDCState": atiStkSwSysDCState,
       "atiStkSwSysTemperatureLimitValue": atiStkSwSysTemperatureLimitValue,
       "atiStkSwSysUplinkInfoTable": atiStkSwSysUplinkInfoTable,
       "atiStkSwSysUplinkInfoEntry": atiStkSwSysUplinkInfoEntry,
       "atiStkSwSysUplinkModuleId": atiStkSwSysUplinkModuleId,
       "atiStkSwSysUplinkPortId": atiStkSwSysUplinkPortId,
       "atiStkSwSysUplinkSetup": atiStkSwSysUplinkSetup,
       "atiStkSwSysUplinkType": atiStkSwSysUplinkType,
       "atiStkSwSysUplinkDetails": atiStkSwSysUplinkDetails,
       "atiStkSwSysUplinkPortType": atiStkSwSysUplinkPortType,
       "atiStkSwSysSystemTimeConfig": atiStkSwSysSystemTimeConfig,
       "atiStkSwSysCurrentTime": atiStkSwSysCurrentTime,
       "atiStkSwSysCurrentDate": atiStkSwSysCurrentDate,
       "atiStkSwSysSNTPStatus": atiStkSwSysSNTPStatus,
       "atiStkSwSysSNTPServerIPAddress": atiStkSwSysSNTPServerIPAddress,
       "atiStkSwSysSNTPUTCOffset": atiStkSwSysSNTPUTCOffset,
       "atiStkSwSysSNTPDSTStatus": atiStkSwSysSNTPDSTStatus,
       "atiStkSwSysSNTPPollingInterval": atiStkSwSysSNTPPollingInterval,
       "atiStkSwSysSNTPLastDelta": atiStkSwSysSNTPLastDelta,
       "atiStkSwSysInfoGroup": atiStkSwSysInfoGroup,
       "atiStkSwTemperatureInfoTable": atiStkSwTemperatureInfoTable,
       "atiStkSwTemperatureInfoEntry": atiStkSwTemperatureInfoEntry,
       "atiStkSwTemperatureInfoModuleId": atiStkSwTemperatureInfoModuleId,
       "atiStkSwTemperatureInfoTemperature": atiStkSwTemperatureInfoTemperature,
       "atiStkSwFanInfoTable": atiStkSwFanInfoTable,
       "atiStkSwFanInfoEntry": atiStkSwFanInfoEntry,
       "atiStkSwFanInfoModuleId": atiStkSwFanInfoModuleId,
       "atiStkSwFanInfoFanId": atiStkSwFanInfoFanId,
       "atiStkSwFanInfoState": atiStkSwFanInfoState,
       "atiStkSwFanInfoSpeed": atiStkSwFanInfoSpeed,
       "atiStkSwVoltageInfoTable": atiStkSwVoltageInfoTable,
       "atiStkSwVoltageInfoEntry": atiStkSwVoltageInfoEntry,
       "atiStkSwVoltageInfoModuleId": atiStkSwVoltageInfoModuleId,
       "atiStkSwVoltageInfoIndex": atiStkSwVoltageInfoIndex,
       "atiStkSwVoltageInfoLevel": atiStkSwVoltageInfoLevel,
       "atiStkSwVoltageInfoMeasured": atiStkSwVoltageInfoMeasured,
       "atiStkSwCPUInfoTable": atiStkSwCPUInfoTable,
       "atiStkSwCPUInfoEntry": atiStkSwCPUInfoEntry,
       "atiStkSwCPUInfoModuleId": atiStkSwCPUInfoModuleId,
       "atiStkSwCPUInfoAvgLastMinute": atiStkSwCPUInfoAvgLastMinute,
       "atiStkSwCPUInfoAvgLast20Seconds": atiStkSwCPUInfoAvgLast20Seconds,
       "atiStkSwCPUInfoAvgSecond": atiStkSwCPUInfoAvgSecond,
       "atiStkSwMemoryGroup": atiStkSwMemoryGroup,
       "atiStkSwMemoryInfoTable": atiStkSwMemoryInfoTable,
       "atiStkSwMemoryInfoEntry": atiStkSwMemoryInfoEntry,
       "atiStkSwMemoryInfoModuleId": atiStkSwMemoryInfoModuleId,
       "atiStkSwMemoryInfoTotalBuffers": atiStkSwMemoryInfoTotalBuffers,
       "atiStkSwMemoryPoolTable": atiStkSwMemoryPoolTable,
       "atiStkSwMemoryPoolEntry": atiStkSwMemoryPoolEntry,
       "atiStkSwMemoryPoolModuleId": atiStkSwMemoryPoolModuleId,
       "atiStkSwMemoryPoolIndex": atiStkSwMemoryPoolIndex,
       "atiStkSwMemoryPoolName": atiStkSwMemoryPoolName,
       "atiStkSwMemoryPoolTotal": atiStkSwMemoryPoolTotal,
       "atiStkSwMemoryPoolFree": atiStkSwMemoryPoolFree,
       "atiStkSwMemoryComBuffersTable": atiStkSwMemoryComBuffersTable,
       "atiStkSwMemoryComBuffersEntry": atiStkSwMemoryComBuffersEntry,
       "atiStkSwMemoryComBuffersModuleId": atiStkSwMemoryComBuffersModuleId,
       "atiStkSwMemoryTotalComBuffers": atiStkSwMemoryTotalComBuffers,
       "atiStkSwMemoryFreeComBuffers": atiStkSwMemoryFreeComBuffers,
       "atiStkSwSysMgmtACLGroup": atiStkSwSysMgmtACLGroup,
       "atiStkSwSysMgmtACLStatus": atiStkSwSysMgmtACLStatus,
       "atiStkSwSysMgmtACLConfigTable": atiStkSwSysMgmtACLConfigTable,
       "atiStkSwSysMgmtACLConfigEntry": atiStkSwSysMgmtACLConfigEntry,
       "atiStkSwSysMgmtACLConfigModuleId": atiStkSwSysMgmtACLConfigModuleId,
       "atiStkSwSysMgmtACLConfigId": atiStkSwSysMgmtACLConfigId,
       "atiStkSwSysMgmtACLConfigIpAddr": atiStkSwSysMgmtACLConfigIpAddr,
       "atiStkSwSysMgmtACLConfigMask": atiStkSwSysMgmtACLConfigMask,
       "atiStkSwSysMgmtACLConfigApplication": atiStkSwSysMgmtACLConfigApplication,
       "atiStkSwSysMgmtACLConfigRowStatus": atiStkSwSysMgmtACLConfigRowStatus,
       "atiStkSwPortGroup": atiStkSwPortGroup,
       "atiStkSwPortConfigTable": atiStkSwPortConfigTable,
       "atiStkSwPortConfigEntry": atiStkSwPortConfigEntry,
       "atiStkSwModuleId": atiStkSwModuleId,
       "atiStkSwPortId": atiStkSwPortId,
       "atiStkSwPortName": atiStkSwPortName,
       "atiStkSwPortState": atiStkSwPortState,
       "atiStkSwPortLinkState": atiStkSwPortLinkState,
       "atiStkSwPortNegotiation": atiStkSwPortNegotiation,
       "atiStkSwPortSpeed": atiStkSwPortSpeed,
       "atiStkSwPortDuplexStatus": atiStkSwPortDuplexStatus,
       "atiStkSwPortFlowControl": atiStkSwPortFlowControl,
       "atiStkSwPortBackPressure": atiStkSwPortBackPressure,
       "atiStkSwPortPriority": atiStkSwPortPriority,
       "atiStkSwPortBroadcastProcessing": atiStkSwPortBroadcastProcessing,
       "atiStkSwPortMDIO": atiStkSwPortMDIO,
       "atiStkSwPortHOLLimit": atiStkSwPortHOLLimit,
       "atiStkSwPortBackPressureLimit": atiStkSwPortBackPressureLimit,
       "atiStkSwPortSTPState": atiStkSwPortSTPState,
       "atiStkSwPortMirroringConfig": atiStkSwPortMirroringConfig,
       "atiStkSwPortMirroringState": atiStkSwPortMirroringState,
       "atiStkSwPortMirroringSourceModuleId": atiStkSwPortMirroringSourceModuleId,
       "atiStkSwPortMirroringSourcePortId": atiStkSwPortMirroringSourcePortId,
       "atiStkSwPortMirroringDestinationModuleId": atiStkSwPortMirroringDestinationModuleId,
       "atiStkSwPortMirroringDestinationPortId": atiStkSwPortMirroringDestinationPortId,
       "atiStkSwPortMirroringSourceRxList": atiStkSwPortMirroringSourceRxList,
       "atiStkSwPortMirroringSourceTxList": atiStkSwPortMirroringSourceTxList,
       "atiStkSwPortSecurityConfig": atiStkSwPortSecurityConfig,
       "atiStkSwPortSecurityMode": atiStkSwPortSecurityMode,
       "atiStkSwPortIntrusionDetectionTable": atiStkSwPortIntrusionDetectionTable,
       "atiStkSwPortIntrusionDetectionEntry": atiStkSwPortIntrusionDetectionEntry,
       "atiStkSwPortIntrusionDetectionAction": atiStkSwPortIntrusionDetectionAction,
       "atiStkSwPortIntrusionDetectionPortList": atiStkSwPortIntrusionDetectionPortList,
       "atiStkPortSecurityConfigTable": atiStkPortSecurityConfigTable,
       "atiStkPortSecurityConfigEntry": atiStkPortSecurityConfigEntry,
       "atiStkPortSecurityMode": atiStkPortSecurityMode,
       "atiStkPortSecurityThreshold": atiStkPortSecurityThreshold,
       "atiStkPortIntrusionAction": atiStkPortIntrusionAction,
       "atiStkPortIntrusionActionStatus": atiStkPortIntrusionActionStatus,
       "atiStkDOSConfig": atiStkDOSConfig,
       "atiStkDOSConfigLANIpAddress": atiStkDOSConfigLANIpAddress,
       "atiStkDOSConfigLANSubnetMask": atiStkDOSConfigLANSubnetMask,
       "atiStkPortDOSAttackConfigTable": atiStkPortDOSAttackConfigTable,
       "atiStkPortDOSAttackConfigEntry": atiStkPortDOSAttackConfigEntry,
       "atiStkSwPortDOSAttackType": atiStkSwPortDOSAttackType,
       "atiStkSwPortDOSAttackActionStatus": atiStkSwPortDOSAttackActionStatus,
       "atiStkSwPortDOSAttackMirrorPort": atiStkSwPortDOSAttackMirrorPort,
       "atiStkSwPortDOSAttackMirrorPortStatus": atiStkSwPortDOSAttackMirrorPortStatus,
       "atiStkSwIntrusionAttackTable": atiStkSwIntrusionAttackTable,
       "atiStkSwIntrusionAttackEntry": atiStkSwIntrusionAttackEntry,
       "atiStkSwIntruderAttackVlanId": atiStkSwIntruderAttackVlanId,
       "atiStkSwIntruderAttackMacAddr": atiStkSwIntruderAttackMacAddr,
       "atiStkSwPortStormDetectCurrentTable": atiStkSwPortStormDetectCurrentTable,
       "atiStkSwPortStormDetectCurrentEntry": atiStkSwPortStormDetectCurrentEntry,
       "atiStkSwPortStormDetectCurrentHighStatus": atiStkSwPortStormDetectCurrentHighStatus,
       "atiStkSwPortStormDetectCurrentHighAction": atiStkSwPortStormDetectCurrentHighAction,
       "atiStkSwPortStormDetectCurrentHighExpiry": atiStkSwPortStormDetectCurrentHighExpiry,
       "atiStkSwPortStormDetectCurrentLowStatus": atiStkSwPortStormDetectCurrentLowStatus,
       "atiStkSwPortStormDetectCurrentLowAction": atiStkSwPortStormDetectCurrentLowAction,
       "atiStkSwPortStormDetectCurrentLowExpiry": atiStkSwPortStormDetectCurrentLowExpiry,
       "atiStkSwPortLoopDetectCurrentTable": atiStkSwPortLoopDetectCurrentTable,
       "atiStkSwPortLoopDetectCurrentEntry": atiStkSwPortLoopDetectCurrentEntry,
       "atiStkSwPortLoopDetectCurrentStatus": atiStkSwPortLoopDetectCurrentStatus,
       "atiStkSwPortLoopDetectCurrentAction": atiStkSwPortLoopDetectCurrentAction,
       "atiStkSwPortLoopDetectCurrentExpiry": atiStkSwPortLoopDetectCurrentExpiry,
       "atiStkSwPortLoopDetectCurrentVlanId": atiStkSwPortLoopDetectCurrentVlanId,
       "atiStkSwVlanGroup": atiStkSwVlanGroup,
       "atiStkSwVlanConfigTable": atiStkSwVlanConfigTable,
       "atiStkSwVlanConfigEntry": atiStkSwVlanConfigEntry,
       "atiStkSwVlanId": atiStkSwVlanId,
       "atiStkSwVlanName": atiStkSwVlanName,
       "atiStkSwVlanTaggedPortListModule1": atiStkSwVlanTaggedPortListModule1,
       "atiStkSwVlanUntaggedPortListModule1": atiStkSwVlanUntaggedPortListModule1,
       "atiStkSwVlanTaggedPortListModule2": atiStkSwVlanTaggedPortListModule2,
       "atiStkSwVlanUntaggedPortListModule2": atiStkSwVlanUntaggedPortListModule2,
       "atiStkSwVlanTaggedPortListModule3": atiStkSwVlanTaggedPortListModule3,
       "atiStkSwVlanUntaggedPortListModule3": atiStkSwVlanUntaggedPortListModule3,
       "atiStkSwVlanTaggedPortListModule4": atiStkSwVlanTaggedPortListModule4,
       "atiStkSwVlanUntaggedPortListModule4": atiStkSwVlanUntaggedPortListModule4,
       "atiStkSwVlanTaggedPortListModule5": atiStkSwVlanTaggedPortListModule5,
       "atiStkSwVlanUntaggedPortListModule5": atiStkSwVlanUntaggedPortListModule5,
       "atiStkSwVlanTaggedPortListModule6": atiStkSwVlanTaggedPortListModule6,
       "atiStkSwVlanUntaggedPortListModule6": atiStkSwVlanUntaggedPortListModule6,
       "atiStkSwVlanTaggedPortListModule7": atiStkSwVlanTaggedPortListModule7,
       "atiStkSwVlanUntaggedPortListModule7": atiStkSwVlanUntaggedPortListModule7,
       "atiStkSwVlanTaggedPortListModule8": atiStkSwVlanTaggedPortListModule8,
       "atiStkSwVlanUntaggedPortListModule8": atiStkSwVlanUntaggedPortListModule8,
       "atiStkSwVlanConfigEntryStatus": atiStkSwVlanConfigEntryStatus,
       "atiStkSwVlanActualUntaggedPortListModule1": atiStkSwVlanActualUntaggedPortListModule1,
       "atiStkSwPort2VlanTable": atiStkSwPort2VlanTable,
       "atiStkSwPort2VlanEntry": atiStkSwPort2VlanEntry,
       "atiStkSwPortVlanId": atiStkSwPortVlanId,
       "atiStkSwPortVlanName": atiStkSwPortVlanName,
       "atiStkSwMacAddr2VlanTable": atiStkSwMacAddr2VlanTable,
       "atiStkSwMacAddr2VlanEntry": atiStkSwMacAddr2VlanEntry,
       "atiStkSwMacAddress": atiStkSwMacAddress,
       "atiStkSwMacAddrVlanId": atiStkSwMacAddrVlanId,
       "atiStkSwMacAddrVlanName": atiStkSwMacAddrVlanName,
       "atiStkSwMacAddrModuleId": atiStkSwMacAddrModuleId,
       "atiStkSwMacAddrPortId": atiStkSwMacAddrPortId,
       "atiStkSwMacAddrPortList": atiStkSwMacAddrPortList,
       "atiStkSwVlanMode": atiStkSwVlanMode,
       "atiStkSwVlanUplinkVlanPort": atiStkSwVlanUplinkVlanPort,
       "atiStkSwGVRPConfig": atiStkSwGVRPConfig,
       "atiStkSwGVRPStatus": atiStkSwGVRPStatus,
       "atiStkSwGVRPGIPStatus": atiStkSwGVRPGIPStatus,
       "atiStkSwGVRPJoinTimer": atiStkSwGVRPJoinTimer,
       "atiStkSwGVRPLeaveTimer": atiStkSwGVRPLeaveTimer,
       "atiStkSwGVRPLeaveAllTimer": atiStkSwGVRPLeaveAllTimer,
       "atiStkSwGVRPPortConfigTable": atiStkSwGVRPPortConfigTable,
       "atiStkSwGVRPPortConfigEntry": atiStkSwGVRPPortConfigEntry,
       "atiStkSwGVRPPortConfigModuleId": atiStkSwGVRPPortConfigModuleId,
       "atiStkSwGVRPPortConfigPortId": atiStkSwGVRPPortConfigPortId,
       "atiStkSwGVRPPortConfigStatus": atiStkSwGVRPPortConfigStatus,
       "atiStkSwGVRPCountersTable": atiStkSwGVRPCountersTable,
       "atiStkSwGVRPCountersEntry": atiStkSwGVRPCountersEntry,
       "atiStkSwGVRPCountersModuleId": atiStkSwGVRPCountersModuleId,
       "atiStkSwGVRPCountersGARPRxPkt": atiStkSwGVRPCountersGARPRxPkt,
       "atiStkSwGVRPCountersInvalidGARPRxPkt": atiStkSwGVRPCountersInvalidGARPRxPkt,
       "atiStkSwGVRPCountersGARPTxPkt": atiStkSwGVRPCountersGARPTxPkt,
       "atiStkSwGVRPCountersGARPTxDisabled": atiStkSwGVRPCountersGARPTxDisabled,
       "atiStkSwGVRPCountersPortNotSending": atiStkSwGVRPCountersPortNotSending,
       "atiStkSwGVRPCountersGARPDisabled": atiStkSwGVRPCountersGARPDisabled,
       "atiStkSwGVRPCountersPortNotListening": atiStkSwGVRPCountersPortNotListening,
       "atiStkSwGVRPCountersInvalidPort": atiStkSwGVRPCountersInvalidPort,
       "atiStkSwGVRPCountersInvalidProtocol": atiStkSwGVRPCountersInvalidProtocol,
       "atiStkSwGVRPCountersInvalidFormat": atiStkSwGVRPCountersInvalidFormat,
       "atiStkSwGVRPCountersDatabaseFull": atiStkSwGVRPCountersDatabaseFull,
       "atiStkSwGVRPCountersRxMsgLeaveAll": atiStkSwGVRPCountersRxMsgLeaveAll,
       "atiStkSwGVRPCountersRxMsgJoinEmpty": atiStkSwGVRPCountersRxMsgJoinEmpty,
       "atiStkSwGVRPCountersRxMsgJoinIn": atiStkSwGVRPCountersRxMsgJoinIn,
       "atiStkSwGVRPCountersRxMsgLeaveEmpty": atiStkSwGVRPCountersRxMsgLeaveEmpty,
       "atiStkSwGVRPCountersRxMsgLeaveIn": atiStkSwGVRPCountersRxMsgLeaveIn,
       "atiStkSwGVRPCountersRxMsgEmpty": atiStkSwGVRPCountersRxMsgEmpty,
       "atiStkSwGVRPCountersRxMsgBadMsg": atiStkSwGVRPCountersRxMsgBadMsg,
       "atiStkSwGVRPCountersRxMsgBadAttribute": atiStkSwGVRPCountersRxMsgBadAttribute,
       "atiStkSwGVRPCountersTxMsgLeaveAll": atiStkSwGVRPCountersTxMsgLeaveAll,
       "atiStkSwGVRPCountersTxMsgJoinEmpty": atiStkSwGVRPCountersTxMsgJoinEmpty,
       "atiStkSwGVRPCountersTxMsgJoinIn": atiStkSwGVRPCountersTxMsgJoinIn,
       "atiStkSwGVRPCountersTxMsgLeaveEmpty": atiStkSwGVRPCountersTxMsgLeaveEmpty,
       "atiStkSwGVRPCountersTxMsgLeaveIn": atiStkSwGVRPCountersTxMsgLeaveIn,
       "atiStkSwGVRPCountersTxMsgEmpty": atiStkSwGVRPCountersTxMsgEmpty,
       "atiStkSwMacAddrGroup": atiStkSwMacAddrGroup,
       "atiStkSwStaticMacAddrTable": atiStkSwStaticMacAddrTable,
       "atiStkSwStaticMacAddrEntry": atiStkSwStaticMacAddrEntry,
       "atiStkSwStaticMacAddress": atiStkSwStaticMacAddress,
       "atiStkSwStaticMacAddrVlanId": atiStkSwStaticMacAddrVlanId,
       "atiStkSwStaticMacAddrModuleId": atiStkSwStaticMacAddrModuleId,
       "atiStkSwStaticMacAddrPortId": atiStkSwStaticMacAddrPortId,
       "atiStkSwStaticMacAddrPortList": atiStkSwStaticMacAddrPortList,
       "atiStkSwStaticMacAddrEntryStatus": atiStkSwStaticMacAddrEntryStatus,
       "atiStkSwEthStatsGroup": atiStkSwEthStatsGroup,
       "atiStkSwEthModuleMonTable": atiStkSwEthModuleMonTable,
       "atiStkSwEthModuleMonEntry": atiStkSwEthModuleMonEntry,
       "atiStkSwEthModuleMonTxGoodFrames": atiStkSwEthModuleMonTxGoodFrames,
       "atiStkSwEthModuleMonRxGoodFrames": atiStkSwEthModuleMonRxGoodFrames,
       "atiStkSwEthModuleMonTxTotalBytes": atiStkSwEthModuleMonTxTotalBytes,
       "atiStkSwEthModuleMonTxBroadcastFrames": atiStkSwEthModuleMonTxBroadcastFrames,
       "atiStkSwEthModuleMonTxMulticastFrames": atiStkSwEthModuleMonTxMulticastFrames,
       "atiStkSwEthModuleMonRxOverrunFrames": atiStkSwEthModuleMonRxOverrunFrames,
       "atiStkSwEthModuleErrTable": atiStkSwEthModuleErrTable,
       "atiStkSwEthModuleErrEntry": atiStkSwEthModuleErrEntry,
       "atiStkSwEthModuleErrRxCRC": atiStkSwEthModuleErrRxCRC,
       "atiStkSwEthModuleErrRxBadFrames": atiStkSwEthModuleErrRxBadFrames,
       "atiStkSwEthModuleErrCollisions": atiStkSwEthModuleErrCollisions,
       "atiStkSwEthPortMonTable": atiStkSwEthPortMonTable,
       "atiStkSwEthPortMonEntry": atiStkSwEthPortMonEntry,
       "atiStkSwEthPortMonTxGoodFrames": atiStkSwEthPortMonTxGoodFrames,
       "atiStkSwEthPortMonRxGoodFrames": atiStkSwEthPortMonRxGoodFrames,
       "atiStkSwEthPortMonTxTotalBytes": atiStkSwEthPortMonTxTotalBytes,
       "atiStkSwEthPortMonTxBroadcastFrames": atiStkSwEthPortMonTxBroadcastFrames,
       "atiStkSwEthPortMonTxMulticastFrames": atiStkSwEthPortMonTxMulticastFrames,
       "atiStkSwEthPortMonRxOverrunFrames": atiStkSwEthPortMonRxOverrunFrames,
       "atiStkSwEthPortErrTable": atiStkSwEthPortErrTable,
       "atiStkSwEthPortErrEntry": atiStkSwEthPortErrEntry,
       "atiStkSwEthPortErrRxBadFrames": atiStkSwEthPortErrRxBadFrames,
       "atiStkSwEthPortErrCollisions": atiStkSwEthPortErrCollisions,
       "atiStkSwTrapsGroup": atiStkSwTrapsGroup,
       "atiStkSwFanStopTrap": atiStkSwFanStopTrap,
       "atiStkSwTemperatureAbnormalTrap": atiStkSwTemperatureAbnormalTrap,
       "atiStkSwIntrusionDetectionTrap": atiStkSwIntrusionDetectionTrap,
       "atiStkSwDOSTrap": atiStkSwDOSTrap,
       "atiStkSwSTPPortStateChangeTrap": atiStkSwSTPPortStateChangeTrap,
       "atiStkSwSTPTrunkStateChangeTrap": atiStkSwSTPTrunkStateChangeTrap,
       "atiStkSwSysRPSStateChangedTrap": atiStkSwSysRPSStateChangedTrap,
       "atiStkSwTrapVarMgmtType": atiStkSwTrapVarMgmtType,
       "atiStkSwTrapVarMgmtIpAddr": atiStkSwTrapVarMgmtIpAddr,
       "atiStkSwMgmtDisabledTrap": atiStkSwMgmtDisabledTrap,
       "atiStkSwTemperatureLimitTrap": atiStkSwTemperatureLimitTrap,
       "atiStkSwFanOkTrap": atiStkSwFanOkTrap,
       "atiStkSwTemperatureNormalTrap": atiStkSwTemperatureNormalTrap,
       "atiStkSwHighRateStormDetectedTrap": atiStkSwHighRateStormDetectedTrap,
       "atiStkSwWarningHighRateStormBlockedTrap": atiStkSwWarningHighRateStormBlockedTrap,
       "atiStkSwRecoverHighRateStormBlockedTrap": atiStkSwRecoverHighRateStormBlockedTrap,
       "atiStkSwLowRateStormDetectedTrap": atiStkSwLowRateStormDetectedTrap,
       "atiStkSwWarningLowRateStormBlockedTrap": atiStkSwWarningLowRateStormBlockedTrap,
       "atiStkSwRecoverLowRateStormBlockedTrap": atiStkSwRecoverLowRateStormBlockedTrap,
       "atiStkSwStackTopologyChangeTrap": atiStkSwStackTopologyChangeTrap,
       "atiStkSwBPDUGuardIsTriggeredTrap": atiStkSwBPDUGuardIsTriggeredTrap,
       "atiStkSwLoopDetectedTrap": atiStkSwLoopDetectedTrap,
       "atiStkSwWarningLoopBlockedTrap": atiStkSwWarningLoopBlockedTrap,
       "atiStkSwRecoverLoopBlockedTrap": atiStkSwRecoverLoopBlockedTrap,
       "atiStkSwQoSGroup": atiStkSwQoSGroup,
       "atiStkSwQoSGroupNumberOfQueues": atiStkSwQoSGroupNumberOfQueues,
       "atiStkSwQoSGroupSchedulingMode": atiStkSwQoSGroupSchedulingMode,
       "atiStkSwQoSGroupCoSToQueueTable": atiStkSwQoSGroupCoSToQueueTable,
       "atiStkSwQoSGroupCoSToQueueEntry": atiStkSwQoSGroupCoSToQueueEntry,
       "atiStkSwQoSGroupCoSPriority": atiStkSwQoSGroupCoSPriority,
       "atiStkSwQoSGroupCoSQueue": atiStkSwQoSGroupCoSQueue,
       "atiStkSwQoSGroupQueueToWeightTable": atiStkSwQoSGroupQueueToWeightTable,
       "atiStkSwQoSGroupQueueToWeightEntry": atiStkSwQoSGroupQueueToWeightEntry,
       "atiStkSwQoSGroupQueue": atiStkSwQoSGroupQueue,
       "atiStkSwQoSGroupQueueWeight": atiStkSwQoSGroupQueueWeight,
       "atiStkSwQosFlowGrpTable": atiStkSwQosFlowGrpTable,
       "atiStkSwQosFlowGrpEntry": atiStkSwQosFlowGrpEntry,
       "atiStkSwQosFlowGrpModuleId": atiStkSwQosFlowGrpModuleId,
       "atiStkSwQosFlowGrpId": atiStkSwQosFlowGrpId,
       "atiStkSwQosFlowGrpDescription": atiStkSwQosFlowGrpDescription,
       "atiStkSwQosFlowGrpDSCPValue": atiStkSwQosFlowGrpDSCPValue,
       "atiStkSwQosFlowGrpPriority": atiStkSwQosFlowGrpPriority,
       "atiStkSwQosFlowGrpRemarkPriority": atiStkSwQosFlowGrpRemarkPriority,
       "atiStkSwQosFlowGrpTos": atiStkSwQosFlowGrpTos,
       "atiStkSwQosFlowGrpTosToPriority": atiStkSwQosFlowGrpTosToPriority,
       "atiStkSwQosFlowGrpPriorityToTos": atiStkSwQosFlowGrpPriorityToTos,
       "atiStkSwQosFlowGrpClassifierList": atiStkSwQosFlowGrpClassifierList,
       "atiStkSwQosFlowGrpRowStatus": atiStkSwQosFlowGrpRowStatus,
       "atiStkSwQosTrafficClassTable": atiStkSwQosTrafficClassTable,
       "atiStkSwQosTrafficClassEntry": atiStkSwQosTrafficClassEntry,
       "atiStkSwQosTrafficClassModuleId": atiStkSwQosTrafficClassModuleId,
       "atiStkSwQosTrafficClassId": atiStkSwQosTrafficClassId,
       "atiStkSwQosTrafficClassDescription": atiStkSwQosTrafficClassDescription,
       "atiStkSwQosTrafficClassExceedAction": atiStkSwQosTrafficClassExceedAction,
       "atiStkSwQosTrafficClassExceedRemarkValue": atiStkSwQosTrafficClassExceedRemarkValue,
       "atiStkSwQosTrafficClassDSCPValue": atiStkSwQosTrafficClassDSCPValue,
       "atiStkSwQosTrafficClassMaxBandwidth": atiStkSwQosTrafficClassMaxBandwidth,
       "atiStkSwQosTrafficClassBurstSize": atiStkSwQosTrafficClassBurstSize,
       "atiStkSwQosTrafficClassPriority": atiStkSwQosTrafficClassPriority,
       "atiStkSwQosTrafficClassRemarkPriority": atiStkSwQosTrafficClassRemarkPriority,
       "atiStkSwQosTrafficClassToS": atiStkSwQosTrafficClassToS,
       "atiStkSwQosTrafficClassMoveToSToPriority": atiStkSwQosTrafficClassMoveToSToPriority,
       "atiStkSwQosTrafficClassMovePriorityToToS": atiStkSwQosTrafficClassMovePriorityToToS,
       "atiStkSwQosTrafficClassFlowGroupList": atiStkSwQosTrafficClassFlowGroupList,
       "atiStkSwQosTrafficClassRowStatus": atiStkSwQosTrafficClassRowStatus,
       "atiStkSwQosPolicyTable": atiStkSwQosPolicyTable,
       "atiStkSwQosPolicyEntry": atiStkSwQosPolicyEntry,
       "atiStkSwQosPolicyModuleId": atiStkSwQosPolicyModuleId,
       "atiStkSwQosPolicyId": atiStkSwQosPolicyId,
       "atiStkSwQosPolicyDescription": atiStkSwQosPolicyDescription,
       "atiStkSwQosPolicyRemarkDSCP": atiStkSwQosPolicyRemarkDSCP,
       "atiStkSwQosPolicyDSCPValue": atiStkSwQosPolicyDSCPValue,
       "atiStkSwQosPolicyToS": atiStkSwQosPolicyToS,
       "atiStkSwQosPolicyMoveToSToPriority": atiStkSwQosPolicyMoveToSToPriority,
       "atiStkSwQosPolicyMovePriorityToToS": atiStkSwQosPolicyMovePriorityToToS,
       "atiStkSwQosPolicySendToMirrorPort": atiStkSwQosPolicySendToMirrorPort,
       "atiStkSwQosPolicyTrafficClassList": atiStkSwQosPolicyTrafficClassList,
       "atiStkSwQosPolicyRedirectPort": atiStkSwQosPolicyRedirectPort,
       "atiStkSwQosPolicyIngressPortList": atiStkSwQosPolicyIngressPortList,
       "atiStkSwQosPolicyEgressPortList": atiStkSwQosPolicyEgressPortList,
       "atiStkSwQosPolicyRowStatus": atiStkSwQosPolicyRowStatus,
       "atiStkSwQoSGroupPortCoSPriorityTable": atiStkSwQoSGroupPortCoSPriorityTable,
       "atiStkSwQoSGroupPortCoSPriorityEntry": atiStkSwQoSGroupPortCoSPriorityEntry,
       "atiStkSwQoSGroupPortCoSPriorityModuleId": atiStkSwQoSGroupPortCoSPriorityModuleId,
       "atiStkSwQoSGroupPortCoSPriorityPortId": atiStkSwQoSGroupPortCoSPriorityPortId,
       "atiStkSwQoSGroupPortCoSPriorityPriority": atiStkSwQoSGroupPortCoSPriorityPriority,
       "atiStkSwQoSGroupPortCoSPriorityOverridePriority": atiStkSwQoSGroupPortCoSPriorityOverridePriority,
       "atiStkSwTrunkGroup": atiStkSwTrunkGroup,
       "atiStkSwStaticTrunkTable": atiStkSwStaticTrunkTable,
       "atiStkSwStaticTrunkEntry": atiStkSwStaticTrunkEntry,
       "atiStkSwStaticTrunkModuleId": atiStkSwStaticTrunkModuleId,
       "atiStkSwStaticTrunkIndex": atiStkSwStaticTrunkIndex,
       "atiStkSwStaticTrunkId": atiStkSwStaticTrunkId,
       "atiStkSwStaticTrunkName": atiStkSwStaticTrunkName,
       "atiStkSwStaticTrunkMethod": atiStkSwStaticTrunkMethod,
       "atiStkSwStaticTrunkPortList": atiStkSwStaticTrunkPortList,
       "atiStkSwStaticTrunkStatus": atiStkSwStaticTrunkStatus,
       "atiStkSwStaticTrunkRowStatus": atiStkSwStaticTrunkRowStatus,
       "atiStkSwACLGroup": atiStkSwACLGroup,
       "atiStkSwACLConfigTable": atiStkSwACLConfigTable,
       "atiStkSwACLConfigEntry": atiStkSwACLConfigEntry,
       "atiStkSwACLModuleId": atiStkSwACLModuleId,
       "atiStkSwACLId": atiStkSwACLId,
       "atiStkSwACLDescription": atiStkSwACLDescription,
       "atiStkSwACLAction": atiStkSwACLAction,
       "atiStkSwACLClassifierList": atiStkSwACLClassifierList,
       "atiStkSwACLPortList": atiStkSwACLPortList,
       "atiStkSwACLRowStatus": atiStkSwACLRowStatus}
)
