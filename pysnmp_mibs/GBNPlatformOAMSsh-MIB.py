# SNMP MIB module (GBNPlatformOAMSsh-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/gcom/GBNPlatformOAMSsh-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:59 2025
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

(gbnPlatformOAM,) = mibBuilder.importSymbols(
    "GBNPlatformOAM-MIB",
    "gbnPlatformOAM")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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

gbnPlatformOAMSsh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    gbnPlatformOAMSsh.setRevisions(
        ("1905-05-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SshVersion_Type(Integer32):
    """Custom type sshVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_SshVersion_Type.__name__ = "Integer32"
_SshVersion_Object = MibScalar
sshVersion = _SshVersion_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11, 1),
    _SshVersion_Type()
)
sshVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshVersion.setStatus("current")


class _SshState_Type(Integer32):
    """Custom type sshState based on Integer32"""
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


_SshState_Type.__name__ = "Integer32"
_SshState_Object = MibScalar
sshState = _SshState_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11, 2),
    _SshState_Type()
)
sshState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshState.setStatus("current")


class _SshKeyAvailable_Type(Integer32):
    """Custom type sshKeyAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_SshKeyAvailable_Type.__name__ = "Integer32"
_SshKeyAvailable_Object = MibScalar
sshKeyAvailable = _SshKeyAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11, 3),
    _SshKeyAvailable_Type()
)
sshKeyAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshKeyAvailable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNPlatformOAMSsh-MIB",
    **{"gbnPlatformOAMSsh": gbnPlatformOAMSsh,
       "sshVersion": sshVersion,
       "sshState": sshState,
       "sshKeyAvailable": sshKeyAvailable}
)
