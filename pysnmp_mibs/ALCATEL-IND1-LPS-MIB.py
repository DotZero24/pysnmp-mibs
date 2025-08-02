_AB='learnedPortSecurityL2MacAddressGroup'
_AA='learnedPortSecurityTrapObjectsGroup'
_A9='learnedPortSecurityTrapsGroup'
_A8='learnedPortSecurityGlobGroup'
_A7='learnedPortSecurityMacAddressGroup'
_A6='learnedPortSecurityGroup'
_A5='lpsLearnMac'
_A4='lpsPortUpAfterLearningWindowExpiredTrap'
_A3='lpsViolationTrap'
_A2='lpsMacAddressRowStatus'
_A1='lpsL2MacAddressRowStatus'
_A0='lpsL2MacAddressLearnType'
_z='lpsLearningWindowPseudoMacMove'
_y='lpsLearningWindowLearnAsStatic'
_x='lpsLearningWindowBootupStatus'
_w='lpsLearningWindowNoAging'
_v='lpsConvertToStatic'
_u='lpsLearningWindowTimeWithStaticConversion'
_t='lpsLearningWindowTime'
_s='lpsMacAddressLearnType'
_r='lpsLearnTrapThreshold'
_q='lpsViolatingMac'
_p='lpsMaxFilteredMacNum'
_o='lpsRelease'
_n='lpsOperStatus'
_m='lpsAdminStatus'
_l='lpsHiMacRange'
_k='lpsLoMacRange'
_j='lpsMaxMacNum'
_i='lpsViolationOption'
_h='not-accessible'
_g='lpsL2MacAddress'
_f='lpsL2VlanId'
_e='dynamic'
_d='configured'
_c='locked'
_b='000000000000'
_a='DisplayString'
_Z='lpsTrapViolationType'
_Y='lpsTrapViolatingMac'
_X='lpsTrapSwitchIpAddr'
_W='lpsTrapBridgeMac'
_V='lpsRowStatus'
_U='lpsMacAddress'
_T='lpsTrapSwitchVlan'
_S='MacAddress'
_R='ifIndex'
_Q='IF-MIB'
_P='systemServicesTime'
_O='systemServicesDate'
_N='lpsTrapSwitchSlice'
_M='lpsTrapSwitchPort'
_L='lpsTrapSwitchName'
_K='disable'
_J='enable'
_I='deprecated'
_H='read-only'
_G='read-write'
_F='ALCATEL-IND1-SYSTEM-MIB'
_E='accessible-for-notify'
_D='read-create'
_C='Integer32'
_B='current'
_A='ALCATEL-IND1-LPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1MacAddress,sourceLearningTraps=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1MacAddress','sourceLearningTraps')
systemServicesDate,systemServicesTime=mibBuilder.importSymbols(_F,_O,_P)
ifIndex,=mibBuilder.importSymbols(_Q,_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_a,_S,'PhysAddress','RowStatus','TextualConvention')
alcatelIND1LearnedPortSecurityMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,2))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1LearnedPortSecurityMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1LearnedPortSecurityMIBObjects=_AlcatelIND1LearnedPortSecurityMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,2,1))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBObjects.setStatus(_B)
_LearnedPortSecurityTable_Object=MibTable
learnedPortSecurityTable=_LearnedPortSecurityTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1))
if mibBuilder.loadTexts:learnedPortSecurityTable.setStatus(_B)
_LearnedPortSecurityEntry_Object=MibTableRow
learnedPortSecurityEntry=_LearnedPortSecurityEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1))
learnedPortSecurityEntry.setIndexNames((0,_Q,_R))
if mibBuilder.loadTexts:learnedPortSecurityEntry.setStatus(_B)
class _LpsViolationOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('restrict',1),('shutdown',2),('discard',3)))
_LpsViolationOption_Type.__name__=_C
_LpsViolationOption_Object=MibTableColumn
lpsViolationOption=_LpsViolationOption_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,1),_LpsViolationOption_Type())
lpsViolationOption.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsViolationOption.setStatus(_B)
class _LpsMaxMacNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_LpsMaxMacNum_Type.__name__=_C
_LpsMaxMacNum_Object=MibTableColumn
lpsMaxMacNum=_LpsMaxMacNum_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,2),_LpsMaxMacNum_Type())
lpsMaxMacNum.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsMaxMacNum.setStatus(_B)
class _LpsLoMacRange_Type(MacAddress):defaultHexValue=_b
_LpsLoMacRange_Type.__name__=_S
_LpsLoMacRange_Object=MibTableColumn
lpsLoMacRange=_LpsLoMacRange_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,3),_LpsLoMacRange_Type())
lpsLoMacRange.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsLoMacRange.setStatus(_B)
class _LpsHiMacRange_Type(MacAddress):defaultHexValue='ffffffffffff'
_LpsHiMacRange_Type.__name__=_S
_LpsHiMacRange_Object=MibTableColumn
lpsHiMacRange=_LpsHiMacRange_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,4),_LpsHiMacRange_Type())
lpsHiMacRange.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsHiMacRange.setStatus(_B)
class _LpsAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_c,3)))
_LpsAdminStatus_Type.__name__=_C
_LpsAdminStatus_Object=MibTableColumn
lpsAdminStatus=_LpsAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,5),_LpsAdminStatus_Type())
lpsAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsAdminStatus.setStatus(_B)
class _LpsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('securityViolated',3),(_c,4)))
_LpsOperStatus_Type.__name__=_C
_LpsOperStatus_Object=MibTableColumn
lpsOperStatus=_LpsOperStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,6),_LpsOperStatus_Type())
lpsOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:lpsOperStatus.setStatus(_B)
_LpsRowStatus_Type=RowStatus
_LpsRowStatus_Object=MibTableColumn
lpsRowStatus=_LpsRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,7),_LpsRowStatus_Type())
lpsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsRowStatus.setStatus(_B)
class _LpsRelease_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('release',1))
_LpsRelease_Type.__name__=_C
_LpsRelease_Object=MibTableColumn
lpsRelease=_LpsRelease_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,8),_LpsRelease_Type())
lpsRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsRelease.setStatus(_B)
class _LpsMaxFilteredMacNum_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LpsMaxFilteredMacNum_Type.__name__=_C
_LpsMaxFilteredMacNum_Object=MibTableColumn
lpsMaxFilteredMacNum=_LpsMaxFilteredMacNum_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,9),_LpsMaxFilteredMacNum_Type())
lpsMaxFilteredMacNum.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsMaxFilteredMacNum.setStatus(_B)
class _LpsLearnTrapThreshold_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_LpsLearnTrapThreshold_Type.__name__=_C
_LpsLearnTrapThreshold_Object=MibTableColumn
lpsLearnTrapThreshold=_LpsLearnTrapThreshold_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,10),_LpsLearnTrapThreshold_Type())
lpsLearnTrapThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsLearnTrapThreshold.setStatus(_B)
class _LpsViolatingMac_Type(MacAddress):defaultHexValue=_b
_LpsViolatingMac_Type.__name__=_S
_LpsViolatingMac_Object=MibTableColumn
lpsViolatingMac=_LpsViolatingMac_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,1,1,11),_LpsViolatingMac_Type())
lpsViolatingMac.setMaxAccess(_H)
if mibBuilder.loadTexts:lpsViolatingMac.setStatus(_B)
_LearnedPortSecurityMacAddressTable_Object=MibTable
learnedPortSecurityMacAddressTable=_LearnedPortSecurityMacAddressTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,2))
if mibBuilder.loadTexts:learnedPortSecurityMacAddressTable.setStatus(_I)
_LearnedPortSecurityMacAddressEntry_Object=MibTableRow
learnedPortSecurityMacAddressEntry=_LearnedPortSecurityMacAddressEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,2,1))
learnedPortSecurityMacAddressEntry.setIndexNames((0,_Q,_R),(0,_A,_U))
if mibBuilder.loadTexts:learnedPortSecurityMacAddressEntry.setStatus(_I)
_LpsMacAddress_Type=MacAddress
_LpsMacAddress_Object=MibTableColumn
lpsMacAddress=_LpsMacAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,2,1,1),_LpsMacAddress_Type())
lpsMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:lpsMacAddress.setStatus(_I)
class _LpsMacAddressLearnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_LpsMacAddressLearnType_Type.__name__=_C
_LpsMacAddressLearnType_Object=MibTableColumn
lpsMacAddressLearnType=_LpsMacAddressLearnType_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,2,1,2),_LpsMacAddressLearnType_Type())
lpsMacAddressLearnType.setMaxAccess(_H)
if mibBuilder.loadTexts:lpsMacAddressLearnType.setStatus(_I)
_LpsMacAddressRowStatus_Type=RowStatus
_LpsMacAddressRowStatus_Object=MibTableColumn
lpsMacAddressRowStatus=_LpsMacAddressRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,2,1,3),_LpsMacAddressRowStatus_Type())
lpsMacAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsMacAddressRowStatus.setStatus(_I)
_LearnedPortSecurityGlobalGroup_ObjectIdentity=ObjectIdentity
learnedPortSecurityGlobalGroup=_LearnedPortSecurityGlobalGroup_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,3))
class _LpsLearningWindowTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsLearningWindowTime_Type.__name__=_C
_LpsLearningWindowTime_Object=MibScalar
lpsLearningWindowTime=_LpsLearningWindowTime_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,3,1),_LpsLearningWindowTime_Type())
lpsLearningWindowTime.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowTime.setStatus(_B)
class _LpsLearningWindowTimeWithStaticConversion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LpsLearningWindowTimeWithStaticConversion_Type.__name__=_C
_LpsLearningWindowTimeWithStaticConversion_Object=MibScalar
lpsLearningWindowTimeWithStaticConversion=_LpsLearningWindowTimeWithStaticConversion_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,3,2),_LpsLearningWindowTimeWithStaticConversion_Type())
lpsLearningWindowTimeWithStaticConversion.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowTimeWithStaticConversion.setStatus(_B)
class _LpsConvertToStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1001,17000))
_LpsConvertToStatic_Type.__name__=_C
_LpsConvertToStatic_Object=MibScalar
lpsConvertToStatic=_LpsConvertToStatic_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,3,3),_LpsConvertToStatic_Type())
lpsConvertToStatic.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsConvertToStatic.setStatus(_B)
class _LpsLearningWindowNoAging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LpsLearningWindowNoAging_Type.__name__=_C
_LpsLearningWindowNoAging_Object=MibScalar
lpsLearningWindowNoAging=_LpsLearningWindowNoAging_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,3,4),_LpsLearningWindowNoAging_Type())
lpsLearningWindowNoAging.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowNoAging.setStatus(_B)
class _LpsLearningWindowBootupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LpsLearningWindowBootupStatus_Type.__name__=_C
_LpsLearningWindowBootupStatus_Object=MibScalar
lpsLearningWindowBootupStatus=_LpsLearningWindowBootupStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,3,5),_LpsLearningWindowBootupStatus_Type())
lpsLearningWindowBootupStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowBootupStatus.setStatus(_B)
class _LpsLearningWindowExpiryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LpsLearningWindowExpiryStatus_Type.__name__=_C
_LpsLearningWindowExpiryStatus_Object=MibScalar
lpsLearningWindowExpiryStatus=_LpsLearningWindowExpiryStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,3,6),_LpsLearningWindowExpiryStatus_Type())
lpsLearningWindowExpiryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:lpsLearningWindowExpiryStatus.setStatus(_B)
class _LpsLearningWindowLearnAsStatic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LpsLearningWindowLearnAsStatic_Type.__name__=_C
_LpsLearningWindowLearnAsStatic_Object=MibScalar
lpsLearningWindowLearnAsStatic=_LpsLearningWindowLearnAsStatic_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,3,7),_LpsLearningWindowLearnAsStatic_Type())
lpsLearningWindowLearnAsStatic.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowLearnAsStatic.setStatus(_B)
class _LpsLearningWindowPseudoMacMove_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_LpsLearningWindowPseudoMacMove_Type.__name__=_C
_LpsLearningWindowPseudoMacMove_Object=MibScalar
lpsLearningWindowPseudoMacMove=_LpsLearningWindowPseudoMacMove_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,3,8),_LpsLearningWindowPseudoMacMove_Type())
lpsLearningWindowPseudoMacMove.setMaxAccess(_G)
if mibBuilder.loadTexts:lpsLearningWindowPseudoMacMove.setStatus(_B)
_LearnedPortSecurityL2MacAddressTable_Object=MibTable
learnedPortSecurityL2MacAddressTable=_LearnedPortSecurityL2MacAddressTable_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,4))
if mibBuilder.loadTexts:learnedPortSecurityL2MacAddressTable.setStatus(_B)
_LearnedPortSecurityL2MacAddressEntry_Object=MibTableRow
learnedPortSecurityL2MacAddressEntry=_LearnedPortSecurityL2MacAddressEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,4,1))
learnedPortSecurityL2MacAddressEntry.setIndexNames((0,_Q,_R),(0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:learnedPortSecurityL2MacAddressEntry.setStatus(_B)
class _LpsL2VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_LpsL2VlanId_Type.__name__=_C
_LpsL2VlanId_Object=MibTableColumn
lpsL2VlanId=_LpsL2VlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,4,1,1),_LpsL2VlanId_Type())
lpsL2VlanId.setMaxAccess(_h)
if mibBuilder.loadTexts:lpsL2VlanId.setStatus(_B)
_LpsL2MacAddress_Type=MacAddress
_LpsL2MacAddress_Object=MibTableColumn
lpsL2MacAddress=_LpsL2MacAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,4,1,2),_LpsL2MacAddress_Type())
lpsL2MacAddress.setMaxAccess(_h)
if mibBuilder.loadTexts:lpsL2MacAddress.setStatus(_B)
class _LpsL2MacAddressLearnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_d,1),(_e,2),('filtered',3),('quarantined',4)))
_LpsL2MacAddressLearnType_Type.__name__=_C
_LpsL2MacAddressLearnType_Object=MibTableColumn
lpsL2MacAddressLearnType=_LpsL2MacAddressLearnType_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,4,1,3),_LpsL2MacAddressLearnType_Type())
lpsL2MacAddressLearnType.setMaxAccess(_H)
if mibBuilder.loadTexts:lpsL2MacAddressLearnType.setStatus(_B)
_LpsL2MacAddressRowStatus_Type=RowStatus
_LpsL2MacAddressRowStatus_Object=MibTableColumn
lpsL2MacAddressRowStatus=_LpsL2MacAddressRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,8,2,1,4,1,4),_LpsL2MacAddressRowStatus_Type())
lpsL2MacAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lpsL2MacAddressRowStatus.setStatus(_B)
_AlcatelIND1LearnedPortSecurityMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1LearnedPortSecurityMIBConformance=_AlcatelIND1LearnedPortSecurityMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,2,2))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBConformance.setStatus(_B)
_AlcatelIND1LearnedPortSecurityMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1LearnedPortSecurityMIBGroups=_AlcatelIND1LearnedPortSecurityMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,2,2,1))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBGroups.setStatus(_B)
_AlcatelIND1LearnedPortSecurityMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1LearnedPortSecurityMIBCompliances=_AlcatelIND1LearnedPortSecurityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,8,2,2,2))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBCompliances.setStatus(_B)
_LpsTraps_ObjectIdentity=ObjectIdentity
lpsTraps=_LpsTraps_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,9,0,2))
_LpsTrapsDesc_ObjectIdentity=ObjectIdentity
lpsTrapsDesc=_LpsTrapsDesc_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,1))
_LpsTrapsObj_ObjectIdentity=ObjectIdentity
lpsTrapsObj=_LpsTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,2))
class _LpsTrapSwitchName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LpsTrapSwitchName_Type.__name__=_a
_LpsTrapSwitchName_Object=MibScalar
lpsTrapSwitchName=_LpsTrapSwitchName_Object((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,2,1),_LpsTrapSwitchName_Type())
lpsTrapSwitchName.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsTrapSwitchName.setStatus(_B)
_LpsTrapSwitchIpAddr_Type=IpAddress
_LpsTrapSwitchIpAddr_Object=MibScalar
lpsTrapSwitchIpAddr=_LpsTrapSwitchIpAddr_Object((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,2,2),_LpsTrapSwitchIpAddr_Type())
lpsTrapSwitchIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsTrapSwitchIpAddr.setStatus(_B)
_LpsTrapSwitchSlice_Type=Integer32
_LpsTrapSwitchSlice_Object=MibScalar
lpsTrapSwitchSlice=_LpsTrapSwitchSlice_Object((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,2,3),_LpsTrapSwitchSlice_Type())
lpsTrapSwitchSlice.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsTrapSwitchSlice.setStatus(_B)
_LpsTrapSwitchPort_Type=Integer32
_LpsTrapSwitchPort_Object=MibScalar
lpsTrapSwitchPort=_LpsTrapSwitchPort_Object((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,2,4),_LpsTrapSwitchPort_Type())
lpsTrapSwitchPort.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsTrapSwitchPort.setStatus(_B)
_LpsTrapViolatingMac_Type=MacAddress
_LpsTrapViolatingMac_Object=MibScalar
lpsTrapViolatingMac=_LpsTrapViolatingMac_Object((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,2,5),_LpsTrapViolatingMac_Type())
lpsTrapViolatingMac.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsTrapViolatingMac.setStatus(_B)
class _LpsTrapViolationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('learnWindowExpired',1),('macOutOfRange',2),('macsLearnLimitReached',3)))
_LpsTrapViolationType_Type.__name__=_C
_LpsTrapViolationType_Object=MibScalar
lpsTrapViolationType=_LpsTrapViolationType_Object((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,2,6),_LpsTrapViolationType_Type())
lpsTrapViolationType.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsTrapViolationType.setStatus(_B)
_LpsTrapSwitchVlan_Type=Integer32
_LpsTrapSwitchVlan_Object=MibScalar
lpsTrapSwitchVlan=_LpsTrapSwitchVlan_Object((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,2,7),_LpsTrapSwitchVlan_Type())
lpsTrapSwitchVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsTrapSwitchVlan.setStatus(_B)
_LpsTrapBridgeMac_Type=Integer32
_LpsTrapBridgeMac_Object=MibScalar
lpsTrapBridgeMac=_LpsTrapBridgeMac_Object((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,2,8),_LpsTrapBridgeMac_Type())
lpsTrapBridgeMac.setMaxAccess(_E)
if mibBuilder.loadTexts:lpsTrapBridgeMac.setStatus(_B)
learnedPortSecurityGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,2,2,1,1))
learnedPortSecurityGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_V),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:learnedPortSecurityGroup.setStatus(_B)
learnedPortSecurityMacAddressGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,2,2,1,2))
learnedPortSecurityMacAddressGroup.setObjects(*((_A,_U),(_A,_s),(_A,_V)))
if mibBuilder.loadTexts:learnedPortSecurityMacAddressGroup.setStatus(_I)
learnedPortSecurityGlobGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,2,2,1,3))
learnedPortSecurityGlobGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:learnedPortSecurityGlobGroup.setStatus(_B)
learnedPortSecurityL2MacAddressGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,2,2,1,5))
learnedPortSecurityL2MacAddressGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:learnedPortSecurityL2MacAddressGroup.setStatus(_B)
learnedPortSecurityTrapObjectsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,8,2,2,1,6))
learnedPortSecurityTrapObjectsGroup.setObjects(*((_A,_W),(_A,_X),(_A,_L),(_A,_M),(_A,_N),(_A,_T),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:learnedPortSecurityTrapObjectsGroup.setStatus(_B)
lpsViolationTrap=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,1,0,1))
lpsViolationTrap.setObjects(*((_A,_L),(_A,_X),(_A,_N),(_A,_M),(_A,_Y),(_A,_Z),(_F,_O),(_F,_P),(_A,_T)))
if mibBuilder.loadTexts:lpsViolationTrap.setStatus(_B)
lpsPortUpAfterLearningWindowExpiredTrap=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,1,0,2))
lpsPortUpAfterLearningWindowExpiredTrap.setObjects(*((_A,_L),(_A,_N),(_A,_M),(_F,_O),(_F,_P)))
if mibBuilder.loadTexts:lpsPortUpAfterLearningWindowExpiredTrap.setStatus(_B)
lpsLearnMac=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,9,0,2,1,0,3))
lpsLearnMac.setObjects(*((_A,_L),(_A,_N),(_A,_M),(_A,_T),(_F,_O),(_F,_P),(_A,_W)))
if mibBuilder.loadTexts:lpsLearnMac.setStatus(_B)
learnedPortSecurityTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,8,2,2,1,4))
learnedPortSecurityTrapsGroup.setObjects(*((_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:learnedPortSecurityTrapsGroup.setStatus(_B)
alcatelIND1LearnedPortSecurityMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,8,2,2,2,1))
alcatelIND1LearnedPortSecurityMIBCompliance.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:alcatelIND1LearnedPortSecurityMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alcatelIND1LearnedPortSecurityMIB':alcatelIND1LearnedPortSecurityMIB,'alcatelIND1LearnedPortSecurityMIBObjects':alcatelIND1LearnedPortSecurityMIBObjects,'learnedPortSecurityTable':learnedPortSecurityTable,'learnedPortSecurityEntry':learnedPortSecurityEntry,_i:lpsViolationOption,_j:lpsMaxMacNum,_k:lpsLoMacRange,_l:lpsHiMacRange,_m:lpsAdminStatus,_n:lpsOperStatus,_V:lpsRowStatus,_o:lpsRelease,_p:lpsMaxFilteredMacNum,_r:lpsLearnTrapThreshold,_q:lpsViolatingMac,'learnedPortSecurityMacAddressTable':learnedPortSecurityMacAddressTable,'learnedPortSecurityMacAddressEntry':learnedPortSecurityMacAddressEntry,_U:lpsMacAddress,_s:lpsMacAddressLearnType,_A2:lpsMacAddressRowStatus,'learnedPortSecurityGlobalGroup':learnedPortSecurityGlobalGroup,_t:lpsLearningWindowTime,_u:lpsLearningWindowTimeWithStaticConversion,_v:lpsConvertToStatic,_w:lpsLearningWindowNoAging,_x:lpsLearningWindowBootupStatus,'lpsLearningWindowExpiryStatus':lpsLearningWindowExpiryStatus,_y:lpsLearningWindowLearnAsStatic,_z:lpsLearningWindowPseudoMacMove,'learnedPortSecurityL2MacAddressTable':learnedPortSecurityL2MacAddressTable,'learnedPortSecurityL2MacAddressEntry':learnedPortSecurityL2MacAddressEntry,_f:lpsL2VlanId,_g:lpsL2MacAddress,_A0:lpsL2MacAddressLearnType,_A1:lpsL2MacAddressRowStatus,'alcatelIND1LearnedPortSecurityMIBConformance':alcatelIND1LearnedPortSecurityMIBConformance,'alcatelIND1LearnedPortSecurityMIBGroups':alcatelIND1LearnedPortSecurityMIBGroups,_A6:learnedPortSecurityGroup,_A7:learnedPortSecurityMacAddressGroup,_A8:learnedPortSecurityGlobGroup,_A9:learnedPortSecurityTrapsGroup,_AB:learnedPortSecurityL2MacAddressGroup,_AA:learnedPortSecurityTrapObjectsGroup,'alcatelIND1LearnedPortSecurityMIBCompliances':alcatelIND1LearnedPortSecurityMIBCompliances,'alcatelIND1LearnedPortSecurityMIBCompliance':alcatelIND1LearnedPortSecurityMIBCompliance,'lpsTraps':lpsTraps,'lpsTrapsDesc':lpsTrapsDesc,_A3:lpsViolationTrap,_A4:lpsPortUpAfterLearningWindowExpiredTrap,_A5:lpsLearnMac,'lpsTrapsObj':lpsTrapsObj,_L:lpsTrapSwitchName,_X:lpsTrapSwitchIpAddr,_N:lpsTrapSwitchSlice,_M:lpsTrapSwitchPort,_Y:lpsTrapViolatingMac,_Z:lpsTrapViolationType,_T:lpsTrapSwitchVlan,_W:lpsTrapBridgeMac})