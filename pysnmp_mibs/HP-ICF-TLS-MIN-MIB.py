# SNMP MIB module (HP-ICF-TLS-MIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-ICF-TLS-MIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:34:18 2025
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

hpicfTlsMinMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112)
)
if mibBuilder.loadTexts:
    hpicfTlsMinMIB.setRevisions(
        ("2020-02-24 09:00",
         "2017-05-11 09:00",
         "2017-04-05 09:00",
         "2016-06-22 09:00",
         "2014-10-01 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfTlsMinObjects_ObjectIdentity = ObjectIdentity
hpicfTlsMinObjects = _HpicfTlsMinObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0)
)
_HpicfTlsMinConfigObjects_ObjectIdentity = ObjectIdentity
hpicfTlsMinConfigObjects = _HpicfTlsMinConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1)
)
_HpicfTlsMinTable_Object = MibTable
hpicfTlsMinTable = _HpicfTlsMinTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfTlsMinTable.setStatus("current")
_HpicfTlsMinEntry_Object = MibTableRow
hpicfTlsMinEntry = _HpicfTlsMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1)
)
hpicfTlsMinEntry.setIndexNames(
    (0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"),
)
if mibBuilder.loadTexts:
    hpicfTlsMinEntry.setStatus("current")


class _HpicfTlsMinApp_Type(Integer32):
    """Custom type hpicfTlsMinApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("webSsl", 1),
          ("openflow", 2),
          ("syslog", 3),
          ("tr69", 4),
          ("cloud", 5),
          ("radsec", 6))
    )


_HpicfTlsMinApp_Type.__name__ = "Integer32"
_HpicfTlsMinApp_Object = MibTableColumn
hpicfTlsMinApp = _HpicfTlsMinApp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 1),
    _HpicfTlsMinApp_Type()
)
hpicfTlsMinApp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTlsMinApp.setStatus("current")


class _HpicfTlsMinVersion_Type(Integer32):
    """Custom type hpicfTlsMinVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tls1dot0", 1),
          ("tls1dot1", 2),
          ("tls1dot2", 3))
    )


_HpicfTlsMinVersion_Type.__name__ = "Integer32"
_HpicfTlsMinVersion_Object = MibTableColumn
hpicfTlsMinVersion = _HpicfTlsMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 2),
    _HpicfTlsMinVersion_Type()
)
hpicfTlsMinVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinVersion.setStatus("current")
_HpicfTlsMinCloseSSLSess_Type = TruthValue
_HpicfTlsMinCloseSSLSess_Object = MibTableColumn
hpicfTlsMinCloseSSLSess = _HpicfTlsMinCloseSSLSess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 3),
    _HpicfTlsMinCloseSSLSess_Type()
)
hpicfTlsMinCloseSSLSess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinCloseSSLSess.setStatus("current")
_HpicfTlsMinRowStatus_Type = RowStatus
_HpicfTlsMinRowStatus_Object = MibTableColumn
hpicfTlsMinRowStatus = _HpicfTlsMinRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 4),
    _HpicfTlsMinRowStatus_Type()
)
hpicfTlsMinRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinRowStatus.setStatus("current")


class _HpicfTlsStrictRfc5424_Type(TruthValue):
    """Custom type hpicfTlsStrictRfc5424 based on TruthValue"""
    defaultValue = 2


_HpicfTlsStrictRfc5424_Type.__name__ = "TruthValue"
_HpicfTlsStrictRfc5424_Object = MibTableColumn
hpicfTlsStrictRfc5424 = _HpicfTlsStrictRfc5424_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 5),
    _HpicfTlsStrictRfc5424_Type()
)
hpicfTlsStrictRfc5424.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTlsStrictRfc5424.setStatus("current")
_HpicfTlsMinCipherTable_Object = MibTable
hpicfTlsMinCipherTable = _HpicfTlsMinCipherTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfTlsMinCipherTable.setStatus("current")
_HpicfTlsMinCipherEntry_Object = MibTableRow
hpicfTlsMinCipherEntry = _HpicfTlsMinCipherEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1)
)
hpicfTlsMinCipherEntry.setIndexNames(
    (0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"),
    (0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipher"),
)
if mibBuilder.loadTexts:
    hpicfTlsMinCipherEntry.setStatus("current")


class _HpicfTlsMinCipher_Type(Integer32):
    """Custom type hpicfTlsMinCipher based on Integer32"""
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
              36)
        )
    )
    namedValues = NamedValues(
        *(("aes256Sha256", 1),
          ("aes256Sha", 2),
          ("aes128Sha256", 3),
          ("aes128Sha", 4),
          ("des3CbcSha", 5),
          ("aes256GcmSha384", 6),
          ("aes128GcmSha256", 7),
          ("ecdhEcdsaAes256GcmSha384", 8),
          ("ecdhRsaAaes256GcmSha384", 9),
          ("ecdhEcdsaAes128GcmSha256", 10),
          ("ecdhRsaAes128GcmSha256", 11),
          ("ecdhEcdsaAes256Sha384", 12),
          ("ecdhRsaAes256Sha384", 13),
          ("ecdhEcdsaAes256Sha", 14),
          ("ecdhRsaAes256Sha", 15),
          ("ecdhEcdsaAes128Sha256", 16),
          ("ecdhRsaAes128Sha256", 17),
          ("ecdhEcdsaAes128Sha", 18),
          ("ecdhRsaAes128Sha", 19),
          ("ecdhEcdsaDesCbc3Sha", 20),
          ("ecdhRsaDesCbc3Sha", 21),
          ("ecdheEcdsaAes128GcmSha256", 22),
          ("ecdheRsaAes128GcmSha256", 23),
          ("ecdheEcdsaAes128Sha256", 24),
          ("ecdheRsaAes128Sha256", 25),
          ("ecdheEcdsaAes128Sha", 26),
          ("ecdheRsaAes128Sha", 27),
          ("ecdheEcdsaAes256GcmSha384", 28),
          ("ecdheRsaAes256GcmSha384", 29),
          ("ecdheEcdsaAes256Sha384", 30),
          ("ecdheRsaAes256Sha384", 31),
          ("ecdheEcdsaAes256Sha", 32),
          ("ecdheRsaAes256Sha", 33),
          ("ecdheEcdsaDesCbc3Sha", 34),
          ("ecdheRsaDesCbc3Sha", 35),
          ("all", 36))
    )


_HpicfTlsMinCipher_Type.__name__ = "Integer32"
_HpicfTlsMinCipher_Object = MibTableColumn
hpicfTlsMinCipher = _HpicfTlsMinCipher_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 1),
    _HpicfTlsMinCipher_Type()
)
hpicfTlsMinCipher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTlsMinCipher.setStatus("current")
_HpicfTlsMinCipherRowStatus_Type = RowStatus
_HpicfTlsMinCipherRowStatus_Object = MibTableColumn
hpicfTlsMinCipherRowStatus = _HpicfTlsMinCipherRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 2),
    _HpicfTlsMinCipherRowStatus_Type()
)
hpicfTlsMinCipherRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinCipherRowStatus.setStatus("current")


class _HpicfTlsMinCipherConfig_Type(Integer32):
    """Custom type hpicfTlsMinCipherConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enforce", 1),
          ("disable", 2))
    )


_HpicfTlsMinCipherConfig_Type.__name__ = "Integer32"
_HpicfTlsMinCipherConfig_Object = MibTableColumn
hpicfTlsMinCipherConfig = _HpicfTlsMinCipherConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 3),
    _HpicfTlsMinCipherConfig_Type()
)
hpicfTlsMinCipherConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTlsMinCipherConfig.setStatus("current")
_HpicfTlsMinConformance_ObjectIdentity = ObjectIdentity
hpicfTlsMinConformance = _HpicfTlsMinConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1)
)
_HpicfTlsMinCompliances_ObjectIdentity = ObjectIdentity
hpicfTlsMinCompliances = _HpicfTlsMinCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1)
)
_HpicfTlsMinGroups_ObjectIdentity = ObjectIdentity
hpicfTlsMinGroups = _HpicfTlsMinGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2)
)

# Managed Objects groups

hpicfTlsMinConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 1)
)
hpicfTlsMinConfigGroup.setObjects(
      *(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfTlsMinConfigGroup.setStatus("deprecated")

hpicfTlsMinConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 2)
)
hpicfTlsMinConfigGroup1.setObjects(
      *(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
)
if mibBuilder.loadTexts:
    hpicfTlsMinConfigGroup1.setStatus("deprecated")

hpicfTlsMinConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 3)
)
hpicfTlsMinConfigGroup2.setObjects(
      *(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
)
if mibBuilder.loadTexts:
    hpicfTlsMinConfigGroup2.setStatus("deprecated")

hpicfTlsMinConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 4)
)
hpicfTlsMinConfigGroup3.setObjects(
      *(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"),
        ("HP-ICF-TLS-MIN-MIB", "hpicfTlsStrictRfc5424"))
)
if mibBuilder.loadTexts:
    hpicfTlsMinConfigGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfTlsMinCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 1)
)
hpicfTlsMinCompliance1.setObjects(
    ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup")
)
if mibBuilder.loadTexts:
    hpicfTlsMinCompliance1.setStatus(
        "deprecated"
    )

hpicfTlsMinCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 2)
)
hpicfTlsMinCompliance2.setObjects(
    ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup1")
)
if mibBuilder.loadTexts:
    hpicfTlsMinCompliance2.setStatus(
        "deprecated"
    )

hpicfTlsMinCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 3)
)
hpicfTlsMinCompliance3.setObjects(
    ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup2")
)
if mibBuilder.loadTexts:
    hpicfTlsMinCompliance3.setStatus(
        "deprecated"
    )

hpicfTlsMinCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 4)
)
hpicfTlsMinCompliance4.setObjects(
    ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup3")
)
if mibBuilder.loadTexts:
    hpicfTlsMinCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-TLS-MIN-MIB",
    **{"hpicfTlsMinMIB": hpicfTlsMinMIB,
       "hpicfTlsMinObjects": hpicfTlsMinObjects,
       "hpicfTlsMinConfigObjects": hpicfTlsMinConfigObjects,
       "hpicfTlsMinTable": hpicfTlsMinTable,
       "hpicfTlsMinEntry": hpicfTlsMinEntry,
       "hpicfTlsMinApp": hpicfTlsMinApp,
       "hpicfTlsMinVersion": hpicfTlsMinVersion,
       "hpicfTlsMinCloseSSLSess": hpicfTlsMinCloseSSLSess,
       "hpicfTlsMinRowStatus": hpicfTlsMinRowStatus,
       "hpicfTlsStrictRfc5424": hpicfTlsStrictRfc5424,
       "hpicfTlsMinCipherTable": hpicfTlsMinCipherTable,
       "hpicfTlsMinCipherEntry": hpicfTlsMinCipherEntry,
       "hpicfTlsMinCipher": hpicfTlsMinCipher,
       "hpicfTlsMinCipherRowStatus": hpicfTlsMinCipherRowStatus,
       "hpicfTlsMinCipherConfig": hpicfTlsMinCipherConfig,
       "hpicfTlsMinConformance": hpicfTlsMinConformance,
       "hpicfTlsMinCompliances": hpicfTlsMinCompliances,
       "hpicfTlsMinCompliance1": hpicfTlsMinCompliance1,
       "hpicfTlsMinCompliance2": hpicfTlsMinCompliance2,
       "hpicfTlsMinCompliance3": hpicfTlsMinCompliance3,
       "hpicfTlsMinCompliance4": hpicfTlsMinCompliance4,
       "hpicfTlsMinGroups": hpicfTlsMinGroups,
       "hpicfTlsMinConfigGroup": hpicfTlsMinConfigGroup,
       "hpicfTlsMinConfigGroup1": hpicfTlsMinConfigGroup1,
       "hpicfTlsMinConfigGroup2": hpicfTlsMinConfigGroup2,
       "hpicfTlsMinConfigGroup3": hpicfTlsMinConfigGroup3}
)
