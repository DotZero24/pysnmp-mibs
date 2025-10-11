# SNMP MIB module (FASTPATH-QOS-AUTOVOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/FASTPATH-QOS-AUTOVOIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:43 2025
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

(fastPathQOS,) = mibBuilder.importSymbols(
    "FASTPATH-QOS-MIB",
    "fastPathQOS")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathQOSAUTOVOIP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    fastPathQOSAUTOVOIP.setRevisions(
        ("2007-11-23 00:00",
         "2007-11-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PercentByFives(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(35, 35),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(55, 55),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(65, 65),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(85, 85),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(95, 95),
        ValueRangeConstraint(100, 100),
    )



class Sixteenths(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_AgentAutoVoIPCfgGroup_ObjectIdentity = ObjectIdentity
agentAutoVoIPCfgGroup = _AgentAutoVoIPCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1)
)
_AgentAutoVoIPTable_Object = MibTable
agentAutoVoIPTable = _AgentAutoVoIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    agentAutoVoIPTable.setStatus("current")
_AgentAutoVoIPEntry_Object = MibTableRow
agentAutoVoIPEntry = _AgentAutoVoIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1, 1)
)
agentAutoVoIPEntry.setIndexNames(
    (0, "FASTPATH-QOS-AUTOVOIP-MIB", "agentAutoVoIPIntfIndex"),
)
if mibBuilder.loadTexts:
    agentAutoVoIPEntry.setStatus("current")
_AgentAutoVoIPIntfIndex_Type = InterfaceIndexOrZero
_AgentAutoVoIPIntfIndex_Object = MibTableColumn
agentAutoVoIPIntfIndex = _AgentAutoVoIPIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1, 1, 1),
    _AgentAutoVoIPIntfIndex_Type()
)
agentAutoVoIPIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentAutoVoIPIntfIndex.setStatus("current")


class _AgentAutoVoIPMode_Type(Integer32):
    """Custom type agentAutoVoIPMode based on Integer32"""
    defaultValue = 2

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


_AgentAutoVoIPMode_Type.__name__ = "Integer32"
_AgentAutoVoIPMode_Object = MibTableColumn
agentAutoVoIPMode = _AgentAutoVoIPMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1, 1, 2),
    _AgentAutoVoIPMode_Type()
)
agentAutoVoIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAutoVoIPMode.setStatus("current")


class _AgentAutoVoIPCosQueue_Type(Unsigned32):
    """Custom type agentAutoVoIPCosQueue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentAutoVoIPCosQueue_Type.__name__ = "Unsigned32"
_AgentAutoVoIPCosQueue_Object = MibTableColumn
agentAutoVoIPCosQueue = _AgentAutoVoIPCosQueue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1, 1, 3),
    _AgentAutoVoIPCosQueue_Type()
)
agentAutoVoIPCosQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAutoVoIPCosQueue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-QOS-AUTOVOIP-MIB",
    **{"PercentByFives": PercentByFives,
       "Sixteenths": Sixteenths,
       "fastPathQOSAUTOVOIP": fastPathQOSAUTOVOIP,
       "agentAutoVoIPCfgGroup": agentAutoVoIPCfgGroup,
       "agentAutoVoIPTable": agentAutoVoIPTable,
       "agentAutoVoIPEntry": agentAutoVoIPEntry,
       "agentAutoVoIPIntfIndex": agentAutoVoIPIntfIndex,
       "agentAutoVoIPMode": agentAutoVoIPMode,
       "agentAutoVoIPCosQueue": agentAutoVoIPCosQueue}
)
