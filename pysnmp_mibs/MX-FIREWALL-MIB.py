# SNMP MIB module (MX-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-FIREWALL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:40 2025
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

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

firewallMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450)
)
if mibBuilder.loadTexts:
    firewallMIB.setRevisions(
        ("2006-03-06 00:00",
         "2005-04-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FirewallMIBObjects_ObjectIdentity = ObjectIdentity
firewallMIBObjects = _FirewallMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1)
)


class _FirewallEnable_Type(MxEnableState):
    """Custom type firewallEnable based on MxEnableState"""
    defaultValue = 1


_FirewallEnable_Type.__name__ = "MxEnableState"
_FirewallEnable_Object = MibScalar
firewallEnable = _FirewallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 10),
    _FirewallEnable_Type()
)
firewallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallEnable.setStatus("current")
_FirewallSecurity_ObjectIdentity = ObjectIdentity
firewallSecurity = _FirewallSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100)
)


class _FirewallSecurityBadTcpPacketRule_Type(MxEnableState):
    """Custom type firewallSecurityBadTcpPacketRule based on MxEnableState"""
    defaultValue = 1


_FirewallSecurityBadTcpPacketRule_Type.__name__ = "MxEnableState"
_FirewallSecurityBadTcpPacketRule_Object = MibScalar
firewallSecurityBadTcpPacketRule = _FirewallSecurityBadTcpPacketRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 10),
    _FirewallSecurityBadTcpPacketRule_Type()
)
firewallSecurityBadTcpPacketRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityBadTcpPacketRule.setStatus("current")


class _FirewallSecurityTcpSynCookiesRule_Type(MxEnableState):
    """Custom type firewallSecurityTcpSynCookiesRule based on MxEnableState"""
    defaultValue = 1


_FirewallSecurityTcpSynCookiesRule_Type.__name__ = "MxEnableState"
_FirewallSecurityTcpSynCookiesRule_Object = MibScalar
firewallSecurityTcpSynCookiesRule = _FirewallSecurityTcpSynCookiesRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 20),
    _FirewallSecurityTcpSynCookiesRule_Type()
)
firewallSecurityTcpSynCookiesRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityTcpSynCookiesRule.setStatus("current")


class _FirewallSecuritySourceRoutedPacketRule_Type(MxEnableState):
    """Custom type firewallSecuritySourceRoutedPacketRule based on MxEnableState"""
    defaultValue = 0


_FirewallSecuritySourceRoutedPacketRule_Type.__name__ = "MxEnableState"
_FirewallSecuritySourceRoutedPacketRule_Object = MibScalar
firewallSecuritySourceRoutedPacketRule = _FirewallSecuritySourceRoutedPacketRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 30),
    _FirewallSecuritySourceRoutedPacketRule_Type()
)
firewallSecuritySourceRoutedPacketRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecuritySourceRoutedPacketRule.setStatus("current")


class _FirewallSecurityMulticastPacketRule_Type(MxEnableState):
    """Custom type firewallSecurityMulticastPacketRule based on MxEnableState"""
    defaultValue = 1


_FirewallSecurityMulticastPacketRule_Type.__name__ = "MxEnableState"
_FirewallSecurityMulticastPacketRule_Object = MibScalar
firewallSecurityMulticastPacketRule = _FirewallSecurityMulticastPacketRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 40),
    _FirewallSecurityMulticastPacketRule_Type()
)
firewallSecurityMulticastPacketRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityMulticastPacketRule.setStatus("current")


class _FirewallSecurityIdentRule_Type(MxEnableState):
    """Custom type firewallSecurityIdentRule based on MxEnableState"""
    defaultValue = 1


_FirewallSecurityIdentRule_Type.__name__ = "MxEnableState"
_FirewallSecurityIdentRule_Object = MibScalar
firewallSecurityIdentRule = _FirewallSecurityIdentRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 50),
    _FirewallSecurityIdentRule_Type()
)
firewallSecurityIdentRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityIdentRule.setStatus("current")


class _FirewallSecurityReversePathFilteringRule_Type(MxEnableState):
    """Custom type firewallSecurityReversePathFilteringRule based on MxEnableState"""
    defaultValue = 0


_FirewallSecurityReversePathFilteringRule_Type.__name__ = "MxEnableState"
_FirewallSecurityReversePathFilteringRule_Object = MibScalar
firewallSecurityReversePathFilteringRule = _FirewallSecurityReversePathFilteringRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 60),
    _FirewallSecurityReversePathFilteringRule_Type()
)
firewallSecurityReversePathFilteringRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityReversePathFilteringRule.setStatus("current")


class _FirewallSecurityBlockWanEchoRequestRule_Type(MxEnableState):
    """Custom type firewallSecurityBlockWanEchoRequestRule based on MxEnableState"""
    defaultValue = 0


_FirewallSecurityBlockWanEchoRequestRule_Type.__name__ = "MxEnableState"
_FirewallSecurityBlockWanEchoRequestRule_Object = MibScalar
firewallSecurityBlockWanEchoRequestRule = _FirewallSecurityBlockWanEchoRequestRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 70),
    _FirewallSecurityBlockWanEchoRequestRule_Type()
)
firewallSecurityBlockWanEchoRequestRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityBlockWanEchoRequestRule.setStatus("current")


class _FirewallSecurityBlockLanEchoRequestRule_Type(MxEnableState):
    """Custom type firewallSecurityBlockLanEchoRequestRule based on MxEnableState"""
    defaultValue = 0


_FirewallSecurityBlockLanEchoRequestRule_Type.__name__ = "MxEnableState"
_FirewallSecurityBlockLanEchoRequestRule_Object = MibScalar
firewallSecurityBlockLanEchoRequestRule = _FirewallSecurityBlockLanEchoRequestRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 80),
    _FirewallSecurityBlockLanEchoRequestRule_Type()
)
firewallSecurityBlockLanEchoRequestRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityBlockLanEchoRequestRule.setStatus("current")


class _FirewallSecurityBlockWanEchoBroadcastRule_Type(MxEnableState):
    """Custom type firewallSecurityBlockWanEchoBroadcastRule based on MxEnableState"""
    defaultValue = 1


_FirewallSecurityBlockWanEchoBroadcastRule_Type.__name__ = "MxEnableState"
_FirewallSecurityBlockWanEchoBroadcastRule_Object = MibScalar
firewallSecurityBlockWanEchoBroadcastRule = _FirewallSecurityBlockWanEchoBroadcastRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 90),
    _FirewallSecurityBlockWanEchoBroadcastRule_Type()
)
firewallSecurityBlockWanEchoBroadcastRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityBlockWanEchoBroadcastRule.setStatus("current")


class _FirewallSecurityBlockIcmpRedirectionInRule_Type(MxEnableState):
    """Custom type firewallSecurityBlockIcmpRedirectionInRule based on MxEnableState"""
    defaultValue = 1


_FirewallSecurityBlockIcmpRedirectionInRule_Type.__name__ = "MxEnableState"
_FirewallSecurityBlockIcmpRedirectionInRule_Object = MibScalar
firewallSecurityBlockIcmpRedirectionInRule = _FirewallSecurityBlockIcmpRedirectionInRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 100),
    _FirewallSecurityBlockIcmpRedirectionInRule_Type()
)
firewallSecurityBlockIcmpRedirectionInRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityBlockIcmpRedirectionInRule.setStatus("current")


class _FirewallSecurityBlockIcmpRedirectionOutRule_Type(MxEnableState):
    """Custom type firewallSecurityBlockIcmpRedirectionOutRule based on MxEnableState"""
    defaultValue = 1


_FirewallSecurityBlockIcmpRedirectionOutRule_Type.__name__ = "MxEnableState"
_FirewallSecurityBlockIcmpRedirectionOutRule_Object = MibScalar
firewallSecurityBlockIcmpRedirectionOutRule = _FirewallSecurityBlockIcmpRedirectionOutRule_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 110),
    _FirewallSecurityBlockIcmpRedirectionOutRule_Type()
)
firewallSecurityBlockIcmpRedirectionOutRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecurityBlockIcmpRedirectionOutRule.setStatus("current")
_FirewallSecuritySpoof_ObjectIdentity = ObjectIdentity
firewallSecuritySpoof = _FirewallSecuritySpoof_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 1000)
)


class _FirewallSecuritySpoofEnable_Type(MxEnableState):
    """Custom type firewallSecuritySpoofEnable based on MxEnableState"""
    defaultValue = 1


_FirewallSecuritySpoofEnable_Type.__name__ = "MxEnableState"
_FirewallSecuritySpoofEnable_Object = MibScalar
firewallSecuritySpoofEnable = _FirewallSecuritySpoofEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 1000, 10),
    _FirewallSecuritySpoofEnable_Type()
)
firewallSecuritySpoofEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecuritySpoofEnable.setStatus("current")
_FirewallSecuritySpoofTable_Object = MibTable
firewallSecuritySpoofTable = _FirewallSecuritySpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 1000, 100)
)
if mibBuilder.loadTexts:
    firewallSecuritySpoofTable.setStatus("current")
_FirewallSecuritySpoofEntry_Object = MibTableRow
firewallSecuritySpoofEntry = _FirewallSecuritySpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 1000, 100, 5)
)
firewallSecuritySpoofEntry.setIndexNames(
    (0, "MX-FIREWALL-MIB", "firewallSecuritySpoofIndex"),
)
if mibBuilder.loadTexts:
    firewallSecuritySpoofEntry.setStatus("current")


class _FirewallSecuritySpoofIndex_Type(Unsigned32):
    """Custom type firewallSecuritySpoofIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FirewallSecuritySpoofIndex_Type.__name__ = "Unsigned32"
_FirewallSecuritySpoofIndex_Object = MibTableColumn
firewallSecuritySpoofIndex = _FirewallSecuritySpoofIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 1000, 100, 5, 10),
    _FirewallSecuritySpoofIndex_Type()
)
firewallSecuritySpoofIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSecuritySpoofIndex.setStatus("current")


class _FirewallSecuritySpoofLabel_Type(OctetString):
    """Custom type firewallSecuritySpoofLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FirewallSecuritySpoofLabel_Type.__name__ = "OctetString"
_FirewallSecuritySpoofLabel_Object = MibTableColumn
firewallSecuritySpoofLabel = _FirewallSecuritySpoofLabel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 1000, 100, 5, 20),
    _FirewallSecuritySpoofLabel_Type()
)
firewallSecuritySpoofLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSecuritySpoofLabel.setStatus("current")


class _FirewallSecuritySpoofAddress_Type(OctetString):
    """Custom type firewallSecuritySpoofAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FirewallSecuritySpoofAddress_Type.__name__ = "OctetString"
_FirewallSecuritySpoofAddress_Object = MibTableColumn
firewallSecuritySpoofAddress = _FirewallSecuritySpoofAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 1000, 100, 5, 30),
    _FirewallSecuritySpoofAddress_Type()
)
firewallSecuritySpoofAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSecuritySpoofAddress.setStatus("current")


class _FirewallSecuritySpoofRuleEnable_Type(MxEnableState):
    """Custom type firewallSecuritySpoofRuleEnable based on MxEnableState"""
    defaultValue = 0


_FirewallSecuritySpoofRuleEnable_Type.__name__ = "MxEnableState"
_FirewallSecuritySpoofRuleEnable_Object = MibTableColumn
firewallSecuritySpoofRuleEnable = _FirewallSecuritySpoofRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 100, 1000, 100, 5, 40),
    _FirewallSecuritySpoofRuleEnable_Type()
)
firewallSecuritySpoofRuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSecuritySpoofRuleEnable.setStatus("current")
_FirewallSyslog_ObjectIdentity = ObjectIdentity
firewallSyslog = _FirewallSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 200)
)


class _FirewallSyslogEnable_Type(MxEnableState):
    """Custom type firewallSyslogEnable based on MxEnableState"""
    defaultValue = 0


_FirewallSyslogEnable_Type.__name__ = "MxEnableState"
_FirewallSyslogEnable_Object = MibScalar
firewallSyslogEnable = _FirewallSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 1, 200, 10),
    _FirewallSyslogEnable_Type()
)
firewallSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallSyslogEnable.setStatus("current")
_FirewallConformance_ObjectIdentity = ObjectIdentity
firewallConformance = _FirewallConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 2)
)
_FirewallCompliances_ObjectIdentity = ObjectIdentity
firewallCompliances = _FirewallCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 2, 1)
)
_FirewallGroups_ObjectIdentity = ObjectIdentity
firewallGroups = _FirewallGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 2, 2)
)

# Managed Objects groups

firewallGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 2, 2, 1)
)
firewallGroupVer1.setObjects(
    ("MX-FIREWALL-MIB", "firewallEnable")
)
if mibBuilder.loadTexts:
    firewallGroupVer1.setStatus("current")

firewallSecurityGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 2, 2, 2)
)
firewallSecurityGroupVer1.setObjects(
      *(("MX-FIREWALL-MIB", "firewallSecurityBadTcpPacketRule"),
        ("MX-FIREWALL-MIB", "firewallSecurityTcpSynCookiesRule"),
        ("MX-FIREWALL-MIB", "firewallSecuritySourceRoutedPacketRule"),
        ("MX-FIREWALL-MIB", "firewallSecurityMulticastPacketRule"),
        ("MX-FIREWALL-MIB", "firewallSecurityIdentRule"),
        ("MX-FIREWALL-MIB", "firewallSecurityReversePathFilteringRule"),
        ("MX-FIREWALL-MIB", "firewallSecurityBlockWanEchoRequestRule"),
        ("MX-FIREWALL-MIB", "firewallSecurityBlockLanEchoRequestRule"),
        ("MX-FIREWALL-MIB", "firewallSecurityBlockWanEchoBroadcastRule"),
        ("MX-FIREWALL-MIB", "firewallSecurityBlockIcmpRedirectionInRule"),
        ("MX-FIREWALL-MIB", "firewallSecurityBlockIcmpRedirectionOutRule"))
)
if mibBuilder.loadTexts:
    firewallSecurityGroupVer1.setStatus("current")

firewallSecuritySpoofGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 2, 2, 3)
)
firewallSecuritySpoofGroupVer1.setObjects(
      *(("MX-FIREWALL-MIB", "firewallSecuritySpoofEnable"),
        ("MX-FIREWALL-MIB", "firewallSecuritySpoofLabel"),
        ("MX-FIREWALL-MIB", "firewallSecuritySpoofAddress"),
        ("MX-FIREWALL-MIB", "firewallSecuritySpoofRuleEnable"))
)
if mibBuilder.loadTexts:
    firewallSecuritySpoofGroupVer1.setStatus("current")

firewallSyslogGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 2, 2, 4)
)
firewallSyslogGroupVer1.setObjects(
    ("MX-FIREWALL-MIB", "firewallSyslogEnable")
)
if mibBuilder.loadTexts:
    firewallSyslogGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

firewallComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 450, 2, 1, 1)
)
firewallComplVer1.setObjects(
      *(("MX-FIREWALL-MIB", "firewallGroupVer1"),
        ("MX-FIREWALL-MIB", "firewallSecurityGroupVer1"),
        ("MX-FIREWALL-MIB", "firewallSecuritySpoofGroupVer1"),
        ("MX-FIREWALL-MIB", "firewallSyslogGroupVer1"))
)
if mibBuilder.loadTexts:
    firewallComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-FIREWALL-MIB",
    **{"firewallMIB": firewallMIB,
       "firewallMIBObjects": firewallMIBObjects,
       "firewallEnable": firewallEnable,
       "firewallSecurity": firewallSecurity,
       "firewallSecurityBadTcpPacketRule": firewallSecurityBadTcpPacketRule,
       "firewallSecurityTcpSynCookiesRule": firewallSecurityTcpSynCookiesRule,
       "firewallSecuritySourceRoutedPacketRule": firewallSecuritySourceRoutedPacketRule,
       "firewallSecurityMulticastPacketRule": firewallSecurityMulticastPacketRule,
       "firewallSecurityIdentRule": firewallSecurityIdentRule,
       "firewallSecurityReversePathFilteringRule": firewallSecurityReversePathFilteringRule,
       "firewallSecurityBlockWanEchoRequestRule": firewallSecurityBlockWanEchoRequestRule,
       "firewallSecurityBlockLanEchoRequestRule": firewallSecurityBlockLanEchoRequestRule,
       "firewallSecurityBlockWanEchoBroadcastRule": firewallSecurityBlockWanEchoBroadcastRule,
       "firewallSecurityBlockIcmpRedirectionInRule": firewallSecurityBlockIcmpRedirectionInRule,
       "firewallSecurityBlockIcmpRedirectionOutRule": firewallSecurityBlockIcmpRedirectionOutRule,
       "firewallSecuritySpoof": firewallSecuritySpoof,
       "firewallSecuritySpoofEnable": firewallSecuritySpoofEnable,
       "firewallSecuritySpoofTable": firewallSecuritySpoofTable,
       "firewallSecuritySpoofEntry": firewallSecuritySpoofEntry,
       "firewallSecuritySpoofIndex": firewallSecuritySpoofIndex,
       "firewallSecuritySpoofLabel": firewallSecuritySpoofLabel,
       "firewallSecuritySpoofAddress": firewallSecuritySpoofAddress,
       "firewallSecuritySpoofRuleEnable": firewallSecuritySpoofRuleEnable,
       "firewallSyslog": firewallSyslog,
       "firewallSyslogEnable": firewallSyslogEnable,
       "firewallConformance": firewallConformance,
       "firewallCompliances": firewallCompliances,
       "firewallComplVer1": firewallComplVer1,
       "firewallGroups": firewallGroups,
       "firewallGroupVer1": firewallGroupVer1,
       "firewallSecurityGroupVer1": firewallSecurityGroupVer1,
       "firewallSecuritySpoofGroupVer1": firewallSecuritySpoofGroupVer1,
       "firewallSyslogGroupVer1": firewallSyslogGroupVer1}
)
