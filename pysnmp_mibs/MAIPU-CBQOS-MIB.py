# SNMP MIB module (MAIPU-CBQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-CBQOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:06 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

maipuCBQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Unsigned64(TextualConvention, Counter64):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Maipu_ObjectIdentity = ObjectIdentity
maipu = _Maipu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651)
)
_MpMgmt2_ObjectIdentity = ObjectIdentity
mpMgmt2 = _MpMgmt2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6)
)
_MpRouterTech_ObjectIdentity = ObjectIdentity
mpRouterTech = _MpRouterTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2)
)
_MpRtQoSv2_ObjectIdentity = ObjectIdentity
mpRtQoSv2 = _MpRtQoSv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3)
)
_MaipuCBQosMIBObjects_ObjectIdentity = ObjectIdentity
maipuCBQosMIBObjects = _MaipuCBQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1)
)
_MpCbQosServicePolicy_ObjectIdentity = ObjectIdentity
mpCbQosServicePolicy = _MpCbQosServicePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1)
)
_MpCbQosServicePolicyTable_Object = MibTable
mpCbQosServicePolicyTable = _MpCbQosServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpCbQosServicePolicyTable.setStatus("current")
_MpCbQosServicePolicyEntry_Object = MibTableRow
mpCbQosServicePolicyEntry = _MpCbQosServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1)
)
mpCbQosServicePolicyEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosServicePolicyEntry.setStatus("current")
_MpCbQosPolicyIndex_Type = Unsigned32
_MpCbQosPolicyIndex_Object = MibTableColumn
mpCbQosPolicyIndex = _MpCbQosPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1, 1),
    _MpCbQosPolicyIndex_Type()
)
mpCbQosPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCbQosPolicyIndex.setStatus("current")


class _MpCbQosIfType_Type(Integer32):
    """Custom type mpCbQosIfType based on Integer32"""
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
        *(("mainInterface", 1),
          ("subInterface", 2),
          ("frDLCI", 3),
          ("atmPVC", 4),
          ("controlPlane", 5),
          ("vlanPort", 6))
    )


_MpCbQosIfType_Type.__name__ = "Integer32"
_MpCbQosIfType_Object = MibTableColumn
mpCbQosIfType = _MpCbQosIfType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1, 2),
    _MpCbQosIfType_Type()
)
mpCbQosIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosIfType.setStatus("current")


class _MpCbQosPolicyDirection_Type(Integer32):
    """Custom type mpCbQosPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_MpCbQosPolicyDirection_Type.__name__ = "Integer32"
_MpCbQosPolicyDirection_Object = MibTableColumn
mpCbQosPolicyDirection = _MpCbQosPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1, 3),
    _MpCbQosPolicyDirection_Type()
)
mpCbQosPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPolicyDirection.setStatus("current")
_MpCbQosIfIndex_Type = Integer32
_MpCbQosIfIndex_Object = MibTableColumn
mpCbQosIfIndex = _MpCbQosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1, 4),
    _MpCbQosIfIndex_Type()
)
mpCbQosIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosIfIndex.setStatus("current")


class _MpCbQosFrDLCI_Type(Unsigned32):
    """Custom type mpCbQosFrDLCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_MpCbQosFrDLCI_Type.__name__ = "Unsigned32"
_MpCbQosFrDLCI_Object = MibTableColumn
mpCbQosFrDLCI = _MpCbQosFrDLCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1, 5),
    _MpCbQosFrDLCI_Type()
)
mpCbQosFrDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosFrDLCI.setStatus("current")


class _MpCbQosAtmVPI_Type(Unsigned32):
    """Custom type mpCbQosAtmVPI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MpCbQosAtmVPI_Type.__name__ = "Unsigned32"
_MpCbQosAtmVPI_Object = MibTableColumn
mpCbQosAtmVPI = _MpCbQosAtmVPI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1, 6),
    _MpCbQosAtmVPI_Type()
)
mpCbQosAtmVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosAtmVPI.setStatus("current")


class _MpCbQosAtmVCI_Type(Unsigned32):
    """Custom type mpCbQosAtmVCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpCbQosAtmVCI_Type.__name__ = "Unsigned32"
_MpCbQosAtmVCI_Object = MibTableColumn
mpCbQosAtmVCI = _MpCbQosAtmVCI_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1, 7),
    _MpCbQosAtmVCI_Type()
)
mpCbQosAtmVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosAtmVCI.setStatus("current")
_MpCbQosEntityIndex_Type = Integer32
_MpCbQosEntityIndex_Object = MibTableColumn
mpCbQosEntityIndex = _MpCbQosEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1, 8),
    _MpCbQosEntityIndex_Type()
)
mpCbQosEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosEntityIndex.setStatus("current")


class _MpCbQosVlanIndex_Type(Unsigned32):
    """Custom type mpCbQosVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MpCbQosVlanIndex_Type.__name__ = "Unsigned32"
_MpCbQosVlanIndex_Object = MibTableColumn
mpCbQosVlanIndex = _MpCbQosVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 1, 1, 1, 9),
    _MpCbQosVlanIndex_Type()
)
mpCbQosVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosVlanIndex.setStatus("current")
_MpCbQosInterfacePolicy_ObjectIdentity = ObjectIdentity
mpCbQosInterfacePolicy = _MpCbQosInterfacePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 2)
)
_MpCbQosInterfacePolicyTable_Object = MibTable
mpCbQosInterfacePolicyTable = _MpCbQosInterfacePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpCbQosInterfacePolicyTable.setStatus("current")
_MpCbQosInterfacePolicyEntry_Object = MibTableRow
mpCbQosInterfacePolicyEntry = _MpCbQosInterfacePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 2, 1, 1)
)
mpCbQosInterfacePolicyEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "ifIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyDirection"),
)
if mibBuilder.loadTexts:
    mpCbQosInterfacePolicyEntry.setStatus("current")
_MpCbQosIFPolicyIndex_Type = Unsigned32
_MpCbQosIFPolicyIndex_Object = MibTableColumn
mpCbQosIFPolicyIndex = _MpCbQosIFPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 2, 1, 1, 1),
    _MpCbQosIFPolicyIndex_Type()
)
mpCbQosIFPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosIFPolicyIndex.setStatus("current")
_MpCbQosFrameRelayVCPolicy_ObjectIdentity = ObjectIdentity
mpCbQosFrameRelayVCPolicy = _MpCbQosFrameRelayVCPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 3)
)
_MpCbQosFrameRelayPolicyTable_Object = MibTable
mpCbQosFrameRelayPolicyTable = _MpCbQosFrameRelayPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mpCbQosFrameRelayPolicyTable.setStatus("current")
_MpCbQosFrameRelayPolicyEntry_Object = MibTableRow
mpCbQosFrameRelayPolicyEntry = _MpCbQosFrameRelayPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 3, 1, 1)
)
mpCbQosFrameRelayPolicyEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "ifIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosFrDLCI"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyDirection"),
)
if mibBuilder.loadTexts:
    mpCbQosFrameRelayPolicyEntry.setStatus("current")
_MpCbQosFRPolicyIndex_Type = Unsigned32
_MpCbQosFRPolicyIndex_Object = MibTableColumn
mpCbQosFRPolicyIndex = _MpCbQosFRPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 3, 1, 1, 1),
    _MpCbQosFRPolicyIndex_Type()
)
mpCbQosFRPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosFRPolicyIndex.setStatus("current")
_MpCbQosATMPVCPolicy_ObjectIdentity = ObjectIdentity
mpCbQosATMPVCPolicy = _MpCbQosATMPVCPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 4)
)
_MpCbQosATMPVCPolicyTable_Object = MibTable
mpCbQosATMPVCPolicyTable = _MpCbQosATMPVCPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mpCbQosATMPVCPolicyTable.setStatus("current")
_MpCbQosATMPVCPolicyEntry_Object = MibTableRow
mpCbQosATMPVCPolicyEntry = _MpCbQosATMPVCPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 4, 1, 1)
)
mpCbQosATMPVCPolicyEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "ifIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosAtmVPI"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosAtmVCI"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyDirection"),
)
if mibBuilder.loadTexts:
    mpCbQosATMPVCPolicyEntry.setStatus("current")
_MpCbQosATMPVCPolicyIndex_Type = Unsigned32
_MpCbQosATMPVCPolicyIndex_Object = MibTableColumn
mpCbQosATMPVCPolicyIndex = _MpCbQosATMPVCPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 4, 1, 1, 1),
    _MpCbQosATMPVCPolicyIndex_Type()
)
mpCbQosATMPVCPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosATMPVCPolicyIndex.setStatus("current")
_MpCbQosObjects_ObjectIdentity = ObjectIdentity
mpCbQosObjects = _MpCbQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 5)
)
_MpCbQosObjectsTable_Object = MibTable
mpCbQosObjectsTable = _MpCbQosObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    mpCbQosObjectsTable.setStatus("current")
_MpCbQosObjectsEntry_Object = MibTableRow
mpCbQosObjectsEntry = _MpCbQosObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 5, 1, 1)
)
mpCbQosObjectsEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosObjectsEntry.setStatus("current")
_MpCbQosObjectsIndex_Type = Unsigned32
_MpCbQosObjectsIndex_Object = MibTableColumn
mpCbQosObjectsIndex = _MpCbQosObjectsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 5, 1, 1, 1),
    _MpCbQosObjectsIndex_Type()
)
mpCbQosObjectsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCbQosObjectsIndex.setStatus("current")
_MpCbQosConfigIndex_Type = Unsigned32
_MpCbQosConfigIndex_Object = MibTableColumn
mpCbQosConfigIndex = _MpCbQosConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 5, 1, 1, 2),
    _MpCbQosConfigIndex_Type()
)
mpCbQosConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosConfigIndex.setStatus("current")


class _MpCbQosObjectsType_Type(Integer32):
    """Custom type mpCbQosObjectsType based on Integer32"""
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
        *(("policymap", 1),
          ("classmap", 2),
          ("matchStatement", 3),
          ("queueing", 4),
          ("randomDetect", 5),
          ("trafficShaping", 6),
          ("police", 7),
          ("set", 8))
    )


_MpCbQosObjectsType_Type.__name__ = "Integer32"
_MpCbQosObjectsType_Object = MibTableColumn
mpCbQosObjectsType = _MpCbQosObjectsType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 5, 1, 1, 3),
    _MpCbQosObjectsType_Type()
)
mpCbQosObjectsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosObjectsType.setStatus("current")
_MpCbQosParentObjectsIndex_Type = Unsigned32
_MpCbQosParentObjectsIndex_Object = MibTableColumn
mpCbQosParentObjectsIndex = _MpCbQosParentObjectsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 5, 1, 1, 4),
    _MpCbQosParentObjectsIndex_Type()
)
mpCbQosParentObjectsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosParentObjectsIndex.setStatus("current")
_MpCbQosPolicyMapCfg_ObjectIdentity = ObjectIdentity
mpCbQosPolicyMapCfg = _MpCbQosPolicyMapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 6)
)
_MpCbQosPolicyMapCfgTable_Object = MibTable
mpCbQosPolicyMapCfgTable = _MpCbQosPolicyMapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    mpCbQosPolicyMapCfgTable.setStatus("current")
_MpCbQosPolicyMapCfgEntry_Object = MibTableRow
mpCbQosPolicyMapCfgEntry = _MpCbQosPolicyMapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 6, 1, 1)
)
mpCbQosPolicyMapCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosPolicyMapCfgEntry.setStatus("current")


class _MpCbQosPolicyMapName_Type(DisplayString):
    """Custom type mpCbQosPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpCbQosPolicyMapName_Type.__name__ = "DisplayString"
_MpCbQosPolicyMapName_Object = MibTableColumn
mpCbQosPolicyMapName = _MpCbQosPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 6, 1, 1, 1),
    _MpCbQosPolicyMapName_Type()
)
mpCbQosPolicyMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPolicyMapName.setStatus("current")


class _MpCbQosPolicyMapDesc_Type(DisplayString):
    """Custom type mpCbQosPolicyMapDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpCbQosPolicyMapDesc_Type.__name__ = "DisplayString"
_MpCbQosPolicyMapDesc_Object = MibTableColumn
mpCbQosPolicyMapDesc = _MpCbQosPolicyMapDesc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 6, 1, 1, 2),
    _MpCbQosPolicyMapDesc_Type()
)
mpCbQosPolicyMapDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPolicyMapDesc.setStatus("current")
_MpCbQosClassMapCfg_ObjectIdentity = ObjectIdentity
mpCbQosClassMapCfg = _MpCbQosClassMapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 7)
)
_MpCbQosCMCfgTable_Object = MibTable
mpCbQosCMCfgTable = _MpCbQosCMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    mpCbQosCMCfgTable.setStatus("current")
_MpCbQosCMCfgEntry_Object = MibTableRow
mpCbQosCMCfgEntry = _MpCbQosCMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 7, 1, 1)
)
mpCbQosCMCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosCMCfgEntry.setStatus("current")


class _MpCbQosCMName_Type(DisplayString):
    """Custom type mpCbQosCMName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpCbQosCMName_Type.__name__ = "DisplayString"
_MpCbQosCMName_Object = MibTableColumn
mpCbQosCMName = _MpCbQosCMName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 7, 1, 1, 1),
    _MpCbQosCMName_Type()
)
mpCbQosCMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMName.setStatus("current")


class _MpCbQosCMDesc_Type(DisplayString):
    """Custom type mpCbQosCMDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpCbQosCMDesc_Type.__name__ = "DisplayString"
_MpCbQosCMDesc_Object = MibTableColumn
mpCbQosCMDesc = _MpCbQosCMDesc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 7, 1, 1, 2),
    _MpCbQosCMDesc_Type()
)
mpCbQosCMDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMDesc.setStatus("current")


class _MpCbQosCMInfo_Type(Integer32):
    """Custom type mpCbQosCMInfo based on Integer32"""
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
          ("matchAll", 2),
          ("matchAny", 3))
    )


_MpCbQosCMInfo_Type.__name__ = "Integer32"
_MpCbQosCMInfo_Object = MibTableColumn
mpCbQosCMInfo = _MpCbQosCMInfo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 7, 1, 1, 3),
    _MpCbQosCMInfo_Type()
)
mpCbQosCMInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMInfo.setStatus("current")
_MpCbQosMatchStmtCfg_ObjectIdentity = ObjectIdentity
mpCbQosMatchStmtCfg = _MpCbQosMatchStmtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 8)
)
_MpCbQosMatchStmtCfgTable_Object = MibTable
mpCbQosMatchStmtCfgTable = _MpCbQosMatchStmtCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mpCbQosMatchStmtCfgTable.setStatus("current")
_MpCbQosMatchStmtCfgEntry_Object = MibTableRow
mpCbQosMatchStmtCfgEntry = _MpCbQosMatchStmtCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 8, 1, 1)
)
mpCbQosMatchStmtCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosMatchStmtCfgEntry.setStatus("current")


class _MpCbQosMatchStmtName_Type(DisplayString):
    """Custom type mpCbQosMatchStmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpCbQosMatchStmtName_Type.__name__ = "DisplayString"
_MpCbQosMatchStmtName_Object = MibTableColumn
mpCbQosMatchStmtName = _MpCbQosMatchStmtName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 8, 1, 1, 1),
    _MpCbQosMatchStmtName_Type()
)
mpCbQosMatchStmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosMatchStmtName.setStatus("current")


class _MpCbQosMatchStmtInfo_Type(Integer32):
    """Custom type mpCbQosMatchStmtInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("matchNot", 2))
    )


_MpCbQosMatchStmtInfo_Type.__name__ = "Integer32"
_MpCbQosMatchStmtInfo_Object = MibTableColumn
mpCbQosMatchStmtInfo = _MpCbQosMatchStmtInfo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 8, 1, 1, 2),
    _MpCbQosMatchStmtInfo_Type()
)
mpCbQosMatchStmtInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosMatchStmtInfo.setStatus("current")
_MpCbQosQueueingCfg_ObjectIdentity = ObjectIdentity
mpCbQosQueueingCfg = _MpCbQosQueueingCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9)
)
_MpCbQosQueueingCfgTable_Object = MibTable
mpCbQosQueueingCfgTable = _MpCbQosQueueingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgTable.setStatus("current")
_MpCbQosQueueingCfgEntry_Object = MibTableRow
mpCbQosQueueingCfgEntry = _MpCbQosQueueingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1)
)
mpCbQosQueueingCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgEntry.setStatus("current")
_MpCbQosQueueingCfgBandwidth_Type = Unsigned32
_MpCbQosQueueingCfgBandwidth_Object = MibTableColumn
mpCbQosQueueingCfgBandwidth = _MpCbQosQueueingCfgBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 1),
    _MpCbQosQueueingCfgBandwidth_Type()
)
mpCbQosQueueingCfgBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgBandwidth.setStatus("current")


class _MpCbQosQueueingCfgBandwidthUnits_Type(Integer32):
    """Custom type mpCbQosQueueingCfgBandwidthUnits based on Integer32"""
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
        *(("kbps", 1),
          ("percentage", 2),
          ("percentageRemaining", 3),
          ("ratioRemaining", 4))
    )


_MpCbQosQueueingCfgBandwidthUnits_Type.__name__ = "Integer32"
_MpCbQosQueueingCfgBandwidthUnits_Object = MibTableColumn
mpCbQosQueueingCfgBandwidthUnits = _MpCbQosQueueingCfgBandwidthUnits_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 2),
    _MpCbQosQueueingCfgBandwidthUnits_Type()
)
mpCbQosQueueingCfgBandwidthUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgBandwidthUnits.setStatus("current")
_MpCbQosQueueingCfgFlowEnabled_Type = TruthValue
_MpCbQosQueueingCfgFlowEnabled_Object = MibTableColumn
mpCbQosQueueingCfgFlowEnabled = _MpCbQosQueueingCfgFlowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 3),
    _MpCbQosQueueingCfgFlowEnabled_Type()
)
mpCbQosQueueingCfgFlowEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgFlowEnabled.setStatus("current")
_MpCbQosQueueingCfgPriorityEnabled_Type = TruthValue
_MpCbQosQueueingCfgPriorityEnabled_Object = MibTableColumn
mpCbQosQueueingCfgPriorityEnabled = _MpCbQosQueueingCfgPriorityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 4),
    _MpCbQosQueueingCfgPriorityEnabled_Type()
)
mpCbQosQueueingCfgPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgPriorityEnabled.setStatus("current")


class _MpCbQosQueueingCfgDynamicQNumber_Type(Integer32):
    """Custom type mpCbQosQueueingCfgDynamicQNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_MpCbQosQueueingCfgDynamicQNumber_Type.__name__ = "Integer32"
_MpCbQosQueueingCfgDynamicQNumber_Object = MibTableColumn
mpCbQosQueueingCfgDynamicQNumber = _MpCbQosQueueingCfgDynamicQNumber_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 5),
    _MpCbQosQueueingCfgDynamicQNumber_Type()
)
mpCbQosQueueingCfgDynamicQNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgDynamicQNumber.setStatus("current")
_MpCbQosQueueingCfgPrioBurstSize_Type = Unsigned32
_MpCbQosQueueingCfgPrioBurstSize_Object = MibTableColumn
mpCbQosQueueingCfgPrioBurstSize = _MpCbQosQueueingCfgPrioBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 6),
    _MpCbQosQueueingCfgPrioBurstSize_Type()
)
mpCbQosQueueingCfgPrioBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgPrioBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgPrioBurstSize.setUnits("Bytes")


class _MpCbQosQueueingCfgQLimitUnits_Type(Integer32):
    """Custom type mpCbQosQueueingCfgQLimitUnits based on Integer32"""
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
        *(("packets", 1),
          ("bytes", 2),
          ("cells", 3),
          ("ms", 4),
          ("us", 5))
    )


_MpCbQosQueueingCfgQLimitUnits_Type.__name__ = "Integer32"
_MpCbQosQueueingCfgQLimitUnits_Object = MibTableColumn
mpCbQosQueueingCfgQLimitUnits = _MpCbQosQueueingCfgQLimitUnits_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 7),
    _MpCbQosQueueingCfgQLimitUnits_Type()
)
mpCbQosQueueingCfgQLimitUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgQLimitUnits.setStatus("current")
_MpCbQosQueueingCfgAggregateQLimit_Type = Unsigned32
_MpCbQosQueueingCfgAggregateQLimit_Object = MibTableColumn
mpCbQosQueueingCfgAggregateQLimit = _MpCbQosQueueingCfgAggregateQLimit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 8),
    _MpCbQosQueueingCfgAggregateQLimit_Type()
)
mpCbQosQueueingCfgAggregateQLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgAggregateQLimit.setStatus("current")
_MpCbQosQueueingCfgAggrQLimitTime_Type = Unsigned32
_MpCbQosQueueingCfgAggrQLimitTime_Object = MibTableColumn
mpCbQosQueueingCfgAggrQLimitTime = _MpCbQosQueueingCfgAggrQLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 9),
    _MpCbQosQueueingCfgAggrQLimitTime_Type()
)
mpCbQosQueueingCfgAggrQLimitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgAggrQLimitTime.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgAggrQLimitTime.setUnits("milli-seconds")
_MpCbQosQueueingCfgIndividualQLimit_Type = Unsigned32
_MpCbQosQueueingCfgIndividualQLimit_Object = MibTableColumn
mpCbQosQueueingCfgIndividualQLimit = _MpCbQosQueueingCfgIndividualQLimit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 9, 1, 1, 10),
    _MpCbQosQueueingCfgIndividualQLimit_Type()
)
mpCbQosQueueingCfgIndividualQLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCfgIndividualQLimit.setStatus("current")
_MpCbQosREDCfg_ObjectIdentity = ObjectIdentity
mpCbQosREDCfg = _MpCbQosREDCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 10)
)
_MpCbQosREDCfgTable_Object = MibTable
mpCbQosREDCfgTable = _MpCbQosREDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    mpCbQosREDCfgTable.setStatus("current")
_MpCbQosREDCfgEntry_Object = MibTableRow
mpCbQosREDCfgEntry = _MpCbQosREDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 10, 1, 1)
)
mpCbQosREDCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosREDCfgEntry.setStatus("current")


class _MpCbQosREDCfgExponWeight_Type(Integer32):
    """Custom type mpCbQosREDCfgExponWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MpCbQosREDCfgExponWeight_Type.__name__ = "Integer32"
_MpCbQosREDCfgExponWeight_Object = MibTableColumn
mpCbQosREDCfgExponWeight = _MpCbQosREDCfgExponWeight_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 10, 1, 1, 1),
    _MpCbQosREDCfgExponWeight_Type()
)
mpCbQosREDCfgExponWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDCfgExponWeight.setStatus("current")


class _MpCbQosREDCfgDscpPrec_Type(Integer32):
    """Custom type mpCbQosREDCfgDscpPrec based on Integer32"""
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
        *(("precedence", 1),
          ("dscp", 2),
          ("discardClass", 3),
          ("l2Cos", 4),
          ("atmClp", 5),
          ("mplsExp", 6),
          ("redDefault", 7),
          ("redUserDefault", 8))
    )


_MpCbQosREDCfgDscpPrec_Type.__name__ = "Integer32"
_MpCbQosREDCfgDscpPrec_Object = MibTableColumn
mpCbQosREDCfgDscpPrec = _MpCbQosREDCfgDscpPrec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 10, 1, 1, 2),
    _MpCbQosREDCfgDscpPrec_Type()
)
mpCbQosREDCfgDscpPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDCfgDscpPrec.setStatus("current")
_MpCbQosREDCfgECNEnabled_Type = TruthValue
_MpCbQosREDCfgECNEnabled_Object = MibTableColumn
mpCbQosREDCfgECNEnabled = _MpCbQosREDCfgECNEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 10, 1, 1, 3),
    _MpCbQosREDCfgECNEnabled_Type()
)
mpCbQosREDCfgECNEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDCfgECNEnabled.setStatus("current")
_MpCbQosREDClassCfg_ObjectIdentity = ObjectIdentity
mpCbQosREDClassCfg = _MpCbQosREDClassCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11)
)
_MpCbQosREDClassCfgTable_Object = MibTable
mpCbQosREDClassCfgTable = _MpCbQosREDClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1)
)
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgTable.setStatus("current")
_MpCbQosREDClassCfgEntry_Object = MibTableRow
mpCbQosREDClassCfgEntry = _MpCbQosREDClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1, 1)
)
mpCbQosREDClassCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosREDValue"),
)
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgEntry.setStatus("current")


class _MpCbQosREDValue_Type(Integer32):
    """Custom type mpCbQosREDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpCbQosREDValue_Type.__name__ = "Integer32"
_MpCbQosREDValue_Object = MibTableColumn
mpCbQosREDValue = _MpCbQosREDValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1, 1, 1),
    _MpCbQosREDValue_Type()
)
mpCbQosREDValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCbQosREDValue.setStatus("current")


class _MpCbQosREDCfgPktDropProb_Type(Integer32):
    """Custom type mpCbQosREDCfgPktDropProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MpCbQosREDCfgPktDropProb_Type.__name__ = "Integer32"
_MpCbQosREDCfgPktDropProb_Object = MibTableColumn
mpCbQosREDCfgPktDropProb = _MpCbQosREDCfgPktDropProb_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1, 1, 2),
    _MpCbQosREDCfgPktDropProb_Type()
)
mpCbQosREDCfgPktDropProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDCfgPktDropProb.setStatus("current")


class _MpCbQosREDClassCfgMinThresholdUnit_Type(Integer32):
    """Custom type mpCbQosREDClassCfgMinThresholdUnit based on Integer32"""
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
        *(("packets", 1),
          ("bytes", 2),
          ("cells", 3),
          ("ms", 4),
          ("us", 5))
    )


_MpCbQosREDClassCfgMinThresholdUnit_Type.__name__ = "Integer32"
_MpCbQosREDClassCfgMinThresholdUnit_Object = MibTableColumn
mpCbQosREDClassCfgMinThresholdUnit = _MpCbQosREDClassCfgMinThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1, 1, 3),
    _MpCbQosREDClassCfgMinThresholdUnit_Type()
)
mpCbQosREDClassCfgMinThresholdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgMinThresholdUnit.setStatus("current")


class _MpCbQosREDClassCfgMaxThresholdUnit_Type(Integer32):
    """Custom type mpCbQosREDClassCfgMaxThresholdUnit based on Integer32"""
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
        *(("packets", 1),
          ("bytes", 2),
          ("cells", 3),
          ("ms", 4),
          ("us", 5))
    )


_MpCbQosREDClassCfgMaxThresholdUnit_Type.__name__ = "Integer32"
_MpCbQosREDClassCfgMaxThresholdUnit_Object = MibTableColumn
mpCbQosREDClassCfgMaxThresholdUnit = _MpCbQosREDClassCfgMaxThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1, 1, 4),
    _MpCbQosREDClassCfgMaxThresholdUnit_Type()
)
mpCbQosREDClassCfgMaxThresholdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgMaxThresholdUnit.setStatus("current")
_MpCbQosREDClassCfgMinThreshold_Type = Unsigned32
_MpCbQosREDClassCfgMinThreshold_Object = MibTableColumn
mpCbQosREDClassCfgMinThreshold = _MpCbQosREDClassCfgMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1, 1, 5),
    _MpCbQosREDClassCfgMinThreshold_Type()
)
mpCbQosREDClassCfgMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgMinThreshold.setStatus("current")
_MpCbQosREDClassCfgMaxThreshold_Type = Unsigned32
_MpCbQosREDClassCfgMaxThreshold_Object = MibTableColumn
mpCbQosREDClassCfgMaxThreshold = _MpCbQosREDClassCfgMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1, 1, 6),
    _MpCbQosREDClassCfgMaxThreshold_Type()
)
mpCbQosREDClassCfgMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgMaxThreshold.setStatus("current")
_MpCbQosREDClassCfgMinThresholdTime_Type = Unsigned32
_MpCbQosREDClassCfgMinThresholdTime_Object = MibTableColumn
mpCbQosREDClassCfgMinThresholdTime = _MpCbQosREDClassCfgMinThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1, 1, 7),
    _MpCbQosREDClassCfgMinThresholdTime_Type()
)
mpCbQosREDClassCfgMinThresholdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgMinThresholdTime.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgMinThresholdTime.setUnits("milli-seconds")
_MpCbQosREDClassCfgMaxThresholdTime_Type = Unsigned32
_MpCbQosREDClassCfgMaxThresholdTime_Object = MibTableColumn
mpCbQosREDClassCfgMaxThresholdTime = _MpCbQosREDClassCfgMaxThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 11, 1, 1, 8),
    _MpCbQosREDClassCfgMaxThresholdTime_Type()
)
mpCbQosREDClassCfgMaxThresholdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgMaxThresholdTime.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDClassCfgMaxThresholdTime.setUnits("milli-seconds")
_MpCbQosPoliceCfg_ObjectIdentity = ObjectIdentity
mpCbQosPoliceCfg = _MpCbQosPoliceCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12)
)
_MpCbQosPoliceCfgTable_Object = MibTable
mpCbQosPoliceCfgTable = _MpCbQosPoliceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1)
)
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgTable.setStatus("current")
_MpCbQosPoliceCfgEntry_Object = MibTableRow
mpCbQosPoliceCfgEntry = _MpCbQosPoliceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1)
)
mpCbQosPoliceCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgEntry.setStatus("current")
_MpCbQosPoliceCfgRate64_Type = Unsigned64
_MpCbQosPoliceCfgRate64_Object = MibTableColumn
mpCbQosPoliceCfgRate64 = _MpCbQosPoliceCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 1),
    _MpCbQosPoliceCfgRate64_Type()
)
mpCbQosPoliceCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgRate64.setUnits("bits/second")
_MpCbQosPoliceCfgBurstSize_Type = Unsigned32
_MpCbQosPoliceCfgBurstSize_Object = MibTableColumn
mpCbQosPoliceCfgBurstSize = _MpCbQosPoliceCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 2),
    _MpCbQosPoliceCfgBurstSize_Type()
)
mpCbQosPoliceCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgBurstSize.setUnits("Octets")
_MpCbQosPoliceCfgExtBurstSize_Type = Unsigned32
_MpCbQosPoliceCfgExtBurstSize_Object = MibTableColumn
mpCbQosPoliceCfgExtBurstSize = _MpCbQosPoliceCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 3),
    _MpCbQosPoliceCfgExtBurstSize_Type()
)
mpCbQosPoliceCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgExtBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgExtBurstSize.setUnits("Octets")
_MpCbQosPoliceCfgPir64_Type = Unsigned64
_MpCbQosPoliceCfgPir64_Object = MibTableColumn
mpCbQosPoliceCfgPir64 = _MpCbQosPoliceCfgPir64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 4),
    _MpCbQosPoliceCfgPir64_Type()
)
mpCbQosPoliceCfgPir64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgPir64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgPir64.setUnits("bits/second")


class _MpCbQosPoliceCfgRateType_Type(Integer32):
    """Custom type mpCbQosPoliceCfgRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bps", 1),
          ("percentage", 2),
          ("cps", 3))
    )


_MpCbQosPoliceCfgRateType_Type.__name__ = "Integer32"
_MpCbQosPoliceCfgRateType_Object = MibTableColumn
mpCbQosPoliceCfgRateType = _MpCbQosPoliceCfgRateType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 5),
    _MpCbQosPoliceCfgRateType_Type()
)
mpCbQosPoliceCfgRateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgRateType.setStatus("current")


class _MpCbQosPoliceCfgPercentRateValue_Type(Unsigned32):
    """Custom type mpCbQosPoliceCfgPercentRateValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpCbQosPoliceCfgPercentRateValue_Type.__name__ = "Unsigned32"
_MpCbQosPoliceCfgPercentRateValue_Object = MibTableColumn
mpCbQosPoliceCfgPercentRateValue = _MpCbQosPoliceCfgPercentRateValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 6),
    _MpCbQosPoliceCfgPercentRateValue_Type()
)
mpCbQosPoliceCfgPercentRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgPercentRateValue.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgPercentRateValue.setUnits("% of Interface Bandwidth")


class _MpCbQosPoliceCfgPercentPirValue_Type(Unsigned32):
    """Custom type mpCbQosPoliceCfgPercentPirValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpCbQosPoliceCfgPercentPirValue_Type.__name__ = "Unsigned32"
_MpCbQosPoliceCfgPercentPirValue_Object = MibTableColumn
mpCbQosPoliceCfgPercentPirValue = _MpCbQosPoliceCfgPercentPirValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 7),
    _MpCbQosPoliceCfgPercentPirValue_Type()
)
mpCbQosPoliceCfgPercentPirValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgPercentPirValue.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgPercentPirValue.setUnits("% of Interface Bandwidth")
_MpCbQosPoliceCfgCellRate_Type = Unsigned32
_MpCbQosPoliceCfgCellRate_Object = MibTableColumn
mpCbQosPoliceCfgCellRate = _MpCbQosPoliceCfgCellRate_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 8),
    _MpCbQosPoliceCfgCellRate_Type()
)
mpCbQosPoliceCfgCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgCellRate.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgCellRate.setUnits("cells/second")
_MpCbQosPoliceCfgCellPir_Type = Unsigned32
_MpCbQosPoliceCfgCellPir_Object = MibTableColumn
mpCbQosPoliceCfgCellPir = _MpCbQosPoliceCfgCellPir_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 9),
    _MpCbQosPoliceCfgCellPir_Type()
)
mpCbQosPoliceCfgCellPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgCellPir.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgCellPir.setUnits("cells/second")
_MpCbQosPoliceCfgBurstCell_Type = Unsigned32
_MpCbQosPoliceCfgBurstCell_Object = MibTableColumn
mpCbQosPoliceCfgBurstCell = _MpCbQosPoliceCfgBurstCell_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 10),
    _MpCbQosPoliceCfgBurstCell_Type()
)
mpCbQosPoliceCfgBurstCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgBurstCell.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgBurstCell.setUnits("Cells")
_MpCbQosPoliceCfgExtBurstCell_Type = Unsigned32
_MpCbQosPoliceCfgExtBurstCell_Object = MibTableColumn
mpCbQosPoliceCfgExtBurstCell = _MpCbQosPoliceCfgExtBurstCell_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 11),
    _MpCbQosPoliceCfgExtBurstCell_Type()
)
mpCbQosPoliceCfgExtBurstCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgExtBurstCell.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgExtBurstCell.setUnits("Cells")
_MpCbQosPoliceCfgBurstTime_Type = Unsigned32
_MpCbQosPoliceCfgBurstTime_Object = MibTableColumn
mpCbQosPoliceCfgBurstTime = _MpCbQosPoliceCfgBurstTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 12),
    _MpCbQosPoliceCfgBurstTime_Type()
)
mpCbQosPoliceCfgBurstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgBurstTime.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgBurstTime.setUnits("milli-seconds")
_MpCbQosPoliceCfgExtBurstTime_Type = Unsigned32
_MpCbQosPoliceCfgExtBurstTime_Object = MibTableColumn
mpCbQosPoliceCfgExtBurstTime = _MpCbQosPoliceCfgExtBurstTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 12, 1, 1, 13),
    _MpCbQosPoliceCfgExtBurstTime_Type()
)
mpCbQosPoliceCfgExtBurstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgExtBurstTime.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceCfgExtBurstTime.setUnits("milli-seconds")
_MpCbQosPoliceActionCfg_ObjectIdentity = ObjectIdentity
mpCbQosPoliceActionCfg = _MpCbQosPoliceActionCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13)
)
_MpCbQosPoliceActionCfgTable_Object = MibTable
mpCbQosPoliceActionCfgTable = _MpCbQosPoliceActionCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13, 1)
)
if mibBuilder.loadTexts:
    mpCbQosPoliceActionCfgTable.setStatus("current")
_MpCbQosPoliceActionCfgEntry_Object = MibTableRow
mpCbQosPoliceActionCfgEntry = _MpCbQosPoliceActionCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13, 1, 1)
)
mpCbQosPoliceActionCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPoliceActionCfgIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosPoliceActionCfgEntry.setStatus("current")
_MpCbQosPoliceActionCfgIndex_Type = Unsigned32
_MpCbQosPoliceActionCfgIndex_Object = MibTableColumn
mpCbQosPoliceActionCfgIndex = _MpCbQosPoliceActionCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13, 1, 1, 1),
    _MpCbQosPoliceActionCfgIndex_Type()
)
mpCbQosPoliceActionCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpCbQosPoliceActionCfgIndex.setStatus("current")


class _MpCbQosPoliceActionCfgConform_Type(Integer32):
    """Custom type mpCbQosPoliceActionCfgConform based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("transmit", 1),
          ("setIpDSCP", 2),
          ("setIpPrecedence", 3),
          ("setQosGroup", 4),
          ("drop", 5),
          ("setMplsExp", 6),
          ("setAtmClp", 7),
          ("setFrDe", 8),
          ("setL2Cos", 9),
          ("setDiscardClass", 10),
          ("setMplsExpTopMost", 11),
          ("setIpDscpTunnel", 12),
          ("setIpPrecedenceTunnel", 13),
          ("setL2CosInner", 14))
    )


_MpCbQosPoliceActionCfgConform_Type.__name__ = "Integer32"
_MpCbQosPoliceActionCfgConform_Object = MibTableColumn
mpCbQosPoliceActionCfgConform = _MpCbQosPoliceActionCfgConform_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13, 1, 1, 2),
    _MpCbQosPoliceActionCfgConform_Type()
)
mpCbQosPoliceActionCfgConform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceActionCfgConform.setStatus("current")
_MpCbQosPoliceActionCfgConformSetValue_Type = Unsigned32
_MpCbQosPoliceActionCfgConformSetValue_Object = MibTableColumn
mpCbQosPoliceActionCfgConformSetValue = _MpCbQosPoliceActionCfgConformSetValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13, 1, 1, 3),
    _MpCbQosPoliceActionCfgConformSetValue_Type()
)
mpCbQosPoliceActionCfgConformSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceActionCfgConformSetValue.setStatus("current")


class _MpCbQosPoliceActionCfgExceed_Type(Integer32):
    """Custom type mpCbQosPoliceActionCfgExceed based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("transmit", 1),
          ("setIpDSCP", 2),
          ("setIpPrecedence", 3),
          ("setQosGroup", 4),
          ("drop", 5),
          ("setMplsExp", 6),
          ("setAtmClp", 7),
          ("setFrDe", 8),
          ("setL2Cos", 9),
          ("setDiscardClass", 10),
          ("setMplsExpTopMost", 11),
          ("setIpDscpTunnel", 12),
          ("setIpPrecedenceTunnel", 13),
          ("setL2CosInner", 14))
    )


_MpCbQosPoliceActionCfgExceed_Type.__name__ = "Integer32"
_MpCbQosPoliceActionCfgExceed_Object = MibTableColumn
mpCbQosPoliceActionCfgExceed = _MpCbQosPoliceActionCfgExceed_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13, 1, 1, 4),
    _MpCbQosPoliceActionCfgExceed_Type()
)
mpCbQosPoliceActionCfgExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceActionCfgExceed.setStatus("current")
_MpCbQosPoliceActionCfgExceedSetValue_Type = Unsigned32
_MpCbQosPoliceActionCfgExceedSetValue_Object = MibTableColumn
mpCbQosPoliceActionCfgExceedSetValue = _MpCbQosPoliceActionCfgExceedSetValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13, 1, 1, 5),
    _MpCbQosPoliceActionCfgExceedSetValue_Type()
)
mpCbQosPoliceActionCfgExceedSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceActionCfgExceedSetValue.setStatus("current")


class _MpCbQosPoliceActionCfgViolate_Type(Integer32):
    """Custom type mpCbQosPoliceActionCfgViolate based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("transmit", 1),
          ("setIpDSCP", 2),
          ("setIpPrecedence", 3),
          ("setQosGroup", 4),
          ("drop", 5),
          ("setMplsExp", 6),
          ("setAtmClp", 7),
          ("setFrDe", 8),
          ("setL2Cos", 9),
          ("setDiscardClass", 10),
          ("setMplsExpTopMost", 11),
          ("setIpDscpTunnel", 12),
          ("setIpPrecedenceTunnel", 13),
          ("setL2CosInner", 14))
    )


_MpCbQosPoliceActionCfgViolate_Type.__name__ = "Integer32"
_MpCbQosPoliceActionCfgViolate_Object = MibTableColumn
mpCbQosPoliceActionCfgViolate = _MpCbQosPoliceActionCfgViolate_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13, 1, 1, 6),
    _MpCbQosPoliceActionCfgViolate_Type()
)
mpCbQosPoliceActionCfgViolate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceActionCfgViolate.setStatus("current")
_MpCbQosPoliceActionCfgViolateSetValue_Type = Unsigned32
_MpCbQosPoliceActionCfgViolateSetValue_Object = MibTableColumn
mpCbQosPoliceActionCfgViolateSetValue = _MpCbQosPoliceActionCfgViolateSetValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 13, 1, 1, 7),
    _MpCbQosPoliceActionCfgViolateSetValue_Type()
)
mpCbQosPoliceActionCfgViolateSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceActionCfgViolateSetValue.setStatus("current")
_MpCbQosTSCfg_ObjectIdentity = ObjectIdentity
mpCbQosTSCfg = _MpCbQosTSCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14)
)
_MpCbQosTSCfgTable_Object = MibTable
mpCbQosTSCfgTable = _MpCbQosTSCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1)
)
if mibBuilder.loadTexts:
    mpCbQosTSCfgTable.setStatus("current")
_MpCbQosTSCfgEntry_Object = MibTableRow
mpCbQosTSCfgEntry = _MpCbQosTSCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1)
)
mpCbQosTSCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosTSCfgEntry.setStatus("current")
_MpCbQosTSCfgRate64_Type = Unsigned64
_MpCbQosTSCfgRate64_Object = MibTableColumn
mpCbQosTSCfgRate64 = _MpCbQosTSCfgRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 1),
    _MpCbQosTSCfgRate64_Type()
)
mpCbQosTSCfgRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSCfgRate64.setUnits("bits/second")
_MpCbQosTSCfgBurstSize_Type = Integer32
_MpCbQosTSCfgBurstSize_Object = MibTableColumn
mpCbQosTSCfgBurstSize = _MpCbQosTSCfgBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 2),
    _MpCbQosTSCfgBurstSize_Type()
)
mpCbQosTSCfgBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSCfgBurstSize.setUnits("bits")
_MpCbQosTSCfgExtBurstSize_Type = Integer32
_MpCbQosTSCfgExtBurstSize_Object = MibTableColumn
mpCbQosTSCfgExtBurstSize = _MpCbQosTSCfgExtBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 3),
    _MpCbQosTSCfgExtBurstSize_Type()
)
mpCbQosTSCfgExtBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgExtBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSCfgExtBurstSize.setUnits("bits")
_MpCbQosTSCfgAdaptiveEnabled_Type = TruthValue
_MpCbQosTSCfgAdaptiveEnabled_Object = MibTableColumn
mpCbQosTSCfgAdaptiveEnabled = _MpCbQosTSCfgAdaptiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 4),
    _MpCbQosTSCfgAdaptiveEnabled_Type()
)
mpCbQosTSCfgAdaptiveEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgAdaptiveEnabled.setStatus("current")
_MpCbQosTSCfgAdaptiveRate64_Type = Unsigned64
_MpCbQosTSCfgAdaptiveRate64_Object = MibTableColumn
mpCbQosTSCfgAdaptiveRate64 = _MpCbQosTSCfgAdaptiveRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 5),
    _MpCbQosTSCfgAdaptiveRate64_Type()
)
mpCbQosTSCfgAdaptiveRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgAdaptiveRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSCfgAdaptiveRate64.setUnits("bits/second")


class _MpCbQosTSCfgLimitType_Type(Integer32):
    """Custom type mpCbQosTSCfgLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("peak", 2))
    )


_MpCbQosTSCfgLimitType_Type.__name__ = "Integer32"
_MpCbQosTSCfgLimitType_Object = MibTableColumn
mpCbQosTSCfgLimitType = _MpCbQosTSCfgLimitType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 6),
    _MpCbQosTSCfgLimitType_Type()
)
mpCbQosTSCfgLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgLimitType.setStatus("current")


class _MpCbQosTSCfgRateType_Type(Integer32):
    """Custom type mpCbQosTSCfgRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bps", 1),
          ("percentage", 2),
          ("cps", 3))
    )


_MpCbQosTSCfgRateType_Type.__name__ = "Integer32"
_MpCbQosTSCfgRateType_Object = MibTableColumn
mpCbQosTSCfgRateType = _MpCbQosTSCfgRateType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 7),
    _MpCbQosTSCfgRateType_Type()
)
mpCbQosTSCfgRateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgRateType.setStatus("current")


class _MpCbQosTSCfgPercentRateValue_Type(Unsigned32):
    """Custom type mpCbQosTSCfgPercentRateValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpCbQosTSCfgPercentRateValue_Type.__name__ = "Unsigned32"
_MpCbQosTSCfgPercentRateValue_Object = MibTableColumn
mpCbQosTSCfgPercentRateValue = _MpCbQosTSCfgPercentRateValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 8),
    _MpCbQosTSCfgPercentRateValue_Type()
)
mpCbQosTSCfgPercentRateValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgPercentRateValue.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSCfgPercentRateValue.setUnits("% of Interface Bandwidth")
_MpCbQosTSCfgBurstTime_Type = Unsigned32
_MpCbQosTSCfgBurstTime_Object = MibTableColumn
mpCbQosTSCfgBurstTime = _MpCbQosTSCfgBurstTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 9),
    _MpCbQosTSCfgBurstTime_Type()
)
mpCbQosTSCfgBurstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgBurstTime.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSCfgBurstTime.setUnits("milli-seconds")
_MpCbQosTSCfgExtBurstTime_Type = Unsigned32
_MpCbQosTSCfgExtBurstTime_Object = MibTableColumn
mpCbQosTSCfgExtBurstTime = _MpCbQosTSCfgExtBurstTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 14, 1, 1, 10),
    _MpCbQosTSCfgExtBurstTime_Type()
)
mpCbQosTSCfgExtBurstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSCfgExtBurstTime.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSCfgExtBurstTime.setUnits("milli-seconds")
_MpCbQosSetCfg_ObjectIdentity = ObjectIdentity
mpCbQosSetCfg = _MpCbQosSetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15)
)
_MpCbQosSetCfgTable_Object = MibTable
mpCbQosSetCfgTable = _MpCbQosSetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1)
)
if mibBuilder.loadTexts:
    mpCbQosSetCfgTable.setStatus("current")
_MpCbQosSetCfgEntry_Object = MibTableRow
mpCbQosSetCfgEntry = _MpCbQosSetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1)
)
mpCbQosSetCfgEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosConfigIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosSetCfgEntry.setStatus("current")


class _MpCbQosSetCfgFeature_Type(Bits):
    """Custom type mpCbQosSetCfgFeature based on Bits"""
    namedValues = NamedValues(
        *(("ipDscp", 0),
          ("ipPrecedence", 1),
          ("qosGroupNumber", 2),
          ("frDeBit", 3),
          ("atmClpBit", 4),
          ("l2Cos", 5),
          ("mplsExp", 6),
          ("discardClass", 7),
          ("mplsExpTopMost", 8),
          ("frFecnBecn", 9),
          ("ipDscpTunnel", 10),
          ("ipPrecedenceTunnel", 11),
          ("l2CosInner", 12),
          ("ipTos", 13))
    )

_MpCbQosSetCfgFeature_Type.__name__ = "Bits"
_MpCbQosSetCfgFeature_Object = MibTableColumn
mpCbQosSetCfgFeature = _MpCbQosSetCfgFeature_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 1),
    _MpCbQosSetCfgFeature_Type()
)
mpCbQosSetCfgFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgFeature.setStatus("current")


class _MpCbQosSetCfgIpDSCPValue_Type(Integer32):
    """Custom type mpCbQosSetCfgIpDSCPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpCbQosSetCfgIpDSCPValue_Type.__name__ = "Integer32"
_MpCbQosSetCfgIpDSCPValue_Object = MibTableColumn
mpCbQosSetCfgIpDSCPValue = _MpCbQosSetCfgIpDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 2),
    _MpCbQosSetCfgIpDSCPValue_Type()
)
mpCbQosSetCfgIpDSCPValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgIpDSCPValue.setStatus("current")


class _MpCbQosSetCfgIpPrecedenceValue_Type(Integer32):
    """Custom type mpCbQosSetCfgIpPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpCbQosSetCfgIpPrecedenceValue_Type.__name__ = "Integer32"
_MpCbQosSetCfgIpPrecedenceValue_Object = MibTableColumn
mpCbQosSetCfgIpPrecedenceValue = _MpCbQosSetCfgIpPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 3),
    _MpCbQosSetCfgIpPrecedenceValue_Type()
)
mpCbQosSetCfgIpPrecedenceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgIpPrecedenceValue.setStatus("current")
_MpCbQosSetCfgQosGroupValue_Type = Integer32
_MpCbQosSetCfgQosGroupValue_Object = MibTableColumn
mpCbQosSetCfgQosGroupValue = _MpCbQosSetCfgQosGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 4),
    _MpCbQosSetCfgQosGroupValue_Type()
)
mpCbQosSetCfgQosGroupValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgQosGroupValue.setStatus("current")


class _MpCbQosSetCfgL2CosValue_Type(Integer32):
    """Custom type mpCbQosSetCfgL2CosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpCbQosSetCfgL2CosValue_Type.__name__ = "Integer32"
_MpCbQosSetCfgL2CosValue_Object = MibTableColumn
mpCbQosSetCfgL2CosValue = _MpCbQosSetCfgL2CosValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 5),
    _MpCbQosSetCfgL2CosValue_Type()
)
mpCbQosSetCfgL2CosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgL2CosValue.setStatus("current")


class _MpCbQosSetCfgMplsExpValue_Type(Unsigned32):
    """Custom type mpCbQosSetCfgMplsExpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpCbQosSetCfgMplsExpValue_Type.__name__ = "Unsigned32"
_MpCbQosSetCfgMplsExpValue_Object = MibTableColumn
mpCbQosSetCfgMplsExpValue = _MpCbQosSetCfgMplsExpValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 6),
    _MpCbQosSetCfgMplsExpValue_Type()
)
mpCbQosSetCfgMplsExpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgMplsExpValue.setStatus("current")


class _MpCbQosSetCfgDiscardClassValue_Type(Unsigned32):
    """Custom type mpCbQosSetCfgDiscardClassValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpCbQosSetCfgDiscardClassValue_Type.__name__ = "Unsigned32"
_MpCbQosSetCfgDiscardClassValue_Object = MibTableColumn
mpCbQosSetCfgDiscardClassValue = _MpCbQosSetCfgDiscardClassValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 7),
    _MpCbQosSetCfgDiscardClassValue_Type()
)
mpCbQosSetCfgDiscardClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgDiscardClassValue.setStatus("current")


class _MpCbQosSetCfgMplsExpTopMostValue_Type(Unsigned32):
    """Custom type mpCbQosSetCfgMplsExpTopMostValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpCbQosSetCfgMplsExpTopMostValue_Type.__name__ = "Unsigned32"
_MpCbQosSetCfgMplsExpTopMostValue_Object = MibTableColumn
mpCbQosSetCfgMplsExpTopMostValue = _MpCbQosSetCfgMplsExpTopMostValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 8),
    _MpCbQosSetCfgMplsExpTopMostValue_Type()
)
mpCbQosSetCfgMplsExpTopMostValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgMplsExpTopMostValue.setStatus("current")
_MpCbQosSetCfgFrFecnBecn_Type = Unsigned32
_MpCbQosSetCfgFrFecnBecn_Object = MibTableColumn
mpCbQosSetCfgFrFecnBecn = _MpCbQosSetCfgFrFecnBecn_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 9),
    _MpCbQosSetCfgFrFecnBecn_Type()
)
mpCbQosSetCfgFrFecnBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgFrFecnBecn.setStatus("current")


class _MpCbQosSetCfgIpDSCPTunnelValue_Type(Integer32):
    """Custom type mpCbQosSetCfgIpDSCPTunnelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MpCbQosSetCfgIpDSCPTunnelValue_Type.__name__ = "Integer32"
_MpCbQosSetCfgIpDSCPTunnelValue_Object = MibTableColumn
mpCbQosSetCfgIpDSCPTunnelValue = _MpCbQosSetCfgIpDSCPTunnelValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 10),
    _MpCbQosSetCfgIpDSCPTunnelValue_Type()
)
mpCbQosSetCfgIpDSCPTunnelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgIpDSCPTunnelValue.setStatus("current")


class _MpCbQosSetCfgIpPrecedenceTunnelValue_Type(Integer32):
    """Custom type mpCbQosSetCfgIpPrecedenceTunnelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpCbQosSetCfgIpPrecedenceTunnelValue_Type.__name__ = "Integer32"
_MpCbQosSetCfgIpPrecedenceTunnelValue_Object = MibTableColumn
mpCbQosSetCfgIpPrecedenceTunnelValue = _MpCbQosSetCfgIpPrecedenceTunnelValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 11),
    _MpCbQosSetCfgIpPrecedenceTunnelValue_Type()
)
mpCbQosSetCfgIpPrecedenceTunnelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgIpPrecedenceTunnelValue.setStatus("current")


class _MpCbQosSetCfgL2CosInnerValue_Type(Integer32):
    """Custom type mpCbQosSetCfgL2CosInnerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MpCbQosSetCfgL2CosInnerValue_Type.__name__ = "Integer32"
_MpCbQosSetCfgL2CosInnerValue_Object = MibTableColumn
mpCbQosSetCfgL2CosInnerValue = _MpCbQosSetCfgL2CosInnerValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 12),
    _MpCbQosSetCfgL2CosInnerValue_Type()
)
mpCbQosSetCfgL2CosInnerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgL2CosInnerValue.setStatus("current")


class _MpCbQosSetCfgIpTosValue_Type(Integer32):
    """Custom type mpCbQosSetCfgIpTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpCbQosSetCfgIpTosValue_Type.__name__ = "Integer32"
_MpCbQosSetCfgIpTosValue_Object = MibTableColumn
mpCbQosSetCfgIpTosValue = _MpCbQosSetCfgIpTosValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 15, 1, 1, 13),
    _MpCbQosSetCfgIpTosValue_Type()
)
mpCbQosSetCfgIpTosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetCfgIpTosValue.setStatus("current")
_MpCbQosClassMapStats_ObjectIdentity = ObjectIdentity
mpCbQosClassMapStats = _MpCbQosClassMapStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16)
)
_MpCbQosCMStatsTable_Object = MibTable
mpCbQosCMStatsTable = _MpCbQosCMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1)
)
if mibBuilder.loadTexts:
    mpCbQosCMStatsTable.setStatus("current")
_MpCbQosCMStatsEntry_Object = MibTableRow
mpCbQosCMStatsEntry = _MpCbQosCMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1)
)
mpCbQosCMStatsEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosCMStatsEntry.setStatus("current")
_MpCbQosCMPrePolicyPkt64_Type = Counter64
_MpCbQosCMPrePolicyPkt64_Object = MibTableColumn
mpCbQosCMPrePolicyPkt64 = _MpCbQosCMPrePolicyPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 1),
    _MpCbQosCMPrePolicyPkt64_Type()
)
mpCbQosCMPrePolicyPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMPrePolicyPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMPrePolicyPkt64.setUnits("Packets")
_MpCbQosCMPrePolicyByte64_Type = Counter64
_MpCbQosCMPrePolicyByte64_Object = MibTableColumn
mpCbQosCMPrePolicyByte64 = _MpCbQosCMPrePolicyByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 2),
    _MpCbQosCMPrePolicyByte64_Type()
)
mpCbQosCMPrePolicyByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMPrePolicyByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMPrePolicyByte64.setUnits("Octets")
_MpCbQosCMPrePolicyBitRate64_Type = Unsigned64
_MpCbQosCMPrePolicyBitRate64_Object = MibTableColumn
mpCbQosCMPrePolicyBitRate64 = _MpCbQosCMPrePolicyBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 3),
    _MpCbQosCMPrePolicyBitRate64_Type()
)
mpCbQosCMPrePolicyBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMPrePolicyBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMPrePolicyBitRate64.setUnits("bits per second")
_MpCbQosCMPostPolicyPkt64_Type = Counter64
_MpCbQosCMPostPolicyPkt64_Object = MibTableColumn
mpCbQosCMPostPolicyPkt64 = _MpCbQosCMPostPolicyPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 4),
    _MpCbQosCMPostPolicyPkt64_Type()
)
mpCbQosCMPostPolicyPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMPostPolicyPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMPostPolicyPkt64.setUnits("Packets")
_MpCbQosCMPostPolicyByte64_Type = Counter64
_MpCbQosCMPostPolicyByte64_Object = MibTableColumn
mpCbQosCMPostPolicyByte64 = _MpCbQosCMPostPolicyByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 5),
    _MpCbQosCMPostPolicyByte64_Type()
)
mpCbQosCMPostPolicyByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMPostPolicyByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMPostPolicyByte64.setUnits("Octets")
_MpCbQosCMPostPolicyBitRate64_Type = Unsigned64
_MpCbQosCMPostPolicyBitRate64_Object = MibTableColumn
mpCbQosCMPostPolicyBitRate64 = _MpCbQosCMPostPolicyBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 6),
    _MpCbQosCMPostPolicyBitRate64_Type()
)
mpCbQosCMPostPolicyBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMPostPolicyBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMPostPolicyBitRate64.setUnits("bits per second")
_MpCbQosCMDropPkt64_Type = Counter64
_MpCbQosCMDropPkt64_Object = MibTableColumn
mpCbQosCMDropPkt64 = _MpCbQosCMDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 7),
    _MpCbQosCMDropPkt64_Type()
)
mpCbQosCMDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMDropPkt64.setUnits("Packets")
_MpCbQosCMDropByte64_Type = Counter64
_MpCbQosCMDropByte64_Object = MibTableColumn
mpCbQosCMDropByte64 = _MpCbQosCMDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 8),
    _MpCbQosCMDropByte64_Type()
)
mpCbQosCMDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMDropByte64.setUnits("Octets")
_MpCbQosCMDropBitRate64_Type = Unsigned64
_MpCbQosCMDropBitRate64_Object = MibTableColumn
mpCbQosCMDropBitRate64 = _MpCbQosCMDropBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 9),
    _MpCbQosCMDropBitRate64_Type()
)
mpCbQosCMDropBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMDropBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMDropBitRate64.setUnits("bits per second")
_MpCbQosCMNoBufDropPkt64_Type = Counter64
_MpCbQosCMNoBufDropPkt64_Object = MibTableColumn
mpCbQosCMNoBufDropPkt64 = _MpCbQosCMNoBufDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 16, 1, 1, 10),
    _MpCbQosCMNoBufDropPkt64_Type()
)
mpCbQosCMNoBufDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosCMNoBufDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosCMNoBufDropPkt64.setUnits("Packets")
_MpCbQosMatchStmtStats_ObjectIdentity = ObjectIdentity
mpCbQosMatchStmtStats = _MpCbQosMatchStmtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 17)
)
_MpCbQosMatchStmtStatsTable_Object = MibTable
mpCbQosMatchStmtStatsTable = _MpCbQosMatchStmtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 17, 1)
)
if mibBuilder.loadTexts:
    mpCbQosMatchStmtStatsTable.setStatus("current")
_MpCbQosMatchStmtStatsEntry_Object = MibTableRow
mpCbQosMatchStmtStatsEntry = _MpCbQosMatchStmtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 17, 1, 1)
)
mpCbQosMatchStmtStatsEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosMatchStmtStatsEntry.setStatus("current")
_MpCbQosMatchPrePolicyPkt64_Type = Counter64
_MpCbQosMatchPrePolicyPkt64_Object = MibTableColumn
mpCbQosMatchPrePolicyPkt64 = _MpCbQosMatchPrePolicyPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 17, 1, 1, 1),
    _MpCbQosMatchPrePolicyPkt64_Type()
)
mpCbQosMatchPrePolicyPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosMatchPrePolicyPkt64.setStatus("current")
_MpCbQosMatchPrePolicyByte64_Type = Counter64
_MpCbQosMatchPrePolicyByte64_Object = MibTableColumn
mpCbQosMatchPrePolicyByte64 = _MpCbQosMatchPrePolicyByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 17, 1, 1, 2),
    _MpCbQosMatchPrePolicyByte64_Type()
)
mpCbQosMatchPrePolicyByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosMatchPrePolicyByte64.setStatus("current")
_MpCbQosMatchPrePolicyBitRate64_Type = Unsigned64
_MpCbQosMatchPrePolicyBitRate64_Object = MibTableColumn
mpCbQosMatchPrePolicyBitRate64 = _MpCbQosMatchPrePolicyBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 17, 1, 1, 3),
    _MpCbQosMatchPrePolicyBitRate64_Type()
)
mpCbQosMatchPrePolicyBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosMatchPrePolicyBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosMatchPrePolicyBitRate64.setUnits("bits per second")
_MpCbQosPoliceStats_ObjectIdentity = ObjectIdentity
mpCbQosPoliceStats = _MpCbQosPoliceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18)
)
_MpCbQosPoliceStatsTable_Object = MibTable
mpCbQosPoliceStatsTable = _MpCbQosPoliceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1)
)
if mibBuilder.loadTexts:
    mpCbQosPoliceStatsTable.setStatus("current")
_MpCbQosPoliceStatsEntry_Object = MibTableRow
mpCbQosPoliceStatsEntry = _MpCbQosPoliceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1)
)
mpCbQosPoliceStatsEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosPoliceStatsEntry.setStatus("current")
_MpCbQosPoliceConformedPkt64_Type = Counter64
_MpCbQosPoliceConformedPkt64_Object = MibTableColumn
mpCbQosPoliceConformedPkt64 = _MpCbQosPoliceConformedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1, 1),
    _MpCbQosPoliceConformedPkt64_Type()
)
mpCbQosPoliceConformedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceConformedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceConformedPkt64.setUnits("Packets")
_MpCbQosPoliceConformedByte64_Type = Counter64
_MpCbQosPoliceConformedByte64_Object = MibTableColumn
mpCbQosPoliceConformedByte64 = _MpCbQosPoliceConformedByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1, 2),
    _MpCbQosPoliceConformedByte64_Type()
)
mpCbQosPoliceConformedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceConformedByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceConformedByte64.setUnits("Octets")
_MpCbQosPoliceConformedBitRate64_Type = Unsigned64
_MpCbQosPoliceConformedBitRate64_Object = MibTableColumn
mpCbQosPoliceConformedBitRate64 = _MpCbQosPoliceConformedBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1, 3),
    _MpCbQosPoliceConformedBitRate64_Type()
)
mpCbQosPoliceConformedBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceConformedBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceConformedBitRate64.setUnits("bits per second")
_MpCbQosPoliceExceededPkt64_Type = Counter64
_MpCbQosPoliceExceededPkt64_Object = MibTableColumn
mpCbQosPoliceExceededPkt64 = _MpCbQosPoliceExceededPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1, 4),
    _MpCbQosPoliceExceededPkt64_Type()
)
mpCbQosPoliceExceededPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceExceededPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceExceededPkt64.setUnits("Packets")
_MpCbQosPoliceExceededByte64_Type = Counter64
_MpCbQosPoliceExceededByte64_Object = MibTableColumn
mpCbQosPoliceExceededByte64 = _MpCbQosPoliceExceededByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1, 5),
    _MpCbQosPoliceExceededByte64_Type()
)
mpCbQosPoliceExceededByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceExceededByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceExceededByte64.setUnits("Octets")
_MpCbQosPoliceExceededBitRate64_Type = Unsigned64
_MpCbQosPoliceExceededBitRate64_Object = MibTableColumn
mpCbQosPoliceExceededBitRate64 = _MpCbQosPoliceExceededBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1, 6),
    _MpCbQosPoliceExceededBitRate64_Type()
)
mpCbQosPoliceExceededBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceExceededBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceExceededBitRate64.setUnits("bits per second")
_MpCbQosPoliceViolatedPkt64_Type = Counter64
_MpCbQosPoliceViolatedPkt64_Object = MibTableColumn
mpCbQosPoliceViolatedPkt64 = _MpCbQosPoliceViolatedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1, 7),
    _MpCbQosPoliceViolatedPkt64_Type()
)
mpCbQosPoliceViolatedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceViolatedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceViolatedPkt64.setUnits("Packets")
_MpCbQosPoliceViolatedByte64_Type = Counter64
_MpCbQosPoliceViolatedByte64_Object = MibTableColumn
mpCbQosPoliceViolatedByte64 = _MpCbQosPoliceViolatedByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1, 8),
    _MpCbQosPoliceViolatedByte64_Type()
)
mpCbQosPoliceViolatedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceViolatedByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceViolatedByte64.setUnits("Octets")
_MpCbQosPoliceViolatedBitRate64_Type = Unsigned64
_MpCbQosPoliceViolatedBitRate64_Object = MibTableColumn
mpCbQosPoliceViolatedBitRate64 = _MpCbQosPoliceViolatedBitRate64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 18, 1, 1, 9),
    _MpCbQosPoliceViolatedBitRate64_Type()
)
mpCbQosPoliceViolatedBitRate64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosPoliceViolatedBitRate64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosPoliceViolatedBitRate64.setUnits("bits per second")
_MpCbQosQueueingStats_ObjectIdentity = ObjectIdentity
mpCbQosQueueingStats = _MpCbQosQueueingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 19)
)
_MpCbQosQueueingStatsTable_Object = MibTable
mpCbQosQueueingStatsTable = _MpCbQosQueueingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 19, 1)
)
if mibBuilder.loadTexts:
    mpCbQosQueueingStatsTable.setStatus("current")
_MpCbQosQueueingStatsEntry_Object = MibTableRow
mpCbQosQueueingStatsEntry = _MpCbQosQueueingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 19, 1, 1)
)
mpCbQosQueueingStatsEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosQueueingStatsEntry.setStatus("current")


class _MpCbQosQueueingQDepthUnit_Type(Integer32):
    """Custom type mpCbQosQueueingQDepthUnit based on Integer32"""
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
        *(("packets", 1),
          ("bytes", 2),
          ("cells", 3),
          ("ms", 4),
          ("us", 5))
    )


_MpCbQosQueueingQDepthUnit_Type.__name__ = "Integer32"
_MpCbQosQueueingQDepthUnit_Object = MibTableColumn
mpCbQosQueueingQDepthUnit = _MpCbQosQueueingQDepthUnit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 19, 1, 1, 1),
    _MpCbQosQueueingQDepthUnit_Type()
)
mpCbQosQueueingQDepthUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingQDepthUnit.setStatus("current")
_MpCbQosQueueingCurrentQDepth_Type = Gauge32
_MpCbQosQueueingCurrentQDepth_Object = MibTableColumn
mpCbQosQueueingCurrentQDepth = _MpCbQosQueueingCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 19, 1, 1, 2),
    _MpCbQosQueueingCurrentQDepth_Type()
)
mpCbQosQueueingCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingCurrentQDepth.setStatus("current")
_MpCbQosQueueingMaxQDepth_Type = Gauge32
_MpCbQosQueueingMaxQDepth_Object = MibTableColumn
mpCbQosQueueingMaxQDepth = _MpCbQosQueueingMaxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 19, 1, 1, 3),
    _MpCbQosQueueingMaxQDepth_Type()
)
mpCbQosQueueingMaxQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingMaxQDepth.setStatus("current")
_MpCbQosQueueingDiscardByte64_Type = Counter64
_MpCbQosQueueingDiscardByte64_Object = MibTableColumn
mpCbQosQueueingDiscardByte64 = _MpCbQosQueueingDiscardByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 19, 1, 1, 4),
    _MpCbQosQueueingDiscardByte64_Type()
)
mpCbQosQueueingDiscardByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingDiscardByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosQueueingDiscardByte64.setUnits("Octets")
_MpCbQosQueueingDiscardPkt64_Type = Counter64
_MpCbQosQueueingDiscardPkt64_Object = MibTableColumn
mpCbQosQueueingDiscardPkt64 = _MpCbQosQueueingDiscardPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 19, 1, 1, 5),
    _MpCbQosQueueingDiscardPkt64_Type()
)
mpCbQosQueueingDiscardPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosQueueingDiscardPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosQueueingDiscardPkt64.setUnits("Packets")
_MpCbQosTSStats_ObjectIdentity = ObjectIdentity
mpCbQosTSStats = _MpCbQosTSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 20)
)
_MpCbQosTSStatsTable_Object = MibTable
mpCbQosTSStatsTable = _MpCbQosTSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 20, 1)
)
if mibBuilder.loadTexts:
    mpCbQosTSStatsTable.setStatus("current")
_MpCbQosTSStatsEntry_Object = MibTableRow
mpCbQosTSStatsEntry = _MpCbQosTSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 20, 1, 1)
)
mpCbQosTSStatsEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosTSStatsEntry.setStatus("current")
_MpCbQosTSStatsDelayedByte64_Type = Counter64
_MpCbQosTSStatsDelayedByte64_Object = MibTableColumn
mpCbQosTSStatsDelayedByte64 = _MpCbQosTSStatsDelayedByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 20, 1, 1, 1),
    _MpCbQosTSStatsDelayedByte64_Type()
)
mpCbQosTSStatsDelayedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSStatsDelayedByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSStatsDelayedByte64.setUnits("Octets")
_MpCbQosTSStatsDelayedPkt64_Type = Counter64
_MpCbQosTSStatsDelayedPkt64_Object = MibTableColumn
mpCbQosTSStatsDelayedPkt64 = _MpCbQosTSStatsDelayedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 20, 1, 1, 2),
    _MpCbQosTSStatsDelayedPkt64_Type()
)
mpCbQosTSStatsDelayedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSStatsDelayedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSStatsDelayedPkt64.setUnits("Packets")
_MpCbQosTSStatsDropByte64_Type = Counter64
_MpCbQosTSStatsDropByte64_Object = MibTableColumn
mpCbQosTSStatsDropByte64 = _MpCbQosTSStatsDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 20, 1, 1, 3),
    _MpCbQosTSStatsDropByte64_Type()
)
mpCbQosTSStatsDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSStatsDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSStatsDropByte64.setUnits("Octets")
_MpCbQosTSStatsDropPkt64_Type = Counter64
_MpCbQosTSStatsDropPkt64_Object = MibTableColumn
mpCbQosTSStatsDropPkt64 = _MpCbQosTSStatsDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 20, 1, 1, 4),
    _MpCbQosTSStatsDropPkt64_Type()
)
mpCbQosTSStatsDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSStatsDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSStatsDropPkt64.setUnits("Packets")
_MpCbQosTSStatsActive_Type = TruthValue
_MpCbQosTSStatsActive_Object = MibTableColumn
mpCbQosTSStatsActive = _MpCbQosTSStatsActive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 20, 1, 1, 5),
    _MpCbQosTSStatsActive_Type()
)
mpCbQosTSStatsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSStatsActive.setStatus("current")
_MpCbQosTSStatsCurrentQSize_Type = Gauge32
_MpCbQosTSStatsCurrentQSize_Object = MibTableColumn
mpCbQosTSStatsCurrentQSize = _MpCbQosTSStatsCurrentQSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 20, 1, 1, 6),
    _MpCbQosTSStatsCurrentQSize_Type()
)
mpCbQosTSStatsCurrentQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosTSStatsCurrentQSize.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosTSStatsCurrentQSize.setUnits("Packets")
_MpCbQosREDClassStats_ObjectIdentity = ObjectIdentity
mpCbQosREDClassStats = _MpCbQosREDClassStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21)
)
_MpCbQosREDClassStatsTable_Object = MibTable
mpCbQosREDClassStatsTable = _MpCbQosREDClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1)
)
if mibBuilder.loadTexts:
    mpCbQosREDClassStatsTable.setStatus("current")
_MpCbQosREDClassStatsEntry_Object = MibTableRow
mpCbQosREDClassStatsEntry = _MpCbQosREDClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1)
)
mpCbQosREDClassStatsEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosObjectsIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosREDValue"),
)
if mibBuilder.loadTexts:
    mpCbQosREDClassStatsEntry.setStatus("current")
_MpCbQosREDRandomDropPkt64_Type = Counter64
_MpCbQosREDRandomDropPkt64_Object = MibTableColumn
mpCbQosREDRandomDropPkt64 = _MpCbQosREDRandomDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 1),
    _MpCbQosREDRandomDropPkt64_Type()
)
mpCbQosREDRandomDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDRandomDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDRandomDropPkt64.setUnits("Packets")
_MpCbQosREDRandomDropByte64_Type = Counter64
_MpCbQosREDRandomDropByte64_Object = MibTableColumn
mpCbQosREDRandomDropByte64 = _MpCbQosREDRandomDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 2),
    _MpCbQosREDRandomDropByte64_Type()
)
mpCbQosREDRandomDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDRandomDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDRandomDropByte64.setUnits("Octets")
_MpCbQosREDTailDropPkt64_Type = Counter64
_MpCbQosREDTailDropPkt64_Object = MibTableColumn
mpCbQosREDTailDropPkt64 = _MpCbQosREDTailDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 3),
    _MpCbQosREDTailDropPkt64_Type()
)
mpCbQosREDTailDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDTailDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDTailDropPkt64.setUnits("Packets")
_MpCbQosREDTailDropByte64_Type = Counter64
_MpCbQosREDTailDropByte64_Object = MibTableColumn
mpCbQosREDTailDropByte64 = _MpCbQosREDTailDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 4),
    _MpCbQosREDTailDropByte64_Type()
)
mpCbQosREDTailDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDTailDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDTailDropByte64.setUnits("Octets")
_MpCbQosREDTransmitPkt64_Type = Counter64
_MpCbQosREDTransmitPkt64_Object = MibTableColumn
mpCbQosREDTransmitPkt64 = _MpCbQosREDTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 5),
    _MpCbQosREDTransmitPkt64_Type()
)
mpCbQosREDTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDTransmitPkt64.setUnits("Packets")
_MpCbQosREDTransmitByte64_Type = Counter64
_MpCbQosREDTransmitByte64_Object = MibTableColumn
mpCbQosREDTransmitByte64 = _MpCbQosREDTransmitByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 6),
    _MpCbQosREDTransmitByte64_Type()
)
mpCbQosREDTransmitByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDTransmitByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDTransmitByte64.setUnits("Octets")
_MpCbQosREDECNMarkPkt64_Type = Counter64
_MpCbQosREDECNMarkPkt64_Object = MibTableColumn
mpCbQosREDECNMarkPkt64 = _MpCbQosREDECNMarkPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 7),
    _MpCbQosREDECNMarkPkt64_Type()
)
mpCbQosREDECNMarkPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDECNMarkPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDECNMarkPkt64.setUnits("Packets")
_MpCbQosREDECNMarkByte64_Type = Counter64
_MpCbQosREDECNMarkByte64_Object = MibTableColumn
mpCbQosREDECNMarkByte64 = _MpCbQosREDECNMarkByte64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 8),
    _MpCbQosREDECNMarkByte64_Type()
)
mpCbQosREDECNMarkByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDECNMarkByte64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosREDECNMarkByte64.setUnits("Octets")


class _MpCbQosREDMeanQSizeUnits_Type(Integer32):
    """Custom type mpCbQosREDMeanQSizeUnits based on Integer32"""
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
        *(("packets", 1),
          ("bytes", 2),
          ("cells", 3),
          ("ms", 4),
          ("us", 5))
    )


_MpCbQosREDMeanQSizeUnits_Type.__name__ = "Integer32"
_MpCbQosREDMeanQSizeUnits_Object = MibTableColumn
mpCbQosREDMeanQSizeUnits = _MpCbQosREDMeanQSizeUnits_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 9),
    _MpCbQosREDMeanQSizeUnits_Type()
)
mpCbQosREDMeanQSizeUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDMeanQSizeUnits.setStatus("current")
_MpCbQosREDMeanQSize_Type = Unsigned32
_MpCbQosREDMeanQSize_Object = MibTableColumn
mpCbQosREDMeanQSize = _MpCbQosREDMeanQSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 21, 1, 1, 10),
    _MpCbQosREDMeanQSize_Type()
)
mpCbQosREDMeanQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosREDMeanQSize.setStatus("current")
_MpCbQosSetStats_ObjectIdentity = ObjectIdentity
mpCbQosSetStats = _MpCbQosSetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22)
)
_MpCbQosSetStatsTable_Object = MibTable
mpCbQosSetStatsTable = _MpCbQosSetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1)
)
if mibBuilder.loadTexts:
    mpCbQosSetStatsTable.setStatus("current")
_MpCbQosSetStatsEntry_Object = MibTableRow
mpCbQosSetStatsEntry = _MpCbQosSetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1)
)
mpCbQosSetStatsEntry.setIndexNames(
    (0, "MAIPU-CBQOS-MIB", "mpCbQosPolicyIndex"),
    (0, "MAIPU-CBQOS-MIB", "mpCbQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    mpCbQosSetStatsEntry.setStatus("current")
_MpCbQosSetDscpPkt64_Type = Counter64
_MpCbQosSetDscpPkt64_Object = MibTableColumn
mpCbQosSetDscpPkt64 = _MpCbQosSetDscpPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 1),
    _MpCbQosSetDscpPkt64_Type()
)
mpCbQosSetDscpPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetDscpPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetDscpPkt64.setUnits("Packets")
_MpCbQosSetPrecedencePkt64_Type = Counter64
_MpCbQosSetPrecedencePkt64_Object = MibTableColumn
mpCbQosSetPrecedencePkt64 = _MpCbQosSetPrecedencePkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 2),
    _MpCbQosSetPrecedencePkt64_Type()
)
mpCbQosSetPrecedencePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetPrecedencePkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetPrecedencePkt64.setUnits("Packets")
_MpCbQosSetQosGroupPkt64_Type = Counter64
_MpCbQosSetQosGroupPkt64_Object = MibTableColumn
mpCbQosSetQosGroupPkt64 = _MpCbQosSetQosGroupPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 3),
    _MpCbQosSetQosGroupPkt64_Type()
)
mpCbQosSetQosGroupPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetQosGroupPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetQosGroupPkt64.setUnits("Packets")
_MpCbQosSetFrDePkt64_Type = Counter64
_MpCbQosSetFrDePkt64_Object = MibTableColumn
mpCbQosSetFrDePkt64 = _MpCbQosSetFrDePkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 4),
    _MpCbQosSetFrDePkt64_Type()
)
mpCbQosSetFrDePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetFrDePkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetFrDePkt64.setUnits("Packets")
_MpCbQosSetAtmClpPkt64_Type = Counter64
_MpCbQosSetAtmClpPkt64_Object = MibTableColumn
mpCbQosSetAtmClpPkt64 = _MpCbQosSetAtmClpPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 5),
    _MpCbQosSetAtmClpPkt64_Type()
)
mpCbQosSetAtmClpPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetAtmClpPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetAtmClpPkt64.setUnits("Packets")
_MpCbQosSetL2CosPkt64_Type = Counter64
_MpCbQosSetL2CosPkt64_Object = MibTableColumn
mpCbQosSetL2CosPkt64 = _MpCbQosSetL2CosPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 6),
    _MpCbQosSetL2CosPkt64_Type()
)
mpCbQosSetL2CosPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetL2CosPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetL2CosPkt64.setUnits("Packets")
_MpCbQosSetMplsExpImpositionPkt64_Type = Counter64
_MpCbQosSetMplsExpImpositionPkt64_Object = MibTableColumn
mpCbQosSetMplsExpImpositionPkt64 = _MpCbQosSetMplsExpImpositionPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 7),
    _MpCbQosSetMplsExpImpositionPkt64_Type()
)
mpCbQosSetMplsExpImpositionPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetMplsExpImpositionPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetMplsExpImpositionPkt64.setUnits("Packets")
_MpCbQosSetDiscardClassPkt64_Type = Counter64
_MpCbQosSetDiscardClassPkt64_Object = MibTableColumn
mpCbQosSetDiscardClassPkt64 = _MpCbQosSetDiscardClassPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 8),
    _MpCbQosSetDiscardClassPkt64_Type()
)
mpCbQosSetDiscardClassPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetDiscardClassPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetDiscardClassPkt64.setUnits("Packets")
_MpCbQosSetMplsExpTopMostPkt64_Type = Counter64
_MpCbQosSetMplsExpTopMostPkt64_Object = MibTableColumn
mpCbQosSetMplsExpTopMostPkt64 = _MpCbQosSetMplsExpTopMostPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 9),
    _MpCbQosSetMplsExpTopMostPkt64_Type()
)
mpCbQosSetMplsExpTopMostPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetMplsExpTopMostPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetMplsExpTopMostPkt64.setUnits("Packets")
_MpCbQosSetFrFecnBecnPkt64_Type = Counter64
_MpCbQosSetFrFecnBecnPkt64_Object = MibTableColumn
mpCbQosSetFrFecnBecnPkt64 = _MpCbQosSetFrFecnBecnPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 10),
    _MpCbQosSetFrFecnBecnPkt64_Type()
)
mpCbQosSetFrFecnBecnPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetFrFecnBecnPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetFrFecnBecnPkt64.setUnits("Packets")
_MpCbQosSetDscpTunnelPkt64_Type = Counter64
_MpCbQosSetDscpTunnelPkt64_Object = MibTableColumn
mpCbQosSetDscpTunnelPkt64 = _MpCbQosSetDscpTunnelPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 11),
    _MpCbQosSetDscpTunnelPkt64_Type()
)
mpCbQosSetDscpTunnelPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetDscpTunnelPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetDscpTunnelPkt64.setUnits("Packets")
_MpCbQosSetPrecedenceTunnelPkt64_Type = Counter64
_MpCbQosSetPrecedenceTunnelPkt64_Object = MibTableColumn
mpCbQosSetPrecedenceTunnelPkt64 = _MpCbQosSetPrecedenceTunnelPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 12),
    _MpCbQosSetPrecedenceTunnelPkt64_Type()
)
mpCbQosSetPrecedenceTunnelPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetPrecedenceTunnelPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetPrecedenceTunnelPkt64.setUnits("Packets")
_MpCbQosSetTosPkt64_Type = Counter64
_MpCbQosSetTosPkt64_Object = MibTableColumn
mpCbQosSetTosPkt64 = _MpCbQosSetTosPkt64_Object(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2, 3, 4, 1, 22, 1, 1, 13),
    _MpCbQosSetTosPkt64_Type()
)
mpCbQosSetTosPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpCbQosSetTosPkt64.setStatus("current")
if mibBuilder.loadTexts:
    mpCbQosSetTosPkt64.setUnits("Packets")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-CBQOS-MIB",
    **{"Unsigned64": Unsigned64,
       "maipu": maipu,
       "mpMgmt2": mpMgmt2,
       "mpRouterTech": mpRouterTech,
       "mpRtQoSv2": mpRtQoSv2,
       "maipuCBQosMIB": maipuCBQosMIB,
       "maipuCBQosMIBObjects": maipuCBQosMIBObjects,
       "mpCbQosServicePolicy": mpCbQosServicePolicy,
       "mpCbQosServicePolicyTable": mpCbQosServicePolicyTable,
       "mpCbQosServicePolicyEntry": mpCbQosServicePolicyEntry,
       "mpCbQosPolicyIndex": mpCbQosPolicyIndex,
       "mpCbQosIfType": mpCbQosIfType,
       "mpCbQosPolicyDirection": mpCbQosPolicyDirection,
       "mpCbQosIfIndex": mpCbQosIfIndex,
       "mpCbQosFrDLCI": mpCbQosFrDLCI,
       "mpCbQosAtmVPI": mpCbQosAtmVPI,
       "mpCbQosAtmVCI": mpCbQosAtmVCI,
       "mpCbQosEntityIndex": mpCbQosEntityIndex,
       "mpCbQosVlanIndex": mpCbQosVlanIndex,
       "mpCbQosInterfacePolicy": mpCbQosInterfacePolicy,
       "mpCbQosInterfacePolicyTable": mpCbQosInterfacePolicyTable,
       "mpCbQosInterfacePolicyEntry": mpCbQosInterfacePolicyEntry,
       "mpCbQosIFPolicyIndex": mpCbQosIFPolicyIndex,
       "mpCbQosFrameRelayVCPolicy": mpCbQosFrameRelayVCPolicy,
       "mpCbQosFrameRelayPolicyTable": mpCbQosFrameRelayPolicyTable,
       "mpCbQosFrameRelayPolicyEntry": mpCbQosFrameRelayPolicyEntry,
       "mpCbQosFRPolicyIndex": mpCbQosFRPolicyIndex,
       "mpCbQosATMPVCPolicy": mpCbQosATMPVCPolicy,
       "mpCbQosATMPVCPolicyTable": mpCbQosATMPVCPolicyTable,
       "mpCbQosATMPVCPolicyEntry": mpCbQosATMPVCPolicyEntry,
       "mpCbQosATMPVCPolicyIndex": mpCbQosATMPVCPolicyIndex,
       "mpCbQosObjects": mpCbQosObjects,
       "mpCbQosObjectsTable": mpCbQosObjectsTable,
       "mpCbQosObjectsEntry": mpCbQosObjectsEntry,
       "mpCbQosObjectsIndex": mpCbQosObjectsIndex,
       "mpCbQosConfigIndex": mpCbQosConfigIndex,
       "mpCbQosObjectsType": mpCbQosObjectsType,
       "mpCbQosParentObjectsIndex": mpCbQosParentObjectsIndex,
       "mpCbQosPolicyMapCfg": mpCbQosPolicyMapCfg,
       "mpCbQosPolicyMapCfgTable": mpCbQosPolicyMapCfgTable,
       "mpCbQosPolicyMapCfgEntry": mpCbQosPolicyMapCfgEntry,
       "mpCbQosPolicyMapName": mpCbQosPolicyMapName,
       "mpCbQosPolicyMapDesc": mpCbQosPolicyMapDesc,
       "mpCbQosClassMapCfg": mpCbQosClassMapCfg,
       "mpCbQosCMCfgTable": mpCbQosCMCfgTable,
       "mpCbQosCMCfgEntry": mpCbQosCMCfgEntry,
       "mpCbQosCMName": mpCbQosCMName,
       "mpCbQosCMDesc": mpCbQosCMDesc,
       "mpCbQosCMInfo": mpCbQosCMInfo,
       "mpCbQosMatchStmtCfg": mpCbQosMatchStmtCfg,
       "mpCbQosMatchStmtCfgTable": mpCbQosMatchStmtCfgTable,
       "mpCbQosMatchStmtCfgEntry": mpCbQosMatchStmtCfgEntry,
       "mpCbQosMatchStmtName": mpCbQosMatchStmtName,
       "mpCbQosMatchStmtInfo": mpCbQosMatchStmtInfo,
       "mpCbQosQueueingCfg": mpCbQosQueueingCfg,
       "mpCbQosQueueingCfgTable": mpCbQosQueueingCfgTable,
       "mpCbQosQueueingCfgEntry": mpCbQosQueueingCfgEntry,
       "mpCbQosQueueingCfgBandwidth": mpCbQosQueueingCfgBandwidth,
       "mpCbQosQueueingCfgBandwidthUnits": mpCbQosQueueingCfgBandwidthUnits,
       "mpCbQosQueueingCfgFlowEnabled": mpCbQosQueueingCfgFlowEnabled,
       "mpCbQosQueueingCfgPriorityEnabled": mpCbQosQueueingCfgPriorityEnabled,
       "mpCbQosQueueingCfgDynamicQNumber": mpCbQosQueueingCfgDynamicQNumber,
       "mpCbQosQueueingCfgPrioBurstSize": mpCbQosQueueingCfgPrioBurstSize,
       "mpCbQosQueueingCfgQLimitUnits": mpCbQosQueueingCfgQLimitUnits,
       "mpCbQosQueueingCfgAggregateQLimit": mpCbQosQueueingCfgAggregateQLimit,
       "mpCbQosQueueingCfgAggrQLimitTime": mpCbQosQueueingCfgAggrQLimitTime,
       "mpCbQosQueueingCfgIndividualQLimit": mpCbQosQueueingCfgIndividualQLimit,
       "mpCbQosREDCfg": mpCbQosREDCfg,
       "mpCbQosREDCfgTable": mpCbQosREDCfgTable,
       "mpCbQosREDCfgEntry": mpCbQosREDCfgEntry,
       "mpCbQosREDCfgExponWeight": mpCbQosREDCfgExponWeight,
       "mpCbQosREDCfgDscpPrec": mpCbQosREDCfgDscpPrec,
       "mpCbQosREDCfgECNEnabled": mpCbQosREDCfgECNEnabled,
       "mpCbQosREDClassCfg": mpCbQosREDClassCfg,
       "mpCbQosREDClassCfgTable": mpCbQosREDClassCfgTable,
       "mpCbQosREDClassCfgEntry": mpCbQosREDClassCfgEntry,
       "mpCbQosREDValue": mpCbQosREDValue,
       "mpCbQosREDCfgPktDropProb": mpCbQosREDCfgPktDropProb,
       "mpCbQosREDClassCfgMinThresholdUnit": mpCbQosREDClassCfgMinThresholdUnit,
       "mpCbQosREDClassCfgMaxThresholdUnit": mpCbQosREDClassCfgMaxThresholdUnit,
       "mpCbQosREDClassCfgMinThreshold": mpCbQosREDClassCfgMinThreshold,
       "mpCbQosREDClassCfgMaxThreshold": mpCbQosREDClassCfgMaxThreshold,
       "mpCbQosREDClassCfgMinThresholdTime": mpCbQosREDClassCfgMinThresholdTime,
       "mpCbQosREDClassCfgMaxThresholdTime": mpCbQosREDClassCfgMaxThresholdTime,
       "mpCbQosPoliceCfg": mpCbQosPoliceCfg,
       "mpCbQosPoliceCfgTable": mpCbQosPoliceCfgTable,
       "mpCbQosPoliceCfgEntry": mpCbQosPoliceCfgEntry,
       "mpCbQosPoliceCfgRate64": mpCbQosPoliceCfgRate64,
       "mpCbQosPoliceCfgBurstSize": mpCbQosPoliceCfgBurstSize,
       "mpCbQosPoliceCfgExtBurstSize": mpCbQosPoliceCfgExtBurstSize,
       "mpCbQosPoliceCfgPir64": mpCbQosPoliceCfgPir64,
       "mpCbQosPoliceCfgRateType": mpCbQosPoliceCfgRateType,
       "mpCbQosPoliceCfgPercentRateValue": mpCbQosPoliceCfgPercentRateValue,
       "mpCbQosPoliceCfgPercentPirValue": mpCbQosPoliceCfgPercentPirValue,
       "mpCbQosPoliceCfgCellRate": mpCbQosPoliceCfgCellRate,
       "mpCbQosPoliceCfgCellPir": mpCbQosPoliceCfgCellPir,
       "mpCbQosPoliceCfgBurstCell": mpCbQosPoliceCfgBurstCell,
       "mpCbQosPoliceCfgExtBurstCell": mpCbQosPoliceCfgExtBurstCell,
       "mpCbQosPoliceCfgBurstTime": mpCbQosPoliceCfgBurstTime,
       "mpCbQosPoliceCfgExtBurstTime": mpCbQosPoliceCfgExtBurstTime,
       "mpCbQosPoliceActionCfg": mpCbQosPoliceActionCfg,
       "mpCbQosPoliceActionCfgTable": mpCbQosPoliceActionCfgTable,
       "mpCbQosPoliceActionCfgEntry": mpCbQosPoliceActionCfgEntry,
       "mpCbQosPoliceActionCfgIndex": mpCbQosPoliceActionCfgIndex,
       "mpCbQosPoliceActionCfgConform": mpCbQosPoliceActionCfgConform,
       "mpCbQosPoliceActionCfgConformSetValue": mpCbQosPoliceActionCfgConformSetValue,
       "mpCbQosPoliceActionCfgExceed": mpCbQosPoliceActionCfgExceed,
       "mpCbQosPoliceActionCfgExceedSetValue": mpCbQosPoliceActionCfgExceedSetValue,
       "mpCbQosPoliceActionCfgViolate": mpCbQosPoliceActionCfgViolate,
       "mpCbQosPoliceActionCfgViolateSetValue": mpCbQosPoliceActionCfgViolateSetValue,
       "mpCbQosTSCfg": mpCbQosTSCfg,
       "mpCbQosTSCfgTable": mpCbQosTSCfgTable,
       "mpCbQosTSCfgEntry": mpCbQosTSCfgEntry,
       "mpCbQosTSCfgRate64": mpCbQosTSCfgRate64,
       "mpCbQosTSCfgBurstSize": mpCbQosTSCfgBurstSize,
       "mpCbQosTSCfgExtBurstSize": mpCbQosTSCfgExtBurstSize,
       "mpCbQosTSCfgAdaptiveEnabled": mpCbQosTSCfgAdaptiveEnabled,
       "mpCbQosTSCfgAdaptiveRate64": mpCbQosTSCfgAdaptiveRate64,
       "mpCbQosTSCfgLimitType": mpCbQosTSCfgLimitType,
       "mpCbQosTSCfgRateType": mpCbQosTSCfgRateType,
       "mpCbQosTSCfgPercentRateValue": mpCbQosTSCfgPercentRateValue,
       "mpCbQosTSCfgBurstTime": mpCbQosTSCfgBurstTime,
       "mpCbQosTSCfgExtBurstTime": mpCbQosTSCfgExtBurstTime,
       "mpCbQosSetCfg": mpCbQosSetCfg,
       "mpCbQosSetCfgTable": mpCbQosSetCfgTable,
       "mpCbQosSetCfgEntry": mpCbQosSetCfgEntry,
       "mpCbQosSetCfgFeature": mpCbQosSetCfgFeature,
       "mpCbQosSetCfgIpDSCPValue": mpCbQosSetCfgIpDSCPValue,
       "mpCbQosSetCfgIpPrecedenceValue": mpCbQosSetCfgIpPrecedenceValue,
       "mpCbQosSetCfgQosGroupValue": mpCbQosSetCfgQosGroupValue,
       "mpCbQosSetCfgL2CosValue": mpCbQosSetCfgL2CosValue,
       "mpCbQosSetCfgMplsExpValue": mpCbQosSetCfgMplsExpValue,
       "mpCbQosSetCfgDiscardClassValue": mpCbQosSetCfgDiscardClassValue,
       "mpCbQosSetCfgMplsExpTopMostValue": mpCbQosSetCfgMplsExpTopMostValue,
       "mpCbQosSetCfgFrFecnBecn": mpCbQosSetCfgFrFecnBecn,
       "mpCbQosSetCfgIpDSCPTunnelValue": mpCbQosSetCfgIpDSCPTunnelValue,
       "mpCbQosSetCfgIpPrecedenceTunnelValue": mpCbQosSetCfgIpPrecedenceTunnelValue,
       "mpCbQosSetCfgL2CosInnerValue": mpCbQosSetCfgL2CosInnerValue,
       "mpCbQosSetCfgIpTosValue": mpCbQosSetCfgIpTosValue,
       "mpCbQosClassMapStats": mpCbQosClassMapStats,
       "mpCbQosCMStatsTable": mpCbQosCMStatsTable,
       "mpCbQosCMStatsEntry": mpCbQosCMStatsEntry,
       "mpCbQosCMPrePolicyPkt64": mpCbQosCMPrePolicyPkt64,
       "mpCbQosCMPrePolicyByte64": mpCbQosCMPrePolicyByte64,
       "mpCbQosCMPrePolicyBitRate64": mpCbQosCMPrePolicyBitRate64,
       "mpCbQosCMPostPolicyPkt64": mpCbQosCMPostPolicyPkt64,
       "mpCbQosCMPostPolicyByte64": mpCbQosCMPostPolicyByte64,
       "mpCbQosCMPostPolicyBitRate64": mpCbQosCMPostPolicyBitRate64,
       "mpCbQosCMDropPkt64": mpCbQosCMDropPkt64,
       "mpCbQosCMDropByte64": mpCbQosCMDropByte64,
       "mpCbQosCMDropBitRate64": mpCbQosCMDropBitRate64,
       "mpCbQosCMNoBufDropPkt64": mpCbQosCMNoBufDropPkt64,
       "mpCbQosMatchStmtStats": mpCbQosMatchStmtStats,
       "mpCbQosMatchStmtStatsTable": mpCbQosMatchStmtStatsTable,
       "mpCbQosMatchStmtStatsEntry": mpCbQosMatchStmtStatsEntry,
       "mpCbQosMatchPrePolicyPkt64": mpCbQosMatchPrePolicyPkt64,
       "mpCbQosMatchPrePolicyByte64": mpCbQosMatchPrePolicyByte64,
       "mpCbQosMatchPrePolicyBitRate64": mpCbQosMatchPrePolicyBitRate64,
       "mpCbQosPoliceStats": mpCbQosPoliceStats,
       "mpCbQosPoliceStatsTable": mpCbQosPoliceStatsTable,
       "mpCbQosPoliceStatsEntry": mpCbQosPoliceStatsEntry,
       "mpCbQosPoliceConformedPkt64": mpCbQosPoliceConformedPkt64,
       "mpCbQosPoliceConformedByte64": mpCbQosPoliceConformedByte64,
       "mpCbQosPoliceConformedBitRate64": mpCbQosPoliceConformedBitRate64,
       "mpCbQosPoliceExceededPkt64": mpCbQosPoliceExceededPkt64,
       "mpCbQosPoliceExceededByte64": mpCbQosPoliceExceededByte64,
       "mpCbQosPoliceExceededBitRate64": mpCbQosPoliceExceededBitRate64,
       "mpCbQosPoliceViolatedPkt64": mpCbQosPoliceViolatedPkt64,
       "mpCbQosPoliceViolatedByte64": mpCbQosPoliceViolatedByte64,
       "mpCbQosPoliceViolatedBitRate64": mpCbQosPoliceViolatedBitRate64,
       "mpCbQosQueueingStats": mpCbQosQueueingStats,
       "mpCbQosQueueingStatsTable": mpCbQosQueueingStatsTable,
       "mpCbQosQueueingStatsEntry": mpCbQosQueueingStatsEntry,
       "mpCbQosQueueingQDepthUnit": mpCbQosQueueingQDepthUnit,
       "mpCbQosQueueingCurrentQDepth": mpCbQosQueueingCurrentQDepth,
       "mpCbQosQueueingMaxQDepth": mpCbQosQueueingMaxQDepth,
       "mpCbQosQueueingDiscardByte64": mpCbQosQueueingDiscardByte64,
       "mpCbQosQueueingDiscardPkt64": mpCbQosQueueingDiscardPkt64,
       "mpCbQosTSStats": mpCbQosTSStats,
       "mpCbQosTSStatsTable": mpCbQosTSStatsTable,
       "mpCbQosTSStatsEntry": mpCbQosTSStatsEntry,
       "mpCbQosTSStatsDelayedByte64": mpCbQosTSStatsDelayedByte64,
       "mpCbQosTSStatsDelayedPkt64": mpCbQosTSStatsDelayedPkt64,
       "mpCbQosTSStatsDropByte64": mpCbQosTSStatsDropByte64,
       "mpCbQosTSStatsDropPkt64": mpCbQosTSStatsDropPkt64,
       "mpCbQosTSStatsActive": mpCbQosTSStatsActive,
       "mpCbQosTSStatsCurrentQSize": mpCbQosTSStatsCurrentQSize,
       "mpCbQosREDClassStats": mpCbQosREDClassStats,
       "mpCbQosREDClassStatsTable": mpCbQosREDClassStatsTable,
       "mpCbQosREDClassStatsEntry": mpCbQosREDClassStatsEntry,
       "mpCbQosREDRandomDropPkt64": mpCbQosREDRandomDropPkt64,
       "mpCbQosREDRandomDropByte64": mpCbQosREDRandomDropByte64,
       "mpCbQosREDTailDropPkt64": mpCbQosREDTailDropPkt64,
       "mpCbQosREDTailDropByte64": mpCbQosREDTailDropByte64,
       "mpCbQosREDTransmitPkt64": mpCbQosREDTransmitPkt64,
       "mpCbQosREDTransmitByte64": mpCbQosREDTransmitByte64,
       "mpCbQosREDECNMarkPkt64": mpCbQosREDECNMarkPkt64,
       "mpCbQosREDECNMarkByte64": mpCbQosREDECNMarkByte64,
       "mpCbQosREDMeanQSizeUnits": mpCbQosREDMeanQSizeUnits,
       "mpCbQosREDMeanQSize": mpCbQosREDMeanQSize,
       "mpCbQosSetStats": mpCbQosSetStats,
       "mpCbQosSetStatsTable": mpCbQosSetStatsTable,
       "mpCbQosSetStatsEntry": mpCbQosSetStatsEntry,
       "mpCbQosSetDscpPkt64": mpCbQosSetDscpPkt64,
       "mpCbQosSetPrecedencePkt64": mpCbQosSetPrecedencePkt64,
       "mpCbQosSetQosGroupPkt64": mpCbQosSetQosGroupPkt64,
       "mpCbQosSetFrDePkt64": mpCbQosSetFrDePkt64,
       "mpCbQosSetAtmClpPkt64": mpCbQosSetAtmClpPkt64,
       "mpCbQosSetL2CosPkt64": mpCbQosSetL2CosPkt64,
       "mpCbQosSetMplsExpImpositionPkt64": mpCbQosSetMplsExpImpositionPkt64,
       "mpCbQosSetDiscardClassPkt64": mpCbQosSetDiscardClassPkt64,
       "mpCbQosSetMplsExpTopMostPkt64": mpCbQosSetMplsExpTopMostPkt64,
       "mpCbQosSetFrFecnBecnPkt64": mpCbQosSetFrFecnBecnPkt64,
       "mpCbQosSetDscpTunnelPkt64": mpCbQosSetDscpTunnelPkt64,
       "mpCbQosSetPrecedenceTunnelPkt64": mpCbQosSetPrecedenceTunnelPkt64,
       "mpCbQosSetTosPkt64": mpCbQosSetTosPkt64}
)
