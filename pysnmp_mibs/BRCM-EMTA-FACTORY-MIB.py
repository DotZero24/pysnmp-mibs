# SNMP MIB module (BRCM-EMTA-FACTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-EMTA-FACTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:54 2025
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

(cableDataFactory,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-FACTORY-MIB",
    "cableDataFactory")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

emtaFactory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    emtaFactory.setRevisions(
        ("2007-02-05 00:00",
         "2005-11-14 00:00",
         "2005-06-28 00:00",
         "2005-06-14 00:00",
         "2004-03-24 00:00",
         "2002-08-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EmtaFactoryBase_ObjectIdentity = ObjectIdentity
emtaFactoryBase = _EmtaFactoryBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6, 1)
)
_EmtaHighVoltageRingEnabled_Type = TruthValue
_EmtaHighVoltageRingEnabled_Object = MibScalar
emtaHighVoltageRingEnabled = _EmtaHighVoltageRingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6, 1, 1),
    _EmtaHighVoltageRingEnabled_Type()
)
emtaHighVoltageRingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emtaHighVoltageRingEnabled.setStatus("current")
_EmtaDynamicLoadBalancingEnabled_Type = TruthValue
_EmtaDynamicLoadBalancingEnabled_Object = MibScalar
emtaDynamicLoadBalancingEnabled = _EmtaDynamicLoadBalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6, 1, 2),
    _EmtaDynamicLoadBalancingEnabled_Type()
)
emtaDynamicLoadBalancingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emtaDynamicLoadBalancingEnabled.setStatus("current")
_EmtaFactorySecurity_ObjectIdentity = ObjectIdentity
emtaFactorySecurity = _EmtaFactorySecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6, 2)
)
_EmtaTelephonyRootCertificate_Type = OctetString
_EmtaTelephonyRootCertificate_Object = MibScalar
emtaTelephonyRootCertificate = _EmtaTelephonyRootCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6, 2, 1),
    _EmtaTelephonyRootCertificate_Type()
)
emtaTelephonyRootCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emtaTelephonyRootCertificate.setStatus("current")
_EmtaManufacturerCertificate_Type = OctetString
_EmtaManufacturerCertificate_Object = MibScalar
emtaManufacturerCertificate = _EmtaManufacturerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6, 2, 2),
    _EmtaManufacturerCertificate_Type()
)
emtaManufacturerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emtaManufacturerCertificate.setStatus("current")
_EmtaDeviceCertificate_Type = OctetString
_EmtaDeviceCertificate_Object = MibScalar
emtaDeviceCertificate = _EmtaDeviceCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6, 2, 3),
    _EmtaDeviceCertificate_Type()
)
emtaDeviceCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emtaDeviceCertificate.setStatus("current")
_EmtaDevPrivKeyModulus_Type = OctetString
_EmtaDevPrivKeyModulus_Object = MibScalar
emtaDevPrivKeyModulus = _EmtaDevPrivKeyModulus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6, 2, 4),
    _EmtaDevPrivKeyModulus_Type()
)
emtaDevPrivKeyModulus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emtaDevPrivKeyModulus.setStatus("current")
_EmtaDevPrivKeyExponent_Type = OctetString
_EmtaDevPrivKeyExponent_Object = MibScalar
emtaDevPrivKeyExponent = _EmtaDevPrivKeyExponent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 6, 2, 5),
    _EmtaDevPrivKeyExponent_Type()
)
emtaDevPrivKeyExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emtaDevPrivKeyExponent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-EMTA-FACTORY-MIB",
    **{"emtaFactory": emtaFactory,
       "emtaFactoryBase": emtaFactoryBase,
       "emtaHighVoltageRingEnabled": emtaHighVoltageRingEnabled,
       "emtaDynamicLoadBalancingEnabled": emtaDynamicLoadBalancingEnabled,
       "emtaFactorySecurity": emtaFactorySecurity,
       "emtaTelephonyRootCertificate": emtaTelephonyRootCertificate,
       "emtaManufacturerCertificate": emtaManufacturerCertificate,
       "emtaDeviceCertificate": emtaDeviceCertificate,
       "emtaDevPrivKeyModulus": emtaDevPrivKeyModulus,
       "emtaDevPrivKeyExponent": emtaDevPrivKeyExponent}
)
