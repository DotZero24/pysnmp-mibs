# SNMP MIB module (RUCKUS-NDI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/RUCKUS-NDI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:01:52 2025
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

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
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

ruckusNdiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NDType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("static", 2),
          ("dynamic", 3),
          ("inspect", 4),
          ("dhcpv6", 5),
          ("dynamicDhcpv6", 6),
          ("staticDhcpv6", 7),
          ("host", 8))
    )



class NDState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("valid", 2),
          ("pend", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RuckusNdiNotify_ObjectIdentity = ObjectIdentity
ruckusNdiNotify = _RuckusNdiNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 0)
)
_RuckusNdiObjects_ObjectIdentity = ObjectIdentity
ruckusNdiObjects = _RuckusNdiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1)
)
_RuckusNdiVlan_ObjectIdentity = ObjectIdentity
ruckusNdiVlan = _RuckusNdiVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1)
)
_RuckusNdiVlanConfigTable_Object = MibTable
ruckusNdiVlanConfigTable = _RuckusNdiVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusNdiVlanConfigTable.setStatus("current")
_RuckusNdiVlanConfigEntry_Object = MibTableRow
ruckusNdiVlanConfigEntry = _RuckusNdiVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1, 1, 1)
)
ruckusNdiVlanConfigEntry.setIndexNames(
    (0, "RUCKUS-NDI-MIB", "ruckusNdiVlanConfigVlanId"),
)
if mibBuilder.loadTexts:
    ruckusNdiVlanConfigEntry.setStatus("current")
_RuckusNdiVlanConfigVlanId_Type = VlanIndex
_RuckusNdiVlanConfigVlanId_Object = MibTableColumn
ruckusNdiVlanConfigVlanId = _RuckusNdiVlanConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1, 1, 1, 1),
    _RuckusNdiVlanConfigVlanId_Type()
)
ruckusNdiVlanConfigVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusNdiVlanConfigVlanId.setStatus("current")


class _RuckusNdiVlanDynNDInspectionEnable_Type(TruthValue):
    """Custom type ruckusNdiVlanDynNDInspectionEnable based on TruthValue"""
    defaultValue = 2


_RuckusNdiVlanDynNDInspectionEnable_Type.__name__ = "TruthValue"
_RuckusNdiVlanDynNDInspectionEnable_Object = MibTableColumn
ruckusNdiVlanDynNDInspectionEnable = _RuckusNdiVlanDynNDInspectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 1, 1, 1, 2),
    _RuckusNdiVlanDynNDInspectionEnable_Type()
)
ruckusNdiVlanDynNDInspectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusNdiVlanDynNDInspectionEnable.setStatus("current")
_RuckusNdiInterface_ObjectIdentity = ObjectIdentity
ruckusNdiInterface = _RuckusNdiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 2)
)
_RuckusNdInspectIfConfigTable_Object = MibTable
ruckusNdInspectIfConfigTable = _RuckusNdInspectIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruckusNdInspectIfConfigTable.setStatus("current")
_RuckusNdiIfConfigEntry_Object = MibTableRow
ruckusNdiIfConfigEntry = _RuckusNdiIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 2, 1, 1)
)
ruckusNdiIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusNdiIfConfigEntry.setStatus("current")


class _RuckusNdiIfTrustValue_Type(TruthValue):
    """Custom type ruckusNdiIfTrustValue based on TruthValue"""
    defaultValue = 2


_RuckusNdiIfTrustValue_Type.__name__ = "TruthValue"
_RuckusNdiIfTrustValue_Object = MibTableColumn
ruckusNdiIfTrustValue = _RuckusNdiIfTrustValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 2, 1, 1, 1),
    _RuckusNdiIfTrustValue_Type()
)
ruckusNdiIfTrustValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusNdiIfTrustValue.setStatus("current")
_RuckusNdiNDInspect_ObjectIdentity = ObjectIdentity
ruckusNdiNDInspect = _RuckusNdiNDInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3)
)
_RuckusNdiStaticNDInspectTable_Object = MibTable
ruckusNdiStaticNDInspectTable = _RuckusNdiStaticNDInspectTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruckusNdiStaticNDInspectTable.setStatus("current")
_RuckusNdiStaticNDInspectEntry_Object = MibTableRow
ruckusNdiStaticNDInspectEntry = _RuckusNdiStaticNDInspectEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1)
)
ruckusNdiStaticNDInspectEntry.setIndexNames(
    (0, "RUCKUS-NDI-MIB", "ruckusNdiStaticNDInspectIpv6Addr"),
)
if mibBuilder.loadTexts:
    ruckusNdiStaticNDInspectEntry.setStatus("current")
_RuckusNdiStaticNDInspectIpv6Addr_Type = Ipv6Address
_RuckusNdiStaticNDInspectIpv6Addr_Object = MibTableColumn
ruckusNdiStaticNDInspectIpv6Addr = _RuckusNdiStaticNDInspectIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 1),
    _RuckusNdiStaticNDInspectIpv6Addr_Type()
)
ruckusNdiStaticNDInspectIpv6Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusNdiStaticNDInspectIpv6Addr.setStatus("current")
_RuckusNdiStaticNDInspectMacAddr_Type = MacAddress
_RuckusNdiStaticNDInspectMacAddr_Object = MibTableColumn
ruckusNdiStaticNDInspectMacAddr = _RuckusNdiStaticNDInspectMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 2),
    _RuckusNdiStaticNDInspectMacAddr_Type()
)
ruckusNdiStaticNDInspectMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusNdiStaticNDInspectMacAddr.setStatus("current")
_RuckusNdiStaticNDInspectType_Type = NDType
_RuckusNdiStaticNDInspectType_Object = MibTableColumn
ruckusNdiStaticNDInspectType = _RuckusNdiStaticNDInspectType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 3),
    _RuckusNdiStaticNDInspectType_Type()
)
ruckusNdiStaticNDInspectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusNdiStaticNDInspectType.setStatus("current")
_RuckusNdiStaticNDInspectState_Type = NDState
_RuckusNdiStaticNDInspectState_Object = MibTableColumn
ruckusNdiStaticNDInspectState = _RuckusNdiStaticNDInspectState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 4),
    _RuckusNdiStaticNDInspectState_Type()
)
ruckusNdiStaticNDInspectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusNdiStaticNDInspectState.setStatus("current")
_RuckusNdiStaticNDInspectAge_Type = Unsigned32
_RuckusNdiStaticNDInspectAge_Object = MibTableColumn
ruckusNdiStaticNDInspectAge = _RuckusNdiStaticNDInspectAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 5),
    _RuckusNdiStaticNDInspectAge_Type()
)
ruckusNdiStaticNDInspectAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusNdiStaticNDInspectAge.setStatus("current")
_RuckusNdiStaticNDInspectPort_Type = InterfaceIndex
_RuckusNdiStaticNDInspectPort_Object = MibTableColumn
ruckusNdiStaticNDInspectPort = _RuckusNdiStaticNDInspectPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 6),
    _RuckusNdiStaticNDInspectPort_Type()
)
ruckusNdiStaticNDInspectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusNdiStaticNDInspectPort.setStatus("current")
_RuckusNdiStaticNDInspectRowStatus_Type = RowStatus
_RuckusNdiStaticNDInspectRowStatus_Object = MibTableColumn
ruckusNdiStaticNDInspectRowStatus = _RuckusNdiStaticNDInspectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 1, 3, 1, 1, 7),
    _RuckusNdiStaticNDInspectRowStatus_Type()
)
ruckusNdiStaticNDInspectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusNdiStaticNDInspectRowStatus.setStatus("current")
_RuckusNdiConformance_ObjectIdentity = ObjectIdentity
ruckusNdiConformance = _RuckusNdiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 2)
)
_RuckusNdiCompliances_ObjectIdentity = ObjectIdentity
ruckusNdiCompliances = _RuckusNdiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruckusNdiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 47, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusNdiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-NDI-MIB",
    **{"NDType": NDType,
       "NDState": NDState,
       "ruckusNdiMIB": ruckusNdiMIB,
       "ruckusNdiNotify": ruckusNdiNotify,
       "ruckusNdiObjects": ruckusNdiObjects,
       "ruckusNdiVlan": ruckusNdiVlan,
       "ruckusNdiVlanConfigTable": ruckusNdiVlanConfigTable,
       "ruckusNdiVlanConfigEntry": ruckusNdiVlanConfigEntry,
       "ruckusNdiVlanConfigVlanId": ruckusNdiVlanConfigVlanId,
       "ruckusNdiVlanDynNDInspectionEnable": ruckusNdiVlanDynNDInspectionEnable,
       "ruckusNdiInterface": ruckusNdiInterface,
       "ruckusNdInspectIfConfigTable": ruckusNdInspectIfConfigTable,
       "ruckusNdiIfConfigEntry": ruckusNdiIfConfigEntry,
       "ruckusNdiIfTrustValue": ruckusNdiIfTrustValue,
       "ruckusNdiNDInspect": ruckusNdiNDInspect,
       "ruckusNdiStaticNDInspectTable": ruckusNdiStaticNDInspectTable,
       "ruckusNdiStaticNDInspectEntry": ruckusNdiStaticNDInspectEntry,
       "ruckusNdiStaticNDInspectIpv6Addr": ruckusNdiStaticNDInspectIpv6Addr,
       "ruckusNdiStaticNDInspectMacAddr": ruckusNdiStaticNDInspectMacAddr,
       "ruckusNdiStaticNDInspectType": ruckusNdiStaticNDInspectType,
       "ruckusNdiStaticNDInspectState": ruckusNdiStaticNDInspectState,
       "ruckusNdiStaticNDInspectAge": ruckusNdiStaticNDInspectAge,
       "ruckusNdiStaticNDInspectPort": ruckusNdiStaticNDInspectPort,
       "ruckusNdiStaticNDInspectRowStatus": ruckusNdiStaticNDInspectRowStatus,
       "ruckusNdiConformance": ruckusNdiConformance,
       "ruckusNdiCompliances": ruckusNdiCompliances,
       "ruckusNdiCompliance": ruckusNdiCompliance}
)
