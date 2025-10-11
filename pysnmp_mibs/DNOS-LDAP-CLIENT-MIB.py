# SNMP MIB module (DNOS-LDAP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DNOS-LDAP-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:09:48 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

agentLdapClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73)
)
if mibBuilder.loadTexts:
    agentLdapClientMIB.setRevisions(
        ("2017-12-15 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentLdapClientObjects_ObjectIdentity = ObjectIdentity
agentLdapClientObjects = _AgentLdapClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1)
)
_AgentLdapGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentLdapGlobalConfigGroup = _AgentLdapGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 1)
)


class _AgentLdapBindFirst_Type(TruthValue):
    """Custom type agentLdapBindFirst based on TruthValue"""
    defaultValue = 2


_AgentLdapBindFirst_Type.__name__ = "TruthValue"
_AgentLdapBindFirst_Object = MibScalar
agentLdapBindFirst = _AgentLdapBindFirst_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 1, 1),
    _AgentLdapBindFirst_Type()
)
agentLdapBindFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapBindFirst.setStatus("current")


class _AgentLdapAppendWithBaseDN_Type(SnmpAdminString):
    """Custom type agentLdapAppendWithBaseDN based on SnmpAdminString"""
    defaultValue = OctetString("cn=$userid")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentLdapAppendWithBaseDN_Type.__name__ = "SnmpAdminString"
_AgentLdapAppendWithBaseDN_Object = MibScalar
agentLdapAppendWithBaseDN = _AgentLdapAppendWithBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 1, 2),
    _AgentLdapAppendWithBaseDN_Type()
)
agentLdapAppendWithBaseDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapAppendWithBaseDN.setStatus("current")
_AgentLdapServerTable_Object = MibTable
agentLdapServerTable = _AgentLdapServerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2)
)
if mibBuilder.loadTexts:
    agentLdapServerTable.setStatus("current")
_AgentLdapServerEntry_Object = MibTableRow
agentLdapServerEntry = _AgentLdapServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2, 1)
)
agentLdapServerEntry.setIndexNames(
    (0, "DNOS-LDAP-CLIENT-MIB", "agentLdapServerIpAddrType"),
    (0, "DNOS-LDAP-CLIENT-MIB", "agentLdapServerIpAddress"),
)
if mibBuilder.loadTexts:
    agentLdapServerEntry.setStatus("current")
_AgentLdapServerIpAddrType_Type = InetAddressType
_AgentLdapServerIpAddrType_Object = MibTableColumn
agentLdapServerIpAddrType = _AgentLdapServerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2, 1, 1),
    _AgentLdapServerIpAddrType_Type()
)
agentLdapServerIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLdapServerIpAddrType.setStatus("current")
_AgentLdapServerIpAddress_Type = InetAddress
_AgentLdapServerIpAddress_Object = MibTableColumn
agentLdapServerIpAddress = _AgentLdapServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2, 1, 2),
    _AgentLdapServerIpAddress_Type()
)
agentLdapServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLdapServerIpAddress.setStatus("current")
_AgentLdapServerStatus_Type = RowStatus
_AgentLdapServerStatus_Object = MibTableColumn
agentLdapServerStatus = _AgentLdapServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2, 1, 3),
    _AgentLdapServerStatus_Type()
)
agentLdapServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLdapServerStatus.setStatus("current")


class _AgentLdapServerPort_Type(Unsigned32):
    """Custom type agentLdapServerPort based on Unsigned32"""
    defaultValue = 389

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentLdapServerPort_Type.__name__ = "Unsigned32"
_AgentLdapServerPort_Object = MibTableColumn
agentLdapServerPort = _AgentLdapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2, 1, 4),
    _AgentLdapServerPort_Type()
)
agentLdapServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapServerPort.setStatus("current")


class _AgentLdapServerTimeOut_Type(Unsigned32):
    """Custom type agentLdapServerTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AgentLdapServerTimeOut_Type.__name__ = "Unsigned32"
_AgentLdapServerTimeOut_Object = MibTableColumn
agentLdapServerTimeOut = _AgentLdapServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2, 1, 5),
    _AgentLdapServerTimeOut_Type()
)
agentLdapServerTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapServerTimeOut.setStatus("current")


class _AgentLdapServerSSLMode_Type(TruthValue):
    """Custom type agentLdapServerSSLMode based on TruthValue"""
    defaultValue = 2


_AgentLdapServerSSLMode_Type.__name__ = "TruthValue"
_AgentLdapServerSSLMode_Object = MibTableColumn
agentLdapServerSSLMode = _AgentLdapServerSSLMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2, 1, 6),
    _AgentLdapServerSSLMode_Type()
)
agentLdapServerSSLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapServerSSLMode.setStatus("current")


class _AgentLdapServerRootDN_Type(SnmpAdminString):
    """Custom type agentLdapServerRootDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentLdapServerRootDN_Type.__name__ = "SnmpAdminString"
_AgentLdapServerRootDN_Object = MibTableColumn
agentLdapServerRootDN = _AgentLdapServerRootDN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2, 1, 7),
    _AgentLdapServerRootDN_Type()
)
agentLdapServerRootDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapServerRootDN.setStatus("current")


class _AgentLdapServerRootDNPassword_Type(SnmpAdminString):
    """Custom type agentLdapServerRootDNPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentLdapServerRootDNPassword_Type.__name__ = "SnmpAdminString"
_AgentLdapServerRootDNPassword_Object = MibTableColumn
agentLdapServerRootDNPassword = _AgentLdapServerRootDNPassword_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 2, 1, 8),
    _AgentLdapServerRootDNPassword_Type()
)
agentLdapServerRootDNPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapServerRootDNPassword.setStatus("current")
_AgentLdapSearchMapTable_Object = MibTable
agentLdapSearchMapTable = _AgentLdapSearchMapTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 3)
)
if mibBuilder.loadTexts:
    agentLdapSearchMapTable.setStatus("current")
_AgentLdapSearchMapEntry_Object = MibTableRow
agentLdapSearchMapEntry = _AgentLdapSearchMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 3, 1)
)
agentLdapSearchMapEntry.setIndexNames(
    (0, "DNOS-LDAP-CLIENT-MIB", "agentLdapSearchMapName"),
    (0, "DNOS-LDAP-CLIENT-MIB", "agentLdapSearchMapMode"),
)
if mibBuilder.loadTexts:
    agentLdapSearchMapEntry.setStatus("current")


class _AgentLdapSearchMapName_Type(SnmpAdminString):
    """Custom type agentLdapSearchMapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentLdapSearchMapName_Type.__name__ = "SnmpAdminString"
_AgentLdapSearchMapName_Object = MibTableColumn
agentLdapSearchMapName = _AgentLdapSearchMapName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 3, 1, 1),
    _AgentLdapSearchMapName_Type()
)
agentLdapSearchMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLdapSearchMapName.setStatus("current")


class _AgentLdapSearchMapMode_Type(Integer32):
    """Custom type agentLdapSearchMapMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("userprofile", 1)
    )


_AgentLdapSearchMapMode_Type.__name__ = "Integer32"
_AgentLdapSearchMapMode_Object = MibTableColumn
agentLdapSearchMapMode = _AgentLdapSearchMapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 3, 1, 2),
    _AgentLdapSearchMapMode_Type()
)
agentLdapSearchMapMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLdapSearchMapMode.setStatus("current")
_AgentLdapSearchMapStatus_Type = RowStatus
_AgentLdapSearchMapStatus_Object = MibTableColumn
agentLdapSearchMapStatus = _AgentLdapSearchMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 3, 1, 3),
    _AgentLdapSearchMapStatus_Type()
)
agentLdapSearchMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLdapSearchMapStatus.setStatus("current")


class _AgentLdapSearchMapAttribute_Type(SnmpAdminString):
    """Custom type agentLdapSearchMapAttribute based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentLdapSearchMapAttribute_Type.__name__ = "SnmpAdminString"
_AgentLdapSearchMapAttribute_Object = MibTableColumn
agentLdapSearchMapAttribute = _AgentLdapSearchMapAttribute_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 3, 1, 4),
    _AgentLdapSearchMapAttribute_Type()
)
agentLdapSearchMapAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapSearchMapAttribute.setStatus("current")


class _AgentLdapSearchMapFilter_Type(SnmpAdminString):
    """Custom type agentLdapSearchMapFilter based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentLdapSearchMapFilter_Type.__name__ = "SnmpAdminString"
_AgentLdapSearchMapFilter_Object = MibTableColumn
agentLdapSearchMapFilter = _AgentLdapSearchMapFilter_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 3, 1, 5),
    _AgentLdapSearchMapFilter_Type()
)
agentLdapSearchMapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapSearchMapFilter.setStatus("current")


class _AgentLdapSearchMapBaseDN_Type(SnmpAdminString):
    """Custom type agentLdapSearchMapBaseDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentLdapSearchMapBaseDN_Type.__name__ = "SnmpAdminString"
_AgentLdapSearchMapBaseDN_Object = MibTableColumn
agentLdapSearchMapBaseDN = _AgentLdapSearchMapBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 73, 1, 3, 1, 6),
    _AgentLdapSearchMapBaseDN_Type()
)
agentLdapSearchMapBaseDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLdapSearchMapBaseDN.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-LDAP-CLIENT-MIB",
    **{"agentLdapClientMIB": agentLdapClientMIB,
       "agentLdapClientObjects": agentLdapClientObjects,
       "agentLdapGlobalConfigGroup": agentLdapGlobalConfigGroup,
       "agentLdapBindFirst": agentLdapBindFirst,
       "agentLdapAppendWithBaseDN": agentLdapAppendWithBaseDN,
       "agentLdapServerTable": agentLdapServerTable,
       "agentLdapServerEntry": agentLdapServerEntry,
       "agentLdapServerIpAddrType": agentLdapServerIpAddrType,
       "agentLdapServerIpAddress": agentLdapServerIpAddress,
       "agentLdapServerStatus": agentLdapServerStatus,
       "agentLdapServerPort": agentLdapServerPort,
       "agentLdapServerTimeOut": agentLdapServerTimeOut,
       "agentLdapServerSSLMode": agentLdapServerSSLMode,
       "agentLdapServerRootDN": agentLdapServerRootDN,
       "agentLdapServerRootDNPassword": agentLdapServerRootDNPassword,
       "agentLdapSearchMapTable": agentLdapSearchMapTable,
       "agentLdapSearchMapEntry": agentLdapSearchMapEntry,
       "agentLdapSearchMapName": agentLdapSearchMapName,
       "agentLdapSearchMapMode": agentLdapSearchMapMode,
       "agentLdapSearchMapStatus": agentLdapSearchMapStatus,
       "agentLdapSearchMapAttribute": agentLdapSearchMapAttribute,
       "agentLdapSearchMapFilter": agentLdapSearchMapFilter,
       "agentLdapSearchMapBaseDN": agentLdapSearchMapBaseDN}
)
