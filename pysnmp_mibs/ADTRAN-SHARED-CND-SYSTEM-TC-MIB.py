# SNMP MIB module (ADTRAN-SHARED-CND-SYSTEM-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-SHARED-CND-SYSTEM-TC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:46 2025
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

(adGenSystemTCID,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenSystemTCID")

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

adGenCndSystemTCIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 14, 1)
)
if mibBuilder.loadTexts:
    adGenCndSystemTCIdentity.setRevisions(
        ("2019-06-20 00:00",
         "2014-08-26 00:00",
         "2014-07-02 00:00",
         "2012-03-23 00:00",
         "2012-03-21 00:00",
         "2012-01-05 00:00",
         "2009-03-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class GenSystemInterfaceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ds1", 2),
          ("dsx1", 3),
          ("e1", 4),
          ("dsxE1", 5),
          ("gigabitEthernet", 6),
          ("ds3", 7),
          ("portChannel", 8),
          ("tenGigabitEthernet", 9),
          ("erps", 10),
          ("shdsl", 11),
          ("adsl", 12),
          ("vdsl", 13),
          ("efmGroup", 14),
          ("efmLink", 15),
          ("efmPort", 16),
          ("lagGroup", 17),
          ("pppGroup", 18),
          ("imaGroup", 19),
          ("imaLink", 20),
          ("atm", 21),
          ("fxs", 22),
          ("hdsl2", 23),
          ("hdsl4", 24),
          ("adsl2", 25),
          ("vdsl2", 26),
          ("ethernet", 27),
          ("fast", 28),
          ("interleave", 29),
          ("hdsl", 30),
          ("gpon", 31),
          ("ipHost", 32),
          ("frpvc", 33),
          ("sonet", 34),
          ("otn", 35),
          ("wan", 36),
          ("defaultEthernet", 37),
          ("genericBridge", 38),
          ("fibreChannel", 39),
          ("otnTenGigabitEthernet", 40),
          ("hundredGigabitEthernet", 41),
          ("otnHundredGigabitEthernet", 42),
          ("xgigabitEthernet", 43))
    )



class AdGenTrapVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpV1", 1),
          ("snmpV2", 2))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    **{"GenSystemInterfaceType": GenSystemInterfaceType,
       "AdGenTrapVersion": AdGenTrapVersion,
       "adGenCndSystemTCIdentity": adGenCndSystemTCIdentity}
)
