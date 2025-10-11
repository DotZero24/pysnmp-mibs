# SNMP MIB module (OS-TM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-TM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:57 2025
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

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

osTm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38)
)
if mibBuilder.loadTexts:
    osTm.setRevisions(
        ("2016-11-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmPortIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class TmNodeId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class TmSlQueueId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



# MIB Managed Objects in the order of their OIDs

_OsTmCapabilities_ObjectIdentity = ObjectIdentity
osTmCapabilities = _OsTmCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 1)
)


class _OsTmSupport_Type(Integer32):
    """Custom type osTmSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OsTmSupport_Type.__name__ = "Integer32"
_OsTmSupport_Object = MibScalar
osTmSupport = _OsTmSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 1, 1),
    _OsTmSupport_Type()
)
osTmSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osTmSupport.setStatus("current")
_OsTmCountTable_Object = MibTable
osTmCountTable = _OsTmCountTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20)
)
if mibBuilder.loadTexts:
    osTmCountTable.setStatus("current")
_OsTmCountEntry_Object = MibTableRow
osTmCountEntry = _OsTmCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1)
)
osTmCountEntry.setIndexNames(
    (0, "OS-TM-MIB", "osTmCountPort"),
    (0, "OS-TM-MIB", "osTmCountServNode"),
    (0, "OS-TM-MIB", "osTmCountBNode"),
    (0, "OS-TM-MIB", "osTmCountCNode"),
    (0, "OS-TM-MIB", "osTmCountSlQueue"),
)
if mibBuilder.loadTexts:
    osTmCountEntry.setStatus("current")
_OsTmCountPort_Type = TmPortIndex
_OsTmCountPort_Object = MibTableColumn
osTmCountPort = _OsTmCountPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 1),
    _OsTmCountPort_Type()
)
osTmCountPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osTmCountPort.setStatus("current")
_OsTmCountServNode_Type = TmNodeId
_OsTmCountServNode_Object = MibTableColumn
osTmCountServNode = _OsTmCountServNode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 2),
    _OsTmCountServNode_Type()
)
osTmCountServNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osTmCountServNode.setStatus("current")
_OsTmCountBNode_Type = TmNodeId
_OsTmCountBNode_Object = MibTableColumn
osTmCountBNode = _OsTmCountBNode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 3),
    _OsTmCountBNode_Type()
)
osTmCountBNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osTmCountBNode.setStatus("current")
_OsTmCountCNode_Type = TmNodeId
_OsTmCountCNode_Object = MibTableColumn
osTmCountCNode = _OsTmCountCNode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 4),
    _OsTmCountCNode_Type()
)
osTmCountCNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osTmCountCNode.setStatus("current")
_OsTmCountSlQueue_Type = TmSlQueueId
_OsTmCountSlQueue_Object = MibTableColumn
osTmCountSlQueue = _OsTmCountSlQueue_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 5),
    _OsTmCountSlQueue_Type()
)
osTmCountSlQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osTmCountSlQueue.setStatus("current")
_OsTmCountClear_Type = TruthValue
_OsTmCountClear_Object = MibTableColumn
osTmCountClear = _OsTmCountClear_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 6),
    _OsTmCountClear_Type()
)
osTmCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osTmCountClear.setStatus("current")
_OsTmCountPacketsPassed_Type = Counter64
_OsTmCountPacketsPassed_Object = MibTableColumn
osTmCountPacketsPassed = _OsTmCountPacketsPassed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 8),
    _OsTmCountPacketsPassed_Type()
)
osTmCountPacketsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osTmCountPacketsPassed.setStatus("current")
_OsTmCountPacketsDropped_Type = Counter64
_OsTmCountPacketsDropped_Object = MibTableColumn
osTmCountPacketsDropped = _OsTmCountPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 9),
    _OsTmCountPacketsDropped_Type()
)
osTmCountPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osTmCountPacketsDropped.setStatus("current")
_OsTmCountBytesPassed_Type = Counter64
_OsTmCountBytesPassed_Object = MibTableColumn
osTmCountBytesPassed = _OsTmCountBytesPassed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 10),
    _OsTmCountBytesPassed_Type()
)
osTmCountBytesPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osTmCountBytesPassed.setStatus("current")
_OsTmCountBytesDropped_Type = Counter64
_OsTmCountBytesDropped_Object = MibTableColumn
osTmCountBytesDropped = _OsTmCountBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 20, 1, 11),
    _OsTmCountBytesDropped_Type()
)
osTmCountBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osTmCountBytesDropped.setStatus("current")
_OsTmConformance_ObjectIdentity = ObjectIdentity
osTmConformance = _OsTmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 100)
)
_OsTmMIBCompliances_ObjectIdentity = ObjectIdentity
osTmMIBCompliances = _OsTmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 1)
)
_OsTmMIBGroups_ObjectIdentity = ObjectIdentity
osTmMIBGroups = _OsTmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 2)
)

# Managed Objects groups

osTmMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 2, 1)
)
osTmMandatoryGroup.setObjects(
    ("OS-TM-MIB", "osTmSupport")
)
if mibBuilder.loadTexts:
    osTmMandatoryGroup.setStatus("current")

osTmOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 2, 2)
)
osTmOptGroup.setObjects(
      *(("OS-TM-MIB", "osTmCountClear"),
        ("OS-TM-MIB", "osTmCountPacketsPassed"),
        ("OS-TM-MIB", "osTmCountPacketsDropped"),
        ("OS-TM-MIB", "osTmCountBytesPassed"),
        ("OS-TM-MIB", "osTmCountBytesDropped"))
)
if mibBuilder.loadTexts:
    osTmOptGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osTmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 38, 100, 1, 1)
)
osTmMIBCompliance.setObjects(
      *(("OS-TM-MIB", "osTmMandatoryGroup"),
        ("OS-TM-MIB", "osTmOptGroup"))
)
if mibBuilder.loadTexts:
    osTmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-TM-MIB",
    **{"TmPortIndex": TmPortIndex,
       "TmNodeId": TmNodeId,
       "TmSlQueueId": TmSlQueueId,
       "osTm": osTm,
       "osTmCapabilities": osTmCapabilities,
       "osTmSupport": osTmSupport,
       "osTmCountTable": osTmCountTable,
       "osTmCountEntry": osTmCountEntry,
       "osTmCountPort": osTmCountPort,
       "osTmCountServNode": osTmCountServNode,
       "osTmCountBNode": osTmCountBNode,
       "osTmCountCNode": osTmCountCNode,
       "osTmCountSlQueue": osTmCountSlQueue,
       "osTmCountClear": osTmCountClear,
       "osTmCountPacketsPassed": osTmCountPacketsPassed,
       "osTmCountPacketsDropped": osTmCountPacketsDropped,
       "osTmCountBytesPassed": osTmCountBytesPassed,
       "osTmCountBytesDropped": osTmCountBytesDropped,
       "osTmConformance": osTmConformance,
       "osTmMIBCompliances": osTmMIBCompliances,
       "osTmMIBCompliance": osTmMIBCompliance,
       "osTmMIBGroups": osTmMIBGroups,
       "osTmMandatoryGroup": osTmMandatoryGroup,
       "osTmOptGroup": osTmOptGroup}
)
