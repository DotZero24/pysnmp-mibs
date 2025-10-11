# SNMP MIB module (DLINKPRIME-WEB-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-WEB-COMMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:15 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeWebCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 28)
)
if mibBuilder.loadTexts:
    dlinkPrimeWebCommonMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpWebCommonMIBNotifications_ObjectIdentity = ObjectIdentity
dpWebCommonMIBNotifications = _DpWebCommonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 0)
)
_DpWebMIBObjects_ObjectIdentity = ObjectIdentity
dpWebMIBObjects = _DpWebMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 1)
)
_DpWebSessionObjects_ObjectIdentity = ObjectIdentity
dpWebSessionObjects = _DpWebSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 1, 1)
)


class _DpWebSessionTimeout_Type(Unsigned32):
    """Custom type dpWebSessionTimeout based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_DpWebSessionTimeout_Type.__name__ = "Unsigned32"
_DpWebSessionTimeout_Object = MibScalar
dpWebSessionTimeout = _DpWebSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 1, 1, 1),
    _DpWebSessionTimeout_Type()
)
dpWebSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpWebSessionTimeout.setStatus("current")
_DpSslServerObjects_ObjectIdentity = ObjectIdentity
dpSslServerObjects = _DpSslServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 1, 2)
)


class _DpSslServerStatus_Type(TruthValue):
    """Custom type dpSslServerStatus based on TruthValue"""
    defaultValue = 2


_DpSslServerStatus_Type.__name__ = "TruthValue"
_DpSslServerStatus_Object = MibScalar
dpSslServerStatus = _DpSslServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 1, 2, 1),
    _DpSslServerStatus_Type()
)
dpSslServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSslServerStatus.setStatus("current")
_DpWebCommonMIBConformance_ObjectIdentity = ObjectIdentity
dpWebCommonMIBConformance = _DpWebCommonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 2)
)
_DpWebCommonMIBCompliances_ObjectIdentity = ObjectIdentity
dpWebCommonMIBCompliances = _DpWebCommonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 1)
)
_DpWebCommonGroups_ObjectIdentity = ObjectIdentity
dpWebCommonGroups = _DpWebCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 2)
)

# Managed Objects groups

dpWebSessionGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 2, 1)
)
dpWebSessionGroups.setObjects(
    ("DLINKPRIME-WEB-COMMON-MIB", "dpWebSessionTimeout")
)
if mibBuilder.loadTexts:
    dpWebSessionGroups.setStatus("current")

dpSslServerGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 2, 2)
)
dpSslServerGroups.setObjects(
    ("DLINKPRIME-WEB-COMMON-MIB", "dpSslServerStatus")
)
if mibBuilder.loadTexts:
    dpSslServerGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpWebMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 1, 1)
)
dpWebMIBCompliance.setObjects(
      *(("DLINKPRIME-WEB-COMMON-MIB", "dpWebSessionGroups"),
        ("DLINKPRIME-WEB-COMMON-MIB", "dpSslServerGroups"))
)
if mibBuilder.loadTexts:
    dpWebMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-WEB-COMMON-MIB",
    **{"dlinkPrimeWebCommonMIB": dlinkPrimeWebCommonMIB,
       "dpWebCommonMIBNotifications": dpWebCommonMIBNotifications,
       "dpWebMIBObjects": dpWebMIBObjects,
       "dpWebSessionObjects": dpWebSessionObjects,
       "dpWebSessionTimeout": dpWebSessionTimeout,
       "dpSslServerObjects": dpSslServerObjects,
       "dpSslServerStatus": dpSslServerStatus,
       "dpWebCommonMIBConformance": dpWebCommonMIBConformance,
       "dpWebCommonMIBCompliances": dpWebCommonMIBCompliances,
       "dpWebMIBCompliance": dpWebMIBCompliance,
       "dpWebCommonGroups": dpWebCommonGroups,
       "dpWebSessionGroups": dpWebSessionGroups,
       "dpSslServerGroups": dpSslServerGroups}
)
