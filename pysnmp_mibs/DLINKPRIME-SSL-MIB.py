# SNMP MIB module (DLINKPRIME-SSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-SSL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:30 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

dlinkPrimeSslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 16)
)
if mibBuilder.loadTexts:
    dlinkPrimeSslMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpSslNotifications_ObjectIdentity = ObjectIdentity
dpSslNotifications = _DpSslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 16, 0)
)
_DpSslObjects_ObjectIdentity = ObjectIdentity
dpSslObjects = _DpSslObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 16, 1)
)
_DpSslConfiguration_ObjectIdentity = ObjectIdentity
dpSslConfiguration = _DpSslConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 16, 1, 1)
)
_DpSslServiceEnabled_Type = TruthValue
_DpSslServiceEnabled_Object = MibScalar
dpSslServiceEnabled = _DpSslServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 16, 1, 1, 1),
    _DpSslServiceEnabled_Type()
)
dpSslServiceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSslServiceEnabled.setStatus("current")
_DpSslConformance_ObjectIdentity = ObjectIdentity
dpSslConformance = _DpSslConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 16, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-SSL-MIB",
    **{"dlinkPrimeSslMIB": dlinkPrimeSslMIB,
       "dpSslNotifications": dpSslNotifications,
       "dpSslObjects": dpSslObjects,
       "dpSslConfiguration": dpSslConfiguration,
       "dpSslServiceEnabled": dpSslServiceEnabled,
       "dpSslConformance": dpSslConformance}
)
