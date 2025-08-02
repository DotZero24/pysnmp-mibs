_A0='eJapanseEnvLong3'
_z='eInternationalB5'
_y='eInternationalC5'
_x='eInternationalDL'
_w='eCommercial10'
_v='invalid'
_u='KBytes'
_t='InternationalDisplayString'
_s='eLegal216x340'
_r='eFoolscap'
_q='eUSLegal'
_p='disabled'
_o='enabled'
_n='unknown'
_m='testing'
_l='down'
_k='eManualSheet'
_j='eArss'
_i='eManualRoll'
_h='eTray'
_g='eCustom'
_f='ePRC16K184X260'
_e='eJISB5'
_d='ePRC16K195X270'
_c='eISOandJISA4'
_b='eISOandJISA5'
_a='eROC16K'
_Z='eStatement'
_Y='eUSLetter'
_X='eUSExecutive'
_W='eTrue'
_V='eFalse'
_U='other'
_T='deprecated'
_S='Gauge32'
_R='enable'
_Q='TruthValue'
_P='StorageType'
_O='KeyChange'
_N='disable'
_M='Enable'
_L='Disable'
_K='write-only'
_J='SnmpAdminString'
_I='read-create'
_H='DisplayString'
_G='OctetString'
_F='mandatory'
_E='optional'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InternationalDisplayString,KBytes,ProductID=mibBuilder.importSymbols('HOST-RESOURCES-MIB',_t,_u,'ProductID')
IANACharset,=mibBuilder.importSymbols('IANA-CHARSET-MIB','IANACharset')
PrtChannelTypeTC,PrtCoverStatusTC,PrtGeneralResetTC,PrtInputTypeTC,PrtInterpreterLangFamilyTC,PrtMarkerMarkTechTC,PrtMarkerSuppliesTypeTC,PrtMediaPathTypeTC,PrtOutputTypeTC=mibBuilder.importSymbols('IANA-PRINTER-MIB','PrtChannelTypeTC','PrtCoverStatusTC','PrtGeneralResetTC','PrtInputTypeTC','PrtInterpreterLangFamilyTC','PrtMarkerMarkTechTC','PrtMarkerSuppliesTypeTC','PrtMediaPathTypeTC','PrtOutputTypeTC')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
WEPKeytype,=mibBuilder.importSymbols('IEEE802dot11-MIB','WEPKeytype')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
PresentOnOff,PrtCapacityUnitTC,PrtChannelStateTC,PrtConsoleDescriptionStringTC,PrtInterpreterTwoWayTC,PrtLocalizedDescriptionStringTC,PrtMarkerAddressabilityUnitTC,PrtMarkerColorantRoleTC,PrtMarkerCounterUnitTC,PrtMarkerSuppliesClassTC,PrtMarkerSuppliesSupplyUnitTC,PrtMediaPathMaxSpeedPrintUnitTC,PrtMediaUnitTC,PrtOutputPageDeliveryOrientationTC,PrtOutputStackingOrderTC,PrtPrintOrientationTC,PrtSubUnitStatusTC=mibBuilder.importSymbols('Printer-MIB','PresentOnOff','PrtCapacityUnitTC','PrtChannelStateTC','PrtConsoleDescriptionStringTC','PrtInterpreterTwoWayTC','PrtLocalizedDescriptionStringTC','PrtMarkerAddressabilityUnitTC','PrtMarkerColorantRoleTC','PrtMarkerCounterUnitTC','PrtMarkerSuppliesClassTC','PrtMarkerSuppliesSupplyUnitTC','PrtMediaPathMaxSpeedPrintUnitTC','PrtMediaUnitTC','PrtOutputPageDeliveryOrientationTC','PrtOutputStackingOrderTC','PrtPrintOrientationTC','PrtSubUnitStatusTC')
SnmpAdminString,SnmpEngineID=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J,'SnmpEngineID')
KeyChange,=mibBuilder.importSymbols('SNMP-USER-BASED-SM-MIB',_O)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_S,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DateAndTime,DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DateAndTime',_H,'PhysAddress','RowPointer','RowStatus',_P,'TextualConvention','TestAndIncr','TimeStamp',_Q)
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
if mibBuilder.loadTexts:dot11DesiredSSID.setStatus(_A)
class _Dot11DesiredBSSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('infrastructure',1),('independent',2),('any',3)))
_Dot11DesiredBSSType_Type.__name__=_D
_Dot11DesiredBSSType_Object=MibScalar
dot11DesiredBSSType=_Dot11DesiredBSSType_Object((1,2,840,10036,1,1,1,10),_Dot11DesiredBSSType_Type())
dot11DesiredBSSType.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11DesiredBSSType.setStatus(_A)
_Dot11AuthenticationAlgorithmsTable_ObjectIdentity=ObjectIdentity
dot11AuthenticationAlgorithmsTable=_Dot11AuthenticationAlgorithmsTable_ObjectIdentity((1,2,840,10036,1,2))
_Dot11AuthenticationAlgorithmsEntry_ObjectIdentity=ObjectIdentity
dot11AuthenticationAlgorithmsEntry=_Dot11AuthenticationAlgorithmsEntry_ObjectIdentity((1,2,840,10036,1,2,1))
class _Dot11AuthenticationAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('openSystem',1),('sharedKey',2)))
_Dot11AuthenticationAlgorithm_Type.__name__=_D
_Dot11AuthenticationAlgorithm_Object=MibScalar
dot11AuthenticationAlgorithm=_Dot11AuthenticationAlgorithm_Object((1,2,840,10036,1,2,1,2),_Dot11AuthenticationAlgorithm_Type())
dot11AuthenticationAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationAlgorithm.setStatus(_A)
_Dot11AuthenticationAlgorithmsEnable_Type=TruthValue
_Dot11AuthenticationAlgorithmsEnable_Object=MibScalar
dot11AuthenticationAlgorithmsEnable=_Dot11AuthenticationAlgorithmsEnable_Object((1,2,840,10036,1,2,1,3),_Dot11AuthenticationAlgorithmsEnable_Type())
dot11AuthenticationAlgorithmsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11AuthenticationAlgorithmsEnable.setStatus(_A)
_Dot11WEPDefaultKeysTable_ObjectIdentity=ObjectIdentity
dot11WEPDefaultKeysTable=_Dot11WEPDefaultKeysTable_ObjectIdentity((1,2,840,10036,1,3))
_Dot11WEPDefaultKeysEntry_ObjectIdentity=ObjectIdentity
dot11WEPDefaultKeysEntry=_Dot11WEPDefaultKeysEntry_ObjectIdentity((1,2,840,10036,1,3,1))
_Dot11WEPDefaultKeyValue_Type=WEPKeytype
_Dot11WEPDefaultKeyValue_Object=MibScalar
dot11WEPDefaultKeyValue=_Dot11WEPDefaultKeyValue_Object((1,2,840,10036,1,3,1,2),_Dot11WEPDefaultKeyValue_Type())
dot11WEPDefaultKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11WEPDefaultKeyValue.setStatus(_A)
_Dot11PrivacyTable_ObjectIdentity=ObjectIdentity
dot11PrivacyTable=_Dot11PrivacyTable_ObjectIdentity((1,2,840,10036,1,5))
_Dot11PrivacyEntry_ObjectIdentity=ObjectIdentity
dot11PrivacyEntry=_Dot11PrivacyEntry_ObjectIdentity((1,2,840,10036,1,5,1))
_Dot11PrivacyInvoked_Type=TruthValue
_Dot11PrivacyInvoked_Object=MibScalar
dot11PrivacyInvoked=_Dot11PrivacyInvoked_Object((1,2,840,10036,1,5,1,1),_Dot11PrivacyInvoked_Type())
dot11PrivacyInvoked.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11PrivacyInvoked.setStatus(_A)
class _Dot11WEPDefaultKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Dot11WEPDefaultKeyID_Type.__name__=_D
_Dot11WEPDefaultKeyID_Object=MibScalar
dot11WEPDefaultKeyID=_Dot11WEPDefaultKeyID_Object((1,2,840,10036,1,5,1,2),_Dot11WEPDefaultKeyID_Type())
dot11WEPDefaultKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11WEPDefaultKeyID.setStatus(_A)
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
if mibBuilder.loadTexts:dot11CurrentRegDomain.setStatus(_A)
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
dot11RSNConfigAuthenticationSuite.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11RSNConfigAuthenticationSuite.setStatus(_A)
_Dot11RSNConfigAuthenticationSuiteEnabled_Type=TruthValue
_Dot11RSNConfigAuthenticationSuiteEnabled_Object=MibScalar
dot11RSNConfigAuthenticationSuiteEnabled=_Dot11RSNConfigAuthenticationSuiteEnabled_Object((1,2,840,10036,7,3,1,3),_Dot11RSNConfigAuthenticationSuiteEnabled_Type())
dot11RSNConfigAuthenticationSuiteEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dot11RSNConfigAuthenticationSuiteEnabled.setStatus(_A)
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
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,2,1,1))
class _SysDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysDescr_Type.__name__=_H
_SysDescr_Object=MibScalar
sysDescr=_SysDescr_Object((1,3,6,1,2,1,1,1),_SysDescr_Type())
sysDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDescr.setStatus(_F)
_SysObjectID_Type=ObjectIdentifier
_SysObjectID_Object=MibScalar
sysObjectID=_SysObjectID_Object((1,3,6,1,2,1,1,2),_SysObjectID_Type())
sysObjectID.setMaxAccess(_B)
if mibBuilder.loadTexts:sysObjectID.setStatus(_F)
_SysUpTime_Type=TimeTicks
_SysUpTime_Object=MibScalar
sysUpTime=_SysUpTime_Object((1,3,6,1,2,1,1,3),_SysUpTime_Type())
sysUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysUpTime.setStatus(_F)
class _SysContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysContact_Type.__name__=_H
_SysContact_Object=MibScalar
sysContact=_SysContact_Object((1,3,6,1,2,1,1,4),_SysContact_Type())
sysContact.setMaxAccess(_C)
if mibBuilder.loadTexts:sysContact.setStatus(_F)
class _SysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysName_Type.__name__=_H
_SysName_Object=MibScalar
sysName=_SysName_Object((1,3,6,1,2,1,1,5),_SysName_Type())
sysName.setMaxAccess(_C)
if mibBuilder.loadTexts:sysName.setStatus(_F)
class _SysLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysLocation_Type.__name__=_H
_SysLocation_Object=MibScalar
sysLocation=_SysLocation_Object((1,3,6,1,2,1,1,6),_SysLocation_Type())
sysLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLocation.setStatus(_F)
class _SysServices_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_SysServices_Type.__name__=_D
_SysServices_Object=MibScalar
sysServices=_SysServices_Object((1,3,6,1,2,1,1,7),_SysServices_Type())
sysServices.setMaxAccess(_B)
if mibBuilder.loadTexts:sysServices.setStatus(_F)
_SysORLastChange_Type=TimeStamp
_SysORLastChange_Object=MibScalar
sysORLastChange=_SysORLastChange_Object((1,3,6,1,2,1,1,8),_SysORLastChange_Type())
sysORLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:sysORLastChange.setStatus(_A)
_Interfaces_ObjectIdentity=ObjectIdentity
interfaces=_Interfaces_ObjectIdentity((1,3,6,1,2,1,2))
_IfNumber_Type=Integer32
_IfNumber_Object=MibScalar
ifNumber=_IfNumber_Object((1,3,6,1,2,1,2,1),_IfNumber_Type())
ifNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ifNumber.setStatus(_A)
_IfTable_ObjectIdentity=ObjectIdentity
ifTable=_IfTable_ObjectIdentity((1,3,6,1,2,1,2,2))
_IfEntry_ObjectIdentity=ObjectIdentity
ifEntry=_IfEntry_ObjectIdentity((1,3,6,1,2,1,2,2,1))
_IfIndex_Type=InterfaceIndex
_IfIndex_Object=MibScalar
ifIndex=_IfIndex_Object((1,3,6,1,2,1,2,2,1,1),_IfIndex_Type())
ifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIndex.setStatus(_A)
class _IfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfDescr_Type.__name__=_H
_IfDescr_Object=MibScalar
ifDescr=_IfDescr_Object((1,3,6,1,2,1,2,2,1,2),_IfDescr_Type())
ifDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ifDescr.setStatus(_A)
_IfType_Type=IANAifType
_IfType_Object=MibScalar
ifType=_IfType_Object((1,3,6,1,2,1,2,2,1,3),_IfType_Type())
ifType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifType.setStatus(_A)
_IfMtu_Type=Integer32
_IfMtu_Object=MibScalar
ifMtu=_IfMtu_Object((1,3,6,1,2,1,2,2,1,4),_IfMtu_Type())
ifMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:ifMtu.setStatus(_A)
_IfSpeed_Type=Gauge32
_IfSpeed_Object=MibScalar
ifSpeed=_IfSpeed_Object((1,3,6,1,2,1,2,2,1,5),_IfSpeed_Type())
ifSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSpeed.setStatus(_A)
_IfPhysAddress_Type=PhysAddress
_IfPhysAddress_Object=MibScalar
ifPhysAddress=_IfPhysAddress_Object((1,3,6,1,2,1,2,2,1,6),_IfPhysAddress_Type())
ifPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPhysAddress.setStatus(_A)
class _IfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_l,2),(_m,3)))
_IfAdminStatus_Type.__name__=_D
_IfAdminStatus_Object=MibScalar
ifAdminStatus=_IfAdminStatus_Object((1,3,6,1,2,1,2,2,1,7),_IfAdminStatus_Type())
ifAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifAdminStatus.setStatus(_A)
class _IfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),(_l,2),(_m,3),(_n,4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_IfOperStatus_Type.__name__=_D
_IfOperStatus_Object=MibScalar
ifOperStatus=_IfOperStatus_Object((1,3,6,1,2,1,2,2,1,8),_IfOperStatus_Type())
ifOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOperStatus.setStatus(_A)
_IfLastChange_Type=TimeTicks
_IfLastChange_Object=MibScalar
ifLastChange=_IfLastChange_Object((1,3,6,1,2,1,2,2,1,9),_IfLastChange_Type())
ifLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ifLastChange.setStatus(_A)
_IfInOctets_Type=Counter32
_IfInOctets_Object=MibScalar
ifInOctets=_IfInOctets_Object((1,3,6,1,2,1,2,2,1,10),_IfInOctets_Type())
ifInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifInOctets.setStatus(_A)
_IfInUcastPkts_Type=Counter32
_IfInUcastPkts_Object=MibScalar
ifInUcastPkts=_IfInUcastPkts_Object((1,3,6,1,2,1,2,2,1,11),_IfInUcastPkts_Type())
ifInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifInUcastPkts.setStatus(_A)
_IfInNUcastPkts_Type=Counter32
_IfInNUcastPkts_Object=MibScalar
ifInNUcastPkts=_IfInNUcastPkts_Object((1,3,6,1,2,1,2,2,1,12),_IfInNUcastPkts_Type())
ifInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifInNUcastPkts.setStatus(_T)
_IfInDiscards_Type=Counter32
_IfInDiscards_Object=MibScalar
ifInDiscards=_IfInDiscards_Object((1,3,6,1,2,1,2,2,1,13),_IfInDiscards_Type())
ifInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ifInDiscards.setStatus(_A)
_IfInErrors_Type=Counter32
_IfInErrors_Object=MibScalar
ifInErrors=_IfInErrors_Object((1,3,6,1,2,1,2,2,1,14),_IfInErrors_Type())
ifInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifInErrors.setStatus(_A)
_IfInUnknownProtos_Type=Counter32
_IfInUnknownProtos_Object=MibScalar
ifInUnknownProtos=_IfInUnknownProtos_Object((1,3,6,1,2,1,2,2,1,15),_IfInUnknownProtos_Type())
ifInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:ifInUnknownProtos.setStatus(_A)
_IfOutOctets_Type=Counter32
_IfOutOctets_Object=MibScalar
ifOutOctets=_IfOutOctets_Object((1,3,6,1,2,1,2,2,1,16),_IfOutOctets_Type())
ifOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOutOctets.setStatus(_A)
_IfOutUcastPkts_Type=Counter32
_IfOutUcastPkts_Object=MibScalar
ifOutUcastPkts=_IfOutUcastPkts_Object((1,3,6,1,2,1,2,2,1,17),_IfOutUcastPkts_Type())
ifOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOutUcastPkts.setStatus(_A)
_IfOutNUcastPkts_Type=Counter32
_IfOutNUcastPkts_Object=MibScalar
ifOutNUcastPkts=_IfOutNUcastPkts_Object((1,3,6,1,2,1,2,2,1,18),_IfOutNUcastPkts_Type())
ifOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOutNUcastPkts.setStatus(_T)
_IfOutDiscards_Type=Counter32
_IfOutDiscards_Object=MibScalar
ifOutDiscards=_IfOutDiscards_Object((1,3,6,1,2,1,2,2,1,19),_IfOutDiscards_Type())
ifOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOutDiscards.setStatus(_A)
_IfOutErrors_Type=Counter32
_IfOutErrors_Object=MibScalar
ifOutErrors=_IfOutErrors_Object((1,3,6,1,2,1,2,2,1,20),_IfOutErrors_Type())
ifOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOutErrors.setStatus(_A)
_IfOutQLen_Type=Gauge32
_IfOutQLen_Object=MibScalar
ifOutQLen=_IfOutQLen_Object((1,3,6,1,2,1,2,2,1,21),_IfOutQLen_Type())
ifOutQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOutQLen.setStatus(_T)
_IfSpecific_Type=ObjectIdentifier
_IfSpecific_Object=MibScalar
ifSpecific=_IfSpecific_Object((1,3,6,1,2,1,2,2,1,22),_IfSpecific_Type())
ifSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:ifSpecific.setStatus(_T)
_Ip_ObjectIdentity=ObjectIdentity
ip=_Ip_ObjectIdentity((1,3,6,1,2,1,4))
class _IpForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('not-forwarding',2)))
_IpForwarding_Type.__name__=_D
_IpForwarding_Object=MibScalar
ipForwarding=_IpForwarding_Object((1,3,6,1,2,1,4,1),_IpForwarding_Type())
ipForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwarding.setStatus(_F)
_IpDefaultTTL_Type=Integer32
_IpDefaultTTL_Object=MibScalar
ipDefaultTTL=_IpDefaultTTL_Object((1,3,6,1,2,1,4,2),_IpDefaultTTL_Type())
ipDefaultTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:ipDefaultTTL.setStatus(_F)
_IpInReceives_Type=Counter32
_IpInReceives_Object=MibScalar
ipInReceives=_IpInReceives_Object((1,3,6,1,2,1,4,3),_IpInReceives_Type())
ipInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:ipInReceives.setStatus(_F)
_IpInHdrErrors_Type=Counter32
_IpInHdrErrors_Object=MibScalar
ipInHdrErrors=_IpInHdrErrors_Object((1,3,6,1,2,1,4,4),_IpInHdrErrors_Type())
ipInHdrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ipInHdrErrors.setStatus(_F)
_IpInAddrErrors_Type=Counter32
_IpInAddrErrors_Object=MibScalar
ipInAddrErrors=_IpInAddrErrors_Object((1,3,6,1,2,1,4,5),_IpInAddrErrors_Type())
ipInAddrErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ipInAddrErrors.setStatus(_F)
_IpForwDatagrams_Type=Counter32
_IpForwDatagrams_Object=MibScalar
ipForwDatagrams=_IpForwDatagrams_Object((1,3,6,1,2,1,4,6),_IpForwDatagrams_Type())
ipForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:ipForwDatagrams.setStatus(_F)
_IpInUnknownProtos_Type=Counter32
_IpInUnknownProtos_Object=MibScalar
ipInUnknownProtos=_IpInUnknownProtos_Object((1,3,6,1,2,1,4,7),_IpInUnknownProtos_Type())
ipInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:ipInUnknownProtos.setStatus(_F)
_IpInDiscards_Type=Counter32
_IpInDiscards_Object=MibScalar
ipInDiscards=_IpInDiscards_Object((1,3,6,1,2,1,4,8),_IpInDiscards_Type())
ipInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ipInDiscards.setStatus(_F)
_IpInDelivers_Type=Counter32
_IpInDelivers_Object=MibScalar
ipInDelivers=_IpInDelivers_Object((1,3,6,1,2,1,4,9),_IpInDelivers_Type())
ipInDelivers.setMaxAccess(_B)
if mibBuilder.loadTexts:ipInDelivers.setStatus(_F)
_IpOutRequests_Type=Counter32
_IpOutRequests_Object=MibScalar
ipOutRequests=_IpOutRequests_Object((1,3,6,1,2,1,4,10),_IpOutRequests_Type())
ipOutRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ipOutRequests.setStatus(_F)
_IpOutDiscards_Type=Counter32
_IpOutDiscards_Object=MibScalar
ipOutDiscards=_IpOutDiscards_Object((1,3,6,1,2,1,4,11),_IpOutDiscards_Type())
ipOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ipOutDiscards.setStatus(_F)
_IpOutNoRoutes_Type=Counter32
_IpOutNoRoutes_Object=MibScalar
ipOutNoRoutes=_IpOutNoRoutes_Object((1,3,6,1,2,1,4,12),_IpOutNoRoutes_Type())
ipOutNoRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:ipOutNoRoutes.setStatus(_F)
_IpReasmTimeout_Type=Integer32
_IpReasmTimeout_Object=MibScalar
ipReasmTimeout=_IpReasmTimeout_Object((1,3,6,1,2,1,4,13),_IpReasmTimeout_Type())
ipReasmTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ipReasmTimeout.setStatus(_F)
_IpReasmReqds_Type=Counter32
_IpReasmReqds_Object=MibScalar
ipReasmReqds=_IpReasmReqds_Object((1,3,6,1,2,1,4,14),_IpReasmReqds_Type())
ipReasmReqds.setMaxAccess(_B)
if mibBuilder.loadTexts:ipReasmReqds.setStatus(_F)
_IpReasmOKs_Type=Counter32
_IpReasmOKs_Object=MibScalar
ipReasmOKs=_IpReasmOKs_Object((1,3,6,1,2,1,4,15),_IpReasmOKs_Type())
ipReasmOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:ipReasmOKs.setStatus(_F)
_IpReasmFails_Type=Counter32
_IpReasmFails_Object=MibScalar
ipReasmFails=_IpReasmFails_Object((1,3,6,1,2,1,4,16),_IpReasmFails_Type())
ipReasmFails.setMaxAccess(_B)
if mibBuilder.loadTexts:ipReasmFails.setStatus(_F)
_IpFragOKs_Type=Counter32
_IpFragOKs_Object=MibScalar
ipFragOKs=_IpFragOKs_Object((1,3,6,1,2,1,4,17),_IpFragOKs_Type())
ipFragOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFragOKs.setStatus(_F)
_IpFragFails_Type=Counter32
_IpFragFails_Object=MibScalar
ipFragFails=_IpFragFails_Object((1,3,6,1,2,1,4,18),_IpFragFails_Type())
ipFragFails.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFragFails.setStatus(_F)
_IpFragCreates_Type=Counter32
_IpFragCreates_Object=MibScalar
ipFragCreates=_IpFragCreates_Object((1,3,6,1,2,1,4,19),_IpFragCreates_Type())
ipFragCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:ipFragCreates.setStatus(_F)
_IpAddrTable_ObjectIdentity=ObjectIdentity
ipAddrTable=_IpAddrTable_ObjectIdentity((1,3,6,1,2,1,4,20))
_IpAddrEntry_ObjectIdentity=ObjectIdentity
ipAddrEntry=_IpAddrEntry_ObjectIdentity((1,3,6,1,2,1,4,20,1))
_IpAdEntAddr_Type=IpAddress
_IpAdEntAddr_Object=MibScalar
ipAdEntAddr=_IpAdEntAddr_Object((1,3,6,1,2,1,4,20,1,1),_IpAdEntAddr_Type())
ipAdEntAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipAdEntAddr.setStatus(_F)
_IpAdEntIfIndex_Type=Integer32
_IpAdEntIfIndex_Object=MibScalar
ipAdEntIfIndex=_IpAdEntIfIndex_Object((1,3,6,1,2,1,4,20,1,2),_IpAdEntIfIndex_Type())
ipAdEntIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipAdEntIfIndex.setStatus(_F)
_IpAdEntNetMask_Type=IpAddress
_IpAdEntNetMask_Object=MibScalar
ipAdEntNetMask=_IpAdEntNetMask_Object((1,3,6,1,2,1,4,20,1,3),_IpAdEntNetMask_Type())
ipAdEntNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipAdEntNetMask.setStatus(_F)
_IpAdEntBcastAddr_Type=Integer32
_IpAdEntBcastAddr_Object=MibScalar
ipAdEntBcastAddr=_IpAdEntBcastAddr_Object((1,3,6,1,2,1,4,20,1,4),_IpAdEntBcastAddr_Type())
ipAdEntBcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipAdEntBcastAddr.setStatus(_F)
_IpRouteTable_ObjectIdentity=ObjectIdentity
ipRouteTable=_IpRouteTable_ObjectIdentity((1,3,6,1,2,1,4,21))
_IpRouteEntry_ObjectIdentity=ObjectIdentity
ipRouteEntry=_IpRouteEntry_ObjectIdentity((1,3,6,1,2,1,4,21,1))
_IpRouteDest_Type=IpAddress
_IpRouteDest_Object=MibScalar
ipRouteDest=_IpRouteDest_Object((1,3,6,1,2,1,4,21,1,1),_IpRouteDest_Type())
ipRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteDest.setStatus(_F)
_IpRouteIfIndex_Type=Integer32
_IpRouteIfIndex_Object=MibScalar
ipRouteIfIndex=_IpRouteIfIndex_Object((1,3,6,1,2,1,4,21,1,2),_IpRouteIfIndex_Type())
ipRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteIfIndex.setStatus(_F)
_IpRouteMetric1_Type=Integer32
_IpRouteMetric1_Object=MibScalar
ipRouteMetric1=_IpRouteMetric1_Object((1,3,6,1,2,1,4,21,1,3),_IpRouteMetric1_Type())
ipRouteMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteMetric1.setStatus(_F)
_IpRouteNextHop_Type=IpAddress
_IpRouteNextHop_Object=MibScalar
ipRouteNextHop=_IpRouteNextHop_Object((1,3,6,1,2,1,4,21,1,7),_IpRouteNextHop_Type())
ipRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteNextHop.setStatus(_F)
class _IpRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_v,2),('direct',3),('indirect',4)))
_IpRouteType_Type.__name__=_D
_IpRouteType_Object=MibScalar
ipRouteType=_IpRouteType_Object((1,3,6,1,2,1,4,21,1,8),_IpRouteType_Type())
ipRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteType.setStatus(_F)
class _IpRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_U,1),('local',2),('netmgmt',3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('is-is',9),('es-is',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14)))
_IpRouteProto_Type.__name__=_D
_IpRouteProto_Object=MibScalar
ipRouteProto=_IpRouteProto_Object((1,3,6,1,2,1,4,21,1,9),_IpRouteProto_Type())
ipRouteProto.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteProto.setStatus(_F)
_IpRouteMask_Type=IpAddress
_IpRouteMask_Object=MibScalar
ipRouteMask=_IpRouteMask_Object((1,3,6,1,2,1,4,21,1,11),_IpRouteMask_Type())
ipRouteMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteMask.setStatus(_F)
_IpRouteInfo_Type=ObjectIdentifier
_IpRouteInfo_Object=MibScalar
ipRouteInfo=_IpRouteInfo_Object((1,3,6,1,2,1,4,21,1,13),_IpRouteInfo_Type())
ipRouteInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRouteInfo.setStatus(_F)
_IpNetToMediaTable_ObjectIdentity=ObjectIdentity
ipNetToMediaTable=_IpNetToMediaTable_ObjectIdentity((1,3,6,1,2,1,4,22))
_IpNetToMediaEntry_ObjectIdentity=ObjectIdentity
ipNetToMediaEntry=_IpNetToMediaEntry_ObjectIdentity((1,3,6,1,2,1,4,22,1))
_IpNetToMediaIfIndex_Type=Integer32
_IpNetToMediaIfIndex_Object=MibScalar
ipNetToMediaIfIndex=_IpNetToMediaIfIndex_Object((1,3,6,1,2,1,4,22,1,1),_IpNetToMediaIfIndex_Type())
ipNetToMediaIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaIfIndex.setStatus(_F)
_IpNetToMediaPhysAddress_Type=PhysAddress
_IpNetToMediaPhysAddress_Object=MibScalar
ipNetToMediaPhysAddress=_IpNetToMediaPhysAddress_Object((1,3,6,1,2,1,4,22,1,2),_IpNetToMediaPhysAddress_Type())
ipNetToMediaPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaPhysAddress.setStatus(_F)
_IpNetToMediaNetAddress_Type=IpAddress
_IpNetToMediaNetAddress_Object=MibScalar
ipNetToMediaNetAddress=_IpNetToMediaNetAddress_Object((1,3,6,1,2,1,4,22,1,3),_IpNetToMediaNetAddress_Type())
ipNetToMediaNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaNetAddress.setStatus(_F)
class _IpNetToMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_v,2),('dynamic',3),('static',4)))
_IpNetToMediaType_Type.__name__=_D
_IpNetToMediaType_Object=MibScalar
ipNetToMediaType=_IpNetToMediaType_Object((1,3,6,1,2,1,4,22,1,4),_IpNetToMediaType_Type())
ipNetToMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetToMediaType.setStatus(_F)
_IpRoutingDiscards_Type=Counter32
_IpRoutingDiscards_Object=MibScalar
ipRoutingDiscards=_IpRoutingDiscards_Object((1,3,6,1,2,1,4,23),_IpRoutingDiscards_Type())
ipRoutingDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoutingDiscards.setStatus(_F)
_Snmp_ObjectIdentity=ObjectIdentity
snmp=_Snmp_ObjectIdentity((1,3,6,1,2,1,11))
_SnmpInPkts_Type=Counter32
_SnmpInPkts_Object=MibScalar
snmpInPkts=_SnmpInPkts_Object((1,3,6,1,2,1,11,1),_SnmpInPkts_Type())
snmpInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInPkts.setStatus(_F)
_SnmpOutPkts_Type=Counter32
_SnmpOutPkts_Object=MibScalar
snmpOutPkts=_SnmpOutPkts_Object((1,3,6,1,2,1,11,2),_SnmpOutPkts_Type())
snmpOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutPkts.setStatus(_F)
_SnmpInBadVersions_Type=Counter32
_SnmpInBadVersions_Object=MibScalar
snmpInBadVersions=_SnmpInBadVersions_Object((1,3,6,1,2,1,11,3),_SnmpInBadVersions_Type())
snmpInBadVersions.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInBadVersions.setStatus(_F)
_SnmpInBadCommunityNames_Type=Counter32
_SnmpInBadCommunityNames_Object=MibScalar
snmpInBadCommunityNames=_SnmpInBadCommunityNames_Object((1,3,6,1,2,1,11,4),_SnmpInBadCommunityNames_Type())
snmpInBadCommunityNames.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInBadCommunityNames.setStatus(_F)
_SnmpInBadCommunityUses_Type=Counter32
_SnmpInBadCommunityUses_Object=MibScalar
snmpInBadCommunityUses=_SnmpInBadCommunityUses_Object((1,3,6,1,2,1,11,5),_SnmpInBadCommunityUses_Type())
snmpInBadCommunityUses.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInBadCommunityUses.setStatus(_F)
_SnmpInASNParseErrs_Type=Counter32
_SnmpInASNParseErrs_Object=MibScalar
snmpInASNParseErrs=_SnmpInASNParseErrs_Object((1,3,6,1,2,1,11,6),_SnmpInASNParseErrs_Type())
snmpInASNParseErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInASNParseErrs.setStatus(_F)
_SnmpInTooBigs_Type=Counter32
_SnmpInTooBigs_Object=MibScalar
snmpInTooBigs=_SnmpInTooBigs_Object((1,3,6,1,2,1,11,8),_SnmpInTooBigs_Type())
snmpInTooBigs.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInTooBigs.setStatus(_F)
_SnmpInNoSuchNames_Type=Counter32
_SnmpInNoSuchNames_Object=MibScalar
snmpInNoSuchNames=_SnmpInNoSuchNames_Object((1,3,6,1,2,1,11,9),_SnmpInNoSuchNames_Type())
snmpInNoSuchNames.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInNoSuchNames.setStatus(_F)
_SnmpInBadValues_Type=Counter32
_SnmpInBadValues_Object=MibScalar
snmpInBadValues=_SnmpInBadValues_Object((1,3,6,1,2,1,11,10),_SnmpInBadValues_Type())
snmpInBadValues.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInBadValues.setStatus(_F)
_SnmpInReadOnlys_Type=Counter32
_SnmpInReadOnlys_Object=MibScalar
snmpInReadOnlys=_SnmpInReadOnlys_Object((1,3,6,1,2,1,11,11),_SnmpInReadOnlys_Type())
snmpInReadOnlys.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInReadOnlys.setStatus(_F)
_SnmpInGenErrs_Type=Counter32
_SnmpInGenErrs_Object=MibScalar
snmpInGenErrs=_SnmpInGenErrs_Object((1,3,6,1,2,1,11,12),_SnmpInGenErrs_Type())
snmpInGenErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInGenErrs.setStatus(_F)
_SnmpInTotalReqVars_Type=Counter32
_SnmpInTotalReqVars_Object=MibScalar
snmpInTotalReqVars=_SnmpInTotalReqVars_Object((1,3,6,1,2,1,11,13),_SnmpInTotalReqVars_Type())
snmpInTotalReqVars.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInTotalReqVars.setStatus(_F)
_SnmpInTotalSetVars_Type=Counter32
_SnmpInTotalSetVars_Object=MibScalar
snmpInTotalSetVars=_SnmpInTotalSetVars_Object((1,3,6,1,2,1,11,14),_SnmpInTotalSetVars_Type())
snmpInTotalSetVars.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInTotalSetVars.setStatus(_F)
_SnmpInGetRequests_Type=Counter32
_SnmpInGetRequests_Object=MibScalar
snmpInGetRequests=_SnmpInGetRequests_Object((1,3,6,1,2,1,11,15),_SnmpInGetRequests_Type())
snmpInGetRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInGetRequests.setStatus(_F)
_SnmpInGetNexts_Type=Counter32
_SnmpInGetNexts_Object=MibScalar
snmpInGetNexts=_SnmpInGetNexts_Object((1,3,6,1,2,1,11,16),_SnmpInGetNexts_Type())
snmpInGetNexts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInGetNexts.setStatus(_F)
_SnmpInSetRequests_Type=Counter32
_SnmpInSetRequests_Object=MibScalar
snmpInSetRequests=_SnmpInSetRequests_Object((1,3,6,1,2,1,11,17),_SnmpInSetRequests_Type())
snmpInSetRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInSetRequests.setStatus(_F)
_SnmpInGetResponses_Type=Counter32
_SnmpInGetResponses_Object=MibScalar
snmpInGetResponses=_SnmpInGetResponses_Object((1,3,6,1,2,1,11,18),_SnmpInGetResponses_Type())
snmpInGetResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInGetResponses.setStatus(_F)
_SnmpInTraps_Type=Counter32
_SnmpInTraps_Object=MibScalar
snmpInTraps=_SnmpInTraps_Object((1,3,6,1,2,1,11,19),_SnmpInTraps_Type())
snmpInTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInTraps.setStatus(_F)
_SnmpOutTooBigs_Type=Counter32
_SnmpOutTooBigs_Object=MibScalar
snmpOutTooBigs=_SnmpOutTooBigs_Object((1,3,6,1,2,1,11,20),_SnmpOutTooBigs_Type())
snmpOutTooBigs.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutTooBigs.setStatus(_F)
_SnmpOutNoSuchNames_Type=Counter32
_SnmpOutNoSuchNames_Object=MibScalar
snmpOutNoSuchNames=_SnmpOutNoSuchNames_Object((1,3,6,1,2,1,11,21),_SnmpOutNoSuchNames_Type())
snmpOutNoSuchNames.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutNoSuchNames.setStatus(_F)
_SnmpOutBadValues_Type=Counter32
_SnmpOutBadValues_Object=MibScalar
snmpOutBadValues=_SnmpOutBadValues_Object((1,3,6,1,2,1,11,22),_SnmpOutBadValues_Type())
snmpOutBadValues.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutBadValues.setStatus(_F)
_SnmpOutGenErrs_Type=Counter32
_SnmpOutGenErrs_Object=MibScalar
snmpOutGenErrs=_SnmpOutGenErrs_Object((1,3,6,1,2,1,11,24),_SnmpOutGenErrs_Type())
snmpOutGenErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutGenErrs.setStatus(_F)
_SnmpOutGetRequests_Type=Counter32
_SnmpOutGetRequests_Object=MibScalar
snmpOutGetRequests=_SnmpOutGetRequests_Object((1,3,6,1,2,1,11,25),_SnmpOutGetRequests_Type())
snmpOutGetRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutGetRequests.setStatus(_F)
_SnmpOutGetNexts_Type=Counter32
_SnmpOutGetNexts_Object=MibScalar
snmpOutGetNexts=_SnmpOutGetNexts_Object((1,3,6,1,2,1,11,26),_SnmpOutGetNexts_Type())
snmpOutGetNexts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutGetNexts.setStatus(_F)
_SnmpOutSetRequests_Type=Counter32
_SnmpOutSetRequests_Object=MibScalar
snmpOutSetRequests=_SnmpOutSetRequests_Object((1,3,6,1,2,1,11,27),_SnmpOutSetRequests_Type())
snmpOutSetRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutSetRequests.setStatus(_F)
_SnmpOutGetResponses_Type=Counter32
_SnmpOutGetResponses_Object=MibScalar
snmpOutGetResponses=_SnmpOutGetResponses_Object((1,3,6,1,2,1,11,28),_SnmpOutGetResponses_Type())
snmpOutGetResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutGetResponses.setStatus(_F)
_SnmpOutTraps_Type=Counter32
_SnmpOutTraps_Object=MibScalar
snmpOutTraps=_SnmpOutTraps_Object((1,3,6,1,2,1,11,29),_SnmpOutTraps_Type())
snmpOutTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpOutTraps.setStatus(_F)
class _SnmpEnableAuthenTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_p,2)))
_SnmpEnableAuthenTraps_Type.__name__=_D
_SnmpEnableAuthenTraps_Object=MibScalar
snmpEnableAuthenTraps=_SnmpEnableAuthenTraps_Object((1,3,6,1,2,1,11,30),_SnmpEnableAuthenTraps_Type())
snmpEnableAuthenTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpEnableAuthenTraps.setStatus(_F)
_SnmpSilentDrops_Type=Counter32
_SnmpSilentDrops_Object=MibScalar
snmpSilentDrops=_SnmpSilentDrops_Object((1,3,6,1,2,1,11,31),_SnmpSilentDrops_Type())
snmpSilentDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpSilentDrops.setStatus(_A)
_SnmpProxyDrops_Type=Counter32
_SnmpProxyDrops_Object=MibScalar
snmpProxyDrops=_SnmpProxyDrops_Object((1,3,6,1,2,1,11,32),_SnmpProxyDrops_Type())
snmpProxyDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpProxyDrops.setStatus(_A)
_Host_ObjectIdentity=ObjectIdentity
host=_Host_ObjectIdentity((1,3,6,1,2,1,25))
_HrSystem_ObjectIdentity=ObjectIdentity
hrSystem=_HrSystem_ObjectIdentity((1,3,6,1,2,1,25,1))
_HrSystemUptime_Type=TimeTicks
_HrSystemUptime_Object=MibScalar
hrSystemUptime=_HrSystemUptime_Object((1,3,6,1,2,1,25,1,1),_HrSystemUptime_Type())
hrSystemUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:hrSystemUptime.setStatus(_A)
_HrSystemDate_Type=DateAndTime
_HrSystemDate_Object=MibScalar
hrSystemDate=_HrSystemDate_Object((1,3,6,1,2,1,25,1,2),_HrSystemDate_Type())
hrSystemDate.setMaxAccess(_C)
if mibBuilder.loadTexts:hrSystemDate.setStatus(_A)
class _HrSystemInitialLoadDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HrSystemInitialLoadDevice_Type.__name__=_D
_HrSystemInitialLoadDevice_Object=MibScalar
hrSystemInitialLoadDevice=_HrSystemInitialLoadDevice_Object((1,3,6,1,2,1,25,1,3),_HrSystemInitialLoadDevice_Type())
hrSystemInitialLoadDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:hrSystemInitialLoadDevice.setStatus(_A)
class _HrSystemInitialLoadParameters_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HrSystemInitialLoadParameters_Type.__name__=_t
_HrSystemInitialLoadParameters_Object=MibScalar
hrSystemInitialLoadParameters=_HrSystemInitialLoadParameters_Object((1,3,6,1,2,1,25,1,4),_HrSystemInitialLoadParameters_Type())
hrSystemInitialLoadParameters.setMaxAccess(_C)
if mibBuilder.loadTexts:hrSystemInitialLoadParameters.setStatus(_A)
_HrSystemNumUsers_Type=Gauge32
_HrSystemNumUsers_Object=MibScalar
hrSystemNumUsers=_HrSystemNumUsers_Object((1,3,6,1,2,1,25,1,5),_HrSystemNumUsers_Type())
hrSystemNumUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:hrSystemNumUsers.setStatus(_A)
_HrSystemProcesses_Type=Gauge32
_HrSystemProcesses_Object=MibScalar
hrSystemProcesses=_HrSystemProcesses_Object((1,3,6,1,2,1,25,1,6),_HrSystemProcesses_Type())
hrSystemProcesses.setMaxAccess(_B)
if mibBuilder.loadTexts:hrSystemProcesses.setStatus(_A)
class _HrSystemMaxProcesses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HrSystemMaxProcesses_Type.__name__=_D
_HrSystemMaxProcesses_Object=MibScalar
hrSystemMaxProcesses=_HrSystemMaxProcesses_Object((1,3,6,1,2,1,25,1,7),_HrSystemMaxProcesses_Type())
hrSystemMaxProcesses.setMaxAccess(_B)
if mibBuilder.loadTexts:hrSystemMaxProcesses.setStatus(_A)
_HrStorage_ObjectIdentity=ObjectIdentity
hrStorage=_HrStorage_ObjectIdentity((1,3,6,1,2,1,25,2))
_HrMemorySize_Type=KBytes
_HrMemorySize_Object=MibScalar
hrMemorySize=_HrMemorySize_Object((1,3,6,1,2,1,25,2,2),_HrMemorySize_Type())
hrMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:hrMemorySize.setStatus(_A)
if mibBuilder.loadTexts:hrMemorySize.setUnits(_u)
_HrStorageTable_ObjectIdentity=ObjectIdentity
hrStorageTable=_HrStorageTable_ObjectIdentity((1,3,6,1,2,1,25,2,3))
_HrStorageEntry_ObjectIdentity=ObjectIdentity
hrStorageEntry=_HrStorageEntry_ObjectIdentity((1,3,6,1,2,1,25,2,3,1))
class _HrStorageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HrStorageIndex_Type.__name__=_D
_HrStorageIndex_Object=MibScalar
hrStorageIndex=_HrStorageIndex_Object((1,3,6,1,2,1,25,2,3,1,1),_HrStorageIndex_Type())
hrStorageIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hrStorageIndex.setStatus(_A)
_HrStorageType_Type=AutonomousType
_HrStorageType_Object=MibScalar
hrStorageType=_HrStorageType_Object((1,3,6,1,2,1,25,2,3,1,2),_HrStorageType_Type())
hrStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:hrStorageType.setStatus(_A)
_HrStorageDescr_Type=DisplayString
_HrStorageDescr_Object=MibScalar
hrStorageDescr=_HrStorageDescr_Object((1,3,6,1,2,1,25,2,3,1,3),_HrStorageDescr_Type())
hrStorageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hrStorageDescr.setStatus(_A)
class _HrStorageAllocationUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HrStorageAllocationUnits_Type.__name__=_D
_HrStorageAllocationUnits_Object=MibScalar
hrStorageAllocationUnits=_HrStorageAllocationUnits_Object((1,3,6,1,2,1,25,2,3,1,4),_HrStorageAllocationUnits_Type())
hrStorageAllocationUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:hrStorageAllocationUnits.setStatus(_A)
if mibBuilder.loadTexts:hrStorageAllocationUnits.setUnits('Bytes')
class _HrStorageSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HrStorageSize_Type.__name__=_D
_HrStorageSize_Object=MibScalar
hrStorageSize=_HrStorageSize_Object((1,3,6,1,2,1,25,2,3,1,5),_HrStorageSize_Type())
hrStorageSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hrStorageSize.setStatus(_A)
class _HrStorageUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HrStorageUsed_Type.__name__=_D
_HrStorageUsed_Object=MibScalar
hrStorageUsed=_HrStorageUsed_Object((1,3,6,1,2,1,25,2,3,1,6),_HrStorageUsed_Type())
hrStorageUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:hrStorageUsed.setStatus(_A)
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
hrDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hrDeviceIndex.setStatus(_A)
_HrDeviceType_Type=AutonomousType
_HrDeviceType_Object=MibScalar
hrDeviceType=_HrDeviceType_Object((1,3,6,1,2,1,25,3,2,1,2),_HrDeviceType_Type())
hrDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:hrDeviceType.setStatus(_A)
class _HrDeviceDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HrDeviceDescr_Type.__name__=_H
_HrDeviceDescr_Object=MibScalar
hrDeviceDescr=_HrDeviceDescr_Object((1,3,6,1,2,1,25,3,2,1,3),_HrDeviceDescr_Type())
hrDeviceDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hrDeviceDescr.setStatus(_A)
_HrDeviceID_Type=ProductID
_HrDeviceID_Object=MibScalar
hrDeviceID=_HrDeviceID_Object((1,3,6,1,2,1,25,3,2,1,4),_HrDeviceID_Type())
hrDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:hrDeviceID.setStatus(_A)
class _HrDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_n,1),('running',2),('warning',3),(_m,4),(_l,5)))
_HrDeviceStatus_Type.__name__=_D
_HrDeviceStatus_Object=MibScalar
hrDeviceStatus=_HrDeviceStatus_Object((1,3,6,1,2,1,25,3,2,1,5),_HrDeviceStatus_Type())
hrDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hrDeviceStatus.setStatus(_A)
_HrDeviceErrors_Type=Counter32
_HrDeviceErrors_Object=MibScalar
hrDeviceErrors=_HrDeviceErrors_Object((1,3,6,1,2,1,25,3,2,1,6),_HrDeviceErrors_Type())
hrDeviceErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hrDeviceErrors.setStatus(_A)
_HrPrinterTable_ObjectIdentity=ObjectIdentity
hrPrinterTable=_HrPrinterTable_ObjectIdentity((1,3,6,1,2,1,25,3,5))
_HrPrinterEntry_ObjectIdentity=ObjectIdentity
hrPrinterEntry=_HrPrinterEntry_ObjectIdentity((1,3,6,1,2,1,25,3,5,1))
class _HrPrinterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_n,2),('idle',3),('printing',4),('warmup',5)))
_HrPrinterStatus_Type.__name__=_D
_HrPrinterStatus_Object=MibScalar
hrPrinterStatus=_HrPrinterStatus_Object((1,3,6,1,2,1,25,3,5,1,1),_HrPrinterStatus_Type())
hrPrinterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hrPrinterStatus.setStatus(_A)
_HrPrinterDetectedErrorState_Type=OctetString
_HrPrinterDetectedErrorState_Object=MibScalar
hrPrinterDetectedErrorState=_HrPrinterDetectedErrorState_Object((1,3,6,1,2,1,25,3,5,1,2),_HrPrinterDetectedErrorState_Type())
hrPrinterDetectedErrorState.setMaxAccess(_B)
if mibBuilder.loadTexts:hrPrinterDetectedErrorState.setStatus(_A)
_IfMIB_ObjectIdentity=ObjectIdentity
ifMIB=_IfMIB_ObjectIdentity((1,3,6,1,2,1,31))
_IfMIBObjects_ObjectIdentity=ObjectIdentity
ifMIBObjects=_IfMIBObjects_ObjectIdentity((1,3,6,1,2,1,31,1))
_IfTableLastChange_Type=TimeTicks
_IfTableLastChange_Object=MibScalar
ifTableLastChange=_IfTableLastChange_Object((1,3,6,1,2,1,31,1,5),_IfTableLastChange_Type())
ifTableLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ifTableLastChange.setStatus(_A)
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
prtGeneralConfigChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:prtGeneralConfigChanges.setStatus(_A)
class _PrtGeneralCurrentLocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtGeneralCurrentLocalization_Type.__name__=_D
_PrtGeneralCurrentLocalization_Object=MibScalar
prtGeneralCurrentLocalization=_PrtGeneralCurrentLocalization_Object((1,3,6,1,2,1,43,5,1,1,2),_PrtGeneralCurrentLocalization_Type())
prtGeneralCurrentLocalization.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralCurrentLocalization.setStatus(_A)
_PrtGeneralReset_Type=PrtGeneralResetTC
_PrtGeneralReset_Object=MibScalar
prtGeneralReset=_PrtGeneralReset_Object((1,3,6,1,2,1,43,5,1,1,3),_PrtGeneralReset_Type())
prtGeneralReset.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralReset.setStatus(_A)
class _PrtGeneralCurrentOperator_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PrtGeneralCurrentOperator_Type.__name__=_G
_PrtGeneralCurrentOperator_Object=MibScalar
prtGeneralCurrentOperator=_PrtGeneralCurrentOperator_Object((1,3,6,1,2,1,43,5,1,1,4),_PrtGeneralCurrentOperator_Type())
prtGeneralCurrentOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralCurrentOperator.setStatus(_A)
class _PrtGeneralServicePerson_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PrtGeneralServicePerson_Type.__name__=_G
_PrtGeneralServicePerson_Object=MibScalar
prtGeneralServicePerson=_PrtGeneralServicePerson_Object((1,3,6,1,2,1,43,5,1,1,5),_PrtGeneralServicePerson_Type())
prtGeneralServicePerson.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralServicePerson.setStatus(_A)
class _PrtInputDefaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtInputDefaultIndex_Type.__name__=_D
_PrtInputDefaultIndex_Object=MibScalar
prtInputDefaultIndex=_PrtInputDefaultIndex_Object((1,3,6,1,2,1,43,5,1,1,6),_PrtInputDefaultIndex_Type())
prtInputDefaultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputDefaultIndex.setStatus(_A)
class _PrtOutputDefaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtOutputDefaultIndex_Type.__name__=_D
_PrtOutputDefaultIndex_Object=MibScalar
prtOutputDefaultIndex=_PrtOutputDefaultIndex_Object((1,3,6,1,2,1,43,5,1,1,7),_PrtOutputDefaultIndex_Type())
prtOutputDefaultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputDefaultIndex.setStatus(_A)
class _PrtMarkerDefaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtMarkerDefaultIndex_Type.__name__=_D
_PrtMarkerDefaultIndex_Object=MibScalar
prtMarkerDefaultIndex=_PrtMarkerDefaultIndex_Object((1,3,6,1,2,1,43,5,1,1,8),_PrtMarkerDefaultIndex_Type())
prtMarkerDefaultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMarkerDefaultIndex.setStatus(_A)
class _PrtMediaPathDefaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtMediaPathDefaultIndex_Type.__name__=_D
_PrtMediaPathDefaultIndex_Object=MibScalar
prtMediaPathDefaultIndex=_PrtMediaPathDefaultIndex_Object((1,3,6,1,2,1,43,5,1,1,9),_PrtMediaPathDefaultIndex_Type())
prtMediaPathDefaultIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMediaPathDefaultIndex.setStatus(_A)
class _PrtConsoleLocalization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrtConsoleLocalization_Type.__name__=_D
_PrtConsoleLocalization_Object=MibScalar
prtConsoleLocalization=_PrtConsoleLocalization_Object((1,3,6,1,2,1,43,5,1,1,10),_PrtConsoleLocalization_Type())
prtConsoleLocalization.setMaxAccess(_C)
if mibBuilder.loadTexts:prtConsoleLocalization.setStatus(_A)
class _PrtConsoleNumberOfDisplayLines_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtConsoleNumberOfDisplayLines_Type.__name__=_D
_PrtConsoleNumberOfDisplayLines_Object=MibScalar
prtConsoleNumberOfDisplayLines=_PrtConsoleNumberOfDisplayLines_Object((1,3,6,1,2,1,43,5,1,1,11),_PrtConsoleNumberOfDisplayLines_Type())
prtConsoleNumberOfDisplayLines.setMaxAccess(_B)
if mibBuilder.loadTexts:prtConsoleNumberOfDisplayLines.setStatus(_A)
class _PrtGeneralPrinterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PrtGeneralPrinterName_Type.__name__=_G
_PrtGeneralPrinterName_Object=MibScalar
prtGeneralPrinterName=_PrtGeneralPrinterName_Object((1,3,6,1,2,1,43,5,1,1,16),_PrtGeneralPrinterName_Type())
prtGeneralPrinterName.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralPrinterName.setStatus(_A)
class _PrtGeneralSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtGeneralSerialNumber_Type.__name__=_G
_PrtGeneralSerialNumber_Object=MibScalar
prtGeneralSerialNumber=_PrtGeneralSerialNumber_Object((1,3,6,1,2,1,43,5,1,1,17),_PrtGeneralSerialNumber_Type())
prtGeneralSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGeneralSerialNumber.setStatus(_A)
_PrtCover_ObjectIdentity=ObjectIdentity
prtCover=_PrtCover_ObjectIdentity((1,3,6,1,2,1,43,6))
_PrtCoverTable_ObjectIdentity=ObjectIdentity
prtCoverTable=_PrtCoverTable_ObjectIdentity((1,3,6,1,2,1,43,6,1))
_PrtCoverEntry_ObjectIdentity=ObjectIdentity
prtCoverEntry=_PrtCoverEntry_ObjectIdentity((1,3,6,1,2,1,43,6,1,1))
_PrtCoverDescription_Type=PrtLocalizedDescriptionStringTC
_PrtCoverDescription_Object=MibScalar
prtCoverDescription=_PrtCoverDescription_Object((1,3,6,1,2,1,43,6,1,1,2),_PrtCoverDescription_Type())
prtCoverDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtCoverDescription.setStatus(_A)
_PrtCoverStatus_Type=PrtCoverStatusTC
_PrtCoverStatus_Object=MibScalar
prtCoverStatus=_PrtCoverStatus_Object((1,3,6,1,2,1,43,6,1,1,3),_PrtCoverStatus_Type())
prtCoverStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtCoverStatus.setStatus(_A)
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
prtLocalizationLanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:prtLocalizationLanguage.setStatus(_A)
class _PrtLocalizationCountry_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_PrtLocalizationCountry_Type.__name__=_G
_PrtLocalizationCountry_Object=MibScalar
prtLocalizationCountry=_PrtLocalizationCountry_Object((1,3,6,1,2,1,43,7,1,1,3),_PrtLocalizationCountry_Type())
prtLocalizationCountry.setMaxAccess(_B)
if mibBuilder.loadTexts:prtLocalizationCountry.setStatus(_A)
_PrtLocalizationCharacterSet_Type=IANACharset
_PrtLocalizationCharacterSet_Object=MibScalar
prtLocalizationCharacterSet=_PrtLocalizationCharacterSet_Object((1,3,6,1,2,1,43,7,1,1,4),_PrtLocalizationCharacterSet_Type())
prtLocalizationCharacterSet.setMaxAccess(_B)
if mibBuilder.loadTexts:prtLocalizationCharacterSet.setStatus(_A)
_PrtInput_ObjectIdentity=ObjectIdentity
prtInput=_PrtInput_ObjectIdentity((1,3,6,1,2,1,43,8))
_PrtInputTable_ObjectIdentity=ObjectIdentity
prtInputTable=_PrtInputTable_ObjectIdentity((1,3,6,1,2,1,43,8,2))
_PrtInputEntry_ObjectIdentity=ObjectIdentity
prtInputEntry=_PrtInputEntry_ObjectIdentity((1,3,6,1,2,1,43,8,2,1))
_PrtInputType_Type=PrtInputTypeTC
_PrtInputType_Object=MibScalar
prtInputType=_PrtInputType_Object((1,3,6,1,2,1,43,8,2,1,2),_PrtInputType_Type())
prtInputType.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputType.setStatus(_A)
_PrtInputDimUnit_Type=PrtMediaUnitTC
_PrtInputDimUnit_Object=MibScalar
prtInputDimUnit=_PrtInputDimUnit_Object((1,3,6,1,2,1,43,8,2,1,3),_PrtInputDimUnit_Type())
prtInputDimUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputDimUnit.setStatus(_A)
class _PrtInputMediaDimFeedDirDeclared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaDimFeedDirDeclared_Type.__name__=_D
_PrtInputMediaDimFeedDirDeclared_Object=MibScalar
prtInputMediaDimFeedDirDeclared=_PrtInputMediaDimFeedDirDeclared_Object((1,3,6,1,2,1,43,8,2,1,4),_PrtInputMediaDimFeedDirDeclared_Type())
prtInputMediaDimFeedDirDeclared.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaDimFeedDirDeclared.setStatus(_A)
class _PrtInputMediaDimXFeedDirDeclared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaDimXFeedDirDeclared_Type.__name__=_D
_PrtInputMediaDimXFeedDirDeclared_Object=MibScalar
prtInputMediaDimXFeedDirDeclared=_PrtInputMediaDimXFeedDirDeclared_Object((1,3,6,1,2,1,43,8,2,1,5),_PrtInputMediaDimXFeedDirDeclared_Type())
prtInputMediaDimXFeedDirDeclared.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaDimXFeedDirDeclared.setStatus(_A)
class _PrtInputMediaDimFeedDirChosen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaDimFeedDirChosen_Type.__name__=_D
_PrtInputMediaDimFeedDirChosen_Object=MibScalar
prtInputMediaDimFeedDirChosen=_PrtInputMediaDimFeedDirChosen_Object((1,3,6,1,2,1,43,8,2,1,6),_PrtInputMediaDimFeedDirChosen_Type())
prtInputMediaDimFeedDirChosen.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputMediaDimFeedDirChosen.setStatus(_A)
class _PrtInputMediaDimXFeedDirChosen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaDimXFeedDirChosen_Type.__name__=_D
_PrtInputMediaDimXFeedDirChosen_Object=MibScalar
prtInputMediaDimXFeedDirChosen=_PrtInputMediaDimXFeedDirChosen_Object((1,3,6,1,2,1,43,8,2,1,7),_PrtInputMediaDimXFeedDirChosen_Type())
prtInputMediaDimXFeedDirChosen.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputMediaDimXFeedDirChosen.setStatus(_A)
_PrtInputCapacityUnit_Type=PrtCapacityUnitTC
_PrtInputCapacityUnit_Object=MibScalar
prtInputCapacityUnit=_PrtInputCapacityUnit_Object((1,3,6,1,2,1,43,8,2,1,8),_PrtInputCapacityUnit_Type())
prtInputCapacityUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputCapacityUnit.setStatus(_A)
class _PrtInputMaxCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMaxCapacity_Type.__name__=_D
_PrtInputMaxCapacity_Object=MibScalar
prtInputMaxCapacity=_PrtInputMaxCapacity_Object((1,3,6,1,2,1,43,8,2,1,9),_PrtInputMaxCapacity_Type())
prtInputMaxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMaxCapacity.setStatus(_A)
class _PrtInputCurrentLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,2147483647))
_PrtInputCurrentLevel_Type.__name__=_D
_PrtInputCurrentLevel_Object=MibScalar
prtInputCurrentLevel=_PrtInputCurrentLevel_Object((1,3,6,1,2,1,43,8,2,1,10),_PrtInputCurrentLevel_Type())
prtInputCurrentLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputCurrentLevel.setStatus(_A)
_PrtInputStatus_Type=PrtSubUnitStatusTC
_PrtInputStatus_Object=MibScalar
prtInputStatus=_PrtInputStatus_Object((1,3,6,1,2,1,43,8,2,1,11),_PrtInputStatus_Type())
prtInputStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputStatus.setStatus(_A)
class _PrtInputMediaName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputMediaName_Type.__name__=_G
_PrtInputMediaName_Object=MibScalar
prtInputMediaName=_PrtInputMediaName_Object((1,3,6,1,2,1,43,8,2,1,12),_PrtInputMediaName_Type())
prtInputMediaName.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaName.setStatus(_A)
class _PrtInputName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputName_Type.__name__=_G
_PrtInputName_Object=MibScalar
prtInputName=_PrtInputName_Object((1,3,6,1,2,1,43,8,2,1,13),_PrtInputName_Type())
prtInputName.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputName.setStatus(_A)
class _PrtInputVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputVendorName_Type.__name__=_G
_PrtInputVendorName_Object=MibScalar
prtInputVendorName=_PrtInputVendorName_Object((1,3,6,1,2,1,43,8,2,1,14),_PrtInputVendorName_Type())
prtInputVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputVendorName.setStatus(_A)
class _PrtInputModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputModel_Type.__name__=_G
_PrtInputModel_Object=MibScalar
prtInputModel=_PrtInputModel_Object((1,3,6,1,2,1,43,8,2,1,15),_PrtInputModel_Type())
prtInputModel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputModel.setStatus(_A)
class _PrtInputVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputVersion_Type.__name__=_G
_PrtInputVersion_Object=MibScalar
prtInputVersion=_PrtInputVersion_Object((1,3,6,1,2,1,43,8,2,1,16),_PrtInputVersion_Type())
prtInputVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputVersion.setStatus(_A)
class _PrtInputSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PrtInputSerialNumber_Type.__name__=_G
_PrtInputSerialNumber_Object=MibScalar
prtInputSerialNumber=_PrtInputSerialNumber_Object((1,3,6,1,2,1,43,8,2,1,17),_PrtInputSerialNumber_Type())
prtInputSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputSerialNumber.setStatus(_A)
_PrtInputDescription_Type=PrtLocalizedDescriptionStringTC
_PrtInputDescription_Object=MibScalar
prtInputDescription=_PrtInputDescription_Object((1,3,6,1,2,1,43,8,2,1,18),_PrtInputDescription_Type())
prtInputDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInputDescription.setStatus(_A)
_PrtInputSecurity_Type=PresentOnOff
_PrtInputSecurity_Object=MibScalar
prtInputSecurity=_PrtInputSecurity_Object((1,3,6,1,2,1,43,8,2,1,19),_PrtInputSecurity_Type())
prtInputSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputSecurity.setStatus(_A)
class _PrtInputMediaWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaWeight_Type.__name__=_D
_PrtInputMediaWeight_Object=MibScalar
prtInputMediaWeight=_PrtInputMediaWeight_Object((1,3,6,1,2,1,43,8,2,1,20),_PrtInputMediaWeight_Type())
prtInputMediaWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaWeight.setStatus(_A)
class _PrtInputMediaType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputMediaType_Type.__name__=_G
_PrtInputMediaType_Object=MibScalar
prtInputMediaType=_PrtInputMediaType_Object((1,3,6,1,2,1,43,8,2,1,21),_PrtInputMediaType_Type())
prtInputMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaType.setStatus(_A)
class _PrtInputMediaColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtInputMediaColor_Type.__name__=_G
_PrtInputMediaColor_Object=MibScalar
prtInputMediaColor=_PrtInputMediaColor_Object((1,3,6,1,2,1,43,8,2,1,22),_PrtInputMediaColor_Type())
prtInputMediaColor.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaColor.setStatus(_A)
class _PrtInputMediaFormParts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaFormParts_Type.__name__=_D
_PrtInputMediaFormParts_Object=MibScalar
prtInputMediaFormParts=_PrtInputMediaFormParts_Object((1,3,6,1,2,1,43,8,2,1,23),_PrtInputMediaFormParts_Type())
prtInputMediaFormParts.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaFormParts.setStatus(_A)
class _PrtInputMediaLoadTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInputMediaLoadTimeout_Type.__name__=_D
_PrtInputMediaLoadTimeout_Object=MibScalar
prtInputMediaLoadTimeout=_PrtInputMediaLoadTimeout_Object((1,3,6,1,2,1,43,8,2,1,24),_PrtInputMediaLoadTimeout_Type())
prtInputMediaLoadTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInputMediaLoadTimeout.setStatus(_A)
_PrtOutput_ObjectIdentity=ObjectIdentity
prtOutput=_PrtOutput_ObjectIdentity((1,3,6,1,2,1,43,9))
_PrtOutputTable_ObjectIdentity=ObjectIdentity
prtOutputTable=_PrtOutputTable_ObjectIdentity((1,3,6,1,2,1,43,9,2))
_PrtOutputEntry_ObjectIdentity=ObjectIdentity
prtOutputEntry=_PrtOutputEntry_ObjectIdentity((1,3,6,1,2,1,43,9,2,1))
_PrtOutputType_Type=PrtOutputTypeTC
_PrtOutputType_Object=MibScalar
prtOutputType=_PrtOutputType_Object((1,3,6,1,2,1,43,9,2,1,2),_PrtOutputType_Type())
prtOutputType.setMaxAccess(_B)
if mibBuilder.loadTexts:prtOutputType.setStatus(_A)
_PrtOutputCapacityUnit_Type=PrtCapacityUnitTC
_PrtOutputCapacityUnit_Object=MibScalar
prtOutputCapacityUnit=_PrtOutputCapacityUnit_Object((1,3,6,1,2,1,43,9,2,1,3),_PrtOutputCapacityUnit_Type())
prtOutputCapacityUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtOutputCapacityUnit.setStatus(_A)
class _PrtOutputMaxCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMaxCapacity_Type.__name__=_D
_PrtOutputMaxCapacity_Object=MibScalar
prtOutputMaxCapacity=_PrtOutputMaxCapacity_Object((1,3,6,1,2,1,43,9,2,1,4),_PrtOutputMaxCapacity_Type())
prtOutputMaxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMaxCapacity.setStatus(_A)
class _PrtOutputRemainingCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,2147483647))
_PrtOutputRemainingCapacity_Type.__name__=_D
_PrtOutputRemainingCapacity_Object=MibScalar
prtOutputRemainingCapacity=_PrtOutputRemainingCapacity_Object((1,3,6,1,2,1,43,9,2,1,5),_PrtOutputRemainingCapacity_Type())
prtOutputRemainingCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputRemainingCapacity.setStatus(_A)
_PrtOutputStatus_Type=PrtSubUnitStatusTC
_PrtOutputStatus_Object=MibScalar
prtOutputStatus=_PrtOutputStatus_Object((1,3,6,1,2,1,43,9,2,1,6),_PrtOutputStatus_Type())
prtOutputStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtOutputStatus.setStatus(_A)
class _PrtOutputName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputName_Type.__name__=_G
_PrtOutputName_Object=MibScalar
prtOutputName=_PrtOutputName_Object((1,3,6,1,2,1,43,9,2,1,7),_PrtOutputName_Type())
prtOutputName.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputName.setStatus(_A)
class _PrtOutputVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputVendorName_Type.__name__=_G
_PrtOutputVendorName_Object=MibScalar
prtOutputVendorName=_PrtOutputVendorName_Object((1,3,6,1,2,1,43,9,2,1,8),_PrtOutputVendorName_Type())
prtOutputVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:prtOutputVendorName.setStatus(_A)
class _PrtOutputModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputModel_Type.__name__=_G
_PrtOutputModel_Object=MibScalar
prtOutputModel=_PrtOutputModel_Object((1,3,6,1,2,1,43,9,2,1,9),_PrtOutputModel_Type())
prtOutputModel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtOutputModel.setStatus(_A)
class _PrtOutputVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputVersion_Type.__name__=_G
_PrtOutputVersion_Object=MibScalar
prtOutputVersion=_PrtOutputVersion_Object((1,3,6,1,2,1,43,9,2,1,10),_PrtOutputVersion_Type())
prtOutputVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtOutputVersion.setStatus(_A)
class _PrtOutputSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtOutputSerialNumber_Type.__name__=_G
_PrtOutputSerialNumber_Object=MibScalar
prtOutputSerialNumber=_PrtOutputSerialNumber_Object((1,3,6,1,2,1,43,9,2,1,11),_PrtOutputSerialNumber_Type())
prtOutputSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:prtOutputSerialNumber.setStatus(_A)
_PrtOutputDescription_Type=PrtLocalizedDescriptionStringTC
_PrtOutputDescription_Object=MibScalar
prtOutputDescription=_PrtOutputDescription_Object((1,3,6,1,2,1,43,9,2,1,12),_PrtOutputDescription_Type())
prtOutputDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtOutputDescription.setStatus(_A)
_PrtOutputSecurity_Type=PresentOnOff
_PrtOutputSecurity_Object=MibScalar
prtOutputSecurity=_PrtOutputSecurity_Object((1,3,6,1,2,1,43,9,2,1,13),_PrtOutputSecurity_Type())
prtOutputSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputSecurity.setStatus(_A)
_PrtOutputDimUnit_Type=PrtMediaUnitTC
_PrtOutputDimUnit_Object=MibScalar
prtOutputDimUnit=_PrtOutputDimUnit_Object((1,3,6,1,2,1,43,9,2,1,14),_PrtOutputDimUnit_Type())
prtOutputDimUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtOutputDimUnit.setStatus(_A)
class _PrtOutputMaxDimFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMaxDimFeedDir_Type.__name__=_D
_PrtOutputMaxDimFeedDir_Object=MibScalar
prtOutputMaxDimFeedDir=_PrtOutputMaxDimFeedDir_Object((1,3,6,1,2,1,43,9,2,1,15),_PrtOutputMaxDimFeedDir_Type())
prtOutputMaxDimFeedDir.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMaxDimFeedDir.setStatus(_A)
class _PrtOutputMaxDimXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMaxDimXFeedDir_Type.__name__=_D
_PrtOutputMaxDimXFeedDir_Object=MibScalar
prtOutputMaxDimXFeedDir=_PrtOutputMaxDimXFeedDir_Object((1,3,6,1,2,1,43,9,2,1,16),_PrtOutputMaxDimXFeedDir_Type())
prtOutputMaxDimXFeedDir.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMaxDimXFeedDir.setStatus(_A)
class _PrtOutputMinDimFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMinDimFeedDir_Type.__name__=_D
_PrtOutputMinDimFeedDir_Object=MibScalar
prtOutputMinDimFeedDir=_PrtOutputMinDimFeedDir_Object((1,3,6,1,2,1,43,9,2,1,17),_PrtOutputMinDimFeedDir_Type())
prtOutputMinDimFeedDir.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMinDimFeedDir.setStatus(_A)
class _PrtOutputMinDimXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtOutputMinDimXFeedDir_Type.__name__=_D
_PrtOutputMinDimXFeedDir_Object=MibScalar
prtOutputMinDimXFeedDir=_PrtOutputMinDimXFeedDir_Object((1,3,6,1,2,1,43,9,2,1,18),_PrtOutputMinDimXFeedDir_Type())
prtOutputMinDimXFeedDir.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputMinDimXFeedDir.setStatus(_A)
_PrtOutputStackingOrder_Type=PrtOutputStackingOrderTC
_PrtOutputStackingOrder_Object=MibScalar
prtOutputStackingOrder=_PrtOutputStackingOrder_Object((1,3,6,1,2,1,43,9,2,1,19),_PrtOutputStackingOrder_Type())
prtOutputStackingOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputStackingOrder.setStatus(_A)
_PrtOutputPageDeliveryOrientation_Type=PrtOutputPageDeliveryOrientationTC
_PrtOutputPageDeliveryOrientation_Object=MibScalar
prtOutputPageDeliveryOrientation=_PrtOutputPageDeliveryOrientation_Object((1,3,6,1,2,1,43,9,2,1,20),_PrtOutputPageDeliveryOrientation_Type())
prtOutputPageDeliveryOrientation.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputPageDeliveryOrientation.setStatus(_A)
_PrtOutputBursting_Type=PresentOnOff
_PrtOutputBursting_Object=MibScalar
prtOutputBursting=_PrtOutputBursting_Object((1,3,6,1,2,1,43,9,2,1,21),_PrtOutputBursting_Type())
prtOutputBursting.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputBursting.setStatus(_A)
_PrtOutputDecollating_Type=PresentOnOff
_PrtOutputDecollating_Object=MibScalar
prtOutputDecollating=_PrtOutputDecollating_Object((1,3,6,1,2,1,43,9,2,1,22),_PrtOutputDecollating_Type())
prtOutputDecollating.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputDecollating.setStatus(_A)
_PrtOutputPageCollated_Type=PresentOnOff
_PrtOutputPageCollated_Object=MibScalar
prtOutputPageCollated=_PrtOutputPageCollated_Object((1,3,6,1,2,1,43,9,2,1,23),_PrtOutputPageCollated_Type())
prtOutputPageCollated.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputPageCollated.setStatus(_A)
_PrtOutputOffsetStacking_Type=PresentOnOff
_PrtOutputOffsetStacking_Object=MibScalar
prtOutputOffsetStacking=_PrtOutputOffsetStacking_Object((1,3,6,1,2,1,43,9,2,1,24),_PrtOutputOffsetStacking_Type())
prtOutputOffsetStacking.setMaxAccess(_C)
if mibBuilder.loadTexts:prtOutputOffsetStacking.setStatus(_A)
_PrtMarker_ObjectIdentity=ObjectIdentity
prtMarker=_PrtMarker_ObjectIdentity((1,3,6,1,2,1,43,10))
_PrtMarkerTable_ObjectIdentity=ObjectIdentity
prtMarkerTable=_PrtMarkerTable_ObjectIdentity((1,3,6,1,2,1,43,10,2))
_PrtMarkerEntry_ObjectIdentity=ObjectIdentity
prtMarkerEntry=_PrtMarkerEntry_ObjectIdentity((1,3,6,1,2,1,43,10,2,1))
_PrtMarkerMarkTech_Type=PrtMarkerMarkTechTC
_PrtMarkerMarkTech_Object=MibScalar
prtMarkerMarkTech=_PrtMarkerMarkTech_Object((1,3,6,1,2,1,43,10,2,1,2),_PrtMarkerMarkTech_Type())
prtMarkerMarkTech.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerMarkTech.setStatus(_A)
_PrtMarkerCounterUnit_Type=PrtMarkerCounterUnitTC
_PrtMarkerCounterUnit_Object=MibScalar
prtMarkerCounterUnit=_PrtMarkerCounterUnit_Object((1,3,6,1,2,1,43,10,2,1,3),_PrtMarkerCounterUnit_Type())
prtMarkerCounterUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerCounterUnit.setStatus(_A)
_PrtMarkerLifeCount_Type=Counter32
_PrtMarkerLifeCount_Object=MibScalar
prtMarkerLifeCount=_PrtMarkerLifeCount_Object((1,3,6,1,2,1,43,10,2,1,4),_PrtMarkerLifeCount_Type())
prtMarkerLifeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerLifeCount.setStatus(_A)
_PrtMarkerPowerOnCount_Type=Counter32
_PrtMarkerPowerOnCount_Object=MibScalar
prtMarkerPowerOnCount=_PrtMarkerPowerOnCount_Object((1,3,6,1,2,1,43,10,2,1,5),_PrtMarkerPowerOnCount_Type())
prtMarkerPowerOnCount.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerPowerOnCount.setStatus(_A)
class _PrtMarkerProcessColorants_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtMarkerProcessColorants_Type.__name__=_D
_PrtMarkerProcessColorants_Object=MibScalar
prtMarkerProcessColorants=_PrtMarkerProcessColorants_Object((1,3,6,1,2,1,43,10,2,1,6),_PrtMarkerProcessColorants_Type())
prtMarkerProcessColorants.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerProcessColorants.setStatus(_A)
class _PrtMarkerSpotColorants_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtMarkerSpotColorants_Type.__name__=_D
_PrtMarkerSpotColorants_Object=MibScalar
prtMarkerSpotColorants=_PrtMarkerSpotColorants_Object((1,3,6,1,2,1,43,10,2,1,7),_PrtMarkerSpotColorants_Type())
prtMarkerSpotColorants.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerSpotColorants.setStatus(_A)
_PrtMarkerAddressabilityUnit_Type=PrtMarkerAddressabilityUnitTC
_PrtMarkerAddressabilityUnit_Object=MibScalar
prtMarkerAddressabilityUnit=_PrtMarkerAddressabilityUnit_Object((1,3,6,1,2,1,43,10,2,1,8),_PrtMarkerAddressabilityUnit_Type())
prtMarkerAddressabilityUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerAddressabilityUnit.setStatus(_A)
class _PrtMarkerAddressabilityFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerAddressabilityFeedDir_Type.__name__=_D
_PrtMarkerAddressabilityFeedDir_Object=MibScalar
prtMarkerAddressabilityFeedDir=_PrtMarkerAddressabilityFeedDir_Object((1,3,6,1,2,1,43,10,2,1,9),_PrtMarkerAddressabilityFeedDir_Type())
prtMarkerAddressabilityFeedDir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerAddressabilityFeedDir.setStatus(_A)
class _PrtMarkerAddressabilityXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerAddressabilityXFeedDir_Type.__name__=_D
_PrtMarkerAddressabilityXFeedDir_Object=MibScalar
prtMarkerAddressabilityXFeedDir=_PrtMarkerAddressabilityXFeedDir_Object((1,3,6,1,2,1,43,10,2,1,10),_PrtMarkerAddressabilityXFeedDir_Type())
prtMarkerAddressabilityXFeedDir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerAddressabilityXFeedDir.setStatus(_A)
class _PrtMarkerNorthMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerNorthMargin_Type.__name__=_D
_PrtMarkerNorthMargin_Object=MibScalar
prtMarkerNorthMargin=_PrtMarkerNorthMargin_Object((1,3,6,1,2,1,43,10,2,1,11),_PrtMarkerNorthMargin_Type())
prtMarkerNorthMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerNorthMargin.setStatus(_A)
class _PrtMarkerSouthMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerSouthMargin_Type.__name__=_D
_PrtMarkerSouthMargin_Object=MibScalar
prtMarkerSouthMargin=_PrtMarkerSouthMargin_Object((1,3,6,1,2,1,43,10,2,1,12),_PrtMarkerSouthMargin_Type())
prtMarkerSouthMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerSouthMargin.setStatus(_A)
class _PrtMarkerWestMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerWestMargin_Type.__name__=_D
_PrtMarkerWestMargin_Object=MibScalar
prtMarkerWestMargin=_PrtMarkerWestMargin_Object((1,3,6,1,2,1,43,10,2,1,13),_PrtMarkerWestMargin_Type())
prtMarkerWestMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerWestMargin.setStatus(_A)
class _PrtMarkerEastMargin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerEastMargin_Type.__name__=_D
_PrtMarkerEastMargin_Object=MibScalar
prtMarkerEastMargin=_PrtMarkerEastMargin_Object((1,3,6,1,2,1,43,10,2,1,14),_PrtMarkerEastMargin_Type())
prtMarkerEastMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerEastMargin.setStatus(_A)
_PrtMarkerStatus_Type=PrtSubUnitStatusTC
_PrtMarkerStatus_Object=MibScalar
prtMarkerStatus=_PrtMarkerStatus_Object((1,3,6,1,2,1,43,10,2,1,15),_PrtMarkerStatus_Type())
prtMarkerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerStatus.setStatus(_A)
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
prtMarkerSuppliesMarkerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerSuppliesMarkerIndex.setStatus(_A)
class _PrtMarkerSuppliesColorantIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtMarkerSuppliesColorantIndex_Type.__name__=_D
_PrtMarkerSuppliesColorantIndex_Object=MibScalar
prtMarkerSuppliesColorantIndex=_PrtMarkerSuppliesColorantIndex_Object((1,3,6,1,2,1,43,11,1,1,3),_PrtMarkerSuppliesColorantIndex_Type())
prtMarkerSuppliesColorantIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerSuppliesColorantIndex.setStatus(_A)
_PrtMarkerSuppliesClass_Type=PrtMarkerSuppliesClassTC
_PrtMarkerSuppliesClass_Object=MibScalar
prtMarkerSuppliesClass=_PrtMarkerSuppliesClass_Object((1,3,6,1,2,1,43,11,1,1,4),_PrtMarkerSuppliesClass_Type())
prtMarkerSuppliesClass.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerSuppliesClass.setStatus(_A)
_PrtMarkerSuppliesType_Type=PrtMarkerSuppliesTypeTC
_PrtMarkerSuppliesType_Object=MibScalar
prtMarkerSuppliesType=_PrtMarkerSuppliesType_Object((1,3,6,1,2,1,43,11,1,1,5),_PrtMarkerSuppliesType_Type())
prtMarkerSuppliesType.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerSuppliesType.setStatus(_A)
_PrtMarkerSuppliesDescription_Type=PrtLocalizedDescriptionStringTC
_PrtMarkerSuppliesDescription_Object=MibScalar
prtMarkerSuppliesDescription=_PrtMarkerSuppliesDescription_Object((1,3,6,1,2,1,43,11,1,1,6),_PrtMarkerSuppliesDescription_Type())
prtMarkerSuppliesDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerSuppliesDescription.setStatus(_A)
_PrtMarkerSuppliesSupplyUnit_Type=PrtMarkerSuppliesSupplyUnitTC
_PrtMarkerSuppliesSupplyUnit_Object=MibScalar
prtMarkerSuppliesSupplyUnit=_PrtMarkerSuppliesSupplyUnit_Object((1,3,6,1,2,1,43,11,1,1,7),_PrtMarkerSuppliesSupplyUnit_Type())
prtMarkerSuppliesSupplyUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerSuppliesSupplyUnit.setStatus(_A)
class _PrtMarkerSuppliesMaxCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMarkerSuppliesMaxCapacity_Type.__name__=_D
_PrtMarkerSuppliesMaxCapacity_Object=MibScalar
prtMarkerSuppliesMaxCapacity=_PrtMarkerSuppliesMaxCapacity_Object((1,3,6,1,2,1,43,11,1,1,8),_PrtMarkerSuppliesMaxCapacity_Type())
prtMarkerSuppliesMaxCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMarkerSuppliesMaxCapacity.setStatus(_A)
class _PrtMarkerSuppliesLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,2147483647))
_PrtMarkerSuppliesLevel_Type.__name__=_D
_PrtMarkerSuppliesLevel_Object=MibScalar
prtMarkerSuppliesLevel=_PrtMarkerSuppliesLevel_Object((1,3,6,1,2,1,43,11,1,1,9),_PrtMarkerSuppliesLevel_Type())
prtMarkerSuppliesLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMarkerSuppliesLevel.setStatus(_A)
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
prtMarkerColorantMarkerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerColorantMarkerIndex.setStatus(_A)
_PrtMarkerColorantRole_Type=PrtMarkerColorantRoleTC
_PrtMarkerColorantRole_Object=MibScalar
prtMarkerColorantRole=_PrtMarkerColorantRole_Object((1,3,6,1,2,1,43,12,1,1,3),_PrtMarkerColorantRole_Type())
prtMarkerColorantRole.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerColorantRole.setStatus(_A)
class _PrtMarkerColorantValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtMarkerColorantValue_Type.__name__=_G
_PrtMarkerColorantValue_Object=MibScalar
prtMarkerColorantValue=_PrtMarkerColorantValue_Object((1,3,6,1,2,1,43,12,1,1,4),_PrtMarkerColorantValue_Type())
prtMarkerColorantValue.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerColorantValue.setStatus(_A)
class _PrtMarkerColorantTonality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2147483647))
_PrtMarkerColorantTonality_Type.__name__=_D
_PrtMarkerColorantTonality_Object=MibScalar
prtMarkerColorantTonality=_PrtMarkerColorantTonality_Object((1,3,6,1,2,1,43,12,1,1,5),_PrtMarkerColorantTonality_Type())
prtMarkerColorantTonality.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMarkerColorantTonality.setStatus(_A)
_PrtMediaPath_ObjectIdentity=ObjectIdentity
prtMediaPath=_PrtMediaPath_ObjectIdentity((1,3,6,1,2,1,43,13))
_PrtMediaPathTable_ObjectIdentity=ObjectIdentity
prtMediaPathTable=_PrtMediaPathTable_ObjectIdentity((1,3,6,1,2,1,43,13,4))
_PrtMediaPathEntry_ObjectIdentity=ObjectIdentity
prtMediaPathEntry=_PrtMediaPathEntry_ObjectIdentity((1,3,6,1,2,1,43,13,4,1))
_PrtMediaPathMaxSpeedPrintUnit_Type=PrtMediaPathMaxSpeedPrintUnitTC
_PrtMediaPathMaxSpeedPrintUnit_Object=MibScalar
prtMediaPathMaxSpeedPrintUnit=_PrtMediaPathMaxSpeedPrintUnit_Object((1,3,6,1,2,1,43,13,4,1,2),_PrtMediaPathMaxSpeedPrintUnit_Type())
prtMediaPathMaxSpeedPrintUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathMaxSpeedPrintUnit.setStatus(_A)
_PrtMediaPathMediaSizeUnit_Type=PrtMediaUnitTC
_PrtMediaPathMediaSizeUnit_Object=MibScalar
prtMediaPathMediaSizeUnit=_PrtMediaPathMediaSizeUnit_Object((1,3,6,1,2,1,43,13,4,1,3),_PrtMediaPathMediaSizeUnit_Type())
prtMediaPathMediaSizeUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathMediaSizeUnit.setStatus(_A)
class _PrtMediaPathMaxSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMaxSpeed_Type.__name__=_D
_PrtMediaPathMaxSpeed_Object=MibScalar
prtMediaPathMaxSpeed=_PrtMediaPathMaxSpeed_Object((1,3,6,1,2,1,43,13,4,1,4),_PrtMediaPathMaxSpeed_Type())
prtMediaPathMaxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathMaxSpeed.setStatus(_A)
class _PrtMediaPathMaxMediaFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMaxMediaFeedDir_Type.__name__=_D
_PrtMediaPathMaxMediaFeedDir_Object=MibScalar
prtMediaPathMaxMediaFeedDir=_PrtMediaPathMaxMediaFeedDir_Object((1,3,6,1,2,1,43,13,4,1,5),_PrtMediaPathMaxMediaFeedDir_Type())
prtMediaPathMaxMediaFeedDir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathMaxMediaFeedDir.setStatus(_A)
class _PrtMediaPathMaxMediaXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMaxMediaXFeedDir_Type.__name__=_D
_PrtMediaPathMaxMediaXFeedDir_Object=MibScalar
prtMediaPathMaxMediaXFeedDir=_PrtMediaPathMaxMediaXFeedDir_Object((1,3,6,1,2,1,43,13,4,1,6),_PrtMediaPathMaxMediaXFeedDir_Type())
prtMediaPathMaxMediaXFeedDir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathMaxMediaXFeedDir.setStatus(_A)
class _PrtMediaPathMinMediaFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMinMediaFeedDir_Type.__name__=_D
_PrtMediaPathMinMediaFeedDir_Object=MibScalar
prtMediaPathMinMediaFeedDir=_PrtMediaPathMinMediaFeedDir_Object((1,3,6,1,2,1,43,13,4,1,7),_PrtMediaPathMinMediaFeedDir_Type())
prtMediaPathMinMediaFeedDir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathMinMediaFeedDir.setStatus(_A)
class _PrtMediaPathMinMediaXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtMediaPathMinMediaXFeedDir_Type.__name__=_D
_PrtMediaPathMinMediaXFeedDir_Object=MibScalar
prtMediaPathMinMediaXFeedDir=_PrtMediaPathMinMediaXFeedDir_Object((1,3,6,1,2,1,43,13,4,1,8),_PrtMediaPathMinMediaXFeedDir_Type())
prtMediaPathMinMediaXFeedDir.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathMinMediaXFeedDir.setStatus(_A)
_PrtMediaPathType_Type=PrtMediaPathTypeTC
_PrtMediaPathType_Object=MibScalar
prtMediaPathType=_PrtMediaPathType_Object((1,3,6,1,2,1,43,13,4,1,9),_PrtMediaPathType_Type())
prtMediaPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathType.setStatus(_A)
_PrtMediaPathDescription_Type=PrtLocalizedDescriptionStringTC
_PrtMediaPathDescription_Object=MibScalar
prtMediaPathDescription=_PrtMediaPathDescription_Object((1,3,6,1,2,1,43,13,4,1,10),_PrtMediaPathDescription_Type())
prtMediaPathDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathDescription.setStatus(_A)
_PrtMediaPathStatus_Type=PrtSubUnitStatusTC
_PrtMediaPathStatus_Object=MibScalar
prtMediaPathStatus=_PrtMediaPathStatus_Object((1,3,6,1,2,1,43,13,4,1,11),_PrtMediaPathStatus_Type())
prtMediaPathStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtMediaPathStatus.setStatus(_A)
_PrtChannel_ObjectIdentity=ObjectIdentity
prtChannel=_PrtChannel_ObjectIdentity((1,3,6,1,2,1,43,14))
_PrtChannelTable_ObjectIdentity=ObjectIdentity
prtChannelTable=_PrtChannelTable_ObjectIdentity((1,3,6,1,2,1,43,14,1))
_PrtChannelEntry_ObjectIdentity=ObjectIdentity
prtChannelEntry=_PrtChannelEntry_ObjectIdentity((1,3,6,1,2,1,43,14,1,1))
_PrtChannelType_Type=PrtChannelTypeTC
_PrtChannelType_Object=MibScalar
prtChannelType=_PrtChannelType_Object((1,3,6,1,2,1,43,14,1,1,2),_PrtChannelType_Type())
prtChannelType.setMaxAccess(_B)
if mibBuilder.loadTexts:prtChannelType.setStatus(_A)
class _PrtChannelProtocolVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PrtChannelProtocolVersion_Type.__name__=_G
_PrtChannelProtocolVersion_Object=MibScalar
prtChannelProtocolVersion=_PrtChannelProtocolVersion_Object((1,3,6,1,2,1,43,14,1,1,3),_PrtChannelProtocolVersion_Type())
prtChannelProtocolVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtChannelProtocolVersion.setStatus(_A)
class _PrtChannelCurrentJobCntlLangIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtChannelCurrentJobCntlLangIndex_Type.__name__=_D
_PrtChannelCurrentJobCntlLangIndex_Object=MibScalar
prtChannelCurrentJobCntlLangIndex=_PrtChannelCurrentJobCntlLangIndex_Object((1,3,6,1,2,1,43,14,1,1,4),_PrtChannelCurrentJobCntlLangIndex_Type())
prtChannelCurrentJobCntlLangIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtChannelCurrentJobCntlLangIndex.setStatus(_A)
class _PrtChannelDefaultPageDescLangIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrtChannelDefaultPageDescLangIndex_Type.__name__=_D
_PrtChannelDefaultPageDescLangIndex_Object=MibScalar
prtChannelDefaultPageDescLangIndex=_PrtChannelDefaultPageDescLangIndex_Object((1,3,6,1,2,1,43,14,1,1,5),_PrtChannelDefaultPageDescLangIndex_Type())
prtChannelDefaultPageDescLangIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtChannelDefaultPageDescLangIndex.setStatus(_A)
_PrtChannelState_Type=PrtChannelStateTC
_PrtChannelState_Object=MibScalar
prtChannelState=_PrtChannelState_Object((1,3,6,1,2,1,43,14,1,1,6),_PrtChannelState_Type())
prtChannelState.setMaxAccess(_C)
if mibBuilder.loadTexts:prtChannelState.setStatus(_A)
_PrtChannelIfIndex_Type=InterfaceIndexOrZero
_PrtChannelIfIndex_Object=MibScalar
prtChannelIfIndex=_PrtChannelIfIndex_Object((1,3,6,1,2,1,43,14,1,1,7),_PrtChannelIfIndex_Type())
prtChannelIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtChannelIfIndex.setStatus(_A)
_PrtChannelStatus_Type=PrtSubUnitStatusTC
_PrtChannelStatus_Object=MibScalar
prtChannelStatus=_PrtChannelStatus_Object((1,3,6,1,2,1,43,14,1,1,8),_PrtChannelStatus_Type())
prtChannelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtChannelStatus.setStatus(_A)
class _PrtChannelInformation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtChannelInformation_Type.__name__=_G
_PrtChannelInformation_Object=MibScalar
prtChannelInformation=_PrtChannelInformation_Object((1,3,6,1,2,1,43,14,1,1,9),_PrtChannelInformation_Type())
prtChannelInformation.setMaxAccess(_B)
if mibBuilder.loadTexts:prtChannelInformation.setStatus(_A)
_PrtInterpreter_ObjectIdentity=ObjectIdentity
prtInterpreter=_PrtInterpreter_ObjectIdentity((1,3,6,1,2,1,43,15))
_PrtInterpreterTable_ObjectIdentity=ObjectIdentity
prtInterpreterTable=_PrtInterpreterTable_ObjectIdentity((1,3,6,1,2,1,43,15,1))
_PrtInterpreterEntry_ObjectIdentity=ObjectIdentity
prtInterpreterEntry=_PrtInterpreterEntry_ObjectIdentity((1,3,6,1,2,1,43,15,1,1))
_PrtInterpreterLangFamily_Type=PrtInterpreterLangFamilyTC
_PrtInterpreterLangFamily_Object=MibScalar
prtInterpreterLangFamily=_PrtInterpreterLangFamily_Object((1,3,6,1,2,1,43,15,1,1,2),_PrtInterpreterLangFamily_Type())
prtInterpreterLangFamily.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInterpreterLangFamily.setStatus(_A)
class _PrtInterpreterLangLevel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PrtInterpreterLangLevel_Type.__name__=_G
_PrtInterpreterLangLevel_Object=MibScalar
prtInterpreterLangLevel=_PrtInterpreterLangLevel_Object((1,3,6,1,2,1,43,15,1,1,3),_PrtInterpreterLangLevel_Type())
prtInterpreterLangLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInterpreterLangLevel.setStatus(_A)
class _PrtInterpreterLangVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PrtInterpreterLangVersion_Type.__name__=_G
_PrtInterpreterLangVersion_Object=MibScalar
prtInterpreterLangVersion=_PrtInterpreterLangVersion_Object((1,3,6,1,2,1,43,15,1,1,4),_PrtInterpreterLangVersion_Type())
prtInterpreterLangVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInterpreterLangVersion.setStatus(_A)
_PrtInterpreterDescription_Type=PrtLocalizedDescriptionStringTC
_PrtInterpreterDescription_Object=MibScalar
prtInterpreterDescription=_PrtInterpreterDescription_Object((1,3,6,1,2,1,43,15,1,1,5),_PrtInterpreterDescription_Type())
prtInterpreterDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInterpreterDescription.setStatus(_A)
class _PrtInterpreterVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PrtInterpreterVersion_Type.__name__=_G
_PrtInterpreterVersion_Object=MibScalar
prtInterpreterVersion=_PrtInterpreterVersion_Object((1,3,6,1,2,1,43,15,1,1,6),_PrtInterpreterVersion_Type())
prtInterpreterVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInterpreterVersion.setStatus(_A)
_PrtInterpreterDefaultOrientation_Type=PrtPrintOrientationTC
_PrtInterpreterDefaultOrientation_Object=MibScalar
prtInterpreterDefaultOrientation=_PrtInterpreterDefaultOrientation_Object((1,3,6,1,2,1,43,15,1,1,7),_PrtInterpreterDefaultOrientation_Type())
prtInterpreterDefaultOrientation.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInterpreterDefaultOrientation.setStatus(_A)
class _PrtInterpreterFeedAddressability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInterpreterFeedAddressability_Type.__name__=_D
_PrtInterpreterFeedAddressability_Object=MibScalar
prtInterpreterFeedAddressability=_PrtInterpreterFeedAddressability_Object((1,3,6,1,2,1,43,15,1,1,8),_PrtInterpreterFeedAddressability_Type())
prtInterpreterFeedAddressability.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInterpreterFeedAddressability.setStatus(_A)
class _PrtInterpreterXFeedAddressability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_PrtInterpreterXFeedAddressability_Type.__name__=_D
_PrtInterpreterXFeedAddressability_Object=MibScalar
prtInterpreterXFeedAddressability=_PrtInterpreterXFeedAddressability_Object((1,3,6,1,2,1,43,15,1,1,9),_PrtInterpreterXFeedAddressability_Type())
prtInterpreterXFeedAddressability.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInterpreterXFeedAddressability.setStatus(_A)
_PrtInterpreterDefaultCharSetIn_Type=IANACharset
_PrtInterpreterDefaultCharSetIn_Object=MibScalar
prtInterpreterDefaultCharSetIn=_PrtInterpreterDefaultCharSetIn_Object((1,3,6,1,2,1,43,15,1,1,10),_PrtInterpreterDefaultCharSetIn_Type())
prtInterpreterDefaultCharSetIn.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInterpreterDefaultCharSetIn.setStatus(_A)
_PrtInterpreterDefaultCharSetOut_Type=IANACharset
_PrtInterpreterDefaultCharSetOut_Object=MibScalar
prtInterpreterDefaultCharSetOut=_PrtInterpreterDefaultCharSetOut_Object((1,3,6,1,2,1,43,15,1,1,11),_PrtInterpreterDefaultCharSetOut_Type())
prtInterpreterDefaultCharSetOut.setMaxAccess(_C)
if mibBuilder.loadTexts:prtInterpreterDefaultCharSetOut.setStatus(_A)
_PrtInterpreterTwoWay_Type=PrtInterpreterTwoWayTC
_PrtInterpreterTwoWay_Object=MibScalar
prtInterpreterTwoWay=_PrtInterpreterTwoWay_Object((1,3,6,1,2,1,43,15,1,1,12),_PrtInterpreterTwoWay_Type())
prtInterpreterTwoWay.setMaxAccess(_B)
if mibBuilder.loadTexts:prtInterpreterTwoWay.setStatus(_A)
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
if mibBuilder.loadTexts:prtConsoleDisplayBufferText.setStatus(_A)
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_HpPrintServer_ObjectIdentity=ObjectIdentity
hpPrintServer=_HpPrintServer_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Nm_system_ObjectIdentity=ObjectIdentity
nm_system=_Nm_system_ObjectIdentity((1,3,6,1,4,1,11,2,3))
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
gdStatusLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusLineState.setStatus(_A)
_GdStatusPaperOut_Type=Integer32
_GdStatusPaperOut_Object=MibScalar
gdStatusPaperOut=_GdStatusPaperOut_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,8),_GdStatusPaperOut_Type())
gdStatusPaperOut.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusPaperOut.setStatus(_A)
_GdStatusPaperJam_Type=Integer32
_GdStatusPaperJam_Object=MibScalar
gdStatusPaperJam=_GdStatusPaperJam_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,9),_GdStatusPaperJam_Type())
gdStatusPaperJam.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusPaperJam.setStatus(_A)
class _GdStatusBusy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GdStatusBusy_Type.__name__=_D
_GdStatusBusy_Object=MibScalar
gdStatusBusy=_GdStatusBusy_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,14),_GdStatusBusy_Type())
gdStatusBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusBusy.setStatus(_A)
class _GdStatusWait_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GdStatusWait_Type.__name__=_D
_GdStatusWait_Object=MibScalar
gdStatusWait=_GdStatusWait_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,15),_GdStatusWait_Type())
gdStatusWait.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusWait.setStatus(_A)
_GdStatusInitialize_Type=Integer32
_GdStatusInitialize_Object=MibScalar
gdStatusInitialize=_GdStatusInitialize_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,16),_GdStatusInitialize_Type())
gdStatusInitialize.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusInitialize.setStatus(_A)
class _GdStatusDoorOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GdStatusDoorOpen_Type.__name__=_D
_GdStatusDoorOpen_Object=MibScalar
gdStatusDoorOpen=_GdStatusDoorOpen_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,17),_GdStatusDoorOpen_Type())
gdStatusDoorOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusDoorOpen.setStatus(_A)
_GdStatusPrinting_Type=Integer32
_GdStatusPrinting_Object=MibScalar
gdStatusPrinting=_GdStatusPrinting_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,18),_GdStatusPrinting_Type())
gdStatusPrinting.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusPrinting.setStatus(_A)
_GdStatusPaperOutput_Type=Integer32
_GdStatusPaperOutput_Object=MibScalar
gdStatusPaperOutput=_GdStatusPaperOutput_Object((1,3,6,1,4,1,11,2,3,9,1,1,2,19),_GdStatusPaperOutput_Type())
gdStatusPaperOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusPaperOutput.setStatus(_A)
_GdStatusDisplay_Type=DisplayString
_GdStatusDisplay_Object=MibScalar
gdStatusDisplay=_GdStatusDisplay_Object((1,3,6,1,4,1,11,2,3,9,1,1,3),_GdStatusDisplay_Type())
gdStatusDisplay.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusDisplay.setStatus(_A)
class _GdStatusId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_GdStatusId_Type.__name__=_G
_GdStatusId_Object=MibScalar
gdStatusId=_GdStatusId_Object((1,3,6,1,4,1,11,2,3,9,1,1,7),_GdStatusId_Type())
gdStatusId.setMaxAccess(_B)
if mibBuilder.loadTexts:gdStatusId.setStatus(_A)
_GdStatusJobTimeout_Type=Integer32
_GdStatusJobTimeout_Object=MibScalar
gdStatusJobTimeout=_GdStatusJobTimeout_Object((1,3,6,1,4,1,11,2,3,9,1,1,10),_GdStatusJobTimeout_Type())
gdStatusJobTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:gdStatusJobTimeout.setStatus('obsolete')
class _GdPasswords_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GdPasswords_Type.__name__=_G
_GdPasswords_Object=MibScalar
gdPasswords=_GdPasswords_Object((1,3,6,1,4,1,11,2,3,9,1,1,13),_GdPasswords_Type())
gdPasswords.setMaxAccess(_C)
if mibBuilder.loadTexts:gdPasswords.setStatus(_A)
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
if mibBuilder.loadTexts:energy_star.setStatus(_E)
class _Sleep_mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_Sleep_mode_Type.__name__=_D
_Sleep_mode_Object=MibScalar
sleep_mode=_Sleep_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,2),_Sleep_mode_Type())
sleep_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleep_mode.setStatus(_E)
class _Speed_energy_usage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('eFasterFirstPage',1),('eSaveEnergy',2),('eSaveMostEnergy',3),('eSaveMoreEnergy',4)))
_Speed_energy_usage_Type.__name__=_D
_Speed_energy_usage_Object=MibScalar
speed_energy_usage=_Speed_energy_usage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,50),_Speed_energy_usage_Type())
speed_energy_usage.setMaxAccess(_C)
if mibBuilder.loadTexts:speed_energy_usage.setStatus(_E)
class _Start_engine_early_warmup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eValue1',1))
_Start_engine_early_warmup_Type.__name__=_D
_Start_engine_early_warmup_Object=MibScalar
start_engine_early_warmup=_Start_engine_early_warmup_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,99),_Start_engine_early_warmup_Type())
start_engine_early_warmup.setMaxAccess(_K)
if mibBuilder.loadTexts:start_engine_early_warmup.setStatus(_F)
class _Enable_engine_early_warmup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eDisable',1),('eEnable',2)))
_Enable_engine_early_warmup_Type.__name__=_D
_Enable_engine_early_warmup_Object=MibScalar
enable_engine_early_warmup=_Enable_engine_early_warmup_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,1,101),_Enable_engine_early_warmup_Type())
enable_engine_early_warmup.setMaxAccess(_C)
if mibBuilder.loadTexts:enable_engine_early_warmup.setStatus(_E)
_Status_system_ObjectIdentity=ObjectIdentity
status_system=_Status_system_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2))
class _Install_date_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_Install_date_Type.__name__=_H
_Install_date_Object=MibScalar
install_date=_Install_date_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,8),_Install_date_Type())
install_date.setMaxAccess(_C)
if mibBuilder.loadTexts:install_date.setStatus(_E)
_Date_and_time_Type=OctetString
_Date_and_time_Object=MibScalar
date_and_time=_Date_and_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,2,17),_Date_and_time_Type())
date_and_time.setMaxAccess(_C)
if mibBuilder.loadTexts:date_and_time.setStatus(_E)
_Id_ObjectIdentity=ObjectIdentity
id=_Id_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3))
_Model_number_Type=DisplayString
_Model_number_Object=MibScalar
model_number=_Model_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,1),_Model_number_Type())
model_number.setMaxAccess(_B)
if mibBuilder.loadTexts:model_number.setStatus(_E)
class _Model_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Model_name_Type.__name__=_H
_Model_name_Object=MibScalar
model_name=_Model_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,2),_Model_name_Type())
model_name.setMaxAccess(_B)
if mibBuilder.loadTexts:model_name.setStatus(_E)
class _Serial_number_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Serial_number_Type.__name__=_H
_Serial_number_Object=MibScalar
serial_number=_Serial_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,3),_Serial_number_Type())
serial_number.setMaxAccess(_B)
if mibBuilder.loadTexts:serial_number.setStatus(_E)
_Fw_rom_datecode_Type=DisplayString
_Fw_rom_datecode_Object=MibScalar
fw_rom_datecode=_Fw_rom_datecode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,5),_Fw_rom_datecode_Type())
fw_rom_datecode.setMaxAccess(_B)
if mibBuilder.loadTexts:fw_rom_datecode.setStatus(_E)
_Fw_rom_revision_Type=DisplayString
_Fw_rom_revision_Object=MibScalar
fw_rom_revision=_Fw_rom_revision_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,6),_Fw_rom_revision_Type())
fw_rom_revision.setMaxAccess(_B)
if mibBuilder.loadTexts:fw_rom_revision.setStatus(_E)
class _Device_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Device_name_Type.__name__=_H
_Device_name_Object=MibScalar
device_name=_Device_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,10),_Device_name_Type())
device_name.setMaxAccess(_C)
if mibBuilder.loadTexts:device_name.setStatus(_E)
_Device_location_Type=DisplayString
_Device_location_Object=MibScalar
device_location=_Device_location_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,11),_Device_location_Type())
device_location.setMaxAccess(_C)
if mibBuilder.loadTexts:device_location.setStatus(_E)
_Asset_number_Type=DisplayString
_Asset_number_Object=MibScalar
asset_number=_Asset_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,3,12),_Asset_number_Type())
asset_number.setMaxAccess(_C)
if mibBuilder.loadTexts:asset_number.setStatus(_E)
_Test_ObjectIdentity=ObjectIdentity
test=_Test_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5))
class _Print_internal_page_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,7,8,9,100,101,254,255,256,350,450)));namedValues=NamedValues(*(('eNotPrintingAnInternalPage',1),('ePrintingAnUnknownInternalPage',2),('eDeviceDemoPage1ConfigurationPage',3),('eDeviceDemoPage2',4),('eDeviceDemoPage5ErrorLog',7),('eDeviceDemoPage6FileSystemDirectoryListing',8),('eDeviceDemoPage7MenuMap',9),('ePrintUsagePage',100),('eSuppliesPage',101),('eDevicePaperPathTest',254),('eDevicePageRegistrationPage',255),('ePrintQualityPages',256),('ePCLFontList1',350),('ePSFontList',450)))
_Print_internal_page_Type.__name__=_D
_Print_internal_page_Object=MibScalar
print_internal_page=_Print_internal_page_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,5,2),_Print_internal_page_Type())
print_internal_page.setMaxAccess(_C)
if mibBuilder.loadTexts:print_internal_page.setStatus(_E)
_Job_ObjectIdentity=ObjectIdentity
job=_Job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6))
_Settings_job_ObjectIdentity=ObjectIdentity
settings_job=_Settings_job_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1))
class _Cancel_job_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_Cancel_job_Type.__name__=_D
_Cancel_job_Object=MibScalar
cancel_job=_Cancel_job_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,2),_Cancel_job_Type())
cancel_job.setMaxAccess(_K)
if mibBuilder.loadTexts:cancel_job.setStatus(_E)
class _Encryption_password_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Encryption_password_type_Type.__name__=_D
_Encryption_password_type_Object=MibScalar
encryption_password_type=_Encryption_password_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,15),_Encryption_password_type_Type())
encryption_password_type.setMaxAccess(_C)
if mibBuilder.loadTexts:encryption_password_type.setStatus(_E)
_Encryption_password_max_length_Type=Integer32
_Encryption_password_max_length_Object=MibScalar
encryption_password_max_length=_Encryption_password_max_length_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,16),_Encryption_password_max_length_Type())
encryption_password_max_length.setMaxAccess(_C)
if mibBuilder.loadTexts:encryption_password_max_length.setStatus(_E)
_Encryption_password_min_length_Type=Integer32
_Encryption_password_min_length_Object=MibScalar
encryption_password_min_length=_Encryption_password_min_length_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,17),_Encryption_password_min_length_Type())
encryption_password_min_length.setMaxAccess(_C)
if mibBuilder.loadTexts:encryption_password_min_length.setStatus(_E)
class _Job_storage_supported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Job_storage_supported_Type.__name__=_D
_Job_storage_supported_Object=MibScalar
job_storage_supported=_Job_storage_supported_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,18),_Job_storage_supported_Type())
job_storage_supported.setMaxAccess(_C)
if mibBuilder.loadTexts:job_storage_supported.setStatus(_E)
_Job_storage_type_Type=OctetString
_Job_storage_type_Object=MibScalar
job_storage_type=_Job_storage_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,19),_Job_storage_type_Type())
job_storage_type.setMaxAccess(_C)
if mibBuilder.loadTexts:job_storage_type.setStatus(_E)
_Job_storage_mode_Type=OctetString
_Job_storage_mode_Object=MibScalar
job_storage_mode=_Job_storage_mode_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,20),_Job_storage_mode_Type())
job_storage_mode.setMaxAccess(_C)
if mibBuilder.loadTexts:job_storage_mode.setStatus(_E)
class _Job_storage_available_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_W,1)))
_Job_storage_available_Type.__name__=_D
_Job_storage_available_Object=MibScalar
job_storage_available=_Job_storage_available_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,21),_Job_storage_available_Type())
job_storage_available.setMaxAccess(_C)
if mibBuilder.loadTexts:job_storage_available.setStatus(_E)
_Job_storage_encryption_Type=OctetString
_Job_storage_encryption_Object=MibScalar
job_storage_encryption=_Job_storage_encryption_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,1,22),_Job_storage_encryption_Type())
job_storage_encryption.setMaxAccess(_C)
if mibBuilder.loadTexts:job_storage_encryption.setStatus(_E)
_Active_print_jobs_ObjectIdentity=ObjectIdentity
active_print_jobs=_Active_print_jobs_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,2))
_Job_being_parsed_ObjectIdentity=ObjectIdentity
job_being_parsed=_Job_being_parsed_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,2,1))
class _Current_job_parsing_id_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_Current_job_parsing_id_Type.__name__=_D
_Current_job_parsing_id_Object=MibScalar
current_job_parsing_id=_Current_job_parsing_id_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,6,2,1,1),_Current_job_parsing_id_Type())
current_job_parsing_id.setMaxAccess(_B)
if mibBuilder.loadTexts:current_job_parsing_id.setStatus(_E)
_Errorlog_ObjectIdentity=ObjectIdentity
errorlog=_Errorlog_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11))
_Error1_ObjectIdentity=ObjectIdentity
error1=_Error1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1))
_Error1_time_stamp_Type=Integer32
_Error1_time_stamp_Object=MibScalar
error1_time_stamp=_Error1_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1,1),_Error1_time_stamp_Type())
error1_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error1_time_stamp.setStatus(_E)
_Error1_code_Type=Integer32
_Error1_code_Object=MibScalar
error1_code=_Error1_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1,2),_Error1_code_Type())
error1_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error1_code.setStatus(_E)
_Error1_date_time_Type=OctetString
_Error1_date_time_Object=MibScalar
error1_date_time=_Error1_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,1,3),_Error1_date_time_Type())
error1_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error1_date_time.setStatus(_E)
_Error2_ObjectIdentity=ObjectIdentity
error2=_Error2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2))
_Error2_time_stamp_Type=Integer32
_Error2_time_stamp_Object=MibScalar
error2_time_stamp=_Error2_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2,1),_Error2_time_stamp_Type())
error2_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error2_time_stamp.setStatus(_E)
_Error2_code_Type=Integer32
_Error2_code_Object=MibScalar
error2_code=_Error2_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2,2),_Error2_code_Type())
error2_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error2_code.setStatus(_E)
_Error2_date_time_Type=OctetString
_Error2_date_time_Object=MibScalar
error2_date_time=_Error2_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,2,3),_Error2_date_time_Type())
error2_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error2_date_time.setStatus(_E)
_Error3_ObjectIdentity=ObjectIdentity
error3=_Error3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3))
_Error3_time_stamp_Type=Integer32
_Error3_time_stamp_Object=MibScalar
error3_time_stamp=_Error3_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3,1),_Error3_time_stamp_Type())
error3_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error3_time_stamp.setStatus(_E)
_Error3_code_Type=Integer32
_Error3_code_Object=MibScalar
error3_code=_Error3_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3,2),_Error3_code_Type())
error3_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error3_code.setStatus(_E)
_Error3_date_time_Type=OctetString
_Error3_date_time_Object=MibScalar
error3_date_time=_Error3_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,3,3),_Error3_date_time_Type())
error3_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error3_date_time.setStatus(_E)
_Error4_ObjectIdentity=ObjectIdentity
error4=_Error4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4))
_Error4_time_stamp_Type=Integer32
_Error4_time_stamp_Object=MibScalar
error4_time_stamp=_Error4_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4,1),_Error4_time_stamp_Type())
error4_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error4_time_stamp.setStatus(_E)
_Error4_code_Type=Integer32
_Error4_code_Object=MibScalar
error4_code=_Error4_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4,2),_Error4_code_Type())
error4_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error4_code.setStatus(_E)
_Error4_date_time_Type=OctetString
_Error4_date_time_Object=MibScalar
error4_date_time=_Error4_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,4,3),_Error4_date_time_Type())
error4_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error4_date_time.setStatus(_E)
_Error5_ObjectIdentity=ObjectIdentity
error5=_Error5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5))
_Error5_time_stamp_Type=Integer32
_Error5_time_stamp_Object=MibScalar
error5_time_stamp=_Error5_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5,1),_Error5_time_stamp_Type())
error5_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error5_time_stamp.setStatus(_E)
_Error5_code_Type=Integer32
_Error5_code_Object=MibScalar
error5_code=_Error5_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5,2),_Error5_code_Type())
error5_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error5_code.setStatus(_E)
_Error5_date_time_Type=OctetString
_Error5_date_time_Object=MibScalar
error5_date_time=_Error5_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,5,3),_Error5_date_time_Type())
error5_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error5_date_time.setStatus(_E)
_Error6_ObjectIdentity=ObjectIdentity
error6=_Error6_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6))
_Error6_time_stamp_Type=Integer32
_Error6_time_stamp_Object=MibScalar
error6_time_stamp=_Error6_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6,1),_Error6_time_stamp_Type())
error6_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error6_time_stamp.setStatus(_E)
_Error6_code_Type=Integer32
_Error6_code_Object=MibScalar
error6_code=_Error6_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6,2),_Error6_code_Type())
error6_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error6_code.setStatus(_E)
_Error6_date_time_Type=OctetString
_Error6_date_time_Object=MibScalar
error6_date_time=_Error6_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,6,3),_Error6_date_time_Type())
error6_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error6_date_time.setStatus(_E)
_Error7_ObjectIdentity=ObjectIdentity
error7=_Error7_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7))
_Error7_time_stamp_Type=Integer32
_Error7_time_stamp_Object=MibScalar
error7_time_stamp=_Error7_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7,1),_Error7_time_stamp_Type())
error7_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error7_time_stamp.setStatus(_E)
_Error7_code_Type=Integer32
_Error7_code_Object=MibScalar
error7_code=_Error7_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7,2),_Error7_code_Type())
error7_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error7_code.setStatus(_E)
_Error7_date_time_Type=OctetString
_Error7_date_time_Object=MibScalar
error7_date_time=_Error7_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,7,3),_Error7_date_time_Type())
error7_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error7_date_time.setStatus(_E)
_Error8_ObjectIdentity=ObjectIdentity
error8=_Error8_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8))
_Error8_time_stamp_Type=Integer32
_Error8_time_stamp_Object=MibScalar
error8_time_stamp=_Error8_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8,1),_Error8_time_stamp_Type())
error8_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error8_time_stamp.setStatus(_E)
_Error8_code_Type=Integer32
_Error8_code_Object=MibScalar
error8_code=_Error8_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8,2),_Error8_code_Type())
error8_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error8_code.setStatus(_E)
_Error8_date_time_Type=OctetString
_Error8_date_time_Object=MibScalar
error8_date_time=_Error8_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,8,3),_Error8_date_time_Type())
error8_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error8_date_time.setStatus(_E)
_Error9_ObjectIdentity=ObjectIdentity
error9=_Error9_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9))
_Error9_time_stamp_Type=Integer32
_Error9_time_stamp_Object=MibScalar
error9_time_stamp=_Error9_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9,1),_Error9_time_stamp_Type())
error9_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error9_time_stamp.setStatus(_E)
_Error9_code_Type=Integer32
_Error9_code_Object=MibScalar
error9_code=_Error9_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9,2),_Error9_code_Type())
error9_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error9_code.setStatus(_E)
_Error9_date_time_Type=OctetString
_Error9_date_time_Object=MibScalar
error9_date_time=_Error9_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,9,3),_Error9_date_time_Type())
error9_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error9_date_time.setStatus(_E)
_Error10_ObjectIdentity=ObjectIdentity
error10=_Error10_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10))
_Error10_time_stamp_Type=Integer32
_Error10_time_stamp_Object=MibScalar
error10_time_stamp=_Error10_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10,1),_Error10_time_stamp_Type())
error10_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error10_time_stamp.setStatus(_E)
_Error10_code_Type=Integer32
_Error10_code_Object=MibScalar
error10_code=_Error10_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10,2),_Error10_code_Type())
error10_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error10_code.setStatus(_E)
_Error10_date_time_Type=OctetString
_Error10_date_time_Object=MibScalar
error10_date_time=_Error10_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,10,3),_Error10_date_time_Type())
error10_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error10_date_time.setStatus(_E)
_Error11_ObjectIdentity=ObjectIdentity
error11=_Error11_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11))
_Error11_time_stamp_Type=Integer32
_Error11_time_stamp_Object=MibScalar
error11_time_stamp=_Error11_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11,1),_Error11_time_stamp_Type())
error11_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error11_time_stamp.setStatus(_E)
_Error11_code_Type=Integer32
_Error11_code_Object=MibScalar
error11_code=_Error11_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11,2),_Error11_code_Type())
error11_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error11_code.setStatus(_E)
_Error11_date_time_Type=OctetString
_Error11_date_time_Object=MibScalar
error11_date_time=_Error11_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,11,3),_Error11_date_time_Type())
error11_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error11_date_time.setStatus(_E)
_Error12_ObjectIdentity=ObjectIdentity
error12=_Error12_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12))
_Error12_time_stamp_Type=Integer32
_Error12_time_stamp_Object=MibScalar
error12_time_stamp=_Error12_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12,1),_Error12_time_stamp_Type())
error12_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error12_time_stamp.setStatus(_E)
_Error12_code_Type=Integer32
_Error12_code_Object=MibScalar
error12_code=_Error12_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12,2),_Error12_code_Type())
error12_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error12_code.setStatus(_E)
_Error12_date_time_Type=OctetString
_Error12_date_time_Object=MibScalar
error12_date_time=_Error12_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,12,3),_Error12_date_time_Type())
error12_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error12_date_time.setStatus(_E)
_Error13_ObjectIdentity=ObjectIdentity
error13=_Error13_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13))
_Error13_time_stamp_Type=Integer32
_Error13_time_stamp_Object=MibScalar
error13_time_stamp=_Error13_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13,1),_Error13_time_stamp_Type())
error13_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error13_time_stamp.setStatus(_E)
_Error13_code_Type=Integer32
_Error13_code_Object=MibScalar
error13_code=_Error13_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13,2),_Error13_code_Type())
error13_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error13_code.setStatus(_E)
_Error13_date_time_Type=OctetString
_Error13_date_time_Object=MibScalar
error13_date_time=_Error13_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,13,3),_Error13_date_time_Type())
error13_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error13_date_time.setStatus(_E)
_Error14_ObjectIdentity=ObjectIdentity
error14=_Error14_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14))
_Error14_time_stamp_Type=Integer32
_Error14_time_stamp_Object=MibScalar
error14_time_stamp=_Error14_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14,1),_Error14_time_stamp_Type())
error14_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error14_time_stamp.setStatus(_E)
_Error14_code_Type=Integer32
_Error14_code_Object=MibScalar
error14_code=_Error14_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14,2),_Error14_code_Type())
error14_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error14_code.setStatus(_E)
_Error14_date_time_Type=OctetString
_Error14_date_time_Object=MibScalar
error14_date_time=_Error14_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,14,3),_Error14_date_time_Type())
error14_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error14_date_time.setStatus(_E)
_Error15_ObjectIdentity=ObjectIdentity
error15=_Error15_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15))
_Error15_time_stamp_Type=Integer32
_Error15_time_stamp_Object=MibScalar
error15_time_stamp=_Error15_time_stamp_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15,1),_Error15_time_stamp_Type())
error15_time_stamp.setMaxAccess(_B)
if mibBuilder.loadTexts:error15_time_stamp.setStatus(_E)
_Error15_code_Type=Integer32
_Error15_code_Object=MibScalar
error15_code=_Error15_code_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15,2),_Error15_code_Type())
error15_code.setMaxAccess(_B)
if mibBuilder.loadTexts:error15_code.setStatus(_E)
_Error15_date_time_Type=OctetString
_Error15_date_time_Object=MibScalar
error15_date_time=_Error15_date_time_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,11,15,3),_Error15_date_time_Type())
error15_date_time.setMaxAccess(_B)
if mibBuilder.loadTexts:error15_date_time.setStatus(_E)
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
printed_media_simplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_simplex_count.setStatus(_E)
class _Printed_media_duplex_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,930576247))
_Printed_media_duplex_count_Type.__name__=_D
_Printed_media_duplex_count_Object=MibScalar
printed_media_duplex_count=_Printed_media_duplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,1,3),_Printed_media_duplex_count_Type())
printed_media_duplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_duplex_count.setStatus(_E)
_Usage_printer_total_charge_Type=OctetString
_Usage_printer_total_charge_Object=MibScalar
usage_printer_total_charge=_Usage_printer_total_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,2),_Usage_printer_total_charge_Type())
usage_printer_total_charge.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_printer_total_charge.setStatus(_E)
_Usage_average_toner_coverage_Type=OctetString
_Usage_average_toner_coverage_Object=MibScalar
usage_average_toner_coverage=_Usage_average_toner_coverage_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,3),_Usage_average_toner_coverage_Type())
usage_average_toner_coverage.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_average_toner_coverage.setStatus(_E)
class _Usage_staple_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,930576247))
_Usage_staple_count_Type.__name__=_D
_Usage_staple_count_Object=MibScalar
usage_staple_count=_Usage_staple_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,4),_Usage_staple_count_Type())
usage_staple_count.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_staple_count.setStatus(_E)
_Usage_printer_mono_total_charge_Type=OctetString
_Usage_printer_mono_total_charge_Object=MibScalar
usage_printer_mono_total_charge=_Usage_printer_mono_total_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,12),_Usage_printer_mono_total_charge_Type())
usage_printer_mono_total_charge.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_printer_mono_total_charge.setStatus(_E)
_Usage_printer_color_total_charge_Type=OctetString
_Usage_printer_color_total_charge_Object=MibScalar
usage_printer_color_total_charge=_Usage_printer_color_total_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,13),_Usage_printer_color_total_charge_Type())
usage_printer_color_total_charge.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_printer_color_total_charge.setStatus(_E)
_Print_meter_equivalent_impression_count_Type=OctetString
_Print_meter_equivalent_impression_count_Object=MibScalar
print_meter_equivalent_impression_count=_Print_meter_equivalent_impression_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,1,44),_Print_meter_equivalent_impression_count_Type())
print_meter_equivalent_impression_count.setMaxAccess(_B)
if mibBuilder.loadTexts:print_meter_equivalent_impression_count.setStatus(_E)
_Scanner_accounting_ObjectIdentity=ObjectIdentity
scanner_accounting=_Scanner_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,2))
_Usage_scanner_total_charge_Type=OctetString
_Usage_scanner_total_charge_Object=MibScalar
usage_scanner_total_charge=_Usage_scanner_total_charge_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,2,2),_Usage_scanner_total_charge_Type())
usage_scanner_total_charge.setMaxAccess(_B)
if mibBuilder.loadTexts:usage_scanner_total_charge.setStatus(_E)
_Printer_color_accounting_ObjectIdentity=ObjectIdentity
printer_color_accounting=_Printer_color_accounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3))
_Printed_media_color_usage_ObjectIdentity=ObjectIdentity
printed_media_color_usage=_Printed_media_color_usage_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1))
_Printed_media_color_simplex_count_Type=Integer32
_Printed_media_color_simplex_count_Object=MibScalar
printed_media_color_simplex_count=_Printed_media_color_simplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1,1),_Printed_media_color_simplex_count_Type())
printed_media_color_simplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_color_simplex_count.setStatus(_E)
_Printed_media_color_duplex_count_Type=Integer32
_Printed_media_color_duplex_count_Object=MibScalar
printed_media_color_duplex_count=_Printed_media_color_duplex_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,1,16,3,1,3),_Printed_media_color_duplex_count_Type())
printed_media_color_duplex_count.setMaxAccess(_B)
if mibBuilder.loadTexts:printed_media_color_duplex_count.setStatus(_E)
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
scanner_accessory_adf_sheet_count.setMaxAccess(_B)
if mibBuilder.loadTexts:scanner_accessory_adf_sheet_count.setStatus(_E)
class _Scanner_accessory_flatbed_scan_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Scanner_accessory_flatbed_scan_count_Type.__name__=_D
_Scanner_accessory_flatbed_scan_count_Object=MibScalar
scanner_accessory_flatbed_scan_count=_Scanner_accessory_flatbed_scan_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,21),_Scanner_accessory_flatbed_scan_count_Type())
scanner_accessory_flatbed_scan_count.setMaxAccess(_B)
if mibBuilder.loadTexts:scanner_accessory_flatbed_scan_count.setStatus(_E)
_Scanner_accessory_copy_job_scan_count_Type=Integer32
_Scanner_accessory_copy_job_scan_count_Object=MibScalar
scanner_accessory_copy_job_scan_count=_Scanner_accessory_copy_job_scan_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,61),_Scanner_accessory_copy_job_scan_count_Type())
scanner_accessory_copy_job_scan_count.setMaxAccess(_B)
if mibBuilder.loadTexts:scanner_accessory_copy_job_scan_count.setStatus(_E)
_Scanner_accessory_send_job_scan_count_Type=Integer32
_Scanner_accessory_send_job_scan_count_Object=MibScalar
scanner_accessory_send_job_scan_count=_Scanner_accessory_send_job_scan_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,62),_Scanner_accessory_send_job_scan_count_Type())
scanner_accessory_send_job_scan_count.setMaxAccess(_B)
if mibBuilder.loadTexts:scanner_accessory_send_job_scan_count.setStatus(_E)
_Scanner_accessory_total_copy_pages_printed_Type=Integer32
_Scanner_accessory_total_copy_pages_printed_Object=MibScalar
scanner_accessory_total_copy_pages_printed=_Scanner_accessory_total_copy_pages_printed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,63),_Scanner_accessory_total_copy_pages_printed_Type())
scanner_accessory_total_copy_pages_printed.setMaxAccess(_B)
if mibBuilder.loadTexts:scanner_accessory_total_copy_pages_printed.setStatus(_E)
class _Scan_to_folder_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999999))
_Scan_to_folder_count_Type.__name__=_D
_Scan_to_folder_count_Object=MibScalar
scan_to_folder_count=_Scan_to_folder_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,89),_Scan_to_folder_count_Type())
scan_to_folder_count.setMaxAccess(_B)
if mibBuilder.loadTexts:scan_to_folder_count.setStatus(_E)
class _Fax_job_scan_count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999999))
_Fax_job_scan_count_Type.__name__=_D
_Fax_job_scan_count_Object=MibScalar
fax_job_scan_count=_Fax_job_scan_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,90),_Fax_job_scan_count_Type())
fax_job_scan_count.setMaxAccess(_B)
if mibBuilder.loadTexts:fax_job_scan_count.setStatus(_E)
_Scanner_accessory_total_copy_mono_pages_printed_Type=Integer32
_Scanner_accessory_total_copy_mono_pages_printed_Object=MibScalar
scanner_accessory_total_copy_mono_pages_printed=_Scanner_accessory_total_copy_mono_pages_printed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,122),_Scanner_accessory_total_copy_mono_pages_printed_Type())
scanner_accessory_total_copy_mono_pages_printed.setMaxAccess(_B)
if mibBuilder.loadTexts:scanner_accessory_total_copy_mono_pages_printed.setStatus(_E)
_Scanner_accessory_total_copy_color_pages_printed_Type=Integer32
_Scanner_accessory_total_copy_color_pages_printed_Object=MibScalar
scanner_accessory_total_copy_color_pages_printed=_Scanner_accessory_total_copy_color_pages_printed_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,2,2,1,123),_Scanner_accessory_total_copy_color_pages_printed_Type())
scanner_accessory_total_copy_color_pages_printed.setMaxAccess(_B)
if mibBuilder.loadTexts:scanner_accessory_total_copy_color_pages_printed.setStatus(_E)
_Processing_subsystem_ObjectIdentity=ObjectIdentity
processing_subsystem=_Processing_subsystem_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3))
_Pdl_ObjectIdentity=ObjectIdentity
pdl=_Pdl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3))
_Pdl_pcl_ObjectIdentity=ObjectIdentity
pdl_pcl=_Pdl_pcl_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3))
_Pcl_total_page_count_Type=Integer32
_Pcl_total_page_count_Object=MibScalar
pcl_total_page_count=_Pcl_total_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,3,5),_Pcl_total_page_count_Type())
pcl_total_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:pcl_total_page_count.setStatus(_E)
_Pdl_postscript_ObjectIdentity=ObjectIdentity
pdl_postscript=_Pdl_postscript_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4))
_Postscript_total_page_count_Type=Integer32
_Postscript_total_page_count_Object=MibScalar
postscript_total_page_count=_Postscript_total_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,3,4,5),_Postscript_total_page_count_Type())
postscript_total_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:postscript_total_page_count.setStatus(_E)
_Fax_proc_sub_ObjectIdentity=ObjectIdentity
fax_proc_sub=_Fax_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7))
_Settings_fax_proc_sub_ObjectIdentity=ObjectIdentity
settings_fax_proc_sub=_Settings_fax_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1))
_Fax_print_page_count_Type=Integer32
_Fax_print_page_count_Object=MibScalar
fax_print_page_count=_Fax_print_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,1,32),_Fax_print_page_count_Type())
fax_print_page_count.setMaxAccess(_C)
if mibBuilder.loadTexts:fax_print_page_count.setStatus(_E)
_Status_fax_proc_sub_ObjectIdentity=ObjectIdentity
status_fax_proc_sub=_Status_fax_proc_sub_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2))
_Afax_send_page_count_Type=Integer32
_Afax_send_page_count_Object=MibScalar
afax_send_page_count=_Afax_send_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,11),_Afax_send_page_count_Type())
afax_send_page_count.setMaxAccess(_C)
if mibBuilder.loadTexts:afax_send_page_count.setStatus(_E)
_Afax_recv_page_count_Type=Integer32
_Afax_recv_page_count_Object=MibScalar
afax_recv_page_count=_Afax_recv_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,3,7,2,12),_Afax_recv_page_count_Type())
afax_recv_page_count.setMaxAccess(_C)
if mibBuilder.loadTexts:afax_recv_page_count.setStatus(_E)
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
if mibBuilder.loadTexts:total_engine_page_count.setStatus(_E)
_Total_mono_page_count_Type=Integer32
_Total_mono_page_count_Object=MibScalar
total_mono_page_count=_Total_mono_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,6),_Total_mono_page_count_Type())
total_mono_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:total_mono_page_count.setStatus(_E)
_Total_color_page_count_Type=Integer32
_Total_color_page_count_Object=MibScalar
total_color_page_count=_Total_color_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,7),_Total_color_page_count_Type())
total_color_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:total_color_page_count.setStatus(_E)
_Duplex_page_count_Type=Integer32
_Duplex_page_count_Object=MibScalar
duplex_page_count=_Duplex_page_count_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,2,22),_Duplex_page_count_Type())
duplex_page_count.setMaxAccess(_B)
if mibBuilder.loadTexts:duplex_page_count.setStatus(_E)
_Intray_ObjectIdentity=ObjectIdentity
intray=_Intray_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3))
_Status_intray_ObjectIdentity=ObjectIdentity
status_intray=_Status_intray_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,2))
_Not_ready_tray_empty_Type=OctetString
_Not_ready_tray_empty_Object=MibScalar
not_ready_tray_empty=_Not_ready_tray_empty_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,2,2),_Not_ready_tray_empty_Type())
not_ready_tray_empty.setMaxAccess(_B)
if mibBuilder.loadTexts:not_ready_tray_empty.setStatus(_E)
_Intrays_ObjectIdentity=ObjectIdentity
intrays=_Intrays_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3))
_Intray1_ObjectIdentity=ObjectIdentity
intray1=_Intray1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1))
class _Tray1_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,15,17,24,25,26,34,44,45,71,74,75,78,80,81,89,90,91,92,100,101,110,111,118,121,122,127,328,32765)));namedValues=NamedValues(*((_X,1),(_Y,2),(_q,3),(_r,10),(_Z,15),(_a,17),('eISOandJISA6',24),(_b,25),(_c,26),(_d,34),('eJISB6',44),(_e,45),('eJapansePostcardSingle',71),('eIndexCard4x6',74),('eIndexCard5x8',75),('eIndexCard3x5',78),('eMonarch',80),(_w,81),(_f,89),(_x,90),(_y,91),('eInternationalC6',92),(_z,100),(_g,101),(_A0,110),('eJapanseEnvLong4',111),('ePhoto10x15',118),('ePhotoLSizeCard',121),('eIndexCard5x7',122),(_s,127),('eJapanseOufuku148x200',328),('eAnySize',32765)))
_Tray1_media_size_loaded_Type.__name__=_D
_Tray1_media_size_loaded_Object=MibScalar
tray1_media_size_loaded=_Tray1_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,1),_Tray1_media_size_loaded_Type())
tray1_media_size_loaded.setMaxAccess(_C)
if mibBuilder.loadTexts:tray1_media_size_loaded.setStatus(_E)
_Tray1_media_name_Type=OctetString
_Tray1_media_name_Object=MibScalar
tray1_media_name=_Tray1_media_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,4),_Tray1_media_name_Type())
tray1_media_name.setMaxAccess(_C)
if mibBuilder.loadTexts:tray1_media_name.setStatus(_E)
_Tray1_custom_media_width_Type=Integer32
_Tray1_custom_media_width_Object=MibScalar
tray1_custom_media_width=_Tray1_custom_media_width_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,10),_Tray1_custom_media_width_Type())
tray1_custom_media_width.setMaxAccess(_B)
if mibBuilder.loadTexts:tray1_custom_media_width.setStatus(_E)
_Tray1_custom_media_length_Type=Integer32
_Tray1_custom_media_length_Object=MibScalar
tray1_custom_media_length=_Tray1_custom_media_length_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,11),_Tray1_custom_media_length_Type())
tray1_custom_media_length.setMaxAccess(_B)
if mibBuilder.loadTexts:tray1_custom_media_length.setStatus(_E)
class _Tray1_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4)))
_Tray1_type_Type.__name__=_D
_Tray1_type_Object=MibScalar
tray1_type=_Tray1_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,17),_Tray1_type_Type())
tray1_type.setMaxAccess(_C)
if mibBuilder.loadTexts:tray1_type.setStatus(_E)
_Tray1_media_key_Type=OctetString
_Tray1_media_key_Object=MibScalar
tray1_media_key=_Tray1_media_key_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,1,20),_Tray1_media_key_Type())
tray1_media_key.setMaxAccess(_B)
if mibBuilder.loadTexts:tray1_media_key.setStatus(_E)
_Intray2_ObjectIdentity=ObjectIdentity
intray2=_Intray2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2))
class _Tray2_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,15,17,25,26,34,45,81,89,90,91,100,101,110)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,15),(_a,17),(_b,25),(_c,26),(_d,34),(_e,45),(_w,81),(_f,89),(_x,90),(_y,91),(_z,100),(_g,101),(_A0,110)))
_Tray2_media_size_loaded_Type.__name__=_D
_Tray2_media_size_loaded_Object=MibScalar
tray2_media_size_loaded=_Tray2_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,1),_Tray2_media_size_loaded_Type())
tray2_media_size_loaded.setMaxAccess(_C)
if mibBuilder.loadTexts:tray2_media_size_loaded.setStatus(_E)
_Tray2_media_name_Type=OctetString
_Tray2_media_name_Object=MibScalar
tray2_media_name=_Tray2_media_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,4),_Tray2_media_name_Type())
tray2_media_name.setMaxAccess(_C)
if mibBuilder.loadTexts:tray2_media_name.setStatus(_E)
_Tray2_custom_media_width_Type=Integer32
_Tray2_custom_media_width_Object=MibScalar
tray2_custom_media_width=_Tray2_custom_media_width_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,10),_Tray2_custom_media_width_Type())
tray2_custom_media_width.setMaxAccess(_B)
if mibBuilder.loadTexts:tray2_custom_media_width.setStatus(_E)
_Tray2_custom_media_length_Type=Integer32
_Tray2_custom_media_length_Object=MibScalar
tray2_custom_media_length=_Tray2_custom_media_length_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,11),_Tray2_custom_media_length_Type())
tray2_custom_media_length.setMaxAccess(_B)
if mibBuilder.loadTexts:tray2_custom_media_length.setStatus(_E)
class _Tray2_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4)))
_Tray2_type_Type.__name__=_D
_Tray2_type_Object=MibScalar
tray2_type=_Tray2_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,17),_Tray2_type_Type())
tray2_type.setMaxAccess(_C)
if mibBuilder.loadTexts:tray2_type.setStatus(_E)
_Tray2_media_key_Type=OctetString
_Tray2_media_key_Object=MibScalar
tray2_media_key=_Tray2_media_key_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,2,20),_Tray2_media_key_Type())
tray2_media_key.setMaxAccess(_B)
if mibBuilder.loadTexts:tray2_media_key.setStatus(_E)
_Intray3_ObjectIdentity=ObjectIdentity
intray3=_Intray3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3))
class _Tray3_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,15,17,25,26,34,45,89,101,127)));namedValues=NamedValues(*((_X,1),(_Y,2),(_q,3),(_r,10),(_Z,15),(_a,17),(_b,25),(_c,26),(_d,34),(_e,45),(_f,89),(_g,101),(_s,127)))
_Tray3_media_size_loaded_Type.__name__=_D
_Tray3_media_size_loaded_Object=MibScalar
tray3_media_size_loaded=_Tray3_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,1),_Tray3_media_size_loaded_Type())
tray3_media_size_loaded.setMaxAccess(_C)
if mibBuilder.loadTexts:tray3_media_size_loaded.setStatus(_E)
_Tray3_media_name_Type=OctetString
_Tray3_media_name_Object=MibScalar
tray3_media_name=_Tray3_media_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,4),_Tray3_media_name_Type())
tray3_media_name.setMaxAccess(_C)
if mibBuilder.loadTexts:tray3_media_name.setStatus(_E)
_Tray3_custom_media_width_Type=Integer32
_Tray3_custom_media_width_Object=MibScalar
tray3_custom_media_width=_Tray3_custom_media_width_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,10),_Tray3_custom_media_width_Type())
tray3_custom_media_width.setMaxAccess(_B)
if mibBuilder.loadTexts:tray3_custom_media_width.setStatus(_E)
_Tray3_custom_media_length_Type=Integer32
_Tray3_custom_media_length_Object=MibScalar
tray3_custom_media_length=_Tray3_custom_media_length_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,11),_Tray3_custom_media_length_Type())
tray3_custom_media_length.setMaxAccess(_B)
if mibBuilder.loadTexts:tray3_custom_media_length.setStatus(_E)
class _Tray3_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4)))
_Tray3_type_Type.__name__=_D
_Tray3_type_Object=MibScalar
tray3_type=_Tray3_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,17),_Tray3_type_Type())
tray3_type.setMaxAccess(_C)
if mibBuilder.loadTexts:tray3_type.setStatus(_E)
_Tray3_media_key_Type=OctetString
_Tray3_media_key_Object=MibScalar
tray3_media_key=_Tray3_media_key_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,3,20),_Tray3_media_key_Type())
tray3_media_key.setMaxAccess(_B)
if mibBuilder.loadTexts:tray3_media_key.setStatus(_E)
_Intray5_ObjectIdentity=ObjectIdentity
intray5=_Intray5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,5))
class _Tray5_media_size_loaded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,15,17,25,26,34,45,89,101,127)));namedValues=NamedValues(*((_X,1),(_Y,2),(_q,3),(_r,10),(_Z,15),(_a,17),(_b,25),(_c,26),(_d,34),(_e,45),(_f,89),(_g,101),(_s,127)))
_Tray5_media_size_loaded_Type.__name__=_D
_Tray5_media_size_loaded_Object=MibScalar
tray5_media_size_loaded=_Tray5_media_size_loaded_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,5,1),_Tray5_media_size_loaded_Type())
tray5_media_size_loaded.setMaxAccess(_C)
if mibBuilder.loadTexts:tray5_media_size_loaded.setStatus(_E)
_Tray5_media_name_Type=OctetString
_Tray5_media_name_Object=MibScalar
tray5_media_name=_Tray5_media_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,5,4),_Tray5_media_name_Type())
tray5_media_name.setMaxAccess(_C)
if mibBuilder.loadTexts:tray5_media_name.setStatus(_E)
_Tray5_custom_media_width_Type=Integer32
_Tray5_custom_media_width_Object=MibScalar
tray5_custom_media_width=_Tray5_custom_media_width_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,5,10),_Tray5_custom_media_width_Type())
tray5_custom_media_width.setMaxAccess(_B)
if mibBuilder.loadTexts:tray5_custom_media_width.setStatus(_E)
_Tray5_custom_media_length_Type=Integer32
_Tray5_custom_media_length_Object=MibScalar
tray5_custom_media_length=_Tray5_custom_media_length_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,5,11),_Tray5_custom_media_length_Type())
tray5_custom_media_length.setMaxAccess(_B)
if mibBuilder.loadTexts:tray5_custom_media_length.setStatus(_E)
class _Tray5_type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4)))
_Tray5_type_Type.__name__=_D
_Tray5_type_Object=MibScalar
tray5_type=_Tray5_type_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,5,17),_Tray5_type_Type())
tray5_type.setMaxAccess(_C)
if mibBuilder.loadTexts:tray5_type.setStatus(_E)
_Tray5_media_key_Type=OctetString
_Tray5_media_key_Object=MibScalar
tray5_media_key=_Tray5_media_key_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,3,3,5,20),_Tray5_media_key_Type())
tray5_media_key.setMaxAccess(_B)
if mibBuilder.loadTexts:tray5_media_key.setStatus(_E)
_Print_media_ObjectIdentity=ObjectIdentity
print_media=_Print_media_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8))
_Settings_print_media_ObjectIdentity=ObjectIdentity
settings_print_media=_Settings_print_media_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1))
_Media_names_enabled_Type=OctetString
_Media_names_enabled_Object=MibScalar
media_names_enabled=_Media_names_enabled_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,1,3),_Media_names_enabled_Type())
media_names_enabled.setMaxAccess(_C)
if mibBuilder.loadTexts:media_names_enabled.setStatus(_E)
_Media_info_ObjectIdentity=ObjectIdentity
media_info=_Media_info_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3))
_Media1_ObjectIdentity=ObjectIdentity
media1=_Media1_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1))
class _Media1_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media1_name_Type.__name__=_H
_Media1_name_Object=MibScalar
media1_name=_Media1_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,1,1),_Media1_name_Type())
media1_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media1_name.setStatus(_E)
_Media2_ObjectIdentity=ObjectIdentity
media2=_Media2_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2))
class _Media2_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media2_name_Type.__name__=_H
_Media2_name_Object=MibScalar
media2_name=_Media2_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,2,1),_Media2_name_Type())
media2_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media2_name.setStatus(_E)
_Media3_ObjectIdentity=ObjectIdentity
media3=_Media3_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3))
class _Media3_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media3_name_Type.__name__=_H
_Media3_name_Object=MibScalar
media3_name=_Media3_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,3,1),_Media3_name_Type())
media3_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media3_name.setStatus(_E)
_Media4_ObjectIdentity=ObjectIdentity
media4=_Media4_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4))
class _Media4_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media4_name_Type.__name__=_H
_Media4_name_Object=MibScalar
media4_name=_Media4_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,4,1),_Media4_name_Type())
media4_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media4_name.setStatus(_E)
_Media5_ObjectIdentity=ObjectIdentity
media5=_Media5_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5))
class _Media5_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media5_name_Type.__name__=_H
_Media5_name_Object=MibScalar
media5_name=_Media5_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,5,1),_Media5_name_Type())
media5_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media5_name.setStatus(_E)
_Media6_ObjectIdentity=ObjectIdentity
media6=_Media6_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6))
class _Media6_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media6_name_Type.__name__=_H
_Media6_name_Object=MibScalar
media6_name=_Media6_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,6,1),_Media6_name_Type())
media6_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media6_name.setStatus(_E)
_Media7_ObjectIdentity=ObjectIdentity
media7=_Media7_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7))
class _Media7_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media7_name_Type.__name__=_H
_Media7_name_Object=MibScalar
media7_name=_Media7_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,7,1),_Media7_name_Type())
media7_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media7_name.setStatus(_E)
_Media8_ObjectIdentity=ObjectIdentity
media8=_Media8_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8))
class _Media8_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media8_name_Type.__name__=_H
_Media8_name_Object=MibScalar
media8_name=_Media8_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,8,1),_Media8_name_Type())
media8_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media8_name.setStatus(_E)
_Media9_ObjectIdentity=ObjectIdentity
media9=_Media9_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9))
class _Media9_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media9_name_Type.__name__=_H
_Media9_name_Object=MibScalar
media9_name=_Media9_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,9,1),_Media9_name_Type())
media9_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media9_name.setStatus(_E)
_Media10_ObjectIdentity=ObjectIdentity
media10=_Media10_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10))
class _Media10_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media10_name_Type.__name__=_H
_Media10_name_Object=MibScalar
media10_name=_Media10_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,10,1),_Media10_name_Type())
media10_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media10_name.setStatus(_E)
_Media11_ObjectIdentity=ObjectIdentity
media11=_Media11_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11))
class _Media11_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media11_name_Type.__name__=_H
_Media11_name_Object=MibScalar
media11_name=_Media11_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,11,1),_Media11_name_Type())
media11_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media11_name.setStatus(_E)
_Media12_ObjectIdentity=ObjectIdentity
media12=_Media12_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12))
class _Media12_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media12_name_Type.__name__=_H
_Media12_name_Object=MibScalar
media12_name=_Media12_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,12,1),_Media12_name_Type())
media12_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media12_name.setStatus(_E)
_Media13_ObjectIdentity=ObjectIdentity
media13=_Media13_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13))
class _Media13_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media13_name_Type.__name__=_H
_Media13_name_Object=MibScalar
media13_name=_Media13_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,13,1),_Media13_name_Type())
media13_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media13_name.setStatus(_E)
_Media14_ObjectIdentity=ObjectIdentity
media14=_Media14_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14))
class _Media14_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media14_name_Type.__name__=_H
_Media14_name_Object=MibScalar
media14_name=_Media14_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,14,1),_Media14_name_Type())
media14_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media14_name.setStatus(_E)
_Media15_ObjectIdentity=ObjectIdentity
media15=_Media15_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15))
class _Media15_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media15_name_Type.__name__=_H
_Media15_name_Object=MibScalar
media15_name=_Media15_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,15,1),_Media15_name_Type())
media15_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media15_name.setStatus(_E)
_Media16_ObjectIdentity=ObjectIdentity
media16=_Media16_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,16))
class _Media16_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media16_name_Type.__name__=_H
_Media16_name_Object=MibScalar
media16_name=_Media16_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,16,1),_Media16_name_Type())
media16_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media16_name.setStatus(_E)
_Media17_ObjectIdentity=ObjectIdentity
media17=_Media17_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,17))
class _Media17_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media17_name_Type.__name__=_H
_Media17_name_Object=MibScalar
media17_name=_Media17_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,17,1),_Media17_name_Type())
media17_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media17_name.setStatus(_E)
_Media18_ObjectIdentity=ObjectIdentity
media18=_Media18_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,18))
class _Media18_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media18_name_Type.__name__=_H
_Media18_name_Object=MibScalar
media18_name=_Media18_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,18,1),_Media18_name_Type())
media18_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media18_name.setStatus(_E)
_Media19_ObjectIdentity=ObjectIdentity
media19=_Media19_ObjectIdentity((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,19))
class _Media19_name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_Media19_name_Type.__name__=_H
_Media19_name_Object=MibScalar
media19_name=_Media19_name_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,8,3,19,1),_Media19_name_Type())
media19_name.setMaxAccess(_C)
if mibBuilder.loadTexts:media19_name.setStatus(_E)
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
consumable_status_cartridge_model.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_status_cartridge_model.setStatus(_E)
class _Consumable_status_manufacturing_date_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Consumable_status_manufacturing_date_Type.__name__=_H
_Consumable_status_manufacturing_date_Object=MibScalar
consumable_status_manufacturing_date=_Consumable_status_manufacturing_date_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1,2),_Consumable_status_manufacturing_date_Type())
consumable_status_manufacturing_date.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_status_manufacturing_date.setStatus(_E)
class _Consumable_status_serial_number_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Consumable_status_serial_number_Type.__name__=_H
_Consumable_status_serial_number_Object=MibScalar
consumable_status_serial_number=_Consumable_status_serial_number_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1,3),_Consumable_status_serial_number_Type())
consumable_status_serial_number.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_status_serial_number.setStatus(_E)
class _Consumable_status_first_install_date_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Consumable_status_first_install_date_Type.__name__=_H
_Consumable_status_first_install_date_Object=MibScalar
consumable_status_first_install_date=_Consumable_status_first_install_date_Object((1,3,6,1,4,1,11,2,3,9,4,2,1,4,1,10,1,1,8),_Consumable_status_first_install_date_Type())
consumable_status_first_install_date.setMaxAccess(_B)
if mibBuilder.loadTexts:consumable_status_first_install_date.setStatus(_E)
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
npSysModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:npSysModelNumber.setStatus(_A)
_NpSysCardServices1_Type=Integer32
_NpSysCardServices1_Object=MibScalar
npSysCardServices1=_NpSysCardServices1_Object((1,3,6,1,4,1,11,2,4,3,1,16),_NpSysCardServices1_Type())
npSysCardServices1.setMaxAccess(_B)
if mibBuilder.loadTexts:npSysCardServices1.setStatus(_A)
_NpSysCardServices2_Type=Integer32
_NpSysCardServices2_Object=MibScalar
npSysCardServices2=_NpSysCardServices2_Object((1,3,6,1,4,1,11,2,4,3,1,17),_NpSysCardServices2_Type())
npSysCardServices2.setMaxAccess(_B)
if mibBuilder.loadTexts:npSysCardServices2.setStatus(_A)
_NpSysCardServices3_Type=Integer32
_NpSysCardServices3_Object=MibScalar
npSysCardServices3=_NpSysCardServices3_Object((1,3,6,1,4,1,11,2,4,3,1,22),_NpSysCardServices3_Type())
npSysCardServices3.setMaxAccess(_B)
if mibBuilder.loadTexts:npSysCardServices3.setStatus(_A)
_NpCfg_ObjectIdentity=ObjectIdentity
npCfg=_NpCfg_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,5))
class _NpCfgSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('manual-one',1),('bootp-two',2),('manual-three',3),('bootp-four',4),('dhcp',5),('not-configured',6),('default-config',7),('rarp',8),(_B,9),('auto-ip',10)))
_NpCfgSource_Type.__name__=_D
_NpCfgSource_Object=MibScalar
npCfgSource=_NpCfgSource_Object((1,3,6,1,4,1,11,2,4,3,5,1),_NpCfgSource_Type())
npCfgSource.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSource.setStatus(_A)
_NpCfgYiaddr_Type=IpAddress
_NpCfgYiaddr_Object=MibScalar
npCfgYiaddr=_NpCfgYiaddr_Object((1,3,6,1,4,1,11,2,4,3,5,2),_NpCfgYiaddr_Type())
npCfgYiaddr.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgYiaddr.setStatus(_A)
_NpCfgSiaddr_Type=IpAddress
_NpCfgSiaddr_Object=MibScalar
npCfgSiaddr=_NpCfgSiaddr_Object((1,3,6,1,4,1,11,2,4,3,5,3),_NpCfgSiaddr_Type())
npCfgSiaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:npCfgSiaddr.setStatus(_A)
_NpCfgLogServer_Type=IpAddress
_NpCfgLogServer_Object=MibScalar
npCfgLogServer=_NpCfgLogServer_Object((1,3,6,1,4,1,11,2,4,3,5,5),_NpCfgLogServer_Type())
npCfgLogServer.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgLogServer.setStatus(_A)
_NpCfgSubnetMask_Type=IpAddress
_NpCfgSubnetMask_Object=MibScalar
npCfgSubnetMask=_NpCfgSubnetMask_Object((1,3,6,1,4,1,11,2,4,3,5,12),_NpCfgSubnetMask_Type())
npCfgSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSubnetMask.setStatus(_A)
_NpCfgDefaultGateway_Type=IpAddress
_NpCfgDefaultGateway_Object=MibScalar
npCfgDefaultGateway=_NpCfgDefaultGateway_Object((1,3,6,1,4,1,11,2,4,3,5,13),_NpCfgDefaultGateway_Type())
npCfgDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgDefaultGateway.setStatus(_A)
class _NpCfgDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NpCfgDomainName_Type.__name__=_G
_NpCfgDomainName_Object=MibScalar
npCfgDomainName=_NpCfgDomainName_Object((1,3,6,1,4,1,11,2,4,3,5,16),_NpCfgDomainName_Type())
npCfgDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgDomainName.setStatus(_A)
_NpCfgIPP_Type=Integer32
_NpCfgIPP_Object=MibScalar
npCfgIPP=_NpCfgIPP_Object((1,3,6,1,4,1,11,2,4,3,5,18),_NpCfgIPP_Type())
npCfgIPP.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgIPP.setStatus(_A)
_NpCfgDNSNameServerId_Type=IpAddress
_NpCfgDNSNameServerId_Object=MibScalar
npCfgDNSNameServerId=_NpCfgDNSNameServerId_Object((1,3,6,1,4,1,11,2,4,3,5,21),_NpCfgDNSNameServerId_Type())
npCfgDNSNameServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgDNSNameServerId.setStatus(_A)
_NpCfgWINSNameServerIdPri_Type=IpAddress
_NpCfgWINSNameServerIdPri_Object=MibScalar
npCfgWINSNameServerIdPri=_NpCfgWINSNameServerIdPri_Object((1,3,6,1,4,1,11,2,4,3,5,22),_NpCfgWINSNameServerIdPri_Type())
npCfgWINSNameServerIdPri.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgWINSNameServerIdPri.setStatus(_A)
_NpCfgWINSNameServerIdSec_Type=IpAddress
_NpCfgWINSNameServerIdSec_Object=MibScalar
npCfgWINSNameServerIdSec=_NpCfgWINSNameServerIdSec_Object((1,3,6,1,4,1,11,2,4,3,5,23),_NpCfgWINSNameServerIdSec_Type())
npCfgWINSNameServerIdSec.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgWINSNameServerIdSec.setStatus(_A)
_NpCfgPasswd1_Type=DisplayString
_NpCfgPasswd1_Object=MibScalar
npCfgPasswd1=_NpCfgPasswd1_Object((1,3,6,1,4,1,11,2,4,3,5,29),_NpCfgPasswd1_Type())
npCfgPasswd1.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgPasswd1.setStatus(_A)
class _NpCfgLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('autoNegotiate',1),('full10T',2),('half10T',3),('full100T',4),('half100T',5),('auto100T',6),('full1000T',7)))
_NpCfgLinkType_Type.__name__=_D
_NpCfgLinkType_Object=MibScalar
npCfgLinkType=_NpCfgLinkType_Object((1,3,6,1,4,1,11,2,4,3,5,35),_NpCfgLinkType_Type())
npCfgLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgLinkType.setStatus(_A)
class _NpCfgSnmpDefaultReadCmnty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCfgSnmpDefaultReadCmnty_Type.__name__=_D
_NpCfgSnmpDefaultReadCmnty_Object=MibScalar
npCfgSnmpDefaultReadCmnty=_NpCfgSnmpDefaultReadCmnty_Object((1,3,6,1,4,1,11,2,4,3,5,40),_NpCfgSnmpDefaultReadCmnty_Type())
npCfgSnmpDefaultReadCmnty.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSnmpDefaultReadCmnty.setStatus(_A)
class _NpCfgBonjourServiceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_NpCfgBonjourServiceName_Type.__name__=_G
_NpCfgBonjourServiceName_Object=MibScalar
npCfgBonjourServiceName=_NpCfgBonjourServiceName_Object((1,3,6,1,4,1,11,2,4,3,5,44),_NpCfgBonjourServiceName_Type())
npCfgBonjourServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgBonjourServiceName.setStatus(_A)
class _NpCfgBonjourHighestPriorityService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,16)));namedValues=NamedValues(*(('p9100-Printing',1),('IPP-Printing',2),('lPD-Printing-RAW',3),('lPD-Printing-TEXT',4),('lPD-Printing-AUTO',5),('lPD-Printing-BINPS',6),('lPD-Printing-Queue5',7),('lPD-Printing-Queue6',8),('lPD-Printing-Queue7',9),('lPD-Printing-Queue8',10),('lPD-Printing-Queue9',11),('lPD-Printing-Queue10',12),('IPPS-Printing',16)))
_NpCfgBonjourHighestPriorityService_Type.__name__=_D
_NpCfgBonjourHighestPriorityService_Object=MibScalar
npCfgBonjourHighestPriorityService=_NpCfgBonjourHighestPriorityService_Object((1,3,6,1,4,1,11,2,4,3,5,45),_NpCfgBonjourHighestPriorityService_Type())
npCfgBonjourHighestPriorityService.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgBonjourHighestPriorityService.setStatus(_A)
class _NpCfgBonjourDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NpCfgBonjourDomainName_Type.__name__=_G
_NpCfgBonjourDomainName_Object=MibScalar
npCfgBonjourDomainName=_NpCfgBonjourDomainName_Object((1,3,6,1,4,1,11,2,4,3,5,46),_NpCfgBonjourDomainName_Type())
npCfgBonjourDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:npCfgBonjourDomainName.setStatus(_A)
_NpCfgDNSNameServerIdSecondary_Type=IpAddress
_NpCfgDNSNameServerIdSecondary_Object=MibScalar
npCfgDNSNameServerIdSecondary=_NpCfgDNSNameServerIdSecondary_Object((1,3,6,1,4,1,11,2,4,3,5,47),_NpCfgDNSNameServerIdSecondary_Type())
npCfgDNSNameServerIdSecondary.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgDNSNameServerIdSecondary.setStatus(_A)
class _NpCfgIPv6ConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ipv6-going-down',0),('ipv6-is-up',1)))
_NpCfgIPv6ConfigState_Type.__name__=_D
_NpCfgIPv6ConfigState_Object=MibScalar
npCfgIPv6ConfigState=_NpCfgIPv6ConfigState_Object((1,3,6,1,4,1,11,2,4,3,5,50),_NpCfgIPv6ConfigState_Type())
npCfgIPv6ConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:npCfgIPv6ConfigState.setStatus(_A)
_NpCfgIPv6DNSAddr1_Type=InetAddress
_NpCfgIPv6DNSAddr1_Object=MibScalar
npCfgIPv6DNSAddr1=_NpCfgIPv6DNSAddr1_Object((1,3,6,1,4,1,11,2,4,3,5,56),_NpCfgIPv6DNSAddr1_Type())
npCfgIPv6DNSAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgIPv6DNSAddr1.setStatus(_A)
_NpCfgIPv6DNSAddr2_Type=InetAddress
_NpCfgIPv6DNSAddr2_Object=MibScalar
npCfgIPv6DNSAddr2=_NpCfgIPv6DNSAddr2_Object((1,3,6,1,4,1,11,2,4,3,5,57),_NpCfgIPv6DNSAddr2_Type())
npCfgIPv6DNSAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgIPv6DNSAddr2.setStatus(_A)
_NpCfgIPConfigPrecedence_Type=OctetString
_NpCfgIPConfigPrecedence_Object=MibScalar
npCfgIPConfigPrecedence=_NpCfgIPConfigPrecedence_Object((1,3,6,1,4,1,11,2,4,3,5,59),_NpCfgIPConfigPrecedence_Type())
npCfgIPConfigPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgIPConfigPrecedence.setStatus(_A)
class _NpCfgSTAWirelessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bg-Mode',0),('bgn-Mode',1)))
_NpCfgSTAWirelessMode_Type.__name__=_D
_NpCfgSTAWirelessMode_Object=MibScalar
npCfgSTAWirelessMode=_NpCfgSTAWirelessMode_Object((1,3,6,1,4,1,11,2,4,3,5,72),_NpCfgSTAWirelessMode_Type())
npCfgSTAWirelessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSTAWirelessMode.setStatus(_A)
class _NpCfgWiFiDirectChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,13))
_NpCfgWiFiDirectChannelNumber_Type.__name__=_D
_NpCfgWiFiDirectChannelNumber_Object=MibScalar
npCfgWiFiDirectChannelNumber=_NpCfgWiFiDirectChannelNumber_Object((1,3,6,1,4,1,11,2,4,3,5,85),_NpCfgWiFiDirectChannelNumber_Type())
npCfgWiFiDirectChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgWiFiDirectChannelNumber.setStatus(_A)
class _NpCfgWiFiDirectSSIDPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,13))
_NpCfgWiFiDirectSSIDPrefix_Type.__name__=_G
_NpCfgWiFiDirectSSIDPrefix_Object=MibScalar
npCfgWiFiDirectSSIDPrefix=_NpCfgWiFiDirectSSIDPrefix_Object((1,3,6,1,4,1,11,2,4,3,5,86),_NpCfgWiFiDirectSSIDPrefix_Type())
npCfgWiFiDirectSSIDPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:npCfgWiFiDirectSSIDPrefix.setStatus(_A)
class _NpCfgWiFiDirectSSIDSuffix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_NpCfgWiFiDirectSSIDSuffix_Type.__name__=_G
_NpCfgWiFiDirectSSIDSuffix_Object=MibScalar
npCfgWiFiDirectSSIDSuffix=_NpCfgWiFiDirectSSIDSuffix_Object((1,3,6,1,4,1,11,2,4,3,5,87),_NpCfgWiFiDirectSSIDSuffix_Type())
npCfgWiFiDirectSSIDSuffix.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgWiFiDirectSSIDSuffix.setStatus(_A)
class _NpCfgWiFiDirectConnectionSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('Automatic',0),('Manual',1),('Advanced',2)))
_NpCfgWiFiDirectConnectionSecurity_Type.__name__=_D
_NpCfgWiFiDirectConnectionSecurity_Object=MibScalar
npCfgWiFiDirectConnectionSecurity=_NpCfgWiFiDirectConnectionSecurity_Object((1,3,6,1,4,1,11,2,4,3,5,88),_NpCfgWiFiDirectConnectionSecurity_Type())
npCfgWiFiDirectConnectionSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgWiFiDirectConnectionSecurity.setStatus(_E)
class _NpCfgSysLogProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17)));namedValues=NamedValues(*(('tcp',6),('udp',17)))
_NpCfgSysLogProtocol_Type.__name__=_D
_NpCfgSysLogProtocol_Object=MibScalar
npCfgSysLogProtocol=_NpCfgSysLogProtocol_Object((1,3,6,1,4,1,11,2,4,3,5,97),_NpCfgSysLogProtocol_Type())
npCfgSysLogProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSysLogProtocol.setStatus(_A)
class _NpCfgSysLogPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NpCfgSysLogPort_Type.__name__=_D
_NpCfgSysLogPort_Object=MibScalar
npCfgSysLogPort=_NpCfgSysLogPort_Object((1,3,6,1,4,1,11,2,4,3,5,98),_NpCfgSysLogPort_Type())
npCfgSysLogPort.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgSysLogPort.setStatus(_A)
_NpCfgHpDAPAgentManualServerAddr_Type=InetAddress
_NpCfgHpDAPAgentManualServerAddr_Object=MibScalar
npCfgHpDAPAgentManualServerAddr=_NpCfgHpDAPAgentManualServerAddr_Object((1,3,6,1,4,1,11,2,4,3,5,99),_NpCfgHpDAPAgentManualServerAddr_Type())
npCfgHpDAPAgentManualServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:npCfgHpDAPAgentManualServerAddr.setStatus(_A)
_NpTcp_ObjectIdentity=ObjectIdentity
npTcp=_NpTcp_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,6))
class _NpTcpSyslogMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_NpTcpSyslogMax_Type.__name__=_D
_NpTcpSyslogMax_Object=MibScalar
npTcpSyslogMax=_NpTcpSyslogMax_Object((1,3,6,1,4,1,11,2,4,3,6,11),_NpTcpSyslogMax_Type())
npTcpSyslogMax.setMaxAccess(_C)
if mibBuilder.loadTexts:npTcpSyslogMax.setStatus(_A)
class _NpTcpAppSyslogPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_NpTcpAppSyslogPriority_Type.__name__=_D
_NpTcpAppSyslogPriority_Object=MibScalar
npTcpAppSyslogPriority=_NpTcpAppSyslogPriority_Object((1,3,6,1,4,1,11,2,4,3,6,12),_NpTcpAppSyslogPriority_Type())
npTcpAppSyslogPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:npTcpAppSyslogPriority.setStatus(_A)
_NpCtl_ObjectIdentity=ObjectIdentity
npCtl=_NpCtl_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,7))
class _NpCtlSLP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCtlSLP_Type.__name__=_D
_NpCtlSLP_Object=MibScalar
npCtlSLP=_NpCtlSLP_Object((1,3,6,1,4,1,11,2,4,3,7,21),_NpCtlSLP_Type())
npCtlSLP.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlSLP.setStatus(_A)
class _NpCtlLPD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCtlLPD_Type.__name__=_D
_NpCtlLPD_Object=MibScalar
npCtlLPD=_NpCtlLPD_Object((1,3,6,1,4,1,11,2,4,3,7,22),_NpCtlLPD_Type())
npCtlLPD.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlLPD.setStatus(_A)
class _NpCtl9100_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCtl9100_Type.__name__=_D
_NpCtl9100_Object=MibScalar
npCtl9100=_NpCtl9100_Object((1,3,6,1,4,1,11,2,4,3,7,24),_NpCtl9100_Type())
npCtl9100.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtl9100.setStatus(_A)
class _NpCtlSysLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCtlSysLog_Type.__name__=_D
_NpCtlSysLog_Object=MibScalar
npCtlSysLog=_NpCtlSysLog_Object((1,3,6,1,4,1,11,2,4,3,7,26),_NpCtlSysLog_Type())
npCtlSysLog.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlSysLog.setStatus(_A)
class _NpCtlSnmpVersionAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('snmpV1RW-snmpV3RW',1),('snmpV1RO-snmpV3RW',2),('snmpV1NoAccess-snmpV3RW',3),('snmpV1RW-snmpV3NoAccess',4),('snmpV1RO-snmpV3NoAccess',5)))
_NpCtlSnmpVersionAccess_Type.__name__=_D
_NpCtlSnmpVersionAccess_Object=MibScalar
npCtlSnmpVersionAccess=_NpCtlSnmpVersionAccess_Object((1,3,6,1,4,1,11,2,4,3,7,27),_NpCtlSnmpVersionAccess_Type())
npCtlSnmpVersionAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlSnmpVersionAccess.setStatus(_A)
class _NpCtlSnmpV3InitAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4)));namedValues=NamedValues(*(('Destroy',0),('blockInitEncrypt',4)))
_NpCtlSnmpV3InitAccount_Type.__name__=_D
_NpCtlSnmpV3InitAccount_Object=MibScalar
npCtlSnmpV3InitAccount=_NpCtlSnmpV3InitAccount_Object((1,3,6,1,4,1,11,2,4,3,7,28),_NpCtlSnmpV3InitAccount_Type())
npCtlSnmpV3InitAccount.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlSnmpV3InitAccount.setStatus(_A)
class _NpCtlBonjour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_NpCtlBonjour_Type.__name__=_D
_NpCtlBonjour_Object=MibScalar
npCtlBonjour=_NpCtlBonjour_Object((1,3,6,1,4,1,11,2,4,3,7,29),_NpCtlBonjour_Type())
npCtlBonjour.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlBonjour.setStatus(_A)
class _NpCtlNetworkConnectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto-cable-detect',1),('disable-radio',2),('disable-wired',3)))
_NpCtlNetworkConnectionMode_Type.__name__=_D
_NpCtlNetworkConnectionMode_Object=MibScalar
npCtlNetworkConnectionMode=_NpCtlNetworkConnectionMode_Object((1,3,6,1,4,1,11,2,4,3,7,32),_NpCtlNetworkConnectionMode_Type())
npCtlNetworkConnectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlNetworkConnectionMode.setStatus(_A)
class _NpCtlWSDiscovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_R,1)))
_NpCtlWSDiscovery_Type.__name__=_D
_NpCtlWSDiscovery_Object=MibScalar
npCtlWSDiscovery=_NpCtlWSDiscovery_Object((1,3,6,1,4,1,11,2,4,3,7,36),_NpCtlWSDiscovery_Type())
npCtlWSDiscovery.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWSDiscovery.setStatus(_A)
class _NpCtlWSPrint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_R,1)))
_NpCtlWSPrint_Type.__name__=_D
_NpCtlWSPrint_Object=MibScalar
npCtlWSPrint=_NpCtlWSPrint_Object((1,3,6,1,4,1,11,2,4,3,7,37),_NpCtlWSPrint_Type())
npCtlWSPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWSPrint.setStatus(_A)
class _NpCtlLLMNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_R,1)))
_NpCtlLLMNR_Type.__name__=_D
_NpCtlLLMNR_Object=MibScalar
npCtlLLMNR=_NpCtlLLMNR_Object((1,3,6,1,4,1,11,2,4,3,7,38),_NpCtlLLMNR_Type())
npCtlLLMNR.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlLLMNR.setStatus(_A)
class _NpCtlWPAD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),('automatic-Web-Proxy',1),('manual-url',2),('manual-proxy-settings',3)))
_NpCtlWPAD_Type.__name__=_D
_NpCtlWPAD_Object=MibScalar
npCtlWPAD=_NpCtlWPAD_Object((1,3,6,1,4,1,11,2,4,3,7,39),_NpCtlWPAD_Type())
npCtlWPAD.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWPAD.setStatus(_A)
class _NpCtlFpDot11WirelessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_NpCtlFpDot11WirelessState_Type.__name__=_D
_NpCtlFpDot11WirelessState_Object=MibScalar
npCtlFpDot11WirelessState=_NpCtlFpDot11WirelessState_Object((1,3,6,1,4,1,11,2,4,3,7,47),_NpCtlFpDot11WirelessState_Type())
npCtlFpDot11WirelessState.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlFpDot11WirelessState.setStatus(_A)
class _NpCtlDot11nSTAGuardInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('Auto',0),('Short',1),('Long',2)))
_NpCtlDot11nSTAGuardInterval_Type.__name__=_D
_NpCtlDot11nSTAGuardInterval_Object=MibScalar
npCtlDot11nSTAGuardInterval=_NpCtlDot11nSTAGuardInterval_Object((1,3,6,1,4,1,11,2,4,3,7,51),_NpCtlDot11nSTAGuardInterval_Type())
npCtlDot11nSTAGuardInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlDot11nSTAGuardInterval.setStatus(_A)
class _NpCtlDot11nSTAAMSDUAggregation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_NpCtlDot11nSTAAMSDUAggregation_Type.__name__=_D
_NpCtlDot11nSTAAMSDUAggregation_Object=MibScalar
npCtlDot11nSTAAMSDUAggregation=_NpCtlDot11nSTAAMSDUAggregation_Object((1,3,6,1,4,1,11,2,4,3,7,52),_NpCtlDot11nSTAAMSDUAggregation_Type())
npCtlDot11nSTAAMSDUAggregation.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlDot11nSTAAMSDUAggregation.setStatus(_A)
class _NpCtlDot11nSTABlockACKs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_NpCtlDot11nSTABlockACKs_Type.__name__=_D
_NpCtlDot11nSTABlockACKs_Object=MibScalar
npCtlDot11nSTABlockACKs=_NpCtlDot11nSTABlockACKs_Object((1,3,6,1,4,1,11,2,4,3,7,53),_NpCtlDot11nSTABlockACKs_Type())
npCtlDot11nSTABlockACKs.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlDot11nSTABlockACKs.setStatus(_A)
class _NpCtlDot11nSTAAMPDUAggregation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_NpCtlDot11nSTAAMPDUAggregation_Type.__name__=_D
_NpCtlDot11nSTAAMPDUAggregation_Object=MibScalar
npCtlDot11nSTAAMPDUAggregation=_NpCtlDot11nSTAAMPDUAggregation_Object((1,3,6,1,4,1,11,2,4,3,7,54),_NpCtlDot11nSTAAMPDUAggregation_Type())
npCtlDot11nSTAAMPDUAggregation.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlDot11nSTAAMPDUAggregation.setStatus(_A)
class _NpCtlWiFiDirectSSIDBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-allowed',0),('allowed',1)))
_NpCtlWiFiDirectSSIDBroadcast_Type.__name__=_D
_NpCtlWiFiDirectSSIDBroadcast_Object=MibScalar
npCtlWiFiDirectSSIDBroadcast=_NpCtlWiFiDirectSSIDBroadcast_Object((1,3,6,1,4,1,11,2,4,3,7,57),_NpCtlWiFiDirectSSIDBroadcast_Type())
npCtlWiFiDirectSSIDBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWiFiDirectSSIDBroadcast.setStatus(_A)
class _NpCtlWiFiDirectHidePassphrase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('show',0),('hide',1)))
_NpCtlWiFiDirectHidePassphrase_Type.__name__=_D
_NpCtlWiFiDirectHidePassphrase_Object=MibScalar
npCtlWiFiDirectHidePassphrase=_NpCtlWiFiDirectHidePassphrase_Object((1,3,6,1,4,1,11,2,4,3,7,58),_NpCtlWiFiDirectHidePassphrase_Type())
npCtlWiFiDirectHidePassphrase.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWiFiDirectHidePassphrase.setStatus(_E)
class _NpCtlWiFiDirectHideSsid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('show',0),('hide',1)))
_NpCtlWiFiDirectHideSsid_Type.__name__=_D
_NpCtlWiFiDirectHideSsid_Object=MibScalar
npCtlWiFiDirectHideSsid=_NpCtlWiFiDirectHideSsid_Object((1,3,6,1,4,1,11,2,4,3,7,59),_NpCtlWiFiDirectHideSsid_Type())
npCtlWiFiDirectHideSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWiFiDirectHideSsid.setStatus(_E)
class _NpCtlHpDAPAgentAnnounceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_NpCtlHpDAPAgentAnnounceState_Type.__name__=_D
_NpCtlHpDAPAgentAnnounceState_Object=MibScalar
npCtlHpDAPAgentAnnounceState=_NpCtlHpDAPAgentAnnounceState_Object((1,3,6,1,4,1,11,2,4,3,7,65),_NpCtlHpDAPAgentAnnounceState_Type())
npCtlHpDAPAgentAnnounceState.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlHpDAPAgentAnnounceState.setStatus(_A)
class _NpCtlHpDAPAgentRequireTrustedAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_NpCtlHpDAPAgentRequireTrustedAuth_Type.__name__=_D
_NpCtlHpDAPAgentRequireTrustedAuth_Object=MibScalar
npCtlHpDAPAgentRequireTrustedAuth=_NpCtlHpDAPAgentRequireTrustedAuth_Object((1,3,6,1,4,1,11,2,4,3,7,66),_NpCtlHpDAPAgentRequireTrustedAuth_Type())
npCtlHpDAPAgentRequireTrustedAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlHpDAPAgentRequireTrustedAuth.setStatus(_A)
class _NpCtlDeviceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('WiredStationMode',1),('WirelessStationMode',2),('AccessPointMode',3)))
_NpCtlDeviceMode_Type.__name__=_D
_NpCtlDeviceMode_Object=MibScalar
npCtlDeviceMode=_NpCtlDeviceMode_Object((1,3,6,1,4,1,11,2,4,3,7,67),_NpCtlDeviceMode_Type())
npCtlDeviceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:npCtlDeviceMode.setStatus(_A)
class _NpCtlAirPrintStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_NpCtlAirPrintStatus_Type.__name__=_D
_NpCtlAirPrintStatus_Object=MibScalar
npCtlAirPrintStatus=_NpCtlAirPrintStatus_Object((1,3,6,1,4,1,11,2,4,3,7,68),_NpCtlAirPrintStatus_Type())
npCtlAirPrintStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlAirPrintStatus.setStatus(_A)
class _NpCtlWirelessSTAState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_o,1)))
_NpCtlWirelessSTAState_Type.__name__=_D
_NpCtlWirelessSTAState_Object=MibScalar
npCtlWirelessSTAState=_NpCtlWirelessSTAState_Object((1,3,6,1,4,1,11,2,4,3,7,73),_NpCtlWirelessSTAState_Type())
npCtlWirelessSTAState.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWirelessSTAState.setStatus(_A)
class _NpCtlWiFiDirectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_p,0),(_o,1)))
_NpCtlWiFiDirectState_Type.__name__=_D
_NpCtlWiFiDirectState_Object=MibScalar
npCtlWiFiDirectState=_NpCtlWiFiDirectState_Object((1,3,6,1,4,1,11,2,4,3,7,74),_NpCtlWiFiDirectState_Type())
npCtlWiFiDirectState.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlWiFiDirectState.setStatus(_A)
_NpCtlAirScan_Type=Integer32
_NpCtlAirScan_Object=MibScalar
npCtlAirScan=_NpCtlAirScan_Object((1,3,6,1,4,1,11,2,4,3,7,79),_NpCtlAirScan_Type())
npCtlAirScan.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlAirScan.setStatus(_E)
class _NpCtlAirFax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_R,1)))
_NpCtlAirFax_Type.__name__=_D
_NpCtlAirFax_Object=MibScalar
npCtlAirFax=_NpCtlAirFax_Object((1,3,6,1,4,1,11,2,4,3,7,80),_NpCtlAirFax_Type())
npCtlAirFax.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlAirFax.setStatus(_E)
class _NpCtlGCPrint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_R,1),('remove',2)))
_NpCtlGCPrint_Type.__name__=_D
_NpCtlGCPrint_Object=MibScalar
npCtlGCPrint=_NpCtlGCPrint_Object((1,3,6,1,4,1,11,2,4,3,7,81),_NpCtlGCPrint_Type())
npCtlGCPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlGCPrint.setStatus(_E)
class _NpCtlRebootMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('recovery',1)))
_NpCtlRebootMode_Type.__name__=_D
_NpCtlRebootMode_Object=MibScalar
npCtlRebootMode=_NpCtlRebootMode_Object((1,3,6,1,4,1,11,2,4,3,7,83),_NpCtlRebootMode_Type())
npCtlRebootMode.setMaxAccess(_C)
if mibBuilder.loadTexts:npCtlRebootMode.setStatus(_E)
_NpNpi_ObjectIdentity=ObjectIdentity
npNpi=_NpNpi_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,8))
_NpNpiPeripheralAttributeEntry_ObjectIdentity=ObjectIdentity
npNpiPeripheralAttributeEntry=_NpNpiPeripheralAttributeEntry_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,8,3))
class _NpNpiPaeClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('printer',1),('plotter',2),('xStation',3)))
_NpNpiPaeClass_Type.__name__=_D
_NpNpiPaeClass_Object=MibScalar
npNpiPaeClass=_NpNpiPaeClass_Object((1,3,6,1,4,1,11,2,4,3,8,3,2),_NpNpiPaeClass_Type())
npNpiPaeClass.setMaxAccess(_B)
if mibBuilder.loadTexts:npNpiPaeClass.setStatus(_A)
class _NpNpiPaeIdentification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*(('laserjet-IIISI',1),('laserjet-4SI',5)))
_NpNpiPaeIdentification_Type.__name__=_D
_NpNpiPaeIdentification_Object=MibScalar
npNpiPaeIdentification=_NpNpiPaeIdentification_Object((1,3,6,1,4,1,11,2,4,3,8,3,3),_NpNpiPaeIdentification_Type())
npNpiPaeIdentification.setMaxAccess(_B)
if mibBuilder.loadTexts:npNpiPaeIdentification.setStatus(_A)
_NpIpx_ObjectIdentity=ObjectIdentity
npIpx=_NpIpx_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,10))
_NpIpxSapInfo_Type=OctetString
_NpIpxSapInfo_Object=MibScalar
npIpxSapInfo=_NpIpxSapInfo_Object((1,3,6,1,4,1,11,2,4,3,10,6),_NpIpxSapInfo_Type())
npIpxSapInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:npIpxSapInfo.setStatus(_A)
_NpPort_ObjectIdentity=ObjectIdentity
npPort=_NpPort_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,13))
class _NpPortNumPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NpPortNumPorts_Type.__name__=_D
_NpPortNumPorts_Object=MibScalar
npPortNumPorts=_NpPortNumPorts_Object((1,3,6,1,4,1,11,2,4,3,13,1),_NpPortNumPorts_Type())
npPortNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:npPortNumPorts.setStatus(_A)
_NpDhcp_ObjectIdentity=ObjectIdentity
npDhcp=_NpDhcp_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,16))
class _NpDhcpFQDNBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('Present-JD-Behavior',0),('RFC4702-compliant-Behavior',1)))
_NpDhcpFQDNBehavior_Type.__name__=_D
_NpDhcpFQDNBehavior_Object=MibScalar
npDhcpFQDNBehavior=_NpDhcpFQDNBehavior_Object((1,3,6,1,4,1,11,2,4,3,16,4),_NpDhcpFQDNBehavior_Type())
npDhcpFQDNBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:npDhcpFQDNBehavior.setStatus(_A)
_NpWeb_ObjectIdentity=ObjectIdentity
npWeb=_NpWeb_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,18))
class _NpWebProxyServerId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NpWebProxyServerId_Type.__name__=_G
_NpWebProxyServerId_Object=MibScalar
npWebProxyServerId=_NpWebProxyServerId_Object((1,3,6,1,4,1,11,2,4,3,18,12),_NpWebProxyServerId_Type())
npWebProxyServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:npWebProxyServerId.setStatus(_A)
_NpWebProxyServerPort_Type=Integer32
_NpWebProxyServerPort_Object=MibScalar
npWebProxyServerPort=_NpWebProxyServerPort_Object((1,3,6,1,4,1,11,2,4,3,18,13),_NpWebProxyServerPort_Type())
npWebProxyServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:npWebProxyServerPort.setStatus(_A)
class _NpWebProxyUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NpWebProxyUserName_Type.__name__=_G
_NpWebProxyUserName_Object=MibScalar
npWebProxyUserName=_NpWebProxyUserName_Object((1,3,6,1,4,1,11,2,4,3,18,14),_NpWebProxyUserName_Type())
npWebProxyUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:npWebProxyUserName.setStatus(_A)
class _NpWebProxyUserPasswd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NpWebProxyUserPasswd_Type.__name__=_G
_NpWebProxyUserPasswd_Object=MibScalar
npWebProxyUserPasswd=_NpWebProxyUserPasswd_Object((1,3,6,1,4,1,11,2,4,3,18,15),_NpWebProxyUserPasswd_Type())
npWebProxyUserPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:npWebProxyUserPasswd.setStatus(_A)
_NpSecurity_ObjectIdentity=ObjectIdentity
npSecurity=_NpSecurity_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20))
class _NpSecurityDot11ServerAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16)));namedValues=NamedValues(*(('eap-md5',1),('eap-tls',2),('leap',4),('peap',8),('ttls',16)))
_NpSecurityDot11ServerAuthentication_Type.__name__=_D
_NpSecurityDot11ServerAuthentication_Object=MibScalar
npSecurityDot11ServerAuthentication=_NpSecurityDot11ServerAuthentication_Object((1,3,6,1,4,1,11,2,4,3,20,1),_NpSecurityDot11ServerAuthentication_Type())
npSecurityDot11ServerAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11ServerAuthentication.setStatus(_A)
class _NpSecurityDot1xEapMd5Identity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_NpSecurityDot1xEapMd5Identity_Type.__name__=_G
_NpSecurityDot1xEapMd5Identity_Object=MibScalar
npSecurityDot1xEapMd5Identity=_NpSecurityDot1xEapMd5Identity_Object((1,3,6,1,4,1,11,2,4,3,20,2),_NpSecurityDot1xEapMd5Identity_Type())
npSecurityDot1xEapMd5Identity.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot1xEapMd5Identity.setStatus(_A)
class _NpSecurityDot1xTLSAuthServerId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NpSecurityDot1xTLSAuthServerId_Type.__name__=_G
_NpSecurityDot1xTLSAuthServerId_Object=MibScalar
npSecurityDot1xTLSAuthServerId=_NpSecurityDot1xTLSAuthServerId_Object((1,3,6,1,4,1,11,2,4,3,20,3),_NpSecurityDot1xTLSAuthServerId_Type())
npSecurityDot1xTLSAuthServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot1xTLSAuthServerId.setStatus(_A)
class _NpSecurityPublicKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NpSecurityPublicKey_Type.__name__=_G
_NpSecurityPublicKey_Object=MibScalar
npSecurityPublicKey=_NpSecurityPublicKey_Object((1,3,6,1,4,1,11,2,4,3,20,4),_NpSecurityPublicKey_Type())
npSecurityPublicKey.setMaxAccess(_B)
if mibBuilder.loadTexts:npSecurityPublicKey.setStatus(_A)
class _NpSecurityDot11EncryptedDot1xEapMd5Secret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_NpSecurityDot11EncryptedDot1xEapMd5Secret_Type.__name__=_G
_NpSecurityDot11EncryptedDot1xEapMd5Secret_Object=MibScalar
npSecurityDot11EncryptedDot1xEapMd5Secret=_NpSecurityDot11EncryptedDot1xEapMd5Secret_Object((1,3,6,1,4,1,11,2,4,3,20,6),_NpSecurityDot11EncryptedDot1xEapMd5Secret_Type())
npSecurityDot11EncryptedDot1xEapMd5Secret.setMaxAccess(_K)
if mibBuilder.loadTexts:npSecurityDot11EncryptedDot1xEapMd5Secret.setStatus(_A)
_NpSecurityDot11EncryptedWEPKeyTable_ObjectIdentity=ObjectIdentity
npSecurityDot11EncryptedWEPKeyTable=_NpSecurityDot11EncryptedWEPKeyTable_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20,7))
_NpSecurityDot11EncryptedWEPKeyEntry_ObjectIdentity=ObjectIdentity
npSecurityDot11EncryptedWEPKeyEntry=_NpSecurityDot11EncryptedWEPKeyEntry_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20,7,1))
class _NpSecurityDot11EncryptedWEPKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_NpSecurityDot11EncryptedWEPKey_Type.__name__=_G
_NpSecurityDot11EncryptedWEPKey_Object=MibScalar
npSecurityDot11EncryptedWEPKey=_NpSecurityDot11EncryptedWEPKey_Object((1,3,6,1,4,1,11,2,4,3,20,7,1,2),_NpSecurityDot11EncryptedWEPKey_Type())
npSecurityDot11EncryptedWEPKey.setMaxAccess(_K)
if mibBuilder.loadTexts:npSecurityDot11EncryptedWEPKey.setStatus(_A)
class _NpSecurityDot11SignalStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('level-1-TBD',1),('level-2-TBD',2),('level-3-TBD',3),('level-4-TBD',4),('level-5-TBD',5)))
_NpSecurityDot11SignalStrength_Type.__name__=_D
_NpSecurityDot11SignalStrength_Object=MibScalar
npSecurityDot11SignalStrength=_NpSecurityDot11SignalStrength_Object((1,3,6,1,4,1,11,2,4,3,20,8),_NpSecurityDot11SignalStrength_Type())
npSecurityDot11SignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:npSecurityDot11SignalStrength.setStatus(_A)
_NpSecurityDot11SSIDTable_ObjectIdentity=ObjectIdentity
npSecurityDot11SSIDTable=_NpSecurityDot11SSIDTable_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20,9))
_NpSecurityDot11SSIDEntry_ObjectIdentity=ObjectIdentity
npSecurityDot11SSIDEntry=_NpSecurityDot11SSIDEntry_ObjectIdentity((1,3,6,1,4,1,11,2,4,3,20,9,1))
class _NpSecurityDot11SSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NpSecurityDot11SSID_Type.__name__=_G
_NpSecurityDot11SSID_Object=MibScalar
npSecurityDot11SSID=_NpSecurityDot11SSID_Object((1,3,6,1,4,1,11,2,4,3,20,9,1,2),_NpSecurityDot11SSID_Type())
npSecurityDot11SSID.setMaxAccess(_B)
if mibBuilder.loadTexts:npSecurityDot11SSID.setStatus(_A)
_NpSecurityDot11SSIDTableNumEntries_Type=Integer32
_NpSecurityDot11SSIDTableNumEntries_Object=MibScalar
npSecurityDot11SSIDTableNumEntries=_NpSecurityDot11SSIDTableNumEntries_Object((1,3,6,1,4,1,11,2,4,3,20,10),_NpSecurityDot11SSIDTableNumEntries_Type())
npSecurityDot11SSIDTableNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:npSecurityDot11SSIDTableNumEntries.setStatus(_A)
class _NpSecuritySnmpV3EncryptedUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_NpSecuritySnmpV3EncryptedUserName_Type.__name__=_G
_NpSecuritySnmpV3EncryptedUserName_Object=MibScalar
npSecuritySnmpV3EncryptedUserName=_NpSecuritySnmpV3EncryptedUserName_Object((1,3,6,1,4,1,11,2,4,3,20,13),_NpSecuritySnmpV3EncryptedUserName_Type())
npSecuritySnmpV3EncryptedUserName.setMaxAccess(_K)
if mibBuilder.loadTexts:npSecuritySnmpV3EncryptedUserName.setStatus(_A)
class _NpSecuritySnmpV3AuthKeyPassPhrase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_NpSecuritySnmpV3AuthKeyPassPhrase_Type.__name__=_G
_NpSecuritySnmpV3AuthKeyPassPhrase_Object=MibScalar
npSecuritySnmpV3AuthKeyPassPhrase=_NpSecuritySnmpV3AuthKeyPassPhrase_Object((1,3,6,1,4,1,11,2,4,3,20,14),_NpSecuritySnmpV3AuthKeyPassPhrase_Type())
npSecuritySnmpV3AuthKeyPassPhrase.setMaxAccess(_K)
if mibBuilder.loadTexts:npSecuritySnmpV3AuthKeyPassPhrase.setStatus(_A)
class _NpSecuritySnmpV3PrivKeyPassPhrase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_NpSecuritySnmpV3PrivKeyPassPhrase_Type.__name__=_G
_NpSecuritySnmpV3PrivKeyPassPhrase_Object=MibScalar
npSecuritySnmpV3PrivKeyPassPhrase=_NpSecuritySnmpV3PrivKeyPassPhrase_Object((1,3,6,1,4,1,11,2,4,3,20,15),_NpSecuritySnmpV3PrivKeyPassPhrase_Type())
npSecuritySnmpV3PrivKeyPassPhrase.setMaxAccess(_K)
if mibBuilder.loadTexts:npSecuritySnmpV3PrivKeyPassPhrase.setStatus(_A)
class _NpSecurityDot11ExactMatchServerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_NpSecurityDot11ExactMatchServerId_Type.__name__=_D
_NpSecurityDot11ExactMatchServerId_Object=MibScalar
npSecurityDot11ExactMatchServerId=_NpSecurityDot11ExactMatchServerId_Object((1,3,6,1,4,1,11,2,4,3,20,19),_NpSecurityDot11ExactMatchServerId_Type())
npSecurityDot11ExactMatchServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11ExactMatchServerId.setStatus(_A)
class _NpSecurityDot11EncryptionStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
_NpSecurityDot11EncryptionStrength_Type.__name__=_D
_NpSecurityDot11EncryptionStrength_Object=MibScalar
npSecurityDot11EncryptionStrength=_NpSecurityDot11EncryptionStrength_Object((1,3,6,1,4,1,11,2,4,3,20,20),_NpSecurityDot11EncryptionStrength_Type())
npSecurityDot11EncryptionStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11EncryptionStrength.setStatus(_A)
class _NpSecuritySslRedirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redirectionEnabled',1),('redirectionDisabled',2)))
_NpSecuritySslRedirection_Type.__name__=_D
_NpSecuritySslRedirection_Object=MibScalar
npSecuritySslRedirection=_NpSecuritySslRedirection_Object((1,3,6,1,4,1,11,2,4,3,20,23),_NpSecuritySslRedirection_Type())
npSecuritySslRedirection.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySslRedirection.setStatus(_A)
_NpSecurityServicesSupported_Type=Integer32
_NpSecurityServicesSupported_Object=MibScalar
npSecurityServicesSupported=_NpSecurityServicesSupported_Object((1,3,6,1,4,1,11,2,4,3,20,27),_NpSecurityServicesSupported_Type())
npSecurityServicesSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:npSecurityServicesSupported.setStatus(_A)
_NpSecurityDot11Encryption_Type=Integer32
_NpSecurityDot11Encryption_Object=MibScalar
npSecurityDot11Encryption=_NpSecurityDot11Encryption_Object((1,3,6,1,4,1,11,2,4,3,20,28),_NpSecurityDot11Encryption_Type())
npSecurityDot11Encryption.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11Encryption.setStatus(_A)
_NpSecurityDot11MulticastCipher_Type=Integer32
_NpSecurityDot11MulticastCipher_Object=MibScalar
npSecurityDot11MulticastCipher=_NpSecurityDot11MulticastCipher_Object((1,3,6,1,4,1,11,2,4,3,20,29),_NpSecurityDot11MulticastCipher_Type())
npSecurityDot11MulticastCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11MulticastCipher.setStatus(_A)
class _NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,63))
_NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Type.__name__=_G
_NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Object=MibScalar
npSecurityDot11EncryptedWPAConfigPSKPassPhrase=_NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Object((1,3,6,1,4,1,11,2,4,3,20,36),_NpSecurityDot11EncryptedWPAConfigPSKPassPhrase_Type())
npSecurityDot11EncryptedWPAConfigPSKPassPhrase.setMaxAccess(_K)
if mibBuilder.loadTexts:npSecurityDot11EncryptedWPAConfigPSKPassPhrase.setStatus(_A)
class _NpSecuritySslEncryptionStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
_NpSecuritySslEncryptionStrength_Type.__name__=_D
_NpSecuritySslEncryptionStrength_Object=MibScalar
npSecuritySslEncryptionStrength=_NpSecuritySslEncryptionStrength_Object((1,3,6,1,4,1,11,2,4,3,20,40),_NpSecuritySslEncryptionStrength_Type())
npSecuritySslEncryptionStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySslEncryptionStrength.setStatus(_A)
class _NpSecurityDot11DynamicEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('NONE',0),('BASIC',1),('WPA',2),('WPA2',3),('AUTO',4)))
_NpSecurityDot11DynamicEncryption_Type.__name__=_D
_NpSecurityDot11DynamicEncryption_Object=MibScalar
npSecurityDot11DynamicEncryption=_NpSecurityDot11DynamicEncryption_Object((1,3,6,1,4,1,11,2,4,3,20,42),_NpSecurityDot11DynamicEncryption_Type())
npSecurityDot11DynamicEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11DynamicEncryption.setStatus(_A)
class _NpSecurityDot11LinkAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,128,143)));namedValues=NamedValues(*(('open',1),('shared-key',2),('leap',128),('auto',143)))
_NpSecurityDot11LinkAuthentication_Type.__name__=_D
_NpSecurityDot11LinkAuthentication_Object=MibScalar
npSecurityDot11LinkAuthentication=_NpSecurityDot11LinkAuthentication_Object((1,3,6,1,4,1,11,2,4,3,20,43),_NpSecurityDot11LinkAuthentication_Type())
npSecurityDot11LinkAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot11LinkAuthentication.setStatus(_A)
class _NpSecuritySnmpV3AuthAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('md5',2),('sha-1',3)))
_NpSecuritySnmpV3AuthAlgorithm_Type.__name__=_D
_NpSecuritySnmpV3AuthAlgorithm_Object=MibScalar
npSecuritySnmpV3AuthAlgorithm=_NpSecuritySnmpV3AuthAlgorithm_Object((1,3,6,1,4,1,11,2,4,3,20,44),_NpSecuritySnmpV3AuthAlgorithm_Type())
npSecuritySnmpV3AuthAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySnmpV3AuthAlgorithm.setStatus(_A)
class _NpSecuritySnmpV3PrivAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('des',2),('aes-128',3)))
_NpSecuritySnmpV3PrivAlgorithm_Type.__name__=_D
_NpSecuritySnmpV3PrivAlgorithm_Object=MibScalar
npSecuritySnmpV3PrivAlgorithm=_NpSecuritySnmpV3PrivAlgorithm_Object((1,3,6,1,4,1,11,2,4,3,20,45),_NpSecuritySnmpV3PrivAlgorithm_Type())
npSecuritySnmpV3PrivAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySnmpV3PrivAlgorithm.setStatus(_A)
class _NpSecuritySnmpV3PassPhrase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('key',0),('passphrase',1)))
_NpSecuritySnmpV3PassPhrase_Type.__name__=_D
_NpSecuritySnmpV3PassPhrase_Object=MibScalar
npSecuritySnmpV3PassPhrase=_NpSecuritySnmpV3PassPhrase_Object((1,3,6,1,4,1,11,2,4,3,20,46),_NpSecuritySnmpV3PassPhrase_Type())
npSecuritySnmpV3PassPhrase.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySnmpV3PassPhrase.setStatus(_A)
class _NpSecurityWirelessDirectEncryptedPassPhrase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NpSecurityWirelessDirectEncryptedPassPhrase_Type.__name__=_G
_NpSecurityWirelessDirectEncryptedPassPhrase_Object=MibScalar
npSecurityWirelessDirectEncryptedPassPhrase=_NpSecurityWirelessDirectEncryptedPassPhrase_Object((1,3,6,1,4,1,11,2,4,3,20,55),_NpSecurityWirelessDirectEncryptedPassPhrase_Type())
npSecurityWirelessDirectEncryptedPassPhrase.setMaxAccess(_K)
if mibBuilder.loadTexts:npSecurityWirelessDirectEncryptedPassPhrase.setStatus(_A)
class _NpSecurityDot1xFailSafe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_NpSecurityDot1xFailSafe_Type.__name__=_D
_NpSecurityDot1xFailSafe_Object=MibScalar
npSecurityDot1xFailSafe=_NpSecurityDot1xFailSafe_Object((1,3,6,1,4,1,11,2,4,3,20,57),_NpSecurityDot1xFailSafe_Type())
npSecurityDot1xFailSafe.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecurityDot1xFailSafe.setStatus(_A)
_NpSecuritySSLProtocol_Type=Integer32
_NpSecuritySSLProtocol_Object=MibScalar
npSecuritySSLProtocol=_NpSecuritySSLProtocol_Object((1,3,6,1,4,1,11,2,4,3,20,58),_NpSecuritySSLProtocol_Type())
npSecuritySSLProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:npSecuritySSLProtocol.setStatus(_A)
_Trap_ObjectIdentity=ObjectIdentity
trap=_Trap_ObjectIdentity((1,3,6,1,4,1,11,2,13))
_TrapDest_ObjectIdentity=ObjectIdentity
trapDest=_TrapDest_ObjectIdentity((1,3,6,1,4,1,11,2,13,1))
_TrapDestinationNum_Type=Integer32
_TrapDestinationNum_Object=MibScalar
trapDestinationNum=_TrapDestinationNum_Object((1,3,6,1,4,1,11,2,13,1,1),_TrapDestinationNum_Type())
trapDestinationNum.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDestinationNum.setStatus(_A)
_TrapTest_Type=Integer32
_TrapTest_Object=MibScalar
trapTest=_TrapTest_Object((1,3,6,1,4,1,11,2,13,1,3),_TrapTest_Type())
trapTest.setMaxAccess(_C)
if mibBuilder.loadTexts:trapTest.setStatus(_A)
_TrapSource_Type=Integer32
_TrapSource_Object=MibScalar
trapSource=_TrapSource_Object((1,3,6,1,4,1,11,2,13,1,4),_TrapSource_Type())
trapSource.setMaxAccess(_B)
if mibBuilder.loadTexts:trapSource.setStatus(_A)
_TrapFilterDelay_Type=Integer32
_TrapFilterDelay_Object=MibScalar
trapFilterDelay=_TrapFilterDelay_Object((1,3,6,1,4,1,11,2,13,1,5),_TrapFilterDelay_Type())
trapFilterDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:trapFilterDelay.setStatus(_A)
_TrapFQDNNum_Type=Integer32
_TrapFQDNNum_Object=MibScalar
trapFQDNNum=_TrapFQDNNum_Object((1,3,6,1,4,1,11,2,13,1,6),_TrapFQDNNum_Type())
trapFQDNNum.setMaxAccess(_B)
if mibBuilder.loadTexts:trapFQDNNum.setStatus(_A)
_SnmpAccess_ObjectIdentity=ObjectIdentity
snmpAccess=_SnmpAccess_ObjectIdentity((1,3,6,1,4,1,11,2,15))
_Community_ObjectIdentity=ObjectIdentity
community=_Community_ObjectIdentity((1,3,6,1,4,1,11,2,15,1))
class _SetCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SetCommunityName_Type.__name__=_G
_SetCommunityName_Object=MibScalar
setCommunityName=_SetCommunityName_Object((1,3,6,1,4,1,11,2,15,1,1),_SetCommunityName_Type())
setCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:setCommunityName.setStatus(_A)
class _GetCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GetCommunityName_Type.__name__=_G
_GetCommunityName_Object=MibScalar
getCommunityName=_GetCommunityName_Object((1,3,6,1,4,1,11,2,15,1,2),_GetCommunityName_Type())
getCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:getCommunityName.setStatus(_A)
_PpmMIB_ObjectIdentity=ObjectIdentity
ppmMIB=_PpmMIB_ObjectIdentity((1,3,6,1,4,1,2699,1,2))
_PpmMIBObjects_ObjectIdentity=ObjectIdentity
ppmMIBObjects=_PpmMIBObjects_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1))
_PpmGeneral_ObjectIdentity=ObjectIdentity
ppmGeneral=_PpmGeneral_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,1))
class _PpmGeneralNaturalLanguage_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PpmGeneralNaturalLanguage_Type.__name__=_J
_PpmGeneralNaturalLanguage_Object=MibScalar
ppmGeneralNaturalLanguage=_PpmGeneralNaturalLanguage_Object((1,3,6,1,4,1,2699,1,2,1,1,1),_PpmGeneralNaturalLanguage_Type())
ppmGeneralNaturalLanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmGeneralNaturalLanguage.setStatus(_A)
class _PpmGeneralNumberOfPrinters_Type(Gauge32):defaultValue=0
_PpmGeneralNumberOfPrinters_Type.__name__=_S
_PpmGeneralNumberOfPrinters_Object=MibScalar
ppmGeneralNumberOfPrinters=_PpmGeneralNumberOfPrinters_Object((1,3,6,1,4,1,2699,1,2,1,1,2),_PpmGeneralNumberOfPrinters_Type())
ppmGeneralNumberOfPrinters.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmGeneralNumberOfPrinters.setStatus(_A)
class _PpmGeneralNumberOfPorts_Type(Gauge32):defaultValue=0
_PpmGeneralNumberOfPorts_Type.__name__=_S
_PpmGeneralNumberOfPorts_Object=MibScalar
ppmGeneralNumberOfPorts=_PpmGeneralNumberOfPorts_Object((1,3,6,1,4,1,2699,1,2,1,1,3),_PpmGeneralNumberOfPorts_Type())
ppmGeneralNumberOfPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmGeneralNumberOfPorts.setStatus(_A)
_PpmPrinter_ObjectIdentity=ObjectIdentity
ppmPrinter=_PpmPrinter_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,2))
_PpmPrinterTable_ObjectIdentity=ObjectIdentity
ppmPrinterTable=_PpmPrinterTable_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,2,1))
_PpmPrinterEntry_ObjectIdentity=ObjectIdentity
ppmPrinterEntry=_PpmPrinterEntry_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,2,1,1))
class _PpmPrinterName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PpmPrinterName_Type.__name__=_J
_PpmPrinterName_Object=MibScalar
ppmPrinterName=_PpmPrinterName_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,2),_PpmPrinterName_Type())
ppmPrinterName.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPrinterName.setStatus(_A)
class _PpmPrinterIEEE1284DeviceId_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_PpmPrinterIEEE1284DeviceId_Type.__name__=_G
_PpmPrinterIEEE1284DeviceId_Object=MibScalar
ppmPrinterIEEE1284DeviceId=_PpmPrinterIEEE1284DeviceId_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,3),_PpmPrinterIEEE1284DeviceId_Type())
ppmPrinterIEEE1284DeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPrinterIEEE1284DeviceId.setStatus(_A)
class _PpmPrinterNumberOfPorts_Type(Gauge32):defaultValue=0
_PpmPrinterNumberOfPorts_Type.__name__=_S
_PpmPrinterNumberOfPorts_Object=MibScalar
ppmPrinterNumberOfPorts=_PpmPrinterNumberOfPorts_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,4),_PpmPrinterNumberOfPorts_Type())
ppmPrinterNumberOfPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPrinterNumberOfPorts.setStatus(_A)
class _PpmPrinterPreferredPortIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PpmPrinterPreferredPortIndex_Type.__name__=_D
_PpmPrinterPreferredPortIndex_Object=MibScalar
ppmPrinterPreferredPortIndex=_PpmPrinterPreferredPortIndex_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,5),_PpmPrinterPreferredPortIndex_Type())
ppmPrinterPreferredPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPrinterPreferredPortIndex.setStatus(_A)
class _PpmPrinterHrDeviceIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PpmPrinterHrDeviceIndex_Type.__name__=_D
_PpmPrinterHrDeviceIndex_Object=MibScalar
ppmPrinterHrDeviceIndex=_PpmPrinterHrDeviceIndex_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,6),_PpmPrinterHrDeviceIndex_Type())
ppmPrinterHrDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPrinterHrDeviceIndex.setStatus(_A)
class _PpmPrinterSnmpCommunityName_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PpmPrinterSnmpCommunityName_Type.__name__=_G
_PpmPrinterSnmpCommunityName_Object=MibScalar
ppmPrinterSnmpCommunityName=_PpmPrinterSnmpCommunityName_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,7),_PpmPrinterSnmpCommunityName_Type())
ppmPrinterSnmpCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPrinterSnmpCommunityName.setStatus(_A)
class _PpmPrinterSnmpQueryEnabled_Type(TruthValue):defaultValue=2
_PpmPrinterSnmpQueryEnabled_Type.__name__=_Q
_PpmPrinterSnmpQueryEnabled_Object=MibScalar
ppmPrinterSnmpQueryEnabled=_PpmPrinterSnmpQueryEnabled_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,8),_PpmPrinterSnmpQueryEnabled_Type())
ppmPrinterSnmpQueryEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPrinterSnmpQueryEnabled.setStatus(_A)
_PpmPort_ObjectIdentity=ObjectIdentity
ppmPort=_PpmPort_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,3))
_PpmPortTable_ObjectIdentity=ObjectIdentity
ppmPortTable=_PpmPortTable_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,3,1))
_PpmPortEntry_ObjectIdentity=ObjectIdentity
ppmPortEntry=_PpmPortEntry_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,3,1,1))
class _PpmPortEnabled_Type(TruthValue):defaultValue=2
_PpmPortEnabled_Type.__name__=_Q
_PpmPortEnabled_Object=MibScalar
ppmPortEnabled=_PpmPortEnabled_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,2),_PpmPortEnabled_Type())
ppmPortEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPortEnabled.setStatus(_A)
class _PpmPortName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PpmPortName_Type.__name__=_J
_PpmPortName_Object=MibScalar
ppmPortName=_PpmPortName_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,3),_PpmPortName_Type())
ppmPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPortName.setStatus(_A)
class _PpmPortServiceNameOrURI_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PpmPortServiceNameOrURI_Type.__name__=_J
_PpmPortServiceNameOrURI_Object=MibScalar
ppmPortServiceNameOrURI=_PpmPortServiceNameOrURI_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,4),_PpmPortServiceNameOrURI_Type())
ppmPortServiceNameOrURI.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPortServiceNameOrURI.setStatus(_A)
class _PpmPortProtocolType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PpmPortProtocolType_Type.__name__=_D
_PpmPortProtocolType_Object=MibScalar
ppmPortProtocolType=_PpmPortProtocolType_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,5),_PpmPortProtocolType_Type())
ppmPortProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPortProtocolType.setStatus(_A)
class _PpmPortProtocolTargetPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PpmPortProtocolTargetPort_Type.__name__=_D
_PpmPortProtocolTargetPort_Object=MibScalar
ppmPortProtocolTargetPort=_PpmPortProtocolTargetPort_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,6),_PpmPortProtocolTargetPort_Type())
ppmPortProtocolTargetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPortProtocolTargetPort.setStatus(_A)
class _PpmPortProtocolAltSourceEnabled_Type(TruthValue):defaultValue=2
_PpmPortProtocolAltSourceEnabled_Type.__name__=_Q
_PpmPortProtocolAltSourceEnabled_Object=MibScalar
ppmPortProtocolAltSourceEnabled=_PpmPortProtocolAltSourceEnabled_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,7),_PpmPortProtocolAltSourceEnabled_Type())
ppmPortProtocolAltSourceEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPortProtocolAltSourceEnabled.setStatus(_A)
class _PpmPortPrtChannelIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PpmPortPrtChannelIndex_Type.__name__=_D
_PpmPortPrtChannelIndex_Object=MibScalar
ppmPortPrtChannelIndex=_PpmPortPrtChannelIndex_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,8),_PpmPortPrtChannelIndex_Type())
ppmPortPrtChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPortPrtChannelIndex.setStatus(_A)
class _PpmPortLprByteCountEnabled_Type(TruthValue):defaultValue=2
_PpmPortLprByteCountEnabled_Type.__name__=_Q
_PpmPortLprByteCountEnabled_Object=MibScalar
ppmPortLprByteCountEnabled=_PpmPortLprByteCountEnabled_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,9),_PpmPortLprByteCountEnabled_Type())
ppmPortLprByteCountEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ppmPortLprByteCountEnabled.setStatus(_A)
_SnmpV2_ObjectIdentity=ObjectIdentity
snmpV2=_SnmpV2_ObjectIdentity((1,3,6,1,6))
_SnmpModules_ObjectIdentity=ObjectIdentity
snmpModules=_SnmpModules_ObjectIdentity((1,3,6,1,6,3))
_SnmpFrameworkMIB_ObjectIdentity=ObjectIdentity
snmpFrameworkMIB=_SnmpFrameworkMIB_ObjectIdentity((1,3,6,1,6,3,10))
_SnmpFrameworkMIBObjects_ObjectIdentity=ObjectIdentity
snmpFrameworkMIBObjects=_SnmpFrameworkMIBObjects_ObjectIdentity((1,3,6,1,6,3,10,2))
_SnmpEngine_ObjectIdentity=ObjectIdentity
snmpEngine=_SnmpEngine_ObjectIdentity((1,3,6,1,6,3,10,2,1))
_SnmpEngineID_Type=SnmpEngineID
_SnmpEngineID_Object=MibScalar
snmpEngineID=_SnmpEngineID_Object((1,3,6,1,6,3,10,2,1,1),_SnmpEngineID_Type())
snmpEngineID.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpEngineID.setStatus(_A)
class _SnmpEngineBoots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SnmpEngineBoots_Type.__name__=_D
_SnmpEngineBoots_Object=MibScalar
snmpEngineBoots=_SnmpEngineBoots_Object((1,3,6,1,6,3,10,2,1,2),_SnmpEngineBoots_Type())
snmpEngineBoots.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpEngineBoots.setStatus(_A)
class _SnmpEngineTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SnmpEngineTime_Type.__name__=_D
_SnmpEngineTime_Object=MibScalar
snmpEngineTime=_SnmpEngineTime_Object((1,3,6,1,6,3,10,2,1,3),_SnmpEngineTime_Type())
snmpEngineTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpEngineTime.setStatus(_A)
if mibBuilder.loadTexts:snmpEngineTime.setUnits('seconds')
class _SnmpEngineMaxMessageSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(484,2147483647))
_SnmpEngineMaxMessageSize_Type.__name__=_D
_SnmpEngineMaxMessageSize_Object=MibScalar
snmpEngineMaxMessageSize=_SnmpEngineMaxMessageSize_Object((1,3,6,1,6,3,10,2,1,4),_SnmpEngineMaxMessageSize_Type())
snmpEngineMaxMessageSize.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpEngineMaxMessageSize.setStatus(_A)
_SnmpMPDMIB_ObjectIdentity=ObjectIdentity
snmpMPDMIB=_SnmpMPDMIB_ObjectIdentity((1,3,6,1,6,3,11))
_SnmpMPDMIBObjects_ObjectIdentity=ObjectIdentity
snmpMPDMIBObjects=_SnmpMPDMIBObjects_ObjectIdentity((1,3,6,1,6,3,11,2))
_SnmpMPDStats_ObjectIdentity=ObjectIdentity
snmpMPDStats=_SnmpMPDStats_ObjectIdentity((1,3,6,1,6,3,11,2,1))
_SnmpUnknownSecurityModels_Type=Counter32
_SnmpUnknownSecurityModels_Object=MibScalar
snmpUnknownSecurityModels=_SnmpUnknownSecurityModels_Object((1,3,6,1,6,3,11,2,1,1),_SnmpUnknownSecurityModels_Type())
snmpUnknownSecurityModels.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpUnknownSecurityModels.setStatus(_A)
_SnmpInvalidMsgs_Type=Counter32
_SnmpInvalidMsgs_Object=MibScalar
snmpInvalidMsgs=_SnmpInvalidMsgs_Object((1,3,6,1,6,3,11,2,1,2),_SnmpInvalidMsgs_Type())
snmpInvalidMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpInvalidMsgs.setStatus(_A)
_SnmpUnknownPDUHandlers_Type=Counter32
_SnmpUnknownPDUHandlers_Object=MibScalar
snmpUnknownPDUHandlers=_SnmpUnknownPDUHandlers_Object((1,3,6,1,6,3,11,2,1,3),_SnmpUnknownPDUHandlers_Type())
snmpUnknownPDUHandlers.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpUnknownPDUHandlers.setStatus(_A)
_SnmpUsmMIB_ObjectIdentity=ObjectIdentity
snmpUsmMIB=_SnmpUsmMIB_ObjectIdentity((1,3,6,1,6,3,15))
_UsmMIBObjects_ObjectIdentity=ObjectIdentity
usmMIBObjects=_UsmMIBObjects_ObjectIdentity((1,3,6,1,6,3,15,1))
_UsmStats_ObjectIdentity=ObjectIdentity
usmStats=_UsmStats_ObjectIdentity((1,3,6,1,6,3,15,1,1))
_UsmStatsUnsupportedSecLevels_Type=Counter32
_UsmStatsUnsupportedSecLevels_Object=MibScalar
usmStatsUnsupportedSecLevels=_UsmStatsUnsupportedSecLevels_Object((1,3,6,1,6,3,15,1,1,1),_UsmStatsUnsupportedSecLevels_Type())
usmStatsUnsupportedSecLevels.setMaxAccess(_B)
if mibBuilder.loadTexts:usmStatsUnsupportedSecLevels.setStatus(_A)
_UsmStatsNotInTimeWindows_Type=Counter32
_UsmStatsNotInTimeWindows_Object=MibScalar
usmStatsNotInTimeWindows=_UsmStatsNotInTimeWindows_Object((1,3,6,1,6,3,15,1,1,2),_UsmStatsNotInTimeWindows_Type())
usmStatsNotInTimeWindows.setMaxAccess(_B)
if mibBuilder.loadTexts:usmStatsNotInTimeWindows.setStatus(_A)
_UsmStatsUnknownUserNames_Type=Counter32
_UsmStatsUnknownUserNames_Object=MibScalar
usmStatsUnknownUserNames=_UsmStatsUnknownUserNames_Object((1,3,6,1,6,3,15,1,1,3),_UsmStatsUnknownUserNames_Type())
usmStatsUnknownUserNames.setMaxAccess(_B)
if mibBuilder.loadTexts:usmStatsUnknownUserNames.setStatus(_A)
_UsmStatsUnknownEngineIDs_Type=Counter32
_UsmStatsUnknownEngineIDs_Object=MibScalar
usmStatsUnknownEngineIDs=_UsmStatsUnknownEngineIDs_Object((1,3,6,1,6,3,15,1,1,4),_UsmStatsUnknownEngineIDs_Type())
usmStatsUnknownEngineIDs.setMaxAccess(_B)
if mibBuilder.loadTexts:usmStatsUnknownEngineIDs.setStatus(_A)
_UsmStatsWrongDigests_Type=Counter32
_UsmStatsWrongDigests_Object=MibScalar
usmStatsWrongDigests=_UsmStatsWrongDigests_Object((1,3,6,1,6,3,15,1,1,5),_UsmStatsWrongDigests_Type())
usmStatsWrongDigests.setMaxAccess(_B)
if mibBuilder.loadTexts:usmStatsWrongDigests.setStatus(_A)
_UsmStatsDecryptionErrors_Type=Counter32
_UsmStatsDecryptionErrors_Object=MibScalar
usmStatsDecryptionErrors=_UsmStatsDecryptionErrors_Object((1,3,6,1,6,3,15,1,1,6),_UsmStatsDecryptionErrors_Type())
usmStatsDecryptionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:usmStatsDecryptionErrors.setStatus(_A)
_UsmUser_ObjectIdentity=ObjectIdentity
usmUser=_UsmUser_ObjectIdentity((1,3,6,1,6,3,15,1,2))
_UsmUserSpinLock_Type=TestAndIncr
_UsmUserSpinLock_Object=MibScalar
usmUserSpinLock=_UsmUserSpinLock_Object((1,3,6,1,6,3,15,1,2,1),_UsmUserSpinLock_Type())
usmUserSpinLock.setMaxAccess(_C)
if mibBuilder.loadTexts:usmUserSpinLock.setStatus(_A)
_UsmUserTable_ObjectIdentity=ObjectIdentity
usmUserTable=_UsmUserTable_ObjectIdentity((1,3,6,1,6,3,15,1,2,2))
_UsmUserEntry_ObjectIdentity=ObjectIdentity
usmUserEntry=_UsmUserEntry_ObjectIdentity((1,3,6,1,6,3,15,1,2,2,1))
_UsmUserSecurityName_Type=SnmpAdminString
_UsmUserSecurityName_Object=MibScalar
usmUserSecurityName=_UsmUserSecurityName_Object((1,3,6,1,6,3,15,1,2,2,1,3),_UsmUserSecurityName_Type())
usmUserSecurityName.setMaxAccess(_B)
if mibBuilder.loadTexts:usmUserSecurityName.setStatus(_A)
_UsmUserCloneFrom_Type=RowPointer
_UsmUserCloneFrom_Object=MibScalar
usmUserCloneFrom=_UsmUserCloneFrom_Object((1,3,6,1,6,3,15,1,2,2,1,4),_UsmUserCloneFrom_Type())
usmUserCloneFrom.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserCloneFrom.setStatus(_A)
_UsmUserAuthProtocol_Type=AutonomousType
_UsmUserAuthProtocol_Object=MibScalar
usmUserAuthProtocol=_UsmUserAuthProtocol_Object((1,3,6,1,6,3,15,1,2,2,1,5),_UsmUserAuthProtocol_Type())
usmUserAuthProtocol.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserAuthProtocol.setStatus(_A)
class _UsmUserAuthKeyChange_Type(KeyChange):defaultHexValue=''
_UsmUserAuthKeyChange_Type.__name__=_O
_UsmUserAuthKeyChange_Object=MibScalar
usmUserAuthKeyChange=_UsmUserAuthKeyChange_Object((1,3,6,1,6,3,15,1,2,2,1,6),_UsmUserAuthKeyChange_Type())
usmUserAuthKeyChange.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserAuthKeyChange.setStatus(_A)
class _UsmUserOwnAuthKeyChange_Type(KeyChange):defaultHexValue=''
_UsmUserOwnAuthKeyChange_Type.__name__=_O
_UsmUserOwnAuthKeyChange_Object=MibScalar
usmUserOwnAuthKeyChange=_UsmUserOwnAuthKeyChange_Object((1,3,6,1,6,3,15,1,2,2,1,7),_UsmUserOwnAuthKeyChange_Type())
usmUserOwnAuthKeyChange.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserOwnAuthKeyChange.setStatus(_A)
_UsmUserPrivProtocol_Type=AutonomousType
_UsmUserPrivProtocol_Object=MibScalar
usmUserPrivProtocol=_UsmUserPrivProtocol_Object((1,3,6,1,6,3,15,1,2,2,1,8),_UsmUserPrivProtocol_Type())
usmUserPrivProtocol.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserPrivProtocol.setStatus(_A)
class _UsmUserPrivKeyChange_Type(KeyChange):defaultHexValue=''
_UsmUserPrivKeyChange_Type.__name__=_O
_UsmUserPrivKeyChange_Object=MibScalar
usmUserPrivKeyChange=_UsmUserPrivKeyChange_Object((1,3,6,1,6,3,15,1,2,2,1,9),_UsmUserPrivKeyChange_Type())
usmUserPrivKeyChange.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserPrivKeyChange.setStatus(_A)
class _UsmUserOwnPrivKeyChange_Type(KeyChange):defaultHexValue=''
_UsmUserOwnPrivKeyChange_Type.__name__=_O
_UsmUserOwnPrivKeyChange_Object=MibScalar
usmUserOwnPrivKeyChange=_UsmUserOwnPrivKeyChange_Object((1,3,6,1,6,3,15,1,2,2,1,10),_UsmUserOwnPrivKeyChange_Type())
usmUserOwnPrivKeyChange.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserOwnPrivKeyChange.setStatus(_A)
class _UsmUserPublic_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UsmUserPublic_Type.__name__=_G
_UsmUserPublic_Object=MibScalar
usmUserPublic=_UsmUserPublic_Object((1,3,6,1,6,3,15,1,2,2,1,11),_UsmUserPublic_Type())
usmUserPublic.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserPublic.setStatus(_A)
class _UsmUserStorageType_Type(StorageType):defaultValue=3
_UsmUserStorageType_Type.__name__=_P
_UsmUserStorageType_Object=MibScalar
usmUserStorageType=_UsmUserStorageType_Object((1,3,6,1,6,3,15,1,2,2,1,12),_UsmUserStorageType_Type())
usmUserStorageType.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserStorageType.setStatus(_A)
_UsmUserStatus_Type=RowStatus
_UsmUserStatus_Object=MibScalar
usmUserStatus=_UsmUserStatus_Object((1,3,6,1,6,3,15,1,2,2,1,13),_UsmUserStatus_Type())
usmUserStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:usmUserStatus.setStatus(_A)
_SnmpVacmMIB_ObjectIdentity=ObjectIdentity
snmpVacmMIB=_SnmpVacmMIB_ObjectIdentity((1,3,6,1,6,3,16))
_VacmMIBObjects_ObjectIdentity=ObjectIdentity
vacmMIBObjects=_VacmMIBObjects_ObjectIdentity((1,3,6,1,6,3,16,1))
_VacmContextTable_ObjectIdentity=ObjectIdentity
vacmContextTable=_VacmContextTable_ObjectIdentity((1,3,6,1,6,3,16,1,1))
_VacmContextEntry_ObjectIdentity=ObjectIdentity
vacmContextEntry=_VacmContextEntry_ObjectIdentity((1,3,6,1,6,3,16,1,1,1))
class _VacmContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VacmContextName_Type.__name__=_J
_VacmContextName_Object=MibScalar
vacmContextName=_VacmContextName_Object((1,3,6,1,6,3,16,1,1,1,1),_VacmContextName_Type())
vacmContextName.setMaxAccess(_B)
if mibBuilder.loadTexts:vacmContextName.setStatus(_A)
_VacmSecurityToGroupTable_ObjectIdentity=ObjectIdentity
vacmSecurityToGroupTable=_VacmSecurityToGroupTable_ObjectIdentity((1,3,6,1,6,3,16,1,2))
_VacmSecurityToGroupEntry_ObjectIdentity=ObjectIdentity
vacmSecurityToGroupEntry=_VacmSecurityToGroupEntry_ObjectIdentity((1,3,6,1,6,3,16,1,2,1))
class _VacmGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_VacmGroupName_Type.__name__=_J
_VacmGroupName_Object=MibScalar
vacmGroupName=_VacmGroupName_Object((1,3,6,1,6,3,16,1,2,1,3),_VacmGroupName_Type())
vacmGroupName.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmGroupName.setStatus(_A)
class _VacmSecurityToGroupStorageType_Type(StorageType):defaultValue=3
_VacmSecurityToGroupStorageType_Type.__name__=_P
_VacmSecurityToGroupStorageType_Object=MibScalar
vacmSecurityToGroupStorageType=_VacmSecurityToGroupStorageType_Object((1,3,6,1,6,3,16,1,2,1,4),_VacmSecurityToGroupStorageType_Type())
vacmSecurityToGroupStorageType.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmSecurityToGroupStorageType.setStatus(_A)
_VacmSecurityToGroupStatus_Type=RowStatus
_VacmSecurityToGroupStatus_Object=MibScalar
vacmSecurityToGroupStatus=_VacmSecurityToGroupStatus_Object((1,3,6,1,6,3,16,1,2,1,5),_VacmSecurityToGroupStatus_Type())
vacmSecurityToGroupStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmSecurityToGroupStatus.setStatus(_A)
_VacmAccessTable_ObjectIdentity=ObjectIdentity
vacmAccessTable=_VacmAccessTable_ObjectIdentity((1,3,6,1,6,3,16,1,4))
_VacmAccessEntry_ObjectIdentity=ObjectIdentity
vacmAccessEntry=_VacmAccessEntry_ObjectIdentity((1,3,6,1,6,3,16,1,4,1))
class _VacmAccessContextMatch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exact',1),('prefix',2)))
_VacmAccessContextMatch_Type.__name__=_D
_VacmAccessContextMatch_Object=MibScalar
vacmAccessContextMatch=_VacmAccessContextMatch_Object((1,3,6,1,6,3,16,1,4,1,4),_VacmAccessContextMatch_Type())
vacmAccessContextMatch.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmAccessContextMatch.setStatus(_A)
class _VacmAccessReadViewName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VacmAccessReadViewName_Type.__name__=_J
_VacmAccessReadViewName_Object=MibScalar
vacmAccessReadViewName=_VacmAccessReadViewName_Object((1,3,6,1,6,3,16,1,4,1,5),_VacmAccessReadViewName_Type())
vacmAccessReadViewName.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmAccessReadViewName.setStatus(_A)
class _VacmAccessWriteViewName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VacmAccessWriteViewName_Type.__name__=_J
_VacmAccessWriteViewName_Object=MibScalar
vacmAccessWriteViewName=_VacmAccessWriteViewName_Object((1,3,6,1,6,3,16,1,4,1,6),_VacmAccessWriteViewName_Type())
vacmAccessWriteViewName.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmAccessWriteViewName.setStatus(_A)
class _VacmAccessNotifyViewName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VacmAccessNotifyViewName_Type.__name__=_J
_VacmAccessNotifyViewName_Object=MibScalar
vacmAccessNotifyViewName=_VacmAccessNotifyViewName_Object((1,3,6,1,6,3,16,1,4,1,7),_VacmAccessNotifyViewName_Type())
vacmAccessNotifyViewName.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmAccessNotifyViewName.setStatus(_A)
class _VacmAccessStorageType_Type(StorageType):defaultValue=3
_VacmAccessStorageType_Type.__name__=_P
_VacmAccessStorageType_Object=MibScalar
vacmAccessStorageType=_VacmAccessStorageType_Object((1,3,6,1,6,3,16,1,4,1,8),_VacmAccessStorageType_Type())
vacmAccessStorageType.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmAccessStorageType.setStatus(_A)
_VacmAccessStatus_Type=RowStatus
_VacmAccessStatus_Object=MibScalar
vacmAccessStatus=_VacmAccessStatus_Object((1,3,6,1,6,3,16,1,4,1,9),_VacmAccessStatus_Type())
vacmAccessStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmAccessStatus.setStatus(_A)
_VacmMIBViews_ObjectIdentity=ObjectIdentity
vacmMIBViews=_VacmMIBViews_ObjectIdentity((1,3,6,1,6,3,16,1,5))
_VacmViewSpinLock_Type=TestAndIncr
_VacmViewSpinLock_Object=MibScalar
vacmViewSpinLock=_VacmViewSpinLock_Object((1,3,6,1,6,3,16,1,5,1),_VacmViewSpinLock_Type())
vacmViewSpinLock.setMaxAccess(_C)
if mibBuilder.loadTexts:vacmViewSpinLock.setStatus(_A)
_VacmViewTreeFamilyTable_ObjectIdentity=ObjectIdentity
vacmViewTreeFamilyTable=_VacmViewTreeFamilyTable_ObjectIdentity((1,3,6,1,6,3,16,1,5,2))
_VacmViewTreeFamilyEntry_ObjectIdentity=ObjectIdentity
vacmViewTreeFamilyEntry=_VacmViewTreeFamilyEntry_ObjectIdentity((1,3,6,1,6,3,16,1,5,2,1))
class _VacmViewTreeFamilyMask_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_VacmViewTreeFamilyMask_Type.__name__=_G
_VacmViewTreeFamilyMask_Object=MibScalar
vacmViewTreeFamilyMask=_VacmViewTreeFamilyMask_Object((1,3,6,1,6,3,16,1,5,2,1,3),_VacmViewTreeFamilyMask_Type())
vacmViewTreeFamilyMask.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmViewTreeFamilyMask.setStatus(_A)
class _VacmViewTreeFamilyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('included',1),('excluded',2)))
_VacmViewTreeFamilyType_Type.__name__=_D
_VacmViewTreeFamilyType_Object=MibScalar
vacmViewTreeFamilyType=_VacmViewTreeFamilyType_Object((1,3,6,1,6,3,16,1,5,2,1,4),_VacmViewTreeFamilyType_Type())
vacmViewTreeFamilyType.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmViewTreeFamilyType.setStatus(_A)
class _VacmViewTreeFamilyStorageType_Type(StorageType):defaultValue=3
_VacmViewTreeFamilyStorageType_Type.__name__=_P
_VacmViewTreeFamilyStorageType_Object=MibScalar
vacmViewTreeFamilyStorageType=_VacmViewTreeFamilyStorageType_Object((1,3,6,1,6,3,16,1,5,2,1,5),_VacmViewTreeFamilyStorageType_Type())
vacmViewTreeFamilyStorageType.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmViewTreeFamilyStorageType.setStatus(_A)
_VacmViewTreeFamilyStatus_Type=RowStatus
_VacmViewTreeFamilyStatus_Object=MibScalar
vacmViewTreeFamilyStatus=_VacmViewTreeFamilyStatus_Object((1,3,6,1,6,3,16,1,5,2,1,6),_VacmViewTreeFamilyStatus_Type())
vacmViewTreeFamilyStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:vacmViewTreeFamilyStatus.setStatus(_A)
mibBuilder.exportSymbols('HP-PAGEWIDE-PRO-477DW-MFP-MIB',**{'ieee802dot11':ieee802dot11,'dot11smt':dot11smt,'dot11StationConfigTable':dot11StationConfigTable,'dot11StationConfigEntry':dot11StationConfigEntry,'dot11DesiredSSID':dot11DesiredSSID,'dot11DesiredBSSType':dot11DesiredBSSType,'dot11AuthenticationAlgorithmsTable':dot11AuthenticationAlgorithmsTable,'dot11AuthenticationAlgorithmsEntry':dot11AuthenticationAlgorithmsEntry,'dot11AuthenticationAlgorithm':dot11AuthenticationAlgorithm,'dot11AuthenticationAlgorithmsEnable':dot11AuthenticationAlgorithmsEnable,'dot11WEPDefaultKeysTable':dot11WEPDefaultKeysTable,'dot11WEPDefaultKeysEntry':dot11WEPDefaultKeysEntry,'dot11WEPDefaultKeyValue':dot11WEPDefaultKeyValue,'dot11PrivacyTable':dot11PrivacyTable,'dot11PrivacyEntry':dot11PrivacyEntry,'dot11PrivacyInvoked':dot11PrivacyInvoked,'dot11WEPDefaultKeyID':dot11WEPDefaultKeyID,'dot11phy':dot11phy,'dot11PhyOperationTable':dot11PhyOperationTable,'dot11PhyOperationEntry':dot11PhyOperationEntry,'dot11CurrentRegDomain':dot11CurrentRegDomain,'ieee802dot11i':ieee802dot11i,'dot11RSNConfigAuthenticationSuitesTable':dot11RSNConfigAuthenticationSuitesTable,'dot11RSNConfigAuthenticationSuitesEntry':dot11RSNConfigAuthenticationSuitesEntry,'dot11RSNConfigAuthenticationSuite':dot11RSNConfigAuthenticationSuite,'dot11RSNConfigAuthenticationSuiteEnabled':dot11RSNConfigAuthenticationSuiteEnabled,'org':org,'dod':dod,'internet':internet,'mgmt':mgmt,'mib-2':mib_2,'system':system,'sysDescr':sysDescr,'sysObjectID':sysObjectID,'sysUpTime':sysUpTime,'sysContact':sysContact,'sysName':sysName,'sysLocation':sysLocation,'sysServices':sysServices,'sysORLastChange':sysORLastChange,'interfaces':interfaces,'ifNumber':ifNumber,'ifTable':ifTable,'ifEntry':ifEntry,'ifIndex':ifIndex,'ifDescr':ifDescr,'ifType':ifType,'ifMtu':ifMtu,'ifSpeed':ifSpeed,'ifPhysAddress':ifPhysAddress,'ifAdminStatus':ifAdminStatus,'ifOperStatus':ifOperStatus,'ifLastChange':ifLastChange,'ifInOctets':ifInOctets,'ifInUcastPkts':ifInUcastPkts,'ifInNUcastPkts':ifInNUcastPkts,'ifInDiscards':ifInDiscards,'ifInErrors':ifInErrors,'ifInUnknownProtos':ifInUnknownProtos,'ifOutOctets':ifOutOctets,'ifOutUcastPkts':ifOutUcastPkts,'ifOutNUcastPkts':ifOutNUcastPkts,'ifOutDiscards':ifOutDiscards,'ifOutErrors':ifOutErrors,'ifOutQLen':ifOutQLen,'ifSpecific':ifSpecific,'ip':ip,'ipForwarding':ipForwarding,'ipDefaultTTL':ipDefaultTTL,'ipInReceives':ipInReceives,'ipInHdrErrors':ipInHdrErrors,'ipInAddrErrors':ipInAddrErrors,'ipForwDatagrams':ipForwDatagrams,'ipInUnknownProtos':ipInUnknownProtos,'ipInDiscards':ipInDiscards,'ipInDelivers':ipInDelivers,'ipOutRequests':ipOutRequests,'ipOutDiscards':ipOutDiscards,'ipOutNoRoutes':ipOutNoRoutes,'ipReasmTimeout':ipReasmTimeout,'ipReasmReqds':ipReasmReqds,'ipReasmOKs':ipReasmOKs,'ipReasmFails':ipReasmFails,'ipFragOKs':ipFragOKs,'ipFragFails':ipFragFails,'ipFragCreates':ipFragCreates,'ipAddrTable':ipAddrTable,'ipAddrEntry':ipAddrEntry,'ipAdEntAddr':ipAdEntAddr,'ipAdEntIfIndex':ipAdEntIfIndex,'ipAdEntNetMask':ipAdEntNetMask,'ipAdEntBcastAddr':ipAdEntBcastAddr,'ipRouteTable':ipRouteTable,'ipRouteEntry':ipRouteEntry,'ipRouteDest':ipRouteDest,'ipRouteIfIndex':ipRouteIfIndex,'ipRouteMetric1':ipRouteMetric1,'ipRouteNextHop':ipRouteNextHop,'ipRouteType':ipRouteType,'ipRouteProto':ipRouteProto,'ipRouteMask':ipRouteMask,'ipRouteInfo':ipRouteInfo,'ipNetToMediaTable':ipNetToMediaTable,'ipNetToMediaEntry':ipNetToMediaEntry,'ipNetToMediaIfIndex':ipNetToMediaIfIndex,'ipNetToMediaPhysAddress':ipNetToMediaPhysAddress,'ipNetToMediaNetAddress':ipNetToMediaNetAddress,'ipNetToMediaType':ipNetToMediaType,'ipRoutingDiscards':ipRoutingDiscards,'snmp':snmp,'snmpInPkts':snmpInPkts,'snmpOutPkts':snmpOutPkts,'snmpInBadVersions':snmpInBadVersions,'snmpInBadCommunityNames':snmpInBadCommunityNames,'snmpInBadCommunityUses':snmpInBadCommunityUses,'snmpInASNParseErrs':snmpInASNParseErrs,'snmpInTooBigs':snmpInTooBigs,'snmpInNoSuchNames':snmpInNoSuchNames,'snmpInBadValues':snmpInBadValues,'snmpInReadOnlys':snmpInReadOnlys,'snmpInGenErrs':snmpInGenErrs,'snmpInTotalReqVars':snmpInTotalReqVars,'snmpInTotalSetVars':snmpInTotalSetVars,'snmpInGetRequests':snmpInGetRequests,'snmpInGetNexts':snmpInGetNexts,'snmpInSetRequests':snmpInSetRequests,'snmpInGetResponses':snmpInGetResponses,'snmpInTraps':snmpInTraps,'snmpOutTooBigs':snmpOutTooBigs,'snmpOutNoSuchNames':snmpOutNoSuchNames,'snmpOutBadValues':snmpOutBadValues,'snmpOutGenErrs':snmpOutGenErrs,'snmpOutGetRequests':snmpOutGetRequests,'snmpOutGetNexts':snmpOutGetNexts,'snmpOutSetRequests':snmpOutSetRequests,'snmpOutGetResponses':snmpOutGetResponses,'snmpOutTraps':snmpOutTraps,'snmpEnableAuthenTraps':snmpEnableAuthenTraps,'snmpSilentDrops':snmpSilentDrops,'snmpProxyDrops':snmpProxyDrops,'host':host,'hrSystem':hrSystem,'hrSystemUptime':hrSystemUptime,'hrSystemDate':hrSystemDate,'hrSystemInitialLoadDevice':hrSystemInitialLoadDevice,'hrSystemInitialLoadParameters':hrSystemInitialLoadParameters,'hrSystemNumUsers':hrSystemNumUsers,'hrSystemProcesses':hrSystemProcesses,'hrSystemMaxProcesses':hrSystemMaxProcesses,'hrStorage':hrStorage,'hrMemorySize':hrMemorySize,'hrStorageTable':hrStorageTable,'hrStorageEntry':hrStorageEntry,'hrStorageIndex':hrStorageIndex,'hrStorageType':hrStorageType,'hrStorageDescr':hrStorageDescr,'hrStorageAllocationUnits':hrStorageAllocationUnits,'hrStorageSize':hrStorageSize,'hrStorageUsed':hrStorageUsed,'hrDevice':hrDevice,'hrDeviceTable':hrDeviceTable,'hrDeviceEntry':hrDeviceEntry,'hrDeviceIndex':hrDeviceIndex,'hrDeviceType':hrDeviceType,'hrDeviceDescr':hrDeviceDescr,'hrDeviceID':hrDeviceID,'hrDeviceStatus':hrDeviceStatus,'hrDeviceErrors':hrDeviceErrors,'hrPrinterTable':hrPrinterTable,'hrPrinterEntry':hrPrinterEntry,'hrPrinterStatus':hrPrinterStatus,'hrPrinterDetectedErrorState':hrPrinterDetectedErrorState,'ifMIB':ifMIB,'ifMIBObjects':ifMIBObjects,'ifTableLastChange':ifTableLastChange,'printmib':printmib,'prtGeneral':prtGeneral,'prtGeneralTable':prtGeneralTable,'prtGeneralEntry':prtGeneralEntry,'prtGeneralConfigChanges':prtGeneralConfigChanges,'prtGeneralCurrentLocalization':prtGeneralCurrentLocalization,'prtGeneralReset':prtGeneralReset,'prtGeneralCurrentOperator':prtGeneralCurrentOperator,'prtGeneralServicePerson':prtGeneralServicePerson,'prtInputDefaultIndex':prtInputDefaultIndex,'prtOutputDefaultIndex':prtOutputDefaultIndex,'prtMarkerDefaultIndex':prtMarkerDefaultIndex,'prtMediaPathDefaultIndex':prtMediaPathDefaultIndex,'prtConsoleLocalization':prtConsoleLocalization,'prtConsoleNumberOfDisplayLines':prtConsoleNumberOfDisplayLines,'prtGeneralPrinterName':prtGeneralPrinterName,'prtGeneralSerialNumber':prtGeneralSerialNumber,'prtCover':prtCover,'prtCoverTable':prtCoverTable,'prtCoverEntry':prtCoverEntry,'prtCoverDescription':prtCoverDescription,'prtCoverStatus':prtCoverStatus,'prtLocalization':prtLocalization,'prtLocalizationTable':prtLocalizationTable,'prtLocalizationEntry':prtLocalizationEntry,'prtLocalizationLanguage':prtLocalizationLanguage,'prtLocalizationCountry':prtLocalizationCountry,'prtLocalizationCharacterSet':prtLocalizationCharacterSet,'prtInput':prtInput,'prtInputTable':prtInputTable,'prtInputEntry':prtInputEntry,'prtInputType':prtInputType,'prtInputDimUnit':prtInputDimUnit,'prtInputMediaDimFeedDirDeclared':prtInputMediaDimFeedDirDeclared,'prtInputMediaDimXFeedDirDeclared':prtInputMediaDimXFeedDirDeclared,'prtInputMediaDimFeedDirChosen':prtInputMediaDimFeedDirChosen,'prtInputMediaDimXFeedDirChosen':prtInputMediaDimXFeedDirChosen,'prtInputCapacityUnit':prtInputCapacityUnit,'prtInputMaxCapacity':prtInputMaxCapacity,'prtInputCurrentLevel':prtInputCurrentLevel,'prtInputStatus':prtInputStatus,'prtInputMediaName':prtInputMediaName,'prtInputName':prtInputName,'prtInputVendorName':prtInputVendorName,'prtInputModel':prtInputModel,'prtInputVersion':prtInputVersion,'prtInputSerialNumber':prtInputSerialNumber,'prtInputDescription':prtInputDescription,'prtInputSecurity':prtInputSecurity,'prtInputMediaWeight':prtInputMediaWeight,'prtInputMediaType':prtInputMediaType,'prtInputMediaColor':prtInputMediaColor,'prtInputMediaFormParts':prtInputMediaFormParts,'prtInputMediaLoadTimeout':prtInputMediaLoadTimeout,'prtOutput':prtOutput,'prtOutputTable':prtOutputTable,'prtOutputEntry':prtOutputEntry,'prtOutputType':prtOutputType,'prtOutputCapacityUnit':prtOutputCapacityUnit,'prtOutputMaxCapacity':prtOutputMaxCapacity,'prtOutputRemainingCapacity':prtOutputRemainingCapacity,'prtOutputStatus':prtOutputStatus,'prtOutputName':prtOutputName,'prtOutputVendorName':prtOutputVendorName,'prtOutputModel':prtOutputModel,'prtOutputVersion':prtOutputVersion,'prtOutputSerialNumber':prtOutputSerialNumber,'prtOutputDescription':prtOutputDescription,'prtOutputSecurity':prtOutputSecurity,'prtOutputDimUnit':prtOutputDimUnit,'prtOutputMaxDimFeedDir':prtOutputMaxDimFeedDir,'prtOutputMaxDimXFeedDir':prtOutputMaxDimXFeedDir,'prtOutputMinDimFeedDir':prtOutputMinDimFeedDir,'prtOutputMinDimXFeedDir':prtOutputMinDimXFeedDir,'prtOutputStackingOrder':prtOutputStackingOrder,'prtOutputPageDeliveryOrientation':prtOutputPageDeliveryOrientation,'prtOutputBursting':prtOutputBursting,'prtOutputDecollating':prtOutputDecollating,'prtOutputPageCollated':prtOutputPageCollated,'prtOutputOffsetStacking':prtOutputOffsetStacking,'prtMarker':prtMarker,'prtMarkerTable':prtMarkerTable,'prtMarkerEntry':prtMarkerEntry,'prtMarkerMarkTech':prtMarkerMarkTech,'prtMarkerCounterUnit':prtMarkerCounterUnit,'prtMarkerLifeCount':prtMarkerLifeCount,'prtMarkerPowerOnCount':prtMarkerPowerOnCount,'prtMarkerProcessColorants':prtMarkerProcessColorants,'prtMarkerSpotColorants':prtMarkerSpotColorants,'prtMarkerAddressabilityUnit':prtMarkerAddressabilityUnit,'prtMarkerAddressabilityFeedDir':prtMarkerAddressabilityFeedDir,'prtMarkerAddressabilityXFeedDir':prtMarkerAddressabilityXFeedDir,'prtMarkerNorthMargin':prtMarkerNorthMargin,'prtMarkerSouthMargin':prtMarkerSouthMargin,'prtMarkerWestMargin':prtMarkerWestMargin,'prtMarkerEastMargin':prtMarkerEastMargin,'prtMarkerStatus':prtMarkerStatus,'prtMarkerSupplies':prtMarkerSupplies,'prtMarkerSuppliesTable':prtMarkerSuppliesTable,'prtMarkerSuppliesEntry':prtMarkerSuppliesEntry,'prtMarkerSuppliesMarkerIndex':prtMarkerSuppliesMarkerIndex,'prtMarkerSuppliesColorantIndex':prtMarkerSuppliesColorantIndex,'prtMarkerSuppliesClass':prtMarkerSuppliesClass,'prtMarkerSuppliesType':prtMarkerSuppliesType,'prtMarkerSuppliesDescription':prtMarkerSuppliesDescription,'prtMarkerSuppliesSupplyUnit':prtMarkerSuppliesSupplyUnit,'prtMarkerSuppliesMaxCapacity':prtMarkerSuppliesMaxCapacity,'prtMarkerSuppliesLevel':prtMarkerSuppliesLevel,'prtMarkerColorant':prtMarkerColorant,'prtMarkerColorantTable':prtMarkerColorantTable,'prtMarkerColorantEntry':prtMarkerColorantEntry,'prtMarkerColorantMarkerIndex':prtMarkerColorantMarkerIndex,'prtMarkerColorantRole':prtMarkerColorantRole,'prtMarkerColorantValue':prtMarkerColorantValue,'prtMarkerColorantTonality':prtMarkerColorantTonality,'prtMediaPath':prtMediaPath,'prtMediaPathTable':prtMediaPathTable,'prtMediaPathEntry':prtMediaPathEntry,'prtMediaPathMaxSpeedPrintUnit':prtMediaPathMaxSpeedPrintUnit,'prtMediaPathMediaSizeUnit':prtMediaPathMediaSizeUnit,'prtMediaPathMaxSpeed':prtMediaPathMaxSpeed,'prtMediaPathMaxMediaFeedDir':prtMediaPathMaxMediaFeedDir,'prtMediaPathMaxMediaXFeedDir':prtMediaPathMaxMediaXFeedDir,'prtMediaPathMinMediaFeedDir':prtMediaPathMinMediaFeedDir,'prtMediaPathMinMediaXFeedDir':prtMediaPathMinMediaXFeedDir,'prtMediaPathType':prtMediaPathType,'prtMediaPathDescription':prtMediaPathDescription,'prtMediaPathStatus':prtMediaPathStatus,'prtChannel':prtChannel,'prtChannelTable':prtChannelTable,'prtChannelEntry':prtChannelEntry,'prtChannelType':prtChannelType,'prtChannelProtocolVersion':prtChannelProtocolVersion,'prtChannelCurrentJobCntlLangIndex':prtChannelCurrentJobCntlLangIndex,'prtChannelDefaultPageDescLangIndex':prtChannelDefaultPageDescLangIndex,'prtChannelState':prtChannelState,'prtChannelIfIndex':prtChannelIfIndex,'prtChannelStatus':prtChannelStatus,'prtChannelInformation':prtChannelInformation,'prtInterpreter':prtInterpreter,'prtInterpreterTable':prtInterpreterTable,'prtInterpreterEntry':prtInterpreterEntry,'prtInterpreterLangFamily':prtInterpreterLangFamily,'prtInterpreterLangLevel':prtInterpreterLangLevel,'prtInterpreterLangVersion':prtInterpreterLangVersion,'prtInterpreterDescription':prtInterpreterDescription,'prtInterpreterVersion':prtInterpreterVersion,'prtInterpreterDefaultOrientation':prtInterpreterDefaultOrientation,'prtInterpreterFeedAddressability':prtInterpreterFeedAddressability,'prtInterpreterXFeedAddressability':prtInterpreterXFeedAddressability,'prtInterpreterDefaultCharSetIn':prtInterpreterDefaultCharSetIn,'prtInterpreterDefaultCharSetOut':prtInterpreterDefaultCharSetOut,'prtInterpreterTwoWay':prtInterpreterTwoWay,'prtConsoleDisplayBuffer':prtConsoleDisplayBuffer,'prtConsoleDisplayBufferTable':prtConsoleDisplayBufferTable,'prtConsoleDisplayBufferEntry':prtConsoleDisplayBufferEntry,'prtConsoleDisplayBufferText':prtConsoleDisplayBufferText,'private':private,'enterprises':enterprises,'hpPrintServer':hpPrintServer,'nm':nm,'nm-system':nm_system,'netPeripheral':netPeripheral,'netPrinter':netPrinter,'generalDeviceStatus':generalDeviceStatus,'gdStatusEntry':gdStatusEntry,'gdStatusLineState':gdStatusLineState,'gdStatusPaperOut':gdStatusPaperOut,'gdStatusPaperJam':gdStatusPaperJam,'gdStatusBusy':gdStatusBusy,'gdStatusWait':gdStatusWait,'gdStatusInitialize':gdStatusInitialize,'gdStatusDoorOpen':gdStatusDoorOpen,'gdStatusPrinting':gdStatusPrinting,'gdStatusPaperOutput':gdStatusPaperOutput,'gdStatusDisplay':gdStatusDisplay,'gdStatusId':gdStatusId,'gdStatusJobTimeout':gdStatusJobTimeout,'gdPasswords':gdPasswords,'netPML':netPML,'netPMLmgmt':netPMLmgmt,'device':device,'device-system':device_system,'settings-system':settings_system,'energy-star':energy_star,'sleep-mode':sleep_mode,'speed-energy-usage':speed_energy_usage,'start-engine-early-warmup':start_engine_early_warmup,'enable-engine-early-warmup':enable_engine_early_warmup,'status-system':status_system,'install-date':install_date,'date-and-time':date_and_time,'id':id,'model-number':model_number,'model-name':model_name,'serial-number':serial_number,'fw-rom-datecode':fw_rom_datecode,'fw-rom-revision':fw_rom_revision,'device-name':device_name,'device-location':device_location,'asset-number':asset_number,'test':test,'print-internal-page':print_internal_page,'job':job,'settings-job':settings_job,'cancel-job':cancel_job,'encryption-password-type':encryption_password_type,'encryption-password-max-length':encryption_password_max_length,'encryption-password-min-length':encryption_password_min_length,'job-storage-supported':job_storage_supported,'job-storage-type':job_storage_type,'job-storage-mode':job_storage_mode,'job-storage-available':job_storage_available,'job-storage-encryption':job_storage_encryption,'active-print-jobs':active_print_jobs,'job-being-parsed':job_being_parsed,'current-job-parsing-id':current_job_parsing_id,'errorlog':errorlog,'error1':error1,'error1-time-stamp':error1_time_stamp,'error1-code':error1_code,'error1-date-time':error1_date_time,'error2':error2,'error2-time-stamp':error2_time_stamp,'error2-code':error2_code,'error2-date-time':error2_date_time,'error3':error3,'error3-time-stamp':error3_time_stamp,'error3-code':error3_code,'error3-date-time':error3_date_time,'error4':error4,'error4-time-stamp':error4_time_stamp,'error4-code':error4_code,'error4-date-time':error4_date_time,'error5':error5,'error5-time-stamp':error5_time_stamp,'error5-code':error5_code,'error5-date-time':error5_date_time,'error6':error6,'error6-time-stamp':error6_time_stamp,'error6-code':error6_code,'error6-date-time':error6_date_time,'error7':error7,'error7-time-stamp':error7_time_stamp,'error7-code':error7_code,'error7-date-time':error7_date_time,'error8':error8,'error8-time-stamp':error8_time_stamp,'error8-code':error8_code,'error8-date-time':error8_date_time,'error9':error9,'error9-time-stamp':error9_time_stamp,'error9-code':error9_code,'error9-date-time':error9_date_time,'error10':error10,'error10-time-stamp':error10_time_stamp,'error10-code':error10_code,'error10-date-time':error10_date_time,'error11':error11,'error11-time-stamp':error11_time_stamp,'error11-code':error11_code,'error11-date-time':error11_date_time,'error12':error12,'error12-time-stamp':error12_time_stamp,'error12-code':error12_code,'error12-date-time':error12_date_time,'error13':error13,'error13-time-stamp':error13_time_stamp,'error13-code':error13_code,'error13-date-time':error13_date_time,'error14':error14,'error14-time-stamp':error14_time_stamp,'error14-code':error14_code,'error14-date-time':error14_date_time,'error15':error15,'error15-time-stamp':error15_time_stamp,'error15-code':error15_code,'error15-date-time':error15_date_time,'accounting':accounting,'printer-accounting':printer_accounting,'printed-media-usage':printed_media_usage,'printed-media-simplex-count':printed_media_simplex_count,'printed-media-duplex-count':printed_media_duplex_count,'usage-printer-total-charge':usage_printer_total_charge,'usage-average-toner-coverage':usage_average_toner_coverage,'usage-staple-count':usage_staple_count,'usage-printer-mono-total-charge':usage_printer_mono_total_charge,'usage-printer-color-total-charge':usage_printer_color_total_charge,'print-meter-equivalent-impression-count':print_meter_equivalent_impression_count,'scanner-accounting':scanner_accounting,'usage-scanner-total-charge':usage_scanner_total_charge,'printer-color-accounting':printer_color_accounting,'printed-media-color-usage':printed_media_color_usage,'printed-media-color-simplex-count':printed_media_color_simplex_count,'printed-media-color-duplex-count':printed_media_color_duplex_count,'source-subsystem':source_subsystem,'scanner':scanner,'settings-scanner':settings_scanner,'scanner-accessory-adf-sheet-count':scanner_accessory_adf_sheet_count,'scanner-accessory-flatbed-scan-count':scanner_accessory_flatbed_scan_count,'scanner-accessory-copy-job-scan-count':scanner_accessory_copy_job_scan_count,'scanner-accessory-send-job-scan-count':scanner_accessory_send_job_scan_count,'scanner-accessory-total-copy-pages-printed':scanner_accessory_total_copy_pages_printed,'scan-to-folder-count':scan_to_folder_count,'fax-job-scan-count':fax_job_scan_count,'scanner-accessory-total-copy-mono-pages-printed':scanner_accessory_total_copy_mono_pages_printed,'scanner-accessory-total-copy-color-pages-printed':scanner_accessory_total_copy_color_pages_printed,'processing-subsystem':processing_subsystem,'pdl':pdl,'pdl-pcl':pdl_pcl,'pcl-total-page-count':pcl_total_page_count,'pdl-postscript':pdl_postscript,'postscript-total-page-count':postscript_total_page_count,'fax-proc-sub':fax_proc_sub,'settings-fax-proc-sub':settings_fax_proc_sub,'fax-print-page-count':fax_print_page_count,'status-fax-proc-sub':status_fax_proc_sub,'afax-send-page-count':afax_send_page_count,'afax-recv-page-count':afax_recv_page_count,'destination-subsystem':destination_subsystem,'print-engine':print_engine,'status-prt-eng':status_prt_eng,'total-engine-page-count':total_engine_page_count,'total-mono-page-count':total_mono_page_count,'total-color-page-count':total_color_page_count,'duplex-page-count':duplex_page_count,'intray':intray,'status-intray':status_intray,'not-ready-tray-empty':not_ready_tray_empty,'intrays':intrays,'intray1':intray1,'tray1-media-size-loaded':tray1_media_size_loaded,'tray1-media-name':tray1_media_name,'tray1-custom-media-width':tray1_custom_media_width,'tray1-custom-media-length':tray1_custom_media_length,'tray1-type':tray1_type,'tray1-media-key':tray1_media_key,'intray2':intray2,'tray2-media-size-loaded':tray2_media_size_loaded,'tray2-media-name':tray2_media_name,'tray2-custom-media-width':tray2_custom_media_width,'tray2-custom-media-length':tray2_custom_media_length,'tray2-type':tray2_type,'tray2-media-key':tray2_media_key,'intray3':intray3,'tray3-media-size-loaded':tray3_media_size_loaded,'tray3-media-name':tray3_media_name,'tray3-custom-media-width':tray3_custom_media_width,'tray3-custom-media-length':tray3_custom_media_length,'tray3-type':tray3_type,'tray3-media-key':tray3_media_key,'intray5':intray5,'tray5-media-size-loaded':tray5_media_size_loaded,'tray5-media-name':tray5_media_name,'tray5-custom-media-width':tray5_custom_media_width,'tray5-custom-media-length':tray5_custom_media_length,'tray5-type':tray5_type,'tray5-media-key':tray5_media_key,'print-media':print_media,'settings-print-media':settings_print_media,'media-names-enabled':media_names_enabled,'media-info':media_info,'media1':media1,'media1-name':media1_name,'media2':media2,'media2-name':media2_name,'media3':media3,'media3-name':media3_name,'media4':media4,'media4-name':media4_name,'media5':media5,'media5-name':media5_name,'media6':media6,'media6-name':media6_name,'media7':media7,'media7-name':media7_name,'media8':media8,'media8-name':media8_name,'media9':media9,'media9-name':media9_name,'media10':media10,'media10-name':media10_name,'media11':media11,'media11-name':media11_name,'media12':media12,'media12-name':media12_name,'media13':media13,'media13-name':media13_name,'media14':media14,'media14-name':media14_name,'media15':media15,'media15-name':media15_name,'media16':media16,'media16-name':media16_name,'media17':media17,'media17-name':media17_name,'media18':media18,'media18-name':media18_name,'media19':media19,'media19-name':media19_name,'consumables':consumables,'consumables-1':consumables_1,'consumable-status':consumable_status,'consumable-status-cartridge-model':consumable_status_cartridge_model,'consumable-status-manufacturing-date':consumable_status_manufacturing_date,'consumable-status-serial-number':consumable_status_serial_number,'consumable-status-first-install-date':consumable_status_first_install_date,'interface':interface,'npCard':npCard,'npSys':npSys,'npSysModelNumber':npSysModelNumber,'npSysCardServices1':npSysCardServices1,'npSysCardServices2':npSysCardServices2,'npSysCardServices3':npSysCardServices3,'npCfg':npCfg,'npCfgSource':npCfgSource,'npCfgYiaddr':npCfgYiaddr,'npCfgSiaddr':npCfgSiaddr,'npCfgLogServer':npCfgLogServer,'npCfgSubnetMask':npCfgSubnetMask,'npCfgDefaultGateway':npCfgDefaultGateway,'npCfgDomainName':npCfgDomainName,'npCfgIPP':npCfgIPP,'npCfgDNSNameServerId':npCfgDNSNameServerId,'npCfgWINSNameServerIdPri':npCfgWINSNameServerIdPri,'npCfgWINSNameServerIdSec':npCfgWINSNameServerIdSec,'npCfgPasswd1':npCfgPasswd1,'npCfgLinkType':npCfgLinkType,'npCfgSnmpDefaultReadCmnty':npCfgSnmpDefaultReadCmnty,'npCfgBonjourServiceName':npCfgBonjourServiceName,'npCfgBonjourHighestPriorityService':npCfgBonjourHighestPriorityService,'npCfgBonjourDomainName':npCfgBonjourDomainName,'npCfgDNSNameServerIdSecondary':npCfgDNSNameServerIdSecondary,'npCfgIPv6ConfigState':npCfgIPv6ConfigState,'npCfgIPv6DNSAddr1':npCfgIPv6DNSAddr1,'npCfgIPv6DNSAddr2':npCfgIPv6DNSAddr2,'npCfgIPConfigPrecedence':npCfgIPConfigPrecedence,'npCfgSTAWirelessMode':npCfgSTAWirelessMode,'npCfgWiFiDirectChannelNumber':npCfgWiFiDirectChannelNumber,'npCfgWiFiDirectSSIDPrefix':npCfgWiFiDirectSSIDPrefix,'npCfgWiFiDirectSSIDSuffix':npCfgWiFiDirectSSIDSuffix,'npCfgWiFiDirectConnectionSecurity':npCfgWiFiDirectConnectionSecurity,'npCfgSysLogProtocol':npCfgSysLogProtocol,'npCfgSysLogPort':npCfgSysLogPort,'npCfgHpDAPAgentManualServerAddr':npCfgHpDAPAgentManualServerAddr,'npTcp':npTcp,'npTcpSyslogMax':npTcpSyslogMax,'npTcpAppSyslogPriority':npTcpAppSyslogPriority,'npCtl':npCtl,'npCtlSLP':npCtlSLP,'npCtlLPD':npCtlLPD,'npCtl9100':npCtl9100,'npCtlSysLog':npCtlSysLog,'npCtlSnmpVersionAccess':npCtlSnmpVersionAccess,'npCtlSnmpV3InitAccount':npCtlSnmpV3InitAccount,'npCtlBonjour':npCtlBonjour,'npCtlNetworkConnectionMode':npCtlNetworkConnectionMode,'npCtlWSDiscovery':npCtlWSDiscovery,'npCtlWSPrint':npCtlWSPrint,'npCtlLLMNR':npCtlLLMNR,'npCtlWPAD':npCtlWPAD,'npCtlFpDot11WirelessState':npCtlFpDot11WirelessState,'npCtlDot11nSTAGuardInterval':npCtlDot11nSTAGuardInterval,'npCtlDot11nSTAAMSDUAggregation':npCtlDot11nSTAAMSDUAggregation,'npCtlDot11nSTABlockACKs':npCtlDot11nSTABlockACKs,'npCtlDot11nSTAAMPDUAggregation':npCtlDot11nSTAAMPDUAggregation,'npCtlWiFiDirectSSIDBroadcast':npCtlWiFiDirectSSIDBroadcast,'npCtlWiFiDirectHidePassphrase':npCtlWiFiDirectHidePassphrase,'npCtlWiFiDirectHideSsid':npCtlWiFiDirectHideSsid,'npCtlHpDAPAgentAnnounceState':npCtlHpDAPAgentAnnounceState,'npCtlHpDAPAgentRequireTrustedAuth':npCtlHpDAPAgentRequireTrustedAuth,'npCtlDeviceMode':npCtlDeviceMode,'npCtlAirPrintStatus':npCtlAirPrintStatus,'npCtlWirelessSTAState':npCtlWirelessSTAState,'npCtlWiFiDirectState':npCtlWiFiDirectState,'npCtlAirScan':npCtlAirScan,'npCtlAirFax':npCtlAirFax,'npCtlGCPrint':npCtlGCPrint,'npCtlRebootMode':npCtlRebootMode,'npNpi':npNpi,'npNpiPeripheralAttributeEntry':npNpiPeripheralAttributeEntry,'npNpiPaeClass':npNpiPaeClass,'npNpiPaeIdentification':npNpiPaeIdentification,'npIpx':npIpx,'npIpxSapInfo':npIpxSapInfo,'npPort':npPort,'npPortNumPorts':npPortNumPorts,'npDhcp':npDhcp,'npDhcpFQDNBehavior':npDhcpFQDNBehavior,'npWeb':npWeb,'npWebProxyServerId':npWebProxyServerId,'npWebProxyServerPort':npWebProxyServerPort,'npWebProxyUserName':npWebProxyUserName,'npWebProxyUserPasswd':npWebProxyUserPasswd,'npSecurity':npSecurity,'npSecurityDot11ServerAuthentication':npSecurityDot11ServerAuthentication,'npSecurityDot1xEapMd5Identity':npSecurityDot1xEapMd5Identity,'npSecurityDot1xTLSAuthServerId':npSecurityDot1xTLSAuthServerId,'npSecurityPublicKey':npSecurityPublicKey,'npSecurityDot11EncryptedDot1xEapMd5Secret':npSecurityDot11EncryptedDot1xEapMd5Secret,'npSecurityDot11EncryptedWEPKeyTable':npSecurityDot11EncryptedWEPKeyTable,'npSecurityDot11EncryptedWEPKeyEntry':npSecurityDot11EncryptedWEPKeyEntry,'npSecurityDot11EncryptedWEPKey':npSecurityDot11EncryptedWEPKey,'npSecurityDot11SignalStrength':npSecurityDot11SignalStrength,'npSecurityDot11SSIDTable':npSecurityDot11SSIDTable,'npSecurityDot11SSIDEntry':npSecurityDot11SSIDEntry,'npSecurityDot11SSID':npSecurityDot11SSID,'npSecurityDot11SSIDTableNumEntries':npSecurityDot11SSIDTableNumEntries,'npSecuritySnmpV3EncryptedUserName':npSecuritySnmpV3EncryptedUserName,'npSecuritySnmpV3AuthKeyPassPhrase':npSecuritySnmpV3AuthKeyPassPhrase,'npSecuritySnmpV3PrivKeyPassPhrase':npSecuritySnmpV3PrivKeyPassPhrase,'npSecurityDot11ExactMatchServerId':npSecurityDot11ExactMatchServerId,'npSecurityDot11EncryptionStrength':npSecurityDot11EncryptionStrength,'npSecuritySslRedirection':npSecuritySslRedirection,'npSecurityServicesSupported':npSecurityServicesSupported,'npSecurityDot11Encryption':npSecurityDot11Encryption,'npSecurityDot11MulticastCipher':npSecurityDot11MulticastCipher,'npSecurityDot11EncryptedWPAConfigPSKPassPhrase':npSecurityDot11EncryptedWPAConfigPSKPassPhrase,'npSecuritySslEncryptionStrength':npSecuritySslEncryptionStrength,'npSecurityDot11DynamicEncryption':npSecurityDot11DynamicEncryption,'npSecurityDot11LinkAuthentication':npSecurityDot11LinkAuthentication,'npSecuritySnmpV3AuthAlgorithm':npSecuritySnmpV3AuthAlgorithm,'npSecuritySnmpV3PrivAlgorithm':npSecuritySnmpV3PrivAlgorithm,'npSecuritySnmpV3PassPhrase':npSecuritySnmpV3PassPhrase,'npSecurityWirelessDirectEncryptedPassPhrase':npSecurityWirelessDirectEncryptedPassPhrase,'npSecurityDot1xFailSafe':npSecurityDot1xFailSafe,'npSecuritySSLProtocol':npSecuritySSLProtocol,'trap':trap,'trapDest':trapDest,'trapDestinationNum':trapDestinationNum,'trapTest':trapTest,'trapSource':trapSource,'trapFilterDelay':trapFilterDelay,'trapFQDNNum':trapFQDNNum,'snmpAccess':snmpAccess,'community':community,'setCommunityName':setCommunityName,'getCommunityName':getCommunityName,'ppmMIB':ppmMIB,'ppmMIBObjects':ppmMIBObjects,'ppmGeneral':ppmGeneral,'ppmGeneralNaturalLanguage':ppmGeneralNaturalLanguage,'ppmGeneralNumberOfPrinters':ppmGeneralNumberOfPrinters,'ppmGeneralNumberOfPorts':ppmGeneralNumberOfPorts,'ppmPrinter':ppmPrinter,'ppmPrinterTable':ppmPrinterTable,'ppmPrinterEntry':ppmPrinterEntry,'ppmPrinterName':ppmPrinterName,'ppmPrinterIEEE1284DeviceId':ppmPrinterIEEE1284DeviceId,'ppmPrinterNumberOfPorts':ppmPrinterNumberOfPorts,'ppmPrinterPreferredPortIndex':ppmPrinterPreferredPortIndex,'ppmPrinterHrDeviceIndex':ppmPrinterHrDeviceIndex,'ppmPrinterSnmpCommunityName':ppmPrinterSnmpCommunityName,'ppmPrinterSnmpQueryEnabled':ppmPrinterSnmpQueryEnabled,'ppmPort':ppmPort,'ppmPortTable':ppmPortTable,'ppmPortEntry':ppmPortEntry,'ppmPortEnabled':ppmPortEnabled,'ppmPortName':ppmPortName,'ppmPortServiceNameOrURI':ppmPortServiceNameOrURI,'ppmPortProtocolType':ppmPortProtocolType,'ppmPortProtocolTargetPort':ppmPortProtocolTargetPort,'ppmPortProtocolAltSourceEnabled':ppmPortProtocolAltSourceEnabled,'ppmPortPrtChannelIndex':ppmPortPrtChannelIndex,'ppmPortLprByteCountEnabled':ppmPortLprByteCountEnabled,'snmpV2':snmpV2,'snmpModules':snmpModules,'snmpFrameworkMIB':snmpFrameworkMIB,'snmpFrameworkMIBObjects':snmpFrameworkMIBObjects,'snmpEngine':snmpEngine,'snmpEngineID':snmpEngineID,'snmpEngineBoots':snmpEngineBoots,'snmpEngineTime':snmpEngineTime,'snmpEngineMaxMessageSize':snmpEngineMaxMessageSize,'snmpMPDMIB':snmpMPDMIB,'snmpMPDMIBObjects':snmpMPDMIBObjects,'snmpMPDStats':snmpMPDStats,'snmpUnknownSecurityModels':snmpUnknownSecurityModels,'snmpInvalidMsgs':snmpInvalidMsgs,'snmpUnknownPDUHandlers':snmpUnknownPDUHandlers,'snmpUsmMIB':snmpUsmMIB,'usmMIBObjects':usmMIBObjects,'usmStats':usmStats,'usmStatsUnsupportedSecLevels':usmStatsUnsupportedSecLevels,'usmStatsNotInTimeWindows':usmStatsNotInTimeWindows,'usmStatsUnknownUserNames':usmStatsUnknownUserNames,'usmStatsUnknownEngineIDs':usmStatsUnknownEngineIDs,'usmStatsWrongDigests':usmStatsWrongDigests,'usmStatsDecryptionErrors':usmStatsDecryptionErrors,'usmUser':usmUser,'usmUserSpinLock':usmUserSpinLock,'usmUserTable':usmUserTable,'usmUserEntry':usmUserEntry,'usmUserSecurityName':usmUserSecurityName,'usmUserCloneFrom':usmUserCloneFrom,'usmUserAuthProtocol':usmUserAuthProtocol,'usmUserAuthKeyChange':usmUserAuthKeyChange,'usmUserOwnAuthKeyChange':usmUserOwnAuthKeyChange,'usmUserPrivProtocol':usmUserPrivProtocol,'usmUserPrivKeyChange':usmUserPrivKeyChange,'usmUserOwnPrivKeyChange':usmUserOwnPrivKeyChange,'usmUserPublic':usmUserPublic,'usmUserStorageType':usmUserStorageType,'usmUserStatus':usmUserStatus,'snmpVacmMIB':snmpVacmMIB,'vacmMIBObjects':vacmMIBObjects,'vacmContextTable':vacmContextTable,'vacmContextEntry':vacmContextEntry,'vacmContextName':vacmContextName,'vacmSecurityToGroupTable':vacmSecurityToGroupTable,'vacmSecurityToGroupEntry':vacmSecurityToGroupEntry,'vacmGroupName':vacmGroupName,'vacmSecurityToGroupStorageType':vacmSecurityToGroupStorageType,'vacmSecurityToGroupStatus':vacmSecurityToGroupStatus,'vacmAccessTable':vacmAccessTable,'vacmAccessEntry':vacmAccessEntry,'vacmAccessContextMatch':vacmAccessContextMatch,'vacmAccessReadViewName':vacmAccessReadViewName,'vacmAccessWriteViewName':vacmAccessWriteViewName,'vacmAccessNotifyViewName':vacmAccessNotifyViewName,'vacmAccessStorageType':vacmAccessStorageType,'vacmAccessStatus':vacmAccessStatus,'vacmMIBViews':vacmMIBViews,'vacmViewSpinLock':vacmViewSpinLock,'vacmViewTreeFamilyTable':vacmViewTreeFamilyTable,'vacmViewTreeFamilyEntry':vacmViewTreeFamilyEntry,'vacmViewTreeFamilyMask':vacmViewTreeFamilyMask,'vacmViewTreeFamilyType':vacmViewTreeFamilyType,'vacmViewTreeFamilyStorageType':vacmViewTreeFamilyStorageType,'vacmViewTreeFamilyStatus':vacmViewTreeFamilyStatus})