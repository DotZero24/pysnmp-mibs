# SNMP MIB module (QTECH-WLAN-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-WLAN-SECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:51 2025
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

(qtechApgWlanId,) = mibBuilder.importSymbols(
    "QTECH-AC-MGMT-MIB",
    "qtechApgWlanId")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechWLANsecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61)
)
if mibBuilder.loadTexts:
    qtechWLANsecurityMIB.setRevisions(
        ("2009-10-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechWLANsecurityTraps_ObjectIdentity = ObjectIdentity
qtechWLANsecurityTraps = _QtechWLANsecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 0)
)
_QtechWLANsecurityMIBObjects_ObjectIdentity = ObjectIdentity
qtechWLANsecurityMIBObjects = _QtechWLANsecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1)
)


class _QtechAPworkmode_Type(Integer32):
    """Custom type qtechAPworkmode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fitap", 1),
          ("fatap", 2))
    )


_QtechAPworkmode_Type.__name__ = "Integer32"
_QtechAPworkmode_Object = MibScalar
qtechAPworkmode = _QtechAPworkmode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 1),
    _QtechAPworkmode_Type()
)
qtechAPworkmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAPworkmode.setStatus("current")
_QtechWLANsecurityConfigTable_Object = MibTable
qtechWLANsecurityConfigTable = _QtechWLANsecurityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2)
)
if mibBuilder.loadTexts:
    qtechWLANsecurityConfigTable.setStatus("current")
_QtechWLANsecurityConfigEntry_Object = MibTableRow
qtechWLANsecurityConfigEntry = _QtechWLANsecurityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1)
)
qtechWLANsecurityConfigEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
)
if mibBuilder.loadTexts:
    qtechWLANsecurityConfigEntry.setStatus("current")


class _QtechWLANsecrymode_Type(Integer32):
    """Custom type qtechWLANsecrymode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("staticwep", 2),
          ("wep8021x", 3),
          ("wpanone", 4),
          ("wpapsk", 5),
          ("wpa8021x", 6),
          ("tsn", 7))
    )


_QtechWLANsecrymode_Type.__name__ = "Integer32"
_QtechWLANsecrymode_Object = MibTableColumn
qtechWLANsecrymode = _QtechWLANsecrymode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 1),
    _QtechWLANsecrymode_Type()
)
qtechWLANsecrymode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWLANsecrymode.setStatus("current")


class _Qtechstaticweplength_Type(Integer32):
    """Custom type qtechstaticweplength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wep40", 1),
          ("wep104", 2),
          ("wep128", 3))
    )


_Qtechstaticweplength_Type.__name__ = "Integer32"
_Qtechstaticweplength_Object = MibTableColumn
qtechstaticweplength = _Qtechstaticweplength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 2),
    _Qtechstaticweplength_Type()
)
qtechstaticweplength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechstaticweplength.setStatus("current")


class _Qtech8021xweplength_Type(Integer32):
    """Custom type qtech8021xweplength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wep40", 1),
          ("wep104", 2),
          ("wep128", 3))
    )


_Qtech8021xweplength_Type.__name__ = "Integer32"
_Qtech8021xweplength_Object = MibTableColumn
qtech8021xweplength = _Qtech8021xweplength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 3),
    _Qtech8021xweplength_Type()
)
qtech8021xweplength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech8021xweplength.setStatus("current")


class _QtechWPAenabled_Type(TruthValue):
    """Custom type qtechWPAenabled based on TruthValue"""
    defaultValue = 2


_QtechWPAenabled_Type.__name__ = "TruthValue"
_QtechWPAenabled_Object = MibTableColumn
qtechWPAenabled = _QtechWPAenabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 4),
    _QtechWPAenabled_Type()
)
qtechWPAenabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWPAenabled.setStatus("current")


class _QtechWPAPairwisecipher_Type(Integer32):
    """Custom type qtechWPAPairwisecipher based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("tkiporaes", 3))
    )


_QtechWPAPairwisecipher_Type.__name__ = "Integer32"
_QtechWPAPairwisecipher_Object = MibTableColumn
qtechWPAPairwisecipher = _QtechWPAPairwisecipher_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 5),
    _QtechWPAPairwisecipher_Type()
)
qtechWPAPairwisecipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWPAPairwisecipher.setStatus("current")


class _QtechWPAakmmode_Type(Integer32):
    """Custom type qtechWPAakmmode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021x", 1),
          ("psk", 2),
          ("pskor8021x", 3))
    )


_QtechWPAakmmode_Type.__name__ = "Integer32"
_QtechWPAakmmode_Object = MibTableColumn
qtechWPAakmmode = _QtechWPAakmmode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 6),
    _QtechWPAakmmode_Type()
)
qtechWPAakmmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWPAakmmode.setStatus("current")
_QtechWPApskPassPhrase_Type = DisplayString
_QtechWPApskPassPhrase_Object = MibTableColumn
qtechWPApskPassPhrase = _QtechWPApskPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 7),
    _QtechWPApskPassPhrase_Type()
)
qtechWPApskPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWPApskPassPhrase.setStatus("current")


class _QtechWLANsecry80211i_Type(TruthValue):
    """Custom type qtechWLANsecry80211i based on TruthValue"""
    defaultValue = 1


_QtechWLANsecry80211i_Type.__name__ = "TruthValue"
_QtechWLANsecry80211i_Object = MibTableColumn
qtechWLANsecry80211i = _QtechWLANsecry80211i_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 8),
    _QtechWLANsecry80211i_Type()
)
qtechWLANsecry80211i.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWLANsecry80211i.setStatus("current")


class _QtechWAPIasuIpaddress_Type(Unsigned32):
    """Custom type qtechWAPIasuIpaddress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechWAPIasuIpaddress_Type.__name__ = "Unsigned32"
_QtechWAPIasuIpaddress_Object = MibTableColumn
qtechWAPIasuIpaddress = _QtechWAPIasuIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 9),
    _QtechWAPIasuIpaddress_Type()
)
qtechWAPIasuIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWAPIasuIpaddress.setStatus("current")


class _QtechWAPIcertificateformat_Type(Integer32):
    """Custom type qtechWAPIcertificateformat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("x509v3", 1),
          ("wapigbw", 2))
    )


_QtechWAPIcertificateformat_Type.__name__ = "Integer32"
_QtechWAPIcertificateformat_Object = MibTableColumn
qtechWAPIcertificateformat = _QtechWAPIcertificateformat_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 10),
    _QtechWAPIcertificateformat_Type()
)
qtechWAPIcertificateformat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWAPIcertificateformat.setStatus("current")


class _QtechWAPImsrekeyClientoff_Type(TruthValue):
    """Custom type qtechWAPImsrekeyClientoff based on TruthValue"""
    defaultValue = 2


_QtechWAPImsrekeyClientoff_Type.__name__ = "TruthValue"
_QtechWAPImsrekeyClientoff_Object = MibTableColumn
qtechWAPImsrekeyClientoff = _QtechWAPImsrekeyClientoff_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 11),
    _QtechWAPImsrekeyClientoff_Type()
)
qtechWAPImsrekeyClientoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWAPImsrekeyClientoff.setStatus("current")


class _QtechWAPIimportcertificate_Type(Integer32):
    """Custom type qtechWAPIimportcertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ca", 1),
          ("local", 2),
          ("as", 3))
    )


_QtechWAPIimportcertificate_Type.__name__ = "Integer32"
_QtechWAPIimportcertificate_Object = MibTableColumn
qtechWAPIimportcertificate = _QtechWAPIimportcertificate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 12),
    _QtechWAPIimportcertificate_Type()
)
qtechWAPIimportcertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWAPIimportcertificate.setStatus("current")
_QtechWAPIcacertificatename_Type = DisplayString
_QtechWAPIcacertificatename_Object = MibTableColumn
qtechWAPIcacertificatename = _QtechWAPIcacertificatename_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 13),
    _QtechWAPIcacertificatename_Type()
)
qtechWAPIcacertificatename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWAPIcacertificatename.setStatus("current")
_QtechWAPIlocalcertificatename_Type = DisplayString
_QtechWAPIlocalcertificatename_Object = MibTableColumn
qtechWAPIlocalcertificatename = _QtechWAPIlocalcertificatename_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 14),
    _QtechWAPIlocalcertificatename_Type()
)
qtechWAPIlocalcertificatename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWAPIlocalcertificatename.setStatus("current")
_QtechWAPIascertificatename_Type = DisplayString
_QtechWAPIascertificatename_Object = MibTableColumn
qtechWAPIascertificatename = _QtechWAPIascertificatename_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 15),
    _QtechWAPIascertificatename_Type()
)
qtechWAPIascertificatename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWAPIascertificatename.setStatus("current")
_QtechRSNenabled_Type = TruthValue
_QtechRSNenabled_Object = MibTableColumn
qtechRSNenabled = _QtechRSNenabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 16),
    _QtechRSNenabled_Type()
)
qtechRSNenabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRSNenabled.setStatus("current")


class _QtechRSNPairwisecipher_Type(Integer32):
    """Custom type qtechRSNPairwisecipher based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("tkiporaes", 3))
    )


_QtechRSNPairwisecipher_Type.__name__ = "Integer32"
_QtechRSNPairwisecipher_Object = MibTableColumn
qtechRSNPairwisecipher = _QtechRSNPairwisecipher_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 17),
    _QtechRSNPairwisecipher_Type()
)
qtechRSNPairwisecipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRSNPairwisecipher.setStatus("current")


class _QtechRSNakmmode_Type(Integer32):
    """Custom type qtechRSNakmmode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021x", 1),
          ("psk", 2),
          ("pskor8021x", 3))
    )


_QtechRSNakmmode_Type.__name__ = "Integer32"
_QtechRSNakmmode_Object = MibTableColumn
qtechRSNakmmode = _QtechRSNakmmode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 18),
    _QtechRSNakmmode_Type()
)
qtechRSNakmmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRSNakmmode.setStatus("current")
_QtechRSNpskPassPhrase_Type = DisplayString
_QtechRSNpskPassPhrase_Object = MibTableColumn
qtechRSNpskPassPhrase = _QtechRSNpskPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 19),
    _QtechRSNpskPassPhrase_Type()
)
qtechRSNpskPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRSNpskPassPhrase.setStatus("current")


class _QtechWEPAuthenAlgorithm_Type(Integer32):
    """Custom type qtechWEPAuthenAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_QtechWEPAuthenAlgorithm_Type.__name__ = "Integer32"
_QtechWEPAuthenAlgorithm_Object = MibTableColumn
qtechWEPAuthenAlgorithm = _QtechWEPAuthenAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 20),
    _QtechWEPAuthenAlgorithm_Type()
)
qtechWEPAuthenAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWEPAuthenAlgorithm.setStatus("current")
_QtechWLANsecurityStatus_Type = RowStatus
_QtechWLANsecurityStatus_Object = MibTableColumn
qtechWLANsecurityStatus = _QtechWLANsecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 21),
    _QtechWLANsecurityStatus_Type()
)
qtechWLANsecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWLANsecurityStatus.setStatus("current")
_QtechACauthenMethodsupport_Type = Integer32
_QtechACauthenMethodsupport_Object = MibTableColumn
qtechACauthenMethodsupport = _QtechACauthenMethodsupport_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 22),
    _QtechACauthenMethodsupport_Type()
)
qtechACauthenMethodsupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechACauthenMethodsupport.setStatus("current")


class _QtechWLANEAPAuthenSupport_Type(Integer32):
    """Custom type qtechWLANEAPAuthenSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableEAPAuthentication", 0),
          ("disableEAPAuthentication", 1),
          ("notSupportingEAPAuthentication", 2))
    )


_QtechWLANEAPAuthenSupport_Type.__name__ = "Integer32"
_QtechWLANEAPAuthenSupport_Object = MibTableColumn
qtechWLANEAPAuthenSupport = _QtechWLANEAPAuthenSupport_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 2, 1, 23),
    _QtechWLANEAPAuthenSupport_Type()
)
qtechWLANEAPAuthenSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWLANEAPAuthenSupport.setStatus("current")
_QtechWEPDefaultKeysTable_Object = MibTable
qtechWEPDefaultKeysTable = _QtechWEPDefaultKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 3)
)
if mibBuilder.loadTexts:
    qtechWEPDefaultKeysTable.setStatus("current")
_QtechWEPDefaultKeysEntry_Object = MibTableRow
qtechWEPDefaultKeysEntry = _QtechWEPDefaultKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 3, 1)
)
qtechWEPDefaultKeysEntry.setIndexNames(
    (0, "QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
    (0, "QTECH-WLAN-SECURITY-MIB", "qtechWEPDefaultKeyIndex"),
)
if mibBuilder.loadTexts:
    qtechWEPDefaultKeysEntry.setStatus("current")


class _QtechWEPDefaultKeyIndex_Type(Integer32):
    """Custom type qtechWEPDefaultKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_QtechWEPDefaultKeyIndex_Type.__name__ = "Integer32"
_QtechWEPDefaultKeyIndex_Object = MibTableColumn
qtechWEPDefaultKeyIndex = _QtechWEPDefaultKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 3, 1, 1),
    _QtechWEPDefaultKeyIndex_Type()
)
qtechWEPDefaultKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechWEPDefaultKeyIndex.setStatus("current")
_QtechWEPDefaultKeyValue_Type = OctetString
_QtechWEPDefaultKeyValue_Object = MibTableColumn
qtechWEPDefaultKeyValue = _QtechWEPDefaultKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 3, 1, 2),
    _QtechWEPDefaultKeyValue_Type()
)
qtechWEPDefaultKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWEPDefaultKeyValue.setStatus("current")


class _QtechWEPDefaultKeyLength_Type(Integer32):
    """Custom type qtechWEPDefaultKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wep40", 1),
          ("wep104", 2),
          ("wep128", 3))
    )


_QtechWEPDefaultKeyLength_Type.__name__ = "Integer32"
_QtechWEPDefaultKeyLength_Object = MibTableColumn
qtechWEPDefaultKeyLength = _QtechWEPDefaultKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 1, 3, 1, 3),
    _QtechWEPDefaultKeyLength_Type()
)
qtechWEPDefaultKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWEPDefaultKeyLength.setStatus("current")
_QtechWlansecurityMIBConform_ObjectIdentity = ObjectIdentity
qtechWlansecurityMIBConform = _QtechWlansecurityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 2)
)
_QtechWlansecurityMIBCompliances_ObjectIdentity = ObjectIdentity
qtechWlansecurityMIBCompliances = _QtechWlansecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 2, 1)
)
_QtechWlansecurityMIBGroups_ObjectIdentity = ObjectIdentity
qtechWlansecurityMIBGroups = _QtechWlansecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 2, 2)
)
_QtechWlansecurityTrapvar_ObjectIdentity = ObjectIdentity
qtechWlansecurityTrapvar = _QtechWlansecurityTrapvar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 3)
)
_QtechWlansecurityWepDecrytEnableTrapVar_Type = Integer32
_QtechWlansecurityWepDecrytEnableTrapVar_Object = MibScalar
qtechWlansecurityWepDecrytEnableTrapVar = _QtechWlansecurityWepDecrytEnableTrapVar_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 3, 1),
    _QtechWlansecurityWepDecrytEnableTrapVar_Type()
)
qtechWlansecurityWepDecrytEnableTrapVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlansecurityWepDecrytEnableTrapVar.setStatus("current")
_QtechWlansecurityDeviceMAC_Type = MacAddress
_QtechWlansecurityDeviceMAC_Object = MibScalar
qtechWlansecurityDeviceMAC = _QtechWlansecurityDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 3, 2),
    _QtechWlansecurityDeviceMAC_Type()
)
qtechWlansecurityDeviceMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWlansecurityDeviceMAC.setStatus("current")

# Managed Objects groups

qtechWlansecuritycofigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 2, 2, 1)
)
qtechWlansecuritycofigGroup.setObjects(
      *(("QTECH-WLAN-SECURITY-MIB", "qtechAPworkmode"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWLANsecrymode"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechstaticweplength"),
        ("QTECH-WLAN-SECURITY-MIB", "qtech8021xweplength"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWPAenabled"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWPAPairwisecipher"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWPAakmmode"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWPApskPassPhrase"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWLANsecry80211i"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWAPIasuIpaddress"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWAPIcertificateformat"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWAPImsrekeyClientoff"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWAPIimportcertificate"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWAPIcacertificatename"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWAPIlocalcertificatename"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWAPIascertificatename"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechRSNenabled"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechRSNPairwisecipher"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechRSNakmmode"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechRSNpskPassPhrase"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWEPAuthenAlgorithm"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWLANsecurityStatus"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechACauthenMethodsupport"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWLANEAPAuthenSupport"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWlansecurityWepDecrytEnableTrapVar"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWlansecurityDeviceMAC"))
)
if mibBuilder.loadTexts:
    qtechWlansecuritycofigGroup.setStatus("current")

qtechWEPDefaultKeysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 2, 2, 2)
)
qtechWEPDefaultKeysGroup.setObjects(
      *(("QTECH-WLAN-SECURITY-MIB", "qtechWEPDefaultKeyValue"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWEPDefaultKeyLength"))
)
if mibBuilder.loadTexts:
    qtechWEPDefaultKeysGroup.setStatus("current")


# Notification objects

qtechWlansecurityWepDecrytErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 0, 1)
)
qtechWlansecurityWepDecrytErr.setObjects(
      *(("QTECH-AC-MGMT-MIB", "qtechApgWlanId"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWlansecurityDeviceMAC"))
)
if mibBuilder.loadTexts:
    qtechWlansecurityWepDecrytErr.setStatus(
        "current"
    )


# Notifications groups

qtechWlansecurityTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 2, 2, 3)
)
qtechWlansecurityTrapGroup.setObjects(
    ("QTECH-WLAN-SECURITY-MIB", "qtechWlansecurityWepDecrytErr")
)
if mibBuilder.loadTexts:
    qtechWlansecurityTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechWlansecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 61, 2, 1, 1)
)
qtechWlansecurityMIBCompliance.setObjects(
      *(("QTECH-WLAN-SECURITY-MIB", "qtechWlansecuritycofigGroup"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWEPDefaultKeysGroup"),
        ("QTECH-WLAN-SECURITY-MIB", "qtechWlansecurityTrapGroup"))
)
if mibBuilder.loadTexts:
    qtechWlansecurityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-WLAN-SECURITY-MIB",
    **{"qtechWLANsecurityMIB": qtechWLANsecurityMIB,
       "qtechWLANsecurityTraps": qtechWLANsecurityTraps,
       "qtechWlansecurityWepDecrytErr": qtechWlansecurityWepDecrytErr,
       "qtechWLANsecurityMIBObjects": qtechWLANsecurityMIBObjects,
       "qtechAPworkmode": qtechAPworkmode,
       "qtechWLANsecurityConfigTable": qtechWLANsecurityConfigTable,
       "qtechWLANsecurityConfigEntry": qtechWLANsecurityConfigEntry,
       "qtechWLANsecrymode": qtechWLANsecrymode,
       "qtechstaticweplength": qtechstaticweplength,
       "qtech8021xweplength": qtech8021xweplength,
       "qtechWPAenabled": qtechWPAenabled,
       "qtechWPAPairwisecipher": qtechWPAPairwisecipher,
       "qtechWPAakmmode": qtechWPAakmmode,
       "qtechWPApskPassPhrase": qtechWPApskPassPhrase,
       "qtechWLANsecry80211i": qtechWLANsecry80211i,
       "qtechWAPIasuIpaddress": qtechWAPIasuIpaddress,
       "qtechWAPIcertificateformat": qtechWAPIcertificateformat,
       "qtechWAPImsrekeyClientoff": qtechWAPImsrekeyClientoff,
       "qtechWAPIimportcertificate": qtechWAPIimportcertificate,
       "qtechWAPIcacertificatename": qtechWAPIcacertificatename,
       "qtechWAPIlocalcertificatename": qtechWAPIlocalcertificatename,
       "qtechWAPIascertificatename": qtechWAPIascertificatename,
       "qtechRSNenabled": qtechRSNenabled,
       "qtechRSNPairwisecipher": qtechRSNPairwisecipher,
       "qtechRSNakmmode": qtechRSNakmmode,
       "qtechRSNpskPassPhrase": qtechRSNpskPassPhrase,
       "qtechWEPAuthenAlgorithm": qtechWEPAuthenAlgorithm,
       "qtechWLANsecurityStatus": qtechWLANsecurityStatus,
       "qtechACauthenMethodsupport": qtechACauthenMethodsupport,
       "qtechWLANEAPAuthenSupport": qtechWLANEAPAuthenSupport,
       "qtechWEPDefaultKeysTable": qtechWEPDefaultKeysTable,
       "qtechWEPDefaultKeysEntry": qtechWEPDefaultKeysEntry,
       "qtechWEPDefaultKeyIndex": qtechWEPDefaultKeyIndex,
       "qtechWEPDefaultKeyValue": qtechWEPDefaultKeyValue,
       "qtechWEPDefaultKeyLength": qtechWEPDefaultKeyLength,
       "qtechWlansecurityMIBConform": qtechWlansecurityMIBConform,
       "qtechWlansecurityMIBCompliances": qtechWlansecurityMIBCompliances,
       "qtechWlansecurityMIBCompliance": qtechWlansecurityMIBCompliance,
       "qtechWlansecurityMIBGroups": qtechWlansecurityMIBGroups,
       "qtechWlansecuritycofigGroup": qtechWlansecuritycofigGroup,
       "qtechWEPDefaultKeysGroup": qtechWEPDefaultKeysGroup,
       "qtechWlansecurityTrapGroup": qtechWlansecurityTrapGroup,
       "qtechWlansecurityTrapvar": qtechWlansecurityTrapvar,
       "qtechWlansecurityWepDecrytEnableTrapVar": qtechWlansecurityWepDecrytEnableTrapVar,
       "qtechWlansecurityDeviceMAC": qtechWlansecurityDeviceMAC}
)
