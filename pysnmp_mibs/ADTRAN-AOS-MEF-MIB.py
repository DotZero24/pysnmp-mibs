# SNMP MIB module (ADTRAN-AOS-MEF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-AOS-MEF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:08 2025
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

(adGenAOS,
 adGenAOSMef) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOS",
    "adGenAOSMef")

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

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

adGenAOSMefMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9)
)
if mibBuilder.loadTexts:
    adGenAOSMefMib.setRevisions(
        ("2014-09-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAosMefPerUniPerfHistoryMib_ObjectIdentity = ObjectIdentity
adGenAosMefPerUniPerfHistoryMib = _AdGenAosMefPerUniPerfHistoryMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1)
)
_AdGenAosMefPerCosPerUniPerfHistoryMib_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerUniPerfHistoryMib = _AdGenAosMefPerCosPerUniPerfHistoryMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2)
)
_AdGenAosMefPerEvcPerfHistoryMib_ObjectIdentity = ObjectIdentity
adGenAosMefPerEvcPerfHistoryMib = _AdGenAosMefPerEvcPerfHistoryMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3)
)
_AdGenAosMefPerCosPerEvcPerfHistoryMib_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerEvcPerfHistoryMib = _AdGenAosMefPerCosPerEvcPerfHistoryMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4)
)
_AdGenAosMefPerUniTotalCountMib_ObjectIdentity = ObjectIdentity
adGenAosMefPerUniTotalCountMib = _AdGenAosMefPerUniTotalCountMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 5)
)
_AdGenAosMefPerCosPerUniTotalCountMib_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerUniTotalCountMib = _AdGenAosMefPerCosPerUniTotalCountMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 6)
)
_AdGenAosMefPerEvcTotalCountMib_ObjectIdentity = ObjectIdentity
adGenAosMefPerEvcTotalCountMib = _AdGenAosMefPerEvcTotalCountMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 7)
)
_AdGenAosMefPerCosPerEvcTotalCountMib_ObjectIdentity = ObjectIdentity
adGenAosMefPerCosPerEvcTotalCountMib = _AdGenAosMefPerCosPerEvcTotalCountMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 8)
)
_AdGenAosY1731Mib_ObjectIdentity = ObjectIdentity
adGenAosY1731Mib = _AdGenAosY1731Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-MEF-MIB",
    **{"adGenAOSMefMib": adGenAOSMefMib,
       "adGenAosMefPerUniPerfHistoryMib": adGenAosMefPerUniPerfHistoryMib,
       "adGenAosMefPerCosPerUniPerfHistoryMib": adGenAosMefPerCosPerUniPerfHistoryMib,
       "adGenAosMefPerEvcPerfHistoryMib": adGenAosMefPerEvcPerfHistoryMib,
       "adGenAosMefPerCosPerEvcPerfHistoryMib": adGenAosMefPerCosPerEvcPerfHistoryMib,
       "adGenAosMefPerUniTotalCountMib": adGenAosMefPerUniTotalCountMib,
       "adGenAosMefPerCosPerUniTotalCountMib": adGenAosMefPerCosPerUniTotalCountMib,
       "adGenAosMefPerEvcTotalCountMib": adGenAosMefPerEvcTotalCountMib,
       "adGenAosMefPerCosPerEvcTotalCountMib": adGenAosMefPerCosPerEvcTotalCountMib,
       "adGenAosY1731Mib": adGenAosY1731Mib}
)
