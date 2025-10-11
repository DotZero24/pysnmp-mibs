# SNMP MIB module (DNOS-SMTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DNOS-SMTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:08:36 2025
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

(agentInventoryComponentIndex,) = mibBuilder.importSymbols(
    "DNOS-INVENTORY-MIB",
    "agentInventoryComponentIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathSmtp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169)
)
if mibBuilder.loadTexts:
    fastPathSmtp.setRevisions(
        ("2022-02-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentSmtpConfigGroup_ObjectIdentity = ObjectIdentity
agentSmtpConfigGroup = _AgentSmtpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1)
)
_AgentSmtpServerConfigGroup_ObjectIdentity = ObjectIdentity
agentSmtpServerConfigGroup = _AgentSmtpServerConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1)
)
_AgentSmtpServerTable_Object = MibTable
agentSmtpServerTable = _AgentSmtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1, 1)
)
if mibBuilder.loadTexts:
    agentSmtpServerTable.setStatus("current")
_AgentSmtpServerEntry_Object = MibTableRow
agentSmtpServerEntry = _AgentSmtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1, 1, 1)
)
agentSmtpServerEntry.setIndexNames(
    (0, "DNOS-SMTP-MIB", "agentSmtpServerAddrType"),
    (0, "DNOS-SMTP-MIB", "agentSmtpServerAddr"),
)
if mibBuilder.loadTexts:
    agentSmtpServerEntry.setStatus("current")
_AgentSmtpServerAddrType_Type = InetAddressType
_AgentSmtpServerAddrType_Object = MibTableColumn
agentSmtpServerAddrType = _AgentSmtpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1, 1, 1, 1),
    _AgentSmtpServerAddrType_Type()
)
agentSmtpServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSmtpServerAddrType.setStatus("current")
_AgentSmtpServerAddr_Type = InetAddress
_AgentSmtpServerAddr_Object = MibTableColumn
agentSmtpServerAddr = _AgentSmtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1, 1, 1, 2),
    _AgentSmtpServerAddr_Type()
)
agentSmtpServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSmtpServerAddr.setStatus("current")
_AgentSmtpServerPort_Type = InetPortNumber
_AgentSmtpServerPort_Object = MibTableColumn
agentSmtpServerPort = _AgentSmtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1, 1, 1, 3),
    _AgentSmtpServerPort_Type()
)
agentSmtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSmtpServerPort.setStatus("current")


class _AgentSmtpServerSecurity_Type(Integer32):
    """Custom type agentSmtpServerSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tlsv1", 2))
    )


_AgentSmtpServerSecurity_Type.__name__ = "Integer32"
_AgentSmtpServerSecurity_Object = MibTableColumn
agentSmtpServerSecurity = _AgentSmtpServerSecurity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1, 1, 1, 4),
    _AgentSmtpServerSecurity_Type()
)
agentSmtpServerSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSmtpServerSecurity.setStatus("current")
_AgentSmtpServerloginID_Type = DisplayString
_AgentSmtpServerloginID_Object = MibTableColumn
agentSmtpServerloginID = _AgentSmtpServerloginID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1, 1, 1, 5),
    _AgentSmtpServerloginID_Type()
)
agentSmtpServerloginID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSmtpServerloginID.setStatus("current")
_AgentSmtpServerPassword_Type = DisplayString
_AgentSmtpServerPassword_Object = MibTableColumn
agentSmtpServerPassword = _AgentSmtpServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1, 1, 1, 6),
    _AgentSmtpServerPassword_Type()
)
agentSmtpServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSmtpServerPassword.setStatus("current")
_AgentSmtpServerEntryStatus_Type = RowStatus
_AgentSmtpServerEntryStatus_Object = MibTableColumn
agentSmtpServerEntryStatus = _AgentSmtpServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 169, 1, 1, 1, 1, 7),
    _AgentSmtpServerEntryStatus_Type()
)
agentSmtpServerEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSmtpServerEntryStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-SMTP-MIB",
    **{"fastPathSmtp": fastPathSmtp,
       "agentSmtpConfigGroup": agentSmtpConfigGroup,
       "agentSmtpServerConfigGroup": agentSmtpServerConfigGroup,
       "agentSmtpServerTable": agentSmtpServerTable,
       "agentSmtpServerEntry": agentSmtpServerEntry,
       "agentSmtpServerAddrType": agentSmtpServerAddrType,
       "agentSmtpServerAddr": agentSmtpServerAddr,
       "agentSmtpServerPort": agentSmtpServerPort,
       "agentSmtpServerSecurity": agentSmtpServerSecurity,
       "agentSmtpServerloginID": agentSmtpServerloginID,
       "agentSmtpServerPassword": agentSmtpServerPassword,
       "agentSmtpServerEntryStatus": agentSmtpServerEntryStatus}
)
