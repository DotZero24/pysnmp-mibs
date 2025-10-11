# SNMP MIB module (RAISECOM-EXTLOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-EXTLOOPBACK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:22 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 MacAddress,
 PhysAddress,
 TextualConvention,
 Unsigned32) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "Unsigned32")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcExtLoopback = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45)
)
if mibBuilder.loadTexts:
    rcExtLoopback.setRevisions(
        ("2007-11-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RcExtLoopbackMode(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("port", 2),
          ("dmac", 3),
          ("smac", 4),
          ("cvlan", 5),
          ("svlan", 6),
          ("dvlan", 7))
    )



# MIB Managed Objects in the order of their OIDs

_RcExtloopbackObjectsGroup_ObjectIdentity = ObjectIdentity
rcExtloopbackObjectsGroup = _RcExtloopbackObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 1)
)
_RcExtLoopbackBMDMacTransEnable_Type = EnableVar
_RcExtLoopbackBMDMacTransEnable_Object = MibScalar
rcExtLoopbackBMDMacTransEnable = _RcExtLoopbackBMDMacTransEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 1, 1),
    _RcExtLoopbackBMDMacTransEnable_Type()
)
rcExtLoopbackBMDMacTransEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcExtLoopbackBMDMacTransEnable.setStatus("current")
_RcExtloopbackConfigGroup_ObjectIdentity = ObjectIdentity
rcExtloopbackConfigGroup = _RcExtloopbackConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2)
)
_RcExtLoopbackTable_Object = MibTable
rcExtLoopbackTable = _RcExtLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1)
)
if mibBuilder.loadTexts:
    rcExtLoopbackTable.setStatus("current")
_RcExtLoopbackEntry_Object = MibTableRow
rcExtLoopbackEntry = _RcExtLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1)
)
rcExtLoopbackEntry.setIndexNames(
    (0, "RAISECOM-EXTLOOPBACK-MIB", "rcExtLoopbackPortIndex"),
)
if mibBuilder.loadTexts:
    rcExtLoopbackEntry.setStatus("current")
_RcExtLoopbackPortIndex_Type = Integer32
_RcExtLoopbackPortIndex_Object = MibTableColumn
rcExtLoopbackPortIndex = _RcExtLoopbackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 1),
    _RcExtLoopbackPortIndex_Type()
)
rcExtLoopbackPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcExtLoopbackPortIndex.setStatus("current")
_RcExtLoopbackDMac_Type = MacAddress
_RcExtLoopbackDMac_Object = MibTableColumn
rcExtLoopbackDMac = _RcExtLoopbackDMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 2),
    _RcExtLoopbackDMac_Type()
)
rcExtLoopbackDMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcExtLoopbackDMac.setStatus("current")
_RcExtLoopbackSMac_Type = MacAddress
_RcExtLoopbackSMac_Object = MibTableColumn
rcExtLoopbackSMac = _RcExtLoopbackSMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 3),
    _RcExtLoopbackSMac_Type()
)
rcExtLoopbackSMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcExtLoopbackSMac.setStatus("current")
_RcExtLoopbackSVlan_Type = VlanId
_RcExtLoopbackSVlan_Object = MibTableColumn
rcExtLoopbackSVlan = _RcExtLoopbackSVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 4),
    _RcExtLoopbackSVlan_Type()
)
rcExtLoopbackSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcExtLoopbackSVlan.setStatus("current")
_RcExtLoopbackCVlan_Type = VlanId
_RcExtLoopbackCVlan_Object = MibTableColumn
rcExtLoopbackCVlan = _RcExtLoopbackCVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 5),
    _RcExtLoopbackCVlan_Type()
)
rcExtLoopbackCVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcExtLoopbackCVlan.setStatus("current")
_RcExtLoopbackTime_Type = Integer32
_RcExtLoopbackTime_Object = MibTableColumn
rcExtLoopbackTime = _RcExtLoopbackTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 6),
    _RcExtLoopbackTime_Type()
)
rcExtLoopbackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcExtLoopbackTime.setStatus("current")
_RcExtLoopbackMode_Type = RcExtLoopbackMode
_RcExtLoopbackMode_Object = MibTableColumn
rcExtLoopbackMode = _RcExtLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 7),
    _RcExtLoopbackMode_Type()
)
rcExtLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcExtLoopbackMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-EXTLOOPBACK-MIB",
    **{"RcExtLoopbackMode": RcExtLoopbackMode,
       "rcExtLoopback": rcExtLoopback,
       "rcExtloopbackObjectsGroup": rcExtloopbackObjectsGroup,
       "rcExtLoopbackBMDMacTransEnable": rcExtLoopbackBMDMacTransEnable,
       "rcExtloopbackConfigGroup": rcExtloopbackConfigGroup,
       "rcExtLoopbackTable": rcExtLoopbackTable,
       "rcExtLoopbackEntry": rcExtLoopbackEntry,
       "rcExtLoopbackPortIndex": rcExtLoopbackPortIndex,
       "rcExtLoopbackDMac": rcExtLoopbackDMac,
       "rcExtLoopbackSMac": rcExtLoopbackSMac,
       "rcExtLoopbackSVlan": rcExtLoopbackSVlan,
       "rcExtLoopbackCVlan": rcExtLoopbackCVlan,
       "rcExtLoopbackTime": rcExtLoopbackTime,
       "rcExtLoopbackMode": rcExtLoopbackMode}
)
