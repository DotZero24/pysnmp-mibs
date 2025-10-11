# SNMP MIB module (DNOS-MACSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DNOS-MACSEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:19 2025
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

fastPathMACsec = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78)
)
if mibBuilder.loadTexts:
    fastPathMACsec.setRevisions(
        ("2021-01-28 00:00",
         "2020-08-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MACsecCipherSuite(TextualConvention, Integer32):
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
        *(("gcmAes128", 0),
          ("gcmAes256", 1),
          ("gcmAesXpn128", 2),
          ("gcmAesXpn256", 3))
    )



class MACsecConfidentialityOffset(TextualConvention, Integer32):
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
        *(("noConfidentiality", 0),
          ("confidentialityWithNoOffset", 1),
          ("offset30", 2),
          ("offset50", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AgentMACsecMKAPolicyConfigGroup_ObjectIdentity = ObjectIdentity
agentMACsecMKAPolicyConfigGroup = _AgentMACsecMKAPolicyConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 1)
)
_AgentMACsecMKAPolicyConfigTable_Object = MibTable
agentMACsecMKAPolicyConfigTable = _AgentMACsecMKAPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 1, 1)
)
if mibBuilder.loadTexts:
    agentMACsecMKAPolicyConfigTable.setStatus("current")
_AgentMACsecMKAPolicyConfigEntry_Object = MibTableRow
agentMACsecMKAPolicyConfigEntry = _AgentMACsecMKAPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 1, 1, 1)
)
agentMACsecMKAPolicyConfigEntry.setIndexNames(
    (0, "DNOS-MACSEC-MIB", "agentMACsecMKAPolicyName"),
)
if mibBuilder.loadTexts:
    agentMACsecMKAPolicyConfigEntry.setStatus("current")


class _AgentMACsecMKAPolicyName_Type(SnmpAdminString):
    """Custom type agentMACsecMKAPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentMACsecMKAPolicyName_Type.__name__ = "SnmpAdminString"
_AgentMACsecMKAPolicyName_Object = MibTableColumn
agentMACsecMKAPolicyName = _AgentMACsecMKAPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 1, 1, 1, 1),
    _AgentMACsecMKAPolicyName_Type()
)
agentMACsecMKAPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecMKAPolicyName.setStatus("current")


class _AgentMACsecMKAPolicyKeyServerPriority_Type(Unsigned32):
    """Custom type agentMACsecMKAPolicyKeyServerPriority based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentMACsecMKAPolicyKeyServerPriority_Type.__name__ = "Unsigned32"
_AgentMACsecMKAPolicyKeyServerPriority_Object = MibTableColumn
agentMACsecMKAPolicyKeyServerPriority = _AgentMACsecMKAPolicyKeyServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 1, 1, 1, 2),
    _AgentMACsecMKAPolicyKeyServerPriority_Type()
)
agentMACsecMKAPolicyKeyServerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecMKAPolicyKeyServerPriority.setStatus("current")


class _AgentMACsecMKAPolicySecureAnnouncements_Type(Integer32):
    """Custom type agentMACsecMKAPolicySecureAnnouncements based on Integer32"""
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


_AgentMACsecMKAPolicySecureAnnouncements_Type.__name__ = "Integer32"
_AgentMACsecMKAPolicySecureAnnouncements_Object = MibTableColumn
agentMACsecMKAPolicySecureAnnouncements = _AgentMACsecMKAPolicySecureAnnouncements_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 1, 1, 1, 3),
    _AgentMACsecMKAPolicySecureAnnouncements_Type()
)
agentMACsecMKAPolicySecureAnnouncements.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecMKAPolicySecureAnnouncements.setStatus("current")


class _AgentMACsecMKAPolicyCipherSuite_Type(Integer32):
    """Custom type agentMACsecMKAPolicyCipherSuite based on Integer32"""
    defaultValue = 0

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
        *(("gcmAes128", 0),
          ("gcmAes256", 1),
          ("gcmAesXpn128", 2),
          ("gcmAesXpn256", 3))
    )


_AgentMACsecMKAPolicyCipherSuite_Type.__name__ = "Integer32"
_AgentMACsecMKAPolicyCipherSuite_Object = MibTableColumn
agentMACsecMKAPolicyCipherSuite = _AgentMACsecMKAPolicyCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 1, 1, 1, 4),
    _AgentMACsecMKAPolicyCipherSuite_Type()
)
agentMACsecMKAPolicyCipherSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecMKAPolicyCipherSuite.setStatus("current")


class _AgentMACsecMKAPolicyConfidentialityOffset_Type(Integer32):
    """Custom type agentMACsecMKAPolicyConfidentialityOffset based on Integer32"""
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
        *(("noConfidentiality", 0),
          ("confidentialityWithNoOffset", 1),
          ("offset30", 2),
          ("offset50", 3))
    )


_AgentMACsecMKAPolicyConfidentialityOffset_Type.__name__ = "Integer32"
_AgentMACsecMKAPolicyConfidentialityOffset_Object = MibTableColumn
agentMACsecMKAPolicyConfidentialityOffset = _AgentMACsecMKAPolicyConfidentialityOffset_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 1, 1, 1, 5),
    _AgentMACsecMKAPolicyConfidentialityOffset_Type()
)
agentMACsecMKAPolicyConfidentialityOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecMKAPolicyConfidentialityOffset.setStatus("current")
_AgentMACsecMKAPolicyRowStatus_Type = RowStatus
_AgentMACsecMKAPolicyRowStatus_Object = MibTableColumn
agentMACsecMKAPolicyRowStatus = _AgentMACsecMKAPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 1, 1, 1, 6),
    _AgentMACsecMKAPolicyRowStatus_Type()
)
agentMACsecMKAPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecMKAPolicyRowStatus.setStatus("current")
_AgentMACsecKeyConfigGroup_ObjectIdentity = ObjectIdentity
agentMACsecKeyConfigGroup = _AgentMACsecKeyConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 2)
)
_AgentMACsecKeyConfigTable_Object = MibTable
agentMACsecKeyConfigTable = _AgentMACsecKeyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 2, 1)
)
if mibBuilder.loadTexts:
    agentMACsecKeyConfigTable.setStatus("current")
_AgentMACsecKeyConfigEntry_Object = MibTableRow
agentMACsecKeyConfigEntry = _AgentMACsecKeyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 2, 1, 1)
)
agentMACsecKeyConfigEntry.setIndexNames(
    (0, "DNOS-MACSEC-MIB", "agentMACsecKeyChainName"),
    (0, "DNOS-MACSEC-MIB", "agentMACsecKeyName"),
)
if mibBuilder.loadTexts:
    agentMACsecKeyConfigEntry.setStatus("current")


class _AgentMACsecKeyChainName_Type(OctetString):
    """Custom type agentMACsecKeyChainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentMACsecKeyChainName_Type.__name__ = "OctetString"
_AgentMACsecKeyChainName_Object = MibTableColumn
agentMACsecKeyChainName = _AgentMACsecKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 2, 1, 1, 1),
    _AgentMACsecKeyChainName_Type()
)
agentMACsecKeyChainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecKeyChainName.setStatus("current")


class _AgentMACsecKeyName_Type(OctetString):
    """Custom type agentMACsecKeyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentMACsecKeyName_Type.__name__ = "OctetString"
_AgentMACsecKeyName_Object = MibTableColumn
agentMACsecKeyName = _AgentMACsecKeyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 2, 1, 1, 2),
    _AgentMACsecKeyName_Type()
)
agentMACsecKeyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecKeyName.setStatus("current")


class _AgentMACsecKeyCryptographicAlgorithm_Type(Integer32):
    """Custom type agentMACsecKeyCryptographicAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gcmAes128", 1),
          ("gcmAes256", 2))
    )


_AgentMACsecKeyCryptographicAlgorithm_Type.__name__ = "Integer32"
_AgentMACsecKeyCryptographicAlgorithm_Object = MibTableColumn
agentMACsecKeyCryptographicAlgorithm = _AgentMACsecKeyCryptographicAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 2, 1, 1, 3),
    _AgentMACsecKeyCryptographicAlgorithm_Type()
)
agentMACsecKeyCryptographicAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecKeyCryptographicAlgorithm.setStatus("current")


class _AgentMACsecKeyString_Type(OctetString):
    """Custom type agentMACsecKeyString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
        ValueSizeConstraint(64, 64),
    )


_AgentMACsecKeyString_Type.__name__ = "OctetString"
_AgentMACsecKeyString_Object = MibTableColumn
agentMACsecKeyString = _AgentMACsecKeyString_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 2, 1, 1, 4),
    _AgentMACsecKeyString_Type()
)
agentMACsecKeyString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecKeyString.setStatus("current")


class _AgentMACsecKeyTimeRange_Type(OctetString):
    """Custom type agentMACsecKeyTimeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 31),
    )


_AgentMACsecKeyTimeRange_Type.__name__ = "OctetString"
_AgentMACsecKeyTimeRange_Object = MibTableColumn
agentMACsecKeyTimeRange = _AgentMACsecKeyTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 2, 1, 1, 5),
    _AgentMACsecKeyTimeRange_Type()
)
agentMACsecKeyTimeRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecKeyTimeRange.setStatus("current")
_AgentMACsecKeyRowStatus_Type = RowStatus
_AgentMACsecKeyRowStatus_Object = MibTableColumn
agentMACsecKeyRowStatus = _AgentMACsecKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 2, 1, 1, 6),
    _AgentMACsecKeyRowStatus_Type()
)
agentMACsecKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMACsecKeyRowStatus.setStatus("current")
_AgentMACsecInterfaceConfigGroup_ObjectIdentity = ObjectIdentity
agentMACsecInterfaceConfigGroup = _AgentMACsecInterfaceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 3)
)
_AgentMACsecInterfaceConfigTable_Object = MibTable
agentMACsecInterfaceConfigTable = _AgentMACsecInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 3, 1)
)
if mibBuilder.loadTexts:
    agentMACsecInterfaceConfigTable.setStatus("current")
_AgentMACsecInterfaceConfigEntry_Object = MibTableRow
agentMACsecInterfaceConfigEntry = _AgentMACsecInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 3, 1, 1)
)
agentMACsecInterfaceConfigEntry.setIndexNames(
    (0, "DNOS-MACSEC-MIB", "agentMACsecInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMACsecInterfaceConfigEntry.setStatus("current")
_AgentMACsecInterfaceIndex_Type = InterfaceIndex
_AgentMACsecInterfaceIndex_Object = MibTableColumn
agentMACsecInterfaceIndex = _AgentMACsecInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 3, 1, 1, 1),
    _AgentMACsecInterfaceIndex_Type()
)
agentMACsecInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMACsecInterfaceIndex.setStatus("current")


class _AgentMACsecInterfaceNetworkLink_Type(Integer32):
    """Custom type agentMACsecInterfaceNetworkLink based on Integer32"""
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
          ("switchToSwitch", 2),
          ("hostToSwitch", 3))
    )


_AgentMACsecInterfaceNetworkLink_Type.__name__ = "Integer32"
_AgentMACsecInterfaceNetworkLink_Object = MibTableColumn
agentMACsecInterfaceNetworkLink = _AgentMACsecInterfaceNetworkLink_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 3, 1, 1, 2),
    _AgentMACsecInterfaceNetworkLink_Type()
)
agentMACsecInterfaceNetworkLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMACsecInterfaceNetworkLink.setStatus("current")


class _AgentMACsecInterfaceMKAPolicy_Type(OctetString):
    """Custom type agentMACsecInterfaceMKAPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentMACsecInterfaceMKAPolicy_Type.__name__ = "OctetString"
_AgentMACsecInterfaceMKAPolicy_Object = MibTableColumn
agentMACsecInterfaceMKAPolicy = _AgentMACsecInterfaceMKAPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 3, 1, 1, 3),
    _AgentMACsecInterfaceMKAPolicy_Type()
)
agentMACsecInterfaceMKAPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMACsecInterfaceMKAPolicy.setStatus("current")


class _AgentMACsecInterfaceKeyChain_Type(OctetString):
    """Custom type agentMACsecInterfaceKeyChain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgentMACsecInterfaceKeyChain_Type.__name__ = "OctetString"
_AgentMACsecInterfaceKeyChain_Object = MibTableColumn
agentMACsecInterfaceKeyChain = _AgentMACsecInterfaceKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 3, 1, 1, 4),
    _AgentMACsecInterfaceKeyChain_Type()
)
agentMACsecInterfaceKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMACsecInterfaceKeyChain.setStatus("current")


class _AgentMACsecInterfaceReplayProtection_Type(Integer32):
    """Custom type agentMACsecInterfaceReplayProtection based on Integer32"""
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


_AgentMACsecInterfaceReplayProtection_Type.__name__ = "Integer32"
_AgentMACsecInterfaceReplayProtection_Object = MibTableColumn
agentMACsecInterfaceReplayProtection = _AgentMACsecInterfaceReplayProtection_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 3, 1, 1, 5),
    _AgentMACsecInterfaceReplayProtection_Type()
)
agentMACsecInterfaceReplayProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMACsecInterfaceReplayProtection.setStatus("current")


class _AgentMACsecInterfaceReplayProtectionWindowSize_Type(Unsigned32):
    """Custom type agentMACsecInterfaceReplayProtectionWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AgentMACsecInterfaceReplayProtectionWindowSize_Type.__name__ = "Unsigned32"
_AgentMACsecInterfaceReplayProtectionWindowSize_Object = MibTableColumn
agentMACsecInterfaceReplayProtectionWindowSize = _AgentMACsecInterfaceReplayProtectionWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 3, 1, 1, 6),
    _AgentMACsecInterfaceReplayProtectionWindowSize_Type()
)
agentMACsecInterfaceReplayProtectionWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMACsecInterfaceReplayProtectionWindowSize.setStatus("current")
_AgentMACsecMkaSessionGroup_ObjectIdentity = ObjectIdentity
agentMACsecMkaSessionGroup = _AgentMACsecMkaSessionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4)
)
_AgentMACsecMkaSessionTable_Object = MibTable
agentMACsecMkaSessionTable = _AgentMACsecMkaSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4, 1)
)
if mibBuilder.loadTexts:
    agentMACsecMkaSessionTable.setStatus("current")
_AgentMACsecMkaSessionEntry_Object = MibTableRow
agentMACsecMkaSessionEntry = _AgentMACsecMkaSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4, 1, 1)
)
agentMACsecMkaSessionEntry.setIndexNames(
    (0, "DNOS-MACSEC-MIB", "agentMACsecMkaInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMACsecMkaSessionEntry.setStatus("current")
_AgentMACsecMkaInterfaceIndex_Type = InterfaceIndex
_AgentMACsecMkaInterfaceIndex_Object = MibTableColumn
agentMACsecMkaInterfaceIndex = _AgentMACsecMkaInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4, 1, 1, 1),
    _AgentMACsecMkaInterfaceIndex_Type()
)
agentMACsecMkaInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMACsecMkaInterfaceIndex.setStatus("current")


class _AgentMACsecMkaPolicy_Type(OctetString):
    """Custom type agentMACsecMkaPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AgentMACsecMkaPolicy_Type.__name__ = "OctetString"
_AgentMACsecMkaPolicy_Object = MibTableColumn
agentMACsecMkaPolicy = _AgentMACsecMkaPolicy_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4, 1, 1, 2),
    _AgentMACsecMkaPolicy_Type()
)
agentMACsecMkaPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaPolicy.setStatus("current")


class _AgentMACsecMkaCkn_Type(OctetString):
    """Custom type agentMACsecMkaCkn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
        ValueSizeConstraint(64, 64),
    )


_AgentMACsecMkaCkn_Type.__name__ = "OctetString"
_AgentMACsecMkaCkn_Object = MibTableColumn
agentMACsecMkaCkn = _AgentMACsecMkaCkn_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4, 1, 1, 3),
    _AgentMACsecMkaCkn_Type()
)
agentMACsecMkaCkn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaCkn.setStatus("current")


class _AgentMACsecMkaLocalTxSci_Type(OctetString):
    """Custom type agentMACsecMkaLocalTxSci based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )
    fixed_length = 22


_AgentMACsecMkaLocalTxSci_Type.__name__ = "OctetString"
_AgentMACsecMkaLocalTxSci_Object = MibTableColumn
agentMACsecMkaLocalTxSci = _AgentMACsecMkaLocalTxSci_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4, 1, 1, 4),
    _AgentMACsecMkaLocalTxSci_Type()
)
agentMACsecMkaLocalTxSci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaLocalTxSci.setStatus("current")


class _AgentMACsecMkaPeerRxSci_Type(OctetString):
    """Custom type agentMACsecMkaPeerRxSci based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )
    fixed_length = 22


_AgentMACsecMkaPeerRxSci_Type.__name__ = "OctetString"
_AgentMACsecMkaPeerRxSci_Object = MibTableColumn
agentMACsecMkaPeerRxSci = _AgentMACsecMkaPeerRxSci_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4, 1, 1, 5),
    _AgentMACsecMkaPeerRxSci_Type()
)
agentMACsecMkaPeerRxSci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaPeerRxSci.setStatus("current")


class _AgentMACsecMkaKeyServer_Type(Integer32):
    """Custom type agentMACsecMkaKeyServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AgentMACsecMkaKeyServer_Type.__name__ = "Integer32"
_AgentMACsecMkaKeyServer_Object = MibTableColumn
agentMACsecMkaKeyServer = _AgentMACsecMkaKeyServer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4, 1, 1, 6),
    _AgentMACsecMkaKeyServer_Type()
)
agentMACsecMkaKeyServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaKeyServer.setStatus("current")
_AgentMACsecMkaPeers_Type = Integer32
_AgentMACsecMkaPeers_Object = MibTableColumn
agentMACsecMkaPeers = _AgentMACsecMkaPeers_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 4, 1, 1, 7),
    _AgentMACsecMkaPeers_Type()
)
agentMACsecMkaPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaPeers.setStatus("current")
_AgentMACsecMkaPortStatisticsGroup_ObjectIdentity = ObjectIdentity
agentMACsecMkaPortStatisticsGroup = _AgentMACsecMkaPortStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5)
)
_AgentMACsecMkaStatisticsTable_Object = MibTable
agentMACsecMkaStatisticsTable = _AgentMACsecMkaStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1)
)
if mibBuilder.loadTexts:
    agentMACsecMkaStatisticsTable.setStatus("current")
_AgentMACsecMkaStatisticsEntry_Object = MibTableRow
agentMACsecMkaStatisticsEntry = _AgentMACsecMkaStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1)
)
agentMACsecMkaStatisticsEntry.setIndexNames(
    (0, "DNOS-MACSEC-MIB", "agentMACsecInterfaceIndex"),
)
if mibBuilder.loadTexts:
    agentMACsecMkaStatisticsEntry.setStatus("current")
_AgentMACsecMkaSaksGenerated_Type = Counter64
_AgentMACsecMkaSaksGenerated_Object = MibTableColumn
agentMACsecMkaSaksGenerated = _AgentMACsecMkaSaksGenerated_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 1),
    _AgentMACsecMkaSaksGenerated_Type()
)
agentMACsecMkaSaksGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSaksGenerated.setStatus("current")
_AgentMACsecMkaSaksRekeyed_Type = Counter64
_AgentMACsecMkaSaksRekeyed_Object = MibTableColumn
agentMACsecMkaSaksRekeyed = _AgentMACsecMkaSaksRekeyed_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 2),
    _AgentMACsecMkaSaksRekeyed_Type()
)
agentMACsecMkaSaksRekeyed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSaksRekeyed.setStatus("current")
_AgentMACsecMkaSaksReceived_Type = Counter64
_AgentMACsecMkaSaksReceived_Object = MibTableColumn
agentMACsecMkaSaksReceived = _AgentMACsecMkaSaksReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 3),
    _AgentMACsecMkaSaksReceived_Type()
)
agentMACsecMkaSaksReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSaksReceived.setStatus("current")
_AgentMACsecMkaSaksResponsesReceived_Type = Counter64
_AgentMACsecMkaSaksResponsesReceived_Object = MibTableColumn
agentMACsecMkaSaksResponsesReceived = _AgentMACsecMkaSaksResponsesReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 4),
    _AgentMACsecMkaSaksResponsesReceived_Type()
)
agentMACsecMkaSaksResponsesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSaksResponsesReceived.setStatus("current")
_AgentMACsecMkaPduValidatedandRx_Type = Counter64
_AgentMACsecMkaPduValidatedandRx_Object = MibTableColumn
agentMACsecMkaPduValidatedandRx = _AgentMACsecMkaPduValidatedandRx_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 5),
    _AgentMACsecMkaPduValidatedandRx_Type()
)
agentMACsecMkaPduValidatedandRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaPduValidatedandRx.setStatus("current")
_AgentMACsecMkaPduTransmitted_Type = Counter64
_AgentMACsecMkaPduTransmitted_Object = MibTableColumn
agentMACsecMkaPduTransmitted = _AgentMACsecMkaPduTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 6),
    _AgentMACsecMkaPduTransmitted_Type()
)
agentMACsecMkaPduTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaPduTransmitted.setStatus("current")
_AgentMACsecMkaDistributedSAKs_Type = Counter64
_AgentMACsecMkaDistributedSAKs_Object = MibTableColumn
agentMACsecMkaDistributedSAKs = _AgentMACsecMkaDistributedSAKs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 7),
    _AgentMACsecMkaDistributedSAKs_Type()
)
agentMACsecMkaDistributedSAKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaDistributedSAKs.setStatus("current")
_AgentMACsecMkaVersionMismatchPkts_Type = Counter32
_AgentMACsecMkaVersionMismatchPkts_Object = MibTableColumn
agentMACsecMkaVersionMismatchPkts = _AgentMACsecMkaVersionMismatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 8),
    _AgentMACsecMkaVersionMismatchPkts_Type()
)
agentMACsecMkaVersionMismatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaVersionMismatchPkts.setStatus("current")
_AgentMACsecMkaIcvMismatchPkts_Type = Counter32
_AgentMACsecMkaIcvMismatchPkts_Object = MibTableColumn
agentMACsecMkaIcvMismatchPkts = _AgentMACsecMkaIcvMismatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 9),
    _AgentMACsecMkaIcvMismatchPkts_Type()
)
agentMACsecMkaIcvMismatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaIcvMismatchPkts.setStatus("current")
_AgentMACsecMkaMiDuplicatePkts_Type = Counter32
_AgentMACsecMkaMiDuplicatePkts_Object = MibTableColumn
agentMACsecMkaMiDuplicatePkts = _AgentMACsecMkaMiDuplicatePkts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 10),
    _AgentMACsecMkaMiDuplicatePkts_Type()
)
agentMACsecMkaMiDuplicatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaMiDuplicatePkts.setStatus("current")
_AgentMACsecMkaMnDuplicatePkts_Type = Counter32
_AgentMACsecMkaMnDuplicatePkts_Object = MibTableColumn
agentMACsecMkaMnDuplicatePkts = _AgentMACsecMkaMnDuplicatePkts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 11),
    _AgentMACsecMkaMnDuplicatePkts_Type()
)
agentMACsecMkaMnDuplicatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaMnDuplicatePkts.setStatus("current")
_AgentMACsecMkaInvalidDestinationPkts_Type = Counter32
_AgentMACsecMkaInvalidDestinationPkts_Object = MibTableColumn
agentMACsecMkaInvalidDestinationPkts = _AgentMACsecMkaInvalidDestinationPkts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 12),
    _AgentMACsecMkaInvalidDestinationPkts_Type()
)
agentMACsecMkaInvalidDestinationPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaInvalidDestinationPkts.setStatus("current")
_AgentMACsecMkaFormatingErrorPkts_Type = Counter32
_AgentMACsecMkaFormatingErrorPkts_Object = MibTableColumn
agentMACsecMkaFormatingErrorPkts = _AgentMACsecMkaFormatingErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 5, 1, 1, 13),
    _AgentMACsecMkaFormatingErrorPkts_Type()
)
agentMACsecMkaFormatingErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaFormatingErrorPkts.setStatus("current")
_AgentMACsecMkaGlobalStatisticsGroup_ObjectIdentity = ObjectIdentity
agentMACsecMkaGlobalStatisticsGroup = _AgentMACsecMkaGlobalStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6)
)
_AgentMACsecMkaSessionsSecured_Type = Counter64
_AgentMACsecMkaSessionsSecured_Object = MibScalar
agentMACsecMkaSessionsSecured = _AgentMACsecMkaSessionsSecured_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 1),
    _AgentMACsecMkaSessionsSecured_Type()
)
agentMACsecMkaSessionsSecured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSessionsSecured.setStatus("current")
_AgentMACsecMkaSessionsDeleted_Type = Counter64
_AgentMACsecMkaSessionsDeleted_Object = MibScalar
agentMACsecMkaSessionsDeleted = _AgentMACsecMkaSessionsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 2),
    _AgentMACsecMkaSessionsDeleted_Type()
)
agentMACsecMkaSessionsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSessionsDeleted.setStatus("current")
_AgentMACsecMkaSaksGeneratedGlobal_Type = Counter64
_AgentMACsecMkaSaksGeneratedGlobal_Object = MibScalar
agentMACsecMkaSaksGeneratedGlobal = _AgentMACsecMkaSaksGeneratedGlobal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 3),
    _AgentMACsecMkaSaksGeneratedGlobal_Type()
)
agentMACsecMkaSaksGeneratedGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSaksGeneratedGlobal.setStatus("current")
_AgentMACsecMkaSaksRekeyedGlobal_Type = Counter64
_AgentMACsecMkaSaksRekeyedGlobal_Object = MibScalar
agentMACsecMkaSaksRekeyedGlobal = _AgentMACsecMkaSaksRekeyedGlobal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 4),
    _AgentMACsecMkaSaksRekeyedGlobal_Type()
)
agentMACsecMkaSaksRekeyedGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSaksRekeyedGlobal.setStatus("current")
_AgentMACsecMkaSaksRxGlobal_Type = Counter64
_AgentMACsecMkaSaksRxGlobal_Object = MibScalar
agentMACsecMkaSaksRxGlobal = _AgentMACsecMkaSaksRxGlobal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 5),
    _AgentMACsecMkaSaksRxGlobal_Type()
)
agentMACsecMkaSaksRxGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSaksRxGlobal.setStatus("current")
_AgentMACsecMkaSakResponsesReceivedGlobal_Type = Counter64
_AgentMACsecMkaSakResponsesReceivedGlobal_Object = MibScalar
agentMACsecMkaSakResponsesReceivedGlobal = _AgentMACsecMkaSakResponsesReceivedGlobal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 6),
    _AgentMACsecMkaSakResponsesReceivedGlobal_Type()
)
agentMACsecMkaSakResponsesReceivedGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSakResponsesReceivedGlobal.setStatus("current")
_AgentMACsecMkaPduValidatedandRxGlobal_Type = Counter64
_AgentMACsecMkaPduValidatedandRxGlobal_Object = MibScalar
agentMACsecMkaPduValidatedandRxGlobal = _AgentMACsecMkaPduValidatedandRxGlobal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 7),
    _AgentMACsecMkaPduValidatedandRxGlobal_Type()
)
agentMACsecMkaPduValidatedandRxGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaPduValidatedandRxGlobal.setStatus("current")
_AgentMACsecMkaMkpduTransmittedGlobal_Type = Counter64
_AgentMACsecMkaMkpduTransmittedGlobal_Object = MibScalar
agentMACsecMkaMkpduTransmittedGlobal = _AgentMACsecMkaMkpduTransmittedGlobal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 8),
    _AgentMACsecMkaMkpduTransmittedGlobal_Type()
)
agentMACsecMkaMkpduTransmittedGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaMkpduTransmittedGlobal.setStatus("current")
_AgentMACseMkaDistributedSakGlobal_Type = Counter64
_AgentMACseMkaDistributedSakGlobal_Object = MibScalar
agentMACseMkaDistributedSakGlobal = _AgentMACseMkaDistributedSakGlobal_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 9),
    _AgentMACseMkaDistributedSakGlobal_Type()
)
agentMACseMkaDistributedSakGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACseMkaDistributedSakGlobal.setStatus("current")
_AgentMACsecMkaSakGenerationFailures_Type = Counter64
_AgentMACsecMkaSakGenerationFailures_Object = MibScalar
agentMACsecMkaSakGenerationFailures = _AgentMACsecMkaSakGenerationFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 10),
    _AgentMACsecMkaSakGenerationFailures_Type()
)
agentMACsecMkaSakGenerationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSakGenerationFailures.setStatus("current")
_AgentMACsecMkaSakEncryptionFailures_Type = Counter64
_AgentMACsecMkaSakEncryptionFailures_Object = MibScalar
agentMACsecMkaSakEncryptionFailures = _AgentMACsecMkaSakEncryptionFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 11),
    _AgentMACsecMkaSakEncryptionFailures_Type()
)
agentMACsecMkaSakEncryptionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSakEncryptionFailures.setStatus("current")
_AgentMACsecMkaSakDecryptionFailures_Type = Counter64
_AgentMACsecMkaSakDecryptionFailures_Object = MibScalar
agentMACsecMkaSakDecryptionFailures = _AgentMACsecMkaSakDecryptionFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 12),
    _AgentMACsecMkaSakDecryptionFailures_Type()
)
agentMACsecMkaSakDecryptionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaSakDecryptionFailures.setStatus("current")
_AgentMACsecMkaIckDerivationFailures_Type = Counter64
_AgentMACsecMkaIckDerivationFailures_Object = MibScalar
agentMACsecMkaIckDerivationFailures = _AgentMACsecMkaIckDerivationFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 13),
    _AgentMACsecMkaIckDerivationFailures_Type()
)
agentMACsecMkaIckDerivationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaIckDerivationFailures.setStatus("current")
_AgentMACsecMkaKekDerivationFailures_Type = Counter64
_AgentMACsecMkaKekDerivationFailures_Object = MibScalar
agentMACsecMkaKekDerivationFailures = _AgentMACsecMkaKekDerivationFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 14),
    _AgentMACsecMkaKekDerivationFailures_Type()
)
agentMACsecMkaKekDerivationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaKekDerivationFailures.setStatus("current")
_AgentMACsecMkaInvalidPeerCapability_Type = Counter64
_AgentMACsecMkaInvalidPeerCapability_Object = MibScalar
agentMACsecMkaInvalidPeerCapability = _AgentMACsecMkaInvalidPeerCapability_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 15),
    _AgentMACsecMkaInvalidPeerCapability_Type()
)
agentMACsecMkaInvalidPeerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaInvalidPeerCapability.setStatus("current")
_AgentMACsecMkaRxScCreationFailures_Type = Counter64
_AgentMACsecMkaRxScCreationFailures_Object = MibScalar
agentMACsecMkaRxScCreationFailures = _AgentMACsecMkaRxScCreationFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 16),
    _AgentMACsecMkaRxScCreationFailures_Type()
)
agentMACsecMkaRxScCreationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaRxScCreationFailures.setStatus("current")
_AgentMACsecMkaTxScCreationFailures_Type = Counter64
_AgentMACsecMkaTxScCreationFailures_Object = MibScalar
agentMACsecMkaTxScCreationFailures = _AgentMACsecMkaTxScCreationFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 17),
    _AgentMACsecMkaTxScCreationFailures_Type()
)
agentMACsecMkaTxScCreationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaTxScCreationFailures.setStatus("current")
_AgentMACsecMkaRxSaInstallationFailures_Type = Counter64
_AgentMACsecMkaRxSaInstallationFailures_Object = MibScalar
agentMACsecMkaRxSaInstallationFailures = _AgentMACsecMkaRxSaInstallationFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 18),
    _AgentMACsecMkaRxSaInstallationFailures_Type()
)
agentMACsecMkaRxSaInstallationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaRxSaInstallationFailures.setStatus("current")
_AgentMACsecMkaTxSaInstallationFailures_Type = Counter64
_AgentMACsecMkaTxSaInstallationFailures_Object = MibScalar
agentMACsecMkaTxSaInstallationFailures = _AgentMACsecMkaTxSaInstallationFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 19),
    _AgentMACsecMkaTxSaInstallationFailures_Type()
)
agentMACsecMkaTxSaInstallationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaTxSaInstallationFailures.setStatus("current")
_AgentMACsecMkaPduTxFailures_Type = Counter64
_AgentMACsecMkaPduTxFailures_Object = MibScalar
agentMACsecMkaPduTxFailures = _AgentMACsecMkaPduTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 20),
    _AgentMACsecMkaPduTxFailures_Type()
)
agentMACsecMkaPduTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaPduTxFailures.setStatus("current")
_AgentMACsecMkaPduRxValidationFailures_Type = Counter64
_AgentMACsecMkaPduRxValidationFailures_Object = MibScalar
agentMACsecMkaPduRxValidationFailures = _AgentMACsecMkaPduRxValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 21),
    _AgentMACsecMkaPduRxValidationFailures_Type()
)
agentMACsecMkaPduRxValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaPduRxValidationFailures.setStatus("current")
_AgentMACsecMkaPduRxPeerMnValidationFailures_Type = Counter64
_AgentMACsecMkaPduRxPeerMnValidationFailures_Object = MibScalar
agentMACsecMkaPduRxPeerMnValidationFailures = _AgentMACsecMkaPduRxPeerMnValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 6, 22),
    _AgentMACsecMkaPduRxPeerMnValidationFailures_Type()
)
agentMACsecMkaPduRxPeerMnValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMACsecMkaPduRxPeerMnValidationFailures.setStatus("current")
_AgentMACsecGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentMACsecGlobalConfigGroup = _AgentMACsecGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 7)
)


class _AgentMACsecDefaultSecureAnnouncements_Type(Integer32):
    """Custom type agentMACsecDefaultSecureAnnouncements based on Integer32"""
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


_AgentMACsecDefaultSecureAnnouncements_Type.__name__ = "Integer32"
_AgentMACsecDefaultSecureAnnouncements_Object = MibScalar
agentMACsecDefaultSecureAnnouncements = _AgentMACsecDefaultSecureAnnouncements_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 78, 7, 1),
    _AgentMACsecDefaultSecureAnnouncements_Type()
)
agentMACsecDefaultSecureAnnouncements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMACsecDefaultSecureAnnouncements.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-MACSEC-MIB",
    **{"MACsecCipherSuite": MACsecCipherSuite,
       "MACsecConfidentialityOffset": MACsecConfidentialityOffset,
       "fastPathMACsec": fastPathMACsec,
       "agentMACsecMKAPolicyConfigGroup": agentMACsecMKAPolicyConfigGroup,
       "agentMACsecMKAPolicyConfigTable": agentMACsecMKAPolicyConfigTable,
       "agentMACsecMKAPolicyConfigEntry": agentMACsecMKAPolicyConfigEntry,
       "agentMACsecMKAPolicyName": agentMACsecMKAPolicyName,
       "agentMACsecMKAPolicyKeyServerPriority": agentMACsecMKAPolicyKeyServerPriority,
       "agentMACsecMKAPolicySecureAnnouncements": agentMACsecMKAPolicySecureAnnouncements,
       "agentMACsecMKAPolicyCipherSuite": agentMACsecMKAPolicyCipherSuite,
       "agentMACsecMKAPolicyConfidentialityOffset": agentMACsecMKAPolicyConfidentialityOffset,
       "agentMACsecMKAPolicyRowStatus": agentMACsecMKAPolicyRowStatus,
       "agentMACsecKeyConfigGroup": agentMACsecKeyConfigGroup,
       "agentMACsecKeyConfigTable": agentMACsecKeyConfigTable,
       "agentMACsecKeyConfigEntry": agentMACsecKeyConfigEntry,
       "agentMACsecKeyChainName": agentMACsecKeyChainName,
       "agentMACsecKeyName": agentMACsecKeyName,
       "agentMACsecKeyCryptographicAlgorithm": agentMACsecKeyCryptographicAlgorithm,
       "agentMACsecKeyString": agentMACsecKeyString,
       "agentMACsecKeyTimeRange": agentMACsecKeyTimeRange,
       "agentMACsecKeyRowStatus": agentMACsecKeyRowStatus,
       "agentMACsecInterfaceConfigGroup": agentMACsecInterfaceConfigGroup,
       "agentMACsecInterfaceConfigTable": agentMACsecInterfaceConfigTable,
       "agentMACsecInterfaceConfigEntry": agentMACsecInterfaceConfigEntry,
       "agentMACsecInterfaceIndex": agentMACsecInterfaceIndex,
       "agentMACsecInterfaceNetworkLink": agentMACsecInterfaceNetworkLink,
       "agentMACsecInterfaceMKAPolicy": agentMACsecInterfaceMKAPolicy,
       "agentMACsecInterfaceKeyChain": agentMACsecInterfaceKeyChain,
       "agentMACsecInterfaceReplayProtection": agentMACsecInterfaceReplayProtection,
       "agentMACsecInterfaceReplayProtectionWindowSize": agentMACsecInterfaceReplayProtectionWindowSize,
       "agentMACsecMkaSessionGroup": agentMACsecMkaSessionGroup,
       "agentMACsecMkaSessionTable": agentMACsecMkaSessionTable,
       "agentMACsecMkaSessionEntry": agentMACsecMkaSessionEntry,
       "agentMACsecMkaInterfaceIndex": agentMACsecMkaInterfaceIndex,
       "agentMACsecMkaPolicy": agentMACsecMkaPolicy,
       "agentMACsecMkaCkn": agentMACsecMkaCkn,
       "agentMACsecMkaLocalTxSci": agentMACsecMkaLocalTxSci,
       "agentMACsecMkaPeerRxSci": agentMACsecMkaPeerRxSci,
       "agentMACsecMkaKeyServer": agentMACsecMkaKeyServer,
       "agentMACsecMkaPeers": agentMACsecMkaPeers,
       "agentMACsecMkaPortStatisticsGroup": agentMACsecMkaPortStatisticsGroup,
       "agentMACsecMkaStatisticsTable": agentMACsecMkaStatisticsTable,
       "agentMACsecMkaStatisticsEntry": agentMACsecMkaStatisticsEntry,
       "agentMACsecMkaSaksGenerated": agentMACsecMkaSaksGenerated,
       "agentMACsecMkaSaksRekeyed": agentMACsecMkaSaksRekeyed,
       "agentMACsecMkaSaksReceived": agentMACsecMkaSaksReceived,
       "agentMACsecMkaSaksResponsesReceived": agentMACsecMkaSaksResponsesReceived,
       "agentMACsecMkaPduValidatedandRx": agentMACsecMkaPduValidatedandRx,
       "agentMACsecMkaPduTransmitted": agentMACsecMkaPduTransmitted,
       "agentMACsecMkaDistributedSAKs": agentMACsecMkaDistributedSAKs,
       "agentMACsecMkaVersionMismatchPkts": agentMACsecMkaVersionMismatchPkts,
       "agentMACsecMkaIcvMismatchPkts": agentMACsecMkaIcvMismatchPkts,
       "agentMACsecMkaMiDuplicatePkts": agentMACsecMkaMiDuplicatePkts,
       "agentMACsecMkaMnDuplicatePkts": agentMACsecMkaMnDuplicatePkts,
       "agentMACsecMkaInvalidDestinationPkts": agentMACsecMkaInvalidDestinationPkts,
       "agentMACsecMkaFormatingErrorPkts": agentMACsecMkaFormatingErrorPkts,
       "agentMACsecMkaGlobalStatisticsGroup": agentMACsecMkaGlobalStatisticsGroup,
       "agentMACsecMkaSessionsSecured": agentMACsecMkaSessionsSecured,
       "agentMACsecMkaSessionsDeleted": agentMACsecMkaSessionsDeleted,
       "agentMACsecMkaSaksGeneratedGlobal": agentMACsecMkaSaksGeneratedGlobal,
       "agentMACsecMkaSaksRekeyedGlobal": agentMACsecMkaSaksRekeyedGlobal,
       "agentMACsecMkaSaksRxGlobal": agentMACsecMkaSaksRxGlobal,
       "agentMACsecMkaSakResponsesReceivedGlobal": agentMACsecMkaSakResponsesReceivedGlobal,
       "agentMACsecMkaPduValidatedandRxGlobal": agentMACsecMkaPduValidatedandRxGlobal,
       "agentMACsecMkaMkpduTransmittedGlobal": agentMACsecMkaMkpduTransmittedGlobal,
       "agentMACseMkaDistributedSakGlobal": agentMACseMkaDistributedSakGlobal,
       "agentMACsecMkaSakGenerationFailures": agentMACsecMkaSakGenerationFailures,
       "agentMACsecMkaSakEncryptionFailures": agentMACsecMkaSakEncryptionFailures,
       "agentMACsecMkaSakDecryptionFailures": agentMACsecMkaSakDecryptionFailures,
       "agentMACsecMkaIckDerivationFailures": agentMACsecMkaIckDerivationFailures,
       "agentMACsecMkaKekDerivationFailures": agentMACsecMkaKekDerivationFailures,
       "agentMACsecMkaInvalidPeerCapability": agentMACsecMkaInvalidPeerCapability,
       "agentMACsecMkaRxScCreationFailures": agentMACsecMkaRxScCreationFailures,
       "agentMACsecMkaTxScCreationFailures": agentMACsecMkaTxScCreationFailures,
       "agentMACsecMkaRxSaInstallationFailures": agentMACsecMkaRxSaInstallationFailures,
       "agentMACsecMkaTxSaInstallationFailures": agentMACsecMkaTxSaInstallationFailures,
       "agentMACsecMkaPduTxFailures": agentMACsecMkaPduTxFailures,
       "agentMACsecMkaPduRxValidationFailures": agentMACsecMkaPduRxValidationFailures,
       "agentMACsecMkaPduRxPeerMnValidationFailures": agentMACsecMkaPduRxPeerMnValidationFailures,
       "agentMACsecGlobalConfigGroup": agentMACsecGlobalConfigGroup,
       "agentMACsecDefaultSecureAnnouncements": agentMACsecDefaultSecureAnnouncements}
)
