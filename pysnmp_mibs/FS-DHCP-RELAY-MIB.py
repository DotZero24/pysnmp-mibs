# SNMP MIB module (FS-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-DHCP-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:46 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104)
)
if mibBuilder.loadTexts:
    fsDhcpMIB.setRevisions(
        ("2011-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDhcpMIBObjects_ObjectIdentity = ObjectIdentity
fsDhcpMIBObjects = _FsDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1)
)
if mibBuilder.loadTexts:
    fsDhcpMIBObjects.setStatus("current")
_FsDhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
fsDhcpRelayMIBObjects = _FsDhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1)
)
if mibBuilder.loadTexts:
    fsDhcpRelayMIBObjects.setStatus("current")


class _FsDHCPRelayCycleStatus_Type(Integer32):
    """Custom type fsDHCPRelayCycleStatus based on Integer32"""
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


_FsDHCPRelayCycleStatus_Type.__name__ = "Integer32"
_FsDHCPRelayCycleStatus_Object = MibScalar
fsDHCPRelayCycleStatus = _FsDHCPRelayCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 1),
    _FsDHCPRelayCycleStatus_Type()
)
fsDHCPRelayCycleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDHCPRelayCycleStatus.setStatus("current")
_FsDhcpRelayCounters_ObjectIdentity = ObjectIdentity
fsDhcpRelayCounters = _FsDhcpRelayCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsDhcpRelayCounters.setStatus("current")
_FsDHCPRRxBadPktNum_Type = Integer32
_FsDHCPRRxBadPktNum_Object = MibScalar
fsDHCPRRxBadPktNum = _FsDHCPRRxBadPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 1),
    _FsDHCPRRxBadPktNum_Type()
)
fsDHCPRRxBadPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRRxBadPktNum.setStatus("current")
_FsDHCPRRxServerPktNum_Type = Integer32
_FsDHCPRRxServerPktNum_Object = MibScalar
fsDHCPRRxServerPktNum = _FsDHCPRRxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 2),
    _FsDHCPRRxServerPktNum_Type()
)
fsDHCPRRxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRRxServerPktNum.setStatus("current")
_FsDHCPRTxServerPktNum_Type = Integer32
_FsDHCPRTxServerPktNum_Object = MibScalar
fsDHCPRTxServerPktNum = _FsDHCPRTxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 3),
    _FsDHCPRTxServerPktNum_Type()
)
fsDHCPRTxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRTxServerPktNum.setStatus("current")
_FsDHCPRRxClientPktNum_Type = Integer32
_FsDHCPRRxClientPktNum_Object = MibScalar
fsDHCPRRxClientPktNum = _FsDHCPRRxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 4),
    _FsDHCPRRxClientPktNum_Type()
)
fsDHCPRRxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRRxClientPktNum.setStatus("current")
_FsDHCPRTxClientPktNum_Type = Integer32
_FsDHCPRTxClientPktNum_Object = MibScalar
fsDHCPRTxClientPktNum = _FsDHCPRTxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 5),
    _FsDHCPRTxClientPktNum_Type()
)
fsDHCPRTxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRTxClientPktNum.setStatus("current")
_FsDHCPRRxClientUniPktNum_Type = Integer32
_FsDHCPRRxClientUniPktNum_Object = MibScalar
fsDHCPRRxClientUniPktNum = _FsDHCPRRxClientUniPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 6),
    _FsDHCPRRxClientUniPktNum_Type()
)
fsDHCPRRxClientUniPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRRxClientUniPktNum.setStatus("current")
_FsDHCPRRxClientBroPktNum_Type = Integer32
_FsDHCPRRxClientBroPktNum_Object = MibScalar
fsDHCPRRxClientBroPktNum = _FsDHCPRRxClientBroPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 7),
    _FsDHCPRRxClientBroPktNum_Type()
)
fsDHCPRRxClientBroPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRRxClientBroPktNum.setStatus("current")
_FsDHCPRTxClientUniPktNum_Type = Integer32
_FsDHCPRTxClientUniPktNum_Object = MibScalar
fsDHCPRTxClientUniPktNum = _FsDHCPRTxClientUniPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 8),
    _FsDHCPRTxClientUniPktNum_Type()
)
fsDHCPRTxClientUniPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRTxClientUniPktNum.setStatus("current")
_FsDHCPRTxClientBroPktNum_Type = Integer32
_FsDHCPRTxClientBroPktNum_Object = MibScalar
fsDHCPRTxClientBroPktNum = _FsDHCPRTxClientBroPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 9),
    _FsDHCPRTxClientBroPktNum_Type()
)
fsDHCPRTxClientBroPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRTxClientBroPktNum.setStatus("current")
_FsDHCPRelayDiscoverPktNum_Type = Integer32
_FsDHCPRelayDiscoverPktNum_Object = MibScalar
fsDHCPRelayDiscoverPktNum = _FsDHCPRelayDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 10),
    _FsDHCPRelayDiscoverPktNum_Type()
)
fsDHCPRelayDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRelayDiscoverPktNum.setStatus("current")
_FsDHCPRelayRequestPktNum_Type = Integer32
_FsDHCPRelayRequestPktNum_Object = MibScalar
fsDHCPRelayRequestPktNum = _FsDHCPRelayRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 11),
    _FsDHCPRelayRequestPktNum_Type()
)
fsDHCPRelayRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRelayRequestPktNum.setStatus("current")
_FsDHCPRelayDeclinePktNum_Type = Integer32
_FsDHCPRelayDeclinePktNum_Object = MibScalar
fsDHCPRelayDeclinePktNum = _FsDHCPRelayDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 12),
    _FsDHCPRelayDeclinePktNum_Type()
)
fsDHCPRelayDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRelayDeclinePktNum.setStatus("current")
_FsDHCPRelayReleasePktNum_Type = Integer32
_FsDHCPRelayReleasePktNum_Object = MibScalar
fsDHCPRelayReleasePktNum = _FsDHCPRelayReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 13),
    _FsDHCPRelayReleasePktNum_Type()
)
fsDHCPRelayReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRelayReleasePktNum.setStatus("current")
_FsDHCPRelayInformPktNum_Type = Integer32
_FsDHCPRelayInformPktNum_Object = MibScalar
fsDHCPRelayInformPktNum = _FsDHCPRelayInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 14),
    _FsDHCPRelayInformPktNum_Type()
)
fsDHCPRelayInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRelayInformPktNum.setStatus("current")
_FsDHCPRelayOfferPktNum_Type = Integer32
_FsDHCPRelayOfferPktNum_Object = MibScalar
fsDHCPRelayOfferPktNum = _FsDHCPRelayOfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 15),
    _FsDHCPRelayOfferPktNum_Type()
)
fsDHCPRelayOfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRelayOfferPktNum.setStatus("current")
_FsDHCPRelayAckPktNum_Type = Integer32
_FsDHCPRelayAckPktNum_Object = MibScalar
fsDHCPRelayAckPktNum = _FsDHCPRelayAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 16),
    _FsDHCPRelayAckPktNum_Type()
)
fsDHCPRelayAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRelayAckPktNum.setStatus("current")
_FsDHCPRelayNakPktNum_Type = Integer32
_FsDHCPRelayNakPktNum_Object = MibScalar
fsDHCPRelayNakPktNum = _FsDHCPRelayNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 1, 1, 2, 17),
    _FsDHCPRelayNakPktNum_Type()
)
fsDHCPRelayNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDHCPRelayNakPktNum.setStatus("current")
_FsDhcpMIBConformance_ObjectIdentity = ObjectIdentity
fsDhcpMIBConformance = _FsDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 2)
)
if mibBuilder.loadTexts:
    fsDhcpMIBConformance.setStatus("current")
_FsDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
fsDhcpMIBCompliances = _FsDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 2, 1)
)
_FsDhcpMIBGroups_ObjectIdentity = ObjectIdentity
fsDhcpMIBGroups = _FsDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 2, 2)
)

# Managed Objects groups

fsDhcpRelayCountersObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 2, 2, 1)
)
fsDhcpRelayCountersObjects.setObjects(
      *(("FS-DHCP-RELAY-MIB", "fsDHCPRelayCycleStatus"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRRxBadPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRRxServerPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRTxServerPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRRxClientPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRTxClientPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRRxClientUniPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRRxClientBroPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRTxClientUniPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRTxClientBroPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRelayDiscoverPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRelayRequestPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRelayDeclinePktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRelayReleasePktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRelayInformPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRelayOfferPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRelayAckPktNum"),
        ("FS-DHCP-RELAY-MIB", "fsDHCPRelayNakPktNum"))
)
if mibBuilder.loadTexts:
    fsDhcpRelayCountersObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsDhcpRelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 104, 2, 1, 1)
)
fsDhcpRelayCompliance.setObjects(
    ("FS-DHCP-RELAY-MIB", "fsDhcpRelayCountersObjects")
)
if mibBuilder.loadTexts:
    fsDhcpRelayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-DHCP-RELAY-MIB",
    **{"fsDhcpMIB": fsDhcpMIB,
       "fsDhcpMIBObjects": fsDhcpMIBObjects,
       "fsDhcpRelayMIBObjects": fsDhcpRelayMIBObjects,
       "fsDHCPRelayCycleStatus": fsDHCPRelayCycleStatus,
       "fsDhcpRelayCounters": fsDhcpRelayCounters,
       "fsDHCPRRxBadPktNum": fsDHCPRRxBadPktNum,
       "fsDHCPRRxServerPktNum": fsDHCPRRxServerPktNum,
       "fsDHCPRTxServerPktNum": fsDHCPRTxServerPktNum,
       "fsDHCPRRxClientPktNum": fsDHCPRRxClientPktNum,
       "fsDHCPRTxClientPktNum": fsDHCPRTxClientPktNum,
       "fsDHCPRRxClientUniPktNum": fsDHCPRRxClientUniPktNum,
       "fsDHCPRRxClientBroPktNum": fsDHCPRRxClientBroPktNum,
       "fsDHCPRTxClientUniPktNum": fsDHCPRTxClientUniPktNum,
       "fsDHCPRTxClientBroPktNum": fsDHCPRTxClientBroPktNum,
       "fsDHCPRelayDiscoverPktNum": fsDHCPRelayDiscoverPktNum,
       "fsDHCPRelayRequestPktNum": fsDHCPRelayRequestPktNum,
       "fsDHCPRelayDeclinePktNum": fsDHCPRelayDeclinePktNum,
       "fsDHCPRelayReleasePktNum": fsDHCPRelayReleasePktNum,
       "fsDHCPRelayInformPktNum": fsDHCPRelayInformPktNum,
       "fsDHCPRelayOfferPktNum": fsDHCPRelayOfferPktNum,
       "fsDHCPRelayAckPktNum": fsDHCPRelayAckPktNum,
       "fsDHCPRelayNakPktNum": fsDHCPRelayNakPktNum,
       "fsDhcpMIBConformance": fsDhcpMIBConformance,
       "fsDhcpMIBCompliances": fsDhcpMIBCompliances,
       "fsDhcpRelayCompliance": fsDhcpRelayCompliance,
       "fsDhcpMIBGroups": fsDhcpMIBGroups,
       "fsDhcpRelayCountersObjects": fsDhcpRelayCountersObjects}
)
