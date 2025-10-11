# SNMP MIB module (ALCATEL-ENT1-LLDP-TRUST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-LLDP-TRUST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:13 2025
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

(softentIND1LldpTrust,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1LldpTrust")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpPortId,
 LldpPortIdSubtype,
 LldpPortNumber) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpPortId",
    "LldpPortIdSubtype",
    "LldpPortNumber")

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

alcatelIND1LLDPTRUSTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LLDPTRUSTMIB.setRevisions(
        ("2009-08-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaLLDPTraps_ObjectIdentity = ObjectIdentity
alaLLDPTraps = _AlaLLDPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 0)
)
if mibBuilder.loadTexts:
    alaLLDPTraps.setStatus("current")
_AlcatelIND1LLDPTRUSTMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1LLDPTRUSTMIBObjects = _AlcatelIND1LLDPTRUSTMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LLDPTRUSTMIBObjects.setStatus("current")
_AlaIND1LLDPTRUSTMIBObjects_ObjectIdentity = ObjectIdentity
alaIND1LLDPTRUSTMIBObjects = _AlaIND1LLDPTRUSTMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1)
)
_AlaLLDPTrustPortTable_Object = MibTable
alaLLDPTrustPortTable = _AlaLLDPTrustPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaLLDPTrustPortTable.setStatus("current")
_AlaLLDPTrustPortEntry_Object = MibTableRow
alaLLDPTrustPortEntry = _AlaLLDPTrustPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 1, 1)
)
alaLLDPTrustPortEntry.setIndexNames(
    (0, "ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustLocalPortNumber"),
)
if mibBuilder.loadTexts:
    alaLLDPTrustPortEntry.setStatus("current")
_AlaLLDPTrustLocalPortNumber_Type = LldpPortNumber
_AlaLLDPTrustLocalPortNumber_Object = MibTableColumn
alaLLDPTrustLocalPortNumber = _AlaLLDPTrustLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 1, 1, 1),
    _AlaLLDPTrustLocalPortNumber_Type()
)
alaLLDPTrustLocalPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLLDPTrustLocalPortNumber.setStatus("current")


class _AlaLldpTrustAdminStatus_Type(Integer32):
    """Custom type alaLldpTrustAdminStatus based on Integer32"""
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


_AlaLldpTrustAdminStatus_Type.__name__ = "Integer32"
_AlaLldpTrustAdminStatus_Object = MibTableColumn
alaLldpTrustAdminStatus = _AlaLldpTrustAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 1, 1, 2),
    _AlaLldpTrustAdminStatus_Type()
)
alaLldpTrustAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLldpTrustAdminStatus.setStatus("current")


class _AlaLldpTrustAction_Type(Integer32):
    """Custom type alaLldpTrustAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trap", 1),
          ("shutdown", 2),
          ("both", 3))
    )


_AlaLldpTrustAction_Type.__name__ = "Integer32"
_AlaLldpTrustAction_Object = MibTableColumn
alaLldpTrustAction = _AlaLldpTrustAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 1, 1, 3),
    _AlaLldpTrustAction_Type()
)
alaLldpTrustAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLldpTrustAction.setStatus("current")


class _AlaLldpTrustedStatus_Type(Integer32):
    """Custom type alaLldpTrustedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("violated", 2))
    )


_AlaLldpTrustedStatus_Type.__name__ = "Integer32"
_AlaLldpTrustedStatus_Object = MibTableColumn
alaLldpTrustedStatus = _AlaLldpTrustedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 1, 1, 4),
    _AlaLldpTrustedStatus_Type()
)
alaLldpTrustedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLldpTrustedStatus.setStatus("current")


class _AlaLldpTrustedChassisSubtype_Type(Integer32):
    """Custom type alaLldpTrustedChassisSubtype based on Integer32"""
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
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7),
          ("any", 8))
    )


_AlaLldpTrustedChassisSubtype_Type.__name__ = "Integer32"
_AlaLldpTrustedChassisSubtype_Object = MibTableColumn
alaLldpTrustedChassisSubtype = _AlaLldpTrustedChassisSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 1, 1, 5),
    _AlaLldpTrustedChassisSubtype_Type()
)
alaLldpTrustedChassisSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLldpTrustedChassisSubtype.setStatus("current")
_AlaLLDPTrustedRemTable_Object = MibTable
alaLLDPTrustedRemTable = _AlaLLDPTrustedRemTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaLLDPTrustedRemTable.setStatus("current")
_AlaLLDPTrustedRemEntry_Object = MibTableRow
alaLLDPTrustedRemEntry = _AlaLLDPTrustedRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 2, 1)
)
alaLLDPTrustedRemEntry.setIndexNames(
    (0, "ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustedRemLocalPortNumber"),
)
if mibBuilder.loadTexts:
    alaLLDPTrustedRemEntry.setStatus("current")
_AlaLLDPTrustedRemLocalPortNumber_Type = LldpPortNumber
_AlaLLDPTrustedRemLocalPortNumber_Object = MibTableColumn
alaLLDPTrustedRemLocalPortNumber = _AlaLLDPTrustedRemLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 2, 1, 1),
    _AlaLLDPTrustedRemLocalPortNumber_Type()
)
alaLLDPTrustedRemLocalPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLLDPTrustedRemLocalPortNumber.setStatus("current")
_AlaLLDPTrustedRemChassisIdSubtype_Type = LldpChassisIdSubtype
_AlaLLDPTrustedRemChassisIdSubtype_Object = MibTableColumn
alaLLDPTrustedRemChassisIdSubtype = _AlaLLDPTrustedRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 2, 1, 2),
    _AlaLLDPTrustedRemChassisIdSubtype_Type()
)
alaLLDPTrustedRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLLDPTrustedRemChassisIdSubtype.setStatus("current")
_AlaLLDPTrustedRemChassisId_Type = LldpChassisId
_AlaLLDPTrustedRemChassisId_Object = MibTableColumn
alaLLDPTrustedRemChassisId = _AlaLLDPTrustedRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 2, 1, 3),
    _AlaLLDPTrustedRemChassisId_Type()
)
alaLLDPTrustedRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLLDPTrustedRemChassisId.setStatus("current")
_AlaLLDPTrustedRemPortIdSubtype_Type = LldpPortIdSubtype
_AlaLLDPTrustedRemPortIdSubtype_Object = MibTableColumn
alaLLDPTrustedRemPortIdSubtype = _AlaLLDPTrustedRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 2, 1, 4),
    _AlaLLDPTrustedRemPortIdSubtype_Type()
)
alaLLDPTrustedRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLLDPTrustedRemPortIdSubtype.setStatus("current")
_AlaLLDPTrustedRemPortId_Type = LldpPortId
_AlaLLDPTrustedRemPortId_Object = MibTableColumn
alaLLDPTrustedRemPortId = _AlaLLDPTrustedRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 2, 1, 5),
    _AlaLLDPTrustedRemPortId_Type()
)
alaLLDPTrustedRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLLDPTrustedRemPortId.setStatus("current")
_AlaLLDPTrustPortIfIndex_Type = InterfaceIndex
_AlaLLDPTrustPortIfIndex_Object = MibScalar
alaLLDPTrustPortIfIndex = _AlaLLDPTrustPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 3),
    _AlaLLDPTrustPortIfIndex_Type()
)
alaLLDPTrustPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLLDPTrustPortIfIndex.setStatus("current")


class _AlaLLDPTrustViolationReason_Type(Integer32):
    """Custom type alaLLDPTrustViolationReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("agentalreadyexistonport", 1),
          ("agentalreadyexistonotherport", 2),
          ("chassisidsubtypemissmatch", 3))
    )


_AlaLLDPTrustViolationReason_Type.__name__ = "Integer32"
_AlaLLDPTrustViolationReason_Object = MibScalar
alaLLDPTrustViolationReason = _AlaLLDPTrustViolationReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 4),
    _AlaLLDPTrustViolationReason_Type()
)
alaLLDPTrustViolationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLLDPTrustViolationReason.setStatus("current")
_AlaLLDPTrustPortId_Type = Integer32
_AlaLLDPTrustPortId_Object = MibScalar
alaLLDPTrustPortId = _AlaLLDPTrustPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 5),
    _AlaLLDPTrustPortId_Type()
)
alaLLDPTrustPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLLDPTrustPortId.setStatus("current")
_AlaLLDPTrustChassisId_Type = LldpChassisId
_AlaLLDPTrustChassisId_Object = MibScalar
alaLLDPTrustChassisId = _AlaLLDPTrustChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 1, 1, 6),
    _AlaLLDPTrustChassisId_Type()
)
alaLLDPTrustChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLLDPTrustChassisId.setStatus("current")
_AlaIND1LLDPTRUSTMIBConformance_ObjectIdentity = ObjectIdentity
alaIND1LLDPTRUSTMIBConformance = _AlaIND1LLDPTRUSTMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 2)
)
if mibBuilder.loadTexts:
    alaIND1LLDPTRUSTMIBConformance.setStatus("current")
_AlaIND1LLDPTRUSTMIBGroups_ObjectIdentity = ObjectIdentity
alaIND1LLDPTRUSTMIBGroups = _AlaIND1LLDPTRUSTMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIND1LLDPTRUSTMIBGroups.setStatus("current")
_AlaIND1LLDPTRUSTMIBCompliances_ObjectIdentity = ObjectIdentity
alaIND1LLDPTRUSTMIBCompliances = _AlaIND1LLDPTRUSTMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaIND1LLDPTRUSTMIBCompliances.setStatus("current")

# Managed Objects groups

alaINDLLDPTrustBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 2, 1, 1)
)
alaINDLLDPTrustBaseGroup.setObjects(
      *(("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustPortIfIndex"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustViolationReason"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustPortId"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustChassisId"))
)
if mibBuilder.loadTexts:
    alaINDLLDPTrustBaseGroup.setStatus("current")

alaINDLLDPTrustAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 2, 1, 2)
)
alaINDLLDPTrustAgentGroup.setObjects(
      *(("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLldpTrustAdminStatus"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLldpTrustAction"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLldpTrustedStatus"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLldpTrustedChassisSubtype"))
)
if mibBuilder.loadTexts:
    alaINDLLDPTrustAgentGroup.setStatus("current")

alaINDLLDPTrustRemoteAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 2, 1, 3)
)
alaINDLLDPTrustRemoteAgentGroup.setObjects(
      *(("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustedRemChassisIdSubtype"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustedRemChassisId"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustedRemPortIdSubtype"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustedRemPortId"))
)
if mibBuilder.loadTexts:
    alaINDLLDPTrustRemoteAgentGroup.setStatus("current")


# Notification objects

alaLldpTrustViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 0, 1)
)
alaLldpTrustViolation.setObjects(
      *(("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustPortIfIndex"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLLDPTrustViolationReason"))
)
if mibBuilder.loadTexts:
    alaLldpTrustViolation.setStatus(
        "current"
    )


# Notifications groups

alaLldpTrustTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 2, 1, 4)
)
alaLldpTrustTrapGroup.setObjects(
    ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLldpTrustViolation")
)
if mibBuilder.loadTexts:
    alaLldpTrustTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaIND1LLDPTRUSTMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 87, 1, 2, 2, 1)
)
alaIND1LLDPTRUSTMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaINDLLDPTrustAgentGroup"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaINDLLDPTrustRemoteAgentGroup"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaINDLLDPTrustBaseGroup"),
        ("ALCATEL-ENT1-LLDP-TRUST-MIB", "alaLldpTrustTrapGroup"))
)
if mibBuilder.loadTexts:
    alaIND1LLDPTRUSTMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-LLDP-TRUST-MIB",
    **{"alcatelIND1LLDPTRUSTMIB": alcatelIND1LLDPTRUSTMIB,
       "alaLLDPTraps": alaLLDPTraps,
       "alaLldpTrustViolation": alaLldpTrustViolation,
       "alcatelIND1LLDPTRUSTMIBObjects": alcatelIND1LLDPTRUSTMIBObjects,
       "alaIND1LLDPTRUSTMIBObjects": alaIND1LLDPTRUSTMIBObjects,
       "alaLLDPTrustPortTable": alaLLDPTrustPortTable,
       "alaLLDPTrustPortEntry": alaLLDPTrustPortEntry,
       "alaLLDPTrustLocalPortNumber": alaLLDPTrustLocalPortNumber,
       "alaLldpTrustAdminStatus": alaLldpTrustAdminStatus,
       "alaLldpTrustAction": alaLldpTrustAction,
       "alaLldpTrustedStatus": alaLldpTrustedStatus,
       "alaLldpTrustedChassisSubtype": alaLldpTrustedChassisSubtype,
       "alaLLDPTrustedRemTable": alaLLDPTrustedRemTable,
       "alaLLDPTrustedRemEntry": alaLLDPTrustedRemEntry,
       "alaLLDPTrustedRemLocalPortNumber": alaLLDPTrustedRemLocalPortNumber,
       "alaLLDPTrustedRemChassisIdSubtype": alaLLDPTrustedRemChassisIdSubtype,
       "alaLLDPTrustedRemChassisId": alaLLDPTrustedRemChassisId,
       "alaLLDPTrustedRemPortIdSubtype": alaLLDPTrustedRemPortIdSubtype,
       "alaLLDPTrustedRemPortId": alaLLDPTrustedRemPortId,
       "alaLLDPTrustPortIfIndex": alaLLDPTrustPortIfIndex,
       "alaLLDPTrustViolationReason": alaLLDPTrustViolationReason,
       "alaLLDPTrustPortId": alaLLDPTrustPortId,
       "alaLLDPTrustChassisId": alaLLDPTrustChassisId,
       "alaIND1LLDPTRUSTMIBConformance": alaIND1LLDPTRUSTMIBConformance,
       "alaIND1LLDPTRUSTMIBGroups": alaIND1LLDPTRUSTMIBGroups,
       "alaINDLLDPTrustBaseGroup": alaINDLLDPTrustBaseGroup,
       "alaINDLLDPTrustAgentGroup": alaINDLLDPTrustAgentGroup,
       "alaINDLLDPTrustRemoteAgentGroup": alaINDLLDPTrustRemoteAgentGroup,
       "alaLldpTrustTrapGroup": alaLldpTrustTrapGroup,
       "alaIND1LLDPTRUSTMIBCompliances": alaIND1LLDPTRUSTMIBCompliances,
       "alaIND1LLDPTRUSTMIBCompliance": alaIND1LLDPTRUSTMIBCompliance}
)
