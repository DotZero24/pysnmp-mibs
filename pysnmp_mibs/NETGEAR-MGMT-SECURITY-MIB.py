# SNMP MIB module (NETGEAR-MGMT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/NETGEAR-MGMT-SECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:27:46 2025
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

(ng7000managedswitch,) = mibBuilder.importSymbols(
    "NETGEAR-REF-MIB",
    "ng7000managedswitch")

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

fastPathMgmtSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11)
)
if mibBuilder.loadTexts:
    fastPathMgmtSecurity.setRevisions(
        ("2017-07-11 00:00",
         "2017-05-18 00:00",
         "2017-03-10 00:00",
         "2013-11-11 00:00",
         "2013-08-27 00:00",
         "2011-01-26 00:00",
         "2007-05-23 00:00",
         "2003-11-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentSSLConfigGroup_ObjectIdentity = ObjectIdentity
agentSSLConfigGroup = _AgentSSLConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1)
)


class _AgentSSLAdminMode_Type(Integer32):
    """Custom type agentSSLAdminMode based on Integer32"""
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


_AgentSSLAdminMode_Type.__name__ = "Integer32"
_AgentSSLAdminMode_Object = MibScalar
agentSSLAdminMode = _AgentSSLAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1, 1),
    _AgentSSLAdminMode_Type()
)
agentSSLAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLAdminMode.setStatus("current")


class _AgentSSLSecurePort_Type(Integer32):
    """Custom type agentSSLSecurePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(443, 443),
        ValueRangeConstraint(1025, 65535),
    )


_AgentSSLSecurePort_Type.__name__ = "Integer32"
_AgentSSLSecurePort_Object = MibScalar
agentSSLSecurePort = _AgentSSLSecurePort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1, 2),
    _AgentSSLSecurePort_Type()
)
agentSSLSecurePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLSecurePort.setStatus("current")


class _AgentSSLProtocolLevel_Type(Integer32):
    """Custom type agentSSLProtocolLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ssl30", 1),
          ("tls10", 2),
          ("both", 3),
          ("tls12", 4))
    )


_AgentSSLProtocolLevel_Type.__name__ = "Integer32"
_AgentSSLProtocolLevel_Object = MibScalar
agentSSLProtocolLevel = _AgentSSLProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1, 3),
    _AgentSSLProtocolLevel_Type()
)
agentSSLProtocolLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSLProtocolLevel.setStatus("current")


class _AgentSSLMaxSessions_Type(Integer32):
    """Custom type agentSSLMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AgentSSLMaxSessions_Type.__name__ = "Integer32"
_AgentSSLMaxSessions_Object = MibScalar
agentSSLMaxSessions = _AgentSSLMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1, 4),
    _AgentSSLMaxSessions_Type()
)
agentSSLMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLMaxSessions.setStatus("current")


class _AgentSSLHardTimeout_Type(Integer32):
    """Custom type agentSSLHardTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_AgentSSLHardTimeout_Type.__name__ = "Integer32"
_AgentSSLHardTimeout_Object = MibScalar
agentSSLHardTimeout = _AgentSSLHardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1, 5),
    _AgentSSLHardTimeout_Type()
)
agentSSLHardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLHardTimeout.setStatus("current")


class _AgentSSLSoftTimeout_Type(Integer32):
    """Custom type agentSSLSoftTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AgentSSLSoftTimeout_Type.__name__ = "Integer32"
_AgentSSLSoftTimeout_Object = MibScalar
agentSSLSoftTimeout = _AgentSSLSoftTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1, 6),
    _AgentSSLSoftTimeout_Type()
)
agentSSLSoftTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLSoftTimeout.setStatus("current")
_AgentSSLCertificatePresent_Type = TruthValue
_AgentSSLCertificatePresent_Object = MibScalar
agentSSLCertificatePresent = _AgentSSLCertificatePresent_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1, 7),
    _AgentSSLCertificatePresent_Type()
)
agentSSLCertificatePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSLCertificatePresent.setStatus("current")


class _AgentSSLCertificateControl_Type(Integer32):
    """Custom type agentSSLCertificateControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("generate", 2),
          ("delete", 3))
    )


_AgentSSLCertificateControl_Type.__name__ = "Integer32"
_AgentSSLCertificateControl_Object = MibScalar
agentSSLCertificateControl = _AgentSSLCertificateControl_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1, 8),
    _AgentSSLCertificateControl_Type()
)
agentSSLCertificateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLCertificateControl.setStatus("current")
_AgentSSLCertificateGenerationStatus_Type = TruthValue
_AgentSSLCertificateGenerationStatus_Object = MibScalar
agentSSLCertificateGenerationStatus = _AgentSSLCertificateGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 1, 9),
    _AgentSSLCertificateGenerationStatus_Type()
)
agentSSLCertificateGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSLCertificateGenerationStatus.setStatus("current")
_AgentSSHConfigGroup_ObjectIdentity = ObjectIdentity
agentSSHConfigGroup = _AgentSSHConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2)
)


class _AgentSSHAdminMode_Type(Integer32):
    """Custom type agentSSHAdminMode based on Integer32"""
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


_AgentSSHAdminMode_Type.__name__ = "Integer32"
_AgentSSHAdminMode_Object = MibScalar
agentSSHAdminMode = _AgentSSHAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 1),
    _AgentSSHAdminMode_Type()
)
agentSSHAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHAdminMode.setStatus("current")


class _AgentSSHProtocolLevel_Type(Integer32):
    """Custom type agentSSHProtocolLevel based on Integer32"""
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
        *(("ssh10", 1),
          ("ssh20", 2),
          ("both", 3))
    )


_AgentSSHProtocolLevel_Type.__name__ = "Integer32"
_AgentSSHProtocolLevel_Object = MibScalar
agentSSHProtocolLevel = _AgentSSHProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 2),
    _AgentSSHProtocolLevel_Type()
)
agentSSHProtocolLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHProtocolLevel.setStatus("current")
_AgentSSHSessionsCount_Type = Integer32
_AgentSSHSessionsCount_Object = MibScalar
agentSSHSessionsCount = _AgentSSHSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 3),
    _AgentSSHSessionsCount_Type()
)
agentSSHSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHSessionsCount.setStatus("current")


class _AgentSSHMaxSessionsCount_Type(Integer32):
    """Custom type agentSSHMaxSessionsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AgentSSHMaxSessionsCount_Type.__name__ = "Integer32"
_AgentSSHMaxSessionsCount_Object = MibScalar
agentSSHMaxSessionsCount = _AgentSSHMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 4),
    _AgentSSHMaxSessionsCount_Type()
)
agentSSHMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHMaxSessionsCount.setStatus("current")


class _AgentSSHSessionTimeout_Type(Integer32):
    """Custom type agentSSHSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_AgentSSHSessionTimeout_Type.__name__ = "Integer32"
_AgentSSHSessionTimeout_Object = MibScalar
agentSSHSessionTimeout = _AgentSSHSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 5),
    _AgentSSHSessionTimeout_Type()
)
agentSSHSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHSessionTimeout.setStatus("current")


class _AgentSSHKeysPresent_Type(Integer32):
    """Custom type agentSSHKeysPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 1),
          ("rsa", 2),
          ("both", 3),
          ("none", 4))
    )


_AgentSSHKeysPresent_Type.__name__ = "Integer32"
_AgentSSHKeysPresent_Object = MibScalar
agentSSHKeysPresent = _AgentSSHKeysPresent_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 6),
    _AgentSSHKeysPresent_Type()
)
agentSSHKeysPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHKeysPresent.setStatus("current")


class _AgentSSHKeyGenerationStatus_Type(Integer32):
    """Custom type agentSSHKeyGenerationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 1),
          ("rsa", 2),
          ("both", 3),
          ("none", 4))
    )


_AgentSSHKeyGenerationStatus_Type.__name__ = "Integer32"
_AgentSSHKeyGenerationStatus_Object = MibScalar
agentSSHKeyGenerationStatus = _AgentSSHKeyGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 7),
    _AgentSSHKeyGenerationStatus_Type()
)
agentSSHKeyGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHKeyGenerationStatus.setStatus("current")


class _AgentSSHRSAKeyControl_Type(Integer32):
    """Custom type agentSSHRSAKeyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("generate", 2),
          ("delete", 3))
    )


_AgentSSHRSAKeyControl_Type.__name__ = "Integer32"
_AgentSSHRSAKeyControl_Object = MibScalar
agentSSHRSAKeyControl = _AgentSSHRSAKeyControl_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 8),
    _AgentSSHRSAKeyControl_Type()
)
agentSSHRSAKeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHRSAKeyControl.setStatus("current")


class _AgentSSHDSAKeyControl_Type(Integer32):
    """Custom type agentSSHDSAKeyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("generate", 2),
          ("delete", 3))
    )


_AgentSSHDSAKeyControl_Type.__name__ = "Integer32"
_AgentSSHDSAKeyControl_Object = MibScalar
agentSSHDSAKeyControl = _AgentSSHDSAKeyControl_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 9),
    _AgentSSHDSAKeyControl_Type()
)
agentSSHDSAKeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHDSAKeyControl.setStatus("current")


class _AgentSSHMgmtPortNum_Type(Integer32):
    """Custom type agentSSHMgmtPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSSHMgmtPortNum_Type.__name__ = "Integer32"
_AgentSSHMgmtPortNum_Object = MibScalar
agentSSHMgmtPortNum = _AgentSSHMgmtPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 10),
    _AgentSSHMgmtPortNum_Type()
)
agentSSHMgmtPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHMgmtPortNum.setStatus("current")


class _AgentScpServerAdminMode_Type(Integer32):
    """Custom type agentScpServerAdminMode based on Integer32"""
    defaultValue = 2

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


_AgentScpServerAdminMode_Type.__name__ = "Integer32"
_AgentScpServerAdminMode_Object = MibScalar
agentScpServerAdminMode = _AgentScpServerAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 2, 11),
    _AgentScpServerAdminMode_Type()
)
agentScpServerAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentScpServerAdminMode.setStatus("current")
_AgentListAuthenticationGroup_ObjectIdentity = ObjectIdentity
agentListAuthenticationGroup = _AgentListAuthenticationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3)
)
_AgentListAuthenticationTable_Object = MibTable
agentListAuthenticationTable = _AgentListAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 1)
)
if mibBuilder.loadTexts:
    agentListAuthenticationTable.setStatus("current")
_AgentListAuthenticationEntry_Object = MibTableRow
agentListAuthenticationEntry = _AgentListAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 1, 1)
)
agentListAuthenticationEntry.setIndexNames(
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAuthenticationAccessLevel"),
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAuthenticationIndex"),
)
if mibBuilder.loadTexts:
    agentListAuthenticationEntry.setStatus("current")


class _AgentListAuthenticationAccessLevel_Type(Integer32):
    """Custom type agentListAuthenticationAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("login", 0),
          ("enable", 1))
    )


_AgentListAuthenticationAccessLevel_Type.__name__ = "Integer32"
_AgentListAuthenticationAccessLevel_Object = MibTableColumn
agentListAuthenticationAccessLevel = _AgentListAuthenticationAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 1, 1, 1),
    _AgentListAuthenticationAccessLevel_Type()
)
agentListAuthenticationAccessLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentListAuthenticationAccessLevel.setStatus("current")
_AgentListAuthenticationIndex_Type = Unsigned32
_AgentListAuthenticationIndex_Object = MibTableColumn
agentListAuthenticationIndex = _AgentListAuthenticationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 1, 1, 2),
    _AgentListAuthenticationIndex_Type()
)
agentListAuthenticationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentListAuthenticationIndex.setStatus("current")


class _AgentListAuthenticationName_Type(DisplayString):
    """Custom type agentListAuthenticationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentListAuthenticationName_Type.__name__ = "DisplayString"
_AgentListAuthenticationName_Object = MibTableColumn
agentListAuthenticationName = _AgentListAuthenticationName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 1, 1, 3),
    _AgentListAuthenticationName_Type()
)
agentListAuthenticationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAuthenticationName.setStatus("current")


class _AgentListAuthenticationAccessLine_Type(Bits):
    """Custom type agentListAuthenticationAccessLine based on Bits"""
    namedValues = NamedValues(
        *(("undefined", 0),
          ("console", 1),
          ("telnet", 2),
          ("ssh", 3))
    )

_AgentListAuthenticationAccessLine_Type.__name__ = "Bits"
_AgentListAuthenticationAccessLine_Object = MibTableColumn
agentListAuthenticationAccessLine = _AgentListAuthenticationAccessLine_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 1, 1, 4),
    _AgentListAuthenticationAccessLine_Type()
)
agentListAuthenticationAccessLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAuthenticationAccessLine.setStatus("current")
_AgentListAuthenticationRowStatus_Type = RowStatus
_AgentListAuthenticationRowStatus_Object = MibTableColumn
agentListAuthenticationRowStatus = _AgentListAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 1, 1, 5),
    _AgentListAuthenticationRowStatus_Type()
)
agentListAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAuthenticationRowStatus.setStatus("current")
_AgentListAuthenticationMethodsGroup_ObjectIdentity = ObjectIdentity
agentListAuthenticationMethodsGroup = _AgentListAuthenticationMethodsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 2)
)
_AgentListAuthenticationMethodsTable_Object = MibTable
agentListAuthenticationMethodsTable = _AgentListAuthenticationMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 2, 1)
)
if mibBuilder.loadTexts:
    agentListAuthenticationMethodsTable.setStatus("current")
_AgentListAuthenticationMethodsEntry_Object = MibTableRow
agentListAuthenticationMethodsEntry = _AgentListAuthenticationMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 2, 1, 1)
)
agentListAuthenticationMethodsEntry.setIndexNames(
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAuthenticationAccessLevel"),
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAuthenticationIndex"),
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAuthenticationMethodsIndex"),
)
if mibBuilder.loadTexts:
    agentListAuthenticationMethodsEntry.setStatus("current")
_AgentListAuthenticationMethodsIndex_Type = Unsigned32
_AgentListAuthenticationMethodsIndex_Object = MibTableColumn
agentListAuthenticationMethodsIndex = _AgentListAuthenticationMethodsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 2, 1, 1, 1),
    _AgentListAuthenticationMethodsIndex_Type()
)
agentListAuthenticationMethodsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentListAuthenticationMethodsIndex.setStatus("current")


class _AgentListAuthenticationMethodsValue_Type(Integer32):
    """Custom type agentListAuthenticationMethodsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("enable", 1),
          ("line", 2),
          ("local", 3),
          ("none", 4),
          ("radius", 5),
          ("tacacs", 6),
          ("deny", 7))
    )


_AgentListAuthenticationMethodsValue_Type.__name__ = "Integer32"
_AgentListAuthenticationMethodsValue_Object = MibTableColumn
agentListAuthenticationMethodsValue = _AgentListAuthenticationMethodsValue_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 3, 2, 1, 1, 2),
    _AgentListAuthenticationMethodsValue_Type()
)
agentListAuthenticationMethodsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAuthenticationMethodsValue.setStatus("current")
_AgentListAutorizationGroup_ObjectIdentity = ObjectIdentity
agentListAutorizationGroup = _AgentListAutorizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4)
)
_AgentListAutorizationTable_Object = MibTable
agentListAutorizationTable = _AgentListAutorizationTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 1)
)
if mibBuilder.loadTexts:
    agentListAutorizationTable.setStatus("current")
_AgentListAutorizationEntry_Object = MibTableRow
agentListAutorizationEntry = _AgentListAutorizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 1, 1)
)
agentListAutorizationEntry.setIndexNames(
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAutorizationType"),
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAutorizationIndex"),
)
if mibBuilder.loadTexts:
    agentListAutorizationEntry.setStatus("current")


class _AgentListAutorizationType_Type(Integer32):
    """Custom type agentListAutorizationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("command", 0),
          ("exec", 1))
    )


_AgentListAutorizationType_Type.__name__ = "Integer32"
_AgentListAutorizationType_Object = MibTableColumn
agentListAutorizationType = _AgentListAutorizationType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 1, 1, 1),
    _AgentListAutorizationType_Type()
)
agentListAutorizationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentListAutorizationType.setStatus("current")
_AgentListAutorizationIndex_Type = Unsigned32
_AgentListAutorizationIndex_Object = MibTableColumn
agentListAutorizationIndex = _AgentListAutorizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 1, 1, 2),
    _AgentListAutorizationIndex_Type()
)
agentListAutorizationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentListAutorizationIndex.setStatus("current")


class _AgentListAutorizationName_Type(DisplayString):
    """Custom type agentListAutorizationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AgentListAutorizationName_Type.__name__ = "DisplayString"
_AgentListAutorizationName_Object = MibTableColumn
agentListAutorizationName = _AgentListAutorizationName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 1, 1, 3),
    _AgentListAutorizationName_Type()
)
agentListAutorizationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAutorizationName.setStatus("current")


class _AgentListAutorizationAccessLine_Type(Bits):
    """Custom type agentListAutorizationAccessLine based on Bits"""
    namedValues = NamedValues(
        *(("undefined", 0),
          ("console", 1),
          ("telnet", 2),
          ("ssh", 3))
    )

_AgentListAutorizationAccessLine_Type.__name__ = "Bits"
_AgentListAutorizationAccessLine_Object = MibTableColumn
agentListAutorizationAccessLine = _AgentListAutorizationAccessLine_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 1, 1, 4),
    _AgentListAutorizationAccessLine_Type()
)
agentListAutorizationAccessLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAutorizationAccessLine.setStatus("current")
_AgentListAutorizationRowStatus_Type = RowStatus
_AgentListAutorizationRowStatus_Object = MibTableColumn
agentListAutorizationRowStatus = _AgentListAutorizationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 1, 1, 5),
    _AgentListAutorizationRowStatus_Type()
)
agentListAutorizationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAutorizationRowStatus.setStatus("current")
_AgentListAutorizationMethodsGroup_ObjectIdentity = ObjectIdentity
agentListAutorizationMethodsGroup = _AgentListAutorizationMethodsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 2)
)
_AgentListAutorizationMethodsTable_Object = MibTable
agentListAutorizationMethodsTable = _AgentListAutorizationMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 2, 1)
)
if mibBuilder.loadTexts:
    agentListAutorizationMethodsTable.setStatus("current")
_AgentListAutorizationMethodsEntry_Object = MibTableRow
agentListAutorizationMethodsEntry = _AgentListAutorizationMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 2, 1, 1)
)
agentListAutorizationMethodsEntry.setIndexNames(
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAutorizationType"),
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAutorizationIndex"),
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAutorizationMethodsIndex"),
)
if mibBuilder.loadTexts:
    agentListAutorizationMethodsEntry.setStatus("current")
_AgentListAutorizationMethodsIndex_Type = Unsigned32
_AgentListAutorizationMethodsIndex_Object = MibTableColumn
agentListAutorizationMethodsIndex = _AgentListAutorizationMethodsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 2, 1, 1, 1),
    _AgentListAutorizationMethodsIndex_Type()
)
agentListAutorizationMethodsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentListAutorizationMethodsIndex.setStatus("current")


class _AgentListAutorizationMethodsValue_Type(Integer32):
    """Custom type agentListAutorizationMethodsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("tacacs", 1),
          ("radius", 2),
          ("local", 3),
          ("none", 4))
    )


_AgentListAutorizationMethodsValue_Type.__name__ = "Integer32"
_AgentListAutorizationMethodsValue_Object = MibTableColumn
agentListAutorizationMethodsValue = _AgentListAutorizationMethodsValue_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 4, 2, 1, 1, 2),
    _AgentListAutorizationMethodsValue_Type()
)
agentListAutorizationMethodsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAutorizationMethodsValue.setStatus("current")
_AgentListAccountingGroup_ObjectIdentity = ObjectIdentity
agentListAccountingGroup = _AgentListAccountingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5)
)
_AgentListAccountingTable_Object = MibTable
agentListAccountingTable = _AgentListAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 1)
)
if mibBuilder.loadTexts:
    agentListAccountingTable.setStatus("current")
_AgentListAccountingEntry_Object = MibTableRow
agentListAccountingEntry = _AgentListAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 1, 1)
)
agentListAccountingEntry.setIndexNames(
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAccountingType"),
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAccountingIndex"),
)
if mibBuilder.loadTexts:
    agentListAccountingEntry.setStatus("current")


class _AgentListAccountingType_Type(Integer32):
    """Custom type agentListAccountingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("command", 0),
          ("exec", 1))
    )


_AgentListAccountingType_Type.__name__ = "Integer32"
_AgentListAccountingType_Object = MibTableColumn
agentListAccountingType = _AgentListAccountingType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 1, 1, 1),
    _AgentListAccountingType_Type()
)
agentListAccountingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentListAccountingType.setStatus("current")
_AgentListAccountingIndex_Type = Unsigned32
_AgentListAccountingIndex_Object = MibTableColumn
agentListAccountingIndex = _AgentListAccountingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 1, 1, 2),
    _AgentListAccountingIndex_Type()
)
agentListAccountingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentListAccountingIndex.setStatus("current")


class _AgentListAccountingName_Type(DisplayString):
    """Custom type agentListAccountingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AgentListAccountingName_Type.__name__ = "DisplayString"
_AgentListAccountingName_Object = MibTableColumn
agentListAccountingName = _AgentListAccountingName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 1, 1, 3),
    _AgentListAccountingName_Type()
)
agentListAccountingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAccountingName.setStatus("current")


class _AgentListAccountingRecordType_Type(Integer32):
    """Custom type agentListAccountingRecordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("start-stop", 1),
          ("stop-only", 2),
          ("none", 3))
    )


_AgentListAccountingRecordType_Type.__name__ = "Integer32"
_AgentListAccountingRecordType_Object = MibTableColumn
agentListAccountingRecordType = _AgentListAccountingRecordType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 1, 1, 4),
    _AgentListAccountingRecordType_Type()
)
agentListAccountingRecordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAccountingRecordType.setStatus("current")


class _AgentListAccountingAccessLine_Type(Bits):
    """Custom type agentListAccountingAccessLine based on Bits"""
    namedValues = NamedValues(
        *(("undefined", 0),
          ("console", 1),
          ("telnet", 2),
          ("ssh", 3))
    )

_AgentListAccountingAccessLine_Type.__name__ = "Bits"
_AgentListAccountingAccessLine_Object = MibTableColumn
agentListAccountingAccessLine = _AgentListAccountingAccessLine_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 1, 1, 5),
    _AgentListAccountingAccessLine_Type()
)
agentListAccountingAccessLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAccountingAccessLine.setStatus("current")
_AgentListAccountingRowStatus_Type = RowStatus
_AgentListAccountingRowStatus_Object = MibTableColumn
agentListAccountingRowStatus = _AgentListAccountingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 1, 1, 6),
    _AgentListAccountingRowStatus_Type()
)
agentListAccountingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAccountingRowStatus.setStatus("current")
_AgentListAccountingMethodsGroup_ObjectIdentity = ObjectIdentity
agentListAccountingMethodsGroup = _AgentListAccountingMethodsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 2)
)
_AgentListAccountingMethodsTable_Object = MibTable
agentListAccountingMethodsTable = _AgentListAccountingMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 2, 1)
)
if mibBuilder.loadTexts:
    agentListAccountingMethodsTable.setStatus("current")
_AgentListAccountingMethodsEntry_Object = MibTableRow
agentListAccountingMethodsEntry = _AgentListAccountingMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 2, 1, 1)
)
agentListAccountingMethodsEntry.setIndexNames(
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAccountingType"),
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAccountingIndex"),
    (0, "NETGEAR-MGMT-SECURITY-MIB", "agentListAccountingMethodsIndex"),
)
if mibBuilder.loadTexts:
    agentListAccountingMethodsEntry.setStatus("current")
_AgentListAccountingMethodsIndex_Type = Unsigned32
_AgentListAccountingMethodsIndex_Object = MibTableColumn
agentListAccountingMethodsIndex = _AgentListAccountingMethodsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 2, 1, 1, 1),
    _AgentListAccountingMethodsIndex_Type()
)
agentListAccountingMethodsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentListAccountingMethodsIndex.setStatus("current")


class _AgentListAccountingMethodsValue_Type(Integer32):
    """Custom type agentListAccountingMethodsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("tacacs", 1),
          ("radius", 2))
    )


_AgentListAccountingMethodsValue_Type.__name__ = "Integer32"
_AgentListAccountingMethodsValue_Object = MibTableColumn
agentListAccountingMethodsValue = _AgentListAccountingMethodsValue_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 2, 1, 1, 2),
    _AgentListAccountingMethodsValue_Type()
)
agentListAccountingMethodsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentListAccountingMethodsValue.setStatus("current")
_AgentAccountingUpdateConfigGroup_ObjectIdentity = ObjectIdentity
agentAccountingUpdateConfigGroup = _AgentAccountingUpdateConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 3)
)


class _AgentAccountingUpdateNewinfo_Type(Integer32):
    """Custom type agentAccountingUpdateNewinfo based on Integer32"""
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


_AgentAccountingUpdateNewinfo_Type.__name__ = "Integer32"
_AgentAccountingUpdateNewinfo_Object = MibScalar
agentAccountingUpdateNewinfo = _AgentAccountingUpdateNewinfo_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 3, 1),
    _AgentAccountingUpdateNewinfo_Type()
)
agentAccountingUpdateNewinfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAccountingUpdateNewinfo.setStatus("current")


class _AgentAccountingUpdatePeriodic_Type(Integer32):
    """Custom type agentAccountingUpdatePeriodic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_AgentAccountingUpdatePeriodic_Type.__name__ = "Integer32"
_AgentAccountingUpdatePeriodic_Object = MibScalar
agentAccountingUpdatePeriodic = _AgentAccountingUpdatePeriodic_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 11, 5, 3, 2),
    _AgentAccountingUpdatePeriodic_Type()
)
agentAccountingUpdatePeriodic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAccountingUpdatePeriodic.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETGEAR-MGMT-SECURITY-MIB",
    **{"fastPathMgmtSecurity": fastPathMgmtSecurity,
       "agentSSLConfigGroup": agentSSLConfigGroup,
       "agentSSLAdminMode": agentSSLAdminMode,
       "agentSSLSecurePort": agentSSLSecurePort,
       "agentSSLProtocolLevel": agentSSLProtocolLevel,
       "agentSSLMaxSessions": agentSSLMaxSessions,
       "agentSSLHardTimeout": agentSSLHardTimeout,
       "agentSSLSoftTimeout": agentSSLSoftTimeout,
       "agentSSLCertificatePresent": agentSSLCertificatePresent,
       "agentSSLCertificateControl": agentSSLCertificateControl,
       "agentSSLCertificateGenerationStatus": agentSSLCertificateGenerationStatus,
       "agentSSHConfigGroup": agentSSHConfigGroup,
       "agentSSHAdminMode": agentSSHAdminMode,
       "agentSSHProtocolLevel": agentSSHProtocolLevel,
       "agentSSHSessionsCount": agentSSHSessionsCount,
       "agentSSHMaxSessionsCount": agentSSHMaxSessionsCount,
       "agentSSHSessionTimeout": agentSSHSessionTimeout,
       "agentSSHKeysPresent": agentSSHKeysPresent,
       "agentSSHKeyGenerationStatus": agentSSHKeyGenerationStatus,
       "agentSSHRSAKeyControl": agentSSHRSAKeyControl,
       "agentSSHDSAKeyControl": agentSSHDSAKeyControl,
       "agentSSHMgmtPortNum": agentSSHMgmtPortNum,
       "agentScpServerAdminMode": agentScpServerAdminMode,
       "agentListAuthenticationGroup": agentListAuthenticationGroup,
       "agentListAuthenticationTable": agentListAuthenticationTable,
       "agentListAuthenticationEntry": agentListAuthenticationEntry,
       "agentListAuthenticationAccessLevel": agentListAuthenticationAccessLevel,
       "agentListAuthenticationIndex": agentListAuthenticationIndex,
       "agentListAuthenticationName": agentListAuthenticationName,
       "agentListAuthenticationAccessLine": agentListAuthenticationAccessLine,
       "agentListAuthenticationRowStatus": agentListAuthenticationRowStatus,
       "agentListAuthenticationMethodsGroup": agentListAuthenticationMethodsGroup,
       "agentListAuthenticationMethodsTable": agentListAuthenticationMethodsTable,
       "agentListAuthenticationMethodsEntry": agentListAuthenticationMethodsEntry,
       "agentListAuthenticationMethodsIndex": agentListAuthenticationMethodsIndex,
       "agentListAuthenticationMethodsValue": agentListAuthenticationMethodsValue,
       "agentListAutorizationGroup": agentListAutorizationGroup,
       "agentListAutorizationTable": agentListAutorizationTable,
       "agentListAutorizationEntry": agentListAutorizationEntry,
       "agentListAutorizationType": agentListAutorizationType,
       "agentListAutorizationIndex": agentListAutorizationIndex,
       "agentListAutorizationName": agentListAutorizationName,
       "agentListAutorizationAccessLine": agentListAutorizationAccessLine,
       "agentListAutorizationRowStatus": agentListAutorizationRowStatus,
       "agentListAutorizationMethodsGroup": agentListAutorizationMethodsGroup,
       "agentListAutorizationMethodsTable": agentListAutorizationMethodsTable,
       "agentListAutorizationMethodsEntry": agentListAutorizationMethodsEntry,
       "agentListAutorizationMethodsIndex": agentListAutorizationMethodsIndex,
       "agentListAutorizationMethodsValue": agentListAutorizationMethodsValue,
       "agentListAccountingGroup": agentListAccountingGroup,
       "agentListAccountingTable": agentListAccountingTable,
       "agentListAccountingEntry": agentListAccountingEntry,
       "agentListAccountingType": agentListAccountingType,
       "agentListAccountingIndex": agentListAccountingIndex,
       "agentListAccountingName": agentListAccountingName,
       "agentListAccountingRecordType": agentListAccountingRecordType,
       "agentListAccountingAccessLine": agentListAccountingAccessLine,
       "agentListAccountingRowStatus": agentListAccountingRowStatus,
       "agentListAccountingMethodsGroup": agentListAccountingMethodsGroup,
       "agentListAccountingMethodsTable": agentListAccountingMethodsTable,
       "agentListAccountingMethodsEntry": agentListAccountingMethodsEntry,
       "agentListAccountingMethodsIndex": agentListAccountingMethodsIndex,
       "agentListAccountingMethodsValue": agentListAccountingMethodsValue,
       "agentAccountingUpdateConfigGroup": agentAccountingUpdateConfigGroup,
       "agentAccountingUpdateNewinfo": agentAccountingUpdateNewinfo,
       "agentAccountingUpdatePeriodic": agentAccountingUpdatePeriodic}
)
