# SNMP MIB module (ELTEX-MES-ISS-SNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-SNTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:57 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(fsSntpUnicastServerEntry,) = mibBuilder.importSymbols(
    "FSSNTP-MIB",
    "fsSntpUnicastServerEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eltMesIssSntpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 16)
)
if mibBuilder.loadTexts:
    eltMesIssSntpMIB.setRevisions(
        ("2019-08-15 00:00",
         "2020-12-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NtpStratumType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssSntpObjects_ObjectIdentity = ObjectIdentity
eltMesIssSntpObjects = _EltMesIssSntpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1)
)
_EltMesIssSntpUnicast_ObjectIdentity = ObjectIdentity
eltMesIssSntpUnicast = _EltMesIssSntpUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1)
)
_EltMesIssSntpUnicastServerTable_Object = MibTable
eltMesIssSntpUnicastServerTable = _EltMesIssSntpUnicastServerTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssSntpUnicastServerTable.setStatus("current")
_EltMesIssSntpUnicastServerEntry_Object = MibTableRow
eltMesIssSntpUnicastServerEntry = _EltMesIssSntpUnicastServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssSntpUnicastServerEntry.setStatus("current")
_EltMesIssSntpUnicastServerStratum_Type = NtpStratumType
_EltMesIssSntpUnicastServerStratum_Object = MibTableColumn
eltMesIssSntpUnicastServerStratum = _EltMesIssSntpUnicastServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1, 1, 1, 1),
    _EltMesIssSntpUnicastServerStratum_Type()
)
eltMesIssSntpUnicastServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSntpUnicastServerStratum.setStatus("current")


class _EltMesIssSntpUnicastServerPriority_Type(Integer32):
    """Custom type eltMesIssSntpUnicastServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_EltMesIssSntpUnicastServerPriority_Type.__name__ = "Integer32"
_EltMesIssSntpUnicastServerPriority_Object = MibTableColumn
eltMesIssSntpUnicastServerPriority = _EltMesIssSntpUnicastServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1, 1, 1, 2),
    _EltMesIssSntpUnicastServerPriority_Type()
)
eltMesIssSntpUnicastServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSntpUnicastServerPriority.setStatus("current")
fsSntpUnicastServerEntry.registerAugmentions(
    ("ELTEX-MES-ISS-SNTP-MIB",
     "eltMesIssSntpUnicastServerEntry")
)
eltMesIssSntpUnicastServerEntry.setIndexNames(*fsSntpUnicastServerEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-SNTP-MIB",
    **{"NtpStratumType": NtpStratumType,
       "eltMesIssSntpMIB": eltMesIssSntpMIB,
       "eltMesIssSntpObjects": eltMesIssSntpObjects,
       "eltMesIssSntpUnicast": eltMesIssSntpUnicast,
       "eltMesIssSntpUnicastServerTable": eltMesIssSntpUnicastServerTable,
       "eltMesIssSntpUnicastServerEntry": eltMesIssSntpUnicastServerEntry,
       "eltMesIssSntpUnicastServerStratum": eltMesIssSntpUnicastServerStratum,
       "eltMesIssSntpUnicastServerPriority": eltMesIssSntpUnicastServerPriority}
)
