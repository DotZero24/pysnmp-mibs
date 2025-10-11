# SNMP MIB module (RUGGEDCOM-PTP1588-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-PTP1588-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:26 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(ruggedcomMgmt,) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rcPTP1588 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12)
)
if mibBuilder.loadTexts:
    rcPTP1588.setRevisions(
        ("2015-09-23 13:00",
         "2022-06-17 13:00",
         "2022-07-20 12:15",
         "2022-07-25 10:00",
         "2023-05-01 17:00",
         "2023-07-07 16:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcPTP1588Base_ObjectIdentity = ObjectIdentity
rcPTP1588Base = _RcPTP1588Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1)
)


class _RcPTP1588ClkType_Type(Integer32):
    """Custom type rcPTP1588ClkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ordinaryClock", 2),
          ("p2ptc", 3),
          ("boundaryClock", 4),
          ("e2etc", 5),
          ("ocp2ptc", 6),
          ("oce2etc", 7),
          ("transparentClock", 8),
          ("ocAndTc", 9))
    )


_RcPTP1588ClkType_Type.__name__ = "Integer32"
_RcPTP1588ClkType_Object = MibScalar
rcPTP1588ClkType = _RcPTP1588ClkType_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 1),
    _RcPTP1588ClkType_Type()
)
rcPTP1588ClkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkType.setStatus("current")
_RcPTP1588EthPorts_Type = PortList
_RcPTP1588EthPorts_Object = MibScalar
rcPTP1588EthPorts = _RcPTP1588EthPorts_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 2),
    _RcPTP1588EthPorts_Type()
)
rcPTP1588EthPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588EthPorts.setStatus("current")


class _RcPTP1588StartUpWait_Type(Integer32):
    """Custom type rcPTP1588StartUpWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RcPTP1588StartUpWait_Type.__name__ = "Integer32"
_RcPTP1588StartUpWait_Object = MibScalar
rcPTP1588StartUpWait = _RcPTP1588StartUpWait_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 3),
    _RcPTP1588StartUpWait_Type()
)
rcPTP1588StartUpWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588StartUpWait.setStatus("current")


class _RcPTP1588NetClass_Type(Integer32):
    """Custom type rcPTP1588NetClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("netclass1588", 1),
          ("nonnetclass1588", 2))
    )


_RcPTP1588NetClass_Type.__name__ = "Integer32"
_RcPTP1588NetClass_Object = MibScalar
rcPTP1588NetClass = _RcPTP1588NetClass_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 4),
    _RcPTP1588NetClass_Type()
)
rcPTP1588NetClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588NetClass.setStatus("current")
_RcPTP1588SlaveEthPort_Type = PortList
_RcPTP1588SlaveEthPort_Object = MibScalar
rcPTP1588SlaveEthPort = _RcPTP1588SlaveEthPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 5),
    _RcPTP1588SlaveEthPort_Type()
)
rcPTP1588SlaveEthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588SlaveEthPort.setStatus("current")


class _RcPTP1588SlaveDomain_Type(Integer32):
    """Custom type rcPTP1588SlaveDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RcPTP1588SlaveDomain_Type.__name__ = "Integer32"
_RcPTP1588SlaveDomain_Object = MibScalar
rcPTP1588SlaveDomain = _RcPTP1588SlaveDomain_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 6),
    _RcPTP1588SlaveDomain_Type()
)
rcPTP1588SlaveDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588SlaveDomain.setStatus("current")
_RcPTP1588SlaveAutoReg_Type = TruthValue
_RcPTP1588SlaveAutoReg_Object = MibScalar
rcPTP1588SlaveAutoReg = _RcPTP1588SlaveAutoReg_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 7),
    _RcPTP1588SlaveAutoReg_Type()
)
rcPTP1588SlaveAutoReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588SlaveAutoReg.setStatus("current")
_RcPTP1588SlaveMasteIP_Type = IpAddress
_RcPTP1588SlaveMasteIP_Object = MibScalar
rcPTP1588SlaveMasteIP = _RcPTP1588SlaveMasteIP_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 8),
    _RcPTP1588SlaveMasteIP_Type()
)
rcPTP1588SlaveMasteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588SlaveMasteIP.setStatus("current")
_RcPTP1588SlaveBackUpIP_Type = IpAddress
_RcPTP1588SlaveBackUpIP_Object = MibScalar
rcPTP1588SlaveBackUpIP = _RcPTP1588SlaveBackUpIP_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 9),
    _RcPTP1588SlaveBackUpIP_Type()
)
rcPTP1588SlaveBackUpIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588SlaveBackUpIP.setStatus("current")
_RcPTP1588ServoStatus_Type = DisplayString
_RcPTP1588ServoStatus_Object = MibScalar
rcPTP1588ServoStatus = _RcPTP1588ServoStatus_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 10),
    _RcPTP1588ServoStatus_Type()
)
rcPTP1588ServoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPTP1588ServoStatus.setStatus("current")
_RcPTP1588SlaveFeqAdj_Type = Integer32
_RcPTP1588SlaveFeqAdj_Object = MibScalar
rcPTP1588SlaveFeqAdj = _RcPTP1588SlaveFeqAdj_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 11),
    _RcPTP1588SlaveFeqAdj_Type()
)
rcPTP1588SlaveFeqAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPTP1588SlaveFeqAdj.setStatus("current")
_RcPTP1588E2EDelay_Type = Integer32
_RcPTP1588E2EDelay_Object = MibScalar
rcPTP1588E2EDelay = _RcPTP1588E2EDelay_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 12),
    _RcPTP1588E2EDelay_Type()
)
rcPTP1588E2EDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPTP1588E2EDelay.setStatus("current")


class _RcPTP1588GlobalEnable_Type(TruthValue):
    """Custom type rcPTP1588GlobalEnable based on TruthValue"""
    defaultValue = 2


_RcPTP1588GlobalEnable_Type.__name__ = "TruthValue"
_RcPTP1588GlobalEnable_Object = MibScalar
rcPTP1588GlobalEnable = _RcPTP1588GlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 13),
    _RcPTP1588GlobalEnable_Type()
)
rcPTP1588GlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588GlobalEnable.setStatus("current")


class _RcPTP1588GlobalP2PRequestInterval_Type(Integer32):
    """Custom type rcPTP1588GlobalP2PRequestInterval based on Integer32"""
    defaultValue = 1

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
        *(("value1Sec", 1),
          ("value2Sec", 2),
          ("value4Sec", 3),
          ("value8Sec", 4),
          ("value16Sec", 5),
          ("value32Sec", 6))
    )


_RcPTP1588GlobalP2PRequestInterval_Type.__name__ = "Integer32"
_RcPTP1588GlobalP2PRequestInterval_Object = MibScalar
rcPTP1588GlobalP2PRequestInterval = _RcPTP1588GlobalP2PRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 14),
    _RcPTP1588GlobalP2PRequestInterval_Type()
)
rcPTP1588GlobalP2PRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588GlobalP2PRequestInterval.setStatus("current")


class _RcPTP1588GlobalE2ERequestInterval_Type(Integer32):
    """Custom type rcPTP1588GlobalE2ERequestInterval based on Integer32"""
    defaultValue = 1

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
        *(("value1Sec", 1),
          ("value2Sec", 2),
          ("value4Sec", 3),
          ("value8Sec", 4),
          ("value16Sec", 5),
          ("value32Sec", 6))
    )


_RcPTP1588GlobalE2ERequestInterval_Type.__name__ = "Integer32"
_RcPTP1588GlobalE2ERequestInterval_Object = MibScalar
rcPTP1588GlobalE2ERequestInterval = _RcPTP1588GlobalE2ERequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 15),
    _RcPTP1588GlobalE2ERequestInterval_Type()
)
rcPTP1588GlobalE2ERequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588GlobalE2ERequestInterval.setStatus("current")


class _RcPTP1588Global1Step_Type(TruthValue):
    """Custom type rcPTP1588Global1Step based on TruthValue"""
    defaultValue = 2


_RcPTP1588Global1Step_Type.__name__ = "TruthValue"
_RcPTP1588Global1Step_Object = MibScalar
rcPTP1588Global1Step = _RcPTP1588Global1Step_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 16),
    _RcPTP1588Global1Step_Type()
)
rcPTP1588Global1Step.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588Global1Step.setStatus("current")


class _RcPTP1588ClkAnnounceInt_Type(Integer32):
    """Custom type rcPTP1588ClkAnnounceInt based on Integer32"""
    defaultValue = 1

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
        *(("value1Sec", 1),
          ("value2Sec", 2),
          ("value4Sec", 3),
          ("value8Sec", 4),
          ("value16Sec", 5),
          ("value32Sec", 6))
    )


_RcPTP1588ClkAnnounceInt_Type.__name__ = "Integer32"
_RcPTP1588ClkAnnounceInt_Object = MibScalar
rcPTP1588ClkAnnounceInt = _RcPTP1588ClkAnnounceInt_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 17),
    _RcPTP1588ClkAnnounceInt_Type()
)
rcPTP1588ClkAnnounceInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkAnnounceInt.setStatus("current")


class _RcPTP1588ClkAnnounceRcTout_Type(Integer32):
    """Custom type rcPTP1588ClkAnnounceRcTout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_RcPTP1588ClkAnnounceRcTout_Type.__name__ = "Integer32"
_RcPTP1588ClkAnnounceRcTout_Object = MibScalar
rcPTP1588ClkAnnounceRcTout = _RcPTP1588ClkAnnounceRcTout_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 18),
    _RcPTP1588ClkAnnounceRcTout_Type()
)
rcPTP1588ClkAnnounceRcTout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkAnnounceRcTout.setStatus("current")


class _RcPTP1588ClkSyncInt_Type(Integer32):
    """Custom type rcPTP1588ClkSyncInt based on Integer32"""
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
        *(("value125millSec", 1),
          ("value250millSec", 2),
          ("value500millSec", 3),
          ("value1Sec", 4),
          ("value2Sec", 5))
    )


_RcPTP1588ClkSyncInt_Type.__name__ = "Integer32"
_RcPTP1588ClkSyncInt_Object = MibScalar
rcPTP1588ClkSyncInt = _RcPTP1588ClkSyncInt_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 19),
    _RcPTP1588ClkSyncInt_Type()
)
rcPTP1588ClkSyncInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkSyncInt.setStatus("current")


class _RcPTP1588ClkDelayMech_Type(Integer32):
    """Custom type rcPTP1588ClkDelayMech based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 1),
          ("p2p", 2),
          ("disabled", 254))
    )


_RcPTP1588ClkDelayMech_Type.__name__ = "Integer32"
_RcPTP1588ClkDelayMech_Object = MibScalar
rcPTP1588ClkDelayMech = _RcPTP1588ClkDelayMech_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 20),
    _RcPTP1588ClkDelayMech_Type()
)
rcPTP1588ClkDelayMech.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkDelayMech.setStatus("current")


class _RcPTP1588ClkProfileId_Type(Integer32):
    """Custom type rcPTP1588ClkProfileId based on Integer32"""
    defaultValue = 1

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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("defaultP2PProfile", 0),
          ("powerProfile", 1),
          ("ieee8021as", 2),
          ("lxi", 3),
          ("telecom", 4),
          ("utilityProfile", 5),
          ("defaultE2EProfile", 6),
          ("customProfile", 7),
          ("powerProfileV2", 8))
    )


_RcPTP1588ClkProfileId_Type.__name__ = "Integer32"
_RcPTP1588ClkProfileId_Object = MibScalar
rcPTP1588ClkProfileId = _RcPTP1588ClkProfileId_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 21),
    _RcPTP1588ClkProfileId_Type()
)
rcPTP1588ClkProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkProfileId.setStatus("current")


class _RcPTP1588ClkDomainNumber_Type(Unsigned32):
    """Custom type rcPTP1588ClkDomainNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_RcPTP1588ClkDomainNumber_Type.__name__ = "Unsigned32"
_RcPTP1588ClkDomainNumber_Object = MibScalar
rcPTP1588ClkDomainNumber = _RcPTP1588ClkDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 22),
    _RcPTP1588ClkDomainNumber_Type()
)
rcPTP1588ClkDomainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkDomainNumber.setStatus("current")


class _RcPTP1588ClkNetProtocol_Type(Integer32):
    """Custom type rcPTP1588ClkNetProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee8023", 1),
          ("udpIpv4", 2))
    )


_RcPTP1588ClkNetProtocol_Type.__name__ = "Integer32"
_RcPTP1588ClkNetProtocol_Object = MibScalar
rcPTP1588ClkNetProtocol = _RcPTP1588ClkNetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 23),
    _RcPTP1588ClkNetProtocol_Type()
)
rcPTP1588ClkNetProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkNetProtocol.setStatus("current")


class _RcPTP1588ClkVlanId_Type(Integer32):
    """Custom type rcPTP1588ClkVlanId based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 4094),
    )


_RcPTP1588ClkVlanId_Type.__name__ = "Integer32"
_RcPTP1588ClkVlanId_Object = MibScalar
rcPTP1588ClkVlanId = _RcPTP1588ClkVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 24),
    _RcPTP1588ClkVlanId_Type()
)
rcPTP1588ClkVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkVlanId.setStatus("current")


class _RcPTP1588ClkPriority_Type(Unsigned32):
    """Custom type rcPTP1588ClkPriority based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcPTP1588ClkPriority_Type.__name__ = "Unsigned32"
_RcPTP1588ClkPriority_Object = MibScalar
rcPTP1588ClkPriority = _RcPTP1588ClkPriority_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 25),
    _RcPTP1588ClkPriority_Type()
)
rcPTP1588ClkPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkPriority.setStatus("current")


class _RcPTP1588ClkAccuracy_Type(Integer32):
    """Custom type rcPTP1588ClkAccuracy based on Integer32"""
    defaultValue = 3

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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("timeAccurateTo50ns", 0),
          ("timeAccurateTo100ns", 1),
          ("timeAccurateTo250ns", 2),
          ("timeAccurateTo1us", 3),
          ("timeAccurateTo2to5us", 4),
          ("timeAccurateTo10us", 5),
          ("timeAccurateTo25us", 6),
          ("timeAccurateTo100us", 7),
          ("timeAccurateTo250us", 8),
          ("timeAccurateTo1ms", 9),
          ("timeAccurateTo2to5ms", 10),
          ("timeAccurateTo10ms", 11),
          ("timeAccurateTo25ms", 12),
          ("timeAccurateTo100ms", 13),
          ("timeAccurateTo250ms", 14))
    )


_RcPTP1588ClkAccuracy_Type.__name__ = "Integer32"
_RcPTP1588ClkAccuracy_Object = MibScalar
rcPTP1588ClkAccuracy = _RcPTP1588ClkAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 1, 26),
    _RcPTP1588ClkAccuracy_Type()
)
rcPTP1588ClkAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588ClkAccuracy.setStatus("current")
_RcPTP1588Conformance_ObjectIdentity = ObjectIdentity
rcPTP1588Conformance = _RcPTP1588Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 3)
)
_RcPTP1588Groups_ObjectIdentity = ObjectIdentity
rcPTP1588Groups = _RcPTP1588Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 3, 2)
)
_RcPTP1588BCTables_ObjectIdentity = ObjectIdentity
rcPTP1588BCTables = _RcPTP1588BCTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4)
)
_RcPTP1588BClkTable_Object = MibTable
rcPTP1588BClkTable = _RcPTP1588BClkTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1)
)
if mibBuilder.loadTexts:
    rcPTP1588BClkTable.setStatus("current")
_RcPTP1588BClkEntry_Object = MibTableRow
rcPTP1588BClkEntry = _RcPTP1588BClkEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1)
)
rcPTP1588BClkEntry.setIndexNames(
    (0, "RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkPorts"),
)
if mibBuilder.loadTexts:
    rcPTP1588BClkEntry.setStatus("current")
_RcPTP1588BClkPorts_Type = PortList
_RcPTP1588BClkPorts_Object = MibTableColumn
rcPTP1588BClkPorts = _RcPTP1588BClkPorts_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 1),
    _RcPTP1588BClkPorts_Type()
)
rcPTP1588BClkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkPorts.setStatus("current")
_RcPTP1588BClkGroupName_Type = DisplayString
_RcPTP1588BClkGroupName_Object = MibTableColumn
rcPTP1588BClkGroupName = _RcPTP1588BClkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 2),
    _RcPTP1588BClkGroupName_Type()
)
rcPTP1588BClkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkGroupName.setStatus("current")


class _RcPTP1588BClkProfileId_Type(Integer32):
    """Custom type rcPTP1588BClkProfileId based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("defaultP2PProfile", 0),
          ("powerProfile", 1),
          ("ieee8021as", 2),
          ("lxi", 3),
          ("telecom", 4),
          ("utilityProfile", 5),
          ("defaultE2EProfile", 6),
          ("customProfile", 7),
          ("powerProfileV2", 8))
    )


_RcPTP1588BClkProfileId_Type.__name__ = "Integer32"
_RcPTP1588BClkProfileId_Object = MibTableColumn
rcPTP1588BClkProfileId = _RcPTP1588BClkProfileId_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 3),
    _RcPTP1588BClkProfileId_Type()
)
rcPTP1588BClkProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkProfileId.setStatus("current")


class _RcPTP1588BClkDomainNumber_Type(Unsigned32):
    """Custom type rcPTP1588BClkDomainNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_RcPTP1588BClkDomainNumber_Type.__name__ = "Unsigned32"
_RcPTP1588BClkDomainNumber_Object = MibTableColumn
rcPTP1588BClkDomainNumber = _RcPTP1588BClkDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 4),
    _RcPTP1588BClkDomainNumber_Type()
)
rcPTP1588BClkDomainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkDomainNumber.setStatus("current")


class _RcPTP1588BClkTransportProtocol_Type(Integer32):
    """Custom type rcPTP1588BClkTransportProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer2multicast", 1),
          ("layer3multicast", 2),
          ("layer3unicast", 3))
    )


_RcPTP1588BClkTransportProtocol_Type.__name__ = "Integer32"
_RcPTP1588BClkTransportProtocol_Object = MibTableColumn
rcPTP1588BClkTransportProtocol = _RcPTP1588BClkTransportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 5),
    _RcPTP1588BClkTransportProtocol_Type()
)
rcPTP1588BClkTransportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkTransportProtocol.setStatus("current")


class _RcPTP1588BClkPathDelayMech_Type(Integer32):
    """Custom type rcPTP1588BClkPathDelayMech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("end2end", 1),
          ("peer2peer", 2),
          ("disabled", 3))
    )


_RcPTP1588BClkPathDelayMech_Type.__name__ = "Integer32"
_RcPTP1588BClkPathDelayMech_Object = MibTableColumn
rcPTP1588BClkPathDelayMech = _RcPTP1588BClkPathDelayMech_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 6),
    _RcPTP1588BClkPathDelayMech_Type()
)
rcPTP1588BClkPathDelayMech.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkPathDelayMech.setStatus("current")


class _RcPTP1588BClkPTPPortType_Type(Integer32):
    """Custom type rcPTP1588BClkPTPPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("slaveonly", 2),
          ("masteronly", 3))
    )


_RcPTP1588BClkPTPPortType_Type.__name__ = "Integer32"
_RcPTP1588BClkPTPPortType_Object = MibTableColumn
rcPTP1588BClkPTPPortType = _RcPTP1588BClkPTPPortType_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 7),
    _RcPTP1588BClkPTPPortType_Type()
)
rcPTP1588BClkPTPPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkPTPPortType.setStatus("current")


class _RcPTP1588BClkSyncInt_Type(Integer32):
    """Custom type rcPTP1588BClkSyncInt based on Integer32"""
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
        *(("value125millSec", 1),
          ("value250millSec", 2),
          ("value500millSec", 3),
          ("value1Sec", 4),
          ("value2Sec", 5))
    )


_RcPTP1588BClkSyncInt_Type.__name__ = "Integer32"
_RcPTP1588BClkSyncInt_Object = MibTableColumn
rcPTP1588BClkSyncInt = _RcPTP1588BClkSyncInt_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 8),
    _RcPTP1588BClkSyncInt_Type()
)
rcPTP1588BClkSyncInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkSyncInt.setStatus("current")


class _RcPTP1588BClkAnnounceInt_Type(Integer32):
    """Custom type rcPTP1588BClkAnnounceInt based on Integer32"""
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
        *(("value1Sec", 1),
          ("value2Sec", 2),
          ("value4Sec", 3),
          ("value8Sec", 4),
          ("value16Sec", 5),
          ("value32Sec", 6))
    )


_RcPTP1588BClkAnnounceInt_Type.__name__ = "Integer32"
_RcPTP1588BClkAnnounceInt_Object = MibTableColumn
rcPTP1588BClkAnnounceInt = _RcPTP1588BClkAnnounceInt_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 9),
    _RcPTP1588BClkAnnounceInt_Type()
)
rcPTP1588BClkAnnounceInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkAnnounceInt.setStatus("current")


class _RcPTP1588BClkAnnounceRcTout_Type(Integer32):
    """Custom type rcPTP1588BClkAnnounceRcTout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_RcPTP1588BClkAnnounceRcTout_Type.__name__ = "Integer32"
_RcPTP1588BClkAnnounceRcTout_Object = MibTableColumn
rcPTP1588BClkAnnounceRcTout = _RcPTP1588BClkAnnounceRcTout_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 10),
    _RcPTP1588BClkAnnounceRcTout_Type()
)
rcPTP1588BClkAnnounceRcTout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkAnnounceRcTout.setStatus("current")
_RcPTP1588BClkAutoReg_Type = TruthValue
_RcPTP1588BClkAutoReg_Object = MibTableColumn
rcPTP1588BClkAutoReg = _RcPTP1588BClkAutoReg_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 11),
    _RcPTP1588BClkAutoReg_Type()
)
rcPTP1588BClkAutoReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkAutoReg.setStatus("current")
_RcPTP1588BClkMasterIP_Type = IpAddress
_RcPTP1588BClkMasterIP_Object = MibTableColumn
rcPTP1588BClkMasterIP = _RcPTP1588BClkMasterIP_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 12),
    _RcPTP1588BClkMasterIP_Type()
)
rcPTP1588BClkMasterIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkMasterIP.setStatus("current")
_RcPTP1588BClkBackUpIP_Type = IpAddress
_RcPTP1588BClkBackUpIP_Object = MibTableColumn
rcPTP1588BClkBackUpIP = _RcPTP1588BClkBackUpIP_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 13),
    _RcPTP1588BClkBackUpIP_Type()
)
rcPTP1588BClkBackUpIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkBackUpIP.setStatus("current")
_RcPTP1588BClkGMIdentity_Type = Integer32
_RcPTP1588BClkGMIdentity_Object = MibTableColumn
rcPTP1588BClkGMIdentity = _RcPTP1588BClkGMIdentity_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 14),
    _RcPTP1588BClkGMIdentity_Type()
)
rcPTP1588BClkGMIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkGMIdentity.setStatus("current")


class _RcPTP1588BClkVlanId_Type(Integer32):
    """Custom type rcPTP1588BClkVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 4094),
    )


_RcPTP1588BClkVlanId_Type.__name__ = "Integer32"
_RcPTP1588BClkVlanId_Object = MibTableColumn
rcPTP1588BClkVlanId = _RcPTP1588BClkVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 15),
    _RcPTP1588BClkVlanId_Type()
)
rcPTP1588BClkVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkVlanId.setStatus("current")


class _RcPTP1588BClkPriority_Type(Unsigned32):
    """Custom type rcPTP1588BClkPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcPTP1588BClkPriority_Type.__name__ = "Unsigned32"
_RcPTP1588BClkPriority_Object = MibTableColumn
rcPTP1588BClkPriority = _RcPTP1588BClkPriority_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 4, 1, 1, 16),
    _RcPTP1588BClkPriority_Type()
)
rcPTP1588BClkPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPTP1588BClkPriority.setStatus("current")

# Managed Objects groups

rcPTP1588BaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 3, 2, 1)
)
rcPTP1588BaseGroup.setObjects(
      *(("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkType"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588EthPorts"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588StartUpWait"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588NetClass"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588SlaveEthPort"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588SlaveDomain"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588SlaveAutoReg"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588SlaveMasteIP"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588SlaveBackUpIP"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ServoStatus"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588SlaveFeqAdj"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588E2EDelay"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588GlobalEnable"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588GlobalP2PRequestInterval"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588GlobalE2ERequestInterval"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588Global1Step"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkAnnounceInt"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkAnnounceRcTout"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkSyncInt"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkDelayMech"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkProfileId"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkDomainNumber"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkNetProtocol"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkVlanId"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkPriority"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588ClkAccuracy"))
)
if mibBuilder.loadTexts:
    rcPTP1588BaseGroup.setStatus("current")

rcPTP1588BCTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 12, 3, 2, 2)
)
rcPTP1588BCTablesGroup.setObjects(
      *(("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkPorts"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkGroupName"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkProfileId"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkDomainNumber"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkNetProtocol"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkPathDelayMech"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkPTPPortType"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkSyncInt"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkAnnounceInt"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkAnnounceRcTout"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkAutoReg"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkMasterIP"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkBackUpIP"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkGMIdentity"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkVlanId"),
        ("RUGGEDCOM-PTP1588-MIB", "rcPTP1588BClkPriority"))
)
if mibBuilder.loadTexts:
    rcPTP1588BCTablesGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-PTP1588-MIB",
    **{"rcPTP1588": rcPTP1588,
       "rcPTP1588Base": rcPTP1588Base,
       "rcPTP1588ClkType": rcPTP1588ClkType,
       "rcPTP1588EthPorts": rcPTP1588EthPorts,
       "rcPTP1588StartUpWait": rcPTP1588StartUpWait,
       "rcPTP1588NetClass": rcPTP1588NetClass,
       "rcPTP1588SlaveEthPort": rcPTP1588SlaveEthPort,
       "rcPTP1588SlaveDomain": rcPTP1588SlaveDomain,
       "rcPTP1588SlaveAutoReg": rcPTP1588SlaveAutoReg,
       "rcPTP1588SlaveMasteIP": rcPTP1588SlaveMasteIP,
       "rcPTP1588SlaveBackUpIP": rcPTP1588SlaveBackUpIP,
       "rcPTP1588ServoStatus": rcPTP1588ServoStatus,
       "rcPTP1588SlaveFeqAdj": rcPTP1588SlaveFeqAdj,
       "rcPTP1588E2EDelay": rcPTP1588E2EDelay,
       "rcPTP1588GlobalEnable": rcPTP1588GlobalEnable,
       "rcPTP1588GlobalP2PRequestInterval": rcPTP1588GlobalP2PRequestInterval,
       "rcPTP1588GlobalE2ERequestInterval": rcPTP1588GlobalE2ERequestInterval,
       "rcPTP1588Global1Step": rcPTP1588Global1Step,
       "rcPTP1588ClkAnnounceInt": rcPTP1588ClkAnnounceInt,
       "rcPTP1588ClkAnnounceRcTout": rcPTP1588ClkAnnounceRcTout,
       "rcPTP1588ClkSyncInt": rcPTP1588ClkSyncInt,
       "rcPTP1588ClkDelayMech": rcPTP1588ClkDelayMech,
       "rcPTP1588ClkProfileId": rcPTP1588ClkProfileId,
       "rcPTP1588ClkDomainNumber": rcPTP1588ClkDomainNumber,
       "rcPTP1588ClkNetProtocol": rcPTP1588ClkNetProtocol,
       "rcPTP1588ClkVlanId": rcPTP1588ClkVlanId,
       "rcPTP1588ClkPriority": rcPTP1588ClkPriority,
       "rcPTP1588ClkAccuracy": rcPTP1588ClkAccuracy,
       "rcPTP1588Conformance": rcPTP1588Conformance,
       "rcPTP1588Groups": rcPTP1588Groups,
       "rcPTP1588BaseGroup": rcPTP1588BaseGroup,
       "rcPTP1588BCTablesGroup": rcPTP1588BCTablesGroup,
       "rcPTP1588BCTables": rcPTP1588BCTables,
       "rcPTP1588BClkTable": rcPTP1588BClkTable,
       "rcPTP1588BClkEntry": rcPTP1588BClkEntry,
       "rcPTP1588BClkPorts": rcPTP1588BClkPorts,
       "rcPTP1588BClkGroupName": rcPTP1588BClkGroupName,
       "rcPTP1588BClkProfileId": rcPTP1588BClkProfileId,
       "rcPTP1588BClkDomainNumber": rcPTP1588BClkDomainNumber,
       "rcPTP1588BClkTransportProtocol": rcPTP1588BClkTransportProtocol,
       "rcPTP1588BClkPathDelayMech": rcPTP1588BClkPathDelayMech,
       "rcPTP1588BClkPTPPortType": rcPTP1588BClkPTPPortType,
       "rcPTP1588BClkSyncInt": rcPTP1588BClkSyncInt,
       "rcPTP1588BClkAnnounceInt": rcPTP1588BClkAnnounceInt,
       "rcPTP1588BClkAnnounceRcTout": rcPTP1588BClkAnnounceRcTout,
       "rcPTP1588BClkAutoReg": rcPTP1588BClkAutoReg,
       "rcPTP1588BClkMasterIP": rcPTP1588BClkMasterIP,
       "rcPTP1588BClkBackUpIP": rcPTP1588BClkBackUpIP,
       "rcPTP1588BClkGMIdentity": rcPTP1588BClkGMIdentity,
       "rcPTP1588BClkVlanId": rcPTP1588BClkVlanId,
       "rcPTP1588BClkPriority": rcPTP1588BClkPriority}
)
