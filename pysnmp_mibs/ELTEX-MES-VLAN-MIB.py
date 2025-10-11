# SNMP MIB module (ELTEX-MES-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:52 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

(PortList,
 VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qVlanIndex")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(vlanMulticastTvEntry,) = mibBuilder.importSymbols(
    "RADLAN-vlan-MIB",
    "vlanMulticastTvEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

eltMesVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5)
)
if mibBuilder.loadTexts:
    eltMesVlan.setRevisions(
        ("2018-08-07 00:00",
         "2017-06-05 00:00",
         "2013-11-18 00:00",
         "2013-11-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltVlanMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("tr101", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltVlanMulticastTvTable_Object = MibTable
eltVlanMulticastTvTable = _EltVlanMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 1)
)
if mibBuilder.loadTexts:
    eltVlanMulticastTvTable.setStatus("current")
_EltVlanMulticastTvEntry_Object = MibTableRow
eltVlanMulticastTvEntry = _EltVlanMulticastTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 1, 1)
)
if mibBuilder.loadTexts:
    eltVlanMulticastTvEntry.setStatus("current")
_EltVlanMulticastTvVIDIsTagged_Type = TruthValue
_EltVlanMulticastTvVIDIsTagged_Object = MibTableColumn
eltVlanMulticastTvVIDIsTagged = _EltVlanMulticastTvVIDIsTagged_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 1, 1, 1),
    _EltVlanMulticastTvVIDIsTagged_Type()
)
eltVlanMulticastTvVIDIsTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltVlanMulticastTvVIDIsTagged.setStatus("current")
_EltVlanMode_Type = EltVlanMode
_EltVlanMode_Object = MibScalar
eltVlanMode = _EltVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 2),
    _EltVlanMode_Type()
)
eltVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltVlanMode.setStatus("current")
_EltDot1qVlanStaticTable_Object = MibTable
eltDot1qVlanStaticTable = _EltDot1qVlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 4)
)
if mibBuilder.loadTexts:
    eltDot1qVlanStaticTable.setStatus("current")
_EltDot1qVlanStaticEntry_Object = MibTableRow
eltDot1qVlanStaticEntry = _EltDot1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 4, 1)
)
eltDot1qVlanStaticEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    eltDot1qVlanStaticEntry.setStatus("current")


class _EltDot1qVlanStaticCos_Type(Integer32):
    """Custom type eltDot1qVlanStaticCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_EltDot1qVlanStaticCos_Type.__name__ = "Integer32"
_EltDot1qVlanStaticCos_Object = MibTableColumn
eltDot1qVlanStaticCos = _EltDot1qVlanStaticCos_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 4, 1, 1),
    _EltDot1qVlanStaticCos_Type()
)
eltDot1qVlanStaticCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDot1qVlanStaticCos.setStatus("current")
_EltMesVlanDefault_ObjectIdentity = ObjectIdentity
eltMesVlanDefault = _EltMesVlanDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 5)
)
_EltVlanDefaultForbiddenPorts_Type = PortList
_EltVlanDefaultForbiddenPorts_Object = MibScalar
eltVlanDefaultForbiddenPorts = _EltVlanDefaultForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 5, 1),
    _EltVlanDefaultForbiddenPorts_Type()
)
eltVlanDefaultForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltVlanDefaultForbiddenPorts.setStatus("current")
_EltVlanTriplePlayTable_Object = MibTable
eltVlanTriplePlayTable = _EltVlanTriplePlayTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 6)
)
if mibBuilder.loadTexts:
    eltVlanTriplePlayTable.setStatus("current")
_EltVlanTriplePlayEntry_Object = MibTableRow
eltVlanTriplePlayEntry = _EltVlanTriplePlayEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 6, 1)
)
eltVlanTriplePlayEntry.setIndexNames(
    (0, "ELTEX-MES-VLAN-MIB", "eltVlanTriplePlayInnerVID"),
    (0, "ELTEX-MES-VLAN-MIB", "eltVlanTriplePlayInputPort"),
)
if mibBuilder.loadTexts:
    eltVlanTriplePlayEntry.setStatus("current")
_EltVlanTriplePlayInnerVID_Type = VlanIndex
_EltVlanTriplePlayInnerVID_Object = MibTableColumn
eltVlanTriplePlayInnerVID = _EltVlanTriplePlayInnerVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 6, 1, 1),
    _EltVlanTriplePlayInnerVID_Type()
)
eltVlanTriplePlayInnerVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltVlanTriplePlayInnerVID.setStatus("current")
_EltVlanTriplePlayInputPort_Type = InterfaceIndexOrZero
_EltVlanTriplePlayInputPort_Object = MibTableColumn
eltVlanTriplePlayInputPort = _EltVlanTriplePlayInputPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 6, 1, 2),
    _EltVlanTriplePlayInputPort_Type()
)
eltVlanTriplePlayInputPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltVlanTriplePlayInputPort.setStatus("current")
_EltVlanTriplePlayMulticastTvVID_Type = VlanIndex
_EltVlanTriplePlayMulticastTvVID_Object = MibTableColumn
eltVlanTriplePlayMulticastTvVID = _EltVlanTriplePlayMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 6, 1, 3),
    _EltVlanTriplePlayMulticastTvVID_Type()
)
eltVlanTriplePlayMulticastTvVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltVlanTriplePlayMulticastTvVID.setStatus("current")
_EltVlanTriplePlayRowStatus_Type = RowStatus
_EltVlanTriplePlayRowStatus_Object = MibTableColumn
eltVlanTriplePlayRowStatus = _EltVlanTriplePlayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 6, 1, 4),
    _EltVlanTriplePlayRowStatus_Type()
)
eltVlanTriplePlayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltVlanTriplePlayRowStatus.setStatus("current")
vlanMulticastTvEntry.registerAugmentions(
    ("ELTEX-MES-VLAN-MIB",
     "eltVlanMulticastTvEntry")
)
eltVlanMulticastTvEntry.setIndexNames(*vlanMulticastTvEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-VLAN-MIB",
    **{"EltVlanMode": EltVlanMode,
       "eltMesVlan": eltMesVlan,
       "eltVlanMulticastTvTable": eltVlanMulticastTvTable,
       "eltVlanMulticastTvEntry": eltVlanMulticastTvEntry,
       "eltVlanMulticastTvVIDIsTagged": eltVlanMulticastTvVIDIsTagged,
       "eltVlanMode": eltVlanMode,
       "eltDot1qVlanStaticTable": eltDot1qVlanStaticTable,
       "eltDot1qVlanStaticEntry": eltDot1qVlanStaticEntry,
       "eltDot1qVlanStaticCos": eltDot1qVlanStaticCos,
       "eltMesVlanDefault": eltMesVlanDefault,
       "eltVlanDefaultForbiddenPorts": eltVlanDefaultForbiddenPorts,
       "eltVlanTriplePlayTable": eltVlanTriplePlayTable,
       "eltVlanTriplePlayEntry": eltVlanTriplePlayEntry,
       "eltVlanTriplePlayInnerVID": eltVlanTriplePlayInnerVID,
       "eltVlanTriplePlayInputPort": eltVlanTriplePlayInputPort,
       "eltVlanTriplePlayMulticastTvVID": eltVlanTriplePlayMulticastTvVID,
       "eltVlanTriplePlayRowStatus": eltVlanTriplePlayRowStatus}
)
