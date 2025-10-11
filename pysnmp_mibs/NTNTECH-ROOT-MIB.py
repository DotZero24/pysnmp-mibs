# SNMP MIB module (NTNTECH-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zhone/NTNTECH-ROOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:30 2025
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

ntntechRootMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8059)
)
if mibBuilder.loadTexts:
    ntntechRootMIB.setRevisions(
        ("1902-08-28 11:57",
         "1902-10-22 02:00",
         "1904-10-11 01:01",
         "1904-11-17 10:09")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NtnIpAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:2x:3x:4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class NtnDefaultGateway(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:2x:3x:4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class NtnSubnetMask(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:2x:3x:4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class NtnDisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class NtnMacAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class NtnTimeTicks(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class NtnCounter32(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class NtnGauge32(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class NtnTruthValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NtntechNamingTree_ObjectIdentity = ObjectIdentity
ntntechNamingTree = _NtntechNamingTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1)
)
_NtntechChassis_ObjectIdentity = ObjectIdentity
ntntechChassis = _NtntechChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1)
)
_NtntechChassisConfigurationMIB_ObjectIdentity = ObjectIdentity
ntntechChassisConfigurationMIB = _NtntechChassisConfigurationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1)
)
_NtntechChassisStatusMIB_ObjectIdentity = ObjectIdentity
ntntechChassisStatusMIB = _NtntechChassisStatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2)
)
_NtntechInterfaceModule_ObjectIdentity = ObjectIdentity
ntntechInterfaceModule = _NtntechInterfaceModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2)
)
_NtntechInterfaceModuleConfigurationMIB_ObjectIdentity = ObjectIdentity
ntntechInterfaceModuleConfigurationMIB = _NtntechInterfaceModuleConfigurationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1)
)
_NtntechInterfaceModuleStatusMIB_ObjectIdentity = ObjectIdentity
ntntechInterfaceModuleStatusMIB = _NtntechInterfaceModuleStatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2)
)
_NtntechQoSMIB_ObjectIdentity = ObjectIdentity
ntntechQoSMIB = _NtntechQoSMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 3)
)
_NtntechNMSTraps_ObjectIdentity = ObjectIdentity
ntntechNMSTraps = _NtntechNMSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3)
)
_NtntechNMSTrapsMIB_ObjectIdentity = ObjectIdentity
ntntechNMSTrapsMIB = _NtntechNMSTrapsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 1)
)
_NtntechSystemObjects_ObjectIdentity = ObjectIdentity
ntntechSystemObjects = _NtntechSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 4)
)
_NtntechSystemObjectsIdentifierMIB_ObjectIdentity = ObjectIdentity
ntntechSystemObjectsIdentifierMIB = _NtntechSystemObjectsIdentifierMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 4, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTNTECH-ROOT-MIB",
    **{"NtnIpAddress": NtnIpAddress,
       "NtnDefaultGateway": NtnDefaultGateway,
       "NtnSubnetMask": NtnSubnetMask,
       "NtnDisplayString": NtnDisplayString,
       "NtnMacAddress": NtnMacAddress,
       "NtnTimeTicks": NtnTimeTicks,
       "NtnCounter32": NtnCounter32,
       "NtnGauge32": NtnGauge32,
       "NtnTruthValue": NtnTruthValue,
       "ntntechRootMIB": ntntechRootMIB,
       "ntntechNamingTree": ntntechNamingTree,
       "ntntechChassis": ntntechChassis,
       "ntntechChassisConfigurationMIB": ntntechChassisConfigurationMIB,
       "ntntechChassisStatusMIB": ntntechChassisStatusMIB,
       "ntntechInterfaceModule": ntntechInterfaceModule,
       "ntntechInterfaceModuleConfigurationMIB": ntntechInterfaceModuleConfigurationMIB,
       "ntntechInterfaceModuleStatusMIB": ntntechInterfaceModuleStatusMIB,
       "ntntechQoSMIB": ntntechQoSMIB,
       "ntntechNMSTraps": ntntechNMSTraps,
       "ntntechNMSTrapsMIB": ntntechNMSTrapsMIB,
       "ntntechSystemObjects": ntntechSystemObjects,
       "ntntechSystemObjectsIdentifierMIB": ntntechSystemObjectsIdentifierMIB}
)
