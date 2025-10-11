# SNMP MIB module (IPSEC-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/IPSEC-POLICY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:22:33 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(IkeAuthMethod,
 IkeEncryptionAlgorithm,
 IkeGroupDescription,
 IkeHashAlgorithm,
 IpsecDoiAuthAlgorithm,
 IpsecDoiEncapsulationMode,
 IpsecDoiEspTransform,
 IpsecDoiIdentType,
 IpsecDoiIpcompTransform,
 IpsecDoiSecProtocolId) = mibBuilder.importSymbols(
    "IPSEC-ISAKMP-IKE-DOI-TC",
    "IkeAuthMethod",
    "IkeEncryptionAlgorithm",
    "IkeGroupDescription",
    "IkeHashAlgorithm",
    "IpsecDoiAuthAlgorithm",
    "IpsecDoiEncapsulationMode",
    "IpsecDoiEspTransform",
    "IpsecDoiIdentType",
    "IpsecDoiIpcompTransform",
    "IpsecDoiSecProtocolId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 experimental,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ipspMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 153)
)
if mibBuilder.loadTexts:
    ipspMIB.setRevisions(
        ("2003-01-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IpspBooleanOperator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("or", 1),
          ("and", 2))
    )



class IpspAdminStatus(TextualConvention, Integer32):
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



class IpspSADirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outgoing", 1),
          ("incoming", 2))
    )



class IpspIPPacketLogging(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65536),
    )



class IpspIdentityFilter(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )



class IpspCredentialType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("unknown", 1),
          ("sharedSecret", 2),
          ("x509", 3),
          ("kerberos", 4))
    )



# MIB Managed Objects in the order of their OIDs

_IpspConfigObjects_ObjectIdentity = ObjectIdentity
ipspConfigObjects = _IpspConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1)
)
_IpspLocalConfigObjects_ObjectIdentity = ObjectIdentity
ipspLocalConfigObjects = _IpspLocalConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1, 1)
)


class _IpspSystemPolicyGroupName_Type(SnmpAdminString):
    """Custom type ipspSystemPolicyGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspSystemPolicyGroupName_Type.__name__ = "SnmpAdminString"
_IpspSystemPolicyGroupName_Object = MibScalar
ipspSystemPolicyGroupName = _IpspSystemPolicyGroupName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 1, 1),
    _IpspSystemPolicyGroupName_Type()
)
ipspSystemPolicyGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipspSystemPolicyGroupName.setStatus("current")
_IpspEndpointToGroupTable_Object = MibTable
ipspEndpointToGroupTable = _IpspEndpointToGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2)
)
if mibBuilder.loadTexts:
    ipspEndpointToGroupTable.setStatus("current")
_IpspEndpointToGroupEntry_Object = MibTableRow
ipspEndpointToGroupEntry = _IpspEndpointToGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1)
)
ipspEndpointToGroupEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspEndGroupIdentType"),
    (0, "IPSEC-POLICY-MIB", "ipspEndGroupAddress"),
)
if mibBuilder.loadTexts:
    ipspEndpointToGroupEntry.setStatus("current")
_IpspEndGroupIdentType_Type = InetAddressType
_IpspEndGroupIdentType_Object = MibTableColumn
ipspEndGroupIdentType = _IpspEndGroupIdentType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 1),
    _IpspEndGroupIdentType_Type()
)
ipspEndGroupIdentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspEndGroupIdentType.setStatus("current")


class _IpspEndGroupAddress_Type(InetAddress):
    """Custom type ipspEndGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpspEndGroupAddress_Type.__name__ = "InetAddress"
_IpspEndGroupAddress_Object = MibTableColumn
ipspEndGroupAddress = _IpspEndGroupAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 2),
    _IpspEndGroupAddress_Type()
)
ipspEndGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspEndGroupAddress.setStatus("current")


class _IpspEndGroupName_Type(SnmpAdminString):
    """Custom type ipspEndGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspEndGroupName_Type.__name__ = "SnmpAdminString"
_IpspEndGroupName_Object = MibTableColumn
ipspEndGroupName = _IpspEndGroupName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 3),
    _IpspEndGroupName_Type()
)
ipspEndGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEndGroupName.setStatus("current")
_IpspEndGroupLastChanged_Type = TimeStamp
_IpspEndGroupLastChanged_Object = MibTableColumn
ipspEndGroupLastChanged = _IpspEndGroupLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 4),
    _IpspEndGroupLastChanged_Type()
)
ipspEndGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspEndGroupLastChanged.setStatus("current")


class _IpspEndGroupStorageType_Type(StorageType):
    """Custom type ipspEndGroupStorageType based on StorageType"""
    defaultValue = 3


_IpspEndGroupStorageType_Type.__name__ = "StorageType"
_IpspEndGroupStorageType_Object = MibTableColumn
ipspEndGroupStorageType = _IpspEndGroupStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 5),
    _IpspEndGroupStorageType_Type()
)
ipspEndGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEndGroupStorageType.setStatus("current")
_IpspEndGroupRowStatus_Type = RowStatus
_IpspEndGroupRowStatus_Object = MibTableColumn
ipspEndGroupRowStatus = _IpspEndGroupRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 2, 1, 6),
    _IpspEndGroupRowStatus_Type()
)
ipspEndGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEndGroupRowStatus.setStatus("current")
_IpspGroupContentsTable_Object = MibTable
ipspGroupContentsTable = _IpspGroupContentsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3)
)
if mibBuilder.loadTexts:
    ipspGroupContentsTable.setStatus("current")
_IpspGroupContentsEntry_Object = MibTableRow
ipspGroupContentsEntry = _IpspGroupContentsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1)
)
ipspGroupContentsEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspGroupContName"),
    (0, "IPSEC-POLICY-MIB", "ipspGroupContPriority"),
)
if mibBuilder.loadTexts:
    ipspGroupContentsEntry.setStatus("current")


class _IpspGroupContName_Type(SnmpAdminString):
    """Custom type ipspGroupContName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspGroupContName_Type.__name__ = "SnmpAdminString"
_IpspGroupContName_Object = MibTableColumn
ipspGroupContName = _IpspGroupContName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 1),
    _IpspGroupContName_Type()
)
ipspGroupContName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspGroupContName.setStatus("current")


class _IpspGroupContPriority_Type(Integer32):
    """Custom type ipspGroupContPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpspGroupContPriority_Type.__name__ = "Integer32"
_IpspGroupContPriority_Object = MibTableColumn
ipspGroupContPriority = _IpspGroupContPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 2),
    _IpspGroupContPriority_Type()
)
ipspGroupContPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspGroupContPriority.setStatus("current")


class _IpspGroupContFilter_Type(VariablePointer):
    """Custom type ipspGroupContFilter based on VariablePointer"""
    defaultValue = (1, 3, 6, 1, 2, 1, 153, 1, 7, 1, 0)


_IpspGroupContFilter_Type.__name__ = "VariablePointer"
_IpspGroupContFilter_Object = MibTableColumn
ipspGroupContFilter = _IpspGroupContFilter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 3),
    _IpspGroupContFilter_Type()
)
ipspGroupContFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspGroupContFilter.setStatus("current")


class _IpspGroupContComponentType_Type(Integer32):
    """Custom type ipspGroupContComponentType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("group", 1),
          ("rule", 2))
    )


_IpspGroupContComponentType_Type.__name__ = "Integer32"
_IpspGroupContComponentType_Object = MibTableColumn
ipspGroupContComponentType = _IpspGroupContComponentType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 4),
    _IpspGroupContComponentType_Type()
)
ipspGroupContComponentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspGroupContComponentType.setStatus("current")


class _IpspGroupContComponentName_Type(SnmpAdminString):
    """Custom type ipspGroupContComponentName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspGroupContComponentName_Type.__name__ = "SnmpAdminString"
_IpspGroupContComponentName_Object = MibTableColumn
ipspGroupContComponentName = _IpspGroupContComponentName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 5),
    _IpspGroupContComponentName_Type()
)
ipspGroupContComponentName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspGroupContComponentName.setStatus("current")
_IpspGroupContLastChanged_Type = TimeStamp
_IpspGroupContLastChanged_Object = MibTableColumn
ipspGroupContLastChanged = _IpspGroupContLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 6),
    _IpspGroupContLastChanged_Type()
)
ipspGroupContLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspGroupContLastChanged.setStatus("current")


class _IpspGroupContStorageType_Type(StorageType):
    """Custom type ipspGroupContStorageType based on StorageType"""
    defaultValue = 3


_IpspGroupContStorageType_Type.__name__ = "StorageType"
_IpspGroupContStorageType_Object = MibTableColumn
ipspGroupContStorageType = _IpspGroupContStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 7),
    _IpspGroupContStorageType_Type()
)
ipspGroupContStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspGroupContStorageType.setStatus("current")
_IpspGroupContRowStatus_Type = RowStatus
_IpspGroupContRowStatus_Object = MibTableColumn
ipspGroupContRowStatus = _IpspGroupContRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 3, 1, 8),
    _IpspGroupContRowStatus_Type()
)
ipspGroupContRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspGroupContRowStatus.setStatus("current")
_IpspRuleDefinitionTable_Object = MibTable
ipspRuleDefinitionTable = _IpspRuleDefinitionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4)
)
if mibBuilder.loadTexts:
    ipspRuleDefinitionTable.setStatus("current")
_IpspRuleDefinitionEntry_Object = MibTableRow
ipspRuleDefinitionEntry = _IpspRuleDefinitionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1)
)
ipspRuleDefinitionEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspRuleDefName"),
)
if mibBuilder.loadTexts:
    ipspRuleDefinitionEntry.setStatus("current")


class _IpspRuleDefName_Type(SnmpAdminString):
    """Custom type ipspRuleDefName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspRuleDefName_Type.__name__ = "SnmpAdminString"
_IpspRuleDefName_Object = MibTableColumn
ipspRuleDefName = _IpspRuleDefName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 1),
    _IpspRuleDefName_Type()
)
ipspRuleDefName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspRuleDefName.setStatus("current")


class _IpspRuleDefDescription_Type(SnmpAdminString):
    """Custom type ipspRuleDefDescription based on SnmpAdminString"""
    defaultValue = OctetString("")


_IpspRuleDefDescription_Type.__name__ = "SnmpAdminString"
_IpspRuleDefDescription_Object = MibTableColumn
ipspRuleDefDescription = _IpspRuleDefDescription_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 2),
    _IpspRuleDefDescription_Type()
)
ipspRuleDefDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRuleDefDescription.setStatus("current")
_IpspRuleDefFilter_Type = VariablePointer
_IpspRuleDefFilter_Object = MibTableColumn
ipspRuleDefFilter = _IpspRuleDefFilter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 3),
    _IpspRuleDefFilter_Type()
)
ipspRuleDefFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRuleDefFilter.setStatus("current")


class _IpspRuleDefFilterNegated_Type(TruthValue):
    """Custom type ipspRuleDefFilterNegated based on TruthValue"""
    defaultValue = 2


_IpspRuleDefFilterNegated_Type.__name__ = "TruthValue"
_IpspRuleDefFilterNegated_Object = MibTableColumn
ipspRuleDefFilterNegated = _IpspRuleDefFilterNegated_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 4),
    _IpspRuleDefFilterNegated_Type()
)
ipspRuleDefFilterNegated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRuleDefFilterNegated.setStatus("current")
_IpspRuleDefAction_Type = VariablePointer
_IpspRuleDefAction_Object = MibTableColumn
ipspRuleDefAction = _IpspRuleDefAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 5),
    _IpspRuleDefAction_Type()
)
ipspRuleDefAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRuleDefAction.setStatus("current")


class _IpspRuleDefAdminStatus_Type(IpspAdminStatus):
    """Custom type ipspRuleDefAdminStatus based on IpspAdminStatus"""
    defaultValue = 1


_IpspRuleDefAdminStatus_Type.__name__ = "IpspAdminStatus"
_IpspRuleDefAdminStatus_Object = MibTableColumn
ipspRuleDefAdminStatus = _IpspRuleDefAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 6),
    _IpspRuleDefAdminStatus_Type()
)
ipspRuleDefAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRuleDefAdminStatus.setStatus("current")
_IpspRuleDefLastChanged_Type = TimeStamp
_IpspRuleDefLastChanged_Object = MibTableColumn
ipspRuleDefLastChanged = _IpspRuleDefLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 7),
    _IpspRuleDefLastChanged_Type()
)
ipspRuleDefLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspRuleDefLastChanged.setStatus("current")


class _IpspRuleDefStorageType_Type(StorageType):
    """Custom type ipspRuleDefStorageType based on StorageType"""
    defaultValue = 3


_IpspRuleDefStorageType_Type.__name__ = "StorageType"
_IpspRuleDefStorageType_Object = MibTableColumn
ipspRuleDefStorageType = _IpspRuleDefStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 8),
    _IpspRuleDefStorageType_Type()
)
ipspRuleDefStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRuleDefStorageType.setStatus("current")
_IpspRuleDefRowStatus_Type = RowStatus
_IpspRuleDefRowStatus_Object = MibTableColumn
ipspRuleDefRowStatus = _IpspRuleDefRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 4, 1, 9),
    _IpspRuleDefRowStatus_Type()
)
ipspRuleDefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRuleDefRowStatus.setStatus("current")
_IpspCompoundFilterTable_Object = MibTable
ipspCompoundFilterTable = _IpspCompoundFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5)
)
if mibBuilder.loadTexts:
    ipspCompoundFilterTable.setStatus("current")
_IpspCompoundFilterEntry_Object = MibTableRow
ipspCompoundFilterEntry = _IpspCompoundFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1)
)
ipspCompoundFilterEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspCompFiltName"),
)
if mibBuilder.loadTexts:
    ipspCompoundFilterEntry.setStatus("current")


class _IpspCompFiltName_Type(SnmpAdminString):
    """Custom type ipspCompFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspCompFiltName_Type.__name__ = "SnmpAdminString"
_IpspCompFiltName_Object = MibTableColumn
ipspCompFiltName = _IpspCompFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 1),
    _IpspCompFiltName_Type()
)
ipspCompFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspCompFiltName.setStatus("current")


class _IpspCompFiltDescription_Type(SnmpAdminString):
    """Custom type ipspCompFiltDescription based on SnmpAdminString"""
    defaultHexValue = ""


_IpspCompFiltDescription_Type.__name__ = "SnmpAdminString"
_IpspCompFiltDescription_Object = MibTableColumn
ipspCompFiltDescription = _IpspCompFiltDescription_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 2),
    _IpspCompFiltDescription_Type()
)
ipspCompFiltDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCompFiltDescription.setStatus("current")


class _IpspCompFiltLogicType_Type(IpspBooleanOperator):
    """Custom type ipspCompFiltLogicType based on IpspBooleanOperator"""
    defaultValue = 2


_IpspCompFiltLogicType_Type.__name__ = "IpspBooleanOperator"
_IpspCompFiltLogicType_Object = MibTableColumn
ipspCompFiltLogicType = _IpspCompFiltLogicType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 3),
    _IpspCompFiltLogicType_Type()
)
ipspCompFiltLogicType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCompFiltLogicType.setStatus("current")
_IpspCompFiltLastChanged_Type = TimeStamp
_IpspCompFiltLastChanged_Object = MibTableColumn
ipspCompFiltLastChanged = _IpspCompFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 4),
    _IpspCompFiltLastChanged_Type()
)
ipspCompFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspCompFiltLastChanged.setStatus("current")


class _IpspCompFiltStorageType_Type(StorageType):
    """Custom type ipspCompFiltStorageType based on StorageType"""
    defaultValue = 3


_IpspCompFiltStorageType_Type.__name__ = "StorageType"
_IpspCompFiltStorageType_Object = MibTableColumn
ipspCompFiltStorageType = _IpspCompFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 5),
    _IpspCompFiltStorageType_Type()
)
ipspCompFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCompFiltStorageType.setStatus("current")
_IpspCompFiltRowStatus_Type = RowStatus
_IpspCompFiltRowStatus_Object = MibTableColumn
ipspCompFiltRowStatus = _IpspCompFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 5, 1, 6),
    _IpspCompFiltRowStatus_Type()
)
ipspCompFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCompFiltRowStatus.setStatus("current")
_IpspSubfiltersTable_Object = MibTable
ipspSubfiltersTable = _IpspSubfiltersTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6)
)
if mibBuilder.loadTexts:
    ipspSubfiltersTable.setStatus("current")
_IpspSubfiltersEntry_Object = MibTableRow
ipspSubfiltersEntry = _IpspSubfiltersEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1)
)
ipspSubfiltersEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspCompFiltName"),
    (0, "IPSEC-POLICY-MIB", "ipspSubFiltPriority"),
)
if mibBuilder.loadTexts:
    ipspSubfiltersEntry.setStatus("current")


class _IpspSubFiltPriority_Type(Integer32):
    """Custom type ipspSubFiltPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpspSubFiltPriority_Type.__name__ = "Integer32"
_IpspSubFiltPriority_Object = MibTableColumn
ipspSubFiltPriority = _IpspSubFiltPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 1),
    _IpspSubFiltPriority_Type()
)
ipspSubFiltPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspSubFiltPriority.setStatus("current")
_IpspSubFiltSubfilter_Type = VariablePointer
_IpspSubFiltSubfilter_Object = MibTableColumn
ipspSubFiltSubfilter = _IpspSubFiltSubfilter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 2),
    _IpspSubFiltSubfilter_Type()
)
ipspSubFiltSubfilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSubFiltSubfilter.setStatus("current")


class _IpspSubFiltSubfilterIsNegated_Type(TruthValue):
    """Custom type ipspSubFiltSubfilterIsNegated based on TruthValue"""
    defaultValue = 2


_IpspSubFiltSubfilterIsNegated_Type.__name__ = "TruthValue"
_IpspSubFiltSubfilterIsNegated_Object = MibTableColumn
ipspSubFiltSubfilterIsNegated = _IpspSubFiltSubfilterIsNegated_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 3),
    _IpspSubFiltSubfilterIsNegated_Type()
)
ipspSubFiltSubfilterIsNegated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSubFiltSubfilterIsNegated.setStatus("current")
_IpspSubFiltLastChanged_Type = TimeStamp
_IpspSubFiltLastChanged_Object = MibTableColumn
ipspSubFiltLastChanged = _IpspSubFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 4),
    _IpspSubFiltLastChanged_Type()
)
ipspSubFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspSubFiltLastChanged.setStatus("current")


class _IpspSubFiltStorageType_Type(StorageType):
    """Custom type ipspSubFiltStorageType based on StorageType"""
    defaultValue = 3


_IpspSubFiltStorageType_Type.__name__ = "StorageType"
_IpspSubFiltStorageType_Object = MibTableColumn
ipspSubFiltStorageType = _IpspSubFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 5),
    _IpspSubFiltStorageType_Type()
)
ipspSubFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSubFiltStorageType.setStatus("current")
_IpspSubFiltRowStatus_Type = RowStatus
_IpspSubFiltRowStatus_Object = MibTableColumn
ipspSubFiltRowStatus = _IpspSubFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 6, 1, 6),
    _IpspSubFiltRowStatus_Type()
)
ipspSubFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSubFiltRowStatus.setStatus("current")
_IpspStaticFilters_ObjectIdentity = ObjectIdentity
ipspStaticFilters = _IpspStaticFilters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1, 7)
)
_IpspTrueFilter_Type = Integer32
_IpspTrueFilter_Object = MibScalar
ipspTrueFilter = _IpspTrueFilter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 7, 1),
    _IpspTrueFilter_Type()
)
ipspTrueFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspTrueFilter.setStatus("current")
_IpspTrueFilterInstance_ObjectIdentity = ObjectIdentity
ipspTrueFilterInstance = _IpspTrueFilterInstance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1, 7, 1, 0)
)
_IpspIkePhase1Filter_Type = Integer32
_IpspIkePhase1Filter_Object = MibScalar
ipspIkePhase1Filter = _IpspIkePhase1Filter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 7, 2),
    _IpspIkePhase1Filter_Type()
)
ipspIkePhase1Filter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIkePhase1Filter.setStatus("current")
_IpspIkePhase2Filter_Type = Integer32
_IpspIkePhase2Filter_Object = MibScalar
ipspIkePhase2Filter = _IpspIkePhase2Filter_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 7, 3),
    _IpspIkePhase2Filter_Type()
)
ipspIkePhase2Filter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIkePhase2Filter.setStatus("current")
_IpspIpHeaderFilterTable_Object = MibTable
ipspIpHeaderFilterTable = _IpspIpHeaderFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8)
)
if mibBuilder.loadTexts:
    ipspIpHeaderFilterTable.setStatus("current")
_IpspIpHeaderFilterEntry_Object = MibTableRow
ipspIpHeaderFilterEntry = _IpspIpHeaderFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1)
)
ipspIpHeaderFilterEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIpHeadFiltName"),
)
if mibBuilder.loadTexts:
    ipspIpHeaderFilterEntry.setStatus("current")


class _IpspIpHeadFiltName_Type(SnmpAdminString):
    """Custom type ipspIpHeadFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpHeadFiltName_Type.__name__ = "SnmpAdminString"
_IpspIpHeadFiltName_Object = MibTableColumn
ipspIpHeadFiltName = _IpspIpHeadFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 1),
    _IpspIpHeadFiltName_Type()
)
ipspIpHeadFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpHeadFiltName.setStatus("current")


class _IpspIpHeadFiltType_Type(Bits):
    """Custom type ipspIpHeadFiltType based on Bits"""
    namedValues = NamedValues(
        *(("sourceAddress", 0),
          ("destinationAddress", 1),
          ("sourcePort", 2),
          ("destinationPort", 3),
          ("protocol", 4),
          ("ipv6FlowLabel", 5))
    )

_IpspIpHeadFiltType_Type.__name__ = "Bits"
_IpspIpHeadFiltType_Object = MibTableColumn
ipspIpHeadFiltType = _IpspIpHeadFiltType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 2),
    _IpspIpHeadFiltType_Type()
)
ipspIpHeadFiltType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltType.setStatus("current")


class _IpspIpHeadFiltIPVersion_Type(InetAddressType):
    """Custom type ipspIpHeadFiltIPVersion based on InetAddressType"""
    defaultValue = 2


_IpspIpHeadFiltIPVersion_Type.__name__ = "InetAddressType"
_IpspIpHeadFiltIPVersion_Object = MibTableColumn
ipspIpHeadFiltIPVersion = _IpspIpHeadFiltIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 3),
    _IpspIpHeadFiltIPVersion_Type()
)
ipspIpHeadFiltIPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltIPVersion.setStatus("current")
_IpspIpHeadFiltSrcAddressBegin_Type = InetAddress
_IpspIpHeadFiltSrcAddressBegin_Object = MibTableColumn
ipspIpHeadFiltSrcAddressBegin = _IpspIpHeadFiltSrcAddressBegin_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 4),
    _IpspIpHeadFiltSrcAddressBegin_Type()
)
ipspIpHeadFiltSrcAddressBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltSrcAddressBegin.setStatus("current")
_IpspIpHeadFiltSrcAddressEnd_Type = InetAddress
_IpspIpHeadFiltSrcAddressEnd_Object = MibTableColumn
ipspIpHeadFiltSrcAddressEnd = _IpspIpHeadFiltSrcAddressEnd_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 5),
    _IpspIpHeadFiltSrcAddressEnd_Type()
)
ipspIpHeadFiltSrcAddressEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltSrcAddressEnd.setStatus("current")
_IpspIpHeadFiltDstAddressBegin_Type = InetAddress
_IpspIpHeadFiltDstAddressBegin_Object = MibTableColumn
ipspIpHeadFiltDstAddressBegin = _IpspIpHeadFiltDstAddressBegin_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 6),
    _IpspIpHeadFiltDstAddressBegin_Type()
)
ipspIpHeadFiltDstAddressBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltDstAddressBegin.setStatus("current")
_IpspIpHeadFiltDstAddressEnd_Type = InetAddress
_IpspIpHeadFiltDstAddressEnd_Object = MibTableColumn
ipspIpHeadFiltDstAddressEnd = _IpspIpHeadFiltDstAddressEnd_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 7),
    _IpspIpHeadFiltDstAddressEnd_Type()
)
ipspIpHeadFiltDstAddressEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltDstAddressEnd.setStatus("current")
_IpspIpHeadFiltSrcLowPort_Type = InetPortNumber
_IpspIpHeadFiltSrcLowPort_Object = MibTableColumn
ipspIpHeadFiltSrcLowPort = _IpspIpHeadFiltSrcLowPort_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 8),
    _IpspIpHeadFiltSrcLowPort_Type()
)
ipspIpHeadFiltSrcLowPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltSrcLowPort.setStatus("current")
_IpspIpHeadFiltSrcHighPort_Type = InetPortNumber
_IpspIpHeadFiltSrcHighPort_Object = MibTableColumn
ipspIpHeadFiltSrcHighPort = _IpspIpHeadFiltSrcHighPort_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 9),
    _IpspIpHeadFiltSrcHighPort_Type()
)
ipspIpHeadFiltSrcHighPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltSrcHighPort.setStatus("current")
_IpspIpHeadFiltDstLowPort_Type = InetPortNumber
_IpspIpHeadFiltDstLowPort_Object = MibTableColumn
ipspIpHeadFiltDstLowPort = _IpspIpHeadFiltDstLowPort_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 10),
    _IpspIpHeadFiltDstLowPort_Type()
)
ipspIpHeadFiltDstLowPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltDstLowPort.setStatus("current")
_IpspIpHeadFiltDstHighPort_Type = InetPortNumber
_IpspIpHeadFiltDstHighPort_Object = MibTableColumn
ipspIpHeadFiltDstHighPort = _IpspIpHeadFiltDstHighPort_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 11),
    _IpspIpHeadFiltDstHighPort_Type()
)
ipspIpHeadFiltDstHighPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltDstHighPort.setStatus("current")


class _IpspIpHeadFiltProtocol_Type(Integer32):
    """Custom type ipspIpHeadFiltProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpspIpHeadFiltProtocol_Type.__name__ = "Integer32"
_IpspIpHeadFiltProtocol_Object = MibTableColumn
ipspIpHeadFiltProtocol = _IpspIpHeadFiltProtocol_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 12),
    _IpspIpHeadFiltProtocol_Type()
)
ipspIpHeadFiltProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltProtocol.setStatus("current")


class _IpspIpHeadFiltIPv6FlowLabel_Type(Integer32):
    """Custom type ipspIpHeadFiltIPv6FlowLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_IpspIpHeadFiltIPv6FlowLabel_Type.__name__ = "Integer32"
_IpspIpHeadFiltIPv6FlowLabel_Object = MibTableColumn
ipspIpHeadFiltIPv6FlowLabel = _IpspIpHeadFiltIPv6FlowLabel_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 13),
    _IpspIpHeadFiltIPv6FlowLabel_Type()
)
ipspIpHeadFiltIPv6FlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltIPv6FlowLabel.setStatus("current")
_IpspIpHeadFiltLastChanged_Type = TimeStamp
_IpspIpHeadFiltLastChanged_Object = MibTableColumn
ipspIpHeadFiltLastChanged = _IpspIpHeadFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 14),
    _IpspIpHeadFiltLastChanged_Type()
)
ipspIpHeadFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIpHeadFiltLastChanged.setStatus("current")


class _IpspIpHeadFiltStorageType_Type(StorageType):
    """Custom type ipspIpHeadFiltStorageType based on StorageType"""
    defaultValue = 3


_IpspIpHeadFiltStorageType_Type.__name__ = "StorageType"
_IpspIpHeadFiltStorageType_Object = MibTableColumn
ipspIpHeadFiltStorageType = _IpspIpHeadFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 15),
    _IpspIpHeadFiltStorageType_Type()
)
ipspIpHeadFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltStorageType.setStatus("current")
_IpspIpHeadFiltRowStatus_Type = RowStatus
_IpspIpHeadFiltRowStatus_Object = MibTableColumn
ipspIpHeadFiltRowStatus = _IpspIpHeadFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 8, 1, 16),
    _IpspIpHeadFiltRowStatus_Type()
)
ipspIpHeadFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpHeadFiltRowStatus.setStatus("current")
_IpspIpOffsetFilterTable_Object = MibTable
ipspIpOffsetFilterTable = _IpspIpOffsetFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9)
)
if mibBuilder.loadTexts:
    ipspIpOffsetFilterTable.setStatus("current")
_IpspIpOffsetFilterEntry_Object = MibTableRow
ipspIpOffsetFilterEntry = _IpspIpOffsetFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1)
)
ipspIpOffsetFilterEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIpOffFiltName"),
)
if mibBuilder.loadTexts:
    ipspIpOffsetFilterEntry.setStatus("current")


class _IpspIpOffFiltName_Type(SnmpAdminString):
    """Custom type ipspIpOffFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpOffFiltName_Type.__name__ = "SnmpAdminString"
_IpspIpOffFiltName_Object = MibTableColumn
ipspIpOffFiltName = _IpspIpOffFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 1),
    _IpspIpOffFiltName_Type()
)
ipspIpOffFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpOffFiltName.setStatus("current")


class _IpspIpOffFiltOffset_Type(Integer32):
    """Custom type ipspIpOffFiltOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpspIpOffFiltOffset_Type.__name__ = "Integer32"
_IpspIpOffFiltOffset_Object = MibTableColumn
ipspIpOffFiltOffset = _IpspIpOffFiltOffset_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 2),
    _IpspIpOffFiltOffset_Type()
)
ipspIpOffFiltOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpOffFiltOffset.setStatus("current")


class _IpspIpOffFiltType_Type(Integer32):
    """Custom type ipspIpOffFiltType based on Integer32"""
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
        *(("valueMatch", 1),
          ("valueNotMatch", 2),
          ("arithmeticEqual", 3),
          ("arithmeticNotEqual", 4),
          ("arithmeticLess", 5),
          ("arithmeticGreaterOrEqual", 6),
          ("arithmeticGreater", 7),
          ("arithmeticLessOrEqual", 8))
    )


_IpspIpOffFiltType_Type.__name__ = "Integer32"
_IpspIpOffFiltType_Object = MibTableColumn
ipspIpOffFiltType = _IpspIpOffFiltType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 3),
    _IpspIpOffFiltType_Type()
)
ipspIpOffFiltType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpOffFiltType.setStatus("current")


class _IpspIpOffFiltNumber_Type(Integer32):
    """Custom type ipspIpOffFiltNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpspIpOffFiltNumber_Type.__name__ = "Integer32"
_IpspIpOffFiltNumber_Object = MibTableColumn
ipspIpOffFiltNumber = _IpspIpOffFiltNumber_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 4),
    _IpspIpOffFiltNumber_Type()
)
ipspIpOffFiltNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpOffFiltNumber.setStatus("current")


class _IpspIpOffFiltValue_Type(OctetString):
    """Custom type ipspIpOffFiltValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_IpspIpOffFiltValue_Type.__name__ = "OctetString"
_IpspIpOffFiltValue_Object = MibTableColumn
ipspIpOffFiltValue = _IpspIpOffFiltValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 5),
    _IpspIpOffFiltValue_Type()
)
ipspIpOffFiltValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpOffFiltValue.setStatus("current")
_IpspIpOffFiltLastChanged_Type = TimeStamp
_IpspIpOffFiltLastChanged_Object = MibTableColumn
ipspIpOffFiltLastChanged = _IpspIpOffFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 6),
    _IpspIpOffFiltLastChanged_Type()
)
ipspIpOffFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIpOffFiltLastChanged.setStatus("current")


class _IpspIpOffFiltStorageType_Type(StorageType):
    """Custom type ipspIpOffFiltStorageType based on StorageType"""
    defaultValue = 3


_IpspIpOffFiltStorageType_Type.__name__ = "StorageType"
_IpspIpOffFiltStorageType_Object = MibTableColumn
ipspIpOffFiltStorageType = _IpspIpOffFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 7),
    _IpspIpOffFiltStorageType_Type()
)
ipspIpOffFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpOffFiltStorageType.setStatus("current")
_IpspIpOffFiltRowStatus_Type = RowStatus
_IpspIpOffFiltRowStatus_Object = MibTableColumn
ipspIpOffFiltRowStatus = _IpspIpOffFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 9, 1, 8),
    _IpspIpOffFiltRowStatus_Type()
)
ipspIpOffFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpOffFiltRowStatus.setStatus("current")
_IpspTimeFilterTable_Object = MibTable
ipspTimeFilterTable = _IpspTimeFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10)
)
if mibBuilder.loadTexts:
    ipspTimeFilterTable.setStatus("current")
_IpspTimeFilterEntry_Object = MibTableRow
ipspTimeFilterEntry = _IpspTimeFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1)
)
ipspTimeFilterEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspTimeFiltName"),
)
if mibBuilder.loadTexts:
    ipspTimeFilterEntry.setStatus("current")


class _IpspTimeFiltName_Type(SnmpAdminString):
    """Custom type ipspTimeFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspTimeFiltName_Type.__name__ = "SnmpAdminString"
_IpspTimeFiltName_Object = MibTableColumn
ipspTimeFiltName = _IpspTimeFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 1),
    _IpspTimeFiltName_Type()
)
ipspTimeFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspTimeFiltName.setStatus("current")


class _IpspTimeFiltPeriodStart_Type(DateAndTime):
    """Custom type ipspTimeFiltPeriodStart based on DateAndTime"""
    defaultHexValue = "00000101000000002b0000"


_IpspTimeFiltPeriodStart_Type.__name__ = "DateAndTime"
_IpspTimeFiltPeriodStart_Object = MibTableColumn
ipspTimeFiltPeriodStart = _IpspTimeFiltPeriodStart_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 2),
    _IpspTimeFiltPeriodStart_Type()
)
ipspTimeFiltPeriodStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspTimeFiltPeriodStart.setStatus("current")


class _IpspTimeFiltPeriodEnd_Type(DateAndTime):
    """Custom type ipspTimeFiltPeriodEnd based on DateAndTime"""
    defaultHexValue = "99991231235959092b0000"


_IpspTimeFiltPeriodEnd_Type.__name__ = "DateAndTime"
_IpspTimeFiltPeriodEnd_Object = MibTableColumn
ipspTimeFiltPeriodEnd = _IpspTimeFiltPeriodEnd_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 3),
    _IpspTimeFiltPeriodEnd_Type()
)
ipspTimeFiltPeriodEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspTimeFiltPeriodEnd.setStatus("current")


class _IpspTimeFiltMonthOfYearMask_Type(Bits):
    """Custom type ipspTimeFiltMonthOfYearMask based on Bits"""
    defaultBinValue = "111111111111"

    namedValues = NamedValues(
        *(("january", 0),
          ("february", 1),
          ("march", 2),
          ("april", 3),
          ("may", 4),
          ("june", 5),
          ("july", 6),
          ("august", 7),
          ("september", 8),
          ("october", 9),
          ("november", 10),
          ("december", 11))
    )

_IpspTimeFiltMonthOfYearMask_Type.__name__ = "Bits"
_IpspTimeFiltMonthOfYearMask_Object = MibTableColumn
ipspTimeFiltMonthOfYearMask = _IpspTimeFiltMonthOfYearMask_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 4),
    _IpspTimeFiltMonthOfYearMask_Type()
)
ipspTimeFiltMonthOfYearMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspTimeFiltMonthOfYearMask.setStatus("current")


class _IpspTimeFiltDayOfMonthMask_Type(OctetString):
    """Custom type ipspTimeFiltDayOfMonthMask based on OctetString"""
    defaultHexValue = "fffffffe"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_IpspTimeFiltDayOfMonthMask_Type.__name__ = "OctetString"
_IpspTimeFiltDayOfMonthMask_Object = MibTableColumn
ipspTimeFiltDayOfMonthMask = _IpspTimeFiltDayOfMonthMask_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 5),
    _IpspTimeFiltDayOfMonthMask_Type()
)
ipspTimeFiltDayOfMonthMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspTimeFiltDayOfMonthMask.setStatus("current")


class _IpspTimeFiltDayOfWeekMask_Type(Bits):
    """Custom type ipspTimeFiltDayOfWeekMask based on Bits"""
    defaultBinValue = "1111111"

    namedValues = NamedValues(
        *(("monday", 0),
          ("tuesday", 1),
          ("wednesday", 2),
          ("thursday", 3),
          ("friday", 4),
          ("saturday", 5),
          ("sunday", 6))
    )

_IpspTimeFiltDayOfWeekMask_Type.__name__ = "Bits"
_IpspTimeFiltDayOfWeekMask_Object = MibTableColumn
ipspTimeFiltDayOfWeekMask = _IpspTimeFiltDayOfWeekMask_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 6),
    _IpspTimeFiltDayOfWeekMask_Type()
)
ipspTimeFiltDayOfWeekMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspTimeFiltDayOfWeekMask.setStatus("current")


class _IpspTimeFiltTimeOfDayMaskStart_Type(DateAndTime):
    """Custom type ipspTimeFiltTimeOfDayMaskStart based on DateAndTime"""
    defaultHexValue = "00000000000000002b0000"


_IpspTimeFiltTimeOfDayMaskStart_Type.__name__ = "DateAndTime"
_IpspTimeFiltTimeOfDayMaskStart_Object = MibTableColumn
ipspTimeFiltTimeOfDayMaskStart = _IpspTimeFiltTimeOfDayMaskStart_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 7),
    _IpspTimeFiltTimeOfDayMaskStart_Type()
)
ipspTimeFiltTimeOfDayMaskStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspTimeFiltTimeOfDayMaskStart.setStatus("current")


class _IpspTimeFiltTimeOfDayMaskEnd_Type(DateAndTime):
    """Custom type ipspTimeFiltTimeOfDayMaskEnd based on DateAndTime"""
    defaultHexValue = "00000000000000002b0000"


_IpspTimeFiltTimeOfDayMaskEnd_Type.__name__ = "DateAndTime"
_IpspTimeFiltTimeOfDayMaskEnd_Object = MibTableColumn
ipspTimeFiltTimeOfDayMaskEnd = _IpspTimeFiltTimeOfDayMaskEnd_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 8),
    _IpspTimeFiltTimeOfDayMaskEnd_Type()
)
ipspTimeFiltTimeOfDayMaskEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspTimeFiltTimeOfDayMaskEnd.setStatus("current")
_IpspTimeFiltLastChanged_Type = TimeStamp
_IpspTimeFiltLastChanged_Object = MibTableColumn
ipspTimeFiltLastChanged = _IpspTimeFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 9),
    _IpspTimeFiltLastChanged_Type()
)
ipspTimeFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspTimeFiltLastChanged.setStatus("current")


class _IpspTimeFiltStorageType_Type(StorageType):
    """Custom type ipspTimeFiltStorageType based on StorageType"""
    defaultValue = 3


_IpspTimeFiltStorageType_Type.__name__ = "StorageType"
_IpspTimeFiltStorageType_Object = MibTableColumn
ipspTimeFiltStorageType = _IpspTimeFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 10),
    _IpspTimeFiltStorageType_Type()
)
ipspTimeFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspTimeFiltStorageType.setStatus("current")
_IpspTimeFiltRowStatus_Type = RowStatus
_IpspTimeFiltRowStatus_Object = MibTableColumn
ipspTimeFiltRowStatus = _IpspTimeFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 10, 1, 11),
    _IpspTimeFiltRowStatus_Type()
)
ipspTimeFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspTimeFiltRowStatus.setStatus("current")
_IpspIpsoHeaderFilterTable_Object = MibTable
ipspIpsoHeaderFilterTable = _IpspIpsoHeaderFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11)
)
if mibBuilder.loadTexts:
    ipspIpsoHeaderFilterTable.setStatus("current")
_IpspIpsoHeaderFilterEntry_Object = MibTableRow
ipspIpsoHeaderFilterEntry = _IpspIpsoHeaderFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1)
)
ipspIpsoHeaderFilterEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIpsoHeadFiltName"),
)
if mibBuilder.loadTexts:
    ipspIpsoHeaderFilterEntry.setStatus("current")


class _IpspIpsoHeadFiltName_Type(SnmpAdminString):
    """Custom type ipspIpsoHeadFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpsoHeadFiltName_Type.__name__ = "SnmpAdminString"
_IpspIpsoHeadFiltName_Object = MibTableColumn
ipspIpsoHeadFiltName = _IpspIpsoHeadFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 1),
    _IpspIpsoHeadFiltName_Type()
)
ipspIpsoHeadFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpsoHeadFiltName.setStatus("current")


class _IpspIpsoHeadFiltType_Type(Bits):
    """Custom type ipspIpsoHeadFiltType based on Bits"""
    namedValues = NamedValues(
        *(("classificationLevel", 0),
          ("protectionAuthority", 1))
    )

_IpspIpsoHeadFiltType_Type.__name__ = "Bits"
_IpspIpsoHeadFiltType_Object = MibTableColumn
ipspIpsoHeadFiltType = _IpspIpsoHeadFiltType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 2),
    _IpspIpsoHeadFiltType_Type()
)
ipspIpsoHeadFiltType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsoHeadFiltType.setStatus("current")


class _IpspIpsoHeadFiltClassification_Type(Integer32):
    """Custom type ipspIpsoHeadFiltClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("topSecret", 61),
          ("secret", 90),
          ("confidential", 150),
          ("unclassified", 171))
    )


_IpspIpsoHeadFiltClassification_Type.__name__ = "Integer32"
_IpspIpsoHeadFiltClassification_Object = MibTableColumn
ipspIpsoHeadFiltClassification = _IpspIpsoHeadFiltClassification_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 3),
    _IpspIpsoHeadFiltClassification_Type()
)
ipspIpsoHeadFiltClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsoHeadFiltClassification.setStatus("current")


class _IpspIpsoHeadFiltProtectionAuth_Type(Integer32):
    """Custom type ipspIpsoHeadFiltProtectionAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("genser", 0),
          ("siopesi", 1),
          ("sci", 2),
          ("nsa", 3),
          ("doe", 4))
    )


_IpspIpsoHeadFiltProtectionAuth_Type.__name__ = "Integer32"
_IpspIpsoHeadFiltProtectionAuth_Object = MibTableColumn
ipspIpsoHeadFiltProtectionAuth = _IpspIpsoHeadFiltProtectionAuth_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 4),
    _IpspIpsoHeadFiltProtectionAuth_Type()
)
ipspIpsoHeadFiltProtectionAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsoHeadFiltProtectionAuth.setStatus("current")
_IpspIpsoHeadFiltLastChanged_Type = TimeStamp
_IpspIpsoHeadFiltLastChanged_Object = MibTableColumn
ipspIpsoHeadFiltLastChanged = _IpspIpsoHeadFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 5),
    _IpspIpsoHeadFiltLastChanged_Type()
)
ipspIpsoHeadFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIpsoHeadFiltLastChanged.setStatus("current")


class _IpspIpsoHeadFiltStorageType_Type(StorageType):
    """Custom type ipspIpsoHeadFiltStorageType based on StorageType"""
    defaultValue = 3


_IpspIpsoHeadFiltStorageType_Type.__name__ = "StorageType"
_IpspIpsoHeadFiltStorageType_Object = MibTableColumn
ipspIpsoHeadFiltStorageType = _IpspIpsoHeadFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 6),
    _IpspIpsoHeadFiltStorageType_Type()
)
ipspIpsoHeadFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsoHeadFiltStorageType.setStatus("current")
_IpspIpsoHeadFiltRowStatus_Type = RowStatus
_IpspIpsoHeadFiltRowStatus_Object = MibTableColumn
ipspIpsoHeadFiltRowStatus = _IpspIpsoHeadFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 11, 1, 7),
    _IpspIpsoHeadFiltRowStatus_Type()
)
ipspIpsoHeadFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsoHeadFiltRowStatus.setStatus("current")
_IpspCredentialFilterTable_Object = MibTable
ipspCredentialFilterTable = _IpspCredentialFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12)
)
if mibBuilder.loadTexts:
    ipspCredentialFilterTable.setStatus("current")
_IpspCredentialFilterEntry_Object = MibTableRow
ipspCredentialFilterEntry = _IpspCredentialFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1)
)
ipspCredentialFilterEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspCredFiltName"),
)
if mibBuilder.loadTexts:
    ipspCredentialFilterEntry.setStatus("current")


class _IpspCredFiltName_Type(SnmpAdminString):
    """Custom type ipspCredFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspCredFiltName_Type.__name__ = "SnmpAdminString"
_IpspCredFiltName_Object = MibTableColumn
ipspCredFiltName = _IpspCredFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 1),
    _IpspCredFiltName_Type()
)
ipspCredFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspCredFiltName.setStatus("current")


class _IpspCredFiltCredentialType_Type(IpspCredentialType):
    """Custom type ipspCredFiltCredentialType based on IpspCredentialType"""
    defaultValue = 3


_IpspCredFiltCredentialType_Type.__name__ = "IpspCredentialType"
_IpspCredFiltCredentialType_Object = MibTableColumn
ipspCredFiltCredentialType = _IpspCredFiltCredentialType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 2),
    _IpspCredFiltCredentialType_Type()
)
ipspCredFiltCredentialType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredFiltCredentialType.setStatus("current")


class _IpspCredFiltMatchFieldName_Type(OctetString):
    """Custom type ipspCredFiltMatchFieldName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpspCredFiltMatchFieldName_Type.__name__ = "OctetString"
_IpspCredFiltMatchFieldName_Object = MibTableColumn
ipspCredFiltMatchFieldName = _IpspCredFiltMatchFieldName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 3),
    _IpspCredFiltMatchFieldName_Type()
)
ipspCredFiltMatchFieldName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredFiltMatchFieldName.setStatus("current")


class _IpspCredFiltMatchFieldValue_Type(OctetString):
    """Custom type ipspCredFiltMatchFieldValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_IpspCredFiltMatchFieldValue_Type.__name__ = "OctetString"
_IpspCredFiltMatchFieldValue_Object = MibTableColumn
ipspCredFiltMatchFieldValue = _IpspCredFiltMatchFieldValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 4),
    _IpspCredFiltMatchFieldValue_Type()
)
ipspCredFiltMatchFieldValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredFiltMatchFieldValue.setStatus("current")


class _IpspCredFiltAcceptCredFrom_Type(OctetString):
    """Custom type ipspCredFiltAcceptCredFrom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 117),
    )


_IpspCredFiltAcceptCredFrom_Type.__name__ = "OctetString"
_IpspCredFiltAcceptCredFrom_Object = MibTableColumn
ipspCredFiltAcceptCredFrom = _IpspCredFiltAcceptCredFrom_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 5),
    _IpspCredFiltAcceptCredFrom_Type()
)
ipspCredFiltAcceptCredFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredFiltAcceptCredFrom.setStatus("current")
_IpspCredFiltLastChanged_Type = TimeStamp
_IpspCredFiltLastChanged_Object = MibTableColumn
ipspCredFiltLastChanged = _IpspCredFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 6),
    _IpspCredFiltLastChanged_Type()
)
ipspCredFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspCredFiltLastChanged.setStatus("current")


class _IpspCredFiltStorageType_Type(StorageType):
    """Custom type ipspCredFiltStorageType based on StorageType"""
    defaultValue = 3


_IpspCredFiltStorageType_Type.__name__ = "StorageType"
_IpspCredFiltStorageType_Object = MibTableColumn
ipspCredFiltStorageType = _IpspCredFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 7),
    _IpspCredFiltStorageType_Type()
)
ipspCredFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredFiltStorageType.setStatus("current")
_IpspCredFiltRowStatus_Type = RowStatus
_IpspCredFiltRowStatus_Object = MibTableColumn
ipspCredFiltRowStatus = _IpspCredFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 12, 1, 8),
    _IpspCredFiltRowStatus_Type()
)
ipspCredFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredFiltRowStatus.setStatus("current")
_IpspPeerIdentityFilterTable_Object = MibTable
ipspPeerIdentityFilterTable = _IpspPeerIdentityFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13)
)
if mibBuilder.loadTexts:
    ipspPeerIdentityFilterTable.setStatus("current")
_IpspPeerIdentityFilterEntry_Object = MibTableRow
ipspPeerIdentityFilterEntry = _IpspPeerIdentityFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 1)
)
ipspPeerIdentityFilterEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspPeerIdFiltName"),
)
if mibBuilder.loadTexts:
    ipspPeerIdentityFilterEntry.setStatus("current")


class _IpspPeerIdFiltName_Type(SnmpAdminString):
    """Custom type ipspPeerIdFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspPeerIdFiltName_Type.__name__ = "SnmpAdminString"
_IpspPeerIdFiltName_Object = MibTableColumn
ipspPeerIdFiltName = _IpspPeerIdFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 1, 1),
    _IpspPeerIdFiltName_Type()
)
ipspPeerIdFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspPeerIdFiltName.setStatus("current")
_IpspPeerIdFiltIdentityType_Type = IpsecDoiIdentType
_IpspPeerIdFiltIdentityType_Object = MibTableColumn
ipspPeerIdFiltIdentityType = _IpspPeerIdFiltIdentityType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 1, 2),
    _IpspPeerIdFiltIdentityType_Type()
)
ipspPeerIdFiltIdentityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdFiltIdentityType.setStatus("current")
_IpspPeerIdFiltIdentityValue_Type = IpspIdentityFilter
_IpspPeerIdFiltIdentityValue_Object = MibTableColumn
ipspPeerIdFiltIdentityValue = _IpspPeerIdFiltIdentityValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 1, 3),
    _IpspPeerIdFiltIdentityValue_Type()
)
ipspPeerIdFiltIdentityValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdFiltIdentityValue.setStatus("current")
_IpspPeerIdFiltLastChanged_Type = TimeStamp
_IpspPeerIdFiltLastChanged_Object = MibTableColumn
ipspPeerIdFiltLastChanged = _IpspPeerIdFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 1, 4),
    _IpspPeerIdFiltLastChanged_Type()
)
ipspPeerIdFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspPeerIdFiltLastChanged.setStatus("current")


class _IpspPeerIdFiltStorageType_Type(StorageType):
    """Custom type ipspPeerIdFiltStorageType based on StorageType"""
    defaultValue = 3


_IpspPeerIdFiltStorageType_Type.__name__ = "StorageType"
_IpspPeerIdFiltStorageType_Object = MibTableColumn
ipspPeerIdFiltStorageType = _IpspPeerIdFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 1, 5),
    _IpspPeerIdFiltStorageType_Type()
)
ipspPeerIdFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdFiltStorageType.setStatus("current")
_IpspPeerIdFiltRowStatus_Type = RowStatus
_IpspPeerIdFiltRowStatus_Object = MibTableColumn
ipspPeerIdFiltRowStatus = _IpspPeerIdFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 13, 1, 6),
    _IpspPeerIdFiltRowStatus_Type()
)
ipspPeerIdFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdFiltRowStatus.setStatus("current")
_IpspCompoundActionTable_Object = MibTable
ipspCompoundActionTable = _IpspCompoundActionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 14)
)
if mibBuilder.loadTexts:
    ipspCompoundActionTable.setStatus("current")
_IpspCompoundActionEntry_Object = MibTableRow
ipspCompoundActionEntry = _IpspCompoundActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 14, 1)
)
ipspCompoundActionEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspCompActName"),
)
if mibBuilder.loadTexts:
    ipspCompoundActionEntry.setStatus("current")


class _IpspCompActName_Type(SnmpAdminString):
    """Custom type ipspCompActName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspCompActName_Type.__name__ = "SnmpAdminString"
_IpspCompActName_Object = MibTableColumn
ipspCompActName = _IpspCompActName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 14, 1, 1),
    _IpspCompActName_Type()
)
ipspCompActName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspCompActName.setStatus("current")


class _IpspCompActExecutionStrategy_Type(Integer32):
    """Custom type ipspCompActExecutionStrategy based on Integer32"""
    defaultValue = 2

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
        *(("reserved", 0),
          ("doAll", 1),
          ("doUntilSuccess", 2),
          ("doUntilFailure", 3))
    )


_IpspCompActExecutionStrategy_Type.__name__ = "Integer32"
_IpspCompActExecutionStrategy_Object = MibTableColumn
ipspCompActExecutionStrategy = _IpspCompActExecutionStrategy_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 14, 1, 2),
    _IpspCompActExecutionStrategy_Type()
)
ipspCompActExecutionStrategy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCompActExecutionStrategy.setStatus("current")
_IpspCompActLastChanged_Type = TimeStamp
_IpspCompActLastChanged_Object = MibTableColumn
ipspCompActLastChanged = _IpspCompActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 14, 1, 3),
    _IpspCompActLastChanged_Type()
)
ipspCompActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspCompActLastChanged.setStatus("current")


class _IpspCompActStorageType_Type(StorageType):
    """Custom type ipspCompActStorageType based on StorageType"""
    defaultValue = 3


_IpspCompActStorageType_Type.__name__ = "StorageType"
_IpspCompActStorageType_Object = MibTableColumn
ipspCompActStorageType = _IpspCompActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 14, 1, 4),
    _IpspCompActStorageType_Type()
)
ipspCompActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCompActStorageType.setStatus("current")
_IpspCompActRowStatus_Type = RowStatus
_IpspCompActRowStatus_Object = MibTableColumn
ipspCompActRowStatus = _IpspCompActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 14, 1, 5),
    _IpspCompActRowStatus_Type()
)
ipspCompActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCompActRowStatus.setStatus("current")
_IpspSubactionsTable_Object = MibTable
ipspSubactionsTable = _IpspSubactionsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 15)
)
if mibBuilder.loadTexts:
    ipspSubactionsTable.setStatus("current")
_IpspSubactionsEntry_Object = MibTableRow
ipspSubactionsEntry = _IpspSubactionsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 15, 1)
)
ipspSubactionsEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspCompActName"),
    (0, "IPSEC-POLICY-MIB", "ipspSubActPriority"),
)
if mibBuilder.loadTexts:
    ipspSubactionsEntry.setStatus("current")


class _IpspSubActPriority_Type(Integer32):
    """Custom type ipspSubActPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_IpspSubActPriority_Type.__name__ = "Integer32"
_IpspSubActPriority_Object = MibTableColumn
ipspSubActPriority = _IpspSubActPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 15, 1, 1),
    _IpspSubActPriority_Type()
)
ipspSubActPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspSubActPriority.setStatus("current")
_IpspSubActSubActionName_Type = VariablePointer
_IpspSubActSubActionName_Object = MibTableColumn
ipspSubActSubActionName = _IpspSubActSubActionName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 15, 1, 2),
    _IpspSubActSubActionName_Type()
)
ipspSubActSubActionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSubActSubActionName.setStatus("current")
_AiipspCompActLastChanged_Type = TimeStamp
_AiipspCompActLastChanged_Object = MibTableColumn
aiipspCompActLastChanged = _AiipspCompActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 15, 1, 3),
    _AiipspCompActLastChanged_Type()
)
aiipspCompActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiipspCompActLastChanged.setStatus("current")


class _AiipspCompActStorageType_Type(StorageType):
    """Custom type aiipspCompActStorageType based on StorageType"""
    defaultValue = 3


_AiipspCompActStorageType_Type.__name__ = "StorageType"
_AiipspCompActStorageType_Object = MibTableColumn
aiipspCompActStorageType = _AiipspCompActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 15, 1, 4),
    _AiipspCompActStorageType_Type()
)
aiipspCompActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aiipspCompActStorageType.setStatus("current")
_AiipspCompActRowStatus_Type = RowStatus
_AiipspCompActRowStatus_Object = MibTableColumn
aiipspCompActRowStatus = _AiipspCompActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 15, 1, 5),
    _AiipspCompActRowStatus_Type()
)
aiipspCompActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aiipspCompActRowStatus.setStatus("current")
_IpspStaticActions_ObjectIdentity = ObjectIdentity
ipspStaticActions = _IpspStaticActions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 1, 16)
)
_IpspDropAction_Type = Integer32
_IpspDropAction_Object = MibScalar
ipspDropAction = _IpspDropAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 16, 1),
    _IpspDropAction_Type()
)
ipspDropAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspDropAction.setStatus("current")
_IpspDropActionLog_Type = Integer32
_IpspDropActionLog_Object = MibScalar
ipspDropActionLog = _IpspDropActionLog_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 16, 2),
    _IpspDropActionLog_Type()
)
ipspDropActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspDropActionLog.setStatus("current")
_IpspAcceptAction_Type = Integer32
_IpspAcceptAction_Object = MibScalar
ipspAcceptAction = _IpspAcceptAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 16, 3),
    _IpspAcceptAction_Type()
)
ipspAcceptAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspAcceptAction.setStatus("current")
_IpspAcceptActionLog_Type = Integer32
_IpspAcceptActionLog_Object = MibScalar
ipspAcceptActionLog = _IpspAcceptActionLog_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 16, 4),
    _IpspAcceptActionLog_Type()
)
ipspAcceptActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspAcceptActionLog.setStatus("current")
_IpspRejectIKEAction_Type = Integer32
_IpspRejectIKEAction_Object = MibScalar
ipspRejectIKEAction = _IpspRejectIKEAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 16, 5),
    _IpspRejectIKEAction_Type()
)
ipspRejectIKEAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspRejectIKEAction.setStatus("current")
_IpspRejectIKEActionLog_Type = Integer32
_IpspRejectIKEActionLog_Object = MibScalar
ipspRejectIKEActionLog = _IpspRejectIKEActionLog_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 16, 6),
    _IpspRejectIKEActionLog_Type()
)
ipspRejectIKEActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspRejectIKEActionLog.setStatus("current")
_IpspSaPreconfiguredActionTable_Object = MibTable
ipspSaPreconfiguredActionTable = _IpspSaPreconfiguredActionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17)
)
if mibBuilder.loadTexts:
    ipspSaPreconfiguredActionTable.setStatus("current")
_IpspSaPreconfiguredActionEntry_Object = MibTableRow
ipspSaPreconfiguredActionEntry = _IpspSaPreconfiguredActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1)
)
ipspSaPreconfiguredActionEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspSaPreActActionName"),
    (0, "IPSEC-POLICY-MIB", "ipspSaPreActSADirection"),
)
if mibBuilder.loadTexts:
    ipspSaPreconfiguredActionEntry.setStatus("current")


class _IpspSaPreActActionName_Type(SnmpAdminString):
    """Custom type ipspSaPreActActionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspSaPreActActionName_Type.__name__ = "SnmpAdminString"
_IpspSaPreActActionName_Object = MibTableColumn
ipspSaPreActActionName = _IpspSaPreActActionName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 1),
    _IpspSaPreActActionName_Type()
)
ipspSaPreActActionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspSaPreActActionName.setStatus("current")
_IpspSaPreActSADirection_Type = IpspSADirection
_IpspSaPreActSADirection_Object = MibTableColumn
ipspSaPreActSADirection = _IpspSaPreActSADirection_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 2),
    _IpspSaPreActSADirection_Type()
)
ipspSaPreActSADirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspSaPreActSADirection.setStatus("current")


class _IpspSaPreActActionDescription_Type(SnmpAdminString):
    """Custom type ipspSaPreActActionDescription based on SnmpAdminString"""
    defaultValue = OctetString("")


_IpspSaPreActActionDescription_Type.__name__ = "SnmpAdminString"
_IpspSaPreActActionDescription_Object = MibTableColumn
ipspSaPreActActionDescription = _IpspSaPreActActionDescription_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 3),
    _IpspSaPreActActionDescription_Type()
)
ipspSaPreActActionDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActActionDescription.setStatus("current")


class _IpspSaPreActActionLifetimeSec_Type(Unsigned32):
    """Custom type ipspSaPreActActionLifetimeSec based on Unsigned32"""
    defaultValue = 28800


_IpspSaPreActActionLifetimeSec_Type.__name__ = "Unsigned32"
_IpspSaPreActActionLifetimeSec_Object = MibTableColumn
ipspSaPreActActionLifetimeSec = _IpspSaPreActActionLifetimeSec_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 4),
    _IpspSaPreActActionLifetimeSec_Type()
)
ipspSaPreActActionLifetimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActActionLifetimeSec.setStatus("current")


class _IpspSaPreActActionLifetimeKB_Type(Unsigned32):
    """Custom type ipspSaPreActActionLifetimeKB based on Unsigned32"""
    defaultValue = 0


_IpspSaPreActActionLifetimeKB_Type.__name__ = "Unsigned32"
_IpspSaPreActActionLifetimeKB_Object = MibTableColumn
ipspSaPreActActionLifetimeKB = _IpspSaPreActActionLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 5),
    _IpspSaPreActActionLifetimeKB_Type()
)
ipspSaPreActActionLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActActionLifetimeKB.setStatus("current")


class _IpspSaPreActDoActionLogging_Type(TruthValue):
    """Custom type ipspSaPreActDoActionLogging based on TruthValue"""
    defaultValue = 2


_IpspSaPreActDoActionLogging_Type.__name__ = "TruthValue"
_IpspSaPreActDoActionLogging_Object = MibTableColumn
ipspSaPreActDoActionLogging = _IpspSaPreActDoActionLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 6),
    _IpspSaPreActDoActionLogging_Type()
)
ipspSaPreActDoActionLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActDoActionLogging.setStatus("current")


class _IpspSaPreActDoPacketLogging_Type(IpspIPPacketLogging):
    """Custom type ipspSaPreActDoPacketLogging based on IpspIPPacketLogging"""
    defaultValue = -1


_IpspSaPreActDoPacketLogging_Type.__name__ = "IpspIPPacketLogging"
_IpspSaPreActDoPacketLogging_Object = MibTableColumn
ipspSaPreActDoPacketLogging = _IpspSaPreActDoPacketLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 7),
    _IpspSaPreActDoPacketLogging_Type()
)
ipspSaPreActDoPacketLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActDoPacketLogging.setStatus("current")


class _IpspSaPreActDFHandling_Type(Integer32):
    """Custom type ipspSaPreActDFHandling based on Integer32"""
    defaultValue = 1

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
        *(("reserved", 0),
          ("copy", 1),
          ("set", 2),
          ("clear", 3))
    )


_IpspSaPreActDFHandling_Type.__name__ = "Integer32"
_IpspSaPreActDFHandling_Object = MibTableColumn
ipspSaPreActDFHandling = _IpspSaPreActDFHandling_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 8),
    _IpspSaPreActDFHandling_Type()
)
ipspSaPreActDFHandling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActDFHandling.setStatus("current")


class _IpspSaPreActActionType_Type(IpsecDoiEncapsulationMode):
    """Custom type ipspSaPreActActionType based on IpsecDoiEncapsulationMode"""
    defaultValue = 1


_IpspSaPreActActionType_Type.__name__ = "IpsecDoiEncapsulationMode"
_IpspSaPreActActionType_Object = MibTableColumn
ipspSaPreActActionType = _IpspSaPreActActionType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 9),
    _IpspSaPreActActionType_Type()
)
ipspSaPreActActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActActionType.setStatus("current")
_IpspSaPreActAHSPI_Type = Integer32
_IpspSaPreActAHSPI_Object = MibTableColumn
ipspSaPreActAHSPI = _IpspSaPreActAHSPI_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 10),
    _IpspSaPreActAHSPI_Type()
)
ipspSaPreActAHSPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActAHSPI.setStatus("current")


class _IpspSaPreActAHTransformName_Type(SnmpAdminString):
    """Custom type ipspSaPreActAHTransformName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspSaPreActAHTransformName_Type.__name__ = "SnmpAdminString"
_IpspSaPreActAHTransformName_Object = MibTableColumn
ipspSaPreActAHTransformName = _IpspSaPreActAHTransformName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 11),
    _IpspSaPreActAHTransformName_Type()
)
ipspSaPreActAHTransformName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActAHTransformName.setStatus("current")


class _IpspSaPreActAHSharedSecretName_Type(SnmpAdminString):
    """Custom type ipspSaPreActAHSharedSecretName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspSaPreActAHSharedSecretName_Type.__name__ = "SnmpAdminString"
_IpspSaPreActAHSharedSecretName_Object = MibTableColumn
ipspSaPreActAHSharedSecretName = _IpspSaPreActAHSharedSecretName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 12),
    _IpspSaPreActAHSharedSecretName_Type()
)
ipspSaPreActAHSharedSecretName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActAHSharedSecretName.setStatus("current")
_IpspSaPreActESPSPI_Type = Integer32
_IpspSaPreActESPSPI_Object = MibTableColumn
ipspSaPreActESPSPI = _IpspSaPreActESPSPI_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 13),
    _IpspSaPreActESPSPI_Type()
)
ipspSaPreActESPSPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActESPSPI.setStatus("current")


class _IpspSaPreActESPTransformName_Type(SnmpAdminString):
    """Custom type ipspSaPreActESPTransformName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspSaPreActESPTransformName_Type.__name__ = "SnmpAdminString"
_IpspSaPreActESPTransformName_Object = MibTableColumn
ipspSaPreActESPTransformName = _IpspSaPreActESPTransformName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 14),
    _IpspSaPreActESPTransformName_Type()
)
ipspSaPreActESPTransformName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActESPTransformName.setStatus("current")


class _IpspSaPreActESPEncSecretName_Type(SnmpAdminString):
    """Custom type ipspSaPreActESPEncSecretName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspSaPreActESPEncSecretName_Type.__name__ = "SnmpAdminString"
_IpspSaPreActESPEncSecretName_Object = MibTableColumn
ipspSaPreActESPEncSecretName = _IpspSaPreActESPEncSecretName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 15),
    _IpspSaPreActESPEncSecretName_Type()
)
ipspSaPreActESPEncSecretName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActESPEncSecretName.setStatus("current")


class _IpspSaPreActESPAuthSecretName_Type(SnmpAdminString):
    """Custom type ipspSaPreActESPAuthSecretName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspSaPreActESPAuthSecretName_Type.__name__ = "SnmpAdminString"
_IpspSaPreActESPAuthSecretName_Object = MibTableColumn
ipspSaPreActESPAuthSecretName = _IpspSaPreActESPAuthSecretName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 16),
    _IpspSaPreActESPAuthSecretName_Type()
)
ipspSaPreActESPAuthSecretName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActESPAuthSecretName.setStatus("current")
_IpspSaPreActIPCompSPI_Type = Integer32
_IpspSaPreActIPCompSPI_Object = MibTableColumn
ipspSaPreActIPCompSPI = _IpspSaPreActIPCompSPI_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 17),
    _IpspSaPreActIPCompSPI_Type()
)
ipspSaPreActIPCompSPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActIPCompSPI.setStatus("current")


class _IpspSaPreActIPCompTransformName_Type(SnmpAdminString):
    """Custom type ipspSaPreActIPCompTransformName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspSaPreActIPCompTransformName_Type.__name__ = "SnmpAdminString"
_IpspSaPreActIPCompTransformName_Object = MibTableColumn
ipspSaPreActIPCompTransformName = _IpspSaPreActIPCompTransformName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 18),
    _IpspSaPreActIPCompTransformName_Type()
)
ipspSaPreActIPCompTransformName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActIPCompTransformName.setStatus("current")


class _IpspSaPreActPeerGatewayIdName_Type(SnmpAdminString):
    """Custom type ipspSaPreActPeerGatewayIdName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspSaPreActPeerGatewayIdName_Type.__name__ = "SnmpAdminString"
_IpspSaPreActPeerGatewayIdName_Object = MibTableColumn
ipspSaPreActPeerGatewayIdName = _IpspSaPreActPeerGatewayIdName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 19),
    _IpspSaPreActPeerGatewayIdName_Type()
)
ipspSaPreActPeerGatewayIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActPeerGatewayIdName.setStatus("current")
_IpspSaPreActLastChanged_Type = TimeStamp
_IpspSaPreActLastChanged_Object = MibTableColumn
ipspSaPreActLastChanged = _IpspSaPreActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 20),
    _IpspSaPreActLastChanged_Type()
)
ipspSaPreActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspSaPreActLastChanged.setStatus("current")


class _IpspSaPreActStorageType_Type(StorageType):
    """Custom type ipspSaPreActStorageType based on StorageType"""
    defaultValue = 3


_IpspSaPreActStorageType_Type.__name__ = "StorageType"
_IpspSaPreActStorageType_Object = MibTableColumn
ipspSaPreActStorageType = _IpspSaPreActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 21),
    _IpspSaPreActStorageType_Type()
)
ipspSaPreActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActStorageType.setStatus("current")
_IpspSaPreActRowStatus_Type = RowStatus
_IpspSaPreActRowStatus_Object = MibTableColumn
ipspSaPreActRowStatus = _IpspSaPreActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 17, 1, 22),
    _IpspSaPreActRowStatus_Type()
)
ipspSaPreActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaPreActRowStatus.setStatus("current")
_IpspSaNegotiationParametersTable_Object = MibTable
ipspSaNegotiationParametersTable = _IpspSaNegotiationParametersTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18)
)
if mibBuilder.loadTexts:
    ipspSaNegotiationParametersTable.setStatus("current")
_IpspSaNegotiationParametersEntry_Object = MibTableRow
ipspSaNegotiationParametersEntry = _IpspSaNegotiationParametersEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1)
)
ipspSaNegotiationParametersEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspSaNegParamName"),
)
if mibBuilder.loadTexts:
    ipspSaNegotiationParametersEntry.setStatus("current")


class _IpspSaNegParamName_Type(SnmpAdminString):
    """Custom type ipspSaNegParamName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspSaNegParamName_Type.__name__ = "SnmpAdminString"
_IpspSaNegParamName_Object = MibTableColumn
ipspSaNegParamName = _IpspSaNegParamName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1, 1),
    _IpspSaNegParamName_Type()
)
ipspSaNegParamName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspSaNegParamName.setStatus("current")
_IpspSaNegParamMinLifetimeSecs_Type = Unsigned32
_IpspSaNegParamMinLifetimeSecs_Object = MibTableColumn
ipspSaNegParamMinLifetimeSecs = _IpspSaNegParamMinLifetimeSecs_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1, 2),
    _IpspSaNegParamMinLifetimeSecs_Type()
)
ipspSaNegParamMinLifetimeSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaNegParamMinLifetimeSecs.setStatus("current")
_IpspSaNegParamMinLifetimeKB_Type = Unsigned32
_IpspSaNegParamMinLifetimeKB_Object = MibTableColumn
ipspSaNegParamMinLifetimeKB = _IpspSaNegParamMinLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1, 3),
    _IpspSaNegParamMinLifetimeKB_Type()
)
ipspSaNegParamMinLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaNegParamMinLifetimeKB.setStatus("current")


class _IpspSaNegParamRefreshThreshSecs_Type(Unsigned32):
    """Custom type ipspSaNegParamRefreshThreshSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IpspSaNegParamRefreshThreshSecs_Type.__name__ = "Unsigned32"
_IpspSaNegParamRefreshThreshSecs_Object = MibTableColumn
ipspSaNegParamRefreshThreshSecs = _IpspSaNegParamRefreshThreshSecs_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1, 4),
    _IpspSaNegParamRefreshThreshSecs_Type()
)
ipspSaNegParamRefreshThreshSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaNegParamRefreshThreshSecs.setStatus("current")


class _IpspSaNegParamRefreshThresholdKB_Type(Unsigned32):
    """Custom type ipspSaNegParamRefreshThresholdKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IpspSaNegParamRefreshThresholdKB_Type.__name__ = "Unsigned32"
_IpspSaNegParamRefreshThresholdKB_Object = MibTableColumn
ipspSaNegParamRefreshThresholdKB = _IpspSaNegParamRefreshThresholdKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1, 5),
    _IpspSaNegParamRefreshThresholdKB_Type()
)
ipspSaNegParamRefreshThresholdKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaNegParamRefreshThresholdKB.setStatus("current")
_IpspSaNegParamIdleDurationSecs_Type = Unsigned32
_IpspSaNegParamIdleDurationSecs_Object = MibTableColumn
ipspSaNegParamIdleDurationSecs = _IpspSaNegParamIdleDurationSecs_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1, 6),
    _IpspSaNegParamIdleDurationSecs_Type()
)
ipspSaNegParamIdleDurationSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaNegParamIdleDurationSecs.setStatus("current")
_IpspSaNegParamLastChanged_Type = TimeStamp
_IpspSaNegParamLastChanged_Object = MibTableColumn
ipspSaNegParamLastChanged = _IpspSaNegParamLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1, 7),
    _IpspSaNegParamLastChanged_Type()
)
ipspSaNegParamLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspSaNegParamLastChanged.setStatus("current")


class _IpspSaNegParamStorageType_Type(StorageType):
    """Custom type ipspSaNegParamStorageType based on StorageType"""
    defaultValue = 3


_IpspSaNegParamStorageType_Type.__name__ = "StorageType"
_IpspSaNegParamStorageType_Object = MibTableColumn
ipspSaNegParamStorageType = _IpspSaNegParamStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1, 8),
    _IpspSaNegParamStorageType_Type()
)
ipspSaNegParamStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaNegParamStorageType.setStatus("current")
_IpspSaNegParamRowStatus_Type = RowStatus
_IpspSaNegParamRowStatus_Object = MibTableColumn
ipspSaNegParamRowStatus = _IpspSaNegParamRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 18, 1, 9),
    _IpspSaNegParamRowStatus_Type()
)
ipspSaNegParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspSaNegParamRowStatus.setStatus("current")
_IpspIkeActionTable_Object = MibTable
ipspIkeActionTable = _IpspIkeActionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19)
)
if mibBuilder.loadTexts:
    ipspIkeActionTable.setStatus("current")
_IpspIkeActionEntry_Object = MibTableRow
ipspIkeActionEntry = _IpspIkeActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1)
)
ipspIkeActionEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIkeActName"),
)
if mibBuilder.loadTexts:
    ipspIkeActionEntry.setStatus("current")


class _IpspIkeActName_Type(SnmpAdminString):
    """Custom type ipspIkeActName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIkeActName_Type.__name__ = "SnmpAdminString"
_IpspIkeActName_Object = MibTableColumn
ipspIkeActName = _IpspIkeActName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 1),
    _IpspIkeActName_Type()
)
ipspIkeActName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIkeActName.setStatus("current")


class _IpspIkeActParametersName_Type(SnmpAdminString):
    """Custom type ipspIkeActParametersName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIkeActParametersName_Type.__name__ = "SnmpAdminString"
_IpspIkeActParametersName_Object = MibTableColumn
ipspIkeActParametersName = _IpspIkeActParametersName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 2),
    _IpspIkeActParametersName_Type()
)
ipspIkeActParametersName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActParametersName.setStatus("current")


class _IpspIkeActThresholdDerivedKeys_Type(Integer32):
    """Custom type ipspIkeActThresholdDerivedKeys based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IpspIkeActThresholdDerivedKeys_Type.__name__ = "Integer32"
_IpspIkeActThresholdDerivedKeys_Object = MibTableColumn
ipspIkeActThresholdDerivedKeys = _IpspIkeActThresholdDerivedKeys_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 3),
    _IpspIkeActThresholdDerivedKeys_Type()
)
ipspIkeActThresholdDerivedKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActThresholdDerivedKeys.setStatus("current")


class _IpspIkeActExchangeMode_Type(Integer32):
    """Custom type ipspIkeActExchangeMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("agressive", 2))
    )


_IpspIkeActExchangeMode_Type.__name__ = "Integer32"
_IpspIkeActExchangeMode_Object = MibTableColumn
ipspIkeActExchangeMode = _IpspIkeActExchangeMode_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 4),
    _IpspIkeActExchangeMode_Type()
)
ipspIkeActExchangeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActExchangeMode.setStatus("current")
_IpspIkeActAgressiveModeGroupId_Type = IkeGroupDescription
_IpspIkeActAgressiveModeGroupId_Object = MibTableColumn
ipspIkeActAgressiveModeGroupId = _IpspIkeActAgressiveModeGroupId_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 5),
    _IpspIkeActAgressiveModeGroupId_Type()
)
ipspIkeActAgressiveModeGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActAgressiveModeGroupId.setStatus("current")
_IpspIkeActIdentityType_Type = IpsecDoiIdentType
_IpspIkeActIdentityType_Object = MibTableColumn
ipspIkeActIdentityType = _IpspIkeActIdentityType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 6),
    _IpspIkeActIdentityType_Type()
)
ipspIkeActIdentityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActIdentityType.setStatus("current")


class _IpspIkeActIdentityContext_Type(SnmpAdminString):
    """Custom type ipspIkeActIdentityContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIkeActIdentityContext_Type.__name__ = "SnmpAdminString"
_IpspIkeActIdentityContext_Object = MibTableColumn
ipspIkeActIdentityContext = _IpspIkeActIdentityContext_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 7),
    _IpspIkeActIdentityContext_Type()
)
ipspIkeActIdentityContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActIdentityContext.setStatus("current")


class _IpspIkeActPeerName_Type(SnmpAdminString):
    """Custom type ipspIkeActPeerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspIkeActPeerName_Type.__name__ = "SnmpAdminString"
_IpspIkeActPeerName_Object = MibTableColumn
ipspIkeActPeerName = _IpspIkeActPeerName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 8),
    _IpspIkeActPeerName_Type()
)
ipspIkeActPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActPeerName.setStatus("current")


class _IpspIkeActDoActionLogging_Type(TruthValue):
    """Custom type ipspIkeActDoActionLogging based on TruthValue"""
    defaultValue = 2


_IpspIkeActDoActionLogging_Type.__name__ = "TruthValue"
_IpspIkeActDoActionLogging_Object = MibTableColumn
ipspIkeActDoActionLogging = _IpspIkeActDoActionLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 9),
    _IpspIkeActDoActionLogging_Type()
)
ipspIkeActDoActionLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActDoActionLogging.setStatus("current")


class _IpspIkeActDoPacketLogging_Type(IpspIPPacketLogging):
    """Custom type ipspIkeActDoPacketLogging based on IpspIPPacketLogging"""
    defaultValue = -1


_IpspIkeActDoPacketLogging_Type.__name__ = "IpspIPPacketLogging"
_IpspIkeActDoPacketLogging_Object = MibTableColumn
ipspIkeActDoPacketLogging = _IpspIkeActDoPacketLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 10),
    _IpspIkeActDoPacketLogging_Type()
)
ipspIkeActDoPacketLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActDoPacketLogging.setStatus("current")


class _IpspIkeActVendorId_Type(OctetString):
    """Custom type ipspIkeActVendorId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_IpspIkeActVendorId_Type.__name__ = "OctetString"
_IpspIkeActVendorId_Object = MibTableColumn
ipspIkeActVendorId = _IpspIkeActVendorId_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 11),
    _IpspIkeActVendorId_Type()
)
ipspIkeActVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActVendorId.setStatus("current")
_IpspIkeActLastChanged_Type = TimeStamp
_IpspIkeActLastChanged_Object = MibTableColumn
ipspIkeActLastChanged = _IpspIkeActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 12),
    _IpspIkeActLastChanged_Type()
)
ipspIkeActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIkeActLastChanged.setStatus("current")


class _IpspIkeActStorageType_Type(StorageType):
    """Custom type ipspIkeActStorageType based on StorageType"""
    defaultValue = 3


_IpspIkeActStorageType_Type.__name__ = "StorageType"
_IpspIkeActStorageType_Object = MibTableColumn
ipspIkeActStorageType = _IpspIkeActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 13),
    _IpspIkeActStorageType_Type()
)
ipspIkeActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActStorageType.setStatus("current")
_IpspIkeActRowStatus_Type = RowStatus
_IpspIkeActRowStatus_Object = MibTableColumn
ipspIkeActRowStatus = _IpspIkeActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 19, 1, 14),
    _IpspIkeActRowStatus_Type()
)
ipspIkeActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActRowStatus.setStatus("current")
_IpspIkeActionProposalsTable_Object = MibTable
ipspIkeActionProposalsTable = _IpspIkeActionProposalsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 20)
)
if mibBuilder.loadTexts:
    ipspIkeActionProposalsTable.setStatus("current")
_IpspIkeActionProposalsEntry_Object = MibTableRow
ipspIkeActionProposalsEntry = _IpspIkeActionProposalsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 20, 1)
)
ipspIkeActionProposalsEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIkeActName"),
    (0, "IPSEC-POLICY-MIB", "ipspIkeActPropPriority"),
)
if mibBuilder.loadTexts:
    ipspIkeActionProposalsEntry.setStatus("current")


class _IpspIkeActPropPriority_Type(Integer32):
    """Custom type ipspIkeActPropPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpspIkeActPropPriority_Type.__name__ = "Integer32"
_IpspIkeActPropPriority_Object = MibTableColumn
ipspIkeActPropPriority = _IpspIkeActPropPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 20, 1, 1),
    _IpspIkeActPropPriority_Type()
)
ipspIkeActPropPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIkeActPropPriority.setStatus("current")


class _IpspIkeActPropName_Type(SnmpAdminString):
    """Custom type ipspIkeActPropName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIkeActPropName_Type.__name__ = "SnmpAdminString"
_IpspIkeActPropName_Object = MibTableColumn
ipspIkeActPropName = _IpspIkeActPropName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 20, 1, 2),
    _IpspIkeActPropName_Type()
)
ipspIkeActPropName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActPropName.setStatus("current")
_IpspIkeActPropLastChanged_Type = TimeStamp
_IpspIkeActPropLastChanged_Object = MibTableColumn
ipspIkeActPropLastChanged = _IpspIkeActPropLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 20, 1, 3),
    _IpspIkeActPropLastChanged_Type()
)
ipspIkeActPropLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIkeActPropLastChanged.setStatus("current")


class _IpspIkeActPropStorageType_Type(StorageType):
    """Custom type ipspIkeActPropStorageType based on StorageType"""
    defaultValue = 3


_IpspIkeActPropStorageType_Type.__name__ = "StorageType"
_IpspIkeActPropStorageType_Object = MibTableColumn
ipspIkeActPropStorageType = _IpspIkeActPropStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 20, 1, 4),
    _IpspIkeActPropStorageType_Type()
)
ipspIkeActPropStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActPropStorageType.setStatus("current")
_IpspIkeActPropRowStatus_Type = RowStatus
_IpspIkeActPropRowStatus_Object = MibTableColumn
ipspIkeActPropRowStatus = _IpspIkeActPropRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 20, 1, 5),
    _IpspIkeActPropRowStatus_Type()
)
ipspIkeActPropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeActPropRowStatus.setStatus("current")
_IpspIkeProposalTable_Object = MibTable
ipspIkeProposalTable = _IpspIkeProposalTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21)
)
if mibBuilder.loadTexts:
    ipspIkeProposalTable.setStatus("current")
_IpspIkeProposalEntry_Object = MibTableRow
ipspIkeProposalEntry = _IpspIkeProposalEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1)
)
ipspIkeProposalEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIkeActPropName"),
)
if mibBuilder.loadTexts:
    ipspIkeProposalEntry.setStatus("current")
_IpspIkePropLifetimeDerivedKeys_Type = Unsigned32
_IpspIkePropLifetimeDerivedKeys_Object = MibTableColumn
ipspIkePropLifetimeDerivedKeys = _IpspIkePropLifetimeDerivedKeys_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 1),
    _IpspIkePropLifetimeDerivedKeys_Type()
)
ipspIkePropLifetimeDerivedKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropLifetimeDerivedKeys.setStatus("current")
_IpspIkePropCipherAlgorithm_Type = IkeEncryptionAlgorithm
_IpspIkePropCipherAlgorithm_Object = MibTableColumn
ipspIkePropCipherAlgorithm = _IpspIkePropCipherAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 2),
    _IpspIkePropCipherAlgorithm_Type()
)
ipspIkePropCipherAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropCipherAlgorithm.setStatus("current")
_IpspIkePropCipherKeyLength_Type = Unsigned32
_IpspIkePropCipherKeyLength_Object = MibTableColumn
ipspIkePropCipherKeyLength = _IpspIkePropCipherKeyLength_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 3),
    _IpspIkePropCipherKeyLength_Type()
)
ipspIkePropCipherKeyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropCipherKeyLength.setStatus("current")
_IpspIkePropCipherKeyRounds_Type = Unsigned32
_IpspIkePropCipherKeyRounds_Object = MibTableColumn
ipspIkePropCipherKeyRounds = _IpspIkePropCipherKeyRounds_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 4),
    _IpspIkePropCipherKeyRounds_Type()
)
ipspIkePropCipherKeyRounds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropCipherKeyRounds.setStatus("current")
_IpspIkePropHashAlgorithm_Type = IkeHashAlgorithm
_IpspIkePropHashAlgorithm_Object = MibTableColumn
ipspIkePropHashAlgorithm = _IpspIkePropHashAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 5),
    _IpspIkePropHashAlgorithm_Type()
)
ipspIkePropHashAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropHashAlgorithm.setStatus("current")


class _IpspIkePropPrfAlgorithm_Type(Integer32):
    """Custom type ipspIkePropPrfAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reserved", 0)
    )


_IpspIkePropPrfAlgorithm_Type.__name__ = "Integer32"
_IpspIkePropPrfAlgorithm_Object = MibTableColumn
ipspIkePropPrfAlgorithm = _IpspIkePropPrfAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 6),
    _IpspIkePropPrfAlgorithm_Type()
)
ipspIkePropPrfAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropPrfAlgorithm.setStatus("current")


class _IpspIkePropVendorId_Type(OctetString):
    """Custom type ipspIkePropVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpspIkePropVendorId_Type.__name__ = "OctetString"
_IpspIkePropVendorId_Object = MibTableColumn
ipspIkePropVendorId = _IpspIkePropVendorId_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 7),
    _IpspIkePropVendorId_Type()
)
ipspIkePropVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropVendorId.setStatus("current")
_IpspIkePropDhGroup_Type = IkeGroupDescription
_IpspIkePropDhGroup_Object = MibTableColumn
ipspIkePropDhGroup = _IpspIkePropDhGroup_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 8),
    _IpspIkePropDhGroup_Type()
)
ipspIkePropDhGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropDhGroup.setStatus("current")
_IpspIkePropAuthenticationMethod_Type = IkeAuthMethod
_IpspIkePropAuthenticationMethod_Object = MibTableColumn
ipspIkePropAuthenticationMethod = _IpspIkePropAuthenticationMethod_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 9),
    _IpspIkePropAuthenticationMethod_Type()
)
ipspIkePropAuthenticationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropAuthenticationMethod.setStatus("current")
_IpspIkePropMaxLifetimeSecs_Type = Unsigned32
_IpspIkePropMaxLifetimeSecs_Object = MibTableColumn
ipspIkePropMaxLifetimeSecs = _IpspIkePropMaxLifetimeSecs_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 10),
    _IpspIkePropMaxLifetimeSecs_Type()
)
ipspIkePropMaxLifetimeSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropMaxLifetimeSecs.setStatus("current")
_IpspIkePropMaxLifetimeKB_Type = Unsigned32
_IpspIkePropMaxLifetimeKB_Object = MibTableColumn
ipspIkePropMaxLifetimeKB = _IpspIkePropMaxLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 11),
    _IpspIkePropMaxLifetimeKB_Type()
)
ipspIkePropMaxLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropMaxLifetimeKB.setStatus("current")
_IpspIkePropProposalLastChanged_Type = TimeStamp
_IpspIkePropProposalLastChanged_Object = MibTableColumn
ipspIkePropProposalLastChanged = _IpspIkePropProposalLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 12),
    _IpspIkePropProposalLastChanged_Type()
)
ipspIkePropProposalLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIkePropProposalLastChanged.setStatus("current")


class _IpspIkePropProposalStorageType_Type(StorageType):
    """Custom type ipspIkePropProposalStorageType based on StorageType"""
    defaultValue = 3


_IpspIkePropProposalStorageType_Type.__name__ = "StorageType"
_IpspIkePropProposalStorageType_Object = MibTableColumn
ipspIkePropProposalStorageType = _IpspIkePropProposalStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 13),
    _IpspIkePropProposalStorageType_Type()
)
ipspIkePropProposalStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropProposalStorageType.setStatus("current")
_IpspIkePropProposalRowStatus_Type = RowStatus
_IpspIkePropProposalRowStatus_Object = MibTableColumn
ipspIkePropProposalRowStatus = _IpspIkePropProposalRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 21, 1, 14),
    _IpspIkePropProposalRowStatus_Type()
)
ipspIkePropProposalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkePropProposalRowStatus.setStatus("current")
_IpspIpsecActionTable_Object = MibTable
ipspIpsecActionTable = _IpspIpsecActionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22)
)
if mibBuilder.loadTexts:
    ipspIpsecActionTable.setStatus("current")
_IpspIpsecActionEntry_Object = MibTableRow
ipspIpsecActionEntry = _IpspIpsecActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1)
)
ipspIpsecActionEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIpsecActName"),
)
if mibBuilder.loadTexts:
    ipspIpsecActionEntry.setStatus("current")


class _IpspIpsecActName_Type(SnmpAdminString):
    """Custom type ipspIpsecActName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpsecActName_Type.__name__ = "SnmpAdminString"
_IpspIpsecActName_Object = MibTableColumn
ipspIpsecActName = _IpspIpsecActName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 1),
    _IpspIpsecActName_Type()
)
ipspIpsecActName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpsecActName.setStatus("current")


class _IpspIpsecActParametersName_Type(SnmpAdminString):
    """Custom type ipspIpsecActParametersName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpsecActParametersName_Type.__name__ = "SnmpAdminString"
_IpspIpsecActParametersName_Object = MibTableColumn
ipspIpsecActParametersName = _IpspIpsecActParametersName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 2),
    _IpspIpsecActParametersName_Type()
)
ipspIpsecActParametersName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActParametersName.setStatus("current")


class _IpspIpsecActProposalsName_Type(SnmpAdminString):
    """Custom type ipspIpsecActProposalsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpsecActProposalsName_Type.__name__ = "SnmpAdminString"
_IpspIpsecActProposalsName_Object = MibTableColumn
ipspIpsecActProposalsName = _IpspIpsecActProposalsName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 3),
    _IpspIpsecActProposalsName_Type()
)
ipspIpsecActProposalsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActProposalsName.setStatus("current")
_IpspIpsecActUsePfs_Type = TruthValue
_IpspIpsecActUsePfs_Object = MibTableColumn
ipspIpsecActUsePfs = _IpspIpsecActUsePfs_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 4),
    _IpspIpsecActUsePfs_Type()
)
ipspIpsecActUsePfs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActUsePfs.setStatus("current")


class _IpspIpsecActVendorId_Type(OctetString):
    """Custom type ipspIpsecActVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpspIpsecActVendorId_Type.__name__ = "OctetString"
_IpspIpsecActVendorId_Object = MibTableColumn
ipspIpsecActVendorId = _IpspIpsecActVendorId_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 5),
    _IpspIpsecActVendorId_Type()
)
ipspIpsecActVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActVendorId.setStatus("current")
_IpspIpsecActGroupId_Type = IkeGroupDescription
_IpspIpsecActGroupId_Object = MibTableColumn
ipspIpsecActGroupId = _IpspIpsecActGroupId_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 6),
    _IpspIpsecActGroupId_Type()
)
ipspIpsecActGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActGroupId.setStatus("current")


class _IpspIpsecActPeerGatewayIdName_Type(OctetString):
    """Custom type ipspIpsecActPeerGatewayIdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 116),
    )


_IpspIpsecActPeerGatewayIdName_Type.__name__ = "OctetString"
_IpspIpsecActPeerGatewayIdName_Object = MibTableColumn
ipspIpsecActPeerGatewayIdName = _IpspIpsecActPeerGatewayIdName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 7),
    _IpspIpsecActPeerGatewayIdName_Type()
)
ipspIpsecActPeerGatewayIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActPeerGatewayIdName.setStatus("current")
_IpspIpsecActUseIkeGroup_Type = TruthValue
_IpspIpsecActUseIkeGroup_Object = MibTableColumn
ipspIpsecActUseIkeGroup = _IpspIpsecActUseIkeGroup_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 8),
    _IpspIpsecActUseIkeGroup_Type()
)
ipspIpsecActUseIkeGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActUseIkeGroup.setStatus("current")


class _IpspIpsecActGranularity_Type(Integer32):
    """Custom type ipspIpsecActGranularity based on Integer32"""
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
        *(("subnet", 1),
          ("address", 2),
          ("protocol", 3),
          ("port", 4))
    )


_IpspIpsecActGranularity_Type.__name__ = "Integer32"
_IpspIpsecActGranularity_Object = MibTableColumn
ipspIpsecActGranularity = _IpspIpsecActGranularity_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 9),
    _IpspIpsecActGranularity_Type()
)
ipspIpsecActGranularity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActGranularity.setStatus("current")


class _IpspIpsecActMode_Type(Integer32):
    """Custom type ipspIpsecActMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("transport", 2))
    )


_IpspIpsecActMode_Type.__name__ = "Integer32"
_IpspIpsecActMode_Object = MibTableColumn
ipspIpsecActMode = _IpspIpsecActMode_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 10),
    _IpspIpsecActMode_Type()
)
ipspIpsecActMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActMode.setStatus("current")


class _IpspIpsecActDFHandling_Type(Integer32):
    """Custom type ipspIpsecActDFHandling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("set", 2),
          ("clear", 3))
    )


_IpspIpsecActDFHandling_Type.__name__ = "Integer32"
_IpspIpsecActDFHandling_Object = MibTableColumn
ipspIpsecActDFHandling = _IpspIpsecActDFHandling_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 11),
    _IpspIpsecActDFHandling_Type()
)
ipspIpsecActDFHandling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActDFHandling.setStatus("current")


class _IpspIpsecActDoActionLogging_Type(TruthValue):
    """Custom type ipspIpsecActDoActionLogging based on TruthValue"""
    defaultValue = 2


_IpspIpsecActDoActionLogging_Type.__name__ = "TruthValue"
_IpspIpsecActDoActionLogging_Object = MibTableColumn
ipspIpsecActDoActionLogging = _IpspIpsecActDoActionLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 12),
    _IpspIpsecActDoActionLogging_Type()
)
ipspIpsecActDoActionLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActDoActionLogging.setStatus("current")


class _IpspIpsecActDoPacketLogging_Type(IpspIPPacketLogging):
    """Custom type ipspIpsecActDoPacketLogging based on IpspIPPacketLogging"""
    defaultValue = -1


_IpspIpsecActDoPacketLogging_Type.__name__ = "IpspIPPacketLogging"
_IpspIpsecActDoPacketLogging_Object = MibTableColumn
ipspIpsecActDoPacketLogging = _IpspIpsecActDoPacketLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 13),
    _IpspIpsecActDoPacketLogging_Type()
)
ipspIpsecActDoPacketLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActDoPacketLogging.setStatus("current")
_IpspIpsecActLastChanged_Type = TimeStamp
_IpspIpsecActLastChanged_Object = MibTableColumn
ipspIpsecActLastChanged = _IpspIpsecActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 14),
    _IpspIpsecActLastChanged_Type()
)
ipspIpsecActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIpsecActLastChanged.setStatus("current")


class _IpspIpsecActStorageType_Type(StorageType):
    """Custom type ipspIpsecActStorageType based on StorageType"""
    defaultValue = 3


_IpspIpsecActStorageType_Type.__name__ = "StorageType"
_IpspIpsecActStorageType_Object = MibTableColumn
ipspIpsecActStorageType = _IpspIpsecActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 15),
    _IpspIpsecActStorageType_Type()
)
ipspIpsecActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActStorageType.setStatus("current")
_IpspIpsecActRowStatus_Type = RowStatus
_IpspIpsecActRowStatus_Object = MibTableColumn
ipspIpsecActRowStatus = _IpspIpsecActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 22, 1, 16),
    _IpspIpsecActRowStatus_Type()
)
ipspIpsecActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecActRowStatus.setStatus("current")
_IpspIpsecProposalsTable_Object = MibTable
ipspIpsecProposalsTable = _IpspIpsecProposalsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 23)
)
if mibBuilder.loadTexts:
    ipspIpsecProposalsTable.setStatus("current")
_IpspIpsecProposalsEntry_Object = MibTableRow
ipspIpsecProposalsEntry = _IpspIpsecProposalsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 23, 1)
)
ipspIpsecProposalsEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIpsecPropName"),
    (0, "IPSEC-POLICY-MIB", "ipspIpsecPropPriority"),
    (0, "IPSEC-POLICY-MIB", "ipspIpsecPropProtocolId"),
)
if mibBuilder.loadTexts:
    ipspIpsecProposalsEntry.setStatus("current")


class _IpspIpsecPropName_Type(SnmpAdminString):
    """Custom type ipspIpsecPropName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpsecPropName_Type.__name__ = "SnmpAdminString"
_IpspIpsecPropName_Object = MibTableColumn
ipspIpsecPropName = _IpspIpsecPropName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 23, 1, 1),
    _IpspIpsecPropName_Type()
)
ipspIpsecPropName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpsecPropName.setStatus("current")


class _IpspIpsecPropPriority_Type(Integer32):
    """Custom type ipspIpsecPropPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpspIpsecPropPriority_Type.__name__ = "Integer32"
_IpspIpsecPropPriority_Object = MibTableColumn
ipspIpsecPropPriority = _IpspIpsecPropPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 23, 1, 2),
    _IpspIpsecPropPriority_Type()
)
ipspIpsecPropPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpsecPropPriority.setStatus("current")
_IpspIpsecPropProtocolId_Type = IpsecDoiSecProtocolId
_IpspIpsecPropProtocolId_Object = MibTableColumn
ipspIpsecPropProtocolId = _IpspIpsecPropProtocolId_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 23, 1, 3),
    _IpspIpsecPropProtocolId_Type()
)
ipspIpsecPropProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpsecPropProtocolId.setStatus("current")


class _IpspIpsecPropTransformsName_Type(SnmpAdminString):
    """Custom type ipspIpsecPropTransformsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpsecPropTransformsName_Type.__name__ = "SnmpAdminString"
_IpspIpsecPropTransformsName_Object = MibTableColumn
ipspIpsecPropTransformsName = _IpspIpsecPropTransformsName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 23, 1, 4),
    _IpspIpsecPropTransformsName_Type()
)
ipspIpsecPropTransformsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecPropTransformsName.setStatus("current")
_IpspIpsecPropLastChanged_Type = TimeStamp
_IpspIpsecPropLastChanged_Object = MibTableColumn
ipspIpsecPropLastChanged = _IpspIpsecPropLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 23, 1, 5),
    _IpspIpsecPropLastChanged_Type()
)
ipspIpsecPropLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIpsecPropLastChanged.setStatus("current")


class _IpspIpsecPropStorageType_Type(StorageType):
    """Custom type ipspIpsecPropStorageType based on StorageType"""
    defaultValue = 3


_IpspIpsecPropStorageType_Type.__name__ = "StorageType"
_IpspIpsecPropStorageType_Object = MibTableColumn
ipspIpsecPropStorageType = _IpspIpsecPropStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 23, 1, 6),
    _IpspIpsecPropStorageType_Type()
)
ipspIpsecPropStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecPropStorageType.setStatus("current")
_IpspIpsecPropRowStatus_Type = RowStatus
_IpspIpsecPropRowStatus_Object = MibTableColumn
ipspIpsecPropRowStatus = _IpspIpsecPropRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 23, 1, 7),
    _IpspIpsecPropRowStatus_Type()
)
ipspIpsecPropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecPropRowStatus.setStatus("current")
_IpspIpsecTransformsTable_Object = MibTable
ipspIpsecTransformsTable = _IpspIpsecTransformsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 24)
)
if mibBuilder.loadTexts:
    ipspIpsecTransformsTable.setStatus("current")
_IpspIpsecTransformsEntry_Object = MibTableRow
ipspIpsecTransformsEntry = _IpspIpsecTransformsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 24, 1)
)
ipspIpsecTransformsEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIpsecTranType"),
    (0, "IPSEC-POLICY-MIB", "ipspIpsecTranName"),
    (0, "IPSEC-POLICY-MIB", "ipspIpsecTranPriority"),
)
if mibBuilder.loadTexts:
    ipspIpsecTransformsEntry.setStatus("current")
_IpspIpsecTranType_Type = IpsecDoiSecProtocolId
_IpspIpsecTranType_Object = MibTableColumn
ipspIpsecTranType = _IpspIpsecTranType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 24, 1, 1),
    _IpspIpsecTranType_Type()
)
ipspIpsecTranType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpsecTranType.setStatus("current")


class _IpspIpsecTranName_Type(SnmpAdminString):
    """Custom type ipspIpsecTranName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpsecTranName_Type.__name__ = "SnmpAdminString"
_IpspIpsecTranName_Object = MibTableColumn
ipspIpsecTranName = _IpspIpsecTranName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 24, 1, 2),
    _IpspIpsecTranName_Type()
)
ipspIpsecTranName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpsecTranName.setStatus("current")


class _IpspIpsecTranPriority_Type(Integer32):
    """Custom type ipspIpsecTranPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpspIpsecTranPriority_Type.__name__ = "Integer32"
_IpspIpsecTranPriority_Object = MibTableColumn
ipspIpsecTranPriority = _IpspIpsecTranPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 24, 1, 3),
    _IpspIpsecTranPriority_Type()
)
ipspIpsecTranPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpsecTranPriority.setStatus("current")


class _IpspIpsecTranTransformName_Type(SnmpAdminString):
    """Custom type ipspIpsecTranTransformName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpsecTranTransformName_Type.__name__ = "SnmpAdminString"
_IpspIpsecTranTransformName_Object = MibTableColumn
ipspIpsecTranTransformName = _IpspIpsecTranTransformName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 24, 1, 4),
    _IpspIpsecTranTransformName_Type()
)
ipspIpsecTranTransformName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecTranTransformName.setStatus("current")
_IpspIpsecTranLastChanged_Type = TimeStamp
_IpspIpsecTranLastChanged_Object = MibTableColumn
ipspIpsecTranLastChanged = _IpspIpsecTranLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 24, 1, 5),
    _IpspIpsecTranLastChanged_Type()
)
ipspIpsecTranLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIpsecTranLastChanged.setStatus("current")


class _IpspIpsecTranStorageType_Type(StorageType):
    """Custom type ipspIpsecTranStorageType based on StorageType"""
    defaultValue = 3


_IpspIpsecTranStorageType_Type.__name__ = "StorageType"
_IpspIpsecTranStorageType_Object = MibTableColumn
ipspIpsecTranStorageType = _IpspIpsecTranStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 24, 1, 6),
    _IpspIpsecTranStorageType_Type()
)
ipspIpsecTranStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecTranStorageType.setStatus("current")
_IpspIpsecTranRowStatus_Type = RowStatus
_IpspIpsecTranRowStatus_Object = MibTableColumn
ipspIpsecTranRowStatus = _IpspIpsecTranRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 24, 1, 7),
    _IpspIpsecTranRowStatus_Type()
)
ipspIpsecTranRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpsecTranRowStatus.setStatus("current")
_IpspAhTransformTable_Object = MibTable
ipspAhTransformTable = _IpspAhTransformTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25)
)
if mibBuilder.loadTexts:
    ipspAhTransformTable.setStatus("current")
_IpspAhTransformEntry_Object = MibTableRow
ipspAhTransformEntry = _IpspAhTransformEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1)
)
ipspAhTransformEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspAhTranName"),
)
if mibBuilder.loadTexts:
    ipspAhTransformEntry.setStatus("current")


class _IpspAhTranName_Type(SnmpAdminString):
    """Custom type ipspAhTranName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspAhTranName_Type.__name__ = "SnmpAdminString"
_IpspAhTranName_Object = MibTableColumn
ipspAhTranName = _IpspAhTranName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1, 1),
    _IpspAhTranName_Type()
)
ipspAhTranName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspAhTranName.setStatus("current")
_IpspAhTranMaxLifetimeSec_Type = Unsigned32
_IpspAhTranMaxLifetimeSec_Object = MibTableColumn
ipspAhTranMaxLifetimeSec = _IpspAhTranMaxLifetimeSec_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1, 2),
    _IpspAhTranMaxLifetimeSec_Type()
)
ipspAhTranMaxLifetimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAhTranMaxLifetimeSec.setStatus("current")
_IpspAhTranMaxLifetimeKB_Type = Unsigned32
_IpspAhTranMaxLifetimeKB_Object = MibTableColumn
ipspAhTranMaxLifetimeKB = _IpspAhTranMaxLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1, 3),
    _IpspAhTranMaxLifetimeKB_Type()
)
ipspAhTranMaxLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAhTranMaxLifetimeKB.setStatus("current")
_IpspAhTranAlgorithm_Type = IpsecDoiAuthAlgorithm
_IpspAhTranAlgorithm_Object = MibTableColumn
ipspAhTranAlgorithm = _IpspAhTranAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1, 4),
    _IpspAhTranAlgorithm_Type()
)
ipspAhTranAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAhTranAlgorithm.setStatus("current")
_IpspAhTranReplayProtection_Type = TruthValue
_IpspAhTranReplayProtection_Object = MibTableColumn
ipspAhTranReplayProtection = _IpspAhTranReplayProtection_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1, 5),
    _IpspAhTranReplayProtection_Type()
)
ipspAhTranReplayProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAhTranReplayProtection.setStatus("current")
_IpspAhTranReplayWindowSize_Type = Unsigned32
_IpspAhTranReplayWindowSize_Object = MibTableColumn
ipspAhTranReplayWindowSize = _IpspAhTranReplayWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1, 6),
    _IpspAhTranReplayWindowSize_Type()
)
ipspAhTranReplayWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAhTranReplayWindowSize.setStatus("current")
_IpspAhTranLastChanged_Type = TimeStamp
_IpspAhTranLastChanged_Object = MibTableColumn
ipspAhTranLastChanged = _IpspAhTranLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1, 7),
    _IpspAhTranLastChanged_Type()
)
ipspAhTranLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspAhTranLastChanged.setStatus("current")


class _IpspAhTranStorageType_Type(StorageType):
    """Custom type ipspAhTranStorageType based on StorageType"""
    defaultValue = 3


_IpspAhTranStorageType_Type.__name__ = "StorageType"
_IpspAhTranStorageType_Object = MibTableColumn
ipspAhTranStorageType = _IpspAhTranStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1, 8),
    _IpspAhTranStorageType_Type()
)
ipspAhTranStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAhTranStorageType.setStatus("current")
_IpspAhTranRowStatus_Type = RowStatus
_IpspAhTranRowStatus_Object = MibTableColumn
ipspAhTranRowStatus = _IpspAhTranRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 25, 1, 9),
    _IpspAhTranRowStatus_Type()
)
ipspAhTranRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAhTranRowStatus.setStatus("current")
_IpspEspTransformTable_Object = MibTable
ipspEspTransformTable = _IpspEspTransformTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26)
)
if mibBuilder.loadTexts:
    ipspEspTransformTable.setStatus("current")
_IpspEspTransformEntry_Object = MibTableRow
ipspEspTransformEntry = _IpspEspTransformEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1)
)
ipspEspTransformEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspEspTranName"),
)
if mibBuilder.loadTexts:
    ipspEspTransformEntry.setStatus("current")


class _IpspEspTranName_Type(SnmpAdminString):
    """Custom type ipspEspTranName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspEspTranName_Type.__name__ = "SnmpAdminString"
_IpspEspTranName_Object = MibTableColumn
ipspEspTranName = _IpspEspTranName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 1),
    _IpspEspTranName_Type()
)
ipspEspTranName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspEspTranName.setStatus("current")
_IpspEspTranMaxLifetimeSec_Type = Unsigned32
_IpspEspTranMaxLifetimeSec_Object = MibTableColumn
ipspEspTranMaxLifetimeSec = _IpspEspTranMaxLifetimeSec_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 2),
    _IpspEspTranMaxLifetimeSec_Type()
)
ipspEspTranMaxLifetimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranMaxLifetimeSec.setStatus("current")
_IpspEspTranMaxLifetimeKB_Type = Unsigned32
_IpspEspTranMaxLifetimeKB_Object = MibTableColumn
ipspEspTranMaxLifetimeKB = _IpspEspTranMaxLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 3),
    _IpspEspTranMaxLifetimeKB_Type()
)
ipspEspTranMaxLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranMaxLifetimeKB.setStatus("current")
_IpspEspTranCipherTransformId_Type = IpsecDoiEspTransform
_IpspEspTranCipherTransformId_Object = MibTableColumn
ipspEspTranCipherTransformId = _IpspEspTranCipherTransformId_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 4),
    _IpspEspTranCipherTransformId_Type()
)
ipspEspTranCipherTransformId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranCipherTransformId.setStatus("current")
_IpspEspTranCipherKeyLength_Type = Unsigned32
_IpspEspTranCipherKeyLength_Object = MibTableColumn
ipspEspTranCipherKeyLength = _IpspEspTranCipherKeyLength_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 5),
    _IpspEspTranCipherKeyLength_Type()
)
ipspEspTranCipherKeyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranCipherKeyLength.setStatus("current")
_IpspEspTranCipherKeyRounds_Type = Unsigned32
_IpspEspTranCipherKeyRounds_Object = MibTableColumn
ipspEspTranCipherKeyRounds = _IpspEspTranCipherKeyRounds_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 6),
    _IpspEspTranCipherKeyRounds_Type()
)
ipspEspTranCipherKeyRounds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranCipherKeyRounds.setStatus("current")
_IpspEspTranIntegrityAlgorithmId_Type = IpsecDoiAuthAlgorithm
_IpspEspTranIntegrityAlgorithmId_Object = MibTableColumn
ipspEspTranIntegrityAlgorithmId = _IpspEspTranIntegrityAlgorithmId_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 7),
    _IpspEspTranIntegrityAlgorithmId_Type()
)
ipspEspTranIntegrityAlgorithmId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranIntegrityAlgorithmId.setStatus("current")
_IpspEspTranReplayPrevention_Type = TruthValue
_IpspEspTranReplayPrevention_Object = MibTableColumn
ipspEspTranReplayPrevention = _IpspEspTranReplayPrevention_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 8),
    _IpspEspTranReplayPrevention_Type()
)
ipspEspTranReplayPrevention.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranReplayPrevention.setStatus("current")
_IpspEspTranReplayWindowSize_Type = Unsigned32
_IpspEspTranReplayWindowSize_Object = MibTableColumn
ipspEspTranReplayWindowSize = _IpspEspTranReplayWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 9),
    _IpspEspTranReplayWindowSize_Type()
)
ipspEspTranReplayWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranReplayWindowSize.setStatus("current")
_IpspEspTranLastChanged_Type = TimeStamp
_IpspEspTranLastChanged_Object = MibTableColumn
ipspEspTranLastChanged = _IpspEspTranLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 10),
    _IpspEspTranLastChanged_Type()
)
ipspEspTranLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspEspTranLastChanged.setStatus("current")


class _IpspEspTranStorageType_Type(StorageType):
    """Custom type ipspEspTranStorageType based on StorageType"""
    defaultValue = 3


_IpspEspTranStorageType_Type.__name__ = "StorageType"
_IpspEspTranStorageType_Object = MibTableColumn
ipspEspTranStorageType = _IpspEspTranStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 11),
    _IpspEspTranStorageType_Type()
)
ipspEspTranStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranStorageType.setStatus("current")
_IpspEspTranRowStatus_Type = RowStatus
_IpspEspTranRowStatus_Object = MibTableColumn
ipspEspTranRowStatus = _IpspEspTranRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 26, 1, 12),
    _IpspEspTranRowStatus_Type()
)
ipspEspTranRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspEspTranRowStatus.setStatus("current")
_IpspIpcompTransformTable_Object = MibTable
ipspIpcompTransformTable = _IpspIpcompTransformTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27)
)
if mibBuilder.loadTexts:
    ipspIpcompTransformTable.setStatus("current")
_IpspIpcompTransformEntry_Object = MibTableRow
ipspIpcompTransformEntry = _IpspIpcompTransformEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1)
)
ipspIpcompTransformEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIpcompTranName"),
)
if mibBuilder.loadTexts:
    ipspIpcompTransformEntry.setStatus("current")


class _IpspIpcompTranName_Type(SnmpAdminString):
    """Custom type ipspIpcompTranName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIpcompTranName_Type.__name__ = "SnmpAdminString"
_IpspIpcompTranName_Object = MibTableColumn
ipspIpcompTranName = _IpspIpcompTranName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1, 1),
    _IpspIpcompTranName_Type()
)
ipspIpcompTranName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIpcompTranName.setStatus("current")
_IpspIpcompTranMaxLifetimeSec_Type = Unsigned32
_IpspIpcompTranMaxLifetimeSec_Object = MibTableColumn
ipspIpcompTranMaxLifetimeSec = _IpspIpcompTranMaxLifetimeSec_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1, 2),
    _IpspIpcompTranMaxLifetimeSec_Type()
)
ipspIpcompTranMaxLifetimeSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpcompTranMaxLifetimeSec.setStatus("current")
_IpspIpcompTranMaxLifetimeKB_Type = Unsigned32
_IpspIpcompTranMaxLifetimeKB_Object = MibTableColumn
ipspIpcompTranMaxLifetimeKB = _IpspIpcompTranMaxLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1, 3),
    _IpspIpcompTranMaxLifetimeKB_Type()
)
ipspIpcompTranMaxLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpcompTranMaxLifetimeKB.setStatus("current")
_IpspIpcompTranAlgorithm_Type = IpsecDoiIpcompTransform
_IpspIpcompTranAlgorithm_Object = MibTableColumn
ipspIpcompTranAlgorithm = _IpspIpcompTranAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1, 4),
    _IpspIpcompTranAlgorithm_Type()
)
ipspIpcompTranAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpcompTranAlgorithm.setStatus("current")
_IpspIpcompTranDictionarySize_Type = Unsigned32
_IpspIpcompTranDictionarySize_Object = MibTableColumn
ipspIpcompTranDictionarySize = _IpspIpcompTranDictionarySize_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1, 5),
    _IpspIpcompTranDictionarySize_Type()
)
ipspIpcompTranDictionarySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpcompTranDictionarySize.setStatus("current")
_IpspIpcompTranPrivateAlgorithm_Type = Unsigned32
_IpspIpcompTranPrivateAlgorithm_Object = MibTableColumn
ipspIpcompTranPrivateAlgorithm = _IpspIpcompTranPrivateAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1, 6),
    _IpspIpcompTranPrivateAlgorithm_Type()
)
ipspIpcompTranPrivateAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpcompTranPrivateAlgorithm.setStatus("current")
_IpspIpcompTranLastChanged_Type = TimeStamp
_IpspIpcompTranLastChanged_Object = MibTableColumn
ipspIpcompTranLastChanged = _IpspIpcompTranLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1, 7),
    _IpspIpcompTranLastChanged_Type()
)
ipspIpcompTranLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIpcompTranLastChanged.setStatus("current")


class _IpspIpcompTranStorageType_Type(StorageType):
    """Custom type ipspIpcompTranStorageType based on StorageType"""
    defaultValue = 3


_IpspIpcompTranStorageType_Type.__name__ = "StorageType"
_IpspIpcompTranStorageType_Object = MibTableColumn
ipspIpcompTranStorageType = _IpspIpcompTranStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1, 8),
    _IpspIpcompTranStorageType_Type()
)
ipspIpcompTranStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpcompTranStorageType.setStatus("current")
_IpspIpcompTranRowStatus_Type = RowStatus
_IpspIpcompTranRowStatus_Object = MibTableColumn
ipspIpcompTranRowStatus = _IpspIpcompTranRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 27, 1, 9),
    _IpspIpcompTranRowStatus_Type()
)
ipspIpcompTranRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIpcompTranRowStatus.setStatus("current")
_IpspIkeIdentityTable_Object = MibTable
ipspIkeIdentityTable = _IpspIkeIdentityTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 28)
)
if mibBuilder.loadTexts:
    ipspIkeIdentityTable.setStatus("current")
_IpspIkeIdentityEntry_Object = MibTableRow
ipspIkeIdentityEntry = _IpspIkeIdentityEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 28, 1)
)
ipspIkeIdentityEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspEndGroupIdentType"),
    (0, "IPSEC-POLICY-MIB", "ipspEndGroupAddress"),
    (0, "IPSEC-POLICY-MIB", "ipspIkeActIdentityType"),
    (0, "IPSEC-POLICY-MIB", "ipspIkeActIdentityContext"),
)
if mibBuilder.loadTexts:
    ipspIkeIdentityEntry.setStatus("current")


class _IpspIkeIdCredentialName_Type(SnmpAdminString):
    """Custom type ipspIkeIdCredentialName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspIkeIdCredentialName_Type.__name__ = "SnmpAdminString"
_IpspIkeIdCredentialName_Object = MibTableColumn
ipspIkeIdCredentialName = _IpspIkeIdCredentialName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 28, 1, 1),
    _IpspIkeIdCredentialName_Type()
)
ipspIkeIdCredentialName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeIdCredentialName.setStatus("current")
_IpspIkeIdLastChanged_Type = TimeStamp
_IpspIkeIdLastChanged_Object = MibTableColumn
ipspIkeIdLastChanged = _IpspIkeIdLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 28, 1, 2),
    _IpspIkeIdLastChanged_Type()
)
ipspIkeIdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIkeIdLastChanged.setStatus("current")


class _IpspIkeIdStorageType_Type(StorageType):
    """Custom type ipspIkeIdStorageType based on StorageType"""
    defaultValue = 3


_IpspIkeIdStorageType_Type.__name__ = "StorageType"
_IpspIkeIdStorageType_Object = MibTableColumn
ipspIkeIdStorageType = _IpspIkeIdStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 28, 1, 3),
    _IpspIkeIdStorageType_Type()
)
ipspIkeIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeIdStorageType.setStatus("current")
_IpspIkeIdRowStatus_Type = RowStatus
_IpspIkeIdRowStatus_Object = MibTableColumn
ipspIkeIdRowStatus = _IpspIkeIdRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 28, 1, 4),
    _IpspIkeIdRowStatus_Type()
)
ipspIkeIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIkeIdRowStatus.setStatus("current")
_IpspPeerIdentityTable_Object = MibTable
ipspPeerIdentityTable = _IpspPeerIdentityTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29)
)
if mibBuilder.loadTexts:
    ipspPeerIdentityTable.setStatus("current")
_IpspPeerIdentityEntry_Object = MibTableRow
ipspPeerIdentityEntry = _IpspPeerIdentityEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1)
)
ipspPeerIdentityEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspPeerIdName"),
    (0, "IPSEC-POLICY-MIB", "ipspPeerIdPriority"),
)
if mibBuilder.loadTexts:
    ipspPeerIdentityEntry.setStatus("current")


class _IpspPeerIdName_Type(SnmpAdminString):
    """Custom type ipspPeerIdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspPeerIdName_Type.__name__ = "SnmpAdminString"
_IpspPeerIdName_Object = MibTableColumn
ipspPeerIdName = _IpspPeerIdName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 1),
    _IpspPeerIdName_Type()
)
ipspPeerIdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspPeerIdName.setStatus("current")


class _IpspPeerIdPriority_Type(Integer32):
    """Custom type ipspPeerIdPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpspPeerIdPriority_Type.__name__ = "Integer32"
_IpspPeerIdPriority_Object = MibTableColumn
ipspPeerIdPriority = _IpspPeerIdPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 2),
    _IpspPeerIdPriority_Type()
)
ipspPeerIdPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspPeerIdPriority.setStatus("current")
_IpspPeerIdType_Type = IpsecDoiIdentType
_IpspPeerIdType_Object = MibTableColumn
ipspPeerIdType = _IpspPeerIdType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 3),
    _IpspPeerIdType_Type()
)
ipspPeerIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdType.setStatus("current")
_IpspPeerIdValue_Type = IpspIdentityFilter
_IpspPeerIdValue_Object = MibTableColumn
ipspPeerIdValue = _IpspPeerIdValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 4),
    _IpspPeerIdValue_Type()
)
ipspPeerIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdValue.setStatus("current")
_IpspPeerIdAddressType_Type = InetAddressType
_IpspPeerIdAddressType_Object = MibTableColumn
ipspPeerIdAddressType = _IpspPeerIdAddressType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 5),
    _IpspPeerIdAddressType_Type()
)
ipspPeerIdAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdAddressType.setStatus("current")
_IpspPeerIdAddress_Type = InetAddress
_IpspPeerIdAddress_Object = MibTableColumn
ipspPeerIdAddress = _IpspPeerIdAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 6),
    _IpspPeerIdAddress_Type()
)
ipspPeerIdAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdAddress.setStatus("current")


class _IpspPeerIdCredentialName_Type(SnmpAdminString):
    """Custom type ipspPeerIdCredentialName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspPeerIdCredentialName_Type.__name__ = "SnmpAdminString"
_IpspPeerIdCredentialName_Object = MibTableColumn
ipspPeerIdCredentialName = _IpspPeerIdCredentialName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 7),
    _IpspPeerIdCredentialName_Type()
)
ipspPeerIdCredentialName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdCredentialName.setStatus("current")
_IpspPeerIdLastChanged_Type = TimeStamp
_IpspPeerIdLastChanged_Object = MibTableColumn
ipspPeerIdLastChanged = _IpspPeerIdLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 8),
    _IpspPeerIdLastChanged_Type()
)
ipspPeerIdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspPeerIdLastChanged.setStatus("current")


class _IpspPeerIdStorageType_Type(StorageType):
    """Custom type ipspPeerIdStorageType based on StorageType"""
    defaultValue = 3


_IpspPeerIdStorageType_Type.__name__ = "StorageType"
_IpspPeerIdStorageType_Object = MibTableColumn
ipspPeerIdStorageType = _IpspPeerIdStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 9),
    _IpspPeerIdStorageType_Type()
)
ipspPeerIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdStorageType.setStatus("current")
_IpspPeerIdRowStatus_Type = RowStatus
_IpspPeerIdRowStatus_Object = MibTableColumn
ipspPeerIdRowStatus = _IpspPeerIdRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 29, 1, 10),
    _IpspPeerIdRowStatus_Type()
)
ipspPeerIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspPeerIdRowStatus.setStatus("current")
_IpspAutostartIkeTable_Object = MibTable
ipspAutostartIkeTable = _IpspAutostartIkeTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30)
)
if mibBuilder.loadTexts:
    ipspAutostartIkeTable.setStatus("current")
_IpspAutostartIkeEntry_Object = MibTableRow
ipspAutostartIkeEntry = _IpspAutostartIkeEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1)
)
ipspAutostartIkeEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspAutoIkePriority"),
)
if mibBuilder.loadTexts:
    ipspAutostartIkeEntry.setStatus("current")


class _IpspAutoIkePriority_Type(Integer32):
    """Custom type ipspAutoIkePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpspAutoIkePriority_Type.__name__ = "Integer32"
_IpspAutoIkePriority_Object = MibTableColumn
ipspAutoIkePriority = _IpspAutoIkePriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 1),
    _IpspAutoIkePriority_Type()
)
ipspAutoIkePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspAutoIkePriority.setStatus("current")
_IpspAutoIkeAction_Type = VariablePointer
_IpspAutoIkeAction_Object = MibTableColumn
ipspAutoIkeAction = _IpspAutoIkeAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 2),
    _IpspAutoIkeAction_Type()
)
ipspAutoIkeAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAutoIkeAction.setStatus("current")
_IpspAutoIkeAddressType_Type = InetAddressType
_IpspAutoIkeAddressType_Object = MibTableColumn
ipspAutoIkeAddressType = _IpspAutoIkeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 3),
    _IpspAutoIkeAddressType_Type()
)
ipspAutoIkeAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAutoIkeAddressType.setStatus("current")
_IpspAutoIkeSourceAddress_Type = InetAddress
_IpspAutoIkeSourceAddress_Object = MibTableColumn
ipspAutoIkeSourceAddress = _IpspAutoIkeSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 4),
    _IpspAutoIkeSourceAddress_Type()
)
ipspAutoIkeSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAutoIkeSourceAddress.setStatus("current")
_IpspAutoIkeSourcePort_Type = InetPortNumber
_IpspAutoIkeSourcePort_Object = MibTableColumn
ipspAutoIkeSourcePort = _IpspAutoIkeSourcePort_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 5),
    _IpspAutoIkeSourcePort_Type()
)
ipspAutoIkeSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAutoIkeSourcePort.setStatus("current")
_IpspAutoIkeDestAddress_Type = InetAddress
_IpspAutoIkeDestAddress_Object = MibTableColumn
ipspAutoIkeDestAddress = _IpspAutoIkeDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 6),
    _IpspAutoIkeDestAddress_Type()
)
ipspAutoIkeDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAutoIkeDestAddress.setStatus("current")
_IpspAutoIkeDestPort_Type = InetPortNumber
_IpspAutoIkeDestPort_Object = MibTableColumn
ipspAutoIkeDestPort = _IpspAutoIkeDestPort_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 7),
    _IpspAutoIkeDestPort_Type()
)
ipspAutoIkeDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAutoIkeDestPort.setStatus("current")


class _IpspAutoIkeProtocol_Type(Unsigned32):
    """Custom type ipspAutoIkeProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpspAutoIkeProtocol_Type.__name__ = "Unsigned32"
_IpspAutoIkeProtocol_Object = MibTableColumn
ipspAutoIkeProtocol = _IpspAutoIkeProtocol_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 8),
    _IpspAutoIkeProtocol_Type()
)
ipspAutoIkeProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAutoIkeProtocol.setStatus("current")
_IpspAutoIkeLastChanged_Type = TimeStamp
_IpspAutoIkeLastChanged_Object = MibTableColumn
ipspAutoIkeLastChanged = _IpspAutoIkeLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 9),
    _IpspAutoIkeLastChanged_Type()
)
ipspAutoIkeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspAutoIkeLastChanged.setStatus("current")


class _IpspAutoIkeStorageType_Type(StorageType):
    """Custom type ipspAutoIkeStorageType based on StorageType"""
    defaultValue = 3


_IpspAutoIkeStorageType_Type.__name__ = "StorageType"
_IpspAutoIkeStorageType_Object = MibTableColumn
ipspAutoIkeStorageType = _IpspAutoIkeStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 10),
    _IpspAutoIkeStorageType_Type()
)
ipspAutoIkeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAutoIkeStorageType.setStatus("current")
_IpspAutoIkeRowStatus_Type = RowStatus
_IpspAutoIkeRowStatus_Object = MibTableColumn
ipspAutoIkeRowStatus = _IpspAutoIkeRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 30, 1, 11),
    _IpspAutoIkeRowStatus_Type()
)
ipspAutoIkeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspAutoIkeRowStatus.setStatus("current")
_IpspIpsecCredMngServiceTable_Object = MibTable
ipspIpsecCredMngServiceTable = _IpspIpsecCredMngServiceTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31)
)
if mibBuilder.loadTexts:
    ipspIpsecCredMngServiceTable.setStatus("current")
_IpspIpsecCredMngServiceEntry_Object = MibTableRow
ipspIpsecCredMngServiceEntry = _IpspIpsecCredMngServiceEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31, 1)
)
ipspIpsecCredMngServiceEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIcmsName"),
)
if mibBuilder.loadTexts:
    ipspIpsecCredMngServiceEntry.setStatus("current")


class _IpspIcmsName_Type(SnmpAdminString):
    """Custom type ipspIcmsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspIcmsName_Type.__name__ = "SnmpAdminString"
_IpspIcmsName_Object = MibTableColumn
ipspIcmsName = _IpspIcmsName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31, 1, 1),
    _IpspIcmsName_Type()
)
ipspIcmsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspIcmsName.setStatus("current")


class _IpspIcmsDistinguishedName_Type(OctetString):
    """Custom type ipspIcmsDistinguishedName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_IpspIcmsDistinguishedName_Type.__name__ = "OctetString"
_IpspIcmsDistinguishedName_Object = MibTableColumn
ipspIcmsDistinguishedName = _IpspIcmsDistinguishedName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31, 1, 2),
    _IpspIcmsDistinguishedName_Type()
)
ipspIcmsDistinguishedName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIcmsDistinguishedName.setStatus("current")


class _IpspIcmsPolicyStatement_Type(OctetString):
    """Custom type ipspIcmsPolicyStatement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_IpspIcmsPolicyStatement_Type.__name__ = "OctetString"
_IpspIcmsPolicyStatement_Object = MibTableColumn
ipspIcmsPolicyStatement = _IpspIcmsPolicyStatement_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31, 1, 3),
    _IpspIcmsPolicyStatement_Type()
)
ipspIcmsPolicyStatement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIcmsPolicyStatement.setStatus("current")


class _IpspIcmsMaxChainLength_Type(Integer32):
    """Custom type ipspIcmsMaxChainLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpspIcmsMaxChainLength_Type.__name__ = "Integer32"
_IpspIcmsMaxChainLength_Object = MibTableColumn
ipspIcmsMaxChainLength = _IpspIcmsMaxChainLength_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31, 1, 4),
    _IpspIcmsMaxChainLength_Type()
)
ipspIcmsMaxChainLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIcmsMaxChainLength.setStatus("current")


class _IpspIcmsCredentialName_Type(SnmpAdminString):
    """Custom type ipspIcmsCredentialName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspIcmsCredentialName_Type.__name__ = "SnmpAdminString"
_IpspIcmsCredentialName_Object = MibTableColumn
ipspIcmsCredentialName = _IpspIcmsCredentialName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31, 1, 5),
    _IpspIcmsCredentialName_Type()
)
ipspIcmsCredentialName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIcmsCredentialName.setStatus("current")
_IpspIcmsLastChanged_Type = TimeStamp
_IpspIcmsLastChanged_Object = MibTableColumn
ipspIcmsLastChanged = _IpspIcmsLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31, 1, 6),
    _IpspIcmsLastChanged_Type()
)
ipspIcmsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspIcmsLastChanged.setStatus("current")


class _IpspIcmsStorageType_Type(StorageType):
    """Custom type ipspIcmsStorageType based on StorageType"""
    defaultValue = 3


_IpspIcmsStorageType_Type.__name__ = "StorageType"
_IpspIcmsStorageType_Object = MibTableColumn
ipspIcmsStorageType = _IpspIcmsStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31, 1, 7),
    _IpspIcmsStorageType_Type()
)
ipspIcmsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIcmsStorageType.setStatus("current")
_IpspIcmsRowStatus_Type = RowStatus
_IpspIcmsRowStatus_Object = MibTableColumn
ipspIcmsRowStatus = _IpspIcmsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 31, 1, 8),
    _IpspIcmsRowStatus_Type()
)
ipspIcmsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspIcmsRowStatus.setStatus("current")
_IpspCredMngCRLTable_Object = MibTable
ipspCredMngCRLTable = _IpspCredMngCRLTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 32)
)
if mibBuilder.loadTexts:
    ipspCredMngCRLTable.setStatus("current")
_IpspCredMngCRLEntry_Object = MibTableRow
ipspCredMngCRLEntry = _IpspCredMngCRLEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 32, 1)
)
ipspCredMngCRLEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspIcmsName"),
    (0, "IPSEC-POLICY-MIB", "ipspCmcCRLName"),
)
if mibBuilder.loadTexts:
    ipspCredMngCRLEntry.setStatus("current")


class _IpspCmcCRLName_Type(SnmpAdminString):
    """Custom type ipspCmcCRLName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspCmcCRLName_Type.__name__ = "SnmpAdminString"
_IpspCmcCRLName_Object = MibTableColumn
ipspCmcCRLName = _IpspCmcCRLName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 32, 1, 1),
    _IpspCmcCRLName_Type()
)
ipspCmcCRLName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspCmcCRLName.setStatus("current")


class _IpspCmcDistributionPoint_Type(OctetString):
    """Custom type ipspCmcDistributionPoint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpspCmcDistributionPoint_Type.__name__ = "OctetString"
_IpspCmcDistributionPoint_Object = MibTableColumn
ipspCmcDistributionPoint = _IpspCmcDistributionPoint_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 32, 1, 2),
    _IpspCmcDistributionPoint_Type()
)
ipspCmcDistributionPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCmcDistributionPoint.setStatus("current")


class _IpspCmcThisUpdate_Type(OctetString):
    """Custom type ipspCmcThisUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspCmcThisUpdate_Type.__name__ = "OctetString"
_IpspCmcThisUpdate_Object = MibTableColumn
ipspCmcThisUpdate = _IpspCmcThisUpdate_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 32, 1, 3),
    _IpspCmcThisUpdate_Type()
)
ipspCmcThisUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCmcThisUpdate.setStatus("current")


class _IpspCmcNextUpdate_Type(OctetString):
    """Custom type ipspCmcNextUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspCmcNextUpdate_Type.__name__ = "OctetString"
_IpspCmcNextUpdate_Object = MibTableColumn
ipspCmcNextUpdate = _IpspCmcNextUpdate_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 32, 1, 4),
    _IpspCmcNextUpdate_Type()
)
ipspCmcNextUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCmcNextUpdate.setStatus("current")
_IpspCmcLastChanged_Type = TimeStamp
_IpspCmcLastChanged_Object = MibTableColumn
ipspCmcLastChanged = _IpspCmcLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 32, 1, 5),
    _IpspCmcLastChanged_Type()
)
ipspCmcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspCmcLastChanged.setStatus("current")


class _IpspCmcStorageType_Type(StorageType):
    """Custom type ipspCmcStorageType based on StorageType"""
    defaultValue = 3


_IpspCmcStorageType_Type.__name__ = "StorageType"
_IpspCmcStorageType_Object = MibTableColumn
ipspCmcStorageType = _IpspCmcStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 32, 1, 6),
    _IpspCmcStorageType_Type()
)
ipspCmcStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCmcStorageType.setStatus("current")
_IpspCmcRowStatus_Type = RowStatus
_IpspCmcRowStatus_Object = MibTableColumn
ipspCmcRowStatus = _IpspCmcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 32, 1, 7),
    _IpspCmcRowStatus_Type()
)
ipspCmcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCmcRowStatus.setStatus("current")
_IpspRevokedCertificateTable_Object = MibTable
ipspRevokedCertificateTable = _IpspRevokedCertificateTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 33)
)
if mibBuilder.loadTexts:
    ipspRevokedCertificateTable.setStatus("current")
_IpspRevokedCertificateEntry_Object = MibTableRow
ipspRevokedCertificateEntry = _IpspRevokedCertificateEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 33, 1)
)
ipspRevokedCertificateEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspCmcCRLName"),
    (0, "IPSEC-POLICY-MIB", "ipspRctCertSerialNumber"),
)
if mibBuilder.loadTexts:
    ipspRevokedCertificateEntry.setStatus("current")


class _IpspRctCertSerialNumber_Type(Unsigned32):
    """Custom type ipspRctCertSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpspRctCertSerialNumber_Type.__name__ = "Unsigned32"
_IpspRctCertSerialNumber_Object = MibTableColumn
ipspRctCertSerialNumber = _IpspRctCertSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 33, 1, 1),
    _IpspRctCertSerialNumber_Type()
)
ipspRctCertSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspRctCertSerialNumber.setStatus("current")


class _IpspRctRevokedDate_Type(OctetString):
    """Custom type ipspRctRevokedDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspRctRevokedDate_Type.__name__ = "OctetString"
_IpspRctRevokedDate_Object = MibTableColumn
ipspRctRevokedDate = _IpspRctRevokedDate_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 33, 1, 2),
    _IpspRctRevokedDate_Type()
)
ipspRctRevokedDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRctRevokedDate.setStatus("current")


class _IpspRctRevokedReason_Type(Integer32):
    """Custom type ipspRctRevokedReason based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("reserved", 0),
          ("unspecified", 1),
          ("keyCompromise", 2),
          ("cACompromise", 3),
          ("affiliationChanged", 4),
          ("superseded", 5),
          ("cessationOfOperation", 6),
          ("certificateHold", 7),
          ("removeFromCRL", 8))
    )


_IpspRctRevokedReason_Type.__name__ = "Integer32"
_IpspRctRevokedReason_Object = MibTableColumn
ipspRctRevokedReason = _IpspRctRevokedReason_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 33, 1, 3),
    _IpspRctRevokedReason_Type()
)
ipspRctRevokedReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRctRevokedReason.setStatus("current")
_IpspRctLastChanged_Type = TimeStamp
_IpspRctLastChanged_Object = MibTableColumn
ipspRctLastChanged = _IpspRctLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 33, 1, 4),
    _IpspRctLastChanged_Type()
)
ipspRctLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspRctLastChanged.setStatus("current")


class _IpspRctStorageType_Type(StorageType):
    """Custom type ipspRctStorageType based on StorageType"""
    defaultValue = 3


_IpspRctStorageType_Type.__name__ = "StorageType"
_IpspRctStorageType_Object = MibTableColumn
ipspRctStorageType = _IpspRctStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 33, 1, 5),
    _IpspRctStorageType_Type()
)
ipspRctStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRctStorageType.setStatus("current")
_IpspRctRowStatus_Type = RowStatus
_IpspRctRowStatus_Object = MibTableColumn
ipspRctRowStatus = _IpspRctRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 33, 1, 6),
    _IpspRctRowStatus_Type()
)
ipspRctRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspRctRowStatus.setStatus("current")
_IpspCredentialTable_Object = MibTable
ipspCredentialTable = _IpspCredentialTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34)
)
if mibBuilder.loadTexts:
    ipspCredentialTable.setStatus("current")
_IpspCredentialEntry_Object = MibTableRow
ipspCredentialEntry = _IpspCredentialEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1)
)
ipspCredentialEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspCredName"),
)
if mibBuilder.loadTexts:
    ipspCredentialEntry.setStatus("current")


class _IpspCredName_Type(SnmpAdminString):
    """Custom type ipspCredName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpspCredName_Type.__name__ = "SnmpAdminString"
_IpspCredName_Object = MibTableColumn
ipspCredName = _IpspCredName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 1),
    _IpspCredName_Type()
)
ipspCredName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspCredName.setStatus("current")
_IpspCredType_Type = IpspCredentialType
_IpspCredType_Object = MibTableColumn
ipspCredType = _IpspCredType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 2),
    _IpspCredType_Type()
)
ipspCredType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredType.setStatus("current")


class _IpspCredCredential_Type(OctetString):
    """Custom type ipspCredCredential based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_IpspCredCredential_Type.__name__ = "OctetString"
_IpspCredCredential_Object = MibTableColumn
ipspCredCredential = _IpspCredCredential_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 3),
    _IpspCredCredential_Type()
)
ipspCredCredential.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredCredential.setStatus("current")
_IpspCredSize_Type = Integer32
_IpspCredSize_Object = MibTableColumn
ipspCredSize = _IpspCredSize_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 4),
    _IpspCredSize_Type()
)
ipspCredSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspCredSize.setStatus("current")


class _IpspCredMngName_Type(SnmpAdminString):
    """Custom type ipspCredMngName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspCredMngName_Type.__name__ = "SnmpAdminString"
_IpspCredMngName_Object = MibTableColumn
ipspCredMngName = _IpspCredMngName_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 5),
    _IpspCredMngName_Type()
)
ipspCredMngName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredMngName.setStatus("current")


class _IpspCredRemoteID_Type(OctetString):
    """Custom type ipspCredRemoteID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpspCredRemoteID_Type.__name__ = "OctetString"
_IpspCredRemoteID_Object = MibTableColumn
ipspCredRemoteID = _IpspCredRemoteID_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 6),
    _IpspCredRemoteID_Type()
)
ipspCredRemoteID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredRemoteID.setStatus("current")


class _IpspCredAdminStatus_Type(IpspAdminStatus):
    """Custom type ipspCredAdminStatus based on IpspAdminStatus"""
    defaultValue = 2


_IpspCredAdminStatus_Type.__name__ = "IpspAdminStatus"
_IpspCredAdminStatus_Object = MibTableColumn
ipspCredAdminStatus = _IpspCredAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 7),
    _IpspCredAdminStatus_Type()
)
ipspCredAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredAdminStatus.setStatus("current")
_IpspCredLastChanged_Type = TimeStamp
_IpspCredLastChanged_Object = MibTableColumn
ipspCredLastChanged = _IpspCredLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 8),
    _IpspCredLastChanged_Type()
)
ipspCredLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspCredLastChanged.setStatus("current")


class _IpspCredStorageType_Type(StorageType):
    """Custom type ipspCredStorageType based on StorageType"""
    defaultValue = 3


_IpspCredStorageType_Type.__name__ = "StorageType"
_IpspCredStorageType_Object = MibTableColumn
ipspCredStorageType = _IpspCredStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 9),
    _IpspCredStorageType_Type()
)
ipspCredStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredStorageType.setStatus("current")
_IpspCredRowStatus_Type = RowStatus
_IpspCredRowStatus_Object = MibTableColumn
ipspCredRowStatus = _IpspCredRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 34, 1, 10),
    _IpspCredRowStatus_Type()
)
ipspCredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredRowStatus.setStatus("current")
_IpspCredentialSegmentTable_Object = MibTable
ipspCredentialSegmentTable = _IpspCredentialSegmentTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 35)
)
if mibBuilder.loadTexts:
    ipspCredentialSegmentTable.setStatus("current")
_IpspCredentialSegmentEntry_Object = MibTableRow
ipspCredentialSegmentEntry = _IpspCredentialSegmentEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 35, 1)
)
ipspCredentialSegmentEntry.setIndexNames(
    (0, "IPSEC-POLICY-MIB", "ipspCredName"),
    (0, "IPSEC-POLICY-MIB", "ipspCredSegIndex"),
)
if mibBuilder.loadTexts:
    ipspCredentialSegmentEntry.setStatus("current")


class _IpspCredSegIndex_Type(Integer32):
    """Custom type ipspCredSegIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpspCredSegIndex_Type.__name__ = "Integer32"
_IpspCredSegIndex_Object = MibTableColumn
ipspCredSegIndex = _IpspCredSegIndex_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 35, 1, 1),
    _IpspCredSegIndex_Type()
)
ipspCredSegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipspCredSegIndex.setStatus("current")
_IpspCredSegValue_Type = OctetString
_IpspCredSegValue_Object = MibTableColumn
ipspCredSegValue = _IpspCredSegValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 35, 1, 2),
    _IpspCredSegValue_Type()
)
ipspCredSegValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredSegValue.setStatus("current")
_IpspCredSegLastChanged_Type = TimeStamp
_IpspCredSegLastChanged_Object = MibTableColumn
ipspCredSegLastChanged = _IpspCredSegLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 35, 1, 3),
    _IpspCredSegLastChanged_Type()
)
ipspCredSegLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspCredSegLastChanged.setStatus("current")


class _IpspCredSegStorageType_Type(StorageType):
    """Custom type ipspCredSegStorageType based on StorageType"""
    defaultValue = 3


_IpspCredSegStorageType_Type.__name__ = "StorageType"
_IpspCredSegStorageType_Object = MibTableColumn
ipspCredSegStorageType = _IpspCredSegStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 35, 1, 4),
    _IpspCredSegStorageType_Type()
)
ipspCredSegStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspCredSegStorageType.setStatus("current")
_IpspCredSegRowStatus_Type = RowStatus
_IpspCredSegRowStatus_Object = MibTableColumn
ipspCredSegRowStatus = _IpspCredSegRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 1, 35, 1, 5),
    _IpspCredSegRowStatus_Type()
)
ipspCredSegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipspCredSegRowStatus.setStatus("current")
_IpspNotificationObjects_ObjectIdentity = ObjectIdentity
ipspNotificationObjects = _IpspNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 2)
)
_IpspNotifications_ObjectIdentity = ObjectIdentity
ipspNotifications = _IpspNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 2, 0)
)
_IpspNotificationVariables_ObjectIdentity = ObjectIdentity
ipspNotificationVariables = _IpspNotificationVariables_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 2, 1)
)
_IpspActionExecuted_Type = VariablePointer
_IpspActionExecuted_Object = MibScalar
ipspActionExecuted = _IpspActionExecuted_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 1),
    _IpspActionExecuted_Type()
)
ipspActionExecuted.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipspActionExecuted.setStatus("current")
_IpspIPInterfaceType_Type = InetAddressType
_IpspIPInterfaceType_Object = MibScalar
ipspIPInterfaceType = _IpspIPInterfaceType_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 2),
    _IpspIPInterfaceType_Type()
)
ipspIPInterfaceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipspIPInterfaceType.setStatus("current")
_IpspIPInterfaceAddress_Type = InetAddress
_IpspIPInterfaceAddress_Object = MibScalar
ipspIPInterfaceAddress = _IpspIPInterfaceAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 3),
    _IpspIPInterfaceAddress_Type()
)
ipspIPInterfaceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipspIPInterfaceAddress.setStatus("current")
_IpspIPSourceType_Type = InetAddressType
_IpspIPSourceType_Object = MibScalar
ipspIPSourceType = _IpspIPSourceType_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 4),
    _IpspIPSourceType_Type()
)
ipspIPSourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipspIPSourceType.setStatus("current")
_IpspIPSourceAddress_Type = InetAddress
_IpspIPSourceAddress_Object = MibScalar
ipspIPSourceAddress = _IpspIPSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 5),
    _IpspIPSourceAddress_Type()
)
ipspIPSourceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipspIPSourceAddress.setStatus("current")
_IpspIPDestinationType_Type = InetAddressType
_IpspIPDestinationType_Object = MibScalar
ipspIPDestinationType = _IpspIPDestinationType_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 6),
    _IpspIPDestinationType_Type()
)
ipspIPDestinationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipspIPDestinationType.setStatus("current")
_IpspIPDestinationAddress_Type = InetAddress
_IpspIPDestinationAddress_Object = MibScalar
ipspIPDestinationAddress = _IpspIPDestinationAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 7),
    _IpspIPDestinationAddress_Type()
)
ipspIPDestinationAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipspIPDestinationAddress.setStatus("current")


class _IpspPacketDirection_Type(Integer32):
    """Custom type ipspPacketDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_IpspPacketDirection_Type.__name__ = "Integer32"
_IpspPacketDirection_Object = MibScalar
ipspPacketDirection = _IpspPacketDirection_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 8),
    _IpspPacketDirection_Type()
)
ipspPacketDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipspPacketDirection.setStatus("current")
_IpspPacketPart_Type = OctetString
_IpspPacketPart_Object = MibScalar
ipspPacketPart = _IpspPacketPart_Object(
    (1, 3, 6, 1, 2, 1, 153, 2, 1, 9),
    _IpspPacketPart_Type()
)
ipspPacketPart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipspPacketPart.setStatus("current")
_IpspConformanceObjects_ObjectIdentity = ObjectIdentity
ipspConformanceObjects = _IpspConformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 3)
)
_IpspCompliances_ObjectIdentity = ObjectIdentity
ipspCompliances = _IpspCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 3, 1)
)
_IpspGroups_ObjectIdentity = ObjectIdentity
ipspGroups = _IpspGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 3, 2)
)

# Managed Objects groups

ipspEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 1)
)
ipspEndpointGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspEndGroupName"),
        ("IPSEC-POLICY-MIB", "ipspEndGroupLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspEndGroupStorageType"),
        ("IPSEC-POLICY-MIB", "ipspEndGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ipspEndpointGroup.setStatus("current")

ipspGroupContentsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 2)
)
ipspGroupContentsGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspGroupContComponentType"),
        ("IPSEC-POLICY-MIB", "ipspGroupContFilter"),
        ("IPSEC-POLICY-MIB", "ipspGroupContComponentName"),
        ("IPSEC-POLICY-MIB", "ipspGroupContLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspGroupContStorageType"),
        ("IPSEC-POLICY-MIB", "ipspGroupContRowStatus"))
)
if mibBuilder.loadTexts:
    ipspGroupContentsGroup.setStatus("current")

ipspIpsecSystemPolicyNameGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 3)
)
ipspIpsecSystemPolicyNameGroup.setObjects(
    ("IPSEC-POLICY-MIB", "ipspSystemPolicyGroupName")
)
if mibBuilder.loadTexts:
    ipspIpsecSystemPolicyNameGroup.setStatus("current")

ipspRuleDefinitionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 4)
)
ipspRuleDefinitionGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspRuleDefDescription"),
        ("IPSEC-POLICY-MIB", "ipspRuleDefFilter"),
        ("IPSEC-POLICY-MIB", "ipspRuleDefFilterNegated"),
        ("IPSEC-POLICY-MIB", "ipspRuleDefAction"),
        ("IPSEC-POLICY-MIB", "ipspRuleDefAdminStatus"),
        ("IPSEC-POLICY-MIB", "ipspRuleDefLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspRuleDefStorageType"),
        ("IPSEC-POLICY-MIB", "ipspRuleDefRowStatus"))
)
if mibBuilder.loadTexts:
    ipspRuleDefinitionGroup.setStatus("current")

ipspCompoundFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 5)
)
ipspCompoundFilterGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspCompFiltDescription"),
        ("IPSEC-POLICY-MIB", "ipspCompFiltLogicType"),
        ("IPSEC-POLICY-MIB", "ipspCompFiltLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCompFiltStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCompFiltRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspSubFiltSubfilter"),
        ("IPSEC-POLICY-MIB", "ipspSubFiltSubfilterIsNegated"),
        ("IPSEC-POLICY-MIB", "ipspSubFiltLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspSubFiltStorageType"),
        ("IPSEC-POLICY-MIB", "ipspSubFiltRowStatus"))
)
if mibBuilder.loadTexts:
    ipspCompoundFilterGroup.setStatus("current")

ipspStaticFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 6)
)
ipspStaticFilterGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspTrueFilter"),
        ("IPSEC-POLICY-MIB", "ipspIkePhase1Filter"),
        ("IPSEC-POLICY-MIB", "ipspIkePhase2Filter"))
)
if mibBuilder.loadTexts:
    ipspStaticFilterGroup.setStatus("current")

ipspIPHeaderFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 7)
)
ipspIPHeaderFilterGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspIpHeadFiltType"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltIPVersion"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltSrcAddressBegin"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltSrcAddressEnd"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltDstAddressBegin"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltDstAddressEnd"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltSrcLowPort"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltSrcHighPort"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltDstLowPort"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltDstHighPort"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltProtocol"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltIPv6FlowLabel"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIpHeadFiltRowStatus"))
)
if mibBuilder.loadTexts:
    ipspIPHeaderFilterGroup.setStatus("current")

ipspIPOffsetFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 8)
)
ipspIPOffsetFilterGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspIpOffFiltOffset"),
        ("IPSEC-POLICY-MIB", "ipspIpOffFiltType"),
        ("IPSEC-POLICY-MIB", "ipspIpOffFiltNumber"),
        ("IPSEC-POLICY-MIB", "ipspIpOffFiltValue"),
        ("IPSEC-POLICY-MIB", "ipspIpOffFiltLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIpOffFiltStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIpOffFiltRowStatus"))
)
if mibBuilder.loadTexts:
    ipspIPOffsetFilterGroup.setStatus("current")

ipspTimeFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 9)
)
ipspTimeFilterGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspTimeFiltPeriodStart"),
        ("IPSEC-POLICY-MIB", "ipspTimeFiltPeriodEnd"),
        ("IPSEC-POLICY-MIB", "ipspTimeFiltMonthOfYearMask"),
        ("IPSEC-POLICY-MIB", "ipspTimeFiltDayOfMonthMask"),
        ("IPSEC-POLICY-MIB", "ipspTimeFiltDayOfWeekMask"),
        ("IPSEC-POLICY-MIB", "ipspTimeFiltTimeOfDayMaskStart"),
        ("IPSEC-POLICY-MIB", "ipspTimeFiltTimeOfDayMaskEnd"),
        ("IPSEC-POLICY-MIB", "ipspTimeFiltLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspTimeFiltStorageType"),
        ("IPSEC-POLICY-MIB", "ipspTimeFiltRowStatus"))
)
if mibBuilder.loadTexts:
    ipspTimeFilterGroup.setStatus("current")

ipspIpsoHeaderFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 10)
)
ipspIpsoHeaderFilterGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspIpsoHeadFiltType"),
        ("IPSEC-POLICY-MIB", "ipspIpsoHeadFiltClassification"),
        ("IPSEC-POLICY-MIB", "ipspIpsoHeadFiltProtectionAuth"),
        ("IPSEC-POLICY-MIB", "ipspIpsoHeadFiltLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIpsoHeadFiltStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIpsoHeadFiltRowStatus"))
)
if mibBuilder.loadTexts:
    ipspIpsoHeaderFilterGroup.setStatus("current")

ipspCredentialFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 11)
)
ipspCredentialFilterGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspCredFiltCredentialType"),
        ("IPSEC-POLICY-MIB", "ipspCredFiltMatchFieldName"),
        ("IPSEC-POLICY-MIB", "ipspCredFiltMatchFieldValue"),
        ("IPSEC-POLICY-MIB", "ipspCredFiltAcceptCredFrom"),
        ("IPSEC-POLICY-MIB", "ipspCredFiltLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCredFiltStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCredFiltRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCmcDistributionPoint"),
        ("IPSEC-POLICY-MIB", "ipspCmcThisUpdate"),
        ("IPSEC-POLICY-MIB", "ipspCmcNextUpdate"),
        ("IPSEC-POLICY-MIB", "ipspCmcLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCmcStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCmcRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspRctRevokedDate"),
        ("IPSEC-POLICY-MIB", "ipspRctRevokedReason"),
        ("IPSEC-POLICY-MIB", "ipspRctLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspRctStorageType"),
        ("IPSEC-POLICY-MIB", "ipspRctRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspIcmsDistinguishedName"),
        ("IPSEC-POLICY-MIB", "ipspIcmsPolicyStatement"),
        ("IPSEC-POLICY-MIB", "ipspIcmsMaxChainLength"),
        ("IPSEC-POLICY-MIB", "ipspIcmsCredentialName"),
        ("IPSEC-POLICY-MIB", "ipspIcmsLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIcmsStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIcmsRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredType"),
        ("IPSEC-POLICY-MIB", "ipspCredCredential"),
        ("IPSEC-POLICY-MIB", "ipspCredMngName"),
        ("IPSEC-POLICY-MIB", "ipspCredSize"),
        ("IPSEC-POLICY-MIB", "ipspCredRemoteID"),
        ("IPSEC-POLICY-MIB", "ipspCredAdminStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCredStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCredRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredSegValue"),
        ("IPSEC-POLICY-MIB", "ipspCredSegLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCredSegStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCredSegRowStatus"))
)
if mibBuilder.loadTexts:
    ipspCredentialFilterGroup.setStatus("current")

ipspPeerIdFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 12)
)
ipspPeerIdFilterGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspPeerIdFiltIdentityType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdFiltIdentityValue"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdFiltLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdFiltStorageType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdFiltRowStatus"))
)
if mibBuilder.loadTexts:
    ipspPeerIdFilterGroup.setStatus("current")

ipspCompoundActionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 13)
)
ipspCompoundActionGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspCompActExecutionStrategy"),
        ("IPSEC-POLICY-MIB", "ipspCompActLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCompActStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCompActRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspSubActSubActionName"),
        ("IPSEC-POLICY-MIB", "aiipspCompActLastChanged"),
        ("IPSEC-POLICY-MIB", "aiipspCompActStorageType"),
        ("IPSEC-POLICY-MIB", "aiipspCompActRowStatus"))
)
if mibBuilder.loadTexts:
    ipspCompoundActionGroup.setStatus("current")

ipspPreconfiguredGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 14)
)
ipspPreconfiguredGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspSaPreActActionDescription"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActActionLifetimeSec"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActActionLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActDoActionLogging"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActDoPacketLogging"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActDFHandling"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActActionType"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActAHSPI"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActAHTransformName"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActAHSharedSecretName"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActESPSPI"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActESPTransformName"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActESPEncSecretName"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActESPAuthSecretName"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActIPCompSPI"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActIPCompTransformName"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActPeerGatewayIdName"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActStorageType"),
        ("IPSEC-POLICY-MIB", "ipspSaPreActRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspAhTranMaxLifetimeSec"),
        ("IPSEC-POLICY-MIB", "ipspAhTranMaxLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspAhTranAlgorithm"),
        ("IPSEC-POLICY-MIB", "ipspAhTranReplayProtection"),
        ("IPSEC-POLICY-MIB", "ipspAhTranReplayWindowSize"),
        ("IPSEC-POLICY-MIB", "ipspAhTranLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspAhTranStorageType"),
        ("IPSEC-POLICY-MIB", "ipspEspTranMaxLifetimeSec"),
        ("IPSEC-POLICY-MIB", "ipspEspTranMaxLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspEspTranCipherTransformId"),
        ("IPSEC-POLICY-MIB", "ipspEspTranCipherKeyLength"),
        ("IPSEC-POLICY-MIB", "ipspEspTranCipherKeyRounds"),
        ("IPSEC-POLICY-MIB", "ipspEspTranIntegrityAlgorithmId"),
        ("IPSEC-POLICY-MIB", "ipspEspTranReplayPrevention"),
        ("IPSEC-POLICY-MIB", "ipspEspTranReplayWindowSize"),
        ("IPSEC-POLICY-MIB", "ipspEspTranLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspEspTranStorageType"),
        ("IPSEC-POLICY-MIB", "ipspEspTranRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranDictionarySize"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranMaxLifetimeSec"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranMaxLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranPrivateAlgorithm"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdValue"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdAddress"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdAddressType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdCredentialName"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdStorageType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredType"),
        ("IPSEC-POLICY-MIB", "ipspCredCredential"),
        ("IPSEC-POLICY-MIB", "ipspCredMngName"),
        ("IPSEC-POLICY-MIB", "ipspCredSize"),
        ("IPSEC-POLICY-MIB", "ipspCredRemoteID"),
        ("IPSEC-POLICY-MIB", "ipspCredAdminStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCredStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCredRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredSegValue"),
        ("IPSEC-POLICY-MIB", "ipspCredSegLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCredSegStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCredSegRowStatus"))
)
if mibBuilder.loadTexts:
    ipspPreconfiguredGroup.setStatus("current")

ipspStaticActionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 15)
)
ipspStaticActionGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspDropAction"),
        ("IPSEC-POLICY-MIB", "ipspAcceptAction"),
        ("IPSEC-POLICY-MIB", "ipspRejectIKEAction"),
        ("IPSEC-POLICY-MIB", "ipspDropActionLog"),
        ("IPSEC-POLICY-MIB", "ipspAcceptActionLog"),
        ("IPSEC-POLICY-MIB", "ipspRejectIKEActionLog"))
)
if mibBuilder.loadTexts:
    ipspStaticActionGroup.setStatus("current")

ipspIpsecGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 16)
)
ipspIpsecGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspIpsecActParametersName"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActProposalsName"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActUsePfs"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActVendorId"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActGroupId"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActPeerGatewayIdName"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActUseIkeGroup"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActGranularity"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActMode"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActDFHandling"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActDoActionLogging"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActDoPacketLogging"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIpsecActRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspIpsecPropTransformsName"),
        ("IPSEC-POLICY-MIB", "ipspIpsecPropLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIpsecPropStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIpsecPropRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspIpsecTranTransformName"),
        ("IPSEC-POLICY-MIB", "ipspIpsecTranLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIpsecTranStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIpsecTranRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamMinLifetimeSecs"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamMinLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamRefreshThreshSecs"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamRefreshThresholdKB"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamIdleDurationSecs"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamStorageType"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspAhTranMaxLifetimeSec"),
        ("IPSEC-POLICY-MIB", "ipspAhTranMaxLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspAhTranAlgorithm"),
        ("IPSEC-POLICY-MIB", "ipspAhTranReplayProtection"),
        ("IPSEC-POLICY-MIB", "ipspAhTranReplayWindowSize"),
        ("IPSEC-POLICY-MIB", "ipspAhTranLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspAhTranStorageType"),
        ("IPSEC-POLICY-MIB", "ipspAhTranRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspEspTranMaxLifetimeSec"),
        ("IPSEC-POLICY-MIB", "ipspEspTranMaxLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspEspTranCipherTransformId"),
        ("IPSEC-POLICY-MIB", "ipspEspTranCipherKeyLength"),
        ("IPSEC-POLICY-MIB", "ipspEspTranCipherKeyRounds"),
        ("IPSEC-POLICY-MIB", "ipspEspTranIntegrityAlgorithmId"),
        ("IPSEC-POLICY-MIB", "ipspEspTranReplayPrevention"),
        ("IPSEC-POLICY-MIB", "ipspEspTranReplayWindowSize"),
        ("IPSEC-POLICY-MIB", "ipspEspTranLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspEspTranStorageType"),
        ("IPSEC-POLICY-MIB", "ipspEspTranRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranDictionarySize"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranAlgorithm"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranMaxLifetimeSec"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranMaxLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranPrivateAlgorithm"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIpcompTranRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdValue"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdAddress"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdAddressType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdCredentialName"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdStorageType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredType"),
        ("IPSEC-POLICY-MIB", "ipspCredCredential"),
        ("IPSEC-POLICY-MIB", "ipspCredMngName"),
        ("IPSEC-POLICY-MIB", "ipspCredSize"),
        ("IPSEC-POLICY-MIB", "ipspCredRemoteID"),
        ("IPSEC-POLICY-MIB", "ipspCredAdminStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCredStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCredRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredSegValue"),
        ("IPSEC-POLICY-MIB", "ipspCredSegLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCredSegStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCredSegRowStatus"))
)
if mibBuilder.loadTexts:
    ipspIpsecGroup.setStatus("current")

ipspIkeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 17)
)
ipspIkeGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspIkeActParametersName"),
        ("IPSEC-POLICY-MIB", "ipspIkeActThresholdDerivedKeys"),
        ("IPSEC-POLICY-MIB", "ipspIkeActExchangeMode"),
        ("IPSEC-POLICY-MIB", "ipspIkeActAgressiveModeGroupId"),
        ("IPSEC-POLICY-MIB", "ipspIkeActIdentityType"),
        ("IPSEC-POLICY-MIB", "ipspIkeActIdentityContext"),
        ("IPSEC-POLICY-MIB", "ipspIkeActPeerName"),
        ("IPSEC-POLICY-MIB", "ipspIkeActVendorId"),
        ("IPSEC-POLICY-MIB", "ipspIkeActPropName"),
        ("IPSEC-POLICY-MIB", "ipspIkeActDoActionLogging"),
        ("IPSEC-POLICY-MIB", "ipspIkeActDoPacketLogging"),
        ("IPSEC-POLICY-MIB", "ipspIkeActLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIkeActStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIkeActRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspIkeActPropLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIkeActPropStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIkeActPropRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspIkePropLifetimeDerivedKeys"),
        ("IPSEC-POLICY-MIB", "ipspIkePropCipherAlgorithm"),
        ("IPSEC-POLICY-MIB", "ipspIkePropCipherKeyLength"),
        ("IPSEC-POLICY-MIB", "ipspIkePropCipherKeyRounds"),
        ("IPSEC-POLICY-MIB", "ipspIkePropHashAlgorithm"),
        ("IPSEC-POLICY-MIB", "ipspIkePropPrfAlgorithm"),
        ("IPSEC-POLICY-MIB", "ipspIkePropVendorId"),
        ("IPSEC-POLICY-MIB", "ipspIkePropDhGroup"),
        ("IPSEC-POLICY-MIB", "ipspIkePropAuthenticationMethod"),
        ("IPSEC-POLICY-MIB", "ipspIkePropMaxLifetimeSecs"),
        ("IPSEC-POLICY-MIB", "ipspIkePropMaxLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspIkePropProposalLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIkePropProposalStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIkePropProposalRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamMinLifetimeSecs"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamMinLifetimeKB"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamRefreshThreshSecs"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamRefreshThresholdKB"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamIdleDurationSecs"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamStorageType"),
        ("IPSEC-POLICY-MIB", "ipspSaNegParamRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspIkeIdCredentialName"),
        ("IPSEC-POLICY-MIB", "ipspIkeIdLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIkeIdStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIkeIdRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeAction"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeAddressType"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeSourceAddress"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeSourcePort"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeDestAddress"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeDestPort"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeProtocol"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeStorageType"),
        ("IPSEC-POLICY-MIB", "ipspAutoIkeRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdValue"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdAddress"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdAddressType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdCredentialName"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdStorageType"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCmcDistributionPoint"),
        ("IPSEC-POLICY-MIB", "ipspCmcThisUpdate"),
        ("IPSEC-POLICY-MIB", "ipspCmcNextUpdate"),
        ("IPSEC-POLICY-MIB", "ipspCmcLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCmcStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCmcRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspRctRevokedDate"),
        ("IPSEC-POLICY-MIB", "ipspRctRevokedReason"),
        ("IPSEC-POLICY-MIB", "ipspRctLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspRctStorageType"),
        ("IPSEC-POLICY-MIB", "ipspRctRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspIcmsDistinguishedName"),
        ("IPSEC-POLICY-MIB", "ipspIcmsPolicyStatement"),
        ("IPSEC-POLICY-MIB", "ipspIcmsMaxChainLength"),
        ("IPSEC-POLICY-MIB", "ipspIcmsCredentialName"),
        ("IPSEC-POLICY-MIB", "ipspIcmsLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspIcmsStorageType"),
        ("IPSEC-POLICY-MIB", "ipspIcmsRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredType"),
        ("IPSEC-POLICY-MIB", "ipspCredCredential"),
        ("IPSEC-POLICY-MIB", "ipspCredMngName"),
        ("IPSEC-POLICY-MIB", "ipspCredSize"),
        ("IPSEC-POLICY-MIB", "ipspCredRemoteID"),
        ("IPSEC-POLICY-MIB", "ipspCredAdminStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCredStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCredRowStatus"),
        ("IPSEC-POLICY-MIB", "ipspCredSegValue"),
        ("IPSEC-POLICY-MIB", "ipspCredSegLastChanged"),
        ("IPSEC-POLICY-MIB", "ipspCredSegStorageType"),
        ("IPSEC-POLICY-MIB", "ipspCredSegRowStatus"))
)
if mibBuilder.loadTexts:
    ipspIkeGroup.setStatus("current")

ipspActionLoggingObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 18)
)
ipspActionLoggingObjectGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspActionExecuted"),
        ("IPSEC-POLICY-MIB", "ipspIPInterfaceType"),
        ("IPSEC-POLICY-MIB", "ipspIPInterfaceAddress"),
        ("IPSEC-POLICY-MIB", "ipspIPSourceType"),
        ("IPSEC-POLICY-MIB", "ipspIPSourceAddress"),
        ("IPSEC-POLICY-MIB", "ipspIPDestinationType"),
        ("IPSEC-POLICY-MIB", "ipspIPDestinationAddress"),
        ("IPSEC-POLICY-MIB", "ipspPacketDirection"),
        ("IPSEC-POLICY-MIB", "ipspPacketPart"))
)
if mibBuilder.loadTexts:
    ipspActionLoggingObjectGroup.setStatus("current")


# Notification objects

ipspActionNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 153, 2, 0, 1)
)
ipspActionNotification.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspActionExecuted"),
        ("IPSEC-POLICY-MIB", "ipspIPInterfaceType"),
        ("IPSEC-POLICY-MIB", "ipspIPInterfaceAddress"),
        ("IPSEC-POLICY-MIB", "ipspIPSourceType"),
        ("IPSEC-POLICY-MIB", "ipspIPSourceAddress"),
        ("IPSEC-POLICY-MIB", "ipspIPDestinationType"),
        ("IPSEC-POLICY-MIB", "ipspIPDestinationAddress"),
        ("IPSEC-POLICY-MIB", "ipspPacketDirection"))
)
if mibBuilder.loadTexts:
    ipspActionNotification.setStatus(
        "current"
    )

ipspPacketNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 153, 2, 0, 2)
)
ipspPacketNotification.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspActionExecuted"),
        ("IPSEC-POLICY-MIB", "ipspIPInterfaceType"),
        ("IPSEC-POLICY-MIB", "ipspIPInterfaceAddress"),
        ("IPSEC-POLICY-MIB", "ipspIPSourceType"),
        ("IPSEC-POLICY-MIB", "ipspIPSourceAddress"),
        ("IPSEC-POLICY-MIB", "ipspIPDestinationType"),
        ("IPSEC-POLICY-MIB", "ipspIPDestinationAddress"),
        ("IPSEC-POLICY-MIB", "ipspPacketDirection"),
        ("IPSEC-POLICY-MIB", "ipspPacketPart"))
)
if mibBuilder.loadTexts:
    ipspPacketNotification.setStatus(
        "current"
    )


# Notifications groups

ipspActionNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 153, 3, 2, 19)
)
ipspActionNotificationGroup.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspActionNotification"),
        ("IPSEC-POLICY-MIB", "ipspPacketNotification"))
)
if mibBuilder.loadTexts:
    ipspActionNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ipspRuleFilterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 3, 1, 1)
)
ipspRuleFilterCompliance.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspEndpointGroup"),
        ("IPSEC-POLICY-MIB", "ipspGroupContentsGroup"),
        ("IPSEC-POLICY-MIB", "ipspRuleDefinitionGroup"),
        ("IPSEC-POLICY-MIB", "ipspIPHeaderFilterGroup"),
        ("IPSEC-POLICY-MIB", "ipspStaticFilterGroup"),
        ("IPSEC-POLICY-MIB", "ipspIpsecSystemPolicyNameGroup"),
        ("IPSEC-POLICY-MIB", "ipspCompoundFilterGroup"),
        ("IPSEC-POLICY-MIB", "ipspIPOffsetFilterGroup"),
        ("IPSEC-POLICY-MIB", "ipspTimeFilterGroup"),
        ("IPSEC-POLICY-MIB", "ipspIpsoHeaderFilterGroup"),
        ("IPSEC-POLICY-MIB", "ipspCredentialFilterGroup"),
        ("IPSEC-POLICY-MIB", "ipspPeerIdFilterGroup"))
)
if mibBuilder.loadTexts:
    ipspRuleFilterCompliance.setStatus(
        "current"
    )

ipspIPsecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 3, 1, 2)
)
ipspIPsecCompliance.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspIpsecGroup"),
        ("IPSEC-POLICY-MIB", "ipspStaticActionGroup"),
        ("IPSEC-POLICY-MIB", "ipspPreconfiguredGroup"),
        ("IPSEC-POLICY-MIB", "ipspCompoundActionGroup"))
)
if mibBuilder.loadTexts:
    ipspIPsecCompliance.setStatus(
        "current"
    )

ipspIKECompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 3, 1, 3)
)
ipspIKECompliance.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspIkeGroup"),
        ("IPSEC-POLICY-MIB", "ipspCompoundActionGroup"))
)
if mibBuilder.loadTexts:
    ipspIKECompliance.setStatus(
        "current"
    )

ipspLoggingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 3, 1, 4)
)
ipspLoggingCompliance.setObjects(
      *(("IPSEC-POLICY-MIB", "ipspActionLoggingObjectGroup"),
        ("IPSEC-POLICY-MIB", "ipspActionNotificationGroup"))
)
if mibBuilder.loadTexts:
    ipspLoggingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-POLICY-MIB",
    **{"IpspBooleanOperator": IpspBooleanOperator,
       "IpspAdminStatus": IpspAdminStatus,
       "IpspSADirection": IpspSADirection,
       "IpspIPPacketLogging": IpspIPPacketLogging,
       "IpspIdentityFilter": IpspIdentityFilter,
       "IpspCredentialType": IpspCredentialType,
       "ipspMIB": ipspMIB,
       "ipspConfigObjects": ipspConfigObjects,
       "ipspLocalConfigObjects": ipspLocalConfigObjects,
       "ipspSystemPolicyGroupName": ipspSystemPolicyGroupName,
       "ipspEndpointToGroupTable": ipspEndpointToGroupTable,
       "ipspEndpointToGroupEntry": ipspEndpointToGroupEntry,
       "ipspEndGroupIdentType": ipspEndGroupIdentType,
       "ipspEndGroupAddress": ipspEndGroupAddress,
       "ipspEndGroupName": ipspEndGroupName,
       "ipspEndGroupLastChanged": ipspEndGroupLastChanged,
       "ipspEndGroupStorageType": ipspEndGroupStorageType,
       "ipspEndGroupRowStatus": ipspEndGroupRowStatus,
       "ipspGroupContentsTable": ipspGroupContentsTable,
       "ipspGroupContentsEntry": ipspGroupContentsEntry,
       "ipspGroupContName": ipspGroupContName,
       "ipspGroupContPriority": ipspGroupContPriority,
       "ipspGroupContFilter": ipspGroupContFilter,
       "ipspGroupContComponentType": ipspGroupContComponentType,
       "ipspGroupContComponentName": ipspGroupContComponentName,
       "ipspGroupContLastChanged": ipspGroupContLastChanged,
       "ipspGroupContStorageType": ipspGroupContStorageType,
       "ipspGroupContRowStatus": ipspGroupContRowStatus,
       "ipspRuleDefinitionTable": ipspRuleDefinitionTable,
       "ipspRuleDefinitionEntry": ipspRuleDefinitionEntry,
       "ipspRuleDefName": ipspRuleDefName,
       "ipspRuleDefDescription": ipspRuleDefDescription,
       "ipspRuleDefFilter": ipspRuleDefFilter,
       "ipspRuleDefFilterNegated": ipspRuleDefFilterNegated,
       "ipspRuleDefAction": ipspRuleDefAction,
       "ipspRuleDefAdminStatus": ipspRuleDefAdminStatus,
       "ipspRuleDefLastChanged": ipspRuleDefLastChanged,
       "ipspRuleDefStorageType": ipspRuleDefStorageType,
       "ipspRuleDefRowStatus": ipspRuleDefRowStatus,
       "ipspCompoundFilterTable": ipspCompoundFilterTable,
       "ipspCompoundFilterEntry": ipspCompoundFilterEntry,
       "ipspCompFiltName": ipspCompFiltName,
       "ipspCompFiltDescription": ipspCompFiltDescription,
       "ipspCompFiltLogicType": ipspCompFiltLogicType,
       "ipspCompFiltLastChanged": ipspCompFiltLastChanged,
       "ipspCompFiltStorageType": ipspCompFiltStorageType,
       "ipspCompFiltRowStatus": ipspCompFiltRowStatus,
       "ipspSubfiltersTable": ipspSubfiltersTable,
       "ipspSubfiltersEntry": ipspSubfiltersEntry,
       "ipspSubFiltPriority": ipspSubFiltPriority,
       "ipspSubFiltSubfilter": ipspSubFiltSubfilter,
       "ipspSubFiltSubfilterIsNegated": ipspSubFiltSubfilterIsNegated,
       "ipspSubFiltLastChanged": ipspSubFiltLastChanged,
       "ipspSubFiltStorageType": ipspSubFiltStorageType,
       "ipspSubFiltRowStatus": ipspSubFiltRowStatus,
       "ipspStaticFilters": ipspStaticFilters,
       "ipspTrueFilter": ipspTrueFilter,
       "ipspTrueFilterInstance": ipspTrueFilterInstance,
       "ipspIkePhase1Filter": ipspIkePhase1Filter,
       "ipspIkePhase2Filter": ipspIkePhase2Filter,
       "ipspIpHeaderFilterTable": ipspIpHeaderFilterTable,
       "ipspIpHeaderFilterEntry": ipspIpHeaderFilterEntry,
       "ipspIpHeadFiltName": ipspIpHeadFiltName,
       "ipspIpHeadFiltType": ipspIpHeadFiltType,
       "ipspIpHeadFiltIPVersion": ipspIpHeadFiltIPVersion,
       "ipspIpHeadFiltSrcAddressBegin": ipspIpHeadFiltSrcAddressBegin,
       "ipspIpHeadFiltSrcAddressEnd": ipspIpHeadFiltSrcAddressEnd,
       "ipspIpHeadFiltDstAddressBegin": ipspIpHeadFiltDstAddressBegin,
       "ipspIpHeadFiltDstAddressEnd": ipspIpHeadFiltDstAddressEnd,
       "ipspIpHeadFiltSrcLowPort": ipspIpHeadFiltSrcLowPort,
       "ipspIpHeadFiltSrcHighPort": ipspIpHeadFiltSrcHighPort,
       "ipspIpHeadFiltDstLowPort": ipspIpHeadFiltDstLowPort,
       "ipspIpHeadFiltDstHighPort": ipspIpHeadFiltDstHighPort,
       "ipspIpHeadFiltProtocol": ipspIpHeadFiltProtocol,
       "ipspIpHeadFiltIPv6FlowLabel": ipspIpHeadFiltIPv6FlowLabel,
       "ipspIpHeadFiltLastChanged": ipspIpHeadFiltLastChanged,
       "ipspIpHeadFiltStorageType": ipspIpHeadFiltStorageType,
       "ipspIpHeadFiltRowStatus": ipspIpHeadFiltRowStatus,
       "ipspIpOffsetFilterTable": ipspIpOffsetFilterTable,
       "ipspIpOffsetFilterEntry": ipspIpOffsetFilterEntry,
       "ipspIpOffFiltName": ipspIpOffFiltName,
       "ipspIpOffFiltOffset": ipspIpOffFiltOffset,
       "ipspIpOffFiltType": ipspIpOffFiltType,
       "ipspIpOffFiltNumber": ipspIpOffFiltNumber,
       "ipspIpOffFiltValue": ipspIpOffFiltValue,
       "ipspIpOffFiltLastChanged": ipspIpOffFiltLastChanged,
       "ipspIpOffFiltStorageType": ipspIpOffFiltStorageType,
       "ipspIpOffFiltRowStatus": ipspIpOffFiltRowStatus,
       "ipspTimeFilterTable": ipspTimeFilterTable,
       "ipspTimeFilterEntry": ipspTimeFilterEntry,
       "ipspTimeFiltName": ipspTimeFiltName,
       "ipspTimeFiltPeriodStart": ipspTimeFiltPeriodStart,
       "ipspTimeFiltPeriodEnd": ipspTimeFiltPeriodEnd,
       "ipspTimeFiltMonthOfYearMask": ipspTimeFiltMonthOfYearMask,
       "ipspTimeFiltDayOfMonthMask": ipspTimeFiltDayOfMonthMask,
       "ipspTimeFiltDayOfWeekMask": ipspTimeFiltDayOfWeekMask,
       "ipspTimeFiltTimeOfDayMaskStart": ipspTimeFiltTimeOfDayMaskStart,
       "ipspTimeFiltTimeOfDayMaskEnd": ipspTimeFiltTimeOfDayMaskEnd,
       "ipspTimeFiltLastChanged": ipspTimeFiltLastChanged,
       "ipspTimeFiltStorageType": ipspTimeFiltStorageType,
       "ipspTimeFiltRowStatus": ipspTimeFiltRowStatus,
       "ipspIpsoHeaderFilterTable": ipspIpsoHeaderFilterTable,
       "ipspIpsoHeaderFilterEntry": ipspIpsoHeaderFilterEntry,
       "ipspIpsoHeadFiltName": ipspIpsoHeadFiltName,
       "ipspIpsoHeadFiltType": ipspIpsoHeadFiltType,
       "ipspIpsoHeadFiltClassification": ipspIpsoHeadFiltClassification,
       "ipspIpsoHeadFiltProtectionAuth": ipspIpsoHeadFiltProtectionAuth,
       "ipspIpsoHeadFiltLastChanged": ipspIpsoHeadFiltLastChanged,
       "ipspIpsoHeadFiltStorageType": ipspIpsoHeadFiltStorageType,
       "ipspIpsoHeadFiltRowStatus": ipspIpsoHeadFiltRowStatus,
       "ipspCredentialFilterTable": ipspCredentialFilterTable,
       "ipspCredentialFilterEntry": ipspCredentialFilterEntry,
       "ipspCredFiltName": ipspCredFiltName,
       "ipspCredFiltCredentialType": ipspCredFiltCredentialType,
       "ipspCredFiltMatchFieldName": ipspCredFiltMatchFieldName,
       "ipspCredFiltMatchFieldValue": ipspCredFiltMatchFieldValue,
       "ipspCredFiltAcceptCredFrom": ipspCredFiltAcceptCredFrom,
       "ipspCredFiltLastChanged": ipspCredFiltLastChanged,
       "ipspCredFiltStorageType": ipspCredFiltStorageType,
       "ipspCredFiltRowStatus": ipspCredFiltRowStatus,
       "ipspPeerIdentityFilterTable": ipspPeerIdentityFilterTable,
       "ipspPeerIdentityFilterEntry": ipspPeerIdentityFilterEntry,
       "ipspPeerIdFiltName": ipspPeerIdFiltName,
       "ipspPeerIdFiltIdentityType": ipspPeerIdFiltIdentityType,
       "ipspPeerIdFiltIdentityValue": ipspPeerIdFiltIdentityValue,
       "ipspPeerIdFiltLastChanged": ipspPeerIdFiltLastChanged,
       "ipspPeerIdFiltStorageType": ipspPeerIdFiltStorageType,
       "ipspPeerIdFiltRowStatus": ipspPeerIdFiltRowStatus,
       "ipspCompoundActionTable": ipspCompoundActionTable,
       "ipspCompoundActionEntry": ipspCompoundActionEntry,
       "ipspCompActName": ipspCompActName,
       "ipspCompActExecutionStrategy": ipspCompActExecutionStrategy,
       "ipspCompActLastChanged": ipspCompActLastChanged,
       "ipspCompActStorageType": ipspCompActStorageType,
       "ipspCompActRowStatus": ipspCompActRowStatus,
       "ipspSubactionsTable": ipspSubactionsTable,
       "ipspSubactionsEntry": ipspSubactionsEntry,
       "ipspSubActPriority": ipspSubActPriority,
       "ipspSubActSubActionName": ipspSubActSubActionName,
       "aiipspCompActLastChanged": aiipspCompActLastChanged,
       "aiipspCompActStorageType": aiipspCompActStorageType,
       "aiipspCompActRowStatus": aiipspCompActRowStatus,
       "ipspStaticActions": ipspStaticActions,
       "ipspDropAction": ipspDropAction,
       "ipspDropActionLog": ipspDropActionLog,
       "ipspAcceptAction": ipspAcceptAction,
       "ipspAcceptActionLog": ipspAcceptActionLog,
       "ipspRejectIKEAction": ipspRejectIKEAction,
       "ipspRejectIKEActionLog": ipspRejectIKEActionLog,
       "ipspSaPreconfiguredActionTable": ipspSaPreconfiguredActionTable,
       "ipspSaPreconfiguredActionEntry": ipspSaPreconfiguredActionEntry,
       "ipspSaPreActActionName": ipspSaPreActActionName,
       "ipspSaPreActSADirection": ipspSaPreActSADirection,
       "ipspSaPreActActionDescription": ipspSaPreActActionDescription,
       "ipspSaPreActActionLifetimeSec": ipspSaPreActActionLifetimeSec,
       "ipspSaPreActActionLifetimeKB": ipspSaPreActActionLifetimeKB,
       "ipspSaPreActDoActionLogging": ipspSaPreActDoActionLogging,
       "ipspSaPreActDoPacketLogging": ipspSaPreActDoPacketLogging,
       "ipspSaPreActDFHandling": ipspSaPreActDFHandling,
       "ipspSaPreActActionType": ipspSaPreActActionType,
       "ipspSaPreActAHSPI": ipspSaPreActAHSPI,
       "ipspSaPreActAHTransformName": ipspSaPreActAHTransformName,
       "ipspSaPreActAHSharedSecretName": ipspSaPreActAHSharedSecretName,
       "ipspSaPreActESPSPI": ipspSaPreActESPSPI,
       "ipspSaPreActESPTransformName": ipspSaPreActESPTransformName,
       "ipspSaPreActESPEncSecretName": ipspSaPreActESPEncSecretName,
       "ipspSaPreActESPAuthSecretName": ipspSaPreActESPAuthSecretName,
       "ipspSaPreActIPCompSPI": ipspSaPreActIPCompSPI,
       "ipspSaPreActIPCompTransformName": ipspSaPreActIPCompTransformName,
       "ipspSaPreActPeerGatewayIdName": ipspSaPreActPeerGatewayIdName,
       "ipspSaPreActLastChanged": ipspSaPreActLastChanged,
       "ipspSaPreActStorageType": ipspSaPreActStorageType,
       "ipspSaPreActRowStatus": ipspSaPreActRowStatus,
       "ipspSaNegotiationParametersTable": ipspSaNegotiationParametersTable,
       "ipspSaNegotiationParametersEntry": ipspSaNegotiationParametersEntry,
       "ipspSaNegParamName": ipspSaNegParamName,
       "ipspSaNegParamMinLifetimeSecs": ipspSaNegParamMinLifetimeSecs,
       "ipspSaNegParamMinLifetimeKB": ipspSaNegParamMinLifetimeKB,
       "ipspSaNegParamRefreshThreshSecs": ipspSaNegParamRefreshThreshSecs,
       "ipspSaNegParamRefreshThresholdKB": ipspSaNegParamRefreshThresholdKB,
       "ipspSaNegParamIdleDurationSecs": ipspSaNegParamIdleDurationSecs,
       "ipspSaNegParamLastChanged": ipspSaNegParamLastChanged,
       "ipspSaNegParamStorageType": ipspSaNegParamStorageType,
       "ipspSaNegParamRowStatus": ipspSaNegParamRowStatus,
       "ipspIkeActionTable": ipspIkeActionTable,
       "ipspIkeActionEntry": ipspIkeActionEntry,
       "ipspIkeActName": ipspIkeActName,
       "ipspIkeActParametersName": ipspIkeActParametersName,
       "ipspIkeActThresholdDerivedKeys": ipspIkeActThresholdDerivedKeys,
       "ipspIkeActExchangeMode": ipspIkeActExchangeMode,
       "ipspIkeActAgressiveModeGroupId": ipspIkeActAgressiveModeGroupId,
       "ipspIkeActIdentityType": ipspIkeActIdentityType,
       "ipspIkeActIdentityContext": ipspIkeActIdentityContext,
       "ipspIkeActPeerName": ipspIkeActPeerName,
       "ipspIkeActDoActionLogging": ipspIkeActDoActionLogging,
       "ipspIkeActDoPacketLogging": ipspIkeActDoPacketLogging,
       "ipspIkeActVendorId": ipspIkeActVendorId,
       "ipspIkeActLastChanged": ipspIkeActLastChanged,
       "ipspIkeActStorageType": ipspIkeActStorageType,
       "ipspIkeActRowStatus": ipspIkeActRowStatus,
       "ipspIkeActionProposalsTable": ipspIkeActionProposalsTable,
       "ipspIkeActionProposalsEntry": ipspIkeActionProposalsEntry,
       "ipspIkeActPropPriority": ipspIkeActPropPriority,
       "ipspIkeActPropName": ipspIkeActPropName,
       "ipspIkeActPropLastChanged": ipspIkeActPropLastChanged,
       "ipspIkeActPropStorageType": ipspIkeActPropStorageType,
       "ipspIkeActPropRowStatus": ipspIkeActPropRowStatus,
       "ipspIkeProposalTable": ipspIkeProposalTable,
       "ipspIkeProposalEntry": ipspIkeProposalEntry,
       "ipspIkePropLifetimeDerivedKeys": ipspIkePropLifetimeDerivedKeys,
       "ipspIkePropCipherAlgorithm": ipspIkePropCipherAlgorithm,
       "ipspIkePropCipherKeyLength": ipspIkePropCipherKeyLength,
       "ipspIkePropCipherKeyRounds": ipspIkePropCipherKeyRounds,
       "ipspIkePropHashAlgorithm": ipspIkePropHashAlgorithm,
       "ipspIkePropPrfAlgorithm": ipspIkePropPrfAlgorithm,
       "ipspIkePropVendorId": ipspIkePropVendorId,
       "ipspIkePropDhGroup": ipspIkePropDhGroup,
       "ipspIkePropAuthenticationMethod": ipspIkePropAuthenticationMethod,
       "ipspIkePropMaxLifetimeSecs": ipspIkePropMaxLifetimeSecs,
       "ipspIkePropMaxLifetimeKB": ipspIkePropMaxLifetimeKB,
       "ipspIkePropProposalLastChanged": ipspIkePropProposalLastChanged,
       "ipspIkePropProposalStorageType": ipspIkePropProposalStorageType,
       "ipspIkePropProposalRowStatus": ipspIkePropProposalRowStatus,
       "ipspIpsecActionTable": ipspIpsecActionTable,
       "ipspIpsecActionEntry": ipspIpsecActionEntry,
       "ipspIpsecActName": ipspIpsecActName,
       "ipspIpsecActParametersName": ipspIpsecActParametersName,
       "ipspIpsecActProposalsName": ipspIpsecActProposalsName,
       "ipspIpsecActUsePfs": ipspIpsecActUsePfs,
       "ipspIpsecActVendorId": ipspIpsecActVendorId,
       "ipspIpsecActGroupId": ipspIpsecActGroupId,
       "ipspIpsecActPeerGatewayIdName": ipspIpsecActPeerGatewayIdName,
       "ipspIpsecActUseIkeGroup": ipspIpsecActUseIkeGroup,
       "ipspIpsecActGranularity": ipspIpsecActGranularity,
       "ipspIpsecActMode": ipspIpsecActMode,
       "ipspIpsecActDFHandling": ipspIpsecActDFHandling,
       "ipspIpsecActDoActionLogging": ipspIpsecActDoActionLogging,
       "ipspIpsecActDoPacketLogging": ipspIpsecActDoPacketLogging,
       "ipspIpsecActLastChanged": ipspIpsecActLastChanged,
       "ipspIpsecActStorageType": ipspIpsecActStorageType,
       "ipspIpsecActRowStatus": ipspIpsecActRowStatus,
       "ipspIpsecProposalsTable": ipspIpsecProposalsTable,
       "ipspIpsecProposalsEntry": ipspIpsecProposalsEntry,
       "ipspIpsecPropName": ipspIpsecPropName,
       "ipspIpsecPropPriority": ipspIpsecPropPriority,
       "ipspIpsecPropProtocolId": ipspIpsecPropProtocolId,
       "ipspIpsecPropTransformsName": ipspIpsecPropTransformsName,
       "ipspIpsecPropLastChanged": ipspIpsecPropLastChanged,
       "ipspIpsecPropStorageType": ipspIpsecPropStorageType,
       "ipspIpsecPropRowStatus": ipspIpsecPropRowStatus,
       "ipspIpsecTransformsTable": ipspIpsecTransformsTable,
       "ipspIpsecTransformsEntry": ipspIpsecTransformsEntry,
       "ipspIpsecTranType": ipspIpsecTranType,
       "ipspIpsecTranName": ipspIpsecTranName,
       "ipspIpsecTranPriority": ipspIpsecTranPriority,
       "ipspIpsecTranTransformName": ipspIpsecTranTransformName,
       "ipspIpsecTranLastChanged": ipspIpsecTranLastChanged,
       "ipspIpsecTranStorageType": ipspIpsecTranStorageType,
       "ipspIpsecTranRowStatus": ipspIpsecTranRowStatus,
       "ipspAhTransformTable": ipspAhTransformTable,
       "ipspAhTransformEntry": ipspAhTransformEntry,
       "ipspAhTranName": ipspAhTranName,
       "ipspAhTranMaxLifetimeSec": ipspAhTranMaxLifetimeSec,
       "ipspAhTranMaxLifetimeKB": ipspAhTranMaxLifetimeKB,
       "ipspAhTranAlgorithm": ipspAhTranAlgorithm,
       "ipspAhTranReplayProtection": ipspAhTranReplayProtection,
       "ipspAhTranReplayWindowSize": ipspAhTranReplayWindowSize,
       "ipspAhTranLastChanged": ipspAhTranLastChanged,
       "ipspAhTranStorageType": ipspAhTranStorageType,
       "ipspAhTranRowStatus": ipspAhTranRowStatus,
       "ipspEspTransformTable": ipspEspTransformTable,
       "ipspEspTransformEntry": ipspEspTransformEntry,
       "ipspEspTranName": ipspEspTranName,
       "ipspEspTranMaxLifetimeSec": ipspEspTranMaxLifetimeSec,
       "ipspEspTranMaxLifetimeKB": ipspEspTranMaxLifetimeKB,
       "ipspEspTranCipherTransformId": ipspEspTranCipherTransformId,
       "ipspEspTranCipherKeyLength": ipspEspTranCipherKeyLength,
       "ipspEspTranCipherKeyRounds": ipspEspTranCipherKeyRounds,
       "ipspEspTranIntegrityAlgorithmId": ipspEspTranIntegrityAlgorithmId,
       "ipspEspTranReplayPrevention": ipspEspTranReplayPrevention,
       "ipspEspTranReplayWindowSize": ipspEspTranReplayWindowSize,
       "ipspEspTranLastChanged": ipspEspTranLastChanged,
       "ipspEspTranStorageType": ipspEspTranStorageType,
       "ipspEspTranRowStatus": ipspEspTranRowStatus,
       "ipspIpcompTransformTable": ipspIpcompTransformTable,
       "ipspIpcompTransformEntry": ipspIpcompTransformEntry,
       "ipspIpcompTranName": ipspIpcompTranName,
       "ipspIpcompTranMaxLifetimeSec": ipspIpcompTranMaxLifetimeSec,
       "ipspIpcompTranMaxLifetimeKB": ipspIpcompTranMaxLifetimeKB,
       "ipspIpcompTranAlgorithm": ipspIpcompTranAlgorithm,
       "ipspIpcompTranDictionarySize": ipspIpcompTranDictionarySize,
       "ipspIpcompTranPrivateAlgorithm": ipspIpcompTranPrivateAlgorithm,
       "ipspIpcompTranLastChanged": ipspIpcompTranLastChanged,
       "ipspIpcompTranStorageType": ipspIpcompTranStorageType,
       "ipspIpcompTranRowStatus": ipspIpcompTranRowStatus,
       "ipspIkeIdentityTable": ipspIkeIdentityTable,
       "ipspIkeIdentityEntry": ipspIkeIdentityEntry,
       "ipspIkeIdCredentialName": ipspIkeIdCredentialName,
       "ipspIkeIdLastChanged": ipspIkeIdLastChanged,
       "ipspIkeIdStorageType": ipspIkeIdStorageType,
       "ipspIkeIdRowStatus": ipspIkeIdRowStatus,
       "ipspPeerIdentityTable": ipspPeerIdentityTable,
       "ipspPeerIdentityEntry": ipspPeerIdentityEntry,
       "ipspPeerIdName": ipspPeerIdName,
       "ipspPeerIdPriority": ipspPeerIdPriority,
       "ipspPeerIdType": ipspPeerIdType,
       "ipspPeerIdValue": ipspPeerIdValue,
       "ipspPeerIdAddressType": ipspPeerIdAddressType,
       "ipspPeerIdAddress": ipspPeerIdAddress,
       "ipspPeerIdCredentialName": ipspPeerIdCredentialName,
       "ipspPeerIdLastChanged": ipspPeerIdLastChanged,
       "ipspPeerIdStorageType": ipspPeerIdStorageType,
       "ipspPeerIdRowStatus": ipspPeerIdRowStatus,
       "ipspAutostartIkeTable": ipspAutostartIkeTable,
       "ipspAutostartIkeEntry": ipspAutostartIkeEntry,
       "ipspAutoIkePriority": ipspAutoIkePriority,
       "ipspAutoIkeAction": ipspAutoIkeAction,
       "ipspAutoIkeAddressType": ipspAutoIkeAddressType,
       "ipspAutoIkeSourceAddress": ipspAutoIkeSourceAddress,
       "ipspAutoIkeSourcePort": ipspAutoIkeSourcePort,
       "ipspAutoIkeDestAddress": ipspAutoIkeDestAddress,
       "ipspAutoIkeDestPort": ipspAutoIkeDestPort,
       "ipspAutoIkeProtocol": ipspAutoIkeProtocol,
       "ipspAutoIkeLastChanged": ipspAutoIkeLastChanged,
       "ipspAutoIkeStorageType": ipspAutoIkeStorageType,
       "ipspAutoIkeRowStatus": ipspAutoIkeRowStatus,
       "ipspIpsecCredMngServiceTable": ipspIpsecCredMngServiceTable,
       "ipspIpsecCredMngServiceEntry": ipspIpsecCredMngServiceEntry,
       "ipspIcmsName": ipspIcmsName,
       "ipspIcmsDistinguishedName": ipspIcmsDistinguishedName,
       "ipspIcmsPolicyStatement": ipspIcmsPolicyStatement,
       "ipspIcmsMaxChainLength": ipspIcmsMaxChainLength,
       "ipspIcmsCredentialName": ipspIcmsCredentialName,
       "ipspIcmsLastChanged": ipspIcmsLastChanged,
       "ipspIcmsStorageType": ipspIcmsStorageType,
       "ipspIcmsRowStatus": ipspIcmsRowStatus,
       "ipspCredMngCRLTable": ipspCredMngCRLTable,
       "ipspCredMngCRLEntry": ipspCredMngCRLEntry,
       "ipspCmcCRLName": ipspCmcCRLName,
       "ipspCmcDistributionPoint": ipspCmcDistributionPoint,
       "ipspCmcThisUpdate": ipspCmcThisUpdate,
       "ipspCmcNextUpdate": ipspCmcNextUpdate,
       "ipspCmcLastChanged": ipspCmcLastChanged,
       "ipspCmcStorageType": ipspCmcStorageType,
       "ipspCmcRowStatus": ipspCmcRowStatus,
       "ipspRevokedCertificateTable": ipspRevokedCertificateTable,
       "ipspRevokedCertificateEntry": ipspRevokedCertificateEntry,
       "ipspRctCertSerialNumber": ipspRctCertSerialNumber,
       "ipspRctRevokedDate": ipspRctRevokedDate,
       "ipspRctRevokedReason": ipspRctRevokedReason,
       "ipspRctLastChanged": ipspRctLastChanged,
       "ipspRctStorageType": ipspRctStorageType,
       "ipspRctRowStatus": ipspRctRowStatus,
       "ipspCredentialTable": ipspCredentialTable,
       "ipspCredentialEntry": ipspCredentialEntry,
       "ipspCredName": ipspCredName,
       "ipspCredType": ipspCredType,
       "ipspCredCredential": ipspCredCredential,
       "ipspCredSize": ipspCredSize,
       "ipspCredMngName": ipspCredMngName,
       "ipspCredRemoteID": ipspCredRemoteID,
       "ipspCredAdminStatus": ipspCredAdminStatus,
       "ipspCredLastChanged": ipspCredLastChanged,
       "ipspCredStorageType": ipspCredStorageType,
       "ipspCredRowStatus": ipspCredRowStatus,
       "ipspCredentialSegmentTable": ipspCredentialSegmentTable,
       "ipspCredentialSegmentEntry": ipspCredentialSegmentEntry,
       "ipspCredSegIndex": ipspCredSegIndex,
       "ipspCredSegValue": ipspCredSegValue,
       "ipspCredSegLastChanged": ipspCredSegLastChanged,
       "ipspCredSegStorageType": ipspCredSegStorageType,
       "ipspCredSegRowStatus": ipspCredSegRowStatus,
       "ipspNotificationObjects": ipspNotificationObjects,
       "ipspNotifications": ipspNotifications,
       "ipspActionNotification": ipspActionNotification,
       "ipspPacketNotification": ipspPacketNotification,
       "ipspNotificationVariables": ipspNotificationVariables,
       "ipspActionExecuted": ipspActionExecuted,
       "ipspIPInterfaceType": ipspIPInterfaceType,
       "ipspIPInterfaceAddress": ipspIPInterfaceAddress,
       "ipspIPSourceType": ipspIPSourceType,
       "ipspIPSourceAddress": ipspIPSourceAddress,
       "ipspIPDestinationType": ipspIPDestinationType,
       "ipspIPDestinationAddress": ipspIPDestinationAddress,
       "ipspPacketDirection": ipspPacketDirection,
       "ipspPacketPart": ipspPacketPart,
       "ipspConformanceObjects": ipspConformanceObjects,
       "ipspCompliances": ipspCompliances,
       "ipspRuleFilterCompliance": ipspRuleFilterCompliance,
       "ipspIPsecCompliance": ipspIPsecCompliance,
       "ipspIKECompliance": ipspIKECompliance,
       "ipspLoggingCompliance": ipspLoggingCompliance,
       "ipspGroups": ipspGroups,
       "ipspEndpointGroup": ipspEndpointGroup,
       "ipspGroupContentsGroup": ipspGroupContentsGroup,
       "ipspIpsecSystemPolicyNameGroup": ipspIpsecSystemPolicyNameGroup,
       "ipspRuleDefinitionGroup": ipspRuleDefinitionGroup,
       "ipspCompoundFilterGroup": ipspCompoundFilterGroup,
       "ipspStaticFilterGroup": ipspStaticFilterGroup,
       "ipspIPHeaderFilterGroup": ipspIPHeaderFilterGroup,
       "ipspIPOffsetFilterGroup": ipspIPOffsetFilterGroup,
       "ipspTimeFilterGroup": ipspTimeFilterGroup,
       "ipspIpsoHeaderFilterGroup": ipspIpsoHeaderFilterGroup,
       "ipspCredentialFilterGroup": ipspCredentialFilterGroup,
       "ipspPeerIdFilterGroup": ipspPeerIdFilterGroup,
       "ipspCompoundActionGroup": ipspCompoundActionGroup,
       "ipspPreconfiguredGroup": ipspPreconfiguredGroup,
       "ipspStaticActionGroup": ipspStaticActionGroup,
       "ipspIpsecGroup": ipspIpsecGroup,
       "ipspIkeGroup": ipspIkeGroup,
       "ipspActionLoggingObjectGroup": ipspActionLoggingObjectGroup,
       "ipspActionNotificationGroup": ipspActionNotificationGroup}
)
