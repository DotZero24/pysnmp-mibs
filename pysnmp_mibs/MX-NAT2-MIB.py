# SNMP MIB module (MX-NAT2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-NAT2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:17 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxAdvancedIpPort,
 MxEnableState,
 MxIpAddress,
 MxIpPort) = mibBuilder.importSymbols(
    "MX-TC",
    "MxAdvancedIpPort",
    "MxEnableState",
    "MxIpAddress",
    "MxIpPort")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

natMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500)
)
if mibBuilder.loadTexts:
    natMIB.setRevisions(
        ("2006-03-06 00:00",
         "2005-04-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NatMIBObjects_ObjectIdentity = ObjectIdentity
natMIBObjects = _NatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1)
)
_NatPortForwarding_ObjectIdentity = ObjectIdentity
natPortForwarding = _NatPortForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10)
)
_NatPortForwardingTable_Object = MibTable
natPortForwardingTable = _NatPortForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10)
)
if mibBuilder.loadTexts:
    natPortForwardingTable.setStatus("current")
_NatPortForwardingEntry_Object = MibTableRow
natPortForwardingEntry = _NatPortForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10, 5)
)
natPortForwardingEntry.setIndexNames(
    (0, "MX-NAT2-MIB", "natPortForwardingIndex"),
)
if mibBuilder.loadTexts:
    natPortForwardingEntry.setStatus("current")


class _NatPortForwardingIndex_Type(Unsigned32):
    """Custom type natPortForwardingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NatPortForwardingIndex_Type.__name__ = "Unsigned32"
_NatPortForwardingIndex_Object = MibTableColumn
natPortForwardingIndex = _NatPortForwardingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10, 5, 10),
    _NatPortForwardingIndex_Type()
)
natPortForwardingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natPortForwardingIndex.setStatus("current")
_NatPortForwardingWanStartPort_Type = MxIpPort
_NatPortForwardingWanStartPort_Object = MibTableColumn
natPortForwardingWanStartPort = _NatPortForwardingWanStartPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10, 5, 20),
    _NatPortForwardingWanStartPort_Type()
)
natPortForwardingWanStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortForwardingWanStartPort.setStatus("current")
_NatPortForwardingWanFinishPort_Type = MxIpPort
_NatPortForwardingWanFinishPort_Object = MibTableColumn
natPortForwardingWanFinishPort = _NatPortForwardingWanFinishPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10, 5, 30),
    _NatPortForwardingWanFinishPort_Type()
)
natPortForwardingWanFinishPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortForwardingWanFinishPort.setStatus("current")


class _NatPortForwardingProtocol_Type(Integer32):
    """Custom type natPortForwardingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1),
          ("all", 99))
    )


_NatPortForwardingProtocol_Type.__name__ = "Integer32"
_NatPortForwardingProtocol_Object = MibTableColumn
natPortForwardingProtocol = _NatPortForwardingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10, 5, 40),
    _NatPortForwardingProtocol_Type()
)
natPortForwardingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortForwardingProtocol.setStatus("current")
_NatPortForwardingLanAddr_Type = MxIpAddress
_NatPortForwardingLanAddr_Object = MibTableColumn
natPortForwardingLanAddr = _NatPortForwardingLanAddr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10, 5, 50),
    _NatPortForwardingLanAddr_Type()
)
natPortForwardingLanAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortForwardingLanAddr.setStatus("current")


class _NatPortForwardingLanPort_Type(MxAdvancedIpPort):
    """Custom type natPortForwardingLanPort based on MxAdvancedIpPort"""
    defaultValue = 0


_NatPortForwardingLanPort_Type.__name__ = "MxAdvancedIpPort"
_NatPortForwardingLanPort_Object = MibTableColumn
natPortForwardingLanPort = _NatPortForwardingLanPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10, 5, 60),
    _NatPortForwardingLanPort_Type()
)
natPortForwardingLanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortForwardingLanPort.setStatus("current")


class _NatPortForwardingRuleLabel_Type(OctetString):
    """Custom type natPortForwardingRuleLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NatPortForwardingRuleLabel_Type.__name__ = "OctetString"
_NatPortForwardingRuleLabel_Object = MibTableColumn
natPortForwardingRuleLabel = _NatPortForwardingRuleLabel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10, 5, 70),
    _NatPortForwardingRuleLabel_Type()
)
natPortForwardingRuleLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortForwardingRuleLabel.setStatus("current")


class _NatPortForwardingRuleEnable_Type(MxEnableState):
    """Custom type natPortForwardingRuleEnable based on MxEnableState"""
    defaultValue = 0


_NatPortForwardingRuleEnable_Type.__name__ = "MxEnableState"
_NatPortForwardingRuleEnable_Object = MibTableColumn
natPortForwardingRuleEnable = _NatPortForwardingRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 10, 10, 5, 80),
    _NatPortForwardingRuleEnable_Type()
)
natPortForwardingRuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natPortForwardingRuleEnable.setStatus("current")
_NatSyslog_ObjectIdentity = ObjectIdentity
natSyslog = _NatSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 100)
)


class _NatSyslogEnable_Type(MxEnableState):
    """Custom type natSyslogEnable based on MxEnableState"""
    defaultValue = 0


_NatSyslogEnable_Type.__name__ = "MxEnableState"
_NatSyslogEnable_Object = MibScalar
natSyslogEnable = _NatSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 1, 100, 10),
    _NatSyslogEnable_Type()
)
natSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natSyslogEnable.setStatus("current")
_NatConformance_ObjectIdentity = ObjectIdentity
natConformance = _NatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 2)
)
_NatCompliances_ObjectIdentity = ObjectIdentity
natCompliances = _NatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 2, 1)
)
_NatGroups_ObjectIdentity = ObjectIdentity
natGroups = _NatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 2, 2)
)

# Managed Objects groups

natPortForwardingGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 2, 2, 1)
)
natPortForwardingGroupVer1.setObjects(
      *(("MX-NAT2-MIB", "natPortForwardingWanStartPort"),
        ("MX-NAT2-MIB", "natPortForwardingWanFinishPort"),
        ("MX-NAT2-MIB", "natPortForwardingProtocol"),
        ("MX-NAT2-MIB", "natPortForwardingLanAddr"),
        ("MX-NAT2-MIB", "natPortForwardingLanPort"),
        ("MX-NAT2-MIB", "natPortForwardingRuleLabel"),
        ("MX-NAT2-MIB", "natPortForwardingRuleEnable"))
)
if mibBuilder.loadTexts:
    natPortForwardingGroupVer1.setStatus("current")

natSyslogGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 2, 2, 2)
)
natSyslogGroupVer1.setObjects(
    ("MX-NAT2-MIB", "natSyslogEnable")
)
if mibBuilder.loadTexts:
    natSyslogGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

natComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 500, 2, 1, 1)
)
natComplVer1.setObjects(
      *(("MX-NAT2-MIB", "natPortForwardingGroupVer1"),
        ("MX-NAT2-MIB", "natSyslogGroupVer1"))
)
if mibBuilder.loadTexts:
    natComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-NAT2-MIB",
    **{"natMIB": natMIB,
       "natMIBObjects": natMIBObjects,
       "natPortForwarding": natPortForwarding,
       "natPortForwardingTable": natPortForwardingTable,
       "natPortForwardingEntry": natPortForwardingEntry,
       "natPortForwardingIndex": natPortForwardingIndex,
       "natPortForwardingWanStartPort": natPortForwardingWanStartPort,
       "natPortForwardingWanFinishPort": natPortForwardingWanFinishPort,
       "natPortForwardingProtocol": natPortForwardingProtocol,
       "natPortForwardingLanAddr": natPortForwardingLanAddr,
       "natPortForwardingLanPort": natPortForwardingLanPort,
       "natPortForwardingRuleLabel": natPortForwardingRuleLabel,
       "natPortForwardingRuleEnable": natPortForwardingRuleEnable,
       "natSyslog": natSyslog,
       "natSyslogEnable": natSyslogEnable,
       "natConformance": natConformance,
       "natCompliances": natCompliances,
       "natComplVer1": natComplVer1,
       "natGroups": natGroups,
       "natPortForwardingGroupVer1": natPortForwardingGroupVer1,
       "natSyslogGroupVer1": natSyslogGroupVer1}
)
