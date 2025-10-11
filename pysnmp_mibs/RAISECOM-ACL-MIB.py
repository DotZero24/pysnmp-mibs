# SNMP MIB module (RAISECOM-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:13 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

raisecomAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomIpAccessList_ObjectIdentity = ObjectIdentity
raisecomIpAccessList = _RaisecomIpAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1)
)
_RaisecomIpAclTable_Object = MibTable
raisecomIpAclTable = _RaisecomIpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    raisecomIpAclTable.setStatus("current")
_RaisecomIpAclEntry_Object = MibTableRow
raisecomIpAclEntry = _RaisecomIpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1)
)
raisecomIpAclEntry.setIndexNames(
    (0, "RAISECOM-ACL-MIB", "raisecomIpAclNumber"),
)
if mibBuilder.loadTexts:
    raisecomIpAclEntry.setStatus("current")


class _RaisecomIpAclNumber_Type(Integer32):
    """Custom type raisecomIpAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_RaisecomIpAclNumber_Type.__name__ = "Integer32"
_RaisecomIpAclNumber_Object = MibTableColumn
raisecomIpAclNumber = _RaisecomIpAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 1),
    _RaisecomIpAclNumber_Type()
)
raisecomIpAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIpAclNumber.setStatus("current")


class _RaisecomIpAclAccessType_Type(Integer32):
    """Custom type raisecomIpAclAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RaisecomIpAclAccessType_Type.__name__ = "Integer32"
_RaisecomIpAclAccessType_Object = MibTableColumn
raisecomIpAclAccessType = _RaisecomIpAclAccessType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 2),
    _RaisecomIpAclAccessType_Type()
)
raisecomIpAclAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclAccessType.setStatus("current")


class _RaisecomIpAclProtocol_Type(Integer32):
    """Custom type raisecomIpAclProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomIpAclProtocol_Type.__name__ = "Integer32"
_RaisecomIpAclProtocol_Object = MibTableColumn
raisecomIpAclProtocol = _RaisecomIpAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 3),
    _RaisecomIpAclProtocol_Type()
)
raisecomIpAclProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclProtocol.setStatus("current")
_RaisecomIpAclSourceAddress_Type = IpAddress
_RaisecomIpAclSourceAddress_Object = MibTableColumn
raisecomIpAclSourceAddress = _RaisecomIpAclSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 4),
    _RaisecomIpAclSourceAddress_Type()
)
raisecomIpAclSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclSourceAddress.setStatus("current")
_RaisecomIpAclSourceMask_Type = IpAddress
_RaisecomIpAclSourceMask_Object = MibTableColumn
raisecomIpAclSourceMask = _RaisecomIpAclSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 5),
    _RaisecomIpAclSourceMask_Type()
)
raisecomIpAclSourceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclSourceMask.setStatus("current")


class _RaisecomIpAclSourceProtocolPort_Type(Integer32):
    """Custom type raisecomIpAclSourceProtocolPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomIpAclSourceProtocolPort_Type.__name__ = "Integer32"
_RaisecomIpAclSourceProtocolPort_Object = MibTableColumn
raisecomIpAclSourceProtocolPort = _RaisecomIpAclSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 6),
    _RaisecomIpAclSourceProtocolPort_Type()
)
raisecomIpAclSourceProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclSourceProtocolPort.setStatus("current")
_RaisecomIpAclDestinationAddress_Type = IpAddress
_RaisecomIpAclDestinationAddress_Object = MibTableColumn
raisecomIpAclDestinationAddress = _RaisecomIpAclDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 7),
    _RaisecomIpAclDestinationAddress_Type()
)
raisecomIpAclDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclDestinationAddress.setStatus("current")
_RaisecomIpAclDestinationMask_Type = IpAddress
_RaisecomIpAclDestinationMask_Object = MibTableColumn
raisecomIpAclDestinationMask = _RaisecomIpAclDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 8),
    _RaisecomIpAclDestinationMask_Type()
)
raisecomIpAclDestinationMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclDestinationMask.setStatus("current")


class _RaisecomIpAclDestinationProtocolPort_Type(Integer32):
    """Custom type raisecomIpAclDestinationProtocolPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomIpAclDestinationProtocolPort_Type.__name__ = "Integer32"
_RaisecomIpAclDestinationProtocolPort_Object = MibTableColumn
raisecomIpAclDestinationProtocolPort = _RaisecomIpAclDestinationProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 9),
    _RaisecomIpAclDestinationProtocolPort_Type()
)
raisecomIpAclDestinationProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclDestinationProtocolPort.setStatus("current")
_RaisecomIpAclRef_Type = Gauge32
_RaisecomIpAclRef_Object = MibTableColumn
raisecomIpAclRef = _RaisecomIpAclRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 10),
    _RaisecomIpAclRef_Type()
)
raisecomIpAclRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIpAclRef.setStatus("current")
_RaisecomIpAclStatus_Type = RowStatus
_RaisecomIpAclStatus_Object = MibTableColumn
raisecomIpAclStatus = _RaisecomIpAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 11),
    _RaisecomIpAclStatus_Type()
)
raisecomIpAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclStatus.setStatus("current")
_RaisecomIpAclSetFlag_Type = Unsigned32
_RaisecomIpAclSetFlag_Object = MibTableColumn
raisecomIpAclSetFlag = _RaisecomIpAclSetFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 1, 1, 1, 12),
    _RaisecomIpAclSetFlag_Type()
)
raisecomIpAclSetFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpAclSetFlag.setStatus("current")
_RaisecomMacAccessList_ObjectIdentity = ObjectIdentity
raisecomMacAccessList = _RaisecomMacAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2)
)
_RaisecomMacAclTable_Object = MibTable
raisecomMacAclTable = _RaisecomMacAclTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomMacAclTable.setStatus("current")
_RaisecomMacAclEntry_Object = MibTableRow
raisecomMacAclEntry = _RaisecomMacAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1)
)
raisecomMacAclEntry.setIndexNames(
    (0, "RAISECOM-ACL-MIB", "raisecomMacAclNumber"),
)
if mibBuilder.loadTexts:
    raisecomMacAclEntry.setStatus("current")


class _RaisecomMacAclNumber_Type(Integer32):
    """Custom type raisecomMacAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_RaisecomMacAclNumber_Type.__name__ = "Integer32"
_RaisecomMacAclNumber_Object = MibTableColumn
raisecomMacAclNumber = _RaisecomMacAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 1),
    _RaisecomMacAclNumber_Type()
)
raisecomMacAclNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMacAclNumber.setStatus("current")


class _RaisecomMacAclAccessType_Type(Integer32):
    """Custom type raisecomMacAclAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RaisecomMacAclAccessType_Type.__name__ = "Integer32"
_RaisecomMacAclAccessType_Object = MibTableColumn
raisecomMacAclAccessType = _RaisecomMacAclAccessType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 2),
    _RaisecomMacAclAccessType_Type()
)
raisecomMacAclAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMacAclAccessType.setStatus("current")
_RaisecomMacAclProtocol_Type = Integer32
_RaisecomMacAclProtocol_Object = MibTableColumn
raisecomMacAclProtocol = _RaisecomMacAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 3),
    _RaisecomMacAclProtocol_Type()
)
raisecomMacAclProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMacAclProtocol.setStatus("current")
_RaisecomMacAclSourceAddress_Type = MacAddress
_RaisecomMacAclSourceAddress_Object = MibTableColumn
raisecomMacAclSourceAddress = _RaisecomMacAclSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 4),
    _RaisecomMacAclSourceAddress_Type()
)
raisecomMacAclSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMacAclSourceAddress.setStatus("current")
_RaisecomMacAclSourceMask_Type = MacAddress
_RaisecomMacAclSourceMask_Object = MibTableColumn
raisecomMacAclSourceMask = _RaisecomMacAclSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 5),
    _RaisecomMacAclSourceMask_Type()
)
raisecomMacAclSourceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMacAclSourceMask.setStatus("current")
_RaisecomMacAclDestinationAddress_Type = MacAddress
_RaisecomMacAclDestinationAddress_Object = MibTableColumn
raisecomMacAclDestinationAddress = _RaisecomMacAclDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 6),
    _RaisecomMacAclDestinationAddress_Type()
)
raisecomMacAclDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMacAclDestinationAddress.setStatus("current")
_RaisecomMacAclDestinationMask_Type = MacAddress
_RaisecomMacAclDestinationMask_Object = MibTableColumn
raisecomMacAclDestinationMask = _RaisecomMacAclDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 7),
    _RaisecomMacAclDestinationMask_Type()
)
raisecomMacAclDestinationMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMacAclDestinationMask.setStatus("current")
_RaisecomMacAclRef_Type = Gauge32
_RaisecomMacAclRef_Object = MibTableColumn
raisecomMacAclRef = _RaisecomMacAclRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 8),
    _RaisecomMacAclRef_Type()
)
raisecomMacAclRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMacAclRef.setStatus("current")
_RaisecomMacAclStatus_Type = RowStatus
_RaisecomMacAclStatus_Object = MibTableColumn
raisecomMacAclStatus = _RaisecomMacAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 9),
    _RaisecomMacAclStatus_Type()
)
raisecomMacAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMacAclStatus.setStatus("current")
_RaisecomMacAclSetFlag_Type = Unsigned32
_RaisecomMacAclSetFlag_Object = MibTableColumn
raisecomMacAclSetFlag = _RaisecomMacAclSetFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 2, 1, 1, 10),
    _RaisecomMacAclSetFlag_Type()
)
raisecomMacAclSetFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomMacAclSetFlag.setStatus("current")
_RaisecomUserAccessList_ObjectIdentity = ObjectIdentity
raisecomUserAccessList = _RaisecomUserAccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3)
)
_RaisecomUserAclTable_Object = MibTable
raisecomUserAclTable = _RaisecomUserAclTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    raisecomUserAclTable.setStatus("current")
_RaisecomUserAclEntry_Object = MibTableRow
raisecomUserAclEntry = _RaisecomUserAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1)
)
raisecomUserAclEntry.setIndexNames(
    (0, "RAISECOM-ACL-MIB", "raisecomUserAclNumber"),
)
if mibBuilder.loadTexts:
    raisecomUserAclEntry.setStatus("current")


class _RaisecomUserAclNumber_Type(Integer32):
    """Custom type raisecomUserAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_RaisecomUserAclNumber_Type.__name__ = "Integer32"
_RaisecomUserAclNumber_Object = MibTableColumn
raisecomUserAclNumber = _RaisecomUserAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 1),
    _RaisecomUserAclNumber_Type()
)
raisecomUserAclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomUserAclNumber.setStatus("current")


class _RaisecomUserAclAccessType_Type(Integer32):
    """Custom type raisecomUserAclAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RaisecomUserAclAccessType_Type.__name__ = "Integer32"
_RaisecomUserAclAccessType_Object = MibTableColumn
raisecomUserAclAccessType = _RaisecomUserAclAccessType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 2),
    _RaisecomUserAclAccessType_Type()
)
raisecomUserAclAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclAccessType.setStatus("current")


class _RaisecomUserAclRuleString_Type(OctetString):
    """Custom type raisecomUserAclRuleString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RaisecomUserAclRuleString_Type.__name__ = "OctetString"
_RaisecomUserAclRuleString_Object = MibTableColumn
raisecomUserAclRuleString = _RaisecomUserAclRuleString_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 3),
    _RaisecomUserAclRuleString_Type()
)
raisecomUserAclRuleString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclRuleString.setStatus("current")


class _RaisecomUserAclRuleMask_Type(OctetString):
    """Custom type raisecomUserAclRuleMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RaisecomUserAclRuleMask_Type.__name__ = "OctetString"
_RaisecomUserAclRuleMask_Object = MibTableColumn
raisecomUserAclRuleMask = _RaisecomUserAclRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 4),
    _RaisecomUserAclRuleMask_Type()
)
raisecomUserAclRuleMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclRuleMask.setStatus("current")


class _RaisecomUserAclOffset_Type(Integer32):
    """Custom type raisecomUserAclOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RaisecomUserAclOffset_Type.__name__ = "Integer32"
_RaisecomUserAclOffset_Object = MibTableColumn
raisecomUserAclOffset = _RaisecomUserAclOffset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 5),
    _RaisecomUserAclOffset_Type()
)
raisecomUserAclOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclOffset.setStatus("current")
_RaisecomUserAclRef_Type = Gauge32
_RaisecomUserAclRef_Object = MibTableColumn
raisecomUserAclRef = _RaisecomUserAclRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 6),
    _RaisecomUserAclRef_Type()
)
raisecomUserAclRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomUserAclRef.setStatus("current")
_RaisecomUserAclStatus_Type = RowStatus
_RaisecomUserAclStatus_Object = MibTableColumn
raisecomUserAclStatus = _RaisecomUserAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 7),
    _RaisecomUserAclStatus_Type()
)
raisecomUserAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclStatus.setStatus("current")
_RaisecomUserAclSourceMacAddress_Type = MacAddress
_RaisecomUserAclSourceMacAddress_Object = MibTableColumn
raisecomUserAclSourceMacAddress = _RaisecomUserAclSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 8),
    _RaisecomUserAclSourceMacAddress_Type()
)
raisecomUserAclSourceMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclSourceMacAddress.setStatus("current")
_RaisecomUserAclDestinationMacAddress_Type = MacAddress
_RaisecomUserAclDestinationMacAddress_Object = MibTableColumn
raisecomUserAclDestinationMacAddress = _RaisecomUserAclDestinationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 9),
    _RaisecomUserAclDestinationMacAddress_Type()
)
raisecomUserAclDestinationMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclDestinationMacAddress.setStatus("current")
_RaisecomUserAclEtherType_Type = Integer32
_RaisecomUserAclEtherType_Object = MibTableColumn
raisecomUserAclEtherType = _RaisecomUserAclEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 10),
    _RaisecomUserAclEtherType_Type()
)
raisecomUserAclEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclEtherType.setStatus("current")
_RaisecomUserAclEtherTypeMask_Type = Integer32
_RaisecomUserAclEtherTypeMask_Object = MibTableColumn
raisecomUserAclEtherTypeMask = _RaisecomUserAclEtherTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 11),
    _RaisecomUserAclEtherTypeMask_Type()
)
raisecomUserAclEtherTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclEtherTypeMask.setStatus("current")
_RaisecomUserAclSourceIpAddress_Type = IpAddress
_RaisecomUserAclSourceIpAddress_Object = MibTableColumn
raisecomUserAclSourceIpAddress = _RaisecomUserAclSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 12),
    _RaisecomUserAclSourceIpAddress_Type()
)
raisecomUserAclSourceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclSourceIpAddress.setStatus("current")
_RaisecomUserAclSourceIpMask_Type = IpAddress
_RaisecomUserAclSourceIpMask_Object = MibTableColumn
raisecomUserAclSourceIpMask = _RaisecomUserAclSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 13),
    _RaisecomUserAclSourceIpMask_Type()
)
raisecomUserAclSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclSourceIpMask.setStatus("current")
_RaisecomUserAclDestinationIpAddress_Type = IpAddress
_RaisecomUserAclDestinationIpAddress_Object = MibTableColumn
raisecomUserAclDestinationIpAddress = _RaisecomUserAclDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 14),
    _RaisecomUserAclDestinationIpAddress_Type()
)
raisecomUserAclDestinationIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclDestinationIpAddress.setStatus("current")
_RaisecomUserAclDestinationIpMask_Type = IpAddress
_RaisecomUserAclDestinationIpMask_Object = MibTableColumn
raisecomUserAclDestinationIpMask = _RaisecomUserAclDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 15),
    _RaisecomUserAclDestinationIpMask_Type()
)
raisecomUserAclDestinationIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclDestinationIpMask.setStatus("current")


class _RaisecomUserAclIpPrecedence_Type(Integer32):
    """Custom type raisecomUserAclIpPrecedence based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("routine", 0),
          ("priority", 1),
          ("immediate", 2),
          ("flash", 3),
          ("flash-override", 4),
          ("critical", 5),
          ("internet", 6),
          ("network", 7))
    )


_RaisecomUserAclIpPrecedence_Type.__name__ = "Integer32"
_RaisecomUserAclIpPrecedence_Object = MibTableColumn
raisecomUserAclIpPrecedence = _RaisecomUserAclIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 16),
    _RaisecomUserAclIpPrecedence_Type()
)
raisecomUserAclIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpPrecedence.setStatus("current")


class _RaisecomUserAclIpTos_Type(Integer32):
    """Custom type raisecomUserAclIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RaisecomUserAclIpTos_Type.__name__ = "Integer32"
_RaisecomUserAclIpTos_Object = MibTableColumn
raisecomUserAclIpTos = _RaisecomUserAclIpTos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 17),
    _RaisecomUserAclIpTos_Type()
)
raisecomUserAclIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpTos.setStatus("current")


class _RaisecomUserAclIpDscp_Type(Integer32):
    """Custom type raisecomUserAclIpDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RaisecomUserAclIpDscp_Type.__name__ = "Integer32"
_RaisecomUserAclIpDscp_Object = MibTableColumn
raisecomUserAclIpDscp = _RaisecomUserAclIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 18),
    _RaisecomUserAclIpDscp_Type()
)
raisecomUserAclIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpDscp.setStatus("current")


class _RaisecomUserAclIpFragmentsFlag_Type(Integer32):
    """Custom type raisecomUserAclIpFragmentsFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofragments", 0),
          ("fragments", 1))
    )


_RaisecomUserAclIpFragmentsFlag_Type.__name__ = "Integer32"
_RaisecomUserAclIpFragmentsFlag_Object = MibTableColumn
raisecomUserAclIpFragmentsFlag = _RaisecomUserAclIpFragmentsFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 19),
    _RaisecomUserAclIpFragmentsFlag_Type()
)
raisecomUserAclIpFragmentsFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpFragmentsFlag.setStatus("current")


class _RaisecomUserAclIpProtocol_Type(Integer32):
    """Custom type raisecomUserAclIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomUserAclIpProtocol_Type.__name__ = "Integer32"
_RaisecomUserAclIpProtocol_Object = MibTableColumn
raisecomUserAclIpProtocol = _RaisecomUserAclIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 20),
    _RaisecomUserAclIpProtocol_Type()
)
raisecomUserAclIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpProtocol.setStatus("current")


class _RaisecomUserAclSourceProtocolPort_Type(Integer32):
    """Custom type raisecomUserAclSourceProtocolPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomUserAclSourceProtocolPort_Type.__name__ = "Integer32"
_RaisecomUserAclSourceProtocolPort_Object = MibTableColumn
raisecomUserAclSourceProtocolPort = _RaisecomUserAclSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 21),
    _RaisecomUserAclSourceProtocolPort_Type()
)
raisecomUserAclSourceProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclSourceProtocolPort.setStatus("current")


class _RaisecomUserAclDestinationProtocolPort_Type(Integer32):
    """Custom type raisecomUserAclDestinationProtocolPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomUserAclDestinationProtocolPort_Type.__name__ = "Integer32"
_RaisecomUserAclDestinationProtocolPort_Object = MibTableColumn
raisecomUserAclDestinationProtocolPort = _RaisecomUserAclDestinationProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 22),
    _RaisecomUserAclDestinationProtocolPort_Type()
)
raisecomUserAclDestinationProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclDestinationProtocolPort.setStatus("current")


class _RaisecomUserAclTcpProtocolFlag_Type(Integer32):
    """Custom type raisecomUserAclTcpProtocolFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RaisecomUserAclTcpProtocolFlag_Type.__name__ = "Integer32"
_RaisecomUserAclTcpProtocolFlag_Object = MibTableColumn
raisecomUserAclTcpProtocolFlag = _RaisecomUserAclTcpProtocolFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 23),
    _RaisecomUserAclTcpProtocolFlag_Type()
)
raisecomUserAclTcpProtocolFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclTcpProtocolFlag.setStatus("current")


class _RaisecomUserAclCvlanCos_Type(Integer32):
    """Custom type raisecomUserAclCvlanCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomUserAclCvlanCos_Type.__name__ = "Integer32"
_RaisecomUserAclCvlanCos_Object = MibTableColumn
raisecomUserAclCvlanCos = _RaisecomUserAclCvlanCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 24),
    _RaisecomUserAclCvlanCos_Type()
)
raisecomUserAclCvlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclCvlanCos.setStatus("current")


class _RaisecomUserAclSvlanCos_Type(Integer32):
    """Custom type raisecomUserAclSvlanCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomUserAclSvlanCos_Type.__name__ = "Integer32"
_RaisecomUserAclSvlanCos_Object = MibTableColumn
raisecomUserAclSvlanCos = _RaisecomUserAclSvlanCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 25),
    _RaisecomUserAclSvlanCos_Type()
)
raisecomUserAclSvlanCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclSvlanCos.setStatus("current")


class _RaisecomUserAclCvlan_Type(Integer32):
    """Custom type raisecomUserAclCvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomUserAclCvlan_Type.__name__ = "Integer32"
_RaisecomUserAclCvlan_Object = MibTableColumn
raisecomUserAclCvlan = _RaisecomUserAclCvlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 26),
    _RaisecomUserAclCvlan_Type()
)
raisecomUserAclCvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclCvlan.setStatus("current")


class _RaisecomUserAclSvlan_Type(Integer32):
    """Custom type raisecomUserAclSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomUserAclSvlan_Type.__name__ = "Integer32"
_RaisecomUserAclSvlan_Object = MibTableColumn
raisecomUserAclSvlan = _RaisecomUserAclSvlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 27),
    _RaisecomUserAclSvlan_Type()
)
raisecomUserAclSvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclSvlan.setStatus("current")
_RaisecomUserAclSetFlag_Type = Unsigned32
_RaisecomUserAclSetFlag_Object = MibTableColumn
raisecomUserAclSetFlag = _RaisecomUserAclSetFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 28),
    _RaisecomUserAclSetFlag_Type()
)
raisecomUserAclSetFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclSetFlag.setStatus("current")
_RaisecomUserAclSourceMacMask_Type = MacAddress
_RaisecomUserAclSourceMacMask_Object = MibTableColumn
raisecomUserAclSourceMacMask = _RaisecomUserAclSourceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 29),
    _RaisecomUserAclSourceMacMask_Type()
)
raisecomUserAclSourceMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclSourceMacMask.setStatus("current")
_RaisecomUserAclDestinationMacMask_Type = MacAddress
_RaisecomUserAclDestinationMacMask_Object = MibTableColumn
raisecomUserAclDestinationMacMask = _RaisecomUserAclDestinationMacMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 30),
    _RaisecomUserAclDestinationMacMask_Type()
)
raisecomUserAclDestinationMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclDestinationMacMask.setStatus("current")


class _RaisecomUserAclCos_Type(Integer32):
    """Custom type raisecomUserAclCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomUserAclCos_Type.__name__ = "Integer32"
_RaisecomUserAclCos_Object = MibTableColumn
raisecomUserAclCos = _RaisecomUserAclCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 31),
    _RaisecomUserAclCos_Type()
)
raisecomUserAclCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclCos.setStatus("current")


class _RaisecomUserAclArpType_Type(Integer32):
    """Custom type raisecomUserAclArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("reply", 2))
    )


_RaisecomUserAclArpType_Type.__name__ = "Integer32"
_RaisecomUserAclArpType_Object = MibTableColumn
raisecomUserAclArpType = _RaisecomUserAclArpType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 32),
    _RaisecomUserAclArpType_Type()
)
raisecomUserAclArpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclArpType.setStatus("current")
_RaisecomUserAclArpSenderMac_Type = MacAddress
_RaisecomUserAclArpSenderMac_Object = MibTableColumn
raisecomUserAclArpSenderMac = _RaisecomUserAclArpSenderMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 33),
    _RaisecomUserAclArpSenderMac_Type()
)
raisecomUserAclArpSenderMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclArpSenderMac.setStatus("current")
_RaisecomUserAclArpTargetMac_Type = MacAddress
_RaisecomUserAclArpTargetMac_Object = MibTableColumn
raisecomUserAclArpTargetMac = _RaisecomUserAclArpTargetMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 34),
    _RaisecomUserAclArpTargetMac_Type()
)
raisecomUserAclArpTargetMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclArpTargetMac.setStatus("current")


class _RaisecomUserAclIcmpIgmpType_Type(Integer32):
    """Custom type raisecomUserAclIcmpIgmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomUserAclIcmpIgmpType_Type.__name__ = "Integer32"
_RaisecomUserAclIcmpIgmpType_Object = MibTableColumn
raisecomUserAclIcmpIgmpType = _RaisecomUserAclIcmpIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 35),
    _RaisecomUserAclIcmpIgmpType_Type()
)
raisecomUserAclIcmpIgmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIcmpIgmpType.setStatus("current")


class _RaisecomUserAclIcmpCode_Type(Integer32):
    """Custom type raisecomUserAclIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomUserAclIcmpCode_Type.__name__ = "Integer32"
_RaisecomUserAclIcmpCode_Object = MibTableColumn
raisecomUserAclIcmpCode = _RaisecomUserAclIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 36),
    _RaisecomUserAclIcmpCode_Type()
)
raisecomUserAclIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIcmpCode.setStatus("current")
_RaisecomUserAclIpv6SourceAddress_Type = Ipv6Address
_RaisecomUserAclIpv6SourceAddress_Object = MibTableColumn
raisecomUserAclIpv6SourceAddress = _RaisecomUserAclIpv6SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 37),
    _RaisecomUserAclIpv6SourceAddress_Type()
)
raisecomUserAclIpv6SourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpv6SourceAddress.setStatus("current")
_RaisecomUserAclIpv6SourceMask_Type = Ipv6Address
_RaisecomUserAclIpv6SourceMask_Object = MibTableColumn
raisecomUserAclIpv6SourceMask = _RaisecomUserAclIpv6SourceMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 38),
    _RaisecomUserAclIpv6SourceMask_Type()
)
raisecomUserAclIpv6SourceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpv6SourceMask.setStatus("current")
_RaisecomUserAclIpv6DestinationAddress_Type = Ipv6Address
_RaisecomUserAclIpv6DestinationAddress_Object = MibTableColumn
raisecomUserAclIpv6DestinationAddress = _RaisecomUserAclIpv6DestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 39),
    _RaisecomUserAclIpv6DestinationAddress_Type()
)
raisecomUserAclIpv6DestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpv6DestinationAddress.setStatus("current")
_RaisecomUserAclIpv6DestinationMask_Type = Ipv6Address
_RaisecomUserAclIpv6DestinationMask_Object = MibTableColumn
raisecomUserAclIpv6DestinationMask = _RaisecomUserAclIpv6DestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 40),
    _RaisecomUserAclIpv6DestinationMask_Type()
)
raisecomUserAclIpv6DestinationMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpv6DestinationMask.setStatus("current")
_RaisecomUserAclIpv6SourceMaskLen_Type = Integer32
_RaisecomUserAclIpv6SourceMaskLen_Object = MibTableColumn
raisecomUserAclIpv6SourceMaskLen = _RaisecomUserAclIpv6SourceMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 41),
    _RaisecomUserAclIpv6SourceMaskLen_Type()
)
raisecomUserAclIpv6SourceMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpv6SourceMaskLen.setStatus("current")
_RaisecomUserAclIpv6DestinationMaskLen_Type = Integer32
_RaisecomUserAclIpv6DestinationMaskLen_Object = MibTableColumn
raisecomUserAclIpv6DestinationMaskLen = _RaisecomUserAclIpv6DestinationMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 42),
    _RaisecomUserAclIpv6DestinationMaskLen_Type()
)
raisecomUserAclIpv6DestinationMaskLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpv6DestinationMaskLen.setStatus("current")


class _RaisecomUserAclIpv6Protocol_Type(Integer32):
    """Custom type raisecomUserAclIpv6Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomUserAclIpv6Protocol_Type.__name__ = "Integer32"
_RaisecomUserAclIpv6Protocol_Object = MibTableColumn
raisecomUserAclIpv6Protocol = _RaisecomUserAclIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 43),
    _RaisecomUserAclIpv6Protocol_Type()
)
raisecomUserAclIpv6Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpv6Protocol.setStatus("current")
_RaisecomUserAclIpv6FlowLabel_Type = Integer32
_RaisecomUserAclIpv6FlowLabel_Object = MibTableColumn
raisecomUserAclIpv6FlowLabel = _RaisecomUserAclIpv6FlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 44),
    _RaisecomUserAclIpv6FlowLabel_Type()
)
raisecomUserAclIpv6FlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpv6FlowLabel.setStatus("current")


class _RaisecomUserAclIpv6TrafficClass_Type(Integer32):
    """Custom type raisecomUserAclIpv6TrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(130,
              131,
              132)
        )
    )
    namedValues = NamedValues(
        *(("mld-query", 130),
          ("mld-report", 131),
          ("mld-done", 132))
    )


_RaisecomUserAclIpv6TrafficClass_Type.__name__ = "Integer32"
_RaisecomUserAclIpv6TrafficClass_Object = MibTableColumn
raisecomUserAclIpv6TrafficClass = _RaisecomUserAclIpv6TrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 45),
    _RaisecomUserAclIpv6TrafficClass_Type()
)
raisecomUserAclIpv6TrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIpv6TrafficClass.setStatus("current")


class _RaisecomUserAclIcmpv6Type_Type(Integer32):
    """Custom type raisecomUserAclIcmpv6Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomUserAclIcmpv6Type_Type.__name__ = "Integer32"
_RaisecomUserAclIcmpv6Type_Object = MibTableColumn
raisecomUserAclIcmpv6Type = _RaisecomUserAclIcmpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 46),
    _RaisecomUserAclIcmpv6Type_Type()
)
raisecomUserAclIcmpv6Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclIcmpv6Type.setStatus("current")
_RaisecomUserAclUserLen_Type = Integer32
_RaisecomUserAclUserLen_Object = MibTableColumn
raisecomUserAclUserLen = _RaisecomUserAclUserLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 47),
    _RaisecomUserAclUserLen_Type()
)
raisecomUserAclUserLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomUserAclUserLen.setStatus("current")


class _RaisecomUserAclExtensionSetFlag_Type(OctetString):
    """Custom type raisecomUserAclExtensionSetFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RaisecomUserAclExtensionSetFlag_Type.__name__ = "OctetString"
_RaisecomUserAclExtensionSetFlag_Object = MibTableColumn
raisecomUserAclExtensionSetFlag = _RaisecomUserAclExtensionSetFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 48),
    _RaisecomUserAclExtensionSetFlag_Type()
)
raisecomUserAclExtensionSetFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclExtensionSetFlag.setStatus("current")


class _RaisecomUserAclTunnelLabel_Type(Integer32):
    """Custom type raisecomUserAclTunnelLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_RaisecomUserAclTunnelLabel_Type.__name__ = "Integer32"
_RaisecomUserAclTunnelLabel_Object = MibTableColumn
raisecomUserAclTunnelLabel = _RaisecomUserAclTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 49),
    _RaisecomUserAclTunnelLabel_Type()
)
raisecomUserAclTunnelLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclTunnelLabel.setStatus("current")


class _RaisecomUserAclTunnelExp_Type(Integer32):
    """Custom type raisecomUserAclTunnelExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomUserAclTunnelExp_Type.__name__ = "Integer32"
_RaisecomUserAclTunnelExp_Object = MibTableColumn
raisecomUserAclTunnelExp = _RaisecomUserAclTunnelExp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 50),
    _RaisecomUserAclTunnelExp_Type()
)
raisecomUserAclTunnelExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclTunnelExp.setStatus("current")


class _RaisecomUserAclVcLabel_Type(Integer32):
    """Custom type raisecomUserAclVcLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_RaisecomUserAclVcLabel_Type.__name__ = "Integer32"
_RaisecomUserAclVcLabel_Object = MibTableColumn
raisecomUserAclVcLabel = _RaisecomUserAclVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 51),
    _RaisecomUserAclVcLabel_Type()
)
raisecomUserAclVcLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclVcLabel.setStatus("current")


class _RaisecomUserAclVcExp_Type(Integer32):
    """Custom type raisecomUserAclVcExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomUserAclVcExp_Type.__name__ = "Integer32"
_RaisecomUserAclVcExp_Object = MibTableColumn
raisecomUserAclVcExp = _RaisecomUserAclVcExp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 3, 1, 1, 52),
    _RaisecomUserAclVcExp_Type()
)
raisecomUserAclVcExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomUserAclVcExp.setStatus("current")
_RaisecomIpv6AccessList_ObjectIdentity = ObjectIdentity
raisecomIpv6AccessList = _RaisecomIpv6AccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4)
)
_RaisecomIpv6AclTable_Object = MibTable
raisecomIpv6AclTable = _RaisecomIpv6AclTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    raisecomIpv6AclTable.setStatus("current")
_RaisecomIpv6AclEntry_Object = MibTableRow
raisecomIpv6AclEntry = _RaisecomIpv6AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1)
)
raisecomIpv6AclEntry.setIndexNames(
    (0, "RAISECOM-ACL-MIB", "raisecomIpv6AclNumber"),
)
if mibBuilder.loadTexts:
    raisecomIpv6AclEntry.setStatus("current")


class _RaisecomIpv6AclNumber_Type(Integer32):
    """Custom type raisecomIpv6AclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_RaisecomIpv6AclNumber_Type.__name__ = "Integer32"
_RaisecomIpv6AclNumber_Object = MibTableColumn
raisecomIpv6AclNumber = _RaisecomIpv6AclNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 1),
    _RaisecomIpv6AclNumber_Type()
)
raisecomIpv6AclNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomIpv6AclNumber.setStatus("current")


class _RaisecomIpv6AclAccessType_Type(Integer32):
    """Custom type raisecomIpv6AclAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_RaisecomIpv6AclAccessType_Type.__name__ = "Integer32"
_RaisecomIpv6AclAccessType_Object = MibTableColumn
raisecomIpv6AclAccessType = _RaisecomIpv6AclAccessType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 2),
    _RaisecomIpv6AclAccessType_Type()
)
raisecomIpv6AclAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclAccessType.setStatus("current")


class _RaisecomIpv6AclProtocol_Type(Integer32):
    """Custom type raisecomIpv6AclProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomIpv6AclProtocol_Type.__name__ = "Integer32"
_RaisecomIpv6AclProtocol_Object = MibTableColumn
raisecomIpv6AclProtocol = _RaisecomIpv6AclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 3),
    _RaisecomIpv6AclProtocol_Type()
)
raisecomIpv6AclProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclProtocol.setStatus("current")
_RaisecomIpv6AclSourceAddress_Type = Ipv6Address
_RaisecomIpv6AclSourceAddress_Object = MibTableColumn
raisecomIpv6AclSourceAddress = _RaisecomIpv6AclSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 4),
    _RaisecomIpv6AclSourceAddress_Type()
)
raisecomIpv6AclSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclSourceAddress.setStatus("current")


class _RaisecomIpv6AclSourcePrefixLen_Type(Integer32):
    """Custom type raisecomIpv6AclSourcePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RaisecomIpv6AclSourcePrefixLen_Type.__name__ = "Integer32"
_RaisecomIpv6AclSourcePrefixLen_Object = MibTableColumn
raisecomIpv6AclSourcePrefixLen = _RaisecomIpv6AclSourcePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 5),
    _RaisecomIpv6AclSourcePrefixLen_Type()
)
raisecomIpv6AclSourcePrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclSourcePrefixLen.setStatus("current")
_RaisecomIpv6AclDestinationAddress_Type = Ipv6Address
_RaisecomIpv6AclDestinationAddress_Object = MibTableColumn
raisecomIpv6AclDestinationAddress = _RaisecomIpv6AclDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 6),
    _RaisecomIpv6AclDestinationAddress_Type()
)
raisecomIpv6AclDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclDestinationAddress.setStatus("current")


class _RaisecomIpv6AclDestinationPrefixLen_Type(Integer32):
    """Custom type raisecomIpv6AclDestinationPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RaisecomIpv6AclDestinationPrefixLen_Type.__name__ = "Integer32"
_RaisecomIpv6AclDestinationPrefixLen_Object = MibTableColumn
raisecomIpv6AclDestinationPrefixLen = _RaisecomIpv6AclDestinationPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 7),
    _RaisecomIpv6AclDestinationPrefixLen_Type()
)
raisecomIpv6AclDestinationPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclDestinationPrefixLen.setStatus("current")


class _RaisecomIpv6AclTrafficClass_Type(Integer32):
    """Custom type raisecomIpv6AclTrafficClass based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RaisecomIpv6AclTrafficClass_Type.__name__ = "Integer32"
_RaisecomIpv6AclTrafficClass_Object = MibTableColumn
raisecomIpv6AclTrafficClass = _RaisecomIpv6AclTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 8),
    _RaisecomIpv6AclTrafficClass_Type()
)
raisecomIpv6AclTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclTrafficClass.setStatus("current")


class _RaisecomIpv6AclFlowLabel_Type(Integer32):
    """Custom type raisecomIpv6AclFlowLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_RaisecomIpv6AclFlowLabel_Type.__name__ = "Integer32"
_RaisecomIpv6AclFlowLabel_Object = MibTableColumn
raisecomIpv6AclFlowLabel = _RaisecomIpv6AclFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 9),
    _RaisecomIpv6AclFlowLabel_Type()
)
raisecomIpv6AclFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclFlowLabel.setStatus("current")
_RaisecomIpv6AclRef_Type = Gauge32
_RaisecomIpv6AclRef_Object = MibTableColumn
raisecomIpv6AclRef = _RaisecomIpv6AclRef_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 10),
    _RaisecomIpv6AclRef_Type()
)
raisecomIpv6AclRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomIpv6AclRef.setStatus("current")
_RaisecomIpv6AclStatus_Type = RowStatus
_RaisecomIpv6AclStatus_Object = MibTableColumn
raisecomIpv6AclStatus = _RaisecomIpv6AclStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 11),
    _RaisecomIpv6AclStatus_Type()
)
raisecomIpv6AclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclStatus.setStatus("current")


class _RaisecomIpv6AclSourceProtocolPort_Type(Integer32):
    """Custom type raisecomIpv6AclSourceProtocolPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomIpv6AclSourceProtocolPort_Type.__name__ = "Integer32"
_RaisecomIpv6AclSourceProtocolPort_Object = MibTableColumn
raisecomIpv6AclSourceProtocolPort = _RaisecomIpv6AclSourceProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 12),
    _RaisecomIpv6AclSourceProtocolPort_Type()
)
raisecomIpv6AclSourceProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclSourceProtocolPort.setStatus("current")


class _RaisecomIpv6AclDestinationProtocolPort_Type(Integer32):
    """Custom type raisecomIpv6AclDestinationProtocolPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomIpv6AclDestinationProtocolPort_Type.__name__ = "Integer32"
_RaisecomIpv6AclDestinationProtocolPort_Object = MibTableColumn
raisecomIpv6AclDestinationProtocolPort = _RaisecomIpv6AclDestinationProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 13),
    _RaisecomIpv6AclDestinationProtocolPort_Type()
)
raisecomIpv6AclDestinationProtocolPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclDestinationProtocolPort.setStatus("current")
_RaisecomIpv6AclSetFlag_Type = Unsigned32
_RaisecomIpv6AclSetFlag_Object = MibTableColumn
raisecomIpv6AclSetFlag = _RaisecomIpv6AclSetFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 3, 4, 1, 1, 14),
    _RaisecomIpv6AclSetFlag_Type()
)
raisecomIpv6AclSetFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomIpv6AclSetFlag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-ACL-MIB",
    **{"raisecomAcl": raisecomAcl,
       "raisecomIpAccessList": raisecomIpAccessList,
       "raisecomIpAclTable": raisecomIpAclTable,
       "raisecomIpAclEntry": raisecomIpAclEntry,
       "raisecomIpAclNumber": raisecomIpAclNumber,
       "raisecomIpAclAccessType": raisecomIpAclAccessType,
       "raisecomIpAclProtocol": raisecomIpAclProtocol,
       "raisecomIpAclSourceAddress": raisecomIpAclSourceAddress,
       "raisecomIpAclSourceMask": raisecomIpAclSourceMask,
       "raisecomIpAclSourceProtocolPort": raisecomIpAclSourceProtocolPort,
       "raisecomIpAclDestinationAddress": raisecomIpAclDestinationAddress,
       "raisecomIpAclDestinationMask": raisecomIpAclDestinationMask,
       "raisecomIpAclDestinationProtocolPort": raisecomIpAclDestinationProtocolPort,
       "raisecomIpAclRef": raisecomIpAclRef,
       "raisecomIpAclStatus": raisecomIpAclStatus,
       "raisecomIpAclSetFlag": raisecomIpAclSetFlag,
       "raisecomMacAccessList": raisecomMacAccessList,
       "raisecomMacAclTable": raisecomMacAclTable,
       "raisecomMacAclEntry": raisecomMacAclEntry,
       "raisecomMacAclNumber": raisecomMacAclNumber,
       "raisecomMacAclAccessType": raisecomMacAclAccessType,
       "raisecomMacAclProtocol": raisecomMacAclProtocol,
       "raisecomMacAclSourceAddress": raisecomMacAclSourceAddress,
       "raisecomMacAclSourceMask": raisecomMacAclSourceMask,
       "raisecomMacAclDestinationAddress": raisecomMacAclDestinationAddress,
       "raisecomMacAclDestinationMask": raisecomMacAclDestinationMask,
       "raisecomMacAclRef": raisecomMacAclRef,
       "raisecomMacAclStatus": raisecomMacAclStatus,
       "raisecomMacAclSetFlag": raisecomMacAclSetFlag,
       "raisecomUserAccessList": raisecomUserAccessList,
       "raisecomUserAclTable": raisecomUserAclTable,
       "raisecomUserAclEntry": raisecomUserAclEntry,
       "raisecomUserAclNumber": raisecomUserAclNumber,
       "raisecomUserAclAccessType": raisecomUserAclAccessType,
       "raisecomUserAclRuleString": raisecomUserAclRuleString,
       "raisecomUserAclRuleMask": raisecomUserAclRuleMask,
       "raisecomUserAclOffset": raisecomUserAclOffset,
       "raisecomUserAclRef": raisecomUserAclRef,
       "raisecomUserAclStatus": raisecomUserAclStatus,
       "raisecomUserAclSourceMacAddress": raisecomUserAclSourceMacAddress,
       "raisecomUserAclDestinationMacAddress": raisecomUserAclDestinationMacAddress,
       "raisecomUserAclEtherType": raisecomUserAclEtherType,
       "raisecomUserAclEtherTypeMask": raisecomUserAclEtherTypeMask,
       "raisecomUserAclSourceIpAddress": raisecomUserAclSourceIpAddress,
       "raisecomUserAclSourceIpMask": raisecomUserAclSourceIpMask,
       "raisecomUserAclDestinationIpAddress": raisecomUserAclDestinationIpAddress,
       "raisecomUserAclDestinationIpMask": raisecomUserAclDestinationIpMask,
       "raisecomUserAclIpPrecedence": raisecomUserAclIpPrecedence,
       "raisecomUserAclIpTos": raisecomUserAclIpTos,
       "raisecomUserAclIpDscp": raisecomUserAclIpDscp,
       "raisecomUserAclIpFragmentsFlag": raisecomUserAclIpFragmentsFlag,
       "raisecomUserAclIpProtocol": raisecomUserAclIpProtocol,
       "raisecomUserAclSourceProtocolPort": raisecomUserAclSourceProtocolPort,
       "raisecomUserAclDestinationProtocolPort": raisecomUserAclDestinationProtocolPort,
       "raisecomUserAclTcpProtocolFlag": raisecomUserAclTcpProtocolFlag,
       "raisecomUserAclCvlanCos": raisecomUserAclCvlanCos,
       "raisecomUserAclSvlanCos": raisecomUserAclSvlanCos,
       "raisecomUserAclCvlan": raisecomUserAclCvlan,
       "raisecomUserAclSvlan": raisecomUserAclSvlan,
       "raisecomUserAclSetFlag": raisecomUserAclSetFlag,
       "raisecomUserAclSourceMacMask": raisecomUserAclSourceMacMask,
       "raisecomUserAclDestinationMacMask": raisecomUserAclDestinationMacMask,
       "raisecomUserAclCos": raisecomUserAclCos,
       "raisecomUserAclArpType": raisecomUserAclArpType,
       "raisecomUserAclArpSenderMac": raisecomUserAclArpSenderMac,
       "raisecomUserAclArpTargetMac": raisecomUserAclArpTargetMac,
       "raisecomUserAclIcmpIgmpType": raisecomUserAclIcmpIgmpType,
       "raisecomUserAclIcmpCode": raisecomUserAclIcmpCode,
       "raisecomUserAclIpv6SourceAddress": raisecomUserAclIpv6SourceAddress,
       "raisecomUserAclIpv6SourceMask": raisecomUserAclIpv6SourceMask,
       "raisecomUserAclIpv6DestinationAddress": raisecomUserAclIpv6DestinationAddress,
       "raisecomUserAclIpv6DestinationMask": raisecomUserAclIpv6DestinationMask,
       "raisecomUserAclIpv6SourceMaskLen": raisecomUserAclIpv6SourceMaskLen,
       "raisecomUserAclIpv6DestinationMaskLen": raisecomUserAclIpv6DestinationMaskLen,
       "raisecomUserAclIpv6Protocol": raisecomUserAclIpv6Protocol,
       "raisecomUserAclIpv6FlowLabel": raisecomUserAclIpv6FlowLabel,
       "raisecomUserAclIpv6TrafficClass": raisecomUserAclIpv6TrafficClass,
       "raisecomUserAclIcmpv6Type": raisecomUserAclIcmpv6Type,
       "raisecomUserAclUserLen": raisecomUserAclUserLen,
       "raisecomUserAclExtensionSetFlag": raisecomUserAclExtensionSetFlag,
       "raisecomUserAclTunnelLabel": raisecomUserAclTunnelLabel,
       "raisecomUserAclTunnelExp": raisecomUserAclTunnelExp,
       "raisecomUserAclVcLabel": raisecomUserAclVcLabel,
       "raisecomUserAclVcExp": raisecomUserAclVcExp,
       "raisecomIpv6AccessList": raisecomIpv6AccessList,
       "raisecomIpv6AclTable": raisecomIpv6AclTable,
       "raisecomIpv6AclEntry": raisecomIpv6AclEntry,
       "raisecomIpv6AclNumber": raisecomIpv6AclNumber,
       "raisecomIpv6AclAccessType": raisecomIpv6AclAccessType,
       "raisecomIpv6AclProtocol": raisecomIpv6AclProtocol,
       "raisecomIpv6AclSourceAddress": raisecomIpv6AclSourceAddress,
       "raisecomIpv6AclSourcePrefixLen": raisecomIpv6AclSourcePrefixLen,
       "raisecomIpv6AclDestinationAddress": raisecomIpv6AclDestinationAddress,
       "raisecomIpv6AclDestinationPrefixLen": raisecomIpv6AclDestinationPrefixLen,
       "raisecomIpv6AclTrafficClass": raisecomIpv6AclTrafficClass,
       "raisecomIpv6AclFlowLabel": raisecomIpv6AclFlowLabel,
       "raisecomIpv6AclRef": raisecomIpv6AclRef,
       "raisecomIpv6AclStatus": raisecomIpv6AclStatus,
       "raisecomIpv6AclSourceProtocolPort": raisecomIpv6AclSourceProtocolPort,
       "raisecomIpv6AclDestinationProtocolPort": raisecomIpv6AclDestinationProtocolPort,
       "raisecomIpv6AclSetFlag": raisecomIpv6AclSetFlag}
)
