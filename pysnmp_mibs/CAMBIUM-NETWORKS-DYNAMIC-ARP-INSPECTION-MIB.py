# SNMP MIB module (CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:38 2025
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

(PortList,
 VlanIdOrNone,
 dot1qStaticUnicastEntry,
 dot1qTpFdbEntry,
 dot1qTpFdbPort,
 dot1qVlanStaticEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrNone",
    "dot1qStaticUnicastEntry",
    "dot1qTpFdbEntry",
    "dot1qTpFdbPort",
    "dot1qVlanStaticEntry")

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

cnDaiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 110)
)
if mibBuilder.loadTexts:
    cnDaiMib.setRevisions(
        ("2022-02-17 00:00",
         "2019-03-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TrustState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untrusted", 0),
          ("trusted", 1))
    )



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class AdminStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_CnDaiGlobal_ObjectIdentity = ObjectIdentity
cnDaiGlobal = _CnDaiGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 110, 1)
)


class _CnDaiDebugFlag_Type(Integer32):
    """Custom type cnDaiDebugFlag based on Integer32"""
    defaultValue = 0


_CnDaiDebugFlag_Type.__name__ = "Integer32"
_CnDaiDebugFlag_Object = MibScalar
cnDaiDebugFlag = _CnDaiDebugFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 1, 1),
    _CnDaiDebugFlag_Type()
)
cnDaiDebugFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDaiDebugFlag.setStatus("current")
_CnDaiVlanCfg_ObjectIdentity = ObjectIdentity
cnDaiVlanCfg = _CnDaiVlanCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2)
)
_CnDaiVlanCfgTable_Object = MibTable
cnDaiVlanCfgTable = _CnDaiVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1)
)
if mibBuilder.loadTexts:
    cnDaiVlanCfgTable.setStatus("current")
_CnDaiVlanCfgEntry_Object = MibTableRow
cnDaiVlanCfgEntry = _CnDaiVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1)
)
cnDaiVlanCfgEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB", "cnDaiVlanCfgVlanId"),
)
if mibBuilder.loadTexts:
    cnDaiVlanCfgEntry.setStatus("current")
_CnDaiVlanCfgVlanId_Type = VlanId
_CnDaiVlanCfgVlanId_Object = MibTableColumn
cnDaiVlanCfgVlanId = _CnDaiVlanCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 1),
    _CnDaiVlanCfgVlanId_Type()
)
cnDaiVlanCfgVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnDaiVlanCfgVlanId.setStatus("current")


class _CnDaiVlanCfgDaiAdminStatus_Type(AdminStatus):
    """Custom type cnDaiVlanCfgDaiAdminStatus based on AdminStatus"""
    defaultValue = 2


_CnDaiVlanCfgDaiAdminStatus_Type.__name__ = "AdminStatus"
_CnDaiVlanCfgDaiAdminStatus_Object = MibTableColumn
cnDaiVlanCfgDaiAdminStatus = _CnDaiVlanCfgDaiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 2),
    _CnDaiVlanCfgDaiAdminStatus_Type()
)
cnDaiVlanCfgDaiAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDaiVlanCfgDaiAdminStatus.setStatus("current")
_CnDaiVlanForwarded_Type = Counter32
_CnDaiVlanForwarded_Object = MibTableColumn
cnDaiVlanForwarded = _CnDaiVlanForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 3),
    _CnDaiVlanForwarded_Type()
)
cnDaiVlanForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDaiVlanForwarded.setStatus("current")
_CnDaiVlanDropped_Type = Counter32
_CnDaiVlanDropped_Object = MibTableColumn
cnDaiVlanDropped = _CnDaiVlanDropped_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 4),
    _CnDaiVlanDropped_Type()
)
cnDaiVlanDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDaiVlanDropped.setStatus("current")
_CnDaiVlanInvalidProtocolData_Type = Counter32
_CnDaiVlanInvalidProtocolData_Object = MibTableColumn
cnDaiVlanInvalidProtocolData = _CnDaiVlanInvalidProtocolData_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 5),
    _CnDaiVlanInvalidProtocolData_Type()
)
cnDaiVlanInvalidProtocolData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDaiVlanInvalidProtocolData.setStatus("current")
_CnDaiVlanSrcMacValidationFailures_Type = Counter32
_CnDaiVlanSrcMacValidationFailures_Object = MibTableColumn
cnDaiVlanSrcMacValidationFailures = _CnDaiVlanSrcMacValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 6),
    _CnDaiVlanSrcMacValidationFailures_Type()
)
cnDaiVlanSrcMacValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDaiVlanSrcMacValidationFailures.setStatus("current")
_CnDaiVlanIpValidationFailures_Type = Counter32
_CnDaiVlanIpValidationFailures_Object = MibTableColumn
cnDaiVlanIpValidationFailures = _CnDaiVlanIpValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 7),
    _CnDaiVlanIpValidationFailures_Type()
)
cnDaiVlanIpValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDaiVlanIpValidationFailures.setStatus("current")
_CnDaiVlanDhcpBindingsPermitted_Type = Counter32
_CnDaiVlanDhcpBindingsPermitted_Object = MibTableColumn
cnDaiVlanDhcpBindingsPermitted = _CnDaiVlanDhcpBindingsPermitted_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 8),
    _CnDaiVlanDhcpBindingsPermitted_Type()
)
cnDaiVlanDhcpBindingsPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDaiVlanDhcpBindingsPermitted.setStatus("current")
_CnDaiVlanDhcpBindingsDenied_Type = Counter32
_CnDaiVlanDhcpBindingsDenied_Object = MibTableColumn
cnDaiVlanDhcpBindingsDenied = _CnDaiVlanDhcpBindingsDenied_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 9),
    _CnDaiVlanDhcpBindingsDenied_Type()
)
cnDaiVlanDhcpBindingsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDaiVlanDhcpBindingsDenied.setStatus("current")
_CnDaiVlanStaticBindingsPermitted_Type = Counter32
_CnDaiVlanStaticBindingsPermitted_Object = MibTableColumn
cnDaiVlanStaticBindingsPermitted = _CnDaiVlanStaticBindingsPermitted_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 10),
    _CnDaiVlanStaticBindingsPermitted_Type()
)
cnDaiVlanStaticBindingsPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDaiVlanStaticBindingsPermitted.setStatus("current")
_CnDaiVlanStaticBindingsDenied_Type = Counter32
_CnDaiVlanStaticBindingsDenied_Object = MibTableColumn
cnDaiVlanStaticBindingsDenied = _CnDaiVlanStaticBindingsDenied_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 11),
    _CnDaiVlanStaticBindingsDenied_Type()
)
cnDaiVlanStaticBindingsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDaiVlanStaticBindingsDenied.setStatus("current")
_CnDaiVlanCfgRowStatus_Type = RowStatus
_CnDaiVlanCfgRowStatus_Object = MibTableColumn
cnDaiVlanCfgRowStatus = _CnDaiVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 12),
    _CnDaiVlanCfgRowStatus_Type()
)
cnDaiVlanCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDaiVlanCfgRowStatus.setStatus("current")
_CnDaiIfCfg_ObjectIdentity = ObjectIdentity
cnDaiIfCfg = _CnDaiIfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 110, 3)
)
_CnDaiIfCfgTable_Object = MibTable
cnDaiIfCfgTable = _CnDaiIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 3, 1)
)
if mibBuilder.loadTexts:
    cnDaiIfCfgTable.setStatus("current")
_CnDaiIfCfgEntry_Object = MibTableRow
cnDaiIfCfgEntry = _CnDaiIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 3, 1, 1)
)
cnDaiIfCfgEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB", "cnDaiIfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    cnDaiIfCfgEntry.setStatus("current")


class _CnDaiIfCfgIfIndex_Type(Integer32):
    """Custom type cnDaiIfCfgIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CnDaiIfCfgIfIndex_Type.__name__ = "Integer32"
_CnDaiIfCfgIfIndex_Object = MibTableColumn
cnDaiIfCfgIfIndex = _CnDaiIfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 3, 1, 1, 1),
    _CnDaiIfCfgIfIndex_Type()
)
cnDaiIfCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnDaiIfCfgIfIndex.setStatus("current")


class _CnDaiIfCfgTrustState_Type(TrustState):
    """Custom type cnDaiIfCfgTrustState based on TrustState"""
    defaultValue = 0


_CnDaiIfCfgTrustState_Type.__name__ = "TrustState"
_CnDaiIfCfgTrustState_Object = MibTableColumn
cnDaiIfCfgTrustState = _CnDaiIfCfgTrustState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 110, 3, 1, 1, 2),
    _CnDaiIfCfgTrustState_Type()
)
cnDaiIfCfgTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDaiIfCfgTrustState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB",
    **{"TrustState": TrustState,
       "VlanId": VlanId,
       "AdminStatus": AdminStatus,
       "cnDaiMib": cnDaiMib,
       "cnDaiGlobal": cnDaiGlobal,
       "cnDaiDebugFlag": cnDaiDebugFlag,
       "cnDaiVlanCfg": cnDaiVlanCfg,
       "cnDaiVlanCfgTable": cnDaiVlanCfgTable,
       "cnDaiVlanCfgEntry": cnDaiVlanCfgEntry,
       "cnDaiVlanCfgVlanId": cnDaiVlanCfgVlanId,
       "cnDaiVlanCfgDaiAdminStatus": cnDaiVlanCfgDaiAdminStatus,
       "cnDaiVlanForwarded": cnDaiVlanForwarded,
       "cnDaiVlanDropped": cnDaiVlanDropped,
       "cnDaiVlanInvalidProtocolData": cnDaiVlanInvalidProtocolData,
       "cnDaiVlanSrcMacValidationFailures": cnDaiVlanSrcMacValidationFailures,
       "cnDaiVlanIpValidationFailures": cnDaiVlanIpValidationFailures,
       "cnDaiVlanDhcpBindingsPermitted": cnDaiVlanDhcpBindingsPermitted,
       "cnDaiVlanDhcpBindingsDenied": cnDaiVlanDhcpBindingsDenied,
       "cnDaiVlanStaticBindingsPermitted": cnDaiVlanStaticBindingsPermitted,
       "cnDaiVlanStaticBindingsDenied": cnDaiVlanStaticBindingsDenied,
       "cnDaiVlanCfgRowStatus": cnDaiVlanCfgRowStatus,
       "cnDaiIfCfg": cnDaiIfCfg,
       "cnDaiIfCfgTable": cnDaiIfCfgTable,
       "cnDaiIfCfgEntry": cnDaiIfCfgEntry,
       "cnDaiIfCfgIfIndex": cnDaiIfCfgIfIndex,
       "cnDaiIfCfgTrustState": cnDaiIfCfgTrustState}
)
