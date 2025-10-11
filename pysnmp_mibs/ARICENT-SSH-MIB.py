# SNMP MIB module (ARICENT-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-SSH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:29 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ssh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 97)
)
if mibBuilder.loadTexts:
    ssh.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SshGeneralGroup_ObjectIdentity = ObjectIdentity
sshGeneralGroup = _SshGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 97, 1)
)


class _SshVersionCompatibility_Type(TruthValue):
    """Custom type sshVersionCompatibility based on TruthValue"""
    defaultValue = 2


_SshVersionCompatibility_Type.__name__ = "TruthValue"
_SshVersionCompatibility_Object = MibScalar
sshVersionCompatibility = _SshVersionCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 2076, 97, 1, 1),
    _SshVersionCompatibility_Type()
)
sshVersionCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshVersionCompatibility.setStatus("current")


class _SshCipherList_Type(Integer32):
    """Custom type sshCipherList based on Integer32"""
    defaultValue = 181


_SshCipherList_Type.__name__ = "Integer32"
_SshCipherList_Object = MibScalar
sshCipherList = _SshCipherList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 97, 1, 2),
    _SshCipherList_Type()
)
sshCipherList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshCipherList.setStatus("current")


class _SshMacList_Type(Integer32):
    """Custom type sshMacList based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SshMacList_Type.__name__ = "Integer32"
_SshMacList_Object = MibScalar
sshMacList = _SshMacList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 97, 1, 3),
    _SshMacList_Type()
)
sshMacList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshMacList.setStatus("current")
_SshTrace_Type = Integer32
_SshTrace_Object = MibScalar
sshTrace = _SshTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 97, 1, 4),
    _SshTrace_Type()
)
sshTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshTrace.setStatus("current")


class _SshStatus_Type(TruthValue):
    """Custom type sshStatus based on TruthValue"""
    defaultValue = 1


_SshStatus_Type.__name__ = "TruthValue"
_SshStatus_Object = MibScalar
sshStatus = _SshStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 97, 1, 5),
    _SshStatus_Type()
)
sshStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshStatus.setStatus("current")


class _SshTransportMaxAllowedBytes_Type(Integer32):
    """Custom type sshTransportMaxAllowedBytes based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_SshTransportMaxAllowedBytes_Type.__name__ = "Integer32"
_SshTransportMaxAllowedBytes_Object = MibScalar
sshTransportMaxAllowedBytes = _SshTransportMaxAllowedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 97, 1, 6),
    _SshTransportMaxAllowedBytes_Type()
)
sshTransportMaxAllowedBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshTransportMaxAllowedBytes.setStatus("current")


class _SshSrvBindAddr_Type(OctetString):
    """Custom type sshSrvBindAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SshSrvBindAddr_Type.__name__ = "OctetString"
_SshSrvBindAddr_Object = MibScalar
sshSrvBindAddr = _SshSrvBindAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 97, 1, 7),
    _SshSrvBindAddr_Type()
)
sshSrvBindAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshSrvBindAddr.setStatus("current")


class _SshServerBindPortNo_Type(Unsigned32):
    """Custom type sshServerBindPortNo based on Unsigned32"""
    defaultValue = 22


_SshServerBindPortNo_Type.__name__ = "Unsigned32"
_SshServerBindPortNo_Object = MibScalar
sshServerBindPortNo = _SshServerBindPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 97, 1, 8),
    _SshServerBindPortNo_Type()
)
sshServerBindPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerBindPortNo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-SSH-MIB",
    **{"ssh": ssh,
       "sshGeneralGroup": sshGeneralGroup,
       "sshVersionCompatibility": sshVersionCompatibility,
       "sshCipherList": sshCipherList,
       "sshMacList": sshMacList,
       "sshTrace": sshTrace,
       "sshStatus": sshStatus,
       "sshTransportMaxAllowedBytes": sshTransportMaxAllowedBytes,
       "sshSrvBindAddr": sshSrvBindAddr,
       "sshServerBindPortNo": sshServerBindPortNo}
)
