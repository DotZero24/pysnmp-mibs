# SNMP MIB module (OS-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-SFLOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:55 2025
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

(EntryValidator,
 PortList,
 oaOptiSwitch) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "EntryValidator",
    "PortList",
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


# MODULE-IDENTITY

osSFlow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25)
)
if mibBuilder.loadTexts:
    osSFlow.setRevisions(
        ("2013-05-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OsRcvrOperStatus(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("notReady", 2),
          ("ready", 3))
    )



# MIB Managed Objects in the order of their OIDs

_OsSFlowAgent_ObjectIdentity = ObjectIdentity
osSFlowAgent = _OsSFlowAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 1)
)


class _OsSFlowAgentAddress_Type(OctetString):
    """Custom type osSFlowAgentAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_OsSFlowAgentAddress_Type.__name__ = "OctetString"
_OsSFlowAgentAddress_Object = MibScalar
osSFlowAgentAddress = _OsSFlowAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 1, 1),
    _OsSFlowAgentAddress_Type()
)
osSFlowAgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSFlowAgentAddress.setStatus("current")


class _OsSFlowDefaultTruncateSize_Type(Integer32):
    """Custom type osSFlowDefaultTruncateSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 65536),
    )


_OsSFlowDefaultTruncateSize_Type.__name__ = "Integer32"
_OsSFlowDefaultTruncateSize_Object = MibScalar
osSFlowDefaultTruncateSize = _OsSFlowDefaultTruncateSize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 1, 2),
    _OsSFlowDefaultTruncateSize_Type()
)
osSFlowDefaultTruncateSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSFlowDefaultTruncateSize.setStatus("current")


class _OsSFlowSamplesRateLimit_Type(Integer32):
    """Custom type osSFlowSamplesRateLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_OsSFlowSamplesRateLimit_Type.__name__ = "Integer32"
_OsSFlowSamplesRateLimit_Object = MibScalar
osSFlowSamplesRateLimit = _OsSFlowSamplesRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 1, 3),
    _OsSFlowSamplesRateLimit_Type()
)
osSFlowSamplesRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSFlowSamplesRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    osSFlowSamplesRateLimit.setUnits("Samples per Second")
_OsSFlowSamplesDroppedByRateLimit_Type = Integer32
_OsSFlowSamplesDroppedByRateLimit_Object = MibScalar
osSFlowSamplesDroppedByRateLimit = _OsSFlowSamplesDroppedByRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 1, 4),
    _OsSFlowSamplesDroppedByRateLimit_Type()
)
osSFlowSamplesDroppedByRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSFlowSamplesDroppedByRateLimit.setStatus("current")
_OsSFlowRcvrTable_Object = MibTable
osSFlowRcvrTable = _OsSFlowRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 2)
)
if mibBuilder.loadTexts:
    osSFlowRcvrTable.setStatus("current")
_OsSFlowRcvrEntry_Object = MibTableRow
osSFlowRcvrEntry = _OsSFlowRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 2, 1)
)
osSFlowRcvrEntry.setIndexNames(
    (0, "OS-SFLOW-MIB", "osSFlowRcvrIndex"),
)
if mibBuilder.loadTexts:
    osSFlowRcvrEntry.setStatus("current")


class _OsSFlowRcvrIndex_Type(Integer32):
    """Custom type osSFlowRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_OsSFlowRcvrIndex_Type.__name__ = "Integer32"
_OsSFlowRcvrIndex_Object = MibTableColumn
osSFlowRcvrIndex = _OsSFlowRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 2, 1, 1),
    _OsSFlowRcvrIndex_Type()
)
osSFlowRcvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osSFlowRcvrIndex.setStatus("current")


class _OsSFlowRcvrOwner_Type(OctetString):
    """Custom type osSFlowRcvrOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_OsSFlowRcvrOwner_Type.__name__ = "OctetString"
_OsSFlowRcvrOwner_Object = MibTableColumn
osSFlowRcvrOwner = _OsSFlowRcvrOwner_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 2, 1, 2),
    _OsSFlowRcvrOwner_Type()
)
osSFlowRcvrOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSFlowRcvrOwner.setStatus("current")


class _OsSFlowRcvrAddress_Type(OctetString):
    """Custom type osSFlowRcvrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_OsSFlowRcvrAddress_Type.__name__ = "OctetString"
_OsSFlowRcvrAddress_Object = MibTableColumn
osSFlowRcvrAddress = _OsSFlowRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 2, 1, 6),
    _OsSFlowRcvrAddress_Type()
)
osSFlowRcvrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSFlowRcvrAddress.setStatus("current")


class _OsSFlowRcvrPort_Type(Integer32):
    """Custom type osSFlowRcvrPort based on Integer32"""
    defaultValue = 6343


_OsSFlowRcvrPort_Type.__name__ = "Integer32"
_OsSFlowRcvrPort_Object = MibTableColumn
osSFlowRcvrPort = _OsSFlowRcvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 2, 1, 7),
    _OsSFlowRcvrPort_Type()
)
osSFlowRcvrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSFlowRcvrPort.setStatus("current")
_OsSFlowRcvrAdminStatus_Type = EntryValidator
_OsSFlowRcvrAdminStatus_Object = MibTableColumn
osSFlowRcvrAdminStatus = _OsSFlowRcvrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 2, 1, 98),
    _OsSFlowRcvrAdminStatus_Type()
)
osSFlowRcvrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSFlowRcvrAdminStatus.setStatus("current")
_OsSFlowRcvrOperStatus_Type = OsRcvrOperStatus
_OsSFlowRcvrOperStatus_Object = MibTableColumn
osSFlowRcvrOperStatus = _OsSFlowRcvrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 2, 1, 99),
    _OsSFlowRcvrOperStatus_Type()
)
osSFlowRcvrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSFlowRcvrOperStatus.setStatus("current")
_OsSFlowCpTable_Object = MibTable
osSFlowCpTable = _OsSFlowCpTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3)
)
if mibBuilder.loadTexts:
    osSFlowCpTable.setStatus("current")
_OsSFlowCpEntry_Object = MibTableRow
osSFlowCpEntry = _OsSFlowCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3, 1)
)
osSFlowCpEntry.setIndexNames(
    (0, "OS-SFLOW-MIB", "osSFlowCpName"),
)
if mibBuilder.loadTexts:
    osSFlowCpEntry.setStatus("current")


class _OsSFlowCpName_Type(OctetString):
    """Custom type osSFlowCpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_OsSFlowCpName_Type.__name__ = "OctetString"
_OsSFlowCpName_Object = MibTableColumn
osSFlowCpName = _OsSFlowCpName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3, 1, 1),
    _OsSFlowCpName_Type()
)
osSFlowCpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osSFlowCpName.setStatus("current")


class _OsSflowCpRcvrIndex_Type(Integer32):
    """Custom type osSflowCpRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 9999),
    )


_OsSflowCpRcvrIndex_Type.__name__ = "Integer32"
_OsSflowCpRcvrIndex_Object = MibTableColumn
osSflowCpRcvrIndex = _OsSflowCpRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3, 1, 2),
    _OsSflowCpRcvrIndex_Type()
)
osSflowCpRcvrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSflowCpRcvrIndex.setStatus("current")


class _OsSflowCpRate_Type(Integer32):
    """Custom type osSflowCpRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3600),
    )


_OsSflowCpRate_Type.__name__ = "Integer32"
_OsSflowCpRate_Object = MibTableColumn
osSflowCpRate = _OsSflowCpRate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3, 1, 3),
    _OsSflowCpRate_Type()
)
osSflowCpRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSflowCpRate.setStatus("current")
if mibBuilder.loadTexts:
    osSflowCpRate.setUnits("Seconds")
_OsSflowCpPorts_Type = PortList
_OsSflowCpPorts_Object = MibTableColumn
osSflowCpPorts = _OsSflowCpPorts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3, 1, 4),
    _OsSflowCpPorts_Type()
)
osSflowCpPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSflowCpPorts.setStatus("current")
_OsSflowCpActiveTime_Type = Unsigned32
_OsSflowCpActiveTime_Object = MibTableColumn
osSflowCpActiveTime = _OsSflowCpActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3, 1, 5),
    _OsSflowCpActiveTime_Type()
)
osSflowCpActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSflowCpActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    osSflowCpActiveTime.setUnits("Seconds")
_OsSflowCpSampleCount_Type = Counter64
_OsSflowCpSampleCount_Object = MibTableColumn
osSflowCpSampleCount = _OsSflowCpSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3, 1, 6),
    _OsSflowCpSampleCount_Type()
)
osSflowCpSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSflowCpSampleCount.setStatus("current")
if mibBuilder.loadTexts:
    osSflowCpSampleCount.setUnits("Seconds")
_OsSFlowCpAdminStatus_Type = EntryValidator
_OsSFlowCpAdminStatus_Object = MibTableColumn
osSFlowCpAdminStatus = _OsSFlowCpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3, 1, 98),
    _OsSFlowCpAdminStatus_Type()
)
osSFlowCpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSFlowCpAdminStatus.setStatus("current")


class _OsSFlowCpOperStatus_Type(Integer32):
    """Custom type osSFlowCpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_OsSFlowCpOperStatus_Type.__name__ = "Integer32"
_OsSFlowCpOperStatus_Object = MibTableColumn
osSFlowCpOperStatus = _OsSFlowCpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 3, 1, 99),
    _OsSFlowCpOperStatus_Type()
)
osSFlowCpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osSFlowCpOperStatus.setStatus("current")
_OsSFlowConformance_ObjectIdentity = ObjectIdentity
osSFlowConformance = _OsSFlowConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 100)
)
_OsSFlowMIBCompliances_ObjectIdentity = ObjectIdentity
osSFlowMIBCompliances = _OsSFlowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 100, 1)
)
_OsSFlowMIBGroups_ObjectIdentity = ObjectIdentity
osSFlowMIBGroups = _OsSFlowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 100, 2)
)

# Managed Objects groups

osSFlowMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 100, 2, 1)
)
osSFlowMandatoryGroup.setObjects(
      *(("OS-SFLOW-MIB", "osSFlowAgentAddress"),
        ("OS-SFLOW-MIB", "osSFlowDefaultTruncateSize"),
        ("OS-SFLOW-MIB", "osSFlowSamplesRateLimit"),
        ("OS-SFLOW-MIB", "osSFlowSamplesDroppedByRateLimit"),
        ("OS-SFLOW-MIB", "osSFlowRcvrOwner"),
        ("OS-SFLOW-MIB", "osSFlowRcvrAddress"),
        ("OS-SFLOW-MIB", "osSFlowRcvrPort"),
        ("OS-SFLOW-MIB", "osSFlowRcvrAdminStatus"),
        ("OS-SFLOW-MIB", "osSFlowRcvrOperStatus"),
        ("OS-SFLOW-MIB", "osSflowCpRcvrIndex"),
        ("OS-SFLOW-MIB", "osSflowCpRate"),
        ("OS-SFLOW-MIB", "osSflowCpPorts"),
        ("OS-SFLOW-MIB", "osSflowCpActiveTime"),
        ("OS-SFLOW-MIB", "osSflowCpSampleCount"),
        ("OS-SFLOW-MIB", "osSFlowCpAdminStatus"),
        ("OS-SFLOW-MIB", "osSFlowCpOperStatus"))
)
if mibBuilder.loadTexts:
    osSFlowMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osSFlowMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 25, 100, 1, 1)
)
osSFlowMIBCompliance.setObjects(
    ("OS-SFLOW-MIB", "osSFlowMandatoryGroup")
)
if mibBuilder.loadTexts:
    osSFlowMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-SFLOW-MIB",
    **{"OsRcvrOperStatus": OsRcvrOperStatus,
       "osSFlow": osSFlow,
       "osSFlowAgent": osSFlowAgent,
       "osSFlowAgentAddress": osSFlowAgentAddress,
       "osSFlowDefaultTruncateSize": osSFlowDefaultTruncateSize,
       "osSFlowSamplesRateLimit": osSFlowSamplesRateLimit,
       "osSFlowSamplesDroppedByRateLimit": osSFlowSamplesDroppedByRateLimit,
       "osSFlowRcvrTable": osSFlowRcvrTable,
       "osSFlowRcvrEntry": osSFlowRcvrEntry,
       "osSFlowRcvrIndex": osSFlowRcvrIndex,
       "osSFlowRcvrOwner": osSFlowRcvrOwner,
       "osSFlowRcvrAddress": osSFlowRcvrAddress,
       "osSFlowRcvrPort": osSFlowRcvrPort,
       "osSFlowRcvrAdminStatus": osSFlowRcvrAdminStatus,
       "osSFlowRcvrOperStatus": osSFlowRcvrOperStatus,
       "osSFlowCpTable": osSFlowCpTable,
       "osSFlowCpEntry": osSFlowCpEntry,
       "osSFlowCpName": osSFlowCpName,
       "osSflowCpRcvrIndex": osSflowCpRcvrIndex,
       "osSflowCpRate": osSflowCpRate,
       "osSflowCpPorts": osSflowCpPorts,
       "osSflowCpActiveTime": osSflowCpActiveTime,
       "osSflowCpSampleCount": osSflowCpSampleCount,
       "osSFlowCpAdminStatus": osSFlowCpAdminStatus,
       "osSFlowCpOperStatus": osSFlowCpOperStatus,
       "osSFlowConformance": osSFlowConformance,
       "osSFlowMIBCompliances": osSFlowMIBCompliances,
       "osSFlowMIBCompliance": osSFlowMIBCompliance,
       "osSFlowMIBGroups": osSFlowMIBGroups,
       "osSFlowMandatoryGroup": osSFlowMandatoryGroup}
)
