# SNMP MIB module (ALCATEL-ENT1-INTERSWITCH-PROTOCOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-INTERSWITCH-PROTOCOL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:09:29 2025
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

(softentIND1Aip,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1Aip")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1InterswitchProtocolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1InterswitchProtocolMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-04-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1InterswitchProtocolMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1InterswitchProtocolMIBObjects = _AlcatelIND1InterswitchProtocolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1)
)
_AlcatelIND1InterswitchProtocolMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1InterswitchProtocolMIBNotifications = _AlcatelIND1InterswitchProtocolMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1InterswitchProtocolMIBNotifications.setStatus("current")
_AipLLDPConfig_ObjectIdentity = ObjectIdentity
aipLLDPConfig = _AipLLDPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1)
)
_AipLLDPConfigManAddrTable_Object = MibTable
aipLLDPConfigManAddrTable = _AipLLDPConfigManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aipLLDPConfigManAddrTable.setStatus("current")
_AipLLDPConfigManAddrEntry_Object = MibTableRow
aipLLDPConfigManAddrEntry = _AipLLDPConfigManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1, 1)
)
aipLLDPConfigManAddrEntry.setIndexNames(
    (0, "ALCATEL-ENT1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigManAddrPortNum"),
)
if mibBuilder.loadTexts:
    aipLLDPConfigManAddrEntry.setStatus("current")
_AipLLDPConfigManAddrPortNum_Type = InterfaceIndex
_AipLLDPConfigManAddrPortNum_Object = MibTableColumn
aipLLDPConfigManAddrPortNum = _AipLLDPConfigManAddrPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1, 1, 1),
    _AipLLDPConfigManAddrPortNum_Type()
)
aipLLDPConfigManAddrPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aipLLDPConfigManAddrPortNum.setStatus("current")


class _AipLLDPConfigManAddrTlvTxEnable_Type(TruthValue):
    """Custom type aipLLDPConfigManAddrTlvTxEnable based on TruthValue"""
    defaultValue = 2


_AipLLDPConfigManAddrTlvTxEnable_Type.__name__ = "TruthValue"
_AipLLDPConfigManAddrTlvTxEnable_Object = MibTableColumn
aipLLDPConfigManAddrTlvTxEnable = _AipLLDPConfigManAddrTlvTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1, 1, 2),
    _AipLLDPConfigManAddrTlvTxEnable_Type()
)
aipLLDPConfigManAddrTlvTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipLLDPConfigManAddrTlvTxEnable.setStatus("current")


class _AipLLDPConfigNearestEdgeEnable_Type(TruthValue):
    """Custom type aipLLDPConfigNearestEdgeEnable based on TruthValue"""
    defaultValue = 2


_AipLLDPConfigNearestEdgeEnable_Type.__name__ = "TruthValue"
_AipLLDPConfigNearestEdgeEnable_Object = MibScalar
aipLLDPConfigNearestEdgeEnable = _AipLLDPConfigNearestEdgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 2),
    _AipLLDPConfigNearestEdgeEnable_Type()
)
aipLLDPConfigNearestEdgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipLLDPConfigNearestEdgeEnable.setStatus("current")
_AlcatelIND1InterswitchProtocolMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1InterswitchProtocolMIBConformance = _AlcatelIND1InterswitchProtocolMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2)
)
_AlcatelIND1InterswitchProtocolMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1InterswitchProtocolMIBGroups = _AlcatelIND1InterswitchProtocolMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 1)
)
_AlcatelIND1InterswitchProtocolMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1InterswitchProtocolMIBCompliances = _AlcatelIND1InterswitchProtocolMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 2)
)

# Managed Objects groups

aipLLDPConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 1, 1)
)
aipLLDPConfGroup.setObjects(
      *(("ALCATEL-ENT1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigManAddrTlvTxEnable"),
        ("ALCATEL-ENT1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigNearestEdgeEnable"))
)
if mibBuilder.loadTexts:
    aipLLDPConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1InterswitchProtocolMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 2, 1)
)
alcatelIND1InterswitchProtocolMIBCompliance.setObjects(
    ("ALCATEL-ENT1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfGroup")
)
if mibBuilder.loadTexts:
    alcatelIND1InterswitchProtocolMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-INTERSWITCH-PROTOCOL-MIB",
    **{"alcatelIND1InterswitchProtocolMIB": alcatelIND1InterswitchProtocolMIB,
       "alcatelIND1InterswitchProtocolMIBObjects": alcatelIND1InterswitchProtocolMIBObjects,
       "alcatelIND1InterswitchProtocolMIBNotifications": alcatelIND1InterswitchProtocolMIBNotifications,
       "aipLLDPConfig": aipLLDPConfig,
       "aipLLDPConfigManAddrTable": aipLLDPConfigManAddrTable,
       "aipLLDPConfigManAddrEntry": aipLLDPConfigManAddrEntry,
       "aipLLDPConfigManAddrPortNum": aipLLDPConfigManAddrPortNum,
       "aipLLDPConfigManAddrTlvTxEnable": aipLLDPConfigManAddrTlvTxEnable,
       "aipLLDPConfigNearestEdgeEnable": aipLLDPConfigNearestEdgeEnable,
       "alcatelIND1InterswitchProtocolMIBConformance": alcatelIND1InterswitchProtocolMIBConformance,
       "alcatelIND1InterswitchProtocolMIBGroups": alcatelIND1InterswitchProtocolMIBGroups,
       "aipLLDPConfGroup": aipLLDPConfGroup,
       "alcatelIND1InterswitchProtocolMIBCompliances": alcatelIND1InterswitchProtocolMIBCompliances,
       "alcatelIND1InterswitchProtocolMIBCompliance": alcatelIND1InterswitchProtocolMIBCompliance}
)
