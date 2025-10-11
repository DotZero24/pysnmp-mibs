# SNMP MIB module (ADTRAN-TAeSCUEXT1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TAeSCUEXT1-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:44 2025
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

(adGenSlotInfoIndex,
 adGenSlotProdName) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex",
    "adGenSlotProdName")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adTAeSCUNetworkMgmt,
 adTAeSCUSecAccountUserID,
 adTAeSCUmg,
 adTAeSCUmgNotificationEvents) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCU-MIB",
    "adTAeSCUNetworkMgmt",
    "adTAeSCUSecAccountUserID",
    "adTAeSCUmg",
    "adTAeSCUmgNotificationEvents")

(AdPresence,) = mibBuilder.importSymbols(
    "ADTRAN-TC",
    "AdPresence")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adtranTAeSCUExt1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 241)
)
if mibBuilder.loadTexts:
    adtranTAeSCUExt1MIB.setRevisions(
        ("2013-09-19 10:18",
         "2012-08-14 13:00",
         "2007-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTaIPServicePortProvMgmt_ObjectIdentity = ObjectIdentity
adTaIPServicePortProvMgmt = _AdTaIPServicePortProvMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20)
)


class _AdTaTL1TelnetPortNumber_Type(Integer32):
    """Custom type adTaTL1TelnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaTL1TelnetPortNumber_Type.__name__ = "Integer32"
_AdTaTL1TelnetPortNumber_Object = MibScalar
adTaTL1TelnetPortNumber = _AdTaTL1TelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 1),
    _AdTaTL1TelnetPortNumber_Type()
)
adTaTL1TelnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaTL1TelnetPortNumber.setStatus("current")


class _AdTaTL1RawTCPPortNumber_Type(Integer32):
    """Custom type adTaTL1RawTCPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaTL1RawTCPPortNumber_Type.__name__ = "Integer32"
_AdTaTL1RawTCPPortNumber_Object = MibScalar
adTaTL1RawTCPPortNumber = _AdTaTL1RawTCPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 3),
    _AdTaTL1RawTCPPortNumber_Type()
)
adTaTL1RawTCPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaTL1RawTCPPortNumber.setStatus("current")


class _AdTaSecondaryTelnetPortNumber_Type(Integer32):
    """Custom type adTaSecondaryTelnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaSecondaryTelnetPortNumber_Type.__name__ = "Integer32"
_AdTaSecondaryTelnetPortNumber_Object = MibScalar
adTaSecondaryTelnetPortNumber = _AdTaSecondaryTelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 5),
    _AdTaSecondaryTelnetPortNumber_Type()
)
adTaSecondaryTelnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSecondaryTelnetPortNumber.setStatus("current")


class _AdTaNtwkTerminalTelnetPortNumber_Type(Integer32):
    """Custom type adTaNtwkTerminalTelnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaNtwkTerminalTelnetPortNumber_Type.__name__ = "Integer32"
_AdTaNtwkTerminalTelnetPortNumber_Object = MibScalar
adTaNtwkTerminalTelnetPortNumber = _AdTaNtwkTerminalTelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 6),
    _AdTaNtwkTerminalTelnetPortNumber_Type()
)
adTaNtwkTerminalTelnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaNtwkTerminalTelnetPortNumber.setStatus("current")


class _AdTaAdminTerminalTelnetPortNumber_Type(Integer32):
    """Custom type adTaAdminTerminalTelnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaAdminTerminalTelnetPortNumber_Type.__name__ = "Integer32"
_AdTaAdminTerminalTelnetPortNumber_Object = MibScalar
adTaAdminTerminalTelnetPortNumber = _AdTaAdminTerminalTelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 7),
    _AdTaAdminTerminalTelnetPortNumber_Type()
)
adTaAdminTerminalTelnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaAdminTerminalTelnetPortNumber.setStatus("current")


class _AdTaCraftTerminalTelnetPortNumber_Type(Integer32):
    """Custom type adTaCraftTerminalTelnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaCraftTerminalTelnetPortNumber_Type.__name__ = "Integer32"
_AdTaCraftTerminalTelnetPortNumber_Object = MibScalar
adTaCraftTerminalTelnetPortNumber = _AdTaCraftTerminalTelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 8),
    _AdTaCraftTerminalTelnetPortNumber_Type()
)
adTaCraftTerminalTelnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaCraftTerminalTelnetPortNumber.setStatus("current")


class _AdTaTL1SSHPortNumber_Type(Integer32):
    """Custom type adTaTL1SSHPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaTL1SSHPortNumber_Type.__name__ = "Integer32"
_AdTaTL1SSHPortNumber_Object = MibScalar
adTaTL1SSHPortNumber = _AdTaTL1SSHPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 9),
    _AdTaTL1SSHPortNumber_Type()
)
adTaTL1SSHPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaTL1SSHPortNumber.setStatus("current")


class _AdTaSecondarySSHPortNumber_Type(Integer32):
    """Custom type adTaSecondarySSHPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaSecondarySSHPortNumber_Type.__name__ = "Integer32"
_AdTaSecondarySSHPortNumber_Object = MibScalar
adTaSecondarySSHPortNumber = _AdTaSecondarySSHPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 10),
    _AdTaSecondarySSHPortNumber_Type()
)
adTaSecondarySSHPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSecondarySSHPortNumber.setStatus("current")


class _AdTaCLITelnetPortNumber_Type(Integer32):
    """Custom type adTaCLITelnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaCLITelnetPortNumber_Type.__name__ = "Integer32"
_AdTaCLITelnetPortNumber_Object = MibScalar
adTaCLITelnetPortNumber = _AdTaCLITelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 11),
    _AdTaCLITelnetPortNumber_Type()
)
adTaCLITelnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaCLITelnetPortNumber.setStatus("current")


class _AdTaCLISSHPortNumber_Type(Integer32):
    """Custom type adTaCLISSHPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_AdTaCLISSHPortNumber_Type.__name__ = "Integer32"
_AdTaCLISSHPortNumber_Object = MibScalar
adTaCLISSHPortNumber = _AdTaCLISSHPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 12),
    _AdTaCLISSHPortNumber_Type()
)
adTaCLISSHPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaCLISSHPortNumber.setStatus("current")


class _AdTaSFTPPortNumber_Type(Integer32):
    """Custom type adTaSFTPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdTaSFTPPortNumber_Type.__name__ = "Integer32"
_AdTaSFTPPortNumber_Object = MibScalar
adTaSFTPPortNumber = _AdTaSFTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 13),
    _AdTaSFTPPortNumber_Type()
)
adTaSFTPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSFTPPortNumber.setStatus("current")


class _AdTaTelnetDeadClientDetection_Type(Integer32):
    """Custom type adTaTelnetDeadClientDetection based on Integer32"""
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


_AdTaTelnetDeadClientDetection_Type.__name__ = "Integer32"
_AdTaTelnetDeadClientDetection_Object = MibScalar
adTaTelnetDeadClientDetection = _AdTaTelnetDeadClientDetection_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 17),
    _AdTaTelnetDeadClientDetection_Type()
)
adTaTelnetDeadClientDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaTelnetDeadClientDetection.setStatus("current")


class _AdTaRFC1122TCPDeadClientDetection_Type(Integer32):
    """Custom type adTaRFC1122TCPDeadClientDetection based on Integer32"""
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


_AdTaRFC1122TCPDeadClientDetection_Type.__name__ = "Integer32"
_AdTaRFC1122TCPDeadClientDetection_Object = MibScalar
adTaRFC1122TCPDeadClientDetection = _AdTaRFC1122TCPDeadClientDetection_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 20, 19),
    _AdTaRFC1122TCPDeadClientDetection_Type()
)
adTaRFC1122TCPDeadClientDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaRFC1122TCPDeadClientDetection.setStatus("current")
_AdTaIPAccessPortMgmt_ObjectIdentity = ObjectIdentity
adTaIPAccessPortMgmt = _AdTaIPAccessPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22)
)


class _AdTaSnmpIPAccess_Type(Integer32):
    """Custom type adTaSnmpIPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("sSHTunnelOnly", 3))
    )


_AdTaSnmpIPAccess_Type.__name__ = "Integer32"
_AdTaSnmpIPAccess_Object = MibScalar
adTaSnmpIPAccess = _AdTaSnmpIPAccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22, 5),
    _AdTaSnmpIPAccess_Type()
)
adTaSnmpIPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSnmpIPAccess.setStatus("current")


class _AdTaTL1IPAccess_Type(Integer32):
    """Custom type adTaTL1IPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("sSHTunnelOnly", 3))
    )


_AdTaTL1IPAccess_Type.__name__ = "Integer32"
_AdTaTL1IPAccess_Object = MibScalar
adTaTL1IPAccess = _AdTaTL1IPAccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22, 7),
    _AdTaTL1IPAccess_Type()
)
adTaTL1IPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaTL1IPAccess.setStatus("current")


class _AdTaMenuIPAccess_Type(Integer32):
    """Custom type adTaMenuIPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("sSHTunnelOnly", 3))
    )


_AdTaMenuIPAccess_Type.__name__ = "Integer32"
_AdTaMenuIPAccess_Object = MibScalar
adTaMenuIPAccess = _AdTaMenuIPAccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22, 9),
    _AdTaMenuIPAccess_Type()
)
adTaMenuIPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaMenuIPAccess.setStatus("current")


class _AdTaTerminalServerIPAccess_Type(Integer32):
    """Custom type adTaTerminalServerIPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("sSHTunnelOnly", 3))
    )


_AdTaTerminalServerIPAccess_Type.__name__ = "Integer32"
_AdTaTerminalServerIPAccess_Object = MibScalar
adTaTerminalServerIPAccess = _AdTaTerminalServerIPAccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22, 11),
    _AdTaTerminalServerIPAccess_Type()
)
adTaTerminalServerIPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaTerminalServerIPAccess.setStatus("current")


class _AdTaSSHIPAccess_Type(Integer32):
    """Custom type adTaSSHIPAccess based on Integer32"""
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


_AdTaSSHIPAccess_Type.__name__ = "Integer32"
_AdTaSSHIPAccess_Object = MibScalar
adTaSSHIPAccess = _AdTaSSHIPAccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22, 13),
    _AdTaSSHIPAccess_Type()
)
adTaSSHIPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSHIPAccess.setStatus("current")


class _AdTaSSHIPTunnelsAccess_Type(Integer32):
    """Custom type adTaSSHIPTunnelsAccess based on Integer32"""
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


_AdTaSSHIPTunnelsAccess_Type.__name__ = "Integer32"
_AdTaSSHIPTunnelsAccess_Object = MibScalar
adTaSSHIPTunnelsAccess = _AdTaSSHIPTunnelsAccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22, 15),
    _AdTaSSHIPTunnelsAccess_Type()
)
adTaSSHIPTunnelsAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSHIPTunnelsAccess.setStatus("current")


class _AdTaCLIIPAccess_Type(Integer32):
    """Custom type adTaCLIIPAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("sSHTunnelOnly", 3))
    )


_AdTaCLIIPAccess_Type.__name__ = "Integer32"
_AdTaCLIIPAccess_Object = MibScalar
adTaCLIIPAccess = _AdTaCLIIPAccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22, 17),
    _AdTaCLIIPAccess_Type()
)
adTaCLIIPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaCLIIPAccess.setStatus("current")


class _AdTaHTTPIPAccess_Type(Integer32):
    """Custom type adTaHTTPIPAccess based on Integer32"""
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


_AdTaHTTPIPAccess_Type.__name__ = "Integer32"
_AdTaHTTPIPAccess_Object = MibScalar
adTaHTTPIPAccess = _AdTaHTTPIPAccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22, 18),
    _AdTaHTTPIPAccess_Type()
)
adTaHTTPIPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaHTTPIPAccess.setStatus("current")


class _AdTaHTTPSIPAccess_Type(Integer32):
    """Custom type adTaHTTPSIPAccess based on Integer32"""
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


_AdTaHTTPSIPAccess_Type.__name__ = "Integer32"
_AdTaHTTPSIPAccess_Object = MibScalar
adTaHTTPSIPAccess = _AdTaHTTPSIPAccess_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 22, 19),
    _AdTaHTTPSIPAccess_Type()
)
adTaHTTPSIPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaHTTPSIPAccess.setStatus("current")
_AdTAeSCUAdminPort_ObjectIdentity = ObjectIdentity
adTAeSCUAdminPort = _AdTAeSCUAdminPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 24)
)


class _AdTAeSCUAdminPortMode_Type(Integer32):
    """Custom type adTAeSCUAdminPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("menus", 1),
          ("tl1", 2),
          ("tl1TestAccess", 3),
          ("terminalServer", 4),
          ("cLI", 5))
    )


_AdTAeSCUAdminPortMode_Type.__name__ = "Integer32"
_AdTAeSCUAdminPortMode_Object = MibScalar
adTAeSCUAdminPortMode = _AdTAeSCUAdminPortMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 24, 1),
    _AdTAeSCUAdminPortMode_Type()
)
adTAeSCUAdminPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAdminPortMode.setStatus("current")


class _AdTAeSCUAdminPortModeOpti_Type(Integer32):
    """Custom type adTAeSCUAdminPortModeOpti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("menus", 1),
          ("tl1", 2),
          ("terminalServer", 3))
    )


_AdTAeSCUAdminPortModeOpti_Type.__name__ = "Integer32"
_AdTAeSCUAdminPortModeOpti_Object = MibScalar
adTAeSCUAdminPortModeOpti = _AdTAeSCUAdminPortModeOpti_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 24, 2),
    _AdTAeSCUAdminPortModeOpti_Type()
)
adTAeSCUAdminPortModeOpti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAdminPortModeOpti.setStatus("current")


class _AdTAeSCUAdminPortUseRtsCts_Type(Integer32):
    """Custom type adTAeSCUAdminPortUseRtsCts based on Integer32"""
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


_AdTAeSCUAdminPortUseRtsCts_Type.__name__ = "Integer32"
_AdTAeSCUAdminPortUseRtsCts_Object = MibScalar
adTAeSCUAdminPortUseRtsCts = _AdTAeSCUAdminPortUseRtsCts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 24, 3),
    _AdTAeSCUAdminPortUseRtsCts_Type()
)
adTAeSCUAdminPortUseRtsCts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAdminPortUseRtsCts.setStatus("current")


class _AdTAeSCUAdminPortCarrierLoss_Type(Integer32):
    """Custom type adTAeSCUAdminPortCarrierLoss based on Integer32"""
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


_AdTAeSCUAdminPortCarrierLoss_Type.__name__ = "Integer32"
_AdTAeSCUAdminPortCarrierLoss_Object = MibScalar
adTAeSCUAdminPortCarrierLoss = _AdTAeSCUAdminPortCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 24, 4),
    _AdTAeSCUAdminPortCarrierLoss_Type()
)
adTAeSCUAdminPortCarrierLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAdminPortCarrierLoss.setStatus("current")


class _AdTAeSCUAdminPortDtrLogout_Type(Integer32):
    """Custom type adTAeSCUAdminPortDtrLogout based on Integer32"""
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


_AdTAeSCUAdminPortDtrLogout_Type.__name__ = "Integer32"
_AdTAeSCUAdminPortDtrLogout_Object = MibScalar
adTAeSCUAdminPortDtrLogout = _AdTAeSCUAdminPortDtrLogout_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 24, 5),
    _AdTAeSCUAdminPortDtrLogout_Type()
)
adTAeSCUAdminPortDtrLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAdminPortDtrLogout.setStatus("current")
_AdTAeSCUMuxModuleProv_ObjectIdentity = ObjectIdentity
adTAeSCUMuxModuleProv = _AdTAeSCUMuxModuleProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 16)
)
_AdTAeSCUWriteModuleProvisioning_ObjectIdentity = ObjectIdentity
adTAeSCUWriteModuleProvisioning = _AdTAeSCUWriteModuleProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 16, 7)
)


class _AdTAeSCUProvisioningSource_Type(Integer32):
    """Custom type adTAeSCUProvisioningSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdTAeSCUProvisioningSource_Type.__name__ = "Integer32"
_AdTAeSCUProvisioningSource_Object = MibScalar
adTAeSCUProvisioningSource = _AdTAeSCUProvisioningSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 16, 7, 1),
    _AdTAeSCUProvisioningSource_Type()
)
adTAeSCUProvisioningSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUProvisioningSource.setStatus("current")


class _AdTAeSCUProvDestinationSlots_Type(DisplayString):
    """Custom type adTAeSCUProvDestinationSlots based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AdTAeSCUProvDestinationSlots_Type.__name__ = "DisplayString"
_AdTAeSCUProvDestinationSlots_Object = MibScalar
adTAeSCUProvDestinationSlots = _AdTAeSCUProvDestinationSlots_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 16, 7, 3),
    _AdTAeSCUProvDestinationSlots_Type()
)
adTAeSCUProvDestinationSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUProvDestinationSlots.setStatus("current")


class _AdTAeSCUWriteProvInitiate_Type(Integer32):
    """Custom type adTAeSCUWriteProvInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiate", 1)
    )


_AdTAeSCUWriteProvInitiate_Type.__name__ = "Integer32"
_AdTAeSCUWriteProvInitiate_Object = MibScalar
adTAeSCUWriteProvInitiate = _AdTAeSCUWriteProvInitiate_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 16, 7, 4),
    _AdTAeSCUWriteProvInitiate_Type()
)
adTAeSCUWriteProvInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUWriteProvInitiate.setStatus("current")
_AdTAeSCUWriteProvStatusTable_Object = MibTable
adTAeSCUWriteProvStatusTable = _AdTAeSCUWriteProvStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 16, 7, 5)
)
if mibBuilder.loadTexts:
    adTAeSCUWriteProvStatusTable.setStatus("current")
_AdTAeSCUWriteProvStatusTableEntry_Object = MibTableRow
adTAeSCUWriteProvStatusTableEntry = _AdTAeSCUWriteProvStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 16, 7, 5, 1)
)
adTAeSCUWriteProvStatusTableEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUWriteProvStatusTableEntry.setStatus("current")


class _AdTAeSCUWriteProvInitiateStatus_Type(DisplayString):
    """Custom type adTAeSCUWriteProvInitiateStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTAeSCUWriteProvInitiateStatus_Type.__name__ = "DisplayString"
_AdTAeSCUWriteProvInitiateStatus_Object = MibTableColumn
adTAeSCUWriteProvInitiateStatus = _AdTAeSCUWriteProvInitiateStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 16, 7, 5, 1, 1),
    _AdTAeSCUWriteProvInitiateStatus_Type()
)
adTAeSCUWriteProvInitiateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUWriteProvInitiateStatus.setStatus("current")
_AdTAeSCUUserDefinableAlarm_ObjectIdentity = ObjectIdentity
adTAeSCUUserDefinableAlarm = _AdTAeSCUUserDefinableAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18)
)


class _AdTAeSCUAccModuleRemovedLevel_Type(Integer32):
    """Custom type adTAeSCUAccModuleRemovedLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTAeSCUAccModuleRemovedLevel_Type.__name__ = "Integer32"
_AdTAeSCUAccModuleRemovedLevel_Object = MibScalar
adTAeSCUAccModuleRemovedLevel = _AdTAeSCUAccModuleRemovedLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 3),
    _AdTAeSCUAccModuleRemovedLevel_Type()
)
adTAeSCUAccModuleRemovedLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAccModuleRemovedLevel.setStatus("current")


class _AdTAeSCUCraftLoginAlarmLevel_Type(Integer32):
    """Custom type adTAeSCUCraftLoginAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTAeSCUCraftLoginAlarmLevel_Type.__name__ = "Integer32"
_AdTAeSCUCraftLoginAlarmLevel_Object = MibScalar
adTAeSCUCraftLoginAlarmLevel = _AdTAeSCUCraftLoginAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 4),
    _AdTAeSCUCraftLoginAlarmLevel_Type()
)
adTAeSCUCraftLoginAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUCraftLoginAlarmLevel.setStatus("current")


class _AdTAeSCUMUXRemovedLevel_Type(Integer32):
    """Custom type adTAeSCUMUXRemovedLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTAeSCUMUXRemovedLevel_Type.__name__ = "Integer32"
_AdTAeSCUMUXRemovedLevel_Object = MibScalar
adTAeSCUMUXRemovedLevel = _AdTAeSCUMUXRemovedLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 5),
    _AdTAeSCUMUXRemovedLevel_Type()
)
adTAeSCUMUXRemovedLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUMUXRemovedLevel.setStatus("current")


class _AdTAeSCUTrapAlarmLevel_Type(Integer32):
    """Custom type adTAeSCUTrapAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTAeSCUTrapAlarmLevel_Type.__name__ = "Integer32"
_AdTAeSCUTrapAlarmLevel_Object = MibScalar
adTAeSCUTrapAlarmLevel = _AdTAeSCUTrapAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 6),
    _AdTAeSCUTrapAlarmLevel_Type()
)
adTAeSCUTrapAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUTrapAlarmLevel.setStatus("current")
_AdTAeSCUenvAlarmsTable_Object = MibTable
adTAeSCUenvAlarmsTable = _AdTAeSCUenvAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 7)
)
if mibBuilder.loadTexts:
    adTAeSCUenvAlarmsTable.setStatus("current")
_AdTAeSCUenvAlarmsTableEntry_Object = MibTableRow
adTAeSCUenvAlarmsTableEntry = _AdTAeSCUenvAlarmsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 7, 1)
)
adTAeSCUenvAlarmsTableEntry.setIndexNames(
    (0, "ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUAalarmIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUenvAlarmsTableEntry.setStatus("current")
_AdTAeSCUAalarmIndex_Type = Integer32
_AdTAeSCUAalarmIndex_Object = MibTableColumn
adTAeSCUAalarmIndex = _AdTAeSCUAalarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 7, 1, 1),
    _AdTAeSCUAalarmIndex_Type()
)
adTAeSCUAalarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUAalarmIndex.setStatus("current")
_AdTAeSCUenvAlarmDefaultName_Type = DisplayString
_AdTAeSCUenvAlarmDefaultName_Object = MibTableColumn
adTAeSCUenvAlarmDefaultName = _AdTAeSCUenvAlarmDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 7, 1, 2),
    _AdTAeSCUenvAlarmDefaultName_Type()
)
adTAeSCUenvAlarmDefaultName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUenvAlarmDefaultName.setStatus("current")


class _AdTAeSCUenvAlarmUserName_Type(DisplayString):
    """Custom type adTAeSCUenvAlarmUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AdTAeSCUenvAlarmUserName_Type.__name__ = "DisplayString"
_AdTAeSCUenvAlarmUserName_Object = MibTableColumn
adTAeSCUenvAlarmUserName = _AdTAeSCUenvAlarmUserName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 7, 1, 3),
    _AdTAeSCUenvAlarmUserName_Type()
)
adTAeSCUenvAlarmUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUenvAlarmUserName.setStatus("current")


class _AdTAeSCUenvAlarmInputLevel_Type(Integer32):
    """Custom type adTAeSCUenvAlarmInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTAeSCUenvAlarmInputLevel_Type.__name__ = "Integer32"
_AdTAeSCUenvAlarmInputLevel_Object = MibTableColumn
adTAeSCUenvAlarmInputLevel = _AdTAeSCUenvAlarmInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 7, 1, 4),
    _AdTAeSCUenvAlarmInputLevel_Type()
)
adTAeSCUenvAlarmInputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUenvAlarmInputLevel.setStatus("current")
_AdTAeSCUAIDIndex_Type = Integer32
_AdTAeSCUAIDIndex_Object = MibTableColumn
adTAeSCUAIDIndex = _AdTAeSCUAIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 7, 1, 5),
    _AdTAeSCUAIDIndex_Type()
)
adTAeSCUAIDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAIDIndex.setStatus("current")


class _AdTAeSCUConditionCode_Type(DisplayString):
    """Custom type adTAeSCUConditionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AdTAeSCUConditionCode_Type.__name__ = "DisplayString"
_AdTAeSCUConditionCode_Object = MibTableColumn
adTAeSCUConditionCode = _AdTAeSCUConditionCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 18, 7, 1, 6),
    _AdTAeSCUConditionCode_Type()
)
adTAeSCUConditionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUConditionCode.setStatus("current")
_AdTAeSCUAlarmMg_ObjectIdentity = ObjectIdentity
adTAeSCUAlarmMg = _AdTAeSCUAlarmMg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 20)
)
_AdTAeSCUAlarmEnable_Type = OctetString
_AdTAeSCUAlarmEnable_Object = MibScalar
adTAeSCUAlarmEnable = _AdTAeSCUAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 20, 1),
    _AdTAeSCUAlarmEnable_Type()
)
adTAeSCUAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAlarmEnable.setStatus("current")


class _AdTAeSCUResendAllSnmpTraps_Type(Integer32):
    """Custom type adTAeSCUResendAllSnmpTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("resendAllSnmpUnconfirmedTraps", 1),
          ("getResponse", 2),
          ("resendAllActiveAlarms", 3))
    )


_AdTAeSCUResendAllSnmpTraps_Type.__name__ = "Integer32"
_AdTAeSCUResendAllSnmpTraps_Object = MibScalar
adTAeSCUResendAllSnmpTraps = _AdTAeSCUResendAllSnmpTraps_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 20, 5),
    _AdTAeSCUResendAllSnmpTraps_Type()
)
adTAeSCUResendAllSnmpTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUResendAllSnmpTraps.setStatus("current")
_AdGenSlotExtension_ObjectIdentity = ObjectIdentity
adGenSlotExtension = _AdGenSlotExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 22)
)


class _AdGenSlotInfoStateSaveNVRAM_Type(Integer32):
    """Custom type adGenSlotInfoStateSaveNVRAM based on Integer32"""
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


_AdGenSlotInfoStateSaveNVRAM_Type.__name__ = "Integer32"
_AdGenSlotInfoStateSaveNVRAM_Object = MibScalar
adGenSlotInfoStateSaveNVRAM = _AdGenSlotInfoStateSaveNVRAM_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 22, 1),
    _AdGenSlotInfoStateSaveNVRAM_Type()
)
adGenSlotInfoStateSaveNVRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSlotInfoStateSaveNVRAM.setStatus("current")
_AdGenSlotInfoScuExtTable_Object = MibTable
adGenSlotInfoScuExtTable = _AdGenSlotInfoScuExtTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 22, 3)
)
if mibBuilder.loadTexts:
    adGenSlotInfoScuExtTable.setStatus("current")
_AdGenSlotInfoScuExtEntry_Object = MibTableRow
adGenSlotInfoScuExtEntry = _AdGenSlotInfoScuExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 22, 3, 1)
)
adGenSlotInfoScuExtEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenSlotInfoScuExtEntry.setStatus("current")
_AdGenSlotInfoStateExtension_Type = AdPresence
_AdGenSlotInfoStateExtension_Object = MibTableColumn
adGenSlotInfoStateExtension = _AdGenSlotInfoStateExtension_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 22, 3, 1, 1),
    _AdGenSlotInfoStateExtension_Type()
)
adGenSlotInfoStateExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSlotInfoStateExtension.setStatus("current")
_AdTAeFileTransferMgmt_ObjectIdentity = ObjectIdentity
adTAeFileTransferMgmt = _AdTAeFileTransferMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 24)
)


class _AdTAeSCUFileTransferMethod_Type(Integer32):
    """Custom type adTAeSCUFileTransferMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ftmTFTP", 1),
          ("ftmFTOT", 2),
          ("ftmFTP", 3),
          ("ftmSFTP", 4),
          ("ftmLFFS", 5))
    )


_AdTAeSCUFileTransferMethod_Type.__name__ = "Integer32"
_AdTAeSCUFileTransferMethod_Object = MibScalar
adTAeSCUFileTransferMethod = _AdTAeSCUFileTransferMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 24, 5),
    _AdTAeSCUFileTransferMethod_Type()
)
adTAeSCUFileTransferMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUFileTransferMethod.setStatus("current")


class _AdTAeSCUFileTransferUserID_Type(DisplayString):
    """Custom type adTAeSCUFileTransferUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeSCUFileTransferUserID_Type.__name__ = "DisplayString"
_AdTAeSCUFileTransferUserID_Object = MibScalar
adTAeSCUFileTransferUserID = _AdTAeSCUFileTransferUserID_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 24, 10),
    _AdTAeSCUFileTransferUserID_Type()
)
adTAeSCUFileTransferUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUFileTransferUserID.setStatus("current")


class _AdTAeSCUFileTransferPassword_Type(DisplayString):
    """Custom type adTAeSCUFileTransferPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeSCUFileTransferPassword_Type.__name__ = "DisplayString"
_AdTAeSCUFileTransferPassword_Object = MibScalar
adTAeSCUFileTransferPassword = _AdTAeSCUFileTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 24, 11),
    _AdTAeSCUFileTransferPassword_Type()
)
adTAeSCUFileTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUFileTransferPassword.setStatus("current")


class _AdTAeSCUFileTransferFirmwarePath_Type(DisplayString):
    """Custom type adTAeSCUFileTransferFirmwarePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeSCUFileTransferFirmwarePath_Type.__name__ = "DisplayString"
_AdTAeSCUFileTransferFirmwarePath_Object = MibScalar
adTAeSCUFileTransferFirmwarePath = _AdTAeSCUFileTransferFirmwarePath_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 24, 12),
    _AdTAeSCUFileTransferFirmwarePath_Type()
)
adTAeSCUFileTransferFirmwarePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUFileTransferFirmwarePath.setStatus("current")


class _AdTAeSCUFileTransferReceiveStatus_Type(DisplayString):
    """Custom type adTAeSCUFileTransferReceiveStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeSCUFileTransferReceiveStatus_Type.__name__ = "DisplayString"
_AdTAeSCUFileTransferReceiveStatus_Object = MibScalar
adTAeSCUFileTransferReceiveStatus = _AdTAeSCUFileTransferReceiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 24, 13),
    _AdTAeSCUFileTransferReceiveStatus_Type()
)
adTAeSCUFileTransferReceiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUFileTransferReceiveStatus.setStatus("current")


class _AdTAeSCUFileTransferSendStatus_Type(DisplayString):
    """Custom type adTAeSCUFileTransferSendStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeSCUFileTransferSendStatus_Type.__name__ = "DisplayString"
_AdTAeSCUFileTransferSendStatus_Object = MibScalar
adTAeSCUFileTransferSendStatus = _AdTAeSCUFileTransferSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 24, 14),
    _AdTAeSCUFileTransferSendStatus_Type()
)
adTAeSCUFileTransferSendStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUFileTransferSendStatus.setStatus("current")

# Managed Objects groups


# Notification objects

adTAeSCUCtrpBlownFuse = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24125)
)
adTAeSCUCtrpBlownFuse.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpBlownFuse.setStatus(
        "current"
    )

adTAeSCUCtrpCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24126)
)
adTAeSCUCtrpCardInserted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpCardInserted.setStatus(
        "current"
    )

adTAeSCUCtrpCardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24127)
)
adTAeSCUCtrpCardRemoved.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpCardRemoved.setStatus(
        "current"
    )

adTAeSCUCtrpRmtAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24128)
)
adTAeSCUCtrpRmtAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpRmtAlmClear.setStatus(
        "current"
    )

adTAeSCUCtrpRmtAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24129)
)
adTAeSCUCtrpRmtAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpRmtAlm.setStatus(
        "current"
    )

adTAeSCUCtrpExt1AlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24130)
)
adTAeSCUCtrpExt1AlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpExt1AlmClear.setStatus(
        "current"
    )

adTAeSCUCtrpExt1Alm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24131)
)
adTAeSCUCtrpExt1Alm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpExt1Alm.setStatus(
        "current"
    )

adTAeSCUCtrpExt2AlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24132)
)
adTAeSCUCtrpExt2AlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpExt2AlmClear.setStatus(
        "current"
    )

adTAeSCUCtrpExt2Alm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24133)
)
adTAeSCUCtrpExt2Alm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpExt2Alm.setStatus(
        "current"
    )

adTAeSCUCtrpBusApwrAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24134)
)
adTAeSCUCtrpBusApwrAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpBusApwrAlmClear.setStatus(
        "current"
    )

adTAeSCUCtrpBusApowerAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24135)
)
adTAeSCUCtrpBusApowerAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpBusApowerAlm.setStatus(
        "current"
    )

adTAeSCUCtrpBusBpwrAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24136)
)
adTAeSCUCtrpBusBpwrAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpBusBpwrAlmClear.setStatus(
        "current"
    )

adTAeSCUCtrpBusBpowerAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24137)
)
adTAeSCUCtrpBusBpowerAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCtrpBusBpowerAlm.setStatus(
        "current"
    )

adTAeSCUCardCommRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24138)
)
adTAeSCUCardCommRestored.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCardCommRestored.setStatus(
        "current"
    )

adTAeSCUCardCommFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24139)
)
adTAeSCUCardCommFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCardCommFail.setStatus(
        "current"
    )

adTAeSCUCraftLoginClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24164)
)
adTAeSCUCraftLoginClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCU-MIB", "adTAeSCUSecAccountUserID"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUCraftLoginAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCraftLoginClear.setStatus(
        "current"
    )

adTAeSCUCraftLoginNotfication = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24165)
)
adTAeSCUCraftLoginNotfication.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCU-MIB", "adTAeSCUSecAccountUserID"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUCraftLoginAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTAeSCUCraftLoginNotfication.setStatus(
        "current"
    )

adTASysCtrlInvalidControllerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24168)
)
adTASysCtrlInvalidControllerClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlInvalidControllerClear.setStatus(
        "current"
    )

adTASysCtrlInvalidController = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24169)
)
adTASysCtrlInvalidController.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlInvalidController.setStatus(
        "current"
    )

adTASysModuleRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24170)
)
adTASysModuleRestart.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"))
)
if mibBuilder.loadTexts:
    adTASysModuleRestart.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    **{"adTAeSCUCtrpBlownFuse": adTAeSCUCtrpBlownFuse,
       "adTAeSCUCtrpCardInserted": adTAeSCUCtrpCardInserted,
       "adTAeSCUCtrpCardRemoved": adTAeSCUCtrpCardRemoved,
       "adTAeSCUCtrpRmtAlmClear": adTAeSCUCtrpRmtAlmClear,
       "adTAeSCUCtrpRmtAlm": adTAeSCUCtrpRmtAlm,
       "adTAeSCUCtrpExt1AlmClear": adTAeSCUCtrpExt1AlmClear,
       "adTAeSCUCtrpExt1Alm": adTAeSCUCtrpExt1Alm,
       "adTAeSCUCtrpExt2AlmClear": adTAeSCUCtrpExt2AlmClear,
       "adTAeSCUCtrpExt2Alm": adTAeSCUCtrpExt2Alm,
       "adTAeSCUCtrpBusApwrAlmClear": adTAeSCUCtrpBusApwrAlmClear,
       "adTAeSCUCtrpBusApowerAlm": adTAeSCUCtrpBusApowerAlm,
       "adTAeSCUCtrpBusBpwrAlmClear": adTAeSCUCtrpBusBpwrAlmClear,
       "adTAeSCUCtrpBusBpowerAlm": adTAeSCUCtrpBusBpowerAlm,
       "adTAeSCUCardCommRestored": adTAeSCUCardCommRestored,
       "adTAeSCUCardCommFail": adTAeSCUCardCommFail,
       "adTAeSCUCraftLoginClear": adTAeSCUCraftLoginClear,
       "adTAeSCUCraftLoginNotfication": adTAeSCUCraftLoginNotfication,
       "adTASysCtrlInvalidControllerClear": adTASysCtrlInvalidControllerClear,
       "adTASysCtrlInvalidController": adTASysCtrlInvalidController,
       "adTASysModuleRestart": adTASysModuleRestart,
       "adTaIPServicePortProvMgmt": adTaIPServicePortProvMgmt,
       "adTaTL1TelnetPortNumber": adTaTL1TelnetPortNumber,
       "adTaTL1RawTCPPortNumber": adTaTL1RawTCPPortNumber,
       "adTaSecondaryTelnetPortNumber": adTaSecondaryTelnetPortNumber,
       "adTaNtwkTerminalTelnetPortNumber": adTaNtwkTerminalTelnetPortNumber,
       "adTaAdminTerminalTelnetPortNumber": adTaAdminTerminalTelnetPortNumber,
       "adTaCraftTerminalTelnetPortNumber": adTaCraftTerminalTelnetPortNumber,
       "adTaTL1SSHPortNumber": adTaTL1SSHPortNumber,
       "adTaSecondarySSHPortNumber": adTaSecondarySSHPortNumber,
       "adTaCLITelnetPortNumber": adTaCLITelnetPortNumber,
       "adTaCLISSHPortNumber": adTaCLISSHPortNumber,
       "adTaSFTPPortNumber": adTaSFTPPortNumber,
       "adTaTelnetDeadClientDetection": adTaTelnetDeadClientDetection,
       "adTaRFC1122TCPDeadClientDetection": adTaRFC1122TCPDeadClientDetection,
       "adTaIPAccessPortMgmt": adTaIPAccessPortMgmt,
       "adTaSnmpIPAccess": adTaSnmpIPAccess,
       "adTaTL1IPAccess": adTaTL1IPAccess,
       "adTaMenuIPAccess": adTaMenuIPAccess,
       "adTaTerminalServerIPAccess": adTaTerminalServerIPAccess,
       "adTaSSHIPAccess": adTaSSHIPAccess,
       "adTaSSHIPTunnelsAccess": adTaSSHIPTunnelsAccess,
       "adTaCLIIPAccess": adTaCLIIPAccess,
       "adTaHTTPIPAccess": adTaHTTPIPAccess,
       "adTaHTTPSIPAccess": adTaHTTPSIPAccess,
       "adTAeSCUAdminPort": adTAeSCUAdminPort,
       "adTAeSCUAdminPortMode": adTAeSCUAdminPortMode,
       "adTAeSCUAdminPortModeOpti": adTAeSCUAdminPortModeOpti,
       "adTAeSCUAdminPortUseRtsCts": adTAeSCUAdminPortUseRtsCts,
       "adTAeSCUAdminPortCarrierLoss": adTAeSCUAdminPortCarrierLoss,
       "adTAeSCUAdminPortDtrLogout": adTAeSCUAdminPortDtrLogout,
       "adTAeSCUMuxModuleProv": adTAeSCUMuxModuleProv,
       "adTAeSCUWriteModuleProvisioning": adTAeSCUWriteModuleProvisioning,
       "adTAeSCUProvisioningSource": adTAeSCUProvisioningSource,
       "adTAeSCUProvDestinationSlots": adTAeSCUProvDestinationSlots,
       "adTAeSCUWriteProvInitiate": adTAeSCUWriteProvInitiate,
       "adTAeSCUWriteProvStatusTable": adTAeSCUWriteProvStatusTable,
       "adTAeSCUWriteProvStatusTableEntry": adTAeSCUWriteProvStatusTableEntry,
       "adTAeSCUWriteProvInitiateStatus": adTAeSCUWriteProvInitiateStatus,
       "adTAeSCUUserDefinableAlarm": adTAeSCUUserDefinableAlarm,
       "adTAeSCUAccModuleRemovedLevel": adTAeSCUAccModuleRemovedLevel,
       "adTAeSCUCraftLoginAlarmLevel": adTAeSCUCraftLoginAlarmLevel,
       "adTAeSCUMUXRemovedLevel": adTAeSCUMUXRemovedLevel,
       "adTAeSCUTrapAlarmLevel": adTAeSCUTrapAlarmLevel,
       "adTAeSCUenvAlarmsTable": adTAeSCUenvAlarmsTable,
       "adTAeSCUenvAlarmsTableEntry": adTAeSCUenvAlarmsTableEntry,
       "adTAeSCUAalarmIndex": adTAeSCUAalarmIndex,
       "adTAeSCUenvAlarmDefaultName": adTAeSCUenvAlarmDefaultName,
       "adTAeSCUenvAlarmUserName": adTAeSCUenvAlarmUserName,
       "adTAeSCUenvAlarmInputLevel": adTAeSCUenvAlarmInputLevel,
       "adTAeSCUAIDIndex": adTAeSCUAIDIndex,
       "adTAeSCUConditionCode": adTAeSCUConditionCode,
       "adTAeSCUAlarmMg": adTAeSCUAlarmMg,
       "adTAeSCUAlarmEnable": adTAeSCUAlarmEnable,
       "adTAeSCUResendAllSnmpTraps": adTAeSCUResendAllSnmpTraps,
       "adGenSlotExtension": adGenSlotExtension,
       "adGenSlotInfoStateSaveNVRAM": adGenSlotInfoStateSaveNVRAM,
       "adGenSlotInfoScuExtTable": adGenSlotInfoScuExtTable,
       "adGenSlotInfoScuExtEntry": adGenSlotInfoScuExtEntry,
       "adGenSlotInfoStateExtension": adGenSlotInfoStateExtension,
       "adTAeFileTransferMgmt": adTAeFileTransferMgmt,
       "adTAeSCUFileTransferMethod": adTAeSCUFileTransferMethod,
       "adTAeSCUFileTransferUserID": adTAeSCUFileTransferUserID,
       "adTAeSCUFileTransferPassword": adTAeSCUFileTransferPassword,
       "adTAeSCUFileTransferFirmwarePath": adTAeSCUFileTransferFirmwarePath,
       "adTAeSCUFileTransferReceiveStatus": adTAeSCUFileTransferReceiveStatus,
       "adTAeSCUFileTransferSendStatus": adTAeSCUFileTransferSendStatus,
       "adtranTAeSCUExt1MIB": adtranTAeSCUExt1MIB}
)
