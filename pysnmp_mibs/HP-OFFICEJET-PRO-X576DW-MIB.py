_k='enable'
_j='auto-ip'
_i='default-config'
_h='not-configured'
_g='bootp-four'
_f='manual-three'
_e='bootp-two'
_d='manual-one'
_c='obsolete'
_b='InetAddressType'
_a='InetAddress'
_Z='KBytes'
_Y='false'
_X='true'
_W='disable'
_V='disabled'
_U='enabled'
_T='invalid'
_S='testing'
_R='down'
_Q='unknown'
_P='Gauge32'
_O='Enable'
_N='Disable'
_M='other'
_L='TruthValue'
_K='SnmpAdminString'
_J='write-only'
_I='deprecated'
_H='DisplayString'
_G='OctetString'
_F='optional'
_E='mandatory'
_D='Integer32'
_C='read-write'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
KBytes,ProductID=mibBuilder.importSymbols('HOST-RESOURCES-MIB',_Z,'ProductID')
IANACharset,=mibBuilder.importSymbols('IANA-CHARSET-MIB','IANACharset')
PrtAlertCodeTC,PrtAlertGroupTC,PrtAlertTrainingLevelTC,PrtChannelTypeTC,PrtConsoleColorTC,PrtConsoleDisableTC,PrtCoverStatusTC,PrtGeneralResetTC,PrtInputTypeTC,PrtInterpreterLangFamilyTC,PrtMarkerMarkTechTC,PrtMarkerSuppliesTypeTC,PrtMediaPathTypeTC,PrtOutputTypeTC=mibBuilder.importSymbols('IANA-PRINTER-MIB','PrtAlertCodeTC','PrtAlertGroupTC','PrtAlertTrainingLevelTC','PrtChannelTypeTC','PrtConsoleColorTC','PrtConsoleDisableTC','PrtCoverStatusTC','PrtGeneralResetTC','PrtInputTypeTC','PrtInterpreterLangFamilyTC','PrtMarkerMarkTechTC','PrtMarkerSuppliesTypeTC','PrtMediaPathTypeTC','PrtOutputTypeTC')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
WEPKeytype,=mibBuilder.importSymbols('IEEE802dot11-MIB','WEPKeytype')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_a,'InetAddressPrefixLength',_b)
PresentOnOff,PrtAlertSeverityLevelTC,PrtCapacityUnitTC,PrtChannelStateTC,PrtConsoleDescriptionStringTC,PrtInterpreterTwoWayTC,PrtLocalizedDescriptionStringTC,PrtMarkerAddressabilityUnitTC,PrtMarkerColorantRoleTC,PrtMarkerCounterUnitTC,PrtMarkerSuppliesClassTC,PrtMarkerSuppliesSupplyUnitTC,PrtMediaPathMaxSpeedPrintUnitTC,PrtMediaUnitTC,PrtOutputPageDeliveryOrientationTC,PrtOutputStackingOrderTC,PrtPrintOrientationTC,PrtSubUnitStatusTC=mibBuilder.importSymbols('Printer-MIB','PresentOnOff','PrtAlertSeverityLevelTC','PrtCapacityUnitTC','PrtChannelStateTC','PrtConsoleDescriptionStringTC','PrtInterpreterTwoWayTC','PrtLocalizedDescriptionStringTC','PrtMarkerAddressabilityUnitTC','PrtMarkerColorantRoleTC','PrtMarkerCounterUnitTC','PrtMarkerSuppliesClassTC','PrtMarkerSuppliesSupplyUnitTC','PrtMediaPathMaxSpeedPrintUnitTC','PrtMediaUnitTC','PrtOutputPageDeliveryOrientationTC','PrtOutputStackingOrderTC','PrtPrintOrientationTC','PrtSubUnitStatusTC')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_P,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_H,'PhysAddress','TextualConvention','TimeStamp',_L)
_Ieee802dot11_ObjectIdentity=ObjectIdentity
ieee802dot11=_Ieee802dot11_ObjectIdentity((1,2,840,10036))
_Dot11smt_ObjectIdentity=ObjectIdentity
dot11smt=_Dot11smt_ObjectIdentity((1,2,840,10036,1))
_Dot11StationConfigTable_ObjectIdentity=ObjectIdentity
dot11StationConfigTable=_Dot11StationConfigTable_ObjectIdentity((1,2,840,10036,1,1))
_Dot11StationConfigEntry_ObjectIdentity=ObjectIdentity
dot11StationConfigEntry=_Dot11StationConfigEntry_ObjectIdentity((1,2,840,10036,1,1,1))
class _Dot11DesiredSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot11DesiredSSID_Type.__name__=_G
_Dot11DesiredSSID_Object=MibScalar
dot11DesiredSSID=_Dot11DesiredSSID_Object((1,2,840,10036,1,1,1,9),_Dot11DesiredSSID_Type())
dot11DesiredSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11DesiredSSID.setStatus(_B)
class _Dot11DesiredBSSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('infrastructure',1),('independent',2),('any',3)))
_Dot11DesiredBSSType_Type.__name__=_D
_Dot11DesiredBSSType_Object=MibScalar
dot11DesiredBSSType=_Dot11DesiredBSSType_Object((1,2,840,10036,1,1,1,10),_Dot11DesiredBSSType_Type())
dot11DesiredBSSType.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11DesiredBSSType.setStatus(_B)
_Dot11AuthenticationAlgorithmsTable_ObjectIdentity=ObjectIdentity
dot11AuthenticationAlgorithmsTable=_Dot11AuthenticationAlgorithmsTable_ObjectIdentity((1,2,840,10036,1,2))
_Dot11AuthenticationAlgorithmsEntry_ObjectIdentity=ObjectIdentity
dot11AuthenticationAlgorithmsEntry=_Dot11AuthenticationAlgorithmsEntry_ObjectIdentity((1,2,840,10036,1,2,1))
class _Dot11AuthenticationAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('openSystem',1),('sharedKey',2)))
_Dot11AuthenticationAlgorithm_Type.__name__=_D
_Dot11AuthenticationAlgorithm_Object=MibScalar
dot11AuthenticationAlgorithm=_Dot11AuthenticationAlgorithm_Object((1,2,840,10036,1,2,1,2),_Dot11AuthenticationAlgorithm_Type())
dot11AuthenticationAlgorithm.setMaxAccess(_A)
if mibBuilder.loadTexts:dot11AuthenticationAlgorithm.setStatus(_B)
_Dot11AuthenticationAlgorithmsEnable_Type=TruthValue
_Dot11AuthenticationAlgorithmsEnable_Object=MibScalar
dot11AuthenticationAlgorithmsEnable=_Dot11AuthenticationAlgorithmsEnable_Object((1,2,840,10036,1,2,1,3),_Dot11AuthenticationAlgorithmsEnable_Type())
dot11AuthenticationAlgorithmsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11AuthenticationAlgorithmsEnable.setStatus(_B)
_Dot11WEPDefaultKeysTable_ObjectIdentity=ObjectIdentity
dot11WEPDefaultKeysTable=_Dot11WEPDefaultKeysTable_ObjectIdentity((1,2,840,10036,1,3))
_Dot11WEPDefaultKeysEntry_ObjectIdentity=ObjectIdentity
dot11WEPDefaultKeysEntry=_Dot11WEPDefaultKeysEntry_ObjectIdentity((1,2,840,10036,1,3,1))
_Dot11WEPDefaultKeyValue_Type=WEPKeytype
_Dot11WEPDefaultKeyValue_Object=MibScalar
dot11WEPDefaultKeyValue=_Dot11WEPDefaultKeyValue_Object((1,2,840,10036,1,3,1,2),_Dot11WEPDefaultKeyValue_Type())
dot11WEPDefaultKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11WEPDefaultKeyValue.setStatus(_B)
_Dot11PrivacyTable_ObjectIdentity=ObjectIdentity
dot11PrivacyTable=_Dot11PrivacyTable_ObjectIdentity((1,2,840,10036,1,5))
_Dot11PrivacyEntry_ObjectIdentity=ObjectIdentity
dot11PrivacyEntry=_Dot11PrivacyEntry_ObjectIdentity((1,2,840,10036,1,5,1))
_Dot11PrivacyInvoked_Type=TruthValue
_Dot11PrivacyInvoked_Object=MibScalar
dot11PrivacyInvoked=_Dot11PrivacyInvoked_Object((1,2,840,10036,1,5,1,1),_Dot11PrivacyInvoked_Type())
dot11PrivacyInvoked.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11PrivacyInvoked.setStatus(_B)
class _Dot11WEPDefaultKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Dot11WEPDefaultKeyID_Type.__name__=_D
_Dot11WEPDefaultKeyID_Object=MibScalar
dot11WEPDefaultKeyID=_Dot11WEPDefaultKeyID_Object((1,2,840,10036,1,5,1,2),_Dot11WEPDefaultKeyID_Type())
dot11WEPDefaultKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11WEPDefaultKeyID.setStatus(_B)
_Dot11phy_ObjectIdentity=ObjectIdentity
dot11phy=_Dot11phy_ObjectIdentity((1,2,840,10036,4))
_Dot11PhyOperationTable_ObjectIdentity=ObjectIdentity
dot11PhyOperationTable=_Dot11PhyOperationTable_ObjectIdentity((1,2,840,10036,4,1))
_Dot11PhyOperationEntry_ObjectIdentity=ObjectIdentity
dot11PhyOperationEntry=_Dot11PhyOperationEntry_ObjectIdentity((1,2,840,10036,4,1,1))
class _Dot11CurrentRegDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,32,48,49,50,64,65)));namedValues=NamedValues(*(('fcc',16),('doc',32),('etsi',48),('spain',49),('france',50),('mkk',64),('japan',65)))
_Dot11CurrentRegDomain_Type.__name__=_D
_Dot11CurrentRegDomain_Object=MibScalar
dot11CurrentRegDomain=_Dot11CurrentRegDomain_Object((1,2,840,10036,4,1,1,2),_Dot11CurrentRegDomain_Type())
dot11CurrentRegDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11CurrentRegDomain.setStatus(_B)
_Ieee802dot11i_ObjectIdentity=ObjectIdentity
ieee802dot11i=_Ieee802dot11i_ObjectIdentity((1,2,840,10036,7))
_Dot11RSNConfigAuthenticationSuitesTable_ObjectIdentity=ObjectIdentity
dot11RSNConfigAuthenticationSuitesTable=_Dot11RSNConfigAuthenticationSuitesTable_ObjectIdentity((1,2,840,10036,7,3))
_Dot11RSNConfigAuthenticationSuitesEntry_ObjectIdentity=ObjectIdentity
dot11RSNConfigAuthenticationSuitesEntry=_Dot11RSNConfigAuthenticationSuitesEntry_ObjectIdentity((1,2,840,10036,7,3,1))
class _Dot11RSNConfigAuthenticationSuite_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Dot11RSNConfigAuthenticationSuite_Type.__name__=_G
_Dot11RSNConfigAuthenticationSuite_Object=MibScalar
dot11RSNConfigAuthenticationSuite=_Dot11RSNConfigAuthenticationSuite_Object((1,2,840,10036,7,3,1,2),_Dot11RSNConfigAuthenticationSuite_Type())
dot11RSNConfigAuthenticationSuite.setMaxAccess(_A)
if mibBuilder.loadTexts:dot11RSNConfigAuthenticationSuite.setStatus(_B)
_Dot11RSNConfigAuthenticationSuiteEnabled_Type=TruthValue
_Dot11RSNConfigAuthenticationSuiteEnabled_Object=MibScalar
dot11RSNConfigAuthenticationSuiteEnabled=_Dot11RSNConfigAuthenticationSuiteEnabled_Object((1,2,840,10036,7,3,1,3),_Dot11RSNConfigAuthenticationSuiteEnabled_Type())
dot11RSNConfigAuthenticationSuiteEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11RSNConfigAuthenticationSuiteEnabled.setStatus(_B)
_Org_ObjectIdentity=ObjectIdentity
org=_Org_ObjectIdentity((1,3))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Mgmt_ObjectIdentity=ObjectIdentity
mgmt=_Mgmt_ObjectIdentity((1,3,6,1,2))
_Mib_2_ObjectIdentity=ObjectIdentity
mib_2=_Mib_2_ObjectIdentity((1,3,6,1,2,1))
_Interfaces_ObjectIdentity=ObjectIdentity
interfaces=_Interfaces_ObjectIdentity((1,3,6,1,2,1,2))
_IfNumber_Type=Integer32
_IfNumber_Object=MibScalar
ifNumber=_IfNumber_Object((1,3,6,1,2,1,2,1),_IfNumber_Type())
ifNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:ifNumber.setStatus(_B)
_IfTable_ObjectIdentity=ObjectIdentity
ifTable=_IfTable_ObjectIdentity((1,3,6,1,2,1,2,2))
_IfEntry_ObjectIdentity=ObjectIdentity
ifEntry=_IfEntry_ObjectIdentity((1,3,6,1,2,1,2,2,1))
_IfIndex_Type=InterfaceIndex
_IfIndex_Object=MibScalar
ifIndex=_IfIndex_Object((1,3,6,1,2,1,2,2,1,1),_IfIndex_Type())
ifIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:ifIndex.setStatus(_B)
class _IfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfDescr_Type.__name__=_H
_IfDescr_Object=MibScalar
ifDescr=_IfDescr_Object((1,3,6,1,2,1,2,2,1,2),_IfDescr_Type())
ifDescr.setMaxAccess(_A)
if mibBuilder.loadTexts:ifDescr.setStatus(_B)
_IfType_Type=IANAifType
_IfType_Object=MibScalar
ifType=_IfType_Object((1,3,6,1,2,1,2,2,1,3),_IfType_Type())
ifType.setMaxAccess(_A)
if mibBuilder.loadTexts:ifType.setStatus(_B)
_IfMtu_Type=Integer32
_IfMtu_Object=MibScalar
ifMtu=_IfMtu_Object((1,3,6,1,2,1,2,2,1,4),_IfMtu_Type())
ifMtu.setMaxAccess(_A)
if mibBuilder.loadTexts:ifMtu.setStatus(_B)
_IfSpeed_Type=Gauge32
_IfSpeed_Object=MibScalar
ifSpeed=_IfSpeed_Object((1,3,6,1,2,1,2,2,1,5),_IfSpeed_Type())
ifSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:ifSpeed.setStatus(_B)
_IfPhysAddress_Type=PhysAddress
_IfPhysAddress_Object=MibScalar
ifPhysAddress=_IfPhysAddress_Object((1,3,6,1,2,1,2,2,1,6),_IfPhysAddress_Type())
ifPhysAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:ifPhysAddress.setStatus(_B)
class _IfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_R,2),(_S,3)))
_IfAdminStatus_Type.__name__=_D
_IfAdminStatus_Object=MibScalar
ifAdminStatus=_IfAdminStatus_Object((1,3,6,1,2,1,2,2,1,7),_IfAdminStatus_Type())
ifAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAdminStatus.setStatus(_B)
class _IfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),(_R,2),(_S,3),(_Q,4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_IfOperStatus_Type.__name__=_D
_IfOperStatus_Object=MibScalar
ifOperStatus=_IfOperStatus_Object((1,3,6,1,2,1,2,2,1,8),_IfOperStatus_Type())
ifOperStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:ifOperStatus.setStatus(_B)
_IfLastChange_Type=TimeTicks
_IfLastChange_Object=MibScalar
ifLastChange=_IfLastChange_Object((1,3,6,1,2,1,2,2,1,9),_IfLastChange_Type())
ifLastChange.setMaxAccess(_A)
if mibBuilder.loadTexts:ifLastChange.setStatus(_B)
_IfInOctets_Type=Counter32
_IfInOctets_Object=MibScalar
ifInOctets=_IfInOctets_Object((1,3,6,1,2,1,2,2,1,10),_IfInOctets_Type())
ifInOctets.setMaxAccess(_A)
if mibBuilder.loadTexts:ifInOctets.setStatus(_B)
_IfInUcastPkts_Type=Counter32
_IfInUcastPkts_Object=MibScalar
ifInUcastPkts=_IfInUcastPkts_Object((1,3,6,1,2,1,2,2,1,11),_IfInUcastPkts_Type())
ifInUcastPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:ifInUcastPkts.setStatus(_B)
_IfInNUcastPkts_Type=Counter32
_IfInNUcastPkts_Object=MibScalar
ifInNUcastPkts=_IfInNUcastPkts_Object((1,3,6,1,2,1,2,2,1,12),_IfInNUcastPkts_Type())
ifInNUcastPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:ifInNUcastPkts.setStatus(_I)
_IfInDiscards_Type=Counter32
_IfInDiscards_Object=MibScalar
ifInDiscards=_IfInDiscards_Object((1,3,6,1,2,1,2,2,1,13),_IfInDiscards_Type())
ifInDiscards.setMaxAccess(_A)
if mibBuilder.loadTexts:ifInDiscards.setStatus(_B)
_IfInErrors_Type=Counter32
_IfInErrors_Object=MibScalar
ifInErrors=_IfInErrors_Object((1,3,6,1,2,1,2,2,1,14),_IfInErrors_Type())
ifInErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:ifInErrors.setStatus(_B)
_IfInUnknownProtos_Type=Counter32
_IfInUnknownProtos_Object=MibScalar
ifInUnknownProtos=_IfInUnknownProtos_Object((1,3,6,1,2,1,2,2,1,15),_IfInUnknownProtos_Type())
ifInUnknownProtos.setMaxAccess(_A)
if mibBuilder.loadTexts:ifInUnknownProtos.setStatus(_B)
_IfOutOctets_Type=Counter32
_IfOutOctets_Object=MibScalar
ifOutOctets=_IfOutOctets_Object((1,3,6,1,2,1,2,2,1,16),_IfOutOctets_Type())
ifOutOctets.setMaxAccess(_A)
if mibBuilder.loadTexts:ifOutOctets.setStatus(_B)
_IfOutUcastPkts_Type=Counter32
_IfOutUcastPkts_Object=MibScalar
ifOutUcastPkts=_IfOutUcastPkts_Object((1,3,6,1,2,1,2,2,1,17),_IfOutUcastPkts_Type())
ifOutUcastPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:ifOutUcastPkts.setStatus(_B)
_IfOutNUcastPkts_Type=Counter32
_IfOutNUcastPkts_Object=MibScalar
ifOutNUcastPkts=_IfOutNUcastPkts_Object((1,3,6,1,2,1,2,2,1,18),_IfOutNUcastPkts_Type())
ifOutNUcastPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:ifOutNUcastPkts.setStatus(_I)
_IfOutDiscards_Type=Counter32
_IfOutDiscards_Object=MibScalar
ifOutDiscards=_IfOutDiscards_Object((1,3,6,1,2,1,2,2,1,19),_IfOutDiscards_Type())
ifOutDiscards.setMaxAccess(_A)
if mibBuilder.loadTexts:ifOutDiscards.setStatus(_B)
_IfOutErrors_Type=Counter32
_IfOutErrors_Object=MibScalar
ifOutErrors=_IfOutErrors_Object((1,3,6,1,2,1,2,2,1,20),_IfOutErrors_Type())
ifOutErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:ifOutErrors.setStatus(_B)
_IfOutQLen_Type=Gauge32
_IfOutQLen_Object=MibScalar
ifOutQLen=_IfOutQLen_Object((1,3,6,1,2,1,2,2,1,21),_IfOutQLen_Type())
ifOutQLen.setMaxAccess(_A)
if mibBuilder.loadTexts:ifOutQLen.setStatus(_I)
_IfSpecific_Type=ObjectIdentifier
_IfSpecific_Object=MibScalar
ifSpecific=_IfSpecific_Object((1,3,6,1,2,1,2,2,1,22),_IfSpecific_Type())
ifSpecific.setMaxAccess(_A)
if mibBuilder.loadTexts:ifSpecific.setStatus(_I)
_At_ObjectIdentity=ObjectIdentity
at=_At_ObjectIdentity((1,3,6,1,2,1,3))
_AtTable_ObjectIdentity=ObjectIdentity
atTable=_AtTable_ObjectIdentity((1,3,6,1,2,1,3,1))
_AtEntry_ObjectIdentity=ObjectIdentity
atEntry=_AtEntry_ObjectIdentity((1,3,6,1,2,1,3,1,1))
_AtIfIndex_Type=Integer32
_AtIfIndex_Object=MibScalar
atIfIndex=_AtIfIndex_Object((1,3,6,1,2,1,3,1,1,1),_AtIfIndex_Type())
atIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atIfIndex.setStatus(_I)
_AtPhysAddress_Type=PhysAddress
_AtPhysAddress_Object=MibScalar
atPhysAddress=_AtPhysAddress_Object((1,3,6,1,2,1,3,1,1,2),_AtPhysAddress_Type())
atPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atPhysAddress.setStatus(_I)
_AtNetAddress_Type=IpAddress
_AtNetAddress_Object=MibScalar
atNetAddress=_AtNetAddress_Object((1,3,6,1,2,1,3,1,1,3),_AtNetAddress_Type())
atNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atNetAddress.setStatus(_I)
_Ip_ObjectIdentity=ObjectIdentity
ip=_Ip_ObjectIdentity((1,3,6,1,2,1,4))
class _IpForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('not-forwarding',2)))
_IpForwarding_Type.__name__=_D
_IpForwarding_Object=MibScalar
ipForwarding=_IpForwarding_Object((1,3,6,1,2,1,4,1),_IpForwarding_Type())
ipForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwarding.setStatus(_E)
_IpDefaultTTL_Type=Integer32
_IpDefaultTTL_Object=MibScalar
ipDefaultTTL=_IpDefaultTTL_Object((1,3,6,1,2,1,4,2),_IpDefaultTTL_Type())
ipDefaultTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:ipDefaultTTL.setStatus(_E)
_IpInReceives_Type=Counter32
_IpInReceives_Object=MibScalar
ipInReceives=_IpInReceives_Object((1,3,6,1,2,1,4,3),_IpInReceives_Type())
ipInReceives.setMaxAccess(_A)
if mibBuilder.loadTexts:ipInReceives.setStatus(_E)
_IpInHdrErrors_Type=Counter32
_IpInHdrErrors_Object=MibScalar
ipInHdrErrors=_IpInHdrErrors_Object((1,3,6,1,2,1,4,4),_IpInHdrErrors_Type())
ipInHdrErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:ipInHdrErrors.setStatus(_E)
_IpInAddrErrors_Type=Counter32
_IpInAddrErrors_Object=MibScalar
ipInAddrErrors=_IpInAddrErrors_Object((1,3,6,1,2,1,4,5),_IpInAddrErrors_Type())
ipInAddrErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:ipInAddrErrors.setStatus(_E)
_IpForwDatagrams_Type=Counter32
_IpForwDatagrams_Object=MibScalar
ipForwDatagrams=_IpForwDatagrams_Object((1,3,6,1,2,1,4,6),_IpForwDatagrams_Type())
ipForwDatagrams.setMaxAccess(_A)
if mibBuilder.loadTexts:ipForwDatagrams.setStatus(_E)
_IpInUnknownProtos_Type=Counter32
_IpInUnknownProtos_Object=MibScalar
ipInUnknownProtos=_IpInUnknownProtos_Object((1,3,6,1,2,1,4,7),_IpInUnknownProtos_Type())
ipInUnknownProtos.setMaxAccess(_A)
if mibBuilder.loadTexts:ipInUnknownProtos.setStatus(_E)
_IpInDiscards_Type=Counter32
_IpInDiscards_Object=MibScalar
ipInDiscards=_IpInDiscards_Object((1,3,6,1,2,1,4,8),_IpInDiscards_Type())
ipInDiscards.setMaxAccess(_A)
if mibBuilder.loadTexts:ipInDiscards.setStatus(_E)
_IpInDelivers_Type=Counter32
_IpInDelivers_Object=MibScalar
ipInDelivers=_IpInDelivers_Object((1,3,6,1,2,1,4,9),_IpInDelivers_Type())
ipInDelivers.setMaxAccess(_A)
if mibBuilder.loadTexts:ipInDelivers.setStatus(_E)
_IpOutRequests_Type=Counter32
_IpOutRequests_Object=MibScalar
ipOutRequests=_IpOutRequests_Object((1,3,6,1,2,1,4,10),_IpOutRequests_Type())
ipOutRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:ipOutRequests.setStatus(_E)
_IpOutDiscards_Type=Counter32
_IpOutDiscards_Object=MibScalar
ipOutDiscards=_IpOutDiscards_Object((1,3,6,1,2,1,4,11),_IpOutDiscards_Type())
ipOutDiscards.setMaxAccess(_A)
if mibBuilder.loadTexts:ipOutDiscards.setStatus(_E)
_IpOutNoRoutes_Type=Counter32
_IpOutNoRoutes_Object=MibScalar
ipOutNoRoutes=_IpOutNoRoutes_Object((1,3,6,1,2,1,4,12),_IpOutNoRoutes_Type())
ipOutNoRoutes.setMaxAccess(_A)
if mibBuilder.loadTexts:ipOutNoRoutes.setStatus(_E)
_IpReasmTimeout_Type=Integer32
_IpReasmTimeout_Object=MibScalar
ipReasmTimeout=_IpReasmTimeout_Object((1,3,6,1,2,1,4,13),_IpReasmTimeout_Type())
ipReasmTimeout.setMaxAccess(_A)
if mibBuilder.loadTexts:ipReasmTimeout.setStatus(_E)
_IpReasmReqds_Type=Counter32
_IpReasmReqds_Object=MibScalar
ipReasmReqds=_IpReasmReqds_Object((1,3,6,1,2,1,4,14),_IpReasmReqds_Type())
ipReasmReqds.setMaxAccess(_A)
if mibBuilder.loadTexts:ipReasmReqds.setStatus(_E)
_IpReasmOKs_Type=Counter32
_IpReasmOKs_Object=MibScalar
ipReasmOKs=_IpReasmOKs_Object((1,3,6,1,2,1,4,15),_IpReasmOKs_Type())
ipReasmOKs.setMaxAccess(_A)
if mibBuilder.loadTexts:ipReasmOKs.setStatus(_E)
_IpReasmFails_Type=Counter32
_IpReasmFails_Object=MibScalar
ipReasmFails=_IpReasmFails_Object((1,3,6,1,2,1,4,16),_IpReasmFails_Type())
ipReasmFails.setMaxAccess(_A)
if mibBuilder.loadTexts:ipReasmFails.setStatus(_E)
_IpFragOKs_Type=Counter32
_IpFragOKs_Object=MibScalar
ipFragOKs=_IpFragOKs_Object((1,3,6,1,2,1,4,17),_IpFragOKs_Type())
ipFragOKs.setMaxAccess(_A)
if mibBuilder.loadTexts:ipFragOKs.setStatus(_E)
_IpFragFails_Type=Counter32
_IpFragFails_Object=MibScalar
ipFragFails=_IpFragFails_Object((1,3,6,1,2,1,4,18),_IpFragFails_Type())
ipFragFails.setMaxAccess(_A)
if mibBuilder.loadTexts:ipFragFails.setStatus(_E)
_IpFragCreates_Type=Counter32
_IpFragCreates_Object=MibScalar
ipFragCreates=_IpFragCreates_Object((1,3,6,1,2,1,4,19),_IpFragCreates_Type())
ipFragCreates.setMaxAccess(_A)
if mibBuilder.loadTexts:ipFragCreates.setStatus(_E)
_IpAddrTable_ObjectIdentity=ObjectIdentity
ipAddrTable=_IpAddrTable_ObjectIdentity((1,3,6,1,2,1,4,20))
_IpAddrEntry_ObjectIdentity=ObjectIdentity
ipAddrEntry=_IpAddrEntry_ObjectIdentity((1,3,6,1,2,1,4,20,1))
_IpAdEntAddr_Type=IpAddress
_IpAdEntAddr_Object=MibScalar
ipAdEntAddr=_IpAdEntAddr_Object((1,3,6,1,2,1,4,20,1,1),_IpAdEntAddr_Type())
ipAdEntAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:ipAdEntAddr.setStatus(_E)
_IpAdEntIfIndex_Type=Integer32
_IpAdEntIfIndex_Object=MibScalar
ipAdEntIfIndex=_IpAdEntIfIndex_Object((1,3,6,1,2,1,4,20,1,2),_IpAdEntIfIndex_Type())
ipAdEntIfIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:ipAdEntIfIndex.setStatus(_E)
_IpAdEntNetMask_Type=IpAddress
_IpAdEntNetMask_Object=MibScalar
ipAdEntNetMask=_IpAdEntNetMask_Object((1,3,6,1,2,1,4,20,1,3),_IpAdEntNetMask_Type())
ipAdEntNetMask.setMaxAccess(_A)
if mibBuilder.loadTexts:ipAdEntNetMask.setStatus(_E)
_IpAdEntBcastAddr_Type=Integer32
_IpAdEntBcastAddr_Object=MibScalar
ipAdEntBcastAddr=_IpAdEntBcastAddr_Object((1,3,6,1,2,1,4,20,1,4),_IpAdEntBcastAddr_Type())
ipAdEntBcastAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:ipAdEntBcastAddr.setStatus(_E)
class _IpAdEntReasmMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpAdEntReasmMaxSize_Type.__name__=_D
_IpAdEntReasmMaxSize_Object=MibScalar
ipAdEntReasmMaxSize=_IpAdEntReasmMaxSize_Object((1,3,6,1,2,1,4,20,1,5),_IpAdEntReasmMaxSize_Type())
ipAdEntReasmMaxSize.setMaxAccess(_A)
if mibBuilder.loadTexts:ipAdEntReasmMaxSize.setStatus(_E)
_IpRouteTable_ObjectIdentity=ObjectIdentity
ipRouteTable=_IpRouteTable_ObjectIdentity((1,3,6,1,2,1,4,21))
_IpRouteEntry_ObjectIdentity=ObjectIdentity
ipRouteEntry=_IpRouteEntry_ObjectIdentity((1,3,6,1,2,1,4,21,1))
_IpRouteDest_Type=IpAddress
_IpRouteDest_Object=MibScalar
ipRouteDest=_IpRouteDest_Object((1,3,6,1,2,1,4,21,1,1),_IpRouteDest_Type())
ipRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteDest.setStatus(_E)
_IpRouteIfIndex_Type=Integer32
_IpRouteIfIndex_Object=MibScalar
ipRouteIfIndex=_IpRouteIfIndex_Object((1,3,6,1,2,1,4,21,1,2),_IpRouteIfIndex_Type())
ipRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteIfIndex.setStatus(_E)
_IpRouteMetric1_Type=Integer32
_IpRouteMetric1_Object=MibScalar
ipRouteMetric1=_IpRouteMetric1_Object((1,3,6,1,2,1,4,21,1,3),_IpRouteMetric1_Type())
ipRouteMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteMetric1.setStatus(_E)
_IpRouteMetric2_Type=Integer32
_IpRouteMetric2_Object=MibScalar
ipRouteMetric2=_IpRouteMetric2_Object((1,3,6,1,2,1,4,21,1,4),_IpRouteMetric2_Type())
ipRouteMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteMetric2.setStatus(_E)
_IpRouteMetric3_Type=Integer32
_IpRouteMetric3_Object=MibScalar
ipRouteMetric3=_IpRouteMetric3_Object((1,3,6,1,2,1,4,21,1,5),_IpRouteMetric3_Type())
ipRouteMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteMetric3.setStatus(_E)
_IpRouteMetric4_Type=Integer32
_IpRouteMetric4_Object=MibScalar
ipRouteMetric4=_IpRouteMetric4_Object((1,3,6,1,2,1,4,21,1,6),_IpRouteMetric4_Type())
ipRouteMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteMetric4.setStatus(_E)
_IpRouteNextHop_Type=IpAddress
_IpRouteNextHop_Object=MibScalar
ipRouteNextHop=_IpRouteNextHop_Object((1,3,6,1,2,1,4,21,1,7),_IpRouteNextHop_Type())
ipRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteNextHop.setStatus(_E)
class _IpRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_T,2),('direct',3),('indirect',4)))
_IpRouteType_Type.__name__=_D
_IpRouteType_Object=MibScalar
ipRouteType=_IpRouteType_Object((1,3,6,1,2,1,4,21,1,8),_IpRouteType_Type())
ipRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteType.setStatus(_E)
class _IpRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_M,1),('local',2),('netmgmt',3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('is-is',9),('es-is',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14)))
_IpRouteProto_Type.__name__=_D
_IpRouteProto_Object=MibScalar
ipRouteProto=_IpRouteProto_Object((1,3,6,1,2,1,4,21,1,9),_IpRouteProto_Type())
ipRouteProto.setMaxAccess(_A)
if mibBuilder.loadTexts:ipRouteProto.setStatus(_E)
_IpRouteAge_Type=Integer32
_IpRouteAge_Object=MibScalar
ipRouteAge=_IpRouteAge_Object((1,3,6,1,2,1,4,21,1,10),_IpRouteAge_Type())
ipRouteAge.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteAge.setStatus(_E)
_IpRouteMask_Type=IpAddress
_IpRouteMask_Object=MibScalar
ipRouteMask=_IpRouteMask_Object((1,3,6,1,2,1,4,21,1,11),_IpRouteMask_Type())
ipRouteMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteMask.setStatus(_E)
_IpRouteMetric5_Type=Integer32
_IpRouteMetric5_Object=MibScalar
ipRouteMetric5=_IpRouteMetric5_Object((1,3,6,1,2,1,4,21,1,12),_IpRouteMetric5_Type())
ipRouteMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteMetric5.setStatus(_E)
_IpRouteInfo_Type=ObjectIdentifier
_IpRouteInfo_Object=MibScalar
ipRouteInfo=_IpRouteInfo_Object((1,3,6,1,2,1,4,21,1,13),_IpRouteInfo_Type())
ipRouteInfo.setMaxAccess(_A)
if mibBuilder.loadTexts:ipRouteInfo.setStatus(_E)
_IpNetToMediaTable_ObjectIdentity=ObjectIdentity
ipNetToMediaTable=_IpNetToMediaTable_ObjectIdentity((1,3,6,1,2,1,4,22))
_IpNetToMediaEntry_ObjectIdentity=ObjectIdentity
ipNetToMediaEntry=_IpNetToMediaEntry_ObjectIdentity((1,3,6,1,2,1,4,22,1))
_IpNetToMediaIfIndex_Type=Integer32
_IpNetToMediaIfIndex_Object=MibScalar
ipNetToMediaIfIndex=_IpNetToMediaIfIndex_Object((1,3,6,1,2,1,4,22,1,1),_IpNetToMediaIfIndex_Type())
ipNetToMediaIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaIfIndex.setStatus(_E)
_IpNetToMediaPhysAddress_Type=PhysAddress
_IpNetToMediaPhysAddress_Object=MibScalar
ipNetToMediaPhysAddress=_IpNetToMediaPhysAddress_Object((1,3,6,1,2,1,4,22,1,2),_IpNetToMediaPhysAddress_Type())
ipNetToMediaPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaPhysAddress.setStatus(_E)
_IpNetToMediaNetAddress_Type=IpAddress
_IpNetToMediaNetAddress_Object=MibScalar
ipNetToMediaNetAddress=_IpNetToMediaNetAddress_Object((1,3,6,1,2,1,4,22,1,3),_IpNetToMediaNetAddress_Type())
ipNetToMediaNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaNetAddress.setStatus(_E)
class _IpNetToMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_T,2),('dynamic',3),('static',4)))
_IpNetToMediaType_Type.__name__=_D
_IpNetToMediaType_Object=MibScalar
ipNetToMediaType=_IpNetToMediaType_Object((1,3,6,1,2,1,4,22,1,4),_IpNetToMediaType_Type())
ipNetToMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaType.setStatus(_E)
_IpRoutingDiscards_Type=Counter32
_IpRoutingDiscards_Object=MibScalar
ipRoutingDiscards=_IpRoutingDiscards_Object((1,3,6,1,2,1,4,23),_IpRoutingDiscards_Type())
ipRoutingDiscards.setMaxAccess(_A)
if mibBuilder.loadTexts:ipRoutingDiscards.setStatus(_E)
_Icmp_ObjectIdentity=ObjectIdentity
icmp=_Icmp_ObjectIdentity((1,3,6,1,2,1,5))
_IcmpInMsgs_Type=Counter32
_IcmpInMsgs_Object=MibScalar
icmpInMsgs=_IcmpInMsgs_Object((1,3,6,1,2,1,5,1),_IcmpInMsgs_Type())
icmpInMsgs.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInMsgs.setStatus(_E)
_IcmpInErrors_Type=Counter32
_IcmpInErrors_Object=MibScalar
icmpInErrors=_IcmpInErrors_Object((1,3,6,1,2,1,5,2),_IcmpInErrors_Type())
icmpInErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInErrors.setStatus(_E)
_IcmpInDestUnreachs_Type=Counter32
_IcmpInDestUnreachs_Object=MibScalar
icmpInDestUnreachs=_IcmpInDestUnreachs_Object((1,3,6,1,2,1,5,3),_IcmpInDestUnreachs_Type())
icmpInDestUnreachs.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInDestUnreachs.setStatus(_E)
_IcmpInTimeExcds_Type=Counter32
_IcmpInTimeExcds_Object=MibScalar
icmpInTimeExcds=_IcmpInTimeExcds_Object((1,3,6,1,2,1,5,4),_IcmpInTimeExcds_Type())
icmpInTimeExcds.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInTimeExcds.setStatus(_E)
_IcmpInParmProbs_Type=Counter32
_IcmpInParmProbs_Object=MibScalar
icmpInParmProbs=_IcmpInParmProbs_Object((1,3,6,1,2,1,5,5),_IcmpInParmProbs_Type())
icmpInParmProbs.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInParmProbs.setStatus(_E)
_IcmpInSrcQuenchs_Type=Counter32
_IcmpInSrcQuenchs_Object=MibScalar
icmpInSrcQuenchs=_IcmpInSrcQuenchs_Object((1,3,6,1,2,1,5,6),_IcmpInSrcQuenchs_Type())
icmpInSrcQuenchs.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInSrcQuenchs.setStatus(_E)
_IcmpInRedirects_Type=Counter32
_IcmpInRedirects_Object=MibScalar
icmpInRedirects=_IcmpInRedirects_Object((1,3,6,1,2,1,5,7),_IcmpInRedirects_Type())
icmpInRedirects.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInRedirects.setStatus(_E)
_IcmpInEchos_Type=Counter32
_IcmpInEchos_Object=MibScalar
icmpInEchos=_IcmpInEchos_Object((1,3,6,1,2,1,5,8),_IcmpInEchos_Type())
icmpInEchos.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInEchos.setStatus(_E)
_IcmpInEchoReps_Type=Counter32
_IcmpInEchoReps_Object=MibScalar
icmpInEchoReps=_IcmpInEchoReps_Object((1,3,6,1,2,1,5,9),_IcmpInEchoReps_Type())
icmpInEchoReps.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInEchoReps.setStatus(_E)
_IcmpInTimestamps_Type=Counter32
_IcmpInTimestamps_Object=MibScalar
icmpInTimestamps=_IcmpInTimestamps_Object((1,3,6,1,2,1,5,10),_IcmpInTimestamps_Type())
icmpInTimestamps.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInTimestamps.setStatus(_E)
_IcmpInTimestampReps_Type=Counter32
_IcmpInTimestampReps_Object=MibScalar
icmpInTimestampReps=_IcmpInTimestampReps_Object((1,3,6,1,2,1,5,11),_IcmpInTimestampReps_Type())
icmpInTimestampReps.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInTimestampReps.setStatus(_E)
_IcmpInAddrMasks_Type=Counter32
_IcmpInAddrMasks_Object=MibScalar
icmpInAddrMasks=_IcmpInAddrMasks_Object((1,3,6,1,2,1,5,12),_IcmpInAddrMasks_Type())
icmpInAddrMasks.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInAddrMasks.setStatus(_E)
_IcmpInAddrMaskReps_Type=Counter32
_IcmpInAddrMaskReps_Object=MibScalar
icmpInAddrMaskReps=_IcmpInAddrMaskReps_Object((1,3,6,1,2,1,5,13),_IcmpInAddrMaskReps_Type())
icmpInAddrMaskReps.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpInAddrMaskReps.setStatus(_E)
_IcmpOutMsgs_Type=Counter32
_IcmpOutMsgs_Object=MibScalar
icmpOutMsgs=_IcmpOutMsgs_Object((1,3,6,1,2,1,5,14),_IcmpOutMsgs_Type())
icmpOutMsgs.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutMsgs.setStatus(_E)
_IcmpOutErrors_Type=Counter32
_IcmpOutErrors_Object=MibScalar
icmpOutErrors=_IcmpOutErrors_Object((1,3,6,1,2,1,5,15),_IcmpOutErrors_Type())
icmpOutErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutErrors.setStatus(_E)
_IcmpOutDestUnreachs_Type=Counter32
_IcmpOutDestUnreachs_Object=MibScalar
icmpOutDestUnreachs=_IcmpOutDestUnreachs_Object((1,3,6,1,2,1,5,16),_IcmpOutDestUnreachs_Type())
icmpOutDestUnreachs.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutDestUnreachs.setStatus(_E)
_IcmpOutTimeExcds_Type=Counter32
_IcmpOutTimeExcds_Object=MibScalar
icmpOutTimeExcds=_IcmpOutTimeExcds_Object((1,3,6,1,2,1,5,17),_IcmpOutTimeExcds_Type())
icmpOutTimeExcds.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutTimeExcds.setStatus(_E)
_IcmpOutParmProbs_Type=Counter32
_IcmpOutParmProbs_Object=MibScalar
icmpOutParmProbs=_IcmpOutParmProbs_Object((1,3,6,1,2,1,5,18),_IcmpOutParmProbs_Type())
icmpOutParmProbs.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutParmProbs.setStatus(_E)
_IcmpOutSrcQuenchs_Type=Counter32
_IcmpOutSrcQuenchs_Object=MibScalar
icmpOutSrcQuenchs=_IcmpOutSrcQuenchs_Object((1,3,6,1,2,1,5,19),_IcmpOutSrcQuenchs_Type())
icmpOutSrcQuenchs.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutSrcQuenchs.setStatus(_E)
_IcmpOutRedirects_Type=Counter32
_IcmpOutRedirects_Object=MibScalar
icmpOutRedirects=_IcmpOutRedirects_Object((1,3,6,1,2,1,5,20),_IcmpOutRedirects_Type())
icmpOutRedirects.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutRedirects.setStatus(_E)
_IcmpOutEchos_Type=Counter32
_IcmpOutEchos_Object=MibScalar
icmpOutEchos=_IcmpOutEchos_Object((1,3,6,1,2,1,5,21),_IcmpOutEchos_Type())
icmpOutEchos.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutEchos.setStatus(_E)
_IcmpOutEchoReps_Type=Counter32
_IcmpOutEchoReps_Object=MibScalar
icmpOutEchoReps=_IcmpOutEchoReps_Object((1,3,6,1,2,1,5,22),_IcmpOutEchoReps_Type())
icmpOutEchoReps.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutEchoReps.setStatus(_E)
_IcmpOutTimestamps_Type=Counter32
_IcmpOutTimestamps_Object=MibScalar
icmpOutTimestamps=_IcmpOutTimestamps_Object((1,3,6,1,2,1,5,23),_IcmpOutTimestamps_Type())
icmpOutTimestamps.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutTimestamps.setStatus(_E)
_IcmpOutTimestampReps_Type=Counter32
_IcmpOutTimestampReps_Object=MibScalar
icmpOutTimestampReps=_IcmpOutTimestampReps_Object((1,3,6,1,2,1,5,24),_IcmpOutTimestampReps_Type())
icmpOutTimestampReps.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutTimestampReps.setStatus(_E)
_IcmpOutAddrMasks_Type=Counter32
_IcmpOutAddrMasks_Object=MibScalar
icmpOutAddrMasks=_IcmpOutAddrMasks_Object((1,3,6,1,2,1,5,25),_IcmpOutAddrMasks_Type())
icmpOutAddrMasks.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutAddrMasks.setStatus(_E)
_IcmpOutAddrMaskReps_Type=Counter32
_IcmpOutAddrMaskReps_Object=MibScalar
icmpOutAddrMaskReps=_IcmpOutAddrMaskReps_Object((1,3,6,1,2,1,5,26),_IcmpOutAddrMaskReps_Type())
icmpOutAddrMaskReps.setMaxAccess(_A)
if mibBuilder.loadTexts:icmpOutAddrMaskReps.setStatus(_E)
_Tcp_ObjectIdentity=ObjectIdentity
tcp=_Tcp_ObjectIdentity((1,3,6,1,2,1,6))
class _TcpRtoAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('constant',2),('rsre',3),('vanj',4)))
_TcpRtoAlgorithm_Type.__name__=_D
_TcpRtoAlgorithm_Object=MibScalar
tcpRtoAlgorithm=_TcpRtoAlgorithm_Object((1,3,6,1,2,1,6,1),_TcpRtoAlgorithm_Type())
tcpRtoAlgorithm.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpRtoAlgorithm.setStatus(_E)
_TcpRtoMin_Type=Integer32
_TcpRtoMin_Object=MibScalar
tcpRtoMin=_TcpRtoMin_Object((1,3,6,1,2,1,6,2),_TcpRtoMin_Type())
tcpRtoMin.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpRtoMin.setStatus(_E)
_TcpRtoMax_Type=Integer32
_TcpRtoMax_Object=MibScalar
tcpRtoMax=_TcpRtoMax_Object((1,3,6,1,2,1,6,3),_TcpRtoMax_Type())
tcpRtoMax.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpRtoMax.setStatus(_E)
_TcpMaxConn_Type=Integer32
_TcpMaxConn_Object=MibScalar
tcpMaxConn=_TcpMaxConn_Object((1,3,6,1,2,1,6,4),_TcpMaxConn_Type())
tcpMaxConn.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpMaxConn.setStatus(_E)
_TcpActiveOpens_Type=Counter32
_TcpActiveOpens_Object=MibScalar
tcpActiveOpens=_TcpActiveOpens_Object((1,3,6,1,2,1,6,5),_TcpActiveOpens_Type())
tcpActiveOpens.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpActiveOpens.setStatus(_E)
_TcpPassiveOpens_Type=Counter32
_TcpPassiveOpens_Object=MibScalar
tcpPassiveOpens=_TcpPassiveOpens_Object((1,3,6,1,2,1,6,6),_TcpPassiveOpens_Type())
tcpPassiveOpens.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpPassiveOpens.setStatus(_E)
_TcpAttemptFails_Type=Counter32
_TcpAttemptFails_Object=MibScalar
tcpAttemptFails=_TcpAttemptFails_Object((1,3,6,1,2,1,6,7),_TcpAttemptFails_Type())
tcpAttemptFails.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpAttemptFails.setStatus(_E)
_TcpEstabResets_Type=Counter32
_TcpEstabResets_Object=MibScalar
tcpEstabResets=_TcpEstabResets_Object((1,3,6,1,2,1,6,8),_TcpEstabResets_Type())
tcpEstabResets.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpEstabResets.setStatus(_E)
_TcpCurrEstab_Type=Gauge32
_TcpCurrEstab_Object=MibScalar
tcpCurrEstab=_TcpCurrEstab_Object((1,3,6,1,2,1,6,9),_TcpCurrEstab_Type())
tcpCurrEstab.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpCurrEstab.setStatus(_E)
_TcpInSegs_Type=Counter32
_TcpInSegs_Object=MibScalar
tcpInSegs=_TcpInSegs_Object((1,3,6,1,2,1,6,10),_TcpInSegs_Type())
tcpInSegs.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpInSegs.setStatus(_E)
_TcpOutSegs_Type=Counter32
_TcpOutSegs_Object=MibScalar
tcpOutSegs=_TcpOutSegs_Object((1,3,6,1,2,1,6,11),_TcpOutSegs_Type())
tcpOutSegs.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpOutSegs.setStatus(_E)
_TcpRetransSegs_Type=Counter32
_TcpRetransSegs_Object=MibScalar
tcpRetransSegs=_TcpRetransSegs_Object((1,3,6,1,2,1,6,12),_TcpRetransSegs_Type())
tcpRetransSegs.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpRetransSegs.setStatus(_E)
_TcpConnTable_ObjectIdentity=ObjectIdentity
tcpConnTable=_TcpConnTable_ObjectIdentity((1,3,6,1,2,1,6,13))
_TcpConnEntry_ObjectIdentity=ObjectIdentity
tcpConnEntry=_TcpConnEntry_ObjectIdentity((1,3,6,1,2,1,6,13,1))
class _TcpConnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('closed',1),('listen',2),('synSent',3),('synReceived',4),('established',5),('finWait1',6),('finWait2',7),('closeWait',8),('lastAck',9),('closing',10),('timeWait',11),('deleteTCB',12)))
_TcpConnState_Type.__name__=_D
_TcpConnState_Object=MibScalar
tcpConnState=_TcpConnState_Object((1,3,6,1,2,1,6,13,1,1),_TcpConnState_Type())
tcpConnState.setMaxAccess(_C)
if mibBuilder.loadTexts:tcpConnState.setStatus(_E)
_TcpConnLocalAddress_Type=IpAddress
_TcpConnLocalAddress_Object=MibScalar
tcpConnLocalAddress=_TcpConnLocalAddress_Object((1,3,6,1,2,1,6,13,1,2),_TcpConnLocalAddress_Type())
tcpConnLocalAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpConnLocalAddress.setStatus(_E)
class _TcpConnLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TcpConnLocalPort_Type.__name__=_D
_TcpConnLocalPort_Object=MibScalar
tcpConnLocalPort=_TcpConnLocalPort_Object((1,3,6,1,2,1,6,13,1,3),_TcpConnLocalPort_Type())
tcpConnLocalPort.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpConnLocalPort.setStatus(_E)
_TcpConnRemAddress_Type=IpAddress
_TcpConnRemAddress_Object=MibScalar
tcpConnRemAddress=_TcpConnRemAddress_Object((1,3,6,1,2,1,6,13,1,4),_TcpConnRemAddress_Type())
tcpConnRemAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpConnRemAddress.setStatus(_E)
class _TcpConnRemPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TcpConnRemPort_Type.__name__=_D
_TcpConnRemPort_Object=MibScalar
tcpConnRemPort=_TcpConnRemPort_Object((1,3,6,1,2,1,6,13,1,5),_TcpConnRemPort_Type())
tcpConnRemPort.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpConnRemPort.setStatus(_E)
_TcpInErrs_Type=Counter32
_TcpInErrs_Object=MibScalar
tcpInErrs=_TcpInErrs_Object((1,3,6,1,2,1,6,14),_TcpInErrs_Type())
tcpInErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpInErrs.setStatus(_E)
_TcpOutRsts_Type=Counter32
_TcpOutRsts_Object=MibScalar
tcpOutRsts=_TcpOutRsts_Object((1,3,6,1,2,1,6,15),_TcpOutRsts_Type())
tcpOutRsts.setMaxAccess(_A)
if mibBuilder.loadTexts:tcpOutRsts.setStatus(_E)
_Udp_ObjectIdentity=ObjectIdentity
udp=_Udp_ObjectIdentity((1,3,6,1,2,1,7))
_UdpInDatagrams_Type=Counter32
_UdpInDatagrams_Object=MibScalar
udpInDatagrams=_UdpInDatagrams_Object((1,3,6,1,2,1,7,1),_UdpInDatagrams_Type())
udpInDatagrams.setMaxAccess(_A)
if mibBuilder.loadTexts:udpInDatagrams.setStatus(_B)
_UdpNoPorts_Type=Counter32
_UdpNoPorts_Object=MibScalar
udpNoPorts=_UdpNoPorts_Object((1,3,6,1,2,1,7,2),_UdpNoPorts_Type())
udpNoPorts.setMaxAccess(_A)
if mibBuilder.loadTexts:udpNoPorts.setStatus(_B)
_UdpInErrors_Type=Counter32
_UdpInErrors_Object=MibScalar
udpInErrors=_UdpInErrors_Object((1,3,6,1,2,1,7,3),_UdpInErrors_Type())
udpInErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:udpInErrors.setStatus(_B)
_UdpOutDatagrams_Type=Counter32
_UdpOutDatagrams_Object=MibScalar
udpOutDatagrams=_UdpOutDatagrams_Object((1,3,6,1,2,1,7,4),_UdpOutDatagrams_Type())
udpOutDatagrams.setMaxAccess(_A)
if mibBuilder.loadTexts:udpOutDatagrams.setStatus(_B)
_UdpTable_ObjectIdentity=ObjectIdentity
udpTable=_UdpTable_ObjectIdentity((1,3,6,1,2,1,7,5))
_UdpEntry_ObjectIdentity=ObjectIdentity
udpEntry=_UdpEntry_ObjectIdentity((1,3,6,1,2,1,7,5,1))
_UdpLocalAddress_Type=IpAddress
_UdpLocalAddress_Object=MibScalar
udpLocalAddress=_UdpLocalAddress_Object((1,3,6,1,2,1,7,5,1,1),_UdpLocalAddress_Type())
udpLocalAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:udpLocalAddress.setStatus(_I)
class _UdpLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UdpLocalPort_Type.__name__=_D
_UdpLocalPort_Object=MibScalar
udpLocalPort=_UdpLocalPort_Object((1,3,6,1,2,1,7,5,1,2),_UdpLocalPort_Type())
udpLocalPort.setMaxAccess(_A)
if mibBuilder.loadTexts:udpLocalPort.setStatus(_I)
_Snmp_ObjectIdentity=ObjectIdentity
snmp=_Snmp_ObjectIdentity((1,3,6,1,2,1,11))
_SnmpInPkts_Type=Counter32
_SnmpInPkts_Object=MibScalar
snmpInPkts=_SnmpInPkts_Object((1,3,6,1,2,1,11,1),_SnmpInPkts_Type())
snmpInPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInPkts.setStatus(_E)
_SnmpOutPkts_Type=Counter32
_SnmpOutPkts_Object=MibScalar
snmpOutPkts=_SnmpOutPkts_Object((1,3,6,1,2,1,11,2),_SnmpOutPkts_Type())
snmpOutPkts.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutPkts.setStatus(_E)
_SnmpInBadVersions_Type=Counter32
_SnmpInBadVersions_Object=MibScalar
snmpInBadVersions=_SnmpInBadVersions_Object((1,3,6,1,2,1,11,3),_SnmpInBadVersions_Type())
snmpInBadVersions.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInBadVersions.setStatus(_E)
_SnmpInBadCommunityNames_Type=Counter32
_SnmpInBadCommunityNames_Object=MibScalar
snmpInBadCommunityNames=_SnmpInBadCommunityNames_Object((1,3,6,1,2,1,11,4),_SnmpInBadCommunityNames_Type())
snmpInBadCommunityNames.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInBadCommunityNames.setStatus(_E)
_SnmpInBadCommunityUses_Type=Counter32
_SnmpInBadCommunityUses_Object=MibScalar
snmpInBadCommunityUses=_SnmpInBadCommunityUses_Object((1,3,6,1,2,1,11,5),_SnmpInBadCommunityUses_Type())
snmpInBadCommunityUses.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInBadCommunityUses.setStatus(_E)
_SnmpInASNParseErrs_Type=Counter32
_SnmpInASNParseErrs_Object=MibScalar
snmpInASNParseErrs=_SnmpInASNParseErrs_Object((1,3,6,1,2,1,11,6),_SnmpInASNParseErrs_Type())
snmpInASNParseErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInASNParseErrs.setStatus(_E)
_SnmpInTooBigs_Type=Counter32
_SnmpInTooBigs_Object=MibScalar
snmpInTooBigs=_SnmpInTooBigs_Object((1,3,6,1,2,1,11,8),_SnmpInTooBigs_Type())
snmpInTooBigs.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInTooBigs.setStatus(_E)
_SnmpInNoSuchNames_Type=Counter32
_SnmpInNoSuchNames_Object=MibScalar
snmpInNoSuchNames=_SnmpInNoSuchNames_Object((1,3,6,1,2,1,11,9),_SnmpInNoSuchNames_Type())
snmpInNoSuchNames.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInNoSuchNames.setStatus(_E)
_SnmpInBadValues_Type=Counter32
_SnmpInBadValues_Object=MibScalar
snmpInBadValues=_SnmpInBadValues_Object((1,3,6,1,2,1,11,10),_SnmpInBadValues_Type())
snmpInBadValues.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInBadValues.setStatus(_E)
_SnmpInReadOnlys_Type=Counter32
_SnmpInReadOnlys_Object=MibScalar
snmpInReadOnlys=_SnmpInReadOnlys_Object((1,3,6,1,2,1,11,11),_SnmpInReadOnlys_Type())
snmpInReadOnlys.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInReadOnlys.setStatus(_E)
_SnmpInGenErrs_Type=Counter32
_SnmpInGenErrs_Object=MibScalar
snmpInGenErrs=_SnmpInGenErrs_Object((1,3,6,1,2,1,11,12),_SnmpInGenErrs_Type())
snmpInGenErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInGenErrs.setStatus(_E)
_SnmpInTotalReqVars_Type=Counter32
_SnmpInTotalReqVars_Object=MibScalar
snmpInTotalReqVars=_SnmpInTotalReqVars_Object((1,3,6,1,2,1,11,13),_SnmpInTotalReqVars_Type())
snmpInTotalReqVars.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInTotalReqVars.setStatus(_E)
_SnmpInTotalSetVars_Type=Counter32
_SnmpInTotalSetVars_Object=MibScalar
snmpInTotalSetVars=_SnmpInTotalSetVars_Object((1,3,6,1,2,1,11,14),_SnmpInTotalSetVars_Type())
snmpInTotalSetVars.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInTotalSetVars.setStatus(_E)
_SnmpInGetRequests_Type=Counter32
_SnmpInGetRequests_Object=MibScalar
snmpInGetRequests=_SnmpInGetRequests_Object((1,3,6,1,2,1,11,15),_SnmpInGetRequests_Type())
snmpInGetRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInGetRequests.setStatus(_E)
_SnmpInGetNexts_Type=Counter32
_SnmpInGetNexts_Object=MibScalar
snmpInGetNexts=_SnmpInGetNexts_Object((1,3,6,1,2,1,11,16),_SnmpInGetNexts_Type())
snmpInGetNexts.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInGetNexts.setStatus(_E)
_SnmpInSetRequests_Type=Counter32
_SnmpInSetRequests_Object=MibScalar
snmpInSetRequests=_SnmpInSetRequests_Object((1,3,6,1,2,1,11,17),_SnmpInSetRequests_Type())
snmpInSetRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInSetRequests.setStatus(_E)
_SnmpInGetResponses_Type=Counter32
_SnmpInGetResponses_Object=MibScalar
snmpInGetResponses=_SnmpInGetResponses_Object((1,3,6,1,2,1,11,18),_SnmpInGetResponses_Type())
snmpInGetResponses.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInGetResponses.setStatus(_E)
_SnmpInTraps_Type=Counter32
_SnmpInTraps_Object=MibScalar
snmpInTraps=_SnmpInTraps_Object((1,3,6,1,2,1,11,19),_SnmpInTraps_Type())
snmpInTraps.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpInTraps.setStatus(_E)
_SnmpOutTooBigs_Type=Counter32
_SnmpOutTooBigs_Object=MibScalar
snmpOutTooBigs=_SnmpOutTooBigs_Object((1,3,6,1,2,1,11,20),_SnmpOutTooBigs_Type())
snmpOutTooBigs.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutTooBigs.setStatus(_E)
_SnmpOutNoSuchNames_Type=Counter32
_SnmpOutNoSuchNames_Object=MibScalar
snmpOutNoSuchNames=_SnmpOutNoSuchNames_Object((1,3,6,1,2,1,11,21),_SnmpOutNoSuchNames_Type())
snmpOutNoSuchNames.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutNoSuchNames.setStatus(_E)
_SnmpOutBadValues_Type=Counter32
_SnmpOutBadValues_Object=MibScalar
snmpOutBadValues=_SnmpOutBadValues_Object((1,3,6,1,2,1,11,22),_SnmpOutBadValues_Type())
snmpOutBadValues.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutBadValues.setStatus(_E)
_SnmpOutGenErrs_Type=Counter32
_SnmpOutGenErrs_Object=MibScalar
snmpOutGenErrs=_SnmpOutGenErrs_Object((1,3,6,1,2,1,11,24),_SnmpOutGenErrs_Type())
snmpOutGenErrs.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutGenErrs.setStatus(_E)
_SnmpOutGetRequests_Type=Counter32
_SnmpOutGetRequests_Object=MibScalar
snmpOutGetRequests=_SnmpOutGetRequests_Object((1,3,6,1,2,1,11,25),_SnmpOutGetRequests_Type())
snmpOutGetRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutGetRequests.setStatus(_E)
_SnmpOutGetNexts_Type=Counter32
_SnmpOutGetNexts_Object=MibScalar
snmpOutGetNexts=_SnmpOutGetNexts_Object((1,3,6,1,2,1,11,26),_SnmpOutGetNexts_Type())
snmpOutGetNexts.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutGetNexts.setStatus(_E)
_SnmpOutSetRequests_Type=Counter32
_SnmpOutSetRequests_Object=MibScalar
snmpOutSetRequests=_SnmpOutSetRequests_Object((1,3,6,1,2,1,11,27),_SnmpOutSetRequests_Type())
snmpOutSetRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutSetRequests.setStatus(_E)
_SnmpOutGetResponses_Type=Counter32
_SnmpOutGetResponses_Object=MibScalar
snmpOutGetResponses=_SnmpOutGetResponses_Object((1,3,6,1,2,1,11,28),_SnmpOutGetResponses_Type())
snmpOutGetResponses.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutGetResponses.setStatus(_E)
_SnmpOutTraps_Type=Counter32
_SnmpOutTraps_Object=MibScalar
snmpOutTraps=_SnmpOutTraps_Object((1,3,6,1,2,1,11,29),_SnmpOutTraps_Type())
snmpOutTraps.setMaxAccess(_A)
if mibBuilder.loadTexts:snmpOutTraps.setStatus(_E)
class _SnmpEnableAuthenTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_SnmpEnableAuthenTraps_Type.__name__=_D
_SnmpEnableAuthenTraps_Object=MibScalar
snmpEnableAuthenTraps=_SnmpEnableAuthenTraps_Object((1,3,6,1,2,1,11,30),_SnmpEnableAuthenTraps_Type())
snmpEnableAuthenTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpEnableAuthenTraps.setStatus(_E)
_Host_ObjectIdentity=ObjectIdentity
host=_Host_ObjectIdentity((1,3,6,1,2,1,25))
_HrSystem_ObjectIdentity=ObjectIdentity
hrSystem=_HrSystem_ObjectIdentity((1,3,6,1,2,1,25,1))
_HrSystemUptime_Type=TimeTicks
_HrSystemUptime_Object=MibScalar
hrSystemUptime=_HrSystemUptime_Object((1,3,6,1,2,1,25,1,1),_HrSystemUptime_Type())
hrSystemUptime.setMaxAccess(_A)
if mibBuilder.loadTexts:hrSystemUptime.setStatus(_B)
_HrStorage_ObjectIdentity=ObjectIdentity
hrStorage=_HrStorage_ObjectIdentity((1,3,6,1,2,1,25,2))
_HrMemorySize_Type=KBytes
_HrMemorySize_Object=MibScalar
hrMemorySize=_HrMemorySize_Object((1,3,6,1,2,1,25,2,2),_HrMemorySize_Type())
hrMemorySize.setMaxAccess(_A)
if mibBuilder.loadTexts:hrMemorySize.setStatus(_B)
if mibBuilder.loadTexts:hrMemorySize.setUnits(_Z)
_HrStorageTable_ObjectIdentity=ObjectIdentity
hrStorageTable=_HrStorageTable_ObjectIdentity((1,3,6,1,2,1,25,2,3))
_HrStorageEntry_ObjectIdentity=ObjectIdentity
hrStorageEntry=_HrStorageEntry_ObjectIdentity((1,3,6,1,2,1,25,2,3,1))
class _HrStorageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HrStorageIndex_Type.__name__=_D
_HrStorageIndex_Object=MibScalar
hrStorageIndex=_HrStorageIndex_Object((1,3,6,1,2,1,25,2,3,1,1),_HrStorageIndex_Type())
hrStorageIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:hrStorageIndex.setStatus(_B)
_HrStorageType_Type=AutonomousType
_HrStorageType_Object=MibScalar
hrStorageType=_HrStorageType_Object((1,3,6,1,2,1,25,2,3,1,2),_HrStorageType_Type())
hrStorageType.setMaxAccess(_A)
if mibBuilder.loadTexts:hrStorageType.setStatus(_B)
_HrStorageDescr_Type=DisplayString
_HrStorageDescr_Object=MibScalar
hrStorageDescr=_HrStorageDescr_Object((1,3,6,1,2,1,25,2,3,1,3),_HrStorageDescr_Type())
hrStorageDescr.setMaxAccess(_A)
if mibBuilder.loadTexts:hrStorageDescr.setStatus(_B)
class _HrStorageAllocationUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HrStorageAllocationUnits_Type.__name__=_D
_HrStorageAllocationUnits_Object=MibScalar
hrStorageAllocationUnits=_HrStorageAllocationUnits_Object((1,3,6,1,2,1,25,2,3,1,4),_HrStorageAllocationUnits_Type())
hrStorageAllocationUnits.setMaxAccess(_A)
if mibBuilder.loadTexts:hrStorageAllocationUnits.setStatus(_B)
if mibBuilder.loadTexts:hrStorageAllocationUnits.setUnits('Bytes')
class _HrStorageSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HrStorageSize_Type.__name__=_D
_HrStorageSize_Object=MibScalar
hrStorageSize=_HrStorageSize_Object((1,3,6,1,2,1,25,2,3,1,5),_HrStorageSize_Type())
hrStorageSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hrStorageSize.setStatus(_B)
class _HrStorageUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HrStorageUsed_Type.__name__=_D
_HrStorageUsed_Object=MibScalar
hrStorageUsed=_HrStorageUsed_Object((1,3,6,1,2,1,25,2,3,1,6),_HrStorageUsed_Type())
hrStorageUsed.setMaxAccess(_A)
if mibBuilder.loadTexts:hrStorageUsed.setStatus(_B)
_HrStorageAllocationFailures_Type=Counter32
_HrStorageAllocationFailures_Object=MibScalar
hrStorageAllocationFailures=_HrStorageAllocationFailures_Object((1,3,6,1,2,1,25,2,3,1,7),_HrStorageAllocationFailures_Type())
hrStorageAllocationFailures.setMaxAccess(_A)
if mibBuilder.loadTexts:hrStorageAllocationFailures.setStatus(_B)
_HrDevice_ObjectIdentity=ObjectIdentity
hrDevice=_HrDevice_ObjectIdentity((1,3,6,1,2,1,25,3))
_HrDeviceTable_ObjectIdentity=ObjectIdentity
hrDeviceTable=_HrDeviceTable_ObjectIdentity((1,3,6,1,2,1,25,3,2))
_HrDeviceEntry_ObjectIdentity=ObjectIdentity
hrDeviceEntry=_HrDeviceEntry_ObjectIdentity((1,3,6,1,2,1,25,3,2,1))
class _HrDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HrDeviceIndex_Type.__name__=_D
_HrDeviceIndex_Object=MibScalar
hrDeviceIndex=_HrDeviceIndex_Object((1,3,6,1,2,1,25,3,2,1,1),_HrDeviceIndex_Type())
hrDeviceIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:hrDeviceIndex.setStatus(_B)
_HrDeviceType_Type=AutonomousType
_HrDeviceType_Object=MibScalar
hrDeviceType=_HrDeviceType_Object((1,3,6,1,2,1,25,3,2,1,2),_HrDeviceType_Type())
hrDeviceType.setMaxAccess(_A)
if mibBuilder.loadTexts:hrDeviceType.setStatus(_B)
class _HrDeviceDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HrDeviceDescr_Type.__name__=_H
_HrDeviceDescr_Object=MibScalar
hrDeviceDescr=_HrDeviceDescr_Object((1,3,6,1,2,1,25,3,2,1,3),_HrDeviceDescr_Type())
hrDeviceDescr.setMaxAccess(_A)
if mibBuilder.loadTexts:hrDeviceDescr.setStatus(_B)
_HrDeviceID_Type=ProductID
_HrDeviceID_Object=MibScalar
hrDeviceID=_HrDeviceID_Object((1,3,6,1,2,1,25,3,2,1,4),_HrDeviceID_Type())
hrDeviceID.setMaxAccess(_A)
if mibBuilder.loadTexts:hrDeviceID.setStatus(_B)
class _HrDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),('running',2),('warning',3),(_S,4),(_R,5)))
_HrDeviceStatus_Type.__name__=_D
_HrDeviceStatus_Object=MibScalar
hrDeviceStatus=_HrDeviceStatus_Object((1,3,6,1,2,1,25,3,2,1,5),_HrDeviceStatus_Type())
hrDeviceStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:hrDeviceStatus.setStatus(_B)
_HrDeviceErrors_Type=Counter32
_HrDeviceErrors_Object=MibScalar
hrDeviceErrors=_HrDeviceErrors_Object((1,3,6,1,2,1,25,3,2,1,6),_HrDeviceErrors_Type())
hrDeviceErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:hrDeviceErrors.setStatus(_B)
_HrPrinterTable_ObjectIdentity=ObjectIdentity
hrPrinterTable=_HrPrinterTable_ObjectIdentity((1,3,6,1,2,1,25,3,5))
_HrPrinterEntry_ObjectIdentity=ObjectIdentity
hrPrinterEntry=_HrPrinterEntry_ObjectIdentity((1,3,6,1,2,1,25,3,5,1))
class _HrPrinterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_Q,2),('idle',3),('printing',4),('warmup',5)))
_HrPrinterStatus_Type.__name__=_D
_HrPrinterStatus_Object=MibScalar
hrPrinterStatus=_HrPrinterStatus_Object((1,3,6,1,2,1,25,3,5,1,1),_HrPrinterStatus_Type())
hrPrinterStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:hrPrinterStatus.setStatus(_B)
_HrPrinterDetectedErrorState_Type=OctetString
_HrPrinterDetectedErrorState_Object=MibScalar
hrPrinterDetectedErrorState=_HrPrinterDetectedErrorState_Object((1,3,6,1,2,1,25,3,5,1,2),_HrPrinterDetectedErrorState_Type())
hrPrinterDetectedErrorState.setMaxAccess(_A)
if mibBuilder.loadTexts:hrPrinterDetectedErrorState.setStatus(_B)
_Printmib_ObjectIdentity=ObjectIdentity
printmib=_Printmib_ObjectIdentity((1,3,6,1,2,1,43))
_PrtGeneral_ObjectIdentity=ObjectIdentity
prtGeneral=_PrtGeneral_ObjectIdentity((1,3,6,1,2,1,43,5))
_PrtGeneralTable_ObjectIdentity=ObjectIdentity
prtGeneralTable=_PrtGeneralTable_ObjectIdentity((1,3,6,1,2,1,43,5,1))
_PrtGeneralEntry_ObjectIdentity=ObjectIdentity
prtGeneralEntry=_PrtGeneralEntry_ObjectIdentity((1,3,6,1,2,1,43,5,1,1))
_PrtGeneralConfigChanges_Type=Counter32
_PrtGeneralConfigChanges_Object=MibScalar
prtGeneralConfigChanges=_PrtGeneralConfigChanges_Object((1,3,6,1,2,1,43,5,1,1,1),_PrtGeneralConfigChanges_Type())
prtGeneralConfigChanges.setMaxAccess(_A)
if mibBuilder.loadTexts:prtGeneralConfigChanges.setStatus(_B)
class _PrtGeneralCurrentLocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtGeneralCurrentLocalization_Type.__name__=_D
_PrtGeneralCurrentLocalization_Object=MibScalar
prtGeneralCurrentLocalization=_PrtGeneralCurrentLocalization_Object((1,3,6,1,2,1,43,5,1,1,2),_PrtGeneralCurrentLocalization_Type())
prtGeneralCurrentLocalization.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralCurrentLocalization.setStatus(_B)
_PrtGeneralReset_Type=PrtGeneralResetTC
_PrtGeneralReset_Object=MibScalar
prtGeneralReset=_PrtGeneralReset_Object((1,3,6,1,2,1,43,5,1,1,3),_PrtGeneralReset_Type())
prtGeneralReset.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralReset.setStatus(_B)
class _PrtGeneralCurrentOperator_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PrtGeneralCurrentOperator_Type.__name__=_G
_PrtGeneralCurrentOperator_Object=MibScalar
prtGeneralCurrentOperator=_PrtGeneralCurrentOperator_Object((1,3,6,1,2,1,43,5,1,1,4),_PrtGeneralCurrentOperator_Type())
prtGeneralCurrentOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralCurrentOperator.setStatus(_B)
class _PrtGeneralServicePerson_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PrtGeneralServicePerson_Type.__name__=_G
_PrtGeneralServicePerson_Object=MibScalar
prtGeneralServicePerson=_PrtGeneralServicePerson_Object((1,3,6,1,2,1,43,5,1,1,5),_PrtGeneralServicePerson_Type())
prtGeneralServicePerson.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralServicePerson.setStatus(_B)
class _PrtInputDefaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtInputDefaultIndex_Type.__name__=_D
_PrtInputDefaultIndex_Object=MibScalar
prtInputDefaultIndex=_PrtInputDefaultIndex_Object((1,3,6,1,2,1,43,5,1,1,6),_PrtInputDefaultIndex_Type())
prtInputDefaultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputDefaultIndex.setStatus(_B)
class _PrtOutputDefaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtOutputDefaultIndex_Type.__name__=_D
_PrtOutputDefaultIndex_Object=MibScalar
prtOutputDefaultIndex=_PrtOutputDefaultIndex_Object((1,3,6,1,2,1,43,5,1,1,7),_PrtOutputDefaultIndex_Type())
prtOutputDefaultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputDefaultIndex.setStatus(_B)
class _PrtMarkerDefaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtMarkerDefaultIndex_Type.__name__=_D
_PrtMarkerDefaultIndex_Object=MibScalar
prtMarkerDefaultIndex=_PrtMarkerDefaultIndex_Object((1,3,6,1,2,1,43,5,1,1,8),_PrtMarkerDefaultIndex_Type())
prtMarkerDefaultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMarkerDefaultIndex.setStatus(_B)
class _PrtMediaPathDefaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtMediaPathDefaultIndex_Type.__name__=_D
_PrtMediaPathDefaultIndex_Object=MibScalar
prtMediaPathDefaultIndex=_PrtMediaPathDefaultIndex_Object((1,3,6,1,2,1,43,5,1,1,9),_PrtMediaPathDefaultIndex_Type())
prtMediaPathDefaultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMediaPathDefaultIndex.setStatus(_B)
class _PrtConsoleLocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtConsoleLocalization_Type.__name__=_D
_PrtConsoleLocalization_Object=MibScalar
prtConsoleLocalization=_PrtConsoleLocalization_Object((1,3,6,1,2,1,43,5,1,1,10),_PrtConsoleLocalization_Type())
prtConsoleLocalization.setMaxAccess(_C)
if mibBuilder.loadTexts:prtConsoleLocalization.setStatus(_B)
class _PrtConsoleNumberOfDisplayLines_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtConsoleNumberOfDisplayLines_Type.__name__=_D
_PrtConsoleNumberOfDisplayLines_Object=MibScalar
prtConsoleNumberOfDisplayLines=_PrtConsoleNumberOfDisplayLines_Object((1,3,6,1,2,1,43,5,1,1,11),_PrtConsoleNumberOfDisplayLines_Type())
prtConsoleNumberOfDisplayLines.setMaxAccess(_A)
if mibBuilder.loadTexts:prtConsoleNumberOfDisplayLines.setStatus(_B)
class _PrtConsoleNumberOfDisplayChars_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtConsoleNumberOfDisplayChars_Type.__name__=_D
_PrtConsoleNumberOfDisplayChars_Object=MibScalar
prtConsoleNumberOfDisplayChars=_PrtConsoleNumberOfDisplayChars_Object((1,3,6,1,2,1,43,5,1,1,12),_PrtConsoleNumberOfDisplayChars_Type())
prtConsoleNumberOfDisplayChars.setMaxAccess(_A)
if mibBuilder.loadTexts:prtConsoleNumberOfDisplayChars.setStatus(_B)
_PrtConsoleDisable_Type=PrtConsoleDisableTC
_PrtConsoleDisable_Object=MibScalar
prtConsoleDisable=_PrtConsoleDisable_Object((1,3,6,1,2,1,43,5,1,1,13),_PrtConsoleDisable_Type())
prtConsoleDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:prtConsoleDisable.setStatus(_B)
class _PrtGeneralPrinterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PrtGeneralPrinterName_Type.__name__=_G
_PrtGeneralPrinterName_Object=MibScalar
prtGeneralPrinterName=_PrtGeneralPrinterName_Object((1,3,6,1,2,1,43,5,1,1,16),_PrtGeneralPrinterName_Type())
prtGeneralPrinterName.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralPrinterName.setStatus(_B)
class _PrtGeneralSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtGeneralSerialNumber_Type.__name__=_G
_PrtGeneralSerialNumber_Object=MibScalar
prtGeneralSerialNumber=_PrtGeneralSerialNumber_Object((1,3,6,1,2,1,43,5,1,1,17),_PrtGeneralSerialNumber_Type())
prtGeneralSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralSerialNumber.setStatus(_B)
_PrtAlertCriticalEvents_Type=Counter32
_PrtAlertCriticalEvents_Object=MibScalar
prtAlertCriticalEvents=_PrtAlertCriticalEvents_Object((1,3,6,1,2,1,43,5,1,1,18),_PrtAlertCriticalEvents_Type())
prtAlertCriticalEvents.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertCriticalEvents.setStatus(_B)
_PrtAlertAllEvents_Type=Counter32
_PrtAlertAllEvents_Object=MibScalar
prtAlertAllEvents=_PrtAlertAllEvents_Object((1,3,6,1,2,1,43,5,1,1,19),_PrtAlertAllEvents_Type())
prtAlertAllEvents.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertAllEvents.setStatus(_B)
_PrtStorageRefTable_ObjectIdentity=ObjectIdentity
prtStorageRefTable=_PrtStorageRefTable_ObjectIdentity((1,3,6,1,2,1,43,5,2))
_PrtStorageRefEntry_ObjectIdentity=ObjectIdentity
prtStorageRefEntry=_PrtStorageRefEntry_ObjectIdentity((1,3,6,1,2,1,43,5,2,1))
class _PrtStorageRefIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PrtStorageRefIndex_Type.__name__=_D
_PrtStorageRefIndex_Object=MibScalar
prtStorageRefIndex=_PrtStorageRefIndex_Object((1,3,6,1,2,1,43,5,2,1,2),_PrtStorageRefIndex_Type())
prtStorageRefIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:prtStorageRefIndex.setStatus(_B)
_PrtDeviceRefTable_ObjectIdentity=ObjectIdentity
prtDeviceRefTable=_PrtDeviceRefTable_ObjectIdentity((1,3,6,1,2,1,43,5,3))
_PrtDeviceRefEntry_ObjectIdentity=ObjectIdentity
prtDeviceRefEntry=_PrtDeviceRefEntry_ObjectIdentity((1,3,6,1,2,1,43,5,3,1))
class _PrtDeviceRefIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PrtDeviceRefIndex_Type.__name__=_D
_PrtDeviceRefIndex_Object=MibScalar
prtDeviceRefIndex=_PrtDeviceRefIndex_Object((1,3,6,1,2,1,43,5,3,1,2),_PrtDeviceRefIndex_Type())
prtDeviceRefIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:prtDeviceRefIndex.setStatus(_B)
_PrtCover_ObjectIdentity=ObjectIdentity
prtCover=_PrtCover_ObjectIdentity((1,3,6,1,2,1,43,6))
_PrtCoverTable_ObjectIdentity=ObjectIdentity
prtCoverTable=_PrtCoverTable_ObjectIdentity((1,3,6,1,2,1,43,6,1))
_PrtCoverEntry_ObjectIdentity=ObjectIdentity
prtCoverEntry=_PrtCoverEntry_ObjectIdentity((1,3,6,1,2,1,43,6,1,1))
_PrtCoverDescription_Type=PrtLocalizedDescriptionStringTC
_PrtCoverDescription_Object=MibScalar
prtCoverDescription=_PrtCoverDescription_Object((1,3,6,1,2,1,43,6,1,1,2),_PrtCoverDescription_Type())
prtCoverDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:prtCoverDescription.setStatus(_B)
_PrtCoverStatus_Type=PrtCoverStatusTC
_PrtCoverStatus_Object=MibScalar
prtCoverStatus=_PrtCoverStatus_Object((1,3,6,1,2,1,43,6,1,1,3),_PrtCoverStatus_Type())
prtCoverStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:prtCoverStatus.setStatus(_B)
_PrtLocalization_ObjectIdentity=ObjectIdentity
prtLocalization=_PrtLocalization_ObjectIdentity((1,3,6,1,2,1,43,7))
_PrtLocalizationTable_ObjectIdentity=ObjectIdentity
prtLocalizationTable=_PrtLocalizationTable_ObjectIdentity((1,3,6,1,2,1,43,7,1))
_PrtLocalizationEntry_ObjectIdentity=ObjectIdentity
prtLocalizationEntry=_PrtLocalizationEntry_ObjectIdentity((1,3,6,1,2,1,43,7,1,1))
class _PrtLocalizationLanguage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_PrtLocalizationLanguage_Type.__name__=_G
_PrtLocalizationLanguage_Object=MibScalar
prtLocalizationLanguage=_PrtLocalizationLanguage_Object((1,3,6,1,2,1,43,7,1,1,2),_PrtLocalizationLanguage_Type())
prtLocalizationLanguage.setMaxAccess(_A)
if mibBuilder.loadTexts:prtLocalizationLanguage.setStatus(_B)
class _PrtLocalizationCountry_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_PrtLocalizationCountry_Type.__name__=_G
_PrtLocalizationCountry_Object=MibScalar
prtLocalizationCountry=_PrtLocalizationCountry_Object((1,3,6,1,2,1,43,7,1,1,3),_PrtLocalizationCountry_Type())
prtLocalizationCountry.setMaxAccess(_A)
if mibBuilder.loadTexts:prtLocalizationCountry.setStatus(_B)
_PrtLocalizationCharacterSet_Type=IANACharset
_PrtLocalizationCharacterSet_Object=MibScalar
prtLocalizationCharacterSet=_PrtLocalizationCharacterSet_Object((1,3,6,1,2,1,43,7,1,1,4),_PrtLocalizationCharacterSet_Type())
prtLocalizationCharacterSet.setMaxAccess(_A)
if mibBuilder.loadTexts:prtLocalizationCharacterSet.setStatus(_B)
_PrtInput_ObjectIdentity=ObjectIdentity
prtInput=_PrtInput_ObjectIdentity((1,3,6,1,2,1,43,8))
_PrtInputTable_ObjectIdentity=ObjectIdentity
prtInputTable=_PrtInputTable_ObjectIdentity((1,3,6,1,2,1,43,8,2))
_PrtInputEntry_ObjectIdentity=ObjectIdentity
prtInputEntry=_PrtInputEntry_ObjectIdentity((1,3,6,1,2,1,43,8,2,1))
_PrtInputType_Type=PrtInputTypeTC
_PrtInputType_Object=MibScalar
prtInputType=_PrtInputType_Object((1,3,6,1,2,1,43,8,2,1,2),_PrtInputType_Type())
prtInputType.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputType.setStatus(_B)
_PrtInputDimUnit_Type=PrtMediaUnitTC
_PrtInputDimUnit_Object=MibScalar
prtInputDimUnit=_PrtInputDimUnit_Object((1,3,6,1,2,1,43,8,2,1,3),_PrtInputDimUnit_Type())
prtInputDimUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputDimUnit.setStatus(_B)
class _PrtInputMediaDimFeedDirDeclared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaDimFeedDirDeclared_Type.__name__=_D
_PrtInputMediaDimFeedDirDeclared_Object=MibScalar
prtInputMediaDimFeedDirDeclared=_PrtInputMediaDimFeedDirDeclared_Object((1,3,6,1,2,1,43,8,2,1,4),_PrtInputMediaDimFeedDirDeclared_Type())
prtInputMediaDimFeedDirDeclared.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaDimFeedDirDeclared.setStatus(_B)
class _PrtInputMediaDimXFeedDirDeclared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaDimXFeedDirDeclared_Type.__name__=_D
_PrtInputMediaDimXFeedDirDeclared_Object=MibScalar
prtInputMediaDimXFeedDirDeclared=_PrtInputMediaDimXFeedDirDeclared_Object((1,3,6,1,2,1,43,8,2,1,5),_PrtInputMediaDimXFeedDirDeclared_Type())
prtInputMediaDimXFeedDirDeclared.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaDimXFeedDirDeclared.setStatus(_B)
class _PrtInputMediaDimFeedDirChosen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaDimFeedDirChosen_Type.__name__=_D
_PrtInputMediaDimFeedDirChosen_Object=MibScalar
prtInputMediaDimFeedDirChosen=_PrtInputMediaDimFeedDirChosen_Object((1,3,6,1,2,1,43,8,2,1,6),_PrtInputMediaDimFeedDirChosen_Type())
prtInputMediaDimFeedDirChosen.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputMediaDimFeedDirChosen.setStatus(_B)
class _PrtInputMediaDimXFeedDirChosen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaDimXFeedDirChosen_Type.__name__=_D
_PrtInputMediaDimXFeedDirChosen_Object=MibScalar
prtInputMediaDimXFeedDirChosen=_PrtInputMediaDimXFeedDirChosen_Object((1,3,6,1,2,1,43,8,2,1,7),_PrtInputMediaDimXFeedDirChosen_Type())
prtInputMediaDimXFeedDirChosen.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputMediaDimXFeedDirChosen.setStatus(_B)
_PrtInputCapacityUnit_Type=PrtCapacityUnitTC
_PrtInputCapacityUnit_Object=MibScalar
prtInputCapacityUnit=_PrtInputCapacityUnit_Object((1,3,6,1,2,1,43,8,2,1,8),_PrtInputCapacityUnit_Type())
prtInputCapacityUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputCapacityUnit.setStatus(_B)
class _PrtInputMaxCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMaxCapacity_Type.__name__=_D
_PrtInputMaxCapacity_Object=MibScalar
prtInputMaxCapacity=_PrtInputMaxCapacity_Object((1,3,6,1,2,1,43,8,2,1,9),_PrtInputMaxCapacity_Type())
prtInputMaxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMaxCapacity.setStatus(_B)
class _PrtInputCurrentLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,2147483647))
_PrtInputCurrentLevel_Type.__name__=_D
_PrtInputCurrentLevel_Object=MibScalar
prtInputCurrentLevel=_PrtInputCurrentLevel_Object((1,3,6,1,2,1,43,8,2,1,10),_PrtInputCurrentLevel_Type())
prtInputCurrentLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputCurrentLevel.setStatus(_B)
_PrtInputStatus_Type=PrtSubUnitStatusTC
_PrtInputStatus_Object=MibScalar
prtInputStatus=_PrtInputStatus_Object((1,3,6,1,2,1,43,8,2,1,11),_PrtInputStatus_Type())
prtInputStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputStatus.setStatus(_B)
class _PrtInputMediaName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputMediaName_Type.__name__=_G
_PrtInputMediaName_Object=MibScalar
prtInputMediaName=_PrtInputMediaName_Object((1,3,6,1,2,1,43,8,2,1,12),_PrtInputMediaName_Type())
prtInputMediaName.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaName.setStatus(_B)
class _PrtInputName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputName_Type.__name__=_G
_PrtInputName_Object=MibScalar
prtInputName=_PrtInputName_Object((1,3,6,1,2,1,43,8,2,1,13),_PrtInputName_Type())
prtInputName.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputName.setStatus(_B)
class _PrtInputVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputVendorName_Type.__name__=_G
_PrtInputVendorName_Object=MibScalar
prtInputVendorName=_PrtInputVendorName_Object((1,3,6,1,2,1,43,8,2,1,14),_PrtInputVendorName_Type())
prtInputVendorName.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputVendorName.setStatus(_B)
class _PrtInputModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputModel_Type.__name__=_G
_PrtInputModel_Object=MibScalar
prtInputModel=_PrtInputModel_Object((1,3,6,1,2,1,43,8,2,1,15),_PrtInputModel_Type())
prtInputModel.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputModel.setStatus(_B)
class _PrtInputVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputVersion_Type.__name__=_G
_PrtInputVersion_Object=MibScalar
prtInputVersion=_PrtInputVersion_Object((1,3,6,1,2,1,43,8,2,1,16),_PrtInputVersion_Type())
prtInputVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputVersion.setStatus(_B)
class _PrtInputSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PrtInputSerialNumber_Type.__name__=_G
_PrtInputSerialNumber_Object=MibScalar
prtInputSerialNumber=_PrtInputSerialNumber_Object((1,3,6,1,2,1,43,8,2,1,17),_PrtInputSerialNumber_Type())
prtInputSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputSerialNumber.setStatus(_B)
_PrtInputDescription_Type=PrtLocalizedDescriptionStringTC
_PrtInputDescription_Object=MibScalar
prtInputDescription=_PrtInputDescription_Object((1,3,6,1,2,1,43,8,2,1,18),_PrtInputDescription_Type())
prtInputDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInputDescription.setStatus(_B)
_PrtInputSecurity_Type=PresentOnOff
_PrtInputSecurity_Object=MibScalar
prtInputSecurity=_PrtInputSecurity_Object((1,3,6,1,2,1,43,8,2,1,19),_PrtInputSecurity_Type())
prtInputSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputSecurity.setStatus(_B)
class _PrtInputMediaWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaWeight_Type.__name__=_D
_PrtInputMediaWeight_Object=MibScalar
prtInputMediaWeight=_PrtInputMediaWeight_Object((1,3,6,1,2,1,43,8,2,1,20),_PrtInputMediaWeight_Type())
prtInputMediaWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaWeight.setStatus(_B)
class _PrtInputMediaType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputMediaType_Type.__name__=_G
_PrtInputMediaType_Object=MibScalar
prtInputMediaType=_PrtInputMediaType_Object((1,3,6,1,2,1,43,8,2,1,21),_PrtInputMediaType_Type())
prtInputMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaType.setStatus(_B)
class _PrtInputMediaColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputMediaColor_Type.__name__=_G
_PrtInputMediaColor_Object=MibScalar
prtInputMediaColor=_PrtInputMediaColor_Object((1,3,6,1,2,1,43,8,2,1,22),_PrtInputMediaColor_Type())
prtInputMediaColor.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaColor.setStatus(_B)
class _PrtInputMediaFormParts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaFormParts_Type.__name__=_D
_PrtInputMediaFormParts_Object=MibScalar
prtInputMediaFormParts=_PrtInputMediaFormParts_Object((1,3,6,1,2,1,43,8,2,1,23),_PrtInputMediaFormParts_Type())
prtInputMediaFormParts.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaFormParts.setStatus(_B)
class _PrtInputMediaLoadTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaLoadTimeout_Type.__name__=_D
_PrtInputMediaLoadTimeout_Object=MibScalar
prtInputMediaLoadTimeout=_PrtInputMediaLoadTimeout_Object((1,3,6,1,2,1,43,8,2,1,24),_PrtInputMediaLoadTimeout_Type())
prtInputMediaLoadTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaLoadTimeout.setStatus(_B)
_PrtOutput_ObjectIdentity=ObjectIdentity
prtOutput=_PrtOutput_ObjectIdentity((1,3,6,1,2,1,43,9))
_PrtOutputTable_ObjectIdentity=ObjectIdentity
prtOutputTable=_PrtOutputTable_ObjectIdentity((1,3,6,1,2,1,43,9,2))
_PrtOutputEntry_ObjectIdentity=ObjectIdentity
prtOutputEntry=_PrtOutputEntry_ObjectIdentity((1,3,6,1,2,1,43,9,2,1))
_PrtOutputType_Type=PrtOutputTypeTC
_PrtOutputType_Object=MibScalar
prtOutputType=_PrtOutputType_Object((1,3,6,1,2,1,43,9,2,1,2),_PrtOutputType_Type())
prtOutputType.setMaxAccess(_A)
if mibBuilder.loadTexts:prtOutputType.setStatus(_B)
_PrtOutputCapacityUnit_Type=PrtCapacityUnitTC
_PrtOutputCapacityUnit_Object=MibScalar
prtOutputCapacityUnit=_PrtOutputCapacityUnit_Object((1,3,6,1,2,1,43,9,2,1,3),_PrtOutputCapacityUnit_Type())
prtOutputCapacityUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:prtOutputCapacityUnit.setStatus(_B)
class _PrtOutputMaxCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMaxCapacity_Type.__name__=_D
_PrtOutputMaxCapacity_Object=MibScalar
prtOutputMaxCapacity=_PrtOutputMaxCapacity_Object((1,3,6,1,2,1,43,9,2,1,4),_PrtOutputMaxCapacity_Type())
prtOutputMaxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMaxCapacity.setStatus(_B)
class _PrtOutputRemainingCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,2147483647))
_PrtOutputRemainingCapacity_Type.__name__=_D
_PrtOutputRemainingCapacity_Object=MibScalar
prtOutputRemainingCapacity=_PrtOutputRemainingCapacity_Object((1,3,6,1,2,1,43,9,2,1,5),_PrtOutputRemainingCapacity_Type())
prtOutputRemainingCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputRemainingCapacity.setStatus(_B)
_PrtOutputStatus_Type=PrtSubUnitStatusTC
_PrtOutputStatus_Object=MibScalar
prtOutputStatus=_PrtOutputStatus_Object((1,3,6,1,2,1,43,9,2,1,6),_PrtOutputStatus_Type())
prtOutputStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:prtOutputStatus.setStatus(_B)
class _PrtOutputName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputName_Type.__name__=_G
_PrtOutputName_Object=MibScalar
prtOutputName=_PrtOutputName_Object((1,3,6,1,2,1,43,9,2,1,7),_PrtOutputName_Type())
prtOutputName.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputName.setStatus(_B)
class _PrtOutputVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputVendorName_Type.__name__=_G
_PrtOutputVendorName_Object=MibScalar
prtOutputVendorName=_PrtOutputVendorName_Object((1,3,6,1,2,1,43,9,2,1,8),_PrtOutputVendorName_Type())
prtOutputVendorName.setMaxAccess(_A)
if mibBuilder.loadTexts:prtOutputVendorName.setStatus(_B)
class _PrtOutputModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputModel_Type.__name__=_G
_PrtOutputModel_Object=MibScalar
prtOutputModel=_PrtOutputModel_Object((1,3,6,1,2,1,43,9,2,1,9),_PrtOutputModel_Type())
prtOutputModel.setMaxAccess(_A)
if mibBuilder.loadTexts:prtOutputModel.setStatus(_B)
class _PrtOutputVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputVersion_Type.__name__=_G
_PrtOutputVersion_Object=MibScalar
prtOutputVersion=_PrtOutputVersion_Object((1,3,6,1,2,1,43,9,2,1,10),_PrtOutputVersion_Type())
prtOutputVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:prtOutputVersion.setStatus(_B)
class _PrtOutputSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputSerialNumber_Type.__name__=_G
_PrtOutputSerialNumber_Object=MibScalar
prtOutputSerialNumber=_PrtOutputSerialNumber_Object((1,3,6,1,2,1,43,9,2,1,11),_PrtOutputSerialNumber_Type())
prtOutputSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:prtOutputSerialNumber.setStatus(_B)
_PrtOutputDescription_Type=PrtLocalizedDescriptionStringTC
_PrtOutputDescription_Object=MibScalar
prtOutputDescription=_PrtOutputDescription_Object((1,3,6,1,2,1,43,9,2,1,12),_PrtOutputDescription_Type())
prtOutputDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:prtOutputDescription.setStatus(_B)
_PrtOutputSecurity_Type=PresentOnOff
_PrtOutputSecurity_Object=MibScalar
prtOutputSecurity=_PrtOutputSecurity_Object((1,3,6,1,2,1,43,9,2,1,13),_PrtOutputSecurity_Type())
prtOutputSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputSecurity.setStatus(_B)
_PrtOutputDimUnit_Type=PrtMediaUnitTC
_PrtOutputDimUnit_Object=MibScalar
prtOutputDimUnit=_PrtOutputDimUnit_Object((1,3,6,1,2,1,43,9,2,1,14),_PrtOutputDimUnit_Type())
prtOutputDimUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:prtOutputDimUnit.setStatus(_B)
class _PrtOutputMaxDimFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMaxDimFeedDir_Type.__name__=_D
_PrtOutputMaxDimFeedDir_Object=MibScalar
prtOutputMaxDimFeedDir=_PrtOutputMaxDimFeedDir_Object((1,3,6,1,2,1,43,9,2,1,15),_PrtOutputMaxDimFeedDir_Type())
prtOutputMaxDimFeedDir.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMaxDimFeedDir.setStatus(_B)
class _PrtOutputMaxDimXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMaxDimXFeedDir_Type.__name__=_D
_PrtOutputMaxDimXFeedDir_Object=MibScalar
prtOutputMaxDimXFeedDir=_PrtOutputMaxDimXFeedDir_Object((1,3,6,1,2,1,43,9,2,1,16),_PrtOutputMaxDimXFeedDir_Type())
prtOutputMaxDimXFeedDir.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMaxDimXFeedDir.setStatus(_B)
class _PrtOutputMinDimFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMinDimFeedDir_Type.__name__=_D
_PrtOutputMinDimFeedDir_Object=MibScalar
prtOutputMinDimFeedDir=_PrtOutputMinDimFeedDir_Object((1,3,6,1,2,1,43,9,2,1,17),_PrtOutputMinDimFeedDir_Type())
prtOutputMinDimFeedDir.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMinDimFeedDir.setStatus(_B)
class _PrtOutputMinDimXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMinDimXFeedDir_Type.__name__=_D
_PrtOutputMinDimXFeedDir_Object=MibScalar
prtOutputMinDimXFeedDir=_PrtOutputMinDimXFeedDir_Object((1,3,6,1,2,1,43,9,2,1,18),_PrtOutputMinDimXFeedDir_Type())
prtOutputMinDimXFeedDir.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMinDimXFeedDir.setStatus(_B)
_PrtOutputStackingOrder_Type=PrtOutputStackingOrderTC
_PrtOutputStackingOrder_Object=MibScalar
prtOutputStackingOrder=_PrtOutputStackingOrder_Object((1,3,6,1,2,1,43,9,2,1,19),_PrtOutputStackingOrder_Type())
prtOutputStackingOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputStackingOrder.setStatus(_B)
_PrtOutputPageDeliveryOrientation_Type=PrtOutputPageDeliveryOrientationTC
_PrtOutputPageDeliveryOrientation_Object=MibScalar
prtOutputPageDeliveryOrientation=_PrtOutputPageDeliveryOrientation_Object((1,3,6,1,2,1,43,9,2,1,20),_PrtOutputPageDeliveryOrientation_Type())
prtOutputPageDeliveryOrientation.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputPageDeliveryOrientation.setStatus(_B)
_PrtOutputBursting_Type=PresentOnOff
_PrtOutputBursting_Object=MibScalar
prtOutputBursting=_PrtOutputBursting_Object((1,3,6,1,2,1,43,9,2,1,21),_PrtOutputBursting_Type())
prtOutputBursting.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputBursting.setStatus(_B)
_PrtOutputDecollating_Type=PresentOnOff
_PrtOutputDecollating_Object=MibScalar
prtOutputDecollating=_PrtOutputDecollating_Object((1,3,6,1,2,1,43,9,2,1,22),_PrtOutputDecollating_Type())
prtOutputDecollating.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputDecollating.setStatus(_B)
_PrtOutputPageCollated_Type=PresentOnOff
_PrtOutputPageCollated_Object=MibScalar
prtOutputPageCollated=_PrtOutputPageCollated_Object((1,3,6,1,2,1,43,9,2,1,23),_PrtOutputPageCollated_Type())
prtOutputPageCollated.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputPageCollated.setStatus(_B)
_PrtOutputOffsetStacking_Type=PresentOnOff
_PrtOutputOffsetStacking_Object=MibScalar
prtOutputOffsetStacking=_PrtOutputOffsetStacking_Object((1,3,6,1,2,1,43,9,2,1,24),_PrtOutputOffsetStacking_Type())
prtOutputOffsetStacking.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputOffsetStacking.setStatus(_B)
_PrtMarker_ObjectIdentity=ObjectIdentity
prtMarker=_PrtMarker_ObjectIdentity((1,3,6,1,2,1,43,10))
_PrtMarkerTable_ObjectIdentity=ObjectIdentity
prtMarkerTable=_PrtMarkerTable_ObjectIdentity((1,3,6,1,2,1,43,10,2))
_PrtMarkerEntry_ObjectIdentity=ObjectIdentity
prtMarkerEntry=_PrtMarkerEntry_ObjectIdentity((1,3,6,1,2,1,43,10,2,1))
_PrtMarkerMarkTech_Type=PrtMarkerMarkTechTC
_PrtMarkerMarkTech_Object=MibScalar
prtMarkerMarkTech=_PrtMarkerMarkTech_Object((1,3,6,1,2,1,43,10,2,1,2),_PrtMarkerMarkTech_Type())
prtMarkerMarkTech.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerMarkTech.setStatus(_B)
_PrtMarkerCounterUnit_Type=PrtMarkerCounterUnitTC
_PrtMarkerCounterUnit_Object=MibScalar
prtMarkerCounterUnit=_PrtMarkerCounterUnit_Object((1,3,6,1,2,1,43,10,2,1,3),_PrtMarkerCounterUnit_Type())
prtMarkerCounterUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerCounterUnit.setStatus(_B)
_PrtMarkerLifeCount_Type=Counter32
_PrtMarkerLifeCount_Object=MibScalar
prtMarkerLifeCount=_PrtMarkerLifeCount_Object((1,3,6,1,2,1,43,10,2,1,4),_PrtMarkerLifeCount_Type())
prtMarkerLifeCount.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerLifeCount.setStatus(_B)
_PrtMarkerPowerOnCount_Type=Counter32
_PrtMarkerPowerOnCount_Object=MibScalar
prtMarkerPowerOnCount=_PrtMarkerPowerOnCount_Object((1,3,6,1,2,1,43,10,2,1,5),_PrtMarkerPowerOnCount_Type())
prtMarkerPowerOnCount.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerPowerOnCount.setStatus(_B)
class _PrtMarkerProcessColorants_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtMarkerProcessColorants_Type.__name__=_D
_PrtMarkerProcessColorants_Object=MibScalar
prtMarkerProcessColorants=_PrtMarkerProcessColorants_Object((1,3,6,1,2,1,43,10,2,1,6),_PrtMarkerProcessColorants_Type())
prtMarkerProcessColorants.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerProcessColorants.setStatus(_B)
class _PrtMarkerSpotColorants_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtMarkerSpotColorants_Type.__name__=_D
_PrtMarkerSpotColorants_Object=MibScalar
prtMarkerSpotColorants=_PrtMarkerSpotColorants_Object((1,3,6,1,2,1,43,10,2,1,7),_PrtMarkerSpotColorants_Type())
prtMarkerSpotColorants.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerSpotColorants.setStatus(_B)
_PrtMarkerAddressabilityUnit_Type=PrtMarkerAddressabilityUnitTC
_PrtMarkerAddressabilityUnit_Object=MibScalar
prtMarkerAddressabilityUnit=_PrtMarkerAddressabilityUnit_Object((1,3,6,1,2,1,43,10,2,1,8),_PrtMarkerAddressabilityUnit_Type())
prtMarkerAddressabilityUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerAddressabilityUnit.setStatus(_B)
class _PrtMarkerAddressabilityFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerAddressabilityFeedDir_Type.__name__=_D
_PrtMarkerAddressabilityFeedDir_Object=MibScalar
prtMarkerAddressabilityFeedDir=_PrtMarkerAddressabilityFeedDir_Object((1,3,6,1,2,1,43,10,2,1,9),_PrtMarkerAddressabilityFeedDir_Type())
prtMarkerAddressabilityFeedDir.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerAddressabilityFeedDir.setStatus(_B)
class _PrtMarkerAddressabilityXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerAddressabilityXFeedDir_Type.__name__=_D
_PrtMarkerAddressabilityXFeedDir_Object=MibScalar
prtMarkerAddressabilityXFeedDir=_PrtMarkerAddressabilityXFeedDir_Object((1,3,6,1,2,1,43,10,2,1,10),_PrtMarkerAddressabilityXFeedDir_Type())
prtMarkerAddressabilityXFeedDir.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerAddressabilityXFeedDir.setStatus(_B)
class _PrtMarkerNorthMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerNorthMargin_Type.__name__=_D
_PrtMarkerNorthMargin_Object=MibScalar
prtMarkerNorthMargin=_PrtMarkerNorthMargin_Object((1,3,6,1,2,1,43,10,2,1,11),_PrtMarkerNorthMargin_Type())
prtMarkerNorthMargin.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerNorthMargin.setStatus(_B)
class _PrtMarkerSouthMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerSouthMargin_Type.__name__=_D
_PrtMarkerSouthMargin_Object=MibScalar
prtMarkerSouthMargin=_PrtMarkerSouthMargin_Object((1,3,6,1,2,1,43,10,2,1,12),_PrtMarkerSouthMargin_Type())
prtMarkerSouthMargin.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerSouthMargin.setStatus(_B)
class _PrtMarkerWestMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerWestMargin_Type.__name__=_D
_PrtMarkerWestMargin_Object=MibScalar
prtMarkerWestMargin=_PrtMarkerWestMargin_Object((1,3,6,1,2,1,43,10,2,1,13),_PrtMarkerWestMargin_Type())
prtMarkerWestMargin.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerWestMargin.setStatus(_B)
class _PrtMarkerEastMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerEastMargin_Type.__name__=_D
_PrtMarkerEastMargin_Object=MibScalar
prtMarkerEastMargin=_PrtMarkerEastMargin_Object((1,3,6,1,2,1,43,10,2,1,14),_PrtMarkerEastMargin_Type())
prtMarkerEastMargin.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerEastMargin.setStatus(_B)
_PrtMarkerStatus_Type=PrtSubUnitStatusTC
_PrtMarkerStatus_Object=MibScalar
prtMarkerStatus=_PrtMarkerStatus_Object((1,3,6,1,2,1,43,10,2,1,15),_PrtMarkerStatus_Type())
prtMarkerStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerStatus.setStatus(_B)
_PrtMarkerSupplies_ObjectIdentity=ObjectIdentity
prtMarkerSupplies=_PrtMarkerSupplies_ObjectIdentity((1,3,6,1,2,1,43,11))
_PrtMarkerSuppliesTable_ObjectIdentity=ObjectIdentity
prtMarkerSuppliesTable=_PrtMarkerSuppliesTable_ObjectIdentity((1,3,6,1,2,1,43,11,1))
_PrtMarkerSuppliesEntry_ObjectIdentity=ObjectIdentity
prtMarkerSuppliesEntry=_PrtMarkerSuppliesEntry_ObjectIdentity((1,3,6,1,2,1,43,11,1,1))
class _PrtMarkerSuppliesMarkerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtMarkerSuppliesMarkerIndex_Type.__name__=_D
_PrtMarkerSuppliesMarkerIndex_Object=MibScalar
prtMarkerSuppliesMarkerIndex=_PrtMarkerSuppliesMarkerIndex_Object((1,3,6,1,2,1,43,11,1,1,2),_PrtMarkerSuppliesMarkerIndex_Type())
prtMarkerSuppliesMarkerIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerSuppliesMarkerIndex.setStatus(_B)
class _PrtMarkerSuppliesColorantIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtMarkerSuppliesColorantIndex_Type.__name__=_D
_PrtMarkerSuppliesColorantIndex_Object=MibScalar
prtMarkerSuppliesColorantIndex=_PrtMarkerSuppliesColorantIndex_Object((1,3,6,1,2,1,43,11,1,1,3),_PrtMarkerSuppliesColorantIndex_Type())
prtMarkerSuppliesColorantIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerSuppliesColorantIndex.setStatus(_B)
_PrtMarkerSuppliesClass_Type=PrtMarkerSuppliesClassTC
_PrtMarkerSuppliesClass_Object=MibScalar
prtMarkerSuppliesClass=_PrtMarkerSuppliesClass_Object((1,3,6,1,2,1,43,11,1,1,4),_PrtMarkerSuppliesClass_Type())
prtMarkerSuppliesClass.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerSuppliesClass.setStatus(_B)
_PrtMarkerSuppliesType_Type=PrtMarkerSuppliesTypeTC
_PrtMarkerSuppliesType_Object=MibScalar
prtMarkerSuppliesType=_PrtMarkerSuppliesType_Object((1,3,6,1,2,1,43,11,1,1,5),_PrtMarkerSuppliesType_Type())
prtMarkerSuppliesType.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerSuppliesType.setStatus(_B)
_PrtMarkerSuppliesDescription_Type=PrtLocalizedDescriptionStringTC
_PrtMarkerSuppliesDescription_Object=MibScalar
prtMarkerSuppliesDescription=_PrtMarkerSuppliesDescription_Object((1,3,6,1,2,1,43,11,1,1,6),_PrtMarkerSuppliesDescription_Type())
prtMarkerSuppliesDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerSuppliesDescription.setStatus(_B)
_PrtMarkerSuppliesSupplyUnit_Type=PrtMarkerSuppliesSupplyUnitTC
_PrtMarkerSuppliesSupplyUnit_Object=MibScalar
prtMarkerSuppliesSupplyUnit=_PrtMarkerSuppliesSupplyUnit_Object((1,3,6,1,2,1,43,11,1,1,7),_PrtMarkerSuppliesSupplyUnit_Type())
prtMarkerSuppliesSupplyUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerSuppliesSupplyUnit.setStatus(_B)
class _PrtMarkerSuppliesMaxCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerSuppliesMaxCapacity_Type.__name__=_D
_PrtMarkerSuppliesMaxCapacity_Object=MibScalar
prtMarkerSuppliesMaxCapacity=_PrtMarkerSuppliesMaxCapacity_Object((1,3,6,1,2,1,43,11,1,1,8),_PrtMarkerSuppliesMaxCapacity_Type())
prtMarkerSuppliesMaxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMarkerSuppliesMaxCapacity.setStatus(_B)
class _PrtMarkerSuppliesLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,2147483647))
_PrtMarkerSuppliesLevel_Type.__name__=_D
_PrtMarkerSuppliesLevel_Object=MibScalar
prtMarkerSuppliesLevel=_PrtMarkerSuppliesLevel_Object((1,3,6,1,2,1,43,11,1,1,9),_PrtMarkerSuppliesLevel_Type())
prtMarkerSuppliesLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMarkerSuppliesLevel.setStatus(_B)
_PrtMarkerColorant_ObjectIdentity=ObjectIdentity
prtMarkerColorant=_PrtMarkerColorant_ObjectIdentity((1,3,6,1,2,1,43,12))
_PrtMarkerColorantTable_ObjectIdentity=ObjectIdentity
prtMarkerColorantTable=_PrtMarkerColorantTable_ObjectIdentity((1,3,6,1,2,1,43,12,1))
_PrtMarkerColorantEntry_ObjectIdentity=ObjectIdentity
prtMarkerColorantEntry=_PrtMarkerColorantEntry_ObjectIdentity((1,3,6,1,2,1,43,12,1,1))
class _PrtMarkerColorantMarkerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtMarkerColorantMarkerIndex_Type.__name__=_D
_PrtMarkerColorantMarkerIndex_Object=MibScalar
prtMarkerColorantMarkerIndex=_PrtMarkerColorantMarkerIndex_Object((1,3,6,1,2,1,43,12,1,1,2),_PrtMarkerColorantMarkerIndex_Type())
prtMarkerColorantMarkerIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerColorantMarkerIndex.setStatus(_B)
_PrtMarkerColorantRole_Type=PrtMarkerColorantRoleTC
_PrtMarkerColorantRole_Object=MibScalar
prtMarkerColorantRole=_PrtMarkerColorantRole_Object((1,3,6,1,2,1,43,12,1,1,3),_PrtMarkerColorantRole_Type())
prtMarkerColorantRole.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerColorantRole.setStatus(_B)
class _PrtMarkerColorantValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtMarkerColorantValue_Type.__name__=_G
_PrtMarkerColorantValue_Object=MibScalar
prtMarkerColorantValue=_PrtMarkerColorantValue_Object((1,3,6,1,2,1,43,12,1,1,4),_PrtMarkerColorantValue_Type())
prtMarkerColorantValue.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerColorantValue.setStatus(_B)
class _PrtMarkerColorantTonality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2147483647))
_PrtMarkerColorantTonality_Type.__name__=_D
_PrtMarkerColorantTonality_Object=MibScalar
prtMarkerColorantTonality=_PrtMarkerColorantTonality_Object((1,3,6,1,2,1,43,12,1,1,5),_PrtMarkerColorantTonality_Type())
prtMarkerColorantTonality.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMarkerColorantTonality.setStatus(_B)
_PrtMediaPath_ObjectIdentity=ObjectIdentity
prtMediaPath=_PrtMediaPath_ObjectIdentity((1,3,6,1,2,1,43,13))
_PrtMediaPathTable_ObjectIdentity=ObjectIdentity
prtMediaPathTable=_PrtMediaPathTable_ObjectIdentity((1,3,6,1,2,1,43,13,4))
_PrtMediaPathEntry_ObjectIdentity=ObjectIdentity
prtMediaPathEntry=_PrtMediaPathEntry_ObjectIdentity((1,3,6,1,2,1,43,13,4,1))
_PrtMediaPathMaxSpeedPrintUnit_Type=PrtMediaPathMaxSpeedPrintUnitTC
_PrtMediaPathMaxSpeedPrintUnit_Object=MibScalar
prtMediaPathMaxSpeedPrintUnit=_PrtMediaPathMaxSpeedPrintUnit_Object((1,3,6,1,2,1,43,13,4,1,2),_PrtMediaPathMaxSpeedPrintUnit_Type())
prtMediaPathMaxSpeedPrintUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathMaxSpeedPrintUnit.setStatus(_B)
_PrtMediaPathMediaSizeUnit_Type=PrtMediaUnitTC
_PrtMediaPathMediaSizeUnit_Object=MibScalar
prtMediaPathMediaSizeUnit=_PrtMediaPathMediaSizeUnit_Object((1,3,6,1,2,1,43,13,4,1,3),_PrtMediaPathMediaSizeUnit_Type())
prtMediaPathMediaSizeUnit.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathMediaSizeUnit.setStatus(_B)
class _PrtMediaPathMaxSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMaxSpeed_Type.__name__=_D
_PrtMediaPathMaxSpeed_Object=MibScalar
prtMediaPathMaxSpeed=_PrtMediaPathMaxSpeed_Object((1,3,6,1,2,1,43,13,4,1,4),_PrtMediaPathMaxSpeed_Type())
prtMediaPathMaxSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathMaxSpeed.setStatus(_B)
class _PrtMediaPathMaxMediaFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMaxMediaFeedDir_Type.__name__=_D
_PrtMediaPathMaxMediaFeedDir_Object=MibScalar
prtMediaPathMaxMediaFeedDir=_PrtMediaPathMaxMediaFeedDir_Object((1,3,6,1,2,1,43,13,4,1,5),_PrtMediaPathMaxMediaFeedDir_Type())
prtMediaPathMaxMediaFeedDir.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathMaxMediaFeedDir.setStatus(_B)
class _PrtMediaPathMaxMediaXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMaxMediaXFeedDir_Type.__name__=_D
_PrtMediaPathMaxMediaXFeedDir_Object=MibScalar
prtMediaPathMaxMediaXFeedDir=_PrtMediaPathMaxMediaXFeedDir_Object((1,3,6,1,2,1,43,13,4,1,6),_PrtMediaPathMaxMediaXFeedDir_Type())
prtMediaPathMaxMediaXFeedDir.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathMaxMediaXFeedDir.setStatus(_B)
class _PrtMediaPathMinMediaFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMinMediaFeedDir_Type.__name__=_D
_PrtMediaPathMinMediaFeedDir_Object=MibScalar
prtMediaPathMinMediaFeedDir=_PrtMediaPathMinMediaFeedDir_Object((1,3,6,1,2,1,43,13,4,1,7),_PrtMediaPathMinMediaFeedDir_Type())
prtMediaPathMinMediaFeedDir.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathMinMediaFeedDir.setStatus(_B)
class _PrtMediaPathMinMediaXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMinMediaXFeedDir_Type.__name__=_D
_PrtMediaPathMinMediaXFeedDir_Object=MibScalar
prtMediaPathMinMediaXFeedDir=_PrtMediaPathMinMediaXFeedDir_Object((1,3,6,1,2,1,43,13,4,1,8),_PrtMediaPathMinMediaXFeedDir_Type())
prtMediaPathMinMediaXFeedDir.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathMinMediaXFeedDir.setStatus(_B)
_PrtMediaPathType_Type=PrtMediaPathTypeTC
_PrtMediaPathType_Object=MibScalar
prtMediaPathType=_PrtMediaPathType_Object((1,3,6,1,2,1,43,13,4,1,9),_PrtMediaPathType_Type())
prtMediaPathType.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathType.setStatus(_B)
_PrtMediaPathDescription_Type=PrtLocalizedDescriptionStringTC
_PrtMediaPathDescription_Object=MibScalar
prtMediaPathDescription=_PrtMediaPathDescription_Object((1,3,6,1,2,1,43,13,4,1,10),_PrtMediaPathDescription_Type())
prtMediaPathDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathDescription.setStatus(_B)
_PrtMediaPathStatus_Type=PrtSubUnitStatusTC
_PrtMediaPathStatus_Object=MibScalar
prtMediaPathStatus=_PrtMediaPathStatus_Object((1,3,6,1,2,1,43,13,4,1,11),_PrtMediaPathStatus_Type())
prtMediaPathStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:prtMediaPathStatus.setStatus(_B)
_PrtChannel_ObjectIdentity=ObjectIdentity
prtChannel=_PrtChannel_ObjectIdentity((1,3,6,1,2,1,43,14))
_PrtChannelTable_ObjectIdentity=ObjectIdentity
prtChannelTable=_PrtChannelTable_ObjectIdentity((1,3,6,1,2,1,43,14,1))
_PrtChannelEntry_ObjectIdentity=ObjectIdentity
prtChannelEntry=_PrtChannelEntry_ObjectIdentity((1,3,6,1,2,1,43,14,1,1))
_PrtChannelType_Type=PrtChannelTypeTC
_PrtChannelType_Object=MibScalar
prtChannelType=_PrtChannelType_Object((1,3,6,1,2,1,43,14,1,1,2),_PrtChannelType_Type())
prtChannelType.setMaxAccess(_A)
if mibBuilder.loadTexts:prtChannelType.setStatus(_B)
class _PrtChannelProtocolVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtChannelProtocolVersion_Type.__name__=_G
_PrtChannelProtocolVersion_Object=MibScalar
prtChannelProtocolVersion=_PrtChannelProtocolVersion_Object((1,3,6,1,2,1,43,14,1,1,3),_PrtChannelProtocolVersion_Type())
prtChannelProtocolVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:prtChannelProtocolVersion.setStatus(_B)
class _PrtChannelCurrentJobCntlLangIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtChannelCurrentJobCntlLangIndex_Type.__name__=_D
_PrtChannelCurrentJobCntlLangIndex_Object=MibScalar
prtChannelCurrentJobCntlLangIndex=_PrtChannelCurrentJobCntlLangIndex_Object((1,3,6,1,2,1,43,14,1,1,4),_PrtChannelCurrentJobCntlLangIndex_Type())
prtChannelCurrentJobCntlLangIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtChannelCurrentJobCntlLangIndex.setStatus(_B)
class _PrtChannelDefaultPageDescLangIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtChannelDefaultPageDescLangIndex_Type.__name__=_D
_PrtChannelDefaultPageDescLangIndex_Object=MibScalar
prtChannelDefaultPageDescLangIndex=_PrtChannelDefaultPageDescLangIndex_Object((1,3,6,1,2,1,43,14,1,1,5),_PrtChannelDefaultPageDescLangIndex_Type())
prtChannelDefaultPageDescLangIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtChannelDefaultPageDescLangIndex.setStatus(_B)
_PrtChannelState_Type=PrtChannelStateTC
_PrtChannelState_Object=MibScalar
prtChannelState=_PrtChannelState_Object((1,3,6,1,2,1,43,14,1,1,6),_PrtChannelState_Type())
prtChannelState.setMaxAccess(_C)
if mibBuilder.loadTexts:prtChannelState.setStatus(_B)
_PrtChannelIfIndex_Type=InterfaceIndexOrZero
_PrtChannelIfIndex_Object=MibScalar
prtChannelIfIndex=_PrtChannelIfIndex_Object((1,3,6,1,2,1,43,14,1,1,7),_PrtChannelIfIndex_Type())
prtChannelIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtChannelIfIndex.setStatus(_B)
_PrtChannelStatus_Type=PrtSubUnitStatusTC
_PrtChannelStatus_Object=MibScalar
prtChannelStatus=_PrtChannelStatus_Object((1,3,6,1,2,1,43,14,1,1,8),_PrtChannelStatus_Type())
prtChannelStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:prtChannelStatus.setStatus(_B)
class _PrtChannelInformation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtChannelInformation_Type.__name__=_G
_PrtChannelInformation_Object=MibScalar
prtChannelInformation=_PrtChannelInformation_Object((1,3,6,1,2,1,43,14,1,1,9),_PrtChannelInformation_Type())
prtChannelInformation.setMaxAccess(_A)
if mibBuilder.loadTexts:prtChannelInformation.setStatus(_B)
_PrtInterpreter_ObjectIdentity=ObjectIdentity
prtInterpreter=_PrtInterpreter_ObjectIdentity((1,3,6,1,2,1,43,15))
_PrtInterpreterTable_ObjectIdentity=ObjectIdentity
prtInterpreterTable=_PrtInterpreterTable_ObjectIdentity((1,3,6,1,2,1,43,15,1))
_PrtInterpreterEntry_ObjectIdentity=ObjectIdentity
prtInterpreterEntry=_PrtInterpreterEntry_ObjectIdentity((1,3,6,1,2,1,43,15,1,1))
_PrtInterpreterLangFamily_Type=PrtInterpreterLangFamilyTC
_PrtInterpreterLangFamily_Object=MibScalar
prtInterpreterLangFamily=_PrtInterpreterLangFamily_Object((1,3,6,1,2,1,43,15,1,1,2),_PrtInterpreterLangFamily_Type())
prtInterpreterLangFamily.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInterpreterLangFamily.setStatus(_B)
class _PrtInterpreterLangLevel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PrtInterpreterLangLevel_Type.__name__=_G
_PrtInterpreterLangLevel_Object=MibScalar
prtInterpreterLangLevel=_PrtInterpreterLangLevel_Object((1,3,6,1,2,1,43,15,1,1,3),_PrtInterpreterLangLevel_Type())
prtInterpreterLangLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInterpreterLangLevel.setStatus(_B)
class _PrtInterpreterLangVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PrtInterpreterLangVersion_Type.__name__=_G
_PrtInterpreterLangVersion_Object=MibScalar
prtInterpreterLangVersion=_PrtInterpreterLangVersion_Object((1,3,6,1,2,1,43,15,1,1,4),_PrtInterpreterLangVersion_Type())
prtInterpreterLangVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInterpreterLangVersion.setStatus(_B)
_PrtInterpreterDescription_Type=PrtLocalizedDescriptionStringTC
_PrtInterpreterDescription_Object=MibScalar
prtInterpreterDescription=_PrtInterpreterDescription_Object((1,3,6,1,2,1,43,15,1,1,5),_PrtInterpreterDescription_Type())
prtInterpreterDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInterpreterDescription.setStatus(_B)
class _PrtInterpreterVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PrtInterpreterVersion_Type.__name__=_G
_PrtInterpreterVersion_Object=MibScalar
prtInterpreterVersion=_PrtInterpreterVersion_Object((1,3,6,1,2,1,43,15,1,1,6),_PrtInterpreterVersion_Type())
prtInterpreterVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInterpreterVersion.setStatus(_B)
_PrtInterpreterDefaultOrientation_Type=PrtPrintOrientationTC
_PrtInterpreterDefaultOrientation_Object=MibScalar
prtInterpreterDefaultOrientation=_PrtInterpreterDefaultOrientation_Object((1,3,6,1,2,1,43,15,1,1,7),_PrtInterpreterDefaultOrientation_Type())
prtInterpreterDefaultOrientation.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInterpreterDefaultOrientation.setStatus(_B)
class _PrtInterpreterFeedAddressability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInterpreterFeedAddressability_Type.__name__=_D
_PrtInterpreterFeedAddressability_Object=MibScalar
prtInterpreterFeedAddressability=_PrtInterpreterFeedAddressability_Object((1,3,6,1,2,1,43,15,1,1,8),_PrtInterpreterFeedAddressability_Type())
prtInterpreterFeedAddressability.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInterpreterFeedAddressability.setStatus(_B)
class _PrtInterpreterXFeedAddressability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInterpreterXFeedAddressability_Type.__name__=_D
_PrtInterpreterXFeedAddressability_Object=MibScalar
prtInterpreterXFeedAddressability=_PrtInterpreterXFeedAddressability_Object((1,3,6,1,2,1,43,15,1,1,9),_PrtInterpreterXFeedAddressability_Type())
prtInterpreterXFeedAddressability.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInterpreterXFeedAddressability.setStatus(_B)
_PrtInterpreterDefaultCharSetIn_Type=IANACharset
_PrtInterpreterDefaultCharSetIn_Object=MibScalar
prtInterpreterDefaultCharSetIn=_PrtInterpreterDefaultCharSetIn_Object((1,3,6,1,2,1,43,15,1,1,10),_PrtInterpreterDefaultCharSetIn_Type())
prtInterpreterDefaultCharSetIn.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInterpreterDefaultCharSetIn.setStatus(_B)
_PrtInterpreterDefaultCharSetOut_Type=IANACharset
_PrtInterpreterDefaultCharSetOut_Object=MibScalar
prtInterpreterDefaultCharSetOut=_PrtInterpreterDefaultCharSetOut_Object((1,3,6,1,2,1,43,15,1,1,11),_PrtInterpreterDefaultCharSetOut_Type())
prtInterpreterDefaultCharSetOut.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInterpreterDefaultCharSetOut.setStatus(_B)
_PrtInterpreterTwoWay_Type=PrtInterpreterTwoWayTC
_PrtInterpreterTwoWay_Object=MibScalar
prtInterpreterTwoWay=_PrtInterpreterTwoWay_Object((1,3,6,1,2,1,43,15,1,1,12),_PrtInterpreterTwoWay_Type())
prtInterpreterTwoWay.setMaxAccess(_A)
if mibBuilder.loadTexts:prtInterpreterTwoWay.setStatus(_B)
_PrtConsoleDisplayBuffer_ObjectIdentity=ObjectIdentity
prtConsoleDisplayBuffer=_PrtConsoleDisplayBuffer_ObjectIdentity((1,3,6,1,2,1,43,16))
_PrtConsoleDisplayBufferTable_ObjectIdentity=ObjectIdentity
prtConsoleDisplayBufferTable=_PrtConsoleDisplayBufferTable_ObjectIdentity((1,3,6,1,2,1,43,16,5))
_PrtConsoleDisplayBufferEntry_ObjectIdentity=ObjectIdentity
prtConsoleDisplayBufferEntry=_PrtConsoleDisplayBufferEntry_ObjectIdentity((1,3,6,1,2,1,43,16,5,1))
_PrtConsoleDisplayBufferText_Type=PrtConsoleDescriptionStringTC
_PrtConsoleDisplayBufferText_Object=MibScalar
prtConsoleDisplayBufferText=_PrtConsoleDisplayBufferText_Object((1,3,6,1,2,1,43,16,5,1,2),_PrtConsoleDisplayBufferText_Type())
prtConsoleDisplayBufferText.setMaxAccess(_C)
if mibBuilder.loadTexts:prtConsoleDisplayBufferText.setStatus(_B)
_PrtConsoleLights_ObjectIdentity=ObjectIdentity
prtConsoleLights=_PrtConsoleLights_ObjectIdentity((1,3,6,1,2,1,43,17))
_PrtConsoleLightTable_ObjectIdentity=ObjectIdentity
prtConsoleLightTable=_PrtConsoleLightTable_ObjectIdentity((1,3,6,1,2,1,43,17,6))
_PrtConsoleLightEntry_ObjectIdentity=ObjectIdentity
prtConsoleLightEntry=_PrtConsoleLightEntry_ObjectIdentity((1,3,6,1,2,1,43,17,6,1))
class _PrtConsoleOnTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PrtConsoleOnTime_Type.__name__=_D
_PrtConsoleOnTime_Object=MibScalar
prtConsoleOnTime=_PrtConsoleOnTime_Object((1,3,6,1,2,1,43,17,6,1,2),_PrtConsoleOnTime_Type())
prtConsoleOnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:prtConsoleOnTime.setStatus(_B)
class _PrtConsoleOffTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PrtConsoleOffTime_Type.__name__=_D
_PrtConsoleOffTime_Object=MibScalar
prtConsoleOffTime=_PrtConsoleOffTime_Object((1,3,6,1,2,1,43,17,6,1,3),_PrtConsoleOffTime_Type())
prtConsoleOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:prtConsoleOffTime.setStatus(_B)
_PrtConsoleColor_Type=PrtConsoleColorTC
_PrtConsoleColor_Object=MibScalar
prtConsoleColor=_PrtConsoleColor_Object((1,3,6,1,2,1,43,17,6,1,4),_PrtConsoleColor_Type())
prtConsoleColor.setMaxAccess(_A)
if mibBuilder.loadTexts:prtConsoleColor.setStatus(_B)
_PrtConsoleDescription_Type=PrtConsoleDescriptionStringTC
_PrtConsoleDescription_Object=MibScalar
prtConsoleDescription=_PrtConsoleDescription_Object((1,3,6,1,2,1,43,17,6,1,5),_PrtConsoleDescription_Type())
prtConsoleDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:prtConsoleDescription.setStatus(_B)
_PrtAlert_ObjectIdentity=ObjectIdentity
prtAlert=_PrtAlert_ObjectIdentity((1,3,6,1,2,1,43,18))
_PrtAlertTable_ObjectIdentity=ObjectIdentity
prtAlertTable=_PrtAlertTable_ObjectIdentity((1,3,6,1,2,1,43,18,1))
_PrtAlertEntry_ObjectIdentity=ObjectIdentity
prtAlertEntry=_PrtAlertEntry_ObjectIdentity((1,3,6,1,2,1,43,18,1,1))
_PrtAlertSeverityLevel_Type=PrtAlertSeverityLevelTC
_PrtAlertSeverityLevel_Object=MibScalar
prtAlertSeverityLevel=_PrtAlertSeverityLevel_Object((1,3,6,1,2,1,43,18,1,1,2),_PrtAlertSeverityLevel_Type())
prtAlertSeverityLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertSeverityLevel.setStatus(_B)
_PrtAlertTrainingLevel_Type=PrtAlertTrainingLevelTC
_PrtAlertTrainingLevel_Object=MibScalar
prtAlertTrainingLevel=_PrtAlertTrainingLevel_Object((1,3,6,1,2,1,43,18,1,1,3),_PrtAlertTrainingLevel_Type())
prtAlertTrainingLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertTrainingLevel.setStatus(_B)
_PrtAlertGroup_Type=PrtAlertGroupTC
_PrtAlertGroup_Object=MibScalar
prtAlertGroup=_PrtAlertGroup_Object((1,3,6,1,2,1,43,18,1,1,4),_PrtAlertGroup_Type())
prtAlertGroup.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertGroup.setStatus(_B)
class _PrtAlertGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_PrtAlertGroupIndex_Type.__name__=_D
_PrtAlertGroupIndex_Object=MibScalar
prtAlertGroupIndex=_PrtAlertGroupIndex_Object((1,3,6,1,2,1,43,18,1,1,5),_PrtAlertGroupIndex_Type())
prtAlertGroupIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertGroupIndex.setStatus(_B)
class _PrtAlertLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtAlertLocation_Type.__name__=_D
_PrtAlertLocation_Object=MibScalar
prtAlertLocation=_PrtAlertLocation_Object((1,3,6,1,2,1,43,18,1,1,6),_PrtAlertLocation_Type())
prtAlertLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertLocation.setStatus(_B)
_PrtAlertCode_Type=PrtAlertCodeTC
_PrtAlertCode_Object=MibScalar
prtAlertCode=_PrtAlertCode_Object((1,3,6,1,2,1,43,18,1,1,7),_PrtAlertCode_Type())
prtAlertCode.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertCode.setStatus(_B)
_PrtAlertDescription_Type=PrtLocalizedDescriptionStringTC
_PrtAlertDescription_Object=MibScalar
prtAlertDescription=_PrtAlertDescription_Object((1,3,6,1,2,1,43,18,1,1,8),_PrtAlertDescription_Type())
prtAlertDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertDescription.setStatus(_B)
_PrtAlertTime_Type=TimeTicks
_PrtAlertTime_Object=MibScalar
prtAlertTime=_PrtAlertTime_Object((1,3,6,1,2,1,43,18,1,1,9),_PrtAlertTime_Type())
prtAlertTime.setMaxAccess(_A)
if mibBuilder.loadTexts:prtAlertTime.setStatus(_B)
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_HpPrintServer_ObjectIdentity=ObjectIdentity
hpPrintServer=_HpPrintServer_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,11,2,3))
_NetPeripheral_ObjectIdentity=ObjectIdentity
netPeripheral=_NetPeripheral_ObjectIdentity((1,3,6,1,4,1,11,2,3,9))
_NetPrinter_ObjectIdentity=ObjectIdentity
netPrinter=_NetPrinter_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,1))
_GeneralDeviceStatus_ObjectIdentity=ObjectIdentity
generalDeviceStatus=_GeneralDeviceStatus_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,1,1))
_GdStatusEntry_ObjectIdentity=ObjectIdentity
gdStatusEntry=_GdStatusEntry_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,1,1,2))
class _GdStatusLineState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GdStatusLineState_Type.__name__=_D
_GdStatusLineState_Object=MibScalar
gdStatusLineState=_GdStatusLineState_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,1),_GdStatusLineState_Type())
gdStatusLineState.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusLineState.setStatus(_B)
_GdStatusPaperOut_Type=Integer32
_GdStatusPaperOut_Object=MibScalar
gdStatusPaperOut=_GdStatusPaperOut_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,8),_GdStatusPaperOut_Type())
gdStatusPaperOut.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusPaperOut.setStatus(_B)
_GdStatusPaperJam_Type=Integer32
_GdStatusPaperJam_Object=MibScalar
gdStatusPaperJam=_GdStatusPaperJam_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,9),_GdStatusPaperJam_Type())
gdStatusPaperJam.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusPaperJam.setStatus(_B)
class _GdStatusBusy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GdStatusBusy_Type.__name__=_D
_GdStatusBusy_Object=MibScalar
gdStatusBusy=_GdStatusBusy_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,14),_GdStatusBusy_Type())
gdStatusBusy.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusBusy.setStatus(_B)
class _GdStatusWait_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GdStatusWait_Type.__name__=_D
_GdStatusWait_Object=MibScalar
gdStatusWait=_GdStatusWait_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,15),_GdStatusWait_Type())
gdStatusWait.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusWait.setStatus(_B)
_GdStatusInitialize_Type=Integer32
_GdStatusInitialize_Object=MibScalar
gdStatusInitialize=_GdStatusInitialize_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,16),_GdStatusInitialize_Type())
gdStatusInitialize.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusInitialize.setStatus(_B)
class _GdStatusDoorOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GdStatusDoorOpen_Type.__name__=_D
_GdStatusDoorOpen_Object=MibScalar
gdStatusDoorOpen=_GdStatusDoorOpen_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,17),_GdStatusDoorOpen_Type())
gdStatusDoorOpen.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusDoorOpen.setStatus(_B)
_GdStatusPrinting_Type=Integer32
_GdStatusPrinting_Object=MibScalar
gdStatusPrinting=_GdStatusPrinting_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,18),_GdStatusPrinting_Type())
gdStatusPrinting.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusPrinting.setStatus(_B)
_GdStatusPaperOutput_Type=Integer32
_GdStatusPaperOutput_Object=MibScalar
gdStatusPaperOutput=_GdStatusPaperOutput_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,19),_GdStatusPaperOutput_Type())
gdStatusPaperOutput.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusPaperOutput.setStatus(_B)
_GdStatusDisplay_Type=DisplayString
_GdStatusDisplay_Object=MibScalar
gdStatusDisplay=_GdStatusDisplay_Object((1,3,6,1,4,1,11,2,3,9,1,1,3),_GdStatusDisplay_Type())
gdStatusDisplay.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusDisplay.setStatus(_B)
class _GdStatusId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_GdStatusId_Type.__name__=_G
_GdStatusId_Object=MibScalar
gdStatusId=_GdStatusId_Object((1,3,6,1,4,1,11,2,3,9,1,1,7),_GdStatusId_Type())
gdStatusId.setMaxAccess(_A)
if mibBuilder.loadTexts:gdStatusId.setStatus(_B)
_GdStatusJobTimeout_Type=Integer32
_GdStatusJobTimeout_Object=MibScalar
gdStatusJobTimeout=_GdStatusJobTimeout_Object((1,3,6,1,4,1,11,2,3,9,1,1,10),_GdStatusJobTimeout_Type())
gdStatusJobTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:gdStatusJobTimeout.setStatus(_c)
class _GdPasswords_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GdPasswords_Type.__name__=_G
_GdPasswords_Object=MibScalar
gdPasswords=_GdPasswords_Object((1,3,6,1,4,1,11,2,3,9,1,1,13),_GdPasswords_Type())
gdPasswords.setMaxAccess(_C)
if mibBuilder.loadTexts:gdPasswords.setStatus(_B)
_NetPML_ObjectIdentity=ObjectIdentity
netPML=_NetPML_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4))
_NetPMLmgmt_ObjectIdentity=ObjectIdentity
netPMLmgmt=_NetPMLmgmt_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1))
_Device_system_ObjectIdentity=ObjectIdentity
device_system=_Device_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1))
_Settings_system_ObjectIdentity=ObjectIdentity
settings_system=_Settings_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1))
_Energy_star_Type=Integer32
_Energy_star_Object=MibScalar
energy_star=_Energy_star_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,1),_Energy_star_Type())
energy_star.setMaxAccess(_C)
if mibBuilder.loadTexts:energy_star.setStatus(_F)
class _Sleep_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eFalse',1),('eTrue',2)))
_Sleep_mode_Type.__name__=_D
_Sleep_mode_Object=MibScalar
sleep_mode=_Sleep_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,2),_Sleep_mode_Type())
sleep_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleep_mode.setStatus(_F)
class _Speed_energy_usage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eFasterFirstPage',1),('eSaveEnergy',2),('eSaveMostEnergy',3),('eSaveMoreEnergy',4)))
_Speed_energy_usage_Type.__name__=_D
_Speed_energy_usage_Object=MibScalar
speed_energy_usage=_Speed_energy_usage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,50),_Speed_energy_usage_Type())
speed_energy_usage.setMaxAccess(_C)
if mibBuilder.loadTexts:speed_energy_usage.setStatus(_F)
class _Enable_engine_early_warmup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eDisable',1),('eEnable',2)))
_Enable_engine_early_warmup_Type.__name__=_D
_Enable_engine_early_warmup_Object=MibScalar
enable_engine_early_warmup=_Enable_engine_early_warmup_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,101),_Enable_engine_early_warmup_Type())
enable_engine_early_warmup.setMaxAccess(_C)
if mibBuilder.loadTexts:enable_engine_early_warmup.setStatus(_F)
_Status_system_ObjectIdentity=ObjectIdentity
status_system=_Status_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2))
class _Install_date_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_Install_date_Type.__name__=_H
_Install_date_Object=MibScalar
install_date=_Install_date_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,8),_Install_date_Type())
install_date.setMaxAccess(_C)
if mibBuilder.loadTexts:install_date.setStatus(_F)
_Date_and_time_Type=OctetString
_Date_and_time_Object=MibScalar
date_and_time=_Date_and_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,17),_Date_and_time_Type())
date_and_time.setMaxAccess(_C)
if mibBuilder.loadTexts:date_and_time.setStatus(_F)
_Id_ObjectIdentity=ObjectIdentity
id=_Id_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3))
_Model_number_Type=DisplayString
_Model_number_Object=MibScalar
model_number=_Model_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,1),_Model_number_Type())
model_number.setMaxAccess(_A)
if mibBuilder.loadTexts:model_number.setStatus(_F)
class _Model_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Model_name_Type.__name__=_H
_Model_name_Object=MibScalar
model_name=_Model_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,2),_Model_name_Type())
model_name.setMaxAccess(_A)
if mibBuilder.loadTexts:model_name.setStatus(_F)
class _Serial_number_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Serial_number_Type.__name__=_H
_Serial_number_Object=MibScalar
serial_number=_Serial_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,3),_Serial_number_Type())
serial_number.setMaxAccess(_A)
if mibBuilder.loadTexts:serial_number.setStatus(_F)
_Fw_rom_datecode_Type=DisplayString
_Fw_rom_datecode_Object=MibScalar
fw_rom_datecode=_Fw_rom_datecode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,5),_Fw_rom_datecode_Type())
fw_rom_datecode.setMaxAccess(_A)
if mibBuilder.loadTexts:fw_rom_datecode.setStatus(_F)
_Fw_rom_revision_Type=DisplayString
_Fw_rom_revision_Object=MibScalar
fw_rom_revision=_Fw_rom_revision_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,6),_Fw_rom_revision_Type())
fw_rom_revision.setMaxAccess(_A)
if mibBuilder.loadTexts:fw_rom_revision.setStatus(_F)
_Device_location_Type=DisplayString
_Device_location_Object=MibScalar
device_location=_Device_location_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,11),_Device_location_Type())
device_location.setMaxAccess(_C)
if mibBuilder.loadTexts:device_location.setStatus(_F)
_Asset_number_Type=DisplayString
_Asset_number_Object=MibScalar
asset_number=_Asset_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,12),_Asset_number_Type())
asset_number.setMaxAccess(_C)
if mibBuilder.loadTexts:asset_number.setStatus(_F)
_Test_ObjectIdentity=ObjectIdentity
test=_Test_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5))
class _Print_internal_page_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,7,8,9,100,101,254,255,256,350,450)));namedValues=NamedValues(*(('eNotPrintingAnInternalPage',1),('ePrintingAnUnknownInternalPage',2),('eDeviceDemoPage1ConfigurationPage',3),('eDeviceDemoPage2',4),('eDeviceDemoPage5ErrorLog',7),('eDeviceDemoPage6FileSystemDirectoryListing',8),('eDeviceDemoPage7MenuMap',9),('ePrintUsagePage',100),('eSuppliesPage',101),('eDevicePaperPathTest',254),('eDevicePageRegistrationPage',255),('ePrintQualityPages',256),('ePCLFontList1',350),('ePSFontList',450)))
_Print_internal_page_Type.__name__=_D
_Print_internal_page_Object=MibScalar
print_internal_page=_Print_internal_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,2),_Print_internal_page_Type())
print_internal_page.setMaxAccess(_C)
if mibBuilder.loadTexts:print_internal_page.setStatus(_F)
_Errorlog_ObjectIdentity=ObjectIdentity
errorlog=_Errorlog_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11))
_Error1_ObjectIdentity=ObjectIdentity
error1=_Error1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1))
_Error1_time_stamp_Type=Integer32
_Error1_time_stamp_Object=MibScalar
error1_time_stamp=_Error1_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1,1),_Error1_time_stamp_Type())
error1_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error1_time_stamp.setStatus(_F)
_Error1_code_Type=Integer32
_Error1_code_Object=MibScalar
error1_code=_Error1_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1,2),_Error1_code_Type())
error1_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error1_code.setStatus(_F)
_Error1_date_time_Type=OctetString
_Error1_date_time_Object=MibScalar
error1_date_time=_Error1_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1,3),_Error1_date_time_Type())
error1_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error1_date_time.setStatus(_F)
_Error2_ObjectIdentity=ObjectIdentity
error2=_Error2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2))
_Error2_time_stamp_Type=Integer32
_Error2_time_stamp_Object=MibScalar
error2_time_stamp=_Error2_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2,1),_Error2_time_stamp_Type())
error2_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error2_time_stamp.setStatus(_F)
_Error2_code_Type=Integer32
_Error2_code_Object=MibScalar
error2_code=_Error2_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2,2),_Error2_code_Type())
error2_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error2_code.setStatus(_F)
_Error2_date_time_Type=OctetString
_Error2_date_time_Object=MibScalar
error2_date_time=_Error2_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2,3),_Error2_date_time_Type())
error2_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error2_date_time.setStatus(_F)
_Error3_ObjectIdentity=ObjectIdentity
error3=_Error3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3))
_Error3_time_stamp_Type=Integer32
_Error3_time_stamp_Object=MibScalar
error3_time_stamp=_Error3_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3,1),_Error3_time_stamp_Type())
error3_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error3_time_stamp.setStatus(_F)
_Error3_code_Type=Integer32
_Error3_code_Object=MibScalar
error3_code=_Error3_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3,2),_Error3_code_Type())
error3_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error3_code.setStatus(_F)
_Error3_date_time_Type=OctetString
_Error3_date_time_Object=MibScalar
error3_date_time=_Error3_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3,3),_Error3_date_time_Type())
error3_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error3_date_time.setStatus(_F)
_Error4_ObjectIdentity=ObjectIdentity
error4=_Error4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4))
_Error4_time_stamp_Type=Integer32
_Error4_time_stamp_Object=MibScalar
error4_time_stamp=_Error4_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4,1),_Error4_time_stamp_Type())
error4_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error4_time_stamp.setStatus(_F)
_Error4_code_Type=Integer32
_Error4_code_Object=MibScalar
error4_code=_Error4_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4,2),_Error4_code_Type())
error4_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error4_code.setStatus(_F)
_Error4_date_time_Type=OctetString
_Error4_date_time_Object=MibScalar
error4_date_time=_Error4_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4,3),_Error4_date_time_Type())
error4_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error4_date_time.setStatus(_F)
_Error5_ObjectIdentity=ObjectIdentity
error5=_Error5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5))
_Error5_time_stamp_Type=Integer32
_Error5_time_stamp_Object=MibScalar
error5_time_stamp=_Error5_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5,1),_Error5_time_stamp_Type())
error5_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error5_time_stamp.setStatus(_F)
_Error5_code_Type=Integer32
_Error5_code_Object=MibScalar
error5_code=_Error5_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5,2),_Error5_code_Type())
error5_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error5_code.setStatus(_F)
_Error5_date_time_Type=OctetString
_Error5_date_time_Object=MibScalar
error5_date_time=_Error5_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5,3),_Error5_date_time_Type())
error5_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error5_date_time.setStatus(_F)
_Error6_ObjectIdentity=ObjectIdentity
error6=_Error6_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6))
_Error6_time_stamp_Type=Integer32
_Error6_time_stamp_Object=MibScalar
error6_time_stamp=_Error6_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6,1),_Error6_time_stamp_Type())
error6_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error6_time_stamp.setStatus(_F)
_Error6_code_Type=Integer32
_Error6_code_Object=MibScalar
error6_code=_Error6_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6,2),_Error6_code_Type())
error6_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error6_code.setStatus(_F)
_Error6_date_time_Type=OctetString
_Error6_date_time_Object=MibScalar
error6_date_time=_Error6_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6,3),_Error6_date_time_Type())
error6_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error6_date_time.setStatus(_F)
_Error7_ObjectIdentity=ObjectIdentity
error7=_Error7_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7))
_Error7_time_stamp_Type=Integer32
_Error7_time_stamp_Object=MibScalar
error7_time_stamp=_Error7_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7,1),_Error7_time_stamp_Type())
error7_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error7_time_stamp.setStatus(_F)
_Error7_code_Type=Integer32
_Error7_code_Object=MibScalar
error7_code=_Error7_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7,2),_Error7_code_Type())
error7_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error7_code.setStatus(_F)
_Error7_date_time_Type=OctetString
_Error7_date_time_Object=MibScalar
error7_date_time=_Error7_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7,3),_Error7_date_time_Type())
error7_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error7_date_time.setStatus(_F)
_Error8_ObjectIdentity=ObjectIdentity
error8=_Error8_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8))
_Error8_time_stamp_Type=Integer32
_Error8_time_stamp_Object=MibScalar
error8_time_stamp=_Error8_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8,1),_Error8_time_stamp_Type())
error8_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error8_time_stamp.setStatus(_F)
_Error8_code_Type=Integer32
_Error8_code_Object=MibScalar
error8_code=_Error8_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8,2),_Error8_code_Type())
error8_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error8_code.setStatus(_F)
_Error8_date_time_Type=OctetString
_Error8_date_time_Object=MibScalar
error8_date_time=_Error8_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8,3),_Error8_date_time_Type())
error8_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error8_date_time.setStatus(_F)
_Error9_ObjectIdentity=ObjectIdentity
error9=_Error9_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9))
_Error9_time_stamp_Type=Integer32
_Error9_time_stamp_Object=MibScalar
error9_time_stamp=_Error9_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9,1),_Error9_time_stamp_Type())
error9_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error9_time_stamp.setStatus(_F)
_Error9_code_Type=Integer32
_Error9_code_Object=MibScalar
error9_code=_Error9_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9,2),_Error9_code_Type())
error9_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error9_code.setStatus(_F)
_Error9_date_time_Type=OctetString
_Error9_date_time_Object=MibScalar
error9_date_time=_Error9_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9,3),_Error9_date_time_Type())
error9_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error9_date_time.setStatus(_F)
_Error10_ObjectIdentity=ObjectIdentity
error10=_Error10_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10))
_Error10_time_stamp_Type=Integer32
_Error10_time_stamp_Object=MibScalar
error10_time_stamp=_Error10_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10,1),_Error10_time_stamp_Type())
error10_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error10_time_stamp.setStatus(_F)
_Error10_code_Type=Integer32
_Error10_code_Object=MibScalar
error10_code=_Error10_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10,2),_Error10_code_Type())
error10_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error10_code.setStatus(_F)
_Error10_date_time_Type=OctetString
_Error10_date_time_Object=MibScalar
error10_date_time=_Error10_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10,3),_Error10_date_time_Type())
error10_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error10_date_time.setStatus(_F)
_Error11_ObjectIdentity=ObjectIdentity
error11=_Error11_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11))
_Error11_time_stamp_Type=Integer32
_Error11_time_stamp_Object=MibScalar
error11_time_stamp=_Error11_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11,1),_Error11_time_stamp_Type())
error11_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error11_time_stamp.setStatus(_F)
_Error11_code_Type=Integer32
_Error11_code_Object=MibScalar
error11_code=_Error11_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11,2),_Error11_code_Type())
error11_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error11_code.setStatus(_F)
_Error11_date_time_Type=OctetString
_Error11_date_time_Object=MibScalar
error11_date_time=_Error11_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11,3),_Error11_date_time_Type())
error11_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error11_date_time.setStatus(_F)
_Error12_ObjectIdentity=ObjectIdentity
error12=_Error12_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12))
_Error12_time_stamp_Type=Integer32
_Error12_time_stamp_Object=MibScalar
error12_time_stamp=_Error12_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12,1),_Error12_time_stamp_Type())
error12_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error12_time_stamp.setStatus(_F)
_Error12_code_Type=Integer32
_Error12_code_Object=MibScalar
error12_code=_Error12_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12,2),_Error12_code_Type())
error12_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error12_code.setStatus(_F)
_Error12_date_time_Type=OctetString
_Error12_date_time_Object=MibScalar
error12_date_time=_Error12_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12,3),_Error12_date_time_Type())
error12_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error12_date_time.setStatus(_F)
_Error13_ObjectIdentity=ObjectIdentity
error13=_Error13_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13))
_Error13_time_stamp_Type=Integer32
_Error13_time_stamp_Object=MibScalar
error13_time_stamp=_Error13_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13,1),_Error13_time_stamp_Type())
error13_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error13_time_stamp.setStatus(_F)
_Error13_code_Type=Integer32
_Error13_code_Object=MibScalar
error13_code=_Error13_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13,2),_Error13_code_Type())
error13_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error13_code.setStatus(_F)
_Error13_date_time_Type=OctetString
_Error13_date_time_Object=MibScalar
error13_date_time=_Error13_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13,3),_Error13_date_time_Type())
error13_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error13_date_time.setStatus(_F)
_Error14_ObjectIdentity=ObjectIdentity
error14=_Error14_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14))
_Error14_time_stamp_Type=Integer32
_Error14_time_stamp_Object=MibScalar
error14_time_stamp=_Error14_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14,1),_Error14_time_stamp_Type())
error14_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error14_time_stamp.setStatus(_F)
_Error14_code_Type=Integer32
_Error14_code_Object=MibScalar
error14_code=_Error14_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14,2),_Error14_code_Type())
error14_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error14_code.setStatus(_F)
_Error14_date_time_Type=OctetString
_Error14_date_time_Object=MibScalar
error14_date_time=_Error14_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14,3),_Error14_date_time_Type())
error14_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error14_date_time.setStatus(_F)
_Error15_ObjectIdentity=ObjectIdentity
error15=_Error15_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15))
_Error15_time_stamp_Type=Integer32
_Error15_time_stamp_Object=MibScalar
error15_time_stamp=_Error15_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15,1),_Error15_time_stamp_Type())
error15_time_stamp.setMaxAccess(_A)
if mibBuilder.loadTexts:error15_time_stamp.setStatus(_F)
_Error15_code_Type=Integer32
_Error15_code_Object=MibScalar
error15_code=_Error15_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15,2),_Error15_code_Type())
error15_code.setMaxAccess(_A)
if mibBuilder.loadTexts:error15_code.setStatus(_F)
_Error15_date_time_Type=OctetString
_Error15_date_time_Object=MibScalar
error15_date_time=_Error15_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15,3),_Error15_date_time_Type())
error15_date_time.setMaxAccess(_A)
if mibBuilder.loadTexts:error15_date_time.setStatus(_F)
_Accounting_ObjectIdentity=ObjectIdentity
accounting=_Accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16))
_Printer_accounting_ObjectIdentity=ObjectIdentity
printer_accounting=_Printer_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1))
_Printed_media_usage_ObjectIdentity=ObjectIdentity
printed_media_usage=_Printed_media_usage_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1))
class _Printed_media_simplex_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,930576247))
_Printed_media_simplex_count_Type.__name__=_D
_Printed_media_simplex_count_Object=MibScalar
printed_media_simplex_count=_Printed_media_simplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,1),_Printed_media_simplex_count_Type())
printed_media_simplex_count.setMaxAccess(_A)
if mibBuilder.loadTexts:printed_media_simplex_count.setStatus(_F)
class _Printed_media_duplex_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,930576247))
_Printed_media_duplex_count_Type.__name__=_D
_Printed_media_duplex_count_Object=MibScalar
printed_media_duplex_count=_Printed_media_duplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,3),_Printed_media_duplex_count_Type())
printed_media_duplex_count.setMaxAccess(_A)
if mibBuilder.loadTexts:printed_media_duplex_count.setStatus(_F)
_Printer_color_accounting_ObjectIdentity=ObjectIdentity
printer_color_accounting=_Printer_color_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3))
_Printed_media_color_usage_ObjectIdentity=ObjectIdentity
printed_media_color_usage=_Printed_media_color_usage_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1))
_Printed_media_color_simplex_count_Type=Integer32
_Printed_media_color_simplex_count_Object=MibScalar
printed_media_color_simplex_count=_Printed_media_color_simplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1,1),_Printed_media_color_simplex_count_Type())
printed_media_color_simplex_count.setMaxAccess(_A)
if mibBuilder.loadTexts:printed_media_color_simplex_count.setStatus(_F)
_Printed_media_color_duplex_count_Type=Integer32
_Printed_media_color_duplex_count_Object=MibScalar
printed_media_color_duplex_count=_Printed_media_color_duplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1,3),_Printed_media_color_duplex_count_Type())
printed_media_color_duplex_count.setMaxAccess(_A)
if mibBuilder.loadTexts:printed_media_color_duplex_count.setStatus(_F)
_Source_subsystem_ObjectIdentity=ObjectIdentity
source_subsystem=_Source_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2))
_Scanner_ObjectIdentity=ObjectIdentity
scanner=_Scanner_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2))
_Settings_scanner_ObjectIdentity=ObjectIdentity
settings_scanner=_Settings_scanner_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1))
class _Scanner_accessory_adf_sheet_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Scanner_accessory_adf_sheet_count_Type.__name__=_D
_Scanner_accessory_adf_sheet_count_Object=MibScalar
scanner_accessory_adf_sheet_count=_Scanner_accessory_adf_sheet_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,20),_Scanner_accessory_adf_sheet_count_Type())
scanner_accessory_adf_sheet_count.setMaxAccess(_A)
if mibBuilder.loadTexts:scanner_accessory_adf_sheet_count.setStatus(_F)
class _Scanner_accessory_flatbed_scan_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Scanner_accessory_flatbed_scan_count_Type.__name__=_D
_Scanner_accessory_flatbed_scan_count_Object=MibScalar
scanner_accessory_flatbed_scan_count=_Scanner_accessory_flatbed_scan_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,21),_Scanner_accessory_flatbed_scan_count_Type())
scanner_accessory_flatbed_scan_count.setMaxAccess(_A)
if mibBuilder.loadTexts:scanner_accessory_flatbed_scan_count.setStatus(_F)
_Scanner_accessory_copy_job_scan_count_Type=Integer32
_Scanner_accessory_copy_job_scan_count_Object=MibScalar
scanner_accessory_copy_job_scan_count=_Scanner_accessory_copy_job_scan_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,61),_Scanner_accessory_copy_job_scan_count_Type())
scanner_accessory_copy_job_scan_count.setMaxAccess(_A)
if mibBuilder.loadTexts:scanner_accessory_copy_job_scan_count.setStatus(_F)
_Scanner_accessory_send_job_scan_count_Type=Integer32
_Scanner_accessory_send_job_scan_count_Object=MibScalar
scanner_accessory_send_job_scan_count=_Scanner_accessory_send_job_scan_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,62),_Scanner_accessory_send_job_scan_count_Type())
scanner_accessory_send_job_scan_count.setMaxAccess(_A)
if mibBuilder.loadTexts:scanner_accessory_send_job_scan_count.setStatus(_F)
_Scanner_accessory_total_copy_pages_printed_Type=Integer32
_Scanner_accessory_total_copy_pages_printed_Object=MibScalar
scanner_accessory_total_copy_pages_printed=_Scanner_accessory_total_copy_pages_printed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,63),_Scanner_accessory_total_copy_pages_printed_Type())
scanner_accessory_total_copy_pages_printed.setMaxAccess(_A)
if mibBuilder.loadTexts:scanner_accessory_total_copy_pages_printed.setStatus(_F)
class _Scan_to_folder_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999999))
_Scan_to_folder_count_Type.__name__=_D
_Scan_to_folder_count_Object=MibScalar
scan_to_folder_count=_Scan_to_folder_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,89),_Scan_to_folder_count_Type())
scan_to_folder_count.setMaxAccess(_A)
if mibBuilder.loadTexts:scan_to_folder_count.setStatus(_F)
class _Fax_job_scan_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999999))
_Fax_job_scan_count_Type.__name__=_D
_Fax_job_scan_count_Object=MibScalar
fax_job_scan_count=_Fax_job_scan_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,90),_Fax_job_scan_count_Type())
fax_job_scan_count.setMaxAccess(_A)
if mibBuilder.loadTexts:fax_job_scan_count.setStatus(_F)
_Processing_subsystem_ObjectIdentity=ObjectIdentity
processing_subsystem=_Processing_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3))
_Pdl_ObjectIdentity=ObjectIdentity
pdl=_Pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3))
_Pdl_pcl_ObjectIdentity=ObjectIdentity
pdl_pcl=_Pdl_pcl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3))
_Pcl_total_page_count_Type=Integer32
_Pcl_total_page_count_Object=MibScalar
pcl_total_page_count=_Pcl_total_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,5),_Pcl_total_page_count_Type())
pcl_total_page_count.setMaxAccess(_A)
if mibBuilder.loadTexts:pcl_total_page_count.setStatus(_F)
_Pdl_postscript_ObjectIdentity=ObjectIdentity
pdl_postscript=_Pdl_postscript_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4))
_Postscript_total_page_count_Type=Integer32
_Postscript_total_page_count_Object=MibScalar
postscript_total_page_count=_Postscript_total_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4,5),_Postscript_total_page_count_Type())
postscript_total_page_count.setMaxAccess(_A)
if mibBuilder.loadTexts:postscript_total_page_count.setStatus(_F)
_Fax_proc_sub_ObjectIdentity=ObjectIdentity
fax_proc_sub=_Fax_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7))
_Settings_fax_proc_sub_ObjectIdentity=ObjectIdentity
settings_fax_proc_sub=_Settings_fax_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1))
_Fax_print_page_count_Type=Integer32
_Fax_print_page_count_Object=MibScalar
fax_print_page_count=_Fax_print_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,32),_Fax_print_page_count_Type())
fax_print_page_count.setMaxAccess(_C)
if mibBuilder.loadTexts:fax_print_page_count.setStatus(_F)
_Status_fax_proc_sub_ObjectIdentity=ObjectIdentity
status_fax_proc_sub=_Status_fax_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2))
_Afax_send_page_count_Type=Integer32
_Afax_send_page_count_Object=MibScalar
afax_send_page_count=_Afax_send_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,11),_Afax_send_page_count_Type())
afax_send_page_count.setMaxAccess(_C)
if mibBuilder.loadTexts:afax_send_page_count.setStatus(_F)
_Afax_recv_page_count_Type=Integer32
_Afax_recv_page_count_Object=MibScalar
afax_recv_page_count=_Afax_recv_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,12),_Afax_recv_page_count_Type())
afax_recv_page_count.setMaxAccess(_C)
if mibBuilder.loadTexts:afax_recv_page_count.setStatus(_F)
_Destination_subsystem_ObjectIdentity=ObjectIdentity
destination_subsystem=_Destination_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4))
_Print_engine_ObjectIdentity=ObjectIdentity
print_engine=_Print_engine_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1))
_Status_prt_eng_ObjectIdentity=ObjectIdentity
status_prt_eng=_Status_prt_eng_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2))
_Total_engine_page_count_Type=Integer32
_Total_engine_page_count_Object=MibScalar
total_engine_page_count=_Total_engine_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,5),_Total_engine_page_count_Type())
total_engine_page_count.setMaxAccess(_C)
if mibBuilder.loadTexts:total_engine_page_count.setStatus(_F)
_Total_mono_page_count_Type=Integer32
_Total_mono_page_count_Object=MibScalar
total_mono_page_count=_Total_mono_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,6),_Total_mono_page_count_Type())
total_mono_page_count.setMaxAccess(_A)
if mibBuilder.loadTexts:total_mono_page_count.setStatus(_F)
_Total_color_page_count_Type=Integer32
_Total_color_page_count_Object=MibScalar
total_color_page_count=_Total_color_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,7),_Total_color_page_count_Type())
total_color_page_count.setMaxAccess(_A)
if mibBuilder.loadTexts:total_color_page_count.setStatus(_F)
_Duplex_page_count_Type=Integer32
_Duplex_page_count_Object=MibScalar
duplex_page_count=_Duplex_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,22),_Duplex_page_count_Type())
duplex_page_count.setMaxAccess(_A)
if mibBuilder.loadTexts:duplex_page_count.setStatus(_F)
_Consumables_ObjectIdentity=ObjectIdentity
consumables=_Consumables_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10))
_Consumables_1_ObjectIdentity=ObjectIdentity
consumables_1=_Consumables_1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1))
_Consumable_status_ObjectIdentity=ObjectIdentity
consumable_status=_Consumable_status_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1))
class _Consumable_status_cartridge_model_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Consumable_status_cartridge_model_Type.__name__=_H
_Consumable_status_cartridge_model_Object=MibScalar
consumable_status_cartridge_model=_Consumable_status_cartridge_model_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1,1),_Consumable_status_cartridge_model_Type())
consumable_status_cartridge_model.setMaxAccess(_A)
if mibBuilder.loadTexts:consumable_status_cartridge_model.setStatus(_F)
class _Consumable_status_manufacturing_date_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Consumable_status_manufacturing_date_Type.__name__=_H
_Consumable_status_manufacturing_date_Object=MibScalar
consumable_status_manufacturing_date=_Consumable_status_manufacturing_date_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1,2),_Consumable_status_manufacturing_date_Type())
consumable_status_manufacturing_date.setMaxAccess(_A)
if mibBuilder.loadTexts:consumable_status_manufacturing_date.setStatus(_F)
class _Consumable_status_serial_number_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Consumable_status_serial_number_Type.__name__=_H
_Consumable_status_serial_number_Object=MibScalar
consumable_status_serial_number=_Consumable_status_serial_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1,3),_Consumable_status_serial_number_Type())
consumable_status_serial_number.setMaxAccess(_A)
if mibBuilder.loadTexts:consumable_status_serial_number.setStatus(_F)
class _Consumable_status_first_install_date_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Consumable_status_first_install_date_Type.__name__=_H
_Consumable_status_first_install_date_Object=MibScalar
consumable_status_first_install_date=_Consumable_status_first_install_date_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1,8),_Consumable_status_first_install_date_Type())
consumable_status_first_install_date.setMaxAccess(_A)
if mibBuilder.loadTexts:consumable_status_first_install_date.setStatus(_F)
_Interface_ObjectIdentity=ObjectIdentity
interface=_Interface_ObjectIdentity((1,3,6,1,4,1,11,2,4))
_NpCard_ObjectIdentity=ObjectIdentity
npCard=_NpCard_ObjectIdentity((1,3,6,1,4,1,11,2,4,3))
_NpSys_ObjectIdentity=ObjectIdentity
npSys=_NpSys_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,1))
class _NpSysModelNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NpSysModelNumber_Type.__name__=_G
_NpSysModelNumber_Object=MibScalar
npSysModelNumber=_NpSysModelNumber_Object((1,3,6,1,4,1,11,2,4,3,1,10),_NpSysModelNumber_Type())
npSysModelNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:npSysModelNumber.setStatus(_B)
_NpSysCardServices1_Type=Integer32
_NpSysCardServices1_Object=MibScalar
npSysCardServices1=_NpSysCardServices1_Object((1,3,6,1,4,1,11,2,4,3,1,16),_NpSysCardServices1_Type())
npSysCardServices1.setMaxAccess(_A)
if mibBuilder.loadTexts:npSysCardServices1.setStatus(_B)
_NpSysCardServices2_Type=Integer32
_NpSysCardServices2_Object=MibScalar
npSysCardServices2=_NpSysCardServices2_Object((1,3,6,1,4,1,11,2,4,3,1,17),_NpSysCardServices2_Type())
npSysCardServices2.setMaxAccess(_A)
if mibBuilder.loadTexts:npSysCardServices2.setStatus(_B)
_NpSysCardServices3_Type=Integer32
_NpSysCardServices3_Object=MibScalar
npSysCardServices3=_NpSysCardServices3_Object((1,3,6,1,4,1,11,2,4,3,1,22),_NpSysCardServices3_Type())
npSysCardServices3.setMaxAccess(_A)
if mibBuilder.loadTexts:npSysCardServices3.setStatus(_B)
_NpSysFactoryMacAddress_Type=OctetString
_NpSysFactoryMacAddress_Object=MibScalar
npSysFactoryMacAddress=_NpSysFactoryMacAddress_Object((1,3,6,1,4,1,11,2,4,3,1,23),_NpSysFactoryMacAddress_Type())
npSysFactoryMacAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:npSysFactoryMacAddress.setStatus(_B)
_NpCfg_ObjectIdentity=ObjectIdentity
npCfg=_NpCfg_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,5))
class _NpCfgSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3),(_g,4),('dhcp',5),(_h,6),(_i,7),('rarp',8),(_A,9),(_j,10)))
_NpCfgSource_Type.__name__=_D
_NpCfgSource_Object=MibScalar
npCfgSource=_NpCfgSource_Object((1,3,6,1,4,1,11,2,4,3,5,1),_NpCfgSource_Type())
npCfgSource.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSource.setStatus(_B)
_NpCfgYiaddr_Type=IpAddress
_NpCfgYiaddr_Object=MibScalar
npCfgYiaddr=_NpCfgYiaddr_Object((1,3,6,1,4,1,11,2,4,3,5,2),_NpCfgYiaddr_Type())
npCfgYiaddr.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgYiaddr.setStatus(_B)
_NpCfgSiaddr_Type=IpAddress
_NpCfgSiaddr_Object=MibScalar
npCfgSiaddr=_NpCfgSiaddr_Object((1,3,6,1,4,1,11,2,4,3,5,3),_NpCfgSiaddr_Type())
npCfgSiaddr.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgSiaddr.setStatus(_B)
_NpCfgSubnetMask_Type=IpAddress
_NpCfgSubnetMask_Object=MibScalar
npCfgSubnetMask=_NpCfgSubnetMask_Object((1,3,6,1,4,1,11,2,4,3,5,12),_NpCfgSubnetMask_Type())
npCfgSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSubnetMask.setStatus(_B)
_NpCfgDefaultGateway_Type=IpAddress
_NpCfgDefaultGateway_Object=MibScalar
npCfgDefaultGateway=_NpCfgDefaultGateway_Object((1,3,6,1,4,1,11,2,4,3,5,13),_NpCfgDefaultGateway_Type())
npCfgDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgDefaultGateway.setStatus(_B)
class _NpCfgDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NpCfgDomainName_Type.__name__=_G
_NpCfgDomainName_Object=MibScalar
npCfgDomainName=_NpCfgDomainName_Object((1,3,6,1,4,1,11,2,4,3,5,16),_NpCfgDomainName_Type())
npCfgDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgDomainName.setStatus(_B)
_NpCfgIPP_Type=Integer32
_NpCfgIPP_Object=MibScalar
npCfgIPP=_NpCfgIPP_Object((1,3,6,1,4,1,11,2,4,3,5,18),_NpCfgIPP_Type())
npCfgIPP.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgIPP.setStatus(_B)
_NpCfgDNSNameServerId_Type=IpAddress
_NpCfgDNSNameServerId_Object=MibScalar
npCfgDNSNameServerId=_NpCfgDNSNameServerId_Object((1,3,6,1,4,1,11,2,4,3,5,21),_NpCfgDNSNameServerId_Type())
npCfgDNSNameServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgDNSNameServerId.setStatus(_B)
_NpCfgWINSNameServerIdPri_Type=IpAddress
_NpCfgWINSNameServerIdPri_Object=MibScalar
npCfgWINSNameServerIdPri=_NpCfgWINSNameServerIdPri_Object((1,3,6,1,4,1,11,2,4,3,5,22),_NpCfgWINSNameServerIdPri_Type())
npCfgWINSNameServerIdPri.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgWINSNameServerIdPri.setStatus(_B)
_NpCfgWINSNameServerIdSec_Type=IpAddress
_NpCfgWINSNameServerIdSec_Object=MibScalar
npCfgWINSNameServerIdSec=_NpCfgWINSNameServerIdSec_Object((1,3,6,1,4,1,11,2,4,3,5,23),_NpCfgWINSNameServerIdSec_Type())
npCfgWINSNameServerIdSec.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgWINSNameServerIdSec.setStatus(_B)
class _NpCfgPasswd1Verify_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NpCfgPasswd1Verify_Type.__name__=_G
_NpCfgPasswd1Verify_Object=MibScalar
npCfgPasswd1Verify=_NpCfgPasswd1Verify_Object((1,3,6,1,4,1,11,2,4,3,5,28),_NpCfgPasswd1Verify_Type())
npCfgPasswd1Verify.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgPasswd1Verify.setStatus(_B)
_NpCfgPasswd1_Type=DisplayString
_NpCfgPasswd1_Object=MibScalar
npCfgPasswd1=_NpCfgPasswd1_Object((1,3,6,1,4,1,11,2,4,3,5,29),_NpCfgPasswd1_Type())
npCfgPasswd1.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgPasswd1.setStatus(_B)
class _NpCfgLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('autoNegotiate',1),('full10T',2),('half10T',3),('full100T',4),('half100T',5),('auto100T',6),('full1000T',7)))
_NpCfgLinkType_Type.__name__=_D
_NpCfgLinkType_Object=MibScalar
npCfgLinkType=_NpCfgLinkType_Object((1,3,6,1,4,1,11,2,4,3,5,35),_NpCfgLinkType_Type())
npCfgLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgLinkType.setStatus(_B)
class _NpCfgSnmpDefaultReadCmnty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCfgSnmpDefaultReadCmnty_Type.__name__=_D
_NpCfgSnmpDefaultReadCmnty_Object=MibScalar
npCfgSnmpDefaultReadCmnty=_NpCfgSnmpDefaultReadCmnty_Object((1,3,6,1,4,1,11,2,4,3,5,40),_NpCfgSnmpDefaultReadCmnty_Type())
npCfgSnmpDefaultReadCmnty.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSnmpDefaultReadCmnty.setStatus(_B)
class _NpCfgBonjourDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NpCfgBonjourDomainName_Type.__name__=_G
_NpCfgBonjourDomainName_Object=MibScalar
npCfgBonjourDomainName=_NpCfgBonjourDomainName_Object((1,3,6,1,4,1,11,2,4,3,5,46),_NpCfgBonjourDomainName_Type())
npCfgBonjourDomainName.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgBonjourDomainName.setStatus(_B)
_NpCfgDNSNameServerIdSecondary_Type=IpAddress
_NpCfgDNSNameServerIdSecondary_Object=MibScalar
npCfgDNSNameServerIdSecondary=_NpCfgDNSNameServerIdSecondary_Object((1,3,6,1,4,1,11,2,4,3,5,47),_NpCfgDNSNameServerIdSecondary_Type())
npCfgDNSNameServerIdSecondary.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgDNSNameServerIdSecondary.setStatus(_B)
_NpCfgIPv6DomainName_Type=OctetString
_NpCfgIPv6DomainName_Object=MibScalar
npCfgIPv6DomainName=_NpCfgIPv6DomainName_Object((1,3,6,1,4,1,11,2,4,3,5,49),_NpCfgIPv6DomainName_Type())
npCfgIPv6DomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgIPv6DomainName.setStatus(_B)
class _NpCfgIPv6ConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ipv6-going-down',0),('ipv6-is-up',1)))
_NpCfgIPv6ConfigState_Type.__name__=_D
_NpCfgIPv6ConfigState_Object=MibScalar
npCfgIPv6ConfigState=_NpCfgIPv6ConfigState_Object((1,3,6,1,4,1,11,2,4,3,5,50),_NpCfgIPv6ConfigState_Type())
npCfgIPv6ConfigState.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPv6ConfigState.setStatus(_B)
_NpCfgIPAddrTable_ObjectIdentity=ObjectIdentity
npCfgIPAddrTable=_NpCfgIPAddrTable_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,5,53))
_NpCfgIPAddrEntry_ObjectIdentity=ObjectIdentity
npCfgIPAddrEntry=_NpCfgIPAddrEntry_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,5,53,1))
class _NpCfgIPAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NpCfgIPAddrIndex_Type.__name__=_D
_NpCfgIPAddrIndex_Object=MibScalar
npCfgIPAddrIndex=_NpCfgIPAddrIndex_Object((1,3,6,1,4,1,11,2,4,3,5,53,1,1),_NpCfgIPAddrIndex_Type())
npCfgIPAddrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPAddrIndex.setStatus(_B)
class _NpCfgIPAddrType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,16)));namedValues=NamedValues(*((_Q,0),('ipv4',1),('ipv6',2),('ipv4z',3),('ipv6z',4),('dns',16)))
_NpCfgIPAddrType_Type.__name__=_b
_NpCfgIPAddrType_Object=MibScalar
npCfgIPAddrType=_NpCfgIPAddrType_Object((1,3,6,1,4,1,11,2,4,3,5,53,1,2),_NpCfgIPAddrType_Type())
npCfgIPAddrType.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPAddrType.setStatus(_B)
class _NpCfgIPAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NpCfgIPAddress_Type.__name__=_a
_NpCfgIPAddress_Object=MibScalar
npCfgIPAddress=_NpCfgIPAddress_Object((1,3,6,1,4,1,11,2,4,3,5,53,1,3),_NpCfgIPAddress_Type())
npCfgIPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPAddress.setStatus(_B)
_NpCfgIPAddrIfIndex_Type=InterfaceIndex
_NpCfgIPAddrIfIndex_Object=MibScalar
npCfgIPAddrIfIndex=_NpCfgIPAddrIfIndex_Object((1,3,6,1,4,1,11,2,4,3,5,53,1,4),_NpCfgIPAddrIfIndex_Type())
npCfgIPAddrIfIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPAddrIfIndex.setStatus(_B)
class _NpCfgIPAddrConfigBy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3),(_g,4),('dhcpv4',5),(_h,6),(_i,7),('rarp',8),(_A,9),(_j,10),('dhcpv6',11),('stateless',12),('linklocal',13)))
_NpCfgIPAddrConfigBy_Type.__name__=_D
_NpCfgIPAddrConfigBy_Object=MibScalar
npCfgIPAddrConfigBy=_NpCfgIPAddrConfigBy_Object((1,3,6,1,4,1,11,2,4,3,5,53,1,5),_NpCfgIPAddrConfigBy_Type())
npCfgIPAddrConfigBy.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPAddrConfigBy.setStatus(_B)
class _NpCfgIPAddrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('undefined',0),('valid',1),(_T,2)))
_NpCfgIPAddrStatus_Type.__name__=_D
_NpCfgIPAddrStatus_Object=MibScalar
npCfgIPAddrStatus=_NpCfgIPAddrStatus_Object((1,3,6,1,4,1,11,2,4,3,5,53,1,6),_NpCfgIPAddrStatus_Type())
npCfgIPAddrStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPAddrStatus.setStatus(_B)
_NpCfgIPAddrPrefixLength_Type=InetAddressPrefixLength
_NpCfgIPAddrPrefixLength_Object=MibScalar
npCfgIPAddrPrefixLength=_NpCfgIPAddrPrefixLength_Object((1,3,6,1,4,1,11,2,4,3,5,53,1,7),_NpCfgIPAddrPrefixLength_Type())
npCfgIPAddrPrefixLength.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPAddrPrefixLength.setStatus(_B)
_NpCfgIPAddrValidLifetime_Type=OctetString
_NpCfgIPAddrValidLifetime_Object=MibScalar
npCfgIPAddrValidLifetime=_NpCfgIPAddrValidLifetime_Object((1,3,6,1,4,1,11,2,4,3,5,53,1,8),_NpCfgIPAddrValidLifetime_Type())
npCfgIPAddrValidLifetime.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPAddrValidLifetime.setStatus(_B)
_NpCfgIPAddrPrefLifetime_Type=OctetString
_NpCfgIPAddrPrefLifetime_Object=MibScalar
npCfgIPAddrPrefLifetime=_NpCfgIPAddrPrefLifetime_Object((1,3,6,1,4,1,11,2,4,3,5,53,1,9),_NpCfgIPAddrPrefLifetime_Type())
npCfgIPAddrPrefLifetime.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgIPAddrPrefLifetime.setStatus(_B)
_NpCfgIPv6DNSAddr1_Type=InetAddress
_NpCfgIPv6DNSAddr1_Object=MibScalar
npCfgIPv6DNSAddr1=_NpCfgIPv6DNSAddr1_Object((1,3,6,1,4,1,11,2,4,3,5,56),_NpCfgIPv6DNSAddr1_Type())
npCfgIPv6DNSAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgIPv6DNSAddr1.setStatus(_B)
_NpCfgIPv6DNSAddr2_Type=InetAddress
_NpCfgIPv6DNSAddr2_Object=MibScalar
npCfgIPv6DNSAddr2=_NpCfgIPv6DNSAddr2_Object((1,3,6,1,4,1,11,2,4,3,5,57),_NpCfgIPv6DNSAddr2_Type())
npCfgIPv6DNSAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgIPv6DNSAddr2.setStatus(_B)
_NpCfgIPConfigPrecedence_Type=OctetString
_NpCfgIPConfigPrecedence_Object=MibScalar
npCfgIPConfigPrecedence=_NpCfgIPConfigPrecedence_Object((1,3,6,1,4,1,11,2,4,3,5,59),_NpCfgIPConfigPrecedence_Type())
npCfgIPConfigPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgIPConfigPrecedence.setStatus(_B)
class _NpCfgSTAWirelessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bg-Mode',0),('bgn-Mode',1)))
_NpCfgSTAWirelessMode_Type.__name__=_D
_NpCfgSTAWirelessMode_Object=MibScalar
npCfgSTAWirelessMode=_NpCfgSTAWirelessMode_Object((1,3,6,1,4,1,11,2,4,3,5,72),_NpCfgSTAWirelessMode_Type())
npCfgSTAWirelessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSTAWirelessMode.setStatus(_B)
class _NpCfgWirelessDirectSSIDPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_NpCfgWirelessDirectSSIDPrefix_Type.__name__=_G
_NpCfgWirelessDirectSSIDPrefix_Object=MibScalar
npCfgWirelessDirectSSIDPrefix=_NpCfgWirelessDirectSSIDPrefix_Object((1,3,6,1,4,1,11,2,4,3,5,86),_NpCfgWirelessDirectSSIDPrefix_Type())
npCfgWirelessDirectSSIDPrefix.setMaxAccess(_A)
if mibBuilder.loadTexts:npCfgWirelessDirectSSIDPrefix.setStatus(_B)
class _NpCfgWirelessDirectSSIDSuffix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_NpCfgWirelessDirectSSIDSuffix_Type.__name__=_G
_NpCfgWirelessDirectSSIDSuffix_Object=MibScalar
npCfgWirelessDirectSSIDSuffix=_NpCfgWirelessDirectSSIDSuffix_Object((1,3,6,1,4,1,11,2,4,3,5,87),_NpCfgWirelessDirectSSIDSuffix_Type())
npCfgWirelessDirectSSIDSuffix.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgWirelessDirectSSIDSuffix.setStatus(_B)
_NpCtl_ObjectIdentity=ObjectIdentity
npCtl=_NpCtl_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,7))
_NpCtlProtocolSet_Type=Integer32
_NpCtlProtocolSet_Object=MibScalar
npCtlProtocolSet=_NpCtlProtocolSet_Object((1,3,6,1,4,1,11,2,4,3,7,9),_NpCtlProtocolSet_Type())
npCtlProtocolSet.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlProtocolSet.setStatus(_B)
class _NpCtlSLP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCtlSLP_Type.__name__=_D
_NpCtlSLP_Object=MibScalar
npCtlSLP=_NpCtlSLP_Object((1,3,6,1,4,1,11,2,4,3,7,21),_NpCtlSLP_Type())
npCtlSLP.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlSLP.setStatus(_B)
class _NpCtlLPD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCtlLPD_Type.__name__=_D
_NpCtlLPD_Object=MibScalar
npCtlLPD=_NpCtlLPD_Object((1,3,6,1,4,1,11,2,4,3,7,22),_NpCtlLPD_Type())
npCtlLPD.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlLPD.setStatus(_B)
class _NpCtl9100_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCtl9100_Type.__name__=_D
_NpCtl9100_Object=MibScalar
npCtl9100=_NpCtl9100_Object((1,3,6,1,4,1,11,2,4,3,7,24),_NpCtl9100_Type())
npCtl9100.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtl9100.setStatus(_B)
class _NpCtlSnmpVersionAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('snmpV1RW-snmpV3RW',1),('snmpV1RO-snmpV3RW',2),('snmpV1NoAccess-snmpV3RW',3),('snmpV1RW-snmpV3NoAccess',4),('snmpV1RO-snmpV3NoAccess',5)))
_NpCtlSnmpVersionAccess_Type.__name__=_D
_NpCtlSnmpVersionAccess_Object=MibScalar
npCtlSnmpVersionAccess=_NpCtlSnmpVersionAccess_Object((1,3,6,1,4,1,11,2,4,3,7,27),_NpCtlSnmpVersionAccess_Type())
npCtlSnmpVersionAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlSnmpVersionAccess.setStatus(_B)
class _NpCtlSnmpV3InitAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4)));namedValues=NamedValues(*(('Destroy',0),('blockInitEncrypt',4)))
_NpCtlSnmpV3InitAccount_Type.__name__=_D
_NpCtlSnmpV3InitAccount_Object=MibScalar
npCtlSnmpV3InitAccount=_NpCtlSnmpV3InitAccount_Object((1,3,6,1,4,1,11,2,4,3,7,28),_NpCtlSnmpV3InitAccount_Type())
npCtlSnmpV3InitAccount.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlSnmpV3InitAccount.setStatus(_B)
class _NpCtlBonjour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCtlBonjour_Type.__name__=_D
_NpCtlBonjour_Object=MibScalar
npCtlBonjour=_NpCtlBonjour_Object((1,3,6,1,4,1,11,2,4,3,7,29),_NpCtlBonjour_Type())
npCtlBonjour.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlBonjour.setStatus(_B)
class _NpCtlNetworkConnectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto-cable-detect',1),('disable-radio',2),('disable-wired',3)))
_NpCtlNetworkConnectionMode_Type.__name__=_D
_NpCtlNetworkConnectionMode_Object=MibScalar
npCtlNetworkConnectionMode=_NpCtlNetworkConnectionMode_Object((1,3,6,1,4,1,11,2,4,3,7,32),_NpCtlNetworkConnectionMode_Type())
npCtlNetworkConnectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlNetworkConnectionMode.setStatus(_B)
class _NpCtlWSDiscovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_k,1)))
_NpCtlWSDiscovery_Type.__name__=_D
_NpCtlWSDiscovery_Object=MibScalar
npCtlWSDiscovery=_NpCtlWSDiscovery_Object((1,3,6,1,4,1,11,2,4,3,7,36),_NpCtlWSDiscovery_Type())
npCtlWSDiscovery.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWSDiscovery.setStatus(_B)
class _NpCtlWSPrint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_k,1)))
_NpCtlWSPrint_Type.__name__=_D
_NpCtlWSPrint_Object=MibScalar
npCtlWSPrint=_NpCtlWSPrint_Object((1,3,6,1,4,1,11,2,4,3,7,37),_NpCtlWSPrint_Type())
npCtlWSPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWSPrint.setStatus(_B)
class _NpCtlWPAD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_W,0),('automatic-Web-Proxy',1),('manual-url',2),('manual-proxy-settings',3)))
_NpCtlWPAD_Type.__name__=_D
_NpCtlWPAD_Object=MibScalar
npCtlWPAD=_NpCtlWPAD_Object((1,3,6,1,4,1,11,2,4,3,7,39),_NpCtlWPAD_Type())
npCtlWPAD.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWPAD.setStatus(_B)
class _NpCtlFpDot11WirelessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_NpCtlFpDot11WirelessState_Type.__name__=_D
_NpCtlFpDot11WirelessState_Object=MibScalar
npCtlFpDot11WirelessState=_NpCtlFpDot11WirelessState_Object((1,3,6,1,4,1,11,2,4,3,7,47),_NpCtlFpDot11WirelessState_Type())
npCtlFpDot11WirelessState.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlFpDot11WirelessState.setStatus(_B)
class _NpCtlDot11nSTAGuardInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('Auto',0),('Short',1),('Long',2)))
_NpCtlDot11nSTAGuardInterval_Type.__name__=_D
_NpCtlDot11nSTAGuardInterval_Object=MibScalar
npCtlDot11nSTAGuardInterval=_NpCtlDot11nSTAGuardInterval_Object((1,3,6,1,4,1,11,2,4,3,7,51),_NpCtlDot11nSTAGuardInterval_Type())
npCtlDot11nSTAGuardInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlDot11nSTAGuardInterval.setStatus(_B)
class _NpCtlDot11nSTAAMSDUAggregation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_NpCtlDot11nSTAAMSDUAggregation_Type.__name__=_D
_NpCtlDot11nSTAAMSDUAggregation_Object=MibScalar
npCtlDot11nSTAAMSDUAggregation=_NpCtlDot11nSTAAMSDUAggregation_Object((1,3,6,1,4,1,11,2,4,3,7,52),_NpCtlDot11nSTAAMSDUAggregation_Type())
npCtlDot11nSTAAMSDUAggregation.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlDot11nSTAAMSDUAggregation.setStatus(_B)
class _NpCtlDot11nSTABlockACKs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_NpCtlDot11nSTABlockACKs_Type.__name__=_D
_NpCtlDot11nSTABlockACKs_Object=MibScalar
npCtlDot11nSTABlockACKs=_NpCtlDot11nSTABlockACKs_Object((1,3,6,1,4,1,11,2,4,3,7,53),_NpCtlDot11nSTABlockACKs_Type())
npCtlDot11nSTABlockACKs.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlDot11nSTABlockACKs.setStatus(_B)
class _NpCtlDot11nSTAAMPDUAggregation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_NpCtlDot11nSTAAMPDUAggregation_Type.__name__=_D
_NpCtlDot11nSTAAMPDUAggregation_Object=MibScalar
npCtlDot11nSTAAMPDUAggregation=_NpCtlDot11nSTAAMPDUAggregation_Object((1,3,6,1,4,1,11,2,4,3,7,54),_NpCtlDot11nSTAAMPDUAggregation_Type())
npCtlDot11nSTAAMPDUAggregation.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlDot11nSTAAMPDUAggregation.setStatus(_B)
class _NpCtlWirelessDirectSSIDBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-allowed',0),('allowed',1)))
_NpCtlWirelessDirectSSIDBroadcast_Type.__name__=_D
_NpCtlWirelessDirectSSIDBroadcast_Object=MibScalar
npCtlWirelessDirectSSIDBroadcast=_NpCtlWirelessDirectSSIDBroadcast_Object((1,3,6,1,4,1,11,2,4,3,7,57),_NpCtlWirelessDirectSSIDBroadcast_Type())
npCtlWirelessDirectSSIDBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWirelessDirectSSIDBroadcast.setStatus(_B)
class _NpCtlWirelessDirectHidePassphrase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('show',0),('hide',1)))
_NpCtlWirelessDirectHidePassphrase_Type.__name__=_D
_NpCtlWirelessDirectHidePassphrase_Object=MibScalar
npCtlWirelessDirectHidePassphrase=_NpCtlWirelessDirectHidePassphrase_Object((1,3,6,1,4,1,11,2,4,3,7,58),_NpCtlWirelessDirectHidePassphrase_Type())
npCtlWirelessDirectHidePassphrase.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWirelessDirectHidePassphrase.setStatus(_c)
class _NpCtlDeviceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('WiredStationMode',1),('WirelessStationMode',2),('AccessPointMode',3)))
_NpCtlDeviceMode_Type.__name__=_D
_NpCtlDeviceMode_Object=MibScalar
npCtlDeviceMode=_NpCtlDeviceMode_Object((1,3,6,1,4,1,11,2,4,3,7,67),_NpCtlDeviceMode_Type())
npCtlDeviceMode.setMaxAccess(_A)
if mibBuilder.loadTexts:npCtlDeviceMode.setStatus(_B)
class _NpCtlWirelessSTAState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_U,1)))
_NpCtlWirelessSTAState_Type.__name__=_D
_NpCtlWirelessSTAState_Object=MibScalar
npCtlWirelessSTAState=_NpCtlWirelessSTAState_Object((1,3,6,1,4,1,11,2,4,3,7,73),_NpCtlWirelessSTAState_Type())
npCtlWirelessSTAState.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWirelessSTAState.setStatus(_B)
class _NpCtlWirelessDirectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_U,1)))
_NpCtlWirelessDirectState_Type.__name__=_D
_NpCtlWirelessDirectState_Object=MibScalar
npCtlWirelessDirectState=_NpCtlWirelessDirectState_Object((1,3,6,1,4,1,11,2,4,3,7,74),_NpCtlWirelessDirectState_Type())
npCtlWirelessDirectState.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWirelessDirectState.setStatus(_B)
_NpNpi_ObjectIdentity=ObjectIdentity
npNpi=_NpNpi_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,8))
_NpNpiPeripheralAttributeEntry_ObjectIdentity=ObjectIdentity
npNpiPeripheralAttributeEntry=_NpNpiPeripheralAttributeEntry_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,8,3))
class _NpNpiPaeClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('printer',1),('plotter',2),('xStation',3)))
_NpNpiPaeClass_Type.__name__=_D
_NpNpiPaeClass_Object=MibScalar
npNpiPaeClass=_NpNpiPaeClass_Object((1,3,6,1,4,1,11,2,4,3,8,3,2),_NpNpiPaeClass_Type())
npNpiPaeClass.setMaxAccess(_A)
if mibBuilder.loadTexts:npNpiPaeClass.setStatus(_B)
class _NpNpiPaeIdentification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*(('laserjet-IIISI',1),('laserjet-4SI',5)))
_NpNpiPaeIdentification_Type.__name__=_D
_NpNpiPaeIdentification_Object=MibScalar
npNpiPaeIdentification=_NpNpiPaeIdentification_Object((1,3,6,1,4,1,11,2,4,3,8,3,3),_NpNpiPaeIdentification_Type())
npNpiPaeIdentification.setMaxAccess(_A)
if mibBuilder.loadTexts:npNpiPaeIdentification.setStatus(_B)
_NpNpiCardAttributeEntry_ObjectIdentity=ObjectIdentity
npNpiCardAttributeEntry=_NpNpiCardAttributeEntry_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,8,4))
class _NpNpiCaeClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('rs-232',1),('centronics',2),('csma-cd-network',3),('token-ring-network',4),('scsi',5),('hpib',6),('localtalk',7),('hpna',8),('usb',9),('firewire',10),('bluetooth',11),('ieee802-11b',12)))
_NpNpiCaeClass_Type.__name__=_D
_NpNpiCaeClass_Object=MibScalar
npNpiCaeClass=_NpNpiCaeClass_Object((1,3,6,1,4,1,11,2,4,3,8,4,2),_NpNpiCaeClass_Type())
npNpiCaeClass.setMaxAccess(_A)
if mibBuilder.loadTexts:npNpiCaeClass.setStatus(_B)
_NpIpx_ObjectIdentity=ObjectIdentity
npIpx=_NpIpx_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,10))
_NpIpxSapInfo_Type=OctetString
_NpIpxSapInfo_Object=MibScalar
npIpxSapInfo=_NpIpxSapInfo_Object((1,3,6,1,4,1,11,2,4,3,10,6),_NpIpxSapInfo_Type())
npIpxSapInfo.setMaxAccess(_A)
if mibBuilder.loadTexts:npIpxSapInfo.setStatus(_B)
_NpIpxGetUnitCfgResp2_Type=OctetString
_NpIpxGetUnitCfgResp2_Object=MibScalar
npIpxGetUnitCfgResp2=_NpIpxGetUnitCfgResp2_Object((1,3,6,1,4,1,11,2,4,3,10,7),_NpIpxGetUnitCfgResp2_Type())
npIpxGetUnitCfgResp2.setMaxAccess(_A)
if mibBuilder.loadTexts:npIpxGetUnitCfgResp2.setStatus(_B)
class _NpIpxRcfgAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_NpIpxRcfgAddress_Type.__name__=_G
_NpIpxRcfgAddress_Object=MibScalar
npIpxRcfgAddress=_NpIpxRcfgAddress_Object((1,3,6,1,4,1,11,2,4,3,10,13),_NpIpxRcfgAddress_Type())
npIpxRcfgAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:npIpxRcfgAddress.setStatus(_B)
_NpPort_ObjectIdentity=ObjectIdentity
npPort=_NpPort_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,13))
class _NpPortNumPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NpPortNumPorts_Type.__name__=_D
_NpPortNumPorts_Object=MibScalar
npPortNumPorts=_NpPortNumPorts_Object((1,3,6,1,4,1,11,2,4,3,13,1),_NpPortNumPorts_Type())
npPortNumPorts.setMaxAccess(_A)
if mibBuilder.loadTexts:npPortNumPorts.setStatus(_B)
_NpWeb_ObjectIdentity=ObjectIdentity
npWeb=_NpWeb_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,18))
class _NpWebProxyServerId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NpWebProxyServerId_Type.__name__=_G
_NpWebProxyServerId_Object=MibScalar
npWebProxyServerId=_NpWebProxyServerId_Object((1,3,6,1,4,1,11,2,4,3,18,12),_NpWebProxyServerId_Type())
npWebProxyServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:npWebProxyServerId.setStatus(_B)
_NpWebProxyServerPort_Type=Integer32
_NpWebProxyServerPort_Object=MibScalar
npWebProxyServerPort=_NpWebProxyServerPort_Object((1,3,6,1,4,1,11,2,4,3,18,13),_NpWebProxyServerPort_Type())
npWebProxyServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:npWebProxyServerPort.setStatus(_B)
class _NpWebProxyUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NpWebProxyUserName_Type.__name__=_G
_NpWebProxyUserName_Object=MibScalar
npWebProxyUserName=_NpWebProxyUserName_Object((1,3,6,1,4,1,11,2,4,3,18,14),_NpWebProxyUserName_Type())
npWebProxyUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:npWebProxyUserName.setStatus(_B)
class _NpWebProxyUserPasswd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NpWebProxyUserPasswd_Type.__name__=_G
_NpWebProxyUserPasswd_Object=MibScalar
npWebProxyUserPasswd=_NpWebProxyUserPasswd_Object((1,3,6,1,4,1,11,2,4,3,18,15),_NpWebProxyUserPasswd_Type())
npWebProxyUserPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:npWebProxyUserPasswd.setStatus(_B)
_NpSecurity_ObjectIdentity=ObjectIdentity
npSecurity=_NpSecurity_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20))
class _NpSecurityDot11ServerAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16)));namedValues=NamedValues(*(('eap-md5',1),('eap-tls',2),('leap',4),('peap',8),('ttls',16)))
_NpSecurityDot11ServerAuthentication_Type.__name__=_D
_NpSecurityDot11ServerAuthentication_Object=MibScalar
npSecurityDot11ServerAuthentication=_NpSecurityDot11ServerAuthentication_Object((1,3,6,1,4,1,11,2,4,3,20,1),_NpSecurityDot11ServerAuthentication_Type())
npSecurityDot11ServerAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11ServerAuthentication.setStatus(_B)
class _NpSecurityDot1xEapMd5Identity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_NpSecurityDot1xEapMd5Identity_Type.__name__=_G
_NpSecurityDot1xEapMd5Identity_Object=MibScalar
npSecurityDot1xEapMd5Identity=_NpSecurityDot1xEapMd5Identity_Object((1,3,6,1,4,1,11,2,4,3,20,2),_NpSecurityDot1xEapMd5Identity_Type())
npSecurityDot1xEapMd5Identity.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot1xEapMd5Identity.setStatus(_B)
class _NpSecurityDot1xTLSAuthServerId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NpSecurityDot1xTLSAuthServerId_Type.__name__=_G
_NpSecurityDot1xTLSAuthServerId_Object=MibScalar
npSecurityDot1xTLSAuthServerId=_NpSecurityDot1xTLSAuthServerId_Object((1,3,6,1,4,1,11,2,4,3,20,3),_NpSecurityDot1xTLSAuthServerId_Type())
npSecurityDot1xTLSAuthServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot1xTLSAuthServerId.setStatus(_B)
class _NpSecurityPublicKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NpSecurityPublicKey_Type.__name__=_G
_NpSecurityPublicKey_Object=MibScalar
npSecurityPublicKey=_NpSecurityPublicKey_Object((1,3,6,1,4,1,11,2,4,3,20,4),_NpSecurityPublicKey_Type())
npSecurityPublicKey.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityPublicKey.setStatus(_B)
class _NpSecurityDot11EncryptedDot11NetworkName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_NpSecurityDot11EncryptedDot11NetworkName_Type.__name__=_G
_NpSecurityDot11EncryptedDot11NetworkName_Object=MibScalar
npSecurityDot11EncryptedDot11NetworkName=_NpSecurityDot11EncryptedDot11NetworkName_Object((1,3,6,1,4,1,11,2,4,3,20,5),_NpSecurityDot11EncryptedDot11NetworkName_Type())
npSecurityDot11EncryptedDot11NetworkName.setMaxAccess(_J)
if mibBuilder.loadTexts:npSecurityDot11EncryptedDot11NetworkName.setStatus(_B)
class _NpSecurityDot11EncryptedDot1xEapMd5Secret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_NpSecurityDot11EncryptedDot1xEapMd5Secret_Type.__name__=_G
_NpSecurityDot11EncryptedDot1xEapMd5Secret_Object=MibScalar
npSecurityDot11EncryptedDot1xEapMd5Secret=_NpSecurityDot11EncryptedDot1xEapMd5Secret_Object((1,3,6,1,4,1,11,2,4,3,20,6),_NpSecurityDot11EncryptedDot1xEapMd5Secret_Type())
npSecurityDot11EncryptedDot1xEapMd5Secret.setMaxAccess(_J)
if mibBuilder.loadTexts:npSecurityDot11EncryptedDot1xEapMd5Secret.setStatus(_B)
class _NpSecurityDot11SignalStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('level-1-TBD',1),('level-2-TBD',2),('level-3-TBD',3),('level-4-TBD',4),('level-5-TBD',5)))
_NpSecurityDot11SignalStrength_Type.__name__=_D
_NpSecurityDot11SignalStrength_Object=MibScalar
npSecurityDot11SignalStrength=_NpSecurityDot11SignalStrength_Object((1,3,6,1,4,1,11,2,4,3,20,8),_NpSecurityDot11SignalStrength_Type())
npSecurityDot11SignalStrength.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityDot11SignalStrength.setStatus(_B)
_NpSecurityDot11SSIDTable_ObjectIdentity=ObjectIdentity
npSecurityDot11SSIDTable=_NpSecurityDot11SSIDTable_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20,9))
_NpSecurityDot11SSIDEntry_ObjectIdentity=ObjectIdentity
npSecurityDot11SSIDEntry=_NpSecurityDot11SSIDEntry_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20,9,1))
class _NpSecurityDot11SSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NpSecurityDot11SSID_Type.__name__=_G
_NpSecurityDot11SSID_Object=MibScalar
npSecurityDot11SSID=_NpSecurityDot11SSID_Object((1,3,6,1,4,1,11,2,4,3,20,9,1,2),_NpSecurityDot11SSID_Type())
npSecurityDot11SSID.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityDot11SSID.setStatus(_B)
_NpSecurityDot11SSIDTableNumEntries_Type=Integer32
_NpSecurityDot11SSIDTableNumEntries_Object=MibScalar
npSecurityDot11SSIDTableNumEntries=_NpSecurityDot11SSIDTableNumEntries_Object((1,3,6,1,4,1,11,2,4,3,20,10),_NpSecurityDot11SSIDTableNumEntries_Type())
npSecurityDot11SSIDTableNumEntries.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityDot11SSIDTableNumEntries.setStatus(_B)
class _NpSecurityDot11SSLCertLoaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_NpSecurityDot11SSLCertLoaded_Type.__name__=_D
_NpSecurityDot11SSLCertLoaded_Object=MibScalar
npSecurityDot11SSLCertLoaded=_NpSecurityDot11SSLCertLoaded_Object((1,3,6,1,4,1,11,2,4,3,20,11),_NpSecurityDot11SSLCertLoaded_Type())
npSecurityDot11SSLCertLoaded.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityDot11SSLCertLoaded.setStatus(_B)
class _NpSecurityDot11TLSCertLoaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_NpSecurityDot11TLSCertLoaded_Type.__name__=_D
_NpSecurityDot11TLSCertLoaded_Object=MibScalar
npSecurityDot11TLSCertLoaded=_NpSecurityDot11TLSCertLoaded_Object((1,3,6,1,4,1,11,2,4,3,20,12),_NpSecurityDot11TLSCertLoaded_Type())
npSecurityDot11TLSCertLoaded.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityDot11TLSCertLoaded.setStatus(_B)
class _NpSecuritySnmpV3EncryptedUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_NpSecuritySnmpV3EncryptedUserName_Type.__name__=_G
_NpSecuritySnmpV3EncryptedUserName_Object=MibScalar
npSecuritySnmpV3EncryptedUserName=_NpSecuritySnmpV3EncryptedUserName_Object((1,3,6,1,4,1,11,2,4,3,20,13),_NpSecuritySnmpV3EncryptedUserName_Type())
npSecuritySnmpV3EncryptedUserName.setMaxAccess(_J)
if mibBuilder.loadTexts:npSecuritySnmpV3EncryptedUserName.setStatus(_B)
class _NpSecuritySnmpV3AuthKeyPassPhrase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_NpSecuritySnmpV3AuthKeyPassPhrase_Type.__name__=_G
_NpSecuritySnmpV3AuthKeyPassPhrase_Object=MibScalar
npSecuritySnmpV3AuthKeyPassPhrase=_NpSecuritySnmpV3AuthKeyPassPhrase_Object((1,3,6,1,4,1,11,2,4,3,20,14),_NpSecuritySnmpV3AuthKeyPassPhrase_Type())
npSecuritySnmpV3AuthKeyPassPhrase.setMaxAccess(_J)
if mibBuilder.loadTexts:npSecuritySnmpV3AuthKeyPassPhrase.setStatus(_B)
class _NpSecuritySnmpV3PrivKeyPassPharse_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_NpSecuritySnmpV3PrivKeyPassPharse_Type.__name__=_G
_NpSecuritySnmpV3PrivKeyPassPharse_Object=MibScalar
npSecuritySnmpV3PrivKeyPassPharse=_NpSecuritySnmpV3PrivKeyPassPharse_Object((1,3,6,1,4,1,11,2,4,3,20,15),_NpSecuritySnmpV3PrivKeyPassPharse_Type())
npSecuritySnmpV3PrivKeyPassPharse.setMaxAccess(_J)
if mibBuilder.loadTexts:npSecuritySnmpV3PrivKeyPassPharse.setStatus(_B)
class _NpSecurityDot11ExactMatchServerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_NpSecurityDot11ExactMatchServerId_Type.__name__=_D
_NpSecurityDot11ExactMatchServerId_Object=MibScalar
npSecurityDot11ExactMatchServerId=_NpSecurityDot11ExactMatchServerId_Object((1,3,6,1,4,1,11,2,4,3,20,19),_NpSecurityDot11ExactMatchServerId_Type())
npSecurityDot11ExactMatchServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11ExactMatchServerId.setStatus(_B)
class _NpSecurityDot11EncryptionStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
_NpSecurityDot11EncryptionStrength_Type.__name__=_D
_NpSecurityDot11EncryptionStrength_Object=MibScalar
npSecurityDot11EncryptionStrength=_NpSecurityDot11EncryptionStrength_Object((1,3,6,1,4,1,11,2,4,3,20,20),_NpSecurityDot11EncryptionStrength_Type())
npSecurityDot11EncryptionStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11EncryptionStrength.setStatus(_B)
class _NpSecurityCertBuff_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_NpSecurityCertBuff_Type.__name__=_G
_NpSecurityCertBuff_Object=MibScalar
npSecurityCertBuff=_NpSecurityCertBuff_Object((1,3,6,1,4,1,11,2,4,3,20,21),_NpSecurityCertBuff_Type())
npSecurityCertBuff.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityCertBuff.setStatus(_B)
class _NpSecurityCertBuffIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('block1',1),('block2',2),('block3',3),('block4',4),('block5',5),('block6',6)))
_NpSecurityCertBuffIndex_Type.__name__=_D
_NpSecurityCertBuffIndex_Object=MibScalar
npSecurityCertBuffIndex=_NpSecurityCertBuffIndex_Object((1,3,6,1,4,1,11,2,4,3,20,22),_NpSecurityCertBuffIndex_Type())
npSecurityCertBuffIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityCertBuffIndex.setStatus(_B)
class _NpSecuritySslRedirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redirectionEnabled',1),('redirectionDisabled',2)))
_NpSecuritySslRedirection_Type.__name__=_D
_NpSecuritySslRedirection_Object=MibScalar
npSecuritySslRedirection=_NpSecuritySslRedirection_Object((1,3,6,1,4,1,11,2,4,3,20,23),_NpSecuritySslRedirection_Type())
npSecuritySslRedirection.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySslRedirection.setStatus(_B)
class _NpSecurityReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('Set',0),('Reset',1)))
_NpSecurityReset_Type.__name__=_D
_NpSecurityReset_Object=MibScalar
npSecurityReset=_NpSecurityReset_Object((1,3,6,1,4,1,11,2,4,3,20,24),_NpSecurityReset_Type())
npSecurityReset.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityReset.setStatus(_B)
class _NpSecurityDot11WEPStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('not-set',1),('strenth-40-bit',2),('strenth-104-bit',3)))
_NpSecurityDot11WEPStrength_Type.__name__=_D
_NpSecurityDot11WEPStrength_Object=MibScalar
npSecurityDot11WEPStrength=_NpSecurityDot11WEPStrength_Object((1,3,6,1,4,1,11,2,4,3,20,26),_NpSecurityDot11WEPStrength_Type())
npSecurityDot11WEPStrength.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityDot11WEPStrength.setStatus(_B)
_NpSecurityServicesSupported_Type=Integer32
_NpSecurityServicesSupported_Object=MibScalar
npSecurityServicesSupported=_NpSecurityServicesSupported_Object((1,3,6,1,4,1,11,2,4,3,20,27),_NpSecurityServicesSupported_Type())
npSecurityServicesSupported.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityServicesSupported.setStatus(_B)
_NpSecurityDot11Encryption_Type=Integer32
_NpSecurityDot11Encryption_Object=MibScalar
npSecurityDot11Encryption=_NpSecurityDot11Encryption_Object((1,3,6,1,4,1,11,2,4,3,20,28),_NpSecurityDot11Encryption_Type())
npSecurityDot11Encryption.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11Encryption.setStatus(_B)
_NpSecurityDot11MulticastCipher_Type=Integer32
_NpSecurityDot11MulticastCipher_Object=MibScalar
npSecurityDot11MulticastCipher=_NpSecurityDot11MulticastCipher_Object((1,3,6,1,4,1,11,2,4,3,20,29),_NpSecurityDot11MulticastCipher_Type())
npSecurityDot11MulticastCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11MulticastCipher.setStatus(_B)
_NpSecurityDot11BeaconTable_ObjectIdentity=ObjectIdentity
npSecurityDot11BeaconTable=_NpSecurityDot11BeaconTable_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20,33))
_NpSecurityDot11BeaconEntry_ObjectIdentity=ObjectIdentity
npSecurityDot11BeaconEntry=_NpSecurityDot11BeaconEntry_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20,33,1))
class _NpSecurityDot11BeaconInfoXMLString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_NpSecurityDot11BeaconInfoXMLString_Type.__name__=_G
_NpSecurityDot11BeaconInfoXMLString_Object=MibScalar
npSecurityDot11BeaconInfoXMLString=_NpSecurityDot11BeaconInfoXMLString_Object((1,3,6,1,4,1,11,2,4,3,20,33,1,2),_NpSecurityDot11BeaconInfoXMLString_Type())
npSecurityDot11BeaconInfoXMLString.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityDot11BeaconInfoXMLString.setStatus(_B)
_NpSecurityDot11BeaconTableNumEntries_Type=Integer32
_NpSecurityDot11BeaconTableNumEntries_Object=MibScalar
npSecurityDot11BeaconTableNumEntries=_NpSecurityDot11BeaconTableNumEntries_Object((1,3,6,1,4,1,11,2,4,3,20,34),_NpSecurityDot11BeaconTableNumEntries_Type())
npSecurityDot11BeaconTableNumEntries.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityDot11BeaconTableNumEntries.setStatus(_B)
_NpSecurityDot11OpenSSIDEnabled_Type=TruthValue
_NpSecurityDot11OpenSSIDEnabled_Object=MibScalar
npSecurityDot11OpenSSIDEnabled=_NpSecurityDot11OpenSSIDEnabled_Object((1,3,6,1,4,1,11,2,4,3,20,35),_NpSecurityDot11OpenSSIDEnabled_Type())
npSecurityDot11OpenSSIDEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:npSecurityDot11OpenSSIDEnabled.setStatus(_B)
class _NpSecurityDot11DynamicEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('NONE',0),('BASIC',1),('WPA',2),('WPA2',3),('AUTO',4)))
_NpSecurityDot11DynamicEncryption_Type.__name__=_D
_NpSecurityDot11DynamicEncryption_Object=MibScalar
npSecurityDot11DynamicEncryption=_NpSecurityDot11DynamicEncryption_Object((1,3,6,1,4,1,11,2,4,3,20,42),_NpSecurityDot11DynamicEncryption_Type())
npSecurityDot11DynamicEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11DynamicEncryption.setStatus(_B)
class _NpSecurityDot11LinkAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,128,143)));namedValues=NamedValues(*(('open',1),('shared-key',2),('leap',128),('auto',143)))
_NpSecurityDot11LinkAuthentication_Type.__name__=_D
_NpSecurityDot11LinkAuthentication_Object=MibScalar
npSecurityDot11LinkAuthentication=_NpSecurityDot11LinkAuthentication_Object((1,3,6,1,4,1,11,2,4,3,20,43),_NpSecurityDot11LinkAuthentication_Type())
npSecurityDot11LinkAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11LinkAuthentication.setStatus(_B)
class _NpSecuritySnmpV3AuthAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('md5',2),('sha-1',3)))
_NpSecuritySnmpV3AuthAlgorithm_Type.__name__=_D
_NpSecuritySnmpV3AuthAlgorithm_Object=MibScalar
npSecuritySnmpV3AuthAlgorithm=_NpSecuritySnmpV3AuthAlgorithm_Object((1,3,6,1,4,1,11,2,4,3,20,44),_NpSecuritySnmpV3AuthAlgorithm_Type())
npSecuritySnmpV3AuthAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySnmpV3AuthAlgorithm.setStatus(_B)
class _NpSecuritySnmpV3PrivAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('des',2),('aes-128',3)))
_NpSecuritySnmpV3PrivAlgorithm_Type.__name__=_D
_NpSecuritySnmpV3PrivAlgorithm_Object=MibScalar
npSecuritySnmpV3PrivAlgorithm=_NpSecuritySnmpV3PrivAlgorithm_Object((1,3,6,1,4,1,11,2,4,3,20,45),_NpSecuritySnmpV3PrivAlgorithm_Type())
npSecuritySnmpV3PrivAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySnmpV3PrivAlgorithm.setStatus(_B)
class _NpSecuritySnmpV3PassPhrase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('key',0),('passphrase',1)))
_NpSecuritySnmpV3PassPhrase_Type.__name__=_D
_NpSecuritySnmpV3PassPhrase_Object=MibScalar
npSecuritySnmpV3PassPhrase=_NpSecuritySnmpV3PassPhrase_Object((1,3,6,1,4,1,11,2,4,3,20,46),_NpSecuritySnmpV3PassPhrase_Type())
npSecuritySnmpV3PassPhrase.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySnmpV3PassPhrase.setStatus(_B)
class _NpSecurityWirelessDirectEncryptionMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noSecurity',1),('wpa',2)))
_NpSecurityWirelessDirectEncryptionMethod_Type.__name__=_D
_NpSecurityWirelessDirectEncryptionMethod_Object=MibScalar
npSecurityWirelessDirectEncryptionMethod=_NpSecurityWirelessDirectEncryptionMethod_Object((1,3,6,1,4,1,11,2,4,3,20,51),_NpSecurityWirelessDirectEncryptionMethod_Type())
npSecurityWirelessDirectEncryptionMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityWirelessDirectEncryptionMethod.setStatus(_B)
class _NpSecurityWirelessDirectEncryptedPassPhrase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NpSecurityWirelessDirectEncryptedPassPhrase_Type.__name__=_G
_NpSecurityWirelessDirectEncryptedPassPhrase_Object=MibScalar
npSecurityWirelessDirectEncryptedPassPhrase=_NpSecurityWirelessDirectEncryptedPassPhrase_Object((1,3,6,1,4,1,11,2,4,3,20,55),_NpSecurityWirelessDirectEncryptedPassPhrase_Type())
npSecurityWirelessDirectEncryptedPassPhrase.setMaxAccess(_J)
if mibBuilder.loadTexts:npSecurityWirelessDirectEncryptedPassPhrase.setStatus(_B)
class _NpSecurityDot1xFailSafe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_NpSecurityDot1xFailSafe_Type.__name__=_D
_NpSecurityDot1xFailSafe_Object=MibScalar
npSecurityDot1xFailSafe=_NpSecurityDot1xFailSafe_Object((1,3,6,1,4,1,11,2,4,3,20,57),_NpSecurityDot1xFailSafe_Type())
npSecurityDot1xFailSafe.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot1xFailSafe.setStatus(_B)
_NpSecuritySSLProtocol_Type=Integer32
_NpSecuritySSLProtocol_Object=MibScalar
npSecuritySSLProtocol=_NpSecuritySSLProtocol_Object((1,3,6,1,4,1,11,2,4,3,20,58),_NpSecuritySSLProtocol_Type())
npSecuritySSLProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySSLProtocol.setStatus(_B)
_SnmpAccess_ObjectIdentity=ObjectIdentity
snmpAccess=_SnmpAccess_ObjectIdentity((1,3,6,1,4,1,11,2,15))
_Community_ObjectIdentity=ObjectIdentity
community=_Community_ObjectIdentity((1,3,6,1,4,1,11,2,15,1))
class _SetCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SetCommunityName_Type.__name__=_G
_SetCommunityName_Object=MibScalar
setCommunityName=_SetCommunityName_Object((1,3,6,1,4,1,11,2,15,1,1),_SetCommunityName_Type())
setCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:setCommunityName.setStatus(_B)
class _GetCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GetCommunityName_Type.__name__=_G
_GetCommunityName_Object=MibScalar
getCommunityName=_GetCommunityName_Object((1,3,6,1,4,1,11,2,15,1,2),_GetCommunityName_Type())
getCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:getCommunityName.setStatus(_B)
_PpmMIB_ObjectIdentity=ObjectIdentity
ppmMIB=_PpmMIB_ObjectIdentity((1,3,6,1,4,1,2699,1,2))
_PpmMIBObjects_ObjectIdentity=ObjectIdentity
ppmMIBObjects=_PpmMIBObjects_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1))
_PpmGeneral_ObjectIdentity=ObjectIdentity
ppmGeneral=_PpmGeneral_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,1))
class _PpmGeneralNaturalLanguage_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PpmGeneralNaturalLanguage_Type.__name__=_K
_PpmGeneralNaturalLanguage_Object=MibScalar
ppmGeneralNaturalLanguage=_PpmGeneralNaturalLanguage_Object((1,3,6,1,4,1,2699,1,2,1,1,1),_PpmGeneralNaturalLanguage_Type())
ppmGeneralNaturalLanguage.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmGeneralNaturalLanguage.setStatus(_B)
class _PpmGeneralNumberOfPrinters_Type(Gauge32):defaultValue=0
_PpmGeneralNumberOfPrinters_Type.__name__=_P
_PpmGeneralNumberOfPrinters_Object=MibScalar
ppmGeneralNumberOfPrinters=_PpmGeneralNumberOfPrinters_Object((1,3,6,1,4,1,2699,1,2,1,1,2),_PpmGeneralNumberOfPrinters_Type())
ppmGeneralNumberOfPrinters.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmGeneralNumberOfPrinters.setStatus(_B)
class _PpmGeneralNumberOfPorts_Type(Gauge32):defaultValue=0
_PpmGeneralNumberOfPorts_Type.__name__=_P
_PpmGeneralNumberOfPorts_Object=MibScalar
ppmGeneralNumberOfPorts=_PpmGeneralNumberOfPorts_Object((1,3,6,1,4,1,2699,1,2,1,1,3),_PpmGeneralNumberOfPorts_Type())
ppmGeneralNumberOfPorts.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmGeneralNumberOfPorts.setStatus(_B)
_PpmPrinter_ObjectIdentity=ObjectIdentity
ppmPrinter=_PpmPrinter_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,2))
_PpmPrinterTable_ObjectIdentity=ObjectIdentity
ppmPrinterTable=_PpmPrinterTable_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,2,1))
_PpmPrinterEntry_ObjectIdentity=ObjectIdentity
ppmPrinterEntry=_PpmPrinterEntry_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,2,1,1))
class _PpmPrinterName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PpmPrinterName_Type.__name__=_K
_PpmPrinterName_Object=MibScalar
ppmPrinterName=_PpmPrinterName_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,2),_PpmPrinterName_Type())
ppmPrinterName.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPrinterName.setStatus(_B)
class _PpmPrinterIEEE1284DeviceId_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_PpmPrinterIEEE1284DeviceId_Type.__name__=_G
_PpmPrinterIEEE1284DeviceId_Object=MibScalar
ppmPrinterIEEE1284DeviceId=_PpmPrinterIEEE1284DeviceId_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,3),_PpmPrinterIEEE1284DeviceId_Type())
ppmPrinterIEEE1284DeviceId.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPrinterIEEE1284DeviceId.setStatus(_B)
class _PpmPrinterNumberOfPorts_Type(Gauge32):defaultValue=0
_PpmPrinterNumberOfPorts_Type.__name__=_P
_PpmPrinterNumberOfPorts_Object=MibScalar
ppmPrinterNumberOfPorts=_PpmPrinterNumberOfPorts_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,4),_PpmPrinterNumberOfPorts_Type())
ppmPrinterNumberOfPorts.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPrinterNumberOfPorts.setStatus(_B)
class _PpmPrinterPreferredPortIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PpmPrinterPreferredPortIndex_Type.__name__=_D
_PpmPrinterPreferredPortIndex_Object=MibScalar
ppmPrinterPreferredPortIndex=_PpmPrinterPreferredPortIndex_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,5),_PpmPrinterPreferredPortIndex_Type())
ppmPrinterPreferredPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPrinterPreferredPortIndex.setStatus(_B)
class _PpmPrinterHrDeviceIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PpmPrinterHrDeviceIndex_Type.__name__=_D
_PpmPrinterHrDeviceIndex_Object=MibScalar
ppmPrinterHrDeviceIndex=_PpmPrinterHrDeviceIndex_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,6),_PpmPrinterHrDeviceIndex_Type())
ppmPrinterHrDeviceIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPrinterHrDeviceIndex.setStatus(_B)
class _PpmPrinterSnmpCommunityName_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PpmPrinterSnmpCommunityName_Type.__name__=_G
_PpmPrinterSnmpCommunityName_Object=MibScalar
ppmPrinterSnmpCommunityName=_PpmPrinterSnmpCommunityName_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,7),_PpmPrinterSnmpCommunityName_Type())
ppmPrinterSnmpCommunityName.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPrinterSnmpCommunityName.setStatus(_B)
class _PpmPrinterSnmpQueryEnabled_Type(TruthValue):defaultValue=2
_PpmPrinterSnmpQueryEnabled_Type.__name__=_L
_PpmPrinterSnmpQueryEnabled_Object=MibScalar
ppmPrinterSnmpQueryEnabled=_PpmPrinterSnmpQueryEnabled_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,8),_PpmPrinterSnmpQueryEnabled_Type())
ppmPrinterSnmpQueryEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPrinterSnmpQueryEnabled.setStatus(_B)
_PpmPort_ObjectIdentity=ObjectIdentity
ppmPort=_PpmPort_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,3))
_PpmPortTable_ObjectIdentity=ObjectIdentity
ppmPortTable=_PpmPortTable_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,3,1))
_PpmPortEntry_ObjectIdentity=ObjectIdentity
ppmPortEntry=_PpmPortEntry_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,3,1,1))
class _PpmPortEnabled_Type(TruthValue):defaultValue=2
_PpmPortEnabled_Type.__name__=_L
_PpmPortEnabled_Object=MibScalar
ppmPortEnabled=_PpmPortEnabled_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,2),_PpmPortEnabled_Type())
ppmPortEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPortEnabled.setStatus(_B)
class _PpmPortName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PpmPortName_Type.__name__=_K
_PpmPortName_Object=MibScalar
ppmPortName=_PpmPortName_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,3),_PpmPortName_Type())
ppmPortName.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPortName.setStatus(_B)
class _PpmPortServiceNameOrURI_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PpmPortServiceNameOrURI_Type.__name__=_K
_PpmPortServiceNameOrURI_Object=MibScalar
ppmPortServiceNameOrURI=_PpmPortServiceNameOrURI_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,4),_PpmPortServiceNameOrURI_Type())
ppmPortServiceNameOrURI.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPortServiceNameOrURI.setStatus(_B)
class _PpmPortProtocolType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PpmPortProtocolType_Type.__name__=_D
_PpmPortProtocolType_Object=MibScalar
ppmPortProtocolType=_PpmPortProtocolType_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,5),_PpmPortProtocolType_Type())
ppmPortProtocolType.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPortProtocolType.setStatus(_B)
class _PpmPortProtocolTargetPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PpmPortProtocolTargetPort_Type.__name__=_D
_PpmPortProtocolTargetPort_Object=MibScalar
ppmPortProtocolTargetPort=_PpmPortProtocolTargetPort_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,6),_PpmPortProtocolTargetPort_Type())
ppmPortProtocolTargetPort.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPortProtocolTargetPort.setStatus(_B)
class _PpmPortProtocolAltSourceEnabled_Type(TruthValue):defaultValue=2
_PpmPortProtocolAltSourceEnabled_Type.__name__=_L
_PpmPortProtocolAltSourceEnabled_Object=MibScalar
ppmPortProtocolAltSourceEnabled=_PpmPortProtocolAltSourceEnabled_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,7),_PpmPortProtocolAltSourceEnabled_Type())
ppmPortProtocolAltSourceEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPortProtocolAltSourceEnabled.setStatus(_B)
class _PpmPortPrtChannelIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PpmPortPrtChannelIndex_Type.__name__=_D
_PpmPortPrtChannelIndex_Object=MibScalar
ppmPortPrtChannelIndex=_PpmPortPrtChannelIndex_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,8),_PpmPortPrtChannelIndex_Type())
ppmPortPrtChannelIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPortPrtChannelIndex.setStatus(_B)
class _PpmPortLprByteCountEnabled_Type(TruthValue):defaultValue=2
_PpmPortLprByteCountEnabled_Type.__name__=_L
_PpmPortLprByteCountEnabled_Object=MibScalar
ppmPortLprByteCountEnabled=_PpmPortLprByteCountEnabled_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,9),_PpmPortLprByteCountEnabled_Type())
ppmPortLprByteCountEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:ppmPortLprByteCountEnabled.setStatus(_B)
mibBuilder.exportSymbols('HP-OFFICEJET-PRO-X576DW-MIB',**{'ieee802dot11':ieee802dot11,'dot11smt':dot11smt,'dot11StationConfigTable':dot11StationConfigTable,'dot11StationConfigEntry':dot11StationConfigEntry,'dot11DesiredSSID':dot11DesiredSSID,'dot11DesiredBSSType':dot11DesiredBSSType,'dot11AuthenticationAlgorithmsTable':dot11AuthenticationAlgorithmsTable,'dot11AuthenticationAlgorithmsEntry':dot11AuthenticationAlgorithmsEntry,'dot11AuthenticationAlgorithm':dot11AuthenticationAlgorithm,'dot11AuthenticationAlgorithmsEnable':dot11AuthenticationAlgorithmsEnable,'dot11WEPDefaultKeysTable':dot11WEPDefaultKeysTable,'dot11WEPDefaultKeysEntry':dot11WEPDefaultKeysEntry,'dot11WEPDefaultKeyValue':dot11WEPDefaultKeyValue,'dot11PrivacyTable':dot11PrivacyTable,'dot11PrivacyEntry':dot11PrivacyEntry,'dot11PrivacyInvoked':dot11PrivacyInvoked,'dot11WEPDefaultKeyID':dot11WEPDefaultKeyID,'dot11phy':dot11phy,'dot11PhyOperationTable':dot11PhyOperationTable,'dot11PhyOperationEntry':dot11PhyOperationEntry,'dot11CurrentRegDomain':dot11CurrentRegDomain,'ieee802dot11i':ieee802dot11i,'dot11RSNConfigAuthenticationSuitesTable':dot11RSNConfigAuthenticationSuitesTable,'dot11RSNConfigAuthenticationSuitesEntry':dot11RSNConfigAuthenticationSuitesEntry,'dot11RSNConfigAuthenticationSuite':dot11RSNConfigAuthenticationSuite,'dot11RSNConfigAuthenticationSuiteEnabled':dot11RSNConfigAuthenticationSuiteEnabled,'org':org,'dod':dod,'internet':internet,'mgmt':mgmt,'mib-2':mib_2,'interfaces':interfaces,'ifNumber':ifNumber,'ifTable':ifTable,'ifEntry':ifEntry,'ifIndex':ifIndex,'ifDescr':ifDescr,'ifType':ifType,'ifMtu':ifMtu,'ifSpeed':ifSpeed,'ifPhysAddress':ifPhysAddress,'ifAdminStatus':ifAdminStatus,'ifOperStatus':ifOperStatus,'ifLastChange':ifLastChange,'ifInOctets':ifInOctets,'ifInUcastPkts':ifInUcastPkts,'ifInNUcastPkts':ifInNUcastPkts,'ifInDiscards':ifInDiscards,'ifInErrors':ifInErrors,'ifInUnknownProtos':ifInUnknownProtos,'ifOutOctets':ifOutOctets,'ifOutUcastPkts':ifOutUcastPkts,'ifOutNUcastPkts':ifOutNUcastPkts,'ifOutDiscards':ifOutDiscards,'ifOutErrors':ifOutErrors,'ifOutQLen':ifOutQLen,'ifSpecific':ifSpecific,'at':at,'atTable':atTable,'atEntry':atEntry,'atIfIndex':atIfIndex,'atPhysAddress':atPhysAddress,'atNetAddress':atNetAddress,'ip':ip,'ipForwarding':ipForwarding,'ipDefaultTTL':ipDefaultTTL,'ipInReceives':ipInReceives,'ipInHdrErrors':ipInHdrErrors,'ipInAddrErrors':ipInAddrErrors,'ipForwDatagrams':ipForwDatagrams,'ipInUnknownProtos':ipInUnknownProtos,'ipInDiscards':ipInDiscards,'ipInDelivers':ipInDelivers,'ipOutRequests':ipOutRequests,'ipOutDiscards':ipOutDiscards,'ipOutNoRoutes':ipOutNoRoutes,'ipReasmTimeout':ipReasmTimeout,'ipReasmReqds':ipReasmReqds,'ipReasmOKs':ipReasmOKs,'ipReasmFails':ipReasmFails,'ipFragOKs':ipFragOKs,'ipFragFails':ipFragFails,'ipFragCreates':ipFragCreates,'ipAddrTable':ipAddrTable,'ipAddrEntry':ipAddrEntry,'ipAdEntAddr':ipAdEntAddr,'ipAdEntIfIndex':ipAdEntIfIndex,'ipAdEntNetMask':ipAdEntNetMask,'ipAdEntBcastAddr':ipAdEntBcastAddr,'ipAdEntReasmMaxSize':ipAdEntReasmMaxSize,'ipRouteTable':ipRouteTable,'ipRouteEntry':ipRouteEntry,'ipRouteDest':ipRouteDest,'ipRouteIfIndex':ipRouteIfIndex,'ipRouteMetric1':ipRouteMetric1,'ipRouteMetric2':ipRouteMetric2,'ipRouteMetric3':ipRouteMetric3,'ipRouteMetric4':ipRouteMetric4,'ipRouteNextHop':ipRouteNextHop,'ipRouteType':ipRouteType,'ipRouteProto':ipRouteProto,'ipRouteAge':ipRouteAge,'ipRouteMask':ipRouteMask,'ipRouteMetric5':ipRouteMetric5,'ipRouteInfo':ipRouteInfo,'ipNetToMediaTable':ipNetToMediaTable,'ipNetToMediaEntry':ipNetToMediaEntry,'ipNetToMediaIfIndex':ipNetToMediaIfIndex,'ipNetToMediaPhysAddress':ipNetToMediaPhysAddress,'ipNetToMediaNetAddress':ipNetToMediaNetAddress,'ipNetToMediaType':ipNetToMediaType,'ipRoutingDiscards':ipRoutingDiscards,'icmp':icmp,'icmpInMsgs':icmpInMsgs,'icmpInErrors':icmpInErrors,'icmpInDestUnreachs':icmpInDestUnreachs,'icmpInTimeExcds':icmpInTimeExcds,'icmpInParmProbs':icmpInParmProbs,'icmpInSrcQuenchs':icmpInSrcQuenchs,'icmpInRedirects':icmpInRedirects,'icmpInEchos':icmpInEchos,'icmpInEchoReps':icmpInEchoReps,'icmpInTimestamps':icmpInTimestamps,'icmpInTimestampReps':icmpInTimestampReps,'icmpInAddrMasks':icmpInAddrMasks,'icmpInAddrMaskReps':icmpInAddrMaskReps,'icmpOutMsgs':icmpOutMsgs,'icmpOutErrors':icmpOutErrors,'icmpOutDestUnreachs':icmpOutDestUnreachs,'icmpOutTimeExcds':icmpOutTimeExcds,'icmpOutParmProbs':icmpOutParmProbs,'icmpOutSrcQuenchs':icmpOutSrcQuenchs,'icmpOutRedirects':icmpOutRedirects,'icmpOutEchos':icmpOutEchos,'icmpOutEchoReps':icmpOutEchoReps,'icmpOutTimestamps':icmpOutTimestamps,'icmpOutTimestampReps':icmpOutTimestampReps,'icmpOutAddrMasks':icmpOutAddrMasks,'icmpOutAddrMaskReps':icmpOutAddrMaskReps,'tcp':tcp,'tcpRtoAlgorithm':tcpRtoAlgorithm,'tcpRtoMin':tcpRtoMin,'tcpRtoMax':tcpRtoMax,'tcpMaxConn':tcpMaxConn,'tcpActiveOpens':tcpActiveOpens,'tcpPassiveOpens':tcpPassiveOpens,'tcpAttemptFails':tcpAttemptFails,'tcpEstabResets':tcpEstabResets,'tcpCurrEstab':tcpCurrEstab,'tcpInSegs':tcpInSegs,'tcpOutSegs':tcpOutSegs,'tcpRetransSegs':tcpRetransSegs,'tcpConnTable':tcpConnTable,'tcpConnEntry':tcpConnEntry,'tcpConnState':tcpConnState,'tcpConnLocalAddress':tcpConnLocalAddress,'tcpConnLocalPort':tcpConnLocalPort,'tcpConnRemAddress':tcpConnRemAddress,'tcpConnRemPort':tcpConnRemPort,'tcpInErrs':tcpInErrs,'tcpOutRsts':tcpOutRsts,'udp':udp,'udpInDatagrams':udpInDatagrams,'udpNoPorts':udpNoPorts,'udpInErrors':udpInErrors,'udpOutDatagrams':udpOutDatagrams,'udpTable':udpTable,'udpEntry':udpEntry,'udpLocalAddress':udpLocalAddress,'udpLocalPort':udpLocalPort,'snmp':snmp,'snmpInPkts':snmpInPkts,'snmpOutPkts':snmpOutPkts,'snmpInBadVersions':snmpInBadVersions,'snmpInBadCommunityNames':snmpInBadCommunityNames,'snmpInBadCommunityUses':snmpInBadCommunityUses,'snmpInASNParseErrs':snmpInASNParseErrs,'snmpInTooBigs':snmpInTooBigs,'snmpInNoSuchNames':snmpInNoSuchNames,'snmpInBadValues':snmpInBadValues,'snmpInReadOnlys':snmpInReadOnlys,'snmpInGenErrs':snmpInGenErrs,'snmpInTotalReqVars':snmpInTotalReqVars,'snmpInTotalSetVars':snmpInTotalSetVars,'snmpInGetRequests':snmpInGetRequests,'snmpInGetNexts':snmpInGetNexts,'snmpInSetRequests':snmpInSetRequests,'snmpInGetResponses':snmpInGetResponses,'snmpInTraps':snmpInTraps,'snmpOutTooBigs':snmpOutTooBigs,'snmpOutNoSuchNames':snmpOutNoSuchNames,'snmpOutBadValues':snmpOutBadValues,'snmpOutGenErrs':snmpOutGenErrs,'snmpOutGetRequests':snmpOutGetRequests,'snmpOutGetNexts':snmpOutGetNexts,'snmpOutSetRequests':snmpOutSetRequests,'snmpOutGetResponses':snmpOutGetResponses,'snmpOutTraps':snmpOutTraps,'snmpEnableAuthenTraps':snmpEnableAuthenTraps,'host':host,'hrSystem':hrSystem,'hrSystemUptime':hrSystemUptime,'hrStorage':hrStorage,'hrMemorySize':hrMemorySize,'hrStorageTable':hrStorageTable,'hrStorageEntry':hrStorageEntry,'hrStorageIndex':hrStorageIndex,'hrStorageType':hrStorageType,'hrStorageDescr':hrStorageDescr,'hrStorageAllocationUnits':hrStorageAllocationUnits,'hrStorageSize':hrStorageSize,'hrStorageUsed':hrStorageUsed,'hrStorageAllocationFailures':hrStorageAllocationFailures,'hrDevice':hrDevice,'hrDeviceTable':hrDeviceTable,'hrDeviceEntry':hrDeviceEntry,'hrDeviceIndex':hrDeviceIndex,'hrDeviceType':hrDeviceType,'hrDeviceDescr':hrDeviceDescr,'hrDeviceID':hrDeviceID,'hrDeviceStatus':hrDeviceStatus,'hrDeviceErrors':hrDeviceErrors,'hrPrinterTable':hrPrinterTable,'hrPrinterEntry':hrPrinterEntry,'hrPrinterStatus':hrPrinterStatus,'hrPrinterDetectedErrorState':hrPrinterDetectedErrorState,'printmib':printmib,'prtGeneral':prtGeneral,'prtGeneralTable':prtGeneralTable,'prtGeneralEntry':prtGeneralEntry,'prtGeneralConfigChanges':prtGeneralConfigChanges,'prtGeneralCurrentLocalization':prtGeneralCurrentLocalization,'prtGeneralReset':prtGeneralReset,'prtGeneralCurrentOperator':prtGeneralCurrentOperator,'prtGeneralServicePerson':prtGeneralServicePerson,'prtInputDefaultIndex':prtInputDefaultIndex,'prtOutputDefaultIndex':prtOutputDefaultIndex,'prtMarkerDefaultIndex':prtMarkerDefaultIndex,'prtMediaPathDefaultIndex':prtMediaPathDefaultIndex,'prtConsoleLocalization':prtConsoleLocalization,'prtConsoleNumberOfDisplayLines':prtConsoleNumberOfDisplayLines,'prtConsoleNumberOfDisplayChars':prtConsoleNumberOfDisplayChars,'prtConsoleDisable':prtConsoleDisable,'prtGeneralPrinterName':prtGeneralPrinterName,'prtGeneralSerialNumber':prtGeneralSerialNumber,'prtAlertCriticalEvents':prtAlertCriticalEvents,'prtAlertAllEvents':prtAlertAllEvents,'prtStorageRefTable':prtStorageRefTable,'prtStorageRefEntry':prtStorageRefEntry,'prtStorageRefIndex':prtStorageRefIndex,'prtDeviceRefTable':prtDeviceRefTable,'prtDeviceRefEntry':prtDeviceRefEntry,'prtDeviceRefIndex':prtDeviceRefIndex,'prtCover':prtCover,'prtCoverTable':prtCoverTable,'prtCoverEntry':prtCoverEntry,'prtCoverDescription':prtCoverDescription,'prtCoverStatus':prtCoverStatus,'prtLocalization':prtLocalization,'prtLocalizationTable':prtLocalizationTable,'prtLocalizationEntry':prtLocalizationEntry,'prtLocalizationLanguage':prtLocalizationLanguage,'prtLocalizationCountry':prtLocalizationCountry,'prtLocalizationCharacterSet':prtLocalizationCharacterSet,'prtInput':prtInput,'prtInputTable':prtInputTable,'prtInputEntry':prtInputEntry,'prtInputType':prtInputType,'prtInputDimUnit':prtInputDimUnit,'prtInputMediaDimFeedDirDeclared':prtInputMediaDimFeedDirDeclared,'prtInputMediaDimXFeedDirDeclared':prtInputMediaDimXFeedDirDeclared,'prtInputMediaDimFeedDirChosen':prtInputMediaDimFeedDirChosen,'prtInputMediaDimXFeedDirChosen':prtInputMediaDimXFeedDirChosen,'prtInputCapacityUnit':prtInputCapacityUnit,'prtInputMaxCapacity':prtInputMaxCapacity,'prtInputCurrentLevel':prtInputCurrentLevel,'prtInputStatus':prtInputStatus,'prtInputMediaName':prtInputMediaName,'prtInputName':prtInputName,'prtInputVendorName':prtInputVendorName,'prtInputModel':prtInputModel,'prtInputVersion':prtInputVersion,'prtInputSerialNumber':prtInputSerialNumber,'prtInputDescription':prtInputDescription,'prtInputSecurity':prtInputSecurity,'prtInputMediaWeight':prtInputMediaWeight,'prtInputMediaType':prtInputMediaType,'prtInputMediaColor':prtInputMediaColor,'prtInputMediaFormParts':prtInputMediaFormParts,'prtInputMediaLoadTimeout':prtInputMediaLoadTimeout,'prtOutput':prtOutput,'prtOutputTable':prtOutputTable,'prtOutputEntry':prtOutputEntry,'prtOutputType':prtOutputType,'prtOutputCapacityUnit':prtOutputCapacityUnit,'prtOutputMaxCapacity':prtOutputMaxCapacity,'prtOutputRemainingCapacity':prtOutputRemainingCapacity,'prtOutputStatus':prtOutputStatus,'prtOutputName':prtOutputName,'prtOutputVendorName':prtOutputVendorName,'prtOutputModel':prtOutputModel,'prtOutputVersion':prtOutputVersion,'prtOutputSerialNumber':prtOutputSerialNumber,'prtOutputDescription':prtOutputDescription,'prtOutputSecurity':prtOutputSecurity,'prtOutputDimUnit':prtOutputDimUnit,'prtOutputMaxDimFeedDir':prtOutputMaxDimFeedDir,'prtOutputMaxDimXFeedDir':prtOutputMaxDimXFeedDir,'prtOutputMinDimFeedDir':prtOutputMinDimFeedDir,'prtOutputMinDimXFeedDir':prtOutputMinDimXFeedDir,'prtOutputStackingOrder':prtOutputStackingOrder,'prtOutputPageDeliveryOrientation':prtOutputPageDeliveryOrientation,'prtOutputBursting':prtOutputBursting,'prtOutputDecollating':prtOutputDecollating,'prtOutputPageCollated':prtOutputPageCollated,'prtOutputOffsetStacking':prtOutputOffsetStacking,'prtMarker':prtMarker,'prtMarkerTable':prtMarkerTable,'prtMarkerEntry':prtMarkerEntry,'prtMarkerMarkTech':prtMarkerMarkTech,'prtMarkerCounterUnit':prtMarkerCounterUnit,'prtMarkerLifeCount':prtMarkerLifeCount,'prtMarkerPowerOnCount':prtMarkerPowerOnCount,'prtMarkerProcessColorants':prtMarkerProcessColorants,'prtMarkerSpotColorants':prtMarkerSpotColorants,'prtMarkerAddressabilityUnit':prtMarkerAddressabilityUnit,'prtMarkerAddressabilityFeedDir':prtMarkerAddressabilityFeedDir,'prtMarkerAddressabilityXFeedDir':prtMarkerAddressabilityXFeedDir,'prtMarkerNorthMargin':prtMarkerNorthMargin,'prtMarkerSouthMargin':prtMarkerSouthMargin,'prtMarkerWestMargin':prtMarkerWestMargin,'prtMarkerEastMargin':prtMarkerEastMargin,'prtMarkerStatus':prtMarkerStatus,'prtMarkerSupplies':prtMarkerSupplies,'prtMarkerSuppliesTable':prtMarkerSuppliesTable,'prtMarkerSuppliesEntry':prtMarkerSuppliesEntry,'prtMarkerSuppliesMarkerIndex':prtMarkerSuppliesMarkerIndex,'prtMarkerSuppliesColorantIndex':prtMarkerSuppliesColorantIndex,'prtMarkerSuppliesClass':prtMarkerSuppliesClass,'prtMarkerSuppliesType':prtMarkerSuppliesType,'prtMarkerSuppliesDescription':prtMarkerSuppliesDescription,'prtMarkerSuppliesSupplyUnit':prtMarkerSuppliesSupplyUnit,'prtMarkerSuppliesMaxCapacity':prtMarkerSuppliesMaxCapacity,'prtMarkerSuppliesLevel':prtMarkerSuppliesLevel,'prtMarkerColorant':prtMarkerColorant,'prtMarkerColorantTable':prtMarkerColorantTable,'prtMarkerColorantEntry':prtMarkerColorantEntry,'prtMarkerColorantMarkerIndex':prtMarkerColorantMarkerIndex,'prtMarkerColorantRole':prtMarkerColorantRole,'prtMarkerColorantValue':prtMarkerColorantValue,'prtMarkerColorantTonality':prtMarkerColorantTonality,'prtMediaPath':prtMediaPath,'prtMediaPathTable':prtMediaPathTable,'prtMediaPathEntry':prtMediaPathEntry,'prtMediaPathMaxSpeedPrintUnit':prtMediaPathMaxSpeedPrintUnit,'prtMediaPathMediaSizeUnit':prtMediaPathMediaSizeUnit,'prtMediaPathMaxSpeed':prtMediaPathMaxSpeed,'prtMediaPathMaxMediaFeedDir':prtMediaPathMaxMediaFeedDir,'prtMediaPathMaxMediaXFeedDir':prtMediaPathMaxMediaXFeedDir,'prtMediaPathMinMediaFeedDir':prtMediaPathMinMediaFeedDir,'prtMediaPathMinMediaXFeedDir':prtMediaPathMinMediaXFeedDir,'prtMediaPathType':prtMediaPathType,'prtMediaPathDescription':prtMediaPathDescription,'prtMediaPathStatus':prtMediaPathStatus,'prtChannel':prtChannel,'prtChannelTable':prtChannelTable,'prtChannelEntry':prtChannelEntry,'prtChannelType':prtChannelType,'prtChannelProtocolVersion':prtChannelProtocolVersion,'prtChannelCurrentJobCntlLangIndex':prtChannelCurrentJobCntlLangIndex,'prtChannelDefaultPageDescLangIndex':prtChannelDefaultPageDescLangIndex,'prtChannelState':prtChannelState,'prtChannelIfIndex':prtChannelIfIndex,'prtChannelStatus':prtChannelStatus,'prtChannelInformation':prtChannelInformation,'prtInterpreter':prtInterpreter,'prtInterpreterTable':prtInterpreterTable,'prtInterpreterEntry':prtInterpreterEntry,'prtInterpreterLangFamily':prtInterpreterLangFamily,'prtInterpreterLangLevel':prtInterpreterLangLevel,'prtInterpreterLangVersion':prtInterpreterLangVersion,'prtInterpreterDescription':prtInterpreterDescription,'prtInterpreterVersion':prtInterpreterVersion,'prtInterpreterDefaultOrientation':prtInterpreterDefaultOrientation,'prtInterpreterFeedAddressability':prtInterpreterFeedAddressability,'prtInterpreterXFeedAddressability':prtInterpreterXFeedAddressability,'prtInterpreterDefaultCharSetIn':prtInterpreterDefaultCharSetIn,'prtInterpreterDefaultCharSetOut':prtInterpreterDefaultCharSetOut,'prtInterpreterTwoWay':prtInterpreterTwoWay,'prtConsoleDisplayBuffer':prtConsoleDisplayBuffer,'prtConsoleDisplayBufferTable':prtConsoleDisplayBufferTable,'prtConsoleDisplayBufferEntry':prtConsoleDisplayBufferEntry,'prtConsoleDisplayBufferText':prtConsoleDisplayBufferText,'prtConsoleLights':prtConsoleLights,'prtConsoleLightTable':prtConsoleLightTable,'prtConsoleLightEntry':prtConsoleLightEntry,'prtConsoleOnTime':prtConsoleOnTime,'prtConsoleOffTime':prtConsoleOffTime,'prtConsoleColor':prtConsoleColor,'prtConsoleDescription':prtConsoleDescription,'prtAlert':prtAlert,'prtAlertTable':prtAlertTable,'prtAlertEntry':prtAlertEntry,'prtAlertSeverityLevel':prtAlertSeverityLevel,'prtAlertTrainingLevel':prtAlertTrainingLevel,'prtAlertGroup':prtAlertGroup,'prtAlertGroupIndex':prtAlertGroupIndex,'prtAlertLocation':prtAlertLocation,'prtAlertCode':prtAlertCode,'prtAlertDescription':prtAlertDescription,'prtAlertTime':prtAlertTime,'private':private,'enterprises':enterprises,'hpPrintServer':hpPrintServer,'nm':nm,'system':system,'netPeripheral':netPeripheral,'netPrinter':netPrinter,'generalDeviceStatus':generalDeviceStatus,'gdStatusEntry':gdStatusEntry,'gdStatusLineState':gdStatusLineState,'gdStatusPaperOut':gdStatusPaperOut,'gdStatusPaperJam':gdStatusPaperJam,'gdStatusBusy':gdStatusBusy,'gdStatusWait':gdStatusWait,'gdStatusInitialize':gdStatusInitialize,'gdStatusDoorOpen':gdStatusDoorOpen,'gdStatusPrinting':gdStatusPrinting,'gdStatusPaperOutput':gdStatusPaperOutput,'gdStatusDisplay':gdStatusDisplay,'gdStatusId':gdStatusId,'gdStatusJobTimeout':gdStatusJobTimeout,'gdPasswords':gdPasswords,'netPML':netPML,'netPMLmgmt':netPMLmgmt,'device':device,'device-system':device_system,'settings-system':settings_system,'energy-star':energy_star,'sleep-mode':sleep_mode,'speed-energy-usage':speed_energy_usage,'enable-engine-early-warmup':enable_engine_early_warmup,'status-system':status_system,'install-date':install_date,'date-and-time':date_and_time,'id':id,'model-number':model_number,'model-name':model_name,'serial-number':serial_number,'fw-rom-datecode':fw_rom_datecode,'fw-rom-revision':fw_rom_revision,'device-location':device_location,'asset-number':asset_number,'test':test,'print-internal-page':print_internal_page,'errorlog':errorlog,'error1':error1,'error1-time-stamp':error1_time_stamp,'error1-code':error1_code,'error1-date-time':error1_date_time,'error2':error2,'error2-time-stamp':error2_time_stamp,'error2-code':error2_code,'error2-date-time':error2_date_time,'error3':error3,'error3-time-stamp':error3_time_stamp,'error3-code':error3_code,'error3-date-time':error3_date_time,'error4':error4,'error4-time-stamp':error4_time_stamp,'error4-code':error4_code,'error4-date-time':error4_date_time,'error5':error5,'error5-time-stamp':error5_time_stamp,'error5-code':error5_code,'error5-date-time':error5_date_time,'error6':error6,'error6-time-stamp':error6_time_stamp,'error6-code':error6_code,'error6-date-time':error6_date_time,'error7':error7,'error7-time-stamp':error7_time_stamp,'error7-code':error7_code,'error7-date-time':error7_date_time,'error8':error8,'error8-time-stamp':error8_time_stamp,'error8-code':error8_code,'error8-date-time':error8_date_time,'error9':error9,'error9-time-stamp':error9_time_stamp,'error9-code':error9_code,'error9-date-time':error9_date_time,'error10':error10,'error10-time-stamp':error10_time_stamp,'error10-code':error10_code,'error10-date-time':error10_date_time,'error11':error11,'error11-time-stamp':error11_time_stamp,'error11-code':error11_code,'error11-date-time':error11_date_time,'error12':error12,'error12-time-stamp':error12_time_stamp,'error12-code':error12_code,'error12-date-time':error12_date_time,'error13':error13,'error13-time-stamp':error13_time_stamp,'error13-code':error13_code,'error13-date-time':error13_date_time,'error14':error14,'error14-time-stamp':error14_time_stamp,'error14-code':error14_code,'error14-date-time':error14_date_time,'error15':error15,'error15-time-stamp':error15_time_stamp,'error15-code':error15_code,'error15-date-time':error15_date_time,'accounting':accounting,'printer-accounting':printer_accounting,'printed-media-usage':printed_media_usage,'printed-media-simplex-count':printed_media_simplex_count,'printed-media-duplex-count':printed_media_duplex_count,'printer-color-accounting':printer_color_accounting,'printed-media-color-usage':printed_media_color_usage,'printed-media-color-simplex-count':printed_media_color_simplex_count,'printed-media-color-duplex-count':printed_media_color_duplex_count,'source-subsystem':source_subsystem,'scanner':scanner,'settings-scanner':settings_scanner,'scanner-accessory-adf-sheet-count':scanner_accessory_adf_sheet_count,'scanner-accessory-flatbed-scan-count':scanner_accessory_flatbed_scan_count,'scanner-accessory-copy-job-scan-count':scanner_accessory_copy_job_scan_count,'scanner-accessory-send-job-scan-count':scanner_accessory_send_job_scan_count,'scanner-accessory-total-copy-pages-printed':scanner_accessory_total_copy_pages_printed,'scan-to-folder-count':scan_to_folder_count,'fax-job-scan-count':fax_job_scan_count,'processing-subsystem':processing_subsystem,'pdl':pdl,'pdl-pcl':pdl_pcl,'pcl-total-page-count':pcl_total_page_count,'pdl-postscript':pdl_postscript,'postscript-total-page-count':postscript_total_page_count,'fax-proc-sub':fax_proc_sub,'settings-fax-proc-sub':settings_fax_proc_sub,'fax-print-page-count':fax_print_page_count,'status-fax-proc-sub':status_fax_proc_sub,'afax-send-page-count':afax_send_page_count,'afax-recv-page-count':afax_recv_page_count,'destination-subsystem':destination_subsystem,'print-engine':print_engine,'status-prt-eng':status_prt_eng,'total-engine-page-count':total_engine_page_count,'total-mono-page-count':total_mono_page_count,'total-color-page-count':total_color_page_count,'duplex-page-count':duplex_page_count,'consumables':consumables,'consumables-1':consumables_1,'consumable-status':consumable_status,'consumable-status-cartridge-model':consumable_status_cartridge_model,'consumable-status-manufacturing-date':consumable_status_manufacturing_date,'consumable-status-serial-number':consumable_status_serial_number,'consumable-status-first-install-date':consumable_status_first_install_date,'interface':interface,'npCard':npCard,'npSys':npSys,'npSysModelNumber':npSysModelNumber,'npSysCardServices1':npSysCardServices1,'npSysCardServices2':npSysCardServices2,'npSysCardServices3':npSysCardServices3,'npSysFactoryMacAddress':npSysFactoryMacAddress,'npCfg':npCfg,'npCfgSource':npCfgSource,'npCfgYiaddr':npCfgYiaddr,'npCfgSiaddr':npCfgSiaddr,'npCfgSubnetMask':npCfgSubnetMask,'npCfgDefaultGateway':npCfgDefaultGateway,'npCfgDomainName':npCfgDomainName,'npCfgIPP':npCfgIPP,'npCfgDNSNameServerId':npCfgDNSNameServerId,'npCfgWINSNameServerIdPri':npCfgWINSNameServerIdPri,'npCfgWINSNameServerIdSec':npCfgWINSNameServerIdSec,'npCfgPasswd1Verify':npCfgPasswd1Verify,'npCfgPasswd1':npCfgPasswd1,'npCfgLinkType':npCfgLinkType,'npCfgSnmpDefaultReadCmnty':npCfgSnmpDefaultReadCmnty,'npCfgBonjourDomainName':npCfgBonjourDomainName,'npCfgDNSNameServerIdSecondary':npCfgDNSNameServerIdSecondary,'npCfgIPv6DomainName':npCfgIPv6DomainName,'npCfgIPv6ConfigState':npCfgIPv6ConfigState,'npCfgIPAddrTable':npCfgIPAddrTable,'npCfgIPAddrEntry':npCfgIPAddrEntry,'npCfgIPAddrIndex':npCfgIPAddrIndex,'npCfgIPAddrType':npCfgIPAddrType,'npCfgIPAddress':npCfgIPAddress,'npCfgIPAddrIfIndex':npCfgIPAddrIfIndex,'npCfgIPAddrConfigBy':npCfgIPAddrConfigBy,'npCfgIPAddrStatus':npCfgIPAddrStatus,'npCfgIPAddrPrefixLength':npCfgIPAddrPrefixLength,'npCfgIPAddrValidLifetime':npCfgIPAddrValidLifetime,'npCfgIPAddrPrefLifetime':npCfgIPAddrPrefLifetime,'npCfgIPv6DNSAddr1':npCfgIPv6DNSAddr1,'npCfgIPv6DNSAddr2':npCfgIPv6DNSAddr2,'npCfgIPConfigPrecedence':npCfgIPConfigPrecedence,'npCfgSTAWirelessMode':npCfgSTAWirelessMode,'npCfgWirelessDirectSSIDPrefix':npCfgWirelessDirectSSIDPrefix,'npCfgWirelessDirectSSIDSuffix':npCfgWirelessDirectSSIDSuffix,'npCtl':npCtl,'npCtlProtocolSet':npCtlProtocolSet,'npCtlSLP':npCtlSLP,'npCtlLPD':npCtlLPD,'npCtl9100':npCtl9100,'npCtlSnmpVersionAccess':npCtlSnmpVersionAccess,'npCtlSnmpV3InitAccount':npCtlSnmpV3InitAccount,'npCtlBonjour':npCtlBonjour,'npCtlNetworkConnectionMode':npCtlNetworkConnectionMode,'npCtlWSDiscovery':npCtlWSDiscovery,'npCtlWSPrint':npCtlWSPrint,'npCtlWPAD':npCtlWPAD,'npCtlFpDot11WirelessState':npCtlFpDot11WirelessState,'npCtlDot11nSTAGuardInterval':npCtlDot11nSTAGuardInterval,'npCtlDot11nSTAAMSDUAggregation':npCtlDot11nSTAAMSDUAggregation,'npCtlDot11nSTABlockACKs':npCtlDot11nSTABlockACKs,'npCtlDot11nSTAAMPDUAggregation':npCtlDot11nSTAAMPDUAggregation,'npCtlWirelessDirectSSIDBroadcast':npCtlWirelessDirectSSIDBroadcast,'npCtlWirelessDirectHidePassphrase':npCtlWirelessDirectHidePassphrase,'npCtlDeviceMode':npCtlDeviceMode,'npCtlWirelessSTAState':npCtlWirelessSTAState,'npCtlWirelessDirectState':npCtlWirelessDirectState,'npNpi':npNpi,'npNpiPeripheralAttributeEntry':npNpiPeripheralAttributeEntry,'npNpiPaeClass':npNpiPaeClass,'npNpiPaeIdentification':npNpiPaeIdentification,'npNpiCardAttributeEntry':npNpiCardAttributeEntry,'npNpiCaeClass':npNpiCaeClass,'npIpx':npIpx,'npIpxSapInfo':npIpxSapInfo,'npIpxGetUnitCfgResp2':npIpxGetUnitCfgResp2,'npIpxRcfgAddress':npIpxRcfgAddress,'npPort':npPort,'npPortNumPorts':npPortNumPorts,'npWeb':npWeb,'npWebProxyServerId':npWebProxyServerId,'npWebProxyServerPort':npWebProxyServerPort,'npWebProxyUserName':npWebProxyUserName,'npWebProxyUserPasswd':npWebProxyUserPasswd,'npSecurity':npSecurity,'npSecurityDot11ServerAuthentication':npSecurityDot11ServerAuthentication,'npSecurityDot1xEapMd5Identity':npSecurityDot1xEapMd5Identity,'npSecurityDot1xTLSAuthServerId':npSecurityDot1xTLSAuthServerId,'npSecurityPublicKey':npSecurityPublicKey,'npSecurityDot11EncryptedDot11NetworkName':npSecurityDot11EncryptedDot11NetworkName,'npSecurityDot11EncryptedDot1xEapMd5Secret':npSecurityDot11EncryptedDot1xEapMd5Secret,'npSecurityDot11SignalStrength':npSecurityDot11SignalStrength,'npSecurityDot11SSIDTable':npSecurityDot11SSIDTable,'npSecurityDot11SSIDEntry':npSecurityDot11SSIDEntry,'npSecurityDot11SSID':npSecurityDot11SSID,'npSecurityDot11SSIDTableNumEntries':npSecurityDot11SSIDTableNumEntries,'npSecurityDot11SSLCertLoaded':npSecurityDot11SSLCertLoaded,'npSecurityDot11TLSCertLoaded':npSecurityDot11TLSCertLoaded,'npSecuritySnmpV3EncryptedUserName':npSecuritySnmpV3EncryptedUserName,'npSecuritySnmpV3AuthKeyPassPhrase':npSecuritySnmpV3AuthKeyPassPhrase,'npSecuritySnmpV3PrivKeyPassPharse':npSecuritySnmpV3PrivKeyPassPharse,'npSecurityDot11ExactMatchServerId':npSecurityDot11ExactMatchServerId,'npSecurityDot11EncryptionStrength':npSecurityDot11EncryptionStrength,'npSecurityCertBuff':npSecurityCertBuff,'npSecurityCertBuffIndex':npSecurityCertBuffIndex,'npSecuritySslRedirection':npSecuritySslRedirection,'npSecurityReset':npSecurityReset,'npSecurityDot11WEPStrength':npSecurityDot11WEPStrength,'npSecurityServicesSupported':npSecurityServicesSupported,'npSecurityDot11Encryption':npSecurityDot11Encryption,'npSecurityDot11MulticastCipher':npSecurityDot11MulticastCipher,'npSecurityDot11BeaconTable':npSecurityDot11BeaconTable,'npSecurityDot11BeaconEntry':npSecurityDot11BeaconEntry,'npSecurityDot11BeaconInfoXMLString':npSecurityDot11BeaconInfoXMLString,'npSecurityDot11BeaconTableNumEntries':npSecurityDot11BeaconTableNumEntries,'npSecurityDot11OpenSSIDEnabled':npSecurityDot11OpenSSIDEnabled,'npSecurityDot11DynamicEncryption':npSecurityDot11DynamicEncryption,'npSecurityDot11LinkAuthentication':npSecurityDot11LinkAuthentication,'npSecuritySnmpV3AuthAlgorithm':npSecuritySnmpV3AuthAlgorithm,'npSecuritySnmpV3PrivAlgorithm':npSecuritySnmpV3PrivAlgorithm,'npSecuritySnmpV3PassPhrase':npSecuritySnmpV3PassPhrase,'npSecurityWirelessDirectEncryptionMethod':npSecurityWirelessDirectEncryptionMethod,'npSecurityWirelessDirectEncryptedPassPhrase':npSecurityWirelessDirectEncryptedPassPhrase,'npSecurityDot1xFailSafe':npSecurityDot1xFailSafe,'npSecuritySSLProtocol':npSecuritySSLProtocol,'snmpAccess':snmpAccess,'community':community,'setCommunityName':setCommunityName,'getCommunityName':getCommunityName,'ppmMIB':ppmMIB,'ppmMIBObjects':ppmMIBObjects,'ppmGeneral':ppmGeneral,'ppmGeneralNaturalLanguage':ppmGeneralNaturalLanguage,'ppmGeneralNumberOfPrinters':ppmGeneralNumberOfPrinters,'ppmGeneralNumberOfPorts':ppmGeneralNumberOfPorts,'ppmPrinter':ppmPrinter,'ppmPrinterTable':ppmPrinterTable,'ppmPrinterEntry':ppmPrinterEntry,'ppmPrinterName':ppmPrinterName,'ppmPrinterIEEE1284DeviceId':ppmPrinterIEEE1284DeviceId,'ppmPrinterNumberOfPorts':ppmPrinterNumberOfPorts,'ppmPrinterPreferredPortIndex':ppmPrinterPreferredPortIndex,'ppmPrinterHrDeviceIndex':ppmPrinterHrDeviceIndex,'ppmPrinterSnmpCommunityName':ppmPrinterSnmpCommunityName,'ppmPrinterSnmpQueryEnabled':ppmPrinterSnmpQueryEnabled,'ppmPort':ppmPort,'ppmPortTable':ppmPortTable,'ppmPortEntry':ppmPortEntry,'ppmPortEnabled':ppmPortEnabled,'ppmPortName':ppmPortName,'ppmPortServiceNameOrURI':ppmPortServiceNameOrURI,'ppmPortProtocolType':ppmPortProtocolType,'ppmPortProtocolTargetPort':ppmPortProtocolTargetPort,'ppmPortProtocolAltSourceEnabled':ppmPortProtocolAltSourceEnabled,'ppmPortPrtChannelIndex':ppmPortPrtChannelIndex,'ppmPortLprByteCountEnabled':ppmPortLprByteCountEnabled})