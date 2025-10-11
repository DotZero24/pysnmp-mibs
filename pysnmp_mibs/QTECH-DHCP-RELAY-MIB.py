# SNMP MIB module (QTECH-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-DHCP-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:52 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104)
)
if mibBuilder.loadTexts:
    qtechDhcpMIB.setRevisions(
        ("2011-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechDhcpMIBObjects_ObjectIdentity = ObjectIdentity
qtechDhcpMIBObjects = _QtechDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1)
)
if mibBuilder.loadTexts:
    qtechDhcpMIBObjects.setStatus("current")
_QtechDhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
qtechDhcpRelayMIBObjects = _QtechDhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1)
)
if mibBuilder.loadTexts:
    qtechDhcpRelayMIBObjects.setStatus("current")


class _QtechDHCPRelayCycleStatus_Type(Integer32):
    """Custom type qtechDHCPRelayCycleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_QtechDHCPRelayCycleStatus_Type.__name__ = "Integer32"
_QtechDHCPRelayCycleStatus_Object = MibScalar
qtechDHCPRelayCycleStatus = _QtechDHCPRelayCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 1),
    _QtechDHCPRelayCycleStatus_Type()
)
qtechDHCPRelayCycleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDHCPRelayCycleStatus.setStatus("current")
_QtechDhcpRelayCounters_ObjectIdentity = ObjectIdentity
qtechDhcpRelayCounters = _QtechDhcpRelayCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qtechDhcpRelayCounters.setStatus("current")
_QtechDHCPRRxBadPktNum_Type = Integer32
_QtechDHCPRRxBadPktNum_Object = MibScalar
qtechDHCPRRxBadPktNum = _QtechDHCPRRxBadPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 1),
    _QtechDHCPRRxBadPktNum_Type()
)
qtechDHCPRRxBadPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRRxBadPktNum.setStatus("current")
_QtechDHCPRRxServerPktNum_Type = Integer32
_QtechDHCPRRxServerPktNum_Object = MibScalar
qtechDHCPRRxServerPktNum = _QtechDHCPRRxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 2),
    _QtechDHCPRRxServerPktNum_Type()
)
qtechDHCPRRxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRRxServerPktNum.setStatus("current")
_QtechDHCPRTxServerPktNum_Type = Integer32
_QtechDHCPRTxServerPktNum_Object = MibScalar
qtechDHCPRTxServerPktNum = _QtechDHCPRTxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 3),
    _QtechDHCPRTxServerPktNum_Type()
)
qtechDHCPRTxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRTxServerPktNum.setStatus("current")
_QtechDHCPRRxClientPktNum_Type = Integer32
_QtechDHCPRRxClientPktNum_Object = MibScalar
qtechDHCPRRxClientPktNum = _QtechDHCPRRxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 4),
    _QtechDHCPRRxClientPktNum_Type()
)
qtechDHCPRRxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRRxClientPktNum.setStatus("current")
_QtechDHCPRTxClientPktNum_Type = Integer32
_QtechDHCPRTxClientPktNum_Object = MibScalar
qtechDHCPRTxClientPktNum = _QtechDHCPRTxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 5),
    _QtechDHCPRTxClientPktNum_Type()
)
qtechDHCPRTxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRTxClientPktNum.setStatus("current")
_QtechDHCPRRxClientUniPktNum_Type = Integer32
_QtechDHCPRRxClientUniPktNum_Object = MibScalar
qtechDHCPRRxClientUniPktNum = _QtechDHCPRRxClientUniPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 6),
    _QtechDHCPRRxClientUniPktNum_Type()
)
qtechDHCPRRxClientUniPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRRxClientUniPktNum.setStatus("current")
_QtechDHCPRRxClientBroPktNum_Type = Integer32
_QtechDHCPRRxClientBroPktNum_Object = MibScalar
qtechDHCPRRxClientBroPktNum = _QtechDHCPRRxClientBroPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 7),
    _QtechDHCPRRxClientBroPktNum_Type()
)
qtechDHCPRRxClientBroPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRRxClientBroPktNum.setStatus("current")
_QtechDHCPRTxClientUniPktNum_Type = Integer32
_QtechDHCPRTxClientUniPktNum_Object = MibScalar
qtechDHCPRTxClientUniPktNum = _QtechDHCPRTxClientUniPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 8),
    _QtechDHCPRTxClientUniPktNum_Type()
)
qtechDHCPRTxClientUniPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRTxClientUniPktNum.setStatus("current")
_QtechDHCPRTxClientBroPktNum_Type = Integer32
_QtechDHCPRTxClientBroPktNum_Object = MibScalar
qtechDHCPRTxClientBroPktNum = _QtechDHCPRTxClientBroPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 9),
    _QtechDHCPRTxClientBroPktNum_Type()
)
qtechDHCPRTxClientBroPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRTxClientBroPktNum.setStatus("current")
_QtechDHCPRelayDiscoverPktNum_Type = Integer32
_QtechDHCPRelayDiscoverPktNum_Object = MibScalar
qtechDHCPRelayDiscoverPktNum = _QtechDHCPRelayDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 10),
    _QtechDHCPRelayDiscoverPktNum_Type()
)
qtechDHCPRelayDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRelayDiscoverPktNum.setStatus("current")
_QtechDHCPRelayRequestPktNum_Type = Integer32
_QtechDHCPRelayRequestPktNum_Object = MibScalar
qtechDHCPRelayRequestPktNum = _QtechDHCPRelayRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 11),
    _QtechDHCPRelayRequestPktNum_Type()
)
qtechDHCPRelayRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRelayRequestPktNum.setStatus("current")
_QtechDHCPRelayDeclinePktNum_Type = Integer32
_QtechDHCPRelayDeclinePktNum_Object = MibScalar
qtechDHCPRelayDeclinePktNum = _QtechDHCPRelayDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 12),
    _QtechDHCPRelayDeclinePktNum_Type()
)
qtechDHCPRelayDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRelayDeclinePktNum.setStatus("current")
_QtechDHCPRelayReleasePktNum_Type = Integer32
_QtechDHCPRelayReleasePktNum_Object = MibScalar
qtechDHCPRelayReleasePktNum = _QtechDHCPRelayReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 13),
    _QtechDHCPRelayReleasePktNum_Type()
)
qtechDHCPRelayReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRelayReleasePktNum.setStatus("current")
_QtechDHCPRelayInformPktNum_Type = Integer32
_QtechDHCPRelayInformPktNum_Object = MibScalar
qtechDHCPRelayInformPktNum = _QtechDHCPRelayInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 14),
    _QtechDHCPRelayInformPktNum_Type()
)
qtechDHCPRelayInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRelayInformPktNum.setStatus("current")
_QtechDHCPRelayOfferPktNum_Type = Integer32
_QtechDHCPRelayOfferPktNum_Object = MibScalar
qtechDHCPRelayOfferPktNum = _QtechDHCPRelayOfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 15),
    _QtechDHCPRelayOfferPktNum_Type()
)
qtechDHCPRelayOfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRelayOfferPktNum.setStatus("current")
_QtechDHCPRelayAckPktNum_Type = Integer32
_QtechDHCPRelayAckPktNum_Object = MibScalar
qtechDHCPRelayAckPktNum = _QtechDHCPRelayAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 16),
    _QtechDHCPRelayAckPktNum_Type()
)
qtechDHCPRelayAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRelayAckPktNum.setStatus("current")
_QtechDHCPRelayNakPktNum_Type = Integer32
_QtechDHCPRelayNakPktNum_Object = MibScalar
qtechDHCPRelayNakPktNum = _QtechDHCPRelayNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 1, 1, 2, 17),
    _QtechDHCPRelayNakPktNum_Type()
)
qtechDHCPRelayNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDHCPRelayNakPktNum.setStatus("current")
_QtechDhcpMIBConformance_ObjectIdentity = ObjectIdentity
qtechDhcpMIBConformance = _QtechDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 2)
)
if mibBuilder.loadTexts:
    qtechDhcpMIBConformance.setStatus("current")
_QtechDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
qtechDhcpMIBCompliances = _QtechDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 2, 1)
)
_QtechDhcpMIBGroups_ObjectIdentity = ObjectIdentity
qtechDhcpMIBGroups = _QtechDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 2, 2)
)

# Managed Objects groups

qtechDhcpRelayCountersObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 2, 2, 1)
)
qtechDhcpRelayCountersObjects.setObjects(
      *(("QTECH-DHCP-RELAY-MIB", "qtechDHCPRelayCycleStatus"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRRxBadPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRRxServerPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRTxServerPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRRxClientPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRTxClientPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRRxClientUniPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRRxClientBroPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRTxClientUniPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRTxClientBroPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRelayDiscoverPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRelayRequestPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRelayDeclinePktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRelayReleasePktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRelayInformPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRelayOfferPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRelayAckPktNum"),
        ("QTECH-DHCP-RELAY-MIB", "qtechDHCPRelayNakPktNum"))
)
if mibBuilder.loadTexts:
    qtechDhcpRelayCountersObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechDhcpRelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 104, 2, 1, 1)
)
qtechDhcpRelayCompliance.setObjects(
    ("QTECH-DHCP-RELAY-MIB", "qtechDhcpRelayCountersObjects")
)
if mibBuilder.loadTexts:
    qtechDhcpRelayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-DHCP-RELAY-MIB",
    **{"qtechDhcpMIB": qtechDhcpMIB,
       "qtechDhcpMIBObjects": qtechDhcpMIBObjects,
       "qtechDhcpRelayMIBObjects": qtechDhcpRelayMIBObjects,
       "qtechDHCPRelayCycleStatus": qtechDHCPRelayCycleStatus,
       "qtechDhcpRelayCounters": qtechDhcpRelayCounters,
       "qtechDHCPRRxBadPktNum": qtechDHCPRRxBadPktNum,
       "qtechDHCPRRxServerPktNum": qtechDHCPRRxServerPktNum,
       "qtechDHCPRTxServerPktNum": qtechDHCPRTxServerPktNum,
       "qtechDHCPRRxClientPktNum": qtechDHCPRRxClientPktNum,
       "qtechDHCPRTxClientPktNum": qtechDHCPRTxClientPktNum,
       "qtechDHCPRRxClientUniPktNum": qtechDHCPRRxClientUniPktNum,
       "qtechDHCPRRxClientBroPktNum": qtechDHCPRRxClientBroPktNum,
       "qtechDHCPRTxClientUniPktNum": qtechDHCPRTxClientUniPktNum,
       "qtechDHCPRTxClientBroPktNum": qtechDHCPRTxClientBroPktNum,
       "qtechDHCPRelayDiscoverPktNum": qtechDHCPRelayDiscoverPktNum,
       "qtechDHCPRelayRequestPktNum": qtechDHCPRelayRequestPktNum,
       "qtechDHCPRelayDeclinePktNum": qtechDHCPRelayDeclinePktNum,
       "qtechDHCPRelayReleasePktNum": qtechDHCPRelayReleasePktNum,
       "qtechDHCPRelayInformPktNum": qtechDHCPRelayInformPktNum,
       "qtechDHCPRelayOfferPktNum": qtechDHCPRelayOfferPktNum,
       "qtechDHCPRelayAckPktNum": qtechDHCPRelayAckPktNum,
       "qtechDHCPRelayNakPktNum": qtechDHCPRelayNakPktNum,
       "qtechDhcpMIBConformance": qtechDhcpMIBConformance,
       "qtechDhcpMIBCompliances": qtechDhcpMIBCompliances,
       "qtechDhcpRelayCompliance": qtechDhcpRelayCompliance,
       "qtechDhcpMIBGroups": qtechDhcpMIBGroups,
       "qtechDhcpRelayCountersObjects": qtechDhcpRelayCountersObjects}
)
