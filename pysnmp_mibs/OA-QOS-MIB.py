# SNMP MIB module (OA-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:39 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaClassification_ObjectIdentity = ObjectIdentity
oaClassification = _OaClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21)
)
_OaQoS_ObjectIdentity = ObjectIdentity
oaQoS = _OaQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2)
)


class _OaQoSSaveMode_Type(Integer32):
    """Custom type oaQoSSaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("allQoSParams", 2))
    )


_OaQoSSaveMode_Type.__name__ = "Integer32"
_OaQoSSaveMode_Object = MibScalar
oaQoSSaveMode = _OaQoSSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 1),
    _OaQoSSaveMode_Type()
)
oaQoSSaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaQoSSaveMode.setStatus("mandatory")
_OaQoSMaxPriorQueuesNumber_Type = Integer32
_OaQoSMaxPriorQueuesNumber_Object = MibScalar
oaQoSMaxPriorQueuesNumber = _OaQoSMaxPriorQueuesNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 2),
    _OaQoSMaxPriorQueuesNumber_Type()
)
oaQoSMaxPriorQueuesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSMaxPriorQueuesNumber.setStatus("mandatory")
_OaQoSModuleStatusTable_Object = MibTable
oaQoSModuleStatusTable = _OaQoSModuleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 3)
)
if mibBuilder.loadTexts:
    oaQoSModuleStatusTable.setStatus("mandatory")
_OaQoSModuleStatusEntry_Object = MibTableRow
oaQoSModuleStatusEntry = _OaQoSModuleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 3, 1)
)
oaQoSModuleStatusEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oaQoSSlotId"),
    (0, "OA-QOS-MIB", "oaQoSModuleId"),
)
if mibBuilder.loadTexts:
    oaQoSModuleStatusEntry.setStatus("mandatory")
_OaQoSSlotId_Type = Integer32
_OaQoSSlotId_Object = MibTableColumn
oaQoSSlotId = _OaQoSSlotId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 3, 1, 1),
    _OaQoSSlotId_Type()
)
oaQoSSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSSlotId.setStatus("mandatory")
_OaQoSModuleId_Type = Integer32
_OaQoSModuleId_Object = MibTableColumn
oaQoSModuleId = _OaQoSModuleId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 3, 1, 2),
    _OaQoSModuleId_Type()
)
oaQoSModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSModuleId.setStatus("mandatory")


class _OaQoSModuleStatus_Type(Integer32):
    """Custom type oaQoSModuleStatus based on Integer32"""
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
          ("supported", 2),
          ("notSupported", 3))
    )


_OaQoSModuleStatus_Type.__name__ = "Integer32"
_OaQoSModuleStatus_Object = MibTableColumn
oaQoSModuleStatus = _OaQoSModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 3, 1, 3),
    _OaQoSModuleStatus_Type()
)
oaQoSModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSModuleStatus.setStatus("mandatory")
_OaQoSRun_ObjectIdentity = ObjectIdentity
oaQoSRun = _OaQoSRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10)
)


class _OaQoSCounterMode_Type(Integer32):
    """Custom type oaQoSCounterMode based on Integer32"""
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
          ("perPackets", 2),
          ("perOctets", 3))
    )


_OaQoSCounterMode_Type.__name__ = "Integer32"
_OaQoSCounterMode_Object = MibScalar
oaQoSCounterMode = _OaQoSCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 1),
    _OaQoSCounterMode_Type()
)
oaQoSCounterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaQoSCounterMode.setStatus("mandatory")


class _OaQoSTxSchedAlg_Type(Integer32):
    """Custom type oaQoSTxSchedAlg based on Integer32"""
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
        *(("other", 1),
          ("wrr", 2),
          ("hybrid1sp3wrr", 3),
          ("hybrid2sp2wrr", 4),
          ("sp", 5))
    )


_OaQoSTxSchedAlg_Type.__name__ = "Integer32"
_OaQoSTxSchedAlg_Object = MibScalar
oaQoSTxSchedAlg = _OaQoSTxSchedAlg_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 2),
    _OaQoSTxSchedAlg_Type()
)
oaQoSTxSchedAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaQoSTxSchedAlg.setStatus("mandatory")
_OaQoSQParamsTable_Object = MibTable
oaQoSQParamsTable = _OaQoSQParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 6)
)
if mibBuilder.loadTexts:
    oaQoSQParamsTable.setStatus("mandatory")
_OaQoSQParamsEntry_Object = MibTableRow
oaQoSQParamsEntry = _OaQoSQParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 6, 1)
)
oaQoSQParamsEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oaQoSQParamsQueueNumber"),
)
if mibBuilder.loadTexts:
    oaQoSQParamsEntry.setStatus("mandatory")
_OaQoSQParamsQueueNumber_Type = Integer32
_OaQoSQParamsQueueNumber_Object = MibTableColumn
oaQoSQParamsQueueNumber = _OaQoSQParamsQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 6, 1, 1),
    _OaQoSQParamsQueueNumber_Type()
)
oaQoSQParamsQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSQParamsQueueNumber.setStatus("mandatory")


class _OaQoSQParamsQueueWeight_Type(Integer32):
    """Custom type oaQoSQParamsQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OaQoSQParamsQueueWeight_Type.__name__ = "Integer32"
_OaQoSQParamsQueueWeight_Object = MibTableColumn
oaQoSQParamsQueueWeight = _OaQoSQParamsQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 6, 1, 2),
    _OaQoSQParamsQueueWeight_Type()
)
oaQoSQParamsQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaQoSQParamsQueueWeight.setStatus("mandatory")
_OaQoSTOSCfgTable_Object = MibTable
oaQoSTOSCfgTable = _OaQoSTOSCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 9)
)
if mibBuilder.loadTexts:
    oaQoSTOSCfgTable.setStatus("mandatory")
_OaQoSTOSCfgEntry_Object = MibTableRow
oaQoSTOSCfgEntry = _OaQoSTOSCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 9, 1)
)
oaQoSTOSCfgEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oaQoSTOSServiceLevel"),
)
if mibBuilder.loadTexts:
    oaQoSTOSCfgEntry.setStatus("mandatory")


class _OaQoSTOSServiceLevel_Type(Integer32):
    """Custom type oaQoSTOSServiceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OaQoSTOSServiceLevel_Type.__name__ = "Integer32"
_OaQoSTOSServiceLevel_Object = MibTableColumn
oaQoSTOSServiceLevel = _OaQoSTOSServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 9, 1, 1),
    _OaQoSTOSServiceLevel_Type()
)
oaQoSTOSServiceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSTOSServiceLevel.setStatus("mandatory")


class _OaQoSTOSvalue_Type(Integer32):
    """Custom type oaQoSTOSvalue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_OaQoSTOSvalue_Type.__name__ = "Integer32"
_OaQoSTOSvalue_Object = MibTableColumn
oaQoSTOSvalue = _OaQoSTOSvalue_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 9, 1, 2),
    _OaQoSTOSvalue_Type()
)
oaQoSTOSvalue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaQoSTOSvalue.setStatus("mandatory")


class _OaQoSTOSvalueAfterReset_Type(Integer32):
    """Custom type oaQoSTOSvalueAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_OaQoSTOSvalueAfterReset_Type.__name__ = "Integer32"
_OaQoSTOSvalueAfterReset_Object = MibTableColumn
oaQoSTOSvalueAfterReset = _OaQoSTOSvalueAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 9, 1, 3),
    _OaQoSTOSvalueAfterReset_Type()
)
oaQoSTOSvalueAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaQoSTOSvalueAfterReset.setStatus("mandatory")


class _OaQoSTOSvalueDefault_Type(Integer32):
    """Custom type oaQoSTOSvalueDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_OaQoSTOSvalueDefault_Type.__name__ = "Integer32"
_OaQoSTOSvalueDefault_Object = MibTableColumn
oaQoSTOSvalueDefault = _OaQoSTOSvalueDefault_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 9, 1, 4),
    _OaQoSTOSvalueDefault_Type()
)
oaQoSTOSvalueDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSTOSvalueDefault.setStatus("mandatory")
_OaQoSVPTCfgTable_Object = MibTable
oaQoSVPTCfgTable = _OaQoSVPTCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 10)
)
if mibBuilder.loadTexts:
    oaQoSVPTCfgTable.setStatus("mandatory")
_OaQoSVPTCfgEntry_Object = MibTableRow
oaQoSVPTCfgEntry = _OaQoSVPTCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 10, 1)
)
oaQoSVPTCfgEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oaQoSVPTServiceLevel"),
)
if mibBuilder.loadTexts:
    oaQoSVPTCfgEntry.setStatus("mandatory")


class _OaQoSVPTServiceLevel_Type(Integer32):
    """Custom type oaQoSVPTServiceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OaQoSVPTServiceLevel_Type.__name__ = "Integer32"
_OaQoSVPTServiceLevel_Object = MibTableColumn
oaQoSVPTServiceLevel = _OaQoSVPTServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 10, 1, 1),
    _OaQoSVPTServiceLevel_Type()
)
oaQoSVPTServiceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSVPTServiceLevel.setStatus("mandatory")


class _OaQoSVPTvalue_Type(Integer32):
    """Custom type oaQoSVPTvalue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OaQoSVPTvalue_Type.__name__ = "Integer32"
_OaQoSVPTvalue_Object = MibTableColumn
oaQoSVPTvalue = _OaQoSVPTvalue_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 10, 1, 2),
    _OaQoSVPTvalue_Type()
)
oaQoSVPTvalue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaQoSVPTvalue.setStatus("mandatory")


class _OaQoSVPTvalueAfterReset_Type(Integer32):
    """Custom type oaQoSVPTvalueAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OaQoSVPTvalueAfterReset_Type.__name__ = "Integer32"
_OaQoSVPTvalueAfterReset_Object = MibTableColumn
oaQoSVPTvalueAfterReset = _OaQoSVPTvalueAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 10, 1, 3),
    _OaQoSVPTvalueAfterReset_Type()
)
oaQoSVPTvalueAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaQoSVPTvalueAfterReset.setStatus("mandatory")


class _OaQoSVPTvalueDefault_Type(Integer32):
    """Custom type oaQoSVPTvalueDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OaQoSVPTvalueDefault_Type.__name__ = "Integer32"
_OaQoSVPTvalueDefault_Object = MibTableColumn
oaQoSVPTvalueDefault = _OaQoSVPTvalueDefault_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 10, 10, 1, 4),
    _OaQoSVPTvalueDefault_Type()
)
oaQoSVPTvalueDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSVPTvalueDefault.setStatus("mandatory")
_OaQoSPerm_ObjectIdentity = ObjectIdentity
oaQoSPerm = _OaQoSPerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11)
)


class _OaQoSPermCounterMode_Type(Integer32):
    """Custom type oaQoSPermCounterMode based on Integer32"""
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
          ("perPackets", 2),
          ("perOctets", 3))
    )


_OaQoSPermCounterMode_Type.__name__ = "Integer32"
_OaQoSPermCounterMode_Object = MibScalar
oaQoSPermCounterMode = _OaQoSPermCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 1),
    _OaQoSPermCounterMode_Type()
)
oaQoSPermCounterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSPermCounterMode.setStatus("mandatory")


class _OaQoSPermTxSchedAlg_Type(Integer32):
    """Custom type oaQoSPermTxSchedAlg based on Integer32"""
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
        *(("other", 1),
          ("wrr", 2),
          ("hybrid1sp3wrr", 3),
          ("hybrid2sp2wrr", 4),
          ("sp", 5))
    )


_OaQoSPermTxSchedAlg_Type.__name__ = "Integer32"
_OaQoSPermTxSchedAlg_Object = MibScalar
oaQoSPermTxSchedAlg = _OaQoSPermTxSchedAlg_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 2),
    _OaQoSPermTxSchedAlg_Type()
)
oaQoSPermTxSchedAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSPermTxSchedAlg.setStatus("mandatory")
_OaQoSPermQParamsTable_Object = MibTable
oaQoSPermQParamsTable = _OaQoSPermQParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 6)
)
if mibBuilder.loadTexts:
    oaQoSPermQParamsTable.setStatus("mandatory")
_OaQoSPermQParamsEntry_Object = MibTableRow
oaQoSPermQParamsEntry = _OaQoSPermQParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 6, 1)
)
oaQoSPermQParamsEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oaQoSPermQParamsQueueNumber"),
)
if mibBuilder.loadTexts:
    oaQoSPermQParamsEntry.setStatus("mandatory")
_OaQoSPermQParamsQueueNumber_Type = Integer32
_OaQoSPermQParamsQueueNumber_Object = MibTableColumn
oaQoSPermQParamsQueueNumber = _OaQoSPermQParamsQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 6, 1, 1),
    _OaQoSPermQParamsQueueNumber_Type()
)
oaQoSPermQParamsQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSPermQParamsQueueNumber.setStatus("mandatory")


class _OaQoSPermQParamsQueueWeight_Type(Integer32):
    """Custom type oaQoSPermQParamsQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OaQoSPermQParamsQueueWeight_Type.__name__ = "Integer32"
_OaQoSPermQParamsQueueWeight_Object = MibTableColumn
oaQoSPermQParamsQueueWeight = _OaQoSPermQParamsQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 6, 1, 2),
    _OaQoSPermQParamsQueueWeight_Type()
)
oaQoSPermQParamsQueueWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSPermQParamsQueueWeight.setStatus("mandatory")
_OaQoSPermTOSCfgTable_Object = MibTable
oaQoSPermTOSCfgTable = _OaQoSPermTOSCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 9)
)
if mibBuilder.loadTexts:
    oaQoSPermTOSCfgTable.setStatus("mandatory")
_OaQoSPermTOSCfgEntry_Object = MibTableRow
oaQoSPermTOSCfgEntry = _OaQoSPermTOSCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 9, 1)
)
oaQoSPermTOSCfgEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oaQoSPermTOSServiceLevel"),
)
if mibBuilder.loadTexts:
    oaQoSPermTOSCfgEntry.setStatus("mandatory")


class _OaQoSPermTOSServiceLevel_Type(Integer32):
    """Custom type oaQoSPermTOSServiceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OaQoSPermTOSServiceLevel_Type.__name__ = "Integer32"
_OaQoSPermTOSServiceLevel_Object = MibTableColumn
oaQoSPermTOSServiceLevel = _OaQoSPermTOSServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 9, 1, 1),
    _OaQoSPermTOSServiceLevel_Type()
)
oaQoSPermTOSServiceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSPermTOSServiceLevel.setStatus("mandatory")


class _OaQoSPermTOSvalue_Type(Integer32):
    """Custom type oaQoSPermTOSvalue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_OaQoSPermTOSvalue_Type.__name__ = "Integer32"
_OaQoSPermTOSvalue_Object = MibTableColumn
oaQoSPermTOSvalue = _OaQoSPermTOSvalue_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 9, 1, 2),
    _OaQoSPermTOSvalue_Type()
)
oaQoSPermTOSvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSPermTOSvalue.setStatus("mandatory")
_OaQoSPermVPTCfgTable_Object = MibTable
oaQoSPermVPTCfgTable = _OaQoSPermVPTCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 10)
)
if mibBuilder.loadTexts:
    oaQoSPermVPTCfgTable.setStatus("mandatory")
_OaQoSPermVPTCfgEntry_Object = MibTableRow
oaQoSPermVPTCfgEntry = _OaQoSPermVPTCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 10, 1)
)
oaQoSPermVPTCfgEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oaQoSPermVPTServiceLevel"),
)
if mibBuilder.loadTexts:
    oaQoSPermVPTCfgEntry.setStatus("mandatory")


class _OaQoSPermVPTServiceLevel_Type(Integer32):
    """Custom type oaQoSPermVPTServiceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_OaQoSPermVPTServiceLevel_Type.__name__ = "Integer32"
_OaQoSPermVPTServiceLevel_Object = MibTableColumn
oaQoSPermVPTServiceLevel = _OaQoSPermVPTServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 10, 1, 1),
    _OaQoSPermVPTServiceLevel_Type()
)
oaQoSPermVPTServiceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSPermVPTServiceLevel.setStatus("mandatory")


class _OaQoSPermVPTvalue_Type(Integer32):
    """Custom type oaQoSPermVPTvalue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OaQoSPermVPTvalue_Type.__name__ = "Integer32"
_OaQoSPermVPTvalue_Object = MibTableColumn
oaQoSPermVPTvalue = _OaQoSPermVPTvalue_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 21, 2, 11, 10, 1, 2),
    _OaQoSPermVPTvalue_Type()
)
oaQoSPermVPTvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaQoSPermVPTvalue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-QOS-MIB",
    **{"oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaClassification": oaClassification,
       "oaQoS": oaQoS,
       "oaQoSSaveMode": oaQoSSaveMode,
       "oaQoSMaxPriorQueuesNumber": oaQoSMaxPriorQueuesNumber,
       "oaQoSModuleStatusTable": oaQoSModuleStatusTable,
       "oaQoSModuleStatusEntry": oaQoSModuleStatusEntry,
       "oaQoSSlotId": oaQoSSlotId,
       "oaQoSModuleId": oaQoSModuleId,
       "oaQoSModuleStatus": oaQoSModuleStatus,
       "oaQoSRun": oaQoSRun,
       "oaQoSCounterMode": oaQoSCounterMode,
       "oaQoSTxSchedAlg": oaQoSTxSchedAlg,
       "oaQoSQParamsTable": oaQoSQParamsTable,
       "oaQoSQParamsEntry": oaQoSQParamsEntry,
       "oaQoSQParamsQueueNumber": oaQoSQParamsQueueNumber,
       "oaQoSQParamsQueueWeight": oaQoSQParamsQueueWeight,
       "oaQoSTOSCfgTable": oaQoSTOSCfgTable,
       "oaQoSTOSCfgEntry": oaQoSTOSCfgEntry,
       "oaQoSTOSServiceLevel": oaQoSTOSServiceLevel,
       "oaQoSTOSvalue": oaQoSTOSvalue,
       "oaQoSTOSvalueAfterReset": oaQoSTOSvalueAfterReset,
       "oaQoSTOSvalueDefault": oaQoSTOSvalueDefault,
       "oaQoSVPTCfgTable": oaQoSVPTCfgTable,
       "oaQoSVPTCfgEntry": oaQoSVPTCfgEntry,
       "oaQoSVPTServiceLevel": oaQoSVPTServiceLevel,
       "oaQoSVPTvalue": oaQoSVPTvalue,
       "oaQoSVPTvalueAfterReset": oaQoSVPTvalueAfterReset,
       "oaQoSVPTvalueDefault": oaQoSVPTvalueDefault,
       "oaQoSPerm": oaQoSPerm,
       "oaQoSPermCounterMode": oaQoSPermCounterMode,
       "oaQoSPermTxSchedAlg": oaQoSPermTxSchedAlg,
       "oaQoSPermQParamsTable": oaQoSPermQParamsTable,
       "oaQoSPermQParamsEntry": oaQoSPermQParamsEntry,
       "oaQoSPermQParamsQueueNumber": oaQoSPermQParamsQueueNumber,
       "oaQoSPermQParamsQueueWeight": oaQoSPermQParamsQueueWeight,
       "oaQoSPermTOSCfgTable": oaQoSPermTOSCfgTable,
       "oaQoSPermTOSCfgEntry": oaQoSPermTOSCfgEntry,
       "oaQoSPermTOSServiceLevel": oaQoSPermTOSServiceLevel,
       "oaQoSPermTOSvalue": oaQoSPermTOSvalue,
       "oaQoSPermVPTCfgTable": oaQoSPermVPTCfgTable,
       "oaQoSPermVPTCfgEntry": oaQoSPermVPTCfgEntry,
       "oaQoSPermVPTServiceLevel": oaQoSPermVPTServiceLevel,
       "oaQoSPermVPTvalue": oaQoSPermVPTvalue}
)
