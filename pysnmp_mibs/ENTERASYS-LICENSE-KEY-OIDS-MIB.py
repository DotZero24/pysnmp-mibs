# SNMP MIB module (ENTERASYS-LICENSE-KEY-OIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-LICENSE-KEY-OIDS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:13 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(etsysOidOtherLicenseKeyId,) = mibBuilder.importSymbols(
    "ENTERASYS-OIDS-MIB",
    "etsysOidOtherLicenseKeyId")

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

etsysLicenseKeyOidsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 56)
)
if mibBuilder.loadTexts:
    etsysLicenseKeyOidsMIB.setRevisions(
        ("2015-03-12 16:10",
         "2014-08-07 13:11",
         "2013-10-07 12:46",
         "2013-07-31 13:52",
         "2012-01-27 17:11",
         "2011-08-19 12:53",
         "2011-03-08 15:11",
         "2010-11-18 14:09",
         "2009-08-05 20:14",
         "2008-02-26 13:51",
         "2008-01-18 15:56",
         "2007-06-11 14:24",
         "2006-11-13 15:29",
         "2006-09-05 17:37",
         "2006-08-15 19:56",
         "2005-12-13 21:12",
         "2004-11-03 17:01",
         "2004-08-24 13:29")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysLicKeyIdNSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNSeries = _EtsysLicKeyIdNSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1)
)
_EtsysLicKeyIdNL3AdvancedFeature_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNL3AdvancedFeature = _EtsysLicKeyIdNL3AdvancedFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNL3AdvancedFeature.setStatus("current")
_EtsysLicKeyIdNGoldRedundancy_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNGoldRedundancy = _EtsysLicKeyIdNGoldRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNGoldRedundancy.setStatus("current")
_EtsysLicKeyIdNPlatinumHighCapacity_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNPlatinumHighCapacity = _EtsysLicKeyIdNPlatinumHighCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNPlatinumHighCapacity.setStatus("current")
_EtsysLicKeyIdNPlatinumPortCapacity_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNPlatinumPortCapacity = _EtsysLicKeyIdNPlatinumPortCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNPlatinumPortCapacity.setStatus("current")
_EtsysLicKeyIdNGoldPolicy_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNGoldPolicy = _EtsysLicKeyIdNGoldPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNGoldPolicy.setStatus("current")
_EtsysLicKeyIdNL3DiamondFeature_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNL3DiamondFeature = _EtsysLicKeyIdNL3DiamondFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNL3DiamondFeature.setStatus("current")
_EtsysLicKeyIdCSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdCSeries = _EtsysLicKeyIdCSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 2)
)
_EtsysLicKeyIdCAdvancedRouting_ObjectIdentity = ObjectIdentity
etsysLicKeyIdCAdvancedRouting = _EtsysLicKeyIdCAdvancedRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdCAdvancedRouting.setStatus("current")
_EtsysLicKeyIdC3IpV6Routing_ObjectIdentity = ObjectIdentity
etsysLicKeyIdC3IpV6Routing = _EtsysLicKeyIdC3IpV6Routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdC3IpV6Routing.setStatus("current")
_EtsysLicKeyIdBSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdBSeries = _EtsysLicKeyIdBSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 3)
)
_EtsysLicKeyIdBPolicy_ObjectIdentity = ObjectIdentity
etsysLicKeyIdBPolicy = _EtsysLicKeyIdBPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdBPolicy.setStatus("current")
_EtsysLicKeyIdBRouting_ObjectIdentity = ObjectIdentity
etsysLicKeyIdBRouting = _EtsysLicKeyIdBRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdBRouting.setStatus("current")
_EtsysLicKeyIdDSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdDSeries = _EtsysLicKeyIdDSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 4)
)
_EtsysLicKeyIdDPolicy_ObjectIdentity = ObjectIdentity
etsysLicKeyIdDPolicy = _EtsysLicKeyIdDPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdDPolicy.setStatus("current")
_EtsysLicKeyIdGSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdGSeries = _EtsysLicKeyIdGSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 5)
)
_EtsysLicKeyIdGRouting_ObjectIdentity = ObjectIdentity
etsysLicKeyIdGRouting = _EtsysLicKeyIdGRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdGRouting.setStatus("current")
_EtsysLicKeyIdSSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSSeries = _EtsysLicKeyIdSSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6)
)
_EtsysLicKeyIdSxEOSxPPC_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxPPC = _EtsysLicKeyIdSxEOSxPPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxPPC.setStatus("current")
_EtsysLicKeyIdSxEOSxL3xACCESS_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxL3xACCESS = _EtsysLicKeyIdSxEOSxL3xACCESS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxL3xACCESS.setStatus("current")
_EtsysLicKeyIdSxEOSxL3xCORE_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxL3xCORE = _EtsysLicKeyIdSxEOSxL3xCORE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxL3xCORE.setStatus("current")
_EtsysLicKeyIdSSAxEOSx2XUSER_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSSAxEOSx2XUSER = _EtsysLicKeyIdSSAxEOSx2XUSER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 4)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSSAxEOSx2XUSER.setStatus("current")
_EtsysLicKeyIdSxEOSxVSB_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxVSB = _EtsysLicKeyIdSxEOSxVSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 5)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxVSB.setStatus("current")
_EtsysLicKeyIdSSAxEOSxVSB_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSSAxEOSxVSB = _EtsysLicKeyIdSSAxEOSxVSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 6)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSSAxEOSxVSB.setStatus("current")
_EtsysLicKeyIdS1xEOSxVSB_ObjectIdentity = ObjectIdentity
etsysLicKeyIdS1xEOSxVSB = _EtsysLicKeyIdS1xEOSxVSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 7)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdS1xEOSxVSB.setStatus("current")
_EtsysLicKeyIdS1xEOSxUSER_ObjectIdentity = ObjectIdentity
etsysLicKeyIdS1xEOSxUSER = _EtsysLicKeyIdS1xEOSxUSER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 8)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdS1xEOSxUSER.setStatus("current")
_EtsysLicKeyIdSxEOSxFLOW_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxFLOW = _EtsysLicKeyIdSxEOSxFLOW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 9)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxFLOW.setStatus("current")
_EtsysLicKeyIdSxEOSxMACSEC_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxMACSEC = _EtsysLicKeyIdSxEOSxMACSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 10)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxMACSEC.setStatus("current")
_EtsysLicKeyIdSxEOSxKMACSEC_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxKMACSEC = _EtsysLicKeyIdSxEOSxKMACSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 11)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxKMACSEC.setStatus("current")
_EtsysLicKeyIdKSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdKSeries = _EtsysLicKeyIdKSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 7)
)
_EtsysLicKeyIdKxEOSxL3_ObjectIdentity = ObjectIdentity
etsysLicKeyIdKxEOSxL3 = _EtsysLicKeyIdKxEOSxL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdKxEOSxL3.setStatus("current")
_EtsysLicKeyIdKxEOSxPPC_ObjectIdentity = ObjectIdentity
etsysLicKeyIdKxEOSxPPC = _EtsysLicKeyIdKxEOSxPPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdKxEOSxPPC.setStatus("current")
_EtsysLicKeyIdKxEOSxVSB_ObjectIdentity = ObjectIdentity
etsysLicKeyIdKxEOSxVSB = _EtsysLicKeyIdKxEOSxVSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 7, 3)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdKxEOSxVSB.setStatus("current")
_EtsysLicKeyId7100Series_ObjectIdentity = ObjectIdentity
etsysLicKeyId7100Series = _EtsysLicKeyId7100Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 8)
)
_EtsysLicKeyId71AxEOSxADVL3_ObjectIdentity = ObjectIdentity
etsysLicKeyId71AxEOSxADVL3 = _EtsysLicKeyId71AxEOSxADVL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 8, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyId71AxEOSxADVL3.setStatus("current")
_EtsysLicKeyId71AxEOSxGxADVL3_ObjectIdentity = ObjectIdentity
etsysLicKeyId71AxEOSxGxADVL3 = _EtsysLicKeyId71AxEOSxGxADVL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 8, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyId71AxEOSxGxADVL3.setStatus("current")
_EtsysLicKeyId71AxEOSxGMACSEC_ObjectIdentity = ObjectIdentity
etsysLicKeyId71AxEOSxGMACSEC = _EtsysLicKeyId71AxEOSxGMACSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 8, 3)
)
if mibBuilder.loadTexts:
    etsysLicKeyId71AxEOSxGMACSEC.setStatus("current")
_EtsysLicKeyId71AxEOSxKMACSEC_ObjectIdentity = ObjectIdentity
etsysLicKeyId71AxEOSxKMACSEC = _EtsysLicKeyId71AxEOSxKMACSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 8, 4)
)
if mibBuilder.loadTexts:
    etsysLicKeyId71AxEOSxKMACSEC.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-LICENSE-KEY-OIDS-MIB",
    **{"etsysLicenseKeyOidsMIB": etsysLicenseKeyOidsMIB,
       "etsysLicKeyIdNSeries": etsysLicKeyIdNSeries,
       "etsysLicKeyIdNL3AdvancedFeature": etsysLicKeyIdNL3AdvancedFeature,
       "etsysLicKeyIdNGoldRedundancy": etsysLicKeyIdNGoldRedundancy,
       "etsysLicKeyIdNPlatinumHighCapacity": etsysLicKeyIdNPlatinumHighCapacity,
       "etsysLicKeyIdNPlatinumPortCapacity": etsysLicKeyIdNPlatinumPortCapacity,
       "etsysLicKeyIdNGoldPolicy": etsysLicKeyIdNGoldPolicy,
       "etsysLicKeyIdNL3DiamondFeature": etsysLicKeyIdNL3DiamondFeature,
       "etsysLicKeyIdCSeries": etsysLicKeyIdCSeries,
       "etsysLicKeyIdCAdvancedRouting": etsysLicKeyIdCAdvancedRouting,
       "etsysLicKeyIdC3IpV6Routing": etsysLicKeyIdC3IpV6Routing,
       "etsysLicKeyIdBSeries": etsysLicKeyIdBSeries,
       "etsysLicKeyIdBPolicy": etsysLicKeyIdBPolicy,
       "etsysLicKeyIdBRouting": etsysLicKeyIdBRouting,
       "etsysLicKeyIdDSeries": etsysLicKeyIdDSeries,
       "etsysLicKeyIdDPolicy": etsysLicKeyIdDPolicy,
       "etsysLicKeyIdGSeries": etsysLicKeyIdGSeries,
       "etsysLicKeyIdGRouting": etsysLicKeyIdGRouting,
       "etsysLicKeyIdSSeries": etsysLicKeyIdSSeries,
       "etsysLicKeyIdSxEOSxPPC": etsysLicKeyIdSxEOSxPPC,
       "etsysLicKeyIdSxEOSxL3xACCESS": etsysLicKeyIdSxEOSxL3xACCESS,
       "etsysLicKeyIdSxEOSxL3xCORE": etsysLicKeyIdSxEOSxL3xCORE,
       "etsysLicKeyIdSSAxEOSx2XUSER": etsysLicKeyIdSSAxEOSx2XUSER,
       "etsysLicKeyIdSxEOSxVSB": etsysLicKeyIdSxEOSxVSB,
       "etsysLicKeyIdSSAxEOSxVSB": etsysLicKeyIdSSAxEOSxVSB,
       "etsysLicKeyIdS1xEOSxVSB": etsysLicKeyIdS1xEOSxVSB,
       "etsysLicKeyIdS1xEOSxUSER": etsysLicKeyIdS1xEOSxUSER,
       "etsysLicKeyIdSxEOSxFLOW": etsysLicKeyIdSxEOSxFLOW,
       "etsysLicKeyIdSxEOSxMACSEC": etsysLicKeyIdSxEOSxMACSEC,
       "etsysLicKeyIdSxEOSxKMACSEC": etsysLicKeyIdSxEOSxKMACSEC,
       "etsysLicKeyIdKSeries": etsysLicKeyIdKSeries,
       "etsysLicKeyIdKxEOSxL3": etsysLicKeyIdKxEOSxL3,
       "etsysLicKeyIdKxEOSxPPC": etsysLicKeyIdKxEOSxPPC,
       "etsysLicKeyIdKxEOSxVSB": etsysLicKeyIdKxEOSxVSB,
       "etsysLicKeyId7100Series": etsysLicKeyId7100Series,
       "etsysLicKeyId71AxEOSxADVL3": etsysLicKeyId71AxEOSxADVL3,
       "etsysLicKeyId71AxEOSxGxADVL3": etsysLicKeyId71AxEOSxGxADVL3,
       "etsysLicKeyId71AxEOSxGMACSEC": etsysLicKeyId71AxEOSxGMACSEC,
       "etsysLicKeyId71AxEOSxKMACSEC": etsysLicKeyId71AxEOSxKMACSEC}
)
