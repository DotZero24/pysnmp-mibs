# SNMP MIB module (HM2-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-TC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:56:22 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hm2TcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 1)
)
if mibBuilder.loadTexts:
    hm2TcMib.setRevisions(
        ("2011-03-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class HmEnabledStatus(TextualConvention, Integer32):
    status = "current"
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



class HmActionValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("action", 2))
    )



class HmTimeHHMM24(TextualConvention, OctetString):
    status = "current"
    displayHint = "5a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class HmTimeSeconds1970(TextualConvention, Unsigned32):
    status = "current"


class HmLargeDisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class HmExtraLargeDisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1400a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )



class HmAccessLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readWrite", 1),
          ("readOnly", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hirschmann_ObjectIdentity = ObjectIdentity
hirschmann = _Hirschmann_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248)
)
_Hm2ConfigurationMibs_ObjectIdentity = ObjectIdentity
hm2ConfigurationMibs = _Hm2ConfigurationMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11)
)
_Hm2PlatformMibs_ObjectIdentity = ObjectIdentity
hm2PlatformMibs = _Hm2PlatformMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-TC-MIB",
    **{"HmEnabledStatus": HmEnabledStatus,
       "HmActionValue": HmActionValue,
       "HmTimeHHMM24": HmTimeHHMM24,
       "HmTimeSeconds1970": HmTimeSeconds1970,
       "HmLargeDisplayString": HmLargeDisplayString,
       "HmExtraLargeDisplayString": HmExtraLargeDisplayString,
       "HmAccessLevel": HmAccessLevel,
       "hirschmann": hirschmann,
       "hm2ConfigurationMibs": hm2ConfigurationMibs,
       "hm2TcMib": hm2TcMib,
       "hm2PlatformMibs": hm2PlatformMibs}
)
