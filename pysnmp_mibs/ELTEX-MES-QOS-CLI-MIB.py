# SNMP MIB module (ELTEX-MES-QOS-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-QOS-CLI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:34 2025
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

(eltMesQosCliMib,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesQosCliMib")

(AceActionType,
 AceObjectType,
 AclDefaultAction,
 AclObjectType,
 BinaryStatus,
 ClassMapAction,
 InterfaceType,
 RlQosAceTidxActionDropType,
 rlQosAceTidxEntry,
 rlQosClassMapIndex,
 rlQosIfPolicyEntry,
 rlQosPolicerEntry,
 rlQosTupleEntry) = mibBuilder.importSymbols(
    "RADLAN-QOS-CLI-MIB",
    "AceActionType",
    "AceObjectType",
    "AclDefaultAction",
    "AclObjectType",
    "BinaryStatus",
    "ClassMapAction",
    "InterfaceType",
    "RlQosAceTidxActionDropType",
    "rlQosAceTidxEntry",
    "rlQosClassMapIndex",
    "rlQosIfPolicyEntry",
    "rlQosPolicerEntry",
    "rlQosTupleEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EltQosIfTrustMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cos", 1),
          ("dscp", 2),
          ("cos-dscp", 3))
    )



class EltQosMappingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cos-dscp", 0),
          ("dscp-cos", 1))
    )



class EltQosAclConfMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("commit", 2))
    )



class EltQosAceTidxCommitAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("add", 1),
          ("delete", 2))
    )



class EltQosTupleState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 0),
          ("temporary", 1))
    )



class EltQosTrafficLimiterMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("pps", 1))
    )



class EltPolicerAction(TextualConvention, Integer32):
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
        *(("none", 1),
          ("drop", 2),
          ("remark", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EltQosOffsetListTable_Object = MibTable
eltQosOffsetListTable = _EltQosOffsetListTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1)
)
if mibBuilder.loadTexts:
    eltQosOffsetListTable.setStatus("current")
_EltQosOffsetListEntry_Object = MibTableRow
eltQosOffsetListEntry = _EltQosOffsetListEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1)
)
eltQosOffsetListEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosAclIndex"),
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosOffsetListName"),
)
if mibBuilder.loadTexts:
    eltQosOffsetListEntry.setStatus("current")
_EltQosAclIndex_Type = Integer32
_EltQosAclIndex_Object = MibTableColumn
eltQosAclIndex = _EltQosAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 1),
    _EltQosAclIndex_Type()
)
eltQosAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAclIndex.setStatus("current")


class _EltQosOffsetListName_Type(OctetString):
    """Custom type eltQosOffsetListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltQosOffsetListName_Type.__name__ = "OctetString"
_EltQosOffsetListName_Object = MibTableColumn
eltQosOffsetListName = _EltQosOffsetListName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 2),
    _EltQosOffsetListName_Type()
)
eltQosOffsetListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosOffsetListName.setStatus("current")
_EltQosOffsetListOffsetPointer1_Type = Integer32
_EltQosOffsetListOffsetPointer1_Object = MibTableColumn
eltQosOffsetListOffsetPointer1 = _EltQosOffsetListOffsetPointer1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 3),
    _EltQosOffsetListOffsetPointer1_Type()
)
eltQosOffsetListOffsetPointer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer1.setStatus("current")
_EltQosOffsetListOffsetPointer2_Type = Integer32
_EltQosOffsetListOffsetPointer2_Object = MibTableColumn
eltQosOffsetListOffsetPointer2 = _EltQosOffsetListOffsetPointer2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 4),
    _EltQosOffsetListOffsetPointer2_Type()
)
eltQosOffsetListOffsetPointer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer2.setStatus("current")
_EltQosOffsetListOffsetPointer3_Type = Integer32
_EltQosOffsetListOffsetPointer3_Object = MibTableColumn
eltQosOffsetListOffsetPointer3 = _EltQosOffsetListOffsetPointer3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 5),
    _EltQosOffsetListOffsetPointer3_Type()
)
eltQosOffsetListOffsetPointer3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer3.setStatus("current")
_EltQosOffsetListOffsetPointer4_Type = Integer32
_EltQosOffsetListOffsetPointer4_Object = MibTableColumn
eltQosOffsetListOffsetPointer4 = _EltQosOffsetListOffsetPointer4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 6),
    _EltQosOffsetListOffsetPointer4_Type()
)
eltQosOffsetListOffsetPointer4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer4.setStatus("current")
_EltQosOffsetListOffsetPointer5_Type = Integer32
_EltQosOffsetListOffsetPointer5_Object = MibTableColumn
eltQosOffsetListOffsetPointer5 = _EltQosOffsetListOffsetPointer5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 7),
    _EltQosOffsetListOffsetPointer5_Type()
)
eltQosOffsetListOffsetPointer5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer5.setStatus("current")
_EltQosOffsetListStatus_Type = RowStatus
_EltQosOffsetListStatus_Object = MibTableColumn
eltQosOffsetListStatus = _EltQosOffsetListStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 8),
    _EltQosOffsetListStatus_Type()
)
eltQosOffsetListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListStatus.setStatus("current")
_EltQosOffsetListOffsetPointer6_Type = Integer32
_EltQosOffsetListOffsetPointer6_Object = MibTableColumn
eltQosOffsetListOffsetPointer6 = _EltQosOffsetListOffsetPointer6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 9),
    _EltQosOffsetListOffsetPointer6_Type()
)
eltQosOffsetListOffsetPointer6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer6.setStatus("current")
_EltQosOffsetListOffsetPointer7_Type = Integer32
_EltQosOffsetListOffsetPointer7_Object = MibTableColumn
eltQosOffsetListOffsetPointer7 = _EltQosOffsetListOffsetPointer7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 10),
    _EltQosOffsetListOffsetPointer7_Type()
)
eltQosOffsetListOffsetPointer7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer7.setStatus("current")
_EltQosOffsetListOffsetPointer8_Type = Integer32
_EltQosOffsetListOffsetPointer8_Object = MibTableColumn
eltQosOffsetListOffsetPointer8 = _EltQosOffsetListOffsetPointer8_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 11),
    _EltQosOffsetListOffsetPointer8_Type()
)
eltQosOffsetListOffsetPointer8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer8.setStatus("current")
_EltQosOffsetListOffsetPointer9_Type = Integer32
_EltQosOffsetListOffsetPointer9_Object = MibTableColumn
eltQosOffsetListOffsetPointer9 = _EltQosOffsetListOffsetPointer9_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 12),
    _EltQosOffsetListOffsetPointer9_Type()
)
eltQosOffsetListOffsetPointer9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer9.setStatus("current")
_EltQosOffsetListOffsetPointer10_Type = Integer32
_EltQosOffsetListOffsetPointer10_Object = MibTableColumn
eltQosOffsetListOffsetPointer10 = _EltQosOffsetListOffsetPointer10_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 13),
    _EltQosOffsetListOffsetPointer10_Type()
)
eltQosOffsetListOffsetPointer10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer10.setStatus("current")
_EltQosOffsetListOffsetPointer11_Type = Integer32
_EltQosOffsetListOffsetPointer11_Object = MibTableColumn
eltQosOffsetListOffsetPointer11 = _EltQosOffsetListOffsetPointer11_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 14),
    _EltQosOffsetListOffsetPointer11_Type()
)
eltQosOffsetListOffsetPointer11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer11.setStatus("current")
_EltQosOffsetListOffsetPointer12_Type = Integer32
_EltQosOffsetListOffsetPointer12_Object = MibTableColumn
eltQosOffsetListOffsetPointer12 = _EltQosOffsetListOffsetPointer12_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 15),
    _EltQosOffsetListOffsetPointer12_Type()
)
eltQosOffsetListOffsetPointer12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer12.setStatus("current")
_EltQosOffsetListOffsetPointer13_Type = Integer32
_EltQosOffsetListOffsetPointer13_Object = MibTableColumn
eltQosOffsetListOffsetPointer13 = _EltQosOffsetListOffsetPointer13_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 16),
    _EltQosOffsetListOffsetPointer13_Type()
)
eltQosOffsetListOffsetPointer13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer13.setStatus("current")
_EltQosOffsetListOffsetPointer14_Type = Integer32
_EltQosOffsetListOffsetPointer14_Object = MibTableColumn
eltQosOffsetListOffsetPointer14 = _EltQosOffsetListOffsetPointer14_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 17),
    _EltQosOffsetListOffsetPointer14_Type()
)
eltQosOffsetListOffsetPointer14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer14.setStatus("current")
_EltQosOffsetListOffsetPointer15_Type = Integer32
_EltQosOffsetListOffsetPointer15_Object = MibTableColumn
eltQosOffsetListOffsetPointer15 = _EltQosOffsetListOffsetPointer15_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 1, 1, 18),
    _EltQosOffsetListOffsetPointer15_Type()
)
eltQosOffsetListOffsetPointer15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosOffsetListOffsetPointer15.setStatus("current")
_EltQosClassMapActionCfgTable_Object = MibTable
eltQosClassMapActionCfgTable = _EltQosClassMapActionCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 5)
)
if mibBuilder.loadTexts:
    eltQosClassMapActionCfgTable.setStatus("current")
_EltQosClassMapActionCfgEntry_Object = MibTableRow
eltQosClassMapActionCfgEntry = _EltQosClassMapActionCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 5, 1)
)
eltQosClassMapActionCfgEntry.setIndexNames(
    (0, "RADLAN-QOS-CLI-MIB", "rlQosClassMapIndex"),
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosClassMapActionCfgAction"),
)
if mibBuilder.loadTexts:
    eltQosClassMapActionCfgEntry.setStatus("current")
_EltQosClassMapActionCfgAction_Type = ClassMapAction
_EltQosClassMapActionCfgAction_Object = MibTableColumn
eltQosClassMapActionCfgAction = _EltQosClassMapActionCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 5, 1, 1),
    _EltQosClassMapActionCfgAction_Type()
)
eltQosClassMapActionCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosClassMapActionCfgAction.setStatus("current")
_EltQosClassMapActionCfgValue_Type = Integer32
_EltQosClassMapActionCfgValue_Object = MibTableColumn
eltQosClassMapActionCfgValue = _EltQosClassMapActionCfgValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 5, 1, 2),
    _EltQosClassMapActionCfgValue_Type()
)
eltQosClassMapActionCfgValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosClassMapActionCfgValue.setStatus("current")
_EltQosClassMapActionCfgStatus_Type = RowStatus
_EltQosClassMapActionCfgStatus_Object = MibTableColumn
eltQosClassMapActionCfgStatus = _EltQosClassMapActionCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 5, 1, 3),
    _EltQosClassMapActionCfgStatus_Type()
)
eltQosClassMapActionCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosClassMapActionCfgStatus.setStatus("current")
_EltQosDscpToCosTable_Object = MibTable
eltQosDscpToCosTable = _EltQosDscpToCosTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 6)
)
if mibBuilder.loadTexts:
    eltQosDscpToCosTable.setStatus("current")
_EltQosDscpToCosEntry_Object = MibTableRow
eltQosDscpToCosEntry = _EltQosDscpToCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 6, 1)
)
eltQosDscpToCosEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosDscp"),
)
if mibBuilder.loadTexts:
    eltQosDscpToCosEntry.setStatus("current")


class _EltQosDscp_Type(Integer32):
    """Custom type eltQosDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_EltQosDscp_Type.__name__ = "Integer32"
_EltQosDscp_Object = MibTableColumn
eltQosDscp = _EltQosDscp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 6, 1, 1),
    _EltQosDscp_Type()
)
eltQosDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosDscp.setStatus("current")


class _EltQosCos_Type(Integer32):
    """Custom type eltQosCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EltQosCos_Type.__name__ = "Integer32"
_EltQosCos_Object = MibTableColumn
eltQosCos = _EltQosCos_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 6, 1, 2),
    _EltQosCos_Type()
)
eltQosCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosCos.setStatus("current")
_EltQosCosToDscpTable_Object = MibTable
eltQosCosToDscpTable = _EltQosCosToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 7)
)
if mibBuilder.loadTexts:
    eltQosCosToDscpTable.setStatus("current")
_EltQosCosToDscpEntry_Object = MibTableRow
eltQosCosToDscpEntry = _EltQosCosToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 7, 1)
)
eltQosCosToDscpEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosCosIndex"),
)
if mibBuilder.loadTexts:
    eltQosCosToDscpEntry.setStatus("current")


class _EltQosCosIndex_Type(Integer32):
    """Custom type eltQosCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EltQosCosIndex_Type.__name__ = "Integer32"
_EltQosCosIndex_Object = MibTableColumn
eltQosCosIndex = _EltQosCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 7, 1, 1),
    _EltQosCosIndex_Type()
)
eltQosCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosCosIndex.setStatus("current")


class _EltQosDscpValue_Type(Integer32):
    """Custom type eltQosDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_EltQosDscpValue_Type.__name__ = "Integer32"
_EltQosDscpValue_Object = MibTableColumn
eltQosDscpValue = _EltQosDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 7, 1, 2),
    _EltQosDscpValue_Type()
)
eltQosDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosDscpValue.setStatus("current")
_EltQosIfConfigTable_Object = MibTable
eltQosIfConfigTable = _EltQosIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 8)
)
if mibBuilder.loadTexts:
    eltQosIfConfigTable.setStatus("current")
_EltQosIfConfigEntry_Object = MibTableRow
eltQosIfConfigEntry = _EltQosIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 8, 1)
)
if mibBuilder.loadTexts:
    eltQosIfConfigEntry.setStatus("current")
_EltQosIfTrustMode_Type = EltQosIfTrustMode
_EltQosIfTrustMode_Object = MibTableColumn
eltQosIfTrustMode = _EltQosIfTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 8, 1, 1),
    _EltQosIfTrustMode_Type()
)
eltQosIfTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosIfTrustMode.setStatus("current")


class _EltQosIfCirPortRateLimitPps_Type(Unsigned32):
    """Custom type eltQosIfCirPortRateLimitPps based on Unsigned32"""
    defaultValue = 0


_EltQosIfCirPortRateLimitPps_Type.__name__ = "Unsigned32"
_EltQosIfCirPortRateLimitPps_Object = MibTableColumn
eltQosIfCirPortRateLimitPps = _EltQosIfCirPortRateLimitPps_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 8, 1, 2),
    _EltQosIfCirPortRateLimitPps_Type()
)
eltQosIfCirPortRateLimitPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosIfCirPortRateLimitPps.setStatus("current")


class _EltQosIfCbsPortRateLimitPackets_Type(Unsigned32):
    """Custom type eltQosIfCbsPortRateLimitPackets based on Unsigned32"""
    defaultValue = 0


_EltQosIfCbsPortRateLimitPackets_Type.__name__ = "Unsigned32"
_EltQosIfCbsPortRateLimitPackets_Object = MibTableColumn
eltQosIfCbsPortRateLimitPackets = _EltQosIfCbsPortRateLimitPackets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 8, 1, 3),
    _EltQosIfCbsPortRateLimitPackets_Type()
)
eltQosIfCbsPortRateLimitPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosIfCbsPortRateLimitPackets.setStatus("current")
_EltQosMappingCfgTable_Object = MibTable
eltQosMappingCfgTable = _EltQosMappingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 9)
)
if mibBuilder.loadTexts:
    eltQosMappingCfgTable.setStatus("current")
_EltQosMappingCfgEntry_Object = MibTableRow
eltQosMappingCfgEntry = _EltQosMappingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 9, 1)
)
eltQosMappingCfgEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosMappingCfgIndex"),
)
if mibBuilder.loadTexts:
    eltQosMappingCfgEntry.setStatus("current")
_EltQosMappingCfgIndex_Type = EltQosMappingType
_EltQosMappingCfgIndex_Object = MibTableColumn
eltQosMappingCfgIndex = _EltQosMappingCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 9, 1, 1),
    _EltQosMappingCfgIndex_Type()
)
eltQosMappingCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosMappingCfgIndex.setStatus("current")


class _EltQosMappingCfgEnable_Type(TruthValue):
    """Custom type eltQosMappingCfgEnable based on TruthValue"""
    defaultValue = 2


_EltQosMappingCfgEnable_Type.__name__ = "TruthValue"
_EltQosMappingCfgEnable_Object = MibTableColumn
eltQosMappingCfgEnable = _EltQosMappingCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 9, 1, 2),
    _EltQosMappingCfgEnable_Type()
)
eltQosMappingCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosMappingCfgEnable.setStatus("current")
_EltQosAceTidxTable_Object = MibTable
eltQosAceTidxTable = _EltQosAceTidxTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10)
)
if mibBuilder.loadTexts:
    eltQosAceTidxTable.setStatus("current")
_EltQosAceTidxEntry_Object = MibTableRow
eltQosAceTidxEntry = _EltQosAceTidxEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1)
)
if mibBuilder.loadTexts:
    eltQosAceTidxEntry.setStatus("current")
_EltQosAceTidxTuple1_Type = Integer32
_EltQosAceTidxTuple1_Object = MibTableColumn
eltQosAceTidxTuple1 = _EltQosAceTidxTuple1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 1),
    _EltQosAceTidxTuple1_Type()
)
eltQosAceTidxTuple1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple1.setStatus("current")
_EltQosAceTidxTuple2_Type = Integer32
_EltQosAceTidxTuple2_Object = MibTableColumn
eltQosAceTidxTuple2 = _EltQosAceTidxTuple2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 2),
    _EltQosAceTidxTuple2_Type()
)
eltQosAceTidxTuple2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple2.setStatus("current")
_EltQosAceTidxTuple3_Type = Integer32
_EltQosAceTidxTuple3_Object = MibTableColumn
eltQosAceTidxTuple3 = _EltQosAceTidxTuple3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 3),
    _EltQosAceTidxTuple3_Type()
)
eltQosAceTidxTuple3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple3.setStatus("current")
_EltQosAceTidxTuple4_Type = Integer32
_EltQosAceTidxTuple4_Object = MibTableColumn
eltQosAceTidxTuple4 = _EltQosAceTidxTuple4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 4),
    _EltQosAceTidxTuple4_Type()
)
eltQosAceTidxTuple4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple4.setStatus("current")
_EltQosAceTidxTuple5_Type = Integer32
_EltQosAceTidxTuple5_Object = MibTableColumn
eltQosAceTidxTuple5 = _EltQosAceTidxTuple5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 5),
    _EltQosAceTidxTuple5_Type()
)
eltQosAceTidxTuple5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple5.setStatus("current")
_EltQosAceTidxTuple6_Type = Integer32
_EltQosAceTidxTuple6_Object = MibTableColumn
eltQosAceTidxTuple6 = _EltQosAceTidxTuple6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 6),
    _EltQosAceTidxTuple6_Type()
)
eltQosAceTidxTuple6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple6.setStatus("current")
_EltQosAceTidxTuple7_Type = Integer32
_EltQosAceTidxTuple7_Object = MibTableColumn
eltQosAceTidxTuple7 = _EltQosAceTidxTuple7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 7),
    _EltQosAceTidxTuple7_Type()
)
eltQosAceTidxTuple7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple7.setStatus("current")
_EltQosAceTidxTuple8_Type = Integer32
_EltQosAceTidxTuple8_Object = MibTableColumn
eltQosAceTidxTuple8 = _EltQosAceTidxTuple8_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 8),
    _EltQosAceTidxTuple8_Type()
)
eltQosAceTidxTuple8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple8.setStatus("current")
_EltQosAceTidxTuple9_Type = Integer32
_EltQosAceTidxTuple9_Object = MibTableColumn
eltQosAceTidxTuple9 = _EltQosAceTidxTuple9_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 9),
    _EltQosAceTidxTuple9_Type()
)
eltQosAceTidxTuple9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple9.setStatus("current")
_EltQosAceTidxTuple10_Type = Integer32
_EltQosAceTidxTuple10_Object = MibTableColumn
eltQosAceTidxTuple10 = _EltQosAceTidxTuple10_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 10),
    _EltQosAceTidxTuple10_Type()
)
eltQosAceTidxTuple10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple10.setStatus("current")
_EltQosAceTidxTuple11_Type = Integer32
_EltQosAceTidxTuple11_Object = MibTableColumn
eltQosAceTidxTuple11 = _EltQosAceTidxTuple11_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 11),
    _EltQosAceTidxTuple11_Type()
)
eltQosAceTidxTuple11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple11.setStatus("current")
_EltQosAceTidxTuple12_Type = Integer32
_EltQosAceTidxTuple12_Object = MibTableColumn
eltQosAceTidxTuple12 = _EltQosAceTidxTuple12_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 12),
    _EltQosAceTidxTuple12_Type()
)
eltQosAceTidxTuple12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple12.setStatus("current")
_EltQosAceTidxTuple13_Type = Integer32
_EltQosAceTidxTuple13_Object = MibTableColumn
eltQosAceTidxTuple13 = _EltQosAceTidxTuple13_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 13),
    _EltQosAceTidxTuple13_Type()
)
eltQosAceTidxTuple13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple13.setStatus("current")
_EltQosAceTidxTuple14_Type = Integer32
_EltQosAceTidxTuple14_Object = MibTableColumn
eltQosAceTidxTuple14 = _EltQosAceTidxTuple14_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 14),
    _EltQosAceTidxTuple14_Type()
)
eltQosAceTidxTuple14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple14.setStatus("current")
_EltQosAceTidxTuple15_Type = Integer32
_EltQosAceTidxTuple15_Object = MibTableColumn
eltQosAceTidxTuple15 = _EltQosAceTidxTuple15_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 10, 1, 15),
    _EltQosAceTidxTuple15_Type()
)
eltQosAceTidxTuple15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTuple15.setStatus("current")
_EltQosTupleTable_Object = MibTable
eltQosTupleTable = _EltQosTupleTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 12)
)
if mibBuilder.loadTexts:
    eltQosTupleTable.setStatus("current")
_EltQosTupleEntry_Object = MibTableRow
eltQosTupleEntry = _EltQosTupleEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 12, 1)
)
if mibBuilder.loadTexts:
    eltQosTupleEntry.setStatus("current")


class _EltQosTupleState_Type(EltQosTupleState):
    """Custom type eltQosTupleState based on EltQosTupleState"""
    defaultValue = 0


_EltQosTupleState_Type.__name__ = "EltQosTupleState"
_EltQosTupleState_Object = MibTableColumn
eltQosTupleState = _EltQosTupleState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 12, 1, 1),
    _EltQosTupleState_Type()
)
eltQosTupleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosTupleState.setStatus("current")
_EltMesQosCandidateConfigMib_ObjectIdentity = ObjectIdentity
eltMesQosCandidateConfigMib = _EltMesQosCandidateConfigMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13)
)
_EltQosIfConfigTempTable_Object = MibTable
eltQosIfConfigTempTable = _EltQosIfConfigTempTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1)
)
if mibBuilder.loadTexts:
    eltQosIfConfigTempTable.setStatus("current")
_EltQosIfConfigTempEntry_Object = MibTableRow
eltQosIfConfigTempEntry = _EltQosIfConfigTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1)
)
eltQosIfConfigTempEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosIfConfigTempIndex"),
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosIfConfigTempType"),
)
if mibBuilder.loadTexts:
    eltQosIfConfigTempEntry.setStatus("current")
_EltQosIfConfigTempIndex_Type = Integer32
_EltQosIfConfigTempIndex_Object = MibTableColumn
eltQosIfConfigTempIndex = _EltQosIfConfigTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1, 1),
    _EltQosIfConfigTempIndex_Type()
)
eltQosIfConfigTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosIfConfigTempIndex.setStatus("current")
_EltQosIfConfigTempType_Type = InterfaceType
_EltQosIfConfigTempType_Object = MibTableColumn
eltQosIfConfigTempType = _EltQosIfConfigTempType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1, 2),
    _EltQosIfConfigTempType_Type()
)
eltQosIfConfigTempType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosIfConfigTempType.setStatus("current")
_EltQosIfConfigRowStatus_Type = RowStatus
_EltQosIfConfigRowStatus_Object = MibTableColumn
eltQosIfConfigRowStatus = _EltQosIfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1, 3),
    _EltQosIfConfigRowStatus_Type()
)
eltQosIfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosIfConfigRowStatus.setStatus("current")


class _EltQosIfConfigTempAclIn_Type(Integer32):
    """Custom type eltQosIfConfigTempAclIn based on Integer32"""
    defaultValue = 0


_EltQosIfConfigTempAclIn_Type.__name__ = "Integer32"
_EltQosIfConfigTempAclIn_Object = MibTableColumn
eltQosIfConfigTempAclIn = _EltQosIfConfigTempAclIn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1, 4),
    _EltQosIfConfigTempAclIn_Type()
)
eltQosIfConfigTempAclIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosIfConfigTempAclIn.setStatus("current")


class _EltQosIfConfigTempAclOut_Type(Integer32):
    """Custom type eltQosIfConfigTempAclOut based on Integer32"""
    defaultValue = 0


_EltQosIfConfigTempAclOut_Type.__name__ = "Integer32"
_EltQosIfConfigTempAclOut_Object = MibTableColumn
eltQosIfConfigTempAclOut = _EltQosIfConfigTempAclOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1, 5),
    _EltQosIfConfigTempAclOut_Type()
)
eltQosIfConfigTempAclOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosIfConfigTempAclOut.setStatus("current")


class _EltQosIfConfigTempIpv6AclIn_Type(Integer32):
    """Custom type eltQosIfConfigTempIpv6AclIn based on Integer32"""
    defaultValue = 0


_EltQosIfConfigTempIpv6AclIn_Type.__name__ = "Integer32"
_EltQosIfConfigTempIpv6AclIn_Object = MibTableColumn
eltQosIfConfigTempIpv6AclIn = _EltQosIfConfigTempIpv6AclIn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1, 6),
    _EltQosIfConfigTempIpv6AclIn_Type()
)
eltQosIfConfigTempIpv6AclIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosIfConfigTempIpv6AclIn.setStatus("current")


class _EltQosIfConfigTempIpv6AclOut_Type(Integer32):
    """Custom type eltQosIfConfigTempIpv6AclOut based on Integer32"""
    defaultValue = 0


_EltQosIfConfigTempIpv6AclOut_Type.__name__ = "Integer32"
_EltQosIfConfigTempIpv6AclOut_Object = MibTableColumn
eltQosIfConfigTempIpv6AclOut = _EltQosIfConfigTempIpv6AclOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1, 7),
    _EltQosIfConfigTempIpv6AclOut_Type()
)
eltQosIfConfigTempIpv6AclOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosIfConfigTempIpv6AclOut.setStatus("current")
_EltQosIfConfigTempAclDefaultAction_Type = AclDefaultAction
_EltQosIfConfigTempAclDefaultAction_Object = MibTableColumn
eltQosIfConfigTempAclDefaultAction = _EltQosIfConfigTempAclDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1, 8),
    _EltQosIfConfigTempAclDefaultAction_Type()
)
eltQosIfConfigTempAclDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosIfConfigTempAclDefaultAction.setStatus("current")
_EltQosIfConfigTempAclDefaultActionOut_Type = AclDefaultAction
_EltQosIfConfigTempAclDefaultActionOut_Object = MibTableColumn
eltQosIfConfigTempAclDefaultActionOut = _EltQosIfConfigTempAclDefaultActionOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 1, 1, 9),
    _EltQosIfConfigTempAclDefaultActionOut_Type()
)
eltQosIfConfigTempAclDefaultActionOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosIfConfigTempAclDefaultActionOut.setStatus("current")


class _EltQosAclConfMode_Type(EltQosAclConfMode):
    """Custom type eltQosAclConfMode based on EltQosAclConfMode"""
    defaultValue = 1


_EltQosAclConfMode_Type.__name__ = "EltQosAclConfMode"
_EltQosAclConfMode_Object = MibScalar
eltQosAclConfMode = _EltQosAclConfMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 2),
    _EltQosAclConfMode_Type()
)
eltQosAclConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosAclConfMode.setStatus("current")
_EltQosAceTidxTempTable_Object = MibTable
eltQosAceTidxTempTable = _EltQosAceTidxTempTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3)
)
if mibBuilder.loadTexts:
    eltQosAceTidxTempTable.setStatus("current")
_EltQosAceTidxTempEntry_Object = MibTableRow
eltQosAceTidxTempEntry = _EltQosAceTidxTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1)
)
eltQosAceTidxTempEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosAceTidxTempAclIndex"),
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosAceTidxTempIndex"),
)
if mibBuilder.loadTexts:
    eltQosAceTidxTempEntry.setStatus("current")
_EltQosAceTidxTempAclIndex_Type = Integer32
_EltQosAceTidxTempAclIndex_Object = MibTableColumn
eltQosAceTidxTempAclIndex = _EltQosAceTidxTempAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 1),
    _EltQosAceTidxTempAclIndex_Type()
)
eltQosAceTidxTempAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosAceTidxTempAclIndex.setStatus("current")
_EltQosAceTidxTempIndex_Type = Integer32
_EltQosAceTidxTempIndex_Object = MibTableColumn
eltQosAceTidxTempIndex = _EltQosAceTidxTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 2),
    _EltQosAceTidxTempIndex_Type()
)
eltQosAceTidxTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosAceTidxTempIndex.setStatus("current")
_EltQosAceTidxTempStatus_Type = RowStatus
_EltQosAceTidxTempStatus_Object = MibTableColumn
eltQosAceTidxTempStatus = _EltQosAceTidxTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 3),
    _EltQosAceTidxTempStatus_Type()
)
eltQosAceTidxTempStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempStatus.setStatus("current")
_EltQosAceTidxTempAction_Type = AceActionType
_EltQosAceTidxTempAction_Object = MibTableColumn
eltQosAceTidxTempAction = _EltQosAceTidxTempAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 4),
    _EltQosAceTidxTempAction_Type()
)
eltQosAceTidxTempAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempAction.setStatus("current")
_EltQosAceTidxTempType_Type = AceObjectType
_EltQosAceTidxTempType_Object = MibTableColumn
eltQosAceTidxTempType = _EltQosAceTidxTempType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 5),
    _EltQosAceTidxTempType_Type()
)
eltQosAceTidxTempType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempType.setStatus("current")
_EltQosAceTidxTempActionDropType_Type = RlQosAceTidxActionDropType
_EltQosAceTidxTempActionDropType_Object = MibTableColumn
eltQosAceTidxTempActionDropType = _EltQosAceTidxTempActionDropType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 6),
    _EltQosAceTidxTempActionDropType_Type()
)
eltQosAceTidxTempActionDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempActionDropType.setStatus("current")
_EltQosAceTidxTempAccount_Type = BinaryStatus
_EltQosAceTidxTempAccount_Object = MibTableColumn
eltQosAceTidxTempAccount = _EltQosAceTidxTempAccount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 7),
    _EltQosAceTidxTempAccount_Type()
)
eltQosAceTidxTempAccount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempAccount.setStatus("current")


class _EltQosAceTidxTempTimeRange_Type(DisplayString):
    """Custom type eltQosAceTidxTempTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltQosAceTidxTempTimeRange_Type.__name__ = "DisplayString"
_EltQosAceTidxTempTimeRange_Object = MibTableColumn
eltQosAceTidxTempTimeRange = _EltQosAceTidxTempTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 8),
    _EltQosAceTidxTempTimeRange_Type()
)
eltQosAceTidxTempTimeRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTimeRange.setStatus("current")
_EltQosAceTidxTempCommitAction_Type = EltQosAceTidxCommitAction
_EltQosAceTidxTempCommitAction_Object = MibTableColumn
eltQosAceTidxTempCommitAction = _EltQosAceTidxTempCommitAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 9),
    _EltQosAceTidxTempCommitAction_Type()
)
eltQosAceTidxTempCommitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempCommitAction.setStatus("current")
_EltQosAceTidxTempTuple1_Type = Integer32
_EltQosAceTidxTempTuple1_Object = MibTableColumn
eltQosAceTidxTempTuple1 = _EltQosAceTidxTempTuple1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 10),
    _EltQosAceTidxTempTuple1_Type()
)
eltQosAceTidxTempTuple1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple1.setStatus("current")
_EltQosAceTidxTempTuple2_Type = Integer32
_EltQosAceTidxTempTuple2_Object = MibTableColumn
eltQosAceTidxTempTuple2 = _EltQosAceTidxTempTuple2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 11),
    _EltQosAceTidxTempTuple2_Type()
)
eltQosAceTidxTempTuple2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple2.setStatus("current")
_EltQosAceTidxTempTuple3_Type = Integer32
_EltQosAceTidxTempTuple3_Object = MibTableColumn
eltQosAceTidxTempTuple3 = _EltQosAceTidxTempTuple3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 12),
    _EltQosAceTidxTempTuple3_Type()
)
eltQosAceTidxTempTuple3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple3.setStatus("current")
_EltQosAceTidxTempTuple4_Type = Integer32
_EltQosAceTidxTempTuple4_Object = MibTableColumn
eltQosAceTidxTempTuple4 = _EltQosAceTidxTempTuple4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 13),
    _EltQosAceTidxTempTuple4_Type()
)
eltQosAceTidxTempTuple4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple4.setStatus("current")
_EltQosAceTidxTempTuple5_Type = Integer32
_EltQosAceTidxTempTuple5_Object = MibTableColumn
eltQosAceTidxTempTuple5 = _EltQosAceTidxTempTuple5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 14),
    _EltQosAceTidxTempTuple5_Type()
)
eltQosAceTidxTempTuple5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple5.setStatus("current")
_EltQosAceTidxTempTuple6_Type = Integer32
_EltQosAceTidxTempTuple6_Object = MibTableColumn
eltQosAceTidxTempTuple6 = _EltQosAceTidxTempTuple6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 15),
    _EltQosAceTidxTempTuple6_Type()
)
eltQosAceTidxTempTuple6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple6.setStatus("current")
_EltQosAceTidxTempTuple7_Type = Integer32
_EltQosAceTidxTempTuple7_Object = MibTableColumn
eltQosAceTidxTempTuple7 = _EltQosAceTidxTempTuple7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 16),
    _EltQosAceTidxTempTuple7_Type()
)
eltQosAceTidxTempTuple7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple7.setStatus("current")
_EltQosAceTidxTempTuple8_Type = Integer32
_EltQosAceTidxTempTuple8_Object = MibTableColumn
eltQosAceTidxTempTuple8 = _EltQosAceTidxTempTuple8_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 17),
    _EltQosAceTidxTempTuple8_Type()
)
eltQosAceTidxTempTuple8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple8.setStatus("current")
_EltQosAceTidxTempTuple9_Type = Integer32
_EltQosAceTidxTempTuple9_Object = MibTableColumn
eltQosAceTidxTempTuple9 = _EltQosAceTidxTempTuple9_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 18),
    _EltQosAceTidxTempTuple9_Type()
)
eltQosAceTidxTempTuple9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple9.setStatus("current")
_EltQosAceTidxTempTuple10_Type = Integer32
_EltQosAceTidxTempTuple10_Object = MibTableColumn
eltQosAceTidxTempTuple10 = _EltQosAceTidxTempTuple10_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 19),
    _EltQosAceTidxTempTuple10_Type()
)
eltQosAceTidxTempTuple10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple10.setStatus("current")
_EltQosAceTidxTempTuple11_Type = Integer32
_EltQosAceTidxTempTuple11_Object = MibTableColumn
eltQosAceTidxTempTuple11 = _EltQosAceTidxTempTuple11_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 20),
    _EltQosAceTidxTempTuple11_Type()
)
eltQosAceTidxTempTuple11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple11.setStatus("current")
_EltQosAceTidxTempTuple12_Type = Integer32
_EltQosAceTidxTempTuple12_Object = MibTableColumn
eltQosAceTidxTempTuple12 = _EltQosAceTidxTempTuple12_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 21),
    _EltQosAceTidxTempTuple12_Type()
)
eltQosAceTidxTempTuple12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple12.setStatus("current")
_EltQosAceTidxTempTuple13_Type = Integer32
_EltQosAceTidxTempTuple13_Object = MibTableColumn
eltQosAceTidxTempTuple13 = _EltQosAceTidxTempTuple13_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 22),
    _EltQosAceTidxTempTuple13_Type()
)
eltQosAceTidxTempTuple13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple13.setStatus("current")
_EltQosAceTidxTempTuple14_Type = Integer32
_EltQosAceTidxTempTuple14_Object = MibTableColumn
eltQosAceTidxTempTuple14 = _EltQosAceTidxTempTuple14_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 23),
    _EltQosAceTidxTempTuple14_Type()
)
eltQosAceTidxTempTuple14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple14.setStatus("current")
_EltQosAceTidxTempTuple15_Type = Integer32
_EltQosAceTidxTempTuple15_Object = MibTableColumn
eltQosAceTidxTempTuple15 = _EltQosAceTidxTempTuple15_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 24),
    _EltQosAceTidxTempTuple15_Type()
)
eltQosAceTidxTempTuple15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple15.setStatus("current")
_EltQosAceTidxTempTuple16_Type = Integer32
_EltQosAceTidxTempTuple16_Object = MibTableColumn
eltQosAceTidxTempTuple16 = _EltQosAceTidxTempTuple16_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 25),
    _EltQosAceTidxTempTuple16_Type()
)
eltQosAceTidxTempTuple16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple16.setStatus("current")
_EltQosAceTidxTempTuple17_Type = Integer32
_EltQosAceTidxTempTuple17_Object = MibTableColumn
eltQosAceTidxTempTuple17 = _EltQosAceTidxTempTuple17_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 26),
    _EltQosAceTidxTempTuple17_Type()
)
eltQosAceTidxTempTuple17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple17.setStatus("current")
_EltQosAceTidxTempTuple18_Type = Integer32
_EltQosAceTidxTempTuple18_Object = MibTableColumn
eltQosAceTidxTempTuple18 = _EltQosAceTidxTempTuple18_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 27),
    _EltQosAceTidxTempTuple18_Type()
)
eltQosAceTidxTempTuple18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple18.setStatus("current")
_EltQosAceTidxTempTuple19_Type = Integer32
_EltQosAceTidxTempTuple19_Object = MibTableColumn
eltQosAceTidxTempTuple19 = _EltQosAceTidxTempTuple19_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 28),
    _EltQosAceTidxTempTuple19_Type()
)
eltQosAceTidxTempTuple19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple19.setStatus("current")
_EltQosAceTidxTempTuple20_Type = Integer32
_EltQosAceTidxTempTuple20_Object = MibTableColumn
eltQosAceTidxTempTuple20 = _EltQosAceTidxTempTuple20_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 29),
    _EltQosAceTidxTempTuple20_Type()
)
eltQosAceTidxTempTuple20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple20.setStatus("current")
_EltQosAceTidxTempTuple21_Type = Integer32
_EltQosAceTidxTempTuple21_Object = MibTableColumn
eltQosAceTidxTempTuple21 = _EltQosAceTidxTempTuple21_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 30),
    _EltQosAceTidxTempTuple21_Type()
)
eltQosAceTidxTempTuple21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple21.setStatus("current")
_EltQosAceTidxTempTuple22_Type = Integer32
_EltQosAceTidxTempTuple22_Object = MibTableColumn
eltQosAceTidxTempTuple22 = _EltQosAceTidxTempTuple22_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 31),
    _EltQosAceTidxTempTuple22_Type()
)
eltQosAceTidxTempTuple22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple22.setStatus("current")
_EltQosAceTidxTempTuple23_Type = Integer32
_EltQosAceTidxTempTuple23_Object = MibTableColumn
eltQosAceTidxTempTuple23 = _EltQosAceTidxTempTuple23_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 32),
    _EltQosAceTidxTempTuple23_Type()
)
eltQosAceTidxTempTuple23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple23.setStatus("current")
_EltQosAceTidxTempTuple24_Type = Integer32
_EltQosAceTidxTempTuple24_Object = MibTableColumn
eltQosAceTidxTempTuple24 = _EltQosAceTidxTempTuple24_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 33),
    _EltQosAceTidxTempTuple24_Type()
)
eltQosAceTidxTempTuple24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple24.setStatus("current")
_EltQosAceTidxTempTuple25_Type = Integer32
_EltQosAceTidxTempTuple25_Object = MibTableColumn
eltQosAceTidxTempTuple25 = _EltQosAceTidxTempTuple25_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 34),
    _EltQosAceTidxTempTuple25_Type()
)
eltQosAceTidxTempTuple25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple25.setStatus("current")
_EltQosAceTidxTempTuple26_Type = Integer32
_EltQosAceTidxTempTuple26_Object = MibTableColumn
eltQosAceTidxTempTuple26 = _EltQosAceTidxTempTuple26_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 3, 1, 35),
    _EltQosAceTidxTempTuple26_Type()
)
eltQosAceTidxTempTuple26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltQosAceTidxTempTuple26.setStatus("current")
_EltQosAceTidxCandidateTable_Object = MibTable
eltQosAceTidxCandidateTable = _EltQosAceTidxCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4)
)
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTable.setStatus("current")
_EltQosAceTidxCandidateEntry_Object = MibTableRow
eltQosAceTidxCandidateEntry = _EltQosAceTidxCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1)
)
eltQosAceTidxCandidateEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosAceTidxCandidateAclIndex"),
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosAceTidxCandidateIndex"),
)
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateEntry.setStatus("current")
_EltQosAceTidxCandidateAclIndex_Type = Integer32
_EltQosAceTidxCandidateAclIndex_Object = MibTableColumn
eltQosAceTidxCandidateAclIndex = _EltQosAceTidxCandidateAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 1),
    _EltQosAceTidxCandidateAclIndex_Type()
)
eltQosAceTidxCandidateAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateAclIndex.setStatus("current")
_EltQosAceTidxCandidateIndex_Type = Integer32
_EltQosAceTidxCandidateIndex_Object = MibTableColumn
eltQosAceTidxCandidateIndex = _EltQosAceTidxCandidateIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 2),
    _EltQosAceTidxCandidateIndex_Type()
)
eltQosAceTidxCandidateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateIndex.setStatus("current")
_EltQosAceTidxCandidateAction_Type = AceActionType
_EltQosAceTidxCandidateAction_Object = MibTableColumn
eltQosAceTidxCandidateAction = _EltQosAceTidxCandidateAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 3),
    _EltQosAceTidxCandidateAction_Type()
)
eltQosAceTidxCandidateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateAction.setStatus("current")
_EltQosAceTidxCandidateType_Type = AceObjectType
_EltQosAceTidxCandidateType_Object = MibTableColumn
eltQosAceTidxCandidateType = _EltQosAceTidxCandidateType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 4),
    _EltQosAceTidxCandidateType_Type()
)
eltQosAceTidxCandidateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateType.setStatus("current")
_EltQosAceTidxCandidateTuple1_Type = Integer32
_EltQosAceTidxCandidateTuple1_Object = MibTableColumn
eltQosAceTidxCandidateTuple1 = _EltQosAceTidxCandidateTuple1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 5),
    _EltQosAceTidxCandidateTuple1_Type()
)
eltQosAceTidxCandidateTuple1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple1.setStatus("current")
_EltQosAceTidxCandidateTuple2_Type = Integer32
_EltQosAceTidxCandidateTuple2_Object = MibTableColumn
eltQosAceTidxCandidateTuple2 = _EltQosAceTidxCandidateTuple2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 6),
    _EltQosAceTidxCandidateTuple2_Type()
)
eltQosAceTidxCandidateTuple2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple2.setStatus("current")
_EltQosAceTidxCandidateTuple3_Type = Integer32
_EltQosAceTidxCandidateTuple3_Object = MibTableColumn
eltQosAceTidxCandidateTuple3 = _EltQosAceTidxCandidateTuple3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 7),
    _EltQosAceTidxCandidateTuple3_Type()
)
eltQosAceTidxCandidateTuple3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple3.setStatus("current")
_EltQosAceTidxCandidateTuple4_Type = Integer32
_EltQosAceTidxCandidateTuple4_Object = MibTableColumn
eltQosAceTidxCandidateTuple4 = _EltQosAceTidxCandidateTuple4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 8),
    _EltQosAceTidxCandidateTuple4_Type()
)
eltQosAceTidxCandidateTuple4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple4.setStatus("current")
_EltQosAceTidxCandidateTuple5_Type = Integer32
_EltQosAceTidxCandidateTuple5_Object = MibTableColumn
eltQosAceTidxCandidateTuple5 = _EltQosAceTidxCandidateTuple5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 9),
    _EltQosAceTidxCandidateTuple5_Type()
)
eltQosAceTidxCandidateTuple5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple5.setStatus("current")
_EltQosAceTidxCandidateTuple6_Type = Integer32
_EltQosAceTidxCandidateTuple6_Object = MibTableColumn
eltQosAceTidxCandidateTuple6 = _EltQosAceTidxCandidateTuple6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 10),
    _EltQosAceTidxCandidateTuple6_Type()
)
eltQosAceTidxCandidateTuple6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple6.setStatus("current")
_EltQosAceTidxCandidateTuple7_Type = Integer32
_EltQosAceTidxCandidateTuple7_Object = MibTableColumn
eltQosAceTidxCandidateTuple7 = _EltQosAceTidxCandidateTuple7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 11),
    _EltQosAceTidxCandidateTuple7_Type()
)
eltQosAceTidxCandidateTuple7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple7.setStatus("current")
_EltQosAceTidxCandidateTuple8_Type = Integer32
_EltQosAceTidxCandidateTuple8_Object = MibTableColumn
eltQosAceTidxCandidateTuple8 = _EltQosAceTidxCandidateTuple8_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 12),
    _EltQosAceTidxCandidateTuple8_Type()
)
eltQosAceTidxCandidateTuple8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple8.setStatus("current")
_EltQosAceTidxCandidateAccount_Type = BinaryStatus
_EltQosAceTidxCandidateAccount_Object = MibTableColumn
eltQosAceTidxCandidateAccount = _EltQosAceTidxCandidateAccount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 13),
    _EltQosAceTidxCandidateAccount_Type()
)
eltQosAceTidxCandidateAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateAccount.setStatus("current")
_EltQosAceTidxCandidateStatus_Type = RowStatus
_EltQosAceTidxCandidateStatus_Object = MibTableColumn
eltQosAceTidxCandidateStatus = _EltQosAceTidxCandidateStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 14),
    _EltQosAceTidxCandidateStatus_Type()
)
eltQosAceTidxCandidateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateStatus.setStatus("current")


class _EltQosAceTidxCandidateTimeRange_Type(DisplayString):
    """Custom type eltQosAceTidxCandidateTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltQosAceTidxCandidateTimeRange_Type.__name__ = "DisplayString"
_EltQosAceTidxCandidateTimeRange_Object = MibTableColumn
eltQosAceTidxCandidateTimeRange = _EltQosAceTidxCandidateTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 15),
    _EltQosAceTidxCandidateTimeRange_Type()
)
eltQosAceTidxCandidateTimeRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTimeRange.setStatus("current")
_EltQosAceTidxCandidateTimeRangeIsActive_Type = TruthValue
_EltQosAceTidxCandidateTimeRangeIsActive_Object = MibTableColumn
eltQosAceTidxCandidateTimeRangeIsActive = _EltQosAceTidxCandidateTimeRangeIsActive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 16),
    _EltQosAceTidxCandidateTimeRangeIsActive_Type()
)
eltQosAceTidxCandidateTimeRangeIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTimeRangeIsActive.setStatus("current")
_EltQosAceTidxCandidateTuple9_Type = Integer32
_EltQosAceTidxCandidateTuple9_Object = MibTableColumn
eltQosAceTidxCandidateTuple9 = _EltQosAceTidxCandidateTuple9_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 17),
    _EltQosAceTidxCandidateTuple9_Type()
)
eltQosAceTidxCandidateTuple9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple9.setStatus("current")
_EltQosAceTidxCandidateTuple10_Type = Integer32
_EltQosAceTidxCandidateTuple10_Object = MibTableColumn
eltQosAceTidxCandidateTuple10 = _EltQosAceTidxCandidateTuple10_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 18),
    _EltQosAceTidxCandidateTuple10_Type()
)
eltQosAceTidxCandidateTuple10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple10.setStatus("current")
_EltQosAceTidxCandidateTuple11_Type = Integer32
_EltQosAceTidxCandidateTuple11_Object = MibTableColumn
eltQosAceTidxCandidateTuple11 = _EltQosAceTidxCandidateTuple11_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 19),
    _EltQosAceTidxCandidateTuple11_Type()
)
eltQosAceTidxCandidateTuple11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple11.setStatus("current")
_EltQosAceTidxCandidateActionDropType_Type = RlQosAceTidxActionDropType
_EltQosAceTidxCandidateActionDropType_Object = MibTableColumn
eltQosAceTidxCandidateActionDropType = _EltQosAceTidxCandidateActionDropType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 20),
    _EltQosAceTidxCandidateActionDropType_Type()
)
eltQosAceTidxCandidateActionDropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateActionDropType.setStatus("current")
_EltQosAceTidxCandidateTuple12_Type = Integer32
_EltQosAceTidxCandidateTuple12_Object = MibTableColumn
eltQosAceTidxCandidateTuple12 = _EltQosAceTidxCandidateTuple12_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 21),
    _EltQosAceTidxCandidateTuple12_Type()
)
eltQosAceTidxCandidateTuple12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple12.setStatus("current")
_EltQosAceTidxCandidateTuple13_Type = Integer32
_EltQosAceTidxCandidateTuple13_Object = MibTableColumn
eltQosAceTidxCandidateTuple13 = _EltQosAceTidxCandidateTuple13_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 22),
    _EltQosAceTidxCandidateTuple13_Type()
)
eltQosAceTidxCandidateTuple13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple13.setStatus("current")
_EltQosAceTidxCandidateTuple14_Type = Integer32
_EltQosAceTidxCandidateTuple14_Object = MibTableColumn
eltQosAceTidxCandidateTuple14 = _EltQosAceTidxCandidateTuple14_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 23),
    _EltQosAceTidxCandidateTuple14_Type()
)
eltQosAceTidxCandidateTuple14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple14.setStatus("current")
_EltQosAceTidxCandidateTuple15_Type = Integer32
_EltQosAceTidxCandidateTuple15_Object = MibTableColumn
eltQosAceTidxCandidateTuple15 = _EltQosAceTidxCandidateTuple15_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 24),
    _EltQosAceTidxCandidateTuple15_Type()
)
eltQosAceTidxCandidateTuple15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple15.setStatus("current")
_EltQosAceTidxCandidateTuple16_Type = Integer32
_EltQosAceTidxCandidateTuple16_Object = MibTableColumn
eltQosAceTidxCandidateTuple16 = _EltQosAceTidxCandidateTuple16_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 25),
    _EltQosAceTidxCandidateTuple16_Type()
)
eltQosAceTidxCandidateTuple16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple16.setStatus("current")
_EltQosAceTidxCandidateTuple17_Type = Integer32
_EltQosAceTidxCandidateTuple17_Object = MibTableColumn
eltQosAceTidxCandidateTuple17 = _EltQosAceTidxCandidateTuple17_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 26),
    _EltQosAceTidxCandidateTuple17_Type()
)
eltQosAceTidxCandidateTuple17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple17.setStatus("current")
_EltQosAceTidxCandidateTuple18_Type = Integer32
_EltQosAceTidxCandidateTuple18_Object = MibTableColumn
eltQosAceTidxCandidateTuple18 = _EltQosAceTidxCandidateTuple18_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 27),
    _EltQosAceTidxCandidateTuple18_Type()
)
eltQosAceTidxCandidateTuple18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple18.setStatus("current")
_EltQosAceTidxCandidateTuple19_Type = Integer32
_EltQosAceTidxCandidateTuple19_Object = MibTableColumn
eltQosAceTidxCandidateTuple19 = _EltQosAceTidxCandidateTuple19_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 28),
    _EltQosAceTidxCandidateTuple19_Type()
)
eltQosAceTidxCandidateTuple19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple19.setStatus("current")
_EltQosAceTidxCandidateTuple20_Type = Integer32
_EltQosAceTidxCandidateTuple20_Object = MibTableColumn
eltQosAceTidxCandidateTuple20 = _EltQosAceTidxCandidateTuple20_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 29),
    _EltQosAceTidxCandidateTuple20_Type()
)
eltQosAceTidxCandidateTuple20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple20.setStatus("current")
_EltQosAceTidxCandidateTuple21_Type = Integer32
_EltQosAceTidxCandidateTuple21_Object = MibTableColumn
eltQosAceTidxCandidateTuple21 = _EltQosAceTidxCandidateTuple21_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 30),
    _EltQosAceTidxCandidateTuple21_Type()
)
eltQosAceTidxCandidateTuple21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple21.setStatus("current")
_EltQosAceTidxCandidateTuple22_Type = Integer32
_EltQosAceTidxCandidateTuple22_Object = MibTableColumn
eltQosAceTidxCandidateTuple22 = _EltQosAceTidxCandidateTuple22_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 31),
    _EltQosAceTidxCandidateTuple22_Type()
)
eltQosAceTidxCandidateTuple22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple22.setStatus("current")
_EltQosAceTidxCandidateTuple23_Type = Integer32
_EltQosAceTidxCandidateTuple23_Object = MibTableColumn
eltQosAceTidxCandidateTuple23 = _EltQosAceTidxCandidateTuple23_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 32),
    _EltQosAceTidxCandidateTuple23_Type()
)
eltQosAceTidxCandidateTuple23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple23.setStatus("current")
_EltQosAceTidxCandidateTuple24_Type = Integer32
_EltQosAceTidxCandidateTuple24_Object = MibTableColumn
eltQosAceTidxCandidateTuple24 = _EltQosAceTidxCandidateTuple24_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 33),
    _EltQosAceTidxCandidateTuple24_Type()
)
eltQosAceTidxCandidateTuple24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple24.setStatus("current")
_EltQosAceTidxCandidateTuple25_Type = Integer32
_EltQosAceTidxCandidateTuple25_Object = MibTableColumn
eltQosAceTidxCandidateTuple25 = _EltQosAceTidxCandidateTuple25_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 34),
    _EltQosAceTidxCandidateTuple25_Type()
)
eltQosAceTidxCandidateTuple25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple25.setStatus("current")
_EltQosAceTidxCandidateTuple26_Type = Integer32
_EltQosAceTidxCandidateTuple26_Object = MibTableColumn
eltQosAceTidxCandidateTuple26 = _EltQosAceTidxCandidateTuple26_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 4, 1, 35),
    _EltQosAceTidxCandidateTuple26_Type()
)
eltQosAceTidxCandidateTuple26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAceTidxCandidateTuple26.setStatus("current")
_EltQosAclCandidateTable_Object = MibTable
eltQosAclCandidateTable = _EltQosAclCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 5)
)
if mibBuilder.loadTexts:
    eltQosAclCandidateTable.setStatus("current")
_EltQosAclCandidateEntry_Object = MibTableRow
eltQosAclCandidateEntry = _EltQosAclCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 5, 1)
)
eltQosAclCandidateEntry.setIndexNames(
    (0, "ELTEX-MES-QOS-CLI-MIB", "eltQosAclCandidateIndex"),
)
if mibBuilder.loadTexts:
    eltQosAclCandidateEntry.setStatus("current")
_EltQosAclCandidateIndex_Type = Integer32
_EltQosAclCandidateIndex_Object = MibTableColumn
eltQosAclCandidateIndex = _EltQosAclCandidateIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 5, 1, 1),
    _EltQosAclCandidateIndex_Type()
)
eltQosAclCandidateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltQosAclCandidateIndex.setStatus("current")


class _EltQosAclCandidateName_Type(DisplayString):
    """Custom type eltQosAclCandidateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltQosAclCandidateName_Type.__name__ = "DisplayString"
_EltQosAclCandidateName_Object = MibTableColumn
eltQosAclCandidateName = _EltQosAclCandidateName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 5, 1, 2),
    _EltQosAclCandidateName_Type()
)
eltQosAclCandidateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAclCandidateName.setStatus("current")
_EltQosAclCandidateType_Type = AclObjectType
_EltQosAclCandidateType_Object = MibTableColumn
eltQosAclCandidateType = _EltQosAclCandidateType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 5, 1, 3),
    _EltQosAclCandidateType_Type()
)
eltQosAclCandidateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAclCandidateType.setStatus("current")
_EltQosAclCandidateStatus_Type = RowStatus
_EltQosAclCandidateStatus_Object = MibTableColumn
eltQosAclCandidateStatus = _EltQosAclCandidateStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 5, 1, 4),
    _EltQosAclCandidateStatus_Type()
)
eltQosAclCandidateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAclCandidateStatus.setStatus("current")
_EltQosAclCandidateNumOfAces_Type = Integer32
_EltQosAclCandidateNumOfAces_Object = MibTableColumn
eltQosAclCandidateNumOfAces = _EltQosAclCandidateNumOfAces_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 5, 1, 5),
    _EltQosAclCandidateNumOfAces_Type()
)
eltQosAclCandidateNumOfAces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltQosAclCandidateNumOfAces.setStatus("current")


class _EltQosDeleteCandidateAction_Type(Integer32):
    """Custom type eltQosDeleteCandidateAction based on Integer32"""
    defaultValue = 0


_EltQosDeleteCandidateAction_Type.__name__ = "Integer32"
_EltQosDeleteCandidateAction_Object = MibScalar
eltQosDeleteCandidateAction = _EltQosDeleteCandidateAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 13, 6),
    _EltQosDeleteCandidateAction_Type()
)
eltQosDeleteCandidateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosDeleteCandidateAction.setStatus("current")


class _EltQosTrafficLimiterMode_Type(EltQosTrafficLimiterMode):
    """Custom type eltQosTrafficLimiterMode based on EltQosTrafficLimiterMode"""
    defaultValue = 0


_EltQosTrafficLimiterMode_Type.__name__ = "EltQosTrafficLimiterMode"
_EltQosTrafficLimiterMode_Object = MibScalar
eltQosTrafficLimiterMode = _EltQosTrafficLimiterMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 14),
    _EltQosTrafficLimiterMode_Type()
)
eltQosTrafficLimiterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosTrafficLimiterMode.setStatus("current")
_EltQosPolicerConfigTable_Object = MibTable
eltQosPolicerConfigTable = _EltQosPolicerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 15)
)
if mibBuilder.loadTexts:
    eltQosPolicerConfigTable.setStatus("current")
_EltQosPolicerConfigEntry_Object = MibTableRow
eltQosPolicerConfigEntry = _EltQosPolicerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 15, 1)
)
if mibBuilder.loadTexts:
    eltQosPolicerConfigEntry.setStatus("current")


class _EltQosPolicerConfigCirPps_Type(Unsigned32):
    """Custom type eltQosPolicerConfigCirPps based on Unsigned32"""
    defaultValue = 0


_EltQosPolicerConfigCirPps_Type.__name__ = "Unsigned32"
_EltQosPolicerConfigCirPps_Object = MibTableColumn
eltQosPolicerConfigCirPps = _EltQosPolicerConfigCirPps_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 15, 1, 1),
    _EltQosPolicerConfigCirPps_Type()
)
eltQosPolicerConfigCirPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosPolicerConfigCirPps.setStatus("current")


class _EltQosPolicerConfigCbsPakets_Type(Unsigned32):
    """Custom type eltQosPolicerConfigCbsPakets based on Unsigned32"""
    defaultValue = 0


_EltQosPolicerConfigCbsPakets_Type.__name__ = "Unsigned32"
_EltQosPolicerConfigCbsPakets_Object = MibTableColumn
eltQosPolicerConfigCbsPakets = _EltQosPolicerConfigCbsPakets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 15, 1, 2),
    _EltQosPolicerConfigCbsPakets_Type()
)
eltQosPolicerConfigCbsPakets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosPolicerConfigCbsPakets.setStatus("current")
_EltQosPolicerConfigPpsAction_Type = EltPolicerAction
_EltQosPolicerConfigPpsAction_Object = MibTableColumn
eltQosPolicerConfigPpsAction = _EltQosPolicerConfigPpsAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 15, 1, 3),
    _EltQosPolicerConfigPpsAction_Type()
)
eltQosPolicerConfigPpsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosPolicerConfigPpsAction.setStatus("current")


class _EltQosPolicerConfigPirPps_Type(Unsigned32):
    """Custom type eltQosPolicerConfigPirPps based on Unsigned32"""
    defaultValue = 0


_EltQosPolicerConfigPirPps_Type.__name__ = "Unsigned32"
_EltQosPolicerConfigPirPps_Object = MibTableColumn
eltQosPolicerConfigPirPps = _EltQosPolicerConfigPirPps_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 15, 1, 4),
    _EltQosPolicerConfigPirPps_Type()
)
eltQosPolicerConfigPirPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosPolicerConfigPirPps.setStatus("current")


class _EltQosPolicerConfigPbsPakets_Type(Unsigned32):
    """Custom type eltQosPolicerConfigPbsPakets based on Unsigned32"""
    defaultValue = 0


_EltQosPolicerConfigPbsPakets_Type.__name__ = "Unsigned32"
_EltQosPolicerConfigPbsPakets_Object = MibTableColumn
eltQosPolicerConfigPbsPakets = _EltQosPolicerConfigPbsPakets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 15, 1, 5),
    _EltQosPolicerConfigPbsPakets_Type()
)
eltQosPolicerConfigPbsPakets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosPolicerConfigPbsPakets.setStatus("current")
_EltQosPolicerConfigPpsPeakAction_Type = EltPolicerAction
_EltQosPolicerConfigPpsPeakAction_Object = MibTableColumn
eltQosPolicerConfigPpsPeakAction = _EltQosPolicerConfigPpsPeakAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 88, 15, 1, 6),
    _EltQosPolicerConfigPpsPeakAction_Type()
)
eltQosPolicerConfigPpsPeakAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltQosPolicerConfigPpsPeakAction.setStatus("current")
rlQosIfPolicyEntry.registerAugmentions(
    ("ELTEX-MES-QOS-CLI-MIB",
     "eltQosIfConfigEntry")
)
eltQosIfConfigEntry.setIndexNames(*rlQosIfPolicyEntry.getIndexNames())
rlQosAceTidxEntry.registerAugmentions(
    ("ELTEX-MES-QOS-CLI-MIB",
     "eltQosAceTidxEntry")
)
eltQosAceTidxEntry.setIndexNames(*rlQosAceTidxEntry.getIndexNames())
rlQosTupleEntry.registerAugmentions(
    ("ELTEX-MES-QOS-CLI-MIB",
     "eltQosTupleEntry")
)
eltQosTupleEntry.setIndexNames(*rlQosTupleEntry.getIndexNames())
rlQosPolicerEntry.registerAugmentions(
    ("ELTEX-MES-QOS-CLI-MIB",
     "eltQosPolicerConfigEntry")
)
eltQosPolicerConfigEntry.setIndexNames(*rlQosPolicerEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-QOS-CLI-MIB",
    **{"EltQosIfTrustMode": EltQosIfTrustMode,
       "EltQosMappingType": EltQosMappingType,
       "EltQosAclConfMode": EltQosAclConfMode,
       "EltQosAceTidxCommitAction": EltQosAceTidxCommitAction,
       "EltQosTupleState": EltQosTupleState,
       "EltQosTrafficLimiterMode": EltQosTrafficLimiterMode,
       "EltPolicerAction": EltPolicerAction,
       "eltQosOffsetListTable": eltQosOffsetListTable,
       "eltQosOffsetListEntry": eltQosOffsetListEntry,
       "eltQosAclIndex": eltQosAclIndex,
       "eltQosOffsetListName": eltQosOffsetListName,
       "eltQosOffsetListOffsetPointer1": eltQosOffsetListOffsetPointer1,
       "eltQosOffsetListOffsetPointer2": eltQosOffsetListOffsetPointer2,
       "eltQosOffsetListOffsetPointer3": eltQosOffsetListOffsetPointer3,
       "eltQosOffsetListOffsetPointer4": eltQosOffsetListOffsetPointer4,
       "eltQosOffsetListOffsetPointer5": eltQosOffsetListOffsetPointer5,
       "eltQosOffsetListStatus": eltQosOffsetListStatus,
       "eltQosOffsetListOffsetPointer6": eltQosOffsetListOffsetPointer6,
       "eltQosOffsetListOffsetPointer7": eltQosOffsetListOffsetPointer7,
       "eltQosOffsetListOffsetPointer8": eltQosOffsetListOffsetPointer8,
       "eltQosOffsetListOffsetPointer9": eltQosOffsetListOffsetPointer9,
       "eltQosOffsetListOffsetPointer10": eltQosOffsetListOffsetPointer10,
       "eltQosOffsetListOffsetPointer11": eltQosOffsetListOffsetPointer11,
       "eltQosOffsetListOffsetPointer12": eltQosOffsetListOffsetPointer12,
       "eltQosOffsetListOffsetPointer13": eltQosOffsetListOffsetPointer13,
       "eltQosOffsetListOffsetPointer14": eltQosOffsetListOffsetPointer14,
       "eltQosOffsetListOffsetPointer15": eltQosOffsetListOffsetPointer15,
       "eltQosClassMapActionCfgTable": eltQosClassMapActionCfgTable,
       "eltQosClassMapActionCfgEntry": eltQosClassMapActionCfgEntry,
       "eltQosClassMapActionCfgAction": eltQosClassMapActionCfgAction,
       "eltQosClassMapActionCfgValue": eltQosClassMapActionCfgValue,
       "eltQosClassMapActionCfgStatus": eltQosClassMapActionCfgStatus,
       "eltQosDscpToCosTable": eltQosDscpToCosTable,
       "eltQosDscpToCosEntry": eltQosDscpToCosEntry,
       "eltQosDscp": eltQosDscp,
       "eltQosCos": eltQosCos,
       "eltQosCosToDscpTable": eltQosCosToDscpTable,
       "eltQosCosToDscpEntry": eltQosCosToDscpEntry,
       "eltQosCosIndex": eltQosCosIndex,
       "eltQosDscpValue": eltQosDscpValue,
       "eltQosIfConfigTable": eltQosIfConfigTable,
       "eltQosIfConfigEntry": eltQosIfConfigEntry,
       "eltQosIfTrustMode": eltQosIfTrustMode,
       "eltQosIfCirPortRateLimitPps": eltQosIfCirPortRateLimitPps,
       "eltQosIfCbsPortRateLimitPackets": eltQosIfCbsPortRateLimitPackets,
       "eltQosMappingCfgTable": eltQosMappingCfgTable,
       "eltQosMappingCfgEntry": eltQosMappingCfgEntry,
       "eltQosMappingCfgIndex": eltQosMappingCfgIndex,
       "eltQosMappingCfgEnable": eltQosMappingCfgEnable,
       "eltQosAceTidxTable": eltQosAceTidxTable,
       "eltQosAceTidxEntry": eltQosAceTidxEntry,
       "eltQosAceTidxTuple1": eltQosAceTidxTuple1,
       "eltQosAceTidxTuple2": eltQosAceTidxTuple2,
       "eltQosAceTidxTuple3": eltQosAceTidxTuple3,
       "eltQosAceTidxTuple4": eltQosAceTidxTuple4,
       "eltQosAceTidxTuple5": eltQosAceTidxTuple5,
       "eltQosAceTidxTuple6": eltQosAceTidxTuple6,
       "eltQosAceTidxTuple7": eltQosAceTidxTuple7,
       "eltQosAceTidxTuple8": eltQosAceTidxTuple8,
       "eltQosAceTidxTuple9": eltQosAceTidxTuple9,
       "eltQosAceTidxTuple10": eltQosAceTidxTuple10,
       "eltQosAceTidxTuple11": eltQosAceTidxTuple11,
       "eltQosAceTidxTuple12": eltQosAceTidxTuple12,
       "eltQosAceTidxTuple13": eltQosAceTidxTuple13,
       "eltQosAceTidxTuple14": eltQosAceTidxTuple14,
       "eltQosAceTidxTuple15": eltQosAceTidxTuple15,
       "eltQosTupleTable": eltQosTupleTable,
       "eltQosTupleEntry": eltQosTupleEntry,
       "eltQosTupleState": eltQosTupleState,
       "eltMesQosCandidateConfigMib": eltMesQosCandidateConfigMib,
       "eltQosIfConfigTempTable": eltQosIfConfigTempTable,
       "eltQosIfConfigTempEntry": eltQosIfConfigTempEntry,
       "eltQosIfConfigTempIndex": eltQosIfConfigTempIndex,
       "eltQosIfConfigTempType": eltQosIfConfigTempType,
       "eltQosIfConfigRowStatus": eltQosIfConfigRowStatus,
       "eltQosIfConfigTempAclIn": eltQosIfConfigTempAclIn,
       "eltQosIfConfigTempAclOut": eltQosIfConfigTempAclOut,
       "eltQosIfConfigTempIpv6AclIn": eltQosIfConfigTempIpv6AclIn,
       "eltQosIfConfigTempIpv6AclOut": eltQosIfConfigTempIpv6AclOut,
       "eltQosIfConfigTempAclDefaultAction": eltQosIfConfigTempAclDefaultAction,
       "eltQosIfConfigTempAclDefaultActionOut": eltQosIfConfigTempAclDefaultActionOut,
       "eltQosAclConfMode": eltQosAclConfMode,
       "eltQosAceTidxTempTable": eltQosAceTidxTempTable,
       "eltQosAceTidxTempEntry": eltQosAceTidxTempEntry,
       "eltQosAceTidxTempAclIndex": eltQosAceTidxTempAclIndex,
       "eltQosAceTidxTempIndex": eltQosAceTidxTempIndex,
       "eltQosAceTidxTempStatus": eltQosAceTidxTempStatus,
       "eltQosAceTidxTempAction": eltQosAceTidxTempAction,
       "eltQosAceTidxTempType": eltQosAceTidxTempType,
       "eltQosAceTidxTempActionDropType": eltQosAceTidxTempActionDropType,
       "eltQosAceTidxTempAccount": eltQosAceTidxTempAccount,
       "eltQosAceTidxTempTimeRange": eltQosAceTidxTempTimeRange,
       "eltQosAceTidxTempCommitAction": eltQosAceTidxTempCommitAction,
       "eltQosAceTidxTempTuple1": eltQosAceTidxTempTuple1,
       "eltQosAceTidxTempTuple2": eltQosAceTidxTempTuple2,
       "eltQosAceTidxTempTuple3": eltQosAceTidxTempTuple3,
       "eltQosAceTidxTempTuple4": eltQosAceTidxTempTuple4,
       "eltQosAceTidxTempTuple5": eltQosAceTidxTempTuple5,
       "eltQosAceTidxTempTuple6": eltQosAceTidxTempTuple6,
       "eltQosAceTidxTempTuple7": eltQosAceTidxTempTuple7,
       "eltQosAceTidxTempTuple8": eltQosAceTidxTempTuple8,
       "eltQosAceTidxTempTuple9": eltQosAceTidxTempTuple9,
       "eltQosAceTidxTempTuple10": eltQosAceTidxTempTuple10,
       "eltQosAceTidxTempTuple11": eltQosAceTidxTempTuple11,
       "eltQosAceTidxTempTuple12": eltQosAceTidxTempTuple12,
       "eltQosAceTidxTempTuple13": eltQosAceTidxTempTuple13,
       "eltQosAceTidxTempTuple14": eltQosAceTidxTempTuple14,
       "eltQosAceTidxTempTuple15": eltQosAceTidxTempTuple15,
       "eltQosAceTidxTempTuple16": eltQosAceTidxTempTuple16,
       "eltQosAceTidxTempTuple17": eltQosAceTidxTempTuple17,
       "eltQosAceTidxTempTuple18": eltQosAceTidxTempTuple18,
       "eltQosAceTidxTempTuple19": eltQosAceTidxTempTuple19,
       "eltQosAceTidxTempTuple20": eltQosAceTidxTempTuple20,
       "eltQosAceTidxTempTuple21": eltQosAceTidxTempTuple21,
       "eltQosAceTidxTempTuple22": eltQosAceTidxTempTuple22,
       "eltQosAceTidxTempTuple23": eltQosAceTidxTempTuple23,
       "eltQosAceTidxTempTuple24": eltQosAceTidxTempTuple24,
       "eltQosAceTidxTempTuple25": eltQosAceTidxTempTuple25,
       "eltQosAceTidxTempTuple26": eltQosAceTidxTempTuple26,
       "eltQosAceTidxCandidateTable": eltQosAceTidxCandidateTable,
       "eltQosAceTidxCandidateEntry": eltQosAceTidxCandidateEntry,
       "eltQosAceTidxCandidateAclIndex": eltQosAceTidxCandidateAclIndex,
       "eltQosAceTidxCandidateIndex": eltQosAceTidxCandidateIndex,
       "eltQosAceTidxCandidateAction": eltQosAceTidxCandidateAction,
       "eltQosAceTidxCandidateType": eltQosAceTidxCandidateType,
       "eltQosAceTidxCandidateTuple1": eltQosAceTidxCandidateTuple1,
       "eltQosAceTidxCandidateTuple2": eltQosAceTidxCandidateTuple2,
       "eltQosAceTidxCandidateTuple3": eltQosAceTidxCandidateTuple3,
       "eltQosAceTidxCandidateTuple4": eltQosAceTidxCandidateTuple4,
       "eltQosAceTidxCandidateTuple5": eltQosAceTidxCandidateTuple5,
       "eltQosAceTidxCandidateTuple6": eltQosAceTidxCandidateTuple6,
       "eltQosAceTidxCandidateTuple7": eltQosAceTidxCandidateTuple7,
       "eltQosAceTidxCandidateTuple8": eltQosAceTidxCandidateTuple8,
       "eltQosAceTidxCandidateAccount": eltQosAceTidxCandidateAccount,
       "eltQosAceTidxCandidateStatus": eltQosAceTidxCandidateStatus,
       "eltQosAceTidxCandidateTimeRange": eltQosAceTidxCandidateTimeRange,
       "eltQosAceTidxCandidateTimeRangeIsActive": eltQosAceTidxCandidateTimeRangeIsActive,
       "eltQosAceTidxCandidateTuple9": eltQosAceTidxCandidateTuple9,
       "eltQosAceTidxCandidateTuple10": eltQosAceTidxCandidateTuple10,
       "eltQosAceTidxCandidateTuple11": eltQosAceTidxCandidateTuple11,
       "eltQosAceTidxCandidateActionDropType": eltQosAceTidxCandidateActionDropType,
       "eltQosAceTidxCandidateTuple12": eltQosAceTidxCandidateTuple12,
       "eltQosAceTidxCandidateTuple13": eltQosAceTidxCandidateTuple13,
       "eltQosAceTidxCandidateTuple14": eltQosAceTidxCandidateTuple14,
       "eltQosAceTidxCandidateTuple15": eltQosAceTidxCandidateTuple15,
       "eltQosAceTidxCandidateTuple16": eltQosAceTidxCandidateTuple16,
       "eltQosAceTidxCandidateTuple17": eltQosAceTidxCandidateTuple17,
       "eltQosAceTidxCandidateTuple18": eltQosAceTidxCandidateTuple18,
       "eltQosAceTidxCandidateTuple19": eltQosAceTidxCandidateTuple19,
       "eltQosAceTidxCandidateTuple20": eltQosAceTidxCandidateTuple20,
       "eltQosAceTidxCandidateTuple21": eltQosAceTidxCandidateTuple21,
       "eltQosAceTidxCandidateTuple22": eltQosAceTidxCandidateTuple22,
       "eltQosAceTidxCandidateTuple23": eltQosAceTidxCandidateTuple23,
       "eltQosAceTidxCandidateTuple24": eltQosAceTidxCandidateTuple24,
       "eltQosAceTidxCandidateTuple25": eltQosAceTidxCandidateTuple25,
       "eltQosAceTidxCandidateTuple26": eltQosAceTidxCandidateTuple26,
       "eltQosAclCandidateTable": eltQosAclCandidateTable,
       "eltQosAclCandidateEntry": eltQosAclCandidateEntry,
       "eltQosAclCandidateIndex": eltQosAclCandidateIndex,
       "eltQosAclCandidateName": eltQosAclCandidateName,
       "eltQosAclCandidateType": eltQosAclCandidateType,
       "eltQosAclCandidateStatus": eltQosAclCandidateStatus,
       "eltQosAclCandidateNumOfAces": eltQosAclCandidateNumOfAces,
       "eltQosDeleteCandidateAction": eltQosDeleteCandidateAction,
       "eltQosTrafficLimiterMode": eltQosTrafficLimiterMode,
       "eltQosPolicerConfigTable": eltQosPolicerConfigTable,
       "eltQosPolicerConfigEntry": eltQosPolicerConfigEntry,
       "eltQosPolicerConfigCirPps": eltQosPolicerConfigCirPps,
       "eltQosPolicerConfigCbsPakets": eltQosPolicerConfigCbsPakets,
       "eltQosPolicerConfigPpsAction": eltQosPolicerConfigPpsAction,
       "eltQosPolicerConfigPirPps": eltQosPolicerConfigPirPps,
       "eltQosPolicerConfigPbsPakets": eltQosPolicerConfigPbsPakets,
       "eltQosPolicerConfigPpsPeakAction": eltQosPolicerConfigPpsPeakAction}
)
